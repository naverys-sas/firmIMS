# 6. Interface homme-machine

## 6.1 Principe

Les écrans ne décident de rien. Chaque application écran fait deux traductions, et seulement celles-là :

1. **boutons et joysticks locaux → mot de commande** envoyé au MC42 ;
2. **mot d'état reçu du MC42 → pages, voyants, buzzer**.

Toute la logique (qui a le droit de démarrer, quel joystick est actif, quand afficher un message) est dans `80 HMI` du MC42. Conséquence : un nouvel écran (MD5) ou la suppression d'un écran ne touche que son application et le dépaquetage de son mot de commande. C'est l'exigence « préparer MD4 → MD5 » du cahier des charges.

## 6.2 Le contrat IHM

Le contrat est la liste des APPOUT / APPIN entre le MC42 et les écrans, avec la signification de chaque bit. Il est écrit une fois dans [spec/80_HMI.csv](spec/80_HMI.csv) (canaux), [spec/80_HMI_bits.csv](spec/80_HMI_bits.csv) (position de chaque bit) et sa traduction IQAN [iqan/80_HMI.txt](iqan/80_HMI.txt) ; il ne change que par une décision.

### Écran → MC42 (une liaison par écran)

| Liaison | Contenu | Remarques |
|---|---|---|
| `HMI <écran> command word` | bits B1 à B18 (table ci-dessous), mêmes positions pour tous les écrans | reprend les bits de la 108.3.1, déjà partagés entre MD4-5 et MD4-10 |
| `HMI <écran> joystick left`, `… right` | % | seulement si le joystick est branché sur l'écran |
| `HMI <écran> page` | numéro de page active | pour les messages contextuels |
| MD4-10 seulement | `auto off tyva 24v`, `a/c option tyva`, mots équipements cabine (`dtobin c10 B`, `B_1`, `c10_1`) | conservés, renommés `HMI MD410 cab word 1..3` |

Table des bits de commande (positions de la 108.3.1, conservées) :

| Bit | Commande | Bit | Commande |
|---|---|---|---|
| B1 | Up | B10 | Safety off |
| B2 | Down | B11 | Safety off reset |
| B3 | Cancel | B12 | Screen state ok |
| B4 | Slow | B13 | Info page |
| B5 | Fast | B14 | 10 h check certified |
| B6 | Off | B15 | Reset 1-year maintenance |
| B7 | Continue | B16 | Reset 2-year maintenance |
| B8 | Free | B17 | Reset 4-year maintenance |
| B9 | Start / stop | B18 | Super slow |

Anomalie relevée : le MD4-10 envoie « super slow » sur **B14** (`B14 F5 speed super slow C10`) alors que le MD4-5 l'envoie sur B18 et utilise B14 pour le contrôle 10 h. En v2, l'application MD4-10 envoie super slow sur B18 ; le dépaquetage MC42 de l'ancienne position disparaît (D33).

### MC42 → écrans (un seul jeu, lu par tous les écrans)

| Liaison | Contenu |
|---|---|
| `HMI Status word 1` | états système : started, engines ready, battery ok to start, shutdown page, startup page, main page E / T, safety disabled, buzzer request, joystick to zero |
| `HMI Status word 2` | chenilles : speed mode (2 bits), free, up/down state (3 bits), lock state, tension active, tension error |
| `HMI Status word 3` | énergie : PMS state (3 bits), charging state (2 bits), charger connected, battery warning, battery error, isolation low |
| `HMI Status word 4` | thermique : engine state, water temp state (2 bits), oil warning, fan states, fuel line ignition |
| `HMI Values` | SOC, tension et courant batterie, régime ou vitesse, températures (eau, huile, batterie, variateurs), heures, compteur de relevages |

Les mots d'état remplacent `dtobin 2`, `dtobin 3`, `Joystick to zero`, `batt ok to start` et les groupes `mc.d4s Screen state` / `mc.d3 Screen State`. Leur bit-map exact est dans [spec/80_HMI_bits.csv](spec/80_HMI_bits.csv).

## 6.3 `80 HMI` dans le MC42

```
HMI Inputs                  HMI Command arbitration                 logique métier
 MD4-5  command word ─┐
 MD4-10 command word ─┼─► OR des sources par commande ──► CMD Start stop, CMD Up, CMD Down,
 MD3    command word ─┤    (bascules faites ici, une fois)    CMD Speed mode, CMD Free, CMD Cancel…
 Keypad keys        ──┤
 Radio (MD3)        ──┤   joystick : source choisie par     CMD Joystick left / right
 Télécommande cab   ──┘   CFG Joystick source (une seule)
```

- Une commande momentanée est le OU de ses sources ; une **bascule** (Free, Start/stop) n'est faite qu'une fois, ici, sur le OU (corrige le double basculement de Free en cabine, anomalies.md 2.0).
- Le joystick n'a qu'**une** source à la fois, fixée par les réglages `joystick plugged …` (et `Joystick plugged md3`, nouveau). Une source absente (`CFG Has_…` faux) donne 0.
- Les messages (CMSG, IMSG) sont regroupés dans `HMI Messages`, classés par famille (SYS, BAT, CHG, DRV, PMP, ENG, HYD, TRK, KBX, CAB, MNT). Leurs codes et textes sont conservés (contrat SAV).

## 6.4 Les applications écran

| Application | Écran | Particularités conservées |
|---|---|---|
| `MD4-5 app` | MD4-5, tableau de bord, adresse 1 | 18 boutons, joystick local optionnel (C2:1/C2:2), buzzer C2:3, niveau d'eau V10 (C2:1 partagé, D12) |
| `MD4-10 app` | MD4-10, Commuter, adresse 2 | boutons tactiles, joystick cabine, NMEA hors-bords Mercury/Yamaha/COX, GPS Garmin, A/C sur batterie Tyva 24 V (CAN D), boutons cabine et porte |
| `MD3 app` ✚ | MD3, bateaux lignée B, adresse 0 | pages reprises de la V69 (thermique) et de la V35 (électrique), joysticks C2:1/C2:2, buzzer C2:12, radio (option `Radio remote`) |
| `MD5 app` (futur) | MD5 | même contrat ; voir §6.5 |

Chaque application a la même structure : `HMI link` (APPIN/APPOUT et paquetage), `Pages`, `Local I/O`, et ses équipements propres. Les textes sont en anglais. Les pages MD3 électriques (V35) seront reconstruites sur les mêmes mots d'état que les MD4.

## 6.5 Préparer le MD5

Ce que l'on sait (fiche Parker IQAN-MD5) : écran tactile capacitif 5", 8", 10,1" ou 12,3", 3 bus CAN (2.0B et **CAN FD**), 2 ports Ethernet, 9-32 V, IP65. Ce que l'architecture v2 garantit : remplacer un MD4 par un MD5 = créer `MD5 app` qui lit les mêmes mots d'état et produit le même mot de commande ; le MC42 ne change pas, sauf la ligne de dépaquetage de la nouvelle source.

À vérifier avant d'engager le MD5 ([10_besoins_iqandesign.md](10_besoins_iqandesign.md), B9) :
- version d'IQANdesign qui supporte le MD5 (probablement une version 7.x) et si elle ouvre les projets 6.08 sans perte ;
- si un MD5 et un MC42 peuvent cohabiter dans un même projet avec un MD3 et des MD4 (parc mixte) ;
- format des pages : les pages MD4 ne seront pas reprises telles quelles ; prévoir de les redessiner.
