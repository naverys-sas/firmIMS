# MC2 — Oil Security

11 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Oil Security

####   `DIN`
- Propriétés : Name, English=Hydraulic pump statut · Module=MC2[1] · Module index=0
- Utilisé par : ``, `1 - UP Special`, `10 hours check-up`, `2 - DOWN Special`, `3 - Forward`, `4 - Backward`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Allow Cruise`, `Allow Run Cruise`, `Auto Beach after Down`, `Auto Off Bip`, `Auto Stop Timer`, `Backlight Value`, `Bad pressure`, `Bip`, `C`, `Command State`, `Couché night`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`, `DOWN Counter`, `Days in current year`, `Dec`, `ET`, `ET h`, `Engine hours`, `F1 - Button`, `Ho`, `Ho h`, `Ho night`, `Hour actual`, `IDC Auto Sleep`, `IDC Speed Fast`, `IDC Speed Free`, `IDC Speed R Wait`, `IDC Speed S Wait`, `IDC Speed Slow`, `Iguana PIN`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Ko to move`, `L`, `Latence Math`, `LatenceTimer`, `Levé night`, `Lon`, `M`, `Math Droit`, `Math Gauche`, `Mini Wait`, `Méridian`, `Night mode`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `Oil level`, `Oil level`, `Ok to move`, `Point mort Manip +`, `Point mort Manip -`, `Process Down Engine`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Reset Speed`, `Reset Startup`, `Reset on startup`, `Rise`, `Security PIN`, `Set`, `Setup PIN`, `Show P-1-2`, `Show Start`, `Show Timer`, `Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `Stop Cruise`, `Stop in :`, `Store TIMER UP/DOWN`, `Sunrise`, `Sunset`, `Sécurité hydraulique`, `TRACK DOWN`, `TRACK UP`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer Special Mode`, `Timer UP/DOWN`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Timer to Img`, `Timer to Img`, `Toggle Free`, `Track DOWN Delay`, `Track UP Delay`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `UP/DOWN Special mode`, `VIEW ENGINE RUN PAGE`, `VIEW START PAGE`, `Wait Bad Pressure`, `Wait Buz 2`, `Wait Oil Level`, `Wait Very Low Oil Level`, `X`, `Y`, `Year since 2000`, `Z`, `days since 2000`, `Event log: Acceleration`, `Event log: Check UP`, `Event log: Engine Start/Stop`, `Event log: Hydraulic and Engine Event`, `Statistics log: Engine Hours`, `Statistics log: System 1 Log`, `Statistics log: System 2 log`
- Ligne export : 16282 · id 13228

####   `VIN`
- Propriétés : Name, English=Oil level Analog · Unit=% · Reference voltage=Reference voltage A · Error value=0 · Calibration={50; 1800; 0; 100} · Alarms={Yes; 5; No; 120} · Module=MC2[1] · Module index=4
- Lit : ``, `Oil level`
- Utilisé par : `1 - UP Special`, `10 hours check-up`, `2 - DOWN Special`, `3 - Forward`, `4 - Backward`, `ALL ASK STOP`, `ASK STOP`, `Action Down`, `Action UP`, `Allow Cruise`, `Allow Run Cruise`, `Auto Beach after Down`, `Auto Off Bip`, `Auto Stop Timer`, `Backlight Value`, `Bad pressure`, `Bip`, `C`, `Command State`, `Couché night`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`, `DOWN Counter`, `Days in current year`, `Dec`, `ET`, `ET h`, `Engine hours`, `F1 - Button`, `Ho`, `Ho h`, `Ho night`, `Hour actual`, `IDC Auto Sleep`, `IDC Speed Fast`, `IDC Speed Free`, `IDC Speed R Wait`, `IDC Speed S Wait`, `IDC Speed Slow`, `Iguana PIN`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Ko to move`, `L`, `Latence Math`, `LatenceTimer`, `Levé night`, `Lon`, `M`, `Math Droit`, `Math Gauche`, `Mini Wait`, `Méridian`, `Night mode`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `Oil level`, `Oil level`, `Ok to move`, `Point mort Manip +`, `Point mort Manip -`, `Process Down Engine`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Reset Speed`, `Reset Startup`, `Reset on startup`, `Rise`, `Security PIN`, `Set`, `Setup PIN`, `Show P-1-2`, `Show Start`, `Show Timer`, `Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `Stop Cruise`, `Stop in :`, `Store TIMER UP/DOWN`, `Sunrise`, `Sunset`, `Sécurité hydraulique`, `TRACK DOWN`, `TRACK UP`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer Special Mode`, `Timer UP/DOWN`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Timer to Img`, `Timer to Img`, `Toggle Free`, `Track DOWN Delay`, `Track UP Delay`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `UP/DOWN Special mode`, `VIEW ENGINE RUN PAGE`, `VIEW START PAGE`, `Wait Bad Pressure`, `Wait Buz 2`, `Wait Oil Level`, `Wait Very Low Oil Level`, `X`, `Y`, `Year since 2000`, `Z`, `days since 2000`, `Event log: Acceleration`, `Event log: Check UP`, `Event log: Engine Start/Stop`, `Event log: Hydraulic and Engine Event`, `Statistics log: Engine Hours`, `Statistics log: System 1 Log`, `Statistics log: System 2 log`
- Ligne export : 16293 · id 13229

#### Wait Very Low Oil Level  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Oil level Analog [%] < 80`
- Lit : ``, `Oil level`
- Utilisé par : `Bad Oil Level Buzzer`, `Bad Oil Tracks Level`, `Oil level`, `Stop in :`, `Sécurité hydraulique`
- Ligne export : 16318 · id 13230

#### Stop in :  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=30
- Logique :
  - **Decreasing** = `Wait Very Low Oil Level`
  - **Resetting** = `(Wait Very Low Oil Level ? 0 : 100)`
- Lit : ``, `Wait Very Low Oil Level`
- Utilisé par : `Oil level`
- Ligne export : 16363 · id 13238

#### Oil level  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=Low Oil Tracks Level · Text, English=Stop Engine Immediately. And contact your service center. · Channel=Stop in : [s]
- Logique :
  - **Showing** = `Wait Very Low Oil Level`
  - **Hiding** = `not(Wait Very Low Oil Level)`
- Lit : ``, `Stop in :`, `Wait Very Low Oil Level`
- Utilisé par : ``, `Oil level`, `Wait Oil Level`, `Wait Very Low Oil Level`
- Ligne export : 16424 · id 13249

#### Wait Bad Pressure  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `(not(Hydraulic pump statut)) AND (Engine START)`
- Lit : ``, `Engine START`
- Utilisé par : `Bad pressure`, `Sécurité hydraulique`, `Event log: Hydraulic and Engine Event`, `MD3 page: BASE`, `Statistics log: System 1 Log`
- Ligne export : 16480 · id 13259

#### Sécurité hydraulique  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Wait Bad Pressure) OR (Wait Very Low Oil Level)`
- Lit : ``, `Wait Bad Pressure`, `Wait Very Low Oil Level`
- Utilisé par : *(personne)*
- Ligne export : 16531 · id 13268

#### Bad Oil Level Buzzer  `APPOUT`
- Propriétés : Input channel=Wait Very Low Oil Level · Send method=On change · Transmit rate=1000
- Lit : `Wait Very Low Oil Level`
- Utilisé par : `CAN IN Oil level`
- Ligne export : 16581 · id 13277

#### Bad pressure  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=Hydraulic pump lubrification failure · Text, English=Stop Engine Immediately. And contact your service center.
- Logique :
  - **Showing** = `Wait Bad Pressure`
- Lit : ``, `Wait Bad Pressure`
- Utilisé par : *(personne)*
- Ligne export : 16592 · id 13278

#### Wait Oil Level  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Oil level Analog [%] < 90`
- Lit : ``, `Oil level`
- Utilisé par : `Oil level`, `Event log: Hydraulic and Engine Event`, `MD3 page: BASE`, `Statistics log: System 1 Log`
- Ligne export : 16640 · id 13286

#### Oil level  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header, English=Low Oil Tracks Level · Text, English=Check Oil Level and hydraulic circuit. And contact your service center. · Channel=Oil level Analog [%]
- Logique :
  - **Showing** = `Wait Oil Level`
  - **Hiding** = `not(Wait Oil Level)`
- Lit : ``, `Oil level`, `Wait Oil Level`
- Utilisé par : ``, `Wait Oil Level`, `Wait Very Low Oil Level`
- Ligne export : 16685 · id 13294
