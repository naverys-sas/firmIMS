"""Lot 5 : IQANdesign 6.08 connaît-il une méthode « Expression » pour les groupes d'objets ?

Chaque groupe d'objets a un champ texte « Expression », vide dans tous nos projets, et les
méthodes connues ont les codes 90 à 96. Les feuilles de la v2 écrivent les conditions comme des
expressions (« Drive Type mc = 0 »). Si IQANdesign les accepte, l'outil peut les écrire telles
quelles au lieu de les traduire en objets.

Sur une copie de TESTIA (108.3.1), groupe « Activating » (229603) du canal is_x100_mc_s, qui
contient l'objet simple A (is_x100_mc) :
  L5_texte        méthode And inchangée, Expression = « A »
  L5_code_NN      méthode = code NN (codes inconnus voisins), Expression = « A »
L'export texte montre le nom de la méthode et l'expression relue.

Usage (depuis la racine du dépôt) : python outils_format/essais/faire_lot5.py [dossier de sortie]"""
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.dirname(HERE)]
import iqanprojet  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "TESTIA.idax")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "essais_format", "lot5")
CODES = [86, 87, 88, 89, 97, 98, 99, 100, 101, 102]


def faire(code):
    pr = iqanprojet.Projet(SRC)
    (sec, g), = pr.by_oid(229603)
    pr.set_text(sec, g, 4, "A")
    if code is not None:
        g.obj.values[2] = b"\xcd" + struct.pack("<H", code)
    return pr


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for code in [None] + CODES:
        name = "L5_texte" if code is None else "L5_code_%d" % code
        path = os.path.join(OUT, name + ".idax")
        faire(code).save(path)
        iqanprojet.Projet(path)
        print("écrit", path)
