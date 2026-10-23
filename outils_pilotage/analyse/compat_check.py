"""Compatibility contract between two IQANdesign exports (reference vs candidate).

Extracts what the installed fleet depends on and reports every removal or change:
stored parameters (name, type, states order, unit), adjust items, CAN frames (id, direction,
content layout), physical pins, error messages, logs, inter-application links.

Usage: python -I compat_check.py reference.txt candidate.txt report.md [--ignore-app]
--ignore-app compares by element name only (for projects whose applications are named differently).
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_build import KB  # noqa: E402

PARAM_KINDS = {'SP', 'IP', 'FP', 'DP', 'TP', 'SIP', 'PCC'}
CAN_KINDS = {'GFIN', 'GFOUT', 'JFIN', 'JFOUT', 'JPIN', 'JPOUT', 'TSC1', 'DM1IN', 'SPN', 'GPIN', 'GPOUT'}
PIN_KINDS = {'DOUT', 'DIN', 'VIN', 'VIN32', 'CIN', 'FIN', 'PWM', 'COUT', 'VOUT', 'PCOUT', 'VDIN', 'MDGN'}


def contract(path):
    kb = KB(path)
    P = lambda c, k: c['node']['props'].get(k, '')
    C = {}
    for c in kb.chans:
        k = c['kind']
        if k in PARAM_KINDS:
            subs = [s for s in c['node']['sub'] if s.startswith('State ')]
            C[('Paramètre', c['app'], c['name'])] = (
                f"{k} unité={P(c, 'Unit')} défaut={P(c, 'Default state name') or P(c, 'Default mode')} "
                f"états={'|'.join(s.split('=', 1)[1] for s in subs)} modes={P(c, 'Mode selector')}")
        elif k in CAN_KINDS:
            if k in ('GPIN', 'GPOUT'):
                C[('Signal CAN', c['app'], c['name'])] = f"{k} longueur={P(c, 'Length')} type={P(c, 'Type')} unité={P(c, 'Unit')}"
            else:
                C[('Trame CAN', c['app'], c['name'])] = (
                    f"{k} module={P(c, 'Module')} id={P(c, 'Identifier') or P(c, 'PGN')} dlc={P(c, 'Data length')} "
                    f"contenu={P(c, 'Parameters')}")
        elif k in PIN_KINDS and P(c, 'Module'):
            C[('Broche', c['app'], f"{P(c, 'Module')}#{P(c, 'Module index')}")] = f"{k} {c['name']}"
        elif k in ('CMSG', 'IMSG'):
            h = P(c, 'Header, English') or P(c, 'Header')
            C[('Message', c['app'], c['name'])] = f"{h} | {P(c, 'Dialog type')}"
        elif k in ('APPIN', 'APPOUT'):
            C[('Liaison appli', c['app'], c['name'])] = f"{k} ← {P(c, 'Input channel')}"
    for label, n in kb.nonchan_users:
        if label.startswith(('Single adjust item', 'Dual adjust item')):
            C[('Réglage', '', n['props'].get('Name'))] = n['props'].get('Channel', '') + ' ' + n['props'].get('Channel 1', '')
        elif 'log' in label.lower():
            C[('Journal', '', label)] = ''
    return C


def main():
    ref, cand, out = sys.argv[1:4]
    A, B = contract(ref), contract(cand)
    if '--ignore-app' in sys.argv:
        A = {(k[0], '', k[2]): v for k, v in A.items()}
        B = {(k[0], '', k[2]): v for k, v in B.items()}
    removed = sorted((k for k in A if k not in B), key=str)
    added = sorted((k for k in B if k not in A), key=str)
    changed = sorted((k for k in A if k in B and A[k] != B[k]), key=str)
    L = [f"# Contrôle de compatibilité", '', f"- Référence : `{ref}`", f"- Candidat : `{cand}`", '',
         f"**{len(removed)} éléments supprimés, {len(changed)} modifiés, {len(added)} ajoutés.** "
         "Un élément supprimé ou modifié casse potentiellement un bateau déjà livré ; il doit être justifié.", '']
    for title, keys, fmt in (('Supprimés', removed, lambda k: f"- {k[0]} · {k[1]} · `{k[2]}` — était : {A[k]}"),
                             ('Modifiés', changed, lambda k: f"- {k[0]} · {k[1]} · `{k[2]}`\n  - avant : {A[k]}\n  - après : {B[k]}"),
                             ('Ajoutés', added, lambda k: f"- {k[0]} · {k[1]} · `{k[2]}` — {B[k]}")):
        L += [f"## {title} ({len(keys)})", '']
        L += [fmt(k) for k in keys]
        L.append('')
    open(out, 'w', encoding='utf-8').write('\n'.join(L))
    print(len(A), 'éléments de contrat ;', len(removed), 'supprimés', len(changed), 'modifiés', len(added), 'ajoutés')


if __name__ == '__main__':
    main()
