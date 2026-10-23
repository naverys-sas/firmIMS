# MC42 — Track Up/Down

38 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Track Up/Down

#### MD3 - UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `UP/DOWN Button Input = 1`
- Lit : ``, `UP/DOWN Button Input`
- Utilisé par : `Bloc`, `Don'push button`, `Inter EV UP Delay`, `Inter EV tendre Chenille`, `State Up/Down`
- Ligne export : 11963 · id 26146

#### Inter EV UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `MD3 - UP`
  - **Blocking** = `Engine_Stopped`
- Lit : ``, `Engine_Stopped`, `MD3 - UP`
- Utilisé par : `Inter EV UP`, `Inter EV Verin`
- Ligne export : 12008 · id 26154

#### MD3 - DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `UP/DOWN Button Input = 2`
- Lit : ``, `UP/DOWN Button Input`
- Utilisé par : `Don'push button`, `Inter EV DOWN delay`, `Inter EV tendre Chenille`
- Ligne export : 12058 · id 26163

#### Inter EV DOWN delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `MD3 - DOWN`
  - **Blocking** = `Engine_Stopped`
- Lit : ``, `Engine_Stopped`, `MD3 - DOWN`
- Utilisé par : `Inter EV DOWN`, `Inter EV Verin`
- Ligne export : 12103 · id 26171

#### Locking UP Track  `DP`
- Propriétés : True text=ACTIVE · False text=NO ACTIVE · Default mode={True}
- Utilisé par : `Bloc`, `Adjust group: Setup`, `Single adjust item: Locking UP Track`
- Ligne export : 12153 · id 26181

#### Landing time bloking  `IP`
- Propriétés : Unit=ms · Mode selector=Landing Block Number · Default mode: One={1000} · Mode 1: Two={2500}
- Lit : `Landing Block Number`
- Utilisé par : `Locking Phase Duration`
- Ligne export : 12166 · id 62556

#### EV Bloc delay  `IP`
- Propriétés : Unit=ms · Default mode={0}
- Utilisé par : `EV Landing Lock`, `Locking Phase Duration`, `Adjust group: Master Electric`, `Single adjust item: EV Bloc delay`
- Ligne export : 12180 · id 63084

#### Locking Phase Duration  `IMAC`
- Propriétés : Unit=ms
- Logique :
  - **Controlling** = `Landing time bloking [ms] + EV Bloc delay [ms]`
- Lit : ``, `EV Bloc delay`, `Landing time bloking`
- Utilisé par : `Bloc`
- Ligne export : 12192 · id 63089

#### Bloc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=Locking Phase Duration [ms]
- Logique :
  - **Activating** = `(State Up/Down >= 100) AND (NegativeFlank(MD3 - UP))`
  - **Blocking** = `Engine_Stopped OR (not(Locking UP Track))`
- Lit : ``, `Engine_Stopped`, `Locking Phase Duration`, `Locking UP Track`, `MD3 - UP`, `State Up/Down`
- Utilisé par : `EV Landing Lock`, `HIGH`, `LOW`, `Libre`
- Ligne export : 12235 · id 26182

#### Inter EV Verin  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP Delay) OR (Inter EV DOWN delay)`
- Lit : ``, `Inter EV DOWN delay`, `Inter EV UP Delay`
- Utilisé par : `Libre`, `SPEED Engine`, `Super Ok tension`
- Ligne export : 12303 · id 26193

#### Libre  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter EV Verin`
  - **Blocking** = `Bloc OR Engine_Stopped`
- Lit : ``, `Bloc`, `Engine_Stopped`, `Inter EV Verin`
- Utilisé par : `EV Landing UnBlock`
- Ligne export : 12353 · id 26202

#### Force tension  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Inter EV tendre Chenille`
- Ligne export : 12410 · id 26240

#### With tension  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `Inter EV tendre Chenille`, `Adjust group: Master Tracks`, `Single adjust item: With tension`
- Ligne export : 12423 · id 33264

#### Inter EV tendre Chenille  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Super Ok tension) OR (Force tension)`
  - **Blocking** = `(MD3 - UP) OR (MD3 - DOWN) OR Engine_Stopped OR (not(With tension))`
- Lit : ``, `Engine_Stopped`, `Force tension`, `MD3 - DOWN`, `MD3 - UP`, `Super Ok tension`, `With tension`
- Utilisé par : `HIGH`, `IDC Tension`, `NEED MORE SPEED`
- Ligne export : 12436 · id 26241

#### IDC Tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Drive Type
- Fonction *Thermique* :
  - **Activating** = `(Inter EV tendre Chenille) OR Untingthen`
- Fonction *Electric* :
  - **Activating** = `(M3 - Run and Inter EV tendre Chenille) OR Untingthen`
- Lit : ``, `Drive Type`, `Inter EV tendre Chenille`, `M3 - Run`, `Untingthen`
- Utilisé par : `EV Tension`, `Inter EV By Pass`
- Ligne export : 12515 · id 33246

#### EV Tension  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=IDC Tension · Module=MC42 (MC42[1]) · Module index=11
- Lit : `IDC Tension`
- Utilisé par : `Measure group: Hydraulic`
- Ligne export : 12605 · id 26277

#### EV Landing Lock  `DOUT`
- Propriétés : Delay on=EV Bloc delay [ms] · Delay off=0 · Input channel=Bloc · Module=MC42 (MC42[1]) · Module index=13
- Lit : `Bloc`, `EV Bloc delay`
- Utilisé par : `Inter EV By Pass`, `Measure group: Hydraulic`
- Ligne export : 12618 · id 26301

#### Locking pressure  `VIN`
- Propriétés : Unit=bar · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-SP500 · Calibration={500; 4500; 0; 500} · Alarms={No; 0; No; 100} · Module=MC42 (MC42[1]) · Module index=1
- Utilisé par : `OK BLOC`, `OK UP/DOWN`, `Adjust group: Master Tracks`, `Dual adjust item: Locking pressure`, `Measure group: Hydraulic`
- Ligne export : 12631 · id 26534

#### OK UP/DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Locking pressure [bar] <= 10`
- Lit : ``, `Locking pressure`
- Utilisé par : `Inter EV DOWN`, `Inter EV UP`, `OK UP/DOWN`, `OK UP/DOWN Input`
- Ligne export : 12655 · id 26302

#### Inter EV UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP Delay) AND (OK UP/DOWN)`
- Lit : ``, `Inter EV UP Delay`, `OK UP/DOWN`
- Utilisé par : `EV Up`, `HIGH`, `Inter EV By Pass`
- Ligne export : 12700 · id 26326

#### EV Up  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter EV UP · Module=MC42 (MC42[1]) · Module index=9
- Lit : `Inter EV UP`
- Utilisé par : `Measure group: Hydraulic`, `Measure group: Pump Sevcon`
- Ligne export : 12750 · id 26335

#### Inter EV DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV DOWN delay) AND (OK UP/DOWN)`
- Lit : ``, `Inter EV DOWN delay`, `OK UP/DOWN`
- Utilisé par : `EV Down`, `HIGH`, `Inter EV By Pass`
- Ligne export : 12763 · id 26336

#### EV Down  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter EV DOWN · Module=MC42 (MC42[1]) · Module index=10
- Lit : `Inter EV DOWN`
- Utilisé par : `Measure group: Hydraulic`, `Measure group: Pump Sevcon`
- Ligne export : 12813 · id 26345

#### HIGH  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Inter EV tendre Chenille) OR (Inter EV UP) OR (Inter EV DOWN)`
  - **Blocking** = `Bloc`
- Lit : ``, `Bloc`, `Inter EV DOWN`, `Inter EV UP`, `Inter EV tendre Chenille`
- Utilisé par : `Engine hydro`, `Inter EV By Pass`, `LOW`
- Ligne export : 12826 · id 57285

#### LOW  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1500
- Logique :
  - **Activating** = `NegativeFlank(HIGH) OR Bloc`
- Lit : ``, `Bloc`, `HIGH`
- Utilisé par : `Engine hydro`, `Inter EV By Pass`
- Ligne export : 12890 · id 57295

#### Inter EV By Pass  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV DOWN) OR (Inter EV UP) OR (IDC Tension) OR (EV Landing Lock) OR HIGH OR LOW OR (Force EV By Pass)`
  - **Blocking** = `Untingthen and (not(Force EV By Pass))`
- Lit : ``, `EV Landing Lock`, `Force EV By Pass`, `HIGH`, `IDC Tension`, `Inter EV DOWN`, `Inter EV UP`, `LOW`, `Untingthen`
- Utilisé par : `EV By pass`
- Ligne export : 12941 · id 26346

#### EV By pass  `DOUT`
- Propriétés : Delay on=0 · Delay off=300 · Input channel=Inter EV By Pass · Module=MC42 (MC42[1]) · Module index=8
- Lit : `Inter EV By Pass`
- Utilisé par : `Measure group: Hydraulic`, `Measure group: Pump Sevcon`
- Ligne export : 13043 · id 26378

#### EV Landing UnBlock  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Libre · Module=MC42 (MC42[1]) · Module index=12
- Lit : `Libre`
- Utilisé par : `Measure group: Hydraulic`
- Ligne export : 13056 · id 26412

#### State Up/Down Raw  `IMAC`
- Logique :
  - **Controlling** = `State Up/Down`
- Lit : ``, `State Up/Down`
- Utilisé par : `State Up/Down`
- Ligne export : 13069 · id 56851

#### Don'push button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True`
  - **Blocking** = `(MD3 - UP) OR (MD3 - DOWN)`
- Lit : ``, `MD3 - DOWN`, `MD3 - UP`
- Utilisé par : `State Up/Down`
- Ligne export : 13110 · id 56919

#### State Up/Down  `SMC`
- Propriétés : Default state name=Error
- Fonction *DOWN* :
  - **Activating** = `((State Up/Down Raw < 25) and (State Up/Down Raw > 0)) OR ((State Up/Down Raw = 0) and MD3 - UP)`
  - **Blocking** = `Don'push button`
- Fonction *INTERMEDIATE* :
  - **Activating** = `(State Up/Down Raw >= 25) AND (State Up/Down Raw <= 75)`
  - **Blocking** = `Don'push button`
- Fonction *UP* :
  - **Activating** = `State Up/Down Raw > 75`
  - **Blocking** = `Don'push button`
- Lit : ``, `Don'push button`, `MD3 - UP`, `State Up/Down Raw`
- Utilisé par : `Bloc`, `State Up/Down`, `State Up/Down Raw`, `Up/DOWN STATE`
- Ligne export : 13167 · id 56859

#### OK BLOC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Locking pressure [bar] >= 100`
- Lit : ``, `Locking pressure`
- Utilisé par : *(personne)*
- Ligne export : 13348 · id 56948

#### Engine hydro  `SMC`
- Propriétés : Default state name=OFF
- Fonction *LOW* :
  - **Activating** = `LOW`
  - **Blocking** = `HIGH`
- Fonction *HIGHT* :
  - **Activating** = `HIGH`
- Lit : ``, `HIGH`, `LOW`
- Utilisé par : `Engine hydro Speed`
- Ligne export : 13393 · id 57305

#### LOW SPEED  `IP`
- Propriétés : Unit=rpm · Default mode={-2000}
- Utilisé par : `Engine hydro Speed`, `Adjust group: Master Electric`, `Single adjust item: LOW SPEED`
- Ligne export : 13471 · id 57318

#### HIGH SPEED  `IP`
- Propriétés : Unit=rpm · Default mode={-3000}
- Utilisé par : `Engine hydro Speed`, `Adjust group: Master Electric`, `Single adjust item: HIGH SPEED`
- Ligne export : 13483 · id 57319

#### Engine hydro Speed  `IMAC`
- Propriétés : Unit=rpm · Function selector=Engine hydro
- Fonction *OFF* :
  - **Controlling** = `0`
- Fonction *LOW* :
  - **Controlling** = `LOW SPEED [rpm]`
- Fonction *HIGHT* :
  - **Controlling** = `HIGH SPEED [rpm]`
- Lit : ``, `Engine hydro`, `HIGH SPEED`, `LOW SPEED`
- Utilisé par : `M3_Speed`
- Ligne export : 13495 · id 57320

#### Landing Block Number  `SP`
- Propriétés : Input channel=None · Default state name=One · States={Two}
- Utilisé par : `Landing time bloking`, `Adjust group: Master Config`, `Single adjust item: Landing Block Number`
- Ligne export : 13598 · id 62554

#### Force EV By Pass  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Inter EV By Pass`, `Adjust group: Master Features`, `Single adjust item: Force EV By Pass`
- Ligne export : 13610 · id 63111
