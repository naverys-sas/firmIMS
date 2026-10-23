# MC42 — KeyBox

75 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## KeyBox

#### 0x70C  `GFIN`
- Propriétés : Identifier=0x70C · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={} · Module=KeyBox (Generic) · Module index=0
- Utilisé par : *(personne)*
- Ligne export : 24724 · id 58578

#### Byte 0  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`
- Ligne export : 24740 · id 58579

#### Byte 1  `GPOUT`
- Propriétés : Input value=0x0C · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`
- Ligne export : 24751 · id 58580

#### GFOUT-D:Generic  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=KeyBox (Generic) · Module index=2
- Lit : `Byte 0`, `Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 24762 · id 58581

#### KeyBox Can Ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `0x70C`
- Lit : ``
- Utilisé par : `CanBus Error TB`, `Measure group: CanBus`
- Ligne export : 24784 · id 58582

#### CanBus Error TB  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=KeyBox T2 · Text=The KeyBox TB don't respond with the system, try a reboot to fix.
- Logique :
  - **Showing** = `not(KeyBox Can Ok)`
  - **Hiding** = `KeyBox Can Ok`
- Lit : ``, `KeyBox Can Ok`
- Utilisé par : *(personne)*
- Ligne export : 24827 · id 58590

#### Aft Fan Max Test  `DP`
> Allows to test full fan without crancking
- Propriétés : True text=Force On · False text=Auto · Default mode={False}
- Utilisé par : `K1 Fan Rear / Fan`, `K2 Fan Super / Pump`, `Adjust group: Master Cooling`, `Single adjust item: Aft Fan Max Test`
- Ligne export : 24881 · id 63103

#### Aft Fan Low Test  `DP`
> Allows to test low fan without crancking
- Propriétés : True text=Force On · False text=Auto · Default mode={False}
- Utilisé par : `K1 Fan Rear / Fan`, `Adjust group: Master Cooling`, `Single adjust item: Aft Fan Low Test`
- Ligne export : 24894 · id 66018

#### Activate Low Aft Fan  `FGI`
- Propriétés : Input type=Digital · Input=Activate Low Aft Fan · Default state name=Default state
- Lit : `Activate Low Aft Fan`
- Utilisé par : `Activate Low Aft Fan`, `K1 Fan Rear / Fan`, `K6 Engine Water Pump`, `K7 Exhaust Water Pump`
- Ligne export : 24907 · id 66266

#### K1 Fan Rear / Fan  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Activate Low Aft Fan) OR (Aft Fan Max Test) OR (Aft Fan Low Test)`
- Lit : ``, `Activate Low Aft Fan`, `Aft Fan Low Test`, `Aft Fan Max Test`
- Utilisé par : `ON_Bits`
- Ligne export : 24918 · id 58599

#### Activate High Aft Fan  `FGI`
- Propriétés : Input type=Digital · Input=Activate High Aft Fan · Default state name=Default state
- Lit : `Activate High Aft Fan`
- Utilisé par : `Activate High Aft Fan`, `K2 Fan Super / Pump`, `K6 Engine Water Pump`, `K7 Exhaust Water Pump`, `MD3 page: Thermic`
- Ligne export : 24975 · id 66268

#### K2 Fan Super / Pump  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Activate High Aft Fan) OR (Aft Fan Max Test)`
- Lit : ``, `Activate High Aft Fan`, `Aft Fan Max Test`
- Utilisé par : `ON_Bits`
- Ligne export : 24986 · id 58606

#### Exhaust Fan Test  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `K3 Fan Exhaust / AutoOff`, `Adjust group: Master Cooling`, `Single adjust item: Exhaust Fan Test`
- Ligne export : 25036 · id 60073

#### Activate Exhaust  `FGI`
- Propriétés : Input type=Digital · Input=Activate exhaust Fan · Default state name=Default state
- Lit : `Activate exhaust Fan`
- Utilisé par : `K3 Fan Exhaust / AutoOff`, `K6 Engine Water Pump`, `K7 Exhaust Water Pump`
- Ligne export : 25049 · id 66264

#### K3 Fan Exhaust / AutoOff  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Activate Exhaust) OR (Exhaust Fan Test)`
- Lit : ``, `Activate Exhaust`, `Exhaust Fan Test`
- Utilisé par : `ON_Bits`, `Event log: Thermic Events`
- Ligne export : 25060 · id 58613

#### K4 Engine Power / Search Lights  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Out SWITCH ON Engine`
- Lit : ``, `Out SWITCH ON Engine`
- Utilisé par : `ON_Bits`
- Ligne export : 25110 · id 58620

#### K5 Engine Start  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Out START Engine`
- Lit : ``, `Out START Engine`
- Utilisé par : `ON_Bits`
- Ligne export : 25153 · id 58627

#### Force Engine pump  `DP`
> Allows to pilot Engine pump to flush the system
- Propriétés : True text=Force On · False text=Auto · Default mode={False}
- Utilisé par : `K6 Engine Water Pump`, `Adjust group: Master Cooling`, `Single adjust item: Force Engine pump`
- Ligne export : 25196 · id 66422

#### K6 Engine Water Pump  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine_Started OR (Activate Low Aft Fan) OR (Activate High Aft Fan) OR (Activate Exhaust) OR (Force Engine pump)`
- Lit : ``, `Activate Exhaust`, `Activate High Aft Fan`, `Activate Low Aft Fan`, `Engine_Started`, `Force Engine pump`
- Utilisé par : `ON_Bits`
- Ligne export : 25209 · id 58634

#### Force Exhaust pump  `DP`
> Force Exhaust pump to flush the system
- Propriétés : True text=Force On · False text=Auto · Default mode={False}
- Utilisé par : `K7 Exhaust Water Pump`, `Adjust group: Master Cooling`, `Single adjust item: Force Exhaust pump`
- Ligne export : 25280 · id 66421

#### K7 Exhaust Water Pump  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine_Started OR (Activate Low Aft Fan) OR (Activate High Aft Fan) OR (Activate Exhaust) OR (Force Exhaust pump)`
- Lit : ``, `Activate Exhaust`, `Activate High Aft Fan`, `Activate Low Aft Fan`, `Engine_Started`, `Force Exhaust pump`
- Utilisé par : `ON_Bits`
- Ligne export : 25293 · id 58641

#### K8  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 25364 · id 58648

#### K9  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 25400 · id 58655

#### K10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 25436 · id 58662

#### K11  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 25472 · id 58669

#### K12  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 25508 · id 58676

#### K13  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 25544 · id 58684

#### ON_Bits  `IMAC`
- Logique :
  ```qcode
  Result := K1 Fan Rear / Fan * 1 + K2 Fan Super / Pump  * 2 + K3 Fan Exhaust / AutoOff * 4 + K4 Engine Power / Search Lights * 8 + K5 Engine Start * 16 + K6 Engine Water Pump * 32 + K7 Exhaust Water Pump * 64 + K8 * 128 + K9 * 256 + K10 * 512 + K11 * 1024 + K12 * 2048 + K13 * 4096
  ```
- Lit : `K1 Fan Rear / Fan`, `K10`, `K11`, `K12`, `K13`, `K2 Fan Super / Pump`, `K3 Fan Exhaust / AutoOff`, `K4 Engine Power / Search Lights`, `K5 Engine Start`, `K6 Engine Water Pump`, `K7 Exhaust Water Pump`, `K8`, `K9`
- Utilisé par : `OFF_Bits`, `ON_Bits_GOUT`
- Ligne export : 25580 · id 58692

#### ON_Bits_GOUT  `GPOUT`
- Propriétés : Input value=ON_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `ON_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 25598 · id 58726

#### OFF_Bits  `IMAC`
- Logique :
  ```qcode
  Result := bnot(ON_Bits) band 0x1FFF
  ```
- Lit : `ON_Bits`
- Utilisé par : `OFF_Bits_GOUT`
- Ligne export : 25610 · id 58727

#### OFF_Bits_GOUT  `GPOUT`
- Propriétés : Input value=OFF_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `OFF_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 25628 · id 58738

#### Program KeyBox  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Trigger HeartBeat`, `Adjust group: Master Config`, `Single adjust item: Program KeyBox`
- Ligne export : 25640 · id 58739

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=0x20C · Data length=8 · Send method=On change · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{OFF_Bits_GOUT; 0}; {ON_Bits_GOUT; 16}} · Module=KeyBox (Generic) · Module index=0
- Lit : `OFF_Bits_GOUT`, `ON_Bits_GOUT`
- Utilisé par : *(personne)*
- Ligne export : 25653 · id 58740

#### BYTE 0 - HB  `GPOUT`
- Propriétés : Input value=0x2B · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 25675 · id 58741

#### BYTE 1 - HB  `GPOUT`
- Propriétés : Input value=0x17 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 25686 · id 58742

#### BYTE 2 - HB  `GPOUT`
- Propriétés : Input value=0x10 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 25697 · id 58743

#### BYTE 4 - HB  `GPOUT`
- Propriétés : Input value=0xF4 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 25708 · id 58744

#### ID Prog  `IMAC`
- Logique :
  - **Controlling** = `0x0C + 0x600`
- Lit : ``
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 25719 · id 58745

#### BYTE 5 - HB  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`
- Ligne export : 25762 · id 58753

#### Trigger HeartBeat  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(Program KeyBox)`
- Lit : ``, `Program KeyBox`
- Utilisé par : `GFOUT-D:Generic`, `Trigger Speed`
- Ligne export : 25773 · id 58754

#### GFOUT-D:Generic  `GFOUT`
- Propriétés : Identifier=ID Prog · Data length=8 · Send method=On trigger · Trigger=Trigger HeartBeat · Unused bits=Set to 0 · Parameters={{BYTE 0 - HB; 0}; {BYTE 1 - HB; 8}; {BYTE 2 - HB; 16}; {BYTE 4 - HB; 32}; {BYTE 5 - HB; 40}} · Module=KeyBox (Generic) · Module index=3
- Lit : `BYTE 0 - HB`, `BYTE 1 - HB`, `BYTE 2 - HB`, `BYTE 4 - HB`, `BYTE 5 - HB`, `ID Prog`, `Trigger HeartBeat`
- Utilisé par : *(personne)*
- Ligne export : 25817 · id 58762

#### BYTE 0 - HB  `GPOUT`
- Propriétés : Input value=0x2F · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 25849 · id 58763

#### BYTE 1 - HB  `GPOUT`
- Propriétés : Input value=0x10 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 25860 · id 58764

#### BYTE 2 - HB  `GPOUT`
- Propriétés : Input value=0x20 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 25871 · id 58765

#### BYTE 4 - HB  `GPOUT`
- Propriétés : Input value=0x02 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 25882 · id 58766

#### Trigger Speed  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `NegativeFlank(Trigger HeartBeat)`
- Lit : ``, `Trigger HeartBeat`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 25893 · id 58767

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=ID Prog · Data length=8 · Send method=On trigger · Trigger=Trigger Speed · Unused bits=Set to 0 · Parameters={{BYTE 0 - HB; 0}; {BYTE 1 - HB; 8}; {BYTE 2 - HB; 16}; {BYTE 4 - HB; 32}} · Module=KeyBox (Generic) · Module index=4
- Lit : `BYTE 0 - HB`, `BYTE 1 - HB`, `BYTE 2 - HB`, `BYTE 4 - HB`, `ID Prog`, `Trigger Speed`
- Utilisé par : *(personne)*
- Ligne export : 25937 · id 58775

#### ID Fault  `IMAC`
- Logique :
  - **Controlling** = `0x0C + 0x180`
- Lit : ``
- Utilisé par : `GFIN-B:Generic`
- Ligne export : 25966 · id 58776

#### GFIN-B:Generic  `GFIN`
- Propriétés : Identifier=ID Fault · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{K1 Fault; 1}; {K2 Fault; 2}; {K3 Fault; 3}; {K4 Fault; 4}; {K5 Fault; 5}; {K6 Fault; 6}; {K7 Fault; 7}; {K8 Fault; 8}; {K9 Fault; 9}; {K10 Fault; 10}; {K11 Fault; 11}; {K12 Fault; 12}; {K13 Fault; 13}} · Module=KeyBox (Generic) · Module index=1
- Lit : `ID Fault`, `K1 Fault`, `K10 Fault`, `K11 Fault`, `K12 Fault`, `K13 Fault`, `K2 Fault`, `K3 Fault`, `K4 Fault`, `K5 Fault`, `K6 Fault`, `K7 Fault`, `K8 Fault`, `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 26009 · id 58784

#### K1 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K1 fuse is blown`
- Ligne export : 26064 · id 58785

#### K1 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K1 fuse is blown
- Logique :
  - **Showing** = `K1 Fault`
- Lit : ``, `K1 Fault`
- Utilisé par : *(personne)*
- Ligne export : 26076 · id 58786

#### K2 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K2 fuse is blown`
- Ligne export : 26122 · id 58794

#### K2 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K2 fuse is blown
- Logique :
  - **Showing** = `K2 Fault`
- Lit : ``, `K2 Fault`
- Utilisé par : *(personne)*
- Ligne export : 26134 · id 58795

#### K3 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K3 fuse is blown`
- Ligne export : 26180 · id 58803

#### K3 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K4 fuse is blown
- Logique :
  - **Showing** = `K3 Fault`
- Lit : ``, `K3 Fault`, `K4 fuse is blown`
- Utilisé par : *(personne)*
- Ligne export : 26192 · id 58804

#### K4 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K4 fuse is blown`
- Ligne export : 26238 · id 58812

#### K4 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm
- Logique :
  - **Showing** = `K4 Fault`
- Lit : ``, `K4 Fault`
- Utilisé par : `K3 fuse is blown`
- Ligne export : 26250 · id 58813

#### K5 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K5 fuse is blown`
- Ligne export : 26296 · id 58821

#### K5 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K5 fuse is blown
- Logique :
  - **Showing** = `K5 Fault`
- Lit : ``, `K5 Fault`
- Utilisé par : *(personne)*
- Ligne export : 26308 · id 58822

#### K6 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K6 fuse is blown`
- Ligne export : 26354 · id 58830

#### K6 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K6 fuse is blown
- Logique :
  - **Showing** = `K6 Fault`
- Lit : ``, `K6 Fault`
- Utilisé par : *(personne)*
- Ligne export : 26366 · id 58831

#### K7 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K7 fuse is blown`
- Ligne export : 26412 · id 58839

#### K7 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K7 fuse is blown
- Logique :
  - **Showing** = `K7 Fault`
- Lit : ``, `K7 Fault`
- Utilisé par : *(personne)*
- Ligne export : 26424 · id 58840

#### K8 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K8 fuse is blown`
- Ligne export : 26470 · id 58848

#### K8 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K8 fuse is blown
- Logique :
  - **Showing** = `K8 Fault`
- Lit : ``, `K8 Fault`
- Utilisé par : *(personne)*
- Ligne export : 26482 · id 58849

#### K9 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K9 fuse is blown`
- Ligne export : 26528 · id 58857

#### K9 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K9 fuse is blown
- Logique :
  - **Showing** = `K9 Fault`
- Lit : ``, `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 26540 · id 58858

#### K10 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K10 fuse is blown`
- Ligne export : 26586 · id 58866

#### K10 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K10 fuse is blown
- Logique :
  - **Showing** = `K10 Fault`
- Lit : ``, `K10 Fault`
- Utilisé par : *(personne)*
- Ligne export : 26598 · id 58867

#### K11 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K11 fuse is blown`
- Ligne export : 26644 · id 58875

#### K11 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K11 fuse is blown
- Logique :
  - **Showing** = `K11 Fault`
- Lit : ``, `K11 Fault`
- Utilisé par : *(personne)*
- Ligne export : 26656 · id 58876

#### K12 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K12 fuse is blown`
- Ligne export : 26702 · id 58884

#### K12 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K12 fuse is blown
- Logique :
  - **Showing** = `K12 Fault`
- Lit : ``, `K12 Fault`
- Utilisé par : `K13 fuse is blown`
- Ligne export : 26714 · id 58885

#### K13 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K13 fuse is blown`
- Ligne export : 26760 · id 58928

#### K13 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K12 fuse is blown
- Logique :
  - **Showing** = `K13 Fault`
- Lit : ``, `K12 fuse is blown`, `K13 Fault`
- Utilisé par : *(personne)*
- Ligne export : 26772 · id 58929
