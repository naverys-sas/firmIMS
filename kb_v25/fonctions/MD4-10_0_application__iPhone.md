# MD4-10[0] application — iPhone

21 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## iPhone — actif seulement si `Remote Control`

#### CAN IN 100  `GFIN`
- Propriétés : Identifier=0x100 · Data length=8 · Timeout=1000 · Paged protocol={Not used} · Parameters={{RadioGauche; 16}; {RadioDroit; 0}; {RadioStop; 32}; {RadioStart; 40}; {RadioSpeed; 48}} · Module=IPhone Remote (Generic) · Module index=1
- Lit : `RadioDroit`, `RadioGauche`, `RadioSpeed`, `RadioStart`, `RadioStop`
- Utilisé par : `Timeout radio`
- Ligne export : 3902 · id 41473

#### RadioGauche  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `CAN IN 100`, `RadioGauche%`
- Ligne export : 3933 · id 41474

#### RadioDroit  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `CAN IN 100`, `RadioDroit%`
- Ligne export : 3946 · id 41475

#### RadioStop  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `CAN IN 100`, `RadioStopInter`
- Ligne export : 3959 · id 41476

#### RadioStart  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `CAN IN 100`, `RadioStartInter`
- Ligne export : 3971 · id 41477

#### RadioSpeed  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `CAN IN 100`, `IDC Speed R`, `IDC Speed S`
- Ligne export : 3983 · id 41478

#### Timeout radio  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `True`
  - **Resetting** = `CAN IN 100`
- Lit : `CAN IN 100`
- Utilisé par : `Command State`, `State Latence`
- Ligne export : 3995 · id 41479

#### CAN IN 101  `GFIN`
- Propriétés : Identifier=0x101 · Data length=8 · Timeout=1000 · Paged protocol={Not used} · Parameters={{TimelapsIn [ms]; 32}} · Module=IPhone Remote (Generic) · Module index=0
- Lit : `TimelapsIn`
- Utilisé par : *(personne)*
- Ligne export : 4054 · id 41490

#### TimelapsIn  `GPIN`
- Propriétés : Unit=ms · Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `CAN IN 101`, `Latence Math`
- Ligne export : 4073 · id 41491

#### LatenceTimer  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=40000
- Logique :
  - **Increasing** = `True`
- Utilisé par : `Latence Math`, `TimeLapsOut`
- Ligne export : 4086 · id 41492

#### Latence Math  `MAC`
- Propriétés : Unit=ms · Limiting object group=Signed
- Logique :
  - **Controlling** = `LatenceTimer [ms] - TimelapsIn [ms]`
- Lit : `LatenceTimer`, `TimelapsIn`
- Utilisé par : `Command State`, `State Latence`
- Ligne export : 4138 · id 41502

#### State Latence  `SMC`
- Propriétés : Default state name=Default state
- Fonction *Latence niv 1* :
  - **Activating** = `(Timeout radio [ms] > 500) OR (Latence Math [ms] > 500)`
- Lit : `Latence Math`, `Timeout radio`
- Utilisé par : `RadioDroit%`, `RadioGauche%`
- Ligne export : 4182 · id 41510

#### RadioGauche%  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=State Latence
- Fonction *Default state* :
  - **Controlling** = `(200 * (RadioGauche / 65535)) - 100`
- Fonction *Latence niv 1* :
  - **Controlling** = `0`
- Lit : `RadioGauche`, `State Latence`
- Utilisé par : `Math Gauche`
- Ligne export : 4233 · id 41519

#### RadioDroit%  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=State Latence
- Fonction *Default state* :
  - **Controlling** = `(200 * (RadioDroit / 65535)) - 100`
- Fonction *Latence niv 1* :
  - **Controlling** = `0`
- Lit : `RadioDroit`, `State Latence`
- Utilisé par : `Math Droit`
- Ligne export : 4326 · id 41536

#### Command State  `SMC`
- Propriétés : Default state name=Normal
- Fonction *Radio* :
  - **Activating** = `(Timeout radio [ms] <= 800) AND (Latence Math [ms] <= 800)`
- Lit : `Latence Math`, `Timeout radio`
- Utilisé par : `IDC Speed R`, `IDC Speed R Wait`, `IDC Speed S`, `IDC Speed S Wait`, `Math Droit`, `Math Gauche`, `RadioMode`
- Ligne export : 4419 · id 41553

#### RadioMode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Command State = 1`
- Lit : `Command State`
- Utilisé par : *(personne)*
- Ligne export : 4470 · id 41562

#### RadioStopInter  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `0 < RadioStop`
- Lit : `RadioStop`
- Utilisé par : `Start Button`
- Ligne export : 4515 · id 41570

#### RadioStartInter  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `0 < RadioStart`
- Lit : `RadioStart`
- Utilisé par : `Start Button`
- Ligne export : 4560 · id 41578

#### TimeLapsOut  `GPOUT`
- Propriétés : Input value=LatenceTimer [ms] · Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian
- Lit : `LatenceTimer`
- Utilisé par : `CANOUT 102`
- Ligne export : 4605 · id 41586

#### Run Engine Statut  `GPOUT`
- Propriétés : Input value=CAN Engine Ready · Length=1 Byte (= 8 bits) · Type=Signed integer
- Lit : `CAN Engine Ready`
- Utilisé par : `CANOUT 102`
- Ligne export : 4617 · id 41587

#### CANOUT 102  `GFOUT`
- Propriétés : Identifier=0x102 · Data length=8 · Send method=Continuously · Transmit rate=50 · Unused bits=Set to 0 · Parameters={{TimeLapsOut [ms]; 32}; {Run Engine Statut; 0}} · Module=IPhone Remote (Generic) · Module index=0
- Lit : `Run Engine Statut`, `TimeLapsOut`
- Utilisé par : *(personne)*
- Ligne export : 4628 · id 41588
