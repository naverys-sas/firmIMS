# Anomalies et bugs probables — v117

Lecture commentée de [anomalies_auto.md](anomalies_auto.md). Chaque point cite le canal et sa ligne dans l'export ; la fiche complète s'affiche avec `python -I outils/card.py . "<nom du canal>"`. « À confirmer » signifie que la logique est anormale mais qu'elle peut être voulue : seul quelqu'un qui connaît le bateau peut trancher.

## Priorité 1 — peut toucher la sécurité ou une fonction visible

### 1.1 Batterie Kreisel : défaut d'isolement sans message, puis coupure
- `BMW tyva - Isolation Error` (l.8831) a bien une logique Kreisel (`Batt - Iso_Resist <= eb Isolation Protection Level`).
- Mais `Error Iso_Resist` (l.7887) et le message critique `e Battery Protection mc` « e1170 Battery Isolation » (l.12747) ont leur fonction **Kreisel vide**.
- Conséquence : sur une batterie Kreisel, un isolement bas ne déclenche **aucun message**, puis `IDC Battery Protection` (délai 100 s, l.6355) lève `Battery ERROR DIGIT` et la batterie passe en erreur. Le pilote perd la puissance sans avoir été prévenu.
- `Flag Ground Fault Detection` (l.16413) est aussi vide pour Kreisel.
- **À confirmer**, puis compléter les fonctions Kreisel sur le modèle BMW.

### 1.2 Batterie Kreisel : fin de charge jamais signalée par la batterie
- `Battery CHARGED` (l.7462) a une fonction Kreisel **vide**, alors que BMW/Novum/Tyva testent `Battery SOC >= eb Charge Max` ou `Charger asks End Of Charge`.
- La transition *End Of Charge* de `E.Power Management System` ne peut donc jamais se produire en Kreisel ; la charge ne s'arrête que si le chargeur coupe sa demande (*Charger Off*). Le journal « Battery Charged » ne s'écrit jamais.
- **À confirmer** (le BMS Kreisel limite peut-être lui-même le courant), sinon recopier la logique BMW.

### 1.3 Keypad PKP2400SI (objet de la v117) : non câblé
- Commentaire de version : « Rajout du composant Keypad PKP_2400_SI ». Dans le logiciel : module déclaré, trame heartbeat `heart` 0x715 sans timeout, `FSM Keypad X100` à un seul état et lue par personne (l.103375), groupes `CAN Keypad X100` et `Keypad PKP 2400SI` vides.
- Aucun bouton du keypad n'agit sur la machine. Si cette version a été livrée sur le bateau #117, le keypad y est inerte.
- Le projet plus récent `TESTIA.idax` (version 108.3.1) contient le pilotage du keypad (LED, rétroéclairage, nombre de touches, message « Keypad is not working ») : voir [compat_v117_vers_TESTIA.md](compat_v117_vers_TESTIA.md).

### 1.4 Erreur pompe M3 (variante Sevcon J1939) jamais affichée
- `e M3 - Pump Engine CMSG mc` « e1168 Pump Engine » (l.42721) n'a **aucune condition d'affichage** : le message ne peut pas apparaître. La variante « gen » a bien la sienne (`e gen M3 - Pump Engine CMSG mc`).
- Probablement oublié lors de la copie gen → j19. Condition attendue, sur le modèle de la variante gen : `M3 - New Error Code`.

### 1.5 Contrainte matérielle sur le port CAN B
- `CAN Speed B mc` ne propose qu'une vitesse : 500 (électrique), 125 (keyboxes cabine) **ou** 250 (moteur thermique). Les keyboxes cabine et les moteurs J1939 partagent le port B du MC42.
- Un bateau thermique avec cabine à keyboxes ne peut donc pas fonctionner avec les deux. C'est une limite de conception à connaître pour la compatibilité (pas un bug de logique).

## Priorité 2 — robustesse

### 2.1 Pertes de communication CAN
- Aucun module n'a de timeout (`Timeout=Not used` sur les 23 modules CAN).
- 35 trames reçues n'ont pas de timeout (liste dans [anomalies_auto.md](anomalies_auto.md#trames-can-reçues-sans-timeout-perte-de-communication-non-détectée-35)). Pour les batteries, la perte est détectée par **une** trame sentinelle par marque (`SynthesisBMS_M0` Tyva, `BMS_NTHT_Errors novum`, `257 mBMS_FuncSTAT` Kreisel, heartbeats BMW) : si seule une trame de mesure s'arrête, sa valeur reste figée sans alarme. Risque faible (même émetteur) mais réel.
- Sans aucune détection : keypad (`heart`), `GFIN-A:Generic` keybox X100, trames `GFIN-E/F/G` keyboxes cabine (à vérifier : les messages `CanBus Error KTB/KBB/KTC` utilisent peut-être d'autres trames).

### 2.2 État thermique « Low » qui reste vrai
- `T Engine Temp State` (l.57816), fonction *Low* : `static outputValue` passe à True quand l'eau est sous le seuil bas, et **rien ne la remet à False** (pas de `else`). Les fonctions Mid/High/Critical ont une hystérésis, pas Low.
- Effet réel selon la priorité des états de la machine d'état : si un état plus haut gagne toujours, sans effet ; sinon l'état peut rester « Low ». **À confirmer.**

### 2.3 Même identifiant émis plusieurs fois
- Isomètre Bender Tyva : 8 trames différentes émises sur l'identifiant `0x22` (requêtes). Correct si elles sont envoyées à la demande, risqué si plusieurs partent en continu.
- Keyboxes cabine : 4 trames sur l'identifiant `0` (NMT) et 2 sur `ID` (programmation). Probablement voulu (commandes ponctuelles).

### 2.4 Qcode sans branche par défaut
- `T Speed error` (l.60584) : si la consigne vaut 0, `Result` n'est pas affecté. Sans conséquence aujourd'hui car son seul lecteur `T ?Speed OK` n'est utilisé par personne.

## Priorité 3 — maintenabilité (ce que la v2 doit corriger)

| Constat | Ampleur | Exemple |
|---|---|---|
| Logique dupliquée électrique / thermique | Translate, Track tension, Track Up/Down, KeyBox X100 en deux copies (≈ 330 canaux au total) | `Over Tension` existe deux fois, l.48588 et l.68559 |
| Logique dupliquée par variateur | Zapi M1 et M2 : 72 + 71 canaux identiques au suffixe près | `Emmergency Stop - Z.M1.Right` / `Emmergency Stop Left` |
| Canaux lus par personne | 274, dont 110 bits de debug, 14 pour l'écran MD3 absent | groupe `mc.d3 Screen State` |
| Réglages de forçage en production | 38 réglages `Force`, `Debug`, `Test`, `Sim` (protégés par le PIN Master) | `Debug: Mute Battery Error`, `Force EV By Pass`, `bypsass brake T` |
| Fonctions désactivées par un `AND False` | 8 | `Auto Light and Start broken need brightness` (l.91522), `E Don'push button` |
| Chantiers inachevés | 6 groupes WIP/broken/soon | `WIP/45.Maintenance`, `broken PIN Pad 4ET`, `broeknE.Sevcon.M3.gen.soon` |
| Message jamais affiché | `r u sure check 10 hours` (l.3091) | contrôle 10 h en cours de développement |
| Mot de passe en clair | la description du groupe `PIN code delivery date` contient le mot de passe de déverrouillage | à retirer avant de partager le projet |
| Noms en double dans un même groupe | 86 (surtout octets de trames et messages de keyboxes) | `K1 Fault` ×3 dans `Keyboxs CAB` |
| Fautes et langues mélangées | nombreuses | `Emmergency`, `Hight`, `Kresel`, `Punp`, `Démarrage` |

## Faux positifs écartés (vérifiés)

- `Over Tension`, `Keep ON`, `Emmergency Stop …` « se lisent eux-mêmes » : ce sont des bascules auto-maintenues avec un groupe de blocage, conformes à l'usage IQAN.
- `Kreisel - Cell_T_max_Master` ↔ `Cell_T_max_Master` : pas de boucle, ce sont deux canaux homonymes dans deux groupes différents.
- Divisions en Qcode (`Fuel Economy`, `BMW- Max Current`) : protégées par un test préalable.
- Isolement NovumTech volontairement sans action : « no action on iso error on novum based supplier recommandation » (description de `IDC Battery Protection`).
- Modes `STOP` / `Clear ERROR` vides des consignes Brusa : valeur 0 voulue à l'arrêt.
