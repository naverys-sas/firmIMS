"""Blocs d'objets d'un projet IQANdesign (sections tag 0xb5, 0xca, 0xc8).

Contenu décompressé :
  u8 0x12 + u32 longueur + en-tête (copie de l'en-tête projet)
  préambule brut jusqu'au premier enregistrement 0x96
  enregistrements [u8 marque][u32 longueur][charge] :
    0x96 : un arbre d'objets, noeuds de 12 octets en pré-ordre
           [u8 classe][u8 sous-classe][u8 a][u8 b][u32 id objet][u16 rang][u16 nb enfants]
           (rang = position parmi les frères)
    0x97 : les propriétés des objets du même arbre, dans le même ordre, IMBRIQUÉES :
           [classe][sous-classe][version][00] + champs + enfants + champs de fin
           (X, Y... d'un parent viennent après ses enfants).
           Champs typés : c9 u32, ca u32/réel, cb [u8 table][u16 n° de chaîne] (ffff = aucun),
           cd u16, cf [u8 genre][u16 numéro][u8 0][u8 maître] (référence à un canal),
           d2 u16, d4 8 octets ; les autres champs sont bruts, propres à chaque classe.
    0x98 : CRC32 de tout ce qui précède, marque et longueur comprises (u32)
Le préambule contient le compteur d'identifiants (u32, dernier id attribué ou suivant).
"""
import struct
import zlib


class Node:
    __slots__ = ("cls", "sub", "a", "b", "oid", "idx", "children", "props", "parent", "obj", "st")

    def __init__(self, cls, sub, a, b, oid, idx):
        self.cls, self.sub, self.a, self.b, self.oid, self.idx = cls, sub, a, b, oid, idx
        self.children, self.props, self.parent = [], b"", None

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()


def parse_tree(pl):
    def rec(p, parent):
        cls, sub, a, b, oid, idx, nc = struct.unpack_from("<BBBBIHH", pl, p)
        n = Node(cls, sub, a, b, oid, idx)
        n.parent = parent
        p += 12
        for _ in range(nc):
            c, p = rec(p, n)
            n.children.append(c)
        return n, p
    root, p = rec(0, None)
    if p != len(pl):
        raise ValueError("arbre : %d octets en trop" % (len(pl) - p))
    return root


def encode_tree(root):
    out = bytearray()
    for n in root.walk():
        out += struct.pack("<BBBBIHH", n.cls, n.sub, n.a, n.b, n.oid, n.idx, len(n.children))
    return bytes(out)


def _candidates(pl, n, start):
    sig = bytes([n.cls, n.sub])
    p = pl.find(sig, start)
    while p >= 0:
        if p + 8 < len(pl) and pl[p + 3] == 0 and pl[p + 4] == 0xCB and pl[p + 5] < 4:
            yield p
        p = pl.find(sig, p + 1)


def split_props(root, pl):
    """Découpe le flux de propriétés objet par objet (méthode par recherche, provisoire).

    Chaque objet commence par [classe][sous-classe][version][00] suivi d'un champ typé
    (octet 0xc9..0xd5) ; on prend la première position possible de l'objet suivant."""
    return split_props_checked(root, pl, lambda n, table, idx: True)


def split_props_checked(root, pl, name_ok):
    """Comme split_props, mais une position n'est retenue que si name_ok(noeud, table, n° de chaîne
    du nom) l'accepte (par exemple en comparant à l'export texte) : élimine les fausses
    signatures trouvées au hasard dans les données."""
    nodes = list(root.walk())
    if pl[:2] != bytes([nodes[0].cls, nodes[0].sub]):
        raise ValueError("propriétés : premier objet inattendu")
    starts = [0]
    for n in nodes[1:]:
        p = next((c for c in _candidates(pl, n, starts[-1] + 4)
                  if name_ok(n, pl[c + 5], struct.unpack_from("<H", pl, c + 6)[0])), None)
        if p is None:
            raise ValueError("objet %d introuvable dans les propriétés" % n.oid)
        starts.append(p)
    starts.append(len(pl))
    for k, n in enumerate(nodes):
        n.props = pl[starts[k]:starts[k + 1]]
    return nodes


class Block:
    def __init__(self, data):
        if zlib.crc32(data[:-4]) != struct.unpack("<I", data[-4:])[0]:
            raise ValueError("CRC32 du bloc d'objets incorrect")
        hl = struct.unpack_from("<I", data, 1)[0]
        first = data.index(b"\x96", 5 + hl)
        self.head = data[:first]
        self.records = []  # (marque, objet) : arbre (Node) ou propriétés (bytes)
        p, trees = first, []
        while True:
            mark = data[p]
            n = struct.unpack_from("<I", data, p + 1)[0]
            pl = data[p + 5:p + 5 + n]
            if mark == 0x98:
                break
            if mark == 0x96:
                t = parse_tree(pl)
                trees.append(t)
                self.records.append([mark, t])
            else:
                self.records.append([mark, pl])
            p += 5 + n
        self.trees = trees

    def encode(self):
        out = bytearray(self.head)
        for mark, obj in self.records:
            pl = encode_tree(obj) if mark == 0x96 else obj
            out += struct.pack("<BI", mark, len(pl)) + pl
        out += struct.pack("<BI", 0x98, 4)
        out += struct.pack("<I", zlib.crc32(out))
        return bytes(out)
