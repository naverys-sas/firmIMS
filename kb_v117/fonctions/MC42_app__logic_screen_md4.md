# MC42 app — logic screen md4

260 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## logic screen md4

#### 4ET Automatic Joystick Inhibition  `IP`
- Propriétés : Unit=s · Default mode={300}
- Utilisé par : `Auto Off - Timer 4ET`, `Auto PAUSE/OFF 4ET`, `Single adjust item: Automatic Joystick Inhibition`
- Ligne export : 75853 · id 214069

#### 4ET Neutral Deadband Joystick  `FP`
- Propriétés : Unit=% · Default mode={10}
- Utilisé par : `Point mort Manip +`, `Point mort Manip -`, `Single adjust item: Neutral Deadband Joystick`
- Ligne export : 75865 · id 214070

#### Point mort Manip -  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `4ET Neutral Deadband Joystick [%] * -1`
- Lit : `4ET Neutral Deadband Joystick`
- Utilisé par : `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`
- Ligne export : 75877 · id 214071

#### Point mort Manip +  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `4ET Neutral Deadband Joystick [%]`
- Lit : `4ET Neutral Deadband Joystick`
- Utilisé par : `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`
- Ligne export : 75921 · id 214079

#### DMAC EV Pompe 2 Gauche  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `courbe(Left Joystick mc: {{-95; -100}; {Point mort Manip - [%]; 0}; {Point mort Manip + [%]; 0}; {95; 100}}, Freeze)`
- Lit : `Left Joystick mc`, `Point mort Manip +`, `Point mort Manip -`
- Utilisé par : `Math Gauche Left 45`
- Ligne export : 75963 · id 214087

#### Math Gauche Left 45  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `DMAC EV Pompe 2 Gauche [%]`
- Lit : `DMAC EV Pompe 2 Gauche`
- Utilisé par : `4ET Joystick Zero`, `DMAC_EV_2_Left`, `DMAC_EV_2_Left`, `T Joystick not zero`, `T Max Manip`
- Ligne export : 76027 · id 214097

#### DMAC EV Pompe 1 Droite  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `courbe(Right Joystick mc: {{-95; -100}; {Point mort Manip - [%]; 0}; {Point mort Manip + [%]; 0}; {95; 100}}, Freeze)`
- Lit : `Point mort Manip +`, `Point mort Manip -`, `Right Joystick mc`
- Utilisé par : `Math Droit Right 45`
- Ligne export : 76069 · id 214106

#### Math Droit Right 45  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `DMAC EV Pompe 1 Droite [%]`
- Lit : `DMAC EV Pompe 1 Droite`
- Utilisé par : `4ET Joystick Zero`, `DMAC_EV_1_Right`, `DMAC_EV_1_Right`, `T Joystick not zero`, `T Max Manip`
- Ligne export : 76133 · id 214116

#### 4ET Joystick Zero  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Math Droit Right 45 [%] = 0) AND (Math Gauche Left 45 [%] = 0)`
- Lit : `Math Droit Right 45`, `Math Gauche Left 45`
- Utilisé par : `MDs - Start Button Blocking Neutral E mc`, `Stop To Move`, `T Joystick is not in neutral position`, `T MD3 start last checks`, `e Joystick to zero CMSG mc`
- Ligne export : 76175 · id 214124

#### Stop To Move  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `4ET Joystick Zero`
- Lit : `4ET Joystick Zero`
- Utilisé par : `Auto PAUSE/OFF 4ET`
- Ligne export : 76229 · id 214133

#### Auto PAUSE/OFF 4ET  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=4ET Automatic Joystick Inhibition [s]
- Logique :
  - **Decreasing** = `Stop To Move`
  - **Resetting** = `(PositiveFlank(Stop To Move)) OR (Inter UP) OR (Inter DOWN) OR (Is_Thermic mc)`
- Lit : `4ET Automatic Joystick Inhibition`, `Inter DOWN`, `Inter UP`, `Is_Thermic mc`, `Stop To Move`
- Utilisé par : `4ET Start Button`, `ALL ASK STOP`, `Auto Off - Timer 4ET`, `Start Button 4ET bit`
- Ligne export : 76272 · id 214141

#### DEBUG Start soft 4ET  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `4ET Start Button`
- Ligne export : 76353 · id 214154

#### 4ET Start Button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(4ET Start Button) OR (PositiveFlank(B9 Start Button 4ET START Sel)) OR (PositiveFlank(DEBUG Start soft 4ET))`
  - **Blocking** = `(NegativeFlank(B9 Start Button 4ET START Sel)) OR (PositiveFlank((Auto PAUSE/OFF 4ET [s] <= 0))) OR (NegativeFlank(DEBUG Start soft 4ET))`
- Lit : `Auto PAUSE/OFF 4ET`, `B9 Start Button 4ET START Sel`, `DEBUG Start soft 4ET`
- Utilisé par : `Screen_Start/Stop mc`, `Stop Engine Flank`
- Ligne export : 76366 · id 214155

#### Stop Engine Flank  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank(4ET Start Button)`
- Lit : `4ET Start Button`
- Utilisé par : *(personne)*
- Ligne export : 76458 · id 214169

#### Engines READY 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Batt or engine started mc`
- Lit : `Batt or engine started mc`
- Utilisé par : `45 Speed state`, `4ET Engine hours`, `E&T Engines ready`, `IMS Hours Elec`, `Ok to move 45`, `Reset safety to on 45`, `Show standby jauge`, `T Engine State 45`, `Timer hiding first 10 hours check message`, `Timer hiding second 10 hours check message`, `safety orange`, `show discharge jauge`
- Ligne export : 76502 · id 214177

#### 4ET Enable Tracks with Arms Up?  `DP`
- Propriétés : True text=ACTIVE · False text=NO ACTIVE · Default mode={False}
- Utilisé par : `4ET Re-Track mode in water`
- Ligne export : 76545 · id 214185

#### Reset on startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset on startup`
- Utilisé par : `4ET Re-Track mode in water`
- Ligne export : 76558 · id 214186

#### 4ET Re-Track mode in water  `MEM`
- Propriétés : Input channel=4ET Enable Tracks with Arms Up? · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Resetting** = `Reset on startup`
- Lit : `4ET Enable Tracks with Arms Up?`, `Reset on startup`
- Utilisé par : `Ok to move 45`, `Single adjust item: Re-Track mode in water`
- Ligne export : 76608 · id 214195

#### Ok to move 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Engines READY 45) AND (TRACK DOWN 4ET or 4ET Re-Track mode in water)`
- Lit : `4ET Re-Track mode in water`, `Engines READY 45`, `TRACK DOWN 4ET`
- Utilisé par : `45 Speed state`, `Ko to move`
- Ligne export : 76652 · id 214203

#### 45 Speed state  `FSM`
- Propriétés : Store value=No · Resetting channel=Reset Speed
- État 0 **Parking**
  - transition *Push Slow Or Start* (état cible non exporté par IQANdesign)
    - **Activating** = `(PositiveFlank(IDC Speed S)) OR (PositiveFlank(Engines READY 45)) OR (Ok to move 45)`
  - transition *Push Fast* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed Fast)`
- État 1 **Slow**
  - transition *Stay Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC speed super slow)`
  - transition *Push Fast* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed Fast)`
- État 2 **Super Slow**
  - transition *Push Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed S)`
  - transition *Push Road* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed Fast)`
- État 3 **Fast**
  - transition *Push Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed S)`
  - transition *push fast to super slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC speed super slow)`
- Lit : `Engines READY 45`, `IDC Speed Fast`, `IDC Speed S`, `IDC speed super slow`, `Ok to move 45`, `Reset Speed`
- Utilisé par : `BUTTON DRIVE 4ET`, `BUTTON DRIVE Slow 4ET`, `BUTTON DRIVE Super Slow 4ET`, `Screen_Speed Input mc`, `Voyant  slow`, `voyant fast`, `voyant normal`
- Ligne export : 76718 · id 214214

#### Auto Fast after Down IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3100
- Logique :
  - **Activating** = `(PositiveFlank(TRACK DOWN 4ET)) AND (4ET Auto Fast After Down)`
- Lit : `4ET Auto Fast After Down`, `TRACK DOWN 4ET`
- Utilisé par : `Auto Fast after Down IDC delayed`
- Ligne export : 76999 · id 214264

#### Auto Fast after Down IDC delayed  `IDC`
> bof astuce timing posflank pb
- Propriétés : Toggle=No · Delay on=3000 · Delay off=0
- Logique :
  - **Activating** = `Auto Fast after Down IDC`
- Lit : `Auto Fast after Down IDC`
- Utilisé par : `IDC Speed Fast`
- Ligne export : 77050 · id 214273

#### IDC Speed Fast  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B5 F3 Speed Fast FAST Sel) OR (Auto Fast after Down IDC delayed)`
- Lit : `Auto Fast after Down IDC delayed`, `B5 F3 Speed Fast FAST Sel`
- Utilisé par : `45 Speed state`, `IDC Speed Fast Wait`
- Ligne export : 77093 · id 214281

#### IDC Speed S  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B4 F2 Speed Slow SLOW Sel`
- Lit : `B4 F2 Speed Slow SLOW Sel`
- Utilisé par : `45 Speed state`, `IDC Speed S Wait`
- Ligne export : 77143 · id 214290

#### IDC Speed S Wait  `IDC`
> tempo to switch to super slow
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `IDC Speed S`
- Lit : `IDC Speed S`
- Utilisé par : *(personne)*
- Ligne export : 77186 · id 214298

#### IDC Speed Fast Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1500 · Delay off=0
- Logique :
  - **Activating** = `IDC Speed Fast`
- Lit : `IDC Speed Fast`
- Utilisé par : *(personne)*
- Ligne export : 77229 · id 214306

#### Ko to move  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Ok to move 45)`
- Lit : `Ok to move 45`
- Utilisé par : `Reset Speed`
- Ligne export : 77272 · id 214315

#### Reset Speed  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Ko to move`
- Lit : `Ko to move`
- Utilisé par : `45 Speed state`
- Ligne export : 77316 · id 214323

#### 4ET Auto Fast After Down  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Auto Fast after Down IDC`, `Single adjust item: Auto Fast After Down`
- Ligne export : 77359 · id 214331

#### Force Safety off up/down 45  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Safety_disable 45 sel`, `Adjust group: Master Features`, `Single adjust item: Force Safety off up/down 45`
- Ligne export : 77372 · id 214332

#### Safety_disable 45  `IDC`
- Propriétés : Toggle=No · Delay on=1500 · Delay off=0
- Logique :
  - **Activating** = `B10 Safety off button 45 SAFETY OFF Sel   [Latching Or]`
  - **Blocking** = `Reset safety to on 45`
- Lit : `B10 Safety off button 45 SAFETY OFF Sel`, `Reset safety to on 45`
- Utilisé par : `Reset safety to on 45`, `Safety_disable 45 sel`
- Ligne export : 77385 · id 214350

#### 4ET Engine hours  `TMR`
- Propriétés : Type (Unit)=Hours [h] · Store value=Yes · Reset value=10
- Logique :
  - **Decreasing** = `Engines READY 45`
  - **Resetting** = `4ET Engine hours [h] <= 0`
- Lit : `Engines READY 45`
- Utilisé par : *(personne)*
- Ligne export : 83458 · id 215457

#### T Engine State 45  `SMC`
- Propriétés : Default state name=OFF
- Fonction *Started* :
  - **Activating** = `Engines READY 45`
  - **Blocking** = `not(Engines READY 45)`
- Lit : `Engines READY 45`
- Utilisé par : `T Engine Button OutPut`
- Ligne export : 83519 · id 215476

#### T Engine Button OutPut  `TP`
- Propriétés : Mode selector=T Engine State 45 · Default mode: OFF={START} · Mode 1: Started={STOP}
- Lit : `T Engine State 45`
- Utilisé par : *(personne)*
- Ligne export : 83567 · id 215485

#### safety orange  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Engines READY 45) AND (Safety_disable 45 sel)`
- Lit : `Engines READY 45`, `Safety_disable 45 sel`
- Utilisé par : `not safety orange`, `MD4-10 page: MAIN`, `MD4-5 page: BASE`
- Ligne export : 83580 · id 215489

#### not safety orange  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(safety orange)`
- Lit : `safety orange`
- Utilisé par : `MD4-10 page: MAIN`, `MD4-5 page: BASE`
- Ligne export : 83630 · id 215498

#### Screen_Speed Input mc  `IMAC`
- Logique :
  - **Controlling** = `45 Speed state`
- Lit : `45 Speed state`
- Utilisé par : `E Speed Int`, `T SPEED Engine`, `T Speed Int`
- Ligne export : 84613 · id 187210

#### IMS Hours Elec  `TMR`
- Propriétés : Type (Unit)=Hours [h] · Store value=Yes · Reset value=0
- Logique :
  - **Increasing** = `Engines READY 45`
- Lit : `Engines READY 45`
- Utilisé par : `Elec/10 hours true entre 10 et 16h`, `Elec/md4 10 hours check-up 45`, `Elec/md4 10 hours check-up 45`, `IMS hours Elec RESET`, `Maintenance`, `first! 1yr maintenance`, `Event log: Inspections`, `MD4-10 page: MAINTENANCE`, `MD4-5 page: MAINTENANCE`
- Ligne export : 84654 · id 236675

#### Lampe sur bouton maintenance main page  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(affichage button 1yr maintenance) OR (2yrs Maintenance) OR (4yrs Maintenance) OR (Elec/10 hours true entre 10 et 16h) OR (Therm/10 hours true entre 10 et 16h)`
- Lit : `2yrs Maintenance`, `4yrs Maintenance`, `Elec/10 hours true entre 10 et 16h`, `Therm/10 hours true entre 10 et 16h`, `affichage button 1yr maintenance`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 89705 · id 238850

#### IDC speed super slow  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B18 F5 speed super slow Sel`
- Lit : `B18 F5 speed super slow Sel`
- Utilisé par : `45 Speed state`
- Ligne export : 89852 · id 240529

#### Voyant  slow  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(45 Speed state = 2) AND (BUTTON DRIVE 4ET)`
- Lit : `45 Speed state`, `BUTTON DRIVE 4ET`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 89895 · id 240546

#### voyant normal  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(45 Speed state = 1) AND (BUTTON DRIVE 4ET)`
- Lit : `45 Speed state`, `BUTTON DRIVE 4ET`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 89947 · id 240550

#### voyant fast  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(45 Speed state = 3) AND (BUTTON DRIVE 4ET)`
- Lit : `45 Speed state`, `BUTTON DRIVE 4ET`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 89999 · id 240561

#### enabled ON/OFF T&E  `IDC`
> prend en compte les condition de enable du bouton on/off. pour le therm le bouton est toujours enable mais pour les elec la batterie doit être opérationelle (pas d'erreur)
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Is_Thermic mc) OR (batt ok to start)`
- Lit : `Is_Thermic mc`, `batt ok to start`
- Utilisé par : `enabled ON/OFF T&E`
- Ligne export : 90051 · id 240661

#### E&T Engines ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Engines READY 45) OR (T Engine_Started mc)`
- Lit : `Engines READY 45`, `T Engine_Started mc`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 90101 · id 240911

#### E&T OK BLOC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T OK BLOC) OR (OK BLOC)`
- Lit : `OK BLOC`, `T OK BLOC`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 90151 · id 241031

#### E&T Show symbole track white  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(T show symbole track bleu) OR (E show symbole track bleu)`
- Lit : `E show symbole track bleu`, `T show symbole track bleu`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 90201 · id 241055

## logic screen md4 / 45.UP/DOWN

#### Engines started 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Batt or engine started mc`
- Lit : `Batt or engine started mc`
- Utilisé par : `DOWN Counter`, `Inter DOWN`, `Inter DOWN Delay`, `Inter UP`, `Inter UP Delay`, `UP Counter`
- Ligne export : 77453 · id 214428

#### 4ET UP/DOWN Mode  `DP`
- Propriétés : True text=Auto · False text=Manual · Default mode={False}
- Utilisé par : `DOWN Counter`, `Inter DOWN Super Delay 4ET`, `Inter UP Super Delay 4ET`, `UP Counter`, `Single adjust item: UP/DOWN Mode`
- Ligne export : 77496 · id 214436

#### Inter UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(B1 Virtual UP 4ETUP sel and Engines started 2) OR (UP Counter)`
  - **Blocking** = `B2 Virtual DOWN 4ETDOWN sel`
- Lit : `B1 Virtual UP 4ETUP sel`, `B2 Virtual DOWN 4ETDOWN sel`, `Engines started 2`, `UP Counter`
- Utilisé par : `Inter UP Super Delay 4ET`, `Timer UP/DOWN`, `UP/DOWN Choice`
- Ligne export : 77509 · id 214455

#### Inter UP Super Delay 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Inter UP Delay`
  - **Blocking** = `not(4ET UP/DOWN Mode)`
- Lit : `4ET UP/DOWN Mode`, `Inter UP Delay`
- Utilisé par : `Auto UP`, `UP Counter`
- Ligne export : 77582 · id 214467

#### TRACK UP 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `4ET Store TIMER UP/DOWN [ms] >= internal timer UP/DOWN`
- Lit : `4ET Store TIMER UP/DOWN`, `internal timer UP/DOWN`
- Utilisé par : `IDC Auto Sleep`, `Intermediaire`, `TRACK UP 4ET`, `Track UP Delay`
- Ligne export : 77633 · id 214493

#### Track UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `TRACK UP 4ET`
- Lit : `TRACK UP 4ET`
- Utilisé par : `UP Counter`
- Ligne export : 77678 · id 214501

#### UP Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(Inter UP Super Delay 4ET)`
  - **Resetting** = `(UP Counter >= 2) OR (PositiveFlank(B2 Virtual DOWN 4ETDOWN sel)) OR (Track UP Delay) OR ((PositiveFlank(B1 Virtual UP 4ETUP sel)) and (UP Counter = 1)) OR (NegativeFlank(Engines started 2)) OR (not(4ET UP/DOWN Mode))`
- Lit : `4ET UP/DOWN Mode`, `B1 Virtual UP 4ETUP sel`, `B2 Virtual DOWN 4ETDOWN sel`, `Engines started 2`, `Inter UP Super Delay 4ET`, `Track UP Delay`
- Utilisé par : `Inter UP`, `Inter UP Delay`, `auto up/down 4ET`
- Ligne export : 77721 · id 214437

#### UP/DOWN Choice  `SMC`
- Propriétés : Default state name=IDLE
- Fonction *UP* :
  - **Activating** = `(Inter UP Delay) AND (4ET Store TIMER UP/DOWN [ms] < internal timer UP/DOWN) AND (OK UP/DOWN Sel)`
- Fonction *DOWN* :
  - **Activating** = `(Inter DOWN Delay) AND (4ET Store TIMER UP/DOWN [ms] > 0) AND (OK UP/DOWN Sel)`
- Lit : `4ET Store TIMER UP/DOWN`, `Inter DOWN Delay`, `Inter UP Delay`, `OK UP/DOWN Sel`, `internal timer UP/DOWN`
- Utilisé par : `4ET Value UP/DOWN`
- Ligne export : 77839 · id 214564

#### 4ET Value UP/DOWN  `IP`
- Propriétés : Unit=ms · Mode selector=UP/DOWN Choice · Default mode: IDLE={0} · Mode 1: UP={10} · Mode 2: DOWN={-12}
- Lit : `12`, `UP/DOWN Choice`
- Utilisé par : `4ET Store TIMER UP/DOWN`
- Ligne export : 77942 · id 214580

#### Inter DOWN Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(B2 Virtual DOWN 4ETDOWN sel and Engines started 2) OR (DOWN Counter)`
  - **Blocking** = `B1 Virtual UP 4ETUP sel`
- Lit : `B1 Virtual UP 4ETUP sel`, `B2 Virtual DOWN 4ETDOWN sel`, `DOWN Counter`, `Engines started 2`
- Utilisé par : `Inter DOWN Super Delay 4ET`, `Timer UP/DOWN`, `UP/DOWN Choice`
- Ligne export : 77958 · id 214509

#### Timer UP/DOWN  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `(Inter UP Delay) OR (Inter DOWN Delay)`
  - **Resetting** = `Timer UP/DOWN [ms] > 100`
- Lit : `Inter DOWN Delay`, `Inter UP Delay`
- Utilisé par : `4ET Store TIMER UP/DOWN`, `Adjust group: Master Config`
- Ligne export : 78031 · id 214581

#### 4ET Store TIMER UP/DOWN  `MEM`
- Propriétés : Input channel=4ET Value UP/DOWN [ms] · Action=Add · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `Timer UP/DOWN [ms] > 100`
  - **Resetting** = `0 > 4ET Store TIMER UP/DOWN [ms]`
- Lit : `4ET Value UP/DOWN`, `Timer UP/DOWN`
- Utilisé par : `State Up/Down 4ET`, `TRACK DOWN 4ET`, `TRACK UP 4ET`, `UP/DOWN Choice`
- Ligne export : 78099 · id 214476

#### internal timer UP/DOWN  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `100 * 4ET Timer UP/DOWN [s]`
- Lit : `4ET Timer UP/DOWN`
- Utilisé par : `State Up/Down 4ET`, `TRACK UP 4ET`, `UP/DOWN Choice`
- Ligne export : 78154 · id 214485

#### Inter DOWN Super Delay 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Inter DOWN Delay`
  - **Blocking** = `not(4ET UP/DOWN Mode)`
- Lit : `4ET UP/DOWN Mode`, `Inter DOWN Delay`
- Utilisé par : `DOWN Counter`, `DOWN Super`
- Ligne export : 78198 · id 214521

#### Track DOWN Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `TRACK DOWN 4ET`
- Lit : `TRACK DOWN 4ET`
- Utilisé par : `DOWN Counter`
- Ligne export : 78249 · id 214538

#### DOWN Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(Inter DOWN Super Delay 4ET)`
  - **Resetting** = `(DOWN Counter >= 2) OR (PositiveFlank(B1 Virtual UP 4ETUP sel)) OR (Track DOWN Delay) OR ((PositiveFlank(B2 Virtual DOWN 4ETDOWN sel)) and (DOWN Counter = 1)) OR (NegativeFlank(Engines started 2)) OR (not(4ET UP/DOWN Mode))`
- Lit : `4ET UP/DOWN Mode`, `B1 Virtual UP 4ETUP sel`, `B2 Virtual DOWN 4ETDOWN sel`, `Engines started 2`, `Inter DOWN Super Delay 4ET`, `Track DOWN Delay`
- Utilisé par : `Inter DOWN`, `Inter DOWN Delay`, `auto up/down 4ET`
- Ligne export : 78292 · id 214546

#### TRACK DOWN 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `4ET Store TIMER UP/DOWN [ms] <= 0`
- Lit : `4ET Store TIMER UP/DOWN`
- Utilisé par : `Auto Fast after Down IDC`, `Intermediaire`, `KTB K11 IDC True- SearchLight`, `OK Buz`, `Ok to move 45`, `TRACK DOWN 4ET APPOUT`, `TRACK DOWN 4ET [logic screen md4.45.UP/DOWN]`, `Track DOWN Delay`
- Ligne export : 78410 · id 214530

#### Inter DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B2 Virtual DOWN 4ETDOWN sel and Engines started 2) OR (DOWN Counter)`
  - **Blocking** = `B1 Virtual UP 4ETUP sel`
- Lit : `B1 Virtual UP 4ETUP sel`, `B2 Virtual DOWN 4ETDOWN sel`, `DOWN Counter`, `Engines started 2`
- Utilisé par : `Action Down`, `Auto PAUSE/OFF 4ET`, `Reset safety to on 45`, `UP/DOWN Button 4ET`
- Ligne export : 78455 · id 214594

#### Inter UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B1 Virtual UP 4ETUP sel and Engines started 2) OR (UP Counter)`
  - **Blocking** = `B2 Virtual DOWN 4ETDOWN sel`
- Lit : `B1 Virtual UP 4ETUP sel`, `B2 Virtual DOWN 4ETDOWN sel`, `Engines started 2`, `UP Counter`
- Utilisé par : `Action UP`, `Auto PAUSE/OFF 4ET`, `UP/DOWN Button 4ET`
- Ligne export : 78528 · id 214606

#### State Up/Down 4ET  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `(4ET Store TIMER UP/DOWN [ms] / internal timer UP/DOWN) * 100`
- Lit : `4ET Store TIMER UP/DOWN`, `internal timer UP/DOWN`
- Utilisé par : `Reset safety to on 45`, `Screen_State Up/Down mc`, `StateM Up/Down`
- Ligne export : 78601 · id 214618

#### UP/DOWN Button 4ET  `SMC`
- Propriétés : Default state name=IDLE
- Fonction *UP* :
  - **Activating** = `Inter UP`
- Fonction *DOWN* :
  - **Activating** = `Inter DOWN`
- Lit : `Inter DOWN`, `Inter UP`
- Utilisé par : `DOWN E`, `DOWN T`, `UP E`, `UP T`
- Ligne export : 78653 · id 214627

#### StateM Up/Down  `SMC`
- Propriétés : Default state name=Default state
- Fonction *0* :
  - **Activating** = `State Up/Down 4ET [%] < 25`
- Fonction *1* :
  - **Activating** = `(State Up/Down 4ET [%] >= 25) AND (State Up/Down 4ET [%] <= 75)`
- Fonction *2* :
  - **Activating** = `State Up/Down 4ET [%] > 75`
- Lit : `State Up/Down 4ET`
- Utilisé par : *(personne)*
- Ligne export : 78724 · id 214639

#### Intermediaire  `IDC`
- Propriétés : Toggle=No · Delay on=100 · Delay off=100
- Logique :
  - **Activating** = `True`
  - **Blocking** = `(TRACK UP 4ET) OR (TRACK DOWN 4ET)`
- Lit : `TRACK DOWN 4ET`, `TRACK UP 4ET`
- Utilisé par : `Action Down`, `Action UP`, `Timer Auto Sleep Engine`
- Ligne export : 78841 · id 214656

#### Action UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter UP) AND Intermediaire`
- Lit : `Inter UP`, `Intermediaire`
- Utilisé par : `Show P-1-2`
- Ligne export : 78898 · id 214666

#### Action Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter DOWN) AND Intermediaire`
- Lit : `Inter DOWN`, `Intermediaire`
- Utilisé par : `Show P-1-2`
- Ligne export : 78948 · id 214675

#### 4E Time Sleep engine  `FP`
- Propriétés : Unit=s · Mode selector=Drive Type mc · Default mode: Electric={20} · Mode 1: Fossil={55}
- Lit : `Drive Type mc`
- Utilisé par : `Process Down Engine`, `Timer Auto Sleep Engine`, `Timer sleep engine to Img`, `Adjust group: Master Features`, `Single adjust item: 4E Time Sleep engine`
- Ligne export : 78998 · id 214684

#### IDC Auto Sleep  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `PositiveFlank(TRACK UP 4ET)`
- Lit : `TRACK UP 4ET`
- Utilisé par : `Timer Auto Sleep Engine`
- Ligne export : 79012 · id 214685

#### Timer Auto Sleep Engine  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=4E Time Sleep engine [s]
- Logique :
  - **Decreasing** = `(IDC Auto Sleep) OR (Inside(Timer Auto Sleep Engine [s], 0, 4E Time Sleep engine [s]))`
  - **Resetting** = `Intermediaire OR (ALL ASK STOP)`
- Lit : `4E Time Sleep engine`, `ALL ASK STOP`, `IDC Auto Sleep`, `Intermediaire`
- Utilisé par : `ASK STOP 4ET`, `Process Down Engine`, `Timer sleep engine to Img`
- Ligne export : 79056 · id 214693

#### ASK STOP 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Timer Auto Sleep Engine [s] <= 0`
- Lit : `Timer Auto Sleep Engine`
- Utilisé par : `ALL ASK STOP`
- Ligne export : 79132 · id 214706

#### Process Down Engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inside(Timer Auto Sleep Engine [s], 0, 4E Time Sleep engine [s])`
- Lit : `4E Time Sleep engine`, `Timer Auto Sleep Engine`
- Utilisé par : `Mini Wait`, `Number UP&Down`, `Statistics log: System Stats`
- Ligne export : 79177 · id 214714

#### Mini Wait  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=50
- Logique :
  - **Activating** = `Process Down Engine`
- Lit : `Process Down Engine`
- Utilisé par : `Show P-1-2`
- Ligne export : 79223 · id 214722

#### Show P-1-2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True`
  - **Blocking** = `(Action UP) OR (Action Down) OR (Mini Wait)`
- Lit : `Action Down`, `Action UP`, `Mini Wait`
- Utilisé par : *(personne)*
- Ligne export : 79266 · id 214730

#### Timer sleep engine to Img  `IMAC`
- Logique :
  - **Controlling** = `((Timer Auto Sleep Engine [s] / 4E Time Sleep engine [s]) * 100) / 15`
- Lit : `4E Time Sleep engine`, `Timer Auto Sleep Engine`
- Utilisé par : `Timer sleep engine to Img`
- Ligne export : 79330 · id 214741

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
- Lit : `Timer sleep engine to Img`
- Utilisé par : *(personne)*
- Ligne export : 79391 · id 214751

#### auto up/down 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `(UP Counter = 1) OR (DOWN Counter = 1)`
- Lit : `DOWN Counter`, `UP Counter`
- Utilisé par : `T VIEW TRACK STATE`, `auto up/down 4ET output`, `brokenVIEW TRACK STATE`
- Ligne export : 79664 · id 214787

#### auto up/down 4ET output  `APPOUT`
- Propriétés : Input channel=auto up/down 4ET · Send method=On change · Transmit rate=1000
- Lit : `auto up/down 4ET`
- Utilisé par : *(personne)*
- Ligne export : 79718 · id 214796

#### Number UP&Down  `ECNT`
- Propriétés : Store value=Yes · Reset value=0
- Logique :
  - **Increasing** = `Process Down Engine`
- Lit : `Process Down Engine`
- Utilisé par : `Maintenance`, `Nbr UP&DOWN RESET`, `first! 1yr maintenance`, `Event log: Inspections`, `MD4-10 page: MAINTENANCE`, `MD4-5 page: MAINTENANCE`
- Ligne export : 79729 · id 236661

## logic screen md4 / 45.buzzer

#### UP  `FGI`
- Propriétés : Input type=Digital · Input=B1 Virtual UP 4ETUP sel · Default state name=Default state
- Lit : `B1 Virtual UP 4ETUP sel`
- Utilisé par : `E Engine OutPut Text`, `OK Buz up down`, `T Engine OutPut Text`, `Adjust group: Maintenance`, `Adjust group: Master Config`, `Adjust group: Setup`
- Ligne export : 79802 · id 214808

#### TRACK UP 4ET  `FGI`
- Propriétés : Input type=Digital · Input=TRACK UP 4ET · Default state name=Default state
- Lit : `TRACK UP 4ET`
- Utilisé par : `OK Buz up down`
- Ligne export : 79813 · id 214809

#### Auto UP  `FGI`
- Propriétés : Input type=Digital · Input=Inter UP Super Delay 4ET · Default state name=Default state
- Lit : `Inter UP Super Delay 4ET`
- Utilisé par : `OK Buz up down`
- Ligne export : 79824 · id 214810

#### OK Buz up down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=150
- Logique :
  - **Activating** = `PositiveFlank(UP) OR (PositiveFlank(TRACK UP 4ET)) OR (PositiveFlank(Auto UP))`
- Lit : `Auto UP`, `TRACK UP 4ET`, `UP`
- Utilisé par : `Inter Buzzer 45`, `Wait Buz up down`
- Ligne export : 79835 · id 214811

#### Wait Buz up down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `NegativeFlank(OK Buz up down)`
- Lit : `OK Buz up down`
- Utilisé par : `OK Buz 2nd up down`
- Ligne export : 79895 · id 214821

#### OK Buz 2nd up down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=150
- Logique :
  - **Activating** = `NegativeFlank(Wait Buz up down)`
- Lit : `Wait Buz up down`
- Utilisé par : `Inter Buzzer 45`
- Ligne export : 79939 · id 214829

#### OK Buz Oil  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `PositiveFlank(Wait_Very_Low_Oil_Level)`
- Lit : `Wait_Very_Low_Oil_Level`
- Utilisé par : `Inter Buzzer 45`
- Ligne export : 79983 · id 214837

#### Inter Buzzer 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(OK Buz up down) OR (OK Buz 2nd up down) OR (OK Buz Oil) OR (test buzzer 45) OR (OK Buz)`
- Lit : `OK Buz`, `OK Buz 2nd up down`, `OK Buz Oil`, `OK Buz up down`, `test buzzer 45`
- Utilisé par : `Inter Buzzer for 45 button`
- Ligne export : 80027 · id 214845

#### test buzzer 45  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Inter Buzzer 45`, `Single adjust item: Test buzzer MD4`
- Ligne export : 80105 · id 229138

#### DOWN  `FGI`
- Propriétés : Input type=Digital · Input=B2 Virtual DOWN 4ETDOWN sel · Default state name=Default state
- Lit : `B2 Virtual DOWN 4ETDOWN sel`
- Utilisé par : `OK Buz`, `Adjust group: Setup`
- Ligne export : 80118 · id 229153

#### TRACK DOWN 4ET [logic screen md4.45.UP/DOWN]  `FGI`
- Propriétés : Input type=Digital · Input=TRACK DOWN 4ET · Default state name=Default state
- Lit : `TRACK DOWN 4ET`
- Utilisé par : *(personne)*
- Ligne export : 80129 · id 229154

#### DOWN Super  `FGI`
- Propriétés : Input type=Digital · Input=Inter DOWN Super Delay 4ET · Default state name=Default state
- Lit : `Inter DOWN Super Delay 4ET`
- Utilisé par : `OK Buz`
- Ligne export : 80140 · id 229155

#### OK Buz  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `PositiveFlank(DOWN) OR (PositiveFlank(TRACK DOWN 4ET [logic screen md4.45.UP/DOWN])) OR (PositiveFlank(DOWN Super))`
- Lit : `DOWN`, `DOWN Super`, `TRACK DOWN 4ET`
- Utilisé par : `Inter Buzzer 45`
- Ligne export : 80151 · id 229156

## logic screen md4 / 45.screen state and pin

#### Fake SM Remote 4ET  `SMC`
- Propriétés : Default state name=NO
- Fonction *UP* :
  - **Activating** = `False`
- Fonction *DOWN* :
  - **Activating** = `False`
- Utilisé par : `Remote Ask Stop 4ET`, `Unlock Boat remote 4ET`
- Ligne export : 80227 · id 214890

#### Unlock Boat remote 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((Fake SM Remote 4ET > 0))) OR (Unlock Boat remote 4ET)`
- Lit : `Fake SM Remote 4ET`
- Utilisé par : `eBoat State 4E`
- Ligne export : 80298 · id 214870

#### eCharger Charging IDC  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `E.Charging State Machine = 2`
- Lit : `E.Charging State Machine`
- Utilisé par : `Auto Off - Timer 4ET`, `Charging State`, `Continue 4ET`, `eBoat State 4E`
- Ligne export : 80358 · id 214881

#### 4ET Time ask remote  `IP`
- Propriétés : Unit=ms · Default mode={5000}
- Utilisé par : `Remote Ask Stop 4ET`
- Ligne export : 80403 · id 214889

#### Remote Ask Stop 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=4ET Time ask remote [ms] · Delay off=0
- Logique :
  - **Activating** = `Fake SM Remote 4ET = 1`
- Lit : `4ET Time ask remote`, `Fake SM Remote 4ET`
- Utilisé par : `Off Button - IDC 4ET`
- Ligne export : 80415 · id 214902

#### Auto Off - Timer 4ET  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=4ET Auto Global switch Off [min]
- Logique :
  - **Decreasing** = `Auto PAUSE/OFF 4ET [s] < (4ET Automatic Joystick Inhibition [s] - 20)`
  - **Resetting** = `(B9 Start Button 4ET START Sel) OR (PositiveFlank((2 = Auto Off Message 4ET))) OR (eCharger Charging IDC) OR (Auto PAUSE/OFF 4ET [s] > (4ET Automatic Joystick Inhibition [s] - 20)) OR (Is_Thermic mc)`
- Lit : `4ET Auto Global switch Off`, `4ET Automatic Joystick Inhibition`, `Auto Off Message 4ET`, `Auto PAUSE/OFF 4ET`, `B9 Start Button 4ET START Sel`, `Is_Thermic mc`, `eCharger Charging IDC`
- Utilisé par : `Auto Off Message 4ET`, `Off Button - IDC 4ET`, `ShutDown Confirmed`
- Ligne export : 80460 · id 214910

#### Auto Off Message 4ET  `IMSG`
- Propriétés : Show message=All · Dialog type=Confirmation · Header=Automatic Shutdown · Text=I seems that you don't use the boat, press Continue to keep the boat ON. If not the boat will stop in 30 minutes. · Left button=Continue · Right button=OFF
- Logique :
  - **Showing** = `Auto Off - Timer 4ET [min] <= 20`
- Lit : `Auto Off - Timer 4ET`
- Utilisé par : `Auto Off - Timer 4ET`
- Ligne export : 80579 · id 214927

#### 4ET Auto Global switch Off  `IP`
- Propriétés : Unit=min · Default mode={120}
- Utilisé par : `Auto Off - Timer 4ET`, `Single adjust item: Auto Global switch Off`
- Ligne export : 80629 · id 214935

#### Off Button - IDC 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=100 · Delay off=0
- Logique :
  - **Activating** = `(B6 OFF Button 4ET OFF Sel) OR (Auto Off - Timer 4ET [min] <= 0) OR (Remote Ask Stop 4ET)`
- Lit : `Auto Off - Timer 4ET`, `B6 OFF Button 4ET OFF Sel`, `Remote Ask Stop 4ET`
- Utilisé par : `Continue 4ET`, `Power Down State 4ET`
- Ligne export : 80641 · id 214936

#### Continue 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Continue 4ET) OR (B7 Continue Button 4ET CONTINUE Sel)`
  - **Blocking** = `(PositiveFlank(Off Button - IDC 4ET)) OR (NegativeFlank(eCharger Charging IDC))`
- Lit : `B7 Continue Button 4ET CONTINUE Sel`, `Off Button - IDC 4ET`, `eCharger Charging IDC`
- Utilisé par : `Charging State`, `eBoat State 4E`
- Ligne export : 80700 · id 214946

#### Power Down State 4ET  `FSM`
- Propriétés : Store value=No · Resetting channel=B3 Cancel Button 4ET CANCEL Sel
- État 0 **Power On**
  - transition *Ask Stop* (état cible non exporté par IQANdesign)
    - **Activating** = `(Off Button - IDC 4ET) OR ((Charger End Charge and 4ET Auto Off After Charge?) and Is_Electric mc)`
- État 1 **Power Down**
  - transition *Time to Down* (état cible non exporté par IQANdesign)
    - **Activating** = `Power Down Timer ET`
- État 2 **Stop**
- Lit : `4ET Auto Off After Charge?`, `B3 Cancel Button 4ET CANCEL Sel`, `Charger End Charge`, `Is_Electric mc`, `Off Button - IDC 4ET`, `Power Down Timer ET`
- Utilisé par : `Auto Off Cmd`, `Power Down`, `Power Down Timer Ask 4ET`
- Ligne export : 80766 · id 215274

#### Power Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Power Down State 4ET = 1`
- Lit : `Power Down State 4ET`
- Utilisé par : `Auto Off Lamps`, `eBoat State 4E`
- Ligne export : 80868 · id 215364

#### eBoat State 4E  `FSM`
- Propriétés : Store value=No
- État 0 **Startup**
  - transition *Unlock* (état cible non exporté par IQANdesign)
    - **Activating** = `(Unlock Boat remote 4ET) OR (Good PIN 4ET)`
  - transition *Shutdown* (état cible non exporté par IQANdesign)
    - **Activating** = `Power Down`
- État 1 **Run**
  - transition *Shutdown* (état cible non exporté par IQANdesign)
    - **Activating** = `Power Down`
  - transition *Charging* (état cible non exporté par IQANdesign)
    - **Activating** = `eCharger Charging IDC and (not(Continue 4ET))`
- État 2 **ShutDown**
  - transition *Cancel Sh* (état cible non exporté par IQANdesign)
    - **Activating** = `B3 Cancel Button 4ET CANCEL Sel`
  - transition *Cancel* (état cible non exporté par IQANdesign)
    - **Activating** = `B3 Cancel Button 4ET CANCEL Sel`
- État 3 **Charging**
  - transition *Shutdown* (état cible non exporté par IQANdesign)
    - **Activating** = `Power Down`
  - transition *Continue* (état cible non exporté par IQANdesign)
    - **Activating** = `Continue 4ET`
- Lit : `B3 Cancel Button 4ET CANCEL Sel`, `Continue 4ET`, `Good PIN 4ET`, `Power Down`, `Unlock Boat remote 4ET`, `eCharger Charging IDC`
- Utilisé par : `Main page IDC`, `ShutDown page IDC`, `Startup page IDC`, `eScreen Charging`
- Ligne export : 80913 · id 214957

#### Main page IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `1 = eBoat State 4E`
- Lit : `eBoat State 4E`
- Utilisé par : `Main page IDC E`, `Main page IDC T`
- Ligne export : 81195 · id 215014

#### eScreen NOT Charging  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(eScreen Charging)`
- Lit : `eScreen Charging`
- Utilisé par : `MD4-10 page: SHUTDOWN`, `MD4-5 page: SHUTDOWN`
- Ligne export : 82250 · id 215266

#### Power Down Timer Ask 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Power Down State 4ET = 1`
- Lit : `Power Down State 4ET`
- Utilisé par : `BarTimer`, `Power Down Timer ET`
- Ligne export : 82294 · id 215292

#### 4ET Time ask Power Down  `IP`
- Propriétés : Unit=ms · Default mode={3000}
- Utilisé par : `Power Down Timer ET`, `ShutDownBar`
- Ligne export : 82339 · id 215300

#### Power Down Timer ET  `IDC`
- Propriétés : Toggle=No · Delay on=4ET Time ask Power Down [ms] · Delay off=0
- Logique :
  - **Activating** = `Power Down Timer Ask 4ET`
- Lit : `4ET Time ask Power Down`, `Power Down Timer Ask 4ET`
- Utilisé par : `Power Down State 4ET`
- Ligne export : 82351 · id 215301

#### Charger End Charge  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `PositiveFlank((3 = E.Charging State Machine))`
- Lit : `E.Charging State Machine`
- Utilisé par : `Power Down State 4ET`
- Ligne export : 82394 · id 215309

#### 4ET Auto Off After Charge?  `DP`
> If False: Boat will remain on after charge
- Propriétés : True text=Yes · False text=No · Default mode={True}
- Utilisé par : `Power Down State 4ET`
- Ligne export : 82447 · id 215318

#### Start Button 4ET bit  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Start Button 4ET bit) OR (PositiveFlank(B9 Start Button 4ET START Sel))`
  - **Blocking** = `(NegativeFlank(B9 Start Button 4ET START Sel)) OR (PositiveFlank((Auto PAUSE/OFF 4ET [s] <= 0)))`
- Lit : `Auto PAUSE/OFF 4ET`, `B9 Start Button 4ET START Sel`
- Utilisé par : `Stop Engine Flank 4ET`
- Ligne export : 82460 · id 215319

#### Stop Engine Flank 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank(Start Button 4ET bit)`
- Lit : `Start Button 4ET bit`
- Utilisé par : *(personne)*
- Ligne export : 82536 · id 215331

#### Charging State  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `eCharger Charging IDC`
  - **Blocking** = `Continue 4ET`
- Lit : `Continue 4ET`, `eCharger Charging IDC`
- Utilisé par : `Charger Charging Wait 2 minutes`
- Ligne export : 82580 · id 215339

#### Charger Charging Wait 2 minutes  `IDC`
- Propriétés : Toggle=No · Delay on=120000 · Delay off=0
- Logique :
  - **Activating** = `Charging State`
- Lit : `Charging State`
- Utilisé par : `Auto Off Lamps`
- Ligne export : 82630 · id 215348

#### Auto Off Cmd  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `Power Down State 4ET = 2`
- Lit : `Power Down State 4ET`
- Utilisé par : `KBB K10 IDC - AUTO OFF POWER BOX`
- Ligne export : 82673 · id 215356

#### Charger Connected  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `1 = E.Charging State Machine`
- Lit : `E.Charging State Machine`
- Utilisé par : *(personne)*
- Ligne export : 82718 · id 215372

#### BarTimer  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Power Down Timer Ask 4ET`
  - **Resetting** = `NegativeFlank(Power Down Timer Ask 4ET)`
- Lit : `Power Down Timer Ask 4ET`
- Utilisé par : `ShutDownBar`
- Ligne export : 82763 · id 215380

#### ShutDownBar  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(BarTimer [ms]: 0->0, 4ET Time ask Power Down [ms]->100, Freeze)`
- Lit : `4ET Time ask Power Down`, `BarTimer`
- Utilisé par : `MD4-10 page: SHUTDOWN`, `MD4-5 page: SHUTDOWN`
- Ligne export : 82823 · id 215391

#### Main page on  `IDC`
> main active page 1, bit 0
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(B13 Info page on 45 Sel)`
- Lit : `B13 Info page on 45 Sel`
- Utilisé par : `MD4-5 page: BASE Info`
- Ligne export : 82870 · id 215401

#### Info page on  `IDC`
> info active page 2, info bit 1
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B13 Info page on 45 Sel`
- Lit : `B13 Info page on 45 Sel`
- Utilisé par : `Info page on E`, `Info page on T`
- Ligne export : 82914 · id 215410

#### 4et.Is_Electric  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Drive Type mc = 0`
- Lit : `Drive Type mc`
- Utilisé par : `Info page on E`, `Main page IDC E`
- Ligne export : 82957 · id 214381

#### 4et.Is_Thermic  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Drive Type mc = 1`
- Lit : `Drive Type mc`
- Utilisé par : `Info page on T`, `Main page IDC T`
- Ligne export : 83002 · id 214373

#### Info page on T  `IDC`
> info active page 2
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `4et.Is_Thermic AND (Info page on)`
- Lit : `4et.Is_Thermic`, `Info page on`
- Utilisé par : *(personne)*
- Ligne export : 83047 · id 215436

#### Info page on E  `IDC`
> info active page 2
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `4et.Is_Electric AND (Info page on)`
- Lit : `4et.Is_Electric`, `Info page on`
- Utilisé par : *(personne)*
- Ligne export : 83097 · id 215445

#### BUTTON DRIVE 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `MDs - Start Button Blocking Neutral E mc and (State All Speed Int > 1)`
  - **Blocking** = `(45 Speed state = 0) OR ((E.Power Management System <> 2) and Is_Electric mc)`
- Lit : `45 Speed state`, `E.Power Management System`, `Is_Electric mc`, `MDs - Start Button Blocking Neutral E mc`, `State All Speed Int`
- Utilisé par : `BUTTON DRIVE 4ET 45/10`, `BUTTON DRIVE Slow 4ET`, `BUTTON DRIVE Super Slow 4ET`, `Voyant  slow`, `voyant fast`, `voyant normal`
- Ligne export : 83147 · id 214391

#### BUTTON DRIVE Super Slow 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(BUTTON DRIVE 4ET) AND (45 Speed state = 1)`
  - **Blocking** = `(45 Speed state = 0) OR (45 Speed state = 2)`
- Lit : `45 Speed state`, `BUTTON DRIVE 4ET`
- Utilisé par : *(personne)*
- Ligne export : 83242 · id 214402

#### BUTTON DRIVE Slow 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(BUTTON DRIVE 4ET) AND ((45 Speed state = 2) or (45 Speed state = 3))`
  - **Blocking** = `(45 Speed state = 0) OR (45 Speed state = 1)`
- Lit : `45 Speed state`, `BUTTON DRIVE 4ET`
- Utilisé par : *(personne)*
- Ligne export : 83312 · id 214413

#### eScreen Charging  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `3 = eBoat State 4E`
- Lit : `eBoat State 4E`
- Utilisé par : `eScreen NOT Charging`, `MD4-10 page: SHUTDOWN`, `MD4-10 page: STARTUP PIN`, `MD4-5 page: SHUTDOWN`, `MD4-5 page: brokenSTARTUP PIN`
- Ligne export : 83412 · id 215258

## logic screen md4 / 45.screen state and pin / broken PIN Pad 4ET

#### 4ET PIN CODE  `IP`
- Propriétés : Default mode={1000}
- Utilisé par : `Good PIN 4ET`
- Ligne export : 81255 · id 215042

#### PIN State  `SMC`
- Propriétés : Default state name=NO
- Fonction *1* : (vide)
- Fonction *2* : (vide)
- Fonction *3* : (vide)
- Fonction *4* : (vide)
- Fonction *5* : (vide)
- Fonction *6* : (vide)
- Fonction *7* : (vide)
- Fonction *8* : (vide)
- Fonction *9* : (vide)
- Fonction *0* : (vide)
- Utilisé par : `PIN Value`, `PIN counter`
- Ligne export : 81267 · id 215043

#### PIN Value  `IMAC`
- Propriétés : Function selector=PIN State
- Fonction *NO* :
  - **Controlling** = `0`
- Fonction *1* :
  - **Controlling** = `1`
- Fonction *2* :
  - **Controlling** = `2`
- Fonction *3* :
  - **Controlling** = `3`
- Fonction *4* :
  - **Controlling** = `4`
- Fonction *5* :
  - **Controlling** = `5`
- Fonction *6* :
  - **Controlling** = `6`
- Fonction *7* :
  - **Controlling** = `7`
- Fonction *8* :
  - **Controlling** = `8`
- Fonction *9* :
  - **Controlling** = `9`
- Fonction *0* :
  - **Controlling** = `0`
- Lit : `PIN State`
- Utilisé par : `Number 1`, `Number 2`, `Number 3`, `Number 4`
- Ligne export : 81516 · id 215087

#### PIN counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank((PIN State > 0))`
  - **Resetting** = `PIN counter > 3`
- Lit : `PIN State`
- Utilisé par : `Number 1`, `Number 2`, `Number 3`, `Number 4`, `PIN Pad Show 45`
- Ligne export : 81867 · id 215165

#### Number 1  `MEM`
- Propriétés : Input channel=PIN Value · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `1 = PIN counter`
- Lit : `PIN Value`, `PIN counter`
- Utilisé par : `Good PIN 4ET`
- Ligne export : 81937 · id 215177

#### Number 2  `MEM`
- Propriétés : Input channel=PIN Value · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `2 = PIN counter`
- Lit : `PIN Value`, `PIN counter`
- Utilisé par : `Good PIN 4ET`
- Ligne export : 81983 · id 215185

#### Number 3  `MEM`
- Propriétés : Input channel=PIN Value · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `3 = PIN counter`
- Lit : `PIN Value`, `PIN counter`
- Utilisé par : `Good PIN 4ET`
- Ligne export : 82029 · id 215193

#### Number 4  `MEM`
- Propriétés : Input channel=PIN Value · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `0 = PIN counter`
- Lit : `PIN Value`, `PIN counter`
- Utilisé par : `Good PIN 4ET`
- Ligne export : 82075 · id 215201

#### Good PIN 4ET  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  if 4ET PIN CODE  = 1000 then
  Result := True
  else
  Result := (1000*Number 1 + 100*Number 2 + 10*Number 3 + 1*Number 4) = 4ET PIN CODE
  endif
  ```
- Lit : `4ET PIN CODE`, `Number 1`, `Number 2`, `Number 3`, `Number 4`
- Utilisé par : `eBoat State 4E`
- Ligne export : 82121 · id 215209

#### PIN Pad Show 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PIN Pad Show 45`
  - **Blocking** = `PositiveFlank((0 = PIN counter))`
- Lit : `PIN counter`
- Utilisé par : `PIN Show 45`
- Ligne export : 82145 · id 215231

#### PIN Show 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(PIN Pad Show 45)`
- Lit : `PIN Pad Show 45`
- Utilisé par : `MD4-5 page: brokenSTARTUP PIN`
- Ligne export : 82205 · id 215242

## logic screen md4 / WIP/45.10 hours check
> message pour confirmer à l'utilisateur l'enregistrement du check dans les log

#### Elec/10 hours true entre 10 et 16h  `IDC`
> IDC pour l'activation ou non des messages entre 10 et 16h (mod 10) et si la 10 hours check list n'est pas faite
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `((IMS Hours Elec [h] mod 10) >= 0) AND ((IMS Hours Elec [h] mod 10) < 5) AND (IMS Hours Elec [h] >= 10) AND (Is_Electric mc) AND (Timer hiding first 10 hours check message [h] <= 0) AND (Timer hiding second 10 hours check message [h] <= 0)`
- Lit : `IMS Hours Elec`, `Is_Electric mc`, `Timer hiding first 10 hours check message`, `Timer hiding second 10 hours check message`
- Utilisé par : `10 hours true`, `Lampe sur bouton maintenance main page`
- Ligne export : 84723 · id 237471

#### r u sure 10 hours check  `IMSG`
> message de confirmation de certification de la 10 hours
- Propriétés : Show message=All · Dialog type=Confirmation · Header=RESET Maintenance? · Left button=No · Right button=Yes
- Logique :
  - **Showing** = `B14 10 hours`
  - **Hiding** = `(r u sure 10 hours wait) OR (r u sure 10 hours check = 5) OR (r u sure 10 hours check = 2)`
- Lit : `B14 10 hours`, `RESET Maintenance`, `r u sure 10 hours wait`
- Utilisé par : `Timer hiding first 10 hours check message`, `Timer hiding second 10 hours check message`, `r u sure 10 hours wait`, `Event log: Inspections`
- Ligne export : 84820 · id 237511

#### r u sure 10 hours wait  `IDC`
> IDC pour cacher le message "are you sure" en cas de réponse "yes" et pour afficher le message de confirmation d'enregistrement du check
- Propriétés : Toggle=No · Delay on=500 · Delay off=5000
- Logique :
  - **Activating** = `r u sure 10 hours check = 4`
- Lit : `r u sure 10 hours check`
- Utilisé par : `r u sure 10 hours check`, `recording 10 hours check`
- Ligne export : 84893 · id 237531

#### Timer hiding first 10 hours check message  `TMR`
> Timer (h) pour enlever le 1er message entre 10 et 12h si la check list est certifiée faite
- Propriétés : Type (Unit)=Hours [h] · Store value=Yes · Reset value=3
- Logique :
  - **Decreasing** = `(Engines READY 45) OR (T Engine_Started mc)`
  - **Resetting** = `(r u sure 10 hours check = 4) AND (not((r u sure 10 hours check = 1)))`
- Lit : `Engines READY 45`, `T Engine_Started mc`, `r u sure 10 hours check`
- Utilisé par : `Elec/10 hours true entre 10 et 16h`, `Elec/md4 10 hours check-up 45`, `Therm/10 hours true entre 10 et 16h`, `Therm/md4 10 hours check-up 45`
- Ligne export : 84938 · id 237485

#### Timer hiding second 10 hours check message  `TMR`
> Timer (h) pour enlever le 2eme message entre 12 et 16h si la check list est certifiée faite
- Propriétés : Type (Unit)=Hours [h] · Store value=Yes · Reset value=5,2
- Logique :
  - **Decreasing** = `(Engines READY 45) OR (T Engine_Started mc)`
  - **Resetting** = `(r u sure 10 hours check = 4) AND (not((r u sure 10 hours check = 1)))`
- Lit : `Engines READY 45`, `T Engine_Started mc`, `r u sure 10 hours check`
- Utilisé par : `Elec/10 hours true entre 10 et 16h`, `Elec/md4 10 hours check-up 45`, `Therm/10 hours true entre 10 et 16h`, `Therm/md4 10 hours check-up 45`
- Ligne export : 85023 · id 237498

#### Elec/md4 10 hours check-up 45  `CMSG`
> pop up message entre 10 et 12h (mod 10)
- Propriétés : Show message=All · Dialog type=Message · Text, English=10h Check to be performed
- Logique :
  - **Showing** = `((IMS Hours Elec [h] mod 10) >= 0) AND ((IMS Hours Elec [h] mod 10) <= 2) AND (IMS Hours Elec [h] >= 10) AND (Is_Electric mc) AND (Timer hiding first 10 hours check message [h] = 0)`
  - **Hiding** = `Timer hiding first 10 hours check message [h] > 0`
- Lit : `IMS Hours Elec`, `Is_Electric mc`, `Timer hiding first 10 hours check message`
- Utilisé par : *(personne)*
- Ligne export : 85108 · id 237443

#### Elec/md4 10 hours check-up 45  `CMSG`
> pop up message entre 12 et 16h (mod 10)
- Propriétés : Show message=All · Dialog type=Message · Header, English=10h Check not performed · Text, English=Look for details in Maintenance menu
- Logique :
  - **Showing** = `((IMS Hours Elec [h] mod 10) > 2) AND ((IMS Hours Elec [h] mod 10) < 5) AND (IMS Hours Elec [h] >= 10) AND (Is_Electric mc) AND (Timer hiding second 10 hours check message [h] = 0)`
  - **Hiding** = `Timer hiding second 10 hours check message [h] > 0`
- Lit : `IMS Hours Elec`, `Is_Electric mc`, `Timer hiding second 10 hours check message`
- Utilisé par : *(personne)*
- Ligne export : 85208 · id 237457

#### recording 10 hours check  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Text=10h Check recorded
- Logique :
  - **Showing** = `r u sure 10 hours wait`
  - **Hiding** = `not(r u sure 10 hours wait)`
- Lit : `r u sure 10 hours wait`
- Utilisé par : *(personne)*
- Ligne export : 85308 · id 237522

#### Maintenance type ------>  `TFC`
> Text qui s'affiche dans les log pour savoir quel type de maintenance a été réalisé
- Propriétés : Texts={{10h check}}
- Utilisé par : `Event log: Inspections`
- Ligne export : 85362 · id 239500

#### Therm/10 hours true entre 10 et 16h  `IDC`
> IDC pour l'activation ou non des messages entre 10 et 16h (mod 10) et si la 10 hours check list n'est pas faite
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `((IMS Hours Therm [h] mod 10) >= 0) AND ((IMS Hours Therm [h] mod 10) < 5) AND (IMS Hours Therm [h] >= 10) AND (Is_Thermic mc) AND (Timer hiding first 10 hours check message [h] <= 0) AND (Timer hiding second 10 hours check message [h] <= 0)`
- Lit : `IMS Hours Therm`, `Is_Thermic mc`, `Timer hiding first 10 hours check message`, `Timer hiding second 10 hours check message`
- Utilisé par : `10 hours true`, `Lampe sur bouton maintenance main page`
- Ligne export : 85374 · id 239894

#### Therm/md4 10 hours check-up 45  `CMSG`
> pop up message entre 12 et 16h (mod 10)
- Propriétés : Show message=All · Dialog type=Message · Header, English=10h Check not performed · Text, English=Look for details in Maintenance menu
- Logique :
  - **Showing** = `((IMS Hours Therm [h] mod 10) > 2) AND ((IMS Hours Therm [h] mod 10) < 5) AND (IMS Hours Therm [h] >= 10) AND (Is_Thermic mc) AND (Timer hiding second 10 hours check message [h] = 0)`
  - **Hiding** = `Timer hiding second 10 hours check message [h] > 0`
- Lit : `IMS Hours Therm`, `Is_Thermic mc`, `Timer hiding second 10 hours check message`
- Utilisé par : *(personne)*
- Ligne export : 85471 · id 239913

#### Therm/md4 10 hours check-up 45  `CMSG`
> pop up message entre 10 et 12h (mod 10)
- Propriétés : Show message=All · Dialog type=Message · Text, English=10h Check to be performed
- Logique :
  - **Showing** = `((IMS Hours Therm [h] mod 10) >= 0) AND ((IMS Hours Therm [h] mod 10) <= 2) AND (IMS Hours Therm [h] >= 10) AND (Is_Thermic mc) AND (Timer hiding first 10 hours check message [h] = 0)`
  - **Hiding** = `Timer hiding first 10 hours check message [h] > 0`
- Lit : `IMS Hours Therm`, `Is_Thermic mc`, `Timer hiding first 10 hours check message`
- Utilisé par : *(personne)*
- Ligne export : 85571 · id 239931

#### 10 hours true  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Therm/10 hours true entre 10 et 16h) OR (Elec/10 hours true entre 10 et 16h)`
- Lit : `Elec/10 hours true entre 10 et 16h`, `Therm/10 hours true entre 10 et 16h`
- Utilisé par : `MD4-5 page: 10 HOURS CHECK`, `MD4-5 page: MAINTENANCE`
- Ligne export : 85671 · id 239948

## logic screen md4 / WIP/45.Maintenance

#### Delivery month  `IP`
> date de livraison (mois)
- Propriétés : Default mode={0}
- Utilisé par : `Complete delivery date`, `Current month - Delivery month`, `Adjust group: Delivery date`, `MD4-5 page: INFO`, `MD4-5 page: MAINTENANCE`, `Single adjust item: Delivery month`
- Ligne export : 86857 · id 238162

#### Delivery day  `IP`
> date de livraison (jour), pas utilisé dans le programme
- Propriétés : Default mode={0}
- Utilisé par : `Adjust group: Delivery date`, `Single adjust item: Delivery day`
- Ligne export : 86869 · id 238163

#### Delivery Year  `IP`
> date de livraison (année)
- Propriétés : Default mode={2025}
- Utilisé par : `Année après livraison`, `Current Year - Delivery Year`, `Adjust group: Delivery date`, `MD4-5 page: INFO`, `Single adjust item: Delivery Year`
- Ligne export : 86881 · id 238164

#### Current month - Delivery month  `MAC`
- Logique :
  ```qcode
  Result:= Time/Date.Month - Delivery month
  ```
- Lit : `Date`, `Delivery month`, `Time`
- Utilisé par : `diff month >= 0`
- Ligne export : 86893 · id 238165

#### Current Year - Delivery Year  `MAC`
- Logique :
  ```qcode
  Result:= Time/Date.Year - Delivery Year
  ```
- Lit : `Date`, `Delivery Year`, `Time`
- Utilisé par : `diff year >=5`, `first year`, `second year`
- Ligne export : 86911 · id 238173

#### first year  `IDC`
> Condition pour la toute 1ère maintenance
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Current Year - Delivery Year = 1`
- Lit : `Current Year - Delivery Year`
- Utilisé par : `diff month >= 0`
- Ligne export : 86929 · id 238181

#### diff month >= 0  `IDC`
> Condition pour la toute 1ère maintenance: la différence d'année doit être supérieur à 1 et la diff de mois supérieur à 0.
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Current month - Delivery month >= 0) AND (first year)`
- Lit : `Current month - Delivery month`, `first year`
- Utilisé par : `first! 1yr maintenance`
- Ligne export : 86974 · id 238189

#### second year  `IDC`
> si la diff d'année est supérieur à 2 alors la condition s'active indéfiniment 
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Current Year - Delivery Year >= 2`
- Lit : `Current Year - Delivery Year`
- Utilisé par : `first! 1yr maintenance`
- Ligne export : 87026 · id 238208

#### RESET Maintenance  `DP`
> Met à jour la date actuel. fait comme un RESET classique mais sans rajouter +1 à maintenance counter
- Propriétés : True text=RESET  · False text=False · Default mode={False}
- Utilisé par : `>5 years maintenance wait log`, `IMS hours Elec RESET`, `IMS hours therm RESET`, `Nbr UP&DOWN RESET`, `RESET pin code`, `Remise sur False de RESET Maintenance Counter`, `day RESET 1yr maintenance`, `month RESET 1yr maintenance`, `r u sure 10 hours check`, `r u sure Maintenance`, `year RESET 1yr maintenance`, `Adjust group: Delivery date`, `Event log: Inspections`, `Single adjust item: RESET Maintenance`
- Ligne export : 87071 · id 238595

#### r u sure Maintenance  `IMSG`
> Message demandant si c'est vraiment ok pour le RESET maintenance (même message pour toutes les maintenances) 
- Propriétés : Show message=All · Dialog type=Confirmation · Header=RESET Maintenance? · Left button=No · Right button=Yes
- Logique :
  - **Showing** = `RESET pin code`
  - **Hiding** = `(r u sure Maintenance = 2) OR (r u sure Maintenance = 5) OR (r u sure RESET 1yr wait)`
- Lit : `RESET Maintenance`, `RESET pin code`, `r u sure RESET 1yr wait`
- Utilisé par : `IMS hours Elec RESET`, `IMS hours therm RESET`, `Nbr UP&DOWN RESET`, `Wait reset pin code`, `affichage Button RESET 2yrs maintenance`, `affichage Button RESET 4yrs maintenance`, `affichage button 1yr maintenance`, `day RESET 1yr maintenance`, `month RESET 1yr maintenance`, `r u sure RESET 1yr wait`, `year RESET 1yr maintenance`, `Event log: Inspections`
- Ligne export : 87084 · id 238606

#### r u sure RESET 1yr wait  `IDC`
> IDC pour cacher le message "are you sure" en cas de réponse "yes" et pour afficher le message de confirmation d'enregistrement du check
- Propriétés : Toggle=No · Delay on=500 · Delay off=5000
- Logique :
  - **Activating** = `r u sure Maintenance = 4`
- Lit : `r u sure Maintenance`
- Utilisé par : `Maintenance Counter`, `r u sure Maintenance`, `recording 10 hours check`
- Ligne export : 87157 · id 238614

#### Wait reset pin code  `IDC`
> Pour que le reseting du "RESET pin code" se fasse correctement
- Propriétés : Toggle=No · Delay on=200 · Delay off=2000
- Logique :
  - **Activating** = `r u sure Maintenance = 1`
- Lit : `r u sure Maintenance`
- Utilisé par : `RESET pin code`
- Ligne export : 87202 · id 239864

#### RESET pin code  `PCC`
> code pin necessaire pour RESET une maintenance. Same pin code as delivery date menu
- Propriétés : Show message=All · Header=RESET Pin Code · Text=Call Iguana Yachts support to have the pin code · PIN code=PIN Code delivery date & RESET Maintenance
- Logique :
  - **Showing** = `(B15 1yr) OR (B16 2yrs) OR (B17 4yrs)`
  - **Resetting** = `Wait reset pin code`
- Lit : `B15 1yr`, `B16 2yrs`, `B17 4yrs`, `RESET Maintenance`, `Wait reset pin code`
- Utilisé par : `r u sure Maintenance`
- Ligne export : 87247 · id 239758

#### month RESET 1yr maintenance  `MEM`
> Mémorise le mois quand on appuie sur RESET
- Propriétés : Input channel=Month · Action=Replace · Store value=Yes · Reset value=Month
- Logique :
  - **Activating** = `r u sure Maintenance = 4`
  - **Resetting** = `RESET Maintenance`
- Lit : `Month`, `RESET Maintenance`, `r u sure Maintenance`
- Utilisé par : `Current month - month RESET 1yr Maintenance`, `MD4-5 page: MAINTENANCE`
- Ligne export : 87312 · id 238216

#### day RESET 1yr maintenance  `MEM`
- Propriétés : Input channel=Day · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `r u sure Maintenance = 4`
  - **Resetting** = `RESET Maintenance`
- Lit : `Day`, `RESET Maintenance`, `r u sure Maintenance`
- Utilisé par : *(personne)*
- Ligne export : 87365 · id 238224

#### year RESET 1yr maintenance  `MEM`
> Mémorise l'année quand on appuie sur RESET
- Propriétés : Input channel=Year · Action=Replace · Store value=Yes · Reset value=Year
- Logique :
  - **Activating** = `r u sure Maintenance = 4`
  - **Resetting** = `RESET Maintenance`
- Lit : `RESET Maintenance`, `Year`, `r u sure Maintenance`
- Utilisé par : `année de la prochaine maintenance`, `current year - year RESET 1yr Maintenance`
- Ligne export : 87418 · id 238232

#### Maintenance Counter  `ECNT`
> a chaque RESET le maintenance counter est incrémenté de +1. => permet de savoir où en est dans la séquence des maintenance
- Propriétés : Store value=Yes · Reset value=0
- Logique :
  - **Increasing** = `r u sure RESET 1yr wait`
- Lit : `r u sure RESET 1yr wait`
- Utilisé par : `1yr Maintenance`, `2yrs Maintenance`, `4yrs Maintenance`, `Counter activation 2yr maintenance`, `Counter activation 4yrs maintenance`, `Maintenance counter = 0`, `Maintenance counter >=1`, `diff year >=5`, `first! 1yr maintenance`, `Adjust group: Delivery date`, `Single adjust item: Maintenance Counter`
- Ligne export : 87471 · id 238571

#### first! 1yr maintenance  `IDC`
> toute 1ère maintenance, elle permet quand on la RESET d'enregistrer la date de la 1ère maintenance et donc de calibrer les suivantes
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(diff month >= 0) OR (second year) OR (IMS Hours Elec [h] >= 50) OR (IMS Hours Therm [h] >= 50) OR (Number UP&Down >= 100)`
  - **Blocking** = `Maintenance Counter >= 1`
- Lit : `IMS Hours Elec`, `IMS Hours Therm`, `Maintenance Counter`, `Number UP&Down`, `diff month >= 0`, `second year`
- Utilisé par : `First 1yr Maintenance wait log`, `affichage button 1yr maintenance`, `message pour faire la maintenance`
- Ligne export : 87522 · id 238240

#### Current month - month RESET 1yr Maintenance  `MAC`
- Logique :
  ```qcode
  Result:= Time/Date.Month - month RESET 1yr maintenance
  ```
- Lit : `Date`, `Time`, `month RESET 1yr maintenance`
- Utilisé par : `diff month`
- Ligne export : 87608 · id 238264

#### current year - year RESET 1yr Maintenance  `MAC`
- Logique :
  ```qcode
  Result:=Time/Date.Year - year RESET 1yr maintenance
  ```
- Lit : `Date`, `Time`, `year RESET 1yr maintenance`
- Utilisé par : `diff year`, `diff year >=5`, `year after`
- Ligne export : 87626 · id 238272

#### Remise sur False de RESET Maintenance Counter  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Set "RESET Maintenance" to False!!
- Logique :
  - **Showing** = `RESET Maintenance`
  - **Hiding** = `not(RESET Maintenance)`
- Lit : `RESET Maintenance`
- Utilisé par : *(personne)*
- Ligne export : 87644 · id 238601

#### recording 10 hours check  `CMSG`
> message que dit que l'enregistrement à bien été enregistré dans les log
- Propriétés : Show message=All · Dialog type=Information · Text=Maintenance recorded
- Logique :
  - **Showing** = `r u sure RESET 1yr wait`
  - **Hiding** = `not(r u sure RESET 1yr wait)`
- Lit : `r u sure RESET 1yr wait`
- Utilisé par : *(personne)*
- Ligne export : 87698 · id 238627

#### diff year  `IDC`
> Condition pour la toute les maintenance suivante
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `current year - year RESET 1yr Maintenance = 1`
- Lit : `current year - year RESET 1yr Maintenance`
- Utilisé par : `diff month`
- Ligne export : 87752 · id 238670

#### diff month  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(diff year) AND (Current month - month RESET 1yr Maintenance >= 0)`
- Lit : `Current month - month RESET 1yr Maintenance`, `diff year`
- Utilisé par : `Maintenance`
- Ligne export : 87797 · id 238675

#### year after  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `current year - year RESET 1yr Maintenance >= 2`
- Lit : `current year - year RESET 1yr Maintenance`
- Utilisé par : `Maintenance`
- Ligne export : 87849 · id 238686

#### IMS hours therm RESET  `MEM`
> enregistre le nombre d'heure IMS therm au moment du reset
- Propriétés : Input channel=IMS Hours Therm [h] · Action=Replace · Store value=Yes · Reset value=IMS Hours Therm [h]
- Logique :
  - **Activating** = `r u sure Maintenance = 4`
  - **Resetting** = `RESET Maintenance`
- Lit : `IMS Hours Therm`, `RESET Maintenance`, `r u sure Maintenance`
- Utilisé par : `IMS hours ther + 50`
- Ligne export : 87894 · id 240173

#### IMS hours ther + 50  `MAC`
- Logique :
  ```qcode
  Result:=IMS hours therm RESET + 50
  ```
- Lit : `IMS hours therm RESET`
- Utilisé par : `Maintenance`
- Ligne export : 87947 · id 240218

#### IMS hours Elec RESET  `MEM`
> enregistre les IMS hours au moment du reset
- Propriétés : Input channel=IMS Hours Elec [h] · Action=Replace · Store value=Yes · Reset value=IMS Hours Elec [h]
- Logique :
  - **Activating** = `r u sure Maintenance = 4`
  - **Resetting** = `RESET Maintenance`
- Lit : `IMS Hours Elec`, `RESET Maintenance`, `r u sure Maintenance`
- Utilisé par : `IMS hours elec + 50`
- Ligne export : 87965 · id 240177

#### IMS hours elec + 50  `MAC`
- Logique :
  ```qcode
  Result:=IMS hours Elec RESET + 50
  ```
- Lit : `IMS hours Elec RESET`
- Utilisé par : `Maintenance`
- Ligne export : 88018 · id 240229

#### Nbr UP&DOWN RESET  `MEM`
> enregistre le nombre de UP&DOWN au moment du reset
- Propriétés : Input channel=Number UP&Down · Action=Replace · Store value=Yes · Reset value=Number UP&Down
- Logique :
  - **Activating** = `r u sure Maintenance = 4`
  - **Resetting** = `RESET Maintenance`
- Lit : `Number UP&Down`, `RESET Maintenance`, `r u sure Maintenance`
- Utilisé par : `nbr up&down + 100`
- Ligne export : 88036 · id 240203

#### nbr up&down + 100  `MAC`
- Logique :
  ```qcode
  Result:=Nbr UP&DOWN RESET + 100
  ```
- Lit : `Nbr UP&DOWN RESET`
- Utilisé par : `Maintenance`
- Ligne export : 88089 · id 240234

#### Maintenance  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(diff month) OR (year after) OR (IMS Hours Elec [h] >= IMS hours elec + 50) OR (IMS Hours Therm [h] >= IMS hours ther + 50) OR (Number UP&Down >= nbr up&down + 100)`
- Lit : `IMS Hours Elec`, `IMS Hours Therm`, `IMS hours elec + 50`, `IMS hours ther + 50`, `Number UP&Down`, `diff month`, `nbr up&down + 100`, `year after`
- Utilisé par : `1yr Maintenance`, `2yrs Maintenance`, `4yrs Maintenance`, `Maintenance type->`
- Ligne export : 88107 · id 238646

#### diff year >=5  `IDC`
> en cas de maintenance non faite depuis au moins 4 ans ce IDC s'active et fait poper un message d'alerte de type "critical"
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `((current year - year RESET 1yr Maintenance >= 5) and (Maintenance Counter >= 1)) OR ((Maintenance Counter = 0) and (Current Year - Delivery Year >= 5))`
- Lit : `Current Year - Delivery Year`, `Maintenance Counter`, `current year - year RESET 1yr Maintenance`
- Utilisé par : `>5 years maintenance wait log`, `Counter activation 2yr maintenance`, `Counter activation 4yrs maintenance`, `activation text yearly maintenance`, `message d'alerte pour non entretien depuis 4 ans au moins`, `Event log: Inspections`
- Ligne export : 88184 · id 239818

#### >5 years maintenance wait log  `IDC`
> Utile pour que l'enregistrement des log se fasse correctement
- Propriétés : Toggle=No · Delay on=200 · Delay off=0
- Logique :
  - **Activating** = `(diff year >=5) OR (RESET Maintenance)`
- Lit : `RESET Maintenance`, `diff year >=5`
- Utilisé par : `Counter activation 2yr maintenance`, `Counter activation 4yrs maintenance`, `activation text yearly maintenance`, `Event log: Inspections`
- Ligne export : 88274 · id 240145

#### Counter activation 2yr maintenance  `IDC`
> utile pour activer la 2yrs maintenance au bon moment dans la séquence des maintenance.
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Maintenance Counter = 1) OR (Maintenance Counter = 5) OR (Maintenance Counter = 9) OR (Maintenance Counter = 13) OR (Maintenance Counter = 17) OR (Maintenance Counter = 21) OR (Maintenance Counter = 25) OR (Maintenance Counter = 29) OR (Maintenance Counter = 33) OR (Maintenance Counter = 37) OR (Maintenance Counter = 41) OR (Maintenance Counter = 45) OR (Maintenance Counter = 49) OR (Maintenance Counter = 53) OR (Maintenance Counter = 57) OR (Maintenance Counter = 61)`
  - **Blocking** = `(diff year >=5) OR (>5 years maintenance wait log)`
- Lit : `13`, `>5 years maintenance wait log`, `Maintenance Counter`, `diff year >=5`
- Utilisé par : `2yrs Maintenance`, `activation text yearly maintenance`, `Event log: Inspections`, `MD4-5 page: MAINTENANCE`
- Ligne export : 88324 · id 238784

#### 2yrs Maintenance  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Maintenance AND (Counter activation 2yr maintenance)`
  - **Blocking** = `Maintenance Counter < 1`
- Lit : `Counter activation 2yr maintenance`, `Maintenance`, `Maintenance Counter`
- Utilisé par : `2yrs maintenance wait log`, `Lampe sur bouton maintenance main page`, `Maintenance type-->`, `affichage Button RESET 2yrs maintenance`, `message pour faire la maintenance`, `MD4-5 page: MAINTENANCE`
- Ligne export : 88518 · id 238707

#### 1yr Maintenance  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Maintenance AND ((Maintenance Counter mod 2) = 0)`
  - **Blocking** = `Maintenance Counter <= 1`
- Lit : `Maintenance`, `Maintenance Counter`
- Utilisé par : `1yr maintenance wait log`, `affichage button 1yr maintenance`, `message pour faire la maintenance`
- Ligne export : 88577 · id 238711

#### Counter activation 4yrs maintenance  `IDC`
> utile pour activer la 4yrs maintenance au bon moment dans la séquence des maintenance.
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Maintenance Counter = 3) OR (Maintenance Counter = 7) OR (Maintenance Counter = 11) OR (Maintenance Counter = 15) OR (Maintenance Counter = 19) OR (Maintenance Counter = 23) OR (Maintenance Counter = 27) OR (Maintenance Counter = 31) OR (Maintenance Counter = 35) OR (Maintenance Counter = 39) OR (Maintenance Counter = 43) OR (Maintenance Counter = 47) OR (Maintenance Counter = 51) OR (Maintenance Counter = 55) OR (Maintenance Counter = 59) OR (Maintenance Counter = 63)`
  - **Blocking** = `(diff year >=5) OR (>5 years maintenance wait log)`
- Lit : `>5 years maintenance wait log`, `Maintenance Counter`, `diff year >=5`
- Utilisé par : `4yrs Maintenance`, `activation text yearly maintenance`, `Event log: Inspections`, `MD4-5 page: MAINTENANCE`
- Ligne export : 88647 · id 238788

#### 4yrs Maintenance  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Maintenance AND (Counter activation 4yrs maintenance)`
  - **Blocking** = `Maintenance Counter <= 1`
- Lit : `Counter activation 4yrs maintenance`, `Maintenance`, `Maintenance Counter`
- Utilisé par : `4yrs maintenance wait log`, `Lampe sur bouton maintenance main page`, `Maintenance type ---->`, `affichage Button RESET 4yrs maintenance`, `message pour faire la maintenance`, `MD4-5 page: MAINTENANCE`
- Ligne export : 88841 · id 238715

#### affichage button 1yr maintenance  `IDC`
> IDC pour afficher les notifications et boutons pour les maintenance de 1ère année
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(first! 1yr maintenance) OR (1yr Maintenance)`
  - **Blocking** = `r u sure Maintenance = 1`
- Lit : `1yr Maintenance`, `first! 1yr maintenance`, `r u sure Maintenance`
- Utilisé par : `Lampe sur bouton maintenance main page`, `MD4-5 page: 1YR MAINTENANCE`, `MD4-5 page: MAINTENANCE`
- Ligne export : 88900 · id 238839

#### message pour faire la maintenance  `CMSG`
> message pop up d'alerte de maintenance à réaliser
- Propriétés : Show message=All · Dialog type=Message · Text=Maintenance to be performed
- Logique :
  - **Showing** = `(1yr Maintenance) OR (2yrs Maintenance) OR (4yrs Maintenance) OR (first! 1yr maintenance)`
- Lit : `1yr Maintenance`, `2yrs Maintenance`, `4yrs Maintenance`, `first! 1yr maintenance`
- Utilisé par : *(personne)*
- Ligne export : 88959 · id 238859

#### Maintenance type->  `TFC`
> text qui s'enregistre dans les log lors d'un RESET pour savoir quelle maintenance a été réalisé dans les log
- Propriétés : Texts={{Yearly Maintenance}}
- Lit : `Maintenance`
- Utilisé par : `Event log: Inspections`
- Ligne export : 89026 · id 238883

#### Maintenance type-->  `TFC`
> text qui s'enregistre dans les log lors d'un RESET pour savoir quelle maintenance a été réalisé dans les log
- Propriétés : Texts={{2yrs Maintenance}}
- Lit : `2yrs Maintenance`
- Utilisé par : `Event log: Inspections`
- Ligne export : 89038 · id 238899

#### Maintenance type ---->  `TFC`
> text qui s'enregistre dans les log lors d'un RESET pour savoir quelle maintenance a été réalisé dans les log
- Propriétés : Texts={{4yrs Maintenance}}
- Lit : `4yrs Maintenance`
- Utilisé par : `Event log: Inspections`
- Ligne export : 89050 · id 238906

#### First 1yr Maintenance wait log  `IDC`
> delay de 500ms pour que le log n'enregistre pas "1yr maintenance" lorsqu'une autre maintenance est RESET. En effet, la "1yr maintenance " se met en true un bref instant quand on RESET n'importe quelle maintenance.
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `first! 1yr maintenance`
- Lit : `first! 1yr maintenance`
- Utilisé par : `Event log: Inspections`
- Ligne export : 89062 · id 239415

#### 2yrs maintenance wait log  `IDC`
> Utile pour que l'enregistrement des log se fasse correctement
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `2yrs Maintenance`
- Lit : `2yrs Maintenance`
- Utilisé par : `Event log: Inspections`
- Ligne export : 89105 · id 239421

#### 4yrs maintenance wait log  `IDC`
> Utile pour que l'enregistrement des log se fasse correctement
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `4yrs Maintenance`
- Lit : `4yrs Maintenance`
- Utilisé par : `Event log: Inspections`
- Ligne export : 89148 · id 239433

#### 1yr maintenance wait log  `IDC`
> Utile pour que l'enregistrement des log se fasse correctement
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `1yr Maintenance`
- Lit : `1yr Maintenance`
- Utilisé par : `Event log: Inspections`
- Ligne export : 89191 · id 239445

#### année de la prochaine maintenance  `MAC`
> rajoute 1 à l'année mémorisé lors du RESET maintenance pour afficher l'année de la prochaine maintenance sur la maintenance page
- Logique :
  ```qcode
  Result:=year RESET 1yr maintenance + 1
  ```
- Lit : `year RESET 1yr maintenance`
- Utilisé par : `MD4-5 page: MAINTENANCE`
- Ligne export : 89234 · id 239489

#### Maintenance counter = 0  `IDC`
> utilisé pour afficher la date de la prochaine maintenance quand aucune maintenance n'a encore été faite
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Maintenance Counter = 0`
  - **Blocking** = `Maintenance Counter >= 1`
- Lit : `Maintenance Counter`
- Utilisé par : `MD4-5 page: MAINTENANCE`
- Ligne export : 89252 · id 239509

#### Année après livraison  `MAC`
> Rajoute +1 à l'année de livraison
- Logique :
  ```qcode
  Result:=Delivery Year + 1
  ```
- Lit : `Delivery Year`
- Utilisé par : `MD4-5 page: MAINTENANCE`
- Ligne export : 89306 · id 239521

#### Maintenance counter >=1  `IDC`
> utilisé pour afficher la date de la prochaine maintenance après la 1ère maintenance
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Maintenance Counter >= 1`
- Lit : `Maintenance Counter`
- Utilisé par : `MD4-5 page: MAINTENANCE`
- Ligne export : 89324 · id 239533

#### IDC text yearly maintenance  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : *(personne)*
- Ligne export : 89369 · id 239582

#### activation text yearly maintenance  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(not(Counter activation 2yr maintenance)) AND (not(Counter activation 4yrs maintenance))`
  - **Blocking** = `(Counter activation 2yr maintenance) OR (Counter activation 4yrs maintenance) OR (diff year >=5) OR (>5 years maintenance wait log)`
- Lit : `>5 years maintenance wait log`, `Counter activation 2yr maintenance`, `Counter activation 4yrs maintenance`, `diff year >=5`
- Utilisé par : `Event log: Inspections`, `MD4-5 page: MAINTENANCE`
- Ligne export : 89405 · id 239646

#### Complete delivery date  `CMSG`
> Tant que le mois est à zero (valeur par défaut) c'est que la date de livraison n'a pas été rempli donc un message pop pour dire de compléter la date
- Propriétés : Show message=All · Dialog type=Warning · Header=Complete the delivery date! · Text=Call Iguana Yachts support if you don't know the delivery date code pin
- Logique :
  - **Showing** = `Delivery month = 0`
  - **Hiding** = `Delivery month >= 1`
- Lit : `Delivery month`
- Utilisé par : *(personne)*
- Ligne export : 89485 · id 239739

#### affichage Button RESET 2yrs maintenance  `IDC`
> IDC pour bloquer l'affichage du bouton RESET quand le message "r u sure..." est affiché, permet d'éviter certain cas de défaillance
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `2yrs Maintenance`
  - **Blocking** = `r u sure Maintenance = 1`
- Lit : `2yrs Maintenance`, `r u sure Maintenance`
- Utilisé par : `MD4-5 page: 2YRS MAINTENANCE`
- Ligne export : 89542 · id 239784

#### affichage Button RESET 4yrs maintenance  `IDC`
> IDC pour bloquer l'affichage du bouton RESET quand le message "r u sure..." est affiché, permet d'éviter certain cas de défaillance
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `4yrs Maintenance`
  - **Blocking** = `r u sure Maintenance = 1`
- Lit : `4yrs Maintenance`, `r u sure Maintenance`
- Utilisé par : `MD4-5 page: 4YRS MAINTENANCE`
- Ligne export : 89594 · id 239789

#### message d'alerte pour non entretien depuis 4 ans au moins  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header=Warning! · Text=You didn't maintain your boat for 4 years now (at least). It's dangerous to use your boat! Call Iguana Yachts support before using it.
- Logique :
  - **Showing** = `diff year >=5`
- Lit : `diff year >=5`
- Utilisé par : *(personne)*
- Ligne export : 89646 · id 239830

#### Maintenance type:  `TFC`
> text qui s'enregistre dans les log lors d'un RESET pour savoir quelle maintenance a été réalisé dans les log
- Propriétés : Texts={{1, 2 & 4yrs maintenance}}
- Utilisé par : `Event log: Inspections`
- Ligne export : 89692 · id 240136

## logic screen md4 / WIP/45.Maintenance / Time/Date

#### Date  `SIC`
- Propriétés : Value=Date
- Utilisé par : `Current Year - Delivery Year`, `Current month - Delivery month`, `Current month - month RESET 1yr Maintenance`, `Date 2`, `current year - year RESET 1yr Maintenance`, `daysSince2000`, `MD4-5 page: BASE`
- Ligne export : 85763 · id 237936

#### daysSince2000  `IMAC`
- Logique :
  - **Controlling** = `Date - 36526`
- Lit : `Date`
- Utilisé par : `daysInCurrentYear`, `yearSince2000`
- Ligne export : 85772 · id 237937

#### yearSince2000  `IMAC`
- Logique :
  ```qcode
  removeLeapYearDays := daysSince2000 div 1462
  Result := (daysSince2000 -1 -removeLeapYearDays) div 365
  ```
- Lit : `daysSince2000`
- Utilisé par : `Year`, `daysInCurrentYear`, `isLeapYear`
- Ligne export : 85815 · id 237945

#### isLeapYear  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result := (yearSince2000 mod 4) = 0
  ```
- Lit : `yearSince2000`
- Utilisé par : `Day`, `Month text`
- Ligne export : 85834 · id 237958

#### daysInCurrentYear  `IMAC`
- Logique :
  ```qcode
  Result := (daysSince2000 - (yearSince2000 * 365)) - (yearSince2000 div 4)
  ```
- Lit : `daysSince2000`, `yearSince2000`
- Utilisé par : `Day`, `Month text`
- Ligne export : 85854 · id 237967

#### Month text  `SMC`
- Propriétés : Default state name=jan
- Fonction *feb* :
  - **Activating** = `(Inside(daysInCurrentYear, 30, 60)) OR (Inside(daysInCurrentYear, 31, 60)) OR ((isLeapYear ? A : B))`
- Fonction *mars* :
  - **Activating** = `Inside(daysInCurrentYear, 59, 91)`
- Fonction *april* :
  - **Activating** = `Inside(daysInCurrentYear, 90, 121)`
- Fonction *may* :
  - **Activating** = `Inside(daysInCurrentYear, 120, 152)`
- Fonction *june* :
  - **Activating** = `Inside(daysInCurrentYear, 151, 182)`
- Fonction *july* :
  - **Activating** = `Inside(daysInCurrentYear, 181, 213)`
- Fonction *aug* :
  - **Activating** = `Inside(daysInCurrentYear, 212, 244)`
- Fonction *sept* :
  - **Activating** = `Inside(daysInCurrentYear, 243, 274)`
- Fonction *oct* :
  - **Activating** = `Inside(daysInCurrentYear, 273, 305)`
- Fonction *nov* :
  - **Activating** = `Inside(daysInCurrentYear, 304, 335)`
- Fonction *dec* :
  - **Activating** = `Inside(daysInCurrentYear, 334, 366)`
- Lit : `daysInCurrentYear`, `isLeapYear`
- Utilisé par : `Day`, `Month`
- Ligne export : 85872 · id 237978

#### Day  `IMAC`
- Propriétés : Function selector=Month text
- Fonction *jan* :
  - **Controlling** = `daysInCurrentYear + (isLeapYear ? 1 : 0)`
- Fonction *feb* :
  - **Controlling** = `(daysInCurrentYear - 31) + (isLeapYear ? 1 : 0)`
- Fonction *mars* :
  - **Controlling** = `daysInCurrentYear - 59`
- Fonction *april* :
  - **Controlling** = `daysInCurrentYear - 90`
- Fonction *may* :
  - **Controlling** = `daysInCurrentYear - 120`
- Fonction *june* :
  - **Controlling** = `daysInCurrentYear - 151`
- Fonction *july* :
  - **Controlling** = `daysInCurrentYear - 181`
- Fonction *aug* :
  - **Controlling** = `daysInCurrentYear - 212`
- Fonction *sept* :
  - **Controlling** = `daysInCurrentYear - 243`
- Fonction *oct* :
  - **Controlling** = `daysInCurrentYear - 273`
- Fonction *nov* :
  - **Controlling** = `daysInCurrentYear - 304`
- Fonction *dec* :
  - **Controlling** = `daysInCurrentYear - 334`
- Lit : `Month text`, `daysInCurrentYear`, `isLeapYear`
- Utilisé par : `day RESET 1yr maintenance`
- Ligne export : 86274 · id 238028

#### Time  `SIC`
- Propriétés : Value=Time
- Utilisé par : `Current Year - Delivery Year`, `Current month - Delivery month`, `Current month - month RESET 1yr Maintenance`, `Hours`, `Time 2`, `current year - year RESET 1yr Maintenance`, `minutes`, `seconds`, `Adjust group: Master Tracks`
- Ligne export : 86707 · id 238116

#### Hours  `IMAC`
- Logique :
  ```qcode
  Result := (Time * 3600) div 3600
  ```
- Lit : `Time`
- Utilisé par : `minutes`, `seconds`
- Ligne export : 86716 · id 238117

#### minutes  `IMAC`
- Logique :
  ```qcode
  Result := ((Time - Hours) * 3600) div 60
  ```
- Lit : `Hours`, `Time`
- Utilisé par : *(personne)*
- Ligne export : 86734 · id 238126

#### seconds  `IMAC`
- Logique :
  ```qcode
  result := ((Time - Hours) * 3600) mod 60
  ```
- Lit : `Hours`, `Time`
- Utilisé par : *(personne)*
- Ligne export : 86752 · id 238136

#### Year  `IMAC`
- Logique :
  - **Controlling** = `yearSince2000 + 2000`
- Lit : `yearSince2000`
- Utilisé par : `year RESET 1yr maintenance`
- Ligne export : 86770 · id 238146

#### Month  `IMAC`
- Logique :
  - **Controlling** = `Month text + 1`
- Lit : `Month text`
- Utilisé par : `month RESET 1yr maintenance`
- Ligne export : 86813 · id 238154

## logic screen md4 / WIP/Pin delivery date

#### Adjustable parameter  `FP`
- Propriétés : Unit=% · Default mode={42}
- Utilisé par : `Single adjust item: Adjustable parameter`
- Ligne export : 89828 · id 239719

## logic screen md4 / send data to md4

#### ShutDown page IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(2 = eBoat State 4E) OR (3 = eBoat State 4E)`
- Lit : `eBoat State 4E`
- Utilisé par : `trameb 2`
- Ligne export : 83703 · id 215022

#### Startup page IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `0 = eBoat State 4E`
- Lit : `eBoat State 4E`
- Utilisé par : `trameb 2`
- Ligne export : 83757 · id 215250

#### Main page IDC E  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `4et.Is_Electric AND (Main page IDC)`
- Lit : `4et.Is_Electric`, `Main page IDC`
- Utilisé par : `trameb 2`
- Ligne export : 83802 · id 215418

#### Main page IDC T  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `4et.Is_Thermic AND (Main page IDC)`
- Lit : `4et.Is_Thermic`, `Main page IDC`
- Utilisé par : `trameb 2`
- Ligne export : 83852 · id 215427

#### Engines READY for 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Batt or engine started mc`
- Lit : `Batt or engine started mc`
- Utilisé par : `trameb 2`
- Ligne export : 83902 · id 216661

#### Safety_disable 45 sel  `IDC`
- Propriétés : Toggle=No · Delay on=1500 · Delay off=0
- Logique :
  - **Activating** = `(Safety_disable 45) OR (Force Safety off up/down 45)`
- Lit : `Force Safety off up/down 45`, `Safety_disable 45`
- Utilisé par : `Safety_disable mc`, `safety orange`, `trameb 2`
- Ligne export : 83945 · id 215508

#### Inter Buzzer for 45 button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter Buzzer 45`
- Lit : `Inter Buzzer 45`
- Utilisé par : `trameb 2`
- Ligne export : 83995 · id 216684

#### ALL ASK STOP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(ASK STOP 4ET) OR (PositiveFlank((Auto PAUSE/OFF 4ET [s] <= 0)))`
- Lit : `ASK STOP 4ET`, `Auto PAUSE/OFF 4ET`
- Utilisé par : `B9 toggle`, `Timer Auto Sleep Engine`, `trameb 2`
- Ligne export : 84038 · id 214797

#### Reset safety to on 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank(B9 Start Button 4ET START Sel)) OR ((State Up/Down 4ET [%] <= 0) and (NegativeFlank(Inter DOWN))) OR (not(Engines READY 45)) OR (B11 Safety off button 45 reset SAFETY OFF RESET Sel) OR (NegativeFlank(B9 Start Button 4ET START Sel)) OR ((not(Safety_disable 45)) and (NegativeFlank(B10 Safety off button 45 SAFETY OFF Sel)))`
- Lit : `B10 Safety off button 45 SAFETY OFF Sel`, `B11 Safety off button 45 reset SAFETY OFF RESET Sel`, `B9 Start Button 4ET START Sel`, `Engines READY 45`, `Inter DOWN`, `Safety_disable 45`, `State Up/Down 4ET`
- Utilisé par : `Safety_disable 45`, `trameb 2`
- Ligne export : 84098 · id 214333

#### enabled ON/OFF T&E  `FGI`
- Propriétés : Input type=Digital · Input=enabled ON/OFF T&E · Default state name=Default state
- Lit : `enabled ON/OFF T&E`
- Utilisé par : `trameb 2`
- Ligne export : 84216 · id 240670

#### BUTTON DRIVE 4ET 45/10  `FGI`
- Propriétés : Input type=Digital · Input=BUTTON DRIVE 4ET · Default state name=Default state
- Lit : `BUTTON DRIVE 4ET`
- Utilisé par : `trameb 2`
- Ligne export : 84227 · id 240917

#### trameb 2  `ARC`
- Propriétés : Array size=12 · Store value=No
- Logique :
  ```qcode
  This[0]:=Inter Buzzer for 45 button*1
  This[1]:=Main page IDC E*2
  This[2]:=Main page IDC T*4
  This[3]:=ShutDown page IDC*8
  This[4]:=Startup page IDC*16
  This[5]:=Engines READY for 45*32
  This[6]:=Safety_disable 45 sel*64
  This[7]:=ALL ASK STOP*128
  This[8]:=Reset safety to on 45*256
  This[9]:=batt ok to start*512
  This[10]:=enabled ON/OFF T&E*1024
  This[11]:=BUTTON DRIVE 4ET 45/10*2048
  ```
- Lit : `12`, `ALL ASK STOP`, `BUTTON DRIVE 4ET 45/10`, `Engines READY for 45`, `Inter Buzzer for 45 button`, `Main page IDC E`, `Main page IDC T`, `Reset safety to on 45`, `Safety_disable 45 sel`, `ShutDown page IDC`, `Startup page IDC`, `batt ok to start`, `enabled ON/OFF T&E`
- Utilisé par : `dtobin 2`
- Ligne export : 84238 · id 216705

#### dtobin 2  `MAC`
- Logique :
  ```qcode
  Result:=trameb 2[0]+trameb 2[1]+trameb 2[2]+trameb 2[3]+trameb 2[4]+trameb 2[5]+trameb 2[6]+trameb 2[7]+trameb 2[8]+trameb 2[9]+trameb 2[10]+trameb 2[11]
  ```
- Lit : `trameb 2`
- Utilisé par : `debug btod 2`, `infos for 45/10 dtobin 2 APPOUT`
- Ligne export : 84269 · id 216738

#### debug btod 2  `ARC`
- Propriétés : Array size=12 · Store value=No
- Logique :
  ```qcode
  This[0]:=dtobin 2 mod 2
  This[1]:=(dtobin 2 div 2) mod 2
  This[2]:=(dtobin 2 div 4) mod 2
  This[3]:=(dtobin 2 div 8) mod 2
  This[4]:=(dtobin 2 div 16) mod 2
  This[5]:=(dtobin 2 div 32) mod 2
  This[6]:=(dtobin 2 div 64) mod 2
  This[7]:=(dtobin 2 div 128) mod 2
  This[8]:=(dtobin 2 div 256) mod 2
  This[9]:=(dtobin 2 div 512) mod 2
  This[10]:=(dtobin 2 div 1024) mod 2
  This[11]:=(dtobin 2 div 2048) mod 2
  ```
- Lit : `12`, `dtobin 2`
- Utilisé par : `debug Be1 Inter Buzzer for 45`, `debug Be10 batt ok to start`, `debug Be2 Main page IDC E`, `debug Be3 Main page IDC T`, `debug Be4 ShutDown page IDC`, `debug Be5 Startup page IDC`, `debug Be6 Engines READY for 45`, `debug Be7 Safety_disable 45 sel`, `debug Be8 ALL ASK STOP`, `debug Be9 Reset safety to on 45`, `debug button drive 4ET 45/10`, `debug enabled on/off`
- Ligne export : 84287 · id 216770

#### debug Be1 Inter Buzzer for 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 2[0]
  ```
- Lit : `debug btod 2`
- Utilisé par : *(personne)*
- Ligne export : 84318 · id 216815

#### debug Be2 Main page IDC E  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 2[1]
  ```
- Lit : `debug btod 2`
- Utilisé par : *(personne)*
- Ligne export : 84338 · id 216823

#### debug Be3 Main page IDC T  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 2[2]
  ```
- Lit : `debug btod 2`
- Utilisé par : *(personne)*
- Ligne export : 84358 · id 216831

#### debug Be4 ShutDown page IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 2[3]
  ```
- Lit : `debug btod 2`
- Utilisé par : *(personne)*
- Ligne export : 84378 · id 216839

#### debug Be5 Startup page IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 2[4]
  ```
- Lit : `debug btod 2`
- Utilisé par : *(personne)*
- Ligne export : 84398 · id 216847

#### debug Be6 Engines READY for 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 2[5]
  ```
- Lit : `debug btod 2`
- Utilisé par : *(personne)*
- Ligne export : 84418 · id 216855

#### debug Be7 Safety_disable 45 sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 2[6]
  ```
- Lit : `debug btod 2`
- Utilisé par : *(personne)*
- Ligne export : 84438 · id 216863

#### infos for 45/10 dtobin 2 APPOUT  `APPOUT`
- Propriétés : Input channel=dtobin 2 · Send method=On change · Transmit rate=200
- Lit : `dtobin 2`
- Utilisé par : `dtobin 2 APPIN c10`, `info from mc dtobin 2 APPIN`
- Ligne export : 84458 · id 216903

#### debug Be8 ALL ASK STOP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 2[7]
  ```
- Lit : `debug btod 2`
- Utilisé par : *(personne)*
- Ligne export : 84469 · id 217142

#### debug Be9 Reset safety to on 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 2[8]
  ```
- Lit : `debug btod 2`
- Utilisé par : *(personne)*
- Ligne export : 84489 · id 217150

#### Safety_disable mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Safety_disable 45 sel`
- Lit : `Safety_disable 45 sel`
- Utilisé par : `fast d3`, `fast d3 safetyoff`, `s.slow d3`, `s.slow d3 safetyoff`, `slow d3`, `slow d3 safetyoff`
- Ligne export : 84509 · id 212661

#### debug Be10 batt ok to start  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 2[9]
  ```
- Lit : `debug btod 2`
- Utilisé par : *(personne)*
- Ligne export : 84552 · id 233829

#### debug enabled on/off  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 2[10]
  ```
- Lit : `debug btod 2`
- Utilisé par : *(personne)*
- Ligne export : 84572 · id 240925

#### debug button drive 4ET 45/10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 2[11]
  ```
- Lit : `debug btod 2`
- Utilisé par : *(personne)*
- Ligne export : 84592 · id 240929
