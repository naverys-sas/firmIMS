# MC2 — Engine Fan

57 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Engine Fan

#### MDGN-Status:MC2[1]  `MDGN`
- Propriétés : Value=Module status · Module=MC2[1] · Module index=0
- Utilisé par : `Inter Allumage Thermique`
- Ligne export : 16761 · id 13561

#### Bad Oil Tracks Level  `FGI`
- Propriétés : Input type=Digital · Input=Wait Very Low Oil Level · Default state name=Default state
- Lit : `Wait Very Low Oil Level`
- Utilisé par : `Oil Security Activation`
- Ligne export : 16772 · id 13562

#### Reset Startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset Startup`
- Lit : ``, `Reset Startup`
- Utilisé par : ``, `Pre Fuel line ignition IDC`, `Reset Startup`, `TEST Full Fan`
- Ligne export : 16783 · id 14610

#### OIL security  `SP`
- Propriétés : Input channel=None · Default state name=ACTIVE · States={Unactive}
- Utilisé par : ``
- Ligne export : 16833 · id 16719

####   `MEM`
- Propriétés : Name, English=OIL Security · Input channel=OIL security · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : ``, `OIL security`, `Reset Startup`
- Utilisé par : `% Timer FAN`, `1 - UP Special`, `10 hours check-up`, `2 - DOWN Special`, `3 - Forward`, `4 - Backward`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Allow Cruise`, `Allow Run Cruise`, `Auto Beach after Down`, `Auto Off Bip`, `Auto Stop Timer`, `AutoStopafter 5 secondes`, `Backlight Value`, `Bip`, `C`, `Calibration Timer`, `Command State`, `Couché night`, `Coupure Thermique avec sécurité`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`, `DOWN Counter`, `Days in current year`, `Dec`, `Digit Engine On`, `ET`, `ET h`, `Engine hours`, `Etat Engine`, `F1 - Button`, `FAN Processing`, `FAN Timer`, `Fan mode State`, `Fuel line ignition`, `Fuel line ignition`, `Fuel line ignition IDC`, `Fuel line ignition Output`, `Ho`, `Ho h`, `Ho night`, `Hot/Cold`, `Hour actual`, `IDC Auto Sleep`, `IDC Speed Fast`, `IDC Speed Free`, `IDC Speed R Wait`, `IDC Speed S Wait`, `IDC Speed Slow`, `Iguana PIN`, `Inter Allumage Thermique`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter FAN`, `Inter Full Fan`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Joystick is not in neutral position`, `Ko to move`, `L`, `Latence Math`, `LatenceTimer`, `Levé night`, `Lon`, `M`, `MD3 START`, `MD3 STOP`, `Math Droit`, `Math Gauche`, `Math Timer`, `Memorizing Water Temp`, `Mini Wait`, `Méridian`, `Night mode`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `Oil Security Activation`, `Ok to move`, `Point mort Manip +`, `Point mort Manip -`, `Pre Fuel line ignition IDC`, `Process Down Engine`, `Progress`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Reset Speed`, `Reset Startup`, `Reset Startup`, `Reset on startup`, `Rise`, `START Engine`, `Security PIN`, `Set`, `Setup PIN`, `Show P-1-2`, `Show Start`, `Show Timer`, `Speed`, `Starter Proctection IDC`, `Starter Protection`, `Starter Protection CMSG`, `State Latence`, `State Up/Down`, `State Up/Down`, `Stop Cruise`, `Store TIMER UP/DOWN`, `Sunrise`, `Sunset`, `TEST Full Fan`, `TRACK DOWN`, `TRACK UP`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer Special Mode`, `Timer UP/DOWN`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Timer to Img`, `Timer to Img`, `Toggle Free`, `Track DOWN Delay`, `Track UP Delay`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `UP/DOWN Special mode`, `VIEW ENGINE RUN PAGE`, `VIEW START PAGE`, `Wait Buz 2`, `Wait SWITCH ON Engine`, `X`, `Y`, `Year since 2000`, `Z`, `days since 2000`, `Event log: Acceleration`, `Event log: Check UP`, `Event log: Engine Start/Stop`, `Event log: Hydraulic and Engine Event`, `Statistics log: Engine Hours`, `Statistics log: System 1 Log`, `Statistics log: System 2 log`
- Ligne export : 16845 · id 14618

#### Oil Security Activation  `IDC`
- Propriétés : Toggle=No · Delay on=60000 · Delay off=0
- Logique :
  - **Activating** = `(Bad Oil Tracks Level) AND (OIL Security = 0)`
- Lit : ``, `Bad Oil Tracks Level`
- Utilisé par : `Coupure Thermique avec sécurité`
- Ligne export : 16889 · id 13564

#### MD3 Start/Stop Button  `APPIN`
- Propriétés : Input channel=Can Out Button State
- Lit : `Can Out Button State`
- Utilisé par : `MD3 START`, `MD3 STOP`
- Ligne export : 16941 · id 13573

#### MD3 STOP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `NegativeFlank(MD3 Start/Stop Button)`
- Lit : ``, `MD3 Start/Stop Button`
- Utilisé par : `Coupure Thermique avec sécurité`, `START Engine`
- Ligne export : 16950 · id 13574

#### Coupure Thermique avec sécurité  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MD3 STOP) OR (Oil Security Activation)`
- Lit : ``, `MD3 STOP`, `Oil Security Activation`
- Utilisé par : `Digit Engine On`, `FAN Timer`, `Memorizing Water Temp`
- Ligne export : 16994 · id 13582

#### Calibration Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Fuel line ignition IDC`
  - **Resetting** = `(PositiveFlank(Fuel line ignition IDC)) OR (not(Pre Fuel line ignition IDC))`
- Lit : ``, `Fuel line ignition IDC`, `Pre Fuel line ignition IDC`
- Utilisé par : `Fuel line ignition Output`, `Pre Fuel line ignition IDC`, `Progress`
- Ligne export : 17044 · id 22526

#### Fuel line ignition  `MEM`
- Propriétés : Input channel=Fuel line ignition State · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `NegativeFlank(Pre Fuel line ignition IDC)`
- Lit : ``, `Fuel line ignition State`, `Pre Fuel line ignition IDC`
- Utilisé par : `Fuel line ignition`, `Pre Fuel line ignition IDC`, `Adjust group: Maintenance`, `Single adjust item: Fuel line ignition`
- Ligne export : 17112 · id 22537

#### Fuel line ignition  `CMSG`
- Propriétés : Show message=All · Dialog type=Message · Header=Fuel line ignition · Text=Please wait during fuel line ignition. (Engine need to be stop). · Channel=Progress [%]
- Logique :
  - **Showing** = `PositiveFlank(Fuel line ignition IDC)`
  - **Hiding** = `NegativeFlank(Fuel line ignition IDC)`
- Lit : ``, `Fuel line ignition`, `Fuel line ignition IDC`, `Progress`
- Utilisé par : `Pre Fuel line ignition IDC`, `Adjust group: Maintenance`, `Single adjust item: Fuel line ignition`
- Ligne export : 17156 · id 22586

#### Starter Protection CMSG  `IMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Starter Temperature Protection · Text=Please check fuel level, battery level, oil level, fuel line, fuel filter. Do NOT start the engine more than 5 time per minute. You can start an fuel line ignition buy press RUN. · Left button=Ok · Center button=RUN
- Logique :
  - **Showing** = `Starter Proctection IDC`
  - **Hiding** = `(2 = Starter Protection CMSG) OR ((not(Fuel line ignition IDC)) and (not(Starter Proctection IDC))) OR (NegativeFlank(Fuel line ignition IDC))`
- Lit : ``, `C`, `Fuel line ignition IDC`, `Starter Proctection IDC`
- Utilisé par : `Pre Fuel line ignition IDC`
- Ligne export : 17211 · id 22877

#### Pre Fuel line ignition IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((1 = Fuel line ignition))) OR (PositiveFlank((3 = Starter Protection CMSG))) OR (Pre Fuel line ignition IDC)`
  - **Blocking** = `(Calibration Timer [s] > 50) OR (Engine START) OR (Reset Startup)`
- Lit : ``, `C`, `Calibration Timer`, `Engine START`, `Fuel line ignition`, `Reset Startup`, `Starter Protection CMSG`
- Utilisé par : `Calibration Timer`, `Fuel line ignition`, `Fuel line ignition IDC`
- Ligne export : 17301 · id 22893

#### Fuel line ignition IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Pre Fuel line ignition IDC`
  - **Blocking** = `Engine START`
- Lit : ``, `Engine START`, `Pre Fuel line ignition IDC`
- Utilisé par : `Calibration Timer`, `Fuel line ignition`, `MD3 START`, `Starter Protection CMSG`, `Event log: Hydraulic and Engine Event`
- Ligne export : 17401 · id 22546

#### Fuel line ignition State  `SP`
- Propriétés : Input channel=None · Default state name=OFF · States={RUN}
- Utilisé par : `Fuel line ignition`
- Ligne export : 17451 · id 22525

#### Progress  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `Calibration Timer [s] * 2`
- Lit : ``, `Calibration Timer`
- Utilisé par : `Fuel line ignition`
- Ligne export : 17463 · id 22578

#### Starter Protection Slope  `SFC`
- Propriétés : Input channel=Starter Protection [%] · Enable=Yes · Type=Slopes · Slopes={{10; 1}; {0; 0}}
- Lit : `Starter Protection`
- Utilisé par : `Starter Proctection IDC`
- Ligne export : 17506 · id 22871

#### Starter Proctection IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Starter Protection Slope [%] >= 150`
- Lit : ``, `Starter Protection Slope`
- Utilisé par : `Starter Protection CMSG`
- Ligne export : 17524 · id 22925

#### Out START Engine  `DOUT`
- Propriétés : Delay on=1000 · Delay off=0 · Input channel=START Engine · Module=MC2[1] · Module index=21
- Lit : `START Engine`
- Utilisé par : `Etat Engine`, `Starter Protection`, `Statistics log: System 1 Log`
- Ligne export : 17569 · id 13607

#### Starter Protection  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `1000 * Out START Engine`
- Lit : ``, `Out START Engine`
- Utilisé par : `Starter Protection Slope`
- Ligne export : 17582 · id 22872

#### START Engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MD3 START) OR (START Engine)`
  - **Blocking** = `(Engine START) OR (MD3 STOP) OR (PositiveFlank(AutoStopafter 5 secondes)) OR (Joystick Neutral)`
- Lit : ``, `AutoStopafter 5 secondes`, `Engine START`, `Joystick Neutral`, `MD3 START`, `MD3 STOP`
- Utilisé par : `AutoStopafter 5 secondes`, `FAN Processing`, `Inter FAN`, `Out START Engine`
- Ligne export : 17625 · id 13599

#### AutoStopafter 5 secondes  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `START Engine`
  - **Blocking** = `Engine START`
- Lit : ``, `Engine START`, `START Engine`
- Utilisé par : `Digit Engine On`, `START Engine`
- Ligne export : 17704 · id 17451

#### MD3 START  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `MD3 Start/Stop Button`
  - **Blocking** = `Fuel line ignition IDC`
- Lit : ``, `Fuel line ignition IDC`, `MD3 Start/Stop Button`
- Utilisé par : `Digit Engine On`, `FAN Timer`, `Joystick is not in neutral position`, `START Engine`
- Ligne export : 17754 · id 13591

#### Joystick Neutral  `FGI`
- Propriétés : Input type=Digital · Input=Condition Accélération Thermique · Default state name=Default state
- Lit : `Condition Accélération Thermique`
- Utilisé par : `Joystick is not in neutral position`, `START Engine`
- Ligne export : 17804 · id 17813

#### MD3 Status CAN In  `APPIN`
- Propriétés : Input channel=MD3 CAN Status · Error value=0
- Lit : `MD3 CAN Status`
- Utilisé par : `Inter Allumage Thermique`
- Ligne export : 17815 · id 13608

#### ECU Engine  `DP`
- Propriétés : True text=ON · False text=OFF · Default mode={False}
- Utilisé par : `Inter Allumage Thermique`, `Adjust group: Master Setup`, `Single adjust item: ECU Engine`
- Ligne export : 17825 · id 17536

#### Digit Engine On  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Digit Engine On) OR (MD3 START)`
  - **Blocking** = `(Coupure Thermique avec sécurité) OR (PositiveFlank(AutoStopafter 5 secondes))`
- Lit : ``, `AutoStopafter 5 secondes`, `Coupure Thermique avec sécurité`, `MD3 START`
- Utilisé par : `Inter Allumage Thermique`, `Inter FAN`
- Ligne export : 17838 · id 13609

#### Fuel line ignition Output  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inside((Calibration Timer [s] mod 10), 1, 9)`
- Lit : ``, `Calibration Timer`
- Utilisé par : `Inter Allumage Thermique`
- Ligne export : 17903 · id 22622

#### Inter Allumage Thermique  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(((64 = MDGN-Status:MC2[1]) and (64 = MD3 Status CAN In)) and Digit Engine On) OR (ECU Engine) OR (Fuel line ignition Output)`
- Lit : ``, `C`, `Digit Engine On`, `ECU Engine`, `Fuel line ignition Output`, `MD3 Status CAN In`, `MDGN-Status:MC2[1]`
- Utilisé par : `Etat Engine`, `Out SWITCH ON Engine`
- Ligne export : 17958 · id 13619

#### Out SWITCH ON Engine  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter Allumage Thermique · Module=MC2[1] · Module index=20
- Lit : `Inter Allumage Thermique`
- Utilisé par : `Engine START`, `Thermic Engine STATE`, `Wait SWITCH ON Engine`
- Ligne export : 18051 · id 13629

#### Temp cold/hot  `FP`
- Propriétés : Unit=°C · Default mode={92}
- Utilisé par : `Hot/Cold`, `Adjust group: Master Setup`, `Single adjust item: Temp cold/hot`
- Ligne export : 18064 · id 13630

#### Water Temps  `FGI`
- Propriétés : Unit=°C · Input type=Integer · Input=Engine coolant temperature [°C] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `C`
- Utilisé par : `% Timer FAN`, `FAN Processing`, `Inter Full Fan`, `Memorizing Water Temp`
- Ligne export : 18076 · id 13631

#### Memorizing Water Temp  `MEM`
- Propriétés : Input channel=Water Temps [°C] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `(Water Temps [°C] <> 0) AND (PositiveFlank(Coupure Thermique avec sécurité))`
- Lit : ``, `Coupure Thermique avec sécurité`, `Water Temps`
- Utilisé par : `% Timer FAN`, `Fan mode State`, `Hot/Cold`
- Ligne export : 18090 · id 13632

#### Fan Mode  `DP`
- Propriétés : True text=Temp · False text=Timer · Default mode={False}
- Utilisé par : `Fan mode State`, `Hot/Cold`, `Adjust group: Master Setup`, `Single adjust item: Fan Mode`
- Ligne export : 18144 · id 18426

#### Hot/Cold  `SMC`
- Propriétés : Default state name=Water Cold
- Fonction *Water Hot* :
  - **Activating** = `Memorizing Water Temp [°C] > Temp cold/hot [°C]`
  - **Blocking** = `Fan Mode`
- Fonction *Timer Mode* :
  - **Activating** = `Fan Mode`
- Lit : ``, `Fan Mode`, `Memorizing Water Temp`, `Temp cold/hot`
- Utilisé par : `Math Timer`
- Ligne export : 18157 · id 13641

#### Ambiante Temperature  `SP`
- Propriétés : Input channel=None · Default state name=Normal · States={High}
- Utilisé par : `Timer Fan Engine Hot`, `Timer Fan Engine cold`, `Adjust group: Setup`, `Single adjust item: Ambiante Temperature`
- Ligne export : 18237 · id 14122

#### Timer Fan Engine cold  `FP`
- Propriétés : Unit=s · Mode selector=Ambiante Temperature · Default mode: Normal={60} · Mode 1: High={120}
- Lit : `Ambiante Temperature`
- Utilisé par : `Math Timer`
- Ligne export : 18249 · id 13649

#### Timer Fan Engine Hot  `FP`
- Propriétés : Unit=s · Mode selector=Ambiante Temperature · Default mode: Normal={180} · Mode 1: High={270}
- Lit : `Ambiante Temperature`
- Utilisé par : `Math Timer`
- Ligne export : 18263 · id 13650

#### Minimum Fan  `IP`
- Propriétés : Default mode={20}
- Utilisé par : `Math Timer`
- Ligne export : 18277 · id 18438

#### Math Timer  `IMAC`
- Propriétés : Unit=s · Function selector=Hot/Cold
- Fonction *Water Cold* :
  - **Controlling** = `Timer Fan Engine cold [s]`
- Fonction *Water Hot* :
  - **Controlling** = `Timer Fan Engine Hot [s]`
- Fonction *Timer Mode* :
  - **Controlling** = `Minimum Fan`
- Lit : ``, `Hot/Cold`, `Minimum Fan`, `Timer Fan Engine Hot`, `Timer Fan Engine cold`
- Utilisé par : `% Timer FAN`, `FAN Processing`, `FAN Timer`
- Ligne export : 18289 · id 13651

#### FAN Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=Math Timer [s]
- Logique :
  - **Decreasing** = `(Inside(FAN Timer [s], 0, Math Timer [s])) OR (PositiveFlank(Coupure Thermique avec sécurité))`
  - **Resetting** = `(MD3 START) OR (PositiveFlank(Coupure Thermique avec sécurité))`
- Lit : ``, `Coupure Thermique avec sécurité`, `MD3 START`, `Math Timer`
- Utilisé par : `% Timer FAN`, `FAN Processing`
- Ligne export : 18392 · id 13674

#### Stop temp Fan  `IP`
- Propriétés : Default mode={82}
- Utilisé par : `FAN Processing`
- Ligne export : 18470 · id 18395

#### Fan mode State  `SMC`
- Propriétés : Default state name=Timer
- Fonction *Temps* :
  - **Activating** = `Fan Mode`
  - **Blocking** = `Memorizing Water Temp [°C] < 88`
- Lit : ``, `Fan Mode`, `Memorizing Water Temp`
- Utilisé par : `% Timer FAN`, `FAN Processing`
- Ligne export : 18482 · id 18422

#### FAN Processing  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Fan mode State
- Fonction *Timer* :
  - **Activating** = `Inside(FAN Timer [s], 0, Math Timer [s])`
- Fonction *Temps* :
  - **Activating** = `Water Temps [°C] >= Stop temp Fan`
  - **Blocking** = `START Engine`
- Lit : ``, `FAN Timer`, `Fan mode State`, `Math Timer`, `START Engine`, `Stop temp Fan`, `Water Temps`
- Utilisé par : `% Timer FAN`, `Inter FAN`
- Ligne export : 18531 · id 13687

#### Inter FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Digit Engine On) OR (FAN Processing)`
  - **Blocking** = `START Engine`
- Lit : ``, `Digit Engine On`, `FAN Processing`, `START Engine`
- Utilisé par : `Out FAN Engine`
- Ligne export : 18617 · id 13695

#### Out FAN Engine  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter FAN · Module=MC2[1] · Module index=22
- Lit : `Inter FAN`
- Utilisé par : *(personne)*
- Ligne export : 18674 · id 13705

#### Etat Engine  `SMC`
- Propriétés : Default state name=OFF
- Fonction *START Engine* :
  - **Activating** = `Out START Engine`
- Fonction *SWITCH ON Engine* :
  - **Activating** = `Inter Allumage Thermique`
- Lit : ``, `Inter Allumage Thermique`, `Out START Engine`
- Utilisé par : *(personne)*
- Ligne export : 18687 · id 13706

#### FAN Plus temp  `FP`
- Propriétés : Unit=°C · Default mode={97}
- Utilisé par : `Inter Full Fan`, `Adjust group: Master Setup`, `Single adjust item: FAN Plus temp`
- Ligne export : 18758 · id 13718

#### Full Fan Mode  `SP`
> This channel is used to give unit and names to the MEM
- Propriétés : Input channel=None · Default state name=AUTO · States={FULL}
- Utilisé par : `TEST Full Fan`, `Adjust group: Maintenance`, `Single adjust item: `
- Ligne export : 18770 · id 16705

#### TEST Full Fan  `MEM`
- Propriétés : Input channel=Full Fan Mode · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : ``, `Full Fan Mode`, `Reset Startup`
- Utilisé par : `Inter Full Fan`, `Single adjust item: `
- Ligne export : 18783 · id 14594

#### Inter Full Fan  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `(Water Temps [°C] > FAN Plus temp [°C]) OR (1 = TEST Full Fan)`
  - **Blocking** = `Engine STOP`
- Lit : ``, `Engine STOP`, `FAN Plus temp`, `TEST Full Fan`, `Water Temps`
- Utilisé par : `OUT Full FAN`
- Ligne export : 18826 · id 13720

#### OUT Full FAN  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter Full Fan · Module=MC2[1] · Module index=23
- Lit : `Inter Full Fan`
- Utilisé par : `MD3 page: BASE`
- Ligne export : 18887 · id 13729

#### % Timer FAN  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Fan mode State
- Fonction *Timer* :
  - **Controlling** = `FAN Processing * lin(FAN Timer [s]: 0->0, Math Timer [s]->100, Freeze)`
- Fonction *Temps* :
  - **Controlling** = `FAN Processing * lin(Water Temps [°C]: 82->0, Memorizing Water Temp [°C]->99, Freeze)`
- Lit : ``, `FAN Processing`, `FAN Timer`, `Fan mode State`, `Math Timer`, `Memorizing Water Temp`, `Water Temps`
- Utilisé par : `CAN Out tIMER FAN`
- Ligne export : 18900 · id 14953

#### CAN Out tIMER FAN  `APPOUT`
- Propriétés : Input channel=% Timer FAN [%] · Send method=On change · Transmit rate=1000
- Lit : `% Timer FAN`
- Utilisé par : `Can tIMER in`
- Ligne export : 19001 · id 13740

#### Wait SWITCH ON Engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=200000
- Logique :
  - **Activating** = `Out SWITCH ON Engine`
- Lit : ``, `Out SWITCH ON Engine`
- Utilisé par : `Active le groupe: SAEJ Std input`
- Ligne export : 19012 · id 17244

#### Joystick is not in neutral position  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header, English=Neutral position · Text, English=Please put jostick in neutral position before start engine.
- Logique :
  - **Showing** = `(Joystick Neutral) AND (PositiveFlank(MD3 START))`
- Lit : ``, `Joystick Neutral`, `MD3 START`
- Utilisé par : *(personne)*
- Ligne export : 19055 · id 17815
