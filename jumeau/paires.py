"""Build the list of (v2 channel, 108.3.1 channel) pairs to compare in the twin.

The v2 runs beside the old logic in the same project, so one simulation run feeds both
with the same inputs. Each v2 spec row names in its "origin" column the 108.3.1 channel(s)
it replaces; when two are given ("e X / T X") the first is the electric one, the second the
thermal one. Only names that exist exactly once in the MC42 app of the 108.3.1 are kept.

python -I paires.py <spec_dir> <index_canaux.csv> <out.csv>
"""
import csv
import re
import sys
from pathlib import Path

SKIP_TYPES = {'ALIAS'}
DIGITAL = {'IDC', 'DP', 'COPY_D'}


def load_index(path):
    count = {}
    types = {}
    with open(path, encoding='utf-8-sig') as f:
        for row in csv.DictReader(f, delimiter=';'):
            if not row['appli'].startswith('MC42'):
                continue
            count[row['nom']] = count.get(row['nom'], 0) + 1
            types[row['nom']] = row['type']
    return {n: types[n] for n, c in count.items() if c == 1}


def candidates(origin):
    origin = origin.split(';')[0]
    origin = re.sub(r'\(.*?\)', '', origin)
    return [p.strip().strip('"') for p in origin.split(' / ') if p.strip()]


def main(spec_dir, index_path, out_path):
    known = load_index(index_path)
    pairs = []
    for spec in sorted(Path(spec_dir).glob('*.csv')):
        if spec.name.endswith('_bits.csv'):
            continue
        seen = set()
        with open(spec, encoding='utf-8-sig') as f:
            for row in csv.DictReader(f, delimiter=';'):
                name, typ = row['channel'], row['type']
                if name in seen or typ in SKIP_TYPES or not row.get('origin'):
                    continue
                seen.add(name)
                found = [c for c in candidates(row['origin']) if c in known]
                if not found:
                    continue
                two = len(found) == 2
                for i, old in enumerate(found):
                    variant = ('E' if i == 0 else 'T') if two else '*'
                    kind = 'digital' if typ in DIGITAL or known[old] in DIGITAL else 'analog'
                    pairs.append({'module': spec.stem, 'v2': name, 'ancien': old,
                                  'variante': variant, 'nature': kind})
    with open(out_path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['module', 'v2', 'ancien', 'variante', 'nature'], delimiter=';')
        w.writeheader()
        w.writerows(pairs)
    print(f'{len(pairs)} paires ecrites dans {out_path}')


if __name__ == '__main__':
    main(*sys.argv[1:4])
