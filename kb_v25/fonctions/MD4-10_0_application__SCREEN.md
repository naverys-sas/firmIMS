# MD4-10[0] application — SCREEN

31 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## SCREEN

#### Cancel Button  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Boat State`, `OFF Button`, `Power Down State`, `MD4-10 page: SHUTDOWN`
- Ligne export : 21999 · id 48468

#### Boat State  `FSM`
- Propriétés : Store value=No
- État 0 **Startup**
  - transition *Unlock* (état cible non exporté par IQANdesign)
    - **Activating** = `(Unlock Boat) OR (Good PIN)`
  - transition *Shut Down* (état cible non exporté par IQANdesign)
    - **Activating** = `Power Down`
- État 1 **Run**
  - transition *Shut Down* (état cible non exporté par IQANdesign)
    - **Activating** = `Power Down`
  - transition *Charging* (état cible non exporté par IQANdesign)
    - **Activating** = `Charger Charging IDC and (not(Continue))`
- État 2 **ShutDown**
  - transition *Cancel* (état cible non exporté par IQANdesign)
    - **Activating** = `Unlock Boat and Cancel Button`
  - transition *Cancel* (état cible non exporté par IQANdesign)
    - **Activating** = `Cancel Button and (not(Unlock Boat))`
- État 3 **Charging**
  - transition *Continue* (état cible non exporté par IQANdesign)
    - **Activating** = `Continue`
  - transition *Shutdown* (état cible non exporté par IQANdesign)
    - **Activating** = `Power Down`
- Lit : `Cancel Button`, `Charger Charging IDC`, `Continue`, `Good PIN`, `Power Down`, `Unlock Boat`
- Utilisé par : `Main page IDC`, `Screen Charging`, `ShutDown page IDC`, `Startup page IDC`
- Ligne export : 22009 · id 48431

#### Main page IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `1 = Boat State`
- Lit : `Boat State`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 22303 · id 48506

#### ShutDown page IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(2 = Boat State) OR (3 = Boat State)`
- Lit : `Boat State`
- Utilisé par : `MD4-10 page: SHUTDOWN`
- Ligne export : 22348 · id 48519

#### Startup page IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `0 = Boat State`
- Lit : `Boat State`
- Utilisé par : `MD4-10 page: STARTUP`
- Ligne export : 23600 · id 49977

#### Continue Button  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Continue`, `MD4-10 page: SHUTDOWN`
- Ligne export : 23645 · id 60153

#### Continue  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Continue OR (Continue Button)`
  - **Blocking** = `(PositiveFlank(Off Button - IDC)) OR (NegativeFlank(Charger Charging IDC))`
- Lit : `Charger Charging IDC`, `Continue Button`, `Off Button - IDC`
- Utilisé par : `Auto Off Message`, `Boat State`, `Charging State`, `Event log: A/C Bat Pack`, `Event log: Acceleration`, `Event log: BMW Battery`, `Event log: Battery Isolation`, `Event log: Electronic Logs`, `Event log: WattAlps Battery`
- Ligne export : 23655 · id 60159

#### Screen Charging  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `3 = Boat State`
- Lit : `Boat State`
- Utilisé par : `Screen NOT Charging`, `MD4-10 page: SHUTDOWN`, `MD4-10 page: STARTUP`
- Ligne export : 23721 · id 60174

#### Screen NOT Charging  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Screen Charging)`
- Lit : `Screen Charging`
- Utilisé par : `MD4-10 page: SHUTDOWN`
- Ligne export : 23766 · id 60198

## SCREEN / PIN Pad

#### 1 VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `PIN State`, `MD4-10 page: STARTUP`
- Ligne export : 22417 · id 49167

#### 3 VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `PIN State`, `MD4-10 page: STARTUP`
- Ligne export : 22427 · id 49169

#### 2 VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `PIN State`, `MD4-10 page: STARTUP`
- Ligne export : 22437 · id 49170

#### 4 VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `PIN State`, `MD4-10 page: STARTUP`
- Ligne export : 22447 · id 49171

#### 5 VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `PIN State`, `MD4-10 page: STARTUP`
- Ligne export : 22457 · id 49172

#### 6 VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `PIN State`, `MD4-10 page: STARTUP`
- Ligne export : 22467 · id 49173

#### 7 VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `PIN State`, `MD4-10 page: STARTUP`
- Ligne export : 22477 · id 49174

#### 8 VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `PIN State`, `MD4-10 page: STARTUP`
- Ligne export : 22487 · id 49175

#### 9 VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `PIN State`, `MD4-10 page: STARTUP`
- Ligne export : 22497 · id 49177

#### 0 VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `PIN State`, `MD4-10 page: STARTUP`
- Ligne export : 22507 · id 49179

#### PIN CODE  `IP`
- Propriétés : Default mode={1000}
- Utilisé par : `Good PIN`, `Adjust group: Main Setup`, `Single adjust item: PIN CODE`
- Ligne export : 22517 · id 49533

#### PIN State  `SMC`
- Propriétés : Default state name=NO
- Fonction *1* :
  - **Activating** = `1 VDIN`
- Fonction *2* :
  - **Activating** = `2 VDIN`
- Fonction *3* :
  - **Activating** = `3 VDIN`
- Fonction *4* :
  - **Activating** = `4 VDIN`
- Fonction *5* :
  - **Activating** = `5 VDIN`
- Fonction *6* :
  - **Activating** = `6 VDIN`
- Fonction *7* :
  - **Activating** = `7 VDIN`
- Fonction *8* :
  - **Activating** = `8 VDIN`
- Fonction *9* :
  - **Activating** = `9 VDIN`
- Fonction *0* :
  - **Activating** = `0 VDIN`
- Lit : `0 VDIN`, `1 VDIN`, `2 VDIN`, `3 VDIN`, `4 VDIN`, `5 VDIN`, `6 VDIN`, `7 VDIN`, `8 VDIN`, `9 VDIN`
- Utilisé par : `PIN Value`, `PIN counter`
- Ligne export : 22529 · id 49594

#### PIN Value  `IMAC`
- Propriétés : Function selector=PIN State
- Fonction *NO* :
  - **Controlling** = `0`
- Fonction *1* :
  - **Controlling** = `1`
- Fonction *2* :
  - **Controlling** = `2`
- Fonction *3* :
  - **Controlling** = `3`
- Fonction *4* :
  - **Controlling** = `4`
- Fonction *5* :
  - **Controlling** = `5`
- Fonction *6* :
  - **Controlling** = `6`
- Fonction *7* :
  - **Controlling** = `7`
- Fonction *8* :
  - **Controlling** = `8`
- Fonction *9* :
  - **Controlling** = `9`
- Fonction *0* :
  - **Controlling** = `0`
- Lit : `PIN State`
- Utilisé par : `Number 1`, `Number 2`, `Number 3`, `Number 4`
- Ligne export : 22848 · id 49640

#### PIN counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank((PIN State > 0))`
  - **Resetting** = `PIN counter > 3`
- Lit : `PIN State`
- Utilisé par : `Number 1`, `Number 2`, `Number 3`, `Number 4`, `PIN Pad Show`
- Ligne export : 23199 · id 49573

#### Number 1  `MEM`
- Propriétés : Input channel=PIN Value · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `1 = PIN counter`
- Lit : `PIN Value`, `PIN counter`
- Utilisé par : `Good PIN`
- Ligne export : 23269 · id 49590

#### Number 2  `MEM`
- Propriétés : Input channel=PIN Value · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `2 = PIN counter`
- Lit : `PIN Value`, `PIN counter`
- Utilisé par : `Good PIN`
- Ligne export : 23315 · id 49704

#### Number 3  `MEM`
- Propriétés : Input channel=PIN Value · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `3 = PIN counter`
- Lit : `PIN Value`, `PIN counter`
- Utilisé par : `Good PIN`
- Ligne export : 23361 · id 49715

#### Number 4  `MEM`
- Propriétés : Input channel=PIN Value · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `0 = PIN counter`
- Lit : `PIN Value`, `PIN counter`
- Utilisé par : `Good PIN`
- Ligne export : 23407 · id 49726

#### Good PIN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  if PIN CODE  = 1000 then
  Result := True
  else
  Result := (1000*Number 1 + 100*Number 2 + 10*Number 3 + 1*Number 4) = PIN CODE
  endif
  ```
- Lit : `Number 1`, `Number 2`, `Number 3`, `Number 4`, `PIN CODE`
- Utilisé par : `Boat State`
- Ligne export : 23453 · id 49751

#### PIN PAD  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `PIN Pad Show`, `MD4-10 page: STARTUP`
- Ligne export : 23477 · id 49768

#### PIN Pad Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank(PIN PAD)) OR (PIN Pad Show)`
  - **Blocking** = `PositiveFlank((0 = PIN counter))`
- Lit : `PIN PAD`, `PIN counter`
- Utilisé par : `PIN Show`, `MD4-10 page: STARTUP`
- Ligne export : 23487 · id 49771

#### PIN Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(PIN Pad Show)`
- Lit : `PIN Pad Show`
- Utilisé par : `MD4-10 page: STARTUP`
- Ligne export : 23555 · id 49793
