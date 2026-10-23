# MC42[1] application — Proemion

27 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Proemion — actif seulement si `Proemion Gateway`

#### Drive Mode  `GPOUT`
- Propriétés : Input value=Battery DRIVE MODE · Length=1 bit · Type=Unsigned integer
- Lit : `Battery DRIVE MODE`
- Utilisé par : `Proemion Battery Value 1`
- Ligne export : 68307 · id 84819

#### Charger Charging  `GPOUT`
- Propriétés : Input value=Charger CHARGING · Length=1 bit · Type=Unsigned integer
- Lit : `Charger CHARGING`
- Utilisé par : `Proemion Battery Value 1`
- Ligne export : 68318 · id 84826

#### Battery SOC  `GPOUT`
- Propriétés : Input value=Battery SOC [%] · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Battery SOC`
- Utilisé par : `Proemion Battery Value 1`, `SOC`, `MD4-10 page: INFO`, `Measure group: Battery Kreisel`
- Ligne export : 68329 · id 84828

#### Battery Instant Voltage  `GPOUT`
- Propriétés : Input value=Battery InstantVoltage [V] · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Lit : `Battery InstantVoltage`
- Utilisé par : `Proemion Battery Value 1`
- Ligne export : 68340 · id 84830

#### Battery U Track  `GPOUT`
- Propriétés : Input value=BMS_U_Trac [V] · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Lit : `BMS_U_Trac`
- Utilisé par : `Proemion Battery Value 1`
- Ligne export : 68352 · id 84832

#### Iso Resist  `GPOUT`
- Propriétés : Input value=BMS_Iso_Resist [kOhm] · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `BMS_Iso_Resist`
- Utilisé par : `Proemion Battery Value 1`
- Ligne export : 68364 · id 84834

#### Wait after starting  `IDC`
- Propriétés : Toggle=No · Delay on=20000 · Delay off=0
- Logique :
  - **Activating** = `True`
- Utilisé par : `Trigger Timer`
- Ligne export : 68376 · id 85109

#### Trigger Timer  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=10
- Logique :
  - **Decreasing** = `Wait after starting`
  - **Resetting** = `Trigger Timer [min] <= 0`
- Lit : `Wait after starting`
- Utilisé par : `Trigger`
- Ligne export : 68419 · id 85104

#### Trigger  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Trigger Timer [min] <= 0`
- Lit : `Trigger Timer`
- Utilisé par : `Proemion Battery Value 1`, `Proemion Battery Value 2`, `Proemion Device`
- Ligne export : 68480 · id 85116

#### Proemion Battery Value 1  `GFOUT`
- Propriétés : Identifier=0x7451223 · Data length=8 · Send method=On trigger · Trigger=Trigger · Unused bits=Set to 0 · Parameters={{Drive Mode; 0}; {Charger Charging; 1}; {Battery SOC [%]; 8}; {Battery Instant Voltage [V]; 16}; {Battery U Track [V]; 32}; {Iso Resist [kOhm]; 48}} · Module=Promeion (Generic) · Module index=0
- Lit : `Battery Instant Voltage`, `Battery SOC`, `Battery U Track`, `Charger Charging`, `Drive Mode`, `Iso Resist`, `Trigger`
- Utilisé par : *(personne)*
- Ligne export : 68525 · id 84818

#### Current Bat  `GPOUT`
- Propriétés : Input value=Current Bat [A] · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Lit : `Current Bat`
- Utilisé par : `Proemion Battery Value 2`, `Measure group: Battery Kreisel`
- Ligne export : 68560 · id 84836

#### DiffCellVoltage  `GPOUT`
- Propriétés : Input value=DiffCellVoltage [mV] · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian
- Lit : `DiffCellVoltage`
- Utilisé par : `Proemion Battery Value 2`
- Ligne export : 68572 · id 85072

#### Proemion Battery Value 2  `GFOUT`
- Propriétés : Identifier=0x7451224 · Data length=8 · Send method=On trigger · Trigger=Trigger · Unused bits=Set to 0 · Parameters={{Current Bat [A]; 0}; {DiffCellVoltage [mV]; 16}} · Module=Promeion (Generic) · Module index=1
- Lit : `Current Bat`, `DiffCellVoltage`, `Trigger`
- Utilisé par : *(personne)*
- Ligne export : 68584 · id 84839

#### Error 1  `GPOUT`
- Propriétés : Input value=Error 1 - MEM · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Error 1 - MEM`
- Utilisé par : `Proemion Secon Value`
- Ligne export : 68607 · id 84848

#### Error 2  `GPOUT`
- Propriétés : Input value=Error 2 - MEM · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Error 2 - MEM`
- Utilisé par : `Proemion Secon Value`
- Ligne export : 68619 · id 84849

#### Error 3  `GPOUT`
- Propriétés : Input value=Error 3 - MEM · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Error 3 - MEM`
- Utilisé par : `Proemion Secon Value`
- Ligne export : 68631 · id 84850

#### Proemion Secon Value  `GFOUT`
- Propriétés : Identifier=0x7451225 · Data length=8 · Send method=On change · Unused bits=Set to 0 · Parameters={{Error 1; 0}; {Error 2; 16}; {Error 3; 32}} · Module=Promeion (Generic) · Module index=2
- Lit : `Error 1`, `Error 2`, `Error 3`
- Utilisé par : *(personne)*
- Ligne export : 68643 · id 84854

#### GFIN-A:Generic  `GFIN`
- Propriétés : Identifier=0x7451220 · Data length=DonÂt care · Timeout=2000 · Paged protocol={Not used} · Parameters={{Network State; 0}; {Signal Quality; 8}} · Module=Promeion (Generic) · Module index=0
- Lit : `Network State`, `Signal Quality`
- Utilisé par : *(personne)*
- Ligne export : 68668 · id 84856

#### Network State  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `Measure group: Proemion`
- Ligne export : 68690 · id 84857

#### Signal Quality  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `Measure group: Proemion`
- Ligne export : 68702 · id 84859

#### Messages  `SP`
- Propriétés : Input channel=None · Default state name=None · States={Notify boat used tomorrow; Report an issue has arised}
- Utilisé par : `Message`, `Adjust group: Config Electric Drive`, `MD4-10 page: SERVICE`, `Single adjust item: Messages`
- Ligne export : 68714 · id 84927

#### Message  `GPOUT`
- Propriétés : Input value=Messages · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `Messages`
- Utilisé par : `Iqan Message`
- Ligne export : 68727 · id 84931

#### Send Message  `APPIN`
- Propriétés : Input channel=Send message
- Lit : `Send message`
- Utilisé par : `Iqan Message`
- Ligne export : 68739 · id 84955

#### Iqan Message  `GFOUT`
- Propriétés : Identifier=0x7451226 · Data length=8 · Send method=On trigger · Trigger=Send Message · Unused bits=Set to 0 · Parameters={{Message; 0}} · Module=Promeion (Generic) · Module index=3
- Lit : `Message`, `Send Message`
- Utilisé par : *(personne)*
- Ligne export : 68748 · id 84919

#### MDGN-+BAT:MC2[1]  `MAC`
- Propriétés : Unit=cV · Limiting object group=Signed
- Logique :
  - **Controlling** = `MDGN-+BAT:MC2[1] [V] * 100`
- Lit : `MDGN-+BAT:MC2[1]`
- Utilisé par : `MDGN-+BAT:MC2[1]`, `Proemion Device`
- Ligne export : 68768 · id 85148

#### MDGN-+BAT:MC2[1]  `GPOUT`
- Propriétés : Input value=MDGN-+BAT:MC2[1] [cV] · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `MDGN-+BAT:MC2[1]`
- Utilisé par : `MDGN-+BAT:MC2[1]`, `Proemion Device`
- Ligne export : 68812 · id 84977

#### Proemion Device  `GFOUT`
- Propriétés : Identifier=0x7451230 · Data length=8 · Send method=On trigger · Trigger=Trigger · Unused bits=Set to 0 · Parameters={{MDGN-+BAT:MC2[1] [cV]; 0}} · Module=Promeion (Generic) · Module index=4
- Lit : `MDGN-+BAT:MC2[1]`, `Trigger`
- Utilisé par : *(personne)*
- Ligne export : 68824 · id 84975
