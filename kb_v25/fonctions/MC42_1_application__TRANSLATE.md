# MC42[1] application — TRANSLATE

25 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## TRANSLATE

#### CAN Speed  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `CAN Speed Input`
- Lit : `CAN Speed Input`
- Utilisé par : `State All Speed`, `State SPEED`, `State Speed Table`
- Ligne export : 60387 · id 75569

#### State SPEED  `SMC`
- Propriétés : Default state name=Slow
- Fonction *Super Slow* :
  - **Activating** = `CAN Speed = 2`
  - **Blocking** = `CAN Speed = 1`
- Fonction *Fast Speed* :
  - **Activating** = `(CAN Speed = 3) OR (CAN Speed = 4) OR (CAN Speed = 5)`
  - **Blocking** = `CAN Speed = 1`
- Lit : `CAN Speed`
- Utilisé par : `Max Speed`, `Start Speed`, `Stop Speed`
- Ligne export : 60429 · id 37954

#### Max Speed  `IP`
- Propriétés : Unit=% · Mode selector=State SPEED · Default mode: Slow={35} · Mode 1: Super Slow={15} · Mode 2: Fast Speed={100}
- Lit : `State SPEED`
- Utilisé par : `DMAC_Speed_1_Right`, `DMAC_Speed_2_Left`, `Min Speed`, `Adjust group: Master Drive`, `Single adjust item: Max Speed`
- Ligne export : 60540 · id 37965

#### Min Speed  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `0 - Max Speed [%]`
- Lit : `Max Speed`
- Utilisé par : `DMAC_Speed_1_Right`, `DMAC_Speed_2_Left`
- Ligne export : 60556 · id 37966

#### Left Joystick  `APPIN`
- Propriétés : Input channel=Left Joystick [%] · Error value=0
- Utilisé par : `DMAC_EV_Pompe_2_Left`, `Adjust group: Master Drive`, `Dual adjust item: Left Joystick`, `Measure group: Motor Left`
- Ligne export : 60599 · id 77881

#### DMAC_EV_Pompe_2_Left  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Left Joystick [%]`
- Lit : `Left Joystick`
- Utilisé par : `DMAC Table Left`, `Joystick to zero`, `Left unfree`, `Right unfree`, `Table Droite Auto`, `Table Gauche Auto`
- Ligne export : 60609 · id 37974

#### Right Joystick  `APPIN`
- Propriétés : Input channel=Right Joystick [%] · Error value=0
- Utilisé par : `DMAC_EV_Pompe_1_Right`, `Adjust group: Master Drive`, `Dual adjust item: Right Joystick`, `Measure group: Motor Right`
- Ligne export : 60659 · id 77879

#### DMAC_EV_Pompe_1_Right  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Right Joystick [%]`
- Lit : `Right Joystick`
- Utilisé par : `DMAC Table Right`, `Joystick to zero`, `Left unfree`, `Right unfree`, `Table Droite Auto`, `Table Gauche Auto`
- Ligne export : 60669 · id 37985

#### IDC Free  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(CAN Free) OR (Tracks pressure Mode)`
- Lit : `CAN Free`, `Tracks pressure Mode`
- Utilisé par : `State Speed Table`
- Ligne export : 60719 · id 56089

#### State Speed Table  `SMC`
- Propriétés : Default state name=OFF
- Fonction *IDLE* :
  - **Activating** = `CAN Speed = 0`
  - **Blocking** = `not(Engines Ready)`
- Fonction *Free* :
  - **Activating** = `(CAN Speed = 1) OR (CAN Speed = 2) OR (CAN Speed = 3)`
  - **Blocking** = `(not(Engines Ready)) OR (not(IDC Free))`
- Fonction *UnFree* :
  - **Activating** = `(CAN Speed = 1) OR (CAN Speed = 2) OR (CAN Speed = 3)`
  - **Blocking** = `(not(Engines Ready)) OR (IDC Free)`
- Fonction *Road Ask* :
  - **Activating** = `CAN Speed = 4`
  - **Blocking** = `not(Engines Ready)`
- Fonction *Road Cruise* :
  - **Activating** = `CAN Speed = 5`
  - **Blocking** = `not(Engines Ready)`
- Lit : `CAN Speed`, `Engines Ready`, `IDC Free`
- Utilisé par : `DMAC Table Left`, `DMAC Table Right`
- Ligne export : 60769 · id 38066

#### Table Gauche Auto  `LTC`
- Propriétés : Unit=% · Row selector=DMAC_EV_Pompe_2_Left [%] · Column selector=DMAC_EV_Pompe_1_Right [%] · Interpolation=Yes · Lookup table=(0; -100; -90; -80; -70; -60; -50; -40; -30; -20; -10; 0; 10; 20; 30; 40; 50; 60; 70; 80; 90; 100); (-100; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-90; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-80; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-70; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-60; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-50; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-40; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-30; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-20; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100); (10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 97; 90; 90; 90; 90; 90; 90; 90; 90; 90; 90); (20; 0; 0; 0; 0; 0; 0; 0; 0; 0...
- Lit : `DMAC_EV_Pompe_1_Right`, `DMAC_EV_Pompe_2_Left`
- Utilisé par : `DMAC Table Left`
- Ligne export : 61034 · id 38087

#### Max_diffrential  `IP`
- Propriétés : Unit=% · Default mode={70}
- Utilisé par : `Left unfree`, `Right unfree`
- Ligne export : 61047 · id 55739

#### Left unfree  `MAC`
- Logique :
  ```qcode
  right := DMAC_EV_Pompe_1_Right
  left := DMAC_EV_Pompe_2_Left
  
  if (right > 0 and left < 0) or (right < 0 and left > 0) then
    res := 0
  elseif  Abs(right) <= Abs(left) then
    res := left
  elseif Abs(right) > Abs(left) then
    res := MaxOfAbs(right * Max_diffrential  / 100, left)
  endif
  
  
  Result := res
  ```
- Lit : `DMAC_EV_Pompe_1_Right`, `DMAC_EV_Pompe_2_Left`, `Max_diffrential`
- Utilisé par : `DMAC Table Left`
- Ligne export : 61059 · id 55783

#### DMAC Table Left  `DMAC`
- Propriétés : Unit=% · Function selector=State Speed Table
- Fonction *OFF* :
  - **Controlling +/-** = `0`
- Fonction *IDLE* :
  - **Controlling +/-** = `0`
- Fonction *Free* :
  - **Controlling +/-** = `DMAC_EV_Pompe_2_Left [%]`
- Fonction *UnFree* :
  - **Controlling +/-** = `Left unfree`
- Fonction *Road Ask* :
  - **Controlling +/-** = `0`
- Fonction *Road Cruise* :
  - **Controlling +/-** = `Table Gauche Auto [%]`
- Lit : `DMAC_EV_Pompe_2_Left`, `Left unfree`, `State Speed Table`, `Table Gauche Auto`
- Utilisé par : `DMAC_Speed_2_Left`
- Ligne export : 61089 · id 38088

#### Table Droite Auto  `LTC`
- Propriétés : Unit=% · Row selector=DMAC_EV_Pompe_1_Right [%] · Column selector=DMAC_EV_Pompe_2_Left [%] · Interpolation=Yes · Lookup table=(0; -100; -90; -80; -70; -60; -50; -40; -30; -20; -10; 0; 10; 20; 30; 40; 50; 60; 70; 80; 90; 100); (-100; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-90; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-80; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-70; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-60; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-50; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-40; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-30; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-20; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100); (10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 97; 90; 90; 90; 90; 90; 90; 90; 90; 90; 90); (20; 0; 0; 0; 0; 0; 0; 0; 0; 0...
- Lit : `DMAC_EV_Pompe_1_Right`, `DMAC_EV_Pompe_2_Left`
- Utilisé par : `DMAC Table Right`
- Ligne export : 61339 · id 38135

#### Right unfree  `MAC`
- Logique :
  ```qcode
  right := DMAC_EV_Pompe_1_Right
  left := DMAC_EV_Pompe_2_Left
  
  if (right > 0 and left < 0) or (right < 0 and left > 0) then
    res := 0
  elseif  Abs(right) >= Abs(left) then
    res := right
  elseif Abs(right) < Abs(left) then
    res := MaxOfAbs(left * Max_diffrential  / 100, right)
  endif
  
  
  Result := res
  ```
- Lit : `DMAC_EV_Pompe_1_Right`, `DMAC_EV_Pompe_2_Left`, `Max_diffrential`
- Utilisé par : `DMAC Table Right`
- Ligne export : 61352 · id 55703

#### DMAC Table Right  `DMAC`
- Propriétés : Unit=% · Function selector=State Speed Table
- Fonction *OFF* :
  - **Controlling +/-** = `0`
- Fonction *IDLE* :
  - **Controlling +/-** = `0`
- Fonction *Free* :
  - **Controlling +/-** = `DMAC_EV_Pompe_1_Right [%]`
- Fonction *UnFree* :
  - **Controlling +/-** = `Right unfree`
- Fonction *Road Ask* :
  - **Controlling +/-** = `0`
- Fonction *Road Cruise* :
  - **Controlling +/-** = `Table Droite Auto [%]`
- Lit : `DMAC_EV_Pompe_1_Right`, `Right unfree`, `State Speed Table`, `Table Droite Auto`
- Utilisé par : `DMAC_Speed_1_Right`
- Ligne export : 61382 · id 38136

#### Start Speed  `IP`
- Propriétés : Unit=%/s · Mode selector=State SPEED · Default mode: Slow={50} · Mode 1: Super Slow={50} · Mode 2: Fast Speed={30}
- Lit : `State SPEED`
- Utilisé par : `Left Filter`, `Right Filter`, `Adjust group: Master Drive`, `Single adjust item: Start Speed`
- Ligne export : 61632 · id 38182

#### Stop Speed  `IP`
- Propriétés : Unit=%/s · Mode selector=State SPEED · Default mode: Slow={60} · Mode 1: Super Slow={60} · Mode 2: Fast Speed={80}
- Lit : `State SPEED`
- Utilisé par : `Left Filter`, `Right Filter`, `Adjust group: Master Drive`, `Single adjust item: Stop Speed`
- Ligne export : 61648 · id 38183

#### DMAC_Speed_1_Right  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `courbe(DMAC Table Right [%]: {{-100; Min Speed [%]}; {0; 0}; {100; Max Speed [%]}}, Freeze) *% Current Limiting [%]`
- Lit : `Current Limiting`, `DMAC Table Right`, `Max Speed`, `Min Speed`
- Utilisé par : `Right Filter`
- Ligne export : 61664 · id 56033

#### Right Filter  `SFC`
- Propriétés : Input channel=DMAC_Speed_1_Right [%] · Enable=Yes · Type=Slopes · Slopes={{Start Speed [%/s]; Stop Speed [%/s]}; {Start Speed [%/s]; Stop Speed [%/s]}}
- Lit : `DMAC_Speed_1_Right`, `Start Speed`, `Stop Speed`
- Utilisé par : `Math Right`
- Ligne export : 61734 · id 38184

#### DMAC_Speed_2_Left  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `courbe(DMAC Table Left [%]: {{-100; Min Speed [%]}; {0; 0}; {100; Max Speed [%]}}, Freeze) *% Current Limiting [%]`
- Lit : `Current Limiting`, `DMAC Table Left`, `Max Speed`, `Min Speed`
- Utilisé par : `Left Filter`
- Ligne export : 61752 · id 56057

#### Left Filter  `SFC`
- Propriétés : Input channel=DMAC_Speed_2_Left [%] · Enable=Yes · Type=Slopes · Slopes={{Start Speed [%/s]; Stop Speed [%/s]}; {Start Speed [%/s]; Stop Speed [%/s]}}
- Lit : `DMAC_Speed_2_Left`, `Start Speed`, `Stop Speed`
- Utilisé par : `Math Left`
- Ligne export : 61822 · id 38185

#### Joystick to zero  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(DMAC_EV_Pompe_1_Right [%] = 0) AND (DMAC_EV_Pompe_2_Left [%] = 0)`
- Lit : `DMAC_EV_Pompe_1_Right`, `DMAC_EV_Pompe_2_Left`
- Utilisé par : `Joystick to zero CMSG`, `Joystick to zero output`, `MD4 - Start Button Blocking Neutral`
- Ligne export : 61840 · id 38186

#### State All Speed  `SMC`
- Propriétés : Default state name=OFF
- Fonction *IDLE* :
  - **Activating** = `CAN Speed = 0`
  - **Blocking** = `not(Engines Ready)`
- Fonction *Slow* :
  - **Activating** = `CAN Speed = 1`
  - **Blocking** = `not(Engines Ready)`
- Fonction *Super Slow* :
  - **Activating** = `CAN Speed = 2`
  - **Blocking** = `not(Engines Ready)`
- Fonction *Fast* :
  - **Activating** = `CAN Speed = 3`
  - **Blocking** = `not(Engines Ready)`
- Fonction *Road Ask* :
  - **Activating** = `CAN Speed = 4`
  - **Blocking** = `not(Engines Ready)`
- Fonction *Road Cruise* :
  - **Activating** = `CAN Speed = 5`
  - **Blocking** = `not(Engines Ready)`
- Lit : `CAN Speed`, `Engines Ready`
- Utilisé par : `Speed State`
- Ligne export : 61894 · id 56137
