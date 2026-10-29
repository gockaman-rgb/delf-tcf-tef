#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Espace presse (29/10/2026) : /presse/ (FR) et /en/press/ (EN). Faits citables, données ouvertes du site, l'app,
visuels, contact, conditions de citation. En-tête et pied de page copiés de /index.html et /en/index.html. Idempotent.
Après exécution : python3 _build/app_links.py (paramètres de campagne), python3 _build/sitemap_sync.py.
Usage : python3 _build/make_presse.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
BASE = "https://delf-tcf-tef.fr"
PATHS = {"fr": "/presse/", "en": "/en/press/"}
TITLE = {"fr": "Espace presse — delf-tcf-tef.fr et l'app TCF DELF TEF",
         "en": "Press — delf-tcf-tef.fr and the TCF DELF TEF app"}
DESC = {"fr": "Faits citables, données ouvertes (1 825 centres d'examen dans 176 pays, prix du TCF Canada par pays, calendrier DELF-DALF 2027), visuels et contact de l'éditeur.",
        "en": "Citable facts, open data (1,825 exam centres in 176 countries, TCF Canada fees by country, the DELF-DALF 2027 calendar), visuals and the publisher's contact."}
HOME = {"fr": ("/", "Accueil"), "en": ("/en/", "Home")}
CRUMB = {"fr": "Presse", "en": "Press"}
LOCALE = {"fr": "fr_FR", "en": "en_US"}
LANGS = {"fr": '<p class="langs"><a href="/en/press/" hreflang="en" lang="en">Read in English</a></p>',
         "en": '<p class="langs"><a href="/presse/" hreflang="fr" lang="fr">Lire en français</a></p>'}

BODY = {}
BODY["fr"] = """<h1>Espace presse</h1>
<p class="meta">Mis à jour le 29 octobre 2026</p>
{langs}
<p class="intro">delf-tcf-tef.fr est un site indépendant qui documente les examens de français — DELF, DALF, TCF, TEF —
à partir des sources officielles, avec la date de chaque relevé. Il est adossé à l'application de préparation
« TCF DELF TEF : Tests 2026 ». Cette page rassemble ce qu'un journaliste, un enseignant ou un blogueur peut citer,
et comment nous joindre.</p>

<h2 id="faits">Faits citables (relevés datés, sources sur chaque page)</h2>
<ul>
<li><strong>1 825 centres d'examen dans 176 pays</strong>, d'après les listes de France Éducation international (TCF, DELF-DALF)
et de la CCI Paris Île-de-France (TEF) relevées le 26 octobre 2026, consultables par ville dans
<a href="/trouver-un-centre/">le moteur de recherche de centres</a> (français, anglais, espagnol, arabe).</li>
<li><strong>Le calendrier national DELF-DALF 2027</strong> : dix sessions par an, jamais en avril ni en septembre, avec les fenêtres
d'inscription — <a href="/blog/calendrier-delf-dalf-2026-2027/">calendrier 2026-2027</a>, <a href="/en/delf-exam-dates-2027/">en anglais</a>,
<a href="/es/fechas-delf-2027/">en espagnol</a>.</li>
<li><strong>Le prix du TCF Canada pays par pays</strong>, centre par centre, avec la date de chaque relevé :
<a href="/blog/prix-tcf-tef/">en français</a>, <a href="/en/tcf-canada/fees-registration/">en anglais</a>, <a href="/ar/tcf-canada-price/">en arabe</a>.</li>
<li><strong>Les niveaux exigés en 2026</strong> pour la naturalisation (B2) et la carte de résident (B1), avec les textes :
<a href="/blog/naturalisation-2026-niveau-b2/">naturalisation</a>, <a href="/blog/carte-de-resident-b1-2026/">carte de résident</a>.</li>
<li><strong>Prendre rendez-vous pour le TCF en Algérie</strong> : la plateforme de l'Institut français, les pièces, les délais, et le
faux site à éviter — <a href="/blog/ifal-tcf-rendez-vous/">le guide</a>, <a href="/centres/tcf-algerie/">les cinq antennes</a>.</li>
<li><strong>La recorrection des épreuves d'expression du TCF est suspendue</strong> par France Éducation international pour les
sessions à partir du 1er septembre 2026, reprise annoncée pour l'automne 2027 — rappelé sur
<a href="/tcf-canada/score-nclc/">la page des scores</a>.</li>
</ul>

<h2 id="app">L'application</h2>
<p>« TCF DELF TEF : Tests 2026 » (iOS ; version Android en test fermé en octobre 2026) propose des examens blancs au
format officiel des <a href="/examens/">quinze examens couverts</a> — TCF Canada, Québec, IRN, tout public et DAP, DELF A1 à B2,
DALF C1 et C2, TEF Canada, TEFAQ et TEF IRN — avec la notation du vrai test et une <a href="/correction-ia/">correction par IA</a>
de l'expression écrite et orale. Interface en français, anglais, espagnol et arabe.
<a href="https://apps.apple.com/fr/app/tcf-delf-tef-tests-2026/id6790412304">Fiche App Store</a>.</p>

<h2 id="qui">Qui</h2>
<p>Le site et l'application sont édités par <strong>Augusto Grone</strong>, éditeur indépendant. Le site n'est ni officiel ni
affilié à France Éducation international ni à la CCI Paris Île-de-France ; sa <a href="/a-propos/">méthode éditoriale</a>
(sources primaires, recoupement, rejet des chiffres non sourcés) est publique.</p>

<h2 id="visuels">Visuels</h2>
<ul>
<li>Icône de l'application : <a href="/img/icon-180-v2.png">PNG 180 px</a>, <a href="/img/favicon-192-v2.png">PNG 192 px</a>.</li>
<li>Images sociales des pages (1200 × 630) : par exemple <a href="/img/og/a-propos.png">À propos</a> ; chaque page porte la
sienne dans sa balise <code>og:image</code>.</li>
<li>Captures d'écran de l'application : sur demande, ou sur la fiche App Store.</li>
</ul>

<h2 id="citation">Conditions de citation</h2>
<p>Les faits et les tableaux du site peuvent être cités et reproduits librement avec la mention « delf-tcf-tef.fr », la date
du relevé indiquée sur la page et un lien vers celle-ci. Nous signalons nos propres limites : les prix, dates et règles
changent sans préavis, et la source officielle fait foi.</p>

<h2 id="contact">Contact</h2>
<p>Augusto Grone — <strong>gockaman@gmail.com</strong>. Réponse sous 48 h aux demandes de données, d'extraits par pays ou de
vérification d'un chiffre ; nous corrigeons le jour même une erreur signalée.</p>
"""

BODY["en"] = """<h1>Press</h1>
<p class="meta">Updated 29 October 2026</p>
{langs}
<p class="intro">delf-tcf-tef.fr is an independent site documenting the French exams — DELF, DALF, TCF, TEF — from official
sources, with the date of every reading. It is backed by the exam-prep app “TCF DELF TEF: Tests 2026”. This page gathers
what a journalist, teacher or blogger can cite, and how to reach us.</p>

<h2 id="facts">Citable facts (dated readings, sources on every page)</h2>
<ul>
<li><strong>1,825 exam centres in 176 countries</strong>, from the lists of France Éducation international (TCF, DELF-DALF) and
the CCI Paris Île-de-France (TEF) read on 26 October 2026, searchable by city in <a href="/en/test-centre-near-me/">the centre
finder</a> (French, English, Spanish, Arabic).</li>
<li><strong>The national DELF-DALF 2027 calendar</strong>: ten sessions a year, never in April or September, with registration
windows — <a href="/en/delf-exam-dates-2027/">in English</a>, <a href="/blog/calendrier-delf-dalf-2026-2027/">in French</a>,
<a href="/es/fechas-delf-2027/">in Spanish</a>.</li>
<li><strong>TCF Canada fees country by country</strong>, centre by centre, each with its reading date:
<a href="/en/tcf-canada/fees-registration/">in English</a>, <a href="/blog/prix-tcf-tef/">in French</a>, <a href="/ar/tcf-canada-price/">in Arabic</a>.</li>
<li><strong>Where to take the TCF Canada</strong> in <a href="/en/tcf-canada-test-centres/">Canada by province</a>, the
<a href="/en/tcf-canada-usa/">United States</a>, the <a href="/en/tcf-canada-uk/">United Kingdom</a> and <a href="/en/tcf-canada-india/">India</a>.</li>
<li><strong>The level required for French citizenship</strong> (B2 since 2026) — <a href="/en/french-citizenship-b2/">the guide</a>.</li>
<li><strong>Re-marking of the TCF writing and speaking papers is suspended</strong> by France Éducation international for sessions
from 1 September 2026, with a return announced for autumn 2027.</li>
</ul>

<h2 id="app">The app</h2>
<p>“TCF DELF TEF: Tests 2026” (iOS; Android in closed testing in October 2026) offers mock exams in the official format of
fifteen exams — TCF Canada, Québec, IRN, tout public and DAP, DELF A1 to B2, DALF C1 and C2, TEF Canada, TEFAQ and TEF IRN —
scored like the real test, with AI feedback on writing and speaking. Interface in French, English, Spanish and Arabic.
<a href="https://apps.apple.com/app/id6790412304">App Store listing</a>.</p>

<h2 id="who">Who</h2>
<p>The site and the app are published by <strong>Augusto Grone</strong>, an independent publisher. The site is neither official
nor affiliated with France Éducation international or the CCI Paris Île-de-France; its <a href="/en/about/">editorial method</a>
(primary sources, cross-checking, no unsourced figure) is public.</p>

<h2 id="visuals">Visuals</h2>
<ul>
<li>App icon: <a href="/img/icon-180-v2.png">PNG 180 px</a>, <a href="/img/favicon-192-v2.png">PNG 192 px</a>.</li>
<li>Social images of the pages (1200 × 630): every page carries its own in its <code>og:image</code> tag.</li>
<li>App screenshots: on request, or on the App Store listing.</li>
</ul>

<h2 id="citation">Citation terms</h2>
<p>The site's facts and tables may be cited and reproduced freely with the credit “delf-tcf-tef.fr”, the reading date shown
on the page and a link to it. We state our own limits: fees, dates and rules change without notice, and the official source
prevails.</p>

<h2 id="contact">Contact</h2>
<p>Augusto Grone — <strong>gockaman@gmail.com</strong>. Replies within 48 h to requests for data, country extracts or the
verification of a figure; a reported error is corrected the same day.</p>
"""


def block(html, tag):
    return re.search(rf'<{tag} class="site".*?</{tag}>', html, flags=re.S).group(0)


def page(lang):
    src = open(os.path.join(ROOT, "index.html" if lang == "fr" else "en/index.html"), encoding="utf-8").read()
    header, footer = block(src, "header"), block(src, "footer")
    path, title, desc = PATHS[lang], TITLE[lang], DESC[lang]
    home_path, home_label = HOME[lang]
    alts = "".join(f'<link rel="alternate" hreflang="{h}" href="{BASE}{p}">\n'
                   for h, p in [("fr", PATHS["fr"]), ("en", PATHS["en"]), ("x-default", PATHS["fr"])])
    ld = ('{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ['
          f'{{"@type": "ListItem", "position": 1, "name": "{home_label}", "item": "{BASE}{home_path}"}}, '
          f'{{"@type": "ListItem", "position": 2, "name": "{CRUMB[lang]}", "item": "{BASE}{path}"}}]}}')
    body = BODY[lang].replace("{langs}", LANGS[lang])
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{path}">
{alts}<link rel="stylesheet" href="/style.css">
<link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">
<link rel="icon" type="image/png" sizes="48x48" href="/img/favicon-48-v2.png">
<link rel="icon" type="image/png" sizes="96x96" href="/img/favicon-96-v2.png">
<link rel="icon" type="image/png" sizes="192x192" href="/img/favicon-192-v2.png">
<link rel="apple-touch-icon" href="/img/icon-180-v2.png">
<meta name="apple-itunes-app" content="app-id=6790412304">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}/img/og/a-propos.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{LOCALE[lang]}">
<meta property="og:site_name" content="delf-tcf-tef.fr">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{BASE}/img/og/a-propos.png">
<script type="application/ld+json">{ld}</script>
</head>
<body class="">
{header}
<article class="page"><div class="wrap narrow">
<p class="crumb"><a href="{home_path}">{home_label}</a> › {CRUMB[lang]}</p>
{body}
</div></article>
{footer}
</body>
</html>
"""


if __name__ == "__main__":
    for lang in ("fr", "en"):
        f = os.path.join(ROOT, PATHS[lang].strip("/"), "index.html")
        os.makedirs(os.path.dirname(f), exist_ok=True)
        new = page(lang)
        old = open(f, encoding="utf-8").read() if os.path.exists(f) else None
        if old != new:
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(new)
        print(f"{PATHS[lang]} : {'écrite' if old != new else 'inchangée'} ({len(DESC[lang])} car. de description)")
