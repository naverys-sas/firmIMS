# MC42[1] application — SEAT

4 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## SEAT

#### Seat UP/DOWN  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `Seat UP/DOWN Input`
- Lit : `Seat UP/DOWN Input`
- Utilisé par : `UP/DOWN`
- Ligne export : 67606 · id 53379

#### UP/DOWN  `PWM`
- Propriétés : Bidirectional=No · BWL=0 · Input channel=Seat UP/DOWN [%] · Default mode={{0; 85; 0; 0}} · Module=MC42[1] · Module index=6
- Lit : `Seat UP/DOWN`
- Utilisé par : *(personne)*
- Ligne export : 67647 · id 43502

#### Seat Front Back  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `Seat Front Back Input`
- Lit : `Seat Front Back Input`
- Utilisé par : `FRONT BACK`, `Adjust group: Seat Setup`, `Single adjust item: Seat Front Back`
- Ligne export : 67668 · id 53392

#### FRONT BACK  `PWM`
- Propriétés : Bidirectional=No · BWL=0 · Input channel=Seat Front Back [%] · Default mode={{0; 85; 0; 0}} · Module=MC42[1] · Module index=9
- Lit : `Seat Front Back`
- Utilisé par : *(personne)*
- Ligne export : 67709 · id 43503
