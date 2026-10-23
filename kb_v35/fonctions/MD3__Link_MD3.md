# MD3 — Link MD3

14 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Link MD3

#### MDGN-Status:MD3[0]  `MDGN`
- Propriétés : Value=Module status · Module=MD3[0] · Module index=0
- Utilisé par : `MD3 State`, `MDGN-Status:MD3[0]`
- Ligne export : 9792 · id 54525

#### Drive Type  `APPIN`
- Propriétés : Input channel=Drive Type
- Lit : `Drive Type`
- Utilisé par : `Drive Type`, `Is_Electric_MD3`, `Is_Thermic_MD3`, `Stop To Move`, `Adjust group: Master Config`, `Single adjust item: Drive Type`
- Ligne export : 9803 · id 61672

#### Drive Type  `SP`
- Propriétés : Input channel=Drive Type · Default state name=Thermique · States={Electric}
- Lit : `Drive Type`
- Utilisé par : `Drive Type`, `Is_Electric_MD3`, `Is_Thermic_MD3`, `Stop To Move`, `Adjust group: Master Config`, `Single adjust item: Drive Type`
- Ligne export : 9812 · id 56279

#### Is_Thermic_MD3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Drive Type = 0`
- Lit : ``, `Drive Type`
- Utilisé par : `Show_Thermic`
- Ligne export : 9824 · id 56298

#### Is_Electric_MD3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Drive Type = 1`
- Lit : ``, `Drive Type`
- Utilisé par : `Show_Elec`, `Adjust group: Master Charger`
- Ligne export : 9869 · id 56306

#### Speed Input  `APPOUT`
- Propriétés : Input channel=Speed State · Send method=On change · Transmit rate=1000
- Lit : `Speed State`
- Utilisé par : *(personne)*
- Ligne export : 9914 · id 61642

#### State Up/Down  `APPOUT`
- Propriétés : Input channel=State Up/Down · Send method=On change · Transmit rate=1000
- Lit : `State Up/Down`
- Utilisé par : *(personne)*
- Ligne export : 9925 · id 61644

#### IDC Speed Free  `APPOUT`
- Propriétés : Input channel=IDC Speed Free · Send method=On change · Transmit rate=1000
- Lit : `IDC Speed Free`
- Utilisé par : `Free Input`
- Ligne export : 9936 · id 61645

#### UP/DOWN Button  `APPOUT`
- Propriétés : Input channel=UP/DOWN Button · Send method=On change · Transmit rate=1000
- Lit : `UP/DOWN Button`
- Utilisé par : `UP/DOWN Button Input`
- Ligne export : 9947 · id 61646

#### MDGN-Status:MD3[0]  `APPOUT`
- Propriétés : Input channel=MDGN-Status:MD3[0] · Send method=On change · Transmit rate=1000
- Lit : `MDGN-Status:MD3[0]`
- Utilisé par : `MD3 State`
- Ligne export : 9958 · id 61648

#### F4 Speed Free  `APPOUT`
- Propriétés : Input channel=F4 Speed Free · Send method=On change · Transmit rate=1000
- Lit : `F4 Speed Free`
- Utilisé par : `F4 Input`, `MD3 page: BASE`
- Ligne export : 9969 · id 61650

#### OK UP/DOWN Input  `APPIN`
- Propriétés : Input channel=OK UP/DOWN
- Lit : `OK UP/DOWN`
- Utilisé par : `UP/DOWN Choice`
- Ligne export : 9980 · id 61668

#### Oil level Very Low Input  `APPIN`
- Propriétés : Input channel=Wait_Very_Low_Oil_Level
- Lit : `Wait_Very_Low_Oil_Level`
- Utilisé par : `OK Buz Oil`
- Ligne export : 9989 · id 61669

#### ENGINE RUN Input  `APPIN`
- Propriétés : Input channel=System Started
- Lit : `System Started`
- Utilisé par : `ENGINE RUN`, `ENGINE RUN`, `Run Engine Statut`
- Ligne export : 9998 · id 61670
