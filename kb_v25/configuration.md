# Configuration, variantes et réglages — V25.74 (Commuter)

Les **sélecteurs** sont les paramètres d'état (SP) qui choisissent la fonction active d'un canal : ce sont eux qui rendent le même logiciel compatible avec plusieurs équipements. Toute v2 doit conserver chacun de ces choix (voir `v2/compatibilite.md`).

## Sélecteurs de variante (paramètres réglables)

### M-Track - Brand
- Valeurs : 0=Sevcon · 1=Zapi (défaut Sevcon)
- Défini dans : ELEC / MOTORS / M-Tracks (MC42[1] application)
- Réglable via : Single adjust item: M-Track - Brand
- Canaux qui changent de logique (20) : `M1 - Heatsink`, `M1 - CURRENT`, `M1 - CAN OK`, `M1 - RUN`, `M1 - Ready`, `M1 - Voltage`, `M1 - Torque`, `M1 - Speed`, `M1 - KTY`, `M2 - Heatsink`, `M2 - CURRENT`, `M2 - CAN OK`, `M2 - RUN`, `M2 - Ready`, `M2 - Voltage`, `M2 - Torque`, `M2 - Speed`, `M2 - KTY`, `M1 - Error mode`, `M2 - Error mode`

### Battery Brand
- Valeurs : 0=Kreisel · 1=BMW · 2=WattApls (défaut Kreisel)
- Défini dans : ELEC / BATTERY (MC42[1] application)
- Réglable via : Single adjust item: Battery Brand
- Canaux qui changent de logique (11) : `Cell_T_max_Master`, `BMS_Iso_Resist`, `Battery InstantVoltage`, `Battery SOC`, `Current Bat`, `BMS_U_Trac`, `LowCellVoltage`, `HighCellVoltage`, `Max Discharge`, `Flag Ground Fault Detection`, `Desired Voltage`

### Engine Brand
- Valeurs : 0=Mercury · 1=Yamaha · 2=COX (défaut Mercury)
- Défini dans : NMEA / OutBoard (MD4-10[0] application)
- Réglable via : Single adjust item: Engine Brand
- Canaux qui changent de logique (10) : `Adress Loose`, `OutBoard_Adresse`, `Outboard_Priority`, `Engine 2 - Tank`, `Trim Value`, `Engine Oil Pressure - 1`, `Engine temp - 1`, `Fuel rate - 1`, `Engine Hour - 1`, `Alternator - 1`

### M-Pump - Brand
- Valeurs : 0=Sevcon (défaut Sevcon)
- Défini dans : ELEC / MOTORS / M-Hydrau (MC42[1] application)
- Réglable via : Single adjust item: M-Pump - Brand
- Canaux qui changent de logique (7) : `Heatsink`, `Engine Temps`, `M3 - Voltage`, `M3 - Run`, `M3 - CAN OK`, `M3 - Ready`, `M3 - Error mode`

### Person
- Valeurs : 0=Person 1 · 1=Person 2 · 2=Person 3 (défaut Person 1)
- Défini dans : EQUIPEMENT / SEAT (MD4-10[0] application)
- Réglable via : Single adjust item: Person
- Canaux qui changent de logique (2) : `Seat Up Down`, `Seat Front Back`

### Select Node
- Valeurs : 0=None · 1=KeyBox TB (GPS) · 2=KeyBox BB (Equip) · 3=KeyBox TC (Equip) (défaut None)
- Défini dans : PROGRAM KEYBOX (MD4-10[0] application)
- Réglable via : Single adjust item: Select Node
- Canaux qui changent de logique (1) : `New ID`

### GPS Speed factor
- Valeurs : 0=m/s · 1=kts (défaut m/s)
- Défini dans : NMEA / GPS (MD4-10[0] application)
- Réglable via : Single adjust item: GPS Speed factor
- Canaux qui changent de logique (1) : `GPS Factor`

### Node Init
- Valeurs : 0=0x50 · 1=0x51 · 2=0x52 (défaut 0x50)
- Défini dans : ELEC / BATTERY / BMW (MC42[1] application) · entrée auto : `Init Counter`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `Node Init ID`

### DcuErrorCode P
- Valeurs : 0=0 · 1=4097 · 2=8192 (défaut 0)
- Défini dans : ELEC / BATTERY / BMW (MC42[1] application) · entrée auto : `DcuErrorCode M`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `DcuErrorCode T`

### BatErrorCode P
- Valeurs : 0=0 · 1=4097 · 2=4098 · 3=4099 · 4=8193 · 5=12289 · 6=12290 · 7=12291 · 8=12292 · 9=16385 · 10=20481 · 11=24577 · 12=28673 · 13=32769 · 14=40961 · 15=40962 · 16=40963 · 17=40964 · 18=40965 · 19=40966 · 20=40967 · 21=40968 · 22=40969 · 23=40970 · 24=40971 · 25=40972 · 26=40973 · 27=40974 · 28=40975 · 29=40976 · 30=40977 · 31=40978 · 32=40979 · 33=40980 · 34=40981 · 35=40982 · 36=40983 · 37=40984 · 38=40985 · 39=40992 · 40=40993 · 41=45057 · 42=45058 · 43=45059 · 44=45060 · 45=45061 · 46=45062 · 47=45063 · 48=45064 · 49=45065 · 50=49153 · 51=49154 · 52=53249 · 53=65280 (défaut 0)
- Défini dans : ELEC / BATTERY / BMW (MC42[1] application) · entrée auto : `BatErrorCode M`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `BatErrorCode T`

### IsoMonErrorCode P
- Valeurs : 0=0 · 1=4097 · 2=8193 · 3=12289 · 4=16385 · 5=16386 · 6=20481 · 7=65280 (défaut 0)
- Défini dans : ELEC / BATTERY / BMW (MC42[1] application) · entrée auto : `IsoMonErrorCode M`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `IsoMonErrorCode T`

### Input Voltage
- Valeurs : 0=220 V · 1=110 V (défaut 220 V)
- Défini dans : ELEC / CHARGER (MC42[1] application)
- Réglable via : Single adjust item: Input Voltage
- Canaux qui changent de logique (1) : `Input Voltage Value`

### Charger Brand
- Valeurs : 0=Brusa · 1=Elcon · 2=BMW · 3=Valeo (défaut Brusa)
- Défini dans : ELEC / CHARGER (MC42[1] application)
- Réglable via : Single adjust item: Charger Brand
- Canaux qui changent de logique (1) : `Charger Output Current`

### FAN MODE
- Valeurs : 0=AUTO · 1=OFF · 2=FORCE ON (défaut AUTO)
- Défini dans : ELEC / MOTORS / Cooling (MC42[1] application)
- Réglable via : Single adjust item: FAN MODE
- Canaux qui changent de logique (1) : `FAN OUT`

### PUMP VAR MODE
- Valeurs : 0=AUTO · 1=OFF · 2=FORCE ON (défaut AUTO)
- Défini dans : ELEC / MOTORS / Cooling (MC42[1] application)
- Réglable via : Single adjust item: PUMP VAR MODE
- Canaux qui changent de logique (1) : `PUMP VAR`

## Menus de réglage (Adjust groups)

### Maintenance
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Tracks pressure Mode`, `Re-Track mode in water`, `Test Mode Locking`, `Ladder Protection`, `Battery Protection`, `Reset Ladder Sensor when UP`

### Main Setup
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Automatic Joystick Inhibition`, `Wifi Remote Control`, `Cruise Control`, `Auto Fast After Down`, `Neutral Joystick`, `Wiper delay`, `Auto Charge 12V`, `PIN CODE`, `Auto Global switch Off`, `A/C Batt Pack?`

### Charger Setup
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Input Voltage`, `Charging Current`, `Auto Off After Charge?`

### Seat Setup
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Seat Up Down`, `Seat Front Back`, `Person`, `Person 1`, `Person 2`, `Person 3`

### Track Setup
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Min Tension Pressure`, `Arms locks enable?`, `Max Tension Pressure`

### Back Light Setup
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `MODE`, `Min back light`, `Screen backlight default value`

### Config Electric Drive
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Battery Brand`, `Charger Brand`, `M-Track - Brand`, `M-Pump - Brand`, `Proemion Gateway`, `Messages`, `KBB Keybox Type?`, `KTB Keybox Type?`, `KTC Keybox Type?`

### Config Outboard
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Number of Engines`, `Engine Brand`, `Fuel Capacity (One Tank)`, `Fuel Tanks Selection`

### Config GPS
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `GPS Speed factor`

### Config Options
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Single Button Equipement?`, `VHF - Show`, `Fridge - Show`, `Aux 1 - Show`, `Aux 1 - Text`, `Aux 1 - Need HT`, `Aux 2 - Show`, `Aux 2 - Text`, `Aux 2 - Need HT`, `Aux 3 - Show`, `Aux 3 - Text`, `Aux 3 - Need HT`, `Aux 4 - Show`, `Aux 4 - Text`, `Aux 4 - Need HT`, `Aux 5- Show`, `Aux 5 - Text`, `Aux 5 - Need HT`

### Master Setup
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Tension to charge`, `Water Level`, `Oil level Analog`, `Water Level Protection`, `Engines Time Starting`, `Ladder Stop Sensor`, `Ladder Protection`, `Reset Ladder Sensor when UP`, `Acceleration Sensor`

### Master Battery
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Battery ECO level`, `Battery LOW level`, `Battery max temp`, `Battery hight temp`, `Charging Current`, `Desired Voltage`, `Current Limiting - Error`, `Current Limiting - Increase`, `Current Limiting - Decrease`, `Balancing Frequency`, `WattAlps Debug`, `Force BMW Charge`, `Battery Protection Level`

### Master Drive
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Dead Man Timer Cruise Control`, `Max Speed`, `Left Joystick`, `Right Joystick`, `Stop Speed`, `Start Speed`

### Master Track
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Low Speed Pump`, `Hight Speed Pump`, `LOCK SPEED`, `Timer UP/DOWN`, `Parking`, `Time to tension`, `End Of Tension delay`, `Start By Pass`, `PMax derating`, `Stop By Pass`, `Tension Error Parameter`, `Min Speed for tensionning`, `Hydraulic speed slope`, `Passive Tension Pressure Limiter`

### Master Features
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Engine - Force`, `Variator Force`, `Battery Force`, `Power Controler Force`, `Battery Power Force`, `Charging Force`, `Oil security`, `HVLP Pump Test`, `Enable Power Zapi`, `Force unbrake`

### Master Cooling
- Visible = Yes
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `FAN MODE`, `PUMP VAR MODE`, `M-Tracks Controller Fan Temp`, `Engine Max Temp`, `Engine Eco Temp`, `M-Tracks Controller Pump Temp`

### Master A/C Bat Pack
- Visible = A/C Batt Pack?
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `A/CBat 1st Node ID`, `A/C ClimRelay KB Port`, `A/C Voltage High Limit`, `A/C Voltage Low Limit`, `A/C Voltage Float Level`, `A/C MinSOCforStartCharging`, `A/C MaxSOCforEndCharging`, `Battery NoAUX Level Mode`, `A/C Mute Watchdog`, `A/C Override Volt Limits`, `A/C Override Tracks Up`, `A/C SOC Top Limit`

### Keybox Setup
- Visible = No
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Select Node`

## Tous les réglages (Adjust items) et le canal qu’ils modifient

| Réglage | Canal | Visible | Actif |
|---|---|---|---|
| Tracks pressure Mode | Tracks pressure Mode | Yes | Yes |
| Re-Track mode in water | Re-Track mode in water | Yes | Yes |
| Wifi Remote Control | Remote Control | Yes | Yes |
| Battery ECO level | Battery ECO level [%] | Yes | Yes |
| Battery LOW level | Battery LOW level [%] | Yes | Yes |
| Battery max temp | Battery max temp [Â°C] | Yes | Yes |
| Battery hight temp | Battery hight temp [Â°C] | Yes | Yes |
| Charging Current | Max Current Line [A] | Yes | Yes |
| Desired Voltage | Desired Voltage [V] | Yes | Yes |
| Timer UP/DOWN | Timer UP/DOWN [s] | Yes | Yes |
| Max Speed | Max Speed [%] | Yes | Yes |
| Right Joystick | Right Joystick [%] | Yes | Yes |
| Left Joystick | Left Joystick [%] | Yes | Yes |
| Tension Error Parameter | Tension Error Parameter [%] | Yes | Yes |
| Hight Speed Pump | HIGH SPEED [rpm] | Yes | Yes |
| Start Speed | Start Speed [%/s] | Yes | Yes |
| Stop Speed | Stop Speed [%/s] | Yes | Yes |
| Variator Force | Variator Force | Yes | Yes |
| Acceleration Sensor | Acceleration Sensor | Yes | Yes |
| Low Speed Pump | LOW SPEED [rpm] | Yes | Yes |
| Time to tension | Time to tension [ms] | Yes | Yes |
| Select Node | Select Node | Yes | Yes |
| Battery Force | Battery Force | Yes | Yes |
| Person | Person | Yes | Yes |
| Seat Up Down | Seat Up Down [%] | Yes | Yes |
| Seat Front Back | Seat Front Back [%] | Yes | Yes |
| Wiper delay | Wiper delay [s] | Yes | Yes |
| Person 1 | Person 1 | Yes | Yes |
| Person 2 | Person 2 | Yes | Yes |
| Person 3 | Person 3 | Yes | Yes |
| Automatic Joystick Inhibition | Automatic Joystick Inhibition [s] | Yes | Yes |
| PIN CODE | PIN CODE | Yes | Yes |
| Oil security | Oil security | Yes | Yes |
| Dead Man Timer Cruise Control | Auto Stop Timer [s] | Yes | Yes |
| Auto Fast After Down | Auto Fast After Down | Yes | Yes |
| Cruise Control | Cruise Control | Yes | Yes |
| Neutral Joystick | Neutral Joystick [%] | Yes | Yes |
| Auto Charge 12V | Auto Charge 12V | Yes | Yes |
| Engines Time Starting | Engine Time Starting [ms] | Yes | Yes |
| Water Level | Water Level [%] | Yes | Yes |
| Oil level Analog | Oil level Analog [%] | Yes | Yes |
| Water Level Protection | Water Level Protection | Yes | Yes |
| HVLP Pump Test | HVLP Pump Test | Yes | Yes |
| Ladder Stop Sensor | Ladder Stop Sensor [Pulse/s] | Yes | Yes |
| Ladder Protection | Ladder Protection | Yes | Yes |
| Reset Ladder Sensor when UP | Reset Ladder Sensor when UP | Yes | Yes |
| Test Mode Locking | Test Mode Locking | Yes | Yes |
| LOCK SPEED | LOCK SPEED [rpm] | Yes | Yes |
| Aux 1 - Need HT | Aux 1 - Need HT | Yes | Yes |
| Aux 1 - Text | Aux 1 - Text | Yes | Yes |
| Aux 1 - Show | Aux 1 - Show | Yes | Yes |
| Aux 2 - Show | Aux 2 - Show | Yes | Yes |
| Aux 2 - Text | Aux 2 - Text | Yes | Yes |
| Aux 2 - Need HT | Aux 2 - Need HT | Yes | Yes |
| Aux 3 - Show | Aux 3 - Show | Yes | Yes |
| Aux 3 - Text | Aux 3 - Text | Yes | Yes |
| Aux 3 - Need HT | Aux 3 - Need HT | Yes | Yes |
| VHF - Show | VHF - Show | Yes | Yes |
| Fridge - Show | Fridge - Show | Yes | Yes |
| Auto Global switch Off | Auto Global switch Off [min] | Yes | Yes |
| Charging Force | Force Charging | Yes | Yes |
| Charger Brand | Charger Brand | Yes | Yes |
| Input Voltage | Input Voltage | Yes | Yes |
| Battery Protection | Battery Protection | Yes | Yes |
| Parking | Parking [%] | Yes | Yes |
| Min Tension Pressure | Min Tension Pressure [bar] | Yes | Yes |
| GPS Speed factor | GPS Speed factor | Yes | Yes |
| MODE | MODE | Yes | Yes |
| Min back light | Min back light [%] | Yes | Yes |
| Screen backlight default value | Screen backlight default value [%] | Yes | Yes |
| Number of Engines | Number of Engines | Yes | Yes |
| Engine Brand | Engine Brand | Yes | Yes |
| Fuel Capacity (One Tank) | Fuel Capacity (One Tank) [L] | Yes | Yes |
| Fuel Tanks Selection | Fuel Tanks Selection | Yes | Yes |
| Battery Brand | Battery Brand | Yes | Yes |
| Start By Pass | Start By Pass [ms] | Yes | Yes |
| Stop By Pass | Stop By Pass [ms] | Yes | Yes |
| Current Limiting - Error | Current Limiting - Error [A] | Yes | Yes |
| Current Limiting - Increase | Current Limiting - Increase [%/s] | Yes | Yes |
| Current Limiting - Decrease | Current Limiting - Decrease [%/s] | Yes | Yes |
| FAN MODE | FAN MODE | Yes | Yes |
| PUMP VAR MODE | PUMP VAR MODE | Yes | Yes |
| Engine - Force | Engine - Force ON | Yes | Yes |
| M-Tracks Controller Fan Temp | M-Tracks Controller Fan Temp [Â°C] | Yes | Yes |
| Engine Max Temp | Engine Max Temp [Â°C] | Yes | Yes |
| Engine Eco Temp | Engine Eco Temp [Â°C] | Yes | Yes |
| M-Tracks Controller Pump Temp | M-Tracks Controller Pump Temp [Â°C] | Yes | Yes |
| M-Track - Brand | M-Track - Brand | Yes | Yes |
| M-Pump - Brand | M-Pump - Brand | Yes | Yes |
| Arms locks enable? | Arms locks enable? | Yes | Yes |
| Power Controler Force | Power Controler Force | Yes | Yes |
| Battery Power Force | Battery Power Force | Yes | Yes |
| Proemion Gateway | Proemion Gateway | Yes | Yes |
| Messages | Messages | No | Yes |
| Balancing Frequency | Balancing Frequency | Yes | Yes |
| WattAlps Debug | WattAlps Debug | Is WattAlps | Yes |
| Enable Power Zapi | Enable Power Zapi | Yes | Yes |
| Auto Off After Charge? | Auto Off After Charge? | Yes | Yes |
| Force BMW Charge | Force BMW Charge | Yes | Yes |
| A/C Batt Pack? | A/C Batt Pack? | Yes | Yes |
| PMax derating | PMax derating [%] | Yes | Yes |
| A/CBat 1st Node ID | A/CBat 1st Node ID | Yes | Yes |
| A/C Voltage High Limit | A/C Voltage High Limit [mV] | Yes | Yes |
| A/C Voltage Low Limit | A/C Voltage Low Limit [mV] | Yes | Yes |
| A/C Mute Watchdog | A/C Mute Watchdog | Yes | Yes |
| A/C Override Volt Limits | A/C Override Volt Limits | Yes | Yes |
| A/C Override Tracks Up | A/C Override Tracks Up | Yes | Yes |
| Min Speed for tensionning | Min Speed for tensionning [RPM] | Yes | Yes |
| Hydraulic speed slope | Hydraulic speed slope [/s] | Yes | Yes |
| Max Tension Pressure | Max Tension Pressure [bar] | Yes | Yes |
| End Of Tension delay | End Of Tension delay [ms] | Yes | Yes |
| A/C SOC Top Limit | A/C SOC Top Limit [%] | Yes | Yes |
| Battery NoAUX Level Mode | Battery NoAUX Level Mode [%] | Yes | Yes |
| A/C MinSOCforStartCharging | A/C MinSOCforStartCharging [%] | Yes | Yes |
| A/C MaxSOCforEndCharging | A/C MaxSOCforEndCharging [%] | Yes | Yes |
| A/C Voltage Float Level | A/C Voltage Float Level [mV] | Yes | Yes |
| KTB Keybox Type? | KTB Keybox Type? | Yes | Yes |
| KBB Keybox Type? | KBB Keybox Type? | Yes | Yes |
| KTC Keybox Type? | KTC Keybox Type? | Yes | Yes |
| Aux 4 - Show | Aux 4 - Show | Is single button Eqt | Yes |
| Aux 4 - Text | Aux 4 - Text | Is single button Eqt | Yes |
| Aux 4 - Need HT | Aux 4 - Need HT | Is single button Eqt | Yes |
| Aux 5- Show | Aux 5- Show | Is single button Eqt | Yes |
| Aux 5 - Text | Aux 5 - Text | Is single button Eqt | Yes |
| Aux 5 - Need HT | Aux 5 - Need HT | Is single button Eqt | Yes |
| Single Button Equipement? | Single Button Equipement? | Yes | Yes |
| A/C ClimRelay KB Port | A/C ClimRelay KB Port | Yes | Yes |
| Tension to charge | Tension to charge | Yes | Yes |
| Battery Protection Level | Battery Protection Level [KOhm] | Yes | Yes |
| Force unbrake | Force unbrake | Yes | Yes |
| Passive Tension Pressure Limiter | Passive Tension Pressure Limiter | Yes | Yes |