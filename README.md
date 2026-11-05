# Firmware Iguana Yachts — analyse et refonte v2

Dossier de travail du firmware IQAN des bateaux Iguana Yachts : analyse des versions en service et construction de la v2.

## Ce qu'il y a ici

| Dossier / fichier | Contenu |
|---|---|
| `TESTIA.idax` | **Version de référence 108.3.1** (keypad Blink complet). Jamais modifiée. |
| `v117_testia.idax`, `avecMD3_V69.03.01.WIP.idax`, `version_avec_MD3_et_moteur_VW_V5.37.idax` | Versions en service analysées (v117, lignée MD3 V69, lignée MC2 + VW). Jamais modifiées. |
| [kb_108_3_1/](kb_108_3_1/README.md) | Base de connaissances de la 108.3.1 : architecture, anomalies, configuration, interfaces, une fiche par canal. **Point d'entrée pour comprendre le firmware.** |
| [kb_v117/](kb_v117/README.md), [kb_md3_v69/](kb_md3_v69/README.md), [kb_vw_v537/](kb_vw_v537/README.md), [kb_v25/](kb_v25/README.md), [kb_v35/](kb_v35/README.md) | Bases de connaissances des autres versions. |
| [kb_flotte/](kb_flotte/README.md) | La flotte (registre), les lignées de projets, la confrontation faisceaux / logiciel. |
| [docs/](docs/) | Documents fournis : fiches techniques, schémas, configurations, anciennes versions du firmware (`docs/versions_firmware`). |
| [v2/refonte/](v2/refonte/README.md) | **Conception de la v2 (« refonte de la refonte »)** : architecture, conventions, interfaces d'équipements, IHM, journaux, compatibilité et migration, plans de faisceaux, conception détaillée en tableaux et au format IQAN, besoins IQANdesign, plan de construction. **Point d'entrée pour construire la v2.** |
| [v2/](v2/) | Refonte : [proposition_v2.md](v2/proposition_v2.md), [methode.md](v2/methode.md), [compatibilite.md](v2/compatibilite.md), [journalisation.md](v2/journalisation.md), **[DECISIONS.md](v2/DECISIONS.md)** (toutes les décisions et leur raison), rapports d'étapes. |
| `Firmware_Iguana_compagnon.html` | Document compagnon interactif (architecture, scénarios, variantes, explorateur des canaux, bugs, faisceaux, v2). Version en ligne privée : https://claude.ai/artifact/5T1eqv3aCcAYWKirx3qpsw |
| `kb_*/outils/` | Scripts Python (bibliothèque standard uniquement) qui régénèrent tout depuis un export texte IQANdesign. |
| [exports/](exports/) | Exports texte (UTF-8) de chaque version, y compris la v2 en cours : c'est ce qu'il faut comparer d'un commit à l'autre pour voir ce qui a changé dans la logique. |
| [faisceaux/](faisceaux/) | Brochage relevé dans IQANdesign, un fichier par contrôleur ou écran et par version. |
| `v2/projet/v2_mc42.idax` | Copie du projet v2 MC42 en cours (mise à jour à chaque étape validée). |
| [outils_pilotage/](outils_pilotage/) | `analyse/` : scripts d'analyse et de contrôle (compat_check, diff_versions, harness…). `conception/` : génération du format IQAN depuis les tableaux de conception, contrôle de conformité d'un export, écarts E/T. `gui/` : scripts PowerShell qui pilotent IQANdesign par messages Windows. |

La copie de travail vivante de la v2 est `..\testia_sandbox\v2_mc42\v2_mc42.idax` ; elle est recopiée dans `v2/projet/` et son export dans `exports/` à chaque étape. Dépôt GitHub privé : `naverys-sas/firmIMS`.

## Règles de travail

- On ne modifie jamais un `.idax` d'origine : on travaille sur une copie.
- On n'envoie rien à un contrôleur ni à un bateau sans accord explicite.
- Chaque version v2 passe deux contrôles avant d'être proposée : `compat_check.py` (aucun réglage, trame, broche ou message existant cassé) et `anomalies.py`.
- Chaque choix de conception est noté dans [v2/DECISIONS.md](v2/DECISIONS.md).

## Régénérer une base de connaissances

```bash
"/c/Program Files (x86)/IQANdesign 6.08/IQANdesign.exe" copie.idax -saveas export.txt
sh kb_108_3_1/outils/run_all.sh export.txt kb_nouvelle_version
```
