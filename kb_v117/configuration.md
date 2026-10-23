# Configuration, variantes et réglages — v117

Les **sélecteurs** sont les paramètres d'état (SP) qui choisissent la fonction active d'un canal : ce sont eux qui rendent le même logiciel compatible avec plusieurs équipements. Toute v2 doit conserver chacun de ces choix (voir `v2/compatibilite.md`).

## Sélecteurs de variante (paramètres réglables)

### T Engine type
- Valeurs : 0=EB2 1.2L · 1=FORD 1.5L · 2=Kubo (défaut EB2 1.2L)
- Défini dans : mc.Thermic / T.Engine i/o (MC42 app)
- Réglable via : Single adjust item: Engine type
- Canaux qui changent de logique (26) : `T Water °C Low`, `T Water °C High`, `T Water °C Critical`, `T Water °C Critical Critical`, `T Para enclench voyant pression huile`, `T FS - Start réduction`, `T General speed filtering`, `T Idle decel filter`, `T Pump Curent - Low Speed`, `T Pump Curent  - Hight Speed`, `T Pump Curent - Super Low Speed`, `T Pump Max curent`, `T IDLE Speed`, `T Slow Max  Speed`, `T Hight Speed`, `T Tension/UpDown Speed`, `T Min Speed mode`, `% load at current speed T45`, `Speed CAN T45`, `Engine coolant temp T45`, `T Min Speed acc1`, `Malfunction lamp T45`, `Red stop lamp T45`, `Amber warning lamp T45`, `Protect lamp T45`, `Actual engine, % torque T45`

### eb Battery Brand
- Valeurs : 0=BMW · 1=NovumTech · 2=Tyva · 3=Kreisel (défaut BMW)
- Défini dans : mc.Electric / E.BATTERY (MC42 app)
- Réglable via : Single adjust item: Battery Brand
- Canaux qui changent de logique (21) : `Cell_T_max_Master`, `Battery STANDBY`, `Battery CHARGE`, `Battery SOC`, `eb Charge Max`, `Battery CHARGED`, `Error Iso_Resist`, `Batt - Iso_Resist`, `IsoMonTriggerRecord tempo`, `eb Isolation Protection Level`, `BMW tyva - Isolation Error`, `Battery InstantVoltage`, `Current Bat`, `BMS_U_Trac`, `e Battery Protection mc`, `LowCellVoltage check bmw`, `HighCellVoltage check bmw`, `Max Discharge`, `Flag Ground Fault Detection`, `CPI_BMS_U_Trac`, `ec Max Full Charge Voltage`

### em1 M-Track - Brand
- Valeurs : 0=Sevcon · 1=Zapi (défaut Sevcon)
- Défini dans : mc.Electric / E.MOTORS (MC42 app)
- Réglable via : Single adjust item: M-Track - Brand
- Canaux qui changent de logique (20) : `M1 - Heatsink`, `M1 - CURRENT`, `M1 - CAN OK`, `M1 - RUN`, `M1 - Ready`, `M1 - Voltage`, `M1 - Torque`, `M1 - Speed`, `M1 - KTY`, `M2 - Heatsink`, `M2 - CURRENT`, `M2 - CAN OK`, `M2 - RUN`, `M2 - Ready`, `M2 - Voltage`, `M2 - Torque`, `M2 - Speed`, `M2 - KTY`, `M1 - Error mode`, `M2 - Error mode`

### md4 Engine Brand
- Valeurs : 0=Mercury · 1=Yamaha · 2=COX (défaut Mercury)
- Défini dans : c5.NMEA / OutBoards nmea (MD4-CAB app)
- Réglable via : Single adjust item: md4 Engine Brand
- Canaux qui changent de logique (10) : `Adress Loose`, `OutBoard_Adresse`, `Outboard_Priority`, `Engine 2 - Tank`, `Trim Value`, `Engine Oil Pressure - 1`, `Engine temp - 1`, `Fuel rate - 1`, `Engine Hour - 1`, `Alternator - 1`

### Tyva gen bender
- Valeurs : 0=gen1 · 1=gen2 (défaut gen1)
- Défini dans : mc.Electric / E.BATTERY / E. Tyva / bender tyva (MC42 app)
- Réglable via : Single adjust item: Tyva gen bender
- Canaux qui changent de logique (8) : `Batt - Iso_Resist - tyva`, `volt tyva mean off`, `tyva isomon extra can ok`, `iso value not valid tyva`, `system failure tyva isomon com`, `tyva isomon can nok`, `tyva isomon can ok`, `system failure tyva isomon gen2`

### em M-Pump - Brand
- Valeurs : 0=Sevcon gen · 1=Sevcon j19 (défaut Sevcon gen)
- Défini dans : mc.Electric / E.MOTORS (MC42 app) · entrée auto : `is_x100_math`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (7) : `M3 - Heatsink`, `M3 - Engine Temps`, `M3 - Voltage`, `M3 - Run`, `M3 - CAN OK`, `M3 - Ready`, `M3 - Error mode`

### Drive Type mc
- Valeurs : 0=Electric · 1=Fossil (défaut Electric)
- Défini dans : Initialization (MC42 app)
- Réglable via : Single adjust item: Drive Type
- Canaux qui changent de logique (7) : `EV Tension Sel`, `EV Lock Sel`, `EV Up Sel`, `EV Down Sel`, `EV By pass Sel`, `EV UnBlock Sel`, `4E Time Sleep engine`

### T Ambiante Temperature
- Valeurs : 0=Normal · 1=High (défaut Normal)
- Défini dans : mc.Thermic / T.Power (MC42 app)
- Réglable via : Single adjust item: Ambiante Temperature
- Canaux qui changent de logique (4) : `T Timer Fan Hot`, `T Timer Fan Mild`, `T Timer Fan Low`, `T Timer Fan Critical`

### ec Charger Brand
- Valeurs : 0=BMW · 1=Brusa · 2=Elcon (défaut BMW)
- Défini dans : mc.Electric / E.CHARGER (MC42 app)
- Réglable via : Single adjust item: Charger Brand
- Canaux qui changent de logique (2) : `Charger Output Current`, `Charger Output Voltage`

### em ZAPI Node
- Valeurs : 0=8-10 · 1=1-4 · 2=4-8 (défaut 8-10)
- Défini dans : mc.Electric / E.MOTORS (MC42 app)
- Réglable via : Single adjust item: ZAPI Node
- Canaux qui changent de logique (2) : `Node_ID`, `Node_ID`

### T Number of lockers
- Valeurs : 0=One · 1=Two · 2=Custom (défaut One)
- Défini dans : mc.Thermic / T.Track Up/Down (MC42 app)
- Réglable via : Single adjust item: Number of lockers
- Canaux qui changent de logique (2) : `T Locking Time`, `T unLocking Time`

### is_cab_1
- Valeurs : 0=x100 · 1=cab (défaut x100)
- Défini dans : mc.I/O (MC42 app) · entrée auto : `is_cab_math`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (2) : `sel batt reset/batt on or brake`, `sel var power`

### md4 Person
- Valeurs : 0=md4 Person 1 · 1=md4 Person 2 · 2=md4 Person 3 (défaut md4 Person 1)
- Défini dans : logic screen c10 and KB / cEQUIPEMENT / SEAT (MC42 app)
- Réglable via : Single adjust item: Person
- Canaux qui changent de logique (2) : `md4 Seat Up Down`, `md4 Seat Front Back`

### CAN Speed B mc
- Valeurs : 0=500 elec · 1=125 cab keybox · 2=250 thermal engine (défaut 500 elec)
- Défini dans : Initialization (MC42 app)
- Réglable via : Single adjust item: CAN B Speed
- Canaux qui changent de logique (1) : `Can Speed B`

### CAN Speed C mc
- Valeurs : 0=500 · 1=125 Prog Keybox x100 (défaut 500)
- Défini dans : Initialization (MC42 app)
- Réglable via : Single adjust item: CAN C Speed
- Canaux qui changent de logique (1) : `Can Speed C`

### water level state
- Valeurs : 0=Default state · 1=error (défaut Default state)
- Défini dans : mc.Link MC42-Screens Logic ims / joystick mc42 / level sensor cab or right joy (MC42 app) · entrée auto : `water nok`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `level to p`

### Node Init
- Valeurs : 0=0x50 · 1=0x51 · 2=0x52 (défaut 0x50)
- Défini dans : mc.Electric / E.BATTERY / E.BMW (MC42 app) · entrée auto : `Init Counter`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `Node Init ID`

### DcuErrorCode P
- Valeurs : 0=0 · 1=4097 · 2=8192 (défaut 0)
- Défini dans : mc.Electric / E.BATTERY / E.BMW (MC42 app) · entrée auto : `DcuErrorCode M`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `DcuErrorCode T`

### BatErrorCode P
- Valeurs : 0=0 · 1=4097 · 2=4098 · 3=4099 · 4=8193 · 5=12289 · 6=12290 · 7=12291 · 8=12292 · 9=16385 · 10=20481 · 11=24577 · 12=28673 · 13=32769 · 14=40961 · 15=40962 · 16=40963 · 17=40964 · 18=40965 · 19=40966 · 20=40967 · 21=40968 · 22=40969 · 23=40970 · 24=40971 · 25=40972 · 26=40973 · 27=40974 · 28=40975 · 29=40976 · 30=40977 · 31=40978 · 32=40979 · 33=40980 · 34=40981 · 35=40982 · 36=40983 · 37=40984 · 38=40985 · 39=40992 · 40=40993 · 41=45057 · 42=45058 · 43=45059 · 44=45060 · 45=45061 · 46=45062 · 47=45063 · 48=45064 · 49=45065 · 50=49153 · 51=49154 · 52=53249 · 53=65280 (défaut 0)
- Défini dans : mc.Electric / E.BATTERY / E.BMW (MC42 app) · entrée auto : `BatErrorCode M`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `BatErrorCode T`

### IsoMonErrorCode P
- Valeurs : 0=0 · 1=4097 · 2=8193 · 3=12289 · 4=16385 · 5=16386 · 6=20481 · 7=65280 (défaut 0)
- Défini dans : mc.Electric / E.BATTERY / E.BMW (MC42 app) · entrée auto : `IsoMonErrorCode M`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `IsoMonErrorCode T`

### tyva off on state
- Valeurs : 0=off · 1=on (défaut off)
- Défini dans : mc.Electric / E.BATTERY / E. Tyva (MC42 app) · entrée auto : `Tyva batt can ok`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `Soc Tyva onoff CHECK`

### isomon tyva off on state
- Valeurs : 0=off · 1=on (défaut off)
- Défini dans : mc.Electric / E.BATTERY / E. Tyva (MC42 app) · entrée auto : `isomon Tyva batt can ok`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `r isomon Tyva onoff`

### balancing state
- Valeurs : 0=Charging · 1=Balancing (défaut Charging)
- Défini dans : mc.Electric / E.CHARGER (MC42 app) · entrée auto : `Charger end of charge but balancing calc`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `ec AC Max Current Line`

### ec AC Voltage Range
- Valeurs : 0=230 V · 1=110 V (défaut 230 V)
- Défini dans : mc.Electric / E.CHARGER (MC42 app)
- Réglable via : Single adjust item: AC Voltage Range
- Canaux qui changent de logique (1) : `AC Voltage Value`

### em FAN MODE
- Valeurs : 0=AUTO · 1=OFF · 2=FORCE ON (défaut AUTO)
- Défini dans : mc.Electric / E.MOTORS / E.Cooling (MC42 app)
- Réglable via : Single adjust item: Fan mode
- Canaux qui changent de logique (1) : `E rad FAN OUT`

### em PUMP VAR MODE
- Valeurs : 0=AUTO · 1=OFF · 2=FORCE ON (défaut AUTO)
- Défini dans : mc.Electric / E.MOTORS / E.Cooling (MC42 app)
- Réglable via : Single adjust item: Pump var mode
- Canaux qui changent de logique (1) : `E water PUMP VAR`

### e Landing Block Number
- Valeurs : 0=One · 1=Two (défaut One)
- Défini dans : mc.Electric / E.Track Up/Down (MC42 app)
- Réglable via : Single adjust item: Landing Block Number
- Canaux qui changent de logique (1) : `e Landing time bloking`

### sim state moteur
- Valeurs : 0=not_sim · 1=sim (défaut not_sim)
- Défini dans : (racine) (MC42 app) · entrée auto : `sim start engine_m`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `sim thermal engine speed`

### reset/brake or tyva on qcode
- Valeurs : 0=Electric 1 novum old · 1=Fossil 1 · 2=Electric 2 Tyva (défaut Electric 1 novum old)
- Défini dans : mc.I/O (MC42 app) · entrée auto : `create new state tyva elec`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `Brake T/ Batt HT reset / tyva on SEL qcode`

### md4 Select Node
- Valeurs : 0=None · 1=KeyBox TB (GPS) · 2=KeyBox BB (Equip) · 3=KeyBox TC (Equip) (défaut None)
- Défini dans : logic screen c10 and KB / Keyboxs CAB / Program KB CAB (MC42 app)
- Réglable via : Single adjust item: md4 Select Node
- Canaux qui changent de logique (1) : `New ID`

### md4 GPS Speed factor
- Valeurs : 0=m/s · 1=kts (défaut m/s)
- Défini dans : c5.NMEA / GPS (MD4-CAB app)
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `GPS Factor`

### tyva1 off on state
- Valeurs : 0=off · 1=on (défaut off)
- Défini dans : a/c tyva24v (MD4-CAB app) · entrée auto : `Tyva1 batt can ok`
- Réglable via : *(aucun menu)*
- Canaux qui changent de logique (1) : `Soc Tyva1 onoff CHECK`

## Menus de réglage (Adjust groups)

### Maintenance
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Tracks pressure Mode`, `Re-Track mode in water`, `Tracks pressure Mode`, `Oil security`, `Fuel line ignition State`, `Reset Ladder Sensor when UP`, `Allow remote connection`

### Setup
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `UP/DOWN Mode`, `Automatic Joystick Inhibition`, `Auto Global switch Off`, `Auto Fast After Down`, `Neutral Deadband Joystick`, `Locking UP Track`, `Right Joystick`, `Left Joystick mc 36`, `Global Auto Off`, `Locking UP Track`, `Ambiante Temperature`, `E Auto Charge 12V`

### Setup PIN
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all

### Setup Speed
- Visible = Yes
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Stop Slope`, `Start Slope`, `Max Speed`, `Stop Slope`, `Start Slope`, `Forward - direct corrector`, `Backward - direct corrector`

### Setup Charger
- Visible = Is_Electric mc
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `AC Voltage Range`, `AC Max Current Line`, `AC Voltage Value`

### Setup Seat
- Visible = electronic seat
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Seat Up Down`, `Seat Front Back`, `Person`, `Person 1`, `Person 2`, `Person 3`

### Setup Outboard
- Visible = is_cab_mc
- PIN code = Not used
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `md4 Engine Brand`, `md4 Number of Engines`, `md4 Fuel Capacity (One Tank)`, `md4 Fuel Tanks Selection`

### Master Config
- Visible = Yes
- PIN code = Iguana Master menus PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Drive Type`, `Battery Brand`, `Charger Brand`, `ZAPI Node`, `Timer UP/DOWN`, `With Auto Off Relay`, `Landing Block Number`, `CAN B Speed`, `CAN C Speed`, `Engine type`, `Number of lockers`, `Program KeyBox`, `Program KeyBox`, `M-Track - Brand`, `Is_Cab_mc`, `Joystick plugged md45`, `joystick plugged mc42`, `Joystick plugged md10`, `Reset Ladder Sensor when UP`, `T Locking Time`, `electronic seat`, `Tyva gen bender`, `V10 motor`

### Master Electric
- Visible = Is_Electric mc
- PIN code = Iguana Master menus PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `High speed`, `Low speed`, `Pump var mode`, `Fan mode`, `Force K3 Auto-off`, `Battery Watchdog Delay`, `Battery Precharge Delay`, `Disable Crash Signal (V1)`, `Reset ZAPI state`

### Master Tracks
- Visible = Yes
- PIN code = Iguana Master menus PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Max_differential`, `With tension`, `Tension Pressure`, `Time to tension`, `EV Bloc delay`, `Max_diffrential`, `With tension`, `Tension Pressure`, `Time to tension`, `Right Joystick`, `Left Joystick`, `Right Joystick C41 C2:2`, `Left Joystick C41 C2:1`, `Right Joystick`, `Left Joystick mc 36`

### Master Features
- Visible = Yes
- PIN code = Iguana Master menus PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Engine - Force Ready`, `Power Controler Force`, `Charging Force`, `Variator Force`, `Battery Force Discharge`, `Speed Hydro Force`, `Force EV By Pass`, `Manual Start Engine`, `ECU Engine on`, `ECU Engine priming`, `Force at 2200 rpm`, `Force EV By Pass`, `Test Locker`, `debug screen`, `Force Safety off up/down 45`, `Is_a_Sim`, `Test buzzer MD4`, `bypsass brake T`, `T Force 12v port sensor on`, `max soc customer`, `md4 Water Level Protection`, `4E Time Sleep engine`, `test batt main on/off`, `up/down 20 times`, `a/c option`, `a/c option tyva`, `trig balancing`, `feature inflate 24v`, `Demisting option`

### Master Battery
- Visible = Is_Electric mc
- PIN code = Iguana Master menus PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Battery Management`, `Tension to charge`, `Charge Max`, `Battery hight temp`, `Battery max temp`, `Current Limiting - Error`, `Current Limiting - Increase`, `Current Limiting - Decrease`, `Force BMW Charge`, `Isolation Protection Level`, `Battery Error Clearance Delay`, `Trig Debug Cell Voltage`

### Master System Debug
- Visible = Is_Electric mc
- PIN code = Iguana Master menus PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Debug: Trig Charger Ready`, `Debug: Trig Low LTBat Voltage`, `Debug: Mute Battery Error`, `Debug: Trig Battery Error`, `Debug: Mute Watchdog`, `Debug: Test End Of Charge`, `Debug: Trig Battery Low Voltage Error`, `Debug: Inhibit System Crash Signal`, `Debug: Trig Battery Charged`

### Master Thermic
- Visible = Is_Thermic mc
- PIN code = Iguana Master menus PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `T FS - Decres Speed`, `T FP - Start réduction`, `T FP - Incres Speed`, `T FP - Decres Speed`, `T FP - Max Error`, `T FT - Incres Speed`, `T FT - Decres Speed`, `T FT - Max Error`, `T FO - Incres Speed`, `T FO - Decres Speed`, `T FO - Max Error`, `T FS - Start réduction`, `T FS - Incres Speed`, `T FS - Max Error`, `FXs Display`, `Min Speed mode`, `Tension/UpDown Speed`, `IDLE Speed`, `Slow Max  Speed`, `Hight Speed`, `Min Speed acc1`, `Max Speed Gap`, `Idle decel filter`, `General speed filtering`, `?Throttle pulse at Start up`, `Tempo Need Min Speed`, `Need Pressure Tempo`

### Master Thermic Cooling
- Visible = Is_Thermic mc
- PIN code = Iguana Master menus PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Water °C Critical Critical`, `Water °C Critical`, `Timer Fan Hot`, `Timer Fan Mild`, `Timer Fan Low`, `Water °C Low`, `Water °C High`, `Timer Fan Critical`, `Oil Temp Mid/High`, `Oil Temp Low/Mid`, `Oil Temp Critical`, `Aft Fan Max Test`, `Exhaust Fan Test`, `Aft Fan Low Test`, `Force Engine pump`, `Force Exhaust pump`, `Exhaust temp sensor MC42`

### Master Thermic Pumps
- Visible = Is_Thermic mc
- PIN code = Iguana Master menus PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Min current Left Fordward`, `Min current Right Backward`, `Min current Right Fordward`, `Min current Left Backward`, `Check Pump`, `Pump Curent  - Hight Speed`, `Pump Curent - Super Low Speed`, `Pump Max curent`, `Pump Curent - Low Speed`

### Master Sim Menu
- Visible = is_a_sim
- PIN code = Iguana Master menus PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `sim thermal engine speed`

### Master Charger
- Visible = Is_Electric mc
- PIN code = Iguana Master menus PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Max Full Charge Voltage`

### Master Config Options
- Visible = is_cab_mc
- PIN code = Iguana Master menus PIN
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `md4 Ladder Protection`, `md4 Aux 3 - Need HT`, `md4 Aux 1 - Show`, `md4 Aux 1 - Text`, `md4 Aux 1 - Need HT`, `md4 Aux 2 - Show`, `md4 Aux 2 - Text`, `md4 Aux 2 - Need HT`, `md4 Aux 3 - Show`, `md4 Aux 3 - Text`, `md4 VHF - Show`, `md4 Fridge - Show`, `md4 Aux 5- Show`, `md4 Aux 4 - Show`, `md4 Aux 4 - Text`, `AC`

### Delivery date
- Visible = Yes
- PIN code = PIN Code delivery date & RESET Maintenance
- Access levels = {Allow all; Allow all}
- Allow mode copy = No
- Reference channel = Not used
  - View/Adjust=Allow all
  - Set factory default value=Allow all
- Contenu : `Delivery day`, `Delivery month`, `Delivery Year`, `RESET Maintenance`, `Maintenance Counter`

## Tous les réglages (Adjust items) et le canal qu’ils modifient

| Réglage | Canal | Visible | Actif |
|---|---|---|---|
| CAN B Speed | CAN Speed B mc | Yes | Yes |
| Is_Cab_mc | is_cab_mc | Yes | Yes |
| Drive Type | Drive Type mc | Yes | Yes |
| CAN C Speed | CAN Speed C mc | Yes | Yes |
| Timer UP/DOWN | 4ET Timer UP/DOWN [s] | Yes | Yes |
| Is_a_Sim | is_a_sim | Yes | Yes |
| Reset Ladder Sensor when UP | mc Reset Ladder Sensor when UP | is_cab_mc | is_cab_mc |
| Tracks pressure Mode | e Tracks pressure Mode | Is_Electric mc | Yes |
| Current Limiting - Decrease | eb Current Limiting - Decrease [%/s] | Yes | Yes |
| Battery max temp | eb Battery max temp [°C] | Yes | Yes |
| Battery Brand | eb Battery Brand | Is_Electric mc | Yes |
| Battery Watchdog Delay | eb Battery Watchdog Delay [ms] | Yes | Yes |
| Debug: Mute Watchdog | eb Debug: Mute Watchdog | Is_Electric mc | Yes |
| Charging Force | eb Charging Force | Is_Electric mc | Yes |
| Charge Max | eb Charge Max [%] | Yes | Yes |
| Battery Error Clearance Delay | eb Battery Error Clearance Delay [s] | Yes | Yes |
| Battery hight temp | eb Battery hight temp [°C] | Yes | Yes |
| Current Limiting - Error | eb Current Limiting - Error [A] | Yes | Yes |
| Current Limiting - Increase | eb Current Limiting - Increase [%/s] | Yes | Yes |
| Battery Precharge Delay | eb Battery Precharge Delay [s] | Yes | Yes |
| Max Full Charge Voltage | ec Max Full Charge Voltage [V] | Yes | Yes |
| With Auto Off Relay | E With Auto Off Relay | Is_Electric mc | Yes |
| Locking UP Track | e Locking UP Track | Is_Electric mc | Yes |
| AC Max Current Line | ec AC Max Current Line [A] | not balancing | Yes |
| AC Voltage Range | ec AC Voltage Range | Yes | Yes |
| Controller Pump Temp | em Controller Pump Temp [°C] | Yes | Yes |
| Engine Max Temp | em Engine Max Temp [°C] | Yes | Yes |
| Controller Fan Temp | em Controller Fan Temp [°C] | Yes | Yes |
| Engine Eco Temp | em Engine Eco Temp [°C] | Yes | Yes |
| Pump var mode | em PUMP VAR MODE | Yes | Yes |
| Fan mode | em FAN MODE | Yes | Yes |
| Variator Force | E Variator Force | Is_Electric mc | Yes |
| HVLP Pump Test | E HVLP Pump Test | Yes | Yes |
| Power Controler Force | E Power Controler Force | Is_Electric mc | Yes |
| Battery Force Discharge | E Battery Force Discharge | Is_Electric mc | Yes |
| Enable Power Zapi | em Enable Power Zapi | Yes | Yes |
| Charger Brand | ec Charger Brand | Is_Electric mc | Yes |
| Tension to charge | E Tension to charge 12V | Yes | Yes |
| Force BMW Charge | eb Force BMW Charge | Is_BMW | Yes |
| Tension Error Parameter | e Tension Error Parameter [%] | Yes | Yes |
| Stop Slope | e Stop Slope [%/s] | Is_Electric mc | Yes |
| Start Slope | e Start Slope [%/s] | Is_Electric mc | Yes |
| Max Speed | e Max Speed [%] | Is_Electric mc | Yes |
| ZAPI Node | em ZAPI Node | Is_MT_Zapi 2 | Yes |
| Landing Block Number | e Landing Block Number | Is_Electric mc | Yes |
| Trig Debug Cell Voltage | eb Trig Debug Cell Voltage | Is_Novum | Yes |
| Isolation Protection Level | eb Isolation Protection Level [kOhm] | Is_bender_present | Yes |
| Battery Management | E Battery Management | Yes | Yes |
| Tension Pressure | e Tension Pressure [bar] | Is_Electric mc | Yes |
| Time to tension | e Time to tension [ms] | Is_Electric mc | Yes |
| EV Bloc delay | e EV Bloc delay [ms] | Is_Electric mc | Yes |
| With tension | e With tension | Is_Electric mc | Yes |
| Max_differential | e Max_differential [%] | Is_Electric mc | Yes |
| Engine - Force Ready | em Engine - Force Ready | Is_Electric mc | Yes |
| Force EV By Pass | e Force EV By Pass | Is_Electric mc | Yes |
| Debug: Trig Charger Ready | ec Debug: Trig Charger Ready | Is_Electric mc | Yes |
| Debug: Trig Low LTBat Voltage | E Debug: Trig Low LTBat Voltage 12V | Is_Electric mc | Yes |
| Debug: Mute Battery Error | eb Debug: Mute Battery Error | Is_Novum | Yes |
| Debug: Trig Battery Error | eb Debug: Trig Battery Error | Is_Novum | Yes |
| Debug: Trig Battery Low Voltage Error | eb Debug: Trig Battery Low Voltage Error | Is_Novum | Yes |
| Debug: Test End Of Charge | eb Debug: Test End Of Charge | Is_Novum | Yes |
| Debug: Inhibit System Crash Signal | e Debug: Inhibit System Crash Signal | Is_Electric mc | Yes |
| Debug: Trig Battery Charged | ec Debug: Trig Battery Charged | Is_Electric mc | Yes |
| Program KeyBox | mk E Program KeyBox x100 | Is_Electric_x100 mc | Yes |
| Disable Crash Signal (V1) | E Disable Crash Signal (NOVUM V1) | Is_Novum | Yes |
| Low speed | e LOW SPEED [rpm] | Yes | Yes |
| High speed | e HIGH SPEED [rpm] | Yes | Yes |
| Reset ZAPI state | Reset ZAPI state | Is_MT_Zapi | Yes |
| Error clear brusa | Error clear brusa | Yes | Yes |
| Right Joystick | Right Joystick ET45 C2:2 [%] | Joystick plugged md45 | Yes |
| Left Joystick | Left Joy ET45 ou water level C2:1 [%] | Joystick plugged md45 | Yes |
| Global Auto Off | E Global Auto Off [h] | Is_Electric mc | Yes |
| Force K3 Auto-off | E Force K3 Auto-off | Yes | Yes |
| Speed Hydro Force | Speed Hydro Force | VARIATOR SUPER ON E mc | Yes |
| Exhaust temp sensor MC42 | Exhaust temp sensor mc | Yes | Yes |
| Tracks pressure Mode | T Tracks pressure Mode | Is_Thermic mc | Yes |
| Oil security | OIL security | Yes | Yes |
| Fuel line ignition State | T Fuel line ignition State | Is_Thermic mc | Yes |
| Locking UP Track | T Locking UP Track | Is_Thermic mc | Yes |
| Ambiante Temperature | T Ambiante Temperature | Is_Thermic mc | Yes |
| Stop Slope | T Stop Slope [%/s] | Is_Thermic mc | Yes |
| Start Slope | T Start Slope [%/s] | Is_Thermic mc | Yes |
| Forward - direct corrector | T Forward - direct corrector [%] | Is_Thermic mc | Yes |
| Backward - direct corrector | T Backward - direct corrector [%] | Is_Thermic mc | Yes |
| Engine type | T Engine type | Is_Thermic mc | Yes |
| Number of lockers | T Number of lockers | Is_Thermic mc | Yes |
| Max_diffrential | T Max_diffrential [%] | Is_Thermic mc | Yes |
| With tension | T With tension | Is_Thermic mc | Yes |
| Tension Pressure | T Tension Pressure [bar] | Is_Thermic mc | Yes |
| Time to tension | T Time to tension [ms] | Is_Thermic mc | Yes |
| Manual Start Engine | T Manual Start Engine | Is_Thermic mc | Yes |
| ECU Engine on | T ECU Engine on | Is_Thermic mc | Yes |
| Force at 2200 rpm | T Force at 2200 rpm | Is_Thermic mc | Yes |
| Force EV By Pass | T Force EV By Pass | Is_Thermic mc | Yes |
| Test Locker | T Test Locker | Is_Thermic mc | Yes |
| T FS - Decres Speed | T FS - Decres Speed [%/s] | FXs Display | Yes |
| T FP - Start réduction | T FP - Start réduction [%] | FXs Display | Yes |
| T FP - Incres Speed | T FP - Incres Speed [%/s] | FXs Display | Yes |
| T FP - Decres Speed | T FP - Decres Speed [%/s] | FXs Display | Yes |
| T FP - Max Error | T FP - Max Error [%] | FXs Display | Yes |
| T FT - Incres Speed | T FT - Incres Speed [%/s] | FXs Display | Yes |
| T FT - Decres Speed | T FT - Decres Speed [%/s] | FXs Display | Yes |
| T FT - Max Error | T FT - Max Error [°C] | FXs Display | Yes |
| T FO - Incres Speed | T FO - Incres Speed [%/s] | FXs Display | Yes |
| T FO - Decres Speed | T FO - Decres Speed [%/s] | FXs Display | Yes |
| T FO - Max Error | T FO - Max Error [°C] | FXs Display | Yes |
| T FS - Start réduction | T FS - Start réduction [%] | FXs Display | Yes |
| T FS - Incres Speed | T FS - Incres Speed [%/s] | FXs Display | Yes |
| T FS - Max Error | T FS - Max Error [%] | FXs Display | Yes |
| FXs Display | FXs Display | Yes | Yes |
| Min Speed mode | T Min Speed mode [rpm] | Yes | Yes |
| Tension/UpDown Speed | T Tension/UpDown Speed [rpm] | Yes | Yes |
| IDLE Speed | T IDLE Speed [rpm] | Yes | Yes |
| Slow Max  Speed | T Slow Max  Speed [rpm] | Yes | Yes |
| Hight Speed | T Hight Speed [rpm] | Yes | Yes |
| Min Speed acc1 | T Min Speed acc1 [rpm] | Yes | Yes |
| Max Speed Gap | T Max Speed Gap [%] | Yes | Yes |
| Idle decel filter | T Idle decel filter | Yes | Yes |
| General speed filtering | T General speed filtering [%/s] | Yes | Yes |
| ?Throttle pulse at Start up | T Throttle pulse at Start up | Yes | Yes |
| Tempo Need Min Speed | T Tempo Need Min Speed [ms] | Yes | Yes |
| Need Pressure Tempo | T Need Pressure Tempo [ms] | Yes | Yes |
| Water °C Critical Critical | T Water °C Critical Critical [°C] | Yes | Yes |
| Water °C Critical | T Water °C Critical [°C] | Yes | Yes |
| Timer Fan Hot | T Timer Fan Hot [s] | Yes | Yes |
| Timer Fan Mild | T Timer Fan Mild [s] | Yes | Yes |
| Timer Fan Low | T Timer Fan Low [s] | Yes | Yes |
| Water °C Low | T Water °C Low [°C] | Yes | Yes |
| Water °C High | T Water °C High [°C] | Yes | Yes |
| Timer Fan Critical | T Timer Fan Critical [s] | Yes | Yes |
| Oil Temp Mid/High | T Oil Temp Mid/High [°C] | Yes | Yes |
| Oil Temp Low/Mid | T Oil Temp Low/Mid [°C] | Yes | Yes |
| Oil Temp Critical | T Oil Temp Critical [°C] | Yes | Yes |
| Aft Fan Max Test | mk T Aft Fan Max Test | Yes | Yes |
| Exhaust Fan Test | mk T Exhaust Fan Test | Yes | Yes |
| Aft Fan Low Test | mk T Aft Fan Low Test | Yes | Yes |
| Force Engine pump | mk T Force Engine pump | Yes | Yes |
| Force Exhaust pump | mk T Force Exhaust pump | Yes | Yes |
| Min current Left Fordward | T Min current Left Fordward [mA] | Yes | Yes |
| Min current Right Backward | T Min current Right Backward [mA] | Yes | Yes |
| Min current Right Fordward | T Min current Right Fordward [mA] | Yes | Yes |
| Min current Left Backward | T Min current Left Backward [mA] | Yes | Yes |
| Check Pump | T Check Pump | Yes | Yes |
| Pump Curent  - Hight Speed | T Pump Curent  - Hight Speed [mA] | Yes | Yes |
| Pump Curent - Super Low Speed | T Pump Curent - Super Low Speed [mA] | Yes | Yes |
| Pump Max curent | T Pump Max curent [mA] | Yes | Yes |
| Pump Curent - Low Speed | T Pump Curent - Low Speed [mA] | Yes | Yes |
| AC Voltage Value | AC Voltage Value [V] | Yes | Yes |
| Program KeyBox | mk T Program KeyBox | Is_Thermic mc | Yes |
| debug screen | debug screen | Yes | Yes |
| sim thermal engine speed | sim thermal engine speed | Yes | Yes |
| ECU Engine priming | T ECU Engine prime | Is_Thermic mc | Yes |
| M-Track - Brand | em1 M-Track - Brand | Is_Electric mc | Yes |
| Re-Track mode in water | 4ET Re-Track mode in water | Yes | Yes |
| UP/DOWN Mode | 4ET UP/DOWN Mode | Yes | Yes |
| Automatic Joystick Inhibition | 4ET Automatic Joystick Inhibition [s] | Is_Electric mc | Yes |
| Auto Global switch Off | 4ET Auto Global switch Off [min] | Is_Electric mc | Yes |
| Auto Fast After Down | 4ET Auto Fast After Down | Yes | Yes |
| Neutral Deadband Joystick | 4ET Neutral Deadband Joystick [%] | Yes | Yes |
| Force Safety off up/down 45 | Force Safety off up/down 45 | Yes | Yes |
| md4 Select Node | md4 Select Node | Yes | Yes |
| Person | md4 Person | Yes | Yes |
| Test buzzer MD4 | test buzzer 45 | Yes | Yes |
| bypsass brake T | bypsass brake T | Is_Thermic mc | Yes |
| Joystick plugged md45 | Joystick plugged md45 | is_x100_mc_s | Yes |
| Right Joystick | Low water level RJoy [%] | joystick plugged mc42 | Yes |
| Left Joystick mc 36 | Left Joystick mc 36 [%] | joystick plugged mc42 | Yes |
| joystick plugged mc42 | joystick plugged mc42 | Yes | Yes |
| Joystick plugged md10 | Joystick plugged md10 | is_cab_mc | Yes |
| T Force 12v port sensor on | T Force 12v port sensor on | Is_Thermic mc | Yes |
| max soc customer | max soc customer [%] | Is_Electric mc | Yes |
| Person 2 | md4 Person 2 | Yes | Yes |
| Seat Front Back | md4 Seat Front Back [%] | Yes | Yes |
| Seat Up Down | md4 Seat Up Down [%] | Yes | Yes |
| Person 3 | md4 Person 3 | Yes | Yes |
| Person 1 | md4 Person 1 | Yes | Yes |
| md4 Engine Brand | md4 Engine Brand | Yes | Yes |
| md4 Number of Engines | md4 Number of Engines | Yes | Yes |
| md4 Fuel Capacity (One Tank) | md4 Fuel Capacity (One Tank) [L] | Yes | Yes |
| md4 Fuel Tanks Selection | md4 Fuel Tanks Selection | Yes | Yes |
| md4 Aux 3 - Need HT | md4 Aux 3 - Need HT | Yes | Yes |
| md4 Aux 1 - Show | md4 Aux 1 - Show | Yes | Yes |
| md4 Aux 1 - Text | md4 Aux 1 - Text | Yes | Yes |
| md4 Aux 1 - Need HT | md4 Aux 1 - Need HT | Yes | Yes |
| md4 Aux 2 - Show | md4 Aux 2 - Show | Yes | Yes |
| md4 Aux 2 - Text | md4 Aux 2 - Text | Yes | Yes |
| md4 Aux 2 - Need HT | md4 Aux 2 - Need HT | Yes | Yes |
| md4 Aux 3 - Show | md4 Aux 3 - Show | Yes | Yes |
| md4 Aux 3 - Text | md4 Aux 3 - Text | Yes | Yes |
| md4 VHF - Show | md4 VHF - Show | Yes | Yes |
| md4 Fridge - Show | md4 Fridge - Show | Yes | Yes |
| md4 Water Level Protection | md4 Water Level Protection | is_cab_mc | Yes |
| T Locking Time | T Locking Time [ms] | T Number of lockers custom | Yes |
| 4E Time Sleep engine | 4E Time Sleep engine [s] | Yes | Yes |
| test batt main on/off | test batt main on/off | Is_Tyva | Yes |
| up/down 20 times | up/down 20 times | Yes | Yes |
| md4 Aux 5- Show | md4 Aux 5- Show | Yes | Yes |
| md4 Aux 4 - Show | md4 Aux 4 - Show | Yes | Yes |
| md4 Aux 4 - Text | md4 Aux 4 - Text | Yes | Yes |
| AC | AC | Yes | Yes |
| a/c option | a/c option | is_cab_mc | Yes |
| electronic seat | electronic seat | is_cab_mc | Yes |
| trig balancing | trig balancing | Yes | Yes |
| Tyva gen bender | Tyva gen bender | Yes | Yes |
| Allow remote connection | Allow remote connection | Yes | Yes |
| feature inflate 24v | feature inflate 24v | Yes | Yes |
| a/c option tyva | a/c option tyva | a/c option | Yes |
| E Auto Charge 12V | E Auto Charge 12V | Yes | Yes |
| Demisting option | Demisting option | is_cab_mc | Yes |
| Right Joystick C41 C2:2 | Right Joystick C41 C2:2 [%] | Joystick plugged md10 | Yes |
| Left Joystick C41 C2:1 | Left Joystick C41 C2:1 [%] | Joystick plugged md10 | Yes |
| Adjustable parameter | Adjustable parameter [%] | Yes | Yes |
| Delivery day | Delivery day | Yes | Yes |
| Delivery month | Delivery month | Yes | Yes |
| Delivery Year | Delivery Year | Yes | Yes |
| RESET Maintenance | RESET Maintenance | Yes | Yes |
| Maintenance Counter | Maintenance Counter | Yes | Yes |
| md4 Ladder Protection | md4 Ladder Protection | Yes | Yes |
| V10 motor | V10 motor | Yes | Yes |