# 12. Estimation : temps, consommation, modèle

Estimation faite le 23/10/2026 à partir du plan de construction ([11_plan_de_construction.md](11_plan_de_construction.md)), de la taille des projets et de ce qu'on a appris en pilotant IQANdesign sur le PC. Ce sont des **fourchettes** : la principale inconnue est la vitesse réelle de saisie par pilotage de l'interface, qu'on n'a mesurée que sur quelques actions.

## Taille du travail

| Élément | Ordre de grandeur |
|---|---|
| 108.3.1 (base de la v2 MC42-MD4) | ~15 000 objets nommés dans l'export, ~146 000 lignes |
| V69 (base de la v2 MC42-MD3) | ~3 600 objets |
| V5.37 (base de la v2 MC2) | ~2 900 objets |
| Spécification v2 déjà écrite | 400 lignes de canaux (CFG, BAT, CHG, DRV, PMP, ENG, TRK, HMI, LOG) |
| Canaux à créer, réécrire ou déplacer dans la v2 MC42-MD4 | **1 500 à 2 500** estimés (dont ~300 paramètres à glisser-déposer) |

## Temps

### Cloud (conception, outils, vérification) : 8 à 15 jours de travail Claude

| Travail | Estimation |
|---|---|
| Spécification détaillée des groupes restants (ACT, PWR, HYD, THM, CAB, MNT, KBX, KPD) au format `iqan/*.txt` | 3 à 5 jours |
| Outils (contrôles par identifiant interne, conventions, comparaison du socle entre projets, feuilles de migration) | 2 à 3 jours |
| Vérification de chaque export après saisie, corrections | 2 à 4 jours, étalés |
| Préparation du jumeau numérique (scénarios de test par ligne de la matrice de compatibilité, trames CAN simulées par équipement) | 1 à 3 jours |

Le cloud ne bloque rien chez toi et peut tourner pendant que tu travailles.

### PC (saisie dans IQANdesign par pilotage) : 120 à 250 heures de PC

C'est le gros morceau, et le plus incertain.

| Travail | Estimation | Hypothèse |
|---|---|---|
| v2 MC42-MD4, étapes 2 à 10 | 70 à 150 h | 2 à 4 minutes par canal en pilotant l'écran (capture, clic, saisie, contrôle) |
| Glisser-déposer des paramètres et rangement des blocs | 10 à 20 h | souris réelle, **PC indisponible pour toi pendant ce temps** |
| v2 MC42-MD3 et v2 MC2 | 20 à 40 h si la copie de groupes entre projets marche (essai B13) ; 60 à 100 h sinon | |
| Jumeau numérique IQANsimulate | 15 à 40 h | **si** la licence actuelle permet de simuler un MC42 avec des trames CAN injectées (essai B10, inconnu aujourd'hui) |
| Reprises (coupures du Remote Control, limites d'utilisation, erreurs de saisie) | +20 à 30 % | constaté hier : coupures et limite atteinte le soir |

### Calendrier réaliste : 2 à 4 mois

En comptant 2 à 3 créneaux PC libres de quelques heures par semaine, tes validations (écarts E/T, questions Q1 à Q7), puis les essais à quai d'un bateau pilote par lignée. Avec le PC disponible la nuit et le week-end, le bas de la fourchette est atteignable. Les étapes 2 à 10 peuvent être livrées à la flotte 108.x au fil de l'eau, donc le gain arrive avant la fin.

## Consommation (crédits)

Le pilotage de l'écran est ce qui coûte : chaque action envoie une capture d'écran et relit le contexte. La conception cloud coûte peu en comparaison.

| Poste | Ordre de grandeur |
|---|---|
| Cloud, conception et vérification | quelques dizaines de millions de jetons au total |
| PC, pilotage d'IQANdesign | **plusieurs centaines de millions de jetons**, majoritairement relus depuis le cache |

**Avec l'abonnement Pro (précisé par Nicolas le 23/10/2026)** : Pro a les limites les plus basses (fenêtres de 5 heures et plafond hebdomadaire). Le travail cloud y tient en l'étalant. Le pilotage PC, non : une séance de saisie avec captures d'écran épuise la fenêtre en une heure environ, comme hier soir. À ce rythme, 120 à 250 heures de pilotage prendraient plus d'un an.

| Option | Coût indicatif (prix publics connus, à vérifier sur la page des offres) | Effet |
|---|---|---|
| Rester en Pro | ~20 $ / mois | conception cloud et vérifications oui ; saisie PC surtout faite par toi avec les fiches `iqan/*.txt`, Claude ne pilotant que les glisser-déposer et les lots longs |
| **Max 5x pendant la saisie** | ~100 $ / mois, 2 à 4 mois → **200 à 400 $** | calendrier de 3 à 5 mois, saisie pilotée en séances régulières |
| Max 20x pendant la saisie | ~200 $ / mois, 2 à 3 mois → **400 à 600 $** | calendrier le plus court (bas de la fourchette de 2 à 4 mois) |
| API à l'usage | variable, plusieurs centaines à quelques milliers de $ selon le cache et la part d'Opus | pas de limite de fenêtre, mais coût non plafonné ; déconseillé |

Recommandation : passer en **Max 5x** le temps des étapes de saisie (étapes 2 à 12), revenir en Pro ensuite. L'abonnement se change d'un mois à l'autre.

Trois leviers pour réduire nettement temps et consommation :
1. **Copier plutôt que saisir** : si les essais B5 et B13 montrent que la copie de groupes garde les références, le report vers les projets MD3 et MC2 est divisé par deux à trois.
2. **Toi pour les saisies courtes, Claude pour les longues** : un bloc de 5 canaux te prend 5 minutes avec la fiche `iqan/*.txt`, et coûte plus cher en pilotage qu'il ne rapporte.
3. **Séances longues et préparées** : le cloud prépare la liste exacte des actions avant chaque créneau PC, la séance PC ne fait qu'exécuter et exporter.

## Quel modèle Claude

| Travail | Modèle conseillé | Pourquoi |
|---|---|---|
| Conception, arbitrages, revue des exports, diagnostic d'un écart | **Opus** (le plus capable) | erreurs de logique coûteuses sur une machine en service ; c'est là que la qualité compte |
| Saisie répétitive pilotée dans IQANdesign, à partir d'une fiche précise | **Sonnet** | assez fiable pour exécuter une liste d'actions vérifiée, nettement moins cher et plus rapide ; chaque lot est de toute façon vérifié par l'export et les contrôles automatiques |
| Haiku | déconseillé | pas assez sûr pour une logique de sécurité machine |

Règle proposée : Opus prépare et vérifie, Sonnet exécute au PC, Opus relit l'export de chaque lot avant de passer au suivant.

## Ce qui est incertain

- La vitesse réelle de pilotage par canal (mesurée sur quelques actions seulement) : à recaler après la première étape.
- IQANsimulate : on ne sait pas encore ce que ta licence permet (B10). Si le MC42 ne peut pas être simulé avec des trames CAN, le jumeau numérique se réduit à une simulation des entrées / sorties, ou demande une licence supplémentaire.
- Les copies de groupes entre projets (B13), qui font varier le report MD3 / MC2 du simple au triple.
- Les essais à quai et sur bateau, qui dépendent de la disponibilité des bateaux, pas de Claude.
