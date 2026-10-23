# MC42 — Link MC42

10 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Link MC42

#### Speed Input  `APPIN`
- Propriétés : Input channel=Speed Input
- Utilisé par : `SPEED Engine`, `Speed Int`
- Ligne export : 10112 · id 61651

#### UP/DOWN Button Input  `APPIN`
- Propriétés : Input channel=UP/DOWN Button
- Lit : `UP/DOWN Button`
- Utilisé par : `MD3 - DOWN`, `MD3 - UP`
- Ligne export : 10121 · id 61653

#### State Up/Down  `APPIN`
- Propriétés : Input channel=State Up/Down · Error value=0
- Lit : `State Up/Down`
- Utilisé par : `Up/DOWN STATE`
- Ligne export : 10130 · id 61654

#### MD3 State  `APPIN`
- Propriétés : Input channel=MDGN-Status:MD3[0] · Error value=0
- Lit : `MDGN-Status:MD3[0]`
- Utilisé par : `PARKER OK`
- Ligne export : 10140 · id 61655

#### F4 Input  `APPIN`
- Propriétés : Input channel=F4 Speed Free
- Lit : `F4 Speed Free`
- Utilisé par : `F4 Off`
- Ligne export : 10150 · id 61656

#### Free Input  `APPIN`
- Propriétés : Input channel=IDC Speed Free
- Lit : `IDC Speed Free`
- Utilisé par : `IDC Free`
- Ligne export : 10159 · id 61658

#### OK UP/DOWN  `APPOUT`
- Propriétés : Input channel=OK UP/DOWN · Send method=On change · Transmit rate=1000
- Lit : `OK UP/DOWN`
- Utilisé par : `OK UP/DOWN Input`
- Ligne export : 10168 · id 61659

#### Wait_Very_Low_Oil_Level  `APPOUT`
- Propriétés : Input channel=Wait_Very_Low_Oil_Level · Send method=On change · Transmit rate=1000
- Lit : `Wait_Very_Low_Oil_Level`
- Utilisé par : `Oil Not Good`, `Oil Security Activation`, `Oil level Very Low Input`, `SÃ©curitÃ© hydraulique`, `Event log: Hydraulic Event`, `MD3 page: BASE`, `Statistics log: Thermic Stats`
- Ligne export : 10179 · id 61661

#### System Started  `APPOUT`
- Propriétés : Input channel=System Started · Send method=On change · Transmit rate=1000
- Lit : `System Started`
- Utilisé par : `10 minutes auto tender`, `ENGINE RUN Input`, `Over Tension`, `SARTING`, `Thermic Engine STATE`, `Wait engine start`
- Ligne export : 10190 · id 61662

#### Drive Type  `APPOUT`
- Propriétés : Input channel=Drive Type · Send method=On change · Transmit rate=1000
- Lit : `Drive Type`
- Utilisé par : `Adjust group: Master Config`, `Single adjust item: Drive Type`
- Ligne export : 10201 · id 61663
