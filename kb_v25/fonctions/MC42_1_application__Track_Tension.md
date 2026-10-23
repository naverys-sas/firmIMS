# MC42[1] application — Track Tension

35 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Track Tension

#### Track pressure  `VIN`
- Propriétés : Unit=bar · Reference voltage=Reference voltage A · Error value=0 · Device type=IQAN-SP500 · Calibration={500; 4500; 0; 500} · Alarms={No; 0; No; 100} · Module=MC42[1] · Module index=2
- Utilisé par : `Pression Filter`, `Track Tension Error`, `Event log: Electronic Logs`, `MD4-10 page: INFO`, `Measure group: HVLP`, `Measure group: Hydraulic`
- Ligne export : 64331 · id 38483

#### Tracks pressure Mode  `SP`
> This channel is used to give unit and names to the MEM
- Propriétés : Input channel=None · Default state name=AUTO · States={UNTIGHTEN}
- Utilisé par : `EV Tension Force Open`, `IDC Free`, `ON/OFF/Untighed`, `Tension State`, `Tracks pressure Mode`, `Adjust group: Maintenance`, `MD4-10 page: SETUP`, `Single adjust item: Tracks pressure Mode`
- Ligne export : 64355 · id 38579

#### Reset Startup  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True   [Latching And]`
  - **Blocking** = `Reset Startup`
- Lit : `Reset Startup`
- Utilisé par : `Reset Startup`, `Reset Startup`, `Tracks pressure Mode`
- Ligne export : 64367 · id 38580

#### Tracks pressure Mode  `MEM`
- Propriétés : Input channel=Tracks pressure Mode · Action=Replace · Store value=Yes
- Logique :
  - **Resetting** = `Reset Startup`
- Lit : `Reset Startup`, `Tracks pressure Mode`
- Utilisé par : `EV Tension Force Open`, `IDC Free`, `ON/OFF/Untighed`, `Tension State`, `Adjust group: Maintenance`, `MD4-10 page: SETUP`, `Single adjust item: Tracks pressure Mode`
- Ligne export : 64417 · id 38589

#### Engines Ready  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engines Ready`
- Lit : `Engines Ready`
- Utilisé par : `10 minutes auto tender`, `Engines Ready output`, `Over Tension`, `State All Speed`, `State Speed Table`, `Wait engine start`
- Ligne export : 64460 · id 74909

#### Wait engine start  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Engines Ready`
- Lit : `Engines Ready`
- Utilisé par : `ON/OFF/Untighed`, `Ok tension`, `Tension State`, `Wait engine Stop`
- Ligne export : 64503 · id 38597

#### ON/OFF/Untighed  `SMC`
- Propriétés : Default state name=OFF
- Fonction *ON* :
  - **Activating** = `Wait engine start`
  - **Blocking** = `Tracks pressure Mode`
- Fonction *UNTIGHTED* :
  - **Activating** = `Tracks pressure Mode`
- Lit : `Tracks pressure Mode`, `Wait engine start`
- Utilisé par : `Super Ok tension`
- Ligne export : 64546 · id 38668

#### Pression Filter  `SFC`
- Propriétés : Input channel=Track pressure [bar] · Enable=Yes · Type=Slopes · Slopes={{50; 50}; {1; 1}}
- Lit : `Track pressure`
- Utilisé par : `Flag High Pressure Tension`, `Need Pressure`
- Ligne export : 64624 · id 38696

#### Time to tension  `IP`
- Propriétés : Unit=ms · Default mode={150}
- Utilisé par : `Super Ok tension`, `Adjust group: Master Track`, `Single adjust item: Time to tension`
- Ligne export : 64642 · id 38713

#### Ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `PositiveFlank(Wait engine start)`
- Lit : `Wait engine start`
- Utilisé par : `Super Ok tension`, `Measure group: HVLP`
- Ligne export : 64654 · id 38714

#### 10 minutes auto tender  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=10
- Logique :
  - **Decreasing** = `Engines Ready`
  - **Resetting** = `(10 minutes auto tender [min] <= 0) OR (NegativeFlank(Super Ok tension))`
- Lit : `Engines Ready`, `Super Ok tension`
- Utilisé par : `Super Ok tension`
- Ligne export : 64698 · id 38723

#### Need Pressure  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `(Min Tension Pressure [bar] > Pression Filter [bar]) AND (not(Flag End of tensionning))`
- Lit : `Flag End of tensionning`, `Min Tension Pressure`, `Pression Filter`
- Utilisé par : `Super Ok tension`
- Ligne export : 64767 · id 38735

#### Inter Ev Verin  `FGI`
- Propriétés : Input type=Digital · Input=Inter EV Verin · Default state name=Default state
- Lit : `Inter EV Verin`
- Utilisé par : `Super Ok tension`
- Ligne export : 64820 · id 38753

#### Over Tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `(Over Tension) OR (Slope Super Ok [%] > Tension Error Parameter [%])`
  - **Blocking** = `not(Engines Ready)`
- Lit : `Engines Ready`, `Slope Super Ok`, `Tension Error Parameter`
- Utilisé par : `Super Ok tension`, `Track Tension Error`, `Event log: Electronic Logs`
- Ligne export : 64831 · id 38755

#### Super Ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=Time to tension [ms] · Function selector=ON/OFF/Untighed
- Fonction *OFF* :
  - **Blocking** = `True`
- Fonction *ON* :
  - **Activating** = `(NegativeFlank(Ok tension)) OR (10 minutes auto tender [min] = 0) OR (Need Pressure)`
  - **Blocking** = `(Over Tension) OR (Inter Ev Verin)`
- Fonction *UNTIGHTED* :
  - **Blocking** = `True`
- Lit : `10 minutes auto tender`, `Inter Ev Verin`, `Need Pressure`, `ON/OFF/Untighed`, `Ok tension`, `Over Tension`, `Time to tension`
- Utilisé par : `10 minutes auto tender`, `Delay Off super ok tension`, `Flag End of tensionning`, `OK Tension`
- Ligne export : 64891 · id 38765

#### Ref Speed Slope  `IMAC`
- Logique :
  - **Controlling** = `MaxOf (Absolute)(Hydraulic speed slope [/s], 1000)`
- Lit : `Hydraulic speed slope`
- Utilisé par : `End of Tension Phase Delay`
- Ligne export : 65027 · id 92611

#### End Of Tension delay  `IP`
> Delay to allow a new tensionning phase after the previous one
- Propriétés : Unit=ms · Default mode={500}
- Utilisé par : `End of Tension Phase Delay`, `Adjust group: Master Track`, `Single adjust item: End Of Tension delay`
- Ligne export : 65075 · id 91766

#### Min Tension Pressure  `IP`
- Propriétés : Unit=bar · Default mode={150}
- Utilisé par : `Need Pressure`, `Adjust group: Track Setup`, `Single adjust item: Min Tension Pressure`
- Ligne export : 65087 · id 60026

#### End of Tension Phase Delay  `MAC`
> Duration of End of Tension phase: decel + adjustable still phase.
- Propriétés : Unit=ms · Limiting object group=Signed
- Logique :
  - **Controlling** = `((Abs((LOW SPEED [rpm] / Ref Speed Slope))) * 1000) + End Of Tension delay [ms]`
- Lit : `C`, `End Of Tension delay`, `LOW SPEED`, `Ref Speed Slope`
- Utilisé par : `Flag End of tensionning`
- Ligne export : 65099 · id 91737

#### Flag End of tensionning  `IDC`
> Rised at the end of a tensionning operation
- Propriétés : Toggle=No · Delay on=0 · Delay off=End of Tension Phase Delay [ms]
- Logique :
  - **Activating** = `NegativeFlank(Super Ok tension)`
- Lit : `End of Tension Phase Delay`, `Super Ok tension`
- Utilisé par : `Need Pressure`, `Tension State`
- Ligne export : 65169 · id 91733

#### Tension Error Parameter  `FP`
- Propriétés : Unit=% · Default mode={100}
- Utilisé par : `Over Tension`, `Adjust group: Master Track`, `Single adjust item: Tension Error Parameter`
- Ligne export : 65213 · id 38754

#### Super Ok Tension Math  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `Delay Off super ok tension * 100`
- Lit : `Delay Off super ok tension`
- Utilisé par : `Slope Super Ok`
- Ligne export : 65225 · id 38805

#### Slope Super Ok  `SFC`
- Propriétés : Input channel=Super Ok Tension Math [%] · Enable=Yes · Type=Slopes · Slopes={{5; 1}; {2; 2}}
- Lit : `Super Ok Tension Math`
- Utilisé par : `Over Tension`
- Ligne export : 65268 · id 38813

#### Delay Off super ok tension  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `Super Ok tension`
- Lit : `Super Ok tension`
- Utilisé par : `Super Ok Tension Math`
- Ligne export : 65286 · id 38797

#### Parking  `IP`
- Propriétés : Unit=% · Default mode={50}
- Utilisé par : `PWM Selector`, `Adjust group: Master Track`, `Single adjust item: Parking`
- Ligne export : 65329 · id 60056

#### Wait engine Stop  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=4000
- Logique :
  - **Activating** = `Wait engine start`
- Lit : `Wait engine start`
- Utilisé par : `Tension State`
- Ligne export : 65341 · id 60076

#### Max Tension Pressure  `IP`
- Propriétés : Unit=bar · Default mode={170}
- Utilisé par : `Flag High Pressure Tension`, `Adjust group: Track Setup`, `Single adjust item: Max Tension Pressure`
- Ligne export : 65384 · id 91743

#### Flag High Pressure Tension  `IDC`
> Rised at the end of a tensionning operation
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `Pression Filter [bar] > Max Tension Pressure [bar]`
- Lit : `Max Tension Pressure`, `Pression Filter`
- Utilisé par : `Tension State`
- Ligne export : 65396 · id 91755

#### Tension State  `SMC`
- Propriétés : Default state name=ON/OFF
- Fonction *Parking* :
  - **Activating** = `Wait engine Stop`
  - **Blocking** = `(Wait engine start) OR (Tracks pressure Mode)`
- Fonction *Unthingten* :
  - **Activating** = `Tracks pressure Mode`
- Fonction *End Of Tension* :
  - **Activating** = `(Flag End of tensionning) AND (Flag High Pressure Tension)`
  - **Blocking** = `Tracks pressure Mode`
- Lit : `Flag End of tensionning`, `Flag High Pressure Tension`, `Tracks pressure Mode`, `Wait engine Stop`, `Wait engine start`
- Utilisé par : `PWM Selector`
- Ligne export : 65441 · id 60032

#### PMax derating  `IP`
> Must be adjusted to have a correct tension pressure adjustment
- Propriétés : Unit=% · Default mode={10}
- Utilisé par : `PWM Selector`, `Adjust group: Master Track`, `Single adjust item: PMax derating`
- Ligne export : 65571 · id 90726

#### PWM Selector  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Tension State
- Fonction *ON/OFF* :
  - **Controlling** = `0`
- Fonction *Parking* :
  - **Controlling** = `Parking [%]`
  - **Limiting** = `Passive Tension Pressure Limiter`
- Fonction *Unthingten* :
  - **Controlling** = `100`
  - **Limiting** = `Passive Tension Pressure Limiter`
- Fonction *End Of Tension* :
  - **Controlling** = `PMax derating [%]`
  - **Limiting** = `Passive Tension Pressure Limiter`
- Lit : `PMax derating`, `Parking`, `Passive Tension Pressure Limiter`, `Tension State`
- Utilisé par : `PWM Pression tendeur`, `Measure group: HVLP`
- Ligne export : 65583 · id 60042

#### PWM Pression tendeur  `COUT`
- Propriétés : Bidirectional=No · BWL=0 · Device type=EM21DEÂG12 · Input channel=PWM Selector [%] · Default mode={{0; 900; 250; 250}} · Module=MC42[1] · Module index=0
- Lit : `PWM Selector`
- Utilisé par : `Measure group: Hydraulic`
- Ligne export : 65739 · id 38904

#### Track Tension Error  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Tracks · Text=Try a Calibrating (Setting/Maintenance). Use straight. Contact your service center. · Channel=Track pressure [bar]
- Logique :
  - **Showing** = `Over Tension`
- Lit : `Over Tension`, `Track pressure`
- Utilisé par : *(personne)*
- Ligne export : 65760 · id 38905

#### Passive Tension Pressure Limiter  `DP`
> True If  Circuit as an X100 Passive type pressure limiting valve for Tension Ram
- Propriétés : Default mode={False}
- Utilisé par : `EV Tension Force Open`, `PWM Selector`, `Adjust group: Master Track`, `Single adjust item: Passive Tension Pressure Limiter`
- Ligne export : 65806 · id 94325

#### EV Tension Force Open  `IDC`
> True if untighten mode with a passive Tension Pressure limiting Valve
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Passive Tension Pressure Limiter) AND (Tracks pressure Mode)`
- Lit : `Passive Tension Pressure Limiter`, `Tracks pressure Mode`
- Utilisé par : `Condition motor ON`, `Inter EV By Pass`, `OK UP/DOWN`
- Ligne export : 65819 · id 94333
