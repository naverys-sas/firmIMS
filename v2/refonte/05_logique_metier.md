# 5. Logique métier

La logique métier est écrite **une seule fois** pour l'électrique et le thermique. Ce qui diffère réellement entre les deux propulsions est isolé à deux endroits : les pilotes d'équipements (`20 EQP`) et les adaptateurs de propulsion (`30 ACT`). Tout le reste lit des grandeurs normalisées.

Méthode de construction (rappel de [../methode.md](../methode.md)) : chaque bloc est **transplanté** depuis la 108.3.1 (ou la V25 / V69 pour ce qui a été perdu), puis renommé et rangé. On ne réécrit pas de mémoire des rampes, délais et séquences qui ont dix ans de mise au point.

## 5.1 L'idée centrale : une consigne de propulsion, deux façons de l'exécuter

Sur un bateau thermique, les chenilles sont entraînées par deux pompes Rexroth A10VG à cylindrée variable (consigne en courant), le moteur thermique fournit la puissance (consigne de régime), et une troisième pompe alimente le bloc hydraulique. Sur un bateau électrique, chaque chenille a son moteur SEW et son variateur (consigne de vitesse), et le variateur HVLP entraîne la pompe du bloc hydraulique.

Vu de la logique, les deux bateaux font la même chose :

| Besoin de la logique | Canal v2 (produit par) | Électrique (`30 ACT`) | Thermique (`30 ACT`) |
|---|---|---|---|
| Faire avancer la chenille gauche / droite | `TRK Left cmd`, `TRK Right cmd` (%, après rampes) — `50 TRK` | consignes M2 / M1 vers les variateurs (`ACT M2 speed cmd`, `ACT M1 speed cmd`) et frein | courants des pompes C1:14 / C1:15 selon `T Pump wiring`, courbes `T Min current …` |
| Avoir de la puissance pour avancer | `TRK Translate power request` (niveau : lent, normal, rapide) | rien (le variateur suit la consigne) | régime moteur demandé (`T Slow Max Speed`, `T Hight Speed`…) |
| Avoir de la pression hydraulique (relevage, tension) | `HYD Power request` (aucune, relevage, tension) — `50 TRK`, `55 HYD` | vitesse de la pompe M3 (`E Engine hydro speed`, High / Low) | régime `T Tension/UpDown Speed` |
| Savoir si la propulsion est prête | `PWR System started` — `40 PWR` | variateurs prêts (`E Engines Ready`, délais 750 / 500 ms) | moteur démarré (`T System Started DELAYS`) |
| Arrêt d'urgence | `PWR Crash` — `40 PWR` | signal de crash batterie (`System Ask imminent Crash`) | toujours faux |

`ACT Traction` et `ACT Hydraulic power` contiennent chacun deux sous-groupes, `… electric` et `… thermal`, activés par `CFG Is_Electric` / `CFG Is_Thermic`. Ce sont les **seuls** groupes où la propulsion change la logique.

## 5.2 `40 PWR` — énergie et états du système

### PWR System state
- Une machine d'état unique `PWR System state` : Off, Starting, Started, Stopping, Fault. Elle remplace `e System Started`, `T System Started DELAYS`, `Batt or engine started mc`, `Démarrage`, `IMS Asks Power`.
- **Cause d'arrêt** ✚ : `PWR Stop cause` (état) = Button, Auto-off, Crash, Low battery, Battery error, Engine fault, Screen request. Écrite dans le journal système (exigence de [../journalisation.md](../journalisation.md)).
- Auto-off, Keep-on et message d'arrêt repris de la 108.3.1 (`Global Auto Off Timer`, `Auto Off`, `Keep ON`, `System Shutdown`), sans changement de délais.

### PWR Battery management (électrique)
- Machine `E.Power Management System` reprise **telle quelle** (états 0 OFF, 1 Standby, 2 Discharge, 3 Charge, 4 Crash, 5 Charge Aborted, 6 Auto Off), renommée `PWR PMS state`. Ses états sont lus par les journaux : leurs numéros ne changent pas.
- `E.Battery CMD` → `PWR Battery cmd`, `Battery Watchdog`, `IDC Battery Protection` (isolement bas 100 s), `Battery ERROR DIGIT` → `PWR Battery fault`. Elles ne lisent plus que l'interface `BAT …` ([04_equipements.md](04_equipements.md) §4.1).

### PWR Charging (électrique)
- `E.Charging State Machine` reprise telle quelle (0 OFF, 1 Charger Ready, 2 Charging, 3 Finish Charge), consignes tension / courant, fin de charge (`Charger asks End Of Charge`), équilibrage Tyva.
- ✚ Statistiques de charge : nombre de charges, énergie chargée (intégration `CHG Output voltage × CHG Output current`), durée.

### PWR Engine management (thermique)
- Repris de `T.Power`, `T.Oil security`, `T.SAEJ Std engine input`, `T.Engine Speed calc` : démarrage (relais K4/K5 de la keybox), protection du démarreur, allumage ligne carburant, états d'eau / échappement avec hystérésis (D11), consigne de régime.
- La consigne de régime devient la somme arbitrée de `TRK Translate power request` et `HYD Power request`, traduite en tr/min par `ACT` avec les calibrations de `T Engine type`.

## 5.3 `50 TRK` — chenilles

L'annexe [ecarts_E_T.md](annexes/ecarts_E_T.md) liste **canal par canal** les différences entre les copies E et T de la 108.3.1, avec les deux versions côte à côte et une case à cocher. Synthèse et proposition :

| Bloc | Canaux communs / identiques | Nature des écarts | Proposition v2 |
|---|---|---|---|
| Translate | 18 / 7 | rampes et vitesses max (réglages séparés E / T), crash (E), `Joystick to zero` (E), `Engine Stopped` (T) | un bloc ; rampes et vitesses lues dans `TRK Param …` = paramètre E ou T selon `Drive Type mc` (les deux objets paramètres restent, D27) ; crash via `PWR Crash` (faux en thermique) ; « système démarré » via `PWR System started` |
| Track tension | 18 / 12 | délai « besoin de pression » fixe 500 ms (E) ou réglable (T) ; blocage par `Untighten` (T) ; codes de message e1038 (E) / e1043 (T) | un bloc ; délai = 500 ms ou `T Need Pressure Tempo` ; `Untighten` dans les deux (sans effet en E tant que la commande n'existe pas) ; les deux messages gardent leur code, affichés selon la propulsion |
| Track Up/Down | 25 / 14 | modèle de verrouillage : blocs d'atterrissage 1 / 2 (E) ou verrous One / Two / Custom (T) ; by-pass pendant la descente (T) ; vitesse pompe High / Low (E) ; schémas d'écran | une machine de relevage ; temps de verrouillage = `TRK Lock time` choisi selon la propulsion ; by-pass en descente activé par `CFG Is_Thermic` jusqu'à essai en électrique ; vitesse hydraulique via `HYD Power request` |
| Keybox X100 | 55 / 33 | sens des relais K1, K3 à K7 | pilote unique (§4.6), relais commandés par la couche concernée |

Chaque ligne « différente » de l'annexe doit recevoir une décision de Nicolas avant la construction de `50 TRK` (étape 4 du plan, [11_plan_de_construction.md](11_plan_de_construction.md)). Sans décision, la règle par défaut est : **chaque propulsion garde exactement son comportement 108.3.1**, par un choix explicite selon `CFG Is_Thermic`.

### TRK Translate
Entrées : `CMD Joystick left`, `CMD Joystick right` (déjà arbitrés entre MC42, MD4-5, MD4-10, MD3, voir [06_ihm.md](06_ihm.md)), `CMD Speed mode`, `CMD Free`, `PWR System started`, `PWR Crash`.
Chaîne (identique dans les deux copies actuelles) : validation par système démarré et crash → mode de vitesse (Idle, Free, UnFree) → différentiel max en mode UnFree (`Max_differential`) → rampes de démarrage / arrêt selon le mode → `TRK Left cmd`, `TRK Right cmd`.
Supprimé : `Cruise Left` / `Cruise Right` (tables lues par personne).

### TRK Tension
- X100 et thermique : électrovanne de tension C1:58, surveillance de surpression (`Over Tension` → message de tension).
- Commuter V25 (`Cab track tension` = PWM) : consigne PWM du tendeur sur C1:14/39 (COUT-A), reprise de `PWM Pression tendeur` de la V25.74 ; sortie partagée avec la pompe thermique, sans conflit puisqu'un Commuter est toujours électrique (D32).

### TRK Up/Down
Machine de relevage unique (montée, descente, blocage, déblocage, verrous, blocs d'atterrissage), sources de commande : écrans, keypad, télécommande cabine (C1:28/29), radio MD3. Sécurités inchangées (appui maintenu 3 s aux butées pour le keypad, `Force Safety off up/down 45` rangé dans `90 MNT`).
Le relevage au keypad reste **réservé au thermique** comme en 108.3.1 ; l'ouvrir à l'électrique est un changement de comportement à décider (question Q4 du [README](README.md)).

## 5.4 `55 HYD` — hydraulique

Niveau d'huile (C1:8), pression de blocage (C1:9), pression chenilles (C1:10), température d'huile (C1:25 en X100), état de pompe (C1:26 en thermique), sécurité huile. Un seul jeu de seuils pour les deux propulsions ; les événements (niveau très bas, mauvaise pression, défaut de tension) alimentent `LOG HYD …`.

## 5.5 `60 THM` — gestion thermique

- Thermique : ventilateurs arrière / échappement, pompes à eau moteur et échappement (relais keybox X100), temporisations selon `T Ambiante Temperature`, seuils d'eau selon `T Engine type`, tests de ventilateurs (rangés dans `90 MNT`).
- Électrique : ventilateur de radiateur et pompe à eau des variateurs (`em FAN MODE`, `em PUMP VAR MODE`), sur températures `DRV Mx heatsink temp`, `DRV Mx motor temp`, `PMP … temp`.

## 5.6 `70 CAB` — équipements de cabine et options

Repris de `logic screen c10 and KB / cEQUIPEMENT`, `mc.Accesory i/o CAB`, `electronic seat`, `feature inflate 24v` : éclairages, essuie-glace, guindeau, douche, siège électrique (3 personnes), AUX 1 à 5 avec texte et besoin de HT, échelle (capteur Hall, protection), télécommande de relevage, gonflage 24 V. La climatisation sur batterie Tyva 24 V reste dans l'application MD4-10 (la batterie est raccordée au CAN de l'écran).

✚ Accéléromètre (option `Accelerometer`) : lecture X/Y/Z, détection de choc, journal `Acceleration` repris de la V25.74.

## 5.7 Sous-ensemble du projet v2 MC2

Le projet MC2 reprend : `00 CFG` (sous-ensemble thermique + `Hydraulic Bloc` V01 / V01-Locking / V17-Locking), son propre `10 IO` (sorties 2 à 23 du MC2, alimentations directes moteur, démarreur, ventilateurs, PWM de tendeur), `25 ENG` (même pilote J1939), `30 ACT` thermique, `40 PWR` (partie moteur), `50 TRK`, `55 HYD`, `60 THM`, `80 HMI` réduit au MD3 et à la radio, `85 LOG`. La logique est copiée depuis la v2 MC42 une fois celle-ci validée.

## 5.8 Corrections reprises ou à faire au moment de la transplantation

| Point | Origine | Traitement |
|---|---|---|
| Kreisel : isolement, message e1170, fin de charge | D9 | repris |
| Message e1168 pompe M3 J1939 | D10 | repris |
| Hystérésis état thermique « Low » | D11 | repris |
| Groupe niveau d'eau V10 / joystick gauche MD4-5 | D12 | repris ; l'entrée C2:1 sort du groupe désactivable |
| Timeouts CAN et perte de température moteur | D14 à D17 | repris |
| Câblage pompes | D8, D18, D21 | repris (`T Pump wiring`) |
| Brusa : « courant de sortie » = courant secteur | anomalie relevée ici | corrigé : `CHG Output current` lit le courant batterie, le courant secteur devient `CHG Mains current` (D29) |
| Zapi M1 : `Ready` forcé à vrai, M2 lu | anomalie relevée ici | M1 lit le signal Zapi comme M2 ; à valider sur un bateau Zapi (D29) |
| `T Speed error` sans branche par défaut | anomalies.md 2.4 | supprimé (lu par personne) |
| Bouton Free basculé deux fois en cabine | anomalies.md 2.0 | une seule bascule, dans `HMI Command arbitration` |
| Keypad : délai 1 s annoncé / 3 s réel, alerte au pré-opérationnel | anomalies.md 2.0 bis | description alignée, alerte retardée de 3 s |
