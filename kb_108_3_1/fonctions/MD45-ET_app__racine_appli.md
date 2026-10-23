# MD45-ET app — (racine appli)

64 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## (racine)

#### Cancel Button 45  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `OFF Button 45`, `trameb buttons 45`, `MD4-5 page: SHUTDOWN`
- Ligne export : 116887 · id 201449

#### Continue Button 45  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb buttons 45`, `MD4-5 page: SHUTDOWN`
- Ligne export : 116897 · id 201510

#### OFF Button 45  `VDIN`
> reset by Cancel Button 45
- Propriétés : Toggle=Yes · Resetting channel=Cancel Button 45 · Store value=No
- Lit : `Cancel Button 45`
- Utilisé par : `trameb buttons 45`, `MD4-5 page: brokenSTARTUP PIN`
- Ligne export : 116907 · id 201412

#### Virtual DOWN 45  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb buttons 45`, `MD4-5 page: BASE`
- Ligne export : 116918 · id 180851

#### Virtual UP 45  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb buttons 45`, `MD4-5 page: BASE`
- Ligne export : 116928 · id 180852

#### info from mc dtobin 2 APPIN  `APPIN`
- Propriétés : Input channel=infos for 45/10 dtobin 2 APPOUT · Error value=0
- Lit : `infos for 45/10 dtobin 2 APPOUT`
- Utilisé par : `info from mc bintod 2`
- Ligne export : 116938 · id 217091

#### info from mc bintod 2  `ARC`
- Propriétés : Array size=12 · Store value=No
- Logique :
  ```qcode
  This[0]:=info from mc dtobin 2 APPIN mod 2
  This[1]:=(info from mc dtobin 2 APPIN div 2) mod 2
  This[2]:=(info from mc dtobin 2 APPIN div 4) mod 2
  This[3]:=(info from mc dtobin 2 APPIN div 8) mod 2
  This[4]:=(info from mc dtobin 2 APPIN div 16) mod 2
  This[5]:=(info from mc dtobin 2 APPIN div 32) mod 2
  This[6]:=(info from mc dtobin 2 APPIN div 64) mod 2
  This[7]:=(info from mc dtobin 2 APPIN div 128) mod 2
  This[8]:=(info from mc dtobin 2 APPIN div 256) mod 2
  This[9]:=(info from mc dtobin 2 APPIN div 512) mod 2
  This[10]:=(info from mc dtobin 2 APPIN div 1024) mod 2
  This[11]:=(info from mc dtobin 2 APPIN div 2048) mod 2
  ```
- Lit : `info from mc dtobin 2 APPIN`
- Utilisé par : `Be1 Inter Buzzer for 45`, `Be2 Main page IDC E`, `Be3 Main page IDC T`, `Be4 ShutDown page IDC`, `Be5 Startup page IDC`, `Be6 Engines READY for 45`, `Be7 Safety_disable 45 sel`, `Be8 ALL ASK STOP`, `Be9 Reset safety to on 45`, `be10 enabled ON/OFF T&E`, `be11 button drive 4ET 45/10`
- Ligne export : 116948 · id 216983

#### Be8 ALL ASK STOP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=info from mc bintod 2[7]
  ```
- Lit : `info from mc bintod 2`
- Utilisé par : *(personne)*
- Ligne export : 116979 · id 217165

#### Start Button 4ET  `VDIN`
> Reset Be8 ALL ASK STOP
- Propriétés : Toggle=No
- Utilisé par : `Reset Free Button 45`, `trameb buttons 45`, `MD4-5 page: BASE`
- Ligne export : 116999 · id 180447

#### Reset Free Button 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank(Start Button 4ET)`
- Lit : `Start Button 4ET`
- Utilisé par : `F4 Speed Free 45`
- Ligne export : 117009 · id 180780

#### F4 Speed Free 45  `VDIN`
> reset by Reset Free Button 45
- Propriétés : Toggle=No · Resetting channel=Reset Free Button 45
- Lit : `Reset Free Button 45`
- Utilisé par : `trameb buttons 45`, `MD4-5 page: BASE`
- Ligne export : 117053 · id 180788

#### Be9 Reset safety to on 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=info from mc bintod 2[8]
  ```
- Lit : `info from mc bintod 2`
- Utilisé par : `Safety off button 45`
- Ligne export : 117063 · id 217173

#### Safety off button 45  `VDIN`
> Reset by Be9 Reset safety to on 45
- Propriétés : Toggle=No · Resetting channel=Be9 Reset safety to on 45
- Lit : `Be9 Reset safety to on 45`
- Utilisé par : `trameb buttons 45`, `MD4-5 page: BASE`
- Ligne export : 117083 · id 210195

#### F3 Speed Fast 45  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb buttons 45`, `MD4-5 page: BASE`
- Ligne export : 117093 · id 180605

#### F2 Speed Slow 45  `VDIN`
> Slow = normal sur le md4
- Propriétés : Toggle=No
- Utilisé par : `trameb buttons 45`, `MD4-5 page: BASE`
- Ligne export : 117103 · id 180615

#### Safety off button 45 reset  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb buttons 45`, `MD4-5 page: BASE`
- Ligne export : 117113 · id 212850

#### MD4-Status:MD45  `MDGN`
- Propriétés : Value=Module status · Module=MD45-ET-39 (MD4-5[1]) · Module index=0
- Utilisé par : `md45 State ok`
- Ligne export : 117123 · id 216430

#### md45 State ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `MD4-Status:MD45 = 64`
- Lit : `MD4-Status:MD45`
- Utilisé par : `trameb buttons 45`
- Ligne export : 117134 · id 216466

#### Active display page MD45  `SIC`
> 1 main, 2 info
- Propriétés : Value=Active display page
- Utilisé par : `Info page on 45`
- Ligne export : 117179 · id 202634

#### Info page on 45  `IDC`
> info active page 2, info bit 1
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Active display page MD45 = 3`
  - **Blocking** = `(Active display page MD45 = 1) OR (Active display page MD45 = 2)`
- Lit : `Active display page MD45`
- Utilisé par : `trameb buttons 45`
- Ligne export : 117188 · id 216524

#### RESET 10 hours check  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb buttons 45`, `MD4-5 page: 10 HOURS CHECK`
- Ligne export : 117251 · id 236867

#### RESET 1ry Maintenance  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb buttons 45`, `MD4-5 page: 1YR MAINTENANCE`
- Ligne export : 117261 · id 238428

#### RESET 2yrs Maintenance  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb buttons 45`, `MD4-5 page: 2YRS MAINTENANCE`
- Ligne export : 117271 · id 238430

#### RESET 4yrs Maintenance  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `trameb buttons 45`, `MD4-5 page: 4YRS MAINTENANCE`
- Ligne export : 117281 · id 238432

#### F5 Speed Super slow 45  `VDIN`
> Super slow = slow sur le MD4
- Propriétés : Toggle=No
- Utilisé par : `trameb buttons 45`, `MD4-5 page: BASE`
- Ligne export : 117291 · id 240461

#### trameb buttons 45  `ARC`
- Propriétés : Array size=18 · Store value=No
- Logique :
  ```qcode
  This[0]:=Virtual UP 45*1
  This[1]:=Virtual DOWN 45*2
  This[2]:=Cancel Button 45*4
  This[3]:=F2 Speed Slow 45*8
  This[4]:=F3 Speed Fast 45*16
  This[5]:=OFF Button 45*32
  This[6]:=Continue Button 45*64
  This[7]:=F4 Speed Free 45*128
  This[8]:=Start Button 4ET*256
  This[9]:=Safety off button 45*512
  This[10]:=Safety off button 45 reset*1024
  This[11]:=md45 State ok*2048
  This[12]:=Info page on 45*4096
  This[13]:=RESET 10 hours check*8192
  This[14]:=RESET 1ry Maintenance*16384
  This[15]:=RESET 2yrs Maintenance*32768
  This[16]:=RESET 4yrs Maintenance*65536
  This[17]:=F5 Speed Super slow 45*131072
  ```
- Lit : `Cancel Button 45`, `Continue Button 45`, `F2 Speed Slow 45`, `F3 Speed Fast 45`, `F4 Speed Free 45`, `F5 Speed Super slow 45`, `Info page on 45`, `OFF Button 45`, `RESET 10 hours check`, `RESET 1ry Maintenance`, `RESET 2yrs Maintenance`, `RESET 4yrs Maintenance`, `Safety off button 45`, `Safety off button 45 reset`, `Start Button 4ET`, `Virtual DOWN 45`, `Virtual UP 45`, `md45 State ok`
- Utilisé par : `buttons 45 dtobin`
- Ligne export : 117301 · id 213488

#### buttons 45 dtobin  `MAC`
- Logique :
  ```qcode
  Result:=trameb buttons 45[0]+trameb buttons 45[1]+trameb buttons 45[2]+trameb buttons 45[3]+trameb buttons 45[4]+trameb buttons 45[5]+trameb buttons 45[6]+trameb buttons 45[7]+trameb buttons 45[8]+trameb buttons 45[9]+trameb buttons 45[10]+trameb buttons 45[11]+trameb buttons 45[12]+trameb buttons 45[13]+trameb buttons 45[14]+trameb buttons 45[15]+trameb buttons 45[16]+trameb buttons 45[17]
  ```
- Lit : `trameb buttons 45`
- Utilisé par : `buttons 45 bin to d debug`, `buttons 45 dtobin APPOUT`
- Ligne export : 117341 · id 213504

#### buttons 45 bin to d debug  `ARC`
- Propriétés : Array size=18 · Store value=No
- Logique :
  ```qcode
  This[0]:=buttons 45 dtobin mod 2
  This[1]:=(buttons 45 dtobin div 2) mod 2
  This[2]:=(buttons 45 dtobin div 4) mod 2
  This[3]:=(buttons 45 dtobin div 8) mod 2
  This[4]:=(buttons 45 dtobin div 16) mod 2
  This[5]:=(buttons 45 dtobin div 32) mod 2
  This[6]:=(buttons 45 dtobin div 64) mod 2
  This[7]:=(buttons 45 dtobin div 128) mod 2
  This[8]:=(buttons 45 dtobin div 256) mod 2
  This[9]:=(buttons 45 dtobin div 512) mod 2
  This[10]:=(buttons 45 dtobin div 1024) mod 2
  This[11]:=(buttons 45 dtobin div 2048) mod 2
  This[12]:=(buttons 45 dtobin div 4096) mod 2
  This[13]:=(buttons 45 dtobin div 8192) mod 2
  This[14]:=(buttons 45 dtobin div 16384) mod 2
  This[15]:=(buttons 45 dtobin div 32768) mod 2
  This[16]:=(buttons 45 dtobin div 65536) mod 2
  This[17]:=(buttons 45 dtobin div 131072) mod 2
  ```
- Lit : `buttons 45 dtobin`
- Utilisé par : `B1 UP 45`, `B10 SAFETY OFF 45`, `B11 SAFETY OFF RESET 45`, `B12 45 State ok`, `B13 Info page on 45`, `B14 10 hours certified button`, `B15 RESET 1yr Maintenance button`, `B16 RESET 2yrs Maintenance button`, `B17 RESET 4yrs Maintenance button`, `B18 super slow 45`, `B2 DOWN 45`, `B3 CANCEL 45`, `B4 SLOW 45`, `B5 FAST 45`, `B6 OFF 45`, `B7 CONTINUE 45`, `B8 FREE 45`, `B9 START 45`
- Ligne export : 117359 · id 213518

#### B1 UP 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[0]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117396 · id 213535

#### B2 DOWN 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[1]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117416 · id 213541

#### B3 CANCEL 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[2]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117436 · id 213689

#### B4 SLOW 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[3]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117456 · id 213697

#### B5 FAST 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[4]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117476 · id 213712

#### B6 OFF 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[5]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117496 · id 213720

#### B7 CONTINUE 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[6]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117516 · id 213735

#### B8 FREE 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[7]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117536 · id 213743

#### B9 START 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[8]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117556 · id 213758

#### B10 SAFETY OFF 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[9]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117576 · id 213766

#### B11 SAFETY OFF RESET 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[10]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117596 · id 213781

#### buttons 45 dtobin APPOUT  `APPOUT`
- Propriétés : Input channel=buttons 45 dtobin · Send method=On change · Transmit rate=1000
- Lit : `buttons 45 dtobin`
- Utilisé par : `dtob APPIN 45`
- Ligne export : 117616 · id 213809

#### Be1 Inter Buzzer for 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=info from mc bintod 2[0]
  ```
- Lit : `info from mc bintod 2`
- Utilisé par : `Buzzer ET45 C2:3`
- Ligne export : 117627 · id 217010

#### Buzzer ET45 C2:3  `DOUT`
> input is Be1 Inter Buzzer for 45
- Propriétés : Delay on=0 · Delay off=0 · Input channel=Be1 Inter Buzzer for 45 · Module=MD45-ET-39 (MD4-5[1]) · Module index=0
- Lit : `Be1 Inter Buzzer for 45`
- Utilisé par : *(personne)*
- Ligne export : 117647 · id 181358

#### B12 45 State ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[11]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117660 · id 216485

#### B13 Info page on 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[12]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117680 · id 216546

#### +BAT:MD45  `MDGN`
- Propriétés : Value=Supply voltage [V] · Module=MD45-ET-39 (MD4-5[1]) · Module index=4
- Utilisé par : *(personne)*
- Ligne export : 117700 · id 216578

#### Be2 Main page IDC E  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=info from mc bintod 2[1]
  ```
- Lit : `info from mc bintod 2`
- Utilisé par : `Main page n45`, `MD4-5 page: MAIN Elec`
- Ligne export : 117711 · id 217018

#### Be3 Main page IDC T  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=info from mc bintod 2[2]
  ```
- Lit : `info from mc bintod 2`
- Utilisé par : `Main page n45`, `MD4-5 page: MAIN Thermic`
- Ligne export : 117731 · id 217026

#### Be4 ShutDown page IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=info from mc bintod 2[3]
  ```
- Lit : `info from mc bintod 2`
- Utilisé par : `MD4-5 page: SHUTDOWN`
- Ligne export : 117751 · id 217034

#### Be5 Startup page IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=info from mc bintod 2[4]
  ```
- Lit : `info from mc bintod 2`
- Utilisé par : `MD4-5 page: brokenSTARTUP PIN`
- Ligne export : 117771 · id 217042

#### Be6 Engines READY for 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=info from mc bintod 2[5]
  ```
- Lit : `info from mc bintod 2`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 117791 · id 217050

#### Be7 Safety_disable 45 sel  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=info from mc bintod 2[6]
  ```
- Lit : `info from mc bintod 2`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 117811 · id 217058

#### Main page n45  `IDC`
> Be2 Main page IDC E OR Be3 Main page IDC T
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Be2 Main page IDC E) OR (Be3 Main page IDC T)`
- Lit : `Be2 Main page IDC E`, `Be3 Main page IDC T`
- Utilisé par : `MD4-5 page: SHUTDOWN`, `MD4-5 page: brokenSTARTUP PIN`
- Ligne export : 117831 · id 217095

#### Joystick plugged md45  `DP`
> inside Master Config
- Propriétés : Default mode={False}
- Utilisé par : `Active le groupe: Joystick md45`, `Adjust group: Master Config`, `Dual adjust item: Left Joystick`, `Dual adjust item: Right Joystick`, `Measure group: Translation`, `Single adjust item: Joystick plugged md45`
- Ligne export : 117881 · id 229325

#### 45Project version  `SIC`
- Propriétés : Value=Project version
- Lit : `Project version`
- Utilisé par : `MD4-5 page: INFO`
- Ligne export : 117956 · id 232924

#### batt ok to start APPIN  `APPIN`
- Propriétés : Input channel=batt ok to start APPOUT
- Lit : `batt ok to start APPOUT`
- Utilisé par : `Be10 batt ok to start md4`
- Ligne export : 117965 · id 236414

#### Be10 batt ok to start md4  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=batt ok to start APPIN
  ```
- Lit : `batt ok to start APPIN`
- Utilisé par : *(personne)*
- Ligne export : 117974 · id 236402

#### B14 10 hours certified button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[13]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 117994 · id 236875

#### B15 RESET 1yr Maintenance button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[14]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 118014 · id 238455

#### B16 RESET 2yrs Maintenance button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[15]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 118034 · id 238467

#### B17 RESET 4yrs Maintenance button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[16]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 118054 · id 238479

#### V10 motor  `DP`
- Propriétés : True text=True · False text=False · Default mode={False}
- Utilisé par : `Adjust group: Master Config`, `MD4-5 page: INFO`, `Single adjust item: V10 motor`
- Ligne export : 118074 · id 240704

#### B18 super slow 45  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=buttons 45 bin to d debug[17]
  ```
- Lit : `buttons 45 bin to d debug`
- Utilisé par : *(personne)*
- Ligne export : 118177 · id 240470

#### be10 enabled ON/OFF T&E  `IDC`
> envoi dans le MD4 du enable du bouton on/off, valable pour therm et elec
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=info from mc bintod 2[10]
  ```
- Lit : `info from mc bintod 2`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 118197 · id 240683

#### be11 button drive 4ET 45/10  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=info from mc bintod 2[11]
  ```
- Lit : `info from mc bintod 2`
- Utilisé par : `MD4-5 page: BASE`
- Ligne export : 118217 · id 240949
