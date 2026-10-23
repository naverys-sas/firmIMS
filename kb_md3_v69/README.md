# Base de connaissances — version MD3 V69.03.1

Projet `avecMD3_V69.03.01.WIP.idax` (« eb2/ford add/on », version 69.03.1, dernier enregistrement 27/07/2023 par Maxime B.). Même organisation de fichiers que [../kb_108_3_1/](../kb_108_3_1/README.md) : `fonctions/`, `index_canaux.csv`, `anomalies_auto.md`, `configuration.md`, `interfaces.md`, `outils/`.

Historique noté dans le projet : 69.01 « eb2 70 », 69.02 « correction div0 in Speed error », 69.03 « move exhaust sensor to mc42 ».

## Ce que c'est

- **Un projet distinct** de la lignée 108.x : identifiant de projet différent (`EF4370B5…` contre `A9A417A5…` pour v117/108.3.1), créé avec une autre version d'IQANdesign. Ce n'est pas une ancienne 108, c'est une branche parallèle.
- **Thermique uniquement** : moteurs EB2 1.2L ou Ford 1.5L (J1939, 250 kb/s). Pas de batterie haute tension, pas de chargeur, pas de variateurs.
- 689 canaux en 2 applications : **MC42** (468) et **MD3** (221).
- Équipements : écran **MD3**, radiocommande **Radio** (trames `0x100`/`0x101` : gauche, droite, stop, start, vitesse), télématique **Proemion**, **KeyBox** (13 relais), **Garmin** (position, date/heure), G1x.
- Groupes MC42 : `Initialization`, `KeyBox`, `Link MC42`, `Proemion`, `Screen State`, `Thermic` (Power, Oil security, Pump, Engine i/o EB2/Ford…), `Track Up/Down`, `Track tension`, `Translate`. Groupes MD3 : `BUZZER`, `BackLight`, `Link MD3`, `PIN`, `RADIO`, `UP_DOWN`.

## C'est l'ancêtre de la branche thermique de la 108.x

La plupart des groupes thermiques de la 108.3.1 (`mc.Thermic`, `T.Track…`, `T.KeyBox x100 T`) viennent de ce projet : mêmes noms de réglages dans les menus, mais les **canaux** ont été renommés avec le préfixe `T ` (`Engine type` → `T Engine type`, `IDLE Speed` → `T IDLE Speed`…).

## Écarts qui comptent pour la compatibilité (V69 → 108.3.1)

Détail complet : [compat_md3_v69_vers_108_3_1.md](compat_md3_v69_vers_108_3_1.md) (comparaison par nom, les applications n'ayant pas le même nom).

| Écart | Conséquence pour un bateau MD3 qu'on passerait en 108.3.1 |
|---|---|
| Projet différent, 113 paramètres renommés ou absents | les réglages du bateau ne sont **pas** repris automatiquement : il faut les relever et les ressaisir (ou les migrer par fichier de paramètres avec une table de correspondance) |
| **Sorties pompes inversées** : en V69 `COUT 0 = Pump 1 Right`, `COUT 1 = Pump 2 Left` ; en 108.3.1 `COUT 0 = T Pump 2 Left`, `COUT 1 = T Pump 1 Right` | si le câblage est le même, gauche et droite seraient permutées. **À vérifier sur un bateau MD3** |
| MC42 déclaré à l'adresse `[1]` en V69, `[0]` en 108.x | réglage d'adresse du module à reprendre |
| Radio, Proemion, Garmin (date/heure), MD3 absents de la 108.3.1 | fonctions à réintégrer comme options |
| Électrovannes : mêmes broches (8 à 14) dans les deux projets | compatible |
| Journaux : Thermic Events / Thermic Stats / Hydraulic Event / System Stats identiques ; « Check UP » (10 h) propre à V69 | compatible, à étendre |
