"""Lot 2 : modifications de propriétés d'objets dans une copie du projet MD3.
E1 : IDC "Inter DOWN Delay" (8658), Delay on 1000 -> 1500 ms (même taille).
E2 : IDC "ALL ASK STOP" (6352), Function selector "Command State" -> "Not used" (taille différente).
Usage (depuis Documents\\testia) : python essais_format\\outils\\faire_lot2.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.dirname(HERE)]  # outils_format/ (dépôt) ou même dossier (PC)
import iqanprj, iqanobj

SRC = "avecMD3_V69.03.01.WIP.idax"
OUT = os.path.join("essais_format", "lot2")
H = bytes.fromhex
EDITS = {
    "E1_md3_delai_1500.idax": [(H("0406 0000 cb007500 cb004900 cd0000 c9e8030000"),
                                H("0406 0000 cb007500 cb004900 cd0000 c9dc050000"))],
    "E2_md3_selecteur_retire.idax": [(H("0406 0000 cb006900 cb004900 cd0000 c900000000 c9f4010000 cf0453000000"),
                                      H("0406 0000 cb006900 cb004900 cd0000 c900000000 c9f4010000 cd3600"))],
}
os.makedirs(OUT, exist_ok=True)
for name, edits in EDITS.items():
    p = iqanprj.Project(SRC)
    done = 0
    for s in p.sections:
        if s.tag in (0xB5, 0xCA, 0xC8):
            bl = iqanobj.Block(s.data)
            for r in bl.records:
                if r[0] == 0x97:
                    for old, new in edits:
                        if old in r[1]:
                            assert r[1].count(old) == 1
                            r[1] = r[1].replace(old, new)
                            done += 1
            s.data = bl.encode()
    assert done == len(edits), (name, done)
    p.save(os.path.join(OUT, name))
    print("écrit", name)
