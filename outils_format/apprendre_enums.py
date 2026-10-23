"""Apprend la liste des énumérés d'IQANdesign (jeton cd) à partir des projets et de leurs exports.

Pour chaque type d'objet, les valeurs typées sont alignées dans l'ordre sur les propriétés de
l'export texte (alignement monotone qui maximise les valeurs déjà lisibles) ; chaque énuméré
aligné sur une propriété vote pour son texte. On garde un code quand au moins 3 votes et 75 %
d'entre eux s'accordent. Résultat : iqan_enums.json.

Usage (depuis outils_format/) : python apprendre_enums.py"""
import json
import os
import struct
from collections import Counter, defaultdict

import banc_props
import iqanobj
import iqanprj
import iqanprops
import iqanstr
import iqansym
import iqantxt
import iqanvaleurs

SKIP = ("X", "Y")


def collect():
    """Rend [(valeurs, propriétés texte, contexte)] groupés par (classe, sous-classe, version)."""
    by = defaultdict(list)
    for idax, txt in banc_props.PROJETS:
        T = iqantxt.read(os.path.join(banc_props.ROOT, "exports", txt))
        secs = iqanprj.Project(os.path.join(banc_props.ROOT, idax)).sections
        syms = iqansym.parse(next(s for s in secs if s.tag == 0xBD).data)[1]
        seen = Counter()
        blocks = {}
        for i, s in enumerate(secs):
            if s.tag in (0xB5, 0xCA, 0xC8):
                blocks[i] = iqanobj.Block(s.data)
                for m, o in blocks[i].records:
                    if m == 0x96:
                        seen.update(n.oid for n in o.walk())
        for i, bl in blocks.items():
            strs = iqanstr.parse(secs[i + 1].data)[1][0].strings if secs[i + 1].tag in (0xC6, 0xCB) else []
            ctx = iqanvaleurs.Context(strs, syms, {})
            trees = [o for m, o in bl.records if m == 0x96]
            props = [o for m, o in bl.records if m == 0x97]
            for t, pl in zip(trees, props):
                iqanprops.parse_stream(t, pl)
                for n in t.walk():
                    if n.oid in T and seen[n.oid] == 1:
                        by[(n.cls, n.sub, n.obj.ver)].append((n.obj.values, T[n.oid]["props"], ctx))
    return by


def align(rows, enums):
    """Alignement monotone valeurs -> clés de l'export ; rend {clé: n° de valeur}."""
    keys = []
    for _, tp, _ in rows:
        for k, _ in tp:
            if k not in keys and k not in SKIP:
                keys.append(k)
    nv = max(len(v) for v, _, _ in rows)
    S = [[0.0] * nv for _ in keys]
    for vals, tp, ctx in rows:
        ctx.enums = enums
        d = dict(tp)
        for i, v in enumerate(vals):
            x = iqanvaleurs.render(v, ctx).strip()
            unknown = v[0] == 0xCD and struct.unpack_from("<H", v, 1)[0] not in enums
            for a, k in enumerate(keys):
                if k in d:
                    if x == d[k].strip():
                        S[a][i] += 1
                    elif unknown:
                        S[a][i] += 0.5
    m = len(keys)
    D = [[0.0] * (nv + 1) for _ in range(m + 1)]
    for a in range(m - 1, -1, -1):
        for i in range(nv - 1, -1, -1):
            D[a][i] = max(D[a + 1][i], D[a][i + 1], S[a][i] + D[a + 1][i + 1] if S[a][i] > 0 else -1)
    a = i = 0
    amap = {}
    while a < m and i < nv:
        if S[a][i] > 0 and abs(D[a][i] - (S[a][i] + D[a + 1][i + 1])) < 1e-9:
            amap[keys[a]] = i
            a += 1
            i += 1
        elif D[a][i] == D[a + 1][i]:
            a += 1
        else:
            i += 1
    return amap


def learn(by):
    enums = {}
    for _ in range(5):
        votes = defaultdict(Counter)
        for rows in by.values():
            amap = align(rows, enums)
            for vals, tp, _ in rows:
                d = dict(tp)
                for k, i in amap.items():
                    if i < len(vals) and vals[i][0] == 0xCD and k in d:
                        votes[struct.unpack_from("<H", vals[i], 1)[0]][d[k]] += 1
        new = {}
        for c, v in votes.items():
            text, n = v.most_common(1)[0]
            if n >= 3 and n >= 0.75 * sum(v.values()):
                new[c] = text
        if new == enums:
            break
        enums = new
    return enums


if __name__ == "__main__":
    enums = learn(collect())
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "iqan_enums.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump({str(k): v for k, v in sorted(enums.items())}, f, ensure_ascii=False, indent=0)
    print("%d énumérés appris -> %s" % (len(enums), path))
