# MC42 — (racine appli)

12 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## (racine)

#### Status:MC42[1]  `MDGN`
- Propriétés : Value=Module status · Module=MC42 (MC42[1]) · Module index=0
- Utilisé par : *(personne)*
- Ligne export : 14769 · id 32508

#### MD3_Start/Stop  `APPIN`
- Propriétés : Input channel=Can Out Button F1
- Lit : `Can Out Button F1`
- Utilisé par : `MD3 START`, `MD3 STOP`
- Ligne export : 14780 · id 54459

#### S/N:MC42[1]  `MDGN`
- Propriétés : Value=Serial number · Module=MC42 (MC42[1]) · Module index=1
- Utilisé par : *(personne)*
- Ligne export : 23950 · id 32510

#### Address:MC42[1]  `MDGN`
- Propriétés : Value=Id tag · Module=MC42 (MC42[1]) · Module index=3
- Utilisé par : *(personne)*
- Ligne export : 23961 · id 32513

#### Temp:MC42[1]  `MDGN`
- Propriétés : Value=Temperature [°C] · Module=MC42 (MC42[1]) · Module index=2
- Lit : `C`
- Utilisé par : *(personne)*
- Ligne export : 23972 · id 32514

#### VREF-A:MC42[1]  `MDGN`
- Propriétés : Value=Reference voltage A · Module=MC42 (MC42[1]) · Module index=5
- Utilisé par : `Measure group: System Monitoring`
- Ligne export : 23983 · id 32515

#### 12V Batt.  `MDGN`
- Propriétés : Value=Supply voltage [V] · Module=MC42 (MC42[1]) · Module index=4
- Utilisé par : `MDGN-+BAT:MC2[1]`, `Measure group: System Monitoring`
- Ligne export : 23994 · id 32516

#### PIN 44  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Inter EV Frein`
- Lit : ``, `Inter EV Frein`
- Utilisé par : `Pin 44 (Brake)`
- Ligne export : 24650 · id 54870

#### Pin 44 (Brake)  `DOUT`
- Propriétés : Delay on=0 · Delay off=0 · Input channel=PIN 44 · Module=MC42 (MC42[1]) · Module index=14
- Lit : `PIN 44`
- Utilisé par : *(personne)*
- Ligne export : 24693 · id 54869

#### Proemion  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Active le groupe: Proemion`, `Adjust group: Master Config`, `Measure group: Proemion`, `Single adjust item: Proemion`
- Ligne export : 26819 · id 61696

#### Thermic Engine STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *STARTING* :
  - **Activating** = `Out SWITCH ON Engine`
  - **Blocking** = `System Started DELAYS`
- Fonction *READY* :
  - **Activating** = `(Out SWITCH ON Engine) AND (System Started DELAYS)`
- Lit : ``, `Out SWITCH ON Engine`, `System Started DELAYS`
- Utilisé par : `Power State Int`
- Ligne export : 27119 · id 51442

#### debug temps screen  `DP`
- Propriétés : Default mode={False}
- Utilisé par : `Adjust group: Master Features`, `MD3 page: Thermic`, `Single adjust item: debug temps screen`
- Ligne export : 27204 · id 67860
