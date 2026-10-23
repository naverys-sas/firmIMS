"""Generate IQANdesign-style text blocks from the v2 design tables.

Usage: python -I gen_iqan.py spec_dir out_dir

Each spec_dir/*.csv (separator ';', UTF-8) describes channels of one function
group. Columns:
  group        group path inside the application, '/'-separated
  channel      channel name
  type         IQAN channel type code: IDC, MAC, IMAC, SMC, SP, IP, FP, DP, FGI, TMR...
  unit         unit (empty for booleans and states)
  description  one sentence, English
  selector     function or mode selector (empty = Default function)
  function     function / state name for this row (empty = Default function)
  activating   IDC/SMC: activating expression; MAC/IMAC: controlling expression;
               parameters: default value; SP: states separated by '|'
  blocking     IDC/SMC: blocking expression
  properties   extra Key=Value pairs separated by ' & ' (Delay on=1000 & Delay off=0)
  origin       108.3.1 channel(s) this one replaces, or 'new' (kept as a comment)

Several rows with the same group + channel give the functions of a channel
with a selector. The output mirrors the layout of an IQANdesign text export
(BEGIN/END blocks, Key=Value) so that it can be entered in the IDE field by
field and compared with the export of the result. Object ids are not real
IQAN ids: they start at 900000 and only make the blocks well formed.
Expressions are written in the 'Expression' field of an object group; in the
IDE they are entered as math / single objects combined by the group method.
"""
import csv, glob, os, sys
from collections import OrderedDict

TYPES = {
    'IDC': 'Internal digital channel (IDC)', 'MAC': 'Math channel (MAC)',
    'IMAC': 'Integer math channel (IMAC)', 'SMC': 'State machine channel (SMC)',
    'SP': 'State parameter channel (SP)', 'IP': 'Integer parameter channel (IP)',
    'FP': 'Function parameter channel (FP)', 'DP': 'Digital parameter channel (DP)',
    'FGI': 'Function group input channel (FGI)', 'TMR': 'Timer channel (TMR)',
    'CMSG': 'Conditional message channel (CMSG)', 'APPOUT': 'Application output channel (APPOUT)',
    'APPIN': 'Application input channel (APPIN)', 'ARC': 'Array channel (ARC)',
}
DIGITAL = {'IDC', 'SMC', 'CMSG'}
PARAM = {'SP', 'IP', 'FP', 'DP'}


class Ids:
    def __init__(self):
        self.n = 900000

    def __call__(self):
        self.n += 1
        return self.n


def block(out, ind, typ, props, ids, body=None):
    i = ids()
    pad = '  ' * ind
    out.append('')
    out.append(f'{pad}BEGIN {i}')
    out.append(f'{pad}{typ}')
    for k, v in props:
        out.append(f'{pad}{k}={v}')
    if body:
        body(ind + 1)
    out.append(f'{pad}END {i}')


def object_group(out, ind, name, method, expr, ids):
    block(out, ind, 'Object group',
          [('Name', name), ('Description', ''), ('Method', method if expr else 'Or'),
           ('Valid', 'True'), ('Expression', expr)], ids)


def channel(out, ind, rows, ids):
    r0 = rows[0]
    code = r0['type'].strip()
    typ = TYPES.get(code, code)
    props = [('Name', r0['channel']), ('Description', r0['description'])]
    if r0['origin']:
        props[1] = ('Description', r0['description'] + f"  [origin: {r0['origin']}]")
    if r0['unit']:
        props.append(('Unit', r0['unit']))
    for kv in filter(None, (p.strip() for p in r0['properties'].split(' & '))):
        k, _, v = kv.partition('=')
        props.append((k.strip(), v.strip()))
    sel = r0['selector'].strip()

    if code in PARAM:
        if code == 'SP':
            states = r0['activating'].split('|')
            props += [('Input channel', 'None'), ('Default state name', states[0]),
                      ('States', '{' + '; '.join(states[1:]) + '}')]
            props += [(f'  State {n}', s) for n, s in enumerate(states[1:], 1)]
        else:
            props.append(('Mode selector', sel or 'Not used'))
            if sel:
                for n, r in enumerate(rows):
                    label = 'Default mode' if n == 0 else f'Mode {n}'
                    props.append((f"{label}: {r['function']}", '{' + r['activating'] + '}'))
            else:
                props.append(('Default mode', '{' + r0['activating'] + '}'))
        block(out, ind, typ, props, ids)
        return

    if code in ('FGI', 'APPIN', 'APPOUT', 'ARC'):
        if r0['activating']:
            props.append(('Input channel', r0['activating']))
        block(out, ind, typ, props, ids)
        return

    props.append(('Function selector', sel or 'Not used'))

    def body(bi):
        for r in rows:
            fname = r['function'] or 'Default function'

            def fbody(fi, r=r):
                if code in DIGITAL:
                    first = 'Showing' if code == 'CMSG' else 'Activating'
                    object_group(out, fi, first, 'Expression', r['activating'], ids)
                    if code != 'CMSG':
                        object_group(out, fi, 'Blocking', 'Expression', r['blocking'], ids)
                else:
                    object_group(out, fi, 'Controlling', 'Expression', r['activating'], ids)
            block(out, bi, 'Function', [('Name', fname), ('Description', '')], ids, fbody)
    block(out, ind, typ, props, ids, body)


def generate(path, ids):
    rows = list(csv.DictReader(open(path, encoding='utf-8-sig'), delimiter=';'))
    tree = OrderedDict()
    for r in rows:
        r = {k: (v or '').strip() for k, v in r.items()}
        tree.setdefault(r['group'], OrderedDict()).setdefault(r['channel'], []).append(r)
    out = [f'// Generated from {os.path.basename(path)} by outils_pilotage/conception/gen_iqan.py',
           '// Not an importable file: IQANdesign has no text import. Enter in the IDE, then',
           '// compare the export of the project with check_spec.py.']
    for gpath, chans in tree.items():
        parts = gpath.split('/')

        def nest(level, ind):
            if level == len(parts):
                for rs in chans.values():
                    channel(out, ind, rs, ids)
                return
            block(out, ind, 'Function group',
                  [('Name', parts[level]), ('Description', ''), ('Enabled', 'Yes')],
                  ids, lambda bi: nest(level + 1, bi))
        nest(0, 0)
    return '\n'.join(out) + '\n'


def main():
    spec_dir, out_dir = sys.argv[1], sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)
    ids = Ids()
    for path in sorted(glob.glob(os.path.join(spec_dir, '*.csv'))):
        with open(path, encoding='utf-8-sig') as f:
            if 'channel' not in f.readline().split(';'):
                continue  # a plain table (e.g. a bit map), not a channel spec
        name = os.path.splitext(os.path.basename(path))[0] + '.txt'
        with open(os.path.join(out_dir, name), 'w', encoding='utf-8') as f:
            f.write(generate(path, ids))
        print('written', name)


if __name__ == '__main__':
    main()
