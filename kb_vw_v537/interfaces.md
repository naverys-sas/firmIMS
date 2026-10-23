# Interfaces matérielles et CAN — v117

Généré par `tools/reports.py`. Les identifiants viennent de l'export texte ; le bus et le module sont ceux déclarés sur chaque canal.

## Modules

- **MD3[0]** (MD3 module)
- **MC2[1]** (MC2 module)
- **J1939[0]** (J1939 module)
- **Radio** (Generic module)
- **G1x** (G1x module)

## Bus CAN déclarés

- **Diagnostics** (Diagnostics bus) J1939 start address=128
- **J1939** (J1939 bus) Speed=250 · Address claim=No
- **Master** (Master bus) 
- **Radio** (Generic bus) Speed=125 · Identifier size=Standard (11 bits)

## Entrées / sorties physiques

| Appli | Groupe | Canal | Type | Module | Index | Entrée / source |
|---|---|---|---|---|---|---|
| MC2 | (racine) |  | SIC |  |  |  |
| MC2 | SAEJ ECM | Malfunction lamp | MDGN | J1939[0] | 0 |  |
| MC2 | SAEJ ECM | Red stop lamp | MDGN | J1939[0] | 0 |  |
| MC2 | SAEJ ECM | Amber warning lamp | MDGN | J1939[0] | 0 |  |
| MC2 | SAEJ ECM | Protect lamp | MDGN | J1939[0] | 0 |  |
| MC2 | Translate | Pump 1 Right | COUT | MC2[1] | 0 | Pump 1 Right Filter ECC1 [%] |
| MC2 | Oil Security |  | DIN | MC2[1] | 0 |  |
| MC2 | Engine Fan | MDGN-Status:MC2[1] | MDGN | MC2[1] | 0 |  |
| MC2 | Translate | Pump 2 Left | COUT | MC2[1] | 1 | Pump 2 Left Filter ECC1 [%] |
| MC2 | (racine) | MDGN-S/N:MC2[1] | MDGN | MC2[1] | 1 |  |
| MC2 | UP/DOWN TRACK | EV - Select Blocage or Blocage | DOUT | MC2[1] | 2 | Map bloc - Blocage/selctor |
| MC2 | (racine) | MDGN-Temp:MC2[1] | MDGN | MC2[1] | 2 |  |
| MC2 | Track Tension | Track pressure | VIN | MC2[1] | 2 |  |
| MC2 | UP/DOWN TRACK / Locking Track | Locking pressure | VIN | MC2[1] | 3 |  |
| MC2 | UP/DOWN TRACK | EV - Dé blocage | DOUT | MC2[1] | 3 | Map bloc - Déblocage |
| MC2 | (racine) | MDGN-Address:MC2[1] | MDGN | MC2[1] | 3 |  |
| MC2 | (racine) |  | MDGN | MC2[1] | 4 |  |
| MC2 | Track Tension | PWM Pression tendeur | COUT | MC2[1] | 4 | PWM Selector [%] |
| MC2 | Oil Security |  | VIN | MC2[1] | 4 |  |
| MC2 | (racine) | MDGN-VREF:MC2[1] | MDGN | MC2[1] | 5 |  |
| MC2 | (racine) | Alim by pass et frein | DOUT | MC2[1] | 5 | TRUE |
| MC2 | (racine) | Alim moteur | DOUT | MC2[1] | 6 | TRUE |
| MC2 | (racine) | Alim vérin et tendeur | DOUT | MC2[1] | 7 | TRUE |
| MC2 | Translate | EV Frein | DOUT | MC2[1] | 12 | Inter EV Frein |
| MC2 | UP/DOWN TRACK | EV By pass | DOUT | MC2[1] | 13 | Inter EV By Pass |
| MC2 | UP/DOWN TRACK | EV Descente | DOUT | MC2[1] | 14 | Inter EV DOWN |
| MC2 | UP/DOWN TRACK | EV Montée | DOUT | MC2[1] | 15 | Inter EV UP |
| MC2 | UP/DOWN TRACK | EV Tendeur Chenille | DOUT | MC2[1] | 18 | Map bloc - tendeur Chenille |
| MC2 | UP/DOWN TRACK | EV DéTendeur Chenille | DOUT | MC2[1] | 19 | Map bloc - dé tendeur Chenille |
| MC2 | Engine Fan | Out SWITCH ON Engine | DOUT | MC2[1] | 20 | Inter Allumage Thermique |
| MC2 | Engine Fan | Out START Engine | DOUT | MC2[1] | 21 | START Engine |
| MC2 | Engine Fan | Out FAN Engine | DOUT | MC2[1] | 22 | Inter FAN |
| MC2 | Engine Fan | OUT Full FAN | DOUT | MC2[1] | 23 | Inter Full Fan |
| MD3 | BLACK LIGHT | Time | SIC |  |  |  |
| MD3 | BLACK LIGHT | Date | SIC |  |  |  |
| MD3 | (racine) | Status:G1x | MDGN | G1x | 0 |  |
| MD3 | (racine) | Network state:G1x | MDGN | G1x | 1 |  |
| MD3 | (racine) | Left Joystick | VIN | MD3[0] | 0 |  |
| MD3 | BUZZER | Buzzer | DOUT | MD3[0] | 0 | Inter Buzzer |
| MD3 | (racine) | MDGN-Status:MD3[0] | MDGN | MD3[0] | 0 |  |
| MD3 | (racine) | Right Joystick | VIN | MD3[0] | 1 |  |
| MD3 | RADIO | MDGN-S/N:MD3[0] | MDGN | MD3[0] | 1 |  |
| MD3 | (racine) | MDGN-Temp:MD3-0 | MDGN | MD3[0] | 2 |  |
| MD3 | (racine) | MDGN-+BAT:MD3-0 | MDGN | MD3[0] | 3 |  |
| MD3 | (racine) | MDGN-VREF:MD3-0 | MDGN | MD3[0] | 4 |  |
| MD3 | Acceleration | X | VIN | MD3[0] | 4 |  |
| MD3 | Acceleration | Y | VIN | MD3[0] | 5 |  |
| MD3 | Acceleration | Z | VIN | MD3[0] | 6 |  |

## Trames CAN

| Appli | Groupe | Trame | Sens | Module | Identifiant | Période / timeout | Contenu |
|---|---|---|---|---|---|---|---|
| MC2 | SAEJ ECM | SPN 629 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 100 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 110 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 105 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 175 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 102 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 1485 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 637 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 656 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 636 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 626 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 677 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 655 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 654 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 653 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 652 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 651 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 639 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 98 | reçue |  |  |  |  |
| MC2 | SAEJ ECM | SPN 106 | reçue |  |  |  |  |
| MC2 | SAEJ Std input |  | reçue |  |  |  |  |
| MC2 | SAEJ Std input | Intake manifold temperature | reçue |  |  |  |  |
| MC2 | SAEJ Std input |  | reçue |  |  |  |  |
| MC2 | SAEJ Std input | Driver's demand, engine % | reçue |  |  |  |  |
| MC2 | SAEJ Std input | Actual engine, % torque | reçue |  |  |  |  |
| MC2 | SAEJ Std input | Engine speed | reçue |  |  |  |  |
| MC2 | SAEJ Std input | Accelerator pedal position | reçue |  |  |  |  |
| MC2 | SAEJ Std input | % load at current speed | reçue |  |  |  |  |
| MC2 | SAEJ Std input | Air inlet pressure | reçue |  |  |  |  |
| MC2 | SAEJ ECM | DM1 | reçue | J1939[0] |  |  | SPN 98 |
| MC2 | SAEJ Std input | Engine Temperature | reçue | J1939[0] | 65262 | 2000 | Engine coolant temperature [°C] |
| MC2 | SAEJ Std input | Inlet / Exhaust conditions 1 | reçue | J1939[0] | 65270 | 2000 | Intake manifold temperature [°C], Air inlet pressure [kPa] |
| MC2 | SAEJ Std input | Engine fluid level/pressure 1 | reçue | J1939[0] | 65263 | 2000 | Engine oil pressure [kPa] |
| MC2 | SAEJ Std input | EEC1 | reçue | J1939[0] | 61444 | 2000 | Driver's demand, engine % [%], Actual engine, % torque [%], Engine speed [rpm] |
| MC2 | SAEJ Std input | EEC2 | reçue | J1939[0] | 61443 | 2000 | Accelerator pedal position [%], % load at current speed [%] |
| MC2 | Speed Engine | TSC1-A:J1939-0 | émise | J1939[0] |  | 20 |  |
| MD3 | RADIO | CAN IN 100 | reçue | Radio (Generic) | 0x100 | 1000 | RadioGauche, RadioDroit, RadioStop, RadioStart, RadioSpeed |
| MD3 | RADIO | CAN IN 101 | reçue | Radio (Generic) | 0x101 | 1000 | TimelapsIn [ms] |
| MD3 | RADIO | CANOUT 102 | émise | Radio (Generic) | 0x102 | 100 | TimeLapsOut [ms], Run Engine Statut |

## Liaisons entre applications (APPOUT → APPIN)

- MC2 `CAN - ENGINE RUN` (← `Engine START`) → MD3 `CAN - ENGINE RUN - Out`
- MC2 `CAN Out tIMER FAN` (← `% Timer FAN [%]`) → MD3 `Can tIMER in`
- MC2 `CAN OK UP/DOWN` (← `OK UP/DOWN`) → MD3 `OK UP/DOWN`
- MC2 `Bad Oil Level Buzzer` (← `Wait Very Low Oil Level`) → MD3 `CAN IN Oil level`
- MD3 `Manip Gauche CanOut` (← `Math Gauche [%]`) → MC2 `Left CanIn`
- MD3 `Manip Droit CanOut` (← `Math Droit [%]`) → MC2 `Right CanIn`
- MD3 `CAN  Speed` (← `Speed`) → MC2 `CAN Speed`
- MD3 `CAN  Free` (← `IDC Speed Free`) → MC2 `CAN Free`
- MD3 `Can Out UP/DOWN Button` (← `UP/DOWN Button`) → MC2 `Can In MD3 UP/DOWN Button`
- MD3 `CAN OUT State Up/Down` (← `State Up/Down`) → MC2 `CAN IN State Up/Down`
- MD3 `Can Out Button State` (← `F1 - Button`) → MC2 `MD3 Start/Stop Button`
- MD3 `MD3 CAN Status` (← `MDGN-Status:MD3[0]`) → MC2 `MD3 Status CAN In`