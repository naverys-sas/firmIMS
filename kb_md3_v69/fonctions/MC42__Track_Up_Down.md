# MC42 — Track Up/Down

40 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Track Up/Down

#### MD3 - UP  `IDC`
> arm up
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `UP/DOWN Button Input = 1`
- Lit : ``, `UP/DOWN Button Input`
- Utilisé par : `Don'push button`, `EV tendre Chenille`, `Inter EV UP Delay`, `Lock landing`, `State Up/Down`
- Ligne export : 11650 · id 26146

#### Inter EV UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `MD3 - UP`
  - **Blocking** = `not(Engine_Started)`
- Lit : ``, `Engine_Started`, `MD3 - UP`
- Utilisé par : `Inter EV UP`, `Inter EV Verin`
- Ligne export : 11695 · id 26154

#### MD3 - DOWN  `IDC`
> arm down
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `UP/DOWN Button Input = 2`
- Lit : ``, `UP/DOWN Button Input`
- Utilisé par : `Don'push button`, `EV tendre Chenille`, `Inter EV DOWN delay`
- Ligne export : 11746 · id 26163

#### Inter EV DOWN delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `MD3 - DOWN`
  - **Blocking** = `not(Engine_Started)`
- Lit : ``, `Engine_Started`, `MD3 - DOWN`
- Utilisé par : `Inter EV DOWN`, `Inter EV Verin`
- Ligne export : 11791 · id 26171

#### Locking UP Track  `DP`
- Propriétés : True text=ACTIVE · False text=NO ACTIVE · Default mode={True}
- Utilisé par : `Lock landing`, `Adjust group: Setup`, `Single adjust item: Locking UP Track`
- Ligne export : 11842 · id 26181

#### Number of lockers  `SP`
- Propriétés : Input channel=None · Default state name=One · States={Two}
- Utilisé par : `Locking Time`, `Adjust group: Master Config`, `Single adjust item: Number of lockers`
- Ligne export : 11855 · id 62554

#### Locking Time  `IP`
> Adapted to number of locker
- Propriétés : Unit=ms · Mode selector=Number of lockers · Default mode: One={1000} · Mode 1: Two={2500}
- Lit : `Number of lockers`
- Utilisé par : `Lock landing`
- Ligne export : 11867 · id 62556

#### Test Locker  `DP`
> Test lockers with engine started and arms down
- Propriétés : Default mode={False}
- Utilisé par : `Force Lock`, `Adjust group: Master Features`, `Single adjust item: Test Locker`
- Ligne export : 11881 · id 66648

#### Force Lock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `PositiveFlank(Test Locker)`
  - **Blocking** = `not(Engine_Started)`
- Lit : ``, `Engine_Started`, `Test Locker`
- Utilisé par : `Force Unlock`, `Lock landing`, `OK UP/DOWN`
- Ligne export : 11894 · id 65571

#### Lock landing  `IDC`
> locking arm in high position
- Propriétés : Toggle=No · Delay on=0 · Delay off=Locking Time [ms]
- Logique :
  - **Activating** = `((State Up/Down >= 100) and (NegativeFlank(MD3 - UP))) OR (Force Lock)`
  - **Blocking** = `(not(Locking UP Track)) OR not(Engine_Started)`
- Lit : ``, `Engine_Started`, `Force Lock`, `Locking Time`, `Locking UP Track`, `MD3 - UP`, `State Up/Down`
- Utilisé par : `HIGH arm`, `IDC EV By Pass`, `Inter Lock landing`, `LOW arm`, `Need Min Speed`, `Unlock landing`
- Ligne export : 11946 · id 26182

#### Inter EV Verin  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP Delay) OR (Inter EV DOWN delay)`
- Lit : ``, `Inter EV DOWN delay`, `Inter EV UP Delay`
- Utilisé par : `SPEED Engine`, `Super Ok tension`, `Unlock landing`
- Ligne export : 12031 · id 26193

#### Unlock landing  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter EV Verin`
  - **Blocking** = `(Lock landing) OR not(Engine_Started)`
- Lit : ``, `Engine_Started`, `Inter EV Verin`, `Lock landing`
- Utilisé par : `Inter Unlock`
- Ligne export : 12081 · id 26202

#### Force tension  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `EV tendre Chenille`
- Ligne export : 12139 · id 26240

#### With tension  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `EV tendre Chenille`, `Adjust group: Master Tracks`, `Single adjust item: With tension`
- Ligne export : 12152 · id 33264

#### EV tendre Chenille  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Super Ok tension) OR (Force tension)`
  - **Blocking** = `(MD3 - UP) OR (MD3 - DOWN) OR (not(With tension)) OR not(Engine_Started)`
- Lit : ``, `Engine_Started`, `Force tension`, `MD3 - DOWN`, `MD3 - UP`, `Super Ok tension`, `With tension`
- Utilisé par : `IDC EV By Pass`, `IDC Tension`, `Need Min Speed`
- Ligne export : 12165 · id 26241

#### Force EV By Pass  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `IDC EV By Pass`, `Inter EV By Pass`, `Adjust group: Master Features`, `Single adjust item: Force EV By Pass`
- Ligne export : 12245 · id 63111

#### Locking pressure  `VIN`
- Propriétés : Unit=bar · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-SP500 · Calibration={500; 4500; 0; 500} · Alarms={No; 0; No; 100} · Module=MC42 (MC42[1]) · Module index=1
- Utilisé par : `OK UP/DOWN`, `Adjust group: Master Tracks`, `Dual adjust item: Locking pressure`, `Measure group: Hydraulic`
- Ligne export : 12258 · id 26534

#### OK UP/DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Locking pressure [bar] <= 10`
  - **Blocking** = `Untighten OR (Force Lock)`
- Lit : ``, `Force Lock`, `Locking pressure`, `Untighten`
- Utilisé par : `Inter EV DOWN`, `Inter EV UP`, `OK UP/DOWN`, `OK UP/DOWN Input`
- Ligne export : 12282 · id 26302

#### Inter EV UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP Delay) AND (OK UP/DOWN)`
- Lit : ``, `Inter EV UP Delay`, `OK UP/DOWN`
- Utilisé par : `EV Up`, `HIGH arm`, `IDC EV By Pass`
- Ligne export : 12341 · id 26326

#### Inter EV DOWN  `IDC`
> tempo to make sure that bypass off before down
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV DOWN delay) AND (OK UP/DOWN)`
- Lit : ``, `Inter EV DOWN delay`, `OK UP/DOWN`
- Utilisé par : `EV Down`, `HIGH arm`, `IDC EV By Pass Down`, `Measure group: Hydraulic`
- Ligne export : 12391 · id 67754

#### IDC Tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(EV tendre Chenille) AND (Inter EV By Pass)`
- Lit : ``, `EV tendre Chenille`, `Inter EV By Pass`
- Utilisé par : `Inter Tension`
- Ligne export : 12441 · id 33246

#### Inter Tension  `IDC`
> Delay On to avoid emptying Tension before pression is raised
- Propriétés : Toggle=No · Delay on=300 · Delay off=0
- Logique :
  - **Activating** = `(IDC Tension) OR Untighten`
- Lit : ``, `IDC Tension`, `Untighten`
- Utilisé par : `EV Tension`
- Ligne export : 12491 · id 65780

#### HIGH arm  `IDC`
> arm high
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Inter EV UP) OR (Inter EV DOWN)`
  - **Blocking** = `Lock landing`
- Lit : ``, `Inter EV DOWN`, `Inter EV UP`, `Lock landing`
- Utilisé par : `IDC EV By Pass`, `LOW arm`
- Ligne export : 12541 · id 57285

#### LOW arm  `IDC`
> arm down/low
- Propriétés : Toggle=No · Delay on=0 · Delay off=1500
- Logique :
  - **Activating** = `(NegativeFlank(HIGH arm)) OR (Lock landing)`
- Lit : ``, `HIGH arm`, `Lock landing`
- Utilisé par : `IDC EV By Pass`
- Ligne export : 12598 · id 57295

#### IDC EV By Pass Down  `IDC`
> no tempo to make sure that bypass off before down
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter EV DOWN`
- Lit : ``, `Inter EV DOWN`
- Utilisé par : `IDC EV By Pass sel`
- Ligne export : 12649 · id 26346

#### IDC EV By Pass  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP) OR (EV tendre Chenille) OR (Lock landing) OR (HIGH arm) OR (LOW arm) OR (Force EV By Pass)`
- Lit : ``, `EV tendre Chenille`, `Force EV By Pass`, `HIGH arm`, `Inter EV UP`, `LOW arm`, `Lock landing`
- Utilisé par : `IDC EV By Pass sel`
- Ligne export : 12692 · id 67818

#### IDC EV By Pass sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(IDC EV By Pass) OR (IDC EV By Pass Down)`
- Lit : ``, `IDC EV By Pass`, `IDC EV By Pass Down`
- Utilisé par : `Inter EV By Pass`
- Ligne export : 12770 · id 67843

#### Inter EV By Pass  `IDC`
> By Pass required and min speed done. Attention: latching Event, stays true even if need min speed is false. Delay Off to avoid emtying consumer before opening by pass
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(IDC EV By Pass sel) AND (Min Speed Ok)   [verrouillé]`
  - **Blocking** = `((not(Force EV By Pass)) and Untighten) OR (not(IDC EV By Pass sel))`
- Lit : ``, `Force EV By Pass`, `IDC EV By Pass sel`, `Min Speed Ok`, `Untighten`
- Utilisé par : `EV By pass`, `IDC Tension`, `Inter Lock landing`, `Need Min Speed`, `Measure group: Thermic vs Hydraulic`
- Ligne export : 12820 · id 64204

#### Inter Lock landing  `IDC`
> delay before locking
- Propriétés : Toggle=No · Delay on=300 · Delay off=0
- Logique :
  - **Activating** = `(Lock landing) AND (Inter EV By Pass)`
- Lit : ``, `Inter EV By Pass`, `Lock landing`
- Utilisé par : `EV Lock`
- Ligne export : 12902 · id 65541

#### EV Lock  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter Lock landing · Module=MC42 (MC42[1]) · Module index=13
- Lit : `Inter Lock landing`
- Utilisé par : `Measure group: Hydraulic`
- Ligne export : 12952 · id 26301

#### EV Tension  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter Tension · Module=MC42 (MC42[1]) · Module index=11
- Lit : `Inter Tension`
- Utilisé par : `Measure group: Hydraulic`, `Measure group: Thermic vs Hydraulic`
- Ligne export : 12965 · id 26277

#### EV Up  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter EV UP · Module=MC42 (MC42[1]) · Module index=9
- Lit : `Inter EV UP`
- Utilisé par : `Measure group: Hydraulic`
- Ligne export : 12978 · id 26335

#### EV Down  `DOUT`
> tempo to make sure that bypass off before down
- Propriétés : Delay on=0 · Delay off=3000 · Input channel=Inter EV DOWN · Module=MC42 (MC42[1]) · Module index=10
- Lit : `Inter EV DOWN`
- Utilisé par : `Measure group: Hydraulic`
- Ligne export : 12991 · id 26345

#### EV By pass  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter EV By Pass · Module=MC42 (MC42[1]) · Module index=8
- Lit : `Inter EV By Pass`
- Utilisé par : `Measure group: Hydraulic`, `Measure group: Thermic vs Hydraulic`
- Ligne export : 13004 · id 26378

#### Force Unlock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `NegativeFlank(Force Lock)`
- Lit : ``, `Force Lock`
- Utilisé par : `Inter Unlock`
- Ligne export : 13017 · id 65592

#### Inter Unlock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Unlock landing) OR (Force Unlock)`
- Lit : ``, `Force Unlock`, `Unlock landing`
- Utilisé par : `EV Unlock`
- Ligne export : 13061 · id 65417

#### EV Unlock  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter Unlock · Module=MC42 (MC42[1]) · Module index=12
- Lit : `Inter Unlock`
- Utilisé par : `Measure group: Hydraulic`
- Ligne export : 13111 · id 26412

#### State Up/Down Raw  `IMAC`
- Logique :
  - **Controlling** = `State Up/Down`
- Lit : ``, `State Up/Down`
- Utilisé par : `State Up/Down`
- Ligne export : 13124 · id 56851

#### Don'push button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True`
  - **Blocking** = `(MD3 - UP) OR (MD3 - DOWN)`
- Lit : ``, `MD3 - DOWN`, `MD3 - UP`
- Utilisé par : `State Up/Down`
- Ligne export : 13165 · id 56919

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
- Utilisé par : `Lock landing`, `State Up/Down`, `State Up/Down Raw`, `Up/DOWN STATE`
- Ligne export : 13222 · id 56859
