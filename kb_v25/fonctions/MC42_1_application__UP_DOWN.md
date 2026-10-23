# MC42[1] application — UP/DOWN

47 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## UP/DOWN

#### Engine Stop Fonction Output  `FGI`
- Propriétés : Input type=Digital · Input=Engines Not Ready · Default state name=Default state
- Lit : `Engines Not Ready`
- Utilisé par : `Block`, `Inter EV By Pass`, `Inter EV DOWN Delay`, `Inter EV UP Delay`, `Inter EV tendre`, `Unblock`
- Ligne export : 62169 · id 38228

#### Pression Blocage Bras  `VIN`
- Propriétés : Unit=bar · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-SP500 · Calibration={500; 4500; 0; 500} · Alarms={No; 0; No; 100} · Module=MC42[1] · Module index=1
- Utilisé par : `OK BLOC`, `OK UP/DOWN`, `MD4-10 page: INFO`, `Measure group: Hydraulic`
- Ligne export : 62180 · id 38230

#### OK UP/DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=500
- Logique :
  - **Activating** = `Pression Blocage Bras [bar] <= 8`
  - **Blocking** = `EV Tension Force Open`
- Lit : `EV Tension Force Open`, `Pression Blocage Bras`
- Utilisé par : `Inter EV DOWN`, `Inter EV UP`, `OK UP/DOWN output`
- Ligne export : 62204 · id 38231

#### MD3 - UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `UP/DOWN Button Input = 1`
- Lit : `UP/DOWN Button Input`
- Utilisé par : `Block`, `Don'push button`, `HIGH`, `Inter EV UP Delay`, `Inter EV tendre`, `State Up/Down`
- Ligne export : 62256 · id 38239

#### Inter EV UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `MD3 - UP`
  - **Blocking** = `Engine Stop Fonction Output`
- Lit : `Engine Stop Fonction Output`, `MD3 - UP`
- Utilisé par : `Inter EV UP`, `Inter EV Verin`
- Ligne export : 62301 · id 38247

#### Inter EV UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP Delay) AND (OK UP/DOWN)`
- Lit : `Inter EV UP Delay`, `OK UP/DOWN`
- Utilisé par : `EV UP`
- Ligne export : 62351 · id 38256

#### EV UP  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter EV UP · Module=MC42[1] · Module index=9
- Lit : `Inter EV UP`
- Utilisé par : `Measure group: HVLP`
- Ligne export : 62401 · id 38265

#### MD3 - DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `UP/DOWN Button Input = 2`
- Lit : `UP/DOWN Button Input`
- Utilisé par : `Don'push button`, `HIGH`, `Inter EV DOWN Delay`, `Inter EV tendre`
- Ligne export : 62414 · id 38266

#### Inter EV DOWN Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `MD3 - DOWN`
  - **Blocking** = `Engine Stop Fonction Output`
- Lit : `Engine Stop Fonction Output`, `MD3 - DOWN`
- Utilisé par : `Inter EV DOWN`, `Inter EV Verin`
- Ligne export : 62459 · id 38274

#### Inter EV DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV DOWN Delay) AND (OK UP/DOWN)`
- Lit : `Inter EV DOWN Delay`, `OK UP/DOWN`
- Utilisé par : `EV DOWN`
- Ligne export : 62509 · id 38283

#### EV DOWN  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter EV DOWN · Module=MC42[1] · Module index=10
- Lit : `Inter EV DOWN`
- Utilisé par : `Measure group: HVLP`
- Ligne export : 62559 · id 38292

#### OK Tension  `FGI`
- Propriétés : Input type=Digital · Input=Super Ok tension · Default state name=Default state
- Lit : `Super Ok tension`
- Utilisé par : `Inter EV tendre`
- Ligne export : 62572 · id 38293

#### Inter EV tendre  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `OK Tension`
  - **Blocking** = `(Engine Stop Fonction Output) OR (MD3 - UP) OR (MD3 - DOWN)`
- Lit : `Engine Stop Fonction Output`, `MD3 - DOWN`, `MD3 - UP`, `OK Tension`
- Utilisé par : `Condition motor ON`, `LOW`
- Ligne export : 62583 · id 38294

#### M3 - RUN - with F  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Engine - Force ON) OR (M3 - Run)`
- Lit : `Engine - Force ON`, `M3 - Run`
- Utilisé par : `Condition motor ON`
- Ligne export : 62647 · id 38305

#### Condition motor ON  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(M3 - RUN - with F and Inter EV tendre) OR (EV Tension Force Open)`
- Lit : `EV Tension Force Open`, `Inter EV tendre`, `M3 - RUN - with F`
- Utilisé par : `EV Tendeur Chenille`
- Ligne export : 62697 · id 38314

#### EV Tendeur Chenille  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Condition motor ON · Module=MC42[1] · Module index=11
- Lit : `Condition motor ON`
- Utilisé par : `Measure group: HVLP`, `Measure group: Motor Hydrau`
- Ligne export : 62763 · id 38323

#### State Up/Down Raw  `IMAC`
- Logique :
  - **Controlling** = `CAN IN State Up/Down [%]`
- Lit : `CAN IN State Up/Down`
- Utilisé par : `Block`, `State Up/Down`
- Ligne export : 62776 · id 75717

#### Arms locks enable?  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `Block`, `Adjust group: Track Setup`, `Single adjust item: Arms locks enable?`
- Ligne export : 62817 · id 77887

#### Block  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `(State Up/Down Raw >= 100) AND (NegativeFlank(MD3 - UP)) AND (Arms locks enable?)`
  - **Blocking** = `Engine Stop Fonction Output`
- Lit : `Arms locks enable?`, `Engine Stop Fonction Output`, `MD3 - UP`, `State Up/Down Raw`
- Utilisé par : `Block IDC`, `Unblock`
- Ligne export : 62830 · id 38326

#### Test Mode Locking State  `SP`
- Propriétés : Input channel=None · Default state name=OFF · States={RUN}
- Utilisé par : `Test Mode Locking`
- Ligne export : 62897 · id 54261

#### Reset Startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset Startup`
- Lit : `Reset Startup`
- Utilisé par : `Reset Startup`, `Reset Startup`, `Test Mode Locking`
- Ligne export : 62909 · id 54286

#### Test Mode Locking  `MEM`
- Propriétés : Input channel=Test Mode Locking State · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : `Reset Startup`, `Test Mode Locking State`
- Utilisé par : `Test Mode On`, `Adjust group: Maintenance`, `Single adjust item: Test Mode Locking`
- Ligne export : 62959 · id 54263

#### Test Mode On  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Test Mode Locking = 1`
- Lit : `Test Mode Locking`
- Utilisé par : `LOCK`, `Oscilator`
- Ligne export : 63002 · id 54299

#### Oscilator  `IDC`
- Propriétés : Toggle=No · Delay on=7000 · Delay off=0
- Logique :
  - **Activating** = `Test Mode On`
  - **Blocking** = `Oscilator`
- Lit : `Test Mode On`
- Utilisé par : `Bloc Test`
- Ligne export : 63047 · id 54317

#### Bloc Test  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `PositiveFlank(Oscilator)`
- Lit : `Oscilator`
- Utilisé par : `Block IDC`, `UnBlock Test`
- Ligne export : 63097 · id 54338

#### Block IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Block OR (Bloc Test)`
- Lit : `Bloc Test`, `Block`
- Utilisé par : `EV Blocage bras`, `LOCK`
- Ligne export : 63141 · id 54392

#### EV Blocage bras  `DOUT`
- Propriétés : Delay on=1000 · Delay off=0 · Input channel=Block IDC · Module=MC42[1] · Module index=13
- Lit : `Block IDC`
- Utilisé par : `Measure group: HVLP`
- Ligne export : 63191 · id 38337

#### LOCK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `(Block IDC) OR (Test Mode On)`
- Lit : `Block IDC`, `Test Mode On`
- Utilisé par : `Engine hydro`, `HIGH`, `LOW`
- Ligne export : 63204 · id 54428

#### HIGH  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(MD3 - UP) OR (MD3 - DOWN)`
  - **Blocking** = `LOCK`
- Lit : `LOCK`, `MD3 - DOWN`, `MD3 - UP`
- Utilisé par : `Engine hydro`, `LOW`
- Ligne export : 63254 · id 38372

#### LOW  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Inter EV tendre) OR NegativeFlank(HIGH)`
  - **Blocking** = `LOCK`
- Lit : `HIGH`, `Inter EV tendre`, `LOCK`
- Utilisé par : `Engine hydro`
- Ligne export : 63311 · id 38382

#### Engine hydro  `SMC`
- Propriétés : Default state name=OFF
- Fonction *LOW* :
  - **Activating** = `LOW`
  - **Blocking** = `HIGH`
- Fonction *HIGHT* :
  - **Activating** = `HIGH`
- Fonction *LOCK* :
  - **Activating** = `LOCK`
- Lit : `HIGH`, `LOCK`, `LOW`
- Utilisé par : `Engine hydro Speed`
- Ligne export : 63369 · id 38392

#### LOW SPEED  `IP`
- Propriétés : Unit=rpm · Default mode={-2000}
- Utilisé par : `End of Tension Phase Delay`, `Engine hydro Speed`, `Single adjust item: Low Speed Pump`
- Ligne export : 63478 · id 38458

#### HIGH SPEED  `IP`
- Propriétés : Unit=rpm · Default mode={-2500}
- Utilisé par : `Engine hydro Speed`, `Single adjust item: Hight Speed Pump`
- Ligne export : 63490 · id 38459

#### LOCK SPEED  `IP`
- Propriétés : Unit=rpm · Default mode={-1000}
- Utilisé par : `Engine hydro Speed`, `Adjust group: Master Track`, `Single adjust item: LOCK SPEED`
- Ligne export : 63502 · id 54410

#### Engine hydro Speed  `IMAC`
- Propriétés : Unit=rpm · Function selector=Engine hydro
- Fonction *OFF* :
  - **Controlling** = `0`
- Fonction *LOW* :
  - **Controlling** = `LOW SPEED [rpm]`
- Fonction *HIGHT* :
  - **Controlling** = `HIGH SPEED [rpm]`
- Fonction *LOCK* :
  - **Controlling** = `LOCK SPEED [rpm]`
- Lit : `Engine hydro`, `HIGH SPEED`, `LOCK SPEED`, `LOW SPEED`
- Utilisé par : `Inter EV By Pass`, `Speed`
- Ligne export : 63514 · id 38460

#### Start By Pass  `IP`
- Propriétés : Unit=ms · Default mode={0}
- Utilisé par : `Inter EV By Pass`, `Adjust group: Master Track`, `Single adjust item: Start By Pass`
- Ligne export : 63648 · id 69899

#### Stop By Pass  `IP`
- Propriétés : Unit=ms · Default mode={0}
- Utilisé par : `Inter EV By Pass`, `Adjust group: Master Track`, `Single adjust item: Stop By Pass`
- Ligne export : 63660 · id 69901

#### Inter EV By Pass  `IDC`
- Propriétés : Toggle=No · Delay on=Start By Pass [ms] · Delay off=Stop By Pass [ms]
- Logique :
  - **Activating** = `Engine hydro Speed [rpm] <> 0`
  - **Blocking** = `(Engine Stop Fonction Output) OR (EV Tension Force Open)`
- Lit : `EV Tension Force Open`, `Engine Stop Fonction Output`, `Engine hydro Speed`, `Start By Pass`, `Stop By Pass`
- Utilisé par : `EV BY PASS`
- Ligne export : 63672 · id 38338

#### EV BY PASS  `DOUT`
- Propriétés : Delay on=0 · Delay off=250 · Input channel=Inter EV By Pass · Module=MC42[1] · Module index=8
- Lit : `Inter EV By Pass`
- Utilisé par : `Measure group: HVLP`, `Measure group: Motor Hydrau`
- Ligne export : 63731 · id 38351

#### Inter EV Verin  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP Delay) OR (Inter EV DOWN Delay)`
- Lit : `Inter EV DOWN Delay`, `Inter EV UP Delay`
- Utilisé par : `Inter Ev Verin`, `Unblock`
- Ligne export : 63744 · id 38352

#### Unblock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter EV Verin`
  - **Blocking** = `(Engine Stop Fonction Output) OR Block`
- Lit : `Block`, `Engine Stop Fonction Output`, `Inter EV Verin`
- Utilisé par : `Unblock IDC`
- Ligne export : 63794 · id 38361

#### UnBlock Test  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=4000
- Logique :
  - **Activating** = `NegativeFlank(Bloc Test)`
- Lit : `Bloc Test`
- Utilisé par : `Unblock IDC`
- Ligne export : 63851 · id 54359

#### Unblock IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Unblock OR (UnBlock Test)`
- Lit : `UnBlock Test`, `Unblock`
- Utilisé par : `EV DÃ©blocage`
- Ligne export : 63895 · id 54381

#### EV DÃ©blocage  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Unblock IDC · Module=MC42[1] · Module index=12
- Lit : `Unblock IDC`
- Utilisé par : `Measure group: HVLP`
- Ligne export : 63945 · id 38371

#### Don'push button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True`
  - **Blocking** = `(MD3 - UP) OR (MD3 - DOWN)`
- Lit : `MD3 - DOWN`, `MD3 - UP`
- Utilisé par : `State Up/Down`
- Ligne export : 63958 · id 38405

#### OK BLOC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Pression Blocage Bras [bar] >= 100`
- Lit : `Pression Blocage Bras`
- Utilisé par : `State Up/Down`
- Ligne export : 64015 · id 38415

#### State Up/Down  `SMC`
- Propriétés : Default state name=Default state
- Fonction *DOWN* :
  - **Activating** = `((State Up/Down Raw < 25) and (State Up/Down Raw > 0)) OR ((State Up/Down Raw = 0) and MD3 - UP)`
  - **Blocking** = `Don'push button`
- Fonction *INTERMEDIATE* :
  - **Activating** = `(State Up/Down Raw >= 25) AND (State Up/Down Raw <= 75)`
  - **Blocking** = `Don'push button`
- Fonction *UP* :
  - **Activating** = `State Up/Down Raw > 75`
  - **Blocking** = `(Don'push button) OR ((State Up/Down Raw >= 98) and OK BLOC)`
- Fonction *UP AND BLOC* :
  - **Activating** = `(State Up/Down Raw >= 98) AND (OK BLOC)`
  - **Blocking** = `Don'push button`
- Lit : `C`, `Don'push button`, `MD3 - UP`, `OK BLOC`, `State Up/Down Raw`
- Utilisé par : `Up/DOWN STATE`
- Ligne export : 64060 · id 38423
