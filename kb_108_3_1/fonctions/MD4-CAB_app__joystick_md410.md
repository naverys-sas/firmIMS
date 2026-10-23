# MD4-CAB app — joystick md410

4 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## joystick md410 — actif seulement si `Joystick plugged md10`

#### Left Joystick C41 C2:1  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-LST · Calibration={500; 4500; -100; 100} · Alarms={No; 0; No; 100} · Module=MD4-CAB-40 (MD4-10[2]) · Module index=0
- Utilisé par : `Left Joystick C10 CanOut`, `Adjust group: Master Tracks`, `Dual adjust item: Left Joystick C41 C2:1`, `Measure group: Translation`
- Ligne export : 113963 · id 217475

#### Right Joystick C41 C2:2  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-LST · Calibration={500; 4500; -100; 100} · Alarms={No; 0; No; 100} · Module=MD4-CAB-40 (MD4-10[2]) · Module index=1
- Utilisé par : `Right Joystick C10 CanOut`, `Adjust group: Master Tracks`, `Dual adjust item: Right Joystick C41 C2:2`, `Measure group: Translation`
- Ligne export : 113987 · id 217529

#### Right Joystick C10 CanOut  `APPOUT`
- Propriétés : Input channel=Right Joystick C41 C2:2 [%] · Send method=Continuously · Transmit rate=100
- Lit : `Right Joystick C41 C2:2`
- Utilisé par : `Right Joystick C41 C2:2 APPIN`
- Ligne export : 114011 · id 223337

#### Left Joystick C10 CanOut  `APPOUT`
- Propriétés : Input channel=Left Joystick C41 C2:1 [%] · Send method=Continuously · Transmit rate=100
- Lit : `Left Joystick C41 C2:1`
- Utilisé par : `Left Joystick C41 C2:1 APPIN`
- Ligne export : 114022 · id 223339
