# -*- coding: utf-8 -*-
"""Pages pays d'Europe (make_pays.py) — le TCF (dont le TCF Canada) et le DELF-DALF en Allemagne, en Suisse, en
Belgique, en Italie, aux Pays-Bas, au Portugal, en Roumanie, en Pologne, en Grèce et en Irlande (26/10/2026).

Liste FEI : data/fei_monde/<tcf|delf>_<pays>.json, lue le 26 octobre 2026 (extraction monde). Relevé : le site de
chaque centre, ouvert le 26 octobre 2026 (module d'inscription de l'Institut français d'Allemagne, swiss-exams,
alliancefr.be… lus dans Chrome quand la page ne s'affiche qu'en JavaScript). Traductions anglaises :
pays_config_en_eu.py. Branché par une ligne à la fin de pays_config.py ; make_pays.py lit TABLES (indicatifs,
villes) dans le bloc « Europe ».

Module autonome : il n'importe ni pays_config ni make_pays (pays_config l'importe à sa fin, make_pays à son
chargement) — d'où ses propres table() et releve().

Règle de rédaction (celle de pays_config.py) : un prix, une date, une règle n'entrent ici que lus sur le site du
centre ou de l'organisme le 26 octobre 2026 ; sinon « non publié ». Jamais d'adresse e-mail prénom.nom.
"""
import html
import re

DATE = "2026-10-26"
D_FR = "26 octobre 2026"
OK_CA = [("ok", "TCF Canada")]
NO_CA = [("no", "pas de TCF Canada")]


def table(caption, head, rows, wide=True):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = "\n".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return (f'<div class="tablewrap{" wide" if wide else ""}">\n<table>\n<caption>{caption}</caption>\n'
            f"<thead><tr>{th}</tr></thead>\n<tbody>\n{body}\n</tbody>\n</table>\n</div>")


def releve(rows, caption="Ce que le site de chaque centre affichait le 26 octobre 2026. « Non publié » : rien sur le site ce jour-là — le centre fait foi."):
    return table(caption, ["Centre", "Déclinaisons", "Prix", "Sessions et inscription"],
                 [(f"<strong>{a}</strong>", b, c, d) for a, b, c, d in rows])


# ---------------------------------------------------------------------------
# Tables lues par make_pays.py (bloc « Europe ») : identifiants FEI, indicatifs, villes.
# ---------------------------------------------------------------------------
PAYS_ID = {"Allemagne": 60, "Suisse": 94, "Belgique": 62, "Italie": 78, "Pays-Bas": 84, "Portugal": 86,
           "Roumanie": 87, "Pologne": 85, "Grèce": 74, "Irlande": 76}
# Longueurs possibles du numéro national (sans le 0 de l'appel intérieur ; l'italien garde son 0).
PHONE = {"Allemagne": ("49", set(range(7, 12))), "Suisse": ("41", {9}), "Belgique": ("32", {8, 9}),
         "Italie": ("39", set(range(6, 12))), "Pays-Bas": ("31", {9}), "Portugal": ("351", {9}),
         "Roumanie": ("40", {9}), "Pologne": ("48", {9}), "Grèce": ("30", {10}), "Irlande": ("353", {7, 8, 9})}
CITY = {"Allemagne": {"Aachen": "Aix-la-Chapelle", "Bremen (Brême)": "Brême", "Bremen": "Brême", "Dresden": "Dresde",
                      "Frankfurt/Main": "Francfort", "Frankfurt Am Main": "Francfort", "Hamburg": "Hambourg",
                      "Köln": "Cologne", "Mainz": "Mayence", "Freiburg": "Fribourg-en-Brisgau", "Saarbrücken": "Sarrebruck"},
        "Suisse": {"Bellinzona": "Bellinzone"},
        "Belgique": {"Antwerpen": "Anvers", "Gent": "Gand", "Kortrijk": "Courtrai"},
        "Italie": {"Padova": "Padoue", "Vicenza": "Vicence"},
        "Pays-Bas": {"Den Haag (La Haye)": "La Haye", "Nijmegen (Nimègue)": "Nimègue"},
        "Roumanie": {"Timisoara": "Timișoara"}}
CITY_T = {"en": {"Allemagne": {"Aix-la-Chapelle": "Aachen", "Brême": "Bremen", "Dresde": "Dresden", "Francfort": "Frankfurt",
                               "Hambourg": "Hamburg", "Mayence": "Mainz", "Fribourg-en-Brisgau": "Freiburg",
                               "Sarrebruck": "Saarbrücken", "Hanovre": "Hanover"},
                 "Suisse": {"Berne": "Bern", "Genève": "Geneva"},
                 "Belgique": {"Bruxelles": "Brussels", "Gand": "Ghent", "Anvers": "Antwerp", "Courtrai": "Kortrijk"},
                 "Italie": {"Aoste": "Aosta", "Bologne": "Bologna", "Gênes": "Genoa", "Padoue": "Padua", "Palerme": "Palermo",
                            "Venise": "Venice", "Vicence": "Vicenza"},
                 "Pays-Bas": {"La Haye": "The Hague", "Nimègue": "Nijmegen"},
                 "Portugal": {"Lisbonne": "Lisbon"},
                 "Roumanie": {"Bucarest": "Bucharest"},
                 "Pologne": {"Cracovie": "Kraków", "Varsovie": "Warsaw"},
                 "Grèce": {"Athènes": "Athens", "Thessalonique": "Thessaloniki"}}}
ADDR_T = {"en": {"Allemagne": {"Bremen (Brême)": "Bremen", "Hambourg": "Hamburg", "Hanovre": "Hanover"},
                 "Suisse": {"Berne": "Bern", "Genève": "Geneva", "Lucerne": "Luzern"},
                 "Belgique": {"Bruxelles": "Brussels", "Gand": "Ghent"},
                 "Italie": {"Aoste": "Aosta", "Bologne": "Bologna", "Gênes": "Genoa", "Palerme": "Palermo", "Venise": "Venice"},
                 "Pays-Bas": {"Den Haag (La Haye)": "Den Haag", "Nijmegen (Nimègue)": "Nijmegen"},
                 "Portugal": {"Lisbonne": "Lisbon"},
                 "Roumanie": {"Bucarest": "Bucharest"},
                 "Pologne": {"Cracovie": "Kraków", "Varsovie": "Warsaw"},
                 "Grèce": {"Athènes": "Athens", "Thessalonique": "Thessaloniki"}}}


def phone_eu(phone, country):
    """Lien tel: d'un numéro européen de FEI, en gardant sa découpe (« 49-30-885-902-19 » → +49 30 885 902 19).
    Indicatif « 00cc » ou « cc » ôté, puis le 0 de l'appel intérieur (sauf en Italie, où il fait partie du
    numéro). Longueur impossible → le numéro s'affiche tel que FEI l'écrit, sans lien."""
    cc, lens = PHONE[country]
    toks = re.findall(r"\d+", re.split(r"\s*/\s*", phone)[0])
    s = "".join(toks)
    drop = 0
    if s.startswith("00" + cc):
        drop = 2 + len(cc)
    elif s.startswith(cc) and len(s) - len(cc) in lens:
        drop = len(cc)
    elif s.startswith("0" + cc) and len(s) - len(cc) - 1 in lens and country != "Italie":
        drop = 1 + len(cc)                 # « 041-44-261-93-06 » : un 0 devant l'indicatif suisse
    out, n = [], drop
    for t in toks:
        if n >= len(t):
            n -= len(t)
            continue
        out.append(t[n:])
        n = 0
    if out and out[0] == "0" and len(out) > 1 and country == "Italie":
        out = [out[0] + out[1]] + out[2:]     # « 00390-248-… » : le 0 italien rejoint le groupe suivant
    if country != "Italie" and out and out[0].startswith("0"):
        out[0] = out[0][1:]
        out = [t for t in out if t]
    x = "".join(out)
    if not x or len(x) not in lens or (country != "Italie" and x[0] == "0"):
        return html.escape(phone)
    return f'<a href="tel:+{cc}{x}">+{cc} {" ".join(out)}</a>'


TABLES = dict(PAYS_ID=PAYS_ID, PHONE=PHONE, CITY=CITY, CITY_T=CITY_T, ADDR_T=ADDR_T, phone=phone_eu)

PAGES = []

# Liens communs (mêmes cibles que pays_config.py)
A_TCF = ("/tcf-canada/", "TCF Canada : la page d'accueil", "Les quatre épreuves, la notation sur 699 et la conversion NCLC.")
A_NCLC = ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", "458 en compréhension orale, 453 à l'écrit.")
A_TEF = ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", "Les deux tests acceptés par IRCC, côte à côte.")
A_DELF = ("/delf-b2/", "DELF B2 : la page d'accueil", "Le format, le barème (50 sur 100) et la préparation.")
A_DIPL = ("/blog/diplome-ou-test-delf-tcf/", "Diplôme ou test : lequel vous faut-il ?", "Un diplôme s'obtient à vie ; un test vous situe pour deux ans.")
A_EUR = ("/centres/tcf-europe/", "Centres TCF en Europe", "Pays par pays : qui propose le TCF Canada, et à quel prix.")
EU = dict(published=DATE, date_label=D_FR, list_date=D_FR, releve_date=D_FR)
IF_DE = "https://www.institutfrancais.de/de/franzoesisch-lernen/pruefungen-zertifikate/anmeldung-fuer-sprachzertifikate"

# ===========================================================================
# ALLEMAGNE — TCF
# ===========================================================================
DE_IF = ["berlin-institut-francais", "breme-institut-francais", "hambourg-institut-francais-de-hambourg",
         "mayence-institut-francais", "munich-institut-francais", "stuttgart-institut-francais-d-allemagne-antenne-stuttgart"]
PAGES.append(dict(EU,
    slug="tcf-allemagne", exam="tcf", file="fei_monde/tcf_allemagne", layout="cities", chip="Allemagne",
    crumb="TCF en Allemagne",
    pointer="Dix centres annoncent le TCF Canada, dont six Instituts français à 295 € ; 23 sessions jusqu'en décembre 2027.",
    title="TCF Canada en Allemagne : 10 centres, 295 €, dates",
    desc="TCF Canada en Allemagne : Berlin, Hambourg, Munich, Stuttgart, Mayence, Brême à 295 €, Erlangen à 210 € ; les sessions de novembre 2026 à 2027.",
    h1="TCF Canada en Allemagne : les centres qui le proposent, les prix et les dates",
    intro="""En Allemagne, {n} centres sont agréés pour le TCF par France Éducation international, et <strong>dix annoncent le
TCF Canada</strong> : les Instituts français de Berlin, Brême, Hambourg, Mayence, Munich et Stuttgart, qui le vendent
sur un module d'inscription commun à <strong>295 €</strong>, l'Institut d'Aix-la-Chapelle (295 €), celui de Bonn,
l'Institut franco-allemand d'Erlangen (<strong>210 €</strong>) et l'Institut français de Mannheim. Le 26 octobre 2026,
le module comptait 23 sessions TCF Canada jusqu'en décembre 2027 ; la première avec des places : Munich, le
<strong>17 novembre</strong> (inscriptions jusqu'au 8 novembre). Francfort, Tübingen et Dresde ne le proposent pas.""",
    facts=["<strong>{n} centres agréés</strong> (liste FEI du 26 octobre 2026), <strong>10 qui annoncent le TCF Canada</strong> : Berlin, Brême, Hambourg, Mayence, Munich, Stuttgart, Aix-la-Chapelle, Bonn, Erlangen et Mannheim.",
           "<strong>295 €</strong> dans les six Instituts français du module commun et à Aix-la-Chapelle ; <strong>210 €</strong> à Erlangen (sur ordinateur) ; Bonn et Mannheim ne publient pas leur tarif.",
           "Sessions TCF Canada 2026 : Munich 17/11 et 04/12, Stuttgart 27/11, 10/12 et 11/12, Hambourg 01/12, Berlin 02/12, Brême 07/12, Mayence 14/12 ; ⚠️ Berlin 04/11 <strong>complet</strong>.",
           "En 2027 : Berlin 20/01 et 17/02 ; Hambourg 11/02, 03/03, 27/05, 02/06 et 01/07 ; Mayence 18/02, 29/04, 24/06, 15/07, 21/10 et 16/12.",
           "<strong>Pas de TCF Canada</strong> chez Eloquia à Francfort (tout public, DAP, Québec, IRN), à Tübingen (pas de TCF sur le site) ni à Dresde (aucune session au module).",
           "Résultats sous 15 jours ouvrés ; 30 jours d'attente entre deux passations ; TCF IRN à 280 €, TCF Québec à 295 €."],
    stats=[("{n}", "centres agréés", "10 annoncent le TCF Canada"), ("295 €", "le TCF Canada", "210 € à Erlangen"),
           ("23", "sessions TCF Canada", "au module, jusqu'en déc. 2027"), ("17 nov.", "première place libre", "Munich, clôture le 8 nov.")],
    sections=[
        ("releve", "Le TCF Canada en Allemagne, centre par centre", releve([
            ("Instituts français de Berlin, Brême, Hambourg, Mayence, Munich et Stuttgart", "<strong>Canada</strong>, Québec, IRN, tout public",
             "Canada <strong>295 €</strong> · Québec 295 € · IRN 280 € · tout public 295 € (180 € les trois épreuves obligatoires)",
             "Canada, 2026 : Berlin 04/11 <strong>complet</strong> ; Munich 17/11 (clôture 08/11) ; Stuttgart 27/11 (19/11) ; Hambourg 01/12 (22/11) ; Berlin 02/12 (24/11) ; Munich 04/12 (29/11) ; Brême 07/12 (29/11) ; Stuttgart 10/12 et 11/12 (03/12) ; Mayence 14/12 (01/12). 2027 : Berlin 20/01 et 17/02, Hambourg 11/02, 03/03, 27/05, 02/06 et 01/07, Mayence 18/02, 29/04, 24/06, 15/07, 21/10 et 16/12. Réservation et paiement en ligne."),
            ("Institut culturel franco-allemand d'Aix-la-Chapelle", "<strong>Canada</strong>, Québec, IRN, tout public",
             "Canada <strong>295 €</strong> ; −15 % pour ses élèves, les scolaires, les étudiants et les demandeurs d'emploi",
             "06/11 et 11/12/2026 (clôture 04/12) ; réservation en ligne, avec un compte candidat, ou par e-mail."),
            ("Institut français de Bonn", "<strong>Canada</strong>, Québec, IRN, tout public, DAP", "non publié",
             "Le vendredi : 27/11/2026 (clôture 26/10) et 18/12/2026 (clôture 16/11). L'inscription ne vaut qu'une fois les frais reçus ; elle est ferme, sauf certificat médical (25 € retenus)."),
            ("Institut franco-allemand d'Erlangen", "<strong>Canada</strong>, Québec, IRN, tout public — sur ordinateur (e-TCF)",
             "Canada <strong>210 €</strong> · IRN 210 € · tout public 100 €, +55 € par épreuve facultative · Québec 50 à 55 € par épreuve",
             "Dates non publiées ; inscription par formulaire PDF."),
            ("Institut français de Mannheim", "<strong>Canada</strong>, Québec, IRN, tout public", "non publié",
             "Dates non publiées : écrire à l'adresse TCF de l'Institut."),
            ("Eloquia (Francfort)", "tout public, DAP, Québec, IRN — <strong>pas de TCF Canada</strong>", "non publié", "Réservation en ligne."),
            ("Institut culturel franco-allemand de Tübingen", "aucun TCF sur le site (DELF-DALF seulement)", "—", "—"),
            ("Institut français de Dresde", "cité parmi les centres TCF de l'Institut français d'Allemagne", "—",
             "Aucune session TCF au module d'inscription le 26 octobre 2026."),
        ]) + """
<p>Le module commun des Instituts français (« Anmeldung für Sprachzertifikate ») affichait 112 sessions TCF le 26 octobre
2026, chacune avec sa date limite d'inscription, en général une à deux semaines avant l'examen ; « Keine Plätze mehr frei »
signale une session complète. Le TEF Canada, l'autre test accepté par IRCC, avait des sessions publiées ce jour-là à Bonn
et à Erlangen sur la carte du Français des affaires.</p>"""),
        ("inscription", "S'inscrire au TCF Canada en Allemagne", """<p>Dans les six Instituts français du module, on choisit la session
sur la page « Anmeldung für Sprachzertifikate » de l'Institut français d'Allemagne (filtre TCF, puis la ville), on crée un
compte et on paie en ligne. À Aix-la-Chapelle, on réserve en ligne ou par e-mail en indiquant la déclinaison et la session ;
à Bonn, l'inscription n'est valable qu'une fois les frais reçus avant la clôture, et elle n'est ni remboursée ni reportée,
sauf certificat médical ; à Erlangen, on renvoie un formulaire PDF.</p>

<p>Les résultats arrivent sous 15 jours ouvrés ; l'attestation est numérique, avec un QR code et la photo du candidat, et
vaut deux ans. Il faut attendre 30 jours entre deux passations, quelle que soit la déclinaison.</p>"""),
    ],
    list_title="Les {n} centres TCF agréés en Allemagne",
    faq=[("Où passer le TCF Canada en Allemagne ?", "Dans l'un des dix centres qui l'annonçaient le 26 octobre 2026 : les Instituts français de Berlin, Brême, Hambourg, Mayence, Munich et Stuttgart (module d'inscription commun, 295 €), l'Institut culturel franco-allemand d'Aix-la-Chapelle (295 €), l'Institut français de Bonn, l'Institut franco-allemand d'Erlangen (210 €) et l'Institut français de Mannheim."),
         ("Combien coûte le TCF Canada en Allemagne ?", "295 € dans les Instituts français de Berlin, Brême, Hambourg, Mayence, Munich et Stuttgart, comme à Aix-la-Chapelle ; 210 € à Erlangen. Bonn et Mannheim ne publiaient pas leur tarif le 26 octobre 2026."),
         ("Quand a lieu le prochain TCF Canada à Berlin ?", "La session du 4 novembre 2026 était complète le 26 octobre ; les suivantes sont le 2 décembre 2026 (inscriptions jusqu'au 24 novembre), puis le 20 janvier et le 17 février 2027."),
         ("Peut-on passer le TCF Canada à Francfort ?", "Pas chez Eloquia, le seul centre TCF de Francfort : son site propose le TCF tout public, DAP, Québec et IRN, pas la version Canada. Les centres voisins qui l'annoncent sont Mayence (295 €) et Mannheim."),
         ("Le TCF IRN se passe-t-il en Allemagne ?", "Oui : 280 € dans les Instituts français de Berlin, Hambourg et Munich, avec des sessions jusqu'en juillet 2027, et 210 € à Erlangen. L'attestation est celle que délivre France Éducation international partout dans le monde.")],
    also=[("/centres/delf-allemagne/", "DELF et DALF en Allemagne", "Les sessions 2026-2027 et les prix, B2 à 201 €."),
          ("/centres/tcf-suisse/", "TCF en Suisse", "Deux centres annoncent le TCF Canada, à Montreux et à Zurich."), A_EUR, A_NCLC],
    sources="module d'inscription de l'Institut français d'Allemagne (« Anmeldung für Sprachzertifikate », 112 sessions TCF) et ses pages TCF ; sites de l'Institut culturel franco-allemand d'Aix-la-Chapelle (page TCF Kanada), de l'Institut français de Bonn, de l'Institut franco-allemand d'Erlangen (e-TCF), de l'Institut français de Mannheim, d'Eloquia et de l'Institut culturel franco-allemand de Tübingen ; carte des centres TEF du Français des affaires ; consultés le 26 octobre 2026.",
    badges=dict({k: OK_CA for k in DE_IF + ["aix-la-chapelle-institut-culturel-franco-allemand-aix-la-chapelle", "bonn-institut-francais",
                                             "erlangen-institut-franco-allemand", "mannheim-institut-francais"]},
                **{"francfort-eloquia-gmbh-sprachinstitut": NO_CA, "tubingen-institut-culturel-franco-allemand": [("no", "TCF absent du site")],
                   "dresde-institut-francais": [("no", "aucune session TCF publiée")]}),
    notes={"berlin-institut-francais": "Session TCF Canada du 4 novembre 2026 complète ; suivante le 2 décembre.",
           "aix-la-chapelle-institut-culturel-franco-allemand-aix-la-chapelle": "FEI fait précéder l'adresse de « Centre de passation » : l'Institut est au 62, Lothringerstraße.",
           "mannheim-institut-francais": "Dates et tarif non publiés le 26 octobre 2026."},
    urls=dict({k: IF_DE for k in DE_IF},
              **{"aix-la-chapelle-institut-culturel-franco-allemand-aix-la-chapelle": "https://www.ifaachen.de/zertifikate/sprachpruefung-tcf/tcf-kanada",
                 "bonn-institut-francais": "https://www.ifb.uni-bonn.de/pruefungen",
                 "erlangen-institut-franco-allemand": "https://www.dfi-erlangen.de/de/pruefungen/e-tcf",
                 "mannheim-institut-francais": "https://www.if-mannheim.eu/tcf/",
                 "francfort-eloquia-gmbh-sprachinstitut": "https://www.eloquia.com/pruefungen/fremdsprachenzertifikate/franzoesisch/tcf/"}),
))

# ===========================================================================
# ALLEMAGNE — DELF-DALF
# ===========================================================================
DE_IF_DELF = ["berlin-institut-francais-d-allemagne-antenne-de-berlin", "breme-institut-francais-bremen", "cologne-institut-francais-koln",
              "dusseldorf-institut-francais-dusseldorf", "hambourg-institut-francais-hambourg", "leipzig-institut-francais-leipzig",
              "mayence-institut-francais", "munich-institut-francais-munich", "stuttgart-institut-francais-stuttgart"]
PAGES.append(dict(EU,
    slug="delf-allemagne", exam="delf", file="fei_monde/delf_allemagne", layout="cities", chip="Allemagne",
    crumb="DELF en Allemagne",
    pointer="",
    title="DELF en Allemagne : dates 2026-2027, prix (B2 201 €)",
    desc="DELF et DALF en Allemagne : les sessions de novembre 2026 à novembre 2027, les prix (A1 137 €, B2 201 €, C1 224 €), les {n} centres et l'inscription.",
    h1="DELF et DALF en Allemagne : les dates 2026-2027, les prix et les {n} centres",
    intro="""En Allemagne, le DELF et le DALF tout public se passent dans <strong>{n} centres d'examen</strong>, dont neuf Instituts
français qui vendent leurs sessions sur un même module en ligne. Les écrits y tombent les mêmes jours : prochaine session
les <strong>19 et 20 novembre 2026</strong> (DALF le 21), inscriptions jusqu'au 8 à 13 novembre selon la ville ; puis
janvier, mars, juin, septembre et novembre 2027. Le DELF B2 coûte <strong>201 €</strong>, 170,85 € avec la réduction
de 15 % réservée aux élèves d'un cours de préparation de l'Institut.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 26 octobre 2026), coordonnés par le bureau de coopération linguistique et éducative de l'Institut français d'Allemagne.",
           "Novembre 2026 : A2 et B1 le 19, A1 et B2 le 20, DALF C1 et C2 le 21 novembre, dans les Instituts français de Berlin, Brême, Cologne, Düsseldorf, Hambourg, Leipzig, Mayence, Munich et Stuttgart.",
           "2027, écrits du B2 : <strong>22 janvier, 12 mars, 11 juin, 24 septembre, 19 novembre</strong> ; DALF les 23 janvier, 13 mars, 12 juin, 23 septembre et 20 novembre.",
           "Prix des Instituts français : <strong>A1 137 € · A2 161 € · B1 179 € · B2 201 € · C1 224 € · C2 253 €</strong> ; −15 % après un cours de préparation de l'Institut terminé 4 mois au plus avant l'examen.",
           "Les diplômes sont indépendants : on s'inscrit directement au niveau visé ; 50 points sur 100 pour l'obtenir.",
           "Résultats sous 15 jours ouvrés ; diplôme papier environ 6 mois après l'examen."],
    stats=[("{n}", "centres d'examen", "liste FEI du 26 octobre 2026"), ("201 €", "le DELF B2", "170,85 € avec −15 %"),
           ("20 nov.", "prochain B2", "clôture du 8 au 13 nov."), ("5", "sessions en 2027", "janv., mars, juin, sept., nov.")],
    sections=[
        ("calendrier", "Les sessions de novembre 2026 à novembre 2027", table(
            "Dates des écrits du DELF-DALF tout public au module d'inscription des Instituts français, relevées le 26 octobre 2026. Clôture : la date limite d'inscription, qui varie de quelques jours d'une ville à l'autre.",
            ["Session", "A1", "A2", "B1", "B2", "DALF C1 · C2", "Instituts français", "Clôture"],
            [("<strong>Nov. 2026</strong>", "20/11", "19/11", "19/11", "20/11", "21/11", "Berlin, Brême, Cologne, Düsseldorf, Hambourg, Leipzig, Mayence, Munich, Stuttgart", "08 au 13/11"),
             ("Janv. 2027", "22/01", "21/01", "21/01", "22/01", "23/01", "Cologne, Düsseldorf, Mayence, Stuttgart", "13 au 15/01"),
             ("Mars 2027", "12/03", "11/03", "11/03", "12/03", "13/03", "Berlin, Cologne, Düsseldorf, Hambourg, Munich, Stuttgart", "02 au 05/03"),
             ("Juin 2027", "11/06", "10/06", "10/06", "11/06", "12/06", "Berlin, Cologne, Düsseldorf, Hambourg, Mayence, Munich, Stuttgart", "01 au 04/06"),
             ("Sept. 2027", "24/09", "25/09", "25/09", "24/09", "23/09", "Hambourg, Mayence, Munich, Stuttgart", "14 au 17/09"),
             ("Nov. 2027", "19/11", "18/11", "18/11", "19/11", "20/11", "Hambourg, Mayence, Munich, Stuttgart", "09 au 12/11")]) + """
<p>Les oraux ont lieu à des dates propres à chaque centre. Le DELF junior a deux sessions au module, les 24 avril et
12 juin 2027 ; le DELF Prim, les 23 janvier et 5 juin 2027. Les autres centres de la liste — Aix-la-Chapelle, Bonn,
Erlangen, Francfort, Fribourg-en-Brisgau, Hanovre, Heidelberg, Karlsruhe, Kiel, Mannheim, Rostock, Sarrebruck, Tübingen —
gèrent leurs propres inscriptions : à Mannheim, la clôture de novembre 2026 tombe le 6 novembre.</p>"""),
        ("prix", "Combien coûte le DELF en Allemagne ?", table(
            "Prix du module d'inscription des Instituts français, relevés le 26 octobre 2026.",
            ["Niveau", "Prix", "Avec la réduction de 15 %"],
            [("DELF A1", "137 €", "116,45 €"), ("DELF A2", "161 €", "136,85 €"), ("DELF B1", "179 €", "152,15 €"),
             ("<strong>DELF B2</strong>", "<strong>201 €</strong>", "<strong>170,85 €</strong>"), ("DALF C1", "224 €", "190,40 €"),
             ("DALF C2", "253 €", "215,05 €"), ("DELF junior A1 à B2", "72 à 121 €", "—"), ("DELF Prim A1.1 à A2", "40 à 66 €", "—")], wide=False) + """
<p>La réduction de 15 % s'applique quand on a suivi un cours de préparation de l'Institut français terminé quatre mois au
plus avant l'examen. Les autres centres fixent leurs propres tarifs. Le DELF scolaire, à prix préférentiel, s'organise
avec les écoles et les ministères de l'Éducation des seize Länder.</p>"""),
        ("inscription", "S'inscrire, résultats et diplôme", """<p>Dans les Instituts français, on choisit sa session sur la page
« Anmeldung für Sprachzertifikate » (filtre DELF ou DALF, puis la ville), on crée un compte et on paie en ligne ; chaque
session affiche sa date limite. Les diplômes sont indépendants : on peut s'inscrire au B2 sans avoir passé l'A1, l'A2 ou
le B1. Chaque épreuve est notée sur 25 ; il faut 50 points sur 100, et au moins 5 dans chaque épreuve.</p>

<p>Le centre communique les résultats sous 15 jours ouvrés après la dernière épreuve ; le diplôme papier arrive environ
6 mois après l'examen, et une attestation de réussite peut être demandée en attendant.</p>"""),
    ],
    list_title="Les {n} centres d'examen DELF-DALF, ville par ville",
    faq=[("Quand a lieu le prochain DELF en Allemagne ?", "Les 19 et 20 novembre 2026 (A2 et B1 le 19, A1 et B2 le 20) et le 21 novembre pour le DALF, dans neuf Instituts français ; inscriptions jusqu'au 8 à 13 novembre selon la ville. Suivent janvier, mars, juin, septembre et novembre 2027."),
         ("Quelles sont les dates du DELF B2 en 2027 en Allemagne ?", "Le 22 janvier, le 12 mars, le 11 juin, le 24 septembre et le 19 novembre 2027 dans les Instituts français, chaque session dans quatre à sept villes. Le DALF C1 et C2 a lieu le lendemain (le 23 septembre en septembre)."),
         ("Combien coûte le DELF B2 en Allemagne ?", "201 € dans les Instituts français, 170,85 € avec la réduction de 15 % accordée après un cours de préparation de l'Institut. Le DALF coûte 224 € (C1) et 253 € (C2)."),
         ("Faut-il passer l'A1 avant le B2 ?", "Non : les diplômes DELF et DALF sont indépendants, on s'inscrit directement au niveau visé. Réussir le B1 ne donne pas pour autant l'A1 et l'A2."),
         ("Quand reçoit-on le diplôme ?", "Les résultats arrivent sous 15 jours ouvrés après la dernière épreuve ; le diplôme papier, environ 6 mois après l'examen. Une attestation de réussite peut être demandée avant.")],
    also=[("/centres/tcf-allemagne/", "TCF Canada en Allemagne", "Dix centres, 295 €, 23 sessions au module."),
          ("/centres/delf-suisse/", "DELF et DALF en Suisse", "Le calendrier national 2027, B2 de CHF 370 à 390."), A_DELF, A_DIPL],
    sources="module d'inscription de l'Institut français d'Allemagne (« Anmeldung für Sprachzertifikate », filtres DELF et DALF) et sa page « DELF DALF für Erwachsene » ; site de l'Institut français de Mannheim ; consultés le 26 octobre 2026.",
    notes={"mannheim-institut-francais-mannheim": "Clôture des inscriptions DELF-DALF de novembre 2026 : le 6 novembre (site de l'Institut).",
           "berlin-institut-francais-d-allemagne-antenne-de-berlin": "Sessions et inscription au module commun des Instituts français."},
    urls=dict({k: IF_DE for k in DE_IF_DELF}, **{"mannheim-institut-francais-mannheim": "https://www.if-mannheim.eu/delf-dalf/"}),
))

# ===========================================================================
# SUISSE — TCF
# ===========================================================================
CH_SE = ["berne-swiss-exams", "geneve-swiss-exams", "lausanne-swiss-exams", "winterthur-swiss-exams"]
PAGES.append(dict(EU,
    slug="tcf-suisse", exam="tcf", file="fei_monde/tcf_suisse", layout="cities", chip="Suisse",
    crumb="TCF en Suisse",
    pointer="TCF Canada annoncé à Montreux (ALPADIA, CHF 290) et à Zurich (Alliance française) ; ailleurs, le tout public seulement.",
    title="TCF Canada en Suisse : Montreux, Zurich, prix en CHF",
    desc="TCF en Suisse : seuls ALPADIA (Montreux, CHF 290) et l'Alliance française de Zurich annoncent le TCF Canada ; Swiss Exams et Fribourg, le tout public.",
    h1="TCF Canada en Suisse : les centres, les prix en CHF et les prochaines sessions",
    intro="""En Suisse, {n} centres sont agréés pour le TCF, mais <strong>deux seulement annoncent le TCF Canada</strong> :
ALPADIA Language Schools à Montreux (<strong>CHF 290</strong>, mais aucune date 2026 publiée) et l'Alliance française de
Zurich (dates et devis par e-mail). Swiss Exams — Berne, Genève, Lausanne, Winterthur — et le Centre de langues de
l'Université de Fribourg ne font passer que le <strong>TCF tout public</strong>, sur ordinateur, à CHF 320 et CHF 300.
Prochaine session : Fribourg le 12 novembre 2026. Pour un dossier canadien, le TEF Canada avait aussi des sessions
publiées à Genève le 26 octobre 2026.""",
    facts=["<strong>{n} centres agréés</strong> (liste FEI du 26 octobre 2026) : Swiss Exams dans quatre villes, l'Université de Fribourg, ALPADIA à Montreux et l'Alliance française de Zurich.",
           "<strong>TCF Canada</strong> : ALPADIA (Montreux), <strong>CHF 290</strong>, dates publiées pour 2025 seulement ; l'Alliance française de Zurich, sur demande.",
           "TCF tout public sur ordinateur : <strong>CHF 320</strong> chez Swiss Exams (CHF 160 les trois épreuves obligatoires), <strong>CHF 300</strong> à Fribourg (CHF 155).",
           "Prochaines sessions tout public : Fribourg 12/11/2026 (clôture 29/10), Lausanne 21/11 (clôture 23/10), Genève 04/12 et Berne 05/12/2026 (clôture 06/11).",
           "Selon l'Université de Fribourg, le TCF tout public vaut pour l'accès à la nationalité française si les cinq épreuves sont passées dans la même session.",
           "TEF Canada, l'autre test accepté par IRCC : sessions publiées à l'IFAGE de Genève le 26 octobre 2026."],
    stats=[("{n}", "centres agréés", "2 annoncent le TCF Canada"), ("CHF 290", "le TCF Canada", "ALPADIA, Montreux"),
           ("CHF 320", "le TCF tout public", "Swiss Exams ; CHF 300 à Fribourg"), ("12 nov.", "prochaine session", "Fribourg, clôture le 29 oct.")],
    sections=[
        ("releve", "Le TCF en Suisse, centre par centre", releve([
            ("ALPADIA Language Schools (Montreux)", "<strong>Canada</strong> et Québec, tout public et IRN",
             "Canada et Québec <strong>CHF 290</strong> (CHF 65 à 80 par épreuve) · tout public et IRN CHF 280",
             "Sept à huit sessions par an annoncées, mais seules les dates 2025 sont en ligne. Inscription par téléphone, au moins un mois avant ; paiement en espèces à l'arrivée."),
            ("Alliance française de Zurich", "tout public, Québec, <strong>Canada</strong>, IRN", "non publié (devis sur demande)",
             "« Dates fixes » communiquées par e-mail : informations, devis et inscription auprès de l'école de l'Alliance."),
            ("Swiss Exams (Berne, Genève, Lausanne, Winterthur)", "tout public seulement, sur ordinateur",
             "CHF 320 · CHF 160 les trois épreuves obligatoires · CHF 105 l'expression écrite ou orale seule",
             "Lausanne 21/11/2026 (clôture 23/10) ; Genève 04/12 et Berne 05/12 (clôture 06/11) ; 2027 : Lausanne 30/01 et 27/02, Genève 06/02, Berne 20/02. Résultats trois semaines après. Inscription en ligne."),
            ("Centre de langues de l'Université de Fribourg", "tout public seulement, sur ordinateur ; candidats externes admis",
             "CHF 300 · CHF 155 les épreuves obligatoires · CHF 90 par épreuve complémentaire",
             "12/11/2026 (clôture 29/10), 12/01/2027 (04/01), 04/03 (18/02), 29/04 (15/04), 06/07 (22/06), 31/08/2027 (17/08). Formulaire en ligne et pièce d'identité."),
        ]) + """
<p>Swiss Exams rappelle que les demandes de recorrection sont suspendues pour les sessions postérieures au 31 août 2026,
jusqu'à l'automne 2027 : un incident pendant les épreuves se signale au centre le jour même. La liste de France
Éducation international indique une option ordinateur pour cinq centres ; ALPADIA et l'Alliance de Zurich n'en déclarent
pas.</p>"""),
    ],
    list_title="Les {n} centres TCF agréés en Suisse",
    faq=[("Où passer le TCF Canada en Suisse ?", "Le 26 octobre 2026, deux centres agréés l'annonçaient : ALPADIA Language Schools à Montreux (CHF 290, dates 2026 non publiées : appeler l'école) et l'Alliance française de Zurich (dates et devis par e-mail). Swiss Exams et l'Université de Fribourg ne font passer que le TCF tout public."),
         ("Combien coûte le TCF en Suisse ?", "CHF 320 le TCF tout public complet chez Swiss Exams (CHF 160 les trois épreuves obligatoires), CHF 300 à l'Université de Fribourg, CHF 290 le TCF Canada chez ALPADIA à Montreux."),
         ("Quand a lieu le prochain TCF à Genève ou à Lausanne ?", "Chez Swiss Exams : Lausanne le 21 novembre 2026 (clôture le 23 octobre) et Genève le 4 décembre 2026 (clôture le 6 novembre), puis Lausanne les 30 janvier et 27 février 2027 et Genève le 6 février 2027 — en TCF tout public, sur ordinateur."),
         ("Le TCF tout public suffit-il pour la nationalité française ?", "Selon le Centre de langues de l'Université de Fribourg, il est reconnu pour un dossier d'accès à la nationalité si les épreuves obligatoires et les deux épreuves complémentaires sont passées dans la même session. Pour un dossier canadien, il faut le TCF Canada ou le TEF Canada."),
         ("Où passer le TEF Canada en Suisse ?", "La carte du Français des affaires affichait le 26 octobre 2026 des sessions TEF Canada à l'IFAGE, à Genève. Le TEF Canada est l'autre test de français accepté par IRCC.")],
    also=[("/centres/delf-suisse/", "DELF et DALF en Suisse", "Le calendrier national 2027 et les prix par centre."),
          ("/centres/tcf-allemagne/", "TCF Canada en Allemagne", "Dix centres, 295 €, des sessions chaque mois."), A_EUR, A_TEF],
    sources="module d'inscription de Swiss Exams (inscription-tcf.swiss-exams.ch) et sa page TCF ; pages TCF et « Dates d'examens et inscription » du Centre de langues de l'Université de Fribourg ; page des centres d'examen d'ALPADIA ; page « Examens TEF et TCF » de l'Alliance française de Zurich ; carte des centres TEF du Français des affaires ; consultés le 26 octobre 2026.",
    badges=dict({k: [("no", "tout public seulement")] for k in CH_SE + ["fribourg-centre-de-langues-de-l-universite"]},
                **{"montreux-alpadia-language-schools": [("ok", "TCF Canada"), ("part", "dates 2025 seulement")],
                   "zurich-alliance-francaise": [("ok", "TCF Canada"), ("part", "sur demande")]}),
    notes={"montreux-alpadia-language-schools": "Inscription aux examens : ALPADIA donne le +41 21 621 84 48 ; le numéro publié par FEI est incomplet."},
    urls=dict({k: "https://inscription-tcf.swiss-exams.ch/list" for k in CH_SE},
              **{"fribourg-centre-de-langues-de-l-universite": "https://www.unifr.ch/centredelangues/fr/tests/tcf/",
                 "montreux-alpadia-language-schools": "https://www.alpadia.com/en/our-exam-centres",
                 "zurich-alliance-francaise": "https://afzurich.ch/courses/examens-tef/"}),
))

# ===========================================================================
# SUISSE — DELF-DALF
# ===========================================================================
PAGES.append(dict(EU,
    slug="delf-suisse", exam="delf", file="fei_monde/delf_suisse", layout="cities", chip="Suisse",
    crumb="DELF en Suisse",
    pointer="",
    title="DELF en Suisse : dates 2027, prix en CHF, {n} centres",
    desc="DELF et DALF en Suisse : les cinq sessions 2027 (20 mars, 22 mai, 19 juin, 18 septembre, 13 novembre), les clôtures et les prix (B2 CHF 370 à 390).",
    h1="DELF et DALF en Suisse : le calendrier 2027, les prix et les {n} centres d'examen",
    intro="""En Suisse, le DELF et le DALF tout public suivent un <strong>calendrier national</strong>, publié sur delfdalf.ch par la
Fondation Esprit Francophonie : en 2027, les épreuves collectives ont lieu le <strong>samedi 20 mars</strong> (inscriptions
jusqu'au <strong>8 janvier</strong>), puis les 22 mai, 19 juin, 18 septembre et 13 novembre. On s'inscrit en ligne dans
l'un des centres régionaux, où le DELF B2 coûte de <strong>CHF 370 à 390</strong>. La session du 14 novembre 2026 est
close depuis le 11 septembre.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 26 octobre 2026), gérés par le service de coopération et d'action culturelle que nomme la liste de FEI (Zurich) ; calendrier et inscriptions sur delfdalf.ch.",
           "2027 : <strong>20 mars</strong> (clôture 8 janvier), <strong>22 mai</strong> (12 mars), <strong>19 juin</strong> (9 avril), <strong>18 septembre</strong> (6 août), <strong>13 novembre</strong> (10 septembre).",
           "Oraux au fil du mois de la session, selon le centre ; oral du DALF C2 la veille des écrits.",
           "DELF B2 : <strong>CHF 370</strong> à Neuchâtel, 375 à Genève et Lausanne, 380 à Berne et Liestal, 390 à Zurich (KV Zürich).",
           "Septembre : quatre centres seulement (Genève, Liestal, Lugano, Saint-Gall) ; DELF junior en mars, mai, juin et novembre ; DELF Prim en mai et juin.",
           "Programme d'examen envoyé par e-mail au plus tard deux semaines avant la première épreuve."],
    stats=[("{n}", "centres d'examen", "liste FEI du 26 octobre 2026"), ("20 mars", "première session 2027", "clôture le 8 janvier"),
           ("CHF 370-390", "le DELF B2", "selon le centre"), ("5", "sessions par an", "mars, mai, juin, sept., nov.")],
    sections=[
        ("calendrier", "Le calendrier national 2027", table(
            "Calendrier des examens 2027 pour la Suisse (version du 29 septembre 2026, delfdalf.ch), « sous réserve de toute modification ». Tous les niveaux ne sont pas ouverts dans tous les centres.",
            ["Session", "Épreuves collectives", "Oraux", "Oral C2", "Clôture des inscriptions"],
            [("<strong>Mars 2027</strong>", "samedi 20/03", "01 au 31/03", "vendredi 19/03", "<strong>vendredi 08/01/2027</strong>"),
             ("Mai 2027", "samedi 22/05", "01 au 31/05", "vendredi 21/05", "vendredi 12/03"),
             ("Juin 2027", "samedi 19/06", "01 au 30/06", "vendredi 18/06", "vendredi 09/04"),
             ("Septembre 2027", "samedi 18/09", "01 au 30/09", "vendredi 17/09", "vendredi 06/08"),
             ("Novembre 2027", "samedi 13/11", "01 au 30/11", "vendredi 12/11", "vendredi 10/09")]) + """
<p>Les sessions de mars et de novembre réunissent le plus de centres — Aarau, Bellinzone, Berne, Genève, Lausanne,
Liestal, Lucerne, Neuchâtel, Saint-Gall, Sierre, Weinfelden et les deux centres zurichois ; celle de septembre n'a lieu
qu'à Genève, Liestal, Lugano et Saint-Gall. Le calendrier 2026 plaçait la dernière session de l'année le samedi
14 novembre 2026, avec une clôture le 11 septembre.</p>"""),
        ("prix", "Combien coûte le DELF en Suisse ?", table(
            "Frais d'inscription affichés par les centres sur delfdalf.ch le 26 octobre 2026.",
            ["Niveau", "Genève · Lausanne", "Berne", "Liestal", "Zurich (KV Zürich)", "Neuchâtel"],
            [("DELF A1", "CHF 205", "CHF 200", "CHF 190", "CHF 200", "—"), ("DELF A2", "CHF 235", "CHF 230", "CHF 240", "CHF 230", "—"),
             ("DELF B1", "CHF 285", "CHF 290", "CHF 280", "CHF 290", "CHF 280"),
             ("<strong>DELF B2</strong>", "<strong>CHF 375</strong>", "<strong>CHF 380</strong>", "<strong>CHF 380</strong>", "<strong>CHF 390</strong>", "<strong>CHF 370</strong>"),
             ("DALF C1", "CHF 415", "CHF 410", "CHF 415", "CHF 420", "CHF 410"), ("DALF C2", "CHF 435", "CHF 430", "CHF 430", "CHF 430", "CHF 430")]) + """
<p>À Berne et à Zurich, un changement demandé après réception du programme d'examen ne s'accorde qu'exceptionnellement,
contre CHF 50 ; à Zurich, un report à une session ultérieure après la clôture coûte aussi CHF 50.</p>"""),
        ("inscription", "S'inscrire", """<p>L'inscription se fait en ligne depuis delfdalf.ch, en choisissant son centre régional. Le
programme d'examen personnel — avec les adresses des épreuves, qui n'ont pas toujours lieu dans les mêmes locaux — arrive
par e-mail au plus tard deux semaines avant la première épreuve ; programme et résultats ne partent que par voie
électronique, d'où la consigne de donner une adresse e-mail privée.</p>"""),
    ],
    list_title="Les {n} centres d'examen DELF-DALF agréés en Suisse",
    faq=[("Quelles sont les dates du DELF 2027 en Suisse ?", "Les épreuves collectives ont lieu le samedi 20 mars, le 22 mai, le 19 juin, le 18 septembre et le 13 novembre 2027 ; les clôtures d'inscription tombent le 8 janvier, le 12 mars, le 9 avril, le 6 août et le 10 septembre 2027."),
         ("Combien coûte le DELF B2 en Suisse ?", "De CHF 370 à CHF 390 selon le centre : CHF 370 à Neuchâtel, 375 à Genève et Lausanne, 380 à Berne et Liestal, 390 au KV Zürich. Le DALF C1 coûte CHF 410 à 420."),
         ("Peut-on encore s'inscrire pour novembre 2026 ?", "Non : la session du 14 novembre 2026 a fermé ses inscriptions le 11 septembre. La prochaine est celle du 20 mars 2027, avec une clôture le 8 janvier 2027."),
         ("Où passer le DELF à Genève ou à Lausanne ?", "Au Centre d'examens Lac Léman, chez l'IFAGE (place des Augustins 19, à Genève), qui organise aussi les sessions de Lausanne : DELF B2 à CHF 375."),
         ("Quand reçoit-on son programme d'examen ?", "Par e-mail, au plus tard deux semaines avant la première épreuve. Il donne les adresses des épreuves, qui changent parfois d'une session à l'autre.")],
    also=[("/centres/tcf-suisse/", "TCF en Suisse", "Le TCF Canada à Montreux et à Zurich, le tout public ailleurs."),
          ("/centres/delf-allemagne/", "DELF et DALF en Allemagne", "Six sessions de novembre 2026 à novembre 2027."), A_DELF, A_DIPL],
    sources="calendriers des examens 2026 et 2027 pour la Suisse (PDF des 21 avril et 29 septembre 2026) et pages des centres d'examen de delfdalf.ch (Genève-Lausanne, Berne, Liestal, Zurich Limmat, Neuchâtel), consultés le 26 octobre 2026.",
    org_url="https://www.delfdalf.ch/",
    urls={"geneve-ifage-fondation-pour-la-formation-des-adultes": "https://www.delfdalf.ch/centredexamen-geneve-lausanne",
          "berne-wks-kv-bildung-ag": "https://www.delfdalf.ch/prufungszentrum-bern",
          "liestal-centre-d-examens-region-baloise": "https://www.delfdalf.ch/prufungszentrum-basel",
          "zurich-wirtschaftschule-kv-zurich": "https://www.delfdalf.ch/prufungszentrum-zurich-limmat",
          "zurich-minerva-schweiz-ag": "https://www.delfdalf.ch/prufungszentrum-zurich-minerva",
          "neuchatel-lycee-jean-piaget": "https://www.delfdalf.ch/centredexamens-neuchatel",
          "lucerne-smarttalk-gmbh": "https://www.delfdalf.ch/prufungszentrum-luzern",
          "aarau-hkv-swiss-ag": "https://www.delfdalf.ch/centres-examens/aarau",
          "altstatten-wzr-rorschach-rheintal": "https://www.delfdalf.ch/prufungszentrum/saint-gall-altstaetten",
          "bellinzone-scuola-cantonale-di-commercio": "https://www.delfdalf.ch/prufungszentrum-chur-bellinzona",
          "sierre-hes-so-valais-wallis": "https://www.delfdalf.ch/centres-examens/sierre",
          "weinfelden-bildungszentrum-wirtschaft-weinfelden": "https://www.delfdalf.ch/prufungszentrum-weinfelden-thurgau"},
    notes={"geneve-ifage-fondation-pour-la-formation-des-adultes": "Centre d'examens Lac Léman : organise aussi les sessions de Lausanne.",
           "zurich-wirtschaftschule-kv-zurich": "Centre d'examens « Zurich Limmat » sur delfdalf.ch."},
))

# ===========================================================================
# BELGIQUE — TCF (+ DELF en bref)
# ===========================================================================
PAGES.append(dict(EU,
    slug="tcf-belgique", exam="tcf", file="fei_monde/tcf_belgique", layout="cities", chip="Belgique",
    crumb="TCF en Belgique",
    pointer="Bruxelles (268 €, le 9 décembre 2026) et Gand (260 €) font passer le TCF Canada, sur ordinateur.",
    title="TCF Canada en Belgique : Bruxelles 268 €, Gand 260 €",
    desc="TCF Canada en Belgique : l'Alliance française de Bruxelles-Europe (268 €, session du 9 décembre 2026) et celle de Gand (260 €), sur ordinateur.",
    h1="TCF Canada en Belgique : les deux centres, les prix et les dates",
    intro="""En Belgique, deux centres sont agréés pour le TCF, et <strong>tous deux font passer le TCF Canada</strong>, sur
ordinateur : l'<strong>Alliance française de Bruxelles-Europe</strong> (<strong>268 €</strong>, prochaine session le
<strong>mercredi 9 décembre 2026</strong>) et l'<strong>Alliance française de Flandre orientale</strong>, à Gand
(<strong>260 €</strong>, trois sessions par an, dont le calendrier 2027 n'était pas publié le 26 octobre 2026). On réserve
et on paie en ligne, sur le site de chaque Alliance ; l'oral a lieu le jour même des épreuves écrites.""",
    facts=["<strong>2 centres agréés</strong> (liste FEI du 26 octobre 2026), les deux avec le TCF Canada, sur ordinateur.",
           "Bruxelles : TCF Canada <strong>268 €</strong> le 9 décembre 2026 ; TCF tout public 258 € le 10 décembre, TCF IRN 220 € le 14 décembre.",
           "Gand : TCF Canada <strong>260 €</strong>, tout public 250 € ; trois sessions par an (février, mai, août-septembre) ; 2027 non publié.",
           "Bruxelles remet une attestation provisoire le jour même ; Gand affiche les résultats des QCM à la fin du test, les résultats complets sous 15 jours ouvrés.",
           "30 jours d'attente entre deux passations ; toute inscription est nominative.",
           "DELF-DALF : 6 centres en Belgique ; session du 17 au 26 novembre 2026, inscriptions jusqu'au 3 novembre à Gand (closes à Bruxelles) ; 2027 pas encore programmé."],
    stats=[("2", "centres agréés", "les deux avec le TCF Canada"), ("268 €", "le TCF Canada à Bruxelles", "260 € à Gand"),
           ("9 déc.", "prochaine session", "Bruxelles, 2026"), ("30 jours", "entre deux passations", "")],
    sections=[
        ("releve", "Le TCF en Belgique, centre par centre", releve([
            ("Alliance française de Bruxelles-Europe", "<strong>Canada</strong>, IRN, tout public — sur ordinateur",
             "Canada <strong>268 €</strong> · tout public 258 € · IRN 220 €",
             "Canada mercredi 09/12/2026 (10 h–12 h 40, oral l'après-midi) ; tout public 10/12 ; IRN 14/12/2026. Convocation par e-mail au plus tard 5 jours avant ; attestation provisoire le jour même, certificat de FEI sous deux semaines."),
            ("Alliance française de Flandre orientale (Gand)", "<strong>Canada</strong>, IRN, tout public — sur ordinateur",
             "Canada <strong>260 €</strong> · tout public 250 €",
             "Trois sessions par an (février, mai, août-septembre) : en 2026, Canada les 12 et 16/02 et du 20/08 au 17/09 ; 2027 non publié. Paiement à l'inscription : le formulaire seul ne vaut pas inscription. Résultats complets sous 15 jours ouvrés."),
        ]) + """
<p>À Bruxelles, une demande d'horaire particulier pour l'oral s'envoie au service des examens avant la fin des
inscriptions ; les candidats sont photographiés le jour des épreuves. À Gand, une annulation après la clôture n'est
remboursée que sur justificatif (un certificat médical, par exemple), moins des frais de dossier d'environ 2 €.</p>"""),
        ("delf", "Le DELF et le DALF en Belgique", """<p>Le DELF et le DALF se passent dans 6 centres (liste FEI du 26 octobre
2026) — les Alliances françaises de Bruxelles-Europe, d'Anvers et de Flandre orientale, KU Leuven Kulak à Courtrai,
l'Institut supérieur des langues vivantes de l'Université de Liège et l'École européenne de Mol —, sous la gestion
centrale de l'Alliance de Bruxelles-Europe. Celle-ci tient quatre sessions tout public par an : en 2026, mars, juin,
septembre et novembre, avec des écrits du 17 au 26 novembre et des inscriptions closes le 24 octobre. Le 26 octobre
2026, aucune session 2027 n'était encore en vente et les tarifs n'étaient pas affichés ; les apprenants de l'Alliance
ont 10 % de réduction. À Gand, les inscriptions de novembre restent ouvertes jusqu'au 3 novembre : dates, prix et centres
sur notre page <a href="/centres/delf-belgique/">DELF et DALF en Belgique</a>.</p>"""),
    ],
    list_title="Les {n} centres TCF agréés en Belgique",
    faq=[("Où passer le TCF Canada en Belgique ?", "À l'Alliance française de Bruxelles-Europe, avenue des Arts 46 (268 €), ou à l'Alliance française de Flandre orientale, Henleykaai 86 à Gand (260 €) : ce sont les deux centres TCF agréés du pays, et tous deux proposent la version Canada, sur ordinateur."),
         ("Quand a lieu le prochain TCF Canada à Bruxelles ?", "Le mercredi 9 décembre 2026, de 10 h à 12 h 40 pour les épreuves écrites, l'oral ayant lieu l'après-midi. Gand n'avait pas encore publié ses sessions 2027 le 26 octobre 2026."),
         ("Combien coûte le TCF Canada en Belgique ?", "268 € à Bruxelles et 260 € à Gand. Le TCF tout public coûte 258 € à Bruxelles et 250 € à Gand, le TCF IRN 220 € à Bruxelles."),
         ("Quand reçoit-on ses résultats ?", "À Bruxelles, une attestation provisoire est remise le jour des épreuves et le certificat de France Éducation international arrive sous deux semaines ; à Gand, les résultats complets arrivent sous 15 jours ouvrés."),
         ("Peut-on passer le DELF à Bruxelles en 2027 ?", "Oui, mais les sessions 2027 n'étaient pas encore programmées le 26 octobre 2026. En 2026, l'Alliance de Bruxelles-Europe en a tenu quatre : mars, juin, septembre et novembre.")],
    also=[("/centres/delf-belgique/", "DELF et DALF en Belgique", "Du 17 au 26 novembre 2026, B2 à 191 € à Gand."),
          ("/centres/tcf-pays-bas/", "TCF Canada aux Pays-Bas", "Amsterdam 290 €, La Haye, Rotterdam."),
          ("/centres/tcf-france/", "Centres TCF en France", "Lille et le Nord, de l'autre côté de la frontière."), A_EUR, A_NCLC],
    sources="sites de l'Alliance française de Bruxelles-Europe (pages TCF Canada, TCF IRN, TCF tout public et DELF-DALF tout public, onglets Calendrier et S'inscrire) et de l'Alliance française de Flandre orientale (page TCF), consultés le 26 octobre 2026 ; liste DELF-DALF de FEI pour la Belgique, lue le même jour.",
    badges={"bruxelles-alliance-francaise-de-bruxelles-europe": OK_CA, "gand-alliance-francaise-de-flandre-orientale": OK_CA},
    urls={"bruxelles-alliance-francaise-de-bruxelles-europe": "https://alliancefr.be/passer-un-examen/tcf/tcf-canada"},
))

# ===========================================================================
# ITALIE — TCF
# ===========================================================================
IT_CA = ["turin-alliance-francaise", "genes-alliance-francaise", "milan-institut-francais-italia", "venise-alliance-francaise",
         "bari-alliance-francaise", "latina-alliance-francaise-sud-latium", "aoste-alliance-francaise"]
PAGES.append(dict(EU,
    slug="tcf-italie", exam="tcf", file="fei_monde/tcf_italie", layout="cities", chip="Italie",
    crumb="TCF en Italie",
    pointer="Sept centres annoncent le TCF Canada, de 210 € (Gênes) à 250 € (Venise) ; Milan 240 €, Turin 220 €.",
    title="TCF Canada en Italie : 7 centres, 210 à 250 €, dates",
    desc="TCF Canada en Italie : Turin 220 €, Gênes 210 €, Milan 240 €, Venise 250 €, Bari, Aoste, Latina ; les sessions de novembre 2026 à 2027.",
    h1="TCF Canada en Italie : les centres qui le proposent, les prix et les dates",
    intro="""En Italie, {n} centres sont agréés pour le TCF ; le 26 octobre 2026, <strong>sept annonçaient le TCF Canada</strong>
sur leur site : les Alliances françaises de Turin (<strong>220 €</strong>), Gênes (<strong>210 €</strong>), Venise
(<strong>250 €</strong>), Bari (220 €), Aoste et Latina, et l'Institut français de Milan (<strong>240 €</strong>). Prochaines
sessions : Latina le 13 novembre, Turin le 1er décembre, Milan le 10 décembre, Venise le 16 décembre 2026, Gênes le
16 janvier 2027. Le Centre Saint-Louis de Rome ne propose que le tout public, l'IRN et le Québec.""",
    facts=["<strong>{n} centres agréés</strong> (liste FEI du 26 octobre 2026), <strong>7 qui annoncent le TCF Canada</strong> : Turin, Gênes, Venise, Bari, Aoste, Latina et l'Institut français de Milan.",
           "TCF Canada : <strong>210 €</strong> à Gênes, <strong>220 €</strong> à Turin et à Bari, <strong>240 €</strong> à Milan, <strong>250 €</strong> à Venise ; Aoste et Latina ne publient pas leur tarif.",
           "Sessions : Latina 13/11 et 11/12 ; Turin 01/12 (clôture 06/11) ; Milan 10/12 (inscriptions jusqu'au 30/10) ; Venise 16/12/2026 (clôture 13/11) ; Gênes 16/01/2027 (clôture 21/12).",
           "En 2027 : Milan 09/03 ; Turin 16/03 et 06/07 ; Gênes 06/03, 08/05 et 10/07.",
           "<strong>Pas de TCF Canada</strong> au Centre Saint-Louis de Rome (tout public, IRN, Québec) ni à l'Alliance de Padoue (tout public seulement).",
           "TEF Canada, l'autre test accepté par IRCC : sessions publiées par l'Alliance française de Vicence le 26 octobre 2026."],
    stats=[("{n}", "centres agréés", "7 annoncent le TCF Canada"), ("210–250 €", "le TCF Canada", "selon le centre"),
           ("13 nov.", "prochaine session", "Latina ; Turin le 1er déc."), ("2 ans", "de validité", "")],
    sections=[
        ("releve", "Le TCF Canada en Italie, centre par centre", releve([
            ("Alliance française de Turin", "<strong>Canada</strong>, Québec, IRN, tout public — sur ordinateur (clavier QWERTY)",
             "Canada <strong>220 €</strong>", "Mardi 01/12/2026 (clôture 06/11), 16/03/2027 (19/02), 06/07/2027 (04/06). Formulaire en ligne, puis virement."),
            ("Alliance française de Gênes", "<strong>Canada</strong>, Québec, IRN, tout public — sur papier",
             "Canada <strong>210 €</strong> · IRN 160 € · tout public 100 € (+50 € par épreuve facultative)",
             "16/01/2027 (clôture 21/12/2026), 06/03 (10/02), 08/05 (13/04), 10/07/2027 (06/06). Inscription par e-mail ou sur place ; résultats en une vingtaine de jours."),
            ("Institut français de Milan", "<strong>Canada</strong>, Québec, tout public", "Canada <strong>240 €</strong>",
             "10/12/2026 (inscriptions du 05 au 30/10) et 09/03/2027 (du 11 au 31/01). Photo prise le jour de l'examen."),
            ("Alliance française de Venise", "<strong>Canada</strong>, Québec, IRN, tout public",
             "Canada <strong>250 €</strong> · IRN 160 € · tout public 110 € (+65 € par épreuve facultative)",
             "18/11/2026 (clôture 16/10) et 16/12/2026 (clôture 13/11)."),
            ("Alliance française de Bari", "<strong>Canada</strong>, Québec, IRN, tout public", "Canada <strong>220 €</strong> (4 × 55 €) · IRN 140 €",
             "Dates non publiées sur la page TCF Canada."),
            ("Alliance française Sud Latium (Latina)", "<strong>Canada</strong>, Québec, IRN, tout public — sur ordinateur", "non publié",
             "Canada et IRN : 13/11 et 11/12/2026 ; 2027 non publié."),
            ("Alliance française d'Aoste", "<strong>Canada</strong>, tout public", "non publié", "Dates non publiées."),
            ("Institut français – Centre Saint-Louis (Rome)", "tout public, IRN, Québec — <strong>pas de TCF Canada</strong>", "non publié",
             "30/11/2026 ; inscriptions ouvertes le mois précédent, closes 10 jours ouvrés avant ; résultats en deux semaines."),
            ("Alliance française de Padoue", "tout public seulement", "non publié", "Formulaire, puis virement."),
            ("Alliance française de Vicence", "TCF (version non précisée)", "non publié", "Session extraordinaire DFP-TEF-TCF le 18/12/2026 (inscription jusqu'au 26/10) ; autres dates sur demande."),
        ]) + """
<p>Bologne (site inaccessible), Naples (centre linguistique de l'université, site injoignable), Palerme (pas de page TCF)
et Trieste (site vide) n'ont pu être relevés le 26 octobre 2026 : leurs contacts figurent dans la liste ci-dessous.
Chaque centre choisit ses dates — « le sessioni d'esame sono a discrezione di ogni singolo centro », rappelle Venise.</p>"""),
    ],
    list_title="Les {n} centres TCF agréés en Italie",
    faq=[("Où passer le TCF Canada en Italie ?", "Le 26 octobre 2026, sept centres agréés l'annonçaient : les Alliances françaises de Turin, Gênes, Venise, Bari, Aoste et Latina, et l'Institut français de Milan. Le Centre Saint-Louis de Rome ne le propose pas."),
         ("Combien coûte le TCF Canada en Italie ?", "210 € à Gênes, 220 € à Turin et à Bari, 240 € à l'Institut français de Milan, 250 € à Venise. Aoste et Latina ne publiaient pas leur tarif."),
         ("Peut-on passer le TCF Canada à Rome ?", "Pas au Centre Saint-Louis, l'Institut français de Rome : il propose le TCF tout public, le TCF IRN et le TCF Québec. Le centre le plus proche qui l'annonce est l'Alliance française Sud Latium, à Latina."),
         ("Quand a lieu le prochain TCF Canada à Milan ?", "Le 10 décembre 2026, avec des inscriptions du 5 au 30 octobre, puis le 9 mars 2027 (inscriptions du 11 au 31 janvier), à 240 €."),
         ("Le TCF se passe-t-il sur ordinateur en Italie ?", "Cela dépend du centre : Turin et Latina le font passer sur ordinateur ; Gênes, pour le moment, uniquement sur papier.")],
    also=[("/centres/delf-italie/", "DELF et DALF en Italie", "Février, avril et juin 2027, B2 à 160 €."),
          ("/centres/tcf-suisse/", "TCF en Suisse", "ALPADIA (Montreux) et l'Alliance de Zurich annoncent le TCF Canada."),
          ("/centres/tcf-france/", "Centres TCF en France", "Nice, Lyon, Grenoble, de l'autre côté des Alpes."), A_EUR, A_NCLC],
    sources="calendrier TCF Canada 2026-2027 (PDF) de l'Alliance française de Turin ; pages TCF des Alliances françaises de Gênes, Venise, Bari (TCF Canada), Latina (Sud Latium), Aoste, Padoue et Vicence ; calendrier TCF 2026-2027 de l'Institut français de Milan ; page TCF de l'Institut français – Centre Saint-Louis de Rome ; carte des centres TEF du Français des affaires ; consultés le 26 octobre 2026.",
    badges=dict({k: OK_CA for k in IT_CA},
                **{"rome-institut-francais-centre-saint-louis": NO_CA, "padoue-alliance-francaise-di-padova": [("no", "tout public seulement")]}),
    notes={"genes-alliance-francaise": "TCF sur papier seulement pour le moment (site de l'Alliance).",
           "bologne-alliance-francaise": "Site inaccessible le 26 octobre 2026 : non relevé.",
           "naples-centro-linguistico-di-ateneo": "Site injoignable le 26 octobre 2026 : non relevé."},
    urls={"turin-alliance-francaise": "https://www.alliancefrto.it/esami-e-certificazioni/",
          "genes-alliance-francaise": "http://www.alliancefrge.it/esami-e-certificazioni",
          "milan-institut-francais-italia": "https://www.institutfrancais.it/fr/milan/calendrier-des-epreuves-du-tcf-tcf-quebec-et-tcf-canada",
          "venise-alliance-francaise": "https://afvenezia.it/certificazioni/tcf/",
          "bari-alliance-francaise": "https://alliancefrba.it/prod/tcf-canada/",
          "latina-alliance-francaise-sud-latium": "https://afsudlatium.it/tcf/",
          "aoste-alliance-francaise": "https://alliancefraoste.it/tcf/",
          "rome-institut-francais-centre-saint-louis": "https://www.ifcsl.com/centre-saint-louis/tcf"},
))

# ===========================================================================
# PAYS-BAS — TCF
# ===========================================================================
NL_AF = ["amsterdam-alliance-francaise", "la-haye-alliance-francaise", "rotterdam-alliance-francaise"]
PAGES.append(dict(EU,
    slug="tcf-pays-bas", exam="tcf", file="fei_monde/tcf_pays_bas", layout="cities", chip="Pays-Bas",
    crumb="TCF aux Pays-Bas",
    pointer="Les Alliances d'Amsterdam (290 €), de La Haye et de Rotterdam annoncent le TCF Canada.",
    title="TCF Canada aux Pays-Bas : Amsterdam 290 €, dates",
    desc="TCF Canada aux Pays-Bas : les Alliances françaises d'Amsterdam (290 €, prochaine place le 13 janvier 2027), de La Haye et de Rotterdam.",
    h1="TCF Canada aux Pays-Bas : les centres, les prix et les dates",
    intro="""Aux Pays-Bas, {n} centres sont agréés pour le TCF, et les <strong>trois Alliances françaises</strong> — Amsterdam,
La Haye et Rotterdam — annoncent le TCF Canada. Amsterdam le fait passer sur ordinateur à <strong>290 €</strong> : sa
session du 25 novembre 2026 était complète le 26 octobre, la suivante a lieu le <strong>13 janvier 2027</strong>
(inscription avant le 29 décembre). La Haye vend ses sessions sur son module en ligne ; Rotterdam affiche de 75 à 300 €
selon la version. Les quatre autres centres sont des établissements d'enseignement.""",
    facts=["<strong>{n} centres agréés</strong> (liste FEI du 26 octobre 2026) : trois Alliances françaises, l'Institut français des Pays-Bas à Groningen et trois hautes écoles (Leeuwarden, Nimègue, Utrecht).",
           "<strong>TCF Canada à Amsterdam : 290 €</strong> ; ⚠️ 25/11/2026 complet ; 13/01/2027 ouvert, inscription avant le 29/12/2026.",
           "TCF IRN à Amsterdam : 205 €, le 16/12/2026 (inscription avant le 01/12) ; TCF Québec : 75 € par épreuve, dates sur demande.",
           "La Haye : TCF Canada, Québec, IRN et tout public, sessions à réserver en ligne ; attestation sous 15 jours ouvrés.",
           "Rotterdam : TCF tout public, Québec, Canada et IRN, de 75 à 300 € selon la version.",
           "TEF Canada, l'autre test accepté par IRCC : sessions publiées par l'Alliance française de La Haye le 26 octobre 2026."],
    stats=[("{n}", "centres agréés", "3 Alliances avec le TCF Canada"), ("290 €", "le TCF Canada", "à Amsterdam"),
           ("13 janv.", "prochaine place", "Amsterdam, 2027"), ("205 €", "le TCF IRN", "à Amsterdam")],
    sections=[
        ("releve", "Le TCF aux Pays-Bas, centre par centre", releve([
            ("Alliance française d'Amsterdam", "<strong>Canada</strong>, Québec, IRN, tout public — sur ordinateur",
             "Canada <strong>290 €</strong> · IRN 205 € · Québec 75 € par épreuve",
             "Canada : 25/11/2026 <strong>complet</strong> ; 13/01/2027 (inscription avant le 29/12/2026). IRN : 16/12/2026 (avant le 01/12). Tout public : 27/01/2027 (avant le 12/01). Québec sur demande. Convocation par e-mail."),
            ("Alliance française de La Haye", "<strong>Canada</strong>, Québec, IRN, tout public", "non relevé (module en ligne)",
             "Sessions à réserver sur le module de l'Alliance ; attestation de résultats sous 15 jours ouvrés, valable deux ans."),
            ("Alliance française de Rotterdam", "<strong>Canada</strong>, Québec, IRN, tout public", "75 € à 300 € selon la version",
             "Dates non publiées sur la page TCF."),
            ("Institut français des Pays-Bas (Groningen), NHL Stenden (Leeuwarden), HAN (Nimègue), Hogeschool Utrecht",
             "non publié", "—", "Pas de page TCF trouvée le 26 octobre 2026 : contacter l'établissement."),
        ])),
    ],
    list_title="Les {n} centres TCF agréés aux Pays-Bas",
    faq=[("Où passer le TCF Canada aux Pays-Bas ?", "Dans l'une des trois Alliances françaises, qui l'annonçaient le 26 octobre 2026 : Amsterdam (290 €, sur ordinateur), La Haye et Rotterdam."),
         ("Quand a lieu le prochain TCF Canada à Amsterdam ?", "La session du 25 novembre 2026 était complète le 26 octobre ; la suivante a lieu le 13 janvier 2027, avec une inscription avant le 29 décembre 2026."),
         ("Combien coûte le TCF Canada aux Pays-Bas ?", "290 € à l'Alliance française d'Amsterdam. Rotterdam affiche de 75 à 300 € selon la version ; La Haye vend ses sessions sur son module en ligne."),
         ("Où passer le TCF IRN pour la nationalité française aux Pays-Bas ?", "À l'Alliance française d'Amsterdam, 205 €, le 16 décembre 2026 (inscription avant le 1er décembre), ou dans les Alliances de La Haye et de Rotterdam.")],
    also=[("/centres/delf-pays-bas/", "DELF et DALF aux Pays-Bas", "Mars et juin 2027 à Amsterdam, B2 à 175 €."),
          ("/centres/tcf-belgique/", "TCF Canada en Belgique", "Bruxelles 268 €, Gand 260 €."),
          ("/centres/tcf-allemagne/", "TCF Canada en Allemagne", "Dix centres, 295 €."), A_EUR, A_TEF],
    sources="pages TCF des Alliances françaises d'Amsterdam, de La Haye et de Rotterdam, et carte des centres TEF du Français des affaires, consultées le 26 octobre 2026.",
    badges={k: OK_CA for k in NL_AF},
    notes={"amsterdam-alliance-francaise": "Session TCF Canada du 25 novembre 2026 complète ; suivante le 13 janvier 2027."},
    urls={"amsterdam-alliance-francaise": "https://www.afamsterdam.nl/en/certifications/tcf/",
          "la-haye-alliance-francaise": "https://www.aflahaye.nl/diplomes-tests/tcf/",
          "rotterdam-alliance-francaise": "http://www.alliancerotterdam.nl/produit/tcf/"},
))

# ===========================================================================
# PORTUGAL — TCF
# ===========================================================================
PAGES.append(dict(EU,
    slug="tcf-portugal", exam="tcf", file="fei_monde/tcf_portugal", layout="cities", chip="Portugal",
    crumb="TCF au Portugal",
    pointer="Porto et Faro (220 €), Viseu (211 €) affichent un tarif TCF Canada ; à Faro, date au choix.",
    title="TCF Canada au Portugal : Porto, Faro, Viseu, prix",
    desc="TCF Canada au Portugal : 220 € à Porto et à Faro (Algarve, date au choix sur ordinateur), 211 € à Viseu ; Lisbonne et Coimbra sur demande.",
    h1="TCF Canada au Portugal : les centres, les prix et les sessions",
    intro="""Au Portugal, {n} centres sont agréés pour le TCF. Le 26 octobre 2026, trois Alliances françaises affichaient un
tarif TCF Canada : <strong>Porto</strong> et <strong>Faro</strong> (Algarve), <strong>220 €</strong>, et
<strong>Viseu</strong>, <strong>211 €</strong>. À Faro, le test se passe sur ordinateur n'importe quel jour ouvré, à une
date choisie par le candidat au moins 7 jours à l'avance ; ailleurs, aucune date n'est en ligne : il faut contacter
l'Alliance. Lisbonne et Coimbra ne précisent ni la version ni le prix.""",
    facts=["<strong>{n} centres agréés</strong> (liste FEI du 26 octobre 2026) : les Alliances françaises de Lisbonne, Porto, Coimbra, Viseu et de l'Algarve (Faro), et l'institut de langues de l'Universidade Nova de Lisboa.",
           "TCF Canada : <strong>220 €</strong> à Porto et à Faro, <strong>211 €</strong> à Viseu.",
           "Faro : TCF sur ordinateur à la demande, tout jour ouvré sauf du 8 au 21 août et la seconde quinzaine de décembre, réservé 7 jours avant au moins.",
           "TCF IRN 220 € à Faro et à Porto ; TCF tout public 100 € les épreuves obligatoires à Faro.",
           "Lisbonne : TCF présenté sans version ni tarif, formulaire de contact ; Coimbra : calendrier et prix sur demande."],
    stats=[("{n}", "centres agréés", "3 affichent le TCF Canada"), ("220 €", "le TCF Canada", "Porto et Faro ; 211 € à Viseu"),
           ("7 jours", "de délai à Faro", "date au choix du candidat"), ("2 ans", "de validité", "")],
    sections=[
        ("releve", "Le TCF au Portugal, centre par centre", releve([
            ("Alliance française de l'Algarve (Faro)", "<strong>Canada</strong>, Québec, IRN, tout public — sur ordinateur",
             "Canada ou Québec <strong>220 €</strong> · IRN 220 € · tout public 100 € (+65 € écrit, +55 € oral)",
             "Tout jour ouvré, sauf du 8 au 21 août et la seconde quinzaine de décembre, à une date fixée par le candidat au moins 7 jours avant. Fiche d'inscription en ligne."),
            ("Alliance française de Porto", "<strong>Canada</strong>, IRN, Québec, tout public", "Canada <strong>220 €</strong> · IRN 220 €",
             "Dates non publiées."),
            ("Alliance française de Viseu", "<strong>Canada</strong>, Québec", "Canada <strong>211 €</strong>",
             "Dates en ligne périmées ; inscription au moins 7 jours avant, par formulaire et preuve de paiement ; sessions supplémentaires sur demande, avec supplément."),
            ("Alliance française de Coimbra", "TCF sur ordinateur (versions non précisées)", "sur demande",
             "Calendrier et prix sur demande ; inscription sur place."),
            ("Alliance française de Lisbonne", "TCF (versions non précisées)", "non publié", "Formulaire de contact sur la page examens."),
            ("Instituto de Línguas – Universidade Nova de Lisboa", "non relevé", "—", "Site injoignable le 26 octobre 2026."),
        ])),
    ],
    list_title="Les {n} centres TCF agréés au Portugal",
    faq=[("Où passer le TCF Canada au Portugal ?", "Le 26 octobre 2026, trois Alliances françaises affichaient un tarif TCF Canada : Porto (220 €), Faro en Algarve (220 €) et Viseu (211 €). Lisbonne et Coimbra font passer le TCF, sans préciser les versions en ligne."),
         ("Combien coûte le TCF Canada au Portugal ?", "220 € à Porto et à Faro, 211 € à Viseu, pour les quatre épreuves."),
         ("Peut-on choisir sa date de TCF Canada au Portugal ?", "À Faro, oui : l'Alliance de l'Algarve fait passer le TCF sur ordinateur n'importe quel jour ouvré, hors du 8 au 21 août et de la seconde quinzaine de décembre, à condition de réserver au moins 7 jours avant."),
         ("Où passer le TCF à Lisbonne ?", "À l'Alliance française de Lisbonne, qui ne précise en ligne ni version ni tarif : il faut passer par son formulaire de contact. L'institut de langues de l'Universidade Nova de Lisboa est aussi agréé.")],
    also=[("/centres/delf-portugal/", "DELF et DALF au Portugal", "Le calendrier national, B2 à 140 €."),
          ("/centres/tcf-espagne/", "TCF Canada en Espagne", "Onze centres, de 275 à 287 €."),
          ("/centres/delf-espagne/", "DELF et DALF en Espagne", "Le calendrier national 2027."), A_EUR, A_NCLC],
    sources="pages TCF des Alliances françaises de l'Algarve, de Porto, de Viseu, de Coimbra et de Lisbonne, consultées le 26 octobre 2026.",
    badges={"faro-alliance-francaise-de-l-algarve": OK_CA, "porto-alliance-francaise": OK_CA, "viseu-alliance-francaise": OK_CA},
    notes={"lisbonne-instituto-de-linguas-da-universidade-nova-de-lisbo": "Site injoignable le 26 octobre 2026.",
           "faro-alliance-francaise-de-l-algarve": "TCF sur ordinateur, à la date choisie par le candidat (7 jours avant au moins)."},
    urls={"faro-alliance-francaise-de-l-algarve": "https://www.alliancefr.pt/algarve/exame/teste-de-nivel-linguistico-tcf/",
          "porto-alliance-francaise": "https://www.alliancefr.pt/porto/exame/teste-de-nivel-linguistico-tcf/",
          "viseu-alliance-francaise": "https://www.alliancefr.pt/viseu/exame/tcf/",
          "coimbra-alliance-francaise": "https://www.alliancefr.pt/coimbra/exame/teste-de-nivel-linguistico-tcf/",
          "lisbonne-alliance-francaise": "https://lisboa.alliancefr.pt/exames/"},
))

# ===========================================================================
# ROUMANIE — TCF
# ===========================================================================
RO = ["bucarest-institut-francais", "cluj-napoca-institut-francais", "timisoara-institut-francais-de-roumanie"]
PAGES.append(dict(EU,
    slug="tcf-roumanie", exam="tcf", file="fei_monde/tcf_roumanie", layout="cities", chip="Roumanie",
    crumb="TCF en Roumanie",
    pointer="Les trois Instituts français (Bucarest, Cluj-Napoca, Timișoara) présentent le TCF Canada ; tarifs non publiés.",
    title="TCF Canada en Roumanie : Bucarest, Cluj, Timișoara",
    desc="TCF Canada en Roumanie : les Instituts français de Bucarest, Cluj-Napoca et Timișoara, sur ordinateur ; à Timișoara, le 4 novembre et en décembre 2026.",
    h1="TCF Canada en Roumanie : les trois Instituts français, les sessions, l'inscription",
    intro="""En Roumanie, les trois centres agréés pour le TCF sont les antennes de l'<strong>Institut français</strong> —
<strong>Bucarest</strong>, <strong>Cluj-Napoca</strong> et <strong>Timișoara</strong> —, et toutes trois présentent le
TCF Canada, sur ordinateur. Timișoara publie un calendrier : <strong>4 novembre</strong> (inscriptions jusqu'au
27 octobre), 18 novembre, 9 et 16 décembre 2026. À Cluj-Napoca, on fixe sa date avec le secrétariat au moins 10 jours
ouvrés avant ; Bucarest renvoie à son service des inscriptions. Aucun des trois ne publiait son tarif le 26 octobre
2026.""",
    facts=["<strong>3 centres agréés</strong> (liste FEI du 26 octobre 2026), tous Instituts français, tous sur ordinateur, tous avec le TCF Canada au programme.",
           "Timișoara : sessions les 04/11 (clôture 27/10), 18/11 (10/11), 09/12 (01/12) et 16/12/2026 (08/12).",
           "Cluj-Napoca : date sur rendez-vous, inscription au moins 10 jours ouvrés avant ; convocation par e-mail deux jours avant.",
           "Tarifs non publiés : à demander à l'Institut.",
           "Les quatre versions présentées partout : tout public, Canada, Québec, IRN."],
    stats=[("3", "centres agréés", "Bucarest, Cluj-Napoca, Timișoara"), ("4 nov.", "prochaine session", "Timișoara, clôture le 27 oct."),
           ("10 jours", "de délai à Cluj", "jours ouvrés, sur rendez-vous"), ("2 ans", "de validité", "")],
    sections=[
        ("releve", "Le TCF en Roumanie, centre par centre", releve([
            ("Institut français de Timișoara", "tout public, <strong>Canada</strong>, Québec, IRN", "non publié",
             "Calendrier septembre-décembre 2026 : 04/11 (clôture 27/10), 18/11 (10/11), 09/12 (01/12), 16/12 (08/12)."),
            ("Institut français de Cluj-Napoca", "tout public, <strong>Canada</strong>, Québec, IRN — sur ordinateur", "non publié",
             "Sur rendez-vous : inscription au moins 10 jours ouvrés avant la date choisie, après échange avec le secrétariat ; convocation par e-mail deux jours avant. Expression écrite sur clavier AZERTY."),
            ("Institut français de Bucarest", "tout public, <strong>Canada</strong>, Québec, IRN", "non publié",
             "Aucune date en ligne le 26 octobre 2026 : s'adresser au service des inscriptions (cours et certifications)."),
        ])),
    ],
    list_title="Les {n} centres TCF agréés en Roumanie",
    faq=[("Où passer le TCF Canada en Roumanie ?", "À l'Institut français, dans l'une de ses trois antennes agréées : Bucarest, Cluj-Napoca ou Timișoara. Toutes trois présentent le TCF Canada, sur ordinateur."),
         ("Quand a lieu le prochain TCF à Timișoara ?", "Le 4 novembre 2026 (inscriptions jusqu'au 27 octobre), puis le 18 novembre, le 9 et le 16 décembre 2026."),
         ("Combien coûte le TCF Canada en Roumanie ?", "Les Instituts français ne publiaient pas leur tarif le 26 octobre 2026 : il faut le demander au service des inscriptions."),
         ("Comment s'inscrire à Cluj-Napoca ?", "En choisissant une date avec le secrétariat de l'Institut, au moins 10 jours ouvrés avant ; la convocation arrive par e-mail deux jours avant l'examen.")],
    also=[("/centres/delf-roumanie/", "DELF et DALF en Roumanie", "Les 14 et 15 novembre 2026, inscriptions jusqu'au 3 novembre."),
          ("/centres/tcf-pologne/", "TCF Canada en Pologne", "Varsovie et Cracovie."), ("/centres/tcf-grece/", "TCF Canada en Grèce", "Athènes, six sessions jusqu'en juin 2027."), A_EUR, A_NCLC],
    sources="pages TCF-TEF des Instituts français de Bucarest, Cluj-Napoca et Timișoara (institutfrancais.ro), consultées le 26 octobre 2026.",
    badges={k: OK_CA for k in RO},
    urls={"bucarest-institut-francais": "https://institutfrancais.ro/bucuresti/fr/tests-de-francais-tcf-et-tef/",
          "cluj-napoca-institut-francais": "https://institutfrancais.ro/cluj-napoca/teste-de-limba-franceza-tcf-si-tef/",
          "timisoara-institut-francais-de-roumanie": "https://institutfrancais.ro/timisoara/tcf-test-de-cunoastere-a-limbii-franceze/"},
))

# ===========================================================================
# POLOGNE — TCF
# ===========================================================================
PAGES.append(dict(EU,
    slug="tcf-pologne", exam="tcf", file="fei_monde/tcf_pologne", layout="cities", chip="Pologne",
    crumb="TCF en Pologne",
    pointer="Institut français de Varsovie (TCF Canada à chaque session, dernière le 27 novembre 2026) et de Cracovie.",
    title="TCF Canada en Pologne : Varsovie, Cracovie, dates",
    desc="TCF Canada en Pologne : l'Institut français de Varsovie (session du 27 novembre 2026, inscriptions jusqu'au 27 octobre) et celui de Cracovie.",
    h1="TCF Canada en Pologne : Varsovie et Cracovie, les sessions et l'inscription",
    intro="""En Pologne, le TCF se passe à l'<strong>Institut français de Pologne</strong>, à <strong>Varsovie</strong> et à
<strong>Cracovie</strong>. À Varsovie, chacune des 8 sessions de 2026 comprenait le TCF Canada ; la dernière de l'année a
lieu le <strong>27 novembre 2026</strong>, avec des inscriptions jusqu'au <strong>27 octobre</strong>, et le calendrier
2027 n'était pas encore publié le 26 octobre 2026. Cracovie présente aussi le TCF Canada. Les tarifs ne sont pas en ligne ;
l'inscription passe par un formulaire à télécharger.""",
    facts=["<strong>2 centres agréés</strong> (liste FEI du 26 octobre 2026), les deux antennes de l'Institut français de Pologne.",
           "Varsovie : 8 sessions en 2026, toutes avec le TCF Canada, en alternance avec le TCF Québec ou le TCF IRN ; inscriptions closes un mois avant.",
           "Dernière session 2026 : <strong>27/11</strong> (tout public, DAP, IRN, Canada), inscriptions jusqu'au <strong>27/10</strong>.",
           "Inscription : formulaire à télécharger sur la page TCF Canada de l'Institut ; tarif non publié.",
           "Cracovie : pages TCF Canada, Québec, IRN, tout public et DAP ; dates non publiées.",
           "TEF Canada, l'autre test accepté par IRCC : sessions publiées par l'Alliance française de Łódź le 26 octobre 2026."],
    stats=[("2", "centres agréés", "Varsovie et Cracovie"), ("27 nov.", "dernière session 2026", "à Varsovie"),
           ("27 oct.", "clôture des inscriptions", "un mois avant"), ("8", "sessions en 2026", "toutes avec le TCF Canada")],
    sections=[
        ("releve", "Le TCF en Pologne", releve([
            ("Institut français de Pologne – Varsovie", "<strong>Canada</strong>, Québec, IRN, tout public, DAP", "non publié",
             "2026 : 27/02, 27/03, 17/04, 29/05, 19/06, 25/09, 23/10 et <strong>27/11</strong> (inscriptions jusqu'au 27/10), TCF Canada à chaque fois ; 2027 non publié. Formulaire d'inscription à télécharger."),
            ("Institut français de Pologne – Cracovie", "<strong>Canada</strong>, Québec, IRN, tout public, DAP", "non publié", "Dates non publiées."),
        ])),
    ],
    list_title="Les {n} centres TCF agréés en Pologne",
    faq=[("Où passer le TCF Canada en Pologne ?", "À l'Institut français de Pologne, à Varsovie (Plac Europejski 3) ou à Cracovie : ce sont les deux centres TCF agréés, et tous deux présentent la version Canada."),
         ("Quand a lieu le prochain TCF Canada à Varsovie ?", "Le 27 novembre 2026, avec des inscriptions jusqu'au 27 octobre 2026. Le calendrier 2027 n'était pas publié le 26 octobre 2026 ; en 2026, l'Institut a tenu 8 sessions, toutes avec le TCF Canada."),
         ("Combien coûte le TCF Canada en Pologne ?", "L'Institut français ne publiait pas son tarif le 26 octobre 2026 : il figure sur le formulaire d'inscription ou s'obtient auprès du service des examens."),
         ("Où passer le TEF Canada en Pologne ?", "La carte du Français des affaires affichait le 26 octobre 2026 des sessions TEF Canada à l'Alliance française de Łódź.")],
    also=[("/centres/delf-pologne/", "DELF et DALF en Pologne", "Du 16 au 20 novembre 2026, B2 à 620 zł."),
          ("/centres/tcf-allemagne/", "TCF Canada en Allemagne", "Berlin, 295 €, des sessions chaque mois."), ("/centres/tcf-roumanie/", "TCF Canada en Roumanie", "Bucarest, Cluj, Timișoara."), A_EUR, A_TEF],
    sources="pages TCF de l'Institut français de Pologne (Varsovie et Cracovie) et son calendrier des sessions TCF 2026 (PDF), carte des centres TEF du Français des affaires, consultés le 26 octobre 2026.",
    badges={"varsovie-institut-francais": OK_CA, "cracovie-institut-francais": OK_CA},
    urls={"varsovie-institut-francais": "https://institutfrancais.pl/kursy-i-egzaminy/warszawa/egzaminy-warszawa/tcf-test-de-connaissance-du-francais",
          "cracovie-institut-francais": "https://institutfrancais.pl/kursy-i-egzaminy/krakow/egzaminy-krakow/tcf-test-de-connaissance-du-francais"},
))

# ===========================================================================
# GRÈCE — TCF
# ===========================================================================
PAGES.append(dict(EU,
    slug="tcf-grece", exam="tcf", file="fei_monde/tcf_grece", layout="cities", chip="Grèce",
    crumb="TCF en Grèce",
    pointer="Institut français de Grèce, à Athènes : TCF Canada le 19 novembre 2026, puis cinq sessions jusqu'en juin 2027.",
    title="TCF Canada en Grèce : Athènes, dates 2026-2027",
    desc="TCF Canada en Grèce : l'Institut français d'Athènes, le 19 novembre 2026 (inscriptions du 2 au 5 novembre), puis cinq sessions jusqu'en juin 2027.",
    h1="TCF Canada en Grèce : Athènes et Thessalonique, les dates et l'inscription",
    intro="""En Grèce, le TCF Canada se passe à l'<strong>Institut français de Grèce</strong>, à Athènes : son calendrier
2026-2027 réunit le TCF tout public, le TCF Québec, le TCF Canada et le TCF IRN le <strong>19 novembre 2026</strong> —
inscriptions du <strong>2 au 5 novembre</strong> seulement —, puis les 21 janvier, 25 février, 24 mars, 22 avril et
17 juin 2027. L'Institut français de Thessalonique présente le TCF à 100 €, sans parler de la version Canada. À Athènes,
chaque fenêtre d'inscription ne dure que quatre jours.""",
    facts=["<strong>2 centres agréés</strong> (liste FEI du 26 octobre 2026) : les Instituts français d'Athènes et de Thessalonique, sur ordinateur.",
           "Athènes : 6 sessions TCF, TCF Canada compris, de novembre 2026 à juin 2027 ; fenêtre d'inscription de 4 jours, fixée pour chaque session.",
           "Prochaine : <strong>19/11/2026</strong>, inscriptions du 02 au 05/11 ; puis 21/01/2027, inscriptions du 30/11 au 03/12/2026.",
           "2027 : 25/02 (inscriptions du 01 au 04/02), 24/03 (01 au 04/03), 22/04 (05 au 08/04), 17/06 (31/05 au 03/06).",
           "Tarif du TCF Canada non publié à Athènes ; Thessalonique affiche 100 € pour le TCF, sans préciser la version."],
    stats=[("2", "centres agréés", "Athènes et Thessalonique"), ("19 nov.", "prochaine session", "Athènes"),
           ("4 jours", "pour s'inscrire", "du 2 au 5 novembre"), ("6", "sessions", "de nov. 2026 à juin 2027")],
    sections=[
        ("releve", "Le TCF en Grèce", releve([
            ("Institut français de Grèce (Athènes)", "tout public, Québec, <strong>Canada</strong>, IRN", "non publié",
             "19/11/2026 (inscriptions du 02 au 05/11), 21/01/2027 (30/11 au 03/12/2026), 25/02 (01 au 04/02), 24/03 (01 au 04/03), 22/04 (05 au 08/04), 17/06/2027 (31/05 au 03/06). Dossier d'inscription à télécharger."),
            ("Institut français de Thessalonique", "TCF (version non précisée)", "100 €", "Dates non publiées : contacter le service des examens."),
        ])),
    ],
    list_title="Les {n} centres TCF agréés en Grèce",
    faq=[("Où passer le TCF Canada en Grèce ?", "À l'Institut français de Grèce, rue Sina 31 à Athènes : son calendrier 2026-2027 comprend le TCF Canada à chaque session. L'Institut français de Thessalonique présente le TCF sans préciser la version Canada."),
         ("Quand a lieu le prochain TCF Canada à Athènes ?", "Le 19 novembre 2026, avec des inscriptions du 2 au 5 novembre seulement ; puis le 21 janvier 2027 (inscriptions du 30 novembre au 3 décembre 2026)."),
         ("Quelles sont les dates du TCF 2027 en Grèce ?", "À Athènes : le 21 janvier, le 25 février, le 24 mars, le 22 avril et le 17 juin 2027, chaque fois avec une fenêtre d'inscription de quatre jours."),
         ("Combien coûte le TCF en Grèce ?", "Thessalonique affiche 100 € pour le TCF ; l'Institut français d'Athènes ne publie pas son tarif dans son calendrier.")],
    also=[("/centres/delf-grece/", "DELF et DALF en Grèce", "B2 le 15 mai 2027, inscriptions du 1er au 15 février."),
          ("/centres/tcf-italie/", "TCF Canada en Italie", "Sept centres, de 210 à 250 €."), ("/centres/tcf-roumanie/", "TCF Canada en Roumanie", "Bucarest, Cluj, Timișoara."), A_EUR, A_NCLC],
    sources="calendrier « Examens du TCF – sessions 2026-2027 » (PDF) et page des examens de l'Institut français de Grèce (ifg.gr) ; page TCF de l'Institut français de Thessalonique (ift.gr) ; consultés le 26 octobre 2026.",
    badges={"athenes-institut-francais": OK_CA},
    notes={"athenes-institut-francais": "FEI donne ifa.gr, qui renvoie vers ifg.gr."},
    urls={"athenes-institut-francais": "https://www.ifg.gr/eksetaseis/poies-eksetaseis/",
          "thessalonique-institut-francais": "https://www.ift.gr/tcf-test-gnosis-gallikon/"},
))

# ===========================================================================
# IRLANDE — TCF
# ===========================================================================
PAGES.append(dict(EU,
    slug="tcf-irlande", exam="tcf", file="fei_monde/tcf_irlande", layout="cities", chip="Irlande",
    crumb="TCF en Irlande",
    pointer="Alliance française de Dublin (chaque mois) et French Institute de Galway : TCF Canada à 270 €.",
    title="TCF Canada en Irlande : Dublin et Galway, 270 €",
    desc="TCF Canada en Irlande : 270 € à l'Alliance française de Dublin, avec des sessions chaque mois, et au French Institute de Galway. Inscription, résultats.",
    h1="TCF Canada en Irlande : Dublin et Galway, les prix et l'inscription",
    intro="""En Irlande, deux centres sont agréés pour le TCF, et <strong>les deux affichent le TCF Canada à 270 €</strong> :
l'<strong>Alliance française de Dublin</strong>, qui organise des sessions TEF et TCF chaque mois sur ses ordinateurs, et
le <strong>French Institute de Galway</strong>. À Dublin, on s'inscrit par e-mail avec une copie de son passeport, au plus
tard un mois avant l'examen ; les résultats arrivent en deux à trois semaines. À Galway, les dates s'obtiennent sur
demande.""",
    facts=["<strong>2 centres agréés</strong> (liste FEI du 26 octobre 2026) : l'Alliance française de Dublin et le French Institute de Galway.",
           "<strong>TCF Canada : 270 €</strong> dans les deux ; à Dublin, TCF IRN 270 €, TCF Québec 270 € (les quatre épreuves), TCF tout public 300 €.",
           "Dublin : sessions « chaque mois » ; inscriptions closes un mois avant chaque examen ; examen sur les ordinateurs du centre.",
           "Résultats en 2 à 3 semaines à Dublin ; attestation valable 2 ans.",
           "Galway : dates sur demande."],
    stats=[("2", "centres agréés", "Dublin et Galway"), ("270 €", "le TCF Canada", "dans les deux centres"),
           ("1 mois", "de délai à Dublin", "clôture avant l'examen"), ("2 à 3 sem.", "pour les résultats", "à Dublin")],
    sections=[
        ("releve", "Le TCF en Irlande", releve([
            ("Alliance française de Dublin", "<strong>Canada</strong>, Québec, IRN, tout public — sur les ordinateurs du centre",
             "Canada <strong>270 €</strong> · IRN 270 € · Québec 270 € (60 à 90 € par épreuve) · tout public 300 € (150 € les épreuves obligatoires)",
             "Sessions chaque mois ; inscription par e-mail au service des examens, avec une copie du passeport, au plus tard un mois avant ; résultats en 2 à 3 semaines."),
            ("The French Institute (Galway)", "<strong>Canada</strong>, Québec, IRN, tout public", "Canada <strong>270 €</strong>", "Dates sur demande."),
        ])),
    ],
    list_title="Les {n} centres TCF agréés en Irlande",
    faq=[("Où passer le TCF Canada en Irlande ?", "À l'Alliance française de Dublin, 1 Kildare Street, ou au French Institute de Galway : les deux centres agréés affichent le TCF Canada à 270 €."),
         ("Combien coûte le TCF Canada en Irlande ?", "270 € à Dublin comme à Galway, relevés le 26 octobre 2026. À Dublin, le TCF IRN coûte aussi 270 € et le TCF tout public complet 300 €."),
         ("Quand a lieu le prochain TCF Canada à Dublin ?", "L'Alliance française de Dublin organise des sessions TEF et TCF chaque mois ; l'inscription ferme un mois avant chaque examen. On réserve par e-mail auprès du service des examens."),
         ("Quand arrivent les résultats ?", "Deux à trois semaines après l'examen à Dublin ; l'attestation est valable deux ans.")],
    also=[("/centres/delf-irlande/", "DELF et DALF en Irlande", "Cinq sessions en 2027, B2 à 145 € à Dublin."),
          ("/centres/tcf-royaume-uni/", "TCF Canada au Royaume-Uni", "Londres £260, Glasgow £325."), ("/centres/tcf-belgique/", "TCF Canada en Belgique", "Bruxelles 268 €, Gand 260 €."), A_EUR, A_NCLC],
    sources="pages « Exams & Certification » et « TEF-TCF » de l'Alliance française de Dublin, page TCF du French Institute de Galway, consultées le 26 octobre 2026.",
    badges={"dublin-alliance-francaise": OK_CA, "galway-the-french-institute": OK_CA},
    urls={"dublin-alliance-francaise": "https://www.alliance-francaise.ie/tef-tcf/",
          "galway-the-french-institute": "https://frenchinstitute.ie/tcf-exam-and-delf-dalf-preparation/"},
))


# ###########################################################################
# SUITE (26/10/2026, après-midi) : DELF-DALF en Italie, Roumanie, Pays-Bas, Grèce, Pologne, Belgique, Portugal,
# Irlande et Suède ; TCF (et DELF) en Autriche et au Luxembourg. La Suède n'a aucun centre TCF (liste FEI) : sa page
# DELF dit où passer le TEF Canada et le TCF Canada au plus près. Relevé : sites des centres et des organismes de
# gestion DELF, ouverts le 26 octobre 2026 (calendriers PDF lus avec pdftotext).
# ###########################################################################
PAYS_ID.update({"Luxembourg": 375, "Autriche": 61, "Suède": 93})
PHONE.update({"Luxembourg": ("352", set(range(6, 12))), "Autriche": ("43", set(range(7, 14))), "Suède": ("46", {7, 8, 9})})
CITY["Italie"].update({"Torino": "Turin", "Firenze": "Florence", "Bologna": "Bologne", "Catania": "Catane", "Verona": "Vérone",
                       "Ventimiglia": "Vintimille", "Aosta": "Aoste"})
CITY.update({"Portugal": {"Caldas Da Rainha": "Caldas da Rainha"},
             "Pologne": {"Lódz": "Łódź", "Poznan": "Poznań", "Torun": "Toruń", "Wroclaw": "Wrocław", "Gdansk": "Gdańsk",
                         "Wodzislaw Slaski": "Wodzisław Śląski"},
             "Suède": {"Sollentua": "Sollentuna"},
             "Luxembourg": {"Luxembourg Ville": "Luxembourg", "Esch-Sur-Alzette": "Esch-sur-Alzette"},
             "Autriche": {"Wien": "Vienne"}})
CITY["Roumanie"].update({"Brasov": "Brașov", "Constanta": "Constanța", "Iasi": "Iași", "Pitesti": "Pitești", "Ploiesti": "Ploiești"})
CITY_T["en"]["Italie"].update({"Catane": "Catania", "Vérone": "Verona", "Vintimille": "Ventimiglia", "Messine": "Messina"})
CITY_T["en"]["Pays-Bas"]["Groningue"] = "Groningen"
CITY_T["en"].update({"Suède": {"Göteborg": "Gothenburg"}, "Autriche": {"Vienne": "Vienna"}})
ADDR_T["en"]["Italie"]["Messine"] = "Messina"
ADDR_T["en"]["Pays-Bas"].update({"La Haye": "Den Haag", "Groningue": "Groningen"})
ADDR_T["en"].update({"Autriche": {"Vienne": "Vienna", "Ambassade de France - Autriche": "French Embassy in Austria,"},
                     "Luxembourg": {"Luxembourg Ville": "Luxembourg City"}})

A_CAL = ("/blog/calendrier-delf-dalf-2026-2027/", "Calendrier DELF-DALF 2026-2027", "Les sessions nationales en France et la méthode pour choisir.")
NO_LINK = "Site indiqué par FEI injoignable le 26 octobre 2026."

# ===========================================================================
# ITALIE — DELF-DALF
# ===========================================================================
PAGES.append(dict(EU,
    slug="delf-italie", exam="delf", file="fei_monde/delf_italie", layout="cities", chip="Italie",
    crumb="DELF en Italie",
    pointer="",
    title="DELF en Italie : dates 2027, prix (B2 160 €), centres",
    desc="DELF et DALF en Italie : les sessions de février, avril et juin 2027 et leurs inscriptions, les prix (B2 160 €, 144 € réduit) et les {n} centres.",
    h1="DELF et DALF en Italie : le calendrier 2026-2027, les prix et les {n} centres",
    intro="""En Italie, le DELF et le DALF tout public suivent un même calendrier, publié à l'identique par l'Institut français
de Milan et l'Alliance française de Turin : après la session de novembre 2026 (écrits du 10 au 13 novembre, inscriptions
closes le 2 octobre) viennent <strong>février 2027</strong> — DELF B2 le <strong>25 février</strong>, inscriptions du
<strong>2 novembre au 4 décembre 2026</strong> —, avril (B2 le 8 avril) et juin 2027 (B2 le 16 juin). Le DELF B2 coûte
<strong>160 €</strong>, 144 € au tarif réduit, à Milan, à Turin et à Rome.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 26 octobre 2026) : les Instituts français de Milan, Florence, Naples et Palerme, le Centre Saint-Louis de Rome, le lycée Victor-Hugo de Florence et vingt Alliances françaises.",
           "Février 2027 : C2 le 18, C1 le 19, A1 et A2 le 23, B1 le 24, <strong>B2 le 25 février</strong> ; inscriptions du 2 novembre au 4 décembre 2026 (mêmes dates à Naples).",
           "Avril 2027 : C1 le 5, C2 le 6, B1 le 7, <strong>B2 le 8</strong>, A1 et A2 le 9 avril ; inscriptions jusqu'au 19 février. À Milan, avril n'ouvre que le B2, le C1 et le C2.",
           "Juin 2027 : C2 le 14, C1 le 15, <strong>B2 le 16</strong>, B1 le 17, A1 et A2 le 18 juin ; inscriptions jusqu'au 23 avril 2027.",
           "Prix à Milan, Turin et Rome : <strong>A1 80 € · A2 90 € · B1 125 € · B2 160 € · C1 et C2 195 €</strong> ; tarif réduit de 72 à 176 €.",
           "Le calendrier couvre l'année 2026-2027 : la session de novembre 2027 n'était pas publiée le 26 octobre 2026."],
    stats=[("{n}", "centres d'examen", "liste FEI du 26 octobre 2026"), ("160 €", "le DELF B2", "144 € au tarif réduit"),
           ("25 févr.", "prochain B2", "inscriptions jusqu'au 4 déc."), ("3", "sessions en 2027", "février, avril, juin")],
    sections=[
        ("calendrier", "Le calendrier 2026-2027 du DELF-DALF tout public", table(
            "Dates des épreuves écrites collectives, identiques dans les calendriers 2026-2027 de l'Institut français de Milan et de l'Alliance française de Turin, relevées le 26 octobre 2026. Les oraux ont lieu pendant le mois de la session.",
            ["Session", "A1", "A2", "B1", "B2", "C1", "C2", "Inscriptions"],
            [("Nov. 2026", "10/11", "11/11", "11/11", "10/11", "12/11", "13/11", "closes le 02/10"),
             ("<strong>Févr. 2027</strong>", "23/02", "23/02", "24/02", "<strong>25/02</strong>", "19/02", "18/02", "du 02/11 au 04/12/2026"),
             ("Avril 2027", "09/04", "09/04", "07/04", "08/04", "05/04", "06/04", "jusqu'au 19/02 (Milan : du 01/02 au 19/02)"),
             ("Juin 2027", "18/06", "18/06", "17/06", "16/06", "15/06", "14/06", "jusqu'au 23/04 (Milan : du 01/04 au 23/04)")]) + """
<p>Les oraux se passent du 2 au 30 novembre 2026, du 1er au 26 février, du 1er au 30 avril et du 1er au 30 juin 2027.
L'Alliance de Turin prévient que les inscriptions ferment très en avance sur les épreuves. L'Institut français de Naples
annonce quatre sessions par an (novembre, février, mars-avril, juin) avec la même fenêtre pour février ; le Centre
Saint-Louis de Rome, les mêmes mois, et prévient que l'oral peut précéder l'écrit. Tous les centres n'ouvrent pas tous
les niveaux à chaque session.</p>"""),
        ("prix", "Combien coûte le DELF en Italie ?", table(
            "Tarifs 2026-2027 de l'Alliance française de Turin, les mêmes à l'Institut français de Milan et au Centre Saint-Louis de Rome, relevés le 26 octobre 2026.",
            ["Niveau", "Tarif plein", "Tarif réduit"],
            [("DELF A1", "80 €", "72 €"), ("DELF A2", "90 €", "81 €"), ("DELF B1", "125 €", "113 €"),
             ("<strong>DELF B2</strong>", "<strong>160 €</strong>", "<strong>144 €</strong>"), ("DALF C1", "195 €", "176 €"),
             ("DALF C2", "195 €", "176 €"), ("DELF scolaire A1 à B2 (Turin)", "68 à 135 €", "—"), ("DELF Prim A1.1 à A2 (Turin)", "50 à 78 €", "—")], wide=False) + """
<p>Le tarif réduit vise, selon les centres, les moins de 18 ans, les élèves du secondaire, les élèves du centre et les
étudiants des universités conventionnées (à Milan : Insubria, Pavie, Bicocca, ainsi que les enseignants de français). Le
Centre Saint-Louis ne rembourse pas les frais d'examen.</p>"""),
        ("inscription", "S'inscrire, résultats et diplôme", """<p>On s'inscrit auprès du centre choisi — en ligne à l'Institut
français de Milan, auprès du secrétariat des examens ailleurs —, pendant la fenêtre de la session. Les diplômes sont
indépendants : on s'inscrit directement au niveau visé, et il faut 50 points sur 100 pour l'obtenir.</p>

<p>Le DELF scolaire, à tarif préférentiel (68 € l'A1, 135 € le B2 à Turin), s'organise avec les établissements ; le DELF
Prim s'adresse aux enfants. Les centres publient les résultats de chaque session sur leur site.</p>"""),
    ],
    list_title="Les {n} centres d'examen DELF-DALF, ville par ville",
    faq=[("Quelles sont les dates du DELF 2027 en Italie ?", "Selon le calendrier 2026-2027 de l'Institut français de Milan et de l'Alliance française de Turin, le DELF B2 a lieu le 25 février, le 8 avril et le 16 juin 2027 ; les inscriptions de février vont du 2 novembre au 4 décembre 2026. La session de novembre 2027 n'était pas publiée le 26 octobre 2026."),
         ("Combien coûte le DELF B2 en Italie ?", "160 €, ou 144 € au tarif réduit, à Milan, à Turin et à Rome. Le DALF C1 et le DALF C2 coûtent 195 € (176 € au tarif réduit)."),
         ("Peut-on encore s'inscrire pour novembre 2026 ?", "Non : les inscriptions de la session de novembre 2026 (écrits du 10 au 13 novembre) ont fermé le 2 octobre. La prochaine est celle de février 2027, avec des inscriptions du 2 novembre au 4 décembre 2026."),
         ("Où passer le DELF à Rome ou à Milan ?", "À Rome, à l'Institut français – Centre Saint-Louis (Largo Toniolo) ; à Milan, à l'Institut français (Corso Magenta 63). Tous deux appliquent les mêmes tarifs, 160 € le B2."),
         ("Faut-il passer l'A1 avant le B2 ?", "Non : les diplômes DELF et DALF sont indépendants, on s'inscrit directement au niveau visé.")],
    also=[("/centres/tcf-italie/", "TCF Canada en Italie", "Sept centres l'annoncent, de 210 à 250 €."),
          ("/centres/delf-suisse/", "DELF et DALF en Suisse", "Le calendrier national 2027, B2 de CHF 370 à 390."), A_CAL, A_DELF],
    sources="calendrier DELF-DALF tout public 2026-2027 (PDF) et page « DELF DALF – tout public » de l'Institut français de Milan ; calendrier DELF-DALF tout public 2026-2027 et tarifs 2026-2027 (PDF) de l'Alliance française de Turin ; pages DELF-DALF de l'Institut français de Naples et du Centre Saint-Louis de Rome ; consultés le 26 octobre 2026.",
    urls={"cagliari-alliance-francaise-de-cagliari": "", "sassari-alliance-francaise-sassari-c-o-liceo-statale-margherita-di-castelvi": "",
          "vintimille-alliance-francaise-vintimille": "", "trieste-alliance-francaise-trieste": "",
          "milan-institut-francais-d-italie-milan": "https://www.institutfrancais.it/milano/delf-dalf-le-certificazioni-ufficiali-tout-public",
          "rome-institut-francais-centre-saint-louis": "https://www.ifcsl.com/centre-saint-louis/delfdalf-adulti",
          "turin-alliance-francaise-torino": "https://www.alliancefrto.it/esami-e-certificazioni/",
          "naples-institut-francais-d-italie-naples": "https://www.institutfrancais.it/napoli/delf-dalf-tout-public"},
    notes={"cagliari-alliance-francaise-de-cagliari": "Site indiqué par FEI hors service le 26 octobre 2026.",
           "sassari-alliance-francaise-sassari-c-o-liceo-statale-margherita-di-castelvi": "Site indiqué par FEI réservé aux comptes Google le 26 octobre 2026.",
           "vintimille-alliance-francaise-vintimille": "FEI ne donne pas d'adresse de site valide.",
           "trieste-alliance-francaise-trieste": "Site vide le 26 octobre 2026."},
))

# ===========================================================================
# ROUMANIE — DELF-DALF
# ===========================================================================
PAGES.append(dict(EU,
    slug="delf-roumanie", exam="delf", file="fei_monde/delf_roumanie", layout="cities", chip="Roumanie",
    crumb="DELF en Roumanie",
    pointer="",
    title="DELF en Roumanie : sessions 2026-2027, {n} centres",
    desc="DELF et DALF en Roumanie : session des 14 et 15 novembre 2026, inscriptions jusqu'au 3 novembre, résultats le 17 décembre ; dates 2027 non publiées.",
    h1="DELF et DALF en Roumanie : les sessions, les inscriptions et les {n} centres",
    intro="""En Roumanie, le DELF et le DALF tout public se passent dans <strong>{n} centres</strong> — les antennes de l'Institut
français à Bucarest, Cluj-Napoca, Iași et Timișoara et six Alliances françaises —, sous la gestion centrale de l'Institut
français de Roumanie. Prochaine session : les <strong>14 et 15 novembre 2026</strong>, avec des inscriptions en ligne
ouvertes jusqu'au <strong>3 novembre</strong> et des résultats le 17 décembre. Le calendrier 2027 n'était pas publié le
26 octobre 2026 ; en 2026, Bucarest a tenu quatre sessions (février, avril, juin, novembre).""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 26 octobre 2026) : les Instituts français de Bucarest, Cluj-Napoca, Iași et Timișoara, les Alliances françaises de Brașov, Constanța, Craiova, Pitești, Ploiești et Suceava.",
           "Novembre 2026 : épreuves les <strong>14 et 15 novembre</strong>, inscriptions du 14 septembre au <strong>3 novembre</strong>, résultats le 17 décembre (Bucarest, Cluj-Napoca, Iași).",
           "Bucarest, 2026 : 14-15 février, 4-5 avril, 6-7 juin et 14-15 novembre ; Cluj-Napoca et Iași : 14-15 mars, 6-7 juin et 14-15 novembre.",
           "En novembre 2026, l'Institut de Cluj-Napoca fait aussi passer l'examen à Oradea ; en mars, il était allé à Bistrița, Satu Mare, Sibiu et Târgu Mureș.",
           "Tarifs absents des pages DELF-DALF des Instituts le 26 octobre 2026 : à demander au secrétariat.",
           "Diplôme 4 à 5 mois après l'affichage des résultats (Iași) ; inscription en ligne, avec un tutoriel."],
    stats=[("{n}", "centres d'examen", "4 Instituts français, 6 Alliances"), ("14-15 nov.", "prochaine session", "2026"),
           ("3 nov.", "clôture des inscriptions", "en ligne"), ("17 déc.", "résultats", "session de novembre")],
    sections=[
        ("calendrier", "Les sessions 2026 des Instituts français", table(
            "Sessions DELF-DALF tout public publiées par les Instituts français de Bucarest, Cluj-Napoca et Iași, relevées le 26 octobre 2026. Le calendrier 2027 n'était pas encore en ligne.",
            ["Session", "Épreuves", "Inscriptions", "Résultats", "Où"],
            [("Février 2026", "14-15/02", "01/01 – 04/02", "12/03", "Bucarest"),
             ("Mars 2026", "14-15/03", "01/01 – 02/03", "16/04", "Cluj-Napoca (et Bistrița, Satu Mare, Sibiu, Târgu Mureș), Iași"),
             ("Avril 2026", "04-05/04", "02/03 – 25/03", "16/04", "Bucarest"),
             ("Juin 2026", "06-07/06", "20/04 – 26/05", "18/06", "Bucarest, Cluj-Napoca, Iași"),
             ("<strong>Novembre 2026</strong>", "<strong>14-15/11</strong>", "14/09 – <strong>03/11</strong>", "17/12", "Bucarest, Cluj-Napoca (et Oradea), Iași")]) + """
<p>Le DELF junior a son propre calendrier : à Iași, les 14-15 mars, 23-24 mai et 14-15 novembre 2026, avec des épreuves
au printemps à Piatra-Neamț, Focșani et Galați. Timișoara et les six Alliances françaises de la liste n'ont pas été
relevées : leurs coordonnées figurent ci-dessous.</p>"""),
        ("inscription", "S'inscrire et recevoir son diplôme", """<p>L'inscription se fait en ligne, sur le site de l'antenne de
l'Institut français choisie, qui publie un tutoriel ; le règlement DELF-DALF est joint à chaque page. Les diplômes sont
indépendants : on s'inscrit directement au niveau visé, et il faut 50 points sur 100 pour réussir.</p>

<p>À Bucarest, le diplôme se retire au service des inscriptions (cours et examens), muni d'une pièce d'identité ; à Iași,
il arrive 4 à 5 mois après l'affichage des résultats. Les tarifs ne figurent pas sur ces pages : il faut les demander au
service des inscriptions de l'antenne choisie.</p>"""),
    ],
    list_title="Les {n} centres d'examen DELF-DALF, ville par ville",
    faq=[("Quand a lieu le prochain DELF en Roumanie ?", "Les 14 et 15 novembre 2026, dans les Instituts français de Bucarest, Cluj-Napoca et Iași ; les inscriptions en ligne restent ouvertes jusqu'au 3 novembre, et les résultats sont annoncés le 17 décembre 2026."),
         ("Les dates du DELF 2027 en Roumanie sont-elles connues ?", "Pas encore : le 26 octobre 2026, les Instituts français de Roumanie ne publiaient que leurs sessions 2026. Bucarest en a tenu quatre (février, avril, juin, novembre), Cluj-Napoca et Iași trois (mars, juin, novembre)."),
         ("Combien coûte le DELF en Roumanie ?", "Les Instituts français ne publiaient pas leurs tarifs sur leurs pages DELF-DALF le 26 octobre 2026 : il faut les demander au service des inscriptions de l'antenne choisie."),
         ("Quand reçoit-on son diplôme ?", "Les résultats de la session de novembre 2026 sont annoncés le 17 décembre ; à Iași, le diplôme arrive 4 à 5 mois après l'affichage des résultats. À Bucarest, on le retire avec une pièce d'identité.")],
    also=[("/centres/tcf-roumanie/", "TCF Canada en Roumanie", "Bucarest, Cluj-Napoca, Timișoara."),
          ("/centres/delf-pologne/", "DELF et DALF en Pologne", "Du 16 au 20 novembre 2026, B2 à 620 zł."), A_CAL, A_DELF],
    sources="pages DELF-DALF pour les adultes des Instituts français de Bucarest, Cluj-Napoca et Iași (institutfrancais.ro) et page « Calendar și tarife » du DELF junior de Iași, consultées le 26 octobre 2026.",
    urls={"bucarest-institut-francais-de-roumanie-a-bucarest": "https://institutfrancais.ro/bucuresti/fr/examens-delf-dalf/",
          "cluj-napoca-institut-francais-de-roumanie-a-cluj-napoca": "https://institutfrancais.ro/cluj-napoca/delf-dalf-2/",
          "iasi-institut-francais-de-roumanie-a-iasi": "https://institutfrancais.ro/iasi/delf-dalf/"},
))

# ===========================================================================
# PAYS-BAS — DELF-DALF
# ===========================================================================
PAGES.append(dict(EU,
    slug="delf-pays-bas", exam="delf", file="fei_monde/delf_pays_bas", layout="cities", chip="Pays-Bas",
    crumb="DELF aux Pays-Bas",
    pointer="",
    title="DELF aux Pays-Bas : dates 2027, prix (B2 175 €)",
    desc="DELF et DALF aux Pays-Bas : sessions de mars et juin 2027 à Amsterdam, novembre 2026, prix (B2 175 €), les {n} centres et l'inscription.",
    h1="DELF et DALF aux Pays-Bas : les sessions 2026-2027, les prix et les {n} centres",
    intro="""Aux Pays-Bas, le DELF et le DALF tout public se passent dans <strong>{n} centres</strong>, dont les Alliances
françaises d'Amsterdam, de La Haye et de Rotterdam et l'Institut français à Groningue. L'Alliance d'Amsterdam annonce deux
sessions en 2027 : du <strong>9 au 11 mars</strong> (inscriptions à partir de janvier) et du <strong>7 au 11 juin</strong>
(à partir d'avril). La session de novembre 2026, du 9 au 13 novembre, fermait ses inscriptions les 25 et 26 octobre. Le
DELF B2 coûte <strong>175 €</strong>.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 26 octobre 2026), sous la gestion de l'Institut français des Pays-Bas (La Haye) : trois Alliances françaises, l'Institut français à Groningue et à La Haye, le lycée français Van Gogh et la HAN à Arnhem.",
           "2027 à Amsterdam : <strong>9-11 mars</strong> et <strong>7-11 juin</strong> ; inscriptions ouvertes en janvier et en avril 2027. La Haye annonce des sessions en mars, juin et novembre.",
           "Novembre 2026 : A1 et A2 le 9, B1 le 10, B2 le 11, C1 le 12, C2 le 13 novembre ; inscriptions closes le 25 octobre à Amsterdam, le 26 octobre à l'Institut français.",
           "Prix (Amsterdam, Institut français) : <strong>A1 110 € · A2 110 € · B1 155 € · B2 175 € · C1 220 € · C2 230 €</strong>.",
           "DELF junior à Amsterdam : A1 et A2 le 12 avril, B1 et B2 le 13 avril 2027 (B2 180 €) ; DELF Prim le 26 mai 2027.",
           "Rotterdam fait passer les examens « tout au long de l'année » ; dates sur demande."],
    stats=[("{n}", "centres d'examen", "liste FEI du 26 octobre 2026"), ("175 €", "le DELF B2", "C1 220 €, C2 230 €"),
           ("9-11 mars", "première session 2027", "Amsterdam"), ("2", "sessions annoncées", "mars et juin 2027")],
    sections=[
        ("calendrier", "Les sessions 2026-2027", table(
            "Sessions DELF-DALF tout public publiées par l'Institut français des Pays-Bas et l'Alliance française d'Amsterdam, relevées le 26 octobre 2026.",
            ["Session", "Épreuves écrites", "Inscriptions", "Où"],
            [("Juin 2026", "A1 et A2 01/06, B1 02/06, B2 03/06, C1 04/06, C2 05/06", "12/01 – 18/05/2026", "Institut français (Groningue)"),
             ("Novembre 2026", "A1 et A2 09/11, B1 10/11, <strong>B2 11/11</strong>, C1 12/11, C2 13/11", "jusqu'au 25/10 (Amsterdam) ; 01/07 – 26/10 (Institut français)", "Amsterdam, Groningue"),
             ("<strong>Mars 2027</strong>", "du 9 au 11 mars", "à partir de janvier 2027", "Amsterdam"),
             ("<strong>Juin 2027</strong>", "du 7 au 11 juin", "à partir d'avril 2027", "Amsterdam")]) + """
<p>Le détail par niveau des sessions 2027 n'était pas publié le 26 octobre 2026. L'Alliance française de La Haye vend ses
sessions de mars, juin et novembre sur son site, sans dates ni prix en clair ce jour-là ; celle de Rotterdam propose des
examens tout au long de l'année et renvoie à sa fiche DELF-DALF.</p>"""),
        ("prix", "Combien coûte le DELF aux Pays-Bas ?", table(
            "Tarifs affichés par l'Alliance française d'Amsterdam et l'Institut français des Pays-Bas le 26 octobre 2026.",
            ["Niveau", "Tout public", "DELF junior (Amsterdam)"],
            [("A1", "110 €", "110 €"), ("A2", "110 €", "110 €"), ("B1", "155 €", "155 €"),
             ("<strong>B2</strong>", "<strong>175 €</strong>", "180 €"), ("DALF C1", "220 €", "—"), ("DALF C2", "230 €", "—"),
             ("DELF Prim A1.1 · A1 · A2 (Amsterdam)", "65 € · 90 € · 90 €", "—")], wide=False)),
        ("inscription", "S'inscrire", """<p>Chaque centre gère ses inscriptions : à Amsterdam, elles ouvrent en janvier pour mars
et en avril pour juin ; à La Haye, un bouton par session (mars, juin, novembre) mène au module de l'Alliance ; à
Groningue, l'Institut français répond par e-mail. Les diplômes sont indépendants : on s'inscrit directement au niveau visé,
et il faut 50 points sur 100 pour l'obtenir.</p>"""),
    ],
    list_title="Les {n} centres d'examen DELF-DALF, ville par ville",
    faq=[("Quelles sont les dates du DELF 2027 aux Pays-Bas ?", "L'Alliance française d'Amsterdam annonce deux sessions tout public en 2027 : du 9 au 11 mars (inscriptions à partir de janvier) et du 7 au 11 juin (à partir d'avril). La Haye prévoit des sessions en mars, juin et novembre ; le détail par niveau n'était pas publié le 26 octobre 2026."),
         ("Combien coûte le DELF B2 aux Pays-Bas ?", "175 € à l'Alliance française d'Amsterdam et à l'Institut français des Pays-Bas ; 110 € l'A1 ou l'A2, 155 € le B1, 220 € le DALF C1 et 230 € le C2. Le DELF junior B2 coûte 180 € à Amsterdam."),
         ("Peut-on encore s'inscrire pour novembre 2026 ?", "Plus à Amsterdam, où les inscriptions ont fermé le 25 octobre ; l'Institut français les prenait jusqu'au 26 octobre 2026. Les épreuves ont lieu du 9 au 13 novembre."),
         ("Où passer le DELF à La Haye ?", "À l'Alliance française de La Haye, qui organise des sessions en mars, juin et novembre. L'Institut français des Pays-Bas et le lycée français Van Gogh figurent aussi sur la liste FEI.")],
    also=[("/centres/tcf-pays-bas/", "TCF Canada aux Pays-Bas", "Amsterdam 290 €, La Haye, Rotterdam."),
          ("/centres/delf-belgique/", "DELF et DALF en Belgique", "Du 17 au 26 novembre 2026, B2 à 191 € à Gand."), A_CAL, A_DELF],
    sources="pages DELF-DALF de l'Alliance française d'Amsterdam, de l'Alliance française de La Haye, de l'Alliance française de Rotterdam (examens) et de l'Institut français des Pays-Bas (DELF-DALF tout public), consultées le 26 octobre 2026.",
    urls={"amsterdam-alliance-francaise-amsterdam": "https://www.afamsterdam.nl/en/certifications/delfdalf/",
          "la-haye-alliance-francaise-de-la-haye": "https://www.aflahaye.nl/diplomes-tests/diplomes-delf-dalf/",
          "groningue-institut-francais-de-groningue": "https://institutfrancais.nl/certifications-de-francais/delf-dalf/",
          "rotterdam-alliance-francaise-de-rotterdam": "http://www.alliancerotterdam.nl/examens/",
          "la-haye-lycee-francais-van-gogh": ""},
    notes={"la-haye-lycee-francais-van-gogh": NO_LINK},
))

# ===========================================================================
# GRÈCE — DELF-DALF
# ===========================================================================
PAGES.append(dict(EU,
    slug="delf-grece", exam="delf", file="fei_monde/delf_grece", layout="cities", chip="Grèce",
    crumb="DELF en Grèce",
    pointer="",
    title="DELF en Grèce : dates mai 2027, prix (B2 160 €)",
    desc="DELF et DALF en Grèce : B2 le 15 mai 2027 (inscriptions du 1er au 15 février), session des 4 et 5 décembre 2026, prix (B1 et B2 160 €).",
    h1="DELF et DALF en Grèce : les sessions de décembre et de mai, les prix et l'inscription",
    intro="""En Grèce, le DELF et le DALF passent par l'<strong>Institut français de Grèce</strong>, seul centre de la liste FEI,
qui les organise deux fois par an, en décembre et en mai, à Athènes, à Thessalonique et dans des centres de province.
Prochaine session : les <strong>4 et 5 décembre 2026</strong> (inscriptions closes le 11 octobre). En 2027, le DELF B2
a lieu le <strong>samedi 15 mai</strong>, avec des inscriptions en ligne du <strong>1er au 15 février 2027</strong>. Le
DELF B1 et le B2 coûtent <strong>160 €</strong>.""",
    facts=["<strong>1 centre agréé</strong> (liste FEI du 26 octobre 2026), l'Institut français de Grèce, qui fixe les centres d'examen de chaque session selon le nombre d'inscrits par région.",
           "Mai 2027 : A1, A2, C1 et C2 le vendredi 14 mai ; <strong>B1 et B2 le samedi 15 mai</strong> ; inscriptions du 1er au 15 février 2027, uniquement en ligne.",
           "Décembre 2026 : A1, A2, C1 et C2 le 4 décembre, B1 et B2 le 5 décembre ; inscriptions closes depuis le 11 octobre.",
           "Frais 2026 : <strong>A1 et A2 75 € · B1 et B2 160 € · C1 180 € · C2 200 €</strong>.",
           "Oraux à Athènes et à Thessalonique dans les jours qui suivent l'écrit ; en province, le week-end des écrits.",
           "Le programme précise qu'aucune demande de changement d'épreuve, écrite ou orale, n'est acceptée."],
    stats=[("1", "centre agréé", "l'Institut français de Grèce"), ("15 mai", "DELF B2 2027", "samedi, 18 h 30"),
           ("1-15 févr.", "inscriptions", "en ligne"), ("160 €", "le DELF B2", "comme le B1")],
    sections=[
        ("calendrier", "Les sessions de décembre 2026 et de mai 2027", table(
            "Programme des épreuves DELF-DALF de l'Institut français de Grèce (versions du 22 juillet et du 14 octobre 2026), relevé le 26 octobre 2026. Oraux d'Athènes et de Thessalonique ; en province, l'oral a lieu le week-end des écrits.",
            ["Diplôme", "Écrit déc. 2026", "Oral déc. (Athènes, Thess.)", "Écrit mai 2027", "Oral mai (Athènes, Thess.)"],
            [("DELF A1", "ven. 04/12, 17 h", "lun. 07/12", "ven. 14/05, 17 h", "10 ou 12/05"),
             ("DELF A2", "ven. 04/12, 19 h", "mar. 08/12", "ven. 14/05, 19 h", "11 ou 13/05"),
             ("DELF B1", "sam. 05/12, 16 h", "mer. 09/12", "sam. 15/05, 16 h", "17 ou 18/05"),
             ("<strong>DELF B2</strong>", "<strong>sam. 05/12, 18 h 30</strong>", "jeu. 10/12", "<strong>sam. 15/05, 18 h 30</strong>", "19 ou 20/05"),
             ("DALF C1", "ven. 04/12, 17 h", "ven. 11/12", "ven. 14/05, 17 h", "jeu. 27/05"),
             ("DALF C2", "ven. 04/12, 17 h", "lun. 14/12", "ven. 14/05, 17 h", "dim. 23/05")]) + """
<p>Inscriptions : du 1er au 11 octobre 2026 pour décembre (closes), du <strong>1er au 15 février 2027</strong> pour mai.
On ne peut pas s'inscrire à deux diplômes dont les horaires se chevauchent : l'A1 et le C1, par exemple, commencent tous
deux le vendredi à 17 h. Les DELF Prim A1 et A2, pour les moins de 12 ans, suivent les horaires de l'A1 et de l'A2.
L'Institut fait aussi passer, aux mêmes sessions, les examens de la Sorbonne.</p>"""),
        ("prix", "Combien coûte le DELF en Grèce ?", table(
            "Frais d'examen 2026 de l'Institut français de Grèce (DELF, DALF et Sorbonne), relevés le 26 octobre 2026.",
            ["Niveau", "Frais"],
            [("DELF A1 · A2", "75 €"), ("<strong>DELF B1 · B2</strong>", "<strong>160 €</strong>"), ("DALF C1", "180 €"), ("DALF C2", "200 €")], wide=False) + """
<p>Le paiement se fait à l'inscription, en ligne par carte ou à la banque avec le code de paiement que délivre la
plateforme. Ce sont les frais affichés pour 2026 ; ceux de la session de mai 2027 n'étaient pas encore publiés.</p>"""),
        ("inscription", "S'inscrire et passer l'examen", """<p>L'inscription se fait uniquement en ligne, sur la plateforme
eservices.ifg.gr, qui délivre un code de paiement ; elle suppose d'avoir lu le programme et le règlement des examens. Les
centres d'examen de chaque session — Athènes, Thessalonique et villes de province — ne sont annoncés qu'à la clôture des
inscriptions, selon le nombre de candidats par région. La convocation, avec l'heure de l'oral, s'imprime depuis le site
de l'Institut.</p>

<p>Le service des examens de l'Institut français de Grèce est au 31, rue Sina, à Athènes ; l'Institut français de
Thessalonique renseigne aussi les candidats du nord du pays. Les diplômes sont indépendants : on s'inscrit directement au
niveau visé, et il faut 50 points sur 100 pour l'obtenir.</p>"""),
    ],
    list_title="Le centre d'examen DELF-DALF agréé en Grèce",
    faq=[("Quelles sont les dates du DELF 2027 en Grèce ?", "Pour la session de mai 2027 : DELF A1, A2 et DALF C1, C2 le vendredi 14 mai, DELF B1 et B2 le samedi 15 mai 2027, avec des inscriptions du 1er au 15 février 2027. La session de décembre 2027 n'était pas publiée le 26 octobre 2026."),
         ("Quand a lieu le DELF B2 en décembre 2026 ?", "Le samedi 5 décembre 2026, de 18 h 30 à 21 h ; l'oral se passe le 10 décembre à Athènes et à Thessalonique, le 6 décembre en province. Les inscriptions ont fermé le 11 octobre."),
         ("Combien coûte le DELF B2 en Grèce ?", "160 €, comme le B1, selon les frais 2026 de l'Institut français de Grèce ; 75 € l'A1 ou l'A2, 180 € le DALF C1 et 200 € le C2."),
         ("Où passe-t-on le DELF en Grèce ?", "À Athènes, à Thessalonique ou dans un centre de province : l'Institut français de Grèce, seul centre agréé du pays, fixe la liste des centres de chaque session à la clôture des inscriptions, selon le nombre de candidats par région."),
         ("Faut-il passer l'A1 avant le B2 ?", "Non : les diplômes DELF et DALF sont indépendants, on s'inscrit directement au niveau visé. Seule contrainte en Grèce : ne pas choisir deux diplômes dont les horaires se chevauchent.")],
    also=[("/centres/tcf-grece/", "TCF Canada en Grèce", "Athènes, six sessions jusqu'en juin 2027."),
          ("/centres/delf-italie/", "DELF et DALF en Italie", "Février, avril et juin 2027, B2 à 160 €."), A_CAL, A_DELF],
    sources="programmes des examens DELF-DALF-Sorbonne de décembre 2026 et de mai 2027 (PDF), calendrier des examens 2026-2027, frais d'examen 2026 et pages des examens de l'Institut français de Grèce (ifg.gr), consultés le 26 octobre 2026.",
    urls={"athenes-ambassade-de-france-institut-francais-de-grece": "https://www.ifg.gr/eksetaseis/dino-eksetaseis-2/"},
))

# ===========================================================================
# POLOGNE — DELF-DALF
# ===========================================================================
PL_AF = {"katowice-alliance": "https://katowice.afpolska.pl/", "wrocaw-alliance-francaise-stowarzyszenie-wroclaw": "https://wroclaw.afpolska.pl/",
         "rzeszow-alliance-francaise-rzeszow": "https://rzeszow.afpolska.pl/"}
PAGES.append(dict(EU,
    slug="delf-pologne", exam="delf", file="fei_monde/delf_pologne", layout="cities", chip="Pologne",
    crumb="DELF en Pologne",
    pointer="",
    title="DELF en Pologne : sessions, prix (B2 620 zł), centres",
    desc="DELF et DALF en Pologne : session du 16 au 20 novembre 2026 (B2 le 18), inscriptions jusqu'au 6 novembre, prix (B2 620 zł) et les {n} centres.",
    h1="DELF et DALF en Pologne : les sessions, les prix en złotys et les {n} centres",
    intro="""En Pologne, le DELF et le DALF tout public se passent dans <strong>{n} centres</strong> — l'Institut français à
Varsovie et à Cracovie, huit Alliances françaises, des écoles et des universités —, aux mêmes dates : prochaine session du
<strong>16 au 20 novembre 2026</strong>, DELF B2 le <strong>18 novembre</strong>. Les Alliances françaises prennent les
inscriptions jusqu'au <strong>6 novembre</strong> ; à l'Institut français de Varsovie, elles ont fermé le 18 octobre. Le
B2 coûte <strong>620 zł</strong> (527 zł au tarif réduit) ; le calendrier 2027 n'était pas publié le 26 octobre 2026.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 26 octobre 2026), sous la gestion centrale de l'Institut français de Pologne : l'Institut à Varsovie et à Cracovie, huit Alliances françaises, le lycée français de Varsovie, l'université Adam-Mickiewicz de Poznań et trois associations.",
           "Novembre 2026 : A1 et A2 le 16, B1 le 17, <strong>B2 le 18</strong>, C1 le 19, C2 le 20 novembre ; oraux du 13 au 25 novembre dans les Alliances.",
           "Inscriptions : jusqu'au <strong>6 novembre 2026</strong> dans les Alliances françaises ; du 21 septembre au 18 octobre à l'Institut français de Varsovie (closes).",
           "En 2026, trois sessions tout public : février (B2 le 4), juin (B2 le 24) et novembre ; dates 2027 non publiées.",
           "Tarifs 2026 : <strong>A1 300 zł · A2 380 zł · B1 520 zł · B2 620 zł · C1 750 zł · C2 800 zł</strong>, 15 % de moins au tarif réduit.",
           "Résultats environ un mois après la session ; diplôme environ trois mois après (Alliances françaises)."],
    stats=[("{n}", "centres d'examen", "liste FEI du 26 octobre 2026"), ("18 nov.", "prochain B2", "2026"),
           ("6 nov.", "clôture", "dans les Alliances françaises"), ("620 zł", "le DELF B2", "527 zł au tarif réduit")],
    sections=[
        ("calendrier", "Les sessions 2026", table(
            "Dates des épreuves écrites du DELF-DALF tout public publiées par les Alliances françaises de Pologne ; l'Institut français de Varsovie affiche les mêmes pour novembre. Relevé du 26 octobre 2026.",
            ["Session", "A1 · A2", "B1", "B2", "C1", "C2", "Inscriptions (Alliances)"],
            [("Février 2026", "02/02", "03/02", "04/02", "05/02", "06/02", "01/12/2025 – 23/01/2026"),
             ("Juin 2026", "22/06", "23/06", "24/06", "25/06", "26/06", "01/04 – 12/06"),
             ("<strong>Novembre 2026</strong>", "16/11", "17/11", "<strong>18/11</strong>", "19/11", "20/11", "01/09 – <strong>06/11</strong>")]) + """
<p>À l'Institut français de Varsovie, les inscriptions de novembre ont couru du 21 septembre au 18 octobre 2026. Le
calendrier 2027 n'était publié ni par l'Institut ni par les Alliances le 26 octobre 2026 ; l'Institut à Cracovie annonçait
une grille de tarifs 2027 sans la rendre lisible. Les Alliances françaises de Pologne conseillent de vérifier, avant de
s'inscrire, que le centre choisi organise bien la session.</p>"""),
        ("prix", "Combien coûte le DELF en Pologne ?", table(
            "Tarifs 2026, identiques à l'Institut français de Varsovie et dans les Alliances françaises de Pologne, relevés le 26 octobre 2026.",
            ["Niveau", "Tarif", "Tarif réduit"],
            [("DELF A1", "300 zł", "255 zł"), ("DELF A2", "380 zł", "323 zł"), ("DELF B1", "520 zł", "442 zł"),
             ("<strong>DELF B2</strong>", "<strong>620 zł</strong>", "<strong>527 zł</strong>"), ("DALF C1", "750 zł", "637,50 zł"),
             ("DALF C2", "800 zł", "680 zł"), ("DELF junior A1 à B2", "280 à 580 zł", "238 à 493 zł"),
             ("DELF Prim A1.1 à A2", "260 à 350 zł", "221 à 297,50 zł")], wide=False) + """
<p>À l'Institut français de Varsovie, le tarif réduit va à ses élèves (inscrits au trimestre ou au semestre qui précède la
session) et aux candidats présentés par leur école ou leur institution, à partir de cinq ; dans les Alliances, les
conditions se demandent au secrétariat.</p>"""),
        ("inscription", "S'inscrire", """<p>À l'Institut français, on s'inscrit en ligne sur la page de la session, à Varsovie
ou à Cracovie ; dans les Alliances françaises — Gdańsk, Katowice, Lublin, Łódź, Rzeszów, Toruń, Wrocław —, par le
formulaire de l'Alliance choisie. Une attestation de réussite se demande par écrit au moment de l'inscription. Les
diplômes sont indépendants : on s'inscrit directement au niveau visé, et il faut 50 points sur 100 pour l'obtenir.</p>"""),
    ],
    list_title="Les {n} centres d'examen DELF-DALF, ville par ville",
    faq=[("Quand a lieu le prochain DELF en Pologne ?", "Du 16 au 20 novembre 2026 : A1 et A2 le 16, B1 le 17, B2 le 18, DALF C1 le 19 et C2 le 20 novembre. Les Alliances françaises prennent les inscriptions jusqu'au 6 novembre ; à l'Institut français de Varsovie, elles ont fermé le 18 octobre."),
         ("Les dates du DELF 2027 en Pologne sont-elles connues ?", "Pas encore : le 26 octobre 2026, ni l'Institut français ni les Alliances françaises ne publiaient leur calendrier 2027. En 2026, les sessions tout public ont eu lieu en février, en juin et en novembre."),
         ("Combien coûte le DELF B2 en Pologne ?", "620 zł, ou 527 zł au tarif réduit, à l'Institut français comme dans les Alliances françaises (tarifs 2026). Le DALF C1 coûte 750 zł et le C2 800 zł."),
         ("Où passer le DELF à Varsovie ?", "À l'Institut français de Pologne, qui tient la session de novembre (inscriptions en ligne, closes le 18 octobre 2026), ou au lycée français de Varsovie, aussi sur la liste FEI.")],
    also=[("/centres/tcf-pologne/", "TCF Canada en Pologne", "Varsovie et Cracovie."),
          ("/centres/delf-roumanie/", "DELF et DALF en Roumanie", "Les 14 et 15 novembre 2026."), A_CAL, A_DELF],
    sources="page de la session d'automne DELF-DALF tout public et grille des tarifs DELF-DALF 2026 de l'Institut français de Pologne (Varsovie) ; page des certificats DELF-DALF et tarifs 2026 (PDF) des Alliances françaises de Pologne (afpolska.pl) ; consultés le 26 octobre 2026.",
    urls=dict(PL_AF, **{"varsovie-institut-francais-de-pologne": "https://institutfrancais.pl/kursy-i-egzaminy/warszawa/egzaminy-warszawa/delf-dalf/delf-dalf-tp",
                        "cracovie-institut-francais-de-pologne-cracovie": "https://institutfrancais.pl/kursy-i-egzaminy/krakow/egzaminy-krakow/delf-dalf/delf-dalf-tp"}),
    notes={"katowice-alliance": "Site indiqué par FEI injoignable le 26 octobre 2026 : page de l'Alliance sur afpolska.pl.",
           "wrocaw-alliance-francaise-stowarzyszenie-wroclaw": "Page indiquée par FEI introuvable le 26 octobre 2026 : page de l'Alliance sur afpolska.pl.",
           "varsovie-institut-francais-de-pologne": "L'Institut reçoit au Plac Europejski 3 ; FEI donne l'adresse de la rue Widok."},
))

# ===========================================================================
# BELGIQUE — DELF-DALF
# ===========================================================================
PAGES.append(dict(EU,
    slug="delf-belgique", exam="delf", file="fei_monde/delf_belgique", layout="cities", chip="Belgique",
    crumb="DELF en Belgique",
    pointer="",
    title="DELF en Belgique : dates 2026-2027, prix (B2 191 €)",
    desc="DELF et DALF en Belgique : session du 17 au 26 novembre 2026 (B2 le 19), inscriptions à Gand jusqu'au 3 novembre, mars et juin 2027, prix.",
    h1="DELF et DALF en Belgique : les sessions, les prix et les {n} centres",
    intro="""En Belgique, le DELF et le DALF tout public se passent dans <strong>{n} centres</strong>, sous la gestion centrale
de l'Alliance française de Bruxelles-Europe, aux mêmes dates à Bruxelles et à Gand : prochaine session du <strong>17 au
26 novembre 2026</strong>, DELF B2 le <strong>19 novembre</strong>. À Gand, les inscriptions restent ouvertes jusqu'au
<strong>3 novembre</strong> ; à Bruxelles, elles ont fermé le 24 octobre. En 2027, Gand annonce des sessions en mars et
en juin, sans dates d'épreuves le 26 octobre 2026 ; le B2 y coûte <strong>191 €</strong>.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 26 octobre 2026) : les Alliances françaises de Bruxelles-Europe, d'Anvers et de Flandre orientale (Gand), KU Leuven Kulak à Courtrai, l'Institut supérieur des langues vivantes de l'Université de Liège et l'École européenne de Mol.",
           "Novembre 2026 : A1 et A2 le 17, B1 le 18, <strong>B2 le 19</strong>, C1 le 24, C2 le 26 novembre ; oraux du 16 au 20 et du 23 au 27 novembre à Bruxelles.",
           "Inscriptions : jusqu'au <strong>3 novembre 2026</strong> à Gand ; closes le 24 octobre à Bruxelles ; résultats fin décembre à Gand.",
           "2027 à Gand : mars (inscriptions du 1er décembre 2026 au 3 mars 2027) et juin (du 30 mars au 24 mai 2027) ; Bruxelles n'avait encore programmé aucune session 2027.",
           "Prix à Gand : <strong>A1 117 € · A2 127 € · B1 149 € · B2 191 € · C1 238 € · C2 254 €</strong> ; Bruxelles n'affiche pas ses tarifs, −10 % pour ses apprenants.",
           "En 2026, Bruxelles a tenu quatre sessions : mars, juin, septembre et novembre ; diplôme disponible 3 mois après l'examen."],
    stats=[("{n}", "centres d'examen", "liste FEI du 26 octobre 2026"), ("19 nov.", "prochain B2", "Bruxelles et Gand"),
           ("3 nov.", "clôture à Gand", "Bruxelles : 24 oct."), ("191 €", "le DELF B2 à Gand", "172,40 € pour ses élèves")],
    sections=[
        ("calendrier", "Les sessions 2026 et 2027", table(
            "Sessions DELF-DALF tout public de l'Alliance française de Bruxelles-Europe (2026) et de l'Alliance française de Flandre orientale (2027), relevées le 26 octobre 2026.",
            ["Session", "A1 · A2", "B1", "B2", "C1", "C2", "Inscriptions"],
            [("Mars 2026", "17/03", "18/03", "19/03", "24/03", "26/03", "01/12/2025 – 20/02/2026"),
             ("Juin 2026", "09/06", "10/06", "11/06", "16/06", "18/06", "22/02 – 16/05"),
             ("Septembre 2026", "15/09", "16/09", "17/09", "22/09", "24/09", "17/05 – 22/08"),
             ("<strong>Novembre 2026</strong>", "17/11", "18/11", "<strong>19/11</strong>", "24/11", "26/11", "Bruxelles 23/08 – 24/10 ; Gand 13/07 – <strong>03/11</strong>"),
             ("Mars 2027 (Gand)", "non fixé", "non fixé", "non fixé", "non fixé", "non fixé", "01/12/2026 – 03/03/2027"),
             ("Juin 2027 (Gand)", "non fixé", "non fixé", "non fixé", "non fixé", "non fixé", "30/03 – 24/05/2027")]) + """
<p>Les oraux se tiennent la semaine de l'écrit : à Bruxelles, du 16 au 20 novembre pour l'A1 au B2, du 23 au 27 novembre
pour le DALF. La page de Gand affiche le 29 novembre pour le B2 dans son calendrier et le 19 dans le détail du niveau ;
Bruxelles, centre de gestion, donne le 19. Anvers, Courtrai, Liège et Mol n'ont pas été relevés : leurs coordonnées
figurent dans la liste.</p>"""),
        ("prix", "Combien coûte le DELF en Belgique ?", table(
            "Tarifs de la session de novembre 2026 à l'Alliance française de Flandre orientale (Gand), relevés le 26 octobre 2026.",
            ["Niveau", "Tarif", "Élèves d'un cours de l'Alliance"],
            [("DELF A1", "117,00 €", "—"), ("DELF A2", "127,00 €", "—"), ("DELF B1", "149,00 €", "134,60 €"),
             ("<strong>DELF B2</strong>", "<strong>191,00 €</strong>", "<strong>172,40 €</strong>"), ("DALF C1", "238,00 €", "215,60 €"),
             ("DALF C2", "254,00 €", "230,00 €")], wide=False) + """
<p>À Gand, les droits se paient en ligne au moment de l'inscription ; ni remboursement, ni changement de niveau, ni report
après la clôture. L'Alliance de Bruxelles-Europe n'affichait pas ses tarifs le 26 octobre 2026 ; ses apprenants ont 10 %
de réduction, et le diplôme y est disponible à l'accueil trois mois après l'examen.</p>"""),
        ("inscription", "S'inscrire", """<p>On s'inscrit en ligne sur le site de l'Alliance choisie, niveau par niveau ;
l'inscription est nominative. À Gand, les convocations partent par e-mail entre le 3 et le 13 novembre 2026 ; sans
nouvelles une semaine avant l'examen, il faut contacter le centre. Les diplômes sont indépendants : on s'inscrit
directement au niveau visé, et il faut 50 points sur 100 pour l'obtenir.</p>"""),
    ],
    list_title="Les {n} centres d'examen DELF-DALF en Belgique",
    faq=[("Quand a lieu le prochain DELF en Belgique ?", "Du 17 au 26 novembre 2026 à Bruxelles et à Gand : A1 et A2 le 17, B1 le 18, B2 le 19, DALF C1 le 24 et C2 le 26 novembre. Gand prend les inscriptions jusqu'au 3 novembre ; à Bruxelles, elles ont fermé le 24 octobre."),
         ("Quelles sont les dates du DELF 2027 en Belgique ?", "Elles n'étaient pas fixées le 26 octobre 2026. L'Alliance française de Flandre orientale annonce une session en mars 2027 (inscriptions du 1er décembre 2026 au 3 mars 2027) et une en juin (du 30 mars au 24 mai 2027) ; Bruxelles-Europe n'avait encore rien programmé."),
         ("Combien coûte le DELF B2 en Belgique ?", "191 € à l'Alliance française de Gand, 172,40 € pour ses élèves. L'Alliance de Bruxelles-Europe n'affichait pas ses tarifs le 26 octobre 2026 ; ses apprenants ont 10 % de réduction."),
         ("Où passer le DELF à Bruxelles ?", "À l'Alliance française de Bruxelles-Europe, avenue des Arts 46, qui gère aussi le DELF-DALF pour toute la Belgique. En 2026, elle a tenu quatre sessions : mars, juin, septembre et novembre."),
         ("Quand reçoit-on son diplôme ?", "À Gand, les résultats de novembre 2026 arrivent fin décembre ; à Bruxelles, le diplôme est disponible à l'accueil trois mois après l'examen, et une attestation est remise à l'annonce des résultats.")],
    also=[("/centres/tcf-belgique/", "TCF Canada en Belgique", "Bruxelles 268 €, Gand 260 €."),
          ("/centres/delf-pays-bas/", "DELF et DALF aux Pays-Bas", "Mars et juin 2027 à Amsterdam, B2 à 175 €."), A_CAL, A_DELF],
    sources="pages DELF-DALF tout public de l'Alliance française de Bruxelles-Europe (onglets Calendrier et S'inscrire) et DELF-DALF de l'Alliance française de Flandre orientale (Gand), consultées le 26 octobre 2026.",
    urls={"bruxelles-alliance-francaise-bruxelles-europe": "https://alliancefr.be/passer-un-examen/delf-dalf/delf-dalf-tout-public",
          "gand-alliance-francaise-oost-vlaanderen": "https://www.af-ovl.be/delf-dalf"},
))

# ===========================================================================
# PORTUGAL — DELF-DALF
# ===========================================================================
PAGES.append(dict(EU,
    slug="delf-portugal", exam="delf", file="fei_monde/delf_portugal", layout="cities", chip="Portugal",
    crumb="DELF au Portugal",
    pointer="",
    title="DELF au Portugal : dates, prix (B2 140 €), {n} centres",
    desc="DELF et DALF au Portugal : le calendrier national, session des 19 et 20 novembre 2026 (inscriptions jusqu'au 6 novembre), prix (B2 140 €).",
    h1="DELF et DALF au Portugal : le calendrier national, les prix et les {n} centres",
    intro="""Au Portugal, le DELF et le DALF tout public suivent un <strong>calendrier national</strong>, publié par l'Institut
français du Portugal : cinq sessions en 2026, dont la dernière les <strong>19 et 20 novembre</strong> (A1, B1 et C1 le 19 ;
A2, B2 et C2 le 20), avec des inscriptions jusqu'au <strong>6 novembre</strong> dans sept Alliances françaises. Le DELF B2
coûte <strong>140 €</strong>, 126 € au tarif réduit. Le calendrier 2027 n'était pas publié le 26 octobre 2026.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 26 octobre 2026), sous la gestion du service de coopération linguistique et éducative (Lisbonne) : neuf Alliances françaises, les universités d'Aveiro, de Porto et des Açores, deux lycées français, une école internationale et l'Academia de Línguas da Madeira.",
           "Novembre 2026 : A1, B1 et C1 le 19 ; A2, <strong>B2</strong> et C2 le <strong>20 novembre</strong> ; oraux du 16 au 27 novembre ; inscriptions jusqu'au <strong>6 novembre</strong> ; résultats le 15 décembre.",
           "Où, en novembre : Alliances françaises de Porto, Guimarães, Coimbra, Faro, Viseu, Setúbal et Leiria.",
           "En 2026 : février, avril, juin, septembre et novembre ; 2027 non publié.",
           "Tarifs : <strong>A1 65 € · A2 75 € · B1 110 € · B2 140 € · C1 177 € · C2 190 €</strong> ; réduits, de 59 à 171 €.",
           "Le DELF Prim, le DELF junior et le DELF escolar ont leur propre calendrier."],
    stats=[("{n}", "centres d'examen", "liste FEI du 26 octobre 2026"), ("20 nov.", "prochain B2", "2026"),
           ("6 nov.", "clôture des inscriptions", "sept Alliances"), ("140 €", "le DELF B2", "126 € au tarif réduit")],
    sections=[
        ("calendrier", "Le calendrier national 2026", table(
            "Calendrier DELF-DALF 2026 de l'Institut français du Portugal (PDF), relevé le 26 octobre 2026. Le calendrier 2027 n'était pas encore publié.",
            ["Session", "A1 · B1 · C1", "A2 · B2 · C2", "Oraux", "Inscriptions", "Résultats"],
            [("Février", "12/02", "13/02", "09/02 – 20/02", "02/12/2025 – 30/01", "16/03"),
             ("Avril", "09/04", "10/04", "01/04 – 17/04", "01/01 – 27/03", "11/05"),
             ("Juin", "25/06", "26/06", "22/06 – 03/07", "01/01 – 15/06", "21/07"),
             ("Septembre", "24/09", "25/09", "21/09 – 02/10", "01/01 – 11/09", "20/10"),
             ("<strong>Novembre</strong>", "19/11", "<strong>20/11</strong>", "16/11 – 27/11", "01/01 – <strong>06/11</strong>", "15/12")]) + """
<p>Toutes les villes n'ouvrent pas chaque session : en février et en septembre, les Alliances de Lisbonne, Porto, Guimarães,
Coimbra, Faro, Viseu, Setúbal et Leiria et les universités de Porto et d'Aveiro ; en juin, les mêmes et l'Academia de
Línguas da Madeira ; en novembre, les Alliances de Porto, Guimarães, Coimbra, Faro, Viseu, Setúbal et Leiria seulement.</p>"""),
        ("prix", "Combien coûte le DELF au Portugal ?", table(
            "Tarifs 2026 de l'Institut français du Portugal, relevés le 26 octobre 2026.",
            ["Niveau", "Tarif", "Tarif réduit"],
            [("DELF A1", "65 €", "59 €"), ("DELF A2", "75 €", "68 €"), ("DELF B1", "110 €", "99 €"),
             ("<strong>DELF B2</strong>", "<strong>140 €</strong>", "<strong>126 €</strong>"), ("DALF C1", "177 €", "160 €"),
             ("DALF C2", "190 €", "171 €")], wide=False) + """
<p>Le tarif réduit vaut pour les candidats inscrits dans les centres cités par le calendrier et pour les inscriptions de
groupe, à partir de dix candidats par niveau. Le DELF-DALF tout public s'adresse aux candidats de 18 ans et plus ;
avant, ce sont le DELF junior ou le DELF escolar, pour les élèves du primaire et du secondaire, et le DELF Prim.</p>"""),
        ("inscription", "S'inscrire", """<p>On s'inscrit auprès de l'un des centres de la session choisie ; l'Institut français
du Portugal centralise le calendrier et publie, pour chaque diplôme, un PDF de dates et de prix. Après un incident
informatique, il a prolongé de 14 jours les délais de modification et d'annulation des inscriptions. Les diplômes sont
indépendants : on s'inscrit directement au niveau visé, et il faut 50 points sur 100 pour l'obtenir.</p>"""),
    ],
    list_title="Les {n} centres d'examen DELF-DALF, ville par ville",
    faq=[("Quand a lieu le prochain DELF au Portugal ?", "Les 19 et 20 novembre 2026 : A1, B1 et DALF C1 le 19, A2, B2 et C2 le 20, dans les Alliances françaises de Porto, Guimarães, Coimbra, Faro, Viseu, Setúbal et Leiria. Inscriptions jusqu'au 6 novembre, résultats le 15 décembre 2026."),
         ("Les dates du DELF 2027 au Portugal sont-elles connues ?", "Pas encore : le 26 octobre 2026, l'Institut français du Portugal ne publiait que son calendrier 2026, de cinq sessions (février, avril, juin, septembre, novembre)."),
         ("Combien coûte le DELF B2 au Portugal ?", "140 €, ou 126 € au tarif réduit (tarifs 2026 de l'Institut français du Portugal). Le DALF C1 coûte 177 € et le C2 190 €."),
         ("Peut-on passer le DELF à Lisbonne en novembre ?", "Non : en novembre 2026, le calendrier national ne prévoit l'examen que dans les Alliances de Porto, Guimarães, Coimbra, Faro, Viseu, Setúbal et Leiria. L'Alliance française de Lisbonne accueille les sessions de février, juin et septembre.")],
    also=[("/centres/tcf-portugal/", "TCF Canada au Portugal", "Porto et Faro 220 €, Viseu 211 €."),
          ("/centres/delf-espagne/", "DELF et DALF en Espagne", "Le calendrier national 2027."), A_CAL, A_DELF],
    sources="calendrier et tarifs DELF-DALF 2026 (PDF) et page des examens officiels de l'Institut français du Portugal (ifp-lisboa.com), consultés le 26 octobre 2026.",
    org_url="https://www.ifp-lisboa.com/lingua-francesa/examens-officiais/",
    urls={"lisbonne-lycee-francais-charles-lepierre": "https://www.lfcl.pt/",
          "porto-alliance-francaise-porto": "https://www.alliancefr.pt/porto/",
          "faro-alliance-francaise-de-l-algarve": "https://www.alliancefr.pt/algarve/",
          "viseu-alliance-francaise-de-viseu": "https://www.alliancefr.pt/viseu/",
          "coimbra-alliance-francaise-de-coimbra": "https://www.alliancefr.pt/coimbra/",
          "leiria-alliance-francaise-de-leiria": "https://www.alliancefr.pt/leiria/",
          "setubal-alliance-francaise-de-setubal": "https://www.alliancefr.pt/setubal/",
          "guimaraes-alliance-francaise-de-guimaraes-braga": "https://www.alliancefr.pt/braga/",
          "lisbonne-alliance-francaise-de-lisbonne": "https://lisboa.alliancefr.pt/"},
    notes={"lisbonne-lycee-francais-charles-lepierre": "Site indiqué par FEI hors service le 26 octobre 2026 : site actuel du lycée."},
))

# ===========================================================================
# IRLANDE — DELF-DALF
# ===========================================================================
PAGES.append(dict(EU,
    slug="delf-irlande", exam="delf", file="fei_monde/delf_irlande", layout="cities", chip="Irlande",
    crumb="DELF en Irlande",
    pointer="",
    title="DELF en Irlande : dates 2027, prix, {n} centres",
    desc="DELF et DALF en Irlande : B2 le 18 février, 22 avril, 24 juin, 23 septembre et 25 novembre 2027 ; les inscriptions, les prix (B2 145 € à Dublin).",
    h1="DELF et DALF en Irlande : le calendrier 2027, les prix et les {n} Alliances françaises",
    intro="""En Irlande, le DELF et le DALF tout public se passent dans les <strong>{n} Alliances françaises</strong> du pays —
Dublin, Cork, Kilkenny, Limerick, Waterford-Wexford —, sous la gestion centrale de l'Alliance de Dublin. Le calendrier
2027 publié par l'Alliance de Limerick compte cinq sessions, avec un DELF B2 le <strong>18 février</strong>, le 22 avril,
le 24 juin, le 23 septembre et le 25 novembre 2027 ; pour février, inscriptions du <strong>11 novembre 2026 au 11 janvier
2027</strong>. Avant cela, Dublin tient sa session du 24 au 27 novembre 2026, B2 le 26.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 26 octobre 2026) : les Alliances françaises de Dublin, Cork, Kilkenny, Limerick et Waterford-Wexford.",
           "2027 (Limerick) : A1 et A2 le mardi, B1 le mercredi, B2 le jeudi, C1 et C2 le vendredi — semaines du 16 février, du 20 avril, du 22 juin, du 21 septembre et du 23 novembre.",
           "Le DALF C1 et C2 se passe à Dublin, précise l'Alliance de Limerick.",
           "Novembre 2026 à Dublin : A1 et A2 le 24, B1 le 25, <strong>B2 le 26</strong>, C1 et C2 le 27 novembre.",
           "Prix : <strong>B2 145 € à Dublin</strong>, <strong>170 € à Limerick</strong> (tarifs 2027) ; DALF C1 195 € et 220 €.",
           "Résultats environ un mois après l'examen ; diplôme 3 à 4 mois après (Limerick)."],
    stats=[("{n}", "centres d'examen", "les Alliances françaises"), ("18 févr.", "premier B2 2027", "inscriptions jusqu'au 11 janv."),
           ("5", "sessions en 2027", "févr., avril, juin, sept., nov."), ("145 €", "le DELF B2 à Dublin", "170 € à Limerick")],
    sections=[
        ("calendrier", "Le calendrier 2027", table(
            "Calendrier DELF-DALF 2027 de l'Alliance française de Limerick (page mise à jour le 19 octobre 2026), « sujet à modification », relevé le 26 octobre 2026. Dates des épreuves écrites collectives.",
            ["Session", "A1 · A2", "B1", "B2", "C1 · C2 (à Dublin)", "Inscriptions"],
            [("<strong>Février 2027</strong>", "mar. 16/02", "mer. 17/02", "<strong>jeu. 18/02</strong>", "ven. 19/02", "11/11/2026 – 11/01/2027"),
             ("Avril 2027", "mar. 20/04", "mer. 21/04", "jeu. 22/04", "ven. 23/04", "18/01 – 18/03"),
             ("Juin 2027", "mar. 22/06", "mer. 23/06", "jeu. 24/06", "ven. 25/06", "15/03 – 17/05"),
             ("Septembre 2027", "mar. 21/09", "mer. 22/09", "jeu. 23/09", "ven. 24/09", "16/05 – 16/08"),
             ("Novembre 2027", "mar. 23/11", "mer. 24/11", "jeu. 25/11", "ven. 26/11", "18/08 – 18/10")]) + """
<p>L'oral individuel peut avoir lieu un autre jour que l'écrit. L'Alliance française de Dublin, centre de gestion,
affichait pour 2026 trois sessions — février, juin et novembre —, dont la dernière du 24 au 27 novembre 2026 ; elle
n'avait pas encore mis en ligne ses dates 2027 le 26 octobre. Le DELF junior et le DELF scolaire ont leurs propres
sessions (janvier, mars et mai 2027 à Limerick), le DELF Prim en mai et en juin.</p>"""),
        ("prix", "Combien coûte le DELF en Irlande ?", table(
            "Tarifs affichés le 26 octobre 2026 par l'Alliance française de Dublin (tout public) et l'Alliance française de Limerick (tarifs 2027).",
            ["Niveau", "Dublin", "Limerick 2027", "Limerick, tarif réduit"],
            [("DELF A1", "90 €", "115 €", "103,50 €"), ("DELF A2", "100 €", "115 €", "103,50 €"), ("DELF B1", "125 €", "150 €", "135 €"),
             ("<strong>DELF B2</strong>", "<strong>145 €</strong>", "<strong>170 €</strong>", "153 €"), ("DALF C1", "195 €", "220 €", "198 €"),
             ("DALF C2", "205 €", "230 €", "207 €")]) + """
<p>À Limerick, le tarif réduit (−10 %) vaut pour les élèves de l'Alliance et des organismes partenaires — écoles,
établissements d'enseignement supérieur, administrations. Le DELF junior y coûte de 95 à 145 €, le DELF scolaire de 50 à
75 €, le DELF Prim de 45 à 65 €.</p>"""),
        ("inscription", "S'inscrire", """<p>À Limerick, on télécharge le formulaire de son examen, on l'envoie par e-mail à
l'Alliance, puis on paie ; pour les moins de 18 ans, un parent le signe. À Dublin, la convocation arrive une semaine avant
l'examen. Les diplômes sont indépendants : on s'inscrit directement au niveau visé, et il faut 50 points sur 100 pour
l'obtenir.</p>"""),
    ],
    list_title="Les {n} centres d'examen DELF-DALF en Irlande",
    faq=[("Quelles sont les dates du DELF 2027 en Irlande ?", "Selon le calendrier 2027 de l'Alliance française de Limerick, le DELF B2 a lieu le 18 février, le 22 avril, le 24 juin, le 23 septembre et le 25 novembre 2027, le DALF C1 et C2 le lendemain, à Dublin. Pour février, les inscriptions vont du 11 novembre 2026 au 11 janvier 2027."),
         ("Quand a lieu le prochain DELF à Dublin ?", "Du 24 au 27 novembre 2026 : A1 et A2 le 24, B1 le 25, B2 le 26, DALF C1 et C2 le 27 novembre, selon la page de l'Alliance française de Dublin."),
         ("Combien coûte le DELF B2 en Irlande ?", "145 € à l'Alliance française de Dublin, selon les tarifs affichés le 26 octobre 2026 ; 170 € à Limerick en 2027, 153 € au tarif réduit."),
         ("Où passer le DALF C1 en Irlande ?", "À Dublin : l'Alliance française de Limerick précise que toutes les épreuves du DALF C1 et C2 s'y déroulent. Le C1 coûte 195 € à Dublin.")],
    also=[("/centres/tcf-irlande/", "TCF Canada en Irlande", "Dublin et Galway, 270 €."),
          ("/centres/delf-royaume-uni/", "DELF et DALF au Royaume-Uni", "Les centres et les sessions outre-Manche."), A_CAL, A_DELF],
    sources="page DELF & DALF de l'Alliance française de Dublin et page des examens DELF de l'Alliance française de Limerick (calendrier et tarifs 2027), consultées le 26 octobre 2026.",
    urls={"dublin-alliance-francaise-de-dublin": "https://www.alliance-francaise.ie/delf-dalf/",
          "limerick-alliance-francaise-de-limerick": "https://aflimerick.org/delf-exams/"},
    notes={"limerick-alliance-francaise-de-limerick": "Site non donné par FEI : celui de l'Alliance, relevé le 26 octobre 2026."},
))

# ===========================================================================
# SUÈDE — DELF-DALF (aucun centre TCF : TEF Canada et centres voisins)
# ===========================================================================
PAGES.append(dict(EU,
    slug="delf-suede", exam="delf", file="fei_monde/delf_suede", layout="cities", chip="Suède",
    crumb="DELF en Suède",
    pointer="",
    title="DELF en Suède : sessions, prix en SEK, {n} centres",
    desc="DELF et DALF en Suède : trois sessions par an à Stockholm, Uppsala, Borås, Växjö ; prix (B2 1 450 SEK) ; pas de TCF, TEF Canada à Stockholm.",
    h1="DELF et DALF en Suède : les sessions, les prix et les {n} centres",
    intro="""En Suède, le DELF et le DALF tout public sont organisés par l'<strong>Institut français de Suède</strong> trois fois
par an, à Stockholm, Uppsala, Borås et Växjö (Göteborg au printemps). En 2026 : 11-13 mars, 6-8 mai et
<strong>3-5 novembre</strong>, inscriptions closes le 9 octobre. Les dates 2027 n'étaient pas publiées le 26 octobre
2026. Le DELF B2 coûte <strong>1 450 SEK</strong>. La Suède n'a <strong>aucun centre TCF</strong> : pour le Canada,
l'Institut fait passer le TEF Canada (2 900 SEK).""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 26 octobre 2026), surtout des écoles et des lycées ; pour le tout public, l'Institut français de Suède annonce Stockholm, Uppsala, Borås, Växjö et Göteborg.",
           "2026 : 11-13 mars (inscriptions du 30 janvier au 13 février), 6-8 mai (27 mars – 10 avril), 3-5 novembre (25 septembre – 9 octobre).",
           "Tarifs depuis le 1er janvier 2026 : <strong>A1 800 · A2 900 · B1 950 · B2 1 450 · C1 2 500 · C2 2 800 SEK</strong>.",
           "Stockholm (Institut français) et Uppsala (université) : de l'A1 au C2 ; Borås et Växjö : de l'A1 au B2 ; Göteborg (Hvitfeldtska) : B1, B2 et C1 au printemps.",
           "<strong>Pas de centre TCF en Suède</strong> : TEF Canada à l'Institut français de Suède, 2 900 SEK, prochaine session le 25 novembre 2026 (inscriptions du 28 octobre au 11 novembre).",
           "TCF Canada au plus près : Fransk kulturhus à Oslo (3 150 NOK) ; Institut français du Danemark à Copenhague."],
    stats=[("{n}", "centres d'examen", "liste FEI du 26 octobre 2026"), ("3", "sessions par an", "mars, mai, novembre"),
           ("1 450 SEK", "le DELF B2", "C1 2 500 SEK"), ("0", "centre TCF", "TEF Canada à Stockholm")],
    sections=[
        ("calendrier", "Les sessions 2026", table(
            "Sessions DELF-DALF tout public de l'Institut français de Suède, relevées le 26 octobre 2026. Inscriptions dans la limite des places disponibles.",
            ["Session", "Épreuves", "Inscriptions", "Où"],
            [("Hiver 2026", "11, 12 et 13 mars", "30/01 – 13/02", "Stockholm, Uppsala, Borås, Växjö"),
             ("Printemps 2026", "6, 7 et 8 mai", "27/03 – 10/04", "Stockholm, Uppsala, Borås, Växjö, Göteborg"),
             ("<strong>Automne 2026</strong>", "<strong>3, 4 et 5 novembre</strong>", "25/09 – 09/10", "Stockholm, Uppsala, Borås, Växjö")]) + """
<p>Les dates 2027 n'étaient pas encore publiées le 26 octobre 2026 ; en 2026, chaque fenêtre d'inscription a duré deux
semaines et fermé un peu moins d'un mois avant les épreuves. Le DELF-DALF tout public s'adresse aux 18 ans et plus ; les
plus jeunes passent le DELF Prim ou le DELF junior, présentés sur une autre page de l'Institut.</p>"""),
        ("prix", "Combien coûte le DELF en Suède ?", table(
            "Tarifs de l'Institut français de Suède, en vigueur depuis le 1er janvier 2026, relevés le 26 octobre 2026.",
            ["Niveau", "Prix"],
            [("DELF A1", "800 SEK"), ("DELF A2", "900 SEK"), ("DELF B1", "950 SEK"), ("<strong>DELF B2</strong>", "<strong>1 450 SEK</strong>"),
             ("DALF C1", "2 500 SEK"), ("DALF C2", "2 800 SEK")], wide=False) + """
<p>Une fois la convocation envoyée, la place est réservée et les frais ne sont plus remboursés, sauf motif exceptionnel.</p>"""),
        ("tcf", "Pas de TCF en Suède : le TEF Canada et les centres voisins", """<p>Aucun centre TCF n'est agréé en Suède (liste FEI
du 26 octobre 2026). Pour un dossier canadien, l'Institut français de Suède fait passer l'autre test accepté par IRCC, le
<strong>TEF Canada</strong> : 2 900 SEK, plus 100 SEK d'inscription ; prochaine session le <strong>25 novembre 2026</strong>,
inscriptions du 28 octobre au 11 novembre 2026 ; cinq sessions en 2026 (janvier, avril, juin, septembre, novembre). Le TEF
pour la naturalisation française y coûte 2 000 SEK.</p>

<p>Le TCF Canada le plus proche se passe à Oslo, chez Fransk kulturhus (3 150 NOK, plusieurs sessions par an, inscription
au plus tard 5 semaines avant), ou à l'Institut français du Danemark, à Copenhague, dont la session TCF Canada du
30 octobre 2026 a clos ses inscriptions le 18 septembre ; le TCF tout public et le TCF IRN y ont lieu les 15 et 16 mars
2027.</p>"""),
    ],
    list_title="Les {n} centres d'examen DELF-DALF, ville par ville",
    faq=[("Quelles sont les dates du DELF 2027 en Suède ?", "Elles n'étaient pas publiées le 26 octobre 2026. En 2026, l'Institut français de Suède a tenu trois sessions — 11-13 mars, 6-8 mai et 3-5 novembre —, chacune avec deux semaines d'inscription, closes un peu moins d'un mois avant."),
         ("Combien coûte le DELF B2 en Suède ?", "1 450 SEK à l'Institut français de Suède (tarifs en vigueur depuis le 1er janvier 2026) ; 950 SEK le B1, 2 500 SEK le DALF C1."),
         ("Peut-on passer le TCF Canada en Suède ?", "Non : aucun centre TCF n'est agréé en Suède. L'Institut français de Suède fait passer le TEF Canada (2 900 SEK, session du 25 novembre 2026) ; le TCF Canada le plus proche est à Oslo (Fransk kulturhus, 3 150 NOK) ou à Copenhague."),
         ("Où passer le DELF hors de Stockholm ?", "À l'université d'Uppsala (A1 à C2), à Borås (Bodaskolan) et à Växjö (Linnéuniversitetet), de l'A1 au B2, et à Göteborg (Hvitfeldtska gymnasiet) pour le B1, le B2 et le C1 au printemps.")],
    also=[A_EUR, ("/centres/delf-allemagne/", "DELF et DALF en Allemagne", "Les dates 2026-2027, B2 à 201 €."), A_TEF, A_DELF],
    sources="pages des examens DELF et DALF et de l'examen TEF de l'Institut français de Suède (ifsuede.com) ; pages TCF de Fransk kulturhus (Oslo) et de l'Institut français du Danemark ; consultées le 26 octobre 2026.",
    org_url="https://ifsuede.com/",
    urls={"stockholm-institut-francais": "https://ifsuede.com/langue-francaise/examens-de-francais/examens-delf-et-dalf/",
          "hallsberg-alleskolan": ""},
    notes={"hallsberg-alleskolan": NO_LINK},
))

# ===========================================================================
# AUTRICHE — TCF (+ DELF-DALF)
# ===========================================================================
PAGES.append(dict(EU,
    slug="tcf-autriche", exam="tcf", file="fei_monde/tcf_autriche", layout="cities", chip="Autriche",
    crumb="TCF en Autriche",
    pointer="Institut français de Vienne : TCF Canada 295 €, TCF IRN 225 € ; session le 4 décembre 2026.",
    title="TCF Canada en Autriche : Vienne 295 €, DELF 2027",
    desc="TCF Canada en Autriche : 295 € à l'Institut français de Vienne, TCF IRN 225 €, session du 4 décembre 2026 ; DELF-DALF les 27, 28 et 29 janvier 2027.",
    h1="TCF Canada et DELF en Autriche : l'Institut français de Vienne, les prix et les dates",
    intro="""En Autriche, un seul centre est agréé pour le TCF : l'<strong>Institut français d'Autriche</strong>, à Vienne. Il
affiche le <strong>TCF Canada à 295 €</strong>, le TCF IRN à 225 € et le TCF tout public de 135 à 295 € ; sa seule session
TCF publiée a lieu le <strong>4 décembre 2026</strong>, avec une clôture des inscriptions le <strong>4 novembre</strong>.
Pour le DELF et le DALF, la prochaine session de l'Institut tombe les <strong>27, 28 et 29 janvier 2027</strong> ;
l'Institut culturel franco-autrichien de Graz organise la sienne en mai 2027.""",
    facts=["<strong>1 centre TCF agréé</strong> (liste FEI du 26 octobre 2026) : l'Institut français d'Autriche, Praterstraße 38, à Vienne.",
           "TCF Canada <strong>295 €</strong> · TCF IRN 225 € · TCF tout public 135 € (épreuves obligatoires), 235 € avec l'expression écrite ou orale, 295 € complet · TCF Québec sur demande.",
           "Session TCF : <strong>04/12/2026</strong>, inscriptions jusqu'au 04/11 ; pièce d'identité avec photo obligatoire, photo prise le jour de l'examen.",
           "Aucune demande de recorrection pour les sessions postérieures au 1er août 2026.",
           "DELF-DALF à Vienne, janvier 2027 : A2 et B1 le 27, C1 et C2 le 28, <strong>A1 et B2 le 29 janvier</strong> ; frais de 130 à 220 €, 104 € au tarif étudiant ; épreuves aussi à Salzbourg et à Innsbruck.",
           "Graz : DELF-DALF tout public en mai 2027 ; DELF scolaire les 9 et 10 mars 2027 (clôture le 29 janvier)."],
    stats=[("1", "centre TCF agréé", "Vienne"), ("295 €", "le TCF Canada", "TCF IRN 225 €"),
           ("4 déc.", "session TCF", "clôture le 4 nov."), ("27-29 janv.", "DELF-DALF 2027", "Vienne")],
    sections=[
        ("releve", "Le TCF à l'Institut français de Vienne", releve([
            ("Institut français d'Autriche (Vienne)", "<strong>Canada</strong>, IRN, tout public (et DAP) ; Québec sur demande",
             "Canada <strong>295 €</strong> · IRN 225 € · tout public 135 €, 235 € ou 295 €",
             "04/12/2026 (clôture 04/11) ; 2027 non publié. Inscription en ligne sur le portail des examens de l'Institut ; pièce d'identité avec photo obligatoire."),
        ]) + """
<p>Selon l'Institut, la formule « épreuves obligatoires + expression écrite » est le test officiel de la procédure DAP
(demande d'admission préalable). Aucune demande de recorrection n'est acceptée pour les sessions postérieures au
1er août 2026. Le TEF Canada, l'autre test accepté par IRCC, n'a pas de centre en Autriche sur la carte du Français des
affaires lue le 26 octobre 2026.</p>"""),
        ("delf", "Le DELF et le DALF en Autriche", """<p>Deux centres font passer le DELF et le DALF tout public (liste FEI du
26 octobre 2026) : l'<strong>Institut français d'Autriche</strong> à Vienne, gestion centrale du pays, qui organise aussi
des épreuves à Salzbourg et à Innsbruck, et l'<strong>Institut culturel franco-autrichien de Graz</strong>, qui gère ses
propres inscriptions. On peut s'y présenter dès 16 ans.</p>
""" + table("Session DELF-DALF de janvier 2027 de l'Institut français d'Autriche, relevée le 26 octobre 2026.",
            ["Date", "Épreuves écrites"],
            [("mercredi 27/01/2027", "DELF A2 et B1"), ("jeudi 28/01/2027", "DALF C1 et C2"),
             ("<strong>vendredi 29/01/2027</strong>", "<strong>DELF A1 et B2</strong>")], wide=False) + """
<p>Les dates des oraux sont communiquées après la clôture des inscriptions, au plus tard une semaine avant l'écrit. Les
frais vont de 130 à 220 € selon le niveau, 104 € au tarif étudiant ; l'inscription n'est valable qu'une fois les frais
reçus, et ne se rembourse que sur certificat médical. À Graz, le DELF-DALF tout public a lieu en mai 2027 (clôture non
encore fixée) et le DELF scolaire les 9 et 10 mars 2027, inscriptions et paiement jusqu'au 29 janvier 2027.</p>"""),
    ],
    list_title="Le centre TCF agréé en Autriche",
    faq=[("Où passer le TCF Canada en Autriche ?", "À l'Institut français d'Autriche, à Vienne (Praterstraße 38) : c'est le seul centre TCF agréé du pays, et il affiche le TCF Canada à 295 €."),
         ("Quand a lieu le prochain TCF à Vienne ?", "Le 4 décembre 2026, avec une clôture des inscriptions le 4 novembre ; c'était la seule session TCF publiée le 26 octobre 2026. Le TCF Québec se passe à une date fixée sur demande."),
         ("Combien coûte le TCF IRN en Autriche ?", "225 € à l'Institut français de Vienne ; le TCF tout public coûte 135 € pour les épreuves obligatoires et 295 € avec les deux épreuves d'expression."),
         ("Quelles sont les dates du DELF 2027 en Autriche ?", "À l'Institut français de Vienne : DELF A2 et B1 le 27 janvier, DALF C1 et C2 le 28 janvier, DELF A1 et B2 le 29 janvier 2027. À Graz, la session tout public a lieu en mai 2027."),
         ("Combien coûte le DELF en Autriche ?", "De 130 à 220 € à l'Institut français de Vienne selon le niveau, 104 € au tarif étudiant ; Graz fixe ses propres tarifs.")],
    also=[("/centres/tcf-allemagne/", "TCF Canada en Allemagne", "Munich, 295 €, des sessions chaque mois."),
          ("/centres/tcf-suisse/", "TCF en Suisse", "Le TCF Canada à Montreux et à Zurich."), A_EUR, A_NCLC],
    sources="pages TCF et DELF-DALF de l'Institut français d'Autriche (institutfrancais.at) et page DELF-DALF de l'Institut culturel franco-autrichien de Graz (franceautriche.at), consultées le 26 octobre 2026 ; carte des centres TEF du Français des affaires, lue le même jour.",
    badges={"vienne-institut-francais": OK_CA},
    notes={"vienne-institut-francais": "Le lien publié par FEI ne répond plus : page TCF de l'Institut relevée le 26 octobre 2026."},
    urls={"vienne-institut-francais": "https://www.institutfrancais.at/kurse/tcf-zertifikate"},
))

# ===========================================================================
# LUXEMBOURG — TCF (+ DELF-DALF)
# ===========================================================================
LU = ["esch-sur-alzette-institut-national-des-langues-site-belval", "luxembourg-institut-national-des-langues"]
PAGES.append(dict(EU,
    slug="tcf-luxembourg", exam="tcf", file="fei_monde/tcf_luxembourg", layout="cities", chip="Luxembourg",
    crumb="TCF au Luxembourg",
    pointer="Institut national des langues : TCF tout public (120 €) et TCF IRN (150 €), pas de TCF Canada.",
    title="TCF au Luxembourg : INLL, pas de TCF Canada, DELF",
    desc="TCF au Luxembourg : l'Institut national des langues fait passer le TCF tout public (120 €) et le TCF IRN (150 €), pas le TCF Canada ; DELF B2 à 186 €.",
    h1="TCF et DELF au Luxembourg : l'Institut national des langues, les prix et les sessions",
    intro="""Au Luxembourg, les deux centres TCF agréés sont les sites de l'<strong>Institut national des langues Luxembourg</strong>
(INLL), à Luxembourg et à Esch-sur-Alzette (Belval). Son calendrier ne propose que le <strong>TCF tout public</strong>
(120 € les épreuves obligatoires) et le <strong>TCF IRN</strong> (150 €), sur papier : <strong>pas de TCF Canada</strong>.
Les sessions 2026 sont closes ; pour le Canada, les centres les plus proches sont à Bruxelles (268 €), à Aix-la-Chapelle
et à Mayence (295 €). L'INLL fait aussi passer le DELF A2 à B2 et le DALF C1.""",
    facts=["<strong>{n} centres TCF agréés</strong> (liste FEI du 26 octobre 2026) : l'INLL, boulevard de la Foire à Luxembourg, et son site de Belval à Esch-sur-Alzette.",
           "TCF tout public sur papier : <strong>120 €</strong> les épreuves obligatoires, +55 € l'expression écrite, +55 € l'expression orale ; TCF IRN : <strong>150 €</strong>.",
           "Sessions 2026 : TCF IRN le 19/10 (clôture 14/09), TCF tout public le 23/11 (clôture 12/10) ; 2027 non publié.",
           "<strong>Pas de TCF Canada</strong> : la fiche d'inscription 2026 de l'INLL ne propose que le tout public et l'IRN.",
           "L'examen n'a lieu qu'à partir de 5 candidats par niveau ; sinon, les frais sont remboursés.",
           "DELF-DALF à l'INLL : B1 145 €, B2 186 €, C1 232 € (session du 9 au 11 novembre 2026, B2 complet) ; A2 124 € en février 2027."],
    stats=[("{n}", "centres agréés", "les deux sites de l'INLL"), ("0", "TCF Canada", "tout public et IRN seulement"),
           ("150 €", "le TCF IRN", "sur papier"), ("186 €", "le DELF B2", "session de novembre complète")],
    sections=[
        ("releve", "Le TCF à l'Institut national des langues", releve([
            ("Institut national des langues Luxembourg (Luxembourg et Belval)", "tout public et IRN, sur papier — <strong>pas de TCF Canada</strong>",
             "tout public 120 € (+55 € par épreuve d'expression) · IRN 150 €",
             "IRN 19/10/2026 (clôture 14/09) ; tout public 23/11/2026 (clôture 12/10) ; 2027 non publié. Dossier par e-mail ou par courrier : fiche, pièce d'identité, preuve de paiement."),
        ]) + """
<p>Les épreuves 2026 se tiennent au site du Glacis, boulevard de la Foire. Les inscriptions peuvent fermer avant la date
limite affichée ; la convocation arrive au plus tard deux semaines avant la première épreuve. En cas de force majeure,
l'INLL peut reporter l'inscription à une session ultérieure, dans les 12 mois, sur justificatif fourni dans les cinq jours.
Pour le TCF IRN, la fiche demande le motif : naturalisation, carte de résident ou carte de séjour pluriannuelle en
France.</p>"""),
        ("canada", "Où passer le TCF Canada près du Luxembourg ?", """<p>Le 26 octobre 2026, l'INLL ne proposait pas la version
Canada. Les centres qui l'annoncent au plus près : l'Alliance française de Bruxelles-Europe (<strong>268 €</strong>,
session du 9 décembre 2026), l'Institut culturel franco-allemand d'Aix-la-Chapelle et l'Institut français de Mayence
(<strong>295 €</strong>), en Allemagne. Le TEF Canada, l'autre test accepté par IRCC, a un centre au Luxembourg sur la
carte du Français des affaires — inlingua Luxembourg —, sans session publiée le 26 octobre 2026.</p>"""),
        ("delf", "Le DELF et le DALF au Luxembourg", """<p>Deux centres font passer le DELF-DALF (liste FEI du 26 octobre 2026) :
l'INLL, gestion centrale du pays, et le lycée Michel-Lucius, à Luxembourg. L'INLL propose le DELF A2, B1 et B2 et le
DALF C1 :</p>
""" + table("Calendrier des examens 2026 de l'INLL (version du 10 septembre 2026), relevé le 26 octobre 2026.",
            ["Niveau", "Prix", "Épreuves", "Clôture"],
            [("DELF A2", "124 €", "février 2027", "—"), ("DELF B1", "145 €", "9-11/11/2026", "18/09/2026"),
             ("<strong>DELF B2</strong>", "<strong>186 €</strong>", "9-11/11/2026", "plus de places disponibles"),
             ("DALF C1", "232 €", "9-11/11/2026", "18/09/2026")], wide=False) + """
<p>La session de novembre 2026 est close ; les dates 2027 du B1, du B2 et du C1 n'étaient pas publiées le 26 octobre
2026.</p>"""),
    ],
    list_title="Les {n} centres TCF agréés au Luxembourg",
    faq=[("Peut-on passer le TCF Canada au Luxembourg ?", "Non, pas le 26 octobre 2026 : l'Institut national des langues, seul organisme TCF du pays, ne propose que le TCF tout public et le TCF IRN. Les centres les plus proches qui annoncent le TCF Canada sont Bruxelles (268 €), Aix-la-Chapelle et Mayence (295 €)."),
         ("Combien coûte le TCF IRN au Luxembourg ?", "150 € à l'INLL, sur papier. La session 2026 a eu lieu le 19 octobre (clôture le 14 septembre) ; celles de 2027 n'étaient pas publiées."),
         ("Combien coûte le TCF tout public au Luxembourg ?", "120 € pour les épreuves obligatoires à l'INLL, plus 55 € pour l'expression écrite et 55 € pour l'expression orale. Session du 23 novembre 2026, inscriptions closes le 12 octobre."),
         ("Où passer le DELF B2 au Luxembourg ?", "À l'Institut national des langues, 186 € ; la session du 9 au 11 novembre 2026 n'avait plus de places le 26 octobre. Le lycée Michel-Lucius est aussi centre DELF-DALF.")],
    also=[("/centres/tcf-belgique/", "TCF Canada en Belgique", "Bruxelles 268 €, Gand 260 €."),
          ("/centres/tcf-allemagne/", "TCF Canada en Allemagne", "Aix-la-Chapelle et Mayence, 295 €."),
          ("/centres/tcf-france/", "Centres TCF en France", "Les centres agréés, région par région."), A_EUR],
    sources="fiche d'inscription TCF 2026 (PDF), calendrier des examens et tests 2026 (version du 10 septembre 2026) et page des certifications de l'Institut national des langues Luxembourg (inll.lu), consultés le 26 octobre 2026 ; carte des centres TEF du Français des affaires, lue le même jour.",
    badges={k: NO_CA for k in LU},
    notes={"luxembourg-institut-national-des-langues": "FEI indique des sessions sur ordinateur ; le calendrier 2026 de l'INLL annonce le TCF sur papier."},
    urls={k: "https://www.inll.lu/fr/certifications/" for k in LU},
))
