"""Index of a project's channels by name, from its IQANdesign text export (-saveas x.txt).

IQANsimulate numbers components with the object id of the export ("BEGIN n"), but its API does
not list the channels of a project; this index gives the name -> id map the twin needs.
Only objects whose type line ends with "(XYZ)" (channels) and modules are kept.

python -I index_export.py <export.txt> <out.csv>
"""
import csv
import re
import sys

TYPE = re.compile(r'\(([A-Z0-9]+)\)$')


def main(src, dst):
    stack = []          # (id, type, name) of open objects
    rows = []
    pending = None
    with open(src, encoding='utf-8', errors='replace') as f:
        for line in f:
            s = line.strip()
            if s.startswith('BEGIN '):
                pending = [int(s[6:]), None, None]
                stack.append(pending)
            elif s.startswith('END '):
                obj = stack.pop()
                typ = obj[1] or ''
                m = TYPE.search(typ)
                if m or typ.endswith('module'):
                    path = [o[2] for o in stack if o[2] and o[1] in ('Function group', 'Application', 'Module group')]
                    appli = next((o[2] for o in stack if o[1] == 'Application'), '')
                    rows.append({'id': obj[0], 'nom': obj[2] or '', 'type': m.group(1) if m else 'MODULE',
                                 'appli': appli, 'chemin': ' / '.join(path)})
            elif pending is not None and pending[1] is None:
                pending[1] = s
            elif pending is not None and pending[2] is None and s.startswith('Name='):
                pending[2] = s[5:]
    with open(dst, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['id', 'nom', 'type', 'appli', 'chemin'], delimiter=';')
        w.writeheader()
        w.writerows(rows)
    print(f'{len(rows)} canaux et modules -> {dst}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
