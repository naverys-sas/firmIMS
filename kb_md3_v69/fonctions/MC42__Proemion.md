# MC42 — Proemion

9 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Proemion — actif seulement si `Proemion`

#### Wait after stating  `IDC`
- Propriétés : Toggle=No · Delay on=20000 · Delay off=0
- Logique :
  - **Activating** = `True`
- Lit : ``
- Utilisé par : `Trigger Timer`
- Ligne export : 26847 · id 62943

#### Trigger Timer  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=10
- Logique :
  - **Decreasing** = `Wait after stating`
  - **Resetting** = `Trigger Timer [min] <= 0`
- Lit : ``, `Wait after stating`
- Utilisé par : `Trigger`
- Ligne export : 26890 · id 62951

#### Trigger  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Trigger Timer [min] <= 0`
- Lit : ``, `Trigger Timer`
- Utilisé par : `Proemion Device`
- Ligne export : 26951 · id 62962

#### GFIN-A:Generic  `GFIN`
- Propriétés : Identifier=0x7451220 · Data length=Dont care · Timeout=2000 · Paged protocol={Not used} · Parameters={{Network State; 0}; {Signal Quality; 8}} · Module=Proemion (Generic) · Module index=0
- Lit : `Network State`, `Signal Quality`
- Utilisé par : *(personne)*
- Ligne export : 26996 · id 61736

#### Network State  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `Measure group: Proemion`
- Ligne export : 27018 · id 61737

#### Signal Quality  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-A:Generic`, `Measure group: Proemion`
- Ligne export : 27030 · id 61738

#### MDGN-+BAT:MC2[1]  `MAC`
- Propriétés : Unit=cV · Limiting object group=Signed
- Logique :
  - **Controlling** = `12V Batt. [V] * 100`
- Lit : ``, `12V Batt.`
- Utilisé par : `3`
- Ligne export : 27042 · id 62988

#### 3  `GPOUT`
- Propriétés : Input value=MDGN-+BAT:MC2[1] [cV] · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `MDGN-+BAT:MC2[1]`
- Utilisé par : *(personne)*
- Ligne export : 27086 · id 61774

#### Proemion Device  `GFOUT`
- Propriétés : Identifier=0x7451230 · Data length=8 · Send method=On trigger · Trigger=Trigger · Unused bits=Set to 0 · Parameters={{3 [cV]; 0}} · Module=Proemion (Generic) · Module index=5
- Lit : `Trigger`
- Utilisé par : *(personne)*
- Ligne export : 27098 · id 61775
