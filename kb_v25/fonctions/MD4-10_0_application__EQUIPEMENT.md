# MD4-10[0] application — EQUIPEMENT

449 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## EQUIPEMENT

#### OutBoard Button  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `Auto Light and Start`, `Auto Off - Timer`, `Engine 1 - Wait`, `Engine 2 - Wait`, `Engine On`, `MD4-10 page: MAIN`, `MD4-10 page: OUTBOARD`
- Ligne export : 5543 · id 52321

#### GPS  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `KTB K1 IDC - GPS_EQT`, `MD4-10 page: FEATURE`
- Ligne export : 5554 · id 45694

#### Auto Off Lamps  `IDC`
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0
- Logique :
  - **Activating** = `(Power Down) OR (Charger Charging Wait 2 minutes)`
- Lit : `Charger Charging Wait 2 minutes`, `Power Down`
- Utilisé par : `KBB K12 IDC - BILGE`, `KBB K7 IDC - AUX 1`, `KBB K8 DC - PUMP SHOWER`, `KBB K9 IDC - PUMP WIND`, `KTB K1 IDC - GPS_EQT`, `KTB K10 IDC - Fridge`, `KTB K12 IDC - Aux 2`, `KTB K2 IDC - AUDIO/AUX 4`, `KTB K3 IDC - VHF/AUX 5`, `KTB K4 IDC- Cabine`, `KTB K5 IDC - HT - 360 White`, `KTB K6 IDC - NAV`, `KTB K7 IDC - HT - Spot`, `KTB K8 DC - HT - DIM`, `KTB K9 IDC - Cockpit Light`, `KTC K1 IDC - Wipper On/Off`, `KTC K12 IDC - AUX 3`, `KTC K2 IDC - Wipper Speed`, `KTC K3 IDC - Seat Power`, `KTC K4 IDC - Water Cooling`, `KTC K5 IDC - Pump Water`, `KTC K8 DC - Fan wind cmd`
- Ligne export : 5565 · id 49989

#### KTB K1 IDC - GPS_EQT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `GPS`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `GPS`
- Utilisé par : `Adress Loose`, `KTB K1 IDC - GPS_EQT`, `KTB K1 IDC - GPSfct`
- Ligne export : 5615 · id 45009

#### AUDIO  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `KTB K2 IDC - AUDIO/AUX 4`, `MD4-10 page: FEATURE`
- Ligne export : 5665 · id 45696

#### KTB K2 IDC - AUDIO/AUX 4  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `AUDIO OR (AUX 4)`
  - **Blocking** = `(Auto Off Lamps) OR ((not(Battery Drive Mode)) and Aux 4 - Need HT)`
- Lit : `AUDIO`, `AUX 4`, `Auto Off Lamps`, `Aux 4 - Need HT`, `Battery Drive Mode`
- Utilisé par : `KTB K2 IDC - AUDIO/AUX 4`, `KTB K2 IDC - AUDIO/AUX 4`
- Ligne export : 5676 · id 45018

#### VHF  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `KTB K3 IDC - VHF/AUX 5`, `MD4-10 page: FEATURE`
- Ligne export : 5750 · id 45697

#### KTB K3 IDC - VHF/AUX 5  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `VHF OR (AUX 5)`
  - **Blocking** = `(Auto Off Lamps) OR ((not(Battery Drive Mode)) and Aux 5 - Need HT)`
- Lit : `AUX 5`, `Auto Off Lamps`, `Aux 5 - Need HT`, `Battery Drive Mode`, `VHF`
- Utilisé par : `KTB K3 IDC - VHF/AUX 5`, `KTB K3 IDC - VHF/AUX 5`
- Ligne export : 5761 · id 45027

#### Water Level Protection  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `LOW Level`, `Adjust group: Master Setup`, `Single adjust item: Water Level Protection`
- Ligne export : 5835 · id 53610

#### LOW Level  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `(Water Level [%] < 2) and Water Level Protection`
- Lit : `Water Level`, `Water Level Protection`
- Utilisé par : `KBB K8 DC - PUMP SHOWER`
- Ligne export : 5848 · id 49921

#### SHOWER  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `KBB K8 DC - PUMP SHOWER`, `MD4-10 page: FEATURE`
- Ligne export : 5909 · id 45701

#### Button Cabine  `DIN`
- Propriétés : Module=MD4-10[0] · Module index=3
- Utilisé par : `Button Cabine IDC`
- Ligne export : 5920 · id 69854

#### Button Cabine IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `Button Cabine`
- Lit : `Button Cabine`
- Utilisé par : `CABINE ON/OFF`, `Cabine Counter`
- Ligne export : 5930 · id 85585

#### CABINE ON/OFF  `VDIN`
- Propriétés : Toggle=Yes · Resetting channel=Button Cabine IDC · Store value=No
- Lit : `Button Cabine IDC`
- Utilisé par : `Cabine Counter`, `KTB K4 IDC- Cabine`, `MD4-10 page: BASE`, `MD4-10 page: FEATURE`
- Ligne export : 5973 · id 45951

#### Cabine Counter  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `(Button Cabine IDC) OR (PositiveFlank(CABINE ON/OFF))`
  - **Resetting** = `(Cabine Counter >= 2) OR (PositiveFlank(CABINE ON/OFF)) OR (NegativeFlank(CABINE ON/OFF))`
- Lit : `Button Cabine IDC`, `CABINE ON/OFF`
- Utilisé par : `KTB K4 IDC- Cabine`
- Ligne export : 5984 · id 69866

#### KTB K4 IDC- Cabine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(CABINE ON/OFF) OR (Cabine Counter)`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `CABINE ON/OFF`, `Cabine Counter`
- Utilisé par : `KTB K4 IDC- Cabine`, `KTB K4 IDC- Cabine`
- Ligne export : 6068 · id 45036

#### WIND CLEANER  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Wind Cleaner IDC`, `Wind Cleaner Wipper IDC`, `MD4-10 page: MAIN`, `MD4-10 page: OUTBOARD`
- Ligne export : 6125 · id 45702

#### Wind Cleaner IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  - **Activating** = `PositiveFlank(WIND CLEANER)`
- Lit : `WIND CLEANER`
- Utilisé par : `KBB K9 IDC - PUMP WIND`
- Ligne export : 6135 · id 47819

#### Wipper Button  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Wipper Button 2 s`, `Wipper State`, `MD4-10 page: MAIN`, `MD4-10 page: OUTBOARD`
- Ligne export : 6179 · id 47747

#### Wipper Button 2 s  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Wipper Button`
- Lit : `Wipper Button`
- Utilisé par : `Wipper State`
- Ligne export : 6189 · id 49370

#### Wipper State  `ECNT`
- Propriétés : Store value=No · Reset value=0
- Logique :
  - **Increasing** = `PositiveFlank(Wipper Button)`
  - **Resetting** = `(Wipper State >= 4) OR (PositiveFlank(Wipper Button 2 s))`
- Lit : `Wipper Button`, `Wipper Button 2 s`
- Utilisé par : `KTC K1 IDC - Wipper On/Off`, `KTC K2 IDC - Wipper Speed`, `SMC Wipper`, `Wipper Timer`, `MD4-10 page: MAIN`
- Ligne export : 6232 · id 47748

#### Wiper delay  `IP`
- Propriétés : Unit=s · Default mode={5}
- Utilisé par : `Wipper Timer`, `Adjust group: Main Setup`, `Single adjust item: Wiper delay`
- Ligne export : 6301 · id 47767

#### Wipper Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Wipper State = 1`
  - **Resetting** = `(Wipper Timer [s] > Wiper delay [s]) OR (Wipper State <> 1)`
- Lit : `Wiper delay`, `Wipper State`
- Utilisé par : `Wipper Start Inter`
- Ligne export : 6313 · id 47760

#### Wipper Start Inter  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Wipper Timer [s] > 0`
- Lit : `Wipper Timer`
- Utilisé par : `Wipper Int IDC`
- Ligne export : 6385 · id 47768

#### Wipper Int IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(Wipper Start Inter)`
- Lit : `Wipper Start Inter`
- Utilisé par : `KTC K1 IDC - Wipper On/Off`
- Ligne export : 6430 · id 47797

#### Wind Cleaner Wipper IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `PositiveFlank(WIND CLEANER)`
- Lit : `WIND CLEANER`
- Utilisé par : `KTC K1 IDC - Wipper On/Off`
- Ligne export : 6474 · id 54651

#### KTC K1 IDC - Wipper On/Off  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Wipper Int IDC) OR (Wipper State > 1) OR (Wind Cleaner Wipper IDC)`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `Wind Cleaner Wipper IDC`, `Wipper Int IDC`, `Wipper State`
- Utilisé par : `KTC K1 IDC - Wipper On/Off`, `KTC K1 IDC - Wipper On/Off`
- Ligne export : 6518 · id 47084

#### NAV + 360 LIGHT  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `KTB K5 IDC - HT - 360 White`, `KTB K6 IDC - NAV`, `MD4-10 page: FEATURE`
- Ligne export : 6584 · id 47602

#### Auto Light and Start  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Tracks Button or OutBoard Button) and Auto Light ON`
- Lit : `Auto Light ON`, `OutBoard Button`, `Tracks Button`
- Utilisé par : `KTB K11 IDC - SearchLight`, `KTB K5 IDC - HT - 360 White`, `KTB K6 IDC - NAV`
- Ligne export : 6595 · id 55101

#### Blink Light IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Blink Light`
- Lit : `Blink Light`
- Utilisé par : `KTB K11 IDC - SearchLight`, `Not Blink Light`, `Not Blink Light Mode`
- Ligne export : 6649 · id 56929

#### Not Blink Light Mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `Blink Light IDC`
- Lit : `Blink Light IDC`
- Utilisé par : `Not Blink Light`
- Ligne export : 6692 · id 57606

#### Not Blink Light  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Blink Light IDC)`
  - **Blocking** = `not(Not Blink Light Mode)`
- Lit : `Blink Light IDC`, `Not Blink Light Mode`
- Utilisé par : `KTB K11 IDC - SearchLight`
- Ligne export : 6735 · id 57390

#### KTB K5 IDC - HT - 360 White  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(NAV + 360 LIGHT) OR (Auto Light and Start)`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Light and Start`, `Auto Off Lamps`, `NAV + 360 LIGHT`
- Utilisé par : `KTB K5 IDC - HT - 360 White`, `KTB K5 IDC - HT - 360 White`
- Ligne export : 6787 · id 45045

#### KTB K6 IDC - NAV  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(NAV + 360 LIGHT) OR (Auto Light and Start)`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Light and Start`, `Auto Off Lamps`, `NAV + 360 LIGHT`
- Utilisé par : `KTB K6 IDC - NAV`, `KTB K6 IDC - NAV`, `MD4-10 page: MAIN`
- Ligne export : 6844 · id 45054

#### LIGHT HT SPOT  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `KTB K7 IDC - HT - Spot`, `MD4-10 page: FEATURE`
- Ligne export : 6901 · id 52419

#### KTB K7 IDC - HT - Spot  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `LIGHT HT SPOT`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `LIGHT HT SPOT`
- Utilisé par : `KTB K7 IDC - HT - Spot`, `KTB K7 IDC - HT - Spot`
- Ligne export : 6912 · id 45063

#### LIGHT HT DIM  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `KTB K8 DC - HT - DIM`, `MD4-10 page: FEATURE`
- Ligne export : 6962 · id 45705

#### KTB K8 DC - HT - DIM  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `LIGHT HT DIM`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `LIGHT HT DIM`
- Utilisé par : `KTB K8 DC - HT - DIM`, `KTB K8 DC - HT - DIM`
- Ligne export : 6973 · id 45073

#### KTB K9 IDC - Cockpit Light  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `A/C Clim KTBK9`
  - **Blocking** = `Auto Off Lamps`
- Lit : `A/C Clim KTBK9`, `Auto Off Lamps`
- Utilisé par : `KTB K9 IDC - Cockpit Light`, `KTB K9 IDC - Cockpit Light`
- Ligne export : 7023 · id 45083

#### FAN WIND  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `KTC K8 DC - Fan wind cmd`, `MD4-10 page: FEATURE`
- Ligne export : 7073 · id 45709

#### Fridge  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `KTB K10 IDC - Fridge`, `MD4-10 page: FEATURE`
- Ligne export : 7084 · id 54598

#### KTB K10 IDC - Fridge  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Fridge`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `Fridge`
- Utilisé par : `KTB K10 IDC - Fridge`, `KTB K10 IDC - Fridge`
- Ligne export : 7095 · id 45091

#### Search Light  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `KTB K11 IDC - SearchLight`, `MD4-10 page: FEATURE`
- Ligne export : 7145 · id 46094

#### LD UP - VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `LD UP`, `MD4-10 page: MAIN`
- Ligne export : 7156 · id 45947

#### Remote  `IMAC`
- Logique :
  - **Controlling** = `Remote Status`
- Lit : `Remote Status`
- Utilisé par : `LD UP`, `Remote Down Wait 3s`, `Unlock Boat`
- Ligne export : 7166 · id 75712

#### LD UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(LD UP - VDIN) OR (Remote = 1)`
- Lit : `LD UP - VDIN`, `Remote`
- Utilisé par : `LD Down Toogle`, `LD UP - Wait`, `LD UP Toogle`, `MD4-10 page: SETUP`
- Ligne export : 7207 · id 47700

#### LD UP - Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `LD UP`
- Lit : `LD UP`
- Utilisé par : `LD UP Toogle`
- Ligne export : 7259 · id 47675

#### LD DOWN - VDIN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `LD DOWN`, `MD4-10 page: MAIN`
- Ligne export : 7302 · id 45948

#### Remote Down Wait 3s  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `Remote = 2`
- Lit : `Remote`
- Utilisé par : `LD DOWN`
- Ligne export : 7312 · id 51086

#### LD DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(LD DOWN - VDIN) OR (Remote Down Wait 3s)`
- Lit : `LD DOWN - VDIN`, `Remote Down Wait 3s`
- Utilisé par : `LD DOWN - Wait`, `LD Down Toogle`, `LD UP Toogle`, `MD4-10 page: SETUP`
- Ligne export : 7357 · id 47711

#### Ladder Stop Sensor  `IP`
- Propriétés : Unit=Pulse/s · Default mode={100}
- Utilisé par : `Stop Ladder`, `Adjust group: Master Setup`, `Single adjust item: Ladder Stop Sensor`
- Ligne export : 7407 · id 53931

#### Ladder Protection  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `LD Down Toogle`, `LD UP Toogle`, `Stop Ladder`, `Adjust group: Maintenance`, `Adjust group: Master Setup`, `Single adjust item: Ladder Protection`
- Ligne export : 7419 · id 53953

#### KBB K4 IDC- LD DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(LD Down Toogle) OR (LD DOWN - Force)`
  - **Blocking** = `KBB K3 IDC - LD UP`
- Lit : `KBB K3 IDC - LD UP`, `LD DOWN - Force`, `LD Down Toogle`
- Utilisé par : `KBB K3 IDC - LD UP`, `KBB K4 IDC- LD DOWN`, `KBB K4 IDC- LD DOWNfct`, `KTB K11 IDC - SearchLight`, `Ladder Timer`, `Power Down Timer Ask`
- Ligne export : 7432 · id 45865

#### Stop Ladder  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `(Ladder Stop Sensor [Pulse/s] > Speed Mouvement [%/s]) and (LD UP Toogle or LD Down Toogle)`
  - **Blocking** = `not(Ladder Protection)`
- Lit : `LD Down Toogle`, `LD UP Toogle`, `Ladder Protection`, `Ladder Stop Sensor`, `Speed Mouvement`
- Utilisé par : `LD Down Toogle`, `LD UP Toogle`, `Ladder Error Msg`
- Ligne export : 7489 · id 53915

#### Ladder Timer End  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `PositiveFlank((Ladder Timer [ms] <= 0))`
- Lit : `Ladder Timer`
- Utilisé par : `LD Down Toogle`, `LD UP Toogle`
- Ligne export : 7560 · id 69417

#### LD UP Toogle  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank(LD UP - Wait)) OR (LD UP Toogle and Ladder Protection) OR (LD UP - Wait and (not(Ladder Protection)))`
  - **Blocking** = `(PositiveFlank(LD DOWN)) OR (LD UP Toogle and (PositiveFlank(LD UP))) OR (Stop Ladder) OR (Ladder Timer End)`
- Lit : `LD DOWN`, `LD UP`, `LD UP - Wait`, `Ladder Protection`, `Ladder Timer End`, `Stop Ladder`
- Utilisé par : `KBB K3 IDC - LD UP`, `Stop Ladder`
- Ligne export : 7613 · id 48179

#### LD UP - Force  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `KBB K3 IDC - LD UP`, `MD4-10 page: SETUP`
- Ligne export : 7722 · id 58755

#### KBB K3 IDC - LD UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(LD UP Toogle) OR (LD UP - Force)`
  - **Blocking** = `KBB K4 IDC- LD DOWN`
- Lit : `KBB K4 IDC- LD DOWN`, `LD UP - Force`, `LD UP Toogle`
- Utilisé par : `KBB K3 IDC - LD UP`, `KBB K3 IDC - LD UPfct`, `KBB K4 IDC- LD DOWN`, `KTB K11 IDC - SearchLight`, `Ladder Timer`, `Power Down Timer Ask`
- Ligne export : 7732 · id 45856

#### LD DOWN - Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `LD DOWN`
- Lit : `LD DOWN`
- Utilisé par : `LD Down Toogle`
- Ligne export : 7789 · id 47686

#### LD Down Toogle  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank(LD DOWN - Wait)) OR (LD Down Toogle and Ladder Protection) OR (LD DOWN - Wait and (not(Ladder Protection)))`
  - **Blocking** = `(PositiveFlank(LD UP)) OR (LD Down Toogle and (PositiveFlank(LD DOWN))) OR (Stop Ladder) OR (Ladder Timer End)`
- Lit : `LD DOWN`, `LD DOWN - Wait`, `LD UP`, `Ladder Protection`, `Ladder Timer End`, `Stop Ladder`
- Utilisé par : `KBB K4 IDC- LD DOWN`, `Stop Ladder`
- Ligne export : 7832 · id 48212

#### LD DOWN - Force  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `KBB K4 IDC- LD DOWN`, `MD4-10 page: SETUP`
- Ligne export : 7941 · id 58756

#### Speed Mouvement  `MAC`
- Propriétés : Unit=%/s · Limiting object group=Signed
- Logique :
  - **Controlling** = `Abs((DerivativeOf(Ladder Sensor)))`
- Lit : `Ladder Sensor`
- Utilisé par : `Stop Ladder`
- Ligne export : 7951 · id 53892

#### Ladder Timer  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=35000
- Logique :
  - **Decreasing** = `(KBB K3 IDC - LD UP) OR (KBB K4 IDC- LD DOWN)`
  - **Resetting** = `(PositiveFlank(KBB K3 IDC - LD UP)) OR (PositiveFlank(KBB K4 IDC- LD DOWN))`
- Lit : `KBB K3 IDC - LD UP`, `KBB K4 IDC- LD DOWN`
- Utilisé par : `Ladder Timer End`
- Ligne export : 8002 · id 69404

#### KTB K11 IDC - SearchLight  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Search Light) OR (KBB K3 IDC - LD UP) OR (KBB K4 IDC- LD DOWN) OR ((Auto Light and Start and TRACK DOWN) and Tracks Button) OR (Blink Light IDC)`
  - **Blocking** = `Not Blink Light`
- Lit : `Auto Light and Start`, `Blink Light IDC`, `KBB K3 IDC - LD UP`, `KBB K4 IDC- LD DOWN`, `Not Blink Light`, `Search Light`, `TRACK DOWN`, `Tracks Button`
- Utilisé par : `KTB K11 IDC - SearchLight`, `KTB K11 IDC - SearchLight`
- Ligne export : 8077 · id 45099

#### AUX 2  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `Aux 2 - Text`, `KTB K12 IDC - Aux 2`, `Need Charge`, `MD4-10 page: FEATURE`
- Ligne export : 8166 · id 54601

#### KTB K12 IDC - Aux 2  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `AUX 2`
  - **Blocking** = `(Auto Off Lamps) OR ((not(Battery Drive Mode)) and Aux 2 - Need HT)`
- Lit : `AUX 2`, `Auto Off Lamps`, `Aux 2 - Need HT`, `Battery Drive Mode`
- Utilisé par : `KTB K12 IDC - Aux 2`, `KTB K12 IDC - Aux 2`
- Ligne export : 8177 · id 45107

#### HT UP  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `HT Down Toogle`, `HT UP`, `HT UP - Wait`, `HT UP Toogle`, `MD4-10 page: MAIN`
- Ligne export : 8244 · id 45945

#### HT DOWN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `HT DOWN`, `HT DOWN - Wait`, `HT Down Toogle`, `HT UP Toogle`, `MD4-10 page: MAIN`
- Ligne export : 8254 · id 45946

#### HT UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `HT UP`
- Lit : `HT UP`
- Utilisé par : `HT Down Toogle`, `HT UP - Wait`, `HT UP Toogle`, `MD4-10 page: MAIN`
- Ligne export : 8264 · id 51189

#### HT UP - Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `HT UP`
- Lit : `HT UP`
- Utilisé par : `HT UP Toogle`, `KBB K1 IDC - HT - UP`
- Ligne export : 8307 · id 51197

#### HT DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `HT DOWN`
- Lit : `HT DOWN`
- Utilisé par : `HT DOWN - Wait`, `HT Down Toogle`, `HT UP Toogle`, `MD4-10 page: MAIN`
- Ligne export : 8350 · id 51205

#### HT UP Toogle  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank(HT UP - Wait)) OR (HT UP Toogle)`
  - **Blocking** = `(PositiveFlank(HT DOWN)) OR (HT UP Toogle and (PositiveFlank(HT UP)))`
- Lit : `HT DOWN`, `HT UP`, `HT UP - Wait`
- Utilisé par : `HT Timer`
- Ligne export : 8393 · id 51213

#### HT DOWN - Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `HT DOWN`
- Lit : `HT DOWN`
- Utilisé par : `HT Down Toogle`, `KBB K2 IDC - HT -DOWN`
- Ligne export : 8469 · id 51225

#### HT Down Toogle  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank(HT DOWN - Wait)) OR (HT Down Toogle)`
  - **Blocking** = `(PositiveFlank(HT UP)) OR (HT Down Toogle and (PositiveFlank(HT DOWN)))`
- Lit : `HT DOWN`, `HT DOWN - Wait`, `HT UP`
- Utilisé par : `HT Timer`
- Ligne export : 8512 · id 51233

#### HT Timer  `TMR`
- Propriétés : Type (Unit)=Seconds [s] · Store value=Yes · Reset value=0
- Logique :
  - **Increasing** = `HT UP Toogle and (HT Timer [s] < 32)`
  - **Decreasing** = `HT Down Toogle`
- Lit : `HT Down Toogle`, `HT UP Toogle`
- Utilisé par : `KBB K1 IDC - HT - UP`, `KBB K2 IDC - HT -DOWN`, `MD4-10 page: MAIN`
- Ligne export : 8588 · id 51245

#### KBB K2 IDC - HT -DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `((DerivativeOf(HT Timer [s])) < 0) OR (HT DOWN - Wait)`
  - **Blocking** = `KBB K1 IDC - HT - UP`
- Lit : `HT DOWN - Wait`, `HT Timer`, `KBB K1 IDC - HT - UP`
- Utilisé par : `KBB K1 IDC - HT - UP`, `KBB K2 IDC - HT -DOWN`, `KBB K2 IDC - HT -DOWN`
- Ligne export : 8665 · id 45847

#### KBB K1 IDC - HT - UP  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `((DerivativeOf(HT Timer [s])) > 0) OR (HT UP - Wait)`
  - **Blocking** = `KBB K2 IDC - HT -DOWN`
- Lit : `HT Timer`, `HT UP - Wait`, `KBB K2 IDC - HT -DOWN`
- Utilisé par : `KBB K1 IDC - HT - UP`, `KBB K1 IDC - HT - UP`, `KBB K2 IDC - HT -DOWN`
- Ligne export : 8732 · id 45838

#### ANCHOR UP  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `KBB K5 IDC - ANCHOR UP`, `KBB K6 IDC - ANCHOR DOWN`, `MD4-10 page: FEATURE`
- Ligne export : 8799 · id 45949

#### ANCHOR DOWN  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `KBB K5 IDC - ANCHOR UP`, `KBB K6 IDC - ANCHOR DOWN`, `MD4-10 page: FEATURE`
- Ligne export : 8809 · id 45950

#### KBB K5 IDC - ANCHOR UP  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `ANCHOR UP`
  - **Blocking** = `ANCHOR DOWN`
- Lit : `ANCHOR DOWN`, `ANCHOR UP`
- Utilisé par : `KBB K5 IDC - ANCHOR UP`, `KBB K5 IDC - ANCHOR UP`
- Ligne export : 8819 · id 45874

#### KBB K6 IDC - ANCHOR DOWN  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `ANCHOR DOWN`
  - **Blocking** = `ANCHOR UP`
- Lit : `ANCHOR DOWN`, `ANCHOR UP`
- Utilisé par : `KBB K6 IDC - ANCHOR DOWN`, `KBB K6 IDC - ANCHOR DOWN`
- Ligne export : 8869 · id 45883

#### AUX 1  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `Aux 1 - Text`, `KBB K7 IDC - AUX 1`, `Need Charge`, `MD4-10 page: FEATURE`
- Ligne export : 8919 · id 54184

#### KBB K7 IDC - AUX 1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `AUX 1`
  - **Blocking** = `(Auto Off Lamps) OR ((not(Battery Drive Mode)) and Aux 1 - Need HT)`
- Lit : `AUX 1`, `Auto Off Lamps`, `Aux 1 - Need HT`, `Battery Drive Mode`
- Utilisé par : `KBB K7 IDC - AUX 1`, `KBB K7 IDC - AUX 1`
- Ligne export : 8930 · id 45892

#### KBB K8 DC - PUMP SHOWER  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `SHOWER`
  - **Blocking** = `(Auto Off Lamps) OR (LOW Level)`
- Lit : `Auto Off Lamps`, `LOW Level`, `SHOWER`
- Utilisé par : `KBB K8 DC - PUMP SHOWER`, `KBB K8 DC - PUMP SHOWER`
- Ligne export : 8997 · id 45901

#### KBB K9 IDC - PUMP WIND  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Wind Cleaner IDC`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `Wind Cleaner IDC`
- Utilisé par : `KBB K9 IDC - PUMP WIND`, `KBB K9 IDC - PUMP WIND`
- Ligne export : 9054 · id 45910

#### KBB K10 IDC - AUTO OFF POWER BOX  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `Auto Off Cmd`
- Lit : `Auto Off Cmd`
- Utilisé par : `KBB K10 IDC - AUTO OFF POWER BOX`, `KBB K10 IDC - AUTO OFF POWER BOX`
- Ligne export : 9104 · id 45919

#### DOOR  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `Door IDC`, `MD4-10 page: BASE`
- Ligne export : 9147 · id 45993

#### Button Door  `DIN`
- Propriétés : Module=MD4-10[0] · Module index=4
- Utilisé par : `Door IDC`
- Ligne export : 9157 · id 46116

#### Door IDC  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=10000
- Logique :
  - **Activating** = `PositiveFlank(DOOR) OR (PositiveFlank(Button Door))`
- Lit : `Button Door`, `DOOR`
- Utilisé par : `KBB K11 IDC - DOOR`
- Ligne export : 9167 · id 47826

#### KBB K11 IDC - DOOR  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Door IDC`
- Lit : `Door IDC`
- Utilisé par : `KBB K11 IDC - DOOR`, `KBB K11 IDC - DOOR`
- Ligne export : 9219 · id 45928

#### BILGE  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `KBB K12 IDC - BILGE`, `MD4-10 page: FEATURE`
- Ligne export : 9262 · id 45995

#### KBB K12 IDC - BILGE  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `BILGE`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `BILGE`
- Utilisé par : `KBB K12 IDC - BILGE`, `KBB K12 IDC - BILGE`
- Ligne export : 9273 · id 45936

#### 0x717  `GFIN`
- Propriétés : Identifier=0x717 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=0
- Utilisé par : *(personne)*
- Ligne export : 9323 · id 46056

#### 0x718  `GFIN`
- Propriétés : Identifier=0x718 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=1
- Utilisé par : *(personne)*
- Ligne export : 9339 · id 46060

#### Byte 0  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`, `GFOUT-F:Generic`
- Ligne export : 9355 · id 46074

#### Byte 1  `GPOUT`
- Propriétés : Input value=0x17 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`, `GFOUT-F:Generic`
- Ligne export : 9366 · id 46075

#### GFOUT-D:Generic  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=3
- Lit : `Byte 0`, `Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 9377 · id 46076

#### Byte 0  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`, `GFOUT-F:Generic`
- Ligne export : 9399 · id 46080

#### Byte 1  `GPOUT`
- Propriétés : Input value=0x18 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`, `GFOUT-F:Generic`
- Ligne export : 9410 · id 46081

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=4
- Lit : `Byte 0`, `Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 9421 · id 46082

#### KTC K2 IDC - Wipper Speed  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Wipper State = 3`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `Wipper State`
- Utilisé par : `KTC K2 IDC - Wipper Speed`, `KTC K2 IDC - Wipper Speed`
- Ligne export : 9771 · id 47094

#### Seat Power Force  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `KTC K3 IDC - Seat Power`, `MD4-10 page: SETUP`
- Ligne export : 9823 · id 56201

#### KTC K3 IDC - Seat Power  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Alim Seat) OR (Seat Power Force)`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Alim Seat`, `Auto Off Lamps`, `Seat Power Force`
- Utilisé par : `KTC K3 IDC - Seat Power`, `KTC K3 IDC - Seat Power`
- Ligne export : 9834 · id 47104

#### KTC K4 IDC - Water Cooling  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `FAN OUT`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `FAN OUT`
- Utilisé par : `KTC K4 IDC - Water Cooling`, `KTC K4 IDC - Water Cooling`
- Ligne export : 9891 · id 47115

#### KTC K5 IDC - Pump Water  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PUMP OUT`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `PUMP OUT`
- Utilisé par : `KTC K5 IDC - Pump Water`, `KTC K5 IDC - Pump Water`
- Ligne export : 9941 · id 47126

#### KTC K7 IDC - Aux B  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `A/CBatPackDCDCRelay`
- Lit : `A/CBatPackDCDCRelay`
- Utilisé par : `KTC K7 IDC - Aux B`, `KTC K7 IDC - Aux B`
- Ligne export : 9991 · id 47146

#### KTC K6 IDC - Aux A  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `A/CBatPackESwitchRelay`
- Lit : `A/CBatPackESwitchRelay`
- Utilisé par : `KTC K6 IDC - Aux A`, `KTC K6 IDC - Aux A`
- Ligne export : 10034 · id 47136

#### KTC K8 DC - Fan wind cmd  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `FAN WIND`
  - **Blocking** = `Auto Off Lamps`
- Lit : `Auto Off Lamps`, `FAN WIND`
- Utilisé par : `KTC K8 DC - Fan wind cmd`, `KTC K8 DC - Fan wind cmd`
- Ligne export : 10077 · id 47156

#### Active display page  `SIC`
- Propriétés : Value=Active display page
- Utilisé par : `Engine On`
- Ligne export : 10127 · id 52322

#### Trim Mode  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `PositiveFlank(Tracks Button)`
- Lit : `Tracks Button`
- Utilisé par : `Engine On`
- Ligne export : 10136 · id 53883

#### Engine On  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(OutBoard Button) OR (Active display page = 0) OR (Trim Mode)`
- Lit : `Active display page`, `OutBoard Button`, `Trim Mode`
- Utilisé par : `KTC K9 IDC - OutBoard On-OFF`
- Ligne export : 10180 · id 52323

#### KTC K9 IDC - OutBoard On-OFF  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Engine On`
- Lit : `Engine On`
- Utilisé par : `Adress Loose Auto`, `KTC K9 IDC - OutBoard On-OFF`, `KTC K9 IDC - OutBoard On-OFFfct`
- Ligne export : 10239 · id 47165

#### Engine 1 - Wait  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `OutBoard Button`
- Lit : `OutBoard Button`
- Utilisé par : `Engine 1 - Flank`
- Ligne export : 10282 · id 52332

#### Engine 1 - Flank  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(Engine 1 - Wait)`
- Lit : `Engine 1 - Wait`
- Utilisé par : `KTC K10 IDC - OutBoard Start PORT`
- Ligne export : 10325 · id 52340

#### START PORT  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `KTC K10 IDC - OutBoard Start PORT`, `MD4-10 page: OUTBOARD`
- Ligne export : 10369 · id 52400

#### KTC K10 IDC - OutBoard Start PORT  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Engine 1 - Flank) OR (START PORT)`
- Lit : `Engine 1 - Flank`, `START PORT`
- Utilisé par : `KTC K10 IDC - OutBoard Start PORT`, `KTC K10 IDC - OutBoard Start PORT`
- Ligne export : 10379 · id 47174

#### Engine Time Starting  `IP`
- Propriétés : Unit=ms · Default mode={500}
- Utilisé par : `Engine 2 - Wait`, `Single adjust item: Engines Time Starting`
- Ligne export : 10429 · id 53597

#### Engine 2 - Wait  `IDC`
- Propriétés : Toggle=No · Delay on=Engine Time Starting [ms] · Delay off=0
- Logique :
  - **Activating** = `OutBoard Button`
- Lit : `Engine Time Starting`, `OutBoard Button`
- Utilisé par : `Engine 2 - Flank`
- Ligne export : 10441 · id 52348

#### Engine 2 - Flank  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `PositiveFlank(Engine 2 - Wait)`
- Lit : `Engine 2 - Wait`
- Utilisé par : `KTC K11 IDC - OutBoard Start STBD`
- Ligne export : 10484 · id 52356

#### START STBD  `VDIN`
- Propriétés : Toggle=No
- Utilisé par : `KTC K11 IDC - OutBoard Start STBD`, `MD4-10 page: OUTBOARD`
- Ligne export : 10528 · id 52401

#### KTC K11 IDC - OutBoard Start STBD  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Engine 2 - Flank) OR (START STBD)`
- Lit : `Engine 2 - Flank`, `START STBD`
- Utilisé par : `KTC K11 IDC - OutBoard Start STBD`, `KTC K11 IDC - OutBoard Start STBD`
- Ligne export : 10538 · id 47183

#### AUX 3  `VDIN`
- Propriétés : Toggle=Yes · Store value=No
- Utilisé par : `Aux 3 - Text`, `KTC K12 IDC - AUX 3`, `Need Charge`, `MD4-10 page: FEATURE`
- Ligne export : 10588 · id 54632

#### KTC K12 IDC - AUX 3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(AUX 3) OR (A/C Clim KTCK12)`
  - **Blocking** = `(Auto Off Lamps) OR ((not(Battery Drive Mode)) and Aux 3 - if A/C Need HT)`
- Lit : `A/C Clim KTCK12`, `AUX 3`, `Auto Off Lamps`, `Aux 3 - if A/C Need HT`, `Battery Drive Mode`
- Utilisé par : `KTC K12 IDC - AUX 3`, `KTC K12 IDC - AUX 3`
- Ligne export : 10599 · id 47193

#### 0x719  `GFIN`
- Propriétés : Identifier=0x719 · Data length=DonÂt care · Timeout=1000 · Paged protocol={Not used} · Parameters={} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=3
- Utilisé par : *(personne)*
- Ligne export : 10673 · id 47203

#### Byte 0  `GPOUT`
- Propriétés : Input value=0x01 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`, `GFOUT-F:Generic`
- Ligne export : 10689 · id 47205

#### Byte 1  `GPOUT`
- Propriétés : Input value=0x19 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `GFOUT-D:Generic`, `GFOUT-E:Generic`, `GFOUT-F:Generic`
- Ligne export : 10700 · id 47206

#### GFOUT-F:Generic  `GFOUT`
- Propriétés : Identifier=0 · Data length=2 · Send method=Continuously · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{Byte 0; 0}; {Byte 1; 8}} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=5
- Lit : `Byte 0`, `Byte 1`
- Utilisé par : *(personne)*
- Ligne export : 10711 · id 47207

#### SMC Wipper  `SMC`
- Propriétés : Default state name=OFF
- Fonction *INT* :
  - **Activating** = `Wipper State = 1`
- Fonction *Speed 1* :
  - **Activating** = `Wipper State = 2`
- Fonction *Speed 2* :
  - **Activating** = `Wipper State = 3`
- Lit : `Wipper State`
- Utilisé par : *(personne)*
- Ligne export : 10733 · id 47737

#### Unlock Boat  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((Remote > 0))) OR (Unlock Boat)`
- Lit : `Remote`
- Utilisé par : `Boat State`
- Ligne export : 10841 · id 48471

#### KTB Ok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `0x717`
- Utilisé par : `CanBus Error TB`, `MD4-10 page: INFO`, `MD4-10 page: SETUP`
- Ligne export : 10901 · id 53517

#### CanBus Error TB  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Keybox · Text=KTB Communication failure, reboot the system. If the problem persists, contact a service center.
- Logique :
  - **Showing** = `not(KTB Ok)`
  - **Hiding** = `KTB Ok`
- Lit : `KTB Ok`
- Utilisé par : *(personne)*
- Ligne export : 10944 · id 53466

#### CanBus 0x719  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `0x719`
- Utilisé par : `CanBus Error TC`, `MD4-10 page: INFO`, `MD4-10 page: SETUP`
- Ligne export : 10998 · id 53549

#### CanBus Error TC  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Keybox · Text=KTC Communication failure, reboot the system. If the problem persists, contact a service center.
- Logique :
  - **Showing** = `not(CanBus 0x719)`
  - **Hiding** = `CanBus 0x719`
- Lit : `CanBus 0x719`
- Utilisé par : *(personne)*
- Ligne export : 11041 · id 53481

#### CanBus 0x718  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `0x718`
- Utilisé par : `CanBus Error BB`, `MD4-10 page: INFO`, `MD4-10 page: SETUP`
- Ligne export : 11095 · id 53530

#### CanBus Error BB  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Keybox · Text=KBB Communication failure, reboot the system. If the problem persists, contact a service center.
- Logique :
  - **Showing** = `not(CanBus 0x718)`
  - **Hiding** = `CanBus 0x718`
- Lit : `CanBus 0x718`
- Utilisé par : *(personne)*
- Ligne export : 11138 · id 53502

#### Ladder Position  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Ladder Sensor: 0->0, 13000->100, Freeze)`
- Lit : `Ladder Sensor`
- Utilisé par : `Ladder Error Msg`, `Ladder is not up`, `MD4-10 page: MAIN`, `MD4-10 page: SHUTDOWN`
- Ligne export : 11192 · id 53898

#### Ladder Error Msg  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Ladder · Text=Ladder malfunction. Check sensor calibration or contact a service center. · Channel=Ladder Position [%]
- Logique :
  - **Showing** = `(Inside(Ladder Position [%], 2, 98)) AND (Stop Ladder)`
- Lit : `Ladder Position`, `Stop Ladder`
- Utilisé par : `OK Buz 2`
- Ligne export : 11239 · id 53946

#### Need Charge  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(AUX 1 and Aux 1 - Need HT) OR (AUX 2 and Aux 2 - Need HT) OR (AUX 3 and Aux 3 - if A/C Need HT) OR A/CBatPackNeedHT OR (AUX 4 and Aux 4 - Need HT) OR (AUX 5 and Aux 5 - Need HT)`
- Lit : `A/CBatPackNeedHT`, `AUX 1`, `AUX 2`, `AUX 3`, `AUX 4`, `AUX 5`, `Aux 1 - Need HT`, `Aux 2 - Need HT`, `Aux 3 - if A/C Need HT`, `Aux 4 - Need HT`, `Aux 5 - Need HT`
- Utilisé par : `Need Charge output`
- Ligne export : 11295 · id 54194

#### A/C Batt Pack?  `DP`
> Enable the dedicated A/C Li/Ion Battery for air conditionning
- Propriétés : Default mode={False}
- Utilisé par : `Aux 3 - if A/C Need HT`, `Aux 3 - if A/C Show`, `Aux 5 - if A/C Need HT`, `Aux 5 - if A/C Show`, `Active le groupe: EQUIPEMENT / A/C Aentron BatPack`, `Adjust group: Main Setup`, `Adjust group: Master A/C Bat Pack`, `Event log: A/C Bat Pack`, `MD4-10 page: FEATURE`, `Measure group: Aentron BatPack`, `Single adjust item: A/C Batt Pack?`
- Ligne export : 18275 · id 90404

#### KTB Keybox Type?  `SP`
> 1st or 2d generation of Keybox
- Propriétés : Input channel=None · Default state name=1st generation · States={2d generation}
- Utilisé par : `KTB is First Gen`, `KTB is Scd Gen`, `Keybox Gen`, `Adjust group: Config Electric Drive`, `Single adjust item: KTB Keybox Type?`
- Ligne export : 18299 · id 92647

#### KBB Keybox Type?  `SP`
> 1st or 2d generation of Keybox
- Propriétés : Input channel=None · Default state name=1st generation · States={2d generation}
- Utilisé par : `KBB is First Gen`, `KBB is Scd Gen`, `Keybox Gen`, `Adjust group: Config Electric Drive`, `Single adjust item: KBB Keybox Type?`
- Ligne export : 18311 · id 92651

#### KTC Keybox Type?  `SP`
> 1st or 2d generation of Keybox
- Propriétés : Input channel=None · Default state name=1st generation · States={2d generation}
- Utilisé par : `KTC is First Gen`, `KTC is Scd Gen`, `Keybox Gen`, `Adjust group: Config Electric Drive`, `Single adjust item: KTC Keybox Type?`
- Ligne export : 18323 · id 92656

#### KTB is First Gen  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `KTB Keybox Type? = 0`
- Lit : `KTB Keybox Type?`
- Utilisé par : `Active le groupe: EQUIPEMENT / KTB Frame 1st Gen KB`
- Ligne export : 18679 · id 92692

#### KTB is Scd Gen  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `KTB Keybox Type? = 1`
- Lit : `KTB Keybox Type?`
- Utilisé par : `Active le groupe: EQUIPEMENT / KTB Frame 2d Gen KB`
- Ligne export : 18724 · id 92707

#### KBB is First Gen  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `KBB Keybox Type? = 0`
- Lit : `KBB Keybox Type?`
- Utilisé par : `Active le groupe: EQUIPEMENT / KBB Frame 1st Gen KB`
- Ligne export : 18769 · id 93033

#### KBB is Scd Gen  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `KBB Keybox Type? = 1`
- Lit : `KBB Keybox Type?`
- Utilisé par : `Active le groupe: EQUIPEMENT / KBB Frame 2d Gen KB`
- Ligne export : 18814 · id 93041

#### KTC is First Gen  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `KTC Keybox Type? = 0`
- Lit : `KTC Keybox Type?`
- Utilisé par : `Active le groupe: EQUIPEMENT / KTC Frame 1st Gen KB`
- Ligne export : 18859 · id 93055

#### KTC is Scd Gen  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `KTC Keybox Type? = 1`
- Lit : `KTC Keybox Type?`
- Utilisé par : `Active le groupe: EQUIPEMENT / KTC Frame 2d Gen KB`
- Ligne export : 18904 · id 93063

#### Single Button Equipement?  `DP`
> Gather GPS, NMEA, Audio, VHF AIS under the same Keybox output
- Propriétés : True text=Single button · False text=Dedicated buttons · Default mode={False}
- Utilisé par : `Equipment button mode`, `Is multi button Eqt`, `Is single button Eqt`, `Adjust group: Config Options`, `Single adjust item: Single Button Equipement?`
- Ligne export : 20363 · id 93924

#### Is single button Eqt  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Single Button Equipement?`
- Lit : `Single Button Equipement?`
- Utilisé par : `VHF - Show if SIngle Button Eqt`, `Active le groupe: EQUIPEMENT / Options / Single Button Eqt Additional Options`, `Single adjust item: Aux 4 - Need HT`, `Single adjust item: Aux 4 - Show`, `Single adjust item: Aux 4 - Text`, `Single adjust item: Aux 5 - Need HT`, `Single adjust item: Aux 5 - Text`, `Single adjust item: Aux 5- Show`
- Ligne export : 20383 · id 93948

#### Is multi button Eqt  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(Single Button Equipement?)`
- Lit : `Single Button Equipement?`
- Utilisé par : `MD4-10 page: FEATURE`
- Ligne export : 20426 · id 93961

#### AUX 4  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `Aux 4 - Text`, `KTB K2 IDC - AUDIO/AUX 4`, `Need Charge`, `MD4-10 page: FEATURE`
- Ligne export : 20470 · id 94014

#### AUX 5  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `Aux 5 - Text`, `KTB K3 IDC - VHF/AUX 5`, `Need Charge`, `MD4-10 page: FEATURE`
- Ligne export : 20481 · id 94017

#### Equipment button  `TP`
- Propriétés : Mode selector=Equipment button mode · Default mode: Multi button Equipement={GPS} · Mode 1: Single Button Equipement={EQT}
- Lit : `Equipment button mode`
- Utilisé par : `MD4-10 page: FEATURE`
- Ligne export : 20492 · id 94023

#### Equipment button mode  `SMC`
- Propriétés : Default state name=Multi button Equipement
- Fonction *Single Button Equipement* :
  - **Activating** = `Single Button Equipement?`
- Lit : `Single Button Equipement?`
- Utilisé par : `Equipment button`
- Ligne export : 20505 · id 94024

#### A/C Clim KTCK12  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `A/CBatPackClimRelay AND (A/C ClimRelay KB Port = 0)`
- Lit : `A/C ClimRelay KB Port`, `A/CBatPackClimRelay`
- Utilisé par : `KTC K12 IDC - AUX 3`
- Ligne export : 20545 · id 94145

#### A/C Clim KTBK9  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `A/CBatPackClimRelay AND (A/C ClimRelay KB Port = 1)`
- Lit : `A/C ClimRelay KB Port`, `A/CBatPackClimRelay`
- Utilisé par : `KTB K9 IDC - Cockpit Light`
- Ligne export : 20597 · id 94160

## EQUIPEMENT / A/C Aentron BatPack — actif seulement si `A/C Batt Pack?`
> Additionnal battery Li-Ion Battery pack, AENTRON

#### A/CBat 1st Node ID  `IP`
> Node id of the first module of the battery pack. Second module ID is +1
- Propriétés : Default mode={20}
- Utilisé par : `A/CBat 2d Node ID`, `ID_Tx_Amp_N1`, `ID_Tx_Info_N1`, `ID_Tx_Status_N1`, `Adjust group: Master A/C Bat Pack`, `Single adjust item: A/CBat 1st Node ID`
- Ligne export : 13359 · id 90405

#### A/C Voltage High Limit  `IP`
> Max Voltage Value to allow a charge
- Propriétés : Unit=mV · Default mode={16400}
- Utilisé par : `A/C Flag High Voltage`, `Adjust group: Master A/C Bat Pack`, `Single adjust item: A/C Voltage High Limit`
- Ligne export : 13371 · id 90997

#### A/C SOC Memory  `MEM`
> Store a new SOC Value if different AND realistic
- Propriétés : Input channel=A/CBatPack SOC [%] · Action=Replace · Store value=Yes · Reset value=-1
- Logique :
  - **Activating** = `((Abs((A/CBatPack SOC [%] - A/C SOC Memory [%]))) >= 1) AND A/CBatPackSOCTrigger`
- Lit : `A/CBatPack SOC`, `A/CBatPackSOCTrigger`
- Utilisé par : `A/C Flag End Of Charge`, `A/C User SOC`, `Enable A/C StartCharge`, `Measure group: Aentron BatPack`
- Ligne export : 13383 · id 90957

#### A/C Override Volt Limits  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `A/C Flag Float Voltage`, `A/C Flag High Voltage`, `A/C Flag Low Voltage`, `Adjust group: Master A/C Bat Pack`, `Single adjust item: A/C Override Volt Limits`
- Ligne export : 13453 · id 91492

#### A/C Voltage Memory  `MEM`
> Store a new voltage when it significantly change
- Propriétés : Input channel=A/CBatPack Voltage [mV] · Action=Replace · Store value=Yes · Reset value=0
- Logique :
  - **Activating** = `((Abs((A/CBatPack Voltage [mV] - A/C Voltage Memory [mV]))) >= 10) AND A/CBatPackSOCTrigger`
- Lit : `A/CBatPack Voltage`, `A/CBatPackSOCTrigger`
- Utilisé par : `A/C Flag Float Voltage`, `A/C Flag High Voltage`, `A/C Flag Low Voltage`, `A/C Voltage to display`, `Measure group: Aentron BatPack`
- Ligne export : 13466 · id 91645

#### A/C Flag High Voltage  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=300
- Logique :
  - **Activating** = `(A/C Voltage Memory [mV] >= A/C Voltage High Limit [mV]) OR (A/CBatPack Status = 6)`
  - **Blocking** = `A/C Override Volt Limits`
- Lit : `A/C Override Volt Limits`, `A/C Voltage High Limit`, `A/C Voltage Memory`, `A/CBatPack Status`
- Utilisé par : `Enable A/C StartCharge`
- Ligne export : 13536 · id 91290

#### A/C Voltage Low Limit  `IP`
> Lowest Voltage to allow the use of the A/C
- Propriétés : Unit=mV · Default mode={12050}
- Utilisé par : `A/C Flag Low Voltage`, `Adjust group: Master A/C Bat Pack`, `Single adjust item: A/C Voltage Low Limit`
- Ligne export : 13597 · id 91014

#### A/C Flag Low Voltage  `IDC`
> Raise a flag in SOC Low to automatically disable the A/C
- Propriétés : Toggle=No · Delay on=2500 · Delay off=300
- Logique :
  - **Activating** = `((A/C Voltage Memory [mV] <= A/C Voltage Low Limit [mV]) and (A/C Voltage Memory [mV] > 2)) OR (A/CBatPack Status = 5)`
  - **Blocking** = `A/C Override Volt Limits`
- Lit : `A/C Override Volt Limits`, `A/C Voltage Low Limit`, `A/C Voltage Memory`, `A/CBatPack Status`
- Utilisé par : `A/C Flag Float Voltage`, `A/C Info: Low Voltage`, `A/C WatchDog`, `Enable A/C Float`, `Enable A/C Start`, `Enable A/C Start Float`, `Enable A/C Use`
- Ligne export : 13609 · id 91015

#### A/C Override Tracks Up  `DP`
> Force the use of A/C with tracks Down
- Propriétés : Default mode={False}
- Utilisé par : `A/C In Water?`, `Adjust group: Master A/C Bat Pack`, `Single adjust item: A/C Override Tracks Up`
- Ligne export : 13688 · id 91302

#### A/C In Water?  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(not(TRACK DOWN)) OR (A/C Override Tracks Up)`
- Lit : `A/C Override Tracks Up`, `TRACK DOWN`
- Utilisé par : `Enable A/C Float`, `Enable A/C Start`, `Enable A/C Start Float`, `Enable A/C Use`
- Ligne export : 13701 · id 92068

#### A/C Voltage Float Level  `IP`
> Max Voltage Value to allow a charge
- Propriétés : Unit=mV · Default mode={12500}
- Utilisé par : `A/C Flag Float Voltage`, `Adjust group: Master A/C Bat Pack`, `Single adjust item: A/C Voltage Float Level`
- Ligne export : 13752 · id 92100

#### A/C Flag Float Voltage  `IDC`
> Raise a flag in SOC Low to automatically disable the A/C
- Propriétés : Toggle=No · Delay on=1000 · Delay off=300
- Logique :
  - **Activating** = `(A/C Voltage Memory [mV] <= A/C Voltage Float Level [mV]) AND (A/C Voltage Memory [mV] > 2)`
  - **Blocking** = `(A/C Flag Low Voltage) OR (A/C Override Volt Limits)`
- Lit : `A/C Flag Low Voltage`, `A/C Override Volt Limits`, `A/C Voltage Float Level`, `A/C Voltage Memory`
- Utilisé par : `Enable A/C Start`, `Enable A/C Start Float`
- Ligne export : 13764 · id 92111

#### Enable A/C Start Float  `IDC`
> Voltage Lower than Float Voltage and tracks Up
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(A/C In Water?) AND (A/C Flag Float Voltage)`
  - **Blocking** = `(Flag NoAUX Mode MD4) OR (A/C Flag Low Voltage)`
- Lit : `A/C Flag Float Voltage`, `A/C Flag Low Voltage`, `A/C In Water?`, `Flag NoAUX Mode MD4`
- Utilisé par : `A/C Bat Pack State Machine`, `A/C Enable Button`
- Ligne export : 13832 · id 91876

#### A/C Flag Error  `IDC`
> Flag when AETRON Batpack rises an error
- Propriétés : Toggle=No · Delay on=500 · Delay off=1000
- Logique :
  - **Activating** = `(A/CBatPack Status = 2) OR (A/CBatPack Status = 3)`
  - **Blocking** = `not(A/CBatPack CAN OK)`
- Lit : `A/CBatPack CAN OK`, `A/CBatPack Status`
- Utilisé par : `A/C Reboot Request`, `A/CBatPackMode`, `Event log: A/C Bat Pack`
- Ligne export : 13896 · id 91353

#### A/C Bat Pack State Machine  `FSM`
- Propriétés : Store value=No · Resetting channel=A/CBatPack Reset
- État 0 **Off** — The helm is Off, reset state of the Bat Pack
  - transition *Init Bat Pack* — Initiate the BatPack when helm is turned on (état cible non exporté par IQANdesign)
    - **Activating** = `(not(Power Down)) AND (not(A/C Reboot Request))`
- État 1 **Stand-By** — Clim is off and boat is unplugged
  - transition *climOff_startCharge* — Clim is Off and boat start charging (état cible non exporté par IQANdesign)
    - **Activating** = `Enable A/C StartCharge`
  - transition *startClim_chargeOff* — Press MD4 And Tracks Up (état cible non exporté par IQANdesign)
    - **Activating** = `(A/C User Ask) AND (Enable A/C Start)`
- État 2 **Stand-By Charging** — Clim is Off but battery is charging
  - transition *startClim_chargeRun* — Press MD4 and boat is in water // Boat is charging (état cible non exporté par IQANdesign)
    - **Activating** = `(A/C User Ask) AND (Enable A/C Start)`
  - transition *climOff_endCharge* — End of charge (état cible non exporté par IQANdesign)
    - **Activating** = `Enable A/C StopCharge`
- État 3 **On** — Clim is On and boat is unplugged
  - transition *climRun_startCharge* — Start charging while clim is running (état cible non exporté par IQANdesign)
    - **Activating** = `Enable A/C StartCharge`
  - transition *endClim_chargeOff* — Unpress MD4 Or Tracks down (état cible non exporté par IQANdesign)
    - **Activating** = `(not(Enable A/C Use)) OR (not(A/C User Ask))`
  - transition *startFloat* (état cible non exporté par IQANdesign)
    - **Activating** = `(A/C User Ask) AND (Enable A/C Start Float)`
- État 4 **On Charging** — Clim is on AND boat is plugged and charging
  - transition *climRun_endCharge* — Ending Charge while clim is still running (état cible non exporté par IQANdesign)
    - **Activating** = `Enable A/C StopCharge`
  - transition *endClim_chargeRun* — Press MD4 or boat goes out water // Boat is charging (état cible non exporté par IQANdesign)
    - **Activating** = `(not(Enable A/C Use)) OR (not(A/C User Ask))`
- État 5 **On Floating** — A/C On supported by HT battery
  - transition *endClim_Float* (état cible non exporté par IQANdesign)
    - **Activating** = `(not(A/C User Ask)) OR (not(Enable A/C Float))`
  - transition *Floating_Start Charge* (état cible non exporté par IQANdesign)
    - **Activating** = `Enable A/C StartCharge`
- Lit : `A/C Reboot Request`, `A/C User Ask`, `A/CBatPack Reset`, `Enable A/C Float`, `Enable A/C Start`, `Enable A/C Start Float`, `Enable A/C StartCharge`, `Enable A/C StopCharge`, `Enable A/C Use`, `Power Down`
- Utilisé par : `A/C Flag End Of Charge`, `A/C Reboot Request`, `A/C WatchDog`, `A/CBatPackClimRelay`, `A/CBatPackDCDCRelay`, `A/CBatPackESwitchRelay`, `A/CBatPackNeedHT`, `Measure group: Aentron BatPack`
- Ligne export : 13958 · id 90735

#### A/CBatPackRelay  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `A/CBatPack Relay Status = 3`
- Lit : `A/CBatPack Relay Status`
- Utilisé par : `A/C Flag Charging`, `A/C Flag Floating`, `A/C WatchDog`, `A/CBatPackClimRelay`
- Ligne export : 14397 · id 91330

#### A/C Reboot Request  `IDC`
> Ask for a reboot of the system
- Propriétés : Toggle=No · Delay on=0 · Delay off=5000
- Logique :
  - **Activating** = `(A/C Flag Error) OR (A/C WatchDog)`
  - **Blocking** = `A/C Bat Pack State Machine = 0`
- Lit : `A/C Bat Pack State Machine`, `A/C Flag Error`, `A/C WatchDog`
- Utilisé par : `A/C Bat Pack State Machine`, `A/C Error Several Reboot`, `A/C Reboot Counter`, `A/C Warning: Reboot`, `A/C WatchDog`, `A/CBatPack Reset`
- Ligne export : 14442 · id 91308

#### A/C Mute Watchdog  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `A/C WatchDog`, `Adjust group: Master A/C Bat Pack`, `Single adjust item: A/C Mute Watchdog`
- Ligne export : 14501 · id 91478

#### A/C WatchDog  `IDC`
> Check for System error for each mode to ask for a reboot
- Propriétés : Toggle=No · Delay on=5000 · Delay off=0 · Function selector=A/C Bat Pack State Machine
- Fonction *Off* : (vide)
- Fonction *Stand-By* :
  - **Activating** = `A/CBatPackRelay`
  - **Blocking** = `(A/C Reboot Request) OR (A/C Mute Watchdog)`
- Fonction *Stand-By Charging* :
  - **Activating** = `not(A/CBatPackRelay) OR (not(Battery Drive Mode))`
  - **Blocking** = `(A/C Reboot Request) OR (A/C Mute Watchdog)`
- Fonction *On* :
  - **Activating** = `not(A/CBatPackRelay) OR (A/C Flag Low Voltage)`
  - **Blocking** = `(A/C Reboot Request) OR (A/C Mute Watchdog)`
- Fonction *On Charging* :
  - **Activating** = `not(A/CBatPackRelay) OR (not(Battery Drive Mode)) OR (A/C Flag Low Voltage)`
  - **Blocking** = `(A/C Reboot Request) OR (A/C Mute Watchdog)`
- Fonction *On Floating* :
  - **Activating** = `not(A/CBatPackRelay) OR (not(Battery Drive Mode)) OR (A/C Flag Low Voltage)`
  - **Blocking** = `(A/C Reboot Request) OR (A/C Mute Watchdog)`
- Lit : `A/C Bat Pack State Machine`, `A/C Flag Low Voltage`, `A/C Mute Watchdog`, `A/C Reboot Request`, `A/CBatPackRelay`, `Battery Drive Mode`
- Utilisé par : `A/C Reboot Request`
- Ligne export : 14514 · id 91929

#### A/C User Reset  `IDC`
> Reset Toggle switch in case of shutdown of the boat
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `NegativeFlank(A/CBatPackClimRelay) OR (A/C Start Disabled?)`
- Lit : `A/C Start Disabled?`, `A/CBatPackClimRelay`
- Utilisé par : `A/C User Ask`
- Ligne export : 14824 · id 90915

#### A/C User Ask  `VDIN`
- Propriétés : Toggle=Yes · Resetting channel=A/C User Reset · Store value=No
- Lit : `A/C User Reset`
- Utilisé par : `A/C Bat Pack State Machine`, `A/C Start Disabled?`, `MD4-10 page: FEATURE`
- Ligne export : 14875 · id 90894

#### Enable A/C Use  `IDC`
> 500ms delay Off Allows floating state to be enabled
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `A/C In Water?`
  - **Blocking** = `A/C Flag Low Voltage`
- Lit : `A/C Flag Low Voltage`, `A/C In Water?`
- Utilisé par : `A/C Bat Pack State Machine`, `A/C Enable Button`
- Ligne export : 14886 · id 90897

#### A/C MinSOCforStartCharging  `IP`
- Propriétés : Unit=% · Default mode={90}
- Utilisé par : `Enable A/C StartCharge`, `Adjust group: Master A/C Bat Pack`, `Single adjust item: A/C MinSOCforStartCharging`
- Ligne export : 14936 · id 92004

#### Enable A/C StartCharge  `IDC`
> Trigger the DCDC Relay based on charger state delay on take into account HT battery precharge
- Propriétés : Toggle=No · Delay on=1500 · Delay off=0
- Logique :
  - **Activating** = `(Charger Charging State = 3) OR (Charger Charging State = 4)`
  - **Blocking** = `(A/C SOC Memory [%] > A/C MinSOCforStartCharging [%]) OR (A/C Flag High Voltage)`
- Lit : `A/C Flag High Voltage`, `A/C MinSOCforStartCharging`, `A/C SOC Memory`, `Charger Charging State`
- Utilisé par : `A/C Bat Pack State Machine`
- Ligne export : 14948 · id 90974

#### A/CBatPack Reset  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(A/C Reboot Request) OR (Power Down)`
- Lit : `A/C Reboot Request`, `Power Down`
- Utilisé par : `A/C Bat Pack State Machine`
- Ligne export : 15018 · id 91996

#### A/C Flag End Of Charge  `IDC`
- Propriétés : Toggle=No · Delay on=600000 · Delay off=3000
- Logique :
  - **Activating** = `((A/C Bat Pack State Machine = 2) and (A/CBatPack Current [A] < 2)) OR (A/C SOC Memory [%] >= A/C MaxSOCforEndCharging [%])`
- Lit : `A/C Bat Pack State Machine`, `A/C MaxSOCforEndCharging`, `A/C SOC Memory`, `A/CBatPack Current`
- Utilisé par : `Enable A/C StopCharge`
- Ligne export : 15068 · id 91978

#### Enable A/C StopCharge  `IDC`
> Trigger the DCDC Relay based on charger state delay on take into account HT battery precharge
- Propriétés : Toggle=No · Delay on=1500 · Delay off=0
- Logique :
  - **Activating** = `(Charger Charging State > 4) OR (Charger Charging State < 3) OR (A/C Flag End Of Charge)`
- Lit : `A/C Flag End Of Charge`, `Charger Charging State`
- Utilisé par : `A/C Bat Pack State Machine`
- Ligne export : 15140 · id 92019

#### Enable A/C Start  `IDC`
> Voltage Higher than Float voltage and tracks are up
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `A/C In Water?`
  - **Blocking** = `(A/C Flag Float Voltage) OR (A/C Flag Low Voltage)`
- Lit : `A/C Flag Float Voltage`, `A/C Flag Low Voltage`, `A/C In Water?`
- Utilisé par : `A/C Bat Pack State Machine`, `A/C Enable Button`, `A/C Start Disabled?`
- Ligne export : 15201 · id 92144

#### Enable A/C Float  `IDC`
> Voltage Lower than Float Voltage and tracks Up
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `A/C In Water?`
  - **Blocking** = `(Flag NoAUX Mode MD4) OR (A/C Flag Low Voltage)`
- Lit : `A/C Flag Low Voltage`, `A/C In Water?`, `Flag NoAUX Mode MD4`
- Utilisé par : `A/C Bat Pack State Machine`
- Ligne export : 15258 · id 92292

#### A/CBatPackClimRelay  `IDC`
> Triggers the main clim Relay (Aux 3 KTC)
- Propriétés : Toggle=No · Delay on=4000 · Delay off=0
- Logique :
  - **Activating** = `A/C Bat Pack State Machine >= 3`
  - **Blocking** = `not(A/CBatPackRelay)`
- Lit : `A/C Bat Pack State Machine`, `A/CBatPackRelay`
- Utilisé par : `A/C Clim KTBK9`, `A/C Clim KTCK12`, `A/C User Reset`
- Ligne export : 15315 · id 90871

#### A/C Start Disabled?  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank(A/C User Ask)) AND (not(Enable A/C Start))`
- Lit : `A/C User Ask`, `Enable A/C Start`
- Utilisé par : `A/C Info: Start Disabled`, `A/C User Reset`
- Ligne export : 15368 · id 92390

#### A/C MaxSOCforEndCharging  `IP`
- Propriétés : Unit=% · Default mode={99}
- Utilisé par : `A/C Flag End Of Charge`, `Adjust group: Master A/C Bat Pack`, `Single adjust item: A/C MaxSOCforEndCharging`
- Ligne export : 15420 · id 92041

#### A/C Reboot Counter  `ECNT`
> Number of reboot during a session (Boat On)
- Propriétés : Store value=No · Reset value=5
- Logique :
  - **Decreasing** = `PositiveFlank(A/C Reboot Request)`
- Lit : `A/C Reboot Request`
- Utilisé par : `A/C Error Several Reboot`, `A/C Warning: Reboot`
- Ligne export : 15432 · id 91375

#### A/CBatPackESwitchRelay  `IDC`
> Triggers E switch (Aux A KTC)
- Propriétés : Toggle=No · Delay on=50 · Delay off=4000
- Logique :
  - **Activating** = `A/C Bat Pack State Machine >= 2`
- Lit : `A/C Bat Pack State Machine`
- Utilisé par : `KTC K6 IDC - Aux A`, `Active le groupe: EQUIPEMENT / A/C Aentron BatPack / BatPackSync`, `Event log: A/C Bat Pack`
- Ligne export : 15484 · id 90666

#### A/CBatPackDCDCRelay  `IDC`
> Triggers the DCDC (Aux B KTC)
- Propriétés : Toggle=No · Delay on=1000 · Delay off=300
- Logique :
  - **Activating** = `(A/C Bat Pack State Machine = 2) OR (A/C Bat Pack State Machine = 4) OR (A/C Bat Pack State Machine = 5)`
  - **Blocking** = `not(Battery Drive Mode)`
- Lit : `A/C Bat Pack State Machine`, `Battery Drive Mode`
- Utilisé par : `A/C Flag Charging`, `A/C Flag Floating`, `KTC K7 IDC - Aux B`
- Ligne export : 15529 · id 90684

#### A/C Flag Charging  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=300
- Logique :
  - **Activating** = `(A/CBatPack CAN OK) AND A/CBatPackRelay AND A/CBatPackDCDCRelay AND (A/CBatPack Current [A] > 3)`
- Lit : `A/CBatPack CAN OK`, `A/CBatPack Current`, `A/CBatPackDCDCRelay`, `A/CBatPackRelay`
- Utilisé par : `A/CBatPackMode`
- Ligne export : 17224 · id 92470

#### A/CBatPackMode  `SMC`
- Propriétés : Default state name=Steady
- Fonction *Error* :
  - **Activating** = `(A/C Flag Error) AND (A/CBatPack CAN OK)`
- Fonction *Charging* :
  - **Activating** = `A/C Flag Charging`
  - **Blocking** = `A/C Flag Error`
- Lit : `A/C Flag Charging`, `A/C Flag Error`, `A/CBatPack CAN OK`
- Utilisé par : `A/CBatteryState`
- Ligne export : 17290 · id 91570

#### A/C SOC Top Limit  `IP`
> Adaptation of SOC Value for DCDC voltage range
- Propriétés : Unit=% · Default mode={49}
- Utilisé par : `A/C User SOC`, `Adjust group: Master A/C Bat Pack`, `Single adjust item: A/C SOC Top Limit`
- Ligne export : 17375 · id 91833

#### A/C User SOC  `IMAC`
> SOC for presentation to user
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `courbe(A/C SOC Memory [%]: {{0; 0}; {A/C SOC Top Limit [%]; 100}}, Freeze)`
- Lit : `A/C SOC Memory`, `A/C SOC Top Limit`
- Utilisé par : `A/CBatterySOC`
- Ligne export : 17387 · id 91684

#### A/C Voltage to display  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `A/C Voltage Memory [mV] / 1000`
- Lit : `A/C Voltage Memory`
- Utilisé par : `MD4-10 page: FEATURE`
- Ligne export : 17760 · id 91709

#### A/CBatPackNeedHT  `IDC`
> Ask for HT support for floting state
- Propriétés : Toggle=No · Delay on=0 · Delay off=1000
- Logique :
  - **Activating** = `A/C Bat Pack State Machine = 5`
- Lit : `A/C Bat Pack State Machine`
- Utilisé par : `A/C Info: End Floating`, `A/C Info: Floating`, `Need Charge`
- Ligne export : 17804 · id 91856

#### A/C Enable Button  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Enable A/C Start Float) OR (Enable A/C Use) OR (Enable A/C Start)`
- Lit : `Enable A/C Start`, `Enable A/C Start Float`, `Enable A/C Use`
- Utilisé par : `MD4-10 page: FEATURE`
- Ligne export : 17849 · id 92089

#### A/C Flag Floating  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=300
- Logique :
  - **Activating** = `A/CBatPackDCDCRelay AND A/CBatPackRelay AND (Battery Drive Mode)`
- Lit : `A/CBatPackDCDCRelay`, `A/CBatPackRelay`, `Battery Drive Mode`
- Utilisé par : `MD4-10 page: FEATURE`
- Ligne export : 17906 · id 92226

#### A/C Warning: Reboot  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Air Conditionning · Text=A/C System raised an error and rebooted
- Logique :
  - **Showing** = `PositiveFlank(A/C Reboot Request)`
  - **Hiding** = `A/C Reboot Counter <= 0`
- Lit : `A/C Reboot Counter`, `A/C Reboot Request`
- Utilisé par : *(personne)*
- Ligne export : 17963 · id 92236

#### A/C Error Several Reboot  `CMSG`
- Propriétés : Show message=All · Dialog type=Error · Header=Air Conditionning · Text=A/C System rebooted several times. Please turn off the A/C until the next charge of the boat and contact a service center.
- Logique :
  - **Showing** = `(PositiveFlank(A/C Reboot Request)) AND (A/C Reboot Counter <= 0)`
- Lit : `A/C Reboot Counter`, `A/C Reboot Request`
- Utilisé par : *(personne)*
- Ligne export : 18019 · id 92255

#### A/C Info: Floating  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header=Air Conditionning · Text=A/C System is now supported by IMS Supply. Reduce A/C use to save IMS autonomy.
- Logique :
  - **Showing** = `PositiveFlank(A/CBatPackNeedHT)`
- Lit : `A/CBatPackNeedHT`
- Utilisé par : *(personne)*
- Ligne export : 18075 · id 92328

#### A/C Info: Low Voltage  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header=Air Conditionning · Text=The A/C is switched off due to a low state of charge
- Logique :
  - **Showing** = `PositiveFlank(A/C Flag Low Voltage)`
- Lit : `A/C Flag Low Voltage`
- Utilisé par : *(personne)*
- Ligne export : 18122 · id 92379

#### A/C Info: Start Disabled  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header=Air Conditionning · Text=Due to a low level of charge, A/C will be disabled until next charge of the boat.
- Logique :
  - **Showing** = `A/C Start Disabled?`
- Lit : `A/C Start Disabled?`
- Utilisé par : *(personne)*
- Ligne export : 18169 · id 92396

#### A/C Info: End Floating  `CMSG`
- Propriétés : Show message=All · Dialog type=Information · Header=Air Conditionning · Text=Battery SOC is Low. A/C is switched off to priorize IMS State of charge
- Logique :
  - **Showing** = `NegativeFlank(A/CBatPackNeedHT)`
- Lit : `A/CBatPackNeedHT`
- Utilisé par : *(personne)*
- Ligne export : 18215 · id 92451

#### A/C ClimRelay KB Port  `SP`
- Propriétés : Input channel=None · Default state name=KTC_K12 · States={KTB_K09}
- Utilisé par : `A/C Clim KTBK9`, `A/C Clim KTCK12`, `Adjust group: Master A/C Bat Pack`, `Single adjust item: A/C ClimRelay KB Port`
- Ligne export : 18262 · id 94083

## EQUIPEMENT / A/C Aentron BatPack / A/CSOCToShow

#### A/CBatterySOC  `FGI`
> SOC Value
- Propriétés : Unit=% · Input type=Integer · Input=A/C User SOC [%] · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `A/C User SOC`
- Utilisé par : `A/CSOCToShow`, `ScrollState`, `TargetSOC`
- Ligne export : 17454 · id 91513

#### A/CBatteryState  `FGI`
- Propriétés : Input type=State · Input=A/CBatPackMode · Default state name=Steady · States={Error; Charging}
- Lit : `A/CBatPackMode`, `State`
- Utilisé par : `A/CSOCToShow`
- Ligne export : 17468 · id 91514

#### ScrollingSOC  `SFC`
- Propriétés : Input channel=TargetSOC · Enable=Yes · Type=Slopes · Slopes={{15; 100}; {15; 100}}
- Lit : `TargetSOC`
- Utilisé par : `A/CSOCToShow`, `ScrollState`
- Ligne export : 17482 · id 91515

#### ScrollState  `FSM`
- Propriétés : Store value=No
- État 0 **ScrollUp**
  - transition *0 - 1* (état cible non exporté par IQANdesign)
    - **Activating** = `ScrollingSOC >= 100`
- État 1 **ScrollDown**
  - transition *1 - 0* (état cible non exporté par IQANdesign)
    - **Activating** = `ScrollingSOC <= A/CBatterySOC [%]`
- Lit : `A/CBatterySOC`, `ScrollingSOC`
- Utilisé par : `TargetSOC`
- Ligne export : 17500 · id 92428

#### TargetSOC  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=ScrollState
- Fonction *ScrollUp* :
  - **Controlling** = `100`
- Fonction *ScrollDown* :
  - **Controlling** = `A/CBatterySOC [%]`
- Lit : `A/CBatterySOC`, `ScrollState`
- Utilisé par : `ScrollingSOC`
- Ligne export : 17582 · id 91546

#### A/CSOCToShow  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=A/CBatteryState
- Fonction *Steady* :
  - **Controlling** = `A/CBatterySOC [%]`
- Fonction *Error* :
  - **Controlling** = `0`
- Fonction *Charging* :
  - **Controlling** = `ScrollingSOC`
- Lit : `A/CBatterySOC`, `A/CBatteryState`, `ScrollingSOC`
- Utilisé par : `MD4-10 page: FEATURE`
- Ligne export : 17655 · id 91564

## EQUIPEMENT / A/C Aentron BatPack / BatPackSync — actif seulement si `A/CBatPackESwitchRelay`
> CAN Dial with bat pack

#### SyncSignal  `GPOUT`
> Activation signal for CAN dial with Aetron BatPack
- Propriétés : Input value=0 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `SyncBatFrame`
- Ligne export : 15627 · id 90714

#### SyncBatFrame  `GFOUT`
- Propriétés : Identifier=0x80 · Data length=1 · Send method=Continuously · Transmit rate=5 · Unused bits=Set to 0 · Parameters={{SyncSignal; 0}} · Module=A/C Aentron BatPack (Generic) · Module index=0
- Lit : `SyncSignal`
- Utilisé par : *(personne)*
- Ligne export : 15638 · id 90718

#### A/CBat 2d Node ID  `IMAC`
- Logique :
  - **Controlling** = `A/CBat 1st Node ID + 1`
- Lit : `A/CBat 1st Node ID`
- Utilisé par : `ID_Tx_Amp_N2`, `ID_Tx_Info_N2`, `ID_Tx_Status_N2`
- Ligne export : 15657 · id 90812

#### ID_Tx_Status_N1  `IMAC`
> ID of status frame for N1 A/CBatPack
- Logique :
  - **Controlling** = `A/CBat 1st Node ID + 0x180`
- Lit : `A/CBat 1st Node ID`
- Utilisé par : `GFIN-A:N1_Tx_Status`
- Ligne export : 15700 · id 90820

#### GFIN-A:N1_Tx_Status  `GFIN`
- Propriétés : Identifier=ID_Tx_Status_N1 · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{N1 MMS Module State; 0}; {N1 MMS Module SOC [%]; 8}; {N1 MMS Errors; 16}; {N1 MMS Voltage [mV]; 48}} · Module=A/C Aentron BatPack (Generic) · Module index=0
- Lit : `ID_Tx_Status_N1`, `N1 MMS Errors`, `N1 MMS Module SOC`, `N1 MMS Module State`, `N1 MMS Voltage`
- Utilisé par : `A/CBatPack CAN OK`, `A/CBatPackSOCTrigger`
- Ligne export : 15743 · id 90828

#### N1 MMS Module State  `GPIN`
> State of the module
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `A/CBatPack Status`, `GFIN-A:N1_Tx_Status`
- Ligne export : 15771 · id 90829

#### N1 MMS Module SOC  `GPIN`
> SOC of the module in %
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `A/CBatPack SOC`, `GFIN-A:N1_Tx_Status`
- Ligne export : 15783 · id 90830

#### N1 MMS Errors  `GPIN`
> Error message from A/CBat
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `A/CBatPack Error Code`, `GFIN-A:N1_Tx_Status`
- Ligne export : 15795 · id 90831

#### N1 MMS Voltage  `GPIN`
> Voltage of the module
- Propriétés : Unit=mV · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `A/CBatPack Voltage`, `GFIN-A:N1_Tx_Status`
- Ligne export : 15808 · id 90832

#### ID_Tx_Status_N2  `IMAC`
> ID of status frame for N2 A/CBatPack
- Logique :
  - **Controlling** = `A/CBat 2d Node ID + 0x180`
- Lit : `A/CBat 2d Node ID`
- Utilisé par : `GFIN-B:N2_Tx_Status`
- Ligne export : 15821 · id 90833

#### GFIN-B:N2_Tx_Status  `GFIN`
- Propriétés : Identifier=ID_Tx_Status_N2 · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{N2 MMS Module State; 0}; {N2 MMS Module SOC [%]; 8}; {N2 MMS Errors; 16}; {N2 MMS Voltage [mV]; 48}} · Module=A/C Aentron BatPack (Generic) · Module index=1
- Lit : `ID_Tx_Status_N2`, `N2 MMS Errors`, `N2 MMS Module SOC`, `N2 MMS Module State`, `N2 MMS Voltage`
- Utilisé par : `A/CBatPack CAN OK`, `A/CBatPackSOCTrigger`
- Ligne export : 15864 · id 90841

#### N2 MMS Module State  `GPIN`
> State of the module
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `A/CBatPack Status`, `GFIN-B:N2_Tx_Status`
- Ligne export : 15892 · id 90842

#### N2 MMS Module SOC  `GPIN`
> SOC of the module in %
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `A/CBatPack SOC`, `GFIN-B:N2_Tx_Status`
- Ligne export : 15904 · id 90843

#### N2 MMS Errors  `GPIN`
> Error message from A/CBat
- Propriétés : Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `A/CBatPack Error Code`, `GFIN-B:N2_Tx_Status`
- Ligne export : 15916 · id 90844

#### N2 MMS Voltage  `GPIN`
> Voltage of the module
- Propriétés : Unit=mV · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian · Error value=0
- Utilisé par : `A/CBatPack Voltage`, `GFIN-B:N2_Tx_Status`
- Ligne export : 15929 · id 90845

#### A/CBatPack SOC  `IMAC`
> SOC of the A/C Battery, based on the min SOC of each module
- Propriétés : Unit=%
- Logique :
  - **Controlling** = `MinOf (Absolute)(N1 MMS Module SOC [%], N2 MMS Module SOC [%])`
- Lit : `N1 MMS Module SOC`, `N2 MMS Module SOC`
- Utilisé par : `A/C SOC Memory`, `Measure group: Aentron BatPack`
- Ligne export : 15942 · id 90846

#### A/CBatPack Status  `SMC`
> State of the Bat pack based on CAN Module state from the battery
- Propriétés : Default state name=Open
- Fonction *Connected* :
  - **Activating** = `(N1 MMS Module State = 0x01) AND (N2 MMS Module State = 0x01)`
- Fonction *Error* :
  - **Activating** = `(N1 MMS Module State = 0x80) OR (N2 MMS Module State = 0x80)`
- Fonction *Crash* :
  - **Activating** = `(N1 MMS Module State = 0x08) OR (N2 MMS Module State = 0x08)`
- Fonction *Warning* :
  - **Activating** = `(N1 MMS Module State = 0x40) OR (N2 MMS Module State = 0x40)`
- Fonction *Low Voltage* :
  - **Activating** = `(N1 MMS Module State = 0x02) OR (N2 MMS Module State = 0x02)`
- Fonction *High Voltage* :
  - **Activating** = `(N1 MMS Module State = 0x04) OR (N2 MMS Module State = 0x04)`
- Lit : `N1 MMS Module State`, `N2 MMS Module State`
- Utilisé par : `A/C Flag Error`, `A/C Flag High Voltage`, `A/C Flag Low Voltage`, `Measure group: Aentron BatPack`
- Ligne export : 15990 · id 91045

#### A/CBatPack Voltage  `IMAC`
- Propriétés : Unit=mV
- Logique :
  - **Controlling** = `MaxOf (Absolute)(N1 MMS Voltage [mV], N2 MMS Voltage [mV])`
- Lit : `N1 MMS Voltage`, `N2 MMS Voltage`
- Utilisé par : `A/C Voltage Memory`, `A/CBatPackSmoothVoltage`, `Measure group: Aentron BatPack`
- Ligne export : 16251 · id 91084

#### ID_Tx_Info_N1  `IMAC`
> ID of status frame for N1 A/CBatPack
- Logique :
  - **Controlling** = `A/CBat 1st Node ID + 0x280`
- Lit : `A/CBat 1st Node ID`
- Utilisé par : `GFIN-C:N1_Tx_Info`
- Ligne export : 16299 · id 91410

#### GFIN-C:N1_Tx_Info  `GFIN`
- Propriétés : Identifier=ID_Tx_Info_N1 · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{N1 Maximum String Cells Voltage [*0.02 Volt]; 0}; {N1 Minimum String Cells Voltage [*0.02 Volt]; 8}; {N1 MMS SOH [%]; 24}; {N1 Maximum Module Temperature [Â°C]; 32}; {N1 Module Relay Status; 56}} · Module=A/C Aentron BatPack (Generic) · Module index=2
- Lit : `C`, `ID_Tx_Info_N1`, `N1 MMS SOH`, `N1 Maximum Module Temperature`, `N1 Maximum String Cells Voltage`, `N1 Minimum String Cells Voltage`, `N1 Module Relay Status`
- Utilisé par : *(personne)*
- Ligne export : 16342 · id 91099

#### N1 Maximum String Cells Voltage  `GPIN`
> Max Cell Voltage of N1
- Propriétés : Unit=*0.02 Volt · Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `A/CBatPack N1 Voltage Balance`, `GFIN-C:N1_Tx_Info`
- Ligne export : 16373 · id 91090

#### N1 Minimum String Cells Voltage  `GPIN`
> Min Cell Voltage of N1
- Propriétés : Unit=*0.02 Volt · Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `A/CBatPack N1 Voltage Balance`, `GFIN-C:N1_Tx_Info`
- Ligne export : 16385 · id 91092

#### N1 MMS SOH  `GPIN`
> N1 State of Health calculation
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-C:N1_Tx_Info`
- Ligne export : 16397 · id 91094

#### N1 Maximum Module Temperature  `GPIN`
> Max Temp
- Propriétés : Unit=Â°C · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `A/CBatPack Temp`, `GFIN-C:N1_Tx_Info`
- Ligne export : 16409 · id 91096

#### N1 Module Relay Status  `GPIN`
> Feed back on N1 Relay Status 1: Close, 0: Open
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `A/CBatPack Relay Status`, `GFIN-C:N1_Tx_Info`
- Ligne export : 16421 · id 91098

#### ID_Tx_Info_N2  `IMAC`
> ID of status frame for N2 A/CBatPack
- Logique :
  - **Controlling** = `A/CBat 2d Node ID + 0x280`
- Lit : `A/CBat 2d Node ID`
- Utilisé par : `GFIN-D:N2_Tx_Info`
- Ligne export : 16433 · id 91429

#### GFIN-D:N2_Tx_Info  `GFIN`
- Propriétés : Identifier=ID_Tx_Info_N2 · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{N2 Maximum String Cells Voltage [*0.02 Volt]; 0}; {N2 Minimum String Cells Voltage [*0.02 Volt]; 8}; {N2 MMS SOH [%]; 24}; {N2 Maximum Module Temperature [Â°C]; 32}; {N2 Module Relay Status; 56}} · Module=A/C Aentron BatPack (Generic) · Module index=3
- Lit : `C`, `ID_Tx_Info_N2`, `N2 MMS SOH`, `N2 Maximum Module Temperature`, `N2 Maximum String Cells Voltage`, `N2 Minimum String Cells Voltage`, `N2 Module Relay Status`
- Utilisé par : *(personne)*
- Ligne export : 16476 · id 91111

#### N2 Maximum String Cells Voltage  `GPIN`
> Max Cell Voltage of N2
- Propriétés : Unit=*0.02 Volt · Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `A/CBatPack N2 Voltage Balance`, `GFIN-D:N2_Tx_Info`
- Ligne export : 16507 · id 91106

#### N2 Minimum String Cells Voltage  `GPIN`
> Min Cell Voltage of N2
- Propriétés : Unit=*0.02 Volt · Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `A/CBatPack N2 Voltage Balance`, `GFIN-D:N2_Tx_Info`
- Ligne export : 16519 · id 91107

#### N2 MMS SOH  `GPIN`
> N2 State of Health calculation
- Propriétés : Unit=% · Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `GFIN-D:N2_Tx_Info`
- Ligne export : 16531 · id 91108

#### N2 Maximum Module Temperature  `GPIN`
> Max Temp for N2
- Propriétés : Unit=Â°C · Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `A/CBatPack Temp`, `GFIN-D:N2_Tx_Info`
- Ligne export : 16543 · id 91109

#### N2 Module Relay Status  `GPIN`
> Feed back on N2 Relay Status 1: Close, 0: Open
- Propriétés : Length=1 Byte (= 8 bits) · Type=Signed integer · Error value=0
- Utilisé par : `A/CBatPack Relay Status`, `GFIN-D:N2_Tx_Info`
- Ligne export : 16555 · id 91110

#### A/CBatPack N1 Voltage Balance  `MAC`
> Max voltage difference for N1 cells
- Propriétés : Unit=V · Limiting object group=Unsigned
- Logique :
  - **Controlling** = `(N1 Maximum String Cells Voltage [*0.02 Volt] * 0,02) - (N1 Minimum String Cells Voltage [*0.02 Volt] * 0,02)`
- Lit : `N1 Maximum String Cells Voltage`, `N1 Minimum String Cells Voltage`
- Utilisé par : `Measure group: Aentron BatPack`
- Ligne export : 16567 · id 91112

#### A/CBatPack Temp  `MAC`
- Propriétés : Unit=Â° · Limiting object group=Signed
- Logique :
  - **Controlling** = `MaxOf (Absolute)(N1 Maximum Module Temperature [Â°C], N2 Maximum Module Temperature [Â°C])`
- Lit : `N1 Maximum Module Temperature`, `N2 Maximum Module Temperature`
- Utilisé par : `Measure group: Aentron BatPack`
- Ligne export : 16629 · id 91183

#### A/CBatPack N2 Voltage Balance  `MAC`
> Max voltage difference for N2 cells
- Propriétés : Unit=V · Limiting object group=Unsigned
- Logique :
  - **Controlling** = `(N2 Maximum String Cells Voltage [*0.02 Volt] * 0,02) - (N2 Minimum String Cells Voltage [*0.02 Volt] * 0,02)`
- Lit : `N2 Maximum String Cells Voltage`, `N2 Minimum String Cells Voltage`
- Utilisé par : `Measure group: Aentron BatPack`
- Ligne export : 16678 · id 91202

#### A/CBatPack Relay Status  `SMC`
- Propriétés : Default state name=Full Open
- Fonction *N1 Closed* :
  - **Activating** = `(N1 Module Relay Status = 0x01) AND (N2 Module Relay Status = 0x00)`
- Fonction *N2 Closed* :
  - **Activating** = `(N1 Module Relay Status = 0x00) AND (N2 Module Relay Status = 0x01)`
- Fonction *Full Closed* :
  - **Activating** = `(N1 Module Relay Status = 0x01) AND (N2 Module Relay Status = 0x01)`
- Lit : `N1 Module Relay Status`, `N2 Module Relay Status`
- Utilisé par : `A/CBatPackRelay`
- Ligne export : 16740 · id 91219

#### ID_Tx_Amp_N1  `IMAC`
> ID of status frame for N1 A/CBatPack
- Logique :
  - **Controlling** = `A/CBat 1st Node ID + 0x480`
- Lit : `A/CBat 1st Node ID`
- Utilisé par : `GFIN-E:N1_Tx_Amp`
- Ligne export : 16875 · id 91448

#### GFIN-E:N1_Tx_Amp  `GFIN`
> Current From N1
- Propriétés : Identifier=ID_Tx_Amp_N1 · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{N1 MMS Current [*0.03125 A]; 40}} · Module=A/C Aentron BatPack (Generic) · Module index=4
- Lit : `ID_Tx_Amp_N1`, `N1 MMS Current`
- Utilisé par : *(personne)*
- Ligne export : 16918 · id 91242

#### N1 MMS Current  `GPIN`
> Current from N1
- Propriétés : Unit=*0.03125 A · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `A/CBatPack Current`, `GFIN-E:N1_Tx_Amp`
- Ligne export : 16937 · id 91241

#### ID_Tx_Amp_N2  `IMAC`
> ID of status frame for N2 A/CBatPack
- Logique :
  - **Controlling** = `A/CBat 2d Node ID + 0x480`
- Lit : `A/CBat 2d Node ID`
- Utilisé par : `GFIN-F:N2_Tx_Amp`
- Ligne export : 16950 · id 91467

#### GFIN-F:N2_Tx_Amp  `GFIN`
> Current From N2
- Propriétés : Identifier=ID_Tx_Amp_N2 · Data length=DonÂt care · Paged protocol={Not used} · Parameters={{N2 MMS Current [*0.03125 A]; 40}} · Module=A/C Aentron BatPack (Generic) · Module index=5
- Lit : `ID_Tx_Amp_N2`, `N2 MMS Current`
- Utilisé par : *(personne)*
- Ligne export : 16993 · id 91246

#### N2 MMS Current  `GPIN`
> Current from N1
- Propriétés : Unit=*0.03125 A · Length=2 Bytes (= 16 bits) · Type=Signed integer · Byte order=Little-endian · Error value=0
- Utilisé par : `A/CBatPack Current`, `GFIN-F:N2_Tx_Amp`
- Ligne export : 17012 · id 91245

#### A/CBatPack Current  `MAC`
- Propriétés : Unit=A · Limiting object group=Signed
- Logique :
  - **Controlling** = `(N1 MMS Current [*0.03125 A] * 0,03125) + (N2 MMS Current [*0.03125 A] * 0,03125)`
- Lit : `N1 MMS Current`, `N2 MMS Current`
- Utilisé par : `A/C Flag Charging`, `A/C Flag End Of Charge`, `Measure group: Aentron BatPack`
- Ligne export : 17025 · id 91247

#### A/CBatPack Error Code  `TFC`
- Propriétés : Delimiter=// · Texts={{N1 MMS Errors; Value; 0}; {N2 MMS Errors; Value; 0}}
- Lit : `N1 MMS Errors`, `N2 MMS Errors`
- Utilisé par : `Event log: A/C Bat Pack`, `Measure group: Aentron BatPack`
- Ligne export : 17087 · id 91278

#### A/CBatPack CAN OK  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `GFIN-A:N1_Tx_Status OR GFIN-B:N2_Tx_Status`
- Lit : `GFIN-A:N1_Tx_Status`, `GFIN-B:N2_Tx_Status`
- Utilisé par : `A/C Flag Charging`, `A/C Flag Error`, `A/CBatPackMode`
- Ligne export : 17105 · id 91362

#### A/CBatPackSOCTrigger  `IDC`
> Used to trig the storage of a SOC level
- Propriétés : Toggle=No · Delay on=0 · Delay off=100
- Logique :
  - **Activating** = `GFIN-A:N1_Tx_Status OR GFIN-B:N2_Tx_Status`
- Lit : `GFIN-A:N1_Tx_Status`, `GFIN-B:N2_Tx_Status`
- Utilisé par : `A/C SOC Memory`, `A/C Voltage Memory`
- Ligne export : 17155 · id 91499

#### A/CBatPackSmoothVoltage  `SFC`
- Propriétés : Input channel=A/CBatPack Voltage [mV] · Enable=Yes · Type=Slopes · Slopes={{1000; 1000}; {1000; 1000}}
- Lit : `A/CBatPack Voltage`
- Utilisé par : *(personne)*
- Ligne export : 17205 · id 92306

## EQUIPEMENT / KBB Frame 1st Gen KB — actif seulement si `KBB is First Gen`
> KBB activation frame for 1st Gen Keybox

#### KBB K1 IDC - HT - UP  `FGI`
- Propriétés : Input type=Digital · Input=KBB K1 IDC - HT - UP · Default state name=Default state
- Lit : `KBB K1 IDC - HT - UP`
- Utilisé par : `K1`
- Ligne export : 18976 · id 93104

#### KBB K2 IDC - HT -DOWN  `FGI`
- Propriétés : Input type=Digital · Input=KBB K2 IDC - HT -DOWN · Default state name=Default state
- Lit : `KBB K2 IDC - HT -DOWN`
- Utilisé par : `K2`
- Ligne export : 18987 · id 93105

#### KBB K3 IDC - LD UP  `FGI`
- Propriétés : Input type=Digital · Input=KBB K3 IDC - LD UP · Default state name=Default state
- Lit : `KBB K3 IDC - LD UP`
- Utilisé par : `K3`
- Ligne export : 18998 · id 93106

#### KBB K4 IDC- LD DOWN  `FGI`
- Propriétés : Input type=Digital · Input=KBB K4 IDC- LD DOWN · Default state name=Default state
- Lit : `KBB K4 IDC- LD DOWN`
- Utilisé par : `K4`
- Ligne export : 19009 · id 93107

#### KBB K5 IDC - ANCHOR UP  `FGI`
- Propriétés : Input type=Digital · Input=KBB K5 IDC - ANCHOR UP · Default state name=Default state
- Lit : `KBB K5 IDC - ANCHOR UP`
- Utilisé par : `K5`
- Ligne export : 19020 · id 93108

#### KBB K6 IDC - ANCHOR DOWN  `FGI`
- Propriétés : Input type=Digital · Input=KBB K6 IDC - ANCHOR DOWN · Default state name=Default state
- Lit : `KBB K6 IDC - ANCHOR DOWN`
- Utilisé par : `K6`
- Ligne export : 19031 · id 93109

#### KBB K7 IDC - AUX 1  `FGI`
- Propriétés : Input type=Digital · Input=KBB K7 IDC - AUX 1 · Default state name=Default state
- Lit : `KBB K7 IDC - AUX 1`
- Utilisé par : `K7`
- Ligne export : 19042 · id 93110

#### KBB K11 IDC - DOOR  `FGI`
- Propriétés : Input type=Digital · Input=KBB K11 IDC - DOOR · Default state name=Default state
- Lit : `KBB K11 IDC - DOOR`
- Utilisé par : `K11`
- Ligne export : 19053 · id 93111

#### KBB K9 IDC - PUMP WIND  `FGI`
- Propriétés : Input type=Digital · Input=KBB K9 IDC - PUMP WIND · Default state name=Default state
- Lit : `KBB K9 IDC - PUMP WIND`
- Utilisé par : `K9`
- Ligne export : 19064 · id 93112

#### KBB K10 IDC - AUTO OFF POWER BOX  `FGI`
- Propriétés : Input type=Digital · Input=KBB K10 IDC - AUTO OFF POWER BOX · Default state name=Default state
- Lit : `KBB K10 IDC - AUTO OFF POWER BOX`
- Utilisé par : `K10`
- Ligne export : 19075 · id 93113

#### KBB K8 DC - PUMP SHOWER  `FGI`
- Propriétés : Input type=Digital · Input=KBB K8 DC - PUMP SHOWER · Default state name=Default state
- Lit : `KBB K8 DC - PUMP SHOWER`
- Utilisé par : `K8`
- Ligne export : 19086 · id 93114

#### KBB K12 IDC - BILGE  `FGI`
- Propriétés : Input type=Digital · Input=KBB K12 IDC - BILGE · Default state name=Default state
- Lit : `KBB K12 IDC - BILGE`
- Utilisé par : `K12`
- Ligne export : 19097 · id 93115

#### K1  `GPOUT`
- Propriétés : Input value=KBB K1 IDC - HT - UP · Length=1 bit · Type=Unsigned integer
- Lit : `KBB K1 IDC - HT - UP`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19108 · id 93116

#### K2  `GPOUT`
- Propriétés : Input value=KBB K2 IDC - HT -DOWN · Length=1 bit · Type=Unsigned integer
- Lit : `KBB K2 IDC - HT -DOWN`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19119 · id 93117

#### K3  `GPOUT`
- Propriétés : Input value=KBB K3 IDC - LD UP · Length=1 bit · Type=Unsigned integer
- Lit : `KBB K3 IDC - LD UP`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19130 · id 93118

#### K4  `GPOUT`
- Propriétés : Input value=KBB K4 IDC- LD DOWN · Length=1 bit · Type=Unsigned integer
- Lit : `KBB K4 IDC- LD DOWN`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19141 · id 93119

#### K5  `GPOUT`
- Propriétés : Input value=KBB K5 IDC - ANCHOR UP · Length=1 bit · Type=Unsigned integer
- Lit : `KBB K5 IDC - ANCHOR UP`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19152 · id 93120

#### K6  `GPOUT`
- Propriétés : Input value=KBB K6 IDC - ANCHOR DOWN · Length=1 bit · Type=Unsigned integer
- Lit : `KBB K6 IDC - ANCHOR DOWN`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19163 · id 93121

#### K7  `GPOUT`
- Propriétés : Input value=KBB K7 IDC - AUX 1 · Length=1 bit · Type=Unsigned integer
- Lit : `KBB K7 IDC - AUX 1`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19174 · id 93122

#### K8  `GPOUT`
- Propriétés : Input value=KBB K8 DC - PUMP SHOWER · Length=1 bit · Type=Unsigned integer
- Lit : `KBB K8 DC - PUMP SHOWER`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19185 · id 93123

#### K9  `GPOUT`
- Propriétés : Input value=KBB K9 IDC - PUMP WIND · Length=1 bit · Type=Unsigned integer
- Lit : `KBB K9 IDC - PUMP WIND`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19196 · id 93124

#### K10  `GPOUT`
- Propriétés : Input value=KBB K10 IDC - AUTO OFF POWER BOX · Length=1 bit · Type=Unsigned integer
- Lit : `KBB K10 IDC - AUTO OFF POWER BOX`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19207 · id 93125

#### K11  `GPOUT`
- Propriétés : Input value=KBB K11 IDC - DOOR · Length=1 bit · Type=Unsigned integer
- Lit : `KBB K11 IDC - DOOR`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19218 · id 93126

#### K12  `GPOUT`
- Propriétés : Input value=KBB K12 IDC - BILGE · Length=1 bit · Type=Unsigned integer
- Lit : `KBB K12 IDC - BILGE`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19229 · id 93127

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=0x218 · Data length=8 · Send method=On change · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{K1; 0}; {K2; 1}; {K3; 2}; {K4; 3}; {K5; 4}; {K6; 5}; {K7; 6}; {K8; 7}; {K9; 8}; {K10; 9}; {K11; 10}; {K12; 11}} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=0
- Lit : `K1`, `K10`, `K11`, `K12`, `K2`, `K3`, `K4`, `K5`, `K6`, `K7`, `K8`, `K9`
- Utilisé par : *(personne)*
- Ligne export : 19240 · id 93128

## EQUIPEMENT / KBB Frame 2d Gen KB — actif seulement si `KBB is Scd Gen`
> KBB activation frame for 2d Gen Keybox

#### KBB K1 IDC - HT - UP  `FGI`
- Propriétés : Input type=Digital · Input=KBB K1 IDC - HT - UP · Default state name=Default state
- Lit : `KBB K1 IDC - HT - UP`
- Utilisé par : `ON_Bits`
- Ligne export : 19906 · id 93494

#### KBB K2 IDC - HT -DOWN  `FGI`
- Propriétés : Input type=Digital · Input=KBB K2 IDC - HT -DOWN · Default state name=Default state
- Lit : `KBB K2 IDC - HT -DOWN`
- Utilisé par : `ON_Bits`
- Ligne export : 19917 · id 93495

#### KBB K3 IDC - LD UPfct  `FGI`
- Propriétés : Input type=Digital · Input=KBB K3 IDC - LD UP · Default state name=Default state
- Lit : `KBB K3 IDC - LD UP`
- Utilisé par : `ON_Bits`
- Ligne export : 19928 · id 93496

#### KBB K4 IDC- LD DOWNfct  `FGI`
- Propriétés : Input type=Digital · Input=KBB K4 IDC- LD DOWN · Default state name=Default state
- Lit : `KBB K4 IDC- LD DOWN`
- Utilisé par : `ON_Bits`
- Ligne export : 19939 · id 93497

#### KBB K5 IDC - ANCHOR UP  `FGI`
- Propriétés : Input type=Digital · Input=KBB K5 IDC - ANCHOR UP · Default state name=Default state
- Lit : `KBB K5 IDC - ANCHOR UP`
- Utilisé par : `ON_Bits`
- Ligne export : 19950 · id 93498

#### KBB K6 IDC - ANCHOR DOWN  `FGI`
- Propriétés : Input type=Digital · Input=KBB K6 IDC - ANCHOR DOWN · Default state name=Default state
- Lit : `KBB K6 IDC - ANCHOR DOWN`
- Utilisé par : `ON_Bits`
- Ligne export : 19961 · id 93499

#### KBB K7 IDC - AUX 1  `FGI`
- Propriétés : Input type=Digital · Input=KBB K7 IDC - AUX 1 · Default state name=Default state
- Lit : `KBB K7 IDC - AUX 1`
- Utilisé par : `ON_Bits`
- Ligne export : 19972 · id 93500

#### KBB K11 IDC - DOOR  `FGI`
- Propriétés : Input type=Digital · Input=KBB K11 IDC - DOOR · Default state name=Default state
- Lit : `KBB K11 IDC - DOOR`
- Utilisé par : `ON_Bits`
- Ligne export : 19983 · id 93501

#### KBB K9 IDC - PUMP WIND  `FGI`
- Propriétés : Input type=Digital · Input=KBB K9 IDC - PUMP WIND · Default state name=Default state
- Lit : `KBB K9 IDC - PUMP WIND`
- Utilisé par : `ON_Bits`
- Ligne export : 19994 · id 93502

#### KBB K10 IDC - AUTO OFF POWER BOX  `FGI`
- Propriétés : Input type=Digital · Input=KBB K10 IDC - AUTO OFF POWER BOX · Default state name=Default state
- Lit : `KBB K10 IDC - AUTO OFF POWER BOX`
- Utilisé par : `ON_Bits`
- Ligne export : 20005 · id 93503

#### KBB K8 DC - PUMP SHOWER  `FGI`
- Propriétés : Input type=Digital · Input=KBB K8 DC - PUMP SHOWER · Default state name=Default state
- Lit : `KBB K8 DC - PUMP SHOWER`
- Utilisé par : `ON_Bits`
- Ligne export : 20016 · id 93504

#### KBB K12 IDC - BILGE  `FGI`
- Propriétés : Input type=Digital · Input=KBB K12 IDC - BILGE · Default state name=Default state
- Lit : `KBB K12 IDC - BILGE`
- Utilisé par : `ON_Bits`
- Ligne export : 20027 · id 93505

#### ON_Bits  `IMAC`
- Logique :
  ```qcode
  Result := KBB K1 IDC - HT - UP * 1 + KBB K2 IDC - HT -DOWN  * 2 + KBB K3 IDC - LD UPfct * 4 + KBB K4 IDC- LD DOWNfct * 8 + KBB K5 IDC - ANCHOR UP * 16 + KBB K6 IDC - ANCHOR DOWN * 32 + KBB K7 IDC - AUX 1 * 64 + KBB K8 DC - PUMP SHOWER * 128 + KBB K9 IDC - PUMP WIND * 256 + KBB K10 IDC - AUTO OFF POWER BOX * 512 + KBB K11 IDC - DOOR * 1024 + KBB K12 IDC - BILGE * 2048 + 0 * 4096
  ```
- Lit : `KBB K1 IDC - HT - UP`, `KBB K10 IDC - AUTO OFF POWER BOX`, `KBB K11 IDC - DOOR`, `KBB K12 IDC - BILGE`, `KBB K2 IDC - HT -DOWN`, `KBB K3 IDC - LD UPfct`, `KBB K4 IDC- LD DOWNfct`, `KBB K5 IDC - ANCHOR UP`, `KBB K6 IDC - ANCHOR DOWN`, `KBB K7 IDC - AUX 1`, `KBB K8 DC - PUMP SHOWER`, `KBB K9 IDC - PUMP WIND`
- Utilisé par : `OFF_Bits`, `ON_Bits_GOUT`
- Ligne export : 20038 · id 93615

#### ON_Bits_GOUT  `GPOUT`
- Propriétés : Input value=ON_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `ON_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 20056 · id 93649

#### OFF_Bits  `IMAC`
- Logique :
  ```qcode
  Result := bnot(ON_Bits) band 0x1FFF
  ```
- Lit : `ON_Bits`
- Utilisé par : `OFF_Bits_GOUT`
- Ligne export : 20068 · id 93650

#### OFF_Bits_GOUT  `GPOUT`
- Propriétés : Input value=OFF_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `OFF_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 20086 · id 93661

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=0x218 · Data length=8 · Send method=On change · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{OFF_Bits_GOUT; 0}; {ON_Bits_GOUT; 16}} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=11
- Lit : `OFF_Bits_GOUT`, `ON_Bits_GOUT`
- Utilisé par : *(personne)*
- Ligne export : 20098 · id 93662

## EQUIPEMENT / KTB Frame 1st Gen KB — actif seulement si `KTB is First Gen`
> KTB activation frame for 1st Gen Keybox

#### KTB K1 IDC - GPS_EQT  `FGI`
- Propriétés : Input type=Digital · Input=KTB K1 IDC - GPS_EQT · Default state name=Default state
- Lit : `KTB K1 IDC - GPS_EQT`
- Utilisé par : `Adress Loose`, `K1`
- Ligne export : 18362 · id 92672

#### KTB K2 IDC - AUDIO/AUX 4  `FGI`
- Propriétés : Input type=Digital · Input=KTB K2 IDC - AUDIO/AUX 4 · Default state name=Default state
- Lit : `KTB K2 IDC - AUDIO/AUX 4`
- Utilisé par : `K2`
- Ligne export : 18373 · id 92674

#### KTB K3 IDC - VHF/AUX 5  `FGI`
- Propriétés : Input type=Digital · Input=KTB K3 IDC - VHF/AUX 5 · Default state name=Default state
- Lit : `KTB K3 IDC - VHF/AUX 5`
- Utilisé par : `K3`
- Ligne export : 18384 · id 92676

#### KTB K4 IDC- Cabine  `FGI`
- Propriétés : Input type=Digital · Input=KTB K4 IDC- Cabine · Default state name=Default state
- Lit : `KTB K4 IDC- Cabine`
- Utilisé par : `K4`
- Ligne export : 18395 · id 92678

#### KTB K5 IDC - HT - 360 White  `FGI`
- Propriétés : Input type=Digital · Input=KTB K5 IDC - HT - 360 White · Default state name=Default state
- Lit : `KTB K5 IDC - HT - 360 White`
- Utilisé par : `K5`
- Ligne export : 18406 · id 92680

#### KTB K6 IDC - NAV  `FGI`
- Propriétés : Input type=Digital · Input=KTB K6 IDC - NAV · Default state name=Default state
- Lit : `KTB K6 IDC - NAV`
- Utilisé par : `K6`, `MD4-10 page: MAIN`
- Ligne export : 18417 · id 92682

#### KTB K7 IDC - HT - Spot  `FGI`
- Propriétés : Input type=Digital · Input=KTB K7 IDC - HT - Spot · Default state name=Default state
- Lit : `KTB K7 IDC - HT - Spot`
- Utilisé par : `K7`
- Ligne export : 18428 · id 92684

#### KTB K11 IDC - SearchLight  `FGI`
- Propriétés : Input type=Digital · Input=KTB K11 IDC - SearchLight · Default state name=Default state
- Lit : `KTB K11 IDC - SearchLight`
- Utilisé par : `K11`
- Ligne export : 18439 · id 92686

#### KTB K9 IDC - Cockpit Light  `FGI`
- Propriétés : Input type=Digital · Input=KTB K9 IDC - Cockpit Light · Default state name=Default state
- Lit : `KTB K9 IDC - Cockpit Light`
- Utilisé par : `K9`
- Ligne export : 18450 · id 92688

#### KTB K10 IDC - Fridge  `FGI`
- Propriétés : Input type=Digital · Input=KTB K10 IDC - Fridge · Default state name=Default state
- Lit : `KTB K10 IDC - Fridge`
- Utilisé par : `K10`
- Ligne export : 18461 · id 92689

#### KTB K8 DC - HT - DIM  `FGI`
- Propriétés : Input type=Digital · Input=KTB K8 DC - HT - DIM · Default state name=Default state
- Lit : `KTB K8 DC - HT - DIM`
- Utilisé par : `K8`
- Ligne export : 18472 · id 92690

#### KTB K12 IDC - Aux 2  `FGI`
- Propriétés : Input type=Digital · Input=KTB K12 IDC - Aux 2 · Default state name=Default state
- Lit : `KTB K12 IDC - Aux 2`
- Utilisé par : `K12`
- Ligne export : 18483 · id 92691

#### K1  `GPOUT`
- Propriétés : Input value=KTB K1 IDC - GPS_EQT · Length=1 bit · Type=Unsigned integer
- Lit : `KTB K1 IDC - GPS_EQT`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 18494 · id 92858

#### K2  `GPOUT`
- Propriétés : Input value=KTB K2 IDC - AUDIO/AUX 4 · Length=1 bit · Type=Unsigned integer
- Lit : `KTB K2 IDC - AUDIO/AUX 4`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 18505 · id 92868

#### K3  `GPOUT`
- Propriétés : Input value=KTB K3 IDC - VHF/AUX 5 · Length=1 bit · Type=Unsigned integer
- Lit : `KTB K3 IDC - VHF/AUX 5`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 18516 · id 92878

#### K4  `GPOUT`
- Propriétés : Input value=KTB K4 IDC- Cabine · Length=1 bit · Type=Unsigned integer
- Lit : `KTB K4 IDC- Cabine`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 18527 · id 92889

#### K5  `GPOUT`
- Propriétés : Input value=KTB K5 IDC - HT - 360 White · Length=1 bit · Type=Unsigned integer
- Lit : `KTB K5 IDC - HT - 360 White`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 18538 · id 92900

#### K6  `GPOUT`
- Propriétés : Input value=KTB K6 IDC - NAV · Length=1 bit · Type=Unsigned integer
- Lit : `KTB K6 IDC - NAV`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 18549 · id 92911

#### K7  `GPOUT`
- Propriétés : Input value=KTB K7 IDC - HT - Spot · Length=1 bit · Type=Unsigned integer
- Lit : `KTB K7 IDC - HT - Spot`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 18560 · id 92921

#### K8  `GPOUT`
- Propriétés : Input value=KTB K8 DC - HT - DIM · Length=1 bit · Type=Unsigned integer
- Lit : `KTB K8 DC - HT - DIM`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 18571 · id 92931

#### K9  `GPOUT`
- Propriétés : Input value=KTB K9 IDC - Cockpit Light · Length=1 bit · Type=Unsigned integer
- Lit : `KTB K9 IDC - Cockpit Light`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 18582 · id 92940

#### K10  `GPOUT`
- Propriétés : Input value=KTB K10 IDC - Fridge · Length=1 bit · Type=Unsigned integer
- Lit : `KTB K10 IDC - Fridge`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 18593 · id 92950

#### K11  `GPOUT`
- Propriétés : Input value=KTB K11 IDC - SearchLight · Length=1 bit · Type=Unsigned integer
- Lit : `KTB K11 IDC - SearchLight`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 18604 · id 92965

#### K12  `GPOUT`
- Propriétés : Input value=KTB K12 IDC - Aux 2 · Length=1 bit · Type=Unsigned integer
- Lit : `KTB K12 IDC - Aux 2`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 18615 · id 92977

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=0x217 · Data length=8 · Send method=On change · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{K1; 0}; {K2; 1}; {K3; 2}; {K4; 3}; {K5; 4}; {K6; 5}; {K7; 6}; {K8; 7}; {K9; 8}; {K10; 9}; {K11; 10}; {K12; 11}} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=10
- Lit : `K1`, `K10`, `K11`, `K12`, `K2`, `K3`, `K4`, `K5`, `K6`, `K7`, `K8`, `K9`
- Utilisé par : *(personne)*
- Ligne export : 18626 · id 92978

## EQUIPEMENT / KTB Frame 2d Gen KB — actif seulement si `KTB is Scd Gen`
> KTB activation frame for 2d Gen Keybox

#### KTB K1 IDC - GPSfct  `FGI`
- Propriétés : Input type=Digital · Input=KTB K1 IDC - GPS_EQT · Default state name=Default state
- Lit : `KTB K1 IDC - GPS_EQT`
- Utilisé par : `ON_Bits`
- Ligne export : 19664 · id 93211

#### KTB K2 IDC - AUDIO/AUX 4  `FGI`
- Propriétés : Input type=Digital · Input=KTB K2 IDC - AUDIO/AUX 4 · Default state name=Default state
- Lit : `KTB K2 IDC - AUDIO/AUX 4`
- Utilisé par : `ON_Bits`
- Ligne export : 19675 · id 93212

#### KTB K3 IDC - VHF/AUX 5  `FGI`
- Propriétés : Input type=Digital · Input=KTB K3 IDC - VHF/AUX 5 · Default state name=Default state
- Lit : `KTB K3 IDC - VHF/AUX 5`
- Utilisé par : `ON_Bits`
- Ligne export : 19686 · id 93213

#### KTB K4 IDC- Cabine  `FGI`
- Propriétés : Input type=Digital · Input=KTB K4 IDC- Cabine · Default state name=Default state
- Lit : `KTB K4 IDC- Cabine`
- Utilisé par : `ON_Bits`
- Ligne export : 19697 · id 93214

#### KTB K5 IDC - HT - 360 White  `FGI`
- Propriétés : Input type=Digital · Input=KTB K5 IDC - HT - 360 White · Default state name=Default state
- Lit : `KTB K5 IDC - HT - 360 White`
- Utilisé par : `ON_Bits`
- Ligne export : 19708 · id 93215

#### KTB K6 IDC - NAV  `FGI`
- Propriétés : Input type=Digital · Input=KTB K6 IDC - NAV · Default state name=Default state
- Lit : `KTB K6 IDC - NAV`
- Utilisé par : `ON_Bits`, `MD4-10 page: MAIN`
- Ligne export : 19719 · id 93216

#### KTB K7 IDC - HT - Spot  `FGI`
- Propriétés : Input type=Digital · Input=KTB K7 IDC - HT - Spot · Default state name=Default state
- Lit : `KTB K7 IDC - HT - Spot`
- Utilisé par : `ON_Bits`
- Ligne export : 19730 · id 93217

#### KTB K11 IDC - SearchLight  `FGI`
- Propriétés : Input type=Digital · Input=KTB K11 IDC - SearchLight · Default state name=Default state
- Lit : `KTB K11 IDC - SearchLight`
- Utilisé par : `ON_Bits`
- Ligne export : 19741 · id 93218

#### KTB K9 IDC - Cockpit Light  `FGI`
- Propriétés : Input type=Digital · Input=KTB K9 IDC - Cockpit Light · Default state name=Default state
- Lit : `KTB K9 IDC - Cockpit Light`
- Utilisé par : `ON_Bits`
- Ligne export : 19752 · id 93219

#### KTB K10 IDC - Fridge  `FGI`
- Propriétés : Input type=Digital · Input=KTB K10 IDC - Fridge · Default state name=Default state
- Lit : `KTB K10 IDC - Fridge`
- Utilisé par : `ON_Bits`
- Ligne export : 19763 · id 93220

#### KTB K8 DC - HT - DIM  `FGI`
- Propriétés : Input type=Digital · Input=KTB K8 DC - HT - DIM · Default state name=Default state
- Lit : `KTB K8 DC - HT - DIM`
- Utilisé par : `ON_Bits`
- Ligne export : 19774 · id 93221

#### KTB K12 IDC - Aux 2  `FGI`
- Propriétés : Input type=Digital · Input=KTB K12 IDC - Aux 2 · Default state name=Default state
- Lit : `KTB K12 IDC - Aux 2`
- Utilisé par : `ON_Bits`
- Ligne export : 19785 · id 93222

#### ON_Bits  `IMAC`
- Logique :
  ```qcode
  Result := KTB K1 IDC - GPSfct * 1 + KTB K2 IDC - AUDIO/AUX 4  * 2 + KTB K3 IDC - VHF/AUX 5 * 4 + KTB K4 IDC- Cabine * 8 + KTB K5 IDC - HT - 360 White * 16 + KTB K6 IDC - NAV * 32 + KTB K7 IDC - HT - Spot * 64 + KTB K8 DC - HT - DIM * 128 + KTB K9 IDC - Cockpit Light * 256 + KTB K10 IDC - Fridge * 512 + KTB K11 IDC - SearchLight * 1024 + KTB K12 IDC - Aux 2 * 2048 + 0 * 4096
  ```
- Lit : `KTB K1 IDC - GPSfct`, `KTB K10 IDC - Fridge`, `KTB K11 IDC - SearchLight`, `KTB K12 IDC - Aux 2`, `KTB K2 IDC - AUDIO/AUX 4`, `KTB K3 IDC - VHF/AUX 5`, `KTB K4 IDC- Cabine`, `KTB K5 IDC - HT - 360 White`, `KTB K6 IDC - NAV`, `KTB K7 IDC - HT - Spot`, `KTB K8 DC - HT - DIM`, `KTB K9 IDC - Cockpit Light`
- Utilisé par : `OFF_Bits`, `ON_Bits_GOUT`
- Ligne export : 19796 · id 93284

#### ON_Bits_GOUT  `GPOUT`
- Propriétés : Input value=ON_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `ON_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19814 · id 93318

#### OFF_Bits  `IMAC`
- Logique :
  ```qcode
  Result := bnot(ON_Bits) band 0x1FFF
  ```
- Lit : `ON_Bits`
- Utilisé par : `OFF_Bits_GOUT`
- Ligne export : 19826 · id 93319

#### OFF_Bits_GOUT  `GPOUT`
- Propriétés : Input value=OFF_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `OFF_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19844 · id 93330

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=0x217 · Data length=8 · Send method=On change · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{OFF_Bits_GOUT; 0}; {ON_Bits_GOUT; 16}} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=6
- Lit : `OFF_Bits_GOUT`, `ON_Bits_GOUT`
- Utilisé par : *(personne)*
- Ligne export : 19856 · id 93331

## EQUIPEMENT / KTC Frame 1st Gen KB — actif seulement si `KTC is First Gen`
> KTC activation frame for 1st Gen Keybox

#### KTC K1 IDC - Wipper On/Off  `FGI`
- Propriétés : Input type=Digital · Input=KTC K1 IDC - Wipper On/Off · Default state name=Default state
- Lit : `KTC K1 IDC - Wipper On/Off`
- Utilisé par : `K1`
- Ligne export : 19320 · id 93157

#### KTC K2 IDC - Wipper Speed  `FGI`
- Propriétés : Input type=Digital · Input=KTC K2 IDC - Wipper Speed · Default state name=Default state
- Lit : `KTC K2 IDC - Wipper Speed`
- Utilisé par : `K2`
- Ligne export : 19331 · id 93158

#### KTC K3 IDC - Seat Power  `FGI`
- Propriétés : Input type=Digital · Input=KTC K3 IDC - Seat Power · Default state name=Default state
- Lit : `KTC K3 IDC - Seat Power`
- Utilisé par : `K3`
- Ligne export : 19342 · id 93159

#### KTC K4 IDC - Water Cooling  `FGI`
- Propriétés : Input type=Digital · Input=KTC K4 IDC - Water Cooling · Default state name=Default state
- Lit : `KTC K4 IDC - Water Cooling`
- Utilisé par : `K4`
- Ligne export : 19353 · id 93160

#### KTC K5 IDC - Pump Water  `FGI`
- Propriétés : Input type=Digital · Input=KTC K5 IDC - Pump Water · Default state name=Default state
- Lit : `KTC K5 IDC - Pump Water`
- Utilisé par : `K5`
- Ligne export : 19364 · id 93161

#### KTC K6 IDC - Aux A  `FGI`
- Propriétés : Input type=Digital · Input=KTC K6 IDC - Aux A · Default state name=Default state
- Lit : `KTC K6 IDC - Aux A`
- Utilisé par : `K6`
- Ligne export : 19375 · id 93162

#### KTC K7 IDC - Aux B  `FGI`
- Propriétés : Input type=Digital · Input=KTC K7 IDC - Aux B · Default state name=Default state
- Lit : `KTC K7 IDC - Aux B`
- Utilisé par : `K7`
- Ligne export : 19386 · id 93163

#### KTC K11 IDC - OutBoard Start STBD  `FGI`
- Propriétés : Input type=Digital · Input=KTC K11 IDC - OutBoard Start STBD · Default state name=Default state
- Lit : `KTC K11 IDC - OutBoard Start STBD`
- Utilisé par : `K11`
- Ligne export : 19397 · id 93164

#### KTC K9 IDC - OutBoard On-OFF  `FGI`
- Propriétés : Input type=Digital · Input=KTC K9 IDC - OutBoard On-OFF · Default state name=Default state
- Lit : `KTC K9 IDC - OutBoard On-OFF`
- Utilisé par : `Adress Loose Auto`, `K9`
- Ligne export : 19408 · id 93165

#### KTC K10 IDC - OutBoard Start PORT  `FGI`
- Propriétés : Input type=Digital · Input=KTC K10 IDC - OutBoard Start PORT · Default state name=Default state
- Lit : `KTC K10 IDC - OutBoard Start PORT`
- Utilisé par : `K10`
- Ligne export : 19419 · id 93166

#### KTC K8 DC - Fan wind cmd  `FGI`
- Propriétés : Input type=Digital · Input=KTC K8 DC - Fan wind cmd · Default state name=Default state
- Lit : `KTC K8 DC - Fan wind cmd`
- Utilisé par : `K8`
- Ligne export : 19430 · id 93167

#### KTC K12 IDC - AUX 3  `FGI`
- Propriétés : Input type=Digital · Input=KTC K12 IDC - AUX 3 · Default state name=Default state
- Lit : `KTC K12 IDC - AUX 3`
- Utilisé par : `K12`
- Ligne export : 19441 · id 93168

#### K1  `GPOUT`
- Propriétés : Input value=KTC K1 IDC - Wipper On/Off · Length=1 bit · Type=Unsigned integer
- Lit : `KTC K1 IDC - Wipper On/Off`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19452 · id 93169

#### K2  `GPOUT`
- Propriétés : Input value=KTC K2 IDC - Wipper Speed · Length=1 bit · Type=Unsigned integer
- Lit : `KTC K2 IDC - Wipper Speed`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19463 · id 93170

#### K3  `GPOUT`
- Propriétés : Input value=KTC K3 IDC - Seat Power · Length=1 bit · Type=Unsigned integer
- Lit : `KTC K3 IDC - Seat Power`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19474 · id 93171

#### K4  `GPOUT`
- Propriétés : Input value=KTC K4 IDC - Water Cooling · Length=1 bit · Type=Unsigned integer
- Lit : `KTC K4 IDC - Water Cooling`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19485 · id 93172

#### K5  `GPOUT`
- Propriétés : Input value=KTC K5 IDC - Pump Water · Length=1 bit · Type=Unsigned integer
- Lit : `KTC K5 IDC - Pump Water`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19496 · id 93173

#### K6  `GPOUT`
- Propriétés : Input value=KTC K6 IDC - Aux A · Length=1 bit · Type=Unsigned integer
- Lit : `KTC K6 IDC - Aux A`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19507 · id 93174

#### K7  `GPOUT`
- Propriétés : Input value=KTC K7 IDC - Aux B · Length=1 bit · Type=Unsigned integer
- Lit : `KTC K7 IDC - Aux B`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19518 · id 93175

#### K8  `GPOUT`
- Propriétés : Input value=KTC K8 DC - Fan wind cmd · Length=1 bit · Type=Unsigned integer
- Lit : `KTC K8 DC - Fan wind cmd`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19529 · id 93176

#### K9  `GPOUT`
- Propriétés : Input value=KTC K9 IDC - OutBoard On-OFF · Length=1 bit · Type=Unsigned integer
- Lit : `KTC K9 IDC - OutBoard On-OFF`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19540 · id 93177

#### K10  `GPOUT`
- Propriétés : Input value=KTC K10 IDC - OutBoard Start PORT · Length=1 bit · Type=Unsigned integer
- Lit : `KTC K10 IDC - OutBoard Start PORT`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19551 · id 93178

#### K11  `GPOUT`
- Propriétés : Input value=KTC K11 IDC - OutBoard Start STBD · Length=1 bit · Type=Unsigned integer
- Lit : `KTC K11 IDC - OutBoard Start STBD`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19562 · id 93179

#### K12  `GPOUT`
- Propriétés : Input value=KTC K12 IDC - AUX 3 · Length=1 bit · Type=Unsigned integer
- Lit : `KTC K12 IDC - AUX 3`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 19573 · id 93180

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=0x219 · Data length=8 · Send method=On change · Transmit rate=500 · Unused bits=Set to 0 · Parameters={{K1; 0}; {K2; 1}; {K3; 2}; {K4; 3}; {K5; 4}; {K6; 5}; {K7; 6}; {K8; 7}; {K9; 8}; {K10; 9}; {K11; 10}; {K12; 11}} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=1
- Lit : `K1`, `K10`, `K11`, `K12`, `K2`, `K3`, `K4`, `K5`, `K6`, `K7`, `K8`, `K9`
- Utilisé par : *(personne)*
- Ligne export : 19584 · id 93181

## EQUIPEMENT / KTC Frame 2d Gen KB — actif seulement si `KTC is Scd Gen`
> KTC activation frame for 2d Gen Keybox

#### KTC K1 IDC - Wipper On/Off  `FGI`
- Propriétés : Input type=Digital · Input=KTC K1 IDC - Wipper On/Off · Default state name=Default state
- Lit : `KTC K1 IDC - Wipper On/Off`
- Utilisé par : `ON_Bits`
- Ligne export : 20148 · id 93697

#### KTC K2 IDC - Wipper Speed  `FGI`
- Propriétés : Input type=Digital · Input=KTC K2 IDC - Wipper Speed · Default state name=Default state
- Lit : `KTC K2 IDC - Wipper Speed`
- Utilisé par : `ON_Bits`
- Ligne export : 20159 · id 93698

#### KTC K3 IDC - Seat Power  `FGI`
- Propriétés : Input type=Digital · Input=KTC K3 IDC - Seat Power · Default state name=Default state
- Lit : `KTC K3 IDC - Seat Power`
- Utilisé par : `ON_Bits`
- Ligne export : 20170 · id 93699

#### KTC K4 IDC - Water Cooling  `FGI`
- Propriétés : Input type=Digital · Input=KTC K4 IDC - Water Cooling · Default state name=Default state
- Lit : `KTC K4 IDC - Water Cooling`
- Utilisé par : `ON_Bits`
- Ligne export : 20181 · id 93700

#### KTC K5 IDC - Pump Water  `FGI`
- Propriétés : Input type=Digital · Input=KTC K5 IDC - Pump Water · Default state name=Default state
- Lit : `KTC K5 IDC - Pump Water`
- Utilisé par : `ON_Bits`
- Ligne export : 20192 · id 93701

#### KTC K6 IDC - Aux A  `FGI`
- Propriétés : Input type=Digital · Input=KTC K6 IDC - Aux A · Default state name=Default state
- Lit : `KTC K6 IDC - Aux A`
- Utilisé par : `ON_Bits`
- Ligne export : 20203 · id 93702

#### KTC K7 IDC - Aux B  `FGI`
- Propriétés : Input type=Digital · Input=KTC K7 IDC - Aux B · Default state name=Default state
- Lit : `KTC K7 IDC - Aux B`
- Utilisé par : `ON_Bits`
- Ligne export : 20214 · id 93703

#### KTC K11 IDC - OutBoard Start STBD  `FGI`
- Propriétés : Input type=Digital · Input=KTC K11 IDC - OutBoard Start STBD · Default state name=Default state
- Lit : `KTC K11 IDC - OutBoard Start STBD`
- Utilisé par : `ON_Bits`
- Ligne export : 20225 · id 93704

#### KTC K9 IDC - OutBoard On-OFFfct  `FGI`
- Propriétés : Input type=Digital · Input=KTC K9 IDC - OutBoard On-OFF · Default state name=Default state
- Lit : `KTC K9 IDC - OutBoard On-OFF`
- Utilisé par : `ON_Bits`
- Ligne export : 20236 · id 93705

#### KTC K10 IDC - OutBoard Start PORT  `FGI`
- Propriétés : Input type=Digital · Input=KTC K10 IDC - OutBoard Start PORT · Default state name=Default state
- Lit : `KTC K10 IDC - OutBoard Start PORT`
- Utilisé par : `ON_Bits`
- Ligne export : 20247 · id 93706

#### KTC K8 DC - Fan wind cmd  `FGI`
- Propriétés : Input type=Digital · Input=KTC K8 DC - Fan wind cmd · Default state name=Default state
- Lit : `KTC K8 DC - Fan wind cmd`
- Utilisé par : `ON_Bits`
- Ligne export : 20258 · id 93707

#### KTC K12 IDC - AUX 3  `FGI`
- Propriétés : Input type=Digital · Input=KTC K12 IDC - AUX 3 · Default state name=Default state
- Lit : `KTC K12 IDC - AUX 3`
- Utilisé par : `ON_Bits`
- Ligne export : 20269 · id 93708

#### ON_Bits  `IMAC`
- Logique :
  ```qcode
  Result := KTC K1 IDC - Wipper On/Off * 1 + KTC K2 IDC - Wipper Speed  * 2 + KTC K3 IDC - Seat Power* 4 + KTC K4 IDC - Water Cooling * 8 + KTC K5 IDC - Pump Water * 16 + KTC K6 IDC - Aux A * 32 + KTC K7 IDC - Aux B * 64 + KTC K8 DC - Fan wind cmd * 128 + KTC K9 IDC - OutBoard On-OFFfct * 256 + KTC K10 IDC - OutBoard Start PORT * 512 + KTC K11 IDC - OutBoard Start STBD * 1024 + KTC K12 IDC - AUX 3 * 2048 + 0 * 4096
  ```
- Lit : `KTC K1 IDC - Wipper On/Off`, `KTC K10 IDC - OutBoard Start PORT`, `KTC K11 IDC - OutBoard Start STBD`, `KTC K12 IDC - AUX 3`, `KTC K2 IDC - Wipper Speed`, `KTC K3 IDC - Seat Power`, `KTC K4 IDC - Water Cooling`, `KTC K5 IDC - Pump Water`, `KTC K6 IDC - Aux A`, `KTC K7 IDC - Aux B`, `KTC K8 DC - Fan wind cmd`, `KTC K9 IDC - OutBoard On-OFFfct`
- Utilisé par : `OFF_Bits`, `ON_Bits_GOUT`
- Ligne export : 20280 · id 93770

#### ON_Bits_GOUT  `GPOUT`
- Propriétés : Input value=ON_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `ON_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 20298 · id 93804

#### OFF_Bits  `IMAC`
- Logique :
  ```qcode
  Result := bnot(ON_Bits) band 0x1FFF
  ```
- Lit : `ON_Bits`
- Utilisé par : `OFF_Bits_GOUT`
- Ligne export : 20310 · id 93805

#### OFF_Bits_GOUT  `GPOUT`
- Propriétés : Input value=OFF_Bits · Length=2 Bytes (= 16 bits) · Type=Unsigned integer · Byte order=Little-endian
- Lit : `OFF_Bits`
- Utilisé par : `GFOUT-E:Generic`
- Ligne export : 20328 · id 93816

#### GFOUT-E:Generic  `GFOUT`
- Propriétés : Identifier=0x219 · Data length=8 · Send method=On change · Transmit rate=1000 · Unused bits=Set to 0 · Parameters={{OFF_Bits_GOUT; 0}; {ON_Bits_GOUT; 16}} · Module=KEYBOX EQUIPEMENT (Generic) · Module index=12
- Lit : `OFF_Bits_GOUT`, `ON_Bits_GOUT`
- Utilisé par : *(personne)*
- Ligne export : 20340 · id 93817

## EQUIPEMENT / Options

#### Aux 1 - Show  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Adjust group: Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: Aux 1 - Show`
- Ligne export : 11398 · id 54554

#### Aux 1 - Text  `TP`
- Propriétés : Default mode={AUX 1}
- Lit : `AUX 1`
- Utilisé par : `Adjust group: Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: Aux 1 - Text`
- Ligne export : 11411 · id 54555

#### Aux 1 - Need HT  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `KBB K7 IDC - AUX 1`, `Need Charge`, `Adjust group: Config Options`, `Single adjust item: Aux 1 - Need HT`
- Ligne export : 11422 · id 54556

#### Aux 2 - Show  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Adjust group: Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: Aux 2 - Show`
- Ligne export : 11435 · id 54580

#### Aux 2 - Text  `TP`
- Propriétés : Default mode={AUX 2}
- Lit : `AUX 2`
- Utilisé par : `Adjust group: Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: Aux 2 - Text`
- Ligne export : 11448 · id 54581

#### Aux 2 - Need HT  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `KTB K12 IDC - Aux 2`, `Need Charge`, `Adjust group: Config Options`, `Single adjust item: Aux 2 - Need HT`
- Ligne export : 11459 · id 54582

#### Aux 3 - Show  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Aux 3 - if A/C Show`, `Adjust group: Config Options`, `Single adjust item: Aux 3 - Show`
- Ligne export : 11472 · id 54609

#### Aux 3 - Text  `TP`
- Propriétés : Default mode={AUX 3}
- Lit : `AUX 3`
- Utilisé par : `Adjust group: Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: Aux 3 - Text`
- Ligne export : 11485 · id 54610

#### Aux 3 - Need HT  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Aux 3 - if A/C Need HT`, `Adjust group: Config Options`, `Single adjust item: Aux 3 - Need HT`
- Ligne export : 11496 · id 54611

#### VHF - Show  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `VHF - Show if SIngle Button Eqt`, `Adjust group: Config Options`, `Single adjust item: VHF - Show`
- Ligne export : 11509 · id 55477

#### Fridge - Show  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `Adjust group: Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: Fridge - Show`
- Ligne export : 11522 · id 55478

#### Aux 3 - if A/C Show  `IDC`
> Reserve Aux 3 to A/C if there is a A/C Bat Pack
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Aux 3 - Show`
  - **Blocking** = `A/C Batt Pack?`
- Lit : `A/C Batt Pack?`, `Aux 3 - Show`
- Utilisé par : `MD4-10 page: FEATURE`
- Ligne export : 11535 · id 90926

#### Aux 3 - if A/C Need HT  `IDC`
> Reserve Aux 3 to A/C if there is a A/C Bat Pack
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Aux 3 - Need HT`
  - **Blocking** = `A/C Batt Pack?`
- Lit : `A/C Batt Pack?`, `Aux 3 - Need HT`
- Utilisé par : `KTC K12 IDC - AUX 3`, `Need Charge`
- Ligne export : 11585 · id 90932

#### VHF - Show if SIngle Button Eqt  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `VHF - Show`
  - **Blocking** = `Is single button Eqt`
- Lit : `Is single button Eqt`, `VHF - Show`
- Utilisé par : `MD4-10 page: FEATURE`
- Ligne export : 11825 · id 93972

## EQUIPEMENT / Options / Single Button Eqt Additional Options — actif seulement si `Is single button Eqt`

#### Aux 4 - Show  `DP`
> New Option for single button Eqipement (KTB07, ex Audio)
- Propriétés : Default mode={False}
- Utilisé par : `Adjust group: Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: Aux 4 - Show`
- Ligne export : 11650 · id 93939

#### Aux 4 - Text  `TP`
> New Option for single button Eqipement (KTB07, ex Audio)
- Propriétés : Default mode={AUX 4}
- Lit : `AUX 4`
- Utilisé par : `Adjust group: Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: Aux 4 - Text`
- Ligne export : 11663 · id 93940

#### Aux 4 - Need HT  `DP`
> New Option for single button Eqipement (KTB07, ex Audio)
- Propriétés : Default mode={False}
- Utilisé par : `KTB K2 IDC - AUDIO/AUX 4`, `Need Charge`, `Adjust group: Config Options`, `Single adjust item: Aux 4 - Need HT`
- Ligne export : 11674 · id 93941

#### Aux 5- Show  `DP`
> New Option for single button Eqipement (KTB08, ex VHF)
- Propriétés : Default mode={False}
- Utilisé par : `Aux 5 - if A/C Show`, `Adjust group: Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: Aux 5- Show`
- Ligne export : 11687 · id 93945

#### Aux 5 - Text  `TP`
> New Option for single button Eqipement (KTB08, ex VHF)
- Propriétés : Default mode={AUX 5}
- Lit : `AUX 5`
- Utilisé par : `Adjust group: Config Options`, `MD4-10 page: FEATURE`, `Single adjust item: Aux 5 - Text`
- Ligne export : 11700 · id 93946

#### Aux 5 - Need HT  `DP`
> New Option for single button Eqipement (KTB08, ex VHF)
- Propriétés : Default mode={False}
- Utilisé par : `Aux 5 - if A/C Need HT`, `KTB K3 IDC - VHF/AUX 5`, `Need Charge`, `Adjust group: Config Options`, `Single adjust item: Aux 5 - Need HT`
- Ligne export : 11711 · id 93947

#### Aux 5 - if A/C Show  `IDC`
> Reserve Aux 3 to A/C if there is a A/C Bat Pack
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Aux 5- Show`
  - **Blocking** = `A/C Batt Pack?`
- Lit : `A/C Batt Pack?`, `Aux 5- Show`
- Utilisé par : *(personne)*
- Ligne export : 11724 · id 94103

#### Aux 5 - if A/C Need HT  `IDC`
> Reserve Aux 3 to A/C if there is a A/C Bat Pack
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Aux 5 - Need HT`
  - **Blocking** = `A/C Batt Pack?`
- Lit : `A/C Batt Pack?`, `Aux 5 - Need HT`
- Utilisé par : *(personne)*
- Ligne export : 11774 · id 94112

## EQUIPEMENT / Power

#### Auto Global switch Off  `IP`
- Propriétés : Unit=min · Default mode={120}
- Utilisé par : `Auto Off - Timer`, `Adjust group: Main Setup`, `Single adjust item: Auto Global switch Off`
- Ligne export : 11891 · id 57002

#### Power Down State  `FSM`
- Propriétés : Store value=No · Resetting channel=Cancel Button
- État 0 **Power On**
  - transition *Ask Stop* (état cible non exporté par IQANdesign)
    - **Activating** = `(Off Button - IDC) OR (Charger End Charge and Auto Off After Charge?)`
- État 1 **Power Down**
  - transition *Time to Down* (état cible non exporté par IQANdesign)
    - **Activating** = `Power Down Timer`
- État 2 **Stop**
- Lit : `Auto Off After Charge?`, `Cancel Button`, `Charger End Charge`, `Off Button - IDC`, `Power Down Timer`
- Utilisé par : `Auto Off Cmd`, `Power Down`, `Power Down State output`, `Power Down Timer Ask`
- Ligne export : 11903 · id 57204

#### Power Down Timer Ask  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Power Down State = 1) AND (not(KBB K3 IDC - LD UP)) AND (not(KBB K4 IDC- LD DOWN))`
- Lit : `KBB K3 IDC - LD UP`, `KBB K4 IDC- LD DOWN`, `Power Down State`
- Utilisé par : `BarTimer`, `Power Down Timer`
- Ligne export : 11996 · id 58935

#### Time ask Power Down  `IP`
- Propriétés : Unit=ms · Default mode={3000}
- Utilisé par : `Power Down Timer`, `ShutDownBar`
- Ligne export : 12057 · id 57227

#### Power Down Timer  `IDC`
- Propriétés : Toggle=No · Delay on=Time ask Power Down [ms] · Delay off=0
- Logique :
  - **Activating** = `Power Down Timer Ask`
- Lit : `Power Down Timer Ask`, `Time ask Power Down`
- Utilisé par : `Power Down State`
- Ligne export : 12069 · id 57229

#### Time ask remote  `IP`
- Propriétés : Unit=ms · Default mode={5000}
- Utilisé par : `Remote Ask Stop`
- Ligne export : 12112 · id 57223

#### Remote Ask Stop  `IDC`
- Propriétés : Toggle=No · Delay on=Time ask remote [ms] · Delay off=0
- Logique :
  - **Activating** = `Remote Status = 1`
- Lit : `Remote Status`, `Time ask remote`
- Utilisé par : `Off Button - IDC`
- Ligne export : 12124 · id 57219

#### OFF Button  `VDIN`
- Propriétés : Toggle=Yes · Resetting channel=Cancel Button · Store value=No
- Lit : `Cancel Button`
- Utilisé par : `Off Button - IDC`, `MD4-10 page: BASE`, `MD4-10 page: STARTUP`
- Ligne export : 12169 · id 57001

#### Auto Off - Timer  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=Auto Global switch Off [min]
- Logique :
  - **Decreasing** = `True`
  - **Resetting** = `(Tracks Button) OR (OutBoard Button) OR (PositiveFlank((2 = Auto Off Message))) OR (Charger Charging IDC)`
- Lit : `Auto Global switch Off`, `Auto Off Message`, `C`, `Charger Charging IDC`, `OutBoard Button`, `Tracks Button`
- Utilisé par : `Auto Off Message`, `Off Button - IDC`
- Ligne export : 12180 · id 57003

#### Auto Off Message  `IMSG`
- Propriétés : Show message=All · Dialog type=Confirmation · Header=Automatic Shutdown · Text=I seems that you don't use the boat, press Continue to keep the boat ON. If not the boat will stop in 30 minutes. · Left button=Continue · Right button=OFF
- Logique :
  - **Showing** = `Auto Off - Timer [min] <= 20`
- Lit : `Auto Off - Timer`, `Continue`
- Utilisé par : `Auto Off - Timer`
- Ligne export : 12270 · id 57018

#### Charger Charging IDC  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=0
- Logique :
  - **Activating** = `Charger Charging State = 4`
- Lit : `Charger Charging State`
- Utilisé par : `Auto Off - Timer`, `Boat State`, `Charging State`, `Continue`
- Ligne export : 12320 · id 57375

#### Off Button - IDC  `IDC`
- Propriétés : Toggle=No · Delay on=100 · Delay off=0
- Logique :
  - **Activating** = `(OFF Button) OR (Auto Off - Timer [min] <= 0) OR (Remote Ask Stop)`
- Lit : `Auto Off - Timer`, `OFF Button`, `Remote Ask Stop`
- Utilisé par : `Continue`, `Power Down State`
- Ligne export : 12365 · id 57027

#### Charger End Charge  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=500
- Logique :
  - **Activating** = `PositiveFlank((5 = Charger Charging State))`
- Lit : `Charger Charging State`
- Utilisé par : `Power Down State`
- Ligne export : 12424 · id 57429

#### Charging State  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Charger Charging IDC`
  - **Blocking** = `Continue`
- Lit : `Charger Charging IDC`, `Continue`
- Utilisé par : `Charger Charging Wait 2 minutes`
- Ligne export : 12477 · id 60220

#### Charger Charging Wait 2 minutes  `IDC`
- Propriétés : Toggle=No · Delay on=120000 · Delay off=0
- Logique :
  - **Activating** = `Charging State`
- Lit : `Charging State`
- Utilisé par : `Auto Off Lamps`
- Ligne export : 12527 · id 60135

#### Auto Off Cmd  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `Power Down State = 2`
- Lit : `Power Down State`
- Utilisé par : `KBB K10 IDC - AUTO OFF POWER BOX`
- Ligne export : 12570 · id 56961

#### Power Down  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Power Down State = 1`
- Lit : `Power Down State`
- Utilisé par : `A/C Bat Pack State Machine`, `A/CBatPack Reset`, `Auto Off Lamps`, `Back Light State`, `Boat State`, `Power Down Lights Timer`
- Ligne export : 12615 · id 57257

#### Press Remote  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Remote Status`
- Lit : `Remote Status`
- Utilisé par : `Start Lights Timer 1000`
- Ligne export : 12660 · id 57414

#### Charger Connected  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `1 = Charger Charging State`
- Lit : `Charger Charging State`
- Utilisé par : `Start Lights Gen`
- Ligne export : 12703 · id 57407

#### Start Lights Gen  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `PositiveFlank(True) OR (PositiveFlank(Charger Connected))`
- Lit : `Charger Connected`
- Utilisé par : `Start Lights Timer`
- Ligne export : 12748 · id 57357

#### Start Lights Timer  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=2000
- Logique :
  - **Decreasing** = `True`
  - **Resetting** = `PositiveFlank(Start Lights Gen)`
- Lit : `Start Lights Gen`
- Utilisé par : `Start Lights`
- Ligne export : 12800 · id 57318

#### Start Lights  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Start Lights Timer [ms] mod 250) < 125`
  - **Blocking** = `Start Lights Timer [ms] <= 0`
- Lit : `Start Lights Timer`
- Utilisé par : `Blink Light`
- Ligne export : 12860 · id 57330

#### Power Down Lights Timer  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Power Down`
- Lit : `Power Down`
- Utilisé par : `Power Down Lights`
- Ligne export : 12923 · id 57486

#### Power Down Lights  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Power Down Lights Timer [ms] mod 2000) < 1900`
  - **Blocking** = `Power Down Lights Timer [ms] <= 0`
- Lit : `Power Down Lights Timer`
- Utilisé par : `Blink Light`
- Ligne export : 12975 · id 57497

#### Start Lights Timer 1000  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=1000
- Logique :
  - **Decreasing** = `True`
  - **Resetting** = `PositiveFlank(Press Remote)`
- Lit : `Press Remote`
- Utilisé par : `Start Lights 1000`
- Ligne export : 13038 · id 57546

#### Start Lights 1000  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Start Lights Timer 1000 [ms] mod 250) < 125`
  - **Blocking** = `Start Lights Timer 1000 [ms] <= 0`
- Lit : `Start Lights Timer 1000`
- Utilisé par : `Blink Light`
- Ligne export : 13098 · id 57557

#### Blink Light  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Start Lights) OR (Power Down Lights) OR (Start Lights 1000)`
- Lit : `Power Down Lights`, `Start Lights`, `Start Lights 1000`
- Utilisé par : `Blink Light IDC`
- Ligne export : 13161 · id 57451

#### BarTimer  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=0
- Logique :
  - **Increasing** = `Power Down Timer Ask`
  - **Resetting** = `NegativeFlank(Power Down Timer Ask)`
- Lit : `Power Down Timer Ask`
- Utilisé par : `ShutDownBar`
- Ligne export : 13218 · id 58920

#### ShutDownBar  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(BarTimer [ms]: 0->0, Time ask Power Down [ms]->100, Freeze)`
- Lit : `BarTimer`, `Time ask Power Down`
- Utilisé par : `MD4-10 page: SHUTDOWN`
- Ligne export : 13278 · id 58950

#### Auto Off After Charge?  `DP`
> If False: Boat will remain on after charge
- Propriétés : True text=Yes · False text=No · Default mode={True}
- Utilisé par : `Power Down State`, `Adjust group: Charger Setup`, `Single adjust item: Auto Off After Charge?`
- Ligne export : 13325 · id 90387

## EQUIPEMENT / SEAT

#### Person 1  `TP`
- Propriétés : Default mode={John}
- Utilisé par : `Adjust group: Seat Setup`, `Single adjust item: Person 1`
- Ligne export : 9458 · id 48110

#### Person 2  `TP`
- Propriétés : Default mode={Steve}
- Utilisé par : `Adjust group: Seat Setup`, `Single adjust item: Person 2`
- Ligne export : 9469 · id 48116

#### Person 3  `TP`
- Propriétés : Default mode={Florent}
- Utilisé par : `Adjust group: Seat Setup`, `Single adjust item: Person 3`
- Ligne export : 9480 · id 48117

#### Person  `SP`
- Propriétés : Input channel=None · Default state name=Person 1 · States={Person 2; Person 3}
- Utilisé par : `Seat Front Back`, `Seat Up Down`, `Adjust group: Seat Setup`, `MD4-10 page: BASE`, `Single adjust item: Person`
- Ligne export : 9491 · id 46871

#### Seat Up Down  `IP`
- Propriétés : Unit=% · Mode selector=Person · Default mode: Person 1={80} · Mode 1: Person 2={80} · Mode 2: Person 3={80}
- Lit : `Person`
- Utilisé par : `Seat UP/DOWN MAC`, `Adjust group: Seat Setup`, `Single adjust item: Seat Up Down`
- Ligne export : 9504 · id 47262

#### Seat position  `VDIN`
- Propriétés : Toggle=Yes · Store value=Yes
- Utilisé par : `Alim Seat`, `Seat State`, `MD4-10 page: BASE`
- Ligne export : 9520 · id 48056

#### Seat State  `SMC`
- Propriétés : Default state name=Standing
- Fonction *Seating* :
  - **Activating** = `Seat position`
- Lit : `Seat position`
- Utilisé par : `Seat Front/Back MAC`
- Ligne export : 9531 · id 48052

#### Seat UP/DOWN MAC  `MAC`
- Propriétés : Limiting object group=Unsigned
- Logique :
  - **Controlling** = `Seat Up Down [%]`
- Lit : `Seat Up Down`
- Utilisé par : `Alim Seat`, `Seat UP/DOWN MAC output`
- Ligne export : 9571 · id 48058

#### Seat Front Back  `IP`
- Propriétés : Unit=% · Mode selector=Person · Default mode: Person 1={80} · Mode 1: Person 2={80} · Mode 2: Person 3={80}
- Lit : `Person`
- Utilisé par : `Seat Front/Back MAC`, `Adjust group: Seat Setup`, `Single adjust item: Seat Front Back`
- Ligne export : 9613 · id 47270

#### Seat Front/Back MAC  `MAC`
- Propriétés : Limiting object group=Unsigned · Function selector=Seat State
- Fonction *Standing* :
  - **Controlling** = `0`
- Fonction *Seating* :
  - **Controlling** = `Seat Front Back [%]`
- Lit : `Seat Front Back`, `Seat State`
- Utilisé par : `Alim Seat`, `Seat Front/Back MAC output`
- Ligne export : 9629 · id 48081

#### Alim Seat  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=20000
- Logique :
  - **Activating** = `(PositiveFlank(Seat position)) OR (NegativeFlank(Seat position)) OR (DerivativeOf(Seat UP/DOWN MAC)) OR (DerivativeOf(Seat Front/Back MAC))`
- Lit : `Seat Front/Back MAC`, `Seat UP/DOWN MAC`, `Seat position`
- Utilisé par : `KTC K3 IDC - Seat Power`
- Ligne export : 9702 · id 48103
