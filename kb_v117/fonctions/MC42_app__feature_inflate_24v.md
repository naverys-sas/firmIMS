# MC42 app — feature inflate 24v

4 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## feature inflate 24v — actif seulement si `feature inflate 24v`

#### T V sensor inflate 24v  `VIN32`
- Propriétés : Unit=V · Error value=0 · Calibration={0; 30000; 0; 30} · Alarms={No; 0; No; 100} · Module=MC42-33 (MC42[0]) · Module index=0
- Utilisé par : `Inflate system battery`, `Inflate system battery low`
- Ligne export : 103175 · id 236397

#### Inflate system battery  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `T V sensor inflate 24v [V]`
- Lit : `T V sensor inflate 24v`
- Utilisé par : `e Low voltage 24v`
- Ligne export : 103197 · id 236432

#### e Low voltage 24v  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Low voltage 24v · Text=Please start one of your engine to charge the 24v inflate system battery. The system is disable until the battery is charging · Channel=Inflate system battery
- Logique :
  - **Showing** = `Inflate system battery low`
- Lit : `Inflate system battery`, `Inflate system battery low`
- Utilisé par : *(personne)*
- Ligne export : 103239 · id 236421

#### Inflate system battery low  `IDC`
- Propriétés : Toggle=No · Delay on=3000 · Delay off=0
- Logique :
  - **Activating** = `T V sensor inflate 24v [V] <= 22`
- Lit : `T V sensor inflate 24v`
- Utilisé par : `T K8`, `e Low voltage 24v`
- Ligne export : 103285 · id 236449
