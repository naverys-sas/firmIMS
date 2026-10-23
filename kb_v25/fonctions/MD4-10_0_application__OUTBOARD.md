# MD4-10[0] application — OUTBOARD

3 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## OUTBOARD

#### Gauge Page IDC  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=2000
- Logique :
  - **Activating** = `Engine RUN FAST - NMEA`
  - **Blocking** = `CAN Engine Ready`
- Lit : `CAN Engine Ready`, `Engine RUN FAST - NMEA`
- Utilisé par : `Hide Gauge Page`, `Show Gauge Page`
- Ligne export : 20687 · id 49456

#### Show Gauge Page  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank(Gauge Page IDC)`
- Lit : `Gauge Page IDC`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 20737 · id 49483

#### Hide Gauge Page  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank(Gauge Page IDC)`
- Lit : `Gauge Page IDC`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 20781 · id 49496
