# MD4-CAB app — c5.NMEA

106 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## c5.NMEA / GPS

#### md4 GPS Speed factor  `SP`
- Propriétés : Input channel=None · Default state name=m/s · States={kts}
- Utilisé par : `GPS Factor`
- Ligne export : 106786 · id 220448

#### GPS Factor  `IP`
- Propriétés : Mode selector=md4 GPS Speed factor · Default mode: m/s={5144} · Mode 1: kts={10000}
- Lit : `md4 GPS Speed factor`
- Utilisé par : `Speed Over Ground Kts`
- Ligne export : 106798 · id 220450

#### Adress_Search  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Adress_Search OR (PositiveFlank(Adress Loose))`
  - **Blocking** = `PositiveFlank(Garmin - NMEA)`
- Lit : `Adress Loose`, `Adress_Search`, `Garmin - NMEA`
- Utilisé par : `Adress_Search`, `GPS Adresse Find`, `md4 Adresse_Mem`
- Ligne export : 106812 · id 220451

#### GPS_Adresse_Find_Int  `IMAC`
- Logique :
  - **Controlling** = `GPS Adresse Find [s]`
- Lit : `GPS Adresse Find`
- Utilisé par : `md4 Adresse_Mem`
- Ligne export : 106871 · id 220461

#### md4 Adresse_Mem  `MEM`
- Propriétés : Input channel=GPS_Adresse_Find_Int · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `Adress_Search AND DerivativeOf(GPS_Adresse_Find_Int)`
- Lit : `Adress_Search`, `GPS_Adresse_Find_Int`
- Utilisé par : `GPS_Adress`
- Ligne export : 106912 · id 220469

#### GPS_Adress  `IMAC`
- Logique :
  ```qcode
  result := md4 Adresse_Mem
  ```
- Lit : `md4 Adresse_Mem`
- Utilisé par : `PGN-129026`
- Ligne export : 106964 · id 220478

#### PGN-129026  `IMAC`
- Logique :
  ```qcode
  pgn := 129026
  priority := 2
  source := GPS_Adress
  
  Result := priority * 0x4000000 + pgn * 0x100 + source
  ```
- Lit : `GPS_Adress`
- Utilisé par : `129026-0`
- Ligne export : 106982 · id 220486

#### 129026-0  `GFIN`
- Propriétés : Identifier=PGN-129026 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Speed Over Ground Raw; 32}} · Module=Garmin CAB (Generic) · Module index=0
- Lit : `PGN-129026`, `Speed Over Ground Raw`
- Utilisé par : `Garmin - NMEA`
- Ligne export : 107004 · id 220503

#### Garmin - NMEA  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `129026-0`
- Lit : `129026-0`
- Utilisé par : `Adress Loose`, `Adress_Search`, `MD4-10 page: INFO`
- Ligne export : 107023 · id 220504

#### Adress Loose  `IDC`
- Propriétés : Toggle=No · Delay on=120000 · Delay off=0
- Logique :
  - **Activating** = `Be2 KTB K1 IDC - GPS_EQT and (not(Garmin - NMEA))`
- Lit : `Be2 KTB K1 IDC - GPS_EQT`, `Garmin - NMEA`
- Utilisé par : `Adress_Search`
- Ligne export : 107066 · id 220512

#### GPS Adresse Find  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Adress_Search`
  - **Resetting** = `GPS Adresse Find [s] > 256`
- Lit : `Adress_Search`
- Utilisé par : `GPS_Adresse_Find_Int`
- Ligne export : 107119 · id 220521

#### Speed Over Ground Raw  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `129026-0`, `Speed Over Ground Kts`
- Ligne export : 107180 · id 220532

#### Speed Over Ground Kts  `MAC`
- Propriétés : Unit=Kts
- Logique :
  ```qcode
  if Speed Over Ground Raw < 65500 then
    Result:= (Speed Over Ground Raw  /100) / (GPS Factor / 10000)
  else
    Result:= 0
  endif
  ```
- Lit : `GPS Factor`, `Speed Over Ground Raw`
- Utilisé par : `Fuel Economy`, `MD4-10 page: OUTBOARD`
- Ligne export : 107193 · id 220533

## c5.NMEA / OutBoards nmea

#### md4 Engine Brand  `SP`
- Propriétés : Input channel=None · Default state name=Mercury · States={Yamaha; COX}
- Utilisé par : `Adress Loose`, `Alternator - 1`, `Cox - Show`, `Engine 2 - Tank`, `Engine Hour - 1`, `Engine Oil Pressure - 1`, `Engine temp - 1`, `Fuel rate - 1`, `Mercury - Show`, `OutBoard_Adresse`, `Outboard_Priority`, `Trim Value`, `Yamaha - Show`, `Adjust group: Setup Outboard`, `Single adjust item: md4 Engine Brand`
- Ligne export : 107231 · id 220550

#### 127488-Eng 1  `GFIN`
- Propriétés : Identifier=PGN-127488 · Data length=Dont care · Timeout=1000 · Paged protocol={0xFF; 0} · Parameters={{Engine 1 - Speed - Raw; 8}; {Engine 1 - Trim; 40}} · Module=Outboards (Generic) · Module index=1
- Lit : `Engine 1 - Speed - Raw`, `Engine 1 - Trim`, `PGN-127488`
- Utilisé par : `Engine ON - 1 - NMEA`
- Ligne export : 107244 · id 220553

#### Engine ON - 1 - NMEA  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `127488-Eng 1`
- Lit : `127488-Eng 1`
- Utilisé par : `Engine_Nmea`, `MD4-10 page: MAIN`, `MD4-10 page: OUTBOARD`
- Ligne export : 107267 · id 220554

#### 127488-Eng 2  `GFIN`
- Propriétés : Identifier=PGN-127488 · Data length=Dont care · Timeout=1000 · Paged protocol={0xFF; 1} · Parameters={{Engine 2 - Speed - Raw; 8}; {Engine 2 - Trim; 40}} · Module=Outboards (Generic) · Module index=2
- Lit : `Engine 2 - Speed - Raw`, `Engine 2 - Trim`, `PGN-127488`
- Utilisé par : `Engine ON - 2 - NMEA`
- Ligne export : 107310 · id 220562

#### Engine ON - 2 - NMEA  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `127488-Eng 2`
- Lit : `127488-Eng 2`
- Utilisé par : `Engine_Nmea`, `MD4-10 page: MAIN`, `MD4-10 page: OUTBOARD`
- Ligne export : 107333 · id 220563

#### Engine_Nmea  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Engine ON - 1 - NMEA) OR (Engine ON - 2 - NMEA)`
- Lit : `Engine ON - 1 - NMEA`, `Engine ON - 2 - NMEA`
- Utilisé par : `Adress Loose Auto`, `Adress_Search`, `Alternator - 1`, `Engine Hour - 1`, `Engine Oil Pressure - 1`, `Engine temp - 1`, `Fuel rate - 1`
- Ligne export : 107376 · id 220571

#### Adress Loose Auto  `IDC`
- Propriétés : Toggle=No · Delay on=120000 · Delay off=0
- Logique :
  - **Activating** = `not(Engine_Nmea) AND (Be3 KTC K9 IDC - OutBoard On-OFF)`
- Lit : `Be3 KTC K9 IDC - OutBoard On-OFF`, `Engine_Nmea`
- Utilisé par : `Adress Loose`
- Ligne export : 107426 · id 220580

#### Adress Loose  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=md4 Engine Brand
- Fonction *Mercury* :
  - **Activating** = `Adress Loose Auto`
- Fonction *Yamaha* :
  - **Activating** = `Adress Loose Auto`
- Fonction *COX* : (vide)
- Lit : `Adress Loose Auto`, `md4 Engine Brand`
- Utilisé par : `Adress_Search`
- Ligne export : 107477 · id 220589

#### Adress_Search  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Adress_Search OR (PositiveFlank(Adress Loose))`
  - **Blocking** = `PositiveFlank(Engine_Nmea)`
- Lit : `Adress Loose`, `Adress_Search`, `Engine_Nmea`
- Utilisé par : `Adress_Search`, `Outboard Adresse Find`, `md4 Adresse_Mem`
- Ligne export : 107575 · id 220610

#### Outboard Adresse Find  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Adress_Search`
  - **Resetting** = `Outboard Adresse Find [s] > 256`
- Lit : `Adress_Search`
- Utilisé par : `Outboard_Adress_Find_Int`
- Ligne export : 107634 · id 220620

#### Outboard_Adress_Find_Int  `IMAC`
- Logique :
  - **Controlling** = `Outboard Adresse Find [s]`
- Lit : `Outboard Adresse Find`
- Utilisé par : `md4 Adresse_Mem`
- Ligne export : 107695 · id 220631

#### md4 Adresse_Mem  `MEM`
- Propriétés : Input channel=Outboard_Adress_Find_Int · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `Adress_Search AND DerivativeOf(Outboard_Adress_Find_Int)`
- Lit : `Adress_Search`, `Outboard_Adress_Find_Int`
- Utilisé par : `OutBoard_Adresse`
- Ligne export : 107736 · id 220639

#### OutBoard_Adresse  `IMAC`
- Propriétés : Function selector=md4 Engine Brand
- Fonction *Mercury* :
  ```qcode
  result := md4 Adresse_Mem
  ```
- Fonction *Yamaha* :
  ```qcode
  result := md4 Adresse_Mem
  ```
- Fonction *COX* :
  ```qcode
  result:=0
  ```
- Lit : `md4 Adresse_Mem`, `md4 Engine Brand`
- Utilisé par : `PGN-127488`, `PGN-127489`, `PNG-127505`
- Ligne export : 107788 · id 220648

#### Outboard_Priority  `IMAC`
- Propriétés : Function selector=md4 Engine Brand
- Fonction *Mercury* :
  ```qcode
  result := 2
  ```
- Fonction *Yamaha* :
  ```qcode
  result := 2
  ```
- Fonction *COX* :
  ```qcode
  result := 6
  ```
- Lit : `md4 Engine Brand`
- Utilisé par : `PGN-127488`, `PGN-127489`
- Ligne export : 107822 · id 220670

#### PGN-127488  `IMAC`
- Logique :
  ```qcode
  pgn := 127488
  priority := Outboard_Priority
  source := OutBoard_Adresse
  
  Result := priority * 0x4000000 + pgn * 0x100 + source
  ```
- Lit : `OutBoard_Adresse`, `Outboard_Priority`
- Utilisé par : `127488-Eng 1`, `127488-Eng 2`
- Ligne export : 107856 · id 220692

#### Engine 1 - Speed - Raw  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127488-Eng 1`, `Engine 1 - Speed - filter`
- Ligne export : 107878 · id 220709

#### Engine 1 - Speed - filter  `SFC`
- Propriétés : Input channel=Engine 1 - Speed - Raw · Enable=Yes · Type=Filter · Filter=98
- Lit : `Engine 1 - Speed - Raw`
- Utilisé par : `Engine 1 - Speed`
- Ligne export : 107891 · id 220710

#### Engine 1 - Speed  `MAC`
- Propriétés : Unit=Rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `(Round((Engine 1 - Speed - filter / 400))) * 100`
- Lit : `Engine 1 - Speed - filter`
- Utilisé par : `Engine 1 - RUN`, `Engine 1 - Speed - Gauge`, `Engine RUN FAST - NMEA`
- Ligne export : 107903 · id 220711

#### Engine 2 - Speed - Raw  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127488-Eng 2`, `Engine 2 - Speed - filter`
- Ligne export : 107964 · id 220721

#### Engine 2 - Speed - filter  `SFC`
- Propriétés : Input channel=Engine 2 - Speed - Raw · Enable=Yes · Type=Filter · Filter=98
- Lit : `Engine 2 - Speed - Raw`
- Utilisé par : `Engine 2 - Speed`
- Ligne export : 107977 · id 220722

#### Engine 2 - Speed  `MAC`
- Propriétés : Unit=Rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `(Round((Engine 2 - Speed - filter / 400))) * 100`
- Lit : `Engine 2 - Speed - filter`
- Utilisé par : `Engine 2 - RUN`, `Engine 2 - Speed - Gauge`, `Engine RUN FAST - NMEA`
- Ligne export : 107989 · id 220723

#### PNG-127505  `IMAC`
- Logique :
  ```qcode
  pgn := 127505
  priority := 6
  source := OutBoard_Adresse
  
  Result := priority * 0x4000000 + pgn * 0x100 + source
  ```
- Lit : `OutBoard_Adresse`
- Utilisé par : `127505-Eng 1 - Can`, `127505-Eng 2 Page 1- Can`, `127505-Eng 2 Page 2- Can`
- Ligne export : 108050 · id 220733

#### 127505-Eng 1 - Can  `GFIN`
- Propriétés : Identifier=PNG-127505 · Data length=Dont care · Timeout=3000 · Paged protocol={0x0F; 0} · Parameters={{Engine 1 - Tank - RAW; 8}} · Module=Outboards (Generic) · Module index=3
- Lit : `Engine 1 - Tank - RAW`, `PNG-127505`
- Utilisé par : `md4 Engine 1 - Tank - MEM`
- Ligne export : 108072 · id 220750

#### Engine 1 - Tank - RAW  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127505-Eng 1 - Can`, `Engine 1 - Tank`
- Ligne export : 108092 · id 220751

#### Engine 1 - Tank  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin((Engine 1 - Tank - RAW / 250): 0->0, 95->100, Freeze)`
- Lit : `Engine 1 - Tank - RAW`
- Utilisé par : `Engine 1 - Tank`, `md4 Engine 1 - Tank - MEM`, `MD4-10 page: OUTBOARD`
- Ligne export : 108105 · id 220752

#### 127505-Eng 2 Page 1- Can  `GFIN`
> Tank 2 Reading for Yamaha Engines
- Propriétés : Identifier=PNG-127505 · Data length=Dont care · Timeout=3000 · Paged protocol={0x0F; 1} · Parameters={{Engine 2 Page 1 - Tank - Raw; 8}} · Module=Outboards (Generic) · Module index=4
- Lit : `Engine 2 Page 1 - Tank - Raw`, `PNG-127505`
- Utilisé par : `md4 Engine 2 - Tank - MEM`
- Ligne export : 108161 · id 220761

#### Engine 2 Page 1 - Tank - Raw  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127505-Eng 2 Page 1- Can`, `Engine 2 - Tank`
- Ligne export : 108181 · id 220762

#### 127505-Eng 2 Page 2- Can  `GFIN`
> Tank 2 Reading for Mercury engines
- Propriétés : Identifier=PNG-127505 · Data length=Dont care · Timeout=3000 · Paged protocol={0x0F; 2} · Parameters={{Engine 2 Page 2 - Tank - Raw; 8}} · Module=Outboards (Generic) · Module index=5
- Lit : `Engine 2 Page 2 - Tank - Raw`, `PNG-127505`
- Utilisé par : *(personne)*
- Ligne export : 108194 · id 220763

#### Engine 2 Page 2 - Tank - Raw  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127505-Eng 2 Page 2- Can`, `Engine 2 - Tank`
- Ligne export : 108214 · id 220764

#### Engine 2 - Tank  `MAC`
> Tank Value, depending on Engine brand (PGN page is different)
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=md4 Engine Brand
- Fonction *Mercury* :
  - **Controlling** = `lin((Engine 2 Page 2 - Tank - Raw / 250): 0->0, 95->100, Freeze)`
- Fonction *Yamaha* :
  - **Controlling** = `lin((Engine 2 Page 1 - Tank - Raw / 250): 0->0, 95->100, Freeze)`
- Fonction *COX* :
  - **Controlling** = `0`
- Lit : `Engine 2 Page 1 - Tank - Raw`, `Engine 2 Page 2 - Tank - Raw`, `md4 Engine Brand`
- Utilisé par : `Engine 2 - Tank`, `md4 Engine 2 - Tank - MEM`, `MD4-10 page: OUTBOARD`
- Ligne export : 108227 · id 220765

#### md4 Engine 1 - Tank - MEM  `MEM`
- Propriétés : Input channel=Engine 1 - Tank [%] · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `127505-Eng 1 - Can`
- Lit : `127505-Eng 1 - Can`, `Engine 1 - Tank`
- Utilisé par : `Fuel LOW`, `MD4-10 page: SHUTDOWN`
- Ligne export : 108359 · id 220789

#### md4 Engine 2 - Tank - MEM  `MEM`
- Propriétés : Input channel=Engine 2 - Tank [%] · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `127505-Eng 2 Page 1- Can`
- Lit : `127505-Eng 2 Page 1- Can`, `Engine 2 - Tank`
- Utilisé par : `Fuel LOW`, `MD4-10 page: SHUTDOWN`
- Ligne export : 108403 · id 220797

#### Engine 1 - Speed - Gauge  `MAC`
- Propriétés : Unit=100 Rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Engine 1 - Speed [Rpm] / 100`
- Lit : `Engine 1 - Speed`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 108447 · id 220805

#### Engine 2 - Speed - Gauge  `MAC`
- Propriétés : Unit=100 Rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Engine 2 - Speed [Rpm] / 100`
- Lit : `Engine 2 - Speed`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 108491 · id 220813

#### Trim Value  `IP`
- Propriétés : Mode selector=md4 Engine Brand · Default mode: Mercury={100} · Mode 1: Yamaha={250} · Mode 2: COX={100}
- Lit : `md4 Engine Brand`
- Utilisé par : `Engine 1 - Trim - Gauge`, `Engine 2 - Trim - Gauge`
- Ligne export : 108535 · id 220821

#### Engine 1 - Trim  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `127488-Eng 1`, `Engine 1 - Trim - Gauge`, `MD4-10 page: MAIN`
- Ligne export : 108551 · id 220822

#### Engine 1 - Trim - Gauge  `MAC`
- Propriétés : Unit=Raw · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Engine 1 - Trim: 0->0, Trim Value->100, Freeze)`
- Lit : `Engine 1 - Trim`, `Trim Value`
- Utilisé par : `Engine 1 - Down`, `MD4-10 page: OUTBOARD`
- Ligne export : 108563 · id 220823

#### Engine 2 - Trim  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `127488-Eng 2`, `Engine 2 - Trim - Gauge`, `MD4-10 page: MAIN`
- Ligne export : 108610 · id 220831

#### Engine 2 - Trim - Gauge  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Engine 2 - Trim: 0->0, Trim Value->100, Freeze)`
- Lit : `Engine 2 - Trim`, `Trim Value`
- Utilisé par : `Engine 2 - Down`, `MD4-10 page: OUTBOARD`
- Ligne export : 108622 · id 220832

#### Engine 1 - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True`
- Utilisé par : `Engine 1 - Down`, `Engine 1 - Not Down`
- Ligne export : 108669 · id 220840

#### Engine 1 - Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine 1 - Trim - Gauge [Raw] < 1`
  - **Blocking** = `not(Engine 1 - Show)`
- Lit : `Engine 1 - Show`, `Engine 1 - Trim - Gauge`
- Utilisé par : `Engine 1 - Not Down`, `MD4-10 page: OUTBOARD`
- Ligne export : 108712 · id 220848

#### Engine 1 - Not Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Engine 1 - Down)`
  - **Blocking** = `not(Engine 1 - Show)`
- Lit : `Engine 1 - Down`, `Engine 1 - Show`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 108765 · id 220857

#### md4 Number of Engines  `SP`
- Propriétés : Input channel=None · Default state name=1 Engines · States={2 Engines}
- Utilisé par : `Engine 2 - Show`, `Adjust group: Setup Outboard`, `Single adjust item: md4 Number of Engines`
- Ligne export : 108817 · id 220866

#### Engine 2 - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `md4 Number of Engines = 1`
- Lit : `md4 Number of Engines`
- Utilisé par : `Engine 2 - Down`, `Engine 2 - Not Down`, `MD4-10 page: OUTBOARD`
- Ligne export : 108829 · id 220868

#### Engine 2 - Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine 2 - Trim - Gauge < 1`
  - **Blocking** = `not(Engine 2 - Show)`
- Lit : `Engine 2 - Show`, `Engine 2 - Trim - Gauge`
- Utilisé par : `Engine 2 - Not Down`, `MD4-10 page: OUTBOARD`
- Ligne export : 108874 · id 220876

#### Engine 2 - Not Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Engine 2 - Down)`
  - **Blocking** = `not(Engine 2 - Show)`
- Lit : `Engine 2 - Down`, `Engine 2 - Show`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 108927 · id 220885

#### Engine 2 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine 2 - Speed [Rpm] > 100`
- Lit : `Engine 2 - Speed`
- Utilisé par : `Engine RUN - NMEA`, `MD4-10 page: MAIN`
- Ligne export : 108979 · id 220894

#### Engine 1 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine 1 - Speed [Rpm] > 100`
- Lit : `Engine 1 - Speed`
- Utilisé par : `Engine RUN - NMEA`, `MD4-10 page: MAIN`
- Ligne export : 109024 · id 220902

#### Engine RUN - NMEA  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(Engine 1 - RUN) OR (Engine 2 - RUN)`
- Lit : `Engine 1 - RUN`, `Engine 2 - RUN`
- Utilisé par : *(personne)*
- Ligne export : 109069 · id 220910

#### md4 Fuel Capacity (One Tank)  `IP`
- Propriétés : Unit=L · Default mode={190}
- Utilisé par : `Engine 1 - Tank`, `Engine 2 - Tank`, `Adjust group: Setup Outboard`, `Single adjust item: md4 Fuel Capacity (One Tank)`
- Ligne export : 109119 · id 220919

#### Engine 1 - Tank  `MAC`
- Propriétés : Unit=L · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Engine 1 - Tank [%]: 0->0, 100->md4 Fuel Capacity (One Tank) [L], Freeze)`
- Lit : `Engine 1 - Tank`, `md4 Fuel Capacity (One Tank)`
- Utilisé par : `md4 Engine 1 - Tank - MEM`, `MD4-10 page: OUTBOARD`
- Ligne export : 109131 · id 220920

#### Engine 2 - Tank  `MAC`
- Propriétés : Unit=L · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Engine 2 - Tank [%]: 0->0, 100->md4 Fuel Capacity (One Tank) [L], Freeze)`
- Lit : `Engine 2 - Tank`, `md4 Fuel Capacity (One Tank)`
- Utilisé par : `md4 Engine 2 - Tank - MEM`, `MD4-10 page: OUTBOARD`
- Ligne export : 109178 · id 220928

#### Engine RUN FAST - NMEA  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(Engine 1 - Speed [Rpm] > 2000) OR (Engine 2 - Speed [Rpm] > 2000)`
- Lit : `Engine 1 - Speed`, `Engine 2 - Speed`
- Utilisé par : `Gauge Page IDC`
- Ligne export : 109225 · id 220936

#### PGN-127489  `IMAC`
- Logique :
  ```qcode
  pgn := 127489
  priority := Outboard_Priority
  source := OutBoard_Adresse
  
  Result := priority * 0x4000000 + pgn * 0x100 + source
  ```
- Lit : `OutBoard_Adresse`, `Outboard_Priority`
- Utilisé par : `127489-0`, `127489-1`, `127489-2`
- Ligne export : 109279 · id 220945

#### 127489-0  `GFIN`
- Propriétés : Identifier=PGN-127489 · Data length=Dont care · Timeout=1000 · Paged protocol={0x0F; 0} · Parameters={{Sequence; 4}; {Page; 0}; {Engine Intance; 16}; {Engine oil pressure; 24}; {Engine oil temp.; 40}; {Engine temp. Byte 0; 56}} · Module=Outboards (Generic) · Module index=0
- Lit : `Engine Intance`, `Engine oil pressure`, `Engine oil temp.`, `Engine temp. Byte 0`, `PGN-127489`, `Page`, `Sequence`
- Utilisé par : `Engine Oil Pressure - 1`, `Engine temp - 1`
- Ligne export : 109301 · id 220962

#### Engine oil pressure  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127489-0`, `Engine Oil Pressure`
- Ligne export : 109336 · id 220963

#### Engine Oil Pressure  `MAC`
- Propriétés : Unit=kPa · Limiting object group=Signed
- Logique :
  - **Controlling** = `Engine oil pressure / 10`
- Lit : `Engine oil pressure`
- Utilisé par : `Engine Oil Pressure - 1`, `Engine Oil Pressure - 2`
- Ligne export : 109349 · id 220964

#### Engine temp. Byte 0  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `127489-0`, `Engine temp`
- Ligne export : 109393 · id 220972

#### 127489-1  `GFIN`
- Propriétés : Identifier=PGN-127489 · Data length=Dont care · Timeout=1000 · Paged protocol={0x0F; 1} · Parameters={{Sequence; 4}; {Page; 0}; {Engine temp. Byte 1; 8}; {Alternator potential; 16}; {Fuel rate; 32}; {Total engine hours - Byte 0; 48}} · Module=Outboards (Generic) · Module index=6
- Lit : `Alternator potential`, `Engine temp. Byte 1`, `Fuel rate`, `PGN-127489`, `Page`, `Sequence`, `Total engine hours - Byte 0`
- Utilisé par : `Alternator - 1`, `Engine Hour - 1`, `Fuel rate - 1`
- Ligne export : 109405 · id 220973

#### Engine temp. Byte 1  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `127489-1`, `Engine temp`
- Ligne export : 109440 · id 220974

#### Engine temp  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `(((256 * Engine temp. Byte 1) + Engine temp. Byte 0) / 100) + -273,15`
- Lit : `Engine temp. Byte 0`, `Engine temp. Byte 1`
- Utilisé par : `Engine temp - 1`, `Engine temp - 2`
- Ligne export : 109452 · id 220975

#### Alternator potential  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127489-1`, `Alternator - 1`, `Alternator - 2`, `Alternator potential`
- Ligne export : 109523 · id 220986

#### Alternator potential  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `Alternator potential / 100`
- Lit : `Alternator potential`
- Utilisé par : `127489-1`, `Alternator - 1`, `Alternator - 2`
- Ligne export : 109536 · id 220987

#### Fuel rate  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127489-1`, `Fuel rate`, `Fuel rate - 1`, `Fuel rate - 2`
- Ligne export : 109580 · id 220995

#### Fuel rate  `MAC`
- Propriétés : Unit=L/h · Limiting object group=Signed
- Logique :
  - **Controlling** = `Fuel rate / 10`
- Lit : `Fuel rate`
- Utilisé par : `127489-1`, `Fuel rate - 1`, `Fuel rate - 2`
- Ligne export : 109593 · id 220996

#### Total engine hours - Byte 0  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127489-1`, `Engine Hour`
- Ligne export : 109637 · id 221004

#### 127489-2  `GFIN`
- Propriétés : Identifier=PGN-127489 · Data length=Dont care · Timeout=1000 · Paged protocol={0x0F; 2} · Parameters={{Total engine hours - Byte 1; 8}} · Module=Outboards (Generic) · Module index=7
- Lit : `PGN-127489`, `Total engine hours - Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 109650 · id 221005

#### Total engine hours - Byte 1  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127489-2`, `Engine Hour`
- Ligne export : 109670 · id 221006

#### Engine Hour  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `((65536 * Total engine hours - Byte 1) + Total engine hours - Byte 0) / 3600`
- Lit : `Total engine hours - Byte 0`, `Total engine hours - Byte 1`
- Utilisé par : `Engine Hour - 1`, `Engine Hour - 2`
- Ligne export : 109683 · id 221007

#### Engine Intance  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=99999
- Utilisé par : `127489-0`, `Alternator - 1`, `Alternator - 2`, `Engine Hour - 1`, `Engine Hour - 2`, `Engine Oil Pressure - 1`, `Engine Oil Pressure - 2`, `Engine temp - 1`, `Engine temp - 2`, `Fuel rate - 1`, `Fuel rate - 2`
- Ligne export : 109745 · id 221017

#### Engine Oil Pressure - 1  `MEM`
- Propriétés : Input channel=Engine Oil Pressure [kPa] · Action=Replace · Store value=No · Reset value=0 · Function selector=md4 Engine Brand
- Fonction *Mercury* :
  - **Activating** = `PositiveFlank((Engine Intance = 0))`
- Fonction *Yamaha* :
  - **Activating** = `PositiveFlank((Engine Intance = 0))`
- Fonction *COX* :
  - **Activating** = `Engine_Nmea AND 127489-0`
- Lit : `127489-0`, `Engine Intance`, `Engine Oil Pressure`, `Engine_Nmea`, `md4 Engine Brand`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 109757 · id 221018

#### Engine temp - 1  `MEM`
- Propriétés : Input channel=Engine temp [°C] · Action=Replace · Store value=No · Reset value=0 · Function selector=md4 Engine Brand
- Fonction *Mercury* :
  - **Activating** = `Engine Intance = 0`
- Fonction *Yamaha* :
  - **Activating** = `Engine Intance = 0`
- Fonction *COX* :
  - **Activating** = `Engine_Nmea AND 127489-0`
- Lit : `127489-0`, `Engine Intance`, `Engine temp`, `Engine_Nmea`, `md4 Engine Brand`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 109890 · id 221043

#### Fuel rate - 1  `MEM`
- Propriétés : Input channel=Fuel rate [L/h] · Action=Replace · Store value=No · Reset value=0 · Function selector=md4 Engine Brand
- Fonction *Mercury* :
  - **Activating** = `Engine Intance = 0`
- Fonction *Yamaha* :
  - **Activating** = `Engine Intance = 0`
- Fonction *COX* :
  - **Activating** = `Engine_Nmea AND 127489-1`
- Lit : `127489-1`, `Engine Intance`, `Engine_Nmea`, `Fuel rate`, `md4 Engine Brand`
- Utilisé par : `Fuel Economy`, `MD4-10 page: OUTBOARD`
- Ligne export : 110007 · id 221066

#### Engine Hour - 1  `MEM`
- Propriétés : Input channel=Engine Hour [h] · Action=Replace · Store value=No · Reset value=0 · Function selector=md4 Engine Brand
- Fonction *Mercury* :
  - **Activating** = `Engine Intance = 0`
- Fonction *Yamaha* :
  - **Activating** = `Engine Intance = 0`
- Fonction *COX* :
  - **Activating** = `Engine_Nmea AND 127489-1`
- Lit : `127489-1`, `Engine Hour`, `Engine Intance`, `Engine_Nmea`, `md4 Engine Brand`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 110124 · id 221089

#### Engine Oil Pressure - 2  `MEM`
- Propriétés : Input channel=Engine Oil Pressure [kPa] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank((Engine Intance = 1))`
- Lit : `Engine Intance`, `Engine Oil Pressure`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 110241 · id 221112

#### Engine temp - 2  `MEM`
- Propriétés : Input channel=Engine temp [°C] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `Engine Intance = 1`
- Lit : `Engine Intance`, `Engine temp`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 110295 · id 221121

#### Fuel rate - 2  `MEM`
- Propriétés : Input channel=Fuel rate [L/h] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `Engine Intance = 1`
- Lit : `Engine Intance`, `Fuel rate`
- Utilisé par : `Fuel Economy`, `MD4-10 page: OUTBOARD`
- Ligne export : 110341 · id 221129

#### Engine Hour - 2  `MEM`
- Propriétés : Input channel=Engine Hour [h] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `Engine Intance = 1`
- Lit : `Engine Hour`, `Engine Intance`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 110387 · id 221137

#### Fuel Economy  `MAC`
- Propriétés : Unit=L/nm
- Logique :
  ```qcode
  if Speed Over Ground Kts  > 0 then
    value:= (Fuel rate - 1  + Fuel rate - 2  )/Speed Over Ground Kts
    if value < 20 then
      Result:= value
    else
      Result:=0
    endif
  else
    Result:=0
  endif
  ```
- Lit : `Fuel rate - 1`, `Fuel rate - 2`, `Speed Over Ground Kts`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 110433 · id 221145

#### md4 Fuel Tanks Selection  `SP`
- Propriétés : Input channel=None · Default state name=Tank 1 · States={Tank 2; Tank 1 and 2}
- Utilisé par : `Tank 1 - Show`, `Tank 2 - Show`, `Adjust group: Setup Outboard`, `Single adjust item: md4 Fuel Tanks Selection`
- Ligne export : 110460 · id 221166

#### Tank 1 - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(md4 Fuel Tanks Selection = 0) OR (md4 Fuel Tanks Selection = 2)`
- Lit : `md4 Fuel Tanks Selection`
- Utilisé par : `Fuel LOW`, `MD4-10 page: OUTBOARD`, `MD4-10 page: SHUTDOWN`
- Ligne export : 110473 · id 221169

#### Tank 2 - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(md4 Fuel Tanks Selection = 1) OR (md4 Fuel Tanks Selection = 2)`
- Lit : `md4 Fuel Tanks Selection`
- Utilisé par : `Fuel LOW`, `MD4-10 page: OUTBOARD`, `MD4-10 page: SHUTDOWN`
- Ligne export : 110527 · id 221178

#### Fuel LOW  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=500
- Logique :
  - **Activating** = `((md4 Engine 1 - Tank - MEM [%] < 10) and Tank 1 - Show) OR ((md4 Engine 2 - Tank - MEM [%] < 10) and Tank 2 - Show)`
- Lit : `Tank 1 - Show`, `Tank 2 - Show`, `md4 Engine 1 - Tank - MEM`, `md4 Engine 2 - Tank - MEM`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 110581 · id 221187

#### Alternator - 1  `MEM`
- Propriétés : Input channel=Alternator potential [V] · Action=Replace · Store value=No · Reset value=0 · Function selector=md4 Engine Brand
- Fonction *Mercury* :
  - **Activating** = `PositiveFlank((Engine Intance = 0))`
- Fonction *Yamaha* :
  - **Activating** = `PositiveFlank((Engine Intance = 0))`
- Fonction *COX* :
  - **Activating** = `Engine_Nmea AND 127489-1`
- Lit : `127489-1`, `Alternator potential`, `Engine Intance`, `Engine_Nmea`, `md4 Engine Brand`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 110653 · id 221198

#### Alternator - 2  `MEM`
- Propriétés : Input channel=Alternator potential [V] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank((Engine Intance = 1))`
- Lit : `Alternator potential`, `Engine Intance`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 110786 · id 221223

#### Mercury - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `md4 Engine Brand = 0`
- Lit : `md4 Engine Brand`
- Utilisé par : *(personne)*
- Ligne export : 110840 · id 221232

#### Yamaha - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `md4 Engine Brand = 1`
- Lit : `md4 Engine Brand`
- Utilisé par : *(personne)*
- Ligne export : 110885 · id 221240

#### Sequence  `GPIN`
- Propriétés : Length=4 bits · Type=Unsigned integer · Error value=0
- Utilisé par : `127489-0`, `127489-1`
- Ligne export : 110930 · id 221248

#### Page  `GPIN`
- Propriétés : Length=4 bits · Type=Unsigned integer · Error value=0
- Utilisé par : `127489-0`, `127489-1`
- Ligne export : 110942 · id 221249

#### Engine oil temp.  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127489-0`
- Ligne export : 110954 · id 221250

#### Sequence  `GPIN`
- Propriétés : Length=4 bits · Type=Unsigned integer · Error value=0
- Utilisé par : `127489-0`, `127489-1`
- Ligne export : 110967 · id 221251

#### Page  `GPIN`
- Propriétés : Length=4 bits · Type=Unsigned integer · Error value=0
- Utilisé par : `127489-0`, `127489-1`
- Ligne export : 110979 · id 221252

#### Cox - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `md4 Engine Brand = 2`
- Lit : `md4 Engine Brand`
- Utilisé par : *(personne)*
- Ligne export : 110991 · id 221253
