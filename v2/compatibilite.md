# Compatibilité de la v2 avec le parc existant

Exigence : la v2 doit fonctionner sur **tous** les bateaux et équipements que gère la 108.3.1, ainsi que les bateaux anciens encore en service (dont ceux à écran MD3). Ce document dit ce que cela impose, comment on le vérifie, et les cas où ce n'est pas possible ou pas certain.

## 1. Ce qui constitue le « contrat » avec un bateau livré

Un bateau livré garde dans ses contrôleurs ses **réglages** (marque de batterie, type de moteur, vitesses, seuils…) et il est câblé à des **équipements** qui parlent un protocole fixe. La v2 respecte donc, à l'identique :

| Élément | Pourquoi | Vérification |
|---|---|---|
| Nom, type, unité et **ordre des états** de chaque paramètre réglable (SP/IP/FP/DP/TP) | Un SP est stocké comme un numéro d'état : si « Kreisel » passe de la position 3 à 2, un bateau Kreisel se croit Tyva après mise à jour. | automatique |
| Noms des réglages et des menus, codes PIN | procédures de mise en service et de SAV | automatique |
| Trames CAN : identifiant, longueur, position et taille de chaque signal, période | les batteries, variateurs, chargeurs, moteurs et keyboxes ne changent pas | automatique |
| Affectation des broches MC42 / MD4 | câblage existant | automatique |
| Codes et textes des messages (`e1170 Battery Isolation`…) | documentation SAV, habitudes des pilotes | automatique |
| Journaux (event / statistics logs) | historique et diagnostic | automatique |
| Vitesses CAN B/C sélectionnables | voir limite §3.4 | manuelle |
| Comportement fonctionnel par variante | sécurité | essais (§4) |

L'outil [`kb_108_3_1/outils/compat_check.py`](../kb_108_3_1/outils/compat_check.py) compare l'export texte de la version de référence (108.3.1) et celui de la v2 et liste chaque élément supprimé ou modifié. Il a été testé sur v117 → TESTIA 108.3.1 : 1 406 éléments de contrat, 2 supprimés (ancienne trame heartbeat du keypad), 35 ajoutés ([résultat](../kb_108_3_1/compat_v117_vers_108_3_1.md)). **Règle v2 : zéro suppression ou modification non justifiée par écrit.**

## 2. Matrice des équipements gérés (108.3.1 + MD3)

Chaque ligne doit rester sélectionnable en v2, avec la même valeur de réglage.

| Fonction | Équipements (valeur du sélecteur) | Sélecteur / activation |
|---|---|---|
| Propulsion | Électrique (0), Thermique (1) | `Drive Type mc` → `Is_Electric mc` / `Is_Thermic mc` |
| Batterie HT | BMW (0), NovumTech (1), Tyva (2), Kreisel (3) | `eb Battery Brand` |
| Isomètre Tyva | Bender gen1 (0), gen2 (1) | `Tyva gen bender` |
| Chargeur | BMW (0), Brusa (1), Elcon (2) ; tension réseau 230 V / 110 V | `ec Charger Brand`, `ec AC Voltage Range` |
| Variateurs chenilles | Sevcon gen4 (0), Zapi (1) ; nœud Zapi 8-10 / 1-4 / 4-8 | `em1 M-Track - Brand`, `em ZAPI Node` |
| Pompe hydraulique M3 | Sevcon gen (0), Sevcon J1939 (1) | `em M-Pump - Brand`, **non réglable** : suit `is_x100_math` (x100 → J1939, cabine → gen) |
| Moteur thermique | EB2 1.2L (0), Ford 1.5L (1), Kubota WG16 (2) | `T Engine type` |
| Configuration | x100 (0) / cabine (1) | `is_cab_mc` |
| Écrans | MD4-10 cabine, MD4-5 tableau (chacun optionnel) | modules optionnels |
| Joysticks | MC42, MD4-10, MD4-5, ou capteur de niveau d'eau | réglages `joystick plugged …` |
| Hors-bords (NMEA) | Mercury (0), Yamaha (1), COX (2) | `md4 Engine Brand` |
| Keyboxes | X100 E, X100 T, cabine KTB/KBB/KTC | activation par variante |
| Options | siège électrique, gonflage 24 V, clim Tyva 24 V, verrous 1/2/custom, blocs d'atterrissage 1/2… | réglages Master Features / Options |
| Keypad Blink PKP2400SI | sans (défaut) / avec | réglage `Keypad 8 keys` (108.3.1), relevage par keypad en thermique uniquement |
| Écran MD3 | bateaux anciens, encore nombreux | **absent de la 108.3.1**, voir §3.1 |

## 3. Cas où la compatibilité n'est pas garantie — décisions à prendre

### 3.1 Écran MD3 (« d3 ») — à maintenir (réponse du 22/10/2026)
De nombreux bateaux en exploitation ont encore un MD3 et doivent rester maintenus. Or ni la v117 ni la 108.3.1 ne déclarent de module MD3 : seul subsiste côté MC42 le groupe `mc.d3 Screen State`, dont la plupart des canaux ne sont plus lus. Ces bateaux tournent donc forcément sur un **autre projet** (plus ancien).
- La v2 **peut** les couvrir : IQAN permet des modules optionnels, comme le sont déjà les deux MD4. Il faut ajouter un module MD3 optionnel, son application et ses pages, et rebrancher `mc.d3 Screen State`.
- **Reçu le 22/10/2026** : deux projets MD3, analysés dans [../kb_md3_v69/](../kb_md3_v69/README.md) (MC42 + MD3, EB2/Ford) et [../kb_vw_v537/](../kb_vw_v537/README.md) (**MC2** + MD3, VW 2.0L/Ford). Ce sont deux projets distincts de la 108.x : leurs réglages ne passeront pas automatiquement, il faudra une migration (voir [methode.md](methode.md)). Les bateaux MC2 ont un câblage différent et auront leur propre application v2.
- **Écart à vérifier en priorité** : les sorties de pompe `COUT 0`/`COUT 1` sont « Pump 1 Right »/« Pump 2 Left » en V69 et V5.37, inversées en 108.3.1.
- À vérifier ensemble : un MC42 et ses réglages MD3 actuels doivent rester lisibles par la v2 ; si le projet MD3 a des paramètres que la 108.3.1 n'a pas (ou dans un autre ordre), la v2 devra les reprendre à l'identique, ce qui peut entrer en conflit avec la 108.3.1. L'outil `compat_check.py` le dira dès que j'aurai l'export.

### 3.2 Pompe électro-hydraulique HV pilotée par le HVLP — confirmée
Le groupe s'appelle `broeknE.Sevcon.M3.gen.soon` et son module `Sev_M3_HVLP_soon`, mais il est en service : `em M-Pump - Brand` le choisit automatiquement **dès que le bateau est configuré en cabine** (`is_cab_mc` vrai), et tu as confirmé que ces bateaux ont bien la pompe HV pilotée par le HVLP. La v2 garde ce groupe et ce choix automatique à l'identique ; seul son nom trompeur sera documenté (le renommer changerait le contrat).

### 3.3 Corrections de bugs qui changent un comportement
Corriger les anomalies de priorité 1 (Kreisel sans message d'isolement, fin de charge Kreisel, message pompe M3 J1939) **modifie volontairement** le comportement de ces variantes. C'est compatible au sens du câblage et des réglages, mais un bateau Kreisel s'arrêtera de charger plus tôt qu'avant et affichera un message qu'il n'affichait pas. Chaque correction sera listée dans les notes de version et validée au cas par cas.

### 3.4 Port CAN B partagé
Les keyboxes cabine (125 kb/s) et les moteurs thermiques J1939 (250 kb/s) sont sur le même port B du MC42, donc incompatibles entre eux. La v2 conserve cette limite telle quelle (la lever demanderait un changement de câblage).

### 3.5 Valeurs par défaut des nouveaux réglages
Un réglage **ajouté** en v2 prend sa valeur par défaut sur un bateau mis à jour. Chaque nouveau réglage doit donc avoir une valeur par défaut qui reproduit exactement le comportement 108.3.1.

## 4. Validation avant diffusion

1. `compat_check.py` 108.3.1 → v2 (et projet MD3 → v2) : zéro suppression ou modification non justifiée.
2. `anomalies.py` sur la v2 : aucun canal à sélecteur avec une fonction vide non commentée, aucune trame de sécurité sans timeout.
3. Essais sur banc (IQANsimulate ou contrôleur de test, **jamais** sur un bateau sans accord) pour chaque ligne de la matrice §2 : démarrage, translation, relevage, charge, arrêt, défauts CAN simulés.
4. Mise à jour d'un contrôleur de test qui a des réglages 108.3.1 et d'un autre avec des réglages MD3 « réels » (export des paramètres d'un bateau) puis relecture des réglages : ils doivent être identiques.
