# MD45-ET app — Joystick md45

3 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Joystick md45 — actif seulement si `Joystick plugged md45`
> group disable by joystick plugged md4

#### Right Joystick ET45 C2:2  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-LST · Calibration={500; 4500; -100; 100} · Alarms={No; 0; No; 100} · Module=MD45-ET-39 (MD4-5[1]) · Module index=1
- Utilisé par : `Right Joystick ET45 CanOut`, `Dual adjust item: Right Joystick`, `Measure group: Translation`
- Ligne export : 117909 · id 180542

#### Right Joystick ET45 CanOut  `APPOUT`
- Propriétés : Input channel=Right Joystick ET45 C2:2 [%] · Send method=Continuously · Transmit rate=100
- Lit : `Right Joystick ET45 C2:2`
- Utilisé par : `Right Joystick ET45 C2:2 APPIN`
- Ligne export : 117933 · id 216203

#### Left Joystick ET45 CanOut  `APPOUT`
- Propriétés : Input channel=Left Joy ET45 ou water level C2:1 [%] · Send method=Continuously · Transmit rate=100
- Lit : `Left Joy ET45 ou water level C2:1`
- Utilisé par : `Left Joy ET45 ou water level C2:1 APPIN`
- Ligne export : 117944 · id 216204
