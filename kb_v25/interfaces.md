# Interfaces matérielles et CAN — V25.74 (Commuter)

Généré par `tools/reports.py`. Les identifiants viennent de l'export texte ; le bus et le module sont ceux déclarés sur chaque canal.

## Modules

- **MD4-10[0]** (MD4-10 module)
- **MC42[1]** (MC42 module)
- **Charger Brusa** (Generic module)
- **Motor Sevcon Right - 1** (Generic module)
- **Motor Sevcon Left - 2** (Generic module)
- **Motor Sevcon hydrolic - 3** (Generic module)
- **IPhone Remote** (Generic module)
- **SYNC** (Generic module)
- **G1x** (G1x module)
- **KEYBOX EQUIPEMENT** (Generic module)
- **Charger Elcon** (Generic module)
- **OutBoard** (Generic module)
- **Garmin** (Generic module)
- **Battery Kreisel** (Generic module)
- **Battery WattAlps** (Generic module)
- **Battery BMW** (Generic module)
- **Charger BMW** (Generic module)
- **Motor Zapi - Right - 1** (Generic module)
- **Motor Zapi - Left - 2** (Generic module)
- **MC42-J** (J1939 module)
- **MD4-10-J** (J1939 module)
- **Promeion** (Generic module)
- **A/C Aentron BatPack** (Generic module) — 2x2kWh / 12V Li-Ion Battery Pack

## Bus CAN déclarés

- **Diagnostics bus** (Diagnostics bus) J1939 start address=128
- **BUS -11 bits** (Generic bus) Speed=500 · Identifier size=Standard (11 bits)
- **Radio Bus** (Generic bus) Speed=125 · Identifier size=Standard (11 bits)
- **BUS -29 bits** (Generic bus) Speed=500 · Identifier size=Extended (29 bits)
- **Generic** (Generic bus) Speed=500 · Identifier size=Standard (11 bits)
- **Generic** (Generic bus) Speed=250 · Identifier size=Extended (29 bits)
- **Generic** (Generic bus) Speed=500 · Identifier size=Extended (29 bits)
- **J1939** (J1939 bus) Speed=250 · Address claim=No
- **Master** (Master bus) 
- **Generic** (Generic bus) Speed=500 · Identifier size=Standard (11 bits)

## Entrées / sorties physiques

| Appli | Groupe | Canal | Type | Module | Index | Entrée / source |
|---|---|---|---|---|---|---|
| MC42[1] application | (racine) | Cycle utilization | SIC |  |  |  |
| MC42[1] application | ELEC | MDGN-Status:MC2[1] | MDGN | MC42[1] | 0 |  |
| MC42[1] application | ELEC / Oil Security | Oil level Analog | VIN | MC42[1] | 0 |  |
| MC42[1] application | Track Tension | PWM Pression tendeur | COUT | MC42[1] | 0 | PWM Selector [%] |
| MC42[1] application | Equipement | Ladder_Sensor | DPCNT | MC42[1] | 0 |  |
| MC42[1] application | UP/DOWN | Pression Blocage Bras | VIN | MC42[1] | 1 |  |
| MC42[1] application | (racine) | MDGN-S/N:MC2[1] | MDGN | MC42[1] | 1 |  |
| MC42[1] application | Track Tension | Track pressure | VIN | MC42[1] | 2 |  |
| MC42[1] application | (racine) | MDGN-Temp:MC2[1] | MDGN | MC42[1] | 2 |  |
| MC42[1] application | (racine) | MDGN-Address:MC2[1] | MDGN | MC42[1] | 3 |  |
| MC42[1] application | Equipement | Water Level | VIN | MC42[1] | 3 |  |
| MC42[1] application | (racine) | MDGN-+BAT:MC2[1] | MDGN | MC42[1] | 4 |  |
| MC42[1] application | Equipement | VIN-E:MC42[1] | VIN | MC42[1] | 4 |  |
| MC42[1] application | (racine) | MDGN-VREF:MC2[1] | MDGN | MC42[1] | 5 |  |
| MC42[1] application | Acceleration | X | VIN | MC42[1] | 5 |  |
| MC42[1] application | Acceleration | Y | VIN | MC42[1] | 6 |  |
| MC42[1] application | SEAT | UP/DOWN | PWM | MC42[1] | 6 | Seat UP/DOWN [%] |
| MC42[1] application | (racine) | MDGN-VREF:MC2[1] | MDGN | MC42[1] | 6 |  |
| MC42[1] application | Acceleration | Z | VIN | MC42[1] | 7 |  |
| MC42[1] application | UP/DOWN | EV BY PASS | DOUT | MC42[1] | 8 | Inter EV By Pass |
| MC42[1] application | UP/DOWN | EV UP | DOUT | MC42[1] | 9 | Inter EV UP |
| MC42[1] application | SEAT | FRONT BACK | PWM | MC42[1] | 9 | Seat Front Back [%] |
| MC42[1] application | UP/DOWN | EV DOWN | DOUT | MC42[1] | 10 | Inter EV DOWN |
| MC42[1] application | UP/DOWN | EV Tendeur Chenille | DOUT | MC42[1] | 11 | Condition motor ON |
| MC42[1] application | UP/DOWN | EV DÃ©blocage | DOUT | MC42[1] | 12 | Unblock IDC |
| MC42[1] application | Equipement | REMOTE DOWN | DIN | MC42[1] | 12 |  |
| MC42[1] application | UP/DOWN | EV Blocage bras | DOUT | MC42[1] | 13 | Block IDC |
| MC42[1] application | Equipement | REMOTE UP | DIN | MC42[1] | 13 |  |
| MC42[1] application | ELEC | Var Power | DOUT | MC42[1] | 14 | Var Power |
| MC42[1] application | ELEC | Batt Reset | DOUT | MC42[1] | 15 | IDC - BATT |
| MD4-10[0] application | (racine) | Cycle utilization | SIC |  |  |  |
| MD4-10[0] application | EQUIPEMENT | Active display page | SIC |  |  |  |
| MD4-10[0] application | (racine) | Project version | SIC |  |  |  |
| MD4-10[0] application | NMEA / GPS | Time | SIC |  |  |  |
| MD4-10[0] application | (racine) | Status:G1x | MDGN | G1x | 0 |  |
| MD4-10[0] application | (racine) | Network state:G1x | MDGN | G1x | 1 |  |
| MD4-10[0] application | (racine) | Left Joystick | VIN | MD4-10[0] | 0 |  |
| MD4-10[0] application | Link MD4 | MDGN-Status:MD3[0] | MDGN | MD4-10[0] | 0 |  |
| MD4-10[0] application | BUZZER | Buzzer | DOUT | MD4-10[0] | 0 | Inter Buzzer |
| MD4-10[0] application | (racine) | Right Joystick | VIN | MD4-10[0] | 1 |  |
| MD4-10[0] application | (racine) | S/N:MD4-10[0] | MDGN | MD4-10[0] | 1 |  |
| MD4-10[0] application | (racine) | Temp:MD4-10[0] | MDGN | MD4-10[0] | 2 |  |
| MD4-10[0] application | EQUIPEMENT | Button Cabine | DIN | MD4-10[0] | 3 |  |
| MD4-10[0] application | (racine) | Address:MD4-10[0] | MDGN | MD4-10[0] | 3 |  |
| MD4-10[0] application | EQUIPEMENT | Button Door | DIN | MD4-10[0] | 4 |  |
| MD4-10[0] application | (racine) | +BAT:MD4-10[0] | MDGN | MD4-10[0] | 4 |  |
| MD4-10[0] application | (racine) | VREF:MD4-10[0] | MDGN | MD4-10[0] | 5 |  |

## Trames CAN

| Appli | Groupe | Trame | Sens | Module | Identifiant | Période / timeout | Contenu |
|---|---|---|---|---|---|---|---|
| MC42[1] application | ELEC / CHARGER / Brusa | 1560 - POWER ON - Byte | émise |  |  |  |  |
| MC42[1] application | ELEC / CHARGER / Brusa | 1560 - Cycle Value - Byte | émise |  |  |  |  |
| MD4-10[0] application | EQUIPEMENT / A/C Aentron BatPack / BatPackSync | SyncBatFrame | émise | A/C Aentron BatPack (Generic) | 0x80 | 5 | SyncSignal |
| MD4-10[0] application | EQUIPEMENT / A/C Aentron BatPack / BatPackSync | GFIN-E:N1_Tx_Amp | reçue | A/C Aentron BatPack (Generic) | ID_Tx_Amp_N1 | Not used | N1 MMS Current [*0.03125 A] |
| MD4-10[0] application | EQUIPEMENT / A/C Aentron BatPack / BatPackSync | GFIN-F:N2_Tx_Amp | reçue | A/C Aentron BatPack (Generic) | ID_Tx_Amp_N2 | Not used | N2 MMS Current [*0.03125 A] |
| MD4-10[0] application | EQUIPEMENT / A/C Aentron BatPack / BatPackSync | GFIN-C:N1_Tx_Info | reçue | A/C Aentron BatPack (Generic) | ID_Tx_Info_N1 | Not used | N1 Maximum String Cells Voltage [*0.02 Volt], N1 Minimum String Cells Voltage [*0.02 Volt], N1 MMS SOH [%], N1 Maximum M |
| MD4-10[0] application | EQUIPEMENT / A/C Aentron BatPack / BatPackSync | GFIN-D:N2_Tx_Info | reçue | A/C Aentron BatPack (Generic) | ID_Tx_Info_N2 | Not used | N2 Maximum String Cells Voltage [*0.02 Volt], N2 Minimum String Cells Voltage [*0.02 Volt], N2 MMS SOH [%], N2 Maximum M |
| MD4-10[0] application | EQUIPEMENT / A/C Aentron BatPack / BatPackSync | GFIN-A:N1_Tx_Status | reçue | A/C Aentron BatPack (Generic) | ID_Tx_Status_N1 | Not used | N1 MMS Module State, N1 MMS Module SOC [%], N1 MMS Errors, N1 MMS Voltage [mV] |
| MD4-10[0] application | EQUIPEMENT / A/C Aentron BatPack / BatPackSync | GFIN-B:N2_Tx_Status | reçue | A/C Aentron BatPack (Generic) | ID_Tx_Status_N2 | Not used | N2 MMS Module State, N2 MMS Module SOC [%], N2 MMS Errors, N2 MMS Voltage [mV] |
| MC42[1] application | ELEC / BATTERY / BMW | NMT | émise | Battery BMW (Generic) | 0 | 500 | ID, State |
| MC42[1] application | ELEC / BATTERY / BMW | Bat51TPdo1 | reçue | Battery BMW (Generic) | 0x1D1 | 200 | BatState, BatStateOfCharge, BatCurrent, BatPackVoltage, BatBusVoltage |
| MC42[1] application | ELEC / BATTERY / BMW | Iso52MonRPdo1 | émise | Battery BMW (Generic) | 0x252 | 100 | IsoMonCommand, IsoMonWarningLevel, IsoMonErrorLevel |
| MC42[1] application | ELEC / BATTERY / BMW | Bat51TPdo2 | reçue | Battery BMW (Generic) | 0x2D1 | 5000 | BatAvgTemp, BatMinCellTemp, BatMaxCellTemp, BatBalancingState, BatTimeToFullMinute |
| MC42[1] application | ELEC / BATTERY / BMW | Bat51TPdo3 | reçue | Battery BMW (Generic) | 0x3D1 | 2000 | BatPowerLimitChargeRaw, BatPowerLimitDischargeRaw, BatEnergyRemainingRaw |
| MC42[1] application | ELEC / BATTERY / BMW | Dcu50Heartbeat | reçue | Battery BMW (Generic) | 0x750 | 2000 | DcuNodeState |
| MC42[1] application | ELEC / BATTERY / BMW | Bat51Hartbeat | reçue | Battery BMW (Generic) | 0x751 | 2000 | BatNodeState |
| MC42[1] application | ELEC / BATTERY / BMW | Sync | émise | Battery BMW (Generic) | 0x80 | 20 | SyncCounter |
| MC42[1] application | ELEC / BATTERY / BMW | Bat51Error | reçue | Battery BMW (Generic) | 0xD1 | Not used | BatErrorCode, BatError |
| MC42[1] application | ELEC / BATTERY / BMW | Iso52MonHeartbeat | reçue | Battery BMW (Generic) | 1874 | 2000 | IsoMonNodeState |
| MC42[1] application | ELEC / BATTERY / BMW | Dcu50Error | reçue | Battery BMW (Generic) | 208 | Not used | DcuErrorCode, DcuError |
| MC42[1] application | ELEC / BATTERY / BMW | Iso52MonError | reçue | Battery BMW (Generic) | 210 | Not used | IsoMonErrorCode, IsoMonError |
| MC42[1] application | ELEC / BATTERY / BMW | Iso52MonTPdo1 | reçue | Battery BMW (Generic) | 466 | 2000 | IsoMonResistance, IsoMonVoltage, IsoMonState |
| MC42[1] application | ELEC / BATTERY / BMW | Bat51RPdo1 | émise | Battery BMW (Generic) | 593 | 100 | BatCommand, BatCoolingPolicy |
| MC42[1] application | ELEC / BATTERY / Kreisel | 2047 EXT_FuncRequest | émise | Battery Kreisel (Generic) | 2047 | 100 | Func_MSW_Request_Master, Func_sys_state_req, Func_iso_measurement |
| MC42[1] application | ELEC / BATTERY / Kreisel | 257 mBMS_FuncSTAT | reçue | Battery Kreisel (Generic) | 257 | 2000 | BMS_start_up_ready, BMS_stay_alive, BMS_iso_meas_act, BMS_balancing_act, BMS_reset_denied, BMS_wakeup_active, BMS_Master |
| MC42[1] application | ELEC / BATTERY / Kreisel | 258 mBMS_ROE | reçue | Battery Kreisel (Generic) | 258 | 100 | EVT_ErrNr_SC, EVT_Context, mBMS_ROE_Mux M |
| MC42[1] application | ELEC / BATTERY / Kreisel | 276 mBMS_Trac_Info | reçue | Battery Kreisel (Generic) | 276 | 2000 | BMS_Iso_Resist, BMS_U_Trac [dV] |
| MC42[1] application | ELEC / BATTERY / Kreisel | 277 mBMS_Temp_Info | reçue | Battery Kreisel (Generic) | 277 | 2000 | BMS_ext_Temp_Inlet, BMS_ext_Temp_Outlet |
| MC42[1] application | ELEC / BATTERY / Kreisel | 304 mBMS_Version_1 | reçue | Battery Kreisel (Generic) | 304 | 2000 | VER_CSC_release, VER_CSC_minor, VER_CSC_major, VER_MC_release, VER_MC_minor, VER_MC_major, VER_MC_DS_CRC |
| MC42[1] application | ELEC / BATTERY / Kreisel | 305 mBMS_Version_2 | reçue | Battery Kreisel (Generic) | 305 | 2000 | VER_CSC_release, VER_CSC_minor, VER_CSC_major, VER_MC_release, VER_MC_minor, VER_MC_major, VER_MC_DS_CRC |
| MC42[1] application | ELEC / BATTERY / Kreisel | 912 mBMS_Bat_Info_Master | reçue | Battery Kreisel (Generic) | 912 | 2000 | BMS_SOC_Master, BMS_I_Batt_Maste [A], BMS_U_Batt_Master |
| MC42[1] application | ELEC / BATTERY / Kreisel | 913 mBMS_Cell_Info_Master | reçue | Battery Kreisel (Generic) | 913 | 2000 | U_Cell_min_Master, U_Cell_max_Master, U_Cell_avg_Master, Cell_T_max_Master, Cell_T_min_Master |
| MC42[1] application | ELEC / BATTERY / WattAlps | VMU_BMS_Diag | émise | Battery WattAlps (Generic) | 0x18021E00 | 400 | WattAlps Debug |
| MC42[1] application | ELEC / BATTERY / WattAlps | VMU_BMS_INFO | émise | Battery WattAlps (Generic) | 402726400 | 200 | UBMSModeRequestBMS |
| MC42[1] application | ELEC / BATTERY / WattAlps | BMS_VMU_STATUS | reçue | Battery WattAlps (Generic) | 418382110 | 200 | Heater Command [%], CoolingSystem Command [%], Fan Command [%], Pump Command [%], Balancing Finished, AuxiliaryOutputSta |
| MC42[1] application | ELEC / BATTERY / WattAlps | BMS_VMU_FAULTS | reçue | Battery WattAlps (Generic) | 418382366 | 600 | Coin Low voltage, OilLevel, OpenCircuit, WrongConfiguration, CanCurrentSensorFailure, InsulationControlerFailure, MainPr |
| MC42[1] application | ELEC / BATTERY / WattAlps | BMS_VMU_FAULTS | émise | Battery WattAlps (Generic) | 418382367 | Not used | Coin Low voltage, OilLevel, OpenCircuit, WrongConfiguration, CanCurrentSensorFailure, InsulationControlerFailure, MainPr |
| MC42[1] application | ELEC / BATTERY / WattAlps | BMS_VMU_INFO | reçue | Battery WattAlps (Generic) | 418382622 | 600 | SOH [%], SOC [%], BatteryCurrent, BatteryVoltageBeforeContactors [V], BatteryVoltageAfterContactors [V] |
| MC42[1] application | ELEC / BATTERY / WattAlps | BMS_VMU_CHARGE | reçue | Battery WattAlps (Generic) | 418382878 | 200 | MaxRegenerativeCurrent [A], MaxDischargeCurrent [A], ChargeVoltageSetpoint [V], ChargeCurrentSetpoint [A] |
| MC42[1] application | ELEC / BATTERY / WattAlps | BMS_VMU_TRACE | reçue | Battery WattAlps (Generic) | 418383134 | 600 | DaisyChain Number, BatteryAverageTemperature [Degrees], CurrentModule Number, CellMinVoltage, CellMaxVoltage, BatteryMin |
| MC42[1] application | ELEC / BATTERY / WattAlps | REVISION | reçue | Battery WattAlps (Generic) | 418383390 | 5000 | wrong configuration slave number [Raw], Hardware revision [Raw], Minor revision [Raw], Major revision [Raw] |
| MC42[1] application | ELEC / BATTERY / WattAlps | INSULATION_RESISTANCE | reçue | Battery WattAlps (Generic) | 418383646 | 3000 | ValueOfInsulationResistance [kohm] |
| MC42[1] application | ELEC / CHARGER / BMW | GFOUT-A:Generic | émise | Charger BMW (Generic) | 0x400 | 1000 | ENABLE, POWER_REFERENCE, MAXDCVOLTLIMIT, MAXDCCURRLIMIT |
| MC42[1] application | ELEC / CHARGER / BMW | GFIN-A:Generic | reçue | Charger BMW (Generic) | 0x405 | 200 | CHARGER_STATUS, CHARGER_MAINS_CURRENT, CHARGER_DC_CURRENT, CHARGER_DC_VOLTAGE, CHARGER_MAINS_FREQUENCY |
| MC42[1] application | ELEC / CHARGER / Brusa | 1552 - CAN IN | reçue | Charger Brusa (Generic) | 1552 | 1000 | 1552 - Hardware enable - Byte, 1552 - Error detect - Byte, 1552 - Warning Condition - Byte, 1552 - Automatique charging  |
| MC42[1] application | ELEC / CHARGER / Brusa | 1553 - CAN IN | reçue | Charger Brusa (Generic) | 1553 | 1000 | 1553 - Actual mains current - Byte, 1553 - Actual mains voltage - Byte, 1553 - Actual battery output voltage - Byte, 155 |
| MC42[1] application | ELEC / CHARGER / Brusa | 1555 - CAN IN | reçue | Charger Brusa (Generic) | 1555 | 1000 | 1555 - Power stage temperature - Byte |
| MC42[1] application | ELEC / CHARGER / Brusa | 1560 - Cmd | émise | Charger Brusa (Generic) | 1560 | 100 | 1560 - POWER ON - Byte [bits], 1560 - Cycle Value - Byte [bits], 1560 - Max Current from 230 V - Byte, 1560 - Desired Vo |
| MC42[1] application | ELEC / CHARGER / Elcon | ELCON-OUT | émise | Charger Elcon (Generic) | 0x1806E5F4 | 500 | Max Voltage, Max Curent, Control |
| MC42[1] application | ELEC / CHARGER / Elcon | ELCON-IN | reçue | Charger Elcon (Generic) | 0x18FF50E5 | 1000 | Output Voltage, Output Current, Hardware Failure, Temperature od charger, Input Voltage, Stating State, Communication St |
| MD4-10[0] application | NMEA / GPS | 129025-0 | reçue | Garmin (Generic) | PGN-129025 | 1000 | Latitude G, Longitude G |
| MD4-10[0] application | NMEA / GPS | 129026-0 | reçue | Garmin (Generic) | PGN-129026 | 1000 | Speed Over Ground Raw |
| MD4-10[0] application | NMEA / GPS | 129029-0 | reçue | Garmin (Generic) | PGN-129029 | 1000 | Current Date J, Time_Byte_1_2_J, Time_Byte_3 |
| MD4-10[0] application | NMEA / GPS | 129029-1 | reçue | Garmin (Generic) | PGN-129029 | 1000 | Time_Byte_4 |
| MD4-10[0] application | iPhone | CAN IN 100 | reçue | IPhone Remote (Generic) | 0x100 | 1000 | RadioGauche, RadioDroit, RadioStop, RadioStart, RadioSpeed |
| MD4-10[0] application | iPhone | CAN IN 101 | reçue | IPhone Remote (Generic) | 0x101 | 1000 | TimelapsIn [ms] |
| MD4-10[0] application | iPhone | CANOUT 102 | émise | IPhone Remote (Generic) | 0x102 | 50 | TimeLapsOut [ms], Run Engine Statut |
| MD4-10[0] application | EQUIPEMENT | GFOUT-D:Generic | émise | KEYBOX EQUIPEMENT (Generic) | 0 | 1000 | Byte 0, Byte 1 |
| MD4-10[0] application | EQUIPEMENT | GFOUT-E:Generic | émise | KEYBOX EQUIPEMENT (Generic) | 0 | 1000 | Byte 0, Byte 1 |
| MD4-10[0] application | EQUIPEMENT | GFOUT-F:Generic | émise | KEYBOX EQUIPEMENT (Generic) | 0 | 1000 | Byte 0, Byte 1 |
| MD4-10[0] application | PROGRAM KEYBOX | GFOUT-I:Generic | émise | KEYBOX EQUIPEMENT (Generic) | 0 | 5000 | Byte 0, Byte 1 |
| MD4-10[0] application | EQUIPEMENT / KTB Frame 1st Gen KB | GFOUT-E:Generic | émise | KEYBOX EQUIPEMENT (Generic) | 0x217 | 500 | K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12 |
| MD4-10[0] application | EQUIPEMENT / KTB Frame 2d Gen KB | GFOUT-E:Generic | émise | KEYBOX EQUIPEMENT (Generic) | 0x217 | 1000 | OFF_Bits_GOUT, ON_Bits_GOUT |
| MD4-10[0] application | EQUIPEMENT / KBB Frame 1st Gen KB | GFOUT-E:Generic | émise | KEYBOX EQUIPEMENT (Generic) | 0x218 | 500 | K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12 |
| MD4-10[0] application | EQUIPEMENT / KBB Frame 2d Gen KB | GFOUT-E:Generic | émise | KEYBOX EQUIPEMENT (Generic) | 0x218 | 1000 | OFF_Bits_GOUT, ON_Bits_GOUT |
| MD4-10[0] application | EQUIPEMENT / KTC Frame 1st Gen KB | GFOUT-E:Generic | émise | KEYBOX EQUIPEMENT (Generic) | 0x219 | 500 | K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12 |
| MD4-10[0] application | EQUIPEMENT / KTC Frame 2d Gen KB | GFOUT-E:Generic | émise | KEYBOX EQUIPEMENT (Generic) | 0x219 | 1000 | OFF_Bits_GOUT, ON_Bits_GOUT |
| MD4-10[0] application | EQUIPEMENT | 0x717 | reçue | KEYBOX EQUIPEMENT (Generic) | 0x717 | 1000 |  |
| MD4-10[0] application | EQUIPEMENT | 0x718 | reçue | KEYBOX EQUIPEMENT (Generic) | 0x718 | 1000 |  |
| MD4-10[0] application | EQUIPEMENT | 0x719 | reçue | KEYBOX EQUIPEMENT (Generic) | 0x719 | 1000 |  |
| MD4-10[0] application | PROGRAM KEYBOX | Call Default | reçue | KEYBOX EQUIPEMENT (Generic) | Default Read ID | 1000 |  |
| MD4-10[0] application | PROGRAM KEYBOX | GFOUT-C:Generic | émise | KEYBOX EQUIPEMENT (Generic) | Default Write ID | Not used | BYTE 0 - New ID, BYTE 1 - New ID, BYTE 2 - New ID, BYTE 4 - New ID |
| MD4-10[0] application | PROGRAM KEYBOX | GFOUT-H:Generic | émise | KEYBOX EQUIPEMENT (Generic) | ID | Not used | BYTE 0 - HB, BYTE 1 - HB, BYTE 2 - HB, BYTE 4 - HB, BYTE 5 - HB |
| MD4-10[0] application | PROGRAM KEYBOX | GFOUT-J:Generic | émise | KEYBOX EQUIPEMENT (Generic) | ID | Not used | BYTE 0 - New ID, BYTE 1 - New ID, BYTE 2 - New ID, BYTE 4 - New ID |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Sevcon | 0x332 | reçue | Motor Sevcon Left - 2 (Generic) | 0x332 | 1000 | M2 (Left) - Error, Statut - 2 [Status] |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Sevcon | 0x342 | reçue | Motor Sevcon Left - 2 (Generic) | 0x342 | 1000 | Motor Speed - 2 [rpm], Actual Current - 2 [A], Torque actual- 2 [Raw] |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Sevcon | 0x352 | reçue | Motor Sevcon Left - 2 (Generic) | 0x352 | 1000 | SEV - M2 - KTY [Â°C], SEV - M2 - Heatsink [Â°C], Voltage -2 [Raw] |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Sevcon | GEN - 4 - Left | émise | Motor Sevcon Left - 2 (Generic) | 0x412 | Every cycle | Throttle Input Voltage, Fordward Switch, Inch reverse switch, FS1 Switch |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Sevcon | 0x331 | reçue | Motor Sevcon Right - 1 (Generic) | 0x331 | 1000 | M1 (Right) - Error, Statut - 1 [State] |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Sevcon | 0x341 | reçue | Motor Sevcon Right - 1 (Generic) | 0x341 | 1000 | Motor Speed - 1 [rpm], Actual Current - 1 [A], Torque - 1 [Raw] |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Sevcon | 0x351 | reçue | Motor Sevcon Right - 1 (Generic) | 0x351 | 1000 | SEV - M1 - KTY [Â°C], SEV - M1 - Heatsink [Â°C], Voltage -1 [Raw] |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Sevcon | GEN - 4 - Right | émise | Motor Sevcon Right - 1 (Generic) | 0x411 | Every cycle | Throttle Input Voltage, Fordward Switch, Inch reverse switch, FS1 Switch |
| MC42[1] application | ELEC / MOTORS / M-Hydrau / Sevcon | 0x191071FA | émise | Motor Sevcon hydrolic - 3 (Generic) | 0x191071FA | 200 | Status Word, Torque Demande, Torque Limit |
| MC42[1] application | ELEC / MOTORS / M-Hydrau / Sevcon | 0x191171FA | émise | Motor Sevcon hydrolic - 3 (Generic) | 0x191171FA | 200 | Fw Speed Limit, Rw Speed Limit |
| MC42[1] application | ELEC / MOTORS / M-Hydrau / Sevcon | 0x191271FA | émise | Motor Sevcon hydrolic - 3 (Generic) | 0x191271FA | 200 | I Batt Discharge Limit, I Batt recharge limit |
| MC42[1] application | ELEC / MOTORS / M-Hydrau / Sevcon | 0x1918FF71 | reçue | Motor Sevcon hydrolic - 3 (Generic) | 0x1918FF71 | 500 | Motor Speed [rpm], Torque Mesured |
| MC42[1] application | ELEC / MOTORS / M-Hydrau / Sevcon | 0x1919FF71 | reçue | Motor Sevcon hydrolic - 3 (Generic) | 0x1919FF71 | 500 | Status Word, Limit Word |
| MC42[1] application | ELEC / MOTORS / M-Hydrau / Sevcon | 0x191AFF71 | reçue | Motor Sevcon hydrolic - 3 (Generic) | 0x191AFF71 | 500 | Input Voltage, Heatsink [Byte], Sevcon - Engine Temp [Â°C] |
| MC42[1] application | ELEC / MOTORS / M-Hydrau / Sevcon | 0x191BFF71 | reçue | Motor Sevcon hydrolic - 3 (Generic) | 0x191BFF71 | 3000 | M3 (Pump) - Error |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Zapi Left | NMT | émise | Motor Zapi - Left - 2 (Generic) | 0 | 500 | Func ID, Node ID |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Zapi Left | GFIN PDO2_TX | reçue | Motor Zapi - Left - 2 (Generic) | EMERG | Not used | Left Zapi Error Code, alarm present, Zapi alarm code, flag alarm, extra info alarm |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Zapi Left | GFIN HeartBeat | reçue | Motor Zapi - Left - 2 (Generic) | HeartBeat | 1000 | HeartBeat State |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Zapi Left | GFOUT - PDO1_RX | émise | Motor Zapi - Left - 2 (Generic) | PDO1_RX | 40 | Target SPeed [Hz/10], Enable Power, Forward Req, Reverse Req, Stuffing, Power Line, Brake |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Zapi Left | GFIN PDO1_TX | reçue | Motor Zapi - Left - 2 (Generic) | PDO1_TX | 3000 | Actual_Speed [Hz/10], Out MNC, Stuffing, Actual Current [A*5], Status Byte |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Zapi Left | GFIN PDO2_TX | reçue | Motor Zapi - Left - 2 (Generic) | PDO2_TX | 3000 | Left Zapi Warning, Motor Temp, Heatsink, BDI Percentage, Batterie Current, Batterie Voltage |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Zapi Right | NMT | émise | Motor Zapi - Right - 1 (Generic) | 0 | 500 | Func ID, Node ID |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Zapi Right | GFIN PDO2_TX | reçue | Motor Zapi - Right - 1 (Generic) | EMERG | Not used | Right Zapi Error Code, alarm present, Zapi alarm code, flag alarm, extra info alarm |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Zapi Right | GFIN HeartBeat | reçue | Motor Zapi - Right - 1 (Generic) | HeartBeat | 1000 | HeartBeat State |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Zapi Right | GFOUT - PDO1_RX | émise | Motor Zapi - Right - 1 (Generic) | PDO1_RX | 40 | Target_SPeed [Hz/10], Enable Power, Forward Req, Reverse Req, Stuffing, Power Line, Brake |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Zapi Right | GFIN PDO1_TX | reçue | Motor Zapi - Right - 1 (Generic) | PDO1_TX | 3000 | Actual_Speed [Hz/10], Out MNC, Stuffing, Actual Current [A*5], Status Byte |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Zapi Right | GFIN PDO2_TX | reçue | Motor Zapi - Right - 1 (Generic) | PDO2_TX | 3000 | Right Zapi Warning, Motor Temp, Heatsink, BDI Percentage, Batterie Current, Batterie Voltage |
| MD4-10[0] application | NMEA / OutBoard | 127488-Eng 1 | reçue | OutBoard (Generic) | PGN-127488 | 1000 | Engine 1 - Speed - Raw, Engine 1 - Trim |
| MD4-10[0] application | NMEA / OutBoard | 127488-Eng 2 | reçue | OutBoard (Generic) | PGN-127488 | 1000 | Engine 2 - Speed - Raw, Engine 2 - Trim |
| MD4-10[0] application | NMEA / OutBoard | 127489-0 | reçue | OutBoard (Generic) | PGN-127489 | 1000 | Sequence, Page, Engine Intance, Engine oil pressure, Engine oil temp., Engine temp. Byte 0 |
| MD4-10[0] application | NMEA / OutBoard | 127489-1 | reçue | OutBoard (Generic) | PGN-127489 | 1000 | Sequence, Page, Engine temp. Byte 1, Alternator potential, Fuel rate, Total engine hours - Byte 0 |
| MD4-10[0] application | NMEA / OutBoard | 127489-2 | reçue | OutBoard (Generic) | PGN-127489 | 1000 | Total engine hours - Byte 1 |
| MD4-10[0] application | NMEA / OutBoard | 127505-Eng 1 - Can | reçue | OutBoard (Generic) | PNG-127505 | 3000 | Engine 1 - Tank - RAW |
| MD4-10[0] application | NMEA / OutBoard | 127505-Eng 2 Page 1- Can | reçue | OutBoard (Generic) | PNG-127505 | 3000 | Engine 2 Page 1 - Tank - Raw |
| MD4-10[0] application | NMEA / OutBoard | 127505-Eng 2 Page 2- Can | reçue | OutBoard (Generic) | PNG-127505 | 3000 | Engine 2 Page 2 - Tank - Raw |
| MC42[1] application | Proemion | GFIN-A:Generic | reçue | Promeion (Generic) | 0x7451220 | 2000 | Network State, Signal Quality |
| MC42[1] application | Proemion | Proemion Battery Value 1 | émise | Promeion (Generic) | 0x7451223 | Not used | Drive Mode, Charger Charging, Battery SOC [%], Battery Instant Voltage [V], Battery U Track [V], Iso Resist [kOhm] |
| MC42[1] application | Proemion | Proemion Battery Value 2 | émise | Promeion (Generic) | 0x7451224 | Not used | Current Bat [A], DiffCellVoltage [mV] |
| MC42[1] application | Proemion | Proemion Secon Value | émise | Promeion (Generic) | 0x7451225 | Not used | Error 1, Error 2, Error 3 |
| MC42[1] application | Proemion | Iqan Message | émise | Promeion (Generic) | 0x7451226 | Not used | Message |
| MC42[1] application | Proemion | Proemion Device | émise | Promeion (Generic) | 0x7451230 | Not used | MDGN-+BAT:MC2[1] [cV] |
| MC42[1] application | ELEC / BATTERY / BMW | BMW Error | émise | Promeion (Generic) | 0x7451240 | Not used | BatErrorCode Out, DcuErrorCode Out, IsoMonErrorCode Out |
| MC42[1] application | ELEC / MOTORS / M-Tracks / Zapi Right | Promeion ZAPI | émise | Promeion (Generic) | 0x7451250 | Not used | Right Warning, Left Warning |
| MC42[1] application | ELEC / SYNC | SYNC | émise | SYNC (Generic) | 0x80 | 100 |  |

## Liaisons entre applications (APPOUT → APPIN)

- MC42[1] application `Engines Ready output` (← `Engines Ready`) → MD4-10[0] application `CAN Engine Ready`
- MC42[1] application `FAN OUT output` (← `FAN OUT`) → MD4-10[0] application `FAN OUT`
- MC42[1] application `PUMP VAR output` (← `PUMP VAR`) → MD4-10[0] application `PUMP OUT`
- MC42[1] application `Joystick to zero output` (← `Joystick to zero`) → MD4-10[0] application `Joystick to zero`
- MC42[1] application `OK UP/DOWN output` (← `OK UP/DOWN`) → MD4-10[0] application `OK UP/DOWN`
- MC42[1] application `Ladder_Sensor output` (← `Ladder_Sensor`) → MD4-10[0] application `Ladder Sensor`
- MC42[1] application `Water Level output` (← `Water Level [%]`) → MD4-10[0] application `Water Level`
- MC42[1] application `Charger State Finite` (← `Charger State Finite`) → MD4-10[0] application `Charger Charging State`
- MC42[1] application `Remote output` (← `Remote`) → MD4-10[0] application `Remote Status`
- MC42[1] application `Battery DRIVE` (← `Battery DRIVE MODE`) → MD4-10[0] application `Battery Drive Mode`
- MC42[1] application `Flag NoAUX Mode` (← `Battery NoAUX Mode`) → MD4-10[0] application `Flag NoAUX Mode MD4`
- MD4-10[0] application `Need Charge output` (← `Need Charge`) → MC42[1] application `Need Charge Input`
- ? `MDGN-Status:MD3` (← `?`) → MC42[1] application `MD4-10 Status CAN In`
- MD4-10[0] application `Power Down State output` (← `Power Down State`) → MC42[1] application `Power Down Input`
- MD4-10[0] application `Seat Front/Back MAC output` (← `Seat Front/Back MAC`) → MC42[1] application `Seat Front Back Input`
- MD4-10[0] application `Seat UP/DOWN MAC output` (← `Seat UP/DOWN MAC`) → MC42[1] application `Seat UP/DOWN Input`
- MD4-10[0] application `Speed output` (← `Speed`) → MC42[1] application `CAN Speed Input`
- MD4-10[0] application `F4 Free output` (← `F4 Free`) → MC42[1] application `CAN Free`
- MD4-10[0] application `State Up/Down output` (← `State Up/Down [%]`) → MC42[1] application `CAN IN State Up/Down`
- MD4-10[0] application `UP/DOWN Button output` (← `UP/DOWN Button`) → MC42[1] application `UP/DOWN Button Input`
- MD4-10[0] application `Start Button` (← `Start Button`) → MC42[1] application `Start Button MD4`
- MD4-10[0] application `Left Joystick` (← `Math Gauche [%]`) → MC42[1] application `Left Joystick`
- MD4-10[0] application `Right Joystick` (← `Math Droit [%]`) → MC42[1] application `Right Joystick`
- MD4-10[0] application `Send message` (← `Send message`) → MC42[1] application `Send Message`