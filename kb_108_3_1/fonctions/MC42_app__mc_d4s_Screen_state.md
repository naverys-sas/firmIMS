# MC42 app — mc.d4s Screen state

37 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## mc.d4s Screen state

#### brokenVIEW ENGINE STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *1.STARTING* :
  - **Activating** = `Electric Engine State Feed-back = 1`
- Fonction *2.READY* :
  - **Activating** = `Electric Engine State Feed-back = 2`
  - **Blocking** = `E State Up/Down > 0`
- Fonction *3.DOWN* :
  - **Activating** = `E State Up/Down = 1`
  - **Blocking** = `Engines Error`
- Fonction *4.INTERMEDIAIRE* :
  - **Activating** = `E State Up/Down = 2`
  - **Blocking** = `Engines Error`
- Fonction *5.UP* :
  - **Activating** = `E State Up/Down = 4`
  - **Blocking** = `Engines Error`
- Fonction *10.ERROR* :
  - **Activating** = `Electric Engine State Feed-back = 3`
- Fonction *11.UP AND BLOC* :
  - **Activating** = `E State Up/Down = 3`
  - **Blocking** = `Electric Engine State Feed-back = 3`
- Lit : `E State Up/Down`, `Electric Engine State Feed-back`, `Engines Error`
- Utilisé par : `E Engine OutPut Text`
- Ligne export : 51614 · id 141962

#### Charger STATE  `FGI`
- Propriétés : Input type=State · Input=Charger State Feed-back · Default state name=OFF · States={ERROR; READY; CONNECTED; CHARGING}
- Lit : `Charger State Feed-back`, `State`
- Utilisé par : `Soc state`, `Timer Soc`, `VIEW CHARGER Connected or Runnning boat`, `VIEW CHARGER Ready/ Standby bat`, `VIEW CHARGER STATE`
- Ligne export : 51893 · id 142025

#### Battery State  `FGI`
- Propriétés : Input type=State · Input=Battery State Feed-Back · Default state name=OFF · States={STANDBY; CHARGE; DISCHARGE}
- Lit : `Battery State Feed-Back`, `State`
- Utilisé par : `VIEW CHARGER Connected or Runnning boat`, `VIEW CHARGER Ready/ Standby bat`
- Ligne export : 51909 · id 142029

#### VIEW CHARGER STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ERROR* :
  - **Activating** = `Charger STATE = 1`
- Fonction *READY* :
  - **Activating** = `Charger STATE = 2`
- Fonction *CONNECTED* :
  - **Activating** = `Charger STATE = 3`
- Fonction *CHARGING* :
  - **Activating** = `Charger STATE = 4`
- Lit : `Charger STATE`
- Utilisé par : `VIEW CHARGER Charging`, `VIEW CHARGER Connected or Runnning boat`, `VIEW CHARGER Error`, `VIEW CHARGER Ready/ Standby bat`
- Ligne export : 51924 · id 142034

#### SOC  `FGI`
- Propriétés : Unit=% · Input type=Real · Input=Battery SOC Customer [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `Battery SOC Customer`
- Utilisé par : `SOC FIlter`
- Ligne export : 52065 · id 142059

#### Soc state  `SMC`
- Propriétés : Default state name=SOC
- Fonction *Charging* :
  - **Activating** = `Charger STATE = 4`
- Lit : `Charger STATE`
- Utilisé par : `VIEW SOC md4`
- Ligne export : 52079 · id 142060

#### Timer Soc  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Charger STATE = 4`
  - **Resetting** = `(Timer Soc [ms] >= 4000) OR (NegativeFlank((Charger STATE = 3))) OR (PositiveFlank((Charger STATE = 3)))`
- Lit : `Charger STATE`
- Utilisé par : `VIEW SOC 2`
- Ligne export : 52121 · id 142068

#### SOC FIlter  `SFC`
- Propriétés : Input channel=SOC [%] · Enable=Yes · Type=Slopes · Slopes={{20; 20}; {20; 20}}
- Lit : `SOC`
- Utilisé par : `VIEW SOC 2`, `VIEW SOC md4`
- Ligne export : 52209 · id 142082

#### VIEW SOC 2  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin((MinOf(100, (MaxOf((Timer Soc [ms] / 30), SOC FIlter [%])))): 0->0, 100->100, Freeze)`
- Lit : `SOC FIlter`, `Timer Soc`
- Utilisé par : `VIEW SOC md4`
- Ligne export : 52227 · id 142083

#### VIEW SOC md4  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=Soc state
- Fonction *SOC* :
  - **Controlling** = `lin(SOC FIlter [%]: 0->0, 100->100, Freeze)`
- Fonction *Charging* :
  - **Controlling** = `VIEW SOC 2 [%]`
- Lit : `SOC FIlter`, `Soc state`, `VIEW SOC 2`
- Utilisé par : `MD4-10 page: MAIN`, `MD4-10 page: SHUTDOWN`, `MD4-5 page: MAIN Elec`, `MD4-5 page: SHUTDOWN`
- Ligne export : 52301 · id 142094

#### VIEW CHARGER Ready/ Standby bat  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(VIEW CHARGER STATE = 2) OR ((Battery State = 1) and (Charger STATE = 0))`
- Lit : `Battery State`, `Charger STATE`, `VIEW CHARGER STATE`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 52386 · id 142110

#### VIEW CHARGER Charging  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `VIEW CHARGER STATE = 4`
- Lit : `VIEW CHARGER STATE`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 52458 · id 142118

#### VIEW CHARGER Connected or Runnning boat  `IDC`
> delay to prevent no soc
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `(VIEW CHARGER STATE = 3) OR ((Battery State = 3) and (Charger STATE = 0))`
- Lit : `Battery State`, `Charger STATE`, `VIEW CHARGER STATE`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 52503 · id 142126

#### VIEW CHARGER Error  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `VIEW CHARGER STATE = 1`
- Lit : `VIEW CHARGER STATE`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 52575 · id 142134

#### e State All Speed Int  `IMAC`
- Logique :
  - **Controlling** = `e State All Speed`
- Lit : `e State All Speed`
- Utilisé par : `State All Speed Int`
- Ligne export : 52620 · id 208601

#### T State All Speed Int  `IMAC`
- Logique :
  - **Controlling** = `T State All Speed`
- Lit : `T State All Speed`
- Utilisé par : `State All Speed Int`
- Ligne export : 52661 · id 208609

#### State All Speed Int  `IMAC`
- Logique :
  - **Controlling** = `e State All Speed Int + T State All Speed Int`
- Lit : `T State All Speed Int`, `e State All Speed Int`
- Utilisé par : `BUTTON DRIVE 4ET`
- Ligne export : 52702 · id 208617

#### E Engine OutPut Text  `TP`
- Propriétés : Mode selector=brokenVIEW ENGINE STATE · Default mode: OFF={} · Mode 1: 1.STARTING={STARTING} · Mode 2: 2.READY={READY} · Mode 3: 3.DOWN={DOWN} · Mode 4: 4.INTERMEDIAIRE={} · Mode 5: 5.UP={} · Mode 6: 10.ERROR={ERROR} · Mode 7: 11.UP AND BLOC={UP & LOCK}
- Lit : `UP`, `brokenVIEW ENGINE STATE`
- Utilisé par : *(personne)*
- Ligne export : 52759 · id 142151

#### Power State Int E  `IMAC`
- Logique :
  - **Controlling** = `Electric Engine State Feed-back`
- Lit : `Electric Engine State Feed-back`
- Utilisé par : `Power State Int`, `VIEW BUTTON States md4/md3 mc`
- Ligne export : 52784 · id 156165

#### Power State Int T  `IMAC`
- Logique :
  - **Controlling** = `T Engine State mc`
- Lit : `T Engine State mc`
- Utilisé par : `Power State Int`
- Ligne export : 52825 · id 208476

#### Power State Int  `IMAC`
- Logique :
  - **Controlling** = `Power State Int E + Power State Int T`
- Lit : `Power State Int E`, `Power State Int T`
- Utilisé par : `VIEW BUTTON States md4/md3 mc`
- Ligne export : 52866 · id 208499

#### e Speed Mode Int  `IMAC`
- Logique :
  - **Controlling** = `e Speed Mode`
- Lit : `e Speed Mode`
- Utilisé par : `Speed Mode Int`
- Ligne export : 52923 · id 208522

#### T Speed Mode Int  `IMAC`
- Logique :
  - **Controlling** = `T Speed Mode`
- Lit : `T Speed Mode`
- Utilisé par : `Speed Mode Int`
- Ligne export : 52964 · id 208541

#### Speed Mode Int  `IMAC`
- Logique :
  - **Controlling** = `e Speed Mode Int + T Speed Mode Int`
- Lit : `T Speed Mode Int`, `e Speed Mode Int`
- Utilisé par : `VIEW BUTTON States md4/md3 mc`
- Ligne export : 53005 · id 208562

#### VIEW BUTTON States md4/md3 mc  `SMC`
- Propriétés : Default state name=Stop
- Fonction *Ready* :
  - **Activating** = `(Power State Int = 2) AND (Speed Mode Int <= 1)`
- Fonction *Start* :
  - **Activating** = `Power State Int E = Power State Int`
  - **Blocking** = `(2 = Speed Mode Int) OR (Speed Mode Int <= 1)`
- Fonction *Start Free* :
  - **Activating** = `(Speed Mode Int = 2) AND (2 = Speed Mode Int)`
  - **Blocking** = `e State All Speed <= 1`
- Lit : `Power State Int`, `Power State Int E`, `Speed Mode Int`, `e State All Speed`
- Utilisé par : `F4 Off`
- Ligne export : 53062 · id 156133

#### brokenVIEW TRACK STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *6.SLOW* :
  - **Activating** = `e Speed Pump = 0`
  - **Blocking** = `(E State Up/Down <> 1) OR (Engines Error) OR (Electric Engine State Feed-back = 0)`
- Fonction *7.Super Slow* :
  - **Activating** = `e Speed Pump = 1`
  - **Blocking** = `(E State Up/Down <> 1) OR (Engines Error) OR (Electric Engine State Feed-back = 0)`
- Fonction *8.FAST* :
  - **Activating** = `e Speed Pump = 2`
  - **Blocking** = `(E State Up/Down <> 1) OR (Engines Error) OR (Electric Engine State Feed-back = 0)`
- Fonction *9. Cruise* :
  - **Activating** = `e State All Speed = 6`
  - **Blocking** = `(Engines Error) OR (E State Up/Down <> 1) OR (Electric Engine State Feed-back = 0)`
- Fonction *auto up/down* :
  - **Activating** = `auto up/down 4ET`
  - **Blocking** = `(Engines Error) OR (Electric Engine State Feed-back = 0)`
- Fonction *10.ERROR* :
  - **Activating** = `Electric Engine State Feed-back = 3`
- Lit : `E State Up/Down`, `Electric Engine State Feed-back`, `Engines Error`, `auto up/down 4ET`, `e Speed Pump`, `e State All Speed`
- Utilisé par : `E Track OutPut Text`, `E Track OutPut Text CAB`
- Ligne export : 53215 · id 202054

#### E Track OutPut Text  `TP`
- Propriétés : Mode selector=brokenVIEW TRACK STATE · Default mode: OFF={} · Mode 1: 6.SLOW={} · Mode 2: 7.Super Slow={} · Mode 3: 8.FAST={} · Mode 4: 9. Cruise={} · Mode 5: auto up/down={MOVING} · Mode 6: 10.ERROR={ERROR}
- Lit : `brokenVIEW TRACK STATE`
- Utilisé par : *(personne)*
- Ligne export : 53536 · id 202123

#### T VIEW ENGINE STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *1.STARTING* :
  - **Activating** = `T Engine State mc = 1`
- Fonction *2.READY* :
  - **Activating** = `T Engine State mc = 2`
  - **Blocking** = `T State Up/Down > 0`
- Fonction *3.DOWN* :
  - **Activating** = `T State Up/Down = 1`
- Fonction *4.INTERMEDIAIRE* :
  - **Activating** = `T State Up/Down = 2`
- Fonction *10.ERROR* :
  - **Activating** = `T Engine State mc = 3`
- Fonction *5.UP* :
  - **Activating** = `T State Up/Down = 4`
- Fonction *11.UP AND BLOC* :
  - **Activating** = `T State Up/Down = 3`
  - **Blocking** = `T Engine State mc = 3`
- Lit : `T Engine State mc`, `T State Up/Down`
- Utilisé par : `T Engine OutPut Text`
- Ligne export : 53559 · id 208315

#### T Engine OutPut Text  `TP`
- Propriétés : Mode selector=T VIEW ENGINE STATE · Default mode: OFF={} · Mode 1: 1.STARTING={STARTING} · Mode 2: 2.READY={READY} · Mode 3: 3.DOWN={DOWN} · Mode 4: 4.INTERMEDIAIRE={} · Mode 5: 10.ERROR={ERROR} · Mode 6: 5.UP={} · Mode 7: 11.UP AND BLOC={UP & LOCK}
- Lit : `T VIEW ENGINE STATE`, `UP`
- Utilisé par : *(personne)*
- Ligne export : 53817 · id 208352

#### T VIEW TRACK STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *6.SLOW* :
  - **Activating** = `T Speed Pump = 0`
  - **Blocking** = `(T State Up/Down <> 1) OR (T Engine State mc = 0)`
- Fonction *7.Super Slow* :
  - **Activating** = `T Speed Pump = 1`
  - **Blocking** = `(T State Up/Down <> 1) OR (T Engine State mc = 0)`
- Fonction *8.FAST* :
  - **Activating** = `T Speed Pump = 2`
  - **Blocking** = `(T State Up/Down <> 1) OR (T Engine State mc = 0)`
- Fonction *9. Cruise* :
  - **Activating** = `T State All Speed = 6`
  - **Blocking** = `(T State Up/Down <> 1) OR (T Engine State mc = 0)`
- Fonction *auto up/down* :
  - **Activating** = `auto up/down 4ET`
  - **Blocking** = `T Engine State mc = 0`
- Fonction *10.ERROR* :
  - **Activating** = `T Engine State mc = 3`
- Lit : `T Engine State mc`, `T Speed Pump`, `T State All Speed`, `T State Up/Down`, `auto up/down 4ET`
- Utilisé par : `T Track OutPut Text`
- Ligne export : 53842 · id 208353

#### T Track OutPut Text  `TP`
- Propriétés : Mode selector=T VIEW TRACK STATE · Default mode: OFF={} · Mode 1: 6.SLOW={} · Mode 2: 7.Super Slow={} · Mode 3: 8.FAST={} · Mode 4: 9. Cruise={} · Mode 5: auto up/down={MOVING} · Mode 6: 10.ERROR={ERROR}
- Lit : `T VIEW TRACK STATE`
- Utilisé par : *(personne)*
- Ligne export : 54128 · id 208395

#### E Track OutPut Text CAB  `TP`
- Propriétés : Mode selector=brokenVIEW TRACK STATE · Default mode: OFF={Off} · Mode 1: 6.SLOW={Slow} · Mode 2: 7.Super Slow={S. Slow} · Mode 3: 8.FAST={Fast} · Mode 4: 9. Cruise={} · Mode 5: auto up/down={MOVING} · Mode 6: 10.ERROR={ERROR}
- Lit : `brokenVIEW TRACK STATE`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 54175 · id 233704

#### show discharge jauge  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(E.Power Management System = 2) AND (Engines READY 45)`
- Lit : `E.Power Management System`, `Engines READY 45`
- Utilisé par : `MD4-5 page: MAIN Elec`
- Ligne export : 54198 · id 240347

#### Show standby jauge  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(not(Engines READY 45)) OR (E.Power Management System = 1)`
- Lit : `E.Power Management System`, `Engines READY 45`
- Utilisé par : `MD4-5 page: MAIN Elec`
- Ligne export : 54250 · id 240352

#### show charge jauge  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `E.Power Management System = 3`
- Lit : `E.Power Management System`
- Utilisé par : `MD4-5 page: MAIN Elec`
- Ligne export : 54303 · id 240356

#### Show crash jauge  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `E.Power Management System = 4`
- Lit : `E.Power Management System`
- Utilisé par : `MD4-5 page: MAIN Elec`
- Ligne export : 54348 · id 240360

#### Show symbole batterie 400V  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(E.Power Management System = 2) OR (E.Power Management System = 3)`
- Lit : `E.Power Management System`
- Utilisé par : `MD4-5 page: MAIN Elec`
- Ligne export : 54393 · id 240427
