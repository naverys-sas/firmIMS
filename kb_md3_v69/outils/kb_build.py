"""Build a markdown knowledge base from an IQANdesign text export.

Usage: python -I kb_build.py export.txt kb_dir
"""
import csv, json, os, re, sys
from collections import defaultdict, Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from iqan_parse import parse, CHANNEL_RE  # noqa: E402

UNIT_SUFFIX = re.compile(r'\s*\[[^\]]*\]$')
NUM = re.compile(r'^-?\d+([.,]\d+)?$|^0x[0-9A-Fa-f]+$')
CONSTS = {'True', 'False', 'Not used', 'None', '', 'Unlimited', 'Default', 'Not evaluated', 'Timeout', 'stError', 'Error',
          'OK', 'Out of range', 'Low', 'High'}
UNARY = {'not', 'PositiveFlank', 'NegativeFlank', 'Flank', 'Abs', 'Round', 'DerivativeOf'}
OBJ_TYPES = {'Single object', 'Math object', 'Dual object', 'Vector object', 'Multi vector object'}
OUTPUT_KINDS = {'DOUT', 'GFOUT', 'GPOUT', 'JPOUT', 'JFOUT', 'APPOUT', 'CMSG', 'IMSG', 'PCOUT', 'COUT', 'VOUT',
                'PWMOUT', 'TFC'}
STATEFUL = {'MEM', 'TMR', 'ECNT', 'FSM', 'SMC', 'SFC', 'ARC'}


def slug(s):
    s = re.sub(r'[^\w\-]+', '_', s, flags=re.UNICODE).strip('_')
    return s[:80] or 'x'


def strip_unit(v):
    return UNIT_SUFFIX.sub('', v.strip())


class KB:
    def __init__(self, src):
        self.root = parse(src)
        self.chans = []          # dicts: id, kind, type, name, app, path(list), node, enabled
        self.nonchan_users = []  # (label, node) for adjust items, logs, measure, pages
        self.groups = []         # function groups: path, node, enabled
        self._walk(self.root, [], None, True)
        self.by_name = defaultdict(list)
        for c in self.chans:
            self.by_name[(c['app'], c['name'])].append(c)
        self.global_names = defaultdict(list)
        for c in self.chans:
            self.global_names[c['name']].append(c)
        self._compile_ref_regex()
        self._compute_refs()

    # ---------- tree walk ----------
    def _walk(self, n, path, app, enabled):
        t = n['type']
        name = n['props'].get('Name', '')
        if t == 'Application':
            app = name
        if t in ('Function group', 'Application', 'Initialization'):
            en = enabled and n['props'].get('Enabled', 'Yes') != 'No'
            p = path + [name]
            if t != 'Application' or True:
                self.groups.append({'path': p, 'node': n, 'enabled': en, 'app': app, 'type': t})
            for c in n['children']:
                self._walk(c, p, app, en)
            return
        m = CHANNEL_RE.search(t)
        if m and app:
            self.chans.append({'id': n['id'], 'kind': m.group(1), 'type': t, 'name': name, 'app': app,
                               'path': path, 'node': n, 'enabled': enabled})
            return
        if t in ('Single adjust item', 'Dual adjust item', 'Measure item', 'Event log item', 'Value log item',
                 'Hour counter log item', 'Statistics log item', 'Adjust group', 'Measure group',
                 'Event log', 'Statistics log', 'Value log') or t.endswith('page'):
            self.nonchan_users.append((f"{t}: {name}", n))
            return
        for c in n['children']:
            self._walk(c, path, app, enabled)

    # ---------- references ----------
    def _compile_ref_regex(self):
        names = sorted({c['name'] for c in self.chans if c['name'] and not NUM.match(c['name'])}, key=len, reverse=True)
        self.ref_re = re.compile('|'.join(r'(?<![\w.])' + re.escape(x) + r'(?!\w)' for x in names))

    def values(self, n, top=True):
        vals = []
        for k, v in n['props'].items():
            if k in ('Name', 'Description', 'X', 'Y', 'Last edited', 'Text', 'Header, English',
                     'Text, English', 'Help', 'True text', 'False text', 'Unit', 'Type (Unit)', 'Type',
                     'Method', 'Operator', 'Module', 'Font', 'Color', 'Default state name', 'States',
                     'Store value', 'Toggle', 'Valid', 'Show message', 'Dialog type', 'Send method'):
                continue
            vals.append(v)
        for s in n['sub']:
            if '=' in s:
                k, v = s.split('=', 1)
                if not k.startswith(('Name and company', 'License number', 'Date and time', 'State ', 'Text')):
                    vals.append(v)
        if 'qcode' in n:
            vals.append(n['qcode'])
        for c in n['children']:
            if top or not CHANNEL_RE.search(c['type']):
                if CHANNEL_RE.search(c['type']) and not top:
                    continue
                vals += self.values(c, top=False)
        return vals

    def refs_in(self, n):
        found = set()
        for v in self.values(n):
            v2 = strip_unit(v)
            if v2 in self.global_names and not NUM.match(v2):
                found.add(v2)
                continue
            if '\n' in v or ' ' in v or any(ch in v for ch in '()[]:=<>+-*/'):
                for mm in self.ref_re.finditer(v):
                    found.add(mm.group(0))
        return found

    def resolve(self, src, name):
        """Scope-aware lookup: same function group first, then closest ancestor, then anywhere in the app."""
        cands = [c for c in self.by_name.get((src['app'], name), []) if c['id'] != src['id']]
        if not cands:
            return [c for c in self.global_names.get(name, []) if c['id'] != src['id']]
        best, blen = [], -1
        for c in cands:
            k = 0
            while k < min(len(c['path']), len(src['path'])) and c['path'][k] == src['path'][k]:
                k += 1
            if k == len(c['path']):  # c lives in src's group or an ancestor: visible
                if k > blen:
                    best, blen = [c], k
                elif k == blen:
                    best.append(c)
        return best or cands

    def _compute_refs(self):
        self.uses = {}
        self.used_by = defaultdict(set)
        self.used_by_ui = defaultdict(set)
        for c in self.chans:
            r = self.refs_in(c['node'])
            if not [x for x in self.by_name.get((c['app'], c['name']), []) if x['id'] != c['id']]:
                r.discard(c['name'])  # self-reference (counters, memories) is not a dependency
            self.uses[c['id']] = sorted(r)
            for nm in r:
                for tgt in self.resolve(c, nm):
                    self.used_by[tgt['id']].add(c['id'])
        for label, n in self.nonchan_users:
            for nm in self.refs_in(n):
                for tgt in self.global_names.get(nm, []):
                    self.used_by_ui[tgt['id']].add(label)
        # module pins / bus / log containers are scanned generically: anything outside Applications
        for top in self.root['children']:
            if top['type'] in ('Function group', 'Project'):
                continue
            # already covered via nonchan_users for items; add module-level names (pins)
        for g in self.groups:  # a channel that enables a function group is used
            ena = g['node']['props'].get('Enabled', 'Yes')
            if ena not in ('Yes', 'No', None):
                for tgt in self.global_names.get(strip_unit(ena), []):
                    self.used_by_ui[tgt['id']].add('Active le groupe: ' + ' / '.join(g['path'][2:]))
        self.cid = {c['id']: c for c in self.chans}

    # ---------- rendering of object-list functions ----------
    def render_obj(self, objs, name, seen=None):
        seen = seen or set()
        o = objs.get(name)
        if o is None or name in seen:
            return name
        seen = seen | {name}
        p = o['props']
        t = o['type']

        def op(x):
            x = x.strip()
            return '(' + self.render_obj(objs, x, seen) + ')' if x in objs and objs[x]['type'] == 'Math object' else self.render_obj(objs, x, seen) if x in objs else x

        if t == 'Single object':
            return op(p.get('Input', '?'))
        if t == 'Math object':
            o1, o2 = p.get('Operand 1', ''), p.get('Operand 2', '')
            oper = p.get('Operator', '?')
            if oper in UNARY:
                return f"{oper}({op(o1)})"
            if oper in ('MaxOf', 'MinOf'):
                return f"{oper}({op(o1)}, {op(o2)})"
            if oper == 'Inside':
                return f"Inside({op(o1)}, {op(o2)}, {p.get('Operand 3', '')})"
            return f"{op(o1)} {oper} {op(o2)}"
        if t == 'Dual object':
            return f"({op(p.get('Input', '?'))} ? {p.get('Out 1 (True)', '')} : {p.get('Out 2 (False)', '')})"
        if t == 'Vector object':
            return (f"lin({op(p.get('Input', '?'))}: {p.get('In 1')}->{p.get('Out 1')}, "
                    f"{p.get('In 2')}->{p.get('Out 2')}, {p.get('Outside range', '')})")
        if t == 'Multi vector object':
            return f"courbe({op(p.get('Input', '?'))}: {p.get('Points', '')}, {p.get('Outside range', '')})"
        return f"{t}:{name}"

    def render_group(self, g):
        objs = {c['props'].get('Name'): c for c in g['children'] if c['type'] in OBJ_TYPES}
        if not objs:
            return None
        referenced = set()
        for o in objs.values():
            p = o['props']
            for k in ('Input', 'Operand 1', 'Operand 2', 'Operand 3'):
                v = p.get(k, '').strip()
                if v in objs:
                    referenced.add(v)
        resulting = [n for n in objs if n not in referenced]
        parts = [self.render_obj(objs, n) for n in resulting]
        meth = g['props'].get('Method', '')
        if len(parts) == 1:
            return parts[0] + ('' if meth in ('Or', 'And', 'Multiply (%)', 'MinOf (Absolute)', 'MaxOf (Absolute)') else f'   [{meth}]')
        sep = {'Or': ' OR ', 'And': ' AND ', 'Latching Or': ' OR ', 'Latching And': ' AND ',
               'Multiply (%)': ' ×% ', }.get(meth)
        if sep:
            s = sep.join(f"({x})" if ' ' in x else x for x in parts)
            return s + ('   [verrouillé]' if meth.startswith('Latching') else '')
        return f"{meth}(" + ', '.join(parts) + ')'

    def render_function(self, f, indent='  '):
        out = []
        if 'qcode' in f:
            out.append(indent + '```qcode')
            out += [indent + l for l in f['qcode'].split('\n')]
            out.append(indent + '```')
        for g in f['children']:
            if g['type'] != 'Object group':
                continue
            r = self.render_group(g)
            if r is not None:
                out.append(f"{indent}- **{g['props'].get('Name')}** = `{r}`")
        return out

    # ---------- channel card ----------
    SKIP = {'Name', 'Description', 'X', 'Y', 'Freezed', 'Last edited'}

    def card(self, c):
        n = c['node']
        lines = [f"#### {c['name']}  `{c['kind']}`"]
        d = n['props'].get('Description', '')
        if d:
            lines.append(f"> {d}")
        props = [f"{k}={v}" for k, v in n['props'].items() if k not in self.SKIP and v not in ('', 'Not used')]
        if props:
            lines.append('- Propriétés : ' + ' · '.join(props))
        for ch in n['children']:
            if ch['type'] == 'Function':
                fn = ch['props'].get('Name', '')
                body = self.render_function(ch)
                if body:
                    lines.append(f"- Fonction *{fn}* :" if fn != 'Default function' else '- Logique :')
                    lines += body
                elif fn != 'Default function':
                    lines.append(f"- Fonction *{fn}* : (vide)")
            elif ch['type'] == 'State':
                sname = ch['props'].get('Name')
                idx = sum(1 for x in n['children'][:n['children'].index(ch)] if x['type'] == 'State')
                sd = ch['props'].get('Description', '')
                lines.append(f"- État {idx} **{sname}**" + (f" — {sd}" if sd else ''))
                for tr in ch['children']:
                    if tr['type'] == 'Transition':
                        td = tr['props'].get('Description', '')
                        lines.append(f"  - transition *{tr['props'].get('Name')}*" + (f" — {td}" if td else '')
                                     + " (état cible non exporté par IQANdesign)")
                        for f in tr['children']:
                            if f['type'] == 'Function':
                                lines += self.render_function(f, '    ')
        users = sorted(self.cid[u]['name'] for u in self.used_by.get(c['id'], ()))
        ui = sorted(self.used_by_ui.get(c['id'], ()))
        if self.uses[c['id']]:
            lines.append('- Lit : ' + ', '.join(f"`{x}`" for x in self.uses[c['id']]))
        if users or ui:
            lines.append('- Utilisé par : ' + ', '.join(f"`{x}`" for x in users + ui))
        else:
            lines.append('- Utilisé par : *(personne)*')
        lines.append(f"- Ligne export : {n['line']} · id {c['id']}")
        return '\n'.join(lines)


def main():
    src, out = sys.argv[1], sys.argv[2]
    os.makedirs(os.path.join(out, 'fonctions'), exist_ok=True)
    kb = KB(src)
    # ---- per function-group files (one file per 2nd-level group of each app) ----
    files = defaultdict(list)
    for c in kb.chans:
        key = (c['app'], c['path'][2] if len(c['path']) > 2 else '(racine appli)')
        files[key].append(c)
    index_rows = []
    toc = []
    for (app, grp), chans in sorted(files.items()):
        fname = f"{slug(app)}__{slug(grp)}.md"
        by_sub = defaultdict(list)
        for c in chans:
            by_sub[' / '.join(c['path'][2:]) or '(racine)'].append(c)
        body = [f"# {app} — {grp}", '',
                f"{len(chans)} canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.", '']
        for sub in sorted(by_sub):
            gnode = next((g for g in kb.groups if g['app'] == app and len(g['path']) > 2 and ' / '.join(g['path'][2:]) == sub), None)
            en = '' if not gnode or gnode['enabled'] else ' — **DÉSACTIVÉ**'
            ena = gnode['node']['props'].get('Enabled', 'Yes') if gnode else 'Yes'
            if ena not in ('Yes', 'No'):
                en += f" — actif seulement si `{ena}`"
            body.append(f"## {sub}{en}")
            if gnode and gnode['node']['props'].get('Description'):
                body.append(f"> {gnode['node']['props']['Description']}")
            body.append('')
            for c in by_sub[sub]:
                body.append(kb.card(c))
                body.append('')
                index_rows.append([c['app'], ' / '.join(c['path'][1:]), c['name'], c['kind'], c['id'],
                                   c['node']['line'], len(kb.uses[c['id']]),
                                   len(kb.used_by.get(c['id'], ())) + len(kb.used_by_ui.get(c['id'], ())),
                                   'oui' if c['enabled'] else 'non', fname])
        open(os.path.join(out, 'fonctions', fname), 'w', encoding='utf-8').write('\n'.join(body))
        toc.append((app, grp, len(chans), fname))
    with open(os.path.join(out, 'index_canaux.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(['appli', 'chemin', 'nom', 'type', 'id', 'ligne', 'nb_entrees', 'nb_utilisateurs', 'actif', 'fichier'])
        w.writerows(index_rows)
    json.dump({'toc': toc}, open(os.path.join(out, '_toc.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    # graph export for later threads
    graph = [{'id': c['id'], 'app': c['app'], 'name': c['name'], 'kind': c['kind'],
              'path': c['path'][1:], 'enabled': c['enabled'], 'uses': kb.uses[c['id']],
              'used_by': sorted(kb.cid[u]['name'] for u in kb.used_by.get(c['id'], ())),
              'used_by_ui': sorted(kb.used_by_ui.get(c['id'], ())), 'line': c['node']['line']}
             for c in kb.chans]
    json.dump(graph, open(os.path.join(out, 'graphe_dependances.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    import pickle
    pickle.dump(kb, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kb.pkl'), 'wb'))
    print('files', len(toc), 'channels', len(kb.chans), 'nonchan users', len(kb.nonchan_users))


if __name__ == '__main__':
    main()
