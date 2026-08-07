#!/usr/bin/env python3
"""Gabarit de rendu des articles de blog de delf-tcf-tef.fr.

⚠️ Ce script ne CRÉE que de nouveaux fichiers. Il refuse d'écraser un fichier
existant sauf si `overwrite=True` est passé explicitement — contrairement à
`generate.py`, qui a effacé du contenu rédigé à la main (cf. README).

Le JSON-LD `FAQPage` est construit à partir des mêmes données que la FAQ
visible : les deux ne peuvent donc pas diverger, ce qui est l'exigence de
Google et l'erreur la plus facile à commettre en écrivant le balisage à la main.
"""

import html
import json
import os
import re

BASE = "https://delf-tcf-tef.fr"
APP = "https://apps.apple.com/fr/app/tcf-delf-tef-tests-2026/id6790412304"
AUTHOR = "Augusto Grone"
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

HEADER = """<header class="site"><div class="wrap">
  <a class="logo" href="/"><img src="/img/icon-180.png" alt="" width="30" height="30">DELF&nbsp;·&nbsp;TCF&nbsp;·&nbsp;TEF</a>
  <nav class="main">
    <a href="/tcf-canada/">TCF Canada</a>
    <a href="/tcf-irn/">TCF IRN</a>
    <a href="/delf-b2/">DELF</a>
    <a href="/examens-blancs/">Examens blancs</a>
    <a href="/blog/">Blog</a>
  </nav>
</div></header>"""

FOOTER = """<footer class="site"><div class="wrap">
  <div class="cols">
    <div><h4>Examens</h4><ul>
      <li><a href="/tcf-canada/">TCF Canada</a></li>
      <li><a href="/tcf-quebec/">TCF Québec</a></li>
      <li><a href="/tcf-irn/">TCF IRN (naturalisation)</a></li>
      <li><a href="/tef-canada/">TEF Canada · TEFAQ</a></li>
      <li><a href="/delf-b2/">DELF B2</a></li>
      <li><a href="/delf-b1/">DELF B1</a></li>
      <li><a href="/dalf/">DALF C1 · C2</a></li>
    </ul></div>
    <div><h4>L'application</h4><ul>
      <li><a href="%s">Télécharger sur l'App&nbsp;Store</a></li>
      <li><a href="/examens/">Les 15 examens couverts</a></li>
      <li><a href="/contenu/">Le contenu en détail</a></li>
      <li><a href="/correction-ia/">La correction IA</a></li>
      <li><a href="/score-tcf-699/">Comprendre le score 699</a></li>
      <li><a href="/plan-etude/">Le plan d'étude adaptatif</a></li>
      <li><a href="/examens-blancs/">Examens blancs</a></li>
      <li><a href="/blog/">Blog</a></li>
    </ul></div>
    <div><h4>Le site</h4><ul>
      <li><a href="/a-propos/">À propos · Mentions légales</a></li>
      <li><a href="/support/">Support / Contact</a></li>
      <li><a href="/confidentialite/">Politique de confidentialité</a></li>
      <li><a href="https://naturalisationfrancefacile.fr">Naturalisation France Facile</a></li>
    </ul></div>
  </div>
  <p class="legal">Application non officielle, non affiliée à France Éducation International
  (DELF, DALF, TCF) ni au Français des affaires — CCI Paris Île-de-France (TEF). Les noms
  d'examens sont cités uniquement pour décrire le contenu de préparation.
  © 2026 delf-tcf-tef.fr</p>
</div></footer>""" % APP


def plain(t):
    """HTML → texte nu, pour le JSON-LD (mêmes mots que la page visible)."""
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t).replace(" ", " ").replace(" ", " ")
    return re.sub(r"\s+", " ", t).strip()


def render(a, overwrite=False):
    slug, title, desc = a["slug"], a["title"], a["desc"]
    url = f"{BASE}/blog/{slug}/"
    img = f"{BASE}/img/og/{slug}.png"
    pub = a.get("published", "2026-08-07")
    mod = a.get("modified", "2026-08-07")

    faq_ld = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": plain(q),
                        "acceptedAnswer": {"@type": "Answer", "text": plain(ans)}}
                       for q, ans in a["faq"]],
    }
    article_ld = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": title, "description": desc,
        "datePublished": pub, "dateModified": mod, "inLanguage": "fr-FR",
        "author": {"@type": "Person", "name": AUTHOR, "url": f"{BASE}/a-propos/"},
        "publisher": {"@type": "Organization", "name": "delf-tcf-tef.fr", "url": f"{BASE}/"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "image": {"@type": "ImageObject", "url": img, "width": 1200, "height": 630},
    }
    crumb_ld = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{BASE}/blog/"},
            {"@type": "ListItem", "position": 3, "name": a["crumb"], "item": url},
        ],
    }
    j = lambda d: json.dumps(d, ensure_ascii=False)

    toc = "\n".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in a["toc"])
    facts = "\n".join(f"<li>{f}</li>" for f in a["facts"])
    faq = "\n\n".join(
        f"<details><summary>{q}</summary>\n<p>{ans}</p></details>" for q, ans in a["faq"])
    also = "\n".join(
        f'<li><a href="{u}">{t}</a>\n<p>{d}</p></li>' for u, t, d in a["also"])

    doc = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="/style.css">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/img/favicon-96.png" sizes="96x96" type="image/png">
<link rel="icon" href="/img/favicon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="/img/icon-180.png">
<meta name="apple-itunes-app" content="app-id=6790412304">
<meta property="og:title" content="{a.get('og_title', title)}">
<meta property="og:description" content="{a.get('og_desc', desc)}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="{url}">
<meta property="og:type" content="article">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="delf-tcf-tef.fr">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{a.get('og_title', title)}">
<meta name="twitter:description" content="{a.get('og_desc', desc)}">
<meta name="twitter:image" content="{img}">
<script type="application/ld+json">
{j(article_ld)}
</script>
<script type="application/ld+json">
{j(faq_ld)}
</script>
<script type="application/ld+json">
{j(crumb_ld)}
</script>
</head>
<body class="{a.get('accent', '')}">
{HEADER}
<article class="page"><div class="wrap narrow">
<p class="crumb"><a href="/">Accueil</a> › <a href="/blog/">Blog</a> › {a['crumb']}</p>
<h1>{a['h1']}</h1>
<p class="meta">Par <a href="/a-propos/">{AUTHOR}</a> · Mis à jour le {a['date_fr']} · {a['read']} min de lecture</p>

<p class="intro">{a['intro']}</p>

<div class="facts"><strong>L'essentiel</strong><ul>
{facts}
</ul></div>

<div class="toc"><strong>Au sommaire</strong><ol>
{toc}
<li><a href="#faq">Questions fréquentes</a></li>
</ol></div>

{a['body']}

<div class="cta-band">
<h2>{a['cta_h2']}</h2>
<p>{a['cta_p']}</p>
<a class="btn" href="{APP}">Télécharger sur l'App&nbsp;Store</a>
</div>

<h2 id="faq">Questions fréquentes</h2>
<div class="faq">
{faq}
</div>

<h2 id="a-lire">À lire aussi</h2>
<ul class="posts">
{also}
</ul>

<div class="note">
<p>{a['sources']}</p>
</div>

</div></article>
{FOOTER}
</body>
</html>
"""
    out = os.path.join(ROOT, "blog", slug, "index.html")
    if os.path.exists(out) and not overwrite:
        raise SystemExit(f"REFUS : {out} existe déjà (ce script ne réécrit jamais l'existant)")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    words = len(re.findall(r"\w+", plain(re.sub(r"<script.*?</script>", "", doc, flags=re.S))))
    return out, words


def build(articles, overwrite=False):
    for a in articles:
        out, w = render(a, overwrite)
        print(f"  ✓ /blog/{a['slug']}/ — {w} mots")
