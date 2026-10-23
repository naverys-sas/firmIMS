# Interfaces matérielles et CAN — v117

Généré par `tools/reports.py`. Les identifiants viennent de l'export texte ; le bus et le module sont ceux déclarés sur chaque canal.

## Modules

- **MC42-33** (MC42 module)
- **MD4-CAB-40** (MD4-10 module)
- **MD45-ET-39** (MD4-5 module)
- **Charger Brusa** (Generic module)
- **Sev_M_Track** (Generic module)
- **Sev_M3_HVLP_soon** (Generic module)
- **G1x** (G1x module)
- **Keyboxs CAB** (Generic module)
- **Charger Elcon** (Generic module)
- **Garmin CAB** (Generic module)
- **Batt BMW** (Generic module)
- **Charger BMW** (Generic module)
- **Zapi_M_Track** (Generic module)
- **Batt_Novum** (Generic module)
- **Outboards** (Generic module)
- **Keybox X100 E** (Generic module)
- **EB2 T45** (J1939 module)
- **Ford T45** (J1939 module)
- **Keybox X100 T** (Generic module)
- **Inverter_HVLP_j19** (J1939 module)
- **tyva bender** (Generic module)
- **tyva battery** (Generic module)
- **Kubota WG16** (J1939 module)
- **Battery Kreisel** (Generic module)
- **tyva 24v a/c** (Generic module)
- **Keypad Blink marine 8 keys** (Generic module) — Keypas PKP 2400SI CAN Open (fournisseur: Blink Marine)

## Bus CAN déclarés

- **Diagnostics bus** (Diagnostics bus) J1939 start address=128
- **CanC-mc-Gen11-2** (Generic bus) Speed=Can Speed C [kbps] · Identifier size=Standard (11 bits)
- **CanB-mc-Gen11-125** (Generic bus) Speed=Can Speed B [kbps] · Identifier size=Standard (11 bits)
- **Master** (Master bus) 
- **CanC-mc-Gen29-2** (Generic bus) Speed=Can Speed C [kbps] · Identifier size=Extended (29 bits)
- **CanC-MD410-Gen29-250** (Generic bus) Speed=250 · Identifier size=Extended (29 bits)
- **CanB-mc-J1939** (J1939 bus) Speed=Can Speed B [kbps] · Address claim=No
- **Generic** (Generic bus) Speed=250 · Identifier size=Extended (29 bits)

## Entrées / sorties physiques

| Appli | Groupe | Canal | Type | Module | Index | Entrée / source |
|---|---|---|---|---|---|---|
| MC42 app | logic screen md4 / WIP/45.Maintenance / Time/Date | Date | SIC |  |  |  |
| MC42 app | logic screen md4 / WIP/45.Maintenance / Time/Date | Time | SIC |  |  |  |
| MC42 app | (racine) | Project version | SIC |  |  |  |
| MC42 app | (racine) | Date 2 | SIC |  |  |  |
| MC42 app | (racine) | Time 2 | SIC |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | Malfunction lamp EB2 T45 | MDGN | EB2 T45 (J1939[0]) | 1 |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | Red stop lamp EB2 T45 | MDGN | EB2 T45 (J1939[0]) | 2 |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | Amber warning lamp EB2 T45 | MDGN | EB2 T45 (J1939[0]) | 3 |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | Protect lamp EB2 T45 | MDGN | EB2 T45 (J1939[0]) | 4 |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | Malfunction lamp Ford T | MDGN | Ford T45 (J1939[0]) | 1 |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | Red stop lamp Ford T | MDGN | Ford T45 (J1939[0]) | 2 |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | Amber warning lamp Ford T | MDGN | Ford T45 (J1939[0]) | 3 |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | Protect lamp Ford T | MDGN | Ford T45 (J1939[0]) | 4 |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | Malfunction lamp Kubo T45 | MDGN | Kubota WG16 (J1939[0]) | 1 |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | Red stop lamp Kubo T45 | MDGN | Kubota WG16 (J1939[0]) | 2 |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | Amber warning lamp Kubo T45 | MDGN | Kubota WG16 (J1939[0]) | 3 |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | Protect lamp Kubo T45 | MDGN | Kubota WG16 (J1939[0]) | 4 |  |
| MC42 app | (racine) | Status:MC | MDGN | MC42-33 (MC42[0]) | 0 |  |
| MC42 app | mc.Thermic / T.Pump / pins thermic | T Pump 2 Left mc 14 | COUT | MC42-33 (MC42[0]) | 0 | T Pump 2 Left Filter ECC1 [%] |
| MC42 app | mc.I/O | Oil level Analog mc 8 | VIN | MC42-33 (MC42[0]) | 0 |  |
| MC42 app | logic screen c10 and KB / mc.Accesory i/o CAB | C Ladder_Sensor mc 11 | DPCNT | MC42-33 (MC42[0]) | 0 |  |
| MC42 app | feature inflate 24v | T V sensor inflate 24v | VIN32 | MC42-33 (MC42[0]) | 0 |  |
| MC42 app | mc.Thermic / T.Power | T V sensor port | VIN32 | MC42-33 (MC42[0]) | 1 |  |
| MC42 app | mc.Thermic / T.Pump / pins thermic | T Pump 1 Right mc 15 | COUT | MC42-33 (MC42[0]) | 1 | T Pump 1 Right Filter ECC1 [%] |
| MC42 app | mc.I/O | Locking pressure mc 9 | VIN | MC42-33 (MC42[0]) | 1 |  |
| MC42 app | (racine) | S/N:MC | MDGN | MC42-33 (MC42[0]) | 1 |  |
| MC42 app | mc.I/O | Track pressure mc 10 | VIN | MC42-33 (MC42[0]) | 2 |  |
| MC42 app | (racine) | Temp:MC | MDGN | MC42-33 (MC42[0]) | 2 |  |
| MC42 app | mc.Link MC42-Screens Logic ims / joystick mc42 / level sensor cab or right joy | Low water level RJoy | VIN | MC42-33 (MC42[0]) | 3 |  |
| MC42 app | (racine) | Address:MC | MDGN | MC42-33 (MC42[0]) | 3 |  |
| MC42 app | mc.I/O | mc 12V Batt | MDGN | MC42-33 (MC42[0]) | 4 |  |
| MC42 app | mc.I/O / Oil Temps mc 25 or Current bilge C | T Oil Temps mc 25/Current bilge C | VIN | MC42-33 (MC42[0]) | 4 |  |
| MC42 app | (racine) | Supply v mc42 | MDGN | MC42-33 (MC42[0]) | 4 |  |
| MC42 app | mc.Thermic / T.Oil security / pins oil | T Hydraulic pump statut mc 26 | VIN | MC42-33 (MC42[0]) | 5 |  |
| MC42 app | (racine) | VREF A:MC | MDGN | MC42-33 (MC42[0]) | 5 |  |
| MC42 app | mc.Link MC42-Screens Logic ims / joystick mc42 / left joystick x100 / left joystick x100 | Left Joystick mc 36 | VIN | MC42-33 (MC42[0]) | 6 |  |
| MC42 app | logic screen c10 and KB / mc.Accesory i/o CAB / electronic seat | C UP/DOWN mc 45 | PWM | MC42-33 (MC42[0]) | 6 | Seat UP/DOWN [%] |
| MC42 app | mc.Thermic / T.Exhaust temp | T Exhaust coolant temp mc 52 | VIN | MC42-33 (MC42[0]) | 7 |  |
| MC42 app | mc.I/O | EV By pass mc 41 | DOUT | MC42-33 (MC42[0]) | 8 | EV By pass Sel |
| MC42 app | mc.I/O | EV Up mc 57 | DOUT | MC42-33 (MC42[0]) | 9 | EV Up Sel |
| MC42 app | logic screen c10 and KB / mc.Accesory i/o CAB / electronic seat | C FRONT BACK mc 48 | PWM | MC42-33 (MC42[0]) | 9 | Seat Front Back [%] |
| MC42 app | mc.I/O | EV Down mc 42 | DOUT | MC42-33 (MC42[0]) | 10 | EV Down Sel |
| MC42 app | mc.I/O | EV Tension mc 58 | DOUT | MC42-33 (MC42[0]) | 11 | EV Tension Sel |
| MC42 app | mc.I/O | EV unlock mc 43 | DOUT | MC42-33 (MC42[0]) | 12 | EV UnBlock Sel |
| MC42 app | logic screen c10 and KB / mc.Accesory i/o CAB | C REMOTE LD DOWN mc 28 | DIN | MC42-33 (MC42[0]) | 12 |  |
| MC42 app | mc.I/O | EV lock mc 59 | DOUT | MC42-33 (MC42[0]) | 13 | EV Lock Sel |
| MC42 app | logic screen c10 and KB / mc.Accesory i/o CAB | C REMOTE LD UP mc 29 | DIN | MC42-33 (MC42[0]) | 13 |  |
| MC42 app | mc.I/O | Brake T/ Batt HT reset OR tyva on mc 44 / Var Power C | DOUT | MC42-33 (MC42[0]) | 14 | sel batt reset/batt on or brake |
| MC42 app | mc.I/O / Power Vars E mc 60/ Batt reset C | Power Vars E mc 60/ Batt reset C | DOUT | MC42-33 (MC42[0]) | 15 | sel var power |
| MD4-CAB app | (racine) | cProject version | SIC |  |  |  |
| MD4-CAB app | (racine) | Active display page C | SIC |  |  |  |
| MD4-CAB app | (racine) | MDGN-Status:MD4 C | MDGN | MD4-CAB-40 (MD4-10[2]) | 0 |  |
| MD4-CAB app | (racine) | ETC Buzzer C41 C2:3 | DOUT | MD4-CAB-40 (MD4-10[2]) | 0 | Inter Buzzer CAB |
| MD4-CAB app | joystick md410 | Left Joystick C41 C2:1 | VIN | MD4-CAB-40 (MD4-10[2]) | 0 |  |
| MD4-CAB app | joystick md410 | Right Joystick C41 C2:2 | VIN | MD4-CAB-40 (MD4-10[2]) | 1 |  |
| MD4-CAB app | (racine) | C Button Cabine C41 C2:6 | DIN | MD4-CAB-40 (MD4-10[2]) | 3 |  |
| MD4-CAB app | (racine) | +BAT:MD4-10 | MDGN | MD4-CAB-40 (MD4-10[2]) | 4 |  |
| MD4-CAB app | (racine) | C Button Door C41 C2:7 | DIN | MD4-CAB-40 (MD4-10[2]) | 4 |  |
| MD45-ET app | (racine) | Active display page MD45 | SIC |  |  |  |
| MD45-ET app | (racine) | 45Project version | SIC |  |  |  |
| MD45-ET app | (racine) | MD4-Status:MD45 | MDGN | MD45-ET-39 (MD4-5[1]) | 0 |  |
| MD45-ET app | (racine) | Buzzer ET45 C2:3 | DOUT | MD45-ET-39 (MD4-5[1]) | 0 | Be1 Inter Buzzer for 45 |
| MD45-ET app | Water level V10 motor | Left Joy ET45 ou water level C2:1 | VIN | MD45-ET-39 (MD4-5[1]) | 0 |  |
| MD45-ET app | Joystick md45 | Right Joystick ET45 C2:2 | VIN | MD45-ET-39 (MD4-5[1]) | 1 |  |
| MD45-ET app | (racine) | +BAT:MD45 | MDGN | MD45-ET-39 (MD4-5[1]) | 4 |  |

## Trames CAN

| Appli | Groupe | Trame | Sens | Module | Identifiant | Période / timeout | Contenu |
|---|---|---|---|---|---|---|---|
| MC42 app | mc.Electric / E.CHARGER / E.Charger_Brusa | 1560 - POWER ON - Byte | émise |  |  |  |  |
| MC42 app | mc.Electric / E.CHARGER / E.Charger_Brusa | 1560 - Cycle Value - Byte | émise |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | Status Word | reçue |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | Limit Word | reçue |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | Motor_Speed_Raw | reçue |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | Input Voltage | reçue |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | Torque_Mesured_Raw | reçue |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | M3 (Pump) - Error | reçue |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | Status Word o250 | émise |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | Torque Demande o250 | émise |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | Torque Limit o250 | émise |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | Fw Speed Limit | émise |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | Rw Speed Limit | émise |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | I Batt Discharge Limit | émise |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | I Batt recharge limit | émise |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | Status Word o | émise |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | Torque Demande o | émise |  |  |  |  |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | Torque Limit o | émise |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 629 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 100 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 110 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 105 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 175 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 102 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 1485 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 637 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 656 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 636 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 626 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 677 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 655 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 654 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 653 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 652 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 651 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 639 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 98 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | SPN 106 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | Driver's demand, engine % EB2 T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | Actual engine, % torque EB2 T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | Engine speed EB2 T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | Accelerator pedal position EB2 T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | % load at current speed EB2 T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | Engine coolant temperature EB2 T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | Engine oil pressure EB2 T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 629 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 100 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 110 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 105 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 175 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 102 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 1485 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 637 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 656 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 636 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 626 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 677 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 655 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 654 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 653 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 652 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 651 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 639 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 98 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | SPN 106 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | Driver's demand, engine %, Ford T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | Actual engine, % torque, Ford T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | Engine speed Ford T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | Accelerator pedal position Ford T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | % load at current speed Ford T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | Engine coolant temperature Ford T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | Engine oil pressure Ford T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 629 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 100 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 110 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 105 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 175 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 102 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 1485 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 637 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 656 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 636 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 626 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 677 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 655 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 654 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 653 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 652 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 651 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 639 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 98 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | SPN 106 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | Driver's demand, engine % Kubo T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | Actual engine, % torque Kubo T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | Engine speed Kubo T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | Accelerator pedal position Kubo T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | % load at current speed Kubo T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | Engine coolant temperature Kubo T45 | reçue |  |  |  |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | Engine oil pressure Kubo T45 | reçue |  |  |  |  |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | NMT | émise | Batt BMW (Generic) | 0 | 500 | ID, State |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | Bat51TPdo1 | reçue | Batt BMW (Generic) | 0x1D1 | 200 | BatState, BatStateOfCharge bmw, BatCurrent, BatPackVoltage bmw, BatBusVoltage utrac bmw |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | Iso52MonRPdo1 | émise | Batt BMW (Generic) | 0x252 | 100 | IsoMonCommand, IsoMonWarningLevel, IsoMonErrorLevel |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | Bat51TPdo2 | reçue | Batt BMW (Generic) | 0x2D1 | 5000 | BatAvgTemp, BatMinCellTemp, BatMaxCellTemp bmw, BatBalancingState, BatTimeToFullMinute |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | Bat51TPdo3 | reçue | Batt BMW (Generic) | 0x3D1 | 2000 | BatPowerLimitChargeRaw, BatPowerLimitDischargeRaw, BatEnergyRemainingRaw |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | Dcu50Heartbeat | reçue | Batt BMW (Generic) | 0x750 | 2000 | DcuNodeState |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | Bat51Hartbeat | reçue | Batt BMW (Generic) | 0x751 | 2000 | BatNodeState |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | Sync | émise | Batt BMW (Generic) | 0x80 | 20 | SyncCounter |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | Bat51Error | reçue | Batt BMW (Generic) | 0xD1 | Not used | BatErrorCode, BatError |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | Iso52MonHeartbeat | reçue | Batt BMW (Generic) | 1874 | 2000 | IsoMonNodeState |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | Dcu50Error | reçue | Batt BMW (Generic) | 208 | Not used | DcuErrorCode, DcuError |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | Iso52MonError | reçue | Batt BMW (Generic) | 210 | Not used | IsoMonErrorCode, IsoMonError |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | Iso52MonTPdo1 | reçue | Batt BMW (Generic) | 466 | 2000 | IsoMonResistance BMW, IsoMonVoltage, IsoMonState |
| MC42 app | mc.Electric / E.BATTERY / E.BMW | Bat51RPdo1 | émise | Batt BMW (Generic) | 593 | 100 | BatCommand, BatCoolingPolicy |
| MC42 app | mc.Electric / E.BATTERY / E.NovumTech | BMS_Debug_CellVotage | émise | Batt_Novum (Generic) | 0x220B16B | Not used | TrigCellVoltageFrame1, TrigCellVoltageFrame2, TrigCellVoltageFrame3, TrigCellVoltageFrame4 |
| MC42 app | mc.Electric / E.BATTERY / E.NovumTech | BMS_NTHT_Req | émise | Batt_Novum (Generic) | 35697002 | 100 | BMSModeRequest |
| MC42 app | mc.Electric / E.BATTERY / E.NovumTech | BMS_NTHT_Errors novum | reçue | Batt_Novum (Generic) | 35697008 | 250 | ConfigFail, SoftFailure, SoftConsistencyError, InterlockCut, DCPowerDisconnection, WarningOverChargeCurrent, WarningOver |
| MC42 app | mc.Electric / E.BATTERY / E.NovumTech | BMS_NTHT_G1_Info | reçue | Batt_Novum (Generic) | 35697009 | Not used | BmsMode, SOC novum [%], SOH [%], SOE [%], ModulesCom, InsulationState |
| MC42 app | mc.Electric / E.BATTERY / E.NovumTech | BMS_NTHT_G2_Voltage | reçue | Batt_Novum (Generic) | 35697010 | Not used | BatteryVoltage novum [V], MinCellVolt [mV], MaxCellVolt [mV], MaxBatteryVoltage [V] |
| MC42 app | mc.Electric / E.BATTERY / E.NovumTech | BMS_NTHT_G3_Current | reçue | Batt_Novum (Generic) | 35697011 | Not used | BatteryCurrent [A], MaxDischargeCurrent [A], MaxChargeCurrent [A] |
| MC42 app | mc.Electric / E.BATTERY / E.NovumTech | BMS_NTHT_G4_Temperature | reçue | Batt_Novum (Generic) | 35697012 | Not used | MinTemp [°C], MaxTemp novum [°C], AverageTemp [°C] |
| MC42 app | mc.Electric / E.BATTERY / E.NovumTech | BMS_NTHT_G5_Charger | reçue | Batt_Novum (Generic) | 35697013 | Not used | ChargeCurrentCmd [A], ChargeVoltageCmd [V] |
| MC42 app | mc.Electric / E.BATTERY / E.Kresel | 2047 EXT_FuncRequest | émise | Battery Kreisel (Generic) | 2047 | 100 | Func_MSW_Request_Master, Func_sys_state_req, Func_iso_measurement |
| MC42 app | mc.Electric / E.BATTERY / E.Kresel | 257 mBMS_FuncSTAT | reçue | Battery Kreisel (Generic) | 257 | 2000 | BMS_start_up_ready, BMS_stay_alive, BMS_iso_meas_act, BMS_balancing_act, BMS_reset_denied, BMS_wakeup_active, BMS_Master |
| MC42 app | mc.Electric / E.BATTERY / E.Kresel | 258 mBMS_ROE | reçue | Battery Kreisel (Generic) | 258 | 100 | EVT_ErrNr_SC, EVT_Context, mBMS_ROE_Mux M |
| MC42 app | mc.Electric / E.BATTERY / E.Kresel | 276 mBMS_Trac_Info | reçue | Battery Kreisel (Generic) | 276 | 2000 | BMS_Iso_Resist, BMS_U_Trac [dV] |
| MC42 app | mc.Electric / E.BATTERY / E.Kresel | 277 mBMS_Temp_Info | reçue | Battery Kreisel (Generic) | 277 | 2000 | BMS_ext_Temp_Inlet, BMS_ext_Temp_Outlet |
| MC42 app | mc.Electric / E.BATTERY / E.Kresel | 304 mBMS_Version_1 | reçue | Battery Kreisel (Generic) | 304 | 2000 | VER_CSC_release, VER_CSC_minor, VER_CSC_major, VER_MC_release, VER_MC_minor, VER_MC_major, VER_MC_DS_CRC |
| MC42 app | mc.Electric / E.BATTERY / E.Kresel | 305 mBMS_Version_2 | reçue | Battery Kreisel (Generic) | 305 | 2000 | VER_CSC_release, VER_CSC_minor, VER_CSC_major, VER_MC_release, VER_MC_minor, VER_MC_major, VER_MC_DS_CRC |
| MC42 app | mc.Electric / E.BATTERY / E.Kresel | 912 mBMS_Bat_Info_Master | reçue | Battery Kreisel (Generic) | 912 | 2000 | BMS_SOC_Master, BMS_I_Batt_Maste [A], BMS_U_Batt_Master |
| MC42 app | mc.Electric / E.BATTERY / E.Kresel | 913 mBMS_Cell_Info_Master | reçue | Battery Kreisel (Generic) | 913 | 2000 | U_Cell_min_Master, U_Cell_max_Master, U_Cell_avg_Master, Cell_T_max_Master, Cell_T_min_Master |
| MC42 app | mc.Electric / E.CHARGER / E.Charger_BMW | GFOUT-A:Generic | émise | Charger BMW (Generic) | 0x400 | 200 | ENABLE, POWER_REFERENCE, MAXDCVOLTLIMIT, MAXDCCURRLIMIT |
| MC42 app | mc.Electric / E.CHARGER / E.Charger_BMW | GFIN-A:Generic | reçue | Charger BMW (Generic) | 0x405 | 200 | CHARGER_STATUS, CHARGER_MAINS_CURRENT, CHARGER_DC_CURRENT, CHARGER_DC_VOLTAGE, CHARGER_MAINS_FREQUENCY |
| MC42 app | mc.Electric / E.CHARGER / E.Charger_Brusa | 1552 - CAN IN | reçue | Charger Brusa (Generic) | 1552 | 1000 | 1552 - Hardware enable - Byte, 1552 - Error detect - Byte, 1552 - Warning Condition - Byte, 1552 - Automatique charging  |
| MC42 app | mc.Electric / E.CHARGER / E.Charger_Brusa | 1553 - CAN IN | reçue | Charger Brusa (Generic) | 1553 | 1000 | 1553 - Actual mains current - Byte, 1553 - Actual mains voltage - Byte, 1553 - Actual battery output voltage - Byte, 155 |
| MC42 app | mc.Electric / E.CHARGER / E.Charger_Brusa | 1555 - CAN IN | reçue | Charger Brusa (Generic) | 1555 | 1000 | 1555 - Power stage temperature - Byte |
| MC42 app | mc.Electric / E.CHARGER / E.Charger_Brusa | 1560 - Cmd | émise | Charger Brusa (Generic) | 1560 | 100 | 1560 - POWER ON - Byte [bits], 1560 - Cycle Value - Byte [bits], 1560 - Max Current from 230 V - Byte, 1560 - Desired Vo |
| MC42 app | mc.Electric / E.CHARGER / E.Charger_Elcon | ELCON-OUT | émise | Charger Elcon (Generic) | 0x1806E5F4 | 500 | Max Voltage, Max Curent [A], Char |
| MC42 app | mc.Electric / E.CHARGER / E.Charger_Elcon | ELCON-IN | reçue | Charger Elcon (Generic) | 0x18FF50E5 | 1000 | Output Voltage, Output Current, Hardware Failure, Temperature od charger, Input Voltage, Stating State, Communication St |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | DM1 EB2 T45 | reçue | EB2 T45 (J1939[0]) |  |  | SPN 98 |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | TSC1-A:J1939-0 EB2 T45 | émise | EB2 T45 (J1939[0]) |  | 20 |  |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | EEC1 EB2 T45 | reçue | EB2 T45 (J1939[0]) | 61444 | 3000 | Driver's demand, engine % EB2 T45 [%], Actual engine, % torque EB2 T45 [%], Engine speed EB2 T45 [rpm] |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | EEC2 EB2 T45 | reçue | EB2 T45 (J1939[0]) | 61443 | 3000 | Accelerator pedal position EB2 T45 [%], % load at current speed EB2 T45 [%] |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | Engine Temperature EB 2 | reçue | EB2 T45 (J1939[0]) | 65262 | Not used | Engine coolant temperature EB2 T45 [°C] |
| MC42 app | mc.Thermic / T.Engine i/o / EB2 T45 | Engine fluid level/pressure 1 EB2 | reçue | EB2 T45 (J1939[0]) | 65263 | 2000 | Engine oil pressure EB2 T45 [kPa] |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | DM1 Ford T45 | reçue | Ford T45 (J1939[0]) |  |  | SPN 98 |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | TSC1-A:J1939-0 Ford T45 | émise | Ford T45 (J1939[0]) |  | 20 |  |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | EEC1 Ford T45 | reçue | Ford T45 (J1939[0]) | 61444 | 2000 | Driver's demand, engine %, Ford T45 [%], Actual engine, % torque, Ford T45 [%], Engine speed Ford T45 [rpm] |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | EEC2 Ford T45 | reçue | Ford T45 (J1939[0]) | 61443 | 2000 | Accelerator pedal position Ford T45 [%], % load at current speed Ford T45 [%] |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | Engine Temperature Ford T45 | reçue | Ford T45 (J1939[0]) | 65262 | Not used | Engine coolant temperature Ford T45 [°C] |
| MC42 app | mc.Thermic / T.Engine i/o / Ford T45 | Engine fluid level/pressure 1 Ford T45 | reçue | Ford T45 (J1939[0]) | 65263 | 2000 | Engine oil pressure Ford T45 [kPa] |
| MD4-CAB app | c5.NMEA / GPS | 129026-0 | reçue | Garmin CAB (Generic) | PGN-129026 | 1000 | Speed Over Ground Raw |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | JFIN-A:J1939[113] | reçue | Inverter_HVLP_j19 (J1939[113]) | 71936 | 500 | Status Word, Limit Word |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | JFIN-B:J1939[113] | reçue | Inverter_HVLP_j19 (J1939[113]) | 71680 | 500 | Motor_Speed_Raw, Torque_Mesured_Raw |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | JFIN-C:J1939[113] | reçue | Inverter_HVLP_j19 (J1939[113]) | 72192 | 500 | Input Voltage, insideHeatsink [°C], Sevcon - Engine Temp [°C] |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | JFIN-D:J1939[113] | reçue | Inverter_HVLP_j19 (J1939[113]) | 72448 | 3000 | M3 (Pump) - Error |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | JFOUT-A:J1939[250] | émise | Inverter_HVLP_j19 (J1939[113]) | 69632 | 200 | Status Word o250 [bits], Torque Demande o250 [bits], Torque Limit o250 [bits] |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | JFOUT-B:J1939[113] | émise | Inverter_HVLP_j19 (J1939[113]) | 69888 | 200 | Fw Speed Limit [bits], Rw Speed Limit [bits] |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | JFOUT-C:J1939[250] | émise | Inverter_HVLP_j19 (J1939[113]) | 70144 | 200 | I Batt Discharge Limit [bits], I Batt recharge limit [bits] |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 | JFOUT-A:J1939[113] | émise | Inverter_HVLP_j19 (J1939[113]) | 69632 | 200 | Status Word o [bits], Torque Demande o [bits], Torque Limit o [bits] |
| MC42 app | mc.Electric / E.KeyBox x100 E | GFOUT-D:Generic | émise | Keybox X100 E (Generic) | 0 | 1000 | Byte 0, Byte 1 |
| MC42 app | mc.Electric / E.KeyBox x100 E | GFOUT-E:Generic | émise | Keybox X100 E (Generic) | 0x20C | 1000 | OFF_Bits_GOUT, ON_Bits_GOUT |
| MC42 app | mc.Electric / E.KeyBox x100 E | 0x70C | reçue | Keybox X100 E (Generic) | 0x70C | 1000 |  |
| MC42 app | mc.Electric / E.KeyBox x100 E | GFIN-A:Generic | reçue | Keybox X100 E (Generic) | ID Fault | Not used | K1 Fault, K2 Fault, K3 Fault, K4 Fault, K5 Fault, K6 Fault, K7 Fault, K8 Fault, K9 Fault, K10 Fault, K11 Fault, K12 Faul |
| MC42 app | mc.Electric / E.KeyBox x100 E | GFOUT-A:Generic | émise | Keybox X100 E (Generic) | ID Prog | Not used | BYTE 0 - HB, BYTE 1 - HB, BYTE 2 - HB, BYTE 4 - HB, BYTE 5 - HB |
| MC42 app | mc.Electric / E.KeyBox x100 E | GFOUT-B:Generic | émise | Keybox X100 E (Generic) | ID Prog | Not used | BYTE 0 - HB, BYTE 1 - HB, BYTE 2 - HB, BYTE 4 - HB |
| MC42 app | mc.Thermic / T.KeyBox x100 T | GFOUT-D:Generic | émise | Keybox X100 T (Generic) | 0 | 1000 | Byte 0, Byte 1 |
| MC42 app | mc.Thermic / T.KeyBox x100 T | GFOUT-E:Generic | émise | Keybox X100 T (Generic) | 0x20C | 1000 | T OFF_Bits_GOUT, T ON_Bits_GOUT |
| MC42 app | mc.Thermic / T.KeyBox x100 T | 0x70C | reçue | Keybox X100 T (Generic) | 0x70C | 1000 |  |
| MC42 app | mc.Thermic / T.KeyBox x100 T | GFIN-A:Generic | reçue | Keybox X100 T (Generic) | ID Fault | 1000 | K1 Fault, K2 Fault, K3 Fault, K4 Fault, K5 Fault, K6 Fault, K7 Fault, K8 Fault, K9 Fault, K10 Fault, K11 Fault, K12 Faul |
| MC42 app | mc.Thermic / T.KeyBox x100 T | GFOUT-C:Generic | émise | Keybox X100 T (Generic) | ID Prog | Not used | BYTE 0 - HB, BYTE 1 - HB, BYTE 2 - HB, BYTE 4 - HB, BYTE 5 - HB |
| MC42 app | mc.Thermic / T.KeyBox x100 T | GFOUT-B:Generic | émise | Keybox X100 T (Generic) | ID Prog | Not used | BYTE 0 - HB, BYTE 1 - HB, BYTE 2 - HB, BYTE 4 - HB |
| MC42 app | logic screen c10 and KB / Keyboxs CAB | GFOUT-D:Generic | émise | Keyboxs CAB (Generic) | 0 | 1000 | Byte 0, Byte 1 |
| MC42 app | logic screen c10 and KB / Keyboxs CAB | GFOUT-E:Generic | émise | Keyboxs CAB (Generic) | 0 | 1000 | Byte 0, Byte 1 |
| MC42 app | logic screen c10 and KB / Keyboxs CAB | GFOUT-F:Generic | émise | Keyboxs CAB (Generic) | 0 | 1000 | Byte 0, Byte 1 |
| MC42 app | logic screen c10 and KB / Keyboxs CAB / Program KB CAB | New Generic frame out | émise | Keyboxs CAB (Generic) | 0 | 5000 | Byte 0, Byte 1 |
| MC42 app | logic screen c10 and KB / Keyboxs CAB | Cout ON bits KTB Gen | émise | Keyboxs CAB (Generic) | 0x217 | 1000 | OFF_Bits_GOUT 1, ON_Bits_GOUT 1 |
| MC42 app | logic screen c10 and KB / Keyboxs CAB | Cout ON bits KBB Gen | émise | Keyboxs CAB (Generic) | 0x218 | 1000 | OFF_Bits_GOUT 2, ON_Bits_GOUT 2 |
| MC42 app | logic screen c10 and KB / Keyboxs CAB | Cout ON bits KTC Gen | émise | Keyboxs CAB (Generic) | 0x219 | 1000 | OFF_Bits_GOUT 3, ON_Bits_GOUT 3 |
| MC42 app | logic screen c10 and KB / Keyboxs CAB | 0x717 | reçue | Keyboxs CAB (Generic) | 0x717 | 1000 |  |
| MC42 app | logic screen c10 and KB / Keyboxs CAB | 0x718 | reçue | Keyboxs CAB (Generic) | 0x718 | 1000 |  |
| MC42 app | logic screen c10 and KB / Keyboxs CAB | 0x719 | reçue | Keyboxs CAB (Generic) | 0x719 | 1000 |  |
| MC42 app | logic screen c10 and KB / Keyboxs CAB / Program KB CAB | Call Default | reçue | Keyboxs CAB (Generic) | Default Read ID | 1000 |  |
| MC42 app | logic screen c10 and KB / Keyboxs CAB / Program KB CAB | New Generic frame out | émise | Keyboxs CAB (Generic) | Default Write ID | Not used | BYTE 0 - New ID, BYTE 1 - New ID, BYTE 2 - New ID, BYTE 4 - New ID |
| MC42 app | logic screen c10 and KB / Keyboxs CAB / Program KB CAB | New Generic frame out | émise | Keyboxs CAB (Generic) | ID | Not used | BYTE 0 - HB, BYTE 1 - HB, BYTE 2 - HB, BYTE 4 - HB, BYTE 5 - HB |
| MC42 app | logic screen c10 and KB / Keyboxs CAB / Program KB CAB | New Generic frame out | émise | Keyboxs CAB (Generic) | ID | Not used | BYTE 0 - New ID, BYTE 1 - New ID, BYTE 2 - New ID, BYTE 4 - New ID |
| MC42 app | logic screen c10 and KB / Keyboxs CAB | GFIN-E:Generic | reçue | Keyboxs CAB (Generic) | ID Fault 0x17 KTB | Not used | K1 Fault, K2 Fault, K3 Fault, K4 Fault, K5 Fault, K6 Fault, K7 Fault, K8 Fault, K9 Fault, K10 Fault, K11 Fault, K12 Faul |
| MC42 app | logic screen c10 and KB / Keyboxs CAB | GFIN-F:Generic | reçue | Keyboxs CAB (Generic) | ID Fault 0x18 KBB | Not used | K1 Fault, K2 Fault, K3 Fault, K4 Fault, K5 Fault, K6 Fault, K7 Fault, K8 Fault, K9 Fault, K10 Fault, K11 Fault, K12 Faul |
| MC42 app | logic screen c10 and KB / Keyboxs CAB | GFIN-G:Generic | reçue | Keyboxs CAB (Generic) | ID Fault 0x19 KTC | Not used | K1 Fault, K2 Fault, K3 Fault, K4 Fault, K5 Fault, K6 Fault, K7 Fault, K8 Fault, K9 Fault, K10 Fault, K11 Fault, K12 Faul |
| MC42 app | Keypad 8 keys / Keypad CAN | keys number frame | reçue | Keypad Blink marine 8 keys (Generic) | 0x195 | Not used | keys number |
| MC42 app | Keypad 8 keys / Keypad CAN | set led ON | émise | Keypad Blink marine 8 keys (Generic) | 0x215 | Not used | Red led part 1, Red led part 2, Green led part 1, Green led part 2, Blue led part 2, Blue led part 1 |
| MC42 app | Keypad 8 keys / Keypad CAN | set led blink ON | émise | Keypad Blink marine 8 keys (Generic) | 0x315 | Not used | blue led blink part1, blue led blink part2 |
| MC42 app | Keypad 8 keys / Keypad CAN | backlight 20% activation | émise | Keypad Blink marine 8 keys (Generic) | 0x515 | Not used | backlight level 20% |
| MC42 app | Keypad 8 keys / Keypad CAN | Backlight default color | émise | Keypad Blink marine 8 keys (Generic) | 0x615 | Not used | Set device register, CAN object 2003h byte 1, CAN object 2003h byte 2, Sub index 04, Color |
| MC42 app | Keypad 8 keys / Keypad CAN | Brightness default level | émise | Keypad Blink marine 8 keys (Generic) | 0x615 | Not used | Set device register, CAN object 2003h byte 1, CAN object 2003h byte 2, Sub index 05, Brightness level |
| MC42 app | Keypad 8 keys / Keypad CAN | heartbeat | reçue | Keypad Blink marine 8 keys (Generic) | 0x715 | 2000 | Heartbeat/statut |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | DM1 Kubo T45 | reçue | Kubota WG16 (J1939[0]) |  |  | SPN 98 |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | TSC1-A:J1939-0 Kubo T45 | émise | Kubota WG16 (J1939[0]) |  | 10 |  |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | EEC1 Kubo | reçue | Kubota WG16 (J1939[0]) | 61444 | 3000 | Driver's demand, engine % Kubo T45 [%], Actual engine, % torque Kubo T45 [%], Engine speed Kubo T45 [rpm] |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | EEC2 Kubo | reçue | Kubota WG16 (J1939[0]) | 61443 | 3000 | Accelerator pedal position Kubo T45 [%], % load at current speed Kubo T45 [%] |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | Engine Temperature Kubo | reçue | Kubota WG16 (J1939[0]) | 65262 | Not used | Engine coolant temperature Kubo T45 [°C] |
| MC42 app | mc.Thermic / T.Engine i/o / Kubota WG16 | Engine fluid level/pressure 1 Kubo | reçue | Kubota WG16 (J1939[0]) | 65263 | 2000 | Engine oil pressure Kubo T45 [kPa] |
| MD4-CAB app | c5.NMEA / OutBoards nmea | 127488-Eng 1 | reçue | Outboards (Generic) | PGN-127488 | 1000 | Engine 1 - Speed - Raw, Engine 1 - Trim |
| MD4-CAB app | c5.NMEA / OutBoards nmea | 127488-Eng 2 | reçue | Outboards (Generic) | PGN-127488 | 1000 | Engine 2 - Speed - Raw, Engine 2 - Trim |
| MD4-CAB app | c5.NMEA / OutBoards nmea | 127489-0 | reçue | Outboards (Generic) | PGN-127489 | 1000 | Sequence, Page, Engine Intance, Engine oil pressure, Engine oil temp., Engine temp. Byte 0 |
| MD4-CAB app | c5.NMEA / OutBoards nmea | 127489-1 | reçue | Outboards (Generic) | PGN-127489 | 1000 | Sequence, Page, Engine temp. Byte 1, Alternator potential, Fuel rate, Total engine hours - Byte 0 |
| MD4-CAB app | c5.NMEA / OutBoards nmea | 127489-2 | reçue | Outboards (Generic) | PGN-127489 | 1000 | Total engine hours - Byte 1 |
| MD4-CAB app | c5.NMEA / OutBoards nmea | 127505-Eng 1 - Can | reçue | Outboards (Generic) | PNG-127505 | 3000 | Engine 1 - Tank - RAW |
| MD4-CAB app | c5.NMEA / OutBoards nmea | 127505-Eng 2 Page 1- Can | reçue | Outboards (Generic) | PNG-127505 | 3000 | Engine 2 Page 1 - Tank - Raw |
| MD4-CAB app | c5.NMEA / OutBoards nmea | 127505-Eng 2 Page 2- Can | reçue | Outboards (Generic) | PNG-127505 | 3000 | Engine 2 Page 2 - Tank - Raw |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / broeknE.Sevcon.M3.gen.soon | 0x191071FA | émise | Sev_M3_HVLP_soon (Generic) | 0x191071FA | 200 | Status Word, Torque Demande, Torque Limit |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / broeknE.Sevcon.M3.gen.soon | 0x191171FA | émise | Sev_M3_HVLP_soon (Generic) | 0x191171FA | 200 | Fw Speed Limit, Rw Speed Limit |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / broeknE.Sevcon.M3.gen.soon | 0x191271FA | émise | Sev_M3_HVLP_soon (Generic) | 0x191271FA | 200 | I Batt Discharge Limit, I Batt recharge limit |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / broeknE.Sevcon.M3.gen.soon | 0x1918FF71 | reçue | Sev_M3_HVLP_soon (Generic) | 0x1918FF71 | 500 | Motor_Speed_Raw [rpm], Torque_Mesured_Raw |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / broeknE.Sevcon.M3.gen.soon | 0x1919FF71 | reçue | Sev_M3_HVLP_soon (Generic) | 0x1919FF71 | 500 | Status Word, Limit Word |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / broeknE.Sevcon.M3.gen.soon | 0x191AFF71 | reçue | Sev_M3_HVLP_soon (Generic) | 0x191AFF71 | 500 | Input Voltage, genHeatsink [°C], genSevcon - Engine Temp [°C] |
| MC42 app | mc.Electric / E.MOTORS / E.M3-Hydrau / broeknE.Sevcon.M3.gen.soon | 0x191BFF71 | reçue | Sev_M3_HVLP_soon (Generic) | 0x191BFF71 | 3000 | M3 (Pump) - Error |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Sevcon.M1.M2.gen4 | 0x331 GEN4 | reçue | Sev_M_Track (Generic) | 0x331 | 1000 | Error - S.M1.Right, Statut - S.M1.Right [State] |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Sevcon.M1.M2.gen4 | 0x332 GEN4 | reçue | Sev_M_Track (Generic) | 0x332 | 1000 | Error - S.M2.Left, Statut - S.M2.Left [Status] |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Sevcon.M1.M2.gen4 | 0x341 GEN4 | reçue | Sev_M_Track (Generic) | 0x341 | 1000 | Motor Speed - S.M1.Right [rpm], Actual Current - S.M1.Right [A], Torque - S.M1.Right [Raw] |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Sevcon.M1.M2.gen4 | 0x342 GEN4 | reçue | Sev_M_Track (Generic) | 0x342 | 1000 | Motor Speed - S.M2.Left [rpm], Actual Current - S.M2.Left [A], Torque actual - S.M2.Left [Raw] |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Sevcon.M1.M2.gen4 | 0x351 GEN4 | reçue | Sev_M_Track (Generic) | 0x351 | 1000 | KTY - S.M1.Right [°C], Heatsink - S.M1.Right [°C], Voltage - S.M1.Right [Raw] |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Sevcon.M1.M2.gen4 | 0x352 GEN4 | reçue | Sev_M_Track (Generic) | 0x352 | 1000 | KTY - S.M2.Left [°C], Heatsink - S.M2.Left [°C], Voltage - S.M2.Left [Raw] |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Sevcon.M1.M2.gen4 | outGEN - 4 - S.M1.Right | émise | Sev_M_Track (Generic) | 0x411 | Every cycle | Throttle Input Voltage - S.M1.Right, Fordward Switch - S.M1.Right, Inch reverse switch - S.M1.Right, FS1 Switch - S.M1.R |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Sevcon.M1.M2.gen4 | GEN - 4 - S.M2.Left | émise | Sev_M_Track (Generic) | 0x412 | Every cycle | Throttle Input Voltage - S.M2.Left, Fordward Switch - S.M2.Left, Inch reverse switch - S.M2.Left, FS1 Switch - S.M2.Left |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Sevcon.M1.M2.gen4 | SYNC heartbeat GEN4 | émise | Sev_M_Track (Generic) | 0x80 | 100 |  |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M1.Right.gen | NMT | émise | Zapi_M_Track (Generic) | 0 | 500 | Func ID, Node ID |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M2.Left.gen | NMT | émise | Zapi_M_Track (Generic) | 0 | 500 | Func ID, Node ID |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M1.Right.gen | GFIN PDO2_TX | reçue | Zapi_M_Track (Generic) | EMERG | Not used | Right Zapi Error Code, alarm present, Zapi alarm code, flag alarm, extra info alarm |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M2.Left.gen | GFIN PDO2_TX | reçue | Zapi_M_Track (Generic) | EMERG | Not used | Left Zapi Error Code, alarm present, Zapi alarm code, flag alarm, extra info alarm |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M1.Right.gen | GFIN HeartBeat | reçue | Zapi_M_Track (Generic) | HeartBeat | 1000 | HeartBeat State |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M2.Left.gen | GFIN HeartBeat | reçue | Zapi_M_Track (Generic) | HeartBeat | 1000 | HeartBeat State |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M1.Right.gen | GFOUT - PDO1_RX | émise | Zapi_M_Track (Generic) | PDO1_RX | 40 | Target_SPeed [Hz/10], Enable Power, Forward Req, Reverse Req, Stuffing, Power Line, Brake |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M2.Left.gen | GFOUT - PDO1_RX | émise | Zapi_M_Track (Generic) | PDO1_RX | 40 | Target SPeed [Hz/10], Enable Power, Forward Req, Reverse Req, Stuffing, Power Line, Brake |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M1.Right.gen | GFIN PDO1_TX | reçue | Zapi_M_Track (Generic) | PDO1_TX | 3000 | Actual_Speed [Hz/10], Out MNC, Stuffing, Actual Current [A*5], Status Byte |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M2.Left.gen | GFIN PDO1_TX | reçue | Zapi_M_Track (Generic) | PDO1_TX | 3000 | Actual_Speed [Hz/10], Out MNC, Stuffing, Actual Current [A*5], Status Byte |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M1.Right.gen | GFIN PDO2_TX | reçue | Zapi_M_Track (Generic) | PDO2_TX | 3000 | Right Zapi Warning, Motor Temp, Heatsink, BDI Percentage, Batterie Current [A], Batterie Voltage |
| MC42 app | mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M2.Left.gen | GFIN PDO2_TX | reçue | Zapi_M_Track (Generic) | PDO2_TX | 3000 | Left Zapi Warning, Motor Temp, Heatsink, BDI Percentage, Batterie Current [A], Batterie Voltage |
| MD4-CAB app | a/c tyva24v | VoltageBattery_M0 | reçue | tyva 24v a/c (Generic) | 0x18FF0080 | Not used | VoltageCellMax [mV], VoltageCellMin [mV], BatteryVoltage tyva [V] |
| MD4-CAB app | a/c tyva24v | CurrentBattery_M0 | reçue | tyva 24v a/c (Generic) | 0x18FF0880 | Not used | WRONG BatteryCurrent [A] |
| MD4-CAB app | a/c tyva24v | BatteryState_M0 | reçue | tyva 24v a/c (Generic) | 0x18FF0980 | Not used | SOC tyva [%], SOH [%], CycleCount |
| MD4-CAB app | a/c tyva24v | TemperatureCell_M0 | reçue | tyva 24v a/c (Generic) | 0x18FF0B80 | Not used | TemperatureCellMax [°C], TemperatureCellMin [°C], TemperatureCellMean [°C] |
| MD4-CAB app | a/c tyva24v | TemperaturePDU_M0 | reçue | tyva 24v a/c (Generic) | 0x18FF0F80 | Not used | TemperaturePDU [°C] |
| MD4-CAB app | a/c tyva24v | FirmwareInformation_M0 | reçue | tyva 24v a/c (Generic) | 0x18FF1080 | Not used | FirmwareMajor, FirmwareMinor, FirmwareRevision, FirmwareBuildMode |
| MD4-CAB app | a/c tyva24v | Error_M0 | reçue | tyva 24v a/c (Generic) | 0x18FF1180 | 10000 | ErrorAFEIssues, ErrorBluetooth, ErrorBmsOverTemperature, ErrorCellIssues, ErrorChargerIssue, ErrorCurrentCalibration, Er |
| MD4-CAB app | a/c tyva24v | SynthesisBMS_M0 | reçue | tyva 24v a/c (Generic) | 0x18FF1280 | 10000 | isBalancing, isChargePossible, isChargeRelayClosingAuth, isDischargePossible, isDischargeRelayClosingAuth, isReadyToStar |
| MD4-CAB app | a/c tyva24v | PDUStatus_M0b | reçue | tyva 24v a/c (Generic) | 0x18FF1380 | Not used | PDURelayStatusCharge, PDURelayStatusDecharge, PDURelayStatusPrecharge |
| MD4-CAB app | a/c tyva24v | Warning_M0 | reçue | tyva 24v a/c (Generic) | 0x18FF1480 | 10000 | WarningAFEIssues, WarningBluetooth, WarningBmsOverTemperature, WarningCellIssues, WarningChargerIssue, WarningCurrentCal |
| MD4-CAB app | a/c tyva24v | MaxAdmissibleCurrent_M0 | reçue | tyva 24v a/c (Generic) | 0x18FF1580 | Not used | IMD [A], IMR [A] |
| MD4-CAB app | a/c tyva24v | ConfigurationInformation_M0 | reçue | tyva 24v a/c (Generic) | 0x18FF1680 | Not used | ConfigurationFileVersion |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva | VoltageBattery_M0 | reçue | tyva battery (Generic) | 0x18FF0080 | Not used | VoltageCellMax [mV], VoltageCellMin [mV], BatteryVoltage tyva [V] |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva | CurrentBattery_M0 | reçue | tyva battery (Generic) | 0x18FF0880 | Not used | WRONG BatteryCurrent [A] |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva | BatteryState_M0 | reçue | tyva battery (Generic) | 0x18FF0980 | Not used | SOC tyva [%], SOH [%], CycleCount |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva | TemperatureCell_M0 | reçue | tyva battery (Generic) | 0x18FF0B80 | Not used | TemperatureCellMax [°C], TemperatureCellMin [°C], TemperatureCellMean [°C] |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva | TemperaturePDU_M0 | reçue | tyva battery (Generic) | 0x18FF0F80 | Not used | TemperaturePDU [°C] |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva | Error_M0 | reçue | tyva battery (Generic) | 0x18FF1180 | 1000 | ErrorAFEIssues, ErrorBluetooth, ErrorBmsOverTemperature, ErrorCellIssues, ErrorChargerIssue, ErrorCurrentCalibration, Er |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva | SynthesisBMS_M0 | reçue | tyva battery (Generic) | 0x18FF1280 | 3000 | isBalancing, isChargePossible, isChargeRelayClosingAuth, isDischargePossible, isDischargeRelayClosingAuth, isReadyToStar |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva | PDUStatus_M0b | reçue | tyva battery (Generic) | 0x18FF1380 | Not used | PDURelayStatusCharge, PDURelayStatusDecharge, PDURelayStatusPrecharge |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva | Warning_M0 | reçue | tyva battery (Generic) | 0x18FF1480 | 1000 | WarningAFEIssues, WarningBluetooth, WarningBmsOverTemperature, WarningCellIssues, WarningChargerIssue, WarningCurrentCal |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva | MaxAdmissibleCurrent_M0 | reçue | tyva battery (Generic) | 0x18FF1580 | Not used | IMD [A], IMR [A] |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen1 | get_hv_2 0x22 | émise | tyva bender (Generic) | 0x22 | 1000 | A BYTE 0 - 3A, A BYTE 1 - 00, A BYTE 2 - 00 |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen1 | get_hv_1 0x22 | émise | tyva bender (Generic) | 0x22 | 1000 | A BYTE 0 - 36, A BYTE 1 - 00, A BYTE 2 - 00 |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen1 | close relay hv1 0x22 | émise | tyva bender (Generic) | 0x22 | 1000 | BYTE 0 - D2, BYTE 1 - 01, BYTE 2 - 00, BYTE 3 - 01, BYTE 4 - 00 |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen1 | close relay hv2 0x22 | émise | tyva bender (Generic) | 0x22 | 1000 | BYTE 0 - D2, BYTE 1 - 00, BYTE 2 - 00, BYTE 3 - 01, BYTE 4 - 00 |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen2 | get_HV_System 0x22 | émise | tyva bender (Generic) | 0x22 | 1000 | A BYTE 0 - 5E, A BYTE 1 - FF, A BYTE 2 - FF, A BYTE 3 - FF |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen2 | get_R_iso_corrected 0x22 | émise | tyva bender (Generic) | 0x22 | 1000 | A BYTE 0 - 4C, A BYTE 1 - FF, A BYTE 2 - FF, A BYTE 3 - FF |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen2 | get_R_iso 0x22 | émise | tyva bender (Generic) | 0x22 | 1000 | A BYTE 0 - 4E, A BYTE 1 - FF, A BYTE 2 - FF, A BYTE 3 - FF |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen2 | get_R_iso_neg 0x22 | émise | tyva bender (Generic) | 0x22 | 1000 | A BYTE 0 - 40, A BYTE 1 - FF, A BYTE 2 - FF, A BYTE 3 - FF |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen2 | Response_HV_System 5E | reçue | tyva bender (Generic) | 0x23 | 3000 | HV_System [Volt] |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen2 | Response_R_iso_corrected 4C | reçue | tyva bender (Generic) | 0x23 | 3000 | R_iso_corrected [kOhm] |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen2 | Response_R_iso 4E | reçue | tyva bender (Generic) | 0x23 | 3000 | R_iso [kOhm] |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen2 | Response_R_iso_neg 40 | reçue | tyva bender (Generic) | 0x23 | 3000 | R_iso_neg [kOhm] |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen1 | IMD_Info | reçue | tyva bender (Generic) | 0x37 | 3000 | Iso Measurement tyva [kOhm], Isolation fault tyva, Chassis fault tyva, system failure tyva isomon, Calibration running,  |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen2 | IMD_InfoGeneral gen2 | reçue | tyva bender (Generic) | 0x37 | Not used | IMD G Alarm Device Error 00, IMD G Alarm Eart Conn 03, IMD G Alarm Earthlift 10, IMD G Alarm HV neg Conn 02, IMD G Alarm |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen1 | Response_hv_2 58 | reçue | tyva bender (Generic) | 35 | 3000 | IG IMC HV 2 [Volt] |
| MC42 app | mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen1 | Response_hv_1 54 | reçue | tyva bender (Generic) | 35 | 3000 | IG IMC HV 1 [Volt] |

## Liaisons entre applications (APPOUT → APPIN)

- MD45-ET app `buttons 45 dtobin APPOUT` (← `buttons 45 dtobin`) → MC42 app `dtob APPIN 45`
- MD4-CAB app `dtobin APPOUT C10` (← `dtobin c10`) → MC42 app `dtob APPIN_1 c10`
- MD45-ET app `Right Joystick ET45 CanOut` (← `Right Joystick ET45 C2:2 [%]`) → MC42 app `Right Joystick ET45 C2:2 APPIN`
- MD45-ET app `Left Joystick ET45 CanOut` (← `Left Joy ET45 ou water level C2:1 [%]`) → MC42 app `Left Joy ET45 ou water level C2:1 APPIN`
- MD4-CAB app `Right Joystick C10 CanOut` (← `Right Joystick C41 C2:2 [%]`) → MC42 app `Right Joystick C41 C2:2 APPIN`
- MD4-CAB app `Left Joystick C10 CanOut` (← `Left Joystick C41 C2:1 [%]`) → MC42 app `Left Joystick C41 C2:1 APPIN`
- MD4-CAB app `dtobin APPOUT C10 B` (← `dtobin c10 B`) → MC42 app `dtobin c10 B APPIN`
- MD4-CAB app `dtobin APPOUT C10 B_1` (← `dtobin c10 B_1`) → MC42 app `dtobin c10 B_1 APPIN`
- MD4-CAB app `auto off tyva 24v APPOUT` (← `auto off tyva 24v`) → MC42 app `auto off tyva 24v APPIN`
- MD4-CAB app `a/c option tyva APPOUT` (← `a/c option tyva`) → MC42 app `a/c option tyva APPIN`
- MD4-CAB app `dtoni APPOUT C10_1` (← `dtobin c10_1`) → MC42 app `dtobin c10_1 APPIN`
- MC42 app `infos for 45/10 dtobin 2 APPOUT` (← `dtobin 2`) → MD4-CAB app `dtobin 2 APPIN c10`
- MC42 app `dtobin 3 APPOUT` (← `dtobin 3`) → MD4-CAB app `dtobin 3 APPIN`
- MC42 app `Joystick to zero APPOUT` (← `Joystick to zero`) → MD4-CAB app `Joystick to zero APPIN`
- MC42 app `batt ok to start APPOUT` (← `batt ok to start`) → MD4-CAB app `batt ok to start APPIN`
- MC42 app `infos for 45/10 dtobin 2 APPOUT` (← `dtobin 2`) → MD45-ET app `info from mc dtobin 2 APPIN`
- MC42 app `batt ok to start APPOUT` (← `batt ok to start`) → MD45-ET app `batt ok to start APPIN`