# Base de connaissances — firmware IGUANA YACHTS 108.3.1

Projet IQANdesign `TESTIA.idax`, version **108.3.1** (« Ajout du Keypad PKP 2400SI CANOpen… peut être installé sur tous les thermiques », dernier enregistrement 22/10/2026). C'est la **version de référence** ; la v117 (108.2.2_117) est documentée à part dans `../kb_v117/`. Cette base décrit **tout** le logiciel à partir de l'export texte d'IQANdesign 6.08, sans toucher au fichier d'origine.

## Par où commencer

| Fichier | Contenu |
|---|---|
| [architecture.md](architecture.md) | Vue d'ensemble : contrôleurs, applications, grands blocs fonctionnels, flux principaux, conventions de nommage. **À lire en premier.** |
| [anomalies.md](anomalies.md) | Bugs probables et points à vérifier, triés par gravité, avec la preuve (canal, ligne de l'export). |
| [configuration.md](configuration.md) | Les sélecteurs de variante (marque de batterie, moteur thermique, chargeur…), les menus de réglage et leurs codes PIN. |
| [interfaces.md](interfaces.md) | Modules, bus CAN, entrées/sorties physiques, toutes les trames CAN, liaisons MC42 ↔ écrans. |
| [fonctions/](fonctions/) | Une fiche par canal (3 185), regroupées par grand bloc : propriétés, logique réécrite en clair, ce qu'il lit, qui l'utilise. |
| [index_canaux.csv](index_canaux.csv) | Tableau de tous les canaux (ouvrable dans Excel, séparateur `;`). |
| [graphe_dependances.json](graphe_dependances.json) | Le même graphe en JSON, pour les outils. |
| [evolution_v117_108_3_1.md](evolution_v117_108_3_1.md) | Tout ce qui a changé dans la logique entre la v117 et la 108.3.1. |
| [compat_v117_vers_108_3_1.md](compat_v117_vers_108_3_1.md) | Le même écart vu du parc installé (paramètres, trames, broches, messages), produit par `outils/compat_check.py`. |
| [anomalies_auto.md](anomalies_auto.md) | Sortie brute du détecteur d'anomalies (beaucoup de faux positifs, voir `anomalies.md`). |
| [../v2/](../v2/) | Proposition de refonte v2 et matrice de compatibilité. |

## Comment lire une fiche

```
#### Battery CHARGED  `IDC`
- Fonction *BMW* :                     ← une fonction par valeur du sélecteur (ici la marque de batterie)
  - **Activating** = `(Battery SOC [%] >= eb Charge Max [%]) OR (Charger asks End Of Charge)`
- Fonction *Kreisel* : (vide)          ← dans ce mode le canal reste à False
- Lit : …                              ← dépendances (entrées)
- Utilisé par : …                      ← canaux, écrans, logs et réglages qui le lisent
- Ligne export : 7462 · id 129160      ← position dans l'export texte, pour vérifier
```

La logique « liste d'objets » d'IQAN est réécrite en expression : seuls les objets *résultants* (non référencés par un autre objet) sont combinés par la méthode du groupe (And/Or/Multiply…), conformément au manuel IQANdesign (p. 265). `[verrouillé]` = méthode Latching. Le Qcode est recopié tel quel.

## Limites connues de l'export texte

- **L'état cible des transitions des machines d'état finies (FSM) n'est pas exporté** par IQANdesign. Les fiches donnent les états (avec leur numéro) et les conditions de chaque transition ; la cible se déduit du nom ou doit être lue dans l'IDE.
- **La portée des canaux (private/protected/public) n'est pas exportée.** Les références sont résolues comme IQAN le fait par défaut : d'abord le même groupe de fonctions, puis les groupes parents. Quelques liens peuvent donc être approximatifs quand deux canaux portent le même nom.
- Les images, la mise en page des écrans et les mots de passe ne sont pas analysés.
- IQANdesign **ne sait pas réimporter** un fichier texte : toute modification réelle doit être refaite dans l'IDE (ou pilotée par Claude dans l'IDE, voir la mémoire du projet).

## Régénérer la base (nouvelle version du projet)

Sur une **copie** du projet, jamais l'original :

```bash
"/c/Program Files (x86)/IQANdesign 6.08/IQANdesign.exe" copie.idax -saveas export.txt
sh outils/run_all.sh export.txt kb_nouvelle_version
```

Les scripts Python (stdlib uniquement) sont dans [outils/](outils/) : `iqan_parse.py` (lecture de l'export), `kb_build.py` (fiches + graphe), `anomalies.py`, `reports.py`, `card.py` (affiche la fiche d'un canal : `python -I outils/card.py . "Battery CHARGED"`).

## Chiffres clés 108.3.1

- 3 266 canaux, 3 applications : **MC42 app** (contrôleur principal, 2 795 canaux), **MD4-CAB app** (écran cabine MD4-10, 402), **MD45-ET app** (écran tableau de bord MD4-5, 69).
- 26 modules déclarés (3 IQAN + 23 équipements CAN), 8 bus CAN.
- 219 réglages, 20 menus de réglage, 15 journaux, 19 groupes de mesure.
- Fichier source : `C:\Users\Sav78\Documents\testia\TESTIA.idax` (non modifié). Copie de travail et export : `C:\Users\Sav78\Documents\testia_sandbox\v1083\`.
