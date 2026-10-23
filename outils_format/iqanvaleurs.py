"""Lecture des valeurs typées d'un objet sous la forme de l'export texte d'IQANdesign.

Les énumérés (jeton cd) renvoient à une liste unique pour tout IQANdesign : 0 = No, 1 = Yes,
54 = Not used, 237 = Signed... La correspondance est apprise sur les projets du dépôt
(apprendre_enums.py) et rangée dans iqan_enums.json.
"""
import json
import os
import struct

import iqanprops

ENUMS = {int(k): v for k, v in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                           "iqan_enums.json"), encoding="utf-8")).items()}


class Context:
    """Ce qu'il faut pour lire les valeurs d'un maître : sa table de textes et la table des symboles."""

    def __init__(self, strings, symbols, enums=None):
        self.strings = strings
        self.symbols = {(s.num, s.master, s.kind): s for s in symbols}
        self.enums = ENUMS if enums is None else enums


def items(v):
    """Éléments d'une liste (jeton d2)."""
    n = struct.unpack_from("<H", v, 1)[0]
    p, out = 3, []
    for _ in range(n):
        q = iqanprops.value_end(v, p)
        out.append(v[p:q])
        p = q
    return out


def render(v, ctx):
    t = v[0]
    if t == 0xCB:
        idx = struct.unpack_from("<H", v, 2)[0]
        if idx == 0xFFFE:
            return v[4:-1].decode("utf-8")
        if idx == 0xFFFF:
            return ""  # nom par défaut (A, B, Activating...), donné par IQANdesign
        return ctx.strings[idx] if idx < len(ctx.strings) else "<texte %d ?>" % idx
    if t == 0xD7:
        return "<chiffré>"  # mots de passe, codes PIN
    if t == 0xC9:
        return str(struct.unpack_from("<i", v, 1)[0])
    if t == 0xCA:
        return ("%.6g" % struct.unpack_from("<f", v, 1)[0]).replace(".", ",")
    if t == 0xD5:
        return "0x%X" % struct.unpack_from("<I", v, 1)[0]
    if t == 0xCD:
        c = struct.unpack_from("<H", v, 1)[0]
        return ctx.enums.get(c, "<énuméré %d>" % c)
    if t == 0xCE:
        return "Custom: $%08X" % struct.unpack_from("<I", v, 1)[0]
    if t == 0xCF:
        kind = v[1]
        if v[2:] == b"\xff\xff\xff\xff":
            return "None"
        if kind == 4:
            num, _, m = struct.unpack_from("<HBB", v, 2)
            s = ctx.symbols.get((num, m, 4))
            if s is None:
                return "<canal %d du maître %d ?>" % (num, m)
            return s.name + (" [%s]" % s.unit if s.unit else "")
        if kind == 5:  # opérande local d'un objet mathématique : A, B, C...
            return chr(65 + struct.unpack_from("<I", v, 2)[0])
        return "<réf. %02x %s>" % (kind, v[2:].hex())
    if t == 0xD2:
        return "{" + "; ".join(render(x, ctx) for x in items(v)) + "}"
    if t == 0xDD:
        return "<" + v[1:].hex() + ">"
    return "<?>"
