# MC2 — UP/DOWN TRACK

36 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## UP/DOWN TRACK

#### Can In MD3 UP/DOWN Button  `APPIN`
- Propriétés : Input channel=Can Out UP/DOWN Button
- Lit : `Can Out UP/DOWN Button`
- Utilisé par : `MD3 - DOWN`, `MD3 - UP`
- Ligne export : 11738 · id 12724

#### MD3 - UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Can In MD3 UP/DOWN Button = 1`
- Lit : ``, `Can In MD3 UP/DOWN Button`
- Utilisé par : `Bloc`, `Don'push button`, `Inter EV UP Delay`, `Inter EV tendre Chenille`, `State Up/Down`
- Ligne export : 11747 · id 12725

#### Inter EV UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `MD3 - UP`
  - **Blocking** = `Engine STOP`
- Lit : ``, `Engine STOP`, `MD3 - UP`
- Utilisé par : `Inter EV UP`, `Inter EV Verin`
- Ligne export : 11792 · id 1104

#### MD3 - DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Can In MD3 UP/DOWN Button = 2`
- Lit : ``, `Can In MD3 UP/DOWN Button`
- Utilisé par : `Don'push button`, `Inter EV DOWN delay`, `Inter EV tendre Chenille`
- Ligne export : 11842 · id 12729

#### Inter EV DOWN delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `MD3 - DOWN`
  - **Blocking** = `Engine STOP`
- Lit : ``, `Engine STOP`, `MD3 - DOWN`
- Utilisé par : `Inter EV DOWN`, `Inter EV Verin`
- Ligne export : 11887 · id 1100

#### CAN IN State Up/Down  `APPIN`
- Propriétés : Input channel=CAN OUT State Up/Down · Error value=0
- Lit : `CAN OUT State Up/Down`
- Utilisé par : `Bloc`, `State Up/Down Raw`
- Ligne export : 11937 · id 20621

#### Locking UP Track  `DP`
- Propriétés : True text=ACTIVE · False text=NO ACTIVE · Default mode={False}
- Utilisé par : `Bloc`, `Single adjust item: Locking Up Track`
- Ligne export : 11947 · id 20652

#### Bloc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `(CAN IN State Up/Down >= 100) AND (NegativeFlank(MD3 - UP))`
  - **Blocking** = `(Engine STOP) OR (not(Locking UP Track))`
- Lit : ``, `CAN IN State Up/Down`, `Engine STOP`, `Locking UP Track`, `MD3 - UP`
- Utilisé par : `Libre`, `Map PWM - blocage`, `Map bloc - Blocage/selctor`, `Map bloc - tendeur Chenille`
- Ligne export : 11960 · id 20622

#### Inter EV Verin  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP Delay) OR (Inter EV DOWN delay)`
- Lit : ``, `Inter EV DOWN delay`, `Inter EV UP Delay`
- Utilisé par : `Libre`, `SPEED Engine`, `Super Ok tension`
- Ligne export : 12028 · id 2364

#### Libre  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter EV Verin`
  - **Blocking** = `Bloc OR (Engine STOP)`
- Lit : ``, `Bloc`, `Engine STOP`, `Inter EV Verin`
- Utilisé par : `Map bloc - Blocage/selctor`, `Map bloc - Déblocage`, `Map bloc - dé tendeur Chenille`
- Ligne export : 12078 · id 20635

#### Hydraulic Bloc  `SP`
- Propriétés : Input channel=None · Default state name=V01 · States={V01 - Locking; V17 - Locking}
- Utilisé par : `Active Locking`, `Inter EV By Pass`, `Map PWM - blocage`, `Map bloc - Blocage/selctor`, `Map bloc - Déblocage`, `Map bloc - dé tendeur Chenille`, `Map bloc - tendeur Chenille`, `OK UP/DOWN`, `Adjust group: Master Config`, `Single adjust item: Hydraulic Bloc`
- Ligne export : 12135 · id 21461

#### Force UNTIGHTEN  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Map bloc - dé tendeur Chenille`, `Adjust group: Master Setup`, `Single adjust item: Force UNTIGHTEN`
- Ligne export : 12148 · id 24634

#### Map bloc - dé tendeur Chenille  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Hydraulic Bloc
- Fonction *V01* :
  - **Activating** = `False OR (Force UNTIGHTEN)`
- Fonction *V01 - Locking* :
  - **Activating** = `Libre`
- Fonction *V17 - Locking* :
  - **Activating** = `False`
- Lit : ``, `Force UNTIGHTEN`, `Hydraulic Bloc`, `Libre`
- Utilisé par : `EV DéTendeur Chenille`
- Ligne export : 12161 · id 21501

#### EV DéTendeur Chenille  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Map bloc - dé tendeur Chenille · Module=MC2[1] · Module index=19
- Lit : `Map bloc - dé tendeur Chenille`
- Utilisé par : `Inter EV By Pass`, `Inter EV tendre Chenille`, `Measure group: Track pressure`
- Ligne export : 12273 · id 17129

#### Force tension  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Inter EV tendre Chenille`, `Adjust group: Master Setup`, `Single adjust item: Force tension`
- Ligne export : 12286 · id 21767

#### Inter EV tendre Chenille  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Super Ok tension) OR (Force tension)`
  - **Blocking** = `(MD3 - UP) OR (MD3 - DOWN) OR (EV DéTendeur Chenille) OR (Engine STOP)`
- Lit : ``, `EV DéTendeur Chenille`, `Engine STOP`, `Force tension`, `MD3 - DOWN`, `MD3 - UP`, `Super Ok tension`
- Utilisé par : `Map bloc - tendeur Chenille`, `NEED MORE SPEED`
- Ligne export : 12299 · id 1112

#### Map bloc - tendeur Chenille  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Hydraulic Bloc
- Fonction *V01* :
  - **Activating** = `Inter EV tendre Chenille`
- Fonction *V01 - Locking* :
  - **Activating** = `Bloc OR (Inter EV tendre Chenille)`
- Fonction *V17 - Locking* :
  - **Activating** = `Inter EV tendre Chenille`
- Lit : ``, `Bloc`, `Hydraulic Bloc`, `Inter EV tendre Chenille`
- Utilisé par : `EV Tendeur Chenille`
- Ligne export : 12377 · id 21490

#### EV Tendeur Chenille  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Map bloc - tendeur Chenille · Module=MC2[1] · Module index=18
- Lit : `Map bloc - tendeur Chenille`
- Utilisé par : `Inter EV By Pass`, `Measure group: Track pressure`
- Ligne export : 12489 · id 1062

#### Map bloc - Blocage/selctor  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Hydraulic Bloc
- Fonction *V01* :
  - **Activating** = `False`
- Fonction *V01 - Locking* :
  - **Activating** = `Libre OR Bloc`
- Fonction *V17 - Locking* :
  - **Activating** = `Bloc`
- Lit : ``, `Bloc`, `Hydraulic Bloc`, `Libre`
- Utilisé par : `EV - Select Blocage or Blocage`
- Ligne export : 12502 · id 21518

#### EV - Select Blocage or Blocage  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Map bloc - Blocage/selctor · Module=MC2[1] · Module index=2
- Lit : `Map bloc - Blocage/selctor`
- Utilisé par : `Inter EV By Pass`, `Measure group: Track pressure`
- Ligne export : 12614 · id 20562

#### OK UP/DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0 · Function selector=Hydraulic Bloc
- Fonction *V01* :
  - **Activating** = `True`
- Fonction *V01 - Locking* :
  - **Activating** = `(Track pressure [bar] <= 10) and (Locking pressure [bar] <= 10)`
- Fonction *V17 - Locking* :
  - **Activating** = `Locking pressure [bar] <= 10`
- Lit : ``, `Hydraulic Bloc`, `Locking pressure`, `Track pressure`
- Utilisé par : `CAN OK UP/DOWN`, `Inter EV DOWN`, `Inter EV UP`
- Ligne export : 12627 · id 20706

#### Inter EV UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP Delay) AND (OK UP/DOWN)`
- Lit : ``, `Inter EV UP Delay`, `OK UP/DOWN`
- Utilisé par : `EV Montée`
- Ligne export : 12754 · id 20756

#### EV Montée  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter EV UP · Module=MC2[1] · Module index=15
- Lit : `Inter EV UP`
- Utilisé par : `Inter EV By Pass`
- Ligne export : 12804 · id 1016

#### Inter EV DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV DOWN delay) AND (OK UP/DOWN)`
- Lit : ``, `Inter EV DOWN delay`, `OK UP/DOWN`
- Utilisé par : `EV Descente`
- Ligne export : 12817 · id 20765

#### EV Descente  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter EV DOWN · Module=MC2[1] · Module index=14
- Lit : `Inter EV DOWN`
- Utilisé par : `Inter EV By Pass`
- Ligne export : 12867 · id 1018

#### Inter EV By Pass  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Hydraulic Bloc
- Fonction *V01* :
  - **Activating** = `(EV Descente) OR (EV Montée) OR (EV Tendeur Chenille) OR (EV DéTendeur Chenille)`
- Fonction *V01 - Locking* :
  - **Activating** = `(EV Descente) OR (EV Montée) OR (EV Tendeur Chenille) OR (EV DéTendeur Chenille)`
- Fonction *V17 - Locking* :
  - **Activating** = `(EV Descente) OR (EV Montée) OR (EV Tendeur Chenille) OR (EV DéTendeur Chenille) OR (EV - Select Blocage or Blocage)`
- Lit : ``, `EV - Select Blocage or Blocage`, `EV Descente`, `EV DéTendeur Chenille`, `EV Montée`, `EV Tendeur Chenille`, `Hydraulic Bloc`
- Utilisé par : `EV By pass`
- Ligne export : 12880 · id 1096

#### EV By pass  `DOUT`
- Propriétés : Delay on=0 · Delay off=300 · Input channel=Inter EV By Pass · Module=MC2[1] · Module index=13
- Lit : `Inter EV By Pass`
- Utilisé par : *(personne)*
- Ligne export : 13055 · id 1019

#### CAN OK UP/DOWN  `APPOUT`
- Propriétés : Input channel=OK UP/DOWN · Send method=On change · Transmit rate=1000
- Lit : `OK UP/DOWN`
- Utilisé par : `OK UP/DOWN`
- Ligne export : 13068 · id 20722

#### Active Locking  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Hydraulic Bloc`
- Lit : ``, `Hydraulic Bloc`
- Utilisé par : `Active le groupe: UP/DOWN TRACK / Locking Track`, `Single adjust item: Locking Up Track`
- Ligne export : 13079 · id 21640

#### Map bloc - Déblocage  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Hydraulic Bloc
- Fonction *V01* :
  - **Activating** = `False`
- Fonction *V01 - Locking* :
  - **Activating** = `False`
- Fonction *V17 - Locking* :
  - **Activating** = `Libre`
- Lit : ``, `Hydraulic Bloc`, `Libre`
- Utilisé par : `EV - Dé blocage`
- Ligne export : 13162 · id 21535

#### EV - Dé blocage  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Map bloc - Déblocage · Module=MC2[1] · Module index=3
- Lit : `Map bloc - Déblocage`
- Utilisé par : *(personne)*
- Ligne export : 13267 · id 21488

#### Map PWM - blocage  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Hydraulic Bloc
- Fonction *V01* :
  - **Activating** = `False`
- Fonction *V01 - Locking* :
  - **Activating** = `Bloc`
- Fonction *V17 - Locking* :
  - **Activating** = `False`
- Lit : ``, `Bloc`, `Hydraulic Bloc`
- Utilisé par : `Tension State`
- Ligne export : 13280 · id 21687

#### State Up/Down Raw  `IMAC`
- Logique :
  - **Controlling** = `CAN IN State Up/Down`
- Lit : ``, `CAN IN State Up/Down`
- Utilisé par : `State Up/Down`
- Ligne export : 13385 · id 27364

#### Don'push button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True`
  - **Blocking** = `(MD3 - UP) OR (MD3 - DOWN)`
- Lit : ``, `MD3 - DOWN`, `MD3 - UP`
- Utilisé par : `State Up/Down`
- Ligne export : 13426 · id 27413

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
- Utilisé par : `Up/DOWN STATE`
- Ligne export : 13483 · id 27372

## UP/DOWN TRACK / Locking Track — actif seulement si `Active Locking`

#### Locking pressure  `VIN`
- Propriétés : Unit=bar · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-SP500 · Calibration={500; 4500; 0; 500} · Alarms={No; 0; No; 100} · Module=MC2[1] · Module index=3
- Utilisé par : `OK UP/DOWN`, `Measure group: Track pressure`
- Ligne export : 13137 · id 21468
