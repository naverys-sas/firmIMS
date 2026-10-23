# MC42 — Screen State

6 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Screen State

#### Power State Int  `IMAC`
- Logique :
  - **Controlling** = `Thermic Engine STATE`
- Lit : ``, `Thermic Engine STATE`
- Utilisé par : `VIEW BUTTON States`, `VIEW Power State`, `VIEW SPEED STATE`
- Ligne export : 24022 · id 51473

#### Up/DOWN STATE  `FGI`
- Propriétés : Input type=State · Input=State Up/Down · Default state name=OFF · States={DOWN; INTERMEDIATE; UP}
- Lit : `State`, `State Up/Down`
- Utilisé par : `VIEW SPEED STATE`
- Ligne export : 24063 · id 56647

#### Speed All State  `FGI`
- Propriétés : Input type=State · Input=State All Speed · Default state name=OFF · States={IDLE; SLOW; SUPER SLOW; ROAD; ROAS ASK; ROAD CRUISE}
- Lit : `State`, `State All Speed`
- Utilisé par : `VIEW BUTTON States`, `VIEW SPEED STATE`
- Ligne export : 24078 · id 56652

#### VIEW SPEED STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *STARTING* :
  - **Activating** = `Power State Int = 1`
- Fonction *READY* :
  - **Activating** = `Power State Int = 2`
  - **Blocking** = `(Up/DOWN STATE > 0) OR (Speed All State > 1)`
- Fonction *DOWN* :
  - **Activating** = `Up/DOWN STATE = 1`
- Fonction *INTERMEDIAIRE* :
  - **Activating** = `Up/DOWN STATE = 2`
- Fonction *UP* :
  - **Activating** = `Up/DOWN STATE = 3`
- Fonction *SLOW* :
  - **Activating** = `Speed All State = 2`
  - **Blocking** = `Up/DOWN STATE > 0`
- Fonction *Super Slow* :
  - **Activating** = `Speed All State = 3`
  - **Blocking** = `Up/DOWN STATE > 0`
- Fonction *Fast* :
  - **Activating** = `Speed All State = 4`
  - **Blocking** = `(Up/DOWN STATE > 0) OR (Persistant Water Temp [°C] >= Water °C Critical Critical [°C])`
- Fonction *Road Cruise* :
  - **Activating** = `(Speed All State = 5) OR (Speed All State = 6)`
  - **Blocking** = `(Up/DOWN STATE > 0) OR (Persistant Water Temp [°C] >= Water °C Critical Critical [°C])`
- Lit : ``, `Persistant Water Temp`, `Power State Int`, `Speed All State`, `Up/DOWN STATE`, `Water °C Critical Critical`
- Utilisé par : `MD3 page: BASE`
- Ligne export : 24096 · id 56659

#### VIEW Power State  `SP`
- Propriétés : Input channel=Power State Int · Default state name=Off · States={Starting; Run}
- Lit : `Power State Int`
- Utilisé par : `MD3 page: Thermic`
- Ligne export : 24483 · id 57157

#### VIEW BUTTON States  `SMC`
- Propriétés : Default state name=Stop
- Fonction *Ready* :
  - **Activating** = `(Power State Int = 2) AND (Speed All State <= 1)`
- Fonction *Start* :
  - **Activating** = `Power State Int = 2`
  - **Blocking** = `(2 = Speed Mode) OR (Speed All State <= 1)`
- Fonction *Start Free* :
  - **Activating** = `(Power State Int = 2) AND (2 = Speed Mode)`
  - **Blocking** = `Speed All State <= 1`
- Lit : ``, `Power State Int`, `Speed All State`, `Speed Mode`
- Utilisé par : `MD3 page: Thermic`
- Ligne export : 24496 · id 57185
