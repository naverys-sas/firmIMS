# Jumeau numérique dans IQANsimulate

But : tester la v2 sans bateau. Le programme de la MC42 et des écrans MD4 tourne dans IQANsimulate sur le PC ; des modèles simples jouent le rôle des équipements (batterie, variateurs, pompe, chargeur, moteur, clavier) ; un script rejoue des scénarios et compare l'ancienne logique et la v2.

## Ce que permet IQANsimulate (vérifié le 05/11/2026)

| Point | Constat |
|---|---|
| Installé | IQANsimulate **7.04** (dans `%LOCALAPPDATA%\Programs\IQANsimulate 7`), simulateurs MC4x, MD4 et GC. |
| Projet 6.08 | **Refusé** par la 7.04 : « IQANsimulate only works with projects saved with the same major version ». Il faut IQANsimulate **6**. L'installateur signé Parker `SetupIQANsimulate6.08.exe` est dans les Téléchargements. |
| Mot de passe | IQANsimulate demande le mot de passe du projet à l'ouverture (sa propre base de mots de passe, Tools > Password Manager). Claude ne le tape pas. |
| Pilotage par script | Oui, interface COM `IQANsimulate.IQANsimulateControl2` et `IQANsimulate.IQANProject2` (enregistrées pour la 7 ; à revérifier pour la 6) : ouvrir, démarrer, pause, **avancer d'un cycle**, lire et écrire la valeur de chaque canal, **changer l'état d'un canal ou d'une trame** (perte CAN), heure du simulateur. |
| Licence | À voir au premier lancement de la version 6. |

Conséquence : rien n'est ajouté au firmware pour simuler. Les modèles tournent à côté, dans le script, et écrivent les entrées que les équipements réels enverraient (trames CAN reçues, entrées analogiques). Le programme simulé est exactement celui qui partirait sur un bateau. Les canaux `is_a_sim` et `sim thermal engine speed` de la 108.3.1 ne servent pas.

## Fichiers

| Fichier | Rôle |
|---|---|
| `simcom.ps1` | Pont COM : canaux par nom (`Nom@Module` si le nom existe plusieurs fois), lecture, écriture, état, pas à pas. Mode `-Fake` sans simulateur. |
| `modeles.ps1` | Modèles : batterie (SOC, tension, cellules, températures, contacteurs), variateurs de chenilles, pompe HVLP, chargeur, clavier Blink, moteur thermique J1939. Pannes : `can`, `defaut`, `surchauffe`, `isolement`, `desequilibre`, `calage`. |
| `profils/*.json` | Une configuration de bateau : réglages (Drive Type, marques), noms des canaux, codes d'état, constantes des modèles, points **à vérifier**. `E_tyva_sevcon` (12 bateaux), `T_eb2` (29 bateaux). |
| `scenarios/*.json` | Réglages, état initial, événements datés (touche, écriture, prise secteur, panne, rétablissement), canaux observés, valeurs attendues. |
| `paires.py` → `paires_ancien_v2.csv` | 114 paires (canal v2, canal 108.3.1 qu'il remplace), tirées de la colonne « origin » de la spec v2. |
| `rejouer.ps1` | Ouvre la copie du projet, applique les réglages, déroule le scénario par pas de 100 ms, journal CSV, puis `comparer.py`. |
| `comparer.py` | Rapport : attendus du scénario OK / ÉCHEC, et pour chaque paire le premier instant où ancienne logique et v2 divergent. |

## Lancer

```powershell
powershell -File rejouer.ps1 -Scenario scenarios\E_demarrage.json -Projet C:\Users\Sav78\Documents\testia_sandbox\jumeau\v2_lot8.idax
powershell -File rejouer.ps1 -Scenario scenarios\E_demarrage.json -Fake     # essai du script seul
```

Résultats dans `testia_sandbox\jumeau\resultats\` (CSV + rapport .md). Le script refuse un `.idax` hors de `testia_sandbox`.

## Ancienne logique et v2 dans le même essai

La v2 (groupe « v2 », 316 formules) tourne à côté de l'ancienne logique dans la même copie de la 108.3.1, avec les mêmes entrées. Un seul essai suffit donc à les comparer, sans brancher la v2 sur les sorties. Les modèles réagissent aux sorties de l'ancienne logique (boucle fermée sur l'ancienne). Brancher la v2 sur les sorties, dans une copie à part, ne sera utile que pour tester une v2 qui commande vraiment le bateau.

## Limites

- Modèles volontairement simples (premier ordre) : ils servent à exercer la logique, pas à prédire les performances.
- Codes d'état (StateBMS, Statut Sevcon, Status Word HVLP, état « trame perdue ») et échelles : hypothèses tirées de la 108.3.1, listées dans chaque profil sous `a_verifier`, à confirmer au premier essai réel.
- Les écrans MD4 sont simulés par IQANsimulate ; on observe leurs canaux, on ne clique pas dessus.

## État au 05/11/2026 (soir)

- IQANsimulate 6.08 installé (la 7 est désinstallée), mot de passe du projet enregistré dans son Password Manager : `rejouer.ps1` tourne sans intervention (PowerShell 32 bits conseillé : `C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe`).
- L'API ne liste pas les canaux, mais un canal se désigne par l'identifiant d'objet de l'export texte : `index_export.py` fait la table nom → identifiant (`<projet>.canaux.csv`). Lecture et écriture des entrées fonctionnent.
- **Réglages du bateau** (marque de batterie, variateurs…) : l'API ne les change pas, et un paramètre d'état démarre toujours sur son état par défaut. `profil_copie.py` (entrée forcée par un canal SIM) donne des erreurs IQANdesign (« Invalid context », « Not adjustable ») et retirer les éléments de menu de réglage corrompt le fichier : **ne pas utiliser en l'état**. Piste retenue : régler les paramètres dans IQANsimulate et les enregistrer dans un fichier de simulation `.isax` par profil, que `rejouer.ps1` ouvrira.
- **Copie v2** : refusée par IQANsimulate, 484 erreurs IQANdesign sur 143 canaux v2 (formules mal traduites par l'assembleur : noms non reconnus ou coupés, sélecteurs et rampes). `verifier_projet.ps1` lit la liste d'erreurs d'IQANdesign sans souris.
