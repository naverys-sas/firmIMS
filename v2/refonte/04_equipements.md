# 4. Interfaces normalisées des équipements

Chaque famille d'équipement publie **le même jeu de canaux**, quelle que soit la marque. La logique métier, l'IHM et les journaux ne lisent que ces canaux. Une marque nouvelle remplit les mêmes lignes ([02_conventions.md](02_conventions.md) §2.7) ; une case vide se voit dans ces tableaux et dans le contrôle automatique.

Les canaux d'interface sont des canaux à sélecteur (`Function selector` = le réglage de marque) rangés à la racine du groupe de la famille. Leur nom historique est indiqué entre parenthèses quand il existe ; les références à la logique actuelle viennent de l'export `v2_MC42_en_cours.txt`.

Légende des cases : ✔ fourni · **vide** = fonction vide dans la 108.3.1 · *approx.* = valeur de remplacement · ✚ nouveau en v2.

## 4.1 Batterie haute tension — `21 BAT`

Sélecteur : `eb Battery Brand` (0 BMW = Torqeedo, 1 NovumTech, 2 Tyva, 3 Kreisel).

| Canal v2 (108.3.1) | Unité | Torqeedo (BMW) | NovumTech | Tyva | Kreisel |
|---|---|---|---|---|---|
| `BAT CAN ok` (`Battery CAN OK`) | bool | heartbeats BMW | 5 trames G1-G5 + Errors (D16) | trames de mesure + Error_M0 (D16) | `257 mBMS_FuncSTAT` |
| `BAT Standby` (`Battery STANDBY`) | bool | ✔ | ✔ | ✔ | ✔ |
| `BAT Charge mode` (`Battery CHARGE`) | bool | ✔ | ✔ | ✔ | ✔ |
| `BAT Discharge mode` (`Battery DRIVE MODE`) | bool | ✔ | ✔ | ✔ | ✔ |
| `BAT SOC` (`Battery SOC`) | % | ✔ | ✔ | ✔ (avec contrôle on/off) | ✔ |
| `BAT Voltage` (`Battery InstantVoltage`) | V | ✔ | ✔ | ✔ | ✔ |
| `BAT Voltage traction` (`BMS_U_Trac`) | V | ✔ | *approx.* = tension batterie | *approx.* = tension batterie | ✔ |
| `BAT Voltage precharge ref` (`CPI_BMS_U_Trac`) | V | ✔ | ✔ | ✔ (moyenne) | **vide** → à définir (D29) |
| `BAT Current` (`Current Bat`) | A | ✔ | ✔ | *approx.* = M1 + M2 (sans la pompe M3 ; trame courant marquée WRONG) | ✔ |
| `BAT Max discharge current` (`Max Discharge`) | A | ✔ | ✔ | ✔ | ✔ |
| `BAT Cell T max` (`Cell_T_max_Master`) | °C | ✔ | ✔ | ✔ | ✔ |
| `BAT Cell V min` (`LowCellVoltage check bmw`) | mV | **vide** | ✔ | ✔ | ✔ |
| `BAT Cell V max` (`HighCellVoltage check bmw`) | mV | **vide** | ✔ | ✔ | ✔ |
| `BAT Cell V delta` ✚ | mV | — | max − min | max − min | max − min |
| `BAT Isolation` (`Batt - Iso_Resist`) | kΩ | ✔ | *approx.* = 5000 constant (pas de mesure transmise) | ✔ (Bender gen1/gen2) | ✔ |
| `BAT Isolation low` (`BMW tyva - Isolation Error`) | bool | ✔ | False (volontaire, recommandation fournisseur) | ✔ | ✔ |
| `BAT Isolation error` (`Error Iso_Resist`) | bool | ✔ | ✔ (signal Novum) | ✔ | ✔ depuis D9 |
| `BAT Ground fault` (`Flag Ground Fault Detection`) | bool | ✔ | False | ✔ | **vide** (D13, attente doc Kreisel) |
| `BAT Charged` (`Battery CHARGED`) | bool | ✔ | ✔ | ✔ | ✔ depuis D9 |
| `BAT Error` ✚ | bool | erreur BMS | erreur BMS | erreur BMS | erreur BMS |
| `BAT Warning` ✚ | bool | — | warnings Novum | warnings Tyva | à définir |
| `BAT Error raw code` ✚ | entier | `BatErrorCode` | mot d'erreur Novum | mot d'erreur Tyva | code Kreisel |

Réglages par marque conservés (paramètres à mode, contrat) : `eb Charge Max`, `eb Isolation Protection Level`, `ec Max Full Charge Voltage`, `IsoMonTriggerRecord tempo`.

Cases vides ou approximatives : elles sont **toutes** listées dans D29 avec leur traitement (valeur de remplacement documentée, ou demande de documentation fournisseur). Aucune ne doit rester vide sans description.

Le hub batterie (machine PMS, watchdog, protection d'isolement 100 s, `Battery ERROR DIGIT`) n'est **pas** dans le pilote : c'est de la logique métier, dans `40 PWR / PWR Battery management`.

## 4.2 Chargeur — `22 CHG`

Sélecteur : `ec Charger Brand` (0 BMW = Torqeedo, 1 Brusa, 2 Elcon). Entrées des pilotes par FGI, comme aujourd'hui : `Charger CMD`, `Charger UMax`, `Charger IMax`, `Charger I Target` (Brusa).

| Canal v2 (108.3.1) | Unité | Torqeedo (BMW) | Brusa | Elcon |
|---|---|---|---|---|
| `CHG CAN ok` (`Charger CAN BUS OK`) | bool | ✔ | ✔ | ✔ |
| `CHG AC connected` (`Charger CONNECT to 220V`) | bool | ✔ | ✔ | ✔ |
| `CHG Ready` (`Charger READY`) | bool | ✔ | ✔ | ✔ |
| `CHG Charging` (`Charger CHARGING`) | bool | ✔ | ✔ | ✔ |
| `CHG Error` (`Charger ERROR`) | bool | ✔ | ✔ | ✔ |
| `CHG Output voltage` (`Charger Output Voltage`) | V | ✔ | ✔ | ✔ |
| `CHG Output current` (`Charger Output Current`) | A | ✔ | **courant secteur** au lieu du courant batterie (anomalie, D29) | ✔ |
| `CHG Mains current` ✚ | A | ✔ | ✔ | — |
| `CHG Mains voltage` ✚ | V | — | ✔ | ✔ (`Input Voltage`) |
| `CHG Temperature` ✚ | °C | — | ✔ (étage de puissance) | ✔ |
| `CHG Error raw code` ✚ | entier | statut | octet d'erreur 1552 | octet d'état |

## 4.3 Variateurs de chenilles — `23 DRV`

Sélecteur : `em1 M-Track - Brand` (0 Sevcon gen4, 1 Zapi). M1 = moteur droit, M2 = moteur gauche. Le pilote Zapi est **un** groupe copié deux fois (FGI : nœud, côté) ; le pilote Sevcon gère déjà les deux moteurs.

| Canal v2 (108.3.1), pour M1 et M2 | Unité | Sevcon gen4 | Zapi |
|---|---|---|---|
| `DRV Mx CAN ok` | bool | ✔ | ✔ (heartbeat) |
| `DRV Mx ready` | bool | ✔ | M1 : **True constant**, M2 : ✔ (incohérence, D29) |
| `DRV Mx run` | bool | ✔ | ✔ |
| `DRV Mx error` (`Mx - Error mode`) | bool | ✔ | ✔ |
| `DRV Mx error raw code` ✚ | entier | code d'erreur Sevcon (journal actuel) | code d'erreur Zapi (journal actuel) |
| `DRV Mx warning raw code` ✚ | entier | — | code d'alerte Zapi |
| `DRV Mx speed` | rpm | ✔ | ✔ |
| `DRV Mx current` | A | ✔ | ✔ |
| `DRV Mx torque` | Nm | ✔ | ✔ |
| `DRV Mx voltage` | V | ✔ | ✔ |
| `DRV Mx heatsink temp` | °C | ✔ | ✔ |
| `DRV Mx motor temp` (`Mx - KTY`) | °C | ✔ | ✔ |

Consignes (écrites par `30 ACT / ACT Traction`, lues par les pilotes en FGI) : `ACT Mx speed cmd` (%), `ACT Drive enable`, `ACT Brake request`. Le détail des trames sortantes reste celui de la 108.3.1.

## 4.4 Pompe hydraulique électrique M3 — `24 PMP`

Sélecteur automatique `em M-Pump - Brand` (0 Sevcon HVLP CANopen « gen » en cabine, 1 Sevcon HVLP J1939 en X100). Le groupe historique `broeknE.Sevcon.M3.gen.soon` devient `PMP Sevcon HVLP CANopen` : il est en service sur les Commuter (D4).

| Canal v2 (108.3.1) | Unité | HVLP CANopen | HVLP J1939 |
|---|---|---|---|
| `PMP CAN ok` | bool | ✔ | ✔ |
| `PMP ready` | bool | ✔ | ✔ |
| `PMP run` | bool | ✔ | ✔ |
| `PMP error` | bool | ✔ | ✔ |
| `PMP error raw code` ✚ | entier | ✔ | `M3 - New Error Code` |
| `PMP heatsink temp` | °C | ✔ | ✔ |
| `PMP motor temp` | °C | ✔ | ✔ |
| `PMP voltage` | V | ✔ | ✔ |

Consignes : `ACT Pump speed cmd` (rpm ou %), `ACT Pump enable`.

## 4.5 Moteur thermique — `25 ENG`

Les trois pilotes EB2, Ford et Kubota de la 108.3.1 sont **identiques** (mêmes PGN, mêmes SPN, même adresse source 0). La v2 n'a qu'**un pilote J1939** ; `T Engine type` ne choisit plus que les calibrations (seuils d'eau, régimes, courants de pompe…, 22 paramètres à mode conservés). Décision D28. Le même pilote sert au projet MC2 (VW 2.0L et Ford 1.5L sont aussi en J1939).

| Canal v2 (108.3.1) | Unité | Source J1939 |
|---|---|---|
| `ENG CAN ok` ✚ | bool | EEC1 reçue (timeout 300 ms à valider) |
| `ENG Speed` (`T Speed CAN 42`) | rpm | EEC1, SPN 190 |
| `ENG Coolant temp` (`T Engine coolant temp`) | °C | ET1, SPN 110 (timeout 3 s, D15) |
| `ENG Coolant temp lost` (`T Engine temp CAN lost`) | bool | D15 |
| `ENG Oil pressure` | kPa | EFL/P1, SPN 100 |
| `ENG Load` (`T % load at current speed`) | % | EEC2, SPN 92 |
| `ENG Torque` | % | EEC1, SPN 513 |
| `ENG MIL lamp`, `ENG Red stop lamp`, `ENG Amber lamp`, `ENG Protect lamp` | bool | DM1 (lampes) |
| `ENG DM1 active` ✚ | bool | au moins un code DM1 actif |
| `ENG DM1 last SPN` ✚, `ENG DM1 last FMI` ✚ | entier | DM1 (pour le journal) |

Consigne : `ACT Engine speed request` (rpm) → TSC1. Démarrage, arrêt et alimentation passent par les relais de la keybox X100 (§4.6) et sont pilotés par `40 PWR / PWR Engine management`.

## 4.6 Keyboxes — `26 KBX`

**Keybox X100** (un seul module CAN, deux brochages de relais selon la propulsion). Aujourd'hui deux groupes de 68 et 71 canaux, dont 33 identiques. En v2 : un pilote qui expose `KBX X100 Kn cmd` et `KBX X100 Kn fuse blown` (n = 1 à 13) et `KBX X100 CAN ok`. **Le sens de chaque relais est décidé hors du pilote**, par la couche qui le commande :

| Relais | Électrique (108.3.1) | Thermique (108.3.1) | Commandé en v2 par |
|---|---|---|---|
| K1 | ventilateur arrière (FAN MK) | ventilateur arrière | `60 THM` |
| K2 | ventilateur super / pompe | idem | `60 THM` |
| K3 | ancien ventilateur échappement / auto-off | ventilateur échappement / auto-off | `60 THM` ou `40 PWR` selon propulsion |
| K4 | alimentation variateurs / projecteurs | alimentation moteur / projecteurs | `40 PWR` |
| K5 | démarrage variateurs | démarreur | `40 PWR` |
| K6 | allumage DC/DC | pompe à eau moteur | `40 PWR` (E) / `60 THM` (T) |
| K7 | AUX 2 | pompe à eau échappement | `70 CAB` (E) / `60 THM` (T) |
| K8 à K13 | identiques | identiques | selon fonction |

**Keyboxes cabine KTB, KBB, KTC** : trois instances d'un même groupe (FGI : nœud 0x717 / 0x718 / 0x719, nom), chacune avec 13 relais, 13 états de fusible, CAN ok, programmation. Les 3 × 13 messages « fuse is blown » sont produits par le même modèle.

## 4.7 Keypad Blink PKP2400SI — `27 KPD`

Repris de la 108.3.1 (conforme à la notice) : état CANopen, touches, LED. Interface : `KPD CAN ok`, `KPD Key start stop`, `KPD Key free`, `KPD Key slow`, `KPD Key normal`, `KPD Key fast`, `KPD Key up`, `KPD Key down`. Les touches deviennent des **sources** de commandes dans `80 HMI` au même titre que les boutons d'écran. Corrections : délai annoncé 1 s / réel 3 s (description alignée), pas d'alerte « Keypad HS » pendant le pré-opérationnel des 3 premières secondes.

## 4.8 Télémétrie Proemion — `28 TEL` (option)

Présente en V25, V35 et V69, perdue en 108.3.1. Reprise telle quelle de la V69 (la plus récente), activée par `Proemion gateway`. Elle ne lit que des interfaces normalisées, ce qui la rend identique en électrique et en thermique.

## 4.9 Préparer les équipements futurs

- **Nouvelle batterie, nouveau chargeur, nouveau variateur** : une colonne de plus dans le tableau de la famille, un état de plus en fin de sélecteur, un sous-groupe pilote. Rien d'autre ne change.
- **Nouveau moteur électrique de chenille** : il ne change que les calibrations du variateur (aucune logique IQAN), sauf si sa température est lue autrement ; dans ce cas, `DRV Mx motor temp` change de source dans le pilote.
- **Nouveau moteur thermique** : s'il parle J1939 standard, un état de plus dans `T Engine type` et une colonne de calibrations ; sinon un pilote dédié qui remplit l'interface `ENG`.
- **Variateurs en CAN FD, MD5 en Ethernet** : hors de portée d'IQANdesign 6.08 ; voir [06_ihm.md](06_ihm.md) §6.5 et [10_besoins_iqandesign.md](10_besoins_iqandesign.md).
