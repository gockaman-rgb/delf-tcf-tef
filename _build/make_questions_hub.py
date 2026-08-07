#!/usr/bin/env python3
"""Génère /questions/ — l'index de toutes les questions traitées sur le site.

Les questions sont EXTRAITES des blocs FAQ existants : le hub ne peut donc pas
se désynchroniser du contenu, et il n'invente aucune réponse. Chaque entrée
renvoie vers la page qui répond, à son ancre #faq.

⚠️ Pas de schéma FAQPage sur cette page : les réponses sont déjà balisées sur
les 30 pages sources. Dupliquer le balisage serait redondant et risqué.
Le hub porte un `CollectionPage` + `BreadcrumbList`.

Relancer après tout ajout de FAQ : `python3 _build/make_questions_hub.py`
"""

import glob
import html
import json
import os
import re
import unicodedata

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
BASE = "https://delf-tcf-tef.fr"
APP = "https://apps.apple.com/fr/app/tcf-delf-tef-tests-2026/id6790412304"

# ordre d'affichage → (titre de rubrique, chapô)
SECTIONS = [
    ("choisir", "Choisir son examen", "Quelle version passer, ce que chacune prouve, et à qui elle sert."),
    ("canada", "Immigration au Canada", "NCLC, Entrée express, citoyenneté : les seuils et les tests acceptés."),
    ("quebec", "Programmes québécois", "Échelle québécoise, PSTQ, PEQ — un référentiel distinct du fédéral."),
    ("france", "Naturalisation et titres de séjour", "Les niveaux exigés depuis 2026 et les justificatifs recevables."),
    ("argent", "Prix, financement et démarches", "Ce que coûte un test, ce que le CPF finance, les délais et la validité."),
    ("epreuves", "S'entraîner par épreuve", "Formats, durées, consignes et méthode, épreuve par épreuve."),
    ("app", "L'application", "Contenu, correction IA, plan d'étude, abonnement et confidentialité."),
]

# affectation d'une page à sa rubrique
PAGE_SECTION = {
    "blog/difference-tcf-tef": "choisir", "blog/diplome-ou-test-delf-tcf": "choisir",
    "examens": "choisir", "blog/tcf-irn-ou-tef-irn": "choisir",
    "tcf-canada": "canada", "blog/tcf-canada-nclc-7": "canada",
    "blog/tcf-ou-tef-canada": "canada", "tef-canada": "canada",
    "tcf-quebec": "quebec", "blog/tefaq-oral-quebec": "quebec",
    "tcf-irn": "france", "delf-b1": "france", "delf-b2": "france", "dalf": "france",
    "blog/naturalisation-2026-niveau-b2": "france", "blog/carte-de-resident-b1-2026": "france",
    "blog/b1-ou-b2-nationalite-francaise": "france",
    "blog/prix-tcf-tef": "argent", "blog/cpf-test-francais": "argent",
    "blog/repasser-tcf-tef": "argent", "blog/validite-attestation-tcf-tef": "argent",
    "examens-blancs": "epreuves", "blog/examen-blanc-tcf-gratuit": "epreuves",
    "score-tcf-699": "epreuves", "blog/production-ecrite-delf-b2": "epreuves",
    "blog/synthese-dalf-c1": "epreuves",
    "blog/exercices-comprehension-orale-tcf-canada": "epreuves",
    "blog/exercices-comprehension-ecrite-tcf-canada": "epreuves",
    "blog/sujets-expression-ecrite-tcf-canada": "epreuves",
    "blog/sujets-expression-orale-tcf-canada": "epreuves",
    "blog/exercices-tcf-irn": "epreuves", "blog/exercices-tef-canada": "epreuves",
    "blog/exercices-delf-b2": "epreuves", "blog/exercices-structures-langue-tcf": "epreuves",
    "contenu": "app", "correction-ia": "app", "plan-etude": "app", "support": "app",
}

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


def norm(t):
    t = html.unescape(t).replace(" ", " ").replace(" ", " ")
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", re.sub(r"<[^>]+>", "", t))).strip()


def collect():
    """Toutes les questions des blocs FAQPage, dédoublonnées, avec leur page."""
    out, seen = {k: [] for k, _, _ in SECTIONS}, set()
    files = sorted(f for f in glob.glob(os.path.join(ROOT, "**/*.html"), recursive=True)
                   if "/.claude/" not in f and "/_build/" not in f)
    for path in files:
        rel = os.path.relpath(path, ROOT).replace("/index.html", "").replace(".html", "")
        sec = PAGE_SECTION.get(rel)
        if not sec:
            continue
        s = open(path, encoding="utf-8").read()
        title = norm(re.search(r"<h1>(.*?)</h1>", s, re.S).group(1))
        url = "/" if rel == "index" else f"/{rel}/"
        for m in re.finditer(r"application/ld\+json[^>]*>(.*?)</script>", s, re.S):
            d = json.loads(m.group(1))
            if d.get("@type") != "FAQPage":
                continue
            for q in d["mainEntity"]:
                name = norm(q["name"])
                key = name.lower().rstrip(" ?").replace("'", "'")
                if key in seen:
                    continue
                seen.add(key)
                out[sec].append((name, url, title))
    return out


def build():
    data = collect()
    total = sum(len(v) for v in data.values())

    blocks, toc = [], []
    for key, titre, chapo in SECTIONS:
        items = data[key]
        if not items:
            continue
        toc.append(f'<li><a href="#{key}">{titre}</a> <span class="badge">{len(items)}</span></li>')
        lis = "\n".join(
            f'<li><a href="{u}#faq">{q}</a>\n<p>{t}</p></li>' for q, u, t in items)
        blocks.append(
            f'<h2 id="{key}">{titre}</h2>\n<p>{chapo}</p>\n<ul class="posts">\n{lis}\n</ul>')

    desc = (f"Les {total} questions traitées sur le site, classées par thème : examens, "
            "immigration, naturalisation, prix et entraînement. Chacune renvoie à sa réponse.")
    ld_page = json.dumps({
        "@context": "https://schema.org", "@type": "CollectionPage",
        "name": "Toutes les questions sur le DELF, le TCF et le TEF",
        "description": desc, "url": f"{BASE}/questions/", "inLanguage": "fr-FR",
        "isPartOf": {"@type": "WebSite", "name": "delf-tcf-tef.fr", "url": f"{BASE}/"},
    }, ensure_ascii=False)
    ld_crumb = json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": "Toutes les questions",
             "item": f"{BASE}/questions/"}],
    }, ensure_ascii=False)

    doc = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Toutes vos questions sur le DELF, le TCF et le TEF</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}/questions/">
<link rel="stylesheet" href="/style.css">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/img/favicon-96.png" sizes="96x96" type="image/png">
<link rel="icon" href="/img/favicon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="/img/icon-180.png">
<meta name="apple-itunes-app" content="app-id=6790412304">
<meta property="og:title" content="Toutes vos questions sur le DELF, le TCF et le TEF">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}/img/og/questions.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="{BASE}/questions/">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="delf-tcf-tef.fr">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Toutes vos questions sur le DELF, le TCF et le TEF">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{BASE}/img/og/questions.png">
<script type="application/ld+json">
{ld_page}
</script>
<script type="application/ld+json">
{ld_crumb}
</script>
</head>
<body>
{HEADER}
<article class="page"><div class="wrap narrow">
<p class="crumb"><a href="/">Accueil</a> › Toutes les questions</p>
<h1>Toutes vos questions sur le DELF, le TCF et le TEF</h1>
<p class="meta">Par <a href="/a-propos/">Augusto Grone</a> · Mis à jour le 7 août 2026 · {total} questions</p>

<p class="intro">Les <strong>{total} questions</strong> traitées sur ce site, classées par thème.
Chaque question renvoie à la page qui y répond, avec ses sources et sa date de vérification. Si
vous ne trouvez pas la vôtre, <a href="/support/">écrivez-nous</a> — c'est souvent comme ça qu'un
article naît.</p>

<div class="toc"><strong>Par thème</strong><ol>
{chr(10).join(toc)}
</ol></div>

{chr(10).join(blocks)}

<div class="cta-band">
<h2>La meilleure réponse reste votre propre score</h2>
<p>Examens blancs chronométrés au format officiel de 15 variantes d'examens, conversion NCLC et
Échelle québécoise par épreuve, correction IA de l'écrit et de l'oral sur les critères officiels —
dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».</p>
<a class="btn" href="{APP}">Télécharger sur l'App&nbsp;Store</a>
</div>

<div class="note">
<p><strong>Comment cette page est tenue à jour.</strong> Elle est générée automatiquement à partir
des questions réellement publiées sur le site : elle ne peut donc pas annoncer une réponse qui
n'existe pas. Les réponses elles-mêmes restent sur leurs pages d'origine, avec leurs sources et
leur date de vérification — la réglementation et les formats d'examen évoluent, parfois sans
annonce.</p>
</div>

</div></article>
{FOOTER}
</body>
</html>
"""
    out = os.path.join(ROOT, "questions", "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print(f"✓ /questions/ — {total} questions")
    for key, titre, _ in SECTIONS:
        if data[key]:
            print(f"    {titre:38} {len(data[key]):3}")


if __name__ == "__main__":
    build()
