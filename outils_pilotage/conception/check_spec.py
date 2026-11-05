"""Check an IQANdesign text export against the v2 design tables.

Usage: python -I check_spec.py export.txt spec_dir [> report.md]

For every channel of spec_dir/*.csv (same format as gen_iqan.py) the export
must contain a channel with the same name, in a function group with the same
name as the last part of the spec group, of the same IQAN type, and with the
same function selector and function names. Logic expressions are not
compared (the IDE stores them as objects): diff_versions.py and a review do
that. Exit code 1 when anything is missing or different, so that the check
can gate a commit.
"""
import csv, glob, os, sys
from collections import OrderedDict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'analyse'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from iqan_parse import parse  # noqa: E402
from gen_iqan import TYPES  # noqa: E402


def index(root):
    out = {}

    def walk(n, group):
        if n['type'] in ('Function group', 'Application'):
            group = n['props'].get('Name', '')
        elif n['type'].endswith(')') and '(' in n['type']:
            funcs = [c['props'].get('Name', '') for c in n['children'] if c['type'] == 'Function']
            out.setdefault(n['props'].get('Name', ''), []).append((group, n, funcs))
        for c in n['children']:
            walk(c, group)
    walk(root, '')
    return out


def spec(spec_dir):
    chans = OrderedDict()
    for path in sorted(glob.glob(os.path.join(spec_dir, '*.csv'))):
        with open(path, encoding='utf-8-sig') as f:
            if 'channel' not in f.readline().split(';'):
                continue
        for r in csv.DictReader(open(path, encoding='utf-8-sig'), delimiter=';'):
            r = {k: (v or '').strip() for k, v in r.items() if k}
            key = (os.path.basename(path), r['channel'])
            chans.setdefault(key, []).append(r)
    return chans


def main():
    export, spec_dir = sys.argv[1], sys.argv[2]
    idx = index(parse(export))
    problems, ok = [], 0
    for (fname, name), rows in spec(spec_dir).items():
        r0 = rows[0]
        want_type = TYPES.get(r0['type'], r0['type'])
        want_group = r0['group'].split('/')[-1]
        found = idx.get(name, [])
        if not found:
            problems.append((fname, name, 'missing'))
            continue
        here = [f for f in found if f[0] == want_group] or found
        group, node, funcs = here[0]
        issues = []
        if group != want_group:
            issues.append(f'in group `{group}` instead of `{want_group}`')
        if node['type'] != want_type:
            issues.append(f'type `{node["type"]}` instead of `{want_type}`')
        sel = r0['selector']
        if r0['type'] not in ('SP', 'IP', 'FP', 'DP', 'FGI', 'APPIN', 'APPOUT', 'ARC'):
            if (node['props'].get('Function selector') or 'Not used') != (sel or 'Not used'):
                issues.append(f'selector `{node["props"].get("Function selector")}` instead of `{sel or "Not used"}`')
            want_funcs = [r['function'] for r in rows if r['function']]
            if want_funcs and sorted(want_funcs) != sorted(funcs):
                issues.append(f'functions {funcs} instead of {want_funcs}')
        if not node['props'].get('Description'):
            issues.append('no description')
        if issues:
            problems.append((fname, name, '; '.join(issues)))
        else:
            ok += 1
    print(f'# Conformité de `{os.path.basename(export)}` à la conception v2\n')
    print(f'{ok} canaux conformes, {len(problems)} écarts.\n')
    if problems:
        print('| Table | Canal | Écart |\n|---|---|---|')
        for fname, name, why in problems:
            print(f'| {fname} | `{name}` | {why} |')
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
