# MD3 — (racine appli)

55 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## (racine)

#### MDGN-VREF:MD3-0  `MDGN`
- Propriétés : Value=Reference voltage [V] · Module=MD3[0] · Module index=4
- Utilisé par : *(personne)*
- Ligne export : 43 · id 1040

#### MDGN-+BAT:MD3-0  `MDGN`
- Propriétés : Value=Supply voltage [V] · Module=MD3[0] · Module index=3
- Utilisé par : *(personne)*
- Ligne export : 54 · id 1041

#### MDGN-Temp:MD3-0  `MDGN`
- Propriétés : Value=Temperature [Â°C] · Module=MD3[0] · Module index=2
- Lit : `C`
- Utilisé par : *(personne)*
- Ligne export : 65 · id 1042

#### F4 Speed Free  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `F4 Input`, `F4 Speed Free`, `Toggle Free`, `MD3 page: BASE`
- Ligne export : 76 · id 1189

#### Automatic Joystick Inhibition  `IP`
- Propriétés : Unit=s · Default mode={300}
- Utilisé par : `Auto PAUSE/OFF`, `Adjust group: Setup`, `Single adjust item: Automatic Joystick Inhibition`
- Ligne export : 86 · id 59460

#### ENGINE RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `ENGINE RUN Input`
- Lit : ``, `ENGINE RUN Input`
- Utilisé par : `Engine hours`, `Ok to move`, `Speed State`, `Stop To Move`, `VIEW START PAGE`
- Ligne export : 98 · id 36087

#### Re-Track mode in water  `DP`
- Propriétés : True text=ACTIVE · False text=NO ACTIVE · Default mode={False}
- Utilisé par : `Ok to move`, `Re-Track mode in water`, `Adjust group: Maintenance`, `Single adjust item: Re-Track mode in water`
- Ligne export : 141 · id 22278

#### Reset on startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset on startup`
- Lit : ``
- Utilisé par : `Re-Track mode in water`
- Ligne export : 154 · id 22290

#### Re-Track mode in water  `MEM`
- Propriétés : Input channel=Re-Track mode in water · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Resetting** = `Reset on startup`
- Lit : ``, `Re-Track mode in water`, `Reset on startup`
- Utilisé par : `Ok to move`, `Adjust group: Maintenance`, `Single adjust item: Re-Track mode in water`
- Ligne export : 204 · id 22279

#### Ok to move  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(ENGINE RUN) AND (TRACK DOWN or Re-Track mode in water)`
- Lit : ``, `C`, `ENGINE RUN`, `Re-Track mode in water`, `TRACK DOWN`
- Utilisé par : `Ko to move`, `Math Droit`, `Math Gauche`, `Speed State`
- Ligne export : 248 · id 6388

#### Left Joystick  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-LST · Calibration={500; 4500; -100; 100} · Alarms={No; 0; No; 100} · Module=MD3[0] · Module index=0
- Utilisé par : `Joystick_Left_DMAC`, `Adjust group: Setup`, `Dual adjust item: Left Joystick`, `Measure group: Engine and Translation`, `Measure group: Translation`
- Ligne export : 314 · id 1004

#### Neutral Joystick  `FP`
- Propriétés : Unit=% · Default mode={10}
- Utilisé par : `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `Adjust group: Setup`, `Single adjust item: Neutral Joystick`
- Ligne export : 338 · id 23852

#### Joytsick_Neutral_Plus  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `Neutral Joystick [%]`
- Lit : ``, `Neutral Joystick`
- Utilisé par : `Joystick_Left_DMAC`, `Joystick_Right_DMAC`
- Ligne export : 350 · id 23853

#### Joytsick_Neutral_Minus  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `Neutral Joystick [%] * -1`
- Lit : ``, `Neutral Joystick`
- Utilisé par : `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Stop Cruise`
- Ligne export : 392 · id 23861

#### Joystick_Left_DMAC  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `courbe(Left Joystick [%]: {{-95; -100}; {Joytsick_Neutral_Minus [%]; 0}; {Joytsick_Neutral_Plus [%]; 0}; {95; 100}}, Freeze)`
- Lit : ``, `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `Left Joystick`
- Utilisé par : `Allow Cruise`, `Allow Run Cruise`, `Auto Stop Timer`, `Math Gauche`, `Stop Cruise`
- Ligne export : 436 · id 23869

#### Math Gauche  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Command State
- Fonction *Normal* :
  - **Controlling** = `Joystick_Left_DMAC [%]`
- Fonction *Radio* :
  - **Controlling** = `Ok to move * RadioGauche% [%]`
- Lit : ``, `Command State`, `Joystick_Left_DMAC`, `Ok to move`, `RadioGauche%`
- Utilisé par : `Joystick Zero`, `Manip Gauche CanOut`
- Ligne export : 500 · id 6654

#### Right Joystick  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-LST · Calibration={500; 4500; -100; 100} · Alarms={No; 0; No; 100} · Module=MD3[0] · Module index=1
- Utilisé par : `Joystick_Right_DMAC`, `Adjust group: Setup`, `Dual adjust item: Right Joystick`, `Measure group: Engine and Translation`, `Measure group: Translation`
- Ligne export : 589 · id 1065

#### Joystick_Right_DMAC  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `courbe(Right Joystick [%]: {{-95; -100}; {Joytsick_Neutral_Minus [%]; 0}; {Joytsick_Neutral_Plus [%]; 0}; {95; 100}}, Freeze)`
- Lit : ``, `Joytsick_Neutral_Minus`, `Joytsick_Neutral_Plus`, `Right Joystick`
- Utilisé par : `Allow Cruise`, `Allow Run Cruise`, `Auto Stop Timer`, `Math Droit`, `Stop Cruise`
- Ligne export : 613 · id 23880

#### Math Droit  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Command State
- Fonction *Normal* :
  - **Controlling** = `Joystick_Right_DMAC [%]`
- Fonction *Radio* :
  - **Controlling** = `Ok to move * RadioDroit% [%]`
- Lit : ``, `Command State`, `Joystick_Right_DMAC`, `Ok to move`, `RadioDroit%`
- Utilisé par : `Joystick Zero`, `Manip Droit CanOut`
- Ligne export : 677 · id 6678

#### Joystick Zero  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Math Droit [%] = 0) AND (Math Gauche [%] = 0)`
- Lit : ``, `Math Droit`, `Math Gauche`
- Utilisé par : `Stop To Move`
- Ligne export : 766 · id 59497

#### Stop To Move  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Drive Type
- Fonction *Thermique* : (vide)
- Fonction *Electric* :
  - **Activating** = `Joystick Zero`
  - **Blocking** = `not(ENGINE RUN)`
- Lit : ``, `Drive Type`, `ENGINE RUN`, `Joystick Zero`
- Utilisé par : `Auto PAUSE/OFF`
- Ligne export : 820 · id 59461

#### Auto PAUSE/OFF  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=Automatic Joystick Inhibition [s]
- Logique :
  - **Decreasing** = `Stop To Move`
  - **Resetting** = `(PositiveFlank(Stop To Move)) OR (PositiveFlank(F1 - START PAGE))`
- Lit : ``, `Automatic Joystick Inhibition`, `F1 - START PAGE`, `Stop To Move`
- Utilisé par : `ALL ASK STOP`
- Ligne export : 895 · id 59449

#### ALL ASK STOP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `(ASK STOP) OR (PositiveFlank((Auto PAUSE/OFF [s] <= 0)))`
- Fonction *Radio* :
  - **Activating** = `(ASK STOP) OR RadioStopInter`
- Lit : ``, `ASK STOP`, `Auto PAUSE/OFF`, `Command State`, `RadioStopInter`
- Utilisé par : `All Ask Stop`, `F1 - START PAGE`
- Ligne export : 963 · id 6352

#### F1 - START PAGE  `VDIN`
- Propriétés : Toggle=Yes · Resetting channel=ALL ASK STOP · Store value=No
- Lit : `ALL ASK STOP`
- Utilisé par : `Auto PAUSE/OFF`, `Can Out Button F1`, `Toggle Free`, `MD3 page: BASE`
- Ligne export : 1061 · id 12773

#### Manip Gauche CanOut  `APPOUT`
- Propriétés : Input channel=Math Gauche [%] · Send method=Continuously · Transmit rate=100
- Lit : `Math Gauche`
- Utilisé par : `Left CanIn`
- Ligne export : 1072 · id 1448

#### Manip Droit CanOut  `APPOUT`
- Propriétés : Input channel=Math Droit [%] · Send method=Continuously · Transmit rate=100
- Lit : `Math Droit`
- Utilisé par : `Right CanIn`
- Ligne export : 1083 · id 1450

#### VIEW START PAGE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Unlock`
  - **Blocking** = `Lock OR (ENGINE RUN)`
- Lit : ``, `ENGINE RUN`, `Lock`, `Unlock`
- Utilisé par : `VIEW ENGINE RUN PAGE`
- Ligne export : 3428 · id 6023

#### VIEW ENGINE RUN PAGE  `IDC`
- Propriétés : Toggle=No · Delay on=10 · Delay off=0
- Logique :
  - **Activating** = `not(VIEW START PAGE)`
  - **Blocking** = `Lock`
- Lit : ``, `Lock`, `VIEW START PAGE`
- Utilisé par : *(personne)*
- Ligne export : 3485 · id 6117

#### Ko to move  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Ok to move)`
- Lit : ``, `Ok to move`
- Utilisé par : `Reset Speed`
- Ligne export : 3536 · id 6621

#### Remote Control  `DP`
- Propriétés : True text=Active · False text=Unactive · Default mode={False}
- Utilisé par : `Active le groupe: RADIO`, `Adjust group: Setup`, `Single adjust item: Remote Control`
- Ligne export : 3580 · id 9359

#### F3 Speed Fast  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `IDC Speed R`, `MD3 page: BASE`
- Ligne export : 4374 · id 17295

#### F2 Speed Slow  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `IDC Speed S`, `MD3 page: BASE`
- Ligne export : 4384 · id 17296

#### Auto Fast After Down  `DP`
- Propriétés : True text=Active · False text=No active · Default mode={False}
- Utilisé par : `Auto Fast after Down`, `Adjust group: Setup`, `Single adjust item: Auto Fast After Down`
- Ligne export : 4394 · id 23301

#### Auto Fast after Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `(PositiveFlank(TRACK DOWN)) AND (Auto Fast After Down)`
- Lit : ``, `Auto Fast After Down`, `TRACK DOWN`
- Utilisé par : `Auto Fast after Down Wait`
- Ligne export : 4407 · id 23302

#### Toggle Free  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(F4 Speed Free)`
  - **Resetting** = `(PositiveFlank(F1 - START PAGE)) OR (Toggle Free > 1)`
- Lit : ``, `F1 - START PAGE`, `F4 Speed Free`
- Utilisé par : `IDC Speed Free`
- Ligne export : 4458 · id 35653

#### IDC Speed Free  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Toggle Free`
- Lit : ``, `Toggle Free`
- Utilisé par : `Free Input`, `IDC Speed Free`
- Ligne export : 4527 · id 17299

#### Auto Fast after Down Wait  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `NegativeFlank(Auto Fast after Down)`
- Lit : ``, `Auto Fast after Down`
- Utilisé par : `IDC Speed R`
- Ligne export : 4570 · id 63071

#### IDC Speed R  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `(F3 Speed Fast) OR (Auto Fast after Down Wait)`
- Fonction *Radio* :
  - **Activating** = `2 = RadioSpeed`
- Lit : ``, `Auto Fast after Down Wait`, `Command State`, `F3 Speed Fast`, `RadioSpeed`
- Utilisé par : `IDC Speed R Wait`, `Speed State`
- Ligne export : 4614 · id 17355

#### IDC Speed S  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `F2 Speed Slow`
- Fonction *Radio* :
  - **Activating** = `1 = RadioSpeed`
- Lit : ``, `Command State`, `F2 Speed Slow`, `RadioSpeed`
- Utilisé par : `IDC Speed S Wait`, `Speed State`
- Ligne export : 4697 · id 17391

#### IDC Speed S Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1500 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `IDC Speed S`
- Fonction *Radio* : (vide)
- Lit : ``, `Command State`, `IDC Speed S`
- Utilisé par : `Speed State`
- Ligne export : 4773 · id 23180

#### IDC Speed R Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1500 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `IDC Speed R`
- Fonction *Radio* : (vide)
- Lit : ``, `Command State`, `IDC Speed R`
- Utilisé par : `Speed State`
- Ligne export : 4840 · id 23215

#### Reset Speed  `IDC`
- Propriétés : Toggle=No · Delay on=100 · Delay off=0
- Logique :
  - **Activating** = `Ko to move`
- Lit : ``, `Ko to move`
- Utilisé par : `Speed State`
- Ligne export : 4907 · id 23250

#### Speed State  `FSM`
- Propriétés : Store value=No · Resetting channel=Reset Speed
- État 0 **Parking**
  - transition *Push Slow Or Start* (état cible non exporté par IQANdesign)
    - **Activating** = `(PositiveFlank(IDC Speed S)) OR (PositiveFlank(ENGINE RUN)) OR (PositiveFlank(Ok to move))`
  - transition *Push Fast* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed R)`
- État 1 **Slow**
  - transition *Stay Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed S Wait)`
  - transition *Push Road* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed R)`
- État 2 **Super Slow**
  - transition *Push Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed S)`
  - transition *Push Road* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed R)`
- État 3 **Fast**
  - transition *Stay Road And Allow Cruise* (état cible non exporté par IQANdesign)
    - **Activating** = `(PositiveFlank(IDC Speed R Wait)) and Allow Cruise`
  - transition *Push Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed S)`
- État 4 **Road Cruise Ask**
  - transition *Push Road* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed R)`
  - transition *Push Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed S)`
  - transition *Ok To Road Cruise* (état cible non exporté par IQANdesign)
    - **Activating** = `Allow Run Cruise`
- État 5 **Road Cruise**
  - transition *Stop or Push Road* (état cible non exporté par IQANdesign)
    - **Activating** = `(Stop Cruise) OR (PositiveFlank(IDC Speed R))`
  - transition *Push Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed S)`
- Lit : ``, `Allow Cruise`, `Allow Run Cruise`, `ENGINE RUN`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `Ok to move`, `Reset Speed`, `Stop Cruise`
- Utilisé par : `Auto Stop Timer`, `Bip`, `Speed Input`
- Ligne export : 4950 · id 23130

#### Auto Stop Timer  `IP`
- Propriétés : Unit=s · Default mode={15}
- Utilisé par : `Auto Off Bip`, `Auto Stop Timer`, `Stop Cruise`, `Adjust group: Master Tracks`, `Single adjust item: Auto Stop Timer`
- Ligne export : 5411 · id 23964

#### Auto Stop Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=Auto Stop Timer [s]
- Logique :
  - **Decreasing** = `Speed State = 5`
  - **Resetting** = `(Joystick_Right_DMAC [%] > 0) OR (Joystick_Left_DMAC [%] > 0) OR (PositiveFlank((Speed State = 5)))`
- Lit : ``, `Auto Stop Timer`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Speed State`
- Utilisé par : `Auto Off Bip`, `Stop Cruise`, `Adjust group: Master Tracks`, `Single adjust item: Auto Stop Timer`
- Ligne export : 5423 · id 23950

#### Stop Cruise  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Joystick_Right_DMAC [%] < (Joytsick_Neutral_Minus [%] * 2)) OR (Joystick_Left_DMAC [%] < (Joytsick_Neutral_Minus [%] * 2)) OR (Auto Stop Timer [s] <= 0)`
- Lit : ``, `Auto Stop Timer`, `C`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`, `Joytsick_Neutral_Minus`
- Utilisé par : `Speed State`
- Ligne export : 5512 · id 23742

#### Cruise Control  `DP`
- Propriétés : True text=Active · False text=No active · Default mode={False}
- Utilisé par : `Allow Cruise`, `Allow Run Cruise`, `Adjust group: Setup`, `Single adjust item: Cruise Control`
- Ligne export : 5584 · id 24101

#### Allow Run Cruise  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Joystick_Right_DMAC [%] > 90) AND (Joystick_Left_DMAC [%] > 90)`
  - **Blocking** = `not(Cruise Control)`
- Lit : ``, `Cruise Control`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`
- Utilisé par : `Speed State`
- Ligne export : 5597 · id 23758

#### Allow Cruise  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Joystick_Right_DMAC [%] = 0) AND (Joystick_Left_DMAC [%] = 0)`
  - **Blocking** = `not(Cruise Control)`
- Lit : ``, `Cruise Control`, `Joystick_Left_DMAC`, `Joystick_Right_DMAC`
- Utilisé par : `Speed State`
- Ligne export : 5659 · id 23800

#### Auto Off Bip  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Auto Stop Timer [s] < 5`
- Lit : ``, `Auto Stop Timer`
- Utilisé par : `Bip`
- Ligne export : 5721 · id 23986

#### Bip  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((Speed State = 4))) OR (PositiveFlank((Speed State = 5))) OR (PositiveFlank(Auto Off Bip))`
- Lit : ``, `Auto Off Bip`, `Speed State`
- Utilisé par : `OK Buz`
- Ligne export : 5766 · id 23779

#### Engine hours  `TMR`
- Propriétés : Type (Unit)=Hours [h] · Store value=Yes · Reset value=10
- Logique :
  - **Decreasing** = `ENGINE RUN`
  - **Resetting** = `Engine hours [h] <= 0`
- Lit : ``, `ENGINE RUN`
- Utilisé par : `10 hours check-up`
- Ligne export : 6269 · id 9957

#### 10 hours check-up  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header=10 hours check-up · Text=Arrange an apointement with your service center.
- Logique :
  - **Showing** = `Engine hours [h] <= 0`
- Lit : ``, `Engine hours`
- Utilisé par : `Event log: Check UP`
- Ligne export : 6330 · id 9975

#### Iguana PIN  `PCC`
- Propriétés : Show message=All · Text=Iguana PIN  · PIN code=4158
- Lit : ``
- Utilisé par : `Adjust group: Master Battery`, `Adjust group: Master Charger`, `Adjust group: Master Config`, `Adjust group: Master Electric`, `Adjust group: Master Features`, `Adjust group: Master Pump`, `Adjust group: Master Thermic`, `Adjust group: Master Tracks`
- Ligne export : 6378 · id 11100

#### Can Out Button F1  `APPOUT`
- Propriétés : Input channel=F1 - START PAGE · Send method=On change · Transmit rate=1000
- Lit : `F1 - START PAGE`
- Utilisé par : `MD3_Start/Stop`
- Ligne export : 6415 · id 12678
