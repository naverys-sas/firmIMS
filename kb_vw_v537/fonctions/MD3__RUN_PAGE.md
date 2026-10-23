# MD3 — RUN PAGE

49 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## RUN PAGE

#### Virtual DOWN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `DOWN`, `DOWN Counter`, `Inter DOWN`, `Inter DOWN Delay`, `Inter UP`, `Inter UP Delay`, `UP Counter`, `MD3 page: ENGINE PAGE`
- Ligne export : 1318 · id 6206

#### Virtual UP  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `DOWN Counter`, `Inter DOWN`, `Inter DOWN Delay`, `Inter UP`, `Inter UP Delay`, `UP`, `UP Counter`, `MD3 page: ENGINE PAGE`
- Ligne export : 1328 · id 6208

#### CAN - Engine Ready  `FGI`
- Propriétés : Input type=Digital · Input=CAN - ENGINE RUN - Out · Default state name=Default state
- Lit : `CAN - ENGINE RUN - Out`
- Utilisé par : `DOWN Counter`, `Inter DOWN`, `Inter DOWN Delay`, `Inter UP`, `Inter UP Delay`, `Timer Special Mode`, `UP Counter`
- Ligne export : 1338 · id 20441

#### UP/DOWN Mode  `DP`
- Propriétés : True text=Auto · False text=Manual · Default mode={False}
- Utilisé par : `DOWN Counter`, `Inter DOWN Super Delay`, `Inter UP Super Delay`, `UP Counter`, `Adjust group: Setup`, `Single adjust item: UP/DOWN Mode`
- Ligne export : 1349 · id 20513

#### Inter DOWN Super Delay  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Inter DOWN Delay`
  - **Blocking** = `not(UP/DOWN Mode)`
- Lit : ``, `Inter DOWN Delay`, `UP/DOWN Mode`
- Utilisé par : `DOWN Counter`, `DOWN Super`
- Ligne export : 1362 · id 20343

#### Track DOWN Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `TRACK DOWN`
- Lit : ``, `TRACK DOWN`
- Utilisé par : `DOWN Counter`
- Ligne export : 1413 · id 20351

#### DOWN Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(Inter DOWN Super Delay)`
  - **Resetting** = `(DOWN Counter >= 2) OR (PositiveFlank(Virtual UP)) OR (Track DOWN Delay) OR ((PositiveFlank(Virtual DOWN)) and (DOWN Counter = 1)) OR (NegativeFlank(CAN - Engine Ready)) OR (not(UP/DOWN Mode))`
- Lit : ``, `CAN - Engine Ready`, `Inter DOWN Super Delay`, `Track DOWN Delay`, `UP/DOWN Mode`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Inter DOWN`, `Inter DOWN Delay`
- Ligne export : 1456 · id 20326

#### Inter DOWN Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(Virtual DOWN and CAN - Engine Ready) OR (DOWN Counter)`
  - **Blocking** = `Virtual UP`
- Lit : ``, `CAN - Engine Ready`, `DOWN Counter`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Inter DOWN Super Delay`, `Timer UP/DOWN`, `UP/DOWN Choice`
- Ligne export : 1574 · id 8658

#### Timer UP/DOWN  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `(Inter UP Delay) OR (Inter DOWN Delay)`
  - **Resetting** = `Timer UP/DOWN [ms] > 100`
- Lit : ``, `Inter DOWN Delay`, `Inter UP Delay`, `Timer UP/DOWN`
- Utilisé par : `Internal Value Timer UP/DOWN`, `Store TIMER UP/DOWN`, `Adjust group: Master Setup`, `Single adjust item: Timer UP/DOWN`
- Ligne export : 1647 · id 8616

#### Value UP/DOWN  `IP`
- Propriétés : Unit=ms · Mode selector=UP/DOWN Choice · Default mode: IDLE={0} · Mode 1: UP={14} · Mode 2: DOWN={-10}
- Lit : `UP/DOWN Choice`
- Utilisé par : `Store TIMER UP/DOWN`
- Ligne export : 1715 · id 8599

#### Store TIMER UP/DOWN  `MEM`
- Propriétés : Input channel=Value UP/DOWN [ms] · Action=Add · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `Timer UP/DOWN [ms] > 100`
  - **Resetting** = `0 > Store TIMER UP/DOWN [ms]`
- Lit : ``, `Timer UP/DOWN`, `Value UP/DOWN`
- Utilisé par : `State Up/Down`, `TRACK DOWN`, `TRACK UP`, `UP/DOWN Choice`
- Ligne export : 1731 · id 8591

#### TRACK DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Store TIMER UP/DOWN [ms] <= 0`
- Lit : ``, `Store TIMER UP/DOWN`
- Utilisé par : `Auto Beach after Down`, `Intermediaire`, `Ok to move`, `TRACK DOWN`, `Track DOWN Delay`
- Ligne export : 1786 · id 6255

#### Inter UP Super Delay  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Inter UP Delay`
  - **Blocking** = `not(UP/DOWN Mode)`
- Lit : ``, `Inter UP Delay`, `UP/DOWN Mode`
- Utilisé par : `UP Counter`, `UP Super`
- Ligne export : 1831 · id 20301

#### Track UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `TRACK UP`
- Lit : ``, `TRACK UP`
- Utilisé par : `UP Counter`
- Ligne export : 1882 · id 20425

#### UP Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(Inter UP Super Delay)`
  - **Resetting** = `(UP Counter >= 2) OR (PositiveFlank(Virtual DOWN)) OR (Track UP Delay) OR ((PositiveFlank(Virtual UP)) and (UP Counter = 1)) OR (NegativeFlank(CAN - Engine Ready)) OR (not(UP/DOWN Mode))`
- Lit : ``, `CAN - Engine Ready`, `Inter UP Super Delay`, `Track UP Delay`, `UP/DOWN Mode`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Inter UP`, `Inter UP Delay`
- Ligne export : 1925 · id 20309

#### Inter UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(Virtual UP and CAN - Engine Ready) OR (UP Counter)`
  - **Blocking** = `Virtual DOWN`
- Lit : ``, `CAN - Engine Ready`, `UP Counter`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Inter UP Super Delay`, `Timer UP/DOWN`, `UP/DOWN Choice`
- Ligne export : 2043 · id 8685

#### Timer UP/DOWN  `IP`
- Propriétés : Unit=s · Default mode={14}
- Utilisé par : `Internal Value Timer UP/DOWN`, `Store TIMER UP/DOWN`, `Timer UP/DOWN`, `Adjust group: Master Setup`, `Single adjust item: Timer UP/DOWN`
- Ligne export : 2116 · id 8632

#### Internal Value Timer UP/DOWN  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `100 * Timer UP/DOWN [s]`
- Lit : ``, `Timer UP/DOWN`
- Utilisé par : `State Up/Down`, `TRACK UP`, `UP/DOWN Choice`
- Ligne export : 2128 · id 8637

#### OK UP/DOWN  `APPIN`
- Propriétés : Input channel=CAN OK UP/DOWN
- Lit : `CAN OK UP/DOWN`
- Utilisé par : `UP/DOWN Choice`
- Ligne export : 2172 · id 20793

#### UP/DOWN Choice  `SMC`
- Propriétés : Default state name=IDLE
- Fonction *UP* :
  - **Activating** = `(Inter UP Delay) AND (Store TIMER UP/DOWN [ms] < Internal Value Timer UP/DOWN) AND (OK UP/DOWN)`
- Fonction *DOWN* :
  - **Activating** = `(Inter DOWN Delay) AND (Store TIMER UP/DOWN [ms] > 0) AND (OK UP/DOWN)`
- Lit : ``, `Inter DOWN Delay`, `Inter UP Delay`, `Internal Value Timer UP/DOWN`, `OK UP/DOWN`, `Store TIMER UP/DOWN`
- Utilisé par : `Value UP/DOWN`
- Ligne export : 2181 · id 8600

#### TRACK UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Store TIMER UP/DOWN [ms] >= Internal Value Timer UP/DOWN`
- Lit : ``, `Internal Value Timer UP/DOWN`, `Store TIMER UP/DOWN`
- Utilisé par : `IDC Auto Sleep`, `Intermediaire`, `TRACK UP`, `Track UP Delay`
- Ligne export : 2284 · id 6251

#### Inter DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Virtual DOWN and CAN - Engine Ready) OR (DOWN Counter)`
  - **Blocking** = `Virtual UP`
- Lit : ``, `CAN - Engine Ready`, `DOWN Counter`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Action Down`, `UP/DOWN Button`
- Ligne export : 2329 · id 6216

#### Inter UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Virtual UP and CAN - Engine Ready) OR (UP Counter)`
  - **Blocking** = `Virtual DOWN`
- Lit : ``, `CAN - Engine Ready`, `UP Counter`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Action UP`, `UP/DOWN Button`
- Ligne export : 2402 · id 6220

#### Intermediaire  `IDC`
- Propriétés : Toggle=No · Delay on=100 · Delay off=100
- Logique :
  - **Activating** = `True`
  - **Blocking** = `(TRACK UP) OR (TRACK DOWN)`
- Lit : ``, `TRACK DOWN`, `TRACK UP`
- Utilisé par : `Action Down`, `Action UP`, `Timer Auto Sleep Engine`
- Ligne export : 2475 · id 6259

#### Action UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter UP) AND Intermediaire`
- Lit : ``, `Inter UP`, `Intermediaire`
- Utilisé par : `Show P-1-2`
- Ligne export : 2532 · id 6270

#### Action Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter DOWN) AND Intermediaire`
- Lit : ``, `Inter DOWN`, `Intermediaire`
- Utilisé par : `Show P-1-2`
- Ligne export : 2582 · id 6274

#### Time Sleep engine  `FP`
- Propriétés : Unit=s · Default mode={20}
- Utilisé par : `Process Down Engine`, `Timer Auto Sleep Engine`, `Timer sleep engine to Img`
- Ligne export : 2632 · id 6340

#### IDC Auto Sleep  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `PositiveFlank(TRACK UP)`
- Lit : ``, `TRACK UP`
- Utilisé par : `Timer Auto Sleep Engine`
- Ligne export : 2644 · id 12893

#### All Ask Stop  `FGI`
- Propriétés : Input type=Digital · Input=ALL ASK STOP · Default state name=Default state
- Lit : `ALL ASK STOP`
- Utilisé par : `Timer Auto Sleep Engine`
- Ligne export : 2688 · id 12948

#### Timer Auto Sleep Engine  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=Time Sleep engine [s]
- Logique :
  - **Decreasing** = `(IDC Auto Sleep) OR (Inside(Timer Auto Sleep Engine [s], 0, Time Sleep engine [s]))`
  - **Resetting** = `Intermediaire OR (All Ask Stop)`
- Lit : ``, `All Ask Stop`, `IDC Auto Sleep`, `Intermediaire`, `Time Sleep engine`
- Utilisé par : `ASK STOP`, `Process Down Engine`, `Timer sleep engine to Img`
- Ligne export : 2699 · id 12921

#### ASK STOP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Timer Auto Sleep Engine [s] <= 0`
- Lit : ``, `Timer Auto Sleep Engine`
- Utilisé par : `ALL ASK STOP`
- Ligne export : 2775 · id 6342

#### Process Down Engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inside(Timer Auto Sleep Engine [s], 0, Time Sleep engine [s])`
- Lit : ``, `Time Sleep engine`, `Timer Auto Sleep Engine`
- Utilisé par : `Mini Wait`, `Statistics log: System 2 log`
- Ligne export : 2820 · id 6358

#### State Up/Down  `IMAC`
- Logique :
  - **Controlling** = `(Store TIMER UP/DOWN [ms] / Internal Value Timer UP/DOWN) * 100`
- Lit : ``, `Internal Value Timer UP/DOWN`, `Store TIMER UP/DOWN`
- Utilisé par : `CAN OUT State Up/Down`, `State Up/Down`
- Ligne export : 2866 · id 10357

#### State Up/Down  `SMC`
- Propriétés : Default state name=Default state
- Fonction *0* :
  - **Activating** = `State Up/Down < 25`
- Fonction *1* :
  - **Activating** = `(State Up/Down >= 25) AND (State Up/Down <= 75)`
- Fonction *2* :
  - **Activating** = `State Up/Down > 75`
- Lit : ``, `State Up/Down`
- Utilisé par : `CAN OUT State Up/Down`
- Ligne export : 2918 · id 10353

#### Mini Wait  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=150
- Logique :
  - **Activating** = `Process Down Engine`
- Lit : ``, `Process Down Engine`
- Utilisé par : `Show P-1-2`
- Ligne export : 3035 · id 14968

#### Show P-1-2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True`
  - **Blocking** = `(Action UP) OR (Action Down) OR (Mini Wait)`
- Lit : ``, `Action Down`, `Action UP`, `Mini Wait`
- Utilisé par : *(personne)*
- Ligne export : 3078 · id 10388

#### Timer sleep engine to Img  `IMAC`
- Logique :
  - **Controlling** = `((Timer Auto Sleep Engine [s] / Time Sleep engine [s]) * 100) / 15`
- Lit : ``, `C`, `Time Sleep engine`, `Timer Auto Sleep Engine`
- Utilisé par : `Timer sleep engine to Img`
- Ligne export : 3142 · id 10442

#### Timer sleep engine to Img  `SMC`
- Propriétés : Default state name=Default state
- Fonction *0* :
  - **Activating** = `Timer sleep engine to Img = 0`
- Fonction *1* :
  - **Activating** = `Timer sleep engine to Img = 1`
- Fonction *2* :
  - **Activating** = `Timer sleep engine to Img = 2`
- Fonction *3* :
  - **Activating** = `Timer sleep engine to Img = 3`
- Fonction *4* :
  - **Activating** = `Timer sleep engine to Img = 4`
- Fonction *5* :
  - **Activating** = `Timer sleep engine to Img = 5`
- Fonction *6* :
  - **Activating** = `Timer sleep engine to Img = 6`
- Fonction *7* :
  - **Activating** = `Timer sleep engine to Img = 7`
- Lit : ``, `Timer sleep engine to Img`
- Utilisé par : *(personne)*
- Ligne export : 3203 · id 10450

#### UP/DOWN Special mode  `SP`
- Propriétés : Input channel=None · Default state name=UNACTIVE · States={ACTIVE}
- Utilisé par : `Timer Special Mode`, `UP/DOWN Special mode`, `Adjust group: Master Setup`, `Single adjust item: UP/DOWN Special mode`
- Ligne export : 3476 · id 24488

#### Reset Startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset Startup`
- Lit : ``
- Utilisé par : `UP/DOWN Special mode`
- Ligne export : 3488 · id 24537

#### UP/DOWN Special mode  `MEM`
- Propriétés : Input channel=UP/DOWN Special mode · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : ``, `Reset Startup`, `UP/DOWN Special mode`
- Utilisé par : `Timer Special Mode`, `Adjust group: Master Setup`, `Single adjust item: UP/DOWN Special mode`
- Ligne export : 3538 · id 24499

#### Timer Special Mode  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `1 = UP/DOWN Special mode`
  - **Resetting** = `(Timer Special Mode [s] > 45) OR (CAN - Engine Ready = 0)`
- Lit : ``, `CAN - Engine Ready`, `UP/DOWN Special mode`
- Utilisé par : `1 - UP Special`, `2 - DOWN Special`, `3 - Forward`, `4 - Backward`
- Ligne export : 3581 · id 24464

#### 1 - UP Special  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inside(Timer Special Mode [s], 2, 10)`
- Lit : ``, `Timer Special Mode`
- Utilisé par : `UP/DOWN Button`
- Ligne export : 3653 · id 24550

#### 2 - DOWN Special  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inside(Timer Special Mode [s], 12, 22)`
- Lit : ``, `Timer Special Mode`
- Utilisé par : `UP/DOWN Button`
- Ligne export : 3699 · id 24563

#### UP/DOWN Button  `SMC`
- Propriétés : Default state name=IDLE
- Fonction *UP* :
  - **Activating** = `(Inter UP) OR (1 - UP Special)`
- Fonction *DOWN* :
  - **Activating** = `(Inter DOWN) OR (2 - DOWN Special)`
- Lit : ``, `1 - UP Special`, `2 - DOWN Special`, `Inter DOWN`, `Inter UP`
- Utilisé par : `Can Out UP/DOWN Button`
- Ligne export : 3745 · id 12715

#### Can Out UP/DOWN Button  `APPOUT`
- Propriétés : Input channel=UP/DOWN Button · Send method=On change · Transmit rate=1000
- Lit : `UP/DOWN Button`
- Utilisé par : `Can In MD3 UP/DOWN Button`
- Ligne export : 3830 · id 12714

#### CAN OUT State Up/Down  `APPOUT`
- Propriétés : Input channel=State Up/Down · Send method=On change · Transmit rate=1000
- Lit : `State Up/Down`
- Utilisé par : `CAN IN State Up/Down`
- Ligne export : 3841 · id 20573

#### 3 - Forward  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inside(Timer Special Mode [s], 25, 33)`
- Lit : ``, `Timer Special Mode`
- Utilisé par : `Math Droit`, `Math Gauche`
- Ligne export : 3852 · id 24595

#### 4 - Backward  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inside(Timer Special Mode [s], 35, 43)`
- Lit : ``, `Timer Special Mode`
- Utilisé par : `Math Droit`, `Math Gauche`
- Ligne export : 3898 · id 24614
