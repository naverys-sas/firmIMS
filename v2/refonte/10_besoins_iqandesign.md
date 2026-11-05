# 10. Ce qui doit se faire sur le PC (IQANdesign)

Le cloud n'a pas IQANdesign. Tout ce qui suit se fait sur le PC de Nicolas, par le fil « Analyse complète et refonte v2 » (pilotage d'IQANdesign à distance), **toujours sur une copie** dans `Documents\testia_sandbox\`, jamais sur un original, jamais connecté à un contrôleur. Chaque point dit ce qu'il faut faire, ce qu'il faut rapporter dans le dépôt et pourquoi il bloque (ou non) la suite.

B1, B2 et B11 sont faits (23/10/2026, [../essais/B1_B2.md](../essais/B1_B2.md)) et ont changé la méthode : trois projets (D38), paramètres déplacés par glisser-déposer, jamais coupés / collés (D40), sélecteurs d'extension pour les nouvelles marques (D41). Ordre recommandé pour la suite : B12, B13, puis B5.

## Essais qui conditionnent la méthode

| # | À faire | À rapporter | Bloque |
|---|---|---|---|
| **B1** ✓ | Persistance des réglages | **Fait.** Réglage conservé si même identifiant de projet, même identifiant interne du canal, même nombre d'états ; le nom ne compte pas. Renommer garde l'identifiant ; couper / coller en crée un nouveau et casse les 17 canaux qui utilisaient `eb Battery Brand` comme sélecteur. | — |
| **B2** ✓ | MD3 et MD4 dans le même projet | **Fait.** Impossible : IQANdesign 6.08 ne propose plus le MD3 à l'ajout, mais ouvre et modifie la V69 et la V35. D'où la v2 MC42-MD3 construite dans une copie de la V69. | — |
| **B11** ✓ | Glisser-déposer d'un paramètre vers un autre groupe | **Fait.** `eb Battery Brand` glissé de `E.BATTERY` vers `E.CHARGER` : numéro inchangé (128958), 27 références intactes, réglage conservé ; le bloc garde ses coordonnées et reste affiché en gris dans l'ancien groupe comme référence. Reste à voir le rangement des blocs dans les schémas. | — |
| **B12** | **Renommer un état** d'un sélecteur (par exemple `Spare 1` → `Test`) sur une copie : vérifier dans le manuel et à l'export que le nombre d'états et l'identifiant sont inchangés. | export, extrait du manuel | la méthode d'ajout d'une marque (02 §2.7, D41) |
| **B13** | **Copier un groupe d'un projet à l'autre** : copier un groupe de logique de la v2 en cours dans une copie de la V69 ; vérifier si les références vers des canaux de même nom existant dans la V69 se rétablissent, ou restent « Undefined ». Vérifier aussi qu'un groupe renommé garde ses objets (même `BEGIN`). | export avant / après, liste des références cassées | le report du socle dans la v2 MC42-MD3 et la v2 MC2 (D38). Si les références ne suivent pas, le report se fera par saisie pilotée depuis les fichiers `iqan/*.txt` |
| **B3** | Retrouver comment les Commuter V25 sont passés en V76 / 108 (#023 est en V23.76) : version V76 dans le dossier complet des versions, notes de mise à jour, ou question à l'atelier sur l'ID-tag du MC42 et l'adresse du MD4-10. | réponse, export de la V76 si trouvée | procédure de migration V25 (D24) |
| **B4** | Exporter en texte les versions manquantes du dossier complet des firmwares : **V65** (Novum + MD3, même lignée que la V69 : à comparer avant de construire la v2 MC42-MD3), V16, V23, V10.8.12, la dernière V5.x (5.55), et la V76. | exports dans `exports/`, régénération des bases `kb_…` | compatibilité des Novum MD3 (#065, #071, #072, #074) et des bateaux sans projet connu |
| **B5** | Vérifier qu'un groupe de fonctions peut être **copié** avec ses FGI et que les références internes suivent (pilote Zapi M1 → M2, keybox KTB → KBB → KTC). | essai sur une copie, export | méthode de construction de `23 DRV` et `26 KBX` (D28) |

## Mesures

| # | À faire | À rapporter |
|---|---|---|
| **B6** | Mémoire disponible pour les journaux : sur une copie, passer les journaux à 50 puis 100 entrées, ajouter un journal de 100 entrées, lire le rapport de mémoire / compilation d'IQANdesign pour le MC42 ; idem sur une copie de la V5.37 pour le MC2. | taux d'occupation par essai → tailles définitives (07 §7.2) |
| **B7** | Charge processeur : temps de cycle et occupation du MC42 annoncés par IQANdesign sur la 108.3.1 (référence pour vérifier que la v2 ne l'alourdit pas). | valeurs |
| **B8** | Valeur du canal de diagnostic d'un module optionnel (MD4-5, MD4-10) quand il est présent / absent, et comportement de l'application quand un module optionnel est absent ; dans la V69, comportement quand le MD3 est absent. | valeurs, extrait du manuel → définition de `CFG Has_…` |

## Pistes à instruire

| # | Sujet | Ce qu'on veut savoir |
|---|---|---|
| **B9** | **MD5** | version d'IQANdesign qui le supporte, licence nécessaire, ouverture d'un projet 6.08 sans perte, cohabitation MD5 + MD4 + MD3 dans un projet |
| **B10** | **IQANsimulate** comme jumeau numérique (demande du cahier des charges) | ce qui est installé avec la licence actuelle ; simulation d'un MC42 avec des trames CAN injectées (batterie, variateurs, moteur) ; possibilité de scripter des scénarios pour tester chaque ligne de la matrice de compatibilité sans banc |

## Construction (après B12, B13 et B5)

La saisie de la v2 suit [11_plan_de_construction.md](11_plan_de_construction.md). Pour chaque étape : le fichier `iqan/*.txt` correspondant dit quoi créer, champ par champ ; après saisie, l'export texte est commité et `check_spec.py` + `compat_check.py` + `anomalies.py` sont lancés. Les tâches répétitives (renommages, descriptions, rebranchements, déplacements par glisser-déposer) sont faites par pilotage de l'IDE ; les choix de comportement restent ceux de Nicolas.

## Questions pour Nicolas (pas d'IQANdesign nécessaire)

Rappelées dans le [README](README.md) : Q1 à Q6 et les questions de câblage F1 à F5 ([09_faisceaux.md](09_faisceaux.md) §9.7).
