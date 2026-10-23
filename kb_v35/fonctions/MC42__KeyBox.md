# MC42 — KeyBox

70 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## KeyBox

#### 0x70C  `GFIN`
- Propriétés : Identifier=0x70C · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={} · Module=KeyBox (Generic) · Module index=0
- Utilisé par : *(personne)*
- Ligne export : 48180 · id 58578

#### Byte 0  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`
- Ligne export : 48196 · id 58579

#### Byte 1  `GPOUT`
- Propriétés : Input value=0x0C · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`
- Ligne export : 48207 · id 58580

#### GFOUT-D:Generic  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=KeyBox (Generic) · Module index=2
- Lit : `Byte 0`, `Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 48218 · id 58581

#### KeyBox Can Ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `0x70C`
- Lit : ``
- Utilisé par : `CanBus Error TB`, `Measure group: CanBus`
- Ligne export : 48240 · id 58582

#### CanBus Error TB  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=KeyBox T2 · Text=The KeyBox TB don't respond with the system, try a reboot to fix.
- Logique :
  - **Showing** = `not(KeyBox Can Ok)`
  - **Hiding** = `KeyBox Can Ok`
- Lit : ``, `KeyBox Can Ok`
- Utilisé par : *(personne)*
- Ligne export : 48283 · id 58590

#### K1 Fan Rear / Fan  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Out FAN Engine) OR (FAN OUT) OR (Full Fan Test)`
- Lit : ``, `FAN OUT`, `Full Fan Test`, `Out FAN Engine`
- Utilisé par : `ON_Bits`
- Ligne export : 48337 · id 58599

#### K2 Fan Super / Pump  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(OUT Full FAN) OR (PUMP VAR) OR (Full Fan Test)`
- Lit : ``, `Full Fan Test`, `OUT Full FAN`, `PUMP VAR`
- Utilisé par : `ON_Bits`
- Ligne export : 48394 · id 58606

#### Force K3  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `K3 Fan Exhaust / AutoOff`, `Adjust group: Master Electric`, `Single adjust item: Force K3`
- Ligne export : 48451 · id 60073

#### K3 Fan Exhaust / AutoOff  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Out FAN Engine) OR (ShuntDown Action) OR (Force K3)`
- Lit : ``, `Force K3`, `Out FAN Engine`, `ShuntDown Action`
- Utilisé par : `ON_Bits`, `Event log: Thermic Events`
- Ligne export : 48464 · id 58613

#### Charger Connected  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=2000
- Logique :
  - **Activating** = `PositiveFlank(Charger CONNECT to 220V)`
- Lit : ``, `Charger CONNECT to 220V`
- Utilisé par : `K4 Engine Power / Search Lights`
- Ligne export : 48521 · id 60248

#### K4 Engine Power / Search Lights  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Out SWITCH ON Engine) OR (Charger Connected)`
- Lit : ``, `Charger Connected`, `Out SWITCH ON Engine`
- Utilisé par : `ON_Bits`
- Ligne export : 48565 · id 58620

#### K5 Engine Start  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Out START Engine`
- Lit : ``, `Out START Engine`
- Utilisé par : `ON_Bits`
- Ligne export : 48615 · id 58627

#### K6 Aux 1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 48658 · id 58634

#### K7 Aux 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 48694 · id 58641

#### K8  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 48730 · id 58648

#### K9  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 48766 · id 58655

#### K10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 48802 · id 58662

#### K11  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 48838 · id 58669

#### K12  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 48874 · id 58676

#### K13  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Lit : ``
- Utilisé par : `ON_Bits`
- Ligne export : 48910 · id 58684

#### ON_Bits  `IMAC`
- Logique :
  ```qcode
  Result := K1 Fan Rear / Fan * 1 + K2 Fan Super / Pump  * 2 + K3 Fan Exhaust / AutoOff * 4 + K4 Engine Power / Search Lights * 8 + K5 Engine Start * 16 + K6 Aux 1 * 32 + K7 Aux 2 * 64 + K8 * 128 + K9 * 256 + K10 * 512 + K11 * 1024 + K12 * 2048 + K13 * 4096
  ```
- Lit : `K1 Fan Rear / Fan`, `K10`, `K11`, `K12`, `K13`, `K2 Fan Super / Pump`, `K3 Fan Exhaust / AutoOff`, `K4 Engine Power / Search Lights`, `K5 Engine Start`, `K6 Aux 1`, `K7 Aux 2`, `K8`, `K9`
- Utilisé par : `OFF_Bits`, `ON_Bits_GOUT`
- Ligne export : 48946 · id 58692

#### ON_Bits_GOUT  `GPOUT`
- Propriétés : Input value=ON_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `ON_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 48964 · id 58726

#### OFF_Bits  `IMAC`
- Logique :
  ```qcode
  Result := bnot(ON_Bits) band 0x1FFF
  ```
- Lit : `ON_Bits`
- Utilisé par : `OFF_Bits_GOUT`
- Ligne export : 48976 · id 58727

#### OFF_Bits_GOUT  `GPOUT`
- Propriétés : Input value=OFF_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `OFF_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 48994 · id 58738

#### Program KeyBox  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Trigger HeartBeat`, `Adjust group: Master Config`, `Single adjust item: Program KeyBox`
- Ligne export : 49006 · id 58739

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=0x20C · Data length=8 · Send method=On change · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{OFF_Bits_GOUT; 0}; {ON_Bits_GOUT; 16}} · Module=KeyBox (Generic) · Module index=0
- Lit : `OFF_Bits_GOUT`, `ON_Bits_GOUT`
- Utilisé par : *(personne)*
- Ligne export : 49019 · id 58740

#### BYTE 0 - HB  `GPOUT`
- Propriétés : Input value=0x2B · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 49041 · id 58741

#### BYTE 1 - HB  `GPOUT`
- Propriétés : Input value=0x17 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 49052 · id 58742

#### BYTE 2 - HB  `GPOUT`
- Propriétés : Input value=0x10 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 49063 · id 58743

#### BYTE 4 - HB  `GPOUT`
- Propriétés : Input value=0xF4 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 49074 · id 58744

#### ID Prog  `IMAC`
- Logique :
  - **Controlling** = `0x0C + 0x600`
- Lit : ``
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 49085 · id 58745

#### BYTE 5 - HB  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`
- Ligne export : 49128 · id 58753

#### Trigger HeartBeat  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(Program KeyBox)`
- Lit : ``, `Program KeyBox`
- Utilisé par : `GFOUT-D:Generic`, `Trigger Speed`
- Ligne export : 49139 · id 58754

#### GFOUT-D:Generic  `GFOUT`
- Propriétés : Identifier=ID Prog · Data length=8 · Send method=On trigger · Trigger=Trigger HeartBeat · Unused bits=Set to 0 · Parameters={{BYTE 0 - HB; 0}; {BYTE 1 - HB; 8}; {BYTE 2 - HB; 16}; {BYTE 4 - HB; 32}; {BYTE 5 - HB; 40}} · Module=KeyBox (Generic) · Module index=3
- Lit : `BYTE 0 - HB`, `BYTE 1 - HB`, `BYTE 2 - HB`, `BYTE 4 - HB`, `BYTE 5 - HB`, `ID Prog`, `Trigger HeartBeat`
- Utilisé par : *(personne)*
- Ligne export : 49183 · id 58762

#### BYTE 0 - HB  `GPOUT`
- Propriétés : Input value=0x2F · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 49215 · id 58763

#### BYTE 1 - HB  `GPOUT`
- Propriétés : Input value=0x10 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 49226 · id 58764

#### BYTE 2 - HB  `GPOUT`
- Propriétés : Input value=0x20 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 49237 · id 58765

#### BYTE 4 - HB  `GPOUT`
- Propriétés : Input value=0x02 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`
- Ligne export : 49248 · id 58766

#### Trigger Speed  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `NegativeFlank(Trigger HeartBeat)`
- Lit : ``, `Trigger HeartBeat`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 49259 · id 58767

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=ID Prog · Data length=8 · Send method=On trigger · Trigger=Trigger Speed · Unused bits=Set to 0 · Parameters={{BYTE 0 - HB; 0}; {BYTE 1 - HB; 8}; {BYTE 2 - HB; 16}; {BYTE 4 - HB; 32}} · Module=KeyBox (Generic) · Module index=4
- Lit : `BYTE 0 - HB`, `BYTE 1 - HB`, `BYTE 2 - HB`, `BYTE 4 - HB`, `ID Prog`, `Trigger Speed`
- Utilisé par : *(personne)*
- Ligne export : 49303 · id 58775

#### ID Fault  `IMAC`
- Logique :
  - **Controlling** = `0x0C + 0x180`
- Lit : ``
- Utilisé par : `GFIN-B:Generic`
- Ligne export : 49332 · id 58776

#### GFIN-B:Generic  `GFIN`
- Propriétés : Identifier=ID Fault · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{K1 Fault; 1}; {K2 Fault; 2}; {K3 Fault; 3}; {K4 Fault; 4}; {K5 Fault; 5}; {K6 Fault; 6}; {K7 Fault; 7}; {K8 Fault; 8}; {K9 Fault; 9}; {K10 Fault; 10}; {K11 Fault; 11}; {K12 Fault; 12}; {K13 Fault; 13}} · Module=KeyBox (Generic) · Module index=1
- Lit : `ID Fault`, `K1 Fault`, `K10 Fault`, `K11 Fault`, `K12 Fault`, `K13 Fault`, `K2 Fault`, `K3 Fault`, `K4 Fault`, `K5 Fault`, `K6 Fault`, `K7 Fault`, `K8 Fault`, `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 49375 · id 58784

#### K1 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K1 fuse is blown`
- Ligne export : 49430 · id 58785

#### K1 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K1 fuse is blown
- Logique :
  - **Showing** = `K1 Fault`
- Lit : ``, `K1 Fault`
- Utilisé par : *(personne)*
- Ligne export : 49442 · id 58786

#### K2 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K2 fuse is blown`
- Ligne export : 49488 · id 58794

#### K2 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K2 fuse is blown
- Logique :
  - **Showing** = `K2 Fault`
- Lit : ``, `K2 Fault`
- Utilisé par : *(personne)*
- Ligne export : 49500 · id 58795

#### K3 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K3 fuse is blown`
- Ligne export : 49546 · id 58803

#### K3 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K4 fuse is blown
- Logique :
  - **Showing** = `K3 Fault`
- Lit : ``, `K3 Fault`, `K4 fuse is blown`
- Utilisé par : *(personne)*
- Ligne export : 49558 · id 58804

#### K4 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K4 fuse is blown`
- Ligne export : 49604 · id 58812

#### K4 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm
- Logique :
  - **Showing** = `K4 Fault`
- Lit : ``, `K4 Fault`
- Utilisé par : `K3 fuse is blown`
- Ligne export : 49616 · id 58813

#### K5 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K5 fuse is blown`
- Ligne export : 49662 · id 58821

#### K5 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K5 fuse is blown
- Logique :
  - **Showing** = `K5 Fault`
- Lit : ``, `K5 Fault`
- Utilisé par : *(personne)*
- Ligne export : 49674 · id 58822

#### K6 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K6 fuse is blown`
- Ligne export : 49720 · id 58830

#### K6 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K6 fuse is blown
- Logique :
  - **Showing** = `K6 Fault`
- Lit : ``, `K6 Fault`
- Utilisé par : *(personne)*
- Ligne export : 49732 · id 58831

#### K7 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K7 fuse is blown`
- Ligne export : 49778 · id 58839

#### K7 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K7 fuse is blown
- Logique :
  - **Showing** = `K7 Fault`
- Lit : ``, `K7 Fault`
- Utilisé par : *(personne)*
- Ligne export : 49790 · id 58840

#### K8 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K8 fuse is blown`
- Ligne export : 49836 · id 58848

#### K8 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K8 fuse is blown
- Logique :
  - **Showing** = `K8 Fault`
- Lit : ``, `K8 Fault`
- Utilisé par : *(personne)*
- Ligne export : 49848 · id 58849

#### K9 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K9 fuse is blown`
- Ligne export : 49894 · id 58857

#### K9 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K9 fuse is blown
- Logique :
  - **Showing** = `K9 Fault`
- Lit : ``, `K9 Fault`
- Utilisé par : *(personne)*
- Ligne export : 49906 · id 58858

#### K10 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K10 fuse is blown`
- Ligne export : 49952 · id 58866

#### K10 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K10 fuse is blown
- Logique :
  - **Showing** = `K10 Fault`
- Lit : ``, `K10 Fault`
- Utilisé par : *(personne)*
- Ligne export : 49964 · id 58867

#### K11 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K11 fuse is blown`
- Ligne export : 50010 · id 58875

#### K11 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K11 fuse is blown
- Logique :
  - **Showing** = `K11 Fault`
- Lit : ``, `K11 Fault`
- Utilisé par : *(personne)*
- Ligne export : 50022 · id 58876

#### K12 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K12 fuse is blown`
- Ligne export : 50068 · id 58884

#### K12 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K12 fuse is blown
- Logique :
  - **Showing** = `K12 Fault`
- Lit : ``, `K12 Fault`
- Utilisé par : `K13 fuse is blown`
- Ligne export : 50080 · id 58885

#### K13 Fault  `GPIN`
- Propriétés : Length=1 bit · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-B:Generic`, `K13 fuse is blown`
- Ligne export : 50126 · id 58928

#### K13 fuse is blown  `CMSG`
- Propriétés : Show message=All · Dialog type=Alarm · Header=K12 fuse is blown
- Logique :
  - **Showing** = `K13 Fault`
- Lit : ``, `K12 fuse is blown`, `K13 Fault`
- Utilisé par : *(personne)*
- Ligne export : 50138 · id 58929

#### Full Fan Test  `DP`
> Allows to test full fan without crancking
- Propriétés : True text=Force On · False text=Auto · Default mode={False}
- Utilisé par : `K1 Fan Rear / Fan`, `K2 Fan Super / Pump`, `Adjust group: Master Thermic`, `Single adjust item: Full Fan Test`
- Ligne export : 50184 · id 63103
