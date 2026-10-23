# outils_format — lire et écrire directement les projets IQANdesign

Le but : que Claude modifie le fichier projet `.idax` / `.idsx` lui-même, sans passer par l'interface d'IQANdesign. IQANdesign ne sert plus qu'à vérifier le résultat (export texte) et à envoyer le programme au contrôleur.

Python 3, bibliothèque standard uniquement. Format décodé le 2026-10-23 sur IQANdesign 6.08 (7 projets Iguana).

| Module | Rôle | Relecture puis réécriture identique à l'octet près |
|---|---|---|
| `iqanprj.py` | Conteneur : sections, compression, CRC32 du fichier | oui, 7 projets |
| `iqanstr.py` | Tables de textes (noms, descriptions, messages, traductions) | oui, 24 tables |
| `iqanobj.py` | Blocs d'objets : arbre des objets, propriétés, CRC32 du bloc | oui, 31 blocs |
| `iqansym.py` | Table des symboles (canaux et modules, numérotation) | oui, 7 projets |
| `iqantxt.py` | Lecture d'un export texte IQANdesign (`-saveas x.txt`) | — |
| `correspondance.py` | Relie chaque objet binaire à son objet de l'export texte | 99,2 % des objets de la 108.3.1 |
| `essais/` | Scripts des fichiers de test envoyés à IQANdesign (lots 1 à 3) | — |

```bash
python iqanprj.py ../TESTIA.idax /tmp/copie.idax      # liste les sections, réécrit, compare
python correspondance.py ../TESTIA.idax ../exports/TESTIA_108.3.1.txt
```

## Le format en bref

**Fichier.** `IQANprj\0` + 2 octets, puis des sections `[u8 tag][u32 longueur][contenu]`. Le contenu d'une section de données est `[u8 mode][u32 taille][u32 taille stockée][données]` (mode 2 = zlib niveau 6, mode 0 = brut). La dernière section (tag `b8`) est le CRC32 de tout le fichier, écrit deux fois. IQANdesign refuse un fichier dont un CRC est faux (« This file is corrupt. Invalid checksum. »), au niveau du fichier comme au niveau d'un bloc.

| Tag | Contenu |
|---|---|
| `b4` | En-tête : nom, description, version, auteur, identifiant de projet (GUID), empreintes des mots de passe |
| `b5` + `c6` | Pour chaque maître : objets + textes |
| `ca` + `cb` | Écrans MD4 : objets + textes supplémentaires (pages) |
| `c8` | Objets au niveau du projet (groupe Applications, conteneurs) |
| `bd` | Table des symboles : chaque canal et module, avec son numéro |
| `b6` | Code compilé. Absent des `.idsx`. IQANdesign ne le met pas à jour à l'enregistrement : il le recompile pour l'envoi. On n'a donc jamais à le produire. |
| `cc` | Image système des MD4 (27 Mo), recopiée telle quelle |

**Textes.** Chaque objet désigne ses textes par un numéro dans la table de son maître. Les textes identiques sont partagés : modifier une chaîne la change partout où elle sert.

**Objets.** Un bloc d'objets contient plusieurs arbres (application, conteneurs de modules, de réglages, de journaux…). Chaque arbre est stocké deux fois : la structure (noeuds de 12 octets : classe, sous-classe, identifiant, rang parmi les frères, nombre d'enfants), puis les propriétés de tous ses objets dans le même ordre. Les propriétés sont imbriquées : un objet écrit ses champs, puis ses enfants, puis ses champs de fin (position X, Y…). La plupart des champs sont typés (chaîne, entier, référence à un canal…), ce qui rend le flux lisible. Le couple (classe, sous-classe) correspond exactement à un type d'objet de l'export texte. L'identifiant d'objet est le même que dans l'export (`BEGIN n`).

**Références entre canaux.** Un canal en désigne un autre par son numéro dans son maître (`cf 04 [numéro] 00 [maître]`), pas par son identifiant. Les numéros suivent l'ordre de l'arbre et sont listés dans la table des symboles. Quand IQANdesign insère un canal, il renumérote ceux qui suivent.

**Compteur d'identifiants.** Le préambule de chaque bloc d'objets contient le compteur des identifiants attribués. Un nouvel objet prend un identifiant au-delà du plus grand existant, et le compteur est mis à jour dans tous les blocs.

## Validé dans IQANdesign (copies seulement, aucun contrôleur)

| Lot | Modification écrite par Claude dans le binaire | Résultat |
|---|---|---|
| 1 | Commentaire modifié (MD3) ; faute « temparture » corrigée dans un message (v2) | acceptés, export identique à la modification près |
| 1 | CRC du fichier faux ; CRC d'un bloc faux | refusés (attendu) |
| 2 | Temporisation `Delay on` 1000 → 1500 ms | acceptée, seule différence dans l'export |
| 2 | Sélecteur de fonction retiré (champ de taille différente) | accepté ; la fonction reprend le nom « Default function », comme dans IQANdesign |
| 3 | Ajout d'un commentaire ; ajout d'un canal en fin d'application ; ajout au milieu avec renumérotation | acceptés (sans renumérotation, IQANdesign plante) |

## Ce qui reste à faire pour tout écrire

Décoder les champs bruts de chaque type d'objet. Il y en a environ 145 dans nos projets, dont une quarantaine couvre 95 % des objets. La vérification est automatique : pour chaque objet des 7 projets, le codage produit doit redonner exactement les octets d'origine, et le décodage doit redonner les propriétés de l'export texte.
