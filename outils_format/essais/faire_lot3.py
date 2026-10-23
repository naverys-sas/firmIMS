"""Lot 3 : ajout d'objets dans une copie du projet MD3 (dépend seulement de iqanprj.py et iqanstr.py).
C1 : ajoute un commentaire dans le groupe 24950 de l'application MC42.
C2 : ajoute un canal Integer parameter (IP) "CLAUDE test IP" = 123 au même endroit,
     avec son entrée dans la table des symboles (numéro 468 du maître MC42) -> plante IQANdesign.
C2a : même canal placé en dernier dans l'arbre (son numéro 468 suit alors l'ordre de l'arbre)
     et nombre de canaux du maître mis à jour dans le préambule.
C2b : comme C2 (au milieu, sans renuméroter) mais avec le nombre de canaux mis à jour.
Usage (depuis Documents\\testia) : python essais_format\\outils\\faire_lot3.py"""
import os, struct, sys, zlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.dirname(HERE)]  # outils_format/ (dépôt) ou même dossier (PC)
import iqanprj, iqanstr

SRC = "avecMD3_V69.03.01.WIP.idax"
OUT = os.path.join("essais_format", "lot3")
NEWID, OLDCTR = 69697, 0x1103F


def records(data):
    hl = struct.unpack_from("<I", data, 1)[0]
    first = data.index(b"\x96", 5 + hl)
    recs, p = [], first
    while data[p] != 0x98:
        n = struct.unpack_from("<I", data, p + 1)[0]
        recs.append([data[p], data[p + 5:p + 5 + n]])
        p += 5 + n
    return data[:first], recs


def pack(head, recs):
    out = bytearray(head)
    for m, pl in recs:
        out += struct.pack("<BI", m, len(pl)) + pl
    out += struct.pack("<BI", 0x98, 4)
    out += struct.pack("<I", zlib.crc32(out))
    return bytes(out)


def tree_insert(pl, parent_id, before_id, node12):
    """Insère un noeud de 12 octets avant le frère before_id, renumérote les rangs."""
    nodes = [list(struct.unpack_from("<BBBBIHH", pl, p)) for p in range(0, len(pl), 12)]
    ip = next(i for i, n in enumerate(nodes) if n[4] == parent_id)
    ib = next(i for i, n in enumerate(nodes) if n[4] == before_id)
    rank = nodes[ib][5]
    nodes[ip][6] += 1
    # renuméroter les frères suivants (enfants directs du parent)
    def subtree_end(i):
        k, todo = i + 1, nodes[i][6]
        while todo:
            k = subtree_end(k)
            todo -= 1
        return k
    k = ip + 1
    for _ in range(nodes[ip][6] - 1):
        if nodes[k][5] >= rank:
            nodes[k][5] += 1
        k = subtree_end(k)
    new = list(struct.unpack("<BBBBIHH", node12))
    new[5] = rank
    nodes.insert(ib, new)
    return b"".join(struct.pack("<BBBBIHH", *n) for n in nodes)


def tree_append(pl, parent_id, node12):
    """Ajoute un noeud comme dernier enfant de parent_id."""
    nodes = [list(struct.unpack_from("<BBBBIHH", pl, p)) for p in range(0, len(pl), 12)]
    ip = next(i for i, n in enumerate(nodes) if n[4] == parent_id)
    def subtree_end(i):
        k, todo = i + 1, nodes[i][6]
        while todo:
            k = subtree_end(k)
            todo -= 1
        return k
    end = subtree_end(ip)
    new = list(struct.unpack("<BBBBIHH", node12))
    new[5] = nodes[ip][6]
    nodes[ip][6] += 1
    nodes.insert(end, new)
    return b"".join(struct.pack("<BBBBIHH", *n) for n in nodes)


def build(name, kind, last=False, count=False):
    p = iqanprj.Project(SRC)
    secs = p.sections
    h, langs = iqanstr.parse(secs[4].data)
    head, recs = records(secs[3].data)
    langs[0].strings.append("CLAUDE : commentaire ajouté directement dans le fichier" if kind == "C1" else "CLAUDE test IP")
    si = len(langs[0].strings) - 1
    if kind == "C1":
        rec = bytes.fromhex("3d000000cb005500cb00") + struct.pack("<H", si) + struct.pack("<IIII", 463, 470, 320, 44)
        node = struct.pack("<BBBBIHH", 0x3D, 0, 0, 0, NEWID, 0, 0)
    else:
        rec = (bytes.fromhex("04300000cb00") + struct.pack("<H", si) +
               bytes.fromhex("cb005500cb006c00cd3600d20100c9") + struct.pack("<I", 123) +
               struct.pack("<III", 0, 400, 700) + b"\0\0\0")
        node = struct.pack("<BBBBIHH", 4, 0x30, 1, 0, NEWID, 0, 0)
    anchor = bytes.fromhex("3d000000cb005500cb009700")  # commentaire 67563
    done = 0
    for k in range(len(recs)):
        if recs[k][0] == 0x96 and struct.unpack_from("<I", recs[k][1], 4)[0] == 24942:
            if last:  # dernier enfant de l'application = dernier canal dans l'ordre de l'arbre
                recs[k][1] = tree_append(recs[k][1], 24942, node)
                trees = [j for j, r in enumerate(recs) if r[0] == 0x96]
                kp = [j for j, r in enumerate(recs) if r[0] == 0x97][trees.index(k)]  # même rang
                pr = recs[kp][1]
                assert pr.endswith(bytes.fromhex("1e0000001e000000"))
                recs[kp][1] = pr[:-8] + rec + pr[-8:]  # avant les champs de fin de l'application
                done += 2
                break
            recs[k][1] = tree_insert(recs[k][1], 24950, 67563, node)
            done += 1
        if recs[k][0] == 0x97 and anchor in recs[k][1]:
            assert recs[k][1].count(anchor) == 1
            recs[k][1] = recs[k][1].replace(anchor, rec + anchor)
            done += 1
    assert done == 2, done
    if count:  # nombre de canaux du maître MC42 dans le préambule : 468 -> 469
        assert head[137:142] == bytes.fromhex("01d4010500")
        head = head[:138] + struct.pack("<H", 469) + head[140:]
    secs[3].data = pack(head, recs)
    secs[4].data = iqanstr.encode(h, langs)
    for s in secs:
        if s.tag in (0xB5, 0xCA, 0xC8):
            d = bytearray(s.data)
            assert struct.unpack_from("<I", d, 79)[0] == OLDCTR
            struct.pack_into("<I", d, 79, NEWID + 1)
            d[-4:] = struct.pack("<I", zlib.crc32(bytes(d[:-4])))
            s.data = bytes(d)
    if kind == "C2":
        b = secs[6].data
        n = struct.unpack_from("<I", b, 1)[0]
        prev = b.index(b"debug temps screen\0") - 11  # dernier canal du maître MC42 (numéro 467)
        assert struct.unpack_from("<IHBBB", b, prev)[1:4] == (467, 0, 1)
        end = b.index(b"\0", b.index(b"\0", b.index(b"\0", prev + 11) + 1) + 1) + 1
        ent = struct.pack("<IHBBBH", NEWID, 468, 0, 1, 4, 0x30) + b"CLAUDE test IP\0\0%\0"
        b = bytearray(b[:end] + ent + b[end:])
        struct.pack_into("<I", b, 1, n + 1)
        secs[6].data = bytes(b)
    os.makedirs(OUT, exist_ok=True)
    p.save(os.path.join(OUT, name))
    print("écrit", name)


if __name__ == "__main__":
    build("C1_md3_commentaire_ajoute.idax", "C1")
    build("C2_md3_canal_ajoute.idax", "C2")
    build("C2a_md3_canal_en_dernier.idax", "C2", last=True, count=True)
    build("C2b_md3_canal_milieu_compte.idax", "C2", count=True)
