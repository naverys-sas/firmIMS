# Anomalies détectées automatiquement — V35.42 (X100)

Liste brute produite par `tools/anomalies.py`. Chaque point est un **indice**, pas une certitude : voir `anomalies.md` pour la lecture commentée et priorisée.

## Références vers un nom de canal inexistant (lien cassé) (10)

- `Latitude Compute` (MAC, MD3 / BackLight, l.7050) : Operand 2 = `1E-7`
- `Longitude Compute` (MAC, MD3 / BackLight, l.7107) : Operand 2 = `1E-7`
- `Wait_Very_Low_Oil_Level` (IDC, MC42 / Track tension, l.14691) : Operand 1 = `Oil level Analog [%]`
- `Wait_Very_Low_Oil_Level` (IDC, MC42 / Track tension, l.14691) : Operand 2 = `OIL Security`
- `Wait Oil Level` (IDC, MC42 / Track tension, l.14862) : Operand 1 = `Oil level Analog [%]`
- `Memorizing Water Temp` (MEM, MC42 / Thermic / Power, l.16321) : Operand 1 = `Engine coolant temperature [Â°C]`
- `Inter Full Fan` (IDC, MC42 / Thermic / Power, l.16861) : Operand 1 = `Engine coolant temperature [Â°C]`
- `Voyant TÂ° Eau Moteur Warning` (IDC, MC42 / Thermic / SAEJ Std input, l.18403) : Operand 1 = `Engine coolant temperature [Â°C]`
- `Voyant TÂ° Eau Moteur Critical` (IDC, MC42 / Thermic / SAEJ Std input, l.18467) : Operand 1 = `Engine coolant temperature [Â°C]`
- `Voyant Pression Huile Moteur` (IDC, MC42 / Thermic / SAEJ Std input, l.18587) : Operand 1 = `Engine oil pressure [kPa]`

## Canaux qui ne servent à rien (lus par aucun canal, écran, log ou réglage) (63)

- `S/N:MC42[1]` (MDGN, MC42, l.21195)
- `Address:MC42[1]` (MDGN, MC42, l.21206)
- `Temp:MC42[1]` (MDGN, MC42, l.21217)
- `Wait batt ON` (IDC, MC42 / Electric, l.22290)
- `Battery POWER` (MAC, MC42 / Electric / BATTERY, l.28506)
- `Bat - 25A-50A` (IDC, MC42 / Electric / BATTERY, l.28675)
- `Bat - 50A-75A` (IDC, MC42 / Electric / BATTERY, l.28729)
- `Bat - 75A-100A` (IDC, MC42 / Electric / BATTERY, l.28783)
- `Bat - 100A-125A` (IDC, MC42 / Electric / BATTERY, l.28837)
- `Bat - up to 125A` (IDC, MC42 / Electric / BATTERY, l.28891)
- `Bat - 1A-25A` (IDC, MC42 / Electric / BATTERY, l.28936)
- `Error Iso_Resist` (IDC, MC42 / Electric / BATTERY, l.29524)
- `Engines Not Ready` (IDC, MC42 / Electric / MOTORS, l.46601)
- `M3 - ENGINE HOT` (IDC, MC42 / Electric / MOTORS / M-Hydrau, l.45705)
- `M3 - Voltage` (MAC, MC42 / Electric / MOTORS / M-Hydrau, l.45750)
- `M3 - Charge` (MAC, MC42 / Electric / MOTORS / M-Hydrau, l.45835)
- `M3 - Ready` (IDC, MC42 / Electric / MOTORS / M-Hydrau, l.45958)
- `M3 - Error mode` (IDC, MC42 / Electric / MOTORS / M-Hydrau, l.46001)
- `M1 - Ready` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.41704)
- `M1 - Voltage` (IMAC, MC42 / Electric / MOTORS / M-Tracks, l.41778)
- `M1 - Charge` (MAC, MC42 / Electric / MOTORS / M-Tracks, l.42068)
- `M1 - ENGINE HOT` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.42148)
- `M2 - Ready` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.42577)
- `M2 - Voltage` (IMAC, MC42 / Electric / MOTORS / M-Tracks, l.42651)
- `M2 - Charge` (MAC, MC42 / Electric / MOTORS / M-Tracks, l.42941)
- `M2 - ENGINE HOT` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.43021)
- `M1 - Error mode` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.43066)
- `M2 - Error mode` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.43140)
- `M1 - Mechanical power` (MAC, MC42 / Electric / MOTORS / M-Tracks, l.43318)
- `M1 - Torque Tracks` (MAC, MC42 / Electric / MOTORS / M-Tracks, l.43380)
- `M1 - 25A-50A` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.43424)
- `M1 - 50A-75A` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.43478)
- `M1 - 75A-100A` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.43532)
- `M1 - 100A-125A` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.43586)
- `M1 - up to 125A` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.43640)
- `M2 - Mechanical power` (MAC, MC42 / Electric / MOTORS / M-Tracks, l.43789)
- `M2 - Torque tracks` (MAC, MC42 / Electric / MOTORS / M-Tracks, l.43851)
- `M2 - 25A-50A` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.43895)
- `M2 - 50A-75A` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.43949)
- `M2 - 75A-100A` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.44003)
- `M2 - 100A-125A` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.44057)
- `M2 - up to 125A` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.44111)
- `Can Speed` (IP, MC42 / Initialization, l.10044)
- `SÃ©curitÃ© hydraulique` (IDC, MC42 / Thermic / Oil security, l.17328)
- `Etat Engine` (SMC, MC42 / Thermic / Power, l.16710)
- `TEST Full Fan` (MEM, MC42 / Thermic / Power, l.16806)
- `Timer FAN` (MAC, MC42 / Thermic / Power, l.16931)
- `Wait SWITCH ON Engine` (IDC, MC42 / Thermic / Power, l.17030)
- `DM1` (DM1IN, MC42 / Thermic / SEJ ECM, l.17572)
- `OK BLOC` (IDC, MC42 / Track Up/Down, l.13348)
- `Tension State` (SMC, MC42 / Track tension, l.14436)
- `MDGN-VREF:MD3-0` (MDGN, MD3, l.43)
- `MDGN-+BAT:MD3-0` (MDGN, MD3, l.54)
- `MDGN-Temp:MD3-0` (MDGN, MD3, l.65)
- `VIEW ENGINE RUN PAGE` (IDC, MD3, l.3485)
- `Speed Over Ground Kts` (MAC, MD3 / BackLight, l.6839)
- `DurÃ©e` (MAC, MD3 / BackLight, l.8442)
- `Backlight Value Filter` (SFC, MD3 / BackLight, l.9031)
- `Backlight` (DCC, MD3 / BackLight, l.9049)
- `RadioStartInter` (IDC, MD3 / RADIO, l.4272)
- `MDGN-S/N:MD3[0]` (MDGN, MD3 / RADIO, l.4362)
- `Timer sleep engine to Img` (SMC, MD3 / UP/DOWN, l.3025)
- `Show Debug` (IDC, MD3 / UP/DOWN, l.3382)

## Canaux sans aucune logique (toutes les conditions vides) (14)

- `Iguana PIN` (PCC, MD3, l.6378)
- `BMW - ERROR DIGIT` (IDC, MC42 / Electric / BATTERY / BMW, l.25152)
- `Test Mode` (SMC, MC42 / Electric / MOTORS / M-Hydrau / Sevcon, l.44410)
- `M3 - Pump Engine CMSG` (CMSG, MC42 / Electric / MOTORS / M-Hydrau / Sevcon, l.45153)
- `Heatsink` (MAC, MC42 / Electric / MOTORS / M-Hydrau, l.45545)
- `Engine Temps` (MAC, MC42 / Electric / MOTORS / M-Hydrau, l.45670)
- `K6 Aux 1` (IDC, MC42 / KeyBox, l.48658)
- `K7 Aux 2` (IDC, MC42 / KeyBox, l.48694)
- `K8` (IDC, MC42 / KeyBox, l.48730)
- `K9` (IDC, MC42 / KeyBox, l.48766)
- `K10` (IDC, MC42 / KeyBox, l.48802)
- `K11` (IDC, MC42 / KeyBox, l.48838)
- `K12` (IDC, MC42 / KeyBox, l.48874)
- `K13` (IDC, MC42 / KeyBox, l.48910)

## Modes de fonction vides (le canal reste à 0 dans ces modes) (11)

- `Stop To Move` (IDC, MD3, l.820) : modes vides ['Thermique']
- `IDC Speed S Wait` (IDC, MD3, l.4773) : modes vides ['Radio']
- `IDC Speed R Wait` (IDC, MD3, l.4840) : modes vides ['Radio']
- `F4 Off` (IDC, MC42 / Electric, l.21767) : modes vides ['Ready', 'Start', 'Start Free']
- `LowCellVoltage` (MAC, MC42 / Electric / BATTERY, l.29621) : modes vides ['BMW']
- `HighCellVoltage` (MAC, MC42 / Electric / BATTERY, l.29687) : modes vides ['BMW']
- `1560 - Max Current from 230 V` (MAC, MC42 / Electric / CHARGER / Brusa, l.33226) : modes vides ['STOP', 'Clear ERROR']
- `1560 - Desired Voltage` (MAC, MC42 / Electric / CHARGER / Brusa, l.33330) : modes vides ['STOP', 'Clear ERROR']
- `1560 - Desired Current` (MAC, MC42 / Electric / CHARGER / Brusa, l.33434) : modes vides ['STOP', 'Clear ERROR']
- `Func State` (SMC, MC42 / Electric / MOTORS / M-Tracks / ZAPI Right, l.35754) : modes vides ['Preprop']
- `Func State` (SMC, MC42 / Electric / MOTORS / M-Tracks / ZAPI Left, l.38074) : modes vides ['Preprop']

## Messages qui ne peuvent jamais s’afficher (groupe Showing vide) (1)

- `M3 - Pump Engine CMSG` (CMSG, MC42 / Electric / MOTORS / M-Hydrau / Sevcon, l.45153)

## Conditions constantes vraies (15)

- `Reset on startup` (IDC, MD3, l.154) groupe Activating
- `Intermediaire` (IDC, MD3 / UP/DOWN, l.2297) groupe Activating
- `Show P-1-2` (IDC, MD3 / UP/DOWN, l.2900) groupe Activating
- `Timeout radio` (TMR, MD3 / RADIO, l.3707) groupe Increasing
- `LatenceTimer` (TMR, MD3 / RADIO, l.3798) groupe Increasing
- `Don'push button` (IDC, MC42 / Track Up/Down, l.13110) groupe Activating
- `Reset Startup` (IDC, MC42 / Track tension, l.13675) groupe Activating
- `Reset Startup` (IDC, MC42 / Thermic / Power, l.15059) groupe Activating
- `Global Auto Off Timer` (TMR, MC42 / Electric, l.22034) groupe Increasing
- `Start 3 s` (IDC, MC42 / Electric / BATTERY, l.23062) groupe Activating
- `Reset Startup` (IDC, MC42 / Electric / BATTERY, l.23408) groupe Activating
- `M1 - Ready` (IDC, MC42 / Electric / MOTORS / M-Tracks, l.41704) groupe Activating
- `FAN OUT` (IDC, MC42 / Electric / MOTORS / Cooling, l.46199) groupe Activating
- `PUMP VAR` (IDC, MC42 / Electric / MOTORS / Cooling, l.46377) groupe Activating
- `Wait after stating` (IDC, MC42 / Proemion, l.50295) groupe Activating

## Conditions constantes fausses (0)


## Noms en double dans un même groupe de fonctions (46)

- MD3 / MD3 : `Re-Track mode in water` ×2
- MD3 / MD3 / UP/DOWN : `Timer UP/DOWN` ×2
- MD3 / MD3 / UP/DOWN : `State Up/Down` ×2
- MD3 / MD3 / UP/DOWN : `Timer sleep engine to Img` ×2
- MD3 / MD3 : `Auto Stop Timer` ×2
- MD3 / MD3 / Link MD3 : `MDGN-Status:MD3[0]` ×2
- MD3 / MD3 / Link MD3 : `Drive Type` ×2
- MC42 / MC42 / Initialization : `J1939 Speed` ×2
- MC42 / MC42 / Track tension : `Tracks pressure Mode` ×2
- MC42 / MC42 / Track tension : `Oil level` ×2
- MC42 / MC42 / Thermic / Power : `Fuel line ignition` ×2
- MC42 / MC42 / Thermic / SAEJ Std input : `ECC1 Integrating` ×2
- MC42 / MC42 / Thermic / Pump : `Punp 1 - Current` ×2
- MC42 / MC42 / Thermic / Pump : `Punp 2 - Current` ×2
- MC42 / MC42 / Electric / BATTERY : `Battery Protection` ×3
- MC42 / MC42 / Electric / BATTERY / BMW : `DcuNodeState` ×2
- MC42 / MC42 / Electric / BATTERY / BMW : `BatNodeState` ×2
- MC42 / MC42 / Electric / BATTERY / BMW : `IsoMonNodeState` ×2
- MC42 / MC42 / Electric / BATTERY / BMW : `BatState` ×2
- MC42 / MC42 / Electric / BATTERY / BMW : `IsoMonState` ×2
- MC42 / MC42 / Electric / CHARGER / Elcon : `Temperature od charger` ×2
- MC42 / MC42 / Electric / CHARGER / Brusa : `1555 - Power stage temperature - Byte` ×2
- MC42 / MC42 / Electric / MOTORS / M-Tracks / ZAPI Right : `GFIN PDO2_TX` ×2
- MC42 / MC42 / Electric / MOTORS / M-Tracks / ZAPI Right : `Right Warning` ×2
- MC42 / MC42 / Electric / MOTORS / M-Tracks / ZAPI Right : `Stuffing` ×3
- MC42 / MC42 / Electric / MOTORS / M-Tracks / ZAPI Right : `Brake` ×2
- MC42 / MC42 / Electric / MOTORS / M-Tracks / ZAPI Left : `GFIN PDO2_TX` ×2
- MC42 / MC42 / Electric / MOTORS / M-Tracks / ZAPI Left : `Brake` ×2
- MC42 / MC42 / Electric / MOTORS / M-Tracks / ZAPI Left : `Stuffing` ×3
- MC42 / MC42 / Electric / MOTORS / M-Tracks / ZAPI Left : `Reset` ×2
- MC42 / MC42 / Electric / MOTORS / M-Tracks / Sevcon : `Throttle Input Voltage` ×2
- MC42 / MC42 / Electric / MOTORS / M-Tracks / Sevcon : `VARIATOR ON Wait` ×2
- MC42 / MC42 / Electric / MOTORS / M-Tracks / Sevcon : `Fordward Switch` ×2
- MC42 / MC42 / Electric / MOTORS / M-Tracks / Sevcon : `Inch reverse switch` ×2
- MC42 / MC42 / Electric / MOTORS / M-Tracks / Sevcon : `FS1 Switch` ×4
- MC42 / MC42 / Electric / MOTORS / M-Tracks : `Instant current Filter` ×2
- MC42 / MC42 / Electric / MOTORS / M-Tracks : `Couple Moteur` ×2
- MC42 / MC42 / Electric / MOTORS / M-Hydrau / Sevcon : `Status Word` ×4
- MC42 / MC42 / Electric / MOTORS / M-Hydrau / Sevcon : `Torque Demande` ×2
- MC42 / MC42 / Electric / MOTORS / M-Hydrau / Sevcon : `Torque Limit` ×2
- MC42 / MC42 / KeyBox : `GFOUT-D:Generic` ×2
- MC42 / MC42 / KeyBox : `GFOUT-E:Generic` ×2
- MC42 / MC42 / KeyBox : `BYTE 0 - HB` ×2
- MC42 / MC42 / KeyBox : `BYTE 1 - HB` ×2
- MC42 / MC42 / KeyBox : `BYTE 2 - HB` ×2
- MC42 / MC42 / KeyBox : `BYTE 4 - HB` ×2

## Boucles de calcul entre canaux combinatoires (1 cycle de retard) (4)

- `MD3 STOP` → `Reset Startup` → `Reset Startup` → `Reset Startup` → `Year since 2000` → `Days in current year` → `M` → `C` → `Pre Fuel line ignition IDC` → `Fuel line ignition IDC` → `MD3 START` → `Joystick Zero` → `AutoStopafter 5 secondes` → ``
- `ZAPI_M2_Error mode` → `Error Wait` → `Emmergency Stop Left` → `Emmergency Stop Right` → `ZAPI_M1_Error mode` → `Error Wait`
- `Wait during start` → `Main Switch Battery`
- `Keep ON` → `Battery CMD`

## Canal qui se lit lui-même (13)

- `Reset on startup` (IDC, MD3, l.154)
- `Adress_Search` (IDC, MD3 / BackLight, l.6613)
- `C` (MAC, MD3 / BackLight, l.7637)
- `Unlock` (IDC, MD3 / PIN, l.9344)
- `Over Tension` (IDC, MC42 / Track tension, l.14333)
- `Pre Fuel line ignition IDC` (IDC, MC42 / Thermic / Power, l.15448)
- `Digit Engine On` (IDC, MC42 / Thermic / Power, l.16114)
- `Need to Charge Voltage` (IDC, MC42, l.21468)
- `MD4 - Start Button Blocking Neutral` (IDC, MC42 / Electric, l.21673)
- `Keep ON` (IDC, MC42 / Electric, l.22591)
- `Emmergency Stop Right` (IDC, MC42 / Electric / MOTORS / M-Tracks / ZAPI Right, l.34897)
- `Emmergency Stop Left` (IDC, MC42 / Electric / MOTORS / M-Tracks / ZAPI Left, l.37177)
- `Auto Off Confirmed` (IDC, MC42 / Electric, l.47161)

## Qcode : if sans else (valeur figée si aucune branche) (0)


## Qcode : divisions par un canal (risque de division par zéro) (7)

- `Speed` (MAC, MC42 / Thermic / SAEJ Std input, l.18828) : / `Speed_RPM`
- `BMW- Max Current` (MAC, MC42 / Electric / BATTERY / BMW, l.25287) : / `BMW_`
- `HV Current` (MAC, MC42 / Electric / CHARGER, l.30878) : / `Desired Voltage`
- `ON_Bits` (IMAC, MC42 / KeyBox, l.48946) : / `Fan`
- `ON_Bits` (IMAC, MC42 / KeyBox, l.48946) : / `Pump`
- `ON_Bits` (IMAC, MC42 / KeyBox, l.48946) : / `AutoOff`
- `ON_Bits` (IMAC, MC42 / KeyBox, l.48946) : / `Search Lights`

## Trames CAN reçues sans timeout (perte de communication non détectée) (6)

- `Dcu50Error` (GFIN, MC42 / Electric / BATTERY / BMW, l.25047)
- `Bat51Error` (GFIN, MC42 / Electric / BATTERY / BMW, l.25082)
- `Iso52MonError` (GFIN, MC42 / Electric / BATTERY / BMW, l.25117)
- `GFIN PDO2_TX` (GFIN, MC42 / Electric / MOTORS / M-Tracks / ZAPI Right, l.34557)
- `GFIN PDO2_TX` (GFIN, MC42 / Electric / MOTORS / M-Tracks / ZAPI Left, l.36887)
- `GFIN-B:Generic` (GFIN, MC42 / KeyBox, l.49375)

## Même identifiant CAN émis plusieurs fois sur le même module (3)

- ('ZAPI (Generic)', 'PDO1_RX') : `GFOUT - PDO1_RX` (GFOUT, MC42 / Electric / MOTORS / M-Tracks / ZAPI Right, l.35375), `GFOUT - PDO1_RX` (GFOUT, MC42 / Electric / MOTORS / M-Tracks / ZAPI Left, l.37845)
- ('ZAPI (Generic)', '0') : `NMT` (GFOUT, MC42 / Electric / MOTORS / M-Tracks / ZAPI Right, l.35885), `NMT` (GFOUT, MC42 / Electric / MOTORS / M-Tracks / ZAPI Left, l.38216)
- ('KeyBox (Generic)', 'ID Prog') : `GFOUT-D:Generic` (GFOUT, MC42 / KeyBox, l.49183), `GFOUT-E:Generic` (GFOUT, MC42 / KeyBox, l.49303)

## Canaux d’un groupe désactivé lus par de la logique active (0)


## Groupes de fonctions désactivés (0)


## Groupes de fonctions au nom suspect (WIP, broken, soon, test…) (0)


## Groupes de fonctions vides (1)

- MC42 : MC42 / Electric / SYNC

## Canaux au nom suspect (test, debug, sim, old…) (21)

- `MDGN-Temp:MD3-0` (MDGN, MD3, l.65)
- `Debug Mode` (DP, MD3 / UP/DOWN, l.3369)
- `Show Debug` (IDC, MD3 / UP/DOWN, l.3382)
- `Temp cold/hot` (FP, MC42 / Thermic / Power, l.16309)
- `Memorizing Water Temp` (MEM, MC42 / Thermic / Power, l.16321)
- `TEST Full Fan` (MEM, MC42 / Thermic / Power, l.16806)
- `Led Temp Water` (SMC, MC42 / Thermic / SAEJ Std input, l.18939)
- `Temp:MC42[1]` (MDGN, MC42, l.21217)
- `HVLP Pump Test` (DP, MC42 / Electric, l.21741)
- `Battery max temp` (IP, MC42 / Electric / BATTERY, l.22882)
- `Battery HIGHT TEMP` (IDC, MC42 / Electric / BATTERY, l.22967)
- `Battery hight temp` (IP, MC42 / Electric / BATTERY, l.28559)
- `Motor Temp` (GPIN, MC42 / Electric / MOTORS / M-Tracks / ZAPI Right, l.35582)
- `Motor Temp` (GPIN, MC42 / Electric / MOTORS / M-Tracks / ZAPI Left, l.37882)
- `Engine Max Temp` (IP, MC42 / Electric / MOTORS / M-Tracks, l.41272)
- `Controller Fan Temp` (IP, MC42 / Electric / MOTORS / M-Tracks, l.41284)
- `Engine Eco Temp` (IP, MC42 / Electric / MOTORS / M-Tracks, l.41414)
- `Controller Pump Temp` (IP, MC42 / Electric / MOTORS / M-Tracks, l.41426)
- `Test Mode` (SMC, MC42 / Electric / MOTORS / M-Hydrau / Sevcon, l.44410)
- `HVLP Speed Test` (IP, MC42 / Electric / MOTORS / M-Hydrau / Sevcon, l.44443)
- `Full Fan Test` (DP, MC42 / KeyBox, l.50184)

## Réglages de mise au point exposés (debug/force/test/sim) (12)

- Engine - Force Ready
- Power Controler Force
- Charging Force
- Variator Force
- Battery Force
- Force BMW Charge
- Speed Hydro Force
- Automatic Joystick Inhibition
- Force K3
- Full Fan Test
- Force EV By Pass
- Force Bat Reset

## Références à un canal d’une autre application (hors APPIN/APPOUT) (0)

