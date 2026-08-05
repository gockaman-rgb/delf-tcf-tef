# delf-tcf-tef.fr

Site statique du site officiel de l'app iOS « TCF DELF TEF - Tests 2026 »
([fiche App Store](https://apps.apple.com/fr/app/tcf-delf-tef-tests-2026/id6790412304)).
Hébergé sur GitHub Pages.

## ⚠️ Ne pas lancer `_build/generate.py` en l'état (02/08/2026)

Le générateur a **dérivé** des pages réellement en ligne : il ne connaît que
10 pages, alors que le site en compte 24 (les autres ont été écrites à la main
et n'ont jamais été reportées dans `PAGES[]`).

Le relancer réécrit les fichiers à partir de cette liste périmée et **efface
du contenu rédigé à la main** : `/blog/` −89 lignes, `/tcf-irn/` −53,
`/tef-canada/` −33, `/tcf-canada/` −29… et `sitemap.xml` retombe de **24 à 11
URLs** (il est reconstruit à partir de `PAGES[]`, pas du contenu du dossier).

Avant tout usage : resynchroniser `PAGES[]` sur les fichiers réels, puis
vérifier `git diff` après exécution — sur un site à jour, le diff doit être vide.
