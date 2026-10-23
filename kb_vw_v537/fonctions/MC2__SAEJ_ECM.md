# MC2 — SAEJ ECM

25 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## SAEJ ECM — actif seulement si `Engine START`

#### DM1  `DM1IN`
> Diagnostic Message 1
- Propriétés : SPN conversion method=4 · FMI texts={OK; Above normal, most severe; Below normal, most severe; Erratic or intermittent; Voltage above normal; Voltage below normal; Current below normal; Current above normal; Out of adjustment; Abnormal frequency; Abnormal update rate; Abnormal rate of change; Root cause not known; Bad component; Out of calibration; Special instructions; Above normal; Above normal, severe; Below normal; Below normal, severe; Received data in error; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Reserved; Not available} · Show message=All · Dialog for undefined SPNs=Yes · Enable DM2 support=False · Enable lamp flash=No · Parameters={SPN 98; SPN 100; SPN 102; SPN 105; SPN 106; SPN 110; SPN 175; SPN 626; SPN 629; SPN 636; SPN 637; SPN 639; SPN 651; SPN 652; SPN 653; SPN 654; SPN 655; SPN 656; SPN 677; SPN 1485} · Module=J1939[0] · Module index=0
- Lit : `SPN 100`, `SPN 102`, `SPN 105`, `SPN 106`, `SPN 110`, `SPN 1485`, `SPN 175`, `SPN 626`, `SPN 629`, `SPN 636`, `SPN 637`, `SPN 639`, `SPN 651`, `SPN 652`, `SPN 653`, `SPN 654`, `SPN 655`, `SPN 656`, `SPN 677`, `SPN 98`
- Utilisé par : *(personne)*
- Ligne export : 13680 · id 3340

#### SPN 629  `SPN`
> Controller #1
- Propriétés : SPN=629 · Dialog priority=Critical · Failures={{8; ErrNo 186 DTC 9.9: CPU Watchdog reset test failure.}; {13; ErrNo 186 DTC 9.9: Watchdog trip failure.}; {2; ErrNo 187 DTC 9.9: RAM cell test failure.}; {12; ErrNo 187 DTC 9.9: RAM address test failure.}; {11; ErrNo 186 DTC 9.9: Main and Fueling ASIC test fail.}}
- Utilisé par : `DM1`
- Ligne export : 13750 · id 3341

#### SPN 100  `SPN`
> Engine Oil Pressure
- Propriétés : SPN=100 · Dialog priority=Warning · Failures={{3; ErrNo 181 DTC 3.1: Voltage above normal.}; {4; ErrNo 182 DTC 3.1: Voltage below normal.}; {1; ErrNo 180 DTC 6.6: Data valid but below normal.}}
- Utilisé par : `DM1`
- Ligne export : 13776 · id 3342

#### SPN 110  `SPN`
> Engine Coolant Temperature
- Propriétés : SPN=110 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 13796 · id 3343

#### SPN 105  `SPN`
> Air Intake Manifold 1 Temperature
- Propriétés : SPN=105 · Dialog priority=Warning · Failures={{3; ErrNo 25 DTC 3.2: Voltage above normal.}; {4; ErrNo 26 DTC 3.2: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 13816 · id 3344

#### SPN 175  `SPN`
> Engine Oil Temperature 1
- Propriétés : SPN=175 · Dialog priority=Critical · Failures={{3; ErrNo 184 DTC 3.7: Voltage above normal.}; {4; ErrNo 185 DTC 3.7: Voltage below normal.}; {0; ErrNo 183 DTC 5.8: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 13836 · id 3345

#### SPN 102  `SPN`
> Boost Pressure
- Propriétés : SPN=102 · Dialog priority=Warning · Failures={{3; ErrNo 67 DTC 3.4: Voltage above normal.}; {4; ErrNo 68 DTC 3.4: Voltage below normal.}; {0; ErrNo 57 DTC -.-: Data valid but above normal.}; {1; ErrNo 58 DTC -.-: Data valid but below normal.}}
- Utilisé par : `DM1`
- Ligne export : 13856 · id 3346

#### SPN 1485  `SPN`
> ECU Main relay
- Propriétés : SPN=1485 · Dialog priority=Warning · Failures={{3; ErrNo 43 DTC 5.1: Short circuit high.}}
- Utilisé par : `DM1`
- Ligne export : 13879 · id 3347

#### SPN 637  `SPN`
> Timing sensor
- Propriétés : SPN=637 · Dialog priority=Warning · Failures={{8; ErrNo 18 DTC 2.4: Extra pulses.}; {2; ErrNo 101 DTC 2.4: Intermittent loss of signal.}; {3; ErrNo 18 DTC 2.4: Permanent loss of signal.}}
- Utilisé par : `DM1`
- Ligne export : 13893 · id 3348

#### SPN 656  `SPN`
> Injector Cylinder #06
- Propriétés : SPN=656 · Dialog priority=Warning · Failures={{2; ErrNo 160 DTC 7.6: Short circuit High Side to Vbatt.}; {4; ErrNo 161 DTC 7.6: Short circuit High or Low Side to ground.}; {3; ErrNo 162 DTC 7.6: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 165 DTC 7.6: Open circuit.}; {11; ErrNo 163 DTC 7.6: Unknown Error.}; {7; ErrNo 164 DTC 7.6: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 13913 · id 3349

#### SPN 636  `SPN`
> f
- Propriétés : SPN=636 · Dialog priority=Critical · Failures={{8; ErrNo 103 DTC 2.5: Extra pulses or high frequency signal.}; {3; ErrNo 102 DTC 2.5: Permanent loss of signal.}}
- Utilisé par : `DM1`
- Ligne export : 13942 · id 3350

#### SPN 626  `SPN`
> Start enable device - Devices that assist an engine in starting - e.g. intake heaters and ether
- Propriétés : SPN=626 · Dialog priority=Warning · Failures={{3; ErrNo 76 DTC 5.4: Voltage above normal.}; {4; ErrNo 75 DTC 5.4: Voltage below normal.}; {5; ErrNo 74 DTC 5.4: Current below normal.}}
- Utilisé par : `DM1`
- Ligne export : 13959 · id 3351

#### SPN 677  `SPN`
> Engine Starter Motor Relay
- Propriétés : SPN=677 · Dialog priority=Warning · Failures={{3; ErrNo 41 DTC 4.6: Short circuit high.}; {4; ErrNo 42 DTC 4.6: Short circuit low.}; {5; ErrNo 107 DTC 4.6: Open circuit.}}
- Utilisé par : `DM1`
- Ligne export : 13979 · id 3352

#### SPN 655  `SPN`
> Injector Cylinder #05
- Propriétés : SPN=655 · Dialog priority=Warning · Failures={{2; ErrNo 150 DTC 7.5: Short circuit High Side to Vbatt.}; {4; ErrNo 151 DTC 7.5: Short circuit High or Low Side to ground.}; {3; ErrNo 152 DTC 7.5: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 155 DTC 7.5: Open circuit.}; {11; ErrNo 153 DTC 7.5: Unknown Error.}; {7; ErrNo 154 DTC 7.5: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 13999 · id 3353

#### SPN 654  `SPN`
> Injector Cylinder #04
- Propriétés : SPN=654 · Dialog priority=Warning · Failures={{2; ErrNo 140 DTC 7.4: Short circuit High Side to Vbatt.}; {4; ErrNo 141 DTC 7.4: Short circuit High or Low Side to ground.}; {3; ErrNo 142 DTC 7.4: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 145 DTC 7.4: Open circuit.}; {11; ErrNo 143 DTC 7.4: Unknown Error.}; {7; ErrNo 144 DTC 7.4: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 14028 · id 3354

#### SPN 653  `SPN`
> Injector Cylinder #03
- Propriétés : SPN=653 · Dialog priority=Warning · Failures={{2; ErrNo 130 DTC 7.3: Short circuit High Side to Vbatt.}; {4; ErrNo 131 DTC 7.3: Short circuit High or Low Side to ground.}; {3; ErrNo 132 DTC 7.3: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 135 DTC 7.3: Open circuit.}; {11; ErrNo 133 DTC 7.3: Unknown Error.}; {7; ErrNo 134 DTC 7.3: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 14057 · id 3355

#### SPN 652  `SPN`
> Injector Cylinder #02
- Propriétés : SPN=652 · Dialog priority=Warning · Failures={{2; ErrNo 120 DTC 7.2: Short circuit High Side to Vbatt.}; {4; ErrNo 121 DTC 7.2: Short circuit High or Low Side to ground.}; {3; ErrNo 122 DTC 7.2: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 125 DTC 7.2: Open circuit.}; {11; ErrNo 123 DTC 7.2: Unknown Error.}; {7; ErrNo 124 DTC 7.2: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 14086 · id 3356

#### SPN 651  `SPN`
> Injector Cylinder #01
- Propriétés : SPN=651 · Dialog priority=Warning · Failures={{2; ErrNo 110 DTC 7.1: Short circuit High Side to Vbatt.}; {4; ErrNo 111 DTC 7.1: Short circuit High or Low Side to ground.}; {3; ErrNo 112 DTC 7.1: Short circuit High Side to Low Side or Low Side to Vbatt.}; {5; ErrNo 115 DTC 7.1: Open circuit.}; {11; ErrNo 113 DTC 7.1: Unknown Error.}; {7; ErrNo 114 DTC 7.1: Cylinder balancing error.}}
- Utilisé par : `DM1`
- Ligne export : 14115 · id 3357

#### SPN 639  `SPN`
> J1939 Network #1, Primary Vehicle Network
- Propriétés : SPN=639 · Dialog priority=Warning · Failures={{2; ErrNo 106 DTC 6.5: Bus Off error.}; {9; ErrNo 106 DTC 6.5: Passive bus error.}; {12; ErrNo 38 DTC 6.5: Loss of message error.}; {11; ErrNo 38 DTC 6.5: Data registers read back failure.}}
- Utilisé par : `DM1`
- Ligne export : 14144 · id 3358

#### Malfunction lamp  `MDGN`
- Propriétés : Value=Module status · Module=J1939[0] · Module index=0
- Utilisé par : *(personne)*
- Ligne export : 14167 · id 3359

#### Red stop lamp  `MDGN`
- Propriétés : Value=Module status · Module=J1939[0] · Module index=0
- Utilisé par : *(personne)*
- Ligne export : 14178 · id 3360

#### Amber warning lamp  `MDGN`
- Propriétés : Value=Module status · Module=J1939[0] · Module index=0
- Utilisé par : *(personne)*
- Ligne export : 14189 · id 3361

#### Protect lamp  `MDGN`
- Propriétés : Value=Module status · Module=J1939[0] · Module index=0
- Utilisé par : *(personne)*
- Ligne export : 14200 · id 3362

#### SPN 98  `SPN`
> Engine oil level
- Propriétés : SPN=98 · Dialog priority=Critical · Failures={{3; ErrNo 27 DTC 3.3: Voltage above normal.}; {4; ErrNo 28 DTC 3.3: Voltage below normal.}; {0; ErrNo 31 DTC 6.1: Data valid but above normal.}}
- Utilisé par : `DM1`
- Ligne export : 14211 · id 3363

#### SPN 106  `SPN`
- Propriétés : SPN=106 · Dialog priority=Dont show · Failures={{4; MAP Voltage Low}}
- Utilisé par : `DM1`
- Ligne export : 14231 · id 11165
