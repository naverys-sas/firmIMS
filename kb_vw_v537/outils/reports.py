"""Write interface and configuration reports (I/O, CAN, app links, variants, adjust menus).

Usage: python -I reports.py export.txt kb_dir
"""
import os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_build import KB  # noqa: E402

IO_KINDS = {'DOUT', 'DIN', 'VIN', 'CIN', 'FIN', 'PWM', 'COUT', 'VOUT', 'PCOUT', 'TEMP', 'RIN', 'SIN', 'VREF', 'MDGN', 'SIC'}
CAN_KINDS = {'GFIN', 'GFOUT', 'JFIN', 'JFOUT', 'JPIN', 'JPOUT', 'TSC1', 'DM1IN', 'DM1OUT', 'SPN', 'NMEAIN', 'NMEAOUT'}


def main():
    src, out = sys.argv[1], sys.argv[2]
    kb = KB(src)
    P = lambda c, k, d='': c['node']['props'].get(k, d)
    grp = lambda c: ' / '.join(c['path'][2:]) or '(racine)'

    # ---------------- interfaces ----------------
    L = ['# Interfaces matérielles et CAN — v117', '',
         "Généré par `tools/reports.py`. Les identifiants viennent de l'export texte ; "
         "le bus et le module sont ceux déclarés sur chaque canal.", '']
    L += ['## Modules', '']
    for top in kb.root['children']:
        if top['type'] == 'Module container':
            for m in top['children']:
                L.append(f"- **{m['props'].get('Name')}** ({m['type']})" +
                         (f" — {m['props']['Description']}" if m['props'].get('Description') else ''))
        if top['type'] == 'CAN bus container':
            L += ['', '## Bus CAN déclarés', '']
            for b in top['children']:
                pr = ' · '.join(f"{k}={v}" for k, v in b['props'].items() if k not in ('Name', 'Description') and v)
                L.append(f"- **{b['props'].get('Name')}** ({b['type']}) {pr}")
    L += ['', '## Entrées / sorties physiques', '', '| Appli | Groupe | Canal | Type | Module | Index | Entrée / source |', '|---|---|---|---|---|---|---|']
    for c in sorted(kb.chans, key=lambda c: (c['app'], P(c, 'Module'), int(P(c, 'Module index', '0') or 0) if P(c, 'Module index', '0').isdigit() else 0)):
        if c['kind'] in IO_KINDS or (P(c, 'Module') and c['kind'] not in CAN_KINDS and c['kind'] not in ('GPIN', 'GPOUT')):
            L.append(f"| {c['app']} | {grp(c)} | {c['name']} | {c['kind']} | {P(c, 'Module')} | {P(c, 'Module index')} | {P(c, 'Input channel')} |")
    L += ['', '## Trames CAN', '', '| Appli | Groupe | Trame | Sens | Module | Identifiant | Période / timeout | Contenu |', '|---|---|---|---|---|---|---|---|']
    for c in sorted(kb.chans, key=lambda c: (P(c, 'Module'), P(c, 'Identifier'))):
        if c['kind'] in CAN_KINDS:
            sens = 'reçue' if c['kind'].endswith('IN') or c['kind'] in ('SPN',) else 'émise'
            per = P(c, 'Transmit rate') if sens == 'émise' else P(c, 'Timeout')
            params = re.findall(r'\{([^;{}]+);', P(c, 'Parameters'))
            ident = P(c, 'Identifier') or P(c, 'PGN')
            L.append(f"| {c['app']} | {grp(c)} | {c['name']} | {sens} | {P(c, 'Module')} | {ident} | {per} | {', '.join(params)[:120]} |")
    L += ['', '## Liaisons entre applications (APPOUT → APPIN)', '']
    outs = {c['name']: c for c in kb.chans if c['kind'] == 'APPOUT'}
    for c in kb.chans:
        if c['kind'] == 'APPIN':
            src_name = re.sub(r'\s*\[[^\]]*\]$', '', P(c, 'Input channel'))
            o = outs.get(src_name)
            L.append(f"- {o['app'] if o else '?'} `{src_name}` (← `{P(o, 'Input channel') if o else '?'}`) → {c['app']} `{c['name']}`")
    open(os.path.join(out, 'interfaces.md'), 'w', encoding='utf-8').write('\n'.join(L))

    # ---------------- configuration ----------------
    L = ['# Configuration, variantes et réglages — v117', '',
         "Les **sélecteurs** sont les paramètres d'état (SP) qui choisissent la fonction active d'un canal : "
         "ce sont eux qui rendent le même logiciel compatible avec plusieurs équipements. "
         "Toute v2 doit conserver chacun de ces choix (voir `v2/compatibilite.md`).", '', '## Sélecteurs de variante (paramètres réglables)', '']
    sel = defaultdict(list)
    for c in kb.chans:
        s = P(c, 'Function selector') or P(c, 'Mode selector')
        if s and s != 'Not used':
            sel[s].append(c)
    for s, lst in sorted(sel.items(), key=lambda x: -len(x[1])):
        srcs = kb.resolve(lst[0], s)
        if not srcs or srcs[0]['kind'] not in ('SP',):
            continue
        sp = srcs[0]
        states = [P(sp, 'Default state name')] + re.findall(r'[^{};]+', P(sp, 'States').strip('{}'))
        states = [x.strip() for x in states if x.strip()]
        adj = sorted(l for l in kb.used_by_ui.get(sp['id'], ()) if 'adjust' in l)
        L.append(f"### {s}")
        L.append(f"- Valeurs : " + ' · '.join(f"{i}={x}" for i, x in enumerate(states)) + f" (défaut {states[0]})")
        L.append(f"- Défini dans : {grp(sp)} ({sp['app']})" + (f" · entrée auto : `{P(sp, 'Input channel')}`" if P(sp, 'Input channel') not in ('', 'None') else ''))
        L.append(f"- Réglable via : {', '.join(adj) if adj else '*(aucun menu)*'}")
        L.append(f"- Canaux qui changent de logique ({len(lst)}) : " + ', '.join(f"`{c['name']}`" for c in lst))
        L.append('')
    L += ['## Menus de réglage (Adjust groups)', '']
    items = {}
    for top in kb.root['children']:
        if top['type'] == 'Adjust item container':
            for it in top['children']:
                items[it['id']] = it
    for top in kb.root['children']:
        if top['type'] == 'Adjust group container':
            for g in top['children']:
                L.append(f"### {g['props'].get('Name')}")
                for k, v in g['props'].items():
                    if k not in ('Name', 'Description') and v:
                        L.append(f"- {k} = {v}")
                for s in g['sub'][:60]:
                    L.append(f"  - {s}")
                its = [c['props'].get('Adjust item') or c['props'].get('Name') for c in g['children']]
                if its:
                    L.append('- Contenu : ' + ', '.join(f"`{x}`" for x in its))
                L.append('')
    L += ['## Tous les réglages (Adjust items) et le canal qu’ils modifient', '', '| Réglage | Canal | Visible | Actif |', '|---|---|---|---|']
    for it in items.values():
        p = it['props']
        L.append(f"| {p.get('Name')} | {p.get('Channel', p.get('Channel 1', ''))} | {p.get('Visible', '')} | {p.get('Enabled', '')} |")
    open(os.path.join(out, 'configuration.md'), 'w', encoding='utf-8').write('\n'.join(L))
    print('ok')


if __name__ == '__main__':
    main()
