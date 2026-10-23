# Anomalies détectées automatiquement — v117

Liste brute produite par `tools/anomalies.py`. Chaque point est un **indice**, pas une certitude : voir `anomalies.md` pour la lecture commentée et priorisée.

## Références vers un nom de canal inexistant (lien cassé) (9)

- `Voyant T° Eau Moteur Warning` (IDC, MC2 / SAEJ Std input, l.14519) : Operand 1 = `Engine coolant temperature [°C]`
- `Voyant T° Eau Moteur Critical` (IDC, MC2 / SAEJ Std input, l.14583) : Operand 1 = `Engine coolant temperature [°C]`
- `Voyant Pression Huile Moteur` (IDC, MC2 / SAEJ Std input, l.14695) : Operand 1 = `Engine oil pressure [kPa]`
- `Wait Very Low Oil Level` (IDC, MC2 / Oil Security, l.16318) : Operand 1 = `Oil level Analog [%]`
- `Wait Bad Pressure` (IDC, MC2 / Oil Security, l.16480) : Operand 1 = `Hydraulic pump statut`
- `Wait Oil Level` (IDC, MC2 / Oil Security, l.16640) : Operand 1 = `Oil level Analog [%]`
- `Oil Security Activation` (IDC, MC2 / Engine Fan, l.16889) : Operand 1 = `OIL Security`
- `Need to charge` (IDC, MC2, l.20258) : Operand 1 = `Battery tension [V]`
- `Charge` (IDC, MC2, l.20303) : Operand 1 = `Battery tension [V]`

## Canaux qui ne servent à rien (lus par aucun canal, écran, log ou réglage) (23)

- `MDGN-Address:MC2[1]` (MDGN, MC2, l.15062)
- `MDGN-S/N:MC2[1]` (MDGN, MC2, l.15073)
- `MDGN-Temp:MC2[1]` (MDGN, MC2, l.15084)
- `MDGN-VREF:MC2[1]` (MDGN, MC2, l.15107)
- `FALSE` (IDC, MC2, l.20429)
- `Etat Engine` (SMC, MC2 / Engine Fan, l.18687)
- `Sécurité hydraulique` (IDC, MC2 / Oil Security, l.16531)
- `DM1` (DM1IN, MC2 / SAEJ ECM, l.13680)
- `Malfunction lamp` (MDGN, MC2 / SAEJ ECM, l.14167)
- `Red stop lamp` (MDGN, MC2 / SAEJ ECM, l.14178)
- `Amber warning lamp` (MDGN, MC2 / SAEJ ECM, l.14189)
- `Protect lamp` (MDGN, MC2 / SAEJ ECM, l.14200)
- `TSC1-A:J1939-0` (TSC1, MC2 / Speed Engine, l.20190)
- `MDGN-VREF:MD3-0` (MDGN, MD3, l.38)
- `MDGN-+BAT:MD3-0` (MDGN, MD3, l.49)
- `MDGN-Temp:MD3-0` (MDGN, MD3, l.60)
- `VIEW START PAGE` (IDC, MD3, l.3988)
- `Setup PIN` (PCC, MD3, l.6963)
- `MDGN-S/N:MD3[0]` (MDGN, MD3 / RADIO, l.4870)
- `Show P-1-2` (IDC, MD3 / RUN PAGE, l.3078)
- `Timer sleep engine to Img` (SMC, MD3 / RUN PAGE, l.3203)
- `Show Timer` (IDC, MD3 / START PAGE, l.933)
- `Timer to Img` (SMC, MD3 / START PAGE, l.1020)

## Canaux sans aucune logique (toutes les conditions vides) (3)

- `Security PIN` (PCC, MD3, l.6926)
- `Setup PIN` (PCC, MD3, l.6963)
- `Iguana PIN` (PCC, MD3, l.7000)

## Modes de fonction vides (le canal reste à 0 dans ces modes) (3)

- `IDC Speed S Wait` (IDC, MD3, l.5279) : modes vides ['Radio']
- `IDC Speed R Wait` (IDC, MD3, l.5346) : modes vides ['Radio']
- `PWM Selector` (MAC, MC2 / Track Tension, l.16116) : modes vides ['Blocage']

## Messages qui ne peuvent jamais s’afficher (groupe Showing vide) (0)


## Conditions constantes vraies (11)

- `Reset on startup` (IDC, MD3, l.184) groupe Activating
- `Intermediaire` (IDC, MD3 / RUN PAGE, l.2475) groupe Activating
- `Show P-1-2` (IDC, MD3 / RUN PAGE, l.3078) groupe Activating
- `Reset Startup` (IDC, MD3 / RUN PAGE, l.3488) groupe Activating
- `Timeout radio` (TMR, MD3 / RADIO, l.4204) groupe Increasing
- `LatenceTimer` (TMR, MD3 / RADIO, l.4295) groupe Increasing
- `OK UP/DOWN` (IDC, MC2 / UP/DOWN TRACK, l.12627) groupe Activating
- `Don'push button` (IDC, MC2 / UP/DOWN TRACK, l.13426) groupe Activating
- `Reset Startup` (IDC, MC2 / Track Tension, l.15169) groupe Activating
- `Reset Startup` (IDC, MC2 / Engine Fan, l.16783) groupe Activating
- `TRUE` (IDC, MC2, l.19112) groupe Activating

## Conditions constantes fausses (7)

- `Map bloc - dé tendeur Chenille` (IDC, MC2 / UP/DOWN TRACK, l.12161) groupe Activating
- `Map bloc - dé tendeur Chenille` (IDC, MC2 / UP/DOWN TRACK, l.12161) groupe Activating
- `Map bloc - Blocage/selctor` (IDC, MC2 / UP/DOWN TRACK, l.12502) groupe Activating
- `Map bloc - Déblocage` (IDC, MC2 / UP/DOWN TRACK, l.13162) groupe Activating
- `Map bloc - Déblocage` (IDC, MC2 / UP/DOWN TRACK, l.13162) groupe Activating
- `Map PWM - blocage` (IDC, MC2 / UP/DOWN TRACK, l.13280) groupe Activating
- `Map PWM - blocage` (IDC, MC2 / UP/DOWN TRACK, l.13280) groupe Activating

## Noms en double dans un même groupe de fonctions (15)

- MD3 / MD3 : `Re-Track mode in water` ×2
- MD3 / MD3 / START PAGE : `Timer to Img` ×2
- MD3 / MD3 / RUN PAGE : `Timer UP/DOWN` ×2
- MD3 / MD3 / RUN PAGE : `State Up/Down` ×2
- MD3 / MD3 / RUN PAGE : `Timer sleep engine to Img` ×2
- MD3 / MD3 / RUN PAGE : `UP/DOWN Special mode` ×2
- MD3 / MD3 / RADIO : `Run Engine Statut` ×2
- MD3 / MD3 : `Auto Stop Timer` ×2
- MC2 / MC2 / Translate : `Punp 1 - Current` ×2
- MC2 / MC2 / Translate : `Punp 2 - Current` ×2
- MC2 / MC2 / Translate : `Pump 2 Left` ×2
- MC2 / MC2 / SAEJ Std input : `Hot Water` ×2
- MC2 / MC2 / Track Tension : `Tracks pressure Mode` ×2
- MC2 / MC2 / Oil Security : `Oil level` ×2
- MC2 / MC2 / Engine Fan : `Fuel line ignition` ×2

## Boucles de calcul entre canaux combinatoires (1 cycle de retard) (3)

- `Days in current year` → `M` → `C`
- `Reset Startup` → `Reset Startup`
- `START Engine` → `AutoStopafter 5 secondes`

## Canal qui se lit lui-même (8)

- `Reset on startup` (IDC, MD3, l.184)
- `Reset Startup` (IDC, MD3 / RUN PAGE, l.3488)
- `F1 - Button` (IDC, MD3, l.7037)
- `C` (MAC, MD3 / BLACK LIGHT, l.7433)
- `Over Tension` (IDC, MC2 / Track Tension, l.15691)
- `Pre Fuel line ignition IDC` (IDC, MC2 / Engine Fan, l.17301)
- `START Engine` (IDC, MC2 / Engine Fan, l.17625)
- `Digit Engine On` (IDC, MC2 / Engine Fan, l.17838)

## Qcode : if sans else (valeur figée si aucune branche) (0)


## Qcode : divisions par un canal (risque de division par zéro) (0)


## Trames CAN reçues sans timeout (perte de communication non détectée) (0)


## Même identifiant CAN émis plusieurs fois sur le même module (0)


## Canaux d’un groupe désactivé lus par de la logique active (0)


## Groupes de fonctions désactivés (0)


## Groupes de fonctions au nom suspect (WIP, broken, soon, test…) (0)


## Groupes de fonctions vides (0)


## Canaux au nom suspect (test, debug, sim, old…) (8)

- `MDGN-Temp:MD3-0` (MDGN, MD3, l.60)
- `Led Temp Water` (SMC, MC2 / SAEJ Std input, l.14935)
- `MDGN-Temp:MC2[1]` (MDGN, MC2, l.15084)
- `Temp cold/hot` (FP, MC2 / Engine Fan, l.18064)
- `Memorizing Water Temp` (MEM, MC2 / Engine Fan, l.18090)
- `Stop temp Fan` (IP, MC2 / Engine Fan, l.18470)
- `FAN Plus temp` (FP, MC2 / Engine Fan, l.18758)
- `TEST Full Fan` (MEM, MC2 / Engine Fan, l.18783)

## Réglages de mise au point exposés (debug/force/test/sim) (2)

- Force tension
- Force UNTIGHTEN

## Références à un canal d’une autre application (hors APPIN/APPOUT) (0)

