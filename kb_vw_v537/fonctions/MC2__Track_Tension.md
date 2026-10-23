# MC2 — Track Tension

25 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Track Tension

#### Track pressure  `VIN`
- Propriétés : Unit=bar · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-SP500 · Calibration={500; 4500; 0; 500} · Alarms={No; 0; No; 100} · Module=MC2[1] · Module index=2
- Utilisé par : `OK UP/DOWN`, `Pression Filter`, `Track Tension Error`, `Measure group: Track pressure`
- Ligne export : 15133 · id 26281

#### Tracks pressure Mode  `SP`
> This channel is used to give unit and names to the MEM
- Propriétés : Input channel=None · Default state name=AUTO · States={UNTIGHTEN}
- Utilisé par : `IDC Free`, `ON/OFF/Untighed`, `Tension State`, `Tracks pressure Mode`, `Adjust group: Maintenance`, `MD3 page: BASE`, `Single adjust item: Tracks pressure Mode`
- Ligne export : 15157 · id 26282

#### Reset Startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset Startup`
- Lit : ``, `Reset Startup`
- Utilisé par : `Reset Startup`, `Tracks pressure Mode`
- Ligne export : 15169 · id 26284

#### Tracks pressure Mode  `MEM`
- Propriétés : Input channel=Tracks pressure Mode · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : ``, `Reset Startup`, `Tracks pressure Mode`
- Utilisé par : `IDC Free`, `ON/OFF/Untighed`, `Tension State`, `Adjust group: Maintenance`, `MD3 page: BASE`, `Single adjust item: Tracks pressure Mode`
- Ligne export : 15219 · id 26293

#### Wait engine start  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Engine START`
- Lit : ``, `Engine START`
- Utilisé par : `ON/OFF/Untighed`, `Ok tension`, `Tension State`, `Wait engine Stop`
- Ligne export : 15262 · id 26301

#### ON/OFF/Untighed  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ON* :
  - **Activating** = `Wait engine start`
  - **Blocking** = `Tracks pressure Mode`
- Fonction *UNTIGHTED* :
  - **Activating** = `Tracks pressure Mode`
- Lit : ``, `Tracks pressure Mode`, `Wait engine start`
- Utilisé par : `Super Ok tension`
- Ligne export : 15305 · id 26309

#### Pression Filter  `SFC`
- Propriétés : Input channel=Track pressure [bar] · Enable=Yes · Type=Slopes · Slopes={{50; 50}; {1; 1}}
- Lit : `Track pressure`
- Utilisé par : `Need Pressure`
- Ligne export : 15383 · id 26322

#### Time to tension  `IP`
- Propriétés : Unit=ms · Default mode={150}
- Utilisé par : `Super Ok tension`
- Ligne export : 15401 · id 26323

#### Ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `PositiveFlank(Wait engine start)`
- Lit : ``, `Wait engine start`
- Utilisé par : `Super Ok tension`
- Ligne export : 15413 · id 26324

#### 10 minutes auto tender  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=10
- Logique :
  - **Decreasing** = `Engine START`
  - **Resetting** = `10 minutes auto tender [min] <= 0`
- Lit : ``, `Engine START`
- Utilisé par : `Super Ok tension`
- Ligne export : 15457 · id 26332

#### Tension Pressure  `IP`
- Propriétés : Unit=bar · Default mode={160}
- Utilisé par : `Need Pressure`, `Adjust group: Master Tracks`, `Single adjust item: Tension Pressure`
- Ligne export : 15518 · id 26343

#### Need Pressure  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `Tension Pressure [bar] > Pression Filter [bar]`
- Lit : ``, `Pression Filter`, `Tension Pressure`
- Utilisé par : `Super Ok tension`
- Ligne export : 15530 · id 26344

#### Tension Error Parameter  `FP`
- Propriétés : Unit=% · Default mode={100}
- Utilisé par : `Over Tension`, `Adjust group: Master Tracks`, `Single adjust item: Tension Error Parameter`
- Ligne export : 15575 · id 26352

#### Delay Off super ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `Super Ok tension`
- Lit : ``, `Super Ok tension`
- Utilisé par : `Super Ok Tension Math`
- Ligne export : 15587 · id 26389

#### Super Ok Tension Math  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `Delay Off super ok tension * 100`
- Lit : ``, `Delay Off super ok tension`
- Utilisé par : `Slope Super Ok`
- Ligne export : 15630 · id 26397

#### Slope Super Ok  `SFC`
- Propriétés : Input channel=Super Ok Tension Math [%] · Enable=Yes · Type=Slopes · Slopes={{5; 1}; {2; 2}}
- Lit : `Super Ok Tension Math`
- Utilisé par : `Over Tension`
- Ligne export : 15673 · id 26405

#### Over Tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Over Tension) OR (Slope Super Ok [%] > Tension Error Parameter [%])`
  - **Blocking** = `not(Engine START)`
- Lit : ``, `Engine START`, `Slope Super Ok`, `Tension Error Parameter`
- Utilisé par : `Super Ok tension`, `Track Tension Error`, `Event log: Hydraulic and Engine Event`
- Ligne export : 15691 · id 26353

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
- Ligne export : 15751 · id 26363

#### Wait engine Stop  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=4000
- Logique :
  - **Activating** = `Wait engine start`
- Lit : ``, `Wait engine start`
- Utilisé par : `Tension State`
- Ligne export : 15887 · id 26406

#### Tension State  `SMC`
- Propriétés : Default state name=ON/OFF
- Fonction *Parking* :
  - **Activating** = `Wait engine Stop`
  - **Blocking** = `(Wait engine start) OR (Tracks pressure Mode)`
- Fonction *Unthingten* :
  - **Activating** = `Tracks pressure Mode`
- Fonction *Blocage* :
  - **Activating** = `Map PWM - blocage`
- Lit : ``, `Map PWM - blocage`, `Tracks pressure Mode`, `Wait engine Stop`, `Wait engine start`
- Utilisé par : `PWM Selector`
- Ligne export : 15930 · id 26414

#### Track Tension Error  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Track Tension Error · Text=Try a Calibrating (Setting/Maintenance). Use straight. Contact your service center. · Channel=Track pressure [bar]
- Logique :
  - **Showing** = `Over Tension`
- Lit : ``, `Over Tension`, `Track pressure`
- Utilisé par : *(personne)*
- Ligne export : 16046 · id 26428

#### PWM Max mA  `IP`
- Propriétés : Unit=mA · Default mode={900}
- Utilisé par : `PWM Pression tendeur`, `Adjust group: Master Tracks`, `Single adjust item: PWM Max mA`
- Ligne export : 16092 · id 26772

#### Parking  `IP`
- Propriétés : Unit=% · Default mode={50}
- Utilisé par : `PWM Selector`, `Adjust group: Master Tracks`, `Single adjust item: Parking`
- Ligne export : 16104 · id 26849

#### PWM Selector  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Tension State
- Fonction *ON/OFF* :
  - **Controlling** = `0`
- Fonction *Parking* :
  - **Controlling** = `Parking [%]`
- Fonction *Unthingten* :
  - **Controlling** = `100`
- Fonction *Blocage* : (vide)
- Lit : ``, `Parking`, `Tension State`
- Utilisé par : `PWM Pression tendeur`
- Ligne export : 16116 · id 26864

#### PWM Pression tendeur  `COUT`
- Propriétés : Bidirectional=No · BWL=0 · Device type=EM21DEG12 · Input channel=PWM Selector [%] · Default mode={{0; PWM Max mA [mA]; 250; 250}} · Module=MC2[1] · Module index=4
- Lit : `PWM Max mA`, `PWM Selector`
- Utilisé par : *(personne)*
- Ligne export : 16244 · id 26886
