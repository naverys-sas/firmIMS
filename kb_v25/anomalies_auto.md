# Anomalies détectées automatiquement — V25.74 (Commuter)

Liste brute produite par `tools/anomalies.py`. Chaque point est un **indice**, pas une certitude : voir `anomalies.md` pour la lecture commentée et priorisée.

## Références vers un nom de canal inexistant (lien cassé) (2)

- `Latitude Compute` (MAC, MD4-10[0] application / NMEA / GPS, l.28289) : Operand 2 = `1E-7`
- `Longitude Compute` (MAC, MD4-10[0] application / NMEA / GPS, l.28346) : Operand 2 = `1E-7`

## Canaux qui ne servent à rien (lus par aucun canal, écran, log ou réglage) (38)

- `MDGN-S/N:MC2[1]` (MDGN, MC42[1] application, l.65870)
- `MDGN-Temp:MC2[1]` (MDGN, MC42[1] application, l.65881)
- `MDGN-Address:MC2[1]` (MDGN, MC42[1] application, l.65892)
- `MDGN-VREF:MC2[1]` (MDGN, MC42[1] application, l.65903)
- `MDGN-VREF:MC2[1]` (MDGN, MC42[1] application, l.68171)
- `2-4g` (IDC, MC42[1] application / Acceleration, l.67422)
- `4-6g` (IDC, MC42[1] application / Acceleration, l.67446)
- `Wait batt ON` (IDC, MC42[1] application / ELEC, l.31342)
- `Battery LOW BAT` (IDC, MC42[1] application / ELEC / BATTERY, l.40624)
- `Error Iso_Resist` (IDC, MC42[1] application / ELEC / BATTERY, l.42025)
- `Valeo - Output current` (MAC, MC42[1] application / ELEC / CHARGER / Valeo, l.46867)
- `Valeo Connected` (IDC, MC42[1] application / ELEC / CHARGER / Valeo, l.46938)
- `Valeo Charging` (IDC, MC42[1] application / ELEC / CHARGER / Valeo, l.46981)
- `Valeo CAN OK` (IDC, MC42[1] application / ELEC / CHARGER / Valeo, l.47017)
- `Valeo Error` (IDC, MC42[1] application / ELEC / CHARGER / Valeo, l.47060)
- `M1 - Mechanical power` (MAC, MC42[1] application / ELEC / MOTORS / M-Tracks, l.56272)
- `M1 - Torque Tracks` (MAC, MC42[1] application / ELEC / MOTORS / M-Tracks, l.56334)
- `M2 - Mechanical power` (MAC, MC42[1] application / ELEC / MOTORS / M-Tracks, l.56743)
- `M2 - Torque tracks` (MAC, MC42[1] application / ELEC / MOTORS / M-Tracks, l.56805)
- `UP/DOWN` (PWM, MC42[1] application / SEAT, l.67647)
- `FRONT BACK` (PWM, MC42[1] application / SEAT, l.67709)
- `Setup PIN` (PCC, MD4-10[0] application, l.5445)
- `Status:G1x` (MDGN, MD4-10[0] application, l.20650)
- `Network state:G1x` (MDGN, MD4-10[0] application, l.20661)
- `S/N:MD4-10[0]` (MDGN, MD4-10[0] application, l.21929)
- `Temp:MD4-10[0]` (MDGN, MD4-10[0] application, l.21940)
- `Address:MD4-10[0]` (MDGN, MD4-10[0] application, l.21951)
- `VREF:MD4-10[0]` (MDGN, MD4-10[0] application, l.21973)
- `SMC Wipper` (SMC, MD4-10[0] application / EQUIPEMENT, l.10733)
- `A/CBatPackSmoothVoltage` (SFC, MD4-10[0] application / EQUIPEMENT / A/C Aentron BatPack / BatPackSync, l.17205)
- `Aux 5 - if A/C Show` (IDC, MD4-10[0] application / EQUIPEMENT / Options / Single Button Eqt Additional Options, l.11724)
- `Aux 5 - if A/C Need HT` (IDC, MD4-10[0] application / EQUIPEMENT / Options / Single Button Eqt Additional Options, l.11774)
- `DurÃ©e` (MAC, MD4-10[0] application / NMEA / GPS, l.29681)
- `MÃ©ridian` (MAC, MD4-10[0] application / NMEA / GPS, l.30423)
- `Backlight Value Filter` (SFC, MD4-10[0] application / NMEA / GPS, l.30626)
- `Engine RUN - NMEA` (IDC, MD4-10[0] application / NMEA / OutBoard, l.25688)
- `Cox - Show` (IDC, MD4-10[0] application / NMEA / OutBoard, l.27610)
- `RadioMode` (IDC, MD4-10[0] application / iPhone, l.4470)

## Canaux sans aucune logique (toutes les conditions vides) (7)

- `Setup PIN` (PCC, MD4-10[0] application, l.5445)
- `Iguana PIN` (PCC, MD4-10[0] application, l.5482)
- `BMW - ERROR DIGIT` (IDC, MC42[1] application / ELEC / BATTERY / BMW, l.34161)
- `Valeo - Output current` (MAC, MC42[1] application / ELEC / CHARGER / Valeo, l.46867)
- `Valeo Ready` (IDC, MC42[1] application / ELEC / CHARGER / Valeo, l.46902)
- `Valeo Charging` (IDC, MC42[1] application / ELEC / CHARGER / Valeo, l.46981)
- `Valeo Error` (IDC, MC42[1] application / ELEC / CHARGER / Valeo, l.47060)

## Modes de fonction vides (le canal reste à 0 dans ces modes) (13)

- `IDC Speed S Wait` (IDC, MD4-10[0] application, l.988) : modes vides ['Radio']
- `IDC Speed R Wait` (IDC, MD4-10[0] application, l.1055) : modes vides ['Radio']
- `A/C WatchDog` (IDC, MD4-10[0] application / EQUIPEMENT / A/C Aentron BatPack, l.14514) : modes vides ['Off']
- `Adress Loose` (IDC, MD4-10[0] application / NMEA / OutBoard, l.23913) : modes vides ['COX']
- `Auto Light ON` (IDC, MD4-10[0] application / NMEA / GPS, l.30485) : modes vides ['Starting', 'Manual', 'Charging', 'Force Manual']
- `LowCellVoltage` (MAC, MC42[1] application / ELEC / BATTERY, l.42122) : modes vides ['BMW']
- `HighCellVoltage` (MAC, MC42[1] application / ELEC / BATTERY, l.42219) : modes vides ['BMW']
- `1560 - Max Current from 230 V` (MAC, MC42[1] application / ELEC / CHARGER / Brusa, l.44315) : modes vides ['STOP', 'Clear ERROR']
- `1560 - Desired Voltage` (MAC, MC42[1] application / ELEC / CHARGER / Brusa, l.44419) : modes vides ['STOP', 'Clear ERROR']
- `1560 - Desired Current` (MAC, MC42[1] application / ELEC / CHARGER / Brusa, l.44523) : modes vides ['STOP', 'Clear ERROR']
- `Charger Output Current` (MAC, MC42[1] application / ELEC / CHARGER, l.45863) : modes vides ['Valeo']
- `Func State` (SMC, MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Right, l.51046) : modes vides ['Preprop']
- `Func State` (SMC, MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Left, l.53289) : modes vides ['Preprop']

## Messages qui ne peuvent jamais s’afficher (groupe Showing vide) (0)


## Conditions constantes vraies (13)

- `Reset on startup` (IDC, MD4-10[0] application, l.1862) groupe Activating
- `Timeout radio` (TMR, MD4-10[0] application / iPhone, l.3995) groupe Increasing
- `LatenceTimer` (TMR, MD4-10[0] application / iPhone, l.4086) groupe Increasing
- `Engine 1 - Show` (IDC, MD4-10[0] application / NMEA / OutBoard, l.25288) groupe Activating
- `Wait 20 secondes` (IDC, MD4-10[0] application / NMEA / GPS, l.30049) groupe Activating
- `Start 3 s` (IDC, MC42[1] application / ELEC / BATTERY, l.32031) groupe Activating
- `Reset Startup` (IDC, MC42[1] application / ELEC / BATTERY, l.32416) groupe Activating
- `FAN OUT` (IDC, MC42[1] application / ELEC / MOTORS / Cooling, l.59171) groupe Activating
- `PUMP VAR` (IDC, MC42[1] application / ELEC / MOTORS / Cooling, l.59349) groupe Activating
- `Reset Startup` (IDC, MC42[1] application / UP/DOWN, l.62909) groupe Activating
- `Don'push button` (IDC, MC42[1] application / UP/DOWN, l.63958) groupe Activating
- `Reset Startup` (IDC, MC42[1] application / Track Tension, l.64367) groupe Activating
- `Wait after starting` (IDC, MC42[1] application / Proemion, l.68376) groupe Activating

## Conditions constantes fausses (2)

- `Flag Ground Fault Detection` (IDC, MC42[1] application / ELEC / BATTERY, l.42773) groupe Activating
- `Flag Ground Fault Detection` (IDC, MC42[1] application / ELEC / BATTERY, l.42773) groupe Activating

## Noms en double dans un même groupe de fonctions (111)

- MD4-10[0] application / MD4-10[0] application : `Start Button` ×2
- MD4-10[0] application / MD4-10[0] application : `Left Joystick` ×2
- MD4-10[0] application / MD4-10[0] application : `Right Joystick` ×2
- MD4-10[0] application / MD4-10[0] application : `Auto Stop Timer` ×2
- MD4-10[0] application / MD4-10[0] application / Link MD4 : `MDGN-Status:MD3[0]` ×2
- MD4-10[0] application / MD4-10[0] application / Link MD4 : `Send message` ×2
- MD4-10[0] application / MD4-10[0] application / UP/DOWN : `Timer UP/DOWN` ×2
- MD4-10[0] application / MD4-10[0] application / BUZZER : `Wait Buz 2` ×3
- MD4-10[0] application / MD4-10[0] application / EQUIPEMENT : `HT UP` ×2
- MD4-10[0] application / MD4-10[0] application / EQUIPEMENT : `HT DOWN` ×2
- MD4-10[0] application / MD4-10[0] application / EQUIPEMENT : `Byte 0` ×3
- MD4-10[0] application / MD4-10[0] application / EQUIPEMENT : `Byte 1` ×3
- MD4-10[0] application / MD4-10[0] application / PROGRAM KEYBOX : `BYTE 0 - New ID` ×2
- MD4-10[0] application / MD4-10[0] application / PROGRAM KEYBOX : `BYTE 1 - New ID` ×2
- MD4-10[0] application / MD4-10[0] application / PROGRAM KEYBOX : `BYTE 2 - New ID` ×2
- MD4-10[0] application / MD4-10[0] application / PROGRAM KEYBOX : `BYTE 4 - New ID` ×2
- MD4-10[0] application / MD4-10[0] application / PROGRAM KEYBOX : `Confirmation` ×2
- MD4-10[0] application / MD4-10[0] application / PROGRAM KEYBOX : `Confirmation Ok` ×2
- MD4-10[0] application / MD4-10[0] application / NMEA / OutBoard : `Engine 1 - Tank` ×2
- MD4-10[0] application / MD4-10[0] application / NMEA / OutBoard : `Engine 2 - Tank` ×2
- MD4-10[0] application / MD4-10[0] application / NMEA / OutBoard : `Alternator potential` ×2
- MD4-10[0] application / MD4-10[0] application / NMEA / OutBoard : `Fuel rate` ×2
- MD4-10[0] application / MD4-10[0] application / NMEA / OutBoard : `Sequence` ×2
- MD4-10[0] application / MD4-10[0] application / NMEA / OutBoard : `Page` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY : `Battery Protection` ×3
- MC42[1] application / MC42[1] application / ELEC / BATTERY / BMW : `DcuNodeState` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / BMW : `BatNodeState` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / BMW : `IsoMonNodeState` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / BMW : `BatState` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / BMW : `IsoMonState` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / Kreisel : `BMS_ext_Temp_Inlet` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / Kreisel : `BMS_ext_Temp_Outlet` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / Kreisel : `VER_CSC_release` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / Kreisel : `VER_MC_release` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / Kreisel : `VER_CSC_minor` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / Kreisel : `VER_CSC_major` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / Kreisel : `VER_MC_minor` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / Kreisel : `VER_MC_major` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / Kreisel : `VER_MC_DS_CRC` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `BMS_VMU_FAULTS` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `Coin Low voltage` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `OilLevel` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `OpenCircuit` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `WrongConfiguration` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `CanCurrentSensorFailure` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `InsulationControlerFailure` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `MainPrechargeSequenceFailure` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `HeatingSystemFailure` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `CoolingSystemFailure` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `Fan Failure` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `OilPump Failure` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `VMU Timeout` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `InsulationMeasurementState` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `InternalCurrentSensorFailure` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `VoltSensorFailure` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `TempSensorFailure` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `ModuleLost` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `InterlockOpened` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `ContactorDamaged` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `AUX2Contactor` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `AUX1Contactor` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `DCContactorMinus` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `DCContactorPlus` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `MainContactorPrecharge` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `MainContactorMinus` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `MainContactorPlus` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `ShutOverVolt` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `AlarmOverVolt` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `WarnOverVolt` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `ShutCriticalDischarge` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `AlarmCriticalDischarge` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `WarnCriticalDischarge` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `ShutOverCurrentDisharge` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `AlarmOverCurrentDisharge` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `WarnOverCurrentDisharge` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `ShutOverCurrentCharge` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `AlarmOverCurrentCharge` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `WarnOverCurrentCharge` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `ShutOverTemp` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `AlarmOverTemp` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `WarnOverTemp` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `ShutLowTemp` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `AlarmLowTemp` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `WarnLowTemp` ×2
- MC42[1] application / MC42[1] application / ELEC / BATTERY / WattAlps : `WattAlps Debug` ×2
- MC42[1] application / MC42[1] application / ELEC / CHARGER / Brusa : `1555 - Power stage temperature - Byte` ×2
- MC42[1] application / MC42[1] application / ELEC / CHARGER / Elcon : `Temperature od charger` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks / Sevcon : `Throttle Input Voltage` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks / Sevcon : `VARIATOR ON Wait` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks / Sevcon : `Fordward Switch` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks / Sevcon : `Inch reverse switch` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks / Sevcon : `FS1 Switch` ×4
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Right : `GFIN PDO2_TX` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Right : `Right Warning` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Right : `Stuffing` ×3
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Right : `Brake` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Left : `GFIN PDO2_TX` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Left : `Brake` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Left : `Stuffing` ×3
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Left : `Reset` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks : `Instant current Filter` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Tracks : `Couple Moteur` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Hydrau / Sevcon : `Speed` ×2
- MC42[1] application / MC42[1] application / ELEC / MOTORS / M-Hydrau / Sevcon : `Status Word` ×3
- MC42[1] application / MC42[1] application / ELEC / Oil Security : `Oil level` ×2
- MC42[1] application / MC42[1] application / ELEC : `Var Power` ×2
- MC42[1] application / MC42[1] application / Track Tension : `Tracks pressure Mode` ×2
- MC42[1] application / MC42[1] application : `MDGN-VREF:MC2[1]` ×2
- MC42[1] application / MC42[1] application / Equipement : `Ladder_Sensor` ×2
- MC42[1] application / MC42[1] application / Equipement : `Bilge Pump Run` ×2
- MC42[1] application / MC42[1] application / Proemion : `MDGN-+BAT:MC2[1]` ×2

## Boucles de calcul entre canaux combinatoires (1 cycle de retard) (11)

- `Days in current year` → `M` → `C`
- `LD UP Toogle` → `Stop Ladder` → `LD Down Toogle`
- `KBB K4 IDC- LD DOWN` → `KBB K3 IDC - LD UP`
- `ZAPI_M1_Error mode` → `Error Wait` → `ZAPI_M2_Error mode` → `Error Wait` → `Emmergency Stop Left` → `Emmergency Stop Right`
- `Flag End of tensionning` → `Need Pressure` → `Super Ok tension`
- `Reset Startup` → `Reset Startup` → `Reset Startup`
- `Wait during start` → `Main Switch Battery`
- `Ladder is not up - Buzz 2` → `Wait Buz 2`
- `Adress_Search` → `Adress_Search`
- `A/C Reboot Request` → `A/C WatchDog`
- `KBB K1 IDC - HT - UP` → `KBB K2 IDC - HT -DOWN`

## Canal qui se lit lui-même (15)

- `Reset on startup` (IDC, MD4-10[0] application, l.1862)
- `LD UP Toogle` (IDC, MD4-10[0] application / EQUIPEMENT, l.7613)
- `LD Down Toogle` (IDC, MD4-10[0] application / EQUIPEMENT, l.7832)
- `HT UP Toogle` (IDC, MD4-10[0] application / EQUIPEMENT, l.8393)
- `HT Down Toogle` (IDC, MD4-10[0] application / EQUIPEMENT, l.8512)
- `Unlock Boat` (IDC, MD4-10[0] application / EQUIPEMENT, l.10841)
- `PIN Pad Show` (IDC, MD4-10[0] application / SCREEN / PIN Pad, l.23487)
- `Continue` (IDC, MD4-10[0] application / SCREEN, l.23655)
- `C` (MAC, MD4-10[0] application / NMEA / GPS, l.28876)
- `Need to Charge Voltage` (IDC, MC42[1] application, l.30934)
- `MD4 - Start Button Blocking Neutral` (IDC, MC42[1] application / ELEC, l.31159)
- `Emmergency Stop Right` (IDC, MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Right, l.50132)
- `Emmergency Stop Left` (IDC, MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Left, l.52385)
- `Oscilator` (IDC, MC42[1] application / UP/DOWN, l.63047)
- `Over Tension` (IDC, MC42[1] application / Track Tension, l.64831)

## Qcode : if sans else (valeur figée si aucune branche) (0)


## Qcode : divisions par un canal (risque de division par zéro) (6)

- `ON_Bits` (IMAC, MD4-10[0] application / EQUIPEMENT / KTB Frame 2d Gen KB, l.19796) : / `AUX 4`
- `ON_Bits` (IMAC, MD4-10[0] application / EQUIPEMENT / KTB Frame 2d Gen KB, l.19796) : / `AUX 5`
- `ON_Bits` (IMAC, MD4-10[0] application / EQUIPEMENT / KTC Frame 2d Gen KB, l.20280) : / `Off`
- `Fuel Economy` (MAC, MD4-10[0] application / NMEA / OutBoard, l.27052) : / `Speed Over Ground Kts`
- `BMW- Max Current` (MAC, MC42[1] application / ELEC / BATTERY / BMW, l.34296) : / `BMW_`
- `HV Current` (MAC, MC42[1] application / ELEC / CHARGER, l.43881) : / `Desired Voltage`

## Trames CAN reçues sans timeout (perte de communication non détectée) (11)

- `GFIN-A:N1_Tx_Status` (GFIN, MD4-10[0] application / EQUIPEMENT / A/C Aentron BatPack / BatPackSync, l.15743)
- `GFIN-B:N2_Tx_Status` (GFIN, MD4-10[0] application / EQUIPEMENT / A/C Aentron BatPack / BatPackSync, l.15864)
- `GFIN-C:N1_Tx_Info` (GFIN, MD4-10[0] application / EQUIPEMENT / A/C Aentron BatPack / BatPackSync, l.16342)
- `GFIN-D:N2_Tx_Info` (GFIN, MD4-10[0] application / EQUIPEMENT / A/C Aentron BatPack / BatPackSync, l.16476)
- `GFIN-E:N1_Tx_Amp` (GFIN, MD4-10[0] application / EQUIPEMENT / A/C Aentron BatPack / BatPackSync, l.16918)
- `GFIN-F:N2_Tx_Amp` (GFIN, MD4-10[0] application / EQUIPEMENT / A/C Aentron BatPack / BatPackSync, l.16993)
- `Dcu50Error` (GFIN, MC42[1] application / ELEC / BATTERY / BMW, l.34056)
- `Bat51Error` (GFIN, MC42[1] application / ELEC / BATTERY / BMW, l.34091)
- `Iso52MonError` (GFIN, MC42[1] application / ELEC / BATTERY / BMW, l.34126)
- `GFIN PDO2_TX` (GFIN, MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Right, l.49842)
- `GFIN PDO2_TX` (GFIN, MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Left, l.52095)

## Même identifiant CAN émis plusieurs fois sur le même module (5)

- ('KEYBOX EQUIPEMENT (Generic)', '0') : `GFOUT-D:Generic` (GFOUT, MD4-10[0] application / EQUIPEMENT, l.9377), `GFOUT-E:Generic` (GFOUT, MD4-10[0] application / EQUIPEMENT, l.9421), `GFOUT-F:Generic` (GFOUT, MD4-10[0] application / EQUIPEMENT, l.10711), `GFOUT-I:Generic` (GFOUT, MD4-10[0] application / PROGRAM KEYBOX, l.21633)
- ('KEYBOX EQUIPEMENT (Generic)', '0x217') : `GFOUT-E:Generic` (GFOUT, MD4-10[0] application / EQUIPEMENT / KTB Frame 1st Gen KB, l.18626), `GFOUT-E:Generic` (GFOUT, MD4-10[0] application / EQUIPEMENT / KTB Frame 2d Gen KB, l.19856)
- ('KEYBOX EQUIPEMENT (Generic)', '0x218') : `GFOUT-E:Generic` (GFOUT, MD4-10[0] application / EQUIPEMENT / KBB Frame 1st Gen KB, l.19240), `GFOUT-E:Generic` (GFOUT, MD4-10[0] application / EQUIPEMENT / KBB Frame 2d Gen KB, l.20098)
- ('KEYBOX EQUIPEMENT (Generic)', '0x219') : `GFOUT-E:Generic` (GFOUT, MD4-10[0] application / EQUIPEMENT / KTC Frame 1st Gen KB, l.19584), `GFOUT-E:Generic` (GFOUT, MD4-10[0] application / EQUIPEMENT / KTC Frame 2d Gen KB, l.20340)
- ('KEYBOX EQUIPEMENT (Generic)', 'ID') : `GFOUT-H:Generic` (GFOUT, MD4-10[0] application / PROGRAM KEYBOX, l.21419), `GFOUT-J:Generic` (GFOUT, MD4-10[0] application / PROGRAM KEYBOX, l.21899)

## Canaux d’un groupe désactivé lus par de la logique active (0)


## Groupes de fonctions désactivés (0)


## Groupes de fonctions au nom suspect (WIP, broken, soon, test…) (0)


## Groupes de fonctions vides (1)

- MD4-10[0] application : MD4-10[0] application / Initialization

## Canaux au nom suspect (test, debug, sim, old…) (31)

- `A/CBatPack Temp` (MAC, MD4-10[0] application / EQUIPEMENT / A/C Aentron BatPack / BatPackSync, l.16629)
- `Temp:MD4-10[0]` (MDGN, MD4-10[0] application, l.21940)
- `Engine temp. Byte 0` (GPIN, MD4-10[0] application / NMEA / OutBoard, l.26012)
- `Engine temp. Byte 1` (GPIN, MD4-10[0] application / NMEA / OutBoard, l.26059)
- `Engine temp` (MAC, MD4-10[0] application / NMEA / OutBoard, l.26071)
- `Engine temp - 1` (MEM, MD4-10[0] application / NMEA / OutBoard, l.26509)
- `Engine temp - 2` (MEM, MD4-10[0] application / NMEA / OutBoard, l.26914)
- `Engine oil temp.` (GPIN, MD4-10[0] application / NMEA / OutBoard, l.27573)
- `HVLP Pump Test` (DP, MC42[1] application / ELEC, l.31227)
- `Battery max temp` (IP, MC42[1] application / ELEC / BATTERY, l.31813)
- `Battery HIGHT TEMP` (IDC, MC42[1] application / ELEC / BATTERY, l.31929)
- `WattAlps Debug` (DP, MC42[1] application / ELEC / BATTERY / WattAlps, l.40238)
- `WattAlps Debug` (GPOUT, MC42[1] application / ELEC / BATTERY / WattAlps, l.40251)
- `Battery hight temp` (IP, MC42[1] application / ELEC / BATTERY, l.40916)
- `Motor Temp` (GPIN, MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Right, l.50874)
- `Motor Temp` (GPIN, MC42[1] application / ELEC / MOTORS / M-Tracks / Zapi Left, l.53097)
- `Engine Max Temp` (IP, MC42[1] application / ELEC / MOTORS / M-Tracks, l.54226)
- `M-Tracks Controller Fan Temp` (IP, MC42[1] application / ELEC / MOTORS / M-Tracks, l.54238)
- `Engine Eco Temp` (IP, MC42[1] application / ELEC / MOTORS / M-Tracks, l.54368)
- `M-Tracks Controller Pump Temp` (IP, MC42[1] application / ELEC / MOTORS / M-Tracks, l.54380)
- `Test Mode` (SMC, MC42[1] application / ELEC / MOTORS / M-Hydrau / Sevcon, l.57332)
- `HVLP Speed Test` (IP, MC42[1] application / ELEC / MOTORS / M-Hydrau / Sevcon, l.57372)
- `Sevcon - Engine Temp` (GPIN, MC42[1] application / ELEC / MOTORS / M-Hydrau / Sevcon, l.57558)
- `M-Hydrau Controller Fan Temp` (IP, MC42[1] application / ELEC / MOTORS / M-Hydrau, l.58521)
- `M-Hydrau Controller Pump Temp` (IP, MC42[1] application / ELEC / MOTORS / M-Hydrau, l.58578)
- `Test Mode Locking State` (SP, MC42[1] application / UP/DOWN, l.62897)
- `Test Mode Locking` (MEM, MC42[1] application / UP/DOWN, l.62959)
- `Test Mode On` (IDC, MC42[1] application / UP/DOWN, l.63002)
- `Bloc Test` (IDC, MC42[1] application / UP/DOWN, l.63097)
- `UnBlock Test` (IDC, MC42[1] application / UP/DOWN, l.63851)
- `MDGN-Temp:MC2[1]` (MDGN, MC42[1] application, l.65881)

## Réglages de mise au point exposés (debug/force/test/sim) (13)

- Variator Force
- Battery Force
- Automatic Joystick Inhibition
- HVLP Pump Test
- Test Mode Locking
- Charging Force
- Engine - Force
- Power Controler Force
- Battery Power Force
- WattAlps Debug
- Force BMW Charge
- A/C Mute Watchdog
- Force unbrake

## Références à un canal d’une autre application (hors APPIN/APPOUT) (0)

