# 2. Conventions de code IQAN

Ces règles s'appliquent à tout ce qui est créé ou modifié dans la v2. Elles visent un projet qu'un collègue peut ouvrir sans connaître son histoire. Un contrôle automatique (`outils_pilotage/conception/check_conventions.py`, à écrire à l'étape 1 du plan) les vérifie sur chaque export.

## 2.1 Langue

- **Tout en anglais** : noms de groupes et de canaux, descriptions, textes d'écran et de messages (cahier des charges : écrans en anglais). La documentation du dépôt reste en français.
- Les fautes historiques ne sont pas recopiées (`Emmergency`, `Hight`, `Kresel`, `Punp`, `bypsass`, `Démarrage`…), **sauf** dans les objets qui font partie du contrat (§2.6).

## 2.2 Noms de groupes

`NN PFX Name`, où `NN` est le rang dans l'arborescence ([01_architecture.md](01_architecture.md) §1.3) et `PFX` le préfixe de couche. Sous-groupes : `PFX Name` sans numéro. Un groupe de marque porte le nom commercial réel, suivi entre parenthèses du nom historique s'il diffère : `BAT Torqeedo (BMW)`.

## 2.3 Noms de canaux

Forme : `PFX Object quantity`, en minuscules après le premier mot, sans unité dans le nom (l'unité est dans le champ *Unit*).

| Préfixe | Couche / famille | Exemples |
|---|---|---|
| `CFG` | configuration dérivée (les paramètres contrat gardent leur nom, §2.6) | `CFG Is_Electric`, `CFG Is_X100` |
| `IO` | broche physique ; le nom finit par la broche | `IO EV tension C1:58`, `IO Joystick left C1:36` |
| `BAT` `CHG` `DRV` `PMP` `ENG` `KBX` `KPD` `TEL` | interface normalisée d'une famille d'équipement | `BAT SOC`, `DRV M1 speed`, `ENG Coolant temp` |
| `TQD` `NOV` `TYV` `KRS` `BRU` `ELC` `SVC` `ZAP` `HVLP` `J19` | canal interne d'un pilote de marque | `TYV Cell V max`, `ZAP Heartbeat` |
| `ACT` | adaptateur de propulsion | `ACT Pump left current`, `ACT Engine speed request` |
| `PWR` `TRK` `HYD` `THM` `CAB` | logique métier | `PWR System ready`, `TRK Left cmd`, `HYD Oil level low` |
| `HMI` `CMD` | IHM : `CMD` = commande arbitrée, `HMI` = état publié ou paquet | `CMD Start stop`, `HMI Speed mode` |
| `LOG` | canal d'événement destiné à un journal | `LOG BAT isolation low` |
| `MNT` | maintenance, forçage, test, simulation | `MNT Mode`, `MNT Force EV by-pass` |

Côtés : `left` / `right` (jamais `Gauche`/`Droit`, `L`/`R` seuls, ni numéros 1/2 sans côté). Moteurs électriques : `M1` = droite, `M2` = gauche, `M3` = pompe, toujours avec le côté en description.

Booléens : nom affirmatif (`BAT CAN ok`, pas `BAT CAN nok` ni `not …`). État de machine : nom en `state` (`PWR PMS state`).

## 2.4 Descriptions

- **Obligatoire** sur tout canal public (préfixé), tout paramètre, tout groupe et tout journal. Une phrase : ce que c'est, l'unité ou les états, d'où ça vient quand ce n'est pas évident.
- Pour un paramètre : la plage utile et la conséquence d'un mauvais réglage.
- Pour un canal à sélecteur : une ligne par fonction vide qui dit pourquoi elle est vide (`Kreisel: no ground-fault signal on this BMS, see D13`).
- **Jamais** de mot de passe, de code PIN ou de nom de client dans une description (le mot de passe de déverrouillage figure aujourd'hui dans la description du groupe `PIN code delivery date`).

## 2.5 Mise en page des schémas

- Flux de gauche à droite : entrées (FGI, lectures) à gauche, calcul au milieu, sorties publiques à droite.
- Pas de bloc empilé sur un autre ; grille de 20 px ; un groupe tient sur un écran 1920 × 1080 au zoom 100 %. Au-delà de ~40 canaux, on découpe en sous-groupes.
- Un **Comment** IQAN en haut à gauche de chaque groupe : rôle du groupe, entrées, sorties, décisions liées (D…).
- Qcode : seulement quand un objet IQAN ne suffit pas ; toujours une branche `else`/par défaut ; un commentaire par bloc `if`.

## 2.6 Ce qui garde son nom historique (le contrat)

Renommer ces objets casserait un bateau livré ou les habitudes du SAV ([../compatibilite.md](../compatibilite.md) §1). Ils gardent **nom, type, unité, ordre des états et identifiant interne** :

- les paramètres réglables (SP, IP, FP, DP, TP, RP…) et leurs entrées de menu ;
- les menus de réglage (Adjust groups) et leurs codes PIN ;
- les trames CAN (identifiant, longueur, position des signaux) ;
- les codes et textes de messages (`e1170 Battery Isolation`…) ;
- les journaux existants et leurs entrées.

Règle de lecture : un nom sans préfixe de couche est soit un objet du contrat, soit un canal interne à portée privée. Le préfixe `CFG Settings (contract)` du groupe rappelle que les paramètres qui y sont rangés ne se renomment pas.

Un paramètre historique dont le nom est trompeur reçoit une **description** qui corrige, pas un nouveau nom. Exemple : `eb Battery Brand`, état `BMW` → description « BMW = Torqeedo pack (BMW i3 cells) ».

## 2.7 Ajouter une marque d'équipement

1. Ajouter l'état **à la fin** du sélecteur de la famille (`eb Battery Brand` : … Kreisel, *NouvelleMarque*). Ne jamais insérer ni réordonner : un bateau livré stocke un numéro d'état.
2. Créer le sous-groupe pilote `PFX Brand`, activé par `CFG Is_PFX_Brand`, qui ne lit que ses trames et ses FGI.
3. Remplir la fonction *NouvelleMarque* de **chaque** canal d'interface de la famille ([04_equipements.md](04_equipements.md)). Le contrôle automatique refuse un canal d'interface avec une fonction vide non commentée.
4. Ajouter la marque aux journaux (codes d'erreur bruts dans `LOG … raw code`).
5. Noter la décision dans `DECISIONS.md`, régénérer la base de connaissances.

## 2.8 Versions et traçabilité

- `Version` du projet : `2.<étape>.<révision>` (ex. `2.3.0`), commentaire de version = liste des décisions D… intégrées.
- Chaque version enregistrée dans IQANdesign est exportée en texte (`exports/`) et commitée avec son `.idax` ; le message de commit cite les décisions.
- Les champs *Last edited* d'IQAN donnent l'auteur ; le dépôt donne le pourquoi.
