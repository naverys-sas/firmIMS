# MC2 — Screen State

8 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Screen State

#### Thermic Engine STATE  `SMC`
- Propriétés : Default state name=OFF
- Fonction *STARTING* :
  - **Activating** = `Out SWITCH ON Engine`
  - **Blocking** = `Engine START`
- Fonction *READY* :
  - **Activating** = `(Engine START) AND (Out SWITCH ON Engine)`
- Lit : ``, `Engine START`, `Out SWITCH ON Engine`
- Utilisé par : `Power State Int`
- Ligne export : 20490 · id 27453

#### Power State Int  `IMAC`
- Logique :
  - **Controlling** = `Thermic Engine STATE`
- Lit : ``, `Thermic Engine STATE`
- Utilisé par : `VIEW BUTTON States`, `VIEW Power State`, `VIEW SPEED STATE`
- Ligne export : 20575 · id 27124

#### Up/DOWN STATE  `FGI`
- Propriétés : Input type=State · Input=State Up/Down · Default state name=OFF · States={DOWN; INTERMEDIATE; UP}
- Lit : `State Up/Down`
- Utilisé par : `VIEW SPEED STATE`
- Ligne export : 20616 · id 27132

#### Speed All State  `FGI`
- Propriétés : Input type=State · Input=State All Speed · Default state name=OFF · States={IDLE; SLOW; SUPER SLOW; ROAD; ROAS ASK; ROAD CRUISE}
- Lit : `State All Speed`
- Utilisé par : `VIEW BUTTON States`, `VIEW SPEED STATE`
- Ligne export : 20631 · id 27136

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
  - **Blocking** = `Up/DOWN STATE > 0`
- Fonction *Road Cruise* :
  - **Activating** = `(Speed All State = 5) OR (Speed All State = 6)`
  - **Blocking** = `Up/DOWN STATE > 0`
- Lit : ``, `Power State Int`, `Speed All State`, `Up/DOWN STATE`
- Utilisé par : `MD3 page: ENGINE PAGE`
- Ligne export : 20649 · id 27143

#### VIEW Power State  `SP`
- Propriétés : Input channel=Power State Int · Default state name=Off · States={Starting; Run}
- Lit : `Power State Int`
- Utilisé par : `MD3 page: ENGINE PAGE`
- Ligne export : 21018 · id 27224

#### Speed Mode  `FGI`
- Propriétés : Input type=State · Input=Speed Mode · Default state name=OFF · States={IDLE; Free; Unfree; Road Ask; Road Cruise}
- Lit : `Speed Mode`
- Utilisé par : `VIEW BUTTON States`
- Ligne export : 21031 · id 27497

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
- Utilisé par : `MD3 page: BASE`
- Ligne export : 21048 · id 27227
