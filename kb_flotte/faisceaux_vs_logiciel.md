# Faisceaux MC42 ↔ brochage du logiciel 108.3.1

Comparaison automatique (outil `harness_pins.py`) des plans RapidHarness avec la liste des broches déclarée dans IQANdesign (`faisceaux/v2_mc42/MC42-33.tsv`). Plans utilisés : **#22679 MC42_X100 thermique IND N** (07/2024), **#28580 MC42_X100 électrique IND H** (07/2024, une IND I de 03/2025 « inversion joysticks » existe mais n'est pas dans le dossier), **#24207 MC42_CAB IND L** (07/2024).

## Concordant

| Broche MC42 | Faisceau | Logiciel 108.3.1 |
|---|---|---|
| C1:2 / C1:18 (CAN B) | J1939 moteur (thermique), J1939 HVLP (électrique), CAN keyboxes (cabine) | idem (bus « CanB ») |
| C1:3 / C1:19 (CAN C) | CAN Drive (x100), CAN batterie HT (cabine) | idem (bus « CanC ») |
| C1:8, 9, 10 | niveau d'huile, pression bloc, pression chenilles | VIN-A, B, C idem |
| C1:11 / 12 | capteur Hall échelle (cabine) | `C Ladder_Sensor mc 11` (compteur) |
| C1:25, 26 | température huile, état pompe (thermique) | idem |
| C1:28 / 29 | télécommande (cabine) | `C REMOTE LD DOWN / UP` |
| C1:41, 42, 43, 57, 58, 59 | EV by-pass, descente, déblocage, montée, tension, blocage | idem |
| C1:44, 60 | frein (thermique) / boîte FBA (électrique) | idem |
| C1:45, 48 | siège électrique (cabine) | idem |
| C1:52, 54 | température échappement, capteur tension démarreur | idem |

## Écarts à trancher

| # | Broche | Faisceau | Logiciel | Conséquence |
|---|---|---|---|---|
| 1 | **C1:14 / 39 / 55** (COUT-A) | **pompe droite** (Right_Pump_1/2, thermique) | `T Pump 2 Left mc 14` (consigne gauche) | Les noms sont inversés entre faisceau et logiciel. Soit la 108.3.1 envoie la consigne gauche à la pompe droite (et quelque chose compense, ex. l'hydraulique ou les joysticks), soit les noms du logiciel sont faux. La V69 et la V5.37 appellent cette sortie « Pump 1 Right », comme le faisceau. Le réglage `T Pump wiring` permet les deux, mais il faut savoir lequel est **correct**. |
| 2 | **C1:24 / C1:36** joysticks | thermique : 24 = droit, 36 = gauche ; électrique IND H : **24 = gauche, 36 = droit** ; électrique IND I (2025) : inversion corrigée | 24 = « RJoy » (droit), 36 = « Left Joystick » | Les bateaux électriques X100 câblés selon l'IND H auraient leurs joysticks inversés, sauf compensation par l'étalonnage. À vérifier sur un bateau électrique X100 de 2024. |
| 3 | **C1:38** | capteur de courant (« Current_sensor », thermique IND N 2024) | `T V sensor inflate 24v` (tension du gonflage 24 V) | Même broche, deux usages. À confirmer : le capteur est-il celui du gonflage, ou un capteur de courant différent ? |
| 4 | **C1:14 / 39** en cabine | **PWM_tension_tracks** (commande de tension des chenilles) | aucun canal électrique ; seule la sortie pompe thermique (inactive en électrique) | **La 108.3.1 ne pilote pas la tension des chenilles par PWM sur un Commuter câblé ainsi.** La famille V25 le faisait sans doute. Point de compatibilité majeur pour la v2. |
| 5 | **C1:26 / 36 / 52** en cabine | accéléromètre (3 axes) | aucun canal en cabine (ces broches servent au thermique / x100) | L'accéléromètre du Commuter n'est pas exploité en 108.3.1 (le projet VW V5.37 lisait X, Y, Z sur le MD3). |
| 6 | **C1:24 / C1:25** en cabine | R10 / R11 | niveau d'eau (cabine) / courant de cale (cabine) | Concordant d'après les noms de canaux, mais les étiquettes du plan (R10, R11) ne le disent pas : à confirmer. |

Les points 4 et 5 confirment qu'il faut le projet de la famille **V25** (Commuter) pour que la v2 couvre vraiment les bateaux cabine.
