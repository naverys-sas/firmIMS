"""Banc de test du découpage des propriétés (iqanprops.py) sur les projets du dépôt.

Pour chaque projet : chaque arbre d'objets est découpé objet par objet, puis réécrit ; la
réécriture doit être identique à l'octet près. Quand l'export texte du projet est disponible,
le nom de chaque objet (première valeur, n° de chaîne) est comparé à celui de l'export.

Usage (depuis outils_format/) : python banc_props.py"""
import os
import struct
import sys
from collections import Counter

import iqanobj
import iqanprj
import iqanprops
import iqanstr
import iqantxt

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PROJETS = [
    ("TESTIA.idax", "TESTIA_108.3.1.txt"),
    ("v117_testia.idax", "v117_108.2.2_117.txt"),
    ("avecMD3_V69.03.01.WIP.idax", "MD3_V69.03.1.txt"),
    ("version_avec_MD3_et_moteur_VW_V5.37.idax", "VW_V5.37.txt"),
    ("docs/versions_firmware/ig29 v25.74.idax", "V25.74_Commuter.txt"),
    ("docs/versions_firmware/X100 C V35.42.idax", "V35.42_X100.txt"),
    ("v2/projet/v2_mc42.idax", "v2_MC42_en_cours.txt"),
]


def name_of(obj, strs):
    """Nom de l'objet : première valeur, chaîne de la table du maître (ou texte en ligne)."""
    if not obj.values or obj.values[0][0] != 0xCB:
        return None
    v = obj.values[0]
    table, idx = v[1], struct.unpack_from("<H", v, 2)[0]
    if idx == 0xFFFE:
        return v[4:-1].decode("utf-8")
    if table != 0 or idx == 0xFFFF:
        return None
    return strs[idx] if idx < len(strs) else "?"


def check(idax, txt=None):
    T = iqantxt.read(txt) if txt and os.path.exists(txt) else {}
    p = iqanprj.Project(idax)
    secs = p.sections
    res = Counter()
    seen = Counter()  # un même identifiant peut servir dans plusieurs arbres (ex. 20, 22)
    for i, s in enumerate(secs):
        if s.tag in (0xB5, 0xCA, 0xC8):
            for m, o in iqanobj.Block(s.data).records:
                if m == 0x96:
                    seen.update(n.oid for n in o.walk())
    for i, s in enumerate(secs):
        if s.tag not in (0xB5, 0xCA, 0xC8):
            continue
        strs = iqanstr.parse(secs[i + 1].data)[1][0].strings if secs[i + 1].tag in (0xC6, 0xCB) else []
        bl = iqanobj.Block(s.data)
        trees = [o for m, o in bl.records if m == 0x96]
        props = [o for m, o in bl.records if m == 0x97]
        for t, pl in zip(trees, props):
            res["arbres"] += 1
            try:
                iqanprops.parse_stream(t, pl)
            except (ValueError, IndexError, struct.error) as e:
                res["arbres non découpés"] += 1
                print("  section %d, arbre %d : %s" % (i, t.oid, e))
                continue
            if iqanprops.encode_stream(t) != pl:
                res["arbres réécrits différents"] += 1
                continue
            for n in t.walk():
                res["objets"] += 1
                ref = dict(T.get(n.oid, {}).get("props", [])).get("Name")
                if ref is None or seen[n.oid] > 1:
                    continue
                got = name_of(n.obj, strs)
                if got is None:
                    continue
                res["noms comparés"] += 1
                if got != ref:
                    res["noms différents"] += 1
    return res


if __name__ == "__main__":
    total = Counter()
    for idax, txt in PROJETS:
        r = check(os.path.join(ROOT, idax), os.path.join(ROOT, "exports", txt))
        total.update(r)
        print("%-45s %s" % (idax, dict(r)))
    print("TOTAL", dict(total))
    bad = total["arbres non découpés"] + total["arbres réécrits différents"] + total["noms différents"]
    sys.exit(1 if bad else 0)
