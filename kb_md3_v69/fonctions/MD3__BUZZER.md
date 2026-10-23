# MD3 — BUZZER

13 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## BUZZER

#### UP  `FGI`
- Propriétés : Input type=Digital · Input=Virtual UP · Default state name=Default state
- Lit : `Virtual UP`
- Utilisé par : `OK Buz 2`
- Ligne export : 5774 · id 8831

#### TRACK UP  `FGI`
- Propriétés : Input type=Digital · Input=TRACK UP · Default state name=Default state
- Lit : `TRACK UP`
- Utilisé par : `OK Buz 2`
- Ligne export : 5785 · id 8833

#### DOWN  `FGI`
- Propriétés : Input type=Digital · Input=Virtual DOWN · Default state name=Default state
- Lit : `Virtual DOWN`
- Utilisé par : `OK Buz`
- Ligne export : 5796 · id 8829

#### TRACK DOWN  `FGI`
- Propriétés : Input type=Digital · Input=TRACK DOWN · Default state name=Default state
- Lit : `TRACK DOWN`
- Utilisé par : `Auto Fast after Down`, `OK Buz`, `Ok to move`
- Ligne export : 5807 · id 8827

#### DOWN Super  `FGI`
- Propriétés : Input type=Digital · Input=Inter DOWN Super Delay · Default state name=Default state
- Lit : `Inter DOWN Super Delay`
- Utilisé par : `OK Buz`
- Ligne export : 5818 · id 20455

#### OK Buz  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `PositiveFlank(DOWN) OR (PositiveFlank(TRACK DOWN)) OR (PositiveFlank(DOWN Super)) OR PositiveFlank(Bip)`
- Lit : ``, `Bip`, `DOWN`, `DOWN Super`, `TRACK DOWN`
- Utilisé par : `Inter Buzzer`
- Ligne export : 5829 · id 8842

#### UP Super  `FGI`
- Propriétés : Input type=Digital · Input=Inter UP Super Delay · Default state name=Default state
- Lit : `Inter UP Super Delay`
- Utilisé par : `OK Buz 2`
- Ligne export : 5897 · id 20510

#### OK Buz 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `PositiveFlank(UP) OR (PositiveFlank(TRACK UP)) OR (PositiveFlank(UP Super))`
- Lit : ``, `TRACK UP`, `UP`, `UP Super`
- Utilisé par : `Inter Buzzer`, `Wait Buz 2`
- Ligne export : 5908 · id 8900

#### Wait Buz 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `NegativeFlank(OK Buz 2)`
- Lit : ``, `OK Buz 2`
- Utilisé par : `OK Buz 3`
- Ligne export : 5968 · id 12854

#### OK Buz 3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `NegativeFlank(Wait Buz 2)`
- Lit : ``, `Wait Buz 2`
- Utilisé par : `Inter Buzzer`
- Ligne export : 6012 · id 9041

#### OK Buz Oil  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `PositiveFlank(Oil level Very Low Input)`
- Lit : ``, `Oil level Very Low Input`
- Utilisé par : `Inter Buzzer`
- Ligne export : 6056 · id 9904

#### Inter Buzzer  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(OK Buz) OR (OK Buz 2) OR (OK Buz 3) OR (OK Buz Oil)`
- Lit : ``, `OK Buz`, `OK Buz 2`, `OK Buz 3`, `OK Buz Oil`
- Utilisé par : `Buzzer`
- Ligne export : 6100 · id 8804

#### Buzzer  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter Buzzer · Module=MD3[0] · Module index=0
- Lit : `Inter Buzzer`
- Utilisé par : *(personne)*
- Ligne export : 6164 · id 8812
