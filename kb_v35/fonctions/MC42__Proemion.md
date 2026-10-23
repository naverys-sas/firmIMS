# MC42 — Proemion

23 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Proemion — actif seulement si `Proemion`

#### Drive Mode  `GPOUT`
- Propriétés : Input value=Battery DRIVE MODE · Length=1 bit · Type=Unsigned integer
- Lit : `Battery DRIVE MODE`
- Utilisé par : `Proemion Battery Value 1`
- Ligne export : 50226 · id 61723

#### Charger Charging  `GPOUT`
- Propriétés : Input value=Charger CHARGING · Length=1 bit · Type=Unsigned integer
- Lit : `Charger CHARGING`
- Utilisé par : `Proemion Battery Value 1`
- Ligne export : 50237 · id 61724

#### Battery SOC  `GPOUT`
- Propriétés : Input value=Battery SOC [%] · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Battery SOC`
- Utilisé par : `Proemion Battery Value 1`, `VIEW SOC`
- Ligne export : 50248 · id 61725

#### Battery Instant Voltage  `GPOUT`
- Propriétés : Input value=Battery InstantVoltage [V] · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Lit : `Battery InstantVoltage`
- Utilisé par : `Proemion Battery Value 1`
- Ligne export : 50259 · id 61726

#### Battery U Track  `GPOUT`
- Propriétés : Input value=BMS_U_Trac [V] · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Lit : `BMS_U_Trac`
- Utilisé par : `Proemion Battery Value 1`
- Ligne export : 50271 · id 61727

#### Iso Resist  `GPOUT`
- Propriétés : Input value=BMS_Iso_Resist [kOhm] · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `BMS_Iso_Resist`
- Utilisé par : `Proemion Battery Value 1`
- Ligne export : 50283 · id 61728

#### Wait after stating  `IDC`
- Propriétés : Toggle=No · Delay on=20000 · Delay off=0
- Logique :
  - **Activating** = `True`
- Lit : ``
- Utilisé par : `Trigger Timer`
- Ligne export : 50295 · id 62943

#### Trigger Timer  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=10
- Logique :
  - **Decreasing** = `Wait after stating`
  - **Resetting** = `Trigger Timer [min] <= 0`
- Lit : ``, `Wait after stating`
- Utilisé par : `Trigger`
- Ligne export : 50338 · id 62951

#### Trigger  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Trigger Timer [min] <= 0`
- Lit : ``, `Trigger Timer`
- Utilisé par : `Proemion Battery Value 1`, `Proemion Battery Value 2`, `Proemion Device`
- Ligne export : 50399 · id 62962

#### Proemion Battery Value 1  `GFOUT`
- Propriétés : Identifier=0x7451223 · Data length=8 · Send method=On trigger · Trigger=Trigger · Unused bits=Set to 0 · Parameters={{Drive Mode; 0}; {Charger Charging; 1}; {Battery SOC [%]; 8}; {Battery Instant Voltage [V]; 16}; {Battery U Track [V]; 32}; {Iso Resist [kOhm]; 48}} · Module=Proemion (Generic) · Module index=0
- Lit : `Battery Instant Voltage`, `Battery SOC`, `Battery U Track`, `Charger Charging`, `Drive Mode`, `Iso Resist`, `Trigger`
- Utilisé par : *(personne)*
- Ligne export : 50444 · id 61729

#### Current Bat  `GPOUT`
- Propriétés : Input value=Current Bat [A] · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Lit : `Current Bat`
- Utilisé par : `Proemion Battery Value 2`
- Ligne export : 50479 · id 61730

#### DiffCellVoltage  `GPOUT`
- Propriétés : Input value=DiffCellVoltage [mV] · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Lit : `DiffCellVoltage`
- Utilisé par : `Proemion Battery Value 2`
- Ligne export : 50491 · id 62829

#### Proemion Battery Value 2  `GFOUT`
- Propriétés : Identifier=0x7451224 · Data length=8 · Send method=On trigger · Trigger=Trigger · Unused bits=Set to 0 · Parameters={{Current Bat [A]; 0}; {DiffCellVoltage [mV]; 16}} · Module=Proemion (Generic) · Module index=1
- Lit : `Current Bat`, `DiffCellVoltage`, `Trigger`
- Utilisé par : *(personne)*
- Ligne export : 50503 · id 61731

#### Error 1  `GPOUT`
- Propriétés : Input value=Error 1 - MEM · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Error 1 - MEM`
- Utilisé par : `Proemion Secon Value`
- Ligne export : 50526 · id 61732

#### Error 2  `GPOUT`
- Propriétés : Input value=Error 2 - MEM · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Error 2 - MEM`
- Utilisé par : `Proemion Secon Value`
- Ligne export : 50538 · id 61733

#### Error 3  `GPOUT`
- Propriétés : Input value=Error 3 - MEM · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Error 3 - MEM`
- Utilisé par : `Proemion Secon Value`
- Ligne export : 50550 · id 61734

#### Proemion Secon Value  `GFOUT`
- Propriétés : Identifier=0x7451225 · Data length=8 · Send method=On change · Unused bits=Set to 0 · Parameters={{Error 1; 0}; {Error 2; 16}; {Error 3; 32}} · Module=Proemion (Generic) · Module index=2
- Lit : `Error 1`, `Error 2`, `Error 3`
- Utilisé par : *(personne)*
- Ligne export : 50562 · id 61735

#### GFIN-A:Generic  `GFIN`
- Propriétés : Identifier=0x7451220 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{Network State; 0}; {Signal Quality; 8}} · Module=Proemion (Generic) · Module index=0
- Lit : `Network State`, `Signal Quality`
- Utilisé par : *(personne)*
- Ligne export : 50587 · id 61736

#### Network State  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `Measure group: Proemion`
- Ligne export : 50609 · id 61737

#### Signal Quality  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `Measure group: Proemion`
- Ligne export : 50621 · id 61738

#### MDGN-+BAT:MC2[1]  `MAC`
- Propriétés : Unit=cV · Limiting object group=Signed
- Logique :
  - **Controlling** = `12V Batt. [V] * 100`
- Lit : ``, `12V Batt.`
- Utilisé par : `12V Batt.`
- Ligne export : 50633 · id 62988

#### 12V Batt.  `GPOUT`
- Propriétés : Input value=MDGN-+BAT:MC2[1] [cV] · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `MDGN-+BAT:MC2[1]`
- Utilisé par : `MDGN-+BAT:MC2[1]`, `Proemion Device`, `Measure group: System Monitoring`
- Ligne export : 50677 · id 61774

#### Proemion Device  `GFOUT`
- Propriétés : Identifier=0x7451230 · Data length=8 · Send method=On trigger · Trigger=Trigger · Unused bits=Set to 0 · Parameters={{12V Batt. [cV]; 0}} · Module=Proemion (Generic) · Module index=5
- Lit : `12V Batt.`, `Trigger`
- Utilisé par : *(personne)*
- Ligne export : 50689 · id 61775
