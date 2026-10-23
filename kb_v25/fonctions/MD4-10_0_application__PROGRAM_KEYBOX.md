# MD4-10[0] application — PROGRAM KEYBOX

37 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## PROGRAM KEYBOX

#### BYTE 0 - New ID  `GPOUT`
- Propriétés : Input value=0x2F · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-C:Generic`, `GFOUT-J:Generic`
- Ligne export : 20841 · id 46024

#### Send new node  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Confirmation`, `MD4-10 page: SETUP`
- Ligne export : 20852 · id 46026

#### BYTE 1 - New ID  `GPOUT`
- Propriétés : Input value=0x11 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-C:Generic`, `GFOUT-J:Generic`
- Ligne export : 20862 · id 46028

#### BYTE 2 - New ID  `GPOUT`
- Propriétés : Input value=0x20 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-C:Generic`, `GFOUT-J:Generic`
- Ligne export : 20873 · id 46030

#### Select Node  `SP`
- Propriétés : Input channel=None · Default state name=None · States={KeyBox TB (GPS); KeyBox BB (Equip); KeyBox TC (Equip)}
- Utilisé par : `Keybox Gen`, `New ID`, `Adjust group: Keybox Setup`, `MD4-10 page: SETUP`, `Single adjust item: Select Node`
- Ligne export : 20884 · id 46048

#### New ID  `IP`
- Propriétés : Mode selector=Select Node · Default mode: None={0} · Mode 1: KeyBox TB (GPS)={0x17} · Mode 2: KeyBox BB (Equip)={0x18} · Mode 3: KeyBox TC (Equip)={0x19}
- Lit : `Select Node`
- Utilisé par : `BYTE 4 - New ID`, `ID`
- Ligne export : 20898 · id 46033

#### BYTE 4 - New ID  `GPOUT`
- Propriétés : Input value=New ID · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `New ID`
- Utilisé par : `GFOUT-C:Generic`, `GFOUT-J:Generic`
- Ligne export : 20916 · id 46032

#### Confirmation  `IMSG`
- Propriétés : Show message=All · Dialog type=Confirmation · Header=Confirmation · Text=Are you sure to reprogram the KeyBox · Left button=Yes · Center button=No
- Logique :
  - **Showing** = `Send new node`
- Lit : `Confirmation`, `Send new node`
- Utilisé par : `Confirmation Ok`, `Confirmation Ok`
- Ligne export : 20927 · id 53734

#### Confirmation Ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `2 = Confirmation`
- Lit : `Confirmation`
- Utilisé par : `GFOUT-C:Generic`, `GFOUT-J:Generic`, `Wait Send`
- Ligne export : 20975 · id 53748

#### Keybox Gen  `SMC`
- Propriétés : Default state name=1st Gen
- Fonction *2d Gen* :
  - **Activating** = `((KTB Keybox Type? = 1) and (Select Node = 1)) OR ((KBB Keybox Type? = 1) and (Select Node = 2)) OR ((KTC Keybox Type? = 1) and (Select Node = 3))`
- Lit : `KBB Keybox Type?`, `KTB Keybox Type?`, `KTC Keybox Type?`, `Select Node`
- Utilisé par : `Default ID`, `Default Read ID`, `Default Write ID`
- Ligne export : 21020 · id 93830

#### Default Write ID  `IMAC`
- Propriétés : Function selector=Keybox Gen
- Fonction *1st Gen* :
  - **Controlling** = `0x615`
- Fonction *2d Gen* :
  - **Controlling** = `0x60C`
- Lit : `Keybox Gen`
- Utilisé par : `GFOUT-C:Generic`
- Ligne export : 21134 · id 93849

#### GFOUT-C:Generic  `GFOUT`
- Propriétés : Identifier=Default Write ID · Data length=8 · Send method=On trigger · Trigger=Confirmation Ok · Unused bits=Set to 0 · Parameters={{BYTE 0 - New ID; 0}; {BYTE 1 - New ID; 8}; {BYTE 2 - New ID; 16}; {BYTE 4 - New ID; 32}} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=2
- Lit : `BYTE 0 - New ID`, `BYTE 1 - New ID`, `BYTE 2 - New ID`, `BYTE 4 - New ID`, `Confirmation Ok`, `Default Write ID`
- Utilisé par : *(personne)*
- Ligne export : 21206 · id 46025

#### BYTE 0 - HB  `GPOUT`
- Propriétés : Input value=0x2B · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-H:Generic`
- Ligne export : 21235 · id 53409

#### BYTE 1 - HB  `GPOUT`
- Propriétés : Input value=0x17 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-H:Generic`
- Ligne export : 21246 · id 53411

#### BYTE 2 - HB  `GPOUT`
- Propriétés : Input value=0x10 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-H:Generic`
- Ligne export : 21257 · id 53412

#### BYTE 4 - HB  `GPOUT`
- Propriétés : Input value=0xF4 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-H:Generic`
- Ligne export : 21268 · id 53413

#### ID  `IMAC`
- Logique :
  - **Controlling** = `New ID + 1536`
- Lit : `New ID`
- Utilisé par : `GFOUT-H:Generic`, `GFOUT-J:Generic`
- Ligne export : 21279 · id 53415

#### BYTE 5 - HB  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-H:Generic`
- Ligne export : 21322 · id 53421

#### Wait Send  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Confirmation Ok`
- Lit : `Confirmation Ok`
- Utilisé par : `Trigger HeartBeat`
- Ligne export : 21333 · id 53439

#### Trigger HeartBeat  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Wait Send`
- Lit : `Wait Send`
- Utilisé par : `GFOUT-H:Generic`
- Ligne export : 21376 · id 53452

#### GFOUT-H:Generic  `GFOUT`
- Propriétés : Identifier=ID · Data length=8 · Send method=On trigger · Trigger=Trigger HeartBeat · Unused bits=Set to 0 · Parameters={{BYTE 0 - HB; 0}; {BYTE 1 - HB; 8}; {BYTE 2 - HB; 16}; {BYTE 4 - HB; 32}; {BYTE 5 - HB; 40}} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=7
- Lit : `BYTE 0 - HB`, `BYTE 1 - HB`, `BYTE 2 - HB`, `BYTE 4 - HB`, `BYTE 5 - HB`, `ID`, `Trigger HeartBeat`
- Utilisé par : *(personne)*
- Ligne export : 21419 · id 53414

#### Default Read ID  `IMAC`
- Propriétés : Function selector=Keybox Gen
- Fonction *1st Gen* :
  - **Controlling** = `0x715`
- Fonction *2d Gen* :
  - **Controlling** = `0x70C`
- Lit : `Keybox Gen`
- Utilisé par : `Call Default`
- Ligne export : 21451 · id 94052

#### Call Default  `GFIN`
- Propriétés : Identifier=Default Read ID · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=2
- Lit : `Default Read ID`
- Utilisé par : `CanBus 0x715`
- Ligne export : 21523 · id 55492

#### Byte 0  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-I:Generic`
- Ligne export : 21539 · id 55493

#### Default ID  `IMAC`
- Propriétés : Function selector=Keybox Gen
- Fonction *1st Gen* :
  - **Controlling** = `0x15`
- Fonction *2d Gen* :
  - **Controlling** = `0x0C`
- Lit : `Keybox Gen`
- Utilisé par : `BYTE 4 - New ID`, `Byte 1`
- Ligne export : 21550 · id 94063

#### Byte 1  `GPOUT`
- Propriétés : Input value=Default ID · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Default ID`
- Utilisé par : `GFOUT-I:Generic`
- Ligne export : 21622 · id 55494

#### GFOUT-I:Generic  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=5000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=8
- Lit : `Byte 0`, `Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 21633 · id 55495

#### CanBus 0x715  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Call Default`
- Lit : `Call Default`
- Utilisé par : `CanBus Error No Program`
- Ligne export : 21655 · id 55515

#### CanBus Error No Program  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Keybox · Text=One or more Keyboxes need to be configured. Contact a service center.
- Logique :
  - **Showing** = `CanBus 0x715`
  - **Hiding** = `not(CanBus 0x715)`
- Lit : `CanBus 0x715`
- Utilisé par : *(personne)*
- Ligne export : 21698 · id 55523

#### BYTE 0 - New ID  `GPOUT`
- Propriétés : Input value=0x2F · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-C:Generic`, `GFOUT-J:Generic`
- Ligne export : 21752 · id 55636

#### Reset  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Confirmation`, `MD4-10 page: SETUP`
- Ligne export : 21763 · id 55637

#### BYTE 1 - New ID  `GPOUT`
- Propriétés : Input value=0x11 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-C:Generic`, `GFOUT-J:Generic`
- Ligne export : 21773 · id 55638

#### BYTE 2 - New ID  `GPOUT`
- Propriétés : Input value=0x20 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-C:Generic`, `GFOUT-J:Generic`
- Ligne export : 21784 · id 55639

#### BYTE 4 - New ID  `GPOUT`
- Propriétés : Input value=Default ID · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Default ID`
- Utilisé par : `GFOUT-C:Generic`, `GFOUT-J:Generic`
- Ligne export : 21795 · id 55640

#### Confirmation  `IMSG`
- Propriétés : Show message=All · Dialog type=Confirmation · Header=Reset · Text=Are you sure to reset the KeyBox · Left button=Yes · Center button=No
- Logique :
  - **Showing** = `Reset`
- Lit : `Reset`
- Utilisé par : `Confirmation`, `Confirmation Ok`, `Confirmation Ok`
- Ligne export : 21806 · id 55641

#### Confirmation Ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `2 = Confirmation`
- Lit : `Confirmation`
- Utilisé par : `GFOUT-C:Generic`, `GFOUT-J:Generic`, `Wait Send`
- Ligne export : 21854 · id 55649

#### GFOUT-J:Generic  `GFOUT`
- Propriétés : Identifier=ID · Data length=8 · Send method=On trigger · Trigger=Confirmation Ok · Unused bits=Set to 0 · Parameters={{BYTE 0 - New ID; 0}; {BYTE 1 - New ID; 8}; {BYTE 2 - New ID; 16}; {BYTE 4 - New ID; 32}} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=9
- Lit : `BYTE 0 - New ID`, `BYTE 1 - New ID`, `BYTE 2 - New ID`, `BYTE 4 - New ID`, `Confirmation Ok`, `ID`
- Utilisé par : *(personne)*
- Ligne export : 21899 · id 55657
