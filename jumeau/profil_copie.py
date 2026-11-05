"""Make a simulation copy of a project set up as one boat configuration (a profile).

IQANsimulate does not let a script change parameters (SetComponentValue on SP/DP is ignored),
and a State parameter always starts on its default state. So, in a COPY only:
- a State parameter (SP) gets as input channel a new Integer parameter "SIM <name>" whose
  default value is the wanted state number (an SP with an input channel follows it, like
  em M-Pump - Brand follows is_x100_math in the 108.3.1);
- a Digital parameter (DP) gets the wanted default value.
The new channels go in a function group "SIM jumeau" at the end of the MC42 application.
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

SP, DP = 0x28, 0x31


def main(base, profil_path, out):
    if os.path.abspath(base) == os.path.abspath(out):
        raise SystemExit('Refus : la copie doit etre un autre fichier que le projet de base.')
    profil = json.load(open(profil_path, encoding='utf-8-sig'))
    a = assembler_v2.Assembleur(base)
    pr, sec = a.pr, a.sec
    app = next(t for t in pr.trees(sec) if (t.cls, t.sub) == (0x2A, 0x00))
    groupe = a.groupe(app, 'SIM jumeau', len(app.children))
    faits = []
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
        ligne = {'group': '', 'channel': 'SIM ' + nom, 'type': 'IP', 'unit': '',
                 'description': 'Jumeau : etat force de %s (copie de simulation)' % nom,
                 'selector': '', 'function': '', 'activating': str(int(valeur)), 'blocking': '',
                 'properties': '', 'origin': ''}
        a.canal(groupe, [ligne], sum(1 for x in groupe.children if x.cls == 0x04))
        cree = a.noms['SIM ' + nom]
        pr.set_ref(ch, 2, cree)
        faits.append('%s (SP) : suit SIM %s = %d' % (nom, nom, int(valeur)))
    for f in a.differe:
        f()
    pr.save(out)
    iqanprojet.Projet(out)  # relecture : CRC et structure
    print('\n'.join(faits))
    print('Copie de simulation : %s' % out)


if __name__ == '__main__':
    main(*sys.argv[1:4])
