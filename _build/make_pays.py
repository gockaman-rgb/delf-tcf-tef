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
from make_centres import clean_city, esc, load, province_ca, slug, stats  # noqa: E402

DATE = "2026-10-08"
DATE_FR = "8 octobre 2026"
FEI_LISTE = "https://www.france-education-international.fr/centres-d-examen/liste?pays=%s&type-centre=%s"
FEI_CARTE = "https://www.france-education-international.fr/centres-d-examen/carte?type-centre=%s"
PAYS_ID = {"États-Unis": 113, "Royaume-Uni": 89, "Espagne": 70, "Mexique": 30, "Colombie": 21,
           "Argentine": 15, "Chili": 20, "Pérou": 34, "Équateur": 25, "Canada": 112}

# ---------------------------------------------------------------------------
# Téléphones : FEI écrit les numéros de toutes les façons (« 1-404-875-1211 », « 917007720 »,
# « 0054-9-341-238-843 »). On n'en fait un lien que si le numéro national retrouvé a une longueur
# possible dans le pays ; sinon il s'affiche tel que FEI l'écrit, sans lien plutôt qu'avec un faux.
# ---------------------------------------------------------------------------
PHONE = {"États-Unis": ("1", {10}), "Royaume-Uni": ("44", {9, 10}), "Espagne": ("34", {9}),
         "Mexique": ("52", {10}), "Colombie": ("57", {10}), "Argentine": ("54", {10, 11}),
         "Chili": ("56", {9}), "Pérou": ("51", {8, 9}), "Équateur": ("593", {8, 9}), "Canada": ("1", {10})}
BAD_PHONES = {"999999889"}   # numéro de remplissage (AF Concepción, liste DELF)


def national(phone, country):
    d = re.sub(r"\D", "", re.split(r"\s*/\s*", phone)[0])
    if not d or d in BAD_PHONES:
        return ""
    cc, lens = PHONE[country]
    if d.startswith("00"):
        d = d[2:]
    if country == "Canada" and len(d) == 12 and d.startswith("01"):
        d = d[1:]                          # « 01-514-278-3535 » : un 0 de trop devant l'indicatif
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
    if country == "Canada":
        return clean_city(c["city"])
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
# Langues (08/10/2026) : pages /es/ et /en/. Le français garde ses chaînes à l'octet près ; l'espagnol
# et l'anglais ont leurs gabarits ci-dessous. Villes, régions et provinces se traduisent à l'affichage :
# les clés des centres (ckey) restent celles du français, pour que badges, notes et sites corrigés se
# partagent entre langues.
# ---------------------------------------------------------------------------
def LANG_OF(spec):
    return spec.get("lang", "fr")


def VARIANT(spec):
    return spec.get("variant", {"fr": "fr", "es": "es-419", "en": "en-US"}[LANG_OF(spec)])


DATE_LABEL = {"fr": DATE_FR, "es-ES": "8 de octubre de 2026", "es-419": "8 de octubre de 2026",
              "en-US": "October 8, 2026", "en-GB": "8 October 2026", "en-CA": "8 October 2026"}
OG_LOCALE = {"es-ES": "es_ES", "es-419": "es_LA", "en-US": "en_US", "en-GB": "en_GB", "en-CA": "en_CA"}
LINK_LABEL = {"fr": "Lire en français", "es": "Leer en español", "en": "Read in English"}
HOME_LABEL = {"es": "Inicio", "en": "Home"}


def words(spec):
    v = VARIANT(spec)
    if v.startswith("es"):
        es = v == "es-ES"                  # Espagne : « la web », « convocatoria », « matricularse »
        return dict(centre="centro", centres="centros", so="en ordenador" if es else "en computadora",
                    paper="en papel", nearby="Cerca", org="organismo",
                    web="web" if es else "sitio web", la_web="la web indicada" if es else "el sitio indicado",
                    lo="la" if es else "el", cambio="ha cambiado" if es else "cambió",
                    del_web="de la web" if es else "del sitio web", en_web="en la web" if es else "en el sitio",
                    ses="convocatoria" if es else "sesión", sess="convocatorias" if es else "sesiones",
                    inscriben="se matriculan" if es else "se inscriben")
    if v.startswith("en"):
        us = v == "en-US"
        return dict(centre="center" if us else "centre", centres="centers" if us else "centres", so="computer-based",
                    paper="paper-based", nearby="Nearby", org="organisation" if v == "en-GB" else "organization")
    return dict(centre="centre", centres="centres", so="sur ordinateur", paper="papier", nearby="À proximité", org="organisme")


CITY_T = {
    "en": {"États-Unis": {"Philadelphie": "Philadelphia", "La Nouvelle-Orléans": "New Orleans", "Saint-Louis": "St. Louis"},
           "Royaume-Uni": {"Londres": "London", "Édimbourg": "Edinburgh", "Saint-Hélier (Jersey)": "St Helier (Jersey)"},
           "Canada": {"Montréal": "Montreal", "Québec": "Quebec City", "St. John's, NL": "St. John's", "Sept-Iles": "Sept-Îles"}},
    "es": {"Espagne": {"Barcelone": "Barcelona", "Carthagène": "Cartagena", "Cadix": "Cádiz", "Saint-Sébastien": "San Sebastián",
                       "Gérone": "Girona", "Grenade": "Granada", "Malaga": "Málaga", "Palma de Majorque": "Palma de Mallorca",
                       "Pampelune": "Pamplona", "Salamanque": "Salamanca", "Saint-Jacques-de-Compostelle": "Santiago de Compostela",
                       "Séville": "Sevilla", "Valence": "Valencia", "Saragosse": "Zaragoza"},
           "Mexique": {"Mexico": "Ciudad de México"},
           "Colombie": {"Carthagène des Indes": "Cartagena de Indias"}},
}
REGION_T = {
    "en": {"États-Unis": {"Géorgie": "Georgia", "Californie": "California", "État de Washington": "Washington State",
                          "État de New York": "New York State", "Pennsylvanie": "Pennsylvania", "District de Columbia": "District of Columbia",
                          "Caroline du Nord": "North Carolina", "Caroline du Sud": "South Carolina", "Floride": "Florida",
                          "Louisiane": "Louisiana", "Porto Rico": "Puerto Rico"},
           "Canada": {"Québec": "Quebec", "Colombie-Britannique": "British Columbia", "Nouveau-Brunswick": "New Brunswick",
                      "Nouvelle-Écosse": "Nova Scotia", "Terre-Neuve-et-Labrador": "Newfoundland and Labrador"}},
    "es": {"Espagne": {"Galice": "Galicia", "Catalogne": "Cataluña", "Pays basque": "País Vasco", "Castille-et-León": "Castilla y León",
                       "Région de Murcie": "Región de Murcia", "Castille-La Manche": "Castilla-La Mancha", "Estrémadure": "Extremadura",
                       "Andalousie": "Andalucía", "Asturies": "Asturias", "Canaries": "Canarias", "Communauté de Madrid": "Comunidad de Madrid",
                       "Baléares": "Islas Baleares", "Navarre": "Navarra", "Cantabrie": "Cantabria", "Aragon": "Aragón",
                       "Communauté valencienne": "Comunidad Valenciana"},
           "Mexique": {"Mexico (CDMX)": "Ciudad de México", "État de Mexico": "Estado de México", "Basse-Californie": "Baja California",
                       "Basse-Californie du Sud": "Baja California Sur"},
           "Argentine": {"Ville de Buenos Aires": "Ciudad de Buenos Aires", "Province de Buenos Aires": "Provincia de Buenos Aires",
                         "Terre de Feu": "Tierra del Fuego"}},
}
# Noms de centres que FEI écrit en français : forme locale sur les pages espagnoles (affichage seulement).
NAME_ES = {"Institut français d'Espagne- Délégation de Bilbao": "Institut français de Bilbao",
           "Institut Français d'Espagne - Barcelone": "Institut français de Barcelona",
           "Institut français d'Espagne - Madrid": "Institut français de Madrid",
           "Institut français d'Espagne - Zaragoza": "Institut français de Zaragoza",
           "Institut français de Valence": "Institut français de Valencia",
           "Pampelune, Université Publique de Navarre": "Universidad Pública de Navarra",
           "Univ. d'Estrémadure (Vicerrectorado de Extensión Universitaria)": "Universidad de Extremadura (Vicerrectorado de Extensión Universitaria)",
           "Université de Salamanque": "Universidad de Salamanca", "INSTITUTO DE LENGUA FRANCESA": "Instituto de Lengua Francesa",
           "Institut français Amérique latine": "Instituto Francés de América Latina (IFAL)",
           "Institut français d'Amérique Latine (IFAL)": "Instituto Francés de América Latina (IFAL)",
           "Centre Pachuca Université Autonome": "Universidad Autónoma del Estado de Hidalgo (Centro de Lenguas)",
           "Université Autonome de l'état de Hidalgo": "Universidad Autónoma del Estado de Hidalgo",
           "Proulex - Université de Guadalajara": "Proulex - Universidad de Guadalajara",
           "Alliance Franco-mexicaine de Guanajuato A.C.": "Alianza Franco-Mexicana de Guanajuato A.C.",
           "Université technologique de Chihuahua": "Universidad Tecnológica de Chihuahua",
           "Université La Salle Victoria": "Universidad La Salle Victoria",
           "Université Autonome de Nuevo Leon": "Universidad Autónoma de Nuevo León",
           "Université Technologique de Nuevo Laredo": "Universidad Tecnológica de Nuevo Laredo",
           "Université Technologique de Puebla": "Universidad Tecnológica de Puebla",
           "UNIVERSITÉ TECHNOLOGIQUE DE NAYARIT": "Universidad Tecnológica de Nayarit",
           "NAYARIT - Colegio de ciencas y letras de Tepic": "Colegio de Ciencias y Letras de Tepic",
           "Institut français (Campus France)": "Instituto Francés (Campus France)",
           "Institut français du Chili": "Instituto Francés de Chile", "INSTITUTO FRANCÉS DE CHILE": "Instituto Francés de Chile",
           "ALLIANCE FRANCAISE D'OSORNO": "Alianza Francesa de Osorno"}
NAME_EN = {"Leeds - AF": "Alliance Française de Leeds"}


# Noms de villes en français dans les adresses de FEI (« SW72JR Londres ») : forme locale sur les pages
# traduites. Le Canada garde ses adresses (Montréal, Québec y sont les noms officiels).
ADDR_T = {"en": {"États-Unis": {"Philadelphie": "Philadelphia", "La Nouvelle-Orléans": "New Orleans", "Saint-Louis": "St. Louis"},
                 "Royaume-Uni": {"Londres": "London", "Édimbourg": "Edinburgh", "Saint-Hélier": "St Helier"}},
          "es": {"Espagne": {k: v for k, v in CITY_T["es"]["Espagne"].items()},
                 "Mexique": {"Ville de Mexico": "Ciudad de México"},
                 "Colombie": {"Carthagène des Indes": "Cartagena de Indias"}}}


def disp_addr(addr, country, spec):
    for fr, loc in ADDR_T.get(LANG_OF(spec), {}).get(country, {}).items():
        addr = re.sub(r"(?<![\w-])" + re.escape(fr) + r"(?![\w-])", loc, addr)
    return addr


# Libellés de l'organisme de gestion DELF que FEI écrit en français : forme espagnole (le Chili garde le nom
# de son service, que le texte de la page cite tel quel).
ORG_ES = {"direction pédagogique": "Dirección pedagógica", "Coordination nationale DELF-DALF": "Coordinación nacional DELF-DALF",
          "Gestion Centrale DELF/DALF": "Gestión central DELF-DALF", "Coopération éducative": "Cooperación educativa"}
NAME_ES_WORDS = {"Carthagène": "Cartagena", "la Terre de Feu": "Tierra del Fuego"}


def disp_name(name, country, spec):
    lang = LANG_OF(spec)
    if lang == "es":
        name = NAME_ES.get(name, name)
        name = re.sub(r"(?i)^alliance\s+fran[çc]aise", "Alianza Francesa", name)
        name = re.sub(r"^Alianza francesa", "Alianza Francesa", name).replace(" - Centre ", " - Centro ")
        name = re.sub(r"^Alianza Francesa d['’]\s*", "Alianza Francesa de ", name)
        for fr, es in NAME_ES_WORDS.items():
            name = name.replace(fr, es)
        return name
    if lang == "en":
        return NAME_EN.get(name, name)
    return NAME_FIX.get((country, name), name)


def disp_city(city, country, spec):
    return CITY_T.get(LANG_OF(spec), {}).get(country, {}).get(city, city)


def disp_region(r, country, spec):
    return REGION_T.get(LANG_OF(spec), {}).get(country, {}).get(r, r)


def region_of(c, country):
    return province_ca(c["city"]) if country == "Canada" else REGION[country][c["_city"]]


# ---------------------------------------------------------------------------
# Rendu
# ---------------------------------------------------------------------------
def host(u):
    return re.sub(r"^https?://(www\.)?", "", u).split("/")[0]


# Noms que la découpe « Ville - Centre » de FEI rend mal (affichage seulement : les clés ne bougent pas).
NAME_FIX = {("Mexique", "NAYARIT - Colegio de ciencas y letras de Tepic"): "Colegio de Ciencias y Letras de Tepic",
            ("Royaume-Uni", "Leeds - AF"): "Alliance française de Leeds",
            ("Espagne", "Pampelune, Université Publique de Navarre"): "Université publique de Navarre"}
BOM = chr(0xFEFF)


def card(c, country, spec):
    k = ckey(c)
    W = words(spec)
    lines = []
    addr = c["address"]
    if c.get("cp") or c.get("city_cp"):    # données v1 (Canada, 19/09) : adresse + code postal + ville, comme make_centres
        addr = " ".join(x for x in [c["address"], (c["cp"] + " " + clean_city(c["city_cp"])).strip()] if x).strip()
        addr = re.sub(r"\s+-\s*$", "", addr)
    if LANG_OF(spec) != "fr":            # « Los Angeles (Californie) » : l'État entre parenthèses, dans la langue de la page
        addr = re.sub(r"\(([^)]*)\)", lambda m: "(" + disp_region(m.group(1), country, spec) + ")", addr)
        addr = disp_addr(addr, country, spec)
    if addr:
        lines.append(f'<p class="addr">{esc(addr)}</p>')
    if c["phone"] and re.sub(r"\D", "", c["phone"]) not in BAD_PHONES:
        lines.append(f'<p class="contact">{phone_html(c["phone"], country)}</p>')
    for e in c["emails"][:2]:
        lines.append(f'<p class="contact"><a href="mailto:{esc(e)}">{esc(e)}</a></p>')
    # Site corrigé quand celui de FEI est mort, détourné ou périmé (relevé du 08/10/2026) ; "" = pas de lien.
    u = spec.get("urls", {}).get(k, c["url"].strip().rstrip(BOM))
    if u:
        u = u if u.startswith("http") else "http://" + u
        lines.append(f'<p class="contact"><a href="{esc(u)}" rel="noopener nofollow">{esc(host(u))}</a></p>')
    note = spec.get("notes", {}).get(k)
    if note:
        lines.append(f'<p class="contact"><em>{note}</em></p>')
    badges = []
    if spec["exam"] == "tcf":
        badges.append(f'<span class="badge ok">{W["so"]}</span>' if c["so"] else f'<span class="badge part">{W["paper"]}</span>')
    for kind, label in spec.get("badges", {}).get(k, []):
        badges.append(f'<span class="badge {kind}">{label}</span>')
    if badges:
        lines.append('<p class="badges">' + " ".join(badges) + "</p>")
    return f'<div class="card centre"><h4>{esc(disp_name(c["name"], country, spec))}</h4>\n' + "\n".join(lines) + "</div>"


_USED = set()


def uniq(cid):
    base, k = cid, 2
    while cid in _USED:
        cid = f"{base}-{k}"
        k += 1
    _USED.add(cid)
    return cid


def by_city(centres, country, spec):
    cities = OrderedDict()
    for c in sorted(centres, key=lambda x: (slug(disp_city(x["_city"], country, spec)), x["name"])):
        cities.setdefault(c["_city"], []).append(c)
    return cities


def city_blocks(centres, country, spec, level):
    out = []
    for city, cs in by_city(centres, country, spec).items():
        shown = disp_city(city, country, spec)
        n = f' <span class="count">({len(cs)})</span>' if len(cs) > 1 else ""
        out.append(f'<h{level} id="{uniq(slug(shown))}">{esc(shown)}{n}</h{level}>')
        out.append('<div class="grid c2 centres">\n' + "\n".join(card(c, country, spec) for c in cs) + "\n</div>")
    return "\n".join(out)


def list_section(d, spec):
    """La liste : par région (h2) puis ville (h3), par ville (h2) pour les petits pays, ou une ville et ses
    voisines (pages ville)."""
    country, centres = d["country"], d["centres"]
    W = words(spec)
    index, body = [], []
    if spec.get("layout") == "city":
        match = sorted((c for c in centres if c["_city"] in spec["match"]), key=lambda x: x["name"])
        near = sorted((c for c in centres if c["_city"] in spec.get("nearby", [])), key=lambda x: (x["_city"], x["name"]))
        body.append('<div class="grid c2 centres">\n' + "\n".join(card(c, country, spec) for c in match) + "\n</div>")
        if near:
            body.append(f'<h3 id="{uniq("nearby")}">{W["nearby"]}</h3>\n<div class="grid c2 centres">\n'
                        + "\n".join(card(c, country, spec) for c in near) + "\n</div>")
        return "\n".join(body), index
    if spec.get("layout") == "regions":
        regs = OrderedDict()
        for c in centres:
            regs.setdefault(region_of(c, country), []).append(c)
        shown = {r: disp_region(r, country, spec) for r in regs}
        if spec.get("region_sort") == "count":
            order = sorted(regs, key=lambda r: (-len(regs[r]), shown[r]))
        else:
            order = sorted(regs, key=lambda r: slug(shown[r]))
        for r in order:
            cs = regs[r]
            rid = uniq("region-" + slug(shown[r]))
            index.append((rid, f"{shown[r]} ({len(cs)})"))
            unit = W["centre"] if len(cs) == 1 else W["centres"]
            body.append(f'<h2 id="{rid}">{esc(shown[r])} — {len(cs)} {unit}</h2>\n' + city_blocks(cs, country, spec, 3))
    else:
        for city, cs in by_city(centres, country, spec).items():
            sh = disp_city(city, country, spec)
            cid = uniq(slug(sh))
            index.append((cid, f"{sh} ({len(cs)})" if len(cs) > 1 else sh))
            n = f' <span class="count">({len(cs)})</span>' if len(cs) > 1 else ""
            body.append(f'<h2 id="{cid}">{esc(sh)}{n}</h2>\n<div class="grid c2 centres">\n'
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
    oname = ORG_ES.get(o["name"], o["name"]) if LANG_OF(spec) == "es" else o["name"]
    ocity = disp_city(o["city"], d["country"], spec)
    parts = [f"<strong>{esc(oname)}</strong>" + (f" ({esc(ocity)})" if ocity else "")]
    if o["address"]:
        parts.append(esc(o["address"]))
    if o["url"] and "@" not in o["url"]:
        parts.append(f'<a href="{esc(o["url"])}" rel="noopener nofollow">{esc(host(o["url"]))}</a>')
    lang, W = LANG_OF(spec), words(spec)
    if lang == "es":
        return ("<p>El DELF y el DALF dependen aquí de un <strong>organismo de gestión central</strong>, que la lista de FEI "
                "distingue de los centros: " + " · ".join(parts) + f". Es quien fija el calendario nacional de {W['sess']}; "
                f"los candidatos {W['inscriben']} en un centro.</p>")
    if lang == "en":
        return (f"<p>Here the DELF and DALF are run by a <strong>central management body</strong>, which FEI’s list shows "
                f"separately from the {W['centres']}: " + " · ".join(parts) + ". It sets the national session calendar; "
                f"candidates register with a {W['centre']}.</p>")
    return ("<p>Le DELF et le DALF y sont pilotés par un <strong>organisme de gestion centrale</strong>, que la liste de FEI "
            "nomme à part des centres : " + " · ".join(parts) + ". C'est lui qui arrête le calendrier national des sessions ; "
            "les candidats, eux, s'inscrivent auprès d'un centre.</p>")


def texts(spec, exam_label, list_date, releve_date, country_name, fei_country, src, carte, extra, sources, exam):
    """Les phrases fixes de la page, par langue. La note de lecture ne parle que de ce que la page affiche :
    badges du relevé, sinon notes en italique, sinon rien (08/10/2026)."""
    lang, W = LANG_OF(spec), words(spec)
    badges, notes = bool(spec.get("badges")), bool(spec.get("notes"))
    if lang == "es":
        so_cap = W["so"][0].upper() + W["so"][1:]
        how = " ".join(x for x in [
            f"«{so_cap}»: según FEI, el centro ofrece {W['sess']} {W['so']}; «{W['paper']}»: no declara esa opción." if exam == "tcf" else "",
            ("Las etiquetas «TCF Canada» vienen" if exam == "tcf" else "Las etiquetas vienen")
            + f" de nuestra revisión {W['del_web']} de cada centro, el {releve_date}." if badges else
            f"Las notas en cursiva vienen de nuestra revisión {W['del_web']} de cada centro, el {releve_date}." if notes else ""] if x)
        exams = "TCF Canada, TCF Québec, TCF IRN" if exam == "tcf" else "DELF B1, DELF B2, DALF C1"
        return dict(
            note=f"""<p><strong>Cómo leer esta lista.</strong> Reproduce la lista oficial de centros autorizados por France
Éducation international (FEI), consultada el {list_date}: nombre, dirección, teléfono, correo genérico y {W['web']}
tal como los publica FEI; cuando {W['la_web']} ya no responde o {W['cambio']} de dirección, damos {W['lo']} que
abrimos ese día. {how + ' ' if how else ''}Un organismo que no figura en esta lista no está autorizado.</p>""",
            official_h2="Las listas oficiales",
            official=f"""<p><a href="{src}" rel="noopener">Lista oficial de centros {exam_label} de FEI — {esc(country_name)}</a> ·
<a href="{carte}" rel="noopener">mapa de centros {exam_label}</a>{extra}. Estas listas cambian: FEI añade y
retira centros a lo largo del año; la nuestra es del {list_date}. En caso de duda, la lista de FEI es la que vale.</p>""",
            sources=f"""<strong>Fuentes.</strong> Lista de centros de examen de France Éducation international
(filtro «{esc(fei_country)}», tipo «{exam_label}»), consultada el {list_date} — datos de contacto tal como los
publica FEI, solo correos genéricos; {sources} Los precios, fechas y condiciones cambian sin aviso:
verifícalos {W['en_web']} del centro antes de pagar.""",
            cta_h2="El centro te da la fecha; el nivel depende de ti",
            cta_p=f"""Cada {W['ses']} se paga completa y no se puede repetir de inmediato. Los simulacros de la app
«TCF DELF TEF: Tests 2026» reproducen el formato oficial de cada examen — {exams} — con la
puntuación del examen real y corrección con IA de la expresión escrita y oral. La app está en español.""")
    if lang == "en":
        how = " ".join(x for x in [
            f"“Computer-based”: FEI lists the {W['centre']} as offering computer sessions; “paper-based”: FEI lists no computer sessions."
            if exam == "tcf" else "",
            ("The “TCF Canada” badges come" if exam == "tcf" else "The badges come")
            + f" from our check of each {W['centre']}’s website on {releve_date}." if badges else
            f"Notes in italics come from our check of each {W['centre']}’s website on {releve_date}." if notes else ""] if x)
        exams = "TCF Canada, TCF Québec, TCF IRN" if exam == "tcf" else "DELF B1, DELF B2, DALF C1"
        return dict(
            note=f"""<p><strong>How to read this list.</strong> It reproduces the official list of test {W['centres']} approved
by France Éducation international (FEI), read on {list_date}: name, address, phone, generic email and website
as FEI publishes them; where the listed website no longer works or has moved, we give the one we opened that
day. {how + ' ' if how else ''}An {W['org']} that is not on this list is not approved.</p>""",
            official_h2="The official lists",
            official=f"""<p><a href="{src}" rel="noopener">FEI’s official list of {exam_label} test {W['centres']} — {esc(country_name)}</a> ·
<a href="{carte}" rel="noopener">map of {exam_label} {W['centres']}</a>{extra}. These lists change: FEI adds and
removes {W['centres']} during the year — ours is dated {list_date}. If in doubt, FEI’s list is the reference.</p>""",
            sources=f"""<strong>Sources.</strong> France Éducation international’s list of exam {W['centres']}
(filter “{esc(fei_country)}”, type “{exam_label}”), read on {list_date} — contact details as FEI publishes
them, generic email addresses only; {sources} Prices, dates and rules change without notice: check them on the
{W['centre']}’s website before paying.""",
            cta_h2=f"The {W['centre']} gives you the date; the score is up to you",
            cta_p=f"""You pay the full fee for each session, and you can’t retake the test right away. The mock exams in the
“TCF DELF TEF: Tests 2026” app follow the official format of each test — {exams} — scored like
the real thing, with AI feedback on writing and speaking.""")
    how = " ".join(x for x in [
        "« Sur ordinateur » : FEI indique que le centre propose des sessions sur ordinateur ; « papier » : il n'en "
        "déclare pas." if exam == "tcf" else "",
        ("Les badges « TCF Canada » viennent" if exam == "tcf" else "Les badges viennent") + " de notre relevé du "
        + releve_date + " sur le site de chaque centre." if badges else
        "Les notes en italique viennent de notre relevé du " + releve_date + " sur le site de chaque centre." if notes else ""] if x)
    return dict(
        note=f"""<p><strong>Comment lire cette liste.</strong> Elle reprend la liste officielle des centres agréés par
France Éducation international, consultée le {list_date} — nom, adresse, téléphone, adresse e-mail
générique et site tels que FEI les publie ; quand le site indiqué ne répond plus ou a changé d'adresse, nous
donnons celui que nous avons ouvert ce jour-là. {how + ' ' if how else ''}Un organisme absent de cette liste n'est pas agréé.</p>""",
        official_h2="Les listes officielles",
        official=f"""<p><a href="{src}" rel="noopener">Liste des centres {exam_label} — {esc(fei_country)}</a> (FEI) ·
<a href="{carte}" rel="noopener">carte des centres {exam_label}</a>{extra}. Ces listes
évoluent : FEI ajoute et retire des centres au fil des agréments — la nôtre est datée du {list_date} ;
en cas de doute, la liste de FEI fait foi.</p>""",
        sources=f"""<strong>Sources.</strong> Liste des centres d'examen de France Éducation international
(filtre « {esc(fei_country)} », type « {exam_label} »), consultée le {list_date} — coordonnées telles que FEI
les publie, adresses e-mail génériques seulement ; {sources} Les prix, dates et modalités
changent sans préavis : vérifiez-les sur le site du centre avant de payer.""",
        cta_h2="Le centre vous donne la date ; le niveau, c'est vous",
        cta_p=f"""Une session se paie en entier et se repasse après un délai. Les examens blancs de
l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent le format officiel de chaque
déclinaison — {'TCF Canada, TCF Québec, TCF IRN' if exam == 'tcf' else 'DELF B1, DELF B2, DALF C1'} — avec la
notation du vrai test et la correction IA de l'écrit et de l'oral.""")


class _Safe(dict):
    def __missing__(self, k):
        return "{" + k + "}"


def page(spec, tr=None):
    lang, var = LANG_OF(spec), VARIANT(spec)
    _USED.clear()
    _USED.update({"liste", "sources-officielles", "faq", "a-lire"} | {sid for sid, _, _ in spec["sections"]})
    d = load(spec["file"])
    country = d["country"]
    for c in d["centres"]:
        c["_city"] = city_of(c, country)
        if country in REGION and spec.get("layout") == "regions":
            assert c["_city"] in REGION[country], (spec["slug"], c["_city"])
    sel = [c for c in d["centres"] if c["_city"] in spec["match"]] if spec.get("layout") == "city" else d["centres"]
    n = len(sel)
    so = sum(1 for c in sel if c["so"])
    ncity = len({c["_city"] for c in sel})
    known = {ckey(c) for c in d["centres"]}
    for k in list(spec.get("badges", {})) + list(spec.get("notes", {})) + list(spec.get("urls", {})):
        assert k in known, (spec["slug"], "clé inconnue", k)
    vals = _Safe(n=n, so=so, ncity=ncity, paper=n - so)
    fmt = lambda s: s.format_map(vals)
    exam_label = "TCF" if spec["exam"] == "tcf" else "DELF-DALF"
    typ = "tcf" if spec["exam"] == "tcf" else "delf_dalf"
    date_label = spec.get("date_label", DATE_LABEL[var])
    list_date = spec.get("list_date", date_label)
    releve_date = spec.get("releve_date", date_label)
    list_html, index = list_section(d, spec)
    T = texts(spec, exam_label, list_date, releve_date, spec.get("country_name", country), country,
              FEI_LISTE % (PAYS_ID[country], typ), FEI_CARTE % typ, spec.get("extra_sources_links", ""),
              fmt(spec["sources"]), spec["exam"])
    sections = "\n\n".join(f'<h2 id="{sid}">{title}</h2>\n{fmt(html)}' for sid, title, html in spec["sections"])
    lst = f"""<h2 id="liste">{fmt(spec['list_title'])}</h2>
{org_block(d, spec) if spec['exam'] == 'delf' else ''}
<div class="note">
{T['note']}
</div>
{fmt(spec.get('list_intro', ''))}
{chips(index) if index else ''}

{list_html}"""
    body = f"""
{stats([tuple(fmt(x) for x in s) for s in spec['stats']])}

{sections}

{lst}

<h2 id="sources-officielles">{T['official_h2']}</h2>
{T['official']}
"""
    toc = [(sid, re.sub(r"<[^>]+>", "", title)) for sid, title, _ in spec["sections"]] + \
          [("liste", re.sub(r"<[^>]+>", "", fmt(spec["list_title"])))] + \
          [(i, t.split(" (")[0]) for i, t in index[:spec.get("toc_regions", 8)]] + \
          [("sources-officielles", T["official_h2"])]
    a = {
        "section": "centres", "section_name": "Centres", "og_slug": "centres-" + spec["slug"],
        "slug": spec["slug"], "accent": "accent-tcf" if spec["exam"] == "tcf" else "accent-delf", "crumb": spec["crumb"],
        "title": fmt(spec["title"]), "desc": fmt(spec["desc"]),
        "og_title": fmt(spec.get("og_title", spec["title"])), "og_desc": fmt(spec.get("og_desc", spec["desc"])),
        "h1": fmt(spec["h1"]),
        "published": DATE, "modified": DATE, "date_fr": date_label, "read": spec.get("read", max(5, n // 8)),
        "intro": fmt(spec["intro"]), "facts": [fmt(f) for f in spec["facts"]],
        "toc": toc, "body": body,
        "cta_h2": spec.get("cta_h2", T["cta_h2"]),
        "cta_p": spec.get("cta_p", T["cta_p"]),
        "faq": [(fmt(q), fmt(r)) for q, r in spec["faq"]], "also": spec["also"],
        "sources": T["sources"],
    }
    tr = translations() if tr is None else tr
    if lang == "fr":
        alts, links = alternates_for(f"/centres/{spec['slug']}/", tr)
    else:
        a.update({"lang": lang, "in_language": var, "og_locale": spec.get("og_locale", OG_LOCALE[var]), "section": lang,
                  "crumbs": [(HOME_LABEL[lang], f"/{lang}/")], "og_slug": f"{lang}-{spec['slug']}"})
        a.pop("section_name")
        alts, links = alternates_for(spec["fr_path"], tr, current=lang)
    if alts:
        a["alternates"], a["lang_links"] = alts, links
    assert len(a["title"]) <= 60, (spec["slug"], len(a["title"]), a["title"])
    assert len(a["desc"]) <= 158, (spec["slug"], len(a["desc"]))
    return a, (n, so, ncity)


# ---------------------------------------------------------------------------
# Traductions : chaque page /es/ ou /en/ porte le chemin de son original français (fr_path) ; les deux
# côtés en tirent leurs balises hreflang et leur lien de langue visible.
# ---------------------------------------------------------------------------
def translated_specs():
    out = []
    for mod in ("pays_config_es", "pays_config_en"):
        try:
            out += __import__(mod).PAGES
        except ModuleNotFoundError:
            pass
    return out


def translations():
    tr = {}
    for p in translated_specs():
        tr.setdefault(p["fr_path"], []).append((p["lang"], f"/{p['lang']}/{p['slug']}/"))
    return tr


def alternates_for(fr_path, tr=None, current="fr"):
    """([(hreflang, chemin)], <p class="langs">…</p>) pour une page et ses traductions, ou (None, None)."""
    tr = translations() if tr is None else tr
    if fr_path not in tr:
        return None, None
    alts = [("fr", fr_path)] + tr[fr_path] + [("x-default", fr_path)]
    others = [("fr", fr_path)] + tr[fr_path]
    links = '<p class="langs">' + " · ".join(f'<a href="{p}" hreflang="{l}" lang="{l}">{LINK_LABEL[l]}</a>'
                                            for l, p in others if l != current) + "</p>"
    return alts, links


def hub(lang):
    """Accueil de langue (/es/, /en/) : texte dans pays_config_<lang>.HUB."""
    H = __import__("pays_config_" + lang).HUB
    var = H.get("variant", {"es": "es-419", "en": "en-US"}[lang])
    a = dict(H, lang=lang, in_language=var, og_locale=OG_LOCALE[var], section="", slug=lang,
             crumbs=[("delf-tcf-tef.fr", "/")], og_slug=f"{lang}-hub", published=DATE, modified=DATE,
             date_fr=DATE_LABEL[var])
    assert len(a["title"]) <= 60 and len(a["desc"]) <= 158, (lang, len(a["title"]), len(a["desc"]))
    return a


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
    tr = translations()
    arts = [page(s, tr)[0] for s in specs() + translated_specs()]
    arts += [hub(lang) for lang in ("es", "en") if hasattr(__import__("pays_config_" + lang), "HUB")] \
        if all(os.path.exists(os.path.join(HERE, f"pays_config_{l}.py")) for l in ("es", "en")) else []
    build(arts, overwrite=force)


if __name__ == "__main__":
    main()
