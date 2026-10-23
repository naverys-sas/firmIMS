# Journalisation v2 : tout enregistrer, partout pareil

Exigence (22/10/2026) : le firmware doit produire le maximum de journaux, événements et statistiques, **uniformisés par le haut** sur toutes les variantes et toutes les lignées, pour faciliter le dépannage et les statistiques de flotte.

## Constat

| Lignée | Journaux d'événements | Journaux de statistiques |
|---|---|---|
| MD3 V69 | Check UP, Hydraulic Event, Thermic Events | System Stats, Thermic Stats |
| 108.3.1 | + Electronic logs, Battery Isolation, BMW Battery, Tyva Battery, New event log (Tyva), Inspections, Novum battery, Balancing TYVA | + Electronic Stats logs |
| VW V5.37 | à analyser (export bloqué par le mot de passe) | |

Trous dans la 108.3.1 : rien pour **Kreisel**, rien pour les **chargeurs** (BMW, Brusa, Elcon), rien pour le **keypad**, la raison d'un **arrêt** (auto-off, crash, coupure demandée) n'est pas enregistrée, pas de statistique de charge (nombre de charges, énergie, durée), les journaux BMW n'ont que deux entrées, un journal s'appelle encore « New event log ».

## Principe v2 : une grille commune, remplie par chaque équipement

Chaque famille d'équipement remplit **les mêmes lignes**, quelle que soit la marque, grâce à la couche de normalisation de la v2. Un équipement absent laisse ses lignes vides ; aucune variante n'a moins de journaux qu'une autre.

### Événements (horodatés)
| Catégorie | Contenu minimal |
|---|---|
| Système | mise sous tension, démarrage, arrêt **avec sa cause** (bouton, auto-off, crash, batterie basse), changement de version, réglage modifié en menu Master |
| Batterie | changement d'état PMS, erreur (code brut de la marque + code normalisé), isolement bas avec la valeur, perte CAN, fin de charge |
| Charge | début, fin, arrêt anormal, erreur chargeur (code brut), tension réseau |
| Propulsion | erreurs et alertes variateurs/moteur (code brut), surchauffe, arrêt d'urgence |
| Hydraulique / chenilles | défaut de tension, pression, niveau et température d'huile, relevage interrompu |
| Thermique | démarrage/arrêt moteur, alertes eau/échappement/huile, DM1 reçus |
| IHM | code PIN faux, keypad hors service, perte d'un écran |
| Maintenance | contrôle 10 h, maintenances 1/2/4 ans, forçage ou mode debug activé |

### Statistiques (compteurs persistants)
Heures de fonctionnement par organe (système, batterie, variateurs M1/M2/M3, moteur thermique, pompe), nombre de démarrages, de relevages, de charges, énergie chargée et déchargée, températures max (batterie, cellules, moteur, huile), SOC minimum atteint, nombre d'erreurs par catégorie.

## Règles de mise en œuvre

1. Noms de journaux et d'entrées **stables et préfixés par catégorie** (`SYS`, `BAT`, `CHG`, `MOT`, `HYD`, `ENG`, `HMI`, `MNT`) : ils deviennent un contrat, comme les messages.
2. Les journaux existants sont **gardés sous leur nom** (les historiques déjà sur les bateaux restent lisibles) ; la grille commune s'ajoute à côté.
3. Chaque entrée enregistre la valeur utile (code brut, valeur mesurée), pas seulement « erreur ».
4. Limite à vérifier : la capacité de stockage des journaux du MC42 et des MD4 (nombre d'entrées par journal, taille totale) ; les événements très fréquents passent en statistiques plutôt qu'en événements.
5. `anomalies.py` vérifiera qu'aucune famille n'a de ligne de la grille non câblée.
