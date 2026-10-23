# Refonte de la refonte — conception de la v2

Conception complète de la v2 du firmware IQAN Iguana Yachts, faite le 23/10/2026 à partir de tout le dépôt (bases de connaissances des cinq projets, registre de la flotte, schémas, cahier des charges, décisions D1 à D21). Elle remplace la [proposition_v2.md](../proposition_v2.md), qui partait de la 108.3.1 en la nettoyant ; ici on part du cahier des charges et de la flotte, et on dit précisément quoi construire. Les choix sont numérotés D22 à D36 dans [../DECISIONS.md](../DECISIONS.md).

Ce qui ne peut se faire qu'avec IQANdesign (essais, saisie, export) est listé dans [10_besoins_iqandesign.md](10_besoins_iqandesign.md).

## En une page

- **Deux projets, un socle** : v2 MC42 pour tous les bateaux MC42 (lignées A et B, écrans MD4-5, MD4-10 et MD3 optionnels, électrique et thermique) et v2 MC2 pour les Original VW / Ford. Mêmes couches, mêmes noms, mêmes journaux.
- **Des couches qui ne se parlent que vers le bas** : configuration → broches → pilotes d'équipements → adaptateurs de propulsion → logique métier → IHM ; journaux et maintenance à part. La logique métier ne connaît aucune marque.
- **La propulsion n'est plus un fork** : la logique chenilles produit une consigne gauche / droite et une demande de puissance hydraulique ; seule la couche `30 ACT` sait si elles vont à des variateurs SEW ou à des pompes Rexroth et un régime moteur. Les copies E et T (≈ 330 canaux divergents) disparaissent.
- **Une interface fixe par famille d'équipement** (batterie, chargeur, variateurs, pompe, moteur, keyboxes) : ajouter une marque = remplir une colonne. Les trous actuels sont visibles dans les tableaux de [04_equipements.md](04_equipements.md).
- **Les écrans ne décident rien** : un mot de commande et des mots d'état communs à tous les écrans. Ajouter le MD3 ou passer au MD5 ne touche que l'application de l'écran.
- **Journaux unifiés** : une grille SYS / BAT / CHG / DRV / ENG / HYD / HMI / MNT identique partout, avec la valeur utile à chaque événement ; les anciens journaux restent lisibles.
- **Rien ne casse sur un bateau 108.x** : paramètres, menus, trames, messages et journaux gardent leur nom et leur objet ; tout nouveau réglage a un défaut égal au comportement actuel.

## Ce qui est nouveau par rapport aux analyses précédentes

1. **Adresse du MC42** : il est à l'adresse 1 sur les Commuter V25 et sur toute la lignée B, à 0 en 108.3.1. Un projet ne connaît qu'une adresse : la migration de ces bateaux demande de changer l'ID-tag du MC42 (D24).
2. **Les réglages V25 ne passeront pas en v2** malgré le même identifiant de projet : la 108.3.1 a recréé ses sélecteurs, et leurs états ne sont pas dans le même ordre (batterie : 0 = Kreisel en V25, 0 = BMW en 108). Règle pour la v2 : déplacer les paramètres, ne jamais les recréer (D25), à confirmer par l'essai B1.
3. **Les trois pilotes moteur EB2 / Ford / Kubota sont identiques** (même adresse source, mêmes trames) : un seul pilote suffit (D28).
4. **Anomalies trouvées** : le « courant de sortie » Brusa lit le courant secteur ; le `Ready` du Zapi M1 est forcé à vrai alors que M2 le lit ; le MD4-10 envoie « super slow » sur le bit du contrôle 10 h du MD4-5 ; tous les journaux sont limités à 10 entrées (D29, D33, D34).
5. **Bateaux sans projet connu** : les Novum à MD3 (#065, #071, #072, #074) sont en V65, que nous n'avons pas ; le #010 et les Kreisel Original (#020, #024, #032) sont à vérifier sur place (§8.1).

## Documents

| Fichier | Contenu |
|---|---|
| [01_architecture.md](01_architecture.md) | Projets, couches, arborescence IQAN, règles entre groupes, contraintes matérielles |
| [02_conventions.md](02_conventions.md) | Langue, noms, descriptions, mise en page, objets du contrat, ajout d'une marque |
| [03_configuration.md](03_configuration.md) | Réglages contrat, indicateurs de variante, nouveaux réglages, ordre des états par lignée, menus |
| [04_equipements.md](04_equipements.md) | Interfaces normalisées par famille, marque par marque, avec les cases vides |
| [05_logique_metier.md](05_logique_metier.md) | Adaptateurs de propulsion, énergie, chenilles, hydraulique, thermique, cabine, sous-ensemble MC2, corrections |
| [06_ihm.md](06_ihm.md) | Contrat IHM, arbitrage des commandes, applications écran, préparation MD5 |
| [07_journalisation.md](07_journalisation.md) | Grille d'événements et de statistiques, déclencheurs et valeurs |
| [08_compatibilite_migration.md](08_compatibilite_migration.md) | Qui reçoit quoi, ce qui est conservé, pièges, procédure de migration |
| [09_faisceaux.md](09_faisceaux.md) | Brochage v2 de chaque connecteur (MC42, MD4-5, MD4-10, MD3, MC2), ID-tags, questions de câblage |
| [10_besoins_iqandesign.md](10_besoins_iqandesign.md) | Essais, mesures et saisies à faire sur le PC |
| [11_plan_de_construction.md](11_plan_de_construction.md) | Étapes de construction, chacune livrable et contrôlée |
| [annexes/ecarts_E_T.md](annexes/ecarts_E_T.md) | Les écarts entre copies E et T de la logique chenilles, canal par canal, à trancher |
| [spec/](spec/) | Conception détaillée en tableaux (un CSV par groupe) : la source de vérité |
| [iqan/](iqan/) | Les mêmes tableaux traduits au format texte IQANdesign, à saisir dans l'IDE |

Outils (dans [../../outils_pilotage/conception/](../../outils_pilotage/conception/), Python stdlib) :

```bash
python -I outils_pilotage/conception/gen_iqan.py v2/refonte/spec v2/refonte/iqan          # tableaux -> format IQAN
python -I outils_pilotage/conception/check_spec.py exports/<export>.txt v2/refonte/spec    # export -> conformité
python -I outils_pilotage/conception/ecarts_e_t.py exports/TESTIA_108.3.1.txt > v2/refonte/annexes/ecarts_E_T.md
```

## Questions pour Nicolas

| # | Question | Proposition par défaut |
|---|---|---|
| Q1 | Reste-t-il un bateau avec batterie WattAlps, chargeur Valeo, pack A/C Aentron ou télécommande iPhone ? | non repris (D35) |
| Q2 | D'accord pour changer l'ID-tag du MC42 (1 → 0) sur les bateaux V25 et lignée B lors de leur migration ? | oui (D24) |
| Q3 | Trancher les écarts E/T de l'annexe, ou accepter la règle « chaque propulsion garde son comportement » ? | règle par défaut (D27) |
| Q4 | Le relevage au keypad doit-il aussi marcher en électrique ? | non, comme en 108.3.1 |
| Q5 | #001 (Kohler) et #010 (one-off V10.8.12) : à couvrir ? | #001 non (D20) ; #010 à vérifier sur place |
| Q6 | Valider l'architecture (D23), les conventions (D26) et la grille de journaux (D34) | — |

Questions de câblage F1 à F5 : [09_faisceaux.md](09_faisceaux.md) §9.7.
