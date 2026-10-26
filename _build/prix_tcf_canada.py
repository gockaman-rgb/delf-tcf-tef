# -*- coding: utf-8 -*-
"""Prix du TCF Canada, pays par pays et ville par ville (26/10/2026) — un seul jeu de données pour deux pages :
/tcf-canada/prix-inscription/ (exam_hubs_config.py, extra_top) et /en/tcf-canada/fees-registration/ (i18n_pages_en.py).

Règle : aucun prix nouveau ici. Chaque prix est déjà publié sur le site, avec sa date, sur la page vers laquelle il
renvoie : /blog/prix-tcf-tef/ (source de vérité : France, Canada 17/09, Maghreb 17/10, Amérique latine, Espagne,
Royaume-Uni, Inde, Émirats, Arabie saoudite), les pages pays et ville (/centres/…, /en/…), les pages du 26/10/2026
(Amérique du Nord : pays_config_en_na.py et les pages Toronto, Ottawa, Vancouver ; Golfe : pays_config_en_arab.py ;
Égypte). Les pages relevées le 26/10 sont en anglais. Mêmes nombres des deux côtés (check_i18n : parité FR → EN).
"""
from pays_config import table


def _a(href, text):
    return f'<a href="{href}">{text}</a>'


# (pays FR, pays EN, lien du pays — ou (FR, EN) —, prix FR, prix EN, détail FR, détail EN, relevé FR, relevé EN)
ROWS = [
    ("Canada", "Canada", "/en/tcf-canada-test-centres/", "390 à 452 $CA", "C$390 to C$452",
     f"{_a('/en/tcf-canada-vancouver/', 'Vancouver')} 390 $ (351 $ adhérent) · {_a('/en/tcf-canada-toronto/', 'Toronto')} 390 $ · "
     f"{_a('/en/tcf-canada-new-brunswick/', 'Moncton, Edmundston, Bathurst')} 390 $ · {_a('/en/tcf-canada-ottawa/', 'Ottawa')}, "
     f"{_a('/en/tcf-canada-alberta/', 'Calgary, Edmonton')}, {_a('/en/tcf-canada-halifax/', 'Halifax')}, "
     f"{_a('/en/tcf-canada-winnipeg/', 'Winnipeg')} 400 $ · {_a('/en/tcf-canada-ontario/', 'GB Language Centre (North York)')} 452 $ "
     f"(26 oct.) · {_a('/centres/tcf-quebec-ville/', 'UQTR, Trois-Rivières')} 440 $ (30 juil.) · "
     f"{_a('/centres/tcf-montreal/', 'Alliance Française de Montréal')} : non publié (17 sept.)",
     f"{_a('/en/tcf-canada-vancouver/', 'Vancouver')} $390 ($351 for members) · {_a('/en/tcf-canada-toronto/', 'Toronto')} $390 · "
     f"{_a('/en/tcf-canada-new-brunswick/', 'Moncton, Edmundston, Bathurst')} $390 · {_a('/en/tcf-canada-ottawa/', 'Ottawa')}, "
     f"{_a('/en/tcf-canada-alberta/', 'Calgary, Edmonton')}, {_a('/en/tcf-canada-halifax/', 'Halifax')}, "
     f"{_a('/en/tcf-canada-winnipeg/', 'Winnipeg')} $400 · {_a('/en/tcf-canada-ontario/', 'GB Language Centre (North York)')} $452 "
     f"(26 Oct) · {_a('/en/tcf-canada-quebec-city/', 'UQTR, Trois-Rivières')} $440 (30 Jul) · "
     f"{_a('/en/tcf-canada-montreal/', 'Alliance Française de Montréal')}: not published (17 Sept)",
     "30 juil. – 26 oct. 2026", "30 Jul – 26 Oct 2026"),
    ("États-Unis", "United States", "/en/tcf-canada-usa/", "330 à 505 $US", "US$330 to US$505",
     f"{_a('/en/tcf-canada-detroit/', 'Detroit')} 330 $ (26 oct.) · {_a('/en/tcf-canada-boston/', 'Boston')} 350 $ (18 oct.) · "
     f"{_a('/en/tcf-canada-new-york/', 'New York')} 350 $ (adhérent) ou 399 $ (18 oct.) · {_a('/en/tcf-canada-denver/', 'Denver')} "
     f"360 $ (Alliance) et 435 $ (Pluma Academy) (26 oct.) · Philadelphie 360 $ et Kansas City 370 $ (8 oct.) · "
     f"{_a('/en/tcf-canada-houston/', 'Houston')} 400 $ (8 oct.) · {_a('/en/tcf-canada-san-diego/', 'San Diego')} 450 $ (18 oct.) · "
     f"{_a('/en/tcf-canada-san-francisco/', 'San Francisco')} 460 $ (26 oct.) et Pasadena 460 $ (18 oct.) · "
     f"{_a('/en/tcf-canada-los-angeles/', 'Los Angeles')} 505 $ (18 oct.)",
     f"{_a('/en/tcf-canada-detroit/', 'Detroit')} $330 (26 Oct) · {_a('/en/tcf-canada-boston/', 'Boston')} $350 (18 Oct) · "
     f"{_a('/en/tcf-canada-new-york/', 'New York')} $350 (members) or $399 (18 Oct) · {_a('/en/tcf-canada-denver/', 'Denver')} "
     f"$360 (Alliance) and $435 (Pluma Academy) (26 Oct) · Philadelphia $360 and Kansas City $370 (8 Oct) · "
     f"{_a('/en/tcf-canada-houston/', 'Houston')} $400 (8 Oct) · {_a('/en/tcf-canada-san-diego/', 'San Diego')} $450 (18 Oct) · "
     f"{_a('/en/tcf-canada-san-francisco/', 'San Francisco')} $460 (26 Oct) and Pasadena $460 (18 Oct) · "
     f"{_a('/en/tcf-canada-los-angeles/', 'Los Angeles')} $505 (18 Oct)",
     "8 – 26 oct. 2026", "8 – 26 Oct 2026"),
    ("France", "France", "/blog/ou-passer-le-tcf-canada-en-france/", "195 à 285 €", "€195 to €285",
     f"{_a('/centres/tcf-paris/', 'Paris')} 195 € (ACTE) et 220 € (ACCORD) · {_a('/centres/tcf-lyon/', 'Lyon')} 220 € · "
     f"{_a('/centres/tcf-montpellier/', 'Montpellier')} 200 € · {_a('/centres/tcf-marseille/', 'Aix-Marseille')} 240 € (60 € par épreuve) · "
     f"{_a('/centres/tcf-rennes/', 'Rennes et Brest')} (CLPS) 285 €",
     f"{_a('/centres/tcf-paris/', 'Paris')} €195 (ACTE) and €220 (ACCORD) · {_a('/centres/tcf-lyon/', 'Lyon')} €220 · "
     f"{_a('/centres/tcf-montpellier/', 'Montpellier')} €200 · {_a('/centres/tcf-marseille/', 'Aix-Marseille')} €240 (€60 per test) · "
     f"{_a('/centres/tcf-rennes/', 'Rennes and Brest')} (CLPS) €285 — pages in French",
     "17 sept. 2026", "17 Sept 2026"),
    ("Algérie", "Algeria", "/blog/tcf-canada-algerie/", "37 500 DA", "37,500 DA",
     "les cinq antennes de l'Institut français, paiement sur la plateforme IFAL", "the five Institut français branches, paid on the IFAL platform (page in French)",
     "17 oct. 2026", "17 Oct 2026"),
    ("Maroc", "Morocco", "/blog/tcf-canada-maroc/", "2 900 Dhs", "2,900 MAD",
     "tarif national de l'Institut français du Maroc", "national fee of the Institut français du Maroc (page in French)",
     "17 oct. 2026", "17 Oct 2026"),
    ("Tunisie", "Tunisia", "/blog/tcf-canada-tunisie/", "880 DT", "880 TND",
     "Institut français de Tunisie", "Institut français de Tunisie (page in French)", "17 oct. 2026", "17 Oct 2026"),
    ("Royaume-Uni", "United Kingdom", ("/centres/tcf-royaume-uni/", "/en/tcf-canada-uk/"), "260 à 325 £", "£260 to £325",
     "Londres (Institut français) 260 £ · Glasgow (Alliance française) 325 £", "London (Institut français) £260 · Glasgow (Alliance française) £325",
     "8 oct. 2026", "8 Oct 2026"),
    ("Espagne", "Spain", "/centres/tcf-espagne/", "275 à 287 €", "€275 to €287",
     "287 € (Instituts français, ILF Séville) · 281 € (Alliances françaises) · 275 € (CELF Séville)",
     "€287 (Instituts français, ILF Seville) · €281 (Alliances françaises) · €275 (CELF Seville)", "8 oct. 2026", "8 Oct 2026"),
    ("Mexique", "Mexico", "/centres/tcf-mexique/", "4 800 à 6 500 pesos", "4,800 to 6,500 pesos",
     "Puebla 4 800 · Guadalajara 4 950 · IFAL (Mexico) 5 150, 6 500 pour une date à la demande · UAEH (Pachuca) 5 800",
     "Puebla 4,800 · Guadalajara 4,950 · IFAL (Mexico City) 5,150, 6,500 for a date on request · UAEH (Pachuca) 5,800",
     "8 oct. 2026", "8 Oct 2026"),
    ("Colombie", "Colombia", "/centres/tcf-colombie/", "dès 1 050 000 pesos", "from 1,050,000 pesos",
     "Medellín et Pereira 1 050 000 · Bogotá jusqu'à 1 247 000", "Medellín and Pereira 1,050,000 · Bogotá up to 1,247,000", "8 oct. 2026", "8 Oct 2026"),
    ("Chili", "Chile", "/centres/tcf-chili/", "299 000 pesos", "299,000 pesos",
     "Institut français du Chili (Santiago) et Alliance française de Concepción", "Institut français du Chili (Santiago) and Alliance française de Concepción",
     "8 oct. 2026", "8 Oct 2026"),
    ("Pérou", "Peru", "/centres/tcf-perou/", "1 240 soles", "1,240 soles",
     "Alliance française de Lima ; 992 soles au tarif adhérent", "Alliance française de Lima; 992 soles for members", "8 oct. 2026", "8 Oct 2026"),
    ("Équateur", "Ecuador", "/centres/tcf-equateur/", "200 à 300 $US", "US$200 to US$300",
     "Cuenca 200 $ · Guayaquil 300 $", "Cuenca $200 · Guayaquil $300", "8 oct. 2026", "8 Oct 2026"),
    ("Inde", "India", "/en/tcf-canada-india/", "26 000 ₹", "₹26,000",
     "New Delhi, Calcutta, Bhopal ; non publié à Ahmedabad et Bangalore", "New Delhi, Kolkata, Bhopal; not published in Ahmedabad or Bangalore",
     "8 oct. 2026", "8 Oct 2026"),
    ("Émirats arabes unis", "United Arab Emirates", "/en/tcf-canada-dubai/", "1 800 AED", "1,800 AED",
     f"Dubaï (deux centres) et {_a('/en/tcf-canada-abu-dhabi/', 'Abou Dhabi')}", f"Dubai (two centres) and {_a('/en/tcf-canada-abu-dhabi/', 'Abu Dhabi')}",
     "8 oct. 2026", "8 Oct 2026"),
    ("Arabie saoudite", "Saudi Arabia", "/en/tcf-canada-saudi-arabia/", "1 950 SAR", "1,950 SAR",
     "Djeddah et Riyad (Alliance française d'Arabie saoudite)", "Jeddah and Riyadh (Alliance française d’Arabie Saoudite)", "13 oct. 2026", "13 Oct 2026"),
    ("Qatar", "Qatar", "/en/tcf-canada-qatar/", "1 300 QAR", "1,300 QAR",
     "Institut français du Qatar (Doha), sur ordinateur", "Institut français du Qatar (Doha), on computer", "26 oct. 2026", "26 Oct 2026"),
    ("Égypte", "Egypt", "/en/tcf-canada-egypt/", "non publié pour 2026", "not published for 2026",
     "barème 2024 : l'équivalent de 250 €, payé en livres égyptiennes au taux du mois",
     "2024 fee list: the equivalent of €250, paid in Egyptian pounds at the month’s exchange rate", "26 oct. 2026", "26 Oct 2026"),
    ("Liban", "Lebanon", "/en/tcf-canada-lebanon/", "non publié", "not published",
     "Instituts français : tarifs dans des calendriers PDF", "Instituts français: fees in PDF calendars only", "13 oct. 2026", "13 Oct 2026"),
    ("Jordanie", "Jordan", "/en/tcf-canada-jordan/", "non publié", "not published",
     "Institut français de Jordanie, trois sessions par an", "Institut français de Jordanie, three sessions a year", "26 oct. 2026", "26 Oct 2026"),
    ("Koweït", "Kuwait", "/en/tcf-canada-kuwait/", "aucun TCF Canada publié", "no TCF Canada published",
     "TEF Canada 130 KD à l'Institut français du Koweït", "TEF Canada 130 KD at the Institut français du Koweït", "26 oct. 2026", "26 Oct 2026"),
]


def _rows(lang):
    fr = lang == "fr"
    return [(_a(href if isinstance(href, str) else href[0 if fr else 1], f"<strong>{pfr if fr else pen}</strong>"), f"<strong>{xfr if fr else xen}</strong>", dfr if fr else den,
             rfr if fr else ren) for pfr, pen, href, xfr, xen, dfr, den, rfr, ren in ROWS]


FR = """
<h2 id="prix-par-pays">Prix du TCF Canada 2026, pays par pays et ville par ville</h2>
<p>Chaque prix ci-dessous est celui que le centre affichait sur son site à la date indiquée ; le lien mène à la page qui
le détaille, centre par centre. Les relevés du 26 octobre 2026 (Canada, États-Unis, Golfe) sont sur nos pages en
anglais.</p>
""" + table("Prix du TCF Canada par pays et par ville, dans la monnaie locale, tels que les centres les affichaient à la date "
            "indiquée (2026). Aucun tarif national : vérifiez sur le site du centre avant de payer. Source des prix publiés "
            "avant le 26 octobre : <a href=\"/blog/prix-tcf-tef/\">Prix du TCF et du TEF en 2026</a>.",
            ["Pays", "TCF Canada", "Détail, ville par ville", "Relevé"], _rows("fr"), wide=True)

EN = """
<h2 id="by-country">TCF Canada fees 2026, by country and by city</h2>
<p>Each fee below is the one the centre showed on its website on the date given; the link leads to the page with the
details, centre by centre. The pages checked on 26 October 2026 cover Canada, the United States and the Gulf; the
France and North Africa pages are in French.</p>
""" + table("TCF Canada fee by country and city, in the local currency, as the centres posted it on the date shown (2026). "
            "There is no national fee: confirm it on the centre’s website before paying.",
            ["Country", "TCF Canada fee", "City by city", "Checked on"], _rows("en"), wide=True)
