# Proposition de refonte v2

Base : **108.3.1** (TESTIA.idax, keypad Blink complet), décrite dans [../kb_108_3_1/](../kb_108_3_1/README.md) ; la v117 reste documentée dans [../kb_v117/](../kb_v117/README.md). La v2 doit aussi couvrir les bateaux à écran MD3 (voir compatibilité §3.1). Contrainte : compatibilité totale avec le parc, voir [compatibilite.md](compatibilite.md). Méthode de construction (trois lignées, deux applications MC42 et MC2) : [methode.md](methode.md). Journaux unifiés : [journalisation.md](journalisation.md).

> IQANdesign ne réimporte pas de texte. La v2 se construit donc **dans l'IDE**, étape par étape, à partir d'une copie de la 108.3.1. Chaque étape se termine par un export texte et par les deux contrôles automatiques (compatibilité et anomalies). Je peux piloter l'IDE pour les modifications répétitives ; les choix de comportement restent les tiens.

## 1. Objectifs

1. **Corriger** les bugs de priorité 1 de [anomalies.md](../kb_108_3_1/anomalies.md).
2. **Ne plus avoir deux copies** d'une même logique (électrique/thermique, M1/M2) : une correction se fait une fois.
3. **Rendre les variantes complètes par construction** : chaque marque fournit les mêmes informations à la logique commune, et un oubli se voit automatiquement.
4. **Alléger** : retirer ce qui ne sert à rien sans toucher au contrat de compatibilité.
5. **Documenter dans le projet** : noms cohérents, descriptions, conventions écrites.

## 2. Architecture cible (dans le vocabulaire IQAN)

```
MC42 app
├─ 0.Config         paramètres de variante (SP/IP… inchangés), canaux Is_…, constantes
├─ 1.Équipements    un groupe par équipement, activé par son Is_… (drivers)
│   ├─ BAT.BMW  BAT.Novum  BAT.Tyva(+Bender gen1/gen2)  BAT.Kreisel
│   ├─ CHG.BMW  CHG.Brusa  CHG.Elcon
│   ├─ MOT.Zapi  MOT.Sevcon4      PMP.SevconGen  PMP.SevconJ1939
│   ├─ ENG.EB2  ENG.Ford  ENG.Kubota
│   └─ KBX.X100  KBX.Cab  KPD.Blink  NMEA…
├─ 2.Normalisation  un canal générique par grandeur (Battery SOC, Battery Isolation…)
│                   à sélecteur de marque, toutes les fonctions remplies
├─ 3.Métier         Énergie (PMS, charge, arrêt) · Chenilles (translation, tension,
│                   relevage) une seule fois · Thermique · Équipements cabine
├─ 4.IHM            empaquetage des boutons/états vers les écrans (MD4-10, MD4-5,
│                   MD3 optionnel), keypad Blink, messages
└─ 9.Maintenance    debug, forçages, simulation (désactivable d'un seul réglage)
```

Les couches communiquent par **sorties de groupe** (function group outputs) et **entrées de groupe** (FGI) au lieu de canaux visibles partout : on voit immédiatement ce qu'un bloc consomme et produit.

## 3. Chantiers, dans l'ordre

### Étape A — Corrections sûres (comportement corrigé, contrat inchangé)
| Correction | Comment, dans l'IDE |
|---|---|
| Entrée C2:1 du MD4-5 (régression 108.3.1, seulement si joystick branché sur le MD4-5) | Sortir `Left Joy ET45 ou water level C2:1` du groupe `Water level V10 motor` (ou réactiver le groupe) et ne désactiver que la calibration niveau d'eau. |
| Kreisel : message et erreur d'isolement | Remplir la fonction *Kreisel* de `Error Iso_Resist` (`Activating = BMW tyva - Isolation Error`, comme BMW) et de `e Battery Protection mc` (`Showing = Error Iso_Resist`). |
| Kreisel : fin de charge | Fonction *Kreisel* de `Battery CHARGED` : `(Battery SOC >= eb Charge Max) OR (Charger asks End Of Charge)`. |
| Kreisel : défaut de masse | Fonction *Kreisel* de `Flag Ground Fault Detection` selon la doc Kreisel, ou `False` avec une description qui le justifie. |
| Message pompe M3 J1939 | `e M3 - Pump Engine CMSG mc` : `Showing = M3 - New Error Code` (modèle de la variante gen). |
| État thermique *Low* | Ajouter la branche de retour avec hystérésis dans le Qcode de `T Engine Temp State`. |
| Timeouts CAN | Mettre un timeout aux trames reçues qui n'en ont pas et qui portent une valeur utilisée en sécurité ; garder l'identifiant et le contenu. |

Ces corrections changent ce que voit le pilote (§3.3 de la compatibilité) : à valider une par une.

### Étape B — Nettoyage sans effet
- Supprimer les canaux lus par personne **qui ne font pas partie du contrat** (bits `debug …`, `B…` des écrans s'ils ne sont pas transmis ; le groupe `mc.d3 Screen State` est **conservé** puisque les bateaux MD3 restent maintenus). Un canal paramètre, une trame ou un message n'est jamais supprimé à cette étape.
- Retirer les `AND False` en supprimant la fonction morte ou en la remplaçant par un réglage d'option explicite.
- Retirer le mot de passe écrit dans la description du groupe `PIN code delivery date`.
- Ranger les 38 réglages de forçage/debug dans un seul menu **Master System Debug**, déjà protégé par PIN, et ajouter un réglage maître « Mode maintenance » qui les rend inopérants hors maintenance.

### Étape C — Une seule logique chenilles
Les groupes Translate, Track tension, Track Up/Down et KeyBox X100 existent en version E et T. **Ils ont divergé** : sur les canaux communs, seuls 8/17 (tension), 7/17 (translation), 5/21 (relevage) et 5/47 (keybox) ont une logique identique. On ne peut donc pas simplement supprimer une copie.

Méthode :
1. Produire le tableau des écarts canal par canal (script à partir des fiches) et te le faire valider : pour chaque écart, garder E, garder T, ou rendre paramétrable.
2. Créer un groupe unique `Chenilles` dont les entrées (FGI) reçoivent la source propre à la propulsion (vitesse, « système démarré », seuils) via les canaux `… Sel` existants.
3. Garder exactement les mêmes sorties physiques et les mêmes messages (`e Track Tension Error mc` et `T Track Tension Error mc` restent deux messages distincts si leurs codes diffèrent).
4. Essais sur banc en électrique **et** en thermique avant de supprimer les anciens groupes.

Même démarche pour Zapi M1/M2 : un groupe « variateur Zapi » écrit une fois et copié deux fois avec des FGI (nœud, côté). Si IQANdesign 6.08 n'offre pas de groupe réutilisable, la copie reste nécessaire, mais faite d'un seul modèle et vérifiée identique par script à chaque version.

### Étape D — Normalisation des équipements
Pour chaque famille (batterie, chargeur, variateur, moteur), écrire la **liste des grandeurs normalisées** (ex. batterie : SOC, tension, courant, T° cellule min/max, isolement, CAN OK, erreur, fin de charge, autorisation charge/décharge) et vérifier que **chaque marque les fournit toutes**. Le contrôle automatique « aucune fonction vide dans un canal à sélecteur » (déjà dans `anomalies.py`) devient bloquant. Ajouter une marque = remplir une colonne, pas chercher où brancher.

### Étape E — Conventions et documentation
- Préfixes de couche (`CFG`, `BAT`, `CHG`, `MOT`, `ENG`, `TRK`, `HMI`, `DBG`) sur les **nouveaux** canaux uniquement : renommer un paramètre, une trame ou un message casserait le contrat.
- Une description sur chaque canal de sortie de groupe.
- La base de connaissances est régénérée à chaque version (`outils/run_all.sh`) et sert de documentation.

## 4. Ce que je propose de faire ensuite

1. Tu m'envoies le projet `.idax` utilisé sur les bateaux MD3 (compatibilité §3.1).
2. Je réalise l'étape A sur une copie, je l'exporte, je passe les deux contrôles et je te livre le rapport avant/après. Rien n'est chargé dans un contrôleur.
3. Je produis le tableau des écarts E/T de l'étape C pour que tu tranches.

## 5. Exemple : la batterie avant / après

Avant (108.3.1, identique en v117) — `Battery CHARGED`, sélecteur `eb Battery Brand` :
```
BMW       : (Battery SOC >= eb Charge Max) OR (Charger asks End Of Charge)
NovumTech : Novum_EndOfCharge OR (Battery SOC >= eb Charge Max) OR (Charger asks End Of Charge)
Tyva      : (Battery SOC >= eb Charge Max) OR (Charger asks End Of Charge)
Kreisel   : (vide)   ← la charge ne se termine jamais côté batterie
```
Après (v2) — même canal, même nom, mêmes délais :
```
BMW       : inchangé
NovumTech : inchangé
Tyva      : inchangé
Kreisel   : (Battery SOC >= eb Charge Max) OR (Charger asks End Of Charge)
```
Et la règle automatique qui aurait signalé l'oubli : « canal à sélecteur `eb Battery Brand` : fonction *Kreisel* vide ».
