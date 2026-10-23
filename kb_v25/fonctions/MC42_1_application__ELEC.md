# MC42[1] application — ELEC

882 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## ELEC

#### Variator Force  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `VARIATOR SUPER ON`, `Adjust group: Master Features`, `Single adjust item: Variator Force`
- Ligne export : 31137 · id 36990

#### Start Button MD4  `APPIN`
- Propriétés : Input channel=Start Button
- Lit : `Start Button`
- Utilisé par : `Joystick to zero CMSG`, `MD4 - Start Button Blocking Neutral`
- Ligne export : 31150 · id 77886

#### MD4 - Start Button Blocking Neutral  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MD4 - Start Button Blocking Neutral) OR (Joystick to zero and (PositiveFlank(Start Button MD4)))`
  - **Blocking** = `NegativeFlank(Start Button MD4)`
- Lit : `Joystick to zero`, `Start Button MD4`
- Utilisé par : `BUTTON DRIVE`, `Charger State Finite`, `VARIATOR ON`
- Ligne export : 31159 · id 48947

#### HVLP Pump Test  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Test Mode`, `VARIATOR ON`, `Adjust group: Master Features`, `Single adjust item: HVLP Pump Test`
- Ligne export : 31227 · id 53775

#### Power Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Power Down Input >= 1`
- Lit : `Power Down Input`
- Utilisé par : `Battery DIGITAL`, `VARIATOR ON`
- Ligne export : 31240 · id 57269

#### VARIATOR ON  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MD4 - Start Button Blocking Neutral) OR (HVLP Pump Test)`
  - **Blocking** = `Power Down`
- Lit : `HVLP Pump Test`, `MD4 - Start Button Blocking Neutral`, `Power Down`
- Utilisé par : `Engine STATE`, `Joystick to zero CMSG`, `VARIATOR SUPER ON`, `VARIATOR Wait OFF`, `Variator hour`, `Wait batt ON`, `Statistics log: Stat Log`
- Ligne export : 31285 · id 36157

#### Wait batt ON  `IDC`
- Propriétés : Toggle=No · Delay on=25000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR ON`
- Lit : `VARIATOR ON`
- Utilisé par : *(personne)*
- Ligne export : 31342 · id 48242

#### MDGN-Status:MC2[1]  `MDGN`
- Propriétés : Value=Module status · Module=MC42[1] · Module index=0
- Utilisé par : `PARKER OK`
- Ligne export : 31385 · id 36206

#### PARKER OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=20
- Logique :
  - **Activating** = `(64 = MDGN-Status:MC2[1]) AND (64 = MD4-10 Status CAN In)`
- Lit : `MD4-10 Status CAN In`, `MDGN-Status:MC2[1]`
- Utilisé par : `Battery DIGITAL`
- Ligne export : 31396 · id 36208

#### Battery Force  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Battery DIGITAL`, `Adjust group: Master Features`, `Single adjust item: Battery Force`
- Ligne export : 31450 · id 46848

#### VARIATOR Wait OFF  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  - **Activating** = `VARIATOR ON`
- Lit : `VARIATOR ON`
- Utilisé par : `Battery DIGITAL`
- Ligne export : 31463 · id 49509

#### Battery Power Force  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `IDC - BATT`, `Adjust group: Master Features`, `Single adjust item: Battery Power Force`
- Ligne export : 31506 · id 84617

#### IDC - BATT  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Battery Error Durring 5 s`
  - **Blocking** = `Battery Power Force`
- Lit : `Battery Error Durring 5 s`, `Battery Power Force`
- Utilisé par : `Batt Reset`, `Battery DIGITAL`
- Ligne export : 31519 · id 52445

#### Battery DIGITAL  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Battery start by charger) OR (Battery Force) OR (VARIATOR Wait OFF) OR (Need to Charge IDC - Public)`
  - **Blocking** = `(not(PARKER OK)) OR (Power Down) OR (IDC - BATT)`
- Lit : `Battery Force`, `Battery start by charger`, `IDC - BATT`, `Need to Charge IDC - Public`, `PARKER OK`, `Power Down`, `VARIATOR Wait OFF`
- Utilisé par : `Battery CMD`
- Ligne export : 31569 · id 36217

#### VARIATOR SUPER ON  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `((Battery STATE >= 3) and VARIATOR ON) OR (Variator Force)`
- Lit : `Battery STATE`, `VARIATOR ON`, `Variator Force`
- Utilisé par : `Emmergency Stop Left`, `Emmergency Stop Right`, `ON/OFF Var`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `Var Power`, `Active le groupe: ELEC / MOTORS / M-Hydrau`, `Active le groupe: ELEC / MOTORS / M-Tracks`
- Ligne export : 47214 · id 36991

#### Joystick to zero CMSG  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Tracks · Text=Please put joysticks in neutral position before start engine.
- Logique :
  - **Showing** = `(PositiveFlank(Start Button MD4)) AND (not(Joystick to zero)) AND (not(VARIATOR ON))`
- Lit : `Joystick to zero`, `Start Button MD4`, `VARIATOR ON`
- Utilisé par : *(personne)*
- Ligne export : 59990 · id 37746

#### Battery State  `SP`
- Propriétés : Input channel=Battery STATE · Default state name=OFF · States={ERROR; READY; RUN; RUN ECO}
- Lit : `Battery STATE`
- Utilisé par : `Battery State`
- Ligne export : 60053 · id 37796

#### Charger STATE  `SP`
- Propriétés : Input channel=Charger STATE · Default state name=OFF · States={ERROR; READY; RUN 220V}
- Lit : `Charger STATE`
- Utilisé par : `Charger STATE`
- Ligne export : 60068 · id 37797

#### Variator hour  `TMR`
- Propriétés : Type (Unit)=Hours [h] · Store value=Yes · Reset value=10
- Logique :
  - **Decreasing** = `VARIATOR ON`
  - **Resetting** = `Variator hour [h] <= 0`
- Lit : `VARIATOR ON`
- Utilisé par : `10 hours check-up`
- Ligne export : 60114 · id 37915

#### 10 hours check-up  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header=check-up · Text=10hours IMS use since last check-up reminder. Please run through a boat inspection. Refer to boat handbook or contact your service center.
- Logique :
  - **Showing** = `Variator hour [h] <= 0`
- Lit : `Variator hour`
- Utilisé par : `Event log: Electronic Logs`
- Ligne export : 60175 · id 37926

#### Batt Reset  `DOUT`
- Propriétés : Delay on=0 · Delay off=1000 · Input channel=IDC - BATT · Module=MC42[1] · Module index=15
- Lit : `IDC - BATT`
- Utilisé par : *(personne)*
- Ligne export : 60223 · id 52457

#### Power Controler Force  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Var Power`, `Adjust group: Master Features`, `Single adjust item: Power Controler Force`
- Ligne export : 60236 · id 77903

#### Var Power  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(VARIATOR SUPER ON) OR (Power Controler Force)`
- Lit : `Power Controler Force`, `VARIATOR SUPER ON`
- Utilisé par : `Var Power`
- Ligne export : 60249 · id 69781

#### Var Power  `DOUT`
- Propriétés : Delay on=500 · Delay off=0 · Input channel=Var Power · Module=MC42[1] · Module index=14
- Lit : `Var Power`
- Utilisé par : *(personne)*
- Ligne export : 60299 · id 52460

#### Engine State  `SP`
- Propriétés : Input channel=Engine STATE · Default state name=OFF · States={STARTING; READY; ERROR}
- Lit : `Engine STATE`
- Utilisé par : `Engine State`
- Ligne export : 60312 · id 74999

#### Engines Not Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engines Not Ready`
- Lit : `Engines Not Ready`
- Utilisé par : `Engine Stop Fonction Output`
- Ligne export : 60326 · id 75003

## ELEC / BATTERY

#### Battery CMD  `FGI`
- Propriétés : Input type=Digital · Input=Battery DIGITAL · Default state name=OFF
- Lit : `Battery DIGITAL`
- Utilisé par : `Main Switch Battery`
- Ligne export : 31673 · id 36235

#### Main Switch Battery  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Battery CMD) AND (Start 3 s) AND (CanOn Wait)`
  - **Blocking** = `(Battery HIGHT TEMP) OR (Battery ERROR DIGIT) OR (Wait during start) OR (IDC Battery Protection)`
- Lit : `Battery CMD`, `Battery ERROR DIGIT`, `Battery HIGHT TEMP`, `CanOn Wait`, `IDC Battery Protection`, `Start 3 s`, `Wait during start`
- Utilisé par : `Bat CMD`, `Charge Mode`, `If not start`, `Switch Battery`, `Switch Battery`, `Wait during start`
- Ligne export : 31684 · id 36321

#### Wait during start  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  - **Activating** = `NegativeFlank(Main Switch Battery)`
- Lit : `Main Switch Battery`
- Utilisé par : `Main Switch Battery`
- Ligne export : 31769 · id 36333

#### Battery max temp  `IP`
- Propriétés : Unit=Â°C · Default mode={55}
- Utilisé par : `Battery HIGHT TEMP`, `Adjust group: Master Battery`, `Single adjust item: Battery max temp`
- Ligne export : 31813 · id 36284

#### Cell_T_max_Master  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - Cell_T_max_Master [Â°C]`
- Fonction *BMW* :
  - **Controlling** = `BMW - Cell_T_max_Master [Â°C]`
- Fonction *WattApls* :
  - **Controlling** = `WattAlps - Cell_T_max_Master [Â°C]`
- Lit : `BMW - Cell_T_max_Master`, `Battery Brand`, `Kreisel - Cell_T_max_Master`, `WattAlps - Cell_T_max_Master`
- Utilisé par : `Battery ECO MODE`, `Battery HIGHT TEMP`, `MD4-10 page: INFO`, `Measure group: Battery Kreisel`, `Statistics log: Stat Log`
- Ligne export : 31825 · id 36287

#### Battery HIGHT TEMP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Cell_T_max_Master [Â°C] >= Battery max temp [Â°C]`
- Lit : `Battery max temp`, `Cell_T_max_Master`
- Utilisé par : `Battery NEED TO CHARGE`, `Main Switch Battery`
- Ligne export : 31929 · id 36295

#### Battery ERROR DIGIT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `(Kreisel - ERROR DIGIT) OR (BMW - ERROR DIGIT) OR (WattApls- ERROR DIGIT)`
- Lit : `BMW - ERROR DIGIT`, `Kreisel - ERROR DIGIT`, `WattApls- ERROR DIGIT`
- Utilisé par : `Battery Error Durring 5 s`, `Battery NEED TO CHARGE`, `Battery STATE`, `Main Switch Battery`
- Ligne export : 31974 · id 36305

#### Start 3 s  `IDC`
- Propriétés : Toggle=No · Delay on=3000 · Delay off=0
- Logique :
  - **Activating** = `True`
- Utilisé par : `Main Switch Battery`
- Ligne export : 32031 · id 36313

#### Battery CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `(Kreisel - CAN OK) OR (BMW CAN OK) OR (WattAlps - CAN OK)`
- Lit : `BMW CAN OK`, `Kreisel - CAN OK`, `WattAlps - CAN OK`
- Utilisé par : `Battery NEED TO CHARGE`, `Battery STATE`, `CanOn Wait`, `IDC Battery Protection`, `MD4-10 page: INFO`
- Ligne export : 32074 · id 36350

#### CanOn Wait  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Battery CAN OK`
- Lit : `Battery CAN OK`
- Utilisé par : `Main Switch Battery`
- Ligne export : 32131 · id 53575

#### BMS_Iso_Resist  `MAC`
- Propriétés : Unit=kOhm · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - Iso_Resist [kOhm]`
- Fonction *BMW* :
  - **Controlling** = `BMW - Iso_Resist [kOhm]`
- Fonction *WattApls* :
  - **Controlling** = `WattAlps - Iso_Resist [kOhm]`
- Lit : `BMW - Iso_Resist`, `Battery Brand`, `Kreisel - Iso_Resist`, `WattAlps - Iso_Resist`
- Utilisé par : `Battery Protection`, `Flag Ground Fault Detection`, `Ground Fault message`, `IDC Battery Protection`, `Iso Resist`, `Event log: Battery Isolation`, `MD4-10 page: INFO`, `Measure group: Battery Kreisel`
- Ligne export : 32174 · id 36619

#### Battery Protection  `MEM`
- Propriétés : Input channel=Battery Protection · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : `Battery Protection`, `Reset Startup`
- Utilisé par : `IDC Battery Protection`, `Adjust group: Maintenance`, `Single adjust item: Battery Protection`
- Ligne export : 32278 · id 59007

#### IDC Battery Protection  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `(Battery CAN OK) AND (BMS_Iso_Resist [kOhm] <= Battery Protection Level [KOhm]) AND (0 = Battery Protection)`
  - **Blocking** = `BMS_Iso_Resist [kOhm] = 0`
- Lit : `BMS_Iso_Resist`, `Battery CAN OK`, `Battery Protection`, `Battery Protection Level`
- Utilisé par : `Battery Protection`, `Error Iso_Resist`, `Main Switch Battery`
- Ligne export : 32321 · id 59015

#### Battery Brand  `SP`
- Propriétés : Input channel=None · Default state name=Kreisel · States={BMW; WattApls}
- Utilisé par : `BMS_Iso_Resist`, `BMS_U_Trac`, `Battery InstantVoltage`, `Battery SOC`, `Cell_T_max_Master`, `Current Bat`, `Desired Voltage`, `Flag Ground Fault Detection`, `HighCellVoltage`, `Is BMW`, `Is Kreisel`, `Is WattAlps`, `LowCellVoltage`, `Max Discharge`, `Adjust group: Config Electric Drive`, `Single adjust item: Battery Brand`
- Ligne export : 32391 · id 67686

#### Battery Protection  `SP`
- Propriétés : Input channel=None · Default state name=True · States={False}
- Utilisé par : `Battery Protection`, `IDC Battery Protection`, `Adjust group: Maintenance`, `Single adjust item: Battery Protection`
- Ligne export : 32404 · id 59026

#### Reset Startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset Startup`
- Lit : `Reset Startup`
- Utilisé par : `Battery Protection`, `Reset Startup`, `Reset Startup`
- Ligne export : 32416 · id 59028

#### Is BMW  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Battery Brand = 1`
- Lit : `Battery Brand`
- Utilisé par : `Active le groupe: ELEC / BATTERY / BMW`, `Event log: BMW Battery`, `Measure group: Battery BMW`
- Ligne export : 32466 · id 67715

#### Is Kreisel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Battery Brand = 0`
- Lit : `Battery Brand`
- Utilisé par : `Active le groupe: ELEC / BATTERY / Kreisel`, `Measure group: Battery Kreisel`
- Ligne export : 35118 · id 67704

#### Is WattAlps  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Battery Brand = 2`
- Lit : `Battery Brand`
- Utilisé par : `Active le groupe: ELEC / BATTERY / WattAlps`, `Event log: WattAlps Battery`, `Measure group: Battery WattAlps`, `Single adjust item: WattAlps Debug`
- Ligne export : 37351 · id 68021

#### Battery InstantVoltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - Battery InstantVoltage [V]`
- Fonction *BMW* :
  - **Controlling** = `BMW_-_Battery_InstantVoltage [V]`
- Fonction *WattApls* :
  - **Controlling** = `WattAlps - Battery InstantVoltage [V]`
- Lit : `BMW_-_Battery_InstantVoltage`, `Battery Brand`, `Kreisel - Battery InstantVoltage`, `WattAlps - Battery InstantVoltage`
- Utilisé par : `Battery Instant Voltage`, `Battery Instant Voltage Filter`, `Charger end charge`, `Measure group: Battery Kreisel`
- Ligne export : 40282 · id 36240

#### Battery Instant Voltage Filter  `SFC`
- Propriétés : Input channel=Battery InstantVoltage [V] · Enable=Yes · Type=Slopes · Slopes={{100; 25}; {50; 50}}
- Lit : `Battery InstantVoltage`
- Utilisé par : `Battery POWER`, `MD4-10 page: INFO`
- Ligne export : 40386 · id 36248

#### Battery SOC  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - SOC [%]`
- Fonction *BMW* :
  - **Controlling** = `BMW - SOC [%]`
- Fonction *WattApls* :
  - **Controlling** = `WattAlps - SOC [%]`
- Lit : `BMW - SOC`, `Battery Brand`, `Kreisel - SOC`, `WattAlps - SOC`
- Utilisé par : `Battery CHARGED`, `Battery ECO MODE`, `Battery LOW BAT`, `Battery Low SOC Alert`, `Battery NEED TO CHARGE`, `Battery NoAUX Mode`, `Battery SOC`, `SOC`, `MD4-10 page: INFO`, `Measure group: Battery Kreisel`
- Ligne export : 40404 · id 36249

#### Battery LOW level  `IP`
- Propriétés : Unit=% · Default mode={5}
- Utilisé par : `Battery LOW BAT`, `Adjust group: Master Battery`, `Single adjust item: Battery LOW level`
- Ligne export : 40508 · id 36265

#### Current Bat  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - CURRENT [A]`
- Fonction *BMW* :
  - **Controlling** = `BMW - CURRENT [A]`
- Fonction *WattApls* :
  - **Controlling** = `WattAlps - CURRENT [A]`
- Lit : `BMW - CURRENT`, `Battery Brand`, `Kreisel - CURRENT`, `WattAlps - CURRENT`
- Utilisé par : `Battery CURRENT`, `Battery LOW BAT`, `Current Bat`, `Cuurent Bat (ABS)`, `Measure group: Battery Kreisel`
- Ligne export : 40520 · id 36267

#### Battery LOW BAT  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=100
- Logique :
  - **Activating** = `Battery SOC [%] <= Battery LOW level [%]`
  - **Blocking** = `Current Bat [A] < -0,1`
- Lit : `Battery LOW level`, `Battery SOC`, `Current Bat`
- Utilisé par : *(personne)*
- Ligne export : 40624 · id 36275

#### Battery DRIVE MODE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `(Kreisel - DRIVE MODE) OR (BMW - DRIVE MODE) OR (WattAlps - DRIVE MODE)`
- Lit : `BMW - DRIVE MODE`, `Kreisel - DRIVE MODE`, `WattAlps - DRIVE MODE`
- Utilisé par : `Battery DRIVE`, `Battery STATE`, `Charger DIGITAL CMD`, `Charger State Finite`, `Drive Mode`, `If not start`, `Reset State`, `Save Iso_Resist`, `Statistics log: Stat Log`
- Ligne export : 40678 · id 36342

#### Battery CURRENT  `SFC`
- Propriétés : Input channel=Current Bat [A] · Enable=Yes · Type=Filter · Filter=90
- Lit : `Current Bat`
- Utilisé par : `Bat - 100A-125A`, `Bat - 1A-25A`, `Bat - 25A-50A`, `Bat - 50A-75A`, `Bat - 75A-100A`, `Bat - up to 125A`, `Battery POWER`
- Ligne export : 40735 · id 36358

#### BMS_U_Trac  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - U_Trac [V]`
- Fonction *BMW* :
  - **Controlling** = `BMW_-_U_Trac [V]`
- Fonction *WattApls* :
  - **Controlling** = `WattAlps- U_Trac [V]`
- Lit : `BMW_-_U_Trac`, `Battery Brand`, `Kreisel - U_Trac`, `WattAlps- U_Trac`
- Utilisé par : `Battery U Track`, `MD4-10 page: INFO`, `Measure group: Battery Kreisel`
- Ligne export : 40747 · id 36361

#### Battery POWER  `MAC`
- Propriétés : Unit=kW · Limiting object group=Signed
- Logique :
  - **Controlling** = `(Battery Instant Voltage Filter [V] * Battery CURRENT [A]) / 1000`
- Lit : `Battery CURRENT`, `Battery Instant Voltage Filter`
- Utilisé par : `MD4-10 page: INFO`
- Ligne export : 40851 · id 36369

#### Battery ECO level  `IP`
- Propriétés : Unit=% · Default mode={10}
- Utilisé par : `Battery ECO MODE`, `Battery Low SOC Alert`, `Adjust group: Master Battery`, `Single adjust item: Battery ECO level`
- Ligne export : 40904 · id 36378

#### Battery hight temp  `IP`
- Propriétés : Unit=Â°C · Default mode={50}
- Utilisé par : `Battery ECO MODE`, `Adjust group: Master Battery`, `Single adjust item: Battery hight temp`
- Ligne export : 40916 · id 36379

#### Battery ECO MODE  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=100
- Logique :
  - **Activating** = `(Battery SOC [%] <= Battery ECO level [%]) OR (Cell_T_max_Master [Â°C] >= Battery hight temp [Â°C])`
- Lit : `Battery ECO level`, `Battery SOC`, `Battery hight temp`, `Cell_T_max_Master`
- Utilisé par : `Battery STATE`, `Statistics log: Stat Log`
- Ligne export : 40928 · id 36380

#### Battery STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ERROR* :
  - **Activating** = `(Battery ERROR DIGIT) AND (Battery CAN OK)`
- Fonction *READY* :
  - **Activating** = `Battery CAN OK`
  - **Blocking** = `(Battery ERROR DIGIT) OR (Battery DRIVE MODE)`
- Fonction *RUN* :
  - **Activating** = `Battery DRIVE MODE`
  - **Blocking** = `(Battery ECO MODE) OR (Battery ERROR DIGIT)`
- Fonction *RUN ECO* :
  - **Activating** = `(Battery DRIVE MODE) AND (Battery ECO MODE)`
  - **Blocking** = `Battery ERROR DIGIT`
- Lit : `Battery CAN OK`, `Battery DRIVE MODE`, `Battery ECO MODE`, `Battery ERROR DIGIT`
- Utilisé par : `Battery State`, `VARIATOR SUPER ON`
- Ligne export : 40982 · id 36417

#### Charge to 220 V  `IP`
- Propriétés : Unit=% · Default mode={100}
- Utilisé par : `Battery CHARGED`, `Battery NEED TO CHARGE`
- Ligne export : 41164 · id 36463

#### Bat - 25A-50A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(25 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 50)`
- Lit : `Battery CURRENT`
- Utilisé par : `Statistics log: Battery Use`
- Ligne export : 41176 · id 36538

#### Bat - 50A-75A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(50 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 75)`
- Lit : `Battery CURRENT`
- Utilisé par : `Statistics log: Battery Use`
- Ligne export : 41230 · id 36547

#### Bat - 75A-100A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(75 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 100)`
- Lit : `Battery CURRENT`
- Utilisé par : `Statistics log: Battery Use`
- Ligne export : 41284 · id 36556

#### Bat - 100A-125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(100 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 125)`
- Lit : `Battery CURRENT`
- Utilisé par : `Statistics log: Battery Use`
- Ligne export : 41338 · id 36565

#### Bat - up to 125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `125 < Battery CURRENT [A]`
- Lit : `Battery CURRENT`
- Utilisé par : `Statistics log: Battery Use`
- Ligne export : 41392 · id 36574

#### Bat - 1A-25A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(1 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 25)`
- Lit : `Battery CURRENT`
- Utilisé par : `Statistics log: Battery Use`
- Ligne export : 41437 · id 36719

#### If not start  `IDC`
- Propriétés : Toggle=No · Delay on=40000 · Delay off=0
- Logique :
  - **Activating** = `Main Switch Battery and (not(Battery DRIVE MODE))`
- Lit : `Battery DRIVE MODE`, `Main Switch Battery`
- Utilisé par : `Battery Error Durring 5 s`, `Fail Start Counter`
- Ligne export : 41491 · id 53715

#### Fail Start Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(If not start)`
- Lit : `If not start`
- Utilisé par : `10 fail Starting`
- Ligne export : 41551 · id 69910

#### 10 fail Starting  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Fail Start Counter >= 10`
- Lit : `Fail Start Counter`
- Utilisé par : `Battery Error Durring 5 s`, `Fail Starting`
- Ligne export : 41603 · id 69916

#### Battery Error Durring 5 s  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=1000
- Logique :
  - **Activating** = `(Battery ERROR DIGIT) OR (If not start)`
  - **Blocking** = `10 fail Starting`
- Lit : `10 fail Starting`, `Battery ERROR DIGIT`, `If not start`
- Utilisé par : `IDC - BATT`
- Ligne export : 41648 · id 48248

#### Force Charging  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Battery NEED TO CHARGE`, `Single adjust item: Charging Force`
- Ligne export : 41705 · id 57517

#### Battery NEED TO CHARGE  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `(Force Charging) OR (Battery SOC [%] < (Charge to 220 V [%] - 5))`
  - **Blocking** = `(Battery ERROR DIGIT) OR (Battery HIGHT TEMP) OR (not(Battery CAN OK))`
- Lit : `Battery CAN OK`, `Battery ERROR DIGIT`, `Battery HIGHT TEMP`, `Battery SOC`, `Charge to 220 V`, `Force Charging`
- Utilisé par : `Charger State Finite`
- Ligne export : 41718 · id 52164

#### Balancing State  `SMC`
- Propriétés : Default state name=Normal
- Fonction *Equilibrage* :
  - **Activating** = `Balancing Counter = 0`
- Lit : `Balancing Counter`
- Utilisé par : `Balancing Time`
- Ligne export : 41801 · id 85013

#### Balancing Time  `IP`
- Propriétés : Unit=ms · Mode selector=Balancing State · Default mode: Normal={5000} · Mode 1: Equilibrage={14400000}
- Lit : `Balancing State`
- Utilisé par : `Battery CHARGED`
- Ligne export : 41843 · id 85021

#### Battery CHARGED  `IDC`
- Propriétés : Toggle=No · Delay on=Balancing Time [ms] · Delay off=0
- Logique :
  - **Activating** = `(Battery SOC [%] >= Charge to 220 V [%]) OR (Charger end charge)`
- Lit : `Balancing Time`, `Battery SOC`, `Charge to 220 V`, `Charger end charge`
- Utilisé par : `Balancing Counter`, `Charger State Finite`
- Ligne export : 41857 · id 52186

#### Balancing Frequency  `IP`
- Propriétés : Default mode={5}
- Utilisé par : `Balancing Counter`, `Adjust group: Master Battery`, `Single adjust item: Balancing Frequency`
- Ligne export : 41909 · id 85022

#### Balancing Counter  `ECNT`
- Propriétés : Store value=Yes · Reset value=Balancing Frequency
- Logique :
  - **Decreasing** = `PositiveFlank(Battery CHARGED)`
  - **Resetting** = `Balancing Counter < 0`
- Lit : `Balancing Frequency`, `Battery CHARGED`
- Utilisé par : `Balancing State`
- Ligne export : 41921 · id 85023

#### Save Iso_Resist  `IDC`
- Propriétés : Toggle=No · Delay on=60000 · Delay off=0
- Logique :
  - **Activating** = `Battery DRIVE MODE`
- Lit : `Battery DRIVE MODE`
- Utilisé par : `Event log: Battery Isolation`
- Ligne export : 41982 · id 53666

#### Error Iso_Resist  `IDC`
- Propriétés : Toggle=No · Delay on=100000 · Delay off=0
- Logique :
  - **Activating** = `IDC Battery Protection`
- Lit : `IDC Battery Protection`
- Utilisé par : *(personne)*
- Ligne export : 42025 · id 53727

#### Battery Protection  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header=High Tension Battery · Text=Battery Isolation Critical Level. High Tension is disabled. Please contact a service center. · Channel=BMS_Iso_Resist [kOhm]
- Logique :
  - **Showing** = `IDC Battery Protection`
  - **Hiding** = `not(IDC Battery Protection)`
- Lit : `BMS_Iso_Resist`, `IDC Battery Protection`
- Utilisé par : `Battery Protection`, `IDC Battery Protection`, `Adjust group: Maintenance`, `Single adjust item: Battery Protection`
- Ligne export : 42068 · id 59037

#### LowCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - LowCellVoltage [mV]`
- Fonction *BMW* : (vide)
- Fonction *WattApls* :
  - **Controlling** = `WattAlps - LowCellVoltage [mV]`
- Lit : `Battery Brand`, `Kreisel - LowCellVoltage`, `WattAlps - LowCellVoltage`
- Utilisé par : `DiffCellVoltage`
- Ligne export : 42122 · id 67955

#### HighCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - HighCellVoltage [mV]`
- Fonction *BMW* : (vide)
- Fonction *WattApls* :
  - **Controlling** = `WattAlps - HighCellVoltage [mV]`
- Lit : `Battery Brand`, `Kreisel - HighCellVoltage`, `WattAlps - HighCellVoltage`
- Utilisé par : `DiffCellVoltage`
- Ligne export : 42219 · id 67963

#### Fail Starting  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=High Tension Battery · Text=The battery fails to connect and is disabled. Contact your service center.
- Logique :
  - **Showing** = `10 fail Starting`
- Lit : `10 fail Starting`
- Utilisé par : *(personne)*
- Ligne export : 42316 · id 69922

#### Max Discharge  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel- Max Current [A]`
- Fonction *BMW* :
  - **Controlling** = `BMW- Max Current [A]`
- Fonction *WattApls* :
  - **Controlling** = `WattAlps- Max Current [A]`
- Lit : `BMW- Max Current`, `Battery Brand`, `Kreisel- Max Current`, `WattAlps- Max Current`
- Utilisé par : `Current Limiting`
- Ligne export : 42362 · id 70877

#### Current Limiting - Error  `FP`
- Propriétés : Unit=A · Default mode={10}
- Utilisé par : `Current Limiting`, `Adjust group: Master Battery`, `Single adjust item: Current Limiting - Error`
- Ligne export : 42466 · id 70885

#### Current Limiting - Increase  `FP`
- Propriétés : Unit=%/s · Default mode={100}
- Utilisé par : `Current Limiting`, `Adjust group: Master Battery`, `Single adjust item: Current Limiting - Increase`
- Ligne export : 42478 · id 70886

#### Current Limiting - Decrease  `FP`
- Propriétés : Unit=%/s · Default mode={10}
- Utilisé par : `Current Limiting`, `Adjust group: Master Battery`, `Single adjust item: Current Limiting - Decrease`
- Ligne export : 42490 · id 70887

#### Cuurent Bat (ABS)  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Abs(Current Bat [A])`
- Lit : `Current Bat`
- Utilisé par : `Current Limiting`
- Ligne export : 42502 · id 75776

#### Current Limiting  `ILC`
- Propriétés : Output=Normal · Enable=Yes · Input channel=Cuurent Bat (ABS) [A] · Start reduction at=Max Discharge [A] · Max error=Current Limiting - Error [A] · Max increase speed=Current Limiting - Increase [%/s] · Max decrease speed=Current Limiting - Decrease [%/s]
- Lit : `Current Limiting - Decrease`, `Current Limiting - Error`, `Current Limiting - Increase`, `Cuurent Bat (ABS)`, `Max Discharge`
- Utilisé par : `DMAC_Speed_1_Right`, `DMAC_Speed_2_Left`
- Ligne export : 42545 · id 70888

#### DiffCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed
- Logique :
  - **Controlling** = `Abs((LowCellVoltage [mV] - HighCellVoltage [mV]))`
- Lit : `HighCellVoltage`, `LowCellVoltage`
- Utilisé par : `DiffCellVoltage`
- Ligne export : 42560 · id 85082

#### Battery NoAUX Level Mode  `IP`
> Minimal SOC To allow high consumption AUX support
- Propriétés : Unit=% · Default mode={40}
- Utilisé par : `Battery NoAUX Mode`, `Adjust group: Master A/C Bat Pack`, `Single adjust item: Battery NoAUX Level Mode`
- Ligne export : 42612 · id 91813

#### Battery NoAUX Mode  `IDC`
> True if No High Consumption AUX is allowed
- Propriétés : Toggle=No · Delay on=5000 · Delay off=100
- Logique :
  - **Activating** = `Battery SOC [%] <= Battery NoAUX Level Mode [%]`
- Lit : `Battery NoAUX Level Mode`, `Battery SOC`
- Utilisé par : `Flag NoAUX Mode`
- Ligne export : 42624 · id 91818

#### Battery Low SOC Alert  `IDC`
> Based on ECO Mode SOC Level
- Propriétés : Toggle=No · Delay on=5000 · Delay off=100
- Logique :
  - **Activating** = `Battery SOC [%] <= Battery ECO level [%]`
- Lit : `Battery ECO level`, `Battery SOC`
- Utilisé par : `Low Bat error warning`
- Ligne export : 42669 · id 94177

#### Low Bat error warning  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=High Tension Battery · Text=Low Battery Level. Recharge promptly
- Logique :
  - **Showing** = `PositiveFlank(Battery Low SOC Alert)`
- Lit : `Battery Low SOC Alert`
- Utilisé par : *(personne)*
- Ligne export : 42714 · id 94183

#### Battery Protection Level  `IP`
- Propriétés : Unit=KOhm · Default mode={1000}
- Utilisé par : `IDC Battery Protection`, `Adjust group: Master Battery`, `Single adjust item: Battery Protection Level`
- Ligne export : 42761 · id 94195

#### Flag Ground Fault Detection  `IDC`
> Raised if battery raises a 0.0 value with a valid measurement
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0 · Function selector=Battery Brand
- Fonction *Kreisel* :
  - **Activating** = `False`
- Fonction *BMW* :
  - **Activating** = `(IsoMonState = 3) AND (BMS_Iso_Resist [kOhm] <= 0)`
- Fonction *WattApls* :
  - **Activating** = `False`
- Lit : `BMS_Iso_Resist`, `Battery Brand`, `IsoMonState`
- Utilisé par : `Ground Fault message`
- Ligne export : 42773 · id 94200

#### Ground Fault message  `CMSG`
> Raised when a ground fault is detected
- Propriétés : Show message=All · Dialog type=Critical · Header=High Tension Battery · Text=A phase of the battery is pulled to ground. Take the boat to a safe place and contact the technical service. · Channel=BMS_Iso_Resist [kOhm]
- Logique :
  - **Showing** = `PositiveFlank(Flag Ground Fault Detection)`
- Lit : `BMS_Iso_Resist`, `Flag Ground Fault Detection`
- Utilisé par : *(personne)*
- Ligne export : 42889 · id 94227

## ELEC / BATTERY / BMW — actif seulement si `Is BMW`

#### NMT  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{ID; 8}; {State; 0}} · Module=Battery BMW (Generic) · Module index=0
- Lit : `ID`, `State`
- Utilisé par : `Init Seq`
- Ligne export : 32537 · id 88113

#### DcuNodeState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Dcu50Heartbeat`, `DcuNodeState`, `Init Seq`, `Measure group: Battery BMW`
- Ligne export : 32559 · id 88114

#### BatNodeState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Bat51Hartbeat`, `BatNodeState`, `Init Seq`, `Measure group: Battery BMW`
- Ligne export : 32571 · id 88115

#### IsoMonNodeState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Init Seq`, `Iso52MonHeartbeat`, `IsoMonNodeState`, `Measure group: Battery BMW`
- Ligne export : 32583 · id 88116

#### Init Seq  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank(NMT)`
  - **Blocking** = `(DcuNodeState = 5) AND (BatNodeState = 5) AND (IsoMonNodeState = 5)`
- Lit : `BatNodeState`, `DcuNodeState`, `IsoMonNodeState`, `NMT`
- Utilisé par : `Init Counter`
- Ligne export : 32595 · id 88117

#### Init Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Init Seq`
  - **Resetting** = `Init Counter >= 3`
- Lit : `Init Seq`
- Utilisé par : `Node Init`
- Ligne export : 32666 · id 88128

#### Node Init  `SP`
- Propriétés : Input channel=Init Counter · Default state name=0x50 · States={0x51; 0x52}
- Lit : `Init Counter`
- Utilisé par : `Node Init ID`
- Ligne export : 32726 · id 88139

#### Node Init ID  `IP`
- Propriétés : Mode selector=Node Init · Default mode: 0x50={0x50} · Mode 1: 0x51={0x51} · Mode 2: 0x52={0x52}
- Lit : `Node Init`
- Utilisé par : `ID`
- Ligne export : 32739 · id 88142

#### ID  `GPOUT`
- Propriétés : Input value=Node Init ID · Length=8 · Type=Unsigned integer
- Lit : `Node Init ID`
- Utilisé par : `NMT`
- Ligne export : 32755 · id 88143

#### State  `GPOUT`
- Propriétés : Input value=1 · Length=8 · Type=Unsigned integer
- Utilisé par : `0x331`, `A/CBatteryState`, `BMS_VMU_STATUS`, `Battery State`, `Charger STATE`, `Engine State`, `NMT`, `Speed State`, `Up/DOWN STATE`
- Ligne export : 32766 · id 88144

#### Dcu50Heartbeat  `GFIN`
- Propriétés : Identifier=0x750 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{DcuNodeState; 0}} · Module=Battery BMW (Generic) · Module index=2
- Lit : `DcuNodeState`
- Utilisé par : `BMW CAN OK`
- Ligne export : 32777 · id 88145

#### Bat51Hartbeat  `GFIN`
- Propriétés : Identifier=0x751 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{BatNodeState; 0}} · Module=Battery BMW (Generic) · Module index=3
- Lit : `BatNodeState`
- Utilisé par : *(personne)*
- Ligne export : 32796 · id 88146

#### Iso52MonHeartbeat  `GFIN`
- Propriétés : Identifier=1874 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{IsoMonNodeState; 0}} · Module=Battery BMW (Generic) · Module index=4
- Lit : `IsoMonNodeState`
- Utilisé par : *(personne)*
- Ligne export : 32815 · id 88147

#### Bat Counter  `ECNT`
- Propriétés : Store value=No · Reset value=1
- Logique :
  - **Increasing** = `PositiveFlank(Sync)`
  - **Resetting** = `Bat Counter >= 201`
- Lit : `Sync`
- Utilisé par : `SyncCounter`
- Ligne export : 32834 · id 88148

#### SyncCounter  `GPOUT`
- Propriétés : Input value=Bat Counter · Length=8 · Type=Unsigned integer
- Lit : `Bat Counter`
- Utilisé par : `Sync`
- Ligne export : 32895 · id 88159

#### Sync  `GFOUT`
- Propriétés : Identifier=0x80 · Data length=1 · Send method=Continuously · Transmit rate=20 · Unused bits=Set to 0 · Parameters={{SyncCounter; 0}} · Module=Battery BMW (Generic) · Module index=1
- Lit : `SyncCounter`
- Utilisé par : `Bat Counter`
- Ligne export : 32906 · id 88160

#### Bat51TPdo1  `GFIN`
- Propriétés : Identifier=0x1D1 · Data length=DonÂt care · Timeout=200 · Paged protocol={Not used} · Parameters={{BatState; 0}; {BatStateOfCharge; 8}; {BatCurrent; 16}; {BatPackVoltage; 32}; {BatBusVoltage; 48}} · Module=Battery BMW (Generic) · Module index=0
- Lit : `BatBusVoltage`, `BatCurrent`, `BatPackVoltage`, `BatState`, `BatStateOfCharge`
- Utilisé par : *(personne)*
- Ligne export : 32925 · id 88161

#### BatState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMW - DRIVE MODE`, `Bat51TPdo1`, `BatState`, `Battery State MEM`, `New Battery State`, `Event log: BMW Battery`, `Measure group: Battery BMW`
- Ligne export : 32956 · id 88162

#### BatStateOfCharge  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMW - SOC`, `Bat51TPdo1`
- Ligne export : 32968 · id 88163

#### BatCurrent  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - CURRENT`, `Bat51TPdo1`
- Ligne export : 32980 · id 88164

#### BatPackVoltage  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW_-_Battery_InstantVoltage`, `Bat51TPdo1`
- Ligne export : 32993 · id 88165

#### BatBusVoltage  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW_-_U_Trac`, `Bat51TPdo1`
- Ligne export : 33006 · id 88166

#### Iso52MonTPdo1  `GFIN`
- Propriétés : Identifier=466 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{IsoMonResistance; 0}; {IsoMonVoltage; 16}; {IsoMonState; 32}} · Module=Battery BMW (Generic) · Module index=8
- Lit : `IsoMonResistance`, `IsoMonState`, `IsoMonVoltage`
- Utilisé par : *(personne)*
- Ligne export : 33019 · id 88167

#### IsoMonResistance  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - Iso_Resist`, `Iso52MonTPdo1`
- Ligne export : 33044 · id 88168

#### IsoMonVoltage  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Iso52MonTPdo1`
- Ligne export : 33057 · id 88169

#### IsoMonState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Flag Ground Fault Detection`, `Iso52MonTPdo1`, `IsoMonState`
- Ligne export : 33070 · id 88170

#### Force BMW Charge  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Charge Mode`, `Adjust group: Master Battery`, `Single adjust item: Force BMW Charge`
- Ligne export : 33082 · id 88171

#### Charge Mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Charger CHARGING) OR (Force BMW Charge)`
  - **Blocking** = `not(Main Switch Battery)`
- Lit : `Charger CHARGING`, `Force BMW Charge`, `Main Switch Battery`
- Utilisé par : `Bat CMD`
- Ligne export : 33095 · id 88172

#### Bat CMD  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ON* :
  - **Activating** = `Main Switch Battery`
  - **Blocking** = `Charge Mode`
- Fonction *Charge* :
  - **Activating** = `Charge Mode`
- Lit : `Charge Mode`, `Main Switch Battery`
- Utilisé par : `Command Value`
- Ligne export : 33153 · id 88182

#### Command Value  `IP`
- Propriétés : Mode selector=Bat CMD · Default mode: OFF={0x00} · Mode 1: ON={0x01} · Mode 2: Charge={0x03}
- Lit : `Bat CMD`
- Utilisé par : `BatCommand`
- Ligne export : 33231 · id 88195

#### BatCommand  `GPOUT`
- Propriétés : Input value=Command Value · Length=8 · Type=Unsigned integer
- Lit : `Command Value`
- Utilisé par : `Bat51RPdo1`
- Ligne export : 33247 · id 88196

#### BatCoolingPolicy  `GPOUT`
- Propriétés : Input value=0x14 · Length=8 · Type=Unsigned integer
- Utilisé par : `Bat51RPdo1`
- Ligne export : 33258 · id 88197

#### Bat51RPdo1  `GFOUT`
- Propriétés : Identifier=593 · Data length=8 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={{BatCommand; 0}; {BatCoolingPolicy; 8}} · Module=Battery BMW (Generic) · Module index=2
- Lit : `BatCommand`, `BatCoolingPolicy`
- Utilisé par : *(personne)*
- Ligne export : 33269 · id 88198

#### IsoMonCommand  `GPOUT`
- Propriétés : Input value=0x01 · Length=8 · Type=Unsigned integer
- Utilisé par : `Iso52MonRPdo1`
- Ligne export : 33291 · id 88199

#### Warning Level  `IP`
- Propriétés : Default mode={750}
- Utilisé par : `IsoMonWarningLevel`
- Ligne export : 33302 · id 88200

#### IsoMonWarningLevel  `GPOUT`
- Propriétés : Input value=Warning Level · Length=16 · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Warning Level`
- Utilisé par : `Iso52MonRPdo1`
- Ligne export : 33314 · id 88201

#### Error Level  `IP`
- Propriétés : Default mode={250}
- Utilisé par : `IsoMonErrorLevel`
- Ligne export : 33326 · id 88202

#### IsoMonErrorLevel  `GPOUT`
- Propriétés : Input value=Error Level · Length=16 · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Error Level`
- Utilisé par : `Iso52MonRPdo1`
- Ligne export : 33338 · id 88203

#### Iso52MonRPdo1  `GFOUT`
- Propriétés : Identifier=0x252 · Data length=8 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={{IsoMonCommand; 0}; {IsoMonWarningLevel; 8}; {IsoMonErrorLevel; 24}} · Module=Battery BMW (Generic) · Module index=3
- Lit : `IsoMonCommand`, `IsoMonErrorLevel`, `IsoMonWarningLevel`
- Utilisé par : *(personne)*
- Ligne export : 33350 · id 88204

#### Bat51TPdo2  `GFIN`
- Propriétés : Identifier=0x2D1 · Data length=DonÂt care · Timeout=5000 · Paged protocol={Not used} · Parameters={{BatAvgTemp; 0}; {BatMinCellTemp; 8}; {BatMaxCellTemp; 16}; {BatBalancingState; 24}; {BatTimeToFullMinute; 32}} · Module=Battery BMW (Generic) · Module index=1
- Lit : `BatAvgTemp`, `BatBalancingState`, `BatMaxCellTemp`, `BatMinCellTemp`, `BatTimeToFullMinute`
- Utilisé par : *(personne)*
- Ligne export : 33375 · id 88205

#### BatAvgTemp  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Bat51TPdo2`
- Ligne export : 33406 · id 88206

#### BatMinCellTemp  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Bat51TPdo2`
- Ligne export : 33418 · id 88207

#### BatMaxCellTemp  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMW - Cell_T_max_Master`, `Bat51TPdo2`
- Ligne export : 33430 · id 88208

#### BatBalancingState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Bat51TPdo2`
- Ligne export : 33442 · id 88209

#### BatTimeToFullMinute  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51TPdo2`
- Ligne export : 33454 · id 88210

#### Bat51TPdo3  `GFIN`
- Propriétés : Identifier=0x3D1 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{BatPowerLimitChargeRaw; 0}; {BatPowerLimitDischargeRaw; 16}; {BatEnergyRemainingRaw; 32}} · Module=Battery BMW (Generic) · Module index=9
- Lit : `BatEnergyRemainingRaw`, `BatPowerLimitChargeRaw`, `BatPowerLimitDischargeRaw`
- Utilisé par : *(personne)*
- Ligne export : 33467 · id 88211

#### BatPowerLimitChargeRaw  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51TPdo3`, `BatPowerLimitCharge`
- Ligne export : 33492 · id 88212

#### BatPowerLimitDischargeRaw  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51TPdo3`, `BatPowerLimitDischarge`
- Ligne export : 33505 · id 88213

#### BatEnergyRemainingRaw  `GPIN`
- Propriétés : Length=32 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51TPdo3`, `BatEnergyRemaining`
- Ligne export : 33518 · id 88214

#### BMW_-_Battery_InstantVoltage  `MAC`
- Propriétés : Unit=V
- Logique :
  ```qcode
  Result := BatPackVoltage * 0.1
  ```
- Lit : `BatPackVoltage`
- Utilisé par : `Battery InstantVoltage`, `Measure group: Battery BMW`
- Ligne export : 33531 · id 88215

#### BMW - CURRENT  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result := BatCurrent * 0.02 - 640
  ```
- Lit : `BatCurrent`
- Utilisé par : `Current Bat`, `Measure group: Battery BMW`
- Ligne export : 33549 · id 88225

#### BMW - Cell_T_max_Master  `MAC`
- Propriétés : Unit=Â°C
- Logique :
  ```qcode
  Result := BatMaxCellTemp - 40
  ```
- Lit : `BatMaxCellTemp`
- Utilisé par : `Cell_T_max_Master`, `Measure group: Battery BMW`
- Ligne export : 33567 · id 88236

#### BMW - Iso_Resist  `MAC`
- Propriétés : Unit=kOhm · Limiting object group=Signed
- Logique :
  - **Controlling** = `IsoMonResistance`
- Lit : `IsoMonResistance`
- Utilisé par : `BMS_Iso_Resist`, `Measure group: Battery BMW`
- Ligne export : 33585 · id 88246

#### BMW_-_U_Trac  `MAC`
- Propriétés : Unit=V
- Logique :
  ```qcode
  Result := BatBusVoltage * 0.1
  ```
- Lit : `BatBusVoltage`
- Utilisé par : `BMS_U_Trac`, `BMW- Max Current`, `Measure group: Battery BMW`
- Ligne export : 33627 · id 88254

#### DcuNodeState  `SMC`
- Propriétés : Default state name=Boot
- Fonction *Stopped* :
  - **Activating** = `DcuNodeState = 4`
- Fonction *Operational* :
  - **Activating** = `DcuNodeState = 5`
- Fonction *Pre-Op* :
  - **Activating** = `DcuNodeState = 127`
- Lit : `DcuNodeState`
- Utilisé par : `Dcu50Heartbeat`, `Init Seq`, `Measure group: Battery BMW`
- Ligne export : 33645 · id 88264

#### BatNodeState  `SMC`
- Propriétés : Default state name=Boot
- Fonction *Stopped* :
  - **Activating** = `BatNodeState = 4`
- Fonction *Operational* :
  - **Activating** = `BatNodeState = 5`
- Fonction *Pre-Op* :
  - **Activating** = `BatNodeState = 127`
- Lit : `BatNodeState`
- Utilisé par : `Bat51Hartbeat`, `Init Seq`, `Measure group: Battery BMW`
- Ligne export : 33753 · id 88280

#### IsoMonNodeState  `SMC`
- Propriétés : Default state name=Boot
- Fonction *Stopped* :
  - **Activating** = `IsoMonNodeState = 4`
- Fonction *Operational* :
  - **Activating** = `IsoMonNodeState = 5`
- Fonction *Pre-Op* :
  - **Activating** = `IsoMonNodeState = 127`
- Lit : `IsoMonNodeState`
- Utilisé par : `Init Seq`, `Iso52MonHeartbeat`, `Measure group: Battery BMW`
- Ligne export : 33861 · id 88296

#### BMW - SOC  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `BatStateOfCharge * 0,5`
- Lit : `BatStateOfCharge`
- Utilisé par : `Battery SOC`, `Measure group: Battery BMW`
- Ligne export : 33969 · id 88312

#### BMW CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  - **Activating** = `Dcu50Heartbeat`
- Lit : `Dcu50Heartbeat`
- Utilisé par : `Battery CAN OK`, `Charger CAN BUS OK`
- Ligne export : 34013 · id 88320

#### Dcu50Error  `GFIN`
- Propriétés : Identifier=208 · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{DcuErrorCode; 24}; {DcuError; 8}} · Module=Battery BMW (Generic) · Module index=5
- Lit : `DcuError`, `DcuErrorCode`
- Utilisé par : *(personne)*
- Ligne export : 34056 · id 88328

#### DcuErrorCode  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Dcu50Error`, `DcuErrorCode M`, `DcuErrorCode Out`, `DcuErrorCode TF`, `Measure group: Battery BMW`
- Ligne export : 34078 · id 88329

#### Bat51Error  `GFIN`
- Propriétés : Identifier=0xD1 · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{BatErrorCode; 24}; {BatError; 8}} · Module=Battery BMW (Generic) · Module index=6
- Lit : `BatError`, `BatErrorCode`
- Utilisé par : *(personne)*
- Ligne export : 34091 · id 88330

#### BatErrorCode  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51Error`, `BatErrorCode M`, `BatErrorCode Out`, `BatErrorCode TF`, `Battery Error Code`, `New Error Code`, `Measure group: Battery BMW`
- Ligne export : 34113 · id 88331

#### Iso52MonError  `GFIN`
- Propriétés : Identifier=210 · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{IsoMonErrorCode; 24}; {IsoMonError; 8}} · Module=Battery BMW (Generic) · Module index=7
- Lit : `IsoMonError`, `IsoMonErrorCode`
- Utilisé par : *(personne)*
- Ligne export : 34126 · id 88332

#### IsoMonErrorCode  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Iso52MonError`, `IsoMonErrorCode M`, `IsoMonErrorCode Out`, `IsoMonErrorCode TF`, `Measure group: Battery BMW`
- Ligne export : 34148 · id 88333

#### BMW - ERROR DIGIT  `IDC`
- Propriétés : Toggle=No · Delay on=100 · Delay off=100
- Utilisé par : `Battery ERROR DIGIT`, `Measure group: Battery BMW`
- Ligne export : 34161 · id 88334

#### BMW - DRIVE MODE  `IDC`
> Kreisel 
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `BatState = 2`
- Lit : `BatState`
- Utilisé par : `Battery DRIVE MODE`, `Measure group: Battery BMW`
- Ligne export : 34197 · id 88341

#### BatPowerLimitCharge  `MAC`
- Propriétés : Unit=kW
- Logique :
  ```qcode
  Result := BatPowerLimitChargeRaw * 0.01 - 320
  ```
- Lit : `BatPowerLimitChargeRaw`
- Utilisé par : `Measure group: Battery BMW`
- Ligne export : 34242 · id 88349

#### BatPowerLimitDischarge  `MAC`
- Propriétés : Unit=kW
- Logique :
  ```qcode
  Result := BatPowerLimitDischargeRaw * 0.01 - 320
  ```
- Lit : `BatPowerLimitDischargeRaw`
- Utilisé par : `BMW- Max Current`, `Measure group: Battery BMW`
- Ligne export : 34260 · id 88360

#### BatEnergyRemaining  `MAC`
- Propriétés : Unit=kWh
- Logique :
  ```qcode
  Result := BatEnergyRemainingRaw * 0.001
  ```
- Lit : `BatEnergyRemainingRaw`
- Utilisé par : `Measure group: Battery BMW`
- Ligne export : 34278 · id 88371

#### BMW- Max Current  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  if BMW_-_U_Trac then
  current :=  BatPowerLimitDischarge * 1000 / BMW_-_U_Trac
  else
  current := 0
  endif
  
  Result := MaxOf(20, current)
  ```
- Lit : `BMW_-_U_Trac`, `BatPowerLimitDischarge`
- Utilisé par : `Max Discharge`, `Measure group: Battery BMW`
- Ligne export : 34296 · id 88381

#### DcuError  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `Dcu50Error`
- Ligne export : 34320 · id 88398

#### BatError  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `Bat51Error`
- Ligne export : 34332 · id 88399

#### IsoMonError  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `Iso52MonError`
- Ligne export : 34344 · id 88400

#### New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `BatErrorCode <> Battery Error Code`
- Lit : `BatErrorCode`, `Battery Error Code`
- Utilisé par : `Battery Error Code`, `Event log: BMW Battery`
- Ligne export : 34356 · id 88401

#### Battery Error Code  `MEM`
- Propriétés : Input channel=BatErrorCode · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(New Error Code)`
- Lit : `BatErrorCode`, `New Error Code`
- Utilisé par : `New Error Code`
- Ligne export : 34401 · id 88409

#### DcuErrorCode M  `IMAC`
- Logique :
  ```qcode
  if DcuErrorCode = 4097 then
  Result := 1
  elseif DcuErrorCode = 8192 then
  Result := 2
  else
  Result := 0
  endif
  ```
- Lit : `DcuErrorCode`
- Utilisé par : `DcuErrorCode P`
- Ligne export : 34446 · id 88417

#### DcuErrorCode P  `SP`
- Propriétés : Input channel=DcuErrorCode M · Default state name=0 · States={4097; 8192}
- Lit : `DcuErrorCode M`
- Utilisé par : `DcuErrorCode T`
- Ligne export : 34470 · id 88434

#### DcuErrorCode T  `TP`
- Propriétés : Mode selector=DcuErrorCode P · Default mode: 0={NoError} · Mode 1: 4097={HVIL_Fail} · Mode 2: 8192={EMCY_Off}
- Lit : `DcuErrorCode P`
- Utilisé par : `DcuErrorCode TF`
- Ligne export : 34483 · id 88437

#### BatErrorCode M  `IMAC`
- Logique :
  ```qcode
  if BatErrorCode = 4097 then
  Result := 1
  elseif BatErrorCode = 4098 then
  Result := 2
  elseif BatErrorCode = 4099 then
  Result := 3
  elseif BatErrorCode = 8193 then
  Result := 4
  elseif BatErrorCode = 12289 then
  Result := 5
  elseif BatErrorCode = 12290 then
  Result := 6
  elseif BatErrorCode = 12291 then
  Result := 7
  elseif BatErrorCode = 12292 then
  Result := 8
  elseif BatErrorCode = 16385 then
  Result := 9
  elseif BatErrorCode = 20481 then
  Result := 10
  elseif BatErrorCode = 24577 then
  Result := 11
  elseif BatErrorCode = 28673 then
  Result := 12
  elseif BatErrorCode = 32769 then
  Result := 13
  elseif BatErrorCode = 40961 then
  Result := 14
  elseif BatErrorCode = 40962 then
  Result := 15
  elseif BatErrorCode = 40963 then
  Result := 16
  elseif BatErrorCode = 40964 then
  Result := 17
  elseif BatErrorCode = 40965 then
  Result := 18
  elseif BatErrorCode = 40966 then
  Result := 19
  elseif BatErrorCode = 40967 then
  Result := 20
  elseif BatErrorCode = 40968 then
  Result := 21
  elseif BatErrorCode = 40969 then
  Result := 22
  elseif BatErrorCode = 40970 then
  Result := 23
  elseif BatErrorCode = 40971 then
  Result := 24
  elseif BatErrorCode = 40972 then
  Result := 25
  elseif BatErrorCode = 40973 then
  Result := 26
  elseif BatErrorCode = 40974 then
  Result := 27
  elseif BatErrorCode = 40975 then
  Result := 28
  elseif BatErrorCode = 40976 then
  Result := 29
  elseif BatErrorCode = 40977 then
  Result := 30
  elseif BatErrorCode = 40978 then
  Result := 31
  elseif BatErrorCode = 40979 then
  Result := 32
  elseif BatErrorCode = 40980 then
  Result := 33
  elseif BatErrorCode = 40981 then
  Result := 34
  elseif BatErrorCode = 40982 then
  Result := 35
  elseif BatErrorCode = 40983 then
  Result := 36
  elseif BatErrorCode = 40984 then
  Result := 37
  elseif BatErrorCode = 40985 then
  Result := 38
  elseif BatErrorCode = 40992 then
  Result := 39
  elseif BatErrorCode = 40993 then
  Result := 40
  elseif BatErrorCode = 45057 then
  Result := 41
  elseif BatErrorCode = 45058 then
  Result := 42
  elseif BatErrorCode = 45059 then
  Result := 43
  elseif BatErrorCode = 45060 then
  Result := 44
  elseif BatErrorCode = 45061 then
  Result := 45
  elseif BatErrorCode = 45062 then
  Result := 46
  elseif BatErrorCode = 45063 then
  Result := 47
  elseif BatErrorCode = 45064 then
  Result := 48
  elseif BatErrorCode = 45065 then
  Result := 49
  elseif BatErrorCode = 49153 then
  Result := 50
  elseif BatErrorCode = 49154 then
  Result := 51
  elseif BatErrorCode = 53249 then
  Result := 52
  elseif BatErrorCode = 65280 then
  Result := 53
  else
  Result := 0
  endif
  ```
- Lit : `BatErrorCode`
- Utilisé par : `BatErrorCode P`
- Ligne export : 34498 · id 88438

#### BatErrorCode P  `SP`
- Propriétés : Input channel=BatErrorCode M · Default state name=0 · States={4097; 4098; 4099; 8193; 12289; 12290; 12291; 12292; 16385; 20481; 24577; 28673; 32769; 40961; 40962; 40963; 40964; 40965; 40966; 40967; 40968; 40969; 40970; 40971; 40972; 40973; 40974; 40975; 40976; 40977; 40978; 40979; 40980; 40981; 40982; 40983; 40984; 40985; 40992; 40993; 45057; 45058; 45059; 45060; 45061; 45062; 45063; 45064; 45065; 49153; 49154; 53249; 65280}
- Lit : `BatErrorCode M`
- Utilisé par : `BatErrorCode T`
- Ligne export : 34624 · id 88659

#### BatErrorCode T  `TP`
- Propriétés : Mode selector=BatErrorCode P · Default mode: 0={NoError} · Mode 1: 4097={OneContactorSticky} · Mode 2: 4098={TwoContactorsSticky} · Mode 3: 4099={PrechargeLock} · Mode 4: 8193={Pack_OverVoltage} · Mode 5: 12289={Pack_UnderVoltage} · Mode 6: 12290={SocLow} · Mode 7: 12291={SocVeryLow} · Mode 8: 12292={SocCriticalLow} · Mode 9: 16385={Bus_OverVoltage} · Mode 10: 20481={Bus_UnderVoltage} · Mode 11: 24577={HVIL_Fail} · Mode 12: 28673={Communication_Error} · Mode 13: 32769={OverCurrent} · Mode 14: 40961={TemperatureHigh} · Mode 15: 40962={TemperatureLow} · Mode 16: 40963={CoolingCompConnLost} · Mode 17: 40964={CoolingModuleConnLost} · Mode 18: 40965={CoolingCompDrOvertemp} · Mode 19: 40966={CoolingCompDrOvercurrent} · Mode 20: 40967={CoolingCompSdOverUnderVoltage} · Mode 21: 40968={CoolingCompSdCriticalOvertemp} · Mode 22: 40969={CoolingCompSdTorqueExceeded} · Mode 23: 40970={CoolingCompSdLinCommError} · Mode 24: 40971={CoolingCompSdExternalSupply} · Mode 25: 40972={CoolingCompSdErrorInverterSupply} · Mode 26: 40973={CoolingCompSdErrorSensor} · Mode 27: 40974={CoolingCompSdShortcircuit} · Mode 28: 40975={CoolingCompSdRunUp} · Mode 29: 40976={CoolingWaterFlowLow} · Mode 30: 40977={CoolingWaterFlowImplausible} · Mode 31: 40978={CoolingWaterFlowVariation} · Mode 32: 40979={CoolingWaterTempLow} · Mode 33: 40980={CoolingWaterTempHigh} · Mode 34: 40981={CoolingWaterTempDiffLow} · Mode 35: 40982={CoolingPresLow} · Mode 36: 40983={CoolingPresHigh} · Mode 37: 40984={CoolingWaterInTempSensor} · Mode 38: 40985={CoolingWaterOutTempSensor} · Mode 39: 40992={CoolingModulePdo2Missing} · Mode 40: 40993={CoolingModulePdo3Missing} · Mode 41: 45057={Internal_Error} · Mode 42: 45058={ServiceDisconnect} · Mode 43: 45059={AbortCharging} · Mode 44: 45060={CoolingValveShortToGround} · Mode 45: 45061={CoolingValveShortToUbat} · Mode 46: 45062={CoolingValveWireBroken} · Mode 47: 45063={CoolingValveDriverError} · Mode 48: 45064={CoolingValveValveStuckAtClosed} · Mode 49: 45065={CoolingValveValveStuckAtOpen} · Mode 50: 49153={Category6Failure} · Mode 51: 49154={Category7Failure} · Mode 52: 53249={ThermalEventHazard} · Mode 53: 65280={DeviceSoftwareGenericFail}
- Lit : `BatErrorCode P`
- Utilisé par : `BatErrorCode TF`
- Ligne export : 34688 · id 88713

#### IsoMonErrorCode M  `IMAC`
- Logique :
  ```qcode
  if IsoMonErrorCode = 8193 then
  Result := 1
  elseif IsoMonErrorCode = 12289 then
  Result := 2
  elseif IsoMonErrorCode = 16385 then
  Result := 3
  elseif IsoMonErrorCode = 16386 then
  Result := 4
  elseif IsoMonErrorCode = 20481 then
  Result := 5
  elseif IsoMonErrorCode = 65280 then
  Result := 6
  else
  Result := 0
  endif
  ```
- Lit : `IsoMonErrorCode`
- Utilisé par : `IsoMonErrorCode P`
- Ligne export : 34805 · id 88714

#### IsoMonErrorCode P  `SP`
- Propriétés : Input channel=IsoMonErrorCode M · Default state name=0 · States={4097; 8193; 12289; 16385; 16386; 20481; 65280}
- Lit : `IsoMonErrorCode M`
- Utilisé par : `IsoMonErrorCode T`
- Ligne export : 34837 · id 88747

#### IsoMonErrorCode T  `TP`
- Propriétés : Mode selector=IsoMonErrorCode P · Default mode: 0={NoError} · Mode 1: 4097={IsoMeasurementNotWorking} · Mode 2: 8193={PlausibilityCheckFailed} · Mode 3: 12289={Warning_Level} · Mode 4: 16385={Error_Intern_Level} · Mode 5: 16386={Error_Extern_Level} · Mode 6: 20481={CommunicationError} · Mode 7: 65280={DeviceSoftwareGenericFail}
- Lit : `IsoMonErrorCode P`
- Utilisé par : `IsoMonErrorCode TF`
- Ligne export : 34855 · id 88755

#### DcuErrorCode TF  `TFC`
- Propriétés : Delimiter=_ · Texts={{DcuErrorCode; Value; 0}; {DcuErrorCode T; Value; 0}}
- Lit : `DcuErrorCode`, `DcuErrorCode T`
- Utilisé par : *(personne)*
- Ligne export : 34880 · id 88756

#### BatErrorCode TF  `TFC`
- Propriétés : Delimiter=_ · Texts={{BatErrorCode; Value; 0}; {BatErrorCode T; Value; 0}}
- Lit : `BatErrorCode`, `BatErrorCode T`
- Utilisé par : `Event log: BMW Battery`
- Ligne export : 34898 · id 88757

#### IsoMonErrorCode TF  `TFC`
- Propriétés : Delimiter=_ · Texts={{IsoMonErrorCode; Value; 0}; {IsoMonErrorCode T; Value; 0}}
- Lit : `IsoMonErrorCode`, `IsoMonErrorCode T`
- Utilisé par : *(personne)*
- Ligne export : 34916 · id 88758

#### IsoMonState  `SP`
- Propriétés : Input channel=IsoMonState · Default state name=Reset · States={SelfCheck; RunningValueInvalid; RunningValueValid; Device Error}
- Lit : `IsoMonState`
- Utilisé par : `Flag Ground Fault Detection`, `Iso52MonTPdo1`
- Ligne export : 34934 · id 88759

#### BatState  `SP`
- Propriétés : Input channel=BatState · Default state name=Reset · States={Precharging; Connected; Device Com Error; Precharge Error; Device Error; Disconnecte_Error; Disconnect}
- Lit : `BatState`
- Utilisé par : `BMW - DRIVE MODE`, `Bat51TPdo1`, `Battery State MEM`, `New Battery State`, `Event log: BMW Battery`, `Measure group: Battery BMW`
- Ligne export : 34949 · id 88764

#### New Battery State  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `BatState <> Battery State MEM`
- Lit : `BatState`, `Battery State MEM`
- Utilisé par : `Battery State MEM`
- Ligne export : 34967 · id 88772

#### Battery State MEM  `MEM`
- Propriétés : Input channel=BatState · Action=Replace · Store value=No
- Logique :
  - **Activating** = `PositiveFlank(New Battery State)`
- Lit : `BatState`, `New Battery State`
- Utilisé par : `New Battery State`
- Ligne export : 35012 · id 88780

#### BatErrorCode Out  `GPOUT`
- Propriétés : Input value=BatErrorCode · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `BatErrorCode`
- Utilisé par : `BMW Error`
- Ligne export : 35056 · id 88788

#### DcuErrorCode Out  `GPOUT`
- Propriétés : Input value=DcuErrorCode · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `DcuErrorCode`
- Utilisé par : `BMW Error`
- Ligne export : 35068 · id 88789

#### IsoMonErrorCode Out  `GPOUT`
- Propriétés : Input value=IsoMonErrorCode · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `IsoMonErrorCode`
- Utilisé par : `BMW Error`
- Ligne export : 35080 · id 88790

#### BMW Error  `GFOUT`
- Propriétés : Identifier=0x7451240 · Data length=8 · Send method=On change · Unused bits=Set to 0 · Parameters={{BatErrorCode Out; 0}; {DcuErrorCode Out; 16}; {IsoMonErrorCode Out; 32}} · Module=Promeion (Generic) · Module index=6
- Lit : `BatErrorCode Out`, `DcuErrorCode Out`, `IsoMonErrorCode Out`
- Utilisé par : `Charger ERROR`
- Ligne export : 35092 · id 88791

## ELEC / BATTERY / Kreisel — actif seulement si `Is Kreisel`

#### 912 mBMS_Bat_Info_Master  `GFIN`
- Propriétés : Identifier=912 · Data length=8 · Timeout=2000 · Paged protocol={Not used} · Parameters={{BMS_SOC_Master; 48}; {BMS_I_Batt_Maste [A]; 0}; {BMS_U_Batt_Master; 16}} · Module=Battery Kreisel (Generic) · Module index=0
- Lit : `BMS_I_Batt_Maste`, `BMS_SOC_Master`, `BMS_U_Batt_Master`
- Utilisé par : *(personne)*
- Ligne export : 35190 · id 66728

#### BMS_SOC_Master  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `912 mBMS_Bat_Info_Master`, `Battery Real SOC`, `Kreisel - SOC`
- Ligne export : 35215 · id 66729

#### BMS_U_Batt_Master  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `912 mBMS_Bat_Info_Master`, `Kreisel - Battery InstantVoltage`
- Ligne export : 35228 · id 66730

#### Kreisel - Battery InstantVoltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `BMS_U_Batt_Master * 0,1`
- Lit : `BMS_U_Batt_Master`
- Utilisé par : `Battery InstantVoltage`
- Ligne export : 35241 · id 66731

#### Kreisel - SOC  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin((BMS_SOC_Master * 0,01): 5->0, 85->100, Freeze)`
- Lit : `BMS_SOC_Master`
- Utilisé par : `Battery SOC`
- Ligne export : 35285 · id 66740

#### BMS_I_Batt_Maste  `GPIN`
- Propriétés : Unit=A · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `912 mBMS_Bat_Info_Master`, `Kreisel - CURRENT`
- Ligne export : 35341 · id 66750

#### Kreisel - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `BMS_I_Batt_Maste [A] * 0,1`
- Lit : `BMS_I_Batt_Maste`
- Utilisé par : `Current Bat`
- Ligne export : 35354 · id 66751

#### 913 mBMS_Cell_Info_Master  `GFIN`
- Propriétés : Identifier=913 · Data length=8 · Timeout=2000 · Paged protocol={Not used} · Parameters={{U_Cell_min_Master; 32}; {U_Cell_max_Master; 16}; {U_Cell_avg_Master; 0}; {Cell_T_max_Master; 48}; {Cell_T_min_Master; 56}} · Module=Battery Kreisel (Generic) · Module index=1
- Lit : `Cell_T_max_Master`, `Cell_T_min_Master`, `U_Cell_avg_Master`, `U_Cell_max_Master`, `U_Cell_min_Master`
- Utilisé par : *(personne)*
- Ligne export : 35398 · id 66769

#### Cell_T_max_Master  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `913 mBMS_Cell_Info_Master`, `Kreisel - Cell_T_max_Master`, `MD4-10 page: INFO`, `Measure group: Battery Kreisel`, `Statistics log: Stat Log`
- Ligne export : 35429 · id 66770

#### Kreisel - Cell_T_max_Master  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Cell_T_max_Master * 1`
- Lit : `Cell_T_max_Master`
- Utilisé par : `Cell_T_max_Master`
- Ligne export : 35441 · id 66771

#### 257 mBMS_FuncSTAT  `GFIN`
- Propriétés : Identifier=257 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{BMS_start_up_ready; 0}; {BMS_stay_alive; 1}; {BMS_iso_meas_act; 2}; {BMS_balancing_act; 3}; {BMS_reset_denied; 4}; {BMS_wakeup_active; 5}; {BMS_Master_available; 8}; {BMS_Master_MSW_Closed; 16}; {BMS_EmergencyState_Master; 24}} · Module=Battery Kreisel (Generic) · Module index=4
- Lit : `BMS_EmergencyState_Master`, `BMS_Master_MSW_Closed`, `BMS_Master_available`, `BMS_balancing_act`, `BMS_iso_meas_act`, `BMS_reset_denied`, `BMS_start_up_ready`, `BMS_stay_alive`, `BMS_wakeup_active`
- Utilisé par : `Kreisel - CAN OK`
- Ligne export : 35485 · id 66787

#### BMS_EmergencyState_Master  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`, `BMS_EmergencyState_Master_IDC`, `Kreisel - ERROR DIGIT`
- Ligne export : 35528 · id 66788

#### Kreisel - ERROR DIGIT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `BMS_EmergencyState_Master`
- Lit : `BMS_EmergencyState_Master`
- Utilisé par : `Battery ERROR CMG`, `Battery ERROR DIGIT`
- Ligne export : 35540 · id 66789

#### Switch Battery  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Main Switch Battery`
- Lit : `Main Switch Battery`
- Utilisé par : `Func_MSW_Request_Master`
- Ligne export : 35583 · id 66805

#### 276 mBMS_Trac_Info  `GFIN`
- Propriétés : Identifier=276 · Data length=8 · Timeout=2000 · Paged protocol={Not used} · Parameters={{BMS_Iso_Resist; 16}; {BMS_U_Trac [dV]; 0}} · Module=Battery Kreisel (Generic) · Module index=2
- Lit : `BMS_Iso_Resist`, `BMS_U_Trac`
- Utilisé par : *(personne)*
- Ligne export : 35626 · id 66870

#### BMS_Iso_Resist  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `276 mBMS_Trac_Info`, `Iso Resist`, `Kreisel - Iso_Resist`, `Event log: Battery Isolation`, `MD4-10 page: INFO`, `Measure group: Battery Kreisel`
- Ligne export : 35648 · id 66871

#### Kreisel - Iso_Resist  `MAC`
- Propriétés : Unit=kOhm · Limiting object group=Signed
- Logique :
  - **Controlling** = `BMS_Iso_Resist * 1`
- Lit : `BMS_Iso_Resist`
- Utilisé par : `BMS_Iso_Resist`
- Ligne export : 35661 · id 66843

#### BMS_Master_MSW_Closed  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`, `BMS_Master_MSW_Closed_IDC`, `BMS_Master_MSW_Opened_IDC`, `Kreisel - DRIVE MODE`
- Ligne export : 35705 · id 66883

#### Kreisel - DRIVE MODE  `IDC`
> Kreisel 
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `BMS_Master_MSW_Closed`
- Lit : `BMS_Master_MSW_Closed`
- Utilisé par : `Battery DRIVE MODE`
- Ligne export : 35717 · id 66884

#### Kreisel - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `257 mBMS_FuncSTAT`
- Lit : `257 mBMS_FuncSTAT`
- Utilisé par : `Battery CAN OK`
- Ligne export : 35760 · id 66892

#### BMS_U_Trac  `GPIN`
- Propriétés : Unit=dV · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `276 mBMS_Trac_Info`, `Battery U Track`, `Kreisel - U_Trac`, `MD4-10 page: INFO`, `Measure group: Battery Kreisel`
- Ligne export : 35803 · id 66901

#### Kreisel - U_Trac  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `BMS_U_Trac [dV] * 0,1`
- Lit : `BMS_U_Trac`
- Utilisé par : `BMS_U_Trac`
- Ligne export : 35816 · id 66902

#### 258 mBMS_ROE  `GFIN`
- Propriétés : Identifier=258 · Data length=DonÂt care · Timeout=100 · Paged protocol={Not used} · Parameters={{EVT_ErrNr_SC; 8}; {EVT_Context; 16}; {mBMS_ROE_Mux M; 0}} · Module=Battery Kreisel (Generic) · Module index=3
- Lit : `EVT_Context`, `EVT_ErrNr_SC`, `mBMS_ROE_Mux M`
- Utilisé par : *(personne)*
- Ligne export : 35860 · id 66930

#### EVT_ErrNr_SC  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `258 mBMS_ROE`, `Battery New Error Code`, `EVT_ErrNr_SC MEM`
- Ligne export : 35885 · id 66931

#### BMS_EmergencyState_Master_IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank((1 = BMS_EmergencyState_Master))`
- Lit : `BMS_EmergencyState_Master`
- Utilisé par : `Event log: Electronic Logs`, `Measure group: Battery Kreisel`
- Ligne export : 35897 · id 66932

#### Battery New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `EVT_ErrNr_SC <> EVT_ErrNr_SC MEM`
- Lit : `EVT_ErrNr_SC`, `EVT_ErrNr_SC MEM`
- Utilisé par : `Battery ERROR CMG`, `EVT_ErrNr_SC MEM`, `Event log: Electronic Logs`
- Ligne export : 35950 · id 66941

#### EVT_ErrNr_SC MEM  `MEM`
- Propriétés : Input channel=EVT_ErrNr_SC · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(Battery New Error Code)`
- Lit : `Battery New Error Code`, `EVT_ErrNr_SC`
- Utilisé par : `Battery Error`, `Battery Error List`, `Battery New Error Code`
- Ligne export : 35995 · id 66949

#### Battery Error List  `SP`
- Propriétés : Input channel=EVT_ErrNr_SC MEM · Default state name=ERR_CSC_OVERVOLTAGE · States={ERR_CSC_UNDERVOLTAGE; ERR_CSC_WARNING; ERR_SSV_TIMEOUT; ERR_ISO_RESISTANCE; ERR_ACC_EMERGENCY; ERR_FLOW_CTR; ERR_CSC_EMERGENCY; ERR_PMB_EMERGENCY; ERR_INTERLOCK_MISSING; ERR_PMB_TIMEOUT; ERR_SSV_INTEROPERABLE; ERR_ISO_MEASUREMENT; ERR_PCB1_TEMPERATURE; ERR_PMB_LIMITS; ERR_NVRAM; ERR_LIFEDATA; ERR_HV_MEAS; ERR_TRAC_VOLTAGE; ERR_WD; ERR_CPU_TEST; ERR_RESET_MONITOR; ERR_ROM_MONITOR; ERR_RAM_MONITOR; ERR_STACK_MONITOR; ERR_PMB_WARNING; ERR_RESERVED_BIT_42; ERR_SSV_CONFIG_HARD; ERR_CSC_EMERG_SHORT_SUP; ERR_BCC_COM; ERR_SUPPLYVOLTAGE; ERR_REFVOLTAGE; ERR_SSV_EMERGENCY; ERR_SSV_WARNING; ERR_PMB_EMERG_SHORT_SUP; ERR_FLASH_MONITOR; ERR_SSV_SUPPLYVOTLAGE; ERR_SSV_WD; ERR_PMB_INTERNAL; ERR_MSW_AGE; ERR_PMB_OVT; ERR_PMB_OC_CHG; ERR_PMB_OC_DCHG; ERR_PMB_OVERVOLTAGE; ERR_CSC_INTERNAL; ERR_CSC_TIMEOUT; ERR_CSC_OVERTEMPERATUR; ERR_MSW_AGE_WRN; ERR_CSC_LIMITS; ERR_SSV_ALIVE_TEST; ERR_PMB_INTEROP; ERR_CSC_INTEROP; ERR_IL_TEST; ERR_PMB_EMERG_TEST; ERR_KL30C_TEST; ERR_WD_TEST; ERR_CRASH; ERR_ACC_EMERG_TEST; ERR_DATASETCONF; ERR_ADC; ERR_DATASET; ERR_CSC_DS_INTEROP; ERR_SSV_STARTUP_TEST; ERR_STARTUP; ERR_MSW_STUCK_TEST; ERR_MSWMINUS_CONTROL; ERR_MSWPLUS_CONTROL; ERR_MSW3_CONTROL; ERR_PMB_DS_INTEROP; ERR_SC_INTERNAL; ERR_ISO_SHORT; ERR_RTC; ERR_PRECHARGE1_POWER; ERR_PRECHARGE1_DIAG; ERR_MC_WD; ERR_MSWMINUS_STUCK; ERR_MSWPLUS_STUCK; ERR_MSW3_STUCK; RESERVED_BIT_46; RESERVED_BIT_47; ERR_PRECHARGE2_DIAG; ERR_PRECHARGE2_POWER; ERR_TIMERMANGEMENT; ERR_TASKSYSTEM; ERR_BSC_OP_9D23H; ERR_BSC_OP_10D; RESERVED_BIT_54; ERR_CSC_EMERG_TEST; ERR_SSV_REFVOLTAGE; ERR_SSV_DS_INTEROP; ERR_SPI_COM; ERR_CELL_OV_WARN; ERR_CELL_UV_WARN; ERR_PMB_OC_PRECH; Reserved_5E; Reserved_5F; STAT_CLOSE_NOT_POSSIBLE_WEAK; STAT_ISO_RES_WARNING; STAT_ISO_GND_WARNING}
- Lit : `EVT_ErrNr_SC MEM`
- Utilisé par : `Battery Error`
- Ligne export : 36040 · id 66957

#### Battery Error  `TFC`
- Propriétés : Texts={{EVT_ErrNr_SC MEM; Value; 0}; { - }; {Battery Error List; Value; 0}}
- Lit : `Battery Error List`, `EVT_ErrNr_SC MEM`
- Utilisé par : `Battery ERROR CMG`, `Event log: Electronic Logs`
- Ligne export : 36149 · id 67056

#### Show battery Msg  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Battery ERROR CMG`
- Ligne export : 36169 · id 67057

#### Battery ERROR CMG  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=High Tension Battery · Channel=Battery Error
- Logique :
  - **Showing** = `(Battery New Error Code) AND (Kreisel - ERROR DIGIT) AND (Battery New Error Code <> 0)`
  - **Hiding** = `(NegativeFlank(Kreisel - ERROR DIGIT)) OR (not(Show battery Msg))`
- Lit : `Battery Error`, `Battery New Error Code`, `Kreisel - ERROR DIGIT`, `Show battery Msg`
- Utilisé par : *(personne)*
- Ligne export : 36182 · id 67058

#### U_Cell_min_Master  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `913 mBMS_Cell_Info_Master`, `Kreisel - LowCellVoltage`
- Ligne export : 36260 · id 67204

#### Kreisel - LowCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed
- Logique :
  - **Controlling** = `U_Cell_min_Master * 1`
- Lit : `U_Cell_min_Master`
- Utilisé par : `LowCellVoltage`, `Measure group: Battery Kreisel`
- Ligne export : 36273 · id 67205

#### U_Cell_max_Master  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `913 mBMS_Cell_Info_Master`, `Kreisel - HighCellVoltage`
- Ligne export : 36317 · id 67213

#### Kreisel - HighCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed
- Logique :
  - **Controlling** = `U_Cell_max_Master * 1`
- Lit : `U_Cell_max_Master`
- Utilisé par : `HighCellVoltage`, `Measure group: Battery Kreisel`
- Ligne export : 36330 · id 67214

#### U_Cell_avg_Master  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `913 mBMS_Cell_Info_Master`, `AvgCellVoltage`
- Ligne export : 36374 · id 67222

#### AvgCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed
- Logique :
  - **Controlling** = `U_Cell_avg_Master * 1`
- Lit : `U_Cell_avg_Master`
- Utilisé par : `Measure group: Battery Kreisel`
- Ligne export : 36387 · id 67223

#### Cell_T_min_Master  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `913 mBMS_Cell_Info_Master`, `Cell_T_Min_Master`
- Ligne export : 36431 · id 67231

#### Cell_T_Min_Master  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Cell_T_min_Master * 1`
- Lit : `Cell_T_min_Master`
- Utilisé par : `Measure group: Battery Kreisel`
- Ligne export : 36443 · id 67232

#### EVT_Context  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `258 mBMS_ROE`, `Measure group: Battery Kreisel`
- Ligne export : 36487 · id 67240

#### mBMS_ROE_Mux M  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `258 mBMS_ROE`, `Measure group: Battery Kreisel`
- Ligne export : 36500 · id 67241

#### BMS_start_up_ready  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`
- Ligne export : 36512 · id 67242

#### BMS_balancing_act  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`
- Ligne export : 36524 · id 67243

#### BMS_stay_alive  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`
- Ligne export : 36536 · id 67244

#### BMS_iso_meas_act  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`
- Ligne export : 36548 · id 67245

#### BMS_reset_denied  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`
- Ligne export : 36560 · id 67246

#### BMS_wakeup_active  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`
- Ligne export : 36572 · id 67247

#### BMS_Master_available  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`, `BMS_Master_available_IDC`, `BMS_Master_not_available_IDC`
- Ligne export : 36584 · id 67248

#### 277 mBMS_Temp_Info  `GFIN`
- Propriétés : Identifier=277 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{BMS_ext_Temp_Inlet; 32}; {BMS_ext_Temp_Outlet; 16}} · Module=Battery Kreisel (Generic) · Module index=5
- Lit : `BMS_ext_Temp_Inlet`, `BMS_ext_Temp_Outlet`
- Utilisé par : *(personne)*
- Ligne export : 36596 · id 67249

#### BMS_ext_Temp_Inlet  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `277 mBMS_Temp_Info`, `BMS_ext_Temp_Inlet`, `Measure group: Battery Kreisel`
- Ligne export : 36618 · id 67250

#### BMS_ext_Temp_Inlet  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `(BMS_ext_Temp_Inlet * 0,1) - 3276,8`
- Lit : `BMS_ext_Temp_Inlet`
- Utilisé par : `277 mBMS_Temp_Info`, `Measure group: Battery Kreisel`
- Ligne export : 36631 · id 67251

#### BMS_ext_Temp_Outlet  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `277 mBMS_Temp_Info`, `BMS_ext_Temp_Outlet`, `Measure group: Battery Kreisel`
- Ligne export : 36684 · id 67260

#### BMS_ext_Temp_Outlet  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `(BMS_ext_Temp_Outlet * 0,1) - 3276,8`
- Lit : `BMS_ext_Temp_Outlet`
- Utilisé par : `277 mBMS_Temp_Info`, `Measure group: Battery Kreisel`
- Ligne export : 36697 · id 67261

#### 304 mBMS_Version_1  `GFIN`
- Propriétés : Identifier=304 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{VER_CSC_release; 56}; {VER_CSC_minor; 48}; {VER_CSC_major; 40}; {VER_MC_release; 32}; {VER_MC_minor; 24}; {VER_MC_major; 16}; {VER_MC_DS_CRC; 0}} · Module=Battery Kreisel (Generic) · Module index=6
- Lit : `VER_CSC_major`, `VER_CSC_minor`, `VER_CSC_release`, `VER_MC_DS_CRC`, `VER_MC_major`, `VER_MC_minor`, `VER_MC_release`
- Utilisé par : *(personne)*
- Ligne export : 36750 · id 67270

#### VER_CSC_release  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36787 · id 67271

#### VER_MC_release  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36799 · id 67272

#### VER_CSC_minor  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36811 · id 67273

#### VER_CSC_major  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36823 · id 67274

#### VER_MC_minor  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36835 · id 67275

#### VER_MC_major  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36847 · id 67276

#### VER_MC_DS_CRC  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36859 · id 67277

#### 305 mBMS_Version_2  `GFIN`
- Propriétés : Identifier=305 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{VER_CSC_release; 56}; {VER_CSC_minor; 48}; {VER_CSC_major; 40}; {VER_MC_release; 32}; {VER_MC_minor; 24}; {VER_MC_major; 16}; {VER_MC_DS_CRC; 0}} · Module=Battery Kreisel (Generic) · Module index=7
- Lit : `VER_CSC_major`, `VER_CSC_minor`, `VER_CSC_release`, `VER_MC_DS_CRC`, `VER_MC_major`, `VER_MC_minor`, `VER_MC_release`
- Utilisé par : *(personne)*
- Ligne export : 36872 · id 67278

#### VER_CSC_release  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36909 · id 67279

#### VER_MC_release  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36921 · id 67280

#### VER_CSC_minor  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36933 · id 67281

#### VER_CSC_major  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36945 · id 67282

#### VER_MC_minor  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36957 · id 67283

#### VER_MC_major  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36969 · id 67284

#### VER_MC_DS_CRC  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`, `Measure group: Battery Kreisel`
- Ligne export : 36981 · id 67285

#### Func_sys_state_req  `GPOUT`
- Propriétés : Input value=1 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `2047 EXT_FuncRequest`
- Ligne export : 36994 · id 67286

#### Func_MSW_Request_Master  `GPOUT`
- Propriétés : Input value=Switch Battery · Length=1 bit · Type=Unsigned integer
- Lit : `Switch Battery`
- Utilisé par : `2047 EXT_FuncRequest`
- Ligne export : 37005 · id 67287

#### Func_iso_measurement  `GPOUT`
- Propriétés : Input value=1 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `2047 EXT_FuncRequest`
- Ligne export : 37016 · id 67288

#### 2047 EXT_FuncRequest  `GFOUT`
- Propriétés : Identifier=2047 · Data length=8 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={{Func_MSW_Request_Master; 0}; {Func_sys_state_req; 16}; {Func_iso_measurement; 8}} · Module=Battery Kreisel (Generic) · Module index=0
- Lit : `Func_MSW_Request_Master`, `Func_iso_measurement`, `Func_sys_state_req`
- Utilisé par : *(personne)*
- Ligne export : 37027 · id 67289

#### Battery Real SOC  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `BMS_SOC_Master * 0,01`
- Lit : `BMS_SOC_Master`
- Utilisé par : `Measure group: Battery Kreisel`
- Ligne export : 37052 · id 67299

#### BMS_Master_available_IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank((1 = BMS_Master_available))`
- Lit : `BMS_Master_available`
- Utilisé par : `Event log: Electronic Logs`, `Measure group: Battery Kreisel`
- Ligne export : 37096 · id 67364

#### BMS_Master_not_available_IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank((1 = BMS_Master_available))`
- Lit : `BMS_Master_available`
- Utilisé par : `Event log: Electronic Logs`, `Measure group: Battery Kreisel`
- Ligne export : 37149 · id 67373

#### BMS_Master_MSW_Closed_IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank((1 = BMS_Master_MSW_Closed))`
- Lit : `BMS_Master_MSW_Closed`
- Utilisé par : `Event log: Electronic Logs`, `Measure group: Battery Kreisel`
- Ligne export : 37202 · id 67382

#### BMS_Master_MSW_Opened_IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank((1 = BMS_Master_MSW_Closed))`
- Lit : `BMS_Master_MSW_Closed`
- Utilisé par : `Event log: Electronic Logs`, `Measure group: Battery Kreisel`
- Ligne export : 37255 · id 67391

#### Kreisel- Max Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `146`
- Utilisé par : `Max Discharge`
- Ligne export : 37308 · id 70907

## ELEC / BATTERY / WattAlps — actif seulement si `Is WattAlps`

#### BMS_VMU_STATUS  `GFIN`
- Propriétés : Identifier=418382110 · Data length=DonÂt care · Timeout=200 · Paged protocol={Not used} · Parameters={{Heater Command [%]; 40}; {CoolingSystem Command [%]; 32}; {Fan Command [%]; 24}; {Pump Command [%]; 16}; {Balancing Finished; 12}; {AuxiliaryOutputState; 11}; {ImminentOpening; 10}; {End Of Charge; 9}; {BalancingRunning; 8}; {BMS State [State]; 0}} · Module=Battery WattAlps (Generic) · Module index=6
- Lit : `AuxiliaryOutputState`, `BMS State`, `Balancing Finished`, `BalancingRunning`, `CoolingSystem Command`, `End Of Charge`, `Fan Command`, `Heater Command`, `ImminentOpening`, `Pump Command`, `State`
- Utilisé par : `WattAlps - CAN OK`
- Ligne export : 37423 · id 70611

#### Heater Command  `GPIN`
- Propriétés : Unit=% · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 37469 · id 70612

#### CoolingSystem Command  `GPIN`
- Propriétés : Unit=% · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 37481 · id 70613

#### Fan Command  `GPIN`
- Propriétés : Unit=% · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 37493 · id 70614

#### Pump Command  `GPIN`
- Propriétés : Unit=% · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 37505 · id 70615

#### Balancing Finished  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 37517 · id 70616

#### AuxiliaryOutputState  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 37529 · id 70617

#### ImminentOpening  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`, `Switch Battery`, `WattAlps - DRIVE MODE`, `WattApls- ERROR DIGIT`
- Ligne export : 37541 · id 70618

#### End Of Charge  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 37553 · id 70619

#### BalancingRunning  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 37565 · id 70620

#### BMS State  `GPIN`
- Propriétés : Unit=State · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`, `WattAlps - DRIVE MODE`
- Ligne export : 37577 · id 70621

#### BMS_VMU_FAULTS  `GFIN`
- Propriétés : Identifier=418382366 · Data length=DonÂt care · Timeout=600 · Paged protocol={Not used} · Parameters={{Coin Low voltage; 58}; {OilLevel; 57}; {OpenCircuit; 53}; {WrongConfiguration; 56}; {CanCurrentSensorFailure; 55}; {InsulationControlerFailure; 54}; {MainPrechargeSequenceFailure; 52}; {HeatingSystemFailure; 51}; {CoolingSystemFailure; 50}; {Fan Failure; 49}; {OilPump Failure; 48}; {VMU Timeout; 47}; {InsulationMeasurementState; 45}; {InternalCurrentSensorFailure; 44}; {VoltSensorFailure; 43}; {TempSensorFailure; 42}; {ModuleLost; 41}; {InterlockOpened; 40}; {ContactorDamaged; 39}; {AUX2Contactor; 38}; {AUX1Contactor; 37}; {DCContactorMinus; 36}; {DCContactorPlus; 35}; {MainContactorPrecharge; 34}; {MainContactorMinus; 33}; {MainContactorPlus; 32}; {ShutOverVolt; 21}; {AlarmOverVolt; 20}; {WarnOverVolt; 19}; {ShutCriticalDischarge; 18}; {AlarmCriticalDischarge; 17}; {WarnCriticalDischarge; 16}; {ShutOverCurrentDisharge; 29}; {AlarmOverCurrentDisharge; 28}; {WarnOverCurrentDisharge; 27}; {ShutOverCurrentCharge; 26}; {AlarmOverCurrentCharge; 25}; {WarnOverCurrentCharge; 24}; {ShutOverTemp; 13}; {AlarmOverTemp; 12}; {WarnOverTemp; 11}; {ShutLowTemp; 10}; {AlarmLowTemp; 9}; {WarnLowTemp; 8}} · Module=Battery WattAlps (Generic) · Module index=0
- Lit : `AUX1Contactor`, `AUX2Contactor`, `AlarmCriticalDischarge`, `AlarmLowTemp`, `AlarmOverCurrentCharge`, `AlarmOverCurrentDisharge`, `AlarmOverTemp`, `AlarmOverVolt`, `CanCurrentSensorFailure`, `Coin Low voltage`, `ContactorDamaged`, `CoolingSystemFailure`, `DCContactorMinus`, `DCContactorPlus`, `Fan Failure`, `HeatingSystemFailure`, `InsulationControlerFailure`, `InsulationMeasurementState`, `InterlockOpened`, `InternalCurrentSensorFailure`, `MainContactorMinus`, `MainContactorPlus`, `MainContactorPrecharge`, `MainPrechargeSequenceFailure`, `ModuleLost`, `OilLevel`, `OilPump Failure`, `OpenCircuit`, `ShutCriticalDischarge`, `ShutLowTemp`, `ShutOverCurrentCharge`, `ShutOverCurrentDisharge`, `ShutOverTemp`, `ShutOverVolt`, `TempSensorFailure`, `VMU Timeout`, `VoltSensorFailure`, `WarnCriticalDischarge`, `WarnLowTemp`, `WarnOverCurrentCharge`, `WarnOverCurrentDisharge`, `WarnOverTemp`, `WarnOverVolt`, `WrongConfiguration`
- Utilisé par : *(personne)*
- Ligne export : 37589 · id 70622

#### Coin Low voltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Coin Low voltage`, `Event log: WattAlps Battery`
- Ligne export : 37737 · id 70623

#### OilLevel  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `OilLevel`, `Event log: WattAlps Battery`
- Ligne export : 37748 · id 70624

#### OpenCircuit  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `OpenCircuit`, `Event log: WattAlps Battery`
- Ligne export : 37759 · id 70625

#### WrongConfiguration  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `WrongConfiguration`
- Ligne export : 37770 · id 70626

#### CanCurrentSensorFailure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `CanCurrentSensorFailure`, `Event log: WattAlps Battery`
- Ligne export : 37781 · id 70627

#### InsulationControlerFailure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `InsulationControlerFailure`, `Event log: WattAlps Battery`
- Ligne export : 37792 · id 70628

#### MainPrechargeSequenceFailure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `MainPrechargeSequenceFailure`, `Event log: WattAlps Battery`
- Ligne export : 37803 · id 70629

#### HeatingSystemFailure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `HeatingSystemFailure`, `Event log: WattAlps Battery`
- Ligne export : 37814 · id 70630

#### CoolingSystemFailure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `CoolingSystemFailure`, `Event log: WattAlps Battery`
- Ligne export : 37825 · id 70631

#### Fan Failure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Fan Failure`, `Event log: WattAlps Battery`
- Ligne export : 37836 · id 70632

#### OilPump Failure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `OilPump Failure`, `Event log: WattAlps Battery`
- Ligne export : 37847 · id 70633

#### VMU Timeout  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `VMU Timeout`, `Event log: WattAlps Battery`
- Ligne export : 37858 · id 70634

#### InsulationMeasurementState  `GPIN`
- Propriétés : Length=2 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `InsulationMeasurementState`, `Event log: WattAlps Battery`
- Ligne export : 37869 · id 70635

#### InternalCurrentSensorFailure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `InternalCurrentSensorFailure`, `Event log: WattAlps Battery`
- Ligne export : 37880 · id 70636

#### VoltSensorFailure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `VoltSensorFailure`, `Event log: WattAlps Battery`
- Ligne export : 37891 · id 70637

#### TempSensorFailure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `TempSensorFailure`, `Event log: WattAlps Battery`
- Ligne export : 37902 · id 70638

#### ModuleLost  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `ModuleLost`, `Event log: WattAlps Battery`
- Ligne export : 37913 · id 70639

#### InterlockOpened  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `InterlockOpened`, `Event log: WattAlps Battery`
- Ligne export : 37924 · id 70640

#### ContactorDamaged  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `ContactorDamaged`, `Event log: WattAlps Battery`
- Ligne export : 37935 · id 70641

#### AUX2Contactor  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `AUX2Contactor`, `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 37946 · id 70642

#### AUX1Contactor  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `AUX1Contactor`, `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 37957 · id 70643

#### DCContactorMinus  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `DCContactorMinus`, `Event log: WattAlps Battery`
- Ligne export : 37968 · id 70644

#### DCContactorPlus  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `DCContactorPlus`, `Event log: WattAlps Battery`
- Ligne export : 37979 · id 70645

#### MainContactorPrecharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `MainContactorPrecharge`, `Event log: WattAlps Battery`
- Ligne export : 37990 · id 70646

#### MainContactorMinus  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `MainContactorMinus`, `Event log: WattAlps Battery`
- Ligne export : 38001 · id 70647

#### MainContactorPlus  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `MainContactorPlus`, `Event log: WattAlps Battery`
- Ligne export : 38012 · id 70648

#### ShutOverVolt  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `ShutOverVolt`, `Event log: WattAlps Battery`
- Ligne export : 38023 · id 70649

#### AlarmOverVolt  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `AlarmOverVolt`, `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Protection Charge`, `Protection Drive`, `Event log: WattAlps Battery`
- Ligne export : 38034 · id 70650

#### WarnOverVolt  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `WarnOverVolt`, `Event log: WattAlps Battery`
- Ligne export : 38045 · id 70651

#### ShutCriticalDischarge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `ShutCriticalDischarge`, `Event log: WattAlps Battery`
- Ligne export : 38056 · id 70652

#### AlarmCriticalDischarge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `AlarmCriticalDischarge`, `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Protection Drive`, `Event log: WattAlps Battery`
- Ligne export : 38067 · id 70653

#### WarnCriticalDischarge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `WarnCriticalDischarge`, `Event log: WattAlps Battery`
- Ligne export : 38078 · id 70654

#### ShutOverCurrentDisharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `ShutOverCurrentDisharge`, `Event log: WattAlps Battery`
- Ligne export : 38089 · id 70655

#### AlarmOverCurrentDisharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `AlarmOverCurrentDisharge`, `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Protection Drive`, `Event log: WattAlps Battery`
- Ligne export : 38100 · id 70656

#### WarnOverCurrentDisharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `WarnOverCurrentDisharge`, `Event log: WattAlps Battery`
- Ligne export : 38111 · id 70657

#### ShutOverCurrentCharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `ShutOverCurrentCharge`, `Event log: WattAlps Battery`
- Ligne export : 38122 · id 70658

#### AlarmOverCurrentCharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `AlarmOverCurrentCharge`, `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Protection Charge`, `Event log: WattAlps Battery`
- Ligne export : 38133 · id 70659

#### WarnOverCurrentCharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `WarnOverCurrentCharge`, `Event log: WattAlps Battery`
- Ligne export : 38144 · id 70660

#### ShutOverTemp  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `ShutOverTemp`
- Ligne export : 38155 · id 70661

#### AlarmOverTemp  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `AlarmOverTemp`, `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Protection Charge`, `Protection Drive`, `Event log: WattAlps Battery`
- Ligne export : 38166 · id 70662

#### WarnOverTemp  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `WarnOverTemp`, `Event log: WattAlps Battery`
- Ligne export : 38177 · id 70663

#### ShutLowTemp  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `ShutLowTemp`, `Event log: WattAlps Battery`
- Ligne export : 38188 · id 70664

#### AlarmLowTemp  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `AlarmLowTemp`, `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Protection Charge`, `Protection Drive`, `Event log: WattAlps Battery`
- Ligne export : 38199 · id 70665

#### WarnLowTemp  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `WarnLowTemp`, `Event log: WattAlps Battery`
- Ligne export : 38210 · id 70666

#### BMS_VMU_INFO  `GFIN`
- Propriétés : Identifier=418382622 · Data length=DonÂt care · Timeout=600 · Paged protocol={Not used} · Parameters={{SOH [%]; 40}; {SOC [%]; 32}; {BatteryCurrent; 16}; {BatteryVoltageBeforeContactors [V]; 0}; {BatteryVoltageAfterContactors [V]; 48}} · Module=Battery WattAlps (Generic) · Module index=1
- Lit : `BatteryCurrent`, `BatteryVoltageAfterContactors`, `BatteryVoltageBeforeContactors`, `SOC`, `SOH`
- Utilisé par : *(personne)*
- Ligne export : 38221 · id 70667

#### SOH  `GPIN`
- Propriétés : Unit=% · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_INFO`
- Ligne export : 38252 · id 70668

#### SOC  `GPIN`
- Propriétés : Unit=% · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_INFO`, `WattAlps - SOC`
- Ligne export : 38264 · id 70669

#### BatteryCurrent  `GPIN`
- Propriétés : Length=16 · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_INFO`, `WattAlps - CURRENT`
- Ligne export : 38276 · id 70670

#### BatteryVoltageBeforeContactors  `GPIN`
- Propriétés : Unit=V · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_INFO`, `WattAlps - Battery InstantVoltage`
- Ligne export : 38289 · id 70671

#### BMS_VMU_CHARGE  `GFIN`
- Propriétés : Identifier=418382878 · Data length=DonÂt care · Timeout=200 · Paged protocol={Not used} · Parameters={{MaxRegenerativeCurrent [A]; 16}; {MaxDischargeCurrent [A]; 0}; {ChargeVoltageSetpoint [V]; 48}; {ChargeCurrentSetpoint [A]; 32}} · Module=Battery WattAlps (Generic) · Module index=2
- Lit : `ChargeCurrentSetpoint`, `ChargeVoltageSetpoint`, `MaxDischargeCurrent`, `MaxRegenerativeCurrent`
- Utilisé par : *(personne)*
- Ligne export : 38302 · id 70672

#### MaxRegenerativeCurrent  `GPIN`
- Propriétés : Unit=A · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_CHARGE`
- Ligne export : 38330 · id 70673

#### MaxDischargeCurrent  `GPIN`
- Propriétés : Unit=A · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_CHARGE`, `WattAlps- Max Current`
- Ligne export : 38343 · id 70674

#### ChargeVoltageSetpoint  `GPIN`
- Propriétés : Unit=V · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_CHARGE`
- Ligne export : 38356 · id 70675

#### ChargeCurrentSetpoint  `GPIN`
- Propriétés : Unit=A · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_CHARGE`
- Ligne export : 38369 · id 70676

#### BMS_VMU_TRACE  `GFIN`
- Propriétés : Identifier=418383134 · Data length=DonÂt care · Timeout=600 · Paged protocol={Not used} · Parameters={{DaisyChain Number; 0}; {BatteryAverageTemperature [Degrees]; 56}; {CurrentModule Number; 2}; {CellMinVoltage; 8}; {CellMaxVoltage; 24}; {BatteryMinTemperature [Degrees Celsius]; 40}; {BatteryMaxTemperature; 48}} · Module=Battery WattAlps (Generic) · Module index=3
- Lit : `BatteryAverageTemperature`, `BatteryMaxTemperature`, `BatteryMinTemperature`, `CellMaxVoltage`, `CellMinVoltage`, `CurrentModule Number`, `DaisyChain Number`
- Utilisé par : *(personne)*
- Ligne export : 38382 · id 70677

#### DaisyChain Number  `GPIN`
- Propriétés : Length=2 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_TRACE`
- Ligne export : 38419 · id 70678

#### BatteryAverageTemperature  `GPIN`
- Propriétés : Unit=Degrees · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_TRACE`
- Ligne export : 38431 · id 70679

#### CurrentModule Number  `GPIN`
- Propriétés : Length=6 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_TRACE`
- Ligne export : 38443 · id 70680

#### CellMinVoltage  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_TRACE`, `WattAlps - LowCellVoltage`
- Ligne export : 38455 · id 70681

#### CellMaxVoltage  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_TRACE`, `WattAlps - HighCellVoltage`
- Ligne export : 38468 · id 70682

#### BatteryMinTemperature  `GPIN`
- Propriétés : Unit=Degrees Celsius · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_TRACE`
- Ligne export : 38481 · id 70683

#### BatteryMaxTemperature  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_TRACE`, `WattAlps - Cell_T_max_Master`
- Ligne export : 38493 · id 70684

#### REVISION  `GFIN`
- Propriétés : Identifier=418383390 · Data length=DonÂt care · Timeout=5000 · Paged protocol={Not used} · Parameters={{wrong configuration slave number [Raw]; 24}; {Hardware revision [Raw]; 16}; {Minor revision [Raw]; 8}; {Major revision [Raw]; 0}} · Module=Battery WattAlps (Generic) · Module index=4
- Lit : `Hardware revision`, `Major revision`, `Minor revision`, `wrong configuration slave number`
- Utilisé par : *(personne)*
- Ligne export : 38505 · id 70685

#### wrong configuration slave number  `GPIN`
- Propriétés : Unit=Raw · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `REVISION`
- Ligne export : 38533 · id 70686

#### Hardware revision  `GPIN`
- Propriétés : Unit=Raw · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `REVISION`
- Ligne export : 38545 · id 70687

#### Minor revision  `GPIN`
- Propriétés : Unit=Raw · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `REVISION`
- Ligne export : 38557 · id 70688

#### Major revision  `GPIN`
- Propriétés : Unit=Raw · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `REVISION`
- Ligne export : 38569 · id 70689

#### INSULATION_RESISTANCE  `GFIN`
- Propriétés : Identifier=418383646 · Data length=DonÂt care · Timeout=3000 · Paged protocol={Not used} · Parameters={{ValueOfInsulationResistance [kohm]; 0}} · Module=Battery WattAlps (Generic) · Module index=5
- Lit : `ValueOfInsulationResistance`
- Utilisé par : *(personne)*
- Ligne export : 38581 · id 70690

#### ValueOfInsulationResistance  `GPIN`
- Propriétés : Unit=kohm · Length=32 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `INSULATION_RESISTANCE`, `WattAlps - Iso_Resist`
- Ligne export : 38600 · id 70691

#### WattAlps - Battery InstantVoltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `0,1 * BatteryVoltageBeforeContactors [V]`
- Lit : `BatteryVoltageBeforeContactors`
- Utilisé par : `Battery InstantVoltage`, `Measure group: Battery WattAlps`
- Ligne export : 38613 · id 70692

#### WattAlps - SOC  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(SOC [%]: 10->0, 95->100, Freeze)`
- Lit : `SOC`
- Utilisé par : `Battery SOC`, `Measure group: Battery WattAlps`
- Ligne export : 38657 · id 70700

#### WattAlps - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `0,1 * BatteryCurrent`
- Lit : `BatteryCurrent`
- Utilisé par : `Current Bat`, `Measure group: Battery WattAlps`
- Ligne export : 38704 · id 70708

#### WattAlps - Cell_T_max_Master  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `BatteryMaxTemperature - 40`
- Lit : `BatteryMaxTemperature`
- Utilisé par : `Cell_T_max_Master`, `Measure group: Battery WattAlps`
- Ligne export : 38748 · id 70716

#### Protection Drive  `IDC`
> LevÃ©e de dÃ©faut bloquant l'Ã©tat Drive
- Propriétés : Toggle=No · Delay on=5000 · Delay off=10000
- Logique :
  - **Activating** = `AlarmCriticalDischarge OR AlarmLowTemp OR AlarmOverCurrentDisharge OR AlarmOverTemp OR AlarmOverVolt`
- Lit : `AlarmCriticalDischarge`, `AlarmLowTemp`, `AlarmOverCurrentDisharge`, `AlarmOverTemp`, `AlarmOverVolt`
- Utilisé par : `Protection WhattApls`, `Request Parameter State`
- Ligne export : 38792 · id 85480

#### Protection Charge  `IDC`
> LevÃ©e de dÃ©faut bloquant l'Ã©tat Charge
- Propriétés : Toggle=No · Delay on=5000 · Delay off=10000
- Logique :
  - **Activating** = `AlarmLowTemp OR AlarmOverCurrentCharge OR AlarmOverTemp OR AlarmOverVolt`
- Lit : `AlarmLowTemp`, `AlarmOverCurrentCharge`, `AlarmOverTemp`, `AlarmOverVolt`
- Utilisé par : `Protection WhattApls`, `Request Parameter State`
- Ligne export : 38863 · id 85491

#### Switch Battery  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Main Switch Battery`
  - **Blocking** = `ImminentOpening`
- Lit : `ImminentOpening`, `Main Switch Battery`
- Utilisé par : `Request Parameter State`
- Ligne export : 38927 · id 70782

#### Request Parameter State  `SMC`
- Propriétés : Default state name=Standby
- Fonction *Charge* :
  - **Activating** = `(Charger CHARGING) AND (Switch Battery)`
  - **Blocking** = `Protection Charge`
- Fonction *Drive* :
  - **Activating** = `Switch Battery`
  - **Blocking** = `(Charger CHARGING) OR (Protection Drive)`
- Lit : `Charger CHARGING`, `Protection Charge`, `Protection Drive`, `Switch Battery`
- Utilisé par : `Protection WhattApls`, `Request Parameter`
- Ligne export : 38977 · id 70790

#### Protection WhattApls  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Request Parameter State
- Fonction *Standby* :
  - **Activating** = `(Protection Drive) OR (Protection Charge)`
- Fonction *Charge* :
  - **Activating** = `Protection Charge`
- Fonction *Drive* :
  - **Activating** = `Protection Drive`
- Lit : `Protection Charge`, `Protection Drive`, `Request Parameter State`
- Utilisé par : `WattApls- ERROR DIGIT`
- Ligne export : 39076 · id 85528

#### WattApls- ERROR DIGIT  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=100
- Logique :
  - **Activating** = `ImminentOpening OR (Protection WhattApls)`
- Lit : `ImminentOpening`, `Protection WhattApls`
- Utilisé par : `Battery ERROR DIGIT`, `Measure group: Battery WattAlps`
- Ligne export : 39188 · id 70724

#### WattAlps - Iso_Resist  `MAC`
- Propriétés : Unit=kOhm · Limiting object group=Signed
- Logique :
  - **Controlling** = `ValueOfInsulationResistance [kohm] * 1`
- Lit : `ValueOfInsulationResistance`
- Utilisé par : `BMS_Iso_Resist`, `Measure group: Battery WattAlps`
- Ligne export : 39238 · id 70732

#### WattAlps - DRIVE MODE  `IDC`
> Kreisel 
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `2 = BMS State [State]`
  - **Blocking** = `ImminentOpening`
- Lit : `BMS State`, `ImminentOpening`
- Utilisé par : `Battery DRIVE MODE`, `Measure group: Battery WattAlps`
- Ligne export : 39282 · id 70740

#### WattAlps - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `BMS_VMU_STATUS`
- Lit : `BMS_VMU_STATUS`
- Utilisé par : `Battery CAN OK`, `Measure group: Battery WattAlps`
- Ligne export : 39334 · id 70749

#### BatteryVoltageAfterContactors  `GPIN`
- Propriétés : Unit=V · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_INFO`, `WattAlps- U_Trac`
- Ligne export : 39377 · id 70757

#### WattAlps- U_Trac  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `0,1 * BatteryVoltageAfterContactors [V]`
- Lit : `BatteryVoltageAfterContactors`
- Utilisé par : `BMS_U_Trac`, `Measure group: Battery WattAlps`
- Ligne export : 39390 · id 70758

#### WattAlps - LowCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed
- Logique :
  - **Controlling** = `CellMinVoltage`
- Lit : `CellMinVoltage`
- Utilisé par : `LowCellVoltage`, `Measure group: Battery WattAlps`
- Ligne export : 39434 · id 70766

#### WattAlps - HighCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed
- Logique :
  - **Controlling** = `CellMaxVoltage`
- Lit : `CellMaxVoltage`
- Utilisé par : `HighCellVoltage`, `Measure group: Battery WattAlps`
- Ligne export : 39476 · id 70774

#### Request Parameter  `IP`
- Propriétés : Mode selector=Request Parameter State · Default mode: Standby={0} · Mode 1: Charge={1} · Mode 2: Drive={2}
- Lit : `Request Parameter State`
- Utilisé par : `UBMSModeRequestBMS`
- Ligne export : 39518 · id 70804

#### UBMSModeRequestBMS  `GPOUT`
- Propriétés : Input value=Request Parameter · Length=3 · Type=Unsigned integer
- Lit : `Request Parameter`
- Utilisé par : `VMU_BMS_INFO`
- Ligne export : 39534 · id 70805

#### VMU_BMS_INFO  `GFOUT`
- Propriétés : Identifier=402726400 · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Parameters={{UBMSModeRequestBMS; 0}} · Module=Battery WattAlps (Generic) · Module index=0
- Lit : `UBMSModeRequestBMS`
- Utilisé par : *(personne)*
- Ligne export : 39545 · id 70806

#### WattAlps- Max Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxDischargeCurrent [A]`
- Lit : `MaxDischargeCurrent`
- Utilisé par : `Max Discharge`, `Measure group: Battery WattAlps`
- Ligne export : 39564 · id 70807

#### Coin Low voltage  `GPOUT`
- Propriétés : Input value=Coin Low voltage · Length=1 · Type=Digital
- Lit : `Coin Low voltage`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39606 · id 84872

#### OilLevel  `GPOUT`
- Propriétés : Input value=OilLevel · Length=1 · Type=Digital
- Lit : `OilLevel`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39617 · id 84873

#### OpenCircuit  `GPOUT`
- Propriétés : Input value=OpenCircuit · Length=1 · Type=Digital
- Lit : `OpenCircuit`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39628 · id 84874

#### WrongConfiguration  `GPOUT`
- Propriétés : Input value=WrongConfiguration · Length=1 · Type=Digital
- Lit : `WrongConfiguration`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`
- Ligne export : 39639 · id 84875

#### CanCurrentSensorFailure  `GPOUT`
- Propriétés : Input value=CanCurrentSensorFailure · Length=1 · Type=Digital
- Lit : `CanCurrentSensorFailure`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39650 · id 84876

#### InsulationControlerFailure  `GPOUT`
- Propriétés : Input value=InsulationControlerFailure · Length=1 · Type=Digital
- Lit : `InsulationControlerFailure`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39661 · id 84877

#### MainPrechargeSequenceFailure  `GPOUT`
- Propriétés : Input value=MainPrechargeSequenceFailure · Length=1 · Type=Digital
- Lit : `MainPrechargeSequenceFailure`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39672 · id 84878

#### HeatingSystemFailure  `GPOUT`
- Propriétés : Input value=HeatingSystemFailure · Length=1 · Type=Digital
- Lit : `HeatingSystemFailure`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39683 · id 84879

#### CoolingSystemFailure  `GPOUT`
- Propriétés : Input value=CoolingSystemFailure · Length=1 · Type=Digital
- Lit : `CoolingSystemFailure`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39694 · id 84880

#### Fan Failure  `GPOUT`
- Propriétés : Input value=Fan Failure · Length=1 · Type=Digital
- Lit : `Fan Failure`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39705 · id 84881

#### OilPump Failure  `GPOUT`
- Propriétés : Input value=OilPump Failure · Length=1 · Type=Digital
- Lit : `OilPump Failure`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39716 · id 84882

#### VMU Timeout  `GPOUT`
- Propriétés : Input value=VMU Timeout · Length=1 · Type=Digital
- Lit : `VMU Timeout`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39727 · id 84883

#### InsulationMeasurementState  `GPOUT`
- Propriétés : Input value=InsulationMeasurementState · Length=2 · Type=Digital
- Lit : `InsulationMeasurementState`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39738 · id 84884

#### InternalCurrentSensorFailure  `GPOUT`
- Propriétés : Input value=InternalCurrentSensorFailure · Length=1 · Type=Digital
- Lit : `InternalCurrentSensorFailure`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39749 · id 84885

#### VoltSensorFailure  `GPOUT`
- Propriétés : Input value=VoltSensorFailure · Length=1 · Type=Digital
- Lit : `VoltSensorFailure`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39760 · id 84886

#### TempSensorFailure  `GPOUT`
- Propriétés : Input value=TempSensorFailure · Length=1 · Type=Digital
- Lit : `TempSensorFailure`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39771 · id 84887

#### ModuleLost  `GPOUT`
- Propriétés : Input value=ModuleLost · Length=1 · Type=Digital
- Lit : `ModuleLost`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39782 · id 84888

#### InterlockOpened  `GPOUT`
- Propriétés : Input value=InterlockOpened · Length=1 · Type=Digital
- Lit : `InterlockOpened`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39793 · id 84889

#### ContactorDamaged  `GPOUT`
- Propriétés : Input value=ContactorDamaged · Length=1 · Type=Digital
- Lit : `ContactorDamaged`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39804 · id 84890

#### AUX2Contactor  `GPOUT`
- Propriétés : Input value=AUX2Contactor · Length=1 · Type=Digital
- Lit : `AUX2Contactor`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39815 · id 84891

#### AUX1Contactor  `GPOUT`
- Propriétés : Input value=AUX1Contactor · Length=1 · Type=Digital
- Lit : `AUX1Contactor`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39826 · id 84892

#### DCContactorMinus  `GPOUT`
- Propriétés : Input value=DCContactorMinus · Length=1 · Type=Digital
- Lit : `DCContactorMinus`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39837 · id 84893

#### DCContactorPlus  `GPOUT`
- Propriétés : Input value=DCContactorPlus · Length=1 · Type=Digital
- Lit : `DCContactorPlus`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39848 · id 84894

#### MainContactorPrecharge  `GPOUT`
- Propriétés : Input value=MainContactorPrecharge · Length=1 · Type=Digital
- Lit : `MainContactorPrecharge`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39859 · id 84895

#### MainContactorMinus  `GPOUT`
- Propriétés : Input value=MainContactorMinus · Length=1 · Type=Digital
- Lit : `MainContactorMinus`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39870 · id 84896

#### MainContactorPlus  `GPOUT`
- Propriétés : Input value=MainContactorPlus · Length=1 · Type=Digital
- Lit : `MainContactorPlus`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39881 · id 84897

#### ShutOverVolt  `GPOUT`
- Propriétés : Input value=ShutOverVolt · Length=1 · Type=Digital
- Lit : `ShutOverVolt`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39892 · id 84898

#### AlarmOverVolt  `GPOUT`
- Propriétés : Input value=AlarmOverVolt · Length=1 · Type=Digital
- Lit : `AlarmOverVolt`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Protection Charge`, `Protection Drive`, `Event log: WattAlps Battery`
- Ligne export : 39903 · id 84899

#### WarnOverVolt  `GPOUT`
- Propriétés : Input value=WarnOverVolt · Length=1 · Type=Digital
- Lit : `WarnOverVolt`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39914 · id 84900

#### ShutCriticalDischarge  `GPOUT`
- Propriétés : Input value=ShutCriticalDischarge · Length=1 · Type=Digital
- Lit : `ShutCriticalDischarge`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39925 · id 84901

#### AlarmCriticalDischarge  `GPOUT`
- Propriétés : Input value=AlarmCriticalDischarge · Length=1 · Type=Digital
- Lit : `AlarmCriticalDischarge`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Protection Drive`, `Event log: WattAlps Battery`
- Ligne export : 39936 · id 84902

#### WarnCriticalDischarge  `GPOUT`
- Propriétés : Input value=WarnCriticalDischarge · Length=1 · Type=Digital
- Lit : `WarnCriticalDischarge`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39947 · id 84903

#### ShutOverCurrentDisharge  `GPOUT`
- Propriétés : Input value=ShutOverCurrentDisharge · Length=1 · Type=Digital
- Lit : `ShutOverCurrentDisharge`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39958 · id 84904

#### AlarmOverCurrentDisharge  `GPOUT`
- Propriétés : Input value=AlarmOverCurrentDisharge · Length=1 · Type=Digital
- Lit : `AlarmOverCurrentDisharge`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Protection Drive`, `Event log: WattAlps Battery`
- Ligne export : 39969 · id 84905

#### WarnOverCurrentDisharge  `GPOUT`
- Propriétés : Input value=WarnOverCurrentDisharge · Length=1 · Type=Digital
- Lit : `WarnOverCurrentDisharge`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39980 · id 84906

#### ShutOverCurrentCharge  `GPOUT`
- Propriétés : Input value=ShutOverCurrentCharge · Length=1 · Type=Digital
- Lit : `ShutOverCurrentCharge`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 39991 · id 84907

#### AlarmOverCurrentCharge  `GPOUT`
- Propriétés : Input value=AlarmOverCurrentCharge · Length=1 · Type=Digital
- Lit : `AlarmOverCurrentCharge`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Protection Charge`, `Event log: WattAlps Battery`
- Ligne export : 40002 · id 84908

#### WarnOverCurrentCharge  `GPOUT`
- Propriétés : Input value=WarnOverCurrentCharge · Length=1 · Type=Digital
- Lit : `WarnOverCurrentCharge`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 40013 · id 84909

#### ShutOverTemp  `GPOUT`
- Propriétés : Input value=ShutOverTemp · Length=1 · Type=Digital
- Lit : `ShutOverTemp`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`
- Ligne export : 40024 · id 84910

#### AlarmOverTemp  `GPOUT`
- Propriétés : Input value=AlarmOverTemp · Length=1 · Type=Digital
- Lit : `AlarmOverTemp`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Protection Charge`, `Protection Drive`, `Event log: WattAlps Battery`
- Ligne export : 40035 · id 84911

#### WarnOverTemp  `GPOUT`
- Propriétés : Input value=WarnOverTemp · Length=1 · Type=Digital
- Lit : `WarnOverTemp`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 40046 · id 84912

#### ShutLowTemp  `GPOUT`
- Propriétés : Input value=ShutLowTemp · Length=1 · Type=Digital
- Lit : `ShutLowTemp`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 40057 · id 84913

#### AlarmLowTemp  `GPOUT`
- Propriétés : Input value=AlarmLowTemp · Length=1 · Type=Digital
- Lit : `AlarmLowTemp`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Protection Charge`, `Protection Drive`, `Event log: WattAlps Battery`
- Ligne export : 40068 · id 84914

#### WarnLowTemp  `GPOUT`
- Propriétés : Input value=WarnLowTemp · Length=1 · Type=Digital
- Lit : `WarnLowTemp`
- Utilisé par : `BMS_VMU_FAULTS`, `BMS_VMU_FAULTS`, `Event log: WattAlps Battery`
- Ligne export : 40079 · id 84915

#### BMS_VMU_FAULTS  `GFOUT`
- Propriétés : Identifier=418382367 · Data length=8 · Send method=On change · Unused bits=Set to 0 · Parameters={{Coin Low voltage; 58}; {OilLevel; 57}; {OpenCircuit; 53}; {WrongConfiguration; 56}; {CanCurrentSensorFailure; 55}; {InsulationControlerFailure; 54}; {MainPrechargeSequenceFailure; 52}; {HeatingSystemFailure; 51}; {CoolingSystemFailure; 50}; {Fan Failure; 49}; {OilPump Failure; 48}; {VMU Timeout; 47}; {InsulationMeasurementState; 45}; {InternalCurrentSensorFailure; 44}; {VoltSensorFailure; 43}; {TempSensorFailure; 42}; {ModuleLost; 41}; {InterlockOpened; 40}; {ContactorDamaged; 39}; {AUX2Contactor; 38}; {AUX1Contactor; 37}; {DCContactorMinus; 36}; {DCContactorPlus; 35}; {MainContactorPrecharge; 34}; {MainContactorMinus; 33}; {MainContactorPlus; 32}; {ShutOverVolt; 21}; {AlarmOverVolt; 20}; {WarnOverVolt; 19}; {ShutCriticalDischarge; 18}; {AlarmCriticalDischarge; 17}; {WarnCriticalDischarge; 16}; {ShutOverCurrentDisharge; 29}; {AlarmOverCurrentDisharge; 28}; {WarnOverCurrentDisharge; 27}; {ShutOverCurrentCharge; 26}; {AlarmOverCurrentCharge; 25}; {WarnOverCurrentCharge; 24}; {ShutOverTemp; 13}; {AlarmOverTemp; 12}; {WarnOverTemp; 11}; {ShutLowTemp; 10}; {AlarmLowTemp; 9}; {WarnLowTemp; 8}} · Module=Battery WattAlps (Generic) · Module index=1
- Lit : `AUX1Contactor`, `AUX2Contactor`, `AlarmCriticalDischarge`, `AlarmLowTemp`, `AlarmOverCurrentCharge`, `AlarmOverCurrentDisharge`, `AlarmOverTemp`, `AlarmOverVolt`, `CanCurrentSensorFailure`, `Coin Low voltage`, `ContactorDamaged`, `CoolingSystemFailure`, `DCContactorMinus`, `DCContactorPlus`, `Fan Failure`, `HeatingSystemFailure`, `InsulationControlerFailure`, `InsulationMeasurementState`, `InterlockOpened`, `InternalCurrentSensorFailure`, `MainContactorMinus`, `MainContactorPlus`, `MainContactorPrecharge`, `MainPrechargeSequenceFailure`, `ModuleLost`, `OilLevel`, `OilPump Failure`, `OpenCircuit`, `ShutCriticalDischarge`, `ShutLowTemp`, `ShutOverCurrentCharge`, `ShutOverCurrentDisharge`, `ShutOverTemp`, `ShutOverVolt`, `TempSensorFailure`, `VMU Timeout`, `VoltSensorFailure`, `WarnCriticalDischarge`, `WarnLowTemp`, `WarnOverCurrentCharge`, `WarnOverCurrentDisharge`, `WarnOverTemp`, `WarnOverVolt`, `WrongConfiguration`
- Utilisé par : *(personne)*
- Ligne export : 40090 · id 84871

#### WattAlps Debug  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `VMU_BMS_Diag`, `WattAlps Debug`, `Adjust group: Master Battery`, `Single adjust item: WattAlps Debug`
- Ligne export : 40238 · id 85228

#### WattAlps Debug  `GPOUT`
- Propriétés : Input value=WattAlps Debug · Length=1 bit · Type=Unsigned integer
- Lit : `WattAlps Debug`
- Utilisé par : `VMU_BMS_Diag`, `Adjust group: Master Battery`, `Single adjust item: WattAlps Debug`
- Ligne export : 40251 · id 85222

#### VMU_BMS_Diag  `GFOUT`
- Propriétés : Identifier=0x18021E00 · Data length=8 · Send method=Continuously · Transmit rate=400 · Unused bits=Set to 0 · Parameters={{WattAlps Debug; 0}} · Module=Battery WattAlps (Generic) · Module index=2
- Lit : `WattAlps Debug`
- Utilisé par : *(personne)*
- Ligne export : 40262 · id 85220

## ELEC / CHARGER

#### Max Current Line  `IP`
- Propriétés : Unit=A · Default mode={10}
- Utilisé par : `1560 - Max Current from 230 V`, `HV Current`, `Single adjust item: Charging Current`
- Ligne export : 42953 · id 36754

#### Charger CONNECT to 220V  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Elcon Connected) OR (Brusa Connected) OR (BMW Connected)`
- Lit : `BMW Connected`, `Brusa Connected`, `Elcon Connected`
- Utilisé par : `Charger State Finite`, `Reset State`
- Ligne export : 42965 · id 36773

#### Charger ERROR  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=100
- Logique :
  - **Activating** = `(Brusa Error) OR (Elcon Error) OR (BMW Error)`
- Lit : `BMW Error`, `Brusa Error`, `Elcon Error`
- Utilisé par : `Charger STATE`, `Reset State`
- Ligne export : 43022 · id 36790

#### Charger READY  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `(Brusa ready) OR (Elcon Ready) OR (BMW Ready)`
- Lit : `BMW Ready`, `Brusa ready`, `Elcon Ready`
- Utilisé par : `Charger State Finite`
- Ligne export : 43079 · id 36936

#### Charger CHARGING  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `(Elcon Charging) OR (Brusa Charging) OR (BMW Charging)`
- Lit : `BMW Charging`, `Brusa Charging`, `Elcon Charging`
- Utilisé par : `Charge Mode`, `Charger Charging`, `Charger STATE`, `Charger State Finite`, `Request Parameter State`
- Ligne export : 43136 · id 36944

#### Reset State  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(NegativeFlank(Charger CONNECT to 220V)) OR (PositiveFlank(Charger ERROR)) OR (NegativeFlank(Battery DRIVE MODE))`
- Lit : `Battery DRIVE MODE`, `Charger CONNECT to 220V`, `Charger ERROR`
- Utilisé par : `Charger State Finite`
- Ligne export : 43193 · id 52042

#### Charger State Finite  `FSM`
- Propriétés : Store value=No · Resetting channel=Reset State
- État 0 **OFF**
  - transition *Connected to 220 V* (état cible non exporté par IQANdesign)
    - **Activating** = `Charger CONNECT to 220V`
- État 1 **Connected**
  - transition *Battery need to charge* (état cible non exporté par IQANdesign)
    - **Activating** = `(Charger READY) AND (Battery NEED TO CHARGE)`
- État 2 **Need to Charge**
  - transition *Wait Battery Start* (état cible non exporté par IQANdesign)
    - **Activating** = `Battery DRIVE MODE`
- État 3 **Battery Started**
  - transition *Cmd Charge* (état cible non exporté par IQANdesign)
    - **Activating** = `Charger CHARGING`
- État 4 **Charging**
  - transition *Charged* (état cible non exporté par IQANdesign)
    - **Activating** = `Battery CHARGED`
- État 5 **Charged**
  - transition *Reset* (état cible non exporté par IQANdesign)
    - **Activating** = `Flank(MD4 - Start Button Blocking Neutral)`
- Lit : `Battery CHARGED`, `Battery DRIVE MODE`, `Battery NEED TO CHARGE`, `Charger CHARGING`, `Charger CONNECT to 220V`, `Charger READY`, `MD4 - Start Button Blocking Neutral`, `Reset State`
- Utilisé par : `Battery start by charger`, `Charger Charging State`, `Charger DIGITAL CMD`, `Charger State Finite`
- Ligne export : 43253 · id 52050

#### Charger DIGITAL CMD  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Charger State Finite = 3) OR (Charger State Finite = 4)`
  - **Blocking** = `not(Battery DRIVE MODE)`
- Lit : `Battery DRIVE MODE`, `Charger State Finite`
- Utilisé par : `CMD`, `CMD`, `Timer charging`
- Ligne export : 43475 · id 36798

#### Desired Voltage  `IP`
- Propriétés : Unit=V · Mode selector=Battery Brand · Default mode: Kreisel={375} · Mode 1: BMW={390} · Mode 2: WattApls={390}
- Lit : `Battery Brand`
- Utilisé par : `1560 - Desired Voltage`, `Charger end charge`, `HV Current`, `Math Voltage`, `Math Voltage`, `Adjust group: Master Battery`, `Single adjust item: Desired Voltage`
- Ligne export : 43537 · id 36852

#### Charger CAN BUS OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Brusa CAN OK) OR (Elcon CAN OK) OR (BMW CAN OK)`
- Lit : `BMW CAN OK`, `Brusa CAN OK`, `Elcon CAN OK`
- Utilisé par : `Charger STATE`, `MD4-10 page: INFO`
- Ligne export : 43553 · id 36928

#### Charger STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ERROR* :
  - **Activating** = `Charger ERROR`
- Fonction *READY* :
  - **Activating** = `Charger CAN BUS OK`
  - **Blocking** = `(Charger ERROR) OR (Charger CHARGING)`
- Fonction *RUN 220V* :
  - **Activating** = `Charger CHARGING`
  - **Blocking** = `Charger ERROR`
- Lit : `Charger CAN BUS OK`, `Charger CHARGING`, `Charger ERROR`
- Utilisé par : `Charger STATE`, `Charger STATE`
- Ligne export : 43610 · id 36952

#### Battery start by charger  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Charger State Finite = 2) OR (Charger State Finite = 3) OR (Charger State Finite = 4)`
- Lit : `Charger State Finite`
- Utilisé par : `Battery DIGITAL`
- Ligne export : 43733 · id 52096

#### Charger Brand  `SP`
- Propriétés : Input channel=None · Default state name=Brusa · States={Elcon; BMW; Valeo}
- Utilisé par : `Charger Output Current`, `Is Charger BMW`, `Is Charger Brusa`, `Is Charger Elcon`, `Is Charger Valeo`, `Adjust group: Config Electric Drive`, `Single adjust item: Charger Brand`
- Ligne export : 43796 · id 57855

#### Is Charger Brusa  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Charger Brand = 0`
- Lit : `Charger Brand`
- Utilisé par : `Active le groupe: ELEC / CHARGER / Brusa`, `Measure group: Charger Brusa`
- Ligne export : 43810 · id 58192

#### Input Voltage  `SP`
- Propriétés : Input channel=None · Default state name=220 V · States={110 V}
- Utilisé par : `Input Voltage Value`, `Adjust group: Charger Setup`, `Measure group: Charger Elcon`, `Single adjust item: Input Voltage`
- Ligne export : 43855 · id 58731

#### Input Voltage Value  `IP`
- Propriétés : Unit=V · Mode selector=Input Voltage · Default mode: 220 V={230} · Mode 1: 110 V={110}
- Lit : `Input Voltage`
- Utilisé par : `HV Current`
- Ligne export : 43867 · id 58874

#### HV Current  `MAC`
- Logique :
  ```qcode
  Result := MinOf(Input Voltage Value  * Max Current Line / Desired Voltage, 10)
  ```
- Lit : `Desired Voltage`, `Input Voltage Value`, `Max Current Line`
- Utilisé par : `1560 - Desired Current`, `Math Current`, `Math Current`
- Ligne export : 43881 · id 58858

#### Is Charger Elcon  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Charger Brand = 1`
- Lit : `Charger Brand`
- Utilisé par : `Active le groupe: ELEC / CHARGER / Elcon`, `Measure group: Charger Elcon`
- Ligne export : 45133 · id 58203

#### Charger Output Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=Charger Brand
- Fonction *Brusa* :
  - **Controlling** = `1553 - output current to the battery [A]`
- Fonction *Elcon* :
  - **Controlling** = `Elcon - output current`
- Fonction *BMW* :
  - **Controlling** = `BMW - Output current [A]`
- Fonction *Valeo* : (vide)
- Lit : `1553 - output current to the battery`, `BMW - Output current`, `Charger Brand`, `Elcon - output current`
- Utilisé par : `Charger end charge`, `MD4-10 page: INFO`
- Ligne export : 45863 · id 58886

#### Is Charger BMW  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Charger Brand = 2`
- Lit : `Charger Brand`
- Utilisé par : `Active le groupe: ELEC / CHARGER / BMW`, `Measure group: Charger BMW`
- Ligne export : 45991 · id 68074

#### Is Charger Valeo  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Charger Brand = 3`
- Lit : `Charger Brand`
- Utilisé par : `Active le groupe: ELEC / CHARGER / Valeo`
- Ligne export : 47097 · id 68851

#### Charger end charge  `IDC`
- Propriétés : Toggle=No · Delay on=3600000 · Delay off=0
- Logique :
  - **Activating** = `((Abs(Charger Output Current [A])) <= 0,5) OR ((Desired Voltage [V] - Battery InstantVoltage [V]) < 2)`
- Lit : `Battery InstantVoltage`, `C`, `Charger Output Current`, `Desired Voltage`
- Utilisé par : `Battery CHARGED`
- Ligne export : 47142 · id 85056

## ELEC / CHARGER / BMW — actif seulement si `Is Charger BMW`

#### GFIN-A:Generic  `GFIN`
- Propriétés : Identifier=0x405 · Data length=DonÂt care · Timeout=200 · Paged protocol={Not used} · Parameters={{CHARGER_STATUS; 0}; {CHARGER_MAINS_CURRENT; 8}; {CHARGER_DC_CURRENT; 24}; {CHARGER_DC_VOLTAGE; 40}; {CHARGER_MAINS_FREQUENCY; 56}} · Module=Charger BMW (Generic) · Module index=0
- Lit : `CHARGER_DC_CURRENT`, `CHARGER_DC_VOLTAGE`, `CHARGER_MAINS_CURRENT`, `CHARGER_MAINS_FREQUENCY`, `CHARGER_STATUS`
- Utilisé par : `BMW Ready`
- Ligne export : 46057 · id 68061

#### CHARGER_STATUS  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Digital
- Utilisé par : `BMW - Status`, `GFIN-A:Generic`
- Ligne export : 46088 · id 68062

#### CHARGER_MAINS_CURRENT  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - Main current`, `GFIN-A:Generic`
- Ligne export : 46099 · id 68092

#### CHARGER_DC_CURRENT  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - Output current`, `GFIN-A:Generic`
- Ligne export : 46112 · id 68093

#### CHARGER_DC_VOLTAGE  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - Output Voltage`, `GFIN-A:Generic`
- Ligne export : 46125 · id 68094

#### CHARGER_MAINS_FREQUENCY  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `BMW - Frequency`, `GFIN-A:Generic`
- Ligne export : 46138 · id 68095

#### BMW - Main current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_MAINS_CURRENT / 10`
- Lit : `CHARGER_MAINS_CURRENT`
- Utilisé par : `BMW Charging`, `Measure group: Charger BMW`
- Ligne export : 46150 · id 68096

#### BMW - Output current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_DC_CURRENT / 10`
- Lit : `CHARGER_DC_CURRENT`
- Utilisé par : `Charger Output Current`, `Measure group: Charger BMW`
- Ligne export : 46194 · id 68109

#### BMW - Output Voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_DC_VOLTAGE / 10`
- Lit : `CHARGER_DC_VOLTAGE`
- Utilisé par : `Measure group: Charger BMW`
- Ligne export : 46238 · id 68128

#### BMW - Frequency  `MAC`
- Propriétés : Unit=Hz · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_MAINS_FREQUENCY`
- Lit : `CHARGER_MAINS_FREQUENCY`
- Utilisé par : `Measure group: Charger BMW`
- Ligne export : 46282 · id 68147

#### BMW Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `GFIN-A:Generic`
- Lit : `GFIN-A:Generic`
- Utilisé par : `BMW CAN OK`, `BMW Connected`, `Charger READY`
- Ligne export : 46324 · id 68230

#### BMW Connected  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `BMW Ready`
- Lit : `BMW Ready`
- Utilisé par : `Charger CONNECT to 220V`
- Ligne export : 46367 · id 68238

#### BMW Charging  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `BMW - Main current [A] > 0,5`
- Lit : `BMW - Main current`
- Utilisé par : `Charger CHARGING`
- Ligne export : 46410 · id 68246

#### BMW CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `BMW Ready`
- Lit : `BMW Ready`
- Utilisé par : `Battery CAN OK`, `Charger CAN BUS OK`
- Ligne export : 46455 · id 68254

#### BMW - Status  `MAC`
- Propriétés : Unit=State · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_STATUS`
- Lit : `CHARGER_STATUS`
- Utilisé par : `BMW Error`, `Measure group: Charger BMW`
- Ligne export : 46498 · id 68294

#### BMW Error  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `3 <= BMW - Status [State]`
- Lit : `BMW - Status`
- Utilisé par : `Charger ERROR`
- Ligne export : 46540 · id 68262

#### CMD  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Charger DIGITAL CMD`
- Lit : `Charger DIGITAL CMD`
- Utilisé par : `ENABLE`
- Ligne export : 46585 · id 68403

#### ENABLE  `GPOUT`
- Propriétés : Input value=CMD · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `CMD`
- Utilisé par : `GFOUT-A:Generic`, `Power`
- Ligne export : 46628 · id 68355

#### Power  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(ENABLE * 100) * 10`
- Lit : `ENABLE`
- Utilisé par : `POWER_REFERENCE`, `Measure group: Track Zapi Right`
- Ligne export : 46639 · id 68447

#### POWER_REFERENCE  `GPOUT`
- Propriétés : Input value=Power · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Power`
- Utilisé par : `GFOUT-A:Generic`
- Ligne export : 46699 · id 68358

#### Math Voltage  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Desired Voltage [V] * 10`
- Lit : `Desired Voltage`
- Utilisé par : `MAXDCVOLTLIMIT`
- Ligne export : 46711 · id 68387

#### MAXDCVOLTLIMIT  `GPOUT`
- Propriétés : Input value=Math Voltage · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Math Voltage`
- Utilisé par : `GFOUT-A:Generic`
- Ligne export : 46755 · id 68360

#### Math Current  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `HV Current * 10`
- Lit : `HV Current`
- Utilisé par : `MAXDCCURRLIMIT`
- Ligne export : 46767 · id 68395

#### MAXDCCURRLIMIT  `GPOUT`
- Propriétés : Input value=Math Current · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Math Current`
- Utilisé par : `GFOUT-A:Generic`
- Ligne export : 46811 · id 68361

#### GFOUT-A:Generic  `GFOUT`
- Propriétés : Identifier=0x400 · Data length=8 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{ENABLE; 0}; {POWER_REFERENCE; 8}; {MAXDCVOLTLIMIT; 24}; {MAXDCCURRLIMIT; 40}} · Module=Charger BMW (Generic) · Module index=0
- Lit : `ENABLE`, `MAXDCCURRLIMIT`, `MAXDCVOLTLIMIT`, `POWER_REFERENCE`
- Utilisé par : *(personne)*
- Ligne export : 46823 · id 68354

## ELEC / CHARGER / Brusa — actif seulement si `Is Charger Brusa`

#### 1552 - CAN IN  `GFIN`
- Propriétés : Identifier=1552 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{1552 - Hardware enable - Byte; 7}; {1552 - Error detect - Byte; 6}; {1552 - Warning Condition - Byte; 5}; {1552 - Automatique charging - Byte; 24}} · Module=Charger Brusa (Generic) · Module index=0
- Lit : `1552 - Automatique charging - Byte`, `1552 - Error detect - Byte`, `1552 - Hardware enable - Byte`, `1552 - Warning Condition - Byte`
- Utilisé par : `Brusa CAN OK`
- Ligne export : 43920 · id 58427

#### 1553 - CAN IN  `GFIN`
- Propriétés : Identifier=1553 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{1553 - Actual mains current - Byte; 0}; {1553 - Actual mains voltage - Byte; 16}; {1553 - Actual battery output voltage - Byte; 32}; {1553 - output current to the battery - Byte; 48}} · Module=Charger Brusa (Generic) · Module index=1
- Lit : `1553 - Actual battery output voltage - Byte`, `1553 - Actual mains current - Byte`, `1553 - Actual mains voltage - Byte`, `1553 - output current to the battery - Byte`
- Utilisé par : *(personne)*
- Ligne export : 43948 · id 58428

#### 1553 - Actual mains current - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1553 - Actual mains current`, `1553 - CAN IN`
- Ligne export : 43976 · id 58429

#### 1553 - Actual mains voltage - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1553 - Actual mains voltage`, `1553 - CAN IN`
- Ligne export : 43989 · id 58430

#### 1555 - CAN IN  `GFIN`
- Propriétés : Identifier=1555 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{1555 - Power stage temperature - Byte; 0}} · Module=Charger Brusa (Generic) · Module index=2
- Lit : `1555 - Power stage temperature - Byte`
- Utilisé par : *(personne)*
- Ligne export : 44002 · id 58431

#### 1555 - Power stage temperature - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1555 - CAN IN`, `1555 - Power stage temperature - Byte`, `Measure group: Charger Brusa`
- Ligne export : 44021 · id 58432

#### 1553 - output current to the battery - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1553 - CAN IN`, `1553 - output current to the battery`
- Ligne export : 44034 · id 58433

#### 1553 - output current to the battery  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `1553 - output current to the battery - Byte / 100`
- Lit : `1553 - output current to the battery - Byte`
- Utilisé par : `Brusa Charging`, `Charger Output Current`, `Measure group: Charger Brusa`
- Ligne export : 44047 · id 58434

#### 1553 - Actual battery output voltage - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1553 - Actual battery output voltage`, `1553 - CAN IN`
- Ligne export : 44091 · id 58442

#### 1553 - Actual battery output voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `1553 - Actual battery output voltage - Byte / 10`
- Lit : `1553 - Actual battery output voltage - Byte`
- Utilisé par : `Measure group: Charger Brusa`
- Ligne export : 44104 · id 58443

#### 1552 - Error detect - Byte  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `1552 - CAN IN`, `Brusa Error`
- Ligne export : 44148 · id 58451

#### 1552 - Hardware enable - Byte  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `1552 - CAN IN`, `1552 - Hardware enable - IDC`
- Ligne export : 44159 · id 58452

#### Timer charging  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `(Charger DIGITAL CMD) AND (Timer charging [ms] < 4000)`
  - **Resetting** = `not(Charger DIGITAL CMD)`
- Lit : `Charger DIGITAL CMD`
- Utilisé par : `Charge start state`
- Ligne export : 44170 · id 58453

#### Charge start state  `SMC`
- Propriétés : Default state name=STOP
- Fonction *Clear ERROR* :
  - **Activating** = `Inside(Timer charging [ms], 1000, 2000)`
- Fonction *Charging* :
  - **Activating** = `Timer charging [ms] > 2100`
- Lit : `Timer charging`
- Utilisé par : `1560 - Desired Current`, `1560 - Desired Voltage`, `1560 - Max Current from 230 V`, `Error clear`, `Power`
- Ligne export : 44239 · id 58465

#### 1560 - Max Current from 230 V  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Charge start state
- Fonction *STOP* : (vide)
- Fonction *Clear ERROR* : (vide)
- Fonction *Charging* :
  - **Controlling** = `Max Current Line [A] * 10`
- Lit : `Charge start state`, `Max Current Line`
- Utilisé par : `1560 - Max Current from 230 V - Byte`
- Ligne export : 44315 · id 58477

#### 1560 - Max Current from 230 V - Byte  `GPOUT`
- Propriétés : Input value=1560 - Max Current from 230 V · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `1560 - Max Current from 230 V`
- Utilisé par : `1560 - Cmd`
- Ligne export : 44407 · id 58497

#### 1560 - Desired Voltage  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Charge start state
- Fonction *STOP* : (vide)
- Fonction *Clear ERROR* : (vide)
- Fonction *Charging* :
  - **Controlling** = `Desired Voltage [V] * 10`
- Lit : `Charge start state`, `Desired Voltage`
- Utilisé par : `1560 - Desired Voltage - Byte`
- Ligne export : 44419 · id 58498

#### 1560 - Desired Voltage - Byte  `GPOUT`
- Propriétés : Input value=1560 - Desired Voltage · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `1560 - Desired Voltage`
- Utilisé par : `1560 - Cmd`
- Ligne export : 44511 · id 58518

#### 1560 - Desired Current  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Charge start state
- Fonction *STOP* : (vide)
- Fonction *Clear ERROR* : (vide)
- Fonction *Charging* :
  - **Controlling** = `HV Current * 10`
- Lit : `Charge start state`, `HV Current`
- Utilisé par : `1560 - Desired Current - Byte`
- Ligne export : 44523 · id 58519

#### 1560 - Desired Current - Byte  `GPOUT`
- Propriétés : Input value=1560 - Desired Current · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `1560 - Desired Current`
- Utilisé par : `1560 - Cmd`
- Ligne export : 44615 · id 58539

#### Power  `DP`
- Propriétés : Mode selector=Charge start state · Default mode: STOP={False} · Mode 1: Clear ERROR={False} · Mode 2: Charging={True}
- Lit : `Charge start state`
- Utilisé par : `1560 - POWER ON - Byte`, `Measure group: Track Zapi Right`
- Ligne export : 44627 · id 58540

#### 1560 - POWER ON - Byte  `JPOUT`
- Propriétés : Input value=Power · Length=1 bit · Resolution=1 · Offset=0
- Lit : `Power`
- Utilisé par : `1560 - Cmd`
- Ligne export : 44644 · id 58541

#### Error clear  `DP`
- Propriétés : Mode selector=Charge start state · Default mode: STOP={False} · Mode 1: Clear ERROR={True} · Mode 2: Charging={False}
- Lit : `Charge start state`
- Utilisé par : `1560 - Cycle Value - Byte`
- Ligne export : 44656 · id 58542

#### 1560 - Cycle Value - Byte  `JPOUT`
- Propriétés : Input value=Error clear · Length=1 bit · Resolution=1 · Offset=0
- Lit : `Error clear`
- Utilisé par : `1560 - Cmd`
- Ligne export : 44673 · id 58543

#### 1560 - Cmd  `GFOUT`
- Propriétés : Identifier=1560 · Data length=7 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={{1560 - POWER ON - Byte [bits]; 7}; {1560 - Cycle Value - Byte [bits]; 6}; {1560 - Max Current from 230 V - Byte; 8}; {1560 - Desired Voltage - Byte; 24}; {1560 - Desired Current - Byte; 40}} · Module=Charger Brusa (Generic) · Module index=0
- Lit : `1560 - Cycle Value - Byte`, `1560 - Desired Current - Byte`, `1560 - Desired Voltage - Byte`, `1560 - Max Current from 230 V - Byte`, `1560 - POWER ON - Byte`
- Utilisé par : *(personne)*
- Ligne export : 44685 · id 58544

#### 1552 - Warning Condition - Byte  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `1552 - CAN IN`
- Ligne export : 44716 · id 58545

#### 1552 - Automatique charging - Byte  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `1552 - CAN IN`
- Ligne export : 44727 · id 58546

#### 1553 - Actual mains current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `1553 - Actual mains current - Byte / 100`
- Lit : `1553 - Actual mains current - Byte`
- Utilisé par : `Measure group: Charger Brusa`
- Ligne export : 44738 · id 58547

#### 1553 - Actual mains voltage  `MAC`
- Propriétés : Unit=V AC · Limiting object group=Signed
- Logique :
  - **Controlling** = `1553 - Actual mains voltage - Byte / 10`
- Lit : `1553 - Actual mains voltage - Byte`
- Utilisé par : `Brusa Connected`, `Measure group: Charger Brusa`
- Ligne export : 44782 · id 58555

#### 1555 - Power stage temperature - Byte  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `1555 - Power stage temperature - Byte / 10`
- Lit : `1555 - Power stage temperature - Byte`
- Utilisé par : `1555 - CAN IN`, `Measure group: Charger Brusa`
- Ligne export : 44826 · id 58563

#### 1552 - Hardware enable - IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `1552 - Hardware enable - Byte`
- Lit : `1552 - Hardware enable - Byte`
- Utilisé par : `Brusa ready`, `Measure group: Charger Brusa`
- Ligne export : 44870 · id 58571

#### Brusa Connected  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `1553 - Actual mains voltage [V AC] >= 90`
- Lit : `1553 - Actual mains voltage`
- Utilisé par : `Charger CONNECT to 220V`
- Ligne export : 44913 · id 58667

#### Brusa Charging  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `1553 - output current to the battery [A] > 0,5`
- Lit : `1553 - output current to the battery`
- Utilisé par : `Charger CHARGING`
- Ligne export : 44958 · id 58675

#### Brusa CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `1552 - CAN IN`
- Lit : `1552 - CAN IN`
- Utilisé par : `Charger CAN BUS OK`
- Ligne export : 45003 · id 58683

#### Brusa Error  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `1552 - Error detect - Byte`
- Lit : `1552 - Error detect - Byte`
- Utilisé par : `Charger ERROR`
- Ligne export : 45046 · id 58691

#### Brusa ready  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `1552 - Hardware enable - IDC`
- Lit : `1552 - Hardware enable - IDC`
- Utilisé par : `Charger READY`
- Ligne export : 45089 · id 58720

## ELEC / CHARGER / Elcon — actif seulement si `Is Charger Elcon`

#### ELCON-IN  `GFIN`
- Propriétés : Identifier=0x18FF50E5 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Output Voltage; 0}; {Output Current; 16}; {Hardware Failure; 32}; {Temperature od charger; 33}; {Input Voltage; 34}; {Stating State; 35}; {Communication State; 36}} · Module=Charger Elcon (Generic) · Module index=0
- Lit : `Communication State`, `Hardware Failure`, `Input Voltage`, `Output Current`, `Output Voltage`, `Stating State`, `Temperature od charger`
- Utilisé par : `Elcon Ready`
- Ligne export : 45199 · id 58090

#### Input Voltage  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Adjust group: Charger Setup`, `Measure group: Charger Elcon`, `Single adjust item: Input Voltage`
- Ligne export : 45236 · id 58091

#### Elcon Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `ELCON-IN`
- Lit : `ELCON-IN`
- Utilisé par : `Charger READY`, `Elcon CAN OK`, `Elcon Connected`
- Ligne export : 45248 · id 58092

#### Elcon Connected  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `Elcon Ready`
- Lit : `Elcon Ready`
- Utilisé par : `Charger CONNECT to 220V`
- Ligne export : 45291 · id 58100

#### Hardware Failure  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Elcon Error`, `Measure group: Charger Elcon`
- Ligne export : 45334 · id 58108

#### Output Current  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `ELCON-IN`, `Elcon - output current`
- Ligne export : 45346 · id 58109

#### Elcon - output current  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Output Current / 10`
- Lit : `Output Current`
- Utilisé par : `Charger Output Current`, `Elcon Charging`, `Measure group: Charger Elcon`
- Ligne export : 45359 · id 58110

#### Output Voltage  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `ELCON-IN`, `Elcon - output Voltage`
- Ligne export : 45403 · id 58118

#### Math Voltage  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Desired Voltage [V] * 10`
- Lit : `Desired Voltage`
- Utilisé par : `Max Voltage`
- Ligne export : 45416 · id 58119

#### Max Voltage  `GPOUT`
- Propriétés : Input value=Math Voltage · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `Math Voltage`
- Utilisé par : `ELCON-OUT`
- Ligne export : 45460 · id 58127

#### Math Current  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `HV Current * 10`
- Lit : `HV Current`
- Utilisé par : `Max Curent`
- Ligne export : 45472 · id 58128

#### Max Curent  `GPOUT`
- Propriétés : Input value=Math Current · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `Math Current`
- Utilisé par : `ELCON-OUT`
- Ligne export : 45516 · id 58136

#### CMD  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Charger DIGITAL CMD)`
- Lit : `Charger DIGITAL CMD`
- Utilisé par : `Control`
- Ligne export : 45528 · id 58137

#### Control  `GPOUT`
- Propriétés : Input value=CMD · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `CMD`
- Utilisé par : `ELCON-OUT`
- Ligne export : 45572 · id 58145

#### ELCON-OUT  `GFOUT`
- Propriétés : Identifier=0x1806E5F4 · Data length=8 · Send method=Continuously · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{Max Voltage; 0}; {Max Curent; 16}; {Control; 32}} · Module=Charger Elcon (Generic) · Module index=0
- Lit : `Control`, `Max Curent`, `Max Voltage`
- Utilisé par : *(personne)*
- Ligne export : 45583 · id 58146

#### Temperature od charger  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Temperature od charger`, `Measure group: Charger Elcon`
- Ligne export : 45608 · id 58147

#### Stating State  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Measure group: Charger Elcon`
- Ligne export : 45620 · id 58148

#### Communication State  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Measure group: Charger Elcon`
- Ligne export : 45632 · id 58149

#### Temperature od charger  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Temperature od charger`
- Lit : `Temperature od charger`
- Utilisé par : `ELCON-IN`, `Measure group: Charger Elcon`
- Ligne export : 45644 · id 58150

#### Elcon - output Voltage  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Output Voltage / 10`
- Lit : `Output Voltage`
- Utilisé par : `Measure group: Charger Elcon`
- Ligne export : 45687 · id 58158

#### Elcon Charging  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `Elcon - output current > 0,5`
- Lit : `Elcon - output current`
- Utilisé par : `Charger CHARGING`
- Ligne export : 45731 · id 58224

#### Elcon CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `Elcon Ready`
- Lit : `Elcon Ready`
- Utilisé par : `Charger CAN BUS OK`
- Ligne export : 45776 · id 58244

#### Elcon Error  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `Hardware Failure`
- Lit : `Hardware Failure`
- Utilisé par : `Charger ERROR`
- Ligne export : 45819 · id 58264

## ELEC / CHARGER / Valeo — actif seulement si `Is Charger Valeo`

#### Valeo - Output current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Utilisé par : *(personne)*
- Ligne export : 46867 · id 70319

#### Valeo Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Utilisé par : `Valeo CAN OK`, `Valeo Connected`
- Ligne export : 46902 · id 70327

#### Valeo Connected  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `Valeo Ready`
- Lit : `Valeo Ready`
- Utilisé par : *(personne)*
- Ligne export : 46938 · id 70335

#### Valeo Charging  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Utilisé par : *(personne)*
- Ligne export : 46981 · id 70343

#### Valeo CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `Valeo Ready`
- Lit : `Valeo Ready`
- Utilisé par : *(personne)*
- Ligne export : 47017 · id 70351

#### Valeo Error  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Utilisé par : *(personne)*
- Ligne export : 47060 · id 70359

## ELEC / MOTORS

#### Engine - Force ON  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Engines Ready`, `M3 - RUN - with F`, `Single adjust item: Engine - Force`
- Ligne export : 59455 · id 74467

#### Engine STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *STARTING* :
  - **Activating** = `VARIATOR ON`
  - **Blocking** = `(M1 - Ready) AND (M2 - Ready) AND (M3 - Ready)`
- Fonction *READY* :
  - **Activating** = `(M1 - Ready) AND (M2 - Ready) AND (M3 - Ready) AND (VARIATOR ON)`
- Fonction *ERROR* :
  - **Activating** = `(M1 - Error mode) OR (M2 - Error mode) OR (M3 - Error mode)`
- Lit : `M1 - Error mode`, `M1 - Ready`, `M2 - Error mode`, `M2 - Ready`, `M3 - Error mode`, `M3 - Ready`, `VARIATOR ON`
- Utilisé par : `Engine State`, `Engines Ready`
- Ligne export : 59468 · id 74468

#### Engines Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Engine STATE = 2) OR (Engine - Force ON)`
- Lit : `Engine - Force ON`, `Engine STATE`
- Utilisé par : `Engines Not Ready`, `Engines Ready`, `Engines Ready output`, `State All Speed`, `State Speed Table`
- Ligne export : 59626 · id 74492

#### Engines Not Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Engines Ready)`
- Lit : `Engines Ready`
- Utilisé par : `Engine Stop Fonction Output`, `Engines Not Ready`
- Ligne export : 59678 · id 74501

## ELEC / MOTORS / Cooling

#### NEED FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(M1 - NEED TO FAN) OR (M2 - NEED TO FAN) OR (M3 - NEED TO FAN)`
- Lit : `M1 - NEED TO FAN`, `M2 - NEED TO FAN`, `M3 - NEED TO FAN`
- Utilisé par : `Timer Fan`
- Ligne export : 59032 · id 72375

#### Timer Fan  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `NEED FAN`
  - **Resetting** = `(not(NEED FAN)) OR (Timer Fan [min] > 10)`
- Lit : `NEED FAN`
- Utilisé par : `FAN OUT`
- Ligne export : 59089 · id 72385

#### FAN MODE  `SP`
- Propriétés : Input channel=None · Default state name=AUTO · States={OFF; FORCE ON}
- Utilisé par : `FAN OUT`, `Adjust group: Master Cooling`, `Single adjust item: FAN MODE`
- Ligne export : 59158 · id 72397

#### FAN OUT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=FAN MODE
- Fonction *AUTO* :
  - **Activating** = `Inside(Timer Fan [min], 0,5, 4)`
- Fonction *OFF* :
  - **Blocking** = `True`
- Fonction *FORCE ON* :
  - **Activating** = `True`
- Lit : `FAN MODE`, `Timer Fan`
- Utilisé par : `FAN OUT output`, `Statistics log: Stat Log`
- Ligne export : 59171 · id 72400

#### NEED PUMP  `IDC`
- Propriétés : Toggle=No · Delay on=20000 · Delay off=0
- Logique :
  - **Activating** = `(M3 - NEED TO PUMP) OR (M2 - NEED TO PUMP) OR (M1 - NEED TO PUMP)`
- Lit : `M1 - NEED TO PUMP`, `M2 - NEED TO PUMP`, `M3 - NEED TO PUMP`
- Utilisé par : `PUMP VAR`
- Ligne export : 59279 · id 72422

#### PUMP VAR MODE  `SP`
- Propriétés : Input channel=None · Default state name=AUTO · States={OFF; FORCE ON}
- Utilisé par : `PUMP VAR`, `Adjust group: Master Cooling`, `Single adjust item: PUMP VAR MODE`
- Ligne export : 59336 · id 72432

#### PUMP VAR  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=PUMP VAR MODE
- Fonction *AUTO* :
  - **Activating** = `NEED PUMP`
- Fonction *OFF* :
  - **Blocking** = `True`
- Fonction *FORCE ON* :
  - **Activating** = `True`
- Lit : `NEED PUMP`, `PUMP VAR MODE`
- Utilisé par : `PUMP VAR output`, `Statistics log: Stat Log`
- Ligne export : 59349 · id 72435

## ELEC / MOTORS / M-Hydrau — actif seulement si `VARIATOR SUPER ON`

#### Oil Not Good  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Wait Very Low Oil Level`
- Lit : `Wait Very Low Oil Level`
- Utilisé par : `Oil not Good`
- Ligne export : 57142 · id 72078

#### Speed  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Engine hydro Speed [rpm]`
- Lit : `Engine hydro Speed`
- Utilisé par : `Adjust group: Master Track`
- Ligne export : 57185 · id 72082

#### M-Pump - Brand  `SP`
- Propriétés : Input channel=None · Default state name=Sevcon · States={}
- Utilisé par : `Engine Temps`, `Heatsink`, `Is M3 Sevcon`, `M3 - CAN OK`, `M3 - Error mode`, `M3 - Ready`, `M3 - Run`, `M3 - Voltage`, `Adjust group: Config Electric Drive`, `Single adjust item: M-Pump - Brand`
- Ligne export : 57227 · id 72124

#### Is M3 Sevcon  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M-Pump - Brand = 0`
- Lit : `M-Pump - Brand`
- Utilisé par : `Active le groupe: ELEC / MOTORS / M-Hydrau / Sevcon`
- Ligne export : 57238 · id 72125

#### Heatsink  `MAC`
- Propriétés : Unit=*C · Limiting object group=Signed · Function selector=M-Pump - Brand
- Fonction *Sevcon* :
  - **Controlling** = `Sevcon - Heatsink [Â°C]`
- Lit : `M-Pump - Brand`, `Sevcon - Heatsink`
- Utilisé par : `M3 - NEED TO FAN`, `M3 - NEED TO PUMP`, `Measure group: Motor Hydrau`
- Ligne export : 58479 · id 72131

#### M-Hydrau Controller Fan Temp  `IP`
- Propriétés : Unit=Â°C · Default mode={30}
- Utilisé par : `M3 - NEED TO FAN`
- Ligne export : 58521 · id 91787

#### M3 - NEED TO FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Heatsink [*C] <= M-Hydrau Controller Fan Temp [Â°C]`
- Lit : `Heatsink`, `M-Hydrau Controller Fan Temp`
- Utilisé par : `NEED FAN`
- Ligne export : 58533 · id 72102

#### M-Hydrau Controller Pump Temp  `IP`
- Propriétés : Unit=Â°C · Default mode={40}
- Utilisé par : `M3 - NEED TO PUMP`
- Ligne export : 58578 · id 91788

#### M3 - NEED TO PUMP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Heatsink [*C] <= M-Hydrau Controller Pump Temp [Â°C]`
- Lit : `Heatsink`, `M-Hydrau Controller Pump Temp`
- Utilisé par : `NEED PUMP`
- Ligne export : 58590 · id 72110

#### Engine Temps  `MAC`
- Propriétés : Unit=*C · Limiting object group=Signed · Function selector=M-Pump - Brand
- Fonction *Sevcon* :
  - **Controlling** = `Sevcon - Engine Temp [Â°C]`
- Lit : `M-Pump - Brand`, `Sevcon - Engine Temp`
- Utilisé par : `M3 - Charge`, `M3 - ENGINE HOT`, `Measure group: Motor Hydrau`
- Ligne export : 58635 · id 72190

#### M3 - ENGINE HOT  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Engine Temps [*C] >= Engine Eco Temp [Â°C]`
- Lit : `Engine Eco Temp`, `Engine Temps`
- Utilisé par : `Event log: Electronic Logs`
- Ligne export : 58677 · id 72152

#### M3 - Voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed · Function selector=M-Pump - Brand
- Fonction *Sevcon* :
  - **Controlling** = `Sevcon - Voltage_3 [V]`
- Lit : `M-Pump - Brand`, `Sevcon - Voltage_3`
- Utilisé par : `Measure group: Motor Hydrau`
- Ligne export : 58722 · id 72201

#### M3 - Run  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Pump - Brand
- Fonction *Sevcon* :
  - **Activating** = `Sevcon - M3 - RUN`
- Lit : `M-Pump - Brand`, `Sevcon - M3 - RUN`
- Utilisé par : `M3 - RUN - with F`, `Measure group: Motor Hydrau`, `Statistics log: Stat Log`
- Ligne export : 58764 · id 72225

#### M3 - Charge  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `((MaxOf((Engine Temps [*C] - 40), 0)) / (Engine Max Temp [Â°C] - 40)) * 100`
- Lit : `C`, `Engine Max Temp`, `Engine Temps`
- Utilisé par : `Measure group: Motor Hydrau`
- Ligne export : 58807 · id 72242

#### M3 - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Pump - Brand
- Fonction *Sevcon* :
  - **Activating** = `Sencon - CAN OK`
- Lit : `M-Pump - Brand`, `Sencon - CAN OK`
- Utilisé par : `MD4-10 page: INFO`, `Measure group: Motor Hydrau`
- Ligne export : 58887 · id 72268

#### M3 - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Pump - Brand
- Fonction *Sevcon* :
  - **Activating** = `Sevcon - Ready`
- Lit : `M-Pump - Brand`, `Sevcon - Ready`
- Utilisé par : `Engine STATE`, `Measure group: Motor Hydrau`
- Ligne export : 58930 · id 72279

#### M3 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Pump - Brand
- Fonction *Sevcon* :
  - **Activating** = `Sevcon - Error mode`
- Lit : `M-Pump - Brand`, `Sevcon - Error mode`
- Utilisé par : `Engine STATE`, `Event log: Electronic Logs`, `Measure group: Motor Hydrau`
- Ligne export : 58973 · id 72530

## ELEC / MOTORS / M-Hydrau / Sevcon — actif seulement si `Is M3 Sevcon`

#### Speed  `FGI`
- Propriétés : Input type=Real · Input=Speed · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Speed`
- Utilisé par : `Speed`, `Speed Slope`, `Adjust group: Master Track`
- Ligne export : 57307 · id 71800

#### Oil not Good  `FGI`
- Propriétés : Input type=Digital · Input=Oil Not Good · Default state name=Default state
- Lit : `Oil Not Good`
- Utilisé par : `ON/OFF Var`
- Ligne export : 57321 · id 71801

#### Test Mode  `SMC`
- Propriétés : Default state name=Normal
- Fonction *Test* :
  - **Activating** = `HVLP Pump Test`
- Lit : `HVLP Pump Test`
- Utilisé par : `Speed`
- Ligne export : 57332 · id 71802

#### HVLP Speed Test  `IP`
- Propriétés : Default mode={-100}
- Utilisé par : `Speed`
- Ligne export : 57372 · id 71810

#### Speed  `IMAC`
- Propriétés : Function selector=Test Mode
- Fonction *Normal* :
  - **Controlling** = `Speed`
- Fonction *Test* :
  - **Controlling** = `HVLP Speed Test`
- Lit : `HVLP Speed Test`, `Speed`, `Test Mode`
- Utilisé par : `Speed`, `Speed Slope`, `Adjust group: Master Track`
- Ligne export : 57384 · id 71811

#### Speed Slope  `SFC`
- Propriétés : Input channel=Speed · Enable=Yes · Type=Slopes · Slopes={{Hydraulic speed slope [/s]; Hydraulic speed slope [/s]}; {Hydraulic speed slope [/s]; Hydraulic speed slope [/s]}}
- Lit : `Hydraulic speed slope`, `Speed`
- Utilisé par : `ON/OFF Var`, `Rw Speed Limit`
- Ligne export : 57456 · id 71826

#### ON/OFF Var  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `(Speed Slope <> 0) AND (VARIATOR SUPER ON)`
  - **Blocking** = `Oil not Good`
- Lit : `Oil not Good`, `Speed Slope`, `VARIATOR SUPER ON`
- Utilisé par : `Variator State`
- Ligne export : 57474 · id 71827

#### 0x191AFF71  `GFIN`
- Propriétés : Identifier=0x191AFF71 · Data length=DonÂt care · Timeout=500 · Paged protocol={Not used} · Parameters={{Input Voltage; 32}; {Heatsink [Byte]; 0}; {Sevcon - Engine Temp [Â°C]; 16}} · Module=Motor Sevcon hydrolic - 3 (Generic) · Module index=4
- Lit : `C`, `Heatsink`, `Input Voltage`, `Sevcon - Engine Temp`
- Utilisé par : *(personne)*
- Ligne export : 57533 · id 71922

#### Sevcon - Engine Temp  `GPIN`
- Propriétés : Unit=Â°C · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x191AFF71`, `Engine Temps`
- Ligne export : 57558 · id 71838

#### 0x1918FF71  `GFIN`
- Propriétés : Identifier=0x1918FF71 · Data length=DonÂt care · Timeout=500 · Paged protocol={Not used} · Parameters={{Motor Speed [rpm]; 16}; {Torque Mesured; 0}} · Module=Motor Sevcon hydrolic - 3 (Generic) · Module index=2
- Lit : `Motor Speed`, `Torque Mesured`
- Utilisé par : *(personne)*
- Ligne export : 57571 · id 71854

#### Sencon - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `0x1918FF71`
- Utilisé par : `M3 - CAN OK`
- Ligne export : 57593 · id 71855

#### Motor Speed  `GPIN`
- Propriétés : Unit=rpm · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x1918FF71`, `Sevcon - M3 - RUN`, `Measure group: HVLP`
- Ligne export : 57636 · id 71863

#### Min Speed for tensionning  `IP`
> Minimum speed to open Tension valve
- Propriétés : Unit=RPM · Default mode={1800}
- Utilisé par : `Sevcon - M3 - RUN`, `Adjust group: Master Track`, `Single adjust item: Min Speed for tensionning`
- Ligne export : 57649 · id 91719

#### Sevcon - M3 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `(Abs(Motor Speed [rpm])) > Min Speed for tensionning [RPM]`
- Lit : `Min Speed for tensionning`, `Motor Speed`
- Utilisé par : `M3 - Run`
- Ligne export : 57661 · id 71864

#### 0x1919FF71  `GFIN`
- Propriétés : Identifier=0x1919FF71 · Data length=DonÂt care · Timeout=500 · Paged protocol={Not used} · Parameters={{Status Word; 32}; {Limit Word; 40}} · Module=Motor Sevcon hydrolic - 3 (Generic) · Module index=3
- Lit : `Limit Word`, `Status Word`
- Utilisé par : *(personne)*
- Ligne export : 57714 · id 71881

#### Status Word  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `0x191071FA`, `0x1919FF71`, `Sevcon - Ready`, `Status Word`
- Ligne export : 57736 · id 71882

#### Sevcon - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Status Word = 7) OR (Status Word = 8)`
- Lit : `Status Word`
- Utilisé par : `M3 - Ready`
- Ligne export : 57748 · id 71883

#### Variator State  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ON* :
  - **Activating** = `ON/OFF Var`
- Lit : `ON/OFF Var`
- Utilisé par : `Status Word`
- Ligne export : 57802 · id 71900

#### Status Word  `IP`
- Propriétés : Mode selector=Variator State · Default mode: OFF={3} · Mode 1: ON={5}
- Lit : `Variator State`
- Utilisé par : `0x191071FA`, `0x1919FF71`, `Sevcon - Ready`, `Status Word`
- Ligne export : 57842 · id 71909

#### Status Word  `GPOUT`
- Propriétés : Input value=Status Word · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Status Word`
- Utilisé par : `0x191071FA`, `0x1919FF71`, `Sevcon - Ready`
- Ligne export : 57856 · id 71910

#### Torque Demande  `GPOUT`
- Propriétés : Input value=-496 · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Utilisé par : `0x191071FA`
- Ligne export : 57868 · id 71911

#### Torque Limit  `GPOUT`
- Propriétés : Input value=496 · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Utilisé par : `0x191071FA`
- Ligne export : 57880 · id 71912

#### 0x191071FA  `GFOUT`
- Propriétés : Identifier=0x191071FA · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Parameters={{Status Word; 16}; {Torque Demande; 0}; {Torque Limit; 32}} · Module=Motor Sevcon hydrolic - 3 (Generic) · Module index=0
- Lit : `Status Word`, `Torque Demande`, `Torque Limit`
- Utilisé par : *(personne)*
- Ligne export : 57892 · id 71913

#### Fw Speed Limit  `GPOUT`
- Propriétés : Input value=2500 · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Utilisé par : `0x191171FA`
- Ligne export : 57917 · id 71914

#### Rw Speed Limit  `GPOUT`
- Propriétés : Input value=Speed Slope · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Lit : `Speed Slope`
- Utilisé par : `0x191171FA`, `Measure group: HVLP`
- Ligne export : 57929 · id 71915

#### 0x191171FA  `GFOUT`
- Propriétés : Identifier=0x191171FA · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Parameters={{Fw Speed Limit; 16}; {Rw Speed Limit; 32}} · Module=Motor Sevcon hydrolic - 3 (Generic) · Module index=1
- Lit : `Fw Speed Limit`, `Rw Speed Limit`
- Utilisé par : *(personne)*
- Ligne export : 57941 · id 71916

#### I Batt Discharge Limit  `GPOUT`
- Propriétés : Input value=50 · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Utilisé par : `0x191271FA`
- Ligne export : 57963 · id 71917

#### I Batt recharge limit  `GPOUT`
- Propriétés : Input value=-50 · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Utilisé par : `0x191271FA`
- Ligne export : 57975 · id 71918

#### 0x191271FA  `GFOUT`
- Propriétés : Identifier=0x191271FA · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Parameters={{I Batt Discharge Limit; 0}; {I Batt recharge limit; 16}} · Module=Motor Sevcon hydrolic - 3 (Generic) · Module index=2
- Lit : `I Batt Discharge Limit`, `I Batt recharge limit`
- Utilisé par : *(personne)*
- Ligne export : 57987 · id 71919

#### Limit Word  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `0x1919FF71`
- Ligne export : 58009 · id 71920

#### Torque Mesured  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x1918FF71`, `Torque actual - 2`
- Ligne export : 58021 · id 71921

#### Input Voltage  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x191AFF71`, `Sevcon - Voltage_3`, `Adjust group: Charger Setup`, `Measure group: Charger Elcon`, `Single adjust item: Input Voltage`
- Ligne export : 58034 · id 71923

#### 0x191BFF71  `GFIN`
- Propriétés : Identifier=0x191BFF71 · Data length=DonÂt care · Timeout=3000 · Paged protocol={Not used} · Parameters={{M3 (Pump) - Error; 0}} · Module=Motor Sevcon hydrolic - 3 (Generic) · Module index=0
- Lit : `M3 (Pump) - Error`
- Utilisé par : *(personne)*
- Ligne export : 58047 · id 71924

#### M3 (Pump) - Error  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x191BFF71`, `Error 3 - MEM`, `M3  (Pump) - Filter`, `M3 - New Error Code`, `Sevcon - Error mode`, `Event log: Electronic Logs`
- Ligne export : 58066 · id 71925

#### Sevcon - Voltage_3  `IMAC`
- Propriétés : Unit=V
- Logique :
  - **Controlling** = `Input Voltage * 0,0625`
- Lit : `Input Voltage`
- Utilisé par : `M3 - Voltage`
- Ligne export : 58079 · id 71926

#### Torque actual - 2  `IMAC`
- Propriétés : Unit=Nm
- Logique :
  - **Controlling** = `Torque Mesured * 0,0625`
- Lit : `Torque Mesured`
- Utilisé par : `Measure group: HVLP`
- Ligne export : 58122 · id 71934

#### Heatsink  `GPIN`
- Propriétés : Unit=Byte · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x191AFF71`, `Sevcon - Heatsink`, `Measure group: Motor Hydrau`
- Ligne export : 58165 · id 71942

#### Sevcon - Heatsink  `IMAC`
- Propriétés : Unit=Â°C
- Logique :
  - **Controlling** = `Heatsink [Byte]`
- Lit : `Heatsink`
- Utilisé par : `Heatsink`
- Ligne export : 58178 · id 71955

#### M3  (Pump) - Filter  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(M3 (Pump) - Error = 0) OR (M3 (Pump) - Error = 17862)`
- Lit : `M3 (Pump) - Error`
- Utilisé par : `M3 - New Error Code`, `Sevcon - Error mode`
- Ligne export : 58219 · id 72606

#### M3 - New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M3 (Pump) - Error <> Error 3 - MEM`
  - **Blocking** = `M3  (Pump) - Filter`
- Lit : `Error 3 - MEM`, `M3  (Pump) - Filter`, `M3 (Pump) - Error`
- Utilisé par : `Error 3 - MEM`, `M3 - Pump Engine CMSG`
- Ligne export : 58273 · id 71989

#### Error 3 - MEM  `MEM`
- Propriétés : Input channel=M3 (Pump) - Error · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M3 - New Error Code)`
- Lit : `M3 (Pump) - Error`, `M3 - New Error Code`
- Utilisé par : `Error 3`, `M3 - New Error Code`, `M3 - Pump Engine CMSG`
- Ligne export : 58325 · id 71979

#### M3 - Pump Engine CMSG  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Hydraulics · Text=Hydraulic pump Motor Error. Stop battery, wait one minute and restart. If the problem persists, contact a service center. · Channel=Error 3 - MEM
- Logique :
  - **Showing** = `M3 - New Error Code`
- Lit : `Error 3 - MEM`, `M3 - New Error Code`
- Utilisé par : *(personne)*
- Ligne export : 58370 · id 71999

#### Sevcon - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M3 (Pump) - Error`
  - **Blocking** = `M3  (Pump) - Filter`
- Lit : `M3  (Pump) - Filter`, `M3 (Pump) - Error`
- Utilisé par : `M3 - Error mode`
- Ligne export : 58416 · id 72513

#### Hydraulic speed slope  `IP`
- Propriétés : Unit=/s · Default mode={1000}
- Utilisé par : `Ref Speed Slope`, `Speed Slope`, `Adjust group: Master Track`, `Single adjust item: Hydraulic speed slope`
- Ligne export : 58466 · id 91728

## ELEC / MOTORS / M-Tracks — actif seulement si `VARIATOR SUPER ON`

#### M-Track - Brand  `SP`
- Propriétés : Input channel=None · Default state name=Sevcon · States={Zapi}
- Utilisé par : `Is_MT_Sevcon`, `Is_MT_Zapi`, `M1 - CAN OK`, `M1 - CURRENT`, `M1 - Error mode`, `M1 - Heatsink`, `M1 - KTY`, `M1 - RUN`, `M1 - Ready`, `M1 - Speed`, `M1 - Torque`, `M1 - Voltage`, `M2 - CAN OK`, `M2 - CURRENT`, `M2 - Error mode`, `M2 - Heatsink`, `M2 - KTY`, `M2 - RUN`, `M2 - Ready`, `M2 - Speed`, `M2 - Torque`, `M2 - Voltage`, `Adjust group: Config Electric Drive`, `Single adjust item: M-Track - Brand`
- Ligne export : 47318 · id 73286

#### Is_MT_Sevcon  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M-Track - Brand = 0`
- Lit : `M-Track - Brand`
- Utilisé par : `Active le groupe: ELEC / MOTORS / M-Tracks / Sevcon`
- Ligne export : 47330 · id 73287

#### Math Right  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `Right Filter [%]`
- Lit : `Right Filter`
- Utilisé par : `Speed CAN Right`, `Speed_CAN_Right`
- Ligne export : 47375 · id 73383

#### Math Left  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `Left Filter [%]`
- Lit : `Left Filter`
- Utilisé par : `Speed CAN Left`, `Speed_CAN_Left`
- Ligne export : 47417 · id 73392

#### Is_MT_Zapi  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M-Track - Brand = 1`
- Lit : `M-Track - Brand`
- Utilisé par : `Active le groupe: ELEC / MOTORS / M-Tracks / Zapi Left`, `Active le groupe: ELEC / MOTORS / M-Tracks / Zapi Right`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 49659 · id 73307

#### Enable Power Zapi  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Enable`, `Enable`, `Forward`, `Forward`, `Adjust group: Master Features`, `Single adjust item: Enable Power Zapi`
- Ligne export : 49704 · id 87238

#### Engine Max Temp  `IP`
- Propriétés : Unit=Â°C · Default mode={110}
- Utilisé par : `M1 - Charge`, `M2 - Charge`, `M3 - Charge`, `Adjust group: Master Cooling`, `Single adjust item: Engine Max Temp`
- Ligne export : 54226 · id 74079

#### M-Tracks Controller Fan Temp  `IP`
- Propriétés : Unit=Â°C · Default mode={60}
- Utilisé par : `M1 - NEED TO FAN`, `M2 - NEED TO FAN`, `Adjust group: Master Cooling`, `Single adjust item: M-Tracks Controller Fan Temp`
- Ligne export : 54238 · id 74080

#### M1 - Heatsink  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M1 - Heatsink [Â°C]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M1_Heatsink [Â°C]`
- Lit : `M-Track - Brand`, `SEV - M1 - Heatsink`, `ZAPI_M1_Heatsink`
- Utilisé par : `M1 - NEED TO FAN`, `M1 - NEED TO PUMP`, `Measure group: Motor Right`
- Ligne export : 54250 · id 74324

#### M1 - NEED TO FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M1 - Heatsink [Â°C] >= M-Tracks Controller Fan Temp [Â°C]`
- Lit : `M-Tracks Controller Fan Temp`, `M1 - Heatsink`
- Utilisé par : `NEED FAN`
- Ligne export : 54323 · id 74081

#### Engine Eco Temp  `IP`
- Propriétés : Unit=Â°C · Default mode={90}
- Utilisé par : `M1 - ENGINE HOT`, `M2 - ENGINE HOT`, `M3 - ENGINE HOT`, `Adjust group: Master Cooling`, `Single adjust item: Engine Eco Temp`
- Ligne export : 54368 · id 74089

#### M-Tracks Controller Pump Temp  `IP`
- Propriétés : Unit=Â°C · Default mode={50}
- Utilisé par : `M1 - NEED TO PUMP`, `M2 - NEED TO PUMP`, `Adjust group: Master Cooling`, `Single adjust item: M-Tracks Controller Pump Temp`
- Ligne export : 54380 · id 74098

#### M1 - NEED TO PUMP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M1 - Heatsink [Â°C] >= M-Tracks Controller Pump Temp [Â°C]`
- Lit : `M-Tracks Controller Pump Temp`, `M1 - Heatsink`
- Utilisé par : `NEED PUMP`
- Ligne export : 54392 · id 74099

#### M1 - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M1 - CURRENT [A]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M1_Actual_current [A]`
- Lit : `M-Track - Brand`, `SEV - M1 - CURRENT`, `ZAPI_M1_Actual_current`
- Utilisé par : `Instant current Filter`, `Measure group: Motor Right`
- Ligne export : 54437 · id 74187

#### M1 - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M1 - CAN OK`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M1_CAN OK`
- Lit : `M-Track - Brand`, `SEV - M1 - CAN OK`, `ZAPI_M1_CAN OK`
- Utilisé par : `MD4-10 page: INFO`, `Measure group: Motor Right`
- Ligne export : 54510 · id 74195

#### M1 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M1 - RUN`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M1_RUN`
- Lit : `M-Track - Brand`, `SEV - M1 - RUN`, `ZAPI_M1_RUN`
- Utilisé par : `Measure group: Motor Right`, `Statistics log: Stat Log`
- Ligne export : 54584 · id 74203

#### M1 - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M1 - Ready`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M1_READY`
- Lit : `M-Track - Brand`, `SEV - M1 - Ready`, `ZAPI_M1_READY`
- Utilisé par : `Engine STATE`, `Measure group: Motor Right`
- Ligne export : 54658 · id 74211

#### M1 - Voltage  `IMAC`
- Propriétés : Unit=V · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M1 - Voltage [V]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M1_Batterie Voltage [V]`
- Lit : `M-Track - Brand`, `SEV - M1 - Voltage`, `ZAPI_M1_Batterie Voltage`
- Utilisé par : `Measure group: Motor Right`
- Ligne export : 54732 · id 74219

#### M1 - Torque  `IMAC`
- Propriétés : Unit=Nm · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M1 - Torque actual [Nm]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M1_Torque [Nm]`
- Lit : `M-Track - Brand`, `SEV - M1 - Torque actual`, `ZAPI_M1_Torque`
- Utilisé par : `MD4-10 page: INFO`, `Measure group: Motor Right`
- Ligne export : 54804 · id 74227

#### M1 - Speed  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M1 - Speed [rpm]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M1_Actual_speed [rpm]`
- Lit : `M-Track - Brand`, `SEV - M1 - Speed`, `ZAPI_M1_Actual_speed`
- Utilisé par : `M1 - Mechanical power`, `MD4-10 page: INFO`, `Measure group: Motor Right`
- Ligne export : 54876 · id 74235

#### M1 - KTY  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M1 - KTY [Â°C]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M1_Motor_Temp [Â°C]`
- Lit : `M-Track - Brand`, `SEV - M1 - KTY`, `ZAPI_M1_Motor_Temp`
- Utilisé par : `M1 - Charge`, `M1 - ENGINE HOT`, `Measure group: Motor Right`
- Ligne export : 54949 · id 74358

#### M1 - Charge  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `((MaxOf((M1 - KTY [Â°C] - 40), 0)) / (Engine Max Temp [Â°C] - 40)) * 100`
- Lit : `C`, `Engine Max Temp`, `M1 - KTY`
- Utilisé par : `MD4-10 page: INFO`
- Ligne export : 55022 · id 74390

#### M1 - ENGINE HOT  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `M1 - KTY [Â°C] >= Engine Eco Temp [Â°C]`
- Lit : `Engine Eco Temp`, `M1 - KTY`
- Utilisé par : `Event log: Electronic Logs`
- Ligne export : 55102 · id 74413

#### M2 - Heatsink  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M2 - Heatsink [Â°C]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Heatsink [Â°C]`
- Lit : `M-Track - Brand`, `SEV - M2 - Heatsink`, `ZAPI_M2_Heatsink`
- Utilisé par : `M2 - NEED TO FAN`, `M2 - NEED TO PUMP`, `Measure group: Motor Left`
- Ligne export : 55147 · id 74681

#### M2 - NEED TO FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M2 - Heatsink [Â°C] >= M-Tracks Controller Fan Temp [Â°C]`
- Lit : `M-Tracks Controller Fan Temp`, `M2 - Heatsink`
- Utilisé par : `NEED FAN`
- Ligne export : 55220 · id 74695

#### M2 - NEED TO PUMP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M2 - Heatsink [Â°C] >= M-Tracks Controller Pump Temp [Â°C]`
- Lit : `M-Tracks Controller Pump Temp`, `M2 - Heatsink`
- Utilisé par : `NEED PUMP`
- Ligne export : 55265 · id 74703

#### M2 - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M2 - CURRENT [A]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Actual_current [A]`
- Lit : `M-Track - Brand`, `SEV - M2 - CURRENT`, `ZAPI_M2_Actual_current`
- Utilisé par : `Instant current Filter`, `Measure group: Motor Left`
- Ligne export : 55310 · id 74711

#### M2 - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M2 - CAN OK`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M2_CAN OK`
- Lit : `M-Track - Brand`, `SEV - M2 - CAN OK`, `ZAPI_M2_CAN OK`
- Utilisé par : `MD4-10 page: INFO`, `Measure group: Motor Left`
- Ligne export : 55383 · id 74725

#### M2 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M2 - RUN`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M2_RUN`
- Lit : `M-Track - Brand`, `SEV - M2 - RUN`, `ZAPI_M2_RUN`
- Utilisé par : `Measure group: Motor Left`, `Statistics log: Stat Log`
- Ligne export : 55457 · id 74739

#### M2 - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M2 - Ready`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M2_READY`
- Lit : `M-Track - Brand`, `SEV - M2 - Ready`, `ZAPI_M2_READY`
- Utilisé par : `Engine STATE`, `Measure group: Motor Left`
- Ligne export : 55531 · id 74753

#### M2 - Voltage  `IMAC`
- Propriétés : Unit=V · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M2 - Voltage [V]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Batterie Voltage [V]`
- Lit : `M-Track - Brand`, `SEV - M2 - Voltage`, `ZAPI_M2_Batterie Voltage`
- Utilisé par : `Measure group: Motor Left`
- Ligne export : 55605 · id 74767

#### M2 - Torque  `IMAC`
- Propriétés : Unit=Nm · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M2 - Torque actual [Nm]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Torque [Nm]`
- Lit : `M-Track - Brand`, `SEV - M2 - Torque actual`, `ZAPI_M2_Torque`
- Utilisé par : `MD4-10 page: INFO`, `Measure group: Motor Left`
- Ligne export : 55677 · id 74781

#### M2 - Speed  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M2 - Speed [rpm]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Actual_speed [rpm]`
- Lit : `M-Track - Brand`, `SEV - M2 - Speed`, `ZAPI_M2_Actual_speed`
- Utilisé par : `M2 - Mechanical power`, `MD4-10 page: INFO`, `Measure group: Motor Left`
- Ligne export : 55749 · id 74795

#### M2 - KTY  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M2 - KTY [Â°C]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Motor_Temp [Â°C]`
- Lit : `M-Track - Brand`, `SEV - M2 - KTY`, `ZAPI_M2_Motor_Temp`
- Utilisé par : `M2 - Charge`, `M2 - ENGINE HOT`, `Measure group: Motor Left`
- Ligne export : 55822 · id 74809

#### M2 - Charge  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `((MaxOf((M2 - KTY [Â°C] - 40), 0)) / (Engine Max Temp [Â°C] - 40)) * 100`
- Lit : `C`, `Engine Max Temp`, `M2 - KTY`
- Utilisé par : `MD4-10 page: INFO`
- Ligne export : 55895 · id 74823

#### M2 - ENGINE HOT  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `M2 - KTY [Â°C] >= Engine Eco Temp [Â°C]`
- Lit : `Engine Eco Temp`, `M2 - KTY`
- Utilisé par : `Event log: Electronic Logs`
- Ligne export : 55975 · id 74835

#### M1 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M1 - Error mode`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M1_Error mode`
- Lit : `M-Track - Brand`, `SEV - M1 - Error mode`, `ZAPI_M1_Error mode`
- Utilisé par : `Engine STATE`, `Measure group: Motor Right`
- Ligne export : 56020 · id 74925

#### M2 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M2 - Error mode`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M2_Error mode`
- Lit : `M-Track - Brand`, `SEV - M2 - Error mode`, `ZAPI_M2_Error mode`
- Utilisé par : `Engine STATE`, `Measure group: Motor Left`
- Ligne export : 56094 · id 74954

#### Instant current Filter  `SFC`
- Propriétés : Input channel=M1 - CURRENT [A] · Enable=Yes · Type=BWL · BWL=20
- Lit : `M1 - CURRENT`
- Utilisé par : `Couple Moteur`, `Couple Moteur`, `M1 - 100A-125A`, `M1 - 25A-50A`, `M1 - 50A-75A`, `M1 - 75A-100A`, `M1 - up to 125A`, `M2 - 100A-125A`, `M2 - 25A-50A`, `M2 - 50A-75A`, `M2 - 75A-100A`, `M2 - up to 125A`
- Ligne export : 56168 · id 75160

#### Couple Moteur  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `26 * courbe(((0,8 * Instant current Filter [A]) / 33): {{0; 0}; {1; 1}; {2; 1,8}; {2,5; 2,18}; {3; 2,45}; {3,5; 2,62}; {4; 2,75}}, Freeze)`
- Lit : `C`, `Instant current Filter`
- Utilisé par : `M1 - Mechanical power`, `M1 - Torque Tracks`, `M2 - Mechanical power`, `M2 - Torque tracks`
- Ligne export : 56180 · id 75161

#### M1 - Mechanical power  `MAC`
- Propriétés : Unit=kW · Limiting object group=Signed
- Logique :
  - **Controlling** = `((M1 - Speed [rpm] * 0,104719) * Couple Moteur [Nm]) / 1000`
- Lit : `Couple Moteur`, `M1 - Speed`
- Utilisé par : *(personne)*
- Ligne export : 56272 · id 75172

#### M1 - Torque Tracks  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Couple Moteur [Nm] * 37,2`
- Lit : `Couple Moteur`
- Utilisé par : *(personne)*
- Ligne export : 56334 · id 75182

#### M1 - 25A-50A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(25 < Instant current Filter [A]) AND (Instant current Filter [A] <= 50)`
- Lit : `Instant current Filter`
- Utilisé par : `Statistics log: Engine Use`
- Ligne export : 56378 · id 75190

#### M1 - 50A-75A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(50 < Instant current Filter [A]) AND (Instant current Filter [A] <= 75)`
- Lit : `Instant current Filter`
- Utilisé par : `Statistics log: Engine Use`
- Ligne export : 56432 · id 75199

#### M1 - 75A-100A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(75 < Instant current Filter [A]) AND (Instant current Filter [A] <= 100)`
- Lit : `Instant current Filter`
- Utilisé par : `Statistics log: Engine Use`
- Ligne export : 56486 · id 75208

#### M1 - 100A-125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(100 < Instant current Filter [A]) AND (Instant current Filter [A] <= 125)`
- Lit : `Instant current Filter`
- Utilisé par : `Statistics log: Engine Use`
- Ligne export : 56540 · id 75217

#### M1 - up to 125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `125 < Instant current Filter [A]`
- Lit : `Instant current Filter`
- Utilisé par : `Statistics log: Engine Use`
- Ligne export : 56594 · id 75226

#### Instant current Filter  `SFC`
- Propriétés : Input channel=M2 - CURRENT [A] · Enable=Yes · Type=BWL · BWL=20
- Lit : `M2 - CURRENT`
- Utilisé par : `Couple Moteur`, `Couple Moteur`, `M1 - 100A-125A`, `M1 - 25A-50A`, `M1 - 50A-75A`, `M1 - 75A-100A`, `M1 - up to 125A`, `M2 - 100A-125A`, `M2 - 25A-50A`, `M2 - 50A-75A`, `M2 - 75A-100A`, `M2 - up to 125A`
- Ligne export : 56639 · id 75234

#### Couple Moteur  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `26 * courbe(((0,8 * Instant current Filter [A]) / 33): {{0; 0}; {1; 1}; {2; 1,8}; {2,5; 2,18}; {3; 2,45}; {3,5; 2,62}; {4; 2,75}}, Freeze)`
- Lit : `C`, `Instant current Filter`
- Utilisé par : `M1 - Mechanical power`, `M1 - Torque Tracks`, `M2 - Mechanical power`, `M2 - Torque tracks`
- Ligne export : 56651 · id 75235

#### M2 - Mechanical power  `MAC`
- Propriétés : Unit=kW · Limiting object group=Signed
- Logique :
  - **Controlling** = `((M2 - Speed [rpm] * 0,104719) * Couple Moteur [Nm]) / 1000`
- Lit : `Couple Moteur`, `M2 - Speed`
- Utilisé par : *(personne)*
- Ligne export : 56743 · id 75246

#### M2 - Torque tracks  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Couple Moteur [Nm] * 37,2`
- Lit : `Couple Moteur`
- Utilisé par : *(personne)*
- Ligne export : 56805 · id 75256

#### M2 - 25A-50A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(25 < Instant current Filter [A]) AND (Instant current Filter [A] <= 50)`
- Lit : `Instant current Filter`
- Utilisé par : `Statistics log: Engine Use`
- Ligne export : 56849 · id 75264

#### M2 - 50A-75A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(50 < Instant current Filter [A]) AND (Instant current Filter [A] <= 75)`
- Lit : `Instant current Filter`
- Utilisé par : `Statistics log: Engine Use`
- Ligne export : 56903 · id 75273

#### M2 - 75A-100A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(75 < Instant current Filter [A]) AND (Instant current Filter [A] <= 100)`
- Lit : `Instant current Filter`
- Utilisé par : `Statistics log: Engine Use`
- Ligne export : 56957 · id 75282

#### M2 - 100A-125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(100 < Instant current Filter [A]) AND (Instant current Filter [A] <= 125)`
- Lit : `Instant current Filter`
- Utilisé par : `Statistics log: Engine Use`
- Ligne export : 57011 · id 75291

#### M2 - up to 125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `125 < Instant current Filter [A]`
- Lit : `Instant current Filter`
- Utilisé par : `Statistics log: Engine Use`
- Ligne export : 57065 · id 75300

#### Force unbrake  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Brake`, `Brake`, `Adjust group: Master Features`, `Single adjust item: Force unbrake`
- Ligne export : 57110 · id 94241

## ELEC / MOTORS / M-Tracks / Sevcon — actif seulement si `Is_MT_Sevcon`

#### Speed CAN Right  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Math Right [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Math Right`
- Utilisé par : `Convert Right`, `Fordward Right`, `Reverse Right`
- Ligne export : 47496 · id 72904

#### 0x341  `GFIN`
- Propriétés : Identifier=0x341 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Motor Speed - 1 [rpm]; 0}; {Actual Current - 1 [A]; 32}; {Torque - 1 [Raw]; 48}} · Module=Motor Sevcon Right - 1 (Generic) · Module index=1
- Lit : `Actual Current - 1`, `Motor Speed - 1`, `Torque - 1`
- Utilisé par : *(personne)*
- Ligne export : 47510 · id 72905

#### Actual Current - 1  `GPIN`
- Propriétés : Unit=A · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x341`, `SEV - M1 - CURRENT`
- Ligne export : 47535 · id 72906

#### SEV - M1 - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Actual Current - 1 [A]`
- Lit : `Actual Current - 1`
- Utilisé par : `M1 - CURRENT`
- Ligne export : 47548 · id 72907

#### 0x331  `GFIN`
- Propriétés : Identifier=0x331 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{M1 (Right) - Error; 16}; {Statut - 1 [State]; 0}} · Module=Motor Sevcon Right - 1 (Generic) · Module index=0
- Lit : `M1 (Right) - Error`, `State`, `Statut - 1`
- Utilisé par : *(personne)*
- Ligne export : 47590 · id 72915

#### M1 (Right) - Error  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x331`, `Error 1 - MEM`, `M1 - New Error Code`, `M1 - Right Engine CMSG`, `SEV - M1 - Error mode`, `Event log: Electronic Logs`
- Ligne export : 47612 · id 72916

#### 0x351  `GFIN`
- Propriétés : Identifier=0x351 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{SEV - M1 - KTY [Â°C]; 0}; {SEV - M1 - Heatsink [Â°C]; 16}; {Voltage -1 [Raw]; 24}} · Module=Motor Sevcon Right - 1 (Generic) · Module index=2
- Lit : `C`, `SEV - M1 - Heatsink`, `SEV - M1 - KTY`, `Voltage -1`
- Utilisé par : *(personne)*
- Ligne export : 47625 · id 72917

#### SEV - M1 - KTY  `GPIN`
- Propriétés : Unit=Â°C · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x351`, `M1 - KTY`
- Ligne export : 47650 · id 72918

#### SEV - M1 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `M1 (Right) - Error`
  - **Blocking** = `M1 (Right) - Error = 0`
- Lit : `M1 (Right) - Error`
- Utilisé par : `FS1 Switch`, `M1 - Error mode`, `M1 - Normal Mode`, `M1 - Right Engine CMSG`
- Ligne export : 47663 · id 72920

#### M1 - Normal Mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(SEV - M1 - Error mode)`
- Lit : `SEV - M1 - Error mode`
- Utilisé par : `SEV - M1 - Ready`
- Ligne export : 47715 · id 72930

#### SEV - M1 - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `0x341`
- Utilisé par : `M1 - CAN OK`
- Ligne export : 47759 · id 72938

#### Motor Speed - 1  `GPIN`
- Propriétés : Unit=rpm · Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x341`, `SEV - M1 - RUN`, `SEV - M1 - Speed`
- Ligne export : 47802 · id 72946

#### SEV - M1 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Motor Speed - 1 [rpm] <> 0`
- Lit : `Motor Speed - 1`
- Utilisé par : `M1 - RUN`
- Ligne export : 47815 · id 72947

#### SEV - M1 - Heatsink  `GPIN`
- Propriétés : Unit=Â°C · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `0x351`, `M1 - Heatsink`
- Ligne export : 47860 · id 72985

#### SEV - M1 - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M1 - Normal Mode`
- Lit : `M1 - Normal Mode`
- Utilisé par : `M1 - Ready`
- Ligne export : 47872 · id 73003

#### M1 - Right Engine CMSG  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Track Motor · Text=Right/Sbd Motor Error. Stop battery, wait one minute and restart. If the problem persists, contact a service center. · Channel=M1 (Right) - Error
- Logique :
  - **Showing** = `SEV - M1 - Error mode`
- Lit : `M1 (Right) - Error`, `SEV - M1 - Error mode`
- Utilisé par : *(personne)*
- Ligne export : 47915 · id 73011

#### Convert Right  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe(Speed CAN Right [%]: {{-100; 3000}; {0; 0}; {100; 3000}}, Freeze)`
- Lit : `Speed CAN Right`
- Utilisé par : `Throttle Input Voltage`
- Ligne export : 47961 · id 73072

#### Throttle Input Voltage  `GPOUT`
- Propriétés : Input value=Convert Right · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Convert Right`
- Utilisé par : `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 48014 · id 73080

#### VARIATOR ON Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR SUPER ON`
- Lit : `VARIATOR SUPER ON`
- Utilisé par : `Fordward Left`, `Fordward Right`, `Reverse Left`, `Reverse Right`
- Ligne export : 48026 · id 73081

#### Fordward Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed CAN Right [%] < 0) AND (VARIATOR ON Wait)`
- Lit : `Speed CAN Right`, `VARIATOR ON Wait`
- Utilisé par : `FS1 Switch`, `Fordward Switch`
- Ligne export : 48069 · id 73089

#### Fordward Switch  `GPOUT`
- Propriétés : Input value=Fordward Right · Length=1 bit · Type=Unsigned integer
- Lit : `Fordward Right`
- Utilisé par : `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 48121 · id 73098

#### Reverse Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed CAN Right [%] > 0) AND (VARIATOR ON Wait)`
- Lit : `Speed CAN Right`, `VARIATOR ON Wait`
- Utilisé par : `FS1 Switch`, `Inch reverse switch`
- Ligne export : 48132 · id 73099

#### Inch reverse switch  `GPOUT`
- Propriétés : Input value=Reverse Right · Length=1 bit · Type=Unsigned integer
- Lit : `Reverse Right`
- Utilisé par : `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 48184 · id 73108

#### FS1 Switch  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Fordward Right) OR (Reverse Right)`
  - **Blocking** = `SEV - M1 - Error mode`
- Lit : `Fordward Right`, `Reverse Right`, `SEV - M1 - Error mode`
- Utilisé par : `FS1 Switch`, `FS1 Switch`, `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 48195 · id 73109

#### FS1 Switch  `GPOUT`
- Propriétés : Input value=FS1 Switch · Length=1 bit · Type=Unsigned integer
- Lit : `FS1 Switch`
- Utilisé par : `FS1 Switch`, `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 48252 · id 73119

#### GEN - 4 - Right  `GFOUT`
- Propriétés : Identifier=0x411 · Data length=8 · Send method=Continuously · Transmit rate=Every cycle · Unused bits=Set to 0 · Parameters={{Throttle Input Voltage; 0}; {Fordward Switch; 16}; {Inch reverse switch; 17}; {FS1 Switch; 18}} · Module=Motor Sevcon Right - 1 (Generic) · Module index=0
- Lit : `FS1 Switch`, `Fordward Switch`, `Inch reverse switch`, `Throttle Input Voltage`
- Utilisé par : *(personne)*
- Ligne export : 48263 · id 73120

#### Torque - 1  `GPIN`
- Propriétés : Unit=Raw · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x341`, `SEV - M1 - Torque actual`
- Ligne export : 48291 · id 73121

#### Voltage -1  `GPIN`
- Propriétés : Unit=Raw · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x351`, `SEV - M1 - Voltage`
- Ligne export : 48304 · id 73122

#### SEV - M1 - Voltage  `IMAC`
- Propriétés : Unit=V
- Logique :
  - **Controlling** = `Voltage -1 [Raw] * 0,0625`
- Lit : `Voltage -1`
- Utilisé par : `M1 - Voltage`
- Ligne export : 48317 · id 73123

#### SEV - M1 - Torque actual  `IMAC`
- Propriétés : Unit=Nm
- Logique :
  - **Controlling** = `(Torque - 1 [Raw] * 0,0625) * 37,2`
- Lit : `Torque - 1`
- Utilisé par : `M1 - Torque`
- Ligne export : 48360 · id 73131

#### Statut - 1  `GPIN`
- Propriétés : Unit=State · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x331`
- Ligne export : 48412 · id 73139

#### Error 1 - MEM  `MEM`
- Propriétés : Input channel=M1 (Right) - Error · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M1 - New Error Code)`
- Lit : `M1 (Right) - Error`, `M1 - New Error Code`
- Utilisé par : `Error 1`, `M1 - New Error Code`, `Measure group: Track Zapi Right`
- Ligne export : 48425 · id 73161

#### M1 - New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M1 (Right) - Error <> Error 1 - MEM`
  - **Blocking** = `(M1 (Right) - Error = 0) OR (M1 (Right) - Error = 19073)`
- Lit : `Error 1 - MEM`, `M1 (Right) - Error`
- Utilisé par : `Error 1 - MEM`, `Event log: Electronic Logs`
- Ligne export : 48470 · id 73169

#### SEV - M1 - Speed  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Motor Speed - 1 [rpm] * -1`
- Lit : `Motor Speed - 1`
- Utilisé par : `M1 - Speed`
- Ligne export : 48533 · id 73179

#### 0x342  `GFIN`
- Propriétés : Identifier=0x342 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Motor Speed - 2 [rpm]; 0}; {Actual Current - 2 [A]; 32}; {Torque actual- 2 [Raw]; 48}} · Module=Motor Sevcon Left - 2 (Generic) · Module index=1
- Lit : `Actual Current - 2`, `Motor Speed - 2`, `Torque actual- 2`
- Utilisé par : *(personne)*
- Ligne export : 48577 · id 73677

#### Actual Current - 2  `GPIN`
- Propriétés : Unit=A · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x342`, `SEV - M2 - CURRENT`
- Ligne export : 48602 · id 73678

#### SEV - M2 - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Actual Current - 2 [A]`
- Lit : `Actual Current - 2`
- Utilisé par : `M2 - CURRENT`
- Ligne export : 48615 · id 73679

#### 0x332  `GFIN`
- Propriétés : Identifier=0x332 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{M2 (Left) - Error; 16}; {Statut - 2 [Status]; 0}} · Module=Motor Sevcon Left - 2 (Generic) · Module index=0
- Lit : `M2 (Left) - Error`, `Statut - 2`
- Utilisé par : *(personne)*
- Ligne export : 48657 · id 73687

#### M2 (Left) - Error  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x332`, `Error 2 - MEM`, `M2 - Left Engine CMSG`, `M2 - New Error Code`, `SEV - M2 - Error mode`, `Event log: Electronic Logs`
- Ligne export : 48679 · id 73688

#### 0x352  `GFIN`
- Propriétés : Identifier=0x352 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{SEV - M2 - KTY [Â°C]; 0}; {SEV - M2 - Heatsink [Â°C]; 16}; {Voltage -2 [Raw]; 24}} · Module=Motor Sevcon Left - 2 (Generic) · Module index=2
- Lit : `C`, `SEV - M2 - Heatsink`, `SEV - M2 - KTY`, `Voltage -2`
- Utilisé par : *(personne)*
- Ligne export : 48692 · id 73689

#### SEV - M2 - KTY  `GPIN`
- Propriétés : Unit=Â°C · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x352`, `M2 - KTY`
- Ligne export : 48717 · id 73690

#### SEV - M2 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `M2 (Left) - Error`
  - **Blocking** = `M2 (Left) - Error = 0`
- Lit : `M2 (Left) - Error`
- Utilisé par : `FS1 Switch`, `M2 - Error mode`, `M2 - Left Engine CMSG`, `M2 - Normal mode`
- Ligne export : 48730 · id 73691

#### M2 - Normal mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(SEV - M2 - Error mode)`
- Lit : `SEV - M2 - Error mode`
- Utilisé par : `SEV - M2 - Ready`
- Ligne export : 48782 · id 73701

#### SEV - M2 - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `0x342`
- Utilisé par : `M2 - CAN OK`
- Ligne export : 48826 · id 73709

#### Motor Speed - 2  `GPIN`
- Propriétés : Unit=rpm · Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x342`, `SEV - M2 - RUN`, `SEV - M2 - Speed`
- Ligne export : 48869 · id 73717

#### SEV - M2 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Motor Speed - 2 [rpm] <> 0`
- Lit : `Motor Speed - 2`
- Utilisé par : `M2 - RUN`
- Ligne export : 48882 · id 73718

#### SEV - M2 - Heatsink  `GPIN`
- Propriétés : Unit=Â°C · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `0x352`, `M2 - Heatsink`
- Ligne export : 48927 · id 73756

#### SEV - M2 - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M2 - Normal mode`
- Lit : `M2 - Normal mode`
- Utilisé par : `M2 - Ready`
- Ligne export : 48939 · id 73765

#### M2 - Left Engine CMSG  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Left Engine · Text=Left/Port Motor Error. Stop battery, wait one minute and restart. If the problem persists, contact a service center. · Channel=M2 (Left) - Error
- Logique :
  - **Showing** = `SEV - M2 - Error mode`
- Lit : `M2 (Left) - Error`, `SEV - M2 - Error mode`
- Utilisé par : *(personne)*
- Ligne export : 48982 · id 73773

#### Torque actual- 2  `GPIN`
- Propriétés : Unit=Raw · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x342`, `SEV - M2 - Torque actual`
- Ligne export : 49028 · id 73833

#### Voltage -2  `GPIN`
- Propriétés : Unit=Raw · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x352`, `SEV - M2 - Voltage`
- Ligne export : 49041 · id 73834

#### SEV - M2 - Voltage  `IMAC`
- Propriétés : Unit=V
- Logique :
  - **Controlling** = `Voltage -2 [Raw] * 0,0625`
- Lit : `Voltage -2`
- Utilisé par : `M2 - Voltage`
- Ligne export : 49054 · id 73835

#### SEV - M2 - Torque actual  `IMAC`
- Propriétés : Unit=Nm
- Logique :
  - **Controlling** = `(Torque actual- 2 [Raw] * 0,0625) * 37,2`
- Lit : `Torque actual- 2`
- Utilisé par : `M2 - Torque`
- Ligne export : 49097 · id 73843

#### Speed CAN Left  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Math Left [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Math Left`
- Utilisé par : `Convert Left`, `Fordward Left`, `Reverse Left`
- Ligne export : 49149 · id 73851

#### Convert Left  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe(Speed CAN Left [%]: {{-100; 3000}; {0; 0}; {100; 3000}}, Freeze)`
- Lit : `Speed CAN Left`
- Utilisé par : `Throttle Input Voltage`
- Ligne export : 49163 · id 73852

#### Throttle Input Voltage  `GPOUT`
- Propriétés : Input value=Convert Left · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Convert Left`
- Utilisé par : `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 49216 · id 73860

#### VARIATOR ON Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR SUPER ON`
- Lit : `VARIATOR SUPER ON`
- Utilisé par : `Fordward Left`, `Fordward Right`, `Reverse Left`, `Reverse Right`
- Ligne export : 49228 · id 73861

#### Fordward Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed CAN Left [%] < 0) AND (VARIATOR ON Wait)`
- Lit : `Speed CAN Left`, `VARIATOR ON Wait`
- Utilisé par : `FS1 Switch`, `Fordward Switch`
- Ligne export : 49271 · id 73869

#### Fordward Switch  `GPOUT`
- Propriétés : Input value=Fordward Left · Length=1 bit · Type=Unsigned integer
- Lit : `Fordward Left`
- Utilisé par : `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 49323 · id 73878

#### Reverse Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed CAN Left [%] > 0) AND (VARIATOR ON Wait)`
- Lit : `Speed CAN Left`, `VARIATOR ON Wait`
- Utilisé par : `FS1 Switch`, `Inch reverse switch`
- Ligne export : 49334 · id 73879

#### Inch reverse switch  `GPOUT`
- Propriétés : Input value=Reverse Left · Length=1 bit · Type=Unsigned integer
- Lit : `Reverse Left`
- Utilisé par : `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 49386 · id 73888

#### FS1 Switch  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Fordward Left) OR (Reverse Left)`
  - **Blocking** = `SEV - M2 - Error mode`
- Lit : `Fordward Left`, `Reverse Left`, `SEV - M2 - Error mode`
- Utilisé par : `FS1 Switch`, `FS1 Switch`, `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 49397 · id 73889

#### FS1 Switch  `GPOUT`
- Propriétés : Input value=FS1 Switch · Length=1 bit · Type=Unsigned integer
- Lit : `FS1 Switch`
- Utilisé par : `FS1 Switch`, `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 49454 · id 73899

#### GEN - 4 - Left  `GFOUT`
- Propriétés : Identifier=0x412 · Data length=8 · Send method=Continuously · Transmit rate=Every cycle · Unused bits=Set to 0 · Parameters={{Throttle Input Voltage; 0}; {Fordward Switch; 16}; {Inch reverse switch; 17}; {FS1 Switch; 18}} · Module=Motor Sevcon Left - 2 (Generic) · Module index=0
- Lit : `FS1 Switch`, `Fordward Switch`, `Inch reverse switch`, `Throttle Input Voltage`
- Utilisé par : *(personne)*
- Ligne export : 49465 · id 73900

#### Statut - 2  `GPIN`
- Propriétés : Unit=Status · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x332`
- Ligne export : 49493 · id 73901

#### Error 2 - MEM  `MEM`
- Propriétés : Input channel=M2 (Left) - Error · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M2 - New Error Code)`
- Lit : `M2 (Left) - Error`, `M2 - New Error Code`
- Utilisé par : `Error 2`, `M2 - New Error Code`, `Measure group: Track Zapi Left`
- Ligne export : 49506 · id 73922

#### M2 - New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M2 (Left) - Error <> Error 2 - MEM`
  - **Blocking** = `(M2 (Left) - Error = 0) OR (M2 (Left) - Error = 19073)`
- Lit : `Error 2 - MEM`, `M2 (Left) - Error`
- Utilisé par : `Error 2 - MEM`, `Event log: Electronic Logs`
- Ligne export : 49551 · id 73930

#### SEV - M2 - Speed  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Motor Speed - 2 [rpm] * -1`
- Lit : `Motor Speed - 2`
- Utilisé par : `M2 - Speed`
- Ligne export : 49614 · id 73940

## ELEC / MOTORS / M-Tracks / Zapi Left — actif seulement si `Is_MT_Zapi`

#### Speed_CAN_Left  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Math Left [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Math Left`
- Utilisé par : `Speed_Left`
- Ligne export : 52008 · id 86763

#### Speed_Left  `MAC`
- Propriétés : Unit=rpm
- Logique :
  ```qcode
  Result := Speed_CAN_Left * 30 * -1
  ```
- Lit : `Speed_CAN_Left`
- Utilisé par : `Enable`, `Forward`, `Reverse`, `Target_speed_can`
- Ligne export : 52022 · id 86764

#### Node_ID  `IP`
- Propriétés : Default mode={8}
- Utilisé par : `EMERG`, `HeartBeat`, `Node ID`, `PDO1_RX`, `PDO1_TX`, `PDO2_TX`
- Ligne export : 52040 · id 86775

#### EMERG  `IMAC`
- Logique :
  - **Controlling** = `0x80 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 52052 · id 86776

#### GFIN PDO2_TX  `GFIN`
- Propriétés : Identifier=EMERG · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{Left Zapi Error Code; 0}; {alarm present; 16}; {Zapi alarm code; 24}; {flag alarm; 32}; {extra info alarm; 40}} · Module=Motor Zapi - Left - 2 (Generic) · Module index=3
- Lit : `EMERG`, `Left Zapi Error Code`, `Zapi alarm code`, `alarm present`, `extra info alarm`, `flag alarm`
- Utilisé par : *(personne)*
- Ligne export : 52095 · id 86784

#### Left Zapi Error Code  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Error 2 - MEM`, `GFIN PDO2_TX`, `Left Error`, `M2 - Zapi - New Error Code`, `Event log: Electronic Logs`
- Ligne export : 52126 · id 86785

#### alarm present  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Left Error`, `ZAPI_M2_Error mode`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 52139 · id 86786

#### Left Error  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Track Engine · Text=Left/Port Motor Error. Stop battery, wait one minute and restart. If the problem persists, contact a service center. · Channel=Left Zapi Error Code
- Logique :
  - **Showing** = `alarm present`
  - **Hiding** = `Left Zapi Error Code = 0`
- Lit : `Left Zapi Error Code`, `alarm present`
- Utilisé par : `Emmergency Stop Left`
- Ligne export : 52151 · id 86787

#### PDO2_TX  `IMAC`
- Logique :
  - **Controlling** = `0x280 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 52206 · id 86796

#### GFIN PDO2_TX  `GFIN`
- Propriétés : Identifier=PDO2_TX · Data length=8 · Timeout=3000 · Paged protocol={Not used} · Parameters={{Left Zapi Warning; 0}; {Motor Temp; 16}; {Heatsink; 24}; {BDI Percentage; 32}; {Batterie Current; 40}; {Batterie Voltage; 48}} · Module=Motor Zapi - Left - 2 (Generic) · Module index=1
- Lit : `BDI Percentage`, `Batterie Current`, `Batterie Voltage`, `Heatsink`, `Left Zapi Warning`, `Motor Temp`, `PDO2_TX`
- Utilisé par : *(personne)*
- Ligne export : 52249 · id 86804

#### Left Zapi Warning  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Left Warning`, `Left Warning`, `M2 - ZAPI - New Warning Code`, `Warning 2 - MEM`, `Event log: Electronic Logs`
- Ligne export : 52283 · id 86805

#### Left Warning  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Track Engine · Text=Left/Port Motor Warning. Decrease speed. If the problem persists, contact a service center. · Channel=Left Zapi Warning
- Logique :
  - **Showing** = `Left Zapi Warning`
- Lit : `Left Zapi Warning`
- Utilisé par : `Emmergency Stop Left`
- Ligne export : 52296 · id 86806

#### Error Wait  `IDC`
- Propriétés : Toggle=No · Delay on=4000 · Delay off=0
- Logique :
  - **Activating** = `ZAPI_M2_Error mode`
- Lit : `ZAPI_M2_Error mode`
- Utilisé par : `Emmergency Stop Left`, `Reset`
- Ligne export : 52342 · id 86814

#### Emmergency Stop Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Emmergency Stop Left) OR (PositiveFlank(Left Warning)) OR (PositiveFlank(Left Error)) OR (PositiveFlank(Emmergency Stop Right))`
  - **Blocking** = `(NegativeFlank(VARIATOR SUPER ON)) OR (PositiveFlank(Error Wait))`
- Lit : `Emmergency Stop Right`, `Error Wait`, `Left Error`, `Left Warning`, `VARIATOR SUPER ON`
- Utilisé par : `Brake`, `Emmergency Stop Right`, `Enable`, `ZAPI_M2_Error mode`
- Ligne export : 52385 · id 86822

#### ZAPI_M2_Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(alarm present) OR (Emmergency Stop Left)`
- Lit : `Emmergency Stop Left`, `alarm present`
- Utilisé par : `Error Wait`, `M2 - Error mode`, `ZAPI_M2_READY`
- Ligne export : 52468 · id 86835

#### Enable  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed_Left [rpm] <> 0) OR (Enable Power Zapi)`
  - **Blocking** = `Emmergency Stop Left`
- Lit : `Emmergency Stop Left`, `Enable Power Zapi`, `Speed_Left`
- Utilisé par : `Brake`, `Power`
- Ligne export : 52518 · id 86844

#### Target_speed_can  `MAC`
- Propriétés : Unit=Hz/10
- Logique :
  ```qcode
  Result := abs(Speed_Left)  * 5 / 6
  ```
- Lit : `Speed_Left`
- Utilisé par : `Target SPeed`
- Ligne export : 52577 · id 86854

#### PDO1_TX  `IMAC`
- Logique :
  - **Controlling** = `0x180 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 52595 · id 86866

#### GFIN PDO1_TX  `GFIN`
- Propriétés : Identifier=PDO1_TX · Data length=8 · Timeout=3000 · Paged protocol={Not used} · Parameters={{Actual_Speed [Hz/10]; 0}; {Out MNC; 16}; {Stuffing; 31}; {Actual Current [A*5]; 56}; {Status Byte; 32}} · Module=Motor Zapi - Left - 2 (Generic) · Module index=0
- Lit : `Actual Current`, `Actual_Speed`, `Out MNC`, `PDO1_TX`, `Status Byte`, `Stuffing`
- Utilisé par : `ZAPI_M2_CAN OK`
- Ligne export : 52638 · id 86874

#### Actual_Speed  `GPIN`
- Propriétés : Unit=Hz/10 · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `ZAPI_M2_Actual_speed`, `ZAPI_M2_RUN`
- Ligne export : 52669 · id 86875

#### Target SPeed  `GPOUT`
- Propriétés : Input value=Target_speed_can [Hz/10] · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Target_speed_can`
- Utilisé par : `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`
- Ligne export : 52682 · id 86876

#### Power  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `Enable`
- Lit : `Enable`
- Utilisé par : `Enable Power`, `Forward`, `Reverse`, `Measure group: Track Zapi Right`
- Ligne export : 52694 · id 86877

#### Forward  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed_Left [rpm] >= 0) OR (Enable Power Zapi)`
  - **Blocking** = `not(Power)`
- Lit : `Enable Power Zapi`, `Power`, `Speed_Left`
- Utilisé par : `Forward Req`
- Ligne export : 52737 · id 86885

#### Reverse  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Speed_Left [rpm] < 0`
  - **Blocking** = `not(Power)`
- Lit : `Power`, `Speed_Left`
- Utilisé par : `Reverse Req`
- Ligne export : 52797 · id 86895

#### Enable Power  `GPOUT`
- Propriétés : Input value=Power · Length=1 bit · Type=Unsigned integer
- Lit : `Power`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 52850 · id 86904

#### Forward Req  `GPOUT`
- Propriétés : Input value=Forward · Length=1 bit · Type=Unsigned integer
- Lit : `Forward`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 52861 · id 86905

#### Reverse Req  `GPOUT`
- Propriétés : Input value=Reverse · Length=1 bit · Type=Unsigned integer
- Lit : `Reverse`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 52872 · id 86906

#### Brake  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `Enable OR (Force unbrake)`
  - **Blocking** = `Emmergency Stop Left`
- Lit : `Emmergency Stop Left`, `Enable`, `Force unbrake`
- Utilisé par : `Brake`, `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 52883 · id 86907

#### Brake  `GPOUT`
- Propriétés : Input value=Brake · Length=1 bit · Type=Unsigned integer
- Lit : `Brake`
- Utilisé par : `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 52940 · id 86916

#### Stuffing  `IDC`
- Propriétés : Toggle=Yes · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank(GFOUT - PDO1_RX)`
- Lit : `GFOUT - PDO1_RX`
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`, `Stuffing`
- Ligne export : 52951 · id 86917

#### Stuffing  `GPOUT`
- Propriétés : Input value=Stuffing · Length=1 bit · Type=Unsigned integer
- Lit : `Stuffing`
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`
- Ligne export : 52995 · id 86925

#### PDO1_RX  `IMAC`
- Logique :
  - **Controlling** = `0x200 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 53006 · id 86926

#### Power Line  `GPOUT`
- Propriétés : Input value=1 · Length=1 bit · Type=Unsigned integer
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 53049 · id 86934

#### GFOUT - PDO1_RX  `GFOUT`
- Propriétés : Identifier=PDO1_RX · Data length=8 · Send method=Continuously · Transmit rate=40 · Unused bits=Set to 0 · Parameters={{Target SPeed [Hz/10]; 0}; {Enable Power; 16}; {Forward Req; 19}; {Reverse Req; 20}; {Stuffing; 31}; {Power Line; 17}; {Brake; 27}} · Module=Motor Zapi - Left - 2 (Generic) · Module index=0
- Lit : `Brake`, `Enable Power`, `Forward Req`, `PDO1_RX`, `Power Line`, `Reverse Req`, `Stuffing`, `Target SPeed`
- Utilisé par : `Stuffing`
- Ligne export : 53060 · id 86935

#### Motor Temp  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M2_Motor_Temp`
- Ligne export : 53097 · id 86936

#### Heatsink  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M2_Heatsink`, `Measure group: Motor Hydrau`
- Ligne export : 53109 · id 86937

#### BDI Percentage  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 53121 · id 86938

#### Batterie Current  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M2_Batterie Current`
- Ligne export : 53133 · id 86939

#### Batterie Voltage  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M2_Batterie Voltage`
- Ligne export : 53145 · id 86940

#### Out MNC  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 53158 · id 86941

#### Stuffing  `GPIN`
- Propriétés : Length=1 bit · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`, `Stuffing`
- Ligne export : 53170 · id 86942

#### VARIATOR ON Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR SUPER ON`
- Lit : `VARIATOR SUPER ON`
- Utilisé par : `Func State`
- Ligne export : 53182 · id 86943

#### Reset  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Func State`, `Reset`, `MD4-10 page: SETUP`
- Ligne export : 53225 · id 86951

#### Reset  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Reset OR (PositiveFlank(Error Wait))`
- Lit : `Error Wait`, `Reset`
- Utilisé par : `Func State`, `MD4-10 page: SETUP`
- Ligne export : 53238 · id 86952

#### Func State  `SMC`
- Propriétés : Default state name=Stop
- Fonction *Start* :
  - **Activating** = `VARIATOR ON Wait`
  - **Blocking** = `Reset`
- Fonction *Preprop* : (vide)
- Fonction *Reset* :
  - **Activating** = `Reset`
- Lit : `Reset`, `VARIATOR ON Wait`
- Utilisé par : `Func`
- Ligne export : 53289 · id 86961

#### Func  `IP`
- Propriétés : Mode selector=Func State · Default mode: Stop={2} · Mode 1: Start={1} · Mode 2: Preprop={0x80} · Mode 3: Reset={0x81}
- Lit : `Func State`
- Utilisé par : `Func ID`
- Ligne export : 53391 · id 86977

#### Func ID  `GPOUT`
- Propriétés : Input value=Func · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Func`
- Utilisé par : `NMT`
- Ligne export : 53409 · id 86978

#### Node ID  `GPOUT`
- Propriétés : Input value=Node_ID · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Node_ID`
- Utilisé par : `NMT`
- Ligne export : 53420 · id 86979

#### NMT  `GFOUT`
- Propriétés : Identifier=0 · Data length=8 · Send method=Continuously · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{Func ID; 0}; {Node ID; 8}} · Module=Motor Zapi - Left - 2 (Generic) · Module index=1
- Lit : `Func ID`, `Node ID`
- Utilisé par : *(personne)*
- Ligne export : 53431 · id 86980

#### HeartBeat  `IMAC`
- Logique :
  - **Controlling** = `0x700 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN HeartBeat`
- Ligne export : 53453 · id 86981

#### GFIN HeartBeat  `GFIN`
- Propriétés : Identifier=HeartBeat · Data length=1 · Timeout=1000 · Paged protocol={Not used} · Parameters={{HeartBeat State; 0}} · Module=Motor Zapi - Left - 2 (Generic) · Module index=2
- Lit : `HeartBeat`, `HeartBeat State`
- Utilisé par : *(personne)*
- Ligne export : 53496 · id 86989

#### HeartBeat State  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN HeartBeat`, `ZAPI_M2_READY`
- Ligne export : 53515 · id 86990

#### ZAPI_M2_CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `GFIN PDO1_TX`
- Lit : `GFIN PDO1_TX`
- Utilisé par : `M2 - CAN OK`
- Ligne export : 53527 · id 86991

#### ZAPI_M2_Batterie Voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `Batterie Voltage / 3,3333`
- Lit : `Batterie Voltage`
- Utilisé par : `M2 - Voltage`, `Measure group: Track Zapi Left`
- Ligne export : 53570 · id 86999

#### ZAPI_M2_Batterie Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Batterie Current * 2`
- Lit : `Batterie Current`
- Utilisé par : `Measure group: Track Zapi Left`
- Ligne export : 53614 · id 87007

#### ZAPI_M2_Motor_Temp  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Motor Temp - 40`
- Lit : `Motor Temp`
- Utilisé par : `M2 - KTY`, `Measure group: Track Zapi Left`
- Ligne export : 53658 · id 87015

#### ZAPI_M2_Heatsink  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Heatsink`
- Lit : `Heatsink`
- Utilisé par : `M2 - Heatsink`, `Measure group: Track Zapi Left`
- Ligne export : 53702 · id 87023

#### ZAPI_M2_Actual_speed  `MAC`
- Propriétés : Unit=rpm
- Logique :
  ```qcode
  Result := Actual_Speed * 6 / 5
  ```
- Lit : `Actual_Speed`
- Utilisé par : `M2 - Speed`, `Measure group: Track Zapi Left`
- Ligne export : 53744 · id 87031

#### Actual Current  `GPIN`
- Propriétés : Unit=A*5 · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `ZAPI_M2_Actual_current`
- Ligne export : 53762 · id 87042

#### ZAPI_M2_Actual_current  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result := Actual Current * 5
  ```
- Lit : `Actual Current`
- Utilisé par : `M2 - CURRENT`, `ZAPI_M2_Torque`, `Measure group: Track Zapi Left`
- Ligne export : 53774 · id 87043

#### Zapi alarm code  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 53792 · id 87053

#### flag alarm  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 53804 · id 87054

#### extra info alarm  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 53816 · id 87055

#### ZAPI_M2_READY  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `HeartBeat State`
  - **Blocking** = `ZAPI_M2_Error mode`
- Lit : `HeartBeat State`, `ZAPI_M2_Error mode`
- Utilisé par : `M2 - Ready`
- Ligne export : 53828 · id 87056

#### ZAPI_M2_RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Actual_Speed [Hz/10] <> 0`
- Lit : `Actual_Speed`
- Utilisé par : `M2 - RUN`, `Measure group: Track Zapi Left`
- Ligne export : 53878 · id 87065

#### Warning 2 - MEM  `MEM`
- Propriétés : Input channel=Left Zapi Warning · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M2 - ZAPI - New Warning Code)`
- Lit : `Left Zapi Warning`, `M2 - ZAPI - New Warning Code`
- Utilisé par : `M2 - ZAPI - New Warning Code`, `Measure group: Track Zapi Left`
- Ligne export : 53923 · id 87073

#### M2 - ZAPI - New Warning Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Left Zapi Warning <> Warning 2 - MEM`
  - **Blocking** = `Left Zapi Warning = 0`
- Lit : `Left Zapi Warning`, `Warning 2 - MEM`
- Utilisé par : `Warning 2 - MEM`, `Event log: Electronic Logs`
- Ligne export : 53968 · id 87081

#### Error 2 - MEM  `MEM`
- Propriétés : Input channel=Left Zapi Error Code · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M2 - Zapi - New Error Code)`
- Lit : `Left Zapi Error Code`, `M2 - Zapi - New Error Code`
- Utilisé par : `Error 2`, `M2 - Zapi - New Error Code`, `Measure group: Track Zapi Left`
- Ligne export : 54022 · id 87090

#### M2 - Zapi - New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Left Zapi Error Code <> Error 2 - MEM`
  - **Blocking** = `Left Zapi Error Code = 0`
- Lit : `Error 2 - MEM`, `Left Zapi Error Code`
- Utilisé par : `Error 2 - MEM`, `Event log: Electronic Logs`
- Ligne export : 54067 · id 87098

#### Status Byte  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 54121 · id 87107

#### ZAPI_M2_Torque  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `26 * courbe(((0,8 * ZAPI_M2_Actual_current [A]) / 33): {{0; 0}; {1; 1}; {2; 1,8}; {2,5; 2,18}; {3; 2,45}; {3,5; 2,62}; {4; 2,75}}, Freeze)`
- Lit : `C`, `ZAPI_M2_Actual_current`
- Utilisé par : `M2 - Torque`, `Measure group: Track Zapi Left`
- Ligne export : 54133 · id 87108

## ELEC / MOTORS / M-Tracks / Zapi Right — actif seulement si `Is_MT_Zapi`

#### Node_ID  `IP`
- Propriétés : Default mode={4}
- Utilisé par : `EMERG`, `HeartBeat`, `Node ID`, `PDO1_RX`, `PDO1_TX`, `PDO2_TX`
- Ligne export : 49744 · id 85946

#### Node ID  `GPOUT`
- Propriétés : Input value=Node_ID · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Node_ID`
- Utilisé par : `NMT`
- Ligne export : 49756 · id 85947

#### Speed_CAN_Right  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Math Right [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Math Right`
- Utilisé par : `Speed_Right`
- Ligne export : 49767 · id 85948

#### Speed_Right  `MAC`
- Propriétés : Unit=rpm
- Logique :
  ```qcode
  Result := Speed_CAN_Right * 30
  ```
- Lit : `Speed_CAN_Right`
- Utilisé par : `Enable`, `Forward`, `Reverse`, `Target_Speed_can`
- Ligne export : 49781 · id 85949

#### EMERG  `IMAC`
- Logique :
  - **Controlling** = `0x80 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 49799 · id 85959

#### GFIN PDO2_TX  `GFIN`
- Propriétés : Identifier=EMERG · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{Right Zapi Error Code; 0}; {alarm present; 16}; {Zapi alarm code; 24}; {flag alarm; 32}; {extra info alarm; 40}} · Module=Motor Zapi - Right - 1 (Generic) · Module index=0
- Lit : `EMERG`, `Right Zapi Error Code`, `Zapi alarm code`, `alarm present`, `extra info alarm`, `flag alarm`
- Utilisé par : *(personne)*
- Ligne export : 49842 · id 85967

#### Right Zapi Error Code  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Error 1 - MEM`, `GFIN PDO2_TX`, `M1 - Zapi New Error Code`, `Right Error`, `Event log: Electronic Logs`
- Ligne export : 49873 · id 85968

#### alarm present  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Right Error`, `ZAPI_M1_Error mode`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 49886 · id 85969

#### Right Error  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Track Engine · Text=Right/Sbd Motor Error. Stop battery, wait one minute and restart. If the problem persists, contact a service center. · Channel=Right Zapi Error Code
- Logique :
  - **Showing** = `alarm present`
  - **Hiding** = `Right Zapi Error Code = 0`
- Lit : `Right Zapi Error Code`, `alarm present`
- Utilisé par : `Emmergency Stop Right`
- Ligne export : 49898 · id 85970

#### PDO2_TX  `IMAC`
- Logique :
  - **Controlling** = `0x280 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 49953 · id 85979

#### GFIN PDO2_TX  `GFIN`
- Propriétés : Identifier=PDO2_TX · Data length=8 · Timeout=3000 · Paged protocol={Not used} · Parameters={{Right Zapi Warning; 0}; {Motor Temp; 16}; {Heatsink; 24}; {BDI Percentage; 32}; {Batterie Current; 40}; {Batterie Voltage; 48}} · Module=Motor Zapi - Right - 1 (Generic) · Module index=2
- Lit : `BDI Percentage`, `Batterie Current`, `Batterie Voltage`, `Heatsink`, `Motor Temp`, `PDO2_TX`, `Right Zapi Warning`
- Utilisé par : *(personne)*
- Ligne export : 49996 · id 85987

#### Right Zapi Warning  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `M1 - Zapi New Warning Code`, `Right Warning`, `Right Warning`, `Warning 1 - MEM`, `Event log: Electronic Logs`
- Ligne export : 50030 · id 85988

#### Right Warning  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Track Engine · Text=Right/Sbd Motor Warning. Decrease speed. If the problem persists, contact a service center. · Channel=Right Zapi Warning
- Logique :
  - **Showing** = `Right Zapi Warning`
- Lit : `Right Zapi Warning`
- Utilisé par : `Emmergency Stop Right`, `Promeion ZAPI`
- Ligne export : 50043 · id 85989

#### Error Wait  `IDC`
- Propriétés : Toggle=No · Delay on=4000 · Delay off=0
- Logique :
  - **Activating** = `ZAPI_M1_Error mode`
- Lit : `ZAPI_M1_Error mode`
- Utilisé par : `Emmergency Stop Right`, `Reset`
- Ligne export : 50089 · id 86006

#### Emmergency Stop Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Emmergency Stop Right) OR (PositiveFlank(Right Warning)) OR (PositiveFlank(Right Error)) OR (PositiveFlank(Emmergency Stop Left))`
  - **Blocking** = `(NegativeFlank(VARIATOR SUPER ON)) OR (PositiveFlank(Error Wait))`
- Lit : `Emmergency Stop Left`, `Error Wait`, `Right Error`, `Right Warning`, `VARIATOR SUPER ON`
- Utilisé par : `Brake`, `Emmergency Stop Left`, `Enable`, `ZAPI_M1_Error mode`
- Ligne export : 50132 · id 86014

#### ZAPI_M1_Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(alarm present) OR (Emmergency Stop Right)`
- Lit : `Emmergency Stop Right`, `alarm present`
- Utilisé par : `Error Wait`, `M1 - Error mode`, `Measure group: Track Zapi Right`
- Ligne export : 50215 · id 85997

#### Enable  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed_Right [rpm] <> 0) OR (Enable Power Zapi)`
  - **Blocking** = `Emmergency Stop Right`
- Lit : `Emmergency Stop Right`, `Enable Power Zapi`, `Speed_Right`
- Utilisé par : `Brake`, `Power`
- Ligne export : 50265 · id 86027

#### PDO1_TX  `IMAC`
- Logique :
  - **Controlling** = `0x180 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 50324 · id 86037

#### GFIN PDO1_TX  `GFIN`
- Propriétés : Identifier=PDO1_TX · Data length=8 · Timeout=3000 · Paged protocol={Not used} · Parameters={{Actual_Speed [Hz/10]; 0}; {Out MNC; 16}; {Stuffing; 31}; {Actual Current [A*5]; 56}; {Status Byte; 32}} · Module=Motor Zapi - Right - 1 (Generic) · Module index=3
- Lit : `Actual Current`, `Actual_Speed`, `Out MNC`, `PDO1_TX`, `Status Byte`, `Stuffing`
- Utilisé par : `ZAPI_M1_CAN OK`
- Ligne export : 50367 · id 86045

#### Actual Current  `GPIN`
- Propriétés : Unit=A*5 · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `ZAPI_M1_Actual_current`
- Ligne export : 50398 · id 86046

#### ZAPI_M1_Actual_current  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result := Actual Current * 5
  ```
- Lit : `Actual Current`
- Utilisé par : `M1 - CURRENT`, `ZAPI_M1_Torque`, `Measure group: Track Zapi Right`
- Ligne export : 50410 · id 86047

#### Target_Speed_can  `MAC`
- Propriétés : Unit=Hz/10
- Logique :
  ```qcode
  Result := abs(Speed_Right) * 5 / 6
  ```
- Lit : `Speed_Right`
- Utilisé par : `Target_SPeed`
- Ligne export : 50428 · id 86057

#### Target_SPeed  `GPOUT`
- Propriétés : Input value=Target_Speed_can [Hz/10] · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Target_Speed_can`
- Utilisé par : `GFOUT - PDO1_RX`, `Measure group: Track Zapi Right`
- Ligne export : 50446 · id 86069

#### Actual_Speed  `GPIN`
- Propriétés : Unit=Hz/10 · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `ZAPI_M1_Actual_speed`, `ZAPI_M1_RUN`
- Ligne export : 50458 · id 86070

#### Power  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `Enable`
- Lit : `Enable`
- Utilisé par : `Enable Power`, `Forward`, `Reverse`, `Measure group: Track Zapi Right`
- Ligne export : 50471 · id 86071

#### Forward  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed_Right [rpm] >= 0) OR (Enable Power Zapi)`
  - **Blocking** = `not(Power)`
- Lit : `Enable Power Zapi`, `Power`, `Speed_Right`
- Utilisé par : `Forward Req`
- Ligne export : 50514 · id 86079

#### Reverse  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Speed_Right [rpm] < 0`
  - **Blocking** = `not(Power)`
- Lit : `Power`, `Speed_Right`
- Utilisé par : `Reverse Req`
- Ligne export : 50574 · id 86089

#### Enable Power  `GPOUT`
- Propriétés : Input value=Power · Length=1 bit · Type=Unsigned integer
- Lit : `Power`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 50627 · id 86098

#### Forward Req  `GPOUT`
- Propriétés : Input value=Forward · Length=1 bit · Type=Unsigned integer
- Lit : `Forward`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 50638 · id 86099

#### Reverse Req  `GPOUT`
- Propriétés : Input value=Reverse · Length=1 bit · Type=Unsigned integer
- Lit : `Reverse`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 50649 · id 86100

#### Stuffing  `IDC`
- Propriétés : Toggle=Yes · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank(GFOUT - PDO1_RX)`
- Lit : `GFOUT - PDO1_RX`
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`, `Stuffing`
- Ligne export : 50660 · id 86102

#### Stuffing  `GPOUT`
- Propriétés : Input value=Stuffing · Length=1 bit · Type=Unsigned integer
- Lit : `Stuffing`
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`
- Ligne export : 50704 · id 86110

#### PDO1_RX  `IMAC`
- Logique :
  - **Controlling** = `0x200 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 50715 · id 86111

#### Power Line  `GPOUT`
- Propriétés : Input value=1 · Length=1 bit · Type=Unsigned integer
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 50758 · id 86119

#### Brake  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `Enable OR (Force unbrake)`
  - **Blocking** = `Emmergency Stop Right`
- Lit : `Emmergency Stop Right`, `Enable`, `Force unbrake`
- Utilisé par : `Brake`, `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 50769 · id 86120

#### Brake  `GPOUT`
- Propriétés : Input value=Brake · Length=1 bit · Type=Unsigned integer
- Lit : `Brake`
- Utilisé par : `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 50826 · id 86129

#### GFOUT - PDO1_RX  `GFOUT`
- Propriétés : Identifier=PDO1_RX · Data length=8 · Send method=Continuously · Transmit rate=40 · Unused bits=Set to 0 · Parameters={{Target_SPeed [Hz/10]; 0}; {Enable Power; 16}; {Forward Req; 19}; {Reverse Req; 20}; {Stuffing; 31}; {Power Line; 17}; {Brake; 27}} · Module=Motor Zapi - Right - 1 (Generic) · Module index=1
- Lit : `Brake`, `Enable Power`, `Forward Req`, `PDO1_RX`, `Power Line`, `Reverse Req`, `Stuffing`, `Target_SPeed`
- Utilisé par : `Stuffing`
- Ligne export : 50837 · id 86101

#### Motor Temp  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M1_Motor_Temp`
- Ligne export : 50874 · id 86130

#### Heatsink  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M1_Heatsink`, `Measure group: Motor Hydrau`
- Ligne export : 50886 · id 86131

#### BDI Percentage  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 50898 · id 86132

#### Batterie Current  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M1_Batterie Current`
- Ligne export : 50910 · id 86133

#### Batterie Voltage  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M1_Batterie Voltage`
- Ligne export : 50922 · id 86134

#### Out MNC  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 50935 · id 86135

#### Stuffing  `GPIN`
- Propriétés : Length=1 bit · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`, `Stuffing`
- Ligne export : 50947 · id 86136

#### VARIATOR ON Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR SUPER ON`
- Lit : `VARIATOR SUPER ON`
- Utilisé par : `Func State`
- Ligne export : 50959 · id 86137

#### Reset  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(Error Wait)`
- Lit : `Error Wait`
- Utilisé par : `Func State`, `MD4-10 page: SETUP`
- Ligne export : 51002 · id 86145

#### Func State  `SMC`
- Propriétés : Default state name=Stop
- Fonction *Start* :
  - **Activating** = `VARIATOR ON Wait`
  - **Blocking** = `Reset`
- Fonction *Preprop* : (vide)
- Fonction *Reset* :
  - **Activating** = `Reset`
- Lit : `Reset`, `VARIATOR ON Wait`
- Utilisé par : `Func`
- Ligne export : 51046 · id 86153

#### Func  `IP`
- Propriétés : Mode selector=Func State · Default mode: Stop={2} · Mode 1: Start={1} · Mode 2: Preprop={0x80} · Mode 3: Reset={0x81}
- Lit : `Func State`
- Utilisé par : `Func ID`
- Ligne export : 51148 · id 86169

#### Func ID  `GPOUT`
- Propriétés : Input value=Func · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Func`
- Utilisé par : `NMT`
- Ligne export : 51166 · id 86170

#### NMT  `GFOUT`
- Propriétés : Identifier=0 · Data length=8 · Send method=Continuously · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{Func ID; 0}; {Node ID; 8}} · Module=Motor Zapi - Right - 1 (Generic) · Module index=0
- Lit : `Func ID`, `Node ID`
- Utilisé par : *(personne)*
- Ligne export : 51177 · id 86171

#### HeartBeat  `IMAC`
- Logique :
  - **Controlling** = `0x700 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN HeartBeat`
- Ligne export : 51199 · id 86172

#### GFIN HeartBeat  `GFIN`
- Propriétés : Identifier=HeartBeat · Data length=1 · Timeout=1000 · Paged protocol={Not used} · Parameters={{HeartBeat State; 0}} · Module=Motor Zapi - Right - 1 (Generic) · Module index=1
- Lit : `HeartBeat`, `HeartBeat State`
- Utilisé par : *(personne)*
- Ligne export : 51242 · id 86180

#### HeartBeat State  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN HeartBeat`, `ZAPI_M1_READY`
- Ligne export : 51261 · id 86181

#### ZAPI_M1_CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `GFIN PDO1_TX`
- Lit : `GFIN PDO1_TX`
- Utilisé par : `M1 - CAN OK`
- Ligne export : 51273 · id 86182

#### ZAPI_M1_Batterie Voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `Batterie Voltage / 3,3333`
- Lit : `Batterie Voltage`
- Utilisé par : `M1 - Voltage`, `Measure group: Track Zapi Right`
- Ligne export : 51316 · id 86190

#### ZAPI_M1_Batterie Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Batterie Current * 2`
- Lit : `Batterie Current`
- Utilisé par : `Measure group: Track Zapi Right`
- Ligne export : 51360 · id 86198

#### ZAPI_M1_Motor_Temp  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Motor Temp - 40`
- Lit : `Motor Temp`
- Utilisé par : `M1 - KTY`, `Measure group: Track Zapi Right`
- Ligne export : 51404 · id 86206

#### ZAPI_M1_Heatsink  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Heatsink`
- Lit : `Heatsink`
- Utilisé par : `M1 - Heatsink`, `Measure group: Track Zapi Right`
- Ligne export : 51448 · id 86214

#### ZAPI_M1_Actual_speed  `MAC`
- Propriétés : Unit=rpm
- Logique :
  ```qcode
  Result := Actual_Speed * 6 / 5
  ```
- Lit : `Actual_Speed`
- Utilisé par : `M1 - Speed`, `Measure group: Track Zapi Right`
- Ligne export : 51490 · id 86222

#### Zapi alarm code  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 51508 · id 86233

#### flag alarm  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 51520 · id 86234

#### extra info alarm  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 51532 · id 86235

#### ZAPI_M1_READY  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `HeartBeat State`
- Lit : `HeartBeat State`
- Utilisé par : `M1 - Ready`
- Ligne export : 51544 · id 86236

#### ZAPI_M1_RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Actual_Speed [Hz/10] <> 0`
- Lit : `Actual_Speed`
- Utilisé par : `M1 - RUN`, `Measure group: Track Zapi Right`
- Ligne export : 51587 · id 86244

#### Warning 1 - MEM  `MEM`
- Propriétés : Input channel=Right Zapi Warning · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M1 - Zapi New Warning Code)`
- Lit : `M1 - Zapi New Warning Code`, `Right Zapi Warning`
- Utilisé par : `M1 - Zapi New Warning Code`
- Ligne export : 51632 · id 86252

#### M1 - Zapi New Warning Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Right Zapi Warning <> Warning 1 - MEM`
  - **Blocking** = `Right Zapi Warning = 0`
- Lit : `Right Zapi Warning`, `Warning 1 - MEM`
- Utilisé par : `Warning 1 - MEM`, `Event log: Electronic Logs`
- Ligne export : 51677 · id 86260

#### Error 1 - MEM  `MEM`
- Propriétés : Input channel=Right Zapi Error Code · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M1 - Zapi New Error Code)`
- Lit : `M1 - Zapi New Error Code`, `Right Zapi Error Code`
- Utilisé par : `Error 1`, `M1 - Zapi New Error Code`, `Measure group: Track Zapi Right`
- Ligne export : 51731 · id 86269

#### M1 - Zapi New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Right Zapi Error Code <> Error 1 - MEM`
  - **Blocking** = `Right Zapi Error Code = 0`
- Lit : `Error 1 - MEM`, `Right Zapi Error Code`
- Utilisé par : `Error 1 - MEM`, `Event log: Electronic Logs`
- Ligne export : 51776 · id 86277

#### Status Byte  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 51830 · id 86286

#### Right Warning  `GPOUT`
- Propriétés : Input value=Right Zapi Warning · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Right Zapi Warning`
- Utilisé par : `Emmergency Stop Right`, `Promeion ZAPI`
- Ligne export : 51842 · id 86287

#### Left Warning  `GPOUT`
- Propriétés : Input value=Left Zapi Warning · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Left Zapi Warning`
- Utilisé par : `Promeion ZAPI`
- Ligne export : 51854 · id 86288

#### Promeion ZAPI  `GFOUT`
- Propriétés : Identifier=0x7451250 · Data length=8 · Send method=On change · Unused bits=Set to 0 · Parameters={{Right Warning; 0}; {Left Warning; 16}} · Module=Promeion (Generic) · Module index=5
- Lit : `Left Warning`, `Right Warning`
- Utilisé par : *(personne)*
- Ligne export : 51866 · id 86289

#### ZAPI_M1_Torque  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `26 * courbe(((0,8 * ZAPI_M1_Actual_current [A]) / 33): {{0; 0}; {1; 1}; {2; 1,8}; {2,5; 2,18}; {3; 2,45}; {3,5; 2,62}; {4; 2,75}}, Freeze)`
- Lit : `C`, `ZAPI_M1_Actual_current`
- Utilisé par : `M1 - Torque`, `Measure group: Track Zapi Right`
- Ligne export : 51888 · id 86290

## ELEC / Oil Security

#### Oil level Analog  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Calibration={50; 1800; 0; 100} · Alarms={Yes; 5; No; 120} · Module=MC42[1] · Module index=0
- Utilisé par : `Oil level`, `Wait Oil Level`, `Wait Very Low Oil Level`, `Adjust group: Master Setup`, `Dual adjust item: Oil level Analog`, `MD4-10 page: INFO`, `Measure group: Hydraulic`
- Ligne export : 59738 · id 37711

#### Oil security  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `Wait Oil Level`, `Wait Very Low Oil Level`, `Adjust group: Master Features`, `Single adjust item: Oil security`
- Ligne export : 59762 · id 52487

#### Wait Very Low Oil Level  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `Oil level Analog [%] < 70`
  - **Blocking** = `not(Oil security)`
- Lit : `Oil level Analog`, `Oil security`
- Utilisé par : `Oil Not Good`, `Oil level`
- Ligne export : 59775 · id 37712

#### Oil level  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header=Hydraulics · Text=Critical Hydraulic Oil Level.  Add oil and contact your service center.
- Logique :
  - **Showing** = `Wait Very Low Oil Level`
  - **Hiding** = `not(Wait Very Low Oil Level)`
- Lit : `Wait Very Low Oil Level`
- Utilisé par : *(personne)*
- Ligne export : 59828 · id 37720

#### Wait Oil Level  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `Oil level Analog [%] < 85`
  - **Blocking** = `not(Oil security)`
- Lit : `Oil level Analog`, `Oil security`
- Utilisé par : `Oil level`, `MD4-10 page: MAIN`
- Ligne export : 59882 · id 37729

#### Oil level  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Hydraulics · Text=Low Hydraulic Oil Level.  Add oil and contact your service center. · Channel=Oil level Analog [%]
- Logique :
  - **Showing** = `Wait Oil Level`
  - **Hiding** = `not(Wait Oil Level)`
- Lit : `Oil level Analog`, `Wait Oil Level`
- Utilisé par : *(personne)*
- Ligne export : 59935 · id 37737

## ELEC / SYNC

#### SYNC  `GFOUT`
- Propriétés : Identifier=0x80 · Data length=0 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={} · Module=SYNC (Generic) · Module index=0
- Utilisé par : *(personne)*
- Ligne export : 60097 · id 37807
