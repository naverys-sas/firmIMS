"""Relie chaque objet binaire d'un projet à son objet dans l'export texte (même identifiant).

Usage : python correspondance.py projet.idax export.txt
Affiche le taux de correspondance ; sert de base pour apprendre le codage des propriétés
classe par classe (l'export texte est la vérité terrain)."""
import sys
from collections import Counter

import iqanobj
import iqanprj
import iqanstr
import iqantxt


def load(idax, txt):
    T = iqantxt.read(txt)
    p = iqanprj.Project(idax)
    B, fails = {}, []
    secs = p.sections
    for i, s in enumerate(secs):
        if s.tag not in (0xB5, 0xCA, 0xC8):
            continue
        strs = iqanstr.parse(secs[i + 1].data)[1][0].strings if secs[i + 1].tag in (0xC6, 0xCB) else []

        def name_ok(n, table, idx):
            props = T.get(n.oid, {}).get("props")
            name = dict(props).get("Name") if props else None
            return name is None or table != 0 or idx == 0xFFFF or (idx < len(strs) and strs[idx] == name)

        bl = iqanobj.Block(s.data)
        trees = [o for m, o in bl.records if m == 0x96]
        props = [o for m, o in bl.records if m == 0x97]
        for t, pr in zip(trees, props):
            try:
                iqanobj.split_props_checked(t, pr, name_ok)
            except ValueError as e:
                fails.append((i, t.oid, str(e)))
                continue
            for n in t.walk():
                B.setdefault(n.oid, []).append((i, n, strs))
    return T, B, p, fails


if __name__ == "__main__":
    T, B, p, fails = load(sys.argv[1], sys.argv[2])
    ok = sum(1 for x in T if x in B)
    print("objets texte : %d, reliés au binaire : %d" % (len(T), ok))
    print("classes :", len({(n.cls, n.sub) for v in B.values() for _, n, _ in v}))
    for f in fails:
        print("arbre non découpé :", f)
