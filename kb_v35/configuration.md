# Configuration, variantes et réglages — V35.42 (X100)

Les **sélecteurs** sont les paramètres d'état (SP) qui choisissent la fonction active d'un canal : ce sont eux qui rendent le même logiciel compatible avec plusieurs équipements. Toute v2 doit conserver chacun de ces choix (voir `v2/compatibilite.md`).

## Sélecteurs de variante (paramètres réglables)

### M-Track - Brand
- Valeurs : 0=Sevcon · 1=Zapi (défaut Sevcon)
- Défini dans : Electric / MOTORS / M-Tracks (MC42) · entrée auto : `M-Track - Brand Main`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (20) : `M1 - Heatsink`, `M1 - CURRENT`, `M1 - CAN OK`, `M1 - RUN`, `M1 - Ready`, `M1 - Voltage`, `M1 - Torque`, `M1 - Speed`, `M1 - KTY`, `M2 - Heatsink`, `M2 - CURRENT`, `M2 - CAN OK`, `M2 - RUN`, `M2 - Ready`, `M2 - Voltage`, `M2 - Torque`, `M2 - Speed`, `M2 - KTY`, `M1 - Error mode`, `M2 - Error mode`

### Engine type
- Valeurs : 0=FORD 1.5L (défaut FORD 1.5L)
- Défini dans : Thermic / Engine Speed (MC42)
- Réglable via : Single adjust item: Engine type
- Canaux qui changent de logique (10) : `IDLE Speed`, `Slow Speed`, `Hight Speed`, `UP/DOWN Speed`, `Min Speed`, `Tension Speed`, `Max curent`, `Curent - Low Speed`, `Curent  - Hight Speed`, `Curent - Super Low Speed`

### Battery Brand
- Valeurs : 0=BMW · 1=WattAlps (défaut BMW)
- Défini dans : Electric / BATTERY (MC42)
- Réglable via : Single adjust item: Battery Brand
- Canaux qui changent de logique (10) : `Cell_T_max_Master`, `BMS_Iso_Resist`, `Battery InstantVoltage`, `Battery SOC`, `Current Bat`, `BMS_U_Trac`, `LowCellVoltage`, `HighCellVoltage`, `Max Discharge`, `Desired Voltage`

### M-Pump - Brand
- Valeurs : 0=Sevcon (défaut Sevcon)
- Défini dans : Electric / MOTORS / M-Hydrau (MC42)
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (7) : `Heatsink`, `Engine Temps`, `M3 - Voltage`, `M3 - Run`, `M3 - CAN OK`, `M3 - Ready`, `M3 - Error mode`

### Ambiante Temperature
- Valeurs : 0=Normal · 1=High (défaut Normal)
- Défini dans : Thermic / Power (MC42)
- Réglable via : Single adjust item: Ambiante Temperature
- Canaux qui changent de logique (2) : `Timer Fan Engine cold`, `Timer Fan Engine Hot`

### ZAPI Node
- Valeurs : 0=8-10 · 1=1-4 · 2=4-8 (défaut 8-10)
- Défini dans : Electric / MOTORS (MC42)
- Réglable via : Single adjust item: ZAPI Node
- Canaux qui changent de logique (2) : `Node_ID`, `Node_ID`

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

### J1939 Speed
- Valeurs : 0=500 Electric · 1=250 Thermic (défaut 500 Electric)
- Défini dans : Initialization (MC42)
- Réglable via : Single adjust item: J1939 Speed
- Canaux qui changent de logique (1) : `J1939 Speed`

### Landing Block Number
- Valeurs : 0=One · 1=Two (défaut One)
- Défini dans : Track Up/Down (MC42)
- Réglable via : Single adjust item: Landing Block Number
- Canaux qui changent de logique (1) : `Landing time bloking`

### Node Init
- Valeurs : 0=0x50 · 1=0x51 · 2=0x52 (défaut 0x50)
- Défini dans : Electric / BATTERY / BMW (MC42) · entrée auto : `Init Counter`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `Node Init ID`

### DcuErrorCode P
- Valeurs : 0=0 · 1=4097 · 2=8192 (défaut 0)
- Défini dans : Electric / BATTERY / BMW (MC42) · entrée auto : `DcuErrorCode M`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `DcuErrorCode T`

### BatErrorCode P
- Valeurs : 0=0 · 1=4097 · 2=4098 · 3=4099 · 4=8193 · 5=12289 · 6=12290 · 7=12291 · 8=12292 · 9=16385 · 10=20481 · 11=24577 · 12=28673 · 13=32769 · 14=40961 · 15=40962 · 16=40963 · 17=40964 · 18=40965 · 19=40966 · 20=40967 · 21=40968 · 22=40969 · 23=40970 · 24=40971 · 25=40972 · 26=40973 · 27=40974 · 28=40975 · 29=40976 · 30=40977 · 31=40978 · 32=40979 · 33=40980 · 34=40981 · 35=40982 · 36=40983 · 37=40984 · 38=40985 · 39=40992 · 40=40993 · 41=45057 · 42=45058 · 43=45059 · 44=45060 · 45=45061 · 46=45062 · 47=45063 · 48=45064 · 49=45065 · 50=49153 · 51=49154 · 52=53249 · 53=65280 (défaut 0)
- Défini dans : Electric / BATTERY / BMW (MC42) · entrée auto : `BatErrorCode M`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `BatErrorCode T`

### IsoMonErrorCode P
- Valeurs : 0=0 · 1=4097 · 2=8193 · 3=12289 · 4=16385 · 5=16386 · 6=20481 · 7=65280 (défaut 0)
- Défini dans : Electric / BATTERY / BMW (MC42) · entrée auto : `IsoMonErrorCode M`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `IsoMonErrorCode T`

### Input Voltage
- Valeurs : 0=230 V · 1=110 V (défaut 230 V)
- Défini dans : Electric / CHARGER (MC42)
- Réglable via : Single adjust item: Input Voltage
- Canaux qui changent de logique (1) : `Input Voltage Value`

### Charger Brand
- Valeurs : 0=BMW · 1=Brusa · 2=Elcon (défaut BMW)
- Défini dans : Electric / CHARGER (MC42)
- Réglable via : Single adjust item: Charger Brand
- Canaux qui changent de logique (1) : `Charger Output Current`

### FAN MODE
- Valeurs : 0=AUTO · 1=OFF · 2=FORCE ON (défaut AUTO)
- Défini dans : Electric / MOTORS / Cooling (MC42)
- Réglable via : Single adjust item: FAN MODE
- Canaux qui changent de logique (1) : `FAN OUT`

### PUMP VAR MODE
- Valeurs : 0=AUTO · 1=OFF · 2=FORCE ON (défaut AUTO)
- Défini dans : Electric / MOTORS / Cooling (MC42)
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
- Contenu : `Tracks pressure Mode`, `Re-Track mode in water`, `Fuel line ignition State`, `Full Fan Mode`, `OIL Security`

### Setup
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `UP/DOWN Mode`, `Automatic Joystick Inhibition`, `Remote Control`, `Auto Fast After Down`, `Neutral Joystick`, `Cruise Control`, `Locking UP Track`, `Ambiante Temperature`, `Right Joystick`, `Left Joystick`, `Global Auto Off`, `Auto Charge 12V`

### Setup Charger
- Visible = Is_Electric
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Max Current Line`, `Input Voltage`, `Charge Max`

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
  - Name, FranÃ§ais=RÃ©glage vitesse
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Start Slope`, `Stop Slope`, `Backward - direct corrector`, `Forward - direct corrector`, `Max Speed`

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
- Contenu : `Drive Type`, `Engine type`, `Battery Brand`, `Charger Brand`, `M-Track - Brand Main`, `ZAPI Node`, `J1939 Speed`, `CAN Speed`, `Timer UP/DOWN`, `Program KeyBox`, `Proemion`, `With Auto Off Relay`, `Landing Block Number`

### Master Thermic
- Visible = Is_Thermic
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Full Fan Engine`, `Full Fan Oil`, `Timer Fan Engine cold`, `Timer Fan Engine Hot`, `Temp cold/hot`, `UP/DOWN Speed`, `IDLE Speed`, `Slow Speed`, `Min Speed`, `Tension Speed`, `Hight Speed`, `FP - Start rÃ©duction`, `FP - Incres Speed`, `FP - Decres Speed`, `FP - Max Error`, `FT - Start rÃ©duction`, `FT - Incres Speed`, `FT - Decres Speed`, `FT - Max Error`, `FO - Start rÃ©duction`, `FO - Incres Speed`, `FO - Decres Speed`, `FO - Max Error`, `FS - Start rÃ©duction`, `FS - Incres Speed`, `FS - Decres Speed`, `FS - Max Error`, `Full Fan Test`

### Master Electric
- Visible = Is_Electric
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Reset`, `LOW SPEED`, `HIGH SPEED`, `PUMP VAR MODE`, `FAN MODE`, `Enable Power Zapi`, `Force K3`, `EV Bloc delay`

### Master Pump
- Visible = Is_Thermic
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Max curent`, `Curent - Super Low Speed`, `Curent - Low Speed`, `Curent  - Hight Speed`, `Min current Right Backward`, `Min current Left Backward`, `Min current Left Fordward`, `Min current Right Fordward`, `Check Pump`

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
- Contenu : `Start Pulse`, `ECU Engine`, `Engine - Force Ready`, `Power Controler Force`, `Charging Force`, `Variator Force`, `Battery Force`, `2200 tr/min`, `Speed Hydro Force`, `Force EV By Pass`, `Force Bat Reset`

### Master Charger
- Visible = Is_Electric_MD3
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Input Voltage Value`, `Desired Voltage`, `Max Current Line`, `Input Voltage`

### Master Battery
- Visible = Is_Electric
- PIN code = Iguana PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Battery Managment`, `Balancing Frequency`, `Tension to charge`, `Battery Protection`, `Charge Max`, `Battery hight temp`, `Battery max temp`, `Current Limiting - Error`, `Current Limiting - Increase`, `Current Limiting - Decrease`, `Force BMW Charge`, `Iso Resist Protection Level`

## Tous les réglages (Adjust items) et le canal qu’ils modifient

| Réglage | Canal | Visible | Actif |
|---|---|---|---|
| J1939 Speed | J1939 Speed | Yes | Yes |
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
| Cruise Control | Cruise Control | Yes | Yes |
| Max curent | Max curent [mA] | Yes | Yes |
| Curent - Super Low Speed | Curent - Super Low Speed [mA] | Yes | Yes |
| Curent - Low Speed | Curent - Low Speed [mA] | Yes | Yes |
| Curent  - Hight Speed | Curent  - Hight Speed [mA] | Yes | Yes |
| Min current Right Backward | Min current Right Backward [mA] | Yes | Yes |
| Min current Left Backward | Min current Left Backward [mA] | Yes | Yes |
| Min current Left Fordward | Min current Left Fordward [mA] | Yes | Yes |
| Min current Right Fordward | Min current Right Fordward [mA] | Yes | Yes |
| Fuel line ignition State | Fuel line ignition State | Is_Thermic | Yes |
| Full Fan Mode | Full Fan Mode | Is_Thermic | Yes |
| ECU Engine | ECU Engine | Is_Thermic | Yes |
| 2200 tr/min | 2200 tr/min | Is_Thermic | Yes |
| Start Pulse | Start Pulse | Is_Thermic | Yes |
| Tracks pressure Mode | Tracks pressure Mode | Yes | Yes |
| Engine type | Engine type | Is_Thermic | Yes |
| With tension | With tension | Yes | Yes |
| Locking UP Track | Locking UP Track | Yes | Yes |
| Start Slope | Start Slope [%/s] | Yes | Yes |
| Stop Slope | Stop Slope [%/s] | Yes | Yes |
| Backward - direct corrector | Backward - direct corrector [%] | Is_Thermic | Yes |
| Forward - direct corrector | Forward - direct corrector [%] | Is_Thermic | Yes |
| Start PIN | Start PIN | Yes | Yes |
| Number 1 | Number 1 | Start PIN | Yes |
| Number 2 | Number 2 | Start PIN | Yes |
| Number 3 | Number 3 | Start PIN | Yes |
| Number 4 | Number 4 | Start PIN | Yes |
| Max_diffrential | Max_diffrential [%] | Yes | Yes |
| Min back light | Min back light [%] | Yes | Yes |
| MODE | MODE | Yes | Yes |
| Back light | Back light [%] | Yes | Yes |
| Ambiante Temperature | Ambiante Temperature | Is_Thermic | Yes |
| Timer Fan Engine cold | Timer Fan Engine cold [s] | Yes | Yes |
| Timer Fan Engine Hot | Timer Fan Engine Hot [s] | Yes | Yes |
| Temp cold/hot | Temp cold/hot [Â°C] | Yes | Yes |
| FT - Max Error | FT - Max Error [Â°C] | Yes | Yes |
| FP - Start rÃ©duction | FP - Start rÃ©duction [%] | Yes | Yes |
| FP - Incres Speed | FP - Incres Speed [%/s] | Yes | Yes |
| FP - Max Error | FP - Max Error [%] | Yes | Yes |
| FP - Decres Speed | FP - Decres Speed [%/s] | Yes | Yes |
| FT - Incres Speed | FT - Incres Speed [%/s] | Yes | Yes |
| FT - Decres Speed | FT - Decres Speed [%/s] | Yes | Yes |
| FT - Start rÃ©duction | FT - Start rÃ©duction [Â°C] | Yes | Yes |
| Check Pump | Check Pump | Yes | Yes |
| UP/DOWN Speed | UP/DOWN Speed [rpm] | Yes | Yes |
| IDLE Speed | IDLE Speed [rpm] | Yes | Yes |
| Slow Speed | Slow Speed [rpm] | Yes | Yes |
| Min Speed | Min Speed [rpm] | Yes | Yes |
| Tension Speed | Tension Speed [rpm] | Yes | Yes |
| Hight Speed | Hight Speed [rpm] | Yes | Yes |
| FO - Start rÃ©duction | FO - Start rÃ©duction [Â°C] | Yes | Yes |
| FO - Incres Speed | FO - Incres Speed [%/s] | Yes | Yes |
| FO - Max Error | FO - Max Error [Â°C] | Yes | Yes |
| FO - Decres Speed | FO - Decres Speed [%/s] | Yes | Yes |
| FS - Start rÃ©duction | FS - Start rÃ©duction [%] | Yes | Yes |
| FS - Incres Speed | FS - Incres Speed [%/s] | Yes | Yes |
| FS - Decres Speed | FS - Decres Speed [%/s] | Yes | Yes |
| FS - Max Error | FS - Max Error [%] | Yes | Yes |
| Tension Pressure | Tension Pressure [bar] | Yes | Yes |
| Full Fan Engine | Full Fan Engine [Â°C] | Yes | Yes |
| Full Fan Oil | Full Fan Oil [Â°C] | Yes | Yes |
| Drive Type | Drive Type | Yes | Yes |
| Input Voltage Value | Input Voltage Value [V] | Yes | Yes |
| Charger Brand | Charger Brand | Is_Electric | Yes |
| Desired Voltage | Desired Voltage [V] | Yes | Yes |
| Max Current Line | Max Current Line [A] | Yes | Yes |
| Input Voltage | Input Voltage | Yes | Yes |
| Engine - Force Ready | Engine - Force Ready | Is_Electric | Yes |
| Auto Charge 12V | Auto Charge 12V | Is_Electric | Yes |
| Tension to charge | Tension to charge | Yes | Yes |
| Power Controler Force | Power Controler Force | Is_Electric | Yes |
| Battery Brand | Battery Brand | Is_Electric | Yes |
| Battery Protection | Battery Protection | Yes | Yes |
| Charge Max | Charge Max [%] | Yes | Yes |
| Battery hight temp | Battery hight temp [Â°C] | Yes | Yes |
| Battery max temp | Battery max temp [Â°C] | Yes | Yes |
| Charging Force | Charging Force | Is_Electric | Yes |
| Current Limiting - Error | Current Limiting - Error [A] | Yes | Yes |
| Current Limiting - Increase | Current Limiting - Increase [%/s] | Yes | Yes |
| Current Limiting - Decrease | Current Limiting - Decrease [%/s] | Yes | Yes |
| Variator Force | Variator Force | Is_Electric | Yes |
| Battery Force | Battery Force | Is_Electric | Yes |
| Force BMW Charge | Force BMW Charge | Is_BMW | Yes |
| Reset | Reset | Yes | Yes |
| LOW SPEED | LOW SPEED [rpm] | Yes | Yes |
| HIGH SPEED | HIGH SPEED [rpm] | Yes | Yes |
| Program KeyBox | Program KeyBox | Yes | Yes |
| PUMP VAR MODE | PUMP VAR MODE | Yes | Yes |
| FAN MODE | FAN MODE | Yes | Yes |
| Global Auto Off | Global Auto Off [h] | Yes | Yes |
| Speed Hydro Force | Speed Hydro Force | Is_Electric | Yes |
| Enable Power Zapi | Enable Power Zapi | Is_MT_Zapi | Yes |
| Automatic Joystick Inhibition | Automatic Joystick Inhibition [s] | Yes | Yes |
| Force K3 | Force K3 | Yes | Yes |
| Max Speed | Max Speed [%] | Is_Electric | Yes |
| M-Track - Brand Main | M-Track - Brand Main | Is_Electric | Yes |
| None | OIL Security | Yes | Yes |
| Proemion | Proemion | Yes | Yes |
| With Auto Off Relay | With Auto Off Relay | Yes | Yes |
| Landing Block Number | Landing Block Number | Yes | Yes |
| Battery Managment | Battery Managment | Yes | Yes |
| ZAPI Node | ZAPI Node | Is_MT_Zapi | Yes |
| Balancing Frequency | Balancing Frequency | Yes | Yes |
| Time to tension | Time to tension [ms] | Yes | Yes |
| EV Bloc delay | EV Bloc delay [ms] | Yes | Yes |
| Full Fan Test | Full Fan Test | Yes | Yes |
| Force EV By Pass | Force EV By Pass | Yes | Yes |
| Iso Resist Protection Level | Iso Resist Protection Level | Yes | Yes |
| Force Bat Reset | Force Bat Reset | Is_Electric | Is_Electric |
| Locking pressure | Locking pressure [bar] | Yes | Yes |