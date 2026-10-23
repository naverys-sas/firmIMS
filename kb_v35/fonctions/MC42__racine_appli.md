# MC42 — (racine appli)

22 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## (racine)

#### Drive Type  `SP`
- Propriétés : Input channel=None · Default state name=Thermique · States={Electric}
- Utilisé par : `Drive Type`, `IDC Tension`, `Is_Electric`, `Is_Thermic`, `PIN 44`, `Power State Int`, `Adjust group: Master Config`, `Single adjust item: Drive Type`
- Ligne export : 10085 · id 36189

#### Status:MC42[1]  `MDGN`
- Propriétés : Value=Module status · Module=MC42 (MC42[1]) · Module index=0
- Utilisé par : `PARKER OK`
- Ligne export : 14964 · id 32508

#### Is_Thermic  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Drive Type = 0`
- Lit : ``, `Drive Type`
- Utilisé par : `Active le groupe: Thermic`, `Adjust group: Master Pump`, `Adjust group: Master Thermic`, `Event log: Thermic Events`, `Measure group: Engine Thermic`, `Measure group: Engine and Translation`, `Measure group: Hydraulic`, `Single adjust item: 2200 tr/min`, `Single adjust item: Ambiante Temperature`, `Single adjust item: Backward - direct corrector`, `Single adjust item: ECU Engine`, `Single adjust item: Engine type`, `Single adjust item: Forward - direct corrector`, `Single adjust item: Fuel line ignition State`, `Single adjust item: Full Fan Mode`, `Single adjust item: Start Pulse`, `Statistics log: Thermic Stats`
- Ligne export : 14975 · id 36195

#### MD3_Start/Stop  `APPIN`
- Propriétés : Input channel=Can Out Button F1
- Lit : `Can Out Button F1`
- Utilisé par : `Joystick to zero CMSG`, `MD3 START`, `MD3 STOP`, `MD4 - Start Button Blocking Neutral`
- Ligne export : 15020 · id 54459

#### S/N:MC42[1]  `MDGN`
- Propriétés : Value=Serial number · Module=MC42 (MC42[1]) · Module index=1
- Utilisé par : *(personne)*
- Ligne export : 21195 · id 32510

#### Address:MC42[1]  `MDGN`
- Propriétés : Value=Id tag · Module=MC42 (MC42[1]) · Module index=3
- Utilisé par : *(personne)*
- Ligne export : 21206 · id 32513

#### Temp:MC42[1]  `MDGN`
- Propriétés : Value=Temperature [Â°C] · Module=MC42 (MC42[1]) · Module index=2
- Lit : `C`
- Utilisé par : *(personne)*
- Ligne export : 21217 · id 32514

#### VREF-A:MC42[1]  `MDGN`
- Propriétés : Value=Reference voltage A · Module=MC42 (MC42[1]) · Module index=5
- Utilisé par : `Measure group: System Monitoring`
- Ligne export : 21228 · id 32515

#### 12V Batt.  `MDGN`
- Propriétés : Value=Supply voltage [V] · Module=MC42 (MC42[1]) · Module index=4
- Utilisé par : `Charge`, `Need to Charge Voltage`, `Need to charge`, `Measure group: System Monitoring`
- Ligne export : 21239 · id 32516

#### Need to charge  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=1000
- Logique :
  - **Activating** = `12V Batt. [V] < 11,8`
- Lit : ``, `12V Batt.`
- Utilisé par : `Batterie State`
- Ligne export : 21250 · id 33014

#### Charge  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=3000
- Logique :
  - **Activating** = `12V Batt. [V] > 13`
- Lit : ``, `12V Batt.`
- Utilisé par : `Batterie State`
- Ligne export : 21295 · id 33022

#### Batterie State  `SMC`
- Propriétés : Default state name=Normal
- Fonction *Charge* :
  - **Activating** = `Charge`
- Fonction *Need to charge* :
  - **Activating** = `Need to charge`
- Lit : ``, `Charge`, `Need to charge`
- Utilisé par : `MD3 page: BASE`
- Ligne export : 21340 · id 33030

#### Is_Electric  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Drive Type = 1`
- Lit : ``, `Drive Type`
- Utilisé par : `Active le groupe: Electric`, `Adjust group: Master Battery`, `Adjust group: Master Electric`, `Adjust group: Setup Charger`, `Event log: Battery Isolation`, `Event log: Electronic Logs`, `Measure group: CanBus`, `Measure group: Electric Engine`, `Single adjust item: Auto Charge 12V`, `Single adjust item: Battery Brand`, `Single adjust item: Battery Force`, `Single adjust item: Charger Brand`, `Single adjust item: Charging Force`, `Single adjust item: Engine - Force Ready`, `Single adjust item: Force Bat Reset`, `Single adjust item: M-Track - Brand Main`, `Single adjust item: Max Speed`, `Single adjust item: Power Controler Force`, `Single adjust item: Speed Hydro Force`, `Single adjust item: Variator Force`, `Statistics log: Electric Stats`
- Ligne export : 21411 · id 36206

#### Tension to charge  `FP`
- Propriétés : Default mode={11,9}
- Utilisé par : `Need to Charge Voltage`, `Adjust group: Master Battery`, `Single adjust item: Tension to charge`
- Ligne export : 21456 · id 54570

#### Need to Charge Voltage  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((Inside(12V Batt. [V], 2, Tension to charge)))) OR (Need to Charge Voltage)`
  - **Blocking** = `12V Batt. [V] > 13,2`
- Lit : ``, `12V Batt.`, `Tension to charge`
- Utilisé par : `Need to Charge Voltage Wait`
- Ligne export : 21468 · id 54571

#### Auto Charge 12V  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `Need to Charge Voltage Wait`, `Adjust group: Setup`, `Single adjust item: Auto Charge 12V`
- Ligne export : 21538 · id 54582

#### Need to Charge Voltage Wait  `IDC`
- Propriétés : Toggle=No · Delay on=100000 · Delay off=100000
- Logique :
  - **Activating** = `Need to Charge Voltage`
  - **Blocking** = `not(Auto Charge 12V)`
- Lit : ``, `Auto Charge 12V`, `Need to Charge Voltage`
- Utilisé par : `Need to Charge IDC - Public`
- Ligne export : 21551 · id 54583

#### Need to Charge IDC - Public  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `Need to Charge Voltage Wait`
- Lit : ``, `Need to Charge Voltage Wait`
- Utilisé par : `Battery CMD`
- Ligne export : 21602 · id 54592

#### PIN 44  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Drive Type
- Fonction *Thermique* :
  - **Activating** = `Inter EV Frein`
- Fonction *Electric* :
  - **Activating** = `(BATT - Reset) OR (Force Bat Reset)`
- Lit : ``, `BATT - Reset`, `Drive Type`, `Force Bat Reset`, `Inter EV Frein`
- Utilisé par : `Pin 44 (Brake/Batt HT)`
- Ligne export : 48071 · id 54870

#### Pin 44 (Brake/Batt HT)  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=PIN 44 · Module=MC42 (MC42[1]) · Module index=14
- Lit : `PIN 44`
- Utilisé par : *(personne)*
- Ligne export : 48152 · id 54869

#### Proemion  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Active le groupe: Proemion`, `Adjust group: Master Config`, `Measure group: Proemion`, `Single adjust item: Proemion`
- Ligne export : 50198 · id 61696

#### Force Bat Reset  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `PIN 44`, `Adjust group: Master Features`, `Single adjust item: Force Bat Reset`
- Ligne export : 50710 · id 63156
