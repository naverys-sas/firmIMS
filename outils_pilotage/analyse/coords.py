"""Dump channel canvas coordinates per function group (for GUI automation).

Usage: python -I coords.py export.txt out.json
out.json: {"App / Group / Sub": [[name, kind, X, Y], ...], ...}
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from iqan_parse import parse, CHANNEL_RE  # noqa: E402


def walk(n, path, out):
    t = n['type']
    if t in ('Function group', 'Application', 'Initialization'):
        path = path + [n['props'].get('Name', '')]
    m = CHANNEL_RE.search(t)
    if m and 'X' in n['props']:
        out.setdefault(' / '.join(path[1:]), []).append(
            [n['props'].get('Name', ''), m.group(1), int(n['props']['X']), int(n['props']['Y'])])
        return
    for c in n['children']:
        walk(c, path, out)


if __name__ == '__main__':
    out = {}
    walk(parse(sys.argv[1]), [], out)
    json.dump(out, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False)
    print(len(out), 'groups')
