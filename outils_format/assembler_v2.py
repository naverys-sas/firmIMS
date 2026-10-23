"""Assemble la logique v2 (feuilles v2/refonte/spec/*.csv) dans une copie du projet MC42.

    python assembler_v2.py projet_de_base.idax dossier_spec sortie.idax [rapport.md]

Pour chaque ligne de la spec, le canal est créé dans un groupe de fonctions « v2 » à la fin de
l'application MC42, rangé selon la colonne group (« 20 EQP Equipment drivers/21 BAT Battery »).
Chaque canal est copié d'un modèle du projet de base (même classe), puis renommé, décrit, et ses
fonctions sont remplacées :
- IDC, SMC : groupes Expression Activating / Blocking (D43) ;
- MAC, IMAC : groupes Expression Controlling / Limiting ;
- SP, DP, IP : valeur par défaut et liste d'états.
Une formule est traduite en script IQAN (« Result := … », canaux désignés par {#identifiant#}).
Une formule illisible ou qui cite un canal inconnu n'est pas inventée : la fonction reste vide,
la formule d'origine va dans la description de la fonction (« À DÉFINIR : … ») et dans le rapport.
Un canal dont le nom existe déjà dans le projet de base n'est pas recréé (rapport).
Non traités pour l'instant (rapport) : APPIN, APPOUT, FGI (liens entre maîtres)."""
import collections
import csv
import glob
import os
import struct
import sys

import iqanexpr
import iqanprojet
import iqanvaleurs

# modèles pris dans le projet de base (identifiants de la 108.3.1, inchangés dans la v2 en cours)
MODELES = {
    "IDC": 229598,   # is_x100_mc_s : Default function, Activating / Blocking
    "MAC": 129549,   # BMW_-_Battery_InstantVoltage : Default function en Expression
    "IMAC": None,    # cherché : premier IMAC dont la fonction est en Expression
    "SMC": 129029,   # Battery State Feed-Back
    "SP": 202379,    # Drive Type mc
    "DP": 169624,    # is_cab_mc
    "IP": 214593,    # 4ET Timer UP/DOWN
}
FG_MODELE = None     # premier groupe de fonctions 0100 version 0
EXPR_DIGITAL = 226741  # groupe Expression Activating (3a01) ; son voisin = Blocking (3a02)
EXPR_MATH = 129554     # groupe Expression Controlling (3a08) ; son voisin = Limiting (3a09)
PAS_X, PAS_Y, COLONNES = 230, 40, 4


class Assembleur:
    def __init__(self, base):
        self.pr = iqanprojet.Projet(base)
        self.sec = self.pr.masters[0]
        self.rapport = collections.defaultdict(list)
        self.noms = {}  # nom -> identifiant, canaux du maître MC42
        for n in self._canaux():
            self.noms.setdefault(self.pr.name(self.sec, n), n.oid)
        self.existants = set(self.noms)
        self.prochain = self.pr.max_oid() + 1
        self._crees = {}
        self.crees = collections.Counter()
        self.differe = []    # fonctions remplies quand tous les canaux existent (formules)
        self.etats_smc = {}  # états des machines d'état créées : défaut + une fonction par état

    # --- outils -----------------------------------------------------------------------------
    def _canaux(self):
        for _, n in self.pr.walk([self.sec]):
            if n.cls == 0x04:
                yield n

    def un(self, oid):
        if not hasattr(self, "_index"):
            self._index = collections.defaultdict(list)
            for _, n in self.pr.walk([self.sec]):
                self._index[n.oid].append(n)
        if oid not in self._index:  # canal créé par l'assembleur
            return self._crees[oid]
        n, = self._index[oid]
        return n

    def modele(self, typ):
        oid = MODELES[typ]
        if oid is None:
            for n in self._canaux():
                if n.sub == 0x2F and n.children and any(g.cls == 0x3A for g in n.children[0].children):
                    MODELES[typ] = oid = n.oid
                    break
        return self.un(oid)

    def nouveau(self, src):
        """Copie de src avec des identifiants libres, insérée nulle part pour l'instant."""
        n = self.pr.clone(self.pr, self.sec, src, self.sec, first_oid=self.prochain)
        self.prochain += sum(1 for _ in n.walk())
        return n

    def poser(self, parent, n):
        self.pr.insert(self.sec, parent, n, check=False)  # identifiants pris après le maximum du projet

    def texte(self, n, i, t):
        self.pr.set_text(self.sec, n, i, t)

    @staticmethod
    def position(n, k, offset_x=4):
        t = bytearray(n.obj.tail)
        struct.pack_into("<II", t, offset_x, 30 + PAS_X * (k % COLONNES), 20 + PAS_Y * (k // COLONNES))
        n.obj.tail = bytes(t)

    # --- groupes de fonctions ---------------------------------------------------------------
    def groupe(self, parent, nom, k):
        global FG_MODELE
        if FG_MODELE is None:
            FG_MODELE = next(n.oid for _, n in self.pr.walk([self.sec])
                             if (n.cls, n.sub, n.obj.ver) == (0x01, 0x00, 0) and n.children)
        src = self.un(FG_MODELE)
        g = self.nouveau(src)
        for c in list(g.children):
            g.children.remove(c)
        t = g.obj.tail
        q = t.index(b"\0", 10) + 1
        k_out = struct.unpack_from("<H", t, q)[0]
        g.obj.tail = t[:q] + b"\0\0" + t[q + 2 + 4 * k_out:]
        self.texte(g, 0, nom)
        self.texte(g, 1, "")
        self.position(g, k, offset_x=2)
        self.poser(parent, g)
        return g

    # --- expressions --------------------------------------------------------------------------
    def script(self, expr, ou):
        """Script IQAN d'une formule de la spec, ou None (rapport) si elle n'est pas traduisible."""
        if not expr:
            return ""
        try:
            arbre = iqanexpr.parse(expr, self.noms)
        except iqanexpr.ExprError as e:
            self.rapport["Formules à définir"].append("%s : « %s » (%s)" % (ou, expr, e))
            return None
        return "Result := " + iqanexpr.to_iqan(arbre, self.noms.__getitem__)

    def fonctions(self, ch, typ, lignes, etats):
        """Remplace les fonctions du canal ch : une par état du sélecteur (ou Default function)."""
        modele_fn = ch.children[0]
        for c in list(ch.children):
            ch.children.remove(c)
        par_nom = {(l["function"] or "Default function"): l for l in lignes}
        noms = etats or ["Default function"]
        inconnus = set(par_nom) - set(noms)
        if inconnus:
            self.rapport["Fonctions sans état correspondant"].append(
                "%s : %s (états : %s)" % (lignes[0]["channel"], sorted(inconnus), noms))
        digital = typ in ("IDC", "SMC")
        g_src = self.un(EXPR_DIGITAL if digital else EXPR_MATH)
        for nom in noms:
            fn = self.nouveau(modele_fn)
            fn.children = []
            self.texte(fn, 0, nom)
            self.texte(fn, 1, "")
            self.poser(ch, fn)
            l = par_nom.get(nom, {})
            a_faire = []
            for j, col in enumerate(("activating", "blocking")):
                g = self.nouveau(g_src if j == 0 else g_src.parent.children[1])
                g.children = []
                ou = "%s / %s / %s" % (lignes[0]["channel"], nom, col)
                s = self.script((l.get(col) or "").strip(), ou)
                if s is None:
                    a_faire.append("%s : %s" % (col, l[col]))
                    s = ""
                self.texte(g, 4, s)
                self.poser(fn, g)
            if a_faire:
                self.texte(fn, 1, "À DÉFINIR : " + " ; ".join(a_faire))

    def etats(self, selecteur):
        if not selecteur:
            return None
        if selecteur in self.etats_smc:
            return self.etats_smc[selecteur]
        if selecteur not in self.noms:
            self.rapport["Sélecteurs inconnus"].append(selecteur)
            return None
        n = self.trouver(selecteur)
        ctx = self.pr.context(self.sec)
        if n.sub == 0x28:  # SP : état par défaut + liste
            return [self.pr.text(self.sec, n, 3)] + [iqanvaleurs.render(v, ctx) for v in iqanvaleurs.items(n.obj.values[4])]
        if n.sub == 0x14:  # SMC : état par défaut + une fonction par état
            return [self.pr.text(self.sec, n, 2)] + [self.pr.name(self.sec, f) for f in n.children]
        self.rapport["Sélecteurs inconnus"].append("%s (classe %02x)" % (selecteur, n.sub))
        return None

    def trouver(self, nom):
        return self.un(self.noms[nom])

    # --- canaux ------------------------------------------------------------------------------
    def canal(self, parent, lignes, k):
        r = lignes[0]
        typ, nom = r["type"], r["channel"]
        if nom in self.existants:
            self.rapport["Canaux déjà présents (non recréés)"].append("%s (%s)" % (nom, typ))
            return
        if typ not in MODELES:
            self.rapport["Types non traités"].append("%s (%s)" % (nom, typ))
            return
        ch = self.nouveau(self.modele(typ))
        self.texte(ch, 0, nom)
        self.texte(ch, 1, r["description"])
        self.position(ch, k)
        props = dict(p.split("=", 1) for p in (r["properties"] or "").split(" & ") if "=" in p)
        if typ == "IDC":
            for cle, i in (("Delay on", 3), ("Delay off", 4)):
                self.pr.set_int(ch, i, int(props.get(cle, 0)))
            ch.obj.values[2] = b"\xcd\x00\x00"  # Toggle = No
            self.differe.append(lambda: (self.selecteur(ch, 5, r),
                                         self.fonctions(ch, typ, lignes, self.etats(r["selector"]))))
        elif typ in ("MAC", "IMAC"):
            self.unite(ch, 2, r["unit"])
            self.differe.append(lambda: (self.selecteur(ch, 4 if typ == "MAC" else 3, r),
                                         self.fonctions(ch, typ, lignes, self.etats(r["selector"]))))
        elif typ == "SMC":
            defaut = props.get("Default state name", "Off")
            self.texte(ch, 2, defaut)
            self.etats_smc[nom] = [defaut] + [l["function"] for l in lignes]
            self.differe.append(lambda: self.fonctions(ch, typ, lignes, [l["function"] for l in lignes]))
        elif typ in ("SP", "DP", "IP"):
            self.parametre(ch, typ, r)
        sym = self.pr.chan_sym[ch.oid]
        sym.desc, sym.unit = "", r["unit"] if typ in ("MAC", "IMAC", "IP") else sym.unit
        self.poser(parent, ch)
        self.crees[typ] += 1
        self.noms[nom] = ch.oid
        self._crees[ch.oid] = ch

    def selecteur(self, ch, i, r):
        if r["selector"] and r["selector"] in self.noms:
            ch.obj.values[i] = bytes([0xCF, iqanprojet.REF]) + struct.pack("<I", self.noms[r["selector"]])
        else:
            ch.obj.values[i] = b"\xcd\x36\x00"  # Not used

    def unite(self, ch, i, unite):
        if unite:
            ch.obj.values[i] = b"\xcb\x00" + struct.pack("<H", self.pr.string_index(self.sec, unite))
        else:
            ch.obj.values[i] = b"\xcd\x36\x00"

    def parametre(self, ch, typ, r):
        val = (r["activating"] or "").strip()
        if typ == "SP":
            etats = val.split("|") if val else ["Default"]
            self.texte(ch, 3, etats[0])
            items = [b"\xcb\x00" + struct.pack("<H", self.pr.string_index(self.sec, e)) for e in etats[1:]]
            ch.obj.values[4] = b"\xd2" + struct.pack("<H", len(items)) + b"".join(items)
            # fin du canal : un identifiant (u32) par état de la liste
            t = ch.obj.tail
            k_links = struct.unpack_from("<H", t, 13)[0]
            fin = 15 + 12 * k_links
            ids = b"".join(struct.pack("<I", self.prochain + j) for j in range(len(items)))
            self.prochain += len(items)
            ch.obj.tail = t[:fin] + ids
        elif typ == "DP":
            v = {"True": 3, "False": 2}.get(val, 2)
            ch.obj.values[5] = b"\xd2\x01\x00\xcd" + struct.pack("<H", v)
        elif typ == "IP":
            self.unite(ch, 2, r["unit"])
            ch.obj.values[4] = b"\xd2\x01\x00\xc9" + struct.pack("<i", int(val or 0))

    # --- ensemble ------------------------------------------------------------------------------
    def assembler(self, dossier):
        lignes = []
        for f in sorted(glob.glob(os.path.join(dossier, "[0-9][0-9]_[A-Z][A-Z][A-Z].csv"))):
            for r in csv.DictReader(open(f, encoding="utf-8-sig"), delimiter=";"):
                lignes.append({k: (v or "").strip() for k, v in r.items()})
        arbre = collections.OrderedDict()
        for r in lignes:
            arbre.setdefault(r["group"], collections.OrderedDict()).setdefault(r["channel"], []).append(r)
        racine_app = next(t for t in self.pr.trees(self.sec) if (t.cls, t.sub) == (0x2A, 0x00))
        v2 = self.groupe(racine_app, "v2", len(racine_app.children))
        groupes = {"": v2}

        def fg(chemin):
            if chemin not in groupes:
                parent, _, nom = chemin.rpartition("/")
                p = fg(parent)
                groupes[chemin] = self.groupe(p, nom, len(p.children))
            return groupes[chemin]
        # deux passes : tous les canaux d'abord, puis leurs fonctions (une formule peut citer un
        # canal défini plus loin dans la spec)
        ordre = [(g, c, ls) for g, chs in arbre.items() for c, ls in chs.items()]
        for g, c, ls in ordre:
            p = fg(g)
            self.canal(p, ls, sum(1 for x in p.children if x.cls == 0x04))
        for f in self.differe:
            f()
        return self.rapport


def rapport_md(rapport, crees):
    out = ["# Assemblage v2 : rapport", "",
           "Canaux créés : %d (%s)." % (sum(crees.values()), ", ".join("%s %d" % kv for kv in sorted(crees.items()))),
           ""]
    for titre, items in rapport.items():
        out.append("## %s (%d)" % (titre, len(items)))
        out.append("")
        out += ["- " + i for i in items]
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    base, spec, sortie = sys.argv[1:4]
    a = Assembleur(base)
    r = a.assembler(spec)
    a.pr.save(sortie)
    iqanprojet.Projet(sortie)
    md = rapport_md(r, a.crees)
    if len(sys.argv) > 4:
        open(sys.argv[4], "w", encoding="utf-8").write(md)
    print(md)
