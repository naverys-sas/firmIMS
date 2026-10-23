# Anomalies détectées automatiquement — v117

Liste brute produite par `tools/anomalies.py`. Chaque point est un **indice**, pas une certitude : voir `anomalies.md` pour la lecture commentée et priorisée.

## Références vers un nom de canal inexistant (lien cassé) (9)

- `Latitude Compute` (MAC, MD3 / BackLight, l.6959) : Operand 2 = `1E-7`
- `Longitude Compute` (MAC, MD3 / BackLight, l.7016) : Operand 2 = `1E-7`
- `Wait_Very_Low_Oil_Level` (IDC, MC42 / Track tension, l.14496) : Operand 1 = `Oil level Analog [%]`
- `Wait_Very_Low_Oil_Level` (IDC, MC42 / Track tension, l.14496) : Operand 2 = `OIL Security`
- `Wait Oil Level` (IDC, MC42 / Track tension, l.14667) : Operand 1 = `Oil level Analog [%]`
- `Engine oil pressure` (MAC, MC42 / Thermic / Engine i/o, l.22630) : Input = `Engine oil pressure EB2 [kPa]`
- `Engine oil pressure` (MAC, MC42 / Thermic / Engine i/o, l.22630) : Input = `Engine oil pressure Ford [kPa]`
- `Engine coolant temp` (MAC, MC42 / Thermic / Engine i/o, l.22826) : Input = `Engine coolant temperature EB2 [°C]`
- `Engine coolant temp` (MAC, MC42 / Thermic / Engine i/o, l.22826) : Input = `Engine coolant temperature Ford [°C]`

## Canaux qui ne servent à rien (lus par aucun canal, écran, log ou réglage) (26)

- `Status:MC42[1]` (MDGN, MC42, l.14769)
- `S/N:MC42[1]` (MDGN, MC42, l.23950)
- `Address:MC42[1]` (MDGN, MC42, l.23961)
- `Temp:MC42[1]` (MDGN, MC42, l.23972)
- `Can Speed` (IP, MC42 / Initialization, l.9743)
- `DM1` (DM1IN, MC42 / Thermic / Engine i/o / EB2, l.20550)
- `DM1` (DM1IN, MC42 / Thermic / Engine i/o / Ford, l.21416)
- `Timer Fan Critical` (FP, MC42 / Thermic / Power, l.16647)
- `oldExhaust Temperature State` (SMC, MC42 / Thermic / Power, l.16675)
- `in Engine coolant temperature` (FGI, MC42 / Thermic / SAEJ Std engine input, l.17667)
- `Activate Critical State` (IDC, MC42 / Thermic / Thermal Management, l.23473)
- `Tension State` (SMC, MC42 / Track tension, l.14284)
- `MDGN-VREF:MD3-0` (MDGN, MD3, l.45)
- `MDGN-+BAT:MD3-0` (MDGN, MD3, l.56)
- `MDGN-Temp:MD3-0` (MDGN, MD3, l.67)
- `VIEW ENGINE RUN PAGE` (IDC, MD3, l.3394)
- `Exhaust temp sensor` (DP, MD3, l.9694)
- `Speed Over Ground Kts` (MAC, MD3 / BackLight, l.6748)
- `Duree` (MAC, MD3 / BackLight, l.8351)
- `Backlight Value Filter` (SFC, MD3 / BackLight, l.8940)
- `Backlight` (DCC, MD3 / BackLight, l.8958)
- `MDGN-Status:MD3[0]` (MDGN, MD3 / Link MD3, l.9611)
- `RadioStartInter` (IDC, MD3 / RADIO, l.4181)
- `MDGN-S/N:MD3[0]` (MDGN, MD3 / RADIO, l.4271)
- `Timer sleep engine to Img` (SMC, MD3 / UP/DOWN, l.2934)
- `Show Debug` (IDC, MD3 / UP/DOWN, l.3291)

## Canaux sans aucune logique (toutes les conditions vides) (8)

- `Stop To Move` (IDC, MD3, l.768)
- `Iguana PIN` (PCC, MD3, l.6287)
- `K8` (IDC, MC42 / KeyBox, l.25364)
- `K9` (IDC, MC42 / KeyBox, l.25400)
- `K10` (IDC, MC42 / KeyBox, l.25436)
- `K11` (IDC, MC42 / KeyBox, l.25472)
- `K12` (IDC, MC42 / KeyBox, l.25508)
- `K13` (IDC, MC42 / KeyBox, l.25544)

## Modes de fonction vides (le canal reste à 0 dans ces modes) (2)

- `IDC Speed S Wait` (IDC, MD3, l.4682) : modes vides ['Radio']
- `IDC Speed R Wait` (IDC, MD3, l.4749) : modes vides ['Radio']

## Messages qui ne peuvent jamais s’afficher (groupe Showing vide) (0)


## Conditions constantes vraies (9)

- `Reset on startup` (IDC, MD3, l.156) groupe Activating
- `Intermediaire` (IDC, MD3 / UP/DOWN, l.2206) groupe Activating
- `Show P-1-2` (IDC, MD3 / UP/DOWN, l.2809) groupe Activating
- `Timeout radio` (TMR, MD3 / RADIO, l.3616) groupe Increasing
- `LatenceTimer` (TMR, MD3 / RADIO, l.3707) groupe Increasing
- `Don'push button` (IDC, MC42 / Track Up/Down, l.13165) groupe Activating
- `Reset Startup` (IDC, MC42 / Track tension, l.13461) groupe Activating
- `Reset Startup` (IDC, MC42 / Thermic / Power, l.14881) groupe Activating
- `Wait after stating` (IDC, MC42 / Proemion, l.26847) groupe Activating

## Conditions constantes fausses (0)


## Noms en double dans un même groupe de fonctions (16)

- MD3 / MD3 : `Re-Track mode in water` ×2
- MD3 / MD3 / UP/DOWN : `Timer UP/DOWN` ×2
- MD3 / MD3 / UP/DOWN : `State Up/Down` ×2
- MD3 / MD3 / UP/DOWN : `Timer sleep engine to Img` ×2
- MD3 / MD3 : `Auto Stop Timer` ×2
- MC42 / MC42 / Track tension : `Tracks pressure Mode` ×2
- MC42 / MC42 / Track tension : `Oil level` ×2
- MC42 / MC42 / Thermic / Power : `Fuel line ignition` ×2
- MC42 / MC42 / Thermic / Pump : `Punp 1 - Current` ×2
- MC42 / MC42 / Thermic / Pump : `Punp 2 - Current` ×2
- MC42 / MC42 / KeyBox : `GFOUT-D:Generic` ×2
- MC42 / MC42 / KeyBox : `GFOUT-E:Generic` ×2
- MC42 / MC42 / KeyBox : `BYTE 0 - HB` ×2
- MC42 / MC42 / KeyBox : `BYTE 1 - HB` ×2
- MC42 / MC42 / KeyBox : `BYTE 2 - HB` ×2
- MC42 / MC42 / KeyBox : `BYTE 4 - HB` ×2

## Boucles de calcul entre canaux combinatoires (1 cycle de retard) (3)

- `Days in current year` → `M` → `C`
- `Reset Startup` → `Reset Startup`
- `MD3 start last checks` → `AutoStopafter 5 secondes`

## Canal qui se lit lui-même (9)

- `Reset on startup` (IDC, MD3, l.156)
- `Adress_Search` (IDC, MD3 / BackLight, l.6522)
- `C` (MAC, MD3 / BackLight, l.7546)
- `Unlock` (IDC, MD3 / PIN, l.9253)
- `Over Tension` (IDC, MC42 / Track tension, l.14045)
- `Pre Fuel line ignition IDC` (IDC, MC42 / Thermic / Power, l.15270)
- `MD3 start last checks` (IDC, MC42 / Thermic / Power, l.15588)
- `Digit Engine On` (IDC, MC42 / Thermic / Power, l.15936)
- `Engine oil pressure` (MAC, MC42 / Thermic / Engine i/o, l.22630)

## Qcode : if sans else (valeur figée si aucune branche) (2)

- `Engine Temp State` (SMC, MC42 / Thermic / Power, l.16795)
- `Speed error` (MAC, MC42 / Thermic / Engine Speed calc, l.19163)

## Qcode : divisions par un canal (risque de division par zéro) (7)

- `Speed error` (MAC, MC42 / Thermic / Engine Speed calc, l.19163) : / `Speed_RPM_needed`
- `Speed Error Calcul` (MAC, MC42 / Thermic / Engine i/o, l.22776) : / `Speed_RPM_needed`
- `Speed Error Calcul` (MAC, MC42 / Thermic / Engine i/o, l.22776) : / `Speed_RPM_needed`
- `ON_Bits` (IMAC, MC42 / KeyBox, l.25580) : / `Fan`
- `ON_Bits` (IMAC, MC42 / KeyBox, l.25580) : / `Pump`
- `ON_Bits` (IMAC, MC42 / KeyBox, l.25580) : / `AutoOff`
- `ON_Bits` (IMAC, MC42 / KeyBox, l.25580) : / `Search Lights`

## Trames CAN reçues sans timeout (perte de communication non détectée) (2)

- `Engine Temperature EB 2` (JFIN, MC42 / Thermic / Engine i/o / EB2, l.21273)
- `Engine Temperature Ford` (JFIN, MC42 / Thermic / Engine i/o / Ford, l.22139)

## Même identifiant CAN émis plusieurs fois sur le même module (1)

- ('KeyBox (Generic)', 'ID Prog') : `GFOUT-D:Generic` (GFOUT, MC42 / KeyBox, l.25817), `GFOUT-E:Generic` (GFOUT, MC42 / KeyBox, l.25937)

## Canaux d’un groupe désactivé lus par de la logique active (0)


## Groupes de fonctions désactivés (0)


## Groupes de fonctions au nom suspect (WIP, broken, soon, test…) (1)

- MC42 : MC42 / Thermic / T.Exhaust temp

## Groupes de fonctions vides (0)


## Canaux au nom suspect (test, debug, sim, old…) (27)

- `MDGN-Temp:MD3-0` (MDGN, MD3, l.67)
- `Debug Mode` (DP, MD3 / UP/DOWN, l.3278)
- `Show Debug` (IDC, MD3 / UP/DOWN, l.3291)
- `Exhaust temp sensor` (DP, MD3, l.9694)
- `Test Locker` (DP, MC42 / Track Up/Down, l.11881)
- `Persistant Water Temp` (MEM, MC42 / Thermic / Power, l.16159)
- `High Temp Timer` (TMR, MC42 / Thermic / Power, l.16261)
- `Mid Temp Timer` (TMR, MC42 / Thermic / Power, l.16336)
- `Low Temp Timer` (TMR, MC42 / Thermic / Power, l.16411)
- `Critical Temp Timer` (TMR, MC42 / Thermic / Power, l.16486)
- `T inExhaust temp` (FGI, MC42 / Thermic / Power, l.16661)
- `Water Temp Hysteresis Gap` (FP, MC42 / Thermic / Power, l.16783)
- `Engine Temp State` (SMC, MC42 / Thermic / Power, l.16795)
- `Exhaust Temp State hy test` (SMC, MC42 / Thermic / Power, l.17054)
- `Oil Temp Mid/High` (FP, MC42 / Thermic / Oil security, l.17404)
- `Oil Temp Low/Mid` (FP, MC42 / Thermic / Oil security, l.17416)
- `Oil Temp Critical` (FP, MC42 / Thermic / Oil security, l.17428)
- `Oil Temp Hysteresis` (FP, MC42 / Thermic / Oil security, l.17440)
- `Engine coolant temp` (MAC, MC42 / Thermic / Engine i/o, l.22826)
- `In Hydraulics Temp State` (FGI, MC42 / Thermic / Thermal Management, l.23094)
- `In Exhaust Temp State` (FGI, MC42 / Thermic / Thermal Management, l.23126)
- `T Exhaust coolant temp mc 52` (VIN, MC42 / Thermic / T.Exhaust temp, l.23882)
- `Temp:MC42[1]` (MDGN, MC42, l.23972)
- `Aft Fan Max Test` (DP, MC42 / KeyBox, l.24881)
- `Aft Fan Low Test` (DP, MC42 / KeyBox, l.24894)
- `Exhaust Fan Test` (DP, MC42 / KeyBox, l.25036)
- `debug temps screen` (DP, MC42, l.27204)

## Réglages de mise au point exposés (debug/force/test/sim) (10)

- Force at 2200 rpm
- Automatic Joystick Inhibition
- Exhaust Fan Test
- Aft Fan Max Test
- Force EV By Pass
- Aft Fan Low Test
- Force Engine pump
- Force Exhaust pump
- Test Locker
- debug temps screen

## Références à un canal d’une autre application (hors APPIN/APPOUT) (0)

