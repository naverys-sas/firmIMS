# Architecture du firmware v117

Synthèse rédigée à partir des fiches générées (`fonctions/`). Chaque affirmation se vérifie dans la fiche du canal cité.

## 1. Matériel et applications

```
 MC42 port C (vitesse « Can Speed C » : 500 ou 125 kb/s), trames 11 et 29 bits
   batteries BMW · NovumTech · Tyva (+ isomètre Bender) · Kreisel
   chargeurs BMW · Brusa · Elcon        variateurs chenilles Zapi ou Sevcon gen4
   pompe M3 Sevcon « gen »              Keybox X100 E / T      Keypad PKP2400SI
 MC42 port B (vitesse « Can Speed B » : 500, 250 ou 125 kb/s)
   J1939 : moteurs EB2 · Ford · Kubota, onduleur pompe M3 Sevcon J1939 (adresse 113)
   générique 11 bits : keyboxes cabine KTB / KBB / KTC
 MC42 port A : bus Master (MC42 ↔ écrans) + bus diagnostic (G1x Bluetooth)

  ┌────────────────┐  Master bus (APPOUT/APPIN)  ┌──────────────────────┐  ┌──────────────┐
  │  MC42-33       │◄──────────────────────────►│ MD4-CAB-40 (C10)     │  │ MD45-ET-39   │
  │  « MC42 app »  │                             │ port C : NMEA Garmin,│  │ écran tableau│
  │  toute la      │                             │ hors-bords (250 kb/s)│  │ MD4-5 (45)   │
  │  logique       │                             │ port D : Tyva 24 V   │  │              │
  └────────────────┘                             └──────────────────────┘  └──────────────┘
```

Les deux écrans sont déclarés **optionnels** (un bateau peut n'avoir que l'un des deux). Aucun module CAN n'a de timeout au niveau module (`Timeout=Not used` partout) : la perte de communication n'est détectée que là où une trame a son propre timeout.

| Application | Rôle | Taille |
|---|---|---|
| **MC42 app** (contrôleur MC42-33) | Toute la logique machine : énergie, propulsion, relevage des chenilles, thermique, équipements, messages d'erreur. | 2 714 canaux |
| **MD4-CAB app** (MD4-10, « C10 ») | Écran cabine : boutons tactiles, joystick cabine, NMEA hors-bords, GPS, batterie 24 V Tyva de la clim. | 402 canaux |
| **MD45-ET app** (MD4-5, « 45 » / « 4ET ») | Écran tableau de bord : 18 boutons, joystick, buzzer, niveau d'eau. | 69 canaux |

Les écrans ne font presque pas de logique : ils **empaquettent les boutons en bits** (`dtob…`, `trameb…`, tableaux ARC) et les envoient au MC42 par APPOUT/APPIN ; le MC42 renvoie de la même façon les états à afficher. La liste exacte des liaisons est dans [interfaces.md](interfaces.md#liaisons-entre-applications-appout--appin).

## 2. Le principe central : un seul logiciel, beaucoup de variantes

Le même programme équipe des bateaux très différents. Deux mécanismes IQAN font la compatibilité :

1. **Groupes activés par un canal** : un groupe entier ne tourne que si son canal « Is_… » est vrai. Exemples : `mc.Electric` ← `Is_Electric mc`, `mc.Thermic` ← `Is_Thermic mc`, `E.BMW` ← `Is_BMW`, `E.Kresel` ← `Is_Kreisel`, `EB2 T45` ← `Is_EB2 mc`, `gen1`/`gen2` (isomètre Bender Tyva), `Keyboxs CAB` ← `is_cab_mc`, `electronic seat`, `feature inflate 24v`, `a/c tyva24v`…
2. **Sélecteurs de fonction** : un même canal a une logique par variante, choisie par un paramètre d'état (SP). Les principaux :

| Sélecteur | Valeurs (0, 1, 2…) | Canaux concernés |
|---|---|---|
| `Drive Type mc` | Electric, Fossil | choix des sorties `… Sel` (électrovannes, boutons) |
| `eb Battery Brand` | BMW, NovumTech, Tyva, Kreisel | 21 canaux génériques batterie (SOC, tension, températures, erreurs, isolement) |
| `ec Charger Brand` | BMW, Brusa, Elcon | chargeur |
| `em1 M-Track - Brand` | Sevcon, Zapi | 20 canaux variateurs chenilles |
| `em M-Pump - Brand` | Sevcon gen, Sevcon j19 | pompe hydraulique M3 |
| `T Engine type` | EB2 1.2L, FORD 1.5L, Kubo | 26 canaux moteur thermique |
| `Tyva gen bender` | gen1, gen2 | isomètre |
| `md4 Engine Brand` | Mercury, Yamaha, COX | hors-bords NMEA |
| `is_cab_mc`, `CAN Speed B/C mc`, `T Number of lockers`, `e Landing Block Number`… | | voir [configuration.md](configuration.md) |

Ces valeurs sont stockées dans chaque contrôleur livré. **Leur nom, leur type et l'ordre de leurs états sont un contrat avec la flotte existante** (voir `v2/compatibilite.md`).

## 3. Les grands blocs du MC42

### 3.1 Énergie électrique (`mc.Electric`, actif si `Is_Electric mc`)

- **E.BATTERY** — « la batterie est le hub » : elle reçoit trois demandes clientes (`IMS engines CMD` = propulsion, `Charger CMD`, `DCDC CMD`) et décide de fermer ses contacteurs.
  - `E.Power Management System` (FSM) : états 0 OFF, 1 Standby, 2 Discharge, 3 Charge, 4 Crash, 5 Charge Aborted, 6 Auto Off. Transitions conditionnées par les demandes, `Battery ERROR DIGIT`, `Battery CHARGED`, `Shutdown CMD`, `Repeated errors locker`.
  - `E.Battery CMD` (FSM) : 0 Off, 1 Stand by, 2 Discharge, 3 Charge ; c'est l'ordre envoyé à la batterie. `Battery Watchdog` compare cet ordre au retour batterie (`Battery State Feed-Back`) et lève une erreur si la batterie ne suit pas.
  - `Battery ERROR DIGIT` = OU des erreurs de chaque marque + watchdog + `IDC Battery Protection` (isolement bas pendant 100 s).
  - Un sous-groupe par marque (E.BMW, E.NovumTech, E. Tyva + bender gen1/gen2, E.Kresel) décode les trames CAN de la marque et fournit des valeurs **normalisées** (SOC, tension, courant, températures cellules, erreurs) via des canaux génériques à sélecteur `eb Battery Brand`.
- **E.CHARGER** — machine d'état `E.Charging State Machine` (0 OFF, 1 Charger Ready, 2 Charging, 3 Finish Charge), consignes tension/courant, un sous-groupe par chargeur (BMW, Brusa, Elcon).
- **E.MOTORS** — variateurs de chenilles M1 (droite) / M2 (gauche) en Zapi **ou** Sevcon gen4, pompe hydraulique M3 (Sevcon « gen » marqué *broken/soon* mais choisi automatiquement en configuration cabine, ou Sevcon J1939 en x100 ; le choix suit `is_cab_mc` via `em M-Pump - Brand`), refroidissement (ventilateur radiateur, pompe à eau).
- **E.Track Up/Down**, **E.Translate**, **E.Track tension**, **E.KeyBox x100 E** — relevage des chenilles, translation (vitesses lente/rapide/libre), tension des chenilles, boîtier à relais X100.
- Gestion de l'arrêt : `System Shutdown` (message interactif), `Global Auto Off Timer`, `Auto Off`, `Keep ON`, `IMS Asks Power`.

### 3.2 Thermique (`mc.Thermic`, actif si `Is_Thermic mc`)

Miroir de l'électrique pour un moteur thermique entraînant la pompe : `T.Power` (démarrage, états thermiques eau/échappement avec hystérésis en Qcode), `T.Oil security`, `T.SAEJ Std engine input`, `T.Engine Speed calc` (consigne de régime), `T.Pump` (courants des pompes 1/2), `T.Engine i/o` avec un sous-groupe J1939 par moteur (EB2, Ford, Kubota : EEC1/EEC2, températures, DM1, TSC1), `T.Thermal Management` (ventilateurs), `T.Translate`, `T.Track tension`, `T.Track Up/Down`, `T.KeyBox x100 T`.

**Point d'architecture majeur :** Translate, Track tension, Track Up/Down et KeyBox existent en **deux copies quasi identiques** (préfixes `E`/`e` et `T`). Les sorties physiques sont ensuite choisies par des canaux `… Sel` (sélecteur `Drive Type mc`), par exemple `EV Lock Sel` = `E EV Lock` en électrique, sa copie `T` en thermique.

### 3.3 Entrées/sorties MC42 (`mc.I/O`)

Électrovannes (EV Tension 58, EV lock 59, EV Up 57, EV Down 42, EV By pass 41, EV unlock 43), capteurs de pression (verrouillage 9, chenilles 10), niveau d'huile (8), batterie 12 V, relais de puissance variateurs (60). Le nombre en fin de nom est la broche du MC42. Liste complète dans [interfaces.md](interfaces.md).

### 3.4 Logique des écrans

- `mc.Link MC42-Screens Logic ims` — reçoit les boutons des deux écrans (tableaux de bits), les joysticks (MC42, MD4-10, MD4-5 ou capteur de niveau d'eau selon la configuration), produit les commandes de démarrage (`Démarrage`), de translation et les retours écrans.
- `logic screen md4` — tout ce qui concerne l'écran 45 : vitesses, relevage (45.UP/DOWN), buzzer, états d'écran et code PIN (`broken PIN Pad 4ET`), envoi des données (`send data to md4`), et trois chantiers marqués **WIP** : contrôle des 10 heures, maintenance annuelle/2 ans/4 ans, date de livraison.
- `logic screen c10 and KB` — écran cabine et les trois keyboxes cabine (13 relais chacune, 42 messages « fuse is blown »), équipements (feux, essuie-glace, guindeau, douche, siège électrique, options).
- `mc.d4s Screen state` et `mc.d3 Screen State` — états affichés ; le second vise un écran **MD3 absent du projet** (aucun module MD3 déclaré) et la plupart de ses canaux ne sont lus par personne.

### 3.5 Nouveauté v117 : Keypad PKP2400SI (Blink Marine)

Le commentaire de version annonce l'ajout du keypad. Dans l'export il n'y a qu'un **squelette** : le module, une trame heartbeat `0x715` (sans timeout), une machine d'état `FSM Keypad X100` avec un seul état et lue par personne, et deux groupes vides (`CAN Keypad X100` dans le MC42, `Keypad PKP 2400SI` dans l'écran 45). La fonction n'est donc pas encore câblée.

## 4. Conventions de nommage observées

| Motif | Sens |
|---|---|
| `E …`, `e …`, `E.` | branche électrique ; `e … mc` = message d'erreur électrique |
| `T …`, `T.` | branche thermique |
| `… mc NN`, `… C41 C2:N`, `… ET45 C2:N` | broche physique (MC42, MD4-10, MD4-5) |
| `… Sel` | sortie choisie selon `Drive Type mc` |
| `eb …`, `ec …`, `em …` | paramètres batterie / chargeur / moteurs (réglables dans les menus Master) |
| `B1…B18`, `Be…`, `debug B…` | bits de boutons transmis entre écrans et MC42 ; les `debug` servent à la mise au point |
| `Is_…` | canal qui active un groupe de variante |
| `… APPOUT` / `… APPIN` | liaison entre applications |

Les noms mélangent anglais et français et contiennent des fautes (`Emmergency`, `Hight`, `Kresel`, `broeknE`, `Punp`, `bypsass`) ; la base les garde tels quels.

## 5. Chiffres de santé

- 274 canaux ne sont lus par aucun autre canal, écran, journal ou réglage ; 110 d'entre eux sont des bits de mise au point (`debug …`, `B…`), 14 visent l'écran MD3 absent, 17 dupliquent le décodage Tyva dans l'écran cabine.
- 35 trames CAN reçues n'ont pas de timeout (dont plusieurs trames batterie).
- 38 réglages de forçage/test/debug sont présents dans les menus (protégés par le PIN Master).
- 6 groupes portent un nom WIP/broken/soon.

Le détail et l'interprétation sont dans [anomalies.md](anomalies.md).
