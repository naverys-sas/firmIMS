# MC42 app — mc.Electric

1335 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## mc.Electric — actif seulement si `Is_Electric mc`

#### E Variator Force  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `VARIATOR SUPER ON E mc`, `Single adjust item: Variator Force`
- Ligne export : 4333 · id 128796

#### E HVLP Pump Test  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `IMS Start Request E mc`, `Single adjust item: HVLP Pump Test`
- Ligne export : 4346 · id 128808

#### E With Auto Off Relay  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `Auto Off`, `E.Power Management System`, `Global Auto Off Timer`, `ShuntDown Turn Off`, `ShutDown Action E mc`, `System Shutdown`, `Single adjust item: With Auto Off Relay`
- Ligne export : 4359 · id 128809

#### F4 Off  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=VIEW BUTTON States md4/md3 mc
- Fonction *Stop* :
  - **Activating** = `B6 OFF Button 4ET OFF Sel`
- Fonction *Ready* : (vide)
- Fonction *Start* : (vide)
- Fonction *Start Free* : (vide)
- Lit : `B6 OFF Button 4ET OFF Sel`, `VIEW BUTTON States md4/md3 mc`
- Utilisé par : `System Shutdown`
- Ligne export : 4372 · id 128810

#### E Global Auto Off  `IP`
- Propriétés : Unit=h · Default mode={8}
- Utilisé par : `System Shutdown`, `Single adjust item: Global Auto Off`
- Ligne export : 4487 · id 128818

#### VARIATOR SUPER ON E mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(E Variator Force) OR (Battery OK IMS Engines)`
- Lit : `Battery OK IMS Engines`, `E Variator Force`
- Utilisé par : `Electric Engine State Feed-back`, `Emmergency Stop - Z.M1.Right`, `Emmergency Stop Left`, `Global Auto Off Timer`, `ON/OFF Var`, `ON/OFF Var gen`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `VARIATOR ON Wait`, `Var Power`, `debug vario on`, `Active le groupe: mc.Electric / E.MOTORS / E.M-Tracks`, `Active le groupe: mc.Electric / E.MOTORS / E.M3-Hydrau`, `Single adjust item: Speed Hydro Force`, `Statistics log: Electronic Stats logs`
- Ligne export : 4499 · id 131705

#### Global Auto Off Timer  `TMR`
- Propriétés : Type (Unit)=Hours [h] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `True`
  - **Resetting** = `(Charger CHARGING) OR (VARIATOR SUPER ON E mc) OR (PositiveFlank((4 = System Shutdown))) OR (not(E With Auto Off Relay)) OR (PositiveFlank((5 = System Shutdown)))`
- Lit : `Charger CHARGING`, `E With Auto Off Relay`, `System Shutdown`, `VARIATOR SUPER ON E mc`
- Utilisé par : `System Shutdown`
- Ligne export : 4549 · id 128841

#### System Shutdown  `IMSG`
- Propriétés : Show message=All · Dialog type=Confirmation · Header=System Shutdown · Text=In few seconds the system shuntdown. · Left button=Switch Off · Right button=Continue
- Logique :
  - **Showing** = `(Global Auto Off Timer [h] >= E Global Auto Off [h]) OR (F4 Off) OR (E With Auto Off Relay and Battery Ask ShutDown) OR (Power Down State C10 >= 1)`
  - **Hiding** = `Flank(MDs - Start Button Blocking Neutral E mc)`
- Lit : `Battery Ask ShutDown`, `E Global Auto Off`, `E With Auto Off Relay`, `F4 Off`, `Global Auto Off Timer`, `MDs - Start Button Blocking Neutral E mc`, `Power Down State C10`
- Utilisé par : `Auto Off`, `Global Auto Off Timer`, `ShutDown Confirmed`, `ShutDown Process Engaged`
- Ligne export : 4657 · id 128819

#### Auto Off  `IDC`
- Propriétés : Toggle=No · Delay on=120000 · Delay off=0
- Logique :
  - **Activating** = `System Shutdown = 1`
  - **Blocking** = `not(E With Auto Off Relay)`
- Lit : `E With Auto Off Relay`, `System Shutdown`
- Utilisé par : `Auto Off Confirmed`, `Adjust group: Master Config`, `Adjust group: Setup`
- Ligne export : 4747 · id 128875

#### Auto Off Confirmed  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Auto Off Confirmed) OR (PositiveFlank(Auto Off))`
- Lit : `Auto Off`
- Utilisé par : `ShutDown Confirmed`
- Ligne export : 4800 · id 133881

#### ShutDown Confirmed  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(System Shutdown = 2) OR (Auto Off Confirmed) OR (Auto Off - Timer 4ET [min] <= 0)`
- Lit : `Auto Off - Timer 4ET`, `Auto Off Confirmed`, `System Shutdown`
- Utilisé par : `Power Down E mc`, `ShuntDown Turn Off`, `ShutDown Process Engaged`, `ShutDown Wait`, `e ShuntDown Message mc`
- Ligne export : 4851 · id 128858

#### Power Down E mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `ShutDown Confirmed`
- Lit : `ShutDown Confirmed`
- Utilisé par : `IMS Start Request E mc`, `Keep ON`, `Power Down Wait`, `ShutDown Process Engaged`
- Ligne export : 4912 · id 128867

#### IMS Start Request E mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MDs - Start Button Blocking Neutral E mc) OR (E HVLP Pump Test)`
  - **Blocking** = `Power Down E mc`
- Lit : `E HVLP Pump Test`, `MDs - Start Button Blocking Neutral E mc`, `Power Down E mc`
- Utilisé par : `IMS Start Request confirmed`, `e Joystick to zero CMSG mc`
- Ligne export : 4955 · id 128831

#### SCREEN OK  `IDC`
> screen state 1 mean ok 
- Propriétés : Toggle=No · Delay on=0 · Delay off=20
- Logique :
  - **Activating** = `Screen_State ok mc`
- Lit : `Screen_State ok mc`
- Utilisé par : `PARKERs OK E mc`
- Ligne export : 5012 · id 167089

#### PARKERs OK E mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=20
- Logique :
  - **Activating** = `(64 = Status:MC) AND (SCREEN OK)`
- Lit : `SCREEN OK`, `Status:MC`
- Utilisé par : `IMS Asks Power`, `Keep ON`
- Ligne export : 5055 · id 128892

#### E Battery Force Discharge  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `IMS Asks Power`, `Single adjust item: Battery Force Discharge`
- Ligne export : 5107 · id 128901

#### IMS Start Request confirmed  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `IMS Start Request E mc`
- Lit : `IMS Start Request E mc`
- Utilisé par : `IMS Asks Power`
- Ligne export : 5120 · id 128902

#### BATT - Reset E mc  `IDC`
- Propriétés : Toggle=No · Delay on=300 · Delay off=0
- Logique :
  - **Activating** = `Battery Ask Reset`
- Lit : `Battery Ask Reset`
- Utilisé par : `Battery Reset E`, `IMS Asks Power`, `Keep ON`
- Ligne export : 5163 · id 128910

#### IMS Asks Power  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(E Battery Force Discharge) OR (IMS Start Request confirmed) OR (Keep ON)`
  - **Blocking** = `(not(PARKERs OK E mc)) OR (Power Down Wait) OR (BATT - Reset E mc)`
- Lit : `BATT - Reset E mc`, `E Battery Force Discharge`, `IMS Start Request confirmed`, `Keep ON`, `PARKERs OK E mc`, `Power Down Wait`
- Utilisé par : `IMS engines CMD`, `Keep ON`
- Ligne export : 5206 · id 128918

#### E Battery Management  `SP`
- Propriétés : Input channel=None · Default state name=Automatic · States={Keep On}
- Utilisé par : `Keep ON`, `Single adjust item: Battery Management`
- Ligne export : 5285 · id 128931

#### Keep ON  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Keep ON) OR ((1 = E Battery Management) and (PositiveFlank(IMS Asks Power)))`
  - **Blocking** = `(not(PARKERs OK E mc)) OR (Power Down E mc) OR (BATT - Reset E mc)`
- Lit : `BATT - Reset E mc`, `E Battery Management`, `IMS Asks Power`, `PARKERs OK E mc`, `Power Down E mc`
- Utilisé par : `IMS Asks Power`
- Ligne export : 5297 · id 128933

#### Power Down Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `Power Down E mc`
- Lit : `Power Down E mc`
- Utilisé par : `IMS Asks Power`
- Ligne export : 5388 · id 128947

#### ShutDown Wait  `IDC`
> Allows a shutdown if battery is standby or off
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `(ShutDown Confirmed) AND (Battery State Feed-Back <= 1)`
- Lit : `Battery State Feed-Back`, `ShutDown Confirmed`
- Utilisé par : `ShuntDown Turn Off`, `ShutDown Action E mc`, `ShutDown Process Engaged`
- Ligne export : 5431 · id 133842

#### ShutDown Process Engaged  `IDC`
> Digit raised when a shutdown process is active.
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(System Shutdown = 1) OR (ShutDown Confirmed) OR (Power Down E mc) OR (ShutDown Wait)`
- Lit : `Power Down E mc`, `ShutDown Confirmed`, `ShutDown Wait`, `System Shutdown`
- Utilisé par : `Shutdown CMD`
- Ligne export : 5483 · id 133900

#### Need to Charge Voltage Wait  `IDC`
- Propriétés : Toggle=No · Delay on=100000 · Delay off=100000
- Logique :
  - **Activating** = `(Need to Charge Voltage) OR (E Debug: Trig Low LTBat Voltage 12V)`
  - **Blocking** = `not(E Auto Charge 12V)`
- Lit : `E Auto Charge 12V`, `E Debug: Trig Low LTBat Voltage 12V`, `Need to Charge Voltage`
- Utilisé par : `DCDC Ask to charge E mc`
- Ligne export : 5549 · id 102186

#### DCDC Ask to charge E mc  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `(Need to Charge Voltage Wait) OR (Need Charge 12v dcdc on C10)`
- Lit : `Need Charge 12v dcdc on C10`, `Need to Charge Voltage Wait`
- Utilisé par : `DCDC CMD`
- Ligne export : 5607 · id 102196

#### e Joystick to zero CMSG mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Message · Header, English=e1152 Neutral position · Text, English=Please put joystick in neutral position before start engine.
- Logique :
  - **Showing** = `(PositiveFlank(Screen_Start/Stop mc)) AND (not(4ET Joystick Zero)) AND (not(IMS Start Request E mc))`
- Lit : `4ET Joystick Zero`, `IMS Start Request E mc`, `Screen_Start/Stop mc`
- Utilisé par : *(personne)*
- Ligne export : 44374 · id 133801

#### E Power Controler Force  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Var Power`, `Single adjust item: Power Controler Force`
- Ligne export : 44437 · id 133831

#### Var Power  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `(VARIATOR SUPER ON E mc) OR (E Power Controler Force)`
- Lit : `E Power Controler Force`, `VARIATOR SUPER ON E mc`
- Utilisé par : `sel batt reset/batt on or brake`, `sel var power`
- Ligne export : 44450 · id 133832

#### ShutDown Action E mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(ShutDown Wait)`
  - **Blocking** = `not(E With Auto Off Relay)`
- Lit : `E With Auto Off Relay`, `ShutDown Wait`
- Utilisé par : `K3 oldFan Exhaust / AutoOff`
- Ligne export : 44500 · id 133851

#### ShuntDown Turn Off  `CMSG`
- Propriétés : Show message=All · Dialog type=Confirmation · Header=Turn Off · Text=Please Turn Off the boat.
- Logique :
  - **Showing** = `(ShutDown Wait) AND (not(E With Auto Off Relay))`
  - **Hiding** = `NegativeFlank(ShutDown Confirmed)`
- Lit : `E With Auto Off Relay`, `ShutDown Confirmed`, `ShutDown Wait`
- Utilisé par : `e ShuntDown Message mc`
- Ligne export : 44552 · id 133860

#### e ShuntDown Message mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Message · Header, English=e1035 Shunt Down · Text, English=Please wait ...
- Logique :
  - **Showing** = `(ShutDown Confirmed) AND (not(ShuntDown Turn Off))`
  - **Hiding** = `(ShuntDown Turn Off) OR (NegativeFlank(ShutDown Confirmed))`
- Lit : `ShuntDown Turn Off`, `ShutDown Confirmed`
- Utilisé par : *(personne)*
- Ligne export : 44614 · id 133870

#### System Ask imminent Crash E mc  `IDC`
> System is about to crash, speed req is set to 0.
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `(Battery Ask Imminent Crash) OR (Tracks Engines Crash)`
- Lit : `Battery Ask Imminent Crash`, `Tracks Engines Crash`
- Utilisé par : `System Crash Signal`
- Ligne export : 44683 · id 133891

#### E Tension to charge 12V  `FP`
- Propriétés : Default mode={11,9}
- Utilisé par : `Need to Charge Voltage`, `Single adjust item: Tension to charge`
- Ligne export : 44733 · id 102173

#### Need to Charge Voltage  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((Inside(mc 12V Batt [V], 2, E Tension to charge 12V)))) OR (Need to Charge Voltage)`
  - **Blocking** = `mc 12V Batt [V] > 13,2`
- Lit : `E Tension to charge 12V`, `mc 12V Batt`
- Utilisé par : `Need to Charge Voltage Wait`
- Ligne export : 44745 · id 102174

#### E Auto Charge 12V  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `Need to Charge Voltage Wait`, `Adjust group: Setup`, `Single adjust item: E Auto Charge 12V`
- Ligne export : 44815 · id 102185

#### E Debug: Trig Low LTBat Voltage 12V  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Need to Charge Voltage Wait`, `Single adjust item: Debug: Trig Low LTBat Voltage`
- Ligne export : 44828 · id 102214

#### E Disable Crash Signal (NOVUM V1)  `DP`
> Does not cut the crash signal when battery is reset
- Propriétés : Default mode={False}
- Utilisé par : `Battery Reset E`, `Single adjust item: Disable Crash Signal (V1)`
- Ligne export : 44841 · id 102215

#### Battery Reset E  `IDC`
> Warning pin 44 sur x100, pin 60 CAB
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `BATT - Reset E mc`
  - **Blocking** = `E Disable Crash Signal (NOVUM V1)`
- Lit : `BATT - Reset E mc`, `E Disable Crash Signal (NOVUM V1)`
- Utilisé par : `Brake T/ Batt HT reset / tyva on SEL qcode`
- Ligne export : 44854 · id 102204

#### debug vario on  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(VARIATOR SUPER ON E mc) AND (debug screen)`
- Lit : `VARIATOR SUPER ON E mc`, `debug screen`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 51545 · id 229297

## mc.Electric / E.BATTERY
> Battery is the hub of several clients: charger, DCDC and IMS Engines. Ti receive a digital request for each of them and will allow commutation based on its state machine.

#### IMS engines CMD  `FGI`
- Propriétés : Input type=Digital · Input=IMS Asks Power · Default state name=OFF
- Lit : `IMS Asks Power`
- Utilisé par : `Battery OK IMS Engines`, `E.Power Management System`
- Ligne export : 5686 · id 128956

#### eb Battery max temp  `IP`
- Propriétés : Unit=°C · Default mode={55}
- Utilisé par : `Battery HIGHT TEMP`, `Single adjust item: Battery max temp`
- Ligne export : 5697 · id 128957

#### eb Battery Brand  `SP`
- Propriétés : Input channel=None · Default state name=BMW · States={NovumTech; Tyva; Kreisel}
- Utilisé par : `BMS_U_Trac`, `BMW tyva - Isolation Error`, `Batt - Iso_Resist`, `Battery CHARGE`, `Battery CHARGED`, `Battery InstantVoltage`, `Battery SOC`, `Battery STANDBY`, `CPI_BMS_U_Trac`, `Cell_T_max_Master`, `Current Bat`, `Error Iso_Resist`, `Flag Ground Fault Detection`, `HighCellVoltage check bmw`, `Is_BMW`, `Is_Kreisel`, `Is_Novum`, `Is_Tyva`, `IsoMonTriggerRecord tempo`, `LowCellVoltage check bmw`, `Max Discharge`, `e Battery Protection mc`, `eb Charge Max`, `eb Isolation Protection Level`, `ec Max Full Charge Voltage`, `Single adjust item: Battery Brand`
- Ligne export : 5709 · id 128958

#### Cell_T_max_Master  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW - Cell_T_max_Master [°C]`
- Fonction *NovumTech* :
  - **Controlling** = `Novum - MaxTemp [°C]`
- Fonction *Tyva* :
  - **Controlling** = `Tyva - MaxTemp [°C]`
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - Cell_T_max_Master [°C]`
- Lit : `BMW - Cell_T_max_Master`, `Kreisel - Cell_T_max_Master`, `Novum - MaxTemp`, `Tyva - MaxTemp`, `eb Battery Brand`
- Utilisé par : `Battery HIGHT TEMP`, `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Statistics log: Electronic Stats logs`
- Ligne export : 5723 · id 128960

#### Battery HIGHT TEMP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Cell_T_max_Master [°C] >= eb Battery max temp [°C]`
- Lit : `Cell_T_max_Master`, `eb Battery max temp`
- Utilisé par : `HT Battery NEED TO CHARGE`
- Ligne export : 5858 · id 128975

#### eb Battery Watchdog Delay  `IP`
- Propriétés : Unit=ms · Default mode={10000}
- Utilisé par : `Battery Watchdog`, `Single adjust item: Battery Watchdog Delay`
- Ligne export : 5903 · id 128983

#### eb Debug: Mute Watchdog  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Battery Watchdog`, `Single adjust item: Debug: Mute Watchdog`
- Ligne export : 5915 · id 128984

#### Is_Tyva  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `eb Battery Brand = 2`
- Lit : `eb Battery Brand`
- Utilisé par : `Battery CAN OK`, `Battery CAN OK delay`, `Is_bender_present`, `create new state tyva elec`, `Active le groupe: mc.Electric / E.BATTERY / E. Tyva`, `Event log: Balancing TYVA`, `Event log: Tyva Battery`, `Measure group: Battery Tyva`, `Single adjust item: test batt main on/off`
- Ligne export : 5928 · id 230182

#### Battery CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `(BMW CAN OK) OR (Novum - CAN OK) OR (tyva batt can ok idc and Is_Tyva) OR (tyva isomon can ok and Is_Tyva) OR (Kreisel - CAN OK)`
- Lit : `BMW CAN OK`, `Is_Tyva`, `Kreisel - CAN OK`, `Novum - CAN OK`, `tyva batt can ok idc`, `tyva isomon can ok`
- Utilisé par : `Battery CHARGE`, `Battery DRIVE MODE`, `Battery STANDBY`, `HT Battery NEED TO CHARGE`, `IDC Battery Protection`, `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Canbus`
- Ligne export : 5973 · id 129097

#### Battery DRIVE MODE  `IDC`
> Battery in DIscharge Mode
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `(BMW - DRIVE MODE) OR (Novum - DRIVE MODE) OR (Tyva discharge b3) OR (Tyva charge b4) OR (Kreisel - DRIVE MODE)`
  - **Blocking** = `not(Battery CAN OK)`
- Lit : `BMW - DRIVE MODE`, `Battery CAN OK`, `Kreisel - DRIVE MODE`, `Novum - DRIVE MODE`, `Tyva charge b4`, `Tyva discharge b3`
- Utilisé par : `Battery DRIVE mc`, `Battery STANDBY`, `Battery State Feed-Back`, `Battery crash counter timer`, `KTB K2 IDC - AUDIO/AUX 4`, `Save Iso_Resist`, `Event log: Electronic logs`, `Statistics log: Electronic Stats logs`
- Ligne export : 6048 · id 128985

#### Battery STANDBY  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=2000 · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Activating** = `BMW CAN OK`
  - **Blocking** = `Battery DRIVE MODE`
- Fonction *NovumTech* :
  - **Activating** = `Novum - STANDBY`
  - **Blocking** = `not(Battery CAN OK)`
- Fonction *Tyva* :
  - **Activating** = `Battery CAN OK`
  - **Blocking** = `Battery DRIVE MODE`
- Fonction *Kreisel* :
  - **Activating** = `Kreisel - CAN OK`
  - **Blocking** = `Battery DRIVE MODE`
- Lit : `BMW CAN OK`, `Battery CAN OK`, `Battery DRIVE MODE`, `Kreisel - CAN OK`, `Novum - STANDBY`, `eb Battery Brand`
- Utilisé par : `Battery State Feed-Back`
- Ligne export : 6127 · id 128995

#### Battery CHARGE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000 · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Activating** = `BMW - CHARGE`
  - **Blocking** = `not(Battery CAN OK)`
- Fonction *NovumTech* :
  - **Activating** = `Novum - CHARGE`
  - **Blocking** = `not(Battery CAN OK)`
- Fonction *Tyva* :
  - **Activating** = `tyva - CHARGE`
  - **Blocking** = `not(Battery CAN OK)`
- Fonction *Kreisel* :
  - **Activating** = `kreisel - CHARGE`
  - **Blocking** = `not(Battery CAN OK)`
- Lit : `BMW - CHARGE`, `Battery CAN OK`, `Novum - CHARGE`, `eb Battery Brand`, `kreisel - CHARGE`, `tyva - CHARGE`
- Utilisé par : `Battery State Feed-Back`, `Battery crash counter timer`, `Event log: Electronic logs`
- Ligne export : 6292 · id 129012

#### Battery State Feed-Back  `SMC`
- Propriétés : Default state name=OFF
- Fonction *STANDBY* :
  - **Activating** = `Battery STANDBY`
- Fonction *CHARGE* :
  - **Activating** = `Battery CHARGE`
- Fonction *DISCHARGE* :
  - **Activating** = `Battery DRIVE MODE`
- Lit : `Battery CHARGE`, `Battery DRIVE MODE`, `Battery STANDBY`
- Utilisé par : `Battery Ask ShutDown`, `Battery OK Charger`, `Battery OK IMS Engines`, `Battery State`, `Battery Watchdog`, `ShutDown Wait`
- Ligne export : 6460 · id 129029

#### Charger Running  `FGI`
- Propriétés : Input type=Digital · Input=Charger Running · Default state name=Default state
- Lit : `Charger Running`
- Utilisé par : `Battery Ask Reset`, `OK Open Battery Relay`
- Ligne export : 6562 · id 129045

#### Engines Running  `FGI`
- Propriétés : Input type=Digital · Input=E Engines Ready · Default state name=Default state
- Lit : `E Engines Ready`
- Utilisé par : `Battery Ask Reset`, `OK Open Battery Relay`
- Ligne export : 6573 · id 129046

#### OK Open Battery Relay  `IDC`
> Check that every device is turned off before opening battery relay
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(not(Charger Running)) AND (not(Engines Running))`
- Lit : `Charger Running`, `Engines Running`
- Utilisé par : `Battery Ask ShutDown`, `E.Battery CMD`
- Ligne export : 6584 · id 129047

#### Battery Watchdog  `IDC`
- Propriétés : Toggle=No · Delay on=eb Battery Watchdog Delay [ms] · Delay off=0 · Function selector=E.Battery CMD
- Fonction *Off* : (vide)
- Fonction *Stand by* :
  - **Activating** = `Battery State Feed-Back <> 1`
  - **Blocking** = `eb Debug: Mute Watchdog`
- Fonction *Discharge* :
  - **Activating** = `Battery State Feed-Back <> 3`
  - **Blocking** = `eb Debug: Mute Watchdog`
- Fonction *Charge* :
  - **Activating** = `Battery State Feed-Back <> 2`
  - **Blocking** = `eb Debug: Mute Watchdog`
- Lit : `Battery State Feed-Back`, `E.Battery CMD`, `eb Battery Watchdog Delay`, `eb Debug: Mute Watchdog`
- Utilisé par : `Battery ERROR DIGIT`, `Adjust group: Master Electric`
- Ligne export : 6636 · id 129056

#### IDC Battery Protection  `IDC`
> no action on iso error on novum based supplier recommandation 
- Propriétés : Toggle=No · Delay on=100000 · Delay off=0
- Logique :
  - **Activating** = `(Battery CAN OK) AND (BMW tyva - Isolation Error)`
  - **Blocking** = `(Batt - Iso_Resist [kOhm] = 0) AND (not(IsoMonTriggerRecord (iso value valid)))`
- Lit : `BMW tyva - Isolation Error`, `Batt - Iso_Resist`, `Battery CAN OK`, `IsoMonTriggerRecord (iso value valid)`
- Utilisé par : `Battery ERROR DIGIT`
- Ligne export : 6792 · id 210524

#### Battery ERROR DIGIT  `IDC`
> Battery Error, can be battery level (on a CAN Frame) or system level (Repeated error or no CAN)
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `(BMW - ERROR DIGIT) OR (Novum_ERROR DIGIT) OR (Battery Watchdog) OR (IDC Battery Protection) OR (tyva - ERROR DIGIT) OR (Kreisel - ERROR DIGIT)`
- Lit : `BMW - ERROR DIGIT`, `Battery Watchdog`, `IDC Battery Protection`, `Kreisel - ERROR DIGIT`, `Novum_ERROR DIGIT`, `tyva - ERROR DIGIT`
- Utilisé par : `E.Battery CMD`, `E.Power Management System`, `HT Battery NEED TO CHARGE`, `batt ok to start`, `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 6859 · id 129087

#### Battery LOW VOLTAGE ERROR DIGIT  `IDC`
> Battery Error, can be battery level (on a CAN Frame) or system level (Repeated error or no CAN)
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `Novum_LOW VOLTAGE ERROR  DIGIT`
- Lit : `Novum_LOW VOLTAGE ERROR  DIGIT`
- Utilisé par : `E.Battery CMD`, `E.Power Management System`
- Ligne export : 6937 · id 129353

#### E.Power Management System  `FSM`
- Propriétés : Store value=No · Resetting channel=Crash recovery flag
- État 0 **OFF**
  - transition *Battery ready* — Starting process when supply turned on (état cible non exporté par IQANdesign)
    - **Activating** = `Battery Wake up Delay Signal`
- État 1 **Standby** — Contactor Open, ready for operation
  - transition *Ask Charge* — Charger is ready. BLocked if repeated error on battery (état cible non exporté par IQANdesign)
    - **Activating** = `(Charger CMD) AND (HT Battery NEED TO CHARGE) AND (not(IMS engines CMD)) AND (not(Repeated errors locker)) AND (not(Shutdown CMD))`
  - transition *Ask Discharge* — Turn On IMS from Stand by OR DCDC Request AND charger is not requesting. Blocked if repeated erro on battery (état cible non exporté par IQANdesign)
    - **Activating** = `(IMS engines CMD or (DCDC CMD and (not(Charger CMD)))) AND (not(Repeated errors locker)) AND (not(Shutdown CMD))`
  - transition *batt off* (état cible non exporté par IQANdesign)
    - **Activating** = `(PositiveFlank(error 1st start to 1)) OR (PositiveFlank(test reset novum))`
- État 2 **Discharge** — Discharge mode for IMS or DCDC support
  - transition *Ask Stand by* — IMS is turned OF and DCDC don't need support (wether batteries are OK or charger is plugged) (état cible non exporté par IQANdesign)
    - **Activating** = `((not(IMS engines CMD)) and ((not(DCDC CMD)) or Charger CMD)) OR (Shutdown CMD)`
  - transition *Critical Discharge Error* (état cible non exporté par IQANdesign)
    - **Activating** = `(Battery ERROR DIGIT) OR (Battery LOW VOLTAGE ERROR DIGIT)`
- État 3 **Charge** — Charge mode, charger charging and DCDC support
  - transition *Ask direct Discharge* — Wait for charge to turn off (état cible non exporté par IQANdesign)
    - **Activating** = `IMS engines CMD`
  - transition *Critical Charge Error* (état cible non exporté par IQANdesign)
    - **Activating** = `Battery ERROR DIGIT`
  - transition *Charger Off* (état cible non exporté par IQANdesign)
    - **Activating** = `(not(Charger CMD)) OR (Shutdown CMD)`
  - transition *End Of Charge* (état cible non exporté par IQANdesign)
    - **Activating** = `Battery CHARGED`
- État 4 **Crash** — Battery Error at system level: the system tries to shutdown properly
- État 5 **Charge Aborted** — Charge is aborted to turn On IMS, message
  - transition *Battery Error* (état cible non exporté par IQANdesign)
    - **Activating** = `(Battery ERROR DIGIT) OR (Battery LOW VOLTAGE ERROR DIGIT)`
  - transition *Ready for discharge* (état cible non exporté par IQANdesign)
    - **Activating** = `e Abort Charging mc = 2`
  - transition *Powerdown* (état cible non exporté par IQANdesign)
    - **Activating** = `Shutdown CMD`
- État 6 **Auto Off**
  - transition *No ShutDown* (état cible non exporté par IQANdesign)
    - **Activating** = `(NegativeFlank(Shutdown CMD)) OR (not(E With Auto Off Relay))`
- Lit : `Battery CHARGED`, `Battery ERROR DIGIT`, `Battery LOW VOLTAGE ERROR DIGIT`, `Battery Wake up Delay Signal`, `Charger CMD`, `Crash recovery flag`, `DCDC CMD`, `E With Auto Off Relay`, `HT Battery NEED TO CHARGE`, `IMS engines CMD`, `Repeated errors locker`, `Shutdown CMD`, `e Abort Charging mc`, `error 1st start to 1`, `test reset novum`
- Utilisé par : `BUTTON DRIVE 4ET`, `Battery Ask Imminent Crash`, `Battery Ask Reset`, `Battery Ask ShutDown`, `Battery Crash Counter`, `Battery OK Charger`, `Battery OK DCDC`, `Battery OK IMS Engines`, `Battery Wake up Delay Signal`, `Crash recovery flag`, `E.Battery CMD`, `Show crash jauge`, `Show standby jauge`, `Show symbole batterie 400V`, `VIEW BAT Charging d3`, `VIEW BAT Ready d3`, `VIEW BAT Run d3`, `e Abort Charging mc`, `show charge jauge`, `show discharge jauge`
- Ligne export : 6980 · id 129202

#### Crash recovery flag  `IDC`
> Allows to exit from a crash state of the battery after 5s
- Propriétés : Toggle=No · Delay on=3000 · Delay off=0
- Logique :
  - **Activating** = `E.Power Management System = 4`
- Lit : `E.Power Management System`
- Utilisé par : `E.Power Management System`
- Ligne export : 7587 · id 129308

#### eb Charging Force  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `HT Battery NEED TO CHARGE`, `Single adjust item: Charging Force`
- Ligne export : 7632 · id 129121

#### Battery Filtered Voltage  `SFC`
- Propriétés : Input channel=Battery InstantVoltage [V] · Enable=Yes · Type=Slopes · Slopes={{100; 25}; {50; 50}}
- Lit : `Battery InstantVoltage`
- Utilisé par : `Battery POWER`, `Battery POWER filter`, `HT Battery NEED TO CHARGE`
- Ligne export : 7645 · id 130181

#### HT Battery NEED TO CHARGE  `IDC`
> Turn to True if the battery needs a charging, based on SOC level and general functionning
- Propriétés : Toggle=No · Delay on=15000 · Delay off=0
- Logique :
  - **Activating** = `(eb Charging Force) OR (Battery Filtered Voltage [V] <= (ec Max Full Charge Voltage [V] - 5))`
  - **Blocking** = `(Battery ERROR DIGIT) OR (Battery HIGHT TEMP) OR (not(Battery CAN OK))`
- Lit : `Battery CAN OK`, `Battery ERROR DIGIT`, `Battery Filtered Voltage`, `Battery HIGHT TEMP`, `eb Charging Force`, `ec Max Full Charge Voltage`
- Utilisé par : `E.Power Management System`
- Ligne export : 7663 · id 129122

#### Battery SOC  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW - SOC [%]`
- Fonction *NovumTech* :
  - **Controlling** = `Novum - SOC [%]`
- Fonction *Tyva* :
  - **Controlling** = `Soc Tyva onoff CHECK`
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - SOC [%]`
- Lit : `BMW - SOC`, `Kreisel - SOC`, `Novum - SOC`, `Soc Tyva onoff CHECK`, `eb Battery Brand`
- Utilisé par : `Battery CHARGED`, `Battery SOC Customer`, `Measure group: Track Engine Sev/Zapi`
- Ligne export : 7746 · id 129135

#### eb Charge Max  `IP`
- Propriétés : Unit=% · Mode selector=eb Battery Brand · Default mode: BMW={100} · Mode 1: NovumTech={95} · Mode 2: Tyva={100} · Mode 3: Kreisel={100}
- Lit : `eb Battery Brand`
- Utilisé par : `Battery CHARGED`, `Single adjust item: Charge Max`
- Ligne export : 7881 · id 129158

#### Battery CHARGED  `IDC`
> Toggles On When Battery is charged. The delay Off allows to keep the information even when the battery frame is resetted
- Propriétés : Toggle=No · Delay on=300 · Delay off=300 · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Activating** = `(Battery SOC [%] >= eb Charge Max [%]) OR (Charger asks End Of Charge)`
- Fonction *NovumTech* :
  - **Activating** = `Novum_EndOfCharge OR (Battery SOC [%] >= eb Charge Max [%]) OR (Charger asks End Of Charge)`
- Fonction *Tyva* :
  - **Activating** = `(Battery SOC [%] >= eb Charge Max [%]) OR (Charger asks End Of Charge)`
- Fonction *Kreisel* : (vide)
- Lit : `Battery SOC`, `Charger asks End Of Charge`, `Novum_EndOfCharge`, `eb Battery Brand`, `eb Charge Max`
- Utilisé par : `E.Power Management System`, `Event log: Electronic logs`
- Ligne export : 7899 · id 129160

#### Charger CMD  `FGI`
- Propriétés : Input type=Digital · Input=Charger REQ · Default state name=Default state
- Lit : `Charger REQ`
- Utilisé par : `Battery OK Charger`, `E.Power Management System`
- Ligne export : 8062 · id 129178

#### DCDC CMD  `FGI`
- Propriétés : Input type=Digital · Input=DCDC Ask to charge E mc · Default state name=StandBy
- Lit : `DCDC Ask to charge E mc`
- Utilisé par : `E.Power Management System`
- Ligne export : 8073 · id 129182

#### Shutdown CMD  `FGI`
- Propriétés : Input type=Digital · Input=ShutDown Process Engaged · Default state name=OFF
- Lit : `ShutDown Process Engaged`
- Utilisé par : `Battery Wake up Delay Signal`, `E.Power Management System`
- Ligne export : 8084 · id 129185

#### Battery Crash Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank((E.Power Management System = 4))`
  - **Resetting** = `Battery crash counter timer [s] = 0`
- Lit : `Battery crash counter timer`, `E.Power Management System`
- Utilisé par : `Repeated errors locker`
- Ligne export : 8095 · id 129316

#### Repeated errors locker  `IDC`
> Block the battery in stand by mode after several faults until ECU is restarted
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Battery Crash Counter > 2`
- Lit : `Battery Crash Counter`
- Utilisé par : `E.Power Management System`, `VIEW BAT Ready d3`, `e Critical Battery Error mc`
- Ligne export : 8165 · id 129328

#### eb Battery Wake Up Delay Value  `IP`
> Delay from OFF to STANDBY state of the battery. Used also by Battery Charged signal to ensure info will be kept even during the shutdown, but no longer.
- Propriétés : Unit=ms · Default mode={3000}
- Utilisé par : `Battery Wake up Delay Signal`
- Ligne export : 8210 · id 129159

#### Battery Wake up Delay Signal  `IDC`
> Pause between Off and standby state of the battery
- Propriétés : Toggle=No · Delay on=eb Battery Wake Up Delay Value [ms] · Delay off=0
- Logique :
  - **Activating** = `E.Power Management System = 0`
  - **Blocking** = `Shutdown CMD`
- Lit : `E.Power Management System`, `Shutdown CMD`, `eb Battery Wake Up Delay Value`
- Utilisé par : `E.Power Management System`
- Ligne export : 8222 · id 129336

#### e Abort Charging mc  `IMSG`
> User message to confirm or not switch from charge to discharge
- Propriétés : Show message=All · Dialog type=Confirmation · Header, English=e1169 Abort Charging · Text, English=Starting IMS will stop the charge. Mind to regularly proceed to a full charge for battery lifetime saving. · Left button=OK
- Logique :
  - **Showing** = `E.Power Management System = 5`
- Lit : `E.Power Management System`
- Utilisé par : `E.Power Management System`
- Ligne export : 8274 · id 129345

#### Error Iso_Resist  `IDC`
> 1s to display error, 100s to cut power
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0 · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Activating** = `BMW tyva - Isolation Error`
- Fonction *NovumTech* :
  - **Activating** = `Novum - Isolation Error`
- Fonction *Tyva* :
  - **Activating** = `(BMW tyva - Isolation Error) AND (system failure tyva isomon com)`
- Fonction *Kreisel* : (vide)
- Lit : `BMW tyva - Isolation Error`, `Novum - Isolation Error`, `eb Battery Brand`, `system failure tyva isomon com`
- Utilisé par : `e Battery Protection mc`, `error 1st start to 1`
- Ligne export : 8324 · id 130276

#### error 1st start to 1  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `Error Iso_Resist`
- Lit : `Error Iso_Resist`
- Utilisé par : `E.Power Management System`
- Ligne export : 8460 · id 233779

#### test reset novum  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `E.Power Management System`
- Ligne export : 8503 · id 233799

#### E.Battery CMD  `FSM`
> State machine to define battery command based on system request and system state
- Propriétés : Store value=No
- État 0 **Off** — Battery is Off, No CAN Msg, Error cleared
  - transition *Boat Start* (état cible non exporté par IQANdesign)
    - **Activating** = `E.Power Management System = 1`
- État 1 **Stand by** — CAN Dialing but contactor Open
  - transition *Reset* (état cible non exporté par IQANdesign)
    - **Activating** = `((E.Power Management System = 0) or (E.Power Management System = 4)) AND (OK Open Battery Relay)`
  - transition *Discharge Request* (état cible non exporté par IQANdesign)
    - **Activating** = `(E.Power Management System = 2) AND (not(Battery ERROR DIGIT)) AND (not(Battery LOW VOLTAGE ERROR DIGIT))`
  - transition *Charge Request* (état cible non exporté par IQANdesign)
    - **Activating** = `(E.Power Management System = 3) AND (not(Battery ERROR DIGIT))`
- État 2 **Discharge** — CAN Dialing, contactor closed for discharge
  - transition *Engines Off* (état cible non exporté par IQANdesign)
    - **Activating** = `((E.Power Management System = 3) or (E.Power Management System = 1)) AND (OK Open Battery Relay)`
  - transition *Crash* (état cible non exporté par IQANdesign)
    - **Activating** = `((E.Power Management System = 0) or (E.Power Management System = 4)) AND (OK Open Battery Relay)`
- État 3 **Charge** — CAN Dialing, contactor closed for charge
  - transition *Charger Off* (état cible non exporté par IQANdesign)
    - **Activating** = `(E.Power Management System = 1) AND (OK Open Battery Relay)`
  - transition *Abort charge* (état cible non exporté par IQANdesign)
    - **Activating** = `(E.Power Management System = 2) AND (OK Open Battery Relay) AND (not(Battery LOW VOLTAGE ERROR DIGIT))`
  - transition *End of Charge* (état cible non exporté par IQANdesign)
    - **Activating** = `(((E.Power Management System = 0) or (E.Power Management System = 4)) or (E.Power Management System = 6)) AND (OK Open Battery Relay)`
- Lit : `Battery ERROR DIGIT`, `Battery LOW VOLTAGE ERROR DIGIT`, `E.Power Management System`, `OK Open Battery Relay`
- Utilisé par : `Battery OK DCDC`, `Battery State Request`, `Battery State Request`, `Battery State Request`, `Battery State Request tyva`, `Battery Watchdog`
- Ligne export : 8516 · id 129361

#### Batt - Iso_Resist  `MAC`
- Propriétés : Unit=kOhm · Limiting object group=Signed · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Controlling** = `IsoMonResistance BMW`
- Fonction *NovumTech* :
  - **Controlling** = `5000`
- Fonction *Tyva* :
  - **Controlling** = `Batt - Iso_Resist - tyva [kOhm]`
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - Iso_Resist [kOhm]`
- Lit : `Batt - Iso_Resist - tyva`, `IsoMonResistance BMW`, `Kreisel - Iso_Resist`, `eb Battery Brand`
- Utilisé par : `BMW tyva - Isolation Error`, `Flag Ground Fault Detection`, `IDC Battery Protection`, `Last Isolation value BMW/tyva`, `e Ground Fault message`, `r isomon Tyva onoff`, `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Battery BMW`
- Ligne export : 8984 · id 129580

#### IsoMonTriggerRecord tempo  `FP`
- Propriétés : Unit=ms · Mode selector=eb Battery Brand · Default mode: BMW={500} · Mode 1: NovumTech={500} · Mode 2: Tyva={40000} · Mode 3: Kreisel={500}
- Lit : `eb Battery Brand`
- Utilisé par : `IsoMonTriggerRecord (iso value valid)`
- Ligne export : 9119 · id 232317

#### IsoMonTriggerRecord (iso value valid)  `IDC`
> Set to 1 when Isolation value can be considered as relevant
- Propriétés : Toggle=No · Delay on=IsoMonTriggerRecord tempo [ms] · Delay off=0
- Logique :
  - **Activating** = `(IsoMonState bmw = 3) OR (tyva batt can ok idc and (not(iso value not valid tyva))) OR (kreisel isomon ok)`
- Lit : `IsoMonState bmw`, `IsoMonTriggerRecord tempo`, `iso value not valid tyva`, `kreisel isomon ok`, `tyva batt can ok idc`
- Utilisé par : `Flag Ground Fault Detection`, `IDC Battery Protection`, `Last Isolation value BMW/tyva`, `isomon Tyva batt can ok`, `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 9137 · id 130130

#### eb Isolation Protection Level  `IP`
- Propriétés : Unit=kOhm · Mode selector=eb Battery Brand · Default mode: BMW={1000} · Mode 1: NovumTech={999} · Mode 2: Tyva={1000} · Mode 3: Kreisel={1000}
- Lit : `eb Battery Brand`
- Utilisé par : `BMW tyva - Isolation Error`, `Single adjust item: Isolation Protection Level`
- Ligne export : 9206 · id 130171

#### Last Isolation value BMW/tyva  `MEM`
> Value is valid when IsoMonStatus is OK
- Propriétés : Input channel=Batt - Iso_Resist [kOhm] · Action=Replace · Store value=No · Reset value=5000
- Logique :
  - **Activating** = `IsoMonTriggerRecord (iso value valid)`
- Lit : `Batt - Iso_Resist`, `IsoMonTriggerRecord (iso value valid)`
- Utilisé par : `BMW tyva - Isolation Error`, `r isomon Tyva onoff`, `Event log: Battery Isolation`
- Ligne export : 9224 · id 130138

#### BMW tyva - Isolation Error  `IDC`
> Set to 1 when Isolation value is too low
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Activating** = `Last Isolation value BMW/tyva [kOhm] <= eb Isolation Protection Level [kOhm]`
- Fonction *NovumTech* :
  - **Activating** = `False`
- Fonction *Tyva* :
  - **Activating** = `Last Isolation value BMW/tyva [kOhm] <= eb Isolation Protection Level [kOhm]`
- Fonction *Kreisel* :
  - **Activating** = `Batt - Iso_Resist [kOhm] <= eb Isolation Protection Level [kOhm]`
- Lit : `Batt - Iso_Resist`, `Last Isolation value BMW/tyva`, `eb Battery Brand`, `eb Isolation Protection Level`
- Utilisé par : `Error Iso_Resist`, `IDC Battery Protection`, `flag true pb isomon tyva`, `Event log: Battery Isolation`
- Ligne export : 9268 · id 130163

#### Battery InstantVoltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW_-_Battery_InstantVoltage [V]`
- Fonction *NovumTech* :
  - **Controlling** = `Novum - BatteryVoltage [V]`
- Fonction *Tyva* :
  - **Controlling** = `BatteryVoltage Tyva`
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - Battery InstantVoltage [V]`
- Lit : `BMW_-_Battery_InstantVoltage`, `BatteryVoltage Tyva`, `Kreisel - Battery InstantVoltage`, `Novum - BatteryVoltage`, `eb Battery Brand`
- Utilisé par : `Battery Filtered Voltage`, `MD4-10 page: INFO`, `MD4-5 page: INFO`, `MD4-5 page: MAIN Elec`, `Measure group: Track Engine Sev/Zapi`
- Ligne export : 9410 · id 129106

#### eb Battery Error Clearance Delay  `IP`
> Battery error counter is set to 0 after this delay in drive mode
- Propriétés : Unit=s · Default mode={120}
- Utilisé par : `Battery crash counter timer`, `Single adjust item: Battery Error Clearance Delay`
- Ligne export : 9545 · id 129186

#### Battery crash counter timer  `TMR`
> Battery error counter is set to 0 after this delay in drive 
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=eb Battery Error Clearance Delay [s]
- Logique :
  - **Decreasing** = `(Battery DRIVE MODE) OR (Battery CHARGE)`
  - **Resetting** = `((not(Battery DRIVE MODE)) and (not(Battery CHARGE))) OR (Battery crash counter timer [s] <= 0)`
- Lit : `Battery CHARGE`, `Battery DRIVE MODE`, `eb Battery Error Clearance Delay`
- Utilisé par : `Battery Crash Counter`
- Ligne export : 9557 · id 129187

#### max soc customer  `FP`
- Propriétés : Unit=% · Default mode={89}
- Utilisé par : `Battery SOC Customer`, `Adjust group: Master Features`, `Single adjust item: max soc customer`
- Ligne export : 9650 · id 232862

#### Battery SOC Customer  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin((Round(Battery SOC [%])): 5->0, max soc customer [%]->100, Freeze)`
- Lit : `Battery SOC`, `max soc customer`
- Utilisé par : `SOC`, `VIEW SOC md3 d3`, `MD4-10 page: INFO`, `MD4-5 page: INFO`, `MD4-5 page: MAIN Elec`
- Ligne export : 9662 · id 129150

#### Start 3 s  `IDC`
> Wait 3s after the supply of the ECU to start to communicate with the battery
- Propriétés : Toggle=No · Delay on=3000 · Delay off=0
- Logique :
  - **Activating** = `True`
- Utilisé par : *(personne)*
- Ligne export : 9717 · id 129441

#### Is_BMW  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `eb Battery Brand = 0`
- Lit : `eb Battery Brand`
- Utilisé par : `Is_bender_present`, `Active le groupe: mc.Electric / E.BATTERY / E.BMW`, `Event log: BMW Battery`, `Measure group: Battery BMW`, `Single adjust item: Force BMW Charge`
- Ligne export : 9760 · id 129449

#### Current Bat  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW - CURRENT [A]`
- Fonction *NovumTech* :
  - **Controlling** = `Novum - BatteryCurrent [A]`
- Fonction *Tyva* :
  - **Controlling** = `M1 - CURRENT [A] + M2 - CURRENT [A]`
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - CURRENT [A]`
- Lit : `BMW - CURRENT`, `Kreisel - CURRENT`, `M1 - CURRENT`, `M2 - CURRENT`, `Novum - BatteryCurrent`, `eb Battery Brand`
- Utilisé par : `Battery CURRENT`, `Cuurent Bat (ABS)`, `Measure group: Track Engine Sev/Zapi`
- Ligne export : 12461 · id 130182

#### Battery CURRENT  `SFC`
- Propriétés : Input channel=Current Bat [A] · Enable=Yes · Type=Filter · Filter=90
- Lit : `Current Bat`
- Utilisé par : `Bat - 100A-125A`, `Bat - 1A-25A`, `Bat - 25A-50A`, `Bat - 50A-75A`, `Bat - 75A-100A`, `Bat - up to 125A`, `Battery CURRENT filter`, `Battery POWER`
- Ligne export : 12598 · id 130197

#### BMS_U_Trac  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW_-_U_Trac [V]`
- Fonction *NovumTech* :
  - **Controlling** = `Novum - BatteryVoltage [V]`
- Fonction *Tyva* :
  - **Controlling** = `BatteryVoltage Tyva`
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - U_Trac [V]`
- Lit : `BMW_-_U_Trac`, `BatteryVoltage Tyva`, `Kreisel - U_Trac`, `Novum - BatteryVoltage`, `eb Battery Brand`
- Utilisé par : `MD4-10 page: INFO`
- Ligne export : 12610 · id 130198

#### Battery POWER  `MAC`
- Propriétés : Unit=kW · Limiting object group=Signed
- Logique :
  - **Controlling** = `(Battery Filtered Voltage [V] * Battery CURRENT [A]) / 1000`
- Lit : `Battery CURRENT`, `Battery Filtered Voltage`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Battery Tyva`
- Ligne export : 12745 · id 130213

#### eb Battery hight temp  `IP`
- Propriétés : Unit=°C · Default mode={50}
- Utilisé par : `Single adjust item: Battery hight temp`
- Ligne export : 12798 · id 130222

#### Bat - 25A-50A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(25 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 50)`
- Lit : `Battery CURRENT`
- Utilisé par : *(personne)*
- Ligne export : 12810 · id 130223

#### Bat - 50A-75A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(50 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 75)`
- Lit : `Battery CURRENT`
- Utilisé par : *(personne)*
- Ligne export : 12864 · id 130232

#### Bat - 75A-100A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(75 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 100)`
- Lit : `Battery CURRENT`
- Utilisé par : *(personne)*
- Ligne export : 12918 · id 130241

#### Bat - 100A-125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(100 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 125)`
- Lit : `Battery CURRENT`
- Utilisé par : *(personne)*
- Ligne export : 12972 · id 130250

#### Bat - up to 125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `125 < Battery CURRENT [A]`
- Lit : `Battery CURRENT`
- Utilisé par : *(personne)*
- Ligne export : 13026 · id 130259

#### Bat - 1A-25A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(1 < Battery CURRENT [A]) AND (Battery CURRENT [A] <= 25)`
- Lit : `Battery CURRENT`
- Utilisé par : *(personne)*
- Ligne export : 13071 · id 130267

#### error 1st start  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(Novum - Isolation Error)`
  - **Resetting** = `Reset Startup`
- Lit : `Novum - Isolation Error`, `Reset Startup`
- Utilisé par : `e Battery Protection mc`, `Event log: Battery Isolation`, `Event log: Novum battery`
- Ligne export : 13125 · id 233765

#### e Battery Protection mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=e1170 Battery Isolation · Text, English=Battery Isolation is low. Please secure the boat and contact your service center · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Showing** = `Error Iso_Resist`
- Fonction *NovumTech* :
  - **Showing** = `error 1st start > 1`
- Fonction *Tyva* :
  - **Showing** = `Error Iso_Resist`
- Fonction *Kreisel* : (vide)
- Lit : `Error Iso_Resist`, `eb Battery Brand`, `error 1st start`
- Utilisé par : *(personne)*
- Ligne export : 13184 · id 130291

#### LowCellVoltage check bmw  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed · Function selector=eb Battery Brand
- Fonction *BMW* : (vide)
- Fonction *NovumTech* :
  - **Controlling** = `Novum - MinCellVoltage [mV]`
- Fonction *Tyva* :
  - **Controlling** = `VoltageCellMin Tyva V`
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - LowCellVoltage [mV]`
- Lit : `Kreisel - LowCellVoltage`, `Novum - MinCellVoltage`, `VoltageCellMin Tyva V`, `eb Battery Brand`
- Utilisé par : `DiffCellVoltage`
- Ligne export : 13318 · id 130299

#### HighCellVoltage check bmw  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed · Function selector=eb Battery Brand
- Fonction *BMW* : (vide)
- Fonction *NovumTech* :
  - **Controlling** = `Novum - MaxCellVoltage [mV]`
- Fonction *Tyva* :
  - **Controlling** = `VoltageCellMax Tyva V`
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel - HighCellVoltage [mV]`
- Lit : `Kreisel - HighCellVoltage`, `Novum - MaxCellVoltage`, `VoltageCellMax Tyva V`, `eb Battery Brand`
- Utilisé par : `DiffCellVoltage`
- Ligne export : 13446 · id 130313

#### Max Discharge  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW- Max Current [A]`
- Fonction *NovumTech* :
  - **Controlling** = `Novum - MaxDischargeBatteryCurrent [A]`
- Fonction *Tyva* :
  - **Controlling** = `IMD Tyva Max curr`
- Fonction *Kreisel* :
  - **Controlling** = `Kreisel- Max Current [A]`
- Lit : `BMW- Max Current`, `IMD Tyva Max curr`, `Kreisel- Max Current`, `Novum - MaxDischargeBatteryCurrent`, `eb Battery Brand`
- Utilisé par : `Current Limiting`
- Ligne export : 13574 · id 130327

#### eb Current Limiting - Error  `FP`
- Propriétés : Unit=A · Default mode={10}
- Utilisé par : `Current Limiting`, `Single adjust item: Current Limiting - Error`
- Ligne export : 13709 · id 130342

#### eb Current Limiting - Increase  `FP`
- Propriétés : Unit=%/s · Default mode={10}
- Utilisé par : `Current Limiting`, `Single adjust item: Current Limiting - Increase`
- Ligne export : 13721 · id 130343

#### eb Current Limiting - Decrease  `FP`
- Propriétés : Unit=%/s · Default mode={100}
- Utilisé par : `Current Limiting`, `Single adjust item: Current Limiting - Decrease`
- Ligne export : 13733 · id 130344

#### Cuurent Bat (ABS)  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Abs(Current Bat [A])`
- Lit : `Current Bat`
- Utilisé par : `Current Limiting`
- Ligne export : 13745 · id 130345

#### Current Limiting  `ILC`
- Propriétés : Output=Normal · Enable=Yes · Input channel=Cuurent Bat (ABS) [A] · Start reduction at=Max Discharge [A] · Max error=eb Current Limiting - Error [A] · Max increase speed=eb Current Limiting - Increase [%/s] · Max decrease speed=eb Current Limiting - Decrease [%/s]
- Lit : `Cuurent Bat (ABS)`, `Max Discharge`, `eb Current Limiting - Decrease`, `eb Current Limiting - Error`, `eb Current Limiting - Increase`
- Utilisé par : `e Math Left`, `e Math Right`, `Adjust group: Master Battery`
- Ligne export : 13788 · id 130353

#### DiffCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed
- Logique :
  - **Controlling** = `Abs((LowCellVoltage check bmw [mV] - HighCellVoltage check bmw [mV]))`
- Lit : `HighCellVoltage check bmw`, `LowCellVoltage check bmw`
- Utilisé par : *(personne)*
- Ligne export : 13803 · id 130354

#### Is_Novum  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `eb Battery Brand = 1`
- Lit : `eb Battery Brand`
- Utilisé par : `Active le groupe: mc.Electric / E.BATTERY / E.NovumTech`, `Event log: Novum battery`, `MD4-5 page: INFO`, `Measure group: Battery NovumTech`, `Single adjust item: Debug: Mute Battery Error`, `Single adjust item: Debug: Test End Of Charge`, `Single adjust item: Debug: Trig Battery Error`, `Single adjust item: Debug: Trig Battery Low Voltage Error`, `Single adjust item: Disable Crash Signal (V1)`, `Single adjust item: Trig Debug Cell Voltage`
- Ligne export : 13855 · id 130363

#### eb Debug: Trig Battery Error  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Novum_ERROR DIGIT`, `Single adjust item: Debug: Trig Battery Error`
- Ligne export : 13900 · id 130478

#### eb Debug: Mute Battery Error  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Novum_ERROR DIGIT`, `Novum_LOW VOLTAGE ERROR  DIGIT`, `Single adjust item: Debug: Mute Battery Error`
- Ligne export : 13913 · id 130479

#### eb Debug: Trig Battery Low Voltage Error  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Novum_LOW VOLTAGE ERROR  DIGIT`, `Single adjust item: Debug: Trig Battery Low Voltage Error`
- Ligne export : 13926 · id 130667

#### Battery OK Charger  `IDC`
> Charger can start charging after battery is in discharge mode
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `(E.Power Management System = 3) AND (Charger CMD)`
  - **Blocking** = `Battery State Feed-Back <> 2`
- Lit : `Battery State Feed-Back`, `Charger CMD`, `E.Power Management System`
- Utilisé par : `Ask Charging CMD`
- Ligne export : 16431 · id 130695

#### Battery OK IMS Engines  `IDC`
> IMS is turned ON as soon as battery is connected
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `(E.Power Management System = 2) AND (IMS engines CMD)`
  - **Blocking** = `Battery State Feed-Back <> 3`
- Lit : `Battery State Feed-Back`, `E.Power Management System`, `IMS engines CMD`
- Utilisé par : `VARIATOR SUPER ON E mc`
- Ligne export : 16492 · id 130705

#### e Critical Battery Error mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header, English=e1113 Battery Error · Text, English=The battery is disconnected due to a series of errors. Please restart IMS. Contact your service center if the event recurs.
- Logique :
  - **Showing** = `Repeated errors locker`
- Lit : `Repeated errors locker`
- Utilisé par : *(personne)*
- Ligne export : 16553 · id 130715

#### Battery Ask Reset  `IDC`
> Ask for Ignition opening due to battery fault
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(E.Power Management System = 4) AND (not(Charger Running)) AND (not(Engines Running))`
- Lit : `Charger Running`, `E.Power Management System`, `Engines Running`
- Utilisé par : `BATT - Reset E mc`
- Ligne export : 16599 · id 130723

#### eb Battery Precharge Delay  `IP`
> Precharge phase Delay of battery, used for DCDC start
- Propriétés : Unit=s · Default mode={10}
- Utilisé par : `DCDC Start Delay`, `Single adjust item: Battery Precharge Delay`
- Ligne export : 16660 · id 130733

#### DCDC Start Delay  `MAC`
> Delay between Battery turn On and DCDC Turn On
- Propriétés : Unit=ms
- Logique :
  ```qcode
  Result:=1000 * eb Battery Precharge Delay
  ```
- Lit : `eb Battery Precharge Delay`
- Utilisé par : `Battery OK DCDC`
- Ligne export : 16672 · id 130734

#### Battery OK DCDC  `IDC`
> DCDC can be turned On
- Propriétés : Toggle=No · Delay on=DCDC Start Delay [ms] · Delay off=0
- Logique :
  - **Activating** = `E.Battery CMD = 2`
  - **Blocking** = `E.Power Management System <> 2`
- Lit : `DCDC Start Delay`, `E.Battery CMD`, `E.Power Management System`
- Utilisé par : `K6 DCDC Ignition`, `KTC K12 IDC - AUX 3`
- Ligne export : 16690 · id 130744

#### Battery Ask ShutDown  `IDC`
- Propriétés : Toggle=No · Delay on=300 · Delay off=0
- Logique :
  - **Activating** = `(OK Open Battery Relay) AND (Battery State Feed-Back <= 1) AND (E.Power Management System = 6)`
- Lit : `Battery State Feed-Back`, `E.Power Management System`, `OK Open Battery Relay`
- Utilisé par : `System Shutdown`
- Ligne export : 16744 · id 130753

#### Battery Ask Imminent Crash  `IDC`
> The battery is about to open its contactor, system must be in safe mode
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `E.Power Management System = 4`
- Lit : `E.Power Management System`
- Utilisé par : `System Ask imminent Crash E mc`
- Ligne export : 16805 · id 130763

#### Flag Ground Fault Detection  `IDC`
> Raised if battery raises a 0.0 value with a valid measurement
- Propriétés : Toggle=No · Delay on=1200 · Delay off=0 · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Activating** = `(IsoMonTriggerRecord (iso value valid)) AND (Batt - Iso_Resist [kOhm] <= 0)`
- Fonction *NovumTech* :
  - **Activating** = `False`
- Fonction *Tyva* :
  - **Activating** = `(IsoMonTriggerRecord (iso value valid)) AND (Batt - Iso_Resist [kOhm] <= 0)`
- Fonction *Kreisel* : (vide)
- Lit : `Batt - Iso_Resist`, `IsoMonTriggerRecord (iso value valid)`, `eb Battery Brand`
- Utilisé par : `e Ground Fault message`
- Ligne export : 16850 · id 210555

#### e Ground Fault message  `CMSG`
> Raised when a ground fault is detected
- Propriétés : Show message=All · Dialog type=Critical · Header=e1155 High Tension Battery · Text=A phase of the battery is pulled to ground. Take the boat to a safe place and contact the technical service. · Channel=Batt - Iso_Resist [kOhm]
- Logique :
  - **Showing** = `PositiveFlank(Flag Ground Fault Detection)`
- Lit : `Batt - Iso_Resist`, `Flag Ground Fault Detection`
- Utilisé par : *(personne)*
- Ligne export : 16997 · id 210563

#### Is_Kreisel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `eb Battery Brand = 3`
- Lit : `eb Battery Brand`
- Utilisé par : `Is_bender_present`, `Active le groupe: mc.Electric / E.BATTERY / E.Kresel`
- Ligne export : 22018 · id 234661

#### Is_bender_present  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Is_BMW OR Is_Tyva OR Is_Kreisel`
- Lit : `Is_BMW`, `Is_Kreisel`, `Is_Tyva`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Single adjust item: Isolation Protection Level`
- Ligne export : 22063 · id 231899

#### BMW/tyva - Bender Error  `IDC`
> Set to 1 when Isolation measurement is not working
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(IsoMonState bmw = 2) OR (IsoMonState bmw = 4) OR (iso value not valid tyva and (not(tyva isomon can nok)))`
- Lit : `IsoMonState bmw`, `iso value not valid tyva`, `tyva isomon can nok`
- Utilisé par : *(personne)*
- Ligne export : 22120 · id 130154

#### Battery InstantVoltage ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(BatteryVoltage tyva [V] Status = OK) OR (BatPackVoltage bmw Status = OK) OR (BatteryVoltage novum [V] Status = OK)`
  - **Blocking** = `(bmw batt can nok) OR (novum batt can nok) OR (tyva batt can nok)`
- Lit : `BatPackVoltage bmw`, `BatteryVoltage novum`, `BatteryVoltage tyva`, `bmw batt can nok`, `novum batt can nok`, `tyva batt can nok`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 22191 · id 233100

#### CPI_BMS_U_Trac  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed · Function selector=eb Battery Brand
- Fonction *BMW* :
  - **Controlling** = `BMW_-_Battery_InstantVoltage [V]`
- Fonction *NovumTech* :
  - **Controlling** = `Novum - BatteryVoltage [V]`
- Fonction *Tyva* :
  - **Controlling** = `volt tyva mean off`
- Fonction *Kreisel* : (vide)
- Lit : `BMW_-_Battery_InstantVoltage`, `Novum - BatteryVoltage`, `eb Battery Brand`, `volt tyva mean off`
- Utilisé par : `MD4-5 page: INFO`
- Ligne export : 22275 · id 233151

#### Battery soc ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(BatStateOfCharge bmw Status = OK) OR (SOC novum [%] Status = OK) OR (SOC tyva [%] Status = OK)`
  - **Blocking** = `(bmw batt can nok) OR (novum batt can nok) OR (tyva batt can nok)`
- Lit : `BatStateOfCharge bmw`, `SOC novum`, `SOC tyva`, `bmw batt can nok`, `novum batt can nok`, `tyva batt can nok`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 22403 · id 233205

#### Battery u trac/cpi volt ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(BatBusVoltage utrac bmw Status = OK) OR (BatteryVoltage novum [V] Status = OK) OR (tyva isomon can ok)`
  - **Blocking** = `(bmw batt can nok) OR (novum batt can nok) OR (tyva isomon can nok)`
- Lit : `BatBusVoltage utrac bmw`, `BatteryVoltage novum`, `bmw batt can nok`, `novum batt can nok`, `tyva isomon can nok`, `tyva isomon can ok`
- Utilisé par : *(personne)*
- Ligne export : 22487 · id 233223

#### Battery r isomon ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(BMS_NTHT_Errors novum Status = OK) OR (tyva isomon can ok) OR (bmw isomon ok)`
- Lit : `BMS_NTHT_Errors novum`, `bmw isomon ok`, `tyva isomon can ok`
- Utilisé par : *(personne)*
- Ligne export : 22569 · id 233258

#### Battery temp ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(BatMaxCellTemp bmw Status = OK) OR (MaxTemp novum [°C] Status = OK) OR (TemperatureCellMax [°C] Status = OK)`
  - **Blocking** = `(bmw batt can nok) OR (novum batt can nok) OR (tyva isomon can nok)`
- Lit : `BatMaxCellTemp bmw`, `MaxTemp novum`, `TemperatureCellMax`, `bmw batt can nok`, `novum batt can nok`, `tyva isomon can nok`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 22628 · id 233286

#### Battery CURRENT filter  `SFC`
- Propriétés : Input channel=Battery CURRENT [A] · Enable=Yes · Type=Moving average · Window size=10
- Lit : `Battery CURRENT`
- Utilisé par : `Battery POWER filter`
- Ligne export : 22712 · id 233321

#### Battery POWER filter  `MAC`
- Propriétés : Unit=kW · Limiting object group=Signed
- Logique :
  - **Controlling** = `(Battery Filtered Voltage [V] * Battery CURRENT filter [A]) / 1000`
- Lit : `Battery CURRENT filter`, `Battery Filtered Voltage`
- Utilisé par : `Measure group: Battery Tyva`
- Ligne export : 22724 · id 233323

#### Save Iso_Resist  `IDC`
> Trigger the log of the Isolation measure
- Propriétés : Toggle=No · Delay on=60000 · Delay off=0
- Logique :
  - **Activating** = `Battery DRIVE MODE`
- Lit : `Battery DRIVE MODE`
- Utilisé par : `Event log: Battery Isolation`
- Ligne export : 22777 · id 130146

#### Battery CAN OK delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(BMW CAN OK) OR (Novum - CAN OK) OR (tyva batt can ok idc and Is_Tyva) OR (tyva isomon can ok and Is_Tyva) OR (Kreisel - CAN OK)`
- Lit : `BMW CAN OK`, `Is_Tyva`, `Kreisel - CAN OK`, `Novum - CAN OK`, `tyva batt can ok idc`, `tyva isomon can ok`
- Utilisé par : `batt ok to start`
- Ligne export : 22820 · id 233866

#### batt ok to start  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Battery CAN OK delay) AND (not(Battery ERROR DIGIT))`
- Lit : `Battery CAN OK delay`, `Battery ERROR DIGIT`
- Utilisé par : `batt ok to start APPOUT`, `enabled ON/OFF T&E`, `trameb 2`
- Ligne export : 22895 · id 233820

#### batt ok to start APPOUT  `APPOUT`
- Propriétés : Input channel=batt ok to start · Send method=On change · Transmit rate=1000
- Lit : `batt ok to start`
- Utilisé par : `batt ok to start APPIN`, `batt ok to start APPIN`
- Ligne export : 25335 · id 236415

## mc.Electric / E.BATTERY / E. Tyva — actif seulement si `Is_Tyva`

#### BatteryState_M0  `GFIN`
- Propriétés : Identifier=0x18FF0980 · Data length=Dont care · Paged protocol={Not used} · Parameters={{SOC tyva [%]; 0}; {SOH [%]; 16}; {CycleCount; 32}} · Module=tyva battery (Generic) · Module index=1
- Lit : `CycleCount`, `SOC tyva`, `SOH`
- Utilisé par : *(personne)*
- Ligne export : 19261 · id 231086

#### SOC tyva  `GPIN`
- Propriétés : Unit=% · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `Battery soc ok`, `BatteryState_M0`, `SOC Tyva`
- Ligne export : 19286 · id 231087

#### SOH  `GPIN`
- Propriétés : Unit=% · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `BatteryState_M0`, `SOH`, `Measure group: Battery Tyva`
- Ligne export : 19299 · id 231088

#### PDUStatus_M0b  `GFIN`
- Propriétés : Identifier=0x18FF1380 · Data length=Dont care · Paged protocol={Not used} · Parameters={{PDURelayStatusCharge; 2}; {PDURelayStatusDecharge; 1}; {PDURelayStatusPrecharge; 0}} · Module=tyva battery (Generic) · Module index=2
- Lit : `PDURelayStatusCharge`, `PDURelayStatusDecharge`, `PDURelayStatusPrecharge`
- Utilisé par : *(personne)*
- Ligne export : 19312 · id 231089

#### PDURelayStatusCharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `PDUStatus_M0b`
- Ligne export : 19337 · id 231090

#### PDURelayStatusDecharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `PDUStatus_M0b`
- Ligne export : 19348 · id 231091

#### PDURelayStatusPrecharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `PDUStatus_M0b`
- Ligne export : 19359 · id 231092

#### SynthesisBMS_M0  `GFIN`
- Propriétés : Identifier=0x18FF1280 · Data length=Dont care · Timeout=3000 · Paged protocol={Not used} · Parameters={{isBalancing; 0}; {isChargePossible; 2}; {isChargeRelayClosingAuth; 4}; {isDischargePossible; 3}; {isDischargeRelayClosingAuth; 5}; {isReadyToStart; 1}; {StateBMS; 6}} · Module=tyva battery (Generic) · Module index=3
- Lit : `StateBMS`, `isBalancing`, `isChargePossible`, `isChargeRelayClosingAuth`, `isDischargePossible`, `isDischargeRelayClosingAuth`, `isReadyToStart`
- Utilisé par : `tyva batt can nok`, `tyva batt can ok idc`
- Ligne export : 19370 · id 231093

#### isBalancing  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `SynthesisBMS_M0`
- Ligne export : 19407 · id 231094

#### isChargePossible  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `SynthesisBMS_M0`
- Ligne export : 19418 · id 231095

#### isChargeRelayClosingAuth  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `SynthesisBMS_M0`
- Ligne export : 19429 · id 231096

#### isDischargePossible  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `SynthesisBMS_M0`, `Tyva - isDischargePossible`
- Ligne export : 19440 · id 231097

#### isDischargeRelayClosingAuth  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `SynthesisBMS_M0`
- Ligne export : 19451 · id 231098

#### isReadyToStart  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `SynthesisBMS_M0`
- Ligne export : 19462 · id 231099

#### StateBMS  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `SynthesisBMS_M0`, `bms decode bin`
- Ligne export : 19473 · id 231100

#### Error_M0  `GFIN`
- Propriétés : Identifier=0x18FF1180 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{ErrorAFEIssues; 23}; {ErrorBluetooth; 13}; {ErrorBmsOverTemperature; 18}; {ErrorCellIssues; 20}; {ErrorChargerIssue; 19}; {ErrorCurrentCalibration; 9}; {ErrorDataLogger; 14}; {ErrorHighVoltage; 11}; {ErrorLowVoltage; 10}; {ErrorNTC; 12}; {ErrorOverCurrent; 30}; {ErrorOverTemperatureCharge; 25}; {ErrorOverTemperatureDischarge; 27}; {ErrorOverVoltage; 29}; {ErrorPDULock; 31}; {ErrorPduFailure; 16}; {ErrorPduOverTemperature; 17}; {ErrorShortCircuit; 21}; {ErrorShortCircuitOnPrecharge; 8}; {ErrorSlaveSilent; 22}; {ErrorUnderTemperatureCharge; 24}; {ErrorUnderTemperatureDischarge; 26}; {ErrorUnderVoltage; 28}} · Module=tyva battery (Generic) · Module index=4
- Lit : `ErrorAFEIssues`, `ErrorBluetooth`, `ErrorBmsOverTemperature`, `ErrorCellIssues`, `ErrorChargerIssue`, `ErrorCurrentCalibration`, `ErrorDataLogger`, `ErrorHighVoltage`, `ErrorLowVoltage`, `ErrorNTC`, `ErrorOverCurrent`, `ErrorOverTemperatureCharge`, `ErrorOverTemperatureDischarge`, `ErrorOverVoltage`, `ErrorPDULock`, `ErrorPduFailure`, `ErrorPduOverTemperature`, `ErrorShortCircuit`, `ErrorShortCircuitOnPrecharge`, `ErrorSlaveSilent`, `ErrorUnderTemperatureCharge`, `ErrorUnderTemperatureDischarge`, `ErrorUnderVoltage`
- Utilisé par : *(personne)*
- Ligne export : 19485 · id 231101

#### ErrorAFEIssues  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19570 · id 231102

#### ErrorBluetooth  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19581 · id 231103

#### ErrorBmsOverTemperature  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19592 · id 231104

#### ErrorCellIssues  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19603 · id 231105

#### ErrorChargerIssue  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19614 · id 231106

#### ErrorCurrentCalibration  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19625 · id 231107

#### ErrorDataLogger  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`
- Ligne export : 19636 · id 231108

#### ErrorHighVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19647 · id 231109

#### ErrorLowVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19658 · id 231110

#### ErrorNTC  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19669 · id 231111

#### ErrorOverCurrent  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19680 · id 231112

#### ErrorOverTemperatureCharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19691 · id 231113

#### ErrorOverTemperatureDischarge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19702 · id 231114

#### ErrorOverVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19713 · id 231115

#### ErrorPDULock  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19724 · id 231116

#### ErrorPduFailure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19735 · id 231117

#### ErrorPduOverTemperature  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19746 · id 231118

#### ErrorShortCircuit  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19757 · id 231119

#### ErrorShortCircuitOnPrecharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19768 · id 231120

#### ErrorSlaveSilent  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19779 · id 231121

#### ErrorUnderTemperatureCharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19790 · id 231122

#### ErrorUnderTemperatureDischarge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19801 · id 231123

#### ErrorUnderVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 19812 · id 231124

#### TemperaturePDU_M0  `GFIN`
- Propriétés : Identifier=0x18FF0F80 · Data length=Dont care · Paged protocol={Not used} · Parameters={{TemperaturePDU [°C]; 0}} · Module=tyva battery (Generic) · Module index=5
- Lit : `TemperaturePDU`
- Utilisé par : *(personne)*
- Ligne export : 19823 · id 231125

#### TemperaturePDU  `GPIN`
- Propriétés : Unit=°C · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `TemperaturePDU`, `TemperaturePDU_M0`
- Ligne export : 19842 · id 231126

#### VoltageBattery_M0  `GFIN`
- Propriétés : Identifier=0x18FF0080 · Data length=Dont care · Paged protocol={Not used} · Parameters={{VoltageCellMax [mV]; 16}; {VoltageCellMin [mV]; 0}; {BatteryVoltage tyva [V]; 32}} · Module=tyva battery (Generic) · Module index=6
- Lit : `BatteryVoltage tyva`, `VoltageCellMax`, `VoltageCellMin`
- Utilisé par : *(personne)*
- Ligne export : 19855 · id 231127

#### VoltageCellMax  `GPIN`
- Propriétés : Unit=mV · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `VoltageBattery_M0`, `VoltageCellMax Tyva V`
- Ligne export : 19880 · id 231128

#### VoltageCellMin  `GPIN`
- Propriétés : Unit=mV · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `VoltageBattery_M0`, `VoltageCellMin Tyva V`
- Ligne export : 19893 · id 231129

#### CurrentBattery_M0  `GFIN`
- Propriétés : Identifier=0x18FF0880 · Data length=Dont care · Paged protocol={Not used} · Parameters={{WRONG BatteryCurrent [A]; 7}} · Module=tyva battery (Generic) · Module index=7
- Lit : `WRONG BatteryCurrent`
- Utilisé par : *(personne)*
- Ligne export : 19906 · id 231130

#### WRONG BatteryCurrent  `GPIN`
- Propriétés : Unit=A · Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Big-endian · Error value=0
- Utilisé par : `CurrentBattery_M0`
- Ligne export : 19925 · id 231131

#### TemperatureCell_M0  `GFIN`
- Propriétés : Identifier=0x18FF0B80 · Data length=Dont care · Paged protocol={Not used} · Parameters={{TemperatureCellMax [°C]; 16}; {TemperatureCellMin [°C]; 0}; {TemperatureCellMean [°C]; 32}} · Module=tyva battery (Generic) · Module index=8
- Lit : `TemperatureCellMax`, `TemperatureCellMean`, `TemperatureCellMin`
- Utilisé par : *(personne)*
- Ligne export : 19938 · id 231132

#### TemperatureCellMax  `GPIN`
- Propriétés : Unit=°C · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `Battery temp ok`, `TemperatureCellMax calc`, `TemperatureCell_M0`
- Ligne export : 19963 · id 231133

#### TemperatureCellMin  `GPIN`
- Propriétés : Unit=°C · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `TemperatureCellMin calc`, `TemperatureCell_M0`
- Ligne export : 19976 · id 231134

#### MaxAdmissibleCurrent_M0  `GFIN`
- Propriétés : Identifier=0x18FF1580 · Data length=Dont care · Paged protocol={Not used} · Parameters={{IMD [A]; 0}; {IMR [A]; 32}} · Module=tyva battery (Generic) · Module index=9
- Lit : `IMD`, `IMR`
- Utilisé par : *(personne)*
- Ligne export : 19989 · id 231135

#### IMD  `GPIN`
- Propriétés : Unit=A · Length=32 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `IMD Tyva Max curr`, `MaxAdmissibleCurrent_M0`
- Ligne export : 20011 · id 231136

#### Warning_M0  `GFIN`
- Propriétés : Identifier=0x18FF1480 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{WarningAFEIssues; 23}; {WarningBluetooth; 13}; {WarningBmsOverTemperature; 18}; {WarningCellIssues; 20}; {WarningChargerIssue; 19}; {WarningCurrentCalibration; 9}; {WarningDataLogger; 14}; {WarningHighVoltage; 11}; {WarningLowVoltage; 10}; {WarningNTC; 12}; {WarningOverCurrent; 30}; {WarningOverTemperatureCharge; 25}; {WarningOverTemperatureDischarge; 27}; {WarningOverVoltage; 29}; {WarningPDULock; 31}; {WarningPduFailure; 16}; {WarningPduOverTemperature; 17}; {WarningShortCircuit; 21}; {WarningShortCircuitOnPrecharge; 8}; {WarningSlaveSilent; 22}; {WarningUnderTemperatureCharge; 24}; {WarningUnderTemperatureDischarge; 26}; {WarningUnderVoltage; 28}} · Module=tyva battery (Generic) · Module index=0
- Lit : `WarningAFEIssues`, `WarningBluetooth`, `WarningBmsOverTemperature`, `WarningCellIssues`, `WarningChargerIssue`, `WarningCurrentCalibration`, `WarningDataLogger`, `WarningHighVoltage`, `WarningLowVoltage`, `WarningNTC`, `WarningOverCurrent`, `WarningOverTemperatureCharge`, `WarningOverTemperatureDischarge`, `WarningOverVoltage`, `WarningPDULock`, `WarningPduFailure`, `WarningPduOverTemperature`, `WarningShortCircuit`, `WarningShortCircuitOnPrecharge`, `WarningSlaveSilent`, `WarningUnderTemperatureCharge`, `WarningUnderTemperatureDischarge`, `WarningUnderVoltage`
- Utilisé par : *(personne)*
- Ligne export : 20024 · id 231137

#### WarningAFEIssues  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20109 · id 231138

#### WarningBluetooth  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20120 · id 231139

#### WarningBmsOverTemperature  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20131 · id 231140

#### WarningCellIssues  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20142 · id 231141

#### WarningChargerIssue  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20153 · id 231142

#### WarningCurrentCalibration  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20164 · id 231143

#### WarningDataLogger  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`
- Ligne export : 20175 · id 231144

#### WarningHighVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20186 · id 231145

#### WarningLowVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20197 · id 231146

#### WarningNTC  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20208 · id 231147

#### WarningOverCurrent  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20219 · id 231148

#### WarningOverTemperatureCharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20230 · id 231149

#### WarningOverTemperatureDischarge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20241 · id 231150

#### WarningOverVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Novum battery`, `Event log: Tyva Battery`
- Ligne export : 20252 · id 231151

#### WarningPDULock  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20263 · id 231152

#### WarningPduFailure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20274 · id 231153

#### WarningPduOverTemperature  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20285 · id 231154

#### WarningShortCircuit  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20296 · id 231155

#### WarningShortCircuitOnPrecharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20307 · id 231156

#### WarningSlaveSilent  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`
- Ligne export : 20318 · id 231157

#### WarningUnderTemperatureCharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20329 · id 231158

#### WarningUnderTemperatureDischarge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 20340 · id 231159

#### WarningUnderVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Novum battery`, `Event log: Tyva Battery`
- Ligne export : 20351 · id 231160

#### TemperaturePDU  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `TemperaturePDU [°C] * 0,01`
- Lit : `TemperaturePDU`
- Utilisé par : `TemperaturePDU_M0`
- Ligne export : 20362 · id 231161

#### VoltageCellMax Tyva V  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `VoltageCellMax [mV] * 0,001`
- Lit : `VoltageCellMax`
- Utilisé par : `Delta cell voltage`, `HighCellVoltage check bmw`, `Measure group: Battery Tyva`
- Ligne export : 20406 · id 231169

#### VoltageCellMin Tyva V  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `VoltageCellMin [mV] * 0,001`
- Lit : `VoltageCellMin`
- Utilisé par : `Delta cell voltage`, `LowCellVoltage check bmw`, `Measure group: Battery Tyva`
- Ligne export : 20450 · id 231177

#### TemperatureCellMax calc  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `TemperatureCellMax [°C] * 0,01`
- Lit : `TemperatureCellMax`
- Utilisé par : `Tyva - MaxTemp`
- Ligne export : 20494 · id 231185

#### TemperatureCellMin calc  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `TemperatureCellMin [°C] * 0,01`
- Lit : `TemperatureCellMin`
- Utilisé par : *(personne)*
- Ligne export : 20538 · id 231193

#### IMD Tyva Max curr  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `IMD [A] * 0,001`
- Lit : `IMD`
- Utilisé par : `Max Discharge`
- Ligne export : 20582 · id 231201

#### SOC Tyva  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `SOC tyva [%] * 0,01`
- Lit : `SOC tyva`
- Utilisé par : `Last Soc value Tyva`, `Soc Tyva onoff CHECK`, `Measure group: Battery Tyva`
- Ligne export : 20626 · id 231209

#### SOH  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `SOH [%] * 0,01`
- Lit : `SOH`
- Utilisé par : `BatteryState_M0`, `Measure group: Battery Tyva`
- Ligne export : 20670 · id 231217

#### BatteryVoltage tyva  `GPIN`
- Propriétés : Unit=V · Length=32 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `Battery InstantVoltage ok`, `BatteryVoltage Tyva`, `VoltageBattery_M0`
- Ligne export : 20714 · id 231225

#### BatteryVoltage Tyva  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `BatteryVoltage tyva [V] * 0,001`
- Lit : `BatteryVoltage tyva`
- Utilisé par : `BMS_U_Trac`, `Battery InstantVoltage`, `Measure group: Battery Tyva`
- Ligne export : 20727 · id 231226

#### TemperatureCellMean  `GPIN`
- Propriétés : Unit=°C · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `TemperatureCellMean calc`, `TemperatureCell_M0`
- Ligne export : 20771 · id 231234

#### TemperatureCellMean calc  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `TemperatureCellMean [°C] * 0,01`
- Lit : `TemperatureCellMean`
- Utilisé par : *(personne)*
- Ligne export : 20784 · id 231235

#### IMR  `GPIN`
- Propriétés : Unit=A · Length=32 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `IMR`, `MaxAdmissibleCurrent_M0`
- Ligne export : 20828 · id 231243

#### IMR  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `IMR [A] * 0,001`
- Lit : `IMR`
- Utilisé par : `MaxAdmissibleCurrent_M0`
- Ligne export : 20841 · id 231244

#### CycleCount  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `BatteryState_M0`
- Ligne export : 20885 · id 231252

#### bms decode bin  `ARC`
- Propriétés : Array size=9 · Store value=No
- Logique :
  ```qcode
  This[0]:=StateBMS mod 2
  This[1]:=(StateBMS div 2) mod 2
  This[2]:=(StateBMS div 4) mod 2
  This[3]:=(StateBMS div 8) mod 2
  This[4]:=(StateBMS div 16) mod 2
  This[5]:=(StateBMS div 32) mod 2
  This[6]:=(StateBMS div 64) mod 2
  This[7]:=(StateBMS div 128) mod 2
  ```
- Lit : `StateBMS`
- Utilisé par : `Tyva charge b4`, `Tyva discharge b3`, `Tyva standby b2`, `fw update b7`, `idle b1`, `off b0`
- Ligne export : 20897 · id 231253

#### off b0  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=bms decode bin[0]
  ```
- Lit : `bms decode bin`
- Utilisé par : *(personne)*
- Ligne export : 20924 · id 231283

#### idle b1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=bms decode bin[1]
  ```
- Lit : `bms decode bin`
- Utilisé par : *(personne)*
- Ligne export : 20944 · id 231291

#### Tyva standby b2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=bms decode bin[2]
  ```
- Lit : `bms decode bin`
- Utilisé par : *(personne)*
- Ligne export : 20964 · id 231299

#### Tyva discharge b3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=bms decode bin[3]
  ```
- Lit : `bms decode bin`
- Utilisé par : `Battery DRIVE MODE`
- Ligne export : 20984 · id 231307

#### Tyva charge b4  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=bms decode bin[4]
  ```
- Lit : `bms decode bin`
- Utilisé par : `Battery DRIVE MODE`
- Ligne export : 21004 · id 231315

#### fw update b7  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=bms decode bin[8]
  ```
- Lit : `bms decode bin`
- Utilisé par : *(personne)*
- Ligne export : 21024 · id 231323

#### Tyva - MaxTemp  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `TemperatureCellMax calc`
- Lit : `TemperatureCellMax calc`
- Utilisé par : `Cell_T_max_Master`
- Ligne export : 21044 · id 231454

#### Tyva - isDischargePossible  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `isDischargePossible`
- Lit : `isDischargePossible`
- Utilisé par : *(personne)*
- Ligne export : 21086 · id 231875

#### tyva batt can nok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(SynthesisBMS_M0 Status = Not evaluated) OR (SynthesisBMS_M0 Status = Timeout)`
- Lit : `SynthesisBMS_M0`
- Utilisé par : `Battery InstantVoltage ok`, `Battery soc ok`
- Ligne export : 21128 · id 232042

#### Battery State Request tyva  `FGI`
- Propriétés : Input type=State · Input=E.Battery CMD · Default state name=Sleep · States={StandBy; Discharge; Charge}
- Lit : `E.Battery CMD`, `State`
- Utilisé par : `tyva Battery CMD`
- Ligne export : 21182 · id 232262

#### tyva Battery CMD  `SMC`
- Propriétés : Default state name=STAND BY
- Fonction *ON* :
  - **Activating** = `Battery State Request tyva = 2`
- Fonction *Charge* :
  - **Activating** = `Battery State Request tyva = 3`
- Lit : `Battery State Request tyva`
- Utilisé par : `batt tyva main on`, `tyva - CHARGE`
- Ligne export : 21197 · id 232250

#### flag true pb isomon tyva  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((BMW tyva - Isolation Error and system failure tyva isomon com))) OR (PositiveFlank(system failure tyva isomon gen2))   [verrouillé]`
  - **Blocking** = `Reset Startup`
- Lit : `BMW tyva - Isolation Error`, `Reset Startup`, `system failure tyva isomon com`, `system failure tyva isomon gen2`
- Utilisé par : `Brake T/ Batt HT reset / tyva on SEL qcode`, `batt tyva main on`, `tyva - ERROR DIGIT`
- Ligne export : 21272 · id 232750

#### batt tyva main on  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(tyva Battery CMD = 1) OR (tyva Battery CMD = 2)`
  - **Blocking** = `flag true pb isomon tyva`
- Lit : `flag true pb isomon tyva`, `tyva Battery CMD`
- Utilisé par : `Brake T/ Batt HT reset / tyva on SEL qcode`
- Ligne export : 21354 · id 232272

#### tyva - CHARGE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(tyva Battery CMD = 2) AND (tyva batt can ok idc)`
- Lit : `tyva Battery CMD`, `tyva batt can ok idc`
- Utilisé par : `Battery CHARGE`
- Ligne export : 21415 · id 232288

#### tyva - ERROR DIGIT  `IDC`
- Propriétés : Toggle=No · Delay on=100 · Delay off=100
- Logique :
  - **Activating** = `ErrorOverCurrent OR ErrorOverTemperatureCharge OR ErrorOverTemperatureDischarge OR ErrorOverVoltage OR ErrorLowVoltage OR ErrorHighVoltage OR ErrorPduOverTemperature OR ErrorUnderTemperatureCharge OR ErrorUnderTemperatureDischarge OR ErrorUnderVoltage OR ErrorBmsOverTemperature OR (flag true pb isomon tyva)`
- Lit : `ErrorBmsOverTemperature`, `ErrorHighVoltage`, `ErrorLowVoltage`, `ErrorOverCurrent`, `ErrorOverTemperatureCharge`, `ErrorOverTemperatureDischarge`, `ErrorOverVoltage`, `ErrorPduOverTemperature`, `ErrorUnderTemperatureCharge`, `ErrorUnderTemperatureDischarge`, `ErrorUnderVoltage`, `flag true pb isomon tyva`
- Utilisé par : `Battery ERROR DIGIT`
- Ligne export : 21467 · id 232325

#### tyva batt can ok idc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `SynthesisBMS_M0 Status = OK`
- Lit : `SynthesisBMS_M0`
- Utilisé par : `Battery CAN OK`, `Battery CAN OK delay`, `IsoMonTriggerRecord (iso value valid)`, `SocTriggerRecord tyva`, `Tyva batt can ok`, `tyva - CHARGE`
- Ligne export : 21587 · id 233185

#### Tyva batt can ok  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `tyva batt can ok idc`
- Lit : `tyva batt can ok idc`
- Utilisé par : `tyva off on state`
- Ligne export : 21632 · id 232056

#### Last Soc value Tyva  `MEM`
- Propriétés : Input channel=SOC Tyva [%] · Action=Replace · Store value=Yes · Reset value=soc bof tyva [%]
- Logique :
  - **Activating** = `SocTriggerRecord tyva`
- Lit : `SOC Tyva`, `SocTriggerRecord tyva`, `soc bof tyva`
- Utilisé par : `Soc Tyva onoff CHECK`
- Ligne export : 21674 · id 233339

#### SocTriggerRecord tyva  `IDC`
- Propriétés : Toggle=No · Delay on=30000 · Delay off=0
- Logique :
  - **Activating** = `tyva batt can ok idc`
- Lit : `tyva batt can ok idc`
- Utilisé par : `Last Soc value Tyva`
- Ligne export : 21718 · id 233351

#### tyva off on state  `SP`
- Propriétés : Input channel=Tyva batt can ok · Default state name=off · States={on}
- Lit : `Tyva batt can ok`
- Utilisé par : `Soc Tyva onoff CHECK`
- Ligne export : 21761 · id 232054

#### Soc Tyva onoff CHECK  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=tyva off on state
- Fonction *off* :
  - **Controlling** = `Last Soc value Tyva [%]`
- Fonction *on* :
  - **Controlling** = `SOC Tyva [%]`
- Lit : `Last Soc value Tyva`, `SOC Tyva`, `tyva off on state`
- Utilisé par : `Battery SOC`
- Ligne export : 21773 · id 232036

#### r isomon Tyva onoff  `MAC`
- Propriétés : Unit=kOhm · Limiting object group=Signed · Function selector=isomon tyva off on state
- Fonction *off* :
  - **Controlling** = `Last Isolation value BMW/tyva [kOhm]`
- Fonction *on* :
  - **Controlling** = `Batt - Iso_Resist [kOhm]`
- Lit : `Batt - Iso_Resist`, `Last Isolation value BMW/tyva`, `isomon tyva off on state`
- Utilisé par : *(personne)*
- Ligne export : 21846 · id 233419

#### isomon tyva off on state  `SP`
- Propriétés : Input channel=isomon Tyva batt can ok · Default state name=off · States={on}
- Lit : `isomon Tyva batt can ok`
- Utilisé par : `r isomon Tyva onoff`
- Ligne export : 21919 · id 233435

#### isomon Tyva batt can ok  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `IsoMonTriggerRecord (iso value valid)`
- Lit : `IsoMonTriggerRecord (iso value valid)`
- Utilisé par : `isomon tyva off on state`
- Ligne export : 21931 · id 233439

#### Delta cell voltage  `MAC`
> V Cell Max - V Cell min
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `VoltageCellMax Tyva V - VoltageCellMin Tyva V`
- Lit : `VoltageCellMax Tyva V`, `VoltageCellMin Tyva V`
- Utilisé par : `Event log: Balancing TYVA`
- Ligne export : 21973 · id 241114

## mc.Electric / E.BATTERY / E. Tyva / bender tyva

#### gen1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Tyva gen bender = 0`
- Lit : `Tyva gen bender`
- Utilisé par : `Active le groupe: mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen1`
- Ligne export : 18422 · id 235783

#### Batt - Iso_Resist - tyva  `MAC`
- Propriétés : Unit=kOhm · Limiting object group=Signed · Function selector=Tyva gen bender
- Fonction *gen1* :
  - **Controlling** = `Iso Measurement tyva [kOhm]`
- Fonction *gen2* :
  - **Controlling** = `IMD G Isolation R iso Corrected [kOhm]`
- Lit : `IMD G Isolation R iso Corrected`, `Iso Measurement tyva`, `Tyva gen bender`
- Utilisé par : `Batt - Iso_Resist`
- Ligne export : 18467 · id 235989

#### Tyva gen bender  `SP`
- Propriétés : Input channel=None · Default state name=gen1 · States={gen2}
- Utilisé par : `Batt - Iso_Resist - tyva`, `gen1`, `gen2`, `iso value not valid tyva`, `system failure tyva isomon com`, `system failure tyva isomon gen2`, `tyva isomon can nok`, `tyva isomon can ok`, `tyva isomon extra can ok`, `volt tyva mean off`, `Adjust group: Master Config`, `Single adjust item: Tyva gen bender`
- Ligne export : 18540 · id 236012

#### gen2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Tyva gen bender = 1`
- Lit : `Tyva gen bender`
- Utilisé par : `Active le groupe: mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen2`
- Ligne export : 18552 · id 236014

#### volt tyva mean off  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Tyva gen bender
- Fonction *gen1* :
  - **Controlling** = `(IG IMC HV 2 [Volt] + IG IMC HV 1 [Volt]) / 2`
- Fonction *gen2* :
  - **Controlling** = `HV_System real`
- Lit : `HV_System real`, `IG IMC HV 1`, `IG IMC HV 2`, `Tyva gen bender`
- Utilisé par : `CPI_BMS_U_Trac`, `soc bof tyva`
- Ligne export : 18597 · id 232068

#### soc bof tyva  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(volt tyva mean off: 300->0, 400->100, Freeze)`
- Lit : `volt tyva mean off`
- Utilisé par : `Last Soc value Tyva`
- Ligne export : 18681 · id 232113

#### tyva isomon extra can ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Tyva gen bender
- Fonction *gen1* :
  - **Activating** = `(IG IMC HV 2 [Volt] Status = OK) AND (IG IMC HV 1 [Volt] Status = OK)`
- Fonction *gen2* :
  - **Activating** = `HV_System [Volt] Status = OK`
- Lit : `HV_System`, `IG IMC HV 1`, `IG IMC HV 2`, `Tyva gen bender`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 18728 · id 233392

#### iso value not valid tyva  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Tyva gen bender
- Fonction *gen1* :
  - **Activating** = `(Isolation not measuring) OR (imc not alive tyva) OR (insulation outdated) OR (Selftest running) OR (Calibration running)`
- Fonction *gen2* :
  - **Activating** = `(IMD G Alarm Device Error 00) OR (IMD G Alarm Iso Outdated 06)`
- Lit : `Calibration running`, `IMD G Alarm Device Error 00`, `IMD G Alarm Iso Outdated 06`, `Isolation not measuring`, `Selftest running`, `Tyva gen bender`, `imc not alive tyva`, `insulation outdated`
- Utilisé par : `BMW/tyva - Bender Error`, `IsoMonTriggerRecord (iso value valid)`
- Ligne export : 18815 · id 232018

#### system failure tyva isomon com  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Tyva gen bender
- Fonction *gen1* :
  - **Activating** = `system failure tyva isomon`
- Fonction *gen2* :
  - **Activating** = `(IMD G Alarm Iso Error 04) OR (IMD G Alarm Iso Warning 05)`
- Lit : `IMD G Alarm Iso Error 04`, `IMD G Alarm Iso Warning 05`, `Tyva gen bender`, `system failure tyva isomon`
- Utilisé par : `Error Iso_Resist`, `flag true pb isomon tyva`
- Ligne export : 18924 · id 236134

#### tyva isomon can nok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Tyva gen bender
- Fonction *gen1* :
  - **Activating** = `(IMD_Info Status = Not evaluated) OR (IMD_Info Status = Timeout)`
- Fonction *gen2* :
  - **Activating** = `(IMD_InfoGeneral gen2 Status = Not evaluated) OR (IMD_InfoGeneral gen2 Status = Timeout)`
- Lit : `IMD_Info`, `IMD_InfoGeneral gen2`, `Tyva gen bender`
- Utilisé par : `BMW/tyva - Bender Error`, `Battery temp ok`, `Battery u trac/cpi volt ok`
- Ligne export : 19005 · id 232236

#### tyva isomon can ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Tyva gen bender
- Fonction *gen1* :
  - **Activating** = `IMD_Info Status = OK`
- Fonction *gen2* :
  - **Activating** = `IMD_InfoGeneral gen2 Status = OK`
- Lit : `IMD_Info`, `IMD_InfoGeneral gen2`, `Tyva gen bender`
- Utilisé par : `Battery CAN OK`, `Battery CAN OK delay`, `Battery r isomon ok`, `Battery u trac/cpi volt ok`
- Ligne export : 19101 · id 233244

#### system failure tyva isomon gen2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Tyva gen bender
- Fonction *gen1* :
  - **Activating** = `False`
- Fonction *gen2* :
  - **Activating** = `(IMD G Alarm Iso Error 04) OR (IMD G Alarm Iso Warning 05)`
- Lit : `IMD G Alarm Iso Error 04`, `IMD G Alarm Iso Warning 05`, `Tyva gen bender`
- Utilisé par : `flag true pb isomon tyva`
- Ligne export : 19179 · id 236177

## mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen1 — actif seulement si `gen1`

#### IMD_Info  `GFIN`
- Propriétés : Identifier=0x37 · Data length=Dont care · Timeout=3000 · Paged protocol={Not used} · Parameters={{Iso Measurement tyva [kOhm]; 0}; {Isolation fault tyva; 23}; {Chassis fault tyva; 22}; {system failure tyva isomon; 21}; {Calibration running; 20}; {Selftest running; 19}; {Insulation warning tyva; 18}; {Isolation not measuring; 39}; {imc not alive tyva; 37}; {insulation outdated; 47}; {12; 26}; {13; 27}} · Module=tyva bender (Generic) · Module index=1
- Lit : `Calibration running`, `Chassis fault tyva`, `Insulation warning tyva`, `Iso Measurement tyva`, `Isolation fault tyva`, `Isolation not measuring`, `Selftest running`, `imc not alive tyva`, `insulation outdated`, `system failure tyva isomon`
- Utilisé par : `tyva isomon can nok`, `tyva isomon can ok`
- Ligne export : 17118 · id 231398

#### Iso Measurement tyva  `GPIN`
> Isolation measurement
- Propriétés : Unit=kOhm · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Batt - Iso_Resist - tyva`, `IMD_Info`
- Ligne export : 17170 · id 231399

#### Isolation fault tyva  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_Info`
- Ligne export : 17183 · id 231400

#### Chassis fault tyva  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_Info`
- Ligne export : 17194 · id 231401

#### system failure tyva isomon  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_Info`, `system failure tyva isomon com`
- Ligne export : 17205 · id 231402

#### Calibration running  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_Info`, `iso value not valid tyva`
- Ligne export : 17216 · id 231403

#### Selftest running  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_Info`, `iso value not valid tyva`
- Ligne export : 17227 · id 231404

#### Insulation warning tyva  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_Info`
- Ligne export : 17238 · id 231405

#### Isolation not measuring  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_Info`, `iso value not valid tyva`
- Ligne export : 17249 · id 231406

#### imc not alive tyva  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_Info`, `iso value not valid tyva`
- Ligne export : 17260 · id 231407

#### insulation outdated  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_Info`, `iso value not valid tyva`
- Ligne export : 17271 · id 231408

#### 12  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : *(personne)*
- Ligne export : 17282 · id 231421

#### 13  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : *(personne)*
- Ligne export : 17293 · id 231422

#### Response_hv_2 58  `GFIN`
- Propriétés : Identifier=35 · Data length=5 · Timeout=3000 · Paged protocol={0xFF; 58} · Parameters={{IG IMC HV 2 [Volt]; 8}} · Module=tyva bender (Generic) · Module index=2
- Lit : `IG IMC HV 2`
- Utilisé par : *(personne)*
- Ligne export : 17304 · id 231428

#### IG IMC HV 2  `GPIN`
- Propriétés : Unit=Volt · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Response_hv_2 58`, `tyva isomon extra can ok`, `volt tyva mean off`
- Ligne export : 17324 · id 231429

#### Response_hv_1 54  `GFIN`
- Propriétés : Identifier=35 · Data length=5 · Timeout=3000 · Paged protocol={0xFF; 54} · Parameters={{IG IMC HV 1 [Volt]; 8}} · Module=tyva bender (Generic) · Module index=0
- Lit : `IG IMC HV 1`
- Utilisé par : *(personne)*
- Ligne export : 17337 · id 231434

#### IG IMC HV 1  `GPIN`
- Propriétés : Unit=Volt · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Response_hv_1 54`, `tyva isomon extra can ok`, `volt tyva mean off`
- Ligne export : 17357 · id 231435

#### get_hv_2 0x22  `GFOUT`
- Propriétés : Identifier=0x22 · Data length=8 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{A BYTE 0 - 3A; 0}; {A BYTE 1 - 00; 8}; {A BYTE 2 - 00; 16}} · Module=tyva bender (Generic) · Module index=0
- Lit : `A BYTE 0 - 3A`, `A BYTE 1 - 00`, `A BYTE 2 - 00`
- Utilisé par : *(personne)*
- Ligne export : 17370 · id 232007

#### A BYTE 1 - 00  `GPOUT`
- Propriétés : Input value=0x00 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_hv_1 0x22`, `get_hv_2 0x22`
- Ligne export : 17395 · id 232008

#### A BYTE 2 - 00  `GPOUT`
- Propriétés : Input value=0x00 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_hv_1 0x22`, `get_hv_2 0x22`
- Ligne export : 17406 · id 232009

#### A BYTE 0 - 3A  `GPOUT`
- Propriétés : Input value=0x3A · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_hv_2 0x22`
- Ligne export : 17417 · id 232010

#### get_hv_1 0x22  `GFOUT`
- Propriétés : Identifier=0x22 · Data length=8 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{A BYTE 0 - 36; 0}; {A BYTE 1 - 00; 8}; {A BYTE 2 - 00; 16}} · Module=tyva bender (Generic) · Module index=1
- Lit : `A BYTE 0 - 36`, `A BYTE 1 - 00`, `A BYTE 2 - 00`
- Utilisé par : *(personne)*
- Ligne export : 17428 · id 232012

#### A BYTE 1 - 00  `GPOUT`
- Propriétés : Input value=0x00 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_hv_1 0x22`, `get_hv_2 0x22`
- Ligne export : 17453 · id 232013

#### A BYTE 2 - 00  `GPOUT`
- Propriétés : Input value=0x00 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_hv_1 0x22`, `get_hv_2 0x22`
- Ligne export : 17464 · id 232014

#### A BYTE 0 - 36  `GPOUT`
- Propriétés : Input value=0x36 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_hv_1 0x22`
- Ligne export : 17475 · id 232015

#### BYTE 0 - D2  `GPOUT`
- Propriétés : Input value=0xD2 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `close relay hv1 0x22`, `close relay hv2 0x22`
- Ligne export : 17486 · id 232132

#### BYTE 1 - 01  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `close relay hv1 0x22`
- Ligne export : 17497 · id 232133

#### BYTE 2 - 00  `GPOUT`
- Propriétés : Input value=0x00 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `close relay hv1 0x22`, `close relay hv2 0x22`
- Ligne export : 17508 · id 232134

#### BYTE 3 - 01  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `close relay hv1 0x22`, `close relay hv2 0x22`
- Ligne export : 17519 · id 232135

#### BYTE 4 - 00  `GPOUT`
- Propriétés : Input value=0x00 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `close relay hv1 0x22`, `close relay hv2 0x22`
- Ligne export : 17530 · id 232136

#### close relay hv1 0x22  `GFOUT`
- Propriétés : Identifier=0x22 · Data length=5 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{BYTE 0 - D2; 0}; {BYTE 1 - 01; 8}; {BYTE 2 - 00; 16}; {BYTE 3 - 01; 24}; {BYTE 4 - 00; 32}} · Module=tyva bender (Generic) · Module index=3
- Lit : `BYTE 0 - D2`, `BYTE 1 - 01`, `BYTE 2 - 00`, `BYTE 3 - 01`, `BYTE 4 - 00`
- Utilisé par : *(personne)*
- Ligne export : 17541 · id 232137

#### BYTE 0 - D2  `GPOUT`
- Propriétés : Input value=0xD2 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `close relay hv1 0x22`, `close relay hv2 0x22`
- Ligne export : 17572 · id 232138

#### BYTE 1 - 00  `GPOUT`
- Propriétés : Input value=0x00 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `close relay hv2 0x22`
- Ligne export : 17583 · id 232139

#### BYTE 2 - 00  `GPOUT`
- Propriétés : Input value=0x00 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `close relay hv1 0x22`, `close relay hv2 0x22`
- Ligne export : 17594 · id 232140

#### BYTE 3 - 01  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `close relay hv1 0x22`, `close relay hv2 0x22`
- Ligne export : 17605 · id 232141

#### BYTE 4 - 00  `GPOUT`
- Propriétés : Input value=0x00 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `close relay hv1 0x22`, `close relay hv2 0x22`
- Ligne export : 17616 · id 232142

#### close relay hv2 0x22  `GFOUT`
- Propriétés : Identifier=0x22 · Data length=5 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{BYTE 0 - D2; 0}; {BYTE 1 - 00; 8}; {BYTE 2 - 00; 16}; {BYTE 3 - 01; 24}; {BYTE 4 - 00; 32}} · Module=tyva bender (Generic) · Module index=4
- Lit : `BYTE 0 - D2`, `BYTE 1 - 00`, `BYTE 2 - 00`, `BYTE 3 - 01`, `BYTE 4 - 00`
- Utilisé par : *(personne)*
- Ligne export : 17627 · id 232143

## mc.Electric / E.BATTERY / E. Tyva / bender tyva / gen2 — actif seulement si `gen2`

#### IMD_InfoGeneral gen2  `GFIN`
- Propriétés : Identifier=0x37 · Data length=8 · Paged protocol={Not used} · Parameters={{IMD G Alarm Device Error 00; 32}; {IMD G Alarm Eart Conn 03; 35}; {IMD G Alarm Earthlift 10; 42}; {IMD G Alarm HV neg Conn 02; 34}; {IMD G Alarm HV pos Conn 01; 33}; {IMD G Alarm Iso Error 04; 36}; {IMD G Alarm Iso Outdated 06; 38}; {IMD G Alarm Iso Warning 05; 37}; {IMD G Alarm Unbalance 07; 39}; {IMD G Alarm Undervoltage 08; 40}; {IMD G Alarm UnsafeToStart 09; 41}; {IMD G Device Activity; 48}; {IMD G Isolation Counter; 24}; {IMD G Isolation R iso Corrected [kOhm]; 0}; {IMD G Isolation R iso Status; 16}; {IMD G Warning Alarm Status Bit11; 43}; {IMD G Warning Alarm Status Bit12; 44}; {IMD G Warning Alarm Status Bit13; 45}; {IMD G Warning Alarm Status Bit14; 46}; {IMD G Warning Alarm Status Bit15; 47}} · Module=tyva bender (Generic) · Module index=3
- Lit : `IMD G Alarm Device Error 00`, `IMD G Alarm Eart Conn 03`, `IMD G Alarm Earthlift 10`, `IMD G Alarm HV neg Conn 02`, `IMD G Alarm HV pos Conn 01`, `IMD G Alarm Iso Error 04`, `IMD G Alarm Iso Outdated 06`, `IMD G Alarm Iso Warning 05`, `IMD G Alarm Unbalance 07`, `IMD G Alarm Undervoltage 08`, `IMD G Alarm UnsafeToStart 09`, `IMD G Device Activity`, `IMD G Isolation Counter`, `IMD G Isolation R iso Corrected`, `IMD G Isolation R iso Status`, `IMD G Warning Alarm Status Bit11`, `IMD G Warning Alarm Status Bit12`, `IMD G Warning Alarm Status Bit13`, `IMD G Warning Alarm Status Bit14`, `IMD G Warning Alarm Status Bit15`
- Utilisé par : `tyva isomon can nok`, `tyva isomon can ok`
- Ligne export : 17682 · id 235760

#### IMD G Alarm Device Error 00  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`, `iso value not valid tyva`
- Ligne export : 17758 · id 235761

#### IMD G Alarm Eart Conn 03  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17769 · id 235762

#### IMD G Alarm Earthlift 10  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17780 · id 235763

#### IMD G Alarm HV neg Conn 02  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17791 · id 235764

#### IMD G Alarm HV pos Conn 01  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17802 · id 235765

#### IMD G Alarm Iso Error 04  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`, `system failure tyva isomon com`, `system failure tyva isomon gen2`
- Ligne export : 17813 · id 235766

#### IMD G Alarm Iso Outdated 06  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`, `iso value not valid tyva`
- Ligne export : 17824 · id 235767

#### IMD G Alarm Iso Warning 05  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`, `system failure tyva isomon com`, `system failure tyva isomon gen2`
- Ligne export : 17835 · id 235768

#### IMD G Alarm Unbalance 07  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17846 · id 235769

#### IMD G Alarm Undervoltage 08  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17857 · id 235770

#### IMD G Alarm UnsafeToStart 09  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17868 · id 235771

#### IMD G Device Activity  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17879 · id 235772

#### IMD G Isolation Counter  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17891 · id 235773

#### IMD G Isolation R iso Corrected  `GPIN`
- Propriétés : Unit=kOhm · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Batt - Iso_Resist - tyva`, `IMD_InfoGeneral gen2`
- Ligne export : 17903 · id 235774

#### IMD G Isolation R iso Status  `GPIN`
- Propriétés : Length=2 · Type=Unsigned integer · Error value=0
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17916 · id 235775

#### IMD G Warning Alarm Status Bit11  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17928 · id 235776

#### IMD G Warning Alarm Status Bit12  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17939 · id 235777

#### IMD G Warning Alarm Status Bit13  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17950 · id 235778

#### IMD G Warning Alarm Status Bit14  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17961 · id 235779

#### IMD G Warning Alarm Status Bit15  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `IMD_InfoGeneral gen2`
- Ligne export : 17972 · id 235780

#### Response_HV_System 5E  `GFIN`
- Propriétés : Identifier=0x23 · Data length=Dont care · Timeout=3000 · Paged protocol={0xFF; 0x5E} · Parameters={{HV_System [Volt]; 8}} · Module=tyva bender (Generic) · Module index=6
- Lit : `HV_System`
- Utilisé par : *(personne)*
- Ligne export : 17983 · id 236061

#### HV_System  `GPIN`
- Propriétés : Unit=Volt · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `HV_System real`, `Response_HV_System 5E`, `tyva isomon extra can ok`
- Ligne export : 18003 · id 236062

#### get_HV_System 0x22  `GFOUT`
- Propriétés : Identifier=0x22 · Data length=8 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 1 · Parameters={{A BYTE 0 - 5E; 0}; {A BYTE 1 - FF; 8}; {A BYTE 2 - FF; 16}; {A BYTE 3 - FF; 24}} · Module=tyva bender (Generic) · Module index=5
- Lit : `A BYTE 0 - 5E`, `A BYTE 1 - FF`, `A BYTE 2 - FF`, `A BYTE 3 - FF`
- Utilisé par : *(personne)*
- Ligne export : 18016 · id 236063

#### A BYTE 1 - FF  `GPOUT`
- Propriétés : Input value=0xFF · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_HV_System 0x22`, `get_R_iso 0x22`, `get_R_iso_corrected 0x22`, `get_R_iso_neg 0x22`
- Ligne export : 18044 · id 236064

#### A BYTE 2 - FF  `GPOUT`
- Propriétés : Input value=0xFF · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_HV_System 0x22`, `get_R_iso 0x22`, `get_R_iso_corrected 0x22`, `get_R_iso_neg 0x22`
- Ligne export : 18055 · id 236065

#### A BYTE 0 - 5E  `GPOUT`
- Propriétés : Input value=0x5E · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_HV_System 0x22`
- Ligne export : 18066 · id 236066

#### A BYTE 3 - FF  `GPOUT`
- Propriétés : Input value=0xFF · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_HV_System 0x22`, `get_R_iso 0x22`, `get_R_iso_corrected 0x22`, `get_R_iso_neg 0x22`
- Ligne export : 18077 · id 236067

#### HV_System real  `MAC`
- Logique :
  ```qcode
  Result:=(HV_System-32128)*0.05
  ```
- Lit : `HV_System`
- Utilisé par : `volt tyva mean off`
- Ligne export : 18088 · id 236068

#### Response_R_iso_corrected 4C  `GFIN`
- Propriétés : Identifier=0x23 · Data length=Dont care · Timeout=3000 · Paged protocol={0xFF; 0x4C} · Parameters={{R_iso_corrected [kOhm]; 8}} · Module=tyva bender (Generic) · Module index=5
- Lit : `R_iso_corrected`
- Utilisé par : *(personne)*
- Ligne export : 18106 · id 236077

#### R_iso_corrected  `GPIN`
- Propriétés : Unit=kOhm · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Response_R_iso_corrected 4C`
- Ligne export : 18126 · id 236078

#### get_R_iso_corrected 0x22  `GFOUT`
- Propriétés : Identifier=0x22 · Data length=8 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 1 · Parameters={{A BYTE 0 - 4C; 0}; {A BYTE 1 - FF; 8}; {A BYTE 2 - FF; 16}; {A BYTE 3 - FF; 24}} · Module=tyva bender (Generic) · Module index=2
- Lit : `A BYTE 0 - 4C`, `A BYTE 1 - FF`, `A BYTE 2 - FF`, `A BYTE 3 - FF`
- Utilisé par : *(personne)*
- Ligne export : 18139 · id 236079

#### A BYTE 1 - FF  `GPOUT`
- Propriétés : Input value=0xFF · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_HV_System 0x22`, `get_R_iso 0x22`, `get_R_iso_corrected 0x22`, `get_R_iso_neg 0x22`
- Ligne export : 18167 · id 236080

#### A BYTE 2 - FF  `GPOUT`
- Propriétés : Input value=0xFF · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_HV_System 0x22`, `get_R_iso 0x22`, `get_R_iso_corrected 0x22`, `get_R_iso_neg 0x22`
- Ligne export : 18178 · id 236081

#### A BYTE 0 - 4C  `GPOUT`
- Propriétés : Input value=0x4C · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_R_iso_corrected 0x22`
- Ligne export : 18189 · id 236082

#### A BYTE 3 - FF  `GPOUT`
- Propriétés : Input value=0xFF · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_HV_System 0x22`, `get_R_iso 0x22`, `get_R_iso_corrected 0x22`, `get_R_iso_neg 0x22`
- Ligne export : 18200 · id 236083

#### Response_R_iso 4E  `GFIN`
- Propriétés : Identifier=0x23 · Data length=Dont care · Timeout=3000 · Paged protocol={0xFF; 0x4E} · Parameters={{R_iso [kOhm]; 8}} · Module=tyva bender (Generic) · Module index=4
- Lit : `R_iso`
- Utilisé par : *(personne)*
- Ligne export : 18211 · id 236084

#### R_iso  `GPIN`
- Propriétés : Unit=kOhm · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Response_R_iso 4E`
- Ligne export : 18231 · id 236085

#### get_R_iso 0x22  `GFOUT`
- Propriétés : Identifier=0x22 · Data length=8 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 1 · Parameters={{A BYTE 0 - 4E; 0}; {A BYTE 1 - FF; 8}; {A BYTE 2 - FF; 16}; {A BYTE 3 - FF; 24}} · Module=tyva bender (Generic) · Module index=7
- Lit : `A BYTE 0 - 4E`, `A BYTE 1 - FF`, `A BYTE 2 - FF`, `A BYTE 3 - FF`
- Utilisé par : *(personne)*
- Ligne export : 18244 · id 236086

#### A BYTE 1 - FF  `GPOUT`
- Propriétés : Input value=0xFF · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_HV_System 0x22`, `get_R_iso 0x22`, `get_R_iso_corrected 0x22`, `get_R_iso_neg 0x22`
- Ligne export : 18272 · id 236087

#### A BYTE 2 - FF  `GPOUT`
- Propriétés : Input value=0xFF · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_HV_System 0x22`, `get_R_iso 0x22`, `get_R_iso_corrected 0x22`, `get_R_iso_neg 0x22`
- Ligne export : 18283 · id 236088

#### A BYTE 0 - 4E  `GPOUT`
- Propriétés : Input value=0x4E · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_R_iso 0x22`
- Ligne export : 18294 · id 236089

#### A BYTE 3 - FF  `GPOUT`
- Propriétés : Input value=0xFF · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_HV_System 0x22`, `get_R_iso 0x22`, `get_R_iso_corrected 0x22`, `get_R_iso_neg 0x22`
- Ligne export : 18305 · id 236090

#### Response_R_iso_neg 40  `GFIN`
- Propriétés : Identifier=0x23 · Data length=Dont care · Timeout=3000 · Paged protocol={0xFF; 0x40} · Parameters={{R_iso_neg [kOhm]; 8}} · Module=tyva bender (Generic) · Module index=7
- Lit : `R_iso_neg`
- Utilisé par : *(personne)*
- Ligne export : 18316 · id 236091

#### R_iso_neg  `GPIN`
- Propriétés : Unit=kOhm · Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Response_R_iso_neg 40`
- Ligne export : 18336 · id 236092

#### get_R_iso_neg 0x22  `GFOUT`
- Propriétés : Identifier=0x22 · Data length=8 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 1 · Parameters={{A BYTE 0 - 40; 0}; {A BYTE 1 - FF; 8}; {A BYTE 2 - FF; 16}; {A BYTE 3 - FF; 24}} · Module=tyva bender (Generic) · Module index=6
- Lit : `A BYTE 0 - 40`, `A BYTE 1 - FF`, `A BYTE 2 - FF`, `A BYTE 3 - FF`
- Utilisé par : *(personne)*
- Ligne export : 18349 · id 236093

#### A BYTE 1 - FF  `GPOUT`
- Propriétés : Input value=0xFF · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_HV_System 0x22`, `get_R_iso 0x22`, `get_R_iso_corrected 0x22`, `get_R_iso_neg 0x22`
- Ligne export : 18377 · id 236094

#### A BYTE 2 - FF  `GPOUT`
- Propriétés : Input value=0xFF · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_HV_System 0x22`, `get_R_iso 0x22`, `get_R_iso_corrected 0x22`, `get_R_iso_neg 0x22`
- Ligne export : 18388 · id 236095

#### A BYTE 0 - 40  `GPOUT`
- Propriétés : Input value=0x40 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_R_iso_neg 0x22`
- Ligne export : 18399 · id 236096

#### A BYTE 3 - FF  `GPOUT`
- Propriétés : Input value=0xFF · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `get_HV_System 0x22`, `get_R_iso 0x22`, `get_R_iso_corrected 0x22`, `get_R_iso_neg 0x22`
- Ligne export : 18410 · id 236097

## mc.Electric / E.BATTERY / E.BMW — actif seulement si `Is_BMW`

#### NMT  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{ID; 8}; {State; 0}} · Module=Batt BMW (Generic) · Module index=2
- Lit : `ID`, `State`
- Utilisé par : `Init Seq`
- Ligne export : 9836 · id 129458

#### DcuNodeState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Dcu50Heartbeat`, `DcuNodeState`, `Init Seq`
- Ligne export : 9858 · id 129459

#### BatNodeState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Bat51Hartbeat`, `BatNodeState`, `Init Seq`
- Ligne export : 9870 · id 129460

#### IsoMonNodeState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Init Seq`, `Iso52MonHeartbeat`, `IsoMonNodeState`
- Ligne export : 9882 · id 129461

#### Init Seq  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank(NMT)`
  - **Blocking** = `(DcuNodeState = 5) AND (BatNodeState = 5) AND (IsoMonNodeState = 5)`
- Lit : `BatNodeState`, `DcuNodeState`, `IsoMonNodeState`, `NMT`
- Utilisé par : `Init Counter`
- Ligne export : 9894 · id 129462

#### Init Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Init Seq`
  - **Resetting** = `Init Counter >= 3`
- Lit : `Init Seq`
- Utilisé par : `Node Init`
- Ligne export : 9965 · id 129473

#### Node Init  `SP`
- Propriétés : Input channel=Init Counter · Default state name=0x50 · States={0x51; 0x52}
- Lit : `Init Counter`
- Utilisé par : `Node Init ID`
- Ligne export : 10025 · id 129484

#### Node Init ID  `IP`
- Propriétés : Mode selector=Node Init · Default mode: 0x50={0x50} · Mode 1: 0x51={0x51} · Mode 2: 0x52={0x52}
- Lit : `Node Init`
- Utilisé par : `ID`
- Ligne export : 10038 · id 129487

#### ID  `GPOUT`
- Propriétés : Input value=Node Init ID · Length=8 · Type=Unsigned integer
- Lit : `Node Init ID`
- Utilisé par : `NMT`
- Ligne export : 10054 · id 129488

#### State  `GPOUT`
- Propriétés : Input value=1 · Length=8 · Type=Unsigned integer
- Utilisé par : `0x331 GEN4`, `Battery State`, `Battery State Request`, `Battery State Request`, `Battery State Request`, `Battery State Request tyva`, `Charger STATE`, `In T Engine Thermal State`, `In T Exhaust Temp State`, `In T Hydraulics Temp State`, `NMT`, `Adjust group: Maintenance`
- Ligne export : 10065 · id 129489

#### Dcu50Heartbeat  `GFIN`
- Propriétés : Identifier=0x750 · Data length=Dont care · Timeout=2000 · Paged protocol={Not used} · Parameters={{DcuNodeState; 0}} · Module=Batt BMW (Generic) · Module index=1
- Lit : `DcuNodeState`
- Utilisé par : `BMW CAN OK`, `bmw batt can nok`
- Ligne export : 10076 · id 129490

#### Bat51Hartbeat  `GFIN`
- Propriétés : Identifier=0x751 · Data length=Dont care · Timeout=2000 · Paged protocol={Not used} · Parameters={{BatNodeState; 0}} · Module=Batt BMW (Generic) · Module index=2
- Lit : `BatNodeState`
- Utilisé par : *(personne)*
- Ligne export : 10095 · id 129491

#### Iso52MonHeartbeat  `GFIN`
- Propriétés : Identifier=1874 · Data length=Dont care · Timeout=2000 · Paged protocol={Not used} · Parameters={{IsoMonNodeState; 0}} · Module=Batt BMW (Generic) · Module index=3
- Lit : `IsoMonNodeState`
- Utilisé par : *(personne)*
- Ligne export : 10114 · id 129492

#### Bat Counter  `ECNT`
- Propriétés : Store value=No · Reset value=1
- Logique :
  - **Increasing** = `PositiveFlank(Sync)`
  - **Resetting** = `Bat Counter >= 201`
- Lit : `Sync`
- Utilisé par : `SyncCounter`
- Ligne export : 10133 · id 129493

#### SyncCounter  `GPOUT`
- Propriétés : Input value=Bat Counter · Length=8 · Type=Unsigned integer
- Lit : `Bat Counter`
- Utilisé par : `Sync`
- Ligne export : 10194 · id 129504

#### Sync  `GFOUT`
- Propriétés : Identifier=0x80 · Data length=1 · Send method=Continuously · Transmit rate=20 · Unused bits=Set to 0 · Parameters={{SyncCounter; 0}} · Module=Batt BMW (Generic) · Module index=1
- Lit : `SyncCounter`
- Utilisé par : `Bat Counter`
- Ligne export : 10205 · id 129505

#### Bat51TPdo1  `GFIN`
- Propriétés : Identifier=0x1D1 · Data length=Dont care · Timeout=200 · Paged protocol={Not used} · Parameters={{BatState; 0}; {BatStateOfCharge bmw; 8}; {BatCurrent; 16}; {BatPackVoltage bmw; 32}; {BatBusVoltage utrac bmw; 48}} · Module=Batt BMW (Generic) · Module index=0
- Lit : `BatBusVoltage utrac bmw`, `BatCurrent`, `BatPackVoltage bmw`, `BatState`, `BatStateOfCharge bmw`
- Utilisé par : *(personne)*
- Ligne export : 10224 · id 129506

#### BatState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMW - DRIVE MODE`, `BMW New Battery State`, `Bat51TPdo1`, `BatState`, `Battery State MEM`, `Event log: BMW Battery`, `Measure group: Battery BMW`
- Ligne export : 10255 · id 129507

#### BatStateOfCharge bmw  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMW - SOC`, `Bat51TPdo1`, `Battery soc ok`
- Ligne export : 10267 · id 129508

#### BatCurrent  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - CURRENT`, `Bat51TPdo1`
- Ligne export : 10279 · id 129509

#### BatPackVoltage bmw  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW_-_Battery_InstantVoltage`, `Bat51TPdo1`, `Battery InstantVoltage ok`
- Ligne export : 10292 · id 129510

#### BatBusVoltage utrac bmw  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW_-_U_Trac`, `Bat51TPdo1`, `Battery u trac/cpi volt ok`
- Ligne export : 10305 · id 129511

#### Iso52MonTPdo1  `GFIN`
- Propriétés : Identifier=466 · Data length=Dont care · Timeout=2000 · Paged protocol={Not used} · Parameters={{IsoMonResistance BMW; 0}; {IsoMonVoltage; 16}; {IsoMonState; 32}} · Module=Batt BMW (Generic) · Module index=4
- Lit : `IsoMonResistance BMW`, `IsoMonState`, `IsoMonVoltage`
- Utilisé par : *(personne)*
- Ligne export : 10318 · id 129512

#### IsoMonResistance BMW  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Batt - Iso_Resist`, `Iso52MonTPdo1`, `bmw isomon ok`
- Ligne export : 10343 · id 129513

#### IsoMonVoltage  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Iso52MonTPdo1`
- Ligne export : 10356 · id 129514

#### IsoMonState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Iso52MonTPdo1`, `IsoMonState bmw`
- Ligne export : 10369 · id 129515

#### eb Force BMW Charge  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Single adjust item: Force BMW Charge`
- Ligne export : 10381 · id 129516

#### BMW Battery CMD  `SMC`
- Propriétés : Default state name=STAND BY
- Fonction *ON* :
  - **Activating** = `Battery State Request = 2`
- Fonction *Charge* :
  - **Activating** = `Battery State Request = 3`
- Lit : `Battery State Request`
- Utilisé par : `BMW - CHARGE`, `Command Value`
- Ligne export : 10394 · id 129517

#### Command Value  `IP`
- Propriétés : Mode selector=BMW Battery CMD · Default mode: STAND BY={0x00} · Mode 1: ON={0x01} · Mode 2: Charge={0x03}
- Lit : `BMW Battery CMD`
- Utilisé par : `BatCommand`
- Ligne export : 10469 · id 129529

#### BatCommand  `GPOUT`
- Propriétés : Input value=Command Value · Length=8 · Type=Unsigned integer
- Lit : `Command Value`
- Utilisé par : `Bat51RPdo1`
- Ligne export : 10485 · id 129530

#### BatCoolingPolicy  `GPOUT`
- Propriétés : Input value=0x14 · Length=8 · Type=Unsigned integer
- Utilisé par : `Bat51RPdo1`
- Ligne export : 10496 · id 129531

#### Bat51RPdo1  `GFOUT`
- Propriétés : Identifier=593 · Data length=8 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={{BatCommand; 0}; {BatCoolingPolicy; 8}} · Module=Batt BMW (Generic) · Module index=3
- Lit : `BatCommand`, `BatCoolingPolicy`
- Utilisé par : *(personne)*
- Ligne export : 10507 · id 129532

#### IsoMonCommand  `GPOUT`
- Propriétés : Input value=0x01 · Length=8 · Type=Unsigned integer
- Utilisé par : `Iso52MonRPdo1`
- Ligne export : 10529 · id 129533

#### Warning Level  `IP`
- Propriétés : Default mode={750}
- Utilisé par : `IsoMonWarningLevel`
- Ligne export : 10540 · id 129534

#### IsoMonWarningLevel  `GPOUT`
- Propriétés : Input value=Warning Level · Length=16 · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Warning Level`
- Utilisé par : `Iso52MonRPdo1`
- Ligne export : 10552 · id 129535

#### Error Level  `IP`
- Propriétés : Default mode={250}
- Utilisé par : `IsoMonErrorLevel`
- Ligne export : 10564 · id 129536

#### IsoMonErrorLevel  `GPOUT`
- Propriétés : Input value=Error Level · Length=16 · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Error Level`
- Utilisé par : `Iso52MonRPdo1`
- Ligne export : 10576 · id 129537

#### Iso52MonRPdo1  `GFOUT`
- Propriétés : Identifier=0x252 · Data length=8 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={{IsoMonCommand; 0}; {IsoMonWarningLevel; 8}; {IsoMonErrorLevel; 24}} · Module=Batt BMW (Generic) · Module index=4
- Lit : `IsoMonCommand`, `IsoMonErrorLevel`, `IsoMonWarningLevel`
- Utilisé par : *(personne)*
- Ligne export : 10588 · id 129538

#### Bat51TPdo2  `GFIN`
- Propriétés : Identifier=0x2D1 · Data length=Dont care · Timeout=5000 · Paged protocol={Not used} · Parameters={{BatAvgTemp; 0}; {BatMinCellTemp; 8}; {BatMaxCellTemp bmw; 16}; {BatBalancingState; 24}; {BatTimeToFullMinute; 32}} · Module=Batt BMW (Generic) · Module index=5
- Lit : `BatAvgTemp`, `BatBalancingState`, `BatMaxCellTemp bmw`, `BatMinCellTemp`, `BatTimeToFullMinute`
- Utilisé par : *(personne)*
- Ligne export : 10613 · id 129539

#### BatAvgTemp  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Bat51TPdo2`
- Ligne export : 10644 · id 129540

#### BatMinCellTemp  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Bat51TPdo2`
- Ligne export : 10656 · id 129541

#### BatMaxCellTemp bmw  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `BMW - Cell_T_max_Master`, `Bat51TPdo2`, `Battery temp ok`
- Ligne export : 10668 · id 129542

#### BatBalancingState  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `Bat51TPdo2`
- Ligne export : 10680 · id 129543

#### BatTimeToFullMinute  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51TPdo2`
- Ligne export : 10692 · id 129544

#### Bat51TPdo3  `GFIN`
- Propriétés : Identifier=0x3D1 · Data length=Dont care · Timeout=2000 · Paged protocol={Not used} · Parameters={{BatPowerLimitChargeRaw; 0}; {BatPowerLimitDischargeRaw; 16}; {BatEnergyRemainingRaw; 32}} · Module=Batt BMW (Generic) · Module index=6
- Lit : `BatEnergyRemainingRaw`, `BatPowerLimitChargeRaw`, `BatPowerLimitDischargeRaw`
- Utilisé par : *(personne)*
- Ligne export : 10705 · id 129545

#### BatPowerLimitChargeRaw  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51TPdo3`, `BatPowerLimitCharge`
- Ligne export : 10730 · id 129546

#### BatPowerLimitDischargeRaw  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51TPdo3`, `BatPowerLimitDischarge`
- Ligne export : 10743 · id 129547

#### BatEnergyRemainingRaw  `GPIN`
- Propriétés : Length=32 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51TPdo3`, `BatEnergyRemaining`
- Ligne export : 10756 · id 129548

#### BMW_-_Battery_InstantVoltage  `MAC`
- Propriétés : Unit=V
- Logique :
  ```qcode
  Result := BatPackVoltage bmw * 0.1
  ```
- Lit : `BatPackVoltage bmw`
- Utilisé par : `Battery InstantVoltage`, `CPI_BMS_U_Trac`, `Measure group: Battery BMW`
- Ligne export : 10769 · id 129549

#### BMW - CURRENT  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result := BatCurrent * 0.02 - 640
  ```
- Lit : `BatCurrent`
- Utilisé par : `Current Bat`, `Measure group: Battery BMW`
- Ligne export : 10787 · id 129559

#### BMW - Cell_T_max_Master  `MAC`
- Propriétés : Unit=°C
- Logique :
  ```qcode
  Result := BatMaxCellTemp bmw - 40
  ```
- Lit : `BatMaxCellTemp bmw`
- Utilisé par : `Cell_T_max_Master`, `Measure group: Battery BMW`
- Ligne export : 10805 · id 129570

#### BMW_-_U_Trac  `MAC`
- Propriétés : Unit=V
- Logique :
  ```qcode
  Result := BatBusVoltage utrac bmw * 0.1
  ```
- Lit : `BatBusVoltage utrac bmw`
- Utilisé par : `BMS_U_Trac`, `BMW- Max Current`, `Measure group: Battery BMW`
- Ligne export : 10823 · id 129588

#### DcuNodeState  `SMC`
- Propriétés : Default state name=Boot
- Fonction *Stopped* :
  - **Activating** = `DcuNodeState = 4`
- Fonction *Operational* :
  - **Activating** = `DcuNodeState = 5`
- Fonction *Pre-Op* :
  - **Activating** = `DcuNodeState = 127`
- Lit : `DcuNodeState`
- Utilisé par : `Dcu50Heartbeat`, `Init Seq`
- Ligne export : 10841 · id 129598

#### BatNodeState  `SMC`
- Propriétés : Default state name=Boot
- Fonction *Stopped* :
  - **Activating** = `BatNodeState = 4`
- Fonction *Operational* :
  - **Activating** = `BatNodeState = 5`
- Fonction *Pre-Op* :
  - **Activating** = `BatNodeState = 127`
- Lit : `BatNodeState`
- Utilisé par : `Bat51Hartbeat`, `Init Seq`
- Ligne export : 10949 · id 129614

#### IsoMonNodeState  `SMC`
- Propriétés : Default state name=Boot
- Fonction *Stopped* :
  - **Activating** = `IsoMonNodeState = 4`
- Fonction *Operational* :
  - **Activating** = `IsoMonNodeState = 5`
- Fonction *Pre-Op* :
  - **Activating** = `IsoMonNodeState = 127`
- Lit : `IsoMonNodeState`
- Utilisé par : `Init Seq`, `Iso52MonHeartbeat`
- Ligne export : 11057 · id 129630

#### BMW - SOC  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `BatStateOfCharge bmw * 0,5`
- Lit : `BatStateOfCharge bmw`
- Utilisé par : `Battery SOC`, `Measure group: Battery BMW`
- Ligne export : 11165 · id 129646

#### BMW CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  - **Activating** = `Dcu50Heartbeat`
- Lit : `Dcu50Heartbeat`
- Utilisé par : `BMW - CHARGE`, `Battery CAN OK`, `Battery CAN OK delay`, `Battery STANDBY`, `Charger CAN BUS OK`, `Measure group: Battery BMW`
- Ligne export : 11209 · id 129654

#### Dcu50Error  `GFIN`
- Propriétés : Identifier=208 · Data length=Dont care · Paged protocol={Not used} · Parameters={{DcuErrorCode; 24}; {DcuError; 8}} · Module=Batt BMW (Generic) · Module index=7
- Lit : `DcuError`, `DcuErrorCode`
- Utilisé par : *(personne)*
- Ligne export : 11252 · id 129662

#### DcuErrorCode  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Dcu50Error`, `DcuErrorCode M`, `DcuErrorCode Out`, `DcuErrorCode TF`
- Ligne export : 11274 · id 129663

#### Bat51Error  `GFIN`
- Propriétés : Identifier=0xD1 · Data length=Dont care · Paged protocol={Not used} · Parameters={{BatErrorCode; 24}; {BatError; 8}} · Module=Batt BMW (Generic) · Module index=8
- Lit : `BatError`, `BatErrorCode`
- Utilisé par : *(personne)*
- Ligne export : 11287 · id 129664

#### BatErrorCode  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Bat51Error`, `BatErrorCode M`, `BatErrorCode Out`, `BatErrorCode TF`, `Battery Error Code`, `New Error Code`
- Ligne export : 11309 · id 129665

#### Iso52MonError  `GFIN`
- Propriétés : Identifier=210 · Data length=Dont care · Paged protocol={Not used} · Parameters={{IsoMonErrorCode; 24}; {IsoMonError; 8}} · Module=Batt BMW (Generic) · Module index=9
- Lit : `IsoMonError`, `IsoMonErrorCode`
- Utilisé par : *(personne)*
- Ligne export : 11322 · id 129666

#### IsoMonErrorCode  `GPIN`
- Propriétés : Length=16 · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Iso52MonError`, `IsoMonErrorCode M`, `IsoMonErrorCode Out`, `IsoMonErrorCode TF`
- Ligne export : 11344 · id 129667

#### BMW - ERROR DIGIT  `IDC`
- Propriétés : Toggle=No · Delay on=100 · Delay off=100
- Utilisé par : `Battery ERROR DIGIT`, `Measure group: Battery BMW`
- Ligne export : 11357 · id 129668

#### BMW - DRIVE MODE  `IDC`
> Kreisel 
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `BatState = 2`
- Lit : `BatState`
- Utilisé par : `Battery DRIVE MODE`, `Measure group: Battery BMW`
- Ligne export : 11393 · id 129675

#### BatPowerLimitCharge  `MAC`
- Propriétés : Unit=kW
- Logique :
  ```qcode
  Result := BatPowerLimitChargeRaw * 0.01 - 320
  ```
- Lit : `BatPowerLimitChargeRaw`
- Utilisé par : `Measure group: Battery BMW`
- Ligne export : 11438 · id 129683

#### BatPowerLimitDischarge  `MAC`
- Propriétés : Unit=kW
- Logique :
  ```qcode
  Result := BatPowerLimitDischargeRaw * 0.01 - 320
  ```
- Lit : `BatPowerLimitDischargeRaw`
- Utilisé par : `BMW- Max Current`, `Measure group: Battery BMW`
- Ligne export : 11456 · id 129694

#### BatEnergyRemaining  `MAC`
- Propriétés : Unit=kWh
- Logique :
  ```qcode
  Result := BatEnergyRemainingRaw * 0.001
  ```
- Lit : `BatEnergyRemainingRaw`
- Utilisé par : `Measure group: Battery BMW`
- Ligne export : 11474 · id 129705

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
- Ligne export : 11492 · id 129715

#### DcuError  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `Dcu50Error`
- Ligne export : 11516 · id 129732

#### BatError  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `Bat51Error`
- Ligne export : 11528 · id 129733

#### IsoMonError  `GPIN`
- Propriétés : Length=1 · Type=Signed integer · Error value=0
- Utilisé par : `Iso52MonError`
- Ligne export : 11540 · id 129734

#### New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `BatErrorCode <> Battery Error Code`
- Lit : `BatErrorCode`, `Battery Error Code`
- Utilisé par : `Battery Error Code`, `Event log: BMW Battery`
- Ligne export : 11552 · id 129735

#### Battery Error Code  `MEM`
- Propriétés : Input channel=BatErrorCode · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(New Error Code)`
- Lit : `BatErrorCode`, `New Error Code`
- Utilisé par : `New Error Code`
- Ligne export : 11597 · id 129743

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
- Ligne export : 11642 · id 129751

#### DcuErrorCode P  `SP`
- Propriétés : Input channel=DcuErrorCode M · Default state name=0 · States={4097; 8192}
- Lit : `DcuErrorCode M`
- Utilisé par : `DcuErrorCode T`
- Ligne export : 11666 · id 129768

#### DcuErrorCode T  `TP`
- Propriétés : Mode selector=DcuErrorCode P · Default mode: 0={NoError} · Mode 1: 4097={HVIL_Fail} · Mode 2: 8192={EMCY_Off}
- Lit : `DcuErrorCode P`
- Utilisé par : `DcuErrorCode TF`
- Ligne export : 11679 · id 129771

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
- Ligne export : 11694 · id 129772

#### BatErrorCode P  `SP`
- Propriétés : Input channel=BatErrorCode M · Default state name=0 · States={4097; 4098; 4099; 8193; 12289; 12290; 12291; 12292; 16385; 20481; 24577; 28673; 32769; 40961; 40962; 40963; 40964; 40965; 40966; 40967; 40968; 40969; 40970; 40971; 40972; 40973; 40974; 40975; 40976; 40977; 40978; 40979; 40980; 40981; 40982; 40983; 40984; 40985; 40992; 40993; 45057; 45058; 45059; 45060; 45061; 45062; 45063; 45064; 45065; 49153; 49154; 53249; 65280}
- Lit : `BatErrorCode M`
- Utilisé par : `BatErrorCode T`
- Ligne export : 11820 · id 129993

#### BatErrorCode T  `TP`
- Propriétés : Mode selector=BatErrorCode P · Default mode: 0={NoError} · Mode 1: 4097={OneContactorSticky} · Mode 2: 4098={TwoContactorsSticky} · Mode 3: 4099={PrechargeLock} · Mode 4: 8193={Pack_OverVoltage} · Mode 5: 12289={Pack_UnderVoltage} · Mode 6: 12290={SocLow} · Mode 7: 12291={SocVeryLow} · Mode 8: 12292={SocCriticalLow} · Mode 9: 16385={Bus_OverVoltage} · Mode 10: 20481={Bus_UnderVoltage} · Mode 11: 24577={HVIL_Fail} · Mode 12: 28673={Communication_Error} · Mode 13: 32769={OverCurrent} · Mode 14: 40961={TemperatureHigh} · Mode 15: 40962={TemperatureLow} · Mode 16: 40963={CoolingCompConnLost} · Mode 17: 40964={CoolingModuleConnLost} · Mode 18: 40965={CoolingCompDrOvertemp} · Mode 19: 40966={CoolingCompDrOvercurrent} · Mode 20: 40967={CoolingCompSdOverUnderVoltage} · Mode 21: 40968={CoolingCompSdCriticalOvertemp} · Mode 22: 40969={CoolingCompSdTorqueExceeded} · Mode 23: 40970={CoolingCompSdLinCommError} · Mode 24: 40971={CoolingCompSdExternalSupply} · Mode 25: 40972={CoolingCompSdErrorInverterSupply} · Mode 26: 40973={CoolingCompSdErrorSensor} · Mode 27: 40974={CoolingCompSdShortcircuit} · Mode 28: 40975={CoolingCompSdRunUp} · Mode 29: 40976={CoolingWaterFlowLow} · Mode 30: 40977={CoolingWaterFlowImplausible} · Mode 31: 40978={CoolingWaterFlowVariation} · Mode 32: 40979={CoolingWaterTempLow} · Mode 33: 40980={CoolingWaterTempHigh} · Mode 34: 40981={CoolingWaterTempDiffLow} · Mode 35: 40982={CoolingPresLow} · Mode 36: 40983={CoolingPresHigh} · Mode 37: 40984={CoolingWaterInTempSensor} · Mode 38: 40985={CoolingWaterOutTempSensor} · Mode 39: 40992={CoolingModulePdo2Missing} · Mode 40: 40993={CoolingModulePdo3Missing} · Mode 41: 45057={Internal_Error} · Mode 42: 45058={ServiceDisconnect} · Mode 43: 45059={AbortCharging} · Mode 44: 45060={CoolingValveShortToGround} · Mode 45: 45061={CoolingValveShortToUbat} · Mode 46: 45062={CoolingValveWireBroken} · Mode 47: 45063={CoolingValveDriverError} · Mode 48: 45064={CoolingValveValveStuckAtClosed} · Mode 49: 45065={CoolingValveValveStuckAtOpen} · Mode 50: 49153={Category6Failure} · Mode 51: 49154={Category7Failure} · Mode 52: 53249={ThermalEventHazard} · Mode 53: 65280={DeviceSoftwareGenericFail}
- Lit : `BatErrorCode P`
- Utilisé par : `BatErrorCode TF`
- Ligne export : 11884 · id 130047

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
- Ligne export : 12001 · id 130048

#### IsoMonErrorCode P  `SP`
- Propriétés : Input channel=IsoMonErrorCode M · Default state name=0 · States={4097; 8193; 12289; 16385; 16386; 20481; 65280}
- Lit : `IsoMonErrorCode M`
- Utilisé par : `IsoMonErrorCode T`
- Ligne export : 12033 · id 130081

#### IsoMonErrorCode T  `TP`
- Propriétés : Mode selector=IsoMonErrorCode P · Default mode: 0={NoError} · Mode 1: 4097={IsoMeasurementNotWorking} · Mode 2: 8193={PlausibilityCheckFailed} · Mode 3: 12289={Warning_Level} · Mode 4: 16385={Error_Intern_Level} · Mode 5: 16386={Error_Extern_Level} · Mode 6: 20481={CommunicationError} · Mode 7: 65280={DeviceSoftwareGenericFail}
- Lit : `IsoMonErrorCode P`
- Utilisé par : `IsoMonErrorCode TF`
- Ligne export : 12051 · id 130089

#### DcuErrorCode TF  `TFC`
- Propriétés : Delimiter=_ · Texts={{DcuErrorCode; Value; 0}; {DcuErrorCode T; Value; 0}}
- Lit : `DcuErrorCode`, `DcuErrorCode T`
- Utilisé par : `Measure group: Battery BMW`
- Ligne export : 12076 · id 130090

#### BatErrorCode TF  `TFC`
- Propriétés : Delimiter=_ · Texts={{BatErrorCode; Value; 0}; {BatErrorCode T; Value; 0}}
- Lit : `BatErrorCode`, `BatErrorCode T`
- Utilisé par : `Event log: BMW Battery`, `Measure group: Battery BMW`
- Ligne export : 12094 · id 130091

#### IsoMonErrorCode TF  `TFC`
- Propriétés : Delimiter=_ · Texts={{IsoMonErrorCode; Value; 0}; {IsoMonErrorCode T; Value; 0}}
- Lit : `IsoMonErrorCode`, `IsoMonErrorCode T`
- Utilisé par : `Measure group: Battery BMW`
- Ligne export : 12112 · id 130092

#### IsoMonState bmw  `SP`
- Propriétés : Input channel=IsoMonState · Default state name=Reset · States={SelfCheck; RunningValueInvalid; RunningValueValid; Device Error}
- Lit : `IsoMonState`
- Utilisé par : `BMW/tyva - Bender Error`, `IsoMonTriggerRecord (iso value valid)`, `Measure group: Battery BMW`
- Ligne export : 12130 · id 130093

#### BatState  `SP`
- Propriétés : Input channel=BatState · Default state name=Reset · States={Precharging; Connected; Device Com Error; Precharge Error; Device Error; Disconnecte_Error; Disconnect}
- Lit : `BatState`
- Utilisé par : `BMW - DRIVE MODE`, `BMW New Battery State`, `Bat51TPdo1`, `Battery State MEM`, `Event log: BMW Battery`, `Measure group: Battery BMW`
- Ligne export : 12145 · id 130098

#### BMW New Battery State  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `BatState <> Battery State MEM`
- Lit : `BatState`, `Battery State MEM`
- Utilisé par : `Battery State MEM`
- Ligne export : 12163 · id 130106

#### Battery State MEM  `MEM`
- Propriétés : Input channel=BatState · Action=Replace · Store value=No
- Logique :
  - **Activating** = `PositiveFlank(BMW New Battery State)`
- Lit : `BMW New Battery State`, `BatState`
- Utilisé par : `BMW New Battery State`
- Ligne export : 12208 · id 130114

#### BatErrorCode Out  `GPOUT`
- Propriétés : Input value=BatErrorCode · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `BatErrorCode`
- Utilisé par : *(personne)*
- Ligne export : 12252 · id 130122

#### DcuErrorCode Out  `GPOUT`
- Propriétés : Input value=DcuErrorCode · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `DcuErrorCode`
- Utilisé par : *(personne)*
- Ligne export : 12264 · id 130123

#### IsoMonErrorCode Out  `GPOUT`
- Propriétés : Input value=IsoMonErrorCode · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `IsoMonErrorCode`
- Utilisé par : *(personne)*
- Ligne export : 12276 · id 130124

#### Battery State Request  `FGI`
- Propriétés : Input type=State · Input=E.Battery CMD · Default state name=Sleep · States={StandBy; Discharge; Charge}
- Lit : `E.Battery CMD`, `State`
- Utilisé par : `BMW Battery CMD`
- Ligne export : 12288 · id 130126

#### BMW - CHARGE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(BMW Battery CMD = 2) AND (BMW CAN OK)`
- Lit : `BMW Battery CMD`, `BMW CAN OK`
- Utilisé par : `Battery CHARGE`
- Ligne export : 12303 · id 130172

#### bmw batt can nok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Dcu50Heartbeat Status = Not evaluated) OR (Dcu50Heartbeat Status = Timeout)`
- Lit : `Dcu50Heartbeat`
- Utilisé par : `Battery InstantVoltage ok`, `Battery soc ok`, `Battery temp ok`, `Battery u trac/cpi volt ok`
- Ligne export : 12361 · id 233135

#### bmw isomon ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `IsoMonResistance BMW Status = OK`
- Lit : `IsoMonResistance BMW`
- Utilisé par : `Battery r isomon ok`
- Ligne export : 12415 · id 233172

## mc.Electric / E.BATTERY / E.Kresel — actif seulement si `Is_Kreisel`

#### 912 mBMS_Bat_Info_Master  `GFIN`
- Propriétés : Identifier=912 · Data length=8 · Timeout=2000 · Paged protocol={Not used} · Parameters={{BMS_SOC_Master; 48}; {BMS_I_Batt_Maste [A]; 0}; {BMS_U_Batt_Master; 16}} · Module=Battery Kreisel (Generic) · Module index=1
- Lit : `BMS_I_Batt_Maste`, `BMS_SOC_Master`, `BMS_U_Batt_Master`
- Utilisé par : *(personne)*
- Ligne export : 22976 · id 234006

#### BMS_SOC_Master  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `912 mBMS_Bat_Info_Master`, `Battery Real SOC`, `Kreisel - SOC`
- Ligne export : 23001 · id 234007

#### BMS_U_Batt_Master  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `912 mBMS_Bat_Info_Master`, `Kreisel - Battery InstantVoltage`
- Ligne export : 23014 · id 234008

#### Kreisel - Battery InstantVoltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `BMS_U_Batt_Master * 0,1`
- Lit : `BMS_U_Batt_Master`
- Utilisé par : `Battery InstantVoltage`
- Ligne export : 23027 · id 234009

#### Kreisel - SOC  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin((BMS_SOC_Master * 0,01): 5->0, 85->100, Freeze)`
- Lit : `BMS_SOC_Master`
- Utilisé par : `Battery SOC`
- Ligne export : 23071 · id 234017

#### BMS_I_Batt_Maste  `GPIN`
- Propriétés : Unit=A · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `912 mBMS_Bat_Info_Master`, `Kreisel - CURRENT`
- Ligne export : 23127 · id 234026

#### Kreisel - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `BMS_I_Batt_Maste [A] * 0,1`
- Lit : `BMS_I_Batt_Maste`
- Utilisé par : `Current Bat`
- Ligne export : 23140 · id 234027

#### 913 mBMS_Cell_Info_Master  `GFIN`
- Propriétés : Identifier=913 · Data length=8 · Timeout=2000 · Paged protocol={Not used} · Parameters={{U_Cell_min_Master; 32}; {U_Cell_max_Master; 16}; {U_Cell_avg_Master; 0}; {Cell_T_max_Master; 48}; {Cell_T_min_Master; 56}} · Module=Battery Kreisel (Generic) · Module index=2
- Lit : `Cell_T_max_Master`, `Cell_T_min_Master`, `U_Cell_avg_Master`, `U_Cell_max_Master`, `U_Cell_min_Master`
- Utilisé par : *(personne)*
- Ligne export : 23184 · id 234035

#### Cell_T_max_Master  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `913 mBMS_Cell_Info_Master`, `Kreisel - Cell_T_max_Master`, `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Statistics log: Electronic Stats logs`
- Ligne export : 23215 · id 234036

#### Kreisel - Cell_T_max_Master  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Cell_T_max_Master * 1`
- Lit : `Cell_T_max_Master`
- Utilisé par : `Cell_T_max_Master`
- Ligne export : 23227 · id 234037

#### 257 mBMS_FuncSTAT  `GFIN`
- Propriétés : Identifier=257 · Data length=Dont care · Timeout=2000 · Paged protocol={Not used} · Parameters={{BMS_start_up_ready; 0}; {BMS_stay_alive; 1}; {BMS_iso_meas_act; 2}; {BMS_balancing_act; 3}; {BMS_reset_denied; 4}; {BMS_wakeup_active; 5}; {BMS_Master_available; 8}; {BMS_Master_MSW_Closed; 16}; {BMS_EmergencyState_Master; 24}} · Module=Battery Kreisel (Generic) · Module index=3
- Lit : `BMS_EmergencyState_Master`, `BMS_Master_MSW_Closed`, `BMS_Master_available`, `BMS_balancing_act`, `BMS_iso_meas_act`, `BMS_reset_denied`, `BMS_start_up_ready`, `BMS_stay_alive`, `BMS_wakeup_active`
- Utilisé par : `Kreisel - CAN OK`
- Ligne export : 23271 · id 234045

#### BMS_EmergencyState_Master  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`, `BMS_EmergencyState_Master_IDC`, `Kreisel - ERROR DIGIT`
- Ligne export : 23314 · id 234046

#### Kreisel - ERROR DIGIT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `BMS_EmergencyState_Master`
- Lit : `BMS_EmergencyState_Master`
- Utilisé par : `Battery ERROR CMG`, `Battery ERROR DIGIT`
- Ligne export : 23326 · id 234047

#### Switch Battery  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Kresel Battery CMD = 1) OR (Kresel Battery CMD = 2)`
- Lit : `Kresel Battery CMD`
- Utilisé par : `Func_MSW_Request_Master`
- Ligne export : 23369 · id 234055

#### 276 mBMS_Trac_Info  `GFIN`
- Propriétés : Identifier=276 · Data length=8 · Timeout=2000 · Paged protocol={Not used} · Parameters={{BMS_Iso_Resist; 16}; {BMS_U_Trac [dV]; 0}} · Module=Battery Kreisel (Generic) · Module index=4
- Lit : `BMS_Iso_Resist`, `BMS_U_Trac`
- Utilisé par : *(personne)*
- Ligne export : 23423 · id 234063

#### BMS_Iso_Resist  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `276 mBMS_Trac_Info`, `Kreisel - Iso_Resist`, `kreisel isomon ok`
- Ligne export : 23445 · id 234064

#### Kreisel - Iso_Resist  `MAC`
- Propriétés : Unit=kOhm · Limiting object group=Signed
- Logique :
  - **Controlling** = `BMS_Iso_Resist * 1`
- Lit : `BMS_Iso_Resist`
- Utilisé par : `Batt - Iso_Resist`
- Ligne export : 23458 · id 234065

#### BMS_Master_MSW_Closed  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`, `BMS_Master_MSW_Closed_IDC`, `BMS_Master_MSW_Opened_IDC`, `Kreisel - DRIVE MODE`
- Ligne export : 23502 · id 234073

#### Kreisel - DRIVE MODE  `IDC`
> Kreisel 
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `BMS_Master_MSW_Closed`
- Lit : `BMS_Master_MSW_Closed`
- Utilisé par : `Battery DRIVE MODE`
- Ligne export : 23514 · id 234074

#### Kreisel - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `257 mBMS_FuncSTAT`
- Lit : `257 mBMS_FuncSTAT`
- Utilisé par : `Battery CAN OK`, `Battery CAN OK delay`, `Battery STANDBY`, `kreisel - CHARGE`
- Ligne export : 23557 · id 234082

#### BMS_U_Trac  `GPIN`
- Propriétés : Unit=dV · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `276 mBMS_Trac_Info`, `Kreisel - U_Trac`, `MD4-10 page: INFO`
- Ligne export : 23600 · id 234090

#### Kreisel - U_Trac  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `BMS_U_Trac [dV] * 0,1`
- Lit : `BMS_U_Trac`
- Utilisé par : `BMS_U_Trac`
- Ligne export : 23613 · id 234091

#### 258 mBMS_ROE  `GFIN`
- Propriétés : Identifier=258 · Data length=Dont care · Timeout=100 · Paged protocol={Not used} · Parameters={{EVT_ErrNr_SC; 8}; {EVT_Context; 16}; {mBMS_ROE_Mux M; 0}} · Module=Battery Kreisel (Generic) · Module index=5
- Lit : `EVT_Context`, `EVT_ErrNr_SC`, `mBMS_ROE_Mux M`
- Utilisé par : *(personne)*
- Ligne export : 23657 · id 234099

#### EVT_ErrNr_SC  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `258 mBMS_ROE`, `Battery New Error Code`, `EVT_ErrNr_SC MEM`
- Ligne export : 23682 · id 234100

#### BMS_EmergencyState_Master_IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank((1 = BMS_EmergencyState_Master))`
- Lit : `BMS_EmergencyState_Master`
- Utilisé par : *(personne)*
- Ligne export : 23694 · id 234101

#### Battery New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `EVT_ErrNr_SC <> EVT_ErrNr_SC MEM`
- Lit : `EVT_ErrNr_SC`, `EVT_ErrNr_SC MEM`
- Utilisé par : `Battery ERROR CMG`, `EVT_ErrNr_SC MEM`
- Ligne export : 23747 · id 234110

#### EVT_ErrNr_SC MEM  `MEM`
- Propriétés : Input channel=EVT_ErrNr_SC · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(Battery New Error Code)`
- Lit : `Battery New Error Code`, `EVT_ErrNr_SC`
- Utilisé par : `Battery Error`, `Battery Error List`, `Battery New Error Code`
- Ligne export : 23792 · id 234118

#### Battery Error List  `SP`
- Propriétés : Input channel=EVT_ErrNr_SC MEM · Default state name=ERR_CSC_OVERVOLTAGE · States={ERR_CSC_UNDERVOLTAGE; ERR_CSC_WARNING; ERR_SSV_TIMEOUT; ERR_ISO_RESISTANCE; ERR_ACC_EMERGENCY; ERR_FLOW_CTR; ERR_CSC_EMERGENCY; ERR_PMB_EMERGENCY; ERR_INTERLOCK_MISSING; ERR_PMB_TIMEOUT; ERR_SSV_INTEROPERABLE; ERR_ISO_MEASUREMENT; ERR_PCB1_TEMPERATURE; ERR_PMB_LIMITS; ERR_NVRAM; ERR_LIFEDATA; ERR_HV_MEAS; ERR_TRAC_VOLTAGE; ERR_WD; ERR_CPU_TEST; ERR_RESET_MONITOR; ERR_ROM_MONITOR; ERR_RAM_MONITOR; ERR_STACK_MONITOR; ERR_PMB_WARNING; ERR_RESERVED_BIT_42; ERR_SSV_CONFIG_HARD; ERR_CSC_EMERG_SHORT_SUP; ERR_BCC_COM; ERR_SUPPLYVOLTAGE; ERR_REFVOLTAGE; ERR_SSV_EMERGENCY; ERR_SSV_WARNING; ERR_PMB_EMERG_SHORT_SUP; ERR_FLASH_MONITOR; ERR_SSV_SUPPLYVOTLAGE; ERR_SSV_WD; ERR_PMB_INTERNAL; ERR_MSW_AGE; ERR_PMB_OVT; ERR_PMB_OC_CHG; ERR_PMB_OC_DCHG; ERR_PMB_OVERVOLTAGE; ERR_CSC_INTERNAL; ERR_CSC_TIMEOUT; ERR_CSC_OVERTEMPERATUR; ERR_MSW_AGE_WRN; ERR_CSC_LIMITS; ERR_SSV_ALIVE_TEST; ERR_PMB_INTEROP; ERR_CSC_INTEROP; ERR_IL_TEST; ERR_PMB_EMERG_TEST; ERR_KL30C_TEST; ERR_WD_TEST; ERR_CRASH; ERR_ACC_EMERG_TEST; ERR_DATASETCONF; ERR_ADC; ERR_DATASET; ERR_CSC_DS_INTEROP; ERR_SSV_STARTUP_TEST; ERR_STARTUP; ERR_MSW_STUCK_TEST; ERR_MSWMINUS_CONTROL; ERR_MSWPLUS_CONTROL; ERR_MSW3_CONTROL; ERR_PMB_DS_INTEROP; ERR_SC_INTERNAL; ERR_ISO_SHORT; ERR_RTC; ERR_PRECHARGE1_POWER; ERR_PRECHARGE1_DIAG; ERR_MC_WD; ERR_MSWMINUS_STUCK; ERR_MSWPLUS_STUCK; ERR_MSW3_STUCK; RESERVED_BIT_46; RESERVED_BIT_47; ERR_PRECHARGE2_DIAG; ERR_PRECHARGE2_POWER; ERR_TIMERMANGEMENT; ERR_TASKSYSTEM; ERR_BSC_OP_9D23H; ERR_BSC_OP_10D; RESERVED_BIT_54; ERR_CSC_EMERG_TEST; ERR_SSV_REFVOLTAGE; ERR_SSV_DS_INTEROP; ERR_SPI_COM; ERR_CELL_OV_WARN; ERR_CELL_UV_WARN; ERR_PMB_OC_PRECH; Reserved_5E; Reserved_5F; STAT_CLOSE_NOT_POSSIBLE_WEAK; STAT_ISO_RES_WARNING; STAT_ISO_GND_WARNING}
- Lit : `EVT_ErrNr_SC MEM`
- Utilisé par : `Battery Error`
- Ligne export : 23837 · id 234126

#### Battery Error  `TFC`
- Propriétés : Texts={{EVT_ErrNr_SC MEM; Value; 0}; { - }; {Battery Error List; Value; 0}}
- Lit : `Battery Error List`, `EVT_ErrNr_SC MEM`
- Utilisé par : `Battery ERROR CMG`, `MsgInterlockCut`, `Adjust group: Master Battery`, `Adjust group: Master System Debug`
- Ligne export : 23946 · id 234225

#### Show battery Msg  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Battery ERROR CMG`
- Ligne export : 23966 · id 234226

#### Battery ERROR CMG  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=High Tension Battery · Channel=Battery Error
- Logique :
  - **Showing** = `(Battery New Error Code) AND (Kreisel - ERROR DIGIT) AND (Battery New Error Code <> 0)`
  - **Hiding** = `(NegativeFlank(Kreisel - ERROR DIGIT)) OR (not(Show battery Msg))`
- Lit : `Battery Error`, `Battery New Error Code`, `Kreisel - ERROR DIGIT`, `Show battery Msg`
- Utilisé par : *(personne)*
- Ligne export : 23979 · id 234227

#### U_Cell_min_Master  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `913 mBMS_Cell_Info_Master`, `Kreisel - LowCellVoltage`
- Ligne export : 24057 · id 234239

#### Kreisel - LowCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed
- Logique :
  - **Controlling** = `U_Cell_min_Master * 1`
- Lit : `U_Cell_min_Master`
- Utilisé par : `LowCellVoltage check bmw`
- Ligne export : 24070 · id 234240

#### U_Cell_max_Master  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `913 mBMS_Cell_Info_Master`, `Kreisel - HighCellVoltage`
- Ligne export : 24114 · id 234248

#### Kreisel - HighCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed
- Logique :
  - **Controlling** = `U_Cell_max_Master * 1`
- Lit : `U_Cell_max_Master`
- Utilisé par : `HighCellVoltage check bmw`
- Ligne export : 24127 · id 234249

#### U_Cell_avg_Master  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `913 mBMS_Cell_Info_Master`, `AvgCellVoltage`
- Ligne export : 24171 · id 234257

#### AvgCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Signed
- Logique :
  - **Controlling** = `U_Cell_avg_Master * 1`
- Lit : `U_Cell_avg_Master`
- Utilisé par : *(personne)*
- Ligne export : 24184 · id 234258

#### Cell_T_min_Master  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `913 mBMS_Cell_Info_Master`, `Cell_T_Min_Master`
- Ligne export : 24228 · id 234266

#### Cell_T_Min_Master  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Cell_T_min_Master * 1`
- Lit : `Cell_T_min_Master`
- Utilisé par : *(personne)*
- Ligne export : 24240 · id 234267

#### EVT_Context  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `258 mBMS_ROE`
- Ligne export : 24284 · id 234275

#### mBMS_ROE_Mux M  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `258 mBMS_ROE`
- Ligne export : 24297 · id 234276

#### BMS_start_up_ready  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`
- Ligne export : 24309 · id 234277

#### BMS_balancing_act  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`
- Ligne export : 24321 · id 234278

#### BMS_stay_alive  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`
- Ligne export : 24333 · id 234279

#### BMS_iso_meas_act  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`
- Ligne export : 24345 · id 234280

#### BMS_reset_denied  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`
- Ligne export : 24357 · id 234281

#### BMS_wakeup_active  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`
- Ligne export : 24369 · id 234282

#### BMS_Master_available  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `257 mBMS_FuncSTAT`, `BMS_Master_available_IDC`, `BMS_Master_not_available_IDC`
- Ligne export : 24381 · id 234283

#### 277 mBMS_Temp_Info  `GFIN`
- Propriétés : Identifier=277 · Data length=Dont care · Timeout=2000 · Paged protocol={Not used} · Parameters={{BMS_ext_Temp_Inlet; 32}; {BMS_ext_Temp_Outlet; 16}} · Module=Battery Kreisel (Generic) · Module index=6
- Lit : `BMS_ext_Temp_Inlet`, `BMS_ext_Temp_Outlet`
- Utilisé par : *(personne)*
- Ligne export : 24393 · id 234284

#### BMS_ext_Temp_Inlet  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `277 mBMS_Temp_Info`, `BMS_ext_Temp_Inlet`
- Ligne export : 24415 · id 234285

#### BMS_ext_Temp_Inlet  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `(BMS_ext_Temp_Inlet * 0,1) - 3276,8`
- Lit : `BMS_ext_Temp_Inlet`
- Utilisé par : `277 mBMS_Temp_Info`
- Ligne export : 24428 · id 234286

#### BMS_ext_Temp_Outlet  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `277 mBMS_Temp_Info`, `BMS_ext_Temp_Outlet`
- Ligne export : 24481 · id 234295

#### BMS_ext_Temp_Outlet  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `(BMS_ext_Temp_Outlet * 0,1) - 3276,8`
- Lit : `BMS_ext_Temp_Outlet`
- Utilisé par : `277 mBMS_Temp_Info`
- Ligne export : 24494 · id 234296

#### 304 mBMS_Version_1  `GFIN`
- Propriétés : Identifier=304 · Data length=Dont care · Timeout=2000 · Paged protocol={Not used} · Parameters={{VER_CSC_release; 56}; {VER_CSC_minor; 48}; {VER_CSC_major; 40}; {VER_MC_release; 32}; {VER_MC_minor; 24}; {VER_MC_major; 16}; {VER_MC_DS_CRC; 0}} · Module=Battery Kreisel (Generic) · Module index=7
- Lit : `VER_CSC_major`, `VER_CSC_minor`, `VER_CSC_release`, `VER_MC_DS_CRC`, `VER_MC_major`, `VER_MC_minor`, `VER_MC_release`
- Utilisé par : *(personne)*
- Ligne export : 24547 · id 234305

#### VER_CSC_release  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24584 · id 234306

#### VER_MC_release  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24596 · id 234307

#### VER_CSC_minor  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24608 · id 234308

#### VER_CSC_major  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24620 · id 234309

#### VER_MC_minor  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24632 · id 234310

#### VER_MC_major  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24644 · id 234311

#### VER_MC_DS_CRC  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24656 · id 234312

#### 305 mBMS_Version_2  `GFIN`
- Propriétés : Identifier=305 · Data length=Dont care · Timeout=2000 · Paged protocol={Not used} · Parameters={{VER_CSC_release; 56}; {VER_CSC_minor; 48}; {VER_CSC_major; 40}; {VER_MC_release; 32}; {VER_MC_minor; 24}; {VER_MC_major; 16}; {VER_MC_DS_CRC; 0}} · Module=Battery Kreisel (Generic) · Module index=0
- Lit : `VER_CSC_major`, `VER_CSC_minor`, `VER_CSC_release`, `VER_MC_DS_CRC`, `VER_MC_major`, `VER_MC_minor`, `VER_MC_release`
- Utilisé par : *(personne)*
- Ligne export : 24669 · id 234313

#### VER_CSC_release  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24706 · id 234314

#### VER_MC_release  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24718 · id 234315

#### VER_CSC_minor  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24730 · id 234316

#### VER_CSC_major  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24742 · id 234317

#### VER_MC_minor  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24754 · id 234318

#### VER_MC_major  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24766 · id 234319

#### VER_MC_DS_CRC  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `304 mBMS_Version_1`, `305 mBMS_Version_2`
- Ligne export : 24778 · id 234320

#### Func_sys_state_req  `GPOUT`
- Propriétés : Input value=1 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `2047 EXT_FuncRequest`
- Ligne export : 24791 · id 234321

#### Func_MSW_Request_Master  `GPOUT`
- Propriétés : Input value=Switch Battery · Length=1 bit · Type=Unsigned integer
- Lit : `Switch Battery`
- Utilisé par : `2047 EXT_FuncRequest`
- Ligne export : 24802 · id 234322

#### Func_iso_measurement  `GPOUT`
- Propriétés : Input value=1 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `2047 EXT_FuncRequest`
- Ligne export : 24813 · id 234323

#### 2047 EXT_FuncRequest  `GFOUT`
- Propriétés : Identifier=2047 · Data length=8 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={{Func_MSW_Request_Master; 0}; {Func_sys_state_req; 16}; {Func_iso_measurement; 8}} · Module=Battery Kreisel (Generic) · Module index=0
- Lit : `Func_MSW_Request_Master`, `Func_iso_measurement`, `Func_sys_state_req`
- Utilisé par : *(personne)*
- Ligne export : 24824 · id 234324

#### Battery Real SOC  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `BMS_SOC_Master * 0,01`
- Lit : `BMS_SOC_Master`
- Utilisé par : *(personne)*
- Ligne export : 24849 · id 234325

#### BMS_Master_available_IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank((1 = BMS_Master_available))`
- Lit : `BMS_Master_available`
- Utilisé par : *(personne)*
- Ligne export : 24893 · id 234333

#### BMS_Master_not_available_IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank((1 = BMS_Master_available))`
- Lit : `BMS_Master_available`
- Utilisé par : *(personne)*
- Ligne export : 24946 · id 234342

#### BMS_Master_MSW_Closed_IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank((1 = BMS_Master_MSW_Closed))`
- Lit : `BMS_Master_MSW_Closed`
- Utilisé par : *(personne)*
- Ligne export : 24999 · id 234351

#### BMS_Master_MSW_Opened_IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank((1 = BMS_Master_MSW_Closed))`
- Lit : `BMS_Master_MSW_Closed`
- Utilisé par : *(personne)*
- Ligne export : 25052 · id 234360

#### Kreisel- Max Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `146`
- Utilisé par : `Max Discharge`
- Ligne export : 25105 · id 234369

#### Kresel Battery CMD  `SMC`
- Propriétés : Default state name=STAND BY
- Fonction *ON* :
  - **Activating** = `Battery State Request = 2`
- Fonction *Charge* :
  - **Activating** = `Battery State Request = 3`
- Lit : `Battery State Request`
- Utilisé par : `Switch Battery`, `kreisel - CHARGE`
- Ligne export : 25147 · id 234579

#### Battery State Request  `FGI`
- Propriétés : Input type=State · Input=E.Battery CMD · Default state name=Sleep · States={StandBy; Discharge; Charge}
- Lit : `E.Battery CMD`, `State`
- Utilisé par : `Kresel Battery CMD`
- Ligne export : 25222 · id 234591

#### kreisel isomon ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `BMS_Iso_Resist Status = OK`
- Lit : `BMS_Iso_Resist`
- Utilisé par : `IsoMonTriggerRecord (iso value valid)`
- Ligne export : 25237 · id 234680

#### kreisel - CHARGE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Kresel Battery CMD = 2) AND (Kreisel - CAN OK)`
- Lit : `Kreisel - CAN OK`, `Kresel Battery CMD`
- Utilisé par : `Battery CHARGE`
- Ligne export : 25282 · id 234709

## mc.Electric / E.BATTERY / E.NovumTech — actif seulement si `Is_Novum`

#### Battery State Request  `FGI`
- Propriétés : Input type=State · Input=E.Battery CMD · Default state name=Sleep · States={StandBy; Discharge; Charge}
- Lit : `E.Battery CMD`, `State`
- Utilisé par : `Battery State`
- Ligne export : 13975 · id 130372

#### Battery State  `IP`
- Propriétés : Mode selector=Battery State Request · Default mode: Sleep={0x00} · Mode 1: StandBy={0x01} · Mode 2: Discharge={0x03} · Mode 3: Charge={0x02}
- Lit : `Battery State Request`
- Utilisé par : `BMSModeRequest`, `main batt on novum`
- Ligne export : 13990 · id 130376

#### BMSModeRequest  `GPOUT`
> Vehicle Mode Request To Battery: 0:Sleep/1:StandBy/2:Charge/3:Discharge
- Propriétés : Input value=Battery State · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Battery State`
- Utilisé par : `BMS_NTHT_Req`
- Ligne export : 14008 · id 130377

#### BMS_NTHT_Req  `GFOUT`
- Propriétés : Identifier=35697002 · Data length=1 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={{BMSModeRequest; 0}} · Module=Batt_Novum (Generic) · Module index=1
- Lit : `BMSModeRequest`
- Utilisé par : *(personne)*
- Ligne export : 14019 · id 130378

#### BMS_NTHT_G1_Info  `GFIN`
- Propriétés : Identifier=35697009 · Data length=Dont care · Paged protocol={Not used} · Parameters={{BmsMode; 0}; {SOC novum [%]; 8}; {SOH [%]; 16}; {SOE [%]; 24}; {ModulesCom; 32}; {InsulationState; 40}} · Module=Batt_Novum (Generic) · Module index=4
- Lit : `BmsMode`, `InsulationState`, `ModulesCom`, `SOC novum`, `SOE`, `SOH`
- Utilisé par : `Novum - CAN OK`
- Ligne export : 14038 · id 130379

#### BMS_NTHT_G2_Voltage  `GFIN`
- Propriétés : Identifier=35697010 · Data length=Dont care · Paged protocol={Not used} · Parameters={{BatteryVoltage novum [V]; 0}; {MinCellVolt [mV]; 16}; {MaxCellVolt [mV]; 32}; {MaxBatteryVoltage [V]; 48}} · Module=Batt_Novum (Generic) · Module index=5
- Lit : `BatteryVoltage novum`, `MaxBatteryVoltage`, `MaxCellVolt`, `MinCellVolt`
- Utilisé par : *(personne)*
- Ligne export : 14072 · id 130380

#### BMS_NTHT_G3_Current  `GFIN`
- Propriétés : Identifier=35697011 · Data length=Dont care · Paged protocol={Not used} · Parameters={{BatteryCurrent [A]; 0}; {MaxDischargeCurrent [A]; 16}; {MaxChargeCurrent [A]; 32}} · Module=Batt_Novum (Generic) · Module index=1
- Lit : `BatteryCurrent`, `MaxChargeCurrent`, `MaxDischargeCurrent`
- Utilisé par : *(personne)*
- Ligne export : 14100 · id 130381

#### BMS_NTHT_G4_Temperature  `GFIN`
- Propriétés : Identifier=35697012 · Data length=Dont care · Paged protocol={Not used} · Parameters={{MinTemp [°C]; 0}; {MaxTemp novum [°C]; 8}; {AverageTemp [°C]; 16}} · Module=Batt_Novum (Generic) · Module index=2
- Lit : `AverageTemp`, `MaxTemp novum`, `MinTemp`
- Utilisé par : *(personne)*
- Ligne export : 14125 · id 130382

#### BMS_NTHT_G5_Charger  `GFIN`
- Propriétés : Identifier=35697013 · Data length=8 · Paged protocol={Not used} · Parameters={{ChargeCurrentCmd [A]; 0}; {ChargeVoltageCmd [V]; 16}} · Module=Batt_Novum (Generic) · Module index=3
- Lit : `ChargeCurrentCmd`, `ChargeVoltageCmd`
- Utilisé par : *(personne)*
- Ligne export : 14150 · id 130383

#### BmsMode  `GPIN`
> Battery Current Mode. 0:Sleep/1:StandBy/2:Charge/3:Discharge
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_NTHT_G1_Info`, `Novum - CHARGE`, `Novum - DRIVE MODE`, `Novum - STANDBY`
- Ligne export : 14172 · id 130384

#### SOC novum  `GPIN`
> Battery State Of Charge in %
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_NTHT_G1_Info`, `Battery soc ok`, `Novum - SOC`
- Ligne export : 14184 · id 130385

#### SOH  `GPIN`
> Battery State Of Health in %
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_NTHT_G1_Info`, `Measure group: Battery Tyva`
- Ligne export : 14196 · id 130386

#### SOE  `GPIN`
> Battery State Of Energy in %
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_NTHT_G1_Info`
- Ligne export : 14208 · id 130387

#### ModulesCom  `GPIN`
> Number of Modules communicating
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_NTHT_G1_Info`
- Ligne export : 14220 · id 130388

#### InsulationState  `GPIN`
> IsoMon Measurement Status: 0:Init / 1:Processing / 2:OK / 3:Nok
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `BMS_NTHT_G1_Info`, `Novum - Bender Error`
- Ligne export : 14232 · id 130389

#### BatteryVoltage novum  `GPIN`
> Battery Voltage with 0.1 Factor
- Propriétés : Unit=V · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_NTHT_G2_Voltage`, `Battery InstantVoltage ok`, `Battery u trac/cpi volt ok`, `Novum - BatteryVoltage`
- Ligne export : 14244 · id 130390

#### MinCellVolt  `GPIN`
> Minimum Cell Voltage in mV
- Propriétés : Unit=mV · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_NTHT_G2_Voltage`, `Novum - MinCellVoltage`
- Ligne export : 14257 · id 130391

#### MaxCellVolt  `GPIN`
> Maximum Cell Voltage in mV
- Propriétés : Unit=mV · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_NTHT_G2_Voltage`, `Novum - MaxCellVoltage`
- Ligne export : 14270 · id 130392

#### MaxBatteryVoltage  `GPIN`
> Maximum Battery Voltage with 0.1 Factor
- Propriétés : Unit=V · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_NTHT_G2_Voltage`
- Ligne export : 14283 · id 130393

#### BatteryCurrent  `GPIN`
> Battery Current in Amps, Negative for discharge, 0.1 Factor
- Propriétés : Unit=A · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_NTHT_G3_Current`, `Novum - BatteryCurrent`
- Ligne export : 14296 · id 130394

#### MaxDischargeCurrent  `GPIN`
> Max Allowable Discharge Current in Amps, Factor 0.1
- Propriétés : Unit=A · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_NTHT_G3_Current`, `Novum - MaxDischargeBatteryCurrent`
- Ligne export : 14309 · id 130395

#### MaxChargeCurrent  `GPIN`
> Max Allowable Charge Current in Amps, Factor 0.1
- Propriétés : Unit=A · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_NTHT_G3_Current`
- Ligne export : 14322 · id 130396

#### MinTemp  `GPIN`
> Minimum Cell Temperature
- Propriétés : Unit=°C · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=-128
- Utilisé par : `BMS_NTHT_G4_Temperature`
- Ligne export : 14335 · id 130397

#### MaxTemp novum  `GPIN`
> Maximum Cell Temperature
- Propriétés : Unit=°C · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=-128
- Utilisé par : `BMS_NTHT_G4_Temperature`, `Battery temp ok`, `Novum - MaxTemp`
- Ligne export : 14347 · id 130398

#### AverageTemp  `GPIN`
> Average Battery Temperature
- Propriétés : Unit=°C · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=-128
- Utilisé par : `BMS_NTHT_G4_Temperature`
- Ligne export : 14359 · id 130399

#### ChargeCurrentCmd  `GPIN`
> Current request for charger, Factor 0.1
- Propriétés : Unit=A · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_NTHT_G5_Charger`, `Novum - ChargeCurrent`
- Ligne export : 14371 · id 130400

#### ChargeVoltageCmd  `GPIN`
> Voltage request for charger, Factor 0.1
- Propriétés : Unit=V · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMS_NTHT_G5_Charger`, `Novum - ChargeVoltage`
- Ligne export : 14384 · id 130401

#### BMS_NTHT_Errors novum  `GFIN`
- Propriétés : Identifier=35697008 · Data length=Dont care · Timeout=250 · Paged protocol={Not used} · Parameters={{ConfigFail; 0}; {SoftFailure; 1}; {SoftConsistencyError; 2}; {InterlockCut; 3}; {DCPowerDisconnection; 4}; {WarningOverChargeCurrent; 8}; {WarningOverDischargeCurrent; 9}; {WarningOverVoltage; 10}; {WarningUnderVoltage; 11}; {WarningOverTemp; 12}; {WarningLowTemp; 13}; {AlarmOverChargeCurrent; 16}; {AlarmOverDischargeCurrent; 17}; {AlarmOverVoltage; 18}; {AlarmUnderVoltage; 19}; {AlarmOverTemp; 20}; {AlarmLowTemp; 21}; {ShutdownOverChargeCurrent; 24}; {ShutdownOverDischargeCurrent; 25}; {ShutdownOverVoltage; 26}; {ShutdownUnderVoltage; 27}; {ShutdownOverTemp; 28}; {ShutdownLowTemp; 29}; {Contactor1Fail; 32}; {Contactor2Fail; 33}; {Contactor3Fail; 34}; {Contactor4Fail; 35}; {Contactor5Fail; 36}; {Contactor6Fail; 37}; {Contactor7Fail; 38}; {TempSensorFail; 40}; {VoltSensorFail; 41}; {CurrentSensorFail; 42}; {CANFail; 43}; {IsometerFail; 44}; {ModuleComLost; 45}; {BalancingRunning; 48}; {ChargeDone; 49}; {HeatingActivated; 50}; {CoolingActivated; 51}; {SOCRecalibration; 52}; {LowBMSSupply; 54}; {PrechargeFail; 55}; {SignalCrash; 46}; {IsometerWarning; 47}} · Module=Batt_Novum (Generic) · Module index=0
- Lit : `AlarmLowTemp`, `AlarmOverChargeCurrent`, `AlarmOverDischargeCurrent`, `AlarmOverTemp`, `AlarmOverVoltage`, `AlarmUnderVoltage`, `BalancingRunning`, `CANFail`, `ChargeDone`, `ConfigFail`, `Contactor1Fail`, `Contactor2Fail`, `Contactor3Fail`, `Contactor4Fail`, `Contactor5Fail`, `Contactor6Fail`, `Contactor7Fail`, `CoolingActivated`, `CurrentSensorFail`, `DCPowerDisconnection`, `HeatingActivated`, `InterlockCut`, `IsometerFail`, `IsometerWarning`, `LowBMSSupply`, `ModuleComLost`, `PrechargeFail`, `SOCRecalibration`, `ShutdownLowTemp`, `ShutdownOverChargeCurrent`, `ShutdownOverDischargeCurrent`, `ShutdownOverTemp`, `ShutdownOverVoltage`, `ShutdownUnderVoltage`, `SignalCrash`, `SoftConsistencyError`, `SoftFailure`, `TempSensorFail`, `VoltSensorFail`, `WarningLowTemp`, `WarningOverChargeCurrent`, `WarningOverDischargeCurrent`, `WarningOverTemp`, `WarningOverVoltage`, `WarningUnderVoltage`
- Utilisé par : `Battery r isomon ok`, `novum batt can nok`
- Ligne export : 14397 · id 130402

#### ConfigFail  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 14548 · id 130403

#### SoftFailure  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 14559 · id 130404

#### SoftConsistencyError  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 14570 · id 130405

#### InterlockCut  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `MsgInterlockCut`, `Event log: Novum battery`
- Ligne export : 14581 · id 130406

#### DCPowerDisconnection  `GPIN`
> Pops 1 if Battery is about to open its contactors
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_ERROR DIGIT`, `Event log: Novum battery`
- Ligne export : 14592 · id 130407

#### WarningOverChargeCurrent  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_WarningFlag`, `Event log: Novum battery`
- Ligne export : 14603 · id 130408

#### WarningOverDischargeCurrent  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_WarningFlag`, `Event log: Novum battery`
- Ligne export : 14614 · id 130409

#### WarningOverVoltage  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_WarningFlag`, `Event log: Novum battery`, `Event log: Tyva Battery`
- Ligne export : 14625 · id 130410

#### WarningOverTemp  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_WarningFlag`, `Event log: Novum battery`
- Ligne export : 14636 · id 130411

#### WarningLowTemp  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_WarningFlag`, `Event log: Novum battery`
- Ligne export : 14647 · id 130412

#### WarningUnderVoltage  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_LOW VOLTAGE ERROR  DIGIT`, `Event log: Novum battery`, `Event log: Tyva Battery`
- Ligne export : 14658 · id 130413

#### Novum_WarningFlag  `IDC`
> Pops out when Novum Battery raises a warning level Error. System needs to warn user and reduce power.
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `WarningOverChargeCurrent OR WarningOverDischargeCurrent OR WarningOverVoltage OR WarningOverTemp OR WarningLowTemp`
- Lit : `WarningLowTemp`, `WarningOverChargeCurrent`, `WarningOverDischargeCurrent`, `WarningOverTemp`, `WarningOverVoltage`
- Utilisé par : *(personne)*
- Ligne export : 14669 · id 130414

#### AlarmUnderVoltage  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_LOW VOLTAGE ERROR  DIGIT`, `Event log: Novum battery`
- Ligne export : 14740 · id 130426

#### AlarmOverChargeCurrent  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_AlarmFlag`, `Event log: Novum battery`
- Ligne export : 14751 · id 130427

#### AlarmOverDischargeCurrent  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_AlarmFlag`, `Event log: Novum battery`
- Ligne export : 14762 · id 130428

#### AlarmOverVoltage  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_AlarmFlag`, `Event log: Novum battery`
- Ligne export : 14773 · id 130429

#### AlarmOverTemp  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_AlarmFlag`, `Event log: Novum battery`
- Ligne export : 14784 · id 130430

#### AlarmLowTemp  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_AlarmFlag`, `Event log: Novum battery`
- Ligne export : 14795 · id 130431

#### Novum_AlarmFlag  `IDC`
> Pops out when Novum Battery raises a alarm level Error. System needs to shutdown.
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `AlarmOverChargeCurrent OR AlarmOverDischargeCurrent OR AlarmOverVoltage OR AlarmOverTemp OR AlarmLowTemp`
- Lit : `AlarmLowTemp`, `AlarmOverChargeCurrent`, `AlarmOverDischargeCurrent`, `AlarmOverTemp`, `AlarmOverVoltage`
- Utilisé par : `Novum_ERROR DIGIT`
- Ligne export : 14806 · id 130432

#### ShutdownUnderVoltage  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_LOW VOLTAGE ERROR  DIGIT`, `Event log: Novum battery`
- Ligne export : 14877 · id 130444

#### ShutdownOverChargeCurrent  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_ShutdownFlag`, `Event log: Novum battery`
- Ligne export : 14888 · id 130445

#### ShutdownOverDischargeCurrent  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_ShutdownFlag`, `Event log: Novum battery`
- Ligne export : 14899 · id 130446

#### ShutdownOverVoltage  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_ShutdownFlag`, `Event log: Novum battery`
- Ligne export : 14910 · id 130447

#### ShutdownOverTemp  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_ShutdownFlag`, `Event log: Novum battery`
- Ligne export : 14921 · id 130448

#### ShutdownLowTemp  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_ShutdownFlag`, `Event log: Novum battery`
- Ligne export : 14932 · id 130449

#### Novum_ShutdownFlag  `IDC`
> Pops out when Novum Battery raises a Shutdownlevel Error. Battery will stop.
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `ShutdownOverChargeCurrent OR ShutdownOverDischargeCurrent OR ShutdownOverVoltage OR ShutdownOverTemp OR ShutdownLowTemp`
- Lit : `ShutdownLowTemp`, `ShutdownOverChargeCurrent`, `ShutdownOverDischargeCurrent`, `ShutdownOverTemp`, `ShutdownOverVoltage`
- Utilisé par : `Novum_ERROR DIGIT`
- Ligne export : 14943 · id 130450

#### TempSensorFail  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_HardwareFailure`, `Event log: Novum battery`
- Ligne export : 15014 · id 130462

#### VoltSensorFail  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_HardwareFailure`, `Event log: Novum battery`
- Ligne export : 15025 · id 130463

#### CurrentSensorFail  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_HardwareFailure`, `Event log: Novum battery`
- Ligne export : 15036 · id 130464

#### CANFail  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_HardwareFailure`, `Event log: Novum battery`
- Ligne export : 15047 · id 130465

#### IsometerFail  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum - Isolation Error`, `Event log: Novum battery`
- Ligne export : 15058 · id 130466

#### Novum_HardwareFailure  `IDC`
> Pops out when Novum Battery raises a Shutdownlevel Error. Battery will stop.
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `TempSensorFail OR VoltSensorFail OR CurrentSensorFail OR CANFail`
- Lit : `CANFail`, `CurrentSensorFail`, `TempSensorFail`, `VoltSensorFail`
- Utilisé par : *(personne)*
- Ligne export : 15069 · id 130467

#### Novum_ERROR DIGIT  `IDC`
> Pops out when Novum Battery raises a warning level Error
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `DCPowerDisconnection OR Novum_AlarmFlag OR Novum_ShutdownFlag OR (eb Debug: Trig Battery Error)`
  - **Blocking** = `(eb Debug: Mute Battery Error) AND (not(eb Debug: Trig Battery Error))`
- Lit : `DCPowerDisconnection`, `Novum_AlarmFlag`, `Novum_ShutdownFlag`, `eb Debug: Mute Battery Error`, `eb Debug: Trig Battery Error`
- Utilisé par : `Battery ERROR DIGIT`
- Ligne export : 15133 · id 130480

#### Contactor1Fail  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15212 · id 130493

#### Contactor2Fail  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15223 · id 130494

#### Contactor3Fail  `GPIN`
> Pops 1 if Battery is about to open its contactors
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15234 · id 130495

#### Contactor4Fail  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15245 · id 130496

#### Contactor5Fail  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15256 · id 130497

#### Contactor6Fail  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15267 · id 130498

#### Contactor7Fail  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15278 · id 130499

#### ModuleComLost  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15289 · id 130500

#### BalancingRunning  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum BalancingRunning`, `Event log: Novum battery`
- Ligne export : 15300 · id 130501

#### ChargeDone  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum_EndOfCharge`, `Event log: Novum battery`
- Ligne export : 15311 · id 130502

#### HeatingActivated  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15322 · id 130503

#### CoolingActivated  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15333 · id 130504

#### SOCRecalibration  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15344 · id 130505

#### LowBMSSupply  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15355 · id 130506

#### PrechargeFail  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15366 · id 130507

#### eb Debug: Test End Of Charge  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Novum_EndOfCharge`, `Test End Of Charge Trigger`, `Single adjust item: Debug: Test End Of Charge`
- Ligne export : 15377 · id 130508

#### Novum_EndOfCharge  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `ChargeDone OR (eb Debug: Test End Of Charge)`
- Lit : `ChargeDone`, `eb Debug: Test End Of Charge`
- Utilisé par : `Battery CHARGED`
- Ligne export : 15390 · id 130509

#### Novum - DRIVE MODE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `BmsMode = 3`
- Lit : `BmsMode`
- Utilisé par : `Battery DRIVE MODE`, `Measure group: Battery NovumTech`
- Ligne export : 15440 · id 130518

#### Novum - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=200
- Logique :
  - **Activating** = `BMS_NTHT_G1_Info`
- Lit : `BMS_NTHT_G1_Info`
- Utilisé par : `Battery CAN OK`, `Battery CAN OK delay`, `Measure group: Battery NovumTech`
- Ligne export : 15485 · id 130526

#### Novum - BatteryVoltage  `MAC`
- Propriétés : Unit=V
- Logique :
  ```qcode
  Result:=BatteryVoltage novum / 10
  ```
- Lit : `BatteryVoltage novum`
- Utilisé par : `BMS_U_Trac`, `Battery InstantVoltage`, `CPI_BMS_U_Trac`, `Measure group: Battery NovumTech`
- Ligne export : 15528 · id 130534

#### Novum - BatteryCurrent  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result:=BatteryCurrent / 10
  ```
- Lit : `BatteryCurrent`
- Utilisé par : `Current Bat`, `Measure group: Battery NovumTech`
- Ligne export : 15546 · id 130544

#### Novum - MaxTemp  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxTemp novum [°C]`
- Lit : `MaxTemp novum`
- Utilisé par : `Cell_T_max_Master`, `Measure group: Battery NovumTech`
- Ligne export : 15564 · id 130554

#### Novum - Bender Error  `IDC`
> Set to 1 when Isolation measurement is not working
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `InsulationState = 3`
- Lit : `InsulationState`
- Utilisé par : `Measure group: Battery NovumTech`
- Ligne export : 15606 · id 130562

#### IsometerWarning  `GPIN`
> Isolation Value reaches a critical level
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Novum - Isolation Error`, `Event log: Novum battery`
- Ligne export : 15651 · id 130570

#### Novum - Isolation Error  `IDC`
> Set to 1 when Isolation value is too low
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `IsometerFail OR IsometerWarning`
- Lit : `IsometerFail`, `IsometerWarning`
- Utilisé par : `Error Iso_Resist`, `error 1st start`, `Event log: Battery Isolation`, `Measure group: Battery NovumTech`
- Ligne export : 15662 · id 130571

#### Novum - SOC  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `SOC novum [%]`
- Lit : `SOC novum`
- Utilisé par : `Battery SOC`, `Measure group: Battery NovumTech`
- Ligne export : 15712 · id 130580

#### Novum - MaxDischargeBatteryCurrent  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result:=MaxDischargeCurrent / 10
  ```
- Lit : `MaxDischargeCurrent`
- Utilisé par : `Max Discharge`, `Measure group: Battery NovumTech`
- Ligne export : 15754 · id 130588

#### Novum - ChargeCurrent  `MAC`
> Current requested by battery for charging in slave mode
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result:=ChargeCurrentCmd / 10
  ```
- Lit : `ChargeCurrentCmd`
- Utilisé par : `Measure group: Battery NovumTech`
- Ligne export : 15772 · id 130598

#### Novum - ChargeVoltage  `MAC`
> Voltage requested by battery for charging in slave mode
- Propriétés : Unit=V
- Logique :
  ```qcode
  Result:=ChargeVoltageCmd / 10
  ```
- Lit : `ChargeVoltageCmd`
- Utilisé par : `Measure group: Battery NovumTech`
- Ligne export : 15791 · id 130608

#### Novum - MinCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Unsigned
- Logique :
  - **Controlling** = `MinCellVolt [mV]`
- Lit : `MinCellVolt`
- Utilisé par : `LowCellVoltage check bmw`, `Measure group: Battery NovumTech`
- Ligne export : 15811 · id 130618

#### Novum - MaxCellVoltage  `MAC`
- Propriétés : Unit=mV · Limiting object group=Unsigned
- Logique :
  - **Controlling** = `MaxCellVolt [mV]`
- Lit : `MaxCellVolt`
- Utilisé par : `HighCellVoltage check bmw`, `Measure group: Battery NovumTech`
- Ligne export : 15853 · id 130626

#### Novum - STANDBY  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `BmsMode = 1`
- Lit : `BmsMode`
- Utilisé par : `Battery STANDBY`, `Measure group: Battery NovumTech`
- Ligne export : 15895 · id 130634

#### Novum - CHARGE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `BmsMode = 2`
- Lit : `BmsMode`
- Utilisé par : `Battery CHARGE`, `Measure group: Battery NovumTech`
- Ligne export : 15940 · id 130642

#### SignalCrash  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `BMS_NTHT_Errors novum`, `Event log: Novum battery`
- Ligne export : 15985 · id 130650

#### MsgInterlockCut  `CMSG`
- Propriétés : Show message=All · Dialog type=Critical · Header=Battery Error · Text=The Battery has detected an opening of the interlock and has disconnected for safety reasons. DO NOT open the power circuit without  authorization.
- Logique :
  - **Showing** = `InterlockCut`
- Lit : `Battery Error`, `InterlockCut`
- Utilisé par : *(personne)*
- Ligne export : 15996 · id 130651

#### Test End Of Charge Trigger  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `eb Debug: Test End Of Charge`
- Lit : `eb Debug: Test End Of Charge`
- Utilisé par : *(personne)*
- Ligne export : 16042 · id 130659

#### Novum_LOW VOLTAGE ERROR  DIGIT  `IDC`
> Pops out when Novum Battery raises a warning level Error
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `WarningUnderVoltage OR AlarmUnderVoltage OR ShutdownUnderVoltage OR (eb Debug: Trig Battery Low Voltage Error)`
  - **Blocking** = `(eb Debug: Mute Battery Error) AND (not(eb Debug: Trig Battery Low Voltage Error))`
- Lit : `AlarmUnderVoltage`, `ShutdownUnderVoltage`, `WarningUnderVoltage`, `eb Debug: Mute Battery Error`, `eb Debug: Trig Battery Low Voltage Error`
- Utilisé par : `Battery LOW VOLTAGE ERROR DIGIT`
- Ligne export : 16085 · id 130668

#### eb Trig Debug Cell Voltage  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `BMS_Debug_CellVotage`, `Single adjust item: Trig Debug Cell Voltage`
- Ligne export : 16164 · id 130681

#### TrigCellVoltageFrame1  `GPOUT`
- Propriétés : Input value=0x26 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `BMS_Debug_CellVotage`
- Ligne export : 16177 · id 130682

#### TrigCellVoltageFrame2  `GPOUT`
- Propriétés : Input value=0x0E · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `BMS_Debug_CellVotage`
- Ligne export : 16188 · id 130683

#### TrigCellVoltageFrame3  `GPOUT`
- Propriétés : Input value=0xE7 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `BMS_Debug_CellVotage`
- Ligne export : 16199 · id 130684

#### TrigCellVoltageFrame4  `GPOUT`
- Propriétés : Input value=0x1A · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `BMS_Debug_CellVotage`
- Ligne export : 16210 · id 130685

#### BMS_Debug_CellVotage  `GFOUT`
- Propriétés : Identifier=0x220B16B · Data length=8 · Send method=On trigger · Trigger=eb Trig Debug Cell Voltage · Unused bits=Set to 0 · Parameters={{TrigCellVoltageFrame1; 24}; {TrigCellVoltageFrame2; 32}; {TrigCellVoltageFrame3; 40}; {TrigCellVoltageFrame4; 48}} · Module=Batt_Novum (Generic) · Module index=0
- Lit : `TrigCellVoltageFrame1`, `TrigCellVoltageFrame2`, `TrigCellVoltageFrame3`, `TrigCellVoltageFrame4`, `eb Trig Debug Cell Voltage`
- Utilisé par : *(personne)*
- Ligne export : 16221 · id 130686

#### Novum BalancingRunning  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `BalancingRunning OR (trig balancing)`
- Lit : `BalancingRunning`, `trig balancing`
- Utilisé par : `Charger end of charge but balancing`, `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 16250 · id 130687

#### main batt on novum  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Battery State = 1) OR (Battery State = 2) OR (Battery State = 3)`
- Lit : `Battery State`
- Utilisé par : *(personne)*
- Ligne export : 16300 · id 232900

#### novum batt can nok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(BMS_NTHT_Errors novum Status = Not evaluated) OR (BMS_NTHT_Errors novum Status = Timeout)`
- Lit : `BMS_NTHT_Errors novum`
- Utilisé par : `Battery InstantVoltage ok`, `Battery soc ok`, `Battery temp ok`, `Battery u trac/cpi volt ok`
- Ligne export : 16363 · id 233122

#### trig balancing  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Novum BalancingRunning`, `Adjust group: Master Features`, `Single adjust item: trig balancing`
- Ligne export : 16417 · id 235525

## mc.Electric / E.CHARGER
> General Charger manamgement: Charger is a battery client, managed by a state machine for transition, and a state variable for its current status. It waits for battery acknoledgement to turn on or off

#### ec Charger Brand  `SP`
- Propriétés : Input channel=None · Default state name=BMW · States={Brusa; Elcon}
- Utilisé par : `Charger Output Current`, `Charger Output Voltage`, `Is_Charger_BMW`, `Is_Charger_Brusa`, `Is_Charger_Elcon`, `Single adjust item: Charger Brand`
- Ligne export : 25371 · id 130782

#### Is_Charger_Elcon  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `ec Charger Brand = 2`
- Lit : `ec Charger Brand`
- Utilisé par : `Active le groupe: mc.Electric / E.CHARGER / E.Charger_Elcon`, `Measure group: Charger Elcon`
- Ligne export : 25384 · id 130786

#### Charger CONNECT to 220V  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(BMW Connected) OR (Elcon Connected) OR (Brusa Connected)`
- Lit : `BMW Connected`, `Brusa Connected`, `Elcon Connected`
- Utilisé par : `Charger Connected`, `Charger Reset State`, `Charger State Feed-back`
- Ligne export : 25429 · id 130794

#### Charger READY  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `(BMW Ready) OR (Elcon Ready) OR (Brusa ready)`
- Lit : `BMW Ready`, `Brusa ready`, `Elcon Ready`
- Utilisé par : *(personne)*
- Ligne export : 25486 · id 130804

#### Charger CHARGING  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `(BMW Charging) OR (Elcon Charging) OR (Brusa Charging)`
- Lit : `BMW Charging`, `Brusa Charging`, `Elcon Charging`
- Utilisé par : `Charger State Feed-back`, `Global Auto Off Timer`
- Ligne export : 25543 · id 130814

#### Charger ERROR  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=100
- Logique :
  - **Activating** = `(BMW Error) OR (Elcon Error) OR (Brusa Error)`
- Lit : `BMW Error`, `Brusa Error`, `Elcon Error`
- Utilisé par : `Charger REQ`, `Charger State Feed-back`
- Ligne export : 25600 · id 130824

#### Charger Reset State  `IDC`
> Resetting the Charger State when unplugged from AC
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank(Charger CONNECT to 220V)`
- Lit : `Charger CONNECT to 220V`
- Utilisé par : `E.Charging State Machine`
- Ligne export : 25657 · id 130834

#### Charger CAN BUS OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(BMW CAN OK) OR (Elcon CAN OK) OR (Brusa CAN OK)`
- Lit : `BMW CAN OK`, `Brusa CAN OK`, `Elcon CAN OK`
- Utilisé par : `Charger State Feed-back`, `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Canbus`
- Ligne export : 25701 · id 130842

#### Charger State Feed-back  `SMC`
> Current state of the charger
- Propriétés : Default state name=OFF
- Fonction *ERROR* :
  - **Activating** = `Charger ERROR`
- Fonction *READY* :
  - **Activating** = `Charger CAN BUS OK`
  - **Blocking** = `(Charger CONNECT to 220V) OR (Charger CHARGING)`
- Fonction *CONNECTED* :
  - **Activating** = `Charger CONNECT to 220V`
  - **Blocking** = `Charger CHARGING`
- Fonction *CHARGING* :
  - **Activating** = `Charger CHARGING`
- Lit : `Charger CAN BUS OK`, `Charger CHARGING`, `Charger CONNECT to 220V`, `Charger ERROR`
- Utilisé par : `Charger Running`, `Charger STATE`, `E.Charging State Machine`, `SOC Scroller d3`, `VIEW BAT Ready d3`, `VIEW BAT Run d3`
- Ligne export : 25758 · id 130852

#### Ask Charging CMD  `FGI`
- Propriétés : Input type=Digital · Input=Battery OK Charger · Default state name=Default state
- Lit : `Battery OK Charger`
- Utilisé par : `E.Charging State Machine`
- Ligne export : 25912 · id 130875

#### E.Charging State Machine  `FSM`
- Propriétés : Store value=No · Resetting channel=Charger Reset State
- État 0 **OFF**
  - transition *Charger Ready & Connected* — CAN Frame, No Error, AC Power Supply (état cible non exporté par IQANdesign)
    - **Activating** = `Charger State Feed-back > 2`
- État 1 **Charger Ready** — Charger is dialing and is connected to AC supply.
  - transition *Charge CMD* (état cible non exporté par IQANdesign)
    - **Activating** = `Ask Charging CMD`
  - transition *Unplug* (état cible non exporté par IQANdesign)
    - **Activating** = `Charger State Feed-back < 2`
- État 2 **Charging** — Send Charging Order
  - transition *Unplug* (état cible non exporté par IQANdesign)
    - **Activating** = `Charger State Feed-back < 2`
  - transition *Stop Charge* (état cible non exporté par IQANdesign)
    - **Activating** = `not(Ask Charging CMD)`
  - transition *Charger End Of Charge* — From Charger point of view charge is finished (état cible non exporté par IQANdesign)
    - **Activating** = `(Charger end of charge) AND (not(Charger end of charge but balancing))`
- État 3 **Finish Charge**
  - transition *Turn Off Delay* (état cible non exporté par IQANdesign)
    - **Activating** = `Turn Off After Charge Delay`
- Lit : `Ask Charging CMD`, `Charger Reset State`, `Charger State Feed-back`, `Charger end of charge`, `Charger end of charge but balancing`, `Turn Off After Charge Delay`
- Utilisé par : `Charger CMD`, `Charger Charging IDC`, `Charger Connected`, `Charger Connected`, `Charger End Charge`, `Charger End Charge`, `Charger REQ`, `Charger State Finite out mc`, `Charger asks End Of Charge`, `Turn Off After Charge Delay`, `eCharger Charging IDC`
- Ligne export : 25923 · id 130876

#### ec Max Full Charge Voltage  `IP`
- Propriétés : Unit=V · Mode selector=eb Battery Brand · Default mode: BMW={390} · Mode 1: NovumTech={385} · Mode 2: Tyva={390} · Mode 3: Kreisel={390}
- Lit : `eb Battery Brand`
- Utilisé par : `Charger UMax`, `Charger end of charge`, `Charger end of charge but balancing`, `HT Battery NEED TO CHARGE`, `Max DC Current`, `Single adjust item: Max Full Charge Voltage`
- Ligne export : 26181 · id 130924

#### ec AC Max Current Line  `IP`
- Propriétés : Unit=A · Mode selector=balancing state · Default mode: Charging={10} · Mode 1: Balancing={0}
- Lit : `balancing state`
- Utilisé par : `Max DC Current`, `Max DC Power`, `Single adjust item: AC Max Current Line`
- Ligne export : 26199 · id 130925

#### ec AC Voltage Range  `SP`
- Propriétés : Input channel=None · Default state name=230 V · States={110 V}
- Utilisé par : `AC Voltage Value`, `Single adjust item: AC Voltage Range`
- Ligne export : 26213 · id 130926

#### AC Voltage Value  `IP`
- Propriétés : Unit=V · Mode selector=ec AC Voltage Range · Default mode: 230 V={230} · Mode 1: 110 V={110}
- Lit : `ec AC Voltage Range`
- Utilisé par : `Max DC Current`, `Max DC Power`, `Adjust group: Setup Charger`, `Single adjust item: AC Voltage Value`
- Ligne export : 26225 · id 130928

#### Max DC Current  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result := MinOf(AC Voltage Value  * ec AC Max Current Line / ec Max Full Charge Voltage, 10)
  ```
- Lit : `AC Voltage Value`, `ec AC Max Current Line`, `ec Max Full Charge Voltage`
- Utilisé par : `Charger I Target`, `Charger IMax`
- Ligne export : 26239 · id 130929

#### Charger CMD  `IDC`
> Trigger for charging. Charge if True, stop Charge if False
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `E.Charging State Machine = 2`
- Lit : `E.Charging State Machine`
- Utilisé par : `Charger CMD`, `Charger CMD`, `Charger CMD`
- Ligne export : 26257 · id 130941

#### Charger UMax  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `ec Max Full Charge Voltage [V]`
- Lit : `ec Max Full Charge Voltage`
- Utilisé par : `Charger UMax`, `Charger UMax`, `Charger UMax`
- Ligne export : 26302 · id 130949

#### Charger IMax  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Max DC Current [A]`
- Lit : `Max DC Current`
- Utilisé par : `Charger IMax`, `Charger IMax`, `Charger IMax`
- Ligne export : 26344 · id 130957

#### Charger Output Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=ec Charger Brand
- Fonction *BMW* :
  - **Controlling** = `BMW - Output current [A]`
- Fonction *Brusa* :
  - **Controlling** = `1553 - Actual mains current [A]`
- Fonction *Elcon* :
  - **Controlling** = `Elcon - output current`
- Lit : `1553 - Actual mains current`, `BMW - Output current`, `Elcon - output current`, `ec Charger Brand`
- Utilisé par : `Charger end of charge`, `Charger end of charge but balancing`, `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 27121 · id 131070

#### Is_Charger_BMW  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `ec Charger Brand = 0`
- Lit : `ec Charger Brand`
- Utilisé par : `Active le groupe: mc.Electric / E.CHARGER / E.Charger_BMW`, `Measure group: Charger BMW`
- Ligne export : 27225 · id 131098

#### Is_Charger_Brusa  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `ec Charger Brand = 1`
- Lit : `ec Charger Brand`
- Utilisé par : `Active le groupe: mc.Electric / E.CHARGER / E.Charger_Brusa`, `Measure group: Charger Brusa`
- Ligne export : 28129 · id 131235

#### Charger asks End Of Charge  `IDC`
> 3 minutes with low current and requirred voltage
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  - **Activating** = `E.Charging State Machine = 3`
- Lit : `E.Charging State Machine`
- Utilisé par : `Battery CHARGED`
- Ligne export : 29479 · id 131440

#### Max DC Power  `MAC`
> Max DC Power based on Max AC Power with 0.9 efficiency
- Propriétés : Unit=kW
- Logique :
  ```qcode
  Result := MinOf(0.9 * AC Voltage Value * ec AC Max Current Line / 1000, 3)
  ```
- Lit : `AC Voltage Value`, `ec AC Max Current Line`
- Utilisé par : `Charger kWMax`
- Ligne export : 29524 · id 131456

#### Charger kWMax  `MAC`
- Propriétés : Unit=kW · Limiting object group=Signed
- Logique :
  - **Controlling** = `Max DC Power [kW]`
- Lit : `Max DC Power`
- Utilisé par : *(personne)*
- Ligne export : 29542 · id 131469

#### Charger I Target  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Max DC Current [A]`
- Lit : `Max DC Current`
- Utilisé par : *(personne)*
- Ligne export : 29584 · id 131619

#### ec Debug: Trig Charger Ready  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Charger REQ`, `Single adjust item: Debug: Trig Charger Ready`
- Ligne export : 29626 · id 131634

#### Charger REQ  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(E.Charging State Machine = 1) OR (E.Charging State Machine = 2) OR (E.Charging State Machine = 3) OR (ec Debug: Trig Charger Ready)`
  - **Blocking** = `Charger ERROR`
- Lit : `Charger ERROR`, `E.Charging State Machine`, `ec Debug: Trig Charger Ready`
- Utilisé par : `Charger CMD`
- Ligne export : 29639 · id 131635

#### Charger Running  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Charger State Feed-back = 4`
- Lit : `Charger State Feed-back`
- Utilisé par : `Charger Running`
- Ligne export : 29716 · id 131647

#### Charger Output Voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed · Function selector=ec Charger Brand
- Fonction *BMW* :
  - **Controlling** = `BMW - Output Voltage [V]`
- Fonction *Brusa* :
  - **Controlling** = `1553 - Actual battery output voltage [V]`
- Fonction *Elcon* :
  - **Controlling** = `Elcon - output Voltage`
- Lit : `1553 - Actual battery output voltage`, `BMW - Output Voltage`, `Elcon - output Voltage`, `ec Charger Brand`
- Utilisé par : `Charger end of charge`, `Charger end of charge but balancing`
- Ligne export : 29761 · id 131655

#### Charger end of charge  `IDC`
> 1 minutes with low current and requirred voltage
- Propriétés : Toggle=No · Delay on=60000 · Delay off=0
- Logique :
  - **Activating** = `(((Abs(Charger Output Current [A])) <= 1) and ((ec Max Full Charge Voltage [V] - Charger Output Voltage [V]) < 1)) OR (ec Debug: Trig Battery Charged)`
- Lit : `Charger Output Current`, `Charger Output Voltage`, `ec Debug: Trig Battery Charged`, `ec Max Full Charge Voltage`
- Utilisé par : `E.Charging State Machine`
- Ligne export : 29865 · id 131683

#### Turn Off After Charge Delay  `IDC`
> Wait at the end of charge before turn Off the Charger
- Propriétés : Toggle=No · Delay on=3000 · Delay off=0
- Logique :
  - **Activating** = `E.Charging State Machine = 3`
- Lit : `E.Charging State Machine`
- Utilisé par : `E.Charging State Machine`
- Ligne export : 29952 · id 131696

#### ec Debug: Trig Battery Charged  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Charger end of charge`, `Single adjust item: Debug: Trig Battery Charged`
- Ligne export : 29997 · id 131704

#### Charger end of charge but balancing  `IDC`
> 1 minutes with low current and requirred voltage
- Propriétés : Toggle=No · Delay on=5000 · Delay off=5000
- Logique :
  - **Activating** = `(((Abs(Charger Output Current [A])) <= 1) and ((ec Max Full Charge Voltage [V] - Charger Output Voltage [V]) < 1)) and Novum BalancingRunning`
- Lit : `Charger Output Current`, `Charger Output Voltage`, `Novum BalancingRunning`, `ec Max Full Charge Voltage`
- Utilisé par : `Charger end of charge but balancing calc`, `E.Charging State Machine`, `K6 DCDC Ignition`, `KTC K12 IDC - AUX 3`, `not balancing`
- Ligne export : 30010 · id 235496

#### balancing state  `SP`
- Propriétés : Input channel=Charger end of charge but balancing calc · Default state name=Charging · States={Balancing}
- Lit : `Charger end of charge but balancing calc`
- Utilisé par : `ec AC Max Current Line`
- Ligne export : 30099 · id 235515

#### Charger end of charge but balancing calc  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Charger end of charge but balancing`
- Lit : `Charger end of charge but balancing`
- Utilisé par : `balancing state`
- Ligne export : 30111 · id 235517

#### not balancing  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Charger end of charge but balancing)`
- Lit : `Charger end of charge but balancing`
- Utilisé par : `Single adjust item: AC Max Current Line`
- Ligne export : 30153 · id 235530

## mc.Electric / E.CHARGER / E.Charger_BMW — actif seulement si `Is_Charger_BMW`

#### CHARGER_STATUS  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Digital
- Utilisé par : `BMW - Status`, `GFIN-A:Generic`
- Ligne export : 27295 · id 131108

#### CHARGER_MAINS_CURRENT  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - Main current`, `GFIN-A:Generic`
- Ligne export : 27306 · id 131109

#### CHARGER_DC_CURRENT  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - Output current`, `GFIN-A:Generic`
- Ligne export : 27319 · id 131110

#### CHARGER_DC_VOLTAGE  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `BMW - Output Voltage`, `GFIN-A:Generic`
- Ligne export : 27332 · id 131111

#### CHARGER_MAINS_FREQUENCY  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `BMW - Frequency`, `GFIN-A:Generic`
- Ligne export : 27345 · id 131112

#### BMW - Main current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_MAINS_CURRENT / 10`
- Lit : `CHARGER_MAINS_CURRENT`
- Utilisé par : `BMW Charging`, `Measure group: Charger BMW`
- Ligne export : 27357 · id 131113

#### BMW - Output current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_DC_CURRENT / 10`
- Lit : `CHARGER_DC_CURRENT`
- Utilisé par : `Charger Output Current`, `Measure group: Charger BMW`
- Ligne export : 27401 · id 131121

#### BMW - Output Voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_DC_VOLTAGE / 10`
- Lit : `CHARGER_DC_VOLTAGE`
- Utilisé par : `Charger Output Voltage`, `Measure group: Charger BMW`
- Ligne export : 27445 · id 131129

#### BMW - Frequency  `MAC`
- Propriétés : Unit=Hz · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_MAINS_FREQUENCY`
- Lit : `CHARGER_MAINS_FREQUENCY`
- Utilisé par : `Measure group: Charger BMW`
- Ligne export : 27489 · id 131137

#### BMW Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `GFIN-A:Generic`
- Lit : `GFIN-A:Generic`
- Utilisé par : `BMW CAN OK`, `BMW Connected`, `Charger READY`, `Measure group: Charger BMW`
- Ligne export : 27531 · id 131145

#### BMW Connected  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `BMW Ready`
- Lit : `BMW Ready`
- Utilisé par : `Charger CONNECT to 220V`
- Ligne export : 27574 · id 131153

#### BMW Charging  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `BMW - Main current [A] > 0,5`
- Lit : `BMW - Main current`
- Utilisé par : `Charger CHARGING`
- Ligne export : 27617 · id 131161

#### BMW CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `BMW Ready`
- Lit : `BMW Ready`
- Utilisé par : `Battery CAN OK`, `Battery CAN OK delay`, `Battery STANDBY`, `Charger CAN BUS OK`, `Measure group: Battery BMW`
- Ligne export : 27662 · id 131169

#### BMW - Status  `MAC`
- Propriétés : Unit=State · Limiting object group=Signed
- Logique :
  - **Controlling** = `CHARGER_STATUS`
- Lit : `CHARGER_STATUS`
- Utilisé par : `BMW Error`, `Measure group: Charger BMW`
- Ligne export : 27705 · id 131177

#### BMW Error  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `3 <= BMW - Status [State]`
- Lit : `BMW - Status`
- Utilisé par : `Charger ERROR`
- Ligne export : 27747 · id 131185

#### CMD  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Charger CMD`
- Lit : `Charger CMD`
- Utilisé par : `ENABLE`
- Ligne export : 27792 · id 131193

#### ENABLE  `GPOUT`
- Propriétés : Input value=CMD · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `CMD`
- Utilisé par : `GFOUT-A:Generic`, `Power`
- Ligne export : 27835 · id 131201

#### Power  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(ENABLE * 100) * 10`
- Lit : `ENABLE`
- Utilisé par : `POWER_REFERENCE`, `Adjust group: Master Features`
- Ligne export : 27846 · id 131202

#### POWER_REFERENCE  `GPOUT`
- Propriétés : Input value=Power · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Power`
- Utilisé par : `GFOUT-A:Generic`
- Ligne export : 27906 · id 131212

#### Math Voltage  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Charger UMax [V] * 10`
- Lit : `Charger UMax`
- Utilisé par : `MAXDCVOLTLIMIT`
- Ligne export : 27918 · id 131213

#### MAXDCVOLTLIMIT  `GPOUT`
- Propriétés : Input value=Math Voltage · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Math Voltage`
- Utilisé par : `GFOUT-A:Generic`
- Ligne export : 27962 · id 131221

#### Math Current  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Charger IMax [A] * 10`
- Lit : `Charger IMax`
- Utilisé par : `MAXDCCURRLIMIT`
- Ligne export : 27974 · id 131222

#### MAXDCCURRLIMIT  `GPOUT`
- Propriétés : Input value=Math Current · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Math Current`
- Utilisé par : `GFOUT-A:Generic`
- Ligne export : 28018 · id 131230

#### Charger CMD  `FGI`
- Propriétés : Input type=Digital · Input=Charger CMD · Default state name=Default state
- Lit : `Charger CMD`
- Utilisé par : `CMD`
- Ligne export : 28030 · id 131232

#### Charger UMax  `FGI`
- Propriétés : Unit=V · Input type=Real · Input=Charger UMax [V] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Charger UMax`
- Utilisé par : `Math Voltage`
- Ligne export : 28041 · id 131233

#### Charger IMax  `FGI`
- Propriétés : Unit=A · Input type=Real · Input=Charger IMax [A] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Charger IMax`
- Utilisé par : `Math Current`
- Ligne export : 28055 · id 131234

#### GFIN-A:Generic  `GFIN`
- Propriétés : Identifier=0x405 · Data length=Dont care · Timeout=200 · Paged protocol={Not used} · Parameters={{CHARGER_STATUS; 0}; {CHARGER_MAINS_CURRENT; 8}; {CHARGER_DC_CURRENT; 24}; {CHARGER_DC_VOLTAGE; 40}; {CHARGER_MAINS_FREQUENCY; 56}} · Module=Charger BMW (Generic) · Module index=0
- Lit : `CHARGER_DC_CURRENT`, `CHARGER_DC_VOLTAGE`, `CHARGER_MAINS_CURRENT`, `CHARGER_MAINS_FREQUENCY`, `CHARGER_STATUS`
- Utilisé par : `BMW Ready`
- Ligne export : 28069 · id 217249

#### GFOUT-A:Generic  `GFOUT`
- Propriétés : Identifier=0x400 · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Parameters={{ENABLE; 0}; {POWER_REFERENCE; 8}; {MAXDCVOLTLIMIT; 24}; {MAXDCCURRLIMIT; 40}} · Module=Charger BMW (Generic) · Module index=0
- Lit : `ENABLE`, `MAXDCCURRLIMIT`, `MAXDCVOLTLIMIT`, `POWER_REFERENCE`
- Utilisé par : *(personne)*
- Ligne export : 28100 · id 217423

## mc.Electric / E.CHARGER / E.Charger_Brusa — actif seulement si `Is_Charger_Brusa`

#### 1552 - CAN IN  `GFIN`
- Propriétés : Identifier=1552 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{1552 - Hardware enable - Byte; 7}; {1552 - Error detect - Byte; 6}; {1552 - Warning Condition - Byte; 5}; {1552 - Automatique charging - Byte; 24}} · Module=Charger Brusa (Generic) · Module index=0
- Lit : `1552 - Automatique charging - Byte`, `1552 - Error detect - Byte`, `1552 - Hardware enable - Byte`, `1552 - Warning Condition - Byte`
- Utilisé par : `Brusa CAN OK`
- Ligne export : 28200 · id 131244

#### 1553 - CAN IN  `GFIN`
- Propriétés : Identifier=1553 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{1553 - Actual mains current - Byte; 0}; {1553 - Actual mains voltage - Byte; 16}; {1553 - Actual battery output voltage - Byte; 32}; {1553 - output current to the battery - Byte; 48}} · Module=Charger Brusa (Generic) · Module index=1
- Lit : `1553 - Actual battery output voltage - Byte`, `1553 - Actual mains current - Byte`, `1553 - Actual mains voltage - Byte`, `1553 - output current to the battery - Byte`
- Utilisé par : *(personne)*
- Ligne export : 28228 · id 131245

#### 1553 - Actual mains current - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1553 - Actual mains current`, `1553 - CAN IN`
- Ligne export : 28256 · id 131246

#### 1553 - Actual mains voltage - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1553 - Actual mains voltage`, `1553 - CAN IN`
- Ligne export : 28269 · id 131247

#### 1555 - CAN IN  `GFIN`
- Propriétés : Identifier=1555 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{1555 - Power stage temperature - Byte; 0}} · Module=Charger Brusa (Generic) · Module index=2
- Lit : `1555 - Power stage temperature - Byte`
- Utilisé par : *(personne)*
- Ligne export : 28282 · id 131248

#### 1555 - Power stage temperature - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1555 - CAN IN`, `1555 - Power stage temperature - Byte`, `Measure group: Charger Brusa`
- Ligne export : 28301 · id 131249

#### 1553 - output current to the battery - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1553 - CAN IN`, `1553 - output current to the battery`
- Ligne export : 28314 · id 131250

#### 1553 - output current to the battery  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `1553 - output current to the battery - Byte / 100`
- Lit : `1553 - output current to the battery - Byte`
- Utilisé par : `Brusa Charging`, `Measure group: Charger Brusa`
- Ligne export : 28327 · id 131251

#### 1553 - Actual battery output voltage - Byte  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `1553 - Actual battery output voltage`, `1553 - CAN IN`
- Ligne export : 28371 · id 131259

#### 1553 - Actual battery output voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `1553 - Actual battery output voltage - Byte / 10`
- Lit : `1553 - Actual battery output voltage - Byte`
- Utilisé par : `Charger Output Voltage`, `Measure group: Charger Brusa`
- Ligne export : 28384 · id 131260

#### 1552 - Error detect - Byte  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `1552 - CAN IN`, `Brusa Error`, `Measure group: Charger Brusa`
- Ligne export : 28428 · id 131268

#### 1552 - Hardware enable - Byte  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `1552 - CAN IN`, `1552 - Hardware enable - IDC`
- Ligne export : 28439 · id 131269

#### Timer charging  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `(Charger CMD) OR (Timer charging [s] < 4)`
  - **Resetting** = `NegativeFlank(Charger CMD)`
- Lit : `Charger CMD`
- Utilisé par : `Charge start state`
- Ligne export : 28450 · id 131270

#### Charge start state  `SMC`
- Propriétés : Default state name=STOP
- Fonction *Clear ERROR* :
  - **Activating** = `Inside(Timer charging [s], 1, 2)`
- Fonction *Charging* :
  - **Activating** = `(Timer charging [s] > 2,1) AND (Charger CMD)`
- Lit : `Charger CMD`, `Timer charging`
- Utilisé par : `1560 - Desired Current`, `1560 - Desired Voltage`, `1560 - Max Current from 230 V`, `Error clear brusa`, `Power`
- Ligne export : 28519 · id 131282

#### 1560 - Max Current from 230 V  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Charge start state
- Fonction *STOP* : (vide)
- Fonction *Clear ERROR* : (vide)
- Fonction *Charging* :
  - **Controlling** = `Charger IMax [A] * 10`
- Lit : `Charge start state`, `Charger IMax`
- Utilisé par : `1560 - Max Current from 230 V - Byte`
- Ligne export : 28602 · id 131294

#### 1560 - Max Current from 230 V - Byte  `GPOUT`
- Propriétés : Input value=1560 - Max Current from 230 V · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `1560 - Max Current from 230 V`
- Utilisé par : `1560 - Cmd`
- Ligne export : 28694 · id 131314

#### 1560 - Desired Voltage  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Charge start state
- Fonction *STOP* : (vide)
- Fonction *Clear ERROR* : (vide)
- Fonction *Charging* :
  - **Controlling** = `Charger UMax [V] * 10`
- Lit : `Charge start state`, `Charger UMax`
- Utilisé par : `1560 - Desired Voltage - Byte`
- Ligne export : 28706 · id 131315

#### 1560 - Desired Voltage - Byte  `GPOUT`
- Propriétés : Input value=1560 - Desired Voltage · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `1560 - Desired Voltage`
- Utilisé par : `1560 - Cmd`
- Ligne export : 28798 · id 131335

#### 1560 - Desired Current  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Charge start state
- Fonction *STOP* : (vide)
- Fonction *Clear ERROR* : (vide)
- Fonction *Charging* :
  - **Controlling** = `Charger I Targret [A] * 10`
- Lit : `Charge start state`, `Charger I Targret`
- Utilisé par : `1560 - Desired Current - Byte`
- Ligne export : 28810 · id 131336

#### 1560 - Desired Current - Byte  `GPOUT`
- Propriétés : Input value=1560 - Desired Current · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `1560 - Desired Current`
- Utilisé par : `1560 - Cmd`
- Ligne export : 28902 · id 131356

#### Power  `DP`
- Propriétés : Mode selector=Charge start state · Default mode: STOP={False} · Mode 1: Clear ERROR={False} · Mode 2: Charging={True}
- Lit : `Charge start state`
- Utilisé par : `1560 - POWER ON - Byte`, `Adjust group: Master Features`
- Ligne export : 28914 · id 131357

#### 1560 - POWER ON - Byte  `JPOUT`
- Propriétés : Input value=Power · Length=1 bit · Resolution=1 · Offset=0
- Lit : `Power`
- Utilisé par : `1560 - Cmd`
- Ligne export : 28931 · id 131358

#### Error clear brusa  `DP`
- Propriétés : Mode selector=Charge start state · Default mode: STOP={False} · Mode 1: Clear ERROR={True} · Mode 2: Charging={False}
- Lit : `Charge start state`
- Utilisé par : `1560 - Cycle Value - Byte`, `Single adjust item: Error clear brusa`
- Ligne export : 28943 · id 131359

#### 1560 - Cycle Value - Byte  `JPOUT`
- Propriétés : Input value=Error clear brusa · Length=1 bit · Resolution=1 · Offset=0
- Lit : `Error clear brusa`
- Utilisé par : `1560 - Cmd`
- Ligne export : 28960 · id 131360

#### 1560 - Cmd  `GFOUT`
- Propriétés : Identifier=1560 · Data length=7 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={{1560 - POWER ON - Byte [bits]; 7}; {1560 - Cycle Value - Byte [bits]; 6}; {1560 - Max Current from 230 V - Byte; 8}; {1560 - Desired Voltage - Byte; 24}; {1560 - Desired Current - Byte; 40}} · Module=Charger Brusa (Generic) · Module index=0
- Lit : `1560 - Cycle Value - Byte`, `1560 - Desired Current - Byte`, `1560 - Desired Voltage - Byte`, `1560 - Max Current from 230 V - Byte`, `1560 - POWER ON - Byte`
- Utilisé par : *(personne)*
- Ligne export : 28972 · id 131361

#### 1552 - Warning Condition - Byte  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `1552 - CAN IN`, `Measure group: Charger Brusa`
- Ligne export : 29003 · id 131362

#### 1552 - Automatique charging - Byte  `GPIN`
- Propriétés : Length=1 bit · Type=Digital
- Utilisé par : `1552 - CAN IN`, `Measure group: Charger Brusa`
- Ligne export : 29014 · id 131363

#### 1553 - Actual mains current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `1553 - Actual mains current - Byte / 100`
- Lit : `1553 - Actual mains current - Byte`
- Utilisé par : `Charger Output Current`, `Measure group: Charger Brusa`
- Ligne export : 29025 · id 131364

#### 1553 - Actual mains voltage  `MAC`
- Propriétés : Unit=V AC · Limiting object group=Signed
- Logique :
  - **Controlling** = `1553 - Actual mains voltage - Byte / 10`
- Lit : `1553 - Actual mains voltage - Byte`
- Utilisé par : `Brusa Connected`, `Measure group: Charger Brusa`
- Ligne export : 29069 · id 131372

#### 1555 - Power stage temperature - Byte  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `1555 - Power stage temperature - Byte / 10`
- Lit : `1555 - Power stage temperature - Byte`
- Utilisé par : `1555 - CAN IN`, `Measure group: Charger Brusa`
- Ligne export : 29113 · id 131380

#### 1552 - Hardware enable - IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `1552 - Hardware enable - Byte`
- Lit : `1552 - Hardware enable - Byte`
- Utilisé par : `Brusa ready`
- Ligne export : 29157 · id 131388

#### Brusa Connected  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `1553 - Actual mains voltage [V AC] >= 90`
- Lit : `1553 - Actual mains voltage`
- Utilisé par : `Charger CONNECT to 220V`
- Ligne export : 29200 · id 131396

#### Brusa Charging  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `1553 - output current to the battery [A] > 0,5`
- Lit : `1553 - output current to the battery`
- Utilisé par : `Charger CHARGING`
- Ligne export : 29245 · id 131404

#### Brusa CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `1552 - CAN IN`
- Lit : `1552 - CAN IN`
- Utilisé par : `Charger CAN BUS OK`
- Ligne export : 29290 · id 131412

#### Brusa Error  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `1552 - Error detect - Byte`
- Lit : `1552 - Error detect - Byte`
- Utilisé par : `Charger ERROR`
- Ligne export : 29333 · id 131420

#### Brusa ready  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `1552 - Hardware enable - IDC`
- Lit : `1552 - Hardware enable - IDC`
- Utilisé par : `Charger READY`
- Ligne export : 29376 · id 131428

#### Charger CMD  `FGI`
- Propriétés : Input type=Digital · Input=Charger CMD · Default state name=Default state
- Lit : `Charger CMD`
- Utilisé par : `Charge start state`, `Timer charging`
- Ligne export : 29419 · id 131436

#### Charger UMax  `FGI`
- Propriétés : Unit=V · Input type=Real · Input=Charger UMax [V] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Charger UMax`
- Utilisé par : `1560 - Desired Voltage`
- Ligne export : 29430 · id 131437

#### Charger IMax  `FGI`
- Propriétés : Unit=A · Input type=Real · Input=Charger IMax [A] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Charger IMax`
- Utilisé par : `1560 - Max Current from 230 V`, `Charger I Targret`
- Ligne export : 29444 · id 131438

#### Charger I Targret  `FGI`
- Propriétés : Unit=A · Input type=Real · Input=Charger IMax [A] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Charger IMax`
- Utilisé par : `1560 - Desired Current`
- Ligne export : 29458 · id 131439

## mc.Electric / E.CHARGER / E.Charger_Elcon — actif seulement si `Is_Charger_Elcon`

#### ELCON-IN  `GFIN`
- Propriétés : Identifier=0x18FF50E5 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Output Voltage; 0}; {Output Current; 16}; {Hardware Failure; 32}; {Temperature od charger; 33}; {Input Voltage; 34}; {Stating State; 35}; {Communication State; 36}} · Module=Charger Elcon (Generic) · Module index=0
- Lit : `Communication State`, `Hardware Failure`, `Input Voltage`, `Output Current`, `Output Voltage`, `Stating State`, `Temperature od charger`
- Utilisé par : `Elcon Ready`
- Ligne export : 26411 · id 130966

#### Input Voltage  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Measure group: Charger Elcon`
- Ligne export : 26448 · id 130967

#### Hardware Failure  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Elcon Error`
- Ligne export : 26460 · id 130968

#### Elcon Error  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `Hardware Failure`
- Lit : `Hardware Failure`
- Utilisé par : `Charger ERROR`, `Elcon Ready`, `Measure group: Charger Elcon`
- Ligne export : 26472 · id 130969

#### Elcon Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `ELCON-IN`
  - **Blocking** = `Elcon Error`
- Lit : `ELCON-IN`, `Elcon Error`
- Utilisé par : `Charger READY`, `Elcon CAN OK`, `Elcon Connected`, `Measure group: Charger Elcon`
- Ligne export : 26515 · id 130977

#### Elcon Connected  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `Elcon Ready`
- Lit : `Elcon Ready`
- Utilisé par : `Charger CONNECT to 220V`, `Measure group: Charger Elcon`
- Ligne export : 26565 · id 130986

#### Output Current  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `ELCON-IN`, `Elcon - output current`
- Ligne export : 26608 · id 130994

#### Elcon - output current  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Output Current / 10`
- Lit : `Output Current`
- Utilisé par : `Charger Output Current`, `Elcon Charging`, `Measure group: Charger Elcon`
- Ligne export : 26621 · id 130995

#### Output Voltage  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `ELCON-IN`, `Elcon - output Voltage`
- Ligne export : 26665 · id 131003

#### Math Voltage  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Charger UMax [V] * 10`
- Lit : `Charger UMax`
- Utilisé par : `Max Voltage`
- Ligne export : 26678 · id 131004

#### Max Voltage  `GPOUT`
- Propriétés : Input value=Math Voltage · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `Math Voltage`
- Utilisé par : `ELCON-OUT`
- Ligne export : 26722 · id 131012

#### Math Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Charger IMax [A] * 10`
- Lit : `Charger IMax`
- Utilisé par : `Max Curent`
- Ligne export : 26734 · id 131013

#### Max Curent  `GPOUT`
- Propriétés : Input value=Math Current [A] · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Big-endian
- Lit : `Math Current`
- Utilisé par : `ELCON-OUT`
- Ligne export : 26778 · id 131021

#### CMD  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Charger CMD)`
- Lit : `Charger CMD`
- Utilisé par : `Char`
- Ligne export : 26790 · id 131022

#### Char  `GPOUT`
- Propriétés : Input value=CMD · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `CMD`
- Utilisé par : `ELCON-OUT`
- Ligne export : 26834 · id 131030

#### ELCON-OUT  `GFOUT`
- Propriétés : Identifier=0x1806E5F4 · Data length=8 · Send method=Continuously · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{Max Voltage; 0}; {Max Curent [A]; 16}; {Char; 32}} · Module=Charger Elcon (Generic) · Module index=0
- Lit : `Char`, `Max Curent`, `Max Voltage`
- Utilisé par : *(personne)*
- Ligne export : 26845 · id 131031

#### Temperature od charger  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Temperature od charger`, `Measure group: Charger Elcon`
- Ligne export : 26870 · id 131032

#### Stating State  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Measure group: Charger Elcon`
- Ligne export : 26882 · id 131033

#### Communication State  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `ELCON-IN`, `Measure group: Charger Elcon`
- Ligne export : 26894 · id 131034

#### Temperature od charger  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Temperature od charger`
- Lit : `Temperature od charger`
- Utilisé par : `ELCON-IN`, `Measure group: Charger Elcon`
- Ligne export : 26906 · id 131035

#### Elcon - output Voltage  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Output Voltage / 10`
- Lit : `Output Voltage`
- Utilisé par : `Charger Output Voltage`, `Measure group: Charger Elcon`
- Ligne export : 26949 · id 131043

#### Elcon Charging  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `Elcon - output current > 0,25`
- Lit : `Elcon - output current`
- Utilisé par : `Charger CHARGING`, `Measure group: Charger Elcon`
- Ligne export : 26993 · id 131051

#### Elcon CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `Elcon Ready`
- Lit : `Elcon Ready`
- Utilisé par : `Charger CAN BUS OK`, `Measure group: Charger Elcon`
- Ligne export : 27038 · id 131059

#### Charger CMD  `FGI`
- Propriétés : Input type=Digital · Input=Charger CMD · Default state name=Default state
- Lit : `Charger CMD`
- Utilisé par : `CMD`
- Ligne export : 27081 · id 131067

#### Charger UMax  `FGI`
- Propriétés : Unit=V · Input type=Real · Input=Charger UMax [V] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Charger UMax`
- Utilisé par : `Math Voltage`
- Ligne export : 27092 · id 131068

#### Charger IMax  `FGI`
- Propriétés : Unit=A · Input type=Real · Input=Charger IMax [A] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Charger IMax`
- Utilisé par : `Math Current`
- Ligne export : 27106 · id 131069

## mc.Electric / E.KeyBox x100 E — actif seulement si `Is_Electric_x100 mc`

#### 0x70C  `GFIN`
- Propriétés : Identifier=0x70C · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={} · Module=Keybox X100 E (Generic) · Module index=1
- Utilisé par : *(personne)*
- Ligne export : 49434 · id 165844

#### Byte 0  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`
- Ligne export : 49450 · id 165845

#### Byte 1  `GPOUT`
- Propriétés : Input value=0x0C · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`
- Ligne export : 49461 · id 165846

#### GFOUT-D:Generic  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=Keybox X100 E (Generic) · Module index=2
- Lit : `Byte 0`, `Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 49472 · id 165847

#### KeyBox E Can Ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `0x70C`
- Utilisé par : `e CanBus Error mc`, `MD4-5 page: INFO`, `Measure group: Canbus`
- Ligne export : 49494 · id 165848

#### e CanBus Error mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header, English=e1166 KeyBox E · Text, English=The KeyBox don't respond with the system, try a reboot to fix.
- Logique :
  - **Showing** = `not(KeyBox E Can Ok)`
  - **Hiding** = `KeyBox E Can Ok`
- Lit : `KeyBox E Can Ok`
- Utilisé par : *(personne)*
- Ligne export : 49537 · id 165856

#### K1 Fan Rear / Fan mk E  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(E rad FAN OUT) OR (E Full Fan Test)`
- Lit : `E Full Fan Test`, `E rad FAN OUT`
- Utilisé par : `ON_Bits`
- Ligne export : 49591 · id 165865

#### K2 Fan Super / Pump  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(E water PUMP VAR) OR (E Full Fan Test)`
- Lit : `E Full Fan Test`, `E water PUMP VAR`
- Utilisé par : `ON_Bits`
- Ligne export : 49641 · id 165874

#### E Force K3 Auto-off  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `K3 oldFan Exhaust / AutoOff`, `Single adjust item: Force K3 Auto-off`
- Ligne export : 49691 · id 165883

#### K3 oldFan Exhaust / AutoOff  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(ShutDown Action E mc) OR (E Force K3 Auto-off)`
- Lit : `E Force K3 Auto-off`, `ShutDown Action E mc`
- Utilisé par : `ON_Bits`
- Ligne export : 49704 · id 165884

#### Charger Connected  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `PositiveFlank(Charger CONNECT to 220V)`
- Lit : `Charger CONNECT to 220V`
- Utilisé par : `K4 Engine Power / Search Lights`
- Ligne export : 49754 · id 165893

#### K4 Engine Power / Search Lights  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Charger Connected`
- Lit : `Charger Connected`
- Utilisé par : `ON_Bits`
- Ligne export : 49798 · id 165901

#### K5 Engine Start  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `ON_Bits`
- Ligne export : 49841 · id 165909

#### K6 DCDC Ignition  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Battery OK DCDC) OR (Charger end of charge but balancing)`
- Lit : `Battery OK DCDC`, `Charger end of charge but balancing`
- Utilisé par : `Clignotement charge DCDC`, `ON_Bits`
- Ligne export : 49877 · id 165916

#### K7 Aux 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `ON_Bits`
- Ligne export : 49927 · id 165924

#### K8  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `ON_Bits`
- Ligne export : 49963 · id 165931

#### K9  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `ON_Bits`
- Ligne export : 49999 · id 165938

#### K10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `ON_Bits`
- Ligne export : 50035 · id 165945

#### K11  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `ON_Bits`
- Ligne export : 50071 · id 165952

#### K12  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `ON_Bits`
- Ligne export : 50107 · id 165959

#### K13  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `ON_Bits`
- Ligne export : 50143 · id 165966

#### ON_Bits  `IMAC`
- Logique :
  ```qcode
  Result := K1 Fan Rear / Fan mk E * 1 + K2 Fan Super / Pump  * 2 + K3 oldFan Exhaust / AutoOff * 4 + K4 Engine Power / Search Lights * 8 + K5 Engine Start * 16 + K6 DCDC Ignition * 32 + K7 Aux 2 * 64 + K8 * 128 + K9 * 256 + K10 * 512 + K11 * 1024 + K12 * 2048 + K13 * 4096
  ```
- Lit : `K1 Fan Rear / Fan mk E`, `K10`, `K11`, `K12`, `K13`, `K2 Fan Super / Pump`, `K3 oldFan Exhaust / AutoOff`, `K4 Engine Power / Search Lights`, `K5 Engine Start`, `K6 DCDC Ignition`, `K7 Aux 2`, `K8`, `K9`
- Utilisé par : `OFF_Bits`, `ON_Bits_GOUT`
- Ligne export : 50179 · id 165973

#### ON_Bits_GOUT  `GPOUT`
- Propriétés : Input value=ON_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `ON_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 50197 · id 166007

#### OFF_Bits  `IMAC`
- Logique :
  ```qcode
  Result := bnot(ON_Bits) band 0x1FFF
  ```
- Lit : `ON_Bits`
- Utilisé par : `OFF_Bits_GOUT`
- Ligne export : 50209 · id 166008

#### OFF_Bits_GOUT  `GPOUT`
- Propriétés : Input value=OFF_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `OFF_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 50227 · id 166019

#### mk E Program KeyBox x100  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Trigger HeartBeat`, `Single adjust item: Program KeyBox`
- Ligne export : 50239 · id 166020

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=0x20C · Data length=8 · Send method=On change · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{OFF_Bits_GOUT; 0}; {ON_Bits_GOUT; 16}} · Module=Keybox X100 E (Generic) · Module index=3
- Lit : `OFF_Bits_GOUT`, `ON_Bits_GOUT`
- Utilisé par : *(personne)*
- Ligne export : 50252 · id 166021

#### BYTE 0 - HB  `GPOUT`
- Propriétés : Input value=0x2B · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-A:Generic`, `GFOUT-B:Generic`
- Ligne export : 50274 · id 166022

#### BYTE 1 - HB  `GPOUT`
- Propriétés : Input value=0x17 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-A:Generic`, `GFOUT-B:Generic`
- Ligne export : 50285 · id 166023

#### BYTE 2 - HB  `GPOUT`
- Propriétés : Input value=0x10 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-A:Generic`, `GFOUT-B:Generic`
- Ligne export : 50296 · id 166024

#### BYTE 4 - HB  `GPOUT`
- Propriétés : Input value=0xF4 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-A:Generic`, `GFOUT-B:Generic`
- Ligne export : 50307 · id 166025

#### ID Prog  `IMAC`
- Logique :
  - **Controlling** = `0x0C + 0x600`
- Utilisé par : `GFOUT-A:Generic`, `GFOUT-B:Generic`
- Ligne export : 50318 · id 166026

#### BYTE 5 - HB  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-A:Generic`
- Ligne export : 50361 · id 166034

#### Trigger HeartBeat  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(mk E Program KeyBox x100)`
- Lit : `mk E Program KeyBox x100`
- Utilisé par : `GFOUT-A:Generic`, `Trigger Speed`
- Ligne export : 50372 · id 166035

#### GFOUT-A:Generic  `GFOUT`
- Propriétés : Identifier=ID Prog · Data length=8 · Send method=On trigger · Trigger=Trigger HeartBeat · Unused bits=Set to 0 · Parameters={{BYTE 0 - HB; 0}; {BYTE 1 - HB; 8}; {BYTE 2 - HB; 16}; {BYTE 4 - HB; 32}; {BYTE 5 - HB; 40}} · Module=Keybox X100 E (Generic) · Module index=0
- Lit : `BYTE 0 - HB`, `BYTE 1 - HB`, `BYTE 2 - HB`, `BYTE 4 - HB`, `BYTE 5 - HB`, `ID Prog`, `Trigger HeartBeat`
- Utilisé par : *(personne)*
- Ligne export : 50416 · id 166043

#### BYTE 0 - HB  `GPOUT`
- Propriétés : Input value=0x2F · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-A:Generic`, `GFOUT-B:Generic`
- Ligne export : 50448 · id 166044

#### BYTE 1 - HB  `GPOUT`
- Propriétés : Input value=0x10 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-A:Generic`, `GFOUT-B:Generic`
- Ligne export : 50459 · id 166045

#### BYTE 2 - HB  `GPOUT`
- Propriétés : Input value=0x20 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-A:Generic`, `GFOUT-B:Generic`
- Ligne export : 50470 · id 166046

#### BYTE 4 - HB  `GPOUT`
- Propriétés : Input value=0x02 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-A:Generic`, `GFOUT-B:Generic`
- Ligne export : 50481 · id 166047

#### Trigger Speed  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `NegativeFlank(Trigger HeartBeat)`
- Lit : `Trigger HeartBeat`
- Utilisé par : `GFOUT-B:Generic`
- Ligne export : 50492 · id 166048

#### GFOUT-B:Generic  `GFOUT`
- Propriétés : Identifier=ID Prog · Data length=8 · Send method=On trigger · Trigger=Trigger Speed · Unused bits=Set to 0 · Parameters={{BYTE 0 - HB; 0}; {BYTE 1 - HB; 8}; {BYTE 2 - HB; 16}; {BYTE 4 - HB; 32}} · Module=Keybox X100 E (Generic) · Module index=1
- Lit : `BYTE 0 - HB`, `BYTE 1 - HB`, `BYTE 2 - HB`, `BYTE 4 - HB`, `ID Prog`, `Trigger Speed`
- Utilisé par : *(personne)*
- Ligne export : 50536 · id 166056

#### ID Fault  `IMAC`
- Logique :
  - **Controlling** = `0x0C + 0x180`
- Utilisé par : `GFIN-A:Generic`
- Ligne export : 50565 · id 166057

#### GFIN-A:Generic  `GFIN`
- Propriétés : Identifier=ID Fault · Data length=Dont care · Paged protocol={Not used} · Parameters={{K1 Fault; 1}; {K2 Fault; 2}; {K3 Fault; 3}; {K4 Fault; 4}; {K5 Fault; 5}; {K6 Fault; 6}; {K7 Fault; 7}; {K8 Fault; 8}; {K9 Fault; 9}; {K10 Fault; 10}; {K11 Fault; 11}; {K12 Fault; 12}; {K13 Fault; 13}} · Module=Keybox X100 E (Generic) · Module index=0
- Lit : `ID Fault`, `K1 Fault`, `K10 Fault`, `K11 Fault`, `K12 Fault`, `K13 Fault`, `K2 Fault`, `K3 Fault`, `K4 Fault`, `K5 Fault`, `K6 Fault`, `K7 Fault`, `K8 Fault`, `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 50608 · id 166065

#### K1 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `e K1 fuse is blown mc`
- Ligne export : 50663 · id 166066

#### e K1 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=e1016 K1 fuse is blown
- Logique :
  - **Showing** = `K1 Fault`
- Lit : `K1 Fault`
- Utilisé par : *(personne)*
- Ligne export : 50675 · id 166067

#### K2 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `e K2 fuse is blown  mc`
- Ligne export : 50721 · id 166075

#### e K2 fuse is blown  mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=e1181 K2 fuse is blown
- Logique :
  - **Showing** = `K2 Fault`
- Lit : `K2 Fault`
- Utilisé par : *(personne)*
- Ligne export : 50733 · id 166076

#### K3 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `e K3 fuse is blown  mc`
- Ligne export : 50779 · id 166084

#### e K3 fuse is blown  mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=e1049 K3 fuse is blown
- Logique :
  - **Showing** = `K3 Fault`
- Lit : `K3 Fault`
- Utilisé par : *(personne)*
- Ligne export : 50791 · id 166085

#### K4 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `e K4 fuse is blown mc`
- Ligne export : 50837 · id 166093

#### e K4 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=e1149 K4 fuse is blown
- Logique :
  - **Showing** = `K4 Fault`
- Lit : `K4 Fault`
- Utilisé par : *(personne)*
- Ligne export : 50849 · id 166094

#### K5 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `e K5 fuse is blown mc`
- Ligne export : 50895 · id 166102

#### e K5 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=e1008 K5 fuse is blown
- Logique :
  - **Showing** = `K5 Fault`
- Lit : `K5 Fault`
- Utilisé par : *(personne)*
- Ligne export : 50907 · id 166103

#### K6 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `e K6 fuse is blown mc`
- Ligne export : 50953 · id 166111

#### e K6 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=e1177 K6 fuse is blown
- Logique :
  - **Showing** = `K6 Fault`
- Lit : `K6 Fault`
- Utilisé par : *(personne)*
- Ligne export : 50965 · id 166112

#### K7 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `e K7 fuse is blown mc`
- Ligne export : 51011 · id 166120

#### e K7 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=e1065 K7 fuse is blown
- Logique :
  - **Showing** = `K7 Fault`
- Lit : `K7 Fault`
- Utilisé par : *(personne)*
- Ligne export : 51023 · id 166121

#### K8 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `e K8 fuse is blown mc`
- Ligne export : 51069 · id 166129

#### e K8 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=e1174 K8 fuse is blown
- Logique :
  - **Showing** = `K8 Fault`
- Lit : `K8 Fault`
- Utilisé par : *(personne)*
- Ligne export : 51081 · id 166130

#### K9 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `e K9 fuse is blown mc`
- Ligne export : 51127 · id 166138

#### e K9 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=e1084 K9 fuse is blown
- Logique :
  - **Showing** = `K9 Fault`
- Lit : `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 51139 · id 166139

#### K10 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `e K10 fuse is blown mc`
- Ligne export : 51185 · id 166147

#### e K10 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=e1196 K10 fuse is blown
- Logique :
  - **Showing** = `K10 Fault`
- Lit : `K10 Fault`
- Utilisé par : *(personne)*
- Ligne export : 51197 · id 166148

#### K11 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `e K11 fuse is blown mc`
- Ligne export : 51243 · id 166156

#### e K11 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=e1196 K11 fuse is blown
- Logique :
  - **Showing** = `K11 Fault`
- Lit : `K11 Fault`
- Utilisé par : *(personne)*
- Ligne export : 51255 · id 166157

#### K12 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `e K12 fuse is blown mc`
- Ligne export : 51301 · id 166165

#### e K12 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=e1067 K12 fuse is blown
- Logique :
  - **Showing** = `K12 Fault`
- Lit : `K12 Fault`
- Utilisé par : *(personne)*
- Ligne export : 51313 · id 166166

#### K13 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `e K13 fuse is blown mc`
- Ligne export : 51359 · id 166174

#### e K13 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=e1200 K13 fuse is blown
- Logique :
  - **Showing** = `K13 Fault`
- Lit : `K13 Fault`
- Utilisé par : *(personne)*
- Ligne export : 51371 · id 166175

#### E Full Fan Test  `DP`
> Allows to test full fan without crancking
- Propriétés : True text=Force On · False text=Auto · Default mode={False}
- Utilisé par : `K1 Fan Rear / Fan mk E`, `K2 Fan Super / Pump`
- Ligne export : 51417 · id 166183

#### Clignotement charge DCDC  `TMR`
> utile pour faire clignoter les flèche entre 400 et 12 sur me MD4
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `K6 DCDC Ignition`
  - **Resetting** = `not(K6 DCDC Ignition)`
- Lit : `K6 DCDC Ignition`
- Utilisé par : `show fleche DCDC charging`
- Ligne export : 51430 · id 240714

#### show fleche DCDC charging  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Clignotement charge DCDC [s] mod 2) = 1`
- Lit : `Clignotement charge DCDC`
- Utilisé par : `MD4-5 page: MAIN Elec`
- Ligne export : 51490 · id 240729

## mc.Electric / E.MOTORS

#### em ZAPI Node  `SP`
- Propriétés : Input channel=None · Default state name=8-10 · States={1-4; 4-8}
- Utilisé par : `Node_ID`, `Node_ID`, `Single adjust item: ZAPI Node`
- Ligne export : 30215 · id 133779

#### em1 M-Track - Brand  `SP`
- Propriétés : Input channel=None · Default state name=Sevcon · States={Zapi}
- Utilisé par : `Is_MT_Sevcon`, `Is_MT_Zapi`, `Is_MT_Zapi 2`, `M1 - CAN OK`, `M1 - CURRENT`, `M1 - Error mode`, `M1 - Heatsink`, `M1 - KTY`, `M1 - RUN`, `M1 - Ready`, `M1 - Speed`, `M1 - Torque`, `M1 - Voltage`, `M2 - CAN OK`, `M2 - CURRENT`, `M2 - Error mode`, `M2 - Heatsink`, `M2 - KTY`, `M2 - RUN`, `M2 - Ready`, `M2 - Speed`, `M2 - Torque`, `M2 - Voltage`, `Single adjust item: M-Track - Brand`
- Ligne export : 30228 · id 131716

#### is_x100_math  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `is_x100_mc_s`
- Lit : `is_x100_mc_s`
- Utilisé par : `em M-Pump - Brand`
- Ligne export : 40172 · id 232411

#### em M-Pump - Brand  `SP`
- Propriétés : Input channel=is_x100_math · Default state name=Sevcon gen · States={Sevcon j19}
- Lit : `is_x100_math`
- Utilisé par : `Is_M3_Sevcon_gen`, `Is_M3_Sevcon_j19`, `M3 - CAN OK`, `M3 - Engine Temps`, `M3 - Error mode`, `M3 - Heatsink`, `M3 - Ready`, `M3 - Run`, `M3 - Voltage`
- Ligne export : 40214 · id 133344

#### em Engine - Force Ready  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `E Engines Ready`, `Single adjust item: Engine - Force Ready`
- Ligne export : 44059 · id 133742

#### E Engines Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  ```qcode
  Result := (E.M-Tracks.M1 - Ready and E.M-Tracks.M2 - Ready and E.M3-Hydrau.M3 - Ready) or em Engine - Force Ready
  ```
- Lit : `em Engine - Force Ready`
- Utilisé par : `Electric Engine State Feed-back`, `Engines Not Ready`, `Engines Running`, `e System Started`
- Ligne export : 44072 · id 133743

#### Electric Engine State Feed-back  `SMC`
- Propriétés : Default state name=OFF
- Fonction *STARTING* :
  - **Activating** = `VARIATOR SUPER ON E mc`
  - **Blocking** = `E Engines Ready`
- Fonction *READY* :
  - **Activating** = `(E Engines Ready) AND (VARIATOR SUPER ON E mc)`
- Lit : `E Engines Ready`, `VARIATOR SUPER ON E mc`
- Utilisé par : `Power State Int E`, `Power State Int E`, `brokenVIEW ENGINE STATE`, `brokenVIEW TRACK STATE`
- Ligne export : 44092 · id 133755

#### Engines Not Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(E Engines Ready)`
- Lit : `E Engines Ready`
- Utilisé par : *(personne)*
- Ligne export : 44177 · id 133769

#### Engines Error  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(M3 - Error mode) OR (M1 - Error mode) OR (M2 - Error mode)`
- Lit : `M1 - Error mode`, `M2 - Error mode`, `M3 - Error mode`
- Utilisé par : `brokenVIEW ENGINE STATE`, `brokenVIEW TRACK STATE`
- Ligne export : 44221 · id 133782

#### Tracks Engines Crash  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(M1 - Error mode) OR (M2 - Error mode)`
- Lit : `M1 - Error mode`, `M2 - Error mode`
- Utilisé par : `System Ask imminent Crash E mc`
- Ligne export : 44278 · id 133792

#### Is_MT_Zapi 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `em1 M-Track - Brand = 1`
- Lit : `em1 M-Track - Brand`
- Utilisé par : `Single adjust item: ZAPI Node`
- Ligne export : 44328 · id 212983

## mc.Electric / E.MOTORS / E.Cooling

#### NEED FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(M1 - NEED TO FAN) OR (M2 - NEED TO FAN) OR (M3 - NEED TO FAN)`
- Lit : `M1 - NEED TO FAN`, `M2 - NEED TO FAN`, `M3 - NEED TO FAN`
- Utilisé par : `Timer Fan`
- Ligne export : 43636 · id 133660

#### Timer Fan  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `NEED FAN`
  - **Resetting** = `(not(NEED FAN)) OR (Timer Fan [min] > 10)`
- Lit : `NEED FAN`
- Utilisé par : `E rad FAN OUT`, `Adjust group: Master Thermic Cooling`
- Ligne export : 43693 · id 133670

#### em FAN MODE  `SP`
- Propriétés : Input channel=None · Default state name=AUTO · States={OFF; FORCE ON}
- Utilisé par : `E rad FAN OUT`, `Single adjust item: Fan mode`
- Ligne export : 43762 · id 133682

#### E rad FAN OUT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em FAN MODE
- Fonction *AUTO* :
  - **Activating** = `Inside(Timer Fan [min], 0,5, 4)`
- Fonction *OFF* :
  - **Blocking** = `True`
- Fonction *FORCE ON* :
  - **Activating** = `True`
- Lit : `Timer Fan`, `em FAN MODE`
- Utilisé par : `K1 Fan Rear / Fan mk E`, `KTC K4 IDC - Water Cooling`, `Statistics log: Electronic Stats logs`
- Ligne export : 43775 · id 133685

#### NEED PUMP  `IDC`
- Propriétés : Toggle=No · Delay on=20000 · Delay off=0
- Logique :
  - **Activating** = `(M3 - NEED TO PUMP) OR (M2 - NEED TO PUMP) OR (M1 - NEED TO PUMP)`
- Lit : `M1 - NEED TO PUMP`, `M2 - NEED TO PUMP`, `M3 - NEED TO PUMP`
- Utilisé par : `E water PUMP VAR`
- Ligne export : 43883 · id 133707

#### em PUMP VAR MODE  `SP`
- Propriétés : Input channel=None · Default state name=AUTO · States={OFF; FORCE ON}
- Utilisé par : `E water PUMP VAR`, `Single adjust item: Pump var mode`
- Ligne export : 43940 · id 133717

#### E water PUMP VAR  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em PUMP VAR MODE
- Fonction *AUTO* :
  - **Activating** = `NEED PUMP`
- Fonction *OFF* :
  - **Blocking** = `True`
- Fonction *FORCE ON* :
  - **Activating** = `True`
- Lit : `NEED PUMP`, `em PUMP VAR MODE`
- Utilisé par : `K2 Fan Super / Pump`, `KTC K5 IDC - Pump Water`, `Statistics log: Electronic Stats logs`
- Ligne export : 43953 · id 133720

## mc.Electric / E.MOTORS / E.M-Tracks — actif seulement si `VARIATOR SUPER ON E mc`

#### Min Speed  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `0 - e Max Speed [%]`
- Lit : `e Max Speed`
- Utilisé par : `e Math Left`, `e Math Right`, `Adjust group: Master Thermic`
- Ligne export : 30259 · id 131719

#### e Math Right  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe((e Right Filter [%] *% Current Limiting [%]): {{-100; Min Speed [%]}; {0; 0}; {100; e Max Speed [%]}}, Freeze)`
- Lit : `Current Limiting`, `Min Speed`, `e Max Speed`, `e Right Filter`
- Utilisé par : `Filter Right`
- Ligne export : 30302 · id 131727

#### Filter Right  `SFC`
- Propriétés : Input channel=e Math Right [%] · Enable=Yes · Type=Slopes · Slopes={{e Start Slope [%/s]; e Stop Slope [%/s]}; {e Start Slope [%/s]; e Stop Slope [%/s]}}
- Lit : `e Math Right`, `e Start Slope`, `e Stop Slope`
- Utilisé par : `Speed CAN Right`, `Speed_CAN_Right`
- Ligne export : 30364 · id 131736

#### Is_MT_Zapi  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `em1 M-Track - Brand = 1`
- Lit : `em1 M-Track - Brand`
- Utilisé par : `Active le groupe: mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M1.Right.gen`, `Active le groupe: mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M2.Left.gen`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`, `Single adjust item: Reset ZAPI state`
- Ligne export : 30382 · id 131737

#### em Enable Power Zapi  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Enable`, `Enable`, `Forward`, `Forward`, `Single adjust item: Enable Power Zapi`
- Ligne export : 30427 · id 131745

#### e Math Left  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe((e Left Filter [%] *% Current Limiting [%]): {{-100; Min Speed [%]}; {0; 0}; {100; e Max Speed [%]}}, Freeze)`
- Lit : `Current Limiting`, `Min Speed`, `e Left Filter`, `e Max Speed`
- Utilisé par : `Filter Left`
- Ligne export : 32685 · id 132102

#### Filter Left  `SFC`
- Propriétés : Input channel=e Math Left [%] · Enable=Yes · Type=Slopes · Slopes={{e Start Slope [%/s]; e Stop Slope [%/s]}; {e Start Slope [%/s]; e Stop Slope [%/s]}}
- Lit : `e Math Left`, `e Start Slope`, `e Stop Slope`
- Utilisé par : `Speed CAN Left Sev`, `Speed_CAN_Left zapi`
- Ligne export : 32747 · id 132111

#### Is_MT_Sevcon  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `em1 M-Track - Brand = 0`
- Lit : `em1 M-Track - Brand`
- Utilisé par : `Active le groupe: mc.Electric / E.MOTORS / E.M-Tracks / E.Sevcon.M1.M2.gen4`
- Ligne export : 35020 · id 132469

#### em Engine Max Temp  `IP`
- Propriétés : Unit=°C · Default mode={110}
- Utilisé par : `M1 - Charge`, `M2 - Charge`, `M3 - Charge`, `Single adjust item: Engine Max Temp`
- Ligne export : 37281 · id 132801

#### em Controller Fan Temp  `IP`
> Difference between hotest temp allowed and current temp
- Propriétés : Unit=°C · Default mode={70}
- Utilisé par : `M1 - NEED TO FAN`, `M2 - NEED TO FAN`, `Single adjust item: Controller Fan Temp`
- Ligne export : 37293 · id 132802

#### M1 - Heatsink  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `Heatsink - S.M1.Right [°C]`
- Fonction *Zapi* :
  - **Controlling** = `Heatsink - Z.M1.Right [°C]`
- Lit : `Heatsink - S.M1.Right`, `Heatsink - Z.M1.Right`, `em1 M-Track - Brand`
- Utilisé par : `M1 - NEED TO FAN`, `M1 - NEED TO PUMP`, `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 37305 · id 132803

#### M1 - NEED TO FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M1 - Heatsink [°C] >= em Controller Fan Temp [°C]`
- Lit : `M1 - Heatsink`, `em Controller Fan Temp`
- Utilisé par : `NEED FAN`
- Ligne export : 37378 · id 132818

#### em Engine Eco Temp  `IP`
- Propriétés : Unit=°C · Default mode={90}
- Utilisé par : `M1 - ENGINE HOT`, `M2 - ENGINE HOT`, `M3 - ENGINE HOT`, `Single adjust item: Engine Eco Temp`
- Ligne export : 37423 · id 132826

#### em Controller Pump Temp  `IP`
> Difference between hotest temp allowed and current temp
- Propriétés : Unit=°C · Default mode={65}
- Utilisé par : `M1 - NEED TO PUMP`, `M2 - NEED TO PUMP`, `Single adjust item: Controller Pump Temp`
- Ligne export : 37435 · id 132827

#### M1 - NEED TO PUMP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M1 - Heatsink [°C] >= em Controller Pump Temp [°C]`
- Lit : `M1 - Heatsink`, `em Controller Pump Temp`
- Utilisé par : `NEED PUMP`
- Ligne export : 37447 · id 132828

#### M1 - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `CURRENT - S.M1.Right [A]`
- Fonction *Zapi* :
  - **Controlling** = `Actual_current - Z.M1.Right [A]`
- Lit : `Actual_current - Z.M1.Right`, `CURRENT - S.M1.Right`, `em1 M-Track - Brand`
- Utilisé par : `Current Bat`, `Instant current Filter`, `Measure group: Track Engine Sev/Zapi`
- Ligne export : 37492 · id 132836

#### M1 - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `CAN OK - S.M1.Right`
- Fonction *Zapi* :
  - **Activating** = `CAN OK - Z.M1.Right`
- Lit : `CAN OK - S.M1.Right`, `CAN OK - Z.M1.Right`, `em1 M-Track - Brand`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Canbus`
- Ligne export : 37565 · id 132851

#### M1 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `RUN - S.M1.Right`
- Fonction *Zapi* :
  - **Activating** = `RUN - Z.M1.Right`
- Lit : `RUN - S.M1.Right`, `RUN - Z.M1.Right`, `em1 M-Track - Brand`
- Utilisé par : `Statistics log: Electronic Stats logs`
- Ligne export : 37639 · id 132866

#### M1 - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `Ready - S.M1.Right`
- Fonction *Zapi* :
  - **Activating** = `True`
- Lit : `Ready - S.M1.Right`, `em1 M-Track - Brand`
- Utilisé par : *(personne)*
- Ligne export : 37713 · id 132881

#### M1 - Voltage  `IMAC`
- Propriétés : Unit=V · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `Voltage - S.M1.Right [V]`
- Fonction *Zapi* :
  - **Controlling** = `Batterie Voltage - Z.M1.Right [V]`
- Lit : `Batterie Voltage - Z.M1.Right`, `Voltage - S.M1.Right`, `em1 M-Track - Brand`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Track Engine Sev/Zapi`
- Ligne export : 37787 · id 132896

#### M1 - Torque  `IMAC`
- Propriétés : Unit=Nm · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `Torque actual - S.M1.Right [Nm]`
- Fonction *Zapi* :
  - **Controlling** = `Torque - Z.M1.Right [Nm]`
- Lit : `Torque - Z.M1.Right`, `Torque actual - S.M1.Right`, `em1 M-Track - Brand`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Track Engine Sev/Zapi`
- Ligne export : 37859 · id 132911

#### M1 - Speed  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `Speed - S.M1.Right [rpm]`
- Fonction *Zapi* :
  - **Controlling** = `Actual_speed - Z.M1.Right [rpm]`
- Lit : `Actual_speed - Z.M1.Right`, `Speed - S.M1.Right`, `em1 M-Track - Brand`
- Utilisé par : `M1 - Mechanical power`, `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Track Engine Sev/Zapi`
- Ligne export : 37931 · id 132926

#### M1 - KTY  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `KTY - S.M1.Right [°C]`
- Fonction *Zapi* :
  - **Controlling** = `Motor_Temp - Z.M1.Right [°C]`
- Lit : `KTY - S.M1.Right`, `Motor_Temp - Z.M1.Right`, `em1 M-Track - Brand`
- Utilisé par : `M1 - Charge`, `M1 - ENGINE HOT`, `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Track Engine Sev/Zapi`
- Ligne export : 38004 · id 132941

#### M1 - Charge  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `((MaxOf((M1 - KTY [°C] - 40), 0)) / (em Engine Max Temp [°C] - 40)) * 100`
- Lit : `M1 - KTY`, `em Engine Max Temp`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 38077 · id 132956

#### M1 - ENGINE HOT  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `M1 - KTY [°C] >= em Engine Eco Temp [°C]`
- Lit : `M1 - KTY`, `em Engine Eco Temp`
- Utilisé par : `Event log: Electronic logs`
- Ligne export : 38157 · id 132968

#### M2 - Heatsink  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `Heatsink - S.M2.Left [°C]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Heatsink [°C]`
- Lit : `Heatsink - S.M2.Left`, `ZAPI_M2_Heatsink`, `em1 M-Track - Brand`
- Utilisé par : `M2 - NEED TO FAN`, `M2 - NEED TO PUMP`, `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 38202 · id 132976

#### M2 - NEED TO FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M2 - Heatsink [°C] >= em Controller Fan Temp [°C]`
- Lit : `M2 - Heatsink`, `em Controller Fan Temp`
- Utilisé par : `NEED FAN`
- Ligne export : 38275 · id 132991

#### M2 - NEED TO PUMP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M2 - Heatsink [°C] >= em Controller Pump Temp [°C]`
- Lit : `M2 - Heatsink`, `em Controller Pump Temp`
- Utilisé par : `NEED PUMP`
- Ligne export : 38320 · id 132999

#### M2 - CURRENT  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `CURRENT - S.M2.Left [A]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Actual_current [A]`
- Lit : `CURRENT - S.M2.Left`, `ZAPI_M2_Actual_current`, `em1 M-Track - Brand`
- Utilisé par : `Current Bat`, `Instant current Filter`, `Measure group: Track Engine Sev/Zapi`
- Ligne export : 38365 · id 133007

#### M2 - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `CAN OK - S.M2.Left`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M2_CAN OK`
- Lit : `CAN OK - S.M2.Left`, `ZAPI_M2_CAN OK`, `em1 M-Track - Brand`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Canbus`
- Ligne export : 38438 · id 133022

#### M2 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `RUN - S.M2.Left`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M2_RUN`
- Lit : `RUN - S.M2.Left`, `ZAPI_M2_RUN`, `em1 M-Track - Brand`
- Utilisé par : `Statistics log: Electronic Stats logs`
- Ligne export : 38512 · id 133037

#### M2 - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `Ready - S.M2.Left`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M2_READY`
- Lit : `Ready - S.M2.Left`, `ZAPI_M2_READY`, `em1 M-Track - Brand`
- Utilisé par : *(personne)*
- Ligne export : 38586 · id 133052

#### M2 - Voltage  `IMAC`
- Propriétés : Unit=V · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `Voltage - S.M2.Left [V]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Batterie Voltage [V]`
- Lit : `Voltage - S.M2.Left`, `ZAPI_M2_Batterie Voltage`, `em1 M-Track - Brand`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Track Engine Sev/Zapi`
- Ligne export : 38660 · id 133067

#### M2 - Torque  `IMAC`
- Propriétés : Unit=Nm · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `Torque actual - S.M2.Left [Nm]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Torque [Nm]`
- Lit : `Torque actual - S.M2.Left`, `ZAPI_M2_Torque`, `em1 M-Track - Brand`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Track Engine Sev/Zapi`
- Ligne export : 38732 · id 133082

#### M2 - Speed  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `Speed - S.M2.Left [rpm]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Actual_speed [rpm]`
- Lit : `Speed - S.M2.Left`, `ZAPI_M2_Actual_speed`, `em1 M-Track - Brand`
- Utilisé par : `M2 - Mechanical power`, `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Track Engine Sev/Zapi`
- Ligne export : 38804 · id 133097

#### M2 - KTY  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Controlling** = `KTY - S.M2.Left [°C]`
- Fonction *Zapi* :
  - **Controlling** = `ZAPI_M2_Motor_Temp [°C]`
- Lit : `KTY - S.M2.Left`, `ZAPI_M2_Motor_Temp`, `em1 M-Track - Brand`
- Utilisé par : `M2 - Charge`, `M2 - ENGINE HOT`, `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Track Engine Sev/Zapi`
- Ligne export : 38877 · id 133112

#### M2 - Charge  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `((MaxOf((M2 - KTY [°C] - 40), 0)) / (em Engine Max Temp [°C] - 40)) * 100`
- Lit : `M2 - KTY`, `em Engine Max Temp`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 38950 · id 133127

#### M2 - ENGINE HOT  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `M2 - KTY [°C] >= em Engine Eco Temp [°C]`
- Lit : `M2 - KTY`, `em Engine Eco Temp`
- Utilisé par : `Event log: Electronic logs`
- Ligne export : 39030 · id 133139

#### M1 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `Error mode - S.M1.Right`
- Fonction *Zapi* :
  - **Activating** = `Error mode - Z.M1.Right`
- Lit : `Error mode - S.M1.Right`, `Error mode - Z.M1.Right`, `em1 M-Track - Brand`
- Utilisé par : `Engines Error`, `Tracks Engines Crash`
- Ligne export : 39075 · id 133147

#### M2 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em1 M-Track - Brand
- Fonction *Sevcon* :
  - **Activating** = `Error mode - S.M2.Left`
- Fonction *Zapi* :
  - **Activating** = `ZAPI_M2_Error mode`
- Lit : `Error mode - S.M2.Left`, `ZAPI_M2_Error mode`, `em1 M-Track - Brand`
- Utilisé par : `Engines Error`, `Tracks Engines Crash`
- Ligne export : 39149 · id 133162

#### Instant current Filter  `SFC`
- Propriétés : Input channel=M1 - CURRENT [A] · Enable=Yes · Type=BWL · BWL=20
- Lit : `M1 - CURRENT`
- Utilisé par : `Couple Moteur`, `Couple Moteur`, `M1 - 100A-125A`, `M1 - 25A-50A`, `M1 - 50A-75A`, `M1 - 75A-100A`, `M1 - up to 125A`, `M2 - 100A-125A`, `M2 - 25A-50A`, `M2 - 50A-75A`, `M2 - 75A-100A`, `M2 - up to 125A`
- Ligne export : 39223 · id 133177

#### Couple Moteur  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `26 * courbe(((0,8 * Instant current Filter [A]) / 33): {{0; 0}; {1; 1}; {2; 1,8}; {2,5; 2,18}; {3; 2,45}; {3,5; 2,62}; {4; 2,75}}, Freeze)`
- Lit : `Instant current Filter`
- Utilisé par : `M1 - Mechanical power`, `M1 - Torque Tracks`, `M2 - Mechanical power`, `M2 - Torque tracks`
- Ligne export : 39235 · id 133178

#### M1 - Mechanical power  `MAC`
- Propriétés : Unit=kW · Limiting object group=Signed
- Logique :
  - **Controlling** = `((M1 - Speed [rpm] * 0,104719) * Couple Moteur [Nm]) / 1000`
- Lit : `Couple Moteur`, `M1 - Speed`
- Utilisé par : *(personne)*
- Ligne export : 39327 · id 133189

#### M1 - Torque Tracks  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Couple Moteur [Nm] * 37,2`
- Lit : `Couple Moteur`
- Utilisé par : *(personne)*
- Ligne export : 39389 · id 133199

#### M1 - 25A-50A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(25 < Instant current Filter [A]) AND (Instant current Filter [A] <= 50)`
- Lit : `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 39433 · id 133207

#### M1 - 50A-75A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(50 < Instant current Filter [A]) AND (Instant current Filter [A] <= 75)`
- Lit : `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 39487 · id 133216

#### M1 - 75A-100A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(75 < Instant current Filter [A]) AND (Instant current Filter [A] <= 100)`
- Lit : `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 39541 · id 133225

#### M1 - 100A-125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(100 < Instant current Filter [A]) AND (Instant current Filter [A] <= 125)`
- Lit : `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 39595 · id 133234

#### M1 - up to 125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `125 < Instant current Filter [A]`
- Lit : `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 39649 · id 133243

#### Instant current Filter  `SFC`
- Propriétés : Input channel=M2 - CURRENT [A] · Enable=Yes · Type=Moving average · Window size=25
- Lit : `M2 - CURRENT`
- Utilisé par : `Couple Moteur`, `Couple Moteur`, `M1 - 100A-125A`, `M1 - 25A-50A`, `M1 - 50A-75A`, `M1 - 75A-100A`, `M1 - up to 125A`, `M2 - 100A-125A`, `M2 - 25A-50A`, `M2 - 50A-75A`, `M2 - 75A-100A`, `M2 - up to 125A`
- Ligne export : 39694 · id 133251

#### Couple Moteur  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `26 * courbe(((0,8 * Instant current Filter [A]) / 33): {{0; 0}; {1; 1}; {2; 1,8}; {2,5; 2,18}; {3; 2,45}; {3,5; 2,62}; {4; 2,75}}, Freeze)`
- Lit : `Instant current Filter`
- Utilisé par : `M1 - Mechanical power`, `M1 - Torque Tracks`, `M2 - Mechanical power`, `M2 - Torque tracks`
- Ligne export : 39706 · id 133252

#### M2 - Mechanical power  `MAC`
- Propriétés : Unit=kW · Limiting object group=Signed
- Logique :
  - **Controlling** = `((M2 - Speed [rpm] * 0,104719) * Couple Moteur [Nm]) / 1000`
- Lit : `Couple Moteur`, `M2 - Speed`
- Utilisé par : *(personne)*
- Ligne export : 39798 · id 133263

#### M2 - Torque tracks  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Couple Moteur [Nm] * 37,2`
- Lit : `Couple Moteur`
- Utilisé par : *(personne)*
- Ligne export : 39860 · id 133273

#### M2 - 25A-50A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(25 < Instant current Filter [A]) AND (Instant current Filter [A] <= 50)`
- Lit : `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 39904 · id 133281

#### M2 - 50A-75A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(50 < Instant current Filter [A]) AND (Instant current Filter [A] <= 75)`
- Lit : `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 39958 · id 133290

#### M2 - 75A-100A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(75 < Instant current Filter [A]) AND (Instant current Filter [A] <= 100)`
- Lit : `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 40012 · id 133299

#### M2 - 100A-125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(100 < Instant current Filter [A]) AND (Instant current Filter [A] <= 125)`
- Lit : `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 40066 · id 133308

#### M2 - up to 125A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `125 < Instant current Filter [A]`
- Lit : `Instant current Filter`
- Utilisé par : *(personne)*
- Ligne export : 40120 · id 133317

## mc.Electric / E.MOTORS / E.M-Tracks / E.Sevcon.M1.M2.gen4 — actif seulement si `Is_MT_Sevcon`

#### Speed CAN Right  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Filter Right [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Filter Right`
- Utilisé par : `Convert Right`, `Fordward Right - S.M1.Right`, `Reverse Right - S.M1.Right`
- Ligne export : 35102 · id 132478

#### 0x341 GEN4  `GFIN`
- Propriétés : Identifier=0x341 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Motor Speed - S.M1.Right [rpm]; 0}; {Actual Current - S.M1.Right [A]; 32}; {Torque - S.M1.Right [Raw]; 48}} · Module=Sev_M_Track (Generic) · Module index=1
- Lit : `Actual Current - S.M1.Right`, `Motor Speed - S.M1.Right`, `Torque - S.M1.Right`
- Utilisé par : `CAN OK - S.M1.Right`
- Ligne export : 35116 · id 132479

#### Actual Current - S.M1.Right  `GPIN`
- Propriétés : Unit=A · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x341 GEN4`, `CURRENT - S.M1.Right`
- Ligne export : 35141 · id 132480

#### CURRENT - S.M1.Right  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Actual Current - S.M1.Right [A]`
- Lit : `Actual Current - S.M1.Right`
- Utilisé par : `M1 - CURRENT`
- Ligne export : 35154 · id 132481

#### 0x331 GEN4  `GFIN`
- Propriétés : Identifier=0x331 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Error - S.M1.Right; 16}; {Statut - S.M1.Right [State]; 0}} · Module=Sev_M_Track (Generic) · Module index=0
- Lit : `Error - S.M1.Right`, `State`, `Statut - S.M1.Right`
- Utilisé par : *(personne)*
- Ligne export : 35196 · id 132489

#### Error - S.M1.Right  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x331 GEN4`, `Error 1 - MEM - S.M1.Right`, `Error mode - S.M1.Right`, `New Error Code - S.M1.Right`, `e Right Engine 1 CMSG - S.M1.Right mc`, `Event log: Electronic logs`
- Ligne export : 35218 · id 132490

#### 0x351 GEN4  `GFIN`
- Propriétés : Identifier=0x351 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{KTY - S.M1.Right [°C]; 0}; {Heatsink - S.M1.Right [°C]; 16}; {Voltage - S.M1.Right [Raw]; 24}} · Module=Sev_M_Track (Generic) · Module index=2
- Lit : `Heatsink - S.M1.Right`, `KTY - S.M1.Right`, `Voltage - S.M1.Right`
- Utilisé par : *(personne)*
- Ligne export : 35231 · id 132491

#### KTY - S.M1.Right  `GPIN`
- Propriétés : Unit=°C · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x351 GEN4`, `M1 - KTY`
- Ligne export : 35256 · id 132492

#### Error mode - S.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `Error - S.M1.Right`
  - **Blocking** = `Error - S.M1.Right = 0`
- Lit : `Error - S.M1.Right`
- Utilisé par : `FS1 Switch - S.M1.Right`, `M1 - Error mode`, `Normal Mode - S.M1.Right`, `e Right Engine 1 CMSG - S.M1.Right mc`
- Ligne export : 35269 · id 132493

#### Normal Mode - S.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Error mode - S.M1.Right)`
- Lit : `Error mode - S.M1.Right`
- Utilisé par : `Ready - S.M1.Right`
- Ligne export : 35321 · id 132502

#### CAN OK - S.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `0x341 GEN4`
- Lit : `0x341 GEN4`
- Utilisé par : `M1 - CAN OK`
- Ligne export : 35365 · id 132510

#### Motor Speed - S.M1.Right  `GPIN`
- Propriétés : Unit=rpm · Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x341 GEN4`, `RUN - S.M1.Right`, `Speed - S.M1.Right`
- Ligne export : 35408 · id 132518

#### RUN - S.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Motor Speed - S.M1.Right [rpm] <> 0`
- Lit : `Motor Speed - S.M1.Right`
- Utilisé par : `M1 - RUN`
- Ligne export : 35421 · id 132519

#### Heatsink - S.M1.Right  `GPIN`
- Propriétés : Unit=°C · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `0x351 GEN4`, `M1 - Heatsink`
- Ligne export : 35466 · id 132527

#### Ready - S.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Normal Mode - S.M1.Right`
- Lit : `Normal Mode - S.M1.Right`
- Utilisé par : `M1 - Ready`
- Ligne export : 35478 · id 132528

#### e Right Engine 1 CMSG - S.M1.Right mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header, English=e1029 Right Engine · Text, English=Error, stop battery, wait one minute, restart. · Channel=Error - S.M1.Right
- Logique :
  - **Showing** = `Error mode - S.M1.Right`
- Lit : `Error - S.M1.Right`, `Error mode - S.M1.Right`
- Utilisé par : *(personne)*
- Ligne export : 35521 · id 132536

#### Convert Right  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe(Speed CAN Right [%]: {{-100; 3000}; {0; 0}; {100; 3000}}, Freeze)`
- Lit : `Speed CAN Right`
- Utilisé par : `Throttle Input Voltage - S.M1.Right`
- Ligne export : 35567 · id 132544

#### Throttle Input Voltage - S.M1.Right  `GPOUT`
- Propriétés : Input value=Convert Right · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Convert Right`
- Utilisé par : `outGEN - 4 - S.M1.Right`
- Ligne export : 35620 · id 132552

#### VARIATOR ON Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR SUPER ON E mc`
- Lit : `VARIATOR SUPER ON E mc`
- Utilisé par : `Fordward - S.M2.Left`, `Fordward Right - S.M1.Right`, `Reverse - S.M2.Left`, `Reverse Right - S.M1.Right`
- Ligne export : 35632 · id 132553

#### Fordward Right - S.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed CAN Right [%] < 0) AND (VARIATOR ON Wait)`
- Lit : `Speed CAN Right`, `VARIATOR ON Wait`
- Utilisé par : `FS1 Switch - S.M1.Right`, `Fordward Switch - S.M1.Right`
- Ligne export : 35675 · id 132561

#### Fordward Switch - S.M1.Right  `GPOUT`
- Propriétés : Input value=Fordward Right - S.M1.Right · Length=1 bit · Type=Unsigned integer
- Lit : `Fordward Right - S.M1.Right`
- Utilisé par : `outGEN - 4 - S.M1.Right`
- Ligne export : 35727 · id 132570

#### Reverse Right - S.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed CAN Right [%] > 0) AND (VARIATOR ON Wait)`
- Lit : `Speed CAN Right`, `VARIATOR ON Wait`
- Utilisé par : `FS1 Switch - S.M1.Right`, `Inch reverse switch - S.M1.Right`
- Ligne export : 35738 · id 132571

#### Inch reverse switch - S.M1.Right  `GPOUT`
- Propriétés : Input value=Reverse Right - S.M1.Right · Length=1 bit · Type=Unsigned integer
- Lit : `Reverse Right - S.M1.Right`
- Utilisé par : `outGEN - 4 - S.M1.Right`
- Ligne export : 35790 · id 132580

#### FS1 Switch - S.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Fordward Right - S.M1.Right) OR (Reverse Right - S.M1.Right)`
  - **Blocking** = `Error mode - S.M1.Right`
- Lit : `Error mode - S.M1.Right`, `Fordward Right - S.M1.Right`, `Reverse Right - S.M1.Right`
- Utilisé par : `FS1 Switch - S.M1.Right`, `outGEN - 4 - S.M1.Right`
- Ligne export : 35801 · id 132581

#### FS1 Switch - S.M1.Right  `GPOUT`
- Propriétés : Input value=FS1 Switch - S.M1.Right · Length=1 bit · Type=Unsigned integer
- Lit : `FS1 Switch - S.M1.Right`
- Utilisé par : `outGEN - 4 - S.M1.Right`
- Ligne export : 35858 · id 132591

#### outGEN - 4 - S.M1.Right  `GFOUT`
- Propriétés : Identifier=0x411 · Data length=8 · Send method=Continuously · Transmit rate=Every cycle · Unused bits=Set to 0 · Parameters={{Throttle Input Voltage - S.M1.Right; 0}; {Fordward Switch - S.M1.Right; 16}; {Inch reverse switch - S.M1.Right; 17}; {FS1 Switch - S.M1.Right; 18}} · Module=Sev_M_Track (Generic) · Module index=2
- Lit : `FS1 Switch - S.M1.Right`, `Fordward Switch - S.M1.Right`, `Inch reverse switch - S.M1.Right`, `Throttle Input Voltage - S.M1.Right`
- Utilisé par : *(personne)*
- Ligne export : 35869 · id 132592

#### Torque - S.M1.Right  `GPIN`
- Propriétés : Unit=Raw · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x341 GEN4`, `Torque actual - S.M1.Right`
- Ligne export : 35897 · id 132593

#### Voltage - S.M1.Right  `GPIN`
- Propriétés : Unit=Raw · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x351 GEN4`, `M1 - Voltage`, `Voltage - S.M1.Right`
- Ligne export : 35910 · id 132594

#### Voltage - S.M1.Right  `IMAC`
- Propriétés : Unit=V
- Logique :
  - **Controlling** = `Voltage - S.M1.Right [Raw] * 0,0625`
- Lit : `Voltage - S.M1.Right`
- Utilisé par : `0x351 GEN4`, `M1 - Voltage`
- Ligne export : 35923 · id 132595

#### Torque actual - S.M1.Right  `IMAC`
- Propriétés : Unit=Nm
- Logique :
  - **Controlling** = `(Torque - S.M1.Right [Raw] * 0,0625) * 37,2`
- Lit : `Torque - S.M1.Right`
- Utilisé par : `M1 - Torque`
- Ligne export : 35966 · id 132603

#### Statut - S.M1.Right  `GPIN`
- Propriétés : Unit=State · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x331 GEN4`
- Ligne export : 36018 · id 132612

#### Error 1 - MEM - S.M1.Right  `MEM`
- Propriétés : Input channel=Error - S.M1.Right · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(New Error Code - S.M1.Right)`
- Lit : `Error - S.M1.Right`, `New Error Code - S.M1.Right`
- Utilisé par : `New Error Code - S.M1.Right`
- Ligne export : 36031 · id 132613

#### New Error Code - S.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Error - S.M1.Right <> Error 1 - MEM - S.M1.Right`
  - **Blocking** = `(Error - S.M1.Right = 0) OR (Error - S.M1.Right = 19073)`
- Lit : `Error - S.M1.Right`, `Error 1 - MEM - S.M1.Right`
- Utilisé par : `Error 1 - MEM - S.M1.Right`, `Event log: Electronic logs`
- Ligne export : 36076 · id 132621

#### Speed - S.M1.Right  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Motor Speed - S.M1.Right [rpm] * -1`
- Lit : `Motor Speed - S.M1.Right`
- Utilisé par : `M1 - Speed`
- Ligne export : 36139 · id 132631

#### 0x342 GEN4  `GFIN`
- Propriétés : Identifier=0x342 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Motor Speed - S.M2.Left [rpm]; 0}; {Actual Current - S.M2.Left [A]; 32}; {Torque actual - S.M2.Left [Raw]; 48}} · Module=Sev_M_Track (Generic) · Module index=4
- Lit : `Actual Current - S.M2.Left`, `Motor Speed - S.M2.Left`, `Torque actual - S.M2.Left`
- Utilisé par : `CAN OK - S.M2.Left`
- Ligne export : 36183 · id 132639

#### Actual Current - S.M2.Left  `GPIN`
- Propriétés : Unit=A · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x342 GEN4`, `CURRENT - S.M2.Left`
- Ligne export : 36208 · id 132640

#### CURRENT - S.M2.Left  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Actual Current - S.M2.Left [A]`
- Lit : `Actual Current - S.M2.Left`
- Utilisé par : `M2 - CURRENT`
- Ligne export : 36221 · id 132641

#### 0x332 GEN4  `GFIN`
- Propriétés : Identifier=0x332 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Error - S.M2.Left; 16}; {Statut - S.M2.Left [Status]; 0}} · Module=Sev_M_Track (Generic) · Module index=3
- Lit : `Error - S.M2.Left`, `Statut - S.M2.Left`
- Utilisé par : *(personne)*
- Ligne export : 36263 · id 132649

#### Error - S.M2.Left  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x332 GEN4`, `Error 2 - MEM - S.M2.Left`, `Error mode - S.M2.Left`, `New Error Code - S.M2.Left`, `e Left Engine 2 CMSG - S.M2.Left mc`, `Event log: Electronic logs`
- Ligne export : 36285 · id 132650

#### 0x352 GEN4  `GFIN`
- Propriétés : Identifier=0x352 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{KTY - S.M2.Left [°C]; 0}; {Heatsink - S.M2.Left [°C]; 16}; {Voltage - S.M2.Left [Raw]; 24}} · Module=Sev_M_Track (Generic) · Module index=5
- Lit : `Heatsink - S.M2.Left`, `KTY - S.M2.Left`, `Voltage - S.M2.Left`
- Utilisé par : *(personne)*
- Ligne export : 36298 · id 132651

#### KTY - S.M2.Left  `GPIN`
- Propriétés : Unit=°C · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x352 GEN4`, `M2 - KTY`
- Ligne export : 36323 · id 132652

#### Error mode - S.M2.Left  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `Error - S.M2.Left`
  - **Blocking** = `Error - S.M2.Left = 0`
- Lit : `Error - S.M2.Left`
- Utilisé par : `FS1 Switch - S.M2.Left`, `M2 - Error mode`, `Normal mode - S.M2.Left`, `e Left Engine 2 CMSG - S.M2.Left mc`
- Ligne export : 36336 · id 132653

#### Normal mode - S.M2.Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Error mode - S.M2.Left)`
- Lit : `Error mode - S.M2.Left`
- Utilisé par : `Ready - S.M2.Left`
- Ligne export : 36388 · id 132662

#### CAN OK - S.M2.Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `0x342 GEN4`
- Lit : `0x342 GEN4`
- Utilisé par : `M2 - CAN OK`
- Ligne export : 36432 · id 132670

#### Motor Speed - S.M2.Left  `GPIN`
- Propriétés : Unit=rpm · Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x342 GEN4`, `RUN - S.M2.Left`, `Speed - S.M2.Left`
- Ligne export : 36475 · id 132678

#### RUN - S.M2.Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Motor Speed - S.M2.Left [rpm] <> 0`
- Lit : `Motor Speed - S.M2.Left`
- Utilisé par : `M2 - RUN`
- Ligne export : 36488 · id 132679

#### Heatsink - S.M2.Left  `GPIN`
- Propriétés : Unit=°C · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `0x352 GEN4`, `M2 - Heatsink`
- Ligne export : 36533 · id 132687

#### Ready - S.M2.Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Normal mode - S.M2.Left`
- Lit : `Normal mode - S.M2.Left`
- Utilisé par : `M2 - Ready`
- Ligne export : 36545 · id 132688

#### e Left Engine 2 CMSG - S.M2.Left mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header, English=e1078 Left Engine · Text, English=Error, stop battery, wait one minute, restart. · Channel=Error - S.M2.Left
- Logique :
  - **Showing** = `Error mode - S.M2.Left`
- Lit : `Error - S.M2.Left`, `Error mode - S.M2.Left`
- Utilisé par : *(personne)*
- Ligne export : 36588 · id 132696

#### Torque actual - S.M2.Left  `GPIN`
- Propriétés : Unit=Raw · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x342 GEN4`, `M2 - Torque`, `Torque actual - S.M2.Left`
- Ligne export : 36634 · id 132704

#### Voltage - S.M2.Left  `GPIN`
- Propriétés : Unit=Raw · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x352 GEN4`, `M2 - Voltage`, `Voltage - S.M2.Left`
- Ligne export : 36647 · id 132705

#### Voltage - S.M2.Left  `IMAC`
- Propriétés : Unit=V
- Logique :
  - **Controlling** = `Voltage - S.M2.Left [Raw] * 0,0625`
- Lit : `Voltage - S.M2.Left`
- Utilisé par : `0x352 GEN4`, `M2 - Voltage`
- Ligne export : 36660 · id 132706

#### Torque actual - S.M2.Left  `IMAC`
- Propriétés : Unit=Nm
- Logique :
  - **Controlling** = `(Torque actual - S.M2.Left [Raw] * 0,0625) * 37,2`
- Lit : `Torque actual - S.M2.Left`
- Utilisé par : `0x342 GEN4`, `M2 - Torque`
- Ligne export : 36703 · id 132714

#### Speed CAN Left Sev  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Filter Left [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Filter Left`
- Utilisé par : `Convert Left`, `Fordward - S.M2.Left`, `Reverse - S.M2.Left`
- Ligne export : 36755 · id 132723

#### Convert Left  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe(Speed CAN Left Sev [%]: {{-100; 3000}; {0; 0}; {100; 3000}}, Freeze)`
- Lit : `Speed CAN Left Sev`
- Utilisé par : `Throttle Input Voltage - S.M2.Left`
- Ligne export : 36769 · id 132724

#### Throttle Input Voltage - S.M2.Left  `GPOUT`
- Propriétés : Input value=Convert Left · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Convert Left`
- Utilisé par : `GEN - 4 - S.M2.Left`
- Ligne export : 36822 · id 132732

#### VARIATOR ON Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR SUPER ON E mc`
- Lit : `VARIATOR SUPER ON E mc`
- Utilisé par : `Fordward - S.M2.Left`, `Fordward Right - S.M1.Right`, `Reverse - S.M2.Left`, `Reverse Right - S.M1.Right`
- Ligne export : 36834 · id 132733

#### Fordward - S.M2.Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed CAN Left Sev [%] < 0) AND (VARIATOR ON Wait)`
- Lit : `Speed CAN Left Sev`, `VARIATOR ON Wait`
- Utilisé par : `FS1 Switch - S.M2.Left`, `Fordward Switch - S.M2.Left`
- Ligne export : 36877 · id 132741

#### Fordward Switch - S.M2.Left  `GPOUT`
- Propriétés : Input value=Fordward - S.M2.Left · Length=1 bit · Type=Unsigned integer
- Lit : `Fordward - S.M2.Left`
- Utilisé par : `GEN - 4 - S.M2.Left`
- Ligne export : 36929 · id 132750

#### Reverse - S.M2.Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed CAN Left Sev [%] > 0) AND (VARIATOR ON Wait)`
- Lit : `Speed CAN Left Sev`, `VARIATOR ON Wait`
- Utilisé par : `FS1 Switch - S.M2.Left`, `Inch reverse switch - S.M2.Left`
- Ligne export : 36940 · id 132751

#### Inch reverse switch - S.M2.Left  `GPOUT`
- Propriétés : Input value=Reverse - S.M2.Left · Length=1 bit · Type=Unsigned integer
- Lit : `Reverse - S.M2.Left`
- Utilisé par : `GEN - 4 - S.M2.Left`
- Ligne export : 36992 · id 132760

#### FS1 Switch - S.M2.Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Fordward - S.M2.Left) OR (Reverse - S.M2.Left)`
  - **Blocking** = `Error mode - S.M2.Left`
- Lit : `Error mode - S.M2.Left`, `Fordward - S.M2.Left`, `Reverse - S.M2.Left`
- Utilisé par : `FS1 Switch - S.M2.Left`, `GEN - 4 - S.M2.Left`
- Ligne export : 37003 · id 132761

#### FS1 Switch - S.M2.Left  `GPOUT`
- Propriétés : Input value=FS1 Switch - S.M2.Left · Length=1 bit · Type=Unsigned integer
- Lit : `FS1 Switch - S.M2.Left`
- Utilisé par : `GEN - 4 - S.M2.Left`
- Ligne export : 37060 · id 132771

#### GEN - 4 - S.M2.Left  `GFOUT`
- Propriétés : Identifier=0x412 · Data length=8 · Send method=Continuously · Transmit rate=Every cycle · Unused bits=Set to 0 · Parameters={{Throttle Input Voltage - S.M2.Left; 0}; {Fordward Switch - S.M2.Left; 16}; {Inch reverse switch - S.M2.Left; 17}; {FS1 Switch - S.M2.Left; 18}} · Module=Sev_M_Track (Generic) · Module index=1
- Lit : `FS1 Switch - S.M2.Left`, `Fordward Switch - S.M2.Left`, `Inch reverse switch - S.M2.Left`, `Throttle Input Voltage - S.M2.Left`
- Utilisé par : *(personne)*
- Ligne export : 37071 · id 132772

#### Statut - S.M2.Left  `GPIN`
- Propriétés : Unit=Status · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x332 GEN4`
- Ligne export : 37099 · id 132773

#### Error 2 - MEM - S.M2.Left  `MEM`
- Propriétés : Input channel=Error - S.M2.Left · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(New Error Code - S.M2.Left)`
- Lit : `Error - S.M2.Left`, `New Error Code - S.M2.Left`
- Utilisé par : `New Error Code - S.M2.Left`
- Ligne export : 37112 · id 132774

#### New Error Code - S.M2.Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Error - S.M2.Left <> Error 2 - MEM - S.M2.Left`
  - **Blocking** = `(Error - S.M2.Left = 0) OR (Error - S.M2.Left = 19073)`
- Lit : `Error - S.M2.Left`, `Error 2 - MEM - S.M2.Left`
- Utilisé par : `Error 2 - MEM - S.M2.Left`, `Event log: Electronic logs`
- Ligne export : 37157 · id 132782

#### Speed - S.M2.Left  `MAC`
- Propriétés : Unit=rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Motor Speed - S.M2.Left [rpm] * -1`
- Lit : `Motor Speed - S.M2.Left`
- Utilisé par : `M2 - Speed`
- Ligne export : 37220 · id 132792

#### SYNC heartbeat GEN4  `GFOUT`
- Propriétés : Identifier=0x80 · Data length=0 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={} · Module=Sev_M_Track (Generic) · Module index=0
- Utilisé par : *(personne)*
- Ligne export : 37264 · id 132800

## mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M1.Right.gen — actif seulement si `Is_MT_Zapi`

#### Node_ID  `IP`
- Propriétés : Mode selector=em ZAPI Node · Default mode: 8-10={8} · Mode 1: 1-4={1} · Mode 2: 4-8={4}
- Lit : `em ZAPI Node`
- Utilisé par : `EMERG`, `HeartBeat`, `Node ID`, `PDO1_RX`, `PDO1_TX`, `PDO2_TX`
- Ligne export : 30467 · id 131747

#### Node ID  `GPOUT`
- Propriétés : Input value=Node_ID · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Node_ID`
- Utilisé par : `NMT`
- Ligne export : 30483 · id 131748

#### Speed_CAN_Right  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Filter Right [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Filter Right`
- Utilisé par : `Speed_Right`
- Ligne export : 30494 · id 131749

#### Speed_Right  `MAC`
- Propriétés : Unit=rpm
- Logique :
  ```qcode
  Result := Speed_CAN_Right * 30
  ```
- Lit : `Speed_CAN_Right`
- Utilisé par : `Enable`, `Forward`, `Reverse`, `Target_Speed_can`
- Ligne export : 30508 · id 131750

#### EMERG  `IMAC`
- Logique :
  - **Controlling** = `0x80 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 30526 · id 131760

#### GFIN PDO2_TX  `GFIN`
- Propriétés : Identifier=EMERG · Data length=Dont care · Paged protocol={Not used} · Parameters={{Right Zapi Error Code; 0}; {alarm present; 16}; {Zapi alarm code; 24}; {flag alarm; 32}; {extra info alarm; 40}} · Module=Zapi_M_Track (Generic) · Module index=3
- Lit : `EMERG`, `Right Zapi Error Code`, `Zapi alarm code`, `alarm present`, `extra info alarm`, `flag alarm`
- Utilisé par : *(personne)*
- Ligne export : 30569 · id 131768

#### Right Zapi Error Code  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Error 1 - MEM - Z.M1.Right`, `GFIN PDO2_TX`, `New Error Code - Z.M1.Right`, `e Right Error - Z.M1.Right mc`, `Event log: Electronic logs`, `Measure group: Track Zapi Right`
- Ligne export : 30600 · id 131769

#### alarm present  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `Error mode - Z.M1.Right`, `GFIN PDO2_TX`, `e Right Error - Z.M1.Right mc`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 30613 · id 131770

#### e Right Error - Z.M1.Right mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header, English=e1171 Engine Right · Text, English=Error, stop battery, wait one minute, restart. · Channel=Right Zapi Error Code
- Logique :
  - **Showing** = `alarm present`
  - **Hiding** = `Right Zapi Error Code = 0`
- Lit : `Right Zapi Error Code`, `alarm present`
- Utilisé par : `Emmergency Stop - Z.M1.Right`
- Ligne export : 30625 · id 131771

#### PDO2_TX  `IMAC`
- Logique :
  - **Controlling** = `0x280 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 30680 · id 131780

#### GFIN PDO2_TX  `GFIN`
- Propriétés : Identifier=PDO2_TX · Data length=8 · Timeout=3000 · Paged protocol={Not used} · Parameters={{Right Zapi Warning; 0}; {Motor Temp; 16}; {Heatsink; 24}; {BDI Percentage; 32}; {Batterie Current [A]; 40}; {Batterie Voltage; 48}} · Module=Zapi_M_Track (Generic) · Module index=0
- Lit : `BDI Percentage`, `Batterie Current`, `Batterie Voltage`, `Heatsink`, `Motor Temp`, `PDO2_TX`, `Right Zapi Warning`
- Utilisé par : *(personne)*
- Ligne export : 30723 · id 131788

#### Right Zapi Warning  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `New Warning Code - Z.M1.Right`, `Right Warning - Z.M1.Right`, `Warning 1 - MEM - Z.M1.Right`, `e Right Warning - Z.M1.Right mc`, `Event log: Electronic logs`, `Measure group: Track Zapi Right`
- Ligne export : 30757 · id 131789

#### e Right Warning - Z.M1.Right mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header, English=e1159 Engine Right · Text, English=Error, stop battery, wait one minute, restart. · Channel=Right Zapi Warning
- Logique :
  - **Showing** = `Right Zapi Warning`
- Lit : `Right Zapi Warning`
- Utilisé par : `Emmergency Stop - Z.M1.Right`
- Ligne export : 30770 · id 131790

#### Error mode - Z.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(alarm present) OR (Emmergency Stop - Z.M1.Right)`
- Lit : `Emmergency Stop - Z.M1.Right`, `alarm present`
- Utilisé par : `Error Wait`, `M1 - Error mode`, `Measure group: Track Zapi Right`
- Ligne export : 30816 · id 131798

#### Error Wait  `IDC`
- Propriétés : Toggle=No · Delay on=4000 · Delay off=0
- Logique :
  - **Activating** = `Error mode - Z.M1.Right`
- Lit : `Error mode - Z.M1.Right`
- Utilisé par : `Emmergency Stop - Z.M1.Right`, `Reset`
- Ligne export : 30866 · id 131807

#### Emmergency Stop - Z.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Emmergency Stop - Z.M1.Right) OR (PositiveFlank(e Right Warning - Z.M1.Right mc)) OR (PositiveFlank(e Right Error - Z.M1.Right mc)) OR (PositiveFlank(Emmergency Stop Left))`
  - **Blocking** = `(NegativeFlank(VARIATOR SUPER ON E mc)) OR (PositiveFlank(Error Wait))`
- Lit : `Emmergency Stop Left`, `Error Wait`, `VARIATOR SUPER ON E mc`, `e Right Error - Z.M1.Right mc`, `e Right Warning - Z.M1.Right mc`
- Utilisé par : `Brake`, `Emmergency Stop Left`, `Enable`, `Error mode - Z.M1.Right`, `Measure group: Track Zapi Right`
- Ligne export : 30909 · id 131815

#### Enable  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed_Right [rpm] <> 0) OR (em Enable Power Zapi)`
  - **Blocking** = `Emmergency Stop - Z.M1.Right`
- Lit : `Emmergency Stop - Z.M1.Right`, `Speed_Right`, `em Enable Power Zapi`
- Utilisé par : `Brake`, `Power`
- Ligne export : 30992 · id 131828

#### PDO1_TX  `IMAC`
- Logique :
  - **Controlling** = `0x180 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 31051 · id 131838

#### GFIN PDO1_TX  `GFIN`
- Propriétés : Identifier=PDO1_TX · Data length=8 · Timeout=3000 · Paged protocol={Not used} · Parameters={{Actual_Speed [Hz/10]; 0}; {Out MNC; 16}; {Stuffing; 31}; {Actual Current [A*5]; 56}; {Status Byte; 32}} · Module=Zapi_M_Track (Generic) · Module index=1
- Lit : `Actual Current`, `Actual_Speed`, `Out MNC`, `PDO1_TX`, `Status Byte`, `Stuffing`
- Utilisé par : `CAN OK - Z.M1.Right`
- Ligne export : 31094 · id 131846

#### Actual Current  `GPIN`
- Propriétés : Unit=A*5 · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `Actual_current - Z.M1.Right`, `GFIN PDO1_TX`
- Ligne export : 31125 · id 131847

#### Actual_current - Z.M1.Right  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result := Actual Current * 5
  ```
- Lit : `Actual Current`
- Utilisé par : `M1 - CURRENT`, `Torque - Z.M1.Right`, `Measure group: Track Zapi Right`
- Ligne export : 31137 · id 131848

#### Target_Speed_can  `MAC`
- Propriétés : Unit=Hz/10
- Logique :
  ```qcode
  Result := abs(Speed_Right) * 5 / 6
  ```
- Lit : `Speed_Right`
- Utilisé par : `Target_SPeed`, `Measure group: Track Zapi Right`
- Ligne export : 31155 · id 131858

#### Target_SPeed  `GPOUT`
- Propriétés : Input value=Target_Speed_can [Hz/10] · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Target_Speed_can`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 31173 · id 131870

#### Actual_Speed  `GPIN`
- Propriétés : Unit=Hz/10 · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Actual_speed - Z.M1.Right`, `GFIN PDO1_TX`, `RUN - Z.M1.Right`
- Ligne export : 31185 · id 131871

#### Power  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `Enable`
- Lit : `Enable`
- Utilisé par : `Enable Power`, `Forward`, `Reverse`, `Adjust group: Master Features`
- Ligne export : 31198 · id 131872

#### Forward  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed_Right [rpm] >= 0) OR (em Enable Power Zapi)`
  - **Blocking** = `not(Power)`
- Lit : `Power`, `Speed_Right`, `em Enable Power Zapi`
- Utilisé par : `Forward Req`, `Adjust group: Setup Speed`
- Ligne export : 31241 · id 131880

#### Reverse  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Speed_Right [rpm] < 0`
  - **Blocking** = `not(Power)`
- Lit : `Power`, `Speed_Right`
- Utilisé par : `Reverse Req`
- Ligne export : 31301 · id 131890

#### Enable Power  `GPOUT`
- Propriétés : Input value=Power · Length=1 bit · Type=Unsigned integer
- Lit : `Power`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 31354 · id 131899

#### Forward Req  `GPOUT`
- Propriétés : Input value=Forward · Length=1 bit · Type=Unsigned integer
- Lit : `Forward`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 31365 · id 131900

#### Reverse Req  `GPOUT`
- Propriétés : Input value=Reverse · Length=1 bit · Type=Unsigned integer
- Lit : `Reverse`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 31376 · id 131901

#### GFOUT - PDO1_RX  `GFOUT`
- Propriétés : Identifier=PDO1_RX · Data length=8 · Send method=Continuously · Transmit rate=40 · Unused bits=Set to 0 · Parameters={{Target_SPeed [Hz/10]; 0}; {Enable Power; 16}; {Forward Req; 19}; {Reverse Req; 20}; {Stuffing; 31}; {Power Line; 17}; {Brake; 27}} · Module=Zapi_M_Track (Generic) · Module index=0
- Lit : `Brake`, `Enable Power`, `Forward Req`, `PDO1_RX`, `Power Line`, `Reverse Req`, `Stuffing`, `Target_SPeed`
- Utilisé par : `Stuffing`
- Ligne export : 31387 · id 131902

#### Stuffing  `IDC`
- Propriétés : Toggle=Yes · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank(GFOUT - PDO1_RX)`
- Lit : `GFOUT - PDO1_RX`
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`, `Stuffing`
- Ligne export : 31424 · id 131903

#### Stuffing  `GPOUT`
- Propriétés : Input value=Stuffing · Length=1 bit · Type=Unsigned integer
- Lit : `Stuffing`
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`
- Ligne export : 31468 · id 131911

#### PDO1_RX  `IMAC`
- Logique :
  - **Controlling** = `0x200 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 31479 · id 131912

#### Power Line  `GPOUT`
- Propriétés : Input value=1 · Length=1 bit · Type=Unsigned integer
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 31522 · id 131920

#### Brake  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `Enable`
  - **Blocking** = `Emmergency Stop - Z.M1.Right`
- Lit : `Emmergency Stop - Z.M1.Right`, `Enable`
- Utilisé par : `Brake`, `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 31533 · id 131921

#### Brake  `GPOUT`
- Propriétés : Input value=Brake · Length=1 bit · Type=Unsigned integer
- Lit : `Brake`
- Utilisé par : `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 31583 · id 131930

#### Motor Temp  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Motor_Temp - Z.M1.Right`
- Ligne export : 31594 · id 131931

#### Heatsink  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Heatsink - Z.M1.Right`
- Ligne export : 31606 · id 131932

#### BDI Percentage  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 31618 · id 131933

#### Batterie Current  `GPIN`
- Propriétés : Unit=A · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `Batterie Current - Z.M1.Right`, `GFIN PDO2_TX`
- Ligne export : 31630 · id 131934

#### Batterie Voltage  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Batterie Voltage - Z.M1.Right`, `GFIN PDO2_TX`
- Ligne export : 31642 · id 131935

#### Out MNC  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 31655 · id 131936

#### Stuffing  `GPIN`
- Propriétés : Length=1 bit · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`, `Stuffing`
- Ligne export : 31667 · id 131937

#### VARIATOR ON Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR SUPER ON E mc`
- Lit : `VARIATOR SUPER ON E mc`
- Utilisé par : `Func State`
- Ligne export : 31679 · id 131938

#### Reset  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(Error Wait)`
- Lit : `Error Wait`
- Utilisé par : `Confirmation`, `Func State`, `Adjust group: Maintenance`, `Adjust group: Master Config`
- Ligne export : 31722 · id 131946

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
- Ligne export : 31766 · id 131954

#### Func  `IP`
- Propriétés : Mode selector=Func State · Default mode: Stop={2} · Mode 1: Start={1} · Mode 2: Preprop={0x80} · Mode 3: Reset={0x81}
- Lit : `Func State`
- Utilisé par : `Func ID`
- Ligne export : 31868 · id 131970

#### Func ID  `GPOUT`
- Propriétés : Input value=Func · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Func`
- Utilisé par : `NMT`
- Ligne export : 31886 · id 131971

#### NMT  `GFOUT`
- Propriétés : Identifier=0 · Data length=8 · Send method=Continuously · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{Func ID; 0}; {Node ID; 8}} · Module=Zapi_M_Track (Generic) · Module index=1
- Lit : `Func ID`, `Node ID`
- Utilisé par : *(personne)*
- Ligne export : 31897 · id 131972

#### HeartBeat  `IMAC`
- Logique :
  - **Controlling** = `0x700 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN HeartBeat`
- Ligne export : 31919 · id 131973

#### GFIN HeartBeat  `GFIN`
- Propriétés : Identifier=HeartBeat · Data length=1 · Timeout=1000 · Paged protocol={Not used} · Parameters={{HeartBeat State; 0}} · Module=Zapi_M_Track (Generic) · Module index=2
- Lit : `HeartBeat`, `HeartBeat State`
- Utilisé par : *(personne)*
- Ligne export : 31962 · id 131981

#### HeartBeat State  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN HeartBeat`, `READY - Z.M1.Right`
- Ligne export : 31981 · id 131982

#### CAN OK - Z.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `GFIN PDO1_TX`
- Lit : `GFIN PDO1_TX`
- Utilisé par : `M1 - CAN OK`, `Measure group: Track Zapi Right`
- Ligne export : 31993 · id 131983

#### Batterie Voltage - Z.M1.Right  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `Batterie Voltage / 3,3333`
- Lit : `Batterie Voltage`
- Utilisé par : `M1 - Voltage`, `Measure group: Track Zapi Right`
- Ligne export : 32036 · id 131991

#### Batterie Current - Z.M1.Right  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Batterie Current [A] * 2`
- Lit : `Batterie Current`
- Utilisé par : `Measure group: Track Zapi Right`
- Ligne export : 32080 · id 131999

#### Motor_Temp - Z.M1.Right  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Motor Temp - 40`
- Lit : `Motor Temp`
- Utilisé par : `M1 - KTY`, `Measure group: Track Zapi Right`
- Ligne export : 32124 · id 132007

#### Heatsink - Z.M1.Right  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Heatsink`
- Lit : `Heatsink`
- Utilisé par : `M1 - Heatsink`, `Measure group: Track Zapi Right`
- Ligne export : 32168 · id 132015

#### Actual_speed - Z.M1.Right  `MAC`
- Propriétés : Unit=rpm
- Logique :
  ```qcode
  Result := Actual_Speed * 6 / 5
  ```
- Lit : `Actual_Speed`
- Utilisé par : `M1 - Speed`, `Measure group: Track Zapi Right`
- Ligne export : 32210 · id 132023

#### Zapi alarm code  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 32228 · id 132034

#### flag alarm  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 32240 · id 132035

#### extra info alarm  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 32252 · id 132036

#### READY - Z.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `HeartBeat State`
- Lit : `HeartBeat State`
- Utilisé par : `Measure group: Track Zapi Right`
- Ligne export : 32264 · id 132037

#### RUN - Z.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Actual_Speed [Hz/10] <> 0`
- Lit : `Actual_Speed`
- Utilisé par : `M1 - RUN`, `Measure group: Track Zapi Right`
- Ligne export : 32307 · id 132045

#### Warning 1 - MEM - Z.M1.Right  `MEM`
- Propriétés : Input channel=Right Zapi Warning · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(New Warning Code - Z.M1.Right)`
- Lit : `New Warning Code - Z.M1.Right`, `Right Zapi Warning`
- Utilisé par : `New Warning Code - Z.M1.Right`
- Ligne export : 32352 · id 132053

#### New Warning Code - Z.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Right Zapi Warning <> Warning 1 - MEM - Z.M1.Right`
  - **Blocking** = `Right Zapi Warning = 0`
- Lit : `Right Zapi Warning`, `Warning 1 - MEM - Z.M1.Right`
- Utilisé par : `Warning 1 - MEM - Z.M1.Right`, `Event log: Electronic logs`
- Ligne export : 32397 · id 132061

#### Error 1 - MEM - Z.M1.Right  `MEM`
- Propriétés : Input channel=Right Zapi Error Code · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(New Error Code - Z.M1.Right)`
- Lit : `New Error Code - Z.M1.Right`, `Right Zapi Error Code`
- Utilisé par : `New Error Code - Z.M1.Right`
- Ligne export : 32451 · id 132070

#### New Error Code - Z.M1.Right  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Right Zapi Error Code <> Error 1 - MEM - Z.M1.Right`
  - **Blocking** = `Right Zapi Error Code = 0`
- Lit : `Error 1 - MEM - Z.M1.Right`, `Right Zapi Error Code`
- Utilisé par : `Error 1 - MEM - Z.M1.Right`
- Ligne export : 32496 · id 132078

#### Status Byte  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 32550 · id 132087

#### Right Warning - Z.M1.Right  `GPOUT`
- Propriétés : Input value=Right Zapi Warning · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Right Zapi Warning`
- Utilisé par : *(personne)*
- Ligne export : 32562 · id 132088

#### Left Warning - Z.M2.Left  `GPOUT`
- Propriétés : Input value=Left Zapi Warning · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Left Zapi Warning`
- Utilisé par : *(personne)*
- Ligne export : 32574 · id 132089

#### Torque - Z.M1.Right  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `26 * courbe(((0,8 * Actual_current - Z.M1.Right [A]) / 33): {{0; 0}; {1; 1}; {2; 1,8}; {2,5; 2,18}; {3; 2,45}; {3,5; 2,62}; {4; 2,75}}, Freeze)`
- Lit : `Actual_current - Z.M1.Right`
- Utilisé par : `M1 - Torque`
- Ligne export : 32586 · id 132091

## mc.Electric / E.MOTORS / E.M-Tracks / E.Zapi.M2.Left.gen — actif seulement si `Is_MT_Zapi`

#### Speed_CAN_Left zapi  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Filter Left [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Filter Left`
- Utilisé par : `Speed_Left`
- Ligne export : 32792 · id 132113

#### Speed_Left  `MAC`
- Propriétés : Unit=rpm
- Logique :
  ```qcode
  Result := Speed_CAN_Left zapi * 30 * -1
  ```
- Lit : `Speed_CAN_Left zapi`
- Utilisé par : `Enable`, `Forward`, `Reverse`, `Target_speed_can`
- Ligne export : 32806 · id 132114

#### Node_ID  `IP`
- Propriétés : Mode selector=em ZAPI Node · Default mode: 8-10={10} · Mode 1: 1-4={4} · Mode 2: 4-8={8}
- Lit : `em ZAPI Node`
- Utilisé par : `EMERG`, `HeartBeat`, `Node ID`, `PDO1_RX`, `PDO1_TX`, `PDO2_TX`
- Ligne export : 32824 · id 132125

#### EMERG  `IMAC`
- Logique :
  - **Controlling** = `0x80 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 32840 · id 132126

#### GFIN PDO2_TX  `GFIN`
- Propriétés : Identifier=EMERG · Data length=Dont care · Paged protocol={Not used} · Parameters={{Left Zapi Error Code; 0}; {alarm present; 16}; {Zapi alarm code; 24}; {flag alarm; 32}; {extra info alarm; 40}} · Module=Zapi_M_Track (Generic) · Module index=4
- Lit : `EMERG`, `Left Zapi Error Code`, `Zapi alarm code`, `alarm present`, `extra info alarm`, `flag alarm`
- Utilisé par : *(personne)*
- Ligne export : 32883 · id 132134

#### Left Zapi Error Code  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `Error 2 - MEM`, `GFIN PDO2_TX`, `M2 - Zapi - New Error Code`, `e Left Error mc`, `Event log: Electronic logs`, `Measure group: Track Zapi Left`
- Ligne export : 32914 · id 132135

#### alarm present  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M2_Error mode`, `e Left Error mc`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 32927 · id 132136

#### e Left Error mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header, English=e1194 Engine Left · Text, English=Error, stop battery, wait one minute, restart. · Channel=Left Zapi Error Code
- Logique :
  - **Showing** = `alarm present`
  - **Hiding** = `Left Zapi Error Code = 0`
- Lit : `Left Zapi Error Code`, `alarm present`
- Utilisé par : `Emmergency Stop Left`
- Ligne export : 32939 · id 132137

#### PDO2_TX  `IMAC`
- Logique :
  - **Controlling** = `0x280 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 32994 · id 132146

#### GFIN PDO2_TX  `GFIN`
- Propriétés : Identifier=PDO2_TX · Data length=8 · Timeout=3000 · Paged protocol={Not used} · Parameters={{Left Zapi Warning; 0}; {Motor Temp; 16}; {Heatsink; 24}; {BDI Percentage; 32}; {Batterie Current [A]; 40}; {Batterie Voltage; 48}} · Module=Zapi_M_Track (Generic) · Module index=6
- Lit : `BDI Percentage`, `Batterie Current`, `Batterie Voltage`, `Heatsink`, `Left Zapi Warning`, `Motor Temp`, `PDO2_TX`
- Utilisé par : *(personne)*
- Ligne export : 33037 · id 132154

#### Left Zapi Warning  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Left Warning - Z.M2.Left`, `M2 - ZAPI - New Warning Code`, `Warning 2 - MEM`, `e Left Warning mc`, `Event log: Electronic logs`, `Measure group: Track Zapi Left`
- Ligne export : 33071 · id 132155

#### e Left Warning mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header, English=e1194 Engine Left · Text, English=Error, stop battery, wait one minute, restart. · Channel=Left Zapi Warning
- Logique :
  - **Showing** = `Left Zapi Warning`
- Lit : `Left Zapi Warning`
- Utilisé par : `Emmergency Stop Left`
- Ligne export : 33084 · id 132156

#### Error Wait  `IDC`
- Propriétés : Toggle=No · Delay on=4000 · Delay off=0
- Logique :
  - **Activating** = `ZAPI_M2_Error mode`
- Lit : `ZAPI_M2_Error mode`
- Utilisé par : `Emmergency Stop Left`, `Reset`
- Ligne export : 33130 · id 132164

#### Emmergency Stop Left  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Emmergency Stop Left) OR (PositiveFlank(e Left Warning mc)) OR (PositiveFlank(e Left Error mc)) OR (PositiveFlank(Emmergency Stop - Z.M1.Right))`
  - **Blocking** = `(NegativeFlank(VARIATOR SUPER ON E mc)) OR (PositiveFlank(Error Wait))`
- Lit : `Emmergency Stop - Z.M1.Right`, `Error Wait`, `VARIATOR SUPER ON E mc`, `e Left Error mc`, `e Left Warning mc`
- Utilisé par : `Brake`, `Emmergency Stop - Z.M1.Right`, `Enable`, `ZAPI_M2_Error mode`, `Measure group: Track Zapi Left`
- Ligne export : 33173 · id 132172

#### ZAPI_M2_Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(alarm present) OR (Emmergency Stop Left)`
- Lit : `Emmergency Stop Left`, `alarm present`
- Utilisé par : `Error Wait`, `M2 - Error mode`, `ZAPI_M2_READY`, `Measure group: Track Zapi Left`
- Ligne export : 33256 · id 132185

#### Enable  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `(Speed_Left [rpm] <> 0) OR (em Enable Power Zapi)`
  - **Blocking** = `Emmergency Stop Left`
- Lit : `Emmergency Stop Left`, `Speed_Left`, `em Enable Power Zapi`
- Utilisé par : `Brake`, `Power`
- Ligne export : 33306 · id 132194

#### Target_speed_can  `MAC`
- Propriétés : Unit=Hz/10
- Logique :
  ```qcode
  Result := abs(Speed_Left)  * 5 / 6
  ```
- Lit : `Speed_Left`
- Utilisé par : `Target SPeed`, `Measure group: Track Zapi Left`
- Ligne export : 33365 · id 132204

#### PDO1_TX  `IMAC`
- Logique :
  - **Controlling** = `0x180 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 33383 · id 132216

#### GFIN PDO1_TX  `GFIN`
- Propriétés : Identifier=PDO1_TX · Data length=8 · Timeout=3000 · Paged protocol={Not used} · Parameters={{Actual_Speed [Hz/10]; 0}; {Out MNC; 16}; {Stuffing; 31}; {Actual Current [A*5]; 56}; {Status Byte; 32}} · Module=Zapi_M_Track (Generic) · Module index=7
- Lit : `Actual Current`, `Actual_Speed`, `Out MNC`, `PDO1_TX`, `Status Byte`, `Stuffing`
- Utilisé par : `ZAPI_M2_CAN OK`
- Ligne export : 33426 · id 132224

#### Actual_Speed  `GPIN`
- Propriétés : Unit=Hz/10 · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `ZAPI_M2_Actual_speed`, `ZAPI_M2_RUN`
- Ligne export : 33457 · id 132225

#### Target SPeed  `GPOUT`
- Propriétés : Input value=Target_speed_can [Hz/10] · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Target_speed_can`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 33470 · id 132226

#### Power  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `Enable`
- Lit : `Enable`
- Utilisé par : `Enable Power`, `Forward`, `Reverse`, `Adjust group: Master Features`
- Ligne export : 33482 · id 132227

#### Forward  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Speed_Left [rpm] >= 0) OR (em Enable Power Zapi)`
  - **Blocking** = `not(Power)`
- Lit : `Power`, `Speed_Left`, `em Enable Power Zapi`
- Utilisé par : `Forward Req`, `Adjust group: Setup Speed`
- Ligne export : 33525 · id 132235

#### Reverse  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Speed_Left [rpm] < 0`
  - **Blocking** = `not(Power)`
- Lit : `Power`, `Speed_Left`
- Utilisé par : `Reverse Req`
- Ligne export : 33585 · id 132245

#### Enable Power  `GPOUT`
- Propriétés : Input value=Power · Length=1 bit · Type=Unsigned integer
- Lit : `Power`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 33638 · id 132254

#### Forward Req  `GPOUT`
- Propriétés : Input value=Forward · Length=1 bit · Type=Unsigned integer
- Lit : `Forward`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 33649 · id 132255

#### Reverse Req  `GPOUT`
- Propriétés : Input value=Reverse · Length=1 bit · Type=Unsigned integer
- Lit : `Reverse`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 33660 · id 132256

#### Brake  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `Enable`
  - **Blocking** = `Emmergency Stop Left`
- Lit : `Emmergency Stop Left`, `Enable`
- Utilisé par : `Brake`, `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 33671 · id 132257

#### Brake  `GPOUT`
- Propriétés : Input value=Brake · Length=1 bit · Type=Unsigned integer
- Lit : `Brake`
- Utilisé par : `GFOUT - PDO1_RX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 33721 · id 132266

#### Stuffing  `IDC`
- Propriétés : Toggle=Yes · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank(GFOUT - PDO1_RX)`
- Lit : `GFOUT - PDO1_RX`
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`, `Stuffing`
- Ligne export : 33732 · id 132267

#### Stuffing  `GPOUT`
- Propriétés : Input value=Stuffing · Length=1 bit · Type=Unsigned integer
- Lit : `Stuffing`
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`
- Ligne export : 33776 · id 132275

#### PDO1_RX  `IMAC`
- Logique :
  - **Controlling** = `0x200 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 33787 · id 132276

#### Power Line  `GPOUT`
- Propriétés : Input value=1 · Length=1 bit · Type=Unsigned integer
- Utilisé par : `GFOUT - PDO1_RX`
- Ligne export : 33830 · id 132284

#### GFOUT - PDO1_RX  `GFOUT`
- Propriétés : Identifier=PDO1_RX · Data length=8 · Send method=Continuously · Transmit rate=40 · Unused bits=Set to 0 · Parameters={{Target SPeed [Hz/10]; 0}; {Enable Power; 16}; {Forward Req; 19}; {Reverse Req; 20}; {Stuffing; 31}; {Power Line; 17}; {Brake; 27}} · Module=Zapi_M_Track (Generic) · Module index=3
- Lit : `Brake`, `Enable Power`, `Forward Req`, `PDO1_RX`, `Power Line`, `Reverse Req`, `Stuffing`, `Target SPeed`
- Utilisé par : `Stuffing`
- Ligne export : 33841 · id 132285

#### Motor Temp  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M2_Motor_Temp`
- Ligne export : 33878 · id 132286

#### Heatsink  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M2_Heatsink`
- Ligne export : 33890 · id 132287

#### BDI Percentage  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`
- Ligne export : 33902 · id 132288

#### Batterie Current  `GPIN`
- Propriétés : Unit=A · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M2_Batterie Current`
- Ligne export : 33914 · id 132289

#### Batterie Voltage  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `ZAPI_M2_Batterie Voltage`
- Ligne export : 33926 · id 132290

#### Out MNC  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 33939 · id 132291

#### Stuffing  `GPIN`
- Propriétés : Length=1 bit · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `GFOUT - PDO1_RX`, `Stuffing`
- Ligne export : 33951 · id 132292

#### VARIATOR ON Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `VARIATOR SUPER ON E mc`
- Lit : `VARIATOR SUPER ON E mc`
- Utilisé par : `Func State`
- Ligne export : 33963 · id 132293

#### Reset ZAPI state  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Reset`, `Adjust group: Master Electric`, `Single adjust item: Reset ZAPI state`
- Ligne export : 34006 · id 132301

#### Reset  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `(Reset ZAPI state) OR (PositiveFlank(Error Wait))`
- Lit : `Error Wait`, `Reset ZAPI state`
- Utilisé par : `Confirmation`, `Func State`, `Adjust group: Maintenance`, `Adjust group: Master Config`
- Ligne export : 34019 · id 132302

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
- Ligne export : 34070 · id 132311

#### Func  `IP`
- Propriétés : Mode selector=Func State · Default mode: Stop={2} · Mode 1: Start={1} · Mode 2: Preprop={0x80} · Mode 3: Reset={0x81}
- Lit : `Func State`
- Utilisé par : `Func ID`
- Ligne export : 34172 · id 132327

#### Func ID  `GPOUT`
- Propriétés : Input value=Func · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Func`
- Utilisé par : `NMT`
- Ligne export : 34190 · id 132328

#### Node ID  `GPOUT`
- Propriétés : Input value=Node_ID · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Node_ID`
- Utilisé par : `NMT`
- Ligne export : 34201 · id 132329

#### NMT  `GFOUT`
- Propriétés : Identifier=0 · Data length=8 · Send method=Continuously · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{Func ID; 0}; {Node ID; 8}} · Module=Zapi_M_Track (Generic) · Module index=2
- Lit : `Func ID`, `Node ID`
- Utilisé par : *(personne)*
- Ligne export : 34212 · id 132330

#### HeartBeat  `IMAC`
- Logique :
  - **Controlling** = `0x700 + Node_ID`
- Lit : `Node_ID`
- Utilisé par : `GFIN HeartBeat`
- Ligne export : 34234 · id 132331

#### GFIN HeartBeat  `GFIN`
- Propriétés : Identifier=HeartBeat · Data length=1 · Timeout=1000 · Paged protocol={Not used} · Parameters={{HeartBeat State; 0}} · Module=Zapi_M_Track (Generic) · Module index=5
- Lit : `HeartBeat`, `HeartBeat State`
- Utilisé par : *(personne)*
- Ligne export : 34277 · id 132339

#### HeartBeat State  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN HeartBeat`, `ZAPI_M2_READY`
- Ligne export : 34296 · id 132340

#### ZAPI_M2_CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `GFIN PDO1_TX`
- Lit : `GFIN PDO1_TX`
- Utilisé par : `M2 - CAN OK`, `Measure group: Track Zapi Left`
- Ligne export : 34308 · id 132341

#### ZAPI_M2_Batterie Voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `Batterie Voltage / 3,3333`
- Lit : `Batterie Voltage`
- Utilisé par : `M2 - Voltage`, `Measure group: Track Zapi Left`
- Ligne export : 34351 · id 132349

#### ZAPI_M2_Batterie Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `Batterie Current [A] * 2`
- Lit : `Batterie Current`
- Utilisé par : `Measure group: Track Zapi Left`
- Ligne export : 34395 · id 132357

#### ZAPI_M2_Motor_Temp  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Motor Temp - 40`
- Lit : `Motor Temp`
- Utilisé par : `M2 - KTY`, `Measure group: Track Zapi Left`
- Ligne export : 34439 · id 132365

#### ZAPI_M2_Heatsink  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `Heatsink`
- Lit : `Heatsink`
- Utilisé par : `M2 - Heatsink`, `Measure group: Track Zapi Left`
- Ligne export : 34483 · id 132373

#### ZAPI_M2_Actual_speed  `MAC`
- Propriétés : Unit=rpm
- Logique :
  ```qcode
  Result := Actual_Speed * 6 / 5
  ```
- Lit : `Actual_Speed`
- Utilisé par : `M2 - Speed`, `Measure group: Track Zapi Left`
- Ligne export : 34525 · id 132381

#### Actual Current  `GPIN`
- Propriétés : Unit=A*5 · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`, `ZAPI_M2_Actual_current`
- Ligne export : 34543 · id 132392

#### ZAPI_M2_Actual_current  `MAC`
- Propriétés : Unit=A
- Logique :
  ```qcode
  Result := Actual Current * 5
  ```
- Lit : `Actual Current`
- Utilisé par : `M2 - CURRENT`, `ZAPI_M2_Torque`, `Measure group: Track Zapi Left`
- Ligne export : 34555 · id 132393

#### Zapi alarm code  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 34573 · id 132403

#### flag alarm  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 34585 · id 132404

#### extra info alarm  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN PDO2_TX`, `Measure group: Track Zapi Left`, `Measure group: Track Zapi Right`
- Ligne export : 34597 · id 132405

#### ZAPI_M2_READY  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `HeartBeat State`
  - **Blocking** = `ZAPI_M2_Error mode`
- Lit : `HeartBeat State`, `ZAPI_M2_Error mode`
- Utilisé par : `M2 - Ready`
- Ligne export : 34609 · id 132406

#### ZAPI_M2_RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Actual_Speed [Hz/10] <> 0`
- Lit : `Actual_Speed`
- Utilisé par : `M2 - RUN`, `Measure group: Track Zapi Left`
- Ligne export : 34659 · id 132415

#### Warning 2 - MEM  `MEM`
- Propriétés : Input channel=Left Zapi Warning · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M2 - ZAPI - New Warning Code)`
- Lit : `Left Zapi Warning`, `M2 - ZAPI - New Warning Code`
- Utilisé par : `M2 - ZAPI - New Warning Code`
- Ligne export : 34704 · id 132423

#### M2 - ZAPI - New Warning Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Left Zapi Warning <> Warning 2 - MEM`
  - **Blocking** = `Left Zapi Warning = 0`
- Lit : `Left Zapi Warning`, `Warning 2 - MEM`
- Utilisé par : `Warning 2 - MEM`
- Ligne export : 34749 · id 132431

#### Error 2 - MEM  `MEM`
- Propriétés : Input channel=Left Zapi Error Code · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M2 - Zapi - New Error Code)`
- Lit : `Left Zapi Error Code`, `M2 - Zapi - New Error Code`
- Utilisé par : `M2 - Zapi - New Error Code`
- Ligne export : 34803 · id 132440

#### M2 - Zapi - New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Left Zapi Error Code <> Error 2 - MEM`
  - **Blocking** = `Left Zapi Error Code = 0`
- Lit : `Error 2 - MEM`, `Left Zapi Error Code`
- Utilisé par : `Error 2 - MEM`
- Ligne export : 34848 · id 132448

#### Status Byte  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `GFIN PDO1_TX`
- Ligne export : 34902 · id 132457

#### ZAPI_M2_Torque  `MAC`
- Propriétés : Unit=Nm · Limiting object group=Signed
- Logique :
  - **Controlling** = `26 * courbe(((0,8 * ZAPI_M2_Actual_current [A]) / 33): {{0; 0}; {1; 1}; {2; 1,8}; {2,5; 2,18}; {3; 2,45}; {3,5; 2,62}; {4; 2,75}}, Freeze)`
- Lit : `ZAPI_M2_Actual_current`
- Utilisé par : `M2 - Torque`
- Ligne export : 34914 · id 132458

## mc.Electric / E.MOTORS / E.M3-Hydrau — actif seulement si `VARIATOR SUPER ON E mc`

#### Oil Not Good  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Wait_Very_Low_Oil_Level`
- Lit : `Wait_Very_Low_Oil_Level`
- Utilisé par : `Oil not Good`, `Oil not Good gen`
- Ligne export : 40244 · id 133326

#### Speed Hydro Force  `IP`
- Propriétés : Default mode={0}
- Utilisé par : `M3_Speed`, `Adjust group: Master Features`, `Single adjust item: Speed Hydro Force`
- Ligne export : 40287 · id 133334

#### M3_Speed  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxOf (Absolute)(Engine hydro Speed E [rpm], Speed Hydro Force)`
- Lit : `Engine hydro Speed E`, `Speed Hydro Force`
- Utilisé par : `M3_speed`, `Speed gen`
- Ligne export : 40299 · id 133335

#### Is_M3_Sevcon_gen  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `em M-Pump - Brand = 0`
- Lit : `em M-Pump - Brand`
- Utilisé par : `Active le groupe: mc.Electric / E.MOTORS / E.M3-Hydrau / broeknE.Sevcon.M3.gen.soon`
- Ligne export : 40348 · id 133345

#### M3 - Heatsink  `MAC`
- Propriétés : Unit=*C · Limiting object group=Signed · Function selector=em M-Pump - Brand
- Fonction *Sevcon gen* :
  - **Controlling** = `genHeatsink [°C]`
- Fonction *Sevcon j19* :
  - **Controlling** = `insideHeatsink [°C]`
- Lit : `em M-Pump - Brand`, `genHeatsink`, `insideHeatsink`
- Utilisé par : `M3 - NEED TO FAN`, `M3 - NEED TO PUMP`, `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 40393 · id 133565

#### HVLP Fan Temp  `IP`
> Difference between hotest temp allowed and current temp
- Propriétés : Default mode={40}
- Utilisé par : `M3 - NEED TO FAN`
- Ligne export : 40466 · id 133657

#### M3 - NEED TO FAN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M3 - Heatsink [*C] <= HVLP Fan Temp`
- Lit : `HVLP Fan Temp`, `M3 - Heatsink`
- Utilisé par : `NEED FAN`
- Ligne export : 40478 · id 133573

#### HVLP Pump Temp  `IP`
> Difference between hotest temp allowed and current temp
- Propriétés : Default mode={50}
- Utilisé par : `M3 - NEED TO PUMP`
- Ligne export : 40523 · id 133658

#### M3 - NEED TO PUMP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M3 - Heatsink [*C] <= HVLP Pump Temp`
- Lit : `HVLP Pump Temp`, `M3 - Heatsink`
- Utilisé par : `NEED PUMP`
- Ligne export : 40535 · id 133581

#### M3 - Engine Temps  `MAC`
- Propriétés : Unit=*C · Limiting object group=Signed · Function selector=em M-Pump - Brand
- Fonction *Sevcon gen* :
  - **Controlling** = `genSevcon - Engine Temp [°C]`
- Fonction *Sevcon j19* :
  - **Controlling** = `Sevcon - Engine Temp [°C]`
- Lit : `Sevcon - Engine Temp`, `em M-Pump - Brand`, `genSevcon - Engine Temp`
- Utilisé par : `M3 - Charge`, `M3 - ENGINE HOT`, `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 40580 · id 133589

#### M3 - ENGINE HOT  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `M3 - Engine Temps [*C] >= em Engine Eco Temp [°C]`
- Lit : `M3 - Engine Temps`, `em Engine Eco Temp`
- Utilisé par : `Event log: Electronic logs`
- Ligne export : 40653 · id 133597

#### M3 - Voltage  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed · Function selector=em M-Pump - Brand
- Fonction *Sevcon gen* :
  - **Controlling** = `gen M3 Voltage [V]`
- Fonction *Sevcon j19* :
  - **Controlling** = `j19 M3 Voltage [V]`
- Lit : `em M-Pump - Brand`, `gen M3 Voltage`, `j19 M3 Voltage`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`
- Ligne export : 40698 · id 133605

#### M3 - Run  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em M-Pump - Brand
- Fonction *Sevcon gen* :
  - **Activating** = `gen - M3 - RUN`
- Fonction *Sevcon j19* :
  - **Activating** = `j19 M3 - RUN`
- Lit : `em M-Pump - Brand`, `gen - M3 - RUN`, `j19 M3 - RUN`
- Utilisé par : `IDC Tension`, `Statistics log: Electronic Stats logs`
- Ligne export : 40771 · id 133613

#### M3 - Charge  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `((MaxOf((M3 - Engine Temps [*C] - 40), 0)) / (em Engine Max Temp [°C] - 40)) * 100`
- Lit : `M3 - Engine Temps`, `em Engine Max Temp`
- Utilisé par : *(personne)*
- Ligne export : 40845 · id 133621

#### M3 - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em M-Pump - Brand
- Fonction *Sevcon gen* :
  - **Activating** = `gen - CAN OK`
- Fonction *Sevcon j19* :
  - **Activating** = `j19 M3 CAN OK`
- Lit : `em M-Pump - Brand`, `gen - CAN OK`, `j19 M3 CAN OK`
- Utilisé par : `MD4-10 page: INFO`, `MD4-5 page: INFO`, `Measure group: Canbus`
- Ligne export : 40925 · id 133633

#### M3 - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em M-Pump - Brand
- Fonction *Sevcon gen* :
  - **Activating** = `gen - Ready`
- Fonction *Sevcon j19* :
  - **Activating** = `j19 M3 Ready`
- Lit : `em M-Pump - Brand`, `gen - Ready`, `j19 M3 Ready`
- Utilisé par : *(personne)*
- Ligne export : 40999 · id 133641

#### M3 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=em M-Pump - Brand
- Fonction *Sevcon gen* :
  - **Activating** = `gen M3 - Error mode`
- Fonction *Sevcon j19* :
  - **Activating** = `Sevcon - Error mode`
- Lit : `Sevcon - Error mode`, `em M-Pump - Brand`, `gen M3 - Error mode`
- Utilisé par : `Engines Error`
- Ligne export : 41073 · id 133649

#### Is_M3_Sevcon_j19  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `em M-Pump - Brand = 1`
- Lit : `em M-Pump - Brand`
- Utilisé par : `Active le groupe: mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19`
- Ligne export : 42331 · id 169856

## mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19 — actif seulement si `Is_M3_Sevcon_j19`

#### JFIN-A:J1939[113]  `JFIN`
- Propriétés : Priority=Dont care · PGN=71936 · Destination address (DA)=255 · Timeout=500 · Paged protocol={Not used} · Multipacket=No · Parameters={{Status Word; 33}; {Limit Word; 41}} · Module=Inverter_HVLP_j19 (J1939[113]) · Module index=0
- Lit : `Limit Word`, `Status Word`
- Utilisé par : *(personne)*
- Ligne export : 42400 · id 229251

#### Status Word  `JPIN`
- Propriétés : Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `JFIN-A:J1939[113]`, `Status Word o`, `Status Word o250`, `j19 M3 Ready`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 42425 · id 170081

#### Limit Word  `JPIN`
- Propriétés : Length=1 Byte (= 8 bits) · J1939 Error check=Yes · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `JFIN-A:J1939[113]`
- Ligne export : 42439 · id 170082

#### Test Mode  `SMC`
- Propriétés : Default state name=Normal
- Fonction *Test* : (vide)
- Utilisé par : `Speed`
- Ligne export : 42453 · id 170083

#### HVLP Speed Test  `IP`
- Propriétés : Default mode={-100}
- Utilisé par : `Speed`
- Ligne export : 42486 · id 170090

#### M3_speed  `FGI`
- Propriétés : Input type=Real · Input=M3_Speed · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `M3_Speed`
- Utilisé par : `Speed`
- Ligne export : 42498 · id 170091

#### Speed  `IMAC`
- Propriétés : Function selector=Test Mode
- Fonction *Normal* :
  - **Controlling** = `Abs(M3_speed)`
- Fonction *Test* :
  - **Controlling** = `HVLP Speed Test`
- Lit : `HVLP Speed Test`, `M3_speed`, `Test Mode`
- Utilisé par : `Speed Slope`, `Speed_compute`, `T Speed Error Calcul`, `TSC1-A:J1939-0 EB2 T45`, `TSC1-A:J1939-0 Ford T45`, `TSC1-A:J1939-0 Kubo T45`, `Adjust group: Master Config`, `Adjust group: Master Thermic`, `Adjust group: Master Thermic Pumps`, `Adjust group: Setup Speed`
- Ligne export : 42512 · id 170092

#### Speed Slope  `SFC`
- Propriétés : Input channel=Speed · Enable=Yes · Type=Slopes · Slopes={{3000; 3000}; {3000; 3000}}
- Lit : `Speed`
- Utilisé par : `ON/OFF Var`
- Ligne export : 42585 · id 170107

#### JFIN-B:J1939[113]  `JFIN`
- Propriétés : Priority=Dont care · PGN=71680 · Destination address (DA)=255 · Timeout=500 · Paged protocol={Not used} · Multipacket=No · Parameters={{Motor_Speed_Raw; 17}; {Torque_Mesured_Raw; 1}} · Module=Inverter_HVLP_j19 (J1939[113]) · Module index=1
- Lit : `Motor_Speed_Raw`, `Torque_Mesured_Raw`
- Utilisé par : `j19 M3 CAN OK`
- Ligne export : 42603 · id 229252

#### j19 M3 CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `JFIN-B:J1939[113]`
- Lit : `JFIN-B:J1939[113]`
- Utilisé par : `M3 - CAN OK`
- Ligne export : 42628 · id 170109

#### Motor_Speed_Raw  `JPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · J1939 Error check=No · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `JFIN-B:J1939[113]`, `Motor Speed`, `j19 M3 - RUN`
- Ligne export : 42671 · id 170117

#### j19 M3 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `(Abs(Motor_Speed_Raw)) > 1800`
- Lit : `Motor_Speed_Raw`
- Utilisé par : `M3 - Run`
- Ligne export : 42685 · id 170118

#### j19 M3 Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Status Word = 7) OR (Status Word = 8)`
- Lit : `Status Word`
- Utilisé par : `M3 - Ready`
- Ligne export : 42738 · id 170127

#### Oil not Good  `FGI`
- Propriétés : Input type=Digital · Input=Oil Not Good · Default state name=Default state
- Lit : `Oil Not Good`
- Utilisé par : `ON/OFF Var`
- Ligne export : 42792 · id 170136

#### ON/OFF Var  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `(Speed Slope <> 0) AND (VARIATOR SUPER ON E mc)`
  - **Blocking** = `Oil not Good`
- Lit : `Oil not Good`, `Speed Slope`, `VARIATOR SUPER ON E mc`
- Utilisé par : `Variator State`
- Ligne export : 42803 · id 170137

#### Variator State  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ON* :
  - **Activating** = `ON/OFF Var`
- Lit : `ON/OFF Var`
- Utilisé par : `Status Word`
- Ligne export : 42862 · id 170147

#### Status Word  `IP`
- Propriétés : Mode selector=Variator State · Default mode: OFF={3} · Mode 1: ON={5}
- Lit : `Variator State`
- Utilisé par : `JFIN-A:J1939[113]`, `Status Word o`, `Status Word o250`, `j19 M3 Ready`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 42902 · id 170155

#### JFIN-C:J1939[113]  `JFIN`
- Propriétés : Priority=Dont care · PGN=72192 · Destination address (DA)=255 · Timeout=500 · Paged protocol={Not used} · Multipacket=No · Parameters={{Input Voltage; 33}; {insideHeatsink [°C]; 1}; {Sevcon - Engine Temp [°C]; 17}} · Module=Inverter_HVLP_j19 (J1939[113]) · Module index=2
- Lit : `Input Voltage`, `Sevcon - Engine Temp`, `insideHeatsink`
- Utilisé par : *(personne)*
- Ligne export : 42916 · id 229253

#### Input Voltage  `JPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · J1939 Error check=No · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `JFIN-C:J1939[113]`, `j19 M3 Voltage`, `Measure group: Charger Elcon`
- Ligne export : 42944 · id 170157

#### j19 M3 Voltage  `IMAC`
- Propriétés : Unit=V
- Logique :
  - **Controlling** = `Input Voltage * 0,0625`
- Lit : `Input Voltage`
- Utilisé par : `M3 - Voltage`
- Ligne export : 42958 · id 170158

#### Torque_Mesured_Raw  `JPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · J1939 Error check=No · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `JFIN-B:J1939[113]`, `Torque actual`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 43001 · id 170166

#### JFIN-D:J1939[113]  `JFIN`
- Propriétés : Priority=Dont care · PGN=72448 · Destination address (DA)=255 · Timeout=3000 · Paged protocol={Not used} · Multipacket=No · Parameters={{M3 (Pump) - Error; 1}} · Module=Inverter_HVLP_j19 (J1939[113]) · Module index=3
- Lit : `M3 (Pump) - Error`
- Utilisé par : *(personne)*
- Ligne export : 43015 · id 229254

#### M3 (Pump) - Error  `JPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · J1939 Error check=Yes · Resolution=1 · Offset=0 · Error value=0
- Utilisé par : `Error 3 - MEM`, `JFIN-D:J1939[113]`, `M3  (Pump) - Filter`, `M3 - New Error Code`, `Sevcon - Error mode`, `Event log: Electronic logs`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 43037 · id 170168

#### M3  (Pump) - Filter  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(M3 (Pump) - Error = 0) OR (M3 (Pump) - Error = 17862)`
- Lit : `M3 (Pump) - Error`
- Utilisé par : `M3 - New Error Code`, `Sevcon - Error mode`
- Ligne export : 43051 · id 170169

#### M3 - New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M3 (Pump) - Error <> Error 3 - MEM`
  - **Blocking** = `M3  (Pump) - Filter`
- Lit : `Error 3 - MEM`, `M3  (Pump) - Filter`, `M3 (Pump) - Error`
- Utilisé par : `Error 3 - MEM`, `Event log: Electronic logs`
- Ligne export : 43105 · id 170178

#### Error 3 - MEM  `MEM`
- Propriétés : Input channel=M3 (Pump) - Error · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(M3 - New Error Code)`
- Lit : `M3 (Pump) - Error`, `M3 - New Error Code`
- Utilisé par : `M3 - New Error Code`, `e M3 - Pump Engine CMSG mc`
- Ligne export : 43157 · id 170187

#### e M3 - Pump Engine CMSG mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header, English=e1168 Pump Engine · Text, English=Error, stop battery, wait one minute, restart. · Channel=Error 3 - MEM
- Lit : `Error 3 - MEM`
- Utilisé par : *(personne)*
- Ligne export : 43202 · id 170195

#### Sevcon - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M3 (Pump) - Error`
  - **Blocking** = `M3  (Pump) - Filter`
- Lit : `M3  (Pump) - Filter`, `M3 (Pump) - Error`
- Utilisé par : `M3 - Error mode`
- Ligne export : 43241 · id 170202

#### Status Word o250  `JPOUT`
- Propriétés : Input value=Status Word · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Lit : `Status Word`
- Utilisé par : `JFOUT-A:J1939[250]`
- Ligne export : 43291 · id 170211

#### Torque Demande o250  `JPOUT`
- Propriétés : Input value=0xFD80 · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-A:J1939[250]`
- Ligne export : 43303 · id 170212

#### Torque Limit o250  `JPOUT`
- Propriétés : Input value=640 · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-A:J1939[250]`
- Ligne export : 43315 · id 170213

#### Fw Speed Limit  `JPOUT`
- Propriétés : Input value=3000 · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-B:J1939[113]`
- Ligne export : 43327 · id 170215

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
- Ligne export : 43339 · id 170216

#### Rw Speed Limit  `JPOUT`
- Propriétés : Input value=Speed_compute · Length=16 · Resolution=1 · Offset=0
- Lit : `Speed_compute`
- Utilisé par : `JFOUT-B:J1939[113]`
- Ligne export : 43361 · id 170232

#### I Batt Discharge Limit  `JPOUT`
- Propriétés : Input value=50 · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-C:J1939[250]`
- Ligne export : 43373 · id 170234

#### I Batt recharge limit  `JPOUT`
- Propriétés : Input value=0xFFCE · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-C:J1939[250]`
- Ligne export : 43385 · id 170235

#### Status Word o  `JPOUT`
- Propriétés : Input value=Status Word · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Lit : `Status Word`
- Utilisé par : `JFOUT-A:J1939[113]`
- Ligne export : 43397 · id 170237

#### Torque Demande o  `JPOUT`
- Propriétés : Input value=0xFD80 · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-A:J1939[113]`
- Ligne export : 43409 · id 170238

#### Torque Limit o  `JPOUT`
- Propriétés : Input value=640 · Length=2 Bytes (= 16 bits) · Resolution=1 · Offset=0
- Utilisé par : `JFOUT-A:J1939[113]`
- Ligne export : 43421 · id 170239

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
- Utilisé par : *(personne)*
- Ligne export : 43433 · id 170241

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
- Utilisé par : *(personne)*
- Ligne export : 43458 · id 170263

#### Sevcon - Engine Temp  `GPIN`
- Propriétés : Unit=°C · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `JFIN-C:J1939[113]`, `M3 - Engine Temps`
- Ligne export : 43483 · id 170289

#### insideHeatsink  `GPIN`
- Propriétés : Unit=°C · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `JFIN-C:J1939[113]`, `M3 - Heatsink`
- Ligne export : 43496 · id 170290

#### JFOUT-A:J1939[250]  `JFOUT`
- Propriétés : J1939 source address=250 · Priority=6 · PGN=69632 · Destination address (DA)=113 · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Multipacket=No · Parameters={{Status Word o250 [bits]; 17}; {Torque Demande o250 [bits]; 1}; {Torque Limit o250 [bits]; 33}} · Module=Inverter_HVLP_j19 (J1939[113]) · Module index=2
- Lit : `Status Word o250`, `Torque Demande o250`, `Torque Limit o250`
- Utilisé par : *(personne)*
- Ligne export : 43509 · id 229256

#### JFOUT-B:J1939[113]  `JFOUT`
- Propriétés : J1939 source address=250 · Priority=6 · PGN=69888 · Destination address (DA)=113 · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Multipacket=No · Parameters={{Fw Speed Limit [bits]; 17}; {Rw Speed Limit [bits]; 33}} · Module=Inverter_HVLP_j19 (J1939[113]) · Module index=3
- Lit : `Fw Speed Limit`, `Rw Speed Limit`
- Utilisé par : *(personne)*
- Ligne export : 43538 · id 229257

#### JFOUT-C:J1939[250]  `JFOUT`
- Propriétés : J1939 source address=250 · Priority=6 · PGN=70144 · Destination address (DA)=113 · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Multipacket=No · Parameters={{I Batt Discharge Limit [bits]; 1}; {I Batt recharge limit [bits]; 17}} · Module=Inverter_HVLP_j19 (J1939[113]) · Module index=1
- Lit : `I Batt Discharge Limit`, `I Batt recharge limit`
- Utilisé par : *(personne)*
- Ligne export : 43564 · id 229258

#### JFOUT-A:J1939[113]  `JFOUT`
- Propriétés : J1939 source address=113 · Priority=6 · PGN=69632 · Destination address (DA)=113 · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Multipacket=No · Parameters={{Status Word o [bits]; 17}; {Torque Demande o [bits]; 1}; {Torque Limit o [bits]; 33}} · Module=Inverter_HVLP_j19 (J1939[113]) · Module index=0
- Lit : `Status Word o`, `Torque Demande o`, `Torque Limit o`
- Utilisé par : *(personne)*
- Ligne export : 43590 · id 229259

## mc.Electric / E.MOTORS / E.M3-Hydrau / broeknE.Sevcon.M3.gen.soon — actif seulement si `Is_M3_Sevcon_gen`

#### Speed gen  `FGI`
- Propriétés : Input type=Real · Input=M3_Speed · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `M3_Speed`
- Utilisé par : `Speed`
- Ligne export : 41172 · id 154819

#### Oil not Good gen  `FGI`
- Propriétés : Input type=Digital · Input=Oil Not Good · Default state name=Default state
- Lit : `Oil Not Good`
- Utilisé par : `ON/OFF Var gen`
- Ligne export : 41186 · id 154820

#### Test Mode  `SMC`
- Propriétés : Default state name=Normal
- Fonction *Test* : (vide)
- Utilisé par : `Speed`
- Ligne export : 41197 · id 154821

#### HVLP Speed Test  `IP`
- Propriétés : Default mode={-100}
- Utilisé par : `Speed`
- Ligne export : 41230 · id 154829

#### Speed  `IMAC`
- Propriétés : Function selector=Test Mode
- Fonction *Normal* :
  - **Controlling** = `Speed gen`
- Fonction *Test* :
  - **Controlling** = `HVLP Speed Test`
- Lit : `HVLP Speed Test`, `Speed gen`, `Test Mode`
- Utilisé par : `Speed Slope`, `Speed_compute`, `T Speed Error Calcul`, `TSC1-A:J1939-0 EB2 T45`, `TSC1-A:J1939-0 Ford T45`, `TSC1-A:J1939-0 Kubo T45`, `Adjust group: Master Config`, `Adjust group: Master Thermic`, `Adjust group: Master Thermic Pumps`, `Adjust group: Setup Speed`
- Ligne export : 41242 · id 154830

#### Speed Slope  `SFC`
- Propriétés : Input channel=Speed · Enable=Yes · Type=Slopes · Slopes={{3000; 3000}; {3000; 3000}}
- Lit : `Speed`
- Utilisé par : `ON/OFF Var gen`
- Ligne export : 41314 · id 154845

#### ON/OFF Var gen  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `(Speed Slope <> 0) AND (VARIATOR SUPER ON E mc)`
  - **Blocking** = `Oil not Good gen`
- Lit : `Oil not Good gen`, `Speed Slope`, `VARIATOR SUPER ON E mc`
- Utilisé par : `Variator State`
- Ligne export : 41332 · id 154846

#### 0x191AFF71  `GFIN`
- Propriétés : Identifier=0x191AFF71 · Data length=Dont care · Timeout=500 · Paged protocol={Not used} · Parameters={{Input Voltage; 32}; {genHeatsink [°C]; 0}; {genSevcon - Engine Temp [°C]; 16}} · Module=Sev_M3_HVLP_soon (Generic) · Module index=1
- Lit : `Input Voltage`, `genHeatsink`, `genSevcon - Engine Temp`
- Utilisé par : *(personne)*
- Ligne export : 41391 · id 154856

#### genSevcon - Engine Temp  `GPIN`
- Propriétés : Unit=°C · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x191AFF71`, `M3 - Engine Temps`
- Ligne export : 41416 · id 154857

#### 0x1918FF71  `GFIN`
- Propriétés : Identifier=0x1918FF71 · Data length=Dont care · Timeout=500 · Paged protocol={Not used} · Parameters={{Motor_Speed_Raw [rpm]; 16}; {Torque_Mesured_Raw; 0}} · Module=Sev_M3_HVLP_soon (Generic) · Module index=0
- Lit : `Motor_Speed_Raw`, `Torque_Mesured_Raw`
- Utilisé par : *(personne)*
- Ligne export : 41429 · id 154858

#### gen - CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `0x1918FF71`
- Utilisé par : `M3 - CAN OK`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 41451 · id 154859

#### Motor_Speed_Raw  `GPIN`
- Propriétés : Unit=rpm · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x1918FF71`, `Motor Speed M3`, `gen - M3 - RUN`
- Ligne export : 41494 · id 154867

#### gen - M3 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `(Abs(Motor_Speed_Raw [rpm])) > 1800`
- Lit : `Motor_Speed_Raw`
- Utilisé par : `M3 - Run`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 41507 · id 154869

#### 0x1919FF71  `GFIN`
- Propriétés : Identifier=0x1919FF71 · Data length=Dont care · Timeout=500 · Paged protocol={Not used} · Parameters={{Status Word; 32}; {Limit Word; 40}} · Module=Sev_M3_HVLP_soon (Generic) · Module index=2
- Lit : `Limit Word`, `Status Word`
- Utilisé par : *(personne)*
- Ligne export : 41560 · id 154878

#### Status Word  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `0x191071FA`, `0x1919FF71`, `Status Word`, `gen - Ready`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 41582 · id 154879

#### gen - Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Status Word = 7) OR (Status Word = 8)`
- Lit : `Status Word`
- Utilisé par : `M3 - Ready`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 41594 · id 154880

#### Variator State  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ON* :
  - **Activating** = `ON/OFF Var gen`
- Lit : `ON/OFF Var gen`
- Utilisé par : `Status Word`
- Ligne export : 41648 · id 154889

#### Status Word  `IP`
- Propriétés : Mode selector=Variator State · Default mode: OFF={3} · Mode 1: ON={5}
- Lit : `Variator State`
- Utilisé par : `0x191071FA`, `0x1919FF71`, `Status Word`, `gen - Ready`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 41688 · id 154897

#### Status Word  `GPOUT`
- Propriétés : Input value=Status Word · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Status Word`
- Utilisé par : `0x191071FA`, `0x1919FF71`, `gen - Ready`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 41702 · id 154898

#### Torque Demande  `GPOUT`
- Propriétés : Input value=-496 · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Utilisé par : `0x191071FA`
- Ligne export : 41714 · id 154899

#### Torque Limit  `GPOUT`
- Propriétés : Input value=496 · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Utilisé par : `0x191071FA`
- Ligne export : 41726 · id 154900

#### 0x191071FA  `GFOUT`
- Propriétés : Identifier=0x191071FA · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Parameters={{Status Word; 16}; {Torque Demande; 0}; {Torque Limit; 32}} · Module=Sev_M3_HVLP_soon (Generic) · Module index=0
- Lit : `Status Word`, `Torque Demande`, `Torque Limit`
- Utilisé par : *(personne)*
- Ligne export : 41738 · id 154901

#### Fw Speed Limit  `GPOUT`
- Propriétés : Input value=3000 · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Utilisé par : `0x191171FA`
- Ligne export : 41763 · id 154902

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
- Utilisé par : `Speed_compute_neg`
- Ligne export : 41775 · id 167146

#### Speed_compute_neg  `IMAC`
- Logique :
  ```qcode
  Result := -Speed_compute
  ```
- Lit : `Speed_compute`
- Utilisé par : `Rw Speed Limit`
- Ligne export : 41797 · id 171429

#### Rw Speed Limit  `GPOUT`
- Propriétés : Input value=Speed_compute_neg · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Lit : `Speed_compute_neg`
- Utilisé par : `0x191171FA`
- Ligne export : 41815 · id 154903

#### 0x191171FA  `GFOUT`
- Propriétés : Identifier=0x191171FA · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Parameters={{Fw Speed Limit; 16}; {Rw Speed Limit; 32}} · Module=Sev_M3_HVLP_soon (Generic) · Module index=1
- Lit : `Fw Speed Limit`, `Rw Speed Limit`
- Utilisé par : *(personne)*
- Ligne export : 41827 · id 154904

#### I Batt Discharge Limit  `GPOUT`
- Propriétés : Input value=50 · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Utilisé par : `0x191271FA`
- Ligne export : 41849 · id 154905

#### I Batt recharge limit  `GPOUT`
- Propriétés : Input value=-50 · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Utilisé par : `0x191271FA`
- Ligne export : 41861 · id 154906

#### 0x191271FA  `GFOUT`
- Propriétés : Identifier=0x191271FA · Data length=8 · Send method=Continuously · Transmit rate=200 · Unused bits=Set to 0 · Parameters={{I Batt Discharge Limit; 0}; {I Batt recharge limit; 16}} · Module=Sev_M3_HVLP_soon (Generic) · Module index=2
- Lit : `I Batt Discharge Limit`, `I Batt recharge limit`
- Utilisé par : *(personne)*
- Ligne export : 41873 · id 154907

#### Limit Word  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `0x1919FF71`
- Ligne export : 41895 · id 154908

#### Torque_Mesured_Raw  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x1918FF71`, `Torque actual gen`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 41907 · id 154909

#### Input Voltage  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x191AFF71`, `gen M3 Voltage`, `Measure group: Charger Elcon`
- Ligne export : 41920 · id 154910

#### 0x191BFF71  `GFIN`
- Propriétés : Identifier=0x191BFF71 · Data length=Dont care · Timeout=3000 · Paged protocol={Not used} · Parameters={{M3 (Pump) - Error; 0}} · Module=Sev_M3_HVLP_soon (Generic) · Module index=3
- Lit : `M3 (Pump) - Error`
- Utilisé par : *(personne)*
- Ligne export : 41933 · id 154911

#### M3 (Pump) - Error  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x191BFF71`, `M3  (Pump) - Filter`, `gen M3 - Error mode`, `gen M3 New Error Code`, `genError 3 - MEM`, `Event log: Electronic logs`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 41952 · id 154912

#### gen M3 Voltage  `IMAC`
- Propriétés : Unit=V
- Logique :
  - **Controlling** = `Input Voltage * 0,0625`
- Lit : `Input Voltage`
- Utilisé par : `M3 - Voltage`, `Measure group: Pump Sevcon HVLP`
- Ligne export : 41965 · id 154913

#### Torque actual gen  `IMAC`
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
- Utilisé par : `Measure group: Pump Sevcon HVLP`
- Ligne export : 42008 · id 154921

#### genHeatsink  `GPIN`
- Propriétés : Unit=°C · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `0x191AFF71`, `M3 - Heatsink`
- Ligne export : 42034 · id 154929

#### M3  (Pump) - Filter  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(M3 (Pump) - Error = 0) OR (M3 (Pump) - Error = 17862)`
- Lit : `M3 (Pump) - Error`
- Utilisé par : `gen M3 - Error mode`, `gen M3 New Error Code`
- Ligne export : 42047 · id 154938

#### gen M3 New Error Code  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M3 (Pump) - Error <> genError 3 - MEM`
  - **Blocking** = `M3  (Pump) - Filter`
- Lit : `M3  (Pump) - Filter`, `M3 (Pump) - Error`, `genError 3 - MEM`
- Utilisé par : `e gen M3 - Pump Engine CMSG mc`, `genError 3 - MEM`
- Ligne export : 42101 · id 154947

#### genError 3 - MEM  `MEM`
- Propriétés : Input channel=M3 (Pump) - Error · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank(gen M3 New Error Code)`
- Lit : `M3 (Pump) - Error`, `gen M3 New Error Code`
- Utilisé par : `e gen M3 - Pump Engine CMSG mc`, `gen M3 New Error Code`
- Ligne export : 42153 · id 154956

#### e gen M3 - Pump Engine CMSG mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header, English=e1028 Hydraulics · Text, English=Hydraulic pump Motor Error. Stop battery, wait one minute and restart. If the problem persists, contact a service center. · Channel=genError 3 - MEM
- Logique :
  - **Showing** = `gen M3 New Error Code`
- Lit : `gen M3 New Error Code`, `genError 3 - MEM`
- Utilisé par : *(personne)*
- Ligne export : 42198 · id 154964

#### gen M3 - Error mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `M3 (Pump) - Error`
  - **Blocking** = `M3  (Pump) - Filter`
- Lit : `M3  (Pump) - Filter`, `M3 (Pump) - Error`
- Utilisé par : `M3 - Error mode`
- Ligne export : 42244 · id 154972

#### Motor Speed M3  `IMAC`
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
- Utilisé par : `Measure group: Pump Sevcon HVLP`
- Ligne export : 42294 · id 171321

## mc.Electric / E.Track Up/Down

#### UP E  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `UP/DOWN Button 4ET = 1`
- Lit : `UP/DOWN Button 4ET`
- Utilisé par : `E Don'push button`, `E lock`, `Inter EV UP Delay`, `Inter EV tendre Chenille E`
- Ligne export : 44919 · id 171368

#### Inter EV UP Delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `UP E`
- Lit : `UP E`
- Utilisé par : `Inter EV UP`, `Inter EV Verin E`
- Ligne export : 44964 · id 128328

#### DOWN E  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `UP/DOWN Button 4ET = 2`
- Lit : `UP/DOWN Button 4ET`
- Utilisé par : `E Don'push button`, `Inter EV DOWN delay`, `Inter EV tendre Chenille E`
- Ligne export : 45007 · id 171387

#### Inter EV DOWN delay  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `DOWN E`
- Lit : `DOWN E`
- Utilisé par : `Inter EV DOWN`, `Inter EV Verin E`
- Ligne export : 45052 · id 128344

#### e Locking UP Track  `DP`
- Propriétés : True text=ACTIVE · False text=NO ACTIVE · Default mode={True}
- Utilisé par : `E lock`, `Single adjust item: Locking UP Track`
- Ligne export : 45095 · id 128352

#### e Landing Block Number  `SP`
- Propriétés : Input channel=None · Default state name=One · States={Two}
- Utilisé par : `e Landing time bloking`, `Single adjust item: Landing Block Number`
- Ligne export : 45108 · id 128571

#### e Landing time bloking  `IP`
- Propriétés : Unit=ms · Mode selector=e Landing Block Number · Default mode: One={1000} · Mode 1: Two={2500}
- Lit : `e Landing Block Number`
- Utilisé par : `Locking Phase Duration`
- Ligne export : 45120 · id 128353

#### e EV Bloc delay  `IP`
- Propriétés : Unit=ms · Default mode={0}
- Utilisé par : `E EV Lock`, `Locking Phase Duration`, `Single adjust item: EV Bloc delay`
- Ligne export : 45134 · id 128354

#### Locking Phase Duration  `IMAC`
- Propriétés : Unit=ms
- Logique :
  - **Controlling** = `e Landing time bloking [ms] + e EV Bloc delay [ms]`
- Lit : `e EV Bloc delay`, `e Landing time bloking`
- Utilisé par : `E lock`
- Ligne export : 45146 · id 128355

#### State Up/Down Raw  `IMAC`
- Logique :
  - **Controlling** = `Screen_State Up/Down mc`
- Lit : `Screen_State Up/Down mc`
- Utilisé par : `E State Up/Down`, `E lock`
- Ligne export : 45189 · id 128483

#### E lock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=Locking Phase Duration [ms]
- Logique :
  - **Activating** = `(State Up/Down Raw >= 100) AND (NegativeFlank(UP E))`
  - **Blocking** = `not(e Locking UP Track)`
- Lit : `Locking Phase Duration`, `State Up/Down Raw`, `UP E`, `e Locking UP Track`
- Utilisé par : `E EV Lock`, `E unlock`, `HIGH`, `LOW`
- Ligne export : 45230 · id 128363

#### Inter EV Verin E  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP Delay) OR (Inter EV DOWN delay)`
- Lit : `Inter EV DOWN delay`, `Inter EV UP Delay`
- Utilisé par : `E Super Ok tension`, `E unlock`
- Ligne export : 45291 · id 128373

#### E unlock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter EV Verin E`
  - **Blocking** = `E lock`
- Lit : `E lock`, `Inter EV Verin E`
- Utilisé par : `E EV UnBlock`
- Ligne export : 45341 · id 128382

#### e Force tension  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Inter EV tendre Chenille E`
- Ligne export : 45391 · id 128391

#### e With tension  `DP`
> permet d'empecher la tension chenille (si sur False)
- Propriétés : Default mode={True}
- Utilisé par : `Inter EV tendre Chenille E`, `Single adjust item: With tension`
- Ligne export : 45404 · id 128392

#### Inter EV tendre Chenille E  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(E Super Ok tension) OR (e Force tension)`
  - **Blocking** = `(UP E) OR (DOWN E) OR (not(e With tension))`
- Lit : `DOWN E`, `E Super Ok tension`, `UP E`, `e Force tension`, `e With tension`
- Utilisé par : `HIGH`, `IDC Tension`
- Ligne export : 45417 · id 128393

#### IDC Tension  `IDC`
> delay to try solve pb overrun hydro pump
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `(M3 - Run and Inter EV tendre Chenille E) OR (E Untingthen)`
- Lit : `E Untingthen`, `Inter EV tendre Chenille E`, `M3 - Run`
- Utilisé par : `E EV Tension`, `E Inter EV By Pass`
- Ligne export : 45489 · id 128405

#### E OK UP/DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `Locking pressure mc 9 [bar] <= 10`
- Lit : `Locking pressure mc 9`
- Utilisé par : `Inter EV DOWN`, `Inter EV UP`, `OK UP/DOWN Sel`
- Ligne export : 45541 · id 128417

#### Inter EV UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV UP Delay) AND (E OK UP/DOWN)`
- Lit : `E OK UP/DOWN`, `Inter EV UP Delay`
- Utilisé par : `E EV Up`, `E Inter EV By Pass`, `HIGH`
- Ligne export : 45586 · id 128425

#### Inter EV DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV DOWN delay) AND (E OK UP/DOWN)`
- Lit : `E OK UP/DOWN`, `Inter EV DOWN delay`
- Utilisé par : `E EV Down`, `E Inter EV By Pass`, `HIGH`
- Ligne export : 45636 · id 128435

#### HIGH  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Inter EV tendre Chenille E) OR (Inter EV UP) OR (Inter EV DOWN)`
  - **Blocking** = `E lock`
- Lit : `E lock`, `Inter EV DOWN`, `Inter EV UP`, `Inter EV tendre Chenille E`
- Utilisé par : `E Inter EV By Pass`, `Engine hydro`, `LOW`
- Ligne export : 45686 · id 128445

#### LOW  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1500
- Logique :
  - **Activating** = `NegativeFlank(HIGH) OR (E lock)`
- Lit : `E lock`, `HIGH`
- Utilisé par : `E Inter EV By Pass`, `Engine hydro`
- Ligne export : 45750 · id 128456

#### e Force EV By Pass  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `E Inter EV By Pass`, `Single adjust item: Force EV By Pass`
- Ligne export : 45801 · id 128573

#### E Inter EV By Pass  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Inter EV DOWN) OR (Inter EV UP) OR (IDC Tension) OR (EV lock mc 59) OR HIGH OR LOW OR (e Force EV By Pass)`
  - **Blocking** = `E Untingthen and (not(e Force EV By Pass))`
- Lit : `E Untingthen`, `EV lock mc 59`, `HIGH`, `IDC Tension`, `Inter EV DOWN`, `Inter EV UP`, `LOW`, `e Force EV By Pass`
- Utilisé par : `E EV By pass`
- Ligne export : 45814 · id 128465

#### E Don'push button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `False`
  - **Blocking** = `(UP E) OR (DOWN E)`
- Lit : `DOWN E`, `UP E`
- Utilisé par : `E State Up/Down`
- Ligne export : 45916 · id 128491

#### OK BLOC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Locking pressure mc 9 [bar] >= 90`
- Lit : `Locking pressure mc 9`
- Utilisé par : `E State Up/Down`, `E&T OK BLOC`
- Ligne export : 45973 · id 128526

#### E State Up/Down  `SMC`
- Propriétés : Default state name=Error
- Fonction *DOWN* :
  - **Activating** = `((State Up/Down Raw < 2) and (State Up/Down Raw > 0)) OR (State Up/Down Raw = 0)`
  - **Blocking** = `E Don'push button`
- Fonction *INTERMEDIATE* :
  - **Activating** = `(State Up/Down Raw >= 2) AND (State Up/Down Raw <= 98)`
  - **Blocking** = `E Don'push button`
- Fonction *UP* :
  - **Activating** = `State Up/Down Raw > 98`
  - **Blocking** = `E Don'push button`
- Fonction *UP AND BLOC* :
  - **Activating** = `(State Up/Down Raw >= 99) AND (OK BLOC)`
  - **Blocking** = `E Don'push button`
- Lit : `E Don'push button`, `OK BLOC`, `State Up/Down Raw`
- Utilisé par : `Elec activ shema inter`, `Elec show schema UP`, `Elec show schema down`, `brokenVIEW ENGINE STATE`, `brokenVIEW TRACK STATE`, `e Up/DOWN STATE d3 Int`
- Ligne export : 46018 · id 128501

#### Engine hydro  `SMC`
- Propriétés : Default state name=OFF
- Fonction *LOW* :
  - **Activating** = `LOW`
  - **Blocking** = `HIGH`
- Fonction *HIGHT* :
  - **Activating** = `HIGH`
- Lit : `HIGH`, `LOW`
- Utilisé par : `Engine hydro Speed E`
- Ligne export : 46230 · id 128534

#### e LOW SPEED  `IP`
- Propriétés : Unit=rpm · Default mode={-2000}
- Utilisé par : `Engine hydro Speed E`, `Single adjust item: Low speed`
- Ligne export : 46308 · id 128547

#### e HIGH SPEED  `IP`
- Propriétés : Unit=rpm · Default mode={-3000}
- Utilisé par : `Engine hydro Speed E`, `Single adjust item: High speed`
- Ligne export : 46320 · id 128548

#### Engine hydro Speed E  `IMAC`
- Propriétés : Unit=rpm · Function selector=Engine hydro
- Fonction *OFF* :
  - **Controlling** = `0`
- Fonction *LOW* :
  - **Controlling** = `e LOW SPEED [rpm]`
- Fonction *HIGHT* :
  - **Controlling** = `e HIGH SPEED [rpm]`
- Lit : `Engine hydro`, `e HIGH SPEED`, `e LOW SPEED`
- Utilisé par : `M3_Speed`
- Ligne export : 46332 · id 128549

#### E EV Up  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter EV UP`
- Lit : `Inter EV UP`
- Utilisé par : `EV Up Sel`
- Ligne export : 46454 · id 204502

#### E EV Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter EV DOWN`
- Lit : `Inter EV DOWN`
- Utilisé par : `EV Down Sel`
- Ligne export : 46497 · id 204513

#### E EV By pass  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=300
- Logique :
  - **Activating** = `E Inter EV By Pass`
- Lit : `E Inter EV By Pass`
- Utilisé par : `EV By pass Sel`
- Ligne export : 46540 · id 204530

#### E EV Tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `IDC Tension`
- Lit : `IDC Tension`
- Utilisé par : `EV Tension Sel`
- Ligne export : 46583 · id 204547

#### E EV Lock  `IDC`
- Propriétés : Toggle=No · Delay on=e EV Bloc delay [ms] · Delay off=0
- Logique :
  - **Activating** = `E lock`
- Lit : `E lock`, `e EV Bloc delay`
- Utilisé par : `EV Lock Sel`
- Ligne export : 46626 · id 204564

#### E EV UnBlock  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `E unlock`
- Lit : `E unlock`
- Utilisé par : `EV UnBlock Sel`
- Ligne export : 46669 · id 204581

#### Elec show schema down  `IDC`
> s'active pour montrer le bon schéma sur le MD4
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `E State Up/Down = 1`
- Lit : `E State Up/Down`
- Utilisé par : `MD4-5 page: MAIN Elec`
- Ligne export : 46712 · id 240868

#### Elec activ shema inter  `IDC`
> s'active pour montrer le bon schéma sur le MD4
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `E State Up/Down = 2`
- Lit : `E State Up/Down`
- Utilisé par : `Timer clignotement schema inter`
- Ligne export : 46757 · id 240872

#### Elec show schema UP  `IDC`
> s'active pour montrer le bon schéma sur le MD4
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(E State Up/Down = 3) OR (E State Up/Down = 4)`
- Lit : `E State Up/Down`
- Utilisé par : `MD4-5 page: MAIN Elec`
- Ligne export : 46802 · id 240876

#### Timer clignotement schema inter  `TMR`
> permet de faire clignoter le shcéma intermédiaire
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Elec activ shema inter`
  - **Resetting** = `not(Elec activ shema inter)`
- Lit : `Elec activ shema inter`
- Utilisé par : `Elec show schema inter`
- Ligne export : 46856 · id 240880

#### Elec show schema inter  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Timer clignotement schema inter [s] mod 2) = 1`
- Lit : `Timer clignotement schema inter`
- Utilisé par : `MD4-5 page: MAIN Elec`
- Ligne export : 46916 · id 240885

## mc.Electric / E.Track tension

#### e Tracks pressure Mode  `SP`
> This channel is used to give unit and names to the MEM
- Propriétés : Input channel=None · Default state name=AUTO · States={UNTIGHTEN}
- Utilisé par : `E Untingthen`, `IDC Free E`, `ON/OFF/Untighed`, `Tension State`, `e Tracks pressure Mode`, `Single adjust item: Tracks pressure Mode`
- Ligne export : 48449 · id 128576

#### e Tracks pressure Mode  `MEM`
- Propriétés : Input channel=e Tracks pressure Mode · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : `Reset Startup`, `e Tracks pressure Mode`
- Utilisé par : `E Untingthen`, `IDC Free E`, `ON/OFF/Untighed`, `Tension State`, `Single adjust item: Tracks pressure Mode`
- Ligne export : 48461 · id 128587

#### Wait engine start  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `e System Started`
- Lit : `e System Started`
- Utilisé par : `ON/OFF/Untighed`, `Ok tension`, `Tension State`, `Wait engine Stop`
- Ligne export : 48504 · id 128595

#### ON/OFF/Untighed  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ON* :
  - **Activating** = `Wait engine start`
  - **Blocking** = `e Tracks pressure Mode`
- Fonction *UNTIGHTED* :
  - **Activating** = `e Tracks pressure Mode`
- Lit : `Wait engine start`, `e Tracks pressure Mode`
- Utilisé par : `E Super Ok tension`
- Ligne export : 48547 · id 128603

#### E Pression Filter  `SFC`
- Propriétés : Input channel=Track pressure mc 10 [bar] · Enable=Yes · Type=Slopes · Slopes={{50; 50}; {1; 1}}
- Lit : `Track pressure mc 10`
- Utilisé par : `Need Pressure`
- Ligne export : 48625 · id 128616

#### e Time to tension  `IP`
- Propriétés : Unit=ms · Default mode={150}
- Utilisé par : `E Super Ok tension`, `Single adjust item: Time to tension`
- Ligne export : 48643 · id 128617

#### Ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `PositiveFlank(Wait engine start)`
- Lit : `Wait engine start`
- Utilisé par : `E Super Ok tension`
- Ligne export : 48655 · id 128618

#### 10 minutes auto tender  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=10
- Logique :
  - **Decreasing** = `e System Started`
  - **Resetting** = `10 minutes auto tender [min] <= 0`
- Lit : `e System Started`
- Utilisé par : `E Super Ok tension`
- Ligne export : 48699 · id 128626

#### e Tension Pressure  `IP`
- Propriétés : Unit=bar · Default mode={160}
- Utilisé par : `E show symbole track bleu`, `Need Pressure`, `Single adjust item: Tension Pressure`
- Ligne export : 48760 · id 128637

#### Need Pressure  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `e Tension Pressure [bar] > E Pression Filter [bar]`
- Lit : `E Pression Filter`, `e Tension Pressure`
- Utilisé par : `E Super Ok tension`, `Adjust group: Master Thermic`
- Ligne export : 48772 · id 128638

#### e Tension Error Parameter  `FP`
- Propriétés : Unit=% · Default mode={100}
- Utilisé par : `Over Tension`, `Single adjust item: Tension Error Parameter`
- Ligne export : 48817 · id 128646

#### E Super Ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=e Time to tension [ms] · Function selector=ON/OFF/Untighed
- Fonction *OFF* :
  - **Blocking** = `True`
- Fonction *ON* :
  - **Activating** = `(NegativeFlank(Ok tension)) OR (10 minutes auto tender [min] = 0) OR (Need Pressure)`
  - **Blocking** = `(Over Tension) OR (Inter EV Verin E)`
- Fonction *UNTIGHTED* :
  - **Blocking** = `True`
- Lit : `10 minutes auto tender`, `Inter EV Verin E`, `Need Pressure`, `ON/OFF/Untighed`, `Ok tension`, `Over Tension`, `e Time to tension`
- Utilisé par : `Delay Off super ok tension`, `Inter EV tendre Chenille E`
- Ligne export : 48829 · id 128647

#### Delay Off super ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `E Super Ok tension`
- Lit : `E Super Ok tension`
- Utilisé par : `Super Ok Tension Math`
- Ligne export : 48965 · id 128673

#### Super Ok Tension Math  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `Delay Off super ok tension * 100`
- Lit : `Delay Off super ok tension`
- Utilisé par : `Slope Super Ok`
- Ligne export : 49008 · id 128681

#### Slope Super Ok  `SFC`
- Propriétés : Input channel=Super Ok Tension Math [%] · Enable=Yes · Type=Slopes · Slopes={{5; 1}; {2; 2}}
- Lit : `Super Ok Tension Math`
- Utilisé par : `Over Tension`
- Ligne export : 49051 · id 128689

#### Over Tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Over Tension) OR (Slope Super Ok [%] > e Tension Error Parameter [%])`
  - **Blocking** = `not(e System Started)`
- Lit : `Over Tension`, `Slope Super Ok`, `e System Started`, `e Tension Error Parameter`
- Utilisé par : `E Super Ok tension`, `Over Tension`, `e Track Tension Error mc`, `Event log: Electronic logs`, `Event log: Hydraulic Event`
- Ligne export : 49069 · id 128690

#### Wait engine Stop  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=4000
- Logique :
  - **Activating** = `Wait engine start`
- Lit : `Wait engine start`
- Utilisé par : `Tension State`
- Ligne export : 49129 · id 128700

#### Tension State  `SMC`
- Propriétés : Default state name=ON/OFF
- Fonction *Parking* :
  - **Activating** = `Wait engine Stop`
  - **Blocking** = `(Wait engine start) OR (e Tracks pressure Mode)`
- Fonction *Unthingten* :
  - **Activating** = `e Tracks pressure Mode`
- Lit : `Wait engine Stop`, `Wait engine start`, `e Tracks pressure Mode`
- Utilisé par : *(personne)*
- Ligne export : 49172 · id 128708

#### e Track Tension Error mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header, English=e1038 Track Tension Error · Text, English=Try a Calibrating (Setting/Maintenance). Use straight. Contact your service center. · Channel=Track pressure mc 10 [bar]
- Logique :
  - **Showing** = `Over Tension`
- Lit : `Over Tension`, `Track pressure mc 10`
- Utilisé par : *(personne)*
- Ligne export : 49257 · id 128722

#### E Untingthen  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `e Tracks pressure Mode`
- Lit : `e Tracks pressure Mode`
- Utilisé par : `E Inter EV By Pass`, `IDC Tension`
- Ligne export : 49303 · id 128730

#### E show symbole track bleu  `IDC`
> fait apparaitre le symbole track en bleu ou en rouge
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Track pressure mc 10 [bar] >= (e Tension Pressure [bar] - 10)`
  - **Blocking** = `Track pressure mc 10 [bar] < (e Tension Pressure [bar] - 10)`
- Lit : `Track pressure mc 10`, `e Tension Pressure`
- Utilisé par : `E&T Show symbole track white`
- Ligne export : 49346 · id 240646

## mc.Electric / E.Translate

#### e System Started  `IDC`
- Propriétés : Toggle=No · Delay on=750 · Delay off=500
- Logique :
  - **Activating** = `E Engines Ready`
- Lit : `E Engines Ready`
- Utilisé par : `10 minutes auto tender`, `Batt or engine started mc`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `Over Tension`, `Wait engine start`, `e State All Speed`
- Ligne export : 46986 · id 127962

#### E Speed Int  `IMAC`
- Logique :
  - **Controlling** = `Screen_Speed Input mc`
- Lit : `Screen_Speed Input mc`
- Utilisé par : `e Speed Mode`, `e Speed Pump`, `e State All Speed`
- Ligne export : 47029 · id 127971

#### e Speed Pump  `SMC`
- Propriétés : Default state name=Slow
- Fonction *Super Slow* :
  - **Activating** = `E Speed Int = 2`
  - **Blocking** = `E Speed Int = 1`
- Fonction *Fast Speed* :
  - **Activating** = `(E Speed Int = 3) OR (E Speed Int = 4) OR (E Speed Int = 5)`
  - **Blocking** = `E Speed Int = 1`
- Lit : `E Speed Int`
- Utilisé par : `brokenVIEW TRACK STATE`, `e Max Speed`, `e Start Slope`, `e Stop Slope`
- Ligne export : 47070 · id 127979

#### IDC Free E  `IDC`
> Activating : e Tracks pressure Mode or Screen_Free Input mc
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(e Tracks pressure Mode) OR (Screen_Free Input mc)`
- Lit : `Screen_Free Input mc`, `e Tracks pressure Mode`
- Utilisé par : `e Speed Mode`
- Ligne export : 47181 · id 127995

#### e Speed Mode  `SMC`
- Propriétés : Default state name=OFF
- Fonction *IDLE* :
  - **Activating** = `E Speed Int = 0`
- Fonction *Free* :
  - **Activating** = `(E Speed Int = 1) OR (E Speed Int = 2) OR (E Speed Int = 3)`
  - **Blocking** = `not(IDC Free E)`
- Fonction *UnFree* :
  - **Activating** = `(E Speed Int = 1) OR (E Speed Int = 2) OR (E Speed Int = 3)`
- Lit : `E Speed Int`, `IDC Free E`
- Utilisé par : `DMAC Table Left`, `DMAC Table Right`, `e Speed Mode Int`
- Ligne export : 47231 · id 128004

#### e Start Slope  `FP`
- Propriétés : Unit=%/s · Mode selector=e Speed Pump · Default mode: Slow={50} · Mode 1: Super Slow={50} · Mode 2: Fast Speed={30}
- Lit : `e Speed Pump`
- Utilisé par : `Filter Left`, `Filter Right`, `e Left Filter`, `e Right Filter`, `Single adjust item: Start Slope`
- Ligne export : 47383 · id 128033

#### e Stop Slope  `FP`
- Propriétés : Unit=%/s · Mode selector=e Speed Pump · Default mode: Slow={80} · Mode 1: Super Slow={80} · Mode 2: Fast Speed={80}
- Lit : `e Speed Pump`
- Utilisé par : `Filter Left`, `Filter Right`, `e Left Filter`, `e Right Filter`, `Single adjust item: Stop Slope`
- Ligne export : 47399 · id 128034

#### e Debug: Inhibit System Crash Signal  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `System Crash Signal`, `Single adjust item: Debug: Inhibit System Crash Signal`
- Ligne export : 47415 · id 128035

#### System Crash Signal  `IDC`
> Set to 0 if system has to manage a crash. Speed are then reduced to 0
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True`
  - **Blocking** = `(System Ask imminent Crash E mc) AND (not(e Debug: Inhibit System Crash Signal))`
- Lit : `System Ask imminent Crash E mc`, `e Debug: Inhibit System Crash Signal`
- Utilisé par : `DMAC Table Left`, `DMAC Table Right`, `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `Adjust group: Master System Debug`
- Ligne export : 47428 · id 128036

#### DMAC_EV_2_Left  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `(Math Gauche Left 45 [%] * e System Started) * System Crash Signal`
- Lit : `Math Gauche Left 45`, `System Crash Signal`, `e System Started`
- Utilisé par : `Cruise Left`, `Cruise Right`, `DMAC Table Left`, `Joystick to zero`, `Left unfree`, `Right unfree`
- Ligne export : 47486 · id 128046

#### DMAC_EV_1_Right  `DMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling +/-** = `(Math Droit Right 45 [%] * e System Started) * System Crash Signal`
- Lit : `Math Droit Right 45`, `System Crash Signal`, `e System Started`
- Utilisé par : `Cruise Left`, `Cruise Right`, `DMAC Table Right`, `Joystick to zero`, `Left unfree`, `Right unfree`
- Ligne export : 47547 · id 128057

#### Cruise Left  `LTC`
- Propriétés : Unit=% · Row selector=DMAC_EV_2_Left [%] · Column selector=DMAC_EV_1_Right [%] · Interpolation=Yes · Lookup table=(0; -100; -90; -80; -70; -60; -50; -40; -30; -20; -10; 0; 10; 20; 30; 40; 50; 60; 70; 80; 90; 100); (-100; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-90; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-80; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-70; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-60; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-50; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-40; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-30; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-20; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100); (10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 97; 90; 90; 90; 90; 90; 90; 90; 90; 90; 90); (20; 0; 0; 0; 0; 0; 0; 0; 0; 0...
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`
- Utilisé par : *(personne)*
- Ligne export : 47608 · id 128068

#### e Max_differential  `IP`
- Propriétés : Unit=% · Default mode={70}
- Utilisé par : `Left unfree`, `Right unfree`, `Single adjust item: Max_differential`
- Ligne export : 47621 · id 128069

#### Left unfree  `MAC`
- Logique :
  ```qcode
  right := DMAC_EV_1_Right
  left := DMAC_EV_2_Left
  
  if (right > 0 and left < 0) or (right < 0 and left > 0) then
    res := 0
  elseif  Abs(right) <= Abs(left) then
    res := left
  elseif Abs(right) > Abs(left) then
    res := MaxOfAbs(right * e Max_differential  / 100, left)
  endif
  
  
  Result := res
  ```
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `e Max_differential`
- Utilisé par : `DMAC Table Left`
- Ligne export : 47633 · id 128070

#### DMAC Table Left  `DMAC`
- Propriétés : Unit=% · Function selector=e Speed Mode
- Fonction *OFF* :
  - **Controlling +/-** = `0`
- Fonction *IDLE* :
  - **Controlling +/-** = `0`
- Fonction *Free* :
  - **Controlling +/-** = `DMAC_EV_2_Left [%] * System Crash Signal`
- Fonction *UnFree* :
  - **Controlling +/-** = `Left unfree * System Crash Signal`
- Lit : `DMAC_EV_2_Left`, `Left unfree`, `System Crash Signal`, `e Speed Mode`
- Utilisé par : `e Brake Activation`, `e Left Filter`
- Ligne export : 47663 · id 128108

#### e Left Filter  `SFC`
- Propriétés : Input channel=DMAC Table Left [%] · Enable=Yes · Type=Slopes · Slopes={{e Start Slope [%/s]; e Stop Slope [%/s]}; {e Start Slope [%/s]; e Stop Slope [%/s]}}
- Lit : `DMAC Table Left`, `e Start Slope`, `e Stop Slope`
- Utilisé par : `e Brake Activation`, `e Math Left`
- Ligne export : 47851 · id 128166

#### Cruise Right  `LTC`
- Propriétés : Unit=% · Row selector=DMAC_EV_1_Right [%] · Column selector=DMAC_EV_2_Left [%] · Interpolation=Yes · Lookup table=(0; -100; -90; -80; -70; -60; -50; -40; -30; -20; -10; 0; 10; 20; 30; 40; 50; 60; 70; 80; 90; 100); (-100; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-90; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-80; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-70; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-60; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-50; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-40; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-30; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-20; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (-10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0); (0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100; 100); (10; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 97; 90; 90; 90; 90; 90; 90; 90; 90; 90; 90); (20; 0; 0; 0; 0; 0; 0; 0; 0; 0...
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`
- Utilisé par : *(personne)*
- Ligne export : 47869 · id 128167

#### Right unfree  `MAC`
> right := DMAC_EV_1_Right <br>left := DMAC_EV_2_Left <br> <br>if (right > 0 and left < 0) or (right < 0 and left > 0) then <br>  res := 0 <br>elseif  Abs(right) >= Abs(left) then <br>  res := right <br>elseif Abs(right) < Abs(left) then <br>  res := MaxOfAbs(left * e Max_differential  / 100, right) <br>endif <br> <br> <br>Result := res
- Logique :
  ```qcode
  right := DMAC_EV_1_Right
  left := DMAC_EV_2_Left
  
  if (right > 0 and left < 0) or (right < 0 and left > 0) then
    res := 0
  elseif  Abs(right) >= Abs(left) then
    res := right
  elseif Abs(right) < Abs(left) then
    res := MaxOfAbs(left * e Max_differential  / 100, right)
  endif
  
  
  Result := res
  ```
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`, `e Max_differential`
- Utilisé par : `DMAC Table Right`
- Ligne export : 47882 · id 128168

#### DMAC Table Right  `DMAC`
- Propriétés : Unit=% · Function selector=e Speed Mode
- Fonction *OFF* :
  - **Controlling +/-** = `0`
- Fonction *IDLE* :
  - **Controlling +/-** = `0`
- Fonction *Free* :
  - **Controlling +/-** = `DMAC_EV_1_Right [%] * System Crash Signal`
- Fonction *UnFree* :
  - **Controlling +/-** = `Right unfree * System Crash Signal`
- Lit : `DMAC_EV_1_Right`, `Right unfree`, `System Crash Signal`, `e Speed Mode`
- Utilisé par : `e Brake Activation`, `e Right Filter`
- Ligne export : 47912 · id 128206

#### e Right Filter  `SFC`
- Propriétés : Input channel=DMAC Table Right [%] · Enable=Yes · Type=Slopes · Slopes={{e Start Slope [%/s]; e Stop Slope [%/s]}; {e Start Slope [%/s]; e Stop Slope [%/s]}}
- Lit : `DMAC Table Right`, `e Start Slope`, `e Stop Slope`
- Utilisé par : `e Brake Activation`, `e Math Right`
- Ligne export : 48100 · id 128264

#### e Brake Activation  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(DMAC Table Left [%] <> 0) OR (DMAC Table Right [%] <> 0) OR (e Right Filter [%] <> 0) OR (e Left Filter [%] <> 0)`
- Lit : `DMAC Table Left`, `DMAC Table Right`, `e Left Filter`, `e Right Filter`
- Utilisé par : *(personne)*
- Ligne export : 48118 · id 128265

#### e State All Speed  `SMC`
- Propriétés : Default state name=OFF
- Fonction *IDLE* :
  - **Activating** = `E Speed Int = 0`
  - **Blocking** = `not(e System Started)`
- Fonction *Slow* :
  - **Activating** = `E Speed Int = 1`
  - **Blocking** = `not(e System Started)`
- Fonction *Super Slow* :
  - **Activating** = `E Speed Int = 2`
  - **Blocking** = `not(e System Started)`
- Fonction *Fast* :
  - **Activating** = `E Speed Int = 3`
  - **Blocking** = `not(e System Started)`
- Lit : `E Speed Int`, `e System Started`
- Utilisé par : `VIEW BUTTON States md4/md3 mc`, `brokenVIEW TRACK STATE`, `e State All Speed Int`, `e State All Speed d3 Int`
- Ligne export : 48190 · id 128285

#### Joystick to zero  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(DMAC_EV_1_Right [%] = 0) AND (DMAC_EV_2_Left [%] = 0)`
- Lit : `DMAC_EV_1_Right`, `DMAC_EV_2_Left`
- Utilisé par : `Joystick to zero APPOUT`, `Ladder is not up`
- Ligne export : 48363 · id 223685

#### e Max Speed  `IP`
- Propriétés : Unit=% · Mode selector=e Speed Pump · Default mode: Slow={35} · Mode 1: Super Slow={15} · Mode 2: Fast Speed={100}
- Lit : `e Speed Pump`
- Utilisé par : `Min Speed`, `e Math Left`, `e Math Right`, `Single adjust item: Max Speed`
- Ligne export : 48417 · id 131718
