# Essai : Claude écrit directement les fichiers projet IQAN

23/10/2026. Question posée : Claude peut-il écrire lui-même les fichiers `.idax` / `.idsx` d'IQANdesign 6.08, au lieu de saisir la refonte v2 en pilotant l'interface ?

## Verdict : faisable

En une demi-journée, le format a été décodé assez loin pour que des fichiers modifiés par Claude soient acceptés par IQANdesign. L'export texte de chacun est identique à l'original, à la modification voulue près. Tout a été fait sur des copies, sans aucun contrôleur.

| Essai | Modification faite par Claude dans le binaire | IQANdesign |
|---|---|---|
| T1 | Texte d'un commentaire (MD3 V69) | accepté, seule différence attendue |
| T4 | Faute « temparture » corrigée dans un message (v2 MC42, 29 Mo) | accepté, seule différence attendue |
| T2, T3 | Checksum du fichier faux ; checksum d'un bloc faux | refusés, comme prévu : nos checksums sont donc bien ceux d'IQANdesign |
| E1 | Temporisation `Delay on` 1000 → 1500 ms | accepté, seule différence attendue |
| E2 | Sélecteur de fonction retiré | accepté ; la fonction s'appelle alors « Default function », comportement normal d'IQANdesign |
| C1 | **Ajout** d'un commentaire dans un groupe | accepté |
| C2a | **Ajout** d'un canal paramètre (IP) en fin d'application | accepté, le canal apparaît avec ses valeurs |
| C2c | **Ajout** d'un canal au milieu d'un groupe, avec renumérotation des canaux suivants | accepté ; toutes les références existantes (opérandes, entrées, sélecteurs, sorties de groupes, scripts) restent justes |
| C2, C2b | Même ajout au milieu, sans renumérotation | plantage d'IQANdesign. C'est ce qui a montré que la renumérotation est obligatoire. |

Les références entre canaux étaient le point le plus risqué. Les règles de renumérotation ont été validées de deux façons :
- par l'essai C2c ;
- en rejouant ce qu'IQANdesign a fait lui-même entre la 108.3.1 et la v2 (6 canaux ajoutés, 1 121 canaux renumérotés). Une fois nos règles appliquées, tous les objets non modifiés redeviennent identiques à l'octet près.

## Ce qui est acquis (outils dans `outils_format/`)

- **Conteneur** : sections, compression, checksums. Relecture puis réécriture identique à l'octet près sur les 7 projets du dépôt.
- **Textes** : noms, descriptions, messages, traductions. Relus et réécrits à l'identique.
- **Arbre des objets** : structure, identifiants, compteur d'identifiants. Les identifiants sont ceux de l'export texte.
- **Table des symboles** : numérotation des canaux par maître et nombre de canaux.
- **Références entre canaux** : jeton `cf 04 [numéro] 00 [maître]` dans les propriétés, plus les listes de sorties des groupes de fonctions (sans préfixe).
- **Propriétés** : 99,2 % des objets de la 108.3.1 sont reliés à leur équivalent de l'export texte. Les champs typés (textes, entiers, références) se lisent directement.
- **Lecture exacte de chaque objet** (`iqanprops.py`, 23/10) : valeurs typées, enfants et fin propre à chaque classe. Les 99 350 objets des 7 projets se relisent exactement. 84 % des propriétés de l'export texte sont retrouvées (`banc_props.py`), et les codes d'énumération sont appris automatiquement (`iqan_enums.json`, 134 codes).
- **Éditeur** (`iqanprojet.py`, 23/10) : renommer, changer une valeur ou une référence, insérer, supprimer, déplacer, copier un objet ou un groupe (y compris depuis un autre projet), remplacer un groupe en gardant les identifiants des canaux de même nom. La renumérotation, les symboles, les compteurs et les listes de sorties sont recalculés à l'enregistrement. **Lot 4 validé par IQANdesign** : les 6 opérations testées sur une copie du projet MD3 V69 s'exportent sans dialogue, et chaque export montre exactement l'effet voulu. Note : à chaque chargement, IQANdesign crée un groupe « Library image group (legacy) » avec le prochain identifiant libre. Ce groupe change donc de numéro d'un export à l'autre, ce n'est pas une erreur.
- **Code compilé** : IQANdesign ne le régénère pas à l'enregistrement, il le recompile à l'envoi. On n'a jamais à le produire.

## Ce qui reste à faire

Il faut décoder les champs non typés de chaque type d'objet : positions X/Y, listes d'états, tables, détails des trames CAN, pages des écrans… Nos projets utilisent environ 145 types d'objets, dont une quarantaine couvre 95 % des objets.

Le travail est mécanique et se vérifie seul. Pour chaque type, le codeur doit redonner exactement les octets de chaque objet des 7 projets, et le décodeur doit redonner ses propriétés dans l'export texte. On dispose ainsi de plus de 30 000 cas de test sans toucher au PC.

| Étape | Contenu | Estimation (travail Claude dans le cloud) |
|---|---|---|
| 1 | Codeur/décodeur des ~40 types de logique MC42 (canaux, objets mathématiques, machines d'état, fonctions, paramètres, trames CAN, J1939) | 4 à 7 jours |
| 2 | Éditeur de haut niveau : ajouter, supprimer, déplacer et copier des objets et des groupes (y compris entre projets), avec renumérotation automatique | 2 à 3 jours |
| 3 | Écrans MD4 et MD3 (pages, contrôles, images), journaux, réglages | 3 à 6 jours |
| 4 | « Compilateur » : Claude écrit la v2 dans le format de l'export texte, l'outil produit le `.idsx`, IQANdesign le vérifie | 2 à 3 jours |

Les étapes 1 et 2 suffisent à démarrer la refonte de la logique MC42. Les écrans peuvent attendre ou rester modifiés à la main.

## Ce que ça change à l'estimation de la refonte (12_estimation.md)

| Poste | Avant (pilotage de l'interface) | Avec la génération directe |
|---|---|---|
| Saisie PC | 120 à 250 h de pilotage, PC bloqué pendant les glisser-déposer | quasi nulle : quelques minutes par lot pour ouvrir, exporter et vérifier (commande en ligne, sans pilotage de l'écran) |
| Travail cloud | 8 à 15 jours | 8 à 15 jours de conception (inchangé) + 10 à 20 jours d'outillage (tableau ci-dessus) |
| Consommation | plusieurs centaines de millions de jetons de captures d'écran ; Max 5x ou 20x recommandé | du travail cloud ordinaire, sans captures d'écran ; Pro peut suffire en étalant, Max 5x pour aller vite |
| Calendrier | 2 à 4 mois, limité par les créneaux PC | 1 à 2 mois, limité surtout par tes validations et les essais à quai |
| Copie entre projets (MD3, MC2) | dépendait de l'essai B13 dans IQANdesign | faite par l'outil : même format, mêmes règles |
| Glisser-déposer des paramètres (B1) | geste à la souris, non automatisable de façon fiable | déplacement d'objet dans l'arbre en gardant son identifiant, donc les réglages des bateaux |

Les gestes que seul IQANdesign peut faire restent les mêmes : envoyer le programme au contrôleur et lire les journaux. Ils restent faits par toi, avec ton accord à chaque fois.

## Risques et garde-fous

- **Format non documenté par Parker.** Une future version d'IQANdesign peut le changer. On reste donc en 6.08 pendant la refonte, et chaque fichier généré est validé en le rouvrant dans IQANdesign, avec comparaison de l'export texte.
- **Un fichier mal formé fait planter IQANdesign au chargement** (vu sur C2 et C2b). Il ne passe pas inaperçu. Le contrôle par export texte reste obligatoire avant tout envoi à un contrôleur.
- **Licence et support.** On modifie nos propres projets, pour l'interopérabilité. Le programme envoyé aux machines reste compilé par IQANdesign.

## Fichiers

- Outils : [`outils_format/`](../../outils_format/README.md). Scripts des essais : `outils_format/essais/`.
- Résultats des exports sur le PC : `Documents\testia\essais_format\lot1\` et `lot4\`. Lot 3 : `Documents\testia\.claude\worktrees\intelligent-golick-ac697c\essais_format\lot3\`.
