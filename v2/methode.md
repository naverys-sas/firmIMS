# Comment construire la v2

## Ce qu'il faut couvrir : trois lignées, trois matériels

| Lignée | Projet | Contrôleur + écran | Propulsion | Identifiant de projet |
|---|---|---|---|---|
| 108.x (v117, 108.3.1) | `TESTIA.idax` | MC42 + MD4-10 / MD4-5 + keypad | électrique ou thermique (EB2, Ford, Kubota) | `A9A417A5…` |
| MD3 V69 | `avecMD3_V69.03.01.WIP.idax` | MC42 + MD3, radio, Proemion | thermique EB2, Ford | `EF4370B5…` |
| VW V5.37 | `version_avec_MD3_et_moteur_VW_V5.37.idax` | **MC2** + MD3, radio | thermique VW 2.0L, Ford | `D2FDEFEA…` |

Ce sont trois projets différents, pas trois versions d'un même projet. La lignée 108.x a repris la logique thermique de V69 en renommant ses canaux.

## Recommandation : page blanche pour la structure, pas pour la logique

**Oui à une page blanche pour l'architecture** : nouvelle arborescence (configuration, équipements, normalisation, métier, IHM, maintenance, journaux), conventions de noms, grille de journaux commune. Repartir de l'existant en le « nettoyant » laisserait les copies E/T, les canaux morts et les noms historiques en place, et on ne finirait jamais.

**Non à une réécriture de la logique de mémoire.** Chaque fonction est **transplantée** depuis la version qui fonctionne sur les bateaux (copier-coller de groupes entre projets dans l'IDE), puis rangée et corrigée. Dix ans de réglages fins (rampes, délais, hystérésis, séquences de démarrage) sont dans ces groupes : les réécrire, c'est réintroduire des bugs déjà corrigés.

Concrètement :
1. **Un socle commun de blocs** (énergie, chenilles, thermique par moteur, keyboxes, IHM), écrits une fois, chacun avec ses entrées/sorties de groupe documentées.
2. **Deux projets livrables** construits avec ce socle, parce que le matériel l'impose :
   - **v2 MC42** : MC42 + écrans MD4-10, MD4-5 **et MD3** en modules optionnels, électrique et thermique, radio et Proemion en options. Remplace la 108.x **et** la V69.
   - **v2 MC2** : MC2 + MD3, thermique VW/Ford, blocs hydrauliques V01/V17. Remplace la V5.37, avec les mêmes blocs de logique et sa propre couche d'entrées/sorties.
3. **La v2 MC42 part du fichier de la 108.3.1** (copie), dans lequel on construit la nouvelle arborescence à côté de l'ancienne, puis on supprime l'ancienne bloc par bloc. C'est une page blanche dans les faits, mais elle garde l'identifiant de projet de la 108.x, ce qui peut préserver les réglages des bateaux 108.x à la mise à jour (**à vérifier sur banc**).
4. **Migration des réglages** pour les bateaux V69 et V5.37 : leurs projets ont un autre identifiant, leurs réglages ne seront pas repris automatiquement. Je fournis pour chaque lignée une table « ancien réglage → nouveau réglage » générée par `compat_check.py`, et la procédure : relever les réglages du bateau, mettre à jour, ressaisir ou réimporter.

## Garde-fous à chaque étape

- `compat_check.py` contre chaque lignée (108.3.1, V69, V5.37) : aucun écart de câblage, de trame ou de message non justifié.
- `anomalies.py` : aucune fonction vide dans un canal à sélecteur, aucune trame de sécurité sans timeout, grille de journaux complète.
- `diff_versions.py` : chaque bloc transplanté a la même logique que l'original, sauf corrections listées.
- Essais sur banc pour chaque configuration de la matrice, jamais sur un bateau sans ton accord.

## Points à vérifier tôt (ils peuvent changer le plan)

- **Sorties pompes** : `COUT 0`/`COUT 1` sont « Pump 1 Right »/« Pump 2 Left » en V69 et en V5.37, mais inversées en 108.3.1. Soit le câblage des bateaux MD4 est différent, soit les noms sont faux dans l'une des versions.
- **Mise à jour d'un MC42 avec un projet d'un autre identifiant** : que deviennent les réglages et les journaux déjà enregistrés ? Un essai sur banc tranche.
- **Capacité mémoire** du MC42 et du MC2 avec MD3 + MD4 + journaux étendus dans un seul projet.
