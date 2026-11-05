# 7. Journalisation unifiée

Exigence (D7) : le maximum d'événements et de statistiques, **identiques sur toutes les variantes et les trois projets**. Ce document détaille la grille annoncée dans [../journalisation.md](../journalisation.md) : noms des journaux, entrées, déclencheurs et valeurs enregistrées.

## 7.1 Constat 108.3.1

- 10 journaux d'événements et 3 de statistiques ; **taille 10 entrées** pour presque tous (1 pour « Novum battery », 9 pour « Balancing TYVA »). Sur un bateau qui tourne, un événement fréquent efface en quelques jours ce qui s'est passé avant une panne.
- Rien pour Kreisel, les chargeurs, le keypad, les keyboxes, les écrans ; la cause d'un arrêt n'est pas enregistrée ; aucune statistique de charge ; un journal s'appelle « New event log ».
- Les journaux par marque (BMW, Tyva, Novum) ont chacun leur forme ; on ne peut pas comparer deux bateaux.

## 7.2 Principes

1. **Une grille par catégorie, la même pour toutes les marques.** Les entrées lisent les interfaces normalisées (`BAT …`, `DRV …`) ; une marque qui ne fournit pas une donnée laisse son entrée inactive, mais l'entrée existe partout.
2. **Chaque événement enregistre sa valeur utile** (code brut de l'équipement, mesure) : value log item plutôt qu'event log item seul.
3. **Les anciens journaux sont gardés tels quels**, nom et entrées compris : sur un bateau mis à jour, l'historique reste lisible. Ils ne reçoivent plus de nouvelles entrées que si leur déclencheur existe encore. Chaque projet étant construit dans une copie de celui de sa lignée (D38), cela vaut pour les journaux de la 108.3.1, de la V69 et de la V5.37 ; seuls les Commuter V25 perdent leur historique et doivent le **relever avant la mise à jour**. Le relevé reste recommandé partout (procédure de migration).
4. **Ce qui arrive souvent devient une statistique**, pas un événement (ex. démarrage d'un ventilateur).
5. Les déclencheurs sont des canaux `LOG …` rangés dans `85 LOG` : on voit au même endroit ce qui est journalisé et pourquoi.
6. Tailles : **à fixer après mesure de la mémoire disponible** sur MC42 ([10_besoins_iqandesign.md](10_besoins_iqandesign.md), B6). Objectif : 100 entrées pour les journaux d'erreurs, 50 pour les autres. Le MC2 aura des tailles plus petites.

## 7.3 Journaux d'événements v2

| Journal | Entrée | Déclencheur (canal `LOG …`) | Valeur enregistrée |
|---|---|---|---|
| **SYS Events** | System start | front montant `PWR System started` | `BAT SOC` ou `ENG Coolant temp` |
| | System stop | front descendant | `PWR Stop cause` (état) |
| | Screen lost | `CFG Has_MD45` / `Has_MD410` / `Has_MD3` passe à faux moteur en marche | numéro d'écran |
| | Supply low | tension 12 V MC42 sous seuil 10 s | tension |
| **BAT Events** | PMS state change | changement de `PWR PMS state` | nouvel état |
| | Battery error | front montant `BAT Error` | `BAT Error raw code` |
| | Battery warning | front montant `BAT Warning` | `BAT Error raw code` |
| | Isolation low | front montant `BAT Isolation low` | `BAT Isolation` (kΩ) |
| | Ground fault | front montant `BAT Ground fault` | `BAT Isolation` |
| | CAN lost | front descendant `BAT CAN ok` système démarré | — |
| | Watchdog | front montant watchdog batterie | `PWR Battery cmd` |
| | Cell imbalance | `BAT Cell V delta` au-dessus du seuil 60 s | `BAT Cell V delta` (mV) |
| | Battery charged | front montant `BAT Charged` | `BAT SOC` |
| **CHG Events** | Charge start | entrée en état Charging | `CHG Mains voltage` |
| | Charge end | sortie normale (Finish) | énergie de la charge (kWh) |
| | Charge aborted | état Charge Aborted | `CHG Error raw code` |
| | Charger error | front montant `CHG Error` | `CHG Error raw code` |
| **DRV Events** | M1 error, M2 error, M3 error | front montant `DRV Mx error`, `PMP error` | code brut |
| | M1 warning, M2 warning | changement de `DRV Mx warning raw code` non nul | code brut |
| | Motor hot, heatsink hot (M1, M2, M3) | seuils existants | température |
| | Inverter CAN lost (M1, M2, M3) | front descendant `… CAN ok` système démarré | — |
| **ENG Events** | Engine start / stop | existants (Thermic Events) | régime / température eau |
| | DM1 fault | nouveau code DM1 actif | SPN puis FMI (deux entrées valeur) |
| | Coolant temp lost | `ENG Coolant temp lost` (D15) | — |
| | High temp, critical engine / hydraulic / exhaust, bad oil pressure, fuel line ignition | existants | mesure associée |
| **HYD Events** | Oil level very low, bad hydraulic pressure, tension error, oil hot | existants (Hydraulic Event) | mesure |
| | Up/down interrupted | sortie de la machine de relevage sur défaut ou annulation | état de la machine |
| **HMI Events** | Wrong PIN | compteur PIN incrémenté | — |
| | Keypad lost | `KPD CAN ok` faux, keypad configuré | — |
| | Keybox CAN lost | `KBX … CAN ok` faux | numéro de keybox |
| | Fuse blown | front montant d'un `KBX … fuse blown` | keybox × 100 + relais |
| **MNT Events** | Maintenance mode on / off | `MNT Mode` | — |
| | Forcing active | OU des forçages, mode maintenance actif | numéro du forçage |
| | 10 h check, maintenance 1 / 2 / 4 ans | existants (Inspections) | heures IMS |

## 7.4 Journaux de statistiques v2

| Journal | Entrée | Type IQAN | Source |
|---|---|---|---|
| **SYS Stats** | System hours | Hour counter | `PWR System started` |
| | Starts | Counter | front montant `PWR System started` |
| | Up/down cycles | Counter | existant (`Number UP and DOWN`) |
| | MC42 max temperature | Maximum | diagnostic MC42 |
| **BAT Stats** | Battery on hours | Hour counter | existant |
| | Charges | Counter | entrée en état Charging |
| | Energy charged, energy discharged | Counter (kWh × 10) | intégration tension × courant |
| | Max cell temperature, max cell delta | Maximum | `BAT Cell T max`, `BAT Cell V delta` |
| | Lowest SOC | Maximum de (100 − SOC) | `BAT SOC` |
| | Battery errors, isolation events | Counter | événements BAT |
| **DRV Stats** | M1, M2, M3 hours | Hour counter | existants |
| | Max heatsink / motor temperature M1, M2, M3 | Maximum | interfaces DRV / PMP |
| | Inverter errors M1, M2, M3 | Counter | événements DRV |
| **ENG Stats** | Engine hours, starts, max water temp, bad pressure, low oil level | existants (Thermic Stats) | |
| | DM1 faults | Counter | événements ENG |
| **HYD Stats** | Tension errors, oil level alarms | Counter | événements HYD |
| | Max oil temperature | Maximum | C1:25 |

## 7.5 Contrôles automatiques

`anomalies.py` est étendu pour vérifier sur chaque export v2 :
- que chaque entrée de la grille existe dans les trois projets (MC42-MD4, MC42-MD3, MC2) quand la catégorie s'y applique ;
- qu'aucune entrée ne lit un canal de pilote de marque (seulement `LOG …` ou une interface normalisée) ;
- que les anciens journaux sont toujours présents, sous leur nom.
