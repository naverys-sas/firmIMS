# MC42 — Translate

24 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Translate

#### Left CanIn  `APPIN`
- Propriétés : Input channel=Manip Gauche CanOut [%] · Error value=0
- Lit : `Manip Gauche CanOut`
- Utilisé par : `DMAC_EV_2_Left`, `Joystick Zero`, `Joystick not zero`, `Max Manip`
- Ligne export : 10228 · id 25340

#### System Started  `IDC`
- Propriétés : Toggle=No · Delay on=750 · Delay off=500
- Logique :
  - **Activating** = `Engine_Started OR (Engines Ready)`
- Lit : ``, `Engine_Started`, `Engines Ready`
- Utilisé par : `10 minutes auto tender`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `ENGINE RUN Input`, `Over Tension`, `SARTING`, `State All Speed`, `System Started`, `Thermic Engine STATE`, `Wait engine start`
- Ligne export : 10238 · id 25341

#### Right CanIn  `APPIN`
- Propriétés : Input channel=Manip Droit CanOut [%] · Error value=0
- Lit : `Manip Droit CanOut`
- Utilisé par : `DMAC_EV_1_Right`, `Joystick Zero`, `Joystick not zero`, `Max Manip`
- Ligne export : 10288 · id 25361

#### Speed Int  `IMAC`
- Logique :
  - **Controlling** = `Speed Input`
- Lit : ``, `Speed Input`
- Utilisé par : `Speed Mode`, `Speed Pump`, `State All Speed`
- Ligne export : 10298 · id 36082

#### Speed Pump  `SMC`
- Propriétés : Default state name=Slow
- Fonction *Super Slow* :
  - **Activating** = `Speed Int = 2`
  - **Blocking** = `Speed Int = 1`
- Fonction *Fast Speed* :
  - **Activating** = `(Speed Int = 3) OR (Speed Int = 4) OR (Speed Int = 5)`
  - **Blocking** = `Speed Int = 1`
- Lit : ``, `Speed Int`
- Utilisé par : `Backward - direct corrector`, `Backward Curent`, `Brake Slope`, `Forward - direct corrector`, `Forward Curent`, `Max Speed`, `Start Slope`, `Stop Slope`
- Ligne export : 10339 · id 25363

#### Engine Stopped  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine_Stopped`
- Lit : ``, `Engine_Stopped`
- Utilisé par : `Speed Mode`
- Ligne export : 10450 · id 25432

#### IDC Free  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Free Input) OR (Tracks pressure Mode)`
- Lit : ``, `Free Input`, `Tracks pressure Mode`
- Utilisé par : `Speed Mode`
- Ligne export : 10493 · id 33764

#### Speed Mode  `SMC`
- Propriétés : Default state name=OFF
- Fonction *IDLE* :
  - **Activating** = `Speed Int = 0`
  - **Blocking** = `Engine Stopped`
- Fonction *Free* :
  - **Activating** = `(Speed Int = 1) OR (Speed Int = 2) OR (Speed Int = 3)`
  - **Blocking** = `(Engine Stopped) OR (not(IDC Free))`
- Fonction *UnFree* :
  - **Activating** = `(Speed Int = 1) OR (Speed Int = 2) OR (Speed Int = 3)`
  - **Blocking** = `Engine Stopped`
- Fonction *Cruise Ask* :
  - **Activating** = `Speed Int = 4`
  - **Blocking** = `Engine Stopped`
- Fonction *Cruise* :
  - **Activating** = `Speed Int = 5`
  - **Blocking** = `Engine Stopped`
- Lit : ``, `Engine Stopped`, `IDC Free`, `Speed Int`
- Utilisé par : `DMAC Table Left`, `DMAC Table Right`, `VIEW BUTTON States`
- Ligne export : 10543 · id 25440

#### Start Slope  `FP`
- Propriétés : Unit=%/s · Mode selector=Speed Pump · Default mode: Slow={50} · Mode 1: Super Slow={50} · Mode 2: Fast Speed={30}
- Lit : `Speed Pump`
- Utilisé par : `Filter Left`, `Filter Right`, `Left Filter`, `Right Filter`, `Adjust group: `, `Single adjust item: Start Slope`
- Ligne export : 10796 · id 25678

#### Stop Slope  `FP`
- Propriétés : Unit=%/s · Mode selector=Speed Pump · Default mode: Slow={60} · Mode 1: Super Slow={60} · Mode 2: Fast Speed={80}
- Lit : `Speed Pump`
- Utilisé par : `Filter Left`, `Filter Right`, `Left Filter`, `Right Filter`, `Adjust group: `, `Single adjust item: Stop Slope`
- Ligne export : 10812 · id 25679

#### DMAC_EV_2_Left  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Left CanIn [%] * System Started`
- Lit : ``, `Left CanIn`, `System Started`
- Utilisé par : `Cruise Left`, `Cruise Right`, `DMAC Table Left`, `Left unfree`, `Right unfree`
- Ligne export : 10828 · id 33931

#### DMAC_EV_1_Right  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Right CanIn [%] * System Started`
- Lit : ``, `Right CanIn`, `System Started`
- Utilisé par : `Cruise Left`, `Cruise Right`, `DMAC Table Right`, `Left unfree`, `Right unfree`
- Ligne export : 10880 · id 33942

#### Cruise Left  `LTC`
- Propriétés : Unit=% · Row selector=DMAC_EV_2_Left [%] · Column selector=DMAC_EV_1_Right [%] · Interpolation=Yes · Lookup table=(0; -100; -90; -80; -70; -60; -50; -40; -30; -20; -10; 0; 10; 20; 30; 40; 50; 60; 70; 80; 90; 100); (-100; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-90; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-80; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-70; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-60; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-50; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-40; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-30; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-20; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100); (10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 97; 90; 90; 90; 90; 90; 90; 90; 90; 90; 90); (20; 0; 0; 0; 0; 0; 0; 0; 0; 0...
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`
- Utilisé par : `DMAC Table Left`
- Ligne export : 10932 · id 33952

#### Max_diffrential  `IP`
- Propriétés : Unit=% · Default mode={70}
- Utilisé par : `Left unfree`, `Right unfree`, `Adjust group: Master Tracks`, `Single adjust item: Max_diffrential`
- Ligne export : 10945 · id 33953

#### Left unfree  `MAC`
- Logique :
  ```qcode
  right := DMAC_EV_1_Right
  left := DMAC_EV_2_Left
  
  if (right > 0 and left < 0) or (right < 0 and left > 0) then
    res := 0
  elseif  Abs(right) <= Abs(left) then
    res := left
  elseif Abs(right) > Abs(left) then
    res := MaxOfAbs(right * Max_diffrential  / 100, left)
  endif
  
  
  Result := res
  ```
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `Max_diffrential`
- Utilisé par : `DMAC Table Left`
- Ligne export : 10957 · id 33954

#### DMAC Table Left  `DMAC`
- Propriétés : Unit=% · Function selector=Speed Mode
- Fonction *OFF* :
  - **Controlling +/-** = `0`
- Fonction *IDLE* :
  - **Controlling +/-** = `0`
- Fonction *Free* :
  - **Controlling +/-** = `DMAC_EV_2_Left [%]`
- Fonction *UnFree* :
  - **Controlling +/-** = `Left unfree`
- Fonction *Cruise Ask* :
  - **Controlling +/-** = `0`
- Fonction *Cruise* :
  - **Controlling +/-** = `Cruise Left [%]`
- Lit : ``, `Cruise Left`, `DMAC_EV_2_Left`, `Left unfree`, `Speed Mode`
- Utilisé par : `Brake Activation`, `Left Filter`
- Ligne export : 10987 · id 33992

#### Left Filter  `SFC`
- Propriétés : Input channel=DMAC Table Left [%] · Enable=Yes · Type=Slopes · Slopes={{Start Slope [%/s]; Stop Slope [%/s]}; {Start Slope [%/s]; Stop Slope [%/s]}}
- Lit : `DMAC Table Left`, `Start Slope`, `Stop Slope`
- Utilisé par : `Brake Activation`, `Math Left`, `Pump 2 Left Filter ECC1`
- Ligne export : 11237 · id 25680

#### Cruise Right  `LTC`
- Propriétés : Unit=% · Row selector=DMAC_EV_1_Right [%] · Column selector=DMAC_EV_2_Left [%] · Interpolation=Yes · Lookup table=(0; -100; -90; -80; -70; -60; -50; -40; -30; -20; -10; 0; 10; 20; 30; 40; 50; 60; 70; 80; 90; 100); (-100; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-90; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-80; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-70; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-60; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-50; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-40; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-30; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-20; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100); (10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 97; 90; 90; 90; 90; 90; 90; 90; 90; 90; 90); (20; 0; 0; 0; 0; 0; 0; 0; 0; 0...
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`
- Utilisé par : `DMAC Table Right`
- Ligne export : 11255 · id 34002

#### Right unfree  `MAC`
- Logique :
  ```qcode
  right := DMAC_EV_1_Right
  left := DMAC_EV_2_Left
  
  if (right > 0 and left < 0) or (right < 0 and left > 0) then
    res := 0
  elseif  Abs(right) >= Abs(left) then
    res := right
  elseif Abs(right) < Abs(left) then
    res := MaxOfAbs(left * Max_diffrential  / 100, right)
  endif
  
  
  Result := res
  ```
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `Max_diffrential`
- Utilisé par : `DMAC Table Right`
- Ligne export : 11268 · id 34003

#### DMAC Table Right  `DMAC`
- Propriétés : Unit=% · Function selector=Speed Mode
- Fonction *OFF* :
  - **Controlling +/-** = `0`
- Fonction *IDLE* :
  - **Controlling +/-** = `0`
- Fonction *Free* :
  - **Controlling +/-** = `DMAC_EV_1_Right [%]`
- Fonction *UnFree* :
  - **Controlling +/-** = `Right unfree`
- Fonction *Cruise Ask* :
  - **Controlling +/-** = `0`
- Fonction *Cruise* :
  - **Controlling +/-** = `Cruise Right [%]`
- Lit : ``, `Cruise Right`, `DMAC_EV_1_Right`, `Right unfree`, `Speed Mode`
- Utilisé par : `Brake Activation`, `Right Filter`
- Ligne export : 11298 · id 34041

#### Right Filter  `SFC`
- Propriétés : Input channel=DMAC Table Right [%] · Enable=Yes · Type=Slopes · Slopes={{Start Slope [%/s]; Stop Slope [%/s]}; {Start Slope [%/s]; Stop Slope [%/s]}}
- Lit : `DMAC Table Right`, `Start Slope`, `Stop Slope`
- Utilisé par : `Brake Activation`, `Math Right`, `Pump 1 Right Filter ECC1`
- Ligne export : 11548 · id 25704

#### Brake Activation  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(DMAC Table Left [%] <> 0) OR (DMAC Table Right [%] <> 0) OR (Right Filter [%] <> 0) OR (Left Filter [%] <> 0)`
- Lit : ``, `DMAC Table Left`, `DMAC Table Right`, `Left Filter`, `Right Filter`
- Utilisé par : `Inter EV Frein`
- Ligne export : 11566 · id 33282

#### Joystick Zero  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Right CanIn [%] = 0) AND (Left CanIn [%] = 0)`
- Lit : ``, `Left CanIn`, `Right CanIn`
- Utilisé par : ``, `Joystick is not in neutral position`, `Joystick to zero CMSG`, `MD4 - Start Button Blocking Neutral`
- Ligne export : 11638 · id 54506

#### State All Speed  `SMC`
- Propriétés : Default state name=OFF
- Fonction *IDLE* :
  - **Activating** = `Speed Int = 0`
  - **Blocking** = `not(System Started)`
- Fonction *Slow* :
  - **Activating** = `Speed Int = 1`
  - **Blocking** = `not(System Started)`
- Fonction *Super Slow* :
  - **Activating** = `Speed Int = 2`
  - **Blocking** = `not(System Started)`
- Fonction *Fast* :
  - **Activating** = `Speed Int = 3`
  - **Blocking** = `not(System Started)`
- Fonction *Cruise Ask* :
  - **Activating** = `Speed Int = 4`
  - **Blocking** = `not(System Started)`
- Fonction *Cruise* :
  - **Activating** = `Speed Int = 5`
  - **Blocking** = `not(System Started)`
- Lit : ``, `Speed Int`, `System Started`
- Utilisé par : `Speed All State`
- Ligne export : 11692 · id 56993
