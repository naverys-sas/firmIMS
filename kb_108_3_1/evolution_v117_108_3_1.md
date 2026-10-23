# Évolution v117 (108.2.2_117) → 108.3.1

88 canaux ajoutés, 7 supprimés, 19 modifiés.

## Activation de groupes modifiée

- `MD45-ET app / Water level V10 motor` : Enabled Yes → No

## Canaux modifiés

### B8 F4 Speed Free 4ET FREE Sel `IDC` — MC42 app / mc.Link MC42-Screens Logic ims
```diff
-- Propriétés : Toggle=No · Delay on=0 · Delay off=0
+- Propriétés : Toggle=Yes · Delay on=0 · Delay off=0
-  - **Activating** = `(B8 F4 Speed Free 4ET FREE) OR (B8 FREE C10)`
+  - **Activating** = `(B8 F4 Speed Free 4ET FREE) OR (B8 FREE C10) OR (Free keypad)`
```
### B1 Virtual UP 4ETUP sel `IDC` — MC42 app / mc.Link MC42-Screens Logic ims
```diff
-  - **Activating** = `(B1 Virtual UP 4ET UP) OR (B1 UP C10) OR (up 20t)`
+  - **Activating** = `(B1 Virtual UP 4ET UP) OR (B1 UP C10) OR (up 20t) OR (keypad up wait) OR (keypad up quick)`
```
### B2 Virtual DOWN 4ETDOWN sel `IDC` — MC42 app / mc.Link MC42-Screens Logic ims
```diff
-  - **Activating** = `(B2 Virtual DOWN 4ET DOWN) OR (B2 DOWN C10) OR (not up 20t)`
+  - **Activating** = `(B2 Virtual DOWN 4ET DOWN) OR (B2 DOWN C10) OR (not up 20t) OR (keypad down wait) OR (keypad down quick)`
```
### Rampe 0->100 `SFC` — MC42 app / mc.Link MC42-Screens Logic ims
```diff
+> Rampe qui permet l'affichage d'une jauge qui se remplit
```
### B9 `IDC` — MC42 app / mc.Link MC42-Screens Logic ims
```diff
+> Channel activée quand on appuis sur le ON/OFF IMS
-  - **Activating** = `(B9 Start Button 4ET START) OR (B9 START C10)`
+  - **Activating** = `(B9 Start Button 4ET START) OR (B9 START C10) OR (Start/Stop keypad)`
```
### B9 wait `IDC` — MC42 app / mc.Link MC42-Screens Logic ims
```diff
+> permet de régler le début de remplissage de la jauge avec le timing d'affichage de la jauge (sinon quand la jauge apparait à l'écran elle est déjà à 20-30%)
```
### B9 toggle `IDC` — MC42 app / mc.Link MC42-Screens Logic ims
```diff
+> s'active quand la jauge atteint une certaine valeur
```
### B9 show jauge OFF `IDC` — MC42 app / mc.Link MC42-Screens Logic ims
```diff
+> Pour savoir si on affiche la jauge bleu (ON) ou Rouge (OFF)
```
### B9 toggle wait `IDC` — MC42 app / mc.Link MC42-Screens Logic ims
```diff
+> Timing pour ne pas que la jauge disparraisse totalement quand on arrête d'appuyer sur ON/OFF IMS
```
### e With tension `DP` — MC42 app / mc.Electric / E.Track Up/Down
```diff
+> permet d'empecher la tension chenille (si sur False)
```
### Elec show schema down `IDC` — MC42 app / mc.Electric / E.Track Up/Down
```diff
+> s'active pour montrer le bon schéma sur le MD4
```
### Elec activ shema inter `IDC` — MC42 app / mc.Electric / E.Track Up/Down
```diff
+> s'active pour montrer le bon schéma sur le MD4
```
### Elec show schema UP `IDC` — MC42 app / mc.Electric / E.Track Up/Down
```diff
+> s'active pour montrer le bon schéma sur le MD4
```
### Timer clignotement schema inter `TMR` — MC42 app / mc.Electric / E.Track Up/Down
```diff
+> permet de faire clignoter le shcéma intermédiaire
```
### T Starter Protection `IMAC` — MC42 app / mc.Thermic / T.Power
```diff
-  - **Controlling** = `1000 * T Out START Engine`
+  - **Controlling** = `1000 * T Out STARTER Engine`
```
### T ON_Bits `IMAC` — MC42 app / mc.Thermic / T.KeyBox x100 T
```diff
-  Result := T K1 Fan Rear / Fan * 1 + T K2 Fan Super / Pump  * 2 + T K3 Fan Exhaust / AutoOff * 4 + T K4 Engine Power / Search Lights * 8 + T K5 Engine Start * 16 + T K6 Engine Water Pump * 32 + T K7 Exhaust Water Pump * 64 + T K8 * 128 + T K9 * 256 + T K10 * 512 + T K11 * 1024 + T K12 * 2048 + T K13 * 4096
+  Result := T K1 Fan Rear / Fan * 1 + T K2 Fan Super / Pump  * 2 + T K3 Fan Exhaust / AutoOff * 4 + T K4 Engine Power ON / Search Lights * 8 + T K5 Engine Starter * 16 + T K6 Engine Water Pump * 32 + T K7 Exhaust Water Pump * 64 + T K8 * 128 + T K9 * 256 + T K10 * 512 + T K11 * 1024 + T K12 * 2048 + T K13 * 4096
```
### T Engine State mc `SMC` — MC42 app / mc.Thermic
```diff
-  - **Activating** = `T Out START Engine`
+  - **Activating** = `T Out STARTER Engine`
```
### 45 Speed state `FSM` — MC42 app / logic screen md4
```diff
-    - **Activating** = `PositiveFlank(IDC speed super slow)`
+    - **Activating** = `(PositiveFlank(IDC speed super slow)) OR (Slow keypad)`
-    - **Activating** = `PositiveFlank(IDC Speed Fast)`
+    - **Activating** = `(PositiveFlank(IDC Speed Fast)) OR (Fast keypad)`
-    - **Activating** = `PositiveFlank(IDC Speed S)`
+    - **Activating** = `(PositiveFlank(IDC Speed S)) OR (Normal keypad)`
-    - **Activating** = `PositiveFlank(IDC Speed Fast)`
+    - **Activating** = `(PositiveFlank(IDC Speed Fast)) OR (Fast keypad)`
-    - **Activating** = `PositiveFlank(IDC Speed S)`
+    - **Activating** = `(PositiveFlank(IDC Speed S)) OR (Normal keypad)`
-    - **Activating** = `PositiveFlank(IDC speed super slow)`
+    - **Activating** = `(PositiveFlank(IDC speed super slow)) OR (Slow keypad)`
```
### F4 Speed Free 45 `VDIN` — MD45-ET app / (racine)
```diff
-- Propriétés : Toggle=Yes · Resetting channel=Reset Free Button 45 · Store value=No
+- Propriétés : Toggle=No · Resetting channel=Reset Free Button 45
```

## Canaux ajoutés

- MC42 app / mc.Link MC42-Screens Logic ims : `Voyant free` (IDC)
- MC42 app / mc.Link MC42-Screens Logic ims : `keypad up wait` (IDC)
- MC42 app / mc.Link MC42-Screens Logic ims : `keypad down wait` (IDC)
- MC42 app / mc.Link MC42-Screens Logic ims : `keypad up quick` (IDC)
- MC42 app / mc.Link MC42-Screens Logic ims : `keypad down quick` (IDC)
- MC42 app / mc.Link MC42-Screens Logic ims : `B1 up toggle` (IDC)
- MC42 app / mc.Link MC42-Screens Logic ims : `B2 down toggle` (IDC)
- MC42 app / mc.Electric / E.BATTERY / E. Tyva : `Delta cell voltage` (MAC)
- MC42 app / mc.Thermic / T.Power : `T Out STARTER Engine` (IDC)
- MC42 app / mc.Thermic / T.Power : `T Out POWER ON Engine` (IDC)
- MC42 app / mc.Thermic / T.KeyBox x100 T : `T K4 Engine Power ON / Search Lights` (IDC)
- MC42 app / mc.Thermic / T.KeyBox x100 T : `T K5 Engine Starter` (IDC)
- MC42 app / (racine) : `Keypad 8 keys` (DP)
- MC42 app / Keypad 8 keys : `FSM keypad` (FSM)
- MC42 app / Keypad 8 keys / Keypad CAN : `heartbeat` (GFIN)
- MC42 app / Keypad 8 keys / Keypad CAN : `Heartbeat/statut` (GPIN)
- MC42 app / Keypad 8 keys / Keypad CAN : `keys number frame` (GFIN)
- MC42 app / Keypad 8 keys / Keypad CAN : `keys number` (GPIN)
- MC42 app / Keypad 8 keys / Keypad CAN : `set led ON` (GFOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Blue led part 2` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Green led part 1` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Red led part 2` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Blue led 1, 2, 3 & 4` (MAC)
- MC42 app / Keypad 8 keys / Keypad CAN : `Blue led part 1` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Green led part 2` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Red led part 1` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Blue led 5, 6, 7 & 8` (MAC)
- MC42 app / Keypad 8 keys / Keypad CAN : `Red led 1, 2, 3 & 4` (MAC)
- MC42 app / Keypad 8 keys / Keypad CAN : `red led#1` (FGI)
- MC42 app / Keypad 8 keys / Keypad CAN : `blue led #1` (FGI)
- MC42 app / Keypad 8 keys / Keypad CAN : `blue led#2` (FGI)
- MC42 app / Keypad 8 keys / Keypad CAN : `blue led #5` (FGI)
- MC42 app / Keypad 8 keys / Keypad CAN : `blue led #6` (FGI)
- MC42 app / Keypad 8 keys / Keypad CAN : `blue led #7` (FGI)
- MC42 app / Keypad 8 keys / Keypad CAN : `set led blink ON` (GFOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `blue led blink part1` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `blue led blink part2` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Blue led blink #4` (FGI)
- MC42 app / Keypad 8 keys / Keypad CAN : `Blue led blink #8` (FGI)
- MC42 app / Keypad 8 keys / Keypad CAN : `Blue led blink 1, 2, 3 & 4` (MAC)
- MC42 app / Keypad 8 keys / Keypad CAN : `Blue led blink 5, 6, 7 & 8` (MAC)
- MC42 app / Keypad 8 keys / Keypad CAN : `Blue led #4` (FGI)
- MC42 app / Keypad 8 keys / Keypad CAN : `blue led #8` (FGI)
- MC42 app / Keypad 8 keys / Keypad CAN : `Backlight default color` (GFOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Set device register` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `CAN object 2003h byte 1` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Sub index 04` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Color` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `CAN object 2003h byte 2` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Keypad backlight color` (SP)
- MC42 app / Keypad 8 keys / Keypad CAN : `Color en hex` (MAC)
- MC42 app / Keypad 8 keys / Keypad CAN : `backlight 20% activation` (GFOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `backlight level 20%` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Keypad backlight?` (DP)
- MC42 app / Keypad 8 keys / Keypad CAN : `backlight` (MAC)
- MC42 app / Keypad 8 keys / Keypad CAN : `trigger backlight` (IDC)
- MC42 app / Keypad 8 keys / Keypad CAN : `trigger` (IDC)
- MC42 app / Keypad 8 keys / Keypad CAN : `Keypad LED brightness level` (SP)
- MC42 app / Keypad 8 keys / Keypad CAN : `level brightness in hex` (MAC)
- MC42 app / Keypad 8 keys / Keypad CAN : `Brightness default level` (GFOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Sub index 05` (GPOUT)
- MC42 app / Keypad 8 keys / Keypad CAN : `Brightness level` (GPOUT)
- MC42 app / Keypad 8 keys : `Start/Stop keypad` (IDC)
- MC42 app / Keypad 8 keys : `Free keypad` (IDC)
- MC42 app / Keypad 8 keys : `No heartbeat` (IDC)
- MC42 app / Keypad 8 keys : `Keypad HS` (CMSG)
- MC42 app / Keypad 8 keys : `Up Keypad` (IDC)
- MC42 app / Keypad 8 keys : `Down Keypad` (IDC)
- MC42 app / Keypad 8 keys : `Slow keypad` (IDC)
- MC42 app / Keypad 8 keys : `Normal keypad` (IDC)
- MC42 app / Keypad 8 keys : `Fast keypad` (IDC)
- MC42 app / Keypad 8 keys : `blue led #1` (MAC)
- MC42 app / Keypad 8 keys : `blue led #5` (MAC)
- MC42 app / Keypad 8 keys : `blue led #6` (MAC)
- MC42 app / Keypad 8 keys : `blue led #7` (MAC)
- MC42 app / Keypad 8 keys : `red led#1` (MAC)
- MC42 app / Keypad 8 keys : `blue led #2` (MAC)
- MC42 app / Keypad 8 keys : `up or down keypad` (SMC)
- MC42 app / Keypad 8 keys : `Blue led blink #4` (IDC)
- MC42 app / Keypad 8 keys : `Blue led blink #8` (IDC)
- MC42 app / Keypad 8 keys : `blue led #4` (IDC)
- MC42 app / Keypad 8 keys : `blue led #8` (IDC)
- MC42 app / Keypad 8 keys : `up keypad toggle` (IDC)
- MC42 app / Keypad 8 keys : `down keypad toggle` (IDC)
- MC42 app / Keypad 8 keys : `Statut stop` (IDC)
- MC42 app / Keypad 8 keys : `statut pre-op` (IDC)
- MC42 app / (racine) : `Activation` (IDC)
- MC42 app / (racine) : `timer for activation` (TMR)

## Canaux supprimés

- MC42 app / mc.Thermic / T.Power : `T Out START Engine` (IDC)
- MC42 app / mc.Thermic / T.Power : `T Out SWITCH ON Engine` (IDC)
- MC42 app / mc.Thermic / T.KeyBox x100 T : `T K4 Engine Power / Search Lights` (IDC)
- MC42 app / mc.Thermic / T.KeyBox x100 T : `T K5 Engine Start` (IDC)
- MC42 app / mc.Keypad_PKP2400SI : `FSM Keypad X100` (FSM)
- MC42 app / mc.Keypad_PKP2400SI : `heart` (GFIN)
- MC42 app / mc.Keypad_PKP2400SI : `heartbeat` (GPIN)