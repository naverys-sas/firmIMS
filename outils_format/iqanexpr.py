"""Lecture des expressions des feuilles de la v2 (« (BAT SOC >= eb Charge Max) OR X »).

Les noms de canaux contiennent des espaces, des tirets, des points : on les reconnaît en prenant,
à chaque position, le plus long nom connu qui commence là (la liste des noms est fournie). Rend un
arbre de tuples :
    ("chan", nom)  ("num", valeur)  ("bool", True/False)
    ("not", x)  ("and", [x, ...])  ("or", [x, ...])
    ("cmp", op, a, b)   op parmi = <> < > <= >=
    ("arith", op, a, b) op parmi + - * /
    ("call", fonction, [arguments])

    arbre = parse("A = 1", noms)       # ExprError si un mot n'est pas un canal connu
"""
import re

RELOPS = ("<>", "<=", ">=", "=", "<", ">")
FUNCS = ("not", "PositiveFlank", "NegativeFlank", "Abs", "MaxOf", "MinOf")
_num = re.compile(r"-?\d+(?:[.,]\d+)?")


class ExprError(Exception):
    pass


class _Parser:
    def __init__(self, s, names):
        self.s, self.p = s, 0
        self.names = sorted(names, key=len, reverse=True)
        self.lower = {n.lower(): n for n in names}

    # --- jetons -----------------------------------------------------------------------------
    def ws(self):
        while self.p < len(self.s) and self.s[self.p].isspace():
            self.p += 1

    def peek_word(self, *words):
        self.ws()
        for w in words:
            e = self.p + len(w)
            if self.s[self.p:e].lower() == w.lower() and (e >= len(self.s) or not self.s[e].isalnum()):
                return w
        return None

    def take(self, tok):
        self.ws()
        if self.s.startswith(tok, self.p):
            self.p += len(tok)
            return True
        return False

    def fail(self, what):
        raise ExprError("%s à la position %d : « %s »" % (what, self.p, self.s[self.p:self.p + 30]))

    # --- grammaire --------------------------------------------------------------------------
    def expr(self):
        items = [self.and_()]
        while self.peek_word("or"):
            self.p += 2
            items.append(self.and_())
        return items[0] if len(items) == 1 else ("or", items)

    def and_(self):
        items = [self.not_()]
        while self.peek_word("and"):
            self.p += 3
            items.append(self.not_())
        return items[0] if len(items) == 1 else ("and", items)

    def not_(self):
        if self.peek_word("not") and not self.channel_here():
            self.p += 3
            return ("not", self.not_())
        return self.cmp()

    def cmp(self):
        a = self.sum()
        self.ws()
        for op in RELOPS:
            if self.take(op):
                return ("cmp", op, a, self.sum())
        return a

    def sum(self):
        a = self.term()
        while True:
            self.ws()
            if self.channel_here():
                return a
            for op in "+-":
                if self.take(op):
                    a = ("arith", op, a, self.term())
                    break
            else:
                return a

    def term(self):
        a = self.unary()
        while True:
            for op in "*/":
                if self.take(op):
                    a = ("arith", op, a, self.unary())
                    break
            else:
                return a

    def channel_here(self):
        """Plus long nom de canal connu qui commence à la position courante (sans avancer)."""
        self.ws()
        rest = self.s[self.p:].lower()
        for n in self.names:
            if rest.startswith(n.lower()):
                e = self.p + len(n)
                if e >= len(self.s) or not (self.s[e].isalnum() or self.s[e] == "_"):
                    return n
        return None

    def unary(self):
        self.ws()
        name = self.channel_here()
        if name:
            self.p += len(name)
            return ("chan", name)
        if self.take("("):
            x = self.expr()
            if not self.take(")"):
                self.fail("parenthèse fermante attendue")
            return x
        w = self.peek_word("True", "False")
        if w:
            self.p += len(w)
            return ("bool", w == "True")
        for f in FUNCS:
            if self.peek_word(f):
                q = self.p
                self.p += len(f)
                if self.take("("):
                    args = [self.expr()]
                    while self.take(","):
                        args.append(self.expr())
                    if not self.take(")"):
                        self.fail("parenthèse fermante attendue")
                    return ("not", args[0]) if f == "not" else ("call", f, args)
                self.p = q
        m = _num.match(self.s, self.p)
        if m:
            self.p = m.end()
            return ("num", float(m.group().replace(",", ".")))
        self.fail("canal inconnu")


def parse(s, names):
    p = _Parser(s, names)
    x = p.expr()
    p.ws()
    if p.p != len(s):
        p.fail("fin d'expression attendue")
    return x


_PREC = {"or": 1, "and": 2, "not": 3, "cmp": 4, "+": 5, "-": 5, "*": 6, "/": 6}


def to_iqan(x, oid_of, prec=0):
    """Texte de script IQAN (groupe Expression) : « Result := » + to_iqan(arbre, oid_of).
    oid_of(nom) rend l'identifiant d'objet du canal, écrit {#identifiant#}."""
    k = x[0]
    if k == "chan":
        return "{#%d#}" % oid_of(x[1])
    if k == "num":
        v = x[1]
        return str(int(v)) if v == int(v) else repr(v)
    if k == "bool":
        return "True" if x[1] else "False"
    if k == "not":
        s, p = "not " + to_iqan(x[1], oid_of, _PREC["not"]), _PREC["not"]
    elif k in ("and", "or"):
        p = _PREC[k]
        s = (" %s " % k).join(to_iqan(i, oid_of, p + 1) for i in x[1])
    elif k == "cmp":
        p = _PREC["cmp"]
        s = "%s %s %s" % (to_iqan(x[2], oid_of, p + 1), x[1], to_iqan(x[3], oid_of, p + 1))
    elif k == "arith":
        p = _PREC[x[1]]
        s = "%s %s %s" % (to_iqan(x[2], oid_of, p), x[1], to_iqan(x[3], oid_of, p + 1))
    elif k == "call":
        return "%s(%s)" % (x[1], ", ".join(to_iqan(a, oid_of) for a in x[2]))
    else:
        raise ExprError("nœud inconnu %r" % (k,))
    if k == "cmp" and prec > 0:  # priorité des comparaisons dans IQAN non vérifiée : parenthèses
        return "(%s)" % s
    return "(%s)" % s if p < prec else s
