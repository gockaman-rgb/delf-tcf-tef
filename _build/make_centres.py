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
           "Émirats arabes unis": 101, "Turquie": 95, "Brésil": 19, "Mexique": 30, "Colombie": 21}
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


def section_multi(datasets):
    body, index = [], []
    for d in datasets:
        cid = uniq("pays-" + slug(d["country"]))
        n = len(d["centres"])
        index.append((cid, f"{d['country']} ({n})"))
        cards, _ = group_cards(d["centres"], d["country"], 3)
        src = FEI_LISTE % (PAYS_ID[d["country"]], "tcf")
        body.append(f'<h2 id="{cid}">{esc(d["country"])} — {n} centre{"s" if n > 1 else ""}</h2>\n'
                    f'<p class="src">Liste officielle : <a href="{src}" rel="noopener">centres TCF, {esc(d["country"])}</a> (FEI).</p>\n{cards}')
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
        body, index = section_multi(datasets)
    st = stats([(str(n), "centres agréés", f"liste FEI du {DATE_FR}"),
                (str(so), "sur ordinateur", "les autres sur papier"),
                (str(ncity), "villes", spec.get("cities_note", "")),
                (spec["stat4"][0], spec["stat4"][1], spec["stat4"][2])])
    guides = "\n".join(f'<li><a href="{u}">{t}</a>' + (f"\n<p>{d}</p>" if d else "") + "</li>" for u, t, d in spec["guides"])
    src_links = " · ".join(f'<a href="{u}" rel="noopener">{t}</a>' for t, u in spec["sources_links"])
    support = ("« Sur ordinateur » signifie que le centre propose des sessions sur ordinateur ; « papier » qu'il n'en\ndéclare pas. " if spec["exam"] == "TCF" else "")
    method = METHOD % {"date": DATE_FR, "decl": spec["decl"], "support": support}
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
nôtre est datée du {DATE_FR} ; en cas de doute, la liste de FEI fait foi.</p>
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
        "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": max(4, n // 25),
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
{spec['sources_text']}, consultée le {DATE_FR}. Les coordonnées sont celles publiées par FEI ; seules les
adresses e-mail génériques (contact, examens, certifications…) sont reprises. Signalez-nous une
erreur ou une fermeture : la liste est mise à jour à chaque nouvelle lecture de la source.""",
    }
    return a


# ---------------------------------------------------------------------------
# Les pages
# ---------------------------------------------------------------------------
G_TCF_FR = [("/blog/ou-passer-le-tcf-irn-en-france/", "Où passer le TCF IRN en France ?", "Les centres relevés à Paris et en région, 140 à 220 €, papier ou ordinateur."),
            ("/blog/ou-passer-le-tcf-canada-en-france/", "Où passer le TCF Canada en France ?", "Les centres qui le proposent, 195 à 285 €, leurs sessions mensuelles.")]
PAGES = [
    dict(slug="tcf-france", files=["tcf_france"], layout="france", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF en France",
         title="Centres TCF agréés en France : liste, adresses, téléphones",
         desc="Les 251 centres TCF agréés par France Éducation international, région par région, avec adresse, téléphone, e-mail et site — liste du 19 septembre 2026.",
         h1="Centres TCF agréés en France : la liste des 251 centres, région par région",
         intro="""France Éducation international agrée <strong>%(n)d centres de passation du TCF</strong> en
France au 19 septembre 2026 — Alliances françaises, écoles de langue, GRETA, organismes de
formation, universités —, dont <strong>%(so)d proposent des sessions sur ordinateur</strong>, dans
<strong>%(cities)d villes</strong>. Voici la liste complète, région par région et ville par ville, avec
l'adresse, le téléphone, l'e-mail et le site de chaque centre, telle que FEI la publie. Vérifiez
ensuite sur le site du centre qu'il organise bien la déclinaison qu'il vous faut : IRN, Canada,
Québec ou tout public.""",
         facts=["<strong>{n} centres agréés</strong> en France, liste FEI du 19 septembre 2026 — {so} avec des sessions sur ordinateur.",
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
         faq=[("Combien de centres TCF y a-t-il en France ?", "251 centres de passation agréés par France Éducation international au 19 septembre 2026, dont 127 proposent des sessions sur ordinateur. L'Île-de-France en compte 33, dont sept dans Paris ; Auvergne-Rhône-Alpes et Occitanie 30 chacune."),
              ("Comment savoir si un centre propose le TCF Canada ou le TCF IRN ?", "La liste officielle ne le précise pas : chaque centre choisit les déclinaisons qu'il organise. Ouvrez la page TCF du centre ou appelez-le. Nos guides « Où passer le TCF IRN en France » et « Où passer le TCF Canada en France » l'ont vérifié pour les principaux centres, avec leurs prix et leurs dates."),
              ("Comment s'inscrire au TCF ?", "Directement auprès du centre — en ligne dans la plupart des cas, avec une pièce d'identité et un paiement par carte. France Éducation international n'inscrit aucun candidat. Les sessions sont hebdomadaires à Paris pour le TCF IRN, mensuelles pour le TCF Canada."),
              ("Cette liste est-elle à jour ?", "Elle reproduit la liste de France Éducation international lue le 19 septembre 2026. FEI agrée et retire des centres au fil de l'année ; en cas de doute, sa liste en ligne fait foi. Les coordonnées reprises sont celles publiées par FEI."),
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
         also=[("/centres/tcf-france/", "Centres TCF en France", "Les 251 centres de passation agréés, région par région."),
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
         also=[("/centres/tcf-france/", "Centres TCF en France", "Les 251 centres agréés, pour le test de français qui accompagne l'examen civique."),
               ("/blog/ou-passer-le-tcf-irn-en-france/", "Où passer le TCF IRN en France ?", "Sept centres à Paris, des sessions chaque semaine, 140 à 220 €."),
               ("/tcf-irn/", "TCF IRN : le test de français pour votre naturalisation", "Format, niveaux exigés, échelle sur 499."),
               ("/blog/b1-ou-b2-nationalite-francaise/", "B1 ou B2 pour la nationalité française ?", "Le tableau des trois démarches.")]),
    dict(slug="tcf-canada", files=["tcf_canada"], layout="canada", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF au Canada",
         title="Centres TCF au Canada : les 47 centres agréés, par province",
         desc="Les 47 centres TCF agréés au Canada — Montréal, Toronto, Vancouver, Ottawa… — par province, avec adresse, téléphone, e-mail et site. Liste FEI 2026.",
         h1="Centres TCF au Canada : les 47 centres agréés, province par province",
         intro="""Au Canada, le TCF Canada et le TCF Québec se passent dans l'un des <strong>47 centres agréés</strong>
par France Éducation international (48 entrées dans sa liste du 19 septembre 2026, un centre apparaissant
deux fois) — Alliances françaises, universités, cégeps, centres de formation —, présents dans
<strong>neuf provinces et au Nunavut</strong>, %(so)d avec des sessions sur ordinateur. Voici la liste
par province et par ville, avec les coordonnées publiées par FEI, et les règles d'inscription relevées
sur les principaux centres.""",
         facts=["<strong>47 centres agréés</strong> (48 entrées FEI, Gaspé en double), liste du 19 septembre 2026 : 23 au Québec dont 7 à Montréal, 7 en Ontario, 5 en Colombie-Britannique, 3 en Alberta.",
                "<strong>45 entrées avec sessions sur ordinateur</strong> ; papier seulement à Sherbrooke, Lethbridge et à l'Université de Victoria.",
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
               ("/centres/tcf-france/", "Centres TCF en France", "Les 251 centres agréés, pour un TCF Canada passé depuis la France."),
               ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", "Les deux tables NCLC et le comparatif de format.")]),
    dict(slug="tcf-algerie", files=["tcf_algerie"], layout="cities", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF en Algérie",
         title="Centres TCF en Algérie : les 5 antennes agréées, contacts",
         desc="Les cinq centres TCF agréés en Algérie — Institut français d'Alger, Oran, Constantine, Annaba, Tlemcen — avec adresse, téléphone, e-mail et site.",
         h1="Centres TCF en Algérie : les 5 antennes agréées et leurs contacts",
         intro="""En Algérie, le TCF — Canada, Québec, IRN, tout public ou DAP — se passe uniquement dans les
<strong>cinq antennes de l'Institut français d'Algérie</strong> : Alger (Hydra), Oran, Constantine,
Annaba et Tlemcen, seuls centres agréés par France Éducation international au 19 septembre 2026, tous
avec des sessions sur ordinateur. L'inscription se fait exclusivement en ligne, sur la plateforme IFAL
opérée par VFS Global. Voici les coordonnées officielles des cinq antennes — et le rappel du faux
site qui imite l'Institut.""",
         facts=["<strong>5 centres agréés</strong>, tous des antennes de l'Institut français d'Algérie ; aucune école privée n'est agréée.",
                "Inscription <strong>en ligne uniquement</strong> sur la plateforme IFAL (forms.vfsglobal.com.dz/IFAL), depuis la page TCF de <strong>if-algerie.com</strong>.",
                "Sessions <strong>chaque mois</strong> sur les cinq antennes ; <strong>26 jours</strong> entre deux inscriptions.",
                "Pièce d'identité : carte biométrique ou passeport (Algériens), passeport biométrique ou carte consulaire (autres).",
                "Tarif non publié hors plateforme ; attestation par e-mail, aucune version papier depuis mars 2023.",
                "⚠️ <strong>if-algerie.fr est une escroquerie</strong> ; le site officiel est if-algerie.com."],
         stat4=("IFAL", "plateforme d'inscription", "opérée par VFS Global"), cities_note="Alger, Oran, Constantine, Annaba, Tlemcen",
         liste_label="ville par ville", decl="Canada, Québec, IRN, tout public, DAP",
         guides=[("/blog/tcf-canada-algerie/", "TCF Canada en Algérie : où le passer, comment s'inscrire", "La plateforme IFAL pas à pas, la règle des 26 jours, les résultats, le faux site à éviter."),
                 ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", ""),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF en Algérie", FEI_LISTE % (115, "tcf")), ("Page TCF de l'Institut français d'Algérie", "https://www.if-algerie.com/tests-et-examens/tcf")],
         sources_text="filtre « Algérie », type « TCF », et site de l'Institut français d'Algérie",
         faq=[("Où passer le TCF Canada en Algérie ?", "Dans l'une des cinq antennes de l'Institut français d'Algérie — Alger (Hydra), Oran, Constantine, Annaba, Tlemcen —, seuls centres agréés par France Éducation international dans le pays. Toutes proposent des sessions sur ordinateur."),
              ("Comment s'inscrire ?", "Exclusivement en ligne, sur la plateforme IFAL opérée par VFS Global, accessible depuis la page TCF du site officiel if-algerie.com : compte, choix de la déclinaison, de l'antenne et de la session, paiement en ligne. Aucune inscription sur place."),
              ("Combien coûte le TCF en Algérie ?", "L'Institut ne publie pas de tarif sur son site : le prix s'affiche sur la plateforme au moment de choisir la session. Les montants de 70 000 à 100 000 dinars qui circulent sont ceux d'un site frauduleux."),
              ("Quel est le site officiel ?", "if-algerie.com. Le site if-algerie.fr, qui imite l'Institut et propose un « candidat partenaire » pour passer l'examen à votre place, est une escroquerie."),
              ("Peut-on aussi passer l'examen civique français en Algérie ?", "Oui, à l'Institut français d'Alger (30, rue des Frères-Kadri, Hydra), avec une pré-inscription sur test-civique.fr et un paiement de 9 000 dinars sur place ou par virement.")],
         also=[("/blog/tcf-canada-algerie/", "TCF Canada en Algérie : où le passer, comment s'inscrire", "Le guide complet, avec le faux site à éviter."),
               ("/centres/tcf-maroc/", "Centres TCF au Maroc", "Les 16 centres agréés, avec leurs contacts."),
               ("/centres/tcf-tunisie/", "Centres TCF en Tunisie", "Les 14 centres agréés, avec leurs contacts."),
               ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", "")]),
    dict(slug="tcf-maroc", files=["tcf_maroc"], layout="cities", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF au Maroc",
         title="Centres TCF au Maroc : les 16 centres agréés, contacts",
         desc="Les 16 centres TCF agréés au Maroc — Instituts français de Casablanca, Rabat, Marrakech, Fès, Tanger, Agadir… — avec adresse, téléphone, e-mail et site.",
         h1="Centres TCF au Maroc : les 16 centres agréés et leurs contacts",
         intro="""Au Maroc, le TCF se passe dans les <strong>%(n)d centres agréés</strong> par France Éducation
international au 19 septembre 2026 : quatorze sites de l'Institut français du Maroc — de Tanger à
Agadir — et les Alliances françaises de Safi et de Ouarzazate, %(so)d avec des sessions sur ordinateur.
Le tarif est national (2 900 dirhams pour le TCF Canada, 1 900 pour l'IRN et le tout public) et
l'inscription se fait en ligne, sur le site de l'Institut de votre ville. Voici les coordonnées de
chaque centre.""",
         facts=["<strong>16 centres agréés</strong> : 14 Instituts français (dont Béni Mellal et Nador, rattachés à Casablanca et Oujda) et 2 Alliances françaises (Safi, Ouarzazate).",
                "Tarif national : <strong>TCF Canada, Québec et TEF Canada 2 900 Dhs</strong> ; TCF IRN et tout public 1 900 Dhs (relevé le 17 septembre 2026).",
                "Inscription <strong>en ligne, sur le site de l'Institut de votre ville</strong> (panier) ; le TCF IRN s'inscrit sur place uniquement.",
                "Casablanca : sessions les mardis, jeudis et samedis ; Rabat : neuf sessions relevées d'ici fin novembre 2026.",
                "<strong>20 jours</strong> de carence entre deux TCF ; aucun remboursement ; report sur justificatif facturé 500 Dhs.",
                "Un organisme absent de cette liste n'est pas agréé : pas d'« agent », pas de revendeur."],
         stat4=("2 900 Dhs", "TCF Canada", "tarif national IFM"), cities_note="de Tanger à Agadir",
         liste_label="ville par ville", decl="Canada, Québec, IRN, tout public, DAP",
         guides=[("/blog/tcf-canada-maroc/", "TCF Canada au Maroc : les 16 centres et l'inscription", "L'inscription en ligne pas à pas, les sessions relevées à Casablanca, Rabat, Tanger et Marrakech, les règles de report."),
                 ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", ""),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF au Maroc", FEI_LISTE % (117, "tcf")), ("Institut français du Maroc — TCF Canada", "https://if-maroc.org/certifications/tcf-canada/")],
         sources_text="filtre « Maroc », type « TCF », et site de l'Institut français du Maroc",
         faq=[("Où passer le TCF Canada au Maroc ?", "Dans l'un des seize centres agréés : les Instituts français d'Agadir, Béni Mellal, Casablanca, El Jadida, Essaouira, Fès, Kénitra, Marrakech, Meknès, Nador, Oujda, Rabat, Tanger et Tétouan, et les Alliances françaises de Safi et de Ouarzazate."),
              ("Combien coûte le TCF au Maroc ?", "2 900 dirhams pour le TCF Canada, le TCF Québec et le TEF Canada ; 1 900 dirhams pour le TCF IRN et le TCF tout public — tarif de l'Institut français du Maroc relevé à Casablanca et Rabat le 17 septembre 2026."),
              ("Comment s'inscrire ?", "En ligne, sur le site de l'Institut français de votre ville (if-maroc.org/casablanca, /rabat…), page TCF Canada : choix de la session, panier, paiement. Pièce d'identité et photo demandées ; convocation remise dès l'inscription. Le TCF IRN s'inscrit à l'accueil."),
              ("À quelle fréquence ont lieu les sessions ?", "Cela dépend du site : à Casablanca, plusieurs sessions par semaine (mardi, jeudi, samedi) relevées le 17 septembre 2026 ; neuf sessions à Rabat d'ici fin novembre ; une date à Tanger et à Marrakech en octobre."),
              ("Peut-on se faire rembourser ?", "Non : « le candidat ne pourra, en aucun cas, être remboursé ». Un report est possible sur justificatif (maladie, décès, accident, examen officiel) envoyé sous 5 jours ouvrés, facturé 500 dirhams.")],
         also=[("/blog/tcf-canada-maroc/", "TCF Canada au Maroc : les 16 centres et l'inscription", "Le guide complet."),
               ("/centres/tcf-algerie/", "Centres TCF en Algérie", "Les cinq antennes de l'Institut français."),
               ("/centres/tcf-tunisie/", "Centres TCF en Tunisie", "Les 14 centres agréés."),
               ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", "")]),
    dict(slug="tcf-tunisie", files=["tcf_tunisie"], layout="cities", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF en Tunisie",
         title="Centres TCF en Tunisie : les 14 centres agréés, contacts",
         desc="Les 14 centres TCF agréés en Tunisie — Institut français de Tunis, Sousse, Sfax, Nabeul, Béja, Kébili, six Alliances françaises — avec leurs contacts.",
         h1="Centres TCF en Tunisie : les 14 centres agréés et leurs contacts",
         intro="""En Tunisie, le TCF se passe dans les <strong>%(n)d centres agréés</strong> par France Éducation
international au 19 septembre 2026 : les pôles de l'Institut français de Tunisie — Tunis, El Mourouj,
Nabeul-Hammamet, Béja, Sousse, Sfax, Kébili, Médenine — et six Alliances françaises (Tunis-Ariana,
Bizerte, Djerba, Gabès, Gafsa, Kairouan), tous avec des sessions sur ordinateur. À l'Institut, le TCF
Canada coûte 880 dinars et se réserve en ligne avant une inscription sur place. Voici les coordonnées
de chaque centre.""",
         facts=["<strong>14 centres agréés</strong> : 8 pôles de l'Institut français de Tunisie et 6 Alliances françaises, tous avec des sessions sur ordinateur.",
                "À l'Institut : <strong>TCF Canada et TCF Québec 880 DT</strong>, TCF IRN 625 DT, TCF tout public 335 DT + 220 DT par expression (17 septembre 2026).",
                "Procédure en deux temps : <strong>rendez-vous en ligne</strong>, puis <strong>inscription et paiement sur place</strong> le jour fixé — un mandataire muni d'une copie de votre carte d'identité peut y aller.",
                "Une session par mois par pôle ; résultats <strong>5 semaines</strong> après ; <strong>30 jours</strong> entre deux sessions.",
                "Paiement en espèces (carte bancaire à Tunis seulement) ; chèques suspendus ; frais non remboursables.",
                "Le TCF Canada est proposé dans sept pôles de l'Institut ; Médenine n'apparaît que pour le tout public."],
         stat4=("880 DT", "TCF Canada à l'Institut", "5 semaines de résultats"), cities_note="de Bizerte à Médenine",
         liste_label="ville par ville", decl="Canada, Québec, IRN, tout public",
         guides=[("/blog/tcf-canada-tunisie/", "TCF Canada en Tunisie : centres, calendrier, inscription", "Le calendrier 2026 de Tunis, la procédure rendez-vous puis inscription, les frais, les délais."),
                 ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", ""),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF en Tunisie", FEI_LISTE % (118, "tcf")), ("Institut français de Tunisie — TCF Canada", "https://www.institutfrancais-tunisie.com/examens/tcf-canada/")],
         sources_text="filtre « Tunisie », type « TCF », et site de l'Institut français de Tunisie",
         faq=[("Où passer le TCF Canada en Tunisie ?", "À l'Institut français de Tunisie — pôles de Tunis, El Mourouj, Nabeul-Hammamet, Béja, Sousse, Sfax et Kébili — ou dans une Alliance française (Tunis-Ariana, Bizerte, Djerba, Gabès, Gafsa, Kairouan). Quatorze centres agréés au total."),
              ("Combien coûte le TCF en Tunisie ?", "À l'Institut français, 880 dinars pour le TCF Canada et le TCF Québec, 625 dinars pour le TCF IRN, 335 dinars pour les épreuves obligatoires du TCF tout public sur ordinateur (17 septembre 2026). Les Alliances ne publient pas de tarif lisible en ligne."),
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
         title="Centres TCF en Afrique : Sénégal, Cameroun, Côte d'Ivoire…",
         desc="Les centres TCF agréés au Sénégal, en Côte d'Ivoire, au Cameroun, en RDC, au Congo, au Bénin, au Togo, en Guinée, au Gabon, au Mali, en Mauritanie, à Maurice.",
         h1="Centres TCF en Afrique subsaharienne et à Maurice : les centres agréés, pays par pays",
         intro="""Dans les pays francophones d'Afrique, le TCF — Canada, Québec, IRN ou tout public — se passe dans les
Instituts français et les Alliances françaises agréés par France Éducation international : <strong>%(n)d
centres dans douze pays</strong> au 19 septembre 2026, dont %(so)d avec des sessions sur ordinateur.
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
              ("Où passer le TCF Canada en Côte d'Ivoire ?", "Dans le seul centre agréé du pays au 19 septembre 2026, à Abidjan (Institut français) : les places y sont comptées, réservez dès l'ouverture des inscriptions."),
              ("Le TCF Canada passé en Afrique est-il accepté par IRCC ?", "Oui, dès lors qu'il est passé dans un centre agréé par France Éducation international : l'attestation est la même partout dans le monde et vaut deux ans."),
              ("Comment vérifier qu'un centre est agréé ?", "En le cherchant dans la liste officielle de FEI, par pays. Un organisme absent de cette liste ne peut pas délivrer d'attestation TCF, quel que soit son site.")],
         also=[("/centres/tcf-maroc/", "Centres TCF au Maroc", "Les 16 centres agréés."),
               ("/centres/tcf-algerie/", "Centres TCF en Algérie", "Les cinq antennes de l'Institut français."),
               ("/centres/tcf-tunisie/", "Centres TCF en Tunisie", "Les 14 centres agréés."),
               ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", "")]),
    dict(slug="tcf-europe", files=["tcf_belgique", "tcf_suisse", "tcf_royaume_uni"], layout="multi", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF en Belgique, Suisse et Royaume-Uni",
         title="Centres TCF en Belgique, en Suisse et au Royaume-Uni",
         desc="Les centres TCF agréés en Belgique, en Suisse et au Royaume-Uni — Bruxelles, Liège, Genève, Londres… — avec adresse, téléphone, e-mail et site.",
         h1="Centres TCF en Belgique, en Suisse et au Royaume-Uni : les centres agréés",
         intro="""Hors de France, en Europe, le TCF se passe dans les <strong>%(n)d centres agréés</strong> par France
Éducation international en Belgique, en Suisse et au Royaume-Uni au 19 septembre 2026 — Alliances
françaises et instituts —, dont %(so)d avec des sessions sur ordinateur. Voici leurs coordonnées,
pays par pays. Pour un dossier de naturalisation française, c'est le TCF IRN qu'il faut y demander ;
pour Entrée express, le TCF Canada.""",
         facts=["<strong>12 centres</strong> : 2 en Belgique, 7 en Suisse, 3 au Royaume-Uni (liste FEI du 19 septembre 2026).",
                "Le réseau français reste le plus dense d'Europe : <strong>251 centres</strong>, dont plusieurs près des frontières belge, suisse et luxembourgeoise.",
                "Chaque centre choisit ses déclinaisons, ses dates et son tarif.",
                "Le TEF relève du réseau du Français des affaires, avec son propre annuaire.",
                "20 à 30 jours entre deux passations ; attestation valable deux ans.",
                "Un organisme absent de cette liste n'est pas agréé."],
         stat4=("3", "pays", "Belgique, Suisse, Royaume-Uni"), cities_note="de Bruxelles à Londres",
         liste_label="pays par pays", decl="Canada, Québec, IRN, tout public, DAP",
         guides=[("/centres/tcf-france/", "Centres TCF en France : les 251 centres agréés", "Pour les frontaliers, le réseau le plus dense."),
                 ("/blog/ou-passer-le-tcf-irn-en-france/", "Où passer le TCF IRN en France ?", ""),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF par pays (FEI)", "https://www.france-education-international.fr/centres-d-examen/liste?type-centre=tcf"), ("Carte des centres TCF", FEI_CARTE % "tcf")],
         sources_text="type « TCF », filtres Belgique, Suisse et Royaume-Uni",
         faq=[("Où passer le TCF en Belgique ?", "Dans l'un des deux centres agréés au 19 septembre 2026, à Bruxelles et Liège, listés ci-dessous — ou dans un centre français proche de la frontière, à Lille par exemple."),
              ("Où passer le TCF en Suisse ?", "Dans l'un des sept centres agréés listés ci-dessous ; cinq proposent des sessions sur ordinateur."),
              ("Où passer le TCF à Londres ?", "Dans l'un des trois centres agréés du Royaume-Uni listés ci-dessous, dont l'Institut français du Royaume-Uni à Londres."),
              ("Le TCF IRN passé à l'étranger est-il accepté pour la naturalisation française ?", "Oui : l'attestation est délivrée par France Éducation international quel que soit le centre, et l'arrêté du 22 décembre 2025 n'exige que la passation en présentiel dans un centre agréé."),
              ("Comment vérifier qu'un centre est agréé ?", "Dans la liste officielle de FEI, par pays ; un organisme absent de cette liste ne peut pas délivrer d'attestation TCF.")],
         also=[("/centres/tcf-france/", "Centres TCF en France", "Les 251 centres agréés, région par région."),
               ("/tcf-irn/", "TCF IRN : le test de français pour votre naturalisation", ""),
               ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", ""),
               ("/blog/difference-tcf-tef/", "TCF ou TEF : les 9 versions comparées", "")]),
    dict(slug="tcf-ameriques", files=["tcf_etats_unis", "tcf_bresil", "tcf_mexique", "tcf_colombie", "tcf_haiti"], layout="multi", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF aux États-Unis et en Amérique latine",
         title="Centres TCF aux États-Unis, au Brésil, au Mexique…",
         desc="Les 51 centres TCF agréés aux États-Unis, au Brésil, au Mexique, en Colombie et en Haïti — New York, São Paulo, Mexico, Bogotá… — avec leurs contacts.",
         h1="Centres TCF aux États-Unis et en Amérique latine : les centres agréés, pays par pays",
         intro="""Sur le continent américain hors Canada, le TCF se passe dans les <strong>%(n)d centres agréés</strong>
par France Éducation international aux États-Unis, au Brésil, au Mexique, en Colombie et en Haïti au
19 septembre 2026 — presque tous des Alliances françaises —, dont %(so)d avec des sessions sur
ordinateur. Pour un candidat à Entrée express installé aux États-Unis, c'est souvent plus simple que
de traverser la frontière vers Toronto ou Vancouver, où les sessions affichent complet en minutes.""",
         facts=["<strong>51 centres dans 5 pays</strong> : États-Unis 18, Brésil 14, Mexique 11, Colombie 7, Haïti 1 (liste FEI du 19 septembre 2026).",
                "Presque tous sont des <strong>Alliances françaises</strong> ; l'inscription se fait sur leur site.",
                "Le TCF Canada passé aux États-Unis est accepté par IRCC comme partout : même attestation, même validité de deux ans.",
                "Tarifs en monnaie locale, fixés par chaque centre.",
                "20 à 30 jours entre deux passations.",
                "Le TEF Canada relève du réseau du Français des affaires."],
         stat4=("5", "pays", "États-Unis, Brésil, Mexique, Colombie, Haïti"), cities_note="de New York à Bogotá",
         liste_label="pays par pays", decl="Canada, Québec, tout public, DAP",
         guides=[("/blog/ou-passer-le-tcf-canada-au-canada/", "Où passer le TCF Canada au Canada ?", "Les 47 centres canadiens et la méthode pour obtenir une place."),
                 ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", ""),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF par pays (FEI)", "https://www.france-education-international.fr/centres-d-examen/liste?type-centre=tcf"), ("Carte des centres TCF", FEI_CARTE % "tcf")],
         sources_text="type « TCF », filtres États-Unis, Brésil, Mexique, Colombie et Haïti",
         faq=[("Où passer le TCF Canada aux États-Unis ?", "Dans l'un des 18 centres agréés listés ci-dessous, presque tous des Alliances françaises, quinze avec des sessions sur ordinateur."),
              ("Où passer le TCF au Brésil ?", "Dans l'un des 14 centres agréés — Alliances françaises de São Paulo, Rio de Janeiro, Brasília et d'autres villes — listés ci-dessous."),
              ("Où passer le TCF au Mexique ?", "Dans l'un des 11 centres agréés listés ci-dessous, à Mexico et en région."),
              ("Le TCF Canada passé hors du Canada est-il accepté par IRCC ?", "Oui : l'attestation est délivrée par France Éducation international quel que soit le centre agréé, et vaut deux ans."),
              ("Comment vérifier qu'un centre est agréé ?", "Dans la liste officielle de FEI, par pays.")],
         also=[("/centres/tcf-canada/", "Centres TCF au Canada", "Les 47 centres agréés, par province."),
               ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", ""),
               ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", ""),
               ("/blog/validite-attestation-tcf-tef/", "Validité de l'attestation : deux ans à partir de quand ?", "")]),
    dict(slug="tcf-moyen-orient", files=["tcf_liban", "tcf_emirats_arabes_unis", "tcf_egypte", "tcf_turquie"], layout="multi", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF au Liban, aux Émirats, en Égypte, en Turquie",
         title="Centres TCF au Liban, aux Émirats, en Égypte, en Turquie",
         desc="Les 16 centres TCF agréés au Liban, aux Émirats arabes unis, en Égypte et en Turquie — Beyrouth, Dubaï, Le Caire, Istanbul… — avec leurs contacts.",
         h1="Centres TCF au Liban, aux Émirats arabes unis, en Égypte et en Turquie",
         intro="""Au Proche et Moyen-Orient, le TCF se passe dans les <strong>%(n)d centres agréés</strong> par France
Éducation international au Liban, aux Émirats arabes unis, en Égypte et en Turquie au 19 septembre
2026 — Instituts français et Alliances françaises —, dont %(so)d avec des sessions sur ordinateur.
Voici leurs coordonnées, pays par pays.""",
         facts=["<strong>16 centres dans 4 pays</strong> : Liban 6, Émirats arabes unis 4, Égypte 3, Turquie 3 (liste FEI du 19 septembre 2026).",
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
               ("/centres/tcf-canada/", "Centres TCF au Canada", "Les 47 centres agréés."),
               ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", ""),
               ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", "")]),
    dict(slug="tcf-inde", files=["tcf_inde"], layout="cities", exam="TCF", accent="accent-tcf",
         crumb="Centres TCF en Inde",
         title="Centres TCF en Inde : les 7 centres agréés, contacts",
         desc="Les sept centres TCF agréés en Inde — Alliances françaises de Delhi, Mumbai, Bangalore, Chennai, Ahmedabad… — avec adresse, téléphone, e-mail et site.",
         h1="Centres TCF en Inde : les 7 centres agréés et leurs contacts",
         intro="""En Inde, le TCF Canada se passe dans l'un des <strong>%(n)d centres agréés</strong> par France Éducation
international au 19 septembre 2026 — les Alliances françaises —, dont %(so)d avec des sessions sur
ordinateur. Voici leurs coordonnées, ville par ville. Le TEF Canada, l'autre test accepté par IRCC,
relève du réseau du Français des affaires, souvent dans les mêmes Alliances.""",
         facts=["<strong>7 centres agréés</strong>, tous des Alliances françaises (liste FEI du 19 septembre 2026), 3 avec des sessions sur ordinateur.",
                "Chaque Alliance fixe ses dates et son tarif ; l'inscription se fait sur son site.",
                "Le TCF Canada passé en Inde est accepté par IRCC comme partout : même attestation, valable deux ans.",
                "20 à 30 jours entre deux passations.",
                "Pour Entrée express, visez le NCLC 7 : 458 en compréhension orale, 453 à l'écrit.",
                "Un organisme absent de cette liste n'est pas agréé."],
         stat4=("7", "Alliances françaises", "de Delhi à Chennai"), cities_note="Delhi, Mumbai, Bangalore…",
         liste_label="ville par ville", decl="Canada, Québec, tout public, DAP",
         guides=[("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", ""),
                 ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", ""),
                 ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub", "")],
         sources_links=[("Liste des centres TCF en Inde", FEI_LISTE % (45, "tcf")), ("Carte des centres TCF", FEI_CARTE % "tcf")],
         sources_text="filtre « Inde », type « TCF »",
         faq=[("Où passer le TCF Canada en Inde ?", "Dans l'une des sept Alliances françaises agréées listées ci-dessous — à Delhi, Mumbai, Bangalore, Chennai, Ahmedabad et d'autres villes."),
              ("Le TCF Canada passé en Inde est-il accepté par IRCC ?", "Oui : l'attestation est délivrée par France Éducation international quel que soit le centre agréé, et vaut deux ans."),
              ("Combien coûte le TCF en Inde ?", "Chaque Alliance fixe son tarif en roupies et le publie sur son site ; il n'existe pas de tarif national."),
              ("TCF Canada ou TEF Canada ?", "Les deux sont acceptés par IRCC ; le TEF relève du réseau du Français des affaires, souvent proposé par les mêmes Alliances. Notre comparatif TCF ou TEF Canada les met côte à côte."),
              ("Comment vérifier qu'un centre est agréé ?", "Dans la liste officielle de FEI, filtre « Inde ».")],
         also=[("/centres/tcf-moyen-orient/", "Centres TCF au Liban, aux Émirats, en Égypte, en Turquie", ""),
               ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", ""),
               ("/blog/ou-passer-le-tcf-canada-au-canada/", "Où passer le TCF Canada au Canada ?", ""),
               ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", "")]),
]


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
    rows = []
    for spec, (n, so, ncity) in pages_built:
        rows.append(f'<tr><td><a href="/centres/{spec["slug"]}/">{esc(spec["crumb"])}</a></td><td><strong>{n}</strong></td><td>{so}</td><td>{ncity}</td></tr>')
    table = ('<div class="tablewrap">\n<table>\n<caption>Les listes de centres publiées sur ce site, d\'après la liste officielle de France Éducation international du 19 septembre 2026.</caption>\n'
             '<thead><tr><th>Liste</th><th>Centres</th><th>Sur ordinateur</th><th>Villes</th></tr></thead>\n<tbody>\n' + "\n".join(rows) + "\n</tbody>\n</table>\n</div>")
    total = sum(n for _, (n, _, _) in pages_built)
    cards = "\n".join(
        f'<div class="card card-link"><span class="tag">{esc(spec["exam"])}</span><h3><a href="/centres/{spec["slug"]}/">{esc(spec["crumb"])}</a></h3><p>{n} centres · {so} sur ordinateur · {ncity} villes</p></div>'
        for spec, (n, so, ncity) in pages_built)
    body = f"""
{stats([(str(total), "centres listés", "avec leurs contacts"), ("32", "pays", "sur les listes FEI"), ("12", "listes", "par pays ou région"), ("19/09", "date de la lecture", "de la liste FEI")])}

<h2 id="listes">Les listes, par examen et par pays</h2>
<div class="grid c2 guides">
{cards}
</div>

{table}

<h2 id="villes">Les guides par ville</h2>
<p>Pour {sum(len(villes_of(k)) for k in VILLES_KEY.values())} grandes villes, une page réunit les centres agréés avec leurs
contacts, ce que leurs sites affichaient le 17 septembre 2026 — déclinaisons, prix, dates — et la
procédure d'inscription du pays.</p>
{villes_hub()}

<h2 id="methode">D'où viennent ces listes</h2>
<p>Toutes reprennent la <strong>liste officielle des centres d'examen de France Éducation
international</strong> — DELF-DALF, TCF et examen civique —, lue pays par pays le 19 septembre
2026, avec les coordonnées que FEI publie : adresse, téléphone, adresse e-mail générique, site.
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
        "title": "Centres d'examen DELF, TCF et examen civique : l'annuaire",
        "desc": "830 centres agréés par FEI dans 32 pays, avec adresse, téléphone, e-mail et site : TCF en France, au Canada, au Maghreb, en Afrique, en Europe, aux Amériques.",
        "og_title": "Centres d'examen DELF, TCF et examen civique : l'annuaire", "og_desc": "830 centres agréés dans 32 pays, avec leurs contacts, d'après la liste officielle de FEI.",
        "h1": "Centres d'examen DELF, TCF et examen civique : l'annuaire des centres agréés",
        "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": 4,
        "intro": f"""Tous les examens de ce site se passent dans un <strong>centre agréé</strong> — par France Éducation
international pour le DELF, le DALF, le TCF et l'examen civique. Cet annuaire reprend sa liste
officielle, lue le 19 septembre 2026 : <strong>{total} centres dans 32 pays</strong>, avec l'adresse,
le téléphone, l'e-mail et le site de chacun, classés par pays, région et ville. Choisissez votre
liste, puis vérifiez sur le site du centre la déclinaison, la date et le prix.""",
        "facts": [f"<strong>{total} centres</strong> avec leurs contacts, d'après la liste officielle de FEI du 19 septembre 2026.",
                  "France : <strong>251 centres TCF</strong>, <strong>143 centres DELF-DALF</strong>, <strong>245 centres d'examen civique</strong>.",
                  "Canada 47 · Maroc 16 · Tunisie 14 · Algérie 5 · Afrique subsaharienne 23 · Europe 12 · Amériques 51 · Moyen-Orient 16 · Inde 7.",
                  "Chaque liste dit qu'un centre est agréé, pas quelle déclinaison il organise : à vérifier sur son site.",
                  "Les prix et dates sont ceux du centre ; nos guides « Où passer » les ont relevés pour les principaux.",
                  "Un organisme absent de ces listes n'est pas agréé."],
        "toc": [("listes", "Les listes, par examen et par pays"), ("villes", "Les guides par ville"), ("methode", "D'où viennent ces listes"), ("regles", "Trois règles avant d'appeler un centre")],
        "body": body,
        "cta_h2": "Le centre vous donne la date ; le score, c'est vous",
        "cta_p": """Une session se paie en entier et se repasse après un délai. Les examens blancs de l'app
«&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent le format officiel de chaque déclinaison, avec
la notation du vrai test et la correction IA de l'écrit et de l'oral.""",
        "faq": [("Comment trouver un centre d'examen près de chez moi ?", "Ouvrez la liste de votre pays ci-dessus : les centres y sont classés par région ou par ville, avec adresse, téléphone, e-mail et site. Pour un autre pays, la liste officielle de France Éducation international se filtre par pays."),
                ("Ces listes sont-elles officielles ?", "Elles reproduisent la liste officielle de France Éducation international, lue le 19 septembre 2026, avec les coordonnées que FEI publie. FEI agrée et retire des centres au fil de l'année : en cas de doute, sa liste en ligne fait foi."),
                ("Un centre TCF fait-il passer le TCF Canada ?", "Pas forcément : chaque centre choisit ses déclinaisons — Canada, Québec, IRN, tout public. La liste de FEI ne le précise pas ; le site du centre, si. Nos guides « Où passer » l'ont vérifié pour les principaux centres."),
                ("Où sont les centres TEF ?", "Le TEF relève du Français des affaires (CCI Paris Île-de-France), qui publie son propre annuaire « Trouver un centre agréé », tous pays confondus."),
                ("Peut-on passer ces examens en ligne ?", "Non. DELF, DALF, TCF et examen civique se passent en présentiel, dans un centre agréé, sur convocation et avec contrôle d'identité. Toute offre « à distance » est une fraude.")],
        "also": [("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ? Le hub des guides", "Prix relevés, dates de session, pas-à-pas d'inscription, pays par pays."),
                 ("/blog/prix-tcf-tef/", "Combien coûte vraiment le TCF ou le TEF ?", "Aucun tarif national : les prix relevés centre par centre."),
                 ("/blog/diplome-ou-test-delf-tcf/", "Diplôme ou test : lequel vous faut-il ?", ""),
                 ("/examens-blancs/", "Examens blancs au format officiel", "")],
        "sources": """<strong>Sources.</strong> Listes et carte des centres d'examen de France Éducation international
(DELF-DALF, TCF, examen civique), lues pays par pays le 19 septembre 2026 ; annuaire « Trouver un
centre agréé » du Français des affaires. Chaque liste cite son filtre et sa date.""",
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
