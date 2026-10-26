#!/usr/bin/env python3
"""Annuaire des centres d'examen — /centres/ et ses pages par pays ou région.

Données : `_build/data/<type>_<pays>.json`, extraites de la liste officielle des centres de
France Éducation international le 19/09/2026 (voir data/parse_fei.py). Chaque centre porte
nom, adresse, téléphone, e-mails (filtrés : adresses génériques seulement), site, et l'option
« sessions sur ordinateur ». La liste FEI ne dit PAS quelles déclinaisons un centre organise.

Usage : python3 _build/make_centres.py [--force]
"""

import glob
import html
import json
import os
import re
import sys
import unicodedata
from collections import OrderedDict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from article_template import build  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
DATE = "2026-09-19"
DATE_FR = "19 septembre 2026"
FEI_LISTE = "https://www.france-education-international.fr/centres-d-examen/liste?pays=%s&type-centre=%s"
FEI_CARTE = "https://www.france-education-international.fr/centres-d-examen/carte?type-centre=%s"
PAYS_ID = {"France": 73, "Canada": 112, "Algérie": 115, "Maroc": 117, "Tunisie": 118, "Sénégal": 145,
           "Côte d'Ivoire": 128, "Cameroun": 124, "Belgique": 62, "Liban": 106, "Inde": 45,
           "République démocratique du Congo": 143, "Bénin": 122, "Togo": 149, "Guinée": 132,
           "Gabon": 130, "Mali": 137, "Congo": 127, "Mauritanie": 139, "Haïti": 27, "Maurice": 138,
           "Égypte": 116, "Suisse": 94, "Royaume-Uni": 89, "États-Unis": 113,
           "Émirats arabes unis": 101, "Turquie": 95, "Brésil": 19, "Mexique": 30, "Colombie": 21,
           "Espagne": 70, "Argentine": 15, "Chili": 20, "Pérou": 34, "Équateur": 25}
PAYS_ID.update({"Allemagne": 60, "Italie": 78, "Pays-Bas": 84, "Portugal": 86, "Roumanie": 87, "Pologne": 85,
                "Grèce": 74, "Irlande": 76, "Autriche": 61, "Luxembourg": 375})   # Europe (26/10/2026 : pays_config_eu.py)
CC = {"France": "33", "Canada": "1", "Algérie": "213", "Maroc": "212", "Tunisie": "216", "Sénégal": "221",
      "Côte d'Ivoire": "225", "Cameroun": "237", "Belgique": "32", "Liban": "961", "Inde": "91",
      "République démocratique du Congo": "243", "Bénin": "229", "Togo": "228", "Guinée": "224",
      "Gabon": "241", "Mali": "223", "Congo": "242", "Mauritanie": "222", "Haïti": "509", "Maurice": "230",
      "Égypte": "20", "Suisse": "41", "Royaume-Uni": "44", "États-Unis": "1", "Émirats arabes unis": "971",
      "Turquie": "90", "Brésil": "55", "Mexique": "52", "Colombie": "57"}

REGIONS_FR = {
    "Auvergne-Rhône-Alpes": "01 03 07 15 26 38 42 43 63 69 73 74",
    "Bourgogne-Franche-Comté": "21 25 39 58 70 71 89 90",
    "Bretagne": "22 29 35 56",
    "Centre-Val de Loire": "18 28 36 37 41 45",
    "Corse": "20 2A 2B",
    "Grand Est": "08 10 51 52 54 55 57 67 68 88",
    "Hauts-de-France": "02 59 60 62 80",
    "Île-de-France": "75 77 78 91 92 93 94 95",
    "Normandie": "14 27 50 61 76",
    "Nouvelle-Aquitaine": "16 17 19 23 24 33 40 47 64 79 86 87",
    "Occitanie": "09 11 12 30 31 32 34 46 48 65 66 81 82",
    "Pays de la Loire": "44 49 53 72 85",
    "Provence-Alpes-Côte d'Azur": "04 05 06 13 83 84",
    "Outre-mer": "97 98",
}
DEP2REG = {d: r for r, ds in REGIONS_FR.items() for d in ds.split()}
REGION_ORDER = ["Île-de-France", "Auvergne-Rhône-Alpes", "Provence-Alpes-Côte d'Azur", "Occitanie",
                "Nouvelle-Aquitaine", "Hauts-de-France", "Grand Est", "Pays de la Loire", "Bretagne",
                "Normandie", "Centre-Val de Loire", "Bourgogne-Franche-Comté", "Corse", "Outre-mer"]


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def esc(s):
    return html.escape(s, quote=True)


def load(name):
    d = json.load(open(os.path.join(DATA, name + ".json"), encoding="utf-8"))
    # FEI liste parfois deux fois le même centre (Gaspé, CASNAV de La Réunion) : on garde la première entrée
    seen, out = set(), []
    for c in d["centres"]:
        k = (c["name"].lower(), c["city"].lower(), c["address"].lower())
        if k not in seen:
            seen.add(k)
            out.append(c)
    for c in out:
        c["type"] = d.get("type", "tcf")
    d["centres"] = out
    return d


def tel_href(phone, country):
    d = re.sub(r"\D", "", phone.split("/")[0])
    if not d:
        return ""
    cc = CC.get(country, "")
    if d.startswith("00"):
        return "+" + d[2:]
    if country == "France" and len(d) == 10 and d[0] == "0":
        return "+33" + d[1:]
    if cc and d.startswith(cc) and len(d) > len(cc) + 5:
        return "+" + d
    if country in ("Canada", "États-Unis"):
        if len(d) == 10:
            return "+1" + d
        if len(d) == 11 and d[0] == "1":
            return "+" + d
        if d.startswith("01") and len(d) == 11:
            return "+" + d[1:]
    if cc and d[0] == "0":
        return "+" + cc + d[1:]
    return "+" + d if len(d) >= 8 else ""


def clean_city(city):
    # « Toulouse Cedex 4 » → Toulouse ; « Montréal (Québec) » → Montréal ; majuscules → capitalisées
    c = re.sub(r"\s*\(.*?\)\s*", "", city)
    c = re.sub(r"\s+cedex.*$", "", c, flags=re.I).strip()
    if c.isupper():
        c = c.title()
    return c


def province_ca(city):
    m = re.search(r"\((.*?)\)", city)
    return m.group(1) if m else "Autres"


def card(c, country):
    lines = []
    addr = " ".join(x for x in [c["address"], (c["cp"] + " " + clean_city(c["city_cp"])).strip()] if x).strip()
    addr = re.sub(r"\s+-\s*$", "", addr)
    if addr:
        lines.append(f'<p class="addr">{esc(addr)}</p>')
    contact = []
    if c["phone"]:
        href = tel_href(c["phone"], country)
        contact.append(f'<a href="tel:{href}">{esc(c["phone"])}</a>' if href else esc(c["phone"]))
    for e in c["emails"][:2]:
        contact.append(f'<a href="mailto:{esc(e)}">{esc(e)}</a>')
    if c["url"]:
        u = c["url"] if c["url"].startswith("http") else "http://" + c["url"]
        host = re.sub(r"^https?://(www\.)?", "", u).split("/")[0]
        contact.append(f'<a href="{esc(u)}" rel="noopener nofollow">{esc(host)}</a>')
    for item in contact:
        lines.append('<p class="contact">' + item + "</p>")
    if c.get("type", "tcf") == "tcf":   # la liste FEI ne renseigne le support que pour le TCF
        badge = '<span class="badge ok">sur ordinateur</span>' if c["so"] else '<span class="badge part">papier</span>'
        lines.append(f'<p class="badges">{badge}</p>')
    return f'<div class="card centre"><h4>{esc(c["name"])}</h4>\n' + "\n".join(lines) + "</div>"


_USED = set()


def uniq(cid):
    """Identifiant unique dans la page (Saint-Denis 93 / 974, Québec province / ville…)."""
    base, k = cid, 2
    while cid in _USED:
        cid = f"{base}-{k}"
        k += 1
    _USED.add(cid)
    return cid


def group_cards(centres, country, head_level=3):
    """Cartes groupées par ville (titre h3 ou h4)."""
    cities = OrderedDict()
    for c in sorted(centres, key=lambda x: (slug(clean_city(x["city"])), x["name"])):
        cities.setdefault(clean_city(c["city"]), []).append(c)
    out = []
    for city, cs in cities.items():
        cid = uniq(slug(city))
        n = f" <span class=\"count\">({len(cs)})</span>" if len(cs) > 1 else ""
        out.append(f'<h{head_level} id="{cid}">{esc(city)}{n}</h{head_level}>')
        out.append('<div class="grid c2 centres">\n' + "\n".join(card(c, country) for c in cs) + "\n</div>")
    return "\n".join(out), list(cities.keys())


def section_france(d, exam_label):
    regs = OrderedDict((r, []) for r in REGION_ORDER)
    for c in d["centres"]:
        dep = c["cp"][:2] if c["cp"] else ""
        if dep == "20":
            reg = "Corse"
        elif dep.startswith("9") and c["cp"][:2] in ("97", "98"):
            reg = "Outre-mer"
        else:
            reg = DEP2REG.get(dep, "Outre-mer" if dep in ("97", "98") else "Autres")
        regs.setdefault(reg, []).append(c)
    body, index = [], []
    for reg, cs in regs.items():
        if not cs:
            continue
        rid = uniq("region-" + slug(reg))
        index.append((rid, f"{reg} ({len(cs)})"))
        cards, cities = group_cards(cs, "France", 3)
        body.append(f'<h2 id="{rid}">{esc(reg)} — {len(cs)} centre{"s" if len(cs) > 1 else ""}</h2>\n{cards}')
    return "\n\n".join(body), index


def section_canada(d):
    order = ["Québec", "Ontario", "Colombie-Britannique", "Alberta", "Saskatchewan", "Manitoba",
             "Nouveau-Brunswick", "Nouvelle-Écosse", "Terre-Neuve-et-Labrador", "Nunavut"]
    provs = OrderedDict((p, []) for p in order)
    for c in d["centres"]:
        provs.setdefault(province_ca(c["city"]), []).append(c)
    body, index = [], []
    for p, cs in provs.items():
        if not cs:
            continue
        pid = uniq("province-" + slug(p))
        index.append((pid, f"{p} ({len(cs)})"))
        cards, _ = group_cards(cs, "Canada", 3)
        body.append(f'<h2 id="{pid}">{esc(p)} — {len(cs)} centre{"s" if len(cs) > 1 else ""}</h2>\n{cards}')
    return "\n\n".join(body), index


def section_country_cities(d):
    cards, cities = group_cards(d["centres"], d["country"], 2)
    index = [(slug(c), c) for c in cities]
    return cards, index


def section_multi(datasets, pointers=None):
    """Un pays par h2. Un pays qui a sa page détaillée (make_pays.py, 08/10/2026) n'y est pas recopié :
    un renvoi remplace ses cartes, pour qu'une même fiche ne vive qu'à un endroit."""
    pointers = pointers or {}
    body, index = [], []
    for d in datasets:
        cid = uniq("pays-" + slug(d["country"]))
        n = len(d["centres"])
        index.append((cid, f"{d['country']} ({n})"))
        src = FEI_LISTE % (PAYS_ID[d["country"]], "tcf")
        head = (f'<h2 id="{cid}">{esc(d["country"])} — {n} centre{"s" if n > 1 else ""}</h2>\n'
                f'<p class="src">Liste officielle : <a href="{src}" rel="noopener">centres TCF, {esc(d["country"])}</a> (FEI).</p>\n')
        if d["country"] in pointers:
            url, label, summary = pointers[d["country"]]
            body.append(head + f'<div class="card card-link"><span class="tag">Page pays</span><h3><a href="{url}">{label}</a></h3>'
                               f'<p>{summary}</p></div>')
            continue
        cards, _ = group_cards(d["centres"], d["country"], 3)
        body.append(head + cards)
    return "\n\n".join(body), index


def chips(index):
    return '<div class="chips index">\n' + "\n".join(f'<a class="chip" href="#{i}">{esc(t)}</a>' for i, t in index) + "\n</div>"


VILLES_KEY = {"tcf-france": ("fr", "tcf"), "delf-france": ("fr", "delf"), "tcf-canada": ("ca", "tcf"),
              "tcf-algerie": ("dz", "tcf"), "tcf-maroc": ("ma", "tcf"), "tcf-tunisie": ("tn", "tcf")}


def villes_of(key):
    """Les pages par ville (make_villes.py) d'un pays et d'un examen : [(url, libellé)]."""
    from villes_config import VILLES
    country, exam = key
    return [(f"/centres/{v['slug']}/", v["crumb"]) for v in VILLES if v["country"] == country and v["exam"] == exam]


def villes_block(slug):
    key = VILLES_KEY.get(slug)
    if not key:
        return ""
    items = villes_of(key)
    if not items:
        return ""
    exam = "TCF" if key[1] == "tcf" else "DELF"
    what = "déclinaisons, prix, dates" if key[1] == "tcf" else "niveaux, prix, dates"
    return (f'\n<h2 id="villes">Les guides par ville</h2>\n<p>Pour les grandes villes, une page réunit les centres {exam} '
            f'agréés avec leurs contacts, ce que leurs sites affichaient le 17 septembre 2026 — {what} — '
            'et la procédure d\'inscription :</p>\n<div class="chips">\n'
            + "\n".join(f'<a class="chip" href="{u}">{esc(t)}</a>' for u, t in items) + "\n</div>\n")


def fr_int(n):
    """1067 → « 1 067 » (espace insécable)."""
    return f"{n:,}".replace(",", "\u00a0")


def stats(items):
    return '<div class="stats">\n' + "\n".join(
        f"<div class=\"stat\"><b>{b}</b><span>{s}</span>{('<em>' + e + '</em>') if e else ''}</div>"
        for b, s, e in items) + "\n</div>"


def counts(datasets):
    cs = [c for d in datasets for c in d["centres"]]
    cities = {clean_city(c["city"]) for c in cs}
    return len(cs), sum(1 for c in cs if c["so"]), len(cities)


METHOD = """<div class="note">
<p><strong>Comment lire cette liste.</strong> Elle reprend la liste officielle des centres agréés
par France Éducation international, consultée le %(date)s — nom, adresse, téléphone, adresse
e-mail générique et site tels que FEI les publie. Elle ne dit pas quelles <em>déclinaisons</em>
un centre organise (%(decl)s) ni ses dates et tarifs : c'est sur le site ou au téléphone du centre
que cela se vérifie, et nos guides « Où passer » l'ont fait pour les principaux centres.
%(support)sUn organisme absent de cette liste n'est pas agréé.</p>
</div>"""


class _Safe(dict):
    def __missing__(self, k):
        return "{" + k + "}"


def computed(datasets):
    cs = [c for d in datasets for c in d["centres"]]
    n, so, ncity = counts(datasets)
    def reg(c):
        dep = c["cp"][:2] if c["cp"] else ""
        return "Corse" if dep == "20" else DEP2REG.get(dep, "")
    v = dict(n=n, so=so, ncity=ncity,
             idf=sum(1 for c in cs if reg(c) == "Île-de-France"), ara=sum(1 for c in cs if reg(c) == "Auvergne-Rhône-Alpes"),
             paca=sum(1 for c in cs if reg(c) == "Provence-Alpes-Côte d'Azur"), occ=sum(1 for c in cs if reg(c) == "Occitanie"),
             paris=sum(1 for c in cs if c["cp"].startswith("75")), lyon=sum(1 for c in cs if clean_city(c["city"]) == "Lyon"),
             deps=len({c["cp"][:2] for c in cs if c["cp"]}))
    return _Safe(v)


def page(spec, datasets):
    _USED.clear()
    _USED.update({"utiliser", "liste", "sources-officielles", "faq", "a-lire"})
    n, so, ncity = counts(datasets)
    vals = computed(datasets)
    spec = dict(spec, facts=[f.format_map(vals) for f in spec["facts"]])
    if spec["layout"] == "france":
        body, index = section_france(datasets[0], spec["exam"])
    elif spec["layout"] == "canada":
        body, index = section_canada(datasets[0])
    elif spec["layout"] == "cities":
        body, index = section_country_cities(datasets[0])
    else:
        body, index = section_multi(datasets, spec.get("pointers"))
    list_date = spec.get("list_date_fr", DATE_FR)
    st = stats([(str(n), "centres agréés", f"liste FEI du {list_date}"),
                (str(so), "sur ordinateur", "les autres sur papier"),
                (str(ncity), "villes", spec.get("cities_note", "")),
                (spec["stat4"][0], spec["stat4"][1], spec["stat4"][2])])
    guides = "\n".join(f'<li><a href="{u}">{t}</a>' + (f"\n<p>{d}</p>" if d else "") + "</li>" for u, t, d in spec["guides"])
    src_links = " · ".join(f'<a href="{u}" rel="noopener">{t}</a>' for t, u in spec["sources_links"])
    support = ("« Sur ordinateur » signifie que le centre propose des sessions sur ordinateur ; « papier » qu'il n'en\ndéclare pas. " if spec["exam"] == "TCF" else "")
    method = METHOD % {"date": list_date, "decl": spec["decl"], "support": support}
    full_body = f"""
{st}

<h2 id="utiliser">Avant de choisir un centre</h2>
{method}
<p>Pour la procédure d'inscription, les prix et les dates relevés centre par centre :</p>
<ul class="posts">
{guides}
</ul>
{villes_block(spec["slug"])}
<h2 id="liste">La liste, {spec['liste_label']}</h2>
{chips(index)}

{body}

<h2 id="sources-officielles">Les listes officielles</h2>
<p>{src_links}. Ces listes évoluent : FEI ajoute et retire des centres au fil des agréments — la
nôtre est datée du {list_date} ; en cas de doute, la liste de FEI fait foi.</p>
"""
    toc = [("utiliser", "Avant de choisir un centre")] + ([("villes", "Les guides par ville")] if villes_block(spec["slug"]) else []) + \
          [("liste", f"La liste, {spec['liste_label']}")] + \
          [(i, t.split(" (")[0]) for i, t in index[:12]] + [("sources-officielles", "Les listes officielles")]
    a = {
        "section": "centres", "section_name": "Centres", "og_slug": "centres-" + spec["slug"],
        "slug": spec["slug"], "accent": spec["accent"], "crumb": spec["crumb"],
        "title": spec["title"], "desc": spec["desc"],
        "og_title": spec["title"], "og_desc": spec["desc"],
        "h1": spec["h1"],
        "published": DATE, "modified": spec.get("modified", DATE), "date_fr": spec.get("date_fr", DATE_FR), "read": max(4, n // 25),
        "intro": spec["intro"] % {"n": n, "so": so, "cities": ncity},
        "facts": spec["facts"],
        "toc": toc,
        "body": full_body,
        "cta_h2": spec.get("cta_h2", "Le centre vous donne la date ; le score, c'est vous"),
        "cta_p": spec.get("cta_p", """Une session se paie en entier et se repasse après un délai. Les examens blancs
de l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent le format officiel de chaque
déclinaison, avec la notation du vrai test et la correction IA de l'écrit et de l'oral — pour ne
réserver que la session utile."""),
        "faq": spec["faq"],
        "also": spec["also"],
        "sources": f"""<strong>Source.</strong> Liste des centres d'examen de France Éducation international,
{spec['sources_text']}, consultée le {list_date}. Les coordonnées sont celles publiées par FEI ; seules les
adresses e-mail génériques (contact, examens, certifications…) sont reprises. Signalez-nous une
erreur ou une fermeture : la liste est mise à jour à chaque nouvelle lecture de la source.""",
    }
    alts, links = langs_of(f"/centres/{spec['slug']}/")
    if alts:
        a["alternates"], a["lang_links"] = alts, links
    return a


def langs_of(fr_path):
    """hreflang et lien « Read in English » d'une page qui a une traduction /es/ ou /en/ (08/10/2026)."""
    from i18n_registry import alternates_for   # import tardif : le registre lit les configs traduites
    return alternates_for(fr_path)


def pays_pointers(*countries):
    """Renvois vers les pages pays TCF (make_pays.py, 08/10/2026) : {pays: (url, titre, résumé)}."""
    from pays_config import PAGES as PAYS
    out = {}
    for p in PAYS:
        d = load(p["file"])
        if p["exam"] == "tcf" and d["country"] in countries:
            out[d["country"]] = (f"/centres/{p['slug']}/", esc(p["title"].replace("{n}", str(len(d["centres"])))), p["pointer"])
    assert len(out) == len(countries), (countries, list(out))
    return out


# ---------------------------------------------------------------------------
# Les pages
# ---------------------------------------------------------------------------
G_TCF_FR = [("/blog/ou-passer-le-tcf-irn-en-france/", "Où passer le TCF IRN en France ?", "Les centres relevés à Paris et en région, 140 à 220 €, papier ou ordinateur."),
            ("/blog/ou-passer-le-tcf-canada-en-france/", "Où passer le TCF Canada en France ?", "Les centres qui le proposent, 195 à 285 €, leurs sessions mensuelles.")]
PAGES = [
    dict(slug="tcf-france", files=["tcf_france"], layout="france", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF en France",
         modified="2026-10-26", date_fr="26 octobre 2026", list_date_fr="26 octobre 2026",   # liste FEI relue le 26/10/2026
         title="Centres TCF agréés en France : liste, adresses, téléphones",
         desc="Les 247 centres TCF agréés par France Éducation international, région par région, avec adresse, téléphone, e-mail et site — liste du 26 octobre 2026.",
         h1="Centres TCF agréés en France : la liste des 247 centres, région par région",
         intro="""France Éducation international agrée <strong>%(n)d centres de passation du TCF</strong> en
France au 26 octobre 2026 — Alliances françaises, écoles de langue, GRETA, organismes de
formation, universités —, dont <strong>%(so)d proposent des sessions sur ordinateur</strong>, dans
<strong>%(cities)d villes</strong>. Voici la liste complète, région par région et ville par ville, avec
l'adresse, le téléphone, l'e-mail et le site de chaque centre, telle que FEI la publie. Vérifiez
ensuite sur le site du centre qu'il organise bien la déclinaison qu'il vous faut : IRN, Canada,
Québec ou tout public.""",
         facts=["<strong>{n} centres agréés</strong> en France, liste FEI du 26 octobre 2026 — {so} avec des sessions sur ordinateur.",
                "<strong>Île-de-France : {idf} centres</strong>, dont {paris} dans Paris ; Auvergne-Rhône-Alpes {ara} ; Occitanie {occ} ; Provence-Alpes-Côte d'Azur {paca}.",
                "La liste dit qu'un centre est agréé TCF, <strong>pas quelle déclinaison</strong> il organise : IRN, Canada, Québec, tout public — à vérifier sur son site.",
                "Adresse, téléphone, e-mail générique et site : les coordonnées publiées par FEI, reprises telles quelles.",
                "Prix libre : de 140 à 220 € pour un TCF IRN, de 195 à 285 € pour un TCF Canada sur les centres relevés — voir nos guides.",
                "Un organisme absent de cette liste ne peut pas vous délivrer d'attestation TCF."],
         stat4=("13", "régions + outre-mer", "index ci-dessous"), cities_note="de Paris à Mayotte",
         liste_label="région par région", decl="IRN, Canada, Québec, tout public, DAP",
         guides=G_TCF_FR + [("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF en France", FEI_LISTE % (73, "tcf")), ("Carte des centres TCF", FEI_CARTE % "tcf")],
         sources_text="filtre « France », type « TCF »",
         faq=[("Combien de centres TCF y a-t-il en France ?", "247 centres de passation agréés par France Éducation international au 26 octobre 2026, dont 129 proposent des sessions sur ordinateur. L'Île-de-France en compte 31, dont sept dans Paris ; Auvergne-Rhône-Alpes et Occitanie 32 chacune."),
              ("Comment savoir si un centre propose le TCF Canada ou le TCF IRN ?", "La liste officielle ne le précise pas : chaque centre choisit les déclinaisons qu'il organise. Ouvrez la page TCF du centre ou appelez-le. Nos guides « Où passer le TCF IRN en France » et « Où passer le TCF Canada en France » l'ont vérifié pour les principaux centres, avec leurs prix et leurs dates."),
              ("Comment s'inscrire au TCF ?", "Directement auprès du centre — en ligne dans la plupart des cas, avec une pièce d'identité et un paiement par carte. France Éducation international n'inscrit aucun candidat. Les sessions sont hebdomadaires à Paris pour le TCF IRN, mensuelles pour le TCF Canada."),
              ("Cette liste est-elle à jour ?", "Elle reproduit la liste de France Éducation international lue le 26 octobre 2026. FEI agrée et retire des centres au fil de l'année ; en cas de doute, sa liste en ligne fait foi. Les coordonnées reprises sont celles publiées par FEI."),
              ("Un centre TCF fait-il aussi passer le DELF ou l'examen civique ?", "Pas forcément : ce sont trois agréments distincts. Nos listes des centres DELF-DALF et des centres d'examen civique en France permettent de vérifier, centre par centre.")],
         also=[("/centres/delf-france/", "Centres DELF-DALF en France", "Les 143 centres d'examen agréés, région par région."),
               ("/centres/examen-civique-france/", "Centres d'examen civique en France", "Les 245 centres agréés par FEI pour l'examen civique."),
               ("/tcf-irn/", "TCF IRN : le test de français pour votre naturalisation", "Format, niveaux exigés depuis 2026, échelle sur 499."),
               ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", "Les quatre épreuves et la conversion NCLC.")]),
    dict(slug="delf-france", files=["delf_france"], layout="france", exam="DELF", accent="accent-delf",
         crumb="Centres DELF-DALF en France",
         title="Centres DELF-DALF en France : liste, adresses, téléphones",
         desc="Les 143 centres d'examen DELF-DALF agréés en France, région par région, avec adresse, téléphone, e-mail et site — liste FEI du 19 septembre 2026.",
         h1="Centres d'examen DELF-DALF en France : la liste des 143 centres agréés",
         intro="""Le DELF et le DALF se passent dans l'un des <strong>%(n)d centres d'examen agréés</strong> par
France Éducation international en France au 19 septembre 2026 — universités, Alliances françaises,
GRETA, écoles de langue —, répartis dans <strong>%(cities)d villes</strong>. Chaque centre choisit les
sessions qu'il ouvre parmi les dix du calendrier national, fixe son tarif et prend les inscriptions.
Voici la liste complète, région par région, avec les coordonnées publiées par FEI.""",
         facts=["<strong>{n} centres agréés</strong> en France, liste FEI du 19 septembre 2026, dont {paris} à Paris et {lyon} à Lyon — 144 entrées chez FEI, un centre y figurant deux fois.",
                "<strong>10 sessions nationales par an</strong> (jamais en avril ni en septembre) ; chaque centre n'en ouvre qu'une partie.",
                "Prix libre : <strong>DELF B2 de 125 € à 280 €</strong> selon le centre, sur ceux relevés le 17 septembre 2026.",
                "L'inscription ferme quatre à dix semaines avant l'écrit, parfois sur deux jours : lisez le calendrier du centre, pas le calendrier national.",
                "Le diplôme est valable à vie ; résultats en quatre à six semaines.",
                "Un organisme absent de cette liste ne peut pas vous faire passer le DELF."],
         stat4=("10", "sessions par an", "calendrier national FEI"), cities_note="universités et Alliances",
         liste_label="région par région", decl="tout public, junior, scolaire, Prim, DALF",
         guides=[("/blog/ou-passer-le-delf-en-france/", "Où passer le DELF en France ? Centres, dates, inscription", "Le calendrier 2026-2027, les 7 centres parisiens, les prix relevés et les fenêtres d'inscription."),
                 ("/delf-b2/", "DELF B2 : format, notation et préparation", "Les quatre épreuves, le seuil de 50 sur 100, la note éliminatoire."),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres DELF-DALF en France", FEI_LISTE % (73, "delf_dalf")), ("Carte des centres DELF-DALF", FEI_CARTE % "delf_dalf"), ("Calendriers des sessions", "https://www.france-education-international.fr/article/informations-pratiques-pour-les-candidats-au-delf-dalf")],
         sources_text="filtre « France », type « DELF / DALF »",
         faq=[("Combien de centres DELF-DALF y a-t-il en France ?", "143 centres d'examen agréés par France Éducation international au 19 septembre 2026 — 144 entrées dans la liste de FEI, un centre y figurant deux fois — : sept à Paris, sept à Lyon, cinq à Toulouse, trois à Marseille, Bordeaux et Strasbourg, et un centre dans la plupart des préfectures."),
              ("Quand ont lieu les sessions du DELF ?", "Dix fois par an selon le calendrier national de FEI — en 2026, il reste les 6-8 octobre, 3-5 novembre et 1-3 décembre —, mais chaque centre n'ouvre qu'une partie de ces sessions et ferme ses inscriptions quatre à dix semaines avant l'écrit. Le calendrier du centre fait foi."),
              ("Combien coûte le DELF ?", "Il n'y a pas de tarif national. Sur les centres relevés le 17 septembre 2026, le DELF B2 va de 125 € (Nantes Université) à 280 € (Alliance française de Paris), le B1 de 125 à 230 €. Les universités sont presque toujours les moins chères."),
              ("Cette liste inclut-elle le DELF junior et scolaire ?", "Oui : la liste de FEI regroupe tous les centres d'examen DELF-DALF, quelle que soit la déclinaison. Un adulte passe le DELF tout public ; les centres de l'académie (CASNAV) sont orientés DELF scolaire."),
              ("Un centre DELF fait-il aussi passer le TCF ?", "Pas forcément : ce sont deux agréments distincts. Notre liste des centres TCF en France permet de vérifier.")],
         also=[("/centres/tcf-france/", "Centres TCF en France", "Les 247 centres de passation agréés, région par région."),
               ("/blog/diplome-ou-test-delf-tcf/", "Diplôme ou test : lequel vous faut-il ?", "Un diplôme s'obtient à vie et peut se rater ; un test vous situe pour deux ans."),
               ("/delf-b1/", "DELF B1 : format, notation et préparation", "Le niveau exigé pour la carte de résident."),
               ("/dalf/", "DALF C1 · C2", "Les diplômes avancés, mêmes centres, même calendrier.")]),
    dict(slug="examen-civique-france", files=["civique_france"], layout="france", exam="Examen civique", accent="accent-irn",
         crumb="Centres d'examen civique en France",
         title="Centres d'examen civique en France : la liste FEI, contacts",
         desc="Les 245 centres agréés par FEI pour l'examen civique, région par région, avec adresse, téléphone et site — liste du 19 septembre 2026 — et le réseau CCIP.",
         h1="Centres d'examen civique en France : la liste des 245 centres agréés par FEI",
         intro="""L'examen civique — obligatoire depuis le 1<sup>er</sup> janvier 2026 pour une première carte de séjour
pluriannuelle, une première carte de résident et la naturalisation — se passe dans un centre agréé par
l'un des deux organismes habilités. Voici la liste des <strong>%(n)d centres du réseau France Éducation
international</strong> au 19 septembre 2026, dans <strong>%(cities)d villes</strong>, avec leurs
coordonnées ; le second réseau, celui de la CCI Paris Île-de-France, se consulte session par session
dans son outil « Trouver une session ».""",
         facts=["<strong>{n} centres FEI</strong> en France, liste du 19 septembre 2026, dans {deps} départements — {paris} à Paris, {idf} en Île-de-France, {ara} en Auvergne-Rhône-Alpes.",
                "<strong>Deux réseaux agréés</strong> : France Éducation international (cette liste, pré-inscription sur test-civique.fr) et la CCI Paris Île-de-France (outil « Trouver une session »).",
                "<strong>40 questions</strong>, 45 minutes, 32 bonnes réponses ; trois mentions (carte pluriannuelle, carte de résident, naturalisation).",
                "Prix libre : <strong>70 à 110 €</strong> sur les centres relevés ; résultats souvent sous 12 heures ; attestation sans durée de validité.",
                "La préparation officielle est gratuite (formation-civique.interieur.gouv.fr).",
                "Un centre TCF n'est pas automatiquement centre d'examen civique : cette liste fait foi pour le réseau FEI."],
         stat4=("2", "réseaux agréés", "FEI et CCI Paris IdF"), cities_note="dans 94 départements",
         liste_label="région par région", decl="mention carte de séjour pluriannuelle, carte de résident ou naturalisation",
         guides=[("/blog/ou-passer-l-examen-civique/", "Où passer l'examen civique ? Centres et inscription 2026", "Les deux réseaux, la pré-inscription sur test-civique.fr, les prix relevés, les centres CCIP de Paris."),
                 ("/blog/naturalisation-2026-niveau-b2/", "Naturalisation 2026 : le niveau B2 est devenu obligatoire", ""),
                 ("/blog/carte-de-resident-b1-2026/", "Carte de résident : le B1 exigé depuis janvier 2026", "")],
         sources_links=[("Liste des centres d'examen civique (FEI)", FEI_LISTE % (73, "examen_civique")), ("Carte des centres", FEI_CARTE % "examen_civique"), ("Pré-inscription test-civique.fr", "https://test-civique.fr/inscription"), ("Outil « Trouver une session » de la CCIP", "https://francais.cci-paris-idf.fr/candidat?produit=21")],
         sources_text="filtre « France », type « Examen civique »",
         cta_h2="Le civique se prépare gratuitement ; le B2, lui, se travaille",
         cta_p="""L'examen civique a ses questions publiées ; le test de français qui l'accompagne, non. Les
examens blancs de l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent le TCF IRN, le TEF
IRN et le DELF au format officiel, avec la correction IA de l'écrit et de l'oral.""",
         faq=[("Où passer l'examen civique près de chez moi ?", "Dans l'un des 245 centres du réseau France Éducation international listés ici — il y en a dans 94 départements —, ou dans un centre du réseau de la CCI Paris Île-de-France, à chercher dans son outil « Trouver une session ». Pour un centre FEI, la pré-inscription se fait sur test-civique.fr."),
              ("Comment s'inscrire ?", "Réseau FEI : formulaire de pré-inscription test-civique.fr (département, ville, centre, mention, numéro étranger AGDREF), puis le centre propose une date et encaisse. Réseau CCIP : outil « Trouver une session » sur francais.cci-paris-idf.fr, puis inscription auprès du centre."),
              ("Combien coûte l'examen civique ?", "Aucun texte ne fixe de tarif. Relevés le 17 septembre 2026 : 70 € à Espaces Formation (Nantes), 75 € à l'Alliance française de Montpellier, 80 à 90 € chez Etoile Institut (Paris), 110 € chez ACCORD (Paris)."),
              ("Quelle mention passer ?", "Celle de votre démarche : carte de séjour pluriannuelle, carte de résident ou naturalisation. La mention carte de résident vaut pour la carte pluriannuelle, pas l'inverse ; aucune des deux ne vaut pour la naturalisation."),
              ("Peut-on le passer à l'étranger ?", "Oui, dans les Instituts français, les Alliances françaises et auprès des consulats — l'Institut français d'Algérie l'organise à Alger pour 9 000 dinars. La carte de FEI se filtre par pays.")],
         also=[("/centres/tcf-france/", "Centres TCF en France", "Les 247 centres agréés, pour le test de français qui accompagne l'examen civique."),
               ("/blog/ou-passer-le-tcf-irn-en-france/", "Où passer le TCF IRN en France ?", "Sept centres à Paris, des sessions chaque semaine, 140 à 220 €."),
               ("/tcf-irn/", "TCF IRN : le test de français pour votre naturalisation", "Format, niveaux exigés, échelle sur 499."),
               ("/blog/b1-ou-b2-nationalite-francaise/", "B1 ou B2 pour la nationalité française ?", "Le tableau des trois démarches.")]),
    dict(slug="tcf-canada", files=["tcf_canada"], layout="canada", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF au Canada",
         modified="2026-10-26", date_fr="26 octobre 2026", list_date_fr="26 octobre 2026",   # liste FEI relue le 26/10/2026
         title="Centres TCF au Canada : les 48 centres agréés, par province",
         desc="Les 48 centres TCF agréés au Canada — Montréal, Toronto, Vancouver, Ottawa… — par province, avec adresse, téléphone, e-mail et site. Liste FEI 2026.",
         h1="Centres TCF au Canada : les 48 centres agréés, province par province",
         intro="""Au Canada, le TCF Canada et le TCF Québec se passent dans l'un des <strong>48 centres agréés</strong>
par France Éducation international (49 entrées dans sa liste du 26 octobre 2026, un centre apparaissant
deux fois) — Alliances françaises, universités, cégeps, centres de formation —, présents dans
<strong>neuf provinces et au Nunavut</strong>, %(so)d avec des sessions sur ordinateur. Voici la liste
par province et par ville, avec les coordonnées publiées par FEI, et les règles d'inscription relevées
sur les principaux centres.""",
         facts=["<strong>48 centres agréés</strong> (49 entrées FEI, Gaspé en double), liste du 26 octobre 2026 : 23 au Québec dont 7 à Montréal, 8 en Ontario, 5 en Colombie-Britannique, 3 en Alberta.",
                "<strong>45 entrées avec sessions sur ordinateur</strong> ; papier seulement à Sherbrooke, Lethbridge, Windsor (Collège Boréal) et à l'Université de Victoria.",
                "Prix libre et souvent non publié : 390 $ (AF Vancouver), 400 $ (AF Edmonton), 440 $ (UQTR) ; rien d'affiché à l'AF Montréal.",
                "⚠️ Les sessions de Toronto et Vancouver affichent <strong>complet en quelques minutes</strong> : inscrivez-vous à l'ouverture, pas à la date d'examen.",
                "<strong>20 jours</strong> entre deux passations, « quel que soit le centre » ; résultats en 2 à 4 semaines.",
                "Aucun centre à l'Île-du-Prince-Édouard, au Yukon ni aux Territoires du Nord-Ouest."],
         stat4=("9 + 1", "provinces + Nunavut", "aucun à l'Î.-P.-É."), cities_note="de Montréal à Iqaluit",
         liste_label="province par province", decl="Canada, Québec, tout public, IRN",
         guides=[("/blog/ou-passer-le-tcf-canada-au-canada/", "Où passer le TCF Canada au Canada ? Centres et inscription", "Prix relevés, sessions trimestrielles, la méthode pour décrocher une place, règles d'annulation."),
                 ("/tcf-quebec/", "TCF Québec : le test modulaire", "Mêmes centres, un autre usage."),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF au Canada", FEI_LISTE % (112, "tcf")), ("Carte des centres TCF", FEI_CARTE % "tcf")],
         sources_text="filtre « Canada », type « TCF »",
         faq=[("Où passer le TCF Canada à Montréal ?", "Dans l'un des sept centres agréés de Montréal — Alliance Française de Montréal, Collège Stanislas, UQAM, Université Concordia, Cégep Marie-Victorin, Centre Yves-Thériault, Collège ELC — ou en banlieue à Laval, Kirkland et Saint-Constant. Tous proposent des sessions sur ordinateur."),
              ("Où passer le TCF Canada à Toronto ?", "À l'Alliance française de Toronto (campus Spadina, North York, Mississauga, Oakville) ou au GB Language Centre de North York. Les sessions de l'Alliance sont trimestrielles, avec une inscription qui ouvre un mois avant à 10 h et se remplit en minutes."),
              ("Combien coûte le TCF Canada au Canada ?", "Aucun tarif national, et beaucoup de centres ne publient rien : 390 $ à l'Alliance française de Vancouver, 400 $ à Edmonton, 440 $ à l'UQTR sur les centres relevés ; l'Alliance Française de Montréal n'affiche aucun prix."),
              ("Tous ces centres proposent-ils le TCF Canada et le TCF Québec ?", "La plupart proposent les deux, mais la liste de FEI ne le précise pas : vérifiez la case cochée à l'inscription — le TCF Québec, modulaire, n'est pas accepté par IRCC."),
              ("Quels documents le jour de l'examen ?", "Passeport valide et convocation imprimée, sans exception à Ottawa ; l'identité est contrôlée pendant toute l'épreuve. Sur ordinateur, le clavier QWERTY est fourni par le centre.")],
         also=[("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", "Les quatre épreuves, la conversion NCLC, les seuils pour Entrée express."),
               ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", "458 en compréhension orale, 453 à l'écrit."),
               ("/centres/tcf-france/", "Centres TCF en France", "Les 247 centres agréés, pour un TCF Canada passé depuis la France."),
               ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", "Les deux tables NCLC et le comparatif de format.")]),
    dict(slug="tcf-algerie", files=["tcf_algerie"], layout="cities", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF en Algérie",
         title="TCF Algérie 2026 : 5 centres, 37 500 DA, rendez-vous IFAL",
         desc="Les 5 centres TCF d'Algérie — Institut français d'Alger, Oran, Constantine, Annaba, Tlemcen —, leurs contacts, les tarifs 2026 (Canada 37 500 DA), IFAL.",
         modified="2026-10-17", date_fr="17 octobre 2026",
         h1="Centres TCF en Algérie : les 5 antennes agréées et leurs contacts",
         intro="""En Algérie, le TCF — Canada, Québec, IRN, tout public ou DAP — se passe uniquement dans les
<strong>cinq antennes de l'Institut français d'Algérie</strong> : Alger (Hydra), Oran, Constantine,
Annaba et Tlemcen, seuls centres agréés par France Éducation international au 19 septembre 2026, tous
avec des sessions sur ordinateur. L'inscription se fait exclusivement en ligne, sur la plateforme IFAL
opérée par VFS Global, et le TCF Canada coûte <strong>37 500 DA</strong> (tarif affiché par les antennes le
17 octobre 2026). Voici les coordonnées officielles des cinq antennes — et le rappel du faux site qui
imite l'Institut.""",
         facts=["<strong>5 centres agréés</strong>, tous des antennes de l'Institut français d'Algérie ; aucune école privée n'est agréée.",
                "Inscription <strong>en ligne uniquement</strong> sur la plateforme IFAL (forms.vfsglobal.com.dz/IFAL), depuis la page TCF de <strong>if-algerie.com</strong>.",
                "Sessions <strong>chaque mois</strong> sur les cinq antennes ; <strong>26 jours</strong> entre deux inscriptions selon la page nationale, <strong>36</strong> selon les pages d'Oran, Constantine, Annaba et Tlemcen.",
                "Pièce d'identité : carte biométrique ou passeport (Algériens), passeport biométrique ou carte consulaire (autres) ; jamais le permis de conduire.",
                "Tarifs des antennes (17 octobre 2026) : <strong>TCF Canada et TCF Québec 37 500 DA</strong>, TCF DAP 19 500 DA, TCF tout public 13 000 DA ; attestation par e-mail, aucune version papier depuis mars 2023.",
                "⚠️ <strong>if-algerie.fr est une escroquerie</strong> ; le site officiel est if-algerie.com."],
         stat4=("IFAL", "plateforme d'inscription", "opérée par VFS Global"), cities_note="Alger, Oran, Constantine, Annaba, Tlemcen",
         liste_label="ville par ville", decl="Canada, Québec, IRN, tout public, DAP",
         guides=[("/blog/ifal-tcf-rendez-vous/", "IFAL TCF : prendre rendez-vous sur la plateforme VFS", "Les étapes, la déclinaison à choisir, les tarifs, les lieux de passation, l'assistance VFS."),
                 ("/blog/tcf-canada-algerie/", "TCF Canada en Algérie : où le passer, comment s'inscrire", "Les cinq antennes, 37 500 DA, les résultats, le faux site à éviter."),
                 ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", ""),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF en Algérie", FEI_LISTE % (115, "tcf")), ("Page TCF de l'Institut français d'Algérie (relue le 17 octobre 2026)", "https://www.if-algerie.com/tests-et-examens/tcf")],
         sources_text="filtre « Algérie », type « TCF », et site de l'Institut français d'Algérie",
         faq=[("Où passer le TCF Canada en Algérie ?", "Dans l'une des cinq antennes de l'Institut français d'Algérie — Alger (Hydra), Oran, Constantine, Annaba, Tlemcen —, seuls centres agréés par France Éducation international dans le pays. Toutes proposent des sessions sur ordinateur."),
              ("Comment s'inscrire ?", "Exclusivement en ligne, sur la plateforme IFAL opérée par VFS Global, accessible depuis la page TCF du site officiel if-algerie.com : compte, choix de la déclinaison, de l'antenne et de la session, paiement en ligne. Aucune inscription sur place."),
              ("Combien coûte le TCF en Algérie ?", "37 500 dinars pour le TCF Canada et le TCF Québec, 19 500 pour le TCF DAP, 13 000 pour le TCF tout public : ce sont les tarifs TTC affichés par les antennes de l'Institut français le 17 octobre 2026, payés en ligne sur la plateforme IFAL. Les montants de 70 000 à 100 000 dinars qui circulent sont ceux d'un site frauduleux."),
              ("Quel est le site officiel ?", "if-algerie.com. Le site if-algerie.fr, qui imite l'Institut et propose un « candidat partenaire » pour passer l'examen à votre place, est une escroquerie."),
              ("Peut-on aussi passer l'examen civique français en Algérie ?", "Oui, à l'Institut français d'Alger (30, rue des Frères-Kadri, Hydra), avec une pré-inscription sur test-civique.fr et un paiement de 9 000 dinars sur place ou par virement.")],
         also=[("/blog/tcf-canada-algerie/", "TCF Canada en Algérie : où le passer, comment s'inscrire", "Le guide complet, avec le faux site à éviter."),
               ("/blog/ifal-tcf-rendez-vous/", "IFAL TCF : prendre rendez-vous sur la plateforme VFS", "Les étapes et l'assistance VFS."),
               ("/centres/tcf-maroc/", "Centres TCF au Maroc", "Les 16 centres agréés, avec leurs contacts."),
               ("/centres/tcf-tunisie/", "Centres TCF en Tunisie", "Les 14 centres agréés, avec leurs contacts."),
               ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", "")]),
    dict(slug="tcf-maroc", files=["tcf_maroc"], layout="cities", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF au Maroc",
         title="TCF Maroc 2026 : 16 centres, 2 900 Dhs, dates et inscription",
         desc="Les 16 centres TCF agréés au Maroc — Instituts français de Casablanca, Rabat, Fès, Tanger, Agadir… —, le TCF Canada à 2 900 Dhs, les dates oct.-déc. 2026.",
         modified="2026-10-17", date_fr="17 octobre 2026",
         h1="Centres TCF au Maroc : les 16 centres agréés et leurs contacts",
         intro="""Au Maroc, le TCF se passe dans les <strong>%(n)d centres agréés</strong> par France Éducation
international au 19 septembre 2026 : quatorze sites de l'Institut français du Maroc — de Tanger à
Agadir — et les Alliances françaises de Safi et de Ouarzazate, %(so)d avec des sessions sur ordinateur.
Le tarif est national (2 900 dirhams pour le TCF Canada, 1 900 pour l'IRN et le tout public) et
l'inscription se fait en ligne, sur le site de l'Institut de votre ville. Voici les coordonnées de
chaque centre.""",
         facts=["<strong>16 centres agréés</strong> : 14 Instituts français (dont Béni Mellal et Nador, rattachés à Casablanca et Oujda) et 2 Alliances françaises (Safi, Ouarzazate).",
                "Tarif national : <strong>TCF Canada, Québec et TEF Canada 2 900 Dhs</strong> ; TCF IRN et tout public 1 900 Dhs (relu le 17 octobre 2026).",
                "Inscription <strong>en ligne, sur le site de l'Institut de votre ville</strong> (panier) ; le TCF IRN s'inscrit sur place uniquement.",
                "Le 17 octobre 2026, <strong>douze villes</strong> affichaient des sessions de TCF Canada jusqu'en décembre : 13 dates ouvertes à Kénitra, 8 à Rabat et à El Jadida, 7 à Casablanca ; aucune à Safi.",
                "<strong>20 jours</strong> de carence entre deux TCF ; aucun remboursement ; report sur justificatif facturé 500 Dhs.",
                "Un organisme absent de cette liste n'est pas agréé : pas d'« agent », pas de revendeur."],
         stat4=("2 900 Dhs", "TCF Canada", "tarif national IFM"), cities_note="de Tanger à Agadir",
         liste_label="ville par ville", decl="Canada, Québec, IRN, tout public, DAP",
         guides=[("/blog/tcf-canada-maroc/", "TCF Canada au Maroc : les 16 centres et l'inscription", "L'inscription en ligne pas à pas, les sessions d'octobre à décembre 2026 ville par ville, les règles de report."),
                 ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", ""),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF au Maroc", FEI_LISTE % (117, "tcf")), ("Institut français du Maroc — TCF Canada", "https://if-maroc.org/certifications/tcf-canada/")],
         sources_text="filtre « Maroc », type « TCF », et site de l'Institut français du Maroc",
         faq=[("Où passer le TCF Canada au Maroc ?", "Dans l'un des seize centres agréés : les Instituts français d'Agadir, Béni Mellal, Casablanca, El Jadida, Essaouira, Fès, Kénitra, Marrakech, Meknès, Nador, Oujda, Rabat, Tanger et Tétouan, et les Alliances françaises de Safi et de Ouarzazate."),
              ("Combien coûte le TCF au Maroc ?", "2 900 dirhams pour le TCF Canada, le TCF Québec et le TEF Canada ; 1 900 dirhams pour le TCF IRN et le TCF tout public — tarif de l'Institut français du Maroc, affiché dans les douze villes qui listaient des sessions le 17 octobre 2026."),
              ("Comment s'inscrire ?", "En ligne, sur le site de l'Institut français de votre ville (if-maroc.org/casablanca, /rabat…), page TCF Canada : choix de la session, panier, paiement. Pièce d'identité et photo demandées ; convocation remise dès l'inscription. Le TCF IRN s'inscrit à l'accueil."),
              ("À quelle fréquence ont lieu les sessions ?", "Cela dépend du site. Le 17 octobre 2026 : treize dates ouvertes à Kénitra d'ici le 18 décembre, huit à Rabat et à El Jadida, sept à Casablanca (plus deux à Béni Mellal), quatre à Fès, trois à Tanger, Meknès, Tétouan et Agadir, deux à Essaouira, une à Marrakech (12 novembre) et à Oujda (10 novembre) ; aucune à Safi."),
              ("Peut-on se faire rembourser ?", "Non : « le candidat ne pourra, en aucun cas, être remboursé ». Un report est possible sur justificatif (maladie, décès, accident, examen officiel) envoyé sous 5 jours ouvrés, facturé 500 dirhams.")],
         also=[("/blog/tcf-canada-maroc/", "TCF Canada au Maroc : les 16 centres et l'inscription", "Le guide complet."),
               ("/centres/tcf-algerie/", "Centres TCF en Algérie", "Les cinq antennes de l'Institut français."),
               ("/centres/tcf-tunisie/", "Centres TCF en Tunisie", "Les 14 centres agréés."),
               ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", "")]),
    dict(slug="tcf-tunisie", files=["tcf_tunisie"], layout="cities", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF en Tunisie",
         title="TCF Tunisie 2026 : 14 centres, 880 DT, dates et inscription",
         desc="Les 14 centres TCF agréés en Tunisie — Institut français de Tunis, Sousse, Sfax, Nabeul, Béja, Kébili, 6 Alliances —, le TCF Canada à 880 DT, les dates.",
         modified="2026-10-17", date_fr="17 octobre 2026",
         h1="Centres TCF en Tunisie : les 14 centres agréés et leurs contacts",
         intro="""En Tunisie, le TCF se passe dans les <strong>%(n)d centres agréés</strong> par France Éducation
international au 19 septembre 2026 : les pôles de l'Institut français de Tunisie — Tunis, El Mourouj,
Nabeul-Hammamet, Béja, Sousse, Sfax, Kébili, Médenine — et six Alliances françaises (Tunis-Ariana,
Bizerte, Djerba, Gabès, Gafsa, Kairouan), tous avec des sessions sur ordinateur. À l'Institut, le TCF
Canada coûte 880 dinars et se réserve en ligne avant une inscription sur place. Voici les coordonnées
de chaque centre.""",
         facts=["<strong>14 centres agréés</strong> : 8 pôles de l'Institut français de Tunisie et 6 Alliances françaises, tous avec des sessions sur ordinateur.",
                "À l'Institut : <strong>TCF Canada et TCF Québec 880 DT</strong>, TCF IRN 625 DT, TCF tout public 335 DT + 220 DT par expression (17 octobre 2026).",
                "Procédure en deux temps : <strong>rendez-vous en ligne</strong>, puis <strong>inscription et paiement sur place</strong> le jour fixé — un mandataire muni d'une copie de votre carte d'identité peut y aller.",
                "Une session par mois par pôle — prochains tests ouverts le 17 octobre 2026 : Tunis 26-27 nov., Sousse 18 et 20 nov., El Mourouj 19 et 26 nov., Béja 26 nov., Nabeul-Hammamet et Sfax 27 nov. ; résultats <strong>5 semaines</strong> après ; <strong>30 jours</strong> entre deux sessions.",
                "Paiement en espèces (carte bancaire à Tunis seulement) ; chèques suspendus ; frais non remboursables.",
                "Le TCF Canada est proposé dans sept pôles de l'Institut ; Médenine n'apparaît que pour le tout public."],
         stat4=("880 DT", "TCF Canada à l'Institut", "5 semaines de résultats"), cities_note="de Bizerte à Médenine",
         liste_label="ville par ville", decl="Canada, Québec, IRN, tout public",
         guides=[("/blog/tcf-canada-tunisie/", "TCF Canada en Tunisie : centres, calendrier, inscription", "Le calendrier d'octobre à décembre pôle par pôle, la procédure rendez-vous puis inscription, les frais, les délais."),
                 ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", ""),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF en Tunisie", FEI_LISTE % (118, "tcf")), ("Institut français de Tunisie — TCF Canada", "https://www.institutfrancais-tunisie.com/examens/tcf-canada/")],
         sources_text="filtre « Tunisie », type « TCF », et site de l'Institut français de Tunisie",
         faq=[("Où passer le TCF Canada en Tunisie ?", "À l'Institut français de Tunisie — pôles de Tunis, El Mourouj, Nabeul-Hammamet, Béja, Sousse, Sfax et Kébili — ou dans une Alliance française (Tunis-Ariana, Bizerte, Djerba, Gabès, Gafsa, Kairouan). Quatorze centres agréés au total."),
              ("Combien coûte le TCF en Tunisie ?", "À l'Institut français, 880 dinars pour le TCF Canada et le TCF Québec, 625 dinars pour le TCF IRN, 335 dinars pour les épreuves obligatoires du TCF tout public sur ordinateur (17 octobre 2026). Les Alliances ne publient pas de tarif lisible en ligne."),
              ("Comment s'inscrire à l'Institut français ?", "Un rendez-vous en ligne pendant la fenêtre ouverte pour la session, puis l'inscription et le paiement sur place au pôle choisi, le jour fixé — en espèces, ou par carte à Tunis. Le candidat peut se faire représenter."),
              ("Combien de temps pour les résultats ?", "Cinq semaines après la passation, indique l'Institut — le délai le plus long que nous ayons relevé. L'attestation vaut ensuite deux ans."),
              ("Quel délai pour repasser le test ?", "Trente jours entre deux sessions de TCF ou de TEF, selon l'Institut ; avec des résultats à cinq semaines et une session par mois, une seconde tentative prend deux à trois mois.")],
         also=[("/blog/tcf-canada-tunisie/", "TCF Canada en Tunisie : centres, calendrier, inscription", "Le guide complet."),
               ("/centres/tcf-maroc/", "Centres TCF au Maroc", "Les 16 centres agréés."),
               ("/centres/tcf-algerie/", "Centres TCF en Algérie", "Les cinq antennes de l'Institut français."),
               ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", "")]),
    dict(slug="tcf-afrique", files=["tcf_senegal", "tcf_cote_d_ivoire", "tcf_cameroun", "tcf_republique_democratique_du_congo", "tcf_congo", "tcf_benin", "tcf_togo", "tcf_guinee", "tcf_gabon", "tcf_mali", "tcf_mauritanie", "tcf_maurice"],
         layout="multi", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF en Afrique",
         modified="2026-10-26", date_fr="26 octobre 2026", list_date_fr="19 septembre et 26 octobre 2026",   # Sénégal relu le 26/10/2026
         title="Centres TCF en Afrique : Sénégal, Cameroun, Côte d'Ivoire…",
         desc="Les centres TCF agréés au Sénégal, en Côte d'Ivoire, au Cameroun, en RDC, au Congo, au Bénin, au Togo, en Guinée, au Gabon, au Mali, en Mauritanie, à Maurice.",
         h1="Centres TCF en Afrique subsaharienne et à Maurice : les centres agréés, pays par pays",
         intro="""Dans les pays francophones d'Afrique, le TCF — Canada, Québec, IRN ou tout public — se passe dans les
Instituts français et les Alliances françaises agréés par France Éducation international : <strong>%(n)d
centres dans douze pays</strong> au 26 octobre 2026, dont %(so)d avec des sessions sur ordinateur.
Le réseau est mince — un seul centre dans plusieurs pays —, ce qui rend la place plus précieuse
qu'ailleurs. Voici les coordonnées de chaque centre, pays par pays.""",
         facts=["<strong>23 centres dans 12 pays</strong> : Cameroun 7, Sénégal 3, RDC 3, Congo 2, et un seul centre en Côte d'Ivoire, au Bénin, au Togo, en Guinée, au Gabon, au Mali, en Mauritanie et à Maurice.",
                "Presque tous sont des <strong>Instituts français ou des Alliances françaises</strong> : l'inscription se fait sur leur site ou à leur accueil.",
                "Un seul centre par pays dans huit pays : les sessions se remplissent, réservez dès l'ouverture.",
                "Les tarifs se paient en monnaie locale et ne sont pas centralisés : demandez-les au centre.",
                "20 à 30 jours entre deux passations ; l'attestation vaut deux ans.",
                "Le TEF Canada relève d'un autre réseau (Le français des affaires), souvent les mêmes Instituts."],
         stat4=("12", "pays", "un seul centre dans 8 d'entre eux"), cities_note="de Dakar à Port-Louis",
         liste_label="pays par pays", decl="Canada, Québec, IRN, tout public, DAP",
         guides=[("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", "Les quatre épreuves, la conversion NCLC, les seuils pour Entrée express."),
                 ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", ""),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF par pays (FEI)", "https://www.france-education-international.fr/centres-d-examen/liste?type-centre=tcf"), ("Carte des centres TCF", FEI_CARTE % "tcf")],
         sources_text="type « TCF », filtres Sénégal, Côte d'Ivoire, Cameroun, République démocratique du Congo, Congo, Bénin, Togo, Guinée, Gabon, Mali, Mauritanie et Maurice",
         faq=[("Où passer le TCF Canada au Sénégal ?", "Dans l'un des trois centres agréés listés ci-dessous, dont l'Institut français de Dakar. Renseignez-vous auprès du centre pour les dates et le tarif, qui ne sont pas centralisés."),
              ("Où passer le TCF Canada au Cameroun ?", "Dans l'un des sept centres agréés — Instituts français et Alliances françaises — listés ci-dessous, à Yaoundé, Douala et en région."),
              ("Où passer le TCF Canada en Côte d'Ivoire ?", "Dans le seul centre agréé du pays au 26 octobre 2026, à Abidjan (Institut français) : les places y sont comptées, réservez dès l'ouverture des inscriptions."),
              ("Le TCF Canada passé en Afrique est-il accepté par IRCC ?", "Oui, dès lors qu'il est passé dans un centre agréé par France Éducation international : l'attestation est la même partout dans le monde et vaut deux ans."),
              ("Comment vérifier qu'un centre est agréé ?", "En le cherchant dans la liste officielle de FEI, par pays. Un organisme absent de cette liste ne peut pas délivrer d'attestation TCF, quel que soit son site.")],
         also=[("/centres/tcf-maroc/", "Centres TCF au Maroc", "Les 16 centres agréés."),
               ("/centres/tcf-algerie/", "Centres TCF en Algérie", "Les cinq antennes de l'Institut français."),
               ("/centres/tcf-tunisie/", "Centres TCF en Tunisie", "Les 14 centres agréés."),
               ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", "")]),
    # Europe (26/10/2026) : quatorze pays (l'Autriche et le Luxembourg ajoutés l'après-midi), chacun renvoyé à sa page pays ; listes FEI du 26 octobre 2026 (data/fei_monde/), sauf
    # l'Espagne et le Royaume-Uni, qui gardent le fichier de leur page (8 octobre) pour n'être comptés qu'une fois sur /centres/.
    dict(slug="tcf-europe", files=["tcf_espagne"] + ["fei_monde/tcf_" + f for f in ("italie", "allemagne", "suisse", "pays_bas", "portugal")]
         + ["tcf_royaume_uni"] + ["fei_monde/tcf_" + f for f in ("roumanie", "belgique", "pologne", "grece", "irlande", "autriche", "luxembourg")],
         layout="multi", exam="TCF", accent="accent-tcf",
         pointers=pays_pointers("Espagne", "Royaume-Uni", "Allemagne", "Suisse", "Belgique", "Italie", "Pays-Bas", "Portugal",
                                "Roumanie", "Pologne", "Grèce", "Irlande", "Autriche", "Luxembourg"),
         modified="2026-10-26", date_fr="26 octobre 2026", list_date_fr="8 et 26 octobre 2026",
         crumb="Centres TCF en Europe",
         title="Centres TCF en Europe : le TCF Canada pays par pays",
         desc="Les 78 centres TCF agréés dans 14 pays d'Europe — Espagne, Allemagne, Italie, Suisse, Belgique… — et qui propose le TCF Canada, à quel prix.",
         h1="Centres TCF en Europe : le TCF Canada pays par pays, les prix et les dates",
         intro="""Hors de France, en Europe, le TCF se passe dans les <strong>%(n)d centres agréés</strong> par France Éducation
international dans les quatorze pays de cette page — Instituts français, Alliances françaises, écoles,
universités —, dont %(so)d avec des sessions sur ordinateur. Chaque pays a sa page détaillée : qui propose le TCF Canada,
à quel prix, à quelles dates. Les tarifs relevés vont de 210 € (Gênes, Erlangen) à 295 € (Allemagne), CHF 290 en Suisse
et £325 à Glasgow. Pour Entrée express, demandez le TCF Canada ; pour la naturalisation française, le TCF IRN.""",
         facts=["<strong>{n} centres</strong> dans 14 pays : Espagne 14, Italie 14, Allemagne 13, Suisse 7, Pays-Bas 7, Portugal 6, Royaume-Uni 3, Roumanie 3, Belgique 2, Pologne 2, Grèce 2, Irlande 2, Luxembourg 2, Autriche 1 (listes FEI du 8 octobre 2026 pour l'Espagne et le Royaume-Uni, du 26 octobre pour les autres).",
                "TCF Canada : Espagne de 275 à 287 € ; Allemagne 295 € (210 € à Erlangen) ; Italie de 210 à 250 € ; Belgique 260 et 268 € ; Irlande 270 € ; Pays-Bas 290 € à Amsterdam ; Portugal 211 et 220 € ; Autriche 295 € à Vienne ; Suisse CHF 290 à Montreux ; Royaume-Uni £260 et £325.",
                "Un centre TCF ne fait pas forcément passer le TCF Canada : en Suisse, seuls ALPADIA (Montreux) et l'Alliance française de Zurich l'annoncent ; à Rome et à Francfort, le centre agréé ne le propose pas ; au Luxembourg, l'Institut national des langues ne fait passer que le tout public et l'IRN. La Suède n'a aucun centre TCF.",
                "⚠️ Places rares : Berlin (4 novembre) et Amsterdam (25 novembre 2026) étaient complets le 26 octobre ; à Londres, la première place libre était le 23 avril 2027 au relevé du 8 octobre.",
                "Le réseau français reste le plus dense d'Europe : <strong>247 centres</strong>, dont plusieurs près des frontières.",
                "Chaque centre choisit ses déclinaisons, ses dates et son tarif ; attestation valable deux ans. Un organisme absent de ces listes n'est pas agréé."],
         stat4=("14", "pays", "de l'Espagne à l'Autriche"), cities_note="de Lisbonne à Varsovie",
         liste_label="pays par pays", decl="Canada, Québec, IRN, tout public, DAP",
         guides=[("/centres/tcf-espagne/", "TCF Canada en Espagne : 11 centres, 281 à 287 €, dates", "Le relevé des 14 centres agréés : déclinaisons, prix, prochaines sessions."),
                 ("/centres/tcf-allemagne/", "TCF Canada en Allemagne : 10 centres, 295 €, dates", "Les Instituts français et leur module commun, 23 sessions jusqu'en 2027."),
                 ("/centres/tcf-italie/", "TCF Canada en Italie : 7 centres, 210 à 250 €, dates", "Turin, Gênes, Milan, Venise… et ceux qui ne le proposent pas."),
                 ("/centres/tcf-suisse/", "TCF Canada en Suisse : Montreux, Zurich, prix en CHF", "Swiss Exams et Fribourg : le tout public seulement."),
                 ("/centres/tcf-royaume-uni/", "TCF Canada à Londres et au Royaume-Uni", "L'Institut français de Londres et l'Alliance de Glasgow, leurs règles, les places."),
                 ("/centres/tcf-france/", "Centres TCF en France : les 247 centres agréés", "Pour les frontaliers, le réseau le plus dense.")],
         sources_links=[("Liste des centres TCF par pays (FEI)", "https://www.france-education-international.fr/centres-d-examen/liste?type-centre=tcf"), ("Carte des centres TCF", FEI_CARTE % "tcf")],
         sources_text="type « TCF », filtres Espagne, Italie, Allemagne, Suisse, Pays-Bas, Portugal, Royaume-Uni, Roumanie, Belgique, Pologne, Grèce, Irlande, Autriche et Luxembourg",
         faq=[("Où passer le TCF Canada en Europe ?", "Dans un centre agréé qui annonce la version Canada : en Espagne, 11 des 14 centres ; en Allemagne, 10 sur 13 ; en Italie, 7 sur 14 ; les deux centres belges et les deux irlandais ; les trois Alliances des Pays-Bas ; l'Institut français de Vienne ; en Suisse, ALPADIA à Montreux et l'Alliance française de Zurich. Chaque page pays les détaille."),
              ("Combien coûte le TCF Canada en Europe ?", "Aucun tarif commun : de 210 € (Gênes, Erlangen) à 295 € (Instituts français d'Allemagne), 290 € à Amsterdam, CHF 290 à Montreux, £260 à Londres et £325 à Glasgow, relevés les 8 et 26 octobre 2026."),
              ("Où passer le TCF en Allemagne ?", "Dans l'un des 13 centres agréés ; dix annoncent le TCF Canada, dont les Instituts français de Berlin, Hambourg, Munich, Stuttgart, Mayence et Brême, à 295 €, sur un module d'inscription commun."),
              ("Où passer le TCF en Suisse ?", "Dans l'un des sept centres agréés : Swiss Exams à Berne, Genève, Lausanne et Winterthur et l'Université de Fribourg font passer le TCF tout public ; ALPADIA à Montreux et l'Alliance française de Zurich annoncent aussi le TCF Canada."),
              ("Le TCF IRN passé à l'étranger est-il accepté pour la naturalisation française ?", "Oui : l'attestation est délivrée par France Éducation international quel que soit le centre, et l'arrêté du 22 décembre 2025 n'exige que la passation en présentiel dans un centre agréé.")],
         also=[("/centres/tcf-france/", "Centres TCF en France", "Les 247 centres agréés, région par région."),
               ("/centres/delf-allemagne/", "DELF et DALF en Allemagne", "Les dates 2026-2027, B2 à 201 €."),
               ("/centres/delf-suisse/", "DELF et DALF en Suisse", "Le calendrier national 2027."),
               ("/centres/delf-suede/", "DELF et DALF en Suède", "Pas de centre TCF : le TEF Canada à Stockholm."),
               ("/tcf-irn/", "TCF IRN : le test de français pour votre naturalisation", "")]),
    dict(slug="tcf-ameriques", files=["tcf_etats_unis", "tcf_mexique", "tcf_colombie", "tcf_argentine", "tcf_equateur", "tcf_chili", "tcf_perou", "tcf_bresil", "tcf_haiti"],
         layout="multi", exam="TCF", accent="accent-tcf",
         pointers=pays_pointers("États-Unis", "Mexique", "Colombie", "Argentine", "Équateur", "Chili", "Pérou"),
         modified="2026-10-08", date_fr="8 octobre 2026", list_date_fr="8 octobre 2026",
         crumb="Centres TCF aux États-Unis et en Amérique latine",
         title="Centres TCF aux États-Unis et en Amérique latine",
         desc="Les 62 centres TCF agréés dans 9 pays des Amériques : États-Unis, Mexique, Brésil, Colombie… Pour 7 pays, qui propose le TCF Canada, à quel prix, quand.",
         h1="Centres TCF aux États-Unis et en Amérique latine : les centres agréés, pays par pays",
         intro="""Sur le continent américain hors Canada, le TCF se passe dans les <strong>%(n)d centres agréés</strong>
par France Éducation international dans neuf pays au 8 octobre 2026 — presque tous des Alliances françaises —, dont
%(so)d avec des sessions sur ordinateur. Pour sept d'entre eux — États-Unis, Mexique, Colombie, Argentine, Chili,
Pérou, Équateur —, une page détaillée donne ce que nous avons relevé ce jour-là sur le site de chaque centre : qui
propose le TCF Canada, à quel prix, à quelles dates. Le Brésil et Haïti sont listés ici, avec leurs coordonnées.""",
         facts=["<strong>{n} centres dans 9 pays</strong> : États-Unis 18, Brésil 14, Mexique 11, Colombie 7, Argentine 5, Équateur 3, Chili 2, Pérou 1, Haïti 1 (liste FEI du 8 octobre 2026).",
                "Le TCF Canada n'est pas proposé partout : <strong>9 centres sur 18</strong> aux États-Unis, 5 sur 11 au Mexique, les 7 Alliances en Colombie.",
                "Prix relevés du TCF Canada : 330 à 460 $ aux États-Unis, 4 800 à 6 500 pesos au Mexique, 1 050 000 à 1 247 000 pesos en Colombie, 299 000 pesos au Chili, 1 240 soles au Pérou, 200 à 300 $ en Équateur.",
                "Le TCF Canada passé hors du Canada est accepté par IRCC comme partout : même attestation, même validité de deux ans.",
                "Brésil et Haïti : coordonnées publiées par FEI ; tarifs en monnaie locale, fixés par chaque centre.",
                "Le TEF Canada relève du réseau du Français des affaires."],
         stat4=("9", "pays", "7 avec une page détaillée"), cities_note="de New York à Lima",
         liste_label="pays par pays", decl="Canada, Québec, IRN, tout public, DAP",
         guides=[("/centres/tcf-etats-unis/", "TCF Canada aux États-Unis : 9 centres, prix et dates", "Qui le propose, de 330 à 460 $, et où restent des places."),
                 ("/centres/tcf-mexique/", "TCF Canada au Mexique : 5 centres, 4 800 à 6 500 pesos", "L'IFAL, Guadalajara, Puebla : sessions de calendrier ou sur demande."),
                 ("/blog/ou-passer-le-tcf-canada-au-canada/", "Où passer le TCF Canada au Canada ?", "Les 48 centres canadiens et la méthode pour obtenir une place.")],
         sources_links=[("Liste des centres TCF par pays (FEI)", "https://www.france-education-international.fr/centres-d-examen/liste?type-centre=tcf"), ("Carte des centres TCF", FEI_CARTE % "tcf")],
         sources_text="type « TCF », filtres États-Unis, Mexique, Colombie, Argentine, Équateur, Chili, Pérou, Brésil et Haïti",
         faq=[("Où passer le TCF Canada aux États-Unis ?", "Dans l'un des neuf centres qui le proposaient le 8 octobre 2026 — Alliances françaises de Detroit, New York, Denver, Philadelphie, Kansas City, Houston et San Francisco, International School of Boston, Pluma Academy à Denver —, de 330 à 460 $. Atlanta, Chicago, Seattle et Washington ne font pas le TCF Canada."),
              ("Où passer le TCF au Brésil ?", "Dans l'une des 14 Alliances françaises agréées listées ci-dessous — São Paulo, Rio de Janeiro, Brasília, Belo Horizonte, Porto Alegre… —, dont 13 proposent des sessions sur ordinateur. Les tarifs se demandent à l'Alliance."),
              ("Où passer le TCF Canada au Mexique ?", "À l'IFAL à Mexico (5 150 pesos en session de calendrier), aux Alliances françaises de Guadalajara (4 950) et de Puebla (4 800), à l'UAEH de Pachuca ou à l'Alliance d'Aguascalientes ; les autres centres agréés ne mentionnent pas le TCF Canada."),
              ("Le TCF Canada passé hors du Canada est-il accepté par IRCC ?", "Oui : l'attestation est délivrée par France Éducation international quel que soit le centre agréé, et vaut deux ans."),
              ("Comment vérifier qu'un centre est agréé ?", "Dans la liste officielle de FEI, par pays. Un organisme absent de cette liste ne peut pas délivrer d'attestation TCF.")],
         also=[("/centres/tcf-canada/", "Centres TCF au Canada", "Les 48 centres agréés, par province."),
               ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", ""),
               ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", ""),
               ("/blog/validite-attestation-tcf-tef/", "Validité de l'attestation : deux ans à partir de quand ?", "")]),
    dict(slug="tcf-moyen-orient", files=["tcf_liban", "tcf_emirats_arabes_unis", "tcf_egypte", "tcf_turquie"], layout="multi", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF au Liban, aux Émirats, en Égypte, en Turquie",
         modified="2026-10-26", date_fr="26 octobre 2026", list_date_fr="19 septembre et 26 octobre 2026",   # Turquie relue le 26/10/2026
         title="Centres TCF au Liban, aux Émirats, en Égypte, en Turquie",
         desc="Les 17 centres TCF agréés au Liban, aux Émirats arabes unis, en Égypte et en Turquie — Beyrouth, Dubaï, Le Caire, Istanbul… — avec leurs contacts.",
         h1="Centres TCF au Liban, aux Émirats arabes unis, en Égypte et en Turquie",
         intro="""Au Proche et Moyen-Orient, le TCF se passe dans les <strong>%(n)d centres agréés</strong> par France
Éducation international au Liban, aux Émirats arabes unis, en Égypte et en Turquie au 26 octobre
2026 — Instituts français, Alliances françaises et, à Antalya, la Henza French Academy —, dont %(so)d avec des sessions sur ordinateur.
Voici leurs coordonnées, pays par pays.""",
         facts=["<strong>17 centres dans 4 pays</strong> : Liban 6, Émirats arabes unis 4, Égypte 3, Turquie 4 (liste FEI du 26 octobre 2026).",
                "Le Liban est l'un des premiers pays d'origine des candidats au TCF Canada : six centres, dont l'Institut français du Liban à Beyrouth.",
                "Chaque centre choisit ses déclinaisons, ses dates et son tarif.",
                "Le TEF Canada relève du réseau du Français des affaires.",
                "20 à 30 jours entre deux passations ; attestation valable deux ans.",
                "Un organisme absent de cette liste n'est pas agréé."],
         stat4=("4", "pays", "Liban, Émirats, Égypte, Turquie"), cities_note="de Beyrouth à Istanbul",
         liste_label="pays par pays", decl="Canada, Québec, IRN, tout public, DAP",
         guides=[("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", ""),
                 ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", ""),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF par pays (FEI)", "https://www.france-education-international.fr/centres-d-examen/liste?type-centre=tcf"), ("Carte des centres TCF", FEI_CARTE % "tcf")],
         sources_text="type « TCF », filtres Liban, Émirats arabes unis, Égypte et Turquie",
         faq=[("Où passer le TCF Canada au Liban ?", "Dans l'un des six centres agréés listés ci-dessous, dont l'Institut français du Liban à Beyrouth et ses antennes."),
              ("Où passer le TCF à Dubaï ?", "Dans l'un des quatre centres agréés des Émirats arabes unis listés ci-dessous, tous avec des sessions sur ordinateur."),
              ("Où passer le TCF en Égypte ?", "Dans l'un des trois centres agréés listés ci-dessous, au Caire et à Alexandrie."),
              ("Le TCF Canada passé au Liban est-il accepté par IRCC ?", "Oui : l'attestation est délivrée par France Éducation international quel que soit le centre agréé, et vaut deux ans."),
              ("Comment vérifier qu'un centre est agréé ?", "Dans la liste officielle de FEI, par pays.")],
         also=[("/centres/tcf-inde/", "Centres TCF en Inde", "Les sept centres agréés."),
               ("/centres/tcf-canada/", "Centres TCF au Canada", "Les 48 centres agréés."),
               ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", ""),
               ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", "")]),
    dict(slug="tcf-inde", files=["tcf_inde"], layout="cities", exam="TCF", accent="accent-tcf",
         modified="2026-10-26", date_fr="26 octobre 2026", list_date_fr="26 octobre 2026",   # liste FEI relue le 26/10/2026 (relevé des sites : 8/10)
         crumb="Centres TCF en Inde",
         title="Centres TCF en Inde : les 7 centres agréés, contacts",
         desc="Les sept centres TCF agréés en Inde — Alliances françaises de New Delhi, Calcutta, Bangalore, Ahmedabad, Bhopal, Lucknow, Trivandrum —, leurs contacts.",
         h1="Centres TCF en Inde : les 7 centres agréés et leurs contacts",
         intro="""En Inde, le TCF Canada se passe dans l'un des <strong>%(n)d centres agréés</strong> par France Éducation
international au 26 octobre 2026 — les Alliances françaises —, dont %(so)d avec des sessions sur
ordinateur. Voici leurs coordonnées, ville par ville. Le TEF Canada, l'autre test accepté par IRCC,
relève du réseau du Français des affaires, souvent dans les mêmes Alliances.""",
         facts=["<strong>7 centres agréés</strong>, tous des Alliances françaises (liste FEI du 26 octobre 2026), 4 avec des sessions sur ordinateur : New Delhi, Calcutta, Ahmedabad, Trivandrum.",
                "Ni Mumbai ni Chennai ne figurent dans la liste du TCF.",
                "<strong>5 Alliances affichent le TCF Canada</strong> le 8 octobre 2026 : New Delhi, Calcutta, Ahmedabad, Bangalore, Bhopal ; Lucknow ne propose que le TEF Canada et Trivandrum annonce le TCF « bientôt ».",
                "Prix : <strong>26 000 roupies</strong> à New Delhi, Calcutta et Bhopal (TTC à New Delhi et Calcutta) ; non publié à Ahmedabad et Bangalore.",
                "Prochaines dates relevées : <strong>18 et 25 novembre</strong> à New Delhi (inscriptions du 4 au 11 novembre), <strong>4 décembre</strong> à Bhopal (une place) ; complet à New Delhi les 14 et 28 octobre et à Bangalore le 14 novembre.",
                "Chaque Alliance fixe ses dates et son tarif ; l'inscription se fait sur son site.",
                "Le TCF Canada passé en Inde est accepté par IRCC comme partout : même attestation, valable deux ans.",
                "20 à 30 jours entre deux passations.",
                "Pour Entrée express, visez le NCLC 7 : 458 en compréhension orale, 453 à l'écrit.",
                "Un organisme absent de cette liste n'est pas agréé."],
         stat4=("7", "Alliances françaises", "de Delhi à Trivandrum"), cities_note="Delhi, Calcutta, Bangalore…",
         liste_label="ville par ville", decl="Canada, Québec, tout public, DAP",
         guides=[("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", ""),
                 ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", ""),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF en Inde", FEI_LISTE % (45, "tcf")), ("Carte des centres TCF", FEI_CARTE % "tcf")],
         sources_text="filtre « Inde », type « TCF », et sites des Alliances françaises de New Delhi, Calcutta, Ahmedabad, Bangalore, Bhopal, Lucknow et Trivandrum (pages TCF et TEF, calendriers, boutiques, consultés le 8 octobre 2026)",
         faq=[("Où passer le TCF Canada en Inde ?", "Dans l'une des sept Alliances françaises agréées listées ci-dessous — à New Delhi, Calcutta, Bangalore, Ahmedabad, Bhopal, Lucknow et Trivandrum. Mumbai et Chennai ne figurent pas dans la liste du TCF de France Éducation international (26 octobre 2026)."),
              ("Le TCF Canada passé en Inde est-il accepté par IRCC ?", "Oui : l'attestation est délivrée par France Éducation international quel que soit le centre agréé, et vaut deux ans."),
              ("Combien coûte le TCF en Inde ?", "26 000 roupies pour le TCF Canada à New Delhi, Calcutta et Bhopal (TTC à New Delhi et Calcutta) le 8 octobre 2026 ; Ahmedabad et Bangalore ne publient pas leur tarif. Calcutta affiche aussi le TCF Québec à 6 500 roupies par épreuve."),
              ("TCF Canada ou TEF Canada ?", "Les deux sont acceptés par IRCC ; le TEF relève du réseau du Français des affaires, souvent proposé par les mêmes Alliances. Notre comparatif TCF ou TEF Canada les met côte à côte."),
              ("Comment vérifier qu'un centre est agréé ?", "Dans la liste officielle de FEI, filtre « Inde ».")],
         also=[("/centres/tcf-moyen-orient/", "Centres TCF au Liban, aux Émirats, en Égypte, en Turquie", ""),
               ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", ""),
               ("/blog/ou-passer-le-tcf-canada-au-canada/", "Où passer le TCF Canada au Canada ?", ""),
               ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", "")]),
]


def regional_counts(pages_built):
    label = {"tcf-europe": "Europe", "tcf-ameriques": "Amériques", "tcf-moyen-orient": "Moyen-Orient", "tcf-inde": "Inde"}
    return [(label[spec["slug"]], n) for spec, (n, _, _) in pages_built if spec["slug"] in label]


def villes_hub():
    groups = [("France — TCF", ("fr", "tcf")), ("France — DELF", ("fr", "delf")), ("Canada", ("ca", "tcf")),
              ("Algérie", ("dz", "tcf")), ("Maroc", ("ma", "tcf")), ("Tunisie", ("tn", "tcf"))]
    out = []
    for label, key in groups:
        items = villes_of(key)
        if items:
            out.append(f'<p class="serie-label">{label}</p>\n<div class="chips">\n' + "\n".join(f'<a class="chip" href="{u}">{esc(t)}</a>' for u, t in items) + "\n</div>")
    return "\n".join(out)


def hub(pages_built):
    # Pages pays (make_pays.py, 08/10/2026) : DELF et TCF dans neuf pays, avec relevés. Import tardif :
    # make_pays importe ce module.
    from make_pays import specs as pays_specs, counts_of
    pays = [(p, counts_of(p)) for p in pays_specs()]
    rows = []
    for spec, (n, so, ncity) in pages_built:
        rows.append(f'<tr><td><a href="/centres/{spec["slug"]}/">{esc(spec["crumb"])}</a></td><td><strong>{n}</strong></td><td>{so}</td><td>{ncity}</td></tr>')
    for p, (n, so, ncity) in pays:
        rows.append(f'<tr><td><a href="/centres/{p["slug"]}/">{esc(p["crumb"])}</a></td><td><strong>{n}</strong></td><td>{so if p["exam"] == "tcf" else "—"}</td><td>{ncity}</td></tr>')
    table = ('<div class="tablewrap">\n<table>\n<caption>Les listes de centres publiées sur ce site, d\'après la liste officielle de France Éducation international lue le 19 septembre 2026, et le 8 ou le 26 octobre 2026 pour les pays détaillés. L\'option « sur ordinateur » n\'existe que pour le TCF.</caption>\n'
             '<thead><tr><th>Liste</th><th>Centres</th><th>Sur ordinateur</th><th>Villes</th></tr></thead>\n<tbody>\n' + "\n".join(rows) + "\n</tbody>\n</table>\n</div>")
    # Chaque fichier de données compté une fois : un pays présent sur une page régionale (en renvoi)
    # et sur sa page pays n'est pas compté deux fois.
    files = {f for spec, _ in pages_built for f in spec["files"]} | {p["file"] for p, _ in pays}
    total = sum(len(load(f)["centres"]) for f in files)
    npays = len({load(f)["country"] for f in files})
    nlists = len(pages_built) + len(pays)
    order = []
    for p, c in pays:
        ctry = load(p["file"])["country"]
        if ctry not in order:
            order.append(ctry)
    cell = {(load(p["file"])["country"], p["exam"]): (p, c) for p, c in pays}
    def link(ctry, exam):
        if (ctry, exam) not in cell:
            return "—"
        p, (n, _, _) = cell[(ctry, exam)]
        return f'<a href="/centres/{p["slug"]}/">{n} centre{"s" if n > 1 else ""}</a>'
    pays_table = ('<div class="tablewrap">\n<table>\n<caption>Une page par examen et par pays : la liste FEI du 8 ou du 26 octobre 2026, le relevé des sites des centres (déclinaisons, prix, dates) et l\'inscription.</caption>\n'
                  '<thead><tr><th>Pays</th><th>TCF, dont TCF Canada</th><th>DELF-DALF</th></tr></thead>\n<tbody>\n'
                  + "\n".join(f'<tr><td><strong>{esc(c)}</strong></td><td>{link(c, "tcf")}</td><td>{link(c, "delf")}</td></tr>' for c in order)
                  + "\n</tbody>\n</table>\n</div>")
    n_delf_pays = sum(c[0] for p, c in pays if p["exam"] == "delf")
    n_tcf_pays = sum(c[0] for p, c in pays if p["exam"] == "tcf")
    cards = "\n".join(
        f'<div class="card card-link"><span class="tag">{esc(spec["exam"])}</span><h3><a href="/centres/{spec["slug"]}/">{esc(spec["crumb"])}</a></h3><p>{n} centres · {so} sur ordinateur · {ncity} villes</p></div>'
        for spec, (n, so, ncity) in pages_built)
    body = f"""
{stats([(fr_int(total), "centres listés", "avec leurs contacts"), (str(npays), "pays", "sur les listes FEI"), (str(nlists), "listes", "par pays ou région"), ("26/10", "dernière lecture", "de la liste FEI")])}

<form class="finder-mini" action="/trouver-un-centre/" method="get" role="search">
<label for="finder-mini-q">Trouver un centre d'examen près de chez vous</label>
<div class="finder-row"><input id="finder-mini-q" name="q" type="search" placeholder="Ville, pays ou nom du centre" autocomplete="off" enterkeyhint="search"><button type="submit">Chercher</button></div>
<p>TCF, DELF-DALF, TEF et examen civique : les centres agréés les plus proches, avec la distance. <a href="/trouver-un-centre/">Ou autour de moi →</a></p>
</form>

<h2 id="listes">Les listes, par examen et par pays</h2>
<div class="grid c2 guides">
{cards}
</div>

{table}

<h2 id="pays">Hors de France : le DELF et le TCF dans {len(order)} pays, avec prix et dates</h2>
<p>Pour {len(order)} pays d'Europe et des Amériques, une page par examen réunit la liste officielle lue le
8 ou le 26 octobre 2026 — {n_tcf_pays} centres TCF, {n_delf_pays} centres DELF-DALF —, ce que le site de chaque centre affichait
ce jour-là — qui propose le TCF Canada, à quel prix, à quelles dates ; le calendrier et les tarifs du DELF — et
la marche à suivre pour s'inscrire.</p>
{pays_table}

<h2 id="villes">Les guides par ville</h2>
<p>Pour {sum(len(villes_of(k)) for k in VILLES_KEY.values())} grandes villes, une page réunit les centres agréés avec leurs
contacts, ce que leurs sites affichaient le 17 septembre 2026 — déclinaisons, prix, dates — et la
procédure d'inscription du pays.</p>
{villes_hub()}

<h2 id="methode">D'où viennent ces listes</h2>
<p>Toutes reprennent la <strong>liste officielle des centres d'examen de France Éducation
international</strong> — DELF-DALF, TCF et examen civique —, lue pays par pays le 19 septembre
2026, le 8 et le 26 octobre 2026, avec les coordonnées que FEI publie : adresse, téléphone, adresse e-mail générique, site.
Elles disent qu'un centre est agréé ; elles ne disent pas quelles déclinaisons il organise, ni ses
dates, ni ses tarifs. C'est le travail de nos guides <a href="/ou-passer/">« Où passer »</a>, qui ont
ouvert les sites des principaux centres. Le TEF, lui, relève du Français des affaires (CCI Paris
Île-de-France), dont l'<a href="https://www.lefrancaisdesaffaires.fr/trouver-un-centre-agree/" rel="noopener">annuaire
des centres agréés</a> couvre tous les pays.</p>

<h2 id="regles">Trois règles avant d'appeler un centre</h2>
<ol>
<li><strong>Vérifiez la déclinaison.</strong> Un centre TCF n'organise pas forcément le TCF Canada, ni
le TCF IRN ; un centre TCF n'est pas automatiquement centre DELF ou centre d'examen civique. Chaque
agrément est distinct.</li>
<li><strong>Le prix et la date sont ceux du centre.</strong> Aucun tarif national, aucun calendrier
central pour le TCF : deux centres de la même ville peuvent avoir des prix du simple au double et des
sessions sans rapport.</li>
<li><strong>Un organisme absent de la liste n'est pas agréé</strong>, quel que soit son site ou son
nom — et une attestation « à distance » n'existe pas. En cas de doute, la liste de FEI fait foi.</li>
</ol>
"""
    return {
        "section": "", "slug": "centres", "accent": "accent-delf", "crumb": "Centres d'examen",
        "lang_links": '<p class="langs"><a href="/es/" hreflang="es" lang="es">En español</a> · <a href="/en/" hreflang="en" lang="en">In English</a></p>',   # pages /es/ et /en/ (08/10/2026)
        "title": "Centres d'examen DELF, TCF et examen civique : l'annuaire",
        "desc": f"{fr_int(total)} centres agréés par FEI dans {npays} pays, avec adresse, téléphone, e-mail et site : France, Canada, Maghreb, Europe, Amériques, Afrique.",
        "og_title": "Centres d'examen DELF, TCF et examen civique : l'annuaire", "og_desc": f"{fr_int(total)} centres agréés dans {npays} pays, avec leurs contacts, d'après la liste officielle de FEI.",
        "h1": "Centres d'examen DELF, TCF et examen civique : l'annuaire des centres agréés",
        "published": DATE, "modified": "2026-10-26", "date_fr": "26 octobre 2026", "read": 5,
        "intro": f"""Tous les examens de ce site se passent dans un <strong>centre agréé</strong> — par France Éducation
international pour le DELF, le DALF, le TCF et l'examen civique. Cet annuaire reprend sa liste
officielle, lue le 19 septembre 2026 et complétée les 8 et 26 octobre 2026 : <strong>{fr_int(total)} centres dans {npays} pays</strong>,
avec l'adresse, le téléphone, l'e-mail et le site de chacun, classés par pays, région et ville. Choisissez votre
liste, puis vérifiez sur le site du centre la déclinaison, la date et le prix.""",
        "facts": [f"<strong>{fr_int(total)} centres</strong> avec leurs contacts, d'après la liste officielle de FEI (19 septembre 2026, complétée les 8 et 26 octobre 2026).",
                  "France : <strong>247 centres TCF</strong>, <strong>143 centres DELF-DALF</strong>, <strong>245 centres d'examen civique</strong>.",
                  "TCF hors de France : Canada 48 · Maroc 16 · Tunisie 14 · Algérie 5 · Afrique subsaharienne 23 · " + " · ".join(f"{t} {n}" for t, n in regional_counts(pages_built)) + ".",
                  f"<strong>{len(order)} pays détaillés</strong> — {', '.join(order[:-1])} et {order[-1]} — : {n_tcf_pays} centres TCF et {n_delf_pays} centres DELF-DALF, avec prix et dates relevés.",
                  "Chaque liste dit qu'un centre est agréé, pas quelle déclinaison il organise : nos relevés le vérifient pour les pays détaillés et les grandes villes.",
                  "Un organisme absent de ces listes n'est pas agréé."],
        "toc": [("listes", "Les listes, par examen et par pays"), ("pays", f"Hors de France : {len(order)} pays détaillés"), ("villes", "Les guides par ville"), ("methode", "D'où viennent ces listes"), ("regles", "Trois règles avant d'appeler un centre")],
        "body": body,
        "cta_h2": "Le centre vous donne la date ; le score, c'est vous",
        "cta_p": """Une session se paie en entier et se repasse après un délai. Les examens blancs de l'app
«&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent le format officiel de chaque déclinaison, avec
la notation du vrai test et la correction IA de l'écrit et de l'oral.""",
        "faq": [("Comment trouver un centre d'examen près de chez moi ?", "Ouvrez la liste de votre pays ci-dessus : les centres y sont classés par région ou par ville, avec adresse, téléphone, e-mail et site. Pour un autre pays, la liste officielle de France Éducation international se filtre par pays."),
                ("Ces listes sont-elles officielles ?", "Elles reproduisent la liste officielle de France Éducation international, lue le 19 septembre 2026 — le 8 octobre 2026 pour l'Espagne, le Royaume-Uni, les États-Unis et l'Amérique latine, le 26 octobre 2026 pour dix autres pays d'Europe et pour le TCF en France, au Canada, en Turquie, au Sénégal et en Inde —, avec les coordonnées que FEI publie. FEI agrée et retire des centres au fil de l'année : en cas de doute, sa liste en ligne fait foi."),
                ("Un centre TCF fait-il passer le TCF Canada ?", "Pas forcément : chaque centre choisit ses déclinaisons — Canada, Québec, IRN, tout public. La liste de FEI ne le précise pas ; le site du centre, si. Nos guides « Où passer » l'ont vérifié pour les principaux centres."),
                ("Où sont les centres TEF ?", "Le TEF relève du Français des affaires (CCI Paris Île-de-France), qui publie son propre annuaire « Trouver un centre agréé », tous pays confondus."),
                ("Peut-on passer ces examens en ligne ?", "Non. DELF, DALF, TCF et examen civique se passent en présentiel, dans un centre agréé, sur convocation et avec contrôle d'identité. Toute offre « à distance » est une fraude.")],
        "also": [("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub des guides", "Prix relevés, dates de session, pas-à-pas d'inscription, pays par pays."),
                 ("/blog/prix-tcf-tef/", "Combien coûte vraiment le TCF ou le TEF ?", "Aucun tarif national : les prix relevés centre par centre."),
                 ("/blog/diplome-ou-test-delf-tcf/", "Diplôme ou test : lequel vous faut-il ?", ""),
                 ("/examens-blancs/", "Examens blancs au format officiel", "")],
        "sources": """<strong>Sources.</strong> Listes et carte des centres d'examen de France Éducation international
(DELF-DALF, TCF, examen civique), lues pays par pays le 19 septembre 2026, et le 8 octobre 2026 pour
l'Espagne, le Royaume-Uni, les États-Unis, le Mexique, la Colombie, l'Argentine, le Chili, le Pérou et
l'Équateur, et le 26 octobre 2026 pour l'Allemagne, la Suisse, la Belgique, l'Italie, les Pays-Bas, le Portugal, la
Roumanie, la Pologne, la Grèce et l'Irlande, ainsi que le TCF en France, au Canada, en Turquie, au Sénégal et en Inde ; annuaire « Trouver un centre agréé » du Français des affaires. Chaque liste cite son filtre
et sa date.""",
    }


def main():
    force = "--force" in sys.argv
    built = []
    arts = []
    for spec in PAGES:
        datasets = [load(f) for f in spec["files"]]
        a = page(spec, datasets)
        assert len(a["title"]) <= 60, (a["slug"], len(a["title"]))
        arts.append(a)
        built.append((spec, counts(datasets)))
    arts.append(hub(built))
    for a in arts:
        assert len(a["desc"]) <= 158, (a["slug"], len(a["desc"]))
    build(arts, overwrite=force)


if __name__ == "__main__":
    main()
