# MC42 app — mc.Link MC42-Screens Logic ims

102 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## mc.Link MC42-Screens Logic ims

#### Batt or engine started mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(e System Started) OR (T Engine_Started mc)`
- Lit : `T Engine_Started mc`, `e System Started`
- Utilisé par : `Engines READY 45`, `Engines READY for 45`, `Engines started 2`
- Ligne export : 253 · id 208212

#### OK UP/DOWN Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(E OK UP/DOWN) OR (T OK UP/DOWN)`
- Lit : `E OK UP/DOWN`, `T OK UP/DOWN`
- Utilisé par : `UP/DOWN Choice`
- Ligne export : 303 · id 208227

#### Screen_Start/Stop mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `4ET Start Button`
- Lit : `4ET Start Button`
- Utilisé par : `MDs - Start Button Blocking Neutral E mc`, `T MD3 START`, `T MD3 STOP`, `T Port winter switch is off`, `e Joystick to zero CMSG mc`, `sim start engine`
- Ligne export : 353 · id 187048

#### dtob APPIN 45  `APPIN`
- Propriétés : Input channel=buttons 45 dtobin APPOUT · Error value=0
- Lit : `buttons 45 dtobin APPOUT`
- Utilisé par : `btod 45`
- Ligne export : 396 · id 213810

#### btod 45  `ARC`
- Propriétés : Array size=18 · Store value=No
- Logique :
  ```qcode
  This[0]:=dtob APPIN 45 mod 2
  This[1]:=(dtob APPIN 45 div 2) mod 2
  This[2]:=(dtob APPIN 45 div 4) mod 2
  This[3]:=(dtob APPIN 45 div 8) mod 2
  This[4]:=(dtob APPIN 45 div 16) mod 2
  This[5]:=(dtob APPIN 45 div 32) mod 2
  This[6]:=(dtob APPIN 45 div 64) mod 2
  This[7]:=(dtob APPIN 45 div 128) mod 2
  This[8]:=(dtob APPIN 45 div 256) mod 2
  This[9]:=(dtob APPIN 45 div 512) mod 2
  This[10]:=(dtob APPIN 45 div 1024) mod 2
  This[11]:=(dtob APPIN 45 div 2048) mod 2
  This[12]:=(dtob APPIN 45 div 4096) mod 2
  This[13]:=(dtob APPIN 45 div 8192) mod 2
  This[14]:=(dtob APPIN 45 div 16384) mod 2
  This[15]:=(dtob APPIN 45 div 32768) mod 2
  This[16]:=(dtob APPIN 45 div 65536) mod 2
  This[17]:=(dtob APPIN 45 div 131072) mod 2
  ```
- Lit : `12`, `13`, `dtob APPIN 45`
- Utilisé par : `B1 Virtual UP 4ET UP`, `B10 Safety off button 45 SAFETY OFF`, `B11 Safety off button 45 reset SAFETY OFF RESET`, `B12 md4-5_State ok`, `B13 Info page on 45`, `B14 10 hours certified`, `B15 1yr Maintenance`, `B16 2yrs Maintenance`, `B17 4yrs Maintenance`, `B18 Speed super slow 45`, `B2 Virtual DOWN 4ET DOWN`, `B3 Cancel Button 4ET CANCEL`, `B4 F2 Speed Slow SLOW`, `B5 F3 Speed Fast FAST`, `B6 OFF Button 4ET OFF`, `B7 Continue Button 4ET CONTINUE`, `B8 F4 Speed Free 4ET FREE`, `B9 Start Button 4ET START`
- Ligne export : 406 · id 213812

#### dtob APPIN_1 c10  `APPIN`
- Propriétés : Input channel=dtobin APPOUT C10 · Error value=0
- Lit : `dtobin APPOUT C10`
- Utilisé par : `btod c10`
- Ligne export : 445 · id 226795

#### btod c10  `ARC`
- Propriétés : Array size=17 · Store value=No
- Logique :
  ```qcode
  This[0]:=dtob APPIN_1 c10 mod 2
  This[1]:=(dtob APPIN_1 c10 div 2) mod 2
  This[2]:=(dtob APPIN_1 c10 div 4) mod 2
  This[3]:=(dtob APPIN_1 c10 div 8) mod 2
  This[4]:=(dtob APPIN_1 c10 div 16) mod 2
  This[5]:=(dtob APPIN_1 c10 div 32) mod 2
  This[6]:=(dtob APPIN_1 c10 div 64) mod 2
  This[7]:=(dtob APPIN_1 c10 div 128) mod 2
  This[8]:=(dtob APPIN_1 c10 div 256) mod 2
  This[9]:=(dtob APPIN_1 c10 div 512) mod 2
  This[10]:=(dtob APPIN_1 c10 div 1024) mod 2
  This[11]:=(dtob APPIN_1 c10 div 2048) mod 2
  This[12]:=(dtob APPIN_1 c10 div 4096) mod 2
  This[13]:=(dtob APPIN_1 c10 div 8192) mod 2
  ```
- Lit : `12`, `13`, `dtob APPIN_1 c10`
- Utilisé par : `B1 UP C10`, `B10 SAFETY OFF C10`, `B11 SAFETY OFF RESET C10`, `B12 45 State ok C10`, `B13 Info page on 45 C10`, `B14 F5 speed super slow C10`, `B2 DOWN C10`, `B3 CANCEL C10`, `B4 SLOW C10`, `B5 FAST C10`, `B6 OFF C10`, `B7 CONTINUE C10`, `B8 FREE C10`, `B9 START C10`
- Ligne export : 455 · id 226603

#### B12 45 State ok C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[11]
  ```
- Lit : `btod c10`
- Utilisé par : `B12 md4-5_State ok sel`
- Ligne export : 488 · id 226736

#### B12 md4-5_State ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[11]
  ```
- Lit : `btod 45`
- Utilisé par : `B12 md4-5_State ok sel`
- Ligne export : 508 · id 226797

#### B12 md4-5_State ok sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B12 md4-5_State ok) OR (B12 45 State ok C10)`
- Lit : `B12 45 State ok C10`, `B12 md4-5_State ok`
- Utilisé par : `Screen_State ok mc`
- Ligne export : 528 · id 216500

#### Screen_State ok mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B12 md4-5_State ok sel`
- Lit : `B12 md4-5_State ok sel`
- Utilisé par : `SCREEN OK`
- Ligne export : 578 · id 187078

#### B8 FREE C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[7]
  ```
- Lit : `btod c10`
- Utilisé par : `B8 F4 Speed Free 4ET FREE Sel`
- Ligne export : 621 · id 226704

#### B8 F4 Speed Free 4ET FREE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[7]
  ```
- Lit : `btod 45`
- Utilisé par : `B8 F4 Speed Free 4ET FREE Sel`
- Ligne export : 641 · id 226805

#### B8 F4 Speed Free 4ET FREE Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B8 F4 Speed Free 4ET FREE) OR (B8 FREE C10)`
- Lit : `B8 F4 Speed Free 4ET FREE`, `B8 FREE C10`
- Utilisé par : `Screen_F4 Input mc`, `Toggle Free 45M`
- Ligne export : 661 · id 213907

#### B9 START C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[8]
  ```
- Lit : `btod c10`
- Utilisé par : `Auto Light and Start broken need brightness`, `Auto Off - Timer`, `B9`, `KTB K11 IDC True- SearchLight`, `Ladder is not up`, `Trim Mode`
- Ligne export : 711 · id 226712

#### B9 Start Button 4ET START  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[8]
  ```
- Lit : `btod 45`
- Utilisé par : `B9`
- Ligne export : 731 · id 226813

#### B9 Start Button 4ET START Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B9 toggle`
- Lit : `B9 toggle`
- Utilisé par : `4ET Start Button`, `Auto Off - Timer 4ET`, `Reset Free Button 45M`, `Reset safety to on 45`, `Start Button 4ET bit`
- Ligne export : 751 · id 213915

#### Reset Free Button 45M  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank(B9 Start Button 4ET START Sel)`
- Lit : `B9 Start Button 4ET START Sel`
- Utilisé par : `Toggle Free 45M`
- Ligne export : 794 · id 214017

#### Toggle Free 45M  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(B8 F4 Speed Free 4ET FREE Sel)`
  - **Resetting** = `(Toggle Free 45M > 1) OR (Reset Free Button 45M)`
- Lit : `B8 F4 Speed Free 4ET FREE Sel`, `Reset Free Button 45M`
- Utilisé par : *(personne)*
- Ligne export : 838 · id 214025

#### IDC Speed Free m4ET  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Screen_F4 Input mc`
- Lit : `Screen_F4 Input mc`
- Utilisé par : `Screen_Free Input mc`
- Ligne export : 906 · id 214037

#### Screen_Free Input mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `IDC Speed Free m4ET`
- Lit : `IDC Speed Free m4ET`
- Utilisé par : `IDC Free E`, `IDC Free T`
- Ligne export : 949 · id 187161

#### Screen_F4 Input mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B8 F4 Speed Free 4ET FREE Sel`
- Lit : `B8 F4 Speed Free 4ET FREE Sel`
- Utilisé par : `IDC Speed Free m4ET`
- Ligne export : 992 · id 187186

#### Screen_State Up/Down mc  `IMAC`
- Logique :
  - **Controlling** = `State Up/Down 4ET [%]`
- Lit : `State Up/Down 4ET`
- Utilisé par : `State Up/Down Raw`, `State Up/Down Raw`, `T Bloc`
- Ligne export : 1035 · id 187286

#### MDs - Start Button Blocking Neutral E mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(MDs - Start Button Blocking Neutral E mc) OR (4ET Joystick Zero and (PositiveFlank(Screen_Start/Stop mc)))`
  - **Blocking** = `NegativeFlank(Screen_Start/Stop mc)`
- Lit : `4ET Joystick Zero`, `Screen_Start/Stop mc`
- Utilisé par : `BUTTON DRIVE 4ET`, `IMS Start Request E mc`, `System Shutdown`
- Ligne export : 1076 · id 128797

#### B1 UP C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[0]
  ```
- Lit : `btod c10`
- Utilisé par : `B1 Virtual UP 4ETUP sel`
- Ligne export : 1144 · id 226648

#### B1 Virtual UP 4ET UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[0]
  ```
- Lit : `btod 45`
- Utilisé par : `B1 Virtual UP 4ETUP sel`
- Ligne export : 1164 · id 226821

#### B1 Virtual UP 4ETUP sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B1 Virtual UP 4ET UP) OR (B1 UP C10) OR (up 20t)`
- Lit : `B1 UP C10`, `B1 Virtual UP 4ET UP`, `up 20t`
- Utilisé par : `DOWN Counter`, `Inter DOWN`, `Inter DOWN Delay`, `Inter UP`, `Inter UP Delay`, `UP`, `UP Counter`
- Ligne export : 1184 · id 213851

#### B2 DOWN C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[1]
  ```
- Lit : `btod c10`
- Utilisé par : `B2 Virtual DOWN 4ETDOWN sel`
- Ligne export : 1241 · id 226656

#### B2 Virtual DOWN 4ET DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[1]
  ```
- Lit : `btod 45`
- Utilisé par : `B2 Virtual DOWN 4ETDOWN sel`
- Ligne export : 1261 · id 226829

#### B2 Virtual DOWN 4ETDOWN sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B2 Virtual DOWN 4ET DOWN) OR (B2 DOWN C10) OR (not up 20t)`
- Lit : `B2 DOWN C10`, `B2 Virtual DOWN 4ET DOWN`, `not up 20t`
- Utilisé par : `DOWN`, `DOWN Counter`, `Inter DOWN`, `Inter DOWN Delay`, `Inter UP`, `Inter UP Delay`, `UP Counter`
- Ligne export : 1281 · id 213859

#### B3 CANCEL C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[2]
  ```
- Lit : `btod c10`
- Utilisé par : `B3 Cancel Button 4ET CANCEL Sel`
- Ligne export : 1338 · id 226664

#### B3 Cancel Button 4ET CANCEL  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[2]
  ```
- Lit : `btod 45`
- Utilisé par : `B3 Cancel Button 4ET CANCEL Sel`
- Ligne export : 1358 · id 226837

#### B3 Cancel Button 4ET CANCEL Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B3 Cancel Button 4ET CANCEL) OR (B3 CANCEL C10)`
- Lit : `B3 CANCEL C10`, `B3 Cancel Button 4ET CANCEL`
- Utilisé par : `Power Down State 4ET`, `eBoat State 4E`
- Ligne export : 1378 · id 213867

#### B4 SLOW C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[3]
  ```
- Lit : `btod c10`
- Utilisé par : `B4 F2 Speed Slow SLOW Sel`
- Ligne export : 1428 · id 226672

#### B4 F2 Speed Slow SLOW  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[3]
  ```
- Lit : `btod 45`
- Utilisé par : `B4 F2 Speed Slow SLOW Sel`
- Ligne export : 1448 · id 226845

#### B4 F2 Speed Slow SLOW Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B4 SLOW C10) OR (B4 F2 Speed Slow SLOW)`
- Lit : `B4 F2 Speed Slow SLOW`, `B4 SLOW C10`
- Utilisé par : `IDC Speed S`
- Ligne export : 1468 · id 213875

#### B5 FAST C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[4]
  ```
- Lit : `btod c10`
- Utilisé par : `B5 F3 Speed Fast FAST Sel`
- Ligne export : 1518 · id 226680

#### B5 F3 Speed Fast FAST  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[4]
  ```
- Lit : `btod 45`
- Utilisé par : `B5 F3 Speed Fast FAST Sel`
- Ligne export : 1538 · id 226853

#### B5 F3 Speed Fast FAST Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B5 F3 Speed Fast FAST) OR (B5 FAST C10)`
- Lit : `B5 F3 Speed Fast FAST`, `B5 FAST C10`
- Utilisé par : `IDC Speed Fast`
- Ligne export : 1558 · id 213883

#### B6 OFF C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[5]
  ```
- Lit : `btod c10`
- Utilisé par : `B6 OFF Button 4ET OFF Sel`, `Off Button - IDC`
- Ligne export : 1608 · id 226688

#### B6 OFF Button 4ET OFF  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[5]
  ```
- Lit : `btod 45`
- Utilisé par : `B6 OFF Button 4ET OFF Sel`
- Ligne export : 1628 · id 226861

#### B6 OFF Button 4ET OFF Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B6 OFF Button 4ET OFF) OR (B6 OFF C10)`
- Lit : `B6 OFF Button 4ET OFF`, `B6 OFF C10`
- Utilisé par : `F4 Off`, `Off Button - IDC 4ET`
- Ligne export : 1648 · id 213891

#### B7 CONTINUE C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[6]
  ```
- Lit : `btod c10`
- Utilisé par : `B7 Continue Button 4ET CONTINUE Sel`, `Charging State`, `Power Down State C10`
- Ligne export : 1698 · id 226696

#### B7 Continue Button 4ET CONTINUE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[6]
  ```
- Lit : `btod 45`
- Utilisé par : `B7 Continue Button 4ET CONTINUE Sel`
- Ligne export : 1718 · id 226869

#### B7 Continue Button 4ET CONTINUE Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B7 Continue Button 4ET CONTINUE) OR (B7 CONTINUE C10)`
- Lit : `B7 CONTINUE C10`, `B7 Continue Button 4ET CONTINUE`
- Utilisé par : `Continue 4ET`
- Ligne export : 1738 · id 213899

#### B10 SAFETY OFF C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[9]
  ```
- Lit : `btod c10`
- Utilisé par : `B10 Safety off button 45 SAFETY OFF Sel`
- Ligne export : 1788 · id 226720

#### B10 Safety off button 45 SAFETY OFF  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[9]
  ```
- Lit : `btod 45`
- Utilisé par : `B10 Safety off button 45 SAFETY OFF Sel`
- Ligne export : 1808 · id 226877

#### B10 Safety off button 45 SAFETY OFF Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B10 Safety off button 45 SAFETY OFF) OR (B10 SAFETY OFF C10)`
- Lit : `B10 SAFETY OFF C10`, `B10 Safety off button 45 SAFETY OFF`
- Utilisé par : `Reset safety to on 45`, `Safety_disable 45`
- Ligne export : 1828 · id 213923

#### B11 SAFETY OFF RESET C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[10]
  ```
- Lit : `btod c10`
- Utilisé par : `B11 Safety off button 45 reset SAFETY OFF RESET Sel`
- Ligne export : 1878 · id 226728

#### B11 Safety off button 45 reset SAFETY OFF RESET  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[10]
  ```
- Lit : `btod 45`
- Utilisé par : `B11 Safety off button 45 reset SAFETY OFF RESET Sel`
- Ligne export : 1898 · id 226885

#### B11 Safety off button 45 reset SAFETY OFF RESET Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B11 Safety off button 45 reset SAFETY OFF RESET) OR (B11 SAFETY OFF RESET C10)`
- Lit : `B11 SAFETY OFF RESET C10`, `B11 Safety off button 45 reset SAFETY OFF RESET`
- Utilisé par : `Reset safety to on 45`
- Ligne export : 1918 · id 213931

#### Right Joystick ET45 C2:2 APPIN  `APPIN`
- Propriétés : Input channel=Right Joystick ET45 CanOut [%] · Error value=0
- Lit : `Right Joystick ET45 CanOut`
- Utilisé par : `Right Joystick mc`
- Ligne export : 1968 · id 216210

#### Left Joy ET45 ou water level C2:1 APPIN  `APPIN`
- Propriétés : Input channel=Left Joystick ET45 CanOut [%] · Error value=0
- Lit : `Left Joystick ET45 CanOut`
- Utilisé par : `Left Joystick mc`
- Ligne export : 1978 · id 216211

#### B13 Info page on 45 C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[12]
  ```
- Lit : `12`, `btod c10`
- Utilisé par : `B13 Info page on 45 Sel`
- Ligne export : 1988 · id 226744

#### B13 Info page on 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[12]
  ```
- Lit : `12`, `btod 45`
- Utilisé par : `B13 Info page on 45 Sel`
- Ligne export : 2008 · id 226893

#### B13 Info page on 45 Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B13 Info page on 45) OR (B13 Info page on 45 C10)`
- Lit : `B13 Info page on 45`, `B13 Info page on 45 C10`
- Utilisé par : `Info page on`, `Main page on`
- Ligne export : 2028 · id 216561

#### Charger State Finite out mc  `APPOUT`
- Propriétés : Input channel=E.Charging State Machine · Send method=On change · Transmit rate=1000
- Lit : `E.Charging State Machine`
- Utilisé par : *(personne)*
- Ligne export : 2078 · id 223042

#### Battery DRIVE mc  `APPOUT`
- Propriétés : Input channel=Battery DRIVE MODE · Send method=On change · Transmit rate=1000
- Lit : `Battery DRIVE MODE`
- Utilisé par : *(personne)*
- Ligne export : 2089 · id 223043

#### TRACK DOWN 4ET APPOUT  `APPOUT`
- Propriétés : Input channel=TRACK DOWN 4ET · Send method=On change · Transmit rate=1000
- Lit : `TRACK DOWN 4ET`
- Utilisé par : *(personne)*
- Ligne export : 2100 · id 223701

#### Joystick to zero APPOUT  `APPOUT`
- Propriétés : Input channel=Joystick to zero · Send method=On change · Transmit rate=1000
- Lit : `Joystick to zero`
- Utilisé par : `Joystick to zero APPIN`
- Ligne export : 2111 · id 223703

#### Right Joystick C41 C2:2 APPIN  `APPIN`
- Propriétés : Input channel=Right Joystick C10 CanOut [%] · Error value=0
- Lit : `Right Joystick C10 CanOut`
- Utilisé par : `Right Joystick mc`
- Ligne export : 2122 · id 229041

#### Left Joystick C41 C2:1 APPIN  `APPIN`
- Propriétés : Input channel=Left Joystick C10 CanOut [%] · Error value=0
- Lit : `Left Joystick C10 CanOut`
- Utilisé par : `Left Joystick mc`
- Ligne export : 2132 · id 229043

#### Left Joystick mc  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(Left Joy ET45 ou water level C2:1 APPIN [%] + Left Joystick C41 C2:1 APPIN [%]) + Left Joystick mc 36 math`
- Lit : `Left Joy ET45 ou water level C2:1 APPIN`, `Left Joystick C41 C2:1 APPIN`, `Left Joystick mc 36 math`
- Utilisé par : `DMAC EV Pompe 2 Gauche`, `Left Joystick neg`
- Ligne export : 2142 · id 229045

#### Right Joystick mc  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `(Right Joystick ET45 C2:2 APPIN [%] + Right Joystick C41 C2:2 APPIN [%]) + Right Joystick mc 24 math`
- Lit : `Right Joystick C41 C2:2 APPIN`, `Right Joystick ET45 C2:2 APPIN`, `Right Joystick mc 24 math`
- Utilisé par : `DMAC EV Pompe 1 Droite`, `Right Joystick neg`
- Ligne export : 2195 · id 229053

#### Right Joystick neg  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `0 - Right Joystick mc`
- Lit : `Right Joystick mc`
- Utilisé par : *(personne)*
- Ligne export : 2760 · id 234734

#### Left Joystick neg  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `0 - Left Joystick mc`
- Lit : `Left Joystick mc`
- Utilisé par : *(personne)*
- Ligne export : 2804 · id 234739

#### up/down 20 times  `DP`
- Propriétés : True text=ON · False text=OFF · Default mode={False}
- Utilisé par : `not up 20t`, `up 20t`, `up/down 20t timer`, `Adjust group: Master Features`, `Single adjust item: up/down 20 times`
- Ligne export : 2848 · id 234752

#### up/down 20t timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=50
- Logique :
  - **Decreasing** = `up/down 20 times`
  - **Resetting** = `up/down 20t timer [s] = 0`
- Lit : `up/down 20 times`
- Utilisé par : `up 20t`
- Ligne export : 2861 · id 234753

#### up 20t  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `up/down 20t timer [s] > 35`
  - **Blocking** = `not(up/down 20 times)`
- Lit : `up/down 20 times`, `up/down 20t timer`
- Utilisé par : `B1 Virtual UP 4ETUP sel`, `not up 20t`
- Ligne export : 2922 · id 234764

#### not up 20t  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `(not(up 20t)) and up/down 20 times`
- Lit : `up 20t`, `up/down 20 times`
- Utilisé par : `B2 Virtual DOWN 4ETDOWN sel`
- Ligne export : 2975 · id 234792

#### B14 10 hours certified  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[13]
  ```
- Lit : `13`, `btod 45`
- Utilisé par : `B14 10 hours`
- Ligne export : 3028 · id 236917

#### B14 10 hours  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B14 10 hours certified`
- Lit : `B14 10 hours certified`
- Utilisé par : `r u sure 10 hours check`
- Ligne export : 3048 · id 237167

#### r u sure check 10 hours  `IMSG`
- Propriétés : Show message=All · Dialog type=Confirmation · Text=Are you sure? · Left button=No · Right button=Yes
- Utilisé par : *(personne)*
- Ligne export : 3091 · id 237222

#### B15 1yr Maintenance  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[14]
  ```
- Lit : `btod 45`
- Utilisé par : `B15 1yr`
- Ligne export : 3132 · id 238500

#### B16 2yrs Maintenance  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[15]
  ```
- Lit : `btod 45`
- Utilisé par : `B16 2yrs`
- Ligne export : 3152 · id 238512

#### B17 4yrs Maintenance  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[16]
  ```
- Lit : `btod 45`
- Utilisé par : `B17 4yrs`
- Ligne export : 3172 · id 238524

#### B15 1yr  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B15 1yr Maintenance`
- Lit : `B15 1yr Maintenance`
- Utilisé par : `RESET pin code`
- Ligne export : 3192 · id 238536

#### B16 2yrs  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B16 2yrs Maintenance`
- Lit : `B16 2yrs Maintenance`
- Utilisé par : `RESET pin code`
- Ligne export : 3235 · id 238548

#### B17 4yrs  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B17 4yrs Maintenance`
- Lit : `B17 4yrs Maintenance`
- Utilisé par : `RESET pin code`
- Ligne export : 3278 · id 238560

#### Rampe 0->100  `SFC`
- Propriétés : Input channel=Démarrage 0->100 · Enable=Yes · Type=Slopes · Slopes={{40; 200}; {0; 0}}
- Lit : `Démarrage 0->100`
- Utilisé par : `B9 toggle`, `MD4-5 page: BASE`
- Ligne export : 3321 · id 240315

#### Démarrage 0->100  `IP`
- Propriétés : Mode selector=Démarrage · Default mode: OFF={0} · Mode 1: demarrage={100}
- Lit : `Démarrage`
- Utilisé par : `Rampe 0->100`
- Ligne export : 3339 · id 240316

#### Démarrage  `SMC`
- Propriétés : Default state name=OFF
- Fonction *demarrage* :
  - **Activating** = `B9 wait`
- Lit : `B9 wait`
- Utilisé par : `Démarrage 0->100`
- Ligne export : 3353 · id 240326

#### B9  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B9 Start Button 4ET START) OR (B9 START C10)`
- Lit : `B9 START C10`, `B9 Start Button 4ET START`
- Utilisé par : `B9 show jauge OFF`, `B9 show jauge ON`, `B9 wait`
- Ligne export : 3393 · id 240371

#### B9 wait  `IDC`
- Propriétés : Toggle=No · Delay on=200 · Delay off=0
- Logique :
  - **Activating** = `B9`
- Lit : `B9`
- Utilisé par : `Démarrage`
- Ligne export : 3443 · id 240401

#### B9 toggle  `IDC`
- Propriétés : Toggle=Yes · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Rampe 0->100 >= 70`
  - **Blocking** = `ALL ASK STOP`
- Lit : `ALL ASK STOP`, `Rampe 0->100`
- Utilisé par : `B9 Start Button 4ET START Sel`, `B9 toggle wait`
- Ligne export : 3486 · id 240407

#### B9 show jauge ON  `IDC`
> permet de régler le timing d'affichage de la jauge de démarrage au bon moment
- Propriétés : Toggle=No · Delay on=100 · Delay off=500
- Logique :
  - **Activating** = `B9 AND (not(B9 toggle wait))`
- Lit : `B9`, `B9 toggle wait`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 3538 · id 240441

#### B18 Speed super slow 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 45[17]
  ```
- Lit : `btod 45`
- Utilisé par : `B18 F5 speed super slow Sel`
- Ligne export : 3589 · id 240485

#### B18 F5 speed super slow Sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(B18 Speed super slow 45) OR (B14 F5 speed super slow C10)`
- Lit : `B14 F5 speed super slow C10`, `B18 Speed super slow 45`
- Utilisé par : `IDC speed super slow`
- Ligne export : 3609 · id 240490

#### B14 F5 speed super slow C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod c10[13]
  ```
- Lit : `13`, `btod c10`
- Utilisé par : `B18 F5 speed super slow Sel`
- Ligne export : 3659 · id 240519

#### B9 show jauge OFF  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `B9 AND (B9 toggle wait)`
- Lit : `B9`, `B9 toggle wait`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 3679 · id 240967

#### B9 toggle wait  `IDC`
- Propriétés : Toggle=No · Delay on=3000 · Delay off=3000
- Logique :
  - **Activating** = `B9 toggle`
- Lit : `B9 toggle`
- Utilisé par : `B9 show jauge OFF`, `B9 show jauge ON`
- Ligne export : 3729 · id 240983

## mc.Link MC42-Screens Logic ims / joystick mc42

#### is_cab or joy_mc42  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `is_cab_mc OR (joystick plugged mc42)`
- Lit : `is_cab_mc`, `joystick plugged mc42`
- Utilisé par : `Active le groupe: mc.Link MC42-Screens Logic ims / joystick mc42 / level sensor cab or right joy`
- Ligne export : 2319 · id 232450

#### joystick plugged mc42  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `is_cab or joy_mc42`, `joy_mc42_and_not_cab`, `Active le groupe: mc.Link MC42-Screens Logic ims / joystick mc42 / left joystick x100 / left joystick x100`, `Adjust group: Master Config`, `Dual adjust item: Left Joystick mc 36`, `Dual adjust item: Right Joystick`, `Measure group: Translation`, `Single adjust item: joystick plugged mc42`
- Ligne export : 2596 · id 229344

#### joy_mc42_and_not_cab  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(joystick plugged mc42) AND is_x100_mc_s`
- Lit : `is_x100_mc_s`, `joystick plugged mc42`
- Utilisé par : `Active le groupe: mc.Link MC42-Screens Logic ims / joystick mc42 / disable math joy if not plugged mc42 and not cab`
- Ligne export : 2709 · id 235964

## mc.Link MC42-Screens Logic ims / joystick mc42 / disable math joy if not plugged mc42 and not cab — actif seulement si `joy_mc42_and_not_cab`

#### Right Joystick mc 24 math  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Low water level RJoy [%]`
- Lit : `Low water level RJoy`
- Utilisé par : `Right Joystick mc`
- Ligne export : 2624 · id 232426

#### Left Joystick mc 36 math  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Left Joystick mc 36 [%]`
- Lit : `Left Joystick mc 36`
- Utilisé par : `Left Joystick mc`
- Ligne export : 2666 · id 232431

## mc.Link MC42-Screens Logic ims / joystick mc42 / left joystick x100 / left joystick x100 — actif seulement si `joystick plugged mc42`

#### Left Joystick mc 36  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Calibration={500; 4500; -100; 100} · Alarms={No; 0; No; 100} · Module=MC42-33 (MC42[0]) · Module index=6
- Utilisé par : `Left Joystick mc 36 math`, `Adjust group: Master Tracks`, `Adjust group: Setup`, `Dual adjust item: Left Joystick mc 36`, `Measure group: Translation`
- Ligne export : 2293 · id 229332

## mc.Link MC42-Screens Logic ims / joystick mc42 / level sensor cab or right joy — actif seulement si `is_cab or joy_mc42`

#### Low water level RJoy  `VIN`
- Propriétés : Unit=% · Reference voltage=Reference voltage A · Error value=0 · Calibration={500; 4500; -100; 100} · Alarms={No; 0; No; 100} · Module=MC42-33 (MC42[0]) · Module index=3
- Utilisé par : `Right Joystick mc 24 math`, `level back to mV`, `water nok`, `Dual adjust item: Right Joystick`, `Measure group: Translation`
- Ligne export : 2384 · id 229331

#### level back to mV  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `courbe(Low water level RJoy [%]: {{-100; 500}; {100; 4500}}, Freeze)`
- Lit : `Low water level RJoy`
- Utilisé par : `level to p`
- Ligne export : 2408 · id 232500

#### level to p  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=water level state
- Fonction *Default state* :
  - **Controlling** = `courbe(level back to mV: {{550; 100}; {2450; 0}}, Freeze)`
- Fonction *error* :
  - **Controlling** = `False`
- Lit : `level back to mV`, `water level state`
- Utilisé par : `Water Level mc 24`
- Ligne export : 2458 · id 232505

#### water nok  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `Low water level RJoy [%] Status type = stError`
- Lit : `Low water level RJoy`
- Utilisé par : `water level state`
- Ligne export : 2539 · id 236466

#### water level state  `SP`
- Propriétés : Input channel=water nok · Default state name=Default state · States={error}
- Lit : `water nok`
- Utilisé par : `level to p`
- Ligne export : 2583 · id 236471
