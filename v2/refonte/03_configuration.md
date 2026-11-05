# 3. Configuration et réglages

## 3.1 Principe

Un seul logiciel par projet équipe toutes les coques de sa lignée. Ce qui distingue un bateau d'un autre tient dans ses **réglages** (paramètres stockés dans le contrôleur), jamais dans une version de logiciel différente. La v2 range ces réglages en trois catégories :

| Catégorie | Où | Règle |
|---|---|---|
| **Réglages historiques** (existants en 108.3.1, en V69 ou en V5.37 selon le projet) | `00 CFG / CFG Settings (historical)`, où ils sont amenés par glisser-déposer | Identifiant interne, nombre et ordre des états conservés ; renommage autorisé ; jamais de couper / coller (§3.2). |
| **Indicateurs de variante** (dérivés) | `00 CFG / CFG Variant flags` | Canaux `CFG Is_…` calculés à partir des réglages ; ce sont eux qui activent les groupes. Jamais réglables. Seul groupe dont le contenu diffère d'un projet à l'autre. |
| **Réglages nouveaux v2** | `00 CFG / CFG Settings (v2)` | Valeur par défaut = comportement actuel de la lignée du projet (§3.5) ; les sélecteurs naissent avec des états de réserve (02 §2.7). |

## 3.2 Déplacer les paramètres par glisser-déposer, jamais par couper / coller

Ce qu'ont montré les essais B1 et B11 ([../essais/B1_B2.md](../essais/B1_B2.md), manuel IQANdesign p. 314-315) : un contrôleur conserve un réglage lors d'une mise à jour si l'identifiant de projet, l'**identifiant interne du canal** et son **nombre d'états** sont les mêmes. Le nom ne compte pas.

| Action dans IQANdesign | Identifiant interne | Références | Réglage sur les bateaux |
|---|---|---|---|
| Renommer | conservé | suivent le nouveau nom | conservé |
| **Glisser-déposer** le bloc sur un autre groupe de l'arborescence | conservé | intactes | conservé |
| **Couper / coller** | **nouveau** | cassées : les 17 canaux qui utilisaient `eb Battery Brand` comme sélecteur passent à « Undefined » et perdent leurs fonctions | **perdu** sur toute la flotte |

D'où la règle D40, qui précise D25 :
- chaque projet v2 est construit **dans une copie** du projet de sa lignée (108.3.1 + étape A, V69, V5.37) ;
- les paramètres historiques sont regroupés dans `00 CFG / CFG Settings (historical)` **par glisser-déposer uniquement**, puis renommés si besoin (fautes, anglais) ; un bloc déplacé garde ses coordonnées d'origine et doit être rangé ensuite ; le glisser-déposer demande la vraie souris du PC (`outils_pilotage/gui/drag.ps1`), donc un créneau où Nicolas laisse le PC ;
- un canal de logique se déplace de la même façon ; quand on le **réécrit**, on crée le nouveau, on rebranche les lecteurs un par un, puis on supprime l'ancien ;
- après chaque lot de déplacements, l'export texte est comparé à l'export précédent : aucun numéro `BEGIN` de paramètre ne doit changer (`compat_check.py`).

Conséquence pour la flotte V25 : leurs réglages ne passeront de toute façon pas en v2 (la 108.3.1 a recréé ses sélecteurs : `Battery Brand` était l'objet 67686 en V25, `eb Battery Brand` est l'objet 128958 en 108.3.1 ; et l'ordre des états diffère, §3.6). Leur migration inclut une ressaisie complète. Les bateaux lignée B, eux, gardent leurs réglages grâce au projet construit dans la V69, sauf les réglages électriques des V35 que la V69 avait supprimés (08 §8.2).

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
| `CFG Has_MD45`, `CFG Has_MD410` (MC42-MD4), `CFG Has_MD3` (MC42-MD3, MC2) | statut de diagnostic du module (MDGN) = présent, avec délai 2 s ; dans un projet sans le module, constante faux | aucun (aujourd'hui les écrans sont supposés présents) |
| `CFG Joystick source` | état : MC42, MD4-5, MD4-10, MD3, selon les réglages `joystick plugged …` | `joystick plugged mc42/md45/md10` lus partout |

Dans la v2 MC42-MD3 et la v2 MC2, les mêmes indicateurs sont calculés à partir des paramètres de la V69 et de la V5.37 (`T Engine type` V69 : 0 EB2 · 1 Ford ; `Number of lockers` à deux états ; `Hydraulic Bloc` du MC2…, §3.6). Les sélecteurs d'extension (`… Brand ext`, 02 §2.7) entrent dans chaque `CFG Is_…` de marque : `ext = Legacy` et sélecteur historique = marque, ou `ext` = marque.

Le sélecteur `em M-Pump - Brand` reste **automatique** (cabine → HVLP CANopen « gen », X100 → HVLP J1939), comme en 108.3.1 (compatibilite.md §3.2).

## 3.4 Réglages nouveaux de la v2

Tous ajoutés dans le menu existant le plus logique. Un réglage créé par la v2 a un **défaut par projet** qui reproduit le comportement actuel de la lignée : c'est ce défaut que prend chaque bateau à la mise à jour. Si la V69 a déjà un paramètre équivalent (`Remote Control`, Proemion), la v2 MC42-MD3 le garde, renommé, au lieu d'en créer un.

| Réglage | Type, états | Défaut | Menu | Pourquoi |
|---|---|---|---|---|
| `T Pump wiring` | SP : Standard, Swapped | Standard (MC42-MD4), **Swapped** (MC42-MD3) | Master Config | D8, D18, D21 (déjà dans la v2 en cours) |
| `Joystick plugged md3` | DP | **True** (MC42-MD3 uniquement) | Master Config | joysticks des bateaux lignée B, branchés sur le MD3 (D30) |
| `Cab track tension` | SP : Valve (108), PWM (V25) | Valve | Master Tracks | commande PWM du tendeur des Commuter V25, perdue en 108 (D32) |
| `Cab PWM tension max current` | IP, mA | 900 | Master Tracks | courant max de la valve EM21DEG12 du tendeur PWM (V25.74 : 0 à 900 mA, rampes 250 ms, consigne en % selon `Tension State`) |
| `Accelerometer` | DP | False | Master Features | accéléromètre câblé sur les Commuter (C1:26/36/52) et sur le MD3 VW (D32) |
| `Proemion gateway` | DP | False | Master Features | télémétrie des lignées A V25 et B (D32) |
| `Radio remote` | DP | False | Master Features | radiocommande des bateaux MD3 : dans la v2 MC42-MD3, c'est `Remote Control` de la V69, renommé |
| `… Brand ext` (×5) | SP : Legacy, Spare 1 … Spare 7 | Legacy | menu de la famille | nouvelles marques sans toucher aux sélecteurs historiques (D41, 02 §2.7) |
| `MNT Mode` | DP | False | Master System Debug | rend opérants les forçages et tests de `90 MNT` (D36) |

## 3.5 Valeurs par défaut et réglages d'usine

- Tout réglage **ajouté** prend sa valeur par défaut sur un bateau mis à jour : elle doit donc reproduire le comportement de la lignée du projet (108.3.1, V69 ou V5.37).
- Les **valeurs par défaut des réglages historiques ne changent pas** (une remise aux valeurs d'usine sur un bateau livré doit donner le même résultat qu'avant).
- Une valeur par défaut fausse connue est corrigée par une **décision explicite** et listée dans les notes de version.

## 3.6 Les sélecteurs n'ont pas le même ordre selon la lignée

Le numéro d'état stocké dans un contrôleur n'a pas le même sens d'une lignée à l'autre. Aucun réglage d'une ancienne lignée ne doit donc être recopié par numéro : la migration se fait **par nom d'état** (feuille de migration, [08_compatibilite_migration.md](08_compatibilite_migration.md)). Depuis que chaque lignée a son projet (D38), seuls les Commuter V25 et les réglages électriques des V35 sont concernés ; ailleurs, chaque projet garde les sélecteurs de sa lignée tels quels, et c'est `CFG Variant flags` qui traduit leurs numéros en indicateurs communs.

| Réglage | V25.74 (lignée A ancienne) | V35.42 / V69 (lignée B) = v2 MC42-MD3 | V5.37 (lignée C) = v2 MC2 | 108.3.1 = v2 MC42-MD4 |
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
- Une entrée de menu (adjust item) ne fait que pointer vers un paramètre : la déplacer d'un menu à l'autre ne touche pas au réglage. Le rangement des menus est donc indépendant de celui des groupes.
- Dans la v2 MC42-MD3, les menus de la V69 sont conservés (noms, codes PIN) et reçoivent les nouveaux réglages ; leurs libellés passent en anglais sur la même règle que les MD4.
