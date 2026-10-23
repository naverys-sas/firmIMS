# MD3 — UP/DOWN

40 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## UP/DOWN

#### Virtual DOWN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `DOWN`, `DOWN Counter`, `Inter DOWN`, `Inter DOWN Delay`, `Inter UP`, `Inter UP Delay`, `UP Counter`, `MD3 page: BASE`
- Ligne export : 1117 · id 6206

#### Virtual UP  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `DOWN Counter`, `Inter DOWN`, `Inter DOWN Delay`, `Inter UP`, `Inter UP Delay`, `UP`, `UP Counter`, `MD3 page: BASE`
- Ligne export : 1127 · id 6208

#### UP/DOWN Mode  `DP`
- Propriétés : True text=Auto · False text=Manual · Default mode={False}
- Utilisé par : `DOWN Counter`, `Inter DOWN Super Delay`, `Inter UP Super Delay`, `UP Counter`, `Adjust group: Setup`, `Single adjust item: UP/DOWN Mode`
- Ligne export : 1137 · id 20513

#### ENGINE RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `ENGINE RUN Input`
- Lit : ``, `ENGINE RUN Input`
- Utilisé par : `DOWN Counter`, `Inter DOWN`, `Inter DOWN Delay`, `Inter UP`, `Inter UP Delay`, `UP Counter`
- Ligne export : 1150 · id 36092

#### Inter DOWN Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(Virtual DOWN and ENGINE RUN) OR (DOWN Counter)`
  - **Blocking** = `Virtual UP`
- Lit : ``, `DOWN Counter`, `ENGINE RUN`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Inter DOWN Super Delay`, `Timer UP/DOWN`, `UP/DOWN Choice`
- Ligne export : 1193 · id 8658

#### Inter DOWN Super Delay  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Inter DOWN Delay`
  - **Blocking** = `not(UP/DOWN Mode)`
- Lit : ``, `Inter DOWN Delay`, `UP/DOWN Mode`
- Utilisé par : `DOWN Counter`, `DOWN Super`
- Ligne export : 1266 · id 20343

#### TRACK DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Store TIMER UP/DOWN [ms] <= 0`
- Lit : ``, `Store TIMER UP/DOWN`
- Utilisé par : `Auto Fast after Down`, `Intermediaire`, `Ok to move`, `TRACK DOWN`, `Track DOWN Delay`
- Ligne export : 1317 · id 6255

#### Track DOWN Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `TRACK DOWN`
- Lit : ``, `TRACK DOWN`
- Utilisé par : `DOWN Counter`
- Ligne export : 1362 · id 20351

#### DOWN Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(Inter DOWN Super Delay)`
  - **Resetting** = `(DOWN Counter >= 2) OR (PositiveFlank(Virtual UP)) OR (Track DOWN Delay) OR ((PositiveFlank(Virtual DOWN)) and (DOWN Counter = 1)) OR (NegativeFlank(ENGINE RUN)) OR (not(UP/DOWN Mode))`
- Lit : ``, `ENGINE RUN`, `Inter DOWN Super Delay`, `Track DOWN Delay`, `UP/DOWN Mode`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Inter DOWN`, `Inter DOWN Delay`
- Ligne export : 1405 · id 20326

#### Inter UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(Virtual UP and ENGINE RUN) OR (UP Counter)`
  - **Blocking** = `Virtual DOWN`
- Lit : ``, `ENGINE RUN`, `UP Counter`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Inter UP Super Delay`, `Timer UP/DOWN`, `UP/DOWN Choice`
- Ligne export : 1523 · id 8685

#### Timer UP/DOWN  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `(Inter UP Delay) OR (Inter DOWN Delay)`
  - **Resetting** = `Timer UP/DOWN [ms] > 100`
- Lit : ``, `Inter DOWN Delay`, `Inter UP Delay`, `Timer UP/DOWN`
- Utilisé par : `Internal Value Timer UP/DOWN`, `Store TIMER UP/DOWN`, `Adjust group: Master Config`, `Single adjust item: Timer UP/DOWN`
- Ligne export : 1596 · id 8616

#### UP/DOWN Choice  `SMC`
- Propriétés : Default state name=IDLE
- Fonction *UP* :
  - **Activating** = `(Inter UP Delay) AND (Store TIMER UP/DOWN [ms] < Internal Value Timer UP/DOWN) AND (OK UP/DOWN Input)`
- Fonction *DOWN* :
  - **Activating** = `(Inter DOWN Delay) AND (Store TIMER UP/DOWN [ms] > 0) AND (OK UP/DOWN Input)`
- Lit : ``, `Inter DOWN Delay`, `Inter UP Delay`, `Internal Value Timer UP/DOWN`, `OK UP/DOWN Input`, `Store TIMER UP/DOWN`
- Utilisé par : `Value UP/DOWN`
- Ligne export : 1664 · id 8600

#### Value UP/DOWN  `IP`
- Propriétés : Unit=ms · Mode selector=UP/DOWN Choice · Default mode: IDLE={0} · Mode 1: UP={14} · Mode 2: DOWN={-10}
- Lit : `UP/DOWN Choice`
- Utilisé par : `Store TIMER UP/DOWN`
- Ligne export : 1767 · id 8599

#### Store TIMER UP/DOWN  `MEM`
- Propriétés : Input channel=Value UP/DOWN [ms] · Action=Add · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `Timer UP/DOWN [ms] > 100`
  - **Resetting** = `0 > Store TIMER UP/DOWN [ms]`
- Lit : ``, `Timer UP/DOWN`, `Value UP/DOWN`
- Utilisé par : `State Up/Down`, `TRACK DOWN`, `TRACK UP`, `UP/DOWN Choice`
- Ligne export : 1783 · id 8591

#### Inter UP Super Delay  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Inter UP Delay`
  - **Blocking** = `not(UP/DOWN Mode)`
- Lit : ``, `Inter UP Delay`, `UP/DOWN Mode`
- Utilisé par : `UP Counter`, `UP Super`
- Ligne export : 1838 · id 20301

#### TRACK UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Store TIMER UP/DOWN [ms] >= Internal Value Timer UP/DOWN`
- Lit : ``, `Internal Value Timer UP/DOWN`, `Store TIMER UP/DOWN`
- Utilisé par : `IDC Auto Sleep`, `Intermediaire`, `TRACK UP`, `Track UP Delay`
- Ligne export : 1889 · id 6251

#### Track UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `TRACK UP`
- Lit : ``, `TRACK UP`
- Utilisé par : `UP Counter`
- Ligne export : 1934 · id 20425

#### UP Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(Inter UP Super Delay)`
  - **Resetting** = `(UP Counter >= 2) OR (PositiveFlank(Virtual DOWN)) OR (Track UP Delay) OR ((PositiveFlank(Virtual UP)) and (UP Counter = 1)) OR (NegativeFlank(ENGINE RUN)) OR (not(UP/DOWN Mode))`
- Lit : ``, `ENGINE RUN`, `Inter UP Super Delay`, `Track UP Delay`, `UP/DOWN Mode`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Inter UP`, `Inter UP Delay`
- Ligne export : 1977 · id 20309

#### Timer UP/DOWN  `IP`
- Propriétés : Unit=s · Default mode={14}
- Utilisé par : `Internal Value Timer UP/DOWN`, `Store TIMER UP/DOWN`, `Timer UP/DOWN`, `Adjust group: Master Config`, `Single adjust item: Timer UP/DOWN`
- Ligne export : 2095 · id 8632

#### Internal Value Timer UP/DOWN  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `100 * Timer UP/DOWN [s]`
- Lit : ``, `Timer UP/DOWN`
- Utilisé par : `State Up/Down`, `TRACK UP`, `UP/DOWN Choice`
- Ligne export : 2107 · id 8637

#### Inter DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Virtual DOWN and ENGINE RUN) OR (DOWN Counter)`
  - **Blocking** = `Virtual UP`
- Lit : ``, `DOWN Counter`, `ENGINE RUN`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Action Down`, `UP/DOWN Button`
- Ligne export : 2151 · id 6216

#### Inter UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Virtual UP and ENGINE RUN) OR (UP Counter)`
  - **Blocking** = `Virtual DOWN`
- Lit : ``, `ENGINE RUN`, `UP Counter`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Action UP`, `UP/DOWN Button`
- Ligne export : 2224 · id 6220

#### Intermediaire  `IDC`
- Propriétés : Toggle=No · Delay on=100 · Delay off=100
- Logique :
  - **Activating** = `True`
  - **Blocking** = `(TRACK UP) OR (TRACK DOWN)`
- Lit : ``, `TRACK DOWN`, `TRACK UP`
- Utilisé par : `Action Down`, `Action UP`, `Timer Auto Sleep Engine`
- Ligne export : 2297 · id 6259

#### Action UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter UP) AND Intermediaire`
- Lit : ``, `Inter UP`, `Intermediaire`
- Utilisé par : `Show P-1-2`
- Ligne export : 2354 · id 6270

#### Action Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter DOWN) AND Intermediaire`
- Lit : ``, `Inter DOWN`, `Intermediaire`
- Utilisé par : `Show P-1-2`
- Ligne export : 2404 · id 6274

#### Time Sleep engine  `FP`
- Propriétés : Unit=s · Default mode={20}
- Utilisé par : `Process Down Engine`, `Timer Auto Sleep Engine`, `Timer sleep engine to Img`
- Ligne export : 2454 · id 6340

#### IDC Auto Sleep  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `PositiveFlank(TRACK UP)`
- Lit : ``, `TRACK UP`
- Utilisé par : `Timer Auto Sleep Engine`
- Ligne export : 2466 · id 12893

#### All Ask Stop  `FGI`
- Propriétés : Input type=Digital · Input=ALL ASK STOP · Default state name=Default state
- Lit : `ALL ASK STOP`
- Utilisé par : `Timer Auto Sleep Engine`
- Ligne export : 2510 · id 12948

#### Timer Auto Sleep Engine  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=Time Sleep engine [s]
- Logique :
  - **Decreasing** = `(IDC Auto Sleep) OR (Inside(Timer Auto Sleep Engine [s], 0, Time Sleep engine [s]))`
  - **Resetting** = `Intermediaire OR (All Ask Stop)`
- Lit : ``, `All Ask Stop`, `IDC Auto Sleep`, `Intermediaire`, `Time Sleep engine`
- Utilisé par : `ASK STOP`, `Process Down Engine`, `Timer sleep engine to Img`
- Ligne export : 2521 · id 12921

#### ASK STOP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Timer Auto Sleep Engine [s] <= 0`
- Lit : ``, `Timer Auto Sleep Engine`
- Utilisé par : `ALL ASK STOP`
- Ligne export : 2597 · id 6342

#### Process Down Engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inside(Timer Auto Sleep Engine [s], 0, Time Sleep engine [s])`
- Lit : ``, `Time Sleep engine`, `Timer Auto Sleep Engine`
- Utilisé par : `Mini Wait`, `Statistics log: System Stats`
- Ligne export : 2642 · id 6358

#### State Up/Down  `IMAC`
- Logique :
  - **Controlling** = `(Store TIMER UP/DOWN [ms] / Internal Value Timer UP/DOWN) * 100`
- Lit : ``, `Internal Value Timer UP/DOWN`, `Store TIMER UP/DOWN`
- Utilisé par : `State Up/Down`, `State Up/Down`
- Ligne export : 2688 · id 10357

#### State Up/Down  `SMC`
- Propriétés : Default state name=Default state
- Fonction *0* :
  - **Activating** = `State Up/Down < 25`
- Fonction *1* :
  - **Activating** = `(State Up/Down >= 25) AND (State Up/Down <= 75)`
- Fonction *2* :
  - **Activating** = `State Up/Down > 75`
- Lit : ``, `State Up/Down`
- Utilisé par : `State Up/Down`
- Ligne export : 2740 · id 10353

#### Mini Wait  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=50
- Logique :
  - **Activating** = `Process Down Engine`
- Lit : ``, `Process Down Engine`
- Utilisé par : `Show P-1-2`
- Ligne export : 2857 · id 14968

#### Show P-1-2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True`
  - **Blocking** = `(Action UP) OR (Action Down) OR (Mini Wait)`
- Lit : ``, `Action Down`, `Action UP`, `Mini Wait`
- Utilisé par : `Show Debug`
- Ligne export : 2900 · id 10388

#### Timer sleep engine to Img  `IMAC`
- Logique :
  - **Controlling** = `((Timer Auto Sleep Engine [s] / Time Sleep engine [s]) * 100) / 15`
- Lit : ``, `C`, `Time Sleep engine`, `Timer Auto Sleep Engine`
- Utilisé par : `Timer sleep engine to Img`
- Ligne export : 2964 · id 10442

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
- Ligne export : 3025 · id 10450

#### UP/DOWN Button  `SMC`
- Propriétés : Default state name=IDLE
- Fonction *UP* :
  - **Activating** = `Inter UP`
- Fonction *DOWN* :
  - **Activating** = `Inter DOWN`
- Lit : ``, `Inter DOWN`, `Inter UP`
- Utilisé par : `UP/DOWN Button`, `UP/DOWN Button Input`
- Ligne export : 3298 · id 12715

#### Debug Mode  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Show Debug`
- Ligne export : 3369 · id 36097

#### Show Debug  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Show P-1-2 and Debug Mode`
- Lit : ``, `Debug Mode`, `Show P-1-2`
- Utilisé par : *(personne)*
- Ligne export : 3382 · id 36102
