"""Index the supplier/engineering documents of docs/ by equipment (CSV).

Usage: python -I docs_index.py docs_dir text_dir out.csv
text_dir holds pdftotext output named <relative path with / replaced by __>.txt
"""
import collections, csv, os, re, sys

CATS = [('Architecture', 'Architecture générale'), ('MC2', 'Contrôleur MC2'), ('mc43', 'Contrôleur MC42'),
        ('MC42', 'Contrôleur MC42'), ('MD4', 'Écran MD4'), ('MD3', 'Écran MD3'), ('DVTC', 'Variateur Sevcon HVLP'),
        ('HVLP', 'Variateur Sevcon HVLP'), ('Gen4', 'Variateur Sevcon Gen4'), ('Sevcon', 'Variateur Sevcon'),
        ('Zapi', 'Variateur Zapi'), ('zapi', 'Variateur Zapi'), ('Kreisel', 'Batterie Kreisel'),
        ('kreisel', 'Batterie Kreisel'), ('Torqeedo', 'Batterie Torqeedo (code : BMW)'),
        ('torqeedo', 'Batterie Torqeedo (code : BMW)'), ('BMW', 'Batterie Torqeedo (code : BMW)'),
        ('Novum', 'Batterie NovumTech'), ('TYVA', 'Batterie Tyva'), ('Tyva', 'Batterie Tyva'),
        ('TYREB', 'Batterie Tyva'), ('BMS', 'Batterie Tyva'), ('WG1605', 'Moteur Kubota WG1605'),
        ('wg1605', 'Moteur Kubota WG1605'), ('Kubota', 'Moteur Kubota WG1605'), ('KORD', 'Moteur Kubota WG1605'),
        ('EB2', 'Moteur EB2'), ('EB0', 'Moteur EB2'), ('VW', 'Moteur VW 2.0'), ('BEF', 'Moteur VW 2.0'),
        ('CBS', 'Moteur VW 2.0'), ('600xxx', 'Moteur VW 2.0'), ('SSG-415', 'Moteur gaz SSG-415'),
        ('a10vg', 'Pompe hydraulique Rexroth A10VG'), ('parker 3349', 'Pompe hydraulique Parker'),
        ('ydrau', 'Hydraulique'), ('Hydraulic', 'Hydraulique'), ('FuseBox', 'Boîte à fusibles'),
        ('Fusebox', 'Boîte à fusibles'), ('Fuse box', 'Boîte à fusibles'), ('Engine_', 'Faisceau moteur / variateur'),
        ('Novec', 'Variateur Sevcon HVLP'), ('Fault_codes', 'Variateur Sevcon HVLP'), ('EVo5', 'Moteur EVO5'),
        ('IGUANA9', 'Variateur Sevcon (réglages)'), ('J1939_Traction', 'Variateur Sevcon HVLP')]


def main():
    docs, text_dir, out = sys.argv[1:4]
    rows = []
    for root, _, files in os.walk(docs):
        for f in files:
            p = os.path.join(root, f)
            rel = os.path.relpath(p, docs).replace(os.sep, '/')
            if rel.startswith(('variantes/', 'Registre')):
                continue
            cat = next((c for k, c in CATS if k in f), 'Autre')
            kind = 'schéma' if rel.startswith('schemas/') else ('vue d\'ensemble' if '/' not in rel else 'fiche / notice')
            t = os.path.join(text_dir, rel.replace('/', '__').rsplit('.', 1)[0] + '.txt')
            size = os.path.getsize(t) if os.path.exists(t) else -1
            content = 'dessin (peu de texte)' if 0 <= size < 300 else ('texte' if size >= 300 else 'non PDF')
            m = re.search(r'IND(?:ICE)?[ _-]*([A-Z])\b', f)
            rows.append([cat, kind, rel, m.group(1) if m else '', content, os.path.getsize(p) // 1024])
    rows.sort()
    with open(out, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh, delimiter=';')
        w.writerow(['équipement', 'type', 'fichier', 'indice', 'contenu', 'Ko'])
        w.writerows(rows)
    print(collections.Counter(r[0] for r in rows).most_common())
    print('Autre:', [r[2] for r in rows if r[0] == 'Autre'])


if __name__ == '__main__':
    main()
