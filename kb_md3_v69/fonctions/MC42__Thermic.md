# MC42 — Thermic

261 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Thermic

#### Engine_Started  `IDC`
> hysteris on dectection of stall engine
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Speed CAN [rpm] > Stall speed eng on   [Latching And]`
  - **Blocking** = `Speed CAN [rpm] < Stall speed eng off`
- Lit : ``, `Speed CAN`, `Stall speed eng off`, `Stall speed eng on`
- Utilisé par : `AutoStopafter 5 secondes`, `Critical Temp Timer`, `ECC1_Engine_Temp`, `ECC1_Oil_Temp`, `ECC1_Power`, `ECC1_Speed`, `EV tendre Chenille`, `Engine Stopped`, `Force Lock`, `Fuel line ignition IDC`, `High Temp Timer`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP Delay`, `K6 Engine Water Pump`, `K7 Exhaust Water Pump`, `Lock landing`, `Low Temp Timer`, `MD3 start last checks`, `Mid Temp Timer`, `Persistant Water Temp`, `Pre Fuel line ignition IDC`, `System Started DELAYS`, `Unlock landing`, `Voyant Pression Huile Moteur`, `Wait Bad Pressure`, `Wait Hot Temperature`, `Event log: Thermic Events`, `Statistics log: Thermic Stats`
- Ligne export : 14807 · id 32282

#### Activate exhaust Fan  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Activate exhaust Fan`
- Lit : ``, `Activate exhaust Fan`
- Utilisé par : `Activate Exhaust`
- Ligne export : 23713 · id 66347

#### Activate Low Aft Fan  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Activate Low Aft Fan`
- Lit : ``, `Activate Low Aft Fan`
- Utilisé par : `Activate Low Aft Fan`
- Ligne export : 23756 · id 66358

#### Activate High Aft Fan  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Activate High Aft Fan`
- Lit : ``, `Activate High Aft Fan`
- Utilisé par : `Activate High Aft Fan`, `MD3 page: Thermic`
- Ligne export : 23799 · id 66368

#### Stall speed eng on  `IP`
- Propriétés : Default mode={700}
- Utilisé par : `Engine_Started`
- Ligne export : 23842 · id 66703

#### Stall speed eng off  `IP`
- Propriétés : Default mode={600}
- Utilisé par : `Engine_Started`
- Ligne export : 23854 · id 66705

## Thermic / Engine Speed calc

#### Joystick not zero  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Right CanIn [%] <> 0) OR (Left CanIn [%] <> 0)`
- Lit : ``, `Left CanIn`, `Right CanIn`
- Utilisé par : `SPEED Engine`
- Ligne export : 18125 · id 29433

#### Force at 2200 rpm  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `SPEED Engine`, `Adjust group: Master Features`, `Single adjust item: Force at 2200 rpm`
- Ligne export : 18179 · id 29454

#### SPEED Engine  `SMC`
- Propriétés : Default state name=Default
- Fonction *Ralenti* :
  - **Activating** = `(Joystick not zero = 0) and (not(Inter EV Verin))`
  - **Blocking** = `(Force at 2200 rpm) OR (Speed Input = 5)`
- Fonction *Regime PV* :
  - **Activating** = `(Speed Input = 2) OR (Speed Input = 1)`
  - **Blocking** = `(Inter EV Verin) OR (Force at 2200 rpm)`
- Fonction *Régime GV* :
  - **Activating** = `(Speed Input = 3) OR (Speed Input = 6)`
  - **Blocking** = `(Force at 2200 rpm) OR (Inter EV Verin)`
- Fonction *Road Cruise* :
  - **Activating** = `(Speed Input = 4) OR (Speed Input = 5)`
  - **Blocking** = `(Force at 2200 rpm) OR (Inter EV Verin)`
- Fonction *Regim UP/DOWN* :
  - **Activating** = `Inter EV Verin`
  - **Blocking** = `Force at 2200 rpm`
- Fonction *2200 tr/min* :
  - **Activating** = `Force at 2200 rpm`
- Lit : ``, `Force at 2200 rpm`, `Inter EV Verin`, `Joystick not zero`, `Speed Input`
- Utilisé par : `Accel Filter`, `Calcul Accélération`, `Decel Filter`
- Ligne export : 18192 · id 29455

#### Max Manip  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxOf (Absolute)(Abs(Right CanIn [%]), Abs(Left CanIn [%]))`
- Lit : ``, `Left CanIn`, `Right CanIn`
- Utilisé par : `Calcul Accélération`
- Ligne export : 18504 · id 29497

#### General speed filtering  `FP`
> Max speed slope applied while running tracks
- Propriétés : Unit=%/s · Mode selector=Engine type · Default mode: EB2 1.2L={25} · Mode 1: FORD 1.5L={100}
- Lit : `Engine type`
- Utilisé par : `Accel Filter`, `Decel Filter`, `Adjust group: Master Thermic`, `Single adjust item: General speed filtering`
- Ligne export : 18555 · id 29506

#### In UP/DOWN Speed  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=Tension/UpDown Speed [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Tension/UpDown Speed`
- Utilisé par : `Calcul Accélération`
- Ligne export : 18569 · id 64857

#### In IDLE Speed  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=IDLE Speed [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `IDLE Speed`
- Utilisé par : `Calcul Accélération`
- Ligne export : 18583 · id 64858

#### In Slow Speed  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=Slow Max  Speed [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Slow Max  Speed`
- Utilisé par : `Calcul Accélération`
- Ligne export : 18597 · id 64859

#### In Hight Speed  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=Hight Speed [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Hight Speed`
- Utilisé par : `Calcul Accélération`
- Ligne export : 18611 · id 64860

#### In Min Speed mode  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=Min Speed mode [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Min Speed mode`
- Utilisé par : `Calcul Accélération`
- Ligne export : 18625 · id 64862

#### Calcul Accélération  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed · Function selector=SPEED Engine
- Fonction *Default* :
  - **Controlling** = `1800`
- Fonction *Ralenti* :
  - **Controlling** = `In IDLE Speed [rpm]`
- Fonction *Regime PV* :
  - **Controlling** = `lin(Max Manip: 0->In Min Speed mode [rpm], 100->In Slow Speed [rpm], Freeze)`
- Fonction *Régime GV* :
  - **Controlling** = `lin(Max Manip: 0->In Min Speed mode [rpm], 100->In Hight Speed [rpm], Freeze)`
- Fonction *Road Cruise* :
  - **Controlling** = `lin(Max Manip: 100->In Min Speed mode [rpm], 0->In Hight Speed [rpm], Freeze)`
- Fonction *Regim UP/DOWN* :
  - **Controlling** = `In UP/DOWN Speed [rpm]`
- Fonction *2200 tr/min* :
  - **Controlling** = `2200`
- Lit : ``, `In Hight Speed`, `In IDLE Speed`, `In Min Speed mode`, `In Slow Speed`, `In UP/DOWN Speed`, `Max Manip`, `SPEED Engine`
- Utilisé par : `Speed_RPM_needed`
- Ligne export : 18639 · id 29509

#### STARTING  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  - **Activating** = `PositiveFlank(System Started DELAYS)`
- Lit : ``, `System Started DELAYS`
- Utilisé par : `Need Min Speed`
- Ligne export : 18882 · id 29583

#### ?Throttle pulse at Start up  `DP`
> Do We apply a short Tension speed event just after start up?
- Propriétés : Default mode={False}
- Utilisé par : `Need Min Speed`, `Adjust group: Master Thermic`, `Single adjust item: ?Throttle pulse at Start up`
- Ligne export : 18926 · id 63182

#### Tempo Need Min Speed  `IP`
> Tempo to allow Idle speed after a Torque request from hydraulic accessories
- Propriétés : Unit=ms · Default mode={300}
- Utilisé par : `Need Min Speed`, `Adjust group: Master Thermic`, `Single adjust item: Tempo Need Min Speed`
- Ligne export : 18939 · id 63241

#### Need Min Speed  `IDC`
> Activated if ther is an hydraulic Torque coming from Accessories pump
- Propriétés : Toggle=No · Delay on=0 · Delay off=Tempo Need Min Speed [ms]
- Logique :
  - **Activating** = `(STARTING and ?Throttle pulse at Start up) OR (Inter EV By Pass) OR (EV tendre Chenille) OR (Lock landing)`
- Lit : ``, `?Throttle pulse at Start up`, `EV tendre Chenille`, `Inter EV By Pass`, `Lock landing`, `STARTING`, `Tempo Need Min Speed`
- Utilisé par : `Speed_RPM_needed`, `Measure group: Thermic vs Hydraulic`
- Ligne export : 18951 · id 29559

#### In Tension Speed  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=Tension/UpDown Speed [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Tension/UpDown Speed`
- Utilisé par : `Speed_RPM_needed`
- Ligne export : 19017 · id 64856

#### Speed_RPM_needed  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxOf((Need Min Speed * In Tension Speed [rpm]), Calcul Accélération [rpm])`
- Lit : ``, `Calcul Accélération`, `In Tension Speed`, `Need Min Speed`
- Utilisé par : `Speed Data remapping`, `Speed Error Calcul`, `Speed error`, `Measure group: Hydraulic`, `Measure group: Thermic vs Hydraulic`
- Ligne export : 19031 · id 29571

#### Speed Data remapping  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Speed_RPM_needed [rpm]: 1000->0, 4000->100, Freeze)`
- Lit : ``, `Speed_RPM_needed`
- Utilisé par : `TSC1 Filter`
- Ligne export : 19084 · id 35858

#### TSC1 Filter  `SFC`
- Propriétés : Input channel=Speed Data remapping [%] · Enable=Yes · Type=Slopes · Slopes={{Accel Filter [%/s]; Decel Filter [%/s]}; {Accel Filter [%/s]; Accel Filter [%/s]}}
- Lit : `Accel Filter`, `Decel Filter`, `Speed Data remapping`
- Utilisé par : `Engine speed to send`, `Measure group: Engine Thermic`
- Ligne export : 19131 · id 29581

#### in Speed CAN  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=Speed CAN [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Speed CAN`
- Utilisé par : `Min Speed Ok`, `Speed error`
- Ligne export : 19149 · id 65177

#### Speed error  `MAC`
> % of error between request speed and real speed
- Propriétés : Unit=%
- Logique :
  ```qcode
  If Speed_RPM_needed <>0 then
  Result:= (Speed_RPM_needed-in Speed CAN) / Speed_RPM_needed
  endif
  ```
- Lit : `Speed_RPM_needed`, `in Speed CAN`
- Utilisé par : `?Speed OK`, `Measure group: Engine Thermic`, `Measure group: Thermic vs Hydraulic`
- Ligne export : 19163 · id 63188

#### Max Speed Gap  `IP`
> Max speed gap to allow by-pass action
- Propriétés : Unit=% · Default mode={20}
- Utilisé par : `?Speed OK`, `Adjust group: Master Thermic`, `Single adjust item: Max Speed Gap`
- Ligne export : 19183 · id 63219

#### ?Speed OK  `IDC`
- Propriétés : Toggle=No · Delay on=300 · Delay off=50
- Logique :
  - **Activating** = `Speed error [%] < Max Speed Gap [%]`
- Lit : ``, `Max Speed Gap`, `Speed error`
- Utilisé par : `Measure group: Thermic vs Hydraulic`
- Ligne export : 19195 · id 63208

#### Engine speed to send  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `TSC1 Filter [%]`
- Lit : ``, `TSC1 Filter`
- Utilisé par : `In Engine speed`, `Measure group: Thermic vs Hydraulic`
- Ligne export : 19240 · id 64871

#### Min Speed Ok  `IDC`
> True if engine speed is high enough to face Hydraulic torque. 1000 ms tempo Off to manage temporary deceleration
- Propriétés : Toggle=No · Delay on=0 · Delay off=300
- Logique :
  - **Activating** = `in Speed CAN [rpm] >= In Min Speed acc1 [rpm]`
- Lit : ``, `In Min Speed acc1`, `in Speed CAN`
- Utilisé par : `Inter EV By Pass`, `Measure group: Thermic vs Hydraulic`
- Ligne export : 19282 · id 66440

#### Idle decel filter  `FP`
> Max decel in Idle mode to avoid stall engine
- Propriétés : Mode selector=Engine type · Default mode: EB2 1.2L={10} · Mode 1: FORD 1.5L={100}
- Lit : `Engine type`
- Utilisé par : `Decel Filter`, `Adjust group: Master Thermic`, `Single adjust item: Idle decel filter`
- Ligne export : 19327 · id 66464

#### Accel Filter  `MAC`
> Max Accel selection depending on Speed engine mode
- Propriétés : Unit=%/s · Function selector=SPEED Engine
- Fonction *Default* :
  ```qcode
  Result:= General speed filtering
  ```
- Fonction *Ralenti* :
  ```qcode
  Result:= General speed filtering
  ```
- Fonction *Regime PV* :
  ```qcode
  Result:= General speed filtering
  ```
- Fonction *Régime GV* :
  ```qcode
  Result:= General speed filtering
  ```
- Fonction *Road Cruise* :
  ```qcode
  Result:= General speed filtering
  ```
- Fonction *Regim UP/DOWN* :
  ```qcode
  Result:= General speed filtering
  ```
- Fonction *2200 tr/min* :
  ```qcode
  Result:= General speed filtering
  ```
- Lit : `General speed filtering`, `SPEED Engine`
- Utilisé par : `TSC1 Filter`
- Ligne export : 19341 · id 66465

#### Decel Filter  `MAC`
- Propriétés : Unit=%/s · Function selector=SPEED Engine
- Fonction *Default* :
  ```qcode
  Result:= General speed filtering
  ```
- Fonction *Ralenti* :
  ```qcode
  Result:= Idle decel filter
  ```
- Fonction *Regime PV* :
  ```qcode
  Result:= General speed filtering
  ```
- Fonction *Régime GV* :
  ```qcode
  Result:= General speed filtering
  ```
- Fonction *Road Cruise* :
  ```qcode
  Result:= General speed filtering
  ```
- Fonction *Regim UP/DOWN* :
  ```qcode
  Result:= General speed filtering
  ```
- Fonction *2200 tr/min* :
  ```qcode
  Result:= General speed filtering
  ```
- Lit : `General speed filtering`, `Idle decel filter`, `SPEED Engine`
- Utilisé par : `TSC1 Filter`
- Ligne export : 19407 · id 66476

#### In Min Speed acc1  `FGI`
- Propriétés : Unit=rpm · Input type=Real · Input=Min Speed acc1 [rpm] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Min Speed acc1`
- Utilisé par : `Min Speed Ok`
- Ligne export : 19473 · id 67073

## Thermic / Engine i/o

#### Engine type  `SP`
- Propriétés : Input channel=None · Default state name=EB2 1.2L · States={FORD 1.5L}
- Utilisé par : `Actual engine, % torque`, `Amber warning lamp`, `Engine coolant temp`, `Engine oil pressure`, `FS - Start réduction`, `General speed filtering`, `Hight Speed`, `IDLE Speed`, `Idle decel filter`, `Is_EB2`, `Is_FORD`, `Malfunction lamp`, `Min Speed acc1`, `Min Speed mode`, `Para enclench voyant pression huile`, `Protect lamp`, `Pump Curent  - Hight Speed`, `Pump Curent - Low Speed`, `Pump Curent - Super Low Speed`, `Pump Max curent`, `Red stop lamp`, `Slow Max  Speed`, `Speed CAN`, `Speed Error Calcul`, `Tension/UpDown Speed`, `Water °C Critical`, `Water °C Critical Critical`, `Water °C High`, `Water °C Low`, `torque OR % load at current speed`, `Adjust group: Master Config`, `Single adjust item: Engine type`
- Ligne export : 20454 · id 29442

#### Is_EB2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine type = 0`
- Lit : ``, `Engine type`
- Utilisé par : `Active le groupe: Thermic / Engine i/o / EB2`, `Active le groupe: Thermic / T.Exhaust temp`, `Measure group: Engine Thermic`
- Ligne export : 20466 · id 63325

#### In Engine speed  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Engine speed to send [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Engine speed to send`
- Utilisé par : `In Engine speed to send EB2`, `in Engine speed to send Ford`
- Ligne export : 20511 · id 64880

#### Is_FORD  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine type = 1`
- Lit : ``, `Engine type`
- Utilisé par : `Active le groupe: Thermic / Engine i/o / Ford`, `Measure group: Engine Thermic`
- Ligne export : 21346 · id 63317

#### Malfunction lamp  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Malfunction lamp EB2`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Malfunction lamp Ford`
- Lit : ``, `Engine type`, `Malfunction lamp EB2`, `Malfunction lamp Ford`
- Utilisé par : `Measure group: Engine Thermic`
- Ligne export : 22212 · id 64598

#### Red stop lamp  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Red stop lamp EB2`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Red stop lamp Ford`
- Lit : ``, `Engine type`, `Red stop lamp EB2`, `Red stop lamp Ford`
- Utilisé par : `Measure group: Engine Thermic`
- Ligne export : 22285 · id 64629

#### Amber warning lamp  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Amber warning lamp EB2`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Amber warning lamp Ford`
- Lit : ``, `Amber warning lamp EB2`, `Amber warning lamp Ford`, `Engine type`
- Utilisé par : `Measure group: Engine Thermic`
- Ligne export : 22358 · id 64661

#### Protect lamp  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Protect lamp EB2`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Protect lamp Ford`
- Lit : ``, `Engine type`, `Protect lamp EB2`, `Protect lamp Ford`
- Utilisé par : `Measure group: Engine Thermic`
- Ligne export : 22431 · id 64693

#### Pump Curent - Low Speed  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: EB2 1.2L={900} · Mode 1: FORD 1.5L={900}
- Lit : `Engine type`
- Utilisé par : `In Curent - Low Speed`, `Adjust group: Master Pump`, `Single adjust item: Pump Curent - Low Speed`
- Ligne export : 22504 · id 32147

#### Pump Curent  - Hight Speed  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: EB2 1.2L={1200} · Mode 1: FORD 1.5L={1200}
- Lit : `Engine type`
- Utilisé par : `In Curent  - Hight Speed`, `Adjust group: Master Pump`, `Single adjust item: Pump Curent  - Hight Speed`
- Ligne export : 22518 · id 32148

#### Pump Curent - Super Low Speed  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: EB2 1.2L={660} · Mode 1: FORD 1.5L={660}
- Lit : `Engine type`
- Utilisé par : `In Curent - Super Low Speed`, `Adjust group: Master Pump`, `Single adjust item: Pump Curent - Super Low Speed`
- Ligne export : 22532 · id 32149

#### Pump Max curent  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: EB2 1.2L={1150} · Mode 1: FORD 1.5L={1150}
- Lit : `Engine type`
- Utilisé par : `In Max curent`, `Adjust group: Master Pump`, `Single adjust item: Pump Max curent`
- Ligne export : 22546 · id 32144

#### IDLE Speed  `FP`
> Engine speed when no torque is required
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: EB2 1.2L={1100} · Mode 1: FORD 1.5L={1000}
- Lit : `Engine type`
- Utilisé par : `In IDLE Speed`, `Adjust group: Master Thermic`, `Single adjust item: IDLE Speed`
- Ligne export : 22560 · id 29444

#### Slow Max  Speed  `FP`
> Max engine speed when Joystick is full forward in slow mode
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: EB2 1.2L={2300} · Mode 1: FORD 1.5L={2300}
- Lit : `Engine type`
- Utilisé par : `In Slow Speed`, `Adjust group: Master Thermic`, `Single adjust item: Slow Max  Speed`
- Ligne export : 22574 · id 29445

#### Hight Speed  `FP`
> Max engine speed when joystick is full forward in Fast mode
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: EB2 1.2L={3000} · Mode 1: FORD 1.5L={3000}
- Lit : `Engine type`
- Utilisé par : `In Hight Speed`, `Adjust group: Master Thermic`, `Single adjust item: Hight Speed`
- Ligne export : 22588 · id 29446

#### Tension/UpDown Speed  `FP`
> Target speed to move arms
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: EB2 1.2L={1800} · Mode 1: FORD 1.5L={1700}
- Lit : `Engine type`
- Utilisé par : `In Tension Speed`, `In UP/DOWN Speed`, `Adjust group: Master Thermic`, `Single adjust item: Tension/UpDown Speed`
- Ligne export : 22602 · id 29507

#### Min Speed mode  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: EB2 1.2L={1300} · Mode 1: FORD 1.5L={1200}
- Lit : `Engine type`
- Utilisé par : `In Min Speed mode`, `Adjust group: Master Thermic`, `Single adjust item: Min Speed mode`
- Ligne export : 22616 · id 29508

#### Engine oil pressure  `MAC`
- Propriétés : Unit=kPa · Limiting object group=Signed · Function selector=Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Engine oil pressure EB2 [kPa]`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Engine oil pressure Ford [kPa]`
- Lit : ``, `Engine type`
- Utilisé par : ``, ``, `Engine fluid level/pressure 1 EB2`, `Engine fluid level/pressure 1 Ford`, `in Engine oil pressure`, `Measure group: Engine Thermic`
- Ligne export : 22630 · id 64017

#### torque OR % load at current speed  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `% load at current speed EB2 [%]`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Actual engine, % torque, Ford [%]`
- Lit : ``, `% load at current speed EB2`, `Actual engine, % torque, Ford`, `Engine type`
- Utilisé par : `in % load at current speed`, `Measure group: Engine Thermic`
- Ligne export : 22703 · id 63486

#### Speed Error Calcul  `MAC`
- Propriétés : Unit=% · Function selector=Engine type
- Fonction *EB2 1.2L* :
  ```qcode
  if Speed_RPM_needed  >  0 then
  Speed := 100 - (EB2.Engine speed EB2 / Speed_RPM_needed) * 100
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
- Fonction *FORD 1.5L* :
  ```qcode
  if Speed_RPM_needed  >  0 then
  Speed := 100 - (Ford.Engine speed Ford / Speed_RPM_needed) * 100
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
- Lit : `Engine type`, `Speed_RPM_needed`
- Utilisé par : `in Speed Error Calc`
- Ligne export : 22776 · id 35843

#### Engine coolant temp  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed · Function selector=Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Engine coolant temperature EB2 [°C]`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Engine coolant temperature Ford [°C]`
- Lit : ``, `C`, `Engine type`
- Utilisé par : `in Engine coolant temperature`, `in Engine coolant temperature`, `MD3 page: Thermic`, `Measure group: Engine Thermic`, `Measure group: Engine and Translation`, `Measure group: Temperature`, `Statistics log: Thermic Stats`
- Ligne export : 22826 · id 65141

#### Actual engine, % torque  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Actual engine, % torque EB2 [%]`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Actual engine, % torque, Ford [%]`
- Lit : ``, `Actual engine, % torque EB2`, `Actual engine, % torque, Ford`, `Engine type`
- Utilisé par : `Measure group: Engine Thermic`, `Measure group: Engine and Translation`
- Ligne export : 22899 · id 65178

#### Speed CAN  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed · Function selector=Engine type
- Fonction *EB2 1.2L* :
  - **Controlling** = `Engine speed EB2 [rpm]`
- Fonction *FORD 1.5L* :
  - **Controlling** = `Engine speed Ford [rpm]`
- Lit : ``, `Engine speed EB2`, `Engine speed Ford`, `Engine type`
- Utilisé par : `Engine_Started`, `in Speed CAN`, `Measure group: Engine Thermic`, `Measure group: Engine and Translation`, `Measure group: Hydraulic`, `Measure group: Thermic vs Hydraulic`
- Ligne export : 22978 · id 65507

#### Min Speed acc1  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: EB2 1.2L={1550} · Mode 1: FORD 1.5L={1200}
- Lit : `Engine type`
- Utilisé par : `In Min Speed acc1`, `Adjust group: Master Thermic`, `Single adjust item: Min Speed acc1`
- Ligne export : 23058 · id 67067

## Thermic / Engine i/o / EB2 — actif seulement si `Is_EB2`

#### DM1  `DM1IN`
> Diagnostic Message 1
- Propriétés : SPN conversion method=4 · FMI texts={OK; Above normal, most severe; Below normal, most severe; Erratic or intermittent; Voltage above normal; Voltage below normal; Current below normal; Current above normal; Out of adjustment; Abnormal frequency; Abnormal update rate; Abnormal rate of change; Root cause not known; Bad component; Out of calibration; Special instructions; Above normal; Above normal, severe; Below normal; Below normal, severe; Received data in error; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Not available} · Show message=All · Dialog for undefined SPNs=Yes · Enable DM2 support=False · Enable lamp flash=No · Parameters={SPN 98; SPN 100; SPN 102; SPN 105; SPN 106; SPN 110; SPN 175; SPN 626; SPN 629; SPN 636; SPN 637; SPN 639; SPN 651; SPN 652; SPN 653; SPN 654; SPN 655; SPN 656; SPN 677; SPN 1485} · Module=Inboard Engine EB2 (J1939[0]) · Module index=0
- Lit : `SPN 100`, `SPN 102`, `SPN 105`, `SPN 106`, `SPN 110`, `SPN 1485`, `SPN 175`, `SPN 626`, `SPN 629`, `SPN 636`, `SPN 637`, `SPN 639`, `SPN 651`, `SPN 652`, `SPN 653`, `SPN 654`, `SPN 655`, `SPN 656`, `SPN 677`, `SPN 98`
- Utilisé par : *(personne)*
- Ligne export : 20550 · id 29039

#### SPN 629  `SPN`
> Controller #1
- Propriétés : SPN=629 · Dialog priority=Critical · Failures={{8; ErrNo 186 DTC 9.9: CPU Watchdog reset test failure.}; {13; ErrNo 186 DTC 9.9: Watchdog trip failure.}; {2; ErrNo 187 DTC 9.9: RAM cell test failure.}; {12; ErrNo 187 DTC 9.9: RAM address test failure.}; {11; ErrNo 186 DTC 9.9: Main and Fueling ASIC test fail.}}
- Utilisé par : `DM1`
- Ligne export : 20620 · id 29040

#### SPN 100  `SPN`
> Engine Oil Pressure
- Propriétés : SPN=100 · Dialog priority=Warning · Failures={{3; ErrNo 181 DTC 3.1: Voltage above normal.}; {4; ErrNo 182 DTC 3.1: Voltage below normal.}; {1; ErrNo 180 DTC 6.6: Data valid but below normal.}}
- Utilisé par : `DM1`
- Ligne export : 20646 · id 29041

#### SPN 110  `SPN`
> Engine Coolant Temperature
- Propriétés : SPN=110 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 20666 · id 29042

#### SPN 105  `SPN`
> Air Intake Manifold 1 Temperature
- Propriétés : SPN=105 · Dialog priority=Warning · Failures={{3; ErrNo 25 DTC 3.2: Voltage above normal.}; {4; ErrNo 26 DTC 3.2: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 20686 · id 29043

#### SPN 175  `SPN`
> Engine Oil Temperature 1
- Propriétés : SPN=175 · Dialog priority=Critical · Failures={{3; ErrNo 184 DTC 3.7: Voltage above normal.}; {4; ErrNo 185 DTC 3.7: Voltage below normal.}; {0; ErrNo 183 DTC 5.8: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 20706 · id 29044

#### SPN 102  `SPN`
> Boost Pressure
- Propriétés : SPN=102 · Dialog priority=Warning · Failures={{3; ErrNo 67 DTC 3.4: Voltage above normal.}; {4; ErrNo 68 DTC 3.4: Voltage below normal.}; {0; ErrNo 57 DTC -.-: Data valid but above normal.}; {1; ErrNo 58 DTC -.-: Data valid but below normal.}}
- Utilisé par : `DM1`
- Ligne export : 20726 · id 29045

#### SPN 1485  `SPN`
> ECU Main relay
- Propriétés : SPN=1485 · Dialog priority=Warning · Failures={{3; ErrNo 43 DTC 5.1: Short circuit high.}}
- Utilisé par : `DM1`
- Ligne export : 20749 · id 29046

#### SPN 637  `SPN`
> Timing sensor
- Propriétés : SPN=637 · Dialog priority=Warning · Failures={{8; ErrNo 18 DTC 2.4: Extra pulses.}; {2; ErrNo 101 DTC 2.4: Intermittent loss of signal.}; {3; ErrNo 18 DTC 2.4: Permanent loss of signal.}}
- Utilisé par : `DM1`
- Ligne export : 20763 · id 29047

#### SPN 656  `SPN`
> Injector Cylinder #06
- Propriétés : SPN=656 · Dialog priority=Warning · Failures={{2; ErrNo 160 DTC 7.6: Short circuit High Side to Vbatt.}; {4; ErrNo 161 DTC 7.6: Short circuit High or Low Side to ground.}; {3; ErrNo 162 DTC 7.6: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 165 DTC 7.6: Open circuit.}; {11; ErrNo 163 DTC 7.6: Unknown Error.}; {7; ErrNo 164 DTC 7.6: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 20783 · id 29048

#### SPN 636  `SPN`
> Engine position sensor
- Propriétés : SPN=636 · Dialog priority=Critical · Failures={{8; ErrNo 103 DTC 2.5: Extra pulses or high frequency signal.}; {3; ErrNo 102 DTC 2.5: Permanent loss of signal.}}
- Utilisé par : `DM1`
- Ligne export : 20812 · id 29049

#### SPN 626  `SPN`
> Start enable device - Devices that assist an engine in starting - e.g. intake heaters and ether
- Propriétés : SPN=626 · Dialog priority=Warning · Failures={{3; ErrNo 76 DTC 5.4: Voltage above normal.}; {4; ErrNo 75 DTC 5.4: Voltage below normal.}; {5; ErrNo 74 DTC 5.4: Current below normal.}}
- Utilisé par : `DM1`
- Ligne export : 20829 · id 29050

#### SPN 677  `SPN`
> Engine Starter Motor Relay
- Propriétés : SPN=677 · Dialog priority=Warning · Failures={{3; ErrNo 41 DTC 4.6: Short circuit high.}; {4; ErrNo 42 DTC 4.6: Short circuit low.}; {5; ErrNo 107 DTC 4.6: Open circuit.}}
- Utilisé par : `DM1`
- Ligne export : 20849 · id 29051

#### SPN 655  `SPN`
> Injector Cylinder #05
- Propriétés : SPN=655 · Dialog priority=Warning · Failures={{2; ErrNo 150 DTC 7.5: Short circuit High Side to Vbatt.}; {4; ErrNo 151 DTC 7.5: Short circuit High or Low Side to ground.}; {3; ErrNo 152 DTC 7.5: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 155 DTC 7.5: Open circuit.}; {11; ErrNo 153 DTC 7.5: Unknown Error.}; {7; ErrNo 154 DTC 7.5: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 20869 · id 29052

#### SPN 654  `SPN`
> Injector Cylinder #04
- Propriétés : SPN=654 · Dialog priority=Warning · Failures={{2; ErrNo 140 DTC 7.4: Short circuit High Side to Vbatt.}; {4; ErrNo 141 DTC 7.4: Short circuit High or Low Side to ground.}; {3; ErrNo 142 DTC 7.4: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 145 DTC 7.4: Open circuit.}; {11; ErrNo 143 DTC 7.4: Unknown Error.}; {7; ErrNo 144 DTC 7.4: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 20898 · id 29053

#### SPN 653  `SPN`
> Injector Cylinder #03
- Propriétés : SPN=653 · Dialog priority=Warning · Failures={{2; ErrNo 130 DTC 7.3: Short circuit High Side to Vbatt.}; {4; ErrNo 131 DTC 7.3: Short circuit High or Low Side to ground.}; {3; ErrNo 132 DTC 7.3: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 135 DTC 7.3: Open circuit.}; {11; ErrNo 133 DTC 7.3: Unknown Error.}; {7; ErrNo 134 DTC 7.3: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 20927 · id 29054

#### SPN 652  `SPN`
> Injector Cylinder #02
- Propriétés : SPN=652 · Dialog priority=Warning · Failures={{2; ErrNo 120 DTC 7.2: Short circuit High Side to Vbatt.}; {4; ErrNo 121 DTC 7.2: Short circuit High or Low Side to ground.}; {3; ErrNo 122 DTC 7.2: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 125 DTC 7.2: Open circuit.}; {11; ErrNo 123 DTC 7.2: Unknown Error.}; {7; ErrNo 124 DTC 7.2: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 20956 · id 29055

#### SPN 651  `SPN`
> Injector Cylinder #01
- Propriétés : SPN=651 · Dialog priority=Warning · Failures={{2; ErrNo 110 DTC 7.1: Short circuit High Side to Vbatt.}; {4; ErrNo 111 DTC 7.1: Short circuit High or Low Side to ground.}; {3; ErrNo 112 DTC 7.1: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 115 DTC 7.1: Open circuit.}; {11; ErrNo 113 DTC 7.1: Unknown Error.}; {7; ErrNo 114 DTC 7.1: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 20985 · id 29056

#### SPN 639  `SPN`
> J1939 Network #1, Primary Vehicle Network
- Propriétés : SPN=639 · Dialog priority=Warning · Failures={{2; ErrNo 106 DTC 6.5: Bus Off error.}; {9; ErrNo 106 DTC 6.5: Passive bus error.}; {12; ErrNo 38 DTC 6.5: Loss of message error.}; {11; ErrNo 38 DTC 6.5: Data registers read back failure.}}
- Utilisé par : `DM1`
- Ligne export : 21014 · id 29057

#### Malfunction lamp EB2  `MDGN`
- Propriétés : Value=Malfunction · Module=Inboard Engine EB2 (J1939[0]) · Module index=1
- Utilisé par : `Malfunction lamp`
- Ligne export : 21037 · id 29058

#### Red stop lamp EB2  `MDGN`
- Propriétés : Value=Red stop · Module=Inboard Engine EB2 (J1939[0]) · Module index=2
- Utilisé par : `Red stop lamp`
- Ligne export : 21048 · id 29059

#### Amber warning lamp EB2  `MDGN`
- Propriétés : Value=Amber warning · Module=Inboard Engine EB2 (J1939[0]) · Module index=3
- Utilisé par : `Amber warning lamp`
- Ligne export : 21059 · id 29060

#### Protect lamp EB2  `MDGN`
- Propriétés : Value=Protect · Module=Inboard Engine EB2 (J1939[0]) · Module index=4
- Utilisé par : `Protect lamp`
- Ligne export : 21070 · id 29061

#### SPN 98  `SPN`
> Engine oil level
- Propriétés : SPN=98 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 21081 · id 29062

#### SPN 106  `SPN`
- Propriétés : SPN=106 · Dialog priority=Dont show · Failures={{4; MAP Voltage Low}}
- Utilisé par : `DM1`
- Ligne export : 21101 · id 29063

#### In Engine speed to send EB2  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=In Engine speed [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `In Engine speed`
- Utilisé par : `TSC1-A:J1939-0 EB2`
- Ligne export : 21115 · id 64878

#### TSC1-A:J1939-0 EB2  `TSC1`
- Propriétés : J1939 source address=3 · Engine speed limits={1000; 4000} · Speed channel=In Engine speed to send EB2 [%] · Priority=3 · Transmit rate=20 · Override control mode=Speed control · Speed control conditions=Transient optimized, disengaged · Override control mode priority=Highest · Use checksum/counter=No · Control purpose=P32 = Temporary Powertrain Control (Original use of TSC1 Command) · Module=Inboard Engine EB2 (J1939[0]) · Module index=0
- Lit : `In Engine speed to send EB2`
- Utilisé par : `Measure group: Engine Thermic`
- Ligne export : 21129 · id 29582

#### EEC1 EB2  `JFIN`
> Electronic Engine Controller 1
- Propriétés : Priority=6 · PGN=61444 · Timeout=3000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Driver's demand, engine % EB2 [%]; 9}; {Actual engine, % torque EB2 [%]; 17}; {Engine speed EB2 [rpm]; 25}} · Module=Inboard Engine EB2 (J1939[0]) · Module index=0
- Lit : `Actual engine, % torque EB2`, `Driver's demand, engine % EB2`, `Engine speed EB2`
- Utilisé par : *(personne)*
- Ligne export : 21152 · id 29983

#### Driver's demand, engine % EB2  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `EEC1 EB2`
- Ligne export : 21179 · id 29984

#### Actual engine, % torque EB2  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `Actual engine, % torque`, `EEC1 EB2`
- Ligne export : 21193 · id 29985

#### Engine speed EB2  `JPIN`
- Propriétés : Unit=rpm · Length=2 Bytes (= 16 bits) · J1939 Error check=Yes · Resolution=0,125 · Offset=0 · Error value=0
- Utilisé par : `EEC1 EB2`, `Speed CAN`
- Ligne export : 21207 · id 29986

#### EEC2 EB2  `JFIN`
> Electronic Engine Controller 2
- Propriétés : Priority=6 · PGN=61443 · Timeout=3000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Accelerator pedal position EB2 [%]; 9}; {% load at current speed EB2 [%]; 17}} · Module=Inboard Engine EB2 (J1939[0]) · Module index=4
- Lit : `% load at current speed EB2`, `Accelerator pedal position EB2`
- Utilisé par : *(personne)*
- Ligne export : 21221 · id 29987

#### Accelerator pedal position EB2  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=0,4 · Offset=0 · Error value=0
- Utilisé par : `EEC2 EB2`
- Ligne export : 21245 · id 29988

#### % load at current speed EB2  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `EEC2 EB2`, `torque OR % load at current speed`
- Ligne export : 21259 · id 29989

#### Engine Temperature EB 2  `JFIN`
> ET1
- Propriétés : Priority=6 · PGN=65262 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine coolant temperature EB2 [°C]; 1}} · Module=Inboard Engine EB2 (J1939[0]) · Module index=1
- Lit : `C`
- Utilisé par : *(personne)*
- Ligne export : 21273 · id 29977

####   `JPIN`
- Propriétés : Name, English=Engine coolant temperature EB2 · Unit=°C · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-40 · Error value=0
- Utilisé par : `10 hours check-up`, `?Speed OK`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Activate Critical State`, `Activate High Aft Fan`, `Activate High Aft Fan`, `Activate Low Aft Fan`, `Activate Low Aft Fan`, `Activate exhaust Fan`, `Activate exhaust Fan`, `Actual engine, % torque`, `Adress Loose`, `Adress_Search`, `Adresse_Mem`, `Alert critical engine`, `Alert critical exhaust`, `Alert critical hydraulic`, `Allow Cruise`, `Allow Run Cruise`, `Amber warning lamp`, `Auto Fast after Down`, `Auto Fast after Down Wait`, `Auto Off Bip`, `Auto PAUSE/OFF`, `Auto Stop Timer`, `AutoStopafter 5 secondes`, `Backlight Value`, `Backward Curent`, `Bad pressure`, `Bip`, `Brake Activation`, `C`, `Calcul Accélération`, `CanBus Error TB`, `Command State`, `Couché night`, `Counter`, `Coupure Thermique avec sécurité`, `Critical Temp Timer`, `Current Date MEN`, `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `DOWN Counter`, `Days in current year`, `Dec`, `Digit Engine On`, `Don'push button`, `Duree`, `ENGINE RUN`, `ENGINE RUN`, `ET`, `ET h`, `EV tendre Chenille`, `Engine Stopped`, `Engine Thermal State`, `Engine coolant temp`, `Engine hours`, `Engine oil pressure`, `Engine speed to send`, `Engine_Started`, `Force Lock`, `Force Unlock`, `Forward Curent`, `Fuel Line Timer`, `Fuel line ignition`, `Fuel line ignition`, `Fuel line ignition IDC`, `Fuel line ignition Output`, `GPS Adresse Find`, `GPS_Adresse_Find_Int`, `Garmin - NMEA`, `HIGH arm`, `High Temp Timer`, `Ho`, `Ho_night`, `Hot Oil`, `Hour actual`, `Hydraulic pump statut`, `Hydraulics Temperature State`, `ID Fault`, `ID Prog`, `IDC Auto Sleep`, `IDC EV By Pass`, `IDC EV By Pass Down`, `IDC EV By Pass sel`, `IDC Free`, `IDC Speed Free`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `IDC Tension`, `Iguana PIN`, `Inter Allumage Thermique`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter EV By Pass`, `Inter EV DOWN`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP`, `Inter EV UP Delay`, `Inter EV Verin`, `Inter Lock landing`, `Inter Tension`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Inter Unlock`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Is_EB2`, `Is_FORD`, `Joystick Zero`, `Joystick is not in neutral position`, `Joystick not zero`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `K1 Fan Rear / Fan`, `K1 fuse is blown`, `K10`, `K10 fuse is blown`, `K11`, `K11 fuse is blown`, `K12`, `K12 fuse is blown`, `K13`, `K13 fuse is blown`, `K2 Fan Super / Pump`, `K2 fuse is blown`, `K3 Fan Exhaust / AutoOff`, `K3 fuse is blown`, `K4 Engine Power / Search Lights`, `K4 fuse is blown`, `K5 Engine Start`, `K5 fuse is blown`, `K6 Engine Water Pump`, `K6 fuse is blown`, `K7 Exhaust Water Pump`, `K7 fuse is blown`, `K8`, `K8 fuse is blown`, `K9`, `K9 fuse is blown`, `KeyBox Can Ok`, `Ko to move`, `L`, `LOW arm`, `Latence Math`, `LatenceTimer`, `Latitude Compute`, `Latitude Compute MEN`, `Levé night`, `Lock`, `Lock landing`, `Lon`, `Longitude Compute`, `Longitude Compute MEN`, `Low Temp Timer`, `M`, `MD3 - DOWN`, `MD3 - UP`, `MD3 START`, `MD3 STOP`, `MD3 start last checks`, `MDGN-+BAT:MC2[1]`, `Malfunction lamp`, `Manual Start Engine Pulse IDC`, `Math Droit`, `Math Gauche`, `Max Manip`, `Mid Temp Timer`, `Min Speed Ok`, `Mini Wait`, `Méridian`, `Need Min Speed`, `New Timer`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `OK UP/DOWN`, `Oil Security Activation`, `Oil pressure`, `Ok to move`, `Out START Engine`, `Out SWITCH ON Engine`, `PIN 44`, `PIn State`, `Persistant Water Temp`, `Power State Int`, `Pre Fuel line ignition IDC`, `Process Down Engine`, `Progress`, `Protect lamp`, `Pump 1 Right`, `Pump 1 Right Filter ECC1`, `Pump 2 Left`, `Pump 2 Left Filter ECC1`, `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Red stop lamp`, `Reset`, `Reset Speed`, `Reset Startup`, `Reset on startup`, `SPEED Engine`, `STARTING`, `Show Debug`, `Show P-1-2`, `Speed CAN`, `Speed Data remapping`, `Speed Int`, `Speed Mode`, `Speed Pump`, `Speed State`, `Speed_RPM_needed`, `Starter Proctection IDC`, `Starter Protection`, `Starter Protection CMSG`, `State`, `State All Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `State Up/Down`, `State Up/Down Raw`, `Stop Cruise`, `Stop To Move`, `Store TIMER UP/DOWN`, `Sunrise`, `Sunset`, `System Started DELAYS`, `TRACK DOWN`, `TRACK UP`, `Temperature State`, `Thermic Engine STATE`, `Time_Diff_MEM`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer UP/DOWN`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Toggle Free`, `Track DOWN Delay`, `Track UP Delay`, `Trigger`, `Trigger HeartBeat`, `Trigger Speed`, `Trigger Timer`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `Unlock`, `Unlock landing`, `VIEW BUTTON States`, `VIEW ENGINE RUN PAGE`, `VIEW SPEED STATE`, `VIEW START PAGE`, `Voyant Pression Huile Moteur`, `Wait Bad Pressure`, `Wait Buz 2`, `Wait Hot Temperature`, `Wait after stating`, `Works Latitude`, `Year since 2000`, `oldExhaust Temperature State`, `out T Exhaust Temps`, `torque OR % load at current speed`, `Event log: Check UP`, `Event log: Hydraulic Event`, `Event log: Thermic Events`, `Statistics log: System Stats`, `Statistics log: Thermic Stats`
- Ligne export : 21294 · id 29979

#### Engine fluid level/pressure 1 EB2  `JFIN`
> EFL/P1
- Propriétés : Priority=6 · PGN=65263 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine oil pressure EB2 [kPa]; 25}} · Module=Inboard Engine EB2 (J1939[0]) · Module index=3
- Lit : `Engine oil pressure`
- Utilisé par : *(personne)*
- Ligne export : 21309 · id 29981

####   `JPIN`
- Propriétés : Name, English=Engine oil pressure EB2 · Unit=kPa · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=4 · Offset=0 · Error value=0
- Lit : `Engine oil pressure`
- Utilisé par : `10 hours check-up`, `?Speed OK`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Activate Critical State`, `Activate High Aft Fan`, `Activate High Aft Fan`, `Activate Low Aft Fan`, `Activate Low Aft Fan`, `Activate exhaust Fan`, `Activate exhaust Fan`, `Actual engine, % torque`, `Adress Loose`, `Adress_Search`, `Adresse_Mem`, `Alert critical engine`, `Alert critical exhaust`, `Alert critical hydraulic`, `Allow Cruise`, `Allow Run Cruise`, `Amber warning lamp`, `Auto Fast after Down`, `Auto Fast after Down Wait`, `Auto Off Bip`, `Auto PAUSE/OFF`, `Auto Stop Timer`, `AutoStopafter 5 secondes`, `Backlight Value`, `Backward Curent`, `Bad pressure`, `Bip`, `Brake Activation`, `C`, `Calcul Accélération`, `CanBus Error TB`, `Command State`, `Couché night`, `Counter`, `Coupure Thermique avec sécurité`, `Critical Temp Timer`, `Current Date MEN`, `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `DOWN Counter`, `Days in current year`, `Dec`, `Digit Engine On`, `Don'push button`, `Duree`, `ENGINE RUN`, `ENGINE RUN`, `ET`, `ET h`, `EV tendre Chenille`, `Engine Stopped`, `Engine Thermal State`, `Engine coolant temp`, `Engine hours`, `Engine oil pressure`, `Engine speed to send`, `Engine_Started`, `Force Lock`, `Force Unlock`, `Forward Curent`, `Fuel Line Timer`, `Fuel line ignition`, `Fuel line ignition`, `Fuel line ignition IDC`, `Fuel line ignition Output`, `GPS Adresse Find`, `GPS_Adresse_Find_Int`, `Garmin - NMEA`, `HIGH arm`, `High Temp Timer`, `Ho`, `Ho_night`, `Hot Oil`, `Hour actual`, `Hydraulic pump statut`, `Hydraulics Temperature State`, `ID Fault`, `ID Prog`, `IDC Auto Sleep`, `IDC EV By Pass`, `IDC EV By Pass Down`, `IDC EV By Pass sel`, `IDC Free`, `IDC Speed Free`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `IDC Tension`, `Iguana PIN`, `Inter Allumage Thermique`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter EV By Pass`, `Inter EV DOWN`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP`, `Inter EV UP Delay`, `Inter EV Verin`, `Inter Lock landing`, `Inter Tension`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Inter Unlock`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Is_EB2`, `Is_FORD`, `Joystick Zero`, `Joystick is not in neutral position`, `Joystick not zero`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `K1 Fan Rear / Fan`, `K1 fuse is blown`, `K10`, `K10 fuse is blown`, `K11`, `K11 fuse is blown`, `K12`, `K12 fuse is blown`, `K13`, `K13 fuse is blown`, `K2 Fan Super / Pump`, `K2 fuse is blown`, `K3 Fan Exhaust / AutoOff`, `K3 fuse is blown`, `K4 Engine Power / Search Lights`, `K4 fuse is blown`, `K5 Engine Start`, `K5 fuse is blown`, `K6 Engine Water Pump`, `K6 fuse is blown`, `K7 Exhaust Water Pump`, `K7 fuse is blown`, `K8`, `K8 fuse is blown`, `K9`, `K9 fuse is blown`, `KeyBox Can Ok`, `Ko to move`, `L`, `LOW arm`, `Latence Math`, `LatenceTimer`, `Latitude Compute`, `Latitude Compute MEN`, `Levé night`, `Lock`, `Lock landing`, `Lon`, `Longitude Compute`, `Longitude Compute MEN`, `Low Temp Timer`, `M`, `MD3 - DOWN`, `MD3 - UP`, `MD3 START`, `MD3 STOP`, `MD3 start last checks`, `MDGN-+BAT:MC2[1]`, `Malfunction lamp`, `Manual Start Engine Pulse IDC`, `Math Droit`, `Math Gauche`, `Max Manip`, `Mid Temp Timer`, `Min Speed Ok`, `Mini Wait`, `Méridian`, `Need Min Speed`, `New Timer`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `OK UP/DOWN`, `Oil Security Activation`, `Oil pressure`, `Ok to move`, `Out START Engine`, `Out SWITCH ON Engine`, `PIN 44`, `PIn State`, `Persistant Water Temp`, `Power State Int`, `Pre Fuel line ignition IDC`, `Process Down Engine`, `Progress`, `Protect lamp`, `Pump 1 Right`, `Pump 1 Right Filter ECC1`, `Pump 2 Left`, `Pump 2 Left Filter ECC1`, `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Red stop lamp`, `Reset`, `Reset Speed`, `Reset Startup`, `Reset on startup`, `SPEED Engine`, `STARTING`, `Show Debug`, `Show P-1-2`, `Speed CAN`, `Speed Data remapping`, `Speed Int`, `Speed Mode`, `Speed Pump`, `Speed State`, `Speed_RPM_needed`, `Starter Proctection IDC`, `Starter Protection`, `Starter Protection CMSG`, `State`, `State All Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `State Up/Down`, `State Up/Down Raw`, `Stop Cruise`, `Stop To Move`, `Store TIMER UP/DOWN`, `Sunrise`, `Sunset`, `System Started DELAYS`, `TRACK DOWN`, `TRACK UP`, `Temperature State`, `Thermic Engine STATE`, `Time_Diff_MEM`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer UP/DOWN`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Toggle Free`, `Track DOWN Delay`, `Track UP Delay`, `Trigger`, `Trigger HeartBeat`, `Trigger Speed`, `Trigger Timer`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `Unlock`, `Unlock landing`, `VIEW BUTTON States`, `VIEW ENGINE RUN PAGE`, `VIEW SPEED STATE`, `VIEW START PAGE`, `Voyant Pression Huile Moteur`, `Wait Bad Pressure`, `Wait Buz 2`, `Wait Hot Temperature`, `Wait after stating`, `Works Latitude`, `Year since 2000`, `oldExhaust Temperature State`, `out T Exhaust Temps`, `torque OR % load at current speed`, `Event log: Check UP`, `Event log: Hydraulic Event`, `Event log: Thermic Events`, `Statistics log: System Stats`, `Statistics log: Thermic Stats`
- Ligne export : 21330 · id 29982

## Thermic / Engine i/o / Ford — actif seulement si `Is_FORD`

#### DM1  `DM1IN`
> Diagnostic Message 1
- Propriétés : SPN conversion method=4 · FMI texts={OK; Above normal, most severe; Below normal, most severe; Erratic or intermittent; Voltage above normal; Voltage below normal; Current below normal; Current above normal; Out of adjustment; Abnormal frequency; Abnormal update rate; Abnormal rate of change; Root cause not known; Bad component; Out of calibration; Special instructions; Above normal; Above normal, severe; Below normal; Below normal, severe; Received data in error; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Not available} · Show message=All · Dialog for undefined SPNs=Yes · Enable DM2 support=False · Enable lamp flash=No · Parameters={SPN 98; SPN 100; SPN 102; SPN 105; SPN 106; SPN 110; SPN 175; SPN 626; SPN 629; SPN 636; SPN 637; SPN 639; SPN 651; SPN 652; SPN 653; SPN 654; SPN 655; SPN 656; SPN 677; SPN 1485} · Module=Inboard Engine Ford (J1939[0]) · Module index=0
- Lit : `SPN 100`, `SPN 102`, `SPN 105`, `SPN 106`, `SPN 110`, `SPN 1485`, `SPN 175`, `SPN 626`, `SPN 629`, `SPN 636`, `SPN 637`, `SPN 639`, `SPN 651`, `SPN 652`, `SPN 653`, `SPN 654`, `SPN 655`, `SPN 656`, `SPN 677`, `SPN 98`
- Utilisé par : *(personne)*
- Ligne export : 21416 · id 64066

#### SPN 629  `SPN`
> Controller #1
- Propriétés : SPN=629 · Dialog priority=Critical · Failures={{8; ErrNo 186 DTC 9.9: CPU Watchdog reset test failure.}; {13; ErrNo 186 DTC 9.9: Watchdog trip failure.}; {2; ErrNo 187 DTC 9.9: RAM cell test failure.}; {12; ErrNo 187 DTC 9.9: RAM address test failure.}; {11; ErrNo 186 DTC 9.9: Main and Fueling ASIC test fail.}}
- Utilisé par : `DM1`
- Ligne export : 21486 · id 64067

#### SPN 100  `SPN`
> Engine Oil Pressure
- Propriétés : SPN=100 · Dialog priority=Warning · Failures={{3; ErrNo 181 DTC 3.1: Voltage above normal.}; {4; ErrNo 182 DTC 3.1: Voltage below normal.}; {1; ErrNo 180 DTC 6.6: Data valid but below normal.}}
- Utilisé par : `DM1`
- Ligne export : 21512 · id 64068

#### SPN 110  `SPN`
> Engine Coolant Temperature
- Propriétés : SPN=110 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 21532 · id 64069

#### SPN 105  `SPN`
> Air Intake Manifold 1 Temperature
- Propriétés : SPN=105 · Dialog priority=Warning · Failures={{3; ErrNo 25 DTC 3.2: Voltage above normal.}; {4; ErrNo 26 DTC 3.2: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 21552 · id 64070

#### SPN 175  `SPN`
> Engine Oil Temperature 1
- Propriétés : SPN=175 · Dialog priority=Critical · Failures={{3; ErrNo 184 DTC 3.7: Voltage above normal.}; {4; ErrNo 185 DTC 3.7: Voltage below normal.}; {0; ErrNo 183 DTC 5.8: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 21572 · id 64071

#### SPN 102  `SPN`
> Boost Pressure
- Propriétés : SPN=102 · Dialog priority=Warning · Failures={{3; ErrNo 67 DTC 3.4: Voltage above normal.}; {4; ErrNo 68 DTC 3.4: Voltage below normal.}; {0; ErrNo 57 DTC -.-: Data valid but above normal.}; {1; ErrNo 58 DTC -.-: Data valid but below normal.}}
- Utilisé par : `DM1`
- Ligne export : 21592 · id 64072

#### SPN 1485  `SPN`
> ECU Main relay
- Propriétés : SPN=1485 · Dialog priority=Warning · Failures={{3; ErrNo 43 DTC 5.1: Short circuit high.}}
- Utilisé par : `DM1`
- Ligne export : 21615 · id 64073

#### SPN 637  `SPN`
> Timing sensor
- Propriétés : SPN=637 · Dialog priority=Warning · Failures={{8; ErrNo 18 DTC 2.4: Extra pulses.}; {2; ErrNo 101 DTC 2.4: Intermittent loss of signal.}; {3; ErrNo 18 DTC 2.4: Permanent loss of signal.}}
- Utilisé par : `DM1`
- Ligne export : 21629 · id 64074

#### SPN 656  `SPN`
> Injector Cylinder #06
- Propriétés : SPN=656 · Dialog priority=Warning · Failures={{2; ErrNo 160 DTC 7.6: Short circuit High Side to Vbatt.}; {4; ErrNo 161 DTC 7.6: Short circuit High or Low Side to ground.}; {3; ErrNo 162 DTC 7.6: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 165 DTC 7.6: Open circuit.}; {11; ErrNo 163 DTC 7.6: Unknown Error.}; {7; ErrNo 164 DTC 7.6: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 21649 · id 64075

#### SPN 636  `SPN`
> Engine position sensor
- Propriétés : SPN=636 · Dialog priority=Critical · Failures={{8; ErrNo 103 DTC 2.5: Extra pulses or high frequency signal.}; {3; ErrNo 102 DTC 2.5: Permanent loss of signal.}}
- Utilisé par : `DM1`
- Ligne export : 21678 · id 64076

#### SPN 626  `SPN`
> Start enable device - Devices that assist an engine in starting - e.g. intake heaters and ether
- Propriétés : SPN=626 · Dialog priority=Warning · Failures={{3; ErrNo 76 DTC 5.4: Voltage above normal.}; {4; ErrNo 75 DTC 5.4: Voltage below normal.}; {5; ErrNo 74 DTC 5.4: Current below normal.}}
- Utilisé par : `DM1`
- Ligne export : 21695 · id 64077

#### SPN 677  `SPN`
> Engine Starter Motor Relay
- Propriétés : SPN=677 · Dialog priority=Warning · Failures={{3; ErrNo 41 DTC 4.6: Short circuit high.}; {4; ErrNo 42 DTC 4.6: Short circuit low.}; {5; ErrNo 107 DTC 4.6: Open circuit.}}
- Utilisé par : `DM1`
- Ligne export : 21715 · id 64078

#### SPN 655  `SPN`
> Injector Cylinder #05
- Propriétés : SPN=655 · Dialog priority=Warning · Failures={{2; ErrNo 150 DTC 7.5: Short circuit High Side to Vbatt.}; {4; ErrNo 151 DTC 7.5: Short circuit High or Low Side to ground.}; {3; ErrNo 152 DTC 7.5: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 155 DTC 7.5: Open circuit.}; {11; ErrNo 153 DTC 7.5: Unknown Error.}; {7; ErrNo 154 DTC 7.5: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 21735 · id 64079

#### SPN 654  `SPN`
> Injector Cylinder #04
- Propriétés : SPN=654 · Dialog priority=Warning · Failures={{2; ErrNo 140 DTC 7.4: Short circuit High Side to Vbatt.}; {4; ErrNo 141 DTC 7.4: Short circuit High or Low Side to ground.}; {3; ErrNo 142 DTC 7.4: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 145 DTC 7.4: Open circuit.}; {11; ErrNo 143 DTC 7.4: Unknown Error.}; {7; ErrNo 144 DTC 7.4: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 21764 · id 64080

#### SPN 653  `SPN`
> Injector Cylinder #03
- Propriétés : SPN=653 · Dialog priority=Warning · Failures={{2; ErrNo 130 DTC 7.3: Short circuit High Side to Vbatt.}; {4; ErrNo 131 DTC 7.3: Short circuit High or Low Side to ground.}; {3; ErrNo 132 DTC 7.3: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 135 DTC 7.3: Open circuit.}; {11; ErrNo 133 DTC 7.3: Unknown Error.}; {7; ErrNo 134 DTC 7.3: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 21793 · id 64081

#### SPN 652  `SPN`
> Injector Cylinder #02
- Propriétés : SPN=652 · Dialog priority=Warning · Failures={{2; ErrNo 120 DTC 7.2: Short circuit High Side to Vbatt.}; {4; ErrNo 121 DTC 7.2: Short circuit High or Low Side to ground.}; {3; ErrNo 122 DTC 7.2: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 125 DTC 7.2: Open circuit.}; {11; ErrNo 123 DTC 7.2: Unknown Error.}; {7; ErrNo 124 DTC 7.2: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 21822 · id 64082

#### SPN 651  `SPN`
> Injector Cylinder #01
- Propriétés : SPN=651 · Dialog priority=Warning · Failures={{2; ErrNo 110 DTC 7.1: Short circuit High Side to Vbatt.}; {4; ErrNo 111 DTC 7.1: Short circuit High or Low Side to ground.}; {3; ErrNo 112 DTC 7.1: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 115 DTC 7.1: Open circuit.}; {11; ErrNo 113 DTC 7.1: Unknown Error.}; {7; ErrNo 114 DTC 7.1: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 21851 · id 64083

#### SPN 639  `SPN`
> J1939 Network #1, Primary Vehicle Network
- Propriétés : SPN=639 · Dialog priority=Warning · Failures={{2; ErrNo 106 DTC 6.5: Bus Off error.}; {9; ErrNo 106 DTC 6.5: Passive bus error.}; {12; ErrNo 38 DTC 6.5: Loss of message error.}; {11; ErrNo 38 DTC 6.5: Data registers read back failure.}}
- Utilisé par : `DM1`
- Ligne export : 21880 · id 64084

#### Malfunction lamp Ford  `MDGN`
- Propriétés : Value=Malfunction · Module=Inboard Engine Ford (J1939[0]) · Module index=1
- Utilisé par : `Malfunction lamp`
- Ligne export : 21903 · id 64085

#### Red stop lamp Ford  `MDGN`
- Propriétés : Value=Red stop · Module=Inboard Engine Ford (J1939[0]) · Module index=2
- Utilisé par : `Red stop lamp`
- Ligne export : 21914 · id 64086

#### Amber warning lamp Ford  `MDGN`
- Propriétés : Value=Amber warning · Module=Inboard Engine Ford (J1939[0]) · Module index=3
- Utilisé par : `Amber warning lamp`
- Ligne export : 21925 · id 64087

#### Protect lamp Ford  `MDGN`
- Propriétés : Value=Protect · Module=Inboard Engine Ford (J1939[0]) · Module index=4
- Utilisé par : `Protect lamp`
- Ligne export : 21936 · id 64088

#### SPN 98  `SPN`
> Engine oil level
- Propriétés : SPN=98 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 21947 · id 64089

#### SPN 106  `SPN`
- Propriétés : SPN=106 · Dialog priority=Dont show · Failures={{4; MAP Voltage Low}}
- Utilisé par : `DM1`
- Ligne export : 21967 · id 64090

#### in Engine speed to send Ford  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=In Engine speed [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `In Engine speed`
- Utilisé par : `TSC1-A:J1939-0 Ford`
- Ligne export : 21981 · id 64876

#### TSC1-A:J1939-0 Ford  `TSC1`
- Propriétés : J1939 source address=Default · Engine speed limits={1000; 4000} · Speed channel=in Engine speed to send Ford [%] · Priority=3 · Transmit rate=20 · Override control mode=Speed control · Speed control conditions=Transient optimized, disengaged · Override control mode priority=Highest · Use checksum/counter=No · Control purpose=P32 = Temporary Powertrain Control (Original use of TSC1 Command) · Module=Inboard Engine Ford (J1939[0]) · Module index=0
- Lit : `in Engine speed to send Ford`
- Utilisé par : `Measure group: Engine Thermic`
- Ligne export : 21995 · id 63539

#### EEC1 Ford  `JFIN`
> Electronic Engine Controller 1
- Propriétés : Priority=3 · PGN=61444 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Driver's demand, engine %, Ford [%]; 9}; {Actual engine, % torque, Ford [%]; 17}; {Engine speed Ford [rpm]; 25}} · Module=Inboard Engine Ford (J1939[0]) · Module index=2
- Lit : `Actual engine, % torque, Ford`, `Driver's demand, engine %, Ford`, `Engine speed Ford`
- Utilisé par : *(personne)*
- Ligne export : 22018 · id 63288

#### Driver's demand, engine %, Ford  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `EEC1 Ford`
- Ligne export : 22045 · id 63289

#### Actual engine, % torque, Ford  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `Actual engine, % torque`, `EEC1 Ford`, `torque OR % load at current speed`
- Ligne export : 22059 · id 63290

#### Engine speed Ford  `JPIN`
- Propriétés : Unit=rpm · Length=2 Bytes (= 16 bits) · J1939 Error check=Yes · Resolution=0,125 · Offset=0 · Error value=0
- Utilisé par : `EEC1 Ford`, `Speed CAN`
- Ligne export : 22073 · id 63291

#### EEC2 Ford  `JFIN`
> Electronic Engine Controller 2
- Propriétés : Priority=3 · PGN=61443 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Accelerator pedal position Ford [%]; 9}; {% load at current speed Ford [%]; 17}} · Module=Inboard Engine Ford (J1939[0]) · Module index=5
- Lit : `% load at current speed Ford`, `Accelerator pedal position Ford`
- Utilisé par : *(personne)*
- Ligne export : 22087 · id 63500

#### Accelerator pedal position Ford  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=0,4 · Offset=0 · Error value=0
- Utilisé par : `EEC2 Ford`
- Ligne export : 22111 · id 63501

#### % load at current speed Ford  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `EEC2 Ford`
- Ligne export : 22125 · id 63502

#### Engine Temperature Ford  `JFIN`
> ET1
- Propriétés : Priority=6 · PGN=65262 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine coolant temperature Ford [°C]; 1}} · Module=Inboard Engine Ford (J1939[0]) · Module index=0
- Lit : `C`
- Utilisé par : *(personne)*
- Ligne export : 22139 · id 63622

####   `JPIN`
- Propriétés : Name, English=Engine coolant temperature Ford · Unit=°C · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-40 · Error value=0
- Utilisé par : `10 hours check-up`, `?Speed OK`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Activate Critical State`, `Activate High Aft Fan`, `Activate High Aft Fan`, `Activate Low Aft Fan`, `Activate Low Aft Fan`, `Activate exhaust Fan`, `Activate exhaust Fan`, `Actual engine, % torque`, `Adress Loose`, `Adress_Search`, `Adresse_Mem`, `Alert critical engine`, `Alert critical exhaust`, `Alert critical hydraulic`, `Allow Cruise`, `Allow Run Cruise`, `Amber warning lamp`, `Auto Fast after Down`, `Auto Fast after Down Wait`, `Auto Off Bip`, `Auto PAUSE/OFF`, `Auto Stop Timer`, `AutoStopafter 5 secondes`, `Backlight Value`, `Backward Curent`, `Bad pressure`, `Bip`, `Brake Activation`, `C`, `Calcul Accélération`, `CanBus Error TB`, `Command State`, `Couché night`, `Counter`, `Coupure Thermique avec sécurité`, `Critical Temp Timer`, `Current Date MEN`, `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `DOWN Counter`, `Days in current year`, `Dec`, `Digit Engine On`, `Don'push button`, `Duree`, `ENGINE RUN`, `ENGINE RUN`, `ET`, `ET h`, `EV tendre Chenille`, `Engine Stopped`, `Engine Thermal State`, `Engine coolant temp`, `Engine hours`, `Engine oil pressure`, `Engine speed to send`, `Engine_Started`, `Force Lock`, `Force Unlock`, `Forward Curent`, `Fuel Line Timer`, `Fuel line ignition`, `Fuel line ignition`, `Fuel line ignition IDC`, `Fuel line ignition Output`, `GPS Adresse Find`, `GPS_Adresse_Find_Int`, `Garmin - NMEA`, `HIGH arm`, `High Temp Timer`, `Ho`, `Ho_night`, `Hot Oil`, `Hour actual`, `Hydraulic pump statut`, `Hydraulics Temperature State`, `ID Fault`, `ID Prog`, `IDC Auto Sleep`, `IDC EV By Pass`, `IDC EV By Pass Down`, `IDC EV By Pass sel`, `IDC Free`, `IDC Speed Free`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `IDC Tension`, `Iguana PIN`, `Inter Allumage Thermique`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter EV By Pass`, `Inter EV DOWN`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP`, `Inter EV UP Delay`, `Inter EV Verin`, `Inter Lock landing`, `Inter Tension`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Inter Unlock`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Is_EB2`, `Is_FORD`, `Joystick Zero`, `Joystick is not in neutral position`, `Joystick not zero`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `K1 Fan Rear / Fan`, `K1 fuse is blown`, `K10`, `K10 fuse is blown`, `K11`, `K11 fuse is blown`, `K12`, `K12 fuse is blown`, `K13`, `K13 fuse is blown`, `K2 Fan Super / Pump`, `K2 fuse is blown`, `K3 Fan Exhaust / AutoOff`, `K3 fuse is blown`, `K4 Engine Power / Search Lights`, `K4 fuse is blown`, `K5 Engine Start`, `K5 fuse is blown`, `K6 Engine Water Pump`, `K6 fuse is blown`, `K7 Exhaust Water Pump`, `K7 fuse is blown`, `K8`, `K8 fuse is blown`, `K9`, `K9 fuse is blown`, `KeyBox Can Ok`, `Ko to move`, `L`, `LOW arm`, `Latence Math`, `LatenceTimer`, `Latitude Compute`, `Latitude Compute MEN`, `Levé night`, `Lock`, `Lock landing`, `Lon`, `Longitude Compute`, `Longitude Compute MEN`, `Low Temp Timer`, `M`, `MD3 - DOWN`, `MD3 - UP`, `MD3 START`, `MD3 STOP`, `MD3 start last checks`, `MDGN-+BAT:MC2[1]`, `Malfunction lamp`, `Manual Start Engine Pulse IDC`, `Math Droit`, `Math Gauche`, `Max Manip`, `Mid Temp Timer`, `Min Speed Ok`, `Mini Wait`, `Méridian`, `Need Min Speed`, `New Timer`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `OK UP/DOWN`, `Oil Security Activation`, `Oil pressure`, `Ok to move`, `Out START Engine`, `Out SWITCH ON Engine`, `PIN 44`, `PIn State`, `Persistant Water Temp`, `Power State Int`, `Pre Fuel line ignition IDC`, `Process Down Engine`, `Progress`, `Protect lamp`, `Pump 1 Right`, `Pump 1 Right Filter ECC1`, `Pump 2 Left`, `Pump 2 Left Filter ECC1`, `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Red stop lamp`, `Reset`, `Reset Speed`, `Reset Startup`, `Reset on startup`, `SPEED Engine`, `STARTING`, `Show Debug`, `Show P-1-2`, `Speed CAN`, `Speed Data remapping`, `Speed Int`, `Speed Mode`, `Speed Pump`, `Speed State`, `Speed_RPM_needed`, `Starter Proctection IDC`, `Starter Protection`, `Starter Protection CMSG`, `State`, `State All Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `State Up/Down`, `State Up/Down Raw`, `Stop Cruise`, `Stop To Move`, `Store TIMER UP/DOWN`, `Sunrise`, `Sunset`, `System Started DELAYS`, `TRACK DOWN`, `TRACK UP`, `Temperature State`, `Thermic Engine STATE`, `Time_Diff_MEM`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer UP/DOWN`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Toggle Free`, `Track DOWN Delay`, `Track UP Delay`, `Trigger`, `Trigger HeartBeat`, `Trigger Speed`, `Trigger Timer`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `Unlock`, `Unlock landing`, `VIEW BUTTON States`, `VIEW ENGINE RUN PAGE`, `VIEW SPEED STATE`, `VIEW START PAGE`, `Voyant Pression Huile Moteur`, `Wait Bad Pressure`, `Wait Buz 2`, `Wait Hot Temperature`, `Wait after stating`, `Works Latitude`, `Year since 2000`, `oldExhaust Temperature State`, `out T Exhaust Temps`, `torque OR % load at current speed`, `Event log: Check UP`, `Event log: Hydraulic Event`, `Event log: Thermic Events`, `Statistics log: System Stats`, `Statistics log: Thermic Stats`
- Ligne export : 22160 · id 63623

#### Engine fluid level/pressure 1 Ford  `JFIN`
> EFL/P1
- Propriétés : Priority=6 · PGN=65263 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine oil pressure Ford [kPa]; 25}} · Module=Inboard Engine Ford (J1939[0]) · Module index=1
- Lit : `Engine oil pressure`
- Utilisé par : *(personne)*
- Ligne export : 22175 · id 63999

####   `JPIN`
- Propriétés : Name, English=Engine oil pressure Ford · Unit=kPa · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=4 · Offset=0 · Error value=0
- Lit : `Engine oil pressure`
- Utilisé par : `10 hours check-up`, `?Speed OK`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Activate Critical State`, `Activate High Aft Fan`, `Activate High Aft Fan`, `Activate Low Aft Fan`, `Activate Low Aft Fan`, `Activate exhaust Fan`, `Activate exhaust Fan`, `Actual engine, % torque`, `Adress Loose`, `Adress_Search`, `Adresse_Mem`, `Alert critical engine`, `Alert critical exhaust`, `Alert critical hydraulic`, `Allow Cruise`, `Allow Run Cruise`, `Amber warning lamp`, `Auto Fast after Down`, `Auto Fast after Down Wait`, `Auto Off Bip`, `Auto PAUSE/OFF`, `Auto Stop Timer`, `AutoStopafter 5 secondes`, `Backlight Value`, `Backward Curent`, `Bad pressure`, `Bip`, `Brake Activation`, `C`, `Calcul Accélération`, `CanBus Error TB`, `Command State`, `Couché night`, `Counter`, `Coupure Thermique avec sécurité`, `Critical Temp Timer`, `Current Date MEN`, `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `DOWN Counter`, `Days in current year`, `Dec`, `Digit Engine On`, `Don'push button`, `Duree`, `ENGINE RUN`, `ENGINE RUN`, `ET`, `ET h`, `EV tendre Chenille`, `Engine Stopped`, `Engine Thermal State`, `Engine coolant temp`, `Engine hours`, `Engine oil pressure`, `Engine speed to send`, `Engine_Started`, `Force Lock`, `Force Unlock`, `Forward Curent`, `Fuel Line Timer`, `Fuel line ignition`, `Fuel line ignition`, `Fuel line ignition IDC`, `Fuel line ignition Output`, `GPS Adresse Find`, `GPS_Adresse_Find_Int`, `Garmin - NMEA`, `HIGH arm`, `High Temp Timer`, `Ho`, `Ho_night`, `Hot Oil`, `Hour actual`, `Hydraulic pump statut`, `Hydraulics Temperature State`, `ID Fault`, `ID Prog`, `IDC Auto Sleep`, `IDC EV By Pass`, `IDC EV By Pass Down`, `IDC EV By Pass sel`, `IDC Free`, `IDC Speed Free`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `IDC Tension`, `Iguana PIN`, `Inter Allumage Thermique`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter EV By Pass`, `Inter EV DOWN`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP`, `Inter EV UP Delay`, `Inter EV Verin`, `Inter Lock landing`, `Inter Tension`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Inter Unlock`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Is_EB2`, `Is_FORD`, `Joystick Zero`, `Joystick is not in neutral position`, `Joystick not zero`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `K1 Fan Rear / Fan`, `K1 fuse is blown`, `K10`, `K10 fuse is blown`, `K11`, `K11 fuse is blown`, `K12`, `K12 fuse is blown`, `K13`, `K13 fuse is blown`, `K2 Fan Super / Pump`, `K2 fuse is blown`, `K3 Fan Exhaust / AutoOff`, `K3 fuse is blown`, `K4 Engine Power / Search Lights`, `K4 fuse is blown`, `K5 Engine Start`, `K5 fuse is blown`, `K6 Engine Water Pump`, `K6 fuse is blown`, `K7 Exhaust Water Pump`, `K7 fuse is blown`, `K8`, `K8 fuse is blown`, `K9`, `K9 fuse is blown`, `KeyBox Can Ok`, `Ko to move`, `L`, `LOW arm`, `Latence Math`, `LatenceTimer`, `Latitude Compute`, `Latitude Compute MEN`, `Levé night`, `Lock`, `Lock landing`, `Lon`, `Longitude Compute`, `Longitude Compute MEN`, `Low Temp Timer`, `M`, `MD3 - DOWN`, `MD3 - UP`, `MD3 START`, `MD3 STOP`, `MD3 start last checks`, `MDGN-+BAT:MC2[1]`, `Malfunction lamp`, `Manual Start Engine Pulse IDC`, `Math Droit`, `Math Gauche`, `Max Manip`, `Mid Temp Timer`, `Min Speed Ok`, `Mini Wait`, `Méridian`, `Need Min Speed`, `New Timer`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `OK UP/DOWN`, `Oil Security Activation`, `Oil pressure`, `Ok to move`, `Out START Engine`, `Out SWITCH ON Engine`, `PIN 44`, `PIn State`, `Persistant Water Temp`, `Power State Int`, `Pre Fuel line ignition IDC`, `Process Down Engine`, `Progress`, `Protect lamp`, `Pump 1 Right`, `Pump 1 Right Filter ECC1`, `Pump 2 Left`, `Pump 2 Left Filter ECC1`, `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Red stop lamp`, `Reset`, `Reset Speed`, `Reset Startup`, `Reset on startup`, `SPEED Engine`, `STARTING`, `Show Debug`, `Show P-1-2`, `Speed CAN`, `Speed Data remapping`, `Speed Int`, `Speed Mode`, `Speed Pump`, `Speed State`, `Speed_RPM_needed`, `Starter Proctection IDC`, `Starter Protection`, `Starter Protection CMSG`, `State`, `State All Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `State Up/Down`, `State Up/Down Raw`, `Stop Cruise`, `Stop To Move`, `Store TIMER UP/DOWN`, `Sunrise`, `Sunset`, `System Started DELAYS`, `TRACK DOWN`, `TRACK UP`, `Temperature State`, `Thermic Engine STATE`, `Time_Diff_MEM`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer UP/DOWN`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Toggle Free`, `Track DOWN Delay`, `Track UP Delay`, `Trigger`, `Trigger HeartBeat`, `Trigger Speed`, `Trigger Timer`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `Unlock`, `Unlock landing`, `VIEW BUTTON States`, `VIEW ENGINE RUN PAGE`, `VIEW SPEED STATE`, `VIEW START PAGE`, `Voyant Pression Huile Moteur`, `Wait Bad Pressure`, `Wait Buz 2`, `Wait Hot Temperature`, `Wait after stating`, `Works Latitude`, `Year since 2000`, `oldExhaust Temperature State`, `out T Exhaust Temps`, `torque OR % load at current speed`, `Event log: Check UP`, `Event log: Hydraulic Event`, `Event log: Thermic Events`, `Statistics log: System Stats`, `Statistics log: Thermic Stats`
- Ligne export : 22196 · id 64000

## Thermic / Oil security

#### Hydraulic pump statut  `VIN`
- Propriétés : Unit=Bar · Reference voltage=Reference voltage A · Error value=0 · Calibration={500; 4500; 0; 30} · Alarms={No; 0; No; 100} · Module=MC42 (MC42[1]) · Module index=5
- Lit : ``
- Utilisé par : `Wait Bad Pressure`, `Measure group: Hydraulic`
- Ligne export : 17130 · id 35669

#### Check Pump  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Wait Bad Pressure`, `Adjust group: Master Pump`, `Single adjust item: Check Pump`
- Ligne export : 17154 · id 35683

#### Wait Bad Pressure  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `Engine_Started AND (Hydraulic pump statut [Bar] <= 10) AND (Check Pump)`
- Lit : ``, `Check Pump`, `Engine_Started`, `Hydraulic pump statut`
- Utilisé par : `Bad pressure`, `Event log: Thermic Events`, `MD3 page: Thermic`, `Statistics log: Thermic Stats`
- Ligne export : 17167 · id 29815

#### Bad pressure  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=Hydraulic pump lubrification failure · Text, English=Stop Engine Immediately. And contact your service center.
- Logique :
  - **Showing** = `Wait Bad Pressure`
- Lit : ``, `Wait Bad Pressure`
- Utilisé par : *(personne)*
- Ligne export : 17226 · id 29834

#### Oil Temps  `VIN`
- Propriétés : Unit=°C · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-ST · Calibration={250; 4750; -50; 150} · Alarms={No; 0; No; 100} · Module=MC42 (MC42[1]) · Module index=4
- Utilisé par : `ECC1_Oil_Temp`, `Hot Oil`, `Hydraulics Temperature State`, `Wait Hot Temperature`, `Measure group: Engine and Translation`, `Measure group: Hydraulic`, `Measure group: Temperature`
- Ligne export : 17274 · id 32974

#### Wait Hot Temperature  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `Engine_Started AND (Oil Temps [°C] >= 95)`
- Lit : ``, `Engine_Started`, `Oil Temps`
- Utilisé par : `Hot Oil`
- Ligne export : 17298 · id 33629

#### Hot Oil  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header=Hydraulic Oil is to hot. · Text=Use the low speed. · Channel=Oil Temps [°C]
- Logique :
  - **Showing** = `Wait Hot Temperature`
  - **Hiding** = `not(Wait Hot Temperature)`
- Lit : ``, `Oil Temps`, `Wait Hot Temperature`
- Utilisé par : *(personne)*
- Ligne export : 17350 · id 33659

#### Oil Temp Mid/High  `FP`
> Oil temperature to ask a low speed Fan
- Propriétés : Unit=°C · Default mode={75}
- Utilisé par : `Hydraulics Temperature State`, `Adjust group: Master Cooling`, `Single adjust item: Oil Temp Mid/High`
- Ligne export : 17404 · id 66144

#### Oil Temp Low/Mid  `FP`
- Propriétés : Unit=°C · Default mode={50}
- Utilisé par : `Hydraulics Temperature State`, `Adjust group: Master Cooling`, `Single adjust item: Oil Temp Low/Mid`
- Ligne export : 17416 · id 66145

#### Oil Temp Critical  `FP`
- Propriétés : Unit=°C · Default mode={90}
- Utilisé par : `ECC1_Oil_Temp`, `Hydraulics Temperature State`, `Adjust group: Master Cooling`, `Single adjust item: Oil Temp Critical`
- Ligne export : 17428 · id 66146

#### Oil Temp Hysteresis  `FP`
- Propriétés : Unit=% · Default mode={0,9}
- Utilisé par : `Hydraulics Temperature State`
- Ligne export : 17440 · id 66945

#### Hydraulics Temperature State  `SMC`
> State machine for Oil temperature based on oil sensor Temp.
- Propriétés : Default state name=Off
- Fonction *Critical* :
  - **Activating** = `Oil Temps [°C] > Oil Temp Critical [°C]`
  - **Blocking** = `Oil Temps [°C] < (Oil Temp Hysteresis [%] * Oil Temp Critical [°C])`
- Fonction *High* :
  - **Activating** = `Oil Temps [°C] > Oil Temp Mid/High [°C]`
  - **Blocking** = `Oil Temps [°C] < (Oil Temp Hysteresis [%] * Oil Temp Mid/High [°C])`
- Fonction *Mid* :
  - **Activating** = `Oil Temps [°C] > Oil Temp Low/Mid [°C]`
  - **Blocking** = `Oil Temps [°C] < (Oil Temp Hysteresis [%] * Oil Temp Low/Mid [°C])`
- Fonction *Low* :
  - **Activating** = `Oil Temps [°C] <= Oil Temp Low/Mid [°C]`
- Lit : ``, `Oil Temp Critical`, `Oil Temp Hysteresis`, `Oil Temp Low/Mid`, `Oil Temp Mid/High`, `Oil Temps`
- Utilisé par : `In Hydraulics Temp State`
- Ligne export : 17452 · id 66114

## Thermic / Power

#### Reset Startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset Startup`
- Lit : ``, `Reset Startup`
- Utilisé par : `Pre Fuel line ignition IDC`, `Reset Startup`
- Ligne export : 14881 · id 30494

#### Oil Security Activation  `IDC`
- Propriétés : Toggle=No · Delay on=60000 · Delay off=0
- Logique :
  - **Activating** = `Wait_Very_Low_Oil_Level`
- Lit : ``, `Wait_Very_Low_Oil_Level`
- Utilisé par : `Coupure Thermique avec sécurité`
- Ligne export : 14931 · id 30513

#### MD3 STOP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `NegativeFlank(MD3_Start/Stop)`
- Lit : ``, `MD3_Start/Stop`
- Utilisé par : `Coupure Thermique avec sécurité`, `MD3 start last checks`
- Ligne export : 14974 · id 30523

#### Coupure Thermique avec sécurité  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MD3 STOP) OR (Oil Security Activation)`
- Lit : ``, `MD3 STOP`, `Oil Security Activation`
- Utilisé par : `Digit Engine On`
- Ligne export : 15018 · id 30531

#### Fuel Line Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Fuel line ignition IDC`
  - **Resetting** = `(PositiveFlank(Fuel line ignition IDC)) OR (not(Pre Fuel line ignition IDC))`
- Lit : ``, `Fuel line ignition IDC`, `Pre Fuel line ignition IDC`
- Utilisé par : `Fuel line ignition Output`, `Pre Fuel line ignition IDC`, `Progress`
- Ligne export : 15068 · id 30540

#### Fuel line ignition  `MEM`
- Propriétés : Input channel=Fuel line ignition State · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `NegativeFlank(Pre Fuel line ignition IDC)`
- Lit : ``, `Fuel line ignition State`, `Pre Fuel line ignition IDC`
- Utilisé par : `Fuel line ignition`, `Pre Fuel line ignition IDC`
- Ligne export : 15136 · id 30552

#### Starter Protection CMSG  `IMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Starter Temperature Protection · Text=Please check fuel level, battery level, oil level, fuel line, fuel filter. Do NOT start the engine more than 5 time per minute. You can start an fuel line ignition buy press RUN. · Left button=Ok · Center button=RUN
- Logique :
  - **Showing** = `Starter Proctection IDC`
  - **Hiding** = `(2 = Starter Protection CMSG) OR ((not(Fuel line ignition IDC)) and (not(Starter Proctection IDC))) OR (NegativeFlank(Fuel line ignition IDC))`
- Lit : ``, `C`, `Fuel line ignition IDC`, `Starter Proctection IDC`
- Utilisé par : `Pre Fuel line ignition IDC`
- Ligne export : 15180 · id 30569

#### Pre Fuel line ignition IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((1 = Fuel line ignition))) OR (PositiveFlank((3 = Starter Protection CMSG))) OR (Pre Fuel line ignition IDC)`
  - **Blocking** = `(Fuel Line Timer [s] > 50) OR Engine_Started OR (Reset Startup)`
- Lit : ``, `C`, `Engine_Started`, `Fuel Line Timer`, `Fuel line ignition`, `Reset Startup`, `Starter Protection CMSG`
- Utilisé par : `Fuel Line Timer`, `Fuel line ignition`, `Fuel line ignition IDC`
- Ligne export : 15270 · id 30582

#### Fuel line ignition IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Pre Fuel line ignition IDC`
  - **Blocking** = `Engine_Started`
- Lit : ``, `Engine_Started`, `Pre Fuel line ignition IDC`
- Utilisé par : `Fuel Line Timer`, `Fuel line ignition`, `MD3 START`, `Starter Protection CMSG`, `Event log: Thermic Events`
- Ligne export : 15370 · id 30597

#### Fuel line ignition State  `SP`
- Propriétés : Input channel=None · Default state name=OFF · States={RUN}
- Utilisé par : `Fuel line ignition`, `Adjust group: Maintenance`, `Single adjust item: Fuel line ignition State`
- Ligne export : 15420 · id 30606

#### Starter Protection Slope  `SFC`
- Propriétés : Input channel=Starter Protection [%] · Enable=Yes · Type=Slopes · Slopes={{10; 1}; {0; 0}}
- Lit : `Starter Protection`
- Utilisé par : `Starter Proctection IDC`
- Ligne export : 15432 · id 30616

#### Starter Proctection IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Starter Protection Slope [%] >= 150`
- Lit : ``, `Starter Protection Slope`
- Utilisé par : `Starter Protection CMSG`
- Ligne export : 15450 · id 30617

#### Out START Engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MD3 start last checks) OR (Manual Start Engine Pulse IDC)`
- Lit : ``, `MD3 start last checks`, `Manual Start Engine Pulse IDC`
- Utilisé par : `K5 Engine Start`, `Starter Protection`, `Statistics log: Thermic Stats`
- Ligne export : 15495 · id 32462

#### Starter Protection  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `1000 * Out START Engine`
- Lit : ``, `Out START Engine`
- Utilisé par : `Starter Protection Slope`
- Ligne export : 15545 · id 30626

#### MD3 start last checks  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MD3 START) OR (MD3 start last checks)`
  - **Blocking** = `Engine_Started OR (MD3 STOP) OR (PositiveFlank(AutoStopafter 5 secondes)) OR (not(Joystick Zero))`
- Lit : ``, `AutoStopafter 5 secondes`, `Engine_Started`, `Joystick Zero`, `MD3 START`, `MD3 STOP`
- Utilisé par : `AutoStopafter 5 secondes`, `Out START Engine`
- Ligne export : 15588 · id 30634

#### AutoStopafter 5 secondes  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `MD3 start last checks`
  - **Blocking** = `Engine_Started`
- Lit : ``, `Engine_Started`, `MD3 start last checks`
- Utilisé par : `Digit Engine On`, `MD3 start last checks`
- Ligne export : 15668 · id 30647

#### MD3 START  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `MD3_Start/Stop`
  - **Blocking** = `Fuel line ignition IDC`
- Lit : ``, `Fuel line ignition IDC`, `MD3_Start/Stop`
- Utilisé par : `Digit Engine On`, `Joystick is not in neutral position`, `MD3 start last checks`
- Ligne export : 15718 · id 30656

#### Manual Start Engine  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Manual Start Engine Pulse IDC`, `Adjust group: Master Features`, `Single adjust item: Manual Start Engine`
- Ligne export : 15768 · id 33227

#### Manual Start Engine Pulse IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `PositiveFlank(Manual Start Engine)`
- Lit : ``, `Manual Start Engine`
- Utilisé par : `Out START Engine`
- Ligne export : 15781 · id 33232

#### Progress  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `Fuel Line Timer [s] * 2`
- Lit : ``, `Fuel Line Timer`
- Utilisé par : `Fuel line ignition`
- Ligne export : 15825 · id 30608

#### Fuel line ignition  `CMSG`
- Propriétés : Show message=All · Dialog type=Message · Header=Fuel line ignition · Text=Please wait during fuel line ignition. (Engine need to be stop). · Channel=Progress [%]
- Logique :
  - **Showing** = `PositiveFlank(Fuel line ignition IDC)`
  - **Hiding** = `NegativeFlank(Fuel line ignition IDC)`
- Lit : ``, `Fuel line ignition`, `Fuel line ignition IDC`, `Progress`
- Utilisé par : `Pre Fuel line ignition IDC`
- Ligne export : 15868 · id 30560

#### ECU Engine on  `DP`
- Propriétés : True text=ON · False text=OFF · Default mode={False}
- Utilisé par : `Inter Allumage Thermique`, `Adjust group: Master Features`, `Single adjust item: ECU Engine on`
- Ligne export : 15923 · id 30667

#### Digit Engine On  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Digit Engine On) OR (MD3 START)`
  - **Blocking** = `(Coupure Thermique avec sécurité) OR (PositiveFlank(AutoStopafter 5 secondes))`
- Lit : ``, `AutoStopafter 5 secondes`, `Coupure Thermique avec sécurité`, `MD3 START`
- Utilisé par : `Inter Allumage Thermique`
- Ligne export : 15936 · id 30668

#### Fuel line ignition Output  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inside((Fuel Line Timer [s] mod 10), 1, 9)`
- Lit : ``, `Fuel Line Timer`
- Utilisé par : `Inter Allumage Thermique`
- Ligne export : 16001 · id 30679

#### Inter Allumage Thermique  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `((64 = 64) and Digit Engine On) OR (ECU Engine on) OR (Fuel line ignition Output)`
- Lit : ``, `Digit Engine On`, `ECU Engine on`, `Fuel line ignition Output`
- Utilisé par : `Out SWITCH ON Engine`
- Ligne export : 16056 · id 30688

#### Water °C Low  `FP`
- Propriétés : Unit=°C · Mode selector=Engine type · Default mode: EB2 1.2L={70} · Mode 1: FORD 1.5L={70}
- Lit : `Engine type`
- Utilisé par : `Engine Temp State`, `Exhaust Temp State hy test`, `oldExhaust Temperature State`, `Adjust group: Master Cooling`, `Single adjust item: Water °C Low`
- Ligne export : 16131 · id 30703

#### in Engine coolant temperature  `FGI`
- Propriétés : Unit=°C · Input type=Real · Input=Engine coolant temp [°C] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Engine coolant temp`
- Utilisé par : `Persistant Water Temp`
- Ligne export : 16145 · id 65162

#### Persistant Water Temp  `MEM`
> System memory used to keep Water temp after engine is turned off
- Propriétés : Input channel=in Engine coolant temperature [°C] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `(in Engine coolant temperature [°C] <> 0) AND (Persistant Water Temp [°C] <> in Engine coolant temperature [°C]) AND Engine_Started`
- Lit : ``, `Engine_Started`, `in Engine coolant temperature`
- Utilisé par : `ECC1_Engine_Temp`, `Engine Temp State`, `Engine Thermal State`, `Speed Pump`, `State All Speed`, `VIEW SPEED STATE`, `Measure group: Engine Thermic`
- Ligne export : 16159 · id 30705

#### Water °C High  `FP`
- Propriétés : Unit=°C · Mode selector=Engine type · Default mode: EB2 1.2L={92} · Mode 1: FORD 1.5L={90}
- Lit : `Engine type`
- Utilisé par : `Engine Temp State`, `Exhaust Temp State hy test`, `oldExhaust Temperature State`, `Adjust group: Master Cooling`, `Single adjust item: Water °C High`
- Ligne export : 16221 · id 65875

#### Ambiante Temperature  `SP`
- Propriétés : Input channel=None · States={High}
- Utilisé par : `Timer Fan Critical`, `Timer Fan Hot`, `Timer Fan Low`, `Timer Fan Mild`, `Adjust group: Setup`, `Single adjust item: Ambiante Temperature`
- Ligne export : 16235 · id 30728

#### Timer Fan Hot  `FP`
- Propriétés : Unit=s · Mode selector=Ambiante Temperature · Default mode: ={180} · Mode 1: High={270}
- Lit : `Ambiante Temperature`
- Utilisé par : `Critical Temp Timer`, `High Temp Timer`, `Adjust group: Master Cooling`, `Single adjust item: Timer Fan Hot`
- Ligne export : 16247 · id 30731

#### High Temp Timer  `TMR`
> Timer triggered at the engine stop to Allow Full Fan if system temperature is still Hot
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=Timer Fan Hot [s]
- Logique :
  - **Decreasing** = `High Temp Timer [s] > 0`
  - **Resetting** = `Engine_Started`
- Lit : ``, `Engine_Started`, `Timer Fan Hot`
- Utilisé par : `Engine Thermal State`
- Ligne export : 16261 · id 65880

#### Timer Fan Mild  `FP`
- Propriétés : Unit=s · Mode selector=Ambiante Temperature · Default mode: ={60} · Mode 1: High={120}
- Lit : `Ambiante Temperature`
- Utilisé par : `Mid Temp Timer`, `Adjust group: Master Cooling`, `Single adjust item: Timer Fan Mild`
- Ligne export : 16322 · id 30730

#### Mid Temp Timer  `TMR`
> Timer triggered at the engine stop to maintain system temp at Mid
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=Timer Fan Mild [s]
- Logique :
  - **Decreasing** = `Mid Temp Timer [s] > 0`
  - **Resetting** = `Engine_Started`
- Lit : ``, `Engine_Started`, `Timer Fan Mild`
- Utilisé par : `Engine Thermal State`
- Ligne export : 16336 · id 65898

#### Timer Fan Low  `FP`
- Propriétés : Unit=s · Mode selector=Ambiante Temperature · Default mode: ={40} · Mode 1: High={80}
- Lit : `Ambiante Temperature`
- Utilisé par : `Low Temp Timer`, `Adjust group: Master Cooling`, `Single adjust item: Timer Fan Low`
- Ligne export : 16397 · id 65954

#### Low Temp Timer  `TMR`
> Timer triggered at the engine stop to maintain system temp at Low
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=Timer Fan Low [s]
- Logique :
  - **Decreasing** = `Low Temp Timer [s] > 0`
  - **Resetting** = `Engine_Started`
- Lit : ``, `Engine_Started`, `Timer Fan Low`
- Utilisé par : `Engine Thermal State`
- Ligne export : 16411 · id 65938

#### Water °C Critical  `FP`
- Propriétés : Unit=°C · Mode selector=Engine type · Default mode: EB2 1.2L={97} · Mode 1: FORD 1.5L={97}
- Lit : `Engine type`
- Utilisé par : `ECC1_Engine_Temp`, `Engine Temp State`, `Exhaust Temp State hy test`, `oldExhaust Temperature State`, `Adjust group: Master Cooling`, `Single adjust item: Water °C Critical`
- Ligne export : 16472 · id 66041

#### Critical Temp Timer  `TMR`
> Timer triggered at the engine stop to Maintain critical state during a period of time
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=Timer Fan Hot [s]
- Logique :
  - **Decreasing** = `Critical Temp Timer [s] > 0`
  - **Resetting** = `Engine_Started`
- Lit : ``, `Engine_Started`, `Timer Fan Hot`
- Utilisé par : `Engine Thermal State`
- Ligne export : 16486 · id 66065

#### Out SWITCH ON Engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter Allumage Thermique`
- Lit : ``, `Inter Allumage Thermique`
- Utilisé par : `K4 Engine Power / Search Lights`, `Thermic Engine STATE`
- Ligne export : 16547 · id 32457

#### Joystick is not in neutral position  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header, English=Neutral position · Text, English=Please put jostick in neutral position before start engine.
- Logique :
  - **Showing** = `(not(Joystick Zero)) AND (PositiveFlank(MD3 START))`
- Lit : ``, `Joystick Zero`, `MD3 START`
- Utilisé par : *(personne)*
- Ligne export : 16590 · id 30874

#### Timer Fan Critical  `FP`
- Propriétés : Unit=s · Mode selector=Ambiante Temperature · Default mode: ={270} · Mode 1: High={540}
- Lit : `Ambiante Temperature`
- Utilisé par : *(personne)*
- Ligne export : 16647 · id 66053

#### T inExhaust temp  `FGI`
- Propriétés : Unit=°C · Input type=Real · Input=out T Exhaust Temps · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `out T Exhaust Temps`
- Utilisé par : `Exhaust Temp State hy test`, `oldExhaust Temperature State`
- Ligne export : 16661 · id 69694

#### oldExhaust Temperature State  `SMC`
> State machine for Engine temperature based on ECU Temp. The temperature after ECU shut down is estimated through temporisations
- Propriétés : Default state name=Low
- Fonction *Critical* :
  - **Activating** = `T inExhaust temp [°C] > Water °C Critical [°C]`
- Fonction *High* :
  - **Activating** = `T inExhaust temp [°C] > Water °C High [°C]`
- Fonction *Mid* :
  - **Activating** = `T inExhaust temp [°C] > Water °C Low [°C]`
- Lit : ``, `T inExhaust temp`, `Water °C Critical`, `Water °C High`, `Water °C Low`
- Utilisé par : *(personne)*
- Ligne export : 16675 · id 66743

#### Water Temp Hysteresis Gap  `FP`
- Propriétés : Unit=°C · Default mode={5}
- Utilisé par : `Engine Temp State`, `Exhaust Temp State hy test`
- Ligne export : 16783 · id 67317

#### Engine Temp State  `SMC`
- Propriétés : Default state name=Off
- Fonction *Critical* :
  ```qcode
  static outputValue:= False
  
  If Persistant Water Temp >= Water °C Critical then
    outputValue := True  //switch on
  elseif Persistant Water Temp < (Water °C Critical - Water Temp Hysteresis Gap ) then
    outputValue := False  //switch off
  endif
  
  Result := OutputValue
  ```
- Fonction *High* :
  ```qcode
  static outputValue:= False
  
  If Persistant Water Temp >= Water °C High then
    outputValue := True  //switch on
  elseif Persistant Water Temp < (Water °C High - Water Temp Hysteresis Gap ) then
    outputValue := False  //switch off
  endif
  
  Result := OutputValue
  ```
- Fonction *Mid* :
  ```qcode
  static outputValue:= False
  
  If Persistant Water Temp >= Water °C Low then
    outputValue := True  //switch on
  elseif Persistant Water Temp < (Water °C Low - Water Temp Hysteresis Gap ) then
    outputValue := False  //switch off
  endif
  
  Result := OutputValue
  ```
- Fonction *Low* :
  ```qcode
  static outputValue:= False
  
  If Persistant Water Temp < Water °C Low then
    outputValue := True  //switch on
  endif
  
  Result := OutputValue
  ```
- Lit : `Persistant Water Temp`, `Water Temp Hysteresis Gap`, `Water °C Critical`, `Water °C High`, `Water °C Low`
- Utilisé par : `Engine Thermal State`, `Event log: Thermic Events`
- Ligne export : 16795 · id 67204

#### Engine Thermal State  `SMC`
- Propriétés : Default state name=Off
- Fonction *Critical* :
  - **Activating** = `Engine Temp State = 1`
  - **Blocking** = `Critical Temp Timer [s] <= 0`
- Fonction *High* :
  - **Activating** = `Engine Temp State = 2`
  - **Blocking** = `High Temp Timer [s] <= 0`
- Fonction *Mid* :
  - **Activating** = `Engine Temp State = 3`
  - **Blocking** = `Mid Temp Timer [s] <= 0`
- Fonction *Low* :
  - **Activating** = `(Engine Temp State = 4) AND (Low Temp Timer [s] > 0)`
  - **Blocking** = `Persistant Water Temp [°C] = 0`
- Lit : ``, `Critical Temp Timer`, `Engine Temp State`, `High Temp Timer`, `Low Temp Timer`, `Mid Temp Timer`, `Persistant Water Temp`
- Utilisé par : `In Engine Thermal State`
- Ligne export : 16868 · id 67376

#### Exhaust Temp State hy test  `SMC`
- Propriétés : Default state name=Off
- Fonction *Critical* :
  ```qcode
  static outputValue:= False
  
  If T inExhaust temp >= Water °C Critical then
    outputValue := True  //switch on
  elseif T inExhaust temp < (Water °C Critical - Water Temp Hysteresis Gap ) then
    outputValue := False  //switch off
  endif
  
  Result := OutputValue
  ```
- Fonction *High* :
  ```qcode
  static outputValue:= False
  
  If T inExhaust temp >= Water °C High then
    outputValue := True  //switch on
  elseif T inExhaust temp < (Water °C High - Water Temp Hysteresis Gap ) then
    outputValue := False  //switch off
  endif
  
  Result := OutputValue
  ```
- Fonction *Mid* :
  ```qcode
  static outputValue:= False
  
  If T inExhaust temp >= Water °C Low then
    outputValue := True  //switch on
  elseif T inExhaust temp < (Water °C Low - Water Temp Hysteresis Gap ) then
    outputValue := False  //switch off
  endif
  
  Result := OutputValue
  ```
- Lit : `T inExhaust temp`, `Water Temp Hysteresis Gap`, `Water °C Critical`, `Water °C High`, `Water °C Low`
- Utilisé par : `In Exhaust Temp State`
- Ligne export : 17054 · id 67924

## Thermic / Pump

#### Min current Right Backward  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `Pump 1 Right`, `Adjust group: Master Pump`, `Single adjust item: Min current Right Backward`
- Ligne export : 19507 · id 32143

#### Step change  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`
- Ligne export : 19519 · id 32145

#### Forward - direct corrector  `FP`
- Propriétés : Unit=% · Mode selector=Speed Pump · Default mode: Slow={0} · Mode 1: Super Slow={0} · Mode 2: Fast Speed={0}
- Lit : `Speed Pump`
- Utilisé par : `Punp 1 - Current`, `Punp 2 - Current`, `Adjust group: `, `Single adjust item: Forward - direct corrector`
- Ligne export : 19531 · id 32146

#### In Curent - Low Speed  `FGI`
- Propriétés : Unit=mA · Input type=Real · Input=Pump Curent - Low Speed [mA] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Pump Curent - Low Speed`
- Utilisé par : `Backward Curent`, `Forward Curent`
- Ligne export : 19547 · id 64842

#### In Curent - Super Low Speed  `FGI`
- Propriétés : Unit=mA · Input type=Real · Input=Pump Curent - Super Low Speed [mA] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Pump Curent - Super Low Speed`
- Utilisé par : `Backward Curent`, `Forward Curent`
- Ligne export : 19561 · id 64844

#### In Curent  - Hight Speed  `FGI`
- Propriétés : Unit=mA · Input type=Real · Input=Pump Curent  - Hight Speed [mA] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Pump Curent  - Hight Speed`
- Utilisé par : `Backward Curent`, `Forward Curent`
- Ligne export : 19575 · id 64845

#### Forward Curent  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed · Function selector=Speed Pump
- Fonction *Slow* :
  - **Controlling** = `In Curent - Low Speed [mA]`
- Fonction *Super Slow* :
  - **Controlling** = `In Curent - Super Low Speed [mA]`
- Fonction *Fast Speed* :
  - **Controlling** = `In Curent  - Hight Speed [mA]`
- Lit : ``, `In Curent  - Hight Speed`, `In Curent - Low Speed`, `In Curent - Super Low Speed`, `Speed Pump`
- Utilisé par : `Punp 1 - Current`, `Punp 2 - Current`
- Ligne export : 19589 · id 32150

#### In Max curent  `FGI`
- Propriétés : Unit=mA · Input type=Real · Input=Pump Max curent [mA] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Pump Max curent`
- Utilisé par : `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`
- Ligne export : 19693 · id 64850

#### Punp 1 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `Forward Curent [mA] - (Forward - direct corrector [%] *% Step change [mA])`
  - **Limiting** = `In Max curent [mA]`
- Lit : ``, `Forward - direct corrector`, `Forward Curent`, `In Max curent`, `Step change`
- Utilisé par : `Filter pump 1 Neg`, `Filter pump 1 Pos`
- Ligne export : 19707 · id 32172

#### coeff pente ?  `FP`
- Propriétés : Unit=mA/s · Default mode={200}
- Utilisé par : `Filter pump 1 Neg`, `Filter pump 1 Pos`, `Filter pump 2 Neg`, `Filter pump 2 Pos`
- Ligne export : 19767 · id 32182

#### Filter pump 1 Pos  `SFC`
- Propriétés : Input channel=Punp 1 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{coeff pente ? [mA/s]; coeff pente ? [mA/s]}; {coeff pente ? [mA/s]; coeff pente ? [mA/s]}}
- Lit : `Punp 1 - Current`, `coeff pente ?`
- Utilisé par : `Pump 1 Right`
- Ligne export : 19779 · id 32183

#### Min current Left Backward  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `Pump 2 Left`, `Adjust group: Master Pump`, `Single adjust item: Min current Left Backward`
- Ligne export : 19797 · id 32184

#### Punp 2 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `Forward Curent [mA] + (Forward - direct corrector [%] *% Step change [mA])`
  - **Limiting** = `In Max curent [mA]`
- Lit : ``, `Forward - direct corrector`, `Forward Curent`, `In Max curent`, `Step change`
- Utilisé par : `Filter pump 2 Neg`, `Filter pump 2 Pos`
- Ligne export : 19809 · id 32185

#### Filter pump 2 Pos  `SFC`
- Propriétés : Input channel=Punp 2 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{coeff pente ? [mA/s]; coeff pente ? [mA/s]}; {coeff pente ? [mA/s]; coeff pente ? [mA/s]}}
- Lit : `Punp 2 - Current`, `coeff pente ?`
- Utilisé par : `Pump 2 Left`
- Ligne export : 19869 · id 32195

#### Min current Left Fordward  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `Pump 2 Left`, `Adjust group: Master Pump`, `Single adjust item: Min current Left Fordward`
- Ligne export : 19887 · id 32196

#### Backward - direct corrector  `FP`
- Propriétés : Unit=% · Mode selector=Speed Pump · Default mode: Slow={0} · Mode 1: Super Slow={0} · Mode 2: Fast Speed={0}
- Lit : `Speed Pump`
- Utilisé par : `Punp 1 - Current`, `Punp 2 - Current`, `Adjust group: `, `Single adjust item: Backward - direct corrector`
- Ligne export : 19899 · id 32197

#### Backward Curent  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed · Function selector=Speed Pump
- Fonction *Slow* :
  - **Controlling** = `In Curent - Low Speed [mA]`
- Fonction *Super Slow* :
  - **Controlling** = `In Curent - Super Low Speed [mA]`
- Fonction *Fast Speed* :
  - **Controlling** = `In Curent  - Hight Speed [mA]`
- Lit : ``, `In Curent  - Hight Speed`, `In Curent - Low Speed`, `In Curent - Super Low Speed`, `Speed Pump`
- Utilisé par : `Punp 1 - Current`, `Punp 2 - Current`
- Ligne export : 19915 · id 32201

#### Punp 2 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `Backward Curent [mA] + (Backward - direct corrector [%] *% Step change [mA])`
  - **Limiting** = `In Max curent [mA]`
- Lit : ``, `Backward - direct corrector`, `Backward Curent`, `In Max curent`, `Step change`
- Utilisé par : `Filter pump 2 Neg`, `Filter pump 2 Pos`
- Ligne export : 20019 · id 32223

#### Filter pump 2 Neg  `SFC`
- Propriétés : Input channel=Punp 2 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{coeff pente ? [mA/s]; coeff pente ? [mA/s]}; {coeff pente ? [mA/s]; coeff pente ? [mA/s]}}
- Lit : `Punp 2 - Current`, `coeff pente ?`
- Utilisé par : `Pump 2 Left`
- Ligne export : 20079 · id 32233

#### Pump 2 Left Filter ECC1  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Left Filter [%] * ECC1 Integrating [%]`
- Lit : ``, `ECC1 Integrating`, `Left Filter`
- Utilisé par : `Pump 2 Left`
- Ligne export : 20097 · id 32367

#### Pump 1 Right Filter ECC1  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Right Filter [%] * ECC1 Integrating [%]`
- Lit : ``, `ECC1 Integrating`, `Right Filter`
- Utilisé par : `Pump 1 Right`
- Ligne export : 20149 · id 32377

#### Min current Right Fordward  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `Pump 1 Right`, `Adjust group: Master Pump`, `Single adjust item: Min current Right Fordward`
- Ligne export : 20201 · id 32235

#### Punp 1 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `Backward Curent [mA] - (Backward - direct corrector [%] *% Step change [mA])`
  - **Limiting** = `In Max curent [mA]`
- Lit : ``, `Backward - direct corrector`, `Backward Curent`, `In Max curent`, `Step change`
- Utilisé par : `Filter pump 1 Neg`, `Filter pump 1 Pos`
- Ligne export : 20213 · id 32236

#### Filter pump 1 Neg  `SFC`
- Propriétés : Input channel=Punp 1 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{coeff pente ? [mA/s]; coeff pente ? [mA/s]}; {coeff pente ? [mA/s]; coeff pente ? [mA/s]}}
- Lit : `Punp 1 - Current`, `coeff pente ?`
- Utilisé par : `Pump 1 Right`
- Ligne export : 20273 · id 32246

#### Pump 1 Right  `COUT`
- Propriétés : Bidirectional=Yes · BWL=0 · Input channel=Pump 1 Right Filter ECC1 [%] · Default mode={{Min current Right Fordward [mA]; Filter pump 1 Pos [mA]; 0; 0}; {Min current Right Backward [mA]; Filter pump 1 Neg [mA]; 0; 0}} · Module=MC42 (MC42[1]) · Module index=0
- Lit : ``, `Filter pump 1 Neg`, `Filter pump 1 Pos`, `Min current Right Backward`, `Min current Right Fordward`, `Pump 1 Right Filter ECC1`
- Utilisé par : `Measure group: Engine and Translation`
- Ligne export : 20291 · id 32234

#### Pump 2 Left  `COUT`
- Propriétés : Bidirectional=Yes · BWL=0 · Input channel=Pump 2 Left Filter ECC1 [%] · Default mode={{Min current Left Fordward [mA]; Filter pump 2 Pos [mA]; 0; 0}; {Min current Left Backward [mA]; Filter pump 2 Neg [mA]; 0; 0}} · Module=MC42 (MC42[1]) · Module index=1
- Lit : ``, `Filter pump 2 Neg`, `Filter pump 2 Pos`, `Min current Left Backward`, `Min current Left Fordward`, `Pump 2 Left Filter ECC1`
- Utilisé par : `Measure group: Engine and Translation`
- Ligne export : 20317 · id 32247

#### Brake Slope  `IP`
- Propriétés : Unit=ms · Mode selector=Speed Pump · Default mode: Slow={750} · Mode 1: Super Slow={1000} · Mode 2: Fast Speed={4000}
- Lit : `Speed Pump`
- Utilisé par : `Inter EV Frein`
- Ligne export : 20343 · id 32311

#### Inter EV Frein  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=Brake Slope [ms]
- Logique :
  - **Activating** = `Brake Activation`
  - **Blocking** = `not(Engine_Started)`
- Lit : ``, `Brake Activation`, `Brake Slope`, `Engine_Started`
- Utilisé par : `PIN 44`
- Ligne export : 20359 · id 32312

## Thermic / SAEJ Std engine input

#### in Engine coolant temperature  `FGI`
- Propriétés : Unit=°C · Input type=Real · Input=Engine coolant temp [°C] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Engine coolant temp`
- Utilisé par : *(personne)*
- Ligne export : 17667 · id 65165

#### Para enclench voyant pression huile  `FP`
- Propriétés : Unit=kPa · Mode selector=Engine type · Default mode: EB2 1.2L={50} · Mode 1: FORD 1.5L={300}
- Lit : `Engine type`
- Utilisé par : `Voyant Pression Huile Moteur`
- Ligne export : 17681 · id 30019

#### in Engine oil pressure  `FGI`
- Propriétés : Unit=kPa · Input type=Real · Input=Engine oil pressure [kPa] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Engine oil pressure`
- Utilisé par : `Voyant Pression Huile Moteur`
- Ligne export : 17695 · id 65125

#### Voyant Pression Huile Moteur  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `(in Engine oil pressure [kPa] < Para enclench voyant pression huile [kPa]) AND Engine_Started`
- Lit : ``, `Engine_Started`, `Para enclench voyant pression huile`, `in Engine oil pressure`
- Utilisé par : `Oil pressure`, `Event log: Thermic Events`, `MD3 page: Thermic`
- Ligne export : 17709 · id 30020

#### FP - Start réduction  `FP`
- Propriétés : Unit=% · Default mode={85}
- Utilisé par : `ECC1_Power`, `Adjust group: Master Thermic`, `Single adjust item: FP - Start réduction`
- Ligne export : 17761 · id 30029

#### FP - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={20}
- Utilisé par : `ECC1_Power`, `Adjust group: Master Thermic`, `Single adjust item: FP - Incres Speed`
- Ligne export : 17773 · id 30030

#### FP - Max Error  `FP`
- Propriétés : Unit=% · Default mode={10}
- Utilisé par : `ECC1_Power`, `Adjust group: Master Thermic`, `Single adjust item: FP - Max Error`
- Ligne export : 17785 · id 30031

#### FP - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={80}
- Utilisé par : `ECC1_Power`, `Adjust group: Master Thermic`, `Single adjust item: FP - Decres Speed`
- Ligne export : 17797 · id 30032

#### in % load at current speed  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=torque OR % load at current speed [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `torque OR % load at current speed`
- Utilisé par : `ECC1_Power`
- Ligne export : 17809 · id 64885

#### ECC1_Power  `ILC`
- Propriétés : Output=Normal · Enable=Engine_Started · Input channel=in % load at current speed [%] · Start reduction at=FP - Start réduction [%] · Max error=FP - Max Error [%] · Max increase speed=FP - Incres Speed [%/s] · Max decrease speed=FP - Decres Speed [%/s]
- Lit : `Engine_Started`, `FP - Decres Speed`, `FP - Incres Speed`, `FP - Max Error`, `FP - Start réduction`, `in % load at current speed`
- Utilisé par : `ECC1 Integrating`, `Measure group: Engine and Translation`
- Ligne export : 17823 · id 30033

#### FT - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={50}
- Utilisé par : `ECC1_Engine_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FT - Incres Speed`
- Ligne export : 17838 · id 30034

#### FT - Max Error  `FP`
- Propriétés : Unit=°C · Default mode={5}
- Utilisé par : `ECC1_Engine_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FT - Max Error`
- Ligne export : 17850 · id 30035

#### FT - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={0,6}
- Utilisé par : `ECC1_Engine_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FT - Decres Speed`
- Ligne export : 17862 · id 30036

#### ECC1_Engine_Temp  `ILC`
- Propriétés : Output=Normal · Enable=Engine_Started · Input channel=Persistant Water Temp [°C] · Start reduction at=Water °C Critical [°C] · Max error=FT - Max Error [°C] · Max increase speed=FT - Incres Speed [%/s] · Max decrease speed=FT - Decres Speed [%/s]
- Lit : `Engine_Started`, `FT - Decres Speed`, `FT - Incres Speed`, `FT - Max Error`, `Persistant Water Temp`, `Water °C Critical`
- Utilisé par : `ECC1 Integrating`, `Measure group: Engine and Translation`
- Ligne export : 17874 · id 30038

#### FO - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={50}
- Utilisé par : `ECC1_Oil_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FO - Incres Speed`
- Ligne export : 17889 · id 35797

#### FO - Max Error  `FP`
- Propriétés : Unit=°C · Default mode={10}
- Utilisé par : `ECC1_Oil_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FO - Max Error`
- Ligne export : 17901 · id 35798

#### FO - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={1}
- Utilisé par : `ECC1_Oil_Temp`, `Adjust group: Master Thermic`, `Single adjust item: FO - Decres Speed`
- Ligne export : 17913 · id 35799

#### ECC1_Oil_Temp  `ILC`
- Propriétés : Output=Normal · Enable=Engine_Started · Input channel=Oil Temps [°C] · Start reduction at=Oil Temp Critical [°C] · Max error=FO - Max Error [°C] · Max increase speed=FO - Incres Speed [%/s] · Max decrease speed=FO - Decres Speed [%/s]
- Lit : `Engine_Started`, `FO - Decres Speed`, `FO - Incres Speed`, `FO - Max Error`, `Oil Temp Critical`, `Oil Temps`
- Utilisé par : `ECC1 Integrating`, `Measure group: Engine and Translation`
- Ligne export : 17925 · id 35801

#### FS - Start réduction  `FP`
- Propriétés : Unit=% · Mode selector=Engine type · Default mode: EB2 1.2L={100} · Mode 1: FORD 1.5L={30}
- Lit : `Engine type`
- Utilisé par : `ECC1_Speed`, `Adjust group: Master Thermic`, `Single adjust item: FS - Start réduction`
- Ligne export : 17940 · id 35838

#### FS - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={20}
- Utilisé par : `ECC1_Speed`, `Adjust group: Master Thermic`, `Single adjust item: FS - Incres Speed`
- Ligne export : 17954 · id 35839

#### FS - Max Error  `FP`
- Propriétés : Unit=% · Default mode={10}
- Utilisé par : `ECC1_Speed`, `Adjust group: Master Thermic`, `Single adjust item: FS - Max Error`
- Ligne export : 17966 · id 35840

#### FS - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={80}
- Utilisé par : `ECC1_Speed`, `Adjust group: Master Thermic`, `Single adjust item: FS - Decres Speed`
- Ligne export : 17978 · id 35841

#### in Speed Error Calc  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Speed Error Calcul [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Speed Error Calcul`
- Utilisé par : `ECC1_Speed`
- Ligne export : 17990 · id 64883

#### ECC1_Speed  `ILC`
- Propriétés : Output=Normal · Enable=Engine_Started · Input channel=in Speed Error Calc [%] · Start reduction at=FS - Start réduction [%] · Max error=FS - Max Error [%] · Max increase speed=FS - Incres Speed [%/s] · Max decrease speed=FS - Decres Speed [%/s]
- Lit : `Engine_Started`, `FS - Decres Speed`, `FS - Incres Speed`, `FS - Max Error`, `FS - Start réduction`, `in Speed Error Calc`
- Utilisé par : `ECC1 Integrating`, `Measure group: Engine and Translation`
- Ligne export : 18004 · id 35842

#### ECC1 Integrating  `MAC`
- Propriétés : Unit=%
- Logique :
  ```qcode
  Result := (ECC1_Engine_Temp/100) * (ECC1_Power/100) * (ECC1_Oil_Temp/100) * (ECC1_Speed/100)
  ```
- Lit : `ECC1_Engine_Temp`, `ECC1_Oil_Temp`, `ECC1_Power`, `ECC1_Speed`
- Utilisé par : `Pump 1 Right Filter ECC1`, `Pump 2 Left Filter ECC1`
- Ligne export : 18019 · id 30039

#### Oil pressure  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=Inboard engine low oil · Text, English=Stop Engine Immediately, let cool down. Check engine oil level. And contact your service center. Oil type : 10W40.
- Logique :
  - **Showing** = `Voyant Pression Huile Moteur`
  - **Hiding** = `not(Voyant Pression Huile Moteur)`
- Lit : ``, `Voyant Pression Huile Moteur`
- Utilisé par : *(personne)*
- Ligne export : 18037 · id 30062

## Thermic / T.Exhaust temp — actif seulement si `Is_EB2`

#### T Exhaust coolant temp mc 52  `VIN`
- Propriétés : Unit=°C · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-ST · Calibration={250; 4750; -50; 150} · Alarms={No; 0; No; 100} · Module=MC42 (MC42[1]) · Module index=7
- Utilisé par : `out T Exhaust Temps`
- Ligne export : 23882 · id 69679

#### out T Exhaust Temps  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `T Exhaust coolant temp mc 52 [°C]`
- Lit : ``, `T Exhaust coolant temp mc 52`
- Utilisé par : `T inExhaust temp`, `MD3 page: Thermic`
- Ligne export : 23906 · id 69680

## Thermic / Thermal Management
> Thermal management of the system, to pilot fans and advise user.

#### In Hydraulics Temp State  `FGI`
- Propriétés : Input type=State · Input=Hydraulics Temperature State · Default state name=Off · States={Critical; High; Mid; Low}
- Lit : `Hydraulics Temperature State`, `State`
- Utilisé par : `Activate Critical State`, `Alert critical hydraulic`, `Temperature State`
- Ligne export : 23094 · id 66161

#### In Engine Thermal State  `FGI`
- Propriétés : Input type=State · Input=Engine Thermal State · Default state name=Off · States={Critical; High; Mid; Low}
- Lit : `Engine Thermal State`, `State`
- Utilisé par : `Activate Critical State`, `Alert critical engine`, `Temperature State`
- Ligne export : 23110 · id 66171

#### In Exhaust Temp State  `FGI`
- Propriétés : Input type=State · Input=Exhaust Temp State hy test · Default state name=Low off · States={Critical; High; Mid}
- Lit : `Exhaust Temp State hy test`, `State`
- Utilisé par : `Activate Critical State`, `Alert critical exhaust`, `Temperature State`
- Ligne export : 23126 · id 66786

#### Temperature State  `SMC`
- Propriétés : Default state name=Off
- Fonction *Critical* :
  - **Activating** = `(In Engine Thermal State = 1) OR (In Exhaust Temp State = 1) OR (In Hydraulics Temp State = 1)`
- Fonction *High* :
  - **Activating** = `(In Engine Thermal State = 2) OR (In Exhaust Temp State = 2) OR (In Hydraulics Temp State = 2)`
- Fonction *Mid* :
  - **Activating** = `(In Engine Thermal State = 3) OR (In Exhaust Temp State = 3) OR (In Hydraulics Temp State = 3)`
- Fonction *Low* :
  - **Activating** = `In Engine Thermal State = 4`
- Lit : ``, `In Engine Thermal State`, `In Exhaust Temp State`, `In Hydraulics Temp State`
- Utilisé par : `Activate High Aft Fan`, `Activate Low Aft Fan`, `Activate exhaust Fan`, `Event log: Thermic Events`, `MD3 page: Thermic`
- Ligne export : 23141 · id 66823

#### Activate exhaust Fan  `IDC`
> The delay avoids state oscilation
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `Temperature State > 0`
- Lit : ``, `Temperature State`
- Utilisé par : `Activate Exhaust`, `Activate exhaust Fan`
- Ligne export : 23336 · id 66180

#### Activate Low Aft Fan  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `Inside(Temperature State, 0, 4)`
- Lit : ``, `Temperature State`
- Utilisé par : `Activate Low Aft Fan`, `Activate Low Aft Fan`
- Ligne export : 23381 · id 66191

#### Activate High Aft Fan  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `Inside(Temperature State, 0, 3)`
- Lit : ``, `Temperature State`
- Utilisé par : `Activate High Aft Fan`, `Activate High Aft Fan`, `MD3 page: Thermic`
- Ligne export : 23427 · id 66208

#### Activate Critical State  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `(In Hydraulics Temp State = 1) OR (In Engine Thermal State = 1) OR (In Exhaust Temp State = 1)`
- Lit : ``, `In Engine Thermal State`, `In Exhaust Temp State`, `In Hydraulics Temp State`
- Utilisé par : *(personne)*
- Ligne export : 23473 · id 66225

#### Alert critical hydraulic  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header=Stop · Text=Hydraulic temparture critical. Derating power
- Logique :
  - **Showing** = `PositiveFlank((In Hydraulics Temp State = 1))`
- Lit : ``, `In Hydraulics Temp State`
- Utilisé par : `Event log: Thermic Events`
- Ligne export : 23544 · id 66883

#### Alert critical engine  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header=Stop · Text=Engine temparture critical. Derating power
- Logique :
  - **Showing** = `PositiveFlank((In Engine Thermal State = 1))`
- Lit : ``, `In Engine Thermal State`
- Utilisé par : `Event log: Thermic Events`
- Ligne export : 23600 · id 66894

#### Alert critical exhaust  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header=Stop · Text=Exhaust temparture critical, check exhaust bay
- Logique :
  - **Showing** = `PositiveFlank((In Exhaust Temp State = 1))`
- Lit : ``, `In Exhaust Temp State`
- Utilisé par : `Event log: Thermic Events`
- Ligne export : 23656 · id 66904
