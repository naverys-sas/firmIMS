# 11. Plan de construction

La v2 MC42 se construit **dans une copie de la v2 en cours** (108.3.1 + étape A, D6), par étapes courtes. Chaque étape laisse un projet qui compile, qui passe les contrôles, et qui se comporte exactement comme avant sauf changements décidés. On ne construit pas la nouvelle arborescence d'un coup à côté de l'ancienne : on **migre bloc par bloc**, en supprimant l'ancien bloc dès que le nouveau est en place.

Chaque étape se termine par :
1. enregistrement, export texte dans `exports/`, copie du `.idax` dans `v2/projet/` ;
2. `check_spec.py` (conformité à la conception), `compat_check.py` contre les cinq projets de référence, `anomalies.py`, `diff_versions.py` contre l'étape précédente ;
3. mise à jour de `DECISIONS.md` et commit.

| Étape | Contenu | Spécification | Prérequis | Effet sur les bateaux |
|---|---|---|---|---|
| **0** | Essais B1, B2, B5 ; exports B4 | [10_besoins_iqandesign.md](10_besoins_iqandesign.md) | — | aucun |
| **1** | Outils : `check_conventions.py`, extension d'`anomalies.py` (fonctions vides des interfaces, grille de journaux), feuilles de migration par lignée | [02_conventions.md](02_conventions.md), [08_compatibilite_migration.md](08_compatibilite_migration.md) | — (cloud) | aucun |
| **2** | `00 CFG` : déplacement des paramètres contrat, indicateurs `CFG Is_…`, nouveaux réglages ; tous les groupes lisent les `CFG Is_…` | [spec/00_CFG.csv](spec/00_CFG.csv) | B1 | aucun (défauts = 108.3.1) |
| **3** | `10 IO` : toutes les broches regroupées, renommées, choix par configuration | [09_faisceaux.md](09_faisceaux.md) | 2 | aucun |
| **4** | `20 EQP` : interfaces BAT, CHG, DRV, PMP, ENG (pilote J1939 unique), KBX, KPD ; la logique lit les interfaces | [spec/21_BAT.csv](spec/21_BAT.csv) à [spec/25_ENG.csv](spec/25_ENG.csv), [04_equipements.md](04_equipements.md) | 2, B5 | corrections D29 (Brusa, Zapi M1) |
| **5** | `80 HMI` : commandes arbitrées, mots d'état, messages regroupés ; adaptation des applications MD4-5 et MD4-10 au contrat | [spec/80_HMI.csv](spec/80_HMI.csv), [06_ihm.md](06_ihm.md) | 4 | correction bit super slow MD4-10 (D33), bascule Free unique |
| **6** | `40 PWR` et `30 ACT` : états système et cause d'arrêt, PMS, charge, gestion moteur, adaptateurs de propulsion | [05_logique_metier.md](05_logique_metier.md) §5.1-5.2 | 4, 5 | aucun |
| **7** | `50 TRK` : fusion E/T selon les décisions prises sur l'annexe des écarts | [spec/50_TRK.csv](spec/50_TRK.csv), [annexes/ecarts_E_T.md](annexes/ecarts_E_T.md) | 6, décisions de Nicolas sur l'annexe | aucun si règle par défaut |
| **8** | `55 HYD`, `60 THM`, `70 CAB` (avec PWM tendeur, accéléromètre) | [05_logique_metier.md](05_logique_metier.md) §5.4-5.6 | 6 | fonctions V25 retrouvées (options désactivées par défaut) |
| **9** | `85 LOG` : grille de journaux, tailles selon B6 | [spec/85_LOG.csv](spec/85_LOG.csv), [07_journalisation.md](07_journalisation.md) | 4 à 8, B6 | nouveaux journaux (les anciens restent) |
| **10** | `90 MNT` : forçages sous `MNT Mode`, contrôle 10 h et maintenances finalisés, nettoyage final (canaux morts, `AND False`, WIP) | [02_conventions.md](02_conventions.md) | 9 | forçages inopérants hors maintenance |
| **11** | `MD3 app` : module MD3 optionnel, pages thermiques (V69) et électriques (V35), radio, Proemion | [06_ihm.md](06_ihm.md) §6.4 | 5, B2 | ouverture aux bateaux lignée B |
| **12** | Projet **v2 MC2** : copie des blocs validés, couche `10 IO` MC2 | [05_logique_metier.md](05_logique_metier.md) §5.7, [09_faisceaux.md](09_faisceaux.md) §9.5 | 11 | ouverture aux bateaux lignée C |
| **13** | Validation : essais par ligne de la matrice (IQANsimulate si B10 concluant, puis banc), premier bateau pilote de chaque lignée avec l'accord de Nicolas | [08_compatibilite_migration.md](08_compatibilite_migration.md) | 12 | — |

Les étapes 2 à 10 ne changent rien de visible sur un bateau 108.x (hors corrections décidées) : elles peuvent être livrées à la flotte A au fil de l'eau, ce qui étale le risque. Les lignées B et C ne reçoivent la v2 qu'après les étapes 11 et 12.
