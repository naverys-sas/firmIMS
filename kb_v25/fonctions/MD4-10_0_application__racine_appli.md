# MD4-10[0] application — (racine appli)

56 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## (racine)

#### Tracks Button  `VDIN`
- Propriétés : Toggle=Yes · Resetting channel=Stop Engine Flank · Store value=No
- Lit : `Stop Engine Flank`
- Utilisé par : `Auto Light and Start`, `Auto Off - Timer`, `KTB K11 IDC - SearchLight`, `Ladder is not up`, `Reset Free Button`, `Start Button`, `Trim Mode`, `MD4-10 page: MAIN`
- Ligne export : 53 · id 48801

#### Auto PAUSE/OFF  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=Automatic Joystick Inhibition [s]
- Logique :
  - **Decreasing** = `Stop To Move`
  - **Resetting** = `PositiveFlank(Stop To Move)`
- Lit : `Automatic Joystick Inhibition`, `Stop To Move`
- Utilisé par : `Start Button`
- Ligne export : 64 · id 48913

#### Start Button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Start Button) OR (PositiveFlank(Tracks Button)) OR PositiveFlank(RadioStartInter)`
  - **Blocking** = `PositiveFlank(RadioStopInter) OR (NegativeFlank(Tracks Button)) OR (PositiveFlank((Auto PAUSE/OFF [s] <= 0)))`
- Lit : `Auto PAUSE/OFF`, `C`, `RadioStartInter`, `RadioStopInter`, `Start Button`, `Tracks Button`
- Utilisé par : `Start Button`, `Start Button MD4`, `Stop Engine Flank`
- Ligne export : 124 · id 41806

#### Stop Engine Flank  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank(Start Button)`
- Lit : `Start Button`
- Utilisé par : `Tracks Button`
- Ligne export : 216 · id 48802

#### Automatic Joystick Inhibition  `IP`
- Propriétés : Unit=s · Default mode={300}
- Utilisé par : `Auto PAUSE/OFF`, `Adjust group: Main Setup`, `Single adjust item: Automatic Joystick Inhibition`
- Ligne export : 260 · id 48901

#### Engine READY  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `CAN Engine Ready`
- Lit : `CAN Engine Ready`
- Utilisé par : `Engine READY`, `Ok to move`, `Stop To Move`
- Ligne export : 272 · id 75707

#### Stop To Move  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Joystick to zero`
  - **Blocking** = `not(Engine READY)`
- Lit : `Engine READY`, `Joystick to zero`
- Utilisé par : `Auto PAUSE/OFF`
- Ligne export : 315 · id 48902

#### Neutral Joystick  `FP`
- Propriétés : Unit=% · Default mode={10}
- Utilisé par : `Point mort Manip +`, `Point mort Manip -`, `Adjust group: Main Setup`, `Single adjust item: Neutral Joystick`
- Ligne export : 366 · id 52817

#### Point mort Manip -  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `Neutral Joystick [%] * -1`
- Lit : `Neutral Joystick`
- Utilisé par : `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`, `Stop Cruise`
- Ligne export : 378 · id 52826

#### Left Joystick  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-LST · Calibration={500; 4500; -100; 100} · Alarms={No; 0; No; 100} · Module=MD4-10[0] · Module index=0
- Utilisé par : `DMAC EV Pompe 2 Gauche`, `Adjust group: Master Drive`, `Dual adjust item: Left Joystick`, `Measure group: Motor Left`
- Ligne export : 422 · id 41220

#### Point mort Manip +  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `Neutral Joystick [%]`
- Lit : `Neutral Joystick`
- Utilisé par : `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`
- Ligne export : 446 · id 52818

#### DMAC EV Pompe 2 Gauche  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `courbe(Left Joystick [%]: {{-95; -100}; {Point mort Manip - [%]; 0}; {Point mort Manip + [%]; 0}; {95; 100}}, Freeze)`
- Lit : `Left Joystick`, `Point mort Manip +`, `Point mort Manip -`
- Utilisé par : `Allow Cruise`, `Allow Run Cruise`, `Auto Stop Timer`, `Math Gauche`, `Stop Cruise`
- Ligne export : 488 · id 52834

#### Right Joystick  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-LST · Calibration={500; 4500; -100; 100} · Alarms={No; 0; No; 100} · Module=MD4-10[0] · Module index=1
- Utilisé par : `DMAC EV Pompe 1 Droite`, `Adjust group: Master Drive`, `Dual adjust item: Right Joystick`, `Measure group: Motor Right`
- Ligne export : 552 · id 41221

#### DMAC EV Pompe 1 Droite  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `courbe(Right Joystick [%]: {{-95; -100}; {Point mort Manip - [%]; 0}; {Point mort Manip + [%]; 0}; {95; 100}}, Freeze)`
- Lit : `Point mort Manip +`, `Point mort Manip -`, `Right Joystick`
- Utilisé par : `Allow Cruise`, `Allow Run Cruise`, `Auto Stop Timer`, `Math Droit`, `Stop Cruise`
- Ligne export : 576 · id 52844

#### Stop Cruise  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(DMAC EV Pompe 1 Droite [%] < (Point mort Manip - [%] * 2)) OR (DMAC EV Pompe 2 Gauche [%] < (Point mort Manip - [%] * 2)) OR (Auto Stop Timer [s] <= 0)`
- Lit : `Auto Stop Timer`, `C`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`, `Point mort Manip -`
- Utilisé par : `Speed`
- Ligne export : 640 · id 52870

#### Ok to move  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Engine READY) AND (TRACK DOWN or Re-Track mode in water)`
- Lit : `C`, `Engine READY`, `Re-Track mode in water`, `TRACK DOWN`
- Utilisé par : `Ko to move`, `Math Droit`, `Math Gauche`, `Speed`
- Ligne export : 712 · id 41209

#### Auto Fast after Down IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `(PositiveFlank(TRACK DOWN)) AND (Auto Fast After Down)`
- Lit : `Auto Fast After Down`, `TRACK DOWN`
- Utilisé par : `IDC Speed R`, `Speed`
- Ligne export : 778 · id 52882

#### IDC Speed R  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `(F3 Speed Fast) OR (Auto Fast after Down IDC)`
- Fonction *Radio* :
  - **Activating** = `2 = RadioSpeed`
- Lit : `Auto Fast after Down IDC`, `Command State`, `F3 Speed Fast`, `RadioSpeed`
- Utilisé par : `IDC Speed R Wait`, `Speed`
- Ligne export : 829 · id 52900

#### IDC Speed S  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `F2 Speed Slow`
- Fonction *Radio* :
  - **Activating** = `1 = RadioSpeed`
- Lit : `Command State`, `F2 Speed Slow`, `RadioSpeed`
- Utilisé par : `IDC Speed S Wait`, `Speed`
- Ligne export : 912 · id 52908

#### IDC Speed S Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1500 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `IDC Speed S`
- Fonction *Radio* : (vide)
- Lit : `Command State`, `IDC Speed S`
- Utilisé par : `Speed`
- Ligne export : 988 · id 52916

#### IDC Speed R Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1500 · Delay off=0 · Function selector=Command State
- Fonction *Normal* :
  - **Activating** = `IDC Speed R`
- Fonction *Radio* : (vide)
- Lit : `Command State`, `IDC Speed R`
- Utilisé par : `Speed`
- Ligne export : 1055 · id 52924

#### Allow Run Cruise  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(DMAC EV Pompe 1 Droite [%] > 90) AND (DMAC EV Pompe 2 Gauche [%] > 90)`
  - **Blocking** = `not(Cruise Control)`
- Lit : `Cruise Control`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`
- Utilisé par : `Speed`
- Ligne export : 1122 · id 52933

#### Allow Cruise  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(DMAC EV Pompe 1 Droite [%] = 0) AND (DMAC EV Pompe 2 Gauche [%] = 0)`
  - **Blocking** = `not(Cruise Control)`
- Lit : `Cruise Control`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`
- Utilisé par : `Speed`
- Ligne export : 1184 · id 52943

#### Reset Speed  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Ko to move`
- Lit : `Ko to move`
- Utilisé par : `Speed`
- Ligne export : 1246 · id 52953

#### Speed  `FSM`
- Propriétés : Store value=No · Resetting channel=Reset Speed
- État 0 **Parking**
  - transition *Push Slow Or Start* (état cible non exporté par IQANdesign)
    - **Activating** = `(PositiveFlank(IDC Speed S)) OR (Ok to move)`
  - transition *Push Road* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed R)`
- État 1 **Slow**
  - transition *Stay Slow* (état cible non exporté par IQANdesign)
    - **Activating** = `PositiveFlank(IDC Speed S Wait)`
  - transition *Push Road or Auto Fast after Down* (état cible non exporté par IQANdesign)
    - **Activating** = `(PositiveFlank(IDC Speed R)) OR (Auto Fast after Down IDC)`
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
- Lit : `Allow Cruise`, `Allow Run Cruise`, `Auto Fast after Down IDC`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `Ok to move`, `Reset Speed`, `Stop Cruise`
- Utilisé par : `Auto Stop Timer`, `Bip Road Cruise`, `Speed output`, `Adjust group: Master Track`
- Ligne export : 1289 · id 52961

#### Auto Stop Timer  `IP`
- Propriétés : Unit=s · Default mode={15}
- Utilisé par : `Auto Off Bip`, `Auto Stop Timer`, `Stop Cruise`, `Single adjust item: Dead Man Timer Cruise Control`
- Ligne export : 1748 · id 53102

#### Auto Stop Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=Auto Stop Timer [s]
- Logique :
  - **Decreasing** = `Speed = 5`
  - **Resetting** = `(DMAC EV Pompe 1 Droite [%] > 0) OR (DMAC EV Pompe 2 Gauche [%] > 0) OR (PositiveFlank((Speed = 5)))`
- Lit : `Auto Stop Timer`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`, `Speed`
- Utilisé par : `Auto Off Bip`, `Stop Cruise`, `Single adjust item: Dead Man Timer Cruise Control`
- Ligne export : 1760 · id 52856

#### Enable Tracks with Arms Up?  `DP`
- Propriétés : True text=ACTIVE · False text=NO ACTIVE · Default mode={False}
- Utilisé par : `Re-Track mode in water`
- Ligne export : 1849 · id 41191

#### Reset on startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset on startup`
- Utilisé par : `Re-Track mode in water`
- Ligne export : 1862 · id 41192

#### Re-Track mode in water  `MEM`
- Propriétés : Input channel=Enable Tracks with Arms Up? · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Resetting** = `Reset on startup`
- Lit : `Enable Tracks with Arms Up?`, `Reset on startup`
- Utilisé par : `Ok to move`, `Adjust group: Maintenance`, `Single adjust item: Re-Track mode in water`
- Ligne export : 1912 · id 41201

#### Auto Fast After Down  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Auto Fast after Down IDC`, `Adjust group: Main Setup`, `Single adjust item: Auto Fast After Down`
- Ligne export : 1956 · id 52881

#### F3 Speed Fast  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `IDC Speed R`, `MD4-10 page: MAIN`
- Ligne export : 1969 · id 52854

#### F2 Speed Slow  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `IDC Speed S`, `MD4-10 page: MAIN`
- Ligne export : 1979 · id 52855

#### Cruise Control  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Allow Cruise`, `Allow Run Cruise`, `Adjust group: Main Setup`, `Adjust group: Master Drive`, `Single adjust item: Cruise Control`
- Ligne export : 1989 · id 52932

#### Ko to move  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Ok to move)`
- Lit : `Ok to move`
- Utilisé par : `Reset Speed`
- Ligne export : 2002 · id 41463

#### Reset Free Button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank(Tracks Button)`
- Lit : `Tracks Button`
- Utilisé par : `F4 Free`
- Ligne export : 2046 · id 56187

#### F4 Free  `VDIN`
- Propriétés : Toggle=Yes · Resetting channel=Reset Free Button · Store value=No
- Lit : `Reset Free Button`
- Utilisé par : `F4 Free output`, `MD4-10 page: MAIN`
- Ligne export : 2090 · id 52815

#### Math Gauche  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Command State
- Fonction *Normal* :
  - **Controlling** = `DMAC EV Pompe 2 Gauche [%]`
- Fonction *Radio* :
  - **Controlling** = `Ok to move * RadioGauche% [%]`
- Lit : `Command State`, `DMAC EV Pompe 2 Gauche`, `Ok to move`, `RadioGauche%`
- Utilisé par : `Left Joystick`
- Ligne export : 2442 · id 41222

#### Math Droit  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Command State
- Fonction *Normal* :
  - **Controlling** = `DMAC EV Pompe 1 Droite [%]`
- Fonction *Radio* :
  - **Controlling** = `Ok to move * RadioDroit% [%]`
- Lit : `Command State`, `DMAC EV Pompe 1 Droite`, `Ok to move`, `RadioDroit%`
- Utilisé par : `Right Joystick`
- Ligne export : 2531 · id 41240

#### Remote Control  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Active le groupe: iPhone`, `Adjust group: Main Setup`, `Single adjust item: Wifi Remote Control`
- Ligne export : 3868 · id 41471

#### Auto Off Bip  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Auto Stop Timer [s] < 5`
- Lit : `Auto Stop Timer`
- Utilisé par : `Bip Road Cruise`
- Ligne export : 4651 · id 53103

#### Bip Road Cruise  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((Speed = 4))) OR (PositiveFlank((Speed = 5))) OR (PositiveFlank(Auto Off Bip))`
- Lit : `Auto Off Bip`, `Speed`
- Utilisé par : `OK Buz`
- Ligne export : 4696 · id 53111

#### Setup PIN  `PCC`
- Propriétés : Show message=All · Text=Setup PIN  · PIN code=1122
- Utilisé par : *(personne)*
- Ligne export : 5445 · id 41792

#### Iguana PIN  `PCC`
- Propriétés : Show message=All · Text=Iguana PIN  · PIN code=4158
- Utilisé par : `Adjust group: Config Electric Drive`, `Adjust group: Config GPS`, `Adjust group: Config Options`, `Adjust group: Config Outboard`, `Adjust group: Master A/C Bat Pack`, `Adjust group: Master Battery`, `Adjust group: Master Cooling`, `Adjust group: Master Drive`, `Adjust group: Master Features`, `Adjust group: Master Setup`, `Adjust group: Master Track`
- Ligne export : 5482 · id 41799

#### Cycle utilization  `SIC`
- Propriétés : Value=Cycle utilization [%]
- Utilisé par : *(personne)*
- Ligne export : 5519 · id 42079

#### Status:G1x  `MDGN`
- Propriétés : Value=Module status · Module=G1x · Module index=0
- Utilisé par : *(personne)*
- Ligne export : 20650 · id 44042

#### Network state:G1x  `MDGN`
- Propriétés : Value=Network state · Module=G1x · Module index=1
- Utilisé par : *(personne)*
- Ligne export : 20661 · id 44043

#### S/N:MD4-10[0]  `MDGN`
- Propriétés : Value=Serial number · Module=MD4-10[0] · Module index=1
- Utilisé par : *(personne)*
- Ligne export : 21929 · id 47903

#### Temp:MD4-10[0]  `MDGN`
- Propriétés : Value=Temperature [Â°C] · Module=MD4-10[0] · Module index=2
- Lit : `C`
- Utilisé par : *(personne)*
- Ligne export : 21940 · id 47904

#### Address:MD4-10[0]  `MDGN`
- Propriétés : Value=Id tag · Module=MD4-10[0] · Module index=3
- Utilisé par : *(personne)*
- Ligne export : 21951 · id 47905

#### +BAT:MD4-10[0]  `MDGN`
- Propriétés : Value=Supply voltage [V] · Module=MD4-10[0] · Module index=4
- Utilisé par : `MD4-10 page: BASE`
- Ligne export : 21962 · id 47906

#### VREF:MD4-10[0]  `MDGN`
- Propriétés : Value=Reference voltage [V] · Module=MD4-10[0] · Module index=5
- Utilisé par : *(personne)*
- Ligne export : 21973 · id 47907

#### Project version  `SIC`
- Propriétés : Value=Project version
- Utilisé par : `MD4-10 page: SHUTDOWN`, `MD4-10 page: STARTUP`
- Ligne export : 23811 · id 53617

#### Right Joystick  `APPOUT`
- Propriétés : Input channel=Math Droit [%] · Send method=Continuously · Transmit rate=100
- Lit : `Math Droit`
- Utilisé par : `DMAC EV Pompe 1 Droite`, `Adjust group: Master Drive`, `Dual adjust item: Right Joystick`, `Measure group: Motor Right`
- Ligne export : 30646 · id 77876

#### Left Joystick  `APPOUT`
- Propriétés : Input channel=Math Gauche [%] · Send method=Continuously · Transmit rate=100
- Lit : `Math Gauche`
- Utilisé par : `DMAC EV Pompe 2 Gauche`, `Adjust group: Master Drive`, `Dual adjust item: Left Joystick`, `Measure group: Motor Left`
- Ligne export : 30657 · id 77878

#### Start Button  `APPOUT`
- Propriétés : Input channel=Start Button · Send method=On change · Transmit rate=1000
- Lit : `Start Button`
- Utilisé par : `Start Button`, `Start Button MD4`, `Stop Engine Flank`
- Ligne export : 30668 · id 77885
