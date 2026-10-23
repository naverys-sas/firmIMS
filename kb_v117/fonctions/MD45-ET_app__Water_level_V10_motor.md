# MD45-ET app — Water level V10 motor

2 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Water level V10 motor

#### Left Joy ET45 ou water level C2:1  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-LST · Calibration={500; 4500; -100; 100} · Alarms={No; 0; No; 100} · Module=MD45-ET-39 (MD4-5[1]) · Module index=0
- Utilisé par : `Calibration water level motor V10`, `Left Joystick ET45 CanOut`, `Dual adjust item: Left Joystick`, `Measure group: Translation`
- Ligne export : 115185 · id 180488

#### Calibration water level motor V10  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe(Left Joy ET45 ou water level C2:1 [%]: {{-95; 100}; {87; 0}}, Freeze)`
- Lit : `Left Joy ET45 ou water level C2:1`
- Utilisé par : `MD4-5 page: INFO`
- Ligne export : 115209 · id 239985
