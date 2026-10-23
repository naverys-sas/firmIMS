# MC2 — (racine appli)

14 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## (racine)

#### MDGN-Address:MC2[1]  `MDGN`
- Propriétés : Value=Id tag · Module=MC2[1] · Module index=3
- Utilisé par : *(personne)*
- Ligne export : 15062 · id 8724

#### MDGN-S/N:MC2[1]  `MDGN`
- Propriétés : Value=Serial number · Module=MC2[1] · Module index=1
- Utilisé par : *(personne)*
- Ligne export : 15073 · id 8728

#### MDGN-Temp:MC2[1]  `MDGN`
- Propriétés : Value=Temperature [°C] · Module=MC2[1] · Module index=2
- Lit : `C`
- Utilisé par : *(personne)*
- Ligne export : 15084 · id 8729

####   `MDGN`
- Propriétés : Name, English=Battery tension · Value=Supply voltage [V] · Module=MC2[1] · Module index=4
- Utilisé par : ``, `1 - UP Special`, `10 hours check-up`, `10 minutes auto tender`, `2 - DOWN Special`, `3 - Forward`, `4 - Backward`, `ALL ASK STOP`, `ASK STOP`, `Accélération Thermique`, `Action Down`, `Action UP`, `Active Locking`, `Allow Cruise`, `Allow Run Cruise`, `Auto Beach after Down`, `Auto Off Bip`, `Auto Stop Timer`, `Backlight Value`, `Backward Curent`, `Batterie State`, `Bip`, `Bloc`, `C`, `Calcul Accélération`, `Charge`, `Command State`, `Condition Accélération Thermique`, `Couché night`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`, `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `DOWN Counter`, `Days in current year`, `Dec`, `Delay Off super ok tension`, `Don'push button`, `ET`, `ET h`, `Engine START`, `Engine STOP`, `Engine hours`, `F1 - Button`, `FALSE`, `Forward Curent`, `Ho`, `Ho h`, `Ho night`, `Hour actual`, `IDC Auto Sleep`, `IDC Free`, `IDC Speed Fast`, `IDC Speed Free`, `IDC Speed R Wait`, `IDC Speed S Wait`, `IDC Speed Slow`, `Iguana PIN`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter EV By Pass`, `Inter EV DOWN`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP`, `Inter EV UP Delay`, `Inter EV Verin`, `Inter EV tendre Chenille`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Ko to move`, `L`, `Latence Math`, `LatenceTimer`, `Levé night`, `Libre`, `Lon`, `M`, `MD3 - DOWN`, `MD3 - UP`, `Map PWM - blocage`, `Map bloc - Blocage/selctor`, `Map bloc - Déblocage`, `Map bloc - dé tendeur Chenille`, `Map bloc - tendeur Chenille`, `Math Droit`, `Math Gauche`, `Max Manip`, `Mini Wait`, `Méridian`, `NEED MORE SPEED`, `Need Pressure`, `Need to charge`, `Night mode`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `OK UP/DOWN`, `ON/OFF/Untighed`, `Ok tension`, `Ok to move`, `Over Tension`, `PWM Selector`, `Point mort Manip +`, `Point mort Manip -`, `Power State Int`, `Process Down Engine`, `Pump 1 Right`, `Pump 1 Right Filter ECC1`, `Pump 2 Left`, `Pump 2 Left Filter ECC1`, `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Reset Speed`, `Reset Startup`, `Reset Startup`, `Reset on startup`, `Rise`, `SARTING`, `SPEED Engine`, `Security PIN`, `Set`, `Setup PIN`, `Show P-1-2`, `Show Start`, `Show Timer`, `Speed`, `Speed Mode`, `Speed Pump`, `State All Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `State Up/Down`, `State Up/Down Raw`, `Stop Cruise`, `Store TIMER UP/DOWN`, `Sunrise`, `Sunset`, `Super Ok Tension Math`, `Super Ok tension`, `TRACK DOWN`, `TRACK UP`, `TRUE`, `Tension State`, `Thermic Engine STATE`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer Special Mode`, `Timer UP/DOWN`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Timer to Img`, `Timer to Img`, `Toggle Free`, `Track DOWN Delay`, `Track Tension Error`, `Track UP Delay`, `Tracks pressure Mode`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `UP/DOWN Special mode`, `VIEW BUTTON States`, `VIEW ENGINE RUN PAGE`, `VIEW SPEED STATE`, `VIEW START PAGE`, `Wait Buz 2`, `Wait engine Stop`, `Wait engine start`, `X`, `Y`, `Year since 2000`, `Z`, `days since 2000`, `Event log: Acceleration`, `Event log: Check UP`, `Event log: Engine Start/Stop`, `Event log: Hydraulic and Engine Event`, `Statistics log: Engine Hours`, `Statistics log: System 1 Log`, `Statistics log: System 2 log`
- Ligne export : 15095 · id 8733

#### MDGN-VREF:MC2[1]  `MDGN`
- Propriétés : Value=Reference voltage [V] · Module=MC2[1] · Module index=5
- Utilisé par : *(personne)*
- Ligne export : 15107 · id 8735

#### TRUE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True`
- Lit : ``
- Utilisé par : `Alim by pass et frein`, `Alim moteur`, `Alim vérin et tendeur`
- Ligne export : 19112 · id 14138

#### Alim moteur  `DOUT`
- Propriétés : Delay on=1000 · Delay off=0 · Input channel=TRUE · Module=MC2[1] · Module index=6
- Lit : `TRUE`
- Utilisé par : *(personne)*
- Ligne export : 19155 · id 14146

#### Alim by pass et frein  `DOUT`
- Propriétés : Delay on=1000 · Delay off=0 · Input channel=TRUE · Module=MC2[1] · Module index=5
- Lit : `TRUE`
- Utilisé par : *(personne)*
- Ligne export : 19168 · id 14147

#### Alim vérin et tendeur  `DOUT`
- Propriétés : Delay on=1000 · Delay off=0 · Input channel=TRUE · Module=MC2[1] · Module index=7
- Lit : `TRUE`
- Utilisé par : *(personne)*
- Ligne export : 19181 · id 14148

#### Need to charge  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=1000
- Logique :
  - **Activating** = `Battery tension [V] < 11,8`
- Lit : ``
- Utilisé par : `Batterie State`
- Ligne export : 20258 · id 17499

#### Charge  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=3000
- Logique :
  - **Activating** = `Battery tension [V] > 13`
- Lit : ``
- Utilisé par : `Batterie State`
- Ligne export : 20303 · id 17503

#### Batterie State  `SMC`
- Propriétés : Default state name=Normal
- Fonction *Charge* :
  - **Activating** = `Charge`
- Fonction *Need to charge* :
  - **Activating** = `Need to charge`
- Lit : ``, `Charge`, `Need to charge`
- Utilisé par : `MD3 page: BASE`
- Ligne export : 20348 · id 14817

####   `SIC`
- Propriétés : Name, English=Project version · Value=Project version
- Utilisé par : ``, `1 - UP Special`, `10 hours check-up`, `10 minutes auto tender`, `2 - DOWN Special`, `3 - Forward`, `4 - Backward`, `ALL ASK STOP`, `ASK STOP`, `Accélération Thermique`, `Action Down`, `Action UP`, `Active Locking`, `Allow Cruise`, `Allow Run Cruise`, `Auto Beach after Down`, `Auto Off Bip`, `Auto Stop Timer`, `Backlight Value`, `Backward Curent`, `Batterie State`, `Bip`, `Bloc`, `C`, `Calcul Accélération`, `Charge`, `Command State`, `Condition Accélération Thermique`, `Couché night`, `DMAC EV Pompe 1 Droite`, `DMAC EV Pompe 2 Gauche`, `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `DOWN Counter`, `Days in current year`, `Dec`, `Delay Off super ok tension`, `Don'push button`, `ET`, `ET h`, `Engine START`, `Engine STOP`, `Engine hours`, `F1 - Button`, `FALSE`, `Forward Curent`, `Ho`, `Ho h`, `Ho night`, `Hour actual`, `IDC Auto Sleep`, `IDC Free`, `IDC Speed Fast`, `IDC Speed Free`, `IDC Speed R Wait`, `IDC Speed S Wait`, `IDC Speed Slow`, `Iguana PIN`, `Inter Buzzer`, `Inter DOWN`, `Inter DOWN Delay`, `Inter DOWN Super Delay`, `Inter EV By Pass`, `Inter EV DOWN`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP`, `Inter EV UP Delay`, `Inter EV Verin`, `Inter EV tendre Chenille`, `Inter UP`, `Inter UP Delay`, `Inter UP Super Delay`, `Intermediaire`, `Internal Value Timer UP/DOWN`, `Ko to move`, `L`, `Latence Math`, `LatenceTimer`, `Levé night`, `Libre`, `Lon`, `M`, `MD3 - DOWN`, `MD3 - UP`, `Map PWM - blocage`, `Map bloc - Blocage/selctor`, `Map bloc - Déblocage`, `Map bloc - dé tendeur Chenille`, `Map bloc - tendeur Chenille`, `Math Droit`, `Math Gauche`, `Max Manip`, `Mini Wait`, `Méridian`, `NEED MORE SPEED`, `Need Pressure`, `Need to charge`, `Night mode`, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`, `OK UP/DOWN`, `ON/OFF/Untighed`, `Ok tension`, `Ok to move`, `Over Tension`, `PWM Selector`, `Point mort Manip +`, `Point mort Manip -`, `Power State Int`, `Process Down Engine`, `Pump 1 Right`, `Pump 1 Right Filter ECC1`, `Pump 2 Left`, `Pump 2 Left Filter ECC1`, `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `R`, `RadioDroit%`, `RadioGauche%`, `RadioMode`, `RadioStartInter`, `RadioStopInter`, `Re-Track mode in water`, `Reset Speed`, `Reset Startup`, `Reset Startup`, `Reset on startup`, `Rise`, `SARTING`, `SPEED Engine`, `Security PIN`, `Set`, `Setup PIN`, `Show P-1-2`, `Show Start`, `Show Timer`, `Speed`, `Speed Mode`, `Speed Pump`, `State All Speed`, `State Latence`, `State Up/Down`, `State Up/Down`, `State Up/Down`, `State Up/Down Raw`, `Stop Cruise`, `Store TIMER UP/DOWN`, `Sunrise`, `Sunset`, `Super Ok Tension Math`, `Super Ok tension`, `TRACK DOWN`, `TRACK UP`, `TRUE`, `Tension State`, `Thermic Engine STATE`, `Timeout radio`, `Timer Auto Sleep Engine`, `Timer Special Mode`, `Timer UP/DOWN`, `Timer sleep engine to Img`, `Timer sleep engine to Img`, `Timer to Img`, `Timer to Img`, `Toggle Free`, `Track DOWN Delay`, `Track Tension Error`, `Track UP Delay`, `Tracks pressure Mode`, `UP Counter`, `UP/DOWN Button`, `UP/DOWN Choice`, `UP/DOWN Special mode`, `VIEW BUTTON States`, `VIEW ENGINE RUN PAGE`, `VIEW SPEED STATE`, `VIEW START PAGE`, `Wait Buz 2`, `Wait engine Stop`, `Wait engine start`, `X`, `Y`, `Year since 2000`, `Z`, `days since 2000`, `Event log: Acceleration`, `Event log: Check UP`, `Event log: Engine Start/Stop`, `Event log: Hydraulic and Engine Event`, `Statistics log: Engine Hours`, `Statistics log: System 1 Log`, `Statistics log: System 2 log`
- Ligne export : 20419 · id 16865

#### FALSE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Blocking** = `True`
- Lit : ``
- Utilisé par : *(personne)*
- Ligne export : 20429 · id 17080
