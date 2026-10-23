# MC42 app — (racine appli)

24 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## (racine)

#### is_x100_mc  `MAC`
> not(is_cab_mc)
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `not(is_cab_mc)`
- Lit : `is_cab_mc`
- Utilisé par : `Is_Electric_x100 mc`, `is_x100_mc_s`
- Ligne export : 152 · id 169733

#### is_x100_mc_s  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `is_x100_mc`
- Lit : `is_x100_mc`
- Utilisé par : `is_x100_math`, `joy_mc42_and_not_cab`, `Active le groupe: mc.Link MC42-Screens Logic ims / joystick mc42 / left joystick x100`, `Single adjust item: Joystick plugged md45`
- Ligne export : 195 · id 229598

#### Is_Electric mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Drive Type mc = 0`
- Lit : `Drive Type mc`
- Utilisé par : `BUTTON DRIVE 4ET`, `Elec/10 hours true entre 10 et 16h`, `Elec/md4 10 hours check-up 45`, `Elec/md4 10 hours check-up 45`, `Power Down State 4ET`, `debug screen E`, `Active le groupe: mc.Electric`, `Active le groupe: mc.I/O / Power Vars E mc 60/ Batt reset C`, `Adjust group: Master Battery`, `Adjust group: Master Charger`, `Adjust group: Master Electric`, `Adjust group: Master System Debug`, `Adjust group: Setup Charger`, `Event log: Battery Isolation`, `Event log: Electronic logs`, `MD4-10 page: INFO`, `MD4-10 page: MAINTENANCE`, `MD4-5 page: BASE`, `MD4-5 page: BASE Info`, `MD4-5 page: INFO`, `MD4-5 page: MAIN Elec`, `MD4-5 page: MAINTENANCE`, `Measure group: Pump Sevcon HVLP`, `Measure group: Track Engine Sev/Zapi`, `Single adjust item: Auto Global switch Off`, `Single adjust item: Automatic Joystick Inhibition`, `Single adjust item: Battery Brand`, `Single adjust item: Battery Force Discharge`, `Single adjust item: Charger Brand`, `Single adjust item: Charging Force`, `Single adjust item: Debug: Inhibit System Crash Signal`, `Single adjust item: Debug: Mute Watchdog`, `Single adjust item: Debug: Trig Battery Charged`, `Single adjust item: Debug: Trig Charger Ready`, `Single adjust item: Debug: Trig Low LTBat Voltage`, `Single adjust item: EV Bloc delay`, `Single adjust item: Engine - Force Ready`, `Single adjust item: Force EV By Pass`, `Single adjust item: Global Auto Off`, `Single adjust item: Landing Block Number`, `Single adjust item: Locking UP Track`, `Single adjust item: M-Track - Brand`, `Single adjust item: Max Speed`, `Single adjust item: Max_differential`, `Single adjust item: Power Controler Force`, `Single adjust item: Start Slope`, `Single adjust item: Stop Slope`, `Single adjust item: Tension Pressure`, `Single adjust item: Time to tension`, `Single adjust item: Tracks pressure Mode`, `Single adjust item: Variator Force`, `Single adjust item: With Auto Off Relay`, `Single adjust item: With tension`, `Single adjust item: max soc customer`, `Statistics log: Electronic Stats logs`
- Ligne export : 3773 · id 202389

#### Is_Electric_x100 mc  `IDC`
> Drive Type mc = 0 AND is_x100_mc
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Drive Type mc = 0) AND is_x100_mc`
- Lit : `Drive Type mc`, `is_x100_mc`
- Utilisé par : `Active le groupe: mc.Electric / E.KeyBox x100 E`, `Single adjust item: Program KeyBox`
- Ligne export : 3818 · id 208093

#### Status:MC  `MDGN`
- Propriétés : Value=Module status · Module=MC42-33 (MC42[0]) · Module index=0
- Utilisé par : `PARKERs OK E mc`
- Ligne export : 3870 · id 156105

#### Is_Thermic mc  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Drive Type mc = 1`
- Lit : `Drive Type mc`
- Utilisé par : `Auto Off - Timer 4ET`, `Auto PAUSE/OFF 4ET`, `Therm/10 hours true entre 10 et 16h`, `Therm/md4 10 hours check-up 45`, `Therm/md4 10 hours check-up 45`, `debug screen T`, `enabled ON/OFF T&E`, `sel thermic or cab`, `Active le groupe: mc.Thermic`, `Adjust group: Master Thermic`, `Adjust group: Master Thermic Cooling`, `Adjust group: Master Thermic Pumps`, `Event log: Thermic Events`, `MD4-10 page: MAINTENANCE`, `MD4-5 page: BASE`, `MD4-5 page: BASE Info`, `MD4-5 page: INFO`, `MD4-5 page: MAIN Thermic`, `MD4-5 page: MAINTENANCE`, `Measure group: Engine Thermic`, `Measure group: Hydraulic`, `Single adjust item: Ambiante Temperature`, `Single adjust item: Backward - direct corrector`, `Single adjust item: ECU Engine on`, `Single adjust item: ECU Engine priming`, `Single adjust item: Engine type`, `Single adjust item: Force EV By Pass`, `Single adjust item: Force at 2200 rpm`, `Single adjust item: Forward - direct corrector`, `Single adjust item: Fuel line ignition State`, `Single adjust item: Locking UP Track`, `Single adjust item: Manual Start Engine`, `Single adjust item: Max_diffrential`, `Single adjust item: Number of lockers`, `Single adjust item: Program KeyBox`, `Single adjust item: Start Slope`, `Single adjust item: Stop Slope`, `Single adjust item: T Force 12v port sensor on`, `Single adjust item: Tension Pressure`, `Single adjust item: Test Locker`, `Single adjust item: Time to tension`, `Single adjust item: Tracks pressure Mode`, `Single adjust item: With tension`, `Single adjust item: bypsass brake T`, `Statistics log: Thermic Stats`
- Ligne export : 55517 · id 202381

#### is_a_sim  `DP`
> Reboot to take effect
- Propriétés : Default mode={False}
- Utilisé par : `is_a_sim_m`, `not_a_sim`, `sim start engine`, `Adjust group: Master Sim Menu`, `Single adjust item: Is_a_Sim`
- Ligne export : 55562 · id 211597

#### not_a_sim  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `not(is_a_sim)`
- Lit : `is_a_sim`
- Utilisé par : `Exhaust temp sensor mc sel`, `Active le groupe: mc.I/O`, `Active le groupe: mc.Thermic / T.Oil security / pins oil`, `Active le groupe: mc.Thermic / T.Pump / pins thermic`
- Ligne export : 55575 · id 211598

#### sim start engine  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `is_a_sim AND (Screen_Start/Stop mc)`
- Lit : `Screen_Start/Stop mc`, `is_a_sim`
- Utilisé par : `sim start engine_m`
- Ligne export : 55619 · id 211753

#### sim start engine_m  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `sim start engine = 1`
- Lit : `sim start engine`
- Utilisé par : `sim state moteur`
- Ligne export : 55669 · id 211760

#### sim state moteur  `SP`
- Propriétés : Input channel=sim start engine_m · Default state name=not_sim · States={sim}
- Lit : `sim start engine_m`
- Utilisé par : `sim thermal engine speed`
- Ligne export : 55713 · id 211750

#### Iguana Master menus PIN  `PCC`
- Propriétés : Show message=All · Text=Iguana PIN  · PIN code=4158
- Utilisé par : `Adjust group: Master Battery`, `Adjust group: Master Charger`, `Adjust group: Master Config`, `Adjust group: Master Config Options`, `Adjust group: Master Electric`, `Adjust group: Master Features`, `Adjust group: Master Sim Menu`, `Adjust group: Master System Debug`, `Adjust group: Master Thermic`, `Adjust group: Master Thermic Cooling`, `Adjust group: Master Thermic Pumps`, `Adjust group: Master Tracks`
- Ligne export : 73599 · id 202760

#### is_a_sim_m  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `is_a_sim = True`
- Lit : `is_a_sim`
- Utilisé par : `sim state`
- Ligne export : 75781 · id 211729

#### sim state  `SP`
- Propriétés : Input channel=is_a_sim_m · Default state name=not_sim · States={sim}
- Lit : `is_a_sim_m`
- Utilisé par : *(personne)*
- Ligne export : 75825 · id 211728

#### Project version  `SIC`
- Propriétés : Value=Project version
- Utilisé par : `45Project version`, `cProject version`, `MD4-5 page: SHUTDOWN`, `MD4-5 page: brokenSTARTUP PIN`
- Ligne export : 90252 · id 216619

#### S/N:MC  `MDGN`
- Propriétés : Value=Serial number · Module=MC42-33 (MC42[0]) · Module index=1
- Utilisé par : *(personne)*
- Ligne export : 103079 · id 38930

#### Temp:MC  `MDGN`
- Propriétés : Value=Temperature [°C] · Module=MC42-33 (MC42[0]) · Module index=2
- Utilisé par : `Measure group: System Monitoring`
- Ligne export : 103090 · id 38931

#### Address:MC  `MDGN`
- Propriétés : Value=Id tag · Module=MC42-33 (MC42[0]) · Module index=3
- Utilisé par : *(personne)*
- Ligne export : 103101 · id 38932

#### VREF A:MC  `MDGN`
- Propriétés : Value=Reference voltage A · Module=MC42-33 (MC42[0]) · Module index=5
- Utilisé par : `Measure group: System Monitoring`
- Ligne export : 103112 · id 38933

#### Supply v mc42  `MDGN`
- Propriétés : Value=Supply voltage [V] · Module=MC42-33 (MC42[0]) · Module index=4
- Utilisé par : `MD4-5 page: BASE`, `MD4-5 page: BASE Info`, `Measure group: System Monitoring`
- Ligne export : 103123 · id 52496

#### Allow remote connection  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Adjust group: Maintenance`, `Single adjust item: Allow remote connection`
- Ligne export : 103134 · id 236385

#### feature inflate 24v  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Active le groupe: feature inflate 24v`, `Adjust group: Master Features`, `Single adjust item: feature inflate 24v`
- Ligne export : 103147 · id 236391

#### Date 2  `SIC`
- Propriétés : Value=Date
- Lit : `Date`
- Utilisé par : *(personne)*
- Ligne export : 103342 · id 239837

#### Time 2  `SIC`
- Propriétés : Value=Time
- Lit : `Time`
- Utilisé par : *(personne)*
- Ligne export : 103351 · id 239838
