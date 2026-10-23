# v2 MC42 — étape A : corrections sûres

Copie de travail : `testia_sandbox\v2_mc42\v2_mc42.idax` (faite à partir de `TESTIA.idax` 108.3.1, même identifiant de projet). Rien n'a été envoyé à un contrôleur. Chaque modification a été faite dans IQANdesign, puis vérifiée par export texte et comparaison automatique.

## Résultat des contrôles

- **Contrat avec le parc** ([etapeA_compat.md](etapeA_compat.md)) : 0 élément supprimé, 0 modifié, 1 ajouté (le réglage `T Pump wiring`). Aucune trame, broche, message ou réglage existant n'a bougé.
- **Logique** ([etapeA_diff_108_3_1_vers_v2.md](etapeA_diff_108_3_1_vers_v2.md)) : 3 canaux ajoutés, 7 modifiés, 1 groupe réactivé.

## Ce qui a changé

| # | Modification | Effet sur le bateau |
|---|---|---|
| 1 | Nouveau réglage `T Pump wiring` (Standard / Swapped) + `T Pump mc14 cmd`, `T Pump mc15 cmd` ; sorties `T Pump 2 Left mc 14` et `T Pump 1 Right mc 15` pilotées selon ce réglage (consigne et courants min/max) | **Aucun en Standard** (valeur par défaut = 108.3.1). En Swapped : câblage V69 / V5.37 |
| 2 | `Error Iso_Resist`, fonction Kreisel = `BMW tyva - Isolation Error` | Kreisel : le défaut d'isolement est remonté comme sur les autres marques |
| 3 | `e Battery Protection mc`, fonction Kreisel : affichage sur `Error Iso_Resist` | Kreisel : le message « e1170 Battery Isolation » s'affiche avant la coupure |
| 4 | `Battery CHARGED`, fonction Kreisel = `(Battery SOC >= eb Charge Max) OR (Charger asks End Of Charge)` | Kreisel : la batterie peut déclarer la fin de charge ; le journal « Battery Charged » s'écrit |
| 5 | `e M3 - Pump Engine CMSG mc` : affichage sur `M3 - New Error Code` | Sevcon J1939 : le message « e1168 Pump Engine » apparaît en cas d'erreur pompe |
| 6 | `T Engine Temp State`, fonction Low : retour à faux au-dessus de (seuil bas + hystérésis) | Thermique : l'état « Low » se libère quand le moteur chauffe |
| 7 | Groupe `Water level V10 motor` (MD45-ET) réactivé | Comportement v117 : entrée C2:1 du MD4-5 de nouveau lue (niveau d'eau ou joystick gauche) |

## Restant de l'étape A

- **Mettre `T Pump wiring` dans le menu Master Config** : IQANdesign crée un réglage par glisser-déposer du canal sur le groupe de réglages, geste que je ne peux pas reproduire de façon fiable. 10 secondes pour toi : groupe `MC42 app / mc.Thermic / T.Pump / pins thermic`, faire glisser le canal `T Pump wiring` sur `Diagnostics > Adjust groups > Master Config`.
- **Timeouts CAN** : les ajouter change ce que voient les calculs quand une trame se perd (valeur d'erreur au lieu de la dernière valeur reçue). Je propose de le faire trame par trame avec toi plutôt qu'en bloc ; liste dans [../kb_108_3_1/anomalies_auto.md](../kb_108_3_1/anomalies_auto.md).
- **Défaut de masse Kreisel** (`Flag Ground Fault Detection`) : laissé tel quel, la logique BMW/Tyva s'appuie sur des signaux que la batterie Kreisel ne fournit pas. À voir avec la doc Kreisel.

## Essais à faire sur banc avant toute diffusion

1. Thermique, `T Pump wiring` = Standard : pompes identiques à la 108.3.1.
2. Thermique, `T Pump wiring` = Swapped : sortie mc14 → pompe droite, mc15 → pompe gauche, sens et courants corrects.
3. Kreisel : simuler un isolement bas (message e1170 puis coupure à 100 s) et une fin de charge.
4. Sevcon J1939 : simuler une erreur pompe, vérifier le message e1168.
5. Thermique : chauffe moteur, vérifier que l'état thermique quitte « Low ».
