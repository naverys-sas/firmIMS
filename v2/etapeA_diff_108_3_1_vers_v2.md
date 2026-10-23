# Évolution 108.3.1 → v2 en cours

3 canaux ajoutés, 0 supprimés, 7 modifiés.

## Activation de groupes modifiée

- `MD45-ET app / Water level V10 motor` : Enabled No → Yes

## Canaux modifiés

### Battery CHARGED `IDC` — MC42 app / mc.Electric / E.BATTERY
```diff
-- Fonction *Kreisel* : (vide)
+- Fonction *Kreisel* :
+  - **Activating** = `(Battery SOC [%] >= eb Charge Max [%]) OR (Charger asks End Of Charge)`
```
### Error Iso_Resist `IDC` — MC42 app / mc.Electric / E.BATTERY
```diff
-- Fonction *Kreisel* : (vide)
+- Fonction *Kreisel* :
+  - **Activating** = `BMW tyva - Isolation Error`
```
### e Battery Protection mc `CMSG` — MC42 app / mc.Electric / E.BATTERY
```diff
-- Fonction *Kreisel* : (vide)
+- Fonction *Kreisel* :
+  - **Showing** = `Error Iso_Resist`
```
### e M3 - Pump Engine CMSG mc `CMSG` — MC42 app / mc.Electric / E.MOTORS / E.M3-Hydrau / E.Sevcon.M3.j19
```diff
+- Logique :
+  - **Showing** = `M3 - New Error Code`
```
### T Engine Temp State `SMC` — MC42 app / mc.Thermic / T.Power
```diff
-    outputValue := True  //switch on
+    outputValue := True
+  elseif T Persistant Water Temp >= (T Water °C Low + T Water Temp Hysteresis Gap ) then
+    outputValue := False
```
### T Pump 1 Right mc 15 `COUT` — MC42 app / mc.Thermic / T.Pump / pins thermic
```diff
-- Propriétés : Bidirectional=Yes · BWL=0 · Input channel=T Pump 1 Right Filter ECC1 [%] · Default mode={{T Min current Right Fordward [mA]; T Filter pump 1 Pos [mA]; 0; 0}; {T Min current Right Backward [mA]; T Filter pump 1 Neg [mA]; 0; 0}} · Module=MC42-33 (MC42[0]) · Module index=1
+- Propriétés : Bidirectional=Yes · BWL=0 · Input channel=T Pump mc15 cmd [%] · Mode selector=T Pump wiring · Default mode: Standard={{T Min current Right Fordward [mA]; T Filter pump 1 Pos [mA]; 0; 0}; {T Min current Right Backward [mA]; T Filter pump 1 Neg [mA]; 0; 0}} · Mode 1: Swapped={{T Min current Left Fordward [mA]; T Filter pump 2 Pos [mA]; 0; 0}; {T Min current Left Backward [mA]; T Filter pump 2 Neg [mA]; 0; 0}} · Module=MC42-33 (MC42[0]) · Module index=1
```
### T Pump 2 Left mc 14 `COUT` — MC42 app / mc.Thermic / T.Pump / pins thermic
```diff
-- Propriétés : Bidirectional=Yes · BWL=0 · Input channel=T Pump 2 Left Filter ECC1 [%] · Default mode={{T Min current Left Fordward [mA]; T Filter pump 2 Pos [mA]; 0; 0}; {T Min current Left Backward [mA]; T Filter pump 2 Neg [mA]; 0; 0}} · Module=MC42-33 (MC42[0]) · Module index=0
+- Propriétés : Bidirectional=Yes · BWL=0 · Input channel=T Pump mc14 cmd [%] · Mode selector=T Pump wiring · Default mode: Standard={{T Min current Left Fordward [mA]; T Filter pump 2 Pos [mA]; 0; 0}; {T Min current Left Backward [mA]; T Filter pump 2 Neg [mA]; 0; 0}} · Mode 1: Swapped={{T Min current Right Fordward [mA]; T Filter pump 1 Pos [mA]; 0; 0}; {T Min current Right Backward [mA]; T Filter pump 1 Neg [mA]; 0; 0}} · Module=MC42-33 (MC42[0]) · Module index=0
```

## Canaux ajoutés

- MC42 app / mc.Thermic / T.Pump / pins thermic : `T Pump wiring` (SP)
- MC42 app / mc.Thermic / T.Pump / pins thermic : `T Pump mc14 cmd` (MAC)
- MC42 app / mc.Thermic / T.Pump / pins thermic : `T Pump mc15 cmd` (MAC)

## Canaux supprimés
