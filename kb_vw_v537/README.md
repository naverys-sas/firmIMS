# Base de connaissances — version MD3 + moteur VW V5.37

Projet `version_avec_MD3_et_moteur_VW_V5.37.idax` (version 5.37, auteur Florent de Labarre, dernier enregistrement 20/07/2021 par Antonin G.). Même organisation que les autres bases : `fonctions/`, `index_canaux.csv`, `anomalies_auto.md`, `configuration.md`, `interfaces.md`, `outils/`.

## Ce que c'est

- **Un troisième projet distinct** (identifiant `D2FDEFEA…`), différent de la lignée MD3 V69 (`EF4370B5…`) et de la lignée 108.x (`A9A417A5…`).
- **Autre contrôleur : MC2** (pas MC42), avec écran **MD3**, radiocommande **Radio** (125 kb/s), moteur en **J1939** (250 kb/s), G1x. 486 canaux : MC2 (287), MD3 (199).
- **Thermique uniquement** : réglage `Engine type` = VW 2.0L (défaut) ou FORD 1.5L ; 13 canaux en dépendent (courants de pompe avant/arrière par vitesse, régimes ralenti, lent, rapide, relevage, tension).
- **Bloc hydraulique** au choix : `Hydraulic Bloc` = V01, V01 - Locking, V17 - Locking (7 canaux en dépendent). Ce réglage n'existe plus dans les versions suivantes.
- Le MC2 pilote directement le moteur : `Out SWITCH ON Engine` (sortie 20), `Out START Engine` (21), ventilateurs (22, 23), alimentations bloc/moteur/vérins (5, 6, 7), tendeur de chenille en PWM (4).
- Groupes MC2 : `Engine Fan`, `Oil Security`, `SAEJ ECM` (SPN moteur), `SAEJ Std input`, `Screen State`, `Speed Engine`, `Track Tension`, `Translate`, `UP DOWN TRACK`. Groupes MD3 : `Acceleration`, `BLACK LIGHT`, `BUZZER`, `RADIO`, `RUN PAGE`, `START PAGE`.

## Conséquences pour la v2

- Le câblage est **entièrement différent** de celui du MC42 (électrovannes sur les sorties 12 à 19 au lieu de 8 à 14, sorties moteur directes, sortie PWM de tendeur). Un projet MC42 ne peut pas piloter ce bateau.
- Un projet IQAN est lié à ses modules : la v2 de ces bateaux sera **une application MC2 distincte**, construite avec les mêmes blocs de logique que la v2 MC42 mais avec sa propre couche d'entrées/sorties.
- Écarts détaillés : [compat_vw_v537_vers_md3_v69.md](compat_vw_v537_vers_md3_v69.md) et [compat_vw_v537_vers_108_3_1.md](compat_vw_v537_vers_108_3_1.md).
