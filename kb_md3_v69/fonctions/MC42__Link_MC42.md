# MC42 — Link MC42

7 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Link MC42

#### Speed Input  `APPIN`
- Propriétés : Input channel=Speed Input
- Utilisé par : `SPEED Engine`, `Speed Int`
- Ligne export : 9773 · id 61651

#### UP/DOWN Button Input  `APPIN`
- Propriétés : Input channel=UP/DOWN Button
- Lit : `UP/DOWN Button`
- Utilisé par : `MD3 - DOWN`, `MD3 - UP`
- Ligne export : 9782 · id 61653

#### State Up/Down  `APPIN`
- Propriétés : Input channel=State Up/Down · Error value=0
- Lit : `State Up/Down`
- Utilisé par : `Up/DOWN STATE`
- Ligne export : 9791 · id 61654

#### Free Input  `APPIN`
- Propriétés : Input channel=IDC Speed Free
- Lit : `IDC Speed Free`
- Utilisé par : `IDC Free`
- Ligne export : 9801 · id 61658

#### OK UP/DOWN  `APPOUT`
- Propriétés : Input channel=OK UP/DOWN · Send method=On change · Transmit rate=1000
- Lit : `OK UP/DOWN`
- Utilisé par : `OK UP/DOWN Input`
- Ligne export : 9810 · id 61659

#### Wait_Very_Low_Oil_Level  `APPOUT`
- Propriétés : Input channel=Wait_Very_Low_Oil_Level · Send method=On change · Transmit rate=1000
- Lit : `Wait_Very_Low_Oil_Level`
- Utilisé par : `Oil Security Activation`, `Oil level Very Low Input`, `Event log: Hydraulic Event`, `MD3 page: BASE`, `Statistics log: Thermic Stats`
- Ligne export : 9821 · id 61661

#### System Started  `APPOUT`
- Propriétés : Input channel=System Started DELAYS · Send method=On change · Transmit rate=1000
- Lit : `System Started DELAYS`
- Utilisé par : `ENGINE RUN Input`
- Ligne export : 9832 · id 61662
