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
  <a class="logo" href="/"><img src="/img/favicon-192.png" alt="" width="30" height="30"><span>DELF&nbsp;·&nbsp;TCF&nbsp;·&nbsp;TEF</span></a>
  <a class="store" href="https://apps.apple.com/fr/app/tcf-delf-tef-tests-2026/id6790412304">App&nbsp;Store</a>
  <button class="menu-btn" type="button" popovertarget="menu" aria-label="Menu"><span></span></button>
  <nav class="main" id="menu" popover aria-label="Navigation principale">
    <div class="menu-panel">
      <a href="/tcf-canada/">TCF Canada</a>
      <a href="/tcf-irn/">TCF IRN</a>
      <a href="/delf-b2/">DELF</a>
      <a href="/centres/">Centres</a>
      <a href="/examens-blancs/">Examens blancs</a>
      <a href="/blog/">Blog</a>
    </div>
    <button class="menu-scrim" type="button" popovertarget="menu" popovertargetaction="hide" tabindex="-1" aria-label="Fermer le menu"></button>
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
      <li><a href="/ou-passer/">Où passer l'examen</a></li>
      <li><a href="/centres/">Annuaire des centres</a></li>
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
      <li><a href="/questions/">Toutes les questions</a></li>
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


# Langues (08/10/2026). Le français reste la valeur par défaut et doit sortir à l'octet près comme avant ;
# « es » et « en » servent aux pages /es/ et /en/ (make_pays.py). Libellés du gabarit seulement : le
# contenu, lui, vient de chaque page. Lien App Store sans vitrine : Apple redirige vers celle du visiteur.
APP_INTL = 'https://apps.apple.com/app/id6790412304'
HEADER_ES = '<header class="site"><div class="wrap">\n  <a class="logo" href="/es/"><img src="/img/favicon-192.png" alt="" width="30" height="30"><span>DELF&nbsp;·&nbsp;TCF&nbsp;·&nbsp;TEF</span></a>\n  <a class="store" href="https://apps.apple.com/app/id6790412304">App&nbsp;Store</a>\n  <button class="menu-btn" type="button" popovertarget="menu" aria-label="Menú"><span></span></button>\n  <nav class="main" id="menu" popover aria-label="Navegación principal">\n    <div class="menu-panel">\n      <a href="/es/">Centros</a>\n      <a href="/es/#tcf-canada">TCF Canada</a>\n      <a href="/es/#delf">DELF</a>\n      <a href="/en/" lang="en">English</a>\n      <a href="/" lang="fr">Français</a>\n    </div>\n    <button class="menu-scrim" type="button" popovertarget="menu" popovertargetaction="hide" tabindex="-1" aria-label="Cerrar el menú"></button>\n  </nav>\n</div></header>'
HEADER_EN = '<header class="site"><div class="wrap">\n  <a class="logo" href="/en/"><img src="/img/favicon-192.png" alt="" width="30" height="30"><span>DELF&nbsp;·&nbsp;TCF&nbsp;·&nbsp;TEF</span></a>\n  <a class="store" href="https://apps.apple.com/app/id6790412304">App&nbsp;Store</a>\n  <button class="menu-btn" type="button" popovertarget="menu" aria-label="Menu"><span></span></button>\n  <nav class="main" id="menu" popover aria-label="Main navigation">\n    <div class="menu-panel">\n      <a href="/en/">All locations</a>\n      <a href="/en/tcf-canada-test-centres/">Canada</a>\n      <a href="/en/tcf-canada-usa/">USA</a>\n      <a href="/en/tcf-canada-uk/">UK</a>\n      <a href="/es/" lang="es">Español</a>\n      <a href="/" lang="fr">Français</a>\n    </div>\n    <button class="menu-scrim" type="button" popovertarget="menu" popovertargetaction="hide" tabindex="-1" aria-label="Close menu"></button>\n  </nav>\n</div></header>'
FOOTER_ES = '<footer class="site"><div class="wrap">\n  <div class="cols">\n    <div><h4>TCF Canada</h4><ul>\n      <li><a href="/es/tcf-canada-espana/">España</a></li>\n      <li><a href="/es/tcf-canada-mexico/">México</a></li>\n      <li><a href="/es/tcf-canada-colombia/">Colombia</a></li>\n      <li><a href="/es/tcf-canada-argentina/">Argentina</a></li>\n      <li><a href="/es/tcf-canada-chile/">Chile</a></li>\n      <li><a href="/es/tcf-canada-peru/">Perú</a></li>\n      <li><a href="/es/tcf-canada-ecuador/">Ecuador</a></li>\n    </ul></div>\n    <div><h4>DELF y DALF</h4><ul>\n      <li><a href="/es/delf-espana/">España</a></li>\n      <li><a href="/es/delf-mexico/">México</a></li>\n      <li><a href="/es/delf-colombia/">Colombia</a></li>\n      <li><a href="/es/delf-argentina/">Argentina</a></li>\n      <li><a href="/es/delf-chile/">Chile</a></li>\n      <li><a href="/es/delf-peru/">Perú</a></li>\n      <li><a href="/es/delf-ecuador/">Ecuador</a></li>\n    </ul></div>\n    <div><h4>El sitio</h4><ul>\n      <li><a href="/es/">Centros de examen</a></li>\n      <li><a href="https://apps.apple.com/app/id6790412304">La app en el App&nbsp;Store</a></li>\n      <li><a href="/" lang="fr">Versión en francés</a></li>\n      <li><a href="/en/" lang="en">English</a></li>\n      <li><a href="/confidentialite/">Privacidad</a></li>\n      <li><a href="/support/">Contacto</a></li>\n    </ul></div>\n  </div>\n  <p class="legal">Aplicación no oficial, sin vínculo con France Éducation International\n  (DELF, DALF, TCF) ni con Le français des affaires — CCI Paris Île-de-France (TEF). Los nombres\n  de los exámenes se citan solo para describir el contenido de preparación.\n  © 2026 delf-tcf-tef.fr</p>\n</div></footer>'
FOOTER_EN = '<footer class="site"><div class="wrap">\n  <div class="cols">\n    <div><h4>TCF Canada</h4><ul>\n      <li><a href="/en/tcf-canada-test-centres/">Canada: all provinces</a></li>\n      <li><a href="/en/tcf-canada-toronto/">Toronto</a></li>\n      <li><a href="/en/tcf-canada-montreal/">Montreal</a></li>\n      <li><a href="/en/tcf-canada-vancouver/">Vancouver</a></li>\n      <li><a href="/en/tcf-canada-ottawa/">Ottawa</a></li>\n      <li><a href="/en/tcf-canada-quebec-city/">Quebec City</a></li>\n      <li><a href="/en/tcf-canada-usa/">United States</a></li>\n      <li><a href="/en/tcf-canada-uk/">United Kingdom</a></li>\n    </ul></div>\n    <div><h4>DELF and DALF</h4><ul>\n      <li><a href="/en/delf-usa/">United States</a></li>\n      <li><a href="/en/delf-uk/">United Kingdom</a></li>\n    </ul></div>\n    <div><h4>The site</h4><ul>\n      <li><a href="/en/">All locations</a></li>\n      <li><a href="https://apps.apple.com/app/id6790412304">The app on the App&nbsp;Store</a></li>\n      <li><a href="/" lang="fr">French version</a></li>\n      <li><a href="/es/" lang="es">Español</a></li>\n      <li><a href="/confidentialite/">Privacy</a></li>\n      <li><a href="/support/">Contact</a></li>\n    </ul></div>\n  </div>\n  <p class="legal">Unofficial app, not affiliated with France Éducation International\n  (DELF, DALF, TCF) or Le français des affaires — CCI Paris Île-de-France (TEF). Exam names\n  are cited only to describe the preparation content.\n  © 2026 delf-tcf-tef.fr</p>\n</div></footer>'
UI = {
    "fr": dict(html="fr", locale="fr_FR", in_language="fr-FR", home="Accueil", by="Par", updated="Mis à jour le",
               read="min de lecture", essentials="L'essentiel", toc="Au sommaire", faq="Questions fréquentes",
               also="À lire aussi", download="Télécharger sur l'App&nbsp;Store", app=APP, header=HEADER, footer=FOOTER),
    "es": dict(html="es", locale="es_ES", in_language="es", home="Inicio", by="Por", updated="Actualizado el",
               read="min de lectura", essentials="Lo esencial", toc="Contenido", faq="Preguntas frecuentes",
               also="Para seguir leyendo", download="Descargar en el App&nbsp;Store", app=APP_INTL,
               header=HEADER_ES, footer=FOOTER_ES),
    "en": dict(html="en", locale="en_US", in_language="en", home="Home", by="By", updated="Updated",
               read="min read", essentials="Key facts", toc="Contents", faq="Frequently asked questions",
               also="Related pages", download="Download on the App&nbsp;Store", app=APP_INTL,
               header=HEADER_EN, footer=FOOTER_EN),
}


def plain(t):
    """HTML → texte nu, pour le JSON-LD (mêmes mots que la page visible)."""
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t).replace(" ", " ").replace(" ", " ")
    return re.sub(r"\s+", " ", t).strip()


def render(a, overwrite=False):
    slug, title, desc = a["slug"], a["title"], a["desc"]
    L = UI[a.get("lang", "fr")]
    # section="blog" (défaut) → /blog/<slug>/ ; section="" → page pilier à la racine, /<slug>/
    section = a.get("section", "blog")
    url = f"{BASE}/{section}/{slug}/" if section else f"{BASE}/{slug}/"
    img = f"{BASE}/img/og/{a.get('og_slug', slug)}.png"
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
        "datePublished": pub, "dateModified": mod, "inLanguage": a.get("in_language", L["in_language"]),
        "author": {"@type": "Person", "name": AUTHOR, "url": f"{BASE}/a-propos/"},
        "publisher": {"@type": "Organization", "name": "delf-tcf-tef.fr", "url": f"{BASE}/"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "image": {"@type": "ImageObject", "url": img, "width": 1200, "height": 630},
    }
    if "crumbs" in a:
        # pages /es/ et /en/ : fil d'Ariane fourni par le générateur, [(libellé, chemin)]
        crumbs = [(n, f"{BASE}{p}") for n, p in a["crumbs"]]
    else:
        crumbs = [("Accueil", f"{BASE}/")]
    if section and "crumbs" not in a:
        # libellé du niveau intermédiaire : « Blog » par défaut, sinon a["section_name"] (ex. « Centres »)
        crumbs.append((a.get("section_name", "Blog" if section == "blog" else section.capitalize()), f"{BASE}/{section}/"))
    crumbs.append((a["crumb"], url))
    crumb_ld = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                            for i, (n, u) in enumerate(crumbs)],
    }
    crumb_html = " › ".join(f'<a href="{u[len(BASE):]}">{n}</a>' for n, u in crumbs[:-1]) + f" › {a['crumb']}"
    j = lambda d: json.dumps(d, ensure_ascii=False)

    toc = "\n".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in a["toc"])
    facts = "\n".join(f"<li>{f}</li>" for f in a["facts"])
    alts = "".join(f'<link rel="alternate" hreflang="{h}" href="{BASE}{p}">\n' for h, p in a.get("alternates", []))
    lang_links = f'{a["lang_links"]}\n' if a.get("lang_links") else ""
    faq = "\n\n".join(
        f"<details><summary>{q}</summary>\n<p>{ans}</p></details>" for q, ans in a["faq"])
    also = "\n".join(
        f'<li><a href="{u}">{t}</a>\n<p>{d}</p></li>' for u, t, d in a["also"])

    doc = f"""<!DOCTYPE html>
<html lang="{L['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
{alts}<link rel="stylesheet" href="/style.css">
<link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">
<link rel="icon" type="image/png" sizes="48x48" href="/img/favicon-48-v2.png">
<link rel="icon" type="image/png" sizes="96x96" href="/img/favicon-96-v2.png">
<link rel="icon" type="image/png" sizes="192x192" href="/img/favicon-192-v2.png">
<link rel="apple-touch-icon" href="/img/icon-180-v2.png">
<meta name="apple-itunes-app" content="app-id=6790412304">
<meta property="og:title" content="{a.get('og_title', title)}">
<meta property="og:description" content="{a.get('og_desc', desc)}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="{url}">
<meta property="og:type" content="article">
<meta property="og:locale" content="{a.get('og_locale', L['locale'])}">
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
{L['header']}
<article class="page"><div class="wrap narrow">
<p class="crumb">{crumb_html}</p>
<h1>{a['h1']}</h1>
<p class="meta">{L['by']} <a href="/a-propos/">{AUTHOR}</a> · {L['updated']} {a['date_fr']} · {a['read']} {L['read']}</p>
{lang_links}
<p class="intro">{a['intro']}</p>

<div class="facts"><strong>{L['essentials']}</strong><ul>
{facts}
</ul></div>

<details class="toc"><summary>{L['toc']}</summary><ol>
{toc}
<li><a href="#faq">{L['faq']}</a></li>
</ol></details>

{a['body']}

<div class="cta-band">
<h2>{a['cta_h2']}</h2>
<p>{a['cta_p']}</p>
<a class="btn" href="{L['app']}">{L['download']}</a>
</div>

<h2 id="faq">{L['faq']}</h2>
<div class="faq">
{faq}
</div>

<h2 id="a-lire">{L['also']}</h2>
<ul class="posts">
{also}
</ul>

<div class="note">
<p>{a['sources']}</p>
</div>

</div></article>
{L['footer']}
</body>
</html>
"""
    out = os.path.join(ROOT, section, slug, "index.html") if section else os.path.join(ROOT, slug, "index.html")
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
        print(f"  ✓ {out[len(ROOT):-len('index.html')]} — {w} mots")
