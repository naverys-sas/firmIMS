# Base de connaissances — V25.74 (Commuter, cabine)

Projet `docs/versions_firmware/ig29 v25.74.idax` (version 25.74, Antonin Groult, 24/03/2022). Export : [../exports/V25.74_Commuter.txt](../exports/V25.74_Commuter.txt). Même organisation que les autres bases : `fonctions/`, `index_canaux.csv`, `anomalies_auto.md`, `configuration.md`, `interfaces.md`.

## Ce que c'est

- **Même identifiant de projet que la 108.x** (`A9A417A5…`) : c'est l'**ancêtre direct** de la lignée v76 → 108. Un bateau en V25 qui reçoit une version de cette lignée garde donc ses réglages enregistrés, pour les paramètres qui ont gardé le même nom et le même type.
- Deux applications : **MD4-10** (écran cabine) et **MC42**. 1 920 canaux.
- Équipements : moteurs de chenilles **Sevcon ou Zapi** (`M-Track - Brand`), pompe hydraulique Sevcon, batteries **Kreisel, BMW (Torqeedo) ou WattAlps** (`Battery Brand`), chargeurs **Brusa, Elcon, BMW**, pack de climatisation **Aentron**, moteurs hors-bord en NMEA 2000 (**Mercury, Yamaha, COX**), Garmin, télécommande iPhone, keybox d'équipement, télémétrie Proemion.
- Sorties propres à la cabine : **commande PWM de pression du tendeur de chenilles** (`PWM Pression tendeur`, COUT-A = C1:14/39), électrovanne de tendeur, siège électrique (avant/arrière en PWM), télécommande de relevage, accéléromètre (`X`, `Z`).
- Journaux : `A/C Bat Pack`, `Acceleration`, `Electronic Logs`, `WattAlps Battery`, statistiques `Battery Use`, `Engine Use`, `Logs`, `Stat Log`.

## Ce que la 108.3.1 a perdu par rapport à la V25

Rapport complet : [../kb_flotte/compat/compat_v25_108.md](../kb_flotte/compat/compat_v25_108.md) (comparaison par nom ; beaucoup d'éléments ont seulement été renommés).

- **Commande PWM du tendeur de chenilles** : plus aucun canal ne pilote C1:14/39 en cabine. C'est l'écart déjà vu sur le plan de faisceau #24207.
- **Accéléromètre** et son journal `Acceleration`.
- **Batterie WattAlps**, **pack de climatisation Aentron**, **télécommande iPhone**, **télémétrie Proemion** (trames 0x7451223 à 0x7451250).
- Programmation des keyboxes d'équipement depuis l'écran (`Select Node`, `New ID`).

## Conséquences pour la v2

Les Commuter du registre en V25 (#025, #028 à #038, #051, #058) ont tous un MC42 et un MD4-10 : la v2 MC42 peut les couvrir, à condition de reprendre la commande PWM du tendeur, l'accéléromètre et les équipements encore montés (à vérifier dans le registre : aucun bateau n'y est noté avec une batterie WattAlps ni un pack Aentron, à part le refit #010).
