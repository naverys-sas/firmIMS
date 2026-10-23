"""Compare the electric (E) and thermal (T) copies of the track logic groups.

Usage: python -I ecarts_e_t.py export.txt > ecarts_E_T.md

Channels are paired by name once the E/T markers are removed. A pair is
"identical" when both channels have the same type, properties and logic once
the E/T markers are removed from every referenced channel name. For each
differing pair, both copies are printed as exported so that the
owner can decide: keep E, keep T, or make it a setting.
"""
import os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'analyse'))
from iqan_parse import parse  # noqa: E402

PAIRS = [('E.Translate', 'T.Translate'),
         ('E.Track tension', 'T.Track tension'),
         ('E.Track Up/Down', 'T.Track Up/Down'),
         ('E.KeyBox x100 E', 'T.KeyBox x100 T')]
SKIP = {'X', 'Y', 'Name', 'Description', 'Last edited'}


def norm(s):
    s = re.sub(r'\[.*?\]', '', s)
    s = re.sub(r'^(E|T|e|t)[ .]', '', s.strip())
    s = re.sub(r'\b(E|T|e)\b', '', s)
    return re.sub(r'\s+', ' ', s.replace(' mc', ' ')).strip().lower()


def signature(n):
    props = tuple(sorted((k, norm(v)) for k, v in n['props'].items() if k not in SKIP))
    return (n['type'], props, norm(n.get('qcode', '')),
            tuple(signature(c) for c in n['children']))


def groups(root):
    out = {}

    def walk(n):
        if n['type'] == 'Function group':
            out[n['props'].get('Name', '')] = n
        for c in n['children']:
            walk(c)
    walk(root)
    return out


def channels(g):
    return {c['props'].get('Name', ''): c for c in g['children']
            if c['type'].endswith(')') and '(' in c['type']}


def render(n, depth=0):
    """Raw rendering of a channel as exported (names exactly as written)."""
    pad = '  ' * depth
    props = ' · '.join(f'{k}={v}' for k, v in n['props'].items() if k not in SKIP)
    head = n['type'] if depth == 0 else f"{n['type']} {n['props'].get('Name', '')}"
    out = [pad + head + (f' · {props}' if props else '')]
    if n.get('qcode'):
        out += [pad + '  | ' + x for x in n['qcode'].split('\n')]
    for c in n['children']:
        out += render(c, depth + 1)
    return out


def main():
    export = sys.argv[1]
    g = groups(parse(export))
    print('# Écarts entre les copies électrique (E) et thermique (T) de la logique chenilles\n')
    print('Généré par `outils_pilotage/conception/ecarts_e_t.py` depuis `%s`. '
          'Pour chaque canal présent dans les deux copies mais avec une logique différente, '
          'il faut choisir : garder E, garder T, ou en faire un réglage dont la valeur par défaut '
          'reproduit chaque propulsion (voir `v2/refonte/05_logique_metier.md`).\n' % os.path.basename(export))
    print('| Groupe E | Groupe T | Communs | Identiques | Seulement E | Seulement T |')
    print('|---|---|---|---|---|---|')
    details = []
    A_all, B_all = {}, {}
    for a, b in PAIRS:
        A, B = channels(g[a]), channels(g[b])
        A_all.update(A)
        B_all.update(B)
        nA, nB = {norm(k): k for k in A}, {norm(k): k for k in B}
        common = sorted(set(nA) & set(nB))
        diff = [c for c in common if signature(A[nA[c]]) != signature(B[nB[c]])]
        onlyA = sorted(nA[c] for c in set(nA) - set(nB))
        onlyB = sorted(nB[c] for c in set(nB) - set(nA))
        print(f'| `{a}` ({len(A)}) | `{b}` ({len(B)}) | {len(common)} | {len(common) - len(diff)} | {len(onlyA)} | {len(onlyB)} |')
        details.append((a, b, onlyA, onlyB, [(nA[c], nB[c]) for c in diff]))
    for a, b, onlyA, onlyB, diff in details:
        print(f'\n## {a} / {b}\n')
        print('Seulement en E : ' + (', '.join(f'`{x}`' for x in onlyA) or '—') + '\n')
        print('Seulement en T : ' + (', '.join(f'`{x}`' for x in onlyB) or '—') + '\n')
        for ea, tb in diff:
            print(f'### `{ea}` ↔ `{tb}`\n')
            print('Décision : ☐ garder E ☐ garder T ☐ réglage\n')
            print('**E**\n```\n' + '\n'.join(render(A_all[ea])) + '\n```')
            print('**T**\n```\n' + '\n'.join(render(B_all[tb])) + '\n```\n')


if __name__ == '__main__':
    main()
