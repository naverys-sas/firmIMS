# MC42[1] application — (racine appli)

17 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## (racine)

#### MDGN-+BAT:MC2[1]  `MDGN`
- Propriétés : Value=Supply voltage [V] · Module=MC42[1] · Module index=4
- Utilisé par : `Battery LOW`, `Need to Charge Voltage`
- Ligne export : 30911 · id 39175

#### Tension to charge  `FP`
- Propriétés : Default mode={11,9}
- Utilisé par : `Need to Charge Voltage`, `Adjust group: Master Setup`, `Single adjust item: Tension to charge`
- Ligne export : 30922 · id 55187

#### Need to Charge Voltage  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank((Inside(MDGN-+BAT:MC2[1] [V], 2, Tension to charge)))) OR (Need to Charge Voltage)`
  - **Blocking** = `MDGN-+BAT:MC2[1] [V] > 13,2`
- Lit : `MDGN-+BAT:MC2[1]`, `Tension to charge`
- Utilisé par : `Need to Charge Voltage Wait`
- Ligne export : 30934 · id 47892

#### Auto Charge 12V  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `Need to Charge Voltage Wait`, `Adjust group: Main Setup`, `Single adjust item: Auto Charge 12V`
- Ligne export : 31004 · id 53589

#### Need to Charge Voltage Wait  `IDC`
- Propriétés : Toggle=No · Delay on=100000 · Delay off=100000
- Logique :
  - **Activating** = `Need to Charge Voltage`
  - **Blocking** = `not(Auto Charge 12V)`
- Lit : `Auto Charge 12V`, `Need to Charge Voltage`
- Utilisé par : `Need to Charge IDC - Public`
- Ligne export : 31017 · id 54225

#### Need to Charge IDC - Public  `IDC`
- Propriétés : Toggle=No · Delay on=1000 · Delay off=1000
- Logique :
  - **Activating** = `(Need to Charge Voltage Wait) OR (Need Charge Input)`
- Lit : `Need Charge Input`, `Need to Charge Voltage Wait`
- Utilisé par : `Battery DIGITAL`
- Ligne export : 31068 · id 47944

#### MDGN-S/N:MC2[1]  `MDGN`
- Propriétés : Value=Serial number · Module=MC42[1] · Module index=1
- Utilisé par : *(personne)*
- Ligne export : 65870 · id 38930

#### MDGN-Temp:MC2[1]  `MDGN`
- Propriétés : Value=Temperature [Â°C] · Module=MC42[1] · Module index=2
- Lit : `C`
- Utilisé par : *(personne)*
- Ligne export : 65881 · id 38931

#### MDGN-Address:MC2[1]  `MDGN`
- Propriétés : Value=Id tag · Module=MC42[1] · Module index=3
- Utilisé par : *(personne)*
- Ligne export : 65892 · id 38932

#### MDGN-VREF:MC2[1]  `MDGN`
- Propriétés : Value=Reference voltage A · Module=MC42[1] · Module index=5
- Utilisé par : *(personne)*
- Ligne export : 65903 · id 38933

#### Cycle utilization  `SIC`
- Propriétés : Value=Cycle utilization [%]
- Utilisé par : *(personne)*
- Ligne export : 67295 · id 39172

#### Acceleration Sensor  `DP`
- Propriétés : Default mode={True}
- Utilisé par : `Active le groupe: Acceleration`, `Adjust group: Master Setup`, `Single adjust item: Acceleration Sensor`
- Ligne export : 67304 · id 42657

#### Battery LOW  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=500
- Logique :
  - **Activating** = `MDGN-+BAT:MC2[1] [V] < 11`
- Lit : `MDGN-+BAT:MC2[1]`
- Utilisé par : `Battery LOW MSG`, `MD4-10 page: MAIN`
- Ligne export : 68126 · id 51538

#### MDGN-VREF:MC2[1]  `MDGN`
- Propriétés : Value=Reference voltage B · Module=MC42[1] · Module index=6
- Utilisé par : *(personne)*
- Ligne export : 68171 · id 52496

#### Battery LOW MSG  `IDC`
- Propriétés : Toggle=No · Delay on=60000 · Delay off=500
- Logique :
  - **Activating** = `Battery LOW`
- Lit : `Battery LOW`
- Utilisé par : `Battery Low`
- Ligne export : 68182 · id 54780

#### Battery Low  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=12V battery is low · Text=It is not recommander to use the boat if the battery is low. Check battery connection, check battery switch and check that 12V battery charge when the hight voltage battery is switch ON.
- Logique :
  - **Showing** = `Battery LOW MSG`
  - **Hiding** = `NegativeFlank(Battery LOW MSG)`
- Lit : `Battery LOW MSG`
- Utilisé par : *(personne)*
- Ligne export : 68225 · id 54771

#### Proemion Gateway  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Active le groupe: Proemion`, `Adjust group: Config Electric Drive`, `MD4-10 page: MAIN`, `Measure group: Proemion`, `Single adjust item: Proemion Gateway`
- Ligne export : 68279 · id 84813
