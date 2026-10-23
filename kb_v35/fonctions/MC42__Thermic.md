# MC42 — Thermic

173 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Thermic — actif seulement si `Is_Thermic`

#### Thermic Engine STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *STARTING* :
  - **Activating** = `Out SWITCH ON Engine`
  - **Blocking** = `System Started`
- Fonction *READY* :
  - **Activating** = `(Out SWITCH ON Engine) AND (System Started)`
- Lit : ``, `Out SWITCH ON Engine`, `System Started`
- Utilisé par : `Power State Int`
- Ligne export : 21109 · id 51442

## Thermic / Engine Speed

#### Joystick not zero  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Right CanIn [%] <> 0) OR (Left CanIn [%] <> 0)`
- Lit : ``, `Left CanIn`, `Right CanIn`
- Utilisé par : `SPEED Engine`
- Ligne export : 19177 · id 29433

#### Engine type  `SP`
- Propriétés : Input channel=None · Default state name=FORD 1.5L · States={}
- Utilisé par : `Curent  - Hight Speed`, `Curent - Low Speed`, `Curent - Super Low Speed`, `Hight Speed`, `IDLE Speed`, `Max curent`, `Min Speed`, `Slow Speed`, `Tension Speed`, `UP/DOWN Speed`, `Adjust group: Master Config`, `Single adjust item: Engine type`
- Ligne export : 19231 · id 29442

#### IDLE Speed  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: FORD 1.5L={1000}
- Lit : `Engine type`
- Utilisé par : `Calcul AccÃ©lÃ©ration`, `Adjust group: Master Thermic`, `Single adjust item: IDLE Speed`
- Ligne export : 19242 · id 29444

#### Slow Speed  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: FORD 1.5L={2300}
- Lit : `Engine type`
- Utilisé par : `Calcul AccÃ©lÃ©ration`, `Adjust group: Master Thermic`, `Single adjust item: Slow Speed`
- Ligne export : 19254 · id 29445

#### Hight Speed  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: FORD 1.5L={3000}
- Lit : `Engine type`
- Utilisé par : `Calcul AccÃ©lÃ©ration`, `Adjust group: Master Thermic`, `Single adjust item: Hight Speed`
- Ligne export : 19266 · id 29446

#### 2200 tr/min  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `SPEED Engine`, `Adjust group: Master Features`, `Single adjust item: 2200 tr/min`
- Ligne export : 19278 · id 29454

#### SPEED Engine  `SMC`
- Propriétés : Default state name=Default
- Fonction *Ralenti* :
  - **Activating** = `(Joystick not zero = 0) and (not(Inter EV Verin))`
  - **Blocking** = `(2200 tr/min) OR (Speed Input = 5)`
- Fonction *Regime PV* :
  - **Activating** = `(Speed Input = 2) OR (Speed Input = 1)`
  - **Blocking** = `(Inter EV Verin) OR (2200 tr/min)`
- Fonction *RÃ©gime GV* :
  - **Activating** = `(Speed Input = 3) OR (Speed Input = 6)`
  - **Blocking** = `(2200 tr/min) OR (Inter EV Verin)`
- Fonction *Road Cruise* :
  - **Activating** = `(Speed Input = 4) OR (Speed Input = 5)`
  - **Blocking** = `(2200 tr/min) OR (Inter EV Verin)`
- Fonction *Regim UP/DOWN* :
  - **Activating** = `Inter EV Verin`
  - **Blocking** = `2200 tr/min`
- Fonction *2200 tr/min* :
  - **Activating** = `2200 tr/min`
- Lit : ``, `2200 tr/min`, `Inter EV Verin`, `Joystick not zero`, `Speed Input`
- Utilisé par : `Calcul AccÃ©lÃ©ration`
- Ligne export : 19291 · id 29455

#### Max Manip  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxOf (Absolute)(Abs(Right CanIn [%]), Abs(Left CanIn [%]))`
- Lit : ``, `Left CanIn`, `Right CanIn`
- Utilisé par : `Calcul AccÃ©lÃ©ration`
- Ligne export : 19603 · id 29497

#### TSC1 Filter Slope  `FP`
- Propriétés : Unit=%/s · Default mode={100}
- Utilisé par : `TSC1 Filter`
- Ligne export : 19654 · id 29506

#### UP/DOWN Speed  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: FORD 1.5L={1700}
- Lit : `Engine type`
- Utilisé par : `Calcul AccÃ©lÃ©ration`, `Adjust group: Master Thermic`, `Single adjust item: UP/DOWN Speed`
- Ligne export : 19666 · id 29507

#### Min Speed  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: FORD 1.5L={1200}
- Lit : `Engine type`
- Utilisé par : `Calcul AccÃ©lÃ©ration`, `Adjust group: Master Thermic`, `Single adjust item: Min Speed`
- Ligne export : 19678 · id 29508

#### Calcul AccÃ©lÃ©ration  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed · Function selector=SPEED Engine
- Fonction *Default* :
  - **Controlling** = `1800`
- Fonction *Ralenti* :
  - **Controlling** = `IDLE Speed [rpm]`
- Fonction *Regime PV* :
  - **Controlling** = `lin(Max Manip: 0->Min Speed [rpm], 100->Slow Speed [rpm], Freeze)`
- Fonction *RÃ©gime GV* :
  - **Controlling** = `lin(Max Manip: 0->Min Speed [rpm], 100->Hight Speed [rpm], Freeze)`
- Fonction *Road Cruise* :
  - **Controlling** = `lin(Max Manip: 100->Min Speed [rpm], 0->Hight Speed [rpm], Freeze)`
- Fonction *Regim UP/DOWN* :
  - **Controlling** = `UP/DOWN Speed [rpm]`
- Fonction *2200 tr/min* :
  - **Controlling** = `2200`
- Lit : ``, `Hight Speed`, `IDLE Speed`, `Max Manip`, `Min Speed`, `SPEED Engine`, `Slow Speed`, `UP/DOWN Speed`
- Utilisé par : `Speed_RPM`
- Ligne export : 19690 · id 29509

#### SARTING  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  - **Activating** = `PositiveFlank(System Started)`
- Lit : ``, `System Started`
- Utilisé par : `NEED MORE SPEED`
- Ligne export : 19933 · id 29583

#### NEED MORE SPEED  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `(Inter EV tendre Chenille and (Engine speed [rpm] < 1500)) OR SARTING`
- Lit : ``, `Engine speed`, `Inter EV tendre Chenille`, `SARTING`
- Utilisé par : `Speed_RPM`
- Ligne export : 19977 · id 29559

#### Tension Speed  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: FORD 1.5L={1800}
- Lit : `Engine type`
- Utilisé par : `Speed_RPM`, `Adjust group: Master Thermic`, `Single adjust item: Tension Speed`
- Ligne export : 20045 · id 29570

#### Speed_RPM  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxOf((NEED MORE SPEED * Tension Speed [rpm]), Calcul AccÃ©lÃ©ration [rpm])`
- Lit : ``, `Calcul AccÃ©lÃ©ration`, `NEED MORE SPEED`, `Tension Speed`
- Utilisé par : `Speed`, `Speed Data`
- Ligne export : 20057 · id 29571

#### Speed Data  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Speed_RPM [rpm]: 1000->0, 4000->100, Freeze)`
- Lit : ``, `Speed_RPM`
- Utilisé par : `TSC1 Filter`
- Ligne export : 20110 · id 35858

#### TSC1 Filter  `SFC`
- Propriétés : Input channel=Speed Data [%] · Enable=Yes · Type=Slopes · Slopes={{TSC1 Filter Slope [%/s]; TSC1 Filter Slope [%/s]}; {TSC1 Filter Slope [%/s]; TSC1 Filter Slope [%/s]}}
- Lit : `Speed Data`, `TSC1 Filter Slope`
- Utilisé par : `TSC1-A:J1939-0`, `Measure group: Engine Thermic`
- Ligne export : 20157 · id 29581

#### TSC1-A:J1939-0  `TSC1`
- Propriétés : J1939 source address=Default · Engine speed limits={1000; 4000} · Speed channel=TSC1 Filter [%] · Priority=3 · Transmit rate=20 · Override control mode=Speed control · Speed control conditions=Transient optimized, disengaged · Override control mode priority=Highest · Use checksum/counter=No · Control purpose=P32 = Temporary Powertrain Control (Original use of TSC1 Command) · Module=Inboard Engine (J1939[0]) · Module index=0
- Lit : `Control`, `Speed`, `TSC1 Filter`
- Utilisé par : `Measure group: Engine Thermic`
- Ligne export : 20175 · id 29582

## Thermic / Oil security

#### Hydraulic pump statut  `VIN`
- Propriétés : Unit=Bar · Reference voltage=Reference voltage A · Error value=0 · Calibration={500; 4500; 0; 30} · Alarms={No; 0; No; 100} · Module=MC42 (MC42[1]) · Module index=5
- Lit : ``
- Utilisé par : `Wait Bad Pressure`, `Measure group: Hydraulic`
- Ligne export : 17232 · id 35669

#### Check Pump  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Wait Bad Pressure`, `Adjust group: Master Pump`, `Single adjust item: Check Pump`
- Ligne export : 17256 · id 35683

#### Wait Bad Pressure  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `Engine_Started AND (Hydraulic pump statut [Bar] <= 10) AND (Check Pump)`
- Lit : ``, `Check Pump`, `Engine_Started`, `Hydraulic pump statut`
- Utilisé par : `Bad pressure`, `SÃ©curitÃ© hydraulique`, `Event log: Thermic Events`, `MD3 page: Thermic`, `Statistics log: Thermic Stats`
- Ligne export : 17269 · id 29815

#### SÃ©curitÃ© hydraulique  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Wait Bad Pressure) OR Wait_Very_Low_Oil_Level`
- Lit : ``, `Wait Bad Pressure`, `Wait_Very_Low_Oil_Level`
- Utilisé par : *(personne)*
- Ligne export : 17328 · id 29824

#### Bad pressure  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=Hydraulic pump lubrification failure · Text, English=Stop Engine Immediately. And contact your service center.
- Logique :
  - **Showing** = `Wait Bad Pressure`
- Lit : ``, `Wait Bad Pressure`
- Utilisé par : *(personne)*
- Ligne export : 17378 · id 29834

#### Oil Temps  `VIN`
- Propriétés : Unit=Â°C · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-ST · Calibration={250; 4750; -50; 150} · Alarms={No; 0; No; 100} · Module=MC42 (MC42[1]) · Module index=4
- Utilisé par : `ECC1_Oil_Temp`, `Hot Oil`, `Inter Full Fan`, `Wait Hot Temperature`, `Measure group: Engine and Translation`, `Measure group: Hydraulic`
- Ligne export : 17426 · id 32974

#### Wait Hot Temperature  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `Engine_Started AND (Oil Temps [Â°C] >= 95)`
- Lit : ``, `Engine_Started`, `Oil Temps`
- Utilisé par : `Hot Oil`
- Ligne export : 17450 · id 33629

#### Hot Oil  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header=Hydraulic Oil is to hot. · Text=Use the low speed. · Channel=Oil Temps [Â°C]
- Logique :
  - **Showing** = `Wait Hot Temperature`
  - **Hiding** = `not(Wait Hot Temperature)`
- Lit : ``, `Oil Temps`, `Wait Hot Temperature`
- Utilisé par : *(personne)*
- Ligne export : 17502 · id 33659

## Thermic / Power

#### Reset Startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset Startup`
- Lit : ``, `Reset Startup`
- Utilisé par : `Pre Fuel line ignition IDC`, `Reset Startup`, `Reset Startup`, `TEST Full Fan`
- Ligne export : 15059 · id 30494

#### Oil Security Activation  `IDC`
- Propriétés : Toggle=No · Delay on=60000 · Delay off=0
- Logique :
  - **Activating** = `Wait_Very_Low_Oil_Level`
- Lit : ``, `Wait_Very_Low_Oil_Level`
- Utilisé par : `Coupure Thermique avec sÃ©curitÃ©`
- Ligne export : 15109 · id 30513

#### MD3 STOP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `NegativeFlank(MD3_Start/Stop)`
- Lit : ``, `MD3_Start/Stop`
- Utilisé par : ``, `Coupure Thermique avec sÃ©curitÃ©`
- Ligne export : 15152 · id 30523

#### Coupure Thermique avec sÃ©curitÃ©  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MD3 STOP) OR (Oil Security Activation)`
- Lit : ``, `MD3 STOP`, `Oil Security Activation`
- Utilisé par : `Digit Engine On`, `FAN Timer`, `Memorizing Water Temp`
- Ligne export : 15196 · id 30531

#### Fuel Line Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Fuel line ignition IDC`
  - **Resetting** = `(PositiveFlank(Fuel line ignition IDC)) OR (not(Pre Fuel line ignition IDC))`
- Lit : ``, `Fuel line ignition IDC`, `Pre Fuel line ignition IDC`
- Utilisé par : `Fuel line ignition Output`, `Pre Fuel line ignition IDC`, `Progress`
- Ligne export : 15246 · id 30540

#### Fuel line ignition  `MEM`
- Propriétés : Input channel=Fuel line ignition State · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `NegativeFlank(Pre Fuel line ignition IDC)`
- Lit : ``, `Fuel line ignition State`, `Pre Fuel line ignition IDC`
- Utilisé par : `Fuel line ignition`, `Pre Fuel line ignition IDC`
- Ligne export : 15314 · id 30552

#### Starter Protection CMSG  `IMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Starter Temperature Protection · Text=Please check fuel level, battery level, oil level, fuel line, fuel filter. Do NOT start the engine more than 5 time per minute. You can start an fuel line ignition buy press RUN. · Left button=Ok · Center button=RUN
- Logique :
  - **Showing** = `Starter Proctection IDC`
  - **Hiding** = `(2 = Starter Protection CMSG) OR ((not(Fuel line ignition IDC)) and (not(Starter Proctection IDC))) OR (NegativeFlank(Fuel line ignition IDC))`
- Lit : ``, `C`, `Fuel line ignition IDC`, `Starter Proctection IDC`
- Utilisé par : `Pre Fuel line ignition IDC`
- Ligne export : 15358 · id 30569

#### Pre Fuel line ignition IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((1 = Fuel line ignition))) OR (PositiveFlank((3 = Starter Protection CMSG))) OR (Pre Fuel line ignition IDC)`
  - **Blocking** = `(Fuel Line Timer [s] > 50) OR Engine_Started OR (Reset Startup)`
- Lit : ``, `C`, `Engine_Started`, `Fuel Line Timer`, `Fuel line ignition`, `Reset Startup`, `Starter Protection CMSG`
- Utilisé par : `Fuel Line Timer`, `Fuel line ignition`, `Fuel line ignition IDC`
- Ligne export : 15448 · id 30582

#### Fuel line ignition IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Pre Fuel line ignition IDC`
  - **Blocking** = `Engine_Started`
- Lit : ``, `Engine_Started`, `Pre Fuel line ignition IDC`
- Utilisé par : `Fuel Line Timer`, `Fuel line ignition`, `MD3 START`, `Starter Protection CMSG`, `Event log: Thermic Events`
- Ligne export : 15548 · id 30597

#### Fuel line ignition State  `SP`
- Propriétés : Input channel=None · Default state name=OFF · States={RUN}
- Utilisé par : `Fuel line ignition`, `Adjust group: Maintenance`, `Single adjust item: Fuel line ignition State`
- Ligne export : 15598 · id 30606

#### Starter Protection Slope  `SFC`
- Propriétés : Input channel=Starter Protection [%] · Enable=Yes · Type=Slopes · Slopes={{10; 1}; {0; 0}}
- Lit : `Starter Protection`
- Utilisé par : `Starter Proctection IDC`
- Ligne export : 15610 · id 30616

#### Starter Proctection IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Starter Protection Slope [%] >= 150`
- Lit : ``, `Starter Protection Slope`
- Utilisé par : `Starter Protection CMSG`
- Ligne export : 15628 · id 30617

#### Out START Engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = ` OR (Start Pulse IDC)`
- Lit : ``, `Start Pulse IDC`
- Utilisé par : `Etat Engine`, `K5 Engine Start`, `Starter Protection`, `Statistics log: Thermic Stats`
- Ligne export : 15673 · id 32462

#### Starter Protection  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `1000 * Out START Engine`
- Lit : ``, `Out START Engine`
- Utilisé par : `Starter Protection Slope`
- Ligne export : 15723 · id 30626

####   `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MD3 START) OR `
  - **Blocking** = `Engine_Started OR (MD3 STOP) OR (PositiveFlank(AutoStopafter 5 secondes)) OR (not(Joystick Zero))`
- Lit : ``, `AutoStopafter 5 secondes`, `Engine_Started`, `Joystick Zero`, `MD3 START`, `MD3 STOP`
- Utilisé par : `10 fail Starting`, `10 hours check-up`, `10 hours check-up`, `1552 - Hardware enable - IDC`, `1553 - Actual battery output voltage`, `1553 - Actual mains current`, `1553 - Actual mains voltage`, `1553 - output current to the battery`, `1555 - Power stage temperature - Byte`, `1560 - Desired Current`, `1560 - Desired Voltage`, `1560 - Max Current from 230 V`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Adress Loose`, `Adress_Search`, `Adresse_Mem`, `Allow Cruise`, `Allow Run Cruise`, `Auto Fast after Down`, `Auto Fast after Down Wait`, `Auto Off`, `Auto Off Bip`, `Auto Off Confirmed`, `Auto PAUSE/OFF`, `Auto Stop Timer`, `AutoStopafter 5 secondes`, `BATT - Reset`, `BMS_Iso_Resist`, `BMS_U_Trac`, `BMW - DRIVE MODE`, `BMW - ERROR DIGIT`, `BMW - Frequency`, `BMW - Iso_Resist`, `BMW - Main current`, `BMW - Output Voltage`, `BMW - Output current`, `BMW - SOC`, `BMW - Status`, `BMW CAN OK`, `BMW CAN OK`, `BMW Charging`, `BMW Connected`, `BMW Error`, `BMW Ready`, `Backlight Value`, `Backward Curent`, `Bad pressure`, `Balancing Counter`, `Balancing State`, `Bat - 100A-125A`, `Bat - 1A-25A`, `Bat - 25A-50A`, `Bat - 50A-75A`, `Bat - 75A-100A`, `Bat - up to 125A`, `Bat CMD`, `Bat Counter`, `BatNodeState`, `Batterie State`, `Battery CAN OK`, `Battery CHARGED`, `Battery CMD`, `Battery DRIVE MODE`, `Battery ERROR DIGIT`, `Battery Error Code`, `Battery Error Durring 5 s`, `Battery HIGHT TEMP`, `Battery InstantVoltage`, `Battery NEED TO CHARGE`, `Battery POWER`, `Battery Protection`, `Battery Protection`, `Battery SOC`, `Battery SOC Costumer`, `Battery STATE`, `Battery State MEM`, `Battery not need to charge`, `Battery start by charger`, `Bip`, `Bloc`, `Brake`, `Brake`, `Brake Activation`, `Brusa CAN OK`, `Brusa Charging`, `Brusa Connected`, `Brusa Error`, `Brusa ready`, `C`, `CMD`, `CMD`, `Calcul AccÃ©lÃ©ration`, `CanBus Error TB`, `CanOn Wait`, `Cell_T_max_Master`, `Charge`, `Charge Mode`, `Charge start state`, `Charger CAN BUS OK`, `Charger CHARGING`, `Charger CONNECT to 220V`, `Charger Connected`, `Charger DIGITAL CMD`, `Charger ERROR`, `Charger Output Current`, `Charger READY`, `Charger STATE`, `Charger State Finite`, `Charger end charge`, `Command State`, `Convert Left`, `Convert Right`, `CouchÃ© night`, `Counter`, `Couple Moteur`, `Couple Moteur`, `Coupure Thermique avec sÃ©curitÃ©`, `Current Bat`, `Current Date MEN`, `Cuurent Bat (ABS)`, `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `DOWN Counter`, `Days in current year`, `DcuNodeState`, `Dec`, `DiffCellVoltage`, `Digit Engine On`, `Don'push button`, `DurÃ©e`, `EMERG`, `EMERG`, `ENGINE RUN`, `ENGINE RUN`, `ET`, `ET h`, `Elcon - output Voltage`, `Elcon - output current`, `Elcon CAN OK`, `Elcon Charging`, `Elcon Connected`, `Elcon Error`, `Elcon Ready`, `Electric Engine STATE`, `Emmergency Stop Left`, `Emmergency Stop Right`, `Enable`, `Enable`, `Engine Stopped`, `Engine Temps`, `Engine hours`, `Engine hydro`, `Engine hydro Speed`, `Engines Not Ready`, `Error 1 - MEM`, `Error 1 - MEM`, `Error 2 - MEM`, `Error 2 - MEM`, `Error 3 - MEM`, `Error Iso_Resist`, `Error Wait`, `Error Wait`, `Etat Engine`, `F4 Off`, `FAN OUT`, `FAN Processing`, `FAN Timer`, `FS1 Switch`, `FS1 Switch`, `Fail Start Counter`, `Fail Starting`, `Fordward Left`, `Fordward Right`, `Forward`, `Forward`, `Forward Curent`, `Fuel Line Timer`, `Fuel line ignition`, `Fuel line ignition`, `Fuel line ignition IDC`, `Fuel line ignition Output`, `Func State`, `Func State`, `GPS Adresse Find`, `GPS_Adresse_Find_Int`, `Garmin - NMEA`, `Global Auto Off Timer`, `HIGH`, `HeartBeat`, `HeartBeat`, `Heatsink`, `HighCellVoltage`, `Ho`, `Ho_night`, `Hot Oil`, `Hot/Cold`, `Hour actual`, `Hydraulic pump statut`, `ID Fault`, `ID Prog`, `IDC Auto Sleep`, `IDC Batt Protection`, `IDC Free`, `IDC Speed Free`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `IDC Tension`, `If not start`, `Iguana PIN`, `Init Counter`, `Init Seq`, `Inter Allumage Thermique`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter EV By Pass`, `Inter EV DOWN`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP`, `Inter EV UP Delay`, `Inter EV Verin`, `Inter EV tendre Chenille`, `Inter FAN`, `Inter Full Fan`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Is_BMW`, `Is_Charger_BMW`, `Is_Charger_Brusa`, `Is_Charger_Elcon`, `Is_Electric`, `Is_Electric_MD3`, `Is_M3_Sevcon`, `Is_MT_Sevcon`, `Is_MT_Zapi`, `Is_Thermic`, `Is_Thermic_MD3`, `Is_WattAlps`, `IsoMonNodeState`, `Joystick Zero`, `Joystick Zero`, `Joystick is not in neutral position`, `Joystick not zero`, `Joystick to zero CMSG`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `K1 Fan Rear / Fan`, `K1 fuse is blown`, `K10`, `K10 fuse is blown`, `K11`, `K11 fuse is blown`, `K12`, `K12 fuse is blown`, `K13`, `K13 fuse is blown`, `K2 Fan Super / Pump`, `K2 fuse is blown`, `K3 Fan Exhaust / AutoOff`, `K3 fuse is blown`, `K4 Engine Power / Search Lights`, `K4 fuse is blown`, `K5 Engine Start`, `K5 fuse is blown`, `K6 Aux 1`, `K6 fuse is blown`, `K7 Aux 2`, `K7 fuse is blown`, `K8`, `K8 fuse is blown`, `K9`, `K9 fuse is blown`, `Keep ON`, `KeyBox Can Ok`, `Ko to move`, `L`, `LOW`, `Latence Math`, `LatenceTimer`, `Latitude Compute`, `Latitude Compute MEN`, `Left Error`, `Left Warning`, `LevÃ© night`, `Libre`, `Lock`, `Locking Phase Duration`, `Lon`, `Longitude Compute`, `Longitude Compute MEN`, `LowCellVoltage`, `M`, `M1 - 100A-125A`, `M1 - 25A-50A`, `M1 - 50A-75A`, `M1 - 75A-100A`, `M1 - CAN OK`, `M1 - CURRENT`, `M1 - Charge`, `M1 - ENGINE HOT`, `M1 - Error mode`, `M1 - Heatsink`, `M1 - KTY`, `M1 - Mechanical power`, `M1 - NEED TO FAN`, `M1 - NEED TO PUMP`, `M1 - New Error Code`, `M1 - Normal Mode`, `M1 - RUN`, `M1 - Ready`, `M1 - Right Engine CMSG`, `M1 - Speed`, `M1 - Torque`, `M1 - Torque Tracks`, `M1 - Voltage`, `M1 - Zapi New Error Code`, `M1 - Zapi New Warning Code`, `M1 - up to 125A`, `M2 - 100A-125A`, `M2 - 25A-50A`, `M2 - 50A-75A`, `M2 - 75A-100A`, `M2 - CAN OK`, `M2 - CURRENT`, `M2 - Charge`, `M2 - ENGINE HOT`, `M2 - Error mode`, `M2 - Heatsink`, `M2 - KTY`, `M2 - Left Engine CMSG`, `M2 - Mechanical power`, `M2 - NEED TO FAN`, `M2 - NEED TO PUMP`, `M2 - New Error Code`, `M2 - Normal mode`, `M2 - RUN`, `M2 - Ready`, `M2 - Speed`, `M2 - Torque`, `M2 - Torque tracks`, `M2 - Voltage`, `M2 - ZAPI - New Warning Code`, `M2 - Zapi - New Error Code`, `M2 - up to 125A`, `M3  (Pump) - Filter`, `M3 - CAN OK`, `M3 - Charge`, `M3 - ENGINE HOT`, `M3 - Error mode`, `M3 - NEED TO FAN`, `M3 - NEED TO PUMP`, `M3 - New Error Code`, `M3 - Pump Engine CMSG`, `M3 - Ready`, `M3 - Run`, `M3 - Voltage`, `M3_Speed`, `MD3 - DOWN`, `MD3 - UP`, `MD3 START`, `MD3 STOP`, `MD4 - Start Button Blocking Neutral`, `MDGN-+BAT:MC2[1]`, `Main Switch Battery`, `Math Current`, `Math Current`, `Math Droit`, `Math Gauche`, `Math Left`, `Math Right`, `Math Timer`, `Math Voltage`, `Math Voltage`, `Max Discharge`, `Max Manip`, `Memorizing Water Temp`, `Min Speed`, `Mini Wait`, `MÃ©ridian`, `NEED FAN`, `NEED MORE SPEED`, `NEED PUMP`, `Need to Charge IDC - Public`, `Need to Charge Voltage`, `Need to Charge Voltage Wait`, `Need to charge`, `New Battery State`, `New Error Code`, `New Timer`, `OK BLOC`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `OK UP/DOWN`, `ON/OFF Var`, `OUT Full FAN`, `Oil Not Good`, `Oil Security Activation`, `Ok to move`, `Out FAN Engine`, `Out START Engine`, `Out SWITCH ON Engine`, `PARKER OK`, `PDO1_RX`, `PDO1_RX`, `PDO1_TX`, `PDO1_TX`, `PDO2_TX`, `PDO2_TX`, `PIN 44`, `PIn State`, `PUMP VAR`, `Power`, `Power`, `Power`, `Power Down`, `Power Down Wait`, `Power State Int`, `Pre Fuel line ignition IDC`, `Process Down Engine`, `Progress`, `Pump 1 Right`, `Pump 1 Right Filter ECC1`, `Pump 2 Left`, `Pump 2 Left Filter ECC1`, `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Request Parameter State`, `Reset`, `Reset`, `Reset`, `Reset Speed`, `Reset Startup`, `Reset Startup`, `Reset State`, `Reset on startup`, `Reverse`, `Reverse`, `Reverse Left`, `Reverse Right`, `Right Error`, `Right Warning`, `SARTING`, `SEV - M1 - CAN OK`, `SEV - M1 - CURRENT`, `SEV - M1 - Error mode`, `SEV - M1 - RUN`, `SEV - M1 - Ready`, `SEV - M1 - Speed`, `SEV - M1 - Torque actual`, `SEV - M1 - Voltage`, `SEV - M2 - CAN OK`, `SEV - M2 - CURRENT`, `SEV - M2 - Error mode`, `SEV - M2 - RUN`, `SEV - M2 - Ready`, `SEV - M2 - Speed`, `SEV - M2 - Torque actual`, `SEV - M2 - Voltage`, `SPEED Engine`, `Save Iso_Resist`, `Sevcon - CAN OK`, `Sevcon - Error mode`, `Sevcon - M3 - RUN`, `Sevcon - Ready`, `Sevcon - Voltage_3`, `Show Debug`, `Show P-1-2`, `Show_Elec`, `Show_Thermic`, `ShuntDown Action`, `ShuntDown Confirmed`, `ShuntDown Message`, `ShuntDown Turn Off`, `ShuntDown Wait`, `Speed`, `Speed Data`, `Speed Int`, `Speed Mode`, `Speed Pump`, `Speed State`, `Speed_RPM`, `Start 3 s`, `Start Pulse IDC`, `Starter Proctection IDC`, `Starter Protection`, `Starter Protection CMSG`, `State`, `State All Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `State Up/Down`, `State Up/Down Raw`, `Stop Cruise`, `Stop To Move`, `Store TIMER UP/DOWN`, `Stuffing`, `Stuffing`, `Sunrise`, `Sunset`, `Switch Battery`, `System Shutdown`, `System Started`, `SÃ©curitÃ© hydraulique`, `TEST Full Fan`, `TRACK DOWN`, `TRACK UP`, `Temperature od charger`, `Test Mode`, `Thermic Engine STATE`, `Time_Diff_MEM`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer FAN`, `Timer Fan`, `Timer UP/DOWN`, `Timer charging`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Toggle Free`, `Track DOWN Delay`, `Track UP Delay`, `Trigger`, `Trigger HeartBeat`, `Trigger Speed`, `Trigger Timer`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `Unlock`, `VARIATOR ON`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR SUPER ON`, `VARIATOR Wait OFF`, `VIEW BAT Charging`, `VIEW BAT Ready`, `VIEW BAT Run`, `VIEW BUTTON States`, `VIEW ENGINE RUN PAGE`, `VIEW SOC`, `VIEW SPEED STATE`, `VIEW START PAGE`, `Var Power`, `Variator State`, `Variator hour`, `Wait Bad Pressure`, `Wait Buz 2`, `Wait Hot Temperature`, `Wait SWITCH ON Engine`, `Wait after stating`, `Wait batt ON`, `Wait during start`, `Warning 1 - MEM`, `Warning 2 - MEM`, `WattAlps - Battery InstantVoltage`, `WattAlps - CAN OK`, `WattAlps - CURRENT`, `WattAlps - Cell_T_max_Master`, `WattAlps - DRIVE MODE`, `WattAlps - HighCellVoltage`, `WattAlps - Iso_Resist`, `WattAlps - LowCellVoltage`, `WattAlps - SOC`, `WattAlps- Max Current`, `WattAlps- U_Trac`, `WattApls- ERROR DIGIT`, `Works Latitude`, `Year since 2000`, `ZAPI_M1_Batterie Current`, `ZAPI_M1_Batterie Voltage`, `ZAPI_M1_CAN OK`, `ZAPI_M1_Error mode`, `ZAPI_M1_Heatsink`, `ZAPI_M1_Motor_Temp`, `ZAPI_M1_READY`, `ZAPI_M1_RUN`, `ZAPI_M1_Torque`, `ZAPI_M2_Batterie Current`, `ZAPI_M2_Batterie Voltage`, `ZAPI_M2_CAN OK`, `ZAPI_M2_Error mode`, `ZAPI_M2_Heatsink`, `ZAPI_M2_Motor_Temp`, `ZAPI_M2_READY`, `ZAPI_M2_RUN`, `ZAPI_M2_Torque`, `Event log: Battery Isolation`, `Event log: Check UP`, `Event log: Electronic Logs`, `Event log: Hydraulic Event`, `Event log: Thermic Events`, `Statistics log: Electric Stats`, `Statistics log: System Stats`, `Statistics log: Thermic Stats`
- Ligne export : 15766 · id 30634

#### AutoStopafter 5 secondes  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = ``
  - **Blocking** = `Engine_Started`
- Lit : ``, `Engine_Started`
- Utilisé par : ``, `Digit Engine On`
- Ligne export : 15846 · id 30647

#### MD3 START  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `MD3_Start/Stop`
  - **Blocking** = `Fuel line ignition IDC`
- Lit : ``, `Fuel line ignition IDC`, `MD3_Start/Stop`
- Utilisé par : ``, `Digit Engine On`, `FAN Timer`, `Joystick is not in neutral position`
- Ligne export : 15896 · id 30656

#### Start Pulse  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Start Pulse IDC`, `Adjust group: Master Features`, `Single adjust item: Start Pulse`
- Ligne export : 15946 · id 33227

#### Start Pulse IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `PositiveFlank(Start Pulse)`
- Lit : ``, `Start Pulse`
- Utilisé par : `Out START Engine`
- Ligne export : 15959 · id 33232

#### Progress  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `Fuel Line Timer [s] * 2`
- Lit : ``, `Fuel Line Timer`
- Utilisé par : `Fuel line ignition`
- Ligne export : 16003 · id 30608

#### Fuel line ignition  `CMSG`
- Propriétés : Show message=All · Dialog type=Message · Header=Fuel line ignition · Text=Please wait during fuel line ignition. (Engine need to be stop). · Channel=Progress [%]
- Logique :
  - **Showing** = `PositiveFlank(Fuel line ignition IDC)`
  - **Hiding** = `NegativeFlank(Fuel line ignition IDC)`
- Lit : ``, `Fuel line ignition`, `Fuel line ignition IDC`, `Progress`
- Utilisé par : `Pre Fuel line ignition IDC`
- Ligne export : 16046 · id 30560

#### ECU Engine  `DP`
- Propriétés : True text=ON · False text=OFF · Default mode={False}
- Utilisé par : `Inter Allumage Thermique`, `Adjust group: Master Features`, `Single adjust item: ECU Engine`
- Ligne export : 16101 · id 30667

#### Digit Engine On  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Digit Engine On) OR (MD3 START)`
  - **Blocking** = `(Coupure Thermique avec sÃ©curitÃ©) OR (PositiveFlank(AutoStopafter 5 secondes))`
- Lit : ``, `AutoStopafter 5 secondes`, `Coupure Thermique avec sÃ©curitÃ©`, `MD3 START`
- Utilisé par : `Inter Allumage Thermique`, `Inter FAN`
- Ligne export : 16114 · id 30668

#### Fuel line ignition Output  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inside((Fuel Line Timer [s] mod 10), 1, 9)`
- Lit : ``, `Fuel Line Timer`
- Utilisé par : `Inter Allumage Thermique`
- Ligne export : 16179 · id 30679

#### Inter Allumage Thermique  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `((64 = 64) and Digit Engine On) OR (ECU Engine) OR (Fuel line ignition Output)`
- Lit : ``, `Digit Engine On`, `ECU Engine`, `Fuel line ignition Output`
- Utilisé par : `Etat Engine`, `Out SWITCH ON Engine`
- Ligne export : 16234 · id 30688

#### Temp cold/hot  `FP`
- Propriétés : Unit=Â°C · Default mode={85}
- Utilisé par : `Hot/Cold`, `Adjust group: Master Thermic`, `Single adjust item: Temp cold/hot`
- Ligne export : 16309 · id 30703

#### Memorizing Water Temp  `MEM`
- Propriétés : Input channel=Engine coolant temperature [Â°C] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `(Engine coolant temperature [Â°C] <> 0) AND (PositiveFlank(Coupure Thermique avec sÃ©curitÃ©))`
- Lit : ``, `C`, `Coupure Thermique avec sÃ©curitÃ©`
- Utilisé par : `Hot/Cold`
- Ligne export : 16321 · id 30705

#### Hot/Cold  `SMC`
- Propriétés : Default state name=Water Cold
- Fonction *Water Hot* :
  - **Activating** = `Memorizing Water Temp [Â°C] > Temp cold/hot [Â°C]`
- Lit : ``, `Memorizing Water Temp`, `Temp cold/hot`
- Utilisé par : `Math Timer`
- Ligne export : 16375 · id 30715

#### Ambiante Temperature  `SP`
- Propriétés : Input channel=None · Default state name=Normal · States={High}
- Utilisé par : `Timer Fan Engine Hot`, `Timer Fan Engine cold`, `Adjust group: Setup`, `Single adjust item: Ambiante Temperature`
- Ligne export : 16417 · id 30728

#### Timer Fan Engine cold  `FP`
- Propriétés : Unit=s · Mode selector=Ambiante Temperature · Default mode: Normal={60} · Mode 1: High={120}
- Lit : `Ambiante Temperature`
- Utilisé par : `Math Timer`, `Adjust group: Master Thermic`, `Single adjust item: Timer Fan Engine cold`
- Ligne export : 16429 · id 30730

#### Timer Fan Engine Hot  `FP`
- Propriétés : Unit=s · Mode selector=Ambiante Temperature · Default mode: Normal={180} · Mode 1: High={270}
- Lit : `Ambiante Temperature`
- Utilisé par : `Math Timer`, `Adjust group: Master Thermic`, `Single adjust item: Timer Fan Engine Hot`
- Ligne export : 16443 · id 30731

#### Math Timer  `IMAC`
- Propriétés : Unit=s · Function selector=Hot/Cold
- Fonction *Water Cold* :
  - **Controlling** = `Timer Fan Engine cold [s]`
- Fonction *Water Hot* :
  - **Controlling** = `Timer Fan Engine Hot [s]`
- Lit : ``, `Hot/Cold`, `Timer Fan Engine Hot`, `Timer Fan Engine cold`
- Utilisé par : `FAN Processing`, `FAN Timer`, `Timer FAN`
- Ligne export : 16457 · id 30733

#### FAN Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=Math Timer [s]
- Logique :
  - **Decreasing** = `(Inside(FAN Timer [s], 0, Math Timer [s])) OR (PositiveFlank(Coupure Thermique avec sÃ©curitÃ©))`
  - **Resetting** = `(MD3 START) OR (PositiveFlank(Coupure Thermique avec sÃ©curitÃ©))`
- Lit : ``, `Coupure Thermique avec sÃ©curitÃ©`, `MD3 START`, `Math Timer`
- Utilisé par : `FAN Processing`, `Timer FAN`
- Ligne export : 16529 · id 30763

#### FAN Processing  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inside(FAN Timer [s], 0, Math Timer [s])`
- Lit : ``, `FAN Timer`, `Math Timer`
- Utilisé par : `Inter FAN`, `Timer FAN`
- Ligne export : 16607 · id 30787

#### Inter FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Digit Engine On) OR (FAN Processing)`
  - **Blocking** = ``
- Lit : ``, `Digit Engine On`, `FAN Processing`
- Utilisé par : `Out FAN Engine`
- Ligne export : 16653 · id 30803

#### Etat Engine  `SMC`
- Propriétés : Default state name=OFF
- Fonction *START Engine* :
  - **Activating** = `Out START Engine`
- Fonction *SWITCH ON Engine* :
  - **Activating** = `Inter Allumage Thermique`
- Lit : ``, `Inter Allumage Thermique`, `Out START Engine`
- Utilisé par : *(personne)*
- Ligne export : 16710 · id 30814

#### Full Fan Engine  `FP`
- Propriétés : Unit=Â°C · Default mode={75}
- Utilisé par : `Inter Full Fan`, `Adjust group: Master Thermic`, `Single adjust item: Full Fan Engine`
- Ligne export : 16781 · id 30826

#### Full Fan Mode  `SP`
> This channel is used to give unit and names to the MEM
- Propriétés : Input channel=None · Default state name=AUTO · States={FULL}
- Utilisé par : `Inter Full Fan`, `TEST Full Fan`, `Adjust group: Maintenance`, `Single adjust item: Full Fan Mode`
- Ligne export : 16793 · id 30827

#### TEST Full Fan  `MEM`
- Propriétés : Input channel=Full Fan Mode · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : ``, `Full Fan Mode`, `Reset Startup`
- Utilisé par : *(personne)*
- Ligne export : 16806 · id 30829

#### Full Fan Oil  `FP`
- Propriétés : Unit=Â°C · Default mode={75}
- Utilisé par : `Inter Full Fan`, `Adjust group: Master Thermic`, `Single adjust item: Full Fan Oil`
- Ligne export : 16849 · id 35949

#### Inter Full Fan  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=5000
- Logique :
  - **Activating** = `(Engine coolant temperature [Â°C] > Full Fan Engine [Â°C]) OR (1 = Full Fan Mode) OR (Oil Temps [Â°C] >= Full Fan Oil [Â°C])`
  - **Blocking** = `Engine_Stopped`
- Lit : ``, `C`, `Engine_Stopped`, `Full Fan Engine`, `Full Fan Mode`, `Full Fan Oil`, `Oil Temps`
- Utilisé par : `OUT Full FAN`
- Ligne export : 16861 · id 30837

#### Timer FAN  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `FAN Processing * lin(FAN Timer [s]: 0->0, Math Timer [s]->100, Freeze)`
- Lit : ``, `FAN Processing`, `FAN Timer`, `Math Timer`
- Utilisé par : *(personne)*
- Ligne export : 16931 · id 30848

#### Out SWITCH ON Engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter Allumage Thermique`
- Lit : ``, `Inter Allumage Thermique`
- Utilisé par : `K4 Engine Power / Search Lights`, `Thermic Engine STATE`, `Wait SWITCH ON Engine`
- Ligne export : 16987 · id 32457

#### Wait SWITCH ON Engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=200000
- Logique :
  - **Activating** = `Out SWITCH ON Engine`
- Lit : ``, `Out SWITCH ON Engine`
- Utilisé par : *(personne)*
- Ligne export : 17030 · id 30866

#### Joystick is not in neutral position  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header, English=Neutral position · Text, English=Please put jostick in neutral position before start engine.
- Logique :
  - **Showing** = `(not(Joystick Zero)) AND (PositiveFlank(MD3 START))`
- Lit : ``, `Joystick Zero`, `MD3 START`
- Utilisé par : *(personne)*
- Ligne export : 17073 · id 30874

#### Out FAN Engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Inter FAN`
- Lit : ``, `Inter FAN`
- Utilisé par : `K1 Fan Rear / Fan`, `K3 Fan Exhaust / AutoOff`
- Ligne export : 17130 · id 32467

#### OUT Full FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter Full Fan`
- Lit : ``, `Inter Full Fan`
- Utilisé par : `K2 Fan Super / Pump`, `MD3 page: Thermic`
- Ligne export : 17173 · id 32472

## Thermic / Pump

#### Min current Right Backward  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `Pump 1 Right`, `Adjust group: Master Pump`, `Single adjust item: Min current Right Backward`
- Ligne export : 20214 · id 32143

#### Max curent  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: FORD 1.5L={1150}
- Lit : `Engine type`
- Utilisé par : `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `Adjust group: Master Pump`, `Single adjust item: Max curent`
- Ligne export : 20226 · id 32144

#### Step change  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`
- Ligne export : 20238 · id 32145

#### Forward - direct corrector  `FP`
- Propriétés : Unit=% · Mode selector=Speed Pump · Default mode: Slow={0} · Mode 1: Super Slow={0} · Mode 2: Fast Speed={0}
- Lit : `Speed Pump`
- Utilisé par : `Punp 1 - Current`, `Punp 2 - Current`, `Adjust group: `, `Single adjust item: Forward - direct corrector`
- Ligne export : 20250 · id 32146

#### Curent - Low Speed  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: FORD 1.5L={900}
- Lit : `Engine type`
- Utilisé par : `Backward Curent`, `Forward Curent`, `Adjust group: Master Pump`, `Single adjust item: Curent - Low Speed`
- Ligne export : 20266 · id 32147

#### Curent  - Hight Speed  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: FORD 1.5L={1200}
- Lit : `Engine type`
- Utilisé par : `Backward Curent`, `Forward Curent`, `Adjust group: Master Pump`, `Single adjust item: Curent  - Hight Speed`
- Ligne export : 20278 · id 32148

#### Curent - Super Low Speed  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: FORD 1.5L={660}
- Lit : `Engine type`
- Utilisé par : `Backward Curent`, `Forward Curent`, `Adjust group: Master Pump`, `Single adjust item: Curent - Super Low Speed`
- Ligne export : 20290 · id 32149

#### Forward Curent  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed · Function selector=Speed Pump
- Fonction *Slow* :
  - **Controlling** = `Curent - Low Speed [mA]`
- Fonction *Super Slow* :
  - **Controlling** = `Curent - Super Low Speed [mA]`
- Fonction *Fast Speed* :
  - **Controlling** = `Curent  - Hight Speed [mA]`
- Lit : ``, `Curent  - Hight Speed`, `Curent - Low Speed`, `Curent - Super Low Speed`, `Speed Pump`
- Utilisé par : `Punp 1 - Current`, `Punp 2 - Current`
- Ligne export : 20302 · id 32150

#### Punp 1 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `Forward Curent [mA] - (Forward - direct corrector [%] *% Step change [mA])`
  - **Limiting** = `Max curent [mA]`
- Lit : ``, `Forward - direct corrector`, `Forward Curent`, `Max curent`, `Step change`
- Utilisé par : `Filter pump 1 Neg`, `Filter pump 1 Pos`
- Ligne export : 20406 · id 32172

#### Slope Fast - Low  `FP`
- Propriétés : Unit=mA/s · Default mode={200}
- Utilisé par : `Filter pump 1 Neg`, `Filter pump 1 Pos`, `Filter pump 2 Neg`, `Filter pump 2 Pos`
- Ligne export : 20466 · id 32182

#### Filter pump 1 Pos  `SFC`
- Propriétés : Input channel=Punp 1 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}; {Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}}
- Lit : `Punp 1 - Current`, `Slope Fast - Low`
- Utilisé par : `Pump 1 Right`
- Ligne export : 20478 · id 32183

#### Min current Left Backward  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `Pump 2 Left`, `Adjust group: Master Pump`, `Single adjust item: Min current Left Backward`
- Ligne export : 20496 · id 32184

#### Punp 2 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `Forward Curent [mA] + (Forward - direct corrector [%] *% Step change [mA])`
  - **Limiting** = `Max curent [mA]`
- Lit : ``, `Forward - direct corrector`, `Forward Curent`, `Max curent`, `Step change`
- Utilisé par : `Filter pump 2 Neg`, `Filter pump 2 Pos`
- Ligne export : 20508 · id 32185

#### Filter pump 2 Pos  `SFC`
- Propriétés : Input channel=Punp 2 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}; {Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}}
- Lit : `Punp 2 - Current`, `Slope Fast - Low`
- Utilisé par : `Pump 2 Left`
- Ligne export : 20568 · id 32195

#### Min current Left Fordward  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `Pump 2 Left`, `Adjust group: Master Pump`, `Single adjust item: Min current Left Fordward`
- Ligne export : 20586 · id 32196

#### Backward - direct corrector  `FP`
- Propriétés : Unit=% · Mode selector=Speed Pump · Default mode: Slow={0} · Mode 1: Super Slow={0} · Mode 2: Fast Speed={0}
- Lit : `Speed Pump`
- Utilisé par : `Punp 1 - Current`, `Punp 2 - Current`, `Adjust group: `, `Single adjust item: Backward - direct corrector`
- Ligne export : 20598 · id 32197

#### Backward Curent  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed · Function selector=Speed Pump
- Fonction *Slow* :
  - **Controlling** = `Curent - Low Speed [mA]`
- Fonction *Super Slow* :
  - **Controlling** = `Curent - Super Low Speed [mA]`
- Fonction *Fast Speed* :
  - **Controlling** = `Curent  - Hight Speed [mA]`
- Lit : ``, `Curent  - Hight Speed`, `Curent - Low Speed`, `Curent - Super Low Speed`, `Speed Pump`
- Utilisé par : `Punp 1 - Current`, `Punp 2 - Current`
- Ligne export : 20614 · id 32201

#### Punp 2 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `Backward Curent [mA] + (Backward - direct corrector [%] *% Step change [mA])`
  - **Limiting** = `Max curent [mA]`
- Lit : ``, `Backward - direct corrector`, `Backward Curent`, `Max curent`, `Step change`
- Utilisé par : `Filter pump 2 Neg`, `Filter pump 2 Pos`
- Ligne export : 20718 · id 32223

#### Filter pump 2 Neg  `SFC`
- Propriétés : Input channel=Punp 2 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}; {Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}}
- Lit : `Punp 2 - Current`, `Slope Fast - Low`
- Utilisé par : `Pump 2 Left`
- Ligne export : 20778 · id 32233

#### Pump 2 Left Filter ECC1  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Left Filter [%] * ECC1 Integrating`
- Lit : ``, `ECC1 Integrating`, `Left Filter`
- Utilisé par : `Pump 2 Left`
- Ligne export : 20796 · id 32367

#### Pump 1 Right Filter ECC1  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Right Filter [%] * ECC1 Integrating`
- Lit : ``, `ECC1 Integrating`, `Right Filter`
- Utilisé par : `Pump 1 Right`
- Ligne export : 20848 · id 32377

#### Min current Right Fordward  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `Pump 1 Right`, `Adjust group: Master Pump`, `Single adjust item: Min current Right Fordward`
- Ligne export : 20900 · id 32235

#### Punp 1 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `Backward Curent [mA] - (Backward - direct corrector [%] *% Step change [mA])`
  - **Limiting** = `Max curent [mA]`
- Lit : ``, `Backward - direct corrector`, `Backward Curent`, `Max curent`, `Step change`
- Utilisé par : `Filter pump 1 Neg`, `Filter pump 1 Pos`
- Ligne export : 20912 · id 32236

#### Filter pump 1 Neg  `SFC`
- Propriétés : Input channel=Punp 1 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}; {Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}}
- Lit : `Punp 1 - Current`, `Slope Fast - Low`
- Utilisé par : `Pump 1 Right`
- Ligne export : 20972 · id 32246

#### Pump 1 Right  `COUT`
- Propriétés : Bidirectional=Yes · BWL=0 · Input channel=Pump 1 Right Filter ECC1 [%] · Default mode={{Min current Right Fordward [mA]; Filter pump 1 Pos [mA]; 0; 0}; {Min current Right Backward [mA]; Filter pump 1 Neg [mA]; 0; 0}} · Module=MC42 (MC42[1]) · Module index=0
- Lit : ``, `Filter pump 1 Neg`, `Filter pump 1 Pos`, `Min current Right Backward`, `Min current Right Fordward`, `Pump 1 Right Filter ECC1`
- Utilisé par : `Measure group: Engine and Translation`
- Ligne export : 20990 · id 32234

#### Pump 2 Left  `COUT`
- Propriétés : Bidirectional=Yes · BWL=0 · Input channel=Pump 2 Left Filter ECC1 [%] · Default mode={{Min current Left Fordward [mA]; Filter pump 2 Pos [mA]; 0; 0}; {Min current Left Backward [mA]; Filter pump 2 Neg [mA]; 0; 0}} · Module=MC42 (MC42[1]) · Module index=1
- Lit : ``, `Filter pump 2 Neg`, `Filter pump 2 Pos`, `Min current Left Backward`, `Min current Left Fordward`, `Pump 2 Left Filter ECC1`
- Utilisé par : `Measure group: Engine and Translation`
- Ligne export : 21016 · id 32247

#### Brake Slope  `IP`
- Propriétés : Unit=ms · Mode selector=Speed Pump · Default mode: Slow={750} · Mode 1: Super Slow={1000} · Mode 2: Fast Speed={4000}
- Lit : `Speed Pump`
- Utilisé par : `Inter EV Frein`
- Ligne export : 21042 · id 32311

#### Inter EV Frein  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=Brake Slope [ms]
- Logique :
  - **Activating** = `Brake Activation`
  - **Blocking** = `Engine_Stopped`
- Lit : ``, `Brake Activation`, `Brake Slope`, `Engine_Stopped`
- Utilisé par : `PIN 44`
- Ligne export : 21058 · id 32312

## Thermic / SAEJ Std input

#### Engine Temperature  `JFIN`
> ET1
- Propriétés : Priority=6 · PGN=65262 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine coolant temperature [Â°C]; 1}} · Module=Inboard Engine (J1939[0]) · Module index=1
- Lit : `C`
- Utilisé par : *(personne)*
- Ligne export : 18153 · id 29977

####   `JPIN`
- Propriétés : Name, English=Engine coolant temperature · Unit=Â°C · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-40 · Error value=0
- Utilisé par : ``, `10 fail Starting`, `10 hours check-up`, `10 hours check-up`, `1552 - Hardware enable - IDC`, `1553 - Actual battery output voltage`, `1553 - Actual mains current`, `1553 - Actual mains voltage`, `1553 - output current to the battery`, `1555 - Power stage temperature - Byte`, `1560 - Desired Current`, `1560 - Desired Voltage`, `1560 - Max Current from 230 V`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Adress Loose`, `Adress_Search`, `Adresse_Mem`, `Allow Cruise`, `Allow Run Cruise`, `Auto Fast after Down`, `Auto Fast after Down Wait`, `Auto Off`, `Auto Off Bip`, `Auto Off Confirmed`, `Auto PAUSE/OFF`, `Auto Stop Timer`, `BATT - Reset`, `BMS_Iso_Resist`, `BMS_U_Trac`, `BMW - DRIVE MODE`, `BMW - ERROR DIGIT`, `BMW - Frequency`, `BMW - Iso_Resist`, `BMW - Main current`, `BMW - Output Voltage`, `BMW - Output current`, `BMW - SOC`, `BMW - Status`, `BMW CAN OK`, `BMW CAN OK`, `BMW Charging`, `BMW Connected`, `BMW Error`, `BMW Ready`, `Backlight Value`, `Backward Curent`, `Bad pressure`, `Balancing Counter`, `Balancing State`, `Bat - 100A-125A`, `Bat - 1A-25A`, `Bat - 25A-50A`, `Bat - 50A-75A`, `Bat - 75A-100A`, `Bat - up to 125A`, `Bat CMD`, `Bat Counter`, `BatNodeState`, `Batterie State`, `Battery CAN OK`, `Battery CHARGED`, `Battery CMD`, `Battery DRIVE MODE`, `Battery ERROR DIGIT`, `Battery Error Code`, `Battery Error Durring 5 s`, `Battery HIGHT TEMP`, `Battery InstantVoltage`, `Battery NEED TO CHARGE`, `Battery POWER`, `Battery Protection`, `Battery Protection`, `Battery SOC`, `Battery SOC Costumer`, `Battery STATE`, `Battery State MEM`, `Battery not need to charge`, `Battery start by charger`, `Bip`, `Bloc`, `Brake`, `Brake`, `Brake Activation`, `Brusa CAN OK`, `Brusa Charging`, `Brusa Connected`, `Brusa Error`, `Brusa ready`, `C`, `CMD`, `CMD`, `Calcul AccÃ©lÃ©ration`, `CanBus Error TB`, `CanOn Wait`, `Cell_T_max_Master`, `Charge`, `Charge Mode`, `Charge start state`, `Charger CAN BUS OK`, `Charger CHARGING`, `Charger CONNECT to 220V`, `Charger Connected`, `Charger DIGITAL CMD`, `Charger ERROR`, `Charger Output Current`, `Charger READY`, `Charger STATE`, `Charger State Finite`, `Charger end charge`, `Command State`, `Convert Left`, `Convert Right`, `CouchÃ© night`, `Counter`, `Couple Moteur`, `Couple Moteur`, `Current Bat`, `Current Date MEN`, `Cuurent Bat (ABS)`, `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `DOWN Counter`, `Days in current year`, `DcuNodeState`, `Dec`, `DiffCellVoltage`, `Don'push button`, `DurÃ©e`, `ECC1 Integrating`, `EMERG`, `EMERG`, `ENGINE RUN`, `ENGINE RUN`, `ET`, `ET h`, `Elcon - output Voltage`, `Elcon - output current`, `Elcon CAN OK`, `Elcon Charging`, `Elcon Connected`, `Elcon Error`, `Elcon Ready`, `Electric Engine STATE`, `Emmergency Stop Left`, `Emmergency Stop Right`, `Enable`, `Enable`, `Engine Stopped`, `Engine Temps`, `Engine hours`, `Engine hydro`, `Engine hydro Speed`, `Engine_Started`, `Engine_Stopped`, `Engines Not Ready`, `Error 1 - MEM`, `Error 1 - MEM`, `Error 2 - MEM`, `Error 2 - MEM`, `Error 3 - MEM`, `Error Iso_Resist`, `Error Wait`, `Error Wait`, `F4 Off`, `FAN OUT`, `FS1 Switch`, `FS1 Switch`, `Fail Start Counter`, `Fail Starting`, `Fordward Left`, `Fordward Right`, `Forward`, `Forward`, `Forward Curent`, `Func State`, `Func State`, `GPS Adresse Find`, `GPS_Adresse_Find_Int`, `Garmin - NMEA`, `Global Auto Off Timer`, `HIGH`, `HeartBeat`, `HeartBeat`, `Heatsink`, `HighCellVoltage`, `Ho`, `Ho_night`, `Hot Oil`, `Hot Water`, `Hour actual`, `Hydraulic pump statut`, `ID Fault`, `ID Prog`, `IDC Auto Sleep`, `IDC Batt Protection`, `IDC Free`, `IDC Speed Free`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `IDC Tension`, `If not start`, `Iguana PIN`, `Init Counter`, `Init Seq`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter EV By Pass`, `Inter EV DOWN`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP`, `Inter EV UP Delay`, `Inter EV Verin`, `Inter EV tendre Chenille`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Is_BMW`, `Is_Charger_BMW`, `Is_Charger_Brusa`, `Is_Charger_Elcon`, `Is_Electric`, `Is_Electric_MD3`, `Is_M3_Sevcon`, `Is_MT_Sevcon`, `Is_MT_Zapi`, `Is_Thermic`, `Is_Thermic_MD3`, `Is_WattAlps`, `IsoMonNodeState`, `Joystick Zero`, `Joystick Zero`, `Joystick not zero`, `Joystick to zero CMSG`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `K1 Fan Rear / Fan`, `K1 fuse is blown`, `K10`, `K10 fuse is blown`, `K11`, `K11 fuse is blown`, `K12`, `K12 fuse is blown`, `K13`, `K13 fuse is blown`, `K2 Fan Super / Pump`, `K2 fuse is blown`, `K3 Fan Exhaust / AutoOff`, `K3 fuse is blown`, `K4 Engine Power / Search Lights`, `K4 fuse is blown`, `K5 Engine Start`, `K5 fuse is blown`, `K6 Aux 1`, `K6 fuse is blown`, `K7 Aux 2`, `K7 fuse is blown`, `K8`, `K8 fuse is blown`, `K9`, `K9 fuse is blown`, `Keep ON`, `KeyBox Can Ok`, `Ko to move`, `L`, `LOW`, `Latence Math`, `LatenceTimer`, `Latitude Compute`, `Latitude Compute MEN`, `Led Temp Water`, `Left Error`, `Left Warning`, `LevÃ© night`, `Libre`, `Lock`, `Locking Phase Duration`, `Lon`, `Longitude Compute`, `Longitude Compute MEN`, `LowCellVoltage`, `M`, `M1 - 100A-125A`, `M1 - 25A-50A`, `M1 - 50A-75A`, `M1 - 75A-100A`, `M1 - CAN OK`, `M1 - CURRENT`, `M1 - Charge`, `M1 - ENGINE HOT`, `M1 - Error mode`, `M1 - Heatsink`, `M1 - KTY`, `M1 - Mechanical power`, `M1 - NEED TO FAN`, `M1 - NEED TO PUMP`, `M1 - New Error Code`, `M1 - Normal Mode`, `M1 - RUN`, `M1 - Ready`, `M1 - Right Engine CMSG`, `M1 - Speed`, `M1 - Torque`, `M1 - Torque Tracks`, `M1 - Voltage`, `M1 - Zapi New Error Code`, `M1 - Zapi New Warning Code`, `M1 - up to 125A`, `M2 - 100A-125A`, `M2 - 25A-50A`, `M2 - 50A-75A`, `M2 - 75A-100A`, `M2 - CAN OK`, `M2 - CURRENT`, `M2 - Charge`, `M2 - ENGINE HOT`, `M2 - Error mode`, `M2 - Heatsink`, `M2 - KTY`, `M2 - Left Engine CMSG`, `M2 - Mechanical power`, `M2 - NEED TO FAN`, `M2 - NEED TO PUMP`, `M2 - New Error Code`, `M2 - Normal mode`, `M2 - RUN`, `M2 - Ready`, `M2 - Speed`, `M2 - Torque`, `M2 - Torque tracks`, `M2 - Voltage`, `M2 - ZAPI - New Warning Code`, `M2 - Zapi - New Error Code`, `M2 - up to 125A`, `M3  (Pump) - Filter`, `M3 - CAN OK`, `M3 - Charge`, `M3 - ENGINE HOT`, `M3 - Error mode`, `M3 - NEED TO FAN`, `M3 - NEED TO PUMP`, `M3 - New Error Code`, `M3 - Pump Engine CMSG`, `M3 - Ready`, `M3 - Run`, `M3 - Voltage`, `M3_Speed`, `MD3 - DOWN`, `MD3 - UP`, `MD4 - Start Button Blocking Neutral`, `MDGN-+BAT:MC2[1]`, `Main Switch Battery`, `Math Current`, `Math Current`, `Math Droit`, `Math Gauche`, `Math Left`, `Math Right`, `Math Voltage`, `Math Voltage`, `Max Discharge`, `Max Manip`, `Min Speed`, `Mini Wait`, `MÃ©ridian`, `NEED FAN`, `NEED MORE SPEED`, `NEED PUMP`, `Need to Charge IDC - Public`, `Need to Charge Voltage`, `Need to Charge Voltage Wait`, `Need to charge`, `New Battery State`, `New Error Code`, `New Timer`, `OK BLOC`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `OK UP/DOWN`, `ON/OFF Var`, `Oil Not Good`, `Oil pressure`, `Ok to move`, `PARKER OK`, `PDO1_RX`, `PDO1_RX`, `PDO1_TX`, `PDO1_TX`, `PDO2_TX`, `PDO2_TX`, `PIN 44`, `PIn State`, `PUMP VAR`, `Power`, `Power`, `Power`, `Power Down`, `Power Down Wait`, `Power State Int`, `Process Down Engine`, `Pump 1 Right`, `Pump 1 Right Filter ECC1`, `Pump 2 Left`, `Pump 2 Left Filter ECC1`, `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Request Parameter State`, `Reset`, `Reset`, `Reset`, `Reset Speed`, `Reset Startup`, `Reset State`, `Reset on startup`, `Reverse`, `Reverse`, `Reverse Left`, `Reverse Right`, `Right Error`, `Right Warning`, `SARTING`, `SEV - M1 - CAN OK`, `SEV - M1 - CURRENT`, `SEV - M1 - Error mode`, `SEV - M1 - RUN`, `SEV - M1 - Ready`, `SEV - M1 - Speed`, `SEV - M1 - Torque actual`, `SEV - M1 - Voltage`, `SEV - M2 - CAN OK`, `SEV - M2 - CURRENT`, `SEV - M2 - Error mode`, `SEV - M2 - RUN`, `SEV - M2 - Ready`, `SEV - M2 - Speed`, `SEV - M2 - Torque actual`, `SEV - M2 - Voltage`, `SPEED Engine`, `Save Iso_Resist`, `Sevcon - CAN OK`, `Sevcon - Error mode`, `Sevcon - M3 - RUN`, `Sevcon - Ready`, `Sevcon - Voltage_3`, `Show Debug`, `Show P-1-2`, `Show_Elec`, `Show_Thermic`, `ShuntDown Action`, `ShuntDown Confirmed`, `ShuntDown Message`, `ShuntDown Turn Off`, `ShuntDown Wait`, `Speed`, `Speed Data`, `Speed Int`, `Speed Mode`, `Speed Pump`, `Speed State`, `Speed_RPM`, `Start 3 s`, `State`, `State All Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `State Up/Down`, `State Up/Down Raw`, `Stop Cruise`, `Stop To Move`, `Store TIMER UP/DOWN`, `Stuffing`, `Stuffing`, `Sunrise`, `Sunset`, `Switch Battery`, `System Shutdown`, `System Started`, `SÃ©curitÃ© hydraulique`, `TRACK DOWN`, `TRACK UP`, `Temperature od charger`, `Test Mode`, `Thermic Engine STATE`, `Time_Diff_MEM`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer Fan`, `Timer UP/DOWN`, `Timer charging`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Toggle Free`, `Track DOWN Delay`, `Track UP Delay`, `Trigger`, `Trigger HeartBeat`, `Trigger Speed`, `Trigger Timer`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `Unlock`, `VARIATOR ON`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR SUPER ON`, `VARIATOR Wait OFF`, `VIEW BAT Charging`, `VIEW BAT Ready`, `VIEW BAT Run`, `VIEW BUTTON States`, `VIEW ENGINE RUN PAGE`, `VIEW SOC`, `VIEW SPEED STATE`, `VIEW START PAGE`, `Var Power`, `Variator State`, `Variator hour`, `Voyant Pression Huile Moteur`, `Voyant TÂ° Eau Moteur Critical`, `Voyant TÂ° Eau Moteur Warning`, `Wait Bad Pressure`, `Wait Buz 2`, `Wait Hot Temperature`, `Wait after stating`, `Wait batt ON`, `Wait during start`, `Warning 1 - MEM`, `Warning 2 - MEM`, `WattAlps - Battery InstantVoltage`, `WattAlps - CAN OK`, `WattAlps - CURRENT`, `WattAlps - Cell_T_max_Master`, `WattAlps - DRIVE MODE`, `WattAlps - HighCellVoltage`, `WattAlps - Iso_Resist`, `WattAlps - LowCellVoltage`, `WattAlps - SOC`, `WattAlps- Max Current`, `WattAlps- U_Trac`, `WattApls- ERROR DIGIT`, `Works Latitude`, `Year since 2000`, `ZAPI_M1_Batterie Current`, `ZAPI_M1_Batterie Voltage`, `ZAPI_M1_CAN OK`, `ZAPI_M1_Error mode`, `ZAPI_M1_Heatsink`, `ZAPI_M1_Motor_Temp`, `ZAPI_M1_READY`, `ZAPI_M1_RUN`, `ZAPI_M1_Torque`, `ZAPI_M2_Batterie Current`, `ZAPI_M2_Batterie Voltage`, `ZAPI_M2_CAN OK`, `ZAPI_M2_Error mode`, `ZAPI_M2_Heatsink`, `ZAPI_M2_Motor_Temp`, `ZAPI_M2_READY`, `ZAPI_M2_RUN`, `ZAPI_M2_Torque`, `Event log: Battery Isolation`, `Event log: Check UP`, `Event log: Electronic Logs`, `Event log: Hydraulic Event`, `Event log: Thermic Events`, `Statistics log: Electric Stats`, `Statistics log: System Stats`, `Statistics log: Thermic Stats`
- Ligne export : 18174 · id 29979

#### Engine fluid level/pressure 1  `JFIN`
> EFL/P1
- Propriétés : Priority=6 · PGN=65263 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine oil pressure [kPa]; 25}} · Module=Inboard Engine (J1939[0]) · Module index=3
- Utilisé par : *(personne)*
- Ligne export : 18189 · id 29981

####   `JPIN`
- Propriétés : Name, English=Engine oil pressure · Unit=kPa · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=4 · Offset=0 · Error value=0
- Utilisé par : ``, `10 fail Starting`, `10 hours check-up`, `10 hours check-up`, `1552 - Hardware enable - IDC`, `1553 - Actual battery output voltage`, `1553 - Actual mains current`, `1553 - Actual mains voltage`, `1553 - output current to the battery`, `1555 - Power stage temperature - Byte`, `1560 - Desired Current`, `1560 - Desired Voltage`, `1560 - Max Current from 230 V`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Adress Loose`, `Adress_Search`, `Adresse_Mem`, `Allow Cruise`, `Allow Run Cruise`, `Auto Fast after Down`, `Auto Fast after Down Wait`, `Auto Off`, `Auto Off Bip`, `Auto Off Confirmed`, `Auto PAUSE/OFF`, `Auto Stop Timer`, `BATT - Reset`, `BMS_Iso_Resist`, `BMS_U_Trac`, `BMW - DRIVE MODE`, `BMW - ERROR DIGIT`, `BMW - Frequency`, `BMW - Iso_Resist`, `BMW - Main current`, `BMW - Output Voltage`, `BMW - Output current`, `BMW - SOC`, `BMW - Status`, `BMW CAN OK`, `BMW CAN OK`, `BMW Charging`, `BMW Connected`, `BMW Error`, `BMW Ready`, `Backlight Value`, `Backward Curent`, `Bad pressure`, `Balancing Counter`, `Balancing State`, `Bat - 100A-125A`, `Bat - 1A-25A`, `Bat - 25A-50A`, `Bat - 50A-75A`, `Bat - 75A-100A`, `Bat - up to 125A`, `Bat CMD`, `Bat Counter`, `BatNodeState`, `Batterie State`, `Battery CAN OK`, `Battery CHARGED`, `Battery CMD`, `Battery DRIVE MODE`, `Battery ERROR DIGIT`, `Battery Error Code`, `Battery Error Durring 5 s`, `Battery HIGHT TEMP`, `Battery InstantVoltage`, `Battery NEED TO CHARGE`, `Battery POWER`, `Battery Protection`, `Battery Protection`, `Battery SOC`, `Battery SOC Costumer`, `Battery STATE`, `Battery State MEM`, `Battery not need to charge`, `Battery start by charger`, `Bip`, `Bloc`, `Brake`, `Brake`, `Brake Activation`, `Brusa CAN OK`, `Brusa Charging`, `Brusa Connected`, `Brusa Error`, `Brusa ready`, `C`, `CMD`, `CMD`, `Calcul AccÃ©lÃ©ration`, `CanBus Error TB`, `CanOn Wait`, `Cell_T_max_Master`, `Charge`, `Charge Mode`, `Charge start state`, `Charger CAN BUS OK`, `Charger CHARGING`, `Charger CONNECT to 220V`, `Charger Connected`, `Charger DIGITAL CMD`, `Charger ERROR`, `Charger Output Current`, `Charger READY`, `Charger STATE`, `Charger State Finite`, `Charger end charge`, `Command State`, `Convert Left`, `Convert Right`, `CouchÃ© night`, `Counter`, `Couple Moteur`, `Couple Moteur`, `Current Bat`, `Current Date MEN`, `Cuurent Bat (ABS)`, `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `DOWN Counter`, `Days in current year`, `DcuNodeState`, `Dec`, `DiffCellVoltage`, `Don'push button`, `DurÃ©e`, `ECC1 Integrating`, `EMERG`, `EMERG`, `ENGINE RUN`, `ENGINE RUN`, `ET`, `ET h`, `Elcon - output Voltage`, `Elcon - output current`, `Elcon CAN OK`, `Elcon Charging`, `Elcon Connected`, `Elcon Error`, `Elcon Ready`, `Electric Engine STATE`, `Emmergency Stop Left`, `Emmergency Stop Right`, `Enable`, `Enable`, `Engine Stopped`, `Engine Temps`, `Engine hours`, `Engine hydro`, `Engine hydro Speed`, `Engine_Started`, `Engine_Stopped`, `Engines Not Ready`, `Error 1 - MEM`, `Error 1 - MEM`, `Error 2 - MEM`, `Error 2 - MEM`, `Error 3 - MEM`, `Error Iso_Resist`, `Error Wait`, `Error Wait`, `F4 Off`, `FAN OUT`, `FS1 Switch`, `FS1 Switch`, `Fail Start Counter`, `Fail Starting`, `Fordward Left`, `Fordward Right`, `Forward`, `Forward`, `Forward Curent`, `Func State`, `Func State`, `GPS Adresse Find`, `GPS_Adresse_Find_Int`, `Garmin - NMEA`, `Global Auto Off Timer`, `HIGH`, `HeartBeat`, `HeartBeat`, `Heatsink`, `HighCellVoltage`, `Ho`, `Ho_night`, `Hot Oil`, `Hot Water`, `Hour actual`, `Hydraulic pump statut`, `ID Fault`, `ID Prog`, `IDC Auto Sleep`, `IDC Batt Protection`, `IDC Free`, `IDC Speed Free`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `IDC Tension`, `If not start`, `Iguana PIN`, `Init Counter`, `Init Seq`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter EV By Pass`, `Inter EV DOWN`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP`, `Inter EV UP Delay`, `Inter EV Verin`, `Inter EV tendre Chenille`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Is_BMW`, `Is_Charger_BMW`, `Is_Charger_Brusa`, `Is_Charger_Elcon`, `Is_Electric`, `Is_Electric_MD3`, `Is_M3_Sevcon`, `Is_MT_Sevcon`, `Is_MT_Zapi`, `Is_Thermic`, `Is_Thermic_MD3`, `Is_WattAlps`, `IsoMonNodeState`, `Joystick Zero`, `Joystick Zero`, `Joystick not zero`, `Joystick to zero CMSG`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `K1 Fan Rear / Fan`, `K1 fuse is blown`, `K10`, `K10 fuse is blown`, `K11`, `K11 fuse is blown`, `K12`, `K12 fuse is blown`, `K13`, `K13 fuse is blown`, `K2 Fan Super / Pump`, `K2 fuse is blown`, `K3 Fan Exhaust / AutoOff`, `K3 fuse is blown`, `K4 Engine Power / Search Lights`, `K4 fuse is blown`, `K5 Engine Start`, `K5 fuse is blown`, `K6 Aux 1`, `K6 fuse is blown`, `K7 Aux 2`, `K7 fuse is blown`, `K8`, `K8 fuse is blown`, `K9`, `K9 fuse is blown`, `Keep ON`, `KeyBox Can Ok`, `Ko to move`, `L`, `LOW`, `Latence Math`, `LatenceTimer`, `Latitude Compute`, `Latitude Compute MEN`, `Led Temp Water`, `Left Error`, `Left Warning`, `LevÃ© night`, `Libre`, `Lock`, `Locking Phase Duration`, `Lon`, `Longitude Compute`, `Longitude Compute MEN`, `LowCellVoltage`, `M`, `M1 - 100A-125A`, `M1 - 25A-50A`, `M1 - 50A-75A`, `M1 - 75A-100A`, `M1 - CAN OK`, `M1 - CURRENT`, `M1 - Charge`, `M1 - ENGINE HOT`, `M1 - Error mode`, `M1 - Heatsink`, `M1 - KTY`, `M1 - Mechanical power`, `M1 - NEED TO FAN`, `M1 - NEED TO PUMP`, `M1 - New Error Code`, `M1 - Normal Mode`, `M1 - RUN`, `M1 - Ready`, `M1 - Right Engine CMSG`, `M1 - Speed`, `M1 - Torque`, `M1 - Torque Tracks`, `M1 - Voltage`, `M1 - Zapi New Error Code`, `M1 - Zapi New Warning Code`, `M1 - up to 125A`, `M2 - 100A-125A`, `M2 - 25A-50A`, `M2 - 50A-75A`, `M2 - 75A-100A`, `M2 - CAN OK`, `M2 - CURRENT`, `M2 - Charge`, `M2 - ENGINE HOT`, `M2 - Error mode`, `M2 - Heatsink`, `M2 - KTY`, `M2 - Left Engine CMSG`, `M2 - Mechanical power`, `M2 - NEED TO FAN`, `M2 - NEED TO PUMP`, `M2 - New Error Code`, `M2 - Normal mode`, `M2 - RUN`, `M2 - Ready`, `M2 - Speed`, `M2 - Torque`, `M2 - Torque tracks`, `M2 - Voltage`, `M2 - ZAPI - New Warning Code`, `M2 - Zapi - New Error Code`, `M2 - up to 125A`, `M3  (Pump) - Filter`, `M3 - CAN OK`, `M3 - Charge`, `M3 - ENGINE HOT`, `M3 - Error mode`, `M3 - NEED TO FAN`, `M3 - NEED TO PUMP`, `M3 - New Error Code`, `M3 - Pump Engine CMSG`, `M3 - Ready`, `M3 - Run`, `M3 - Voltage`, `M3_Speed`, `MD3 - DOWN`, `MD3 - UP`, `MD4 - Start Button Blocking Neutral`, `MDGN-+BAT:MC2[1]`, `Main Switch Battery`, `Math Current`, `Math Current`, `Math Droit`, `Math Gauche`, `Math Left`, `Math Right`, `Math Voltage`, `Math Voltage`, `Max Discharge`, `Max Manip`, `Min Speed`, `Mini Wait`, `MÃ©ridian`, `NEED FAN`, `NEED MORE SPEED`, `NEED PUMP`, `Need to Charge IDC - Public`, `Need to Charge Voltage`, `Need to Charge Voltage Wait`, `Need to charge`, `New Battery State`, `New Error Code`, `New Timer`, `OK BLOC`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `OK UP/DOWN`, `ON/OFF Var`, `Oil Not Good`, `Oil pressure`, `Ok to move`, `PARKER OK`, `PDO1_RX`, `PDO1_RX`, `PDO1_TX`, `PDO1_TX`, `PDO2_TX`, `PDO2_TX`, `PIN 44`, `PIn State`, `PUMP VAR`, `Power`, `Power`, `Power`, `Power Down`, `Power Down Wait`, `Power State Int`, `Process Down Engine`, `Pump 1 Right`, `Pump 1 Right Filter ECC1`, `Pump 2 Left`, `Pump 2 Left Filter ECC1`, `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Request Parameter State`, `Reset`, `Reset`, `Reset`, `Reset Speed`, `Reset Startup`, `Reset State`, `Reset on startup`, `Reverse`, `Reverse`, `Reverse Left`, `Reverse Right`, `Right Error`, `Right Warning`, `SARTING`, `SEV - M1 - CAN OK`, `SEV - M1 - CURRENT`, `SEV - M1 - Error mode`, `SEV - M1 - RUN`, `SEV - M1 - Ready`, `SEV - M1 - Speed`, `SEV - M1 - Torque actual`, `SEV - M1 - Voltage`, `SEV - M2 - CAN OK`, `SEV - M2 - CURRENT`, `SEV - M2 - Error mode`, `SEV - M2 - RUN`, `SEV - M2 - Ready`, `SEV - M2 - Speed`, `SEV - M2 - Torque actual`, `SEV - M2 - Voltage`, `SPEED Engine`, `Save Iso_Resist`, `Sevcon - CAN OK`, `Sevcon - Error mode`, `Sevcon - M3 - RUN`, `Sevcon - Ready`, `Sevcon - Voltage_3`, `Show Debug`, `Show P-1-2`, `Show_Elec`, `Show_Thermic`, `ShuntDown Action`, `ShuntDown Confirmed`, `ShuntDown Message`, `ShuntDown Turn Off`, `ShuntDown Wait`, `Speed`, `Speed Data`, `Speed Int`, `Speed Mode`, `Speed Pump`, `Speed State`, `Speed_RPM`, `Start 3 s`, `State`, `State All Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `State Up/Down`, `State Up/Down Raw`, `Stop Cruise`, `Stop To Move`, `Store TIMER UP/DOWN`, `Stuffing`, `Stuffing`, `Sunrise`, `Sunset`, `Switch Battery`, `System Shutdown`, `System Started`, `SÃ©curitÃ© hydraulique`, `TRACK DOWN`, `TRACK UP`, `Temperature od charger`, `Test Mode`, `Thermic Engine STATE`, `Time_Diff_MEM`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer Fan`, `Timer UP/DOWN`, `Timer charging`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Toggle Free`, `Track DOWN Delay`, `Track UP Delay`, `Trigger`, `Trigger HeartBeat`, `Trigger Speed`, `Trigger Timer`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `Unlock`, `VARIATOR ON`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR SUPER ON`, `VARIATOR Wait OFF`, `VIEW BAT Charging`, `VIEW BAT Ready`, `VIEW BAT Run`, `VIEW BUTTON States`, `VIEW ENGINE RUN PAGE`, `VIEW SOC`, `VIEW SPEED STATE`, `VIEW START PAGE`, `Var Power`, `Variator State`, `Variator hour`, `Voyant Pression Huile Moteur`, `Voyant TÂ° Eau Moteur Critical`, `Voyant TÂ° Eau Moteur Warning`, `Wait Bad Pressure`, `Wait Buz 2`, `Wait Hot Temperature`, `Wait after stating`, `Wait batt ON`, `Wait during start`, `Warning 1 - MEM`, `Warning 2 - MEM`, `WattAlps - Battery InstantVoltage`, `WattAlps - CAN OK`, `WattAlps - CURRENT`, `WattAlps - Cell_T_max_Master`, `WattAlps - DRIVE MODE`, `WattAlps - HighCellVoltage`, `WattAlps - Iso_Resist`, `WattAlps - LowCellVoltage`, `WattAlps - SOC`, `WattAlps- Max Current`, `WattAlps- U_Trac`, `WattApls- ERROR DIGIT`, `Works Latitude`, `Year since 2000`, `ZAPI_M1_Batterie Current`, `ZAPI_M1_Batterie Voltage`, `ZAPI_M1_CAN OK`, `ZAPI_M1_Error mode`, `ZAPI_M1_Heatsink`, `ZAPI_M1_Motor_Temp`, `ZAPI_M1_READY`, `ZAPI_M1_RUN`, `ZAPI_M1_Torque`, `ZAPI_M2_Batterie Current`, `ZAPI_M2_Batterie Voltage`, `ZAPI_M2_CAN OK`, `ZAPI_M2_Error mode`, `ZAPI_M2_Heatsink`, `ZAPI_M2_Motor_Temp`, `ZAPI_M2_READY`, `ZAPI_M2_RUN`, `ZAPI_M2_Torque`, `Event log: Battery Isolation`, `Event log: Check UP`, `Event log: Electronic Logs`, `Event log: Hydraulic Event`, `Event log: Thermic Events`, `Statistics log: Electric Stats`, `Statistics log: System Stats`, `Statistics log: Thermic Stats`
- Ligne export : 18210 · id 29982

#### EEC1  `JFIN`
> Electronic Engine Controller 1
- Propriétés : Priority=3 · PGN=61444 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Driver's demand, engine % [%]; 9}; {Actual engine, % torque [%]; 17}; {Engine speed [rpm]; 25}} · Module=Inboard Engine (J1939[0]) · Module index=0
- Lit : `Actual engine, % torque`, `Driver's demand, engine %`, `Engine speed`
- Utilisé par : *(personne)*
- Ligne export : 18225 · id 29983

#### Driver's demand, engine %  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `EEC1`
- Ligne export : 18252 · id 29984

#### Actual engine, % torque  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `ECC1_Power`, `EEC1`, `Measure group: Engine Thermic`, `Measure group: Engine and Translation`
- Ligne export : 18266 · id 29985

#### Engine speed  `JPIN`
- Propriétés : Unit=rpm · Length=2 Bytes (= 16 bits) · J1939 Error check=Yes · Resolution=0,125 · Offset=0 · Error value=0
- Utilisé par : `EEC1`, `Engine_Started`, `NEED MORE SPEED`, `Speed`, `Measure group: Engine Thermic`, `Measure group: Engine and Translation`
- Ligne export : 18280 · id 29986

#### EEC2  `JFIN`
> Electronic Engine Controller 2
- Propriétés : Priority=3 · PGN=61443 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Accelerator pedal position [%]; 9}; {% load at current speed [%]; 17}} · Module=Inboard Engine (J1939[0]) · Module index=4
- Lit : `% load at current speed`, `Accelerator pedal position`
- Utilisé par : *(personne)*
- Ligne export : 18294 · id 29987

#### Accelerator pedal position  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=0,4 · Offset=0 · Error value=0
- Utilisé par : `EEC2`
- Ligne export : 18318 · id 29988

#### % load at current speed  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `EEC2`, `Measure group: Engine Thermic`
- Ligne export : 18332 · id 29989

#### Para enclench voyant TÂ° moteur warning  `FP`
- Propriétés : Unit=Â°C · Default mode={95}
- Utilisé par : `Voyant TÂ° Eau Moteur Warning`
- Ligne export : 18346 · id 29991

#### Engine_Started  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine speed [rpm] > 700`
- Lit : ``, `Engine speed`
- Utilisé par : ``, `AutoStopafter 5 secondes`, `ECC1_Engine_Temp`, `ECC1_Oil_Temp`, `ECC1_Power`, `ECC1_Speed`, `Engine_Stopped`, `Fuel line ignition IDC`, `Pre Fuel line ignition IDC`, `System Started`, `Voyant Pression Huile Moteur`, `Voyant TÂ° Eau Moteur Critical`, `Voyant TÂ° Eau Moteur Warning`, `Wait Bad Pressure`, `Wait Hot Temperature`, `Event log: Thermic Events`, `Statistics log: Thermic Stats`
- Ligne export : 18358 · id 32282

#### Voyant TÂ° Eau Moteur Warning  `IDC`
- Propriétés : Toggle=No · Delay on=100000 · Delay off=0
- Logique :
  - **Activating** = `(Engine coolant temperature [Â°C] > Para enclench voyant TÂ° moteur warning [Â°C]) AND Engine_Started`
- Lit : ``, `C`, `Engine_Started`, `Para enclench voyant TÂ° moteur warning`
- Utilisé par : `Led Temp Water`, `Event log: Thermic Events`
- Ligne export : 18403 · id 29992

#### Para enclench voyant TÂ° moteur critical  `FP`
- Propriétés : Unit=Â°C · Default mode={100}
- Utilisé par : `Voyant TÂ° Eau Moteur Critical`
- Ligne export : 18455 · id 30001

#### Voyant TÂ° Eau Moteur Critical  `IDC`
- Propriétés : Toggle=No · Delay on=100000 · Delay off=0
- Logique :
  - **Activating** = `(Engine coolant temperature [Â°C] > Para enclench voyant TÂ° moteur critical [Â°C]) AND Engine_Started`
- Lit : ``, `C`, `Engine_Started`, `Para enclench voyant TÂ° moteur critical`
- Utilisé par : `Hot Water`, `Led Temp Water`
- Ligne export : 18467 · id 30002

#### Hot Water  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=Engine over heating · Text, English=Stop Engine Immediately, let cool down. Check fan and coolant level. And contact your service center. · Channel=Engine coolant temperature [Â°C]
- Logique :
  - **Showing** = `Voyant TÂ° Eau Moteur Critical`
  - **Hiding** = `not(Voyant TÂ° Eau Moteur Critical)`
- Lit : ``, `C`, `Voyant TÂ° Eau Moteur Critical`
- Utilisé par : *(personne)*
- Ligne export : 18519 · id 30011

#### Para enclench voyant pression huile  `FP`
- Propriétés : Unit=kPa · Default mode={300}
- Utilisé par : `Voyant Pression Huile Moteur`
- Ligne export : 18575 · id 30019

#### Voyant Pression Huile Moteur  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `(Engine oil pressure [kPa] < Para enclench voyant pression huile [kPa]) AND Engine_Started`
- Lit : ``, `Engine_Started`, `Para enclench voyant pression huile`
- Utilisé par : `Oil pressure`, `Event log: Thermic Events`, `MD3 page: Thermic`
- Ligne export : 18587 · id 30020

#### FP - Start rÃ©duction  `FP`
- Propriétés : Unit=% · Default mode={85}
- Utilisé par : `ECC1_Power`, `Adjust group: Master Thermic`, `Single adjust item: FP - Start rÃ©duction`
- Ligne export : 18639 · id 30029

#### FP - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={20}
- Utilisé par : `ECC1_Power`, `Adjust group: Master Thermic`, `Single adjust item: FP - Incres Speed`
- Ligne export : 18651 · id 30030

#### FP - Max Error  `FP`
- Propriétés : Unit=% · Default mode={10}
- Utilisé par : `ECC1_Power`, `Adjust group: Master Thermic`, `Single adjust item: FP - Max Error`
- Ligne export : 18663 · id 30031

#### FP - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={80}
- Utilisé par : `ECC1_Power`, `Adjust group: Master Thermic`, `Single adjust item: FP - Decres Speed`
- Ligne export : 18675 · id 30032

#### ECC1_Power  `ILC`
- Propriétés : Output=Normal · Enable=Engine_Started · Input channel=Actual engine, % torque [%] · Start reduction at=FP - Start rÃ©duction [%] · Max error=FP - Max Error [%] · Max increase speed=FP - Incres Speed [%/s] · Max decrease speed=FP - Decres Speed [%/s]
- Lit : `Actual engine, % torque`, `Engine_Started`, `FP - Decres Speed`, `FP - Incres Speed`, `FP - Max Error`, `FP - Start rÃ©duction`
- Utilisé par : `ECC1 Integrating`, `Measure group: Engine and Translation`
- Ligne export : 18687 · id 30033

#### FT - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={50}
- Utilisé par : `ECC1_Engine_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FT - Incres Speed`
- Ligne export : 18702 · id 30034

#### FT - Max Error  `FP`
- Propriétés : Unit=Â°C · Default mode={5}
- Utilisé par : `ECC1_Engine_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FT - Max Error`
- Ligne export : 18714 · id 30035

#### FT - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={0,6}
- Utilisé par : `ECC1_Engine_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FT - Decres Speed`
- Ligne export : 18726 · id 30036

#### FT - Start rÃ©duction  `FP`
- Propriétés : Unit=Â°C · Default mode={97}
- Utilisé par : `ECC1_Engine_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FT - Start rÃ©duction`
- Ligne export : 18738 · id 30037

#### ECC1_Engine_Temp  `ILC`
- Propriétés : Output=Normal · Enable=Engine_Started · Input channel=Engine coolant temperature [Â°C] · Start reduction at=FT - Start rÃ©duction [Â°C] · Max error=FT - Max Error [Â°C] · Max increase speed=FT - Incres Speed [%/s] · Max decrease speed=FT - Decres Speed [%/s]
- Lit : `C`, `Engine_Started`, `FT - Decres Speed`, `FT - Incres Speed`, `FT - Max Error`, `FT - Start rÃ©duction`
- Utilisé par : `ECC1 Integrating`, `Measure group: Engine and Translation`
- Ligne export : 18750 · id 30038

#### FO - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={50}
- Utilisé par : `ECC1_Oil_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FO - Incres Speed`
- Ligne export : 18765 · id 35797

#### FO - Max Error  `FP`
- Propriétés : Unit=Â°C · Default mode={10}
- Utilisé par : `ECC1_Oil_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FO - Max Error`
- Ligne export : 18777 · id 35798

#### FO - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={1}
- Utilisé par : `ECC1_Oil_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FO - Decres Speed`
- Ligne export : 18789 · id 35799

#### FO - Start rÃ©duction  `FP`
- Propriétés : Unit=Â°C · Default mode={90}
- Utilisé par : `ECC1_Oil_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FO - Start rÃ©duction`
- Ligne export : 18801 · id 35800

#### ECC1_Oil_Temp  `ILC`
- Propriétés : Output=Normal · Enable=Engine_Started · Input channel=Oil Temps [Â°C] · Start reduction at=FO - Start rÃ©duction [Â°C] · Max error=FO - Max Error [Â°C] · Max increase speed=FO - Incres Speed [%/s] · Max decrease speed=FO - Decres Speed [%/s]
- Lit : `Engine_Started`, `FO - Decres Speed`, `FO - Incres Speed`, `FO - Max Error`, `FO - Start rÃ©duction`, `Oil Temps`
- Utilisé par : `ECC1 Integrating`, `Measure group: Engine and Translation`
- Ligne export : 18813 · id 35801

#### Speed  `MAC`
- Propriétés : Unit=%
- Logique :
  ```qcode
  if Speed_RPM  >  0 then
  Speed := 100 - (Engine speed / Speed_RPM) * 100
  else
  Speed := 0
  endif
  
  if Speed >= 100 then
  Speed := 100
  endif
  if Speed <= 0 then
  Speed := 0
  endif
  Result := Speed
  ```
- Lit : `Engine speed`, `Speed`, `Speed_RPM`
- Utilisé par : `ECC1_Speed`, `TSC1-A:J1939-0`, `Adjust group: `
- Ligne export : 18828 · id 35843

#### FS - Start rÃ©duction  `FP`
- Propriétés : Unit=% · Default mode={30}
- Utilisé par : `ECC1_Speed`, `Adjust group: Master Thermic`, `Single adjust item: FS - Start rÃ©duction`
- Ligne export : 18858 · id 35838

#### FS - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={20}
- Utilisé par : `ECC1_Speed`, `Adjust group: Master Thermic`, `Single adjust item: FS - Incres Speed`
- Ligne export : 18870 · id 35839

#### FS - Max Error  `FP`
- Propriétés : Unit=% · Default mode={10}
- Utilisé par : `ECC1_Speed`, `Adjust group: Master Thermic`, `Single adjust item: FS - Max Error`
- Ligne export : 18882 · id 35840

#### FS - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={80}
- Utilisé par : `ECC1_Speed`, `Adjust group: Master Thermic`, `Single adjust item: FS - Decres Speed`
- Ligne export : 18894 · id 35841

#### ECC1_Speed  `ILC`
- Propriétés : Output=Normal · Enable=Engine_Started · Input channel=Speed [%] · Start reduction at=FS - Start rÃ©duction [%] · Max error=FS - Max Error [%] · Max increase speed=FS - Incres Speed [%/s] · Max decrease speed=FS - Decres Speed [%/s]
- Lit : `Engine_Started`, `FS - Decres Speed`, `FS - Incres Speed`, `FS - Max Error`, `FS - Start rÃ©duction`, `Speed`
- Utilisé par : `ECC1 Integrating`, `Measure group: Engine and Translation`
- Ligne export : 18906 · id 35842

#### ECC1 Integrating  `MAC`
- Logique :
  ```qcode
  Result := (ECC1_Engine_Temp/100) * (ECC1_Power/100) * (ECC1_Oil_Temp/100) * (ECC1_Speed/100)
  ```
- Lit : `ECC1_Engine_Temp`, `ECC1_Oil_Temp`, `ECC1_Power`, `ECC1_Speed`
- Utilisé par : `ECC1 Integrating`, `Pump 1 Right Filter ECC1`, `Pump 2 Left Filter ECC1`
- Ligne export : 18921 · id 30039

#### Led Temp Water  `SMC`
- Propriétés : Default state name=Normal
- Fonction *Warning* :
  - **Activating** = `Voyant TÂ° Eau Moteur Warning`
  - **Blocking** = `Voyant TÂ° Eau Moteur Critical`
- Fonction *Critical* :
  - **Activating** = `Voyant TÂ° Eau Moteur Critical`
- Lit : ``, `Voyant TÂ° Eau Moteur Critical`, `Voyant TÂ° Eau Moteur Warning`
- Utilisé par : `MD3 page: Thermic`
- Ligne export : 18939 · id 30049

#### Oil pressure  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=Inboard engine low oil · Text, English=Stop Engine Immediately, let cool down. Check engine oil level. And contact your service center. Oil type : 10W40.
- Logique :
  - **Showing** = `Voyant Pression Huile Moteur`
  - **Hiding** = `not(Voyant Pression Huile Moteur)`
- Lit : ``, `Voyant Pression Huile Moteur`
- Utilisé par : *(personne)*
- Ligne export : 19017 · id 30062

#### Engine_Stopped  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Engine_Started)`
- Lit : ``, `Engine_Started`
- Utilisé par : `Bloc`, `Engine Stopped`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP Delay`, `Inter EV tendre Chenille`, `Inter Full Fan`, `Libre`
- Ligne export : 19073 · id 32333

#### ECC1 Integrating  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `ECC1 Integrating * 100`
- Lit : ``, `ECC1 Integrating`
- Utilisé par : `Pump 1 Right Filter ECC1`, `Pump 2 Left Filter ECC1`
- Ligne export : 19117 · id 35976

## Thermic / SEJ ECM

#### DM1  `DM1IN`
> Diagnostic Message 1
- Propriétés : SPN conversion method=4 · FMI texts={OK; Above normal, most severe; Below normal, most severe; Erratic or intermittent; Voltage above normal; Voltage below normal; Current below normal; Current above normal; Out of adjustment; Abnormal frequency; Abnormal update rate; Abnormal rate of change; Root cause not known; Bad component; Out of calibration; Special instructions; Above normal; Above normal, severe; Below normal; Below normal, severe; Received data in error; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Not available} · Show message=All · Dialog for undefined SPNs=Yes · Enable DM2 support=False · Enable lamp flash=No · Parameters={SPN 98; SPN 100; SPN 102; SPN 105; SPN 106; SPN 110; SPN 175; SPN 626; SPN 629; SPN 636; SPN 637; SPN 639; SPN 651; SPN 652; SPN 653; SPN 654; SPN 655; SPN 656; SPN 677; SPN 1485} · Module=Inboard Engine (J1939[0]) · Module index=0
- Lit : `SPN 100`, `SPN 102`, `SPN 105`, `SPN 106`, `SPN 110`, `SPN 1485`, `SPN 175`, `SPN 626`, `SPN 629`, `SPN 636`, `SPN 637`, `SPN 639`, `SPN 651`, `SPN 652`, `SPN 653`, `SPN 654`, `SPN 655`, `SPN 656`, `SPN 677`, `SPN 98`
- Utilisé par : *(personne)*
- Ligne export : 17572 · id 29039

#### SPN 629  `SPN`
> Controller #1
- Propriétés : SPN=629 · Dialog priority=Critical · Failures={{8; ErrNo 186 DTC 9.9: CPU Watchdog reset test failure.}; {13; ErrNo 186 DTC 9.9: Watchdog trip failure.}; {2; ErrNo 187 DTC 9.9: RAM cell test failure.}; {12; ErrNo 187 DTC 9.9: RAM address test failure.}; {11; ErrNo 186 DTC 9.9: Main and Fueling ASIC test fail.}}
- Utilisé par : `DM1`
- Ligne export : 17642 · id 29040

#### SPN 100  `SPN`
> Engine Oil Pressure
- Propriétés : SPN=100 · Dialog priority=Warning · Failures={{3; ErrNo 181 DTC 3.1: Voltage above normal.}; {4; ErrNo 182 DTC 3.1: Voltage below normal.}; {1; ErrNo 180 DTC 6.6: Data valid but below normal.}}
- Utilisé par : `DM1`
- Ligne export : 17668 · id 29041

#### SPN 110  `SPN`
> Engine Coolant Temperature
- Propriétés : SPN=110 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 17688 · id 29042

#### SPN 105  `SPN`
> Air Intake Manifold 1 Temperature
- Propriétés : SPN=105 · Dialog priority=Warning · Failures={{3; ErrNo 25 DTC 3.2: Voltage above normal.}; {4; ErrNo 26 DTC 3.2: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 17708 · id 29043

#### SPN 175  `SPN`
> Engine Oil Temperature 1
- Propriétés : SPN=175 · Dialog priority=Critical · Failures={{3; ErrNo 184 DTC 3.7: Voltage above normal.}; {4; ErrNo 185 DTC 3.7: Voltage below normal.}; {0; ErrNo 183 DTC 5.8: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 17728 · id 29044

#### SPN 102  `SPN`
> Boost Pressure
- Propriétés : SPN=102 · Dialog priority=Warning · Failures={{3; ErrNo 67 DTC 3.4: Voltage above normal.}; {4; ErrNo 68 DTC 3.4: Voltage below normal.}; {0; ErrNo 57 DTC -.-: Data valid but above normal.}; {1; ErrNo 58 DTC -.-: Data valid but below normal.}}
- Utilisé par : `DM1`
- Ligne export : 17748 · id 29045

#### SPN 1485  `SPN`
> ECU Main relay
- Propriétés : SPN=1485 · Dialog priority=Warning · Failures={{3; ErrNo 43 DTC 5.1: Short circuit high.}}
- Utilisé par : `DM1`
- Ligne export : 17771 · id 29046

#### SPN 637  `SPN`
> Timing sensor
- Propriétés : SPN=637 · Dialog priority=Warning · Failures={{8; ErrNo 18 DTC 2.4: Extra pulses.}; {2; ErrNo 101 DTC 2.4: Intermittent loss of signal.}; {3; ErrNo 18 DTC 2.4: Permanent loss of signal.}}
- Utilisé par : `DM1`
- Ligne export : 17785 · id 29047

#### SPN 656  `SPN`
> Injector Cylinder #06
- Propriétés : SPN=656 · Dialog priority=Warning · Failures={{2; ErrNo 160 DTC 7.6: Short circuit High Side to Vbatt.}; {4; ErrNo 161 DTC 7.6: Short circuit High or Low Side to ground.}; {3; ErrNo 162 DTC 7.6: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 165 DTC 7.6: Open circuit.}; {11; ErrNo 163 DTC 7.6: Unknown Error.}; {7; ErrNo 164 DTC 7.6: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 17805 · id 29048

#### SPN 636  `SPN`
> Engine position sensor
- Propriétés : SPN=636 · Dialog priority=Critical · Failures={{8; ErrNo 103 DTC 2.5: Extra pulses or high frequency signal.}; {3; ErrNo 102 DTC 2.5: Permanent loss of signal.}}
- Utilisé par : `DM1`
- Ligne export : 17834 · id 29049

#### SPN 626  `SPN`
> Start enable device - Devices that assist an engine in starting - e.g. intake heaters and ether
- Propriétés : SPN=626 · Dialog priority=Warning · Failures={{3; ErrNo 76 DTC 5.4: Voltage above normal.}; {4; ErrNo 75 DTC 5.4: Voltage below normal.}; {5; ErrNo 74 DTC 5.4: Current below normal.}}
- Utilisé par : `DM1`
- Ligne export : 17851 · id 29050

#### SPN 677  `SPN`
> Engine Starter Motor Relay
- Propriétés : SPN=677 · Dialog priority=Warning · Failures={{3; ErrNo 41 DTC 4.6: Short circuit high.}; {4; ErrNo 42 DTC 4.6: Short circuit low.}; {5; ErrNo 107 DTC 4.6: Open circuit.}}
- Utilisé par : `DM1`
- Ligne export : 17871 · id 29051

#### SPN 655  `SPN`
> Injector Cylinder #05
- Propriétés : SPN=655 · Dialog priority=Warning · Failures={{2; ErrNo 150 DTC 7.5: Short circuit High Side to Vbatt.}; {4; ErrNo 151 DTC 7.5: Short circuit High or Low Side to ground.}; {3; ErrNo 152 DTC 7.5: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 155 DTC 7.5: Open circuit.}; {11; ErrNo 153 DTC 7.5: Unknown Error.}; {7; ErrNo 154 DTC 7.5: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 17891 · id 29052

#### SPN 654  `SPN`
> Injector Cylinder #04
- Propriétés : SPN=654 · Dialog priority=Warning · Failures={{2; ErrNo 140 DTC 7.4: Short circuit High Side to Vbatt.}; {4; ErrNo 141 DTC 7.4: Short circuit High or Low Side to ground.}; {3; ErrNo 142 DTC 7.4: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 145 DTC 7.4: Open circuit.}; {11; ErrNo 143 DTC 7.4: Unknown Error.}; {7; ErrNo 144 DTC 7.4: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 17920 · id 29053

#### SPN 653  `SPN`
> Injector Cylinder #03
- Propriétés : SPN=653 · Dialog priority=Warning · Failures={{2; ErrNo 130 DTC 7.3: Short circuit High Side to Vbatt.}; {4; ErrNo 131 DTC 7.3: Short circuit High or Low Side to ground.}; {3; ErrNo 132 DTC 7.3: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 135 DTC 7.3: Open circuit.}; {11; ErrNo 133 DTC 7.3: Unknown Error.}; {7; ErrNo 134 DTC 7.3: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 17949 · id 29054

#### SPN 652  `SPN`
> Injector Cylinder #02
- Propriétés : SPN=652 · Dialog priority=Warning · Failures={{2; ErrNo 120 DTC 7.2: Short circuit High Side to Vbatt.}; {4; ErrNo 121 DTC 7.2: Short circuit High or Low Side to ground.}; {3; ErrNo 122 DTC 7.2: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 125 DTC 7.2: Open circuit.}; {11; ErrNo 123 DTC 7.2: Unknown Error.}; {7; ErrNo 124 DTC 7.2: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 17978 · id 29055

#### SPN 651  `SPN`
> Injector Cylinder #01
- Propriétés : SPN=651 · Dialog priority=Warning · Failures={{2; ErrNo 110 DTC 7.1: Short circuit High Side to Vbatt.}; {4; ErrNo 111 DTC 7.1: Short circuit High or Low Side to ground.}; {3; ErrNo 112 DTC 7.1: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 115 DTC 7.1: Open circuit.}; {11; ErrNo 113 DTC 7.1: Unknown Error.}; {7; ErrNo 114 DTC 7.1: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 18007 · id 29056

#### SPN 639  `SPN`
> J1939 Network #1, Primary Vehicle Network
- Propriétés : SPN=639 · Dialog priority=Warning · Failures={{2; ErrNo 106 DTC 6.5: Bus Off error.}; {9; ErrNo 106 DTC 6.5: Passive bus error.}; {12; ErrNo 38 DTC 6.5: Loss of message error.}; {11; ErrNo 38 DTC 6.5: Data registers read back failure.}}
- Utilisé par : `DM1`
- Ligne export : 18036 · id 29057

#### Malfunction lamp  `MDGN`
- Propriétés : Value=Malfunction · Module=Inboard Engine (J1939[0]) · Module index=1
- Utilisé par : `Measure group: Engine Thermic`
- Ligne export : 18059 · id 29058

#### Red stop lamp  `MDGN`
- Propriétés : Value=Red stop · Module=Inboard Engine (J1939[0]) · Module index=2
- Utilisé par : `Measure group: Engine Thermic`
- Ligne export : 18070 · id 29059

#### Amber warning lamp  `MDGN`
- Propriétés : Value=Amber warning · Module=Inboard Engine (J1939[0]) · Module index=3
- Utilisé par : `Measure group: Engine Thermic`
- Ligne export : 18081 · id 29060

#### Protect lamp  `MDGN`
- Propriétés : Value=Protect · Module=Inboard Engine (J1939[0]) · Module index=4
- Utilisé par : `Measure group: Engine Thermic`
- Ligne export : 18092 · id 29061

#### SPN 98  `SPN`
> Engine oil level
- Propriétés : SPN=98 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 18103 · id 29062

#### SPN 106  `SPN`
- Propriétés : SPN=106 · Dialog priority=DonÂt show · Failures={{4; MAP Voltage Low}}
- Utilisé par : `DM1`
- Ligne export : 18123 · id 29063
