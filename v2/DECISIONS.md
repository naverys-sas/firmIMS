# Journal des décisions — v2

Chaque choix de conception de la v2, avec qui l'a pris, quand et pourquoi. On ajoute une ligne à chaque décision ; on ne réécrit pas les anciennes (une décision annulée reçoit une nouvelle ligne qui la remplace).

| # | Date | Décision | Pourquoi | Décidé par | Où dans le projet |
|---|---|---|---|---|---|
| D1 | 22/10/2026 | La v2 doit rester compatible avec tous les bateaux et équipements en service ; tout écart est signalé | Parc installé à maintenir | Nicolas | [compatibilite.md](compatibilite.md) |
| D2 | 22/10/2026 | Version de référence = `TESTIA.idax` 108.3.1 (keypad Blink complet) | Dernière version fonctionnelle | Nicolas | — |
| D3 | 22/10/2026 | Les bateaux MD3 restent maintenus ; la v2 MC42 intègre le MD3 en écran optionnel | Nombreux bateaux MD3 en exploitation | Nicolas | [methode.md](methode.md) |
| D4 | 22/10/2026 | La pompe HV pilotée par le HVLP (« Sevcon gen », choisie en cabine) est conservée telle quelle | Équipement en service | Nicolas | — |
| D5 | 22/10/2026 | Deux livrables : v2 MC42 (108.x + V69) et v2 MC2 (V5.37) ; structure neuve, logique transplantée depuis les versions en service | Trois projets distincts, deux matériels | Nicolas (« go ») | [methode.md](methode.md) |
| D6 | 22/10/2026 | La v2 MC42 est construite dans une copie de la 108.3.1 pour garder son identifiant de projet | Un identifiant différent efface les réglages et repart sur de nouveaux journaux (manuel IQANdesign, « Project ID ») | Claude, validé | [methode.md](methode.md) |
| D7 | 22/10/2026 | Journaux unifiés par le haut sur toutes les variantes | Dépannage et statistiques de flotte | Nicolas | [journalisation.md](journalisation.md) |
| D8 | 23/10/2026 | Le câblage des pompes devient un réglage `T Pump wiring` (Standard = 108.x, Swapped = V69 / V5.37) plutôt qu'un choix figé | La même broche C1:14 est « pompe gauche » en 108.3.1 et « pompe droite » en V69 | Nicolas | `mc.Thermic / T.Pump / pins thermic`, menu Master Config |
| D9 | 23/10/2026 | Corrections Kreisel : défaut d'isolement, message e1170, fin de charge | Fonctions Kreisel vides (bugs) | Claude, étape A validée | [rapport_etape_A.md](rapport_etape_A.md) |
| D10 | 23/10/2026 | Message e1168 de la pompe M3 Sevcon J1939 affiché sur `M3 - New Error Code` | Message sans condition d'affichage | Claude, étape A validée | idem |
| D11 | 23/10/2026 | Hystérésis ajoutée à l'état thermique « Low » | L'état ne se libérait jamais | Claude, étape A validée | idem |
| D12 | 23/10/2026 | Groupe « Water level V10 motor » (MD4-5) réactivé comme en v117 | Sa désactivation en 108.3.1 coupait aussi l'entrée C2:1 partagée avec le joystick gauche du MD4-5 | Claude, à confirmer par Nicolas | idem |
| D13 | 23/10/2026 | Défaut de masse Kreisel laissé tel quel | Signaux BMW/Tyva absents chez Kreisel ; attente doc Kreisel | Claude | — |
| D14 | 23/10/2026 | Timeouts CAN : ajoutés sur les trames périodiques de mesure (délai = celui des autres trames du même équipement), jamais sur les trames d'événement | Valeur figée sans alarme vs faux déclenchements | Nicolas (« ok ») | [timeouts_can.md](timeouts_can.md) |
| D15 | 23/10/2026 | Perte de la température d'eau moteur (moteur en marche) : message critique « e1201 Engine temperature lost » répété toutes les 30 s, sans action automatique | Un timeout seul ferait tomber la température à 0 °C et effacerait une alerte de surchauffe | Nicolas | `mc.Thermic / T.Engine i/o` : `T Engine temp CAN lost`, `T Engine temp lost repeat`, `T Engine temp CAN lost mc` |
| D16 | 23/10/2026 | Batteries Novum, Tyva HT et Tyva 24 V clim : timeouts sur les trames de mesure utilisées, et ces trames ajoutées à la surveillance « CAN OK » de la batterie (perte = perte de communication batterie, comme une perte de heartbeat aujourd'hui). Trames non utilisées ou marquées WRONG (CurrentBattery_M0) et trames d'information (versions) exclues de la surveillance | Éviter des valeurs figées sans alarme, sans créer de fausse perte | Claude, sur la base de D14 | [timeouts_can.md](timeouts_can.md) |
| D17 | 23/10/2026 | Isomètre Bender gen2 : timeout 3 s seulement ; la logique de perte existait déjà (`tyva isomon can ok` teste l'état de la trame) mais ne pouvait jamais se déclencher sans timeout | Correction d'un défaut latent | Claude, sur la base de D14 | idem |
| D18 | 23/10/2026 | Sens physique de la pompe sur C1:14 inconnu : le paramètre `T Pump wiring` reste réglable par bateau, défaut « Standard » = comportement de la 108.3.1 (aucun changement pour la flotte actuelle) ; le nom des sorties devient neutre (« Pump output C1:14 / C1:15 ») au lieu de Left/Right | Le faisceau et la 108.3.1 se contredisent, personne ne sait trancher ; ne rien casser sur les bateaux en service | Nicolas (« prends les dispositions ») | [../kb_flotte/faisceaux_vs_logiciel.md](../kb_flotte/faisceaux_vs_logiciel.md) |
| D19 | 23/10/2026 | Les électriques Kreisel (#020 à #036) ont un MC42 : ils relèvent de la v2 MC42 | Réponse de Nicolas | Nicolas | — |
| D20 | 23/10/2026 | Coque #001 (Kohler CH1000) : couverte si possible sans complexité ajoutée, sinon abandonnée | « si possible oui, sinon tant pis » | Nicolas | — |
| D21 | 23/10/2026 | `T Pump wiring` : défaut = 108.3.1 (lignée A) ; à la migration d'un bateau de la lignée B (V35, V69), régler la valeur inverse puis contrôler à quai joystick droit = chenille droite | V35 et V69 commandent C1:14 avec le joystick droit, la 108.3.1 avec le gauche | Claude, sur la base de D18 | [../kb_flotte/lignees.md](../kb_flotte/lignees.md) |

## D42 — 23/10/2026 — Génération directe des fichiers IQAN plutôt que pilotage de l'interface

Décision proposée : saisir la v2 en faisant écrire les fichiers projet par Claude (outils `outils_format/`), IQANdesign ne servant plus qu'à vérifier (export texte) et à envoyer au contrôleur.
Raison : essai concluant le 23/10/2026 ([essais/generation_directe.md](essais/generation_directe.md)). Textes, valeurs, ajout d'objets et de canaux, avec renumérotation des références, sont acceptés par IQANdesign 6.08. Le pilotage de l'écran était jugé inefficace (120 à 250 h de PC).
Conséquence : on reste en IQANdesign 6.08 pendant la refonte, et chaque fichier généré est vérifié par export texte avant tout envoi.

## D43 — 23/10/2026 — Les conditions de la v2 deviennent des groupes « Expression » d'IQAN

Décision : chaque formule des feuilles v2 (activation, blocage, calcul) est écrite par l'outil dans un groupe d'objets à méthode Expression (script IQAN `Result := …`), au lieu d'être décomposée en objets simples et mathématiques.
Raison : IQANdesign 6.08 a ce type de groupe en natif (736 dans la 108.3.1) et recompile lui-même les objets de calcul à partir du texte au chargement (lot 6, [essais/generation_directe.md](essais/generation_directe.md)). La formule reste lisible telle quelle dans l'IDE et dans l'export texte (« Qcode expression »), ce qui sert l'objectif de lisibilité pour les collègues.
Conséquence : la spec doit contenir de vraies formules. Les 79 formules encore écrites en clair ou qui citent des canaux non définis (PWR, KPD, KBX, MNT…) sont à compléter avant l'assemblage.

## D44 — 23/10/2026 — La v2 se branche sur l'existant de la 108.3.1 par des liens nommés

Décision : une ligne de spec avec la propriété `existing=Nom` ne crée pas de canal ; son nom v2 désigne le canal existant (entrées écran APPIN, tableaux de bits `btod 45` / `btod c10`, touches du clavier, entrées de la MC42, machines d'état de la gestion d'énergie). Les formules peuvent écrire `X[n]` (élément n d'un tableau, compté depuis 0), `X = Nom d'état` (rang de l'état, liste donnée par `States=…`), un script IQAN brut (`QCODE:` avec les canaux en `{Nom}`), et le type `COPY` copie un canal existant en remplaçant ses références (rampes SFC des chenilles). Un nom porté par plusieurs canaux de la 108.3.1 est refusé ; on le qualifie par son type ou son groupe (`BMW CAN OK@E.BMW`, `Voltage - S.M1.Right@IMAC`).
Raison : les écrans MD4 actuels ne changent pas pendant la refonte de la MC42 ; relier plutôt que recréer évite deux sources pour le même signal. L'ancien assembleur prenait sans le dire le premier de deux canaux homonymes (10 cas, dont `BMW CAN OK` batterie / chargeur) : ce risque d'erreur silencieuse est supprimé.
Conséquence : les mots d'état MC42 → écrans (APPOUT « HMI Status word 1-4 », « HMI Values ») attendent le contrat d'échange avec les applis MD4 et ne sont pas encore générés. Les entrées MD3 sortent de ce projet (projet MC42-MD3 à part, B1/B2).

## D45 — 23/10/2026 — Bits de commande des écrans : on garde la position actuelle de chaque appli

Décision : les commandes `CMD …` lisent les bits tels que les applis MD4 les envoient aujourd'hui. Bits 1 à 13 identiques sur MD4-5 et MD4-10. Écart conservé : sur MD4-10 le bit 14 est « super slow » (bit 18 sur MD4-5), et les bits 14 à 17 de MD4-5 (contrôle 10 h, remises à zéro entretien 1, 2 et 4 ans) n'existent pas sur MD4-10.
Raison : compatibilité avec les bateaux en service sans toucher aux écrans. L'alignement « même position sur tous les écrans » de la spec (80_HMI_bits.csv) se fera avec la reprise des applis MD4.
Conséquence : `CMD Super slow` = bit 18 MD4-5 ou bit 14 MD4-10. Présence des écrans : `CFG Has_MD45` = bit 12 « State ok » reçu de MD4-5, `CFG Has_MD410` = bit 12 reçu de MD4-10 (2 s de retard), plus de lecture de l'état des modules.

## D46 — 23/10/2026 — Codes d'erreur bruts sans équivalent : 0 en attendant

Décision : `BAT Error raw code` vaut 0 pour NovumTech, Tyva et Kreisel ; `ENG DM1 …` et `LOG HYD up down interrupted` restent à définir.
Raison : la 108.3.1 n'a pas de mot d'erreur unique pour ces batteries (seulement des bits séparés, déjà regroupés dans `BAT Error` et `BAT Warning`), et ne lit pas les codes DM1 ni l'interruption d'une montée / descente. Inventer un format serait pire que de l'annoncer manquant.
Conséquence : à reprendre avec les documentations constructeur (Novum, Tyva, Kreisel) et une décision sur l'affichage des défauts moteur.
