# Flotte, documents et confrontation au logiciel

Synthèse faite le 23/10/2026 à partir de `docs/` : `variantes/differentes_configurations.txt`, le registre `Registre Flotte Iguana_mod.xlsx`, l'architecture électrique « All » et les plans de faisceaux. Fichiers produits ici :

| Fichier | Contenu |
|---|---|
| [flotte_technique.csv](flotte_technique.csv) | Une ligne par coque : modèle, finition, propulsion, batterie, chargeur, variateurs, moteur, contrôleur et écran (déduits), famille logicielle relevée, état. **Sans données clients.** |
| [index_documents.csv](index_documents.csv) | Les 164 documents techniques classés par équipement, avec leur indice de révision et s'ils contiennent du texte ou seulement un dessin. |
| [faisceaux_vs_logiciel.md](faisceaux_vs_logiciel.md) | Confrontation broche par broche des plans de faisceaux MC42 avec le brochage de la 108.3.1. |

## La flotte en chiffres (registre)

117 coques (#001 à #119). 82 thermiques, 33 électriques, 2 non renseignées.

| Propulsion | Équipement principal | Coques | Période |
|---|---|---|---|
| Thermique | Kohler CH1000 | 1 | #001 (2013) |
| Thermique | VW 2.0 | 12 | #002 à #027 |
| Thermique | Ford 1.5 | 29 | #012 à #067 |
| Thermique | EB2 | 29 | #054 à #117 |
| Thermique | Kubota WG1605 | 3 | #112, #118, #119 |
| Électrique | Kreisel + Brusa + Sevcon | 9 (dont 5 passées depuis sur une autre batterie) | #020 à #036 |
| Électrique | Torqeedo (« BMW » dans le logiciel) + Zapi et/ou Sevcon | 13 | #016 à #068 |
| Électrique | NovumTech + Sevcon | 9 | #043 à #091 |
| Électrique | Tyva + Sevcon | 12 | #010 (refit) à #105 |

Modèles : RIB 42, Original 29, Commuter (cabine) 20, Sport 14, Bow Rider 4, Pro 3, Pro RIB 2, Fisher 2.

## Les familles logicielles réelles

Le registre relève des versions pour 42 bateaux. Le premier nombre de la version identifie une **famille** de projet, née sur une coque donnée :

| Famille | Bateaux concernés | Ce qu'on en sait |
|---|---|---|
| **V5.x** (5.06 à 5.55) | Original thermiques VW / Ford, #007 à #027 | Projet MC2 + MD3 ; nous avons la **V5.37** |
| **V16 / V23 / V25.x** (25.23 à 25.73) | Commuter (cabine) électriques, #023 à #058 | MC42 + MD4-10 ; **projet non fourni** |
| **V35.x** (35.13 à 35.41) | RIB X100 électriques et thermiques, Original électriques, #016 à #062 | **projet non fourni** |
| **V65 / V66 / V69** | 2022 : Novum, Ford, EB2, #066 à #072 | MC42 + MD3 ; nous avons la **V69.03.1** |
| **V76 → V108** | depuis #076 (MD4-5) et Commuter récents | lignée v117 / 108.3.1 |
| V10.8.12 | #010, premier bateau électrique, refit « Aentron » | one-off |

**Conséquence directe** : pour garantir qu'une v2 se charge sur tous les anciens bateaux, il faut aussi les projets **V25 (Commuter)** et **V35 (X100)**, qui couvrent environ 40 bateaux. Ils sont sans doute dans le dossier des versions du firmware que tu proposais de m'envoyer.

## Ce que disent les dossiers SAV (104 cas)

- Les plus fréquents : demandes de pièces (23), entretien (23), chenilles et bras (20). L'IMS électrique compte 6 cas et l'IMS thermique 4.
- **Déséquilibre des cellules Tyva** sur trois bateaux (#010, #102, #104), et une batterie Tyva hors service (#081). La 108.3.1 a ajouté un journal « Balancing TYVA » ; la v2 doit en faire une vraie surveillance avec alerte et statistiques (écart de cellules, équilibrages).
- #020 : « MC42 No contact – switch OFF battery, wait one minute » à répétition. C'est le cas typique où un journal de perte CAN horodaté aurait aidé.
- Surchauffes thermiques (#075), fuite de radiateur hydraulique (#070) : les seuils et journaux thermiques sont déjà présents, il faudra s'assurer qu'ils remontent tous dans les statistiques.

## Équivalences de vocabulaire (code ↔ terrain)

| Dans le logiciel | Sur le bateau / dans la documentation |
|---|---|
| Battery « BMW », Charger « BMW » | Batterie et chargeur **Torqeedo** (cellules BMW i3) |
| Cab, cabine, C10 | **Commuter**, écran MD4-10 |
| x100 | RIB X100 et versions sans cabine |
| M1 / M2 | Moteurs de chenilles SEW droite / gauche |
| M3 / HVLP | Variateur Sevcon HVLP de la pompe hydraulique |
| Keybox X100 E / T, Keyboxs CAB | Keybox IMS électrique / thermique, keyboxes de console Commuter |

## Documents manquants repérés

- Fiche ou notice **MD3** (écran des anciens bateaux) et **MD5** (futur écran).
- Chargeurs **Brusa** et **Elcon** (protocoles CAN).
- **Keyboxes** (X100 et Commuter) et **keypad Blink PKP2400SI** (le projet cite la notice « PKP_2400_SI_CANopen_UM »).
- Moteur **Ford 1.5**.
- Projets IQAN des familles **V25** et **V35**.

## Questions pour Nicolas

1. ~~MC42 sur les Kreisel ?~~ Oui (D19).
2. Les Commuter ont-ils toujours eu le MD4-10, y compris les premiers (#023, #025) ?
3. ~~Coque #001 ?~~ Si possible, sans complexité ajoutée (D20).
4. Voir les questions de [faisceaux_vs_logiciel.md](faisceaux_vs_logiciel.md) (pompes gauche / droite, joysticks, sorties non pilotées en cabine).
