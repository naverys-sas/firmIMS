# MC2 — Speed Engine

21 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Speed Engine

#### Manip Droit CanIn [%]  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Right CanIn [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Right CanIn`
- Utilisé par : `Condition Accélération Thermique`, `Max Manip`
- Ligne export : 19213 · id 14266

#### Manip Gauche CanIn  [%]  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Left CanIn [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Left CanIn`
- Utilisé par : `Condition Accélération Thermique`, `Max Manip`
- Ligne export : 19227 · id 14267

#### Condition Accélération Thermique  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Manip Droit CanIn [%] [%] <> 0) OR (Manip Gauche CanIn  [%] [%] <> 0)`
- Lit : ``, `Manip Droit CanIn [%]`, `Manip Gauche CanIn  [%]`
- Utilisé par : `Joystick Neutral`, `SPEED Engine`
- Ligne export : 19241 · id 14270

#### Engine type  `SP`
- Propriétés : Input channel=None · Default state name=VW 2.0L · States={FORD 1.5L}
- Utilisé par : `Backward Curent  - Hight Speed`, `Backward Curent - Low Speed`, `Backward Curent - Super Low Speed`, `Forward Curent  - Hight Speed`, `Forward Curent - Low Speed`, `Forward Curent - Super Low Speed`, `IDLE Speed`, `Max curent`, `Min Speed`, `Tension Speed`, `UP/DOWN Speed`, `Value Hight Speed`, `Value Slow Speed`, `Adjust group: Master Config`, `Single adjust item: Engine type`
- Ligne export : 19295 · id 21226

#### IDLE Speed  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: VW 2.0L={1200} · Mode 1: FORD 1.5L={1000}
- Lit : `Engine type`
- Utilisé par : `Calcul Accélération`, `Adjust group: Master Engine`, `Single adjust item: IDLE Speed`
- Ligne export : 19307 · id 14279

#### Value Slow Speed  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: VW 2.0L={1800} · Mode 1: FORD 1.5L={2300}
- Lit : `Engine type`
- Utilisé par : `Calcul Accélération`, `Adjust group: Master Engine`, `Single adjust item: Value Slow Speed`
- Ligne export : 19321 · id 14280

#### Value Hight Speed  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: VW 2.0L={2300} · Mode 1: FORD 1.5L={2800}
- Lit : `Engine type`
- Utilisé par : `Calcul Accélération`, `Adjust group: Master Engine`, `Single adjust item: Value Hight Speed`
- Ligne export : 19335 · id 14281

#### CAN Speed IN  `FGI`
- Propriétés : Input type=State · Input=CAN Speed · Default state name=Parking · States={Slow; Super Slow; Fast; Road Ask; Road Cruise}
- Lit : `CAN Speed`
- Utilisé par : `SPEED Engine`
- Ligne export : 19349 · id 14283

#### 2200 tr/min  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `SPEED Engine`, `Adjust group: Master Setup`, `Single adjust item: 2200 tr/min`
- Ligne export : 19366 · id 17279

#### SPEED Engine  `SMC`
- Propriétés : Default state name=Default
- Fonction *Ralenti* :
  - **Activating** = `(Condition Accélération Thermique = 0) and (not(Inter EV Verin))`
  - **Blocking** = `(2200 tr/min) OR (CAN Speed IN = 5)`
- Fonction *Regime PV* :
  - **Activating** = `(CAN Speed IN = 2) OR (CAN Speed IN = 1)`
  - **Blocking** = `(Inter EV Verin) OR (2200 tr/min)`
- Fonction *Régime GV* :
  - **Activating** = `(CAN Speed IN = 3) OR (CAN Speed IN = 6)`
  - **Blocking** = `(2200 tr/min) OR (Inter EV Verin)`
- Fonction *Road Cruise* :
  - **Activating** = `(CAN Speed IN = 4) OR (CAN Speed IN = 5)`
  - **Blocking** = `(2200 tr/min) OR (Inter EV Verin)`
- Fonction *Regim UP/DOWN* :
  - **Activating** = `Inter EV Verin`
  - **Blocking** = `2200 tr/min`
- Fonction *2200 tr/min* :
  - **Activating** = `2200 tr/min`
- Lit : ``, `2200 tr/min`, `CAN Speed IN`, `Condition Accélération Thermique`, `Inter EV Verin`
- Utilisé par : `Calcul Accélération`
- Ligne export : 19379 · id 14284

#### Max Manip  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxOf (Absolute)(Abs(Manip Droit CanIn [%] [%]), Abs(Manip Gauche CanIn  [%] [%]))`
- Lit : ``, `Manip Droit CanIn [%]`, `Manip Gauche CanIn  [%]`
- Utilisé par : `Calcul Accélération`
- Ligne export : 19691 · id 14308

#### TSC1 Filter Slope  `FP`
- Propriétés : Unit=%/s · Default mode={100}
- Utilisé par : `TSC1 Filter`
- Ligne export : 19742 · id 14317

#### UP/DOWN Speed  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: VW 2.0L={1700} · Mode 1: FORD 1.5L={1700}
- Lit : `Engine type`
- Utilisé par : `Calcul Accélération`, `Adjust group: Master Engine`, `Single adjust item: UP/DOWN Speed`
- Ligne export : 19754 · id 14318

#### Min Speed  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: VW 2.0L={1200} · Mode 1: FORD 1.5L={1300}
- Lit : `Engine type`
- Utilisé par : `Calcul Accélération`, `Adjust group: Master Engine`, `Single adjust item: Min Speed`
- Ligne export : 19768 · id 22263

#### Calcul Accélération  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed · Function selector=SPEED Engine
- Fonction *Default* :
  - **Controlling** = `1800`
- Fonction *Ralenti* :
  - **Controlling** = `IDLE Speed [rpm]`
- Fonction *Regime PV* :
  - **Controlling** = `lin(Max Manip: 0->Min Speed [rpm], 100->Value Slow Speed [rpm], Freeze)`
- Fonction *Régime GV* :
  - **Controlling** = `lin(Max Manip: 0->Min Speed [rpm], 100->Value Hight Speed [rpm], Freeze)`
- Fonction *Road Cruise* :
  - **Controlling** = `lin(Max Manip: 100->Min Speed [rpm], 0->Value Hight Speed [rpm], Freeze)`
- Fonction *Regim UP/DOWN* :
  - **Controlling** = `UP/DOWN Speed [rpm]`
- Fonction *2200 tr/min* :
  - **Controlling** = `2200`
- Lit : ``, `IDLE Speed`, `Max Manip`, `Min Speed`, `SPEED Engine`, `UP/DOWN Speed`, `Value Hight Speed`, `Value Slow Speed`
- Utilisé par : `Accélération Thermique`
- Ligne export : 19782 · id 14319

#### NEED MORE SPEED  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `(Inter EV tendre Chenille and (Engine speed [rpm] < 1500)) OR SARTING`
- Lit : ``, `Engine speed`, `Inter EV tendre Chenille`, `SARTING`
- Utilisé par : `Accélération Thermique`
- Ligne export : 20025 · id 21737

#### Tension Speed  `FP`
- Propriétés : Unit=rpm · Mode selector=Engine type · Default mode: VW 2.0L={1200} · Mode 1: FORD 1.5L={2000}
- Lit : `Engine type`
- Utilisé par : `Accélération Thermique`, `Adjust group: Master Engine`, `Single adjust item: Tension Speed`
- Ligne export : 20093 · id 21774

#### Accélération Thermique  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin((MaxOf((NEED MORE SPEED * Tension Speed [rpm]), Calcul Accélération [rpm])): 1000->0, 2800->100, Freeze)`
- Lit : ``, `Calcul Accélération`, `NEED MORE SPEED`, `Tension Speed`
- Utilisé par : `TSC1 Filter`
- Ligne export : 20107 · id 14354

#### TSC1 Filter  `SFC`
- Propriétés : Input channel=Accélération Thermique [%] · Enable=Yes · Type=Slopes · Slopes={{TSC1 Filter Slope [%/s]; TSC1 Filter Slope [%/s]}; {TSC1 Filter Slope [%/s]; TSC1 Filter Slope [%/s]}}
- Lit : `Accélération Thermique`, `TSC1 Filter Slope`
- Utilisé par : `TSC1-A:J1939-0`
- Ligne export : 20172 · id 14362

#### TSC1-A:J1939-0  `TSC1`
- Propriétés : J1939 source address=Default · Engine speed limits={1000; 2800} · Speed channel=TSC1 Filter [%] · Priority=3 · Transmit rate=20 · Override control mode=Speed control · Speed control conditions=Transient optimized, disengaged · Override control mode priority=Highest · Use checksum/counter=No · Control purpose=P32 = Temporary Powertrain Control (Original use of TSC1 Command) · Module=J1939[0] · Module index=0
- Lit : `Speed`, `TSC1 Filter`
- Utilisé par : *(personne)*
- Ligne export : 20190 · id 14363

#### SARTING  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  - **Activating** = `PositiveFlank(Engine START)`
- Lit : ``, `Engine START`
- Utilisé par : `NEED MORE SPEED`
- Ligne export : 20213 · id 24109
