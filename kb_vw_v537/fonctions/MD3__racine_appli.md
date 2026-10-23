# MD3 — (racine appli)

61 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## (racine)

#### MDGN-VREF:MD3-0  `MDGN`
- Propriétés : Value=Reference voltage [V] · Module=MD3[0] · Module index=4
- Utilisé par : *(personne)*
- Ligne export : 38 · id 1040

#### MDGN-+BAT:MD3-0  `MDGN`
- Propriétés : Value=Supply voltage [V] · Module=MD3[0] · Module index=3
- Utilisé par : *(personne)*
- Ligne export : 49 · id 1041

#### MDGN-Temp:MD3-0  `MDGN`
- Propriétés : Value=Temperature [°C] · Module=MD3[0] · Module index=2
- Lit : `C`
- Utilisé par : *(personne)*
- Ligne export : 60 · id 1042

#### F4 Speed Free  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Toggle Free`, `MD3 page: ENGINE PAGE`
- Ligne export : 71 · id 1189

#### ALL ASK STOP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `ASK STOP`
- Fonction *Radio* :
  - **Activating** = `(ASK STOP) OR RadioStopInter`
- Lit : ``, `ASK STOP`, `Command State`, `RadioStopInter`
- Utilisé par : `All Ask Stop`, `F1 START PAGE`
- Ligne export : 81 · id 6352

#### CAN - ENGINE RUN - Out  `APPIN`
- Propriétés : Input channel=CAN - ENGINE RUN
- Lit : `CAN - ENGINE RUN`
- Utilisé par : `CAN - Engine Ready`, `Engine hours`, `Ok to move`, `Run Engine Statut`, `Speed`, `VIEW ENGINE RUN PAGE`
- Ligne export : 162 · id 6053

#### Re-Track mode in water  `DP`
- Propriétés : True text=ACTIVE · False text=NO ACTIVE · Default mode={False}
- Utilisé par : `Ok to move`, `Re-Track mode in water`, `Adjust group: Maintenance`, `Single adjust item: Re-Track mode in water`
- Ligne export : 171 · id 22278

#### Reset on startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset on startup`
- Lit : ``
- Utilisé par : `Re-Track mode in water`
- Ligne export : 184 · id 22290

#### Re-Track mode in water  `MEM`
- Propriétés : Input channel=Re-Track mode in water · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Resetting** = `Reset on startup`
- Lit : ``, `Re-Track mode in water`, `Reset on startup`
- Utilisé par : `Ok to move`, `Adjust group: Maintenance`, `Single adjust item: Re-Track mode in water`
- Ligne export : 234 · id 22279

#### Ok to move  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(CAN - ENGINE RUN - Out) AND (TRACK DOWN or Re-Track mode in water)`
- Lit : ``, `C`, `CAN - ENGINE RUN - Out`, `Re-Track mode in water`, `TRACK DOWN`
- Utilisé par : `Ko to move`, `Math Droit`, `Math Gauche`, `Speed`
- Ligne export : 278 · id 6388

#### Left Joystick  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-LST · Calibration={500; 4500; -100; 100} · Alarms={No; 0; No; 100} · Module=MD3[0] · Module index=0
- Utilisé par : `DMAC EV Pompe 2 Gauche`, `Adjust group: Master Pump`, `Dual adjust item: Left Joystick`, `Measure group: Translation`
- Ligne export : 344 · id 1004

#### Right Joystick  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-LST · Calibration={500; 4500; -100; 100} · Alarms={No; 0; No; 100} · Module=MD3[0] · Module index=1
- Utilisé par : `DMAC EV Pompe 1 Droite`, `Adjust group: Master Pump`, `Dual adjust item: Right Joystick`, `Measure group: Translation`
- Ligne export : 368 · id 1065

#### Neutral Joystick  `FP`
- Propriétés : Unit=% · Default mode={10}
- Utilisé par : `Point mort Manip +`, `Point mort Manip -`, `Adjust group: Setup`, `Single adjust item: Neutral Joystick`
- Ligne export : 392 · id 23852

#### Point mort Manip +  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `Neutral Joystick [%]`
- Lit : ``, `Neutral Joystick`
- Utilisé par : `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`
- Ligne export : 404 · id 23853

#### Point mort Manip -  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `Neutral Joystick [%] * -1`
- Lit : ``, `Neutral Joystick`
- Utilisé par : `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`, `Stop Cruise`
- Ligne export : 446 · id 23861

#### DMAC EV Pompe 2 Gauche  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `courbe(Left Joystick [%]: {{-100; -100}; {Point mort Manip - [%]; 0}; {Point mort Manip + [%]; 0}; {100; 100}}, Freeze)`
- Lit : ``, `Left Joystick`, `Point mort Manip +`, `Point mort Manip -`
- Utilisé par : `Allow Cruise`, `Allow Run Cruise`, `Auto Stop Timer`, `Math Gauche`, `Stop Cruise`
- Ligne export : 490 · id 23869

#### Math Gauche  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Command State
- Fonction *Normal* :
  - **Controlling** = `MaxOf (Absolute)(DMAC EV Pompe 2 Gauche [%], 100 * 3 - Forward, -100 * 4 - Backward)`
- Fonction *Radio* :
  - **Controlling** = `Ok to move * RadioGauche% [%]`
- Lit : ``, `3 - Forward`, `4 - Backward`, `Command State`, `DMAC EV Pompe 2 Gauche`, `Ok to move`, `RadioGauche%`
- Utilisé par : `Manip Gauche CanOut`
- Ligne export : 554 · id 6654

#### Manip Gauche CanOut  `APPOUT`
- Propriétés : Input channel=Math Gauche [%] · Send method=Continuously · Transmit rate=Every cycle
- Lit : `Math Gauche`
- Utilisé par : `Left CanIn`
- Ligne export : 661 · id 1448

#### DMAC EV Pompe 1 Droite  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `courbe(Right Joystick [%]: {{-100; -100}; {Point mort Manip - [%]; 0}; {Point mort Manip + [%]; 0}; {100; 100}}, Freeze)`
- Lit : ``, `Point mort Manip +`, `Point mort Manip -`, `Right Joystick`
- Utilisé par : `Allow Cruise`, `Allow Run Cruise`, `Auto Stop Timer`, `Math Droit`, `Stop Cruise`
- Ligne export : 672 · id 23880

#### Math Droit  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Command State
- Fonction *Normal* :
  - **Controlling** = `MaxOf (Absolute)(DMAC EV Pompe 1 Droite [%], 100 * 3 - Forward, -100 * 4 - Backward)`
- Fonction *Radio* :
  - **Controlling** = `Ok to move * RadioDroit% [%]`
- Lit : ``, `3 - Forward`, `4 - Backward`, `Command State`, `DMAC EV Pompe 1 Droite`, `Ok to move`, `RadioDroit%`
- Utilisé par : `Manip Droit CanOut`
- Ligne export : 736 · id 6678

#### Manip Droit CanOut  `APPOUT`
- Propriétés : Input channel=Math Droit [%] · Send method=Continuously · Transmit rate=Every cycle
- Lit : `Math Droit`
- Utilisé par : `Right CanIn`
- Ligne export : 843 · id 1450

#### VIEW ENGINE RUN PAGE  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `CAN - ENGINE RUN - Out`
- Lit : ``, `CAN - ENGINE RUN - Out`
- Utilisé par : `VIEW START PAGE`
- Ligne export : 3945 · id 6117

#### VIEW START PAGE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(VIEW ENGINE RUN PAGE)`
- Lit : ``, `VIEW ENGINE RUN PAGE`
- Utilisé par : *(personne)*
- Ligne export : 3988 · id 6023

#### Ko to move  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Ok to move)`
- Lit : ``, `Ok to move`
- Utilisé par : `Reset Speed`
- Ligne export : 4032 · id 6621

#### Remote Control  `DP`
- Propriétés : True text=Active · False text=Unactive · Default mode={False}
- Utilisé par : `Active le groupe: RADIO`, `Adjust group: Setup`, `Single adjust item: Remote Control`
- Ligne export : 4076 · id 9359

#### F3 Speed Fast  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `IDC Speed Fast`, `MD3 page: ENGINE PAGE`
- Ligne export : 4882 · id 17295

#### F2 Speed Slow  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `IDC Speed Slow`, `MD3 page: ENGINE PAGE`
- Ligne export : 4892 · id 17296

#### Auto Beach After Down  `DP`
- Propriétés : True text=Active · False text=No active · Default mode={False}
- Utilisé par : `Auto Beach after Down`, `Adjust group: Setup`, `Single adjust item: Auto Beach After Down`
- Ligne export : 4902 · id 23301

#### Auto Beach after Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `(PositiveFlank(TRACK DOWN)) AND (Auto Beach After Down)`
- Lit : ``, `Auto Beach After Down`, `TRACK DOWN`
- Utilisé par : `IDC Speed Fast`
- Ligne export : 4915 · id 23302

#### F1 START PAGE  `VDIN`
- Propriétés : Toggle=Yes · Resetting channel=ALL ASK STOP · Store value=No
- Lit : `ALL ASK STOP`
- Utilisé par : `F1 - Button`, `Toggle Free`, `MD3 page: ENGINE PAGE`
- Ligne export : 4966 · id 12773

#### Toggle Free  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(F4 Speed Free)`
  - **Resetting** = `(PositiveFlank(F1 START PAGE)) OR (Toggle Free > 1)`
- Lit : ``, `F1 START PAGE`, `F4 Speed Free`
- Utilisé par : `IDC Speed Free`
- Ligne export : 4977 · id 25204

#### IDC Speed Free  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `Toggle Free`
- Fonction *Radio* :
  - **Blocking** = `True`
- Lit : ``, `Command State`, `Toggle Free`
- Utilisé par : `CAN  Free`
- Ligne export : 5046 · id 17299

#### IDC Speed Fast  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `(F3 Speed Fast) OR (Auto Beach after Down)`
- Fonction *Radio* :
  - **Activating** = `2 = RadioSpeed`
- Lit : ``, `Auto Beach after Down`, `Command State`, `F3 Speed Fast`, `RadioSpeed`
- Utilisé par : `IDC Speed R Wait`, `Speed`
- Ligne export : 5120 · id 17355

#### IDC Speed Slow  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `F2 Speed Slow`
- Fonction *Radio* :
  - **Activating** = `1 = RadioSpeed`
- Lit : ``, `Command State`, `F2 Speed Slow`, `RadioSpeed`
- Utilisé par : `IDC Speed S Wait`, `Speed`
- Ligne export : 5203 · id 17391

#### IDC Speed S Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1500 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `IDC Speed Slow`
- Fonction *Radio* : (vide)
- Lit : ``, `Command State`, `IDC Speed Slow`
- Utilisé par : `Speed`
- Ligne export : 5279 · id 23180

#### IDC Speed R Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1500 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `IDC Speed Fast`
- Fonction *Radio* : (vide)
- Lit : ``, `Command State`, `IDC Speed Fast`
- Utilisé par : `Speed`
- Ligne export : 5346 · id 23215

#### Reset Speed  `IDC`
- Propriétés : Toggle=No · Delay on=100 · Delay off=0
- Logique :
  - **Activating** = `Ko to move`
- Lit : ``, `Ko to move`
- Utilisé par : `Speed`
- Ligne export : 5413 · id 23250

#### Speed  `FSM`
- Propriétés : Store value=No · Resetting channel=Reset Speed
- État 0 **Parking**
  - transition *Push Slow Or Start* (état cible non exporté par IQANdesign)
    - **Activating** = `(PositiveFlank(IDC Speed Slow)) OR (PositiveFlank(CAN - ENGINE RUN - Out)) OR (PositiveFlank(Ok to move))`
  - transition *Push Road* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed Fast)`
- État 1 **Slow**
  - transition *Stay Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed S Wait)`
  - transition *Push Road* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed Fast)`
- État 2 **Super Slow**
  - transition *Push Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed Slow)`
  - transition *Push Road* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed Fast)`
- État 3 **Fast**
  - transition *Stay Road And Allow Cruise* (état cible non exporté par IQANdesign)
    - **Activating** = `(PositiveFlank(IDC Speed R Wait)) and Allow Cruise`
  - transition *Push Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed Slow)`
- État 4 **Road Cruise Ask**
  - transition *Push Road* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed Fast)`
  - transition *Push Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed Slow)`
  - transition *Ok To Road Cruise* (état cible non exporté par IQANdesign)
    - **Activating** = `Allow Run Cruise`
- État 5 **Road Cruise**
  - transition *Stop or Push Road* (état cible non exporté par IQANdesign)
    - **Activating** = `(Stop Cruise) OR (PositiveFlank(IDC Speed Fast))`
  - transition *Push Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed Slow)`
- Lit : ``, `Allow Cruise`, `Allow Run Cruise`, `CAN - ENGINE RUN - Out`, `IDC Speed Fast`, `IDC Speed R Wait`, `IDC Speed S Wait`, `IDC Speed Slow`, `Ok to move`, `Reset Speed`, `Stop Cruise`
- Utilisé par : `Auto Stop Timer`, `Bip`, `CAN  Speed`, `TSC1-A:J1939-0`, `Adjust group: `
- Ligne export : 5456 · id 23130

#### Auto Stop Timer  `IP`
- Propriétés : Unit=s · Default mode={15}
- Utilisé par : `Auto Off Bip`, `Auto Stop Timer`, `Stop Cruise`, `Adjust group: Master Tracks`, `Single adjust item: Auto Stop Timer`
- Ligne export : 5917 · id 23964

#### Auto Stop Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=Auto Stop Timer [s]
- Logique :
  - **Decreasing** = `Speed = 5`
  - **Resetting** = `(DMAC EV Pompe 1 Droite [%] > 0) OR (DMAC EV Pompe 2 Gauche [%] > 0) OR (PositiveFlank((Speed = 5)))`
- Lit : ``, `Auto Stop Timer`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`, `Speed`
- Utilisé par : `Auto Off Bip`, `Stop Cruise`, `Adjust group: Master Tracks`, `Single adjust item: Auto Stop Timer`
- Ligne export : 5929 · id 23950

#### Stop Cruise  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(DMAC EV Pompe 1 Droite [%] < (Point mort Manip - [%] * 2)) OR (DMAC EV Pompe 2 Gauche [%] < (Point mort Manip - [%] * 2)) OR (Auto Stop Timer [s] <= 0)`
- Lit : ``, `Auto Stop Timer`, `C`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`, `Point mort Manip -`
- Utilisé par : `Speed`
- Ligne export : 6018 · id 23742

#### Cruise Control  `DP`
- Propriétés : True text=Active · False text=No active · Default mode={False}
- Utilisé par : `Allow Cruise`, `Allow Run Cruise`, `Adjust group: Setup`, `Single adjust item: Cruise Control`
- Ligne export : 6090 · id 24101

#### Allow Run Cruise  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(DMAC EV Pompe 1 Droite [%] > 90) AND (DMAC EV Pompe 2 Gauche [%] > 90)`
  - **Blocking** = `not(Cruise Control)`
- Lit : ``, `Cruise Control`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`
- Utilisé par : `Speed`
- Ligne export : 6103 · id 23758

#### Allow Cruise  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(DMAC EV Pompe 1 Droite [%] = 0) AND (DMAC EV Pompe 2 Gauche [%] = 0)`
  - **Blocking** = `not(Cruise Control)`
- Lit : ``, `Cruise Control`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`
- Utilisé par : `Speed`
- Ligne export : 6165 · id 23800

#### Auto Off Bip  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Auto Stop Timer [s] < 5`
- Lit : ``, `Auto Stop Timer`
- Utilisé par : `Bip`
- Ligne export : 6227 · id 23986

#### Bip  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((Speed = 4))) OR (PositiveFlank((Speed = 5))) OR (PositiveFlank(Auto Off Bip))`
- Lit : ``, `Auto Off Bip`, `Speed`
- Utilisé par : `OK Buz`
- Ligne export : 6272 · id 23779

#### MDGN-Status:MD3[0]  `MDGN`
- Propriétés : Value=Module status · Module=MD3[0] · Module index=0
- Utilisé par : `MD3 CAN Status`
- Ligne export : 6784 · id 9628

#### MD3 CAN Status  `APPOUT`
- Propriétés : Input channel=MDGN-Status:MD3[0] · Send method=Continuously · Transmit rate=Every cycle
- Lit : `MDGN-Status:MD3[0]`
- Utilisé par : `MD3 Status CAN In`
- Ligne export : 6795 · id 9662

#### Engine hours  `TMR`
- Propriétés : Type (Unit)=Hours [h] · Store value=Yes · Reset value=10
- Logique :
  - **Decreasing** = `CAN - ENGINE RUN - Out`
  - **Resetting** = `Engine hours [h] <= 0`
- Lit : ``, `CAN - ENGINE RUN - Out`
- Utilisé par : `10 hours check-up`
- Ligne export : 6806 · id 9957

#### 10 hours check-up  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header=10 hours check-up · Text=Arrange an apointement with your service center.
- Logique :
  - **Showing** = `Engine hours [h] <= 0`
- Lit : ``, `Engine hours`
- Utilisé par : `Event log: Check UP`
- Ligne export : 6867 · id 9975

#### CAN  Speed  `APPOUT`
- Propriétés : Input channel=Speed · Send method=On change · Transmit rate=1000
- Lit : `Speed`
- Utilisé par : `CAN Speed`
- Ligne export : 6915 · id 10899

#### Security PIN  `PCC`
- Propriétés : Show message=All · Text=Security PIN · PIN code=7852
- Lit : ``
- Utilisé par : `Adjust group: Security`
- Ligne export : 6926 · id 11086

#### Setup PIN  `PCC`
- Propriétés : Show message=All · Text=Setup PIN  · PIN code=1122
- Lit : ``
- Utilisé par : *(personne)*
- Ligne export : 6963 · id 11093

#### Iguana PIN  `PCC`
- Propriétés : Show message=All · Text=Iguana PIN  · PIN code=4158
- Lit : ``
- Utilisé par : `Adjust group: Master Config`, `Adjust group: Master Engine`, `Adjust group: Master Pump`, `Adjust group: Master Setup`, `Adjust group: Master Tracks`
- Ligne export : 7000 · id 11100

#### F1 - Button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `F1 START PAGE`
- Fonction *Radio* :
  - **Activating** = `PositiveFlank(RadioStartInter) OR (F1 - Button)`
  - **Blocking** = `RadioStopInter`
- Lit : ``, `Command State`, `F1 START PAGE`, `RadioStartInter`, `RadioStopInter`
- Utilisé par : `Can Out Button State`
- Ligne export : 7037 · id 27534

#### Can Out Button State  `APPOUT`
- Propriétés : Input channel=F1 - Button · Send method=On change · Transmit rate=1000
- Lit : `F1 - Button`
- Utilisé par : `MD3 Start/Stop Button`
- Ligne export : 7126 · id 12678

#### G11 Modem  `DP`
- Propriétés : True text=ON · False text=OFF · Default mode={False}
- Utilisé par : `Adjust group: Setup`, `Measure group: G11 Modem`, `Single adjust item: G11 Modem`
- Ligne export : 8805 · id 21788

#### Status:G1x  `MDGN`
- Propriétés : Value=Module status · Module=G1x · Module index=0
- Utilisé par : `Measure group: G11 Modem`
- Ligne export : 8818 · id 21794

#### Network state:G1x  `MDGN`
- Propriétés : Value=Network state · Module=G1x · Module index=1
- Utilisé par : `Measure group: G11 Modem`
- Ligne export : 8829 · id 21795

#### Acceleration  `DP`
- Propriétés : True text=ACTIVE · False text=OFF · Default mode={False}
- Utilisé par : `Active le groupe: Acceleration`, `Adjust group: Master Config`, `Measure group: Acceleration`, `Single adjust item: Acceleration`
- Ligne export : 8840 · id 21865

#### CAN  Free  `APPOUT`
- Propriétés : Input channel=IDC Speed Free · Send method=On change · Transmit rate=1000
- Lit : `IDC Speed Free`
- Utilisé par : `CAN Free`
- Ligne export : 9103 · id 25191
