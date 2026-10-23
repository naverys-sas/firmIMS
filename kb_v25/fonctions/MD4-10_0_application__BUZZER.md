# MD4-10[0] application — BUZZER

17 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## BUZZER

#### UP  `FGI`
- Propriétés : Input type=Digital · Input=Virtual UP · Default state name=Default state
- Lit : `Virtual UP`
- Utilisé par : `OK Buz 2`
- Ligne export : 4794 · id 41723

#### TRACK UP  `FGI`
- Propriétés : Input type=Digital · Input=TRACK UP · Default state name=Default state
- Lit : `TRACK UP`
- Utilisé par : `OK Buz 2`
- Ligne export : 4805 · id 41724

#### DOWN  `FGI`
- Propriétés : Input type=Digital · Input=Virtual DOWN · Default state name=Default state
- Lit : `Virtual DOWN`
- Utilisé par : `OK Buz`
- Ligne export : 4816 · id 41725

#### Auto DOWN  `FGI`
- Propriétés : Input type=Digital · Input=Inter DOWN Super Delay · Default state name=Default state
- Lit : `Inter DOWN Super Delay`
- Utilisé par : `OK Buz`
- Ligne export : 4827 · id 41727

#### OK Buz  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=150
- Logique :
  - **Activating** = `PositiveFlank(DOWN) OR (PositiveFlank(TRACK DOWN)) OR (PositiveFlank(Auto DOWN)) OR (PositiveFlank(Bip Road Cruise))`
- Lit : `Auto DOWN`, `Bip Road Cruise`, `DOWN`, `TRACK DOWN`
- Utilisé par : `Inter Buzzer`
- Ligne export : 4838 · id 41729

#### Auto UP  `FGI`
- Propriétés : Input type=Digital · Input=Inter UP Super Delay · Default state name=Default state
- Lit : `Inter UP Super Delay`
- Utilisé par : `OK Buz 2`
- Ligne export : 4906 · id 41742

#### OK Buz 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=150
- Logique :
  - **Activating** = `PositiveFlank(UP) OR (PositiveFlank(TRACK UP)) OR (PositiveFlank(Auto UP)) OR (PositiveFlank(Ladder Error Msg))`
- Lit : `Auto UP`, `Ladder Error Msg`, `TRACK UP`, `UP`
- Utilisé par : `Inter Buzzer`, `Wait Buz 2`
- Ligne export : 4917 · id 41743

#### Wait Buz 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `NegativeFlank(OK Buz 2)`
- Lit : `OK Buz 2`
- Utilisé par : `Ladder is not up - Buzz 2`, `Ladder is not up - Buzz 3`, `OK Buz 3`
- Ligne export : 4985 · id 41755

#### OK Buz 3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=150
- Logique :
  - **Activating** = `NegativeFlank(Wait Buz 2)`
- Lit : `Wait Buz 2`
- Utilisé par : `Inter Buzzer`
- Ligne export : 5029 · id 41763

#### Ladder is not up  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Ladder Position [%] > 5) AND (Tracks Button) AND (not(Joystick to zero))`
- Lit : `Joystick to zero`, `Ladder Position`, `Tracks Button`
- Utilisé par : `Ladder is not up - Buzz 1`
- Ligne export : 5073 · id 48756

#### Ladder is not up - Buzz 1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=150
- Logique :
  - **Activating** = `PositiveFlank(Ladder is not up)`
- Lit : `Ladder is not up`
- Utilisé par : `Inter Buzzer`, `Wait Buz 2`
- Ligne export : 5133 · id 49526

#### Wait Buz 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=50
- Logique :
  - **Activating** = `NegativeFlank(Ladder is not up - Buzz 1)`
- Lit : `Ladder is not up - Buzz 1`
- Utilisé par : `Ladder is not up - Buzz 2`, `Ladder is not up - Buzz 3`, `OK Buz 3`
- Ligne export : 5177 · id 54468

#### Ladder is not up - Buzz 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=150
- Logique :
  - **Activating** = `NegativeFlank(Wait Buz 2)`
- Lit : `Wait Buz 2`
- Utilisé par : `Inter Buzzer`, `Wait Buz 2`
- Ligne export : 5221 · id 54476

#### Wait Buz 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=50
- Logique :
  - **Activating** = `NegativeFlank(Ladder is not up - Buzz 2)`
- Lit : `Ladder is not up - Buzz 2`
- Utilisé par : `Ladder is not up - Buzz 2`, `Ladder is not up - Buzz 3`, `OK Buz 3`
- Ligne export : 5265 · id 54506

#### Ladder is not up - Buzz 3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=150
- Logique :
  - **Activating** = `NegativeFlank(Wait Buz 2)`
- Lit : `Wait Buz 2`
- Utilisé par : `Inter Buzzer`
- Ligne export : 5309 · id 54514

#### Inter Buzzer  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(OK Buz) OR (OK Buz 2) OR (OK Buz 3) OR (Ladder is not up - Buzz 1) OR (Ladder is not up - Buzz 2) OR (Ladder is not up - Buzz 3)`
- Lit : `Ladder is not up - Buzz 1`, `Ladder is not up - Buzz 2`, `Ladder is not up - Buzz 3`, `OK Buz`, `OK Buz 2`, `OK Buz 3`
- Utilisé par : `Buzzer`
- Ligne export : 5353 · id 41771

#### Buzzer  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter Buzzer · Module=MD4-10[0] · Module index=0
- Lit : `Inter Buzzer`
- Utilisé par : *(personne)*
- Ligne export : 5431 · id 41781
