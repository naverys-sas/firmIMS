# MC42 — Track tension

30 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Track tension

#### Track pressure  `VIN`
- Propriétés : Unit=bar · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-SP500 · Calibration={500; 4500; 0; 500} · Alarms={No; 0; No; 100} · Module=MC42 (MC42[1]) · Module index=2
- Utilisé par : `Pression Filter`, `Track Tension Error`, `Adjust group: Master Tracks`, `Measure group: Hydraulic`
- Ligne export : 13639 · id 32718

#### Tracks pressure Mode  `SP`
> This channel is used to give unit and names to the MEM
- Propriétés : Input channel=None · Default state name=AUTO · States={UNTIGHTEN}
- Utilisé par : `IDC Free`, `ON/OFF/Untighed`, `Tension State`, `Tracks pressure Mode`, `Untingthen`, `Adjust group: Maintenance`, `Single adjust item: Tracks pressure Mode`
- Ligne export : 13663 · id 32719

#### Reset Startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset Startup`
- Lit : ``, `Reset Startup`
- Utilisé par : ``, `Reset Startup`, `Reset Startup`, `Tracks pressure Mode`
- Ligne export : 13675 · id 32721

#### Tracks pressure Mode  `MEM`
- Propriétés : Input channel=Tracks pressure Mode · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : ``, `Reset Startup`, `Tracks pressure Mode`
- Utilisé par : `IDC Free`, `ON/OFF/Untighed`, `Tension State`, `Untingthen`, `Adjust group: Maintenance`, `Single adjust item: Tracks pressure Mode`
- Ligne export : 13725 · id 32730

#### Wait engine start  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `System Started`
- Lit : ``, `System Started`
- Utilisé par : `ON/OFF/Untighed`, `Ok tension`, `Tension State`, `Wait engine Stop`
- Ligne export : 13768 · id 32738

#### ON/OFF/Untighed  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ON* :
  - **Activating** = `Wait engine start`
  - **Blocking** = `Tracks pressure Mode`
- Fonction *UNTIGHTED* :
  - **Activating** = `Tracks pressure Mode`
- Lit : ``, `Tracks pressure Mode`, `Wait engine start`
- Utilisé par : `Super Ok tension`
- Ligne export : 13811 · id 32746

#### Pression Filter  `SFC`
- Propriétés : Input channel=Track pressure [bar] · Enable=Yes · Type=Slopes · Slopes={{50; 50}; {1; 1}}
- Lit : `Track pressure`
- Utilisé par : `Need Pressure`, `MD3 page: BASE`
- Ligne export : 13889 · id 32759

#### Time to tension  `IP`
- Propriétés : Unit=ms · Default mode={150}
- Utilisé par : `Super Ok tension`, `Adjust group: Master Tracks`, `Single adjust item: Time to tension`
- Ligne export : 13907 · id 32760

#### Ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `PositiveFlank(Wait engine start)`
- Lit : ``, `Wait engine start`
- Utilisé par : `Super Ok tension`
- Ligne export : 13919 · id 32761

#### 10 minutes auto tender  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=10
- Logique :
  - **Decreasing** = `System Started`
  - **Resetting** = `10 minutes auto tender [min] <= 0`
- Lit : ``, `System Started`
- Utilisé par : `Super Ok tension`
- Ligne export : 13963 · id 32769

#### Tension Pressure  `IP`
- Propriétés : Unit=bar · Default mode={160}
- Utilisé par : `Need Pressure`, `Adjust group: Master Tracks`, `Single adjust item: Tension Pressure`
- Ligne export : 14024 · id 32780

#### Need Pressure  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `Tension Pressure [bar] > Pression Filter [bar]`
- Lit : ``, `Pression Filter`, `Tension Pressure`
- Utilisé par : `Super Ok tension`
- Ligne export : 14036 · id 32781

#### Tension Error Parameter  `FP`
- Propriétés : Unit=% · Default mode={100}
- Utilisé par : `Over Tension`
- Ligne export : 14081 · id 32790

#### Super Ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=Time to tension [ms] · Function selector=ON/OFF/Untighed
- Fonction *OFF* :
  - **Blocking** = `True`
- Fonction *ON* :
  - **Activating** = `(NegativeFlank(Ok tension)) OR (10 minutes auto tender [min] = 0) OR (Need Pressure)`
  - **Blocking** = `(Over Tension) OR (Inter EV Verin)`
- Fonction *UNTIGHTED* :
  - **Blocking** = `True`
- Lit : ``, `10 minutes auto tender`, `Inter EV Verin`, `Need Pressure`, `ON/OFF/Untighed`, `Ok tension`, `Over Tension`, `Time to tension`
- Utilisé par : `Delay Off super ok tension`, `Inter EV tendre Chenille`
- Ligne export : 14093 · id 32801

#### Delay Off super ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `Super Ok tension`
- Lit : ``, `Super Ok tension`
- Utilisé par : `Super Ok Tension Math`
- Ligne export : 14229 · id 32827

#### Super Ok Tension Math  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `Delay Off super ok tension * 100`
- Lit : ``, `Delay Off super ok tension`
- Utilisé par : `Slope Super Ok`
- Ligne export : 14272 · id 32835

#### Slope Super Ok  `SFC`
- Propriétés : Input channel=Super Ok Tension Math [%] · Enable=Yes · Type=Slopes · Slopes={{5; 1}; {2; 2}}
- Lit : `Super Ok Tension Math`
- Utilisé par : `Over Tension`
- Ligne export : 14315 · id 32843

#### Over Tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Over Tension) OR (Slope Super Ok [%] > Tension Error Parameter [%])`
  - **Blocking** = `not(System Started)`
- Lit : ``, `Slope Super Ok`, `System Started`, `Tension Error Parameter`
- Utilisé par : `Super Ok tension`, `Track Tension Error`, `Event log: Hydraulic Event`
- Ligne export : 14333 · id 32791

#### Wait engine Stop  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=4000
- Logique :
  - **Activating** = `Wait engine start`
- Lit : ``, `Wait engine start`
- Utilisé par : `Tension State`
- Ligne export : 14393 · id 32845

#### Tension State  `SMC`
- Propriétés : Default state name=ON/OFF
- Fonction *Parking* :
  - **Activating** = `Wait engine Stop`
  - **Blocking** = `(Wait engine start) OR (Tracks pressure Mode)`
- Fonction *Unthingten* :
  - **Activating** = `Tracks pressure Mode`
- Lit : ``, `Tracks pressure Mode`, `Wait engine Stop`, `Wait engine start`
- Utilisé par : *(personne)*
- Ligne export : 14436 · id 32853

#### Track Tension Error  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Track Tension Error · Text=Try a Calibrating (Setting/Maintenance). Use straight. Contact your service center. · Channel=Track pressure [bar]
- Logique :
  - **Showing** = `Over Tension`
- Lit : ``, `Over Tension`, `Track pressure`
- Utilisé par : *(personne)*
- Ligne export : 14521 · id 32890

#### Untingthen  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Tracks pressure Mode`
- Lit : ``, `Tracks pressure Mode`
- Utilisé par : `IDC Tension`, `Inter EV By Pass`
- Ligne export : 14567 · id 33241

####   `VIN`
- Propriétés : Name, English=Oil level Analog · Unit=% · Reference voltage=Reference voltage A · Error value=0 · Calibration={50; 1800; 0; 100} · Alarms={Yes; 5; No; 120} · Module=MC42 (MC42[1]) · Module index=0
- Lit : ``, `Oil level`
- Utilisé par : ``, ``, `10 fail Starting`, `10 hours check-up`, `10 hours check-up`, `10 minutes auto tender`, `1552 - Hardware enable - IDC`, `1553 - Actual battery output voltage`, `1553 - Actual mains current`, `1553 - Actual mains voltage`, `1553 - output current to the battery`, `1555 - Power stage temperature - Byte`, `1560 - Desired Current`, `1560 - Desired Voltage`, `1560 - Max Current from 230 V`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Adress Loose`, `Adress_Search`, `Adresse_Mem`, `Allow Cruise`, `Allow Run Cruise`, `Auto Fast after Down`, `Auto Fast after Down Wait`, `Auto Off`, `Auto Off Bip`, `Auto Off Confirmed`, `Auto PAUSE/OFF`, `Auto Stop Timer`, `BATT - Reset`, `BMS_Iso_Resist`, `BMS_U_Trac`, `BMW - DRIVE MODE`, `BMW - ERROR DIGIT`, `BMW - Frequency`, `BMW - Iso_Resist`, `BMW - Main current`, `BMW - Output Voltage`, `BMW - Output current`, `BMW - SOC`, `BMW - Status`, `BMW CAN OK`, `BMW CAN OK`, `BMW Charging`, `BMW Connected`, `BMW Error`, `BMW Ready`, `Backlight Value`, `Backward Curent`, `Bad pressure`, `Balancing Counter`, `Balancing State`, `Bat - 100A-125A`, `Bat - 1A-25A`, `Bat - 25A-50A`, `Bat - 50A-75A`, `Bat - 75A-100A`, `Bat - up to 125A`, `Bat CMD`, `Bat Counter`, `BatNodeState`, `Batterie State`, `Battery CAN OK`, `Battery CHARGED`, `Battery CMD`, `Battery DRIVE MODE`, `Battery ERROR DIGIT`, `Battery Error Code`, `Battery Error Durring 5 s`, `Battery HIGHT TEMP`, `Battery InstantVoltage`, `Battery NEED TO CHARGE`, `Battery POWER`, `Battery Protection`, `Battery Protection`, `Battery SOC`, `Battery SOC Costumer`, `Battery STATE`, `Battery State MEM`, `Battery not need to charge`, `Battery start by charger`, `Bip`, `Bloc`, `Brake`, `Brake`, `Brake Activation`, `Brusa CAN OK`, `Brusa Charging`, `Brusa Connected`, `Brusa Error`, `Brusa ready`, `C`, `CMD`, `CMD`, `Calcul AccÃ©lÃ©ration`, `CanBus Error TB`, `CanOn Wait`, `Cell_T_max_Master`, `Charge`, `Charge Mode`, `Charge start state`, `Charger CAN BUS OK`, `Charger CHARGING`, `Charger CONNECT to 220V`, `Charger Connected`, `Charger DIGITAL CMD`, `Charger ERROR`, `Charger Output Current`, `Charger READY`, `Charger STATE`, `Charger State Finite`, `Charger end charge`, `Command State`, `Convert Left`, `Convert Right`, `CouchÃ© night`, `Counter`, `Couple Moteur`, `Couple Moteur`, `Current Bat`, `Current Date MEN`, `Cuurent Bat (ABS)`, `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `DOWN Counter`, `Days in current year`, `DcuNodeState`, `Dec`, `Delay Off super ok tension`, `DiffCellVoltage`, `Don'push button`, `DurÃ©e`, `EMERG`, `EMERG`, `ENGINE RUN`, `ENGINE RUN`, `ET`, `ET h`, `Elcon - output Voltage`, `Elcon - output current`, `Elcon CAN OK`, `Elcon Charging`, `Elcon Connected`, `Elcon Error`, `Elcon Ready`, `Electric Engine STATE`, `Emmergency Stop Left`, `Emmergency Stop Right`, `Enable`, `Enable`, `Engine Stopped`, `Engine Temps`, `Engine hours`, `Engine hydro`, `Engine hydro Speed`, `Engines Not Ready`, `Error 1 - MEM`, `Error 1 - MEM`, `Error 2 - MEM`, `Error 2 - MEM`, `Error 3 - MEM`, `Error Iso_Resist`, `Error Wait`, `Error Wait`, `F4 Off`, `FAN OUT`, `FS1 Switch`, `FS1 Switch`, `Fail Start Counter`, `Fail Starting`, `Fordward Left`, `Fordward Right`, `Forward`, `Forward`, `Forward Curent`, `Func State`, `Func State`, `GPS Adresse Find`, `GPS_Adresse_Find_Int`, `Garmin - NMEA`, `Global Auto Off Timer`, `HIGH`, `HeartBeat`, `HeartBeat`, `Heatsink`, `HighCellVoltage`, `Ho`, `Ho_night`, `Hot Oil`, `Hour actual`, `Hydraulic pump statut`, `ID Fault`, `ID Prog`, `IDC Auto Sleep`, `IDC Batt Protection`, `IDC Free`, `IDC Speed Free`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `IDC Tension`, `If not start`, `Iguana PIN`, `Init Counter`, `Init Seq`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter EV By Pass`, `Inter EV DOWN`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP`, `Inter EV UP Delay`, `Inter EV Verin`, `Inter EV tendre Chenille`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Is_BMW`, `Is_Charger_BMW`, `Is_Charger_Brusa`, `Is_Charger_Elcon`, `Is_Electric`, `Is_Electric_MD3`, `Is_M3_Sevcon`, `Is_MT_Sevcon`, `Is_MT_Zapi`, `Is_Thermic`, `Is_Thermic_MD3`, `Is_WattAlps`, `IsoMonNodeState`, `Joystick Zero`, `Joystick Zero`, `Joystick not zero`, `Joystick to zero CMSG`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `K1 Fan Rear / Fan`, `K1 fuse is blown`, `K10`, `K10 fuse is blown`, `K11`, `K11 fuse is blown`, `K12`, `K12 fuse is blown`, `K13`, `K13 fuse is blown`, `K2 Fan Super / Pump`, `K2 fuse is blown`, `K3 Fan Exhaust / AutoOff`, `K3 fuse is blown`, `K4 Engine Power / Search Lights`, `K4 fuse is blown`, `K5 Engine Start`, `K5 fuse is blown`, `K6 Aux 1`, `K6 fuse is blown`, `K7 Aux 2`, `K7 fuse is blown`, `K8`, `K8 fuse is blown`, `K9`, `K9 fuse is blown`, `Keep ON`, `KeyBox Can Ok`, `Ko to move`, `L`, `LOW`, `Latence Math`, `LatenceTimer`, `Latitude Compute`, `Latitude Compute MEN`, `Left Error`, `Left Warning`, `LevÃ© night`, `Libre`, `Lock`, `Locking Phase Duration`, `Lon`, `Longitude Compute`, `Longitude Compute MEN`, `LowCellVoltage`, `M`, `M1 - 100A-125A`, `M1 - 25A-50A`, `M1 - 50A-75A`, `M1 - 75A-100A`, `M1 - CAN OK`, `M1 - CURRENT`, `M1 - Charge`, `M1 - ENGINE HOT`, `M1 - Error mode`, `M1 - Heatsink`, `M1 - KTY`, `M1 - Mechanical power`, `M1 - NEED TO FAN`, `M1 - NEED TO PUMP`, `M1 - New Error Code`, `M1 - Normal Mode`, `M1 - RUN`, `M1 - Ready`, `M1 - Right Engine CMSG`, `M1 - Speed`, `M1 - Torque`, `M1 - Torque Tracks`, `M1 - Voltage`, `M1 - Zapi New Error Code`, `M1 - Zapi New Warning Code`, `M1 - up to 125A`, `M2 - 100A-125A`, `M2 - 25A-50A`, `M2 - 50A-75A`, `M2 - 75A-100A`, `M2 - CAN OK`, `M2 - CURRENT`, `M2 - Charge`, `M2 - ENGINE HOT`, `M2 - Error mode`, `M2 - Heatsink`, `M2 - KTY`, `M2 - Left Engine CMSG`, `M2 - Mechanical power`, `M2 - NEED TO FAN`, `M2 - NEED TO PUMP`, `M2 - New Error Code`, `M2 - Normal mode`, `M2 - RUN`, `M2 - Ready`, `M2 - Speed`, `M2 - Torque`, `M2 - Torque tracks`, `M2 - Voltage`, `M2 - ZAPI - New Warning Code`, `M2 - Zapi - New Error Code`, `M2 - up to 125A`, `M3  (Pump) - Filter`, `M3 - CAN OK`, `M3 - Charge`, `M3 - ENGINE HOT`, `M3 - Error mode`, `M3 - NEED TO FAN`, `M3 - NEED TO PUMP`, `M3 - New Error Code`, `M3 - Pump Engine CMSG`, `M3 - Ready`, `M3 - Run`, `M3 - Voltage`, `M3_Speed`, `MD3 - DOWN`, `MD3 - UP`, `MD4 - Start Button Blocking Neutral`, `MDGN-+BAT:MC2[1]`, `Main Switch Battery`, `Math Current`, `Math Current`, `Math Droit`, `Math Gauche`, `Math Left`, `Math Right`, `Math Voltage`, `Math Voltage`, `Max Discharge`, `Max Manip`, `Min Speed`, `Mini Wait`, `MÃ©ridian`, `NEED FAN`, `NEED MORE SPEED`, `NEED PUMP`, `Need Pressure`, `Need to Charge IDC - Public`, `Need to Charge Voltage`, `Need to Charge Voltage Wait`, `Need to charge`, `New Battery State`, `New Error Code`, `New Timer`, `OK BLOC`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `OK UP/DOWN`, `ON/OFF Var`, `ON/OFF/Untighed`, `Oil Not Good`, `Oil level`, `Oil level`, `Ok tension`, `Ok to move`, `Over Tension`, `PARKER OK`, `PDO1_RX`, `PDO1_RX`, `PDO1_TX`, `PDO1_TX`, `PDO2_TX`, `PDO2_TX`, `PIN 44`, `PIn State`, `PUMP VAR`, `Power`, `Power`, `Power`, `Power Down`, `Power Down Wait`, `Power State Int`, `Process Down Engine`, `Pump 1 Right`, `Pump 1 Right Filter ECC1`, `Pump 2 Left`, `Pump 2 Left Filter ECC1`, `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Request Parameter State`, `Reset`, `Reset`, `Reset`, `Reset Speed`, `Reset Startup`, `Reset Startup`, `Reset State`, `Reset on startup`, `Reverse`, `Reverse`, `Reverse Left`, `Reverse Right`, `Right Error`, `Right Warning`, `SARTING`, `SEV - M1 - CAN OK`, `SEV - M1 - CURRENT`, `SEV - M1 - Error mode`, `SEV - M1 - RUN`, `SEV - M1 - Ready`, `SEV - M1 - Speed`, `SEV - M1 - Torque actual`, `SEV - M1 - Voltage`, `SEV - M2 - CAN OK`, `SEV - M2 - CURRENT`, `SEV - M2 - Error mode`, `SEV - M2 - RUN`, `SEV - M2 - Ready`, `SEV - M2 - Speed`, `SEV - M2 - Torque actual`, `SEV - M2 - Voltage`, `SPEED Engine`, `Save Iso_Resist`, `Sevcon - CAN OK`, `Sevcon - Error mode`, `Sevcon - M3 - RUN`, `Sevcon - Ready`, `Sevcon - Voltage_3`, `Show Debug`, `Show P-1-2`, `Show_Elec`, `Show_Thermic`, `ShuntDown Action`, `ShuntDown Confirmed`, `ShuntDown Message`, `ShuntDown Turn Off`, `ShuntDown Wait`, `Speed`, `Speed Data`, `Speed Int`, `Speed Mode`, `Speed Pump`, `Speed State`, `Speed_RPM`, `Start 3 s`, `State`, `State All Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `State Up/Down`, `State Up/Down Raw`, `Stop Cruise`, `Stop To Move`, `Stop in :`, `Store TIMER UP/DOWN`, `Stuffing`, `Stuffing`, `Sunrise`, `Sunset`, `Super Ok Tension Math`, `Super Ok tension`, `Switch Battery`, `System Shutdown`, `System Started`, `SÃ©curitÃ© hydraulique`, `TRACK DOWN`, `TRACK UP`, `Temperature od charger`, `Tension State`, `Test Mode`, `Thermic Engine STATE`, `Time_Diff_MEM`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer Fan`, `Timer UP/DOWN`, `Timer charging`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Toggle Free`, `Track DOWN Delay`, `Track Tension Error`, `Track UP Delay`, `Tracks pressure Mode`, `Trigger`, `Trigger HeartBeat`, `Trigger Speed`, `Trigger Timer`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `Unlock`, `Untingthen`, `VARIATOR ON`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR SUPER ON`, `VARIATOR Wait OFF`, `VIEW BAT Charging`, `VIEW BAT Ready`, `VIEW BAT Run`, `VIEW BUTTON States`, `VIEW ENGINE RUN PAGE`, `VIEW SOC`, `VIEW SPEED STATE`, `VIEW START PAGE`, `Var Power`, `Variator State`, `Variator hour`, `Wait Bad Pressure`, `Wait Buz 2`, `Wait Hot Temperature`, `Wait Oil Level`, `Wait after stating`, `Wait batt ON`, `Wait during start`, `Wait engine Stop`, `Wait engine start`, `Wait_Very_Low_Oil_Level`, `Warning 1 - MEM`, `Warning 2 - MEM`, `WattAlps - Battery InstantVoltage`, `WattAlps - CAN OK`, `WattAlps - CURRENT`, `WattAlps - Cell_T_max_Master`, `WattAlps - DRIVE MODE`, `WattAlps - HighCellVoltage`, `WattAlps - Iso_Resist`, `WattAlps - LowCellVoltage`, `WattAlps - SOC`, `WattAlps- Max Current`, `WattAlps- U_Trac`, `WattApls- ERROR DIGIT`, `Works Latitude`, `Year since 2000`, `ZAPI_M1_Batterie Current`, `ZAPI_M1_Batterie Voltage`, `ZAPI_M1_CAN OK`, `ZAPI_M1_Error mode`, `ZAPI_M1_Heatsink`, `ZAPI_M1_Motor_Temp`, `ZAPI_M1_READY`, `ZAPI_M1_RUN`, `ZAPI_M1_Torque`, `ZAPI_M2_Batterie Current`, `ZAPI_M2_Batterie Voltage`, `ZAPI_M2_CAN OK`, `ZAPI_M2_Error mode`, `ZAPI_M2_Heatsink`, `ZAPI_M2_Motor_Temp`, `ZAPI_M2_READY`, `ZAPI_M2_RUN`, `ZAPI_M2_Torque`, `Event log: Battery Isolation`, `Event log: Check UP`, `Event log: Electronic Logs`, `Event log: Hydraulic Event`, `Event log: Thermic Events`, `Statistics log: Electric Stats`, `Statistics log: System Stats`, `Statistics log: Thermic Stats`
- Ligne export : 14610 · id 54805

#### OIL security  `SP`
- Propriétés : Input channel=None · Default state name=ACTIVE · States={Unactive}
- Utilisé par : ``
- Ligne export : 14635 · id 61515

####   `MEM`
- Propriétés : Name, English=OIL Security · Input channel=OIL security · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : ``, `OIL security`, `Reset Startup`
- Utilisé par : ``, ``, `10 fail Starting`, `10 hours check-up`, `10 hours check-up`, `10 minutes auto tender`, `1552 - Hardware enable - IDC`, `1553 - Actual battery output voltage`, `1553 - Actual mains current`, `1553 - Actual mains voltage`, `1553 - output current to the battery`, `1555 - Power stage temperature - Byte`, `1560 - Desired Current`, `1560 - Desired Voltage`, `1560 - Max Current from 230 V`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Adress Loose`, `Adress_Search`, `Adresse_Mem`, `Allow Cruise`, `Allow Run Cruise`, `Auto Fast after Down`, `Auto Fast after Down Wait`, `Auto Off`, `Auto Off Bip`, `Auto Off Confirmed`, `Auto PAUSE/OFF`, `Auto Stop Timer`, `BATT - Reset`, `BMS_Iso_Resist`, `BMS_U_Trac`, `BMW - DRIVE MODE`, `BMW - ERROR DIGIT`, `BMW - Frequency`, `BMW - Iso_Resist`, `BMW - Main current`, `BMW - Output Voltage`, `BMW - Output current`, `BMW - SOC`, `BMW - Status`, `BMW CAN OK`, `BMW CAN OK`, `BMW Charging`, `BMW Connected`, `BMW Error`, `BMW Ready`, `Backlight Value`, `Backward Curent`, `Bad pressure`, `Balancing Counter`, `Balancing State`, `Bat - 100A-125A`, `Bat - 1A-25A`, `Bat - 25A-50A`, `Bat - 50A-75A`, `Bat - 75A-100A`, `Bat - up to 125A`, `Bat CMD`, `Bat Counter`, `BatNodeState`, `Batterie State`, `Battery CAN OK`, `Battery CHARGED`, `Battery CMD`, `Battery DRIVE MODE`, `Battery ERROR DIGIT`, `Battery Error Code`, `Battery Error Durring 5 s`, `Battery HIGHT TEMP`, `Battery InstantVoltage`, `Battery NEED TO CHARGE`, `Battery POWER`, `Battery Protection`, `Battery Protection`, `Battery SOC`, `Battery SOC Costumer`, `Battery STATE`, `Battery State MEM`, `Battery not need to charge`, `Battery start by charger`, `Bip`, `Bloc`, `Brake`, `Brake`, `Brake Activation`, `Brusa CAN OK`, `Brusa Charging`, `Brusa Connected`, `Brusa Error`, `Brusa ready`, `C`, `CMD`, `CMD`, `Calcul AccÃ©lÃ©ration`, `CanBus Error TB`, `CanOn Wait`, `Cell_T_max_Master`, `Charge`, `Charge Mode`, `Charge start state`, `Charger CAN BUS OK`, `Charger CHARGING`, `Charger CONNECT to 220V`, `Charger Connected`, `Charger DIGITAL CMD`, `Charger ERROR`, `Charger Output Current`, `Charger READY`, `Charger STATE`, `Charger State Finite`, `Charger end charge`, `Command State`, `Convert Left`, `Convert Right`, `CouchÃ© night`, `Counter`, `Couple Moteur`, `Couple Moteur`, `Current Bat`, `Current Date MEN`, `Cuurent Bat (ABS)`, `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `DOWN Counter`, `Days in current year`, `DcuNodeState`, `Dec`, `Delay Off super ok tension`, `DiffCellVoltage`, `Don'push button`, `DurÃ©e`, `EMERG`, `EMERG`, `ENGINE RUN`, `ENGINE RUN`, `ET`, `ET h`, `Elcon - output Voltage`, `Elcon - output current`, `Elcon CAN OK`, `Elcon Charging`, `Elcon Connected`, `Elcon Error`, `Elcon Ready`, `Electric Engine STATE`, `Emmergency Stop Left`, `Emmergency Stop Right`, `Enable`, `Enable`, `Engine Stopped`, `Engine Temps`, `Engine hours`, `Engine hydro`, `Engine hydro Speed`, `Engines Not Ready`, `Error 1 - MEM`, `Error 1 - MEM`, `Error 2 - MEM`, `Error 2 - MEM`, `Error 3 - MEM`, `Error Iso_Resist`, `Error Wait`, `Error Wait`, `F4 Off`, `FAN OUT`, `FS1 Switch`, `FS1 Switch`, `Fail Start Counter`, `Fail Starting`, `Fordward Left`, `Fordward Right`, `Forward`, `Forward`, `Forward Curent`, `Func State`, `Func State`, `GPS Adresse Find`, `GPS_Adresse_Find_Int`, `Garmin - NMEA`, `Global Auto Off Timer`, `HIGH`, `HeartBeat`, `HeartBeat`, `Heatsink`, `HighCellVoltage`, `Ho`, `Ho_night`, `Hot Oil`, `Hour actual`, `Hydraulic pump statut`, `ID Fault`, `ID Prog`, `IDC Auto Sleep`, `IDC Batt Protection`, `IDC Free`, `IDC Speed Free`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `IDC Tension`, `If not start`, `Iguana PIN`, `Init Counter`, `Init Seq`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter EV By Pass`, `Inter EV DOWN`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP`, `Inter EV UP Delay`, `Inter EV Verin`, `Inter EV tendre Chenille`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Is_BMW`, `Is_Charger_BMW`, `Is_Charger_Brusa`, `Is_Charger_Elcon`, `Is_Electric`, `Is_Electric_MD3`, `Is_M3_Sevcon`, `Is_MT_Sevcon`, `Is_MT_Zapi`, `Is_Thermic`, `Is_Thermic_MD3`, `Is_WattAlps`, `IsoMonNodeState`, `Joystick Zero`, `Joystick Zero`, `Joystick not zero`, `Joystick to zero CMSG`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `K1 Fan Rear / Fan`, `K1 fuse is blown`, `K10`, `K10 fuse is blown`, `K11`, `K11 fuse is blown`, `K12`, `K12 fuse is blown`, `K13`, `K13 fuse is blown`, `K2 Fan Super / Pump`, `K2 fuse is blown`, `K3 Fan Exhaust / AutoOff`, `K3 fuse is blown`, `K4 Engine Power / Search Lights`, `K4 fuse is blown`, `K5 Engine Start`, `K5 fuse is blown`, `K6 Aux 1`, `K6 fuse is blown`, `K7 Aux 2`, `K7 fuse is blown`, `K8`, `K8 fuse is blown`, `K9`, `K9 fuse is blown`, `Keep ON`, `KeyBox Can Ok`, `Ko to move`, `L`, `LOW`, `Latence Math`, `LatenceTimer`, `Latitude Compute`, `Latitude Compute MEN`, `Left Error`, `Left Warning`, `LevÃ© night`, `Libre`, `Lock`, `Locking Phase Duration`, `Lon`, `Longitude Compute`, `Longitude Compute MEN`, `LowCellVoltage`, `M`, `M1 - 100A-125A`, `M1 - 25A-50A`, `M1 - 50A-75A`, `M1 - 75A-100A`, `M1 - CAN OK`, `M1 - CURRENT`, `M1 - Charge`, `M1 - ENGINE HOT`, `M1 - Error mode`, `M1 - Heatsink`, `M1 - KTY`, `M1 - Mechanical power`, `M1 - NEED TO FAN`, `M1 - NEED TO PUMP`, `M1 - New Error Code`, `M1 - Normal Mode`, `M1 - RUN`, `M1 - Ready`, `M1 - Right Engine CMSG`, `M1 - Speed`, `M1 - Torque`, `M1 - Torque Tracks`, `M1 - Voltage`, `M1 - Zapi New Error Code`, `M1 - Zapi New Warning Code`, `M1 - up to 125A`, `M2 - 100A-125A`, `M2 - 25A-50A`, `M2 - 50A-75A`, `M2 - 75A-100A`, `M2 - CAN OK`, `M2 - CURRENT`, `M2 - Charge`, `M2 - ENGINE HOT`, `M2 - Error mode`, `M2 - Heatsink`, `M2 - KTY`, `M2 - Left Engine CMSG`, `M2 - Mechanical power`, `M2 - NEED TO FAN`, `M2 - NEED TO PUMP`, `M2 - New Error Code`, `M2 - Normal mode`, `M2 - RUN`, `M2 - Ready`, `M2 - Speed`, `M2 - Torque`, `M2 - Torque tracks`, `M2 - Voltage`, `M2 - ZAPI - New Warning Code`, `M2 - Zapi - New Error Code`, `M2 - up to 125A`, `M3  (Pump) - Filter`, `M3 - CAN OK`, `M3 - Charge`, `M3 - ENGINE HOT`, `M3 - Error mode`, `M3 - NEED TO FAN`, `M3 - NEED TO PUMP`, `M3 - New Error Code`, `M3 - Pump Engine CMSG`, `M3 - Ready`, `M3 - Run`, `M3 - Voltage`, `M3_Speed`, `MD3 - DOWN`, `MD3 - UP`, `MD4 - Start Button Blocking Neutral`, `MDGN-+BAT:MC2[1]`, `Main Switch Battery`, `Math Current`, `Math Current`, `Math Droit`, `Math Gauche`, `Math Left`, `Math Right`, `Math Voltage`, `Math Voltage`, `Max Discharge`, `Max Manip`, `Min Speed`, `Mini Wait`, `MÃ©ridian`, `NEED FAN`, `NEED MORE SPEED`, `NEED PUMP`, `Need Pressure`, `Need to Charge IDC - Public`, `Need to Charge Voltage`, `Need to Charge Voltage Wait`, `Need to charge`, `New Battery State`, `New Error Code`, `New Timer`, `OK BLOC`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `OK UP/DOWN`, `ON/OFF Var`, `ON/OFF/Untighed`, `Oil Not Good`, `Oil level`, `Oil level`, `Ok tension`, `Ok to move`, `Over Tension`, `PARKER OK`, `PDO1_RX`, `PDO1_RX`, `PDO1_TX`, `PDO1_TX`, `PDO2_TX`, `PDO2_TX`, `PIN 44`, `PIn State`, `PUMP VAR`, `Power`, `Power`, `Power`, `Power Down`, `Power Down Wait`, `Power State Int`, `Process Down Engine`, `Pump 1 Right`, `Pump 1 Right Filter ECC1`, `Pump 2 Left`, `Pump 2 Left Filter ECC1`, `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Request Parameter State`, `Reset`, `Reset`, `Reset`, `Reset Speed`, `Reset Startup`, `Reset Startup`, `Reset State`, `Reset on startup`, `Reverse`, `Reverse`, `Reverse Left`, `Reverse Right`, `Right Error`, `Right Warning`, `SARTING`, `SEV - M1 - CAN OK`, `SEV - M1 - CURRENT`, `SEV - M1 - Error mode`, `SEV - M1 - RUN`, `SEV - M1 - Ready`, `SEV - M1 - Speed`, `SEV - M1 - Torque actual`, `SEV - M1 - Voltage`, `SEV - M2 - CAN OK`, `SEV - M2 - CURRENT`, `SEV - M2 - Error mode`, `SEV - M2 - RUN`, `SEV - M2 - Ready`, `SEV - M2 - Speed`, `SEV - M2 - Torque actual`, `SEV - M2 - Voltage`, `SPEED Engine`, `Save Iso_Resist`, `Sevcon - CAN OK`, `Sevcon - Error mode`, `Sevcon - M3 - RUN`, `Sevcon - Ready`, `Sevcon - Voltage_3`, `Show Debug`, `Show P-1-2`, `Show_Elec`, `Show_Thermic`, `ShuntDown Action`, `ShuntDown Confirmed`, `ShuntDown Message`, `ShuntDown Turn Off`, `ShuntDown Wait`, `Speed`, `Speed Data`, `Speed Int`, `Speed Mode`, `Speed Pump`, `Speed State`, `Speed_RPM`, `Start 3 s`, `State`, `State All Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `State Up/Down`, `State Up/Down Raw`, `Stop Cruise`, `Stop To Move`, `Stop in :`, `Store TIMER UP/DOWN`, `Stuffing`, `Stuffing`, `Sunrise`, `Sunset`, `Super Ok Tension Math`, `Super Ok tension`, `Switch Battery`, `System Shutdown`, `System Started`, `SÃ©curitÃ© hydraulique`, `TRACK DOWN`, `TRACK UP`, `Temperature od charger`, `Tension State`, `Test Mode`, `Thermic Engine STATE`, `Time_Diff_MEM`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer Fan`, `Timer UP/DOWN`, `Timer charging`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Toggle Free`, `Track DOWN Delay`, `Track Tension Error`, `Track UP Delay`, `Tracks pressure Mode`, `Trigger`, `Trigger HeartBeat`, `Trigger Speed`, `Trigger Timer`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `Unlock`, `Untingthen`, `VARIATOR ON`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR SUPER ON`, `VARIATOR Wait OFF`, `VIEW BAT Charging`, `VIEW BAT Ready`, `VIEW BAT Run`, `VIEW BUTTON States`, `VIEW ENGINE RUN PAGE`, `VIEW SOC`, `VIEW SPEED STATE`, `VIEW START PAGE`, `Var Power`, `Variator State`, `Variator hour`, `Wait Bad Pressure`, `Wait Buz 2`, `Wait Hot Temperature`, `Wait Oil Level`, `Wait after stating`, `Wait batt ON`, `Wait during start`, `Wait engine Stop`, `Wait engine start`, `Wait_Very_Low_Oil_Level`, `Warning 1 - MEM`, `Warning 2 - MEM`, `WattAlps - Battery InstantVoltage`, `WattAlps - CAN OK`, `WattAlps - CURRENT`, `WattAlps - Cell_T_max_Master`, `WattAlps - DRIVE MODE`, `WattAlps - HighCellVoltage`, `WattAlps - Iso_Resist`, `WattAlps - LowCellVoltage`, `WattAlps - SOC`, `WattAlps- Max Current`, `WattAlps- U_Trac`, `WattApls- ERROR DIGIT`, `Works Latitude`, `Year since 2000`, `ZAPI_M1_Batterie Current`, `ZAPI_M1_Batterie Voltage`, `ZAPI_M1_CAN OK`, `ZAPI_M1_Error mode`, `ZAPI_M1_Heatsink`, `ZAPI_M1_Motor_Temp`, `ZAPI_M1_READY`, `ZAPI_M1_RUN`, `ZAPI_M1_Torque`, `ZAPI_M2_Batterie Current`, `ZAPI_M2_Batterie Voltage`, `ZAPI_M2_CAN OK`, `ZAPI_M2_Error mode`, `ZAPI_M2_Heatsink`, `ZAPI_M2_Motor_Temp`, `ZAPI_M2_READY`, `ZAPI_M2_RUN`, `ZAPI_M2_Torque`, `Event log: Battery Isolation`, `Event log: Check UP`, `Event log: Electronic Logs`, `Event log: Hydraulic Event`, `Event log: Thermic Events`, `Statistics log: Electric Stats`, `Statistics log: System Stats`, `Statistics log: Thermic Stats`
- Ligne export : 14647 · id 61517

#### Wait_Very_Low_Oil_Level  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Oil level Analog [%] < 80`
  - **Blocking** = `1 = OIL Security`
- Lit : ``, `Oil level`
- Utilisé par : `Oil Not Good`, `Oil Security Activation`, `Oil level`, `Oil level Very Low Input`, `Stop in :`, `SÃ©curitÃ© hydraulique`, `Wait_Very_Low_Oil_Level`, `Event log: Hydraulic Event`, `MD3 page: BASE`, `Statistics log: Thermic Stats`
- Ligne export : 14691 · id 54806

#### Stop in :  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=30
- Logique :
  - **Decreasing** = `Wait_Very_Low_Oil_Level`
  - **Resetting** = `(Wait_Very_Low_Oil_Level ? 0 : 100)`
- Lit : ``, `Wait_Very_Low_Oil_Level`
- Utilisé par : `Oil level`
- Ligne export : 14745 · id 54814

#### Oil level  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=Low Oil Tracks Level · Text, English=Stop Engine Immediately. And contact your service center. · Channel=Stop in : [s]
- Logique :
  - **Showing** = `Wait_Very_Low_Oil_Level`
  - **Hiding** = `not(Wait_Very_Low_Oil_Level)`
- Lit : ``, `Stop in :`, `Wait_Very_Low_Oil_Level`
- Utilisé par : ``, `Oil level`, `Wait Oil Level`, `Wait_Very_Low_Oil_Level`, `Measure group: Engine Thermic`, `Measure group: Hydraulic`
- Ligne export : 14806 · id 54825

#### Wait Oil Level  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Oil level Analog [%] < 90`
- Lit : ``, `Oil level`
- Utilisé par : `Oil level`
- Ligne export : 14862 · id 54834

#### Oil level  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header, English=Low Oil Tracks Level · Text, English=Check Oil Level and hydraulic circuit. And contact your service center. · Channel=Oil level Analog [%]
- Logique :
  - **Showing** = `Wait Oil Level`
  - **Hiding** = `not(Wait Oil Level)`
- Lit : ``, `Oil level`, `Wait Oil Level`
- Utilisé par : ``, `Wait Oil Level`, `Wait_Very_Low_Oil_Level`, `Measure group: Engine Thermic`, `Measure group: Hydraulic`
- Ligne export : 14907 · id 54842
