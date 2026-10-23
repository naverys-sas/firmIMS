# 10. Ce qui doit se faire sur le PC (IQANdesign)

Le cloud n'a pas IQANdesign. Tout ce qui suit se fait sur le PC de Nicolas, par le fil « Analyse complète et refonte v2 » (pilotage d'IQANdesign à distance), **toujours sur une copie** dans `Documents\testia_sandbox\`, jamais sur un original, jamais connecté à un contrôleur. Chaque point dit ce qu'il faut faire, ce qu'il faut rapporter dans le dépôt et pourquoi il bloque (ou non) la suite.

Ordre recommandé : B1 et B2 d'abord, ils peuvent changer la méthode de construction.

## Essais qui conditionnent la méthode

| # | À faire | À rapporter | Bloque |
|---|---|---|---|
| **B1** | **Persistance des réglages.** (a) Lire dans le manuel IQANdesign 6.08 (aide installée) ce qui est conservé dans un contrôleur quand on charge une nouvelle version du même projet : valeurs des paramètres retrouvées par objet interne ou par nom ? (b) Sur une copie de la 108.3.1 : déplacer `eb Battery Brand` dans un autre groupe (glisser, puis couper/coller), renommer un autre paramètre, enregistrer, exporter en texte, comparer les numéros `BEGIN` avant / après. | extrait du manuel, les deux exports, conclusion | la règle D25 (déplacer au lieu de recréer) et toute l'étape 2 du plan |
| **B2** | **MD3 et MD4 dans le même projet.** Sur une copie de la 108.3.1 : ajouter un module MD3 optionnel (adresse 0) à côté du MC42 (0), du MD4-5 (1) et du MD4-10 (2), enregistrer, vérifier qu'IQANdesign l'accepte et que la compilation passe. | export texte, message d'erreur éventuel | la cible « un seul projet MC42 pour les lignées A et B » (D23). Si refusé : un projet MC42-MD3 séparé construit avec le même socle |
| **B3** | Retrouver comment les Commuter V25 sont passés en V76 / 108 (#023 est en V23.76) : version V76 dans le dossier complet des versions, notes de mise à jour, ou question à l'atelier sur l'ID-tag du MC42 et l'adresse du MD4-10. | réponse, export de la V76 si trouvée | procédure de migration V25 (D24) |
| **B4** | Exporter en texte les versions manquantes du dossier complet des firmwares : **V65** (Novum + MD3), V16, V23, V10.8.12, la dernière V5.x (5.55), et la V76. | exports dans `exports/`, régénération des bases `kb_…` | compatibilité des Novum MD3 (#065, #071, #072, #074) et des bateaux sans projet connu |
| **B5** | Vérifier qu'un groupe de fonctions peut être **copié** avec ses FGI et que les références internes suivent (pilote Zapi M1 → M2, keybox KTB → KBB → KTC). | essai sur une copie, export | méthode de construction de `23 DRV` et `26 KBX` (D28) |

## Mesures

| # | À faire | À rapporter |
|---|---|---|
| **B6** | Mémoire disponible pour les journaux : sur une copie, passer les journaux à 50 puis 100 entrées, ajouter un journal de 100 entrées, lire le rapport de mémoire / compilation d'IQANdesign pour le MC42 ; idem sur une copie de la V5.37 pour le MC2. | taux d'occupation par essai → tailles définitives (07 §7.2) |
| **B7** | Charge processeur : temps de cycle et occupation du MC42 annoncés par IQANdesign sur la 108.3.1 (référence pour vérifier que la v2 ne l'alourdit pas). | valeurs |
| **B8** | Valeur du canal de diagnostic d'un module optionnel (MD4-5, MD4-10, MD3) quand il est présent / absent, et comportement de l'application quand un module optionnel est absent. | valeurs, extrait du manuel → définition de `CFG Has_…` |

## Pistes à instruire

| # | Sujet | Ce qu'on veut savoir |
|---|---|---|
| **B9** | **MD5** | version d'IQANdesign qui le supporte, licence nécessaire, ouverture d'un projet 6.08 sans perte, cohabitation MD5 + MD4 + MD3 dans un projet |
| **B10** | **IQANsimulate** comme jumeau numérique (demande du cahier des charges) | ce qui est installé avec la licence actuelle ; simulation d'un MC42 avec des trames CAN injectées (batterie, variateurs, moteur) ; possibilité de scripter des scénarios pour tester chaque ligne de la matrice de compatibilité sans banc |

## Construction (après B1, B2, B5)

La saisie de la v2 suit [11_plan_de_construction.md](11_plan_de_construction.md). Pour chaque étape : le fichier `iqan/*.txt` correspondant dit quoi créer, champ par champ ; après saisie, l'export texte est commité et `check_spec.py` + `compat_check.py` + `anomalies.py` sont lancés. Les tâches répétitives (renommages, descriptions, déplacements) sont faites par pilotage de l'IDE ; les choix de comportement restent ceux de Nicolas.

## Questions pour Nicolas (pas d'IQANdesign nécessaire)

Rappelées dans le [README](README.md) : Q1 à Q6 et les questions de câblage F1 à F5 ([09_faisceaux.md](09_faisceaux.md) §9.7).
