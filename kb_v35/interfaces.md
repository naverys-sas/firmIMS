# Interfaces matérielles et CAN — V35.42 (X100)

Généré par `tools/reports.py`. Les identifiants viennent de l'export texte ; le bus et le module sont ceux déclarés sur chaque canal.

## Modules

- **MD3[0]** (MD3 module)
- **MC42** (MC42 module)
- **Inboard Engine** (J1939 module)
- **Radio** (Generic module)
- **G1x** (G1x module)
- **KeyBox** (Generic module)
- **Garmin** (Generic module)
- **Charger BMW** (Generic module)
- **Battery BMW** (Generic module)
- **ZAPI** (Generic module)
- **Sevcon_M_Track** (Generic module)
- **HVLP** (J1939 module)
- **Elcon** (Generic module)
- **WattAlps** (Generic module)
- **Proemion** (Generic module)
- **Chargeur Brusa** (Generic module)

## Bus CAN déclarés

- **Diagnostics** (Diagnostics bus) J1939 start address=128
- **J1939** (J1939 bus) Speed=J1939 Speed [kbps] · Address claim=No
- **Master** (Master bus) 
- **iPhone** (Generic bus) Speed=125 · Identifier size=Standard (11 bits)
- **Drive** (Generic bus) Speed=Can Speed [kbps] · Identifier size=Standard (11 bits)
- **Garmin** (Generic bus) Speed=250 · Identifier size=Extended (29 bits)
- **Drive** (Generic bus) Speed=Can Speed [kbps] · Identifier size=Extended (29 bits)

## Entrées / sorties physiques

| Appli | Groupe | Canal | Type | Module | Index | Entrée / source |
|---|---|---|---|---|---|---|
| MC42 | Thermic / SEJ ECM | Malfunction lamp | MDGN | Inboard Engine (J1939[0]) | 1 |  |
| MC42 | Thermic / SEJ ECM | Red stop lamp | MDGN | Inboard Engine (J1939[0]) | 2 |  |
| MC42 | Thermic / SEJ ECM | Amber warning lamp | MDGN | Inboard Engine (J1939[0]) | 3 |  |
| MC42 | Thermic / SEJ ECM | Protect lamp | MDGN | Inboard Engine (J1939[0]) | 4 |  |
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
| MC42 | Track Up/Down | EV By pass | DOUT | MC42 (MC42[1]) | 8 | Inter EV By Pass |
| MC42 | Track Up/Down | EV Up | DOUT | MC42 (MC42[1]) | 9 | Inter EV UP |
| MC42 | Track Up/Down | EV Down | DOUT | MC42 (MC42[1]) | 10 | Inter EV DOWN |
| MC42 | Track Up/Down | EV Tension | DOUT | MC42 (MC42[1]) | 11 | IDC Tension |
| MC42 | Track Up/Down | EV Landing UnBlock | DOUT | MC42 (MC42[1]) | 12 | Libre |
| MC42 | Track Up/Down | EV Landing Lock | DOUT | MC42 (MC42[1]) | 13 | Bloc |
| MC42 | (racine) | Pin 44 (Brake/Batt HT) | DOUT | MC42 (MC42[1]) | 14 | PIN 44 |
| MC42 | Electric | Power Controller | DOUT | MC42 (MC42[1]) | 15 | Var Power |
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
| MC42 | Thermic / SEJ ECM | SPN 629 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 100 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 110 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 105 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 175 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 102 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 1485 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 637 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 656 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 636 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 626 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 677 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 655 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 654 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 653 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 652 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 651 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 639 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 98 | reçue |  |  |  |  |
| MC42 | Thermic / SEJ ECM | SPN 106 | reçue |  |  |  |  |
| MC42 | Thermic / SAEJ Std input |  | reçue |  |  |  |  |
| MC42 | Thermic / SAEJ Std input |  | reçue |  |  |  |  |
| MC42 | Thermic / SAEJ Std input | Driver's demand, engine % | reçue |  |  |  |  |
| MC42 | Thermic / SAEJ Std input | Actual engine, % torque | reçue |  |  |  |  |
| MC42 | Thermic / SAEJ Std input | Engine speed | reçue |  |  |  |  |
| MC42 | Thermic / SAEJ Std input | Accelerator pedal position | reçue |  |  |  |  |
| MC42 | Thermic / SAEJ Std input | % load at current speed | reçue |  |  |  |  |
| MC42 | Electric / CHARGER / Brusa | 1560 - POWER ON - Byte | émise |  |  |  |  |
| MC42 | Electric / CHARGER / Brusa | 1560 - Cycle Value - Byte | émise |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | Status Word | reçue |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | Limit Word | reçue |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | Motor_Speed_Raw | reçue |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | Input Voltage | reçue |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | Torque_Mesured_Raw | reçue |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | M3 (Pump) - Error | reçue |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | Status Word | émise |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | Torque Demande | émise |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | Torque Limit | émise |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | Fw Speed Limit | émise |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | Rw Speed Limit | émise |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | I Batt Discharge Limit | émise |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | I Batt recharge limit | émise |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | Status Word | émise |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | Torque Demande | émise |  |  |  |  |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | Torque Limit | émise |  |  |  |  |
| MC42 | Electric / BATTERY / BMW | NMT | émise | Battery BMW (Generic) | 0 | 500 | ID, State |
| MC42 | Electric / BATTERY / BMW | Bat51TPdo1 | reçue | Battery BMW (Generic) | 0x1D1 | 200 | BatState, BatStateOfCharge, BatCurrent, BatPackVoltage, BatBusVoltage |
| MC42 | Electric / BATTERY / BMW | Iso52MonRPdo1 | émise | Battery BMW (Generic) | 0x252 | 100 | IsoMonCommand, IsoMonWarningLevel, IsoMonErrorLevel |
| MC42 | Electric / BATTERY / BMW | Bat51TPdo2 | reçue | Battery BMW (Generic) | 0x2D1 | 5000 | BatAvgTemp, BatMinCellTemp, BatMaxCellTemp, BatBalancingState, BatTimeToFullMinute |
| MC42 | Electric / BATTERY / BMW | Bat51TPdo3 | reçue | Battery BMW (Generic) | 0x3D1 | 2000 | BatPowerLimitChargeRaw, BatPowerLimitDischargeRaw, BatEnergyRemainingRaw |
| MC42 | Electric / BATTERY / BMW | Dcu50Heartbeat | reçue | Battery BMW (Generic) | 0x750 | 2000 | DcuNodeState |
| MC42 | Electric / BATTERY / BMW | Bat51Hartbeat | reçue | Battery BMW (Generic) | 0x751 | 2000 | BatNodeState |
| MC42 | Electric / BATTERY / BMW | Sync | émise | Battery BMW (Generic) | 0x80 | 20 | SyncCounter |
| MC42 | Electric / BATTERY / BMW | Bat51Error | reçue | Battery BMW (Generic) | 0xD1 | Not used | BatErrorCode, BatError |
| MC42 | Electric / BATTERY / BMW | Iso52MonHeartbeat | reçue | Battery BMW (Generic) | 1874 | 2000 | IsoMonNodeState |
| MC42 | Electric / BATTERY / BMW | Dcu50Error | reçue | Battery BMW (Generic) | 208 | Not used | DcuErrorCode, DcuError |
| MC42 | Electric / BATTERY / BMW | Iso52MonError | reçue | Battery BMW (Generic) | 210 | Not used | IsoMonErrorCode, IsoMonError |
| MC42 | Electric / BATTERY / BMW | Iso52MonTPdo1 | reçue | Battery BMW (Generic) | 466 | 2000 | IsoMonResistance, IsoMonVoltage, IsoMonState |
| MC42 | Electric / BATTERY / BMW | Bat51RPdo1 | émise | Battery BMW (Generic) | 593 | 100 | BatCommand, BatCoolingPolicy |
| MC42 | Electric / CHARGER / BMW | GFOUT-A:Generic | émise | Charger BMW (Generic) | 0x400 | 200 | ENABLE, POWER_REFERENCE, MAXDCVOLTLIMIT, MAXDCCURRLIMIT |
| MC42 | Electric / CHARGER / BMW | GFIN-A:Generic | reçue | Charger BMW (Generic) | 0x405 | 200 | CHARGER_STATUS, CHARGER_MAINS_CURRENT, CHARGER_DC_CURRENT, CHARGER_DC_VOLTAGE, CHARGER_MAINS_FREQUENCY |
| MC42 | Electric / CHARGER / Brusa | 1552 - CAN IN | reçue | Chargeur Brusa (Generic) | 1552 | 1000 | 1552 - Hardware enable - Byte, 1552 - Error detect - Byte, 1552 - Warning Condition - Byte, 1552 - Automatique charging  |
| MC42 | Electric / CHARGER / Brusa | 1553 - CAN IN | reçue | Chargeur Brusa (Generic) | 1553 | 1000 | 1553 - Actual mains current - Byte, 1553 - Actual mains voltage - Byte, 1553 - Actual battery output voltage - Byte, 155 |
| MC42 | Electric / CHARGER / Brusa | 1555 - CAN IN | reçue | Chargeur Brusa (Generic) | 1555 | 1000 | 1555 - Power stage temperature - Byte |
| MC42 | Electric / CHARGER / Brusa | 1560 - Cmd | émise | Chargeur Brusa (Generic) | 1560 | 100 | 1560 - POWER ON - Byte [bits], 1560 - Cycle Value - Byte [bits], 1560 - Max Current from 230 V - Byte, 1560 - Desired Vo |
| MC42 | Electric / CHARGER / Elcon | ELCON-OUT | émise | Elcon (Generic) | 0x1806E5F4 | 500 | Max Voltage, Max Curent, Control |
| MC42 | Electric / CHARGER / Elcon | ELCON-IN | reçue | Elcon (Generic) | 0x18FF50E5 | 1000 | Output Voltage, Output Current, Hardware Failure, Temperature od charger, Input Voltage, Stating State, Communication St |
| MD3 | BackLight | 129025-0 | reçue | Garmin (Generic) | PGN-129025 | 1000 | Latitude G, Longitude G |
| MD3 | BackLight | 129026-0 | reçue | Garmin (Generic) | PGN-129026 | 1000 | Speed_Over_Ground_Raw |
| MD3 | BackLight | 129029-0 | reçue | Garmin (Generic) | PGN-129029 | 1000 | Current Date J, Time_Byte_1_2_J, Time_Byte_3 |
| MD3 | BackLight | 129029-1 | reçue | Garmin (Generic) | PGN-129029 | 1000 | Time_Byte_4 |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | JFIN-A:J1939[113] | reçue | HVLP (J1939[113]) | 71936 | 500 | Status Word, Limit Word |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | JFIN-B:J1939[113] | reçue | HVLP (J1939[113]) | 71680 | 500 | Motor_Speed_Raw, Torque_Mesured_Raw |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | JFIN-C:J1939[113] | reçue | HVLP (J1939[113]) | 72192 | 500 | Input Voltage |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | JFIN-D:J1939[113] | reçue | HVLP (J1939[113]) | 72448 | 3000 | M3 (Pump) - Error |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | JFOUT-A:J1939[250] | émise | HVLP (J1939[113]) | 69632 | 200 | Status Word [bits], Torque Demande [bits], Torque Limit [bits] |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | JFOUT-B:J1939[113] | émise | HVLP (J1939[113]) | 69888 | 200 | Fw Speed Limit [bits], Rw Speed Limit [bits] |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | JFOUT-C:J1939[250] | émise | HVLP (J1939[113]) | 70144 | 200 | I Batt Discharge Limit [bits], I Batt recharge limit [bits] |
| MC42 | Electric / MOTORS / M-Hydrau / Sevcon | JFOUT-A:J1939[113] | émise | HVLP (J1939[113]) | 69632 | 200 | Status Word [bits], Torque Demande [bits], Torque Limit [bits] |
| MC42 | Thermic / SEJ ECM | DM1 | reçue | Inboard Engine (J1939[0]) |  |  | SPN 98 |
| MC42 | Thermic / SAEJ Std input | Engine Temperature | reçue | Inboard Engine (J1939[0]) | 65262 | 2000 | Engine coolant temperature [Â°C] |
| MC42 | Thermic / SAEJ Std input | Engine fluid level/pressure 1 | reçue | Inboard Engine (J1939[0]) | 65263 | 2000 | Engine oil pressure [kPa] |
| MC42 | Thermic / SAEJ Std input | EEC1 | reçue | Inboard Engine (J1939[0]) | 61444 | 2000 | Driver's demand, engine % [%], Actual engine, % torque [%], Engine speed [rpm] |
| MC42 | Thermic / SAEJ Std input | EEC2 | reçue | Inboard Engine (J1939[0]) | 61443 | 2000 | Accelerator pedal position [%], % load at current speed [%] |
| MC42 | Thermic / Engine Speed | TSC1-A:J1939-0 | émise | Inboard Engine (J1939[0]) |  | 20 |  |
| MC42 | KeyBox | GFOUT-D:Generic | émise | KeyBox (Generic) | 0 | 1000 | Byte 0, Byte 1 |
| MC42 | KeyBox | GFOUT-E:Generic | émise | KeyBox (Generic) | 0x20C | 1000 | OFF_Bits_GOUT, ON_Bits_GOUT |
| MC42 | KeyBox | 0x70C | reçue | KeyBox (Generic) | 0x70C | 1000 |  |
| MC42 | KeyBox | GFIN-B:Generic | reçue | KeyBox (Generic) | ID Fault | Not used | K1 Fault, K2 Fault, K3 Fault, K4 Fault, K5 Fault, K6 Fault, K7 Fault, K8 Fault, K9 Fault, K10 Fault, K11 Fault, K12 Faul |
| MC42 | KeyBox | GFOUT-D:Generic | émise | KeyBox (Generic) | ID Prog | Not used | BYTE 0 - HB, BYTE 1 - HB, BYTE 2 - HB, BYTE 4 - HB, BYTE 5 - HB |
| MC42 | KeyBox | GFOUT-E:Generic | émise | KeyBox (Generic) | ID Prog | Not used | BYTE 0 - HB, BYTE 1 - HB, BYTE 2 - HB, BYTE 4 - HB |
| MC42 | Proemion | GFIN-A:Generic | reçue | Proemion (Generic) | 0x7451220 | 2000 | Network State, Signal Quality |
| MC42 | Proemion | Proemion Battery Value 1 | émise | Proemion (Generic) | 0x7451223 | Not used | Drive Mode, Charger Charging, Battery SOC [%], Battery Instant Voltage [V], Battery U Track [V], Iso Resist [kOhm] |
| MC42 | Proemion | Proemion Battery Value 2 | émise | Proemion (Generic) | 0x7451224 | Not used | Current Bat [A], DiffCellVoltage [mV] |
| MC42 | Proemion | Proemion Secon Value | émise | Proemion (Generic) | 0x7451225 | Not used | Error 1, Error 2, Error 3 |
| MC42 | Proemion | Proemion Device | émise | Proemion (Generic) | 0x7451230 | Not used | 12V Batt. [cV] |
| MC42 | Electric / BATTERY / BMW | BMW Error | émise | Proemion (Generic) | 0x7451240 | Not used | BatErrorCode Out, DcuErrorCode Out, IsoMonErrorCode Out |
| MC42 | Electric / MOTORS / M-Tracks / ZAPI Right | Promeion ZAPI | émise | Proemion (Generic) | 0x7451250 | Not used | Right Warning, Left Warning |
| MD3 | RADIO | CAN IN 100 | reçue | Radio (Generic) | 0x100 | 1000 | RadioGauche, RadioDroit, RadioStop, RadioStart, RadioSpeed |
| MD3 | RADIO | CAN IN 101 | reçue | Radio (Generic) | 0x101 | 1000 | TimelapsIn [ms] |
| MD3 | RADIO | CANOUT 102 | émise | Radio (Generic) | 0x102 | 100 | TimeLapsOut [ms], Run Engine Statut |
| MC42 | Electric / MOTORS / M-Tracks / Sevcon | 0x331 | reçue | Sevcon_M_Track (Generic) | 0x331 | 1000 | M1 (Right) - Error, Statut - 1 [State] |
| MC42 | Electric / MOTORS / M-Tracks / Sevcon | 0x332 | reçue | Sevcon_M_Track (Generic) | 0x332 | 1000 | M2 (Left) - Error, Statut - 2 [Status] |
| MC42 | Electric / MOTORS / M-Tracks / Sevcon | 0x341 | reçue | Sevcon_M_Track (Generic) | 0x341 | 1000 | Motor Speed - 1 [rpm], Actual Current - 1 [A], Torque - 1 [Raw] |
| MC42 | Electric / MOTORS / M-Tracks / Sevcon | 0x342 | reçue | Sevcon_M_Track (Generic) | 0x342 | 1000 | Motor Speed - 2 [rpm], Actual Current - 2 [A], Torque actual- 2 [Raw] |
| MC42 | Electric / MOTORS / M-Tracks / Sevcon | 0x351 | reçue | Sevcon_M_Track (Generic) | 0x351 | 1000 | SEV - M1 - KTY [Â°C], SEV - M1 - Heatsink [Â°C], Voltage -1 [Raw] |
| MC42 | Electric / MOTORS / M-Tracks / Sevcon | 0x352 | reçue | Sevcon_M_Track (Generic) | 0x352 | 1000 | SEV - M2 - KTY [Â°C], SEV - M2 - Heatsink [Â°C], Voltage -2 [Raw] |
| MC42 | Electric / MOTORS / M-Tracks / Sevcon | GEN - 4 - Right | émise | Sevcon_M_Track (Generic) | 0x411 | Every cycle | Throttle Input Voltage, Fordward Switch, Inch reverse switch, FS1 Switch |
| MC42 | Electric / MOTORS / M-Tracks / Sevcon | GEN - 4 - Left | émise | Sevcon_M_Track (Generic) | 0x412 | Every cycle | Throttle Input Voltage, Fordward Switch, Inch reverse switch, FS1 Switch |
| MC42 | Electric / MOTORS / M-Tracks / Sevcon | SYNC | émise | Sevcon_M_Track (Generic) | 0x80 | 100 |  |
| MC42 | Electric / BATTERY / WattApls | VMU_BMS_INFO | émise | WattAlps (Generic) | 402726400 | 200 | UBMSModeRequestBMS |
| MC42 | Electric / BATTERY / WattApls | BMS_VMU_STATUS | reçue | WattAlps (Generic) | 418382110 | 200 | Heater Command [%], CoolingSystem Command [%], Fan Command [%], Pump Command [%], Balancing Finished, AuxiliaryOutputSta |
| MC42 | Electric / BATTERY / WattApls | BMS_VMU_FAULTS | reçue | WattAlps (Generic) | 418382366 | 600 | Coin Low voltage, OilLevel, OpenCircuit, WrongConfiguration, CanCurrentSensorFailure, InsulationControlerFailure, MainPr |
| MC42 | Electric / BATTERY / WattApls | BMS_VMU_INFO | reçue | WattAlps (Generic) | 418382622 | 600 | SOH [%], SOC [%], BatteryCurrent, BatteryVoltageBeforeContactors [V], BatteryVoltageAfterContactors [V] |
| MC42 | Electric / BATTERY / WattApls | BMS_VMU_CHARGE | reçue | WattAlps (Generic) | 418382878 | 200 | MaxRegenerativeCurrent [A], MaxDischargeCurrent [A], ChargeVoltageSetpoint [V], ChargeCurrentSetpoint [A] |
| MC42 | Electric / BATTERY / WattApls | BMS_VMU_TRACE | reçue | WattAlps (Generic) | 418383134 | 600 | DaisyChain Number, BatteryAverageTemperature [Degrees], CurrentModule Number, CellMinVoltage, CellMaxVoltage, BatteryMin |
| MC42 | Electric / BATTERY / WattApls | REVISION | reçue | WattAlps (Generic) | 418383390 | 5000 | wrong configuration slave number [Raw], Hardware revision [Raw], Minor revision [Raw], Major revision [Raw] |
| MC42 | Electric / BATTERY / WattApls | INSULATION_RESISTANCE | reçue | WattAlps (Generic) | 418383646 | 3000 | ValueOfInsulationResistance [kohm] |
| MC42 | Electric / MOTORS / M-Tracks / ZAPI Right | NMT | émise | ZAPI (Generic) | 0 | 500 | Func ID, Node ID |
| MC42 | Electric / MOTORS / M-Tracks / ZAPI Left | NMT | émise | ZAPI (Generic) | 0 | 500 | Func ID, Node ID |
| MC42 | Electric / MOTORS / M-Tracks / ZAPI Right | GFIN PDO2_TX | reçue | ZAPI (Generic) | EMERG | Not used | Right Zapi Error Code, alarm present, Zapi alarm code, flag alarm, extra info alarm |
| MC42 | Electric / MOTORS / M-Tracks / ZAPI Left | GFIN PDO2_TX | reçue | ZAPI (Generic) | EMERG | Not used | Left Zapi Error Code, alarm present, Zapi alarm code, flag alarm, extra info alarm |
| MC42 | Electric / MOTORS / M-Tracks / ZAPI Right | GFIN HeartBeat | reçue | ZAPI (Generic) | HeartBeat | 1000 | HeartBeat State |
| MC42 | Electric / MOTORS / M-Tracks / ZAPI Left | GFIN HeartBeat | reçue | ZAPI (Generic) | HeartBeat | 1000 | HeartBeat State |
| MC42 | Electric / MOTORS / M-Tracks / ZAPI Right | GFOUT - PDO1_RX | émise | ZAPI (Generic) | PDO1_RX | 40 | Target_SPeed [Hz/10], Enable Power, Forward Req, Reverse Req, Stuffing, Power Line, Brake |
| MC42 | Electric / MOTORS / M-Tracks / ZAPI Left | GFOUT - PDO1_RX | émise | ZAPI (Generic) | PDO1_RX | 40 | Target SPeed [Hz/10], Enable Power, Forward Req, Reverse Req, Stuffing, Power Line, Brake |
| MC42 | Electric / MOTORS / M-Tracks / ZAPI Right | GFIN PDO1_TX | reçue | ZAPI (Generic) | PDO1_TX | 3000 | Actual_Speed [Hz/10], Out MNC, Stuffing, Actual Current [A*5], Status Byte |
| MC42 | Electric / MOTORS / M-Tracks / ZAPI Left | GFIN PDO1_TX | reçue | ZAPI (Generic) | PDO1_TX | 3000 | Actual_Speed [Hz/10], Out MNC, Stuffing, Actual Current [A*5], Status Byte |
| MC42 | Electric / MOTORS / M-Tracks / ZAPI Right | GFIN PDO2_TX | reçue | ZAPI (Generic) | PDO2_TX | 3000 | Right Zapi Warning, Motor Temp, Heatsink, BDI Percentage, Batterie Current, Batterie Voltage |
| MC42 | Electric / MOTORS / M-Tracks / ZAPI Left | GFIN PDO2_TX | reçue | ZAPI (Generic) | PDO2_TX | 3000 | Left Zapi Warning, Motor Temp, Heatsink, BDI Percentage, Batterie Current, Batterie Voltage |

## Liaisons entre applications (APPOUT → APPIN)

- MC42 `Drive Type` (← `Drive Type`) → MD3 `Drive Type`
- MC42 `OK UP/DOWN` (← `OK UP/DOWN`) → MD3 `OK UP/DOWN Input`
- MC42 `Wait_Very_Low_Oil_Level` (← `Wait_Very_Low_Oil_Level`) → MD3 `Oil level Very Low Input`
- MC42 `System Started` (← `System Started`) → MD3 `ENGINE RUN Input`
- MD3 `Speed Input` (← `Speed State`) → MC42 `Speed Input`
- MD3 `UP/DOWN Button` (← `UP/DOWN Button`) → MC42 `UP/DOWN Button Input`
- MD3 `State Up/Down` (← `State Up/Down`) → MC42 `State Up/Down`
- ? `MDGN-Status:MD3` (← `?`) → MC42 `MD3 State`
- MD3 `F4 Speed Free` (← `F4 Speed Free`) → MC42 `F4 Input`
- MD3 `IDC Speed Free` (← `IDC Speed Free`) → MC42 `Free Input`
- MD3 `Manip Gauche CanOut` (← `Math Gauche [%]`) → MC42 `Left CanIn`
- MD3 `Manip Droit CanOut` (← `Math Droit [%]`) → MC42 `Right CanIn`
- MD3 `Can Out Button F1` (← `F1 - START PAGE`) → MC42 `MD3_Start/Stop`