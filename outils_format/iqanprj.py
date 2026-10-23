"""Lecture / écriture du conteneur de projet IQANdesign (.idax / .idsx).

Format (IQANdesign 6.08, décodé le 2026-10-23) :
  b"IQANprj\\0" + u8 version_conteneur + u8 drapeau
  puis une suite de sections [u8 tag][u32 longueur][charge utile]
  - tag 0xb4 : en-tête projet (nom, description, version, auteur, GUID...)
  - charge utile des autres sections : [u8 mode][u32 taille_brute][u32 taille_stockée][données]
    mode 2 = zlib (niveau 6, reproduit à l'octet près par Python), mode 0 = brut
  - tag 0xb8 (dernière) : CRC32 de tout le fichier jusqu'à son propre tag et sa longueur inclus, écrit deux fois (u32 LE).
Bibliothèque standard uniquement.
"""
import struct
import sys
import zlib

MAGIC = b"IQANprj\0"
TAG_HEADER, TAG_CRC = 0xB4, 0xB8


class Section:
    def __init__(self, tag, raw):
        self.tag, self.raw, self.mode, self.data = tag, raw, None, None
        if tag not in (TAG_HEADER, TAG_CRC) and raw[:1] in (b"\x00", b"\x02"):
            self.mode = raw[0]
            usize, csize = struct.unpack_from("<II", raw, 1)
            body = raw[9:9 + csize]
            self.data = zlib.decompress(body) if self.mode == 2 else body
            assert len(self.data) == usize, "taille décompressée inattendue"

    def encode(self):
        if self.data is None:
            return self.raw
        body = zlib.compress(self.data, 6) if self.mode == 2 else self.data
        return struct.pack("<BII", self.mode, len(self.data), len(body)) + body


class Project:
    def __init__(self, path=None):
        self.prefix, self.sections = MAGIC + b"\x0d\x01", []
        if path:
            self.load(open(path, "rb").read())

    def load(self, d):
        if d[:8] != MAGIC:
            raise ValueError("pas un projet IQANdesign")
        self.prefix = d[:10]
        p = 10
        while p < len(d):
            tag = d[p]
            n = struct.unpack_from("<I", d, p + 1)[0]
            self.sections.append(Section(tag, d[p + 5:p + 5 + n]))
            p += 5 + n
        crc = self.sections[-1]
        if crc.tag != TAG_CRC:
            raise ValueError("section CRC absente")
        stored = struct.unpack("<I", crc.raw[:4])[0]
        if stored != zlib.crc32(d[:p - 8]):
            raise ValueError("CRC32 du fichier incorrect")

    def dumps(self):
        out = bytearray(self.prefix)
        for s in self.sections:
            if s.tag == TAG_CRC:
                continue
            payload = s.encode()
            out += struct.pack("<BI", s.tag, len(payload)) + payload
        out += struct.pack("<BI", TAG_CRC, 8)
        crc = zlib.crc32(out)
        out += struct.pack("<II", crc, crc)
        return bytes(out)

    def save(self, path):
        open(path, "wb").write(self.dumps())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: iqanprj.py projet.idax [copie_reecrite.idax]")
    prj = Project(sys.argv[1])
    for i, s in enumerate(prj.sections):
        size = len(s.data) if s.data is not None else len(s.raw)
        print(f"{i:3d} tag=0x{s.tag:02x} mode={s.mode} octets={size}")
    if len(sys.argv) > 2:
        prj.save(sys.argv[2])
        same = open(sys.argv[1], "rb").read() == open(sys.argv[2], "rb").read()
        print("réécriture identique à l'octet près" if same else "réécriture différente")
