# MC42 app — logic screen c10 and KB

379 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## logic screen c10 and KB

#### btod c10_2  `ARC`
- Propriétés : Array size=15 · Store value=No
- Logique :
  ```qcode
  This[0]:=dtobin c10_1 APPIN mod 2
  This[1]:=(dtobin c10_1 APPIN div 2) mod 2
  This[2]:=(dtobin c10_1 APPIN div 4) mod 2
  This[3]:=(dtobin c10_1 APPIN div 8) mod 2
  This[4]:=(dtobin c10_1 APPIN div 16) mod 2
  This[5]:=(dtobin c10_1 APPIN div 32) mod 2
  This[6]:=(dtobin c10_1 APPIN div 64) mod 2
  This[7]:=(dtobin c10_1 APPIN div 128) mod 2
  This[8]:=(dtobin c10_1 APPIN div 256) mod 2
  This[9]:=(dtobin c10_1 APPIN div 512) mod 2
  This[10]:=(dtobin c10_1 APPIN div 1024) mod 2
  This[11]:=(dtobin c10_1 APPIN div 2048) mod 2
  This[12]:=(dtobin c10_1 APPIN div 4096) mod 2
  ```
- Lit : `dtobin c10_1 APPIN`
- Utilisé par : `B1 Button Cabine IDC C10`, `B10`, `B11`, `B12`, `B2 Door IDC C10`, `B3 Main page on C10_1`, `B4 Send new node KB`, `B5 Reset KB`, `B6`, `B7`, `B8`, `B9`
- Ligne export : 90799 · id 226032

#### B1 Button Cabine IDC C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10_2[0]
  ```
- Lit : `btod c10_2`
- Utilisé par : `Cabine Counter`
- Ligne export : 90831 · id 226077

#### B2 Door IDC C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10_2[1]
  ```
- Lit : `btod c10_2`
- Utilisé par : `KBB K11 IDC - DOOR`
- Ligne export : 90851 · id 226085

#### B3 Main page on C10_1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10_2[2]
  ```
- Lit : `btod c10_2`
- Utilisé par : `Engine On`
- Ligne export : 90871 · id 226093

#### dtobin c10_1 APPIN  `APPIN`
- Propriétés : Input channel=dtoni APPOUT C10_1 · Error value=0
- Lit : `dtoni APPOUT C10_1`
- Utilisé par : `btod c10_2`
- Ligne export : 98452 · id 226223

#### B4 Send new node KB  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10_2[3]
  ```
- Lit : `btod c10_2`
- Utilisé par : `Confirmation`
- Ligne export : 98462 · id 226101

#### B5 Reset KB  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10_2[4]
  ```
- Lit : `btod c10_2`
- Utilisé par : `Confirmation`
- Ligne export : 98482 · id 226109

#### B6  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10_2[5]
  ```
- Lit : `btod c10_2`
- Utilisé par : *(personne)*
- Ligne export : 98502 · id 226117

#### B7  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10_2[6]
  ```
- Lit : `btod c10_2`
- Utilisé par : *(personne)*
- Ligne export : 98522 · id 226125

#### B8  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10_2[7]
  ```
- Lit : `btod c10_2`
- Utilisé par : *(personne)*
- Ligne export : 98542 · id 226133

#### B9  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10_2[8]
  ```
- Lit : `btod c10_2`
- Utilisé par : *(personne)*
- Ligne export : 98562 · id 226141

#### B10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10_2[9]
  ```
- Lit : `btod c10_2`
- Utilisé par : *(personne)*
- Ligne export : 98582 · id 226149

#### B11  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10_2[10]
  ```
- Lit : `btod c10_2`
- Utilisé par : *(personne)*
- Ligne export : 98602 · id 226157

#### B12  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10_2[11]
  ```
- Lit : `btod c10_2`
- Utilisé par : *(personne)*
- Ligne export : 98622 · id 226165

#### Ladder is not up  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Ladder Position [%] > 5) AND (B9 START C10) AND (not(Joystick to zero))`
- Lit : `B9 START C10`, `Joystick to zero`, `Ladder Position`
- Utilisé par : `trameb 3`
- Ligne export : 98642 · id 218291

#### trameb 3  `ARC`
- Propriétés : Array size=10 · Store value=No
- Logique :
  ```qcode
  This[0]:=Ladder is not up*1
  This[1]:=KTB K1 IDC - GPS_EQT*2
  This[2]:=True*4
  This[3]:=Is multi button Eqt*8
  This[4]:=0*16
  This[5]:=0*32
  This[6]:=0*64
  This[7]:=0*128
  This[8]:=0*256
  ```
- Lit : `Is multi button Eqt`, `KTB K1 IDC - GPS_EQT`, `Ladder is not up`
- Utilisé par : `dtobin 3`
- Ligne export : 98702 · id 226400

#### dtobin 3  `MAC`
- Logique :
  ```qcode
  Result:=trameb 3[0]+trameb 3[1]+trameb 3[2]+trameb 3[3]+trameb 3[4]+trameb 3[5]+trameb 3[6]+trameb 3[7]+trameb 3[8]
  ```
- Lit : `trameb 3`
- Utilisé par : `debug btod 3`, `dtobin 3 APPOUT`
- Ligne export : 98730 · id 226425

#### debug btod 3  `ARC`
- Propriétés : Array size=10 · Store value=No
- Logique :
  ```qcode
  This[0]:=dtobin 3 mod 2
  This[1]:=(dtobin 3 div 2) mod 2
  This[2]:=(dtobin 3 div 4) mod 2
  This[3]:=(dtobin 3 div 8) mod 2
  This[4]:=(dtobin 3 div 16) mod 2
  This[5]:=(dtobin 3 div 32) mod 2
  This[6]:=(dtobin 3 div 64) mod 2
  This[7]:=(dtobin 3 div 128) mod 2
  This[8]:=(dtobin 3 div 256) mod 2
  ```
- Lit : `dtobin 3`
- Utilisé par : `debug Be1 Ladder is not up`, `debug Be2 KTB K1 IDC - GPS_EQT`, `debug Be3 KTC K9 IDC - OutBoard On-OFF`, `debug Be4 Is multi button Eqt`, `debug Be5`, `debug Be6`, `debug Be7`, `debug Be8`
- Ligne export : 98748 · id 226449

#### debug Be1 Ladder is not up  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 3[0]
  ```
- Lit : `debug btod 3`
- Utilisé par : *(personne)*
- Ligne export : 98777 · id 226482

#### debug Be2 KTB K1 IDC - GPS_EQT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 3[1]
  ```
- Lit : `debug btod 3`
- Utilisé par : *(personne)*
- Ligne export : 98797 · id 226490

#### debug Be3 KTC K9 IDC - OutBoard On-OFF  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 3[2]
  ```
- Lit : `debug btod 3`
- Utilisé par : *(personne)*
- Ligne export : 98817 · id 226498

#### debug Be4 Is multi button Eqt  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 3[3]
  ```
- Lit : `debug btod 3`
- Utilisé par : *(personne)*
- Ligne export : 98837 · id 226506

#### debug Be5  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 3[4]
  ```
- Lit : `debug btod 3`
- Utilisé par : *(personne)*
- Ligne export : 98857 · id 226514

#### debug Be6  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 3[5]
  ```
- Lit : `debug btod 3`
- Utilisé par : *(personne)*
- Ligne export : 98877 · id 226522

#### debug Be7  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 3[6]
  ```
- Lit : `debug btod 3`
- Utilisé par : *(personne)*
- Ligne export : 98897 · id 226530

#### dtobin 3 APPOUT  `APPOUT`
- Propriétés : Input channel=dtobin 3 · Send method=On change · Transmit rate=1000
- Lit : `dtobin 3`
- Utilisé par : `dtobin 3 APPIN`
- Ligne export : 98917 · id 226538

#### debug Be8  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod 3[7]
  ```
- Lit : `debug btod 3`
- Utilisé par : *(personne)*
- Ligne export : 98928 · id 226539

## logic screen c10 and KB / Keyboxs CAB — actif seulement si `is_cab_mc`

#### ON_Bits_GOUT 1  `GPOUT`
- Propriétés : Input value=ON_Bits 1 ktb · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `ON_Bits 1 ktb`
- Utilisé par : `Cout ON bits KTB Gen`
- Ligne export : 99505 · id 219798

#### OFF_Bits 1  `IMAC`
- Logique :
  ```qcode
  Result := bnot(ON_Bits 1 ktb) band 0x1FFF
  ```
- Lit : `ON_Bits 1 ktb`
- Utilisé par : `OFF_Bits_GOUT 1`
- Ligne export : 99517 · id 219799

#### OFF_Bits_GOUT 1  `GPOUT`
- Propriétés : Input value=OFF_Bits 1 · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `OFF_Bits 1`
- Utilisé par : `Cout ON bits KTB Gen`
- Ligne export : 99535 · id 219808

#### Cout ON bits KTB Gen  `GFOUT`
- Propriétés : Identifier=0x217 · Data length=8 · Send method=On change · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{OFF_Bits_GOUT 1; 0}; {ON_Bits_GOUT 1; 16}} · Module=Keyboxs CAB (Generic) · Module index=10
- Lit : `OFF_Bits_GOUT 1`, `ON_Bits_GOUT 1`
- Utilisé par : *(personne)*
- Ligne export : 99547 · id 219809

#### ON_Bits_GOUT 2  `GPOUT`
- Propriétés : Input value=ON_Bits 2 kbb · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `ON_Bits 2 kbb`
- Utilisé par : `Cout ON bits KBB Gen`
- Ligne export : 99569 · id 219855

#### OFF_Bits 2  `IMAC`
- Logique :
  ```qcode
  Result := bnot(ON_Bits 2 kbb) band 0x1FFF
  ```
- Lit : `ON_Bits 2 kbb`
- Utilisé par : `OFF_Bits_GOUT 2`
- Ligne export : 99581 · id 219856

#### OFF_Bits_GOUT 2  `GPOUT`
- Propriétés : Input value=OFF_Bits 2 · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `OFF_Bits 2`
- Utilisé par : `Cout ON bits KBB Gen`
- Ligne export : 99599 · id 219865

#### Cout ON bits KBB Gen  `GFOUT`
- Propriétés : Identifier=0x218 · Data length=8 · Send method=On change · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{OFF_Bits_GOUT 2; 0}; {ON_Bits_GOUT 2; 16}} · Module=Keyboxs CAB (Generic) · Module index=11
- Lit : `OFF_Bits_GOUT 2`, `ON_Bits_GOUT 2`
- Utilisé par : *(personne)*
- Ligne export : 99611 · id 219866

#### ON_Bits_GOUT 3  `GPOUT`
- Propriétés : Input value=ON_Bits 3 ktc · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `ON_Bits 3 ktc`
- Utilisé par : `Cout ON bits KTC Gen`
- Ligne export : 99633 · id 219912

#### OFF_Bits 3  `IMAC`
- Logique :
  ```qcode
  Result := bnot(ON_Bits 3 ktc) band 0x1FFF
  ```
- Lit : `ON_Bits 3 ktc`
- Utilisé par : `OFF_Bits_GOUT 3`
- Ligne export : 99645 · id 219913

#### OFF_Bits_GOUT 3  `GPOUT`
- Propriétés : Input value=OFF_Bits 3 · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `OFF_Bits 3`
- Utilisé par : `Cout ON bits KTC Gen`
- Ligne export : 99663 · id 219922

#### Cout ON bits KTC Gen  `GFOUT`
- Propriétés : Identifier=0x219 · Data length=8 · Send method=On change · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{OFF_Bits_GOUT 3; 0}; {ON_Bits_GOUT 3; 16}} · Module=Keyboxs CAB (Generic) · Module index=12
- Lit : `OFF_Bits_GOUT 3`, `ON_Bits_GOUT 3`
- Utilisé par : *(personne)*
- Ligne export : 99675 · id 219923

#### 0x719  `GFIN`
- Propriétés : Identifier=0x719 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={} · Module=Keyboxs CAB (Generic) · Module index=2
- Utilisé par : *(personne)*
- Ligne export : 99697 · id 219225

#### KTC Ok 0x719  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `0x719`
- Utilisé par : `CanBus Error KTC`, `MD4-10 page: INFO`, `MD4-10 page: SETUP`
- Ligne export : 99713 · id 219272

#### CanBus Error KTC  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Keybox · Text=KTC 0x719 Communication failure, reboot the system. If the problem persists, contact a service center.
- Logique :
  - **Showing** = `not(KTC Ok 0x719)`
  - **Hiding** = `KTC Ok 0x719`
- Lit : `KTC Ok 0x719`
- Utilisé par : *(personne)*
- Ligne export : 99756 · id 219280

#### 0x717  `GFIN`
- Propriétés : Identifier=0x717 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={} · Module=Keyboxs CAB (Generic) · Module index=1
- Utilisé par : *(personne)*
- Ligne export : 99810 · id 219011

#### 0x718  `GFIN`
- Propriétés : Identifier=0x718 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={} · Module=Keyboxs CAB (Generic) · Module index=0
- Utilisé par : *(personne)*
- Ligne export : 99826 · id 219012

#### Byte 0  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`, `GFOUT-F:Generic`
- Ligne export : 99842 · id 219013

#### Byte 1  `GPOUT`
- Propriétés : Input value=0x17 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`, `GFOUT-F:Generic`
- Ligne export : 99853 · id 219014

#### GFOUT-D:Generic  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=Keyboxs CAB (Generic) · Module index=0
- Lit : `Byte 0`, `Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 99864 · id 219015

#### Byte 0  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`, `GFOUT-F:Generic`
- Ligne export : 99886 · id 219016

#### Byte 1  `GPOUT`
- Propriétés : Input value=0x18 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`, `GFOUT-F:Generic`
- Ligne export : 99897 · id 219017

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=Keyboxs CAB (Generic) · Module index=1
- Lit : `Byte 0`, `Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 99908 · id 219018

#### KTB Ok 0x717  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `0x717`
- Utilisé par : `CanBus Error KTB`, `MD4-10 page: INFO`, `MD4-10 page: SETUP`
- Ligne export : 99930 · id 219255

#### CanBus Error KTB  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Keybox · Text=KTB 0x717 Communication failure, reboot the system. If the problem persists, contact a service center.
- Logique :
  - **Showing** = `not(KTB Ok 0x717)`
  - **Hiding** = `KTB Ok 0x717`
- Lit : `KTB Ok 0x717`
- Utilisé par : *(personne)*
- Ligne export : 99973 · id 219263

#### KBB Ok 0x718  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `0x718`
- Utilisé par : `CanBus Error KBB`, `MD4-10 page: INFO`, `MD4-10 page: SETUP`
- Ligne export : 100027 · id 219289

#### CanBus Error KBB  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Keybox · Text=KBB 0x718 Communication failure, reboot the system. If the problem persists, contact a service center.
- Logique :
  - **Showing** = `not(KBB Ok 0x718)`
  - **Hiding** = `KBB Ok 0x718`
- Lit : `KBB Ok 0x718`
- Utilisé par : *(personne)*
- Ligne export : 100070 · id 219297

#### Byte 0  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`, `GFOUT-F:Generic`
- Ligne export : 100124 · id 219226

#### Byte 1  `GPOUT`
- Propriétés : Input value=0x19 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`, `GFOUT-F:Generic`
- Ligne export : 100135 · id 219227

#### GFOUT-F:Generic  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=Keyboxs CAB (Generic) · Module index=2
- Lit : `Byte 0`, `Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 100146 · id 219228

#### ID Fault 0x17 KTB  `IMAC`
- Logique :
  - **Controlling** = `0x17 + 0x180`
- Utilisé par : `GFIN-E:Generic`
- Ligne export : 101044 · id 229612

#### GFIN-E:Generic  `GFIN`
- Propriétés : Identifier=ID Fault 0x17 KTB · Data length=Dont care · Paged protocol={Not used} · Parameters={{K1 Fault; 1}; {K2 Fault; 2}; {K3 Fault; 3}; {K4 Fault; 4}; {K5 Fault; 5}; {K6 Fault; 6}; {K7 Fault; 7}; {K8 Fault; 8}; {K9 Fault; 9}; {K10 Fault; 10}; {K11 Fault; 11}; {K12 Fault; 12}; {K13 Fault; 13}} · Module=Keyboxs CAB (Generic) · Module index=4
- Lit : `ID Fault 0x17 KTB`, `K1 Fault`, `K10 Fault`, `K11 Fault`, `K12 Fault`, `K13 Fault`, `K2 Fault`, `K3 Fault`, `K4 Fault`, `K5 Fault`, `K6 Fault`, `K7 Fault`, `K8 Fault`, `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101087 · id 229620

#### K1 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K1 fuse is blown mc`, `KTB K1 fuse is blown mc`, `KTC K1 fuse is blown mc`
- Ligne export : 101142 · id 229621

#### KTB K1 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTB K1 fuse is blown
- Logique :
  - **Showing** = `K1 Fault`
- Lit : `K1 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101154 · id 229622

#### K2 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K2 fuse is blown  mc`, `KTB K2 fuse is blown  mc`, `KTC K2 fuse is blown  mc`
- Ligne export : 101200 · id 229630

#### KTB K2 fuse is blown  mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTB K2 fuse is blown
- Logique :
  - **Showing** = `K2 Fault`
- Lit : `K2 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101212 · id 229631

#### K3 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K3 fuse is blown  mc`, `KTB K3 fuse is blown  mc`, `KTC K3 fuse is blown  mc`
- Ligne export : 101258 · id 229639

#### KTB K3 fuse is blown  mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTB K3 fuse is blown
- Logique :
  - **Showing** = `K3 Fault`
- Lit : `K3 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101270 · id 229640

#### K4 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K4 fuse is blown mc`, `KTB K4 fuse is blown mc`, `KTC K4 fuse is blown mc`
- Ligne export : 101316 · id 229648

#### KTB K4 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTB K4 fuse is blown
- Logique :
  - **Showing** = `K4 Fault`
- Lit : `K4 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101328 · id 229649

#### K5 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K5 fuse is blown mc`, `KTB K5 fuse is blown mc`, `KTC K5 fuse is blown mc`
- Ligne export : 101374 · id 229657

#### KTB K5 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTB K5 fuse is blown
- Logique :
  - **Showing** = `K5 Fault`
- Lit : `K5 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101386 · id 229658

#### K6 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K6 fuse is blown mc`, `KTB K6 fuse is blown mc`, `KTC K6 fuse is blown mc`
- Ligne export : 101432 · id 229666

#### KTB K6 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTB K6 fuse is blown
- Logique :
  - **Showing** = `K6 Fault`
- Lit : `K6 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101444 · id 229667

#### K7 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K7 fuse is blown mc`, `KTB K7 fuse is blown mc`, `KTC K7 fuse is blown mc`
- Ligne export : 101490 · id 229675

#### KTB K7 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTB K7 fuse is blown
- Logique :
  - **Showing** = `K7 Fault`
- Lit : `K7 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101502 · id 229676

#### K8 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K8 fuse is blown mc`, `KTB K8 fuse is blown mc`, `KTC K8 fuse is blown mc`
- Ligne export : 101548 · id 229684

#### KTB K8 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTB K8 fuse is blown
- Logique :
  - **Showing** = `K8 Fault`
- Lit : `K8 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101560 · id 229685

#### K9 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K9 fuse is blown mc`, `KTB K9 fuse is blown mc`, `KTC K9 fuse is blown mc`
- Ligne export : 101606 · id 229693

#### KTB K9 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTB K9 fuse is blown
- Logique :
  - **Showing** = `K9 Fault`
- Lit : `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101618 · id 229694

#### K10 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K10 fuse is blown mc`, `KTB K10 fuse is blown mc`, `KTC K10 fuse is blown mc`
- Ligne export : 101664 · id 229702

#### KTB K10 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTB K10 fuse is blown
- Logique :
  - **Showing** = `K10 Fault`
- Lit : `K10 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101676 · id 229703

#### K11 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K11 fuse is blown mc`, `KTB K11 fuse is blown mc`, `KTC K11 fuse is blown mc`
- Ligne export : 101722 · id 229711

#### KTB K11 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTB K11 fuse is blown
- Logique :
  - **Showing** = `K11 Fault`
- Lit : `K11 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101734 · id 229712

#### K12 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K12 fuse is blown mc`, `KTB K12 fuse is blown mc`, `KTC K12 fuse is blown mc`
- Ligne export : 101780 · id 229720

#### KTB K12 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTB K12 fuse is blown
- Logique :
  - **Showing** = `K12 Fault`
- Lit : `K12 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101792 · id 229721

#### K13 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K13 fuse is blown mc`, `KTB K13 fuse is blown mc`, `KTC K13 fuse is blown mc`
- Ligne export : 101838 · id 229729

#### KTB K13 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTB K13 fuse is blown
- Logique :
  - **Showing** = `K13 Fault`
- Lit : `K13 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101850 · id 229730

#### ID Fault 0x18 KBB  `IMAC`
- Logique :
  - **Controlling** = `0x18 + 0x180`
- Utilisé par : `GFIN-F:Generic`
- Ligne export : 101896 · id 229782

#### GFIN-F:Generic  `GFIN`
- Propriétés : Identifier=ID Fault 0x18 KBB · Data length=Dont care · Paged protocol={Not used} · Parameters={{K1 Fault; 1}; {K2 Fault; 2}; {K3 Fault; 3}; {K4 Fault; 4}; {K5 Fault; 5}; {K6 Fault; 6}; {K7 Fault; 7}; {K8 Fault; 8}; {K9 Fault; 9}; {K10 Fault; 10}; {K11 Fault; 11}; {K12 Fault; 12}; {K13 Fault; 13}} · Module=Keyboxs CAB (Generic) · Module index=5
- Lit : `ID Fault 0x18 KBB`, `K1 Fault`, `K10 Fault`, `K11 Fault`, `K12 Fault`, `K13 Fault`, `K2 Fault`, `K3 Fault`, `K4 Fault`, `K5 Fault`, `K6 Fault`, `K7 Fault`, `K8 Fault`, `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 101939 · id 229790

#### K1 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K1 fuse is blown mc`, `KTB K1 fuse is blown mc`, `KTC K1 fuse is blown mc`
- Ligne export : 101994 · id 229791

#### KBB K1 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KBB K1 fuse is blown
- Logique :
  - **Showing** = `K1 Fault`
- Lit : `K1 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102006 · id 229792

#### K2 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K2 fuse is blown  mc`, `KTB K2 fuse is blown  mc`, `KTC K2 fuse is blown  mc`
- Ligne export : 102052 · id 229800

#### KBB K2 fuse is blown  mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KBB K2 fuse is blown
- Logique :
  - **Showing** = `K2 Fault`
- Lit : `K2 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102064 · id 229801

#### K3 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K3 fuse is blown  mc`, `KTB K3 fuse is blown  mc`, `KTC K3 fuse is blown  mc`
- Ligne export : 102110 · id 229809

#### KBB K3 fuse is blown  mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KBB K3 fuse is blown
- Logique :
  - **Showing** = `K3 Fault`
- Lit : `K3 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102122 · id 229810

#### K4 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K4 fuse is blown mc`, `KTB K4 fuse is blown mc`, `KTC K4 fuse is blown mc`
- Ligne export : 102168 · id 229818

#### KBB K4 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KBB K4 fuse is blown
- Logique :
  - **Showing** = `K4 Fault`
- Lit : `K4 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102180 · id 229819

#### K5 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K5 fuse is blown mc`, `KTB K5 fuse is blown mc`, `KTC K5 fuse is blown mc`
- Ligne export : 102226 · id 229827

#### KBB K5 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KBB K5 fuse is blown
- Logique :
  - **Showing** = `K5 Fault`
- Lit : `K5 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102238 · id 229828

#### K6 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K6 fuse is blown mc`, `KTB K6 fuse is blown mc`, `KTC K6 fuse is blown mc`
- Ligne export : 102284 · id 229836

#### KBB K6 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KBB K6 fuse is blown
- Logique :
  - **Showing** = `K6 Fault`
- Lit : `K6 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102296 · id 229837

#### K7 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K7 fuse is blown mc`, `KTB K7 fuse is blown mc`, `KTC K7 fuse is blown mc`
- Ligne export : 102342 · id 229845

#### KBB K7 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KBB K7 fuse is blown
- Logique :
  - **Showing** = `K7 Fault`
- Lit : `K7 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102354 · id 229846

#### K8 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K8 fuse is blown mc`, `KTB K8 fuse is blown mc`, `KTC K8 fuse is blown mc`
- Ligne export : 102400 · id 229854

#### KBB K8 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KBB K8 fuse is blown
- Logique :
  - **Showing** = `K8 Fault`
- Lit : `K8 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102412 · id 229855

#### K9 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K9 fuse is blown mc`, `KTB K9 fuse is blown mc`, `KTC K9 fuse is blown mc`
- Ligne export : 102458 · id 229863

#### KBB K9 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KBB K9 fuse is blown
- Logique :
  - **Showing** = `K9 Fault`
- Lit : `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102470 · id 229864

#### K10 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K10 fuse is blown mc`, `KTB K10 fuse is blown mc`, `KTC K10 fuse is blown mc`
- Ligne export : 102516 · id 229872

#### KBB K10 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KBB K10 fuse is blown
- Logique :
  - **Showing** = `K10 Fault`
- Lit : `K10 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102528 · id 229873

#### K11 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K11 fuse is blown mc`, `KTB K11 fuse is blown mc`, `KTC K11 fuse is blown mc`
- Ligne export : 102574 · id 229881

#### KBB K11 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KBB K11 fuse is blown
- Logique :
  - **Showing** = `K11 Fault`
- Lit : `K11 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102586 · id 229882

#### K12 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K12 fuse is blown mc`, `KTB K12 fuse is blown mc`, `KTC K12 fuse is blown mc`
- Ligne export : 102632 · id 229890

#### KBB K12 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KBB K12 fuse is blown
- Logique :
  - **Showing** = `K12 Fault`
- Lit : `K12 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102644 · id 229891

#### K13 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K13 fuse is blown mc`, `KTB K13 fuse is blown mc`, `KTC K13 fuse is blown mc`
- Ligne export : 102690 · id 229899

#### KBB K13 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KBB K13 fuse is blown
- Logique :
  - **Showing** = `K13 Fault`
- Lit : `K13 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102702 · id 229900

#### ID Fault 0x19 KTC  `IMAC`
- Logique :
  - **Controlling** = `0x19 + 0x180`
- Utilisé par : `GFIN-G:Generic`
- Ligne export : 102748 · id 229952

#### GFIN-G:Generic  `GFIN`
- Propriétés : Identifier=ID Fault 0x19 KTC · Data length=Dont care · Paged protocol={Not used} · Parameters={{K1 Fault; 1}; {K2 Fault; 2}; {K3 Fault; 3}; {K4 Fault; 4}; {K5 Fault; 5}; {K6 Fault; 6}; {K7 Fault; 7}; {K8 Fault; 8}; {K9 Fault; 9}; {K10 Fault; 10}; {K11 Fault; 11}; {K12 Fault; 12}; {K13 Fault; 13}} · Module=Keyboxs CAB (Generic) · Module index=6
- Lit : `ID Fault 0x19 KTC`, `K1 Fault`, `K10 Fault`, `K11 Fault`, `K12 Fault`, `K13 Fault`, `K2 Fault`, `K3 Fault`, `K4 Fault`, `K5 Fault`, `K6 Fault`, `K7 Fault`, `K8 Fault`, `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102791 · id 229960

#### K1 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K1 fuse is blown mc`, `KTB K1 fuse is blown mc`, `KTC K1 fuse is blown mc`
- Ligne export : 102846 · id 229961

#### KTC K1 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTC K1 fuse is blown
- Logique :
  - **Showing** = `K1 Fault`
- Lit : `K1 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102858 · id 229962

#### K2 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K2 fuse is blown  mc`, `KTB K2 fuse is blown  mc`, `KTC K2 fuse is blown  mc`
- Ligne export : 102904 · id 229970

#### KTC K2 fuse is blown  mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTC K2 fuse is blown
- Logique :
  - **Showing** = `K2 Fault`
- Lit : `K2 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102916 · id 229971

#### K3 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K3 fuse is blown  mc`, `KTB K3 fuse is blown  mc`, `KTC K3 fuse is blown  mc`
- Ligne export : 102962 · id 229979

#### KTC K3 fuse is blown  mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTC K3 fuse is blown
- Logique :
  - **Showing** = `K3 Fault`
- Lit : `K3 Fault`
- Utilisé par : *(personne)*
- Ligne export : 102974 · id 229980

#### K4 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K4 fuse is blown mc`, `KTB K4 fuse is blown mc`, `KTC K4 fuse is blown mc`
- Ligne export : 103020 · id 229988

#### KTC K4 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTC K4 fuse is blown
- Logique :
  - **Showing** = `K4 Fault`
- Lit : `K4 Fault`
- Utilisé par : *(personne)*
- Ligne export : 103032 · id 229989

#### K5 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K5 fuse is blown mc`, `KTB K5 fuse is blown mc`, `KTC K5 fuse is blown mc`
- Ligne export : 103078 · id 229997

#### KTC K5 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTC K5 fuse is blown
- Logique :
  - **Showing** = `K5 Fault`
- Lit : `K5 Fault`
- Utilisé par : *(personne)*
- Ligne export : 103090 · id 229998

#### K6 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K6 fuse is blown mc`, `KTB K6 fuse is blown mc`, `KTC K6 fuse is blown mc`
- Ligne export : 103136 · id 230006

#### KTC K6 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTC K6 fuse is blown
- Logique :
  - **Showing** = `K6 Fault`
- Lit : `K6 Fault`
- Utilisé par : *(personne)*
- Ligne export : 103148 · id 230007

#### K7 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K7 fuse is blown mc`, `KTB K7 fuse is blown mc`, `KTC K7 fuse is blown mc`
- Ligne export : 103194 · id 230015

#### KTC K7 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTC K7 fuse is blown
- Logique :
  - **Showing** = `K7 Fault`
- Lit : `K7 Fault`
- Utilisé par : *(personne)*
- Ligne export : 103206 · id 230016

#### K8 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K8 fuse is blown mc`, `KTB K8 fuse is blown mc`, `KTC K8 fuse is blown mc`
- Ligne export : 103252 · id 230024

#### KTC K8 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTC K8 fuse is blown
- Logique :
  - **Showing** = `K8 Fault`
- Lit : `K8 Fault`
- Utilisé par : *(personne)*
- Ligne export : 103264 · id 230025

#### K9 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K9 fuse is blown mc`, `KTB K9 fuse is blown mc`, `KTC K9 fuse is blown mc`
- Ligne export : 103310 · id 230033

#### KTC K9 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTC K9 fuse is blown
- Logique :
  - **Showing** = `K9 Fault`
- Lit : `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 103322 · id 230034

#### K10 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K10 fuse is blown mc`, `KTB K10 fuse is blown mc`, `KTC K10 fuse is blown mc`
- Ligne export : 103368 · id 230042

#### KTC K10 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTC K10 fuse is blown
- Logique :
  - **Showing** = `K10 Fault`
- Lit : `K10 Fault`
- Utilisé par : *(personne)*
- Ligne export : 103380 · id 230043

#### K11 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K11 fuse is blown mc`, `KTB K11 fuse is blown mc`, `KTC K11 fuse is blown mc`
- Ligne export : 103426 · id 230051

#### KTC K11 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTC K11 fuse is blown
- Logique :
  - **Showing** = `K11 Fault`
- Lit : `K11 Fault`
- Utilisé par : *(personne)*
- Ligne export : 103438 · id 230052

#### K12 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K12 fuse is blown mc`, `KTB K12 fuse is blown mc`, `KTC K12 fuse is blown mc`
- Ligne export : 103484 · id 230060

#### KTC K12 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTC K12 fuse is blown
- Logique :
  - **Showing** = `K12 Fault`
- Lit : `K12 Fault`
- Utilisé par : *(personne)*
- Ligne export : 103496 · id 230061

#### K13 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-E:Generic`, `GFIN-F:Generic`, `GFIN-G:Generic`, `KBB K13 fuse is blown mc`, `KTB K13 fuse is blown mc`, `KTC K13 fuse is blown mc`
- Ligne export : 103542 · id 230069

#### KTC K13 fuse is blown mc  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header, English=KTC K13 fuse is blown
- Logique :
  - **Showing** = `K13 Fault`
- Lit : `K13 Fault`
- Utilisé par : *(personne)*
- Ligne export : 103554 · id 230070

## logic screen c10 and KB / Keyboxs CAB / Program KB CAB

#### BYTE 0 - New ID  `GPOUT`
- Propriétés : Input value=0x2F · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `New Generic frame out`, `New Generic frame out`
- Ligne export : 100183 · id 219945

#### BYTE 1 - New ID  `GPOUT`
- Propriétés : Input value=0x11 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `New Generic frame out`, `New Generic frame out`
- Ligne export : 100194 · id 219947

#### BYTE 2 - New ID  `GPOUT`
- Propriétés : Input value=0x20 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `New Generic frame out`, `New Generic frame out`
- Ligne export : 100205 · id 219948

#### md4 Select Node  `SP`
- Propriétés : Input channel=None · Default state name=None · States={KeyBox TB (GPS); KeyBox BB (Equip); KeyBox TC (Equip)}
- Utilisé par : `New ID`, `MD4-10 page: SETUP`, `Single adjust item: md4 Select Node`
- Ligne export : 100216 · id 219949

#### New ID  `IP`
- Propriétés : Mode selector=md4 Select Node · Default mode: None={0} · Mode 1: KeyBox TB (GPS)={0x17} · Mode 2: KeyBox BB (Equip)={0x18} · Mode 3: KeyBox TC (Equip)={0x19}
- Lit : `md4 Select Node`
- Utilisé par : `BYTE 4 - New ID`, `ID`
- Ligne export : 100230 · id 219953

#### BYTE 4 - New ID  `GPOUT`
- Propriétés : Input value=New ID · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `New ID`
- Utilisé par : `New Generic frame out`, `New Generic frame out`
- Ligne export : 100248 · id 219954

#### Confirmation  `IMSG`
- Propriétés : Show message=All · Dialog type=Confirmation · Header=Confirmation · Text=Are you sure to reprogram the KeyBox · Left button=Yes · Center button=No
- Logique :
  - **Showing** = `B4 Send new node KB`
- Lit : `B4 Send new node KB`, `Confirmation`
- Utilisé par : `Confirmation Ok`, `Confirmation Ok`
- Ligne export : 100259 · id 219955

#### Confirmation Ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `2 = Confirmation`
- Lit : `Confirmation`
- Utilisé par : `New Generic frame out`, `New Generic frame out`, `Wait Send`
- Ligne export : 100307 · id 219963

#### Default Write ID  `IMAC`
- Logique :
  - **Controlling** = `0x60C`
- Utilisé par : `New Generic frame out`
- Ligne export : 100352 · id 219987

#### New Generic frame out  `GFOUT`
- Propriétés : Identifier=Default Write ID · Data length=8 · Send method=On trigger · Trigger=Confirmation Ok · Unused bits=Set to 0 · Parameters={{BYTE 0 - New ID; 0}; {BYTE 1 - New ID; 8}; {BYTE 2 - New ID; 16}; {BYTE 4 - New ID; 32}} · Module=Keyboxs CAB (Generic) · Module index=5
- Lit : `BYTE 0 - New ID`, `BYTE 1 - New ID`, `BYTE 2 - New ID`, `BYTE 4 - New ID`, `Confirmation Ok`, `Default Write ID`
- Utilisé par : *(personne)*
- Ligne export : 100393 · id 220002

#### BYTE 0 - HB  `GPOUT`
- Propriétés : Input value=0x2B · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `New Generic frame out`
- Ligne export : 100422 · id 220003

#### BYTE 1 - HB  `GPOUT`
- Propriétés : Input value=0x17 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `New Generic frame out`
- Ligne export : 100433 · id 220004

#### BYTE 2 - HB  `GPOUT`
- Propriétés : Input value=0x10 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `New Generic frame out`
- Ligne export : 100444 · id 220005

#### BYTE 4 - HB  `GPOUT`
- Propriétés : Input value=0xF4 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `New Generic frame out`
- Ligne export : 100455 · id 220006

#### ID  `IMAC`
- Logique :
  - **Controlling** = `New ID + 1536`
- Lit : `New ID`
- Utilisé par : `New Generic frame out`, `New Generic frame out`
- Ligne export : 100466 · id 220007

#### BYTE 5 - HB  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `New Generic frame out`
- Ligne export : 100509 · id 220015

#### Wait Send  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Confirmation Ok`
- Lit : `Confirmation Ok`
- Utilisé par : `Trigger HeartBeat`
- Ligne export : 100520 · id 220016

#### Trigger HeartBeat  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Wait Send`
- Lit : `Wait Send`
- Utilisé par : `New Generic frame out`
- Ligne export : 100563 · id 220024

#### New Generic frame out  `GFOUT`
- Propriétés : Identifier=ID · Data length=8 · Send method=On trigger · Trigger=Trigger HeartBeat · Unused bits=Set to 0 · Parameters={{BYTE 0 - HB; 0}; {BYTE 1 - HB; 8}; {BYTE 2 - HB; 16}; {BYTE 4 - HB; 32}; {BYTE 5 - HB; 40}} · Module=Keyboxs CAB (Generic) · Module index=3
- Lit : `BYTE 0 - HB`, `BYTE 1 - HB`, `BYTE 2 - HB`, `BYTE 4 - HB`, `BYTE 5 - HB`, `ID`, `Trigger HeartBeat`
- Utilisé par : *(personne)*
- Ligne export : 100606 · id 220032

#### Default Read ID  `IMAC`
- Logique :
  - **Controlling** = `0x70C`
- Utilisé par : `Call Default`
- Ligne export : 100638 · id 220033

#### Call Default  `GFIN`
- Propriétés : Identifier=Default Read ID · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={} · Module=Keyboxs CAB (Generic) · Module index=3
- Lit : `Default Read ID`
- Utilisé par : `CanBus 0x715`
- Ligne export : 100679 · id 220048

#### Byte 0  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `New Generic frame out`
- Ligne export : 100695 · id 220049

#### Default ID  `IMAC`
- Logique :
  - **Controlling** = `0x0C`
- Utilisé par : `BYTE 4 - New ID`, `Byte 1`
- Ligne export : 100706 · id 220050

#### Byte 1  `GPOUT`
- Propriétés : Input value=Default ID · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Default ID`
- Utilisé par : `New Generic frame out`
- Ligne export : 100747 · id 220065

#### New Generic frame out  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=5000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=Keyboxs CAB (Generic) · Module index=6
- Lit : `Byte 0`, `Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 100758 · id 220066

#### CanBus 0x715  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Call Default`
- Lit : `Call Default`
- Utilisé par : `CanBus Error No Program`
- Ligne export : 100780 · id 220067

#### CanBus Error No Program  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Keybox · Text=One or more Keyboxes need to be configured. Contact a service center.
- Logique :
  - **Showing** = `CanBus 0x715`
  - **Hiding** = `not(CanBus 0x715)`
- Lit : `CanBus 0x715`
- Utilisé par : *(personne)*
- Ligne export : 100823 · id 220075

#### BYTE 0 - New ID  `GPOUT`
- Propriétés : Input value=0x2F · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `New Generic frame out`, `New Generic frame out`
- Ligne export : 100877 · id 220084

#### BYTE 1 - New ID  `GPOUT`
- Propriétés : Input value=0x11 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `New Generic frame out`, `New Generic frame out`
- Ligne export : 100888 · id 220086

#### BYTE 2 - New ID  `GPOUT`
- Propriétés : Input value=0x20 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `New Generic frame out`, `New Generic frame out`
- Ligne export : 100899 · id 220087

#### BYTE 4 - New ID  `GPOUT`
- Propriétés : Input value=Default ID · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Default ID`
- Utilisé par : `New Generic frame out`, `New Generic frame out`
- Ligne export : 100910 · id 220088

#### Confirmation  `IMSG`
- Propriétés : Show message=All · Dialog type=Confirmation · Header=Reset · Text=Are you sure to reset the KeyBox · Left button=Yes · Center button=No
- Logique :
  - **Showing** = `B5 Reset KB`
- Lit : `B5 Reset KB`, `Reset`
- Utilisé par : `Confirmation`, `Confirmation Ok`, `Confirmation Ok`
- Ligne export : 100921 · id 220089

#### Confirmation Ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `2 = Confirmation`
- Lit : `Confirmation`
- Utilisé par : `New Generic frame out`, `New Generic frame out`, `Wait Send`
- Ligne export : 100969 · id 220097

#### New Generic frame out  `GFOUT`
- Propriétés : Identifier=ID · Data length=8 · Send method=On trigger · Trigger=Confirmation Ok · Unused bits=Set to 0 · Parameters={{BYTE 0 - New ID; 0}; {BYTE 1 - New ID; 8}; {BYTE 2 - New ID; 16}; {BYTE 4 - New ID; 32}} · Module=Keyboxs CAB (Generic) · Module index=4
- Lit : `BYTE 0 - New ID`, `BYTE 1 - New ID`, `BYTE 2 - New ID`, `BYTE 4 - New ID`, `Confirmation Ok`, `ID`
- Utilisé par : *(personne)*
- Ligne export : 101014 · id 220105

## logic screen c10 and KB / cEQUIPEMENT — actif seulement si `is_cab_mc`

#### Auto Off Lamps  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `(Power Down) OR (Charger Charging Wait 2 minutes)`
- Lit : `Charger Charging Wait 2 minutes`, `Power Down`
- Utilisé par : `KBB K12 IDC - BILGE`, `KBB K8 DC - PUMP SHOWER`, `KBB K9 IDC - PUMP WIND`, `KTB K1 IDC - GPS_EQT`, `KTB K10 IDC - Fridge`, `KTB K12 IDC - Aux 2`, `KTB K2 IDC - AUDIO/AUX 4`, `KTB K3 IDC - VHF/AUX 5`, `KTB K4 IDC- Cabine`, `KTB K5 IDC - HT - 360 White`, `KTB K6 IDC - NAV`, `KTB K7 IDC - HT - Spot`, `KTB K8 DC - HT - DIM`, `KTB K9 IDC - Cockpit Light`, `KTC K1 IDC - Wipper On/Off`, `KTC K2 IDC - Wipper Speed`, `KTC K3 IDC - Seat Power`, `KTC K4 IDC - Water Cooling`, `KTC K5 IDC - Pump Water`, `KTC K8 DC - Fan wind cmd`
- Ligne export : 90906 · id 218382

#### btod c10 B  `ARC`
- Propriétés : Array size=15 · Store value=No
- Logique :
  ```qcode
  This[0]:=dtobin c10 B APPIN mod 2
  This[1]:=(dtobin c10 B APPIN div 2) mod 2
  This[2]:=(dtobin c10 B APPIN div 4) mod 2
  This[3]:=(dtobin c10 B APPIN div 8) mod 2
  This[4]:=(dtobin c10 B APPIN div 16) mod 2
  This[5]:=(dtobin c10 B APPIN div 32) mod 2
  This[6]:=(dtobin c10 B APPIN div 64) mod 2
  This[7]:=(dtobin c10 B APPIN div 128) mod 2
  This[8]:=(dtobin c10 B APPIN div 256) mod 2
  This[9]:=(dtobin c10 B APPIN div 512) mod 2
  This[10]:=(dtobin c10 B APPIN div 1024) mod 2
  This[11]:=(dtobin c10 B APPIN div 2048) mod 2
  This[12]:=(dtobin c10 B APPIN div 4096) mod 2
  This[13]:=(dtobin c10 B APPIN div 8192) mod 2
  This[14]:=(dtobin c10 B APPIN div 16384) mod 2
  ```
- Lit : `dtobin c10 B APPIN`
- Utilisé par : `B1 LD UP - VDIN`, `B10 CABINE ON/OFF`, `B11 NAV + 360 LIGHT`, `B12 LIGHT HT SPOT`, `B13 Search Light`, `B14 Fridge`, `B15 LIGHT HT DIM`, `B2 LD DOWN - VDIN`, `B3 HT UP D`, `B4 HT DOWN D`, `B5 md4 GPS`, `B6 md4 AUX 4`, `B7 md4 AUDIO`, `B8 md4 AUX 5`, `B9 md4 VHF`
- Ligne export : 90956 · id 228508

#### B5 md4 GPS  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[4]
  ```
- Lit : `btod c10 B`
- Utilisé par : `KTB K1 IDC - GPS_EQT`
- Ligne export : 90990 · id 228591

#### KTB K1 IDC - GPS_EQT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B5 md4 GPS`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `B5 md4 GPS`
- Utilisé par : `ON_Bits 1 ktb`, `trameb 3`
- Ligne export : 91010 · id 218391

#### B6 md4 AUX 4  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[5]
  ```
- Lit : `btod c10 B`
- Utilisé par : `KBB K7 IDC - AUX 1`, `Need Charge 12v dcdc on C10`
- Ligne export : 91060 · id 228599

#### B7 md4 AUDIO  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[6]
  ```
- Lit : `btod c10 B`
- Utilisé par : `KTB K2 IDC - AUDIO/AUX 4`
- Ligne export : 91080 · id 228607

#### KTB K2 IDC - AUDIO/AUX 4  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B7 md4 AUDIO`
  - **Blocking** = `(Auto Off Lamps) OR ((not(Battery DRIVE MODE)) and md4 Aux 4 - Need HT)`
- Lit : `Auto Off Lamps`, `B7 md4 AUDIO`, `Battery DRIVE MODE`, `md4 Aux 4 - Need HT`
- Utilisé par : `ON_Bits 1 ktb`
- Ligne export : 91100 · id 218402

#### B8 md4 AUX 5  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[7]
  ```
- Lit : `btod c10 B`
- Utilisé par : `KTC K6 IDC - Aux A - AC`, `KTC K9 IDC - OutBoard On-OFF`, `Need Charge 12v dcdc on C10`
- Ligne export : 91167 · id 228615

#### B9 md4 VHF  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[8]
  ```
- Lit : `btod c10 B`
- Utilisé par : `KTB K3 IDC - VHF/AUX 5`
- Ligne export : 91187 · id 228623

#### KTB K3 IDC - VHF/AUX 5  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B9 md4 VHF`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `B9 md4 VHF`
- Utilisé par : `ON_Bits 1 ktb`
- Ligne export : 91207 · id 218416

#### md4 Water Level Protection  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `LOW Level`, `Adjust group: Master Features`, `Single adjust item: md4 Water Level Protection`
- Ligne export : 91257 · id 218428

#### LOW Level  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `(Water Level mc 24 < 2) and md4 Water Level Protection`
- Lit : `Water Level mc 24`, `md4 Water Level Protection`
- Utilisé par : `KBB K8 DC - PUMP SHOWER`
- Ligne export : 91270 · id 218429

#### dtobin c10 B APPIN  `APPIN`
- Propriétés : Input channel=dtobin APPOUT C10 B · Error value=0
- Lit : `dtobin APPOUT C10 B`
- Utilisé par : `btod c10 B`
- Ligne export : 91331 · id 228948

#### B10 CABINE ON/OFF  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[9]
  ```
- Lit : `btod c10 B`
- Utilisé par : `Cabine Counter`, `KTB K4 IDC- Cabine`
- Ligne export : 91341 · id 228631

#### Cabine Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `(B1 Button Cabine IDC C10) OR (PositiveFlank(B10 CABINE ON/OFF))`
  - **Resetting** = `(Cabine Counter >= 2) OR (PositiveFlank(B10 CABINE ON/OFF)) OR (NegativeFlank(B10 CABINE ON/OFF))`
- Lit : `B1 Button Cabine IDC C10`, `B10 CABINE ON/OFF`
- Utilisé par : `KTB K4 IDC- Cabine`
- Ligne export : 91361 · id 218450

#### KTB K4 IDC- Cabine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B10 CABINE ON/OFF) OR (Cabine Counter)`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `B10 CABINE ON/OFF`, `Cabine Counter`
- Utilisé par : `ON_Bits 1 ktb`
- Ligne export : 91445 · id 218464

#### dtobin c10 B_1 APPIN  `APPIN`
- Propriétés : Input channel=dtobin APPOUT C10 B_1 · Error value=0
- Lit : `dtobin APPOUT C10 B_1`
- Utilisé par : `btod c10 B_1`
- Ligne export : 91502 · id 228951

#### btod c10 B_1  `ARC`
- Propriétés : Array size=15 · Store value=No
- Logique :
  ```qcode
  This[0]:=dtobin c10 B_1 APPIN mod 2
  This[1]:=(dtobin c10 B_1 APPIN div 2) mod 2
  This[2]:=(dtobin c10 B_1 APPIN div 4) mod 2
  This[3]:=(dtobin c10 B_1 APPIN div 8) mod 2
  This[4]:=(dtobin c10 B_1 APPIN div 16) mod 2
  This[5]:=(dtobin c10 B_1 APPIN div 32) mod 2
  This[6]:=(dtobin c10 B_1 APPIN div 64) mod 2
  This[7]:=(dtobin c10 B_1 APPIN div 128) mod 2
  This[8]:=(dtobin c10 B_1 APPIN div 256) mod 2
  This[9]:=(dtobin c10 B_1 APPIN div 512) mod 2
  This[10]:=(dtobin c10 B_1 APPIN div 1024) mod 2
  This[11]:=(dtobin c10 B_1 APPIN div 2048) mod 2
  This[12]:=(dtobin c10 B_1 APPIN div 4096) mod 2
  This[13]:=(dtobin c10 B_1 APPIN div 8192) mod 2
  This[14]:=(dtobin c10 B_1 APPIN div 16384) mod 2
  ```
- Lit : `dtobin c10 B_1 APPIN`
- Utilisé par : `B10_1 OutBoard Button`, `B11_1 FAN WIND`, `B12_1 AUX 3`, `B13_1 Wipper Button`, `B14_1 SHOWER`, `B15_1 md4 Seat position`, `B1_1 AUX 2`, `B2_1 LD UP - Force`, `B3_1 LD DOWN - Force`, `B4_1 ANCHOR UP`, `B5_1 ANCHOR DOWN`, `B6_1 AUX 1`, `B7_1 WIND CLEANER`, `B8_1 BILGE`, `B9_1 Seat Power Force`
- Ligne export : 91512 · id 228680

#### B7_1 WIND CLEANER  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[6]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `Wind Cleaner IDC`, `Wind Cleaner Wipper IDC`
- Ligne export : 91546 · id 228779

#### Wind Cleaner IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  - **Activating** = `PositiveFlank(B7_1 WIND CLEANER)`
- Lit : `B7_1 WIND CLEANER`
- Utilisé par : `KBB K9 IDC - PUMP WIND`
- Ligne export : 91566 · id 218475

#### B13_1 Wipper Button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[12]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `Wipper Button 2 s`, `Wipper State`
- Ligne export : 91610 · id 228828

#### Wipper Button 2 s  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `B13_1 Wipper Button`
- Lit : `B13_1 Wipper Button`
- Utilisé par : `Wipper State`
- Ligne export : 91630 · id 218484

#### Wipper State  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(B13_1 Wipper Button)`
  - **Resetting** = `(Wipper State >= 4) OR (PositiveFlank(Wipper Button 2 s))`
- Lit : `B13_1 Wipper Button`, `Wipper Button 2 s`
- Utilisé par : `KTC K1 IDC - Wipper On/Off`, `KTC K2 IDC - Wipper Speed`, `SMC Wipper`, `Wipper Timer`, `MD4-10 page: MAIN`
- Ligne export : 91673 · id 218492

#### md4 Wiper delay  `IP`
- Propriétés : Unit=s · Default mode={5}
- Utilisé par : `Wipper Timer`
- Ligne export : 91742 · id 218504

#### Wipper Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Wipper State = 1`
  - **Resetting** = `(Wipper Timer [s] > md4 Wiper delay [s]) OR (Wipper State <> 1)`
- Lit : `Wipper State`, `md4 Wiper delay`
- Utilisé par : `Wipper Start Inter`
- Ligne export : 91754 · id 218505

#### Wipper Start Inter  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Wipper Timer [s] > 0`
- Lit : `Wipper Timer`
- Utilisé par : `Wipper Int IDC`
- Ligne export : 91826 · id 218517

#### Wipper Int IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(Wipper Start Inter)`
- Lit : `Wipper Start Inter`
- Utilisé par : `KTC K1 IDC - Wipper On/Off`
- Ligne export : 91871 · id 218525

#### Wind Cleaner Wipper IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `PositiveFlank(B7_1 WIND CLEANER)`
- Lit : `B7_1 WIND CLEANER`
- Utilisé par : `KTC K1 IDC - Wipper On/Off`
- Ligne export : 91915 · id 218533

#### KTC K1 IDC - Wipper On/Off  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Wipper Int IDC) OR (Wipper State > 1) OR (Wind Cleaner Wipper IDC)`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `Wind Cleaner Wipper IDC`, `Wipper Int IDC`, `Wipper State`
- Utilisé par : `ON_Bits 3 ktc`
- Ligne export : 91959 · id 218541

#### B10_1 OutBoard Button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[9]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `Auto Light and Start broken need brightness`, `Auto Off - Timer`, `Engine 1 - Wait`, `Engine 2 - Wait`, `Engine On`
- Ligne export : 92025 · id 228803

#### Auto Light and Start broken need brightness  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B9 START C10 or B10_1 OutBoard Button) AND False`
- Lit : `B10_1 OutBoard Button`, `B9 START C10`
- Utilisé par : `KTB K11 IDC True- SearchLight`, `KTB K5 IDC - HT - 360 White`, `KTB K6 IDC - NAV`
- Ligne export : 92045 · id 218553

#### Blink Light IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Blink Light`
- Lit : `Blink Light`
- Utilisé par : `Not Blink Light`, `Not Blink Light Mode`
- Ligne export : 92097 · id 218561

#### Not Blink Light Mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Blink Light IDC`
- Lit : `Blink Light IDC`
- Utilisé par : `Not Blink Light`
- Ligne export : 92140 · id 218569

#### Not Blink Light  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Blink Light IDC)`
  - **Blocking** = `not(Not Blink Light Mode)`
- Lit : `Blink Light IDC`, `Not Blink Light Mode`
- Utilisé par : *(personne)*
- Ligne export : 92183 · id 218577

#### B11 NAV + 360 LIGHT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[10]
  ```
- Lit : `btod c10 B`
- Utilisé par : `KTB K5 IDC - HT - 360 White`, `KTB K6 IDC - NAV`
- Ligne export : 92235 · id 228639

#### KTB K5 IDC - HT - 360 White  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B11 NAV + 360 LIGHT) OR (Auto Light and Start broken need brightness)`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Light and Start broken need brightness`, `Auto Off Lamps`, `B11 NAV + 360 LIGHT`
- Utilisé par : `ON_Bits 1 ktb`
- Ligne export : 92255 · id 218586

#### KTB K6 IDC - NAV  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B11 NAV + 360 LIGHT) OR (Auto Light and Start broken need brightness)`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Light and Start broken need brightness`, `Auto Off Lamps`, `B11 NAV + 360 LIGHT`
- Utilisé par : `ON_Bits 1 ktb`, `MD4-10 page: MAIN`
- Ligne export : 92312 · id 218596

#### B12 LIGHT HT SPOT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[11]
  ```
- Lit : `btod c10 B`
- Utilisé par : `KTB K7 IDC - HT - Spot`
- Ligne export : 92369 · id 228648

#### KTB K7 IDC - HT - Spot  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B12 LIGHT HT SPOT`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `B12 LIGHT HT SPOT`
- Utilisé par : `ON_Bits 1 ktb`
- Ligne export : 92389 · id 218607

#### B15 LIGHT HT DIM  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[14]
  ```
- Lit : `btod c10 B`
- Utilisé par : `KTB K8 DC - HT - DIM`
- Ligne export : 92439 · id 228672

#### KTB K8 DC - HT - DIM  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B15 LIGHT HT DIM`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `B15 LIGHT HT DIM`
- Utilisé par : `ON_Bits 1 ktb`
- Ligne export : 92459 · id 218617

#### A/C Clim KTBK9  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : *(personne)*
- Ligne export : 92509 · id 218626

#### KTB K9 IDC - Cockpit Light  `IDC`
> transom light
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B1_1 AUX 2`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `B1_1 AUX 2`
- Utilisé par : `ON_Bits 1 ktb`
- Ligne export : 92545 · id 218633

#### B14 Fridge  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[13]
  ```
- Lit : `btod c10 B`
- Utilisé par : `KTB K10 IDC - Fridge`
- Ligne export : 92595 · id 228664

#### KTB K10 IDC - Fridge  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B14 Fridge`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `B14 Fridge`
- Utilisé par : `ON_Bits 1 ktb`
- Ligne export : 92615 · id 218644

#### Remote  `IMAC`
- Logique :
  - **Controlling** = `Remote mc C`
- Lit : `Remote mc C`
- Utilisé par : `LD UP`, `Remote Down Wait 3s`, `Unlock Boat`
- Ligne export : 92665 · id 218655

#### B1 LD UP - VDIN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[0]
  ```
- Lit : `btod c10 B`
- Utilisé par : `LD UP`
- Ligne export : 92706 · id 228559

#### LD UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B1 LD UP - VDIN) OR (Remote = 1)`
- Lit : `B1 LD UP - VDIN`, `Remote`
- Utilisé par : `LD Down Toogle`, `LD UP - Wait`, `LD UP Toogle`, `MD4-10 page: SETUP`
- Ligne export : 92726 · id 218663

#### LD UP - Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `LD UP`
- Lit : `LD UP`
- Utilisé par : `LD UP Toogle`
- Ligne export : 92778 · id 218672

#### Remote Down Wait 3s  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Remote = 2`
- Lit : `Remote`
- Utilisé par : `LD DOWN`
- Ligne export : 92821 · id 218681

#### B2 LD DOWN - VDIN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[1]
  ```
- Lit : `btod c10 B`
- Utilisé par : `LD DOWN`
- Ligne export : 92866 · id 228567

#### LD DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B2 LD DOWN - VDIN) OR (Remote Down Wait 3s)`
- Lit : `B2 LD DOWN - VDIN`, `Remote Down Wait 3s`
- Utilisé par : `LD DOWN - Wait`, `LD Down Toogle`, `LD UP Toogle`, `MD4-10 page: SETUP`
- Ligne export : 92886 · id 218689

#### md4 Ladder Stop Sensor  `IP`
- Propriétés : Unit=Pulse/s · Default mode={100}
- Utilisé par : `Stop Ladder`
- Ligne export : 92936 · id 218698

#### md4 Ladder Protection  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `LD Down Toogle`, `LD UP Toogle`, `Stop Ladder`, `Adjust group: Master Config Options`, `Single adjust item: md4 Ladder Protection`
- Ligne export : 92948 · id 218699

#### B2_1 LD UP - Force  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[1]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `KBB K3 IDC - LD UP`
- Ligne export : 92961 · id 228739

#### Stop Ladder  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `(md4 Ladder Stop Sensor [Pulse/s] > Speed Mouvement [%/s]) and (LD UP Toogle or LD Down Toogle)`
  - **Blocking** = `not(md4 Ladder Protection)`
- Lit : `LD Down Toogle`, `LD UP Toogle`, `Speed Mouvement`, `md4 Ladder Protection`, `md4 Ladder Stop Sensor`
- Utilisé par : `LD Down Toogle`, `LD UP Toogle`, `Ladder Error Msg`
- Ligne export : 92981 · id 218710

#### Ladder Timer End  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `PositiveFlank((Ladder Timer [ms] <= 0))`
- Lit : `Ladder Timer`
- Utilisé par : `LD Down Toogle`, `LD UP Toogle`
- Ligne export : 93052 · id 218721

#### LD DOWN - Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `LD DOWN`
- Lit : `LD DOWN`
- Utilisé par : `LD Down Toogle`
- Ligne export : 93105 · id 218757

#### LD Down Toogle  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank(LD DOWN - Wait)) OR (LD Down Toogle and md4 Ladder Protection) OR (LD DOWN - Wait and (not(md4 Ladder Protection)))`
  - **Blocking** = `(PositiveFlank(LD UP)) OR (LD Down Toogle and (PositiveFlank(LD DOWN))) OR (Stop Ladder) OR (Ladder Timer End) OR (PositiveFlank((Ladder Position [%] < 4)))`
- Lit : `LD DOWN`, `LD DOWN - Wait`, `LD UP`, `Ladder Position`, `Ladder Timer End`, `Stop Ladder`, `md4 Ladder Protection`
- Utilisé par : `KBB K4 IDC- LD DOWN`, `Stop Ladder`
- Ligne export : 93148 · id 218765

#### LD UP Toogle  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank(LD UP - Wait)) OR (LD UP Toogle and md4 Ladder Protection) OR (LD UP - Wait and (not(md4 Ladder Protection)))`
  - **Blocking** = `(PositiveFlank(LD DOWN)) OR (LD UP Toogle and (PositiveFlank(LD UP))) OR (Stop Ladder) OR (Ladder Timer End)`
- Lit : `LD DOWN`, `LD UP`, `LD UP - Wait`, `Ladder Timer End`, `Stop Ladder`, `md4 Ladder Protection`
- Utilisé par : `KBB K3 IDC - LD UP`, `Stop Ladder`
- Ligne export : 93274 · id 218730

#### B3_1 LD DOWN - Force  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[2]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `KBB K4 IDC- LD DOWN`
- Ligne export : 93383 · id 228747

#### KBB K4 IDC- LD DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(LD Down Toogle) OR (B3_1 LD DOWN - Force)`
  - **Blocking** = `KBB K3 IDC - LD UP`
- Lit : `B3_1 LD DOWN - Force`, `KBB K3 IDC - LD UP`, `LD Down Toogle`
- Utilisé par : `KBB K3 IDC - LD UP`, `KTB K11 IDC True- SearchLight`, `Ladder Timer`, `ON_Bits 2 kbb`, `Power Down Timer Ask`
- Ligne export : 93403 · id 218700

#### KBB K3 IDC - LD UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(LD UP Toogle) OR (B2_1 LD UP - Force)`
  - **Blocking** = `KBB K4 IDC- LD DOWN`
- Lit : `B2_1 LD UP - Force`, `KBB K4 IDC- LD DOWN`, `LD UP Toogle`
- Utilisé par : `KBB K4 IDC- LD DOWN`, `KTB K11 IDC True- SearchLight`, `Ladder Timer`, `ON_Bits 2 kbb`, `Power Down Timer Ask`
- Ligne export : 93460 · id 218747

#### Speed Mouvement  `MAC`
- Propriétés : Unit=%/s · Limiting object group=Signed
- Logique :
  - **Controlling** = `Abs((DerivativeOf(Ladder_Sensor mc)))`
- Lit : `Ladder_Sensor mc`
- Utilisé par : `Stop Ladder`
- Ligne export : 93517 · id 218782

#### Ladder Timer  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=35000
- Logique :
  - **Decreasing** = `(KBB K3 IDC - LD UP) OR (KBB K4 IDC- LD DOWN)`
  - **Resetting** = `(PositiveFlank(KBB K3 IDC - LD UP)) OR (PositiveFlank(KBB K4 IDC- LD DOWN))`
- Lit : `KBB K3 IDC - LD UP`, `KBB K4 IDC- LD DOWN`
- Utilisé par : `Ladder Timer End`
- Ligne export : 93568 · id 218791

#### B13 Search Light  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[12]
  ```
- Lit : `btod c10 B`
- Utilisé par : `KTB K11 IDC True- SearchLight`
- Ligne export : 93643 · id 228656

#### KTB K11 IDC True- SearchLight  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B13 Search Light) OR (KBB K3 IDC - LD UP) OR (KBB K4 IDC- LD DOWN) OR ((Auto Light and Start broken need brightness and TRACK DOWN 4ET) and B9 START C10)`
- Lit : `Auto Light and Start broken need brightness`, `B13 Search Light`, `B9 START C10`, `KBB K3 IDC - LD UP`, `KBB K4 IDC- LD DOWN`, `TRACK DOWN 4ET`
- Utilisé par : `ON_Bits 1 ktb`
- Ligne export : 93663 · id 218804

#### B1_1 AUX 2  `IDC`
> transom
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[0]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `KTB K9 IDC - Cockpit Light`, `Need Charge 12v dcdc on C10`
- Ligne export : 93738 · id 228731

#### KTB K12 IDC - Aux 2  `IDC`
> courtsy, transom 99
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B12_1 AUX 3`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `B12_1 AUX 3`
- Utilisé par : `ON_Bits 1 ktb`
- Ligne export : 93758 · id 218819

#### B3 HT UP D  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[2]
  ```
- Lit : `btod c10 B`
- Utilisé par : `HT UP`
- Ligne export : 93808 · id 228575

#### HT UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B3 HT UP D`
- Lit : `B3 HT UP D`
- Utilisé par : `HT Down Toogle`, `HT UP - Wait`, `HT UP Toogle`
- Ligne export : 93828 · id 218832

#### HT UP - Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `HT UP`
- Lit : `HT UP`
- Utilisé par : `HT UP Toogle`, `KBB K1 IDC - HT - UP`
- Ligne export : 93871 · id 218840

#### B4 HT DOWN D  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B[3]
  ```
- Lit : `btod c10 B`
- Utilisé par : `HT DOWN`
- Ligne export : 93914 · id 228583

#### HT DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B4 HT DOWN D`
- Lit : `B4 HT DOWN D`
- Utilisé par : `HT DOWN - Wait`, `HT Down Toogle`, `HT UP Toogle`
- Ligne export : 93934 · id 218848

#### HT UP Toogle  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank(HT UP - Wait)) OR (HT UP Toogle)`
  - **Blocking** = `(PositiveFlank(HT DOWN)) OR (HT UP Toogle and (PositiveFlank(HT UP)))`
- Lit : `HT DOWN`, `HT UP`, `HT UP - Wait`
- Utilisé par : `HT Timer`
- Ligne export : 93977 · id 218856

#### HT DOWN - Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `HT DOWN`
- Lit : `HT DOWN`
- Utilisé par : `HT Down Toogle`, `KBB K2 IDC - HT -DOWN`
- Ligne export : 94053 · id 218868

#### HT Down Toogle  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank(HT DOWN - Wait)) OR (HT Down Toogle)`
  - **Blocking** = `(PositiveFlank(HT UP)) OR (HT Down Toogle and (PositiveFlank(HT DOWN)))`
- Lit : `HT DOWN`, `HT DOWN - Wait`, `HT UP`
- Utilisé par : `HT Timer`
- Ligne export : 94096 · id 218876

#### HT Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=Yes · Reset value=0
- Logique :
  - **Increasing** = `HT UP Toogle and (HT Timer [s] < 32)`
  - **Decreasing** = `HT Down Toogle`
- Lit : `HT Down Toogle`, `HT UP Toogle`
- Utilisé par : `KBB K1 IDC - HT - UP`, `KBB K2 IDC - HT -DOWN`, `MD4-10 page: MAIN`
- Ligne export : 94172 · id 218888

#### KBB K2 IDC - HT -DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `((DerivativeOf(HT Timer [s])) < 0) OR (HT DOWN - Wait)`
  - **Blocking** = `KBB K1 IDC - HT - UP`
- Lit : `HT DOWN - Wait`, `HT Timer`, `KBB K1 IDC - HT - UP`
- Utilisé par : `KBB K1 IDC - HT - UP`, `ON_Bits 2 kbb`
- Ligne export : 94249 · id 218901

#### KBB K1 IDC - HT - UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `((DerivativeOf(HT Timer [s])) > 0) OR (HT UP - Wait)`
  - **Blocking** = `KBB K2 IDC - HT -DOWN`
- Lit : `HT Timer`, `HT UP - Wait`, `KBB K2 IDC - HT -DOWN`
- Utilisé par : `KBB K2 IDC - HT -DOWN`, `ON_Bits 2 kbb`
- Ligne export : 94316 · id 218912

#### B4_1 ANCHOR UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[3]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `KBB K5 IDC - ANCHOR UP`, `KBB K6 IDC - ANCHOR DOWN`
- Ligne export : 94383 · id 228755

#### B5_1 ANCHOR DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[4]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `KBB K5 IDC - ANCHOR UP`, `KBB K6 IDC - ANCHOR DOWN`
- Ligne export : 94403 · id 228763

#### KBB K5 IDC - ANCHOR UP  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `B4_1 ANCHOR UP`
  - **Blocking** = `B5_1 ANCHOR DOWN`
- Lit : `B4_1 ANCHOR UP`, `B5_1 ANCHOR DOWN`
- Utilisé par : `ON_Bits 2 kbb`
- Ligne export : 94423 · id 218925

#### KBB K6 IDC - ANCHOR DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `B5_1 ANCHOR DOWN`
  - **Blocking** = `B4_1 ANCHOR UP`
- Lit : `B4_1 ANCHOR UP`, `B5_1 ANCHOR DOWN`
- Utilisé par : `ON_Bits 2 kbb`
- Ligne export : 94473 · id 218934

#### B6_1 AUX 1  `IDC`
> gps2
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[5]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `KTC K7 IDC - Aux B`, `Need Charge 12v dcdc on C10`
- Ligne export : 94523 · id 228771

#### KBB K7 IDC - AUX 1  `IDC`
> flir?
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B6 md4 AUX 4`
- Lit : `B6 md4 AUX 4`
- Utilisé par : `ON_Bits 2 kbb`
- Ligne export : 94543 · id 218944

#### B14_1 SHOWER  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[13]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `KBB K8 DC - PUMP SHOWER`
- Ligne export : 94586 · id 228836

#### KBB K8 DC - PUMP SHOWER  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B14_1 SHOWER`
  - **Blocking** = `(Auto Off Lamps) OR (LOW Level)`
- Lit : `Auto Off Lamps`, `B14_1 SHOWER`, `LOW Level`
- Utilisé par : `ON_Bits 2 kbb`
- Ligne export : 94606 · id 218955

#### KBB K9 IDC - PUMP WIND  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Wind Cleaner IDC`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `Wind Cleaner IDC`
- Utilisé par : `ON_Bits 2 kbb`
- Ligne export : 94663 · id 218965

#### KBB K10 IDC - AUTO OFF POWER BOX  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `Auto Off Cmd`
- Lit : `Auto Off Cmd`
- Utilisé par : `ON_Bits 2 kbb`
- Ligne export : 94713 · id 218974

#### KBB K11 IDC - DOOR  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B2 Door IDC C10`
- Lit : `B2 Door IDC C10`
- Utilisé par : `ON_Bits 2 kbb`
- Ligne export : 94756 · id 218993

#### B8_1 BILGE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[7]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `KBB K12 IDC - BILGE`
- Ligne export : 94799 · id 228787

#### KBB K12 IDC - BILGE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B8_1 BILGE`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `B8_1 BILGE`
- Utilisé par : `ON_Bits 2 kbb`
- Ligne export : 94819 · id 219002

#### KTC K2 IDC - Wipper Speed  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Wipper State = 3`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `Wipper State`
- Utilisé par : `ON_Bits 3 ktc`
- Ligne export : 95186 · id 219071

#### B9_1 Seat Power Force  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[8]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `KTC K3 IDC - Seat Power`
- Ligne export : 95238 · id 228795

#### KTC K3 IDC - Seat Power  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Alim Seat) OR (B9_1 Seat Power Force) OR (not(electronic seat))`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Alim Seat`, `Auto Off Lamps`, `B9_1 Seat Power Force`, `electronic seat`
- Utilisé par : `ON_Bits 3 ktc`
- Ligne export : 95258 · id 219081

#### KTC K4 IDC - Water Cooling  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `E rad FAN OUT`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `E rad FAN OUT`
- Utilisé par : `ON_Bits 3 ktc`
- Ligne export : 95323 · id 219091

#### KTC K5 IDC - Pump Water  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `E water PUMP VAR`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `E water PUMP VAR`
- Utilisé par : `ON_Bits 3 ktc`
- Ligne export : 95373 · id 219100

#### KTC K7 IDC - Aux B  `IDC`
> gps2 or cotek 99
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(B6_1 AUX 1) OR (KTC K9 IDC - OutBoard On-OFF)`
- Lit : `B6_1 AUX 1`, `KTC K9 IDC - OutBoard On-OFF`
- Utilisé par : `ON_Bits 3 ktc`
- Ligne export : 95423 · id 219109

#### KTC K6 IDC - Aux A - AC  `IDC`
> batt 24 on
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B8 md4 AUX 5) OR ((not(auto off tyva 24v APPIN)) and a/c option tyva APPIN)`
- Lit : `B8 md4 AUX 5`, `a/c option tyva APPIN`, `auto off tyva 24v APPIN`
- Utilisé par : `ON_Bits 3 ktc`
- Ligne export : 95473 · id 219116

#### B11_1 FAN WIND  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[10]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `KTC K8 DC - Fan wind cmd`
- Ligne export : 95533 · id 228811

#### KTC K8 DC - Fan wind cmd  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B11_1 FAN WIND`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `B11_1 FAN WIND`
- Utilisé par : `ON_Bits 3 ktc`
- Ligne export : 95553 · id 219123

#### Trim Mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `PositiveFlank(B9 START C10)`
- Lit : `B9 START C10`
- Utilisé par : `Engine On`
- Ligne export : 95603 · id 219133

#### Engine On  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B10_1 OutBoard Button) OR (Trim Mode) OR (B3 Main page on C10_1)`
- Lit : `B10_1 OutBoard Button`, `B3 Main page on C10_1`, `Trim Mode`
- Utilisé par : *(personne)*
- Ligne export : 95647 · id 219141

#### KTC K9 IDC - OutBoard On-OFF  `IDC`
> cotek on
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `B8 md4 AUX 5`
- Lit : `B8 md4 AUX 5`
- Utilisé par : `KTC K7 IDC - Aux B`, `ON_Bits 3 ktc`
- Ligne export : 95704 · id 219151

#### Engine 1 - Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `B10_1 OutBoard Button`
- Lit : `B10_1 OutBoard Button`
- Utilisé par : `Engine 1 - Flank`
- Ligne export : 95747 · id 219159

#### Engine 1 - Flank  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(Engine 1 - Wait)`
- Lit : `Engine 1 - Wait`
- Utilisé par : *(personne)*
- Ligne export : 95790 · id 219167

#### KTC K10 IDC - OutBoard Start PORT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `ON_Bits 3 ktc`
- Ligne export : 95834 · id 219175

#### md4 Engine Time Starting  `IP`
- Propriétés : Unit=ms · Default mode={500}
- Utilisé par : `Engine 2 - Wait`
- Ligne export : 95870 · id 219182

#### Engine 2 - Wait  `IDC`
- Propriétés : Toggle=No · Delay on=md4 Engine Time Starting [ms] · Delay off=0
- Logique :
  - **Activating** = `B10_1 OutBoard Button`
- Lit : `B10_1 OutBoard Button`, `md4 Engine Time Starting`
- Utilisé par : `Engine 2 - Flank`
- Ligne export : 95882 · id 219183

#### Engine 2 - Flank  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(Engine 2 - Wait)`
- Lit : `Engine 2 - Wait`
- Utilisé par : *(personne)*
- Ligne export : 95925 · id 219191

#### KTC K11 IDC - OutBoard Start STBD  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Utilisé par : `ON_Bits 3 ktc`
- Ligne export : 95969 · id 219199

#### B12_1 AUX 3  `IDC`
> transom
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[11]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `KTB K12 IDC - Aux 2`, `Need Charge 12v dcdc on C10`
- Ligne export : 96005 · id 228820

#### KTC K12 IDC - AUX 3  `IDC`
> dcdc 91
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Battery OK DCDC) OR (Charger end of charge but balancing)`
- Lit : `Battery OK DCDC`, `Charger end of charge but balancing`
- Utilisé par : `ON_Bits 3 ktc`
- Ligne export : 96025 · id 219214

#### SMC Wipper  `SMC`
- Propriétés : Default state name=OFF
- Fonction *INT* :
  - **Activating** = `Wipper State = 1`
- Fonction *Speed 1* :
  - **Activating** = `Wipper State = 2`
- Fonction *Speed 2* :
  - **Activating** = `Wipper State = 3`
- Lit : `Wipper State`
- Utilisé par : *(personne)*
- Ligne export : 96075 · id 219229

#### Unlock Boat  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((Remote > 0))) OR (Unlock Boat)`
- Lit : `Remote`
- Utilisé par : *(personne)*
- Ligne export : 96183 · id 219245

#### Ladder Position  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Ladder_Sensor mc: 0->0, 13000->100, Freeze)`
- Lit : `Ladder_Sensor mc`
- Utilisé par : `LD Down Toogle`, `Ladder Error Msg`, `Ladder is not up`, `MD4-10 page: MAIN`, `MD4-10 page: SHUTDOWN`
- Ligne export : 96243 · id 219306

#### Ladder Error Msg  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Ladder · Text=Ladder malfunction. Check sensor calibration or contact a service center. · Channel=Ladder Position [%]
- Logique :
  - **Showing** = `(Inside(Ladder Position [%], 2, 98)) AND (Stop Ladder)`
- Lit : `Ladder Position`, `Stop Ladder`
- Utilisé par : *(personne)*
- Ligne export : 96290 · id 219314

#### Need Charge 12v dcdc on C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B6_1 AUX 1 and md4 Aux 1 - Need HT) OR (B1_1 AUX 2 and md4 Aux 2 - Need HT) OR (B12_1 AUX 3 and md4 Aux 3 - Need HT) OR (B6 md4 AUX 4 and md4 Aux 4 - Need HT) OR (B8 md4 AUX 5 and md4 Aux 5 - Need HT)`
- Lit : `B12_1 AUX 3`, `B1_1 AUX 2`, `B6 md4 AUX 4`, `B6_1 AUX 1`, `B8 md4 AUX 5`, `md4 Aux 1 - Need HT`, `md4 Aux 2 - Need HT`, `md4 Aux 3 - Need HT`, `md4 Aux 4 - Need HT`, `md4 Aux 5 - Need HT`
- Utilisé par : `DCDC Ask to charge E mc`
- Ligne export : 96346 · id 219323

#### md4 Single Button Equipement?  `DP`
> Gather GPS, NMEA, Audio, VHF AIS under the same Keybox output
- Propriétés : True text=Single button · False text=Dedicated buttons · Default mode={False}
- Utilisé par : `Equipment button mode`, `Is multi button Eqt`, `Is single button Eqt`
- Ligne export : 96427 · id 219335

#### Is single button Eqt  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `md4 Single Button Equipement?`
- Lit : `md4 Single Button Equipement?`
- Utilisé par : `VHF - Show if SIngle Button Eqt`
- Ligne export : 96440 · id 219336

#### Is multi button Eqt  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(md4 Single Button Equipement?)`
- Lit : `md4 Single Button Equipement?`
- Utilisé par : `trameb 3`, `MD4-10 page: FEATURE`
- Ligne export : 98212 · id 219924

#### Equipment button mode  `SMC`
- Propriétés : Default state name=Multi button Equipement
- Fonction *Single Button Equipement* :
  - **Activating** = `md4 Single Button Equipement?`
- Lit : `md4 Single Button Equipement?`
- Utilisé par : `Equipment button`
- Ligne export : 98256 · id 219932

#### Equipment button  `TP`
- Propriétés : Mode selector=Equipment button mode · Default mode: Multi button Equipement={GPS} · Mode 1: Single Button Equipement={EQT}
- Lit : `Equipment button mode`
- Utilisé par : `MD4-10 page: FEATURE`
- Ligne export : 98296 · id 219940

#### ON_Bits 1 ktb  `IMAC`
- Logique :
  ```qcode
  Result := KTB K1 IDC - GPS_EQT  * 1 + KTB K2 IDC - AUDIO/AUX 4  * 2 + KTB K3 IDC - VHF/AUX 5 * 4 + KTB K4 IDC- Cabine * 8 + KTB K5 IDC - HT - 360 White * 16 + KTB K6 IDC - NAV * 32 + KTB K7 IDC - HT - Spot * 64 + KTB K8 DC - HT - DIM * 128 + KTB K9 IDC - Cockpit Light * 256 + KTB K10 IDC - Fridge * 512 + KTB K11 IDC True- SearchLight * 1024 + KTB K12 IDC - Aux 2 * 2048 + 0 * 4096
  ```
- Lit : `KTB K1 IDC - GPS_EQT`, `KTB K10 IDC - Fridge`, `KTB K11 IDC True- SearchLight`, `KTB K12 IDC - Aux 2`, `KTB K2 IDC - AUDIO/AUX 4`, `KTB K3 IDC - VHF/AUX 5`, `KTB K4 IDC- Cabine`, `KTB K5 IDC - HT - 360 White`, `KTB K6 IDC - NAV`, `KTB K7 IDC - HT - Spot`, `KTB K8 DC - HT - DIM`, `KTB K9 IDC - Cockpit Light`
- Utilisé par : `OFF_Bits 1`, `ON_Bits_GOUT 1`
- Ligne export : 98309 · id 219766

#### ON_Bits 2 kbb  `IMAC`
- Logique :
  ```qcode
  Result := KBB K1 IDC - HT - UP * 1 + KBB K2 IDC - HT -DOWN  * 2 + KBB K3 IDC - LD UP * 4 + KBB K4 IDC- LD DOWN * 8 + KBB K5 IDC - ANCHOR UP * 16 + KBB K6 IDC - ANCHOR DOWN * 32 + KBB K7 IDC - AUX 1 * 64 + KBB K8 DC - PUMP SHOWER * 128 + KBB K9 IDC - PUMP WIND * 256 + KBB K10 IDC - AUTO OFF POWER BOX * 512 + KBB K11 IDC - DOOR * 1024 + KBB K12 IDC - BILGE * 2048 + 0 * 4096
  ```
- Lit : `KBB K1 IDC - HT - UP`, `KBB K10 IDC - AUTO OFF POWER BOX`, `KBB K11 IDC - DOOR`, `KBB K12 IDC - BILGE`, `KBB K2 IDC - HT -DOWN`, `KBB K3 IDC - LD UP`, `KBB K4 IDC- LD DOWN`, `KBB K5 IDC - ANCHOR UP`, `KBB K6 IDC - ANCHOR DOWN`, `KBB K7 IDC - AUX 1`, `KBB K8 DC - PUMP SHOWER`, `KBB K9 IDC - PUMP WIND`
- Utilisé par : `OFF_Bits 2`, `ON_Bits_GOUT 2`
- Ligne export : 98327 · id 219823

#### ON_Bits 3 ktc  `IMAC`
- Logique :
  ```qcode
  Result := KTC K1 IDC - Wipper On/Off * 1 + KTC K2 IDC - Wipper Speed  * 2 + KTC K3 IDC - Seat Power* 4 + KTC K4 IDC - Water Cooling * 8 + KTC K5 IDC - Pump Water * 16 + KTC K6 IDC - Aux A - AC * 32 + KTC K7 IDC - Aux B * 64 + KTC K8 DC - Fan wind cmd * 128 + KTC K9 IDC - OutBoard On-OFF * 256 + KTC K10 IDC - OutBoard Start PORT * 512 + KTC K11 IDC - OutBoard Start STBD * 1024 + KTC K12 IDC - AUX 3 * 2048 + 0 * 4096
  ```
- Lit : `KTC K1 IDC - Wipper On/Off`, `KTC K10 IDC - OutBoard Start PORT`, `KTC K11 IDC - OutBoard Start STBD`, `KTC K12 IDC - AUX 3`, `KTC K2 IDC - Wipper Speed`, `KTC K3 IDC - Seat Power`, `KTC K4 IDC - Water Cooling`, `KTC K5 IDC - Pump Water`, `KTC K6 IDC - Aux A - AC`, `KTC K7 IDC - Aux B`, `KTC K8 DC - Fan wind cmd`, `KTC K9 IDC - OutBoard On-OFF`
- Utilisé par : `OFF_Bits 3`, `ON_Bits_GOUT 3`
- Ligne export : 98345 · id 219880

#### B15_1 md4 Seat position  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10 B_1[14]
  ```
- Lit : `btod c10 B_1`
- Utilisé par : `Alim Seat`, `Seat State`
- Ligne export : 98363 · id 228844

#### True1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True`
- Utilisé par : *(personne)*
- Ligne export : 98390 · id 234800

#### auto off tyva 24v APPIN  `APPIN`
- Propriétés : Input channel=auto off tyva 24v APPOUT
- Lit : `auto off tyva 24v APPOUT`
- Utilisé par : `KTC K6 IDC - Aux A - AC`
- Ligne export : 98433 · id 235402

#### a/c option tyva APPIN  `APPIN`
- Propriétés : Input channel=a/c option tyva APPOUT
- Lit : `a/c option tyva APPOUT`
- Utilisé par : `KTC K6 IDC - Aux A - AC`
- Ligne export : 98442 · id 236463

## logic screen c10 and KB / cEQUIPEMENT / Options

#### md4 Aux 1 - Show  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Adjust group: Master Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: md4 Aux 1 - Show`
- Ligne export : 96498 · id 219345

#### md4 Aux 1 - Text  `TP`
- Propriétés : Default mode={AUX 1}
- Lit : `AUX 1`
- Utilisé par : `Adjust group: Master Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: md4 Aux 1 - Text`
- Ligne export : 96511 · id 219346

#### md4 Aux 1 - Need HT  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Need Charge 12v dcdc on C10`, `Adjust group: Master Config Options`, `Single adjust item: md4 Aux 1 - Need HT`
- Ligne export : 96522 · id 219347

#### md4 Aux 2 - Show  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Adjust group: Master Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: md4 Aux 2 - Show`
- Ligne export : 96535 · id 219348

#### md4 Aux 2 - Text  `TP`
- Propriétés : Default mode={AUX 2}
- Lit : `AUX 2`
- Utilisé par : `Adjust group: Master Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: md4 Aux 2 - Text`
- Ligne export : 96548 · id 219349

#### md4 Aux 2 - Need HT  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Need Charge 12v dcdc on C10`, `Adjust group: Master Config Options`, `Single adjust item: md4 Aux 2 - Need HT`
- Ligne export : 96559 · id 219350

#### md4 Aux 3 - Show  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Adjust group: Master Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: md4 Aux 3 - Show`
- Ligne export : 96572 · id 219351

#### md4 Aux 3 - Text  `TP`
- Propriétés : Default mode={AUX 3}
- Lit : `AUX 3`
- Utilisé par : `Adjust group: Master Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: md4 Aux 3 - Text`
- Ligne export : 96585 · id 219352

#### md4 Aux 3 - Need HT  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Need Charge 12v dcdc on C10`, `Adjust group: Master Config Options`, `Single adjust item: md4 Aux 3 - Need HT`
- Ligne export : 96596 · id 219353

#### md4 VHF - Show  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `VHF - Show if SIngle Button Eqt`, `Adjust group: Master Config Options`, `Single adjust item: md4 VHF - Show`
- Ligne export : 96609 · id 219354

#### md4 Fridge - Show  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `Adjust group: Master Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: md4 Fridge - Show`
- Ligne export : 96622 · id 219355

#### VHF - Show if SIngle Button Eqt  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `md4 VHF - Show`
  - **Blocking** = `Is single button Eqt`
- Lit : `Is single button Eqt`, `md4 VHF - Show`
- Utilisé par : *(personne)*
- Ligne export : 96635 · id 219363

#### md4 Aux 4 - Show  `DP`
> New Option for single button Eqipement (KTB07, ex Audio)
- Propriétés : Default mode={False}
- Utilisé par : `Adjust group: Master Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: md4 Aux 4 - Show`
- Ligne export : 96685 · id 219357

#### md4 Aux 4 - Text  `TP`
> New Option for single button Eqipement (KTB07, ex Audio)
- Propriétés : Default mode={AUX 4}
- Utilisé par : `Adjust group: Master Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: md4 Aux 4 - Text`
- Ligne export : 96698 · id 219358

#### md4 Aux 4 - Need HT  `DP`
> New Option for single button Eqipement (KTB07, ex Audio)
- Propriétés : Default mode={False}
- Utilisé par : `KTB K2 IDC - AUDIO/AUX 4`, `Need Charge 12v dcdc on C10`
- Ligne export : 96709 · id 219359

#### md4 Aux 5- Show  `DP`
> New Option for single button Eqipement (KTB08, ex VHF)
- Propriétés : Default mode={False}
- Utilisé par : `Adjust group: Master Config Options`, `Single adjust item: md4 Aux 5- Show`
- Ligne export : 96722 · id 219360

#### AC  `TP`
> New Option for single button Eqipement (KTB08, ex VHF)
- Propriétés : Default mode={AUX 5}
- Utilisé par : `Adjust group: Master Config Options`, `Adjust group: Setup Charger`, `MD4-10 page: FEATURE`, `Single adjust item: AC`
- Ligne export : 96735 · id 219361

#### md4 Aux 5 - Need HT  `DP`
> New Option for single button Eqipement (KTB08, ex VHF)
- Propriétés : Default mode={False}
- Utilisé par : `Need Charge 12v dcdc on C10`
- Ligne export : 96746 · id 219362

## logic screen c10 and KB / cEQUIPEMENT / Power

#### md4 Auto Global switch Off  `IP`
- Propriétés : Unit=min · Default mode={120}
- Utilisé par : `Auto Off - Timer`
- Ligne export : 96775 · id 219373

#### Power Down State C10  `FSM`
- Propriétés : Store value=No · Resetting channel=B7 CONTINUE C10
- État 0 **Power On**
  - transition *Ask Stop* (état cible non exporté par IQANdesign)
    - **Activating** = `(Off Button - IDC) OR (Charger End Charge and md4 Auto Off After Charge?)`
- État 1 **Power Down**
  - transition *Time to Down* (état cible non exporté par IQANdesign)
    - **Activating** = `Power Down Timer`
- État 2 **Stop**
- Lit : `B7 CONTINUE C10`, `Charger End Charge`, `Off Button - IDC`, `Power Down Timer`, `md4 Auto Off After Charge?`
- Utilisé par : `Auto Off Cmd`, `Power Down`, `Power Down Timer Ask`, `System Shutdown`
- Ligne export : 96787 · id 219374

#### Power Down Timer Ask  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Power Down State C10 = 1) AND (not(KBB K3 IDC - LD UP)) AND (not(KBB K4 IDC- LD DOWN))`
- Lit : `KBB K3 IDC - LD UP`, `KBB K4 IDC- LD DOWN`, `Power Down State C10`
- Utilisé par : `BarTimer`, `Power Down Timer`
- Ligne export : 96880 · id 219392

#### Time ask Power Down  `IP`
- Propriétés : Unit=ms · Default mode={3000}
- Utilisé par : `Power Down Timer`, `ShutDownBar`
- Ligne export : 96941 · id 219402

#### Power Down Timer  `IDC`
- Propriétés : Toggle=No · Delay on=Time ask Power Down [ms] · Delay off=0
- Logique :
  - **Activating** = `Power Down Timer Ask`
- Lit : `Power Down Timer Ask`, `Time ask Power Down`
- Utilisé par : `Power Down State C10`
- Ligne export : 96953 · id 219403

#### Time ask remote  `IP`
- Propriétés : Unit=ms · Default mode={5000}
- Utilisé par : `Remote Ask Stop`
- Ligne export : 96996 · id 219411

#### Remote Ask Stop  `IDC`
- Propriétés : Toggle=No · Delay on=Time ask remote [ms] · Delay off=0
- Logique :
  - **Activating** = `Remote mc C = 2`
- Lit : `Remote mc C`, `Time ask remote`
- Utilisé par : `Off Button - IDC`
- Ligne export : 97008 · id 219412

#### Auto Off - Timer  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=md4 Auto Global switch Off [min]
- Logique :
  - **Decreasing** = `True`
  - **Resetting** = `(B9 START C10) OR (B10_1 OutBoard Button) OR (PositiveFlank((2 = Auto Off Message))) OR (Charger Charging IDC)`
- Lit : `Auto Off Message`, `B10_1 OutBoard Button`, `B9 START C10`, `Charger Charging IDC`, `md4 Auto Global switch Off`
- Utilisé par : `Auto Off Message`, `Off Button - IDC`
- Ligne export : 97053 · id 219421

#### Auto Off Message  `IMSG`
- Propriétés : Show message=All · Dialog type=Confirmation · Header=Automatic Shutdown · Text=I seems that you don't use the boat, press Continue to keep the boat ON. If not the boat will stop in 30 minutes. · Left button=Continue · Right button=OFF
- Logique :
  - **Showing** = `Auto Off - Timer [min] <= 20`
- Lit : `Auto Off - Timer`
- Utilisé par : `Auto Off - Timer`
- Ligne export : 97143 · id 219436

#### Charger Charging IDC  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `E.Charging State Machine = 2`
- Lit : `E.Charging State Machine`
- Utilisé par : `Auto Off - Timer`, `Charging State`
- Ligne export : 97193 · id 219444

#### Off Button - IDC  `IDC`
- Propriétés : Toggle=No · Delay on=100 · Delay off=0
- Logique :
  - **Activating** = `(B6 OFF C10) OR (Auto Off - Timer [min] <= 0) OR (Remote Ask Stop)`
- Lit : `Auto Off - Timer`, `B6 OFF C10`, `Remote Ask Stop`
- Utilisé par : `Power Down State C10`
- Ligne export : 97238 · id 219452

#### Charger End Charge  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `PositiveFlank((3 = E.Charging State Machine))`
- Lit : `E.Charging State Machine`
- Utilisé par : `Power Down State C10`
- Ligne export : 97297 · id 219462

#### Charging State  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Charger Charging IDC`
  - **Blocking** = `B7 CONTINUE C10`
- Lit : `B7 CONTINUE C10`, `Charger Charging IDC`
- Utilisé par : `Charger Charging Wait 2 minutes`
- Ligne export : 97350 · id 219471

#### Charger Charging Wait 2 minutes  `IDC`
- Propriétés : Toggle=No · Delay on=120000 · Delay off=0
- Logique :
  - **Activating** = `Charging State`
- Lit : `Charging State`
- Utilisé par : `Auto Off Lamps`
- Ligne export : 97400 · id 219480

#### Auto Off Cmd  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `Power Down State C10 = 2`
- Lit : `Power Down State C10`
- Utilisé par : `KBB K10 IDC - AUTO OFF POWER BOX`
- Ligne export : 97443 · id 219488

#### Power Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Power Down State C10 = 1`
- Lit : `Power Down State C10`
- Utilisé par : `Auto Off Lamps`, `Power Down Lights Timer`
- Ligne export : 97488 · id 219496

#### Press Remote  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Remote mc C`
- Lit : `Remote mc C`
- Utilisé par : `Start Lights Timer 1000`
- Ligne export : 97533 · id 219504

#### Charger Connected  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `1 = E.Charging State Machine`
- Lit : `E.Charging State Machine`
- Utilisé par : `Start Lights Gen`
- Ligne export : 97576 · id 219512

#### Start Lights Gen  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank(True) OR (PositiveFlank(Charger Connected))`
- Lit : `Charger Connected`
- Utilisé par : `Start Lights Timer`
- Ligne export : 97621 · id 219520

#### Start Lights Timer  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=2000
- Logique :
  - **Decreasing** = `True`
  - **Resetting** = `PositiveFlank(Start Lights Gen)`
- Lit : `Start Lights Gen`
- Utilisé par : `Start Lights`
- Ligne export : 97673 · id 219529

#### Start Lights  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Start Lights Timer [ms] mod 250) < 125`
  - **Blocking** = `Start Lights Timer [ms] <= 0`
- Lit : `Start Lights Timer`
- Utilisé par : `Blink Light`
- Ligne export : 97733 · id 219540

#### Power Down Lights Timer  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Power Down`
- Lit : `Power Down`
- Utilisé par : `Power Down Lights`
- Ligne export : 97796 · id 219550

#### Power Down Lights  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Power Down Lights Timer [ms] mod 2000) < 1900`
  - **Blocking** = `Power Down Lights Timer [ms] <= 0`
- Lit : `Power Down Lights Timer`
- Utilisé par : `Blink Light`
- Ligne export : 97848 · id 219560

#### Start Lights Timer 1000  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=1000
- Logique :
  - **Decreasing** = `True`
  - **Resetting** = `PositiveFlank(Press Remote)`
- Lit : `Press Remote`
- Utilisé par : `Start Lights 1000`
- Ligne export : 97911 · id 219570

#### Start Lights 1000  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Start Lights Timer 1000 [ms] mod 250) < 125`
  - **Blocking** = `Start Lights Timer 1000 [ms] <= 0`
- Lit : `Start Lights Timer 1000`
- Utilisé par : `Blink Light`
- Ligne export : 97971 · id 219581

#### Blink Light  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Start Lights) OR (Power Down Lights) OR (Start Lights 1000)`
- Lit : `Power Down Lights`, `Start Lights`, `Start Lights 1000`
- Utilisé par : `Blink Light IDC`
- Ligne export : 98034 · id 219591

#### BarTimer  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Power Down Timer Ask`
  - **Resetting** = `NegativeFlank(Power Down Timer Ask)`
- Lit : `Power Down Timer Ask`
- Utilisé par : `ShutDownBar`
- Ligne export : 98091 · id 219601

#### ShutDownBar  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(BarTimer [ms]: 0->0, Time ask Power Down [ms]->100, Freeze)`
- Lit : `BarTimer`, `Time ask Power Down`
- Utilisé par : `MD4-10 page: SHUTDOWN`, `MD4-5 page: SHUTDOWN`
- Ligne export : 98151 · id 219612

#### md4 Auto Off After Charge?  `DP`
> If False: Boat will remain on after charge
- Propriétés : True text=Yes · False text=No · Default mode={True}
- Utilisé par : `Power Down State C10`
- Ligne export : 98198 · id 219620

## logic screen c10 and KB / cEQUIPEMENT / SEAT

#### md4 Person 1  `TP`
- Propriétés : Default mode={John}
- Utilisé par : `Single adjust item: Person 1`
- Ligne export : 94884 · id 219020

#### md4 Person 2  `TP`
- Propriétés : Default mode={Steve}
- Utilisé par : `Single adjust item: Person 2`
- Ligne export : 94895 · id 219021

#### md4 Person 3  `TP`
- Propriétés : Default mode={Florent}
- Utilisé par : `Single adjust item: Person 3`
- Ligne export : 94906 · id 219022

#### md4 Person  `SP`
- Propriétés : Input channel=None · Default state name=md4 Person 1 · States={md4 Person 2; md4 Person 3}
- Utilisé par : `md4 Seat Front Back`, `md4 Seat Up Down`, `Single adjust item: Person`
- Ligne export : 94917 · id 219023

#### md4 Seat Up Down  `IP`
- Propriétés : Unit=% · Mode selector=md4 Person · Default mode: md4 Person 1={80} · Mode 1: md4 Person 2={80} · Mode 2: md4 Person 3={80}
- Lit : `md4 Person`
- Utilisé par : `Seat UP/DOWN MAC`, `Single adjust item: Seat Up Down`
- Ligne export : 94930 · id 219026

#### Seat State  `SMC`
- Propriétés : Default state name=Standing
- Fonction *Seating* :
  - **Activating** = `B15_1 md4 Seat position`
- Lit : `B15_1 md4 Seat position`
- Utilisé par : `Seat Front/Back MAC`
- Ligne export : 94946 · id 219028

#### Seat UP/DOWN MAC  `MAC`
- Propriétés : Limiting object group=Unsigned
- Logique :
  - **Controlling** = `md4 Seat Up Down [%]`
- Lit : `md4 Seat Up Down`
- Utilisé par : `Alim Seat`, `Seat UP/DOWN`
- Ligne export : 94986 · id 219036

#### md4 Seat Front Back  `IP`
- Propriétés : Unit=% · Mode selector=md4 Person · Default mode: md4 Person 1={80} · Mode 1: md4 Person 2={80} · Mode 2: md4 Person 3={80}
- Lit : `md4 Person`
- Utilisé par : `Seat Front/Back MAC`, `Single adjust item: Seat Front Back`
- Ligne export : 95028 · id 219044

#### Seat Front/Back MAC  `MAC`
- Propriétés : Limiting object group=Unsigned · Function selector=Seat State
- Fonction *Standing* :
  - **Controlling** = `0`
- Fonction *Seating* :
  - **Controlling** = `md4 Seat Front Back [%]`
- Lit : `Seat State`, `md4 Seat Front Back`
- Utilisé par : `Alim Seat`, `Seat Front Back`
- Ligne export : 95044 · id 219045

#### Alim Seat  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=20000
- Logique :
  - **Activating** = `(PositiveFlank(B15_1 md4 Seat position)) OR (NegativeFlank(B15_1 md4 Seat position)) OR (DerivativeOf(Seat UP/DOWN MAC)) OR (DerivativeOf(Seat Front/Back MAC))`
- Lit : `B15_1 md4 Seat position`, `Seat Front/Back MAC`, `Seat UP/DOWN MAC`
- Utilisé par : `KTC K3 IDC - Seat Power`
- Ligne export : 95117 · id 219060

## logic screen c10 and KB / mc.Accesory i/o CAB — actif seulement si `is_cab_mc`

#### C REMOTE LD UP mc 29  `DIN`
- Propriétés : Module=MC42-33 (MC42[0]) · Module index=13
- Utilisé par : `Remote mc C`
- Ligne export : 98963 · id 43512

#### C REMOTE LD DOWN mc 28  `DIN`
- Propriétés : Module=MC42-33 (MC42[0]) · Module index=12
- Utilisé par : `Remote mc C`
- Ligne export : 98973 · id 43511

#### Remote mc C  `SMC`
- Propriétés : Default state name=NO
- Fonction *UP* :
  - **Activating** = `C REMOTE LD UP mc 29`
- Fonction *DOWN* :
  - **Activating** = `C REMOTE LD DOWN mc 28`
- Lit : `C REMOTE LD DOWN mc 28`, `C REMOTE LD UP mc 29`
- Utilisé par : `Press Remote`, `Remote`, `Remote Ask Stop`
- Ligne export : 98983 · id 46120

#### mc Reset Ladder Sensor when UP  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `C Ladder_Sensor mc 11`, `Single adjust item: Reset Ladder Sensor when UP`
- Ligne export : 99054 · id 53889

#### C Ladder_Sensor mc 11  `DPCNT`
> Ladder
- Propriétés : Sensor type=Quadrature · Accumulate=Yes · Store value=Yes · Resetting channel=mc Reset Ladder Sensor when UP · Reset value=0 · Max=1 · Scaled max=1 · Alarms={No; 0; No; 100} · Module=MC42-33 (MC42[0]) · Module index=0
- Lit : `mc Reset Ladder Sensor when UP`
- Utilisé par : `Ladder_Sensor mc`, `MD4-10 page: SETUP`
- Ligne export : 99067 · id 52431

#### Convert bilge current  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Abs((DerivativeOf(bildge current to p)))`
- Lit : `bildge current to p`
- Utilisé par : `Convert bilge current Filter`
- Ligne export : 99090 · id 55279

#### Convert bilge current Filter  `SFC`
- Propriétés : Input channel=Convert bilge current · Enable=Yes · Type=Filter · Filter=95
- Lit : `Convert bilge current`
- Utilisé par : `Bilge Pump Run`
- Ligne export : 99141 · id 55288

#### Bilge Pump Run  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `Convert bilge current Filter >= 10`
- Lit : `Convert bilge current Filter`
- Utilisé par : `C Bilge Pump Run`
- Ligne export : 99153 · id 55289

#### C Bilge Pump Run  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header, English=e1158 Bilge Pump Run · Text, English=It seems you have water in the bildge.
- Logique :
  - **Showing** = `Bilge Pump Run`
  - **Hiding** = `NegativeFlank(Bilge Pump Run)`
- Lit : `Bilge Pump Run`
- Utilisé par : *(personne)*
- Ligne export : 99198 · id 55297

#### Ladder_Sensor mc  `IMAC`
- Logique :
  - **Controlling** = `Abs(C Ladder_Sensor mc 11)`
- Lit : `C Ladder_Sensor mc 11`
- Utilisé par : `Ladder Position`, `Speed Mouvement`
- Ligne export : 99252 · id 75769

#### Water Level mc 24  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `level to p`
- Lit : `level to p`
- Utilisé par : `LOW Level`, `MD4-10 page: FEATURE`, `MD4-10 page: SHUTDOWN`
- Ligne export : 99294 · id 229348

#### electronic seat  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `KTC K3 IDC - Seat Power`, `Active le groupe: logic screen c10 and KB / mc.Accesory i/o CAB / electronic seat`, `Adjust group: Master Config`, `Adjust group: Setup Seat`, `MD4-10 page: BASE`, `MD4-10 page: SETUP`, `Single adjust item: electronic seat`
- Ligne export : 99336 · id 235489

## logic screen c10 and KB / mc.Accesory i/o CAB / electronic seat — actif seulement si `electronic seat`

#### Seat UP/DOWN  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `Seat UP/DOWN MAC`
- Lit : `Seat UP/DOWN MAC`
- Utilisé par : `C UP/DOWN mc 45`
- Ligne export : 99364 · id 53379

#### C UP/DOWN mc 45  `PWM`
- Propriétés : Bidirectional=No · BWL=0 · Input channel=Seat UP/DOWN [%] · Default mode={{0; 85; 0; 0}} · Module=MC42-33 (MC42[0]) · Module index=6
- Lit : `Seat UP/DOWN`
- Utilisé par : *(personne)*
- Ligne export : 99405 · id 43502

#### Seat Front Back  `IMAC`
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `Seat Front/Back MAC`
- Lit : `Seat Front/Back MAC`
- Utilisé par : `C FRONT BACK mc 48`, `Adjust group: Setup Seat`
- Ligne export : 99426 · id 53392

#### C FRONT BACK mc 48  `PWM`
- Propriétés : Bidirectional=No · BWL=0 · Input channel=Seat Front Back [%] · Default mode={{0; 85; 0; 0}} · Module=MC42-33 (MC42[0]) · Module index=9
- Lit : `Seat Front Back`
- Utilisé par : *(personne)*
- Ligne export : 99467 · id 43503
