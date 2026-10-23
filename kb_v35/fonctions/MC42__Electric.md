# MC42 — Electric

742 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Electric — actif seulement si `Is_Electric`

#### Variator Force  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `VARIATOR SUPER ON`, `Adjust group: Master Features`, `Single adjust item: Variator Force`
- Ligne export : 21660 · id 45730

#### MD4 - Start Button Blocking Neutral  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MD4 - Start Button Blocking Neutral) OR (Joystick Zero and (PositiveFlank(MD3_Start/Stop)))`
  - **Blocking** = `NegativeFlank(MD3_Start/Stop)`
- Lit : ``, `Joystick Zero`, `MD3_Start/Stop`
- Utilisé par : `Charger State Finite`, `System Shutdown`, `VARIATOR ON`
- Ligne export : 21673 · id 45732

#### HVLP Pump Test  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `VARIATOR ON`
- Ligne export : 21741 · id 45743

#### With Auto Off Relay  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `Auto Off`, `Global Auto Off Timer`, `ShuntDown Action`, `ShuntDown Turn Off`, `System Shutdown`, `Adjust group: Master Config`, `Single adjust item: With Auto Off Relay`
- Ligne export : 21754 · id 62457

#### F4 Off  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=VIEW BUTTON States
- Fonction *Stop* :
  - **Activating** = `F4 Input`
- Fonction *Ready* : (vide)
- Fonction *Start* : (vide)
- Fonction *Start Free* : (vide)
- Lit : ``, `F4 Input`, `VIEW BUTTON States`
- Utilisé par : `System Shutdown`
- Ligne export : 21767 · id 59356

#### Global Auto Off  `IP`
- Propriétés : Unit=h · Default mode={8}
- Utilisé par : `System Shutdown`, `Adjust group: Setup`, `Single adjust item: Global Auto Off`
- Ligne export : 21882 · id 59183

#### System Shutdown  `IMSG`
- Propriétés : Show message=All · Dialog type=Confirmation · Header=System Shutdown · Text=In few seconds the system shuntdown. · Left button=Switch Off · Right button=Continue
- Logique :
  - **Showing** = `(Global Auto Off Timer [h] >= Global Auto Off [h]) OR (F4 Off) OR (With Auto Off Relay and (Charger State Finite = 5))`
  - **Hiding** = `Flank(MD4 - Start Button Blocking Neutral)`
- Lit : ``, `C`, `Charger State Finite`, `F4 Off`, `Global Auto Off`, `Global Auto Off Timer`, `MD4 - Start Button Blocking Neutral`, `With Auto Off Relay`
- Utilisé par : `Auto Off`, `Global Auto Off Timer`, `ShuntDown Confirmed`
- Ligne export : 21894 · id 59150

#### VARIATOR ON  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MD4 - Start Button Blocking Neutral) OR (HVLP Pump Test)`
  - **Blocking** = `Power Down`
- Lit : ``, `HVLP Pump Test`, `MD4 - Start Button Blocking Neutral`, `Power Down`
- Utilisé par : `Electric Engine STATE`, `Global Auto Off Timer`, `Joystick to zero CMSG`, `VARIATOR SUPER ON`, `VARIATOR Wait OFF`, `Variator hour`, `Wait batt ON`
- Ligne export : 21977 · id 45752

#### Global Auto Off Timer  `TMR`
- Propriétés : Type (Unit)=Hours [h] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `True`
  - **Resetting** = `(Charger CHARGING) OR (VARIATOR ON) OR (PositiveFlank((4 = System Shutdown))) OR (not(With Auto Off Relay)) OR (PositiveFlank((5 = System Shutdown)))`
- Lit : ``, `C`, `Charger CHARGING`, `System Shutdown`, `VARIATOR ON`, `With Auto Off Relay`
- Utilisé par : `System Shutdown`
- Ligne export : 22034 · id 59172

#### ShuntDown Confirmed  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(System Shutdown = 2) OR (Auto Off Confirmed)`
- Lit : ``, `Auto Off Confirmed`, `System Shutdown`
- Utilisé par : `Power Down`, `ShuntDown Message`, `ShuntDown Turn Off`, `ShuntDown Wait`
- Ligne export : 22142 · id 59164

#### Power Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `ShuntDown Confirmed`
- Lit : ``, `ShuntDown Confirmed`
- Utilisé par : `Charger DIGITAL CMD`, `Keep ON`, `Power Down Wait`, `VARIATOR ON`
- Ligne export : 22194 · id 45744

#### Auto Off  `IDC`
- Propriétés : Toggle=No · Delay on=120000 · Delay off=0
- Logique :
  - **Activating** = `System Shutdown = 1`
  - **Blocking** = `not(With Auto Off Relay)`
- Lit : ``, `System Shutdown`, `With Auto Off Relay`
- Utilisé par : `Auto Off Confirmed`
- Ligne export : 22237 · id 59200

#### Wait batt ON  `IDC`
- Propriétés : Toggle=No · Delay on=25000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR ON`
- Lit : ``, `VARIATOR ON`
- Utilisé par : *(personne)*
- Ligne export : 22290 · id 45762

#### PARKER OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=20
- Logique :
  - **Activating** = `(64 = Status:MC42[1]) AND (64 = MD3 State)`
- Lit : ``, `MD3 State`, `Status:MC42[1]`
- Utilisé par : `Battery CMD`, `Keep ON`
- Ligne export : 22333 · id 45771

#### Battery Force  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Battery CMD`, `Adjust group: Master Features`, `Single adjust item: Battery Force`
- Ligne export : 22387 · id 45780

#### VARIATOR Wait OFF  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  - **Activating** = `VARIATOR ON`
- Lit : ``, `VARIATOR ON`
- Utilisé par : `Battery CMD`
- Ligne export : 22400 · id 45781

#### BATT - Reset  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Battery Error Durring 5 s`
- Lit : ``, `Battery Error Durring 5 s`
- Utilisé par : `Battery CMD`, `Keep ON`, `PIN 44`
- Ligne export : 22443 · id 45789

#### Battery CMD  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Battery start by charger) OR (Battery Force) OR (VARIATOR Wait OFF) OR (Need to Charge IDC - Public) OR (Keep ON)`
  - **Blocking** = `(not(PARKER OK)) OR (Power Down Wait) OR (BATT - Reset)`
- Lit : ``, `BATT - Reset`, `Battery Force`, `Battery start by charger`, `Keep ON`, `Need to Charge IDC - Public`, `PARKER OK`, `Power Down Wait`, `VARIATOR Wait OFF`
- Utilisé par : `Battery CMD`, `Keep ON`
- Ligne export : 22486 · id 45797

#### Battery Managment  `SP`
- Propriétés : Input channel=None · Default state name=Automatic · States={Keep On}
- Utilisé par : `Keep ON`, `Adjust group: Master Battery`, `Single adjust item: Battery Managment`
- Ligne export : 22579 · id 62577

#### Keep ON  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Keep ON) OR ((1 = Battery Managment) and (PositiveFlank(Battery CMD)))`
  - **Blocking** = `(not(PARKER OK)) OR (Power Down) OR (BATT - Reset)`
- Lit : ``, `BATT - Reset`, `Battery CMD`, `Battery Managment`, `C`, `PARKER OK`, `Power Down`
- Utilisé par : `Battery CMD`
- Ligne export : 22591 · id 62580

#### Power Down Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `Power Down`
- Lit : ``, `Power Down`
- Utilisé par : `Battery CMD`
- Ligne export : 22682 · id 62698

#### VARIATOR SUPER ON  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(VARIATOR ON and (Battery STATE = 2)) OR (Variator Force)`
- Lit : ``, `Battery STATE`, `VARIATOR ON`, `Variator Force`
- Utilisé par : `Emmergency Stop Left`, `Emmergency Stop Right`, `ON/OFF Var`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `Var Power`, `Active le groupe: Electric / MOTORS / M-Hydrau`, `Active le groupe: Electric / MOTORS / M-Tracks`
- Ligne export : 34116 · id 47926

#### Joystick to zero CMSG  `CMSG`
- Propriétés : Show message=All · Dialog type=Message · Header=Neutral position · Text=Please put joystick in neutral position before start engine.
- Logique :
  - **Showing** = `PositiveFlank(MD3_Start/Stop) AND (not(Joystick Zero)) AND (not(VARIATOR ON))`
- Lit : ``, `Joystick Zero`, `MD3_Start/Stop`, `VARIATOR ON`
- Utilisé par : *(personne)*
- Ligne export : 46671 · id 49246

#### Variator hour  `TMR`
- Propriétés : Type (Unit)=Hours [h] · Store value=Yes · Reset value=10
- Logique :
  - **Decreasing** = `VARIATOR ON`
  - **Resetting** = `Variator hour [h] <= 0`
- Lit : ``, `VARIATOR ON`
- Utilisé par : `10 hours check-up`
- Ligne export : 46750 · id 49275

#### 10 hours check-up  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header=10 hours check-up · Text=Arrange an apointement with your service center.
- Logique :
  - **Showing** = `Variator hour [h] <= 0`
- Lit : ``, `Variator hour`
- Utilisé par : `Event log: Check UP`
- Ligne export : 46811 · id 49286

#### Power Controler Force  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Var Power`, `Adjust group: Master Features`, `Single adjust item: Power Controler Force`
- Ligne export : 46859 · id 49295

#### Var Power  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `(VARIATOR SUPER ON) OR (Power Controler Force)`
- Lit : ``, `Power Controler Force`, `VARIATOR SUPER ON`
- Utilisé par : `Power Controller`
- Ligne export : 46872 · id 49296

#### Power Controller  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Var Power · Module=MC42 (MC42[1]) · Module index=15
- Lit : `Var Power`
- Utilisé par : *(personne)*
- Ligne export : 46922 · id 54647

#### ShuntDown Wait  `IDC`
- Propriétés : Toggle=No · Delay on=4000 · Delay off=0
- Logique :
  - **Activating** = `ShuntDown Confirmed`
- Lit : ``, `ShuntDown Confirmed`
- Utilisé par : `ShuntDown Action`, `ShuntDown Turn Off`
- Ligne export : 46935 · id 62643

#### ShuntDown Action  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(ShuntDown Wait)`
  - **Blocking** = `not(With Auto Off Relay)`
- Lit : ``, `ShuntDown Wait`, `With Auto Off Relay`
- Utilisé par : `K3 Fan Exhaust / AutoOff`
- Ligne export : 46978 · id 62664

#### ShuntDown Turn Off  `CMSG`
- Propriétés : Show message=All · Dialog type=Confirmation · Header=Turn Off · Text=Please Turn Off the boat.
- Logique :
  - **Showing** = `(ShuntDown Wait) AND (not(With Auto Off Relay))`
  - **Hiding** = `NegativeFlank(ShuntDown Confirmed)`
- Lit : ``, `ShuntDown Confirmed`, `ShuntDown Wait`, `With Auto Off Relay`
- Utilisé par : `ShuntDown Message`
- Ligne export : 47030 · id 62743

#### ShuntDown Message  `CMSG`
- Propriétés : Show message=All · Dialog type=Message · Header=Shunt Down · Text=Please wait ...
- Logique :
  - **Showing** = `(ShuntDown Confirmed) AND (not(ShuntDown Turn Off))`
  - **Hiding** = `(ShuntDown Turn Off) OR (NegativeFlank(ShuntDown Confirmed))`
- Lit : ``, `ShuntDown Confirmed`, `ShuntDown Turn Off`
- Utilisé par : *(personne)*
- Ligne export : 47092 · id 62684

#### Auto Off Confirmed  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Auto Off Confirmed) OR (PositiveFlank(Auto Off))`
- Lit : ``, `Auto Off`
- Utilisé par : `ShuntDown Confirmed`
- Ligne export : 47161 · id 62899

## Electric / BATTERY

#### Battery CMD  `FGI`
- Propriétés : Input type=Digital · Input=Battery CMD · Default state name=OFF
- Lit : `Battery CMD`
- Utilisé par : `Main Switch Battery`
- Ligne export : 22742 · id 45812

#### Main Switch Battery  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Battery CMD) AND (Start 3 s) AND (CanOn Wait)`
  - **Blocking** = `(Battery HIGHT TEMP) OR (Battery ERROR DIGIT) OR (Wait during start) OR (IDC Batt Protection)`
- Lit : ``, `Battery CMD`, `Battery ERROR DIGIT`, `Battery HIGHT TEMP`, `CanOn Wait`, `IDC Batt Protection`, `Start 3 s`, `Wait during start`
- Utilisé par : `Bat CMD`, `Charge Mode`, `If not start`, `Switch Battery`, `Wait during start`
- Ligne export : 22753 · id 45813

#### Wait during start  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  - **Activating** = `NegativeFlank(Main Switch Battery)`
- Lit : ``, `Main Switch Battery`
- Utilisé par : `Main Switch Battery`
- Ligne export : 22838 · id 45827

#### Battery max temp  `IP`
- Propriétés : Unit=Â°C · Default mode={55}
- Utilisé par : `Battery HIGHT TEMP`, `Adjust group: Master Battery`, `Single adjust item: Battery max temp`
- Ligne export : 22882 · id 45835

#### Cell_T_max_Master  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW - Cell_T_max_Master [Â°C]`
- Fonction *WattAlps* :
  - **Controlling** = `WattAlps - Cell_T_max_Master [Â°C]`
- Lit : ``, `BMW - Cell_T_max_Master`, `Battery Brand`, `WattAlps - Cell_T_max_Master`
- Utilisé par : `Battery HIGHT TEMP`
- Ligne export : 22894 · id 45836

#### Battery HIGHT TEMP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Cell_T_max_Master [Â°C] >= Battery max temp [Â°C]`
- Lit : ``, `Battery max temp`, `Cell_T_max_Master`
- Utilisé par : `Battery NEED TO CHARGE`, `Main Switch Battery`
- Ligne export : 22967 · id 45858

#### Battery ERROR DIGIT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `(BMW - ERROR DIGIT) OR (WattApls- ERROR DIGIT)`
- Lit : ``, `BMW - ERROR DIGIT`, `WattApls- ERROR DIGIT`
- Utilisé par : `Battery Error Durring 5 s`, `Battery NEED TO CHARGE`, `Battery STATE`, `Main Switch Battery`
- Ligne export : 23012 · id 45866

#### Start 3 s  `IDC`
- Propriétés : Toggle=No · Delay on=3000 · Delay off=0
- Logique :
  - **Activating** = `True`
- Lit : ``
- Utilisé par : `Main Switch Battery`
- Ligne export : 23062 · id 45876

#### Battery CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `(BMW CAN OK) OR (WattAlps - CAN OK)`
- Lit : ``, `BMW CAN OK`, `WattAlps - CAN OK`
- Utilisé par : `Battery NEED TO CHARGE`, `Battery STATE`, `CanOn Wait`, `IDC Batt Protection`, `Measure group: CanBus`
- Ligne export : 23105 · id 45884

#### CanOn Wait  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Battery CAN OK`
- Lit : ``, `Battery CAN OK`
- Utilisé par : `Main Switch Battery`
- Ligne export : 23155 · id 45894

#### BMS_Iso_Resist  `MAC`
- Propriétés : Unit=kOhm · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW - Iso_Resist [kOhm]`
- Fonction *WattAlps* :
  - **Controlling** = `WattAlps - Iso_Resist [kOhm]`
- Lit : ``, `BMW - Iso_Resist`, `Battery Brand`, `WattAlps - Iso_Resist`
- Utilisé par : `Battery Protection`, `IDC Batt Protection`, `Iso Resist`, `Event log: Battery Isolation`
- Ligne export : 23198 · id 45902

#### Battery Protection  `MEM`
- Propriétés : Input channel=Battery Protection · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : ``, `Battery Protection`, `Reset Startup`
- Utilisé par : `Battery Protection`, `IDC Batt Protection`, `Adjust group: Master Battery`, `Single adjust item: Battery Protection`
- Ligne export : 23271 · id 45924

#### IDC Batt Protection  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `(Battery CAN OK) AND (BMS_Iso_Resist [kOhm] <= Iso Resist Protection Level) AND (0 = Battery Protection)`
  - **Blocking** = `BMS_Iso_Resist [kOhm] = 0`
- Lit : ``, `BMS_Iso_Resist`, `Battery CAN OK`, `Battery Protection`, `Iso Resist Protection Level`
- Utilisé par : `Battery Protection`, `Error Iso_Resist`, `Main Switch Battery`
- Ligne export : 23314 · id 45932

#### Battery Brand  `SP`
- Propriétés : Input channel=None · Default state name=BMW · States={WattAlps}
- Utilisé par : `BMS_Iso_Resist`, `BMS_U_Trac`, `Battery InstantVoltage`, `Battery SOC`, `Cell_T_max_Master`, `Current Bat`, `Desired Voltage`, `HighCellVoltage`, `Is_BMW`, `Is_WattAlps`, `LowCellVoltage`, `Max Discharge`, `Adjust group: Master Config`, `Single adjust item: Battery Brand`
- Ligne export : 23384 · id 45943

#### Battery Protection  `SP`
- Propriétés : Input channel=None · Default state name=True · States={False}
- Utilisé par : `Battery Protection`, `Battery Protection`, `IDC Batt Protection`, `Adjust group: Master Battery`, `Single adjust item: Battery Protection`
- Ligne export : 23396 · id 45946

#### Reset Startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset Startup`
- Lit : ``, `Reset Startup`
- Utilisé par : `Battery Protection`, `Reset Startup`, `Reset Startup`
- Ligne export : 23408 · id 45948

#### Is_BMW  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Battery Brand = 0`
- Lit : ``, `Battery Brand`
- Utilisé par : `Active le groupe: Electric / BATTERY / BMW`, `Measure group: Battery BMW`, `Single adjust item: Force BMW Charge`
- Ligne export : 23458 · id 45957

#### Is_WattAlps  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Battery Brand = 1`
- Lit : ``, `Battery Brand`
- Utilisé par : `Active le groupe: Electric / BATTERY / WattApls`
- Ligne export : 26109 · id 46644

#### Battery InstantVoltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW_-_Battery_InstantVoltage [V]`
- Fonction *WattAlps* :
  - **Controlling** = `WattAlps - Battery InstantVoltage [V]`
- Lit : ``, `BMW_-_Battery_InstantVoltage`, `Battery Brand`, `WattAlps - Battery InstantVoltage`
- Utilisé par : `Battery Instant Voltage`, `Battery Instant Voltage Filter`, `Charger end charge`
- Ligne export : 28134 · id 46857

#### Battery Instant Voltage Filter  `SFC`
- Propriétés : Input channel=Battery InstantVoltage [V] · Enable=Yes · Type=Slopes · Slopes={{100; 25}; {50; 50}}
- Lit : `Battery InstantVoltage`
- Utilisé par : `Battery POWER`
- Ligne export : 28207 · id 46879

#### Battery SOC  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW - SOC [%]`
- Fonction *WattAlps* :
  - **Controlling** = `WattAlps - SOC [%]`
- Lit : ``, `BMW - SOC`, `Battery Brand`, `WattAlps - SOC`
- Utilisé par : `Battery CHARGED`, `Battery NEED TO CHARGE`, `Battery SOC`, `Battery SOC Costumer`, `VIEW SOC`
- Ligne export : 28225 · id 46880

#### Current Bat  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW - CURRENT [A]`
- Fonction *WattAlps* :
  - **Controlling** = `WattAlps - CURRENT [A]`
- Lit : ``, `BMW - CURRENT`, `Battery Brand`, `WattAlps - CURRENT`
- Utilisé par : `Battery CURRENT`, `Current Bat`, `Cuurent Bat (ABS)`
- Ligne export : 28298 · id 46903

#### Battery DRIVE MODE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `(BMW - DRIVE MODE) OR (WattAlps - DRIVE MODE)`
- Lit : ``, `BMW - DRIVE MODE`, `WattAlps - DRIVE MODE`
- Utilisé par : `Battery STATE`, `Charger DIGITAL CMD`, `Charger State Finite`, `Drive Mode`, `If not start`, `Save Iso_Resist`, `Statistics log: Electric Stats`
- Ligne export : 28371 · id 46934

#### Battery CURRENT  `SFC`
- Propriétés : Input channel=Current Bat [A] · Enable=Yes · Type=Filter · Filter=90
- Lit : `Current Bat`
- Utilisé par : `Bat - 100A-125A`, `Bat - 1A-25A`, `Bat - 25A-50A`, `Bat - 50A-75A`, `Bat - 75A-100A`, `Bat - up to 125A`, `Battery POWER`
- Ligne export : 28421 · id 46944

#### BMS_U_Trac  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW_-_U_Trac [V]`
- Fonction *WattAlps* :
  - **Controlling** = `WattAlps- U_Trac [V]`
- Lit : ``, `BMW_-_U_Trac`, `Battery Brand`, `WattAlps- U_Trac`
- Utilisé par : `Battery U Track`, `MD3 page: Elec`
- Ligne export : 28433 · id 46945

#### Battery POWER  `MAC`
- Propriétés : Unit=kW · Limiting object group=Signed
- Logique :
  - **Controlling** = `(Battery Instant Voltage Filter [V] * Battery CURRENT [A]) / 1000`
- Lit : ``, `Battery CURRENT`, `Battery Instant Voltage Filter`
- Utilisé par : *(personne)*
- Ligne export : 28506 · id 46967

#### Battery hight temp  `IP`
- Propriétés : Unit=Â°C · Default mode={50}
- Utilisé par : `Adjust group: Master Battery`, `Single adjust item: Battery hight temp`
- Ligne export : 28559 · id 46977

#### Battery STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *READY* :
  - **Activating** = `Battery CAN OK`
  - **Blocking** = `(Battery ERROR DIGIT) OR (Battery DRIVE MODE)`
- Fonction *RUN* :
  - **Activating** = `Battery DRIVE MODE`
  - **Blocking** = `Battery ERROR DIGIT`
- Lit : ``, `Battery CAN OK`, `Battery DRIVE MODE`, `Battery ERROR DIGIT`
- Utilisé par : `VARIATOR SUPER ON`, `VIEW BAT Ready`, `VIEW BAT Run`
- Ligne export : 28571 · id 46987

#### Charge Max  `IP`
- Propriétés : Unit=% · Default mode={100}
- Utilisé par : `Battery CHARGED`, `Battery NEED TO CHARGE`, `Adjust group: Master Battery`, `Adjust group: Setup Charger`, `Single adjust item: Charge Max`
- Ligne export : 28663 · id 47014

#### Bat - 25A-50A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(25 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 50)`
- Lit : ``, `Battery CURRENT`
- Utilisé par : *(personne)*
- Ligne export : 28675 · id 47015

#### Bat - 50A-75A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(50 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 75)`
- Lit : ``, `Battery CURRENT`
- Utilisé par : *(personne)*
- Ligne export : 28729 · id 47024

#### Bat - 75A-100A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(75 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 100)`
- Lit : ``, `Battery CURRENT`
- Utilisé par : *(personne)*
- Ligne export : 28783 · id 47033

#### Bat - 100A-125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(100 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 125)`
- Lit : ``, `Battery CURRENT`
- Utilisé par : *(personne)*
- Ligne export : 28837 · id 47042

#### Bat - up to 125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `125 < Battery CURRENT [A]`
- Lit : ``, `Battery CURRENT`
- Utilisé par : *(personne)*
- Ligne export : 28891 · id 47051

#### Bat - 1A-25A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(1 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 25)`
- Lit : ``, `Battery CURRENT`
- Utilisé par : *(personne)*
- Ligne export : 28936 · id 47059

#### If not start  `IDC`
- Propriétés : Toggle=No · Delay on=40000 · Delay off=0
- Logique :
  - **Activating** = `Main Switch Battery and (not(Battery DRIVE MODE))`
- Lit : ``, `Battery DRIVE MODE`, `Main Switch Battery`
- Utilisé par : `Battery Error Durring 5 s`, `Fail Start Counter`
- Ligne export : 28990 · id 47068

#### Fail Start Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(If not start)`
- Lit : ``, `If not start`
- Utilisé par : `10 fail Starting`
- Ligne export : 29050 · id 47078

#### 10 fail Starting  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Fail Start Counter >= 10`
- Lit : ``, `Fail Start Counter`
- Utilisé par : `Battery Error Durring 5 s`, `Fail Starting`
- Ligne export : 29102 · id 47088

#### Battery Error Durring 5 s  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=1000
- Logique :
  - **Activating** = `(Battery ERROR DIGIT) OR (If not start)`
  - **Blocking** = `10 fail Starting`
- Lit : ``, `10 fail Starting`, `Battery ERROR DIGIT`, `If not start`
- Utilisé par : `BATT - Reset`
- Ligne export : 29147 · id 47096

#### Charging Force  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Battery NEED TO CHARGE`, `Adjust group: Master Features`, `Single adjust item: Charging Force`
- Ligne export : 29204 · id 47106

#### Battery NEED TO CHARGE  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `(Charging Force) OR (Battery SOC [%] < (Charge Max [%] - 5))`
  - **Blocking** = `(Battery ERROR DIGIT) OR (Battery HIGHT TEMP) OR (not(Battery CAN OK))`
- Lit : ``, `Battery CAN OK`, `Battery ERROR DIGIT`, `Battery HIGHT TEMP`, `Battery SOC`, `Charge Max`, `Charging Force`
- Utilisé par : `Battery not need to charge`, `Charger State Finite`
- Ligne export : 29217 · id 47107

#### Balancing State  `SMC`
- Propriétés : Default state name=Normal
- Fonction *Equilibrage* :
  - **Activating** = `Balancing Counter = 0`
- Lit : ``, `Balancing Counter`
- Utilisé par : `Balancing Time`
- Ligne export : 29300 · id 62780

#### Balancing Time  `IP`
- Propriétés : Unit=ms · Mode selector=Balancing State · Default mode: Normal={5000} · Mode 1: Equilibrage={14400000}
- Lit : `Balancing State`
- Utilisé par : `Battery CHARGED`
- Ligne export : 29342 · id 62784

#### Battery CHARGED  `IDC`
- Propriétés : Toggle=No · Delay on=Balancing Time [ms] · Delay off=0
- Logique :
  - **Activating** = `(Battery SOC [%] >= Charge Max [%]) OR (Charger end charge)`
- Lit : ``, `Balancing Time`, `Battery SOC`, `Charge Max`, `Charger end charge`
- Utilisé par : `Balancing Counter`, `Charger State Finite`
- Ligne export : 29356 · id 47120

#### Balancing Frequency  `IP`
- Propriétés : Default mode={5}
- Utilisé par : `Balancing Counter`, `Adjust group: Master Battery`, `Single adjust item: Balancing Frequency`
- Ligne export : 29408 · id 62786

#### Balancing Counter  `ECNT`
- Propriétés : Store value=Yes · Reset value=Balancing Frequency
- Logique :
  - **Decreasing** = `PositiveFlank(Battery CHARGED)`
  - **Resetting** = `Balancing Counter < 0`
- Lit : ``, `Balancing Frequency`, `Battery CHARGED`
- Utilisé par : `Balancing State`
- Ligne export : 29420 · id 62771

#### Save Iso_Resist  `IDC`
- Propriétés : Toggle=No · Delay on=60000 · Delay off=0
- Logique :
  - **Activating** = `Battery DRIVE MODE`
- Lit : ``, `Battery DRIVE MODE`
- Utilisé par : `Event log: Battery Isolation`
- Ligne export : 29481 · id 47128

#### Error Iso_Resist  `IDC`
- Propriétés : Toggle=No · Delay on=100000 · Delay off=0
- Logique :
  - **Activating** = `IDC Batt Protection`
- Lit : ``, `IDC Batt Protection`
- Utilisé par : *(personne)*
- Ligne export : 29524 · id 47136

#### Battery Protection  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header=Battery Protection · Text=Some thing is wrong with the isolation of the battery. · Channel=BMS_Iso_Resist [kOhm]
- Logique :
  - **Showing** = `IDC Batt Protection`
  - **Hiding** = `not(IDC Batt Protection)`
- Lit : ``, `BMS_Iso_Resist`, `Battery Protection`, `IDC Batt Protection`
- Utilisé par : `Battery Protection`, `IDC Batt Protection`, `Adjust group: Master Battery`, `Single adjust item: Battery Protection`
- Ligne export : 29567 · id 47144

#### LowCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *BMW* : (vide)
- Fonction *WattAlps* :
  - **Controlling** = `WattAlps - LowCellVoltage [mV]`
- Lit : ``, `Battery Brand`, `WattAlps - LowCellVoltage`
- Utilisé par : `DiffCellVoltage`
- Ligne export : 29621 · id 47153

#### HighCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *BMW* : (vide)
- Fonction *WattAlps* :
  - **Controlling** = `WattAlps - HighCellVoltage [mV]`
- Lit : ``, `Battery Brand`, `WattAlps - HighCellVoltage`
- Utilisé par : `DiffCellVoltage`
- Ligne export : 29687 · id 47174

#### Fail Starting  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Impossible to start · Text=The battery have try to start 10 time. There are some things wrong, check the log and contact your service center.
- Logique :
  - **Showing** = `10 fail Starting`
- Lit : ``, `10 fail Starting`
- Utilisé par : *(personne)*
- Ligne export : 29753 · id 47195

#### Max Discharge  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW- Max Current [A]`
- Fonction *WattAlps* :
  - **Controlling** = `WattAlps- Max Current [A]`
- Lit : ``, `BMW- Max Current`, `Battery Brand`, `WattAlps- Max Current`
- Utilisé par : `Current Limiting`
- Ligne export : 29799 · id 47203

#### Current Limiting - Error  `FP`
- Propriétés : Unit=A · Default mode={10}
- Utilisé par : `Current Limiting`, `Adjust group: Master Battery`, `Single adjust item: Current Limiting - Error`
- Ligne export : 29872 · id 47224

#### Current Limiting - Increase  `FP`
- Propriétés : Unit=%/s · Default mode={10}
- Utilisé par : `Current Limiting`, `Adjust group: Master Battery`, `Single adjust item: Current Limiting - Increase`
- Ligne export : 29884 · id 47225

#### Current Limiting - Decrease  `FP`
- Propriétés : Unit=%/s · Default mode={100}
- Utilisé par : `Current Limiting`, `Adjust group: Master Battery`, `Single adjust item: Current Limiting - Decrease`
- Ligne export : 29896 · id 47226

#### Cuurent Bat (ABS)  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Abs(Current Bat [A])`
- Lit : ``, `Current Bat`
- Utilisé par : `Current Limiting`
- Ligne export : 29908 · id 47227

#### Current Limiting  `ILC`
- Propriétés : Output=Normal · Enable=Yes · Input channel=Cuurent Bat (ABS) [A] · Start reduction at=Max Discharge [A] · Max error=Current Limiting - Error [A] · Max increase speed=Current Limiting - Increase [%/s] · Max decrease speed=Current Limiting - Decrease [%/s]
- Lit : `Current Limiting - Decrease`, `Current Limiting - Error`, `Current Limiting - Increase`, `Cuurent Bat (ABS)`, `Max Discharge`
- Utilisé par : `Math Left`, `Math Right`
- Ligne export : 29951 · id 47235

#### Battery SOC Costumer  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Battery SOC [%]: 5->0, 95->100, Freeze)`
- Lit : ``, `Battery SOC`
- Utilisé par : `MD3 page: Elec`
- Ligne export : 29966 · id 60199

#### DiffCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed
- Logique :
  - **Controlling** = `Abs((LowCellVoltage [mV] - HighCellVoltage [mV]))`
- Lit : ``, `HighCellVoltage`, `LowCellVoltage`
- Utilisé par : `DiffCellVoltage`
- Ligne export : 30013 · id 62844

#### Iso Resist Protection Level  `IP`
- Propriétés : Default mode={1000}
- Utilisé par : `IDC Batt Protection`, `Adjust group: Master Battery`, `Single adjust item: Iso Resist Protection Level`
- Ligne export : 30065 · id 63125

## Electric / BATTERY / BMW — actif seulement si `Is_BMW`

#### NMT  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{ID; 8}; {State; 0}} · Module=Battery BMW (Generic) · Module index=0
- Lit : `ID`, `State`
- Utilisé par : `Init Seq`
- Ligne export : 23528 · id 45966

#### DcuNodeState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Dcu50Heartbeat`, `DcuNodeState`, `Init Seq`
- Ligne export : 23550 · id 45967

#### BatNodeState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Bat51Hartbeat`, `BatNodeState`, `Init Seq`
- Ligne export : 23562 · id 45968

#### IsoMonNodeState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Init Seq`, `Iso52MonHeartbeat`, `IsoMonNodeState`
- Ligne export : 23574 · id 45969

#### Init Seq  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank(NMT)`
  - **Blocking** = `(DcuNodeState = 5) AND (BatNodeState = 5) AND (IsoMonNodeState = 5)`
- Lit : ``, `BatNodeState`, `DcuNodeState`, `IsoMonNodeState`, `NMT`
- Utilisé par : `Init Counter`
- Ligne export : 23586 · id 45970

#### Init Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Init Seq`
  - **Resetting** = `Init Counter >= 3`
- Lit : ``, `Init Seq`
- Utilisé par : `Node Init`
- Ligne export : 23657 · id 45981

#### Node Init  `SP`
- Propriétés : Input channel=Init Counter · Default state name=0x50 · States={0x51; 0x52}
- Lit : `Init Counter`
- Utilisé par : `Node Init ID`
- Ligne export : 23717 · id 45992

#### Node Init ID  `IP`
- Propriétés : Mode selector=Node Init · Default mode: 0x50={0x50} · Mode 1: 0x51={0x51} · Mode 2: 0x52={0x52}
- Lit : `Node Init`
- Utilisé par : `ID`
- Ligne export : 23730 · id 45995

#### ID  `GPOUT`
- Propriétés : Input value=Node Init ID · Length=8 · Type=Unsigned integer
- Lit : `Node Init ID`
- Utilisé par : `NMT`
- Ligne export : 23746 · id 45996

#### State  `GPOUT`
- Propriétés : Input value=1 · Length=8 · Type=Unsigned integer
- Utilisé par : `0x331`, `BMS_VMU_STATUS`, `NMT`, `Speed All State`, `Up/DOWN STATE`
- Ligne export : 23757 · id 45997

#### Dcu50Heartbeat  `GFIN`
- Propriétés : Identifier=0x750 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{DcuNodeState; 0}} · Module=Battery BMW (Generic) · Module index=1
- Lit : `DcuNodeState`
- Utilisé par : `BMW CAN OK`
- Ligne export : 23768 · id 45998

#### Bat51Hartbeat  `GFIN`
- Propriétés : Identifier=0x751 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{BatNodeState; 0}} · Module=Battery BMW (Generic) · Module index=2
- Lit : `BatNodeState`
- Utilisé par : *(personne)*
- Ligne export : 23787 · id 45999

#### Iso52MonHeartbeat  `GFIN`
- Propriétés : Identifier=1874 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{IsoMonNodeState; 0}} · Module=Battery BMW (Generic) · Module index=3
- Lit : `IsoMonNodeState`
- Utilisé par : *(personne)*
- Ligne export : 23806 · id 46000

#### Bat Counter  `ECNT`
- Propriétés : Store value=No · Reset value=1
- Logique :
  - **Increasing** = `PositiveFlank(Sync)`
  - **Resetting** = `Bat Counter >= 201`
- Lit : ``, `Sync`
- Utilisé par : `SyncCounter`
- Ligne export : 23825 · id 46001

#### SyncCounter  `GPOUT`
- Propriétés : Input value=Bat Counter · Length=8 · Type=Unsigned integer
- Lit : `Bat Counter`
- Utilisé par : `Sync`
- Ligne export : 23886 · id 46012

#### Sync  `GFOUT`
- Propriétés : Identifier=0x80 · Data length=1 · Send method=Continuously · Transmit rate=20 · Unused bits=Set to 0 · Parameters={{SyncCounter; 0}} · Module=Battery BMW (Generic) · Module index=1
- Lit : `SyncCounter`
- Utilisé par : `Bat Counter`
- Ligne export : 23897 · id 46013

#### Bat51TPdo1  `GFIN`
- Propriétés : Identifier=0x1D1 · Data length=DonÂt care · Timeout=200 · Paged protocol={Not used} · Parameters={{BatState; 0}; {BatStateOfCharge; 8}; {BatCurrent; 16}; {BatPackVoltage; 32}; {BatBusVoltage; 48}} · Module=Battery BMW (Generic) · Module index=9
- Lit : `BatBusVoltage`, `BatCurrent`, `BatPackVoltage`, `BatState`, `BatStateOfCharge`
- Utilisé par : *(personne)*
- Ligne export : 23916 · id 46023

#### BatState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMW - DRIVE MODE`, `Bat51TPdo1`, `BatState`, `Battery State MEM`, `New Battery State`, `Event log: Electronic Logs`, `Measure group: Battery BMW`
- Ligne export : 23947 · id 46024

#### BatStateOfCharge  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMW - SOC`, `Bat51TPdo1`
- Ligne export : 23959 · id 46025

#### BatCurrent  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - CURRENT`, `Bat51TPdo1`
- Ligne export : 23971 · id 46026

#### BatPackVoltage  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW_-_Battery_InstantVoltage`, `Bat51TPdo1`
- Ligne export : 23984 · id 46027

#### BatBusVoltage  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW_-_U_Trac`, `Bat51TPdo1`
- Ligne export : 23997 · id 46028

#### Iso52MonTPdo1  `GFIN`
- Propriétés : Identifier=466 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{IsoMonResistance; 0}; {IsoMonVoltage; 16}; {IsoMonState; 32}} · Module=Battery BMW (Generic) · Module index=7
- Lit : `IsoMonResistance`, `IsoMonState`, `IsoMonVoltage`
- Utilisé par : *(personne)*
- Ligne export : 24010 · id 46029

#### IsoMonResistance  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - Iso_Resist`, `Iso52MonTPdo1`
- Ligne export : 24035 · id 46030

#### IsoMonVoltage  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Iso52MonTPdo1`
- Ligne export : 24048 · id 46031

#### IsoMonState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Iso52MonTPdo1`, `IsoMonState`, `Measure group: Battery BMW`
- Ligne export : 24061 · id 46032

#### Force BMW Charge  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Charge Mode`, `Adjust group: Master Battery`, `Single adjust item: Force BMW Charge`
- Ligne export : 24073 · id 46033

#### Charge Mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Charger CHARGING) OR (Force BMW Charge)`
  - **Blocking** = `not(Main Switch Battery)`
- Lit : ``, `Charger CHARGING`, `Force BMW Charge`, `Main Switch Battery`
- Utilisé par : `Bat CMD`
- Ligne export : 24086 · id 46034

#### Bat CMD  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ON* :
  - **Activating** = `Main Switch Battery`
  - **Blocking** = `Charge Mode`
- Fonction *Charge* :
  - **Activating** = `Charge Mode`
- Lit : ``, `Charge Mode`, `Main Switch Battery`
- Utilisé par : `Command Value`
- Ligne export : 24144 · id 46044

#### Command Value  `IP`
- Propriétés : Mode selector=Bat CMD · Default mode: OFF={0x00} · Mode 1: ON={0x01} · Mode 2: Charge={0x03}
- Lit : `Bat CMD`
- Utilisé par : `BatCommand`
- Ligne export : 24222 · id 46057

#### BatCommand  `GPOUT`
- Propriétés : Input value=Command Value · Length=8 · Type=Unsigned integer
- Lit : `Command Value`
- Utilisé par : `Bat51RPdo1`
- Ligne export : 24238 · id 46058

#### BatCoolingPolicy  `GPOUT`
- Propriétés : Input value=0x14 · Length=8 · Type=Unsigned integer
- Utilisé par : `Bat51RPdo1`
- Ligne export : 24249 · id 46059

#### Bat51RPdo1  `GFOUT`
- Propriétés : Identifier=593 · Data length=8 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={{BatCommand; 0}; {BatCoolingPolicy; 8}} · Module=Battery BMW (Generic) · Module index=2
- Lit : `BatCommand`, `BatCoolingPolicy`
- Utilisé par : *(personne)*
- Ligne export : 24260 · id 46060

#### IsoMonCommand  `GPOUT`
- Propriétés : Input value=0x01 · Length=8 · Type=Unsigned integer
- Utilisé par : `Iso52MonRPdo1`
- Ligne export : 24282 · id 46061

#### Warning Level  `IP`
- Propriétés : Default mode={750}
- Utilisé par : `IsoMonWarningLevel`
- Ligne export : 24293 · id 46062

#### IsoMonWarningLevel  `GPOUT`
- Propriétés : Input value=Warning Level · Length=16 · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Warning Level`
- Utilisé par : `Iso52MonRPdo1`
- Ligne export : 24305 · id 46063

#### Error Level  `IP`
- Propriétés : Default mode={250}
- Utilisé par : `IsoMonErrorLevel`
- Ligne export : 24317 · id 46064

#### IsoMonErrorLevel  `GPOUT`
- Propriétés : Input value=Error Level · Length=16 · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Error Level`
- Utilisé par : `Iso52MonRPdo1`
- Ligne export : 24329 · id 46065

#### Iso52MonRPdo1  `GFOUT`
- Propriétés : Identifier=0x252 · Data length=8 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={{IsoMonCommand; 0}; {IsoMonWarningLevel; 8}; {IsoMonErrorLevel; 24}} · Module=Battery BMW (Generic) · Module index=3
- Lit : `IsoMonCommand`, `IsoMonErrorLevel`, `IsoMonWarningLevel`
- Utilisé par : *(personne)*
- Ligne export : 24341 · id 46066

#### Bat51TPdo2  `GFIN`
- Propriétés : Identifier=0x2D1 · Data length=DonÂt care · Timeout=5000 · Paged protocol={Not used} · Parameters={{BatAvgTemp; 0}; {BatMinCellTemp; 8}; {BatMaxCellTemp; 16}; {BatBalancingState; 24}; {BatTimeToFullMinute; 32}} · Module=Battery BMW (Generic) · Module index=0
- Lit : `BatAvgTemp`, `BatBalancingState`, `BatMaxCellTemp`, `BatMinCellTemp`, `BatTimeToFullMinute`
- Utilisé par : *(personne)*
- Ligne export : 24366 · id 46067

#### BatAvgTemp  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Bat51TPdo2`
- Ligne export : 24397 · id 46068

#### BatMinCellTemp  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Bat51TPdo2`
- Ligne export : 24409 · id 46069

#### BatMaxCellTemp  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMW - Cell_T_max_Master`, `Bat51TPdo2`
- Ligne export : 24421 · id 46070

#### BatBalancingState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Bat51TPdo2`
- Ligne export : 24433 · id 46071

#### BatTimeToFullMinute  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51TPdo2`
- Ligne export : 24445 · id 46072

#### Bat51TPdo3  `GFIN`
- Propriétés : Identifier=0x3D1 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{BatPowerLimitChargeRaw; 0}; {BatPowerLimitDischargeRaw; 16}; {BatEnergyRemainingRaw; 32}} · Module=Battery BMW (Generic) · Module index=8
- Lit : `BatEnergyRemainingRaw`, `BatPowerLimitChargeRaw`, `BatPowerLimitDischargeRaw`
- Utilisé par : *(personne)*
- Ligne export : 24458 · id 46073

#### BatPowerLimitChargeRaw  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51TPdo3`, `BatPowerLimitCharge`
- Ligne export : 24483 · id 46074

#### BatPowerLimitDischargeRaw  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51TPdo3`, `BatPowerLimitDischarge`
- Ligne export : 24496 · id 46075

#### BatEnergyRemainingRaw  `GPIN`
- Propriétés : Length=32 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51TPdo3`, `BatEnergyRemaining`
- Ligne export : 24509 · id 46076

#### BMW_-_Battery_InstantVoltage  `MAC`
- Propriétés : Unit=V
- Logique :
  ```qcode
  Result := BatPackVoltage * 0.1
  ```
- Lit : `BatPackVoltage`
- Utilisé par : `Battery InstantVoltage`, `Measure group: Battery BMW`
- Ligne export : 24522 · id 46077

#### BMW - CURRENT  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result := BatCurrent * 0.02 - 640
  ```
- Lit : `BatCurrent`
- Utilisé par : `Current Bat`, `Measure group: Battery BMW`
- Ligne export : 24540 · id 46087

#### BMW - Cell_T_max_Master  `MAC`
- Propriétés : Unit=Â°C
- Logique :
  ```qcode
  Result := BatMaxCellTemp - 40
  ```
- Lit : `BatMaxCellTemp`
- Utilisé par : `Cell_T_max_Master`, `Measure group: Battery BMW`
- Ligne export : 24558 · id 46098

#### BMW - Iso_Resist  `MAC`
- Propriétés : Unit=kOhm · Limiting object group=Signed
- Logique :
  - **Controlling** = `IsoMonResistance`
- Lit : ``, `IsoMonResistance`
- Utilisé par : `BMS_Iso_Resist`, `Measure group: Battery BMW`
- Ligne export : 24576 · id 46108

#### BMW_-_U_Trac  `MAC`
- Propriétés : Unit=V
- Logique :
  ```qcode
  Result := BatBusVoltage * 0.1
  ```
- Lit : `BatBusVoltage`
- Utilisé par : `BMS_U_Trac`, `BMW- Max Current`, `Measure group: Battery BMW`
- Ligne export : 24618 · id 46116

#### DcuNodeState  `SMC`
- Propriétés : Default state name=Boot
- Fonction *Stopped* :
  - **Activating** = `DcuNodeState = 4`
- Fonction *Operational* :
  - **Activating** = `DcuNodeState = 5`
- Fonction *Pre-Op* :
  - **Activating** = `DcuNodeState = 127`
- Lit : ``, `DcuNodeState`
- Utilisé par : `Dcu50Heartbeat`, `Init Seq`
- Ligne export : 24636 · id 46126

#### BatNodeState  `SMC`
- Propriétés : Default state name=Boot
- Fonction *Stopped* :
  - **Activating** = `BatNodeState = 4`
- Fonction *Operational* :
  - **Activating** = `BatNodeState = 5`
- Fonction *Pre-Op* :
  - **Activating** = `BatNodeState = 127`
- Lit : ``, `BatNodeState`
- Utilisé par : `Bat51Hartbeat`, `Init Seq`
- Ligne export : 24744 · id 46142

#### IsoMonNodeState  `SMC`
- Propriétés : Default state name=Boot
- Fonction *Stopped* :
  - **Activating** = `IsoMonNodeState = 4`
- Fonction *Operational* :
  - **Activating** = `IsoMonNodeState = 5`
- Fonction *Pre-Op* :
  - **Activating** = `IsoMonNodeState = 127`
- Lit : ``, `IsoMonNodeState`
- Utilisé par : `Init Seq`, `Iso52MonHeartbeat`
- Ligne export : 24852 · id 46158

#### BMW - SOC  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `BatStateOfCharge * 0,5`
- Lit : ``, `BatStateOfCharge`
- Utilisé par : `Battery SOC`, `Measure group: Battery BMW`
- Ligne export : 24960 · id 46174

#### BMW CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  - **Activating** = `Dcu50Heartbeat`
- Lit : ``, `Dcu50Heartbeat`
- Utilisé par : `Battery CAN OK`, `Charger CAN BUS OK`, `Measure group: Battery BMW`
- Ligne export : 25004 · id 46182

#### Dcu50Error  `GFIN`
- Propriétés : Identifier=208 · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{DcuErrorCode; 24}; {DcuError; 8}} · Module=Battery BMW (Generic) · Module index=4
- Lit : `DcuError`, `DcuErrorCode`
- Utilisé par : *(personne)*
- Ligne export : 25047 · id 55772

#### DcuErrorCode  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Dcu50Error`, `DcuErrorCode M`, `DcuErrorCode Out`, `DcuErrorCode TF`
- Ligne export : 25069 · id 55773

#### Bat51Error  `GFIN`
- Propriétés : Identifier=0xD1 · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{BatErrorCode; 24}; {BatError; 8}} · Module=Battery BMW (Generic) · Module index=5
- Lit : `BatError`, `BatErrorCode`
- Utilisé par : *(personne)*
- Ligne export : 25082 · id 55775

#### BatErrorCode  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51Error`, `BatErrorCode M`, `BatErrorCode Out`, `BatErrorCode TF`, `Battery Error Code`, `New Error Code`
- Ligne export : 25104 · id 55776

#### Iso52MonError  `GFIN`
- Propriétés : Identifier=210 · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{IsoMonErrorCode; 24}; {IsoMonError; 8}} · Module=Battery BMW (Generic) · Module index=6
- Lit : `IsoMonError`, `IsoMonErrorCode`
- Utilisé par : *(personne)*
- Ligne export : 25117 · id 55778

#### IsoMonErrorCode  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Iso52MonError`, `IsoMonErrorCode M`, `IsoMonErrorCode Out`, `IsoMonErrorCode TF`
- Ligne export : 25139 · id 55779

#### BMW - ERROR DIGIT  `IDC`
- Propriétés : Toggle=No · Delay on=100 · Delay off=100
- Lit : ``
- Utilisé par : `Battery ERROR DIGIT`, `Measure group: Battery BMW`
- Ligne export : 25152 · id 46190

#### BMW - DRIVE MODE  `IDC`
> Kreisel 
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `BatState = 2`
- Lit : ``, `BatState`
- Utilisé par : `Battery DRIVE MODE`, `Measure group: Battery BMW`
- Ligne export : 25188 · id 46206

#### BatPowerLimitCharge  `MAC`
- Propriétés : Unit=kW
- Logique :
  ```qcode
  Result := BatPowerLimitChargeRaw * 0.01 - 320
  ```
- Lit : `BatPowerLimitChargeRaw`
- Utilisé par : `Measure group: Battery BMW`
- Ligne export : 25233 · id 46214

#### BatPowerLimitDischarge  `MAC`
- Propriétés : Unit=kW
- Logique :
  ```qcode
  Result := BatPowerLimitDischargeRaw * 0.01 - 320
  ```
- Lit : `BatPowerLimitDischargeRaw`
- Utilisé par : `BMW- Max Current`, `Measure group: Battery BMW`
- Ligne export : 25251 · id 46225

#### BatEnergyRemaining  `MAC`
- Propriétés : Unit=kWh
- Logique :
  ```qcode
  Result := BatEnergyRemainingRaw * 0.001
  ```
- Lit : `BatEnergyRemainingRaw`
- Utilisé par : `Measure group: Battery BMW`
- Ligne export : 25269 · id 46254

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
- Utilisé par : `Max Discharge`
- Ligne export : 25287 · id 50640

#### DcuError  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `Dcu50Error`
- Ligne export : 25311 · id 55774

#### BatError  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `Bat51Error`
- Ligne export : 25323 · id 55777

#### IsoMonError  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `Iso52MonError`
- Ligne export : 25335 · id 55780

#### New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `BatErrorCode <> Battery Error Code`
- Lit : ``, `BatErrorCode`, `Battery Error Code`
- Utilisé par : `Battery Error Code`, `Event log: Electronic Logs`
- Ligne export : 25347 · id 55781

#### Battery Error Code  `MEM`
- Propriétés : Input channel=BatErrorCode · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(New Error Code)`
- Lit : ``, `BatErrorCode`, `New Error Code`
- Utilisé par : `New Error Code`
- Ligne export : 25392 · id 55789

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
- Ligne export : 25437 · id 55797

#### DcuErrorCode P  `SP`
- Propriétés : Input channel=DcuErrorCode M · Default state name=0 · States={4097; 8192}
- Lit : `DcuErrorCode M`
- Utilisé par : `DcuErrorCode T`
- Ligne export : 25461 · id 55814

#### DcuErrorCode T  `TP`
- Propriétés : Mode selector=DcuErrorCode P · Default mode: 0={NoError} · Mode 1: 4097={HVIL_Fail} · Mode 2: 8192={EMCY_Off}
- Lit : `DcuErrorCode P`
- Utilisé par : `DcuErrorCode TF`
- Ligne export : 25474 · id 55817

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
- Ligne export : 25489 · id 55818

#### BatErrorCode P  `SP`
- Propriétés : Input channel=BatErrorCode M · Default state name=0 · States={4097; 4098; 4099; 8193; 12289; 12290; 12291; 12292; 16385; 20481; 24577; 28673; 32769; 40961; 40962; 40963; 40964; 40965; 40966; 40967; 40968; 40969; 40970; 40971; 40972; 40973; 40974; 40975; 40976; 40977; 40978; 40979; 40980; 40981; 40982; 40983; 40984; 40985; 40992; 40993; 45057; 45058; 45059; 45060; 45061; 45062; 45063; 45064; 45065; 49153; 49154; 53249; 65280}
- Lit : `BatErrorCode M`
- Utilisé par : `BatErrorCode T`
- Ligne export : 25615 · id 56039

#### BatErrorCode T  `TP`
- Propriétés : Mode selector=BatErrorCode P · Default mode: 0={NoError} · Mode 1: 4097={OneContactorSticky} · Mode 2: 4098={TwoContactorsSticky} · Mode 3: 4099={PrechargeLock} · Mode 4: 8193={Pack_OverVoltage} · Mode 5: 12289={Pack_UnderVoltage} · Mode 6: 12290={SocLow} · Mode 7: 12291={SocVeryLow} · Mode 8: 12292={SocCriticalLow} · Mode 9: 16385={Bus_OverVoltage} · Mode 10: 20481={Bus_UnderVoltage} · Mode 11: 24577={HVIL_Fail} · Mode 12: 28673={Communication_Error} · Mode 13: 32769={OverCurrent} · Mode 14: 40961={TemperatureHigh} · Mode 15: 40962={TemperatureLow} · Mode 16: 40963={CoolingCompConnLost} · Mode 17: 40964={CoolingModuleConnLost} · Mode 18: 40965={CoolingCompDrOvertemp} · Mode 19: 40966={CoolingCompDrOvercurrent} · Mode 20: 40967={CoolingCompSdOverUnderVoltage} · Mode 21: 40968={CoolingCompSdCriticalOvertemp} · Mode 22: 40969={CoolingCompSdTorqueExceeded} · Mode 23: 40970={CoolingCompSdLinCommError} · Mode 24: 40971={CoolingCompSdExternalSupply} · Mode 25: 40972={CoolingCompSdErrorInverterSupply} · Mode 26: 40973={CoolingCompSdErrorSensor} · Mode 27: 40974={CoolingCompSdShortcircuit} · Mode 28: 40975={CoolingCompSdRunUp} · Mode 29: 40976={CoolingWaterFlowLow} · Mode 30: 40977={CoolingWaterFlowImplausible} · Mode 31: 40978={CoolingWaterFlowVariation} · Mode 32: 40979={CoolingWaterTempLow} · Mode 33: 40980={CoolingWaterTempHigh} · Mode 34: 40981={CoolingWaterTempDiffLow} · Mode 35: 40982={CoolingPresLow} · Mode 36: 40983={CoolingPresHigh} · Mode 37: 40984={CoolingWaterInTempSensor} · Mode 38: 40985={CoolingWaterOutTempSensor} · Mode 39: 40992={CoolingModulePdo2Missing} · Mode 40: 40993={CoolingModulePdo3Missing} · Mode 41: 45057={Internal_Error} · Mode 42: 45058={ServiceDisconnect} · Mode 43: 45059={AbortCharging} · Mode 44: 45060={CoolingValveShortToGround} · Mode 45: 45061={CoolingValveShortToUbat} · Mode 46: 45062={CoolingValveWireBroken} · Mode 47: 45063={CoolingValveDriverError} · Mode 48: 45064={CoolingValveValveStuckAtClosed} · Mode 49: 45065={CoolingValveValveStuckAtOpen} · Mode 50: 49153={Category6Failure} · Mode 51: 49154={Category7Failure} · Mode 52: 53249={ThermalEventHazard} · Mode 53: 65280={DeviceSoftwareGenericFail}
- Lit : `BatErrorCode P`
- Utilisé par : `BatErrorCode TF`
- Ligne export : 25679 · id 56093

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
- Ligne export : 25796 · id 56094

#### IsoMonErrorCode P  `SP`
- Propriétés : Input channel=IsoMonErrorCode M · Default state name=0 · States={4097; 8193; 12289; 16385; 16386; 20481; 65280}
- Lit : `IsoMonErrorCode M`
- Utilisé par : `IsoMonErrorCode T`
- Ligne export : 25828 · id 56127

#### IsoMonErrorCode T  `TP`
- Propriétés : Mode selector=IsoMonErrorCode P · Default mode: 0={NoError} · Mode 1: 4097={IsoMeasurementNotWorking} · Mode 2: 8193={PlausibilityCheckFailed} · Mode 3: 12289={Warning_Level} · Mode 4: 16385={Error_Intern_Level} · Mode 5: 16386={Error_Extern_Level} · Mode 6: 20481={CommunicationError} · Mode 7: 65280={DeviceSoftwareGenericFail}
- Lit : `IsoMonErrorCode P`
- Utilisé par : `IsoMonErrorCode TF`
- Ligne export : 25846 · id 56135

#### DcuErrorCode TF  `TFC`
- Propriétés : Delimiter=_ · Texts={{DcuErrorCode; Value; 0}; {DcuErrorCode T; Value; 0}}
- Lit : `DcuErrorCode`, `DcuErrorCode T`
- Utilisé par : `Measure group: Battery BMW`
- Ligne export : 25871 · id 56136

#### BatErrorCode TF  `TFC`
- Propriétés : Delimiter=_ · Texts={{BatErrorCode; Value; 0}; {BatErrorCode T; Value; 0}}
- Lit : `BatErrorCode`, `BatErrorCode T`
- Utilisé par : `Event log: Electronic Logs`, `Measure group: Battery BMW`
- Ligne export : 25889 · id 56137

#### IsoMonErrorCode TF  `TFC`
- Propriétés : Delimiter=_ · Texts={{IsoMonErrorCode; Value; 0}; {IsoMonErrorCode T; Value; 0}}
- Lit : `IsoMonErrorCode`, `IsoMonErrorCode T`
- Utilisé par : `Measure group: Battery BMW`
- Ligne export : 25907 · id 56138

#### IsoMonState  `SP`
- Propriétés : Input channel=IsoMonState · Default state name=Reset · States={SelfCheck; RunningValueInvalid; RunningValueValid; Device Error}
- Lit : `IsoMonState`
- Utilisé par : `Iso52MonTPdo1`, `Measure group: Battery BMW`
- Ligne export : 25925 · id 56391

#### BatState  `SP`
- Propriétés : Input channel=BatState · Default state name=Reset · States={Precharging; Connected; Device Com Error; Precharge Error; Device Error; Disconnecte_Error; Disconnect}
- Lit : `BatState`
- Utilisé par : `BMW - DRIVE MODE`, `Bat51TPdo1`, `Battery State MEM`, `New Battery State`, `Event log: Electronic Logs`, `Measure group: Battery BMW`
- Ligne export : 25940 · id 57168

#### New Battery State  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `BatState <> Battery State MEM`
- Lit : ``, `BatState`, `Battery State MEM`
- Utilisé par : `Battery State MEM`, `Event log: Electronic Logs`
- Ligne export : 25958 · id 59868

#### Battery State MEM  `MEM`
- Propriétés : Input channel=BatState · Action=Replace · Store value=No
- Logique :
  - **Activating** = `PositiveFlank(New Battery State)`
- Lit : ``, `BatState`, `New Battery State`
- Utilisé par : `New Battery State`
- Ligne export : 26003 · id 59876

#### BatErrorCode Out  `GPOUT`
- Propriétés : Input value=BatErrorCode · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `BatErrorCode`
- Utilisé par : `BMW Error`
- Ligne export : 26047 · id 61760

#### DcuErrorCode Out  `GPOUT`
- Propriétés : Input value=DcuErrorCode · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `DcuErrorCode`
- Utilisé par : `BMW Error`
- Ligne export : 26059 · id 61762

#### IsoMonErrorCode Out  `GPOUT`
- Propriétés : Input value=IsoMonErrorCode · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `IsoMonErrorCode`
- Utilisé par : `BMW Error`
- Ligne export : 26071 · id 61764

#### BMW Error  `GFOUT`
- Propriétés : Identifier=0x7451240 · Data length=8 · Send method=On change · Unused bits=Set to 0 · Parameters={{BatErrorCode Out; 0}; {DcuErrorCode Out; 16}; {IsoMonErrorCode Out; 32}} · Module=Proemion (Generic) · Module index=3
- Lit : `BatErrorCode Out`, `DcuErrorCode Out`, `IsoMonErrorCode Out`
- Utilisé par : `Charger ERROR`
- Ligne export : 26083 · id 61758

## Electric / BATTERY / WattApls — actif seulement si `Is_WattAlps`

#### BMS_VMU_STATUS  `GFIN`
- Propriétés : Identifier=418382110 · Data length=DonÂt care · Timeout=200 · Paged protocol={Not used} · Parameters={{Heater Command [%]; 40}; {CoolingSystem Command [%]; 32}; {Fan Command [%]; 24}; {Pump Command [%]; 16}; {Balancing Finished; 12}; {AuxiliaryOutputState; 11}; {ImminentOpening; 10}; {End Of Charge; 9}; {BalancingRunning; 8}; {BMS State [State]; 0}} · Module=WattAlps (Generic) · Module index=0
- Lit : `AuxiliaryOutputState`, `BMS State`, `Balancing Finished`, `BalancingRunning`, `CoolingSystem Command`, `End Of Charge`, `Fan Command`, `Heater Command`, `ImminentOpening`, `Pump Command`, `State`
- Utilisé par : `WattAlps - CAN OK`
- Ligne export : 26181 · id 46653

#### Heater Command  `GPIN`
- Propriétés : Unit=% · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 26227 · id 46654

#### CoolingSystem Command  `GPIN`
- Propriétés : Unit=% · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 26239 · id 46655

#### Fan Command  `GPIN`
- Propriétés : Unit=% · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 26251 · id 46656

#### Pump Command  `GPIN`
- Propriétés : Unit=% · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 26263 · id 46657

#### Balancing Finished  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 26275 · id 46658

#### AuxiliaryOutputState  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 26287 · id 46659

#### ImminentOpening  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`, `WattAlps - DRIVE MODE`, `WattApls- ERROR DIGIT`
- Ligne export : 26299 · id 46660

#### End Of Charge  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 26311 · id 46661

#### BalancingRunning  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`
- Ligne export : 26323 · id 46662

#### BMS State  `GPIN`
- Propriétés : Unit=State · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_STATUS`, `WattAlps - DRIVE MODE`
- Ligne export : 26335 · id 46663

#### BMS_VMU_FAULTS  `GFIN`
- Propriétés : Identifier=418382366 · Data length=DonÂt care · Timeout=600 · Paged protocol={Not used} · Parameters={{Coin Low voltage; 58}; {OilLevel; 57}; {OpenCircuit; 53}; {WrongConfiguration; 56}; {CanCurrentSensorFailure; 55}; {InsulationControlerFailure; 54}; {MainPrechargeSequenceFailure; 52}; {HeatingSystemFailure; 51}; {CoolingSystemFailure; 50}; {Fan Failure; 49}; {OilPump Failure; 48}; {VMU Timeout; 47}; {InsulationMeasurementState; 45}; {InternalCurrentSensorFailure; 44}; {VoltSensorFailure; 43}; {TempSensorFailure; 42}; {ModuleLost; 41}; {InterlockOpened; 40}; {ContactorDamaged; 39}; {AUX2Contactor; 38}; {AUX1Contactor; 37}; {DCContactorMinus; 36}; {DCContactorPlus; 35}; {MainContactorPrecharge; 34}; {MainContactorMinus; 33}; {MainContactorPlus; 32}; {ShutOverVolt; 21}; {AlarmOverVolt; 20}; {WarnOverVolt; 19}; {ShutCriticalDischarge; 18}; {AlarmCriticalDischarge; 17}; {WarnCriticalDischarge; 16}; {ShutOverCurrentDisharge; 29}; {AlarmOverCurrentDisharge; 28}; {WarnOverCurrentDisharge; 27}; {ShutOverCurrentCharge; 26}; {AlarmOverCurrentCharge; 25}; {WarnOverCurrentCharge; 24}; {ShutOverTemp; 13}; {AlarmOverTemp; 12}; {WarnOverTemp; 11}; {ShutLowTemp; 10}; {AlarmLowTemp; 9}; {WarnLowTemp; 8}} · Module=WattAlps (Generic) · Module index=6
- Lit : `AUX1Contactor`, `AUX2Contactor`, `AlarmCriticalDischarge`, `AlarmLowTemp`, `AlarmOverCurrentCharge`, `AlarmOverCurrentDisharge`, `AlarmOverTemp`, `AlarmOverVolt`, `CanCurrentSensorFailure`, `Coin Low voltage`, `ContactorDamaged`, `CoolingSystemFailure`, `DCContactorMinus`, `DCContactorPlus`, `Fan Failure`, `HeatingSystemFailure`, `InsulationControlerFailure`, `InsulationMeasurementState`, `InterlockOpened`, `InternalCurrentSensorFailure`, `MainContactorMinus`, `MainContactorPlus`, `MainContactorPrecharge`, `MainPrechargeSequenceFailure`, `ModuleLost`, `OilLevel`, `OilPump Failure`, `OpenCircuit`, `ShutCriticalDischarge`, `ShutLowTemp`, `ShutOverCurrentCharge`, `ShutOverCurrentDisharge`, `ShutOverTemp`, `ShutOverVolt`, `TempSensorFailure`, `VMU Timeout`, `VoltSensorFailure`, `WarnCriticalDischarge`, `WarnLowTemp`, `WarnOverCurrentCharge`, `WarnOverCurrentDisharge`, `WarnOverTemp`, `WarnOverVolt`, `WrongConfiguration`
- Utilisé par : *(personne)*
- Ligne export : 26347 · id 46664

#### Coin Low voltage  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26495 · id 46665

#### OilLevel  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26507 · id 46666

#### OpenCircuit  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26519 · id 46667

#### WrongConfiguration  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26531 · id 46668

#### CanCurrentSensorFailure  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26543 · id 46669

#### InsulationControlerFailure  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26555 · id 46670

#### MainPrechargeSequenceFailure  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26567 · id 46671

#### HeatingSystemFailure  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26579 · id 46672

#### CoolingSystemFailure  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26591 · id 46673

#### Fan Failure  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26603 · id 46674

#### OilPump Failure  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26615 · id 46675

#### VMU Timeout  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26627 · id 46676

#### InsulationMeasurementState  `GPIN`
- Propriétés : Length=2 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26639 · id 46677

#### InternalCurrentSensorFailure  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26651 · id 46678

#### VoltSensorFailure  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26663 · id 46679

#### TempSensorFailure  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26675 · id 46680

#### ModuleLost  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26687 · id 46681

#### InterlockOpened  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26699 · id 46682

#### ContactorDamaged  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26711 · id 46683

#### AUX2Contactor  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26723 · id 46684

#### AUX1Contactor  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26735 · id 46685

#### DCContactorMinus  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26747 · id 46686

#### DCContactorPlus  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26759 · id 46687

#### MainContactorPrecharge  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26771 · id 46688

#### MainContactorMinus  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26783 · id 46689

#### MainContactorPlus  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26795 · id 46690

#### ShutOverVolt  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26807 · id 46691

#### AlarmOverVolt  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26819 · id 46692

#### WarnOverVolt  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26831 · id 46693

#### ShutCriticalDischarge  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26843 · id 46694

#### AlarmCriticalDischarge  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26855 · id 46695

#### WarnCriticalDischarge  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26867 · id 46696

#### ShutOverCurrentDisharge  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26879 · id 46697

#### AlarmOverCurrentDisharge  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26891 · id 46698

#### WarnOverCurrentDisharge  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26903 · id 46699

#### ShutOverCurrentCharge  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26915 · id 46700

#### AlarmOverCurrentCharge  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26927 · id 46701

#### WarnOverCurrentCharge  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26939 · id 46702

#### ShutOverTemp  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26951 · id 46703

#### AlarmOverTemp  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26963 · id 46704

#### WarnOverTemp  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26975 · id 46705

#### ShutLowTemp  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26987 · id 46706

#### AlarmLowTemp  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 26999 · id 46707

#### WarnLowTemp  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `BMS_VMU_FAULTS`
- Ligne export : 27011 · id 46708

#### BMS_VMU_INFO  `GFIN`
- Propriétés : Identifier=418382622 · Data length=DonÂt care · Timeout=600 · Paged protocol={Not used} · Parameters={{SOH [%]; 40}; {SOC [%]; 32}; {BatteryCurrent; 16}; {BatteryVoltageBeforeContactors [V]; 0}; {BatteryVoltageAfterContactors [V]; 48}} · Module=WattAlps (Generic) · Module index=1
- Lit : `BatteryCurrent`, `BatteryVoltageAfterContactors`, `BatteryVoltageBeforeContactors`, `SOC`, `SOH`
- Utilisé par : *(personne)*
- Ligne export : 27023 · id 46709

#### SOH  `GPIN`
- Propriétés : Unit=% · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_INFO`
- Ligne export : 27054 · id 46710

#### SOC  `GPIN`
- Propriétés : Unit=% · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_INFO`, `WattAlps - SOC`
- Ligne export : 27066 · id 46711

#### BatteryCurrent  `GPIN`
- Propriétés : Length=16 · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_INFO`, `WattAlps - CURRENT`
- Ligne export : 27078 · id 46712

#### BatteryVoltageBeforeContactors  `GPIN`
- Propriétés : Unit=V · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_INFO`, `WattAlps - Battery InstantVoltage`
- Ligne export : 27091 · id 46713

#### BMS_VMU_CHARGE  `GFIN`
- Propriétés : Identifier=418382878 · Data length=DonÂt care · Timeout=200 · Paged protocol={Not used} · Parameters={{MaxRegenerativeCurrent [A]; 16}; {MaxDischargeCurrent [A]; 0}; {ChargeVoltageSetpoint [V]; 48}; {ChargeCurrentSetpoint [A]; 32}} · Module=WattAlps (Generic) · Module index=2
- Lit : `ChargeCurrentSetpoint`, `ChargeVoltageSetpoint`, `MaxDischargeCurrent`, `MaxRegenerativeCurrent`
- Utilisé par : *(personne)*
- Ligne export : 27104 · id 46714

#### MaxRegenerativeCurrent  `GPIN`
- Propriétés : Unit=A · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_CHARGE`
- Ligne export : 27132 · id 46715

#### MaxDischargeCurrent  `GPIN`
- Propriétés : Unit=A · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_CHARGE`, `WattAlps- Max Current`
- Ligne export : 27145 · id 46716

#### ChargeVoltageSetpoint  `GPIN`
- Propriétés : Unit=V · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_CHARGE`
- Ligne export : 27158 · id 46717

#### ChargeCurrentSetpoint  `GPIN`
- Propriétés : Unit=A · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_CHARGE`
- Ligne export : 27171 · id 46718

#### BMS_VMU_TRACE  `GFIN`
- Propriétés : Identifier=418383134 · Data length=DonÂt care · Timeout=600 · Paged protocol={Not used} · Parameters={{DaisyChain Number; 0}; {BatteryAverageTemperature [Degrees]; 56}; {CurrentModule Number; 2}; {CellMinVoltage; 8}; {CellMaxVoltage; 24}; {BatteryMinTemperature [Degrees Celsius]; 40}; {BatteryMaxTemperature; 48}} · Module=WattAlps (Generic) · Module index=3
- Lit : `BatteryAverageTemperature`, `BatteryMaxTemperature`, `BatteryMinTemperature`, `CellMaxVoltage`, `CellMinVoltage`, `CurrentModule Number`, `DaisyChain Number`
- Utilisé par : *(personne)*
- Ligne export : 27184 · id 46719

#### DaisyChain Number  `GPIN`
- Propriétés : Length=2 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_TRACE`
- Ligne export : 27221 · id 46720

#### BatteryAverageTemperature  `GPIN`
- Propriétés : Unit=Degrees · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_TRACE`
- Ligne export : 27233 · id 46721

#### CurrentModule Number  `GPIN`
- Propriétés : Length=6 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_TRACE`
- Ligne export : 27245 · id 46722

#### CellMinVoltage  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_TRACE`, `WattAlps - LowCellVoltage`
- Ligne export : 27257 · id 46723

#### CellMaxVoltage  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_TRACE`, `WattAlps - HighCellVoltage`
- Ligne export : 27270 · id 46724

#### BatteryMinTemperature  `GPIN`
- Propriétés : Unit=Degrees Celsius · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_TRACE`
- Ligne export : 27283 · id 46725

#### BatteryMaxTemperature  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_VMU_TRACE`, `WattAlps - Cell_T_max_Master`
- Ligne export : 27295 · id 46726

#### REVISION  `GFIN`
- Propriétés : Identifier=418383390 · Data length=DonÂt care · Timeout=5000 · Paged protocol={Not used} · Parameters={{wrong configuration slave number [Raw]; 24}; {Hardware revision [Raw]; 16}; {Minor revision [Raw]; 8}; {Major revision [Raw]; 0}} · Module=WattAlps (Generic) · Module index=4
- Lit : `Hardware revision`, `Major revision`, `Minor revision`, `wrong configuration slave number`
- Utilisé par : *(personne)*
- Ligne export : 27307 · id 46727

#### wrong configuration slave number  `GPIN`
- Propriétés : Unit=Raw · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `REVISION`
- Ligne export : 27335 · id 46728

#### Hardware revision  `GPIN`
- Propriétés : Unit=Raw · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `REVISION`
- Ligne export : 27347 · id 46729

#### Minor revision  `GPIN`
- Propriétés : Unit=Raw · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `REVISION`
- Ligne export : 27359 · id 46730

#### Major revision  `GPIN`
- Propriétés : Unit=Raw · Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `REVISION`
- Ligne export : 27371 · id 46731

#### INSULATION_RESISTANCE  `GFIN`
- Propriétés : Identifier=418383646 · Data length=DonÂt care · Timeout=3000 · Paged protocol={Not used} · Parameters={{ValueOfInsulationResistance [kohm]; 0}} · Module=WattAlps (Generic) · Module index=5
- Lit : `ValueOfInsulationResistance`
- Utilisé par : *(personne)*
- Ligne export : 27383 · id 46732

#### ValueOfInsulationResistance  `GPIN`
- Propriétés : Unit=kohm · Length=32 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `INSULATION_RESISTANCE`, `WattAlps - Iso_Resist`
- Ligne export : 27402 · id 46733

#### WattAlps - Battery InstantVoltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `0,1 * BatteryVoltageBeforeContactors [V]`
- Lit : ``, `BatteryVoltageBeforeContactors`
- Utilisé par : `Battery InstantVoltage`
- Ligne export : 27415 · id 46734

#### WattAlps - SOC  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(SOC [%]: 10->0, 95->100, Freeze)`
- Lit : ``, `SOC`
- Utilisé par : `Battery SOC`
- Ligne export : 27459 · id 46742

#### WattAlps - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `0,1 * BatteryCurrent`
- Lit : ``, `BatteryCurrent`
- Utilisé par : `Current Bat`
- Ligne export : 27506 · id 46750

#### WattAlps - Cell_T_max_Master  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `BatteryMaxTemperature - 40`
- Lit : ``, `BatteryMaxTemperature`
- Utilisé par : `Cell_T_max_Master`
- Ligne export : 27550 · id 46758

#### WattApls- ERROR DIGIT  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=100
- Logique :
  - **Activating** = `ImminentOpening`
- Lit : ``, `ImminentOpening`
- Utilisé par : `Battery ERROR DIGIT`
- Ligne export : 27594 · id 46766

#### WattAlps - Iso_Resist  `MAC`
- Propriétés : Unit=kOhm · Limiting object group=Signed
- Logique :
  - **Controlling** = `ValueOfInsulationResistance [kohm] * 1`
- Lit : ``, `ValueOfInsulationResistance`
- Utilisé par : `BMS_Iso_Resist`
- Ligne export : 27637 · id 46774

#### WattAlps - DRIVE MODE  `IDC`
> Kreisel 
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `2 = BMS State [State]`
  - **Blocking** = `ImminentOpening`
- Lit : ``, `BMS State`, `ImminentOpening`
- Utilisé par : `Battery DRIVE MODE`
- Ligne export : 27681 · id 46782

#### WattAlps - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `BMS_VMU_STATUS`
- Lit : ``, `BMS_VMU_STATUS`
- Utilisé par : `Battery CAN OK`
- Ligne export : 27733 · id 46791

#### BatteryVoltageAfterContactors  `GPIN`
- Propriétés : Unit=V · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_VMU_INFO`, `WattAlps- U_Trac`
- Ligne export : 27776 · id 46799

#### WattAlps- U_Trac  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `0,1 * BatteryVoltageAfterContactors [V]`
- Lit : ``, `BatteryVoltageAfterContactors`
- Utilisé par : `BMS_U_Trac`
- Ligne export : 27789 · id 46800

#### WattAlps - LowCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed
- Logique :
  - **Controlling** = `CellMinVoltage`
- Lit : ``, `CellMinVoltage`
- Utilisé par : `LowCellVoltage`
- Ligne export : 27833 · id 46808

#### WattAlps - HighCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed
- Logique :
  - **Controlling** = `CellMaxVoltage`
- Lit : ``, `CellMaxVoltage`
- Utilisé par : `HighCellVoltage`
- Ligne export : 27875 · id 46816

#### Switch Battery  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Main Switch Battery`
- Lit : ``, `Main Switch Battery`
- Utilisé par : `Request Parameter State`
- Ligne export : 27917 · id 46824

#### Request Parameter State  `SMC`
- Propriétés : Default state name=Standby
- Fonction *Charge* :
  - **Activating** = `(Charger CHARGING) AND (Switch Battery)`
- Fonction *Drive* :
  - **Activating** = `Switch Battery`
  - **Blocking** = `Charger CHARGING`
- Lit : ``, `Charger CHARGING`, `Switch Battery`
- Utilisé par : `Request Parameter`
- Ligne export : 27960 · id 46832

#### Request Parameter  `IP`
- Propriétés : Mode selector=Request Parameter State · Default mode: Standby={0} · Mode 1: Charge={1} · Mode 2: Drive={2}
- Lit : `Request Parameter State`
- Utilisé par : `UBMSModeRequestBMS`
- Ligne export : 28045 · id 46846

#### UBMSModeRequestBMS  `GPOUT`
- Propriétés : Input value=Request Parameter · Length=3 · Type=Unsigned integer
- Lit : `Request Parameter`
- Utilisé par : `VMU_BMS_INFO`
- Ligne export : 28061 · id 46847

#### VMU_BMS_INFO  `GFOUT`
- Propriétés : Identifier=402726400 · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Parameters={{UBMSModeRequestBMS; 0}} · Module=WattAlps (Generic) · Module index=0
- Lit : `UBMSModeRequestBMS`
- Utilisé par : *(personne)*
- Ligne export : 28072 · id 46848

#### WattAlps- Max Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxDischargeCurrent [A]`
- Lit : ``, `MaxDischargeCurrent`
- Utilisé par : `Max Discharge`
- Ligne export : 28091 · id 46849

## Electric / CHARGER

#### Charger Brand  `SP`
- Propriétés : Input channel=None · Default state name=BMW · States={Brusa; Elcon}
- Utilisé par : `Charger Output Current`, `Is_Charger_BMW`, `Is_Charger_Brusa`, `Is_Charger_Elcon`, `Adjust group: Master Config`, `Single adjust item: Charger Brand`
- Ligne export : 30093 · id 47382

#### Is_Charger_Elcon  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Charger Brand = 2`
- Lit : ``, `Charger Brand`
- Utilisé par : `Active le groupe: Electric / CHARGER / Elcon`, `Measure group: Charger Elcon`
- Ligne export : 30106 · id 53846

#### Charger CONNECT to 220V  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(BMW Connected) OR (Elcon Connected) OR (Brusa Connected)`
- Lit : ``, `BMW Connected`, `Brusa Connected`, `Elcon Connected`
- Utilisé par : `Charger Connected`, `Charger State Finite`, `Reset State`
- Ligne export : 30151 · id 47238

#### Charger READY  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `(BMW Ready) OR (Elcon Ready) OR (Brusa ready)`
- Lit : ``, `BMW Ready`, `Brusa ready`, `Elcon Ready`
- Utilisé par : `Battery not need to charge`, `Charger State Finite`
- Ligne export : 30208 · id 47258

#### Charger CHARGING  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `(BMW Charging) OR (Elcon Charging) OR (Brusa Charging)`
- Lit : ``, `BMW Charging`, `Brusa Charging`, `Elcon Charging`
- Utilisé par : `Charge Mode`, `Charger Charging`, `Charger STATE`, `Charger State Finite`, `Global Auto Off Timer`, `Request Parameter State`
- Ligne export : 30265 · id 47268

#### Charger ERROR  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=100
- Logique :
  - **Activating** = `(BMW Error) OR (Elcon Error) OR (Brusa Error)`
- Lit : ``, `BMW Error`, `Brusa Error`, `Elcon Error`
- Utilisé par : `Charger STATE`, `Reset State`
- Ligne export : 30322 · id 47248

#### Reset State  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(NegativeFlank(Charger CONNECT to 220V)) OR (PositiveFlank(Charger ERROR))`
- Lit : ``, `Charger CONNECT to 220V`, `Charger ERROR`
- Utilisé par : `Charger State Finite`
- Ligne export : 30379 · id 47278

#### Charger State Finite  `FSM`
- Propriétés : Store value=No · Resetting channel=Reset State
- État 0 **OFF**
  - transition *Connected to 220 V* (état cible non exporté par IQANdesign)
    - **Activating** = `Charger CONNECT to 220V`
- État 1 **Connected**
  - transition *Battery need to charge* (état cible non exporté par IQANdesign)
    - **Activating** = `(Charger READY) AND (Battery NEED TO CHARGE)`
  - transition *Battery not need to charge* (état cible non exporté par IQANdesign)
    - **Activating** = `Battery not need to charge`
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
- Lit : ``, `Battery CHARGED`, `Battery DRIVE MODE`, `Battery NEED TO CHARGE`, `Battery not need to charge`, `Charger CHARGING`, `Charger CONNECT to 220V`, `Charger READY`, `MD4 - Start Button Blocking Neutral`, `Reset State`
- Utilisé par : `Battery not need to charge`, `Battery start by charger`, `Charger DIGITAL CMD`, `System Shutdown`
- Ligne export : 30431 · id 47287

#### Battery not need to charge  `IDC`
- Propriétés : Toggle=No · Delay on=60000 · Delay off=0
- Logique :
  - **Activating** = `(not((Charger READY and Battery NEED TO CHARGE))) AND (Charger State Finite = 1)`
- Lit : ``, `Battery NEED TO CHARGE`, `C`, `Charger READY`, `Charger State Finite`
- Utilisé par : `Charger State Finite`
- Ligne export : 30681 · id 60237

#### Charger DIGITAL CMD  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Charger State Finite = 3) OR (Charger State Finite = 4)`
  - **Blocking** = `(not(Battery DRIVE MODE)) OR (Power Down)`
- Lit : ``, `Battery DRIVE MODE`, `Charger State Finite`, `Power Down`
- Utilisé par : `CMD`, `CMD`, `Timer charging`
- Ligne export : 30757 · id 47333

#### Desired Voltage  `IP`
- Propriétés : Unit=V · Mode selector=Battery Brand · Default mode: BMW={390} · Mode 1: WattAlps={390}
- Lit : `Battery Brand`
- Utilisé par : `1560 - Desired Voltage`, `Charger end charge`, `HV Current`, `Math Voltage`, `Math Voltage`, `Adjust group: Master Charger`, `Single adjust item: Desired Voltage`
- Ligne export : 30826 · id 47342

#### Max Current Line  `IP`
- Propriétés : Unit=A · Default mode={10}
- Utilisé par : `1560 - Max Current from 230 V`, `HV Current`, `Adjust group: Master Charger`, `Adjust group: Setup Charger`, `Single adjust item: Max Current Line`
- Ligne export : 30840 · id 47237

#### Input Voltage  `SP`
- Propriétés : Input channel=None · Default state name=230 V · States={110 V}
- Utilisé par : `Input Voltage Value`, `Adjust group: Master Charger`, `Adjust group: Setup Charger`, `Measure group: Charger Elcon`, `Single adjust item: Input Voltage`
- Ligne export : 30852 · id 47394

#### Input Voltage Value  `IP`
- Propriétés : Unit=V · Mode selector=Input Voltage · Default mode: 230 V={230} · Mode 1: 110 V={110}
- Lit : `Input Voltage`
- Utilisé par : `HV Current`, `Adjust group: Master Charger`, `Single adjust item: Input Voltage Value`
- Ligne export : 30864 · id 47396

#### HV Current  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result := MinOf(Input Voltage Value  * Max Current Line / Desired Voltage, 10)
  ```
- Lit : `Desired Voltage`, `Input Voltage Value`, `Max Current Line`
- Utilisé par : `1560 - Desired Current`, `Math Current`, `Math Current`
- Ligne export : 30878 · id 47397

#### Charger CAN BUS OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(BMW CAN OK) OR (Elcon CAN OK) OR (Brusa CAN OK)`
- Lit : ``, `BMW CAN OK`, `Brusa CAN OK`, `Elcon CAN OK`
- Utilisé par : `Charger STATE`, `Measure group: CanBus`
- Ligne export : 31588 · id 47343

#### Charger STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *READY* :
  - **Activating** = `Charger CAN BUS OK`
  - **Blocking** = `(Charger ERROR) OR (Charger CHARGING)`
- Fonction *CHARGING* :
  - **Activating** = `Charger CHARGING`
  - **Blocking** = `Charger ERROR`
- Lit : ``, `Charger CAN BUS OK`, `Charger CHARGING`, `Charger ERROR`
- Utilisé par : `VIEW BAT Charging`, `VIEW BAT Ready`, `VIEW BAT Run`
- Ligne export : 31645 · id 47353

#### Battery start by charger  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Charger State Finite = 2) OR (Charger State Finite = 3) OR (Charger State Finite = 4)`
- Lit : ``, `Charger State Finite`
- Utilisé par : `Battery CMD`
- Ligne export : 31737 · id 47372

#### Charger Output Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=Charger Brand
- Fonction *BMW* :
  - **Controlling** = `BMW - Output current [A]`
- Fonction *Brusa* :
  - **Controlling** = `1553 - Actual mains current [A]`
- Fonction *Elcon* :
  - **Controlling** = `Elcon - output current`
- Lit : ``, `1553 - Actual mains current`, `BMW - Output current`, `Charger Brand`, `Elcon - output current`
- Utilisé par : `Charger end charge`
- Ligne export : 31800 · id 47711

#### Is_Charger_BMW  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Charger Brand = 0`
- Lit : ``, `Charger Brand`
- Utilisé par : `Active le groupe: Electric / CHARGER / BMW`, `Measure group: Charger BMW`
- Ligne export : 31904 · id 47739

#### Is_Charger_Brusa  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Charger Brand = 1`
- Lit : ``, `Charger Brand`
- Utilisé par : `Active le groupe: Electric / CHARGER / Brusa`, `Measure group: Charger Brusa`
- Ligne export : 32765 · id 47918

#### Charger end charge  `IDC`
- Propriétés : Toggle=No · Delay on=3600000 · Delay off=0
- Logique :
  - **Activating** = `((Abs(Charger Output Current [A])) <= 0,5) OR ((Desired Voltage [V] - Battery InstantVoltage [V]) < 2)`
- Lit : ``, `Battery InstantVoltage`, `C`, `Charger Output Current`, `Desired Voltage`
- Utilisé par : `Battery CHARGED`
- Ligne export : 34044 · id 62761

## Electric / CHARGER / BMW — actif seulement si `Is_Charger_BMW`

#### GFIN-A:Generic  `GFIN`
- Propriétés : Identifier=0x405 · Data length=DonÂt care · Timeout=200 · Paged protocol={Not used} · Parameters={{CHARGER_STATUS; 0}; {CHARGER_MAINS_CURRENT; 8}; {CHARGER_DC_CURRENT; 24}; {CHARGER_DC_VOLTAGE; 40}; {CHARGER_MAINS_FREQUENCY; 56}} · Module=Charger BMW (Generic) · Module index=0
- Lit : `CHARGER_DC_CURRENT`, `CHARGER_DC_VOLTAGE`, `CHARGER_MAINS_CURRENT`, `CHARGER_MAINS_FREQUENCY`, `CHARGER_STATUS`
- Utilisé par : `BMW Ready`
- Ligne export : 31970 · id 47748

#### CHARGER_STATUS  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Digital
- Utilisé par : `BMW - Status`, `GFIN-A:Generic`
- Ligne export : 32001 · id 47749

#### CHARGER_MAINS_CURRENT  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - Main current`, `GFIN-A:Generic`
- Ligne export : 32012 · id 47750

#### CHARGER_DC_CURRENT  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - Output current`, `GFIN-A:Generic`
- Ligne export : 32025 · id 47751

#### CHARGER_DC_VOLTAGE  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - Output Voltage`, `GFIN-A:Generic`
- Ligne export : 32038 · id 47752

#### CHARGER_MAINS_FREQUENCY  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `BMW - Frequency`, `GFIN-A:Generic`
- Ligne export : 32051 · id 47753

#### BMW - Main current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_MAINS_CURRENT / 10`
- Lit : ``, `CHARGER_MAINS_CURRENT`
- Utilisé par : `BMW Charging`, `Measure group: Charger BMW`
- Ligne export : 32063 · id 47754

#### BMW - Output current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_DC_CURRENT / 10`
- Lit : ``, `CHARGER_DC_CURRENT`
- Utilisé par : `Charger Output Current`, `Measure group: Charger BMW`
- Ligne export : 32107 · id 47762

#### BMW - Output Voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_DC_VOLTAGE / 10`
- Lit : ``, `CHARGER_DC_VOLTAGE`
- Utilisé par : `Measure group: Charger BMW`
- Ligne export : 32151 · id 47770

#### BMW - Frequency  `MAC`
- Propriétés : Unit=Hz · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_MAINS_FREQUENCY`
- Lit : ``, `CHARGER_MAINS_FREQUENCY`
- Utilisé par : `Measure group: Charger BMW`
- Ligne export : 32195 · id 47778

#### BMW Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `GFIN-A:Generic`
- Lit : ``, `GFIN-A:Generic`
- Utilisé par : `BMW CAN OK`, `BMW Connected`, `Charger READY`, `Measure group: Charger BMW`
- Ligne export : 32237 · id 47786

#### BMW Connected  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `BMW Ready`
- Lit : ``, `BMW Ready`
- Utilisé par : `Charger CONNECT to 220V`
- Ligne export : 32280 · id 47794

#### BMW Charging  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `BMW - Main current [A] > 0,5`
- Lit : ``, `BMW - Main current`
- Utilisé par : `Charger CHARGING`
- Ligne export : 32323 · id 47802

#### BMW CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `BMW Ready`
- Lit : ``, `BMW Ready`
- Utilisé par : `Battery CAN OK`, `Charger CAN BUS OK`, `Measure group: Battery BMW`
- Ligne export : 32368 · id 47810

#### BMW - Status  `MAC`
- Propriétés : Unit=State · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_STATUS`
- Lit : ``, `CHARGER_STATUS`
- Utilisé par : `BMW Error`, `Measure group: Charger BMW`
- Ligne export : 32411 · id 47818

#### BMW Error  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `3 <= BMW - Status [State]`
- Lit : ``, `BMW - Status`
- Utilisé par : `Charger ERROR`
- Ligne export : 32453 · id 47826

#### CMD  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Charger DIGITAL CMD`
- Lit : ``, `Charger DIGITAL CMD`
- Utilisé par : `ENABLE`
- Ligne export : 32498 · id 47834

#### ENABLE  `GPOUT`
- Propriétés : Input value=CMD · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `CMD`
- Utilisé par : `GFOUT-A:Generic`, `Power`
- Ligne export : 32541 · id 47842

#### Power  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(ENABLE * 100) * 10`
- Lit : ``, `ENABLE`
- Utilisé par : `POWER_REFERENCE`
- Ligne export : 32552 · id 47843

#### POWER_REFERENCE  `GPOUT`
- Propriétés : Input value=Power · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Power`
- Utilisé par : `GFOUT-A:Generic`
- Ligne export : 32612 · id 47853

#### Math Voltage  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Desired Voltage [V] * 10`
- Lit : ``, `Desired Voltage`
- Utilisé par : `MAXDCVOLTLIMIT`
- Ligne export : 32624 · id 47854

#### MAXDCVOLTLIMIT  `GPOUT`
- Propriétés : Input value=Math Voltage · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Math Voltage`
- Utilisé par : `GFOUT-A:Generic`
- Ligne export : 32668 · id 47862

#### Math Current  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `HV Current [A] * 10`
- Lit : ``, `HV Current`
- Utilisé par : `MAXDCCURRLIMIT`
- Ligne export : 32680 · id 47863

#### MAXDCCURRLIMIT  `GPOUT`
- Propriétés : Input value=Math Current · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Math Current`
- Utilisé par : `GFOUT-A:Generic`
- Ligne export : 32724 · id 47871

#### GFOUT-A:Generic  `GFOUT`
- Propriétés : Identifier=0x400 · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Parameters={{ENABLE; 0}; {POWER_REFERENCE; 8}; {MAXDCVOLTLIMIT; 24}; {MAXDCCURRLIMIT; 40}} · Module=Charger BMW (Generic) · Module index=0
- Lit : `ENABLE`, `MAXDCCURRLIMIT`, `MAXDCVOLTLIMIT`, `POWER_REFERENCE`
- Utilisé par : *(personne)*
- Ligne export : 32736 · id 47872

## Electric / CHARGER / Brusa — actif seulement si `Is_Charger_Brusa`

#### 1552 - CAN IN  `GFIN`
- Propriétés : Identifier=1552 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{1552 - Hardware enable - Byte; 7}; {1552 - Error detect - Byte; 6}; {1552 - Warning Condition - Byte; 5}; {1552 - Automatique charging - Byte; 24}} · Module=Chargeur Brusa (Generic) · Module index=1
- Lit : `1552 - Automatique charging - Byte`, `1552 - Error detect - Byte`, `1552 - Hardware enable - Byte`, `1552 - Warning Condition - Byte`
- Utilisé par : `Brusa CAN OK`
- Ligne export : 32831 · id 61971

#### 1553 - CAN IN  `GFIN`
- Propriétés : Identifier=1553 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{1553 - Actual mains current - Byte; 0}; {1553 - Actual mains voltage - Byte; 16}; {1553 - Actual battery output voltage - Byte; 32}; {1553 - output current to the battery - Byte; 48}} · Module=Chargeur Brusa (Generic) · Module index=2
- Lit : `1553 - Actual battery output voltage - Byte`, `1553 - Actual mains current - Byte`, `1553 - Actual mains voltage - Byte`, `1553 - output current to the battery - Byte`
- Utilisé par : *(personne)*
- Ligne export : 32859 · id 61972

#### 1553 - Actual mains current - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1553 - Actual mains current`, `1553 - CAN IN`
- Ligne export : 32887 · id 61973

#### 1553 - Actual mains voltage - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1553 - Actual mains voltage`, `1553 - CAN IN`
- Ligne export : 32900 · id 61974

#### 1555 - CAN IN  `GFIN`
- Propriétés : Identifier=1555 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{1555 - Power stage temperature - Byte; 0}} · Module=Chargeur Brusa (Generic) · Module index=0
- Lit : `1555 - Power stage temperature - Byte`
- Utilisé par : *(personne)*
- Ligne export : 32913 · id 61975

#### 1555 - Power stage temperature - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1555 - CAN IN`, `1555 - Power stage temperature - Byte`, `Measure group: Charger Brusa`
- Ligne export : 32932 · id 61976

#### 1553 - output current to the battery - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1553 - CAN IN`, `1553 - output current to the battery`
- Ligne export : 32945 · id 61977

#### 1553 - output current to the battery  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `1553 - output current to the battery - Byte / 100`
- Lit : ``, `1553 - output current to the battery - Byte`
- Utilisé par : `Brusa Charging`, `Measure group: Charger Brusa`
- Ligne export : 32958 · id 61978

#### 1553 - Actual battery output voltage - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1553 - Actual battery output voltage`, `1553 - CAN IN`
- Ligne export : 33002 · id 61986

#### 1553 - Actual battery output voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `1553 - Actual battery output voltage - Byte / 10`
- Lit : ``, `1553 - Actual battery output voltage - Byte`
- Utilisé par : `Measure group: Charger Brusa`
- Ligne export : 33015 · id 61987

#### 1552 - Error detect - Byte  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `1552 - CAN IN`, `Brusa Error`, `Measure group: Charger Brusa`
- Ligne export : 33059 · id 61995

#### 1552 - Hardware enable - Byte  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `1552 - CAN IN`, `1552 - Hardware enable - IDC`, `Measure group: Charger Brusa`
- Ligne export : 33070 · id 61996

#### Timer charging  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `(Charger DIGITAL CMD) AND (Timer charging [ms] < 4000)`
  - **Resetting** = `not(Charger DIGITAL CMD)`
- Lit : ``, `Charger DIGITAL CMD`
- Utilisé par : `Charge start state`
- Ligne export : 33081 · id 61997

#### Charge start state  `SMC`
- Propriétés : Default state name=STOP
- Fonction *Clear ERROR* :
  - **Activating** = `Inside(Timer charging [ms], 1000, 2000)`
- Fonction *Charging* :
  - **Activating** = `Timer charging [ms] > 2100`
- Lit : ``, `Timer charging`
- Utilisé par : `1560 - Desired Current`, `1560 - Desired Voltage`, `1560 - Max Current from 230 V`, `Error clear`, `Power`
- Ligne export : 33150 · id 62009

#### 1560 - Max Current from 230 V  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Charge start state
- Fonction *STOP* : (vide)
- Fonction *Clear ERROR* : (vide)
- Fonction *Charging* :
  - **Controlling** = `Max Current Line [A] * 10`
- Lit : ``, `Charge start state`, `Max Current Line`
- Utilisé par : `1560 - Max Current from 230 V - Byte`
- Ligne export : 33226 · id 62021

#### 1560 - Max Current from 230 V - Byte  `GPOUT`
- Propriétés : Input value=1560 - Max Current from 230 V · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `1560 - Max Current from 230 V`
- Utilisé par : `1560 - Cmd`
- Ligne export : 33318 · id 62041

#### 1560 - Desired Voltage  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Charge start state
- Fonction *STOP* : (vide)
- Fonction *Clear ERROR* : (vide)
- Fonction *Charging* :
  - **Controlling** = `Desired Voltage [V] * 10`
- Lit : ``, `Charge start state`, `Desired Voltage`
- Utilisé par : `1560 - Desired Voltage - Byte`
- Ligne export : 33330 · id 62042

#### 1560 - Desired Voltage - Byte  `GPOUT`
- Propriétés : Input value=1560 - Desired Voltage · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `1560 - Desired Voltage`
- Utilisé par : `1560 - Cmd`
- Ligne export : 33422 · id 62062

#### 1560 - Desired Current  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Charge start state
- Fonction *STOP* : (vide)
- Fonction *Clear ERROR* : (vide)
- Fonction *Charging* :
  - **Controlling** = `HV Current [A] * 10`
- Lit : ``, `Charge start state`, `HV Current`
- Utilisé par : `1560 - Desired Current - Byte`
- Ligne export : 33434 · id 62063

#### 1560 - Desired Current - Byte  `GPOUT`
- Propriétés : Input value=1560 - Desired Current · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `1560 - Desired Current`
- Utilisé par : `1560 - Cmd`
- Ligne export : 33526 · id 62083

#### Power  `DP`
- Propriétés : Mode selector=Charge start state · Default mode: STOP={False} · Mode 1: Clear ERROR={False} · Mode 2: Charging={True}
- Lit : `Charge start state`
- Utilisé par : `1560 - POWER ON - Byte`
- Ligne export : 33538 · id 62084

#### 1560 - POWER ON - Byte  `JPOUT`
- Propriétés : Input value=Power · Length=1 bit · Resolution=1 · Offset=0
- Lit : `Power`
- Utilisé par : `1560 - Cmd`
- Ligne export : 33555 · id 62085

#### Error clear  `DP`
- Propriétés : Mode selector=Charge start state · Default mode: STOP={False} · Mode 1: Clear ERROR={True} · Mode 2: Charging={False}
- Lit : `Charge start state`
- Utilisé par : `1560 - Cycle Value - Byte`
- Ligne export : 33567 · id 62086

#### 1560 - Cycle Value - Byte  `JPOUT`
- Propriétés : Input value=Error clear · Length=1 bit · Resolution=1 · Offset=0
- Lit : `Error clear`
- Utilisé par : `1560 - Cmd`
- Ligne export : 33584 · id 62087

#### 1560 - Cmd  `GFOUT`
- Propriétés : Identifier=1560 · Data length=7 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={{1560 - POWER ON - Byte [bits]; 7}; {1560 - Cycle Value - Byte [bits]; 6}; {1560 - Max Current from 230 V - Byte; 8}; {1560 - Desired Voltage - Byte; 24}; {1560 - Desired Current - Byte; 40}} · Module=Chargeur Brusa (Generic) · Module index=0
- Lit : `1560 - Cycle Value - Byte`, `1560 - Desired Current - Byte`, `1560 - Desired Voltage - Byte`, `1560 - Max Current from 230 V - Byte`, `1560 - POWER ON - Byte`
- Utilisé par : *(personne)*
- Ligne export : 33596 · id 62088

#### 1552 - Warning Condition - Byte  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `1552 - CAN IN`, `Measure group: Charger Brusa`
- Ligne export : 33627 · id 62089

#### 1552 - Automatique charging - Byte  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `1552 - CAN IN`, `Measure group: Charger Brusa`
- Ligne export : 33638 · id 62090

#### 1553 - Actual mains current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `1553 - Actual mains current - Byte / 100`
- Lit : ``, `1553 - Actual mains current - Byte`
- Utilisé par : `Charger Output Current`, `Measure group: Charger Brusa`
- Ligne export : 33649 · id 62091

#### 1553 - Actual mains voltage  `MAC`
- Propriétés : Unit=V AC · Limiting object group=Signed
- Logique :
  - **Controlling** = `1553 - Actual mains voltage - Byte / 10`
- Lit : ``, `1553 - Actual mains voltage - Byte`
- Utilisé par : `Brusa Connected`, `Measure group: Charger Brusa`
- Ligne export : 33693 · id 62099

#### 1555 - Power stage temperature - Byte  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `1555 - Power stage temperature - Byte / 10`
- Lit : ``, `1555 - Power stage temperature - Byte`
- Utilisé par : `1555 - CAN IN`, `Measure group: Charger Brusa`
- Ligne export : 33737 · id 62107

#### 1552 - Hardware enable - IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `1552 - Hardware enable - Byte`
- Lit : ``, `1552 - Hardware enable - Byte`
- Utilisé par : `Brusa ready`
- Ligne export : 33781 · id 62115

#### Brusa Connected  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `1553 - Actual mains voltage [V AC] >= 90`
- Lit : ``, `1553 - Actual mains voltage`
- Utilisé par : `Charger CONNECT to 220V`
- Ligne export : 33824 · id 62123

#### Brusa Charging  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `1553 - output current to the battery [A] > 0,5`
- Lit : ``, `1553 - output current to the battery`
- Utilisé par : `Charger CHARGING`
- Ligne export : 33869 · id 62131

#### Brusa CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `1552 - CAN IN`
- Lit : ``, `1552 - CAN IN`
- Utilisé par : `Charger CAN BUS OK`
- Ligne export : 33914 · id 62139

#### Brusa Error  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `1552 - Error detect - Byte`
- Lit : ``, `1552 - Error detect - Byte`
- Utilisé par : `Charger ERROR`
- Ligne export : 33957 · id 62147

#### Brusa ready  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `1552 - Hardware enable - IDC`
- Lit : ``, `1552 - Hardware enable - IDC`
- Utilisé par : `Charger READY`
- Ligne export : 34000 · id 62155

## Electric / CHARGER / Elcon — actif seulement si `Is_Charger_Elcon`

#### ELCON-IN  `GFIN`
- Propriétés : Identifier=0x18FF50E5 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Output Voltage; 0}; {Output Current; 16}; {Hardware Failure; 32}; {Temperature od charger; 33}; {Input Voltage; 34}; {Stating State; 35}; {Communication State; 36}} · Module=Elcon (Generic) · Module index=0
- Lit : `Communication State`, `Hardware Failure`, `Input Voltage`, `Output Current`, `Output Voltage`, `Stating State`, `Temperature od charger`
- Utilisé par : `Elcon Ready`
- Ligne export : 30917 · id 53702

#### Input Voltage  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Adjust group: Master Charger`, `Adjust group: Setup Charger`, `Measure group: Charger Elcon`, `Single adjust item: Input Voltage`
- Ligne export : 30954 · id 53703

#### Hardware Failure  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Elcon Error`
- Ligne export : 30966 · id 53720

#### Elcon Error  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `Hardware Failure`
- Lit : ``, `Hardware Failure`
- Utilisé par : `Charger ERROR`, `Elcon Ready`, `Measure group: Charger Elcon`
- Ligne export : 30978 · id 53797

#### Elcon Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `ELCON-IN`
  - **Blocking** = `Elcon Error`
- Lit : ``, `ELCON-IN`, `Elcon Error`
- Utilisé par : `Charger READY`, `Elcon CAN OK`, `Elcon Connected`, `Measure group: Charger Elcon`
- Ligne export : 31021 · id 53704

#### Elcon Connected  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `Elcon Ready`
- Lit : ``, `Elcon Ready`
- Utilisé par : `Charger CONNECT to 220V`, `Measure group: Charger Elcon`
- Ligne export : 31071 · id 53712

#### Output Current  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `ELCON-IN`, `Elcon - output current`
- Ligne export : 31114 · id 53721

#### Elcon - output current  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Output Current / 10`
- Lit : ``, `Output Current`
- Utilisé par : `Charger Output Current`, `Elcon Charging`, `Measure group: Charger Elcon`
- Ligne export : 31127 · id 53722

#### Output Voltage  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `ELCON-IN`, `Elcon - output Voltage`
- Ligne export : 31171 · id 53730

#### Math Voltage  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Desired Voltage [V] * 10`
- Lit : ``, `Desired Voltage`
- Utilisé par : `Max Voltage`
- Ligne export : 31184 · id 53732

#### Max Voltage  `GPOUT`
- Propriétés : Input value=Math Voltage · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `Math Voltage`
- Utilisé par : `ELCON-OUT`
- Ligne export : 31228 · id 53740

#### Math Current  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `HV Current [A] * 10`
- Lit : ``, `HV Current`
- Utilisé par : `Max Curent`
- Ligne export : 31240 · id 53742

#### Max Curent  `GPOUT`
- Propriétés : Input value=Math Current · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `Math Current`
- Utilisé par : `ELCON-OUT`
- Ligne export : 31284 · id 53750

#### CMD  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Charger DIGITAL CMD)`
- Lit : ``, `Charger DIGITAL CMD`
- Utilisé par : `Control`
- Ligne export : 31296 · id 53752

#### Control  `GPOUT`
- Propriétés : Input value=CMD · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `CMD`
- Utilisé par : `ELCON-OUT`, `TSC1-A:J1939-0`
- Ligne export : 31340 · id 53760

#### ELCON-OUT  `GFOUT`
- Propriétés : Identifier=0x1806E5F4 · Data length=8 · Send method=Continuously · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{Max Voltage; 0}; {Max Curent; 16}; {Control; 32}} · Module=Elcon (Generic) · Module index=0
- Lit : `Control`, `Max Curent`, `Max Voltage`
- Utilisé par : *(personne)*
- Ligne export : 31351 · id 53761

#### Temperature od charger  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Temperature od charger`, `Measure group: Charger Elcon`
- Ligne export : 31376 · id 53762

#### Stating State  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Measure group: Charger Elcon`
- Ligne export : 31388 · id 53763

#### Communication State  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Measure group: Charger Elcon`
- Ligne export : 31400 · id 53764

#### Temperature od charger  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Temperature od charger`
- Lit : ``, `Temperature od charger`
- Utilisé par : `ELCON-IN`, `Measure group: Charger Elcon`
- Ligne export : 31412 · id 53765

#### Elcon - output Voltage  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Output Voltage / 10`
- Lit : ``, `Output Voltage`
- Utilisé par : `Measure group: Charger Elcon`
- Ligne export : 31455 · id 53773

#### Elcon Charging  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `Elcon - output current > 0,25`
- Lit : ``, `Elcon - output current`
- Utilisé par : `Charger CHARGING`, `Measure group: Charger Elcon`
- Ligne export : 31499 · id 53781

#### Elcon CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `Elcon Ready`
- Lit : ``, `Elcon Ready`
- Utilisé par : `Charger CAN BUS OK`, `Measure group: Charger Elcon`
- Ligne export : 31544 · id 53789

## Electric / MOTORS

#### Engine - Force Ready  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Engines Ready`, `Adjust group: Master Features`, `Single adjust item: Engine - Force Ready`
- Ligne export : 46483 · id 49165

#### Engines Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result := (M-Tracks.M1 - Ready and M-Tracks.M2 - Ready and M-Hydrau.M3 - Ready) or Engine - Force Ready
  ```
- Lit : `Engine - Force Ready`, `M`
- Utilisé par : `Electric Engine STATE`, `Engines Not Ready`, `System Started`
- Ligne export : 46496 · id 49190

#### Electric Engine STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *STARTING* :
  - **Activating** = `VARIATOR ON`
  - **Blocking** = `Engines Ready`
- Fonction *READY* :
  - **Activating** = `(Engines Ready) AND (VARIATOR ON)`
- Lit : ``, `Engines Ready`, `VARIATOR ON`
- Utilisé par : `Power State Int`
- Ligne export : 46516 · id 49166

#### Engines Not Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Engines Ready)`
- Lit : ``, `Engines Ready`
- Utilisé par : *(personne)*
- Ligne export : 46601 · id 49199

#### M-Track - Brand Main  `SP`
- Propriétés : Input channel=None · Default state name=Sevcon · States={Zapi}
- Utilisé par : `M-Track - Brand`, `Adjust group: Master Config`, `Single adjust item: M-Track - Brand Main`
- Ligne export : 46645 · id 60500

#### ZAPI Node  `SP`
- Propriétés : Input channel=None · Default state name=8-10 · States={1-4; 4-8}
- Utilisé par : `Node_ID`, `Node_ID`, `Adjust group: Master Config`, `Single adjust item: ZAPI Node`
- Ligne export : 46657 · id 62721

## Electric / MOTORS / Cooling

#### NEED FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(M1 - NEED TO FAN) OR (M2 - NEED TO FAN) OR (M3 - NEED TO FAN)`
- Lit : ``, `M1 - NEED TO FAN`, `M2 - NEED TO FAN`, `M3 - NEED TO FAN`
- Utilisé par : `Timer Fan`
- Ligne export : 46060 · id 49083

#### Timer Fan  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `NEED FAN`
  - **Resetting** = `(not(NEED FAN)) OR (Timer Fan [min] > 10)`
- Lit : ``, `NEED FAN`
- Utilisé par : `FAN OUT`
- Ligne export : 46117 · id 49093

#### FAN MODE  `SP`
- Propriétés : Input channel=None · Default state name=AUTO · States={OFF; FORCE ON}
- Utilisé par : `FAN OUT`, `Adjust group: Master Electric`, `Single adjust item: FAN MODE`
- Ligne export : 46186 · id 49105

#### FAN OUT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=FAN MODE
- Fonction *AUTO* :
  - **Activating** = `Inside(Timer Fan [min], 0,5, 4)`
- Fonction *OFF* :
  - **Blocking** = `True`
- Fonction *FORCE ON* :
  - **Activating** = `True`
- Lit : ``, `FAN MODE`, `Timer Fan`
- Utilisé par : `K1 Fan Rear / Fan`
- Ligne export : 46199 · id 49108

#### NEED PUMP  `IDC`
- Propriétés : Toggle=No · Delay on=20000 · Delay off=0
- Logique :
  - **Activating** = `(M3 - NEED TO PUMP) OR (M2 - NEED TO PUMP) OR (M1 - NEED TO PUMP)`
- Lit : ``, `M1 - NEED TO PUMP`, `M2 - NEED TO PUMP`, `M3 - NEED TO PUMP`
- Utilisé par : `PUMP VAR`
- Ligne export : 46307 · id 49130

#### PUMP VAR MODE  `SP`
- Propriétés : Input channel=None · Default state name=AUTO · States={OFF; FORCE ON}
- Utilisé par : `PUMP VAR`, `Adjust group: Master Electric`, `Single adjust item: PUMP VAR MODE`
- Ligne export : 46364 · id 49140

#### PUMP VAR  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=PUMP VAR MODE
- Fonction *AUTO* :
  - **Activating** = `NEED PUMP`
- Fonction *OFF* :
  - **Blocking** = `True`
- Fonction *FORCE ON* :
  - **Activating** = `True`
- Lit : ``, `NEED PUMP`, `PUMP VAR MODE`
- Utilisé par : `K2 Fan Super / Pump`
- Ligne export : 46377 · id 49143

## Electric / MOTORS / M-Hydrau — actif seulement si `VARIATOR SUPER ON`

#### Oil Not Good  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Wait_Very_Low_Oil_Level`
- Lit : ``, `Wait_Very_Low_Oil_Level`
- Utilisé par : `Oil not Good`
- Ligne export : 44175 · id 48802

#### Speed Hydro Force  `IP`
- Propriétés : Default mode={0}
- Utilisé par : `M3_Speed`, `Adjust group: Master Features`, `Single adjust item: Speed Hydro Force`
- Ligne export : 44218 · id 59221

#### M3_Speed  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxOf (Absolute)(Engine hydro Speed [rpm], Speed Hydro Force)`
- Lit : ``, `Engine hydro Speed`, `Speed Hydro Force`
- Utilisé par : `M3_speed`
- Ligne export : 44230 · id 48810

#### M-Pump - Brand  `SP`
- Propriétés : Input channel=None · Default state name=Sevcon · States={}
- Utilisé par : `Engine Temps`, `Heatsink`, `Is_M3_Sevcon`, `M3 - CAN OK`, `M3 - Error mode`, `M3 - Ready`, `M3 - Run`, `M3 - Voltage`
- Ligne export : 44279 · id 48981

#### Is_M3_Sevcon  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M-Pump - Brand = 0`
- Lit : ``, `M-Pump - Brand`
- Utilisé par : `Active le groupe: Electric / MOTORS / M-Hydrau / Sevcon`, `Measure group: Pump Sevcon`
- Ligne export : 44290 · id 49006

#### Heatsink  `MAC`
- Propriétés : Unit=*C · Limiting object group=Signed · Function selector=M-Pump - Brand
- Fonction *Sevcon* : (vide)
- Lit : ``, `M-Pump - Brand`
- Utilisé par : `M3 - NEED TO FAN`, `M3 - NEED TO PUMP`
- Ligne export : 45545 · id 48982

#### M3 - NEED TO FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Heatsink [*C] >= Controller Fan Temp [Â°C]`
- Lit : ``, `Controller Fan Temp`, `Heatsink`
- Utilisé par : `NEED FAN`
- Ligne export : 45580 · id 48990

#### M3 - NEED TO PUMP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Heatsink [*C] >= Controller Pump Temp [Â°C]`
- Lit : ``, `Controller Pump Temp`, `Heatsink`
- Utilisé par : `NEED PUMP`
- Ligne export : 45625 · id 48998

#### Engine Temps  `MAC`
- Propriétés : Unit=*C · Limiting object group=Signed · Function selector=M-Pump - Brand
- Fonction *Sevcon* : (vide)
- Lit : ``, `M-Pump - Brand`
- Utilisé par : `M3 - Charge`, `M3 - ENGINE HOT`
- Ligne export : 45670 · id 49014

#### M3 - ENGINE HOT  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Engine Temps [*C] >= Engine Eco Temp [Â°C]`
- Lit : ``, `Engine Eco Temp`, `Engine Temps`
- Utilisé par : *(personne)*
- Ligne export : 45705 · id 49022

#### M3 - Voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed · Function selector=M-Pump - Brand
- Fonction *Sevcon* :
  - **Controlling** = `Sevcon - Voltage_3 [V]`
- Lit : ``, `M-Pump - Brand`, `Sevcon - Voltage_3`
- Utilisé par : *(personne)*
- Ligne export : 45750 · id 49030

#### M3 - Run  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Pump - Brand
- Fonction *Sevcon* :
  - **Activating** = `Sevcon - M3 - RUN`
- Lit : ``, `M-Pump - Brand`, `Sevcon - M3 - RUN`
- Utilisé par : `IDC Tension`, `Statistics log: Electric Stats`
- Ligne export : 45792 · id 49038

#### M3 - Charge  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `((MaxOf((Engine Temps [*C] - 40), 0)) / (Engine Max Temp [Â°C] - 40)) * 100`
- Lit : ``, `C`, `Engine Max Temp`, `Engine Temps`
- Utilisé par : *(personne)*
- Ligne export : 45835 · id 49046

#### M3 - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Pump - Brand
- Fonction *Sevcon* :
  - **Activating** = `Sevcon - CAN OK`
- Lit : ``, `M-Pump - Brand`, `Sevcon - CAN OK`
- Utilisé par : `Measure group: CanBus`
- Ligne export : 45915 · id 49058

#### M3 - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Pump - Brand
- Fonction *Sevcon* :
  - **Activating** = `Sevcon - Ready`
- Lit : ``, `M-Pump - Brand`, `Sevcon - Ready`
- Utilisé par : *(personne)*
- Ligne export : 45958 · id 49066

#### M3 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Pump - Brand
- Fonction *Sevcon* :
  - **Activating** = `Sevcon - Error mode`
- Lit : ``, `M-Pump - Brand`, `Sevcon - Error mode`
- Utilisé par : *(personne)*
- Ligne export : 46001 · id 49074

## Electric / MOTORS / M-Hydrau / Sevcon — actif seulement si `Is_M3_Sevcon`

#### JFIN-A:J1939[113]  `JFIN`
- Propriétés : Priority=DonÂt care · PGN=71936 · Destination address (DA)=255 · Timeout=500 · Paged protocol={Not used} · Multipacket=No · Parameters={{Status Word; 33}; {Limit Word; 41}} · Module=HVLP (J1939[113]) · Module index=0
- Lit : `Limit Word`, `Status Word`
- Utilisé par : *(personne)*
- Ligne export : 44357 · id 54210

#### Status Word  `JPIN`
- Propriétés : Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `JFIN-A:J1939[113]`, `JFOUT-A:J1939[113]`, `JFOUT-A:J1939[250]`, `Sevcon - Ready`, `Status Word`, `Status Word`, `Measure group: Pump Sevcon`
- Ligne export : 44382 · id 54211

#### Limit Word  `JPIN`
- Propriétés : Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `JFIN-A:J1939[113]`
- Ligne export : 44396 · id 54212

#### Test Mode  `SMC`
- Propriétés : Default state name=Normal
- Fonction *Test* : (vide)
- Lit : ``
- Utilisé par : `Speed`
- Ligne export : 44410 · id 54213

#### HVLP Speed Test  `IP`
- Propriétés : Default mode={-100}
- Utilisé par : `Speed`
- Ligne export : 44443 · id 54220

#### M3_speed  `FGI`
- Propriétés : Input type=Real · Input=M3_Speed · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `M3_Speed`
- Utilisé par : `Speed`
- Ligne export : 44455 · id 54443

#### Speed  `IMAC`
- Propriétés : Function selector=Test Mode
- Fonction *Normal* :
  - **Controlling** = `Abs(M3_speed)`
- Fonction *Test* :
  - **Controlling** = `HVLP Speed Test`
- Lit : ``, `HVLP Speed Test`, `M3_speed`, `Test Mode`
- Utilisé par : `Speed`, `Speed Slope`, `Speed_compute`, `TSC1-A:J1939-0`, `Adjust group: `
- Ligne export : 44469 · id 54221

#### Speed Slope  `SFC`
- Propriétés : Input channel=Speed · Enable=Yes · Type=Slopes · Slopes={{3000; 3000}; {3000; 3000}}
- Lit : `Speed`
- Utilisé par : `ON/OFF Var`
- Ligne export : 44542 · id 54236

#### JFIN-B:J1939[113]  `JFIN`
- Propriétés : Priority=DonÂt care · PGN=71680 · Destination address (DA)=255 · Timeout=500 · Paged protocol={Not used} · Multipacket=No · Parameters={{Motor_Speed_Raw; 17}; {Torque_Mesured_Raw; 1}} · Module=HVLP (J1939[113]) · Module index=1
- Lit : `Motor_Speed_Raw`, `Torque_Mesured_Raw`
- Utilisé par : `Sevcon - CAN OK`
- Ligne export : 44560 · id 54245

#### Sevcon - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `JFIN-B:J1939[113]`
- Lit : ``, `JFIN-B:J1939[113]`
- Utilisé par : `M3 - CAN OK`, `Measure group: Pump Sevcon`
- Ligne export : 44585 · id 54246

#### Motor_Speed_Raw  `JPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · J1939 Error check=No · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `JFIN-B:J1939[113]`, `Motor Speed`, `Sevcon - M3 - RUN`
- Ligne export : 44628 · id 54254

#### Sevcon - M3 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `(Abs(Motor_Speed_Raw)) > 1800`
- Lit : ``, `Motor_Speed_Raw`
- Utilisé par : `M3 - Run`, `Measure group: Pump Sevcon`
- Ligne export : 44642 · id 54255

#### Sevcon - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Status Word = 7) OR (Status Word = 8)`
- Lit : ``, `Status Word`
- Utilisé par : `M3 - Ready`, `Measure group: Pump Sevcon`
- Ligne export : 44695 · id 54264

#### Oil not Good  `FGI`
- Propriétés : Input type=Digital · Input=Oil Not Good · Default state name=Default state
- Lit : `Oil Not Good`
- Utilisé par : `ON/OFF Var`
- Ligne export : 44749 · id 54444

#### ON/OFF Var  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `(Speed Slope <> 0) AND (VARIATOR SUPER ON)`
  - **Blocking** = `Oil not Good`
- Lit : ``, `Oil not Good`, `Speed Slope`, `VARIATOR SUPER ON`
- Utilisé par : `Variator State`
- Ligne export : 44760 · id 54445

#### Variator State  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ON* :
  - **Activating** = `ON/OFF Var`
- Lit : ``, `ON/OFF Var`
- Utilisé par : `Status Word`
- Ligne export : 44819 · id 54273

#### Status Word  `IP`
- Propriétés : Mode selector=Variator State · Default mode: OFF={3} · Mode 1: ON={5}
- Lit : `Variator State`
- Utilisé par : `JFIN-A:J1939[113]`, `JFOUT-A:J1939[113]`, `JFOUT-A:J1939[250]`, `Sevcon - Ready`, `Status Word`, `Status Word`, `Measure group: Pump Sevcon`
- Ligne export : 44859 · id 54281

#### JFIN-C:J1939[113]  `JFIN`
- Propriétés : Priority=DonÂt care · PGN=72192 · Destination address (DA)=255 · Timeout=500 · Paged protocol={Not used} · Multipacket=No · Parameters={{Input Voltage; 33}} · Module=HVLP (J1939[113]) · Module index=2
- Lit : `Input Voltage`
- Utilisé par : *(personne)*
- Ligne export : 44873 · id 54282

#### Input Voltage  `JPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · J1939 Error check=No · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `JFIN-C:J1939[113]`, `Sevcon - Voltage_3`, `Adjust group: Master Charger`, `Adjust group: Setup Charger`, `Measure group: Charger Elcon`, `Single adjust item: Input Voltage`
- Ligne export : 44895 · id 54283

#### Sevcon - Voltage_3  `IMAC`
- Propriétés : Unit=V
- Logique :
  - **Controlling** = `Input Voltage * 0,0625`
- Lit : ``, `Input Voltage`
- Utilisé par : `M3 - Voltage`, `Measure group: Pump Sevcon`
- Ligne export : 44909 · id 54284

#### Torque_Mesured_Raw  `JPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · J1939 Error check=No · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `JFIN-B:J1939[113]`, `Torque actual`
- Ligne export : 44952 · id 54292

#### JFIN-D:J1939[113]  `JFIN`
- Propriétés : Priority=DonÂt care · PGN=72448 · Destination address (DA)=255 · Timeout=3000 · Paged protocol={Not used} · Multipacket=No · Parameters={{M3 (Pump) - Error; 1}} · Module=HVLP (J1939[113]) · Module index=3
- Lit : `M3 (Pump) - Error`
- Utilisé par : *(personne)*
- Ligne export : 44966 · id 54301

#### M3 (Pump) - Error  `JPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · J1939 Error check=Yes · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `Error 3 - MEM`, `JFIN-D:J1939[113]`, `M3  (Pump) - Filter`, `M3 - New Error Code`, `Sevcon - Error mode`, `Event log: Electronic Logs`, `Measure group: Pump Sevcon`
- Ligne export : 44988 · id 54302

#### M3  (Pump) - Filter  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(M3 (Pump) - Error = 0) OR (M3 (Pump) - Error = 17862)`
- Lit : ``, `M3 (Pump) - Error`
- Utilisé par : `M3 - New Error Code`, `Sevcon - Error mode`
- Ligne export : 45002 · id 54303

#### M3 - New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M3 (Pump) - Error <> Error 3 - MEM`
  - **Blocking** = `M3  (Pump) - Filter`
- Lit : ``, `Error 3 - MEM`, `M3  (Pump) - Filter`, `M3 (Pump) - Error`
- Utilisé par : `Error 3 - MEM`, `Event log: Electronic Logs`
- Ligne export : 45056 · id 54312

#### Error 3 - MEM  `MEM`
- Propriétés : Input channel=M3 (Pump) - Error · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M3 - New Error Code)`
- Lit : ``, `M3 (Pump) - Error`, `M3 - New Error Code`
- Utilisé par : `Error 3`, `M3 - New Error Code`, `M3 - Pump Engine CMSG`
- Ligne export : 45108 · id 54321

#### M3 - Pump Engine CMSG  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Pump Engine · Text=Error, stop battery, wait one minute, restart. · Channel=Error 3 - MEM
- Lit : ``, `Error 3 - MEM`
- Utilisé par : *(personne)*
- Ligne export : 45153 · id 54329

#### Sevcon - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M3 (Pump) - Error`
  - **Blocking** = `M3  (Pump) - Filter`
- Lit : ``, `M3  (Pump) - Filter`, `M3 (Pump) - Error`
- Utilisé par : `M3 - Error mode`
- Ligne export : 45192 · id 54336

#### Status Word  `JPOUT`
- Propriétés : Input value=Status Word · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Lit : `Status Word`
- Utilisé par : `JFIN-A:J1939[113]`, `JFOUT-A:J1939[113]`, `JFOUT-A:J1939[250]`, `Sevcon - Ready`, `Status Word`, `Measure group: Pump Sevcon`
- Ligne export : 45242 · id 54345

#### Torque Demande  `JPOUT`
- Propriétés : Input value=0xFD80 · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-A:J1939[113]`, `JFOUT-A:J1939[250]`
- Ligne export : 45254 · id 54346

#### Torque Limit  `JPOUT`
- Propriétés : Input value=640 · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-A:J1939[113]`, `JFOUT-A:J1939[250]`
- Ligne export : 45266 · id 54347

#### JFOUT-A:J1939[250]  `JFOUT`
- Propriétés : J1939 source address=250 · Priority=6 · PGN=69632 · Destination address (DA)=113 · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Multipacket=No · Parameters={{Status Word [bits]; 17}; {Torque Demande [bits]; 1}; {Torque Limit [bits]; 33}} · Module=HVLP (J1939[113]) · Module index=1
- Lit : `Status Word`, `Torque Demande`, `Torque Limit`
- Utilisé par : *(personne)*
- Ligne export : 45278 · id 54348

#### Fw Speed Limit  `JPOUT`
- Propriétés : Input value=3000 · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-B:J1939[113]`
- Ligne export : 45307 · id 54349

#### Speed_compute  `IMAC`
- Logique :
  ```qcode
  if Speed = 0 then
  Result := 0
  else
  Result := (bnot(Speed) band 0xFFFF) + 0x1
  endif
  ```
- Lit : `Speed`
- Utilisé par : `Rw Speed Limit`
- Ligne export : 45319 · id 54359

#### Rw Speed Limit  `JPOUT`
- Propriétés : Input value=Speed_compute · Length=16 · Resolution=1 · Offset=0
- Lit : `Speed_compute`
- Utilisé par : `JFOUT-B:J1939[113]`
- Ligne export : 45341 · id 54350

#### JFOUT-B:J1939[113]  `JFOUT`
- Propriétés : J1939 source address=250 · Priority=6 · PGN=69888 · Destination address (DA)=113 · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Multipacket=No · Parameters={{Fw Speed Limit [bits]; 17}; {Rw Speed Limit [bits]; 33}} · Module=HVLP (J1939[113]) · Module index=2
- Lit : `Fw Speed Limit`, `Rw Speed Limit`
- Utilisé par : *(personne)*
- Ligne export : 45353 · id 54351

#### I Batt Discharge Limit  `JPOUT`
- Propriétés : Input value=50 · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-C:J1939[250]`
- Ligne export : 45379 · id 54352

#### I Batt recharge limit  `JPOUT`
- Propriétés : Input value=0xFFCE · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-C:J1939[250]`
- Ligne export : 45391 · id 54353

#### JFOUT-C:J1939[250]  `JFOUT`
- Propriétés : J1939 source address=250 · Priority=6 · PGN=70144 · Destination address (DA)=113 · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Multipacket=No · Parameters={{I Batt Discharge Limit [bits]; 1}; {I Batt recharge limit [bits]; 17}} · Module=HVLP (J1939[113]) · Module index=3
- Lit : `I Batt Discharge Limit`, `I Batt recharge limit`
- Utilisé par : *(personne)*
- Ligne export : 45403 · id 54354

#### Status Word  `JPOUT`
- Propriétés : Input value=Status Word · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Lit : `Status Word`
- Utilisé par : `JFIN-A:J1939[113]`, `JFOUT-A:J1939[113]`, `JFOUT-A:J1939[250]`, `Sevcon - Ready`, `Status Word`, `Measure group: Pump Sevcon`
- Ligne export : 45429 · id 54355

#### Torque Demande  `JPOUT`
- Propriétés : Input value=0xFD80 · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-A:J1939[113]`, `JFOUT-A:J1939[250]`
- Ligne export : 45441 · id 54356

#### Torque Limit  `JPOUT`
- Propriétés : Input value=640 · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-A:J1939[113]`, `JFOUT-A:J1939[250]`
- Ligne export : 45453 · id 54357

#### JFOUT-A:J1939[113]  `JFOUT`
- Propriétés : J1939 source address=113 · Priority=6 · PGN=69632 · Destination address (DA)=113 · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Multipacket=No · Parameters={{Status Word [bits]; 17}; {Torque Demande [bits]; 1}; {Torque Limit [bits]; 33}} · Module=HVLP (J1939[113]) · Module index=0
- Lit : `Status Word`, `Torque Demande`, `Torque Limit`
- Utilisé par : *(personne)*
- Ligne export : 45465 · id 54358

#### Motor Speed  `IMAC`
- Propriétés : Unit=rpm
- Logique :
  ```qcode
  data := Motor_Speed_Raw
  start_byte := data band 0x8000
  if start_byte = 0x8000 then
  Result := (bnot(data) band 0x7FFF + 0x0001 ) * -1
  else
  Result := data
  endif
  ```
- Lit : `Motor_Speed_Raw`
- Utilisé par : `Measure group: Pump Sevcon`
- Ligne export : 45494 · id 61581

#### Torque actual  `MAC`
- Propriétés : Unit=Nm
- Logique :
  ```qcode
  data := Torque_Mesured_Raw
  start_byte := data band 0x8000
  if start_byte = 0x8000 then
  result_data := (bnot(data) band 0x7FFF + 0x0001 ) * -1 / 16
  else
  result_data := data
  endif
  Result := result_data / 16
  ```
- Lit : `Torque_Mesured_Raw`
- Utilisé par : `Measure group: Pump Sevcon`
- Ligne export : 45519 · id 61616

## Electric / MOTORS / M-Tracks — actif seulement si `VARIATOR SUPER ON`

#### M-Track - Brand  `SP`
- Propriétés : Input channel=M-Track - Brand Main · Default state name=Sevcon · States={Zapi}
- Lit : `M-Track - Brand Main`
- Utilisé par : `Is_MT_Sevcon`, `Is_MT_Zapi`, `M1 - CAN OK`, `M1 - CURRENT`, `M1 - Error mode`, `M1 - Heatsink`, `M1 - KTY`, `M1 - RUN`, `M1 - Ready`, `M1 - Speed`, `M1 - Torque`, `M1 - Voltage`, `M2 - CAN OK`, `M2 - CURRENT`, `M2 - Error mode`, `M2 - Heatsink`, `M2 - KTY`, `M2 - RUN`, `M2 - Ready`, `M2 - Speed`, `M2 - Torque`, `M2 - Voltage`
- Ligne export : 34219 · id 47939

#### Max Speed  `IP`
- Propriétés : Unit=% · Mode selector=Speed Pump · Default mode: Slow={35} · Mode 1: Super Slow={15} · Mode 2: Fast Speed={100}
- Lit : `Speed Pump`
- Utilisé par : `Math Left`, `Math Right`, `Min Speed`, `Adjust group: `, `Single adjust item: Max Speed`
- Ligne export : 34231 · id 59589

#### Min Speed  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `0 - Max Speed [%]`
- Lit : ``, `Max Speed`
- Utilisé par : `Math Left`, `Math Right`, `Adjust group: Master Thermic`, `Single adjust item: Min Speed`
- Ligne export : 34247 · id 59590

#### Math Right  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe((Right Filter [%] *% Current Limiting [%]): {{-100; Min Speed [%]}; {0; 0}; {100; Max Speed [%]}}, Freeze)`
- Lit : ``, `Current Limiting`, `Max Speed`, `Min Speed`, `Right Filter`
- Utilisé par : `Filter Right`
- Ligne export : 34290 · id 47949

#### Filter Right  `SFC`
- Propriétés : Input channel=Math Right [%] · Enable=Yes · Type=Slopes · Slopes={{Start Slope [%/s]; Stop Slope [%/s]}; {Start Slope [%/s]; Stop Slope [%/s]}}
- Lit : `Math Right`, `Start Slope`, `Stop Slope`
- Utilisé par : `Speed CAN Right`, `Speed_CAN_Right`, `Measure group: Electric Engine`
- Ligne export : 34352 · id 60179

#### Is_MT_Zapi  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M-Track - Brand = 1`
- Lit : ``, `M-Track - Brand`
- Utilisé par : `Active le groupe: Electric / MOTORS / M-Tracks / ZAPI Left`, `Active le groupe: Electric / MOTORS / M-Tracks / ZAPI Right`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`, `Single adjust item: Enable Power Zapi`, `Single adjust item: ZAPI Node`
- Ligne export : 34370 · id 48288

#### Enable Power Zapi  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Enable`, `Enable`, `Forward`, `Forward`, `Adjust group: Master Electric`, `Single adjust item: Enable Power Zapi`
- Ligne export : 34415 · id 59227

#### Math Left  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe((Left Filter [%] *% Current Limiting [%]): {{-100; Min Speed [%]}; {0; 0}; {100; Max Speed [%]}}, Freeze)`
- Lit : ``, `Current Limiting`, `Left Filter`, `Max Speed`, `Min Speed`
- Utilisé par : `Filter Left`
- Ligne export : 36689 · id 47957

#### Filter Left  `SFC`
- Propriétés : Input channel=Math Left [%] · Enable=Yes · Type=Slopes · Slopes={{Start Slope [%/s]; Stop Slope [%/s]}; {Start Slope [%/s]; Stop Slope [%/s]}}
- Lit : `Math Left`, `Start Slope`, `Stop Slope`
- Utilisé par : `Speed CAN Left`, `Speed_CAN_Left`, `Measure group: Electric Engine`
- Ligne export : 36751 · id 60182

#### Is_MT_Sevcon  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M-Track - Brand = 0`
- Lit : ``, `M-Track - Brand`
- Utilisé par : `Active le groupe: Electric / MOTORS / M-Tracks / Sevcon`
- Ligne export : 39011 · id 47941

#### Engine Max Temp  `IP`
- Propriétés : Unit=Â°C · Default mode={110}
- Utilisé par : `M1 - Charge`, `M2 - Charge`, `M3 - Charge`
- Ligne export : 41272 · id 48297

#### Controller Fan Temp  `IP`
- Propriétés : Unit=Â°C · Default mode={60}
- Utilisé par : `M1 - NEED TO FAN`, `M2 - NEED TO FAN`, `M3 - NEED TO FAN`
- Ligne export : 41284 · id 48298

#### M1 - Heatsink  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M1 - Heatsink [Â°C]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M1_Heatsink [Â°C]`
- Lit : ``, `M-Track - Brand`, `SEV - M1 - Heatsink`, `ZAPI_M1_Heatsink`
- Utilisé par : `M1 - NEED TO FAN`, `M1 - NEED TO PUMP`
- Ligne export : 41296 · id 48299

#### M1 - NEED TO FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M1 - Heatsink [Â°C] >= Controller Fan Temp [Â°C]`
- Lit : ``, `Controller Fan Temp`, `M1 - Heatsink`
- Utilisé par : `NEED FAN`
- Ligne export : 41369 · id 48313

#### Engine Eco Temp  `IP`
- Propriétés : Unit=Â°C · Default mode={90}
- Utilisé par : `M1 - ENGINE HOT`, `M2 - ENGINE HOT`, `M3 - ENGINE HOT`
- Ligne export : 41414 · id 48321

#### Controller Pump Temp  `IP`
- Propriétés : Unit=Â°C · Default mode={50}
- Utilisé par : `M1 - NEED TO PUMP`, `M2 - NEED TO PUMP`, `M3 - NEED TO PUMP`
- Ligne export : 41426 · id 48322

#### M1 - NEED TO PUMP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M1 - Heatsink [Â°C] >= Controller Pump Temp [Â°C]`
- Lit : ``, `Controller Pump Temp`, `M1 - Heatsink`
- Utilisé par : `NEED PUMP`
- Ligne export : 41438 · id 48323

#### M1 - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M1 - CURRENT [A]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M1_Actual_current [A]`
- Lit : ``, `M-Track - Brand`, `SEV - M1 - CURRENT`, `ZAPI_M1_Actual_current`
- Utilisé par : `Instant current Filter`, `Measure group: Electric Engine`
- Ligne export : 41483 · id 48331

#### M1 - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M1 - CAN OK`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M1_CAN OK`
- Lit : ``, `M-Track - Brand`, `SEV - M1 - CAN OK`, `ZAPI_M1_CAN OK`
- Utilisé par : `Measure group: CanBus`
- Ligne export : 41556 · id 48345

#### M1 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M1 - RUN`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M1_RUN`
- Lit : ``, `M-Track - Brand`, `SEV - M1 - RUN`, `ZAPI_M1_RUN`
- Utilisé par : `Statistics log: Electric Stats`
- Ligne export : 41630 · id 48359

#### M1 - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M1 - Ready`
- Fonction *Zapi* :
  - **Activating** = `True`
- Lit : ``, `M-Track - Brand`, `SEV - M1 - Ready`
- Utilisé par : *(personne)*
- Ligne export : 41704 · id 48373

#### M1 - Voltage  `IMAC`
- Propriétés : Unit=V · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M1 - Voltage [V]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M1_Batterie Voltage [V]`
- Lit : ``, `M-Track - Brand`, `SEV - M1 - Voltage`, `ZAPI_M1_Batterie Voltage`
- Utilisé par : *(personne)*
- Ligne export : 41778 · id 48387

#### M1 - Torque  `IMAC`
- Propriétés : Unit=Nm · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M1 - Torque actual [Nm]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M1_Torque [Nm]`
- Lit : ``, `M-Track - Brand`, `SEV - M1 - Torque actual`, `ZAPI_M1_Torque`
- Utilisé par : `Measure group: Electric Engine`
- Ligne export : 41850 · id 48401

#### M1 - Speed  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M1 - Speed [rpm]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M1_Actual_speed [rpm]`
- Lit : ``, `M-Track - Brand`, `SEV - M1 - Speed`, `ZAPI_M1_Actual_speed`
- Utilisé par : `M1 - Mechanical power`, `Measure group: Electric Engine`
- Ligne export : 41922 · id 48415

#### M1 - KTY  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M1 - KTY [Â°C]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M1_Motor_Temp [Â°C]`
- Lit : ``, `M-Track - Brand`, `SEV - M1 - KTY`, `ZAPI_M1_Motor_Temp`
- Utilisé par : `M1 - Charge`, `M1 - ENGINE HOT`, `Measure group: Electric Engine`
- Ligne export : 41995 · id 48429

#### M1 - Charge  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `((MaxOf((M1 - KTY [Â°C] - 40), 0)) / (Engine Max Temp [Â°C] - 40)) * 100`
- Lit : ``, `C`, `Engine Max Temp`, `M1 - KTY`
- Utilisé par : *(personne)*
- Ligne export : 42068 · id 48443

#### M1 - ENGINE HOT  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `M1 - KTY [Â°C] >= Engine Eco Temp [Â°C]`
- Lit : ``, `Engine Eco Temp`, `M1 - KTY`
- Utilisé par : *(personne)*
- Ligne export : 42148 · id 48455

#### M2 - Heatsink  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M2 - Heatsink [Â°C]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Heatsink [Â°C]`
- Lit : ``, `M-Track - Brand`, `SEV - M2 - Heatsink`, `ZAPI_M2_Heatsink`
- Utilisé par : `M2 - NEED TO FAN`, `M2 - NEED TO PUMP`
- Ligne export : 42193 · id 48463

#### M2 - NEED TO FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M2 - Heatsink [Â°C] >= Controller Fan Temp [Â°C]`
- Lit : ``, `Controller Fan Temp`, `M2 - Heatsink`
- Utilisé par : `NEED FAN`
- Ligne export : 42266 · id 48477

#### M2 - NEED TO PUMP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M2 - Heatsink [Â°C] >= Controller Pump Temp [Â°C]`
- Lit : ``, `Controller Pump Temp`, `M2 - Heatsink`
- Utilisé par : `NEED PUMP`
- Ligne export : 42311 · id 48485

#### M2 - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M2 - CURRENT [A]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Actual_current [A]`
- Lit : ``, `M-Track - Brand`, `SEV - M2 - CURRENT`, `ZAPI_M2_Actual_current`
- Utilisé par : `Instant current Filter`, `Measure group: Electric Engine`
- Ligne export : 42356 · id 48493

#### M2 - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M2 - CAN OK`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M2_READY`
- Lit : ``, `M-Track - Brand`, `SEV - M2 - CAN OK`, `ZAPI_M2_READY`
- Utilisé par : `Measure group: CanBus`
- Ligne export : 42429 · id 48507

#### M2 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M2 - RUN`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M2_RUN`
- Lit : ``, `M-Track - Brand`, `SEV - M2 - RUN`, `ZAPI_M2_RUN`
- Utilisé par : `Statistics log: Electric Stats`
- Ligne export : 42503 · id 48521

#### M2 - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M2 - Ready`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M2_READY`
- Lit : ``, `M-Track - Brand`, `SEV - M2 - Ready`, `ZAPI_M2_READY`
- Utilisé par : *(personne)*
- Ligne export : 42577 · id 48535

#### M2 - Voltage  `IMAC`
- Propriétés : Unit=V · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M2 - Voltage [V]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Batterie Voltage [V]`
- Lit : ``, `M-Track - Brand`, `SEV - M2 - Voltage`, `ZAPI_M2_Batterie Voltage`
- Utilisé par : *(personne)*
- Ligne export : 42651 · id 48549

#### M2 - Torque  `IMAC`
- Propriétés : Unit=Nm · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M2 - Torque actual [Nm]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Torque [Nm]`
- Lit : ``, `M-Track - Brand`, `SEV - M2 - Torque actual`, `ZAPI_M2_Torque`
- Utilisé par : `Measure group: Electric Engine`
- Ligne export : 42723 · id 48563

#### M2 - Speed  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M2 - Speed [rpm]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Actual_speed [rpm]`
- Lit : ``, `M-Track - Brand`, `SEV - M2 - Speed`, `ZAPI_M2_Actual_speed`
- Utilisé par : `M2 - Mechanical power`, `Measure group: Electric Engine`
- Ligne export : 42795 · id 48577

#### M2 - KTY  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `SEV - M2 - KTY [Â°C]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Motor_Temp [Â°C]`
- Lit : ``, `M-Track - Brand`, `SEV - M2 - KTY`, `ZAPI_M2_Motor_Temp`
- Utilisé par : `M2 - Charge`, `M2 - ENGINE HOT`, `Measure group: Electric Engine`
- Ligne export : 42868 · id 48591

#### M2 - Charge  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `((MaxOf((M2 - KTY [Â°C] - 40), 0)) / (Engine Max Temp [Â°C] - 40)) * 100`
- Lit : ``, `C`, `Engine Max Temp`, `M2 - KTY`
- Utilisé par : *(personne)*
- Ligne export : 42941 · id 48605

#### M2 - ENGINE HOT  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `M2 - KTY [Â°C] >= Engine Eco Temp [Â°C]`
- Lit : ``, `Engine Eco Temp`, `M2 - KTY`
- Utilisé par : *(personne)*
- Ligne export : 43021 · id 48617

#### M1 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M1 - Error mode`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M1_Error mode`
- Lit : ``, `M-Track - Brand`, `SEV - M1 - Error mode`, `ZAPI_M1_Error mode`
- Utilisé par : *(personne)*
- Ligne export : 43066 · id 48625

#### M2 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `SEV - M2 - Error mode`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M2_Error mode`
- Lit : ``, `M-Track - Brand`, `SEV - M2 - Error mode`, `ZAPI_M2_Error mode`
- Utilisé par : *(personne)*
- Ligne export : 43140 · id 48639

#### Instant current Filter  `SFC`
- Propriétés : Input channel=M1 - CURRENT [A] · Enable=Yes · Type=BWL · BWL=20
- Lit : `M1 - CURRENT`
- Utilisé par : `Couple Moteur`, `Couple Moteur`, `M1 - 100A-125A`, `M1 - 25A-50A`, `M1 - 50A-75A`, `M1 - 75A-100A`, `M1 - up to 125A`, `M2 - 100A-125A`, `M2 - 25A-50A`, `M2 - 50A-75A`, `M2 - 75A-100A`, `M2 - up to 125A`
- Ligne export : 43214 · id 48653

#### Couple Moteur  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `26 * courbe(((0,8 * Instant current Filter [A]) / 33): {{0; 0}; {1; 1}; {2; 1,8}; {2,5; 2,18}; {3; 2,45}; {3,5; 2,62}; {4; 2,75}}, Freeze)`
- Lit : ``, `C`, `Instant current Filter`
- Utilisé par : `M1 - Mechanical power`, `M1 - Torque Tracks`, `M2 - Mechanical power`, `M2 - Torque tracks`
- Ligne export : 43226 · id 48654

#### M1 - Mechanical power  `MAC`
- Propriétés : Unit=kW · Limiting object group=Signed
- Logique :
  - **Controlling** = `((M1 - Speed [rpm] * 0,104719) * Couple Moteur [Nm]) / 1000`
- Lit : ``, `Couple Moteur`, `M1 - Speed`
- Utilisé par : *(personne)*
- Ligne export : 43318 · id 48665

#### M1 - Torque Tracks  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Couple Moteur [Nm] * 37,2`
- Lit : ``, `Couple Moteur`
- Utilisé par : *(personne)*
- Ligne export : 43380 · id 48675

#### M1 - 25A-50A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(25 < Instant current Filter [A]) AND (Instant current Filter [A] <= 50)`
- Lit : ``, `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 43424 · id 48683

#### M1 - 50A-75A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(50 < Instant current Filter [A]) AND (Instant current Filter [A] <= 75)`
- Lit : ``, `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 43478 · id 48692

#### M1 - 75A-100A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(75 < Instant current Filter [A]) AND (Instant current Filter [A] <= 100)`
- Lit : ``, `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 43532 · id 48701

#### M1 - 100A-125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(100 < Instant current Filter [A]) AND (Instant current Filter [A] <= 125)`
- Lit : ``, `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 43586 · id 48710

#### M1 - up to 125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `125 < Instant current Filter [A]`
- Lit : ``, `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 43640 · id 48719

#### Instant current Filter  `SFC`
- Propriétés : Input channel=M2 - CURRENT [A] · Enable=Yes · Type=Moving average · Window size=25
- Lit : `M2 - CURRENT`
- Utilisé par : `Couple Moteur`, `Couple Moteur`, `M1 - 100A-125A`, `M1 - 25A-50A`, `M1 - 50A-75A`, `M1 - 75A-100A`, `M1 - up to 125A`, `M2 - 100A-125A`, `M2 - 25A-50A`, `M2 - 50A-75A`, `M2 - 75A-100A`, `M2 - up to 125A`
- Ligne export : 43685 · id 48727

#### Couple Moteur  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `26 * courbe(((0,8 * Instant current Filter [A]) / 33): {{0; 0}; {1; 1}; {2; 1,8}; {2,5; 2,18}; {3; 2,45}; {3,5; 2,62}; {4; 2,75}}, Freeze)`
- Lit : ``, `C`, `Instant current Filter`
- Utilisé par : `M1 - Mechanical power`, `M1 - Torque Tracks`, `M2 - Mechanical power`, `M2 - Torque tracks`
- Ligne export : 43697 · id 48728

#### M2 - Mechanical power  `MAC`
- Propriétés : Unit=kW · Limiting object group=Signed
- Logique :
  - **Controlling** = `((M2 - Speed [rpm] * 0,104719) * Couple Moteur [Nm]) / 1000`
- Lit : ``, `Couple Moteur`, `M2 - Speed`
- Utilisé par : *(personne)*
- Ligne export : 43789 · id 48739

#### M2 - Torque tracks  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Couple Moteur [Nm] * 37,2`
- Lit : ``, `Couple Moteur`
- Utilisé par : *(personne)*
- Ligne export : 43851 · id 48749

#### M2 - 25A-50A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(25 < Instant current Filter [A]) AND (Instant current Filter [A] <= 50)`
- Lit : ``, `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 43895 · id 48757

#### M2 - 50A-75A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(50 < Instant current Filter [A]) AND (Instant current Filter [A] <= 75)`
- Lit : ``, `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 43949 · id 48766

#### M2 - 75A-100A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(75 < Instant current Filter [A]) AND (Instant current Filter [A] <= 100)`
- Lit : ``, `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 44003 · id 48775

#### M2 - 100A-125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(100 < Instant current Filter [A]) AND (Instant current Filter [A] <= 125)`
- Lit : ``, `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 44057 · id 48784

#### M2 - up to 125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `125 < Instant current Filter [A]`
- Lit : ``, `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 44111 · id 48793

## Electric / MOTORS / M-Tracks / Sevcon — actif seulement si `Is_MT_Sevcon`

#### Speed CAN Right  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Filter Right [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Filter Right`
- Utilisé par : `Convert Right`, `Fordward Right`, `Reverse Right`
- Ligne export : 39093 · id 47966

#### 0x341  `GFIN`
- Propriétés : Identifier=0x341 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Motor Speed - 1 [rpm]; 0}; {Actual Current - 1 [A]; 32}; {Torque - 1 [Raw]; 48}} · Module=Sevcon_M_Track (Generic) · Module index=1
- Lit : `Actual Current - 1`, `Motor Speed - 1`, `Torque - 1`
- Utilisé par : *(personne)*
- Ligne export : 39107 · id 47967

#### Actual Current - 1  `GPIN`
- Propriétés : Unit=A · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x341`, `SEV - M1 - CURRENT`
- Ligne export : 39132 · id 47968

#### SEV - M1 - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Actual Current - 1 [A]`
- Lit : ``, `Actual Current - 1`
- Utilisé par : `M1 - CURRENT`
- Ligne export : 39145 · id 47969

#### 0x331  `GFIN`
- Propriétés : Identifier=0x331 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{M1 (Right) - Error; 16}; {Statut - 1 [State]; 0}} · Module=Sevcon_M_Track (Generic) · Module index=0
- Lit : `M1 (Right) - Error`, `State`, `Statut - 1`
- Utilisé par : *(personne)*
- Ligne export : 39187 · id 47977

#### M1 (Right) - Error  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x331`, `Error 1 - MEM`, `M1 - New Error Code`, `M1 - Right Engine CMSG`, `SEV - M1 - Error mode`
- Ligne export : 39209 · id 47978

#### 0x351  `GFIN`
- Propriétés : Identifier=0x351 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{SEV - M1 - KTY [Â°C]; 0}; {SEV - M1 - Heatsink [Â°C]; 16}; {Voltage -1 [Raw]; 24}} · Module=Sevcon_M_Track (Generic) · Module index=2
- Lit : `C`, `SEV - M1 - Heatsink`, `SEV - M1 - KTY`, `Voltage -1`
- Utilisé par : *(personne)*
- Ligne export : 39222 · id 47979

#### SEV - M1 - KTY  `GPIN`
- Propriétés : Unit=Â°C · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x351`, `M1 - KTY`
- Ligne export : 39247 · id 47980

#### SEV - M1 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `M1 (Right) - Error`
  - **Blocking** = `M1 (Right) - Error = 0`
- Lit : ``, `M1 (Right) - Error`
- Utilisé par : `FS1 Switch`, `M1 - Error mode`, `M1 - Normal Mode`, `M1 - Right Engine CMSG`
- Ligne export : 39260 · id 47981

#### M1 - Normal Mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(SEV - M1 - Error mode)`
- Lit : ``, `SEV - M1 - Error mode`
- Utilisé par : `SEV - M1 - Ready`
- Ligne export : 39312 · id 47990

#### SEV - M1 - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `0x341`
- Lit : ``
- Utilisé par : `M1 - CAN OK`
- Ligne export : 39356 · id 47998

#### Motor Speed - 1  `GPIN`
- Propriétés : Unit=rpm · Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x341`, `SEV - M1 - RUN`, `SEV - M1 - Speed`
- Ligne export : 39399 · id 48006

#### SEV - M1 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Motor Speed - 1 [rpm] <> 0`
- Lit : ``, `Motor Speed - 1`
- Utilisé par : `M1 - RUN`
- Ligne export : 39412 · id 48007

#### SEV - M1 - Heatsink  `GPIN`
- Propriétés : Unit=Â°C · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `0x351`, `M1 - Heatsink`
- Ligne export : 39457 · id 48015

#### SEV - M1 - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M1 - Normal Mode`
- Lit : ``, `M1 - Normal Mode`
- Utilisé par : `M1 - Ready`
- Ligne export : 39469 · id 48016

#### M1 - Right Engine CMSG  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Right Engine · Text=Error, stop battery, wait one minute, restart. · Channel=M1 (Right) - Error
- Logique :
  - **Showing** = `SEV - M1 - Error mode`
- Lit : ``, `M1 (Right) - Error`, `SEV - M1 - Error mode`
- Utilisé par : *(personne)*
- Ligne export : 39512 · id 48024

#### Convert Right  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe(Speed CAN Right [%]: {{-100; 3000}; {0; 0}; {100; 3000}}, Freeze)`
- Lit : ``, `Speed CAN Right`
- Utilisé par : `Throttle Input Voltage`
- Ligne export : 39558 · id 48032

#### Throttle Input Voltage  `GPOUT`
- Propriétés : Input value=Convert Right · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Convert Right`
- Utilisé par : `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 39611 · id 48040

#### VARIATOR ON Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR SUPER ON`
- Lit : ``, `VARIATOR SUPER ON`
- Utilisé par : `Fordward Left`, `Fordward Right`, `Reverse Left`, `Reverse Right`
- Ligne export : 39623 · id 48041

#### Fordward Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed CAN Right [%] < 0) AND (VARIATOR ON Wait)`
- Lit : ``, `Speed CAN Right`, `VARIATOR ON Wait`
- Utilisé par : `FS1 Switch`, `Fordward Switch`
- Ligne export : 39666 · id 48049

#### Fordward Switch  `GPOUT`
- Propriétés : Input value=Fordward Right · Length=1 bit · Type=Unsigned integer
- Lit : `Fordward Right`
- Utilisé par : `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 39718 · id 48058

#### Reverse Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed CAN Right [%] > 0) AND (VARIATOR ON Wait)`
- Lit : ``, `Speed CAN Right`, `VARIATOR ON Wait`
- Utilisé par : `FS1 Switch`, `Inch reverse switch`
- Ligne export : 39729 · id 48059

#### Inch reverse switch  `GPOUT`
- Propriétés : Input value=Reverse Right · Length=1 bit · Type=Unsigned integer
- Lit : `Reverse Right`
- Utilisé par : `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 39781 · id 48068

#### FS1 Switch  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Fordward Right) OR (Reverse Right)`
  - **Blocking** = `SEV - M1 - Error mode`
- Lit : ``, `Fordward Right`, `Reverse Right`, `SEV - M1 - Error mode`
- Utilisé par : `FS1 Switch`, `FS1 Switch`, `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 39792 · id 48069

#### FS1 Switch  `GPOUT`
- Propriétés : Input value=FS1 Switch · Length=1 bit · Type=Unsigned integer
- Lit : `FS1 Switch`
- Utilisé par : `FS1 Switch`, `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 39849 · id 48079

#### GEN - 4 - Right  `GFOUT`
- Propriétés : Identifier=0x411 · Data length=8 · Send method=Continuously · Transmit rate=Every cycle · Unused bits=Set to 0 · Parameters={{Throttle Input Voltage; 0}; {Fordward Switch; 16}; {Inch reverse switch; 17}; {FS1 Switch; 18}} · Module=Sevcon_M_Track (Generic) · Module index=1
- Lit : `FS1 Switch`, `Fordward Switch`, `Inch reverse switch`, `Throttle Input Voltage`
- Utilisé par : *(personne)*
- Ligne export : 39860 · id 48080

#### Torque - 1  `GPIN`
- Propriétés : Unit=Raw · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x341`, `SEV - M1 - Torque actual`
- Ligne export : 39888 · id 48081

#### Voltage -1  `GPIN`
- Propriétés : Unit=Raw · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x351`, `SEV - M1 - Voltage`
- Ligne export : 39901 · id 48082

#### SEV - M1 - Voltage  `IMAC`
- Propriétés : Unit=V
- Logique :
  - **Controlling** = `Voltage -1 [Raw] * 0,0625`
- Lit : ``, `Voltage -1`
- Utilisé par : `M1 - Voltage`
- Ligne export : 39914 · id 48083

#### SEV - M1 - Torque actual  `IMAC`
- Propriétés : Unit=Nm
- Logique :
  - **Controlling** = `(Torque - 1 [Raw] * 0,0625) * 37,2`
- Lit : ``, `Torque - 1`
- Utilisé par : `M1 - Torque`
- Ligne export : 39957 · id 48091

#### Statut - 1  `GPIN`
- Propriétés : Unit=State · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x331`
- Ligne export : 40009 · id 48100

#### Error 1 - MEM  `MEM`
- Propriétés : Input channel=M1 (Right) - Error · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M1 - New Error Code)`
- Lit : ``, `M1 (Right) - Error`, `M1 - New Error Code`
- Utilisé par : `Error 1`, `M1 - New Error Code`
- Ligne export : 40022 · id 48101

#### M1 - New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M1 (Right) - Error <> Error 1 - MEM`
  - **Blocking** = `(M1 (Right) - Error = 0) OR (M1 (Right) - Error = 19073)`
- Lit : ``, `Error 1 - MEM`, `M1 (Right) - Error`
- Utilisé par : `Error 1 - MEM`
- Ligne export : 40067 · id 48109

#### SEV - M1 - Speed  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Motor Speed - 1 [rpm] * -1`
- Lit : ``, `Motor Speed - 1`
- Utilisé par : `M1 - Speed`
- Ligne export : 40130 · id 48119

#### 0x342  `GFIN`
- Propriétés : Identifier=0x342 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Motor Speed - 2 [rpm]; 0}; {Actual Current - 2 [A]; 32}; {Torque actual- 2 [Raw]; 48}} · Module=Sevcon_M_Track (Generic) · Module index=4
- Lit : `Actual Current - 2`, `Motor Speed - 2`, `Torque actual- 2`
- Utilisé par : *(personne)*
- Ligne export : 40174 · id 48127

#### Actual Current - 2  `GPIN`
- Propriétés : Unit=A · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x342`, `SEV - M2 - CURRENT`
- Ligne export : 40199 · id 48128

#### SEV - M2 - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Actual Current - 2 [A]`
- Lit : ``, `Actual Current - 2`
- Utilisé par : `M2 - CURRENT`
- Ligne export : 40212 · id 48129

#### 0x332  `GFIN`
- Propriétés : Identifier=0x332 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{M2 (Left) - Error; 16}; {Statut - 2 [Status]; 0}} · Module=Sevcon_M_Track (Generic) · Module index=3
- Lit : `M2 (Left) - Error`, `Statut - 2`
- Utilisé par : *(personne)*
- Ligne export : 40254 · id 48137

#### M2 (Left) - Error  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x332`, `Error 2 - MEM`, `M2 - Left Engine CMSG`, `M2 - New Error Code`, `SEV - M2 - Error mode`
- Ligne export : 40276 · id 48138

#### 0x352  `GFIN`
- Propriétés : Identifier=0x352 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{SEV - M2 - KTY [Â°C]; 0}; {SEV - M2 - Heatsink [Â°C]; 16}; {Voltage -2 [Raw]; 24}} · Module=Sevcon_M_Track (Generic) · Module index=5
- Lit : `C`, `SEV - M2 - Heatsink`, `SEV - M2 - KTY`, `Voltage -2`
- Utilisé par : *(personne)*
- Ligne export : 40289 · id 48139

#### SEV - M2 - KTY  `GPIN`
- Propriétés : Unit=Â°C · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x352`, `M2 - KTY`
- Ligne export : 40314 · id 48140

#### SEV - M2 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `M2 (Left) - Error`
  - **Blocking** = `M2 (Left) - Error = 0`
- Lit : ``, `M2 (Left) - Error`
- Utilisé par : `FS1 Switch`, `M2 - Error mode`, `M2 - Left Engine CMSG`, `M2 - Normal mode`
- Ligne export : 40327 · id 48141

#### M2 - Normal mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(SEV - M2 - Error mode)`
- Lit : ``, `SEV - M2 - Error mode`
- Utilisé par : `SEV - M2 - Ready`
- Ligne export : 40379 · id 48150

#### SEV - M2 - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `0x342`
- Lit : ``
- Utilisé par : `M2 - CAN OK`
- Ligne export : 40423 · id 48158

#### Motor Speed - 2  `GPIN`
- Propriétés : Unit=rpm · Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x342`, `SEV - M2 - RUN`, `SEV - M2 - Speed`
- Ligne export : 40466 · id 48166

#### SEV - M2 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Motor Speed - 2 [rpm] <> 0`
- Lit : ``, `Motor Speed - 2`
- Utilisé par : `M2 - RUN`
- Ligne export : 40479 · id 48167

#### SEV - M2 - Heatsink  `GPIN`
- Propriétés : Unit=Â°C · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `0x352`, `M2 - Heatsink`
- Ligne export : 40524 · id 48175

#### SEV - M2 - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M2 - Normal mode`
- Lit : ``, `M2 - Normal mode`
- Utilisé par : `M2 - Ready`
- Ligne export : 40536 · id 48176

#### M2 - Left Engine CMSG  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Left Engine · Text=Error, stop battery, wait one minute, restart. · Channel=M2 (Left) - Error
- Logique :
  - **Showing** = `SEV - M2 - Error mode`
- Lit : ``, `M2 (Left) - Error`, `SEV - M2 - Error mode`
- Utilisé par : *(personne)*
- Ligne export : 40579 · id 48184

#### Torque actual- 2  `GPIN`
- Propriétés : Unit=Raw · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x342`, `SEV - M2 - Torque actual`
- Ligne export : 40625 · id 48192

#### Voltage -2  `GPIN`
- Propriétés : Unit=Raw · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x352`, `SEV - M2 - Voltage`
- Ligne export : 40638 · id 48193

#### SEV - M2 - Voltage  `IMAC`
- Propriétés : Unit=V
- Logique :
  - **Controlling** = `Voltage -2 [Raw] * 0,0625`
- Lit : ``, `Voltage -2`
- Utilisé par : `M2 - Voltage`
- Ligne export : 40651 · id 48194

#### SEV - M2 - Torque actual  `IMAC`
- Propriétés : Unit=Nm
- Logique :
  - **Controlling** = `(Torque actual- 2 [Raw] * 0,0625) * 37,2`
- Lit : ``, `Torque actual- 2`
- Utilisé par : `M2 - Torque`
- Ligne export : 40694 · id 48202

#### Speed CAN Left  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Filter Left [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Filter Left`
- Utilisé par : `Convert Left`, `Fordward Left`, `Reverse Left`
- Ligne export : 40746 · id 48211

#### Convert Left  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe(Speed CAN Left [%]: {{-100; 3000}; {0; 0}; {100; 3000}}, Freeze)`
- Lit : ``, `Speed CAN Left`
- Utilisé par : `Throttle Input Voltage`
- Ligne export : 40760 · id 48212

#### Throttle Input Voltage  `GPOUT`
- Propriétés : Input value=Convert Left · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Convert Left`
- Utilisé par : `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 40813 · id 48220

#### VARIATOR ON Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR SUPER ON`
- Lit : ``, `VARIATOR SUPER ON`
- Utilisé par : `Fordward Left`, `Fordward Right`, `Reverse Left`, `Reverse Right`
- Ligne export : 40825 · id 48221

#### Fordward Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed CAN Left [%] < 0) AND (VARIATOR ON Wait)`
- Lit : ``, `Speed CAN Left`, `VARIATOR ON Wait`
- Utilisé par : `FS1 Switch`, `Fordward Switch`
- Ligne export : 40868 · id 48229

#### Fordward Switch  `GPOUT`
- Propriétés : Input value=Fordward Left · Length=1 bit · Type=Unsigned integer
- Lit : `Fordward Left`
- Utilisé par : `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 40920 · id 48238

#### Reverse Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed CAN Left [%] > 0) AND (VARIATOR ON Wait)`
- Lit : ``, `Speed CAN Left`, `VARIATOR ON Wait`
- Utilisé par : `FS1 Switch`, `Inch reverse switch`
- Ligne export : 40931 · id 48239

#### Inch reverse switch  `GPOUT`
- Propriétés : Input value=Reverse Left · Length=1 bit · Type=Unsigned integer
- Lit : `Reverse Left`
- Utilisé par : `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 40983 · id 48248

#### FS1 Switch  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Fordward Left) OR (Reverse Left)`
  - **Blocking** = `SEV - M2 - Error mode`
- Lit : ``, `Fordward Left`, `Reverse Left`, `SEV - M2 - Error mode`
- Utilisé par : `FS1 Switch`, `FS1 Switch`, `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 40994 · id 48249

#### FS1 Switch  `GPOUT`
- Propriétés : Input value=FS1 Switch · Length=1 bit · Type=Unsigned integer
- Lit : `FS1 Switch`
- Utilisé par : `FS1 Switch`, `GEN - 4 - Left`, `GEN - 4 - Right`
- Ligne export : 41051 · id 48259

#### GEN - 4 - Left  `GFOUT`
- Propriétés : Identifier=0x412 · Data length=8 · Send method=Continuously · Transmit rate=Every cycle · Unused bits=Set to 0 · Parameters={{Throttle Input Voltage; 0}; {Fordward Switch; 16}; {Inch reverse switch; 17}; {FS1 Switch; 18}} · Module=Sevcon_M_Track (Generic) · Module index=0
- Lit : `FS1 Switch`, `Fordward Switch`, `Inch reverse switch`, `Throttle Input Voltage`
- Utilisé par : *(personne)*
- Ligne export : 41062 · id 48260

#### Statut - 2  `GPIN`
- Propriétés : Unit=Status · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x332`
- Ligne export : 41090 · id 48261

#### Error 2 - MEM  `MEM`
- Propriétés : Input channel=M2 (Left) - Error · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M2 - New Error Code)`
- Lit : ``, `M2 (Left) - Error`, `M2 - New Error Code`
- Utilisé par : `Error 2`, `M2 - New Error Code`
- Ligne export : 41103 · id 48262

#### M2 - New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M2 (Left) - Error <> Error 2 - MEM`
  - **Blocking** = `(M2 (Left) - Error = 0) OR (M2 (Left) - Error = 19073)`
- Lit : ``, `Error 2 - MEM`, `M2 (Left) - Error`
- Utilisé par : `Error 2 - MEM`
- Ligne export : 41148 · id 48270

#### SEV - M2 - Speed  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Motor Speed - 2 [rpm] * -1`
- Lit : ``, `Motor Speed - 2`
- Utilisé par : `M2 - Speed`
- Ligne export : 41211 · id 48280

#### SYNC  `GFOUT`
- Propriétés : Identifier=0x80 · Data length=0 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={} · Module=Sevcon_M_Track (Generic) · Module index=2
- Utilisé par : *(personne)*
- Ligne export : 41255 · id 50612

## Electric / MOTORS / M-Tracks / ZAPI Left — actif seulement si `Is_MT_Zapi`

#### Speed_CAN_Left  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Filter Left [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Filter Left`
- Utilisé par : `Speed_Left`
- Ligne export : 36796 · id 53327

#### Speed_Left  `MAC`
- Propriétés : Unit=rpm
- Logique :
  ```qcode
  Result := Speed_CAN_Left * 30 * -1
  ```
- Lit : `Speed_CAN_Left`
- Utilisé par : `Enable`, `Forward`, `Reverse`, `Target_speed_can`
- Ligne export : 36810 · id 53006

#### Node_ID  `IP`
- Propriétés : Mode selector=ZAPI Node · Default mode: 8-10={10} · Mode 1: 1-4={4} · Mode 2: 4-8={8}
- Lit : `ZAPI Node`
- Utilisé par : `EMERG`, `HeartBeat`, `Node ID`, `PDO1_RX`, `PDO1_TX`, `PDO2_TX`
- Ligne export : 36828 · id 53062

#### EMERG  `IMAC`
- Logique :
  - **Controlling** = `0x80 + Node_ID`
- Lit : ``, `Node_ID`
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 36844 · id 53218

#### GFIN PDO2_TX  `GFIN`
- Propriétés : Identifier=EMERG · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{Left Zapi Error Code; 0}; {alarm present; 16}; {Zapi alarm code; 24}; {flag alarm; 32}; {extra info alarm; 40}} · Module=ZAPI (Generic) · Module index=10
- Lit : `EMERG`, `Left Zapi Error Code`, `Zapi alarm code`, `alarm present`, `extra info alarm`, `flag alarm`
- Utilisé par : *(personne)*
- Ligne export : 36887 · id 53226

#### Left Zapi Error Code  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Error 2 - MEM`, `GFIN PDO2_TX`, `Left Error`, `M2 - Zapi - New Error Code`, `Event log: Electronic Logs`, `Measure group: Track Zapi Left`
- Ligne export : 36918 · id 53227

#### alarm present  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Left Error`, `ZAPI_M2_Error mode`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 36931 · id 53228

#### Left Error  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Engine Left · Text=Error, stop battery, wait one minute, restart. · Channel=Left Zapi Error Code
- Logique :
  - **Showing** = `alarm present`
  - **Hiding** = `Left Zapi Error Code = 0`
- Lit : ``, `Left Zapi Error Code`, `alarm present`
- Utilisé par : `Emmergency Stop Left`
- Ligne export : 36943 · id 53319

#### PDO2_TX  `IMAC`
- Logique :
  - **Controlling** = `0x280 + Node_ID`
- Lit : ``, `Node_ID`
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 36998 · id 53072

#### GFIN PDO2_TX  `GFIN`
- Propriétés : Identifier=PDO2_TX · Data length=8 · Timeout=3000 · Paged protocol={Not used} · Parameters={{Left Zapi Warning; 0}; {Motor Temp; 16}; {Heatsink; 24}; {BDI Percentage; 32}; {Batterie Current; 40}; {Batterie Voltage; 48}} · Module=ZAPI (Generic) · Module index=8
- Lit : `BDI Percentage`, `Batterie Current`, `Batterie Voltage`, `Heatsink`, `Left Zapi Warning`, `Motor Temp`, `PDO2_TX`
- Utilisé par : *(personne)*
- Ligne export : 37041 · id 53080

#### Left Zapi Warning  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Left Warning`, `Left Warning`, `M2 - ZAPI - New Warning Code`, `Warning 2 - MEM`, `Event log: Electronic Logs`, `Measure group: Track Zapi Left`
- Ligne export : 37075 · id 53081

#### Left Warning  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Engine Left · Text=Error, stop battery, wait one minute, restart. · Channel=Left Zapi Warning
- Logique :
  - **Showing** = `Left Zapi Warning`
- Lit : ``, `Left Zapi Warning`
- Utilisé par : `Emmergency Stop Left`
- Ligne export : 37088 · id 59416

#### Error Wait  `IDC`
- Propriétés : Toggle=No · Delay on=4000 · Delay off=0
- Logique :
  - **Activating** = `ZAPI_M2_Error mode`
- Lit : ``, `ZAPI_M2_Error mode`
- Utilisé par : `Emmergency Stop Left`, `Reset`
- Ligne export : 37134 · id 60267

#### Emmergency Stop Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Emmergency Stop Left) OR (PositiveFlank(Left Warning)) OR (PositiveFlank(Left Error)) OR (PositiveFlank(Emmergency Stop Right))`
  - **Blocking** = `(NegativeFlank(VARIATOR SUPER ON)) OR (PositiveFlank(Error Wait))`
- Lit : ``, `Emmergency Stop Right`, `Error Wait`, `Left Error`, `Left Warning`, `VARIATOR SUPER ON`
- Utilisé par : `Brake`, `Emmergency Stop Right`, `Enable`, `ZAPI_M2_Error mode`, `Measure group: Track Zapi Left`
- Ligne export : 37177 · id 60151

#### ZAPI_M2_Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(alarm present) OR (Emmergency Stop Left)`
- Lit : ``, `Emmergency Stop Left`, `alarm present`
- Utilisé par : `Error Wait`, `M2 - Error mode`, `ZAPI_M2_READY`, `Measure group: Track Zapi Left`
- Ligne export : 37260 · id 53344

#### Enable  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed_Left [rpm] <> 0) OR (Enable Power Zapi)`
  - **Blocking** = `Emmergency Stop Left`
- Lit : ``, `Emmergency Stop Left`, `Enable Power Zapi`, `Speed_Left`
- Utilisé par : `Brake`, `Power`
- Ligne export : 37310 · id 53013

#### Target_speed_can  `MAC`
- Propriétés : Unit=Hz/10
- Logique :
  ```qcode
  Result := abs(Speed_Left)  * 5 / 6
  ```
- Lit : `Speed_Left`
- Utilisé par : `Target SPeed`
- Ligne export : 37369 · id 53021

#### PDO1_TX  `IMAC`
- Logique :
  - **Controlling** = `0x180 + Node_ID`
- Lit : ``, `Node_ID`
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 37387 · id 53099

#### GFIN PDO1_TX  `GFIN`
- Propriétés : Identifier=PDO1_TX · Data length=8 · Timeout=3000 · Paged protocol={Not used} · Parameters={{Actual_Speed [Hz/10]; 0}; {Out MNC; 16}; {Stuffing; 31}; {Actual Current [A*5]; 56}; {Status Byte; 32}} · Module=ZAPI (Generic) · Module index=7
- Lit : `Actual Current`, `Actual_Speed`, `Out MNC`, `PDO1_TX`, `Status Byte`, `Stuffing`
- Utilisé par : `ZAPI_M2_CAN OK`
- Ligne export : 37430 · id 53107

#### Actual_Speed  `GPIN`
- Propriétés : Unit=Hz/10 · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `ZAPI_M2_Actual_speed`, `ZAPI_M2_RUN`
- Ligne export : 37461 · id 53108

#### Target SPeed  `GPOUT`
- Propriétés : Input value=Target_speed_can [Hz/10] · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Target_speed_can`
- Utilisé par : `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`
- Ligne export : 37474 · id 53032

#### Power  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `Enable`
- Lit : ``, `Enable`
- Utilisé par : `Enable Power`, `Forward`, `Reverse`
- Ligne export : 37486 · id 59285

#### Forward  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed_Left [rpm] >= 0) OR (Enable Power Zapi)`
  - **Blocking** = `not(Power)`
- Lit : ``, `Enable Power Zapi`, `Power`, `Speed_Left`
- Utilisé par : `Forward Req`
- Ligne export : 37529 · id 53033

#### Reverse  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Speed_Left [rpm] < 0`
  - **Blocking** = `not(Power)`
- Lit : ``, `Power`, `Speed_Left`
- Utilisé par : `Reverse Req`
- Ligne export : 37589 · id 53041

#### Enable Power  `GPOUT`
- Propriétés : Input value=Power · Length=1 bit · Type=Unsigned integer
- Lit : `Power`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 37642 · id 53049

#### Forward Req  `GPOUT`
- Propriétés : Input value=Forward · Length=1 bit · Type=Unsigned integer
- Lit : `Forward`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 37653 · id 53050

#### Reverse Req  `GPOUT`
- Propriétés : Input value=Reverse · Length=1 bit · Type=Unsigned integer
- Lit : `Reverse`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 37664 · id 53051

#### Brake  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `Enable`
  - **Blocking** = `Emmergency Stop Left`
- Lit : ``, `Emmergency Stop Left`, `Enable`
- Utilisé par : `Brake`, `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 37675 · id 59293

#### Brake  `GPOUT`
- Propriétés : Input value=Brake · Length=1 bit · Type=Unsigned integer
- Lit : `Brake`
- Utilisé par : `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 37725 · id 60067

#### Stuffing  `IDC`
- Propriétés : Toggle=Yes · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank(GFOUT - PDO1_RX)`
- Lit : ``, `GFOUT - PDO1_RX`
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`, `Stuffing`
- Ligne export : 37736 · id 53053

#### Stuffing  `GPOUT`
- Propriétés : Input value=Stuffing · Length=1 bit · Type=Unsigned integer
- Lit : `Stuffing`
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`
- Ligne export : 37780 · id 53061

#### PDO1_RX  `IMAC`
- Logique :
  - **Controlling** = `0x200 + Node_ID`
- Lit : ``, `Node_ID`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 37791 · id 53063

#### Power Line  `GPOUT`
- Propriétés : Input value=1 · Length=1 bit · Type=Unsigned integer
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 37834 · id 53071

#### GFOUT - PDO1_RX  `GFOUT`
- Propriétés : Identifier=PDO1_RX · Data length=8 · Send method=Continuously · Transmit rate=40 · Unused bits=Set to 0 · Parameters={{Target SPeed [Hz/10]; 0}; {Enable Power; 16}; {Forward Req; 19}; {Reverse Req; 20}; {Stuffing; 31}; {Power Line; 17}; {Brake; 27}} · Module=ZAPI (Generic) · Module index=8
- Lit : `Brake`, `Enable Power`, `Forward Req`, `PDO1_RX`, `Power Line`, `Reverse Req`, `Stuffing`, `Target SPeed`
- Utilisé par : `Stuffing`
- Ligne export : 37845 · id 53052

#### Motor Temp  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M2_Motor_Temp`
- Ligne export : 37882 · id 53082

#### Heatsink  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M2_Heatsink`
- Ligne export : 37894 · id 53083

#### BDI Percentage  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 37906 · id 53084

#### Batterie Current  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M2_Batterie Current`
- Ligne export : 37918 · id 53085

#### Batterie Voltage  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M2_Batterie Voltage`
- Ligne export : 37930 · id 53086

#### Out MNC  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 37943 · id 53109

#### Stuffing  `GPIN`
- Propriétés : Length=1 bit · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`, `Stuffing`
- Ligne export : 37955 · id 53110

#### VARIATOR ON Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR SUPER ON`
- Lit : ``, `VARIATOR SUPER ON`
- Utilisé par : `Func State`
- Ligne export : 37967 · id 53111

#### Reset  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Func State`, `Reset`, `Adjust group: Master Electric`, `Single adjust item: Reset`
- Ligne export : 38010 · id 56411

#### Reset  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Reset OR (PositiveFlank(Error Wait))`
- Lit : ``, `Error Wait`, `Reset`
- Utilisé par : `Func State`, `Adjust group: Master Electric`, `Single adjust item: Reset`
- Ligne export : 38023 · id 53119

#### Func State  `SMC`
- Propriétés : Default state name=Stop
- Fonction *Start* :
  - **Activating** = `VARIATOR ON Wait`
  - **Blocking** = `Reset`
- Fonction *Preprop* : (vide)
- Fonction *Reset* :
  - **Activating** = `Reset`
- Lit : ``, `Reset`, `VARIATOR ON Wait`
- Utilisé par : `Func`
- Ligne export : 38074 · id 53126

#### Func  `IP`
- Propriétés : Mode selector=Func State · Default mode: Stop={2} · Mode 1: Start={1} · Mode 2: Preprop={0x80} · Mode 3: Reset={0x81}
- Lit : `Func State`
- Utilisé par : `Func ID`
- Ligne export : 38176 · id 53142

#### Func ID  `GPOUT`
- Propriétés : Input value=Func · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Func`
- Utilisé par : `NMT`
- Ligne export : 38194 · id 53143

#### Node ID  `GPOUT`
- Propriétés : Input value=Node_ID · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Node_ID`
- Utilisé par : `NMT`
- Ligne export : 38205 · id 53144

#### NMT  `GFOUT`
- Propriétés : Identifier=0 · Data length=8 · Send method=Continuously · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{Func ID; 0}; {Node ID; 8}} · Module=ZAPI (Generic) · Module index=7
- Lit : `Func ID`, `Node ID`
- Utilisé par : *(personne)*
- Ligne export : 38216 · id 53145

#### HeartBeat  `IMAC`
- Logique :
  - **Controlling** = `0x700 + Node_ID`
- Lit : ``, `Node_ID`
- Utilisé par : `GFIN HeartBeat`
- Ligne export : 38238 · id 53146

#### GFIN HeartBeat  `GFIN`
- Propriétés : Identifier=HeartBeat · Data length=1 · Timeout=1000 · Paged protocol={Not used} · Parameters={{HeartBeat State; 0}} · Module=ZAPI (Generic) · Module index=9
- Lit : `HeartBeat`, `HeartBeat State`
- Utilisé par : *(personne)*
- Ligne export : 38281 · id 53154

#### HeartBeat State  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN HeartBeat`, `ZAPI_M2_READY`
- Ligne export : 38300 · id 53155

#### ZAPI_M2_CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `GFIN PDO1_TX`
- Lit : ``, `GFIN PDO1_TX`
- Utilisé par : `Measure group: Track Zapi Left`
- Ligne export : 38312 · id 53156

#### ZAPI_M2_Batterie Voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `Batterie Voltage / 3,3333`
- Lit : ``, `Batterie Voltage`
- Utilisé par : `M2 - Voltage`, `Measure group: Track Zapi Left`
- Ligne export : 38355 · id 53164

#### ZAPI_M2_Batterie Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Batterie Current * 2`
- Lit : ``, `Batterie Current`
- Utilisé par : `Measure group: Track Zapi Left`
- Ligne export : 38399 · id 53172

#### ZAPI_M2_Motor_Temp  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Motor Temp - 40`
- Lit : ``, `Motor Temp`
- Utilisé par : `M2 - KTY`, `Measure group: Track Zapi Left`
- Ligne export : 38443 · id 53180

#### ZAPI_M2_Heatsink  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Heatsink`
- Lit : ``, `Heatsink`
- Utilisé par : `M2 - Heatsink`, `Measure group: Track Zapi Left`
- Ligne export : 38487 · id 53188

#### ZAPI_M2_Actual_speed  `MAC`
- Propriétés : Unit=rpm
- Logique :
  ```qcode
  Result := Actual_Speed * 6 / 5
  ```
- Lit : `Actual_Speed`
- Utilisé par : `M2 - Speed`, `Measure group: Track Zapi Left`
- Ligne export : 38529 · id 53196

#### Actual Current  `GPIN`
- Propriétés : Unit=A*5 · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `ZAPI_M2_Actual_current`
- Ligne export : 38547 · id 53207

#### ZAPI_M2_Actual_current  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result := Actual Current * 5
  ```
- Lit : `Actual Current`
- Utilisé par : `M2 - CURRENT`, `ZAPI_M2_Torque`, `Measure group: Track Zapi Left`
- Ligne export : 38559 · id 53208

#### Zapi alarm code  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 38577 · id 53229

#### flag alarm  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 38589 · id 53230

#### extra info alarm  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 38601 · id 53231

#### ZAPI_M2_READY  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `HeartBeat State`
  - **Blocking** = `ZAPI_M2_Error mode`
- Lit : ``, `HeartBeat State`, `ZAPI_M2_Error mode`
- Utilisé par : `M2 - CAN OK`, `M2 - Ready`
- Ligne export : 38613 · id 53328

#### ZAPI_M2_RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Actual_Speed [Hz/10] <> 0`
- Lit : ``, `Actual_Speed`
- Utilisé par : `M2 - RUN`, `Measure group: Track Zapi Left`
- Ligne export : 38663 · id 53336

#### Warning 2 - MEM  `MEM`
- Propriétés : Input channel=Left Zapi Warning · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M2 - ZAPI - New Warning Code)`
- Lit : ``, `Left Zapi Warning`, `M2 - ZAPI - New Warning Code`
- Utilisé par : `M2 - ZAPI - New Warning Code`
- Ligne export : 38708 · id 59790

#### M2 - ZAPI - New Warning Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Left Zapi Warning <> Warning 2 - MEM`
  - **Blocking** = `Left Zapi Warning = 0`
- Lit : ``, `Left Zapi Warning`, `Warning 2 - MEM`
- Utilisé par : `Warning 2 - MEM`, `Event log: Electronic Logs`
- Ligne export : 38753 · id 59798

#### Error 2 - MEM  `MEM`
- Propriétés : Input channel=Left Zapi Error Code · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M2 - Zapi - New Error Code)`
- Lit : ``, `Left Zapi Error Code`, `M2 - Zapi - New Error Code`
- Utilisé par : `Error 2`, `M2 - Zapi - New Error Code`
- Ligne export : 38807 · id 59807

#### M2 - Zapi - New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Left Zapi Error Code <> Error 2 - MEM`
  - **Blocking** = `Left Zapi Error Code = 0`
- Lit : ``, `Error 2 - MEM`, `Left Zapi Error Code`
- Utilisé par : `Error 2 - MEM`, `Event log: Electronic Logs`
- Ligne export : 38852 · id 59815

#### Status Byte  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 38906 · id 60258

#### ZAPI_M2_Torque  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `26 * courbe(((0,8 * ZAPI_M2_Actual_current [A]) / 33): {{0; 0}; {1; 1}; {2; 1,8}; {2,5; 2,18}; {3; 2,45}; {3,5; 2,62}; {4; 2,75}}, Freeze)`
- Lit : ``, `C`, `ZAPI_M2_Actual_current`
- Utilisé par : `M2 - Torque`
- Ligne export : 38918 · id 63046

## Electric / MOTORS / M-Tracks / ZAPI Right — actif seulement si `Is_MT_Zapi`

#### Node_ID  `IP`
- Propriétés : Mode selector=ZAPI Node · Default mode: 8-10={8} · Mode 1: 1-4={1} · Mode 2: 4-8={4}
- Lit : `ZAPI Node`
- Utilisé par : `EMERG`, `HeartBeat`, `Node ID`, `PDO1_RX`, `PDO1_TX`, `PDO2_TX`
- Ligne export : 34455 · id 52192

#### Node ID  `GPOUT`
- Propriétés : Input value=Node_ID · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Node_ID`
- Utilisé par : `NMT`
- Ligne export : 34471 · id 52259

#### Speed_CAN_Right  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Filter Right [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Filter Right`
- Utilisé par : `Speed_Right`
- Ligne export : 34482 · id 52546

#### Speed_Right  `MAC`
- Propriétés : Unit=rpm
- Logique :
  ```qcode
  Result := Speed_CAN_Right * 30
  ```
- Lit : `Speed_CAN_Right`
- Utilisé par : `Enable`, `Forward`, `Reverse`, `Target_Speed_can`
- Ligne export : 34496 · id 52140

#### EMERG  `IMAC`
- Logique :
  - **Controlling** = `0x80 + Node_ID`
- Lit : ``, `Node_ID`
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 34514 · id 52335

#### GFIN PDO2_TX  `GFIN`
- Propriétés : Identifier=EMERG · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{Right Zapi Error Code; 0}; {alarm present; 16}; {Zapi alarm code; 24}; {flag alarm; 32}; {extra info alarm; 40}} · Module=ZAPI (Generic) · Module index=3
- Lit : `EMERG`, `Right Zapi Error Code`, `Zapi alarm code`, `alarm present`, `extra info alarm`, `flag alarm`
- Utilisé par : *(personne)*
- Ligne export : 34557 · id 52343

#### Right Zapi Error Code  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Error 1 - MEM`, `GFIN PDO2_TX`, `M1 - Zapi New Error Code`, `Right Error`, `Event log: Electronic Logs`, `Measure group: Track Zapi Right`
- Ligne export : 34588 · id 52344

#### alarm present  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Right Error`, `ZAPI_M1_Error mode`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 34601 · id 52345

#### Right Error  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Engine Right · Text=Error, stop battery, wait one minute, restart. · Channel=Right Zapi Error Code
- Logique :
  - **Showing** = `alarm present`
  - **Hiding** = `Right Zapi Error Code = 0`
- Lit : ``, `Right Zapi Error Code`, `alarm present`
- Utilisé par : `Emmergency Stop Right`
- Ligne export : 34613 · id 52436

#### PDO2_TX  `IMAC`
- Logique :
  - **Controlling** = `0x280 + Node_ID`
- Lit : ``, `Node_ID`
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 34668 · id 52202

#### GFIN PDO2_TX  `GFIN`
- Propriétés : Identifier=PDO2_TX · Data length=8 · Timeout=3000 · Paged protocol={Not used} · Parameters={{Right Zapi Warning; 0}; {Motor Temp; 16}; {Heatsink; 24}; {BDI Percentage; 32}; {Batterie Current; 40}; {Batterie Voltage; 48}} · Module=ZAPI (Generic) · Module index=1
- Lit : `BDI Percentage`, `Batterie Current`, `Batterie Voltage`, `Heatsink`, `Motor Temp`, `PDO2_TX`, `Right Zapi Warning`
- Utilisé par : *(personne)*
- Ligne export : 34711 · id 52210

#### Right Zapi Warning  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `M1 - Zapi New Warning Code`, `Right Warning`, `Right Warning`, `Warning 1 - MEM`, `Event log: Electronic Logs`, `Measure group: Track Zapi Right`
- Ligne export : 34745 · id 52211

#### Right Warning  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Engine Right · Text=Error, stop battery, wait one minute, restart. · Channel=Right Zapi Warning
- Logique :
  - **Showing** = `Right Zapi Warning`
- Lit : ``, `Right Zapi Warning`
- Utilisé par : `Emmergency Stop Right`, `Promeion ZAPI`
- Ligne export : 34758 · id 59393

#### ZAPI_M1_Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(alarm present) OR (Emmergency Stop Right)`
- Lit : ``, `Emmergency Stop Right`, `alarm present`
- Utilisé par : `Error Wait`, `M1 - Error mode`, `Measure group: Track Zapi Right`
- Ligne export : 34804 · id 52645

#### Error Wait  `IDC`
- Propriétés : Toggle=No · Delay on=4000 · Delay off=0
- Logique :
  - **Activating** = `ZAPI_M1_Error mode`
- Lit : ``, `ZAPI_M1_Error mode`
- Utilisé par : `Emmergency Stop Right`, `Reset`
- Ligne export : 34854 · id 60281

#### Emmergency Stop Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Emmergency Stop Right) OR (PositiveFlank(Right Warning)) OR (PositiveFlank(Right Error)) OR (PositiveFlank(Emmergency Stop Left))`
  - **Blocking** = `(NegativeFlank(VARIATOR SUPER ON)) OR (PositiveFlank(Error Wait))`
- Lit : ``, `Emmergency Stop Left`, `Error Wait`, `Right Error`, `Right Warning`, `VARIATOR SUPER ON`
- Utilisé par : `Brake`, `Emmergency Stop Left`, `Enable`, `ZAPI_M1_Error mode`, `Measure group: Track Zapi Right`
- Ligne export : 34897 · id 60112

#### Enable  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed_Right [rpm] <> 0) OR (Enable Power Zapi)`
  - **Blocking** = `Emmergency Stop Right`
- Lit : ``, `Emmergency Stop Right`, `Enable Power Zapi`, `Speed_Right`
- Utilisé par : `Brake`, `Power`
- Ligne export : 34980 · id 52120

#### PDO1_TX  `IMAC`
- Logique :
  - **Controlling** = `0x180 + Node_ID`
- Lit : ``, `Node_ID`
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 35039 · id 52229

#### GFIN PDO1_TX  `GFIN`
- Propriétés : Identifier=PDO1_TX · Data length=8 · Timeout=3000 · Paged protocol={Not used} · Parameters={{Actual_Speed [Hz/10]; 0}; {Out MNC; 16}; {Stuffing; 31}; {Actual Current [A*5]; 56}; {Status Byte; 32}} · Module=ZAPI (Generic) · Module index=0
- Lit : `Actual Current`, `Actual_Speed`, `Out MNC`, `PDO1_TX`, `Status Byte`, `Stuffing`
- Utilisé par : `ZAPI_M1_CAN OK`
- Ligne export : 35082 · id 52237

#### Actual Current  `GPIN`
- Propriétés : Unit=A*5 · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `ZAPI_M1_Actual_current`
- Ligne export : 35113 · id 52324

#### ZAPI_M1_Actual_current  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result := Actual Current * 5
  ```
- Lit : `Actual Current`
- Utilisé par : `M1 - CURRENT`, `ZAPI_M1_Torque`, `Measure group: Track Zapi Right`
- Ligne export : 35125 · id 52325

#### Target_Speed_can  `MAC`
- Propriétés : Unit=Hz/10
- Logique :
  ```qcode
  Result := abs(Speed_Right) * 5 / 6
  ```
- Lit : `Speed_Right`
- Utilisé par : `Target_SPeed`
- Ligne export : 35143 · id 52151

#### Target_SPeed  `GPOUT`
- Propriétés : Input value=Target_Speed_can [Hz/10] · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Target_Speed_can`
- Utilisé par : `GFOUT - PDO1_RX`, `Measure group: Track Zapi Right`
- Ligne export : 35161 · id 52162

#### Actual_Speed  `GPIN`
- Propriétés : Unit=Hz/10 · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `ZAPI_M1_Actual_speed`, `ZAPI_M1_RUN`
- Ligne export : 35173 · id 52238

#### Power  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `Enable`
- Lit : ``, `Enable`
- Utilisé par : `Enable Power`, `Forward`, `Reverse`
- Ligne export : 35186 · id 59258

#### Forward  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed_Right [rpm] >= 0) OR (Enable Power Zapi)`
  - **Blocking** = `not(Power)`
- Lit : ``, `Enable Power Zapi`, `Power`, `Speed_Right`
- Utilisé par : `Forward Req`
- Ligne export : 35229 · id 52163

#### Reverse  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Speed_Right [rpm] < 0`
  - **Blocking** = `not(Power)`
- Lit : ``, `Power`, `Speed_Right`
- Utilisé par : `Reverse Req`
- Ligne export : 35289 · id 52171

#### Enable Power  `GPOUT`
- Propriétés : Input value=Power · Length=1 bit · Type=Unsigned integer
- Lit : `Power`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 35342 · id 52179

#### Forward Req  `GPOUT`
- Propriétés : Input value=Forward · Length=1 bit · Type=Unsigned integer
- Lit : `Forward`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 35353 · id 52180

#### Reverse Req  `GPOUT`
- Propriétés : Input value=Reverse · Length=1 bit · Type=Unsigned integer
- Lit : `Reverse`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 35364 · id 52181

#### GFOUT - PDO1_RX  `GFOUT`
- Propriétés : Identifier=PDO1_RX · Data length=8 · Send method=Continuously · Transmit rate=40 · Unused bits=Set to 0 · Parameters={{Target_SPeed [Hz/10]; 0}; {Enable Power; 16}; {Forward Req; 19}; {Reverse Req; 20}; {Stuffing; 31}; {Power Line; 17}; {Brake; 27}} · Module=ZAPI (Generic) · Module index=2
- Lit : `Brake`, `Enable Power`, `Forward Req`, `PDO1_RX`, `Power Line`, `Reverse Req`, `Stuffing`, `Target_SPeed`
- Utilisé par : `Stuffing`
- Ligne export : 35375 · id 52182

#### Stuffing  `IDC`
- Propriétés : Toggle=Yes · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank(GFOUT - PDO1_RX)`
- Lit : ``, `GFOUT - PDO1_RX`
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`, `Stuffing`
- Ligne export : 35412 · id 52183

#### Stuffing  `GPOUT`
- Propriétés : Input value=Stuffing · Length=1 bit · Type=Unsigned integer
- Lit : `Stuffing`
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`
- Ligne export : 35456 · id 52191

#### PDO1_RX  `IMAC`
- Logique :
  - **Controlling** = `0x200 + Node_ID`
- Lit : ``, `Node_ID`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 35467 · id 52193

#### Power Line  `GPOUT`
- Propriétés : Input value=1 · Length=1 bit · Type=Unsigned integer
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 35510 · id 52201

#### Brake  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `Enable`
  - **Blocking** = `Emmergency Stop Right`
- Lit : ``, `Emmergency Stop Right`, `Enable`
- Utilisé par : `Brake`, `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 35521 · id 59245

#### Brake  `GPOUT`
- Propriétés : Input value=Brake · Length=1 bit · Type=Unsigned integer
- Lit : `Brake`
- Utilisé par : `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 35571 · id 59579

#### Motor Temp  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M1_Motor_Temp`
- Ligne export : 35582 · id 52212

#### Heatsink  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M1_Heatsink`
- Ligne export : 35594 · id 52213

#### BDI Percentage  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 35606 · id 52214

#### Batterie Current  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M1_Batterie Current`
- Ligne export : 35618 · id 52215

#### Batterie Voltage  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M1_Batterie Voltage`
- Ligne export : 35630 · id 52216

#### Out MNC  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 35643 · id 52239

#### Stuffing  `GPIN`
- Propriétés : Length=1 bit · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`, `Stuffing`
- Ligne export : 35655 · id 52240

#### VARIATOR ON Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR SUPER ON`
- Lit : ``, `VARIATOR SUPER ON`
- Utilisé par : `Func State`
- Ligne export : 35667 · id 52574

#### Reset  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(Error Wait)`
- Lit : ``, `Error Wait`
- Utilisé par : `Func State`, `Adjust group: Master Electric`, `Single adjust item: Reset`
- Ligne export : 35710 · id 52585

#### Func State  `SMC`
- Propriétés : Default state name=Stop
- Fonction *Start* :
  - **Activating** = `VARIATOR ON Wait`
  - **Blocking** = `Reset`
- Fonction *Preprop* : (vide)
- Fonction *Reset* :
  - **Activating** = `Reset`
- Lit : ``, `Reset`, `VARIATOR ON Wait`
- Utilisé par : `Func`
- Ligne export : 35754 · id 52241

#### Func  `IP`
- Propriétés : Mode selector=Func State · Default mode: Stop={2} · Mode 1: Start={1} · Mode 2: Preprop={0x80} · Mode 3: Reset={0x81}
- Lit : `Func State`
- Utilisé par : `Func ID`
- Ligne export : 35856 · id 52257

#### Func ID  `GPOUT`
- Propriétés : Input value=Func · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Func`
- Utilisé par : `NMT`
- Ligne export : 35874 · id 52258

#### NMT  `GFOUT`
- Propriétés : Identifier=0 · Data length=8 · Send method=Continuously · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{Func ID; 0}; {Node ID; 8}} · Module=ZAPI (Generic) · Module index=1
- Lit : `Func ID`, `Node ID`
- Utilisé par : *(personne)*
- Ligne export : 35885 · id 52260

#### HeartBeat  `IMAC`
- Logique :
  - **Controlling** = `0x700 + Node_ID`
- Lit : ``, `Node_ID`
- Utilisé par : `GFIN HeartBeat`
- Ligne export : 35907 · id 52261

#### GFIN HeartBeat  `GFIN`
- Propriétés : Identifier=HeartBeat · Data length=1 · Timeout=1000 · Paged protocol={Not used} · Parameters={{HeartBeat State; 0}} · Module=ZAPI (Generic) · Module index=2
- Lit : `HeartBeat`, `HeartBeat State`
- Utilisé par : *(personne)*
- Ligne export : 35950 · id 52269

#### HeartBeat State  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN HeartBeat`, `ZAPI_M1_READY`
- Ligne export : 35969 · id 52270

#### ZAPI_M1_CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `GFIN PDO1_TX`
- Lit : ``, `GFIN PDO1_TX`
- Utilisé par : `M1 - CAN OK`, `Measure group: Track Zapi Right`
- Ligne export : 35981 · id 52271

#### ZAPI_M1_Batterie Voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `Batterie Voltage / 3,3333`
- Lit : ``, `Batterie Voltage`
- Utilisé par : `M1 - Voltage`, `Measure group: Track Zapi Right`
- Ligne export : 36024 · id 52279

#### ZAPI_M1_Batterie Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Batterie Current * 2`
- Lit : ``, `Batterie Current`
- Utilisé par : `Measure group: Track Zapi Right`
- Ligne export : 36068 · id 52287

#### ZAPI_M1_Motor_Temp  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Motor Temp - 40`
- Lit : ``, `Motor Temp`
- Utilisé par : `M1 - KTY`, `Measure group: Track Zapi Right`
- Ligne export : 36112 · id 52295

#### ZAPI_M1_Heatsink  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Heatsink`
- Lit : ``, `Heatsink`
- Utilisé par : `M1 - Heatsink`, `Measure group: Track Zapi Right`
- Ligne export : 36156 · id 52303

#### ZAPI_M1_Actual_speed  `MAC`
- Propriétés : Unit=rpm
- Logique :
  ```qcode
  Result := Actual_Speed * 6 / 5
  ```
- Lit : `Actual_Speed`
- Utilisé par : `M1 - Speed`, `Measure group: Track Zapi Right`
- Ligne export : 36198 · id 52311

#### Zapi alarm code  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 36216 · id 52346

#### flag alarm  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 36228 · id 52347

#### extra info alarm  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 36240 · id 52348

#### ZAPI_M1_READY  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `HeartBeat State`
- Lit : ``, `HeartBeat State`
- Utilisé par : `Measure group: Track Zapi Right`
- Ligne export : 36252 · id 52598

#### ZAPI_M1_RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Actual_Speed [Hz/10] <> 0`
- Lit : ``, `Actual_Speed`
- Utilisé par : `M1 - RUN`, `Measure group: Track Zapi Right`
- Ligne export : 36295 · id 52624

#### Warning 1 - MEM  `MEM`
- Propriétés : Input channel=Right Zapi Warning · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M1 - Zapi New Warning Code)`
- Lit : ``, `M1 - Zapi New Warning Code`, `Right Zapi Warning`
- Utilisé par : `M1 - Zapi New Warning Code`
- Ligne export : 36340 · id 59545

#### M1 - Zapi New Warning Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Right Zapi Warning <> Warning 1 - MEM`
  - **Blocking** = `Right Zapi Warning = 0`
- Lit : ``, `Right Zapi Warning`, `Warning 1 - MEM`
- Utilisé par : `Warning 1 - MEM`, `Event log: Electronic Logs`
- Ligne export : 36385 · id 59553

#### Error 1 - MEM  `MEM`
- Propriétés : Input channel=Right Zapi Error Code · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M1 - Zapi New Error Code)`
- Lit : ``, `M1 - Zapi New Error Code`, `Right Zapi Error Code`
- Utilisé par : `Error 1`, `M1 - Zapi New Error Code`
- Ligne export : 36439 · id 59662

#### M1 - Zapi New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Right Zapi Error Code <> Error 1 - MEM`
  - **Blocking** = `Right Zapi Error Code = 0`
- Lit : ``, `Error 1 - MEM`, `Right Zapi Error Code`
- Utilisé par : `Error 1 - MEM`, `Event log: Electronic Logs`
- Ligne export : 36484 · id 59670

#### Status Byte  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 36538 · id 60256

#### Right Warning  `GPOUT`
- Propriétés : Input value=Right Zapi Warning · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Right Zapi Warning`
- Utilisé par : `Emmergency Stop Right`, `Promeion ZAPI`
- Ligne export : 36550 · id 61765

#### Left Warning  `GPOUT`
- Propriétés : Input value=Left Zapi Warning · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Left Zapi Warning`
- Utilisé par : `Promeion ZAPI`
- Ligne export : 36562 · id 61769

#### Promeion ZAPI  `GFOUT`
- Propriétés : Identifier=0x7451250 · Data length=8 · Send method=On change · Unused bits=Set to 0 · Parameters={{Right Warning; 0}; {Left Warning; 16}} · Module=Proemion (Generic) · Module index=4
- Lit : `Left Warning`, `Right Warning`
- Utilisé par : *(personne)*
- Ligne export : 36574 · id 61766

#### ZAPI_M1_Torque  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `26 * courbe(((0,8 * ZAPI_M1_Actual_current [A]) / 33): {{0; 0}; {1; 1}; {2; 1,8}; {2,5; 2,18}; {3; 2,45}; {3,5; 2,62}; {4; 2,75}}, Freeze)`
- Lit : ``, `C`, `ZAPI_M1_Actual_current`
- Utilisé par : `M1 - Torque`
- Ligne export : 36596 · id 63021
