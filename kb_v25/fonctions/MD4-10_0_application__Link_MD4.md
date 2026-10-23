# MD4-10[0] application — Link MD4

25 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Link MD4

#### MDGN-Status:MD3[0]  `MDGN`
- Propriétés : Value=Module status · Module=MD4-10[0] · Module index=0
- Utilisé par : `MD4-10 Status CAN In`, `MDGN-Status:MD3[0]`
- Ligne export : 2116 · id 75690

#### Need Charge output  `APPOUT`
- Propriétés : Input channel=Need Charge · Send method=On change · Transmit rate=1000
- Lit : `Need Charge`
- Utilisé par : `Need Charge Input`
- Ligne export : 2127 · id 84760

#### Power Down State output  `APPOUT`
- Propriétés : Input channel=Power Down State · Send method=On change · Transmit rate=1000
- Lit : `Power Down State`
- Utilisé par : `Power Down Input`
- Ligne export : 2138 · id 84762

#### MDGN-Status:MD3[0]  `APPOUT`
- Propriétés : Input channel=MDGN-Status:MD3[0] · Send method=On change · Transmit rate=1000
- Lit : `MDGN-Status:MD3[0]`
- Utilisé par : `MD4-10 Status CAN In`
- Ligne export : 2149 · id 84763

#### Seat Front/Back MAC output  `APPOUT`
- Propriétés : Input channel=Seat Front/Back MAC · Send method=On change · Transmit rate=1000
- Lit : `Seat Front/Back MAC`
- Utilisé par : `Seat Front Back Input`
- Ligne export : 2160 · id 84764

#### Seat UP/DOWN MAC output  `APPOUT`
- Propriétés : Input channel=Seat UP/DOWN MAC · Send method=On change · Transmit rate=1000
- Lit : `Seat UP/DOWN MAC`
- Utilisé par : `Seat UP/DOWN Input`
- Ligne export : 2171 · id 84765

#### Speed output  `APPOUT`
- Propriétés : Input channel=Speed · Send method=On change · Transmit rate=1000
- Lit : `Speed`
- Utilisé par : `CAN Speed Input`
- Ligne export : 2182 · id 84766

#### F4 Free output  `APPOUT`
- Propriétés : Input channel=F4 Free · Send method=On change · Transmit rate=1000
- Lit : `F4 Free`
- Utilisé par : `CAN Free`
- Ligne export : 2193 · id 84767

#### State Up/Down output  `APPOUT`
- Propriétés : Input channel=State Up/Down [%] · Send method=On change · Transmit rate=1000
- Lit : `State Up/Down`
- Utilisé par : `CAN IN State Up/Down`
- Ligne export : 2204 · id 84768

#### UP/DOWN Button output  `APPOUT`
- Propriétés : Input channel=UP/DOWN Button · Send method=On change · Transmit rate=1000
- Lit : `UP/DOWN Button`
- Utilisé par : `UP/DOWN Button Input`
- Ligne export : 2215 · id 84787

#### CAN Engine Ready  `APPIN`
- Propriétés : Input channel=Engines Ready output
- Lit : `Engines Ready output`
- Utilisé par : `Engine READY`, `Gauge Page IDC`, `Run Engine Statut`
- Ligne export : 2226 · id 84801

#### FAN OUT  `APPIN`
- Propriétés : Input channel=FAN OUT output
- Lit : `FAN OUT output`
- Utilisé par : `KTC K4 IDC - Water Cooling`, `Statistics log: Stat Log`
- Ligne export : 2235 · id 84803

#### PUMP OUT  `APPIN`
- Propriétés : Input channel=PUMP VAR output
- Lit : `PUMP VAR output`
- Utilisé par : `KTC K5 IDC - Pump Water`
- Ligne export : 2244 · id 84804

#### Joystick to zero  `APPIN`
- Propriétés : Input channel=Joystick to zero output
- Lit : `Joystick to zero output`
- Utilisé par : `Ladder is not up`, `Stop To Move`
- Ligne export : 2253 · id 84805

#### OK UP/DOWN  `APPIN`
- Propriétés : Input channel=OK UP/DOWN output
- Lit : `OK UP/DOWN output`
- Utilisé par : `UP/DOWN Choice`
- Ligne export : 2262 · id 84806

#### Ladder Sensor  `APPIN`
- Propriétés : Input channel=Ladder_Sensor output · Error value=0
- Lit : `Ladder_Sensor output`
- Utilisé par : `Ladder Position`, `Speed Mouvement`
- Ligne export : 2271 · id 84807

#### Water Level  `APPIN`
- Propriétés : Input channel=Water Level output [%] · Error value=0
- Lit : `Water Level output`
- Utilisé par : `LOW Level`, `Adjust group: Master Setup`, `Dual adjust item: Water Level`, `MD4-10 page: FEATURE`, `MD4-10 page: SHUTDOWN`, `Measure group: Hydraulic`
- Ligne export : 2281 · id 84808

#### Charger Charging State  `APPIN`
- Propriétés : Input channel=Charger State Finite
- Lit : `Charger State Finite`
- Utilisé par : `Charger Charging IDC`, `Charger Connected`, `Charger End Charge`, `Enable A/C StartCharge`, `Enable A/C StopCharge`
- Ligne export : 2291 · id 84809

#### Remote Status  `APPIN`
- Propriétés : Input channel=Remote output
- Lit : `Remote output`
- Utilisé par : `Press Remote`, `Remote`, `Remote Ask Stop`
- Ligne export : 2300 · id 84810

#### Send  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Message`, `MD4-10 page: SERVICE`
- Ligne export : 2309 · id 84932

#### Message  `IMSG`
- Propriétés : Show message=All · Dialog type=Confirmation · Header=Do you want send this message ? · Right button=Send
- Logique :
  - **Showing** = `Send`
- Lit : `Send`
- Utilisé par : `Send message`
- Ligne export : 2319 · id 84943

#### Send message  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `4 = Message`
- Lit : `Message`
- Utilisé par : `Send Message`, `Send message`
- Ligne export : 2367 · id 84947

#### Send message  `APPOUT`
- Propriétés : Input channel=Send message · Send method=On change · Transmit rate=1000
- Lit : `Send message`
- Utilisé par : `Send Message`
- Ligne export : 2412 · id 84953

#### Battery Drive Mode  `APPIN`
- Propriétés : Input channel=Battery DRIVE
- Lit : `Battery DRIVE`
- Utilisé par : `A/C Flag Floating`, `A/C WatchDog`, `A/CBatPackDCDCRelay`, `KBB K7 IDC - AUX 1`, `KTB K12 IDC - Aux 2`, `KTB K2 IDC - AUDIO/AUX 4`, `KTB K3 IDC - VHF/AUX 5`, `KTC K12 IDC - AUX 3`
- Ligne export : 2423 · id 85164

#### Flag NoAUX Mode MD4  `APPIN`
- Propriétés : Input channel=Flag NoAUX Mode
- Lit : `Flag NoAUX Mode`
- Utilisé par : `Enable A/C Float`, `Enable A/C Start Float`
- Ligne export : 2432 · id 91827
