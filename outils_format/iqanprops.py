"""Propriétés des objets d'un projet IQANdesign : découpage exact et réécriture.

Le flux de propriétés d'un arbre (enregistrement 0x97 d'un bloc d'objets) est imbriqué.
Chaque objet s'écrit :

  [classe][sous-classe][version][00]
  N valeurs typées      N fixé par (classe, sous-classe, version), voir NV
  les objets enfants    dans l'ordre de l'arbre (enregistrement 0x96)
  la fin de l'objet     octets non typés, dont la longueur dépend de la classe (TAILS)

Valeurs typées (premier octet = type) :
  c9 u32 | ca f32 | cb [table u8][n° de chaîne u16], suivi d'un texte en ligne terminé par 00
  si le n° vaut fffe | cd u16 (énuméré) | ce u32 (couleur) | cf [genre u8][u32] (référence :
  genre 04 = canal [n° u16][00][maître]) | d2 [n u16] puis n valeurs (liste) | d4 8 octets |
  d5 u32 (hexadécimal) | d7 texte terminé par 00 | dd 16 octets

Fin des canaux (classe 04) : [u32 0][X u32][Y u32][u8][n u16][n x 12 octets], suivis d'octets
propres à certaines classes (voir TAILS).

Découpage appris et vérifié sur les 7 projets du dépôt : voir banc_props.py.
"""
import struct

SIZES = {0xC9: 4, 0xCA: 4, 0xCB: 3, 0xCD: 2, 0xCE: 4, 0xCF: 5, 0xD4: 8, 0xD5: 4, 0xDD: 16}


def value_end(b, p):
    """Fin de la valeur typée commençant en p, ou None si l'octet n'est pas un type."""
    t = b[p]
    if t == 0xD2:
        n = struct.unpack_from("<H", b, p + 1)[0]
        p += 3
        for _ in range(n):
            p = value_end(b, p)
            if p is None:
                return None
        return p
    if t in SIZES:
        q = p + 1 + SIZES[t]
        if t == 0xCB and b[p + 2:p + 4] == b"\xfe\xff":
            q = b.index(b"\0", q) + 1
        return q if q <= len(b) else None
    if t == 0xD7:
        return b.index(b"\0", p + 1) + 1
    return None


def read_values(b, p, nmax):
    """Lit au plus nmax valeurs typées ; rend (fin, [octets de chaque valeur])."""
    vals = []
    while p < len(b) and len(vals) < nmax:
        try:
            q = value_end(b, p)
        except (ValueError, IndexError, struct.error):
            q = None
        if q is None:
            break
        vals.append(b[p:q])
        p = q
    return p, vals


def first_list_len(vals):
    for v in vals:
        if v[0] == 0xD2:
            return struct.unpack_from("<H", v, 1)[0]
    return 0


# Fins d'objets. Chaque règle rend la longueur de la fin à partir de la position p.
def _chan(b, p, vals):
    return 15 + 12 * struct.unpack_from("<H", b, p + 13)[0]


def _chanx(extra):
    return lambda b, p, vals: _chan(b, p, vals) + extra


def _chan_states(b, p, vals):  # canaux à états : un u32 par état (identifiant d'objet)
    return _chan(b, p, vals) + 4 * first_list_len(vals)


def _chan_042e(b, p, vals):
    q = p + _chan(b, p, vals)
    return q - p + 3 + 2 * b[q + 2] + 4


def _fgroup(b, p, vals):  # groupe de fonctions : [u16][X][Y] empreinte\0 [n u16][n x 4] + 24
    q = b.index(b"\0", p + 10) + 1
    n = struct.unpack_from("<H", b, q)[0]
    return q - p + 2 + 4 * n + 24


def _u16_list4(b, p, vals):
    return 2 + 4 * struct.unpack_from("<H", b, p)[0]


def _blob(b, p, vals):  # image : [u8 genre][u32 taille][données] ; genre 1 : 10 octets puis taille
    if b[p] == 1:
        return 15 + struct.unpack_from("<I", b, p + 11)[0]
    return 5 + struct.unpack_from("<I", b, p + 1)[0]


def _rest(b, p, vals):  # objet racine dont la fin varie selon les projets (groupe Telematics)
    return len(b) - p


CHAN = _chan
TAILS = {}
for _c, _l in {
    0x0100: _fgroup, 0x0106: _fgroup, 0x0439: 1957, 0x0a00: _blob,
    0x2a00: 9, 0x2b00: _u16_list4, 0x3d00: 16, 0x3800: 8, 0x0811: 16, 0x080c: 8,
    0x0427: _chanx(4), 0x041f: _chanx(4), 0x042d: _chanx(7), 0x042e: _chan_042e,
    0x0428: _chan_states, 0x041b: _chan_states,
    0x0205: 8, 0x0207: 8, 0x0209: 8, 0x020a: 8, 0x0213: 8, 0x0214: 8, 0x021c: 8, 0x021f: 8,
    0x0302: 9, 0x0303: 9, 0x0305: 9, 0x0306: 9, 0x0701: 2, 0x0703: 2, 0x0704: 2,
    0x0812: 1, 0x0819: 1, 0x081a: 1, 0x4700: _rest,
}.items():
    TAILS[(_c >> 8, _c & 0xFF)] = _l


def tail_rule(cls, sub):
    r = TAILS.get((cls, sub))
    if r is not None:
        return r
    if cls == 0x04:
        return CHAN
    if cls == 0x05:  # objets mathématiques, objets simples : un octet
        return 1
    if cls in (0x33, 0x41):
        return 2
    return 0


# Nombre de valeurs typées, quand la lecture « tant que l'octet est un type » irait trop loin
# (la fin de l'objet commence par un octet qui ressemble à un type, par exemple X = 0xca).
NV_CAPS = {(0x3D, 0x00, 0): 2, (0x08, 0x11, 0): 9, (0x08, 0x0C, 0): 10, (0x02, 0x07, 0): 5,
           (0x03, 0x03, 0): 4}


def nv_default(cls, sub, ver):
    return NV_CAPS.get((cls, sub, ver), 999)


class Obj:
    """Contenu propre d'un objet : en-tête, valeurs typées, fin. Les enfants sont dans le noeud."""
    __slots__ = ("cls", "sub", "ver", "values", "tail")

    def __init__(self, cls, sub, ver, values, tail):
        self.cls, self.sub, self.ver, self.values, self.tail = cls, sub, ver, values, tail

    def head(self):
        return bytes([self.cls, self.sub, self.ver, 0]) + b"".join(self.values)


def parse_stream(root, pl, nv=nv_default):
    """Découpe le flux de propriétés pl de l'arbre root ; chaque noeud reçoit .obj.

    nv(cls, sub, ver) donne le nombre maximal de valeurs typées de l'objet."""
    def rec(n, p):
        if pl[p] != n.cls or pl[p + 1] != n.sub or pl[p + 3] != 0:
            raise ValueError("objet %d : signature attendue en %d" % (n.oid, p))
        ver = pl[p + 2]
        q, vals = read_values(pl, p + 4, nv(n.cls, n.sub, ver))
        for c in n.children:
            q = rec(c, q)
        r = tail_rule(n.cls, n.sub)
        L = r if isinstance(r, int) else r(pl, q, vals)
        n.obj = Obj(n.cls, n.sub, ver, vals, pl[q:q + L])
        return q + L
    end = rec(root, 0)
    if end != len(pl):
        raise ValueError("arbre %d : %d octets non lus" % (root.oid, len(pl) - end))
    return root


def encode_stream(root):
    out = bytearray()

    def rec(n):
        out.extend(n.obj.head())
        for c in n.children:
            rec(c)
        out.extend(n.obj.tail)
    rec(root)
    return bytes(out)
