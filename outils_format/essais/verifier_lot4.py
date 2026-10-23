"""Compare les exports texte IQANdesign des fichiers du lot 4 à l'export du projet d'origine.

Usage : python verifier_lot4.py export_origine.txt dossier_des_exports
Pour chaque L4*.txt : objets ajoutés, supprimés, et propriétés modifiées (avant -> après).
Les lignes qui changent à chaque enregistrement (somme de contrôle du projet) sont ignorées."""
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.dirname(HERE)]
import iqantxt  # noqa: E402

IGNORE = {"Project checksum", "Checksum"}


def props(o):
    return [(k, v) for k, v in o["props"] if k not in IGNORE]


def compare(a, b, out, limit=60):
    added = sorted(set(b) - set(a))
    removed = sorted(set(a) - set(b))
    changed = [i for i in sorted(set(a) & set(b))
               if props(a[i]) != props(b[i]) or a[i]["parent"] != b[i]["parent"] or a[i]["cls"] != b[i]["cls"]]
    out.append("  ajoutés %d, supprimés %d, modifiés %d" % (len(added), len(removed), len(changed)))
    for i in added[:limit]:
        out.append("  + %d %s %r" % (i, b[i]["cls"], dict(b[i]["props"]).get("Name")))
    for i in removed[:limit]:
        out.append("  - %d %s %r" % (i, a[i]["cls"], dict(a[i]["props"]).get("Name")))
    for i in changed[:limit]:
        da, db = dict(props(a[i])), dict(props(b[i]))
        what = ["%s: %r -> %r" % (k, da.get(k), db.get(k)) for k in list(da) + [k for k in db if k not in da]
                if da.get(k) != db.get(k)]
        if a[i]["parent"] != b[i]["parent"]:
            what.append("parent %s -> %s" % (a[i]["parent"], b[i]["parent"]))
        out.append("  ~ %d %s %r : %s" % (i, a[i]["cls"], da.get("Name"), "; ".join(what)[:300]))


if __name__ == "__main__":
    ref = iqantxt.read(sys.argv[1])
    out = []
    for path in sorted(glob.glob(os.path.join(sys.argv[2], "L4*.txt"))):
        out.append("== " + os.path.basename(path))
        compare(ref, iqantxt.read(path), out)
    print("\n".join(out))
