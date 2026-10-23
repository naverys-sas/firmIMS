# Assemblage v2 : rapport

Canaux créés : 181 (COPY 2, DP 5, IDC 104, IMAC 14, IP 2, MAC 45, SMC 3, SP 6).

## Canaux déjà présents (non recréés) (1)

- T Pump wiring (SP)

## Liens vers l'existant (19)

- IO Remote up C1:29 -> C REMOTE LD UP mc 29
- IO Remote down C1:28 -> C REMOTE LD DOWN mc 28
- IO Joystick left C1:36 -> Left Joystick mc 36
- IO Joystick right C1:24 -> Low water level RJoy
- KPD Key up -> Up Keypad
- KPD Key down -> Down Keypad
- KPD Key slow -> Slow keypad
- KPD Key fast -> Fast keypad
- KPD Key free -> Free keypad
- KPD Key start stop -> Start/Stop keypad
- PWR System started -> Batt or engine started mc
- PWR Charging state -> E.Charging State Machine
- PWR PMS state -> E.Power Management System
- HMI MD45 command word -> btod 45
- HMI MD45 joystick left -> Left Joy ET45 ou water level C2:1 APPIN
- HMI MD45 joystick right -> Right Joystick ET45 C2:2 APPIN
- HMI MD410 command word -> btod c10
- HMI MD410 joystick left -> Left Joystick C41 C2:1 APPIN
- HMI MD410 joystick right -> Right Joystick C41 C2:2 APPIN

## Types non traités (6)

- ENG Speed request (FGI)
- HMI Status word 1 (APPOUT)
- HMI Status word 2 (APPOUT)
- HMI Status word 3 (APPOUT)
- HMI Status word 4 (APPOUT)
- HMI Values (APPOUT)

## Formules à définir (4)

- ENG DM1 active / Default function / activating : « DM1 active code count > 0 » (canal inconnu à la position 0 : « DM1 active code count > 0 »)
- ENG DM1 last SPN / Default function / activating : « DM1 SPN » (canal inconnu à la position 0 : « DM1 SPN »)
- ENG DM1 last FMI / Default function / activating : « DM1 FMI » (canal inconnu à la position 0 : « DM1 FMI »)
- LOG HYD up down interrupted / Default function / activating : « TRK Up/Down aborted » (canal inconnu à la position 0 : « TRK Up/Down aborted »)
