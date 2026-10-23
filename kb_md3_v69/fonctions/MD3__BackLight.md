# MD3 — BackLight

66 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## BackLight

#### GPS Speed factor  `SP`
- Propriétés : Input channel=None · Default state name=m/s · States={kts}
- Utilisé par : `GPS_Factor`
- Ligne export : 6350 · id 34772

#### GPS_Factor  `IP`
- Propriétés : Mode selector=GPS Speed factor · Default mode: m/s={5144} · Mode 1: kts={10000}
- Lit : `GPS Speed factor`
- Utilisé par : `Speed Over Ground Kts`
- Ligne export : 6362 · id 34774

#### GPS_Adress  `IMAC`
- Logique :
  ```qcode
  result := Adresse_Mem
  ```
- Lit : `Adresse_Mem`
- Utilisé par : `PGN-129025`, `PGN-129026`, `PGN-129029`, `Measure group: BlackLight`
- Ligne export : 6376 · id 34831

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
- Ligne export : 6394 · id 34840

#### 129026-0  `GFIN`
- Propriétés : Identifier=PGN-129026 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Speed_Over_Ground_Raw; 32}} · Module=Garmin (Generic) · Module index=1
- Lit : `PGN-129026`, `Speed_Over_Ground_Raw`
- Utilisé par : `Garmin - NMEA`
- Ligne export : 6416 · id 34775

#### Garmin - NMEA  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `129026-0`
- Lit : ``, `129026-0`
- Utilisé par : `Adress Loose`, `Adress_Search`, `Measure group: BlackLight`, `Measure group: CanBus`
- Ligne export : 6435 · id 34776

#### Adress Loose  `IDC`
- Propriétés : Toggle=No · Delay on=120000 · Delay off=0
- Logique :
  - **Activating** = `not(Garmin - NMEA)`
- Lit : ``, `Garmin - NMEA`
- Utilisé par : `Adress_Search`
- Ligne export : 6478 · id 34784

#### Adress_Search  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Adress_Search OR (PositiveFlank(Adress Loose))`
  - **Blocking** = `PositiveFlank(Garmin - NMEA)`
- Lit : ``, `Adress Loose`, `Garmin - NMEA`
- Utilisé par : `Adresse_Mem`, `GPS Adresse Find`
- Ligne export : 6522 · id 34793

#### GPS Adresse Find  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Adress_Search`
  - **Resetting** = `GPS Adresse Find [s] > 256`
- Lit : ``, `Adress_Search`
- Utilisé par : `GPS_Adresse_Find_Int`
- Ligne export : 6581 · id 34803

#### GPS_Adresse_Find_Int  `IMAC`
- Logique :
  - **Controlling** = `GPS Adresse Find [s]`
- Lit : ``, `GPS Adresse Find`
- Utilisé par : `Adresse_Mem`
- Ligne export : 6642 · id 34814

#### Adresse_Mem  `MEM`
- Propriétés : Input channel=GPS_Adresse_Find_Int · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `Adress_Search AND DerivativeOf(GPS_Adresse_Find_Int)`
- Lit : ``, `Adress_Search`, `GPS_Adresse_Find_Int`
- Utilisé par : `GPS_Adress`
- Ligne export : 6683 · id 34822

#### Speed_Over_Ground_Raw  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `129026-0`, `Speed Over Ground Kts`
- Ligne export : 6735 · id 34859

#### Speed Over Ground Kts  `MAC`
- Propriétés : Unit=Kts
- Logique :
  ```qcode
  if Speed_Over_Ground_Raw < 65500 and GPS_Factor > 0 then
    Result:= (Speed_Over_Ground_Raw  /100) / (GPS_Factor / 10000)
  else
    Result:= 0
  endif
  ```
- Lit : `GPS_Factor`, `Speed_Over_Ground_Raw`
- Utilisé par : *(personne)*
- Ligne export : 6748 · id 34860

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
- Ligne export : 6770 · id 34876

#### 129029-0  `GFIN`
- Propriétés : Identifier=PGN-129029 · Data length=Dont care · Timeout=1000 · Paged protocol={0x0F; 0} · Parameters={{Current Date J; 24}; {Time_Byte_1_2_J; 40}; {Time_Byte_3; 56}} · Module=Garmin (Generic) · Module index=2
- Lit : `Current Date J`, `PGN-129029`, `Time_Byte_1_2_J`, `Time_Byte_3`
- Utilisé par : *(personne)*
- Ligne export : 6792 · id 34895

#### Time_Byte_1_2_J  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `129029-0`, `Current Time`
- Ligne export : 6818 · id 34896

#### Time_Byte_3  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `129029-0`, `Current Time`
- Ligne export : 6831 · id 34897

#### 129029-1  `GFIN`
- Propriétés : Identifier=PGN-129029 · Data length=Dont care · Timeout=1000 · Paged protocol={0x0F; 1} · Parameters={{Time_Byte_4; 8}} · Module=Garmin (Generic) · Module index=3
- Lit : `PGN-129029`, `Time_Byte_4`
- Utilisé par : *(personne)*
- Ligne export : 6843 · id 34898

#### Time_Byte_4  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `129029-1`, `Current Time`
- Ligne export : 6863 · id 34899

#### Current Time  `MAC`
- Propriétés : Unit=h
- Logique :
  ```qcode
  Result := ( (Time_Byte_1_2_J / 10000)  + (Time_Byte_3 * 255*255 / 10000) + (Time_Byte_4  * 255*255*255/10000) )/3600
  ```
- Lit : `Time_Byte_1_2_J`, `Time_Byte_3`, `Time_Byte_4`
- Utilisé par : `Time Diff`
- Ligne export : 6875 · id 34900

#### Time  `SIC`
- Propriétés : Value=Time
- Utilisé par : `Hour actual`, `Time Diff`
- Ligne export : 6893 · id 34920

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
- Ligne export : 6902 · id 34921

#### 129025-0  `GFIN`
- Propriétés : Identifier=PGN-129025 · Data length=Dont care · Timeout=1000 · Paged protocol={Not used} · Parameters={{Latitude G; 0}; {Longitude G; 32}} · Module=Garmin (Generic) · Module index=0
- Lit : `Latitude G`, `Longitude G`, `PGN-129025`
- Utilisé par : *(personne)*
- Ligne export : 6924 · id 34940

#### Latitude G  `GPIN`
- Propriétés : Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian · Error value=2000000000
- Utilisé par : `129025-0`, `Latitude Compute`
- Ligne export : 6946 · id 34941

#### Latitude Compute  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Latitude G * 1E-7`
- Lit : ``, `Latitude G`
- Utilisé par : `Latitude Compute MEN`, `Works Latitude`, `Measure group: BlackLight`
- Ligne export : 6959 · id 34942

#### Longitude G  `GPIN`
- Propriétés : Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Little-endian · Error value=2000000000
- Utilisé par : `129025-0`, `Longitude Compute`
- Ligne export : 7003 · id 34950

#### Longitude Compute  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Longitude G * 1E-7`
- Lit : ``, `Longitude G`
- Utilisé par : `Longitude Compute MEN`, `Works Latitude`, `Measure group: BlackLight`
- Ligne export : 7016 · id 34951

#### Works Latitude  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Latitude Compute <= 180) AND (Longitude Compute <= 180)`
- Lit : ``, `Latitude Compute`, `Longitude Compute`
- Utilisé par : `New Timer`
- Ligne export : 7060 · id 34959

#### New Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Works Latitude`
  - **Resetting** = `(New Timer [s] > 10) OR (NegativeFlank(Works Latitude))`
- Lit : ``, `Works Latitude`
- Utilisé par : `Current Date MEN`, `Latitude Compute MEN`, `Longitude Compute MEN`, `Time_Diff_MEM`
- Ligne export : 7114 · id 34968

#### Time Diff  `MAC`
- Logique :
  ```qcode
  Result := Time - Current Time
  ```
- Lit : `Current Time`, `Time`
- Utilisé par : `Time_Diff_MEM`
- Ligne export : 7183 · id 34980

#### Time_Diff_MEM  `MEM`
- Propriétés : Input channel=Time Diff · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `New Timer [s] >= 10`
- Lit : ``, `New Timer`, `Time Diff`
- Utilisé par : `Hour actual`
- Ligne export : 7201 · id 34990

#### Hour actual  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `Time - Time_Diff_MEM`
- Lit : ``, `Time`, `Time_Diff_MEM`
- Utilisé par : `Backlight Value`
- Ligne export : 7247 · id 34998

#### Fuseau  `IP`
- Propriétés : Unit=h · Default mode={0}
- Utilisé par : `Couché night`, `Levé night`, `Méridian`, `Sunrise`, `Sunset`
- Ligne export : 7291 · id 35006

#### Current Date J  `GPIN`
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `129029-0`, `Current Date MEN`
- Ligne export : 7303 · id 35007

#### Current Date MEN  `MEM`
- Propriétés : Input channel=Current Date J · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `New Timer [s] >= 10`
- Lit : ``, `Current Date J`, `New Timer`
- Utilisé par : `days since 2000`
- Ligne export : 7316 · id 35008

#### days since 2000  `IMAC`
- Logique :
  ```qcode
  Result := Current Date MEN - 10957
  ```
- Lit : `Current Date MEN`
- Utilisé par : `Days in current year`, `Year since 2000`
- Ligne export : 7362 · id 35016

#### Year since 2000  `IMAC`
- Logique :
  - **Controlling** = `days since 2000 div 365`
- Lit : ``, `days since 2000`
- Utilisé par : `Days in current year`
- Ligne export : 7380 · id 35026

#### Days in current year  `IMAC`
- Logique :
  - **Controlling** = `(days since 2000 - (Year since 2000 * 365)) - (Year since 2000 div 4)`
- Lit : ``, `C`, `Year since 2000`, `days since 2000`
- Utilisé par : `L`, `M`
- Ligne export : 7423 · id 35034

#### M  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(Days in current year * 0,9856) + 356,8`
- Lit : ``, `Days in current year`
- Utilisé par : `C`
- Ligne export : 7493 · id 35045

#### C  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(((M * 2) sin ) * 0,02) + ((M sin ) * 1,9137)`
- Lit : ``, `M`
- Utilisé par : `Couché night`, `Days in current year`, `ET`, `Engine Temperature EB 2`, `Engine Temperature Ford`, `Engine coolant temp`, `Ho`, `Ho_night`, `L`, `Levé night`, `MDGN-Temp:MD3-0`, `Ok to move`, `Pre Fuel line ignition IDC`, `R`, `Starter Protection CMSG`, `Stop Cruise`, `Sunrise`, `Sunset`, `Temp:MC42[1]`, `Timer sleep engine to Img`
- Ligne export : 7546 · id 35054

#### L  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = ``
- Lit : ``, `C`, `Days in current year`
- Utilisé par : `Dec`, `R`
- Ligne export : 7633 · id 35067

#### Dec  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `((L sin ) * 0,39774) asin `
- Lit : ``, `L`
- Utilisé par : `Ho`, `Ho_night`
- Ligne export : 7695 · id 35077

#### Latitude Compute MEN  `MEM`
- Propriétés : Input channel=Latitude Compute · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `New Timer [s] >= 10`
- Lit : ``, `Latitude Compute`, `New Timer`
- Utilisé par : `Ho`, `Ho_night`
- Ligne export : 7755 · id 35087

#### Ho  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(0,1 - ((Dec sin ) * (Latitude Compute MEN sin ))) / ((Dec cos ) * (Latitude Compute MEN cos ))`
- Lit : ``, `C`, `Dec`, `Latitude Compute MEN`
- Utilisé par : `Ho h`
- Ligne export : 7801 · id 35095

#### Ho h  `MAC`
- Propriétés : Unit=h
- Logique :
  ```qcode
  if Ho   > 1 or Ho < -1 then
    Result := 12
  else
    Result := acos (Ho) /15
  endif
  ```
- Lit : `Ho`
- Utilisé par : `Sunrise`, `Sunset`
- Ligne export : 7904 · id 35111

#### Longitude Compute MEN  `MEM`
- Propriétés : Input channel=Longitude Compute · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `New Timer [s] >= 10`
- Lit : ``, `Longitude Compute`, `New Timer`
- Utilisé par : `Lon`
- Ligne export : 7926 · id 35119

#### Lon  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `Longitude Compute MEN / -15`
- Lit : ``, `Longitude Compute MEN`
- Utilisé par : `Couché night`, `Levé night`, `Méridian`, `Sunrise`, `Sunset`
- Ligne export : 7972 · id 35127

#### R  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(((L * 4) sin ) * 0,053) + (((L * 2) sin ) * -2,4652)`
- Lit : ``, `C`, `L`
- Utilisé par : `ET`
- Ligne export : 8016 · id 35135

#### ET  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(C + R) * 4`
- Lit : ``, `C`, `R`
- Utilisé par : `ET h`
- Ligne export : 8112 · id 35149

#### ET h  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `ET / 60`
- Lit : ``, `ET`
- Utilisé par : `Couché night`, `Levé night`, `Méridian`, `Sunrise`, `Sunset`
- Ligne export : 8165 · id 35158

#### Sunset  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `(((12 + ET h [h]) + Lon [h]) + Fuseau [h]) - Ho h [h]`
- Lit : ``, `C`, `ET h`, `Fuseau`, `Ho h`, `Lon`
- Utilisé par : `Backlight Value`, `Duree`
- Ligne export : 8209 · id 35166

#### Sunrise  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `(((12 + ET h [h]) + Lon [h]) + Fuseau [h]) + Ho h [h]`
- Lit : ``, `C`, `ET h`, `Fuseau`, `Ho h`, `Lon`
- Utilisé par : `Backlight Value`, `Duree`
- Ligne export : 8280 · id 35177

#### Duree  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Sunrise [h] - Sunset [h]`
- Lit : ``, `Sunrise`, `Sunset`
- Utilisé par : *(personne)*
- Ligne export : 8351 · id 35188

#### Min back light  `IP`
- Propriétés : Unit=% · Default mode={20}
- Utilisé par : `Backlight Value`, `Adjust group: Backlight`, `Single adjust item: Min back light`
- Ligne export : 8395 · id 35196

#### Ho_night  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(-0,105 - ((Dec sin ) * (Latitude Compute MEN sin ))) / ((Dec cos ) * (Latitude Compute MEN cos ))`
- Lit : ``, `C`, `Dec`, `Latitude Compute MEN`
- Utilisé par : `Ho night h`
- Ligne export : 8407 · id 35197

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
- Utilisé par : `Couché night`, `Levé night`
- Ligne export : 8510 · id 35212

#### Levé night  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxOf(((((12 + ET h [h]) + Lon [h]) + Fuseau [h]) - Ho night h [h]), 0)`
- Lit : ``, `C`, `ET h`, `Fuseau`, `Ho night h`, `Lon`
- Utilisé par : `Backlight Value`, `Measure group: BlackLight`
- Ligne export : 8535 · id 35229

#### Couché night  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `MinOf(((((12 + ET h [h]) + Lon [h]) + Fuseau [h]) + Ho night h [h]), 24)`
- Lit : ``, `C`, `ET h`, `Fuseau`, `Ho night h`, `Lon`
- Utilisé par : `Backlight Value`, `Measure group: BlackLight`
- Ligne export : 8615 · id 35241

#### MODE  `DP`
- Propriétés : True text=AUTO (GPS) · False text=MANUAL · Default mode={False}
- Utilisé par : `Backlight`, `State`, `Adjust group: Backlight`, `Measure group: BlackLight`, `Single adjust item: MODE`
- Ligne export : 8695 · id 35253

#### Back light  `IP`
- Propriétés : Unit=% · Default mode={90}
- Utilisé par : `Backlight Value`, `Adjust group: Backlight`, `Single adjust item: Back light`
- Ligne export : 8708 · id 35254

#### Overdrive BackLight  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `State`, `MD3 page: BASE`, `MD3 page: PIN`
- Ligne export : 8720 · id 35557

#### State  `SMC`
- Propriétés : Default state name=Manuel
- Fonction *Auto* :
  - **Activating** = `MODE OR (not(Overdrive BackLight))`
- Lit : ``, `MODE`, `Overdrive BackLight`
- Utilisé par : `Backlight Value`, `In Engine Thermal State`, `In Exhaust Temp State`, `In Hydraulics Temp State`, `Speed All State`, `Up/DOWN STATE`
- Ligne export : 8731 · id 35572

#### Backlight Value  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed · Function selector=State
- Fonction *Manuel* :
  - **Controlling** = `Back light [%]`
- Fonction *Auto* :
  - **Controlling** = `lin(courbe(Hour actual [h]: {{Levé night [h]; Min back light [%]}; {Sunset [h]; 100}; {Sunrise [h]; 100}; {Couché night [h]; Min back light [%]}}, Freeze): Min back light [%]->Min back light [%], 100->100, Freeze)`
- Lit : ``, `Back light`, `Couché night`, `Hour actual`, `Levé night`, `Min back light`, `State`, `Sunrise`, `Sunset`
- Utilisé par : `Backlight`, `Backlight Value Filter`
- Ligne export : 8779 · id 35301

#### Méridian  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `((12 + ET h [h]) + Lon [h]) + Fuseau [h]`
- Lit : ``, `ET h`, `Fuseau`, `Lon`
- Utilisé par : `Measure group: BlackLight`
- Ligne export : 8878 · id 35330

#### Backlight Value Filter  `SFC`
- Propriétés : Input channel=Backlight Value [%] · Enable=Yes · Type=Slopes · Slopes={{50; 10}; {50; 50}}
- Lit : `Backlight Value`
- Utilisé par : *(personne)*
- Ligne export : 8940 · id 35366

#### Backlight  `DCC`
- Propriétés : Type=Backlight · Input channel=Backlight Value [%] · Enabled=MODE
- Lit : `Backlight Value`, `MODE`
- Utilisé par : *(personne)*
- Ligne export : 8958 · id 35556
