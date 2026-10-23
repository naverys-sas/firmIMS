# MC42[1] application — STATE

19 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## STATE

#### Engine State  `FGI`
- Propriétés : Input type=State · Input=Engine State · Default state name=OFF · States={STARTING; READY; ERROR}
- Lit : `Engine State`, `State`
- Utilisé par : `VIEW ENGINE STATE`
- Ligne export : 65935 · id 38935

#### Up/DOWN STATE  `FGI`
- Propriétés : Input type=State · Input=State Up/Down · Default state name=OFF · States={DOWN; INTERMEDIATE; UP; UP AND BLOC}
- Lit : `State`, `State Up/Down`
- Utilisé par : `VIEW ENGINE STATE`
- Ligne export : 65950 · id 38936

#### Speed State  `FGI`
- Propriétés : Input type=State · Input=State All Speed · Default state name=OFF · States={IDLE; SLOW; SUPER SLOW; ROAD; ROAS ASK; ROAD CRUISE}
- Lit : `State`, `State All Speed`
- Utilisé par : `BUTTON DRIVE`, `VIEW ENGINE STATE`
- Ligne export : 65966 · id 38937

#### VIEW ENGINE STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *STARTING* :
  - **Activating** = `Engine State = 1`
- Fonction *READY* :
  - **Activating** = `Engine State = 2`
  - **Blocking** = `(Up/DOWN STATE > 0) OR (Speed State > 1)`
- Fonction *DOWN* :
  - **Activating** = `Up/DOWN STATE = 1`
  - **Blocking** = `Engine State = 3`
- Fonction *INTERMEDIAIRE* :
  - **Activating** = `Up/DOWN STATE = 2`
  - **Blocking** = `Engine State = 3`
- Fonction *UP* :
  - **Activating** = `Up/DOWN STATE = 3`
  - **Blocking** = `Engine State = 3`
- Fonction *UP AND BLOC* :
  - **Activating** = `Up/DOWN STATE = 4`
  - **Blocking** = `Engine State = 3`
- Fonction *SLOW* :
  - **Activating** = `Speed State = 2`
  - **Blocking** = `(Up/DOWN STATE > 0) OR (Engine State = 3)`
- Fonction *Super Slow* :
  - **Activating** = `Speed State = 3`
  - **Blocking** = `(Up/DOWN STATE > 0) OR (Engine State = 3)`
- Fonction *ROAD* :
  - **Activating** = `Speed State = 4`
  - **Blocking** = `(Up/DOWN STATE > 0) OR (Engine State = 3)`
- Fonction *Road Cruise* :
  - **Activating** = `(Speed State = 5) OR (Speed State = 6)`
  - **Blocking** = `(Up/DOWN STATE > 0) OR (Engine State = 3)`
- Fonction *ERROR* :
  - **Activating** = `Engine State = 3`
- Lit : `Engine State`, `Speed State`, `Up/DOWN STATE`
- Utilisé par : `Engine OutPut Text`
- Ligne export : 65984 · id 38939

#### Charger STATE  `FGI`
- Propriétés : Input type=State · Input=Charger STATE · Default state name=OFF · States={ERROR; READY; RUN 220V}
- Lit : `Charger STATE`, `State`
- Utilisé par : `Charger STATE`, `Soc state`, `Timer Soc`, `VIEW BATTERY STATE`
- Ligne export : 66491 · id 39018

#### Battery State  `FGI`
- Propriétés : Input type=State · Input=Battery State · Default state name=OFF · States={ERROR; READY; RUN; RUN ECO}
- Lit : `Battery State`, `State`
- Utilisé par : `VIEW BATTERY STATE`
- Ligne export : 66506 · id 39019

#### VIEW BATTERY STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *READY* :
  - **Activating** = `Battery State = 2`
  - **Blocking** = `(Battery State = 1) OR (Charger STATE >= 3)`
- Fonction *CHARGE 220V* :
  - **Activating** = `Charger STATE >= 3`
  - **Blocking** = `Battery State = 1`
- Fonction *RUN* :
  - **Activating** = `(Battery State = 3) OR (Battery State = 4)`
  - **Blocking** = `Charger STATE >= 3`
- Fonction *ERROR* :
  - **Activating** = `Battery State = 1`
- Lit : `Battery State`, `Charger STATE`
- Utilisé par : `VIEW BAT Charging`, `VIEW BAT Error`, `VIEW BAT Ready`, `VIEW BAT Run`
- Ligne export : 66522 · id 39021

#### SOC  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Battery SOC [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Battery SOC`
- Utilisé par : `SOC FIlter`
- Ligne export : 66708 · id 39059

#### Soc state  `SMC`
- Propriétés : Default state name=SOC
- Fonction *Charging* :
  - **Activating** = `Charger STATE >= 3`
- Lit : `Charger STATE`
- Utilisé par : `VIEW SOC`
- Ligne export : 66722 · id 39060

#### Timer Soc  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Charger STATE >= 3`
  - **Resetting** = `(Timer Soc [ms] >= 4000) OR (NegativeFlank((Charger STATE >= 3))) OR (PositiveFlank((Charger STATE >= 3)))`
- Lit : `Charger STATE`
- Utilisé par : `VIEW SOC 2`
- Ligne export : 66764 · id 39068

#### SOC FIlter  `SFC`
- Propriétés : Input channel=SOC [%] · Enable=Yes · Type=Slopes · Slopes={{20; 20}; {20; 20}}
- Lit : `SOC`
- Utilisé par : `VIEW SOC`, `VIEW SOC 2`
- Ligne export : 66852 · id 39082

#### VIEW SOC 2  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin((MinOf(100, (MaxOf((Timer Soc [ms] / 30), SOC FIlter [%])))): 0->0, 100->100, Freeze)`
- Lit : `C`, `SOC FIlter`, `Timer Soc`
- Utilisé par : `VIEW SOC`
- Ligne export : 66870 · id 39083

#### VIEW SOC  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Soc state
- Fonction *SOC* :
  - **Controlling** = `lin(SOC FIlter [%]: 0->0, 95->100, Freeze)`
- Fonction *Charging* :
  - **Controlling** = `VIEW SOC 2 [%]`
- Lit : `SOC FIlter`, `Soc state`, `VIEW SOC 2`
- Utilisé par : `MD4-10 page: MAIN`, `MD4-10 page: SHUTDOWN`
- Ligne export : 66944 · id 39094

#### VIEW BAT Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `VIEW BATTERY STATE = 1`
- Lit : `VIEW BATTERY STATE`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 67029 · id 39109

#### VIEW BAT Charging  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `VIEW BATTERY STATE = 2`
- Lit : `VIEW BATTERY STATE`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 67074 · id 39125

#### VIEW BAT Run  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `VIEW BATTERY STATE = 3`
- Lit : `VIEW BATTERY STATE`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 67119 · id 39133

#### VIEW BAT Error  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `VIEW BATTERY STATE = 4`
- Lit : `VIEW BATTERY STATE`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 67164 · id 39149

#### BUTTON DRIVE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MD4 - Start Button Blocking Neutral) AND (Speed State > 1)`
- Lit : `MD4 - Start Button Blocking Neutral`, `Speed State`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 67209 · id 47441

#### Engine OutPut Text  `TP`
- Propriétés : Mode selector=VIEW ENGINE STATE · Default mode: OFF={OFF} · Mode 1: STARTING={START} · Mode 2: READY={READY} · Mode 3: DOWN={DOWN} · Mode 4: INTERMEDIAIRE={...} · Mode 5: UP={UP} · Mode 6: UP AND BLOC={UP} · Mode 7: SLOW={SLOW} · Mode 8: Super Slow={S.SLOW} · Mode 9: ROAD={FAST} · Mode 10: Road Cruise={CRUISE} · Mode 11: ERROR={ERROR}
- Lit : `VIEW ENGINE STATE`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 67261 · id 55695
