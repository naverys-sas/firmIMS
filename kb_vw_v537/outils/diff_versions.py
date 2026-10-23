"""Logic-level diff between two IQANdesign exports (channels added / removed / changed, group enables).

Usage: python -I diff_versions.py old.txt new.txt report.md "old label" "new label"
"""
import difflib, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_build import KB  # noqa: E402


def main():
    old, new, out, lo, ln = sys.argv[1:6]
    a, b = KB(old), KB(new)
    key = lambda c: (c['app'], ' / '.join(c['path'][2:]) or '(racine)', c['name'], c['kind'])
    logic = lambda kb, c: re.sub(r'\n- (Lit|Utilisé par|Ligne export).*', '', kb.card(c))
    A = {key(c): logic(a, c) for c in a.chans}
    B = {key(c): logic(b, c) for c in b.chans}
    rem = [k for k in A if k not in B]
    add = [k for k in B if k not in A]
    chg = [k for k in A if k in B and A[k] != B[k]]
    L = [f"# Évolution {lo} → {ln}", '', f"{len(add)} canaux ajoutés, {len(rem)} supprimés, {len(chg)} modifiés.", '']
    ena = []
    for g in b.groups:
        ga = [x for x in a.groups if x['path'] == g['path']]
        if ga and ga[0]['node']['props'].get('Enabled') != g['node']['props'].get('Enabled'):
            ena.append(f"- `{' / '.join(g['path'][1:])}` : Enabled {ga[0]['node']['props'].get('Enabled')} → {g['node']['props'].get('Enabled')}")
    if ena:
        L += ['## Activation de groupes modifiée', ''] + ena + ['']
    L += ['## Canaux modifiés', '']
    for k in chg:
        L.append(f"### {k[2]} `{k[3]}` — {k[0]} / {k[1]}")
        L.append('```diff')
        L += [l for l in difflib.unified_diff(A[k].split('\n'), B[k].split('\n'), lineterm='', n=0)
              if l[:1] in '+-' and not l.startswith(('+++', '---'))]
        L.append('```')
    L += ['', '## Canaux ajoutés', '']
    L += [f"- {k[0]} / {k[1]} : `{k[2]}` ({k[3]})" for k in add]
    L += ['', '## Canaux supprimés', '']
    L += [f"- {k[0]} / {k[1]} : `{k[2]}` ({k[3]})" for k in rem]
    open(out, 'w', encoding='utf-8').write('\n'.join(L))
    print(len(add), len(rem), len(chg))


if __name__ == '__main__':
    main()
