# -*- coding: utf-8 -*-
"""Ce que les hubs reprennent des pages coupées le 06/11/2026 (coupe_config.py).

Rien n'est réécrit : les faits viennent des fiches existantes de villes_config.py et des guides d'articles_ou_passer.py /
articles_octobre.py, qui restent la source. Les pages coupées ne sont plus rendues ; leurs faits le sont ici, dans la cible.

- GARDER : pour chaque ville, les indices des faits (v["facts"]) qui disent quelque chose de local (adresse réelle de
  passation, horaires, téléphone). Les faits nationaux (tarif, carence) sont déjà dans le hub.
- sections_de(guide, ids) : les sections <h2> d'un guide coupé, déplacées telles quelles dans le hub.
"""
import re

from villes_config import VILLES

PAR_SLUG = {v["slug"]: v for v in VILLES}

GARDER = {
    # Maroc
    "tcf-casablanca": [0, 2], "tcf-rabat": [0, 4], "tcf-marrakech": [1], "tcf-tanger": [0, 3], "tcf-fes": [0, 4],
    "tcf-agadir": [0, 3, 4], "tcf-kenitra": [3], "tcf-meknes": [4], "tcf-el-jadida": [0, 3], "tcf-tetouan": [0, 5], "tcf-oujda": [0, 3],
    # Algérie
    "tcf-oran": [1], "tcf-constantine": [1], "tcf-annaba": [0, 1, 5], "tcf-tlemcen": [1, 4],
    # Tunisie
    "tcf-sousse": [], "tcf-beja": [3],
    # France, TCF
    "tcf-lyon": [0], "tcf-montpellier": [0], "tcf-rennes": [0, 2, 3, 4], "tcf-strasbourg": [0, 5], "tcf-lille": [0, 3, 5], "tcf-nice": [0, 1, 4, 5],
    # France, DELF
    "delf-lyon": [0, 3, 4], "delf-lille": [0, 3, 4, 5], "delf-nantes": [0, 4, 5], "delf-montpellier": [0, 3, 4, 5], "delf-strasbourg": [0],
}


def faits_ville(slug):
    """Les faits locaux d'une ville, et sa note de relevé. Vide si la ville n'a rien en propre."""
    v = PAR_SLUG[slug]
    items = [v["facts"][i] for i in GARDER[slug]]
    out = ""
    if items:
        out += '<ul class="ville-faits">\n' + "\n".join(f"<li>{x}</li>" for x in items) + "\n</ul>\n"
    if v.get("releve_note"):
        out += v["releve_note"].strip() + "\n"
    return out


def tableau_releves(slugs, entete="Centre"):
    """Une ligne par centre, datée : la ligne du centre vient de sa propre page ; les voisins cités ailleurs s'ajoutent ensuite."""
    vus, lignes = set(), []

    def ajoute(r, date):
        cle = re.sub(r"<[^>]+>", "", r[0])
        if cle not in vus:
            vus.add(cle)
            lignes.append(f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{date}</td></tr>")
    for s in slugs:
        v = PAR_SLUG[s]
        if v["releve"]:
            ajoute(v["releve"][0], v.get("releve_date") or "17 septembre 2026")
    for s in slugs:
        v = PAR_SLUG[s]
        for r in v["releve"][1:]:
            ajoute(r, v.get("releve_date") or "17 septembre 2026")
    return ('<div class="tablewrap wide">\n<table>\n<caption>Ce que le site de chaque centre affichait à la date indiquée. '
            '« Non relevé » : non publié ou non vérifié ; le site du centre fait foi.</caption>\n'
            f'<thead><tr><th>{entete}</th><th>Déclinaisons</th><th>Prix</th><th>Sessions et inscription</th><th>Relevé du</th></tr></thead>\n<tbody>\n'
            + "\n".join(lignes) + "\n</tbody>\n</table>\n</div>\n")


def bloc_villes(slugs, ids):
    """Section d'un guide : un h3 par ville (ancre = cible du renvoi), les fiches des centres, les faits locaux, le relevé."""
    from make_centres import card
    from make_villes import centres_of
    out = []
    for s in slugs:
        v = PAR_SLUG[s]
        cards = "\n".join(card(c, ctry) for c, ctry in sorted(centres_of(v["datasets"], v["match"]), key=lambda x: x[0]["name"]))
        out.append(f'<h3 id="{ids[s]}">{v["label"]}</h3>\n<div class="grid c2 centres">\n{cards}\n</div>\n{faits_ville(s)}{tableau_releves([s])}')
    return "\n".join(out)


def sections_de(body, ids):
    """Les sections <h2 id=…> d'un corps d'article, dans l'ordre de ids, sans la barre de série des guides."""
    parts = {}
    for p in re.split(r'(?=<h2 id=")', body):
        m = re.match(r'<h2 id="([^"]+)"', p)
        if m:
            parts[m.group(1)] = p
    out = []
    for i in ids:
        p = re.sub(r'<p class="serie-label">.*?</div>\s*', "", parts[i], flags=re.S)
        out.append(p.strip())
    return "\n\n".join(out) + "\n"
