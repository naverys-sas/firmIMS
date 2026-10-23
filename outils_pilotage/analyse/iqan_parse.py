"""Parse an IQANdesign text export (-saveas .txt) into a JSON tree + channel index.

Usage: python iqan_parse.py export.txt out_dir
Writes out_dir/tree.json, out_dir/channels.json, out_dir/refs.json
"""
import json, re, sys, os
from collections import defaultdict

BEGIN = re.compile(r'^(\s*)BEGIN (\d+)$')
END = re.compile(r'^\s*END (\d+)$')
KV = re.compile(r'^(\s*)([^=]+?)=(.*)$')


def parse(path):
    raw = open(path, 'rb').read().decode('latin1').replace('\r', '')
    lines = raw.split('\n')
    root = {'id': '0', 'type': 'Root', 'props': {}, 'sub': [], 'children': [], 'header': []}
    stack = [root]
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = BEGIN.match(ln)
        if m:
            indent = len(m.group(1))
            node = {'id': m.group(2), 'type': lines[i + 1].strip(), 'indent': indent,
                    'props': {}, 'sub': [], 'children': [], 'line': i + 1}
            stack[-1]['children'].append(node)
            stack.append(node)
            i += 2
            continue
        m = END.match(ln)
        if m and len(stack) > 1 and stack[-1]['id'] == m.group(1):
            stack.pop()
            i += 1
            continue
        node = stack[-1]
        if node is root:
            root['header'].append(ln)
            i += 1
            continue
        if ln.strip() == 'Qcode expression:':
            code = []
            i += 1
            while i < len(lines) and not END.match(lines[i]) and not BEGIN.match(lines[i]):
                code.append(lines[i][node['indent'] + 2:] if lines[i].strip() else '')
                i += 1
            node['qcode'] = '\n'.join(code).rstrip()
            continue
        m = KV.match(ln)
        if m and ln.strip():
            ind = len(m.group(1))
            if ind == node['indent'] and m.group(2) not in node['props']:
                node['props'][m.group(2)] = m.group(3)
            else:
                node['sub'].append(ln.strip())
        elif ln.strip():
            node['sub'].append(ln.strip())
        i += 1
    return root


CHANNEL_RE = re.compile(r'\(([A-Z0-9]+)\)$')
CONTAINERS = {'Application', 'Function group', 'Module', 'Generic module', 'Layer', 'Initialization'}


def walk(node, path, out):
    t = node['type']
    name = node['props'].get('Name', '')
    newpath = path
    if t in ('Application', 'Function group', 'Initialization') or t.endswith('module') or t.startswith('MD4') or t.startswith('MC') or t == 'Module':
        newpath = path + [f"{t}:{name}"]
    m = CHANNEL_RE.search(t)
    if m:
        out.append({'id': node['id'], 'kind': m.group(1), 'type': t, 'name': name,
                    'path': path, 'node': node})
    for c in node['children']:
        walk(c, newpath, out)


def node_text(node):
    """All text of a node and its descendants (values only), for reference scanning."""
    parts = list(node['props'].items())
    vals = [v for k, v in parts if k not in ('Name', 'Description', 'X', 'Y')]
    vals += [s.split('=', 1)[1] if '=' in s else s for s in node['sub']]
    if 'qcode' in node:
        vals.append(node['qcode'])
    for c in node['children']:
        if c['type'] in ('Function', 'Object group', 'Single object', 'Math object', 'Vector object',
                         'Multi vector object', 'Transition', 'State', 'Output', 'Point'):
            vals += node_text(c)
        elif not CHANNEL_RE.search(c['type']):
            vals += node_text(c)
    return vals


def main():
    src, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    root = parse(src)
    chans = []
    walk(root, [], chans)
    names = defaultdict(list)
    for c in chans:
        if c['name']:
            names[c['name']].append(c)
    # reference regex: longest names first, bounded by non-name chars
    sorted_names = sorted(names, key=len, reverse=True)
    exact = set(names)
    pat = re.compile('|'.join(r'(?<![\w.])' + re.escape(n) + r'(?![\w])' for n in sorted_names))
    refs = {}
    for c in chans:
        found = set()
        for v in node_text(c['node']):
            v2 = v.strip()
            if v2 in exact:
                found.add(v2)
                continue
            for mm in pat.finditer(v2):
                found.add(mm.group(0))
        found.discard(c['name'])
        refs[c['id']] = sorted(found)
    json.dump(root, open(os.path.join(out, 'tree.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    slim = [{k: v for k, v in c.items() if k != 'node'} | {'line': c['node']['line'], 'refs': refs[c['id']]} for c in chans]
    json.dump(slim, open(os.path.join(out, 'channels.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(len(chans), 'channels,', len(names), 'distinct names')


if __name__ == '__main__':
    main()
