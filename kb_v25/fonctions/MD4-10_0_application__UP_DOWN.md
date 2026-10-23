# MD4-10[0] application — UP/DOWN

23 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## UP/DOWN

#### Virtual DOWN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `DOWN`, `DOWN Counter`, `Inter DOWN`, `Inter DOWN Delay`, `Inter UP`, `Inter UP Delay`, `UP Counter`, `MD4-10 page: MAIN`
- Ligne export : 2641 · id 41259

#### Virtual UP  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `DOWN Counter`, `Inter DOWN`, `Inter DOWN Delay`, `Inter UP`, `Inter UP Delay`, `UP`, `UP Counter`, `MD4-10 page: MAIN`
- Ligne export : 2651 · id 41260

#### Engine READY  `FGI`
- Propriétés : Input type=Digital · Input=Engine READY · Default state name=Default state
- Lit : `Engine READY`
- Utilisé par : `DOWN Counter`, `Inter DOWN`, `Inter DOWN Delay`, `Inter UP`, `Inter UP Delay`, `UP Counter`
- Ligne export : 2661 · id 41261

#### Inter UP Super Delay  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Inter UP Delay`
- Lit : `Inter UP Delay`
- Utilisé par : `Auto UP`, `UP Counter`
- Ligne export : 2672 · id 41262

#### Track UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `TRACK UP`
- Lit : `TRACK UP`
- Utilisé par : `UP Counter`
- Ligne export : 2715 · id 41270

#### UP Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(Inter UP Super Delay)`
  - **Resetting** = `(UP Counter >= 2) OR (PositiveFlank(Virtual DOWN)) OR (Track UP Delay) OR ((PositiveFlank(Virtual UP)) and (UP Counter = 1)) OR (NegativeFlank(Engine READY))`
- Lit : `Engine READY`, `Inter UP Super Delay`, `Track UP Delay`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Inter UP`, `Inter UP Delay`
- Ligne export : 2758 · id 41278

#### Inter UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(Virtual UP and Engine READY) OR (UP Counter)`
  - **Blocking** = `Virtual DOWN`
- Lit : `Engine READY`, `UP Counter`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Inter UP Super Delay`, `Timer UP/DOWN`, `UP/DOWN Choice`
- Ligne export : 2868 · id 41295

#### UP/DOWN Choice  `SMC`
- Propriétés : Default state name=IDLE
- Fonction *UP* :
  - **Activating** = `(Inter UP Delay) AND (Store TIMER UP/DOWN [ms] < Internal Value Timer UP/DOWN) AND (OK UP/DOWN)`
- Fonction *DOWN* :
  - **Activating** = `(Inter DOWN Delay) AND (Store TIMER UP/DOWN [ms] > 0) AND (OK UP/DOWN)`
- Lit : `Inter DOWN Delay`, `Inter UP Delay`, `Internal Value Timer UP/DOWN`, `OK UP/DOWN`, `Store TIMER UP/DOWN`
- Utilisé par : `Value UP/DOWN`
- Ligne export : 2941 · id 41307

#### Value UP/DOWN  `IP`
- Propriétés : Unit=ms · Mode selector=UP/DOWN Choice · Default mode: IDLE={0} · Mode 1: UP={10} · Mode 2: DOWN={-12}
- Lit : `UP/DOWN Choice`
- Utilisé par : `Store TIMER UP/DOWN`
- Ligne export : 3044 · id 41323

#### Inter DOWN Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(Virtual DOWN and Engine READY) OR (DOWN Counter)`
  - **Blocking** = `Virtual UP`
- Lit : `DOWN Counter`, `Engine READY`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Inter DOWN Super Delay`, `Timer UP/DOWN`, `UP/DOWN Choice`
- Ligne export : 3060 · id 41324

#### Timer UP/DOWN  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `(Inter UP Delay) OR (Inter DOWN Delay)`
  - **Resetting** = `Timer UP/DOWN [ms] > 100`
- Lit : `Inter DOWN Delay`, `Inter UP Delay`, `Timer UP/DOWN`
- Utilisé par : `Internal Value Timer UP/DOWN`, `Store TIMER UP/DOWN`, `Adjust group: Master Track`, `Single adjust item: Timer UP/DOWN`
- Ligne export : 3133 · id 41336

#### Store TIMER UP/DOWN  `MEM`
- Propriétés : Input channel=Value UP/DOWN [ms] · Action=Add · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `Timer UP/DOWN [ms] > 100`
  - **Resetting** = `0 > Store TIMER UP/DOWN [ms]`
- Lit : `Timer UP/DOWN`, `Value UP/DOWN`
- Utilisé par : `State Up/Down`, `TRACK DOWN`, `TRACK UP`, `UP/DOWN Choice`
- Ligne export : 3201 · id 41348

#### Timer UP/DOWN  `IP`
- Propriétés : Unit=s · Default mode={15}
- Utilisé par : `Internal Value Timer UP/DOWN`, `Store TIMER UP/DOWN`, `Timer UP/DOWN`, `Adjust group: Master Track`, `Single adjust item: Timer UP/DOWN`
- Ligne export : 3256 · id 41357

#### Internal Value Timer UP/DOWN  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `100 * Timer UP/DOWN [s]`
- Lit : `Timer UP/DOWN`
- Utilisé par : `State Up/Down`, `TRACK UP`, `UP/DOWN Choice`
- Ligne export : 3268 · id 41358

#### TRACK UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Store TIMER UP/DOWN [ms] >= Internal Value Timer UP/DOWN`
- Lit : `Internal Value Timer UP/DOWN`, `Store TIMER UP/DOWN`
- Utilisé par : `TRACK UP`, `Track UP Delay`
- Ligne export : 3312 · id 41366

#### Inter DOWN Super Delay  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Inter DOWN Delay`
- Lit : `Inter DOWN Delay`
- Utilisé par : `Auto DOWN`, `DOWN Counter`
- Ligne export : 3357 · id 41374

#### TRACK DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Store TIMER UP/DOWN [ms] <= 0`
- Lit : `Store TIMER UP/DOWN`
- Utilisé par : `A/C In Water?`, `Auto Fast after Down IDC`, `KTB K11 IDC - SearchLight`, `OK Buz`, `Ok to move`, `Track DOWN Delay`, `Statistics log: Logs`
- Ligne export : 3400 · id 41382

#### Track DOWN Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `TRACK DOWN`
- Lit : `TRACK DOWN`
- Utilisé par : `DOWN Counter`
- Ligne export : 3445 · id 41390

#### DOWN Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(Inter DOWN Super Delay)`
  - **Resetting** = `(DOWN Counter >= 2) OR (PositiveFlank(Virtual UP)) OR (Track DOWN Delay) OR ((PositiveFlank(Virtual DOWN)) and (DOWN Counter = 1)) OR (NegativeFlank(Engine READY))`
- Lit : `Engine READY`, `Inter DOWN Super Delay`, `Track DOWN Delay`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `Inter DOWN`, `Inter DOWN Delay`
- Ligne export : 3488 · id 41398

#### Inter DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Virtual DOWN and Engine READY) OR (DOWN Counter)`
  - **Blocking** = `Virtual UP`
- Lit : `DOWN Counter`, `Engine READY`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `UP/DOWN Button`
- Ligne export : 3598 · id 41416

#### Inter UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Virtual UP and Engine READY) OR (UP Counter)`
  - **Blocking** = `Virtual DOWN`
- Lit : `Engine READY`, `UP Counter`, `Virtual DOWN`, `Virtual UP`
- Utilisé par : `UP/DOWN Button`
- Ligne export : 3671 · id 41428

#### State Up/Down  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `(Store TIMER UP/DOWN [ms] / Internal Value Timer UP/DOWN) * 100`
- Lit : `Internal Value Timer UP/DOWN`, `Store TIMER UP/DOWN`
- Utilisé par : `State Up/Down output`
- Ligne export : 3744 · id 41440

#### UP/DOWN Button  `SMC`
- Propriétés : Default state name=IDLE
- Fonction *UP* :
  - **Activating** = `Inter UP`
- Fonction *DOWN* :
  - **Activating** = `Inter DOWN`
- Lit : `Inter DOWN`, `Inter UP`
- Utilisé par : `UP/DOWN Button output`
- Ligne export : 3796 · id 41449
