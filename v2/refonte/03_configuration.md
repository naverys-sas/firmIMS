# 3. Configuration et réglages

## 3.1 Principe

Un seul logiciel équipe toutes les coques MC42. Ce qui distingue un bateau d'un autre tient dans ses **réglages** (paramètres stockés dans le contrôleur), jamais dans une version de logiciel différente. La v2 range ces réglages en trois catégories :

| Catégorie | Où | Règle |
|---|---|---|
| **Réglages contrat** (existants en 108.3.1) | `00 CFG / CFG Settings (contract)` | Nom, type, unité, ordre des états **et objet interne** conservés. On les déplace, on ne les recrée pas (§3.2). |
| **Indicateurs de variante** (dérivés) | `00 CFG / CFG Variant flags` | Canaux `CFG Is_…` calculés à partir des réglages ; ce sont eux qui activent les groupes. Jamais réglables. |
| **Réglages nouveaux v2** | `00 CFG / CFG Settings (v2)` | Valeur par défaut = comportement 108.3.1 exact (compatibilité §3.5). |

## 3.2 Pourquoi on déplace les paramètres au lieu de les recréer

Les exports montrent que la 108.3.1 a **recréé** ses paramètres de variante par rapport à la V25.74, alors que les deux projets ont le même identifiant : `Battery Brand` était l'objet 67686 en V25, `eb Battery Brand` est l'objet 128958 en 108.3.1 (même chose pour `Charger Brand`, `M-Track - Brand`). Si IQAN retrouve les valeurs enregistrées par objet interne, et c'est le plus probable, un paramètre recréé repart à sa valeur par défaut sur tous les bateaux mis à jour.

D'où la règle D25 : **la v2 MC42 est construite dans une copie de la 108.3.1, et les paramètres sont déplacés (couper/coller ou glisser) vers `CFG Settings (contract)`, jamais supprimés puis recréés.** Le comportement exact d'IQAN (valeurs retrouvées par objet ou par nom ; un couper/coller garde-t-il l'objet ?) est le premier essai à faire sur le PC ([10_besoins_iqandesign.md](10_besoins_iqandesign.md), B1). Si le déplacement perd les valeurs, les paramètres restent où ils sont et `CFG` ne contient que des alias.

Conséquence pour la flotte V25 : leurs réglages ne passeront de toute façon pas en v2 (objets différents, et ordre des états différent, voir §3.6). Leur migration inclut une ressaisie complète, comme pour les lignées B et C.

## 3.3 Indicateurs de variante

Tous dans `CFG Variant flags`, de type IDC, sans délai. Ils remplacent les canaux `Is_…` dispersés aujourd'hui dans chaque groupe.

| Canal | Définition | Remplace (108.3.1) |
|---|---|---|
| `CFG Is_Electric` | `Drive Type mc = Electric` | `Is_Electric mc` |
| `CFG Is_Thermic` | `Drive Type mc = Fossil` | `Is_Thermic mc` |
| `CFG Is_Cab` | `is_cab_mc` | `is_cab_mc`, `is_cab_math`, `is_cab_1` |
| `CFG Is_X100` | `not CFG Is_Cab` | `is_x100_math`, `is_x100_mc_s` |
| `CFG Is_BAT_Torqeedo` … `CFG Is_BAT_Kreisel` | `Is_Electric and eb Battery Brand = …` | `Is_BMW`, `Is_Novum`, `Is_Tyva`, `Is_Kreisel` |
| `CFG Is_CHG_Torqeedo`, `…_Brusa`, `…_Elcon` | `Is_Electric and ec Charger Brand = …` | `Is_Charger_…` |
| `CFG Is_DRV_Sevcon`, `CFG Is_DRV_Zapi` | `Is_Electric and em1 M-Track - Brand = …` | `Is_MT_Sevcon`, `Is_MT_Zapi` |
| `CFG Is_PMP_HVLP_CANopen`, `CFG Is_PMP_HVLP_J1939` | `Is_Electric and em M-Pump - Brand = …` | `Is_M3_Sevcon_gen`, `Is_M3_Sevcon_j19` |
| `CFG Is_ENG_J1939` | `Is_Thermic` | `Is_EB2 mc`, `Is_FORD mc`, `Is_Kubo mc` (un seul pilote, D28) |
| `CFG Is_Bender_gen1`, `…_gen2` | `Is_BAT_Tyva and Tyva gen bender = …` | `gen1`, `gen2` |
| `CFG Is_KBX_X100` | `CFG Is_X100` | activation implicite de `E/T.KeyBox x100` |
| `CFG Is_KBX_Cab` | `CFG Is_Cab` | `Keyboxs CAB` |
| `CFG Has_MD45`, `CFG Has_MD410`, `CFG Has_MD3` | statut de diagnostic du module (MDGN) = présent, avec délai 2 s | aucun (aujourd'hui les écrans sont supposés présents) |
| `CFG Joystick source` | état : MC42, MD4-5, MD4-10, MD3, selon les réglages `joystick plugged …` | `joystick plugged mc42/md45/md10` lus partout |

Le sélecteur `em M-Pump - Brand` reste **automatique** (cabine → HVLP CANopen « gen », X100 → HVLP J1939), comme en 108.3.1 (compatibilite.md §3.2).

## 3.4 Réglages nouveaux de la v2

Tous ajoutés dans le menu existant le plus logique, avec une valeur par défaut qui reproduit la 108.3.1.

| Réglage | Type, états | Défaut | Menu | Pourquoi |
|---|---|---|---|---|
| `T Pump wiring` | SP : Standard, Swapped | Standard | Master Config | D8, D18, D21 (déjà dans la v2 en cours) |
| `Joystick plugged md3` | DP | False | Master Config | joysticks des bateaux lignée B, branchés sur le MD3 (D30) |
| `Cab track tension` | SP : Valve (108), PWM (V25) | Valve | Master Tracks | commande PWM du tendeur des Commuter V25, perdue en 108 (D32) |
| `Cab PWM tension max current` | IP, mA | 900 | Master Tracks | courant max de la valve EM21DEG12 du tendeur PWM (V25.74 : 0 à 900 mA, rampes 250 ms, consigne en % selon `Tension State`) |
| `Accelerometer` | DP | False | Master Features | accéléromètre câblé sur les Commuter (C1:26/36/52) et sur le MD3 VW (D32) |
| `Proemion gateway` | DP | False | Master Features | télémétrie des lignées A V25 et B (D32) |
| `Radio remote` | DP | False | Master Features | radiocommande des bateaux MD3 (`Remote Control` en V35/V69) |
| `MNT Mode` | DP | False | Master System Debug | rend opérants les forçages et tests de `90 MNT` (D36) |

## 3.5 Valeurs par défaut et réglages d'usine

- Tout réglage **ajouté** prend sa valeur par défaut sur un bateau 108.3.1 mis à jour : elle doit donc reproduire le comportement 108.3.1.
- Les **valeurs par défaut des réglages contrat ne changent pas** (une remise aux valeurs d'usine sur un bateau livré doit donner le même résultat qu'avant).
- Une valeur par défaut fausse connue est corrigée par une **décision explicite** et listée dans les notes de version.

## 3.6 Les sélecteurs n'ont pas le même ordre selon la lignée

Le numéro d'état stocké dans un contrôleur n'a pas le même sens d'une lignée à l'autre. Aucun réglage d'une ancienne lignée ne doit donc être recopié par numéro : la migration se fait **par nom d'état** (feuille de migration, [08_compatibilite_migration.md](08_compatibilite_migration.md)).

| Réglage | V25.74 (lignée A ancienne) | V35.42 / V69 (lignée B) | V5.37 (lignée C, MC2) | 108.3.1 et v2 |
|---|---|---|---|---|
| Batterie | 0 Kreisel · 1 BMW · 2 WattAlps | 0 BMW · 1 WattAlps | — | 0 BMW · 1 NovumTech · 2 Tyva · 3 Kreisel |
| Chargeur | 0 Brusa · 1 Elcon · 2 BMW · 3 Valeo | 0 BMW · 1 Brusa · 2 Elcon | — | 0 BMW · 1 Brusa · 2 Elcon |
| Moteur thermique | — | V35 : 0 Ford · V69 : 0 EB2 · 1 Ford | 0 VW 2.0L · 1 Ford 1.5L | 0 EB2 · 1 Ford · 2 Kubota |
| Vitesse CAN moteur | — | `J1939 Speed` 0 = 500 élec · 1 = 250 therm. | fixe | `CAN Speed B mc` 0 = 500 · 1 = 125 · 2 = 250 |
| Verrous | — | V69 : `Number of lockers` 0 One · 1 Two | `Hydraulic Bloc` V01 / V01-Locking / V17-Locking | `T Number of lockers` 0 One · 1 Two · 2 Custom |

## 3.7 Menus

Les menus (noms, codes PIN, visibilité) sont conservés. Changements :

- Tous les réglages `Debug…`, `Force…`, `Test…`, `Sim…`, `bypsass…` rejoignent **Master System Debug** (aujourd'hui visible seulement en électrique : il devient visible pour toutes les propulsions). Ils restent sans effet tant que `MNT Mode` est faux.
- Les réglages en double (`Locking UP Track` ×2, `Tracks pressure Mode` ×2, `Stop Slope`/`Start Slope` ×2, `With tension` ×2…) n'apparaissent plus qu'une fois : l'entrée de menu affiche le paramètre E ou T selon `Drive Type mc` (deux entrées à visibilité exclusive), les deux objets paramètres restant en place (D27).
- Le menu **Delivery date** perd le mot de passe écrit en clair dans une description.
