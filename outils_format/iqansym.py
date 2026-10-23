"""Table des symboles d'un projet IQANdesign (section tag 0xbd).

  u8 03, u32 nombre d'entrées, u16 nombre de langues?, langue\\0, puis les entrées :
  [u32 id objet][u16 numéro][u8 00][u8 maître][u8 genre 2=module 4=canal][u16 classe]
  nom\\0 description\\0 unité\\0
Les canaux se désignent entre eux par (numéro, maître) : jeton cf 04 [u16 numéro] 00 [maître]
dans les propriétés. Les numéros suivent l'ordre de l'arbre de chaque maître.
"""
import struct


class Symbol:
    def __init__(self, oid, num, z, master, kind, cls, name, desc, unit):
        self.oid, self.num, self.z, self.master, self.kind, self.cls = oid, num, z, master, kind, cls
        self.name, self.desc, self.unit = name, desc, unit


def parse(b):
    n = struct.unpack_from("<I", b, 1)[0]
    q = b.index(b"\0", 7) + 1
    head = b[:q]
    syms = []
    for _ in range(n):
        f = struct.unpack_from("<IHBBBH", b, q)
        q += 11
        s = []
        for _ in range(3):
            e = b.index(b"\0", q)
            s.append(b[q:e].decode("utf-8"))
            q = e + 1
        syms.append(Symbol(*f, *s))
    if q != len(b):
        raise ValueError("table des symboles : %d octets non lus" % (len(b) - q))
    return head, syms


def encode(head, syms):
    out = bytearray(head)
    struct.pack_into("<I", out, 1, len(syms))
    for s in syms:
        out += struct.pack("<IHBBBH", s.oid, s.num, s.z, s.master, s.kind, s.cls)
        for t in (s.name, s.desc, s.unit):
            out += t.encode("utf-8") + b"\0"
    return bytes(out)
