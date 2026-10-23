# MC2 — SAEJ Std input

34 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## SAEJ Std input — actif seulement si `Wait SWITCH ON Engine`

#### Engine Temperature  `JFIN`
> ET1
- Propriétés : Priority=6 · PGN=65262 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine coolant temperature [°C]; 1}} · Module=J1939[0] · Module index=8
- Lit : `C`
- Utilisé par : *(personne)*
- Ligne export : 14262 · id 3527

#### Inlet / Exhaust conditions 1  `JFIN`
> IC1
- Propriétés : Priority=6 · PGN=65270 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Intake manifold temperature [°C]; 17}; {Air inlet pressure [kPa]; 25}} · Module=J1939[0] · Module index=9
- Lit : `Air inlet pressure`, `C`, `Intake manifold temperature`
- Utilisé par : *(personne)*
- Ligne export : 14283 · id 3528

####   `JPIN`
- Propriétés : Name, English=Engine coolant temperature · Unit=°C · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-40 · Error value=0
- Utilisé par : `1 - UP Special`, `10 hours check-up`, `2 - DOWN Special`, `3 - Forward`, `4 - Backward`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Allow Cruise`, `Allow Run Cruise`, `Auto Beach after Down`, `Auto Off Bip`, `Auto Stop Timer`, `Backlight Value`, `Bip`, `C`, `Command State`, `Couché night`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`, `DOWN Counter`, `Days in current year`, `Dec`, `ECC1 Integrating / 100`, `ET`, `ET h`, `Engine hours`, `F1 - Button`, `Ho`, `Ho h`, `Ho night`, `Hot Water`, `Hot Water`, `Hour actual`, `IDC Auto Sleep`, `IDC Speed Fast`, `IDC Speed Free`, `IDC Speed R Wait`, `IDC Speed S Wait`, `IDC Speed Slow`, `Iguana PIN`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Ko to move`, `L`, `Latence Math`, `LatenceTimer`, `Led Temp Water`, `Levé night`, `Lon`, `M`, `Math Droit`, `Math Gauche`, `Mini Wait`, `Méridian`, `Night mode`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `Ok to move`, `Point mort Manip +`, `Point mort Manip -`, `Process Down Engine`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Reset Speed`, `Reset Startup`, `Reset on startup`, `Rise`, `Security PIN`, `Set`, `Setup PIN`, `Show P-1-2`, `Show Start`, `Show Timer`, `Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `Stop Cruise`, `Store TIMER UP/DOWN`, `Sunrise`, `Sunset`, `TRACK DOWN`, `TRACK UP`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer Special Mode`, `Timer UP/DOWN`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Timer to Img`, `Timer to Img`, `Toggle Free`, `Track DOWN Delay`, `Track UP Delay`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `UP/DOWN Special mode`, `VIEW ENGINE RUN PAGE`, `VIEW START PAGE`, `Voyant Pression Huile Moteur`, `Voyant T° Eau Moteur Critical`, `Voyant T° Eau Moteur Warning`, `Wait Buz 2`, `X`, `Y`, `Year since 2000`, `Z`, `days since 2000`, `Event log: Acceleration`, `Event log: Check UP`, `Event log: Engine Start/Stop`, `Event log: Hydraulic and Engine Event`, `Statistics log: Engine Hours`, `Statistics log: System 1 Log`, `Statistics log: System 2 log`
- Ligne export : 14307 · id 3530

#### Intake manifold temperature  `JPIN`
- Propriétés : Unit=°C · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-40 · Error value=0
- Utilisé par : `Inlet / Exhaust conditions 1`, `Measure group: Engine`
- Ligne export : 14322 · id 3532

#### Engine fluid level/pressure 1  `JFIN`
> EFL/P1
- Propriétés : Priority=6 · PGN=65263 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Engine oil pressure [kPa]; 25}} · Module=J1939[0] · Module index=12
- Utilisé par : *(personne)*
- Ligne export : 14336 · id 3533

####   `JPIN`
- Propriétés : Name, English=Engine oil pressure · Unit=kPa · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=4 · Offset=0 · Error value=0
- Utilisé par : `1 - UP Special`, `10 hours check-up`, `2 - DOWN Special`, `3 - Forward`, `4 - Backward`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Allow Cruise`, `Allow Run Cruise`, `Auto Beach after Down`, `Auto Off Bip`, `Auto Stop Timer`, `Backlight Value`, `Bip`, `C`, `Command State`, `Couché night`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`, `DOWN Counter`, `Days in current year`, `Dec`, `ECC1 Integrating / 100`, `ET`, `ET h`, `Engine hours`, `F1 - Button`, `Ho`, `Ho h`, `Ho night`, `Hot Water`, `Hot Water`, `Hour actual`, `IDC Auto Sleep`, `IDC Speed Fast`, `IDC Speed Free`, `IDC Speed R Wait`, `IDC Speed S Wait`, `IDC Speed Slow`, `Iguana PIN`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Ko to move`, `L`, `Latence Math`, `LatenceTimer`, `Led Temp Water`, `Levé night`, `Lon`, `M`, `Math Droit`, `Math Gauche`, `Mini Wait`, `Méridian`, `Night mode`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `Ok to move`, `Point mort Manip +`, `Point mort Manip -`, `Process Down Engine`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Reset Speed`, `Reset Startup`, `Reset on startup`, `Rise`, `Security PIN`, `Set`, `Setup PIN`, `Show P-1-2`, `Show Start`, `Show Timer`, `Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `Stop Cruise`, `Store TIMER UP/DOWN`, `Sunrise`, `Sunset`, `TRACK DOWN`, `TRACK UP`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer Special Mode`, `Timer UP/DOWN`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Timer to Img`, `Timer to Img`, `Toggle Free`, `Track DOWN Delay`, `Track UP Delay`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `UP/DOWN Special mode`, `VIEW ENGINE RUN PAGE`, `VIEW START PAGE`, `Voyant Pression Huile Moteur`, `Voyant T° Eau Moteur Critical`, `Voyant T° Eau Moteur Warning`, `Wait Buz 2`, `X`, `Y`, `Year since 2000`, `Z`, `days since 2000`, `Event log: Acceleration`, `Event log: Check UP`, `Event log: Engine Start/Stop`, `Event log: Hydraulic and Engine Event`, `Statistics log: Engine Hours`, `Statistics log: System 1 Log`, `Statistics log: System 2 log`
- Ligne export : 14357 · id 3535

#### EEC1  `JFIN`
> Electronic Engine Controller 1
- Propriétés : Priority=3 · PGN=61444 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Driver's demand, engine % [%]; 9}; {Actual engine, % torque [%]; 17}; {Engine speed [rpm]; 25}} · Module=J1939[0] · Module index=1
- Lit : `Actual engine, % torque`, `Driver's demand, engine %`, `Engine speed`
- Utilisé par : *(personne)*
- Ligne export : 14372 · id 3539

#### Driver's demand, engine %  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `EEC1`
- Ligne export : 14399 · id 3540

#### Actual engine, % torque  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=-125 · Error value=0
- Utilisé par : `ECC1 Integrating limiting 1`, `EEC1`, `Measure group: Engine`, `Measure group: Track pressure`, `Measure group: Translation`
- Ligne export : 14413 · id 3541

#### Engine speed  `JPIN`
- Propriétés : Unit=rpm · Length=2 Bytes (= 16 bits) · J1939 Error check=Yes · Resolution=0,125 · Offset=0 · Error value=0
- Utilisé par : `EEC1`, `Engine START`, `NEED MORE SPEED`, `Measure group: Engine`
- Ligne export : 14427 · id 3542

#### EEC2  `JFIN`
> Electronic Engine Controller 2
- Propriétés : Priority=3 · PGN=61443 · Timeout=2000 · Paged protocol={Not used} · Multipacket=No · Parameters={{Accelerator pedal position [%]; 9}; {% load at current speed [%]; 17}} · Module=J1939[0] · Module index=7
- Lit : `% load at current speed`, `Accelerator pedal position`
- Utilisé par : *(personne)*
- Ligne export : 14441 · id 3543

#### Accelerator pedal position  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=0,4 · Offset=0 · Error value=0
- Utilisé par : `EEC2`
- Ligne export : 14465 · id 3544

#### % load at current speed  `JPIN`
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `EEC2`
- Ligne export : 14479 · id 3545

#### Air inlet pressure  `JPIN`
- Propriétés : Unit=kPa · Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=2 · Offset=0 · Error value=0
- Utilisé par : `Inlet / Exhaust conditions 1`, `Measure group: Engine`
- Ligne export : 14493 · id 3558

#### Para enclench voyant T° moteur warning  `FP`
- Propriétés : Unit=°C · Default mode={100}
- Utilisé par : `Voyant T° Eau Moteur Warning`
- Ligne export : 14507 · id 3577

#### Voyant T° Eau Moteur Warning  `IDC`
- Propriétés : Toggle=No · Delay on=100000 · Delay off=0
- Logique :
  - **Activating** = `(Engine coolant temperature [°C] > Para enclench voyant T° moteur warning [°C]) AND (Engine START)`
- Lit : ``, `C`, `Engine START`, `Para enclench voyant T° moteur warning`
- Utilisé par : `Led Temp Water`, `Event log: Hydraulic and Engine Event`
- Ligne export : 14519 · id 3578

#### Para enclench voyant T° moteur critical  `FP`
- Propriétés : Unit=°C · Default mode={105}
- Utilisé par : `Voyant T° Eau Moteur Critical`
- Ligne export : 14571 · id 14896

#### Voyant T° Eau Moteur Critical  `IDC`
- Propriétés : Toggle=No · Delay on=100000 · Delay off=0
- Logique :
  - **Activating** = `(Engine coolant temperature [°C] > Para enclench voyant T° moteur critical [°C]) AND (Engine START)`
- Lit : ``, `C`, `Engine START`, `Para enclench voyant T° moteur critical`
- Utilisé par : `Hot Water`, `Led Temp Water`
- Ligne export : 14583 · id 14876

#### Hot Water  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=Engine over heating · Text, English=Stop Engine Immediately, let cool down. Check fan and coolant level. And contact your service center. · Channel=Engine coolant temperature [°C]
- Logique :
  - **Showing** = `Voyant T° Eau Moteur Critical`
- Lit : ``, `C`, `Voyant T° Eau Moteur Critical`
- Utilisé par : *(personne)*
- Ligne export : 14635 · id 8216

#### Para enclench voyant pression huile  `FP`
- Propriétés : Unit=kPa · Default mode={300}
- Utilisé par : `Voyant Pression Huile Moteur`
- Ligne export : 14683 · id 8230

#### Voyant Pression Huile Moteur  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `(Engine oil pressure [kPa] < Para enclench voyant pression huile [kPa]) AND (Engine START)`
- Lit : ``, `Engine START`, `Para enclench voyant pression huile`
- Utilisé par : `Hot Water`, `Event log: Hydraulic and Engine Event`, `MD3 page: BASE`
- Ligne export : 14695 · id 8231

#### FP - Start réduction  `FP`
- Propriétés : Unit=% · Default mode={85}
- Utilisé par : `ECC1 Integrating limiting 1`, `Adjust group: Master Setup`, `Single adjust item: FP - Start réduction`
- Ligne export : 14747 · id 14476

#### FP - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={5}
- Utilisé par : `ECC1 Integrating limiting 1`, `Adjust group: Master Setup`, `Single adjust item: FP - Incres Speed`
- Ligne export : 14759 · id 14477

#### FP - Max Error  `FP`
- Propriétés : Unit=% · Default mode={10}
- Utilisé par : `ECC1 Integrating limiting 1`, `Adjust group: Master Setup`, `Single adjust item: FP - Max Error`
- Ligne export : 14771 · id 14478

#### FP - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={60}
- Utilisé par : `ECC1 Integrating limiting 1`, `Adjust group: Master Setup`, `Single adjust item: FP - Decres Speed`
- Ligne export : 14783 · id 17264

#### ECC1 Integrating limiting 1  `ILC`
- Propriétés : Output=Normal · Enable=Engine START · Input channel=Actual engine, % torque [%] · Start reduction at=FP - Start réduction [%] · Max error=FP - Max Error [%] · Max increase speed=FP - Incres Speed [%/s] · Max decrease speed=FP - Decres Speed [%/s]
- Lit : `Actual engine, % torque`, `Engine START`, `FP - Decres Speed`, `FP - Incres Speed`, `FP - Max Error`, `FP - Start réduction`
- Utilisé par : `ECC1 Integrating / 100`, `Measure group: Engine`, `Measure group: Translation`
- Ligne export : 14795 · id 14480

#### FT - Incres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={50}
- Utilisé par : `ECC1 Integrating limiting 2`, `Adjust group: Master Setup`, `Single adjust item: FT - Incres Speed`
- Ligne export : 14810 · id 17094

#### FT - Max Error  `FP`
- Propriétés : Unit=°C · Default mode={5}
- Utilisé par : `ECC1 Integrating limiting 2`, `Adjust group: Master Setup`, `Single adjust item: FT - Max Error`
- Ligne export : 14822 · id 17095

#### FT - Decres Speed  `FP`
- Propriétés : Unit=%/s · Default mode={0,6}
- Utilisé par : `ECC1 Integrating limiting 2`, `Adjust group: Master Setup`, `Single adjust item: FT - Decres Speed`
- Ligne export : 14834 · id 17100

#### FT - Start réduction  `FP`
- Propriétés : Unit=°C · Default mode={99}
- Utilisé par : `ECC1 Integrating limiting 2`, `Adjust group: Master Setup`, `Single adjust item: FT - Start réduction`
- Ligne export : 14846 · id 17093

#### ECC1 Integrating limiting 2  `ILC`
- Propriétés : Output=Normal · Enable=Engine START · Input channel=Engine coolant temperature [°C] · Start reduction at=FT - Start réduction [°C] · Max error=FT - Max Error [°C] · Max increase speed=FT - Incres Speed [%/s] · Max decrease speed=FT - Decres Speed [%/s]
- Lit : `C`, `Engine START`, `FT - Decres Speed`, `FT - Incres Speed`, `FT - Max Error`, `FT - Start réduction`
- Utilisé par : `ECC1 Integrating / 100`, `Measure group: Engine`, `Measure group: Translation`
- Ligne export : 14858 · id 17088

#### ECC1 Integrating / 100  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `(ECC1 Integrating limiting 1 [%] / 100) * (ECC1 Integrating limiting 2 [%] / 100)`
- Lit : ``, `ECC1 Integrating limiting 1`, `ECC1 Integrating limiting 2`
- Utilisé par : `Pump 1 Right Filter ECC1`, `Pump 2 Left Filter ECC1`
- Ligne export : 14873 · id 14481

#### Led Temp Water  `SMC`
- Propriétés : Default state name=Normal
- Fonction *Warning* :
  - **Activating** = `Voyant T° Eau Moteur Warning`
  - **Blocking** = `Voyant T° Eau Moteur Critical`
- Fonction *Critical* :
  - **Activating** = `Voyant T° Eau Moteur Critical`
- Lit : ``, `Voyant T° Eau Moteur Critical`, `Voyant T° Eau Moteur Warning`
- Utilisé par : `MD3 page: BASE`
- Ligne export : 14935 · id 14859

#### Hot Water  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=Inboard engine low oil · Text, English=Stop Engine Immediately, let cool down. Check engine oil level. And contact your service center. Oil type : 10W40.
- Logique :
  - **Showing** = `Voyant Pression Huile Moteur`
- Lit : ``, `Voyant Pression Huile Moteur`
- Utilisé par : *(personne)*
- Ligne export : 15013 · id 18485
