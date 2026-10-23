# Les lignées de projets IQAN

Un projet IQAN garde son **identifiant** d'une version à l'autre. Tant qu'on charge une version qui a le même identifiant, le contrôleur conserve ses réglages ; avec un identifiant différent, il les efface et repart avec de nouveaux journaux. Les cinq projets en notre possession appartiennent à **trois lignées** seulement :

| Lignée (identifiant) | Versions en notre possession | Matériel | Bateaux (registre) |
|---|---|---|---|
| **A** `A9A417A5…` | **V25.74** (2022) → v117 → **108.3.1** | MC42 + MD4-10 (Commuter), puis MC42 + MD4-5 / MD4-10 | Commuter V16 à V25, puis tous les bateaux depuis #076 |
| **B** `EF4370B5…` | **V35.42** (2022) → **V69.03.1** | MC42 + MD3 | X100 électriques et thermiques V35, puis V65 à V69 (2022) |
| **C** `D2FDEFEA…` | **V5.37** | MC2 + MD3 | Original thermiques VW / Ford, #007 à #027 |

Rapports d'écart : [compat/compat_v25_108.md](compat/compat_v25_108.md), [compat/compat_v35_v69.md](compat/compat_v35_v69.md), [compat/compat_v25_v2.md](compat/compat_v25_v2.md), [compat/compat_v35_v2.md](compat/compat_v35_v2.md).

## Ce que chaque lignée a perdu en route

- **A, de V25 à 108.3.1** : commande PWM du tendeur de chenilles en cabine (C1:14/39), accéléromètre, batterie WattAlps, pack de climatisation Aentron, télécommande iPhone, télémétrie Proemion, programmation des keyboxes depuis l'écran.
- **B, de V35 à V69** : toute la partie électrique (moteurs Sevcon / Zapi, pompe HVLP, batteries BMW et WattAlps, chargeurs Brusa / Elcon / BMW). La V69 est purement thermique.

## La sortie pompe C1:14 change de joystick selon la lignée

Vérifié en remontant la chaîne de canaux dans chaque projet :

| Projet | Nom de la sortie C1:14 | Joystick qui la commande |
|---|---|---|
| V35.42 (B) | `Pump 1 Right` | **droit** (entrée MD3 n° 1) |
| V69.03.1 (B) | `Pump 1 Right` | **droit** (entrée MD3 n° 1) |
| 108.3.1 (A) | `T Pump 2 Left mc 14` | **gauche** (C1:36, ou entrée C2:1 du MD4) |
| Faisceau #22679 IND N (2024) | `Right_Pump` | — |

Les deux lignées envoient donc **des consignes opposées sur la même broche**. Comme les bateaux des deux lignées naviguent, la différence est forcément compensée ailleurs : tuyauterie hydraulique croisée sur les bateaux récents, ou câblage différent. Personne ne sait aujourd'hui lequel (réponse de Nicolas, 23/10/2026).

**Conséquence (décision D21)** : le réglage `T Pump wiring` de la v2 ne peut pas avoir une seule valeur par défaut valable pour toute la flotte. La valeur par défaut reste celle de la 108.3.1 (aucun changement pour la lignée A). Pour un bateau qui vient de la lignée B (ou de la C, à vérifier), la procédure de migration doit régler `T Pump wiring` sur la valeur inverse, puis contrôler à quai que le joystick droit fait bien tourner la chenille droite.

## Bateaux dont la version exacte n'est pas en notre possession

- #026 et #043 (anciennes branches V35 Kreisel et Novum) : refités depuis, plus à couvrir (Nicolas, 23/10/2026).
- Novum à écran MD3 (#065, #071, #072, #074) en **V65** : projet à récupérer (lignée B).
- #024 (V16.34) et #023 (V23.x) : versions antérieures à la V25.
- #010 (V10.8.12, refit Aentron) : version unique.
