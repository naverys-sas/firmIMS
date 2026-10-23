"""Automatic anomaly scan over an IQANdesign text export. Writes anomalies_auto.md.

Usage: python -I anomalies.py export.txt kb_dir
"""
import os, re, sys
from collections import defaultdict, Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_build import KB, OBJ_TYPES, OUTPUT_KINDS, NUM, CONSTS, strip_unit  # noqa: E402

SUSPECT_WORDS = re.compile(r'\b(wip|broken|broek|soon|test|debug|todo|tmp|old|bug|sim|fix|temp)\b', re.I)


def objects(n):
    for c in n['children']:
        if c['type'] in OBJ_TYPES:
            yield c
        elif c['type'] in ('Function', 'Object group', 'State', 'Transition'):
            yield from objects(c)


def groups(n):
    for c in n['children']:
        if c['type'] == 'Object group':
            yield c
        elif c['type'] in ('Function', 'State', 'Transition'):
            yield from groups(c)


def main():
    src, out = sys.argv[1], sys.argv[2]
    kb = KB(src)
    R = defaultdict(list)
    loc = lambda c: f"`{c['name']}` ({c['kind']}, {' / '.join(c['path'][1:])}, l.{c['node']['line']})"

    for c in kb.chans:
        n = c['node']
        users = kb.used_by.get(c['id'], set()) | kb.used_by_ui.get(c['id'], set())
        # 1. dead channels
        if not users and c['kind'] not in OUTPUT_KINDS and c['kind'] not in ('GFIN', 'JFIN', 'SIC'):
            R['dead'].append(c)
        # 2. dangling references inside object lists
        for o in objects(n):
            p = o['props']
            names_in_group = None
            for k in ('Input', 'Operand 1', 'Operand 2', 'Operand 3'):
                v = p.get(k)
                if v is None:
                    continue
                v2 = strip_unit(v)
                if v2 in CONSTS or NUM.match(v2) or re.fullmatch(r'[A-Z]{1,2}', v2) or ':' in v2:
                    continue
                if v2 not in kb.global_names:
                    R['dangling'].append((c, k, v))
                elif not kb.by_name.get((c['app'], v2)):
                    R['crossapp'].append((c, v2))
        # 3. empty logic: channel with functions but every object group empty
        fns = [f for f in n['children'] if f['type'] == 'Function']
        if fns and not any('qcode' in f for f in fns):
            if all(not any(True for _ in objects(f)) for f in fns):
                R['empty'].append(c)
            else:
                emptyf = [f['props'].get('Name') for f in fns if not any(True for _ in objects(f))]
                if emptyf and len(fns) > 1:
                    R['empty_modes'].append((c, emptyf))
        # 4. constant / always-true activations
        for g in groups(n):
            gname = g['props'].get('Name')
            for o in g['children']:
                if o['type'] == 'Single object' and o['props'].get('Input', '').strip() in ('True', '1') \
                        and gname in ('Activating', 'Increasing', 'Showing'):
                    R['const_true'].append((c, gname))
                if o['type'] == 'Single object' and o['props'].get('Input', '').strip() in ('False', '0') \
                        and gname in ('Activating', 'Showing'):
                    R['const_false'].append((c, gname))
        # 5. IMSG/CMSG without showing condition
        if c['kind'] in ('IMSG', 'CMSG'):
            show = [g for g in groups(n) if g['props'].get('Name') == 'Showing' and g['children']]
            if not show:
                R['msg_never'].append(c)
        # 6. Qcode checks
        for f in fns:
            q = f.get('qcode')
            if not q:
                continue
            q = re.sub(r'//[^\n]*', '', q)
            ql = q.lower()
            if re.search(r'\bif\b', ql) and 'else' not in ql and 'result' in ql and not re.match(r'\s*result\s*:=', ql):
                R['qcode_noelse'].append(c)
            for mm in re.finditer(r'/\s*([A-Za-z][\w ]*)', q):
                R['qcode_div'].append((c, mm.group(1).strip()))
        # 7. suspicious names
        if SUSPECT_WORDS.search(c['name']):
            R['suspect_name'].append(c)
        # 8. channel referencing itself (outside counters/memories/timers)
        if c['name'] in kb.refs_in(n) and c['kind'] in ('IDC', 'MAC', 'IMAC')                 and not [x for x in kb.by_name.get((c['app'], c['name']), []) if x['id'] != c['id']]:
            R['selfref'].append(c)
        # 9. GFIN without timeout
        if c['kind'] in ('GFIN', 'JFIN') and n['props'].get('Timeout', '1') in ('0', 'Not used', 'None'):
            R['no_timeout'].append(c)
        # 10. disabled-group channel used from enabled logic
        if not c['enabled']:
            for u in kb.used_by.get(c['id'], ()):
                if kb.cid[u]['enabled']:
                    R['disabled_used'].append((c, kb.cid[u]))

    # duplicates within same app
    dup = Counter((c['app'], ' / '.join(c['path'][1:]), c['name']) for c in kb.chans if c['name'])
    R['dup'] = [(a + ' / ' + g, n, k) for (a, g, n), k in dup.items() if k > 1]
    # same name in several apps that is not an APPIN/APPOUT pair
    # CAN identifiers sent twice
    ids = defaultdict(list)
    for c in kb.chans:
        if c['kind'] == 'GFOUT':
            ids[(c['node']['props'].get('Module'), c['node']['props'].get('Identifier'))].append(c)
    R['dup_tx'] = [(k, v) for k, v in ids.items() if len(v) > 1]
    # function groups disabled / suspect
    for g in kb.groups:
        nm = g['node']['props'].get('Name', '')
        if g['node']['props'].get('Enabled') == 'No':
            R['grp_disabled'].append(g)
        if SUSPECT_WORDS.search(nm):
            R['grp_suspect'].append(g)
        if not g['node']['children']:
            R['grp_empty'].append(g)
    # cycles among combinational channels
    comb = {c['id'] for c in kb.chans if c['kind'] in ('IDC', 'MAC', 'IMAC', 'DMAC')}
    adj = {i: [d['id'] for nm in kb.uses[i] for d in kb.resolve(kb.cid[i], nm) if d['id'] in comb] for i in comb}
    idx, low, st, on, sccs, cnt = {}, {}, [], set(), [], [0]
    sys.setrecursionlimit(100000)

    def sc(v):
        idx[v] = low[v] = cnt[0]; cnt[0] += 1; st.append(v); on.add(v)
        for w in adj[v]:
            if w not in idx:
                sc(w); low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            comp = []
            while True:
                w = st.pop(); on.discard(w); comp.append(w)
                if w == v:
                    break
            if len(comp) > 1:
                sccs.append(comp)
    for v in comb:
        if v not in idx:
            sc(v)
    R['cycles'] = sccs

    # adjust items exposing debug/force/test
    for label, n in kb.nonchan_users:
        if label.startswith(('Single adjust item', 'Dual adjust item')) and re.search(r'debug|force|test|sim|trig|mute|inhibit|bypass|bypsass', label, re.I):
            R['adj_debug'].append(label.split(': ', 1)[1])

    # ---------- write ----------
    L = ['# Anomalies détectées automatiquement — v117', '',
         "Liste brute produite par `tools/anomalies.py`. Chaque point est un **indice**, pas une certitude : "
         "voir `anomalies.md` pour la lecture commentée et priorisée.", '']

    def sec(title, items, fmt, limit=400):
        L.append(f"## {title} ({len(items)})")
        L.append('')
        for it in items[:limit]:
            L.append('- ' + fmt(it))
        if len(items) > limit:
            L.append(f"- … {len(items) - limit} de plus")
        L.append('')

    sec('Références vers un nom de canal inexistant (lien cassé)', R['dangling'], lambda x: f"{loc(x[0])} : {x[1]} = `{x[2]}`")
    sec('Canaux qui ne servent à rien (lus par aucun canal, écran, log ou réglage)', sorted(R['dead'], key=lambda c: (c['app'], c['path'])), loc)
    sec('Canaux sans aucune logique (toutes les conditions vides)', R['empty'], loc)
    sec('Modes de fonction vides (le canal reste à 0 dans ces modes)', R['empty_modes'], lambda x: f"{loc(x[0])} : modes vides {x[1]}")
    sec('Messages qui ne peuvent jamais s’afficher (groupe Showing vide)', R['msg_never'], loc)
    sec('Conditions constantes vraies', R['const_true'], lambda x: f"{loc(x[0])} groupe {x[1]}")
    sec('Conditions constantes fausses', R['const_false'], lambda x: f"{loc(x[0])} groupe {x[1]}")
    sec('Noms en double dans un même groupe de fonctions', R['dup'], lambda x: f"{x[0]} : `{x[1]}` ×{x[2]}")
    sec('Boucles de calcul entre canaux combinatoires (1 cycle de retard)', R['cycles'], lambda comp: ' → '.join(f"`{kb.cid[i]['name']}`" for i in comp))
    sec('Canal qui se lit lui-même', R['selfref'], loc)
    sec('Qcode : if sans else (valeur figée si aucune branche)', R['qcode_noelse'], loc)
    sec('Qcode : divisions par un canal (risque de division par zéro)', R['qcode_div'], lambda x: f"{loc(x[0])} : / `{x[1]}`")
    sec('Trames CAN reçues sans timeout (perte de communication non détectée)', R['no_timeout'], loc)
    sec('Même identifiant CAN émis plusieurs fois sur le même module', R['dup_tx'], lambda x: f"{x[0]} : " + ', '.join(loc(c) for c in x[1]))
    sec('Canaux d’un groupe désactivé lus par de la logique active', R['disabled_used'], lambda x: f"{loc(x[0])} ← lu par {loc(x[1])}")
    sec('Groupes de fonctions désactivés', R['grp_disabled'], lambda g: f"{g['app']} : {' / '.join(g['path'][1:])}")
    sec('Groupes de fonctions au nom suspect (WIP, broken, soon, test…)', R['grp_suspect'], lambda g: f"{g['app']} : {' / '.join(g['path'][1:])}")
    sec('Groupes de fonctions vides', R['grp_empty'], lambda g: f"{g['app']} : {' / '.join(g['path'][1:])}")
    sec('Canaux au nom suspect (test, debug, sim, old…)', R['suspect_name'], loc)
    sec('Réglages de mise au point exposés (debug/force/test/sim)', R['adj_debug'], lambda s: s)
    sec('Références à un canal d’une autre application (hors APPIN/APPOUT)', R['crossapp'], lambda x: f"{loc(x[0])} → `{x[1]}`")
    open(os.path.join(out, 'anomalies_auto.md'), 'w', encoding='utf-8').write('\n'.join(L))
    print({k: len(v) for k, v in R.items()})


if __name__ == '__main__':
    main()
