"""Make a simulation copy of a project set up as one boat configuration (a profile).

IQANsimulate does not let a script change parameters (SetComponentValue on SP/DP is ignored),
and a State parameter always starts on its default state. So, in a COPY only:
- for a State parameter (SP) whose wanted state is not the default one, a State machine channel
  "SIM <name>" with the same states is created, always in the wanted state, and every logic
  reference to the SP in the MC42 application (operands, function selectors, expressions) is
  pointed to it. The SP and its settings-menu items stay as they are: an SP with an input
  channel is refused by IQANdesign ("Invalid context", "Not adjustable"), and removing adjust
  items corrupts the file (adjust group items point to them by position);
- a Digital parameter (DP) gets the wanted default value.
The new channels go at the root of the MC42 application, the only place every group can see.
Never run on an original project: the copy is only for IQANsimulate, never for a boat.

python -I profil_copie.py <base.idax> <profil.json> <copie.idax>
"""
import json
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'outils_format'))
import assembler_v2  # noqa: E402
import iqanprojet  # noqa: E402

SP, DP, EXPR = 0x28, 0x31, 0x3A
REGLAGES = (0x13, 0x2C)  # Single adjust item, Adjust group item: keep pointing to the SP


def etats_sp(pr, sec, ch):
    """Default state name, then the names of the state list (values[4] = d2 count, cb text...)."""
    noms = [pr.text(sec, ch, 3)]
    v = ch.obj.values[4]
    k = struct.unpack_from('<H', v, 1)[0]
    for i in range(k):
        idx = struct.unpack_from('<H', v, 3 + 4 * i + 2)[0]
        noms.append(pr.strtab[sec][1][0].strings[idx])
    return noms


def rediriger(pr, sec, ancien, nouveau):
    """Point every reference to ancien inside the MC42 logic to nouveau. Returns the count."""
    vieux = bytes([0xCF, iqanprojet.REF]) + struct.pack('<I', ancien)
    neuf = bytes([0xCF, iqanprojet.REF]) + struct.pack('<I', nouveau)
    jeton_v, jeton_n = '{#%d#}' % ancien, '{#%d#}' % nouveau
    total = 0
    for _, n in pr.walk([sec]):
        if n.oid in (ancien, nouveau) or n.cls in REGLAGES:
            continue
        for i, v in enumerate(n.obj.values):
            if v == vieux:
                n.obj.values[i] = neuf
                total += 1
            elif n.cls == EXPR and v[:1] == b'\xcb':
                t = pr.text(sec, n, i)
                if jeton_v in t:
                    pr.set_text(sec, n, i, t.replace(jeton_v, jeton_n))
                    total += 1
    return total


def main(base, profil_path, out):
    if os.path.abspath(base) == os.path.abspath(out):
        raise SystemExit('Refus : la copie doit etre un autre fichier que le projet de base.')
    profil = json.load(open(profil_path, encoding='utf-8-sig'))
    a = assembler_v2.Assembleur(base)
    pr, sec = a.pr, a.sec
    app = next(t for t in pr.trees(sec) if (t.cls, t.sub) == (0x2A, 0x00))
    groupe = app  # racine de l'appli : un canal range dans un groupe n'est pas visible des autres (Invalid context)
    faits, redirections = [], []
    for nom, valeur in profil.get('parametres', {}).items():
        trouves = [n for _, n in pr.find(nom, [sec]) if n.cls == 0x04 and n.sub in (SP, DP)]
        if len(trouves) != 1:
            faits.append('%s : %d parametre(s) de ce nom, ignore' % (nom, len(trouves)))
            continue
        ch = trouves[0]
        if ch.sub == DP:
            ch.obj.values[5] = b'\xd2\x01\x00\xcd' + struct.pack('<H', 3 if valeur else 2)
            faits.append('%s (DP) : defaut %s' % (nom, bool(valeur)))
            continue
        etats = etats_sp(pr, sec, ch)
        valeur = int(valeur)
        if valeur == 0:
            faits.append('%s (SP) : deja sur son etat par defaut %s' % (nom, etats[0]))
            continue
        if valeur >= len(etats):
            faits.append('%s (SP) : etat %d inexistant (%s), ignore' % (nom, valeur, ' | '.join(etats)))
            continue
        lignes = [{'group': '', 'channel': 'SIM ' + nom, 'type': 'SMC', 'unit': '',
                   'description': 'Jumeau : %s force sur %s (copie de simulation)' % (nom, etats[valeur]) if i == 1 else '',
                   'selector': '', 'function': etats[i], 'activating': 'True' if i == valeur else 'False',
                   'blocking': '', 'properties': 'Default state name=%s' % etats[0] if i == 1 else '', 'origin': ''}
                  for i in range(1, len(etats))]
        a.canal(groupe, lignes, sum(1 for x in groupe.children if x.cls == 0x04))
        redirections.append((nom, ch.oid, a.noms['SIM ' + nom], etats[valeur]))
    for f in a.differe:
        f()
    for nom, ancien, nouveau, etat in redirections:
        n = rediriger(pr, sec, ancien, nouveau)
        faits.append('%s (SP) : %d reference(s) vers SIM %s, toujours sur %s' % (nom, n, nom, etat))
    pr.save(out)
    iqanprojet.Projet(out)  # relecture : CRC et structure
    print('\n'.join(faits))
    print('Copie de simulation : %s' % out)


if __name__ == '__main__':
    main(*sys.argv[1:4])
