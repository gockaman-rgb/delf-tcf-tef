#!/usr/bin/env python3
"""Pages pays : le TCF (dont le TCF Canada) et le DELF-DALF aux États-Unis, au Royaume-Uni, en
Espagne, au Mexique, en Colombie, en Argentine, au Chili, au Pérou et en Équateur (08/10/2026).

Chaque page réunit ce que l'annuaire et les guides séparent ailleurs : la liste officielle de France
Éducation international lue le 8 octobre 2026 (data/<tcf|delf>_<pays>.json, produits par
data/parse_fei_v2.py), ce que nous avons relevé ce jour-là sur le site de chaque centre — déclinaisons,
prix, dates —, la procédure d'inscription du pays et une FAQ. Le texte rédigé vit dans
pays_config.py ; ce script l'assemble et rend les cartes des centres.

Usage : python3 _build/make_pays.py [--force]
        python3 _build/make_pays.py --keys tcf_etats_unis   # clés des centres, pour la config
"""

import os
import re
import sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from article_template import build  # noqa: E402
from make_centres import esc, load, slug, stats  # noqa: E402

DATE = "2026-10-08"
DATE_FR = "8 octobre 2026"
FEI_LISTE = "https://www.france-education-international.fr/centres-d-examen/liste?pays=%s&type-centre=%s"
FEI_CARTE = "https://www.france-education-international.fr/centres-d-examen/carte?type-centre=%s"
PAYS_ID = {"États-Unis": 113, "Royaume-Uni": 89, "Espagne": 70, "Mexique": 30, "Colombie": 21,
           "Argentine": 15, "Chili": 20, "Pérou": 34, "Équateur": 25}

# ---------------------------------------------------------------------------
# Téléphones : FEI écrit les numéros de toutes les façons (« 1-404-875-1211 », « 917007720 »,
# « 0054-9-341-238-843 »). On n'en fait un lien que si le numéro national retrouvé a une longueur
# possible dans le pays ; sinon il s'affiche tel que FEI l'écrit, sans lien plutôt qu'avec un faux.
# ---------------------------------------------------------------------------
PHONE = {"États-Unis": ("1", {10}), "Royaume-Uni": ("44", {9, 10}), "Espagne": ("34", {9}),
         "Mexique": ("52", {10}), "Colombie": ("57", {10}), "Argentine": ("54", {10, 11}),
         "Chili": ("56", {9}), "Pérou": ("51", {8, 9}), "Équateur": ("593", {8, 9})}
BAD_PHONES = {"999999889"}   # numéro de remplissage (AF Concepción, liste DELF)


def national(phone, country):
    d = re.sub(r"\D", "", re.split(r"\s*/\s*", phone)[0])
    if not d or d in BAD_PHONES:
        return ""
    cc, lens = PHONE[country]
    if d.startswith("00"):
        d = d[2:]
    for n in ([d[len(cc):]] if d.startswith(cc) else []) + [d]:
        x = n[1:] if n.startswith("0") else n
        if country == "Mexique" and len(x) == 11 and x.startswith("1"):
            x = x[1:]                      # ancien préfixe mobile « 1 » après le 52
        if not x or x[0] == "0" or len(x) not in lens:
            continue
        if country == "Argentine" and (len(x) == 11) != x.startswith("9"):
            continue                       # 11 chiffres = mobile « 9 » + 10 ; 10 chiffres ne commencent pas par 9
        if country in ("Pérou", "Équateur") and len(x) == 9 and not x.startswith("9"):
            continue                       # 9 chiffres = mobile, qui commence par 9
        return x
    return ""


def phone_html(phone, country):
    x = national(phone, country)
    if not x:
        return esc(phone)
    cc = PHONE[country][0]
    groups = {8: (4, 4), 9: (3, 3, 3), 10: (3, 3, 4), 11: (1, 2, 4, 4)}[len(x)]
    parts, i = [], 0
    for g in groups:
        parts.append(x[i:i + g])
        i += g
    shown = f"+{cc} " + " ".join(parts)
    return f'<a href="tel:+{cc}{x}">{shown}</a>'


# ---------------------------------------------------------------------------
# Villes et régions. FEI écrit la même ville de plusieurs façons (« Sevilla » / « Séville »,
# « CDMX » / « Ville de Mexico ») : CITY donne le nom affiché, REGION la région où on la range.
# ---------------------------------------------------------------------------
CITY = {
    "États-Unis": {"Atlanta (Géorgie)": "Atlanta", "Bingham Farms (Detroit) (Michigan)": "Detroit (Bingham Farms)",
                   "Cambridge MA (Massachusetts)": "Cambridge", "Chicago (Illinois)": "Chicago", "Denver (Colorado)": "Denver",
                   "Houston (Texas)": "Houston", "Kansas City (Kansas)": "Kansas City", "Los Angeles (Californie)": "Los Angeles",
                   "Mercer Island (Washington)": "Mercer Island", "Middletown (Connecticut)": "Middletown",
                   "New-York (New York)": "New York", "Pasadena (Californie)": "Pasadena",
                   "Philadelphie (Pennsylvanie)": "Philadelphie", "San Diego (Californie)": "San Diego",
                   "San Francisco (Californie)": "San Francisco", "Seattle (Washington)": "Seattle",
                   "Washington DC (District de Columbia)": "Washington", "Washington,": "Washington",
                   "Philadelphia": "Philadelphie", "New Orleans": "La Nouvelle-Orléans", "St. Louis": "Saint-Louis",
                   "Waterown": "Watertown", "Saint Petersburg": "St. Petersburg"},
    "Royaume-Uni": {"Londres": "Londres", "London": "Londres", "Edinburgh": "Édimbourg", "Saint-Hélier": "Saint-Hélier (Jersey)",
                    "St Helier, Jersey": "Saint-Hélier (Jersey)"},
    "Espagne": {"Barcelona": "Barcelone", "Cartagena": "Carthagène", "Cádiz": "Cadix", "Donostia-San Sebastián": "Saint-Sébastien",
                "Girona": "Gérone", "Granada": "Grenade", "Las Palmas De Gran Canaria": "Las Palmas de Gran Canaria",
                "Malaga": "Malaga", "Málaga": "Malaga", "Palma": "Palma de Majorque", "Pamplona": "Pampelune",
                "Salamanca": "Salamanque", "Santa Cruz De Tenerife": "Santa Cruz de Tenerife",
                "Santiago De Compostela": "Saint-Jacques-de-Compostelle", "Santiago de Compostela": "Saint-Jacques-de-Compostelle",
                "Sevilla": "Séville", "Valencia": "Valence"},
    "Mexique": {"Aguascalientes, Ags.": "Aguascalientes", "Guadalajara, Jalisco": "Guadalajara", "Mexico DF": "Mexico",
                "CDMX": "Mexico", "Ciudad De México": "Mexico", "Ville de Mexico": "Mexico",
                "Mineral de la Reforma, Hidalgo": "Pachuca (Mineral de la Reforma)",
                "Mineral De La Reforma": "Pachuca (Mineral de la Reforma)", "San Luis Potosi": "San Luis Potosí",
                "Tepic - NAYARIT": "Tepic", "Tepic": "Tepic", "Cancun": "Cancún", "Atizapan De Zaragoza": "Atizapán de Zaragoza",
                "Naucalpan De Juárez": "Naucalpan de Juárez", "Oaxaca De Juárez": "Oaxaca", "San Cristóbal De Las Casas": "San Cristóbal de las Casas",
                "San Francisco Coacalco": "Coacalco", "San Miguel De Allende": "San Miguel de Allende",
                "San Pedro Garza García": "Monterrey (San Pedro Garza García)", "Tecamác": "Tecámac",
                "Tuxtla Gutierrez": "Tuxtla Gutiérrez", "Villa De Álvarez": "Villa de Álvarez", "XALISCO": "Xalisco"},
    "Colombie": {"Barranquilla, Atlantico": "Barranquilla", "Bogota": "Bogotá", "Carthagène des Indes": "Carthagène des Indes",
                 "Cartagena de Indias": "Carthagène des Indes", "Cucuta": "Cúcuta", "Medellin": "Medellín"},
    "Argentine": {"Cordoba": "Córdoba", "Concepción Del Uruguay": "Concepción del Uruguay", "Lujan": "Luján",
                  "Mar Del Plata": "Mar del Plata", "Olavarria": "Olavarría", "San Carlos De Bariloche": "San Carlos de Bariloche",
                  "San Salvador De Jujuy": "San Salvador de Jujuy"},
    "Chili": {"Concepcion": "Concepción"},
    "Pérou": {},
    "Équateur": {"Guayaquil, Guayas": "Guayaquil"},
}

REGION = {
    "États-Unis": {"Atlanta": "Géorgie", "College Park": "Géorgie", "Detroit (Bingham Farms)": "Michigan",
                   "Cambridge": "Massachusetts", "Watertown": "Massachusetts", "Chicago": "Illinois", "Denver": "Colorado",
                   "Houston": "Texas", "Dallas": "Texas", "Austin": "Texas", "Fort Worth": "Texas", "Kansas City": "Kansas",
                   "Los Angeles": "Californie", "Pasadena": "Californie", "San Diego": "Californie", "San Francisco": "Californie",
                   "Mercer Island": "État de Washington", "Seattle": "État de Washington", "Middletown": "Connecticut",
                   "New York": "État de New York", "Mamaroneck": "État de New York", "Philadelphie": "Pennsylvanie",
                   "Pittsburgh": "Pennsylvanie", "Washington": "District de Columbia", "Baltimore": "Maryland",
                   "Fort Washington": "Maryland", "Charlotte": "Caroline du Nord", "Durham": "Caroline du Nord",
                   "Columbia": "Caroline du Sud", "Miami": "Floride", "St. Petersburg": "Floride", "Milwaukee": "Wisconsin",
                   "Minneapolis": "Minnesota", "La Nouvelle-Orléans": "Louisiane", "Opelousas": "Louisiane",
                   "Portland": "Oregon", "Providence": "Rhode Island", "South Freeport": "Maine", "Saint-Louis": "Missouri",
                   "San Juan": "Porto Rico"},
    "Espagne": {"A Coruña": "Galice", "Vigo": "Galice", "Saint-Jacques-de-Compostelle": "Galice",
                "Barcelone": "Catalogne", "Gérone": "Catalogne", "Granollers": "Catalogne",
                "Bilbao": "Pays basque", "Saint-Sébastien": "Pays basque", "Vitoria-Gasteiz": "Pays basque",
                "Burgos": "Castille-et-León", "Salamanque": "Castille-et-León", "Valladolid": "Castille-et-León",
                "Carthagène": "Région de Murcie", "Ciudad Real": "Castille-La Manche", "Cáceres": "Estrémadure",
                "Cadix": "Andalousie", "Grenade": "Andalousie", "Malaga": "Andalousie", "Séville": "Andalousie",
                "Gijón": "Asturies", "Oviedo": "Asturies", "Las Palmas de Gran Canaria": "Canaries",
                "Santa Cruz de Tenerife": "Canaries", "Logroño": "La Rioja", "Madrid": "Communauté de Madrid",
                "Palma de Majorque": "Baléares", "Pampelune": "Navarre", "Santander": "Cantabrie",
                "Saragosse": "Aragon", "Valence": "Communauté valencienne"},
    "Mexique": {"Aguascalientes": "Aguascalientes", "Atizapán de Zaragoza": "État de Mexico", "Huixquilucan": "État de Mexico",
                "Naucalpan de Juárez": "État de Mexico", "Coacalco": "État de Mexico", "Tecámac": "État de Mexico",
                "Texcoco": "État de Mexico", "Toluca": "État de Mexico", "Mexico": "Mexico (CDMX)",
                "Cancún": "Quintana Roo", "Chetumal": "Quintana Roo", "Chihuahua": "Chihuahua",
                "Ciudad Victoria": "Tamaulipas", "Nuevo Laredo": "Tamaulipas", "Tampico": "Tamaulipas",
                "Cuernavaca": "Morelos", "Culiacán": "Sinaloa", "Durango": "Durango",
                "Guadalajara": "Jalisco", "Zapopan": "Jalisco", "Puerto Vallarta": "Jalisco",
                "Guanajuato": "Guanajuato", "Irapuato": "Guanajuato", "León": "Guanajuato", "San Miguel de Allende": "Guanajuato",
                "Hermosillo": "Sonora", "Ixmiquilpan": "Hidalgo", "Pachuca (Mineral de la Reforma)": "Hidalgo",
                "La Paz": "Basse-Californie du Sud", "Mexicali": "Basse-Californie", "Tijuana": "Basse-Californie",
                "Monterrey": "Nuevo León", "Monterrey (San Pedro Garza García)": "Nuevo León",
                "Morelia": "Michoacán", "Mérida": "Yucatán", "Oaxaca": "Oaxaca", "Petatlán": "Guerrero",
                "Puebla": "Puebla", "Querétaro": "Querétaro", "Saltillo": "Coahuila", "Torreón": "Coahuila",
                "San Cristóbal de las Casas": "Chiapas", "Tuxtla Gutiérrez": "Chiapas", "San Luis Potosí": "San Luis Potosí",
                "Tlaxcala": "Tlaxcala", "Veracruz": "Veracruz", "Xalapa": "Veracruz", "Villa de Álvarez": "Colima",
                "Villahermosa": "Tabasco", "Xalisco": "Nayarit", "Tepic": "Nayarit", "Zacatecas": "Zacatecas"},
    "Argentine": {"Buenos Aires": "Ville de Buenos Aires", "Resistencia": "Chaco",
                  "Bahía Blanca": "Province de Buenos Aires", "Bernal": "Province de Buenos Aires",
                  "Luján": "Province de Buenos Aires", "Mar del Plata": "Province de Buenos Aires",
                  "Mercedes": "Province de Buenos Aires", "Olavarría": "Province de Buenos Aires",
                  "Pehuajó": "Province de Buenos Aires", "Tandil": "Province de Buenos Aires",
                  "Concepción del Uruguay": "Entre Ríos", "Córdoba": "Córdoba", "Mendoza": "Mendoza", "San Rafael": "Mendoza",
                  "Neuquén": "Neuquén", "Posadas": "Misiones", "Rafaela": "Santa Fe", "Rosario": "Santa Fe",
                  "Santa Fe": "Santa Fe", "Venado Tuerto": "Santa Fe", "Salta": "Salta",
                  "San Carlos de Bariloche": "Río Negro", "San Juan": "San Juan", "San Luis": "San Luis",
                  "San Salvador de Jujuy": "Jujuy", "Santa Rosa": "La Pampa", "Tucumán": "Tucumán", "Ushuaia": "Terre de Feu"},
}


# Centres que FEI range sous une autre ville que la leur (relu le 08/10/2026).
CITY_BY_NAME = {("Argentine", "Alliance Française de Resistencia"): "Resistencia"}


def city_of(c, country):
    if (country, c["name"]) in CITY_BY_NAME:
        return CITY_BY_NAME[(country, c["name"])]
    raw = re.sub(r"\s+", " ", c["city"]).strip()
    fixed = CITY.get(country, {}).get(raw)
    if fixed is None:
        fixed = CITY.get(country, {}).get(raw.rstrip(","), raw.rstrip(","))
        fixed = re.sub(r"\s*\(.*?\)\s*$", "", fixed) if country == "États-Unis" else fixed
    return c.get("city_override") or fixed


def ckey(c):
    """Clé stable d'un centre dans la config : ville affichée + nom, en slug."""
    return slug(c["_city"] + " " + c["name"])


# ---------------------------------------------------------------------------
# Rendu
# ---------------------------------------------------------------------------
def host(u):
    return re.sub(r"^https?://(www\.)?", "", u).split("/")[0]


# Noms que la découpe « Ville - Centre » de FEI rend mal (affichage seulement : les clés ne bougent pas).
NAME_FIX = {("Mexique", "NAYARIT - Colegio de ciencas y letras de Tepic"): "Colegio de Ciencias y Letras de Tepic",
            ("Royaume-Uni", "Leeds - AF"): "Alliance française de Leeds",
            ("Espagne", "Pampelune, Université Publique de Navarre"): "Université publique de Navarre"}


def card(c, country, spec):
    k = ckey(c)
    lines = []
    if c["address"]:
        lines.append(f'<p class="addr">{esc(c["address"])}</p>')
    if c["phone"] and re.sub(r"\D", "", c["phone"]) not in BAD_PHONES:
        lines.append(f'<p class="contact">{phone_html(c["phone"], country)}</p>')
    for e in c["emails"][:2]:
        lines.append(f'<p class="contact"><a href="mailto:{esc(e)}">{esc(e)}</a></p>')
    # Site corrigé quand celui de FEI est mort, détourné ou périmé (relevé du 08/10/2026) ; "" = pas de lien.
    u = spec.get("urls", {}).get(k, c["url"].strip().rstrip("\ufeff"))
    if u:
        u = u if u.startswith("http") else "http://" + u
        lines.append(f'<p class="contact"><a href="{esc(u)}" rel="noopener nofollow">{esc(host(u))}</a></p>')
    note = spec.get("notes", {}).get(k)
    if note:
        lines.append(f'<p class="contact"><em>{note}</em></p>')
    badges = []
    if spec["exam"] == "tcf":
        badges.append('<span class="badge ok">sur ordinateur</span>' if c["so"] else '<span class="badge part">papier</span>')
    for kind, label in spec.get("badges", {}).get(k, []):
        badges.append(f'<span class="badge {kind}">{label}</span>')
    if badges:
        lines.append('<p class="badges">' + " ".join(badges) + "</p>")
    name = NAME_FIX.get((country, c["name"]), c["name"])
    return f'<div class="card centre"><h4>{esc(name)}</h4>\n' + "\n".join(lines) + "</div>"


_USED = set()


def uniq(cid):
    base, k = cid, 2
    while cid in _USED:
        cid = f"{base}-{k}"
        k += 1
    _USED.add(cid)
    return cid


def by_city(centres):
    cities = OrderedDict()
    for c in sorted(centres, key=lambda x: (slug(x["_city"]), x["name"])):
        cities.setdefault(c["_city"], []).append(c)
    return cities


def city_blocks(centres, country, spec, level):
    out = []
    for city, cs in by_city(centres).items():
        n = f' <span class="count">({len(cs)})</span>' if len(cs) > 1 else ""
        out.append(f'<h{level} id="{uniq(slug(city))}">{esc(city)}{n}</h{level}>')
        out.append('<div class="grid c2 centres">\n' + "\n".join(card(c, country, spec) for c in cs) + "\n</div>")
    return "\n".join(out)


def list_section(d, spec):
    """La liste : par région (h2) puis ville (h3), ou par ville (h2) pour les petits pays."""
    country, centres = d["country"], d["centres"]
    index, body = [], []
    if spec.get("layout") == "regions":
        regs = OrderedDict()
        for c in centres:
            regs.setdefault(REGION[country][c["_city"]], []).append(c)
        order = sorted(regs, key=lambda r: (-len(regs[r]), r)) if spec.get("region_sort") == "count" else sorted(regs, key=slug)
        for r in order:
            cs = regs[r]
            rid = uniq("region-" + slug(r))
            index.append((rid, f"{r} ({len(cs)})"))
            plural = "s" if len(cs) > 1 else ""
            body.append(f'<h2 id="{rid}">{esc(r)} — {len(cs)} centre{plural}</h2>\n' + city_blocks(cs, country, spec, 3))
    else:
        for city, cs in by_city(centres).items():
            cid = uniq(slug(city))
            index.append((cid, f"{city} ({len(cs)})" if len(cs) > 1 else city))
            n = f' <span class="count">({len(cs)})</span>' if len(cs) > 1 else ""
            body.append(f'<h2 id="{cid}">{esc(city)}{n}</h2>\n<div class="grid c2 centres">\n'
                        + "\n".join(card(c, country, spec) for c in cs) + "\n</div>")
    return "\n\n".join(body), index


def chips(index):
    return '<div class="chips index">\n' + "\n".join(f'<a class="chip" href="#{i}">{esc(t)}</a>' for i, t in index) + "\n</div>"


def org_block(d, spec):
    o = d.get("org")
    if not o:
        return ""
    if "org_url" in spec:                 # site de l'organisme mort ou périmé : corrigé, ou "" = pas de lien
        o = dict(o, url=spec["org_url"])
    parts = [f"<strong>{esc(o['name'])}</strong>" + (f" ({esc(o['city'])})" if o["city"] else "")]
    if o["address"]:
        parts.append(esc(o["address"]))
    if o["url"] and "@" not in o["url"]:
        parts.append(f'<a href="{esc(o["url"])}" rel="noopener nofollow">{esc(host(o["url"]))}</a>')
    return ("<p>Le DELF et le DALF y sont pilotés par un <strong>organisme de gestion centrale</strong>, que la liste de FEI "
            "nomme à part des centres : " + " · ".join(parts) + ". C'est lui qui arrête le calendrier national des sessions ; "
            "les candidats, eux, s'inscrivent auprès d'un centre.</p>")


class _Safe(dict):
    def __missing__(self, k):
        return "{" + k + "}"


def page(spec):
    _USED.clear()
    _USED.update({"liste", "sources-officielles", "faq", "a-lire"} | {sid for sid, _, _ in spec["sections"]})
    d = load(spec["file"])
    country = d["country"]
    for c in d["centres"]:
        c["_city"] = city_of(c, country)
        if country in REGION and spec.get("layout") == "regions":
            assert c["_city"] in REGION[country], (spec["slug"], c["_city"])
    n = len(d["centres"])
    so = sum(1 for c in d["centres"] if c["so"])
    ncity = len({c["_city"] for c in d["centres"]})
    known = {ckey(c) for c in d["centres"]}
    for k in list(spec.get("badges", {})) + list(spec.get("notes", {})) + list(spec.get("urls", {})):
        assert k in known, (spec["slug"], "clé inconnue", k)
    vals = _Safe(n=n, so=so, ncity=ncity, paper=n - so)
    fmt = lambda s: s.format_map(vals)
    exam_label = "TCF" if spec["exam"] == "tcf" else "DELF-DALF"
    typ = "tcf" if spec["exam"] == "tcf" else "delf_dalf"
    list_html, index = list_section(d, spec)
    sections = "\n\n".join(f'<h2 id="{sid}">{title}</h2>\n{fmt(html)}' for sid, title, html in spec["sections"])
    plural = "s" if n > 1 else ""
    if spec["exam"] == "tcf":
        how = ("« Sur ordinateur » : FEI indique que le centre propose des sessions sur ordinateur ; « papier » : il n'en "
               "déclare pas. Les badges « TCF Canada » viennent de notre relevé du " + DATE_FR + " sur le site de chaque centre.")
    else:
        how = "Les badges viennent de notre relevé du " + DATE_FR + " sur le site de chaque centre."
    lst = f"""<h2 id="liste">{fmt(spec['list_title'])}</h2>
{org_block(d, spec) if spec['exam'] == 'delf' else ''}
<div class="note">
<p><strong>Comment lire cette liste.</strong> Elle reprend la liste officielle des centres agréés par
France Éducation international, consultée le {DATE_FR} — nom, adresse, téléphone, adresse e-mail
générique et site tels que FEI les publie ; quand le site indiqué ne répond plus ou a changé d'adresse, nous
donnons celui que nous avons ouvert ce jour-là. {how} Un organisme absent de cette liste n'est pas agréé.</p>
</div>
{fmt(spec.get('list_intro', ''))}
{chips(index)}

{list_html}"""
    src = FEI_LISTE % (PAYS_ID[country], typ)
    body = f"""
{stats([tuple(fmt(x) for x in s) for s in spec['stats']])}

{sections}

{lst}

<h2 id="sources-officielles">Les listes officielles</h2>
<p><a href="{src}" rel="noopener">Liste des centres {exam_label} — {esc(country)}</a> (FEI) ·
<a href="{FEI_CARTE % typ}" rel="noopener">carte des centres {exam_label}</a>{spec.get('extra_sources_links', '')}. Ces listes
évoluent : FEI ajoute et retire des centres au fil des agréments — la nôtre est datée du {DATE_FR} ;
en cas de doute, la liste de FEI fait foi.</p>
"""
    toc = [(sid, re.sub(r"<[^>]+>", "", title)) for sid, title, _ in spec["sections"]] + \
          [("liste", re.sub(r"<[^>]+>", "", fmt(spec["list_title"])))] + \
          [(i, t.split(" (")[0]) for i, t in index[:spec.get("toc_regions", 8)]] + \
          [("sources-officielles", "Les listes officielles")]
    a = {
        "section": "centres", "section_name": "Centres", "og_slug": "centres-" + spec["slug"],
        "slug": spec["slug"], "accent": "accent-tcf" if spec["exam"] == "tcf" else "accent-delf", "crumb": spec["crumb"],
        "title": fmt(spec["title"]), "desc": fmt(spec["desc"]),
        "og_title": fmt(spec.get("og_title", spec["title"])), "og_desc": fmt(spec.get("og_desc", spec["desc"])),
        "h1": fmt(spec["h1"]),
        "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": spec.get("read", max(5, n // 8)),
        "intro": fmt(spec["intro"]), "facts": [fmt(f) for f in spec["facts"]],
        "toc": toc, "body": body,
        "cta_h2": spec.get("cta_h2", "Le centre vous donne la date ; le niveau, c'est vous"),
        "cta_p": spec.get("cta_p", f"""Une session se paie en entier et se repasse après un délai. Les examens blancs de
l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent le format officiel de chaque
déclinaison — {'TCF Canada, TCF Québec, TCF IRN' if spec['exam'] == 'tcf' else 'DELF B1, DELF B2, DALF C1'} — avec la
notation du vrai test et la correction IA de l'écrit et de l'oral."""),
        "faq": [(fmt(q), fmt(r)) for q, r in spec["faq"]], "also": spec["also"],
        "sources": f"""<strong>Sources.</strong> Liste des centres d'examen de France Éducation international
(filtre « {esc(country)} », type « {exam_label} »), consultée le {DATE_FR} — coordonnées telles que FEI
les publie, adresses e-mail génériques seulement ; {fmt(spec['sources'])} Les prix, dates et modalités
changent sans préavis : vérifiez-les sur le site du centre avant de payer.""",
    }
    assert len(a["title"]) <= 60, (spec["slug"], len(a["title"]), a["title"])
    assert len(a["desc"]) <= 158, (spec["slug"], len(a["desc"]))
    return a, (n, so, ncity)


def specs():
    from pays_config import PAGES
    return PAGES


def counts_of(spec):
    d = load(spec["file"])
    return len(d["centres"]), sum(1 for c in d["centres"] if c["so"]), len({city_of(c, d["country"]) for c in d["centres"]})


def main():
    if "--keys" in sys.argv:
        d = load(sys.argv[sys.argv.index("--keys") + 1])
        for c in d["centres"]:
            c["_city"] = city_of(c, d["country"])
            print(f'{ckey(c):70} {c["url"]}')
        return
    force = "--force" in sys.argv
    build([page(s)[0] for s in specs()], overwrite=force)


if __name__ == "__main__":
    main()
