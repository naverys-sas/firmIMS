# MD4-10[0] application — NMEA

159 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## NMEA / GPS

#### GPS Speed factor  `SP`
- Propriétés : Input channel=None · Default state name=m/s · States={kts}
- Utilisé par : `GPS Factor`, `Adjust group: Config GPS`, `Single adjust item: GPS Speed factor`
- Ligne export : 27671 · id 61622

#### GPS Factor  `IP`
- Propriétés : Mode selector=GPS Speed factor · Default mode: m/s={5144} · Mode 1: kts={10000}
- Lit : `GPS Speed factor`
- Utilisé par : `Speed Over Ground Kts`
- Ligne export : 27683 · id 61624

#### Adress_Search  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Adress_Search OR (PositiveFlank(Adress Loose))`
  - **Blocking** = `PositiveFlank(Garmin - NMEA)`
- Lit : `Adress Loose`, `Adress_Search`, `Garmin - NMEA`
- Utilisé par : `Adress_Search`, `Adresse_Mem`, `GPS Adresse Find`
- Ligne export : 27697 · id 62886

#### GPS_Adresse_Find_Int  `IMAC`
- Logique :
  - **Controlling** = `GPS Adresse Find [s]`
- Lit : `GPS Adresse Find`
- Utilisé par : `Adresse_Mem`
- Ligne export : 27756 · id 63034

#### Adresse_Mem  `MEM`
- Propriétés : Input channel=GPS_Adresse_Find_Int · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `Adress_Search AND DerivativeOf(GPS_Adresse_Find_Int)`
- Lit : `Adress_Search`, `GPS_Adresse_Find_Int`
- Utilisé par : `GPS_Adress`
- Ligne export : 27797 · id 62997

#### GPS_Adress  `IMAC`
- Logique :
  ```qcode
  result := Adresse_Mem
  ```
- Lit : `Adresse_Mem`
- Utilisé par : `PGN-129025`, `PGN-129026`, `PGN-129029`
- Ligne export : 27849 · id 61665

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
- Ligne export : 27867 · id 61686

#### 129026-0  `GFIN`
- Propriétés : Identifier=PGN-129026 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Speed Over Ground Raw; 32}} · Module=Garmin (Generic) · Module index=0
- Lit : `PGN-129026`, `Speed Over Ground Raw`
- Utilisé par : `Garmin - NMEA`
- Ligne export : 27889 · id 61649

#### Garmin - NMEA  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `129026-0`
- Lit : `129026-0`
- Utilisé par : `Adress Loose`, `Adress_Search`, `MD4-10 page: INFO`
- Ligne export : 27908 · id 61641

#### Adress Loose  `IDC`
- Propriétés : Toggle=No · Delay on=120000 · Delay off=0
- Logique :
  - **Activating** = `KTB K1 IDC - GPS_EQT and (not(Garmin - NMEA))`
- Lit : `Garmin - NMEA`, `KTB K1 IDC - GPS_EQT`
- Utilisé par : `Adress_Search`
- Ligne export : 27951 · id 63001

#### GPS Adresse Find  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Adress_Search`
  - **Resetting** = `GPS Adresse Find [s] > 256`
- Lit : `Adress_Search`
- Utilisé par : `GPS_Adresse_Find_Int`
- Ligne export : 28004 · id 62881

#### Speed Over Ground Raw  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `129026-0`, `Speed Over Ground Kts`
- Ligne export : 28065 · id 61650

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
- Ligne export : 28078 · id 61625

#### PGN-129029  `IMAC`
- Logique :
  ```qcode
  pgn := 129029
  priority := 3
  source := GPS_Adress
  
  Result := priority * 0x4000000 + pgn * 0x100 + source
  ```
- Lit : `GPS_Adress`
- Utilisé par : `129029-0`, `129029-1`
- Ligne export : 28100 · id 62781

#### 129029-0  `GFIN`
- Propriétés : Identifier=PGN-129029 · Data length=DonÂt care · Timeout=1000 · Paged protocol={0x0F; 0} · Parameters={{Current Date J; 24}; {Time_Byte_1_2_J; 40}; {Time_Byte_3; 56}} · Module=Garmin (Generic) · Module index=1
- Lit : `Current Date J`, `PGN-129029`, `Time_Byte_1_2_J`, `Time_Byte_3`
- Utilisé par : *(personne)*
- Ligne export : 28122 · id 62761

#### Time_Byte_1_2_J  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `129029-0`, `Current Time`
- Ligne export : 28148 · id 62762

#### Time_Byte_3  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `129029-0`, `Current Time`
- Ligne export : 28161 · id 62763

#### 129029-1  `GFIN`
- Propriétés : Identifier=PGN-129029 · Data length=DonÂt care · Timeout=1000 · Paged protocol={0x0F; 1} · Parameters={{Time_Byte_4; 8}} · Module=Garmin (Generic) · Module index=2
- Lit : `PGN-129029`, `Time_Byte_4`
- Utilisé par : *(personne)*
- Ligne export : 28173 · id 62764

#### Time_Byte_4  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `129029-1`, `Current Time`
- Ligne export : 28193 · id 62765

#### Current Time  `MAC`
- Propriétés : Unit=h
- Logique :
  ```qcode
  Result := ( (Time_Byte_1_2_J / 10000)  + (Time_Byte_3 * 255*255 / 10000) + (Time_Byte_4  * 255*255*255/10000) )/3600
  ```
- Lit : `Time_Byte_1_2_J`, `Time_Byte_3`, `Time_Byte_4`
- Utilisé par : `Time Diff`
- Ligne export : 28205 · id 62163

#### Time  `SIC`
- Propriétés : Value=Time
- Utilisé par : `Hour actual`, `Time Diff`, `Adjust group: Master Setup`
- Ligne export : 28223 · id 62183

#### PGN-129025  `IMAC`
- Logique :
  ```qcode
  pgn := 129025
  priority := 2
  source := GPS_Adress
  
  Result := priority * 0x4000000 + pgn * 0x100 + source
  ```
- Lit : `GPS_Adress`
- Utilisé par : `129025-0`
- Ligne export : 28232 · id 62808

#### 129025-0  `GFIN`
- Propriétés : Identifier=PGN-129025 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Latitude G; 0}; {Longitude G; 32}} · Module=Garmin (Generic) · Module index=3
- Lit : `Latitude G`, `Longitude G`, `PGN-129025`
- Utilisé par : *(personne)*
- Ligne export : 28254 · id 62766

#### Latitude G  `GPIN`
- Propriétés : Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian · Error value=2000000000
- Utilisé par : `129025-0`, `Latitude Compute`
- Ligne export : 28276 · id 62767

#### Latitude Compute  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Latitude G * 1E-7`
- Lit : `Latitude G`
- Utilisé par : `Latitude Compute MEN`, `Works Latitude`
- Ligne export : 28289 · id 62186

#### Longitude G  `GPIN`
- Propriétés : Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian · Error value=2000000000
- Utilisé par : `129025-0`, `Longitude Compute`
- Ligne export : 28333 · id 62768

#### Longitude Compute  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Longitude G * 1E-7`
- Lit : `Longitude G`
- Utilisé par : `Longitude Compute MEN`, `Works Latitude`
- Ligne export : 28346 · id 62195

#### Works Latitude  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Latitude Compute <= 180) AND (Longitude Compute <= 180)`
- Lit : `Latitude Compute`, `Longitude Compute`
- Utilisé par : `New Timer`
- Ligne export : 28390 · id 62203

#### New Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Works Latitude`
  - **Resetting** = `(New Timer [s] > 10) OR (NegativeFlank(Works Latitude))`
- Lit : `Works Latitude`
- Utilisé par : `Current Date MEN`, `Latitude Compute MEN`, `Longitude Compute MEN`, `Time_Diff_MEM`
- Ligne export : 28444 · id 62212

#### Time Diff  `MAC`
- Logique :
  ```qcode
  Result := Time - Current Time
  ```
- Lit : `Current Time`, `Time`
- Utilisé par : `Time_Diff_MEM`
- Ligne export : 28513 · id 62224

#### Time_Diff_MEM  `MEM`
- Propriétés : Input channel=Time Diff · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `New Timer [s] >= 10`
- Lit : `New Timer`, `Time Diff`
- Utilisé par : `Hour actual`
- Ligne export : 28531 · id 62234

#### Hour actual  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `Time - Time_Diff_MEM`
- Lit : `Time`, `Time_Diff_MEM`
- Utilisé par : `Backlight Value`
- Ligne export : 28577 · id 62242

#### Fuseau  `IP`
- Propriétés : Unit=h · Default mode={0}
- Utilisé par : `CouchÃ© night`, `LevÃ© night`, `MÃ©ridian`, `Sunrise`, `Sunset`
- Ligne export : 28621 · id 62250

#### Current Date J  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `129029-0`, `Current Date MEN`
- Ligne export : 28633 · id 62769

#### Current Date MEN  `MEM`
- Propriétés : Input channel=Current Date J · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `New Timer [s] >= 10`
- Lit : `Current Date J`, `New Timer`
- Utilisé par : `days since 2000`
- Ligne export : 28646 · id 62252

#### days since 2000  `IMAC`
- Logique :
  ```qcode
  Result := Current Date MEN - 10957
  ```
- Lit : `Current Date MEN`
- Utilisé par : `Days in current year`, `Year since 2000`
- Ligne export : 28692 · id 62260

#### Year since 2000  `IMAC`
- Logique :
  - **Controlling** = `days since 2000 div 365`
- Lit : `days since 2000`
- Utilisé par : `Days in current year`
- Ligne export : 28710 · id 62270

#### Days in current year  `IMAC`
- Logique :
  - **Controlling** = `(days since 2000 - (Year since 2000 * 365)) - (Year since 2000 div 4)`
- Lit : `C`, `Year since 2000`, `days since 2000`
- Utilisé par : `L`, `M`
- Ligne export : 28753 · id 62278

#### M  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(Days in current year * 0,9856) + 356,8`
- Lit : `Days in current year`
- Utilisé par : `C`
- Ligne export : 28823 · id 62289

#### C  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(((M * 2) sin ) * 0,02) + ((M sin ) * 1,9137)`
- Lit : `M`
- Utilisé par : `0x191AFF71`, `0x351`, `0x352`, `Auto Off - Timer`, `Charger end charge`, `CouchÃ© night`, `Couple Moteur`, `Couple Moteur`, `Days in current year`, `ET`, `End of Tension Phase Delay`, `Engine temp`, `GFIN-C:N1_Tx_Info`, `GFIN-D:N2_Tx_Info`, `Ho`, `Ho_night`, `L`, `LevÃ© night`, `M1 - Charge`, `M2 - Charge`, `M3 - Charge`, `MDGN-Temp:MC2[1]`, `Ok to move`, `R`, `Start Button`, `State Up/Down`, `Stop Cruise`, `Sunrise`, `Sunset`, `Temp:MD4-10[0]`, `VIEW SOC 2`, `ZAPI_M1_Torque`, `ZAPI_M2_Torque`
- Ligne export : 28876 · id 62298

#### L  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = ``
- Lit : `C`, `Days in current year`
- Utilisé par : `Dec`, `R`
- Ligne export : 28963 · id 62311

#### Dec  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `((L sin ) * 0,39774) asin `
- Lit : `L`
- Utilisé par : `Ho`, `Ho_night`
- Ligne export : 29025 · id 62321

#### Latitude Compute MEN  `MEM`
- Propriétés : Input channel=Latitude Compute · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `New Timer [s] >= 10`
- Lit : `Latitude Compute`, `New Timer`
- Utilisé par : `Ho`, `Ho_night`
- Ligne export : 29085 · id 62331

#### Ho  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(-0,1 - ((Dec sin ) * (Latitude Compute MEN sin ))) / ((Dec cos ) * (Latitude Compute MEN cos ))`
- Lit : `C`, `Dec`, `Latitude Compute MEN`
- Utilisé par : `Ho h`
- Ligne export : 29131 · id 62339

#### Ho h  `MAC`
- Propriétés : Unit=h
- Logique :
  ```qcode
  if Ho  > 1 or Ho < -1 then
    Result := 12
  else
    Result := acos (Ho) /15
  endif
  ```
- Lit : `Ho`
- Utilisé par : `Sunrise`, `Sunset`
- Ligne export : 29234 · id 62355

#### Longitude Compute MEN  `MEM`
- Propriétés : Input channel=Longitude Compute · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `New Timer [s] >= 10`
- Lit : `Longitude Compute`, `New Timer`
- Utilisé par : `Lon`
- Ligne export : 29256 · id 62363

#### Lon  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `Longitude Compute MEN / -15`
- Lit : `Longitude Compute MEN`
- Utilisé par : `CouchÃ© night`, `LevÃ© night`, `MÃ©ridian`, `Sunrise`, `Sunset`
- Ligne export : 29302 · id 62371

#### R  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(((L * 4) sin ) * 0,053) + (((L * 2) sin ) * -2,4652)`
- Lit : `C`, `L`
- Utilisé par : `ET`
- Ligne export : 29346 · id 62379

#### ET  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(C + R) * 4`
- Lit : `C`, `R`
- Utilisé par : `ET h`
- Ligne export : 29442 · id 62393

#### ET h  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `ET / 60`
- Lit : `ET`
- Utilisé par : `CouchÃ© night`, `LevÃ© night`, `MÃ©ridian`, `Sunrise`, `Sunset`
- Ligne export : 29495 · id 62402

#### Sunset  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `(((12 + ET h [h]) + Lon [h]) + Fuseau [h]) - Ho h [h]`
- Lit : `C`, `ET h`, `Fuseau`, `Ho h`, `Lon`
- Utilisé par : `Backlight Value`, `DurÃ©e`
- Ligne export : 29539 · id 62410

#### Sunrise  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `(((12 + ET h [h]) + Lon [h]) + Fuseau [h]) + Ho h [h]`
- Lit : `C`, `ET h`, `Fuseau`, `Ho h`, `Lon`
- Utilisé par : `Backlight Value`, `DurÃ©e`
- Ligne export : 29610 · id 62421

#### DurÃ©e  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Sunrise [h] - Sunset [h]`
- Lit : `Sunrise`, `Sunset`
- Utilisé par : *(personne)*
- Ligne export : 29681 · id 62432

#### Min back light  `IP`
- Propriétés : Unit=% · Default mode={20}
- Utilisé par : `Backlight Value`, `Adjust group: Back Light Setup`, `Single adjust item: Min back light`
- Ligne export : 29725 · id 62440

#### Ho_night  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(-0,105 - ((Dec sin ) * (Latitude Compute MEN sin ))) / ((Dec cos ) * (Latitude Compute MEN cos ))`
- Lit : `C`, `Dec`, `Latitude Compute MEN`
- Utilisé par : `Ho night h`
- Ligne export : 29737 · id 62441

#### Ho night h  `MAC`
- Propriétés : Unit=h
- Logique :
  ```qcode
  if Ho_night   > 1 or Ho_night < -1 then
    Result := 12
  else
    Result := acos (Ho_night) /15
  endif
  ```
- Lit : `Ho_night`
- Utilisé par : `CouchÃ© night`, `LevÃ© night`
- Ligne export : 29840 · id 62456

#### LevÃ© night  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxOf(((((12 + ET h [h]) + Lon [h]) + Fuseau [h]) - Ho night h [h]), 0)`
- Lit : `C`, `ET h`, `Fuseau`, `Ho night h`, `Lon`
- Utilisé par : `Backlight Value`
- Ligne export : 29864 · id 62473

#### CouchÃ© night  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `MinOf(((((12 + ET h [h]) + Lon [h]) + Fuseau [h]) + Ho night h [h]), 24)`
- Lit : `C`, `ET h`, `Fuseau`, `Ho night h`, `Lon`
- Utilisé par : `Backlight Value`
- Ligne export : 29944 · id 62485

#### MODE  `DP`
- Propriétés : True text=AUTO (GPS) · False text=MANUAL · Default mode={True}
- Utilisé par : `Back Light State`, `Adjust group: Back Light Setup`, `Single adjust item: MODE`
- Ligne export : 30024 · id 62497

#### Screen backlight default value  `IP`
- Propriétés : Unit=% · Default mode={100}
- Utilisé par : `Back Light State`, `Backlight Value`, `Adjust group: Back Light Setup`, `MD4-10 page: FEATURE`, `Single adjust item: Screen backlight default value`
- Ligne export : 30037 · id 62498

#### Wait 20 secondes  `IDC`
- Propriétés : Toggle=No · Delay on=20000 · Delay off=0
- Logique :
  - **Activating** = `True`
- Utilisé par : `Back Light State`
- Ligne export : 30049 · id 84483

#### Back Light State  `FSM`
- Propriétés : Store value=No
- État 0 **Starting**
  - transition *0 - 1* (état cible non exporté par IQANdesign)
    - **Activating** = `Wait 20 secondes`
- État 1 **Manual**
  - transition *1 - 2* (état cible non exporté par IQANdesign)
    ```qcode
    Result := MODE
    ```
- État 2 **Auto**
  - transition *2 - 1* (état cible non exporté par IQANdesign)
    ```qcode
    Result := not(MODE)
    ```
  - transition *2 - 3* (état cible non exporté par IQANdesign)
    ```qcode
    Result := PositiveFlank(Power Down  )
    ```
  - transition *Manual* (état cible non exporté par IQANdesign)
    ```qcode
    Result := DerivativeOf  (Screen backlight default value  ) <> 0
    ```
- État 3 **Charging**
  - transition *3 - 1* (état cible non exporté par IQANdesign)
    ```qcode
    Result := NegativeFlank(Power Down  )
    ```
- État 4 **Force Manual**
- Lit : `MODE`, `Power Down`, `Screen backlight default value`, `Wait 20 secondes`
- Utilisé par : `Auto Light ON`, `Backlight Value`
- Ligne export : 30092 · id 62499

#### Backlight Value  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Back Light State
- Fonction *Starting* :
  - **Controlling** = `100`
- Fonction *Manual* :
  - **Controlling** = `MaxOf(Screen backlight default value [%], Min back light [%])`
- Fonction *Auto* :
  - **Controlling** = `MaxOf(Min back light [%], courbe(Hour actual [h]: {{LevÃ© night [h]; Min back light [%]}; {Sunset [h]; 100}; {Sunrise [h]; 100}; {CouchÃ© night [h]; Min back light [%]}}, Freeze))`
- Fonction *Charging* :
  - **Controlling** = `50`
- Fonction *Force Manual* :
  - **Controlling** = `MaxOf(Screen backlight default value [%], Min back light [%])`
- Lit : `Back Light State`, `CouchÃ© night`, `Hour actual`, `LevÃ© night`, `Min back light`, `Screen backlight default value`, `Sunrise`, `Sunset`
- Utilisé par : `Auto Light ON`, `Backlight Value Filter`
- Ligne export : 30230 · id 62545

#### MÃ©ridian  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `((12 + ET h [h]) + Lon [h]) + Fuseau [h]`
- Lit : `ET h`, `Fuseau`, `Lon`
- Utilisé par : *(personne)*
- Ligne export : 30423 · id 62574

#### Auto Light ON  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=2000 · Function selector=Back Light State
- Fonction *Starting* : (vide)
- Fonction *Manual* : (vide)
- Fonction *Auto* :
  - **Activating** = `Backlight Value [%] <= 95`
- Fonction *Charging* : (vide)
- Fonction *Force Manual* : (vide)
- Lit : `Back Light State`, `Backlight Value`
- Utilisé par : `Auto Light and Start`
- Ligne export : 30485 · id 62584

#### Backlight Value Filter  `SFC`
- Propriétés : Input channel=Backlight Value [%] · Enable=Yes · Type=Slopes · Slopes={{50; 10}; {50; 50}}
- Lit : `Backlight Value`
- Utilisé par : *(personne)*
- Ligne export : 30626 · id 62610

## NMEA / OutBoard

#### Engine Brand  `SP`
- Propriétés : Input channel=None · Default state name=Mercury · States={Yamaha; COX}
- Utilisé par : `Adress Loose`, `Alternator - 1`, `Cox - Show`, `Engine 2 - Tank`, `Engine Hour - 1`, `Engine Oil Pressure - 1`, `Engine temp - 1`, `Fuel rate - 1`, `Mercury - Show`, `OutBoard_Adresse`, `Outboard_Priority`, `Trim Value`, `Yamaha - Show`, `Adjust group: Config Outboard`, `Single adjust item: Engine Brand`
- Ligne export : 23850 · id 61033

#### Engine_Nmea  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Engine ON - 1 - NMEA) OR (Engine ON - 2 - NMEA)`
- Lit : `Engine ON - 1 - NMEA`, `Engine ON - 2 - NMEA`
- Utilisé par : `Adress Loose Auto`, `Adress_Search`, `Alternator - 1`, `Engine Hour - 1`, `Engine Oil Pressure - 1`, `Engine temp - 1`, `Fuel rate - 1`
- Ligne export : 23863 · id 63240

#### Adress Loose  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0 · Function selector=Engine Brand
- Fonction *Mercury* :
  - **Activating** = `Adress Loose Auto`
- Fonction *Yamaha* :
  - **Activating** = `Adress Loose Auto`
- Fonction *COX* : (vide)
- Lit : `Adress Loose Auto`, `Engine Brand`
- Utilisé par : `Adress_Search`
- Ligne export : 23913 · id 63164

#### Adress_Search  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Adress_Search OR (PositiveFlank(Adress Loose))`
  - **Blocking** = `PositiveFlank(Engine_Nmea)`
- Lit : `Adress Loose`, `Adress_Search`, `Engine_Nmea`
- Utilisé par : `Adress_Search`, `Adresse_Mem`, `Outboard Adresse Find`
- Ligne export : 24011 · id 63173

#### Outboard Adresse Find  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Adress_Search`
  - **Resetting** = `Outboard Adresse Find [s] > 256`
- Lit : `Adress_Search`
- Utilisé par : `Outboard_Adress_Find_Int`
- Ligne export : 24070 · id 63183

#### Outboard_Adress_Find_Int  `IMAC`
- Logique :
  - **Controlling** = `Outboard Adresse Find [s]`
- Lit : `Outboard Adresse Find`
- Utilisé par : `Adresse_Mem`
- Ligne export : 24131 · id 63194

#### Adresse_Mem  `MEM`
- Propriétés : Input channel=Outboard_Adress_Find_Int · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `Adress_Search AND DerivativeOf(Outboard_Adress_Find_Int)`
- Lit : `Adress_Search`, `Outboard_Adress_Find_Int`
- Utilisé par : `OutBoard_Adresse`
- Ligne export : 24172 · id 63202

#### OutBoard_Adresse  `IMAC`
- Propriétés : Function selector=Engine Brand
- Fonction *Mercury* :
  ```qcode
  result := Adresse_Mem
  ```
- Fonction *Yamaha* :
  ```qcode
  result := Adresse_Mem
  ```
- Fonction *COX* :
  ```qcode
  result:=0
  ```
- Lit : `Adresse_Mem`, `Engine Brand`
- Utilisé par : `PGN-127488`, `PGN-127489`, `PNG-127505`
- Ligne export : 24224 · id 60922

#### Outboard_Priority  `IMAC`
- Propriétés : Function selector=Engine Brand
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
- Lit : `Engine Brand`
- Utilisé par : `PGN-127488`, `PGN-127489`
- Ligne export : 24258 · id 92516

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
- Ligne export : 24292 · id 60929

#### 127488-Eng 1  `GFIN`
- Propriétés : Identifier=PGN-127488 · Data length=DonÂt care · Timeout=1000 · Paged protocol={0xFF; 0} · Parameters={{Engine 1 - Speed - Raw; 8}; {Engine 1 - Trim; 40}} · Module=OutBoard (Generic) · Module index=0
- Lit : `Engine 1 - Speed - Raw`, `Engine 1 - Trim`, `PGN-127488`
- Utilisé par : `Engine ON - 1 - NMEA`
- Ligne export : 24314 · id 60940

#### Engine ON - 1 - NMEA  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `127488-Eng 1`
- Lit : `127488-Eng 1`
- Utilisé par : `Engine_Nmea`, `MD4-10 page: MAIN`, `MD4-10 page: OUTBOARD`
- Ligne export : 24337 · id 61133

#### 127488-Eng 2  `GFIN`
- Propriétés : Identifier=PGN-127488 · Data length=DonÂt care · Timeout=1000 · Paged protocol={0xFF; 1} · Parameters={{Engine 2 - Speed - Raw; 8}; {Engine 2 - Trim; 40}} · Module=OutBoard (Generic) · Module index=6
- Lit : `Engine 2 - Speed - Raw`, `Engine 2 - Trim`, `PGN-127488`
- Utilisé par : `Engine ON - 2 - NMEA`
- Ligne export : 24380 · id 60953

#### Engine ON - 2 - NMEA  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `127488-Eng 2`
- Lit : `127488-Eng 2`
- Utilisé par : `Engine_Nmea`, `MD4-10 page: MAIN`, `MD4-10 page: OUTBOARD`
- Ligne export : 24403 · id 61346

#### Adress Loose Auto  `IDC`
- Propriétés : Toggle=No · Delay on=120000 · Delay off=0
- Logique :
  - **Activating** = `not(Engine_Nmea) AND (KTC K9 IDC - OutBoard On-OFF)`
- Lit : `Engine_Nmea`, `KTC K9 IDC - OutBoard On-OFF`
- Utilisé par : `Adress Loose`
- Ligne export : 24446 · id 92483

#### Engine 1 - Speed - Raw  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127488-Eng 1`, `Engine 1 - Speed - filter`
- Ligne export : 24497 · id 60941

#### Engine 1 - Speed - filter  `SFC`
- Propriétés : Input channel=Engine 1 - Speed - Raw · Enable=Yes · Type=Filter · Filter=98
- Lit : `Engine 1 - Speed - Raw`
- Utilisé par : `Engine 1 - Speed`
- Ligne export : 24510 · id 60942

#### Engine 1 - Speed  `MAC`
- Propriétés : Unit=Rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `(Round((Engine 1 - Speed - filter / 400))) * 100`
- Lit : `Engine 1 - Speed - filter`
- Utilisé par : `Engine 1 - RUN`, `Engine 1 - Speed - Gauge`, `Engine RUN FAST - NMEA`
- Ligne export : 24522 · id 60943

#### Engine 2 - Speed - Raw  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127488-Eng 2`, `Engine 2 - Speed - filter`
- Ligne export : 24583 · id 60954

#### Engine 2 - Speed - filter  `SFC`
- Propriétés : Input channel=Engine 2 - Speed - Raw · Enable=Yes · Type=Filter · Filter=98
- Lit : `Engine 2 - Speed - Raw`
- Utilisé par : `Engine 2 - Speed`
- Ligne export : 24596 · id 60955

#### Engine 2 - Speed  `MAC`
- Propriétés : Unit=Rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `(Round((Engine 2 - Speed - filter / 400))) * 100`
- Lit : `Engine 2 - Speed - filter`
- Utilisé par : `Engine 2 - RUN`, `Engine 2 - Speed - Gauge`, `Engine RUN FAST - NMEA`
- Ligne export : 24608 · id 60956

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
- Ligne export : 24669 · id 60966

#### 127505-Eng 1 - Can  `GFIN`
- Propriétés : Identifier=PNG-127505 · Data length=DonÂt care · Timeout=3000 · Paged protocol={0x0F; 0} · Parameters={{Engine 1 - Tank - RAW; 8}} · Module=OutBoard (Generic) · Module index=5
- Lit : `Engine 1 - Tank - RAW`, `PNG-127505`
- Utilisé par : `Engine 1 - Tank - MEM`
- Ligne export : 24691 · id 60977

#### Engine 1 - Tank - RAW  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127505-Eng 1 - Can`, `Engine 1 - Tank`
- Ligne export : 24711 · id 60978

#### Engine 1 - Tank  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin((Engine 1 - Tank - RAW / 250): 0->0, 95->100, Freeze)`
- Lit : `Engine 1 - Tank - RAW`
- Utilisé par : `Engine 1 - Tank`, `Engine 1 - Tank - MEM`, `MD4-10 page: OUTBOARD`
- Ligne export : 24724 · id 60979

#### 127505-Eng 2 Page 1- Can  `GFIN`
> Tank 2 Reading for Yamaha Engines
- Propriétés : Identifier=PNG-127505 · Data length=DonÂt care · Timeout=3000 · Paged protocol={0x0F; 1} · Parameters={{Engine 2 Page 1 - Tank - Raw; 8}} · Module=OutBoard (Generic) · Module index=4
- Lit : `Engine 2 Page 1 - Tank - Raw`, `PNG-127505`
- Utilisé par : `Engine 2 - Tank - MEM`
- Ligne export : 24780 · id 60988

#### Engine 2 Page 1 - Tank - Raw  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127505-Eng 2 Page 1- Can`, `Engine 2 - Tank`
- Ligne export : 24800 · id 60989

#### 127505-Eng 2 Page 2- Can  `GFIN`
> Tank 2 Reading for Mercury engines
- Propriétés : Identifier=PNG-127505 · Data length=DonÂt care · Timeout=3000 · Paged protocol={0x0F; 2} · Parameters={{Engine 2 Page 2 - Tank - Raw; 8}} · Module=OutBoard (Generic) · Module index=7
- Lit : `Engine 2 Page 2 - Tank - Raw`, `PNG-127505`
- Utilisé par : *(personne)*
- Ligne export : 24813 · id 94310

#### Engine 2 Page 2 - Tank - Raw  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127505-Eng 2 Page 2- Can`, `Engine 2 - Tank`
- Ligne export : 24833 · id 94311

#### Engine 2 - Tank  `MAC`
> Tank Value, depending on Engine brand (PGN page is different)
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=Engine Brand
- Fonction *Mercury* :
  - **Controlling** = `lin((Engine 2 Page 2 - Tank - Raw / 250): 0->0, 95->100, Freeze)`
- Fonction *Yamaha* :
  - **Controlling** = `lin((Engine 2 Page 1 - Tank - Raw / 250): 0->0, 95->100, Freeze)`
- Fonction *COX* :
  - **Controlling** = `0`
- Lit : `Engine 2 Page 1 - Tank - Raw`, `Engine 2 Page 2 - Tank - Raw`, `Engine Brand`
- Utilisé par : `Engine 2 - Tank`, `Engine 2 - Tank - MEM`, `MD4-10 page: OUTBOARD`
- Ligne export : 24846 · id 60990

#### Engine 1 - Tank - MEM  `MEM`
- Propriétés : Input channel=Engine 1 - Tank [%] · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `127505-Eng 1 - Can`
- Lit : `127505-Eng 1 - Can`, `Engine 1 - Tank`
- Utilisé par : `Fuel LOW`, `MD4-10 page: SHUTDOWN`
- Ligne export : 24978 · id 60999

#### Engine 2 - Tank - MEM  `MEM`
- Propriétés : Input channel=Engine 2 - Tank [%] · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `127505-Eng 2 Page 1- Can`
- Lit : `127505-Eng 2 Page 1- Can`, `Engine 2 - Tank`
- Utilisé par : `Fuel LOW`, `MD4-10 page: SHUTDOWN`
- Ligne export : 25022 · id 61008

#### Engine 1 - Speed - Gauge  `MAC`
- Propriétés : Unit=100 Rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Engine 1 - Speed [Rpm] / 100`
- Lit : `Engine 1 - Speed`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 25066 · id 61017

#### Engine 2 - Speed - Gauge  `MAC`
- Propriétés : Unit=100 Rpm · Limiting object group=Signed
- Logique :
  - **Controlling** = `Engine 2 - Speed [Rpm] / 100`
- Lit : `Engine 2 - Speed`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 25110 · id 61025

#### Trim Value  `IP`
- Propriétés : Mode selector=Engine Brand · Default mode: Mercury={100} · Mode 1: Yamaha={250} · Mode 2: COX={100}
- Lit : `Engine Brand`
- Utilisé par : `Engine 1 - Trim - Gauge`, `Engine 2 - Trim - Gauge`
- Ligne export : 25154 · id 61035

#### Engine 1 - Trim  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `127488-Eng 1`, `Engine 1 - Trim - Gauge`
- Ligne export : 25170 · id 61036

#### Engine 1 - Trim - Gauge  `MAC`
- Propriétés : Unit=Raw · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Engine 1 - Trim: 0->0, Trim Value->100, Freeze)`
- Lit : `Engine 1 - Trim`, `Trim Value`
- Utilisé par : `Engine 1 - Down`, `MD4-10 page: MAIN`, `MD4-10 page: OUTBOARD`
- Ligne export : 25182 · id 61037

#### Engine 2 - Trim  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `127488-Eng 2`, `Engine 2 - Trim - Gauge`
- Ligne export : 25229 · id 61045

#### Engine 2 - Trim - Gauge  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Engine 2 - Trim: 0->0, Trim Value->100, Freeze)`
- Lit : `Engine 2 - Trim`, `Trim Value`
- Utilisé par : `Engine 2 - Down`, `MD4-10 page: MAIN`, `MD4-10 page: OUTBOARD`
- Ligne export : 25241 · id 61046

#### Engine 1 - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `True`
- Utilisé par : `Engine 1 - Down`, `Engine 1 - Not Down`
- Ligne export : 25288 · id 61054

#### Engine 1 - Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine 1 - Trim - Gauge [Raw] < 1`
  - **Blocking** = `not(Engine 1 - Show)`
- Lit : `Engine 1 - Show`, `Engine 1 - Trim - Gauge`
- Utilisé par : `Engine 1 - Not Down`, `MD4-10 page: OUTBOARD`
- Ligne export : 25331 · id 61062

#### Engine 1 - Not Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Engine 1 - Down)`
  - **Blocking** = `not(Engine 1 - Show)`
- Lit : `Engine 1 - Down`, `Engine 1 - Show`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 25384 · id 61071

#### Number of Engines  `SP`
- Propriétés : Input channel=None · Default state name=1 Engines · States={2 Engines}
- Utilisé par : `Engine 2 - Show`, `Adjust group: Config Outboard`, `Single adjust item: Number of Engines`
- Ligne export : 25436 · id 61080

#### Engine 2 - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Number of Engines = 1`
- Lit : `Number of Engines`
- Utilisé par : `Engine 2 - Down`, `Engine 2 - Not Down`, `MD4-10 page: OUTBOARD`
- Ligne export : 25448 · id 61082

#### Engine 2 - Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine 2 - Trim - Gauge < 1`
  - **Blocking** = `not(Engine 2 - Show)`
- Lit : `Engine 2 - Show`, `Engine 2 - Trim - Gauge`
- Utilisé par : `Engine 2 - Not Down`, `MD4-10 page: OUTBOARD`
- Ligne export : 25493 · id 61090

#### Engine 2 - Not Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Engine 2 - Down)`
  - **Blocking** = `not(Engine 2 - Show)`
- Lit : `Engine 2 - Down`, `Engine 2 - Show`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 25546 · id 61099

#### Engine 2 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine 2 - Speed [Rpm] > 100`
- Lit : `Engine 2 - Speed`
- Utilisé par : `Engine RUN - NMEA`, `MD4-10 page: MAIN`
- Ligne export : 25598 · id 61108

#### Engine 1 - RUN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine 1 - Speed [Rpm] > 100`
- Lit : `Engine 1 - Speed`
- Utilisé par : `Engine RUN - NMEA`, `MD4-10 page: MAIN`
- Ligne export : 25643 · id 61116

#### Engine RUN - NMEA  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(Engine 1 - RUN) OR (Engine 2 - RUN)`
- Lit : `Engine 1 - RUN`, `Engine 2 - RUN`
- Utilisé par : *(personne)*
- Ligne export : 25688 · id 61124

#### Fuel Capacity (One Tank)  `IP`
- Propriétés : Unit=L · Default mode={190}
- Utilisé par : `Engine 1 - Tank`, `Engine 2 - Tank`, `Adjust group: Config Outboard`, `Single adjust item: Fuel Capacity (One Tank)`
- Ligne export : 25738 · id 61141

#### Engine 1 - Tank  `MAC`
- Propriétés : Unit=L · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Engine 1 - Tank [%]: 0->0, 100->Fuel Capacity (One Tank) [L], Freeze)`
- Lit : `Engine 1 - Tank`, `Fuel Capacity (One Tank)`
- Utilisé par : `Engine 1 - Tank - MEM`, `MD4-10 page: OUTBOARD`
- Ligne export : 25750 · id 61142

#### Engine 2 - Tank  `MAC`
- Propriétés : Unit=L · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Engine 2 - Tank [%]: 0->0, 100->Fuel Capacity (One Tank) [L], Freeze)`
- Lit : `Engine 2 - Tank`, `Fuel Capacity (One Tank)`
- Utilisé par : `Engine 2 - Tank - MEM`, `MD4-10 page: OUTBOARD`
- Ligne export : 25797 · id 61150

#### Engine RUN FAST - NMEA  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `(Engine 1 - Speed [Rpm] > 2000) OR (Engine 2 - Speed [Rpm] > 2000)`
- Lit : `Engine 1 - Speed`, `Engine 2 - Speed`
- Utilisé par : `Gauge Page IDC`
- Ligne export : 25844 · id 61158

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
- Ligne export : 25898 · id 61167

#### 127489-0  `GFIN`
- Propriétés : Identifier=PGN-127489 · Data length=DonÂt care · Timeout=1000 · Paged protocol={0x0F; 0} · Parameters={{Sequence; 4}; {Page; 0}; {Engine Intance; 16}; {Engine oil pressure; 24}; {Engine oil temp.; 40}; {Engine temp. Byte 0; 56}} · Module=OutBoard (Generic) · Module index=1
- Lit : `Engine Intance`, `Engine oil pressure`, `Engine oil temp.`, `Engine temp. Byte 0`, `PGN-127489`, `Page`, `Sequence`
- Utilisé par : `Engine Oil Pressure - 1`, `Engine temp - 1`
- Ligne export : 25920 · id 61178

#### Engine oil pressure  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127489-0`, `Engine Oil Pressure`
- Ligne export : 25955 · id 61179

#### Engine Oil Pressure  `MAC`
- Propriétés : Unit=kPa · Limiting object group=Signed
- Logique :
  - **Controlling** = `Engine oil pressure / 10`
- Lit : `Engine oil pressure`
- Utilisé par : `Engine Oil Pressure - 1`, `Engine Oil Pressure - 2`
- Ligne export : 25968 · id 61180

#### Engine temp. Byte 0  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `127489-0`, `Engine temp`
- Ligne export : 26012 · id 61188

#### 127489-1  `GFIN`
- Propriétés : Identifier=PGN-127489 · Data length=DonÂt care · Timeout=1000 · Paged protocol={0x0F; 1} · Parameters={{Sequence; 4}; {Page; 0}; {Engine temp. Byte 1; 8}; {Alternator potential; 16}; {Fuel rate; 32}; {Total engine hours - Byte 0; 48}} · Module=OutBoard (Generic) · Module index=2
- Lit : `Alternator potential`, `Engine temp. Byte 1`, `Fuel rate`, `PGN-127489`, `Page`, `Sequence`, `Total engine hours - Byte 0`
- Utilisé par : `Alternator - 1`, `Engine Hour - 1`, `Fuel rate - 1`
- Ligne export : 26024 · id 61391

#### Engine temp. Byte 1  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `127489-1`, `Engine temp`
- Ligne export : 26059 · id 61392

#### Engine temp  `MAC`
- Propriétés : Unit=Â°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `(((256 * Engine temp. Byte 1) + Engine temp. Byte 0) / 100) + -273,15`
- Lit : `C`, `Engine temp. Byte 0`, `Engine temp. Byte 1`
- Utilisé par : `Engine temp - 1`, `Engine temp - 2`
- Ligne export : 26071 · id 61189

#### Alternator potential  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127489-1`, `Alternator - 1`, `Alternator - 2`, `Alternator potential`
- Ligne export : 26142 · id 61395

#### Alternator potential  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `Alternator potential / 100`
- Lit : `Alternator potential`
- Utilisé par : `127489-1`, `Alternator - 1`, `Alternator - 2`
- Ligne export : 26155 · id 61200

#### Fuel rate  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127489-1`, `Fuel rate`, `Fuel rate - 1`, `Fuel rate - 2`
- Ligne export : 26199 · id 61396

#### Fuel rate  `MAC`
- Propriétés : Unit=L/h · Limiting object group=Signed
- Logique :
  - **Controlling** = `Fuel rate / 10`
- Lit : `Fuel rate`
- Utilisé par : `127489-1`, `Fuel rate - 1`, `Fuel rate - 2`
- Ligne export : 26212 · id 61208

#### Total engine hours - Byte 0  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127489-1`, `Engine Hour`
- Ligne export : 26256 · id 61397

#### 127489-2  `GFIN`
- Propriétés : Identifier=PGN-127489 · Data length=DonÂt care · Timeout=1000 · Paged protocol={0x0F; 2} · Parameters={{Total engine hours - Byte 1; 8}} · Module=OutBoard (Generic) · Module index=3
- Lit : `PGN-127489`, `Total engine hours - Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 26269 · id 61398

#### Total engine hours - Byte 1  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127489-2`, `Engine Hour`
- Ligne export : 26289 · id 61399

#### Engine Hour  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `((65536 * Total engine hours - Byte 1) + Total engine hours - Byte 0) / 3600`
- Lit : `Total engine hours - Byte 0`, `Total engine hours - Byte 1`
- Utilisé par : `Engine Hour - 1`, `Engine Hour - 2`
- Ligne export : 26302 · id 61216

#### Engine Intance  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=99999
- Utilisé par : `127489-0`, `Alternator - 1`, `Alternator - 2`, `Engine Hour - 1`, `Engine Hour - 2`, `Engine Oil Pressure - 1`, `Engine Oil Pressure - 2`, `Engine temp - 1`, `Engine temp - 2`, `Fuel rate - 1`, `Fuel rate - 2`
- Ligne export : 26364 · id 61226

#### Engine Oil Pressure - 1  `MEM`
- Propriétés : Input channel=Engine Oil Pressure [kPa] · Action=Replace · Store value=No · Reset value=0 · Function selector=Engine Brand
- Fonction *Mercury* :
  - **Activating** = `PositiveFlank((Engine Intance = 0))`
- Fonction *Yamaha* :
  - **Activating** = `PositiveFlank((Engine Intance = 0))`
- Fonction *COX* :
  - **Activating** = `Engine_Nmea AND 127489-0`
- Lit : `127489-0`, `Engine Brand`, `Engine Intance`, `Engine Oil Pressure`, `Engine_Nmea`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 26376 · id 61227

#### Engine temp - 1  `MEM`
- Propriétés : Input channel=Engine temp [Â°C] · Action=Replace · Store value=No · Reset value=0 · Function selector=Engine Brand
- Fonction *Mercury* :
  - **Activating** = `Engine Intance = 0`
- Fonction *Yamaha* :
  - **Activating** = `Engine Intance = 0`
- Fonction *COX* :
  - **Activating** = `Engine_Nmea AND 127489-0`
- Lit : `127489-0`, `Engine Brand`, `Engine Intance`, `Engine temp`, `Engine_Nmea`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 26509 · id 61236

#### Fuel rate - 1  `MEM`
- Propriétés : Input channel=Fuel rate [L/h] · Action=Replace · Store value=No · Reset value=0 · Function selector=Engine Brand
- Fonction *Mercury* :
  - **Activating** = `Engine Intance = 0`
- Fonction *Yamaha* :
  - **Activating** = `Engine Intance = 0`
- Fonction *COX* :
  - **Activating** = `Engine_Nmea AND 127489-1`
- Lit : `127489-1`, `Engine Brand`, `Engine Intance`, `Engine_Nmea`, `Fuel rate`
- Utilisé par : `Fuel Economy`, `MD4-10 page: OUTBOARD`
- Ligne export : 26626 · id 61244

#### Engine Hour - 1  `MEM`
- Propriétés : Input channel=Engine Hour [h] · Action=Replace · Store value=No · Reset value=0 · Function selector=Engine Brand
- Fonction *Mercury* :
  - **Activating** = `Engine Intance = 0`
- Fonction *Yamaha* :
  - **Activating** = `Engine Intance = 0`
- Fonction *COX* :
  - **Activating** = `Engine_Nmea AND 127489-1`
- Lit : `127489-1`, `Engine Brand`, `Engine Hour`, `Engine Intance`, `Engine_Nmea`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 26743 · id 61252

#### Engine Oil Pressure - 2  `MEM`
- Propriétés : Input channel=Engine Oil Pressure [kPa] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank((Engine Intance = 1))`
- Lit : `Engine Intance`, `Engine Oil Pressure`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 26860 · id 61260

#### Engine temp - 2  `MEM`
- Propriétés : Input channel=Engine temp [Â°C] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `Engine Intance = 1`
- Lit : `Engine Intance`, `Engine temp`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 26914 · id 61269

#### Fuel rate - 2  `MEM`
- Propriétés : Input channel=Fuel rate [L/h] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `Engine Intance = 1`
- Lit : `Engine Intance`, `Fuel rate`
- Utilisé par : `Fuel Economy`, `MD4-10 page: OUTBOARD`
- Ligne export : 26960 · id 61277

#### Engine Hour - 2  `MEM`
- Propriétés : Input channel=Engine Hour [h] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `Engine Intance = 1`
- Lit : `Engine Hour`, `Engine Intance`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 27006 · id 61285

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
- Ligne export : 27052 · id 61293

#### Fuel Tanks Selection  `SP`
- Propriétés : Input channel=None · Default state name=Tank 1 · States={Tank 2; Tank 1 and 2}
- Utilisé par : `Tank 1 - Show`, `Tank 2 - Show`, `Adjust group: Config Outboard`, `Single adjust item: Fuel Tanks Selection`
- Ligne export : 27079 · id 61314

#### Tank 1 - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Fuel Tanks Selection = 0) OR (Fuel Tanks Selection = 2)`
- Lit : `Fuel Tanks Selection`
- Utilisé par : `Fuel LOW`, `MD4-10 page: OUTBOARD`, `MD4-10 page: SHUTDOWN`
- Ligne export : 27092 · id 61317

#### Tank 2 - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Fuel Tanks Selection = 1) OR (Fuel Tanks Selection = 2)`
- Lit : `Fuel Tanks Selection`
- Utilisé par : `Fuel LOW`, `MD4-10 page: OUTBOARD`, `MD4-10 page: SHUTDOWN`
- Ligne export : 27146 · id 61326

#### Fuel LOW  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=500
- Logique :
  - **Activating** = `((Engine 1 - Tank - MEM [%] < 10) and Tank 1 - Show) OR ((Engine 2 - Tank - MEM [%] < 10) and Tank 2 - Show)`
- Lit : `Engine 1 - Tank - MEM`, `Engine 2 - Tank - MEM`, `Tank 1 - Show`, `Tank 2 - Show`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 27200 · id 61335

#### Alternator - 1  `MEM`
- Propriétés : Input channel=Alternator potential [V] · Action=Replace · Store value=No · Reset value=0 · Function selector=Engine Brand
- Fonction *Mercury* :
  - **Activating** = `PositiveFlank((Engine Intance = 0))`
- Fonction *Yamaha* :
  - **Activating** = `PositiveFlank((Engine Intance = 0))`
- Fonction *COX* :
  - **Activating** = `Engine_Nmea AND 127489-1`
- Lit : `127489-1`, `Alternator potential`, `Engine Brand`, `Engine Intance`, `Engine_Nmea`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 27272 · id 61354

#### Alternator - 2  `MEM`
- Propriétés : Input channel=Alternator potential [V] · Action=Replace · Store value=No · Reset value=0
- Logique :
  - **Activating** = `PositiveFlank((Engine Intance = 1))`
- Lit : `Alternator potential`, `Engine Intance`
- Utilisé par : `MD4-10 page: OUTBOARD`
- Ligne export : 27405 · id 61363

#### Mercury - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine Brand = 0`
- Lit : `Engine Brand`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 27459 · id 61372

#### Yamaha - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine Brand = 1`
- Lit : `Engine Brand`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 27504 · id 61380

#### Sequence  `GPIN`
- Propriétés : Length=4 bits · Type=Unsigned integer · Error value=0
- Utilisé par : `127489-0`, `127489-1`
- Ligne export : 27549 · id 61388

#### Page  `GPIN`
- Propriétés : Length=4 bits · Type=Unsigned integer · Error value=0
- Utilisé par : `127489-0`, `127489-1`
- Ligne export : 27561 · id 61389

#### Engine oil temp.  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `127489-0`
- Ligne export : 27573 · id 61390

#### Sequence  `GPIN`
- Propriétés : Length=4 bits · Type=Unsigned integer · Error value=0
- Utilisé par : `127489-0`, `127489-1`
- Ligne export : 27586 · id 61393

#### Page  `GPIN`
- Propriétés : Length=4 bits · Type=Unsigned integer · Error value=0
- Utilisé par : `127489-0`, `127489-1`
- Ligne export : 27598 · id 61394

#### Cox - Show  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine Brand = 2`
- Lit : `Engine Brand`
- Utilisé par : *(personne)*
- Ligne export : 27610 · id 85570
