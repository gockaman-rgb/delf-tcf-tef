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
from article_template import build, indep_line, redirect_map  # noqa: E402
from make_centres import FEI_LISTE, OFFICIEL_PAYS, PAYS_ID, card, clean_city, langs_of, load, esc  # noqa: E402
from villes_config import VILLES  # noqa: E402

DATE = "2026-09-19"
DATE_FR = "19 septembre 2026"
RELEVE = "17 septembre 2026"
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]


# Renvoi de la section « S'inscrire » vers la page qui porte la procédure du pays (06/11/2026).
PROCEDURE_RENVOI = {
    "fr": {"tcf": 'La procédure, les délais et les pièces demandées : <a href="/blog/ou-passer-le-tcf-canada-en-france/">TCF Canada en France</a>, <a href="/blog/ou-passer-le-tcf-irn-en-france/">TCF IRN en France</a>.',
           "delf": 'Le calendrier national, la procédure et les pièges : <a href="/blog/ou-passer-le-delf-en-france/">où passer le DELF en France</a>.'},
    "ca": {"tcf": 'Comment obtenir une place, les prix et les annulations : <a href="/blog/ou-passer-le-tcf-canada-au-canada/">où passer le TCF Canada au Canada</a>.'},
    "dz": {"tcf": 'Les étapes, les pièces, les délais et le faux site à éviter : <a href="/centres/tcf-algerie/#etapes">TCF en Algérie</a>.'},
    "ma": {"tcf": 'Les étapes et les règles : <a href="/centres/tcf-maroc/#inscription">TCF au Maroc</a>.'},
    "tn": {"tcf": 'Le rendez-vous, l\'inscription sur place et le calendrier de chaque pôle : <a href="/centres/tcf-tunisie/#inscription">TCF en Tunisie</a>.'},
}


def list_date(datasets):
    """Date de la liste FEI d'une page : celle de son fichier de données (26/10/2026 : TCF France et Canada relus)."""
    iso = max(load(ds).get("date", DATE) for ds in datasets)
    y, m, d = iso.split("-")
    return iso, f"{'1er' if d == '01' else int(d)} {MOIS[int(m) - 1]} {y}"


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
    liso, lfr = list_date(v["datasets"])
    mod = v.get("modified") or (DATE, DATE_FR)
    if liso > mod[0]:              # liste relue après la dernière retouche de la page
        mod = (liso, lfr)
    exam = v["exam"]
    label = v["label"]
    country = v["country"]
    # cartes
    cards = "\n".join(card(c, ctry) for c, ctry in sorted(cs, key=lambda x: x[0]["name"]))
    near_html = ""
    if near:
        near_html = (f"<h3 id=\"proximite\">À proximité</h3>\n<div class=\"grid c2 centres\">\n"
                     + "\n".join(card(c, ctry) for c, ctry in sorted(near, key=lambda x: (clean_city(x[0]['city']), x[0]['name']))) + "\n</div>")
    # relevé
    rows = v.get("releve", [])
    releve = v.get("releve_date") or RELEVE
    if rows:
        tbl = (f'<div class="tablewrap wide">\n<table>\n<caption>Relevé du {releve}.</caption>\n'
               '<thead><tr><th>Centre</th><th>' + ("Déclinaisons" if exam == "tcf" else "Diplômes") +
               '</th><th>Prix</th><th>Sessions et inscription</th></tr></thead>\n<tbody>\n'
               + "\n".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in rows)
               + "\n</tbody>\n</table>\n</div>")
    else:
        tbl = "<p>Nous n'avons pas encore ouvert les sites de ces centres : les déclinaisons, prix et dates sont à vérifier sur leur site ou par téléphone.</p>"
    exam_label = "TCF" if exam == "tcf" else "DELF-DALF"
    h2l = v.get("h2_label", label)
    head = (f"Le centre agréé {v['prep']} {h2l}" if n == 1 else f"Les {n} centres agréés {v['prep']} {h2l}")
    # 06/11/2026 : plus de bloc de chiffres, de paragraphe de procédure ni de guides commentés sur les pages de ville. Ils
    # répétaient le même texte de page en page (40 à 60 % de phrases partagées) : la procédure vit sur le hub du pays ou le guide.
    intro_centres = v["centres_intro"].replace("{liste_fei}", lfr) if v["centres_intro_propre"] else ""
    renvoi = PROCEDURE_RENVOI[country][exam]
    body = f"""
<h2 id="centres">{head}</h2>
{f"<p>{intro_centres}</p>" if intro_centres else ""}
<div class="grid c2 centres">
{cards}
</div>
{near_html}

<h2 id="releve">Prix et dates</h2>
{tbl}
{v.get('releve_note', '')}

<h2 id="inscription">S'inscrire {v['prep']} {label}</h2>
<p>{renvoi}</p>
"""
    toc = [("centres", head), ("releve", "Prix et dates"), ("inscription", f"S'inscrire {v['prep']} {label}")]
    a = {
        "section": "centres", "section_name": "Centres", "og_slug": v.get("og_slug", "centres"),
        "slug": v["slug"], "accent": "accent-tcf" if exam == "tcf" else "accent-delf", "crumb": v["crumb"],
        "title": v["title"], "desc": v["desc"], "h1": v["h1"],
        "indep": official_line(v),
        "published": v.get("published") or DATE, "modified": mod[0],
        "date_fr": mod[1], "read": 5,
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
(filtre « {country_label(country)} », type « {exam_label} »), consultée le {lfr} — coordonnées telles que FEI
les publie, adresses e-mail génériques seulement ; sites des centres cités dans le tableau, consultés le
{releve}. Les prix, dates et déclinaisons changent sans préavis : vérifiez-les sur le site du centre
avant de payer.""",
    }
    assert len(a["title"]) <= 60, (v["slug"], len(a["title"]))
    assert len(a["desc"]) <= 158, (v["slug"], len(a["desc"]))
    alts, links = langs_of(f"/centres/{v['slug']}/")
    if alts:
        a["alternates"], a["lang_links"] = alts, links
    return a


def official_line(v):
    """Ligne « site indépendant » : plateforme ou site unique quand le pays en a un, sinon la liste officielle de FEI."""
    ctry = country_label(v["country"])
    if ctry in OFFICIEL_PAYS:
        u, label = OFFICIEL_PAYS[ctry]
        return indep_line("fr", u, label, single=True)
    typ = "tcf" if v["exam"] == "tcf" else "delf_dalf"
    return indep_line("fr", FEI_LISTE % (PAYS_ID[ctry], typ), f"centres {'TCF' if v['exam'] == 'tcf' else 'DELF-DALF'}, {ctry} (FEI)")


def country_label(c):
    return {"fr": "France", "ca": "Canada", "dz": "Algérie", "ma": "Maroc", "tn": "Tunisie"}[c]


def main():
    force = "--force" in sys.argv
    rd = redirect_map()
    arts = [page(v) for v in VILLES if f"/centres/{v['slug']}/" not in rd]
    build(arts, overwrite=force)


if __name__ == "__main__":
    main()
