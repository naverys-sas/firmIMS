# MC42 app — mc.Thermic

485 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## mc.Thermic — actif seulement si `Is_Thermic mc`

#### T Stall speed eng on  `IP`
- Propriétés : Default mode={700}
- Utilisé par : `T Engine_Started mc`
- Ligne export : 55743 · id 193874

#### T Stall speed eng off  `IP`
- Propriétés : Default mode={600}
- Utilisé par : `T Engine_Started mc`
- Ligne export : 55755 · id 193875

#### T Engine_Started mc  `IDC`
> hysteris on dectection of stall engine
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Speed CAN 42 [rpm] > T Stall speed eng on   [Latching And]`
  - **Blocking** = `T Speed CAN 42 [rpm] < T Stall speed eng off`
- Lit : `T Speed CAN 42`, `T Stall speed eng off`, `T Stall speed eng on`
- Utilisé par : `Batt or engine started mc`, `E&T Engines ready`, `Engine Stopped`, `Force Lock`, `IMS Hours Therm`, `Inter EV DOWN delay`, `Inter EV UP Delay`, `T AutoStopafter 5 secondes`, `T Bloc`, `T Critical Temp Timer`, `T ECC1_Engine_Temp`, `T ECC1_Oil_Temp`, `T ECC1_Power`, `T ECC1_Speed`, `T EV tendre Chenille`, `T Engine State mc`, `T Fuel line ignition IDC`, `T High Temp Timer`, `T Inter EV Frein`, `T K6 Engine Water Pump`, `T K7 Exhaust Water Pump`, `T Low Temp Timer`, `T MD3 start last checks`, `T Mid Temp Timer`, `T Persistant Water Temp`, `T Persistant Water Temp_1`, `T Pre Fuel line ignition IDC`, `T System Started DELAYS`, `T Wait Bad Pressure`, `T Wait Hot Temperature`, `Timer hiding first 10 hours check message`, `Timer hiding second 10 hours check message`, `Unlock landing`, `Event log: Thermic Events`, `Statistics log: Thermic Stats`
- Ligne export : 55767 · id 192464

#### T Activate exhaust Fan mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Activate exhaust Fan`
- Lit : `T Activate exhaust Fan`
- Utilisé par : `T Activate Exhaust`
- Ligne export : 66397 · id 193850

#### T Activate Low Aft Fan mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Activate Low Aft Fan`
- Lit : `T Activate Low Aft Fan`
- Utilisé par : `T Activate Low Aft Fan`
- Ligne export : 66440 · id 193858

#### T Activate High Aft Fan mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Activate High Aft Fan`
- Lit : `T Activate High Aft Fan`
- Utilisé par : `T Activate High Aft Fan`
- Ligne export : 66483 · id 193866

#### Exhaust temp sensor mc  `DP`
- Propriétés : True text=Active · False text=Unactive · Default mode={True}
- Utilisé par : `Exhaust temp sensor mc sel`, `Single adjust item: Exhaust temp sensor MC42`
- Ligne export : 66526 · id 198578

#### Exhaust temp sensor mc sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Exhaust temp sensor mc) AND not_a_sim AND (Is_EB2 mc or Is_Kubo mc)`
- Lit : `Exhaust temp sensor mc`, `Is_EB2 mc`, `Is_Kubo mc`, `not_a_sim`
- Utilisé par : `Active le groupe: mc.Thermic / T.Exhaust temp`
- Ligne export : 66539 · id 212354

#### T Engine State mc  `SMC`
- Propriétés : Default state name=OFF
- Fonction *STARTING* :
  - **Activating** = `T Out START Engine`
  - **Blocking** = `T Engine_Started mc`
- Fonction *READY* :
  - **Activating** = `T Engine_Started mc`
- Lit : `T Engine_Started mc`, `T Out START Engine`
- Utilisé par : `Power State Int T`, `Power State Int T`, `T VIEW ENGINE STATE`, `T VIEW TRACK STATE`
- Ligne export : 73468 · id 208417

#### IMS Hours Therm  `TMR`
- Propriétés : Type (Unit)=Hours [h] · Store value=Yes · Reset value=0
- Logique :
  - **Increasing** = `T Engine_Started mc`
- Lit : `T Engine_Started mc`
- Utilisé par : `IMS hours therm RESET`, `Maintenance`, `Therm/10 hours true entre 10 et 16h`, `Therm/md4 10 hours check-up 45`, `Therm/md4 10 hours check-up 45`, `first! 1yr maintenance`, `MD4-10 page: MAINTENANCE`, `MD4-5 page: MAINTENANCE`
- Ligne export : 73546 · id 239873

## mc.Thermic / T.Engine Speed calc

#### T Joystick not zero  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Math Gauche Left 45 [%] <> 0) OR (Math Droit Right 45 [%] <> 0)`
- Lit : `Math Droit Right 45`, `Math Gauche Left 45`
- Utilisé par : `T SPEED Engine`
- Ligne export : 59452 · id 193038

#### T Force at 2200 rpm  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `T SPEED Engine`, `Single adjust item: Force at 2200 rpm`
- Ligne export : 59506 · id 193047

#### T SPEED Engine  `SMC`
- Propriétés : Default state name=Default
- Fonction *Ralenti* :
  - **Activating** = `(T Joystick not zero = 0) and (not(T Inter EV Verin))`
  - **Blocking** = `(T Force at 2200 rpm) OR (Screen_Speed Input mc = 5)`
- Fonction *Regime PV* :
  - **Activating** = `(Screen_Speed Input mc = 2) OR (Screen_Speed Input mc = 1)`
  - **Blocking** = `(T Inter EV Verin) OR (T Force at 2200 rpm)`
- Fonction *Régime GV* :
  - **Activating** = `(Screen_Speed Input mc = 3) OR (Screen_Speed Input mc = 6)`
  - **Blocking** = `(T Force at 2200 rpm) OR (T Inter EV Verin) OR (T Persistant Water Temp [°C] >= T Water °C Critical Critical [°C])`
- Fonction *Regim UP/DOWN* :
  - **Activating** = `T Inter EV Verin`
  - **Blocking** = `T Force at 2200 rpm`
- Fonction *2200 tr/min* :
  - **Activating** = `T Force at 2200 rpm`
- Lit : `Screen_Speed Input mc`, `T Force at 2200 rpm`, `T Inter EV Verin`, `T Joystick not zero`, `T Persistant Water Temp`, `T Water °C Critical Critical`
- Utilisé par : `T Accel Filter`, `T Calcul Accélération`, `T Decel Filter`
- Ligne export : 59519 · id 193048

#### T Max Manip  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxOf (Absolute)(Abs(Math Droit Right 45 [%]), Abs(Math Gauche Left 45 [%]))`
- Lit : `Math Droit Right 45`, `Math Gauche Left 45`
- Utilisé par : `T Calcul Accélération`
- Ligne export : 59784 · id 193090

#### T General speed filtering  `FP`
> Max speed slope applied while running tracks
- Propriétés : Unit=%/s · Mode selector=T Engine type · Default mode: EB2 1.2L={25} · Mode 1: FORD 1.5L={100} · Mode 2: Kubo={25}
- Lit : `T Engine type`
- Utilisé par : `T Accel Filter`, `T Decel Filter`, `Single adjust item: General speed filtering`
- Ligne export : 59835 · id 193099

#### In T UP/DOWN Speed  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=T Tension/UpDown Speed [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Tension/UpDown Speed`
- Utilisé par : `T Calcul Accélération`
- Ligne export : 59851 · id 193100

#### In T IDLE Speed  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=T IDLE Speed [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T IDLE Speed`
- Utilisé par : `T Calcul Accélération`
- Ligne export : 59865 · id 193101

#### In T Slow Speed  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=T Slow Max  Speed [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Slow Max  Speed`
- Utilisé par : `T Calcul Accélération`
- Ligne export : 59879 · id 193102

#### In T Hight Speed  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=T Hight Speed [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Hight Speed`
- Utilisé par : `T Calcul Accélération`
- Ligne export : 59893 · id 193103

#### In T Min Speed mode  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=T Min Speed mode [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Min Speed mode`
- Utilisé par : `T Calcul Accélération`
- Ligne export : 59907 · id 193104

#### T Calcul Accélération  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed · Function selector=T SPEED Engine
- Fonction *Default* :
  - **Controlling** = `1800`
- Fonction *Ralenti* :
  - **Controlling** = `In T IDLE Speed [rpm]`
- Fonction *Regime PV* :
  - **Controlling** = `lin(T Max Manip: 0->In T Min Speed mode [rpm], 100->In T Slow Speed [rpm], Freeze)`
- Fonction *Régime GV* :
  - **Controlling** = `lin(T Max Manip: 0->In T Min Speed mode [rpm], 100->In T Hight Speed [rpm], Freeze)`
- Fonction *Regim UP/DOWN* :
  - **Controlling** = `In T UP/DOWN Speed [rpm]`
- Fonction *2200 tr/min* :
  - **Controlling** = `2200`
- Lit : `In T Hight Speed`, `In T IDLE Speed`, `In T Min Speed mode`, `In T Slow Speed`, `In T UP/DOWN Speed`, `T Max Manip`, `T SPEED Engine`
- Utilisé par : `T Speed_RPM_needed`
- Ligne export : 59921 · id 193105

#### T System Started DELAYS  `IDC`
- Propriétés : Toggle=No · Delay on=750 · Delay off=500
- Logique :
  - **Activating** = `T Engine_Started mc`
- Lit : `T Engine_Started mc`
- Utilisé par : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `Over Tension`, `T 10 minutes auto tender`, `T STARTING`, `T State All Speed`, `Wait engine start`
- Ligne export : 60128 · id 199266

#### T STARTING  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=8000
- Logique :
  - **Activating** = `PositiveFlank(T System Started DELAYS)`
- Lit : `T System Started DELAYS`
- Utilisé par : `T Need Min Speed`
- Ligne export : 60171 · id 193155

#### T Throttle pulse at Start up  `DP`
> for cold start
- Propriétés : Default mode={True}
- Utilisé par : `T Need Min Speed`, `Single adjust item: ?Throttle pulse at Start up`
- Ligne export : 60215 · id 193163

#### T Tempo Need Min Speed  `IP`
> Tempo to allow Idle speed after a Torque request from hydraulic accessories
- Propriétés : Unit=ms · Default mode={300}
- Utilisé par : `T Need Min Speed`, `Single adjust item: Tempo Need Min Speed`
- Ligne export : 60228 · id 193164

#### T Need Min Speed  `IDC`
> Activated if ther is an hydraulic Torque coming from Accessories pump
- Propriétés : Toggle=No · Delay on=0 · Delay off=T Tempo Need Min Speed [ms]
- Logique :
  - **Activating** = `(T STARTING and T Throttle pulse at Start up) OR (T Inter EV By Pass) OR (T EV tendre Chenille) OR (T Bloc)`
- Lit : `T Bloc`, `T EV tendre Chenille`, `T Inter EV By Pass`, `T STARTING`, `T Tempo Need Min Speed`, `T Throttle pulse at Start up`
- Utilisé par : `T Speed_RPM_needed`
- Ligne export : 60240 · id 193165

#### In T Tension Speed  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=T Tension/UpDown Speed [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Tension/UpDown Speed`
- Utilisé par : `T Speed_RPM_needed`
- Ligne export : 60306 · id 193176

#### T Speed_RPM_needed  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxOf((T Need Min Speed * In T Tension Speed [rpm]), T Calcul Accélération [rpm])`
- Lit : `In T Tension Speed`, `T Calcul Accélération`, `T Need Min Speed`
- Utilisé par : `T Speed Data remapping`, `T Speed Error Calcul`, `T Speed error`, `MD4-5 page: BASE`, `MD4-5 page: INFO`
- Ligne export : 60320 · id 193177

#### T Speed Data remapping  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(T Speed_RPM_needed [rpm]: 1000->0, 4000->100, Freeze)`
- Lit : `T Speed_RPM_needed`
- Utilisé par : `T TSC1 Filter`
- Ligne export : 60373 · id 193186

#### T Accel Filter  `MAC`
> Max Accel selection depending on Speed engine mode
- Propriétés : Unit=%/s · Function selector=T SPEED Engine
- Fonction *Default* :
  ```qcode
  Result:= T General speed filtering
  ```
- Fonction *Ralenti* :
  ```qcode
  Result:= T General speed filtering
  ```
- Fonction *Regime PV* :
  ```qcode
  Result:= T General speed filtering
  ```
- Fonction *Régime GV* :
  ```qcode
  Result:= T General speed filtering
  ```
- Fonction *Regim UP/DOWN* :
  ```qcode
  Result:= T General speed filtering
  ```
- Fonction *2200 tr/min* :
  ```qcode
  Result:= T General speed filtering
  ```
- Lit : `T General speed filtering`, `T SPEED Engine`
- Utilisé par : `T TSC1 Filter`
- Ligne export : 60420 · id 193233

#### T Idle decel filter  `FP`
> Max decel in Idle mode to avoid stall engine
- Propriétés : Mode selector=T Engine type · Default mode: EB2 1.2L={10} · Mode 1: FORD 1.5L={100} · Mode 2: Kubo={10}
- Lit : `T Engine type`
- Utilisé par : `T Decel Filter`, `Single adjust item: Idle decel filter`
- Ligne export : 60478 · id 193232

#### T Decel Filter  `MAC`
- Propriétés : Unit=%/s · Function selector=T SPEED Engine
- Fonction *Default* :
  ```qcode
  Result:= T General speed filtering
  ```
- Fonction *Ralenti* :
  ```qcode
  Result:= T Idle decel filter
  ```
- Fonction *Regime PV* :
  ```qcode
  Result:= T General speed filtering
  ```
- Fonction *Régime GV* :
  ```qcode
  Result:= T General speed filtering
  ```
- Fonction *Regim UP/DOWN* :
  ```qcode
  Result:= T General speed filtering
  ```
- Fonction *2200 tr/min* :
  ```qcode
  Result:= T General speed filtering
  ```
- Lit : `T General speed filtering`, `T Idle decel filter`, `T SPEED Engine`
- Utilisé par : `T TSC1 Filter`
- Ligne export : 60494 · id 193290

#### T TSC1 Filter  `SFC`
- Propriétés : Input channel=T Speed Data remapping [%] · Enable=Yes · Type=Slopes · Slopes={{T Accel Filter [%/s]; T Decel Filter [%/s]}; {T Accel Filter [%/s]; T Accel Filter [%/s]}}
- Lit : `T Accel Filter`, `T Decel Filter`, `T Speed Data remapping`
- Utilisé par : `T Engine speed to send`
- Ligne export : 60552 · id 193194

#### in T Speed CAN  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=T Speed CAN 42 [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Speed CAN 42`
- Utilisé par : `T Min Speed Ok`, `T Speed error`
- Ligne export : 60570 · id 193195

#### T Speed error  `MAC`
> % of error between request speed and real speed
- Propriétés : Unit=%
- Logique :
  ```qcode
  If T Speed_RPM_needed <> 0 then
  Result:= (T Speed_RPM_needed-in T Speed CAN) / T Speed_RPM_needed
  endif
  ```
- Lit : `T Speed_RPM_needed`, `in T Speed CAN`
- Utilisé par : `T ?Speed OK`
- Ligne export : 60584 · id 193196

#### T Max Speed Gap  `IP`
> Max speed gap to allow by-pass action
- Propriétés : Unit=% · Default mode={20}
- Utilisé par : `T ?Speed OK`, `Single adjust item: Max Speed Gap`
- Ligne export : 60605 · id 193207

#### T ?Speed OK  `IDC`
- Propriétés : Toggle=No · Delay on=300 · Delay off=50
- Logique :
  - **Activating** = `T Speed error [%] < T Max Speed Gap [%]`
- Lit : `T Max Speed Gap`, `T Speed error`
- Utilisé par : *(personne)*
- Ligne export : 60617 · id 193208

#### T Engine speed to send  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `T TSC1 Filter [%]`
- Lit : `T TSC1 Filter`
- Utilisé par : `In T Engine speed`
- Ligne export : 60662 · id 193216

#### In T Min Speed acc1  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=T Min Speed acc1 [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Min Speed acc1`
- Utilisé par : `T Min Speed Ok`
- Ligne export : 60704 · id 193347

#### T Min Speed Ok  `IDC`
> True if engine speed is high enough to face Hydraulic torque. 1000 ms tempo Off to manage temporary deceleration
- Propriétés : Toggle=No · Delay on=0 · Delay off=300
- Logique :
  - **Activating** = `in T Speed CAN [rpm] >= In T Min Speed acc1 [rpm]`
- Lit : `In T Min Speed acc1`, `in T Speed CAN`
- Utilisé par : `T Inter EV By Pass`
- Ligne export : 60718 · id 193224

## mc.Thermic / T.Engine i/o

#### T Engine type  `SP`
- Propriétés : Input channel=None · Default state name=EB2 1.2L · States={FORD 1.5L; Kubo}
- Utilisé par : `% load at current speed T45`, `Actual engine, % torque T45`, `Amber warning lamp T45`, `Engine coolant temp T45`, `Is_EB2 mc`, `Is_FORD mc`, `Is_Kubo mc`, `Malfunction lamp T45`, `Protect lamp T45`, `Red stop lamp T45`, `Speed CAN T45`, `T FS - Start réduction`, `T General speed filtering`, `T Hight Speed`, `T IDLE Speed`, `T Idle decel filter`, `T Min Speed acc1`, `T Min Speed mode`, `T Para enclench voyant pression huile`, `T Pump Curent  - Hight Speed`, `T Pump Curent - Low Speed`, `T Pump Curent - Super Low Speed`, `T Pump Max curent`, `T Slow Max  Speed`, `T Tension/UpDown Speed`, `T Water °C Critical`, `T Water °C Critical Critical`, `T Water °C High`, `T Water °C Low`, `Single adjust item: Engine type`
- Ligne export : 61765 · id 193456

#### In T Engine speed  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=T Engine speed to send [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Engine speed to send`
- Utilisé par : `In Engine speed to send EB2 45-T`, `In Engine speed to send Kubo 45-T`, `in Engine speed to send Ford`
- Ligne export : 61778 · id 193466

#### T Pump Curent - Low Speed  `FP`
- Propriétés : Unit=mA · Mode selector=T Engine type · Default mode: EB2 1.2L={900} · Mode 1: FORD 1.5L={900} · Mode 2: Kubo={900}
- Lit : `T Engine type`
- Utilisé par : `In T Curent - Low Speed`, `Single adjust item: Pump Curent - Low Speed`
- Ligne export : 61792 · id 193613

#### T Pump Curent  - Hight Speed  `FP`
- Propriétés : Unit=mA · Mode selector=T Engine type · Default mode: EB2 1.2L={1200} · Mode 1: FORD 1.5L={1200} · Mode 2: Kubo={1200}
- Lit : `T Engine type`
- Utilisé par : `In T Curent  - Hight Speed`, `Single adjust item: Pump Curent  - Hight Speed`
- Ligne export : 61808 · id 193614

#### T Pump Curent - Super Low Speed  `FP`
- Propriétés : Unit=mA · Mode selector=T Engine type · Default mode: EB2 1.2L={660} · Mode 1: FORD 1.5L={660} · Mode 2: Kubo={660}
- Lit : `T Engine type`
- Utilisé par : `In T Curent - Super Low Speed`, `Single adjust item: Pump Curent - Super Low Speed`
- Ligne export : 61824 · id 193615

#### T Pump Max curent  `FP`
- Propriétés : Unit=mA · Mode selector=T Engine type · Default mode: EB2 1.2L={1150} · Mode 1: FORD 1.5L={1150} · Mode 2: Kubo={1150}
- Lit : `T Engine type`
- Utilisé par : `In T Max curent`, `Single adjust item: Pump Max curent`
- Ligne export : 61840 · id 193616

#### T IDLE Speed  `FP`
> Engine speed when no torque is required
- Propriétés : Unit=rpm · Mode selector=T Engine type · Default mode: EB2 1.2L={1200} · Mode 1: FORD 1.5L={1000} · Mode 2: Kubo={1100}
- Lit : `T Engine type`
- Utilisé par : `In T IDLE Speed`, `Single adjust item: IDLE Speed`
- Ligne export : 61856 · id 193617

#### T Slow Max  Speed  `FP`
> Max engine speed when Joystick is full forward in slow mode
- Propriétés : Unit=rpm · Mode selector=T Engine type · Default mode: EB2 1.2L={2300} · Mode 1: FORD 1.5L={2300} · Mode 2: Kubo={2300}
- Lit : `T Engine type`
- Utilisé par : `In T Slow Speed`, `Single adjust item: Slow Max  Speed`
- Ligne export : 61872 · id 193618

#### T Hight Speed  `FP`
> Max engine speed when joystick is full forward in Fast mode
- Propriétés : Unit=rpm · Mode selector=T Engine type · Default mode: EB2 1.2L={3000} · Mode 1: FORD 1.5L={3000} · Mode 2: Kubo={3000}
- Lit : `T Engine type`
- Utilisé par : `In T Hight Speed`, `Single adjust item: Hight Speed`
- Ligne export : 61888 · id 193619

#### T Tension/UpDown Speed  `FP`
> Target speed to move arms
- Propriétés : Unit=rpm · Mode selector=T Engine type · Default mode: EB2 1.2L={1800} · Mode 1: FORD 1.5L={1700} · Mode 2: Kubo={1800}
- Lit : `T Engine type`
- Utilisé par : `In T Tension Speed`, `In T UP/DOWN Speed`, `Single adjust item: Tension/UpDown Speed`
- Ligne export : 61904 · id 193620

#### T Min Speed mode  `FP`
- Propriétés : Unit=rpm · Mode selector=T Engine type · Default mode: EB2 1.2L={1300} · Mode 1: FORD 1.5L={1200} · Mode 2: Kubo={1300}
- Lit : `T Engine type`
- Utilisé par : `In T Min Speed mode`, `Single adjust item: Min Speed mode`
- Ligne export : 61920 · id 193621

#### % load at current speed T45  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=T Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `% load at current speed EB2 T45 [%]`
- Fonction *FORD 1.5L* :
  - **Controlling** = `% load at current speed Ford T45 [%]`
- Fonction *Kubo* :
  - **Controlling** = `% load at current speed Kubo T45 [%]`
- Lit : `% load at current speed EB2 T45`, `% load at current speed Ford T45`, `% load at current speed Kubo T45`, `T Engine type`
- Utilisé par : `T % load at current speed`
- Ligne export : 61936 · id 203734

#### T % load at current speed  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `% load at current speed T45 [%]`
- Lit : `% load at current speed T45`
- Utilisé par : `in T % load at current speed`
- Ligne export : 62040 · id 193637

#### sim thermal engine speed  `IP`
- Propriétés : Mode selector=sim state moteur · Default mode: not_sim={0} · Mode 1: sim={1200}
- Lit : `sim state moteur`
- Utilisé par : `T Speed CAN 42`, `Adjust group: Master Sim Menu`, `Single adjust item: sim thermal engine speed`
- Ligne export : 62082 · id 211727

#### Speed CAN T45  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed · Function selector=T Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Engine speed EB2 T45 [rpm]`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Engine speed Ford T45 [rpm]`
- Fonction *Kubo* :
  - **Controlling** = `Engine speed Kubo T45 [rpm]`
- Lit : `Engine speed EB2 T45`, `Engine speed Ford T45`, `Engine speed Kubo T45`, `T Engine type`
- Utilisé par : `T Speed CAN 42`, `MD4-5 page: BASE`, `MD4-5 page: INFO`, `MD4-5 page: MAIN Thermic`
- Ligne export : 62096 · id 203750

#### T Speed CAN 42  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Speed CAN T45 [rpm] + sim thermal engine speed`
- Lit : `Speed CAN T45`, `sim thermal engine speed`
- Utilisé par : `T Engine_Started mc`, `T Speed Error Calcul`, `in T Speed CAN`
- Ligne export : 62200 · id 193730

#### T Speed Error Calcul  `MAC`
- Propriétés : Unit=%
- Logique :
  ```qcode
  if T Speed_RPM_needed  >  0 then
  Speed := 100 - (T Speed CAN 42 / T Speed_RPM_needed) * 100
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
- Lit : `Speed`, `T Speed CAN 42`, `T Speed_RPM_needed`
- Utilisé par : `in T Speed Error Calc`
- Ligne export : 62258 · id 193652

#### Engine coolant temp T45  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed · Function selector=T Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Engine coolant temperature EB2 T45 [°C]`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Engine coolant temperature Ford T45 [°C]`
- Fonction *Kubo* :
  - **Controlling** = `Engine coolant temperature Kubo T45 [°C]`
- Lit : `Engine coolant temperature EB2 T45`, `Engine coolant temperature Ford T45`, `Engine coolant temperature Kubo T45`, `T Engine type`
- Utilisé par : `T Engine coolant temp`
- Ligne export : 62288 · id 203718

#### T Engine coolant temp  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Engine coolant temp T45 [°C]`
- Lit : `Engine coolant temp T45`
- Utilisé par : `in T Engine coolant temperature`, `in T Engine coolant temperature`, `Statistics log: Thermic Stats`
- Ligne export : 62392 · id 193699

#### T Min Speed acc1  `FP`
- Propriétés : Unit=rpm · Mode selector=T Engine type · Default mode: EB2 1.2L={1550} · Mode 1: FORD 1.5L={1200} · Mode 2: Kubo={1550}
- Lit : `T Engine type`
- Utilisé par : `In T Min Speed acc1`, `Single adjust item: Min Speed acc1`
- Ligne export : 62434 · id 193746

#### Is_EB2 mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Engine type = 0`
- Lit : `T Engine type`
- Utilisé par : `Exhaust temp sensor mc sel`, `Active le groupe: mc.Thermic / T.Engine i/o / EB2 T45`
- Ligne export : 62450 · id 203549

#### Is_FORD mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Engine type = 1`
- Lit : `T Engine type`
- Utilisé par : `Active le groupe: mc.Thermic / T.Engine i/o / Ford T45`
- Ligne export : 63314 · id 203596

#### Malfunction lamp T45  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=T Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Malfunction lamp EB2 T45`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Malfunction lamp Ford T`
- Fonction *Kubo* :
  - **Controlling** = `Malfunction lamp Kubo T45`
- Lit : `Malfunction lamp EB2 T45`, `Malfunction lamp Ford T`, `Malfunction lamp Kubo T45`, `T Engine type`
- Utilisé par : *(personne)*
- Ligne export : 64178 · id 203643

#### Red stop lamp T45  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=T Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Red stop lamp EB2 T45`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Red stop lamp Ford T`
- Fonction *Kubo* :
  - **Controlling** = `Red stop lamp Kubo T45`
- Lit : `Red stop lamp EB2 T45`, `Red stop lamp Ford T`, `Red stop lamp Kubo T45`, `T Engine type`
- Utilisé par : *(personne)*
- Ligne export : 64282 · id 203658

#### Amber warning lamp T45  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=T Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Amber warning lamp EB2 T45`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Amber warning lamp Ford T`
- Fonction *Kubo* :
  - **Controlling** = `Amber warning lamp Kubo T45`
- Lit : `Amber warning lamp EB2 T45`, `Amber warning lamp Ford T`, `Amber warning lamp Kubo T45`, `T Engine type`
- Utilisé par : *(personne)*
- Ligne export : 64386 · id 203673

#### Protect lamp T45  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=T Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Amber warning lamp EB2 T45`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Amber warning lamp Ford T`
- Fonction *Kubo* :
  - **Controlling** = `Protect lamp Kubo T45`
- Lit : `Amber warning lamp EB2 T45`, `Amber warning lamp Ford T`, `Protect lamp Kubo T45`, `T Engine type`
- Utilisé par : *(personne)*
- Ligne export : 64490 · id 203688

#### Actual engine, % torque T45  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=T Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Actual engine, % torque EB2 T45 [%]`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Actual engine, % torque, Ford T45 [%]`
- Fonction *Kubo* :
  - **Controlling** = `Actual engine, % torque Kubo T45 [%]`
- Lit : `Actual engine, % torque EB2 T45`, `Actual engine, % torque Kubo T45`, `Actual engine, % torque, Ford T45`, `T Engine type`
- Utilisé par : *(personne)*
- Ligne export : 64594 · id 203703

#### T ECU ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Engine speed Ford T45 [rpm] Status = OK) OR (Engine speed EB2 T45 [rpm] Status = OK) OR (Engine speed Kubo T45 [rpm] Status = OK)`
- Lit : `Engine speed EB2 T45`, `Engine speed Ford T45`, `Engine speed Kubo T45`
- Utilisé par : `T Engine coolant temp T45 ok`, `MD4-5 page: INFO`
- Ligne export : 64698 · id 212770

#### Is_Kubo mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Engine type = 2`
- Lit : `T Engine type`
- Utilisé par : `Exhaust temp sensor mc sel`, `Active le groupe: mc.Thermic / T.Engine i/o / Kubota WG16`
- Ligne export : 64761 · id 232589

#### T Engine coolant temp T45 ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(((Engine coolant temperature EB2 T45 [°C] Status = OK) or (Engine coolant temperature Ford T45 [°C] Status = OK)) or (Engine coolant temperature Kubo T45 [°C] Status = OK)) AND (T ECU ok)`
- Lit : `Engine coolant temperature EB2 T45`, `Engine coolant temperature Ford T45`, `Engine coolant temperature Kubo T45`, `T ECU ok`
- Utilisé par : `MD4-5 page: INFO`
- Ligne export : 65638 · id 232931

## mc.Thermic / T.Engine i/o / EB2 T45 — actif seulement si `Is_EB2 mc`

#### DM1 EB2 T45  `DM1IN`
> Diagnostic Message 1
- Propriétés : SPN conversion method=4 · FMI texts={OK; Above normal, most severe; Below normal, most severe; Erratic or intermittent; Voltage above normal; Voltage below normal; Current below normal; Current above normal; Out of adjustment; Abnormal frequency; Abnormal update rate; Abnormal rate of change; Root cause not known; Bad component; Out of calibration; Special instructions; Above normal; Above normal, severe; Below normal; Below normal, severe; Received data in error; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Not available} · Show message=All · Dialog for undefined SPNs=Yes · Enable DM2 support=False · Enable lamp flash=No · Parameters={SPN 98; SPN 100; SPN 102; SPN 105; SPN 106; SPN 110; SPN 175; SPN 626; SPN 629; SPN 636; SPN 637; SPN 639; SPN 651; SPN 652; SPN 653; SPN 654; SPN 655; SPN 656; SPN 677; SPN 1485} · Module=EB2 T45 (J1939[0]) · Module index=0
- Lit : `SPN 100`, `SPN 102`, `SPN 105`, `SPN 106`, `SPN 110`, `SPN 1485`, `SPN 175`, `SPN 626`, `SPN 629`, `SPN 636`, `SPN 637`, `SPN 639`, `SPN 651`, `SPN 652`, `SPN 653`, `SPN 654`, `SPN 655`, `SPN 656`, `SPN 677`, `SPN 98`
- Utilisé par : *(personne)*
- Ligne export : 62520 · id 203558

#### SPN 629  `SPN`
> Controller #1
- Propriétés : SPN=629 · Dialog priority=Critical · Failures={{8; ErrNo 186 DTC 9.9: CPU Watchdog reset test failure.}; {13; ErrNo 186 DTC 9.9: Watchdog trip failure.}; {2; ErrNo 187 DTC 9.9: RAM cell test failure.}; {12; ErrNo 187 DTC 9.9: RAM address test failure.}; {11; ErrNo 186 DTC 9.9: Main and Fueling ASIC test fail.}}
- Lit : `12`, `13`
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62590 · id 203559

#### SPN 100  `SPN`
> Engine Oil Pressure
- Propriétés : SPN=100 · Dialog priority=Warning · Failures={{3; ErrNo 181 DTC 3.1: Voltage above normal.}; {4; ErrNo 182 DTC 3.1: Voltage below normal.}; {1; ErrNo 180 DTC 6.6: Data valid but below normal.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62616 · id 203560

#### SPN 110  `SPN`
> Engine Coolant Temperature
- Propriétés : SPN=110 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62636 · id 203561

#### SPN 105  `SPN`
> Air Intake Manifold 1 Temperature
- Propriétés : SPN=105 · Dialog priority=Warning · Failures={{3; ErrNo 25 DTC 3.2: Voltage above normal.}; {4; ErrNo 26 DTC 3.2: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62656 · id 203562

#### SPN 175  `SPN`
> Engine Oil Temperature 1
- Propriétés : SPN=175 · Dialog priority=Critical · Failures={{3; ErrNo 184 DTC 3.7: Voltage above normal.}; {4; ErrNo 185 DTC 3.7: Voltage below normal.}; {0; ErrNo 183 DTC 5.8: Data valid but above normal.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62676 · id 203563

#### SPN 102  `SPN`
> Boost Pressure
- Propriétés : SPN=102 · Dialog priority=Warning · Failures={{3; ErrNo 67 DTC 3.4: Voltage above normal.}; {4; ErrNo 68 DTC 3.4: Voltage below normal.}; {0; ErrNo 57 DTC -.-: Data valid but above normal.}; {1; ErrNo 58 DTC -.-: Data valid but below normal.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62696 · id 203564

#### SPN 1485  `SPN`
> ECU Main relay
- Propriétés : SPN=1485 · Dialog priority=Warning · Failures={{3; ErrNo 43 DTC 5.1: Short circuit high.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62719 · id 203565

#### SPN 637  `SPN`
> Timing sensor
- Propriétés : SPN=637 · Dialog priority=Warning · Failures={{8; ErrNo 18 DTC 2.4: Extra pulses.}; {2; ErrNo 101 DTC 2.4: Intermittent loss of signal.}; {3; ErrNo 18 DTC 2.4: Permanent loss of signal.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62733 · id 203566

#### SPN 656  `SPN`
> Injector Cylinder #06
- Propriétés : SPN=656 · Dialog priority=Warning · Failures={{2; ErrNo 160 DTC 7.6: Short circuit High Side to Vbatt.}; {4; ErrNo 161 DTC 7.6: Short circuit High or Low Side to ground.}; {3; ErrNo 162 DTC 7.6: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 165 DTC 7.6: Open circuit.}; {11; ErrNo 163 DTC 7.6: Unknown Error.}; {7; ErrNo 164 DTC 7.6: Cylinder balancing error.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62753 · id 203567

#### SPN 636  `SPN`
> Engine position sensor
- Propriétés : SPN=636 · Dialog priority=Critical · Failures={{8; ErrNo 103 DTC 2.5: Extra pulses or high frequency signal.}; {3; ErrNo 102 DTC 2.5: Permanent loss of signal.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62782 · id 203568

#### SPN 626  `SPN`
> Start enable device - Devices that assist an engine in starting - e.g. intake heaters and ether
- Propriétés : SPN=626 · Dialog priority=Warning · Failures={{3; ErrNo 76 DTC 5.4: Voltage above normal.}; {4; ErrNo 75 DTC 5.4: Voltage below normal.}; {5; ErrNo 74 DTC 5.4: Current below normal.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62799 · id 203569

#### SPN 677  `SPN`
> Engine Starter Motor Relay
- Propriétés : SPN=677 · Dialog priority=Warning · Failures={{3; ErrNo 41 DTC 4.6: Short circuit high.}; {4; ErrNo 42 DTC 4.6: Short circuit low.}; {5; ErrNo 107 DTC 4.6: Open circuit.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62819 · id 203570

#### SPN 655  `SPN`
> Injector Cylinder #05
- Propriétés : SPN=655 · Dialog priority=Warning · Failures={{2; ErrNo 150 DTC 7.5: Short circuit High Side to Vbatt.}; {4; ErrNo 151 DTC 7.5: Short circuit High or Low Side to ground.}; {3; ErrNo 152 DTC 7.5: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 155 DTC 7.5: Open circuit.}; {11; ErrNo 153 DTC 7.5: Unknown Error.}; {7; ErrNo 154 DTC 7.5: Cylinder balancing error.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62839 · id 203571

#### SPN 654  `SPN`
> Injector Cylinder #04
- Propriétés : SPN=654 · Dialog priority=Warning · Failures={{2; ErrNo 140 DTC 7.4: Short circuit High Side to Vbatt.}; {4; ErrNo 141 DTC 7.4: Short circuit High or Low Side to ground.}; {3; ErrNo 142 DTC 7.4: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 145 DTC 7.4: Open circuit.}; {11; ErrNo 143 DTC 7.4: Unknown Error.}; {7; ErrNo 144 DTC 7.4: Cylinder balancing error.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62868 · id 203572

#### SPN 653  `SPN`
> Injector Cylinder #03
- Propriétés : SPN=653 · Dialog priority=Warning · Failures={{2; ErrNo 130 DTC 7.3: Short circuit High Side to Vbatt.}; {4; ErrNo 131 DTC 7.3: Short circuit High or Low Side to ground.}; {3; ErrNo 132 DTC 7.3: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 135 DTC 7.3: Open circuit.}; {11; ErrNo 133 DTC 7.3: Unknown Error.}; {7; ErrNo 134 DTC 7.3: Cylinder balancing error.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62897 · id 203573

#### SPN 652  `SPN`
> Injector Cylinder #02
- Propriétés : SPN=652 · Dialog priority=Warning · Failures={{2; ErrNo 120 DTC 7.2: Short circuit High Side to Vbatt.}; {4; ErrNo 121 DTC 7.2: Short circuit High or Low Side to ground.}; {3; ErrNo 122 DTC 7.2: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 125 DTC 7.2: Open circuit.}; {11; ErrNo 123 DTC 7.2: Unknown Error.}; {7; ErrNo 124 DTC 7.2: Cylinder balancing error.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62926 · id 203574

#### SPN 651  `SPN`
> Injector Cylinder #01
- Propriétés : SPN=651 · Dialog priority=Warning · Failures={{2; ErrNo 110 DTC 7.1: Short circuit High Side to Vbatt.}; {4; ErrNo 111 DTC 7.1: Short circuit High or Low Side to ground.}; {3; ErrNo 112 DTC 7.1: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 115 DTC 7.1: Open circuit.}; {11; ErrNo 113 DTC 7.1: Unknown Error.}; {7; ErrNo 114 DTC 7.1: Cylinder balancing error.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62955 · id 203575

#### SPN 639  `SPN`
> J1939 Network #1, Primary Vehicle Network
- Propriétés : SPN=639 · Dialog priority=Warning · Failures={{2; ErrNo 106 DTC 6.5: Bus Off error.}; {9; ErrNo 106 DTC 6.5: Passive bus error.}; {12; ErrNo 38 DTC 6.5: Loss of message error.}; {11; ErrNo 38 DTC 6.5: Data registers read back failure.}}
- Lit : `12`
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 62984 · id 203576

#### Malfunction lamp EB2 T45  `MDGN`
- Propriétés : Value=Malfunction · Module=EB2 T45 (J1939[0]) · Module index=1
- Utilisé par : `Malfunction lamp T45`
- Ligne export : 63007 · id 203577

#### Red stop lamp EB2 T45  `MDGN`
- Propriétés : Value=Red stop · Module=EB2 T45 (J1939[0]) · Module index=2
- Utilisé par : `Red stop lamp T45`
- Ligne export : 63018 · id 203578

#### Amber warning lamp EB2 T45  `MDGN`
- Propriétés : Value=Amber warning · Module=EB2 T45 (J1939[0]) · Module index=3
- Utilisé par : `Amber warning lamp T45`, `Protect lamp T45`
- Ligne export : 63029 · id 203579

#### Protect lamp EB2 T45  `MDGN`
- Propriétés : Value=Protect · Module=EB2 T45 (J1939[0]) · Module index=4
- Utilisé par : *(personne)*
- Ligne export : 63040 · id 203580

#### SPN 98  `SPN`
> Engine oil level
- Propriétés : SPN=98 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 63051 · id 203581

#### SPN 106  `SPN`
- Propriétés : SPN=106 · Dialog priority=Dont show · Failures={{4; MAP Voltage Low}}
- Utilisé par : `DM1 EB2 T45`
- Ligne export : 63071 · id 203582

#### In Engine speed to send EB2 45-T  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=In T Engine speed [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `In T Engine speed`
- Utilisé par : `TSC1-A:J1939-0 EB2 T45`
- Ligne export : 63085 · id 203583

#### TSC1-A:J1939-0 EB2 T45  `TSC1`
- Propriétés : J1939 source address=3 · Engine speed limits={1000; 4000} · Speed channel=In Engine speed to send EB2 45-T [%] · Priority=3 · Transmit rate=20 · Override control mode=Speed control · Speed control conditions=Transient optimized, disengaged · Override control mode priority=Highest · Use checksum/counter=No · Control purpose=P32 = Temporary Powertrain Control (Original use of TSC1 Command) · Module=EB2 T45 (J1939[0]) · Module index=0
- Lit : `In Engine speed to send EB2 45-T`, `Speed`
- Utilisé par : *(personne)*
- Ligne export : 63099 · id 203584

#### EEC1 EB2 T45  `JFIN`
> Electronic Engine Controller 1
- Propriétés : Priority=6 · PGN=61444 · Timeout=3000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Driver's demand, engine % EB2 T45 [%]; 9}; {Actual engine, % torque EB2 T45 [%]; 17}; {Engine speed EB2 T45 [rpm]; 25}} · Module=EB2 T45 (J1939[0]) · Module index=0
- Lit : `Actual engine, % torque EB2 T45`, `Driver's demand, engine % EB2 T45`, `Engine speed EB2 T45`
- Utilisé par : *(personne)*
- Ligne export : 63122 · id 203585

#### Driver's demand, engine % EB2 T45  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `EEC1 EB2 T45`
- Ligne export : 63149 · id 203586

#### Actual engine, % torque EB2 T45  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `Actual engine, % torque T45`, `EEC1 EB2 T45`
- Ligne export : 63163 · id 203587

#### Engine speed EB2 T45  `JPIN`
- Propriétés : Unit=rpm · Length=2 Bytes (= 16 bits) · J1939 Error check=Yes · Resolution=0,125 · Offset=0 · Error value=0
- Utilisé par : `EEC1 EB2 T45`, `Speed CAN T45`, `T ECU ok`
- Ligne export : 63177 · id 203588

#### EEC2 EB2 T45  `JFIN`
> Electronic Engine Controller 2
- Propriétés : Priority=6 · PGN=61443 · Timeout=3000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Accelerator pedal position EB2 T45 [%]; 9}; {% load at current speed EB2 T45 [%]; 17}} · Module=EB2 T45 (J1939[0]) · Module index=1
- Lit : `% load at current speed EB2 T45`, `Accelerator pedal position EB2 T45`
- Utilisé par : *(personne)*
- Ligne export : 63191 · id 203589

#### Accelerator pedal position EB2 T45  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=0,4 · Offset=0 · Error value=0
- Utilisé par : `EEC2 EB2 T45`
- Ligne export : 63215 · id 203590

#### % load at current speed EB2 T45  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `% load at current speed T45`, `EEC2 EB2 T45`
- Ligne export : 63229 · id 203591

#### Engine Temperature EB 2  `JFIN`
> ET1
- Propriétés : Priority=6 · PGN=65262 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine coolant temperature EB2 T45 [°C]; 1}} · Module=EB2 T45 (J1939[0]) · Module index=2
- Lit : `Engine coolant temperature EB2 T45`
- Utilisé par : *(personne)*
- Ligne export : 63243 · id 203592

#### Engine coolant temperature EB2 T45  `JPIN`
- Propriétés : Unit=°C · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-40 · Error value=0
- Utilisé par : `Engine Temperature EB 2`, `Engine coolant temp T45`, `T Engine coolant temp T45 ok`
- Ligne export : 63264 · id 203593

#### Engine fluid level/pressure 1 EB2  `JFIN`
> EFL/P1
- Propriétés : Priority=6 · PGN=65263 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine oil pressure EB2 T45 [kPa]; 25}} · Module=EB2 T45 (J1939[0]) · Module index=3
- Lit : `Engine oil pressure EB2 T45`
- Utilisé par : *(personne)*
- Ligne export : 63278 · id 203594

#### Engine oil pressure EB2 T45  `JPIN`
- Propriétés : Unit=kPa · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=4 · Offset=0 · Error value=0
- Utilisé par : `Engine fluid level/pressure 1 EB2`
- Ligne export : 63299 · id 203595

## mc.Thermic / T.Engine i/o / Ford T45 — actif seulement si `Is_FORD mc`

#### DM1 Ford T45  `DM1IN`
> Diagnostic Message 1
- Propriétés : SPN conversion method=4 · FMI texts={OK; Above normal, most severe; Below normal, most severe; Erratic or intermittent; Voltage above normal; Voltage below normal; Current below normal; Current above normal; Out of adjustment; Abnormal frequency; Abnormal update rate; Abnormal rate of change; Root cause not known; Bad component; Out of calibration; Special instructions; Above normal; Above normal, severe; Below normal; Below normal, severe; Received data in error; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Not available} · Show message=All · Dialog for undefined SPNs=Yes · Enable DM2 support=False · Enable lamp flash=No · Parameters={SPN 98; SPN 100; SPN 102; SPN 105; SPN 106; SPN 110; SPN 175; SPN 626; SPN 629; SPN 636; SPN 637; SPN 639; SPN 651; SPN 652; SPN 653; SPN 654; SPN 655; SPN 656; SPN 677; SPN 1485} · Module=Ford T45 (J1939[0]) · Module index=0
- Lit : `SPN 100`, `SPN 102`, `SPN 105`, `SPN 106`, `SPN 110`, `SPN 1485`, `SPN 175`, `SPN 626`, `SPN 629`, `SPN 636`, `SPN 637`, `SPN 639`, `SPN 651`, `SPN 652`, `SPN 653`, `SPN 654`, `SPN 655`, `SPN 656`, `SPN 677`, `SPN 98`
- Utilisé par : *(personne)*
- Ligne export : 63384 · id 203605

#### SPN 629  `SPN`
> Controller #1
- Propriétés : SPN=629 · Dialog priority=Critical · Failures={{8; ErrNo 186 DTC 9.9: CPU Watchdog reset test failure.}; {13; ErrNo 186 DTC 9.9: Watchdog trip failure.}; {2; ErrNo 187 DTC 9.9: RAM cell test failure.}; {12; ErrNo 187 DTC 9.9: RAM address test failure.}; {11; ErrNo 186 DTC 9.9: Main and Fueling ASIC test fail.}}
- Lit : `12`, `13`
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63454 · id 203606

#### SPN 100  `SPN`
> Engine Oil Pressure
- Propriétés : SPN=100 · Dialog priority=Warning · Failures={{3; ErrNo 181 DTC 3.1: Voltage above normal.}; {4; ErrNo 182 DTC 3.1: Voltage below normal.}; {1; ErrNo 180 DTC 6.6: Data valid but below normal.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63480 · id 203607

#### SPN 110  `SPN`
> Engine Coolant Temperature
- Propriétés : SPN=110 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63500 · id 203608

#### SPN 105  `SPN`
> Air Intake Manifold 1 Temperature
- Propriétés : SPN=105 · Dialog priority=Warning · Failures={{3; ErrNo 25 DTC 3.2: Voltage above normal.}; {4; ErrNo 26 DTC 3.2: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63520 · id 203609

#### SPN 175  `SPN`
> Engine Oil Temperature 1
- Propriétés : SPN=175 · Dialog priority=Critical · Failures={{3; ErrNo 184 DTC 3.7: Voltage above normal.}; {4; ErrNo 185 DTC 3.7: Voltage below normal.}; {0; ErrNo 183 DTC 5.8: Data valid but above normal.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63540 · id 203610

#### SPN 102  `SPN`
> Boost Pressure
- Propriétés : SPN=102 · Dialog priority=Warning · Failures={{3; ErrNo 67 DTC 3.4: Voltage above normal.}; {4; ErrNo 68 DTC 3.4: Voltage below normal.}; {0; ErrNo 57 DTC -.-: Data valid but above normal.}; {1; ErrNo 58 DTC -.-: Data valid but below normal.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63560 · id 203611

#### SPN 1485  `SPN`
> ECU Main relay
- Propriétés : SPN=1485 · Dialog priority=Warning · Failures={{3; ErrNo 43 DTC 5.1: Short circuit high.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63583 · id 203612

#### SPN 637  `SPN`
> Timing sensor
- Propriétés : SPN=637 · Dialog priority=Warning · Failures={{8; ErrNo 18 DTC 2.4: Extra pulses.}; {2; ErrNo 101 DTC 2.4: Intermittent loss of signal.}; {3; ErrNo 18 DTC 2.4: Permanent loss of signal.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63597 · id 203613

#### SPN 656  `SPN`
> Injector Cylinder #06
- Propriétés : SPN=656 · Dialog priority=Warning · Failures={{2; ErrNo 160 DTC 7.6: Short circuit High Side to Vbatt.}; {4; ErrNo 161 DTC 7.6: Short circuit High or Low Side to ground.}; {3; ErrNo 162 DTC 7.6: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 165 DTC 7.6: Open circuit.}; {11; ErrNo 163 DTC 7.6: Unknown Error.}; {7; ErrNo 164 DTC 7.6: Cylinder balancing error.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63617 · id 203614

#### SPN 636  `SPN`
> Engine position sensor
- Propriétés : SPN=636 · Dialog priority=Critical · Failures={{8; ErrNo 103 DTC 2.5: Extra pulses or high frequency signal.}; {3; ErrNo 102 DTC 2.5: Permanent loss of signal.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63646 · id 203615

#### SPN 626  `SPN`
> Start enable device - Devices that assist an engine in starting - e.g. intake heaters and ether
- Propriétés : SPN=626 · Dialog priority=Warning · Failures={{3; ErrNo 76 DTC 5.4: Voltage above normal.}; {4; ErrNo 75 DTC 5.4: Voltage below normal.}; {5; ErrNo 74 DTC 5.4: Current below normal.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63663 · id 203616

#### SPN 677  `SPN`
> Engine Starter Motor Relay
- Propriétés : SPN=677 · Dialog priority=Warning · Failures={{3; ErrNo 41 DTC 4.6: Short circuit high.}; {4; ErrNo 42 DTC 4.6: Short circuit low.}; {5; ErrNo 107 DTC 4.6: Open circuit.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63683 · id 203617

#### SPN 655  `SPN`
> Injector Cylinder #05
- Propriétés : SPN=655 · Dialog priority=Warning · Failures={{2; ErrNo 150 DTC 7.5: Short circuit High Side to Vbatt.}; {4; ErrNo 151 DTC 7.5: Short circuit High or Low Side to ground.}; {3; ErrNo 152 DTC 7.5: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 155 DTC 7.5: Open circuit.}; {11; ErrNo 153 DTC 7.5: Unknown Error.}; {7; ErrNo 154 DTC 7.5: Cylinder balancing error.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63703 · id 203618

#### SPN 654  `SPN`
> Injector Cylinder #04
- Propriétés : SPN=654 · Dialog priority=Warning · Failures={{2; ErrNo 140 DTC 7.4: Short circuit High Side to Vbatt.}; {4; ErrNo 141 DTC 7.4: Short circuit High or Low Side to ground.}; {3; ErrNo 142 DTC 7.4: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 145 DTC 7.4: Open circuit.}; {11; ErrNo 143 DTC 7.4: Unknown Error.}; {7; ErrNo 144 DTC 7.4: Cylinder balancing error.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63732 · id 203619

#### SPN 653  `SPN`
> Injector Cylinder #03
- Propriétés : SPN=653 · Dialog priority=Warning · Failures={{2; ErrNo 130 DTC 7.3: Short circuit High Side to Vbatt.}; {4; ErrNo 131 DTC 7.3: Short circuit High or Low Side to ground.}; {3; ErrNo 132 DTC 7.3: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 135 DTC 7.3: Open circuit.}; {11; ErrNo 133 DTC 7.3: Unknown Error.}; {7; ErrNo 134 DTC 7.3: Cylinder balancing error.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63761 · id 203620

#### SPN 652  `SPN`
> Injector Cylinder #02
- Propriétés : SPN=652 · Dialog priority=Warning · Failures={{2; ErrNo 120 DTC 7.2: Short circuit High Side to Vbatt.}; {4; ErrNo 121 DTC 7.2: Short circuit High or Low Side to ground.}; {3; ErrNo 122 DTC 7.2: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 125 DTC 7.2: Open circuit.}; {11; ErrNo 123 DTC 7.2: Unknown Error.}; {7; ErrNo 124 DTC 7.2: Cylinder balancing error.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63790 · id 203621

#### SPN 651  `SPN`
> Injector Cylinder #01
- Propriétés : SPN=651 · Dialog priority=Warning · Failures={{2; ErrNo 110 DTC 7.1: Short circuit High Side to Vbatt.}; {4; ErrNo 111 DTC 7.1: Short circuit High or Low Side to ground.}; {3; ErrNo 112 DTC 7.1: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 115 DTC 7.1: Open circuit.}; {11; ErrNo 113 DTC 7.1: Unknown Error.}; {7; ErrNo 114 DTC 7.1: Cylinder balancing error.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63819 · id 203622

#### SPN 639  `SPN`
> J1939 Network #1, Primary Vehicle Network
- Propriétés : SPN=639 · Dialog priority=Warning · Failures={{2; ErrNo 106 DTC 6.5: Bus Off error.}; {9; ErrNo 106 DTC 6.5: Passive bus error.}; {12; ErrNo 38 DTC 6.5: Loss of message error.}; {11; ErrNo 38 DTC 6.5: Data registers read back failure.}}
- Lit : `12`
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63848 · id 203623

#### Malfunction lamp Ford T  `MDGN`
- Propriétés : Value=Malfunction · Module=Ford T45 (J1939[0]) · Module index=1
- Utilisé par : `Malfunction lamp T45`
- Ligne export : 63871 · id 203624

#### Red stop lamp Ford T  `MDGN`
- Propriétés : Value=Red stop · Module=Ford T45 (J1939[0]) · Module index=2
- Utilisé par : `Red stop lamp T45`
- Ligne export : 63882 · id 203625

#### Amber warning lamp Ford T  `MDGN`
- Propriétés : Value=Amber warning · Module=Ford T45 (J1939[0]) · Module index=3
- Utilisé par : `Amber warning lamp T45`, `Protect lamp T45`
- Ligne export : 63893 · id 203626

#### Protect lamp Ford T  `MDGN`
- Propriétés : Value=Protect · Module=Ford T45 (J1939[0]) · Module index=4
- Utilisé par : *(personne)*
- Ligne export : 63904 · id 203627

#### SPN 98  `SPN`
> Engine oil level
- Propriétés : SPN=98 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63915 · id 203628

#### SPN 106  `SPN`
- Propriétés : SPN=106 · Dialog priority=Dont show · Failures={{4; MAP Voltage Low}}
- Utilisé par : `DM1 Ford T45`
- Ligne export : 63935 · id 203629

#### in Engine speed to send Ford  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=In T Engine speed [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `In T Engine speed`
- Utilisé par : `TSC1-A:J1939-0 Ford T45`
- Ligne export : 63949 · id 203630

#### TSC1-A:J1939-0 Ford T45  `TSC1`
- Propriétés : J1939 source address=Default · Engine speed limits={1000; 4000} · Speed channel=in Engine speed to send Ford [%] · Priority=3 · Transmit rate=20 · Override control mode=Speed control · Speed control conditions=Transient optimized, disengaged · Override control mode priority=Highest · Use checksum/counter=No · Control purpose=P32 = Temporary Powertrain Control (Original use of TSC1 Command) · Module=Ford T45 (J1939[0]) · Module index=0
- Lit : `Speed`, `in Engine speed to send Ford`
- Utilisé par : *(personne)*
- Ligne export : 63963 · id 203631

#### EEC1 Ford T45  `JFIN`
> Electronic Engine Controller 1
- Propriétés : Priority=3 · PGN=61444 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Driver's demand, engine %, Ford T45 [%]; 9}; {Actual engine, % torque, Ford T45 [%]; 17}; {Engine speed Ford T45 [rpm]; 25}} · Module=Ford T45 (J1939[0]) · Module index=1
- Lit : `Actual engine, % torque, Ford T45`, `Driver's demand, engine %, Ford T45`, `Engine speed Ford T45`
- Utilisé par : *(personne)*
- Ligne export : 63986 · id 203632

#### Driver's demand, engine %, Ford T45  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `EEC1 Ford T45`
- Ligne export : 64013 · id 203633

#### Actual engine, % torque, Ford T45  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `Actual engine, % torque T45`, `EEC1 Ford T45`
- Ligne export : 64027 · id 203634

#### Engine speed Ford T45  `JPIN`
- Propriétés : Unit=rpm · Length=2 Bytes (= 16 bits) · J1939 Error check=Yes · Resolution=0,125 · Offset=0 · Error value=0
- Utilisé par : `EEC1 Ford T45`, `Speed CAN T45`, `T ECU ok`
- Ligne export : 64041 · id 203635

#### EEC2 Ford T45  `JFIN`
> Electronic Engine Controller 2
- Propriétés : Priority=3 · PGN=61443 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Accelerator pedal position Ford T45 [%]; 9}; {% load at current speed Ford T45 [%]; 17}} · Module=Ford T45 (J1939[0]) · Module index=2
- Lit : `% load at current speed Ford T45`, `Accelerator pedal position Ford T45`
- Utilisé par : *(personne)*
- Ligne export : 64055 · id 203636

#### Accelerator pedal position Ford T45  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=0,4 · Offset=0 · Error value=0
- Utilisé par : `EEC2 Ford T45`
- Ligne export : 64079 · id 203637

#### % load at current speed Ford T45  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `% load at current speed T45`, `EEC2 Ford T45`
- Ligne export : 64093 · id 203638

#### Engine Temperature Ford T45  `JFIN`
> ET1
- Propriétés : Priority=6 · PGN=65262 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine coolant temperature Ford T45 [°C]; 1}} · Module=Ford T45 (J1939[0]) · Module index=0
- Lit : `Engine coolant temperature Ford T45`
- Utilisé par : *(personne)*
- Ligne export : 64107 · id 203639

#### Engine coolant temperature Ford T45  `JPIN`
- Propriétés : Unit=°C · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-40 · Error value=0
- Utilisé par : `Engine Temperature Ford T45`, `Engine coolant temp T45`, `T Engine coolant temp T45 ok`
- Ligne export : 64128 · id 203640

#### Engine fluid level/pressure 1 Ford T45  `JFIN`
> EFL/P1
- Propriétés : Priority=6 · PGN=65263 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine oil pressure Ford T45 [kPa]; 25}} · Module=Ford T45 (J1939[0]) · Module index=3
- Lit : `Engine oil pressure Ford T45`
- Utilisé par : *(personne)*
- Ligne export : 64142 · id 203641

#### Engine oil pressure Ford T45  `JPIN`
- Propriétés : Unit=kPa · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=4 · Offset=0 · Error value=0
- Utilisé par : `Engine fluid level/pressure 1 Ford T45`
- Ligne export : 64163 · id 203642

## mc.Thermic / T.Engine i/o / Kubota WG16 — actif seulement si `Is_Kubo mc`

#### DM1 Kubo T45  `DM1IN`
> Diagnostic Message 1
- Propriétés : SPN conversion method=4 · FMI texts={OK; Above normal, most severe; Below normal, most severe; Erratic or intermittent; Voltage above normal; Voltage below normal; Current below normal; Current above normal; Out of adjustment; Abnormal frequency; Abnormal update rate; Abnormal rate of change; Root cause not known; Bad component; Out of calibration; Special instructions; Above normal; Above normal, severe; Below normal; Below normal, severe; Received data in error; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Not available} · Show message=All · Dialog for undefined SPNs=Yes · Enable DM2 support=False · Enable lamp flash=No · Parameters={SPN 98; SPN 100; SPN 102; SPN 105; SPN 106; SPN 110; SPN 175; SPN 626; SPN 629; SPN 636; SPN 637; SPN 639; SPN 651; SPN 652; SPN 653; SPN 654; SPN 655; SPN 656; SPN 677; SPN 1485} · Module=Kubota WG16 (J1939[0]) · Module index=0
- Lit : `SPN 100`, `SPN 102`, `SPN 105`, `SPN 106`, `SPN 110`, `SPN 1485`, `SPN 175`, `SPN 626`, `SPN 629`, `SPN 636`, `SPN 637`, `SPN 639`, `SPN 651`, `SPN 652`, `SPN 653`, `SPN 654`, `SPN 655`, `SPN 656`, `SPN 677`, `SPN 98`
- Utilisé par : *(personne)*
- Ligne export : 64831 · id 232601

#### SPN 629  `SPN`
> Controller #1
- Propriétés : SPN=629 · Dialog priority=Critical · Failures={{8; ErrNo 186 DTC 9.9: CPU Watchdog reset test failure.}; {13; ErrNo 186 DTC 9.9: Watchdog trip failure.}; {2; ErrNo 187 DTC 9.9: RAM cell test failure.}; {12; ErrNo 187 DTC 9.9: RAM address test failure.}; {11; ErrNo 186 DTC 9.9: Main and Fueling ASIC test fail.}}
- Lit : `12`, `13`
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 64901 · id 232602

#### SPN 100  `SPN`
> Engine Oil Pressure
- Propriétés : SPN=100 · Dialog priority=Warning · Failures={{3; ErrNo 181 DTC 3.1: Voltage above normal.}; {4; ErrNo 182 DTC 3.1: Voltage below normal.}; {1; ErrNo 180 DTC 6.6: Data valid but below normal.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 64927 · id 232603

#### SPN 110  `SPN`
> Engine Coolant Temperature
- Propriétés : SPN=110 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 64947 · id 232604

#### SPN 105  `SPN`
> Air Intake Manifold 1 Temperature
- Propriétés : SPN=105 · Dialog priority=Warning · Failures={{3; ErrNo 25 DTC 3.2: Voltage above normal.}; {4; ErrNo 26 DTC 3.2: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 64967 · id 232605

#### SPN 175  `SPN`
> Engine Oil Temperature 1
- Propriétés : SPN=175 · Dialog priority=Critical · Failures={{3; ErrNo 184 DTC 3.7: Voltage above normal.}; {4; ErrNo 185 DTC 3.7: Voltage below normal.}; {0; ErrNo 183 DTC 5.8: Data valid but above normal.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 64987 · id 232606

#### SPN 102  `SPN`
> Boost Pressure
- Propriétés : SPN=102 · Dialog priority=Warning · Failures={{3; ErrNo 67 DTC 3.4: Voltage above normal.}; {4; ErrNo 68 DTC 3.4: Voltage below normal.}; {0; ErrNo 57 DTC -.-: Data valid but above normal.}; {1; ErrNo 58 DTC -.-: Data valid but below normal.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65007 · id 232607

#### SPN 1485  `SPN`
> ECU Main relay
- Propriétés : SPN=1485 · Dialog priority=Warning · Failures={{3; ErrNo 43 DTC 5.1: Short circuit high.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65030 · id 232608

#### SPN 637  `SPN`
> Timing sensor
- Propriétés : SPN=637 · Dialog priority=Warning · Failures={{8; ErrNo 18 DTC 2.4: Extra pulses.}; {2; ErrNo 101 DTC 2.4: Intermittent loss of signal.}; {3; ErrNo 18 DTC 2.4: Permanent loss of signal.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65044 · id 232609

#### SPN 656  `SPN`
> Injector Cylinder #06
- Propriétés : SPN=656 · Dialog priority=Warning · Failures={{2; ErrNo 160 DTC 7.6: Short circuit High Side to Vbatt.}; {4; ErrNo 161 DTC 7.6: Short circuit High or Low Side to ground.}; {3; ErrNo 162 DTC 7.6: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 165 DTC 7.6: Open circuit.}; {11; ErrNo 163 DTC 7.6: Unknown Error.}; {7; ErrNo 164 DTC 7.6: Cylinder balancing error.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65064 · id 232610

#### SPN 636  `SPN`
> Engine position sensor
- Propriétés : SPN=636 · Dialog priority=Critical · Failures={{8; ErrNo 103 DTC 2.5: Extra pulses or high frequency signal.}; {3; ErrNo 102 DTC 2.5: Permanent loss of signal.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65093 · id 232611

#### SPN 626  `SPN`
> Start enable device - Devices that assist an engine in starting - e.g. intake heaters and ether
- Propriétés : SPN=626 · Dialog priority=Warning · Failures={{3; ErrNo 76 DTC 5.4: Voltage above normal.}; {4; ErrNo 75 DTC 5.4: Voltage below normal.}; {5; ErrNo 74 DTC 5.4: Current below normal.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65110 · id 232612

#### SPN 677  `SPN`
> Engine Starter Motor Relay
- Propriétés : SPN=677 · Dialog priority=Warning · Failures={{3; ErrNo 41 DTC 4.6: Short circuit high.}; {4; ErrNo 42 DTC 4.6: Short circuit low.}; {5; ErrNo 107 DTC 4.6: Open circuit.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65130 · id 232613

#### SPN 655  `SPN`
> Injector Cylinder #05
- Propriétés : SPN=655 · Dialog priority=Warning · Failures={{2; ErrNo 150 DTC 7.5: Short circuit High Side to Vbatt.}; {4; ErrNo 151 DTC 7.5: Short circuit High or Low Side to ground.}; {3; ErrNo 152 DTC 7.5: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 155 DTC 7.5: Open circuit.}; {11; ErrNo 153 DTC 7.5: Unknown Error.}; {7; ErrNo 154 DTC 7.5: Cylinder balancing error.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65150 · id 232614

#### SPN 654  `SPN`
> Injector Cylinder #04
- Propriétés : SPN=654 · Dialog priority=Warning · Failures={{2; ErrNo 140 DTC 7.4: Short circuit High Side to Vbatt.}; {4; ErrNo 141 DTC 7.4: Short circuit High or Low Side to ground.}; {3; ErrNo 142 DTC 7.4: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 145 DTC 7.4: Open circuit.}; {11; ErrNo 143 DTC 7.4: Unknown Error.}; {7; ErrNo 144 DTC 7.4: Cylinder balancing error.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65179 · id 232615

#### SPN 653  `SPN`
> Injector Cylinder #03
- Propriétés : SPN=653 · Dialog priority=Warning · Failures={{2; ErrNo 130 DTC 7.3: Short circuit High Side to Vbatt.}; {4; ErrNo 131 DTC 7.3: Short circuit High or Low Side to ground.}; {3; ErrNo 132 DTC 7.3: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 135 DTC 7.3: Open circuit.}; {11; ErrNo 133 DTC 7.3: Unknown Error.}; {7; ErrNo 134 DTC 7.3: Cylinder balancing error.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65208 · id 232616

#### SPN 652  `SPN`
> Injector Cylinder #02
- Propriétés : SPN=652 · Dialog priority=Warning · Failures={{2; ErrNo 120 DTC 7.2: Short circuit High Side to Vbatt.}; {4; ErrNo 121 DTC 7.2: Short circuit High or Low Side to ground.}; {3; ErrNo 122 DTC 7.2: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 125 DTC 7.2: Open circuit.}; {11; ErrNo 123 DTC 7.2: Unknown Error.}; {7; ErrNo 124 DTC 7.2: Cylinder balancing error.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65237 · id 232617

#### SPN 651  `SPN`
> Injector Cylinder #01
- Propriétés : SPN=651 · Dialog priority=Warning · Failures={{2; ErrNo 110 DTC 7.1: Short circuit High Side to Vbatt.}; {4; ErrNo 111 DTC 7.1: Short circuit High or Low Side to ground.}; {3; ErrNo 112 DTC 7.1: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 115 DTC 7.1: Open circuit.}; {11; ErrNo 113 DTC 7.1: Unknown Error.}; {7; ErrNo 114 DTC 7.1: Cylinder balancing error.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65266 · id 232618

#### SPN 639  `SPN`
> J1939 Network #1, Primary Vehicle Network
- Propriétés : SPN=639 · Dialog priority=Warning · Failures={{2; ErrNo 106 DTC 6.5: Bus Off error.}; {9; ErrNo 106 DTC 6.5: Passive bus error.}; {12; ErrNo 38 DTC 6.5: Loss of message error.}; {11; ErrNo 38 DTC 6.5: Data registers read back failure.}}
- Lit : `12`
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65295 · id 232619

#### Malfunction lamp Kubo T45  `MDGN`
- Propriétés : Value=Malfunction · Module=Kubota WG16 (J1939[0]) · Module index=1
- Utilisé par : `Malfunction lamp T45`
- Ligne export : 65318 · id 232620

#### Red stop lamp Kubo T45  `MDGN`
- Propriétés : Value=Red stop · Module=Kubota WG16 (J1939[0]) · Module index=2
- Utilisé par : `Red stop lamp T45`
- Ligne export : 65329 · id 232621

#### Amber warning lamp Kubo T45  `MDGN`
- Propriétés : Value=Amber warning · Module=Kubota WG16 (J1939[0]) · Module index=3
- Utilisé par : `Amber warning lamp T45`
- Ligne export : 65340 · id 232622

#### Protect lamp Kubo T45  `MDGN`
- Propriétés : Value=Protect · Module=Kubota WG16 (J1939[0]) · Module index=4
- Utilisé par : `Protect lamp T45`
- Ligne export : 65351 · id 232623

#### SPN 98  `SPN`
> Engine oil level
- Propriétés : SPN=98 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65362 · id 232624

#### SPN 106  `SPN`
- Propriétés : SPN=106 · Dialog priority=Dont show · Failures={{4; MAP Voltage Low}}
- Utilisé par : `DM1 Kubo T45`
- Ligne export : 65382 · id 232625

#### In Engine speed to send Kubo 45-T  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=In T Engine speed [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `In T Engine speed`
- Utilisé par : `TSC1-A:J1939-0 Kubo T45`
- Ligne export : 65396 · id 232626

#### TSC1-A:J1939-0 Kubo T45  `TSC1`
- Propriétés : J1939 source address=208 · Engine speed limits={1000; 4000} · Speed channel=In Engine speed to send Kubo 45-T [%] · Priority=3 · Transmit rate=10 · Override control mode=Speed control · Speed control conditions=Transient optimized, disengaged · Override control mode priority=Highest · Use checksum/counter=No · Control purpose=P32 = Temporary Powertrain Control (Original use of TSC1 Command) · Module=Kubota WG16 (J1939[0]) · Module index=0
- Lit : `In Engine speed to send Kubo 45-T`, `Speed`
- Utilisé par : *(personne)*
- Ligne export : 65410 · id 232627

#### EEC1 Kubo  `JFIN`
> Electronic Engine Controller 1
- Propriétés : Priority=3 · PGN=61444 · Timeout=3000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Driver's demand, engine % Kubo T45 [%]; 9}; {Actual engine, % torque Kubo T45 [%]; 17}; {Engine speed Kubo T45 [rpm]; 25}} · Module=Kubota WG16 (J1939[0]) · Module index=1
- Lit : `Actual engine, % torque Kubo T45`, `Driver's demand, engine % Kubo T45`, `Engine speed Kubo T45`
- Utilisé par : *(personne)*
- Ligne export : 65433 · id 232628

#### Driver's demand, engine % Kubo T45  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `EEC1 Kubo`
- Ligne export : 65460 · id 232629

#### Actual engine, % torque Kubo T45  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `Actual engine, % torque T45`, `EEC1 Kubo`
- Ligne export : 65474 · id 232630

#### Engine speed Kubo T45  `JPIN`
- Propriétés : Unit=rpm · Length=2 Bytes (= 16 bits) · J1939 Error check=Yes · Resolution=0,125 · Offset=0 · Error value=0
- Utilisé par : `EEC1 Kubo`, `Speed CAN T45`, `T ECU ok`
- Ligne export : 65488 · id 232631

#### EEC2 Kubo  `JFIN`
> Electronic Engine Controller 2
- Propriétés : Priority=3 · PGN=61443 · Timeout=3000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Accelerator pedal position Kubo T45 [%]; 9}; {% load at current speed Kubo T45 [%]; 17}} · Module=Kubota WG16 (J1939[0]) · Module index=0
- Lit : `% load at current speed Kubo T45`, `Accelerator pedal position Kubo T45`
- Utilisé par : *(personne)*
- Ligne export : 65502 · id 232632

#### Accelerator pedal position Kubo T45  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=0,4 · Offset=0 · Error value=0
- Utilisé par : `EEC2 Kubo`
- Ligne export : 65526 · id 232633

#### % load at current speed Kubo T45  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `% load at current speed T45`, `EEC2 Kubo`
- Ligne export : 65540 · id 232634

#### Engine Temperature Kubo  `JFIN`
> ET1
- Propriétés : Priority=6 · PGN=65262 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine coolant temperature Kubo T45 [°C]; 1}} · Module=Kubota WG16 (J1939[0]) · Module index=2
- Lit : `Engine coolant temperature Kubo T45`
- Utilisé par : *(personne)*
- Ligne export : 65554 · id 232635

#### Engine coolant temperature Kubo T45  `JPIN`
- Propriétés : Unit=°C · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-40 · Error value=0
- Utilisé par : `Engine Temperature Kubo`, `Engine coolant temp T45`, `T Engine coolant temp T45 ok`
- Ligne export : 65575 · id 232636

#### Engine fluid level/pressure 1 Kubo  `JFIN`
> EFL/P1
- Propriétés : Priority=6 · PGN=65263 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine oil pressure Kubo T45 [kPa]; 25}} · Module=Kubota WG16 (J1939[0]) · Module index=3
- Lit : `Engine oil pressure Kubo T45`
- Utilisé par : *(personne)*
- Ligne export : 65589 · id 232637

#### Engine oil pressure Kubo T45  `JPIN`
- Propriétés : Unit=kPa · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=4 · Offset=0 · Error value=0
- Utilisé par : `Engine fluid level/pressure 1 Kubo`
- Ligne export : 65610 · id 232638

## mc.Thermic / T.Exhaust temp — actif seulement si `Exhaust temp sensor mc sel`

#### T Exhaust coolant temp mc 52  `VIN`
- Propriétés : Unit=°C · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-ST · Calibration={250; 4750; -50; 150} · Alarms={No; 0; No; 100} · Module=MC42-33 (MC42[0]) · Module index=7
- Utilisé par : `Engine exhaust coolant sensor ok`, `out T Exhaust Temps`, `MD4-5 page: BASE`, `MD4-5 page: INFO`
- Ligne export : 66614 · id 198576

#### out T Exhaust Temps  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `T Exhaust coolant temp mc 52 [°C]`
- Lit : `T Exhaust coolant temp mc 52`
- Utilisé par : `T inExhaust temp`
- Ligne export : 66638 · id 198580

## mc.Thermic / T.KeyBox x100 T

#### mk T Aft Fan Max Test  `DP`
> Allows to test full fan without crancking
- Propriétés : True text=Force On · False text=Auto · Default mode={False}
- Utilisé par : `T K1 Fan Rear / Fan`, `T K2 Fan Super / Pump`, `Single adjust item: Aft Fan Max Test`
- Ligne export : 71365 · id 193898

#### mk T Aft Fan Low Test  `DP`
> Allows to test low fan without crancking
- Propriétés : True text=Force On · False text=Auto · Default mode={False}
- Utilisé par : `T K1 Fan Rear / Fan`, `Single adjust item: Aft Fan Low Test`
- Ligne export : 71378 · id 193899

#### T Activate Low Aft Fan  `FGI`
- Propriétés : Input type=Digital · Input=T Activate Low Aft Fan mc · Default state name=Default state
- Lit : `T Activate Low Aft Fan mc`
- Utilisé par : `T Activate Low Aft Fan mc`, `T K1 Fan Rear / Fan`, `T K6 Engine Water Pump`, `T K7 Exhaust Water Pump`, `MD4-5 page: MAIN Thermic`
- Ligne export : 71391 · id 193900

#### T K1 Fan Rear / Fan  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T Activate Low Aft Fan) OR (mk T Aft Fan Max Test) OR (mk T Aft Fan Low Test)`
- Lit : `T Activate Low Aft Fan`, `mk T Aft Fan Low Test`, `mk T Aft Fan Max Test`
- Utilisé par : `T ON_Bits`
- Ligne export : 71402 · id 193901

#### T Activate High Aft Fan  `FGI`
- Propriétés : Input type=Digital · Input=T Activate High Aft Fan mc · Default state name=Default state
- Lit : `T Activate High Aft Fan mc`
- Utilisé par : `T Activate High Aft Fan mc`, `T K2 Fan Super / Pump`, `T K6 Engine Water Pump`, `T K7 Exhaust Water Pump`, `MD4-5 page: MAIN Thermic`
- Ligne export : 71459 · id 193911

#### T K2 Fan Super / Pump  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T Activate High Aft Fan) OR (mk T Aft Fan Max Test)`
- Lit : `T Activate High Aft Fan`, `mk T Aft Fan Max Test`
- Utilisé par : `T ON_Bits`
- Ligne export : 71470 · id 193912

#### mk T Exhaust Fan Test  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `T K3 Fan Exhaust / AutoOff`, `Single adjust item: Exhaust Fan Test`
- Ligne export : 71520 · id 193921

#### T Activate Exhaust  `FGI`
- Propriétés : Input type=Digital · Input=T Activate exhaust Fan mc · Default state name=Default state
- Lit : `T Activate exhaust Fan mc`
- Utilisé par : `T K3 Fan Exhaust / AutoOff`, `T K6 Engine Water Pump`, `T K7 Exhaust Water Pump`
- Ligne export : 71533 · id 193922

#### T K3 Fan Exhaust / AutoOff  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T Activate Exhaust) OR (mk T Exhaust Fan Test)`
- Lit : `T Activate Exhaust`, `mk T Exhaust Fan Test`
- Utilisé par : `T ON_Bits`, `Event log: Thermic Events`
- Ligne export : 71544 · id 193923

#### T K4 Engine Power / Search Lights  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Out SWITCH ON Engine`
- Lit : `T Out SWITCH ON Engine`
- Utilisé par : `T ON_Bits`
- Ligne export : 71594 · id 193932

#### T K5 Engine Start  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Out START Engine`
- Lit : `T Out START Engine`
- Utilisé par : `T ON_Bits`
- Ligne export : 71637 · id 193940

#### mk T Force Engine pump  `DP`
> Allows to pilot Engine pump to flush the system
- Propriétés : True text=Force On · False text=Auto · Default mode={False}
- Utilisé par : `T K6 Engine Water Pump`, `Single adjust item: Force Engine pump`
- Ligne export : 71680 · id 193948

#### T K6 Engine Water Pump  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T Engine_Started mc) OR (T Activate Low Aft Fan) OR (T Activate High Aft Fan) OR (T Activate Exhaust) OR (mk T Force Engine pump)`
- Lit : `T Activate Exhaust`, `T Activate High Aft Fan`, `T Activate Low Aft Fan`, `T Engine_Started mc`, `mk T Force Engine pump`
- Utilisé par : `T ON_Bits`
- Ligne export : 71693 · id 193949

#### mk T Force Exhaust pump  `DP`
> Force Exhaust pump to flush the system
- Propriétés : True text=Force On · False text=Auto · Default mode={False}
- Utilisé par : `T K7 Exhaust Water Pump`, `Single adjust item: Force Exhaust pump`
- Ligne export : 71764 · id 193961

#### T K7 Exhaust Water Pump  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T Engine_Started mc) OR (T Activate Low Aft Fan) OR (T Activate High Aft Fan) OR (T Activate Exhaust) OR (mk T Force Exhaust pump)`
- Lit : `T Activate Exhaust`, `T Activate High Aft Fan`, `T Activate Low Aft Fan`, `T Engine_Started mc`, `mk T Force Exhaust pump`
- Utilisé par : `T ON_Bits`
- Ligne export : 71777 · id 193962

#### T K8  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Inflate system battery low)`
- Lit : `Inflate system battery low`
- Utilisé par : `T ON_Bits`
- Ligne export : 71848 · id 193974

#### T K9  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `T ON_Bits`
- Ligne export : 71892 · id 193981

#### T K10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `T ON_Bits`
- Ligne export : 71928 · id 193988

#### T K11  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `T ON_Bits`
- Ligne export : 71964 · id 193995

#### T K12  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `T ON_Bits`
- Ligne export : 72000 · id 194002

#### T K13  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `T ON_Bits`
- Ligne export : 72036 · id 194009

#### T ON_Bits  `IMAC`
- Logique :
  ```qcode
  Result := T K1 Fan Rear / Fan * 1 + T K2 Fan Super / Pump  * 2 + T K3 Fan Exhaust / AutoOff * 4 + T K4 Engine Power / Search Lights * 8 + T K5 Engine Start * 16 + T K6 Engine Water Pump * 32 + T K7 Exhaust Water Pump * 64 + T K8 * 128 + T K9 * 256 + T K10 * 512 + T K11 * 1024 + T K12 * 2048 + T K13 * 4096
  ```
- Lit : `T K1 Fan Rear / Fan`, `T K10`, `T K11`, `T K12`, `T K13`, `T K2 Fan Super / Pump`, `T K3 Fan Exhaust / AutoOff`, `T K4 Engine Power / Search Lights`, `T K5 Engine Start`, `T K6 Engine Water Pump`, `T K7 Exhaust Water Pump`, `T K8`, `T K9`
- Utilisé par : `T OFF_Bits`, `T ON_Bits_GOUT`
- Ligne export : 72072 · id 194016

#### T ON_Bits_GOUT  `GPOUT`
- Propriétés : Input value=T ON_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `T ON_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 72090 · id 194050

#### T OFF_Bits  `IMAC`
- Logique :
  ```qcode
  Result := bnot(T ON_Bits) band 0x1FFF
  ```
- Lit : `T ON_Bits`
- Utilisé par : `T OFF_Bits_GOUT`
- Ligne export : 72102 · id 194051

#### T OFF_Bits_GOUT  `GPOUT`
- Propriétés : Input value=T OFF_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `T OFF_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 72120 · id 194062

#### 0x70C  `GFIN`
- Propriétés : Identifier=0x70C · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={} · Module=Keybox X100 T (Generic) · Module index=1
- Lit : `0x70C`
- Utilisé par : `0x70C`, `Default Read ID`, `KeyBox T Can Ok`
- Ligne export : 72132 · id 203034

#### Byte 0  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`
- Ligne export : 72148 · id 203035

#### Byte 1  `GPOUT`
- Propriétés : Input value=0x0C · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`
- Ligne export : 72159 · id 203036

#### GFOUT-D:Generic  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=Keybox X100 T (Generic) · Module index=3
- Lit : `Byte 0`, `Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 72170 · id 203037

#### KeyBox T Can Ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `0x70C`
- Lit : `0x70C`
- Utilisé par : `T CanBus Error mc`, `MD4-5 page: INFO`, `Measure group: Canbus`
- Ligne export : 72192 · id 203038

#### T CanBus Error mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header, English=e1191 KeyBox · Text, English=The KeyBox don't respond with the system, try a reboot to fix.
- Logique :
  - **Showing** = `not(KeyBox T Can Ok)`
  - **Hiding** = `KeyBox T Can Ok`
- Lit : `KeyBox T Can Ok`
- Utilisé par : *(personne)*
- Ligne export : 72235 · id 203046

#### mk T Program KeyBox  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Trigger HeartBeat`, `Single adjust item: Program KeyBox`
- Ligne export : 72289 · id 203055

#### BYTE 0 - HB  `GPOUT`
- Propriétés : Input value=0x2B · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-B:Generic`, `GFOUT-C:Generic`
- Ligne export : 72302 · id 203056

#### BYTE 1 - HB  `GPOUT`
- Propriétés : Input value=0x17 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-B:Generic`, `GFOUT-C:Generic`
- Ligne export : 72313 · id 203057

#### BYTE 2 - HB  `GPOUT`
- Propriétés : Input value=0x10 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-B:Generic`, `GFOUT-C:Generic`
- Ligne export : 72324 · id 203058

#### BYTE 4 - HB  `GPOUT`
- Propriétés : Input value=0xF4 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-B:Generic`, `GFOUT-C:Generic`
- Ligne export : 72335 · id 203059

#### ID Prog  `IMAC`
- Logique :
  - **Controlling** = `0x0C + 0x600`
- Utilisé par : `GFOUT-B:Generic`, `GFOUT-C:Generic`
- Ligne export : 72346 · id 203060

#### BYTE 5 - HB  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-C:Generic`
- Ligne export : 72389 · id 203068

#### Trigger HeartBeat  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(mk T Program KeyBox)`
- Lit : `mk T Program KeyBox`
- Utilisé par : `GFOUT-C:Generic`, `Trigger Speed`
- Ligne export : 72400 · id 203069

#### GFOUT-C:Generic  `GFOUT`
- Propriétés : Identifier=ID Prog · Data length=8 · Send method=On trigger · Trigger=Trigger HeartBeat · Unused bits=Set to 0 · Parameters={{BYTE 0 - HB; 0}; {BYTE 1 - HB; 8}; {BYTE 2 - HB; 16}; {BYTE 4 - HB; 32}; {BYTE 5 - HB; 40}} · Module=Keybox X100 T (Generic) · Module index=2
- Lit : `BYTE 0 - HB`, `BYTE 1 - HB`, `BYTE 2 - HB`, `BYTE 4 - HB`, `BYTE 5 - HB`, `ID Prog`, `Trigger HeartBeat`
- Utilisé par : *(personne)*
- Ligne export : 72444 · id 203077

#### BYTE 0 - HB  `GPOUT`
- Propriétés : Input value=0x2F · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-B:Generic`, `GFOUT-C:Generic`
- Ligne export : 72476 · id 203078

#### BYTE 1 - HB  `GPOUT`
- Propriétés : Input value=0x10 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-B:Generic`, `GFOUT-C:Generic`
- Ligne export : 72487 · id 203079

#### BYTE 2 - HB  `GPOUT`
- Propriétés : Input value=0x20 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-B:Generic`, `GFOUT-C:Generic`
- Ligne export : 72498 · id 203080

#### BYTE 4 - HB  `GPOUT`
- Propriétés : Input value=0x02 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-B:Generic`, `GFOUT-C:Generic`
- Ligne export : 72509 · id 203081

#### Trigger Speed  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `NegativeFlank(Trigger HeartBeat)`
- Lit : `Trigger HeartBeat`
- Utilisé par : `GFOUT-B:Generic`
- Ligne export : 72520 · id 203082

#### GFOUT-B:Generic  `GFOUT`
- Propriétés : Identifier=ID Prog · Data length=8 · Send method=On trigger · Trigger=Trigger Speed · Unused bits=Set to 0 · Parameters={{BYTE 0 - HB; 0}; {BYTE 1 - HB; 8}; {BYTE 2 - HB; 16}; {BYTE 4 - HB; 32}} · Module=Keybox X100 T (Generic) · Module index=1
- Lit : `BYTE 0 - HB`, `BYTE 1 - HB`, `BYTE 2 - HB`, `BYTE 4 - HB`, `ID Prog`, `Trigger Speed`
- Utilisé par : *(personne)*
- Ligne export : 72564 · id 203090

#### ID Fault  `IMAC`
- Logique :
  - **Controlling** = `0x0C + 0x180`
- Utilisé par : `GFIN-A:Generic`
- Ligne export : 72593 · id 203091

#### GFIN-A:Generic  `GFIN`
- Propriétés : Identifier=ID Fault · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{K1 Fault; 1}; {K2 Fault; 2}; {K3 Fault; 3}; {K4 Fault; 4}; {K5 Fault; 5}; {K6 Fault; 6}; {K7 Fault; 7}; {K8 Fault; 8}; {K9 Fault; 9}; {K10 Fault; 10}; {K11 Fault; 11}; {K12 Fault; 12}; {K13 Fault; 13}} · Module=Keybox X100 T (Generic) · Module index=0
- Lit : `12`, `13`, `ID Fault`, `K1 Fault`, `K10 Fault`, `K11 Fault`, `K12 Fault`, `K13 Fault`, `K2 Fault`, `K3 Fault`, `K4 Fault`, `K5 Fault`, `K6 Fault`, `K7 Fault`, `K8 Fault`, `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 72636 · id 203099

#### K1 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `T K1 fuse is blown mc`
- Ligne export : 72691 · id 203100

#### T K1 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=Keybox error: FH1 fuse is blown -> Call AfterSales
- Logique :
  - **Showing** = `K1 Fault`
- Lit : `K1 Fault`
- Utilisé par : *(personne)*
- Ligne export : 72703 · id 203101

#### K2 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `T K2 fuse is blown mc`
- Ligne export : 72749 · id 203109

#### T K2 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=Keybox error: FH2 fuse is blown -> Call AfterSales
- Logique :
  - **Showing** = `K2 Fault`
- Lit : `K2 Fault`
- Utilisé par : *(personne)*
- Ligne export : 72761 · id 203110

#### K3 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `T K3 fuse is blown mc`
- Ligne export : 72807 · id 203118

#### T K3 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=Keybox error: FH3 fuse is blown -> Call AfterSales
- Logique :
  - **Showing** = `K3 Fault`
- Lit : `K3 Fault`
- Utilisé par : *(personne)*
- Ligne export : 72819 · id 203119

#### K4 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `K4 fuse is blown mc T`
- Ligne export : 72865 · id 203127

#### K4 fuse is blown mc T  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=Keybox error: FH5 fuse is blown -> Call AfterSales
- Logique :
  - **Showing** = `K4 Fault`
- Lit : `K4 Fault`
- Utilisé par : *(personne)*
- Ligne export : 72877 · id 203128

#### K5 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `K5 fuse is blown mc T`
- Ligne export : 72923 · id 203136

#### K5 fuse is blown mc T  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=Keybox error: FH4 fuse is blown -> Call AfterSales
- Logique :
  - **Showing** = `K5 Fault`
- Lit : `K5 Fault`
- Utilisé par : *(personne)*
- Ligne export : 72935 · id 203137

#### K6 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `K6 fuse is blown mc T`
- Ligne export : 72981 · id 203145

#### K6 fuse is blown mc T  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=Keybox error: FH6 fuse is blown -> Call AfterSales
- Logique :
  - **Showing** = `K6 Fault`
- Lit : `K6 Fault`
- Utilisé par : *(personne)*
- Ligne export : 72993 · id 203146

#### K7 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `K7 fuse is blown mc T`
- Ligne export : 73039 · id 203154

#### K7 fuse is blown mc T  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=Keybox error: FH7 fuse is blown -> Call AfterSales
- Logique :
  - **Showing** = `K7 Fault`
- Lit : `K7 Fault`
- Utilisé par : *(personne)*
- Ligne export : 73051 · id 203155

#### K8 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `K8 fuse is blown mc T`
- Ligne export : 73097 · id 203163

#### K8 fuse is blown mc T  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=Keybox error: FH8 fuse is blown -> Call AfterSales
- Logique :
  - **Showing** = `K8 Fault`
- Lit : `K8 Fault`
- Utilisé par : *(personne)*
- Ligne export : 73109 · id 203164

#### K9 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `K9 fuse is blown mc T`
- Ligne export : 73155 · id 203172

#### K9 fuse is blown mc T  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=Keybox error: FH9 fuse is blown
- Logique :
  - **Showing** = `K9 Fault`
- Lit : `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 73167 · id 203173

#### K10 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `K10 fuse is blown mc T`
- Ligne export : 73213 · id 203181

#### K10 fuse is blown mc T  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=Keybox error: FH10 fuse is blown
- Logique :
  - **Showing** = `K10 Fault`
- Lit : `K10 Fault`
- Utilisé par : *(personne)*
- Ligne export : 73225 · id 203182

#### K11 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `K11 fuse is blown mc T`
- Ligne export : 73271 · id 203190

#### K11 fuse is blown mc T  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=Keybox error: FH11 fuse is blown
- Logique :
  - **Showing** = `K11 Fault`
- Lit : `K11 Fault`
- Utilisé par : *(personne)*
- Ligne export : 73283 · id 203191

#### K12 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `K12 fuse is blown mc T`
- Ligne export : 73329 · id 203199

#### K12 fuse is blown mc T  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=Keybox error: FH12 fuse is blown
- Logique :
  - **Showing** = `K12 Fault`
- Lit : `K12 Fault`
- Utilisé par : *(personne)*
- Ligne export : 73341 · id 203200

#### K13 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `K13 fuse is blown mc T`
- Ligne export : 73387 · id 203208

#### K13 fuse is blown mc T  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=Keybox error: FH13 fuse is blown
- Logique :
  - **Showing** = `K13 Fault`
- Lit : `K13 Fault`
- Utilisé par : *(personne)*
- Ligne export : 73399 · id 203209

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=0x20C · Data length=8 · Send method=On change · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{T OFF_Bits_GOUT; 0}; {T ON_Bits_GOUT; 16}} · Module=Keybox X100 T (Generic) · Module index=0
- Lit : `T OFF_Bits_GOUT`, `T ON_Bits_GOUT`
- Utilisé par : *(personne)*
- Ligne export : 73445 · id 203275

## mc.Thermic / T.Oil security

#### T Oil Temp Mid/High  `FP`
> Oil temperature to ask a low speed Fan
- Propriétés : Unit=°C · Default mode={75}
- Utilisé par : `T Hydraulics Temperature State`, `Single adjust item: Oil Temp Mid/High`
- Ligne export : 58477 · id 192948

#### T Oil Temp Low/Mid  `FP`
- Propriétés : Unit=°C · Default mode={50}
- Utilisé par : `T Hydraulics Temperature State`, `Single adjust item: Oil Temp Low/Mid`
- Ligne export : 58489 · id 192949

#### T Oil Temp Critical  `FP`
- Propriétés : Unit=°C · Default mode={90}
- Utilisé par : `T ECC1_Oil_Temp`, `T Hydraulics Temperature State`, `Single adjust item: Oil Temp Critical`
- Ligne export : 58501 · id 192950

#### T Oil Temp Hysteresis  `FP`
- Propriétés : Unit=% · Default mode={0,9}
- Utilisé par : `T Hydraulics Temperature State`
- Ligne export : 58513 · id 192951

#### T Hydraulics Temperature State  `SMC`
> State machine for Oil temperature based on oil sensor Temp.
- Propriétés : Default state name=Off
- Fonction *Critical* :
  - **Activating** = `T Oil Temps mc 25/Current bilge C [°C] > T Oil Temp Critical [°C]`
  - **Blocking** = `T Oil Temps mc 25/Current bilge C [°C] < (T Oil Temp Hysteresis [%] * T Oil Temp Critical [°C])`
- Fonction *High* :
  - **Activating** = `T Oil Temps mc 25/Current bilge C [°C] > T Oil Temp Mid/High [°C]`
  - **Blocking** = `T Oil Temps mc 25/Current bilge C [°C] < (T Oil Temp Hysteresis [%] * T Oil Temp Mid/High [°C])`
- Fonction *Mid* :
  - **Activating** = `T Oil Temps mc 25/Current bilge C [°C] > T Oil Temp Low/Mid [°C]`
  - **Blocking** = `T Oil Temps mc 25/Current bilge C [°C] < (T Oil Temp Hysteresis [%] * T Oil Temp Low/Mid [°C])`
- Fonction *Low* :
  - **Activating** = `T Oil Temps mc 25/Current bilge C [°C] <= T Oil Temp Low/Mid [°C]`
- Lit : `T Oil Temp Critical`, `T Oil Temp Hysteresis`, `T Oil Temp Low/Mid`, `T Oil Temp Mid/High`, `T Oil Temps mc 25/Current bilge C`
- Utilisé par : `In T Hydraulics Temp State`
- Ligne export : 58525 · id 192952

## mc.Thermic / T.Oil security / pins oil — actif seulement si `not_a_sim`

#### T Hydraulic pump statut mc 26  `VIN`
- Propriétés : Unit=Bar · Reference voltage=Reference voltage A · Error value=0 · Calibration={500; 4500; 0; 30} · Alarms={No; 0; No; 100} · Module=MC42-33 (MC42[0]) · Module index=5
- Utilisé par : `T Wait Bad Pressure`, `MD4-5 page: BASE`
- Ligne export : 58735 · id 192909

#### T Check Pump  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `T Wait Bad Pressure`, `Single adjust item: Check Pump`
- Ligne export : 58759 · id 192910

#### T Wait Bad Pressure  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `(T Engine_Started mc) AND (T Hydraulic pump statut mc 26 [Bar] <= 10) AND (T Check Pump)`
- Lit : `T Check Pump`, `T Engine_Started mc`, `T Hydraulic pump statut mc 26`
- Utilisé par : `T Bad pressure mc`, `Event log: Thermic Events`, `MD4-5 page: BASE`, `Statistics log: Thermic Stats`
- Ligne export : 58772 · id 192911

#### T Bad pressure mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=e1141 Hydraulic pump lubrification failure · Text, English=Stop Engine Immediately. And contact your service center.
- Logique :
  - **Showing** = `T Wait Bad Pressure`
- Lit : `T Wait Bad Pressure`
- Utilisé par : *(personne)*
- Ligne export : 58831 · id 192921

#### T Wait Hot Temperature  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `(T Engine_Started mc) AND (T Oil Temps mc 25/Current bilge C [°C] >= 95)`
- Lit : `T Engine_Started mc`, `T Oil Temps mc 25/Current bilge C`
- Utilisé par : `T Hot Oil mc`
- Ligne export : 58877 · id 192930

#### T Hot Oil mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=e1185 Hydraulic Oil is to hot. · Text, English=Use the low speed. · Channel=T Oil Temps mc 25/Current bilge C [°C]
- Logique :
  - **Showing** = `T Wait Hot Temperature`
  - **Hiding** = `not(T Wait Hot Temperature)`
- Lit : `T Oil Temps mc 25/Current bilge C`, `T Wait Hot Temperature`
- Utilisé par : *(personne)*
- Ligne export : 58929 · id 192939

## mc.Thermic / T.Power

#### T Reset Startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `T Reset Startup`
- Utilisé par : `T Pre Fuel line ignition IDC`
- Ligne export : 55840 · id 192474

#### T Oil Security Activation  `IDC`
- Propriétés : Toggle=No · Delay on=60000 · Delay off=0
- Logique :
  - **Activating** = `Wait_Very_Low_Oil_Level`
- Lit : `Wait_Very_Low_Oil_Level`
- Utilisé par : `T Coupure Thermique avec sécurité`
- Ligne export : 55890 · id 192483

#### T MD3 STOP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `NegativeFlank(Screen_Start/Stop mc)`
- Lit : `Screen_Start/Stop mc`
- Utilisé par : `T Coupure Thermique avec sécurité`, `T MD3 start last checks`
- Ligne export : 55933 · id 192491

#### T Coupure Thermique avec sécurité  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T MD3 STOP) OR (T Oil Security Activation)`
- Lit : `T MD3 STOP`, `T Oil Security Activation`
- Utilisé par : `T Digit Engine On`
- Ligne export : 55977 · id 192499

#### T Fuel Line Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `T Fuel line ignition IDC`
  - **Resetting** = `(PositiveFlank(T Fuel line ignition IDC)) OR (not(T Pre Fuel line ignition IDC))`
- Lit : `T Fuel line ignition IDC`, `T Pre Fuel line ignition IDC`
- Utilisé par : `T Fuel line ignition Output`, `T Pre Fuel line ignition IDC`, `T Progress`
- Ligne export : 56027 · id 192508

#### T Fuel line ignition  `MEM`
- Propriétés : Input channel=T Fuel line ignition State · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `NegativeFlank(T Pre Fuel line ignition IDC)`
- Lit : `T Fuel line ignition State`, `T Pre Fuel line ignition IDC`
- Utilisé par : `T Pre Fuel line ignition IDC`
- Ligne export : 56095 · id 192520

#### T Starter Protection CMSG  `IMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Starter Temperature Protection · Text=Please check fuel level, battery level, oil level, fuel line, fuel filter. Do NOT start the engine more than 5 time per minute. You can start an fuel line ignition buy press RUN. · Left button=Ok · Center button=RUN
- Logique :
  - **Showing** = `T Starter Proctection IDC`
  - **Hiding** = `(2 = T Starter Protection CMSG) OR ((not(T Fuel line ignition IDC)) and (not(T Starter Proctection IDC))) OR (NegativeFlank(T Fuel line ignition IDC))`
- Lit : `T Fuel line ignition IDC`, `T Starter Proctection IDC`
- Utilisé par : `T Pre Fuel line ignition IDC`
- Ligne export : 56139 · id 192528

#### T Pre Fuel line ignition IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((1 = T Fuel line ignition))) OR (PositiveFlank((3 = T Starter Protection CMSG))) OR (T Pre Fuel line ignition IDC)`
  - **Blocking** = `(T Fuel Line Timer [s] > 50) OR (T Engine_Started mc) OR (T Reset Startup)`
- Lit : `T Engine_Started mc`, `T Fuel Line Timer`, `T Fuel line ignition`, `T Reset Startup`, `T Starter Protection CMSG`
- Utilisé par : `T Fuel Line Timer`, `T Fuel line ignition`, `T Fuel line ignition IDC`
- Ligne export : 56229 · id 192541

#### T Fuel line ignition IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Pre Fuel line ignition IDC`
  - **Blocking** = `T Engine_Started mc`
- Lit : `T Engine_Started mc`, `T Pre Fuel line ignition IDC`
- Utilisé par : `T Fuel Line Timer`, `T Fuel line ignition mc`, `T MD3 START`, `T Starter Protection CMSG`, `Event log: Thermic Events`
- Ligne export : 56329 · id 192556

#### T Fuel line ignition State  `SP`
- Propriétés : Input channel=None · Default state name=OFF · States={RUN}
- Utilisé par : `T Fuel line ignition`, `Single adjust item: Fuel line ignition State`
- Ligne export : 56379 · id 192565

#### T Starter Protection Slope  `SFC`
- Propriétés : Input channel=T Starter Protection [%] · Enable=Yes · Type=Slopes · Slopes={{10; 1}; {0; 0}}
- Lit : `T Starter Protection`
- Utilisé par : `T Starter Proctection IDC`
- Ligne export : 56391 · id 192567

#### T Starter Proctection IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Starter Protection Slope [%] >= 150`
- Lit : `T Starter Protection Slope`
- Utilisé par : `T Starter Protection CMSG`
- Ligne export : 56409 · id 192568

#### T Out START Engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T MD3 start last checks) OR (T Manual Start Engine Pulse IDC)`
  - **Blocking** = `not(port 12v on)`
- Lit : `T MD3 start last checks`, `T Manual Start Engine Pulse IDC`, `port 12v on`
- Utilisé par : `T Engine State mc`, `T K5 Engine Start`, `T Starter Protection`, `Statistics log: Thermic Stats`
- Ligne export : 56454 · id 192576

#### T Starter Protection  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `1000 * T Out START Engine`
- Lit : `T Out START Engine`
- Utilisé par : `T Starter Protection Slope`
- Ligne export : 56512 · id 192585

#### T MD3 start last checks  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T MD3 START) OR (T MD3 start last checks)`
  - **Blocking** = `(T Engine_Started mc) OR (T MD3 STOP) OR (PositiveFlank(T AutoStopafter 5 secondes)) OR (not(4ET Joystick Zero)) OR (not(port 12v on))`
- Lit : `4ET Joystick Zero`, `T AutoStopafter 5 secondes`, `T Engine_Started mc`, `T MD3 START`, `T MD3 STOP`, `port 12v on`
- Utilisé par : `T AutoStopafter 5 secondes`, `T Out START Engine`
- Ligne export : 56555 · id 192593

#### T AutoStopafter 5 secondes  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `T MD3 start last checks`
  - **Blocking** = `T Engine_Started mc`
- Lit : `T Engine_Started mc`, `T MD3 start last checks`
- Utilisé par : `T Digit Engine On`, `T MD3 start last checks`
- Ligne export : 56643 · id 192606

#### T MD3 START  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Screen_Start/Stop mc`
  - **Blocking** = `T Fuel line ignition IDC`
- Lit : `Screen_Start/Stop mc`, `T Fuel line ignition IDC`
- Utilisé par : `T Digit Engine On`, `T Joystick is not in neutral position`, `T MD3 start last checks`
- Ligne export : 56693 · id 192615

#### T Manual Start Engine  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `T Manual Start Engine Pulse IDC`, `Single adjust item: Manual Start Engine`
- Ligne export : 56743 · id 192624

#### T Manual Start Engine Pulse IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `PositiveFlank(T Manual Start Engine)`
- Lit : `T Manual Start Engine`
- Utilisé par : `T Out START Engine`
- Ligne export : 56756 · id 192625

#### T Progress  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `T Fuel Line Timer [s] * 2`
- Lit : `T Fuel Line Timer`
- Utilisé par : `T Fuel line ignition mc`
- Ligne export : 56800 · id 192633

#### T Fuel line ignition mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Message · Header, English=e1015 Fuel line ignition · Text, English=Please wait during fuel line ignition. (Engine need to be stop). · Channel=T Progress [%]
- Logique :
  - **Showing** = `PositiveFlank(T Fuel line ignition IDC)`
  - **Hiding** = `NegativeFlank(T Fuel line ignition IDC)`
- Lit : `T Fuel line ignition IDC`, `T Progress`
- Utilisé par : *(personne)*
- Ligne export : 56843 · id 192641

#### T ECU Engine on  `DP`
- Propriétés : True text=ON · False text=OFF · Default mode={False}
- Utilisé par : `T Inter Allumage Thermique`, `T Persistant Water Temp_1`, `Single adjust item: ECU Engine on`
- Ligne export : 56898 · id 192650

#### T Digit Engine On  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T Digit Engine On) OR (T MD3 START)`
  - **Blocking** = `(T Coupure Thermique avec sécurité) OR (PositiveFlank(T AutoStopafter 5 secondes)) OR (not(port 12v on))`
- Lit : `T AutoStopafter 5 secondes`, `T Coupure Thermique avec sécurité`, `T MD3 START`, `port 12v on`
- Utilisé par : `T Inter Allumage Thermique`
- Ligne export : 56911 · id 192651

#### T Fuel line ignition Output  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inside((T Fuel Line Timer [s] mod 10), 1, 9)`
- Lit : `T Fuel Line Timer`
- Utilisé par : `T Inter Allumage Thermique`
- Ligne export : 56984 · id 192662

#### T ECU Engine prime  `DP`
- Propriétés : True text=ON · False text=OFF · Default mode={False}
- Utilisé par : `ECU priming`, `T ECU prime timer`, `Single adjust item: ECU Engine priming`
- Ligne export : 57039 · id 212378

#### T ECU prime timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=10
- Logique :
  - **Decreasing** = `T ECU Engine prime`
  - **Resetting** = `T ECU prime timer [s] = 0`
- Lit : `T ECU Engine prime`
- Utilisé par : `ECU priming`
- Ligne export : 57052 · id 212367

#### ECU priming  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T ECU prime timer [s] > 6`
  - **Blocking** = `not(T ECU Engine prime)`
- Lit : `T ECU Engine prime`, `T ECU prime timer`
- Utilisé par : `T Inter Allumage Thermique`
- Ligne export : 57113 · id 212390

#### T Inter Allumage Thermique  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `((64 = 64) and T Digit Engine On) OR (T ECU Engine on) OR (T Fuel line ignition Output) OR (ECU priming)`
- Lit : `ECU priming`, `T Digit Engine On`, `T ECU Engine on`, `T Fuel line ignition Output`
- Utilisé par : `T Out SWITCH ON Engine`
- Ligne export : 57166 · id 192671

#### T Water °C Low  `FP`
- Propriétés : Unit=°C · Mode selector=T Engine type · Default mode: EB2 1.2L={70} · Mode 1: FORD 1.5L={70} · Mode 2: Kubo={70}
- Lit : `T Engine type`
- Utilisé par : `T Engine Temp State`, `T Exhaust Temp State hy test`, `Single adjust item: Water °C Low`
- Ligne export : 57248 · id 192683

#### in T Engine coolant temperature  `FGI`
- Propriétés : Unit=°C · Input type=Real · Input=T Engine coolant temp [°C] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Engine coolant temp`
- Utilisé par : `T Persistant Water Temp`, `T Persistant Water Temp_1`, `Voyant temp45`
- Ligne export : 57264 · id 192684

#### T Persistant Water Temp  `MEM`
> System memory used to keep Water temp after engine is turned off
- Propriétés : Input channel=in T Engine coolant temperature [°C] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `(in T Engine coolant temperature [°C] <> 0) AND (T Persistant Water Temp [°C] <> in T Engine coolant temperature [°C]) AND (T Engine_Started mc)`
- Lit : `T Engine_Started mc`, `in T Engine coolant temperature`
- Utilisé par : `T ECC1_Engine_Temp`, `T Engine Temp State`, `T Engine Thermal State`, `T SPEED Engine`, `T Speed Pump`, `T State All Speed`, `MD4-5 page: BASE`
- Ligne export : 57278 · id 192685

#### T Water °C High  `FP`
- Propriétés : Unit=°C · Mode selector=T Engine type · Default mode: EB2 1.2L={91} · Mode 1: FORD 1.5L={90} · Mode 2: Kubo={91}
- Lit : `T Engine type`
- Utilisé par : `T Engine Temp State`, `T Exhaust Temp State hy test`, `Voyant temp45`, `Single adjust item: Water °C High`
- Ligne export : 57340 · id 192695

#### T Ambiante Temperature  `SP`
- Propriétés : Input channel=None · Default state name=Normal · States={High}
- Utilisé par : `T Timer Fan Critical`, `T Timer Fan Hot`, `T Timer Fan Low`, `T Timer Fan Mild`, `Single adjust item: Ambiante Temperature`
- Ligne export : 57356 · id 192696

#### T Timer Fan Hot  `FP`
- Propriétés : Unit=s · Mode selector=T Ambiante Temperature · Default mode: Normal={180} · Mode 1: High={270}
- Lit : `T Ambiante Temperature`
- Utilisé par : `T High Temp Timer`, `Single adjust item: Timer Fan Hot`
- Ligne export : 57368 · id 192698

#### T High Temp Timer  `TMR`
> Timer triggered at the engine stop to Allow Full Fan if system temperature is still Hot
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=T Timer Fan Hot [s]
- Logique :
  - **Decreasing** = `T High Temp Timer [s] > 0`
  - **Resetting** = `T Engine_Started mc`
- Lit : `T Engine_Started mc`, `T Timer Fan Hot`
- Utilisé par : `T Engine Thermal State`
- Ligne export : 57382 · id 192699

#### T Timer Fan Mild  `FP`
- Propriétés : Unit=s · Mode selector=T Ambiante Temperature · Default mode: Normal={60} · Mode 1: High={120}
- Lit : `T Ambiante Temperature`
- Utilisé par : `T Mid Temp Timer`, `Single adjust item: Timer Fan Mild`
- Ligne export : 57443 · id 192710

#### T Mid Temp Timer  `TMR`
> Timer triggered at the engine stop to maintain system temp at Mid
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=T Timer Fan Mild [s]
- Logique :
  - **Decreasing** = `T Mid Temp Timer [s] > 0`
  - **Resetting** = `T Engine_Started mc`
- Lit : `T Engine_Started mc`, `T Timer Fan Mild`
- Utilisé par : `T Engine Thermal State`
- Ligne export : 57457 · id 192711

#### T Timer Fan Low  `FP`
- Propriétés : Unit=s · Mode selector=T Ambiante Temperature · Default mode: Normal={40} · Mode 1: High={80}
- Lit : `T Ambiante Temperature`
- Utilisé par : `T Low Temp Timer`, `Single adjust item: Timer Fan Low`
- Ligne export : 57518 · id 192722

#### T Low Temp Timer  `TMR`
> Timer triggered at the engine stop to maintain system temp at Low
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=T Timer Fan Low [s]
- Logique :
  - **Decreasing** = `T Low Temp Timer [s] > 0`
  - **Resetting** = `T Engine_Started mc`
- Lit : `T Engine_Started mc`, `T Timer Fan Low`
- Utilisé par : `T Engine Thermal State`
- Ligne export : 57532 · id 192723

#### T Water °C Critical  `FP`
- Propriétés : Unit=°C · Mode selector=T Engine type · Default mode: EB2 1.2L={94} · Mode 1: FORD 1.5L={97} · Mode 2: Kubo={94}
- Lit : `T Engine type`
- Utilisé par : `T ECC1_Engine_Temp`, `T Engine Temp State`, `T Exhaust Temp State hy test`, `Voyant temp45`, `Single adjust item: Water °C Critical`
- Ligne export : 57593 · id 192734

#### T Timer Fan Critical  `FP`
- Propriétés : Unit=s · Mode selector=T Ambiante Temperature · Default mode: Normal={270} · Mode 1: High={540}
- Lit : `T Ambiante Temperature`
- Utilisé par : `T Critical Temp Timer`, `Single adjust item: Timer Fan Critical`
- Ligne export : 57609 · id 192763

#### T Critical Temp Timer  `TMR`
> Timer triggered at the engine stop to Maintain critical state during a period of time
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=T Timer Fan Critical [s]
- Logique :
  - **Decreasing** = `T Critical Temp Timer [s] > 0`
  - **Resetting** = `T Engine_Started mc`
- Lit : `T Engine_Started mc`, `T Timer Fan Critical`
- Utilisé par : `T Engine Thermal State`, `T Temperature State`
- Ligne export : 57623 · id 192735

#### T Out SWITCH ON Engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Inter Allumage Thermique`
  - **Blocking** = `not(port 12v on)`
- Lit : `T Inter Allumage Thermique`, `port 12v on`
- Utilisé par : `T K4 Engine Power / Search Lights`
- Ligne export : 57684 · id 192746

#### T Joystick is not in neutral position  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header, English=e1093 Neutral position · Text, English=Please put jostick in neutral position before start engine.
- Logique :
  - **Showing** = `(not(4ET Joystick Zero)) AND (PositiveFlank(T MD3 START))`
- Lit : `4ET Joystick Zero`, `T MD3 START`
- Utilisé par : *(personne)*
- Ligne export : 57735 · id 192754

#### T Water Temp Hysteresis Gap  `FP`
- Propriétés : Unit=°C · Default mode={5}
- Utilisé par : `T Engine Temp State`, `T Exhaust Temp State hy test`, `Voyant temp45`
- Ligne export : 57790 · id 192781

#### T inExhaust temp  `FGI`
- Propriétés : Unit=°C · Input type=Real · Input=out T Exhaust Temps · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `out T Exhaust Temps`
- Utilisé par : `T Exhaust Temp State hy test`
- Ligne export : 57802 · id 198595

#### T Engine Temp State  `SMC`
- Propriétés : Default state name=Off
- Fonction *Critical* :
  ```qcode
  static outputValue:= False
  
  If T Persistant Water Temp >= T Water °C Critical then
    outputValue := True  //switch on
  elseif T Persistant Water Temp < (T Water °C Critical - T Water Temp Hysteresis Gap ) then
    outputValue := False  //switch off
  endif
  
  Result := OutputValue
  ```
- Fonction *High* :
  ```qcode
  static outputValue:= False
  
  If T Persistant Water Temp >= T Water °C High then
    outputValue := True  //switch on
  elseif T Persistant Water Temp < (T Water °C High - T Water Temp Hysteresis Gap ) then
    outputValue := False  //switch off
  endif
  
  Result := OutputValue
  ```
- Fonction *Mid* :
  ```qcode
  static outputValue:= False
  
  If T Persistant Water Temp >= T Water °C Low then
    outputValue := True  //switch on
  elseif T Persistant Water Temp < (T Water °C Low - T Water Temp Hysteresis Gap ) then
    outputValue := False  //switch off
  endif
  
  Result := OutputValue
  ```
- Fonction *Low* :
  ```qcode
  static outputValue:= False
  
  If T Persistant Water Temp < T Water °C Low then
    outputValue := True  //switch on
  endif
  
  Result := OutputValue
  ```
- Lit : `T Persistant Water Temp`, `T Water Temp Hysteresis Gap`, `T Water °C Critical`, `T Water °C High`, `T Water °C Low`
- Utilisé par : `T Engine Thermal State`, `Event log: Thermic Events`
- Ligne export : 57816 · id 192782

#### T Engine Thermal State  `SMC`
- Propriétés : Default state name=Off
- Fonction *Critical* :
  - **Activating** = `T Engine Temp State = 1`
  - **Blocking** = `T Critical Temp Timer [s] <= 0`
- Fonction *High* :
  - **Activating** = `T Engine Temp State = 2`
  - **Blocking** = `T High Temp Timer [s] <= 0`
- Fonction *Mid* :
  - **Activating** = `T Engine Temp State = 3`
  - **Blocking** = `T Mid Temp Timer [s] <= 0`
- Fonction *Low* :
  - **Activating** = `(T Engine Temp State = 4) AND (T Low Temp Timer [s] > 0)`
  - **Blocking** = `T Persistant Water Temp [°C] = 0`
- Lit : `T Critical Temp Timer`, `T Engine Temp State`, `T High Temp Timer`, `T Low Temp Timer`, `T Mid Temp Timer`, `T Persistant Water Temp`
- Utilisé par : `In T Engine Thermal State`
- Ligne export : 57889 · id 192837

#### T Exhaust Temp State hy test  `SMC`
- Propriétés : Default state name=Off
- Fonction *Critical* :
  ```qcode
  static outputValue:= False
  
  If T inExhaust temp >= T Water °C Critical then
    outputValue := True  //switch on
  elseif T inExhaust temp < (T Water °C Critical - T Water Temp Hysteresis Gap ) then
    outputValue := False  //switch off
  endif
  
  Result := OutputValue
  ```
- Fonction *High* :
  ```qcode
  static outputValue:= False
  
  If T inExhaust temp >= T Water °C High then
    outputValue := True  //switch on
  elseif T inExhaust temp < (T Water °C High - T Water Temp Hysteresis Gap ) then
    outputValue := False  //switch off
  endif
  
  Result := OutputValue
  ```
- Fonction *Mid* :
  ```qcode
  static outputValue:= False
  
  If T inExhaust temp >= T Water °C Low then
    outputValue := True  //switch on
  elseif T inExhaust temp < (T Water °C Low - T Water Temp Hysteresis Gap ) then
    outputValue := False  //switch off
  endif
  
  Result := OutputValue
  ```
- Lit : `T Water Temp Hysteresis Gap`, `T Water °C Critical`, `T Water °C High`, `T Water °C Low`, `T inExhaust temp`
- Utilisé par : `In T Exhaust Temp State`
- Ligne export : 58075 · id 192862

#### T Water °C Critical Critical  `FP`
- Propriétés : Unit=°C · Mode selector=T Engine type · Default mode: EB2 1.2L={97} · Mode 1: FORD 1.5L={101} · Mode 2: Kubo={97}
- Lit : `T Engine type`
- Utilisé par : `T SPEED Engine`, `T Speed Pump`, `T State All Speed`, `Single adjust item: Water °C Critical Critical`
- Ligne export : 58134 · id 205821

#### port 12v on  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(T Force 12v port sensor on) OR (T V sensor port [V] > 9)`
- Lit : `T Force 12v port sensor on`, `T V sensor port`
- Utilisé par : `T Digit Engine On`, `T MD3 start last checks`, `T Out START Engine`, `T Out SWITCH ON Engine`, `T Port winter switch is off`
- Ligne export : 58150 · id 232514

#### T Port winter switch is off  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header, English=Port engine battery switch is off · Text, English=Port battery switch is off or the battery too low. Please turn it on to be able to start the inboard engine
- Logique :
  - **Showing** = `(not(port 12v on)) AND (PositiveFlank(Screen_Start/Stop mc))`
- Lit : `Screen_Start/Stop mc`, `port 12v on`
- Utilisé par : *(personne)*
- Ligne export : 58202 · id 232519

#### T Force 12v port sensor on  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `port 12v on`, `Adjust group: Master Features`, `Single adjust item: T Force 12v port sensor on`
- Ligne export : 58257 · id 232532

#### T V sensor port  `VIN32`
- Propriétés : Unit=V · Error value=0 · Calibration={0; 20000; 0; 20} · Alarms={No; 0; No; 100} · Module=MC42-33 (MC42[0]) · Module index=1
- Utilisé par : `port 12v on`
- Ligne export : 58270 · id 232539

#### T Persistant Water Temp_1  `MEM`
> System memory used to keep Water temp after engine is turned off
- Propriétés : Input channel=in T Engine coolant temperature [°C] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `(in T Engine coolant temperature [°C] <> 0) AND (T Persistant Water Temp_1 [°C] <> in T Engine coolant temperature [°C]) AND (T Engine_Started mc or T ECU Engine on)`
- Lit : `T ECU Engine on`, `T Engine_Started mc`, `in T Engine coolant temperature`
- Utilisé par : `MD4-5 page: INFO`
- Ligne export : 58292 · id 232950

#### Voyant temp45  `SMC`
> Cette machine d'état permet d'être en état HIGH ou CRITICALen fonction de "T water". liétat HIGH est atteint 2 degrés après la Twater high et l'état crtical est atteint 2 degrés après le Twater critical. permet de décaler l'allumage du voyant temp45 de 2 degrés
- Propriétés : Default state name=OFF
- Fonction *HIGH* :
  ```qcode
  static outputValue:= False
  
  if in T Engine coolant temperature >= ( T Water °C High + Decalage degrés ) Then
    outputValue := True  //switch on
  endif
  if in T Engine coolant temperature >= T Water °C Critical + Decalage degrés then
    outputValue := False
  elseif in T Engine coolant temperature < ( T Water °C High + Decalage degrés - T Water Temp Hysteresis Gap ) then
    outputValue := False  //switch off
  endif
  
  Result := OutputValue
  ```
- Fonction *CRITICAL* :
  ```qcode
  static outputValue1:= False
  
  If in T Engine coolant temperature >= T Water °C Critical + Decalage degrés then
    outputValue1 := True  //switch on
  elseif in T Engine coolant temperature < (T Water °C Critical + Decalage degrés - T Water Temp Hysteresis Gap ) then
    outputValue1 := False  //switch off
  endif
  
  Result := outputValue1
  ```
- Lit : `Decalage degrés`, `T Water Temp Hysteresis Gap`, `T Water °C Critical`, `T Water °C High`, `in T Engine coolant temperature`
- Utilisé par : `T Alert critical engine mc`, `Event log: Thermic Events`, `MD4-5 page: MAIN Thermic`
- Ligne export : 58356 · id 236483

#### Decalage degrés  `IP`
- Propriétés : Default mode={2}
- Utilisé par : `Voyant temp45`
- Ligne export : 58400 · id 236490

#### T Alert critical engine mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=e1100 Stop · Text, English=Engine temparture critical. Derating power
- Logique :
  - **Showing** = `Voyant temp45 = 2`
- Lit : `Voyant temp45`
- Utilisé par : *(personne)*
- Ligne export : 58412 · id 236621

## mc.Thermic / T.Pump

#### T Step change  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `T Punp 1 - Current`, `T Punp 1 - Current`, `T Punp 2 - Current`, `T Punp 2 - Current`
- Ligne export : 60783 · id 193350

#### T Forward - direct corrector  `FP`
- Propriétés : Unit=% · Mode selector=T Speed Pump · Default mode: Slow={0} · Mode 1: Super Slow={0} · Mode 2: Fast Speed={0}
- Lit : `T Speed Pump`
- Utilisé par : `T Punp 1 - Current`, `T Punp 2 - Current`, `Single adjust item: Forward - direct corrector`
- Ligne export : 60795 · id 193351

#### In T Curent - Low Speed  `FGI`
- Propriétés : Unit=mA · Input type=Real · Input=T Pump Curent - Low Speed [mA] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Pump Curent - Low Speed`
- Utilisé par : `T Backward Curent`, `T Forward Curent`
- Ligne export : 60811 · id 193352

#### In T Curent - Super Low Speed  `FGI`
- Propriétés : Unit=mA · Input type=Real · Input=T Pump Curent - Super Low Speed [mA] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Pump Curent - Super Low Speed`
- Utilisé par : `T Backward Curent`, `T Forward Curent`
- Ligne export : 60825 · id 193353

#### In T Curent  - Hight Speed  `FGI`
- Propriétés : Unit=mA · Input type=Real · Input=T Pump Curent  - Hight Speed [mA] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Pump Curent  - Hight Speed`
- Utilisé par : `T Backward Curent`, `T Forward Curent`
- Ligne export : 60839 · id 193354

#### T Forward Curent  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed · Function selector=T Speed Pump
- Fonction *Slow* :
  - **Controlling** = `In T Curent - Low Speed [mA]`
- Fonction *Super Slow* :
  - **Controlling** = `In T Curent - Super Low Speed [mA]`
- Fonction *Fast Speed* :
  - **Controlling** = `In T Curent  - Hight Speed [mA]`
- Lit : `In T Curent  - Hight Speed`, `In T Curent - Low Speed`, `In T Curent - Super Low Speed`, `T Speed Pump`
- Utilisé par : `T Punp 1 - Current`, `T Punp 2 - Current`
- Ligne export : 60853 · id 193355

#### In T Max curent  `FGI`
- Propriétés : Unit=mA · Input type=Real · Input=T Pump Max curent [mA] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Pump Max curent`
- Utilisé par : `T Punp 1 - Current`, `T Punp 1 - Current`, `T Punp 2 - Current`, `T Punp 2 - Current`
- Ligne export : 60957 · id 193363

#### T Punp 1 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `T Forward Curent [mA] - (T Forward - direct corrector [%] *% T Step change [mA])`
  - **Limiting** = `In T Max curent [mA]`
- Lit : `In T Max curent`, `T Forward - direct corrector`, `T Forward Curent`, `T Step change`
- Utilisé par : `T Filter pump 1 Neg`, `T Filter pump 1 Pos`
- Ligne export : 60971 · id 193364

#### T coeff pente ?  `FP`
- Propriétés : Unit=mA/s · Default mode={200}
- Utilisé par : `T Filter pump 1 Neg`, `T Filter pump 1 Pos`, `T Filter pump 2 Neg`, `T Filter pump 2 Pos`
- Ligne export : 61031 · id 193374

#### T Filter pump 1 Pos  `SFC`
- Propriétés : Input channel=T Punp 1 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{T coeff pente ? [mA/s]; T coeff pente ? [mA/s]}; {T coeff pente ? [mA/s]; T coeff pente ? [mA/s]}}
- Lit : `T Punp 1 - Current`, `T coeff pente ?`
- Utilisé par : `T Pump 1 Right mc 15`
- Ligne export : 61043 · id 193375

#### T Punp 2 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `T Forward Curent [mA] + (T Forward - direct corrector [%] *% T Step change [mA])`
  - **Limiting** = `In T Max curent [mA]`
- Lit : `In T Max curent`, `T Forward - direct corrector`, `T Forward Curent`, `T Step change`
- Utilisé par : `T Filter pump 2 Neg`, `T Filter pump 2 Pos`
- Ligne export : 61061 · id 193377

#### T Filter pump 2 Pos  `SFC`
- Propriétés : Input channel=T Punp 2 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{T coeff pente ? [mA/s]; T coeff pente ? [mA/s]}; {T coeff pente ? [mA/s]; T coeff pente ? [mA/s]}}
- Lit : `T Punp 2 - Current`, `T coeff pente ?`
- Utilisé par : `T Pump 2 Left mc 14`
- Ligne export : 61121 · id 193387

#### T Backward - direct corrector  `FP`
- Propriétés : Unit=% · Mode selector=T Speed Pump · Default mode: Slow={0} · Mode 1: Super Slow={0} · Mode 2: Fast Speed={0}
- Lit : `T Speed Pump`
- Utilisé par : `T Punp 1 - Current`, `T Punp 2 - Current`, `Single adjust item: Backward - direct corrector`
- Ligne export : 61139 · id 193389

#### T Backward Curent  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed · Function selector=T Speed Pump
- Fonction *Slow* :
  - **Controlling** = `In T Curent - Low Speed [mA]`
- Fonction *Super Slow* :
  - **Controlling** = `In T Curent - Super Low Speed [mA]`
- Fonction *Fast Speed* :
  - **Controlling** = `In T Curent  - Hight Speed [mA]`
- Lit : `In T Curent  - Hight Speed`, `In T Curent - Low Speed`, `In T Curent - Super Low Speed`, `T Speed Pump`
- Utilisé par : `T Punp 1 - Current`, `T Punp 2 - Current`
- Ligne export : 61155 · id 193390

#### T Punp 2 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `T Backward Curent [mA] + (T Backward - direct corrector [%] *% T Step change [mA])`
  - **Limiting** = `In T Max curent [mA]`
- Lit : `In T Max curent`, `T Backward - direct corrector`, `T Backward Curent`, `T Step change`
- Utilisé par : `T Filter pump 2 Neg`, `T Filter pump 2 Pos`
- Ligne export : 61259 · id 193398

#### T Filter pump 2 Neg  `SFC`
- Propriétés : Input channel=T Punp 2 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{T coeff pente ? [mA/s]; T coeff pente ? [mA/s]}; {T coeff pente ? [mA/s]; T coeff pente ? [mA/s]}}
- Lit : `T Punp 2 - Current`, `T coeff pente ?`
- Utilisé par : `T Pump 2 Left mc 14`
- Ligne export : 61319 · id 193408

#### T Pump 2 Left Filter ECC1  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `T Left Filter [%] * T ECC1 Integrating [%]`
- Lit : `T ECC1 Integrating`, `T Left Filter`
- Utilisé par : `T Pump 2 Left mc 14`
- Ligne export : 61337 · id 193409

#### T Pump 1 Right Filter ECC1  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `T Right Filter [%] * T ECC1 Integrating [%]`
- Lit : `T ECC1 Integrating`, `T Right Filter`
- Utilisé par : `T Pump 1 Right mc 15`
- Ligne export : 61389 · id 193419

#### T Punp 1 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `T Backward Curent [mA] - (T Backward - direct corrector [%] *% T Step change [mA])`
  - **Limiting** = `In T Max curent [mA]`
- Lit : `In T Max curent`, `T Backward - direct corrector`, `T Backward Curent`, `T Step change`
- Utilisé par : `T Filter pump 1 Neg`, `T Filter pump 1 Pos`
- Ligne export : 61441 · id 193430

#### T Filter pump 1 Neg  `SFC`
- Propriétés : Input channel=T Punp 1 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{T coeff pente ? [mA/s]; T coeff pente ? [mA/s]}; {T coeff pente ? [mA/s]; T coeff pente ? [mA/s]}}
- Lit : `T Punp 1 - Current`, `T coeff pente ?`
- Utilisé par : `T Pump 1 Right mc 15`
- Ligne export : 61501 · id 193440

#### T Brake Slope  `IP`
- Propriétés : Unit=ms · Mode selector=T Speed Pump · Default mode: Slow={750} · Mode 1: Super Slow={1000} · Mode 2: Fast Speed={4000}
- Lit : `T Speed Pump`
- Utilisé par : `T Inter EV Frein`
- Ligne export : 61519 · id 193443

#### T Inter EV Frein  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=T Brake Slope [ms]
- Logique :
  - **Activating** = `(T Brake Activation) OR (bypsass brake T)`
  - **Blocking** = `not(T Engine_Started mc)`
- Lit : `T Brake Activation`, `T Brake Slope`, `T Engine_Started mc`, `bypsass brake T`
- Utilisé par : `Brake T/ Batt HT reset / tyva on SEL qcode`
- Ligne export : 61535 · id 193444

#### bypsass brake T  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `T Inter EV Frein`, `Adjust group: Master Features`, `Single adjust item: bypsass brake T`
- Ligne export : 61721 · id 229233

## mc.Thermic / T.Pump / pins thermic — actif seulement si `not_a_sim`

#### T Min current Right Backward  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `T Pump 1 Right mc 15`, `Single adjust item: Min current Right Backward`
- Ligne export : 61608 · id 193349

#### T Min current Left Backward  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `T Pump 2 Left mc 14`, `Single adjust item: Min current Left Backward`
- Ligne export : 61620 · id 193376

#### T Min current Left Fordward  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `T Pump 2 Left mc 14`, `Single adjust item: Min current Left Fordward`
- Ligne export : 61632 · id 193388

#### T Min current Right Fordward  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `T Pump 1 Right mc 15`, `Single adjust item: Min current Right Fordward`
- Ligne export : 61644 · id 193429

#### T Pump 1 Right mc 15  `COUT`
- Propriétés : Bidirectional=Yes · BWL=0 · Input channel=T Pump 1 Right Filter ECC1 [%] · Default mode={{T Min current Right Fordward [mA]; T Filter pump 1 Pos [mA]; 0; 0}; {T Min current Right Backward [mA]; T Filter pump 1 Neg [mA]; 0; 0}} · Module=MC42-33 (MC42[0]) · Module index=1
- Lit : `T Filter pump 1 Neg`, `T Filter pump 1 Pos`, `T Min current Right Backward`, `T Min current Right Fordward`, `T Pump 1 Right Filter ECC1`
- Utilisé par : `MD4-5 page: BASE`, `MD4-5 page: INFO`
- Ligne export : 61656 · id 193441

#### T Pump 2 Left mc 14  `COUT`
- Propriétés : Bidirectional=Yes · BWL=0 · Input channel=T Pump 2 Left Filter ECC1 [%] · Default mode={{T Min current Left Fordward [mA]; T Filter pump 2 Pos [mA]; 0; 0}; {T Min current Left Backward [mA]; T Filter pump 2 Neg [mA]; 0; 0}} · Module=MC42-33 (MC42[0]) · Module index=0
- Lit : `T Filter pump 2 Neg`, `T Filter pump 2 Pos`, `T Min current Left Backward`, `T Min current Left Fordward`, `T Pump 2 Left Filter ECC1`
- Utilisé par : `MD4-5 page: BASE`, `MD4-5 page: INFO`
- Ligne export : 61682 · id 193442

## mc.Thermic / T.SAEJ Std engine input

#### in T Engine coolant temperature  `FGI`
- Propriétés : Unit=°C · Input type=Real · Input=T Engine coolant temp [°C] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Engine coolant temp`
- Utilisé par : *(personne)*
- Ligne export : 59003 · id 192979

#### T Para enclench voyant pression huile  `FP`
- Propriétés : Unit=kPa · Mode selector=T Engine type · Default mode: EB2 1.2L={50} · Mode 1: FORD 1.5L={300} · Mode 2: Kubo={50}
- Lit : `T Engine type`
- Utilisé par : *(personne)*
- Ligne export : 59017 · id 192980

#### T Voyant Pression Huile Moteur  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Utilisé par : `T Oil pressure mc T`, `Event log: Thermic Events`, `MD4-5 page: MAIN Thermic`
- Ligne export : 59033 · id 192982

#### T FP - Start réduction  `FP`
- Propriétés : Unit=% · Default mode={85}
- Utilisé par : `T ECC1_Power`, `Adjust group: Master Thermic`, `Single adjust item: T FP - Start réduction`
- Ligne export : 59069 · id 192991

#### T FP - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={20}
- Utilisé par : `T ECC1_Power`, `Adjust group: Master Thermic`, `Single adjust item: T FP - Incres Speed`
- Ligne export : 59081 · id 192992

#### T FP - Max Error  `FP`
- Propriétés : Unit=% · Default mode={10}
- Utilisé par : `T ECC1_Power`, `Adjust group: Master Thermic`, `Single adjust item: T FP - Max Error`
- Ligne export : 59093 · id 192993

#### T FP - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={80}
- Utilisé par : `T ECC1_Power`, `Adjust group: Master Thermic`, `Single adjust item: T FP - Decres Speed`
- Ligne export : 59105 · id 192994

#### in T % load at current speed  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=T % load at current speed [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T % load at current speed`
- Utilisé par : `T ECC1_Power`
- Ligne export : 59117 · id 192995

#### T ECC1_Power  `ILC`
- Propriétés : Output=Normal · Enable=T Engine_Started mc · Input channel=in T % load at current speed [%] · Start reduction at=T FP - Start réduction [%] · Max error=T FP - Max Error [%] · Max increase speed=T FP - Incres Speed [%/s] · Max decrease speed=T FP - Decres Speed [%/s]
- Lit : `T Engine_Started mc`, `T FP - Decres Speed`, `T FP - Incres Speed`, `T FP - Max Error`, `T FP - Start réduction`, `in T % load at current speed`
- Utilisé par : `T ECC1 Integrating`
- Ligne export : 59131 · id 192996

#### T FT - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={50}
- Utilisé par : `T ECC1_Engine_Temp`, `Adjust group: Master Thermic`, `Single adjust item: T FT - Incres Speed`
- Ligne export : 59146 · id 192997

#### T FT - Max Error  `FP`
- Propriétés : Unit=°C · Default mode={5}
- Utilisé par : `T ECC1_Engine_Temp`, `Adjust group: Master Thermic`, `Single adjust item: T FT - Max Error`
- Ligne export : 59158 · id 192998

#### T FT - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={0,6}
- Utilisé par : `T ECC1_Engine_Temp`, `Adjust group: Master Thermic`, `Single adjust item: T FT - Decres Speed`
- Ligne export : 59170 · id 192999

#### T ECC1_Engine_Temp  `ILC`
- Propriétés : Output=Normal · Enable=T Engine_Started mc · Input channel=T Persistant Water Temp [°C] · Start reduction at=T Water °C Critical [°C] · Max error=T FT - Max Error [°C] · Max increase speed=T FT - Incres Speed [%/s] · Max decrease speed=T FT - Decres Speed [%/s]
- Lit : `T Engine_Started mc`, `T FT - Decres Speed`, `T FT - Incres Speed`, `T FT - Max Error`, `T Persistant Water Temp`, `T Water °C Critical`
- Utilisé par : `T ECC1 Integrating`
- Ligne export : 59182 · id 193000

#### T FO - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={50}
- Utilisé par : `T ECC1_Oil_Temp`, `Adjust group: Master Thermic`, `Single adjust item: T FO - Incres Speed`
- Ligne export : 59197 · id 193001

#### T FO - Max Error  `FP`
- Propriétés : Unit=°C · Default mode={10}
- Utilisé par : `T ECC1_Oil_Temp`, `Adjust group: Master Thermic`, `Single adjust item: T FO - Max Error`
- Ligne export : 59209 · id 193002

#### T FO - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={1}
- Utilisé par : `T ECC1_Oil_Temp`, `Adjust group: Master Thermic`, `Single adjust item: T FO - Decres Speed`
- Ligne export : 59221 · id 193003

#### T ECC1_Oil_Temp  `ILC`
- Propriétés : Output=Normal · Enable=T Engine_Started mc · Input channel=T Oil Temps mc 25/Current bilge C [°C] · Start reduction at=T Oil Temp Critical [°C] · Max error=T FO - Max Error [°C] · Max increase speed=T FO - Incres Speed [%/s] · Max decrease speed=T FO - Decres Speed [%/s]
- Lit : `T Engine_Started mc`, `T FO - Decres Speed`, `T FO - Incres Speed`, `T FO - Max Error`, `T Oil Temp Critical`, `T Oil Temps mc 25/Current bilge C`
- Utilisé par : `T ECC1 Integrating`
- Ligne export : 59233 · id 193004

#### T FS - Start réduction  `FP`
- Propriétés : Unit=% · Mode selector=T Engine type · Default mode: EB2 1.2L={100} · Mode 1: FORD 1.5L={30} · Mode 2: Kubo={100}
- Lit : `T Engine type`
- Utilisé par : `T ECC1_Speed`, `Adjust group: Master Thermic`, `Single adjust item: T FS - Start réduction`
- Ligne export : 59248 · id 193005

#### T FS - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={20}
- Utilisé par : `T ECC1_Speed`, `Adjust group: Master Thermic`, `Single adjust item: T FS - Incres Speed`
- Ligne export : 59264 · id 193006

#### T FS - Max Error  `FP`
- Propriétés : Unit=% · Default mode={10}
- Utilisé par : `T ECC1_Speed`, `Adjust group: Master Thermic`, `Single adjust item: T FS - Max Error`
- Ligne export : 59276 · id 193007

#### T FS - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={80}
- Utilisé par : `T ECC1_Speed`, `Adjust group: Master Thermic`, `Single adjust item: T FS - Decres Speed`
- Ligne export : 59288 · id 193008

#### in T Speed Error Calc  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=T Speed Error Calcul [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `T Speed Error Calcul`
- Utilisé par : `T ECC1_Speed`
- Ligne export : 59300 · id 193009

#### T ECC1_Speed  `ILC`
- Propriétés : Output=Normal · Enable=T Engine_Started mc · Input channel=in T Speed Error Calc [%] · Start reduction at=T FS - Start réduction [%] · Max error=T FS - Max Error [%] · Max increase speed=T FS - Incres Speed [%/s] · Max decrease speed=T FS - Decres Speed [%/s]
- Lit : `T Engine_Started mc`, `T FS - Decres Speed`, `T FS - Incres Speed`, `T FS - Max Error`, `T FS - Start réduction`, `in T Speed Error Calc`
- Utilisé par : `T ECC1 Integrating`
- Ligne export : 59314 · id 193010

#### T ECC1 Integrating  `MAC`
- Propriétés : Unit=%
- Logique :
  ```qcode
  Result := (T ECC1_Engine_Temp/100) * (T ECC1_Power/100) * (T ECC1_Oil_Temp/100) * (T ECC1_Speed/100)
  ```
- Lit : `T ECC1_Engine_Temp`, `T ECC1_Oil_Temp`, `T ECC1_Power`, `T ECC1_Speed`
- Utilisé par : `T Pump 1 Right Filter ECC1`, `T Pump 2 Left Filter ECC1`
- Ligne export : 59329 · id 193011

#### T Oil pressure mc T  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=e1145 Inboard engine low oil · Text, English=Stop Engine Immediately, let cool down. Check engine oil level. And contact your service center. Oil type : 10W40.
- Logique :
  - **Showing** = `T Voyant Pression Huile Moteur`
  - **Hiding** = `not(T Voyant Pression Huile Moteur)`
- Lit : `T Voyant Pression Huile Moteur`
- Utilisé par : *(personne)*
- Ligne export : 59347 · id 193027

#### FXs Display  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Adjust group: Master Thermic`, `Single adjust item: FXs Display`, `Single adjust item: T FO - Decres Speed`, `Single adjust item: T FO - Incres Speed`, `Single adjust item: T FO - Max Error`, `Single adjust item: T FP - Decres Speed`, `Single adjust item: T FP - Incres Speed`, `Single adjust item: T FP - Max Error`, `Single adjust item: T FP - Start réduction`, `Single adjust item: T FS - Decres Speed`, `Single adjust item: T FS - Incres Speed`, `Single adjust item: T FS - Max Error`, `Single adjust item: T FS - Start réduction`, `Single adjust item: T FT - Decres Speed`, `Single adjust item: T FT - Incres Speed`, `Single adjust item: T FT - Max Error`
- Ligne export : 59414 · id 207931

## mc.Thermic / T.Thermal Management
> Thermal management of the system, to pilot fans and advise user.

#### In T Hydraulics Temp State  `FGI`
- Propriétés : Input type=State · Input=T Hydraulics Temperature State · Default state name=Off · States={Critical; High; Mid; Low}
- Lit : `State`, `T Hydraulics Temperature State`
- Utilisé par : `T Activate Critical State`, `T Alert critical hydraulic mc`, `T Temperature State`
- Ligne export : 65748 · id 193748

#### In T Engine Thermal State  `FGI`
- Propriétés : Input type=State · Input=T Engine Thermal State · Default state name=Off · States={Critical; High; Mid; Low}
- Lit : `State`, `T Engine Thermal State`
- Utilisé par : `T Activate Critical State`, `T Temperature State`
- Ligne export : 65764 · id 193753

#### In T Exhaust Temp State  `FGI`
- Propriétés : Input type=State · Input=T Exhaust Temp State hy test · Default state name=Low off · States={Critical; High; Mid}
- Lit : `State`, `T Exhaust Temp State hy test`
- Utilisé par : `T Activate Critical State`, `T Alert critical exhaust mc`, `T Temperature State`
- Ligne export : 65780 · id 193758

#### T Temperature State  `SMC`
- Propriétés : Default state name=Off
- Fonction *Critical* :
  - **Activating** = `(In T Engine Thermal State = 1) OR (In T Exhaust Temp State = 1) OR (In T Hydraulics Temp State = 1)`
  - **Blocking** = `T Critical Temp Timer [s] <= 0`
- Fonction *High* :
  - **Activating** = `(In T Engine Thermal State = 2) OR (In T Exhaust Temp State = 2) OR (In T Hydraulics Temp State = 2)`
  - **Blocking** = `T Critical Temp Timer [s] <= 0`
- Fonction *Mid* :
  - **Activating** = `(In T Engine Thermal State = 3) OR (In T Exhaust Temp State = 3) OR (In T Hydraulics Temp State = 3)`
  - **Blocking** = `T Critical Temp Timer [s] <= 0`
- Fonction *Low* :
  - **Activating** = `In T Engine Thermal State = 4`
  - **Blocking** = `T Critical Temp Timer [s] <= 0`
- Lit : `In T Engine Thermal State`, `In T Exhaust Temp State`, `In T Hydraulics Temp State`, `T Critical Temp Timer`
- Utilisé par : `T Activate High Aft Fan`, `T Activate Low Aft Fan`, `T Activate exhaust Fan`, `Event log: Thermic Events`
- Ligne export : 65795 · id 193762

#### T Activate exhaust Fan  `IDC`
> The delay avoids state oscilation
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `T Temperature State > 0`
- Lit : `T Temperature State`
- Utilisé par : `T Activate exhaust Fan mc`
- Ligne export : 66026 · id 193788

#### T Activate Low Aft Fan  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `Inside(T Temperature State, 0, 4)`
- Lit : `T Temperature State`
- Utilisé par : `T Activate Low Aft Fan mc`, `T show ventilateur`, `MD4-5 page: MAIN Thermic`
- Ligne export : 66071 · id 193796

#### T Activate High Aft Fan  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `Inside(T Temperature State, 0, 3)`
- Lit : `T Temperature State`
- Utilisé par : `T Activate High Aft Fan mc`, `T show ventilateur`, `MD4-5 page: MAIN Thermic`
- Ligne export : 66117 · id 193804

#### T Activate Critical State  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `(In T Hydraulics Temp State = 1) OR (In T Engine Thermal State = 1) OR (In T Exhaust Temp State = 1)`
- Lit : `In T Engine Thermal State`, `In T Exhaust Temp State`, `In T Hydraulics Temp State`
- Utilisé par : *(personne)*
- Ligne export : 66163 · id 193812

#### T Alert critical hydraulic mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=e1101 Stop · Text, English=Hydraulic temparture critical. Derating power
- Logique :
  - **Showing** = `PositiveFlank((In T Hydraulics Temp State = 1))`
- Lit : `In T Hydraulics Temp State`
- Utilisé par : `Event log: Thermic Events`
- Ligne export : 66234 · id 193823

#### T Alert critical exhaust mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=e1107 Stop · Text, English=Exhaust temparture critical, check exhaust bay
- Logique :
  - **Showing** = `PositiveFlank((In T Exhaust Temp State = 1))`
- Lit : `In T Exhaust Temp State`
- Utilisé par : `Event log: Thermic Events`
- Ligne export : 66290 · id 193841

#### T show ventilateur  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T Activate High Aft Fan) OR (T Activate Low Aft Fan)`
- Lit : `T Activate High Aft Fan`, `T Activate Low Aft Fan`
- Utilisé par : *(personne)*
- Ligne export : 66346 · id 241062

## mc.Thermic / T.Track Up/Down

#### UP T  `IDC`
> arm up
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `UP/DOWN Button 4ET = 1`
- Lit : `UP/DOWN Button 4ET`
- Utilisé par : `Don'push button`, `Inter EV UP Delay`, `T Bloc`, `T EV tendre Chenille`, `T State Up/Down`
- Ligne export : 69017 · id 204135

#### Inter EV UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `UP T`
  - **Blocking** = `not(T Engine_Started mc)`
- Lit : `T Engine_Started mc`, `UP T`
- Utilisé par : `Inter EV UP`, `T Inter EV Verin`
- Ligne export : 69062 · id 204143

#### DOWN T  `IDC`
> arm down
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `UP/DOWN Button 4ET = 2`
- Lit : `UP/DOWN Button 4ET`
- Utilisé par : `Don'push button`, `Inter EV DOWN delay`, `T EV tendre Chenille`
- Ligne export : 69113 · id 204152

#### Inter EV DOWN delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `DOWN T`
  - **Blocking** = `not(T Engine_Started mc)`
- Lit : `DOWN T`, `T Engine_Started mc`
- Utilisé par : `Inter EV DOWN`, `T Inter EV Verin`
- Ligne export : 69158 · id 204160

#### T Locking UP Track  `DP`
- Propriétés : True text=ACTIVE · False text=NO ACTIVE · Default mode={True}
- Utilisé par : `T Bloc`, `Single adjust item: Locking UP Track`
- Ligne export : 69209 · id 204169

#### T Number of lockers  `SP`
- Propriétés : Input channel=None · Default state name=One · States={Two; Custom}
- Utilisé par : `T Locking Time`, `T Number of lockers custom`, `T unLocking Time`, `Single adjust item: Number of lockers`
- Ligne export : 69222 · id 204170

#### T Locking Time  `IP`
> Adapted to number of locker
- Propriétés : Unit=ms · Mode selector=T Number of lockers · Default mode: One={1000} · Mode 1: Two={2500} · Mode 2: Custom={1500}
- Lit : `T Number of lockers`
- Utilisé par : `T Bloc`, `Adjust group: Master Config`, `Single adjust item: T Locking Time`
- Ligne export : 69235 · id 204172

#### T Test Locker  `DP`
> Test lockers with engine started and arms down
- Propriétés : Default mode={False}
- Utilisé par : `Force Lock`, `Single adjust item: Test Locker`
- Ligne export : 69251 · id 204173

#### Force Lock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `PositiveFlank(T Test Locker)`
  - **Blocking** = `not(T Engine_Started mc)`
- Lit : `T Engine_Started mc`, `T Test Locker`
- Utilisé par : `Force Unlock`, `T Bloc`, `T OK UP/DOWN`
- Ligne export : 69264 · id 204174

#### T Bloc  `IDC`
> locking arm in high position
- Propriétés : Toggle=No · Delay on=0 · Delay off=T Locking Time [ms]
- Logique :
  - **Activating** = `((Screen_State Up/Down mc >= 100) and (NegativeFlank(UP T))) OR (Force Lock)`
  - **Blocking** = `(not(T Locking UP Track)) OR (not(T Engine_Started mc))`
- Lit : `Force Lock`, `Screen_State Up/Down mc`, `T Engine_Started mc`, `T Locking Time`, `T Locking UP Track`, `UP T`
- Utilisé par : `HIGH arm`, `IDC EV By Pass`, `Inter Lock landing`, `LOW arm`, `T Need Min Speed`, `Unlock landing`
- Ligne export : 69316 · id 204183

#### T Inter EV Verin  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP Delay) OR (Inter EV DOWN delay)`
- Lit : `Inter EV DOWN delay`, `Inter EV UP Delay`
- Utilisé par : `T SPEED Engine`, `T Super Ok tension`, `Unlock landing`
- Ligne export : 69401 · id 204196

#### Unlock landing  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Inter EV Verin`
  - **Blocking** = `(T Bloc) OR (not(T Engine_Started mc))`
- Lit : `T Bloc`, `T Engine_Started mc`, `T Inter EV Verin`
- Utilisé par : `Inter Unlock`
- Ligne export : 69451 · id 204205

#### T Force tension  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `T EV tendre Chenille`
- Ligne export : 69509 · id 204215

#### T With tension  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `T EV tendre Chenille`, `Single adjust item: With tension`
- Ligne export : 69522 · id 204216

#### T EV tendre Chenille  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T Super Ok tension) OR (T Force tension)`
  - **Blocking** = `(UP T) OR (DOWN T) OR (not(T With tension)) OR (not(T Engine_Started mc))`
- Lit : `DOWN T`, `T Engine_Started mc`, `T Force tension`, `T Super Ok tension`, `T With tension`, `UP T`
- Utilisé par : `IDC EV By Pass`, `IDC Tension`, `T Need Min Speed`
- Ligne export : 69535 · id 204217

#### T Force EV By Pass  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `IDC EV By Pass`, `T Inter EV By Pass`, `Single adjust item: Force EV By Pass`
- Ligne export : 69615 · id 204230

#### T OK UP/DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=T unLocking Time [ms] · Delay off=0
- Logique :
  - **Activating** = `Locking pressure mc 9 [bar] <= 10`
  - **Blocking** = `(T Untighten) OR (Force Lock)`
- Lit : `Force Lock`, `Locking pressure mc 9`, `T Untighten`, `T unLocking Time`
- Utilisé par : `Inter EV DOWN`, `Inter EV UP`, `OK UP/DOWN Sel`
- Ligne export : 69628 · id 204232

#### Inter EV UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP Delay) AND (T OK UP/DOWN)`
- Lit : `Inter EV UP Delay`, `T OK UP/DOWN`
- Utilisé par : `HIGH arm`, `IDC EV By Pass`, `T EV Up`
- Ligne export : 69687 · id 204242

#### Inter EV DOWN  `IDC`
> tempo to make sure that bypass off before down
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV DOWN delay) AND (T OK UP/DOWN)`
- Lit : `Inter EV DOWN delay`, `T OK UP/DOWN`
- Utilisé par : `HIGH arm`, `IDC EV By Pass Down`, `T EV Down`
- Ligne export : 69737 · id 204251

#### IDC EV By Pass Down  `IDC`
> no tempo to make sure that bypass off before down
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter EV DOWN`
- Lit : `Inter EV DOWN`
- Utilisé par : `IDC EV By Pass sel`
- Ligne export : 69787 · id 204297

#### HIGH arm  `IDC`
> arm high
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Inter EV UP) OR (Inter EV DOWN)`
  - **Blocking** = `T Bloc`
- Lit : `Inter EV DOWN`, `Inter EV UP`, `T Bloc`
- Utilisé par : `IDC EV By Pass`, `LOW arm`
- Ligne export : 69830 · id 204278

#### LOW arm  `IDC`
> arm down/low
- Propriétés : Toggle=No · Delay on=0 · Delay off=1500
- Logique :
  - **Activating** = `(NegativeFlank(HIGH arm)) OR (T Bloc)`
- Lit : `HIGH arm`, `T Bloc`
- Utilisé par : `IDC EV By Pass`
- Ligne export : 69887 · id 204288

#### IDC EV By Pass  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP) OR (T EV tendre Chenille) OR (T Bloc) OR (HIGH arm) OR (LOW arm) OR (T Force EV By Pass)`
- Lit : `HIGH arm`, `Inter EV UP`, `LOW arm`, `T Bloc`, `T EV tendre Chenille`, `T Force EV By Pass`
- Utilisé par : `IDC EV By Pass sel`
- Ligne export : 69938 · id 204305

#### IDC EV By Pass sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(IDC EV By Pass) OR (IDC EV By Pass Down)`
- Lit : `IDC EV By Pass`, `IDC EV By Pass Down`
- Utilisé par : `T Inter EV By Pass`
- Ligne export : 70016 · id 204318

#### T Inter EV By Pass  `IDC`
> By Pass required and min speed done. Attention: latching Event, stays true even if need min speed is false. Delay Off to avoid emtying consumer before opening by pass
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(IDC EV By Pass sel) AND (T Min Speed Ok)   [verrouillé]`
  - **Blocking** = `((not(T Force EV By Pass)) and T Untighten) OR (not(IDC EV By Pass sel))`
- Lit : `IDC EV By Pass sel`, `T Force EV By Pass`, `T Min Speed Ok`, `T Untighten`
- Utilisé par : `IDC Tension`, `Inter Lock landing`, `T EV By pass`, `T Need Min Speed`
- Ligne export : 70066 · id 204327

#### IDC Tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T EV tendre Chenille) AND (T Inter EV By Pass)`
- Lit : `T EV tendre Chenille`, `T Inter EV By Pass`
- Utilisé par : `Inter Tension`
- Ligne export : 70148 · id 204260

#### Inter Tension  `IDC`
> Delay On to avoid emptying Tension before pression is raised
- Propriétés : Toggle=No · Delay on=300 · Delay off=0
- Logique :
  - **Activating** = `(IDC Tension) OR (T Untighten)`
- Lit : `IDC Tension`, `T Untighten`
- Utilisé par : `T EV Tension`
- Ligne export : 70198 · id 204269

#### Inter Lock landing  `IDC`
> delay before locking
- Propriétés : Toggle=No · Delay on=300 · Delay off=0
- Logique :
  - **Activating** = `(T Bloc) AND (T Inter EV By Pass)`
- Lit : `T Bloc`, `T Inter EV By Pass`
- Utilisé par : `T EV Lock`
- Ligne export : 70248 · id 204340

#### Force Unlock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `NegativeFlank(Force Lock)`
- Lit : `Force Lock`
- Utilisé par : `Inter Unlock`
- Ligne export : 70298 · id 204354

#### Inter Unlock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Unlock landing) OR (Force Unlock)`
- Lit : `Force Unlock`, `Unlock landing`
- Utilisé par : `T EV UnBlock`
- Ligne export : 70342 · id 204362

#### State Up/Down Raw  `IMAC`
- Logique :
  - **Controlling** = `Screen_State Up/Down mc`
- Lit : `Screen_State Up/Down mc`
- Utilisé par : `T State Up/Down`
- Ligne export : 70392 · id 204372

#### Don'push button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `False`
  - **Blocking** = `(UP T) OR (DOWN T)`
- Lit : `DOWN T`, `UP T`
- Utilisé par : `T State Up/Down`
- Ligne export : 70433 · id 204380

#### T OK BLOC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Locking pressure mc 9 [bar] >= 100`
- Lit : `Locking pressure mc 9`
- Utilisé par : `E&T OK BLOC`, `T State Up/Down`
- Ligne export : 70490 · id 210079

#### T State Up/Down  `SMC`
- Propriétés : Default state name=Error
- Fonction *DOWN* :
  - **Activating** = `((State Up/Down Raw < 2) and (State Up/Down Raw >= 0)) OR ((State Up/Down Raw = 0) and UP T)`
  - **Blocking** = `Don'push button`
- Fonction *INTERMEDIATE* :
  - **Activating** = `(State Up/Down Raw >= 2) AND (State Up/Down Raw <= 98)`
  - **Blocking** = `Don'push button`
- Fonction *UP* :
  - **Activating** = `State Up/Down Raw > 98`
  - **Blocking** = `Don'push button`
- Fonction *UP and bloc* :
  - **Activating** = `(State Up/Down Raw >= 99) AND (T OK BLOC)`
  - **Blocking** = `Don'push button`
- Lit : `Don'push button`, `State Up/Down Raw`, `T OK BLOC`, `UP T`
- Utilisé par : `T Up/DOWN STATE d3 Int`, `T VIEW ENGINE STATE`, `T VIEW TRACK STATE`, `therm activ schema inter`, `therm show schema down`, `therm show schema up`
- Ligne export : 70535 · id 204390

#### T EV Up  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter EV UP`
- Lit : `Inter EV UP`
- Utilisé par : `EV Up Sel`
- Ligne export : 70763 · id 204830

#### T EV Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter EV DOWN`
- Lit : `Inter EV DOWN`
- Utilisé par : `EV Down Sel`
- Ligne export : 70806 · id 204838

#### T EV By pass  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=300
- Logique :
  - **Activating** = `T Inter EV By Pass`
- Lit : `T Inter EV By Pass`
- Utilisé par : `EV By pass Sel`
- Ligne export : 70849 · id 204846

#### T EV Tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter Tension`
- Lit : `Inter Tension`
- Utilisé par : `EV Tension Sel`
- Ligne export : 70892 · id 204854

#### T EV Lock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter Lock landing`
- Lit : `Inter Lock landing`
- Utilisé par : `EV Lock Sel`
- Ligne export : 70935 · id 204862

#### T EV UnBlock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter Unlock`
- Lit : `Inter Unlock`
- Utilisé par : `EV UnBlock Sel`
- Ligne export : 70978 · id 204870

#### T Number of lockers custom  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Number of lockers = 2`
- Lit : `T Number of lockers`
- Utilisé par : `Single adjust item: T Locking Time`
- Ligne export : 71027 · id 233940

#### T unLocking Time  `IP`
> Adapted to number of locker
- Propriétés : Unit=ms · Mode selector=T Number of lockers · Default mode: One={5000} · Mode 1: Two={5000} · Mode 2: Custom={8000}
- Lit : `T Number of lockers`
- Utilisé par : `T OK UP/DOWN`
- Ligne export : 71072 · id 233947

#### therm show schema down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T State Up/Down = 1`
- Lit : `T State Up/Down`
- Utilisé par : `MD4-5 page: MAIN Thermic`
- Ligne export : 71088 · id 240988

#### therm activ schema inter  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T State Up/Down = 2`
- Lit : `T State Up/Down`
- Utilisé par : `Timer clignotement schema inter E`
- Ligne export : 71133 · id 240992

#### therm show schema up  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T State Up/Down = 3) OR (T State Up/Down = 4)`
- Lit : `T State Up/Down`
- Utilisé par : `MD4-5 page: MAIN Thermic`
- Ligne export : 71178 · id 240996

#### Timer clignotement schema inter E  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `therm activ schema inter`
  - **Resetting** = `not(therm activ schema inter)`
- Lit : `therm activ schema inter`
- Utilisé par : `therm show schema inter`
- Ligne export : 71232 · id 241000

#### therm show schema inter  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Timer clignotement schema inter E [s] mod 2) = 1`
- Lit : `Timer clignotement schema inter E`
- Utilisé par : `MD4-5 page: MAIN Thermic`
- Ligne export : 71292 · id 241005

## mc.Thermic / T.Track tension

#### T Tracks pressure Mode  `SP`
> This channel is used to give unit and names to the MEM
- Propriétés : Input channel=None · Default state name=AUTO · States={UNTIGHTEN}
- Utilisé par : `IDC Free T`, `ON/OFF/Untighed`, `T Tracks pressure Mode`, `T Untighten`, `Tension State`, `Single adjust item: Tracks pressure Mode`
- Ligne export : 68013 · id 205137

#### T Tracks pressure Mode  `MEM`
- Propriétés : Input channel=T Tracks pressure Mode · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : `Reset Startup`, `T Tracks pressure Mode`
- Utilisé par : `IDC Free T`, `ON/OFF/Untighed`, `T Untighten`, `Tension State`, `Single adjust item: Tracks pressure Mode`
- Ligne export : 68025 · id 205148

#### Wait engine start  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `T System Started DELAYS`
- Lit : `T System Started DELAYS`
- Utilisé par : `ON/OFF/Untighed`, `Ok tension`, `Tension State`, `Wait engine Stop`
- Ligne export : 68068 · id 205156

#### ON/OFF/Untighed  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ON* :
  - **Activating** = `Wait engine start`
  - **Blocking** = `T Tracks pressure Mode`
- Fonction *UNTIGHTED* :
  - **Activating** = `T Tracks pressure Mode`
- Lit : `T Tracks pressure Mode`, `Wait engine start`
- Utilisé par : `T Super Ok tension`
- Ligne export : 68111 · id 205164

#### T Pression filtered  `SFC`
- Propriétés : Input channel=Track pressure mc 10 [bar] · Enable=Yes · Type=Slopes · Slopes={{50; 50}; {1; 1}}
- Lit : `Track pressure mc 10`
- Utilisé par : `Need Pressure`
- Ligne export : 68189 · id 205177

#### T Time to tension  `IP`
- Propriétés : Unit=ms · Default mode={150}
- Utilisé par : `T Super Ok tension`, `Single adjust item: Time to tension`
- Ligne export : 68207 · id 205178

#### T Untighten  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Tracks pressure Mode`
- Lit : `T Tracks pressure Mode`
- Utilisé par : `Inter Tension`, `Ok tension`, `T Inter EV By Pass`, `T OK UP/DOWN`
- Ligne export : 68219 · id 205179

#### Ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `PositiveFlank(Wait engine start)`
  - **Blocking** = `T Untighten`
- Lit : `T Untighten`, `Wait engine start`
- Utilisé par : `T Super Ok tension`
- Ligne export : 68262 · id 205187

#### T 10 minutes auto tender  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=10
- Logique :
  - **Decreasing** = `T System Started DELAYS`
  - **Resetting** = `T 10 minutes auto tender [min] <= 0`
- Lit : `T System Started DELAYS`
- Utilisé par : `T Super Ok tension`
- Ligne export : 68313 · id 205196

#### T Tension Pressure  `IP`
- Propriétés : Unit=bar · Default mode={160}
- Utilisé par : `Need Pressure`, `T show symbole track bleu`, `Single adjust item: Tension Pressure`
- Ligne export : 68374 · id 205207

#### T Need Pressure Tempo  `IP`
- Propriétés : Unit=ms · Default mode={5000}
- Utilisé par : `Need Pressure`, `Single adjust item: Need Pressure Tempo`
- Ligne export : 68386 · id 205208

#### Need Pressure  `IDC`
- Propriétés : Toggle=No · Delay on=T Need Pressure Tempo [ms] · Delay off=0
- Logique :
  - **Activating** = `T Tension Pressure [bar] > T Pression filtered [bar]`
- Lit : `T Need Pressure Tempo`, `T Pression filtered`, `T Tension Pressure`
- Utilisé par : `T Super Ok tension`, `Adjust group: Master Thermic`
- Ligne export : 68398 · id 205209

#### T Tension Error Parameter  `FP`
- Propriétés : Unit=% · Default mode={100}
- Utilisé par : `Over Tension`
- Ligne export : 68443 · id 205217

#### Delay Off super ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `T Super Ok tension`
- Lit : `T Super Ok tension`
- Utilisé par : `Super Ok Tension Math`
- Ligne export : 68455 · id 205218

#### Super Ok Tension Math  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `Delay Off super ok tension * 100`
- Lit : `Delay Off super ok tension`
- Utilisé par : `Slope Super Ok`
- Ligne export : 68498 · id 205226

#### Slope Super Ok  `SFC`
- Propriétés : Input channel=Super Ok Tension Math [%] · Enable=Yes · Type=Slopes · Slopes={{5; 1}; {2; 2}}
- Lit : `Super Ok Tension Math`
- Utilisé par : `Over Tension`
- Ligne export : 68541 · id 205234

#### Over Tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Over Tension) OR (Slope Super Ok [%] > T Tension Error Parameter [%])`
  - **Blocking** = `not(T System Started DELAYS)`
- Lit : `Over Tension`, `Slope Super Ok`, `T System Started DELAYS`, `T Tension Error Parameter`
- Utilisé par : `Over Tension`, `T Super Ok tension`, `T Track Tension Error mc`, `Event log: Electronic logs`, `Event log: Hydraulic Event`
- Ligne export : 68559 · id 205235

#### T Super Ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=T Time to tension [ms] · Function selector=ON/OFF/Untighed
- Fonction *OFF* :
  - **Blocking** = `True`
- Fonction *ON* :
  - **Activating** = `(NegativeFlank(Ok tension)) OR (T 10 minutes auto tender [min] = 0) OR (Need Pressure)`
  - **Blocking** = `(Over Tension) OR (T Inter EV Verin)`
- Fonction *UNTIGHTED* :
  - **Blocking** = `True`
- Lit : `Need Pressure`, `ON/OFF/Untighed`, `Ok tension`, `Over Tension`, `T 10 minutes auto tender`, `T Inter EV Verin`, `T Time to tension`
- Utilisé par : `Delay Off super ok tension`, `T EV tendre Chenille`
- Ligne export : 68619 · id 205245

#### Wait engine Stop  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=4000
- Logique :
  - **Activating** = `Wait engine start`
- Lit : `Wait engine start`
- Utilisé par : `Tension State`
- Ligne export : 68755 · id 205271

#### Tension State  `SMC`
- Propriétés : Default state name=ON/OFF
- Fonction *Parking* :
  - **Activating** = `Wait engine Stop`
  - **Blocking** = `(Wait engine start) OR (T Tracks pressure Mode)`
- Fonction *Unthingten* :
  - **Activating** = `T Tracks pressure Mode`
- Lit : `T Tracks pressure Mode`, `Wait engine Stop`, `Wait engine start`
- Utilisé par : *(personne)*
- Ligne export : 68798 · id 205279

#### T Track Tension Error mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header, English=e1043 Track Tension Error · Text, English=Try a Calibrating (Setting/Maintenance). Use straight. Contact your service center. · Channel=Track pressure mc 10 [bar]
- Logique :
  - **Showing** = `Over Tension`
- Lit : `Over Tension`, `Track pressure mc 10`
- Utilisé par : *(personne)*
- Ligne export : 68883 · id 205293

#### T show symbole track bleu  `IDC`
> fait apparaitre le symbole track en bleu ou en rouge
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Track pressure mc 10 [bar] >= (T Tension Pressure [bar] - 10)`
  - **Blocking** = `Track pressure mc 10 [bar] < (T Tension Pressure [bar] - 10)`
- Lit : `T Tension Pressure`, `Track pressure mc 10`
- Utilisé par : `E&T Show symbole track white`
- Ligne export : 68929 · id 241041

## mc.Thermic / T.Translate

#### T Speed Int  `IMAC`
- Logique :
  - **Controlling** = `Screen_Speed Input mc`
- Lit : `Screen_Speed Input mc`
- Utilisé par : `T Speed Mode`, `T Speed Pump`, `T State All Speed`
- Ligne export : 66696 · id 205813

#### T Speed Pump  `SMC`
- Propriétés : Default state name=Slow
- Fonction *Super Slow* :
  - **Activating** = `T Speed Int = 2`
  - **Blocking** = `T Speed Int = 1`
- Fonction *Fast Speed* :
  - **Activating** = `(T Speed Int = 3) OR (T Speed Int = 4) OR (T Speed Int = 5)`
  - **Blocking** = `(T Speed Int = 1) OR (T Persistant Water Temp [°C] >= T Water °C Critical Critical [°C])`
- Lit : `T Persistant Water Temp`, `T Speed Int`, `T Water °C Critical Critical`
- Utilisé par : `T Backward - direct corrector`, `T Backward Curent`, `T Brake Slope`, `T Forward - direct corrector`, `T Forward Curent`, `T Start Slope`, `T Stop Slope`, `T VIEW TRACK STATE`
- Ligne export : 66737 · id 205822

#### Engine Stopped  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(T Engine_Started mc)`
- Lit : `T Engine_Started mc`
- Utilisé par : `T Speed Mode`
- Ligne export : 66857 · id 205839

#### IDC Free T  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Screen_Free Input mc) OR (T Tracks pressure Mode)`
- Lit : `Screen_Free Input mc`, `T Tracks pressure Mode`
- Utilisé par : `T Speed Mode`
- Ligne export : 66901 · id 205847

#### T Speed Mode  `SMC`
- Propriétés : Default state name=OFF
- Fonction *IDLE* :
  - **Activating** = `T Speed Int = 0`
  - **Blocking** = `Engine Stopped`
- Fonction *Free* :
  - **Activating** = `(T Speed Int = 1) OR (T Speed Int = 2) OR (T Speed Int = 3)`
  - **Blocking** = `(Engine Stopped) OR (not(IDC Free T))`
- Fonction *UnFree* :
  - **Activating** = `(T Speed Int = 1) OR (T Speed Int = 2) OR (T Speed Int = 3)`
  - **Blocking** = `Engine Stopped`
- Lit : `Engine Stopped`, `IDC Free T`, `T Speed Int`
- Utilisé par : `DMAC Table Left`, `DMAC Table Right`, `T Speed Mode Int`
- Ligne export : 66951 · id 205856

#### T Start Slope  `FP`
- Propriétés : Unit=%/s · Mode selector=T Speed Pump · Default mode: Slow={50} · Mode 1: Super Slow={50} · Mode 2: Fast Speed={30}
- Lit : `T Speed Pump`
- Utilisé par : `T Left Filter`, `T Right Filter`, `Single adjust item: Start Slope`
- Ligne export : 67124 · id 205890

#### T Stop Slope  `FP`
- Propriétés : Unit=%/s · Mode selector=T Speed Pump · Default mode: Slow={60} · Mode 1: Super Slow={60} · Mode 2: Fast Speed={80}
- Lit : `T Speed Pump`
- Utilisé par : `T Left Filter`, `T Right Filter`, `Single adjust item: Stop Slope`
- Ligne export : 67140 · id 205891

#### DMAC_EV_2_Left  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Math Gauche Left 45 [%] * T System Started DELAYS`
- Lit : `Math Gauche Left 45`, `T System Started DELAYS`
- Utilisé par : `Cruise Left`, `Cruise Right`, `DMAC Table Left`, `Left unfree`, `Right unfree`
- Ligne export : 67156 · id 205892

#### DMAC_EV_1_Right  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Math Droit Right 45 [%] * T System Started DELAYS`
- Lit : `Math Droit Right 45`, `T System Started DELAYS`
- Utilisé par : `Cruise Left`, `Cruise Right`, `DMAC Table Right`, `Left unfree`, `Right unfree`
- Ligne export : 67208 · id 205902

#### Cruise Left  `LTC`
- Propriétés : Unit=% · Row selector=DMAC_EV_2_Left [%] · Column selector=DMAC_EV_1_Right [%] · Interpolation=Yes · Lookup table=(0; -100; -90; -80; -70; -60; -50; -40; -30; -20; -10; 0; 10; 20; 30; 40; 50; 60; 70; 80; 90; 100); (-100; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-90; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-80; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-70; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-60; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-50; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-40; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-30; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-20; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100); (10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 97; 90; 90; 90; 90; 90; 90; 90; 90; 90; 90); (20; 0; 0; 0; 0; 0; 0; 0; 0; 0...
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`
- Utilisé par : *(personne)*
- Ligne export : 67260 · id 205912

#### T Max_diffrential  `IP`
- Propriétés : Unit=% · Default mode={70}
- Utilisé par : `Left unfree`, `Right unfree`, `Single adjust item: Max_diffrential`
- Ligne export : 67273 · id 205913

#### Left unfree  `MAC`
- Logique :
  ```qcode
  right := DMAC_EV_1_Right
  left := DMAC_EV_2_Left
  
  if (right > 0 and left < 0) or (right < 0 and left > 0) then
    res := 0
  elseif  Abs(right) <= Abs(left) then
    res := left
  elseif Abs(right) > Abs(left) then
    res := MaxOfAbs(right * T Max_diffrential  / 100, left)
  endif
  
  
  Result := res
  ```
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `T Max_diffrential`
- Utilisé par : `DMAC Table Left`
- Ligne export : 67285 · id 205914

#### DMAC Table Left  `DMAC`
- Propriétés : Unit=% · Function selector=T Speed Mode
- Fonction *OFF* :
  - **Controlling +/-** = `0`
- Fonction *IDLE* :
  - **Controlling +/-** = `0`
- Fonction *Free* :
  - **Controlling +/-** = `DMAC_EV_2_Left [%]`
- Fonction *UnFree* :
  - **Controlling +/-** = `Left unfree`
- Lit : `DMAC_EV_2_Left`, `Left unfree`, `T Speed Mode`
- Utilisé par : `T Brake Activation`, `T Left Filter`
- Ligne export : 67315 · id 205952

#### T Left Filter  `SFC`
- Propriétés : Input channel=DMAC Table Left [%] · Enable=Yes · Type=Slopes · Slopes={{T Start Slope [%/s]; T Stop Slope [%/s]}; {T Start Slope [%/s]; T Stop Slope [%/s]}}
- Lit : `DMAC Table Left`, `T Start Slope`, `T Stop Slope`
- Utilisé par : `T Brake Activation`, `T Pump 2 Left Filter ECC1`
- Ligne export : 67485 · id 206007

#### Cruise Right  `LTC`
- Propriétés : Unit=% · Row selector=DMAC_EV_1_Right [%] · Column selector=DMAC_EV_2_Left [%] · Interpolation=Yes · Lookup table=(0; -100; -90; -80; -70; -60; -50; -40; -30; -20; -10; 0; 10; 20; 30; 40; 50; 60; 70; 80; 90; 100); (-100; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-90; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-80; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-70; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-60; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-50; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-40; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-30; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-20; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100); (10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 97; 90; 90; 90; 90; 90; 90; 90; 90; 90; 90); (20; 0; 0; 0; 0; 0; 0; 0; 0; 0...
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`
- Utilisé par : *(personne)*
- Ligne export : 67503 · id 206008

#### Right unfree  `MAC`
- Logique :
  ```qcode
  right := DMAC_EV_1_Right
  left := DMAC_EV_2_Left
  
  if (right > 0 and left < 0) or (right < 0 and left > 0) then
    res := 0
  elseif  Abs(right) >= Abs(left) then
    res := right
  elseif Abs(right) < Abs(left) then
    res := MaxOfAbs(left * T Max_diffrential  / 100, right)
  endif
  
  
  Result := res
  ```
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `T Max_diffrential`
- Utilisé par : `DMAC Table Right`
- Ligne export : 67516 · id 206009

#### DMAC Table Right  `DMAC`
- Propriétés : Unit=% · Function selector=T Speed Mode
- Fonction *OFF* :
  - **Controlling +/-** = `0`
- Fonction *IDLE* :
  - **Controlling +/-** = `0`
- Fonction *Free* :
  - **Controlling +/-** = `DMAC_EV_1_Right [%]`
- Fonction *UnFree* :
  - **Controlling +/-** = `Right unfree`
- Lit : `DMAC_EV_1_Right`, `Right unfree`, `T Speed Mode`
- Utilisé par : `T Brake Activation`, `T Right Filter`
- Ligne export : 67546 · id 206047

#### T Right Filter  `SFC`
- Propriétés : Input channel=DMAC Table Right [%] · Enable=Yes · Type=Slopes · Slopes={{T Start Slope [%/s]; T Stop Slope [%/s]}; {T Start Slope [%/s]; T Stop Slope [%/s]}}
- Lit : `DMAC Table Right`, `T Start Slope`, `T Stop Slope`
- Utilisé par : `T Brake Activation`, `T Pump 1 Right Filter ECC1`
- Ligne export : 67716 · id 206102

#### T Brake Activation  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(DMAC Table Left [%] <> 0) OR (DMAC Table Right [%] <> 0) OR (T Right Filter [%] <> 0) OR (T Left Filter [%] <> 0)`
- Lit : `DMAC Table Left`, `DMAC Table Right`, `T Left Filter`, `T Right Filter`
- Utilisé par : `T Inter EV Frein`
- Ligne export : 67734 · id 206103

#### T State All Speed  `SMC`
- Propriétés : Default state name=OFF
- Fonction *IDLE* :
  - **Activating** = `T Speed Int = 0`
  - **Blocking** = `not(T System Started DELAYS)`
- Fonction *Slow* :
  - **Activating** = `(T Speed Int = 1) OR (T Persistant Water Temp [°C] >= T Water °C Critical Critical [°C])`
  - **Blocking** = `not(T System Started DELAYS)`
- Fonction *Super Slow* :
  - **Activating** = `T Speed Int = 2`
  - **Blocking** = `not(T System Started DELAYS)`
- Fonction *Fast* :
  - **Activating** = `T Speed Int = 3`
  - **Blocking** = `(not(T System Started DELAYS)) OR (T Persistant Water Temp [°C] >= T Water °C Critical Critical [°C])`
- Lit : `T Persistant Water Temp`, `T Speed Int`, `T System Started DELAYS`, `T Water °C Critical Critical`
- Utilisé par : `T State All Speed Int`, `T State All Speed d3 Int`, `T VIEW TRACK STATE`
- Ligne export : 67806 · id 206123
