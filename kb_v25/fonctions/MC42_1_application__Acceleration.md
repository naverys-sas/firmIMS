# MC42[1] application — Acceleration

11 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Acceleration — actif seulement si `Acceleration Sensor`

#### X  `VIN`
- Propriétés : Unit=g · Reference voltage=Reference voltage A · Error value=0 · Calibration={500; 4500; -16; 16} · Alarms={No; 0; No; 100} · Module=MC42[1] · Module index=5
- Utilisé par : `Sum Cube`, `Measure group: Acceleration`
- Ligne export : 67332 · id 42659

#### Y  `VIN`
- Propriétés : Unit=g · Reference voltage=Reference voltage A · Error value=0 · Calibration={500; 4500; -16; 16} · Alarms={No; 0; No; 100} · Module=MC42[1] · Module index=6
- Utilisé par : `Sum Cube`, `Measure group: Acceleration`
- Ligne export : 67356 · id 42660

#### Z  `VIN`
- Propriétés : Unit=g · Reference voltage=Reference voltage A · Error value=0 · Calibration={500; 4500; -16; 16} · Alarms={No; 0; No; 100} · Module=MC42[1] · Module index=7
- Utilisé par : `Sum Cube`, `Measure group: Acceleration`
- Ligne export : 67380 · id 42661

#### Sum Cube  `MAC`
- Propriétés : Unit=g
- Logique :
  ```qcode
  Result := Sqrt (PowerOf(X,2) + PowerOf(Y, 2) + PowerOf  (Z,2))
  ```
- Lit : `X`, `Y`, `Z`
- Utilisé par : `10-12g`, `12-14g`, `14-16g`, `2-4g`, `4-6g`, `6-8g`, `8-10g`
- Ligne export : 67404 · id 42662

#### 2-4g  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  if (Sum Cube  >=  2 and Sum Cube  <4) then
    Result:= 1
  else
    Result:= 0
  endif
  ```
- Lit : `Sum Cube`
- Utilisé par : *(personne)*
- Ligne export : 67422 · id 42677

#### 4-6g  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  if (Sum Cube  >=  4 and Sum Cube  <6) then
    Result:= 1
  else
    Result:= 0
  endif
  ```
- Lit : `Sum Cube`
- Utilisé par : *(personne)*
- Ligne export : 67446 · id 42692

#### 6-8g  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  if (Sum Cube  >=  6 and Sum Cube  <8) then
    Result:= 1
  else
    Result:= 0
  endif
  ```
- Lit : `Sum Cube`
- Utilisé par : `Event log: Acceleration`
- Ligne export : 67470 · id 42707

#### 8-10g  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  if (Sum Cube  >=  8 and Sum Cube  <10) then
    Result:= 1
  else
    Result:= 0
  endif
  ```
- Lit : `Sum Cube`
- Utilisé par : `Event log: Acceleration`
- Ligne export : 67494 · id 42722

#### 10-12g  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  if (Sum Cube  >=  10 and Sum Cube  < 12) then
    Result:= 1
  else
    Result:= 0
  endif
  ```
- Lit : `Sum Cube`
- Utilisé par : `Event log: Acceleration`
- Ligne export : 67518 · id 42737

#### 12-14g  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  if (Sum Cube  >=  12 and Sum Cube  < 14) then
    Result:= 1
  else
    Result:= 0
  endif
  ```
- Lit : `Sum Cube`
- Utilisé par : `Event log: Acceleration`
- Ligne export : 67542 · id 42752

#### 14-16g  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  if (Sum Cube  >=  14 and Sum Cube  < 16) then
    Result:= 1
  else
    Result:= 0
  endif
  ```
- Lit : `Sum Cube`
- Utilisé par : `Event log: Acceleration`
- Ligne export : 67566 · id 42767
