# delf-tcf-tef.fr

Site statique du site officiel de l'app iOS « TCF DELF TEF - Tests 2026 »
([fiche App Store](https://apps.apple.com/fr/app/tcf-delf-tef-tests-2026/id6790412304)).
Hébergé sur GitHub Pages.

## ⚠️ Ne pas lancer `_build/generate.py` en l'état (mis à jour le 07/08/2026)

Le générateur a **dérivé** des pages réellement en ligne : il ne connaît que
10 pages, alors que le site en compte 24 (les autres ont été écrites à la main
et n'ont jamais été reportées dans `PAGES[]`).

Le relancer réécrit les fichiers à partir de cette liste périmée et **efface
du contenu rédigé à la main**, et `sitemap.xml` retombe de **24 à 11 URLs**
(il est reconstruit à partir de `PAGES[]`, pas du contenu du dossier).

**Le risque a fortement augmenté le 07/08/2026** : les six pages piliers
(`/tcf-canada/`, `/tef-canada/`, `/delf-b2/`, `/delf-b1/`, `/dalf/`,
`/examens-blancs/`) sont passées d'environ 600 mots à 2 000-2 600 mots
rédigés à la main, avec tableaux sourcés, FAQ et JSON-LD `Article`. Une
exécution du générateur les ramènerait à leur version courte, soit
**environ 10 000 mots perdus**.

Avant tout usage : resynchroniser `PAGES[]` sur les fichiers réels, puis
vérifier `git diff` après exécution — sur un site à jour, le diff doit être vide.

## Images Open Graph

`_build/make_og.py` génère les visuels de partage 1200×630 dans `img/og/`,
au gabarit des visuels existants (fond `#0E1420`, accent `#34C47C`).
Par défaut il ne crée que les images manquantes ; `--force` régénère tout.
Ajouter une page = ajouter une entrée dans `PAGES[]` du script.

## En-tête commun (mis à jour le 16/09/2026)

L'en-tête (`<header class="site">…</header>`) est **recopié à l'identique** dans
chaque page et dans les trois gabarits (`_build/generate.py`,
`_build/article_template.py`, `_build/make_questions_hub.py`). Pour le modifier,
remplacer le bloc entier par un script sur les 43 pages + les 3 gabarits, puis
vérifier qu'il ne reste qu'une seule variante :

```bash
for f in $(find . -name "*.html" -not -path "./.git/*"); do awk '/<header class="site">/,/<\/header>/' "$f" | tr -d '\n' | sed 's/  */ /g'; echo; done | sort | uniq -c
```

Sur téléphone (< 800 px) les liens vivent dans un panneau « popover » natif
(`popovertarget` / `popover`, sans JavaScript) ; le CSS correspondant est dans
`style.css`, bloc `@supports selector(:popover-open)`. La page
`/confidentialite/` est autonome (CSS en ligne, pas d'en-tête).

## Accueil et articles : ce qui est partagé (16/09/2026)

- **Note App Store** dans le héros (`.rating`, index.html) : valeur écrite en dur, relevée sur
  `itunes.apple.com/lookup?id=6790412304&country=fr` (4,82 sur 44 notes le 16/09/2026).
  À rafraîchir à la main quand elle bouge.
- **Sommaire** des articles : `<details class="toc">` fermé par défaut ; ouvert et statique sur
  ordinateur grâce à `::details-content` (style.css). Les gabarits `_build/` produisent ce balisage.
- **Carte « Entraînez-vous »** (`.cta-inline`) insérée avant le 3ᵉ `<h2>` des 32 articles longs
  (≥ 7 sections, ≥ 2 000 mots, avec bande finale). Insertion faite par script, pas par les gabarits :
  un nouvel article n'en a pas automatiquement.
- **Bande sombre** `#app` en bas de l'accueil : couleurs fixes (navy des visuels de partage).
