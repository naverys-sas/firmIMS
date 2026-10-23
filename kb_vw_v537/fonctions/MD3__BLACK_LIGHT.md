# MD3 — BLACK LIGHT

37 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## BLACK LIGHT

#### Time  `SIC`
- Propriétés : Value=Time
- Utilisé par : `Hour actual`, `Measure group: BlackLight`
- Ligne export : 7152 · id 18897

#### Hour actual  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `Time`
- Lit : ``, `Time`
- Utilisé par : `Backlight Value`
- Ligne export : 7161 · id 19168

#### Fuseau  `IP`
- Propriétés : Unit=h · Default mode={0}
- Utilisé par : `Couché night`, `Levé night`, `Méridian`, `Rise`, `Set`, `Adjust group: Backlight`, `Measure group: BlackLight`, `Single adjust item: Fuseau`
- Ligne export : 7203 · id 19191

#### Date  `SIC`
- Propriétés : Value=Date
- Utilisé par : `days since 2000`
- Ligne export : 7215 · id 18722

#### days since 2000  `IMAC`
- Logique :
  - **Controlling** = `Date - 36526`
- Lit : ``, `Date`
- Utilisé par : `Days in current year`, `Year since 2000`
- Ligne export : 7224 · id 18723

#### Year since 2000  `IMAC`
- Logique :
  - **Controlling** = `days since 2000 div 365`
- Lit : ``, `days since 2000`
- Utilisé par : `Days in current year`
- Ligne export : 7267 · id 18731

#### Days in current year  `IMAC`
- Logique :
  - **Controlling** = `(days since 2000 - (Year since 2000 * 365)) - (Year since 2000 div 4)`
- Lit : ``, `C`, `Year since 2000`, `days since 2000`
- Utilisé par : `L`, `M`
- Ligne export : 7310 · id 18748

#### M  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(Days in current year * 0,9856) + 356,8`
- Lit : ``, `Days in current year`
- Utilisé par : `C`
- Ligne export : 7380 · id 19196

#### C  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(((M * 2) sin ) * 0,02) + ((M sin ) * 1,9137)`
- Lit : ``, `M`
- Utilisé par : `Couché night`, `Days in current year`, `ECC1 Integrating limiting 2`, `ET`, `Engine Temperature`, `Ho`, `Ho night`, `Hot Water`, `Inlet / Exhaust conditions 1`, `Inter Allumage Thermique`, `L`, `Levé night`, `MDGN-Temp:MC2[1]`, `MDGN-Temp:MD3-0`, `Ok to move`, `Pre Fuel line ignition IDC`, `R`, `Rise`, `Set`, `Starter Protection CMSG`, `Stop Cruise`, `Timer sleep engine to Img`, `Voyant T° Eau Moteur Critical`, `Voyant T° Eau Moteur Warning`, `Water Temps`, `Measure group: Engine`, `Statistics log: System 1 Log`
- Ligne export : 7433 · id 19203

#### L  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = ``
- Lit : ``, `C`, `Days in current year`
- Utilisé par : `Dec`, `R`
- Ligne export : 7520 · id 19217

#### Dec  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `((L sin ) * 0,39774) asin `
- Lit : ``, `L`
- Utilisé par : `Ho`, `Ho night`
- Ligne export : 7582 · id 19273

#### Latitude (+ = North)  `FP`
- Propriétés : Unit=° · Default mode={0}
- Utilisé par : `Ho`, `Ho night`, `Adjust group: Backlight`, `Measure group: BlackLight`, `Single adjust item: Latitude (+ = North)`
- Ligne export : 7642 · id 19409

#### Ho  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `((-0,01454 - ((Dec sin ) * (Latitude (+ = North) [°] sin ))) / ((Dec cos ) * (Latitude (+ = North) [°] cos ))) acos `
- Lit : ``, `C`, `Dec`, `Latitude (+ = North)`
- Utilisé par : `Ho h`
- Ligne export : 7654 · id 19281

#### Ho h  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `Ho / 15`
- Lit : ``, `Ho`
- Utilisé par : `Rise`, `Set`
- Ligne export : 7765 · id 19311

#### Longitude (+ = East)  `FP`
- Propriétés : Unit=° · Default mode={0}
- Utilisé par : `Lon`, `Adjust group: Backlight`, `Measure group: BlackLight`, `Single adjust item: Longitude (+ = East)`
- Ligne export : 7809 · id 19411

#### Lon  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `Longitude (+ = East) [°] / -15`
- Lit : ``, `Longitude (+ = East)`
- Utilisé par : `Couché night`, `Levé night`, `Méridian`, `Rise`, `Set`
- Ligne export : 7821 · id 19324

#### R  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(((L * 4) sin ) * 0,053) + (((L * 2) sin ) * -2,4652)`
- Lit : ``, `C`, `L`
- Utilisé par : `ET`
- Ligne export : 7865 · id 19237

#### ET  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(C + R) * 4`
- Lit : ``, `C`, `R`
- Utilisé par : `ET h`
- Ligne export : 7961 · id 19267

#### ET h  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `ET / 60`
- Lit : ``, `ET`
- Utilisé par : `Couché night`, `Levé night`, `Méridian`, `Rise`, `Set`
- Ligne export : 8014 · id 19348

#### Rise  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `(((12 + ET h [h]) + Lon [h]) + Fuseau [h]) - Ho h [h]`
- Lit : ``, `C`, `ET h`, `Fuseau`, `Ho h`, `Lon`
- Utilisé par : `Backlight Value`, `Rise Hours`, `Rise minutes`
- Ligne export : 8058 · id 19302

#### Set  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `(((12 + ET h [h]) + Lon [h]) + Fuseau [h]) + Ho h [h]`
- Lit : ``, `C`, `ET h`, `Fuseau`, `Ho h`, `Lon`
- Utilisé par : `Backlight Value`, `CANOUT 102`, `Set Hours`, `Set minutes`
- Ligne export : 8129 · id 19379

#### Min black light  `IP`
- Propriétés : Unit=% · Default mode={7}
- Utilisé par : `Backlight Value`, `Adjust group: Backlight`, `Single adjust item: Min black light`
- Ligne export : 8200 · id 19496

#### Ho night  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(-0,105 - ((Dec sin ) * (Latitude (+ = North) [°] sin ))) / ((Dec cos ) * (Latitude (+ = North) [°] cos ))`
- Lit : ``, `C`, `Dec`, `Latitude (+ = North)`
- Utilisé par : `Ho night h`
- Ligne export : 8212 · id 19951

#### Ho night h  `MAC`
- Propriétés : Unit=h
- Logique :
  ```qcode
  if Ho night   > 1 or Ho night < -1 then
    Result := 12
  else
    Result := acos (Ho night) /15
  endif
  ```
- Lit : `Ho night`
- Utilisé par : `Couché night`, `Levé night`
- Ligne export : 8315 · id 19967

#### Levé night  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxOf(((((12 + ET h [h]) + Lon [h]) + Fuseau [h]) - Ho night h [h]), 1)`
- Lit : ``, `C`, `ET h`, `Fuseau`, `Ho night h`, `Lon`
- Utilisé par : `Backlight Value`
- Ligne export : 8337 · id 19975

#### Couché night  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `MinOf(((((12 + ET h [h]) + Lon [h]) + Fuseau [h]) + Ho night h [h]), 23)`
- Lit : ``, `C`, `ET h`, `Fuseau`, `Ho night h`, `Lon`
- Utilisé par : `Backlight Value`
- Ligne export : 8417 · id 19986

#### Backlight Value  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe(Hour actual [h]: {{Levé night [h]; Min black light [%]}; {Rise [h]; 100}; {Set [h]; 100}; {Couché night [h]; Min black light [%]}}, Freeze)`
- Lit : ``, `Couché night`, `Hour actual`, `Levé night`, `Min black light`, `Rise`, `Set`
- Utilisé par : `Backlight`
- Ligne export : 8497 · id 18512

#### MODE  `DP`
- Propriétés : True text=Auto · False text=Manual · Default mode={False}
- Utilisé par : `Backlight`, `Night mode`, `Adjust group: Backlight`, `Measure group: BlackLight`, `Single adjust item: Fuseau`, `Single adjust item: Latitude (+ = North)`, `Single adjust item: Longitude (+ = East)`, `Single adjust item: MODE`, `Single adjust item: Min black light`
- Ligne export : 8553 · id 20087

#### Backlight  `DCC`
- Propriétés : Type=Backlight · Input channel=Backlight Value [%] · Enabled=MODE
- Lit : `Backlight Value`, `MODE`
- Utilisé par : `Night mode`, `Measure group: BlackLight`
- Ligne export : 8566 · id 18511

#### Méridian  `MAC`
- Propriétés : Unit=h · Limiting object group=Signed
- Logique :
  - **Controlling** = `((12 + ET h [h]) + Lon [h]) + Fuseau [h]`
- Lit : ``, `ET h`, `Fuseau`, `Lon`
- Utilisé par : `Measure group: BlackLight`
- Ligne export : 8577 · id 19745

#### Night mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Backlight [%] < 100`
  - **Blocking** = `not(MODE)`
- Lit : ``, `Backlight`, `MODE`
- Utilisé par : `MD3 page: BASE`
- Ligne export : 8639 · id 20044

#### Rise Hours  `IMAC`
- Logique :
  ```qcode
  Result := (Rise * 3600) div 3600
  ```
- Lit : `Rise`
- Utilisé par : `Rise minutes`, `Sunrise`
- Ligne export : 8692 · id 21106

#### Rise minutes  `IMAC`
- Logique :
  ```qcode
  Result := ((Rise - Rise Hours) * 3600) div 60
  ```
- Lit : `Rise`, `Rise Hours`
- Utilisé par : `Sunrise`
- Ligne export : 8710 · id 21117

#### Sunrise  `TFC`
- Propriétés : Texts={{Rise Hours; Value; 0}; { : }; {Rise minutes; Value; 0}}
- Lit : ``, `Rise Hours`, `Rise minutes`
- Utilisé par : `Measure group: BlackLight`
- Ligne export : 8728 · id 21135

#### Set Hours  `IMAC`
- Logique :
  ```qcode
  Result := (Set * 3600) div 3600
  ```
- Lit : `Set`
- Utilisé par : `Set minutes`, `Sunset`
- Ligne export : 8748 · id 21160

#### Set minutes  `IMAC`
- Logique :
  ```qcode
  Result := ((Set - Set Hours) * 3600) div 60
  ```
- Lit : `Set`, `Set Hours`
- Utilisé par : `Sunset`
- Ligne export : 8766 · id 21171

#### Sunset  `TFC`
- Propriétés : Texts={{Set Hours; Value; 0}; { : }; {Set minutes; Value; 0}}
- Lit : ``, `Set Hours`, `Set minutes`
- Utilisé par : `Measure group: BlackLight`
- Ligne export : 8784 · id 21183
