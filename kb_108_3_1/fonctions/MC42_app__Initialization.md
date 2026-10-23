# MC42 app — Initialization

7 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Initialization

#### CAN Speed B mc  `SP`
- Propriétés : Input channel=None · Default state name=500 elec · States={125 cab keybox; 250 thermal engine}
- Utilisé par : `Can Speed B`, `Single adjust item: CAN B Speed`
- Ligne export : 54 · id 202842

#### Can Speed B  `IP`
- Propriétés : Unit=kbps · Mode selector=CAN Speed B mc · Default mode: 500 elec={500} · Mode 1: 125 cab keybox={125} · Mode 2: 250 thermal engine={250}
- Lit : `CAN Speed B mc`
- Utilisé par : *(personne)*
- Ligne export : 67 · id 202844

#### Drive Type mc  `SP`
> Reboot to take effect
- Propriétés : Input channel=None · Default state name=Electric · States={Fossil}
- Utilisé par : `4E Time Sleep engine`, `4et.Is_Electric`, `4et.Is_Thermic`, `EV By pass Sel`, `EV Down Sel`, `EV Lock Sel`, `EV Tension Sel`, `EV UnBlock Sel`, `EV Up Sel`, `Is_Electric mc`, `Is_Electric_x100 mc`, `Is_Thermic mc`, `create new state tyva elec`, `Single adjust item: Drive Type`
- Ligne export : 83 · id 202379

#### is_cab_mc  `DP`
> Reboot to take effect
- Propriétés : Default mode={False}
- Utilisé par : `is_cab or joy_mc42`, `is_cab_math`, `is_x100_mc`, `sel thermic or cab`, `Active le groupe: logic screen c10 and KB / Keyboxs CAB`, `Active le groupe: logic screen c10 and KB / cEQUIPEMENT`, `Active le groupe: logic screen c10 and KB / mc.Accesory i/o CAB`, `Adjust group: Master Config Options`, `Adjust group: Setup Outboard`, `Measure group: Translation`, `Single adjust item: Demisting option`, `Single adjust item: Is_Cab_mc`, `Single adjust item: Joystick plugged md10`, `Single adjust item: Reset Ladder Sensor when UP`, `Single adjust item: a/c option`, `Single adjust item: electronic seat`, `Single adjust item: md4 Water Level Protection`
- Ligne export : 95 · id 169624

#### CAN Speed C mc  `SP`
- Propriétés : Input channel=None · Default state name=500 · States={125 Prog Keybox x100}
- Utilisé par : `Can Speed C`, `Single adjust item: CAN C Speed`
- Ligne export : 108 · id 212581

#### Can Speed C  `IP`
- Propriétés : Unit=kbps · Mode selector=CAN Speed C mc · Default mode: 500={500} · Mode 1: 125 Prog Keybox x100={125}
- Lit : `CAN Speed C mc`
- Utilisé par : *(personne)*
- Ligne export : 120 · id 212583

#### 4ET Timer UP/DOWN  `IP`
> boat16 need more 20s
- Propriétés : Unit=s · Default mode={20}
- Utilisé par : `internal timer UP/DOWN`, `Single adjust item: Timer UP/DOWN`
- Ligne export : 140 · id 214593
