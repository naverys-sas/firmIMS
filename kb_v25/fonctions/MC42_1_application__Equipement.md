# MC42[1] application — Equipement

12 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Equipement

#### REMOTE UP  `DIN`
- Propriétés : Module=MC42[1] · Module index=13
- Utilisé par : `Remote`
- Ligne export : 67746 · id 43512

#### REMOTE DOWN  `DIN`
- Propriétés : Module=MC42[1] · Module index=12
- Utilisé par : `Remote`
- Ligne export : 67756 · id 43511

#### Water Level  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Calibration={3100; 510; 0; 100} · Alarms={No; 0; No; 100} · Module=MC42[1] · Module index=3
- Utilisé par : `Water Level output`, `Adjust group: Master Setup`, `Dual adjust item: Water Level`, `MD4-10 page: FEATURE`, `MD4-10 page: SHUTDOWN`, `Measure group: Hydraulic`
- Ligne export : 67766 · id 43510

#### Remote  `SMC`
- Propriétés : Default state name=NO
- Fonction *UP* :
  - **Activating** = `REMOTE UP`
- Fonction *DOWN* :
  - **Activating** = `REMOTE DOWN`
- Lit : `REMOTE DOWN`, `REMOTE UP`
- Utilisé par : `Remote output`
- Ligne export : 67790 · id 46120

#### Reset Ladder Sensor when UP  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Ladder_Sensor`, `Adjust group: Maintenance`, `Adjust group: Master Setup`, `Single adjust item: Reset Ladder Sensor when UP`
- Ligne export : 67861 · id 53889

#### Ladder_Sensor  `DPCNT`
> Ladder
- Propriétés : Sensor type=Quadrature · Accumulate=Yes · Store value=Yes · Resetting channel=Reset Ladder Sensor when UP · Reset value=0 · Max=1 · Scaled max=1 · Alarms={No; 0; No; 100} · Module=MC42[1] · Module index=0
- Lit : `Reset Ladder Sensor when UP`
- Utilisé par : `Ladder_Sensor`, `Ladder_Sensor output`, `MD4-10 page: SETUP`
- Ligne export : 67874 · id 52431

#### VIN-E:MC42[1]  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Calibration={0; 5000; 0; 100} · Alarms={No; 0; No; 100} · Module=MC42[1] · Module index=4
- Utilisé par : `Convert bilge current`
- Ligne export : 67897 · id 55278

#### Convert bilge current  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Abs((DerivativeOf(VIN-E:MC42[1] [%])))`
- Lit : `VIN-E:MC42[1]`
- Utilisé par : `Convert bilge current Filter`
- Ligne export : 67921 · id 55279

#### Convert bilge current Filter  `SFC`
- Propriétés : Input channel=Convert bilge current · Enable=Yes · Type=Filter · Filter=95
- Lit : `Convert bilge current`
- Utilisé par : `Bilge Pump Run`
- Ligne export : 67972 · id 55288

#### Bilge Pump Run  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `Convert bilge current Filter >= 10`
- Lit : `Convert bilge current Filter`
- Utilisé par : `Bilge Pump Run`
- Ligne export : 67984 · id 55289

#### Bilge Pump Run  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header=Bilge Pump Run · Text=It seems you have water in the bildge.
- Logique :
  - **Showing** = `Bilge Pump Run`
  - **Hiding** = `NegativeFlank(Bilge Pump Run)`
- Lit : `Bilge Pump Run`
- Utilisé par : *(personne)*
- Ligne export : 68029 · id 55297

#### Ladder_Sensor  `IMAC`
- Logique :
  - **Controlling** = `Abs(Ladder_Sensor)`
- Lit : `Ladder_Sensor`
- Utilisé par : `Ladder_Sensor output`, `MD4-10 page: SETUP`
- Ligne export : 68083 · id 75769
