"""Export the channel graph of one IQAN export as compact JSON for the companion web page.

Usage: python -I export_companion_data.py export.txt out.json
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_build import KB  # noqa: E402


def main():
    src, out = sys.argv[1], sys.argv[2]
    kb = KB(src)
    idx = {c['id']: i for i, c in enumerate(kb.chans)}
    groups = {}
    for g in kb.groups:
        if len(g['path']) < 2:
            continue
        key = ' / '.join(g['path'][1:])
        groups[key] = {'en': g['node']['props'].get('Enabled', 'Yes'),
                       'd': g['node']['props'].get('Description', '')}
    chans = []
    for c in kb.chans:
        card = kb.card(c).split('\n')
        body = [l for l in card[1:] if not l.startswith(('- Lit :', '- Utilisé par :', '- Ligne export'))]
        uses = sorted({idx[t['id']] for nm in kb.uses[c['id']] for t in kb.resolve(c, nm)})
        used = sorted(idx[u] for u in kb.used_by.get(c['id'], ()))
        chans.append({'n': c['name'], 'k': c['kind'], 'a': c['app'], 'g': ' / '.join(c['path'][1:]),
                      'b': '\n'.join(body), 'u': uses, 'r': used,
                      'ui': sorted(kb.used_by_ui.get(c['id'], ())), 'l': c['node']['line']})
    json.dump({'chans': chans, 'groups': groups}, open(out, 'w', encoding='utf-8'), ensure_ascii=False,
              separators=(',', ':'))
    print(len(chans), os.path.getsize(out))


if __name__ == '__main__':
    main()
