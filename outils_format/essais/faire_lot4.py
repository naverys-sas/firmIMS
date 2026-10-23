"""Lot 4 : opérations de l'éditeur (iqanprojet.py) sur des copies du projet MD3 V69.

Chaque fichier ne contient qu'une opération, pour que l'export texte d'IQANdesign montre
exactement son effet :
  L4a  renommer le canal « Inter DOWN Delay » (8658) en « Inter DOWN Delay CLAUDE » et passer
       sa temporisation Delay on de 1000 à 1500 ms
  L4b  copier le paramètre « Can Speed » (36114) au milieu du groupe Translate (avant le
       commentaire 67563), sous le nom « CLAUDE test IP » : les canaux suivants sont renumérotés
  L4c  supprimer le canal inutilisé « oldExhaust Temperature State » (66743, groupe Power)
  L4d  déplacer le canal « MD3 START » (30656) du groupe Power à la fin du groupe Translate
  L4e  copier tout le groupe BUZZER (8794) dans l'application MC42, sous le nom « BUZZER copie »,
       chaque canal copié étant renommé « ... copie »
  L4f  remplacer le groupe RADIO (7116) par celui du projet X100 V35.42, en gardant les
       identifiants des canaux de même nom (les réglages des machines restent attachés)

Usage (depuis la racine du dépôt) : python outils_format/essais/faire_lot4.py [dossier de sortie]"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.dirname(HERE)]
import iqanprojet  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "avecMD3_V69.03.01.WIP.idax")
X100 = os.path.join(ROOT, "docs", "versions_firmware", "X100 C V35.42.idax")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "essais_format", "lot4")


def one(pr, oid):
    found = pr.by_oid(oid)
    if len(found) != 1:
        raise SystemExit("objet %d : %d occurrences" % (oid, len(found)))
    return found[0]


def l4a(pr):
    sec, n = one(pr, 8658)
    pr.set_text(sec, n, 0, "Inter DOWN Delay CLAUDE")
    pr.set_int(n, 3, 1500)


def l4b(pr):
    sec, grp = one(pr, 24950)
    anchor = next(c for c in grp.children if c.oid == 67563)
    s, tpl = one(pr, 36114)
    new = pr.clone(pr, s, tpl, sec)
    pr.set_text(sec, new, 0, "CLAUDE test IP")
    pr.insert(sec, grp, new, before=anchor)


def l4c(pr):
    pr.remove(*one(pr, 66743))


def l4d(pr):
    sec, n = one(pr, 30656)
    _, grp = one(pr, 24950)
    pr.move(sec, n, grp)


def l4e(pr):
    sec, grp = one(pr, 8794)
    new = pr.clone(pr, sec, grp, sec)
    pr.set_text(sec, new, 0, pr.name(sec, grp) + " copie")
    for x in new.walk():
        if x.cls == 0x04:
            pr.set_text(sec, x, 0, pr.name(sec, x) + " copie")
    pr.insert(sec, grp.parent, new)


def l4f(pr):
    src = iqanprojet.Projet(X100)
    ss, sn = one(src, 7116)
    sec, old = one(pr, 7116)
    pr.replace(sec, old, src, ss, sn)


TESTS = [("L4a_renommer_valeur", l4a), ("L4b_copier_canal_milieu", l4b), ("L4c_supprimer_canal", l4c),
         ("L4d_deplacer_canal", l4d), ("L4e_copier_groupe", l4e), ("L4f_remplacer_groupe_X100", l4f)]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, op in TESTS:
        pr = iqanprojet.Projet(SRC)
        op(pr)
        path = os.path.join(OUT, name + ".idax")
        pr.save(path)
        iqanprojet.Projet(path)  # relecture : références et numérotation cohérentes
        print("écrit", path)
