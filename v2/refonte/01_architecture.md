# 1. Architecture cible

Ce document décrit la structure du firmware v2 telle qu'elle doit apparaître dans IQANdesign : applications, groupes de fonctions, et règles de communication entre groupes. Il remplace la section 2 de [../proposition_v2.md](../proposition_v2.md), qui restait une esquisse. Les décisions correspondantes sont D22 à D36 dans [../DECISIONS.md](../DECISIONS.md).

## 1.1 Deux projets, un seul socle

| Projet | Contrôleur | Écrans | Bateaux | Identifiant de projet |
|---|---|---|---|---|
| **v2 MC42** | MC42, ID-tag **0** | MD4-5 (adresse 1), MD4-10 (adresse 2), MD3 (adresse 0), tous optionnels ; MD5 plus tard | lignée A (V25 → 108.3.1) et lignée B (V35 → V69) : tous les bateaux MC42, électriques et thermiques | celui de la 108.3.1 (`A9A417A5…`), voir D6 |
| **v2 MC2** | MC2 | MD3 | lignée C (V5.x) : Original thermiques VW / Ford, #002 à #027 | celui de la V5.37 (`D2FDEFEA…`) |

Le **socle** est la conception commune : mêmes couches, mêmes noms, mêmes interfaces, mêmes journaux. Le projet MC2 n'en reprend que la partie thermique, avec sa propre couche d'entrées/sorties (le câblage MC2 n'a rien à voir avec celui du MC42). Un correctif de logique se fait d'abord dans la v2 MC42, puis se reporte dans la v2 MC2 par copier-coller du groupe concerné, vérifié par `diff_versions.py`.

Pourquoi pas un seul projet pour tout : un projet IQAN est lié à ses modules maîtres, et MC2 et MC42 n'ont ni les mêmes broches ni les mêmes ressources. Pourquoi pas trois projets comme aujourd'hui : les lignées A et B ont le même contrôleur et le même câblage hydraulique ; seuls l'écran et l'adresse du MC42 changent (voir §1.5).

## 1.2 Les couches

Le MC42 contient toute la logique. Il est découpé en couches qui ne communiquent que dans un sens : une couche lit la couche du dessous, jamais celle du dessus.

```
                ┌──────────────────────────────────────────────────────────────┐
  écrans        │ MD4-5 app · MD4-10 app · MD3 app · (MD5 app)                  │  pages, joysticks locaux,
  (apps)        │   ne font que traduire : boutons → commandes, états → pages   │  buzzer, NMEA, A/C 24 V
                └───────────────▲──────────────────────────────┬───────────────┘
                                │ APPIN/APPOUT (contrat IHM, §6) │
 MC42 app ┌─────────────────────┴──────────────────────────────▼───────────────┐
          │ 80 HMI   commandes fusionnées (écrans, keypad, keyboxes, radio)     │
          │          états publiés, messages                                    │
          ├─────────────────────────────────────────────────────────────────────┤
          │ 40 PWR  50 TRK  55 HYD  60 THM  70 CAB    logique métier, écrite    │
          │ (énergie,(chenilles)(hydraulique)(refroid.)(cabine)   une seule fois │
          ├─────────────────────────────────────────────────────────────────────┤
          │ 30 ACT   adaptateurs de propulsion : consigne chenilles → variateurs  │
          │          (électrique) ou pompes + régime moteur (thermique)          │
          ├─────────────────────────────────────────────────────────────────────┤
          │ 20 EQP   pilotes d'équipements CAN, un groupe par marque,            │
          │          chacun remplit l'interface normalisée de sa famille (§4)    │
          ├─────────────────────────────────────────────────────────────────────┤
          │ 10 IO    broches physiques du MC42 (seul endroit qui les touche)     │
          ├─────────────────────────────────────────────────────────────────────┤
          │ 00 CFG   réglages de variante (contrat), canaux Is_…, constantes     │
          └─────────────────────────────────────────────────────────────────────┘
            85 LOG  journaux (lit tout, n'est lu par personne)
            90 MNT  maintenance, forçages, simulation (désactivé hors mode maintenance)
```

| Couche | Rôle | Lit | Est lu par |
|---|---|---|---|
| **00 CFG** | Tous les paramètres de variante (marque de batterie, moteur, propulsion…), les canaux `Is_…` qui activent les groupes, les constantes. | rien | tout le monde |
| **10 IO** | Une entrée ou sortie physique = un canal, nommé avec sa broche. Les sorties lisent une consigne venue de la logique ; les entrées sont mises à l'échelle ici. Aucun autre groupe ne déclare de canal physique. | consignes des couches 30 à 70 | couches 20 à 70 |
| **20 EQP** | Pilotes CAN : décodage et encodage des trames d'**une** marque, surveillance de communication (timeout, heartbeat), puis publication des grandeurs normalisées de la famille. | CFG, trames | la famille normalisée seulement |
| **30 ACT** | Traduit les consignes « propulsion » de la logique en ordres pour le matériel présent : variateurs SEW (électrique) ou pompes Rexroth et régime moteur (thermique). C'est la couche qui permet d'écrire la logique chenilles une seule fois. | interfaces normalisées, consignes TRK | IO, EQP (trames sortantes) |
| **40 à 70** | Logique métier : énergie et états du système, chenilles, hydraulique, refroidissement, équipements de cabine. Chaque bloc ne lit que des interfaces normalisées et des commandes HMI. | CFG, interfaces normalisées, HMI (commandes) | ACT, IO, HMI (états), LOG |
| **80 HMI** | Côté entrée : fusionne les boutons de tous les écrans, du keypad, des keyboxes et de la radio en **une** commande par fonction. Côté sortie : publie les états à afficher et porte les messages. | apps écrans (APPIN), logique métier | logique métier (commandes), apps écrans (APPOUT) |
| **85 LOG** | Journaux d'événements et de statistiques (voir [07_journalisation.md](07_journalisation.md)). | tout | personne |
| **90 MNT** | Forçages, tests, simulation, menus de debug. Un seul réglage maître les rend inopérants hors maintenance. | CFG | couches 10 à 70, uniquement via des canaux `MNT …` documentés |

## 1.3 Arborescence du MC42 app

Les numéros sont dans le nom du groupe : ils fixent l'ordre de lecture et de documentation. Les groupes de premier niveau ne sont jamais désactivés ; ce sont leurs sous-groupes de marque ou d'option qui le sont, par un canal `Is_…`.

```
MC42 app
├─ 00 CFG Configuration
│   ├─ CFG Settings (contract)     tous les paramètres réglables existants, inchangés (voir 03_configuration.md)
│   ├─ CFG Variant flags           Is_Electric, Is_Thermic, Is_Cab, Is_X100, Is_BAT_Novum… (IDC)
│   └─ CFG Constants
├─ 10 IO MC42 pins
│   ├─ IO Hydraulic block          EV tension/lock/up/down/by-pass/unlock, pressions, niveau, T° huile
│   ├─ IO Propulsion thermal       sorties pompes C1:14/15 (avec T Pump wiring), état pompe, capteurs moteur
│   ├─ IO Power relays             relais variateurs, reset batterie / frein (selon is_cab_mc)
│   ├─ IO Cab                      siège, échelle, télécommande, PWM tendeur (V25), accéléromètre
│   └─ IO Joystick & level         joystick gauche C1:36, joystick droit / niveau d'eau C1:24
├─ 20 EQP Equipment drivers
│   ├─ 21 BAT Battery              interface BAT + sous-groupes Torqeedo(BMW) · Novum · Tyva(+Bender g1/g2) · Kreisel
│   ├─ 22 CHG Charger              interface CHG + Torqeedo(BMW) · Brusa · Elcon
│   ├─ 23 DRV Traction inverters   interface DRV (M1 droite, M2 gauche) + Sevcon gen4 · Zapi M1 · Zapi M2
│   ├─ 24 PMP Pump inverter        interface PMP (M3) + Sevcon HVLP CANopen (« gen ») · Sevcon HVLP J1939
│   ├─ 25 ENG Thermal engine       interface ENG + J1939 engine (EB2, Ford, Kubota : un seul pilote)
│   ├─ 26 KBX Keyboxes             Keybox X100 (relais E ou T) · Keyboxes cab KTB/KBB/KTC (un modèle, trois instances)
│   ├─ 27 KPD Keypad Blink
│   └─ 28 TEL Telemetry            Proemion (option, lignées A V25 et B)
├─ 30 ACT Propulsion adapters
│   ├─ ACT Traction                consigne chenille G/D → variateurs (E) ou courants pompes + régime (T)
│   └─ ACT Hydraulic power         demande de puissance hydraulique → pompe M3 (E) ou régime moteur (T)
├─ 40 PWR Power & system state
│   ├─ PWR System state            démarrage, « système prêt », arrêt et sa cause, auto-off, keep-on
│   ├─ PWR Battery management      PMS (Standby/Discharge/Charge/Crash/Auto-off), watchdog, protection
│   ├─ PWR Charging                machine de charge, consignes chargeur, fin de charge, équilibrage
│   └─ PWR Engine management       démarrage/arrêt moteur thermique, sécurités, consigne de régime
├─ 50 TRK Tracks
│   ├─ TRK Translate               joysticks → consignes G/D (modes de vitesse, différentiel, rampes)
│   ├─ TRK Tension                 tension des chenilles (EV ou PWM selon variante)
│   └─ TRK Up/Down                 relevage, blocage/déblocage, verrous, blocs d'atterrissage
├─ 55 HYD Hydraulics               niveau, pression, température d'huile, sécurité huile
├─ 60 THM Thermal management       ventilateurs et pompes à eau (moteur thermique ou variateurs)
├─ 70 CAB Cab equipment            éclairage, essuie-glace, guindeau, douche, siège, options AUX, gonflage 24 V
├─ 80 HMI Human-machine interface
│   ├─ HMI Inputs                  dépaquetage des APPIN de chaque écran, keypad, radio → commandes CMD …
│   ├─ HMI Command arbitration     une commande par fonction, avec la priorité des sources
│   ├─ HMI Outputs                 paquetage des états publiés → APPOUT (un jeu commun à tous les écrans)
│   └─ HMI Messages                tous les messages (CMSG/IMSG), classés par famille
├─ 85 LOG Logs                     canaux d'événement normalisés (les journaux eux-mêmes sont hors groupes dans IQAN)
└─ 90 MNT Maintenance              mode maintenance, forçages, tests, simulation, contrôle 10 h et maintenances
```

Applications écran :

```
MD4-5 app   (tableau de bord, toutes coques sauf cabine)  HMI link · pages · joystick local · buzzer · niveau d'eau V10
MD4-10 app  (Commuter)                                     HMI link · pages · joystick local · buzzer · NMEA/hors-bords · GPS · A/C Tyva 24 V
MD3 app     (bateaux lignée B)                              HMI link · pages · joysticks locaux · buzzer · radio
MD5 app     (futur)                                         HMI link · pages · …   (même contrat, voir 06_ihm.md)
```

## 1.4 Règles de communication entre groupes

1. **Une couche ne lit que les couches du dessous**, plus `00 CFG`. La logique métier ne lit jamais un canal d'un pilote de marque (`Tyva …`, `Zapi …`) : elle lit l'interface normalisée (`BAT SOC`, `DRV M1 speed`…).
2. **Les entrées d'un groupe réutilisable passent par des FGI** (Function group input). C'est déjà ainsi que sont faits les pilotes de chargeur dans la 108.3.1 (`Charger CMD`, `Charger UMax`, `Charger IMax`). On généralise : les pilotes Zapi M1 et M2, les trois keyboxes cabine et le pilote moteur J1939 sont un même groupe copié, dont seuls les FGI changent.
3. **Les sorties d'un groupe sont des canaux publics nommés avec le préfixe du groupe.** Un canal interne garde un nom court et une portée privée. Un lecteur sait donc à coup d'œil si un canal est un contrat (préfixe) ou un détail (sans préfixe).
4. **Un sélecteur de marque n'apparaît qu'à un seul endroit par famille** : dans les canaux d'interface de la famille (`Function selector = eb Battery Brand`). Ailleurs, on ne teste pas la marque.
5. **Pas de logique dans les écrans** au-delà de la traduction bouton → bit et bit → affichage, et des équipements raccordés physiquement à l'écran (NMEA, A/C 24 V, joystick local). C'est ce qui rend le passage MD4 → MD5 local.
6. **Aucune fonction morte** : pas de `AND False`, pas de groupe `WIP`/`broken`/`soon`. Une fonction inachevée vit dans une branche du dépôt, pas dans le projet livré ; une option désactivée l'est par un réglage nommé.

## 1.5 Points matériels qui contraignent l'architecture

**Adresses des modules maîtres.** IQAN identifie un module par son type **et** son adresse. Le MC42 reçoit son adresse par l'ID-tag câblé entre ADDR-H et ADDR-L ; s'il ne correspond pas au projet, le MC42 affiche « R3:2 IdTag error » et ne démarre pas l'application (notice MC4x, p. 60 et codes d'erreur).

| Lignée | MC42 | MD4-10 | MD4-5 | MD3 |
|---|---|---|---|---|
| A, V25.74 | **1** | **0** | — | — |
| A, 108.3.1 | 0 | 2 | 1 | — |
| B, V35 / V69 | **1** | — | — | 0 |
| v2 MC42 | 0 | 2 | 1 | 0 |

MD3 et MC42 étant de types différents, ils peuvent tous deux avoir l'adresse 0. En revanche le MC42 ne peut avoir qu'une adresse dans un projet. La v2 garde celle de la 108.3.1 (0) : les bateaux les plus récents et les plus nombreux à mettre à jour ne changent rien. Pour un bateau V25 ou lignée B, la migration comprend **le remplacement de l'ID-tag du MC42 (1 → 0)** et, pour un Commuter V25, le passage de l'adresse du MD4-10 de 0 à 2 dans le menu système de l'écran. Décision D24 ; la façon dont les Commuter V25 ont été passés en V76 est à retrouver (voir [10_besoins_iqandesign.md](10_besoins_iqandesign.md), B3).

**Port CAN B partagé** (keyboxes cabine à 125 kb/s, moteurs J1939 à 250 kb/s, électrique à 500 kb/s) : limite conservée, sans conséquence puisque les Commuter sont tous électriques.

**Broche C1:14/39/55 (COUT-A)** : consigne de pompe thermique (gauche ou droite selon `T Pump wiring`, D18/D21) ou, en cabine V25, commande PWM du tendeur. La même sortie est donc pilotée par `ACT Traction` ou par `TRK Tension` selon `is_cab_mc`, jamais les deux.

**Broches C1:26 / C1:36 / C1:52** : accéléromètre X/Y/Z en cabine (V25, faisceau #24207), état pompe / joystick gauche / température échappement en X100. Choix par `is_cab_mc` dans `10 IO`.

## 1.6 Ce que l'architecture supprime

| Aujourd'hui (108.3.1) | En v2 |
|---|---|
| Translate, Track tension, Track Up/Down, KeyBox X100 en copies E et T (≈ 330 canaux, divergentes) | un bloc `50 TRK` et un pilote `26 KBX` ; les écarts deviennent des réglages ou des entrées (annexe [ecarts_E_T.md](annexes/ecarts_E_T.md)) |
| Trois pilotes moteur identiques EB2 / Ford / Kubota (3 × 38 canaux, même adresse source 0) | un pilote J1939 ; le type de moteur ne choisit que les calibrations |
| Zapi M1 et Zapi M2 écrits deux fois (72 + 71 canaux) | un groupe copié deux fois, FGI nœud et côté, vérifié identique par script |
| 3 × 13 messages « fuse is blown » par keybox cabine, 2 × 13 pour la keybox X100 | un message par relais et par keybox, généré par le même modèle de groupe |
| Logique d'écran répartie entre `mc.Link…`, `logic screen md4`, `logic screen c10 and KB`, `mc.d4s`, `mc.d3` | `80 HMI` : une entrée, un arbitrage, une sortie, quel que soit l'écran |
| 38 réglages de forçage dispersés dans les menus Master | `90 MNT`, inopérants hors mode maintenance |
| 275 canaux lus par personne, 8 `AND False`, 6 groupes WIP/broken/soon | supprimés, ou transformés en option nommée |
