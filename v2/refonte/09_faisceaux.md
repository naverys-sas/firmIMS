# 9. Plans de faisceaux v2 (brochage logiciel)

Ce document fixe, broche par broche, ce que la v2 attend sur chaque connecteur. Il sert à la fois de spécification pour la couche `10 IO` et de référence pour l'atelier. Sources : brochages relevés dans IQANdesign ([../../faisceaux/](../../faisceaux/)), plans RapidHarness de `docs/schemas/` (#22679 X100 thermique IND N, #28580 X100 électrique IND H, #24207 MC42 CAB IND L, #26062 MD4-10, #33530 MD4 X100), exports V25.74, V35.42, V69 et V5.37.

**Aucun changement de câblage n'est demandé par la v2**, sauf l'ID-tag du MC42 et l'adresse du MD4-10 sur les Commuter V25 (§9.6). Les broches dont l'usage dépend de la configuration sont choisies dans `10 IO` par `CFG Is_Cab` / `CFG Is_Thermic`.

## 9.1 MC42, connecteur C1 (66 voies)

Colonnes : X100 thermique (T), X100 électrique (E), Commuter (Cab, toujours électrique). « — » = non utilisé dans cette configuration.

| Broche | Ressource | Canal v2 | X100 T | X100 E | Cab | Remarques |
|---|---|---|---|---|---|---|
| C1:2 / 18 | CAN-B | bus B | J1939 moteur 250 kb/s | J1939 HVLP 500 kb/s | keyboxes cabine 125 kb/s | `CAN Speed B mc` |
| C1:3 / 19 | CAN-C | bus C | keybox X100, keypad | variateurs, batterie, chargeur, keybox X100, keypad | batterie HT, chargeur, variateurs, pompe HVLP « gen » | `CAN Speed C mc` |
| C1:1 / 17 | CAN-A | bus Master + diagnostic | écrans, G1x | idem | idem | |
| C1:4 / 20 | ADDR-L / ADDR-H | ID-tag | **0** | **0** | **0** | v2 MC42-MD4 ; **1** dans la v2 MC42-MD3 (lignée B), voir §9.6 |
| C1:7 | +VREF-A | alimentation capteurs | ✔ | ✔ | ✔ | |
| C1:8 | VIN-A | `IO Oil level C1:8` | ✔ | ✔ | ✔ | |
| C1:9 | VIN-B | `IO Lock pressure C1:9` | ✔ | ✔ | ✔ | |
| C1:10 | VIN-C | `IO Track pressure C1:10` | ✔ | ✔ | ✔ | |
| C1:11 / 12 | DPCNT-A | `IO Ladder sensor C1:11` | — | — | capteur Hall échelle | |
| C1:14 / 39 / 55 | COUT-A | `IO COUT-A C1:14` | pompe (gauche en 108, droite en V35/V69 ; `T Pump wiring`) | — | **PWM tendeur** si `Cab track tension` = PWM (V25) | une seule fonction par configuration |
| C1:15 / 40 / 56 | COUT-B | `IO COUT-B C1:15` | pompe (l'autre côté) | — | — | |
| C1:24 | VIN-D | `IO Joystick right / water level C1:24` | joystick droit MC42 (option) | joystick (IND H : **gauche**, voir §9.7) | niveau d'eau (R10) | |
| C1:25 | VIN-E | `IO Oil temp / bilge current C1:25` | température huile | température huile | courant de cale (R11) | |
| C1:26 | VIN-F | `IO Pump status / accel X C1:26` | état pompe | — | accéléromètre X (option) | |
| C1:28 | DIN-M | `IO Remote down C1:28` | — | — | télécommande descente | |
| C1:29 | DIN-N | `IO Remote up C1:29` | — | — | télécommande montée | |
| C1:36 | VIN-G | `IO Joystick left / accel Y C1:36` | joystick gauche MC42 | joystick (IND H : **droit**) | accéléromètre Y (option) | |
| C1:38 | VIN32-A | `IO 24V inflate voltage C1:38` | tension gonflage 24 V (option) | idem | — | plan IND N : « Current_sensor » (question F3) |
| C1:41 | DOUT-I | `IO EV by-pass C1:41` | ✔ | ✔ | ✔ | |
| C1:42 | DOUT-K | `IO EV down C1:42` | ✔ | ✔ | ✔ | |
| C1:43 | DOUT-M | `IO EV unlock C1:43` | ✔ | ✔ | ✔ | |
| C1:44 | DOUT-O | `IO Brake / batt reset / var power C1:44` | frein | reset batterie HT (Novum) ou ON batterie (Tyva) | alimentation variateurs | selon `CFG Is_Cab` et marque |
| C1:45 | PWM-G | `IO Seat up/down C1:45` | — | — | siège | option `electronic seat` |
| C1:46 / 57 | DOUT-J | `IO EV up C1:57` | ✔ | ✔ | ✔ | |
| C1:47 / 60 | DOUT-P | `IO Var power / batt reset C1:60` | — | alimentation variateurs (boîte FBA) | reset batterie | selon `CFG Is_Cab` |
| C1:48 | PWM-J | `IO Seat front/back C1:48` | — | — | siège | option |
| C1:52 | VIN-H | `IO Exhaust temp / accel Z C1:52` | température échappement | — | accéléromètre Z (option) | |
| C1:54 | VIN32-B | `IO Port voltage C1:54` | tension démarreur / port | — | — | |
| C1:58 | DOUT-L | `IO EV tension C1:58` | ✔ | ✔ | ✔ (si `Cab track tension` = Valve) | |
| C1:59 | DOUT-N | `IO EV lock C1:59` | ✔ | ✔ | ✔ | |
| C1:65 / 66 | +BAT / −BAT | alimentation | | | | |

## 9.2 MD4-5 (tableau de bord, adresse 1)

| Broche | Ressource | Canal v2 | Usage |
|---|---|---|---|
| C2:1 | VIN-A | `IO MD45 joystick left / water level C2:1` | joystick gauche si `Joystick plugged md45`, sinon niveau d'eau V10 (D12) |
| C2:2 | VIN-B | `IO MD45 joystick right C2:2` | joystick droit si `Joystick plugged md45` |
| C2:3 | DOUT-A | `IO MD45 buzzer C2:3` | buzzer |

## 9.3 MD4-10 (Commuter, adresse 2)

| Broche | Ressource | Canal v2 | Usage |
|---|---|---|---|
| C2:1 | VIN-A | `IO MD410 joystick left C2:1` | si `Joystick plugged md10` |
| C2:2 | VIN-B | `IO MD410 joystick right C2:2` | si `Joystick plugged md10` |
| C2:3 | DOUT-A | `IO MD410 buzzer C2:3` | buzzer |
| C2:6 | DIN-D | `IO MD410 cabin button C2:6` | bouton cabine |
| C2:7 | DIN-E | `IO MD410 door button C2:7` | bouton porte |
| CAN C | 250 kb/s, 29 bits | NMEA 2000 | hors-bords Mercury / Yamaha / COX, GPS Garmin |
| CAN D | | batterie Tyva 24 V | climatisation (option `a/c option tyva`) |

## 9.4 MD3 (bateaux lignée B, adresse 0)

| Broche | Ressource | Canal v2 | Usage |
|---|---|---|---|
| C2:1 | VIN-A | `IO MD3 joystick left C2:1` | joystick gauche (`Joystick plugged md3`) |
| C2:2 | VIN-B | `IO MD3 joystick right C2:2` | joystick droit |
| C2:12 | DOUT-A | `IO MD3 buzzer C2:12` | buzzer |
| CAN | 125 kb/s | radio | radiocommande (option `Radio remote`) |

## 9.5 MC2 (projet v2 MC2, bateaux lignée C)

Repris de la V5.37 sans changement.

| Broche | Ressource | Canal v2 | Usage |
|---|---|---|---|
| C1:2 / 16 / 30 | COUT-A | `IO Pump right C1:2` | pompe droite (« Pump 1 Right ») |
| C1:3 / 17 / 31 | COUT-B | `IO Pump left C1:3` | pompe gauche |
| C1:4 | DOUT-C | `IO EV lock select C1:4` | blocage / sélecteur (`Hydraulic Bloc`) |
| C1:5 | DOUT-D | `IO EV unlock C1:5` | déblocage |
| C1:7 | VIN-E | `IO Oil level C1:7` | niveau d'huile |
| C1:8 / 22 / 36 | COUT-E | `IO Track tension PWM C1:8` | tendeur en PWM |
| C1:9 | DOUT-F | `IO Supply by-pass brake C1:9` | alimentation by-pass et frein |
| C1:10 | DOUT-G | `IO Supply engine C1:10` | alimentation moteur |
| C1:11 | DOUT-H | `IO Supply cylinder tension C1:11` | alimentation vérins et tendeur |
| C1:18 | DOUT-M | `IO EV brake C1:18` | frein |
| C1:19 | DOUT-O | `IO EV down C1:19` | descente |
| C1:20 | DIN-A | `IO Pump status C1:20` | état pompe |
| C1:23 | DOUT-S | `IO EV tension C1:23` | tension chenille |
| C1:24 | DOUT-U | `IO Engine switch on C1:24` | contact moteur |
| C1:25 | DOUT-W | `IO Engine fan C1:25` | ventilateur |
| C1:32 | DOUT-N | `IO EV by-pass C1:32` | by-pass |
| C1:33 | DOUT-P | `IO EV up C1:33` | montée |
| C1:34 | VIN-C | `IO Track pressure C1:34` | pression chenilles |
| C1:35 | VIN-D | `IO Lock pressure C1:35` | pression de blocage |
| C1:37 | DOUT-T | `IO EV untension C1:37` | détente chenille |
| C1:38 | DOUT-V | `IO Engine start C1:38` | démarreur |
| C1:39 | DOUT-X | `IO Engine full fan C1:39` | ventilation pleine |

MD3 du projet MC2 : comme §9.4, plus accéléromètre X / Y / Z sur C2:9 / C2:10 / C2:11 (option `Acceleration`).

## 9.6 ID-tags et adresses

| Module | v2 | Ancienne valeur à corriger à la migration |
|---|---|---|
| MC42 | ID-tag **0** dans la v2 MC42-MD4, **1** dans la v2 MC42-MD3 | 1 sur les Commuter V25 seulement ; la lignée B (V35, V65, V69) garde 1 (D39) |
| MD4-5 | adresse 1 | — |
| MD4-10 | adresse 2 | 0 sur V25 |
| MD3 | adresse 0 (type différent du MC42, pas de conflit) | — |
| MC2 | inchangé (projet MC2) | — |

## 9.7 Questions ouvertes sur le câblage

| # | Question | Pourquoi elle compte |
|---|---|---|
| F1 | Sens physique de la pompe sur C1:14 (droite selon le plan, gauche selon la 108.3.1) | réglé par `T Pump wiring` et contrôle à quai, mais le plan devrait être corrigé une fois tranché |
| F2 | Joysticks électriques X100 : bateaux câblés selon #28580 IND H (24 = gauche, 36 = droit) encore en service ? | inversion compensée par l'étalonnage ou non |
| F3 | C1:38 : capteur de tension du gonflage 24 V ou capteur de courant (plan IND N) ? | même broche, deux usages |
| F4 | Commuter : le tendeur est-il en PWM (V25) sur tous les Commuter, ou seulement les premiers ? | valeur par défaut de `Cab track tension` à la migration |
| F5 | Écran des Kreisel Original #020, #024, #032 : MD3 ou MD4-10 ? | configuration à la migration |

## 9.8 Vers un matériel simplifié et standardisé (bateaux futurs, D37)

Les §9.1 à 9.7 décrivent le câblage **existant**, que la v2 pilote et continuera de piloter. En parallèle, le projet proposera un câblage **neuf**, plus simple, pour les bateaux futurs (et éventuellement des refits volontaires). Un câblage neuf s'ajoute dans `10 IO` comme une configuration de plus ; il ne retire jamais le support d'un faisceau existant. Pistes à instruire, qui donneront des propositions de schémas :

- **Un seul brochage MC42 pour tous les modèles** : aujourd'hui C1:24, 25, 26, 36, 44, 47/60, 52 changent de rôle entre X100 thermique, X100 électrique et Commuter.
- **Moins de keyboxes et de fusebox** : les relais K1 à K13 de la keybox X100 changent de sens selon la propulsion ; les Commuter ont trois keyboxes (KTB, KBB, KTC) et plusieurs fusebox FBA selon le variateur. Étudier une distribution de puissance unique par modèle (module de puissance CAN à sorties protégées, ou sorties directes du MC42 et d'un module d'extension IQAN), identique en électrique et en thermique pour tout ce qui n'est pas la propulsion.
- **Faisceaux modulaires** : un faisceau de base commun (MC42, écran, bloc hydraulique, CAN) et un faisceau par propulsion (moteur thermique, ou batterie et variateurs), avec des connecteurs identiques.
- **Bus CAN normalisés** : un bus par usage (propulsion, énergie, confort, écrans), mêmes vitesses sur tous les modèles ; fin du port B partagé.
- **Écran** : câblage prévu pour le MD5 (CAN, Ethernet), emplacement unique des joysticks.

Chaque proposition sera chiffrée (nombre de boîtiers, de références de faisceau, de broches) et comparée à l'existant, puis notée dans `DECISIONS.md`.
