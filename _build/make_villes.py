#!/usr/bin/env python3
"""Pages par ville — « TCF à Paris », « Centre TCF Alger », « DELF à Lyon »… (19/09/2026).

Ce que les gens tapent (autocomplétion Google, 19/09/2026) : « tcf canada paris », « tcf irn lyon »,
« centre tcf alger », « tcf canada maroc rabat », « où passer le delf b2 à paris »… Chaque page :
les centres agréés de la ville (données FEI, contacts), ce que nous avons relevé sur leurs sites
(prix, dates, déclinaisons — daté), la procédure d'inscription du pays, une FAQ.

Usage : python3 _build/make_villes.py [--force]
"""

import json
import os
import re
import sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from article_template import build  # noqa: E402
from make_centres import card, clean_city, load, esc, stats, slug as slugify  # noqa: E402
from villes_config import VILLES, PROCEDURES  # noqa: E402

DATE = "2026-09-19"
DATE_FR = "19 septembre 2026"
RELEVE = "17 septembre 2026"


def centres_of(datasets, names):
    out = []
    for ds in datasets:
        d = load(ds)
        for c in d["centres"]:
            if clean_city(c["city"]) in names:
                out.append((c, d["country"]))
    return out


def page(v):
    cs = centres_of(v["datasets"], v["match"])
    near = centres_of(v["datasets"], v.get("nearby", [])) if v.get("nearby") else []
    n, so = len(cs), sum(1 for c, _ in cs if c["so"])
    exam = v["exam"]
    label = v["label"]
    country = v["country"]
    proc = PROCEDURES[country][exam]
    # cartes
    cards = "\n".join(card(c, ctry) for c, ctry in sorted(cs, key=lambda x: x[0]["name"]))
    near_html = ""
    if near:
        near_html = (f"<h3 id=\"proximite\">À proximité</h3>\n<div class=\"grid c2 centres\">\n"
                     + "\n".join(card(c, ctry) for c, ctry in sorted(near, key=lambda x: (clean_city(x[0]['city']), x[0]['name']))) + "\n</div>")
    # relevé
    rows = v.get("releve", [])
    if rows:
        tbl = ('<div class="tablewrap wide">\n<table>\n<caption>Ce que le site de chaque centre affichait le '
               f'{RELEVE}. « Non relevé » : non publié, ou non vérifié — le site du centre fait foi.</caption>\n'
               '<thead><tr><th>Centre</th><th>' + ("Déclinaisons" if exam == "tcf" else "Diplômes") +
               '</th><th>Prix</th><th>Sessions et inscription</th></tr></thead>\n<tbody>\n'
               + "\n".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in rows)
               + "\n</tbody>\n</table>\n</div>")
    else:
        tbl = "<p>Nous n'avons pas encore ouvert les sites de ces centres : les déclinaisons, prix et dates sont à vérifier sur leur site ou par téléphone.</p>"
    exam_label = "TCF" if exam == "tcf" else "DELF-DALF"
    h2l = v.get("h2_label", label)
    head = (f"Le centre agréé {v['prep']} {h2l}" if n == 1 else f"Les {n} centres agréés {v['prep']} {h2l}")
    if exam == "tcf":
        stat2 = (str(so), "sur ordinateur", "tous les centres de la ville" if so == n else "les autres sur papier")
    else:
        stat2 = ("3", "sessions nationales", "d'ici fin 2026 : oct., nov., déc.")
    st = stats([(str(n), f"centre{'s' if n > 1 else ''} agréé{'s' if n > 1 else ''}", f"liste FEI du {DATE_FR}"),
                stat2, v["stat3"], v["stat4"]])
    guides = "\n".join(f'<li><a href="{u}">{t}</a>' + (f"\n<p>{d}</p>" if d else "") + "</li>" for u, t, d in v["guides"])
    body = f"""
{st}

<h2 id="centres">{head}</h2>
<p>{v['centres_intro']}</p>
<div class="grid c2 centres">
{cards}
</div>
{near_html}

<h2 id="releve">Ce que nous avons relevé, centre par centre</h2>
{tbl}
{v.get('releve_note', '')}

<h2 id="inscription">S'inscrire {v['prep']} {label}</h2>
{proc}
<p>Pour la procédure complète, les prix relevés et les pièges du pays :</p>
<ul class="posts">
{guides}
</ul>
"""
    toc = [("centres", head), ("releve", "Ce que nous avons relevé"), ("inscription", f"S'inscrire {v['prep']} {label}")]
    a = {
        "section": "centres", "section_name": "Centres", "og_slug": v.get("og_slug", "centres"),
        "slug": v["slug"], "accent": "accent-tcf" if exam == "tcf" else "accent-delf", "crumb": v["crumb"],
        "title": v["title"], "desc": v["desc"], "h1": v["h1"],
        "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": 5,
        "intro": v["intro"] % {"n": n, "so": so},
        "facts": v["facts"],
        "toc": toc, "body": body,
        "cta_h2": v.get("cta_h2", "Le centre vous donne la date ; le niveau, c'est vous"),
        "cta_p": v.get("cta_p", f"""Une session se paie en entier et se repasse après un délai. Les examens blancs de
l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent le format officiel de chaque
déclinaison — {'TCF Canada, TCF IRN, TCF Québec' if exam == 'tcf' else 'DELF B1, DELF B2, DALF C1'} — avec la
notation du vrai test et la correction IA de l'écrit et de l'oral."""),
        "faq": v["faq"],
        "also": v["also"],
        "sources": f"""<strong>Sources.</strong> Liste des centres d'examen de France Éducation international
(filtre « {country_label(country)} », type « {exam_label} »), consultée le {DATE_FR} — coordonnées telles que FEI
les publie, adresses e-mail génériques seulement ; sites des centres cités dans le tableau, consultés le
{RELEVE}. Les prix, dates et déclinaisons changent sans préavis : vérifiez-les sur le site du centre
avant de payer.""",
    }
    assert len(a["title"]) <= 60, (v["slug"], len(a["title"]))
    assert len(a["desc"]) <= 158, (v["slug"], len(a["desc"]))
    return a


def country_label(c):
    return {"fr": "France", "ca": "Canada", "dz": "Algérie", "ma": "Maroc", "tn": "Tunisie"}[c]


def main():
    force = "--force" in sys.argv
    arts = [page(v) for v in VILLES]
    build(arts, overwrite=force)


if __name__ == "__main__":
    main()
