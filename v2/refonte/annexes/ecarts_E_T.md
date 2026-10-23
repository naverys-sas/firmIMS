# Écarts entre les copies électrique (E) et thermique (T) de la logique chenilles

Généré par `outils_pilotage/conception/ecarts_e_t.py` depuis `TESTIA_108.3.1.txt`. Pour chaque canal présent dans les deux copies mais avec une logique différente, il faut choisir : garder E, garder T, ou en faire un réglage dont la valeur par défaut reproduit chaque propulsion (voir `v2/refonte/05_logique_metier.md`).

| Groupe E | Groupe T | Communs | Identiques | Seulement E | Seulement T |
|---|---|---|---|---|---|
| `E.Translate` (24) | `T.Translate` (20) | 18 | 7 | 6 | 2 |
| `E.Track tension` (20) | `T.Track tension` (21) | 18 | 12 | 2 | 3 |
| `E.Track Up/Down` (42) | `T.Track Up/Down` (47) | 25 | 14 | 17 | 22 |
| `E.KeyBox x100 E` (68) | `T.KeyBox x100 T` (71) | 55 | 33 | 13 | 16 |

## E.Translate / T.Translate

Seulement en E : `Joystick to zero`, `System Crash Signal`, `e Debug: Inhibit System Crash Signal`, `e Max Speed`, `e Max_differential`, `e System Started`

Seulement en T : `Engine Stopped`, `T Max_diffrential`

### `DMAC Table Left` ↔ `DMAC Table Left`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Dual direction math channel (DMAC) · Unit=% · Function selector=e Speed Mode
  Function OFF
    Object group Controlling +/- · Method=MaxOf (Absolute) · Valid=True · Expression=
      Single object A · Input=0
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
  Function IDLE
    Object group Controlling +/- · Method=MaxOf (Absolute) · Valid=True · Expression=
      Single object A · Input=0
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
  Function Free
    Object group Controlling +/- · Method=MaxOf (Absolute) · Valid=True · Expression=
      Single object A · Input=DMAC_EV_2_Left [%]
      Math object B · Operator=* · Operand 1=A · Operand 2=System Crash Signal
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
  Function UnFree
    Object group Controlling +/- · Method=Multiply (%) · Valid=True · Expression=
      Single object A · Input=Left unfree
      Math object B · Operator=* · Operand 1=A · Operand 2=System Crash Signal
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
```
**T**
```
Dual direction math channel (DMAC) · Unit=% · Function selector=T Speed Mode
  Function OFF
    Object group Controlling +/- · Method=MaxOf (Absolute) · Valid=True · Expression=
      Single object A · Input=0
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
  Function IDLE
    Object group Controlling +/- · Method=MaxOf (Absolute) · Valid=True · Expression=
      Single object A · Input=0
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
  Function Free
    Object group Controlling +/- · Method=MaxOf (Absolute) · Valid=True · Expression=
      Single object A · Input=DMAC_EV_2_Left [%]
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
  Function UnFree
    Object group Controlling +/- · Method=MaxOf (Absolute) · Valid=True · Expression=
      Single object A · Input=Left unfree
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
```

### `DMAC Table Right` ↔ `DMAC Table Right`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Dual direction math channel (DMAC) · Unit=% · Function selector=e Speed Mode
  Function OFF
    Object group Controlling +/- · Method=MaxOf (Absolute) · Valid=True · Expression=
      Single object A · Input=0
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
  Function IDLE
    Object group Controlling +/- · Method=MaxOf (Absolute) · Valid=True · Expression=
      Single object A · Input=0
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
  Function Free
    Object group Controlling +/- · Method=Multiply (%) · Valid=True · Expression=
      Single object A · Input=DMAC_EV_1_Right [%]
      Math object B · Operator=* · Operand 1=A · Operand 2=System Crash Signal
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
  Function UnFree
    Object group Controlling +/- · Method=Multiply (%) · Valid=True · Expression=
      Single object A · Input=Right unfree
      Math object B · Operator=* · Operand 1=A · Operand 2=System Crash Signal
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
```
**T**
```
Dual direction math channel (DMAC) · Unit=% · Function selector=T Speed Mode
  Function OFF
    Object group Controlling +/- · Method=MaxOf (Absolute) · Valid=True · Expression=
      Single object A · Input=0
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
  Function IDLE
    Object group Controlling +/- · Method=MaxOf (Absolute) · Valid=True · Expression=
      Single object A · Input=0
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
  Function Free
    Object group Controlling +/- · Method=MaxOf (Absolute) · Valid=True · Expression=
      Single object A · Input=DMAC_EV_1_Right [%]
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
  Function UnFree
    Object group Controlling +/- · Method=MaxOf (Absolute) · Valid=True · Expression=
      Single object A · Input=Right unfree
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
```

### `DMAC_EV_1_Right` ↔ `DMAC_EV_1_Right`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Dual direction math channel (DMAC) · Unit=% · Function selector=Not used
  Function Default function
    Object group Controlling +/- · Method=Multiply (%) · Valid=True · Expression=
      Math object A · Operator=* · Operand 1=Math Droit Right 45 [%] · Operand 2=e System Started
      Math object B · Operator=* · Operand 1=A · Operand 2=System Crash Signal
    Object group Limiting + · Method=MaxOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
```
**T**
```
Dual direction math channel (DMAC) · Unit=% · Function selector=Not used
  Function Default function
    Object group Controlling +/- · Method=Multiply (%) · Valid=True · Expression=
      Math object A · Operator=* · Operand 1=Math Droit Right 45 [%] · Operand 2=T System Started DELAYS
    Object group Limiting + · Method=MaxOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
```

### `DMAC_EV_2_Left` ↔ `DMAC_EV_2_Left`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Dual direction math channel (DMAC) · Unit=% · Function selector=Not used
  Function Default function
    Object group Controlling +/- · Method=Multiply (%) · Valid=True · Expression=
      Math object A · Operator=* · Operand 1=Math Gauche Left 45 [%] · Operand 2=e System Started
      Math object B · Operator=* · Operand 1=A · Operand 2=System Crash Signal
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
```
**T**
```
Dual direction math channel (DMAC) · Unit=% · Function selector=Not used
  Function Default function
    Object group Controlling +/- · Method=Multiply (%) · Valid=True · Expression=
      Math object A · Operator=* · Operand 1=Math Gauche Left 45 [%] · Operand 2=T System Started DELAYS
    Object group Limiting + · Method=MinOf (Absolute) · Valid=True · Expression=
    Object group Limiting - · Method=MinOf (Absolute) · Valid=True · Expression=
```

### `IDC Free E` ↔ `IDC Free T`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=e Tracks pressure Mode
      Single object B · Input=Screen_Free Input mc
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=Screen_Free Input mc
      Single object B · Input=T Tracks pressure Mode
    Object group Blocking · Method=Or · Valid=True · Expression=
```

### `Left unfree` ↔ `Left unfree`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Math channel (MAC) · Unit=Not used · Function selector=Not used
  Function Default function
    | right := DMAC_EV_1_Right
    | left := DMAC_EV_2_Left
    | 
    | if (right > 0 and left < 0) or (right < 0 and left > 0) then
    |   res := 0
    | elseif  Abs(right) <= Abs(left) then
    |   res := left
    | elseif Abs(right) > Abs(left) then
    |   res := MaxOfAbs(right * e Max_differential  / 100, left)
    | endif
    | 
    | 
    | Result := res
```
**T**
```
Math channel (MAC) · Unit=Not used · Function selector=Not used
  Function Default function
    | right := DMAC_EV_1_Right
    | left := DMAC_EV_2_Left
    | 
    | if (right > 0 and left < 0) or (right < 0 and left > 0) then
    |   res := 0
    | elseif  Abs(right) <= Abs(left) then
    |   res := left
    | elseif Abs(right) > Abs(left) then
    |   res := MaxOfAbs(right * T Max_diffrential  / 100, left)
    | endif
    | 
    | 
    | Result := res
```

### `Right unfree` ↔ `Right unfree`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Math channel (MAC) · Unit=Not used · Function selector=Not used
  Function Default function
    | right := DMAC_EV_1_Right
    | left := DMAC_EV_2_Left
    | 
    | if (right > 0 and left < 0) or (right < 0 and left > 0) then
    |   res := 0
    | elseif  Abs(right) >= Abs(left) then
    |   res := right
    | elseif Abs(right) < Abs(left) then
    |   res := MaxOfAbs(left * e Max_differential  / 100, right)
    | endif
    | 
    | 
    | Result := res
```
**T**
```
Math channel (MAC) · Unit=Not used · Function selector=Not used
  Function Default function
    | right := DMAC_EV_1_Right
    | left := DMAC_EV_2_Left
    | 
    | if (right > 0 and left < 0) or (right < 0 and left > 0) then
    |   res := 0
    | elseif  Abs(right) >= Abs(left) then
    |   res := right
    | elseif Abs(right) < Abs(left) then
    |   res := MaxOfAbs(left * T Max_diffrential  / 100, right)
    | endif
    | 
    | 
    | Result := res
```

### `e Speed Mode` ↔ `T Speed Mode`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
State machine channel (SMC) · Default state name=OFF
  Function IDLE
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=E Speed Int · Operand 2=0
    Object group Blocking · Method=Or · Valid=True · Expression=
  Function Free
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=E Speed Int · Operand 2=1
      Math object B · Operator== · Operand 1=E Speed Int · Operand 2=2
      Math object C · Operator== · Operand 1=E Speed Int · Operand 2=3
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=IDC Free E
  Function UnFree
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=E Speed Int · Operand 2=1
      Math object B · Operator== · Operand 1=E Speed Int · Operand 2=2
      Math object C · Operator== · Operand 1=E Speed Int · Operand 2=3
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
State machine channel (SMC) · Default state name=OFF
  Function IDLE
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=T Speed Int · Operand 2=0
    Object group Blocking · Method=Or · Valid=True · Expression=
      Single object A · Input=Engine Stopped
  Function Free
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=T Speed Int · Operand 2=1
      Math object B · Operator== · Operand 1=T Speed Int · Operand 2=2
      Math object C · Operator== · Operand 1=T Speed Int · Operand 2=3
    Object group Blocking · Method=Or · Valid=True · Expression=
      Single object A · Input=Engine Stopped
      Math object B · Operator=not · Operand 1=IDC Free T
  Function UnFree
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=T Speed Int · Operand 2=1
      Math object B · Operator== · Operand 1=T Speed Int · Operand 2=2
      Math object C · Operator== · Operand 1=T Speed Int · Operand 2=3
    Object group Blocking · Method=Or · Valid=True · Expression=
      Single object A · Input=Engine Stopped
```

### `e Speed Pump` ↔ `T Speed Pump`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
State machine channel (SMC) · Default state name=Slow
  Function Super Slow
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=E Speed Int · Operand 2=2
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=E Speed Int · Operand 2=1
  Function Fast Speed
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=E Speed Int · Operand 2=3
      Math object B · Operator== · Operand 1=E Speed Int · Operand 2=4
      Math object C · Operator== · Operand 1=E Speed Int · Operand 2=5
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=E Speed Int · Operand 2=1
```
**T**
```
State machine channel (SMC) · Default state name=Slow
  Function Super Slow
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=T Speed Int · Operand 2=2
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=T Speed Int · Operand 2=1
  Function Fast Speed
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=T Speed Int · Operand 2=3
      Math object B · Operator== · Operand 1=T Speed Int · Operand 2=4
      Math object C · Operator== · Operand 1=T Speed Int · Operand 2=5
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=T Speed Int · Operand 2=1
      Math object B · Operator=>= · Operand 1=T Persistant Water Temp [Â°C] · Operand 2=T Water Â°C Critical Critical [Â°C]
```

### `e State All Speed` ↔ `T State All Speed`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
State machine channel (SMC) · Default state name=OFF
  Function IDLE
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=E Speed Int · Operand 2=0
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=e System Started
  Function Slow
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=E Speed Int · Operand 2=1
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=e System Started
  Function Super Slow
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=E Speed Int · Operand 2=2
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=e System Started
  Function Fast
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=E Speed Int · Operand 2=3
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=e System Started
```
**T**
```
State machine channel (SMC) · Default state name=OFF
  Function IDLE
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=T Speed Int · Operand 2=0
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=T System Started DELAYS
  Function Slow
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=T Speed Int · Operand 2=1
      Math object B · Operator=>= · Operand 1=T Persistant Water Temp [Â°C] · Operand 2=T Water Â°C Critical Critical [Â°C]
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=T System Started DELAYS
  Function Super Slow
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=T Speed Int · Operand 2=2
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=T System Started DELAYS
  Function Fast
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator== · Operand 1=T Speed Int · Operand 2=3
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=T System Started DELAYS
      Math object B · Operator=>= · Operand 1=T Persistant Water Temp [Â°C] · Operand 2=T Water Â°C Critical Critical [Â°C]
```

### `e Stop Slope` ↔ `T Stop Slope`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Function parameter channel (FP) · Unit=%/s · Mode selector=e Speed Pump · Default mode: Slow={80} · Mode 1: Super Slow={80} · Mode 2: Fast Speed={80}
```
**T**
```
Function parameter channel (FP) · Unit=%/s · Mode selector=T Speed Pump · Default mode: Slow={60} · Mode 1: Super Slow={60} · Mode 2: Fast Speed={80}
```


## E.Track tension / T.Track tension

Seulement en E : `E Pression Filter`, `E Untingthen`

Seulement en T : `T Need Pressure Tempo`, `T Pression filtered`, `T Untighten`

### `10 minutes auto tender` ↔ `T 10 minutes auto tender`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Timer channel (TMR) · Type (Unit)=Minutes [min] · Store value=No · Reset value=10 · Function selector=Not used
  Function Default function
    Object group Increasing · Method=Or · Valid=True · Expression=
    Object group Decreasing · Method=Or · Valid=True · Expression=
      Single object A · Input=e System Started
    Object group Resetting · Method=Or · Valid=True · Expression=
      Math object A · Operator=<= · Operand 1=10 minutes auto tender [min] · Operand 2=0
```
**T**
```
Timer channel (TMR) · Type (Unit)=Minutes [min] · Store value=No · Reset value=10 · Function selector=Not used
  Function Default function
    Object group Increasing · Method=Or · Valid=True · Expression=
    Object group Decreasing · Method=Or · Valid=True · Expression=
      Single object A · Input=T System Started DELAYS
    Object group Resetting · Method=Or · Valid=True · Expression=
      Math object A · Operator=<= · Operand 1=T 10 minutes auto tender [min] · Operand 2=0
```

### `Need Pressure` ↔ `Need Pressure`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=500 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=> · Operand 1=e Tension Pressure [bar] · Operand 2=E Pression Filter [bar]
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=T Need Pressure Tempo [ms] · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=> · Operand 1=T Tension Pressure [bar] · Operand 2=T Pression filtered [bar]
    Object group Blocking · Method=Or · Valid=True · Expression=
```

### `Ok tension` ↔ `Ok tension`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=500 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=PositiveFlank · Operand 1=Wait engine start
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=500 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=PositiveFlank · Operand 1=Wait engine start
    Object group Blocking · Method=Or · Valid=True · Expression=
      Single object A · Input=T Untighten
```

### `Over Tension` ↔ `Over Tension`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=500 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=Over Tension
      Math object B · Operator=> · Operand 1=Slope Super Ok [%] · Operand 2=e Tension Error Parameter [%]
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=e System Started
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=500 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=Over Tension
      Math object B · Operator=> · Operand 1=Slope Super Ok [%] · Operand 2=T Tension Error Parameter [%]
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=T System Started DELAYS
```

### `e Track Tension Error mc` ↔ `T Track Tension Error mc`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Warning · Header, English=e1038 Track Tension Error · Text, English=Try a Calibrating (Setting/Maintenance). Use straight. Contact your service center. · Channel=Track pressure mc 10 [bar] · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=Over Tension
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Warning · Header, English=e1043 Track Tension Error · Text, English=Try a Calibrating (Setting/Maintenance). Use straight. Contact your service center. · Channel=Track pressure mc 10 [bar] · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=Over Tension
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `Wait engine start` ↔ `Wait engine start`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=2000 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=e System Started
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=2000 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=T System Started DELAYS
    Object group Blocking · Method=Or · Valid=True · Expression=
```


## E.Track Up/Down / T.Track Up/Down

Seulement en E : `E lock`, `E unlock`, `Elec activ shema inter`, `Elec show schema UP`, `Elec show schema down`, `Elec show schema inter`, `Engine hydro`, `Engine hydro Speed E`, `HIGH`, `Inter EV tendre Chenille E`, `LOW`, `Locking Phase Duration`, `e EV Bloc delay`, `e HIGH SPEED`, `e LOW SPEED`, `e Landing Block Number`, `e Landing time bloking`

Seulement en T : `Force Lock`, `Force Unlock`, `HIGH arm`, `IDC EV By Pass`, `IDC EV By Pass Down`, `IDC EV By Pass sel`, `Inter Lock landing`, `Inter Tension`, `Inter Unlock`, `LOW arm`, `T Bloc`, `T EV tendre Chenille`, `T Locking Time`, `T Number of lockers`, `T Number of lockers custom`, `T Test Locker`, `T unLocking Time`, `Unlock landing`, `therm activ schema inter`, `therm show schema down`, `therm show schema inter`, `therm show schema up`

### `E EV Lock` ↔ `T EV Lock`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=e EV Bloc delay [ms] · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=E lock
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=Inter Lock landing
    Object group Blocking · Method=Or · Valid=True · Expression=
```

### `E EV Tension` ↔ `T EV Tension`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=IDC Tension
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=Inter Tension
    Object group Blocking · Method=Or · Valid=True · Expression=
```

### `E EV UnBlock` ↔ `T EV UnBlock`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=E unlock
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=Inter Unlock
    Object group Blocking · Method=Or · Valid=True · Expression=
```

### `IDC Tension` ↔ `IDC Tension`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=500 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=and · Operand 1=M3 - Run · Operand 2=Inter EV tendre Chenille E
      Single object B · Input=E Untingthen
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=And · Valid=True · Expression=
      Single object A · Input=T EV tendre Chenille
      Single object B · Input=T Inter EV By Pass
    Object group Blocking · Method=Or · Valid=True · Expression=
```

### `E Inter EV By Pass` ↔ `T Inter EV By Pass`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=Inter EV DOWN
      Single object B · Input=Inter EV UP
      Single object C · Input=IDC Tension
      Single object D · Input=EV lock mc 59
      Single object E · Input=HIGH
      Single object F · Input=LOW
      Single object G · Input=e Force EV By Pass
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=e Force EV By Pass
      Math object B · Operator=and · Operand 1=E Untingthen · Operand 2=A
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=500 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Latching And · Valid=True · Expression=
      Single object A · Input=IDC EV By Pass sel
      Single object B · Input=T Min Speed Ok
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=T Force EV By Pass
      Single object B · Input=T Untighten
      Math object C · Operator=and · Operand 1=A · Operand 2=B
      Math object D · Operator=not · Operand 1=IDC EV By Pass sel
```

### `Inter EV DOWN delay` ↔ `Inter EV DOWN delay`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=1000 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=And · Valid=True · Expression=
      Single object A · Input=DOWN E
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=1000 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=And · Valid=True · Expression=
      Single object A · Input=DOWN T
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=T Engine_Started mc
```

### `Inter EV UP Delay` ↔ `Inter EV UP Delay`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=1000 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=And · Valid=True · Expression=
      Single object A · Input=UP E
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=1000 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=And · Valid=True · Expression=
      Single object A · Input=UP T
    Object group Blocking · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=T Engine_Started mc
```

### `OK BLOC` ↔ `T OK BLOC`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=>= · Operand 1=Locking pressure mc 9 [bar] · Operand 2=90
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=>= · Operand 1=Locking pressure mc 9 [bar] · Operand 2=100
    Object group Blocking · Method=Or · Valid=True · Expression=
```

### `E OK UP/DOWN` ↔ `T OK UP/DOWN`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=5000 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=<= · Operand 1=Locking pressure mc 9 [bar] · Operand 2=10
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=T unLocking Time [ms] · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=<= · Operand 1=Locking pressure mc 9 [bar] · Operand 2=10
    Object group Blocking · Method=Or · Valid=True · Expression=
      Single object A · Input=T Untighten
      Single object B · Input=Force Lock
```

### `E State Up/Down` ↔ `T State Up/Down`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
State machine channel (SMC) · Default state name=Error
  Function DOWN
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=< · Operand 1=State Up/Down Raw · Operand 2=2
      Math object B · Operator=> · Operand 1=State Up/Down Raw · Operand 2=0
      Math object C · Operator=and · Operand 1=A · Operand 2=B
      Math object D · Operator== · Operand 1=State Up/Down Raw · Operand 2=0
    Object group Blocking · Method=Or · Valid=True · Expression=
      Single object A · Input=E Don'push button
  Function INTERMEDIATE
    Object group Activating · Method=And · Valid=True · Expression=
      Math object A · Operator=>= · Operand 1=State Up/Down Raw · Operand 2=2
      Math object B · Operator=<= · Operand 1=State Up/Down Raw · Operand 2=98
    Object group Blocking · Method=Or · Valid=True · Expression=
      Single object A · Input=E Don'push button
  Function UP
    Object group Activating · Method=And · Valid=True · Expression=
      Math object A · Operator=> · Operand 1=State Up/Down Raw · Operand 2=98
    Object group Blocking · Method=Or · Valid=True · Expression=
      Single object A · Input=E Don'push button
  Function UP AND BLOC
    Object group Activating · Method=And · Valid=True · Expression=
      Math object A · Operator=>= · Operand 1=State Up/Down Raw · Operand 2=99
      Single object B · Input=OK BLOC
    Object group Blocking · Method=Or · Valid=True · Expression=
      Single object A · Input=E Don'push button
```
**T**
```
State machine channel (SMC) · Default state name=Error
  Function DOWN
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=< · Operand 1=State Up/Down Raw · Operand 2=2
      Math object B · Operator=>= · Operand 1=State Up/Down Raw · Operand 2=0
      Math object C · Operator=and · Operand 1=A · Operand 2=B
      Math object D · Operator== · Operand 1=State Up/Down Raw · Operand 2=0
      Single object E · Input=UP T
      Math object F · Operator=and · Operand 1=D · Operand 2=E
    Object group Blocking · Method=Or · Valid=True · Expression=
      Single object A · Input=Don'push button
  Function INTERMEDIATE
    Object group Activating · Method=And · Valid=True · Expression=
      Math object A · Operator=>= · Operand 1=State Up/Down Raw · Operand 2=2
      Math object B · Operator=<= · Operand 1=State Up/Down Raw · Operand 2=98
    Object group Blocking · Method=Or · Valid=True · Expression=
      Single object A · Input=Don'push button
  Function UP
    Object group Activating · Method=And · Valid=True · Expression=
      Math object A · Operator=> · Operand 1=State Up/Down Raw · Operand 2=98
    Object group Blocking · Method=Or · Valid=True · Expression=
      Single object A · Input=Don'push button
  Function UP and bloc
    Object group Activating · Method=And · Valid=True · Expression=
      Math object A · Operator=>= · Operand 1=State Up/Down Raw · Operand 2=99
      Single object B · Input=T OK BLOC
    Object group Blocking · Method=Or · Valid=True · Expression=
      Single object A · Input=Don'push button
```

### `Timer clignotement schema inter` ↔ `Timer clignotement schema inter E`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Timer channel (TMR) · Type (Unit)=Seconds [s] · Store value=No · Reset value=0 · Function selector=Not used
  Function Default function
    Object group Increasing · Method=Or · Valid=True · Expression=
      Single object A · Input=Elec activ shema inter
    Object group Decreasing · Method=Or · Valid=True · Expression=
    Object group Resetting · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=Elec activ shema inter
```
**T**
```
Timer channel (TMR) · Type (Unit)=Seconds [s] · Store value=No · Reset value=0 · Function selector=Not used
  Function Default function
    Object group Increasing · Method=Or · Valid=True · Expression=
      Single object A · Input=therm activ schema inter
    Object group Decreasing · Method=Or · Valid=True · Expression=
    Object group Resetting · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=therm activ schema inter
```


## E.KeyBox x100 E / T.KeyBox x100 T

Seulement en E : `Charger Connected`, `Clignotement charge DCDC`, `E Force K3 Auto-off`, `E Full Fan Test`, `GFOUT-A:Generic`, `K1 Fan Rear / Fan mk E`, `K3 oldFan Exhaust / AutoOff`, `K4 Engine Power / Search Lights`, `K5 Engine Start`, `K6 DCDC Ignition`, `K7 Aux 2`, `mk E Program KeyBox x100`, `show fleche DCDC charging`

Seulement en T : `GFOUT-C:Generic`, `T Activate Exhaust`, `T Activate High Aft Fan`, `T Activate Low Aft Fan`, `T K1 Fan Rear / Fan`, `T K3 Fan Exhaust / AutoOff`, `T K4 Engine Power ON / Search Lights`, `T K5 Engine Starter`, `T K6 Engine Water Pump`, `T K7 Exhaust Water Pump`, `mk T Aft Fan Low Test`, `mk T Aft Fan Max Test`, `mk T Exhaust Fan Test`, `mk T Force Engine pump`, `mk T Force Exhaust pump`, `mk T Program KeyBox`

### `e CanBus Error mc` ↔ `T CanBus Error mc`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Error · Header, English=e1166 KeyBox E · Text, English=The KeyBox don't respond with the system, try a reboot to fix. · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=KeyBox E Can Ok
    Object group Hiding · Method=Or · Valid=True · Expression=
      Single object A · Input=KeyBox E Can Ok
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Error · Header, English=e1191 KeyBox · Text, English=The KeyBox don't respond with the system, try a reboot to fix. · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=KeyBox T Can Ok
    Object group Hiding · Method=Or · Valid=True · Expression=
      Single object A · Input=KeyBox T Can Ok
```

### `GFIN-A:Generic` ↔ `GFIN-A:Generic`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Generic frame in channel (GFIN) · Identifier=ID Fault · Data length=DonÂt care · Timeout=Not used · Paged protocol={Not used} · Parameters={{K1 Fault; 1}; {K2 Fault; 2}; {K3 Fault; 3}; {K4 Fault; 4}; {K5 Fault; 5}; {K6 Fault; 6}; {K7 Fault; 7}; {K8 Fault; 8}; {K9 Fault; 9}; {K10 Fault; 10}; {K11 Fault; 11}; {K12 Fault; 12}; {K13 Fault; 13}} · Module=Keybox X100 E (Generic) · Module index=0
```
**T**
```
Generic frame in channel (GFIN) · Identifier=ID Fault · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{K1 Fault; 1}; {K2 Fault; 2}; {K3 Fault; 3}; {K4 Fault; 4}; {K5 Fault; 5}; {K6 Fault; 6}; {K7 Fault; 7}; {K8 Fault; 8}; {K9 Fault; 9}; {K10 Fault; 10}; {K11 Fault; 11}; {K12 Fault; 12}; {K13 Fault; 13}} · Module=Keybox X100 T (Generic) · Module index=0
```

### `GFOUT-E:Generic` ↔ `GFOUT-E:Generic`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Generic frame out channel (GFOUT) · Identifier=0x20C · Data length=8 · Send method=On change · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{OFF_Bits_GOUT; 0}; {ON_Bits_GOUT; 16}} · Module=Keybox X100 E (Generic) · Module index=3
```
**T**
```
Generic frame out channel (GFOUT) · Identifier=0x20C · Data length=8 · Send method=On change · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{T OFF_Bits_GOUT; 0}; {T ON_Bits_GOUT; 16}} · Module=Keybox X100 T (Generic) · Module index=0
```

### `GFOUT-D:Generic` ↔ `GFOUT-D:Generic`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Generic frame out channel (GFOUT) · Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=Keybox X100 E (Generic) · Module index=2
```
**T**
```
Generic frame out channel (GFOUT) · Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=Keybox X100 T (Generic) · Module index=3
```

### `e K1 fuse is blown mc` ↔ `T K1 fuse is blown mc`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=e1016 K1 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K1 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=Keybox error: FH1 fuse is blown -> Call AfterSales · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K1 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `e K10 fuse is blown mc` ↔ `K10 fuse is blown mc T`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=e1196 K10 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K10 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header=Keybox error: FH10 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K10 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `e K11 fuse is blown mc` ↔ `K11 fuse is blown mc T`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=e1196 K11 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K11 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header=Keybox error: FH11 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K11 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `e K12 fuse is blown mc` ↔ `K12 fuse is blown mc T`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=e1067 K12 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K12 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header=Keybox error: FH12 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K12 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `e K13 fuse is blown mc` ↔ `K13 fuse is blown mc T`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=e1200 K13 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K13 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header=Keybox error: FH13 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K13 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `K2 Fan Super / Pump` ↔ `T K2 Fan Super / Pump`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=E water PUMP VAR
      Single object B · Input=E Full Fan Test
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Single object A · Input=T Activate High Aft Fan
      Single object B · Input=mk T Aft Fan Max Test
    Object group Blocking · Method=Or · Valid=True · Expression=
```

### `e K2 fuse is blown  mc` ↔ `T K2 fuse is blown mc`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=e1181 K2 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K2 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=Keybox error: FH2 fuse is blown -> Call AfterSales · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K2 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `e K3 fuse is blown  mc` ↔ `T K3 fuse is blown mc`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=e1049 K3 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K3 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=Keybox error: FH3 fuse is blown -> Call AfterSales · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K3 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `e K4 fuse is blown mc` ↔ `K4 fuse is blown mc T`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=e1149 K4 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K4 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header=Keybox error: FH5 fuse is blown -> Call AfterSales · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K4 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `e K5 fuse is blown mc` ↔ `K5 fuse is blown mc T`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=e1008 K5 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K5 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header=Keybox error: FH4 fuse is blown -> Call AfterSales · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K5 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `e K6 fuse is blown mc` ↔ `K6 fuse is blown mc T`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=e1177 K6 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K6 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header=Keybox error: FH6 fuse is blown -> Call AfterSales · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K6 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `e K7 fuse is blown mc` ↔ `K7 fuse is blown mc T`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=e1065 K7 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K7 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header=Keybox error: FH7 fuse is blown -> Call AfterSales · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K7 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `K8` ↔ `T K8`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=0 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=not · Operand 1=Inflate system battery low
    Object group Blocking · Method=Or · Valid=True · Expression=
```

### `e K8 fuse is blown mc` ↔ `K8 fuse is blown mc T`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=e1174 K8 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K8 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header=Keybox error: FH8 fuse is blown -> Call AfterSales · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K8 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `e K9 fuse is blown mc` ↔ `K9 fuse is blown mc T`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header, English=e1084 K9 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K9 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```
**T**
```
Conditional message channel (CMSG) · Show message=All · Dialog type=Alarm · Header=Keybox error: FH9 fuse is blown · Text= · Channel=Not used · Help= · Function selector=Not used
  Function Default function
    Object group Showing · Method=Or · Valid=True · Expression=
      Single object A · Input=K9 Fault
    Object group Hiding · Method=Or · Valid=True · Expression=
```

### `OFF_Bits` ↔ `T OFF_Bits`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Integer math channel (IMAC) · Unit=Not used · Function selector=Not used
  Function Default function
    | Result := bnot(ON_Bits) band 0x1FFF
```
**T**
```
Integer math channel (IMAC) · Unit=Not used · Function selector=Not used
  Function Default function
    | Result := bnot(T ON_Bits) band 0x1FFF
```

### `ON_Bits` ↔ `T ON_Bits`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Integer math channel (IMAC) · Unit=Not used · Function selector=Not used
  Function Default function
    | Result := K1 Fan Rear / Fan mk E * 1 + K2 Fan Super / Pump  * 2 + K3 oldFan Exhaust / AutoOff * 4 + K4 Engine Power / Search Lights * 8 + K5 Engine Start * 16 + K6 DCDC Ignition * 32 + K7 Aux 2 * 64 + K8 * 128 + K9 * 256 + K10 * 512 + K11 * 1024 + K12 * 2048 + K13 * 4096
```
**T**
```
Integer math channel (IMAC) · Unit=Not used · Function selector=Not used
  Function Default function
    | Result := T K1 Fan Rear / Fan * 1 + T K2 Fan Super / Pump  * 2 + T K3 Fan Exhaust / AutoOff * 4 + T K4 Engine Power ON / Search Lights * 8 + T K5 Engine Starter * 16 + T K6 Engine Water Pump * 32 + T K7 Exhaust Water Pump * 64 + T K8 * 128 + T K9 * 256 + T K10 * 512 + T K11 * 1024 + T K12 * 2048 + T K13 * 4096
```

### `Trigger HeartBeat` ↔ `Trigger HeartBeat`

Décision : ☐ garder E ☐ garder T ☐ réglage

**E**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=1000 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=PositiveFlank · Operand 1=mk E Program KeyBox x100
    Object group Blocking · Method=Or · Valid=True · Expression=
```
**T**
```
Internal digital channel (IDC) · Toggle=No · Delay on=0 · Delay off=1000 · Function selector=Not used
  Function Default function
    Object group Activating · Method=Or · Valid=True · Expression=
      Math object A · Operator=PositiveFlank · Operand 1=mk T Program KeyBox
    Object group Blocking · Method=Or · Valid=True · Expression=
```

