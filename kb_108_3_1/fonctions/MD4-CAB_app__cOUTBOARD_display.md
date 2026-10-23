# MD4-CAB app — cOUTBOARD display

3 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## cOUTBOARD display

#### Gauge Page IDC  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=2000
- Logique :
  - **Activating** = `Engine RUN FAST - NMEA`
  - **Blocking** = `Be6 Engines READY for 45 c10`
- Lit : `Be6 Engines READY for 45 c10`, `Engine RUN FAST - NMEA`
- Utilisé par : `Hide Gauge Page`, `Show Gauge Page`
- Ligne export : 111073 · id 221293

#### Show Gauge Page  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank(Gauge Page IDC)`
- Lit : `Gauge Page IDC`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 111123 · id 221302

#### Hide Gauge Page  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank(Gauge Page IDC)`
- Lit : `Gauge Page IDC`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 111167 · id 221310
