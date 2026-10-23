# Configuration, variantes et réglages — v117

Les **sélecteurs** sont les paramètres d'état (SP) qui choisissent la fonction active d'un canal : ce sont eux qui rendent le même logiciel compatible avec plusieurs équipements. Toute v2 doit conserver chacun de ces choix (voir `v2/compatibilite.md`).

## Sélecteurs de variante (paramètres réglables)

### Engine type
- Valeurs : 0=EB2 1.2L · 1=FORD 1.5L (défaut EB2 1.2L)
- Défini dans : Thermic / Engine i/o (MC42)
- Réglable via : Single adjust item: Engine type
- Canaux qui changent de logique (28) : `Water °C Critical Critical`, `Water °C Low`, `Water °C High`, `Water °C Critical`, `Para enclench voyant pression huile`, `FS - Start réduction`, `General speed filtering`, `Idle decel filter`, `Malfunction lamp`, `Red stop lamp`, `Amber warning lamp`, `Protect lamp`, `Pump Curent - Low Speed`, `Pump Curent  - Hight Speed`, `Pump Curent - Super Low Speed`, `Pump Max curent`, `IDLE Speed`, `Slow Max  Speed`, `Hight Speed`, `Tension/UpDown Speed`, `Min Speed mode`, `Engine oil pressure`, `torque OR % load at current speed`, `Speed Error Calcul`, `Engine coolant temp`, `Actual engine, % torque`, `Speed CAN`, `Min Speed acc1`

### Ambiante Temperature
- Valeurs : 0=High (défaut High)
- Défini dans : Thermic / Power (MC42)
- Réglable via : Single adjust item: Ambiante Temperature
- Canaux qui changent de logique (4) : `Timer Fan Hot`, `Timer Fan Mild`, `Timer Fan Low`, `Timer Fan Critical`

### GPS Speed factor
- Valeurs : 0=m/s · 1=kts (défaut m/s)
- Défini dans : BackLight (MD3)
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `GPS_Factor`

### Text State
- Valeurs : 0=1 · 1=2 · 2=3 · 3=4 · 4=5 (défaut 1)
- Défini dans : PIN (MD3) · entrée auto : `Counter`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `Text ****`

### CAN Speed
- Valeurs : 0=500 · 1=125 Prog Keybox (défaut 500)
- Défini dans : Initialization (MC42)
- Réglable via : Single adjust item: CAN Speed
- Canaux qui changent de logique (1) : `Can Speed`

### Number of lockers
- Valeurs : 0=One · 1=Two (défaut One)
- Défini dans : Track Up/Down (MC42)
- Réglable via : Single adjust item: Number of lockers
- Canaux qui changent de logique (1) : `Locking Time`

## Menus de réglage (Adjust groups)

### Maintenance
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Tracks pressure Mode`, `Re-Track mode in water`, `Fuel line ignition State`, `OIL Security`

### Setup
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `UP/DOWN Mode`, `Automatic Joystick Inhibition`, `Remote Control`, `Auto Fast After Down`, `Neutral Joystick`, `Locking UP Track`, `Ambiante Temperature`, `Right Joystick`, `Left Joystick`

### Setup PIN
- Visible = Unlock
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Start PIN`, `Number 1`, `Number 2`, `Number 3`, `Number 4`

### None
- Name, English = Setup Speed
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - Name, Français=Réglage vitesse
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Start Slope`, `Stop Slope`, `Backward - direct corrector`, `Forward - direct corrector`

### Backlight
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `MODE`, `Min back light`, `Back light`

### Master Config
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Engine type`, `CAN Speed`, `Timer UP/DOWN`, `Program KeyBox`, `Proemion`, `Number of lockers`

### Master Thermic
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Tension/UpDown Speed`, `IDLE Speed`, `Idle decel filter`, `Slow Max  Speed`, `Min Speed mode`, `Hight Speed`, `FP - Start réduction`, `FP - Incres Speed`, `FP - Decres Speed`, `FP - Max Error`, `FT - Incres Speed`, `FT - Decres Speed`, `FT - Max Error`, `FO - Incres Speed`, `FO - Decres Speed`, `FO - Max Error`, `FS - Start réduction`, `FS - Incres Speed`, `FS - Decres Speed`, `FS - Max Error`, `General speed filtering`, `?Throttle pulse at Start up`, `Max Speed Gap`, `Need Pressure Tempo`, `Tempo Need Min Speed`, `Min Speed acc1`

### Master Cooling
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Timer Fan Mild`, `Timer Fan Hot`, `Timer Fan Low`, `Water °C Low`, `Water °C High`, `Water °C Critical`, `Water °C Critical Critical`, `Oil Temp Mid/High`, `Oil Temp Low/Mid`, `Oil Temp Critical`, `Force Engine pump`, `Force Exhaust pump`, `Exhaust Fan Test`, `Aft Fan Max Test`, `Aft Fan Low Test`

### Master Pump
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Pump Max curent`, `Pump Curent - Super Low Speed`, `Pump Curent - Low Speed`, `Pump Curent  - Hight Speed`, `Min current Right Backward`, `Min current Left Backward`, `Min current Left Fordward`, `Min current Right Fordward`, `Check Pump`

### Master Tracks
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Track pressure [bar]
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Auto Stop Timer`, `Max_diffrential`, `With tension`, `Tension Pressure`, `Time to tension`, `Locking pressure`

### Master Features
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Manual Start Engine`, `ECU Engine on`, `Force at 2200 rpm`, `Force EV By Pass`, `Test Locker`, `debug temps screen`

## Tous les réglages (Adjust items) et le canal qu’ils modifient

| Réglage | Canal | Visible | Actif |
|---|---|---|---|
| CAN Speed | CAN Speed | Yes | Yes |
| Left Joystick | Left Joystick [%] | Yes | Yes |
| Right Joystick | Right Joystick [%] | Yes | Yes |
| Timer UP/DOWN | Timer UP/DOWN [s] | Yes | Yes |
| Remote Control | Remote Control | Yes | Yes |
| UP/DOWN Mode | UP/DOWN Mode | Yes | Yes |
| Re-Track mode in water | Re-Track mode in water | Yes | Yes |
| Auto Fast After Down | Auto Fast After Down | Yes | Yes |
| Neutral Joystick | Neutral Joystick [%] | Yes | Yes |
| Auto Stop Timer | Auto Stop Timer [s] | Yes | Yes |
| Cruise Control | Cruise Control | No | Yes |
| Pump Max curent | Pump Max curent [mA] | Yes | Yes |
| Pump Curent - Super Low Speed | Pump Curent - Super Low Speed [mA] | Yes | Yes |
| Pump Curent - Low Speed | Pump Curent - Low Speed [mA] | Yes | Yes |
| Pump Curent  - Hight Speed | Pump Curent  - Hight Speed [mA] | Yes | Yes |
| Min current Right Backward | Min current Right Backward [mA] | Yes | Yes |
| Min current Left Backward | Min current Left Backward [mA] | Yes | Yes |
| Min current Left Fordward | Min current Left Fordward [mA] | Yes | Yes |
| Min current Right Fordward | Min current Right Fordward [mA] | Yes | Yes |
| Fuel line ignition State | Fuel line ignition State | Yes | Yes |
| ECU Engine on | ECU Engine on | Yes | Yes |
| Force at 2200 rpm | Force at 2200 rpm | Yes | Yes |
| Manual Start Engine | Manual Start Engine | Yes | Yes |
| Tracks pressure Mode | Tracks pressure Mode | Yes | Yes |
| Engine type | Engine type | Yes | Yes |
| With tension | With tension | Yes | Yes |
| Locking UP Track | Locking UP Track | Yes | Yes |
| Start Slope | Start Slope [%/s] | Yes | Yes |
| Stop Slope | Stop Slope [%/s] | Yes | Yes |
| Backward - direct corrector | Backward - direct corrector [%] | Yes | Yes |
| Forward - direct corrector | Forward - direct corrector [%] | Yes | Yes |
| Start PIN | Start PIN | Yes | Yes |
| Number 1 | Number 1 | Start PIN | Yes |
| Number 2 | Number 2 | Start PIN | Yes |
| Number 3 | Number 3 | Start PIN | Yes |
| Number 4 | Number 4 | Start PIN | Yes |
| Max_diffrential | Max_diffrential [%] | Yes | Yes |
| Min back light | Min back light [%] | Yes | Yes |
| MODE | MODE | Yes | Yes |
| Back light | Back light [%] | Yes | Yes |
| Ambiante Temperature | Ambiante Temperature | Yes | Yes |
| Timer Fan Mild | Timer Fan Mild [s] | Yes | Yes |
| Timer Fan Hot | Timer Fan Hot [s] | Yes | Yes |
| Water °C Low | Water °C Low [°C] | Yes | Yes |
| FT - Max Error | FT - Max Error [°C] | Yes | Yes |
| FP - Start réduction | FP - Start réduction [%] | Yes | Yes |
| FP - Incres Speed | FP - Incres Speed [%/s] | Yes | Yes |
| FP - Max Error | FP - Max Error [%] | Yes | Yes |
| FP - Decres Speed | FP - Decres Speed [%/s] | Yes | Yes |
| FT - Incres Speed | FT - Incres Speed [%/s] | Yes | Yes |
| FT - Decres Speed | FT - Decres Speed [%/s] | Yes | Yes |
| Check Pump | Check Pump | Yes | Yes |
| Tension/UpDown Speed | Tension/UpDown Speed [rpm] | Yes | Yes |
| IDLE Speed | IDLE Speed [rpm] | Yes | Yes |
| Slow Max  Speed | Slow Max  Speed [rpm] | Yes | Yes |
| Min Speed mode | Min Speed mode [rpm] | Yes | Yes |
| Hight Speed | Hight Speed [rpm] | Yes | Yes |
| FO - Incres Speed | FO - Incres Speed [%/s] | Yes | Yes |
| FO - Max Error | FO - Max Error [°C] | Yes | Yes |
| FO - Decres Speed | FO - Decres Speed [%/s] | Yes | Yes |
| FS - Start réduction | FS - Start réduction [%] | Yes | Yes |
| FS - Incres Speed | FS - Incres Speed [%/s] | Yes | Yes |
| FS - Decres Speed | FS - Decres Speed [%/s] | Yes | Yes |
| FS - Max Error | FS - Max Error [%] | Yes | Yes |
| Tension Pressure | Tension Pressure [bar] | Yes | Yes |
| Program KeyBox | Program KeyBox | Yes | Yes |
| Automatic Joystick Inhibition | Automatic Joystick Inhibition [s] | Yes | Yes |
| Exhaust Fan Test | Exhaust Fan Test | Yes | Yes |
| None | OIL Security | Yes | Yes |
| Proemion | Proemion | Yes | Yes |
| Number of lockers | Number of lockers | Yes | Yes |
| Time to tension | Time to tension [ms] | Yes | Yes |
| Aft Fan Max Test | Aft Fan Max Test | Yes | Yes |
| Force EV By Pass | Force EV By Pass | Yes | Yes |
| Locking pressure | Locking pressure [bar] | Yes | Yes |
| General speed filtering | General speed filtering [%/s] | Yes | Yes |
| ?Throttle pulse at Start up | ?Throttle pulse at Start up | Yes | Yes |
| Max Speed Gap | Max Speed Gap [%] | Yes | Yes |
| Need Pressure Tempo | Need Pressure Tempo [ms] | Yes | Yes |
| Tempo Need Min Speed | Tempo Need Min Speed [ms] | Yes | Yes |
| Timer Fan Low | Timer Fan Low [s] | Yes | Yes |
| Water °C High | Water °C High [°C] | Yes | Yes |
| Aft Fan Low Test | Aft Fan Low Test | Yes | Yes |
| Water °C Critical | Water °C Critical [°C] | Yes | Yes |
| Oil Temp Mid/High | Oil Temp Mid/High [°C] | Yes | Yes |
| Oil Temp Low/Mid | Oil Temp Low/Mid [°C] | Yes | Yes |
| Oil Temp Critical | Oil Temp Critical [°C] | Yes | Yes |
| Force Engine pump | Force Engine pump | Yes | Yes |
| Force Exhaust pump | Force Exhaust pump | Yes | Yes |
| Idle decel filter | Idle decel filter | Yes | Yes |
| Test Locker | Test Locker | Yes | Yes |
| Min Speed acc1 | Min Speed acc1 [rpm] | Yes | Yes |
| Water °C Critical Critical | Water °C Critical Critical [°C] | Yes | Yes |
| debug temps screen | debug temps screen | Yes | Yes |