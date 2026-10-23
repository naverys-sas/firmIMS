# MD4-CAB app — (racine appli)

169 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## (racine)

#### dtobin 2 APPIN c10  `APPIN`
- Propriétés : Input channel=infos for 45/10 dtobin 2 APPOUT · Error value=0
- Lit : `infos for 45/10 dtobin 2 APPOUT`
- Utilisé par : `btod2 c10`
- Ligne export : 103449 · id 223340

#### btod2 c10  `ARC`
- Propriétés : Array size=11 · Store value=No
- Logique :
  ```qcode
  This[0]:=dtobin 2 APPIN c10 mod 2
  This[1]:=(dtobin 2 APPIN c10 div 2) mod 2
  This[2]:=(dtobin 2 APPIN c10 div 4) mod 2
  This[3]:=(dtobin 2 APPIN c10 div 8) mod 2
  This[4]:=(dtobin 2 APPIN c10 div 16) mod 2
  This[5]:=(dtobin 2 APPIN c10 div 32) mod 2
  This[6]:=(dtobin 2 APPIN c10 div 64) mod 2
  This[7]:=(dtobin 2 APPIN c10 div 128) mod 2
  This[8]:=(dtobin 2 APPIN c10 div 256) mod 2
  This[9]:=(dtobin 2 APPIN c10 div 512) mod 2
  This[10]:=(dtobin 2 APPIN c10 div 1024) mod 2
  This[11]:=(dtobin 2 APPIN c10 div 2048) mod 2
  ```
- Lit : `dtobin 2 APPIN c10`
- Utilisé par : `Be1 Inter Buzzer for 45 c10`, `Be2 Main page IDC E c10`, `Be3 Main page IDC T c10`, `Be4 ShutDown page IDC c10`, `Be5 Startup page IDC c10`, `Be6 Engines READY for 45 c10`, `Be7 Safety_disable 45 sel c10`, `Be8 ALL ASK STOP c10`, `Be9 Reset safety to on 45 c10`, `be10 enabled ON/OFF T&E`, `be11 button drive 4ET 10`
- Ligne export : 103459 · id 223054

#### Be8 ALL ASK STOP c10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod2 c10[7]
  ```
- Lit : `btod2 c10`
- Utilisé par : `Start? Tracks md4 Button c10`
- Ligne export : 103492 · id 223087

#### Start? Tracks md4 Button c10  `VDIN`
- Propriétés : Toggle=Yes · Resetting channel=Be8 ALL ASK STOP c10 · Store value=No
- Lit : `Be8 ALL ASK STOP c10`
- Utilisé par : `Reset Free Button c10`, `trameb c10`, `MD4-10 page: MAIN`
- Ligne export : 103512 · id 217434

#### F3 Speed Fast c10  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `trameb c10`, `MD4-10 page: MAIN`
- Ligne export : 103523 · id 217592

#### F2 Speed Slow c10  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `trameb c10`, `MD4-10 page: MAIN`
- Ligne export : 103534 · id 217602

#### Reset Free Button c10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank(Start? Tracks md4 Button c10)`
- Lit : `Start? Tracks md4 Button c10`
- Utilisé par : `F4 Speed Free c10`
- Ligne export : 103545 · id 217767

#### F4 Speed Free c10  `VDIN`
- Propriétés : Toggle=Yes · Resetting channel=Reset Free Button c10 · Store value=No
- Lit : `Reset Free Button c10`
- Utilisé par : `trameb c10`, `MD4-10 page: MAIN`
- Ligne export : 103589 · id 217775

#### MDGN-Status:MD4 C  `MDGN`
- Propriétés : Value=Module status · Module=MD4-CAB-40 (MD4-10[2]) · Module index=0
- Utilisé par : `mdC10_State ok`
- Ligne export : 103600 · id 217797

#### Virtual DOWN c10  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10`, `MD4-10 page: MAIN`
- Ligne export : 103611 · id 217856

#### Virtual UP c10  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10`, `MD4-10 page: MAIN`
- Ligne export : 103621 · id 217857

#### Setup PIN  `PCC`
- Propriétés : Show message=All · Text=Setup PIN  · PIN code=1122
- Utilisé par : *(personne)*
- Ligne export : 103631 · id 218364

#### Iguana PIN  `PCC`
- Propriétés : Show message=All · Text=Iguana PIN  · PIN code=4158
- Utilisé par : *(personne)*
- Ligne export : 103668 · id 218371

#### Cancel Button c10  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `OFF Button c10`, `trameb c10`, `MD4-10 page: SHUTDOWN`
- Ligne export : 103705 · id 220112

#### OFF Button c10  `VDIN`
- Propriétés : Toggle=Yes · Resetting channel=Cancel Button c10 · Store value=No
- Lit : `Cancel Button c10`
- Utilisé par : `trameb c10`, `MD4-10 page: BASE`, `MD4-10 page: STARTUP PIN`
- Ligne export : 103715 · id 219420

#### Continue Button c10  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10`, `MD4-10 page: SHUTDOWN`
- Ligne export : 103726 · id 220415

#### +BAT:MD4-10  `MDGN`
- Propriétés : Value=Supply voltage [V] · Module=MD4-CAB-40 (MD4-10[2]) · Module index=4
- Utilisé par : `MD4-10 page: BASE`
- Ligne export : 103736 · id 220109

#### cProject version  `SIC`
- Propriétés : Value=Project version
- Lit : `Project version`
- Utilisé par : `MD4-10 page: INFO`, `MD4-10 page: SHUTDOWN`, `MD4-10 page: STARTUP PIN`
- Ligne export : 103747 · id 220445

#### dtobin 3 APPIN  `APPIN`
- Propriétés : Input channel=dtobin 3 APPOUT · Error value=0
- Lit : `dtobin 3 APPOUT`
- Utilisé par : `btod 3`
- Ligne export : 103756 · id 226312

#### btod 3  `ARC`
- Propriétés : Array size=10 · Store value=No
- Logique :
  ```qcode
  This[0]:=dtobin 3 APPIN mod 2
  This[1]:=(dtobin 3 APPIN div 2) mod 2
  This[2]:=(dtobin 3 APPIN div 4) mod 2
  This[3]:=(dtobin 3 APPIN div 8) mod 2
  This[4]:=(dtobin 3 APPIN div 16) mod 2
  This[5]:=(dtobin 3 APPIN div 32) mod 2
  This[6]:=(dtobin 3 APPIN div 64) mod 2
  This[7]:=(dtobin 3 APPIN div 128) mod 2
  This[8]:=(dtobin 3 APPIN div 256) mod 2
  ```
- Lit : `dtobin 3 APPIN`
- Utilisé par : `Be1 Ladder is not up`, `Be2 KTB K1 IDC - GPS_EQT`, `Be3 KTC K9 IDC - OutBoard On-OFF`, `Be4 Is multi button Eqt`, `Be5`, `Be6`, `Be7`, `Be8`
- Ligne export : 103766 · id 226263

#### Be2 KTB K1 IDC - GPS_EQT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 3[1]
  ```
- Lit : `btod 3`
- Utilisé par : `Adress Loose`
- Ligne export : 103798 · id 226321

#### Be3 KTC K9 IDC - OutBoard On-OFF  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 3[2]
  ```
- Lit : `btod 3`
- Utilisé par : `Adress Loose Auto`
- Ligne export : 103818 · id 226329

#### Be6 Engines READY for 45 c10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod2 c10[5]
  ```
- Lit : `btod2 c10`
- Utilisé par : `Gauge Page IDC`, `MD4-10 page: MAIN`
- Ligne export : 108120 · id 223399

#### Be9 Reset safety to on 45 c10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod2 c10[8]
  ```
- Lit : `btod2 c10`
- Utilisé par : `Safety off button c10`
- Ligne export : 108294 · id 223105

#### Safety off button c10  `VDIN`
- Propriétés : Toggle=No · Resetting channel=Be9 Reset safety to on 45 c10
- Lit : `Be9 Reset safety to on 45 c10`
- Utilisé par : `trameb c10`, `MD4-10 page: MAIN`
- Ligne export : 108314 · id 223113

#### Safety off button c10 reset  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10`, `MD4-10 page: MAIN`
- Ligne export : 108324 · id 223116

#### mdC10_State ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `MDGN-Status:MD4 C = 64`
- Lit : `MDGN-Status:MD4 C`
- Utilisé par : `trameb c10`
- Ligne export : 108334 · id 223118

#### Active display page C  `SIC`
> 1 main, 2 info
- Propriétés : Value=Active display page
- Utilisé par : `Info page on C10`, `Main page on C10_1`
- Ligne export : 108379 · id 223126

#### Info page on C10  `IDC`
> info active page 2, info bit 1
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Active display page C = 3`
  - **Blocking** = `(Active display page C = 1) OR (Active display page C = 2)`
- Lit : `Active display page C`
- Utilisé par : `trameb c10`
- Ligne export : 108388 · id 223127

#### trameb c10  `ARC`
- Propriétés : Array size=15 · Store value=No
- Logique :
  ```qcode
  This[0]:=Virtual UP c10*1
  This[1]:=Virtual DOWN c10*2
  This[2]:=Cancel Button c10*4
  This[3]:=F2 Speed Slow c10 *8
  This[4]:=F3 Speed Fast c10*16
  This[5]:=OFF Button c10*32
  This[6]:=Continue Button c10*64
  This[7]:=F4 Speed Free c10*128
  This[8]:=Start? Tracks md4 Button c10 *256
  This[9]:=Safety off button c10*512
  This[10]:=Safety off button c10 reset*1024
  This[11]:=mdC10_State ok*2048
  This[12]:=Info page on C10*4096
  This[13]:=F5 speed super slow C10*8192
  ```
- Lit : `12`, `13`, `Cancel Button c10`, `Continue Button c10`, `F2 Speed Slow c10`, `F3 Speed Fast c10`, `F4 Speed Free c10`, `F5 speed super slow C10`, `Info page on C10`, `OFF Button c10`, `Safety off button c10`, `Safety off button c10 reset`, `Start? Tracks md4 Button c10`, `Virtual DOWN c10`, `Virtual UP c10`, `mdC10_State ok`
- Utilisé par : `dtobin c10`
- Ligne export : 108451 · id 223137

#### dtobin c10  `MAC`
- Logique :
  ```qcode
  Result:=trameb c10[0]+trameb c10[1]+trameb c10[2]+trameb c10[3]+trameb c10[4]+trameb c10[5]+trameb c10[6]+trameb c10[7]+trameb c10[8]+trameb c10[9]+trameb c10[10]+trameb c10[11]+trameb c10[12]+trameb c10[13]
  ```
- Lit : `12`, `13`, `trameb c10`
- Utilisé par : `debug btod c10`, `dtobin APPOUT C10`
- Ligne export : 108485 · id 223170

#### debug btod c10  `ARC`
- Propriétés : Array size=15 · Store value=No
- Logique :
  ```qcode
  This[0]:=dtobin c10 mod 2
  This[1]:=(dtobin c10 div 2) mod 2
  This[2]:=(dtobin c10 div 4) mod 2
  This[3]:=(dtobin c10 div 8) mod 2
  This[4]:=(dtobin c10 div 16) mod 2
  This[5]:=(dtobin c10 div 32) mod 2
  This[6]:=(dtobin c10 div 64) mod 2
  This[7]:=(dtobin c10 div 128) mod 2
  This[8]:=(dtobin c10 div 256) mod 2
  This[9]:=(dtobin c10 div 512) mod 2
  This[10]:=(dtobin c10 div 1024) mod 2
  This[11]:=(dtobin c10 div 2048) mod 2
  This[12]:=(dtobin c10 div 4096) mod 2
  This[13]:=(dtobin c10 div 8192) mod 2
  ```
- Lit : `12`, `13`, `dtobin c10`
- Utilisé par : `debug B1 UP C10`, `debug B10 SAFETY OFF C10`, `debug B11 SAFETY OFF RESET C10`, `debug B12 45 State ok C10`, `debug B13 Info page on 45 C10`, `debug B14 F5 speed super slow C10`, `debug B2 DOWN C10`, `debug B3 CANCEL C10`, `debug B4 SLOW C10`, `debug B5 FAST C10`, `debug B6 OFF C10`, `debug B7 CONTINUE C10`, `debug B8 FREE C10`, `debug B9 START C10`
- Ligne export : 108503 · id 223202

#### debug B1 UP C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[0]
  ```
- Lit : `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 108538 · id 223247

#### debug B2 DOWN C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[1]
  ```
- Lit : `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 108558 · id 223255

#### debug B3 CANCEL C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[2]
  ```
- Lit : `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 108578 · id 223263

#### debug B4 SLOW C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[3]
  ```
- Lit : `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 108598 · id 223271

#### debug B5 FAST C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[4]
  ```
- Lit : `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 108618 · id 223279

#### debug B6 OFF C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[5]
  ```
- Lit : `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 108638 · id 223287

#### debug B7 CONTINUE C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[6]
  ```
- Lit : `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 108658 · id 223295

#### debug B8 FREE C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[7]
  ```
- Lit : `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 108678 · id 223303

#### debug B9 START C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[8]
  ```
- Lit : `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 108698 · id 223311

#### debug B10 SAFETY OFF C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[9]
  ```
- Lit : `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 108718 · id 223319

#### debug B11 SAFETY OFF RESET C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[10]
  ```
- Lit : `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 108738 · id 223327

#### dtobin APPOUT C10  `APPOUT`
- Propriétés : Input channel=dtobin c10 · Send method=On change · Transmit rate=1000
- Lit : `dtobin c10`
- Utilisé par : `dtob APPIN_1 c10`
- Ligne export : 108758 · id 223335

#### Be1 Inter Buzzer for 45 c10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod2 c10[0]
  ```
- Lit : `btod2 c10`
- Utilisé par : `Inter Buzzer CAB`
- Ligne export : 108769 · id 223341

#### debug B12 45 State ok C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[11]
  ```
- Lit : `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 108789 · id 223350

#### debug B13 Info page on 45 C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[12]
  ```
- Lit : `12`, `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 108809 · id 223358

#### Be2 Main page IDC E c10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod2 c10[1]
  ```
- Lit : `btod2 c10`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 108829 · id 223367

#### Be3 Main page IDC T c10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod2 c10[2]
  ```
- Lit : `btod2 c10`
- Utilisé par : *(personne)*
- Ligne export : 108849 · id 223375

#### Be4 ShutDown page IDC c10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod2 c10[3]
  ```
- Lit : `btod2 c10`
- Utilisé par : `MD4-10 page: SHUTDOWN`
- Ligne export : 108869 · id 223383

#### Be5 Startup page IDC c10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod2 c10[4]
  ```
- Lit : `btod2 c10`
- Utilisé par : `MD4-10 page: STARTUP PIN`
- Ligne export : 108889 · id 223391

#### Be7 Safety_disable 45 sel c10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod2 c10[6]
  ```
- Lit : `btod2 c10`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 108909 · id 223407

#### Joystick to zero APPIN  `APPIN`
- Propriétés : Input channel=Joystick to zero APPOUT
- Lit : `Joystick to zero APPOUT`
- Utilisé par : *(personne)*
- Ligne export : 108929 · id 223704

#### Be1 Ladder is not up  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 3[0]
  ```
- Lit : `btod 3`
- Utilisé par : `Ladder is not up - Buzz 1`
- Ligne export : 108938 · id 226313

#### Ladder is not up - Buzz 1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=150
- Logique :
  - **Activating** = `PositiveFlank(Be1 Ladder is not up)`
- Lit : `Be1 Ladder is not up`
- Utilisé par : `Inter Buzzer CAB`, `Wait Buz 1st`
- Ligne export : 108958 · id 218301

#### Wait Buz 1st  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=50
- Logique :
  - **Activating** = `NegativeFlank(Ladder is not up - Buzz 1)`
- Lit : `Ladder is not up - Buzz 1`
- Utilisé par : `Ladder is not up - Buzz 2`
- Ligne export : 109002 · id 218309

#### Ladder is not up - Buzz 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=150
- Logique :
  - **Activating** = `NegativeFlank(Wait Buz 1st)`
- Lit : `Wait Buz 1st`
- Utilisé par : `Inter Buzzer CAB`, `Wait Buz 2nd`
- Ligne export : 109046 · id 218317

#### Wait Buz 2nd  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=50
- Logique :
  - **Activating** = `NegativeFlank(Ladder is not up - Buzz 2)`
- Lit : `Ladder is not up - Buzz 2`
- Utilisé par : `Ladder is not up - Buzz 3`
- Ligne export : 109090 · id 218325

#### Ladder is not up - Buzz 3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=150
- Logique :
  - **Activating** = `NegativeFlank(Wait Buz 2nd)`
- Lit : `Wait Buz 2nd`
- Utilisé par : `Inter Buzzer CAB`
- Ligne export : 109134 · id 218333

#### Inter Buzzer CAB  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Ladder is not up - Buzz 1) OR (Ladder is not up - Buzz 2) OR (Ladder is not up - Buzz 3) OR (Be1 Inter Buzzer for 45 c10)`
- Lit : `Be1 Inter Buzzer for 45 c10`, `Ladder is not up - Buzz 1`, `Ladder is not up - Buzz 2`, `Ladder is not up - Buzz 3`
- Utilisé par : `ETC Buzzer C41 C2:3`
- Ligne export : 109178 · id 218349

#### ETC Buzzer C41 C2:3  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Inter Buzzer CAB · Module=MD4-CAB-40 (MD4-10[2]) · Module index=0
- Lit : `Inter Buzzer CAB`
- Utilisé par : *(personne)*
- Ligne export : 109242 · id 218363

#### C Button Cabine C41 C2:6  `DIN`
- Propriétés : Module=MD4-CAB-40 (MD4-10[2]) · Module index=3
- Utilisé par : `Button Cabine IDC`
- Ligne export : 109255 · id 218440

#### Button Cabine IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `C Button Cabine C41 C2:6`
- Lit : `C Button Cabine C41 C2:6`
- Utilisé par : `CABINE ON/OFF`, `trameb c10_1`
- Ligne export : 109265 · id 218441

#### DOOR  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Door IDC`, `MD4-10 page: BASE`
- Ligne export : 109308 · id 218982

#### C Button Door C41 C2:7  `DIN`
- Propriétés : Module=MD4-CAB-40 (MD4-10[2]) · Module index=4
- Utilisé par : `Door IDC`
- Ligne export : 109318 · id 218983

#### Door IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=10000
- Logique :
  - **Activating** = `PositiveFlank(DOOR) OR (PositiveFlank(C Button Door C41 C2:7))`
- Lit : `C Button Door C41 C2:7`, `DOOR`
- Utilisé par : `trameb c10_1`
- Ligne export : 109328 · id 218984

#### Main page on C10_1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Active display page C = 0`
  - **Blocking** = `(Active display page C = 1) OR (Active display page C = 2)`
- Lit : `Active display page C`
- Utilisé par : `trameb c10_1`
- Ligne export : 109380 · id 227193

#### Send new node KB  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10_1`, `MD4-10 page: SETUP`
- Ligne export : 109443 · id 219946

#### Reset KB  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10_1`, `MD4-10 page: SETUP`
- Ligne export : 109453 · id 220085

#### trameb c10_1  `ARC`
- Propriétés : Array size=15 · Store value=No
- Logique :
  ```qcode
  This[0]:=Button Cabine IDC*1
  This[1]:=Door IDC*2
  This[2]:=Main page on C10_1*4
  This[3]:=Send new node KB*8
  This[4]:=Reset KB*16
  This[5]:=0*32
  This[6]:=0*64
  This[7]:=0*128
  This[8]:=0 *256
  This[9]:=0*512
  This[10]:=0*1024
  This[11]:=0*2048
  This[12]:=0*4096
  ```
- Lit : `12`, `Button Cabine IDC`, `Door IDC`, `Main page on C10_1`, `Reset KB`, `Send new node KB`
- Utilisé par : `dtobin c10_1`
- Ligne export : 109463 · id 224575

#### dtobin c10_1  `MAC`
- Logique :
  ```qcode
  Result:=trameb c10_1[0]+trameb c10_1[1]+trameb c10_1[2]+trameb c10_1[3]+trameb c10_1[4]+trameb c10_1[5]+trameb c10_1[6]+trameb c10_1[7]+trameb c10_1[8]+trameb c10_1[9]+trameb c10_1[10]+trameb c10_1[11]+trameb c10_1[12]
  ```
- Lit : `12`, `trameb c10_1`
- Utilisé par : `debug btod c10_1`, `dtoni APPOUT C10_1`
- Ligne export : 109496 · id 224608

#### dtoni APPOUT C10_1  `APPOUT`
- Propriétés : Input channel=dtobin c10_1 · Send method=On change · Transmit rate=1000
- Lit : `dtobin c10_1`
- Utilisé par : `dtobin c10_1 APPIN`
- Ligne export : 109514 · id 224640

#### debug btod c10_1  `ARC`
- Propriétés : Array size=15 · Store value=No
- Logique :
  ```qcode
  This[0]:=dtobin c10_1 mod 2
  This[1]:=(dtobin c10_1 div 2) mod 2
  This[2]:=(dtobin c10_1 div 4) mod 2
  This[3]:=(dtobin c10_1 div 8) mod 2
  This[4]:=(dtobin c10_1 div 16) mod 2
  This[5]:=(dtobin c10_1 div 32) mod 2
  This[6]:=(dtobin c10_1 div 64) mod 2
  This[7]:=(dtobin c10_1 div 128) mod 2
  This[8]:=(dtobin c10_1 div 256) mod 2
  This[9]:=(dtobin c10_1 div 512) mod 2
  This[10]:=(dtobin c10_1 div 1024) mod 2
  This[11]:=(dtobin c10_1 div 2048) mod 2
  This[12]:=(dtobin c10_1 div 4096) mod 2
  ```
- Lit : `12`, `dtobin c10_1`
- Utilisé par : `debug B1 Button Cabine IDC C10`, `debug B10`, `debug B11`, `debug B12`, `debug B2 Door IDC C10`, `debug B3 Main page on C10_1`, `debug B4 KB Send new node`, `debug B5 KB Reset`, `debug B6`, `debug B7`, `debug B8`, `debug B9`
- Ligne export : 109525 · id 224648

#### debug B1 Button Cabine IDC C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10_1[0]
  ```
- Lit : `debug btod c10_1`
- Utilisé par : *(personne)*
- Ligne export : 109558 · id 224693

#### debug B2 Door IDC C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10_1[1]
  ```
- Lit : `debug btod c10_1`
- Utilisé par : *(personne)*
- Ligne export : 109578 · id 224701

#### debug B3 Main page on C10_1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10_1[2]
  ```
- Lit : `debug btod c10_1`
- Utilisé par : *(personne)*
- Ligne export : 109598 · id 224709

#### debug B4 KB Send new node  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10_1[3]
  ```
- Lit : `debug btod c10_1`
- Utilisé par : *(personne)*
- Ligne export : 109618 · id 224717

#### debug B5 KB Reset  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10_1[4]
  ```
- Lit : `debug btod c10_1`
- Utilisé par : *(personne)*
- Ligne export : 109638 · id 224725

#### debug B6  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10_1[5]
  ```
- Lit : `debug btod c10_1`
- Utilisé par : *(personne)*
- Ligne export : 109658 · id 224733

#### debug B7  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10_1[6]
  ```
- Lit : `debug btod c10_1`
- Utilisé par : *(personne)*
- Ligne export : 109678 · id 224741

#### debug B8  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10_1[7]
  ```
- Lit : `debug btod c10_1`
- Utilisé par : *(personne)*
- Ligne export : 109698 · id 224749

#### debug B9  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10_1[8]
  ```
- Lit : `debug btod c10_1`
- Utilisé par : *(personne)*
- Ligne export : 109718 · id 224757

#### debug B10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10_1[9]
  ```
- Lit : `debug btod c10_1`
- Utilisé par : *(personne)*
- Ligne export : 109738 · id 224765

#### debug B11  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10_1[10]
  ```
- Lit : `debug btod c10_1`
- Utilisé par : *(personne)*
- Ligne export : 109758 · id 224773

#### debug B12  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10_1[11]
  ```
- Lit : `debug btod c10_1`
- Utilisé par : *(personne)*
- Ligne export : 109778 · id 224781

#### Be8  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 3[7]
  ```
- Lit : `btod 3`
- Utilisé par : *(personne)*
- Ligne export : 109798 · id 226296

#### Be4 Is multi button Eqt  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 3[3]
  ```
- Lit : `btod 3`
- Utilisé par : `MD4-10 page: FEATURE`
- Ligne export : 109818 · id 226337

#### Be5  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 3[4]
  ```
- Lit : `btod 3`
- Utilisé par : *(personne)*
- Ligne export : 109838 · id 226345

#### Be6  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 3[5]
  ```
- Lit : `btod 3`
- Utilisé par : *(personne)*
- Ligne export : 109858 · id 226353

#### Be7  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod 3[6]
  ```
- Lit : `btod 3`
- Utilisé par : *(personne)*
- Ligne export : 109878 · id 226361

#### OutBoard Button  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `trameb c10_B_1`
- Ligne export : 109898 · id 218380

#### md4 GPS  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `trameb c10_B`, `MD4-10 page: FEATURE`
- Ligne export : 109909 · id 218381

#### md4 AUDIO  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `trameb c10_B`, `MD4-10 page: FEATURE`
- Ligne export : 109920 · id 218400

#### md4 AUX 4  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `trameb c10_B`, `MD4-10 page: FEATURE`
- Ligne export : 109931 · id 218401

#### md4 VHF  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `trameb c10_B`, `MD4-10 page: FEATURE`
- Ligne export : 109942 · id 218414

#### md4 AUX 5  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `trameb c10_B`, `MD4-10 page: FEATURE`
- Ligne export : 109953 · id 218415

#### SHOWER  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `trameb c10_B_1`, `MD4-10 page: FEATURE`
- Ligne export : 109964 · id 218439

#### CABINE ON/OFF  `VDIN`
- Propriétés : Toggle=Yes · Resetting channel=Button Cabine IDC · Store value=No
- Lit : `Button Cabine IDC`
- Utilisé par : `trameb c10_B`, `MD4-10 page: BASE`, `MD4-10 page: FEATURE`
- Ligne export : 109975 · id 218449

#### WIND CLEANER  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10_B_1`, `MD4-10 page: MAIN`, `MD4-10 page: OUTBOARD`
- Ligne export : 109986 · id 218474

#### Wipper Button  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10_B_1`, `MD4-10 page: MAIN`, `MD4-10 page: OUTBOARD`
- Ligne export : 109996 · id 218483

#### NAV + 360 LIGHT  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `trameb c10_B`, `MD4-10 page: FEATURE`
- Ligne export : 110006 · id 218552

#### LIGHT HT SPOT  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `trameb c10_B`, `MD4-10 page: FEATURE`
- Ligne export : 110017 · id 218606

#### LIGHT HT DIM  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `trameb c10_B`, `MD4-10 page: FEATURE`
- Ligne export : 110028 · id 218616

#### FAN WIND  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `trameb c10_B_1`, `MD4-10 page: FEATURE`
- Ligne export : 110039 · id 218642

#### Fridge  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `trameb c10_B`, `MD4-10 page: FEATURE`
- Ligne export : 110050 · id 218643

#### Search Light  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `trameb c10_B`, `MD4-10 page: FEATURE`
- Ligne export : 110061 · id 218653

#### LD UP - VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10_B`, `MD4-10 page: MAIN`
- Ligne export : 110072 · id 218654

#### LD DOWN - VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10_B`, `MD4-10 page: MAIN`
- Ligne export : 110082 · id 218680

#### LD UP - Force  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10_B_1`, `MD4-10 page: SETUP`
- Ligne export : 110092 · id 218746

#### LD DOWN - Force  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10_B_1`, `MD4-10 page: SETUP`
- Ligne export : 110102 · id 218781

#### AUX 2  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `md4 Aux 2 - Text`, `trameb c10_B_1`, `MD4-10 page: FEATURE`
- Ligne export : 110112 · id 218818

#### HT UP D  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10_B`, `MD4-10 page: MAIN`
- Ligne export : 110123 · id 218830

#### HT DOWN D  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10_B`, `MD4-10 page: MAIN`
- Ligne export : 110133 · id 218831

#### ANCHOR UP  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10_B_1`, `MD4-10 page: FEATURE`
- Ligne export : 110143 · id 218923

#### ANCHOR DOWN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10_B_1`, `MD4-10 page: FEATURE`
- Ligne export : 110153 · id 218924

#### AUX 1  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `md4 Aux 1 - Text`, `trameb c10_B_1`, `MD4-10 page: FEATURE`
- Ligne export : 110163 · id 218943

#### BILGE  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `trameb c10_B_1`, `MD4-10 page: FEATURE`
- Ligne export : 110174 · id 219001

#### md4 Seat position  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `trameb c10_B_1`, `MD4-10 page: BASE`
- Ligne export : 110185 · id 219027

#### Seat Power Force  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `trameb c10_B_1`, `MD4-10 page: SETUP`
- Ligne export : 110196 · id 219080

#### AUX 3  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `md4 Aux 3 - Text`, `trameb c10_B_1`, `MD4-10 page: FEATURE`
- Ligne export : 110207 · id 219206

#### trameb c10_B  `ARC`
- Propriétés : Array size=16 · Store value=No
- Logique :
  ```qcode
  This[0]:=LD UP - VDIN*1
  This[1]:=LD DOWN - VDIN*2
  This[2]:=HT UP D*4
  This[3]:=HT DOWN D*8
  This[4]:=md4 GPS*16
  This[5]:=md4 AUX 4*32
  This[6]:=md4 AUDIO*64
  This[7]:=md4 AUX 5*128
  This[8]:=md4 VHF*256
  This[9]:=CABINE ON/OFF*512
  This[10]:=NAV + 360 LIGHT*1024
  This[11]:=LIGHT HT SPOT*2048
  This[12]:=Search Light*4096
  This[13]:=Fridge*8192
  This[14]:=LIGHT HT DIM*16384
  ```
- Lit : `12`, `13`, `CABINE ON/OFF`, `Fridge`, `HT DOWN D`, `HT UP D`, `LD DOWN - VDIN`, `LD UP - VDIN`, `LIGHT HT DIM`, `LIGHT HT SPOT`, `NAV + 360 LIGHT`, `Search Light`, `md4 AUDIO`, `md4 AUX 4`, `md4 AUX 5`, `md4 GPS`, `md4 VHF`
- Utilisé par : `dtobin c10 B`
- Ligne export : 110218 · id 227208

#### dtobin c10 B  `MAC`
- Logique :
  ```qcode
  Result:=trameb c10_B[0]+trameb c10_B[1]+trameb c10_B[2]+trameb c10_B[3]+trameb c10_B[4]+trameb c10_B[5]+trameb c10_B[6]+trameb c10_B[7]+trameb c10_B[8]+trameb c10_B[9]+trameb c10_B[10]+trameb c10_B[11]+trameb c10_B[12]+trameb c10_B[13]+trameb c10_B[14]
  ```
- Lit : `12`, `13`, `trameb c10_B`
- Utilisé par : `debug btod c10 B`, `dtobin APPOUT C10 B`
- Ligne export : 110253 · id 227241

#### debug btod c10 B  `ARC`
- Propriétés : Array size=15 · Store value=No
- Logique :
  ```qcode
  This[0]:=dtobin c10 B mod 2
  This[1]:=(dtobin c10 B div 2) mod 2
  This[2]:=(dtobin c10 B div 4) mod 2
  This[3]:=(dtobin c10 B div 8) mod 2
  This[4]:=(dtobin c10 B div 16) mod 2
  This[5]:=(dtobin c10 B div 32) mod 2
  This[6]:=(dtobin c10 B div 64) mod 2
  This[7]:=(dtobin c10 B div 128) mod 2
  This[8]:=(dtobin c10 B div 256) mod 2
  This[9]:=(dtobin c10 B div 512) mod 2
  This[10]:=(dtobin c10 B div 1024) mod 2
  This[11]:=(dtobin c10 B div 2048) mod 2
  This[12]:=(dtobin c10 B div 4096) mod 2
  This[13]:=(dtobin c10 B div 8192) mod 2
  This[14]:=(dtobin c10 B div 16384) mod 2
  ```
- Lit : `12`, `13`, `dtobin c10 B`
- Utilisé par : `debug B1 LD UP - VDIN`, `debug B10 CABINE ON/OFF`, `debug B11 NAV + 360 LIGHT`, `debug B12 LIGHT HT SPOT`, `debug B13 Search Light`, `debug B14 Fridge`, `debug B15 LIGHT HT DIM`, `debug B2 LD DOWN - VDIN`, `debug B3 HT UP D`, `debug B4 HT DOWN D`, `debug B5 md4 GPS`, `debug B6 md4 AUX 4`, `debug B7 md4 AUDIO`, `debug B8 md4 AUX 5`, `debug B9 md4 VHF`
- Ligne export : 110271 · id 227273

#### debug B1 LD UP - VDIN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[0]
  ```
- Lit : `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110305 · id 227318

#### debug B2 LD DOWN - VDIN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[1]
  ```
- Lit : `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110325 · id 227326

#### debug B3 HT UP D  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[2]
  ```
- Lit : `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110345 · id 227334

#### debug B4 HT DOWN D  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[3]
  ```
- Lit : `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110365 · id 227342

#### debug B5 md4 GPS  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[4]
  ```
- Lit : `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110385 · id 227350

#### debug B6 md4 AUX 4  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[5]
  ```
- Lit : `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110405 · id 227358

#### debug B7 md4 AUDIO  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[6]
  ```
- Lit : `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110425 · id 227366

#### debug B8 md4 AUX 5  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[7]
  ```
- Lit : `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110445 · id 227374

#### debug B9 md4 VHF  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[8]
  ```
- Lit : `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110465 · id 227382

#### debug B10 CABINE ON/OFF  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[9]
  ```
- Lit : `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110485 · id 227390

#### debug B11 NAV + 360 LIGHT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[10]
  ```
- Lit : `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110505 · id 227398

#### dtobin APPOUT C10 B  `APPOUT`
- Propriétés : Input channel=dtobin c10 B · Send method=On change · Transmit rate=1000
- Lit : `dtobin c10 B`
- Utilisé par : `dtobin c10 B APPIN`
- Ligne export : 110525 · id 227406

#### debug B12 LIGHT HT SPOT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[11]
  ```
- Lit : `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110536 · id 227407

#### debug B13 Search Light  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[12]
  ```
- Lit : `12`, `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110556 · id 227415

#### debug B14 Fridge  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[13]
  ```
- Lit : `13`, `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110576 · id 227497

#### debug B15 LIGHT HT DIM  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B[14]
  ```
- Lit : `debug btod c10 B`
- Utilisé par : *(personne)*
- Ligne export : 110596 · id 227505

#### trameb c10_B_1  `ARC`
- Propriétés : Array size=16 · Store value=No
- Logique :
  ```qcode
  This[0]:=AUX 2*1
  This[1]:=LD UP - Force*2
  This[2]:=LD DOWN - Force*4
  This[3]:=ANCHOR UP*8
  This[4]:=ANCHOR DOWN*16
  This[5]:=AUX 1*32
  This[6]:=WIND CLEANER*64
  This[7]:=BILGE*128
  This[8]:=Seat Power Force*256
  This[9]:=OutBoard Button*512
  This[10]:=FAN WIND*1024
  This[11]:=AUX 3*2048
  This[12]:=Wipper Button*4096
  This[13]:=SHOWER*8192
  This[14]:=md4 Seat position*16384
  ```
- Lit : `12`, `13`, `ANCHOR DOWN`, `ANCHOR UP`, `AUX 1`, `AUX 2`, `AUX 3`, `BILGE`, `FAN WIND`, `LD DOWN - Force`, `LD UP - Force`, `OutBoard Button`, `SHOWER`, `Seat Power Force`, `WIND CLEANER`, `Wipper Button`, `md4 Seat position`
- Utilisé par : `dtobin c10 B_1`
- Ligne export : 110616 · id 227801

#### dtobin c10 B_1  `MAC`
- Logique :
  ```qcode
  Result:=trameb c10_B_1[0]+trameb c10_B_1[1]+trameb c10_B_1[2]+trameb c10_B_1[3]+trameb c10_B_1[4]+trameb c10_B_1[5]+trameb c10_B_1[6]+trameb c10_B_1[7]+trameb c10_B_1[8]+trameb c10_B_1[9]+trameb c10_B_1[10]+trameb c10_B_1[11]+trameb c10_B_1[12]+trameb c10_B_1[13]+trameb c10_B_1[14]
  ```
- Lit : `12`, `13`, `trameb c10_B_1`
- Utilisé par : `debug btod c10 B_1`, `dtobin APPOUT C10 B_1`
- Ligne export : 110651 · id 227842

#### debug btod c10 B_1  `ARC`
- Propriétés : Array size=15 · Store value=No
- Logique :
  ```qcode
  This[0]:=dtobin c10 B_1 mod 2
  This[1]:=(dtobin c10 B_1 div 2) mod 2
  This[2]:=(dtobin c10 B_1 div 4) mod 2
  This[3]:=(dtobin c10 B_1 div 8) mod 2
  This[4]:=(dtobin c10 B_1 div 16) mod 2
  This[5]:=(dtobin c10 B_1 div 32) mod 2
  This[6]:=(dtobin c10 B_1 div 64) mod 2
  This[7]:=(dtobin c10 B_1 div 128) mod 2
  This[8]:=(dtobin c10 B_1 div 256) mod 2
  This[9]:=(dtobin c10 B_1 div 512) mod 2
  This[10]:=(dtobin c10 B_1 div 1024) mod 2
  This[11]:=(dtobin c10 B_1 div 2048) mod 2
  This[12]:=(dtobin c10 B_1 div 4096) mod 2
  This[13]:=(dtobin c10 B_1 div 8192) mod 2
  This[14]:=(dtobin c10 B_1 div 16384) mod 2
  ```
- Lit : `12`, `13`, `dtobin c10 B_1`
- Utilisé par : `debug B10_1 OutBoard Button`, `debug B11_1 FAN WIND`, `debug B12_1 AUX 3`, `debug B13_1 Wipper Button`, `debug B14_1 SHOWER`, `debug B15_1 md4 Seat position`, `debug B1_1 AUX 2`, `debug B2_1 LD UP - Force`, `debug B3_1 LD DOWN - Force`, `debug B4_1 ANCHOR UP`, `debug B5_1 ANCHOR DOWN`, `debug B6_1 AUX 1`, `debug B7_1 WIND CLEANER`, `debug B8_1 BILGE`, `debug B9_1 Seat Power Force`
- Ligne export : 110669 · id 227874

#### debug B1_1 AUX 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[0]
  ```
- Lit : `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110706 · id 227919

#### debug B2_1 LD UP - Force  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[1]
  ```
- Lit : `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110726 · id 227927

#### debug B3_1 LD DOWN - Force  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[2]
  ```
- Lit : `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110746 · id 227935

#### debug B4_1 ANCHOR UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[3]
  ```
- Lit : `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110766 · id 227943

#### debug B5_1 ANCHOR DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[4]
  ```
- Lit : `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110786 · id 227951

#### debug B6_1 AUX 1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[5]
  ```
- Lit : `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110806 · id 227959

#### debug B7_1 WIND CLEANER  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[6]
  ```
- Lit : `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110826 · id 227967

#### debug B8_1 BILGE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[7]
  ```
- Lit : `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110846 · id 227975

#### debug B9_1 Seat Power Force  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[8]
  ```
- Lit : `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110866 · id 227983

#### debug B10_1 OutBoard Button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[9]
  ```
- Lit : `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110886 · id 227991

#### debug B11_1 FAN WIND  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[10]
  ```
- Lit : `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110906 · id 227999

#### dtobin APPOUT C10 B_1  `APPOUT`
- Propriétés : Input channel=dtobin c10 B_1 · Send method=On change · Transmit rate=1000
- Lit : `dtobin c10 B_1`
- Utilisé par : `dtobin c10 B_1 APPIN`
- Ligne export : 110926 · id 228007

#### debug B12_1 AUX 3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[11]
  ```
- Lit : `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110937 · id 228008

#### debug B13_1 Wipper Button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[12]
  ```
- Lit : `12`, `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110957 · id 228016

#### debug B14_1 SHOWER  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[13]
  ```
- Lit : `13`, `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110977 · id 228024

#### debug B15_1 md4 Seat position  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10 B_1[14]
  ```
- Lit : `debug btod c10 B_1`
- Utilisé par : *(personne)*
- Ligne export : 110997 · id 228032

#### Joystick plugged md10  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `Active le groupe: joystick md410`, `Adjust group: Master Config`, `Dual adjust item: Left Joystick C41 C2:1`, `Dual adjust item: Right Joystick C41 C2:2`, `Single adjust item: Joystick plugged md10`
- Ligne export : 111017 · id 232421

#### batt ok to start APPIN  `APPIN`
- Propriétés : Input channel=batt ok to start APPOUT
- Lit : `batt ok to start APPOUT`
- Utilisé par : `Be10 batt ok to start c10`
- Ligne export : 111116 · id 236417

#### Be10 batt ok to start c10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=batt ok to start APPIN
  ```
- Lit : `batt ok to start APPIN`
- Utilisé par : `MD4-10 page: MAIN`
- Ligne export : 111125 · id 233841

#### a/c option  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Adjust group: Master Features`, `MD4-10 page: FEATURE`, `Single adjust item: a/c option`, `Single adjust item: a/c option tyva`
- Ligne export : 111145 · id 234848

#### a/c option tyva  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `a/c option tyva APPOUT`, `tyva1 batt can nok D`, `Active le groupe: a/c tyva24v`, `Adjust group: Master Features`, `MD4-10 page: FEATURE`, `Single adjust item: a/c option tyva`
- Ligne export : 113852 · id 236456

#### a/c option tyva APPOUT  `APPOUT`
- Propriétés : Input channel=a/c option tyva · Send method=On change · Transmit rate=1000
- Lit : `a/c option tyva`
- Utilisé par : `a/c option tyva APPIN`
- Ligne export : 113865 · id 236462

#### Demisting option  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Adjust group: Master Features`, `MD4-10 page: FEATURE`, `Single adjust item: Demisting option`
- Ligne export : 113876 · id 236568

#### F5 speed super slow C10  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb c10`
- Ligne export : 113889 · id 240462

#### debug B14 F5 speed super slow C10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=debug btod c10[13]
  ```
- Lit : `13`, `debug btod c10`
- Utilisé par : *(personne)*
- Ligne export : 113899 · id 240508

#### be10 enabled ON/OFF T&E  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod2 c10[10]
  ```
- Lit : `btod2 c10`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 113919 · id 240698

#### be11 button drive 4ET 10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=btod2 c10[11]
  ```
- Lit : `btod2 c10`
- Utilisé par : *(personne)*
- Ligne export : 113939 · id 240957
