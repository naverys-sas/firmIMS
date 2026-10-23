"""Compare deux projets IQANdesign objet par objet (identifiant, classe, valeurs lues, parent).

Les références entre canaux sont comparées par le nom du canal visé, pas par son numéro : une
renumérotation seule ne crée donc aucune différence. Sert à vérifier qu'une modification faite
avec iqanprojet.py ne touche que ce qui était voulu.

Usage : python diff_projets.py avant.idax apres.idax"""
import sys

import iqanprojet


def snapshot(pr):
    out = {}
    for sec, n in pr.walk():
        vals = tuple(pr.text(sec, n, i) for i in range(len(n.obj.values)))
        parent = n.parent.oid if n.parent is not None else None
        out.setdefault(n.oid, []).append((sec, "%02x%02x" % (n.cls, n.sub), parent, vals))
    return out


def diff(a, b):
    A, B = snapshot(a), snapshot(b)
    added = sorted(set(B) - set(A))
    removed = sorted(set(A) - set(B))
    changed = []
    for oid in sorted(set(A) & set(B)):
        if A[oid] != B[oid]:
            changed.append((oid, A[oid], B[oid]))
    return added, removed, changed


def report(a, b, out=sys.stdout):
    added, removed, changed = diff(a, b)
    out.write("objets ajoutés : %d, supprimés : %d, modifiés : %d\n" % (len(added), len(removed), len(changed)))
    B = snapshot(b)
    for oid in added:
        for sec, cls, parent, vals in B[oid]:
            out.write("+ %d (%s, section %d, parent %s) %r\n" % (oid, cls, sec, parent, vals[:3]))
    for oid in removed:
        out.write("- %d\n" % oid)
    for oid, x, y in changed:
        for (s1, c1, p1, v1), (s2, c2, p2, v2) in zip(x, y):
            what = []
            if p1 != p2:
                what.append("parent %s -> %s" % (p1, p2))
            for i in range(max(len(v1), len(v2))):
                u = v1[i] if i < len(v1) else None
                w = v2[i] if i < len(v2) else None
                if u != w:
                    what.append("valeur %d : %r -> %r" % (i, u, w))
            out.write("~ %d (%s, section %d) %s\n" % (oid, c1, s1, "; ".join(what) or "nombre d'occurrences"))
    return added, removed, changed


if __name__ == "__main__":
    report(iqanprojet.Projet(sys.argv[1]), iqanprojet.Projet(sys.argv[2]))
