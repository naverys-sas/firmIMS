# MD3 — START PAGE

5 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## START PAGE

#### Can tIMER in  `APPIN`
- Propriétés : Input channel=CAN Out tIMER FAN [%] · Error value=0
- Lit : `CAN Out tIMER FAN`
- Utilisé par : `Show Start`, `Timer to Img`
- Ligne export : 869 · id 10245

#### Show Start  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not((Inside(Can tIMER in [%], 0, 100)))`
- Lit : ``, `Can tIMER in`
- Utilisé par : `Show Timer`
- Ligne export : 879 · id 10270

#### Show Timer  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Show Start)`
- Lit : ``, `Show Start`
- Utilisé par : *(personne)*
- Ligne export : 933 · id 10283

#### Timer to Img  `IMAC`
- Logique :
  - **Controlling** = `Can tIMER in [%] / 15`
- Lit : ``, `Can tIMER in`
- Utilisé par : `Timer to Img`
- Ligne export : 977 · id 10304

#### Timer to Img  `SMC`
- Propriétés : Default state name=Default state
- Fonction *0* :
  - **Activating** = `Timer to Img = 0`
- Fonction *1* :
  - **Activating** = `Timer to Img = 1`
- Fonction *2* :
  - **Activating** = `Timer to Img = 2`
- Fonction *3* :
  - **Activating** = `Timer to Img = 3`
- Fonction *4* :
  - **Activating** = `Timer to Img = 4`
- Fonction *5* :
  - **Activating** = `Timer to Img = 5`
- Fonction *6* :
  - **Activating** = `Timer to Img = 6`
- Fonction *7* :
  - **Activating** = `Timer to Img = 7`
- Lit : ``, `Timer to Img`
- Utilisé par : *(personne)*
- Ligne export : 1020 · id 10300
