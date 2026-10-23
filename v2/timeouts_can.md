# Timeouts CAN — proposition trame par trame (v2 MC42)

35 trames reçues n'ont pas de timeout dans la 108.3.1. Sans timeout, si une trame cesse d'arriver, ses valeurs restent figées sur la dernière reçue, sans alarme. Avec un timeout, elles passent à leur valeur d'erreur et le statut de la trame devient « Timeout », que la logique peut tester.

**Règle proposée :**
- **Trames périodiques de mesure** (SOC, tension, courant, températures) : timeout = celui des autres trames du même équipement. Une perte devient visible au lieu de donner une valeur figée.
- **Trames événementielles** (codes d'erreur, défauts, appuis de touches) : **pas de timeout**. L'équipement ne les envoie qu'en cas d'événement, donc un timeout se déclencherait en fonctionnement normal.

| # | Trame (équipement) | Contenu | Type | Proposition |
|---|---|---|---|---|
| 1 | `BMS_NTHT_G1_Info` à `G5_Charger` (batterie NovumTech, 5 trames) | SOC, SOH, tensions, courants, températures, consignes chargeur | périodique | **250 ms**, comme `BMS_NTHT_Errors novum` |
| 2 | `BatteryState_M0`, `PDUStatus_M0b`, `TemperaturePDU_M0`, `VoltageBattery_M0`, `CurrentBattery_M0`, `TemperatureCell_M0`, `MaxAdmissibleCurrent_M0` (batterie Tyva HT, 7 trames) | SOC, relais PDU, tensions, courant, températures, courants admissibles | périodique | **1000 ms**, comme `Error_M0` |
| 3 | `IMD_InfoGeneral gen2` (isomètre Bender gen2) | alarmes d'isolement | périodique | **3000 ms**, comme les autres trames Bender |
| 4 | `Engine Temperature …` (EB2, Ford, Kubota, PGN 65262) | température d'eau moteur | périodique J1939 (1 s) | **3000 ms** |
| 5 | Les mêmes 9 trames Tyva de la batterie 24 V clim (écran cabine) | SOC, tensions, températures, versions | périodique | **10000 ms**, comme les autres trames de cette batterie |
| 6 | `Dcu50Error`, `Bat51Error`, `Iso52MonError` (batterie BMW) | codes d'erreur | événement | **pas de timeout** (la perte BMW est déjà détectée par les heartbeats) |
| 7 | `GFIN PDO2_TX` EMERG (variateurs Zapi M1, M2) | alarmes Zapi | événement | **pas de timeout** (le heartbeat Zapi surveille déjà la liaison) |
| 8 | `GFIN-A/E/F/G:Generic` (keyboxes X100 et cabine) | défauts de relais K1 à K13 | événement | **pas de timeout** |
| 9 | `keys number frame` (keypad Blink) | touche appuyée | événement | **pas de timeout** (le heartbeat 0x715 surveille déjà le keypad) |

**Effet à vérifier sur banc pour les lignes 1 à 5 :** la valeur d'erreur des signaux (souvent 0) remplace la dernière valeur. Par exemple, un SOC à 0 % sur perte de trame peut déclencher la demande de charge ou l'arrêt sur batterie basse : c'est le comportement prudent, mais il est nouveau. Je vérifierai pour chaque signal quelle valeur d'erreur il prend et ce que la logique en fait, avant de modifier quoi que ce soit.

## Réalisé le 23/10/2026 (v2 MC42, vérifié par export)

| Équipement | Trames avec timeout | Gestion de la perte |
|---|---|---|
| Moteur J1939 (EB2, Ford, Kubota) | `Engine Temperature …` : 3000 ms | moteur en marche + température absente 5 s → message critique e1201, répété toutes les 30 s (décision D15) |
| Batterie NovumTech | G1 à G5 : 250 ms | `Novum - CAN OK` exige désormais les 5 trames |
| Batterie Tyva HT | BatteryState, PDUStatus, TemperaturePDU, VoltageBattery, TemperatureCell, MaxAdmissibleCurrent : 1000 ms | `tyva batt can ok idc` exige aussi les 5 trames de mesure utilisées |
| Isomètre Bender gen2 | IMD_InfoGeneral gen2 : 3000 ms | logique existante (`tyva isomon can ok`), qui devient enfin opérante |
| Batterie Tyva 24 V clim (écran cabine) | les 6 mêmes trames : 10000 ms | `tyva1 batt can ok idc` exige aussi les 5 trames de mesure utilisées |

Non traités volontairement : `CurrentBattery_M0` (signal marqué « WRONG », inutilisé), trames d'information de version, trames événementielles (erreurs BMW, alarmes Zapi, défauts keyboxes, touches keypad).

**À tester sur banc :** débrancher le CAN de chaque équipement, vérifier la perte détectée et le comportement de la batterie (passage en défaut de communication) ; moteur thermique en marche sans trame de température : message e1201 immédiat puis toutes les 30 s.

**Reste pour toi (optionnel) :** ajouter `T Engine temp CAN lost` au journal « Thermic Events » (glisser-déposer du canal sur le journal, comme pour le menu).
