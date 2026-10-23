# Base de connaissances — V35.42 (X100)

Projet `docs/versions_firmware/X100 C V35.42.idax` (version 35.42, Antonin Groult, 22/09/2022 ; commentaire : ajout de mesures moteur thermique, modification des temps de refreinage en électrique). Export : [../exports/V35.42_X100.txt](../exports/V35.42_X100.txt).

## Ce que c'est

- **Même identifiant de projet que la MD3 V69** (`EF4370B5…`) : c'est l'**ancêtre direct** de la lignée MD3 (V65 → V69).
- Deux applications : **MD3** et **MC42**. 1 375 canaux. Un seul logiciel pour les X100 **thermiques et électriques** (`J1939 Speed` = 500 électrique / 250 thermique).
- Thermique : moteur **Ford 1.5** en J1939 (`Engine type`, une seule valeur), ventilateurs selon `Ambiante Temperature`.
- Électrique : moteurs de chenilles **Sevcon ou Zapi** (`M-Track - Brand`, `ZAPI Node`), pompe Sevcon HVLP en J1939, batteries **BMW (Torqeedo) ou WattAlps**, chargeurs **BMW, Brusa, Elcon**.
- Joysticks sur le **MD3** (entrées 0 et 1), radiocommande, keybox, Garmin, télémétrie Proemion. Réglage `Landing Block Number` (un ou deux blocs d'atterrissage).

## Écarts notables

Rapports : [../kb_flotte/compat/compat_v35_v69.md](../kb_flotte/compat/compat_v35_v69.md) et [../kb_flotte/compat/compat_v35_v2.md](../kb_flotte/compat/compat_v35_v2.md).

- La V69 a gardé le thermique et abandonné toute la partie électrique de la V35 (Sevcon, Zapi, BMW, WattAlps, HVLP). Les X100 électriques en V35 (#016, #026, #039, #042, #043, #053) ne peuvent donc passer ni en V69 ni, sans adaptation, en 108.3.1 (joysticks sur MD3, pas sur MD4).
- **Sortie pompe C1:14** : en V35, elle s'appelle `Pump 1 Right` et reçoit la consigne du **joystick droit**. En 108.3.1, la même broche reçoit la consigne du **joystick gauche**. Voir [../kb_flotte/lignees.md](../kb_flotte/lignees.md).
- #026 (Kreisel) et #043 (NovumTech), notés en V35 dans le registre, ont été refités depuis : leurs anciennes branches V35 ne sont plus à couvrir.
