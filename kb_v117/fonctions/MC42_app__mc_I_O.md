# MC42 app — mc.I/O

50 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## mc.I/O — actif seulement si `not_a_sim`

#### EV Tension Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Drive Type mc
- Fonction *Electric* :
  - **Activating** = `E EV Tension`
- Fonction *Fossil* :
  - **Activating** = `T EV Tension`
- Lit : `Drive Type mc`, `E EV Tension`, `T EV Tension`
- Utilisé par : `EV Tension mc 58`
- Ligne export : 73651 · id 204728

#### EV Tension mc 58  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=EV Tension Sel · Module=MC42-33 (MC42[0]) · Module index=11
- Lit : `EV Tension Sel`
- Utilisé par : `Measure group: Hydraulic`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 73725 · id 128414

#### EV Lock Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Drive Type mc
- Fonction *Electric* :
  - **Activating** = `E EV Lock`
- Fonction *Fossil* :
  - **Activating** = `T EV Lock`
- Lit : `Drive Type mc`, `E EV Lock`, `T EV Lock`
- Utilisé par : `EV lock mc 59`
- Ligne export : 73738 · id 204660

#### EV lock mc 59  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=EV Lock Sel · Module=MC42-33 (MC42[0]) · Module index=13
- Lit : `13`, `EV Lock Sel`
- Utilisé par : `E Inter EV By Pass`, `Measure group: Hydraulic`
- Ligne export : 73812 · id 128415

#### EV Up Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Drive Type mc
- Fonction *Electric* :
  - **Activating** = `E EV Up`
- Fonction *Fossil* :
  - **Activating** = `T EV Up`
- Lit : `Drive Type mc`, `E EV Up`, `T EV Up`
- Utilisé par : `EV Up mc 57`
- Ligne export : 73825 · id 204603

#### EV Up mc 57  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=EV Up Sel · Module=MC42-33 (MC42[0]) · Module index=9
- Lit : `EV Up Sel`
- Utilisé par : `Measure group: Hydraulic`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 73899 · id 128434

#### EV Down Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Drive Type mc
- Fonction *Electric* :
  - **Activating** = `E EV Down`
- Fonction *Fossil* :
  - **Activating** = `T EV Down`
- Lit : `Drive Type mc`, `E EV Down`, `T EV Down`
- Utilisé par : `EV Down mc 42`
- Ligne export : 73912 · id 204626

#### EV Down mc 42  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=EV Down Sel · Module=MC42-33 (MC42[0]) · Module index=10
- Lit : `EV Down Sel`
- Utilisé par : `Measure group: Hydraulic`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 73986 · id 128444

#### EV By pass Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Drive Type mc
- Fonction *Electric* :
  - **Activating** = `E EV By pass`
- Fonction *Fossil* :
  - **Activating** = `T EV By pass`
- Lit : `Drive Type mc`, `E EV By pass`, `T EV By pass`
- Utilisé par : `EV By pass mc 41`
- Ligne export : 73999 · id 204694

#### EV By pass mc 41  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=EV By pass Sel · Module=MC42-33 (MC42[0]) · Module index=8
- Lit : `EV By pass Sel`
- Utilisé par : `Measure group: Hydraulic`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 74073 · id 128481

#### EV UnBlock Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Drive Type mc
- Fonction *Electric* :
  - **Activating** = `E EV UnBlock`
- Fonction *Fossil* :
  - **Activating** = `T EV UnBlock`
- Lit : `Drive Type mc`, `E EV UnBlock`, `T EV UnBlock`
- Utilisé par : `EV unlock mc 43`
- Ligne export : 74086 · id 204762

#### EV unlock mc 43  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=EV UnBlock Sel · Module=MC42-33 (MC42[0]) · Module index=12
- Lit : `12`, `EV UnBlock Sel`
- Utilisé par : `Measure group: Hydraulic`
- Ligne export : 74160 · id 128482

#### mc 12V Batt  `MDGN`
- Propriétés : Value=Supply voltage [V] · Module=MC42-33 (MC42[0]) · Module index=4
- Utilisé par : `12v Battery LOW`, `12v Charge`, `Need to Charge Voltage`, `Need to charge 12v`, `Measure group: System Monitoring`
- Ligne export : 74173 · id 39175

#### 12v Battery LOW  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=500
- Logique :
  - **Activating** = `mc 12V Batt [V] < 11`
- Lit : `mc 12V Batt`
- Utilisé par : `MD4-10 page: MAIN`, `MD4-5 page: BASE`, `MD4-5 page: MAIN Elec`
- Ligne export : 74184 · id 154132

#### Need to charge 12v  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=1000
- Logique :
  - **Activating** = `mc 12V Batt [V] < 11,8`
- Lit : `mc 12V Batt`
- Utilisé par : `Batterie 12v State`
- Ligne export : 74229 · id 102145

#### 12v Charge  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=3000
- Logique :
  - **Activating** = `mc 12V Batt [V] > 13`
- Lit : `13`, `mc 12V Batt`
- Utilisé par : `Batterie 12v State`
- Ligne export : 74274 · id 102153

#### Batterie 12v State  `SMC`
- Propriétés : Default state name=Normal
- Fonction *Charge* :
  - **Activating** = `12v Charge`
- Fonction *Need to charge* :
  - **Activating** = `Need to charge 12v`
- Lit : `12v Charge`, `Need to charge 12v`
- Utilisé par : *(personne)*
- Ligne export : 74319 · id 102161

#### create new state tyva elec  `MAC`
- Logique :
  ```qcode
  static outputValue:= 0
  
  if Drive Type mc=0 and Is_Tyva=0 then//0 mean elec
    outputValue := 0  //0 mean elec no tyva
  elseif Drive Type mc=0 and Is_Tyva=1 then //0 mean elec
    outputValue := 2 //2 mean elec no tyva
  elseif Drive Type mc=1 then //1 mean fossil
    outputValue := 1 //1 mean fossil
  endif
  
  Result := outputValue
  ```
- Lit : `Drive Type mc`, `Is_Tyva`
- Utilisé par : `reset/brake or tyva on qcode`
- Ligne export : 74390 · id 232171

#### reset/brake or tyva on qcode  `SP`
- Propriétés : Input channel=create new state tyva elec · Default state name=Electric 1 novum old · States={Fossil 1; Electric 2 Tyva}
- Lit : `create new state tyva elec`
- Utilisé par : `Brake T/ Batt HT reset / tyva on SEL qcode`
- Ligne export : 74418 · id 232205

#### test batt main on/off  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Brake T/ Batt HT reset / tyva on SEL qcode`, `Adjust group: Master Features`, `Single adjust item: test batt main on/off`
- Ligne export : 74431 · id 232230

#### Brake T/ Batt HT reset / tyva on SEL qcode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=reset/brake or tyva on qcode
- Fonction *Electric 1 novum old* :
  - **Activating** = `Battery Reset E`
- Fonction *Fossil 1* :
  - **Activating** = `T Inter EV Frein`
- Fonction *Electric 2 Tyva* :
  - **Activating** = `(test batt main on/off) OR (batt tyva main on)`
  - **Blocking** = `flag true pb isomon tyva`
- Lit : `Battery Reset E`, `T Inter EV Frein`, `batt tyva main on`, `flag true pb isomon tyva`, `reset/brake or tyva on qcode`, `test batt main on/off`
- Utilisé par : `sel batt reset/batt on or brake`, `sel var power`
- Ligne export : 74444 · id 232211

#### is_cab_math  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `is_cab_mc`
- Lit : `is_cab_mc`
- Utilisé par : `is_cab_1`
- Ligne export : 74563 · id 232360

#### is_cab_1  `SP`
- Propriétés : Input channel=is_cab_math · Default state name=x100 · States={cab}
- Lit : `is_cab_math`
- Utilisé par : `sel batt reset/batt on or brake`, `sel var power`
- Ligne export : 74605 · id 232358

#### sel batt reset/batt on or brake  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=is_cab_1
- Fonction *x100* :
  - **Activating** = `Brake T/ Batt HT reset / tyva on SEL qcode`
- Fonction *cab* :
  - **Activating** = `Var Power`
- Lit : `Brake T/ Batt HT reset / tyva on SEL qcode`, `Var Power`, `is_cab_1`
- Utilisé par : `Brake T/ Batt HT reset OR tyva on mc 44 / Var Power C`
- Ligne export : 74617 · id 232366

#### Brake T/ Batt HT reset OR tyva on mc 44 / Var Power C  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=sel batt reset/batt on or brake · Module=MC42-33 (MC42[0]) · Module index=14
- Lit : `sel batt reset/batt on or brake`
- Utilisé par : *(personne)*
- Ligne export : 74691 · id 208129

#### Locking pressure mc 9  `VIN`
- Propriétés : Unit=bar · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-SP500 · Calibration={500; 4500; 0; 500} · Alarms={No; 0; No; 100} · Module=MC42-33 (MC42[0]) · Module index=1
- Utilisé par : `E OK UP/DOWN`, `Locking pressure mc 9 ok`, `OK BLOC`, `T OK BLOC`, `T OK UP/DOWN`, `MD4-10 page: INFO`, `MD4-5 page: BASE`, `MD4-5 page: INFO`, `Measure group: Hydraulic`
- Ligne export : 74704 · id 128416

#### Track pressure mc 10  `VIN`
- Propriétés : Unit=bar · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-SP500 · Calibration={500; 4500; 0; 500} · Alarms={No; 0; No; 100} · Module=MC42-33 (MC42[0]) · Module index=2
- Utilisé par : `E Pression Filter`, `E show symbole track bleu`, `T Pression filtered`, `T Track Tension Error mc`, `T show symbole track bleu`, `Track pressure mc 10 ok`, `e Track Tension Error mc`, `Event log: Electronic logs`, `MD4-10 page: INFO`, `MD4-5 page: BASE`, `MD4-5 page: BASE Info`, `MD4-5 page: INFO`, `Measure group: Hydraulic`
- Ligne export : 74728 · id 128575

#### Oil level Analog mc 8  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Calibration={50; 1800; 0; 100} · Alarms={Yes; 5; No; 120} · Module=MC42-33 (MC42[0]) · Module index=0
- Utilisé par : `Oil level`, `Oil level Analog mc 8 ok`, `Wait Oil Level`, `Wait_Very_Low_Oil_Level`, `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Hydraulic`
- Ligne export : 74752 · id 128738

#### Reset Startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset Startup`
- Utilisé par : `OIL Security`, `T Tracks pressure Mode`, `e Tracks pressure Mode`, `error 1st start`, `flag true pb isomon tyva`
- Ligne export : 74776 · id 205139

#### OIL security  `SP`
- Propriétés : Input channel=None · Default state name=ACTIVE · States={Unactive}
- Utilisé par : `OIL Security`, `Single adjust item: Oil security`
- Ligne export : 74826 · id 205302

#### OIL Security  `MEM`
- Propriétés : Input channel=OIL security · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : `OIL security`, `Reset Startup`
- Utilisé par : `Wait_Very_Low_Oil_Level`, `Event log: Hydraulic Event`
- Ligne export : 74838 · id 205304

#### Wait_Very_Low_Oil_Level  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Oil level Analog mc 8 [%] < 80`
  - **Blocking** = `1 = OIL Security`
- Lit : `OIL Security`, `Oil level Analog mc 8`
- Utilisé par : `OK Buz Oil`, `Oil Not Good`, `Oil level mc`, `Stop in :`, `T Oil Security Activation`, `Event log: Hydraulic Event`, `Statistics log: Thermic Stats`
- Ligne export : 74881 · id 205312

#### Stop in :  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=30
- Logique :
  - **Decreasing** = `Wait_Very_Low_Oil_Level`
  - **Resetting** = `(Wait_Very_Low_Oil_Level ? 0 : 100)`
- Lit : `Wait_Very_Low_Oil_Level`
- Utilisé par : `Oil level mc`
- Ligne export : 74935 · id 205321

#### Oil level mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=e1045 Low Oil Tracks Level · Text, English=Stop Engine Immediately. And contact your service center. · Channel=Stop in : [s]
- Logique :
  - **Showing** = `Wait_Very_Low_Oil_Level`
  - **Hiding** = `not(Wait_Very_Low_Oil_Level)`
- Lit : `Stop in :`, `Wait_Very_Low_Oil_Level`
- Utilisé par : *(personne)*
- Ligne export : 74996 · id 205332

#### Wait Oil Level  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Oil level Analog mc 8 [%] < 90`
- Lit : `Oil level Analog mc 8`
- Utilisé par : `Oil level`, `MD4-10 page: MAIN`, `MD4-5 page: BASE`
- Ligne export : 75050 · id 205341

#### Oil level  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header, English=e1087 Low Oil Tracks Level · Text, English=Check Oil Level and hydraulic circuit. And contact your service center. · Channel=Oil level Analog mc 8 [%]
- Logique :
  - **Showing** = `Wait Oil Level`
  - **Hiding** = `not(Wait Oil Level)`
- Lit : `Oil level Analog mc 8`, `Wait Oil Level`
- Utilisé par : *(personne)*
- Ligne export : 75095 · id 205349

#### debug screen  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `debug screen E`, `debug screen T`, `debug vario on`, `Adjust group: Master Features`, `MD4-5 page: BASE`, `Single adjust item: debug screen`
- Ligne export : 75149 · id 208909

#### debug screen T  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(debug screen) AND (Is_Thermic mc)`
- Lit : `Is_Thermic mc`, `debug screen`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 75162 · id 217226

#### debug screen E  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(debug screen) AND (Is_Electric mc)`
- Lit : `Is_Electric mc`, `debug screen`
- Utilisé par : *(personne)*
- Ligne export : 75212 · id 217231

#### sel var power  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=is_cab_1
- Fonction *x100* :
  - **Activating** = `Var Power`
- Fonction *cab* :
  - **Activating** = `Brake T/ Batt HT reset / tyva on SEL qcode`
- Lit : `Brake T/ Batt HT reset / tyva on SEL qcode`, `Var Power`, `is_cab_1`
- Utilisé par : `Power Vars E mc 60/ Batt reset C`
- Ligne export : 75262 · id 232371

#### sel thermic or cab  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Is_Thermic mc) OR is_cab_mc`
- Lit : `Is_Thermic mc`, `is_cab_mc`
- Utilisé par : `Active le groupe: mc.I/O / Oil Temps mc 25 or Current bilge C`
- Ligne export : 75336 · id 232546

#### Engine exhaust coolant sensor ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Exhaust coolant temp mc 52 [°C] Status = OK`
- Lit : `T Exhaust coolant temp mc 52`
- Utilisé par : `MD4-5 page: INFO`
- Ligne export : 75555 · id 232973

#### Oil temps sensor ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T Oil Temps mc 25/Current bilge C [°C] Status = OK`
- Lit : `T Oil Temps mc 25/Current bilge C`
- Utilisé par : *(personne)*
- Ligne export : 75600 · id 233012

#### Oil level Analog mc 8 ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Oil level Analog mc 8 [%] Status = OK`
- Lit : `Oil level Analog mc 8`
- Utilisé par : `MD4-5 page: INFO`
- Ligne export : 75645 · id 233043

#### Track pressure mc 10 ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Track pressure mc 10 [bar] Status = OK`
- Lit : `Track pressure mc 10`
- Utilisé par : `MD4-5 page: INFO`
- Ligne export : 75690 · id 233051

#### Locking pressure mc 9 ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Locking pressure mc 9 [bar] Status = OK`
- Lit : `Locking pressure mc 9`
- Utilisé par : `MD4-5 page: INFO`
- Ligne export : 75735 · id 233066

## mc.I/O / Oil Temps mc 25 or Current bilge C — actif seulement si `sel thermic or cab`

#### T Oil Temps mc 25/Current bilge C  `VIN`
- Propriétés : Unit=°C · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-ST · Calibration={0; 4750; -62; 150} · Alarms={No; 0; No; 100} · Module=MC42-33 (MC42[0]) · Module index=4
- Utilisé par : `Oil temps sensor ok`, `T ECC1_Oil_Temp`, `T Hot Oil mc`, `T Hydraulics Temperature State`, `T Wait Hot Temperature`, `current back to mV`, `Measure group: Hydraulic`
- Ligne export : 75401 · id 192929

#### current back to mV  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe(T Oil Temps mc 25/Current bilge C [°C]: {{-50; 250}; {150; 4750}}, Freeze)`
- Lit : `T Oil Temps mc 25/Current bilge C`
- Utilisé par : `bildge current to p`
- Ligne export : 75425 · id 232553

#### bildge current to p  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe(current back to mV: {{0; 0}; {5000; 100}}, Freeze)`
- Lit : `current back to mV`
- Utilisé par : `Convert bilge current`
- Ligne export : 75475 · id 232561

## mc.I/O / Power Vars E mc 60/ Batt reset C — actif seulement si `Is_Electric mc`

#### Power Vars E mc 60/ Batt reset C  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=sel var power · Module=MC42-33 (MC42[0]) · Module index=15
- Lit : `sel var power`
- Utilisé par : *(personne)*
- Ligne export : 75541 · id 133841
