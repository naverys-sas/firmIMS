# Configuration, variantes et réglages — v117

Les **sélecteurs** sont les paramètres d'état (SP) qui choisissent la fonction active d'un canal : ce sont eux qui rendent le même logiciel compatible avec plusieurs équipements. Toute v2 doit conserver chacun de ces choix (voir `v2/compatibilite.md`).

## Sélecteurs de variante (paramètres réglables)

### Engine type
- Valeurs : 0=VW 2.0L · 1=FORD 1.5L (défaut VW 2.0L)
- Défini dans : Speed Engine (MC2)
- Réglable via : Single adjust item: Engine type
- Canaux qui changent de logique (13) : `Max curent`, `Forward Curent - Low Speed`, `Forward Curent  - Hight Speed`, `Forward Curent - Super Low Speed`, `Backward Curent - Low Speed`, `Backward Curent  - Hight Speed`, `Backward Curent - Super Low Speed`, `IDLE Speed`, `Value Slow Speed`, `Value Hight Speed`, `UP/DOWN Speed`, `Min Speed`, `Tension Speed`

### Hydraulic Bloc
- Valeurs : 0=V01 · 1=V01 - Locking · 2=V17 - Locking (défaut V01)
- Défini dans : UP/DOWN TRACK (MC2)
- Réglable via : Single adjust item: Hydraulic Bloc
- Canaux qui changent de logique (7) : `Map bloc - dé tendeur Chenille`, `Map bloc - tendeur Chenille`, `Map bloc - Blocage/selctor`, `OK UP/DOWN`, `Inter EV By Pass`, `Map bloc - Déblocage`, `Map PWM - blocage`

### Ambiante Temperature
- Valeurs : 0=Normal · 1=High (défaut Normal)
- Défini dans : Engine Fan (MC2)
- Réglable via : Single adjust item: Ambiante Temperature
- Canaux qui changent de logique (2) : `Timer Fan Engine cold`, `Timer Fan Engine Hot`

## Menus de réglage (Adjust groups)

### Maintenance
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Tracks pressure Mode`, `Full Fan Mode`, `Re-Track mode in water`, `Fuel line ignition`

### Setup
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `UP/DOWN Mode`, `Ambiante Temperature`, `Remote Control`, `Locking Up Track`, `G11 Modem`, `Auto Beach After Down`, `Neutral Joystick`, `Cruise Control`

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
- Contenu : `Forward`, `Backward`

### Backlight
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `MODE`, `Fuseau`, `Latitude (+ = North)`, `Longitude (+ = East)`, `Min black light`

### Security
- Visible = Yes
- PIN code = Security PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `OIL Security`

### Master Config
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Engine type`, `Hydraulic Bloc`, `Acceleration`

### Master Setup
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Timer UP/DOWN`, `Slope Fast - Low`, `Fan Mode`, `FAN Plus temp`, `Temp cold/hot`, `FP - Start réduction`, `FP - Incres Speed`, `FP - Decres Speed`, `FP - Max Error`, `FT - Start réduction`, `FT - Incres Speed`, `FT - Decres Speed`, `FT - Max Error`, `2200 tr/min`, `ECU Engine`, `Force tension`, `UP/DOWN Special mode`, `Force UNTIGHTEN`

### Master Engine
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `IDLE Speed`, `Min Speed`, `Value Slow Speed`, `Value Hight Speed`, `UP/DOWN Speed`, `Tension Speed`

### Master Pump
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Max curent`, `Forward Curent - Super Low Speed`, `Forward Curent - Low Speed`, `Forward Curent  - Hight Speed`, `Backward Curent - Super Low Speed`, `Backward Curent - Low Speed`, `Backward Curent  - Hight Speed`, `Stop Slope - Pump`, `Start Slope - Pump`, `Right Joystick`, `Left Joystick`, `Min current Right Fordward`, `Min current Right Backward`, `Min current Left Fordward`, `Min current Left Backward`

### Master Tracks
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Auto Stop Timer`, `Max_diffrential`, `Tension Pressure`, `Tension Error Parameter`, `PWM Max mA`, `Parking`

## Tous les réglages (Adjust items) et le canal qu’ils modifient

| Réglage | Canal | Visible | Actif |
|---|---|---|---|
| Left Joystick | Left Joystick [%] | Yes | Yes |
| Right Joystick | Right Joystick [%] | Yes | Yes |
| Min current Right Backward | Min current Right Backward [mA] | Yes | Yes |
| Slope Fast - Low | Slope Fast - Low [mA/s] | Yes | Yes |
| Min current Left Backward | Min current Left Backward [mA] | Yes | Yes |
| Min current Right Fordward | Min current Right Fordward [mA] | Yes | Yes |
| Min current Left Fordward | Min current Left Fordward [mA] | Yes | Yes |
| Timer UP/DOWN | Timer UP/DOWN [s] | Yes | Yes |
| Remote Control | Remote Control | Yes | Yes |
| None | Backward - direct corrector [%] | Yes | Yes |
| None | Forward - direct corrector [%] | Yes | Yes |
| Max curent | Max curent [mA] | Yes | Yes |
| FAN Plus temp | FAN Plus temp [°C] | Yes | Yes |
| Temp cold/hot | Temp cold/hot [°C] | Yes | Yes |
| Ambiante Temperature | Ambiante Temperature | Yes | Yes |
| None | TEST Full Fan | Yes | Engine START |
| None | OIL Security | Yes | Yes |
| FP - Start réduction | FP - Start réduction [%] | Yes | Yes |
| FP - Incres Speed | FP - Incres Speed [%/s] | Yes | Yes |
| FP - Max Error | FP - Max Error [%] | Yes | Yes |
| FT - Start réduction | FT - Start réduction [°C] | Yes | Yes |
| FT - Incres Speed | FT - Incres Speed [%/s] | Yes | Yes |
| FT - Decres Speed | FT - Decres Speed [%/s] | Yes | Yes |
| FT - Max Error | FT - Max Error [°C] | Yes | Yes |
| FP - Decres Speed | FP - Decres Speed [%/s] | Yes | Yes |
| 2200 tr/min | 2200 tr/min | Yes | Yes |
| ECU Engine | ECU Engine | Yes | Yes |
| Fan Mode | Fan Mode | Yes | Yes |
| Fuseau | Fuseau [h] | MODE | Yes |
| Latitude (+ = North) | Latitude (+ = North) [°] | MODE | Yes |
| Longitude (+ = East) | Longitude (+ = East) [°] | MODE | Yes |
| Min black light | Min black light [%] | MODE | Yes |
| MODE | MODE | Yes | Yes |
| UP/DOWN Mode | UP/DOWN Mode | Yes | Yes |
| Locking Up Track | Locking UP Track | Active Locking | Yes |
| Engine type | Engine type | Yes | Yes |
| Backward Curent  - Hight Speed | Backward Curent  - Hight Speed [mA] | Yes | Yes |
| Forward Curent - Low Speed | Forward Curent - Low Speed [mA] | Yes | Yes |
| Forward Curent  - Hight Speed | Forward Curent  - Hight Speed [mA] | Yes | Yes |
| Backward Curent - Low Speed | Backward Curent - Low Speed [mA] | Yes | Yes |
| Stop Slope - Pump | Stop Slope - Pump [%/s] | Yes | Yes |
| Start Slope - Pump | Start Slope - Pump [%/s] | Yes | Yes |
| Hydraulic Bloc | Hydraulic Bloc | Yes | Yes |
| Value Hight Speed | Value Hight Speed [rpm] | Yes | Yes |
| UP/DOWN Speed | UP/DOWN Speed [rpm] | Yes | Yes |
| IDLE Speed | IDLE Speed [rpm] | Yes | Yes |
| Value Slow Speed | Value Slow Speed [rpm] | Yes | Yes |
| Force tension | Force tension | Yes | Yes |
| Tension Speed | Tension Speed [rpm] | Yes | Yes |
| G11 Modem | G11 Modem | Yes | Yes |
| Acceleration | Acceleration | Yes | Yes |
| Min Speed | Min Speed [rpm] | Yes | Yes |
| Re-Track mode in water | Re-Track mode in water | Yes | Yes |
| Fuel line ignition | Fuel line ignition | Yes | Yes |
| Auto Beach After Down | Auto Beach After Down | Yes | Yes |
| Backward Curent - Super Low Speed | Backward Curent - Super Low Speed [mA] | Yes | Yes |
| Forward Curent - Super Low Speed | Forward Curent - Super Low Speed [mA] | Yes | Yes |
| Neutral Joystick | Neutral Joystick [%] | Yes | Yes |
| Auto Stop Timer | Auto Stop Timer [s] | Yes | Yes |
| Cruise Control | Cruise Control | Yes | Yes |
| UP/DOWN Special mode | UP/DOWN Special mode | Yes | Yes |
| Force UNTIGHTEN | Force UNTIGHTEN | Yes | Yes |
| Max_diffrential | Max_diffrential [%] | Yes | Yes |
| Tension Pressure | Tension Pressure [bar] | Yes | Yes |
| Tracks pressure Mode | Tracks pressure Mode | Yes | Yes |
| Tension Error Parameter | Tension Error Parameter [%] | Yes | Yes |
| PWM Max mA | PWM Max mA [mA] | Yes | Yes |
| Parking | Parking [%] | Yes | Yes |