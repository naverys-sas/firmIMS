# Cahier des charges de la refonte (réponses de Nicolas, 23/10/2026)

| Sujet | Décision |
|---|---|
| Stockage | Tout va dans le dépôt privé GitHub `naverys-sas/firmIMS`, y compris le registre des bateaux et les fiches techniques. |
| Versions en service | Connues seulement en partie (colonne du registre). Le dossier complet des versions IQAN peut être fourni : on en tire les exports texte pour l'historique ; les `.idax` volumineux restent hors du dépôt si nécessaire. |
| Priorité | Un code propre, modulaire, maintenable, professionnel. Pas d'autre priorité pour l'instant. |
| Variantes à abandonner | Aucune : la refonte doit pouvoir être chargée aussi sur d'anciens bateaux. Exception (23/10/2026) : #026 et #043 (branches V35.38.01 / V35.40) ont été refités, inutile de les supporter (D22). |
| Évolutions à prévoir | Nouveaux variateurs, moteurs, batteries HT… (non définis) ; **remplacement du MD4 par le MD5** à préparer dans l'architecture. |
| Langue des écrans | Anglais uniquement pour l'instant. |
| Qui maintiendra | Des collègues de Nicolas : documentation et conventions doivent permettre à un autre développeur de reprendre le code. |
| Banc d'essai | Aucun pour l'instant ; piste à étudier : simulation IQANdesign (jumeau numérique des bateaux et de leur interface). |
| Matériel et faisceaux (23/10/2026) | Objectif permanent du projet : **simplifier, épurer et standardiser le matériel** entre contrôleur, écran et équipements, faisceaux compris. Claude proposera de nouveaux schémas de câblage simplifiés, avec si possible moins de fusebox et de keybox, plus standardisés d'un modèle à l'autre. **Ce sont des propositions pour les bateaux futurs** : le code doit rester rétroactif et compatible avec tous les faisceaux existants (D37). |
| Ce qui doit disparaître | Le désordre, l'illisibilité, l'incohérence laissés par une dizaine de développeurs successifs ; la complexité inutile, source de pannes. Objectif : reprendre la connaissance et la maîtrise du code, pouvoir dépanner les vieux bateaux et faire évoluer les nouveaux. |

## Conséquences pour la conception

- Une couche « équipement » par famille avec une interface fixe, pour qu'un nouveau variateur, moteur, batterie ou écran (MD5) se branche sans toucher à la logique métier.
- L'IHM isolée de la logique : les écrans ne lisent que des canaux d'état publiés par la logique, ce qui rend le passage MD4 → MD5 local.
- Simplicité d'abord : chaque canal doit avoir une raison d'exister, un nom clair, une description ; suppression des doublons et des copies divergentes.
- Lisibilité graphique : blocs placés et alignés (pas d'empilement), groupes de taille raisonnable, commentaires dans les schémas.
- Documentation régénérée à chaque version et journal des décisions tenu à jour.
- Chaque choix d'architecture logicielle est aussi jugé sur ce qu'il permettra de simplifier dans les faisceaux futurs, sans jamais retirer le support d'un câblage existant.
