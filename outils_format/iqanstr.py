"""Tables de chaînes d'un projet IQANdesign (sections tag 0xc6 et 0xcb).

Contenu décompressé d'une section de chaînes :
  u8 02, u8 nombre_de_langues, puis pour chaque langue :
    u32 L1 (octets qui suivent jusqu'à la fin de la langue)
    code\\0 nom\\0 u8 drapeau
    u32 L2 (octets qui suivent jusqu'à la fin de la langue)
    u16 n, u32 décalage[n], puis n chaînes [u16 longueur avec \\0][UTF-8][\\0]
    puis un bloc de glyphes (caractères spéciaux pour les écrans, souvent un seul octet 00)
  u32 CRC32 de tout ce qui précède.
Les objets désignent une chaîne par son numéro dans la table : modifier une chaîne
la change partout où elle est utilisée (les chaînes identiques sont partagées).
"""
import struct
import zlib


class Language:
    def __init__(self, code, name, flag, strings, extra=b"\0"):
        self.code, self.name, self.flag, self.strings = code, name, flag, strings
        self.extra = extra  # glyphes des caractères spéciaux pour l'écran (souvent un seul 00)


def _cstr(b, p):
    e = b.index(b"\0", p)
    return b[p:e], e + 1


def parse(data):
    if zlib.crc32(data[:-4]) != struct.unpack("<I", data[-4:])[0]:
        raise ValueError("CRC32 de la table de chaînes incorrect")
    head, nlang = data[0], data[1]
    p, langs = 2, []
    for _ in range(nlang):
        end = p + 4 + struct.unpack_from("<I", data, p)[0]
        p += 4
        code, p = _cstr(data, p)
        name, p = _cstr(data, p)
        flag = data[p]
        p += 1 + 4
        n = struct.unpack_from("<H", data, p)[0]
        offs = struct.unpack_from("<%dI" % n, data, p + 2)
        base = p + 2 + 4 * n
        strings = []
        for o in offs:
            ln = struct.unpack_from("<H", data, base + o)[0]
            strings.append(data[base + o + 2:base + o + 1 + ln].decode("utf-8"))
        extra = data[p + struct.unpack_from("<I", data, p - 4)[0]:end]
        p = end
        langs.append(Language(code.decode(), name.decode(), flag, strings, extra))
    if p != len(data) - 4:
        raise ValueError("table de chaînes : %d octets non lus" % (len(data) - 4 - p))
    return head, langs


def encode(head, langs):
    out = bytearray([head, len(langs)])
    for lg in langs:
        blob, offs = bytearray(), []
        for s in lg.strings:
            offs.append(len(blob))
            raw = s.encode("utf-8") + b"\0"
            blob += struct.pack("<H", len(raw)) + raw
        table = struct.pack("<H", len(offs)) + struct.pack("<%dI" % len(offs), *offs) + blob
        tail = struct.pack("<I", len(table)) + table
        body = lg.code.encode() + b"\0" + lg.name.encode() + b"\0" + bytes([lg.flag]) + tail + lg.extra
        out += struct.pack("<I", len(body)) + body
    out += struct.pack("<I", zlib.crc32(out))
    return bytes(out)
