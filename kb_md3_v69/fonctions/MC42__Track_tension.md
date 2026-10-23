# MC42 — Track tension

31 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Track tension

#### Track pressure  `VIN`
- Propriétés : Unit=bar · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-SP500 · Calibration={500; 4500; 0; 500} · Alarms={No; 0; No; 100} · Module=MC42 (MC42[1]) · Module index=2
- Utilisé par : `Pression filtered`, `Track Tension Error`, `Adjust group: Master Tracks`, `Measure group: Hydraulic`
- Ligne export : 13425 · id 32718

#### Tracks pressure Mode  `SP`
> This channel is used to give unit and names to the MEM
- Propriétés : Input channel=None · Default state name=AUTO · States={UNTIGHTEN}
- Utilisé par : `IDC Free`, `ON/OFF/Untighed`, `Tension State`, `Tracks pressure Mode`, `Untighten`, `Adjust group: Maintenance`, `Single adjust item: Tracks pressure Mode`
- Ligne export : 13449 · id 32719

#### Reset Startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset Startup`
- Lit : ``, `Reset Startup`
- Utilisé par : ``, `Reset Startup`, `Tracks pressure Mode`
- Ligne export : 13461 · id 32721

#### Tracks pressure Mode  `MEM`
- Propriétés : Input channel=Tracks pressure Mode · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : ``, `Reset Startup`, `Tracks pressure Mode`
- Utilisé par : `IDC Free`, `ON/OFF/Untighed`, `Tension State`, `Untighten`, `Adjust group: Maintenance`, `Single adjust item: Tracks pressure Mode`
- Ligne export : 13511 · id 32730

#### Wait engine start  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `System Started DELAYS`
- Lit : ``, `System Started DELAYS`
- Utilisé par : `ON/OFF/Untighed`, `Ok tension`, `Tension State`, `Wait engine Stop`
- Ligne export : 13554 · id 32738

#### ON/OFF/Untighed  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ON* :
  - **Activating** = `Wait engine start`
  - **Blocking** = `Tracks pressure Mode`
- Fonction *UNTIGHTED* :
  - **Activating** = `Tracks pressure Mode`
- Lit : ``, `Tracks pressure Mode`, `Wait engine start`
- Utilisé par : `Super Ok tension`
- Ligne export : 13597 · id 32746

#### Pression filtered  `SFC`
- Propriétés : Input channel=Track pressure [bar] · Enable=Yes · Type=Slopes · Slopes={{50; 50}; {1; 1}}
- Lit : `Track pressure`
- Utilisé par : `Need Pressure`, `MD3 page: BASE`, `Measure group: Thermic vs Hydraulic`
- Ligne export : 13675 · id 32759

#### Time to tension  `IP`
- Propriétés : Unit=ms · Default mode={150}
- Utilisé par : `Super Ok tension`, `Adjust group: Master Tracks`, `Single adjust item: Time to tension`
- Ligne export : 13693 · id 32760

#### Untighten  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Tracks pressure Mode`
- Lit : ``, `Tracks pressure Mode`
- Utilisé par : `Inter EV By Pass`, `Inter Tension`, `OK UP/DOWN`, `Ok tension`
- Ligne export : 13705 · id 33241

#### Ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `PositiveFlank(Wait engine start)`
  - **Blocking** = `Untighten`
- Lit : ``, `Untighten`, `Wait engine start`
- Utilisé par : `Super Ok tension`
- Ligne export : 13748 · id 32761

#### 10 minutes auto tender  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=10
- Logique :
  - **Decreasing** = `System Started DELAYS`
  - **Resetting** = `10 minutes auto tender [min] <= 0`
- Lit : ``, `System Started DELAYS`
- Utilisé par : `Super Ok tension`
- Ligne export : 13799 · id 32769

#### Tension Pressure  `IP`
- Propriétés : Unit=bar · Default mode={160}
- Utilisé par : `Need Pressure`, `Adjust group: Master Tracks`, `Single adjust item: Tension Pressure`
- Ligne export : 13860 · id 32780

#### Need Pressure Tempo  `IP`
- Propriétés : Unit=ms · Default mode={5000}
- Utilisé par : `Need Pressure`, `Adjust group: Master Thermic`, `Single adjust item: Need Pressure Tempo`
- Ligne export : 13872 · id 63236

#### Need Pressure  `IDC`
- Propriétés : Toggle=No · Delay on=Need Pressure Tempo [ms] · Delay off=0
- Logique :
  - **Activating** = `Tension Pressure [bar] > Pression filtered [bar]`
- Lit : ``, `Need Pressure Tempo`, `Pression filtered`, `Tension Pressure`
- Utilisé par : `Super Ok tension`
- Ligne export : 13884 · id 32781

#### Tension Error Parameter  `FP`
- Propriétés : Unit=% · Default mode={100}
- Utilisé par : `Over Tension`
- Ligne export : 13929 · id 32790

#### Delay Off super ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `Super Ok tension`
- Lit : ``, `Super Ok tension`
- Utilisé par : `Super Ok Tension Math`
- Ligne export : 13941 · id 32827

#### Super Ok Tension Math  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `Delay Off super ok tension * 100`
- Lit : ``, `Delay Off super ok tension`
- Utilisé par : `Slope Super Ok`
- Ligne export : 13984 · id 32835

#### Slope Super Ok  `SFC`
- Propriétés : Input channel=Super Ok Tension Math [%] · Enable=Yes · Type=Slopes · Slopes={{5; 1}; {2; 2}}
- Lit : `Super Ok Tension Math`
- Utilisé par : `Over Tension`
- Ligne export : 14027 · id 32843

#### Over Tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Over Tension) OR (Slope Super Ok [%] > Tension Error Parameter [%])`
  - **Blocking** = `not(System Started DELAYS)`
- Lit : ``, `Slope Super Ok`, `System Started DELAYS`, `Tension Error Parameter`
- Utilisé par : `Super Ok tension`, `Track Tension Error`, `Event log: Hydraulic Event`
- Ligne export : 14045 · id 32791

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
- Utilisé par : `Delay Off super ok tension`, `EV tendre Chenille`
- Ligne export : 14105 · id 32801

#### Wait engine Stop  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=4000
- Logique :
  - **Activating** = `Wait engine start`
- Lit : ``, `Wait engine start`
- Utilisé par : `Tension State`
- Ligne export : 14241 · id 32845

#### Tension State  `SMC`
- Propriétés : Default state name=ON/OFF
- Fonction *Parking* :
  - **Activating** = `Wait engine Stop`
  - **Blocking** = `(Wait engine start) OR (Tracks pressure Mode)`
- Fonction *Unthingten* :
  - **Activating** = `Tracks pressure Mode`
- Lit : ``, `Tracks pressure Mode`, `Wait engine Stop`, `Wait engine start`
- Utilisé par : *(personne)*
- Ligne export : 14284 · id 32853

#### Track Tension Error  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Track Tension Error · Text=Try a Calibrating (Setting/Maintenance). Use straight. Contact your service center. · Channel=Track pressure [bar]
- Logique :
  - **Showing** = `Over Tension`
- Lit : ``, `Over Tension`, `Track pressure`
- Utilisé par : *(personne)*
- Ligne export : 14369 · id 32890

####   `VIN`
- Propriétés : Name, English=Oil level Analog · Unit=% · Reference voltage=Reference voltage A · Error value=0 · Calibration={50; 1800; 0; 100} · Alarms={Yes; 5; No; 120} · Module=MC42 (MC42[1]) · Module index=0
- Lit : ``, `Oil level`
- Utilisé par : ``, `10 hours check-up`, `10 minutes auto tender`, `?Speed OK`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Activate Critical State`, `Activate High Aft Fan`, `Activate High Aft Fan`, `Activate Low Aft Fan`, `Activate Low Aft Fan`, `Activate exhaust Fan`, `Activate exhaust Fan`, `Actual engine, % torque`, `Adress Loose`, `Adress_Search`, `Adresse_Mem`, `Alert critical engine`, `Alert critical exhaust`, `Alert critical hydraulic`, `Allow Cruise`, `Allow Run Cruise`, `Amber warning lamp`, `Auto Fast after Down`, `Auto Fast after Down Wait`, `Auto Off Bip`, `Auto PAUSE/OFF`, `Auto Stop Timer`, `AutoStopafter 5 secondes`, `Backlight Value`, `Backward Curent`, `Bad pressure`, `Bip`, `Brake Activation`, `C`, `Calcul Accélération`, `CanBus Error TB`, `Command State`, `Couché night`, `Counter`, `Coupure Thermique avec sécurité`, `Critical Temp Timer`, `Current Date MEN`, `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `DOWN Counter`, `Days in current year`, `Dec`, `Delay Off super ok tension`, `Digit Engine On`, `Don'push button`, `Duree`, `ENGINE RUN`, `ENGINE RUN`, `ET`, `ET h`, `EV tendre Chenille`, `Engine Stopped`, `Engine Thermal State`, `Engine coolant temp`, `Engine hours`, `Engine oil pressure`, `Engine speed to send`, `Engine_Started`, `Force Lock`, `Force Unlock`, `Forward Curent`, `Fuel Line Timer`, `Fuel line ignition`, `Fuel line ignition`, `Fuel line ignition IDC`, `Fuel line ignition Output`, `GPS Adresse Find`, `GPS_Adresse_Find_Int`, `Garmin - NMEA`, `HIGH arm`, `High Temp Timer`, `Ho`, `Ho_night`, `Hot Oil`, `Hour actual`, `Hydraulic pump statut`, `Hydraulics Temperature State`, `ID Fault`, `ID Prog`, `IDC Auto Sleep`, `IDC EV By Pass`, `IDC EV By Pass Down`, `IDC EV By Pass sel`, `IDC Free`, `IDC Speed Free`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `IDC Tension`, `Iguana PIN`, `Inter Allumage Thermique`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter EV By Pass`, `Inter EV DOWN`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP`, `Inter EV UP Delay`, `Inter EV Verin`, `Inter Lock landing`, `Inter Tension`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Inter Unlock`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Is_EB2`, `Is_FORD`, `Joystick Zero`, `Joystick is not in neutral position`, `Joystick not zero`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `K1 Fan Rear / Fan`, `K1 fuse is blown`, `K10`, `K10 fuse is blown`, `K11`, `K11 fuse is blown`, `K12`, `K12 fuse is blown`, `K13`, `K13 fuse is blown`, `K2 Fan Super / Pump`, `K2 fuse is blown`, `K3 Fan Exhaust / AutoOff`, `K3 fuse is blown`, `K4 Engine Power / Search Lights`, `K4 fuse is blown`, `K5 Engine Start`, `K5 fuse is blown`, `K6 Engine Water Pump`, `K6 fuse is blown`, `K7 Exhaust Water Pump`, `K7 fuse is blown`, `K8`, `K8 fuse is blown`, `K9`, `K9 fuse is blown`, `KeyBox Can Ok`, `Ko to move`, `L`, `LOW arm`, `Latence Math`, `LatenceTimer`, `Latitude Compute`, `Latitude Compute MEN`, `Levé night`, `Lock`, `Lock landing`, `Lon`, `Longitude Compute`, `Longitude Compute MEN`, `Low Temp Timer`, `M`, `MD3 - DOWN`, `MD3 - UP`, `MD3 START`, `MD3 STOP`, `MD3 start last checks`, `MDGN-+BAT:MC2[1]`, `Malfunction lamp`, `Manual Start Engine Pulse IDC`, `Math Droit`, `Math Gauche`, `Max Manip`, `Mid Temp Timer`, `Min Speed Ok`, `Mini Wait`, `Méridian`, `Need Min Speed`, `Need Pressure`, `New Timer`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `OK UP/DOWN`, `ON/OFF/Untighed`, `Oil Security Activation`, `Oil level`, `Oil level`, `Oil pressure`, `Ok tension`, `Ok to move`, `Out START Engine`, `Out SWITCH ON Engine`, `Over Tension`, `PIN 44`, `PIn State`, `Persistant Water Temp`, `Power State Int`, `Pre Fuel line ignition IDC`, `Process Down Engine`, `Progress`, `Protect lamp`, `Pump 1 Right`, `Pump 1 Right Filter ECC1`, `Pump 2 Left`, `Pump 2 Left Filter ECC1`, `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Red stop lamp`, `Reset`, `Reset Speed`, `Reset Startup`, `Reset Startup`, `Reset on startup`, `SPEED Engine`, `STARTING`, `Show Debug`, `Show P-1-2`, `Speed CAN`, `Speed Data remapping`, `Speed Int`, `Speed Mode`, `Speed Pump`, `Speed State`, `Speed_RPM_needed`, `Starter Proctection IDC`, `Starter Protection`, `Starter Protection CMSG`, `State`, `State All Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `State Up/Down`, `State Up/Down Raw`, `Stop Cruise`, `Stop To Move`, `Stop in :`, `Store TIMER UP/DOWN`, `Sunrise`, `Sunset`, `Super Ok Tension Math`, `Super Ok tension`, `System Started DELAYS`, `TRACK DOWN`, `TRACK UP`, `Temperature State`, `Tension State`, `Thermic Engine STATE`, `Time_Diff_MEM`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer UP/DOWN`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Toggle Free`, `Track DOWN Delay`, `Track Tension Error`, `Track UP Delay`, `Tracks pressure Mode`, `Trigger`, `Trigger HeartBeat`, `Trigger Speed`, `Trigger Timer`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `Unlock`, `Unlock landing`, `Untighten`, `VIEW BUTTON States`, `VIEW ENGINE RUN PAGE`, `VIEW SPEED STATE`, `VIEW START PAGE`, `Voyant Pression Huile Moteur`, `Wait Bad Pressure`, `Wait Buz 2`, `Wait Hot Temperature`, `Wait Oil Level`, `Wait after stating`, `Wait engine Stop`, `Wait engine start`, `Wait_Very_Low_Oil_Level`, `Works Latitude`, `Year since 2000`, `oldExhaust Temperature State`, `out T Exhaust Temps`, `torque OR % load at current speed`, `Event log: Check UP`, `Event log: Hydraulic Event`, `Event log: Thermic Events`, `Statistics log: System Stats`, `Statistics log: Thermic Stats`
- Ligne export : 14415 · id 54805

#### OIL security  `SP`
- Propriétés : Input channel=None · Default state name=ACTIVE · States={Unactive}
- Utilisé par : ``
- Ligne export : 14440 · id 61515

####   `MEM`
- Propriétés : Name, English=OIL Security · Input channel=OIL security · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : ``, `OIL security`, `Reset Startup`
- Utilisé par : ``, `10 hours check-up`, `10 minutes auto tender`, `?Speed OK`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Activate Critical State`, `Activate High Aft Fan`, `Activate High Aft Fan`, `Activate Low Aft Fan`, `Activate Low Aft Fan`, `Activate exhaust Fan`, `Activate exhaust Fan`, `Actual engine, % torque`, `Adress Loose`, `Adress_Search`, `Adresse_Mem`, `Alert critical engine`, `Alert critical exhaust`, `Alert critical hydraulic`, `Allow Cruise`, `Allow Run Cruise`, `Amber warning lamp`, `Auto Fast after Down`, `Auto Fast after Down Wait`, `Auto Off Bip`, `Auto PAUSE/OFF`, `Auto Stop Timer`, `AutoStopafter 5 secondes`, `Backlight Value`, `Backward Curent`, `Bad pressure`, `Bip`, `Brake Activation`, `C`, `Calcul Accélération`, `CanBus Error TB`, `Command State`, `Couché night`, `Counter`, `Coupure Thermique avec sécurité`, `Critical Temp Timer`, `Current Date MEN`, `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `DOWN Counter`, `Days in current year`, `Dec`, `Delay Off super ok tension`, `Digit Engine On`, `Don'push button`, `Duree`, `ENGINE RUN`, `ENGINE RUN`, `ET`, `ET h`, `EV tendre Chenille`, `Engine Stopped`, `Engine Thermal State`, `Engine coolant temp`, `Engine hours`, `Engine oil pressure`, `Engine speed to send`, `Engine_Started`, `Force Lock`, `Force Unlock`, `Forward Curent`, `Fuel Line Timer`, `Fuel line ignition`, `Fuel line ignition`, `Fuel line ignition IDC`, `Fuel line ignition Output`, `GPS Adresse Find`, `GPS_Adresse_Find_Int`, `Garmin - NMEA`, `HIGH arm`, `High Temp Timer`, `Ho`, `Ho_night`, `Hot Oil`, `Hour actual`, `Hydraulic pump statut`, `Hydraulics Temperature State`, `ID Fault`, `ID Prog`, `IDC Auto Sleep`, `IDC EV By Pass`, `IDC EV By Pass Down`, `IDC EV By Pass sel`, `IDC Free`, `IDC Speed Free`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `IDC Tension`, `Iguana PIN`, `Inter Allumage Thermique`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter EV By Pass`, `Inter EV DOWN`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP`, `Inter EV UP Delay`, `Inter EV Verin`, `Inter Lock landing`, `Inter Tension`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Inter Unlock`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Is_EB2`, `Is_FORD`, `Joystick Zero`, `Joystick is not in neutral position`, `Joystick not zero`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `K1 Fan Rear / Fan`, `K1 fuse is blown`, `K10`, `K10 fuse is blown`, `K11`, `K11 fuse is blown`, `K12`, `K12 fuse is blown`, `K13`, `K13 fuse is blown`, `K2 Fan Super / Pump`, `K2 fuse is blown`, `K3 Fan Exhaust / AutoOff`, `K3 fuse is blown`, `K4 Engine Power / Search Lights`, `K4 fuse is blown`, `K5 Engine Start`, `K5 fuse is blown`, `K6 Engine Water Pump`, `K6 fuse is blown`, `K7 Exhaust Water Pump`, `K7 fuse is blown`, `K8`, `K8 fuse is blown`, `K9`, `K9 fuse is blown`, `KeyBox Can Ok`, `Ko to move`, `L`, `LOW arm`, `Latence Math`, `LatenceTimer`, `Latitude Compute`, `Latitude Compute MEN`, `Levé night`, `Lock`, `Lock landing`, `Lon`, `Longitude Compute`, `Longitude Compute MEN`, `Low Temp Timer`, `M`, `MD3 - DOWN`, `MD3 - UP`, `MD3 START`, `MD3 STOP`, `MD3 start last checks`, `MDGN-+BAT:MC2[1]`, `Malfunction lamp`, `Manual Start Engine Pulse IDC`, `Math Droit`, `Math Gauche`, `Max Manip`, `Mid Temp Timer`, `Min Speed Ok`, `Mini Wait`, `Méridian`, `Need Min Speed`, `Need Pressure`, `New Timer`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `OK UP/DOWN`, `ON/OFF/Untighed`, `Oil Security Activation`, `Oil level`, `Oil level`, `Oil pressure`, `Ok tension`, `Ok to move`, `Out START Engine`, `Out SWITCH ON Engine`, `Over Tension`, `PIN 44`, `PIn State`, `Persistant Water Temp`, `Power State Int`, `Pre Fuel line ignition IDC`, `Process Down Engine`, `Progress`, `Protect lamp`, `Pump 1 Right`, `Pump 1 Right Filter ECC1`, `Pump 2 Left`, `Pump 2 Left Filter ECC1`, `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Red stop lamp`, `Reset`, `Reset Speed`, `Reset Startup`, `Reset Startup`, `Reset on startup`, `SPEED Engine`, `STARTING`, `Show Debug`, `Show P-1-2`, `Speed CAN`, `Speed Data remapping`, `Speed Int`, `Speed Mode`, `Speed Pump`, `Speed State`, `Speed_RPM_needed`, `Starter Proctection IDC`, `Starter Protection`, `Starter Protection CMSG`, `State`, `State All Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `State Up/Down`, `State Up/Down Raw`, `Stop Cruise`, `Stop To Move`, `Stop in :`, `Store TIMER UP/DOWN`, `Sunrise`, `Sunset`, `Super Ok Tension Math`, `Super Ok tension`, `System Started DELAYS`, `TRACK DOWN`, `TRACK UP`, `Temperature State`, `Tension State`, `Thermic Engine STATE`, `Time_Diff_MEM`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer UP/DOWN`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Toggle Free`, `Track DOWN Delay`, `Track Tension Error`, `Track UP Delay`, `Tracks pressure Mode`, `Trigger`, `Trigger HeartBeat`, `Trigger Speed`, `Trigger Timer`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `Unlock`, `Unlock landing`, `Untighten`, `VIEW BUTTON States`, `VIEW ENGINE RUN PAGE`, `VIEW SPEED STATE`, `VIEW START PAGE`, `Voyant Pression Huile Moteur`, `Wait Bad Pressure`, `Wait Buz 2`, `Wait Hot Temperature`, `Wait Oil Level`, `Wait after stating`, `Wait engine Stop`, `Wait engine start`, `Wait_Very_Low_Oil_Level`, `Works Latitude`, `Year since 2000`, `oldExhaust Temperature State`, `out T Exhaust Temps`, `torque OR % load at current speed`, `Event log: Check UP`, `Event log: Hydraulic Event`, `Event log: Thermic Events`, `Statistics log: System Stats`, `Statistics log: Thermic Stats`
- Ligne export : 14452 · id 61517

#### Wait_Very_Low_Oil_Level  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Oil level Analog [%] < 80`
  - **Blocking** = `1 = OIL Security`
- Lit : ``, `Oil level`
- Utilisé par : `Oil Security Activation`, `Oil level`, `Oil level Very Low Input`, `Stop in :`, `Wait_Very_Low_Oil_Level`, `Event log: Hydraulic Event`, `MD3 page: BASE`, `Statistics log: Thermic Stats`
- Ligne export : 14496 · id 54806

#### Stop in :  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=30
- Logique :
  - **Decreasing** = `Wait_Very_Low_Oil_Level`
  - **Resetting** = `(Wait_Very_Low_Oil_Level ? 0 : 100)`
- Lit : ``, `Wait_Very_Low_Oil_Level`
- Utilisé par : `Oil level`
- Ligne export : 14550 · id 54814

#### Oil level  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=Low Oil Tracks Level · Text, English=Stop Engine Immediately. And contact your service center. · Channel=Stop in : [s]
- Logique :
  - **Showing** = `Wait_Very_Low_Oil_Level`
  - **Hiding** = `not(Wait_Very_Low_Oil_Level)`
- Lit : ``, `Stop in :`, `Wait_Very_Low_Oil_Level`
- Utilisé par : ``, `Oil level`, `Wait Oil Level`, `Wait_Very_Low_Oil_Level`, `Measure group: Engine Thermic`, `Measure group: Hydraulic`
- Ligne export : 14611 · id 54825

#### Wait Oil Level  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Oil level Analog [%] < 90`
- Lit : ``, `Oil level`
- Utilisé par : `Oil level`
- Ligne export : 14667 · id 54834

#### Oil level  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header, English=Low Oil Tracks Level · Text, English=Check Oil Level and hydraulic circuit. And contact your service center. · Channel=Oil level Analog [%]
- Logique :
  - **Showing** = `Wait Oil Level`
  - **Hiding** = `not(Wait Oil Level)`
- Lit : ``, `Oil level`, `Wait Oil Level`
- Utilisé par : ``, `Wait Oil Level`, `Wait_Very_Low_Oil_Level`, `Measure group: Engine Thermic`, `Measure group: Hydraulic`
- Ligne export : 14712 · id 54842
