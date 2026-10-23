# Interfaces matérielles et CAN — v117

Généré par `tools/reports.py`. Les identifiants viennent de l'export texte ; le bus et le module sont ceux déclarés sur chaque canal.

## Modules

- **MD3[0]** (MD3 module)
- **MC42** (MC42 module)
- **Inboard Engine EB2** (J1939 module)
- **Radio** (Generic module)
- **G1x** (G1x module)
- **KeyBox** (Generic module)
- **Garmin** (Generic module)
- **Proemion** (Generic module)
- **Inboard Engine Ford** (J1939 module)

## Bus CAN déclarés

- **Diagnostics** (Diagnostics bus) J1939 start address=128
- **J1939** (J1939 bus) Speed=250 · Address claim=No
- **Master** (Master bus) 
- **iPhone** (Generic bus) Speed=125 · Identifier size=Standard (11 bits)
- **Drive** (Generic bus) Speed=Can Speed [kbps] · Identifier size=Standard (11 bits)
- **Garmin** (Generic bus) Speed=250 · Identifier size=Extended (29 bits)
- **Drive** (Generic bus) Speed=Can Speed [kbps] · Identifier size=Extended (29 bits)

## Entrées / sorties physiques

| Appli | Groupe | Canal | Type | Module | Index | Entrée / source |
|---|---|---|---|---|---|---|
| MC42 | Thermic / Engine i/o / EB2 | Malfunction lamp EB2 | MDGN | Inboard Engine EB2 (J1939[0]) | 1 |  |
| MC42 | Thermic / Engine i/o / EB2 | Red stop lamp EB2 | MDGN | Inboard Engine EB2 (J1939[0]) | 2 |  |
| MC42 | Thermic / Engine i/o / EB2 | Amber warning lamp EB2 | MDGN | Inboard Engine EB2 (J1939[0]) | 3 |  |
| MC42 | Thermic / Engine i/o / EB2 | Protect lamp EB2 | MDGN | Inboard Engine EB2 (J1939[0]) | 4 |  |
| MC42 | Thermic / Engine i/o / Ford | Malfunction lamp Ford | MDGN | Inboard Engine Ford (J1939[0]) | 1 |  |
| MC42 | Thermic / Engine i/o / Ford | Red stop lamp Ford | MDGN | Inboard Engine Ford (J1939[0]) | 2 |  |
| MC42 | Thermic / Engine i/o / Ford | Amber warning lamp Ford | MDGN | Inboard Engine Ford (J1939[0]) | 3 |  |
| MC42 | Thermic / Engine i/o / Ford | Protect lamp Ford | MDGN | Inboard Engine Ford (J1939[0]) | 4 |  |
| MC42 | Track tension |  | VIN | MC42 (MC42[1]) | 0 |  |
| MC42 | (racine) | Status:MC42[1] | MDGN | MC42 (MC42[1]) | 0 |  |
| MC42 | Thermic / Pump | Pump 1 Right | COUT | MC42 (MC42[1]) | 0 | Pump 1 Right Filter ECC1 [%] |
| MC42 | Track Up/Down | Locking pressure | VIN | MC42 (MC42[1]) | 1 |  |
| MC42 | Thermic / Pump | Pump 2 Left | COUT | MC42 (MC42[1]) | 1 | Pump 2 Left Filter ECC1 [%] |
| MC42 | (racine) | S/N:MC42[1] | MDGN | MC42 (MC42[1]) | 1 |  |
| MC42 | Track tension | Track pressure | VIN | MC42 (MC42[1]) | 2 |  |
| MC42 | (racine) | Temp:MC42[1] | MDGN | MC42 (MC42[1]) | 2 |  |
| MC42 | (racine) | Address:MC42[1] | MDGN | MC42 (MC42[1]) | 3 |  |
| MC42 | Thermic / Oil security | Oil Temps | VIN | MC42 (MC42[1]) | 4 |  |
| MC42 | (racine) | 12V Batt. | MDGN | MC42 (MC42[1]) | 4 |  |
| MC42 | Thermic / Oil security | Hydraulic pump statut | VIN | MC42 (MC42[1]) | 5 |  |
| MC42 | (racine) | VREF-A:MC42[1] | MDGN | MC42 (MC42[1]) | 5 |  |
| MC42 | Thermic / T.Exhaust temp | T Exhaust coolant temp mc 52 | VIN | MC42 (MC42[1]) | 7 |  |
| MC42 | Track Up/Down | EV By pass | DOUT | MC42 (MC42[1]) | 8 | Inter EV By Pass |
| MC42 | Track Up/Down | EV Up | DOUT | MC42 (MC42[1]) | 9 | Inter EV UP |
| MC42 | Track Up/Down | EV Down | DOUT | MC42 (MC42[1]) | 10 | Inter EV DOWN |
| MC42 | Track Up/Down | EV Tension | DOUT | MC42 (MC42[1]) | 11 | Inter Tension |
| MC42 | Track Up/Down | EV Unlock | DOUT | MC42 (MC42[1]) | 12 | Inter Unlock |
| MC42 | Track Up/Down | EV Lock | DOUT | MC42 (MC42[1]) | 13 | Inter Lock landing |
| MC42 | (racine) | Pin 44 (Brake) | DOUT | MC42 (MC42[1]) | 14 | PIN 44 |
| MD3 | BackLight | Time | SIC |  |  |  |
| MD3 | (racine) | Left Joystick | VIN | MD3[0] | 0 |  |
| MD3 | BUZZER | Buzzer | DOUT | MD3[0] | 0 | Inter Buzzer |
| MD3 | Link MD3 | MDGN-Status:MD3[0] | MDGN | MD3[0] | 0 |  |
| MD3 | (racine) | Right Joystick | VIN | MD3[0] | 1 |  |
| MD3 | RADIO | MDGN-S/N:MD3[0] | MDGN | MD3[0] | 1 |  |
| MD3 | (racine) | MDGN-Temp:MD3-0 | MDGN | MD3[0] | 2 |  |
| MD3 | (racine) | MDGN-+BAT:MD3-0 | MDGN | MD3[0] | 3 |  |
| MD3 | (racine) | MDGN-VREF:MD3-0 | MDGN | MD3[0] | 4 |  |

## Trames CAN

| Appli | Groupe | Trame | Sens | Module | Identifiant | Période / timeout | Contenu |
|---|---|---|---|---|---|---|---|
| MC42 | Thermic / Engine i/o / EB2 | SPN 629 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 100 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 110 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 105 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 175 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 102 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 1485 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 637 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 656 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 636 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 626 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 677 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 655 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 654 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 653 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 652 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 651 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 639 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 98 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | SPN 106 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | Driver's demand, engine % EB2 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | Actual engine, % torque EB2 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | Engine speed EB2 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | Accelerator pedal position EB2 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 | % load at current speed EB2 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 |  | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / EB2 |  | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 629 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 100 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 110 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 105 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 175 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 102 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 1485 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 637 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 656 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 636 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 626 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 677 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 655 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 654 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 653 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 652 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 651 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 639 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 98 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | SPN 106 | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | Driver's demand, engine %, Ford | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | Actual engine, % torque, Ford | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | Engine speed Ford | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | Accelerator pedal position Ford | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford | % load at current speed Ford | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford |  | reçue |  |  |  |  |
| MC42 | Thermic / Engine i/o / Ford |  | reçue |  |  |  |  |
| MD3 | BackLight | 129025-0 | reçue | Garmin (Generic) | PGN-129025 | 1000 | Latitude G, Longitude G |
| MD3 | BackLight | 129026-0 | reçue | Garmin (Generic) | PGN-129026 | 1000 | Speed_Over_Ground_Raw |
| MD3 | BackLight | 129029-0 | reçue | Garmin (Generic) | PGN-129029 | 1000 | Current Date J, Time_Byte_1_2_J, Time_Byte_3 |
| MD3 | BackLight | 129029-1 | reçue | Garmin (Generic) | PGN-129029 | 1000 | Time_Byte_4 |
| MC42 | Thermic / Engine i/o / EB2 | DM1 | reçue | Inboard Engine EB2 (J1939[0]) |  |  | SPN 98 |
| MC42 | Thermic / Engine i/o / EB2 | TSC1-A:J1939-0 EB2 | émise | Inboard Engine EB2 (J1939[0]) |  | 20 |  |
| MC42 | Thermic / Engine i/o / EB2 | EEC1 EB2 | reçue | Inboard Engine EB2 (J1939[0]) | 61444 | 3000 | Driver's demand, engine % EB2 [%], Actual engine, % torque EB2 [%], Engine speed EB2 [rpm] |
| MC42 | Thermic / Engine i/o / EB2 | EEC2 EB2 | reçue | Inboard Engine EB2 (J1939[0]) | 61443 | 3000 | Accelerator pedal position EB2 [%], % load at current speed EB2 [%] |
| MC42 | Thermic / Engine i/o / EB2 | Engine Temperature EB 2 | reçue | Inboard Engine EB2 (J1939[0]) | 65262 | Not used | Engine coolant temperature EB2 [°C] |
| MC42 | Thermic / Engine i/o / EB2 | Engine fluid level/pressure 1 EB2 | reçue | Inboard Engine EB2 (J1939[0]) | 65263 | 2000 | Engine oil pressure EB2 [kPa] |
| MC42 | Thermic / Engine i/o / Ford | DM1 | reçue | Inboard Engine Ford (J1939[0]) |  |  | SPN 98 |
| MC42 | Thermic / Engine i/o / Ford | TSC1-A:J1939-0 Ford | émise | Inboard Engine Ford (J1939[0]) |  | 20 |  |
| MC42 | Thermic / Engine i/o / Ford | EEC1 Ford | reçue | Inboard Engine Ford (J1939[0]) | 61444 | 2000 | Driver's demand, engine %, Ford [%], Actual engine, % torque, Ford [%], Engine speed Ford [rpm] |
| MC42 | Thermic / Engine i/o / Ford | EEC2 Ford | reçue | Inboard Engine Ford (J1939[0]) | 61443 | 2000 | Accelerator pedal position Ford [%], % load at current speed Ford [%] |
| MC42 | Thermic / Engine i/o / Ford | Engine Temperature Ford | reçue | Inboard Engine Ford (J1939[0]) | 65262 | Not used | Engine coolant temperature Ford [°C] |
| MC42 | Thermic / Engine i/o / Ford | Engine fluid level/pressure 1 Ford | reçue | Inboard Engine Ford (J1939[0]) | 65263 | 2000 | Engine oil pressure Ford [kPa] |
| MC42 | KeyBox | GFOUT-D:Generic | émise | KeyBox (Generic) | 0 | 1000 | Byte 0, Byte 1 |
| MC42 | KeyBox | GFOUT-E:Generic | émise | KeyBox (Generic) | 0x20C | 1000 | OFF_Bits_GOUT, ON_Bits_GOUT |
| MC42 | KeyBox | 0x70C | reçue | KeyBox (Generic) | 0x70C | 1000 |  |
| MC42 | KeyBox | GFIN-B:Generic | reçue | KeyBox (Generic) | ID Fault | 1000 | K1 Fault, K2 Fault, K3 Fault, K4 Fault, K5 Fault, K6 Fault, K7 Fault, K8 Fault, K9 Fault, K10 Fault, K11 Fault, K12 Faul |
| MC42 | KeyBox | GFOUT-D:Generic | émise | KeyBox (Generic) | ID Prog | Not used | BYTE 0 - HB, BYTE 1 - HB, BYTE 2 - HB, BYTE 4 - HB, BYTE 5 - HB |
| MC42 | KeyBox | GFOUT-E:Generic | émise | KeyBox (Generic) | ID Prog | Not used | BYTE 0 - HB, BYTE 1 - HB, BYTE 2 - HB, BYTE 4 - HB |
| MC42 | Proemion | GFIN-A:Generic | reçue | Proemion (Generic) | 0x7451220 | 2000 | Network State, Signal Quality |
| MC42 | Proemion | Proemion Device | émise | Proemion (Generic) | 0x7451230 | Not used | 3 [cV] |
| MD3 | RADIO | CAN IN 100 | reçue | Radio (Generic) | 0x100 | 1000 | RadioGauche, RadioDroit, RadioStop, RadioStart, RadioSpeed |
| MD3 | RADIO | CAN IN 101 | reçue | Radio (Generic) | 0x101 | 1000 | TimelapsIn [ms] |
| MD3 | RADIO | CANOUT 102 | émise | Radio (Generic) | 0x102 | 100 | TimeLapsOut [ms], Run Engine Statut |

## Liaisons entre applications (APPOUT → APPIN)

- MC42 `OK UP/DOWN` (← `OK UP/DOWN`) → MD3 `OK UP/DOWN Input`
- MC42 `Wait_Very_Low_Oil_Level` (← `Wait_Very_Low_Oil_Level`) → MD3 `Oil level Very Low Input`
- MC42 `System Started` (← `System Started DELAYS`) → MD3 `ENGINE RUN Input`
- MD3 `Speed Input` (← `Speed State`) → MC42 `Speed Input`
- MD3 `UP/DOWN Button` (← `UP/DOWN Button`) → MC42 `UP/DOWN Button Input`
- MD3 `State Up/Down` (← `State Up/Down`) → MC42 `State Up/Down`
- MD3 `IDC Speed Free` (← `IDC Speed Free`) → MC42 `Free Input`
- MD3 `Manip Gauche CanOut` (← `Math Gauche [%]`) → MC42 `Left CanIn`
- MD3 `Manip Droit CanOut` (← `Math Droit [%]`) → MC42 `Right CanIn`
- MD3 `Can Out Button F1` (← `F1 - START PAGE`) → MC42 `MD3_Start/Stop`