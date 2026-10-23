"""Lot 6 : groupes « Expression » d'IQANdesign (classe 3a), écrits par l'outil.

Un groupe d'objets peut avoir la méthode Expression (énuméré 423) : son texte (valeur 4) est
du script IQAN (« Result := ({#237945#} mod 4) = 0 », canaux désignés par {#identifiant#}) et ses
enfants sont la forme compilée (un objet par opération). La 108.3.1 en compte 736. Questions :
IQANdesign recompile-t-il les enfants à partir du texte au chargement ? Accepte-t-il un groupe
expression créé par l'outil sans enfants ?

Sur des copies de TESTIA (108.3.1) :
  L6a  groupe 237963 « Result := ({#237945#} mod 4) = 0 » : texte changé en « = 1 », enfants
       inchangés (le texte et les enfants ne concordent plus)
  L6b  même changement de texte, enfants supprimés
  L6c  canal is_x100_mc_s (229598) : ses groupes Activating/Blocking (Or/And) remplacés par des
       groupes expression, Activating = « Result := {#169733#} » (is_x100_mc), sans enfants
  L6d  comme L6c, avec l'enfant compilé par l'outil (objet simple vers is_x100_mc)
  L6e  comme L6c, Activating = « Result := {#202379#} = 0 » (Drive Type mc = 0), sans enfants
  L6f  comme L6c, Activating = « Result := PositiveFlank({#169733#}) », sans enfants

Sur le PC : export texte de chaque fichier et réenregistrement (-saveas en .idax), pour voir si
IQANdesign a reconstruit les enfants.

Usage (depuis la racine du dépôt) : python outils_format/essais/faire_lot6.py [dossier de sortie]"""
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.dirname(HERE)]
import iqanprojet  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "TESTIA.idax")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "essais_format", "lot6")


def one(pr, oid):
    found = pr.by_oid(oid)
    if len(found) != 1:
        raise SystemExit("objet %d : %d occurrences" % (oid, len(found)))
    return found[0]


def l6a(pr):
    sec, g = one(pr, 237963)
    pr.set_text(sec, g, 4, "Result := ({#237945#} mod 4) = 1")


def l6b(pr):
    l6a(pr)
    _, g = one(pr, 237963)
    g.children = []


def en_expression(pr, texte, enfant=None):
    """Remplace les groupes du canal 229598 par une copie des groupes expression du canal
    « B12 45 State ok C10 » (226741 Activating, son voisin Blocking vide)."""
    sec, fn = one(pr, 229602)
    _, modele = one(pr, 226741)
    act = pr.clone(pr, sec, modele, sec)
    blk = pr.clone(pr, sec, modele.parent.children[1], sec)
    act.children = []
    pr.set_text(sec, act, 4, texte)
    if enfant is not None:
        ss, src = one(pr, enfant)
        c = pr.clone(pr, ss, src, sec)
        c.oid = act.oid + 2
        c.obj.values[2] = b"\xcf\xff" + struct.pack("<I", 169733)
        c.parent = act
        c.idx = 0
        act.children = [c]
    for old in list(fn.children):
        pr.remove(sec, old)
    pr.insert(sec, fn, act)
    blk.oid = act.oid + 1
    pr.insert(sec, fn, blk)


TESTS = [
    ("L6a_texte_change", l6a),
    ("L6b_texte_sans_enfants", l6b),
    ("L6c_idc_expression", lambda pr: en_expression(pr, "Result := {#169733#}")),
    ("L6d_idc_expression_compilee", lambda pr: en_expression(pr, "Result := {#169733#}", enfant=233847)),
    ("L6e_idc_comparaison", lambda pr: en_expression(pr, "Result := {#202379#} = 0")),
    ("L6f_idc_flanc", lambda pr: en_expression(pr, "Result := PositiveFlank({#169733#})")),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, op in TESTS:
        pr = iqanprojet.Projet(SRC)
        op(pr)
        path = os.path.join(OUT, name + ".idax")
        pr.save(path)
        iqanprojet.Projet(path)
        print("écrit", path)
