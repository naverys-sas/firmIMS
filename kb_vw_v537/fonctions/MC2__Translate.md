# MC2 — Translate

56 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Translate

#### Left CanIn  `APPIN`
- Propriétés : Input channel=Manip Gauche CanOut [%] · Error value=0
- Lit : `Manip Gauche CanOut`
- Utilisé par : `DMAC_EV_2_Left`, `Manip Gauche CanIn  [%]`
- Ligne export : 9142 · id 1452

#### Engine START  `IDC`
- Propriétés : Toggle=No · Delay on=750 · Delay off=500
- Logique :
  - **Activating** = `(Engine speed [rpm] > 700) and Out SWITCH ON Engine`
- Lit : ``, `Engine speed`, `Out SWITCH ON Engine`
- Utilisé par : `10 minutes auto tender`, `AutoStopafter 5 secondes`, `CAN - ENGINE RUN`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `ECC1 Integrating limiting 1`, `ECC1 Integrating limiting 2`, `Engine STOP`, `Fuel line ignition IDC`, `Over Tension`, `Pre Fuel line ignition IDC`, `SARTING`, `START Engine`, `State All Speed`, `Thermic Engine STATE`, `Voyant Pression Huile Moteur`, `Voyant T° Eau Moteur Critical`, `Voyant T° Eau Moteur Warning`, `Wait Bad Pressure`, `Wait engine start`, `Active le groupe: SAEJ ECM`, `Event log: Engine Start/Stop`, `Event log: Hydraulic and Engine Event`, `Single adjust item: `, `Statistics log: Engine Hours`, `Statistics log: System 1 Log`
- Ligne export : 9152 · id 4675

#### Right CanIn  `APPIN`
- Propriétés : Input channel=Manip Droit CanOut [%] · Error value=0
- Lit : `Manip Droit CanOut`
- Utilisé par : `DMAC_EV_1_Right`, `Manip Droit CanIn [%]`
- Ligne export : 9213 · id 1453

#### CAN Speed  `APPIN`
- Propriétés : Input channel=CAN  Speed
- Lit : `CAN  Speed`
- Utilisé par : `CAN Speed IN`, `Speed Mode`, `Speed Pump`, `State All Speed`
- Ligne export : 9223 · id 14042

#### Speed Pump  `SMC`
- Propriétés : Default state name=Slow Speed
- Fonction *Super Slow* :
  - **Activating** = `CAN Speed = 2`
  - **Blocking** = `CAN Speed = 1`
- Fonction *Fast Speed* :
  - **Activating** = `(CAN Speed = 3) OR (CAN Speed = 4) OR (CAN Speed = 5)`
  - **Blocking** = `CAN Speed = 1`
- Lit : ``, `CAN Speed`
- Utilisé par : `Backward - direct corrector`, `Backward Curent`, `Brake Slope`, `Forward - direct corrector`, `Forward Curent`, `Start Slope - Pump`, `Stop Slope - Pump`
- Ligne export : 9232 · id 14043

#### Min current Right Backward  `FP`
- Propriétés : Unit=mA · Default mode={600}
- Utilisé par : `Pump 1 Right`, `Adjust group: Master Pump`, `Single adjust item: Min current Right Backward`
- Ligne export : 9343 · id 3047

#### Max curent  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: VW 2.0L={1600} · Mode 1: FORD 1.5L={1400}
- Lit : `Engine type`
- Utilisé par : `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`, `Adjust group: Master Pump`, `Single adjust item: Max curent`
- Ligne export : 9355 · id 11853

#### Step change  `FP`
- Propriétés : Unit=mA · Default mode={300}
- Utilisé par : `Punp 1 - Current`, `Punp 1 - Current`, `Punp 2 - Current`, `Punp 2 - Current`
- Ligne export : 9369 · id 11864

#### Forward - direct corrector  `FP`
- Propriétés : Unit=% · Mode selector=Speed Pump · Default mode: Slow Speed={0} · Mode 1: Super Slow={0} · Mode 2: Fast Speed={0}
- Lit : `Speed Pump`
- Utilisé par : `Punp 1 - Current`, `Punp 2 - Current`, `Single adjust item: `
- Ligne export : 9381 · id 11821

#### Forward Curent - Low Speed  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: VW 2.0L={1200} · Mode 1: FORD 1.5L={1200}
- Lit : `Engine type`
- Utilisé par : `Forward Curent`, `Adjust group: Master Pump`, `Single adjust item: Forward Curent - Low Speed`
- Ligne export : 9397 · id 21237

#### Forward Curent  - Hight Speed  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: VW 2.0L={1600} · Mode 1: FORD 1.5L={1400}
- Lit : `Engine type`
- Utilisé par : `Forward Curent`, `Adjust group: Master Pump`, `Single adjust item: Forward Curent  - Hight Speed`
- Ligne export : 9411 · id 21239

#### Forward Curent - Super Low Speed  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: VW 2.0L={850} · Mode 1: FORD 1.5L={850}
- Lit : `Engine type`
- Utilisé par : `Forward Curent`, `Adjust group: Master Pump`, `Single adjust item: Forward Curent - Super Low Speed`
- Ligne export : 9425 · id 23399

#### Forward Curent  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed · Function selector=Speed Pump
- Fonction *Slow Speed* :
  - **Controlling** = `Forward Curent - Low Speed [mA]`
- Fonction *Super Slow* :
  - **Controlling** = `Forward Curent - Super Low Speed [mA]`
- Fonction *Fast Speed* :
  - **Controlling** = `Forward Curent  - Hight Speed [mA]`
- Lit : ``, `Forward Curent  - Hight Speed`, `Forward Curent - Low Speed`, `Forward Curent - Super Low Speed`, `Speed Pump`
- Utilisé par : `Punp 1 - Current`, `Punp 2 - Current`
- Ligne export : 9439 · id 21244

#### Punp 1 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `Forward Curent [mA] - (Forward - direct corrector [%] *% Step change [mA])`
  - **Limiting** = `Max curent [mA]`
- Lit : ``, `Forward - direct corrector`, `Forward Curent`, `Max curent`, `Step change`
- Utilisé par : `Filter pump 1 Neg`, `Filter pump 1 Pos`
- Ligne export : 9543 · id 4417

#### Slope Fast - Low  `FP`
- Propriétés : Unit=mA/s · Default mode={200}
- Utilisé par : `Filter pump 1 Neg`, `Filter pump 1 Pos`, `Filter pump 2 Neg`, `Filter pump 2 Pos`, `Adjust group: Master Setup`, `Single adjust item: Slope Fast - Low`
- Ligne export : 9603 · id 4564

#### Filter pump 1 Pos  `SFC`
- Propriétés : Input channel=Punp 1 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}; {Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}}
- Lit : `Punp 1 - Current`, `Slope Fast - Low`
- Utilisé par : `Pump 1 Right`
- Ligne export : 9615 · id 4429

#### Engine STOP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Engine START)`
- Lit : ``, `Engine START`
- Utilisé par : `Bloc`, `Inter EV DOWN delay`, `Inter EV Frein`, `Inter EV UP Delay`, `Inter EV tendre Chenille`, `Inter Full Fan`, `Libre`, `Speed Mode`
- Ligne export : 9633 · id 3655

#### Min current Left Backward  `FP`
- Propriétés : Unit=mA · Default mode={600}
- Utilisé par : `Pump 2 Left`, `Adjust group: Master Pump`, `Single adjust item: Min current Left Backward`
- Ligne export : 9677 · id 7396

#### Punp 2 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `Forward Curent [mA] + (Forward - direct corrector [%] *% Step change [mA])`
  - **Limiting** = `Max curent [mA]`
- Lit : ``, `Forward - direct corrector`, `Forward Curent`, `Max curent`, `Step change`
- Utilisé par : `Filter pump 2 Neg`, `Filter pump 2 Pos`
- Ligne export : 9689 · id 4586

#### Filter pump 2 Pos  `SFC`
- Propriétés : Input channel=Punp 2 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}; {Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}}
- Lit : `Punp 2 - Current`, `Slope Fast - Low`
- Utilisé par : `Pump 2 Left`
- Ligne export : 9749 · id 4629

#### Min current Left Fordward  `FP`
- Propriétés : Unit=mA · Default mode={600}
- Utilisé par : `Pump 2 Left`, `Adjust group: Master Pump`, `Single adjust item: Min current Left Fordward`
- Ligne export : 9767 · id 7406

#### Backward - direct corrector  `FP`
- Propriétés : Unit=% · Mode selector=Speed Pump · Default mode: Slow Speed={0} · Mode 1: Super Slow={0} · Mode 2: Fast Speed={0}
- Lit : `Speed Pump`
- Utilisé par : `Punp 1 - Current`, `Punp 2 - Current`, `Single adjust item: `
- Ligne export : 9779 · id 11812

#### Backward Curent - Low Speed  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: VW 2.0L={1200} · Mode 1: FORD 1.5L={1200}
- Lit : `Engine type`
- Utilisé par : `Backward Curent`, `Adjust group: Master Pump`, `Single adjust item: Backward Curent - Low Speed`
- Ligne export : 9795 · id 21242

#### Backward Curent  - Hight Speed  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: VW 2.0L={1600} · Mode 1: FORD 1.5L={1400}
- Lit : `Engine type`
- Utilisé par : `Backward Curent`, `Adjust group: Master Pump`, `Single adjust item: Backward Curent  - Hight Speed`
- Ligne export : 9809 · id 21243

#### Backward Curent - Super Low Speed  `FP`
- Propriétés : Unit=mA · Mode selector=Engine type · Default mode: VW 2.0L={850} · Mode 1: FORD 1.5L={850}
- Lit : `Engine type`
- Utilisé par : `Backward Curent`, `Adjust group: Master Pump`, `Single adjust item: Backward Curent - Super Low Speed`
- Ligne export : 9823 · id 23397

#### Backward Curent  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed · Function selector=Speed Pump
- Fonction *Slow Speed* :
  - **Controlling** = `Backward Curent - Low Speed [mA]`
- Fonction *Super Slow* :
  - **Controlling** = `Backward Curent - Super Low Speed [mA]`
- Fonction *Fast Speed* :
  - **Controlling** = `Backward Curent  - Hight Speed [mA]`
- Lit : ``, `Backward Curent  - Hight Speed`, `Backward Curent - Low Speed`, `Backward Curent - Super Low Speed`, `Speed Pump`
- Utilisé par : `Punp 1 - Current`, `Punp 2 - Current`
- Ligne export : 9837 · id 21269

#### Punp 2 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `Backward Curent [mA] + (Backward - direct corrector [%] *% Step change [mA])`
  - **Limiting** = `Max curent [mA]`
- Lit : ``, `Backward - direct corrector`, `Backward Curent`, `Max curent`, `Step change`
- Utilisé par : `Filter pump 2 Neg`, `Filter pump 2 Pos`
- Ligne export : 9941 · id 8071

#### Filter pump 2 Neg  `SFC`
- Propriétés : Input channel=Punp 2 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}; {Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}}
- Lit : `Punp 2 - Current`, `Slope Fast - Low`
- Utilisé par : `Pump 2 Left`
- Ligne export : 10001 · id 8092

#### Start Slope - Pump  `FP`
- Propriétés : Unit=%/s · Mode selector=Speed Pump · Default mode: Slow Speed={100} · Mode 1: Super Slow={100} · Mode 2: Fast Speed={30}
- Lit : `Speed Pump`
- Utilisé par : `Pump 1 Right Filter`, `Pump 2 Left`, `Adjust group: Master Pump`, `Single adjust item: Start Slope - Pump`
- Ligne export : 10019 · id 21358

#### Stop Slope - Pump  `FP`
- Propriétés : Unit=%/s · Mode selector=Speed Pump · Default mode: Slow Speed={100} · Mode 1: Super Slow={100} · Mode 2: Fast Speed={30}
- Lit : `Speed Pump`
- Utilisé par : `Pump 1 Right Filter`, `Pump 2 Left`, `Adjust group: Master Pump`, `Single adjust item: Stop Slope - Pump`
- Ligne export : 10035 · id 21359

#### CAN Free  `APPIN`
- Propriétés : Input channel=CAN  Free
- Lit : `CAN  Free`
- Utilisé par : `IDC Free`
- Ligne export : 10051 · id 25222

#### IDC Free  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(CAN Free) OR (Tracks pressure Mode)`
- Lit : ``, `CAN Free`, `Tracks pressure Mode`
- Utilisé par : `Speed Mode`
- Ligne export : 10060 · id 27528

#### Speed Mode  `SMC`
- Propriétés : Default state name=OFF
- Fonction *IDLE* :
  - **Activating** = `CAN Speed = 0`
  - **Blocking** = `Engine STOP`
- Fonction *Free* :
  - **Activating** = `(CAN Speed = 1) OR (CAN Speed = 2) OR (CAN Speed = 3)`
  - **Blocking** = `(Engine STOP) OR (not(IDC Free))`
- Fonction *UnFree* :
  - **Activating** = `(CAN Speed = 1) OR (CAN Speed = 2) OR (CAN Speed = 3)`
  - **Blocking** = `Engine STOP`
- Fonction *Road Ask* :
  - **Activating** = `CAN Speed = 4`
  - **Blocking** = `Engine STOP`
- Fonction *Road Cruise* :
  - **Activating** = `CAN Speed = 5`
  - **Blocking** = `Engine STOP`
- Lit : ``, `CAN Speed`, `Engine STOP`, `IDC Free`
- Utilisé par : `DMAC Table Left`, `DMAC Table Right`, `Speed Mode`
- Ligne export : 10110 · id 25730

#### DMAC_EV_2_Left  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Left CanIn [%] * Engine START`
- Lit : ``, `Engine START`, `Left CanIn`
- Utilisé par : `Cruise Left`, `Cruise Right`, `DMAC Table Left`, `Left unfree`, `Right unfree`
- Ligne export : 10363 · id 25764

#### DMAC_EV_1_Right  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Right CanIn [%] * Engine START`
- Lit : ``, `Engine START`, `Right CanIn`
- Utilisé par : `Cruise Left`, `Cruise Right`, `DMAC Table Right`, `Left unfree`, `Right unfree`
- Ligne export : 10415 · id 25774

#### Cruise Left  `LTC`
- Propriétés : Unit=% · Row selector=DMAC_EV_2_Left [%] · Column selector=DMAC_EV_1_Right [%] · Interpolation=Yes · Lookup table=(0; -100; -90; -80; -70; -60; -50; -40; -30; -20; -10; 0; 10; 20; 30; 40; 50; 60; 70; 80; 90; 100); (-100; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-90; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-80; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-70; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-60; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-50; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-40; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-30; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-20; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100); (10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 97; 90; 90; 90; 90; 90; 90; 90; 90; 90; 90); (20; 0; 0; 0; 0; 0; 0; 0; 0; 0...
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`
- Utilisé par : `DMAC Table Left`
- Ligne export : 10467 · id 25784

#### Max_diffrential  `IP`
- Propriétés : Unit=% · Default mode={70}
- Utilisé par : `Left unfree`, `Right unfree`, `Adjust group: Master Tracks`, `Single adjust item: Max_diffrential`
- Ligne export : 10480 · id 25785

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
- Ligne export : 10492 · id 25786

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
- Fonction *Road Ask* :
  - **Controlling +/-** = `0`
- Fonction *Road Cruise* :
  - **Controlling +/-** = `Cruise Left [%]`
- Lit : ``, `Cruise Left`, `DMAC_EV_2_Left`, `Left unfree`, `Speed Mode`
- Utilisé par : `Inter EV Frein`, `Pump 2 Left`
- Ligne export : 10522 · id 25824

#### Pump 2 Left  `SFC`
- Propriétés : Input channel=DMAC Table Left [%] · Enable=Yes · Type=Slopes · Slopes={{Start Slope - Pump [%/s]; Stop Slope - Pump [%/s]}; {Start Slope - Pump [%/s]; Stop Slope - Pump [%/s]}}
- Lit : `DMAC Table Left`, `Start Slope - Pump`, `Stop Slope - Pump`
- Utilisé par : `Inter EV Frein`, `Pump 2 Left Filter ECC1`, `Measure group: Translation`
- Ligne export : 10772 · id 21431

#### Pump 2 Left Filter ECC1  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Pump 2 Left [%] * ECC1 Integrating / 100 [%]`
- Lit : ``, `ECC1 Integrating / 100`, `Pump 2 Left`
- Utilisé par : `Pump 2 Left`
- Ligne export : 10790 · id 21432

#### Pump 2 Left  `COUT`
- Propriétés : Bidirectional=Yes · BWL=0 · Input channel=Pump 2 Left Filter ECC1 [%] · Default mode={{Min current Left Fordward [mA]; Filter pump 2 Pos [mA]; 100; 100}; {Min current Left Backward [mA]; Filter pump 2 Neg [mA]; 100; 100}} · Module=MC2[1] · Module index=1
- Lit : ``, `Filter pump 2 Neg`, `Filter pump 2 Pos`, `Min current Left Backward`, `Min current Left Fordward`, `Pump 2 Left Filter ECC1`
- Utilisé par : `Inter EV Frein`, `Pump 2 Left Filter ECC1`, `Measure group: Translation`
- Ligne export : 10842 · id 1006

#### Min current Right Fordward  `FP`
- Propriétés : Unit=mA · Default mode={600}
- Utilisé par : `Pump 1 Right`, `Adjust group: Master Pump`, `Single adjust item: Min current Right Fordward`
- Ligne export : 10868 · id 7403

#### Punp 1 - Current  `MAC`
- Propriétés : Unit=mA · Limiting object group=Signed
- Logique :
  - **Controlling** = `Backward Curent [mA] - (Backward - direct corrector [%] *% Step change [mA])`
  - **Limiting** = `Max curent [mA]`
- Lit : ``, `Backward - direct corrector`, `Backward Curent`, `Max curent`, `Step change`
- Utilisé par : `Filter pump 1 Neg`, `Filter pump 1 Pos`
- Ligne export : 10880 · id 8047

#### Filter pump 1 Neg  `SFC`
- Propriétés : Input channel=Punp 1 - Current [mA] · Enable=Yes · Type=Slopes · Slopes={{Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}; {Slope Fast - Low [mA/s]; Slope Fast - Low [mA/s]}}
- Lit : `Punp 1 - Current`, `Slope Fast - Low`
- Utilisé par : `Pump 1 Right`
- Ligne export : 10940 · id 8069

#### Cruise Right  `LTC`
- Propriétés : Unit=% · Row selector=DMAC_EV_1_Right [%] · Column selector=DMAC_EV_2_Left [%] · Interpolation=Yes · Lookup table=(0; -100; -90; -80; -70; -60; -50; -40; -30; -20; -10; 0; 10; 20; 30; 40; 50; 60; 70; 80; 90; 100); (-100; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-90; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-80; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-70; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-60; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-50; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-40; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-30; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-20; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100); (10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 97; 90; 90; 90; 90; 90; 90; 90; 90; 90; 90); (20; 0; 0; 0; 0; 0; 0; 0; 0; 0...
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`
- Utilisé par : `DMAC Table Right`
- Ligne export : 10958 · id 25879

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
- Ligne export : 10971 · id 25880

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
- Fonction *Road Ask* :
  - **Controlling +/-** = `0`
- Fonction *Road Cruise* :
  - **Controlling +/-** = `Cruise Right [%]`
- Lit : ``, `Cruise Right`, `DMAC_EV_1_Right`, `Right unfree`, `Speed Mode`
- Utilisé par : `Inter EV Frein`, `Pump 1 Right Filter`
- Ligne export : 11001 · id 25918

#### Pump 1 Right Filter  `SFC`
- Propriétés : Input channel=DMAC Table Right [%] · Enable=Yes · Type=Slopes · Slopes={{Start Slope - Pump [%/s]; Stop Slope - Pump [%/s]}; {Start Slope - Pump [%/s]; Stop Slope - Pump [%/s]}}
- Lit : `DMAC Table Right`, `Start Slope - Pump`, `Stop Slope - Pump`
- Utilisé par : `Pump 1 Right Filter ECC1`
- Ligne export : 11251 · id 21334

#### Pump 1 Right Filter ECC1  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `Pump 1 Right Filter [%] * ECC1 Integrating / 100 [%]`
- Lit : ``, `ECC1 Integrating / 100`, `Pump 1 Right Filter`
- Utilisé par : `Pump 1 Right`
- Ligne export : 11269 · id 21350

#### Pump 1 Right  `COUT`
- Propriétés : Bidirectional=Yes · BWL=0 · Input channel=Pump 1 Right Filter ECC1 [%] · Default mode={{Min current Right Fordward [mA]; Filter pump 1 Pos [mA]; 100; 100}; {Min current Right Backward [mA]; Filter pump 1 Neg [mA]; 100; 100}} · Module=MC2[1] · Module index=0
- Lit : ``, `Filter pump 1 Neg`, `Filter pump 1 Pos`, `Min current Right Backward`, `Min current Right Fordward`, `Pump 1 Right Filter ECC1`
- Utilisé par : `Inter EV Frein`, `Measure group: Translation`
- Ligne export : 11321 · id 1008

#### Brake Slope  `IP`
- Propriétés : Unit=ms · Mode selector=Speed Pump · Default mode: Slow Speed={750} · Mode 1: Super Slow={0} · Mode 2: Fast Speed={4000}
- Lit : `Speed Pump`
- Utilisé par : `Inter EV Frein`
- Ligne export : 11347 · id 11166

#### Inter EV Frein  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=Brake Slope [ms]
- Logique :
  - **Activating** = `(Pump 1 Right [mA] <> 0) OR (Pump 2 Left [mA] <> 0) OR (DMAC Table Left [%] <> 0) OR (DMAC Table Right [%] <> 0)`
  - **Blocking** = `Engine STOP`
- Lit : ``, `Brake Slope`, `DMAC Table Left`, `DMAC Table Right`, `Engine STOP`, `Pump 1 Right`, `Pump 2 Left`
- Utilisé par : `EV Frein`
- Ligne export : 11363 · id 1108

#### EV Frein  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter EV Frein · Module=MC2[1] · Module index=12
- Lit : `Inter EV Frein`
- Utilisé par : `Measure group: Translation`
- Ligne export : 11442 · id 1020

#### CAN - ENGINE RUN  `APPOUT`
- Propriétés : Input channel=Engine START · Send method=On change · Transmit rate=1000
- Lit : `Engine START`
- Utilisé par : `CAN - ENGINE RUN - Out`
- Ligne export : 11455 · id 6002

#### State All Speed  `SMC`
- Propriétés : Default state name=OFF
- Fonction *IDLE* :
  - **Activating** = `CAN Speed = 0`
  - **Blocking** = `not(Engine START)`
- Fonction *Slow* :
  - **Activating** = `CAN Speed = 1`
  - **Blocking** = `not(Engine START)`
- Fonction *Super Slow* :
  - **Activating** = `CAN Speed = 2`
  - **Blocking** = `not(Engine START)`
- Fonction *Fast* :
  - **Activating** = `CAN Speed = 3`
  - **Blocking** = `not(Engine START)`
- Fonction *Road Ask* :
  - **Activating** = `CAN Speed = 4`
  - **Blocking** = `not(Engine START)`
- Fonction *Road Cruise* :
  - **Activating** = `CAN Speed = 5`
  - **Blocking** = `not(Engine START)`
- Lit : ``, `CAN Speed`, `Engine START`
- Utilisé par : `Speed All State`
- Ligne export : 11466 · id 26081
