# 8. Compatibilité avec la flotte et migration

Exigence (D1) : la v2 doit pouvoir être chargée sur **tous** les bateaux en service, anciens compris ; tout ce qui ne peut pas être garanti est signalé ici. Ce document complète [../compatibilite.md](../compatibilite.md) (le « contrat » d'un bateau livré) avec la vue par lignée et la procédure de migration.

## 8.1 Qui reçoit quoi

Compté sur [../../kb_flotte/flotte_technique.csv](../../kb_flotte/flotte_technique.csv) (bateaux ni retirés ni non construits). La colonne « contrôleur » du registre est une déduction pour les coques anciennes : la famille logicielle relevée prime (une famille V35 implique un MC42).

| Cible | Lignée d'origine | Bateaux | Ce que la mise à jour demande |
|---|---|---|---|
| **v2 MC42-MD4** | A, 108.x / v117 / V76+ (MD4-5 ou MD4-10) | 27 thermiques (#076 à #119) et ~13 électriques récents (#064 à #105) | flash ; **réglages conservés** (paramètres jamais coupés / collés, B1) ; contrôle à quai |
| **v2 MC42-MD4** | A, V23 / V25 (Commuter MD4-10) | #023, #025, #028 à #038, #051, #058 (14) | relevé des réglages et journaux ; **adresse MD4-10 0 → 2 et ID-tag MC42 1 → 0** ; flash ; ressaisie complète (ordre des états différent, §8.3) ; `Cab track tension` = PWM si le tendeur est en PWM |
| **v2 MC42-MD3** | B, V69 et V65 thermiques (MC42 + MD3) | 27 thermiques (#035 à #075) | relevé ; flash ; **réglages conservés**, ID-tag inchangé ; `T Pump wiring` = Swapped et `Joystick plugged md3` = vrai par défaut dans ce projet ; contrôle joystick droit = chenille droite (D21) |
| **v2 MC42-MD3** | B, V35 / V65 électriques | 8 électriques (#016, #039, #042, #053, #065, #071, #072, #074) | relevé ; flash ; réglages communs conservés, **réglages électriques ressaisis** (la V69 avait supprimé ces objets) ; contrôles à quai électriques |
| **v2 MC42-MD3** ou **-MD4** selon l'écran | électriques Kreisel Original #020, #032, et #024 (V16) | 3 | contrôleur MC42 (D19), écran à confirmer (MD3 probable) ; version d'origine inconnue : relevé complet sur le bateau avant toute mise à jour |
| **v2 MC2** | C, V5.x (MC2 + MD3) | ~19 thermiques VW / Ford (#002 à #027) | relevé ; flash ; réglages conservés pour les bateaux en V5.37 (projet construit dans une copie de la V5.37), à vérifier pour les V5.x plus anciennes |
| **à décider** | #001 Kohler CH1000 | 1 | couvert seulement si sans complexité (D20) : aucun projet Kohler en notre possession ; par défaut **non couvert** |
| **à décider** | #010, V10.8.12, one-off (refit Tyva + Sevcon) | 1 | contrôleur inconnu (MC2 probable d'après le numéro, mais un MC2 n'a jamais eu de logique électrique dans nos projets) ; à vérifier sur le bateau |
| **hors périmètre** | #026 (V35.38.01, Kreisel), #043 (V35.40, Novum) | 2 | refités, plus à supporter (D22) |

## 8.2 Ce qui est conservé, ce qui ne l'est pas

| Élément | Lignée A 108.x | Lignée A V25 | Lignée B | Lignée C (MC2) |
|---|---|---|---|---|
| Réglages | **conservés** (mêmes objets, B1) | ressaisis | **conservés** (projet construit dans la V69), sauf réglages électriques des V35 | conservés si V5.37 |
| Historique des journaux | conservé (anciens journaux gardés) | perdu → relevé avant | conservé (journaux V69 gardés) | conservé si V5.37 |
| Câblage MC42 | identique | identique, sauf ID-tag | identique | — (projet MC2 propre) |
| Fonctions | toutes, + corrections étape A | + PWM tendeur, accéléromètre, Proemion (repris de la V25) | toutes, + Proemion, radio ; pages MD3 électriques reconstruites | toutes celles de la V5.37 |
| Messages et codes | identiques | codes 108 (différents de la V25 pour certains) | codes 108 pour les fonctions communes, codes V69 conservés pour celles qui n'existent qu'en lignée B | codes V5.37 |

**Fonctions des anciennes versions qui ne sont pas reprises** (aucun bateau du registre ne les utilise ; à confirmer par Nicolas, question Q1) :
- batterie **WattAlps** (V25, V35) ;
- chargeur **Valeo** (V25) ;
- pack de climatisation **Aentron** (V25 ; seul #010 est noté « Aentron », il a été refité depuis) ;
- télécommande **iPhone** (V25).

Si un bateau en a encore une, elle est ajoutée comme une marque ou une option ordinaire ([02_conventions.md](02_conventions.md) §2.7), sans changer l'architecture.

## 8.3 Pièges identifiés

| Piège | Conséquence si on l'ignore | Parade |
|---|---|---|
| L'ordre des états des sélecteurs diffère entre lignées (batterie : V25 0 = Kreisel, 108 0 = BMW ; chargeur : V25 0 = Brusa, 108 0 = BMW) | un Kreisel se croit Torqeedo après mise à jour | migration par **nom d'état**, jamais par numéro ; feuille de migration ; relecture des réglages après flash |
| ID-tag MC42 = 1 sur V25, 0 en v2 MC42-MD4 (la lignée B garde 1 dans la v2 MC42-MD3) | « R3:2 IdTag error », le MC42 ne démarre pas l'application | remplacer l'ID-tag sur les Commuter V25 ; prévoir des ID-tags 0 en stock ; ne jamais charger la v2 MC42-MD4 sur un bateau MD3 |
| Adresse MD4-10 = 0 sur V25, 2 en v2 | écran non reconnu | réglage dans le menu système du MD4-10 |
| Pompe C1:14 : joystick gauche (A) ou droit (B) | chenilles inversées | `T Pump wiring`, contrôle à quai (D21) |
| Joysticks électriques X100 câblés selon le plan #28580 IND H (24 = gauche) | joysticks inversés | contrôle à quai ; réglage `Right Joystick` / `Left Joystick` (étalonnage) |
| Paramètre coupé / collé ou recréé | réglage perdu sur toute la flotte du projet, fonctions dépendantes cassées (B1) | règle D40, contrôle par identifiant interne (`compat_check.py`) avant chaque livraison |
| État ajouté ou retiré à un sélecteur existant | retour au défaut de ce réglage sur toute la flotte | sélecteurs d'extension (D41) ; contrôle du nombre d'états par `compat_check.py` |

## 8.4 Procédure de migration (bateau d'une autre lignée)

1. **Relever** sur le bateau, avec IQANrun ou IQANdesign en mode mesure : version, tous les réglages (export des paramètres), tous les journaux. Les enregistrer dans le dépôt (`flotte/<coque>/avant_v2/`).
2. Remplir la **feuille de migration** de la lignée (générée par `compat_check.py` : ancien réglage → réglage v2, par nom d'état).
3. Commuter V25 seulement : changer l'**ID-tag** du MC42 (1 → 0) et régler l'adresse du MD4-10 (0 → 2).
4. Charger le projet v2 de la lignée (MC42-MD4, MC42-MD3 ou MC2).
5. **Ressaisir** les réglages qui ne sont pas conservés (V25, électrique V35) selon la feuille ; **relire** chaque valeur, conservée ou non.
6. **Contrôles à quai** : sens des chenilles (joystick droit = chenille droite), relevage, tension, démarrage / arrêt, charge (électrique), alarmes CAN (débrancher un équipement).
7. Exporter les réglages après mise à jour, les enregistrer avec ceux d'avant, consigner dans le registre.

## 8.5 Vérifications automatiques à chaque version

- `compat_check.py` : v2 MC42-MD4 contre la 108.3.1 et la V25.74, v2 MC42-MD3 contre la V69.03.1 et la V35.42, v2 MC2 contre la V5.37. Il compare **par identifiant interne** : un paramètre disparu, un identifiant changé ou un nombre d'états différent bloque la livraison sauf décision explicite.
- `diff_versions.py` entre les trois projets, limité aux groupes du socle : toute différence non justifiée est une erreur de report.
- `anomalies.py` étendu : aucune fonction vide non commentée dans un canal d'interface, aucune trame de mesure sans timeout, grille de journaux complète, conventions de nommage respectées.
