# MD3 — PIN

17 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## PIN

#### F1  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Counter`, `Touch Value`, `MD3 page: PIN`
- Ligne export : 8987 · id 33416

#### F2  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Counter`, `Touch Value`, `MD3 page: PIN`
- Ligne export : 8997 · id 33417

#### F3  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Counter`, `Touch Value`, `MD3 page: PIN`
- Ligne export : 9007 · id 33418

#### F4  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Counter`, `Touch Value`, `MD3 page: PIN`
- Ligne export : 9017 · id 33419

#### Number 1  `IP`
- Propriétés : Default mode={1}
- Utilisé par : `PIn State`, `Adjust group: Setup PIN`, `Single adjust item: Number 1`
- Ligne export : 9027 · id 33420

#### Number 2  `IP`
- Propriétés : Default mode={1}
- Utilisé par : `PIn State`, `Adjust group: Setup PIN`, `Single adjust item: Number 2`
- Ligne export : 9039 · id 33421

#### Number 3  `IP`
- Propriétés : Default mode={1}
- Utilisé par : `PIn State`, `Adjust group: Setup PIN`, `Single adjust item: Number 3`
- Ligne export : 9051 · id 33422

#### Number 4  `IP`
- Propriétés : Default mode={1}
- Utilisé par : `PIn State`, `Adjust group: Setup PIN`, `Single adjust item: Number 4`
- Ligne export : 9063 · id 33423

#### Start PIN  `DP`
- Propriétés : True text=Active · False text=Unactive · Default mode={False}
- Utilisé par : `Unlock`, `Adjust group: Setup PIN`, `Single adjust item: Number 1`, `Single adjust item: Number 2`, `Single adjust item: Number 3`, `Single adjust item: Number 4`, `Single adjust item: Start PIN`
- Ligne export : 9075 · id 33424

#### Touch Value  `IMAC`
- Logique :
  ```qcode
  Result := F1*1 + F2*2 + F3*3 + F4*4
  ```
- Lit : `F1`, `F2`, `F3`, `F4`
- Utilisé par : `PIn State`
- Ligne export : 9088 · id 33425

#### Reset  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Counter > 4) OR ((Counter = 4) and Lock)`
- Lit : ``, `Counter`, `Lock`
- Utilisé par : `Counter`, `PIn State`
- Ligne export : 9106 · id 33441

#### Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(F1) OR PositiveFlank(F2) OR PositiveFlank(F3) OR PositiveFlank(F4)`
  - **Resetting** = `PositiveFlank(Reset)`
- Lit : ``, `F1`, `F2`, `F3`, `F4`, `Reset`
- Utilisé par : `PIn State`, `Reset`, `Text State`
- Ligne export : 9169 · id 33451

#### Unlock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((PIn State = 4))) OR Unlock OR (not(Start PIN))`
- Lit : ``, `PIn State`, `Start PIN`
- Utilisé par : `Lock`, `VIEW START PAGE`, `Adjust group: Setup PIN`, `MD3 page: PIN`, `MD3 page: Thermic`
- Ligne export : 9253 · id 33465

#### Lock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Unlock)`
- Lit : ``, `Unlock`
- Utilisé par : `Reset`, `VIEW ENGINE RUN PAGE`, `VIEW START PAGE`, `MD3 page: PIN`, `MD3 page: Thermic`
- Ligne export : 9321 · id 33476

#### PIn State  `FSM`
- Propriétés : Store value=No · Resetting channel=Reset
- État 0 **Default state**
  - transition *0 - 1* (état cible non exporté par IQANdesign)
    - **Activating** = `(Touch Value = Number 1) AND (Counter = 1)`
- État 1 **State 1**
  - transition *1 - 2* (état cible non exporté par IQANdesign)
    - **Activating** = `(Touch Value = Number 2) AND (Counter = 2)`
- État 2 **State 2**
  - transition *2 - 3* (état cible non exporté par IQANdesign)
    - **Activating** = `(Touch Value = Number 3) AND (Counter = 3)`
- État 3 **State 3**
  - transition *3 - 4* (état cible non exporté par IQANdesign)
    - **Activating** = `(Touch Value = Number 4) AND (Counter = 4)`
- État 4 **State 4**
- Lit : ``, `Counter`, `Number 1`, `Number 2`, `Number 3`, `Number 4`, `Reset`, `Touch Value`
- Utilisé par : `Unlock`
- Ligne export : 9365 · id 33484

#### Text State  `SP`
- Propriétés : Input channel=Counter · Default state name=1 · States={2; 3; 4; 5}
- Lit : `Counter`
- Utilisé par : `Text ****`
- Ligne export : 9561 · id 33519

#### Text ****  `TP`
- Propriétés : Mode selector=Text State · Default mode: 1={} · Mode 1: 2={*} · Mode 2: 3={* *} · Mode 3: 4={* * *} · Mode 4: 5={* * * *}
- Lit : `Text State`
- Utilisé par : `MD3 page: PIN`
- Ligne export : 9576 · id 33524
