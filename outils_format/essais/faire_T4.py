"""Fabrique T4 sur le PC (fichier trop gros pour être transféré) :
copie de v2\\projet\\v2_mc42.idax avec la faute 'temparture' corrigée dans un message.
Usage (depuis Documents\\testia) : python essais_format\\outils\\faire_T4.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.dirname(HERE)]  # outils_format/ (dépôt) ou même dossier (PC)
import iqanprj, iqanstr
src = os.path.join("v2", "projet", "v2_mc42.idax")
dst = os.path.join("essais_format", "lot1", "T4_v2_faute_corrigee.idax")
p = iqanprj.Project(src)
n = 0
for s in p.sections:
    if s.tag in (0xC6, 0xCB):
        h, langs = iqanstr.parse(s.data)
        for lg in langs:
            for k, x in enumerate(lg.strings):
                if x == "Engine temparture critical. Derating power":
                    lg.strings[k] = "Engine temperature critical. Derating power"
                    n += 1
        s.data = iqanstr.encode(h, langs)
assert n == 1, n
p.save(dst)
print("écrit", dst)
