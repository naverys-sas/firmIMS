"""Éditeur de projet IQANdesign : lire un .idax / .idsx, modifier ses objets, l'enregistrer.

    pr = Projet("v2_mc42.idax")
    sec, n = pr.find("E.Battery CMD")[0]
    pr.set_text(sec, n, 0, "E.Battery command")      # renommer
    copie = pr.clone(pr, sec, n)                      # copier (nouveaux identifiants)
    pr.insert(sec, n.parent, copie)                   # coller dans le même groupe
    pr.remove(sec, autre)                             # supprimer
    pr.save("v2_mc42_modifie.idax")

Principes :
- Les références entre canaux (jeton cf 04 [numéro][00][maître], listes de sorties des groupes de
  fonctions, liste des réglages) sont converties en identifiants d'objets au chargement, et
  reconverties en numéros à l'enregistrement. Les numéros suivent l'ordre de l'arbre de chaque
  maître : ajouter, supprimer ou déplacer un canal renumérote donc tout seul les suivants.
- La table des symboles est reconstruite à l'enregistrement, ainsi que le nombre de canaux de
  chaque maître et le compteur d'identifiants.
- Un objet copié d'un autre projet garde ses références vers les canaux de même nom du projet
  cible ; une référence sans équivalent est une erreur (rien n'est deviné).
"""
import copy
import struct

import iqanobj
import iqanprj
import iqanprops
import iqanstr
import iqansym
import iqanvaleurs

REF = 0xFF  # genre interne d'une référence à un canal, désigné par son identifiant d'objet
TAG_OBJ, TAG_SYM = (0xB5, 0xCA, 0xC8), 0xBD


class EditError(Exception):
    pass


def _map_refs(v, f):
    """Applique f aux références de canal d'une valeur (y compris dans les listes)."""
    t = v[0]
    if t == 0xCF and v[1] in (4, REF):
        return f(v)
    if t == 0xD2:
        return v[:3] + b"".join(_map_refs(x, f) for x in iqanvaleurs.items(v))
    return v


def _tail_list(n):
    """Position et longueur d'une liste de canaux dans la fin de l'objet ([u16 n][n x 4 octets])."""
    t = n.obj.tail
    if (n.cls, n.sub) in ((0x01, 0x00), (0x01, 0x06)):  # groupe de fonctions : sorties
        q = t.index(b"\0", 10) + 1
        return q + 2, struct.unpack_from("<H", t, q)[0]
    if (n.cls, n.sub) == (0x2B, 0x00):  # conteneur des réglages
        return 2, struct.unpack_from("<H", t, 0)[0]
    return None


def _links(n):
    """Nombre de liens graphiques d'un canal vers des groupes de fonctions ([u32 id][X][Y] chacun),
    rangés dans la fin du canal ; None si l'objet n'a pas cette structure."""
    if n.cls != 0x04 or isinstance(iqanprops.tail_rule(n.cls, n.sub), int):
        return None
    return struct.unpack_from("<H", n.obj.tail, 13)[0]


class Projet:
    def __init__(self, path):
        self.path = path
        self.p = iqanprj.Project(path)
        self.secs = self.p.sections
        self.blocks, self.strtab = {}, {}
        self.masters = [i for i, s in enumerate(self.secs) if s.tag == 0xB5]
        for i, s in enumerate(self.secs):
            if s.tag in TAG_OBJ:
                bl = iqanobj.Block(s.data)
                trees = [o for m, o in bl.records if m == 0x96]
                props = [o for m, o in bl.records if m == 0x97]
                for t, pl in zip(trees, props):
                    iqanprops.parse_stream(t, pl)
                self.blocks[i] = bl
                if i + 1 < len(self.secs) and self.secs[i + 1].tag in (0xC6, 0xCB):
                    self.strtab[i] = iqanstr.parse(self.secs[i + 1].data)
        self.isym = next(i for i, s in enumerate(self.secs) if s.tag == TAG_SYM)
        self.sym_head, syms = iqansym.parse(self.secs[self.isym].data)
        self.modules = [s for s in syms if s.kind != 4]
        self.chan_sym = {s.oid: s for s in syms if s.kind == 4}
        num2oid = {(s.master, s.num): s.oid for s in syms if s.kind == 4}
        self.unresolved = 0
        self._counter_off = self._find_counter()
        self._count_off = {}
        for k, i in enumerate(self.masters):
            self._count_off[i] = self._find_count(i, sum(1 for s in syms if s.kind == 4 and s.master == k))
        self._positional = set()
        for _, n in self.walk():
            if n.children and [c.idx for c in n.children] == list(range(len(n.children))):
                self._positional.add(id(n))  # un même identifiant peut servir dans plusieurs arbres

        def to_oid(v):
            num, z, m = struct.unpack_from("<HBB", v, 2)
            oid = num2oid.get((m, num))
            if oid is None:
                self.unresolved += 1
                return v
            return bytes([0xCF, REF]) + struct.pack("<I", oid)
        for _, n in self.walk():
            n.obj.values = [_map_refs(v, to_oid) for v in n.obj.values]
            tl = _tail_list(n)
            if tl:
                q, k = tl
                t = bytearray(n.obj.tail)
                for j in range(k):
                    num, z, m = struct.unpack_from("<HBB", t, q + 4 * j)
                    oid = num2oid.get((m, num))
                    if oid is None:
                        raise EditError("objet %d : liste de canaux illisible" % n.oid)
                    struct.pack_into("<I", t, q + 4 * j, oid)
                n.obj.tail = bytes(t)

    # --- lecture -------------------------------------------------------------------------
    def trees(self, sec):
        return [o for m, o in self.blocks[sec].records if m == 0x96]

    def walk(self, secs=None):
        for i in (secs or self.blocks):
            for t in self.trees(i):
                for n in t.walk():
                    yield i, n

    def strings(self, sec):
        return self.strtab[sec][1][0].strings

    def master(self, sec):
        """N° du maître d'une section d'objets (les pages MD4, tag ca, suivent leur maître)."""
        k = None
        for i in sorted(self.blocks):
            if self.secs[i].tag == 0xB5:
                k = self.masters.index(i)
            if i == sec:
                return k if self.secs[i].tag != 0xC8 else None

    def context(self, sec):
        syms = list(self.chan_sym.values())
        return iqanvaleurs.Context(self.strings(sec) if sec in self.strtab else [], syms)

    def text(self, sec, n, i):
        v = n.obj.values[i]
        if v[0] == 0xCF and v[1] == REF:
            o = struct.unpack_from("<I", v, 2)[0]
            s = self.chan_sym.get(o)
            return s.name if s else "<objet %d>" % o
        return iqanvaleurs.render(v, self.context(sec))

    def name(self, sec, n):
        return self.text(sec, n, 0) if n.obj.values and n.obj.values[0][0] == 0xCB else ""

    def find(self, name, secs=None):
        return [(i, n) for i, n in self.walk(secs) if self.name(i, n) == name]

    def by_oid(self, oid):
        return [(i, n) for i, n in self.walk() if n.oid == oid]

    # --- valeurs -------------------------------------------------------------------------
    def string_index(self, sec, text):
        """N° d'un texte dans la table du maître ; ajouté à la fin s'il n'existe pas."""
        langs = self.strtab[sec][1]
        st = langs[0].strings
        if text in st:
            return st.index(text)
        st.append(text)
        return len(st) - 1

    def set_text(self, sec, n, i, text):
        v = n.obj.values[i]
        if v[0] != 0xCB:
            raise EditError("objet %d, valeur %d : ce n'est pas un texte" % (n.oid, i))
        n.obj.values[i] = bytes([0xCB, v[1]]) + struct.pack("<H", self.string_index(sec, text))

    def set_int(self, n, i, x):
        if n.obj.values[i][0] != 0xC9:
            raise EditError("objet %d, valeur %d : ce n'est pas un entier" % (n.oid, i))
        n.obj.values[i] = b"\xc9" + struct.pack("<i", x)

    def set_ref(self, n, i, target_oid):
        if target_oid not in self.chan_sym and not any(o.oid == target_oid for _, o in self.walk(self.masters)):
            raise EditError("canal %d inconnu" % target_oid)
        n.obj.values[i] = bytes([0xCF, REF]) + struct.pack("<I", target_oid)

    # --- structure -----------------------------------------------------------------------
    def max_oid(self):
        return max(n.oid for _, n in self.walk())

    def remove(self, sec, n):
        """Supprime un objet et ses enfants. Refuse si un canal supprimé est encore référencé."""
        gone = {x.oid for x in n.walk()}
        users = []
        for i, o in self.walk():
            if o.oid in gone:
                continue
            for v in o.obj.values:
                def chk(r):
                    if r[1] == REF and struct.unpack_from("<I", r, 2)[0] in gone:
                        users.append(o.oid)
                    return r
                _map_refs(v, chk)
        if users:
            raise EditError("objet %d encore utilisé par %s" % (n.oid, sorted(set(users))[:20]))
        n.parent.children.remove(n)
        for x in gone:
            self.chan_sym.pop(x, None)
        self._drop_links(gone)
        self._drop_from_lists(gone)

    def _drop_from_lists(self, gone):
        """Retire des canaux supprimés des listes de sorties des groupes et de la liste des réglages."""
        for _, o in self.walk():
            tl = _tail_list(o)
            if not tl:
                continue
            q, k = tl
            t = o.obj.tail
            keep = [t[q + 4 * j:q + 4 * j + 4] for j in range(k)
                    if struct.unpack_from("<I", t, q + 4 * j)[0] not in gone]
            if len(keep) != k:
                o.obj.tail = t[:q - 2] + struct.pack("<H", len(keep)) + b"".join(keep) + t[q + 4 * k:]

    def _drop_links(self, gone):
        for _, o in self.walk():
            k = _links(o)
            if not k:
                continue
            t = o.obj.tail
            keep = [t[15 + 12 * j:27 + 12 * j] for j in range(k)
                    if struct.unpack_from("<I", t, 15 + 12 * j)[0] not in gone]
            if len(keep) != k:
                o.obj.tail = (t[:12] + bytes([2 if keep else 0]) + struct.pack("<H", len(keep)) +
                              b"".join(keep) + t[15 + 12 * k:])

    def insert(self, sec, parent, n, before=None):
        """Insère n (et ses enfants) sous parent, avant l'enfant before (à la fin sinon)."""
        used = {o.oid for _, o in self.walk()}
        clash = [x.oid for x in n.walk() if x.oid in used]
        if clash:
            raise EditError("identifiants déjà utilisés : %s" % clash[:10])
        pos = len(parent.children) if before is None else parent.children.index(before)
        parent.children.insert(pos, n)
        n.parent = parent
        if id(parent) not in self._positional:
            n.idx = max([c.idx for c in parent.children if c is not n] + [-1]) + 1

    def move(self, sec, n, parent, before=None, to_sec=None):
        """Déplace un objet (il garde son identifiant, donc les réglages des machines)."""
        n.parent.children.remove(n)
        self.insert(sec if to_sec is None else to_sec, parent, n, before)

    def clone(self, src, src_sec, n, dst_sec, keep_links=False):
        """Copie l'objet n du projet src (qui peut être self) pour l'insérer dans dst_sec.

        Nouveaux identifiants ; textes recopiés dans la table du maître cible ; références vers
        des canaux copiés avec l'objet -> leurs copies ; autres références -> canal de même nom
        dans le projet cible."""
        new = copy.deepcopy(n)
        new.parent = None
        nxt = self.max_oid() + 1
        oidmap = {}
        for x in new.walk():
            oidmap[x.oid] = nxt
            x.oid = nxt
            nxt += 1
        by_name = {}
        for o, s in self.chan_sym.items():
            by_name.setdefault(s.name, []).append(o)
        missing = []

        def ref(v):
            o = struct.unpack_from("<I", v, 2)[0] if v[1] == REF else None
            if o is None:
                missing.append("référence non résolue dans la source")
                return v
            if o in oidmap:
                return v[:2] + struct.pack("<I", oidmap[o])
            if src is self:
                return v
            name = src.chan_sym[o].name if o in src.chan_sym else None
            cand = by_name.get(name, [])
            if len(cand) != 1:
                missing.append(name)
                return v
            return v[:2] + struct.pack("<I", cand[0])
        src_st = src.strings(src_sec) if src_sec in src.strtab else []
        same_table = src is self and src_sec == dst_sec

        def text(v):
            if v[0] == 0xCB:
                idx = struct.unpack_from("<H", v, 2)[0]
                if idx < 0xFFFE and not same_table:
                    return v[:2] + struct.pack("<H", self.string_index(dst_sec, src_st[idx]))
            elif v[0] == 0xD2:
                return v[:3] + b"".join(text(i) for i in iqanvaleurs.items(v))
            elif v[0] == 0xD7 and src is not self:
                raise EditError("objet %d : texte chiffré (code, mot de passe) non copiable entre "
                                "projets" % x.oid)
            return v
        for x in new.walk():
            vals = []
            for v in x.obj.values:
                vals.append(_map_refs(text(v), ref))
            x.obj.values = vals
            tl = _tail_list(x)
            if tl:
                q, k = tl
                t = bytearray(x.obj.tail)
                for j in range(k):
                    struct.pack_into("<I", t, q + 4 * j,
                                     struct.unpack_from("<I", ref(b"\xcf\xff" + t[q + 4 * j:q + 4 * j + 4]), 2)[0])
                x.obj.tail = bytes(t)
            if x.cls == 0x04 and not keep_links:  # liens graphiques vers les groupes de l'original
                k = _links(x)
                if k:
                    t = x.obj.tail
                    x.obj.tail = t[:12] + b"\0\0\0" + t[15 + 12 * k:]
            if x.cls == 0x04:
                old = [o for o, nn in oidmap.items() if nn == x.oid][0]
                s = src.chan_sym.get(old)
                if s is not None:
                    self.chan_sym[x.oid] = iqansym.Symbol(x.oid, 0, 0, 0, 4, s.cls, s.name, s.desc, s.unit)
        if missing:
            raise EditError("références sans équivalent dans le projet cible : %s" % sorted(set(map(str, missing))))
        return new

    def replace(self, sec, old, src, src_sec, src_node, keep_ids=True):
        """Remplace l'objet old (et ses enfants) par une copie de src_node pris dans src.

        keep_ids : les objets de la copie qui ont un équivalent de même nom et de même classe dans
        old reprennent son identifiant ; les réglages enregistrés dans les machines (paramètres)
        restent donc attachés, et les références du reste du projet restent valables.
        Sans équivalent, une référence du reste du projet vers old est une erreur : rien n'est
        modifié."""
        old_ids = {x.oid for x in old.walk()}
        old_named = {}
        for x in old.walk():
            if x.cls == 0x04:  # seuls les canaux portent des réglages ; les sous-objets sont recréés
                old_named.setdefault((x.cls, x.sub, self.name(sec, x)), []).append(x.oid)
        saved = {o: self.chan_sym.pop(o) for o in old_ids if o in self.chan_sym}
        try:  # la copie ne doit pas résoudre ses références vers l'ancien groupe
            new = self.clone(src, src_sec, src_node, sec)
        finally:
            self.chan_sym.update(saved)
        pairs = {}
        if keep_ids:
            for x in new.walk():
                if x.cls != 0x04:
                    continue
                c = old_named.get((x.cls, x.sub, self.name(sec, x)), [])
                if len(c) == 1 and c[0] not in pairs.values():
                    pairs[x.oid] = c[0]
            if old.cls == new.cls and old.sub == new.sub:
                pairs[new.oid] = old.oid
        kept = set(pairs.values())
        missing = []
        for _, o in self.walk():
            if o.oid in old_ids:
                continue
            for v in o.obj.values:
                def look(r):
                    t = struct.unpack_from("<I", r, 2)[0]
                    if r[1] == REF and t in old_ids and t not in kept:
                        missing.append(saved[t].name if t in saved else t)
                    return r
                _map_refs(v, look)
        if missing:
            for x in new.walk():
                self.chan_sym.pop(x.oid, None)
            raise EditError("canaux utilisés ailleurs et absents de la copie : %s" % sorted(set(map(str, missing))))
        # retirer l'ancien objet, puis donner aux objets appariés leur ancien identifiant
        parent = old.parent
        pos = parent.children.index(old)
        parent.children.remove(old)
        for o in old_ids:
            self.chan_sym.pop(o, None)
        self._drop_links(old_ids - kept)
        self._drop_from_lists(old_ids - kept)

        def ren(r):
            t = struct.unpack_from("<I", r, 2)[0]
            return r[:2] + struct.pack("<I", pairs[t]) if r[1] == REF and t in pairs else r
        for x in new.walk():
            x.obj.values = [_map_refs(v, ren) for v in x.obj.values]
            tl = _tail_list(x)
            if tl:
                q, k = tl
                t = bytearray(x.obj.tail)
                for j in range(k):
                    o = struct.unpack_from("<I", t, q + 4 * j)[0]
                    struct.pack_into("<I", t, q + 4 * j, pairs.get(o, o))
                x.obj.tail = bytes(t)
            if x.oid in pairs:
                if x.oid in self.chan_sym:
                    sym = self.chan_sym.pop(x.oid)
                    sym.oid = pairs[x.oid]
                    self.chan_sym[sym.oid] = sym
                x.oid = pairs[x.oid]
        parent.children.insert(pos, new)
        new.parent = parent
        new.idx = old.idx
        return new

    # --- enregistrement ------------------------------------------------------------------
    def _find_counter(self):
        """Compteur des identifiants attribués : dans la copie de l'en-tête du projet en tête de
        chaque bloc, après les deux empreintes (texte\0) et l'identifiant du projet (16 octets)."""
        offs = set()
        for bl in self.blocks.values():
            h = bl.head
            q = h.index(b"\0", h.index(b"\0", 25) + 1) + 1 + 16
            offs.add(q)
            if struct.unpack_from("<I", h, q)[0] < self.max_oid():
                raise EditError("compteur d'identifiants inattendu")
        if len(offs) != 1:
            raise EditError("compteur d'identifiants à des positions différentes")
        return offs.pop()

    def _find_count(self, sec, count):
        h = self.blocks[sec].head
        hl = struct.unpack_from("<I", h, 1)[0]
        pat = struct.pack("<H", count)
        offs = [o for o in range(5 + hl, len(h) - 1) if h[o:o + 2] == pat]
        if len(offs) != 1:
            raise EditError("nombre de canaux du maître introuvable (section %d : %s)" % (sec, offs))
        return offs[0]

    def numbering(self):
        """Numéros des canaux : ordre de l'arbre de chaque maître."""
        num = {}
        for k, i in enumerate(self.masters):
            j = 0
            for t in self.trees(i):
                for n in t.walk():
                    if n.cls == 0x04:
                        num[n.oid] = (k, j)
                        j += 1
        return num

    def save(self, path):
        num = self.numbering()
        names = {}
        for i, n in self.walk(self.masters):
            if n.cls == 0x04:
                names[n.oid] = (i, n)

        def to_num(v):
            if v[1] != REF:
                return v
            o = struct.unpack_from("<I", v, 2)[0]
            if o not in num:
                raise EditError("référence vers l'objet %d qui n'est plus un canal du projet" % o)
            m, j = num[o]
            return b"\xcf\x04" + struct.pack("<HBB", j, 0, m)
        # symboles : modules inchangés, puis canaux par maître et par numéro
        chans = []
        for o, (m, j) in sorted(num.items(), key=lambda kv: kv[1]):
            i, n = names[o]
            s = self.chan_sym.get(o)
            if s is None:
                raise EditError("canal %d sans entrée de symbole (créé sans clone ?)" % o)
            s.num, s.master, s.cls = j, m, n.sub
            s.name = iqanvaleurs.render(n.obj.values[0], self.context(i))
            chans.append(s)
        self.secs[self.isym].data = iqansym.encode(self.sym_head, self.modules + chans)
        ctr = max(struct.unpack_from("<I", next(iter(self.blocks.values())).head, self._counter_off)[0],
                  self.max_oid())
        for i, bl in self.blocks.items():
            for m, t in bl.records:
                if m != 0x96:
                    continue
                for n in t.walk():
                    if id(n) in self._positional:
                        for j, c in enumerate(n.children):
                            c.idx = j
            recs, trees = [], []
            for m, o in bl.records:
                if m == 0x96:
                    trees.append(o)
            k = 0
            for r in bl.records:
                if r[0] == 0x97:
                    t = trees[k]
                    k += 1
                    saved = {}
                    for n in t.walk():
                        saved[id(n)] = (n.obj.values, n.obj.tail)
                        n.obj.values = [_map_refs(v, to_num) for v in n.obj.values]
                        tl = _tail_list(n)
                        if tl:
                            q, cnt = tl
                            tt = bytearray(n.obj.tail)
                            for j in range(cnt):
                                o = struct.unpack_from("<I", tt, q + 4 * j)[0]
                                m2, j2 = num[o]
                                struct.pack_into("<HBB", tt, q + 4 * j, j2, 0, m2)
                            n.obj.tail = bytes(tt)
                    r[1] = iqanprops.encode_stream(t)
                    for n in t.walk():
                        n.obj.values, n.obj.tail = saved[id(n)]
            h = bytearray(bl.head)
            struct.pack_into("<I", h, self._counter_off, ctr)
            if i in self._count_off:
                struct.pack_into("<H", h, self._count_off[i], sum(1 for m, _ in num.values()
                                                                    if m == self.masters.index(i)))
            bl.head = bytes(h)
            self.secs[i].data = bl.encode()
            if i in self.strtab:
                self.secs[i + 1].data = iqanstr.encode(*self.strtab[i])
        self.p.save(path)
