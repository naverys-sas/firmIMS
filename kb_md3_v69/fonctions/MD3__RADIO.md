# MD3 — RADIO

22 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## RADIO — actif seulement si `Remote Control`

#### CAN IN 100  `GFIN`
- Propriétés : Identifier=0x100 · Data length=8 · Timeout=1000 · Paged protocol={Not used} · Parameters={{RadioGauche; 16}; {RadioDroit; 0}; {RadioStop; 32}; {RadioStart; 40}; {RadioSpeed; 48}} · Module=Radio (Generic) · Module index=0
- Lit : `RadioDroit`, `RadioGauche`, `RadioSpeed`, `RadioStart`, `RadioStop`
- Utilisé par : `Timeout radio`
- Ligne export : 3523 · id 7117

#### RadioGauche  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `CAN IN 100`, `RadioGauche%`
- Ligne export : 3554 · id 7118

#### RadioDroit  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `CAN IN 100`, `RadioDroit%`
- Ligne export : 3567 · id 7119

#### RadioStop  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `CAN IN 100`, `RadioStopInter`
- Ligne export : 3580 · id 7120

#### RadioStart  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `CAN IN 100`, `RadioStartInter`
- Ligne export : 3592 · id 7121

#### RadioSpeed  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `CAN IN 100`, `IDC Speed R`, `IDC Speed S`
- Ligne export : 3604 · id 7124

#### Timeout radio  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `True`
  - **Resetting** = `CAN IN 100`
- Lit : ``, `CAN IN 100`
- Utilisé par : `Command State`, `State Latence`
- Ligne export : 3616 · id 7561

#### CAN IN 101  `GFIN`
- Propriétés : Identifier=0x101 · Data length=8 · Timeout=1000 · Paged protocol={Not used} · Parameters={{TimelapsIn [ms]; 32}} · Module=Radio (Generic) · Module index=1
- Lit : `TimelapsIn`
- Utilisé par : *(personne)*
- Ligne export : 3675 · id 7499

#### TimelapsIn  `GPIN`
- Propriétés : Unit=ms · Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `CAN IN 101`, `Latence Math`
- Ligne export : 3694 · id 7500

#### LatenceTimer  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `True`
- Lit : ``
- Utilisé par : `Latence Math`, `TimeLapsOut`
- Ligne export : 3707 · id 7506

#### Latence Math  `MAC`
- Propriétés : Unit=ms · Limiting object group=Signed
- Logique :
  - **Controlling** = `LatenceTimer [ms] - TimelapsIn [ms]`
- Lit : ``, `LatenceTimer`, `TimelapsIn`
- Utilisé par : `Command State`, `State Latence`
- Ligne export : 3759 · id 7553

#### State Latence  `SMC`
- Propriétés : Default state name=Default state
- Fonction *Latence niv 1* :
  - **Activating** = `(Timeout radio [ms] > 500) OR (Latence Math [ms] > 500)`
- Lit : ``, `Latence Math`, `Timeout radio`
- Utilisé par : `RadioDroit%`, `RadioGauche%`
- Ligne export : 3803 · id 7753

#### RadioGauche%  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=State Latence
- Fonction *Default state* :
  - **Controlling** = `(200 * (RadioGauche / 65535)) - 100`
- Fonction *Latence niv 1* :
  - **Controlling** = `0`
- Lit : ``, `RadioGauche`, `State Latence`
- Utilisé par : `Math Gauche`
- Ligne export : 3854 · id 7133

#### RadioDroit%  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=State Latence
- Fonction *Default state* :
  - **Controlling** = `(200 * (RadioDroit / 65535)) - 100`
- Fonction *Latence niv 1* :
  - **Controlling** = `0`
- Lit : ``, `RadioDroit`, `State Latence`
- Utilisé par : `Math Droit`
- Ligne export : 3947 · id 7146

#### Command State  `SMC`
- Propriétés : Default state name=Normal
- Fonction *Radio* :
  - **Activating** = `(Timeout radio [ms] <= 500) AND (Latence Math [ms] <= 500)`
- Lit : ``, `Latence Math`, `Timeout radio`
- Utilisé par : `ALL ASK STOP`, `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `Math Droit`, `Math Gauche`, `RadioMode`
- Ligne export : 4040 · id 7172

#### RadioMode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Command State = 1`
- Lit : ``, `Command State`
- Utilisé par : `MD3 page: BASE`
- Ligne export : 4091 · id 7310

#### RadioStopInter  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `0 < RadioStop`
- Lit : ``, `RadioStop`
- Utilisé par : `ALL ASK STOP`
- Ligne export : 4136 · id 7223

#### RadioStartInter  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `0 < RadioStart`
- Lit : ``, `RadioStart`
- Utilisé par : *(personne)*
- Ligne export : 4181 · id 7227

#### TimeLapsOut  `GPOUT`
- Propriétés : Input value=LatenceTimer [ms] · Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian
- Lit : `LatenceTimer`
- Utilisé par : `CANOUT 102`
- Ligne export : 4226 · id 7501

#### Run Engine Statut  `GPOUT`
- Propriétés : Input value=ENGINE RUN Input · Length=1 Byte (= 8 bits) · Type=Signed integer
- Lit : `ENGINE RUN Input`
- Utilisé par : `CANOUT 102`
- Ligne export : 4238 · id 7552

#### CANOUT 102  `GFOUT`
- Propriétés : Identifier=0x102 · Data length=8 · Send method=Continuously · Transmit rate=100 · Unused bits=Set to 0 · Parameters={{TimeLapsOut [ms]; 32}; {Run Engine Statut; 0}} · Module=Radio (Generic) · Module index=0
- Lit : `Run Engine Statut`, `TimeLapsOut`
- Utilisé par : *(personne)*
- Ligne export : 4249 · id 7502

#### MDGN-S/N:MD3[0]  `MDGN`
- Propriétés : Value=Serial number · Module=MD3[0] · Module index=1
- Utilisé par : *(personne)*
- Ligne export : 4271 · id 21217
