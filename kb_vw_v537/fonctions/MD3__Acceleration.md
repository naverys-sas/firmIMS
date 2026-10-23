# MD3 — Acceleration

10 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Acceleration — actif seulement si `Acceleration`

#### X  `VIN`
- Propriétés : Unit=g · Reference voltage=Reference voltage A · Error value=0 · Calibration={500; 4500; -16; 16} · Alarms={No; 0; No; 100} · Module=MD3[0] · Module index=4
- Lit : ``
- Utilisé par : `Sum Cube`, `Measure group: Acceleration`
- Ligne export : 8868 · id 21828

#### Y  `VIN`
- Propriétés : Unit=g · Reference voltage=Reference voltage A · Error value=0 · Calibration={500; 4500; -16; 16} · Alarms={No; 0; No; 100} · Module=MD3[0] · Module index=5
- Lit : ``
- Utilisé par : `Sum Cube`, `Measure group: Acceleration`
- Ligne export : 8892 · id 21829

#### Z  `VIN`
- Propriétés : Unit=g · Reference voltage=Reference voltage A · Error value=0 · Calibration={500; 4500; -16; 16} · Alarms={No; 0; No; 100} · Module=MD3[0] · Module index=6
- Lit : ``
- Utilisé par : `Sum Cube`, `Measure group: Acceleration`
- Ligne export : 8916 · id 21830

#### Sum Cube  `MAC`
- Propriétés : Unit=g
- Logique :
  ```qcode
  Result := Sqrt (PowerOf(X,2) + PowerOf(Y, 2) + PowerOf  (Z,2))
  ```
- Lit : `X`, `Y`, `Z`
- Utilisé par : `10-12g`, `12-14g`, `14-16g`, `4-6g`, `6-8g`, `8-10g`
- Ligne export : 8940 · id 21894

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
- Utilisé par : `Event log: Acceleration`
- Ligne export : 8958 · id 21959

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
- Ligne export : 8982 · id 21992

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
- Ligne export : 9006 · id 22025

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
- Ligne export : 9030 · id 22058

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
- Ligne export : 9054 · id 22091

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
- Ligne export : 9078 · id 22124
