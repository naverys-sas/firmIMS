"""Build harness (wiring) data: module pin lists from IQANdesign + logic context from the export.

Usage: python -I harness.py out.json lineage_label export.txt pins_dir [lineage_label export.txt pins_dir ...]
pins_dir holds one TSV per module (pin, name, channel, description) dumped from IQANdesign's module List view.
"""
import csv, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_build import KB  # noqa: E402

UNIT = re.compile(r'\s*\[[^\]]*\]$')


def signal_kind(name):
    n = name.upper()
    if n.startswith(('+BAT', '-BAT')):
        return 'power'
    if n.startswith('CAN'):
        return 'can'
    if n.startswith(('ADDR', '+VREF', '-VREF', '+RTC')):
        return 'ref'
    if n.startswith(('VIN', 'DIN', 'DPCNT', 'FIN', 'CIN', 'PIN')):
        return 'in'
    if n.startswith(('DOUT', 'COUT', 'PWM', 'VOUT')):
        return 'out'
    return 'other'


def lineage(label, export, pins_dir):
    kb = KB(export)
    groups = {tuple(g['path']): g for g in kb.groups}
    by_name = {}
    for c in kb.chans:
        by_name.setdefault(c['name'], c)
    mods = []
    for f in sorted(os.listdir(pins_dir)):
        if not f.endswith('.tsv'):
            continue
        rows = []
        with open(os.path.join(pins_dir, f), encoding='utf-8-sig') as fh:
            for r in csv.DictReader(fh, delimiter='\t'):
                ch = (r.get('channel') or '').strip()
                c = by_name.get(UNIT.sub('', ch)) if ch else None
                conds, gpath = [], ''
                if c:
                    gpath = ' / '.join(c['path'][2:])
                    for k in range(2, len(c['path']) + 1):
                        g = groups.get(tuple(c['path'][:k]))
                        if g:
                            en = g['node']['props'].get('Enabled', 'Yes')
                            if en not in ('Yes', '', None):
                                conds.append(en)
                rows.append({'pin': r['pin'], 'sig': (r.get('name') or '').strip(), 'ch': ch,
                             'desc': (r.get('description') or '').strip(), 'kind': signal_kind(r.get('name') or ''),
                             'grp': gpath, 'cond': conds,
                             'chdesc': (c['node']['props'].get('Description', '') if c else ''),
                             'ctype': c['kind'] if c else ''})
        mods.append({'module': f[:-4], 'rows': rows})
    return {'label': label, 'modules': mods}


def main():
    out = sys.argv[1]
    args = sys.argv[2:]
    data = [lineage(*args[i:i + 3]) for i in range(0, len(args), 3)]
    json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
    for l in data:
        print(l['label'], [(m['module'], len(m['rows'])) for m in l['modules']])


if __name__ == '__main__':
    main()
