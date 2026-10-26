# -*- coding: utf-8 -*-
"""Chercheur de centres (26/10/2026) : textes des quatre pages, et leurs specs pour le registre des traductions.

PAGES (anglais, espagnol, arabe) porte fr_path="/trouver-un-centre/" : i18n_registry en tire les balises hreflang
des quatre pages. Le rendu est fait par make_finder.py (gabarit article_template.render) ; les données viennent de
make_gazetteer.py (site/data/finder/, site/data/geo/).

Champs de TEXT : {n} centres, {p} pays, {tcf} {delf} {civ} {tef} par examen, {cities} villes, {date} (listes FEI et
CCI), {date_civ} (examen civique) — remplis par make_finder.py à partir des données.
"""

FR_PATH = "/trouver-un-centre/"

PAGES = [
    dict(lang="en", slug="test-centre-near-me", fr_path=FR_PATH),
    dict(lang="es", slug="centro-de-examen-cerca-de-mi", fr_path=FR_PATH),
    dict(lang="ar", slug="test-centre-near-me", fr_path=FR_PATH),
]

FEI_LISTE = "https://www.france-education-international.fr/centres-d-examen/liste"
CCI_CARTE = "https://francais.cci-paris-idf.fr/candidat"
GEONAMES = '<a href="https://www.geonames.org/" rel="noopener">GeoNames</a> (<a href="https://creativecommons.org/licenses/by/4.0/" rel="noopener">CC BY 4.0</a>)'

REGIONS = {
    "fr": {"europe": "Europe", "monde_arabe": "Monde arabe", "afrique": "Afrique subsaharienne et océan Indien",
           "ameriques": "Amériques et Caraïbes", "asie_oceanie": "Asie et Océanie", "moyen_orient": "Iran et Israël"},
    "en": {"europe": "Europe", "monde_arabe": "Arab world", "afrique": "Sub-Saharan Africa and the Indian Ocean",
           "ameriques": "The Americas and the Caribbean", "asie_oceanie": "Asia and Oceania", "moyen_orient": "Iran and Israel"},
    "es": {"europe": "Europa", "monde_arabe": "Mundo árabe", "afrique": "África subsahariana y océano Índico",
           "ameriques": "América y el Caribe", "asie_oceanie": "Asia y Oceanía", "moyen_orient": "Irán e Israel"},
    "ar": {"europe": "أوروبا", "monde_arabe": "العالم العربي", "afrique": "أفريقيا جنوب الصحراء والمحيط الهندي",
           "ameriques": "الأمريكتان والكاريبي", "asie_oceanie": "آسيا وأوقيانوسيا", "moyen_orient": "إيران وإسرائيل"},
}
REGION_ORDER = {"fr": ["europe", "monde_arabe", "afrique", "ameriques", "asie_oceanie", "moyen_orient"],
                "en": ["ameriques", "europe", "asie_oceanie", "monde_arabe", "afrique", "moyen_orient"],
                "es": ["ameriques", "europe", "monde_arabe", "afrique", "asie_oceanie", "moyen_orient"],
                "ar": ["monde_arabe", "europe", "ameriques", "afrique", "asie_oceanie", "moyen_orient"]}
EXAM_LABEL = {"fr": {"tcf": "TCF", "delf": "DELF-DALF", "civique": "examen civique", "tef": "TEF"},
              "en": {"tcf": "TCF", "delf": "DELF-DALF", "civique": "civics test", "tef": "TEF"},
              "es": {"tcf": "TCF", "delf": "DELF-DALF", "civique": "examen cívico", "tef": "TEF"},
              "ar": {"tcf": "TCF", "delf": "DELF-DALF", "civique": "الامتحان المدني", "tef": "TEF"}}
MONTHS = {"fr": "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split(),
          "en": "January February March April May June July August September October November December".split(),
          "es": "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split(),
          "ar": "يناير فبراير مارس أبريل مايو يونيو يوليو أغسطس سبتمبر أكتوبر نوفمبر ديسمبر".split()}


def date_label(iso, lang):
    y, m, d = int(iso[:4]), int(iso[5:7]), int(iso[8:10])
    mo = MONTHS[lang][m - 1]
    return {"fr": f"{d} {mo} {y}", "en": f"{mo} {d}, {y}", "es": f"{d} de {mo} de {y}", "ar": f"{d} {mo} {y}"}[lang]


def centres_word(n, lang):
    if lang == "ar":
        return "مركز واحد" if n == 1 else "مركزان" if n == 2 else f"{n} مراكز" if n <= 10 else f"{n} مركزًا"
    w = {"fr": "centre", "en": "centre", "es": "centro"}[lang]
    return f"{n} {w}{'s' if n > 1 else ''}"


TEXT = {}

TEXT["fr"] = dict(
    path=FR_PATH, crumb="Trouver un centre",
    title="Centre TCF ou DELF près de chez vous : recherche par ville",
    desc="Le centre d'examen TCF, DELF-DALF, TEF ou examen civique le plus proche : {n} centres agréés dans {p} pays et territoires, avec distance et téléphone.",
    h1="Trouver un centre d'examen TCF, DELF ou TEF près de chez vous",
    intro="""Tapez votre ville, votre pays ou le nom d'un centre — ou touchez « Autour de moi » — pour voir les
centres d'examen agréés les plus proches, avec la distance, l'adresse, le téléphone et le site : <strong>{n} centres
TCF, DELF-DALF, TEF et examen civique dans {p} pays et territoires</strong>, d'après les listes officielles lues le {date}.""",
    facts=["<strong>{n} centres agréés</strong> dans {p} pays et territoires : {tcf} centres TCF, {delf} centres DELF-DALF, {tef} centres TEF et {civ} centres d'examen civique en France.",
           "Listes officielles lues le {date} — France Éducation international pour le TCF et le DELF-DALF, la CCI Paris Île-de-France pour le TEF ; examen civique : liste de FEI du {date_civ}.",
           "La recherche se fait dans votre navigateur : ni votre position ni ce que vous tapez ne partent vers un service tiers."],
    tool_h2="Chercher un centre", label="Ville, pays ou nom du centre", ph="Lyon, Casablanca, Montréal…", go="Chercher",
    legend="Examen", all="Tous", ex={"tcf": "TCF", "delf": "DELF-DALF", "civique": "Examen civique (France)", "tef": "TEF"},
    near="Autour de moi", privacy="Votre position ne sert qu'à calculer les distances dans cette page : elle ne quitte pas votre navigateur.",
    note="""<strong>TCF :</strong> la liste de France Éducation international ne dit pas si un centre organise le TCF Canada,
le TCF IRN ou le TCF Québec — vérifiez sur son site ; <a href="/ou-passer/">nos guides « Où passer »</a> l'ont relevé
pour les principaux centres. <strong>TEF :</strong> la carte de la CCI montre les sessions ouvertes le jour de sa lecture,
pas les épreuves agréées. Cette page n'appelle aucun service tiers — ni carte, ni police, ni statistiques. Noms de lieux :
{geonames}.""",
    noscript="La recherche a besoin de JavaScript ; la liste complète des pays et des villes se trouve plus bas.",
    sections=[
        ("choisir", "TCF Canada, TCF IRN, DELF ou TEF : lequel chercher ?", """<ul class="decision">
<li><b><a href="/tcf-canada/">TCF Canada</a> — immigration au Canada</b><span>Accepté par IRCC, comme le TEF Canada ; l'attestation vaut deux ans. Filtre « TCF », puis vérifiez sur le site du centre qu'il organise bien la version Canada.</span></li>
<li><b><a href="/tcf-quebec/">TCF Québec</a> — immigration au Québec</b><span>Des épreuves au choix ; mêmes centres TCF, même vérification à faire.</span></li>
<li><b><a href="/tcf-irn/">TCF IRN</a> — naturalisation, carte de résident</b><span>Le test des démarches françaises : le B2 est exigé pour la naturalisation depuis 2026, le B1 pour la carte de résident.</span></li>
<li><b><a href="/delf-b2/">DELF</a> et <a href="/dalf/">DALF</a> — un diplôme</b><span>Diplômes valables à vie, passés niveau par niveau ; les adultes passent le DELF tout public. Filtre « DELF-DALF ».</span></li>
<li><b><a href="/tef-canada/">TEF Canada, TEF IRN</a> — l'autre famille de tests</b><span>Organisés par le réseau du Français des affaires (CCI Paris Île-de-France) : filtre « TEF ».</span></li>
<li><b><a href="/blog/ou-passer-l-examen-civique/">Examen civique</a> — titres de séjour, naturalisation</b><span>Obligatoire depuis 2026 avec le test de français ; filtre « Examen civique » pour les centres agréés par FEI en France.</span></li>
</ul>
<p>Un diplôme ou un test ? Les différences sont détaillées dans <a href="/blog/diplome-ou-test-delf-tcf/">diplôme ou test : lequel vous faut-il</a>.</p>"""),
        ("liste-officielle", "Ce que la liste officielle ne dit pas", """<p>Les listes officielles disent qu'un centre est <strong>agréé</strong>.
Elles ne disent ni quelle version du TCF il organise (Canada, Québec, IRN), ni ses <strong>dates</strong>, ni ses
<strong>prix</strong> : il n'existe aucun tarif national, et deux centres d'une même ville peuvent proposer des sessions
et des prix sans rapport. Pour le TEF, la carte de la CCI montre les sessions ouvertes le jour de sa lecture, pas les
épreuves agréées. Ce que nous avons relevé centre par centre se trouve dans <a href="/centres/">l'annuaire des centres</a>,
les <a href="/ou-passer/">guides « Où passer »</a> par pays et par ville, <a href="/blog/prix-tcf-tef/">les prix du TCF
et du TEF</a>, <a href="/blog/tcf-canada-dates-2026/">les dates du TCF Canada</a> et <a href="/blog/calendrier-delf-dalf-2026-2027/">le
calendrier du DELF-DALF</a>. Un organisme absent de ces listes n'est pas agréé.</p>"""),
    ],
    list_h2="Tous les pays et toutes les villes",
    list_intro="Les {p} pays et territoires où se trouve au moins un centre, et le nombre de centres par ville ({cities} villes). Une ville en lien a sa page détaillée sur ce site.",
    ours="Nos pages", official="Listes officielles",
    faq=[("Y a-t-il un centre TCF Canada près de chez moi ?", "Tapez votre ville ou touchez « Autour de moi » avec le filtre TCF : les centres TCF agréés les plus proches s'affichent, avec la distance. La liste de France Éducation international ne dit pas lesquels organisent le TCF Canada : vérifiez sur le site du centre — nos guides par pays et par ville l'ont relevé pour les principaux centres. Le TEF Canada, accepté lui aussi par IRCC, se passe dans les centres du filtre TEF."),
         ("Un adulte peut-il passer le DELF ?", "Oui : le DELF tout public s'adresse aux adultes. Le DELF junior et le DELF scolaire visent les adolescents — en France, les centres de l'académie (CASNAV) sont orientés DELF scolaire. Demandez au centre quelle version il organise avant de vous inscrire."),
         ("Comment réserver une date ?", "Directement auprès du centre, en ligne le plus souvent — jamais auprès de France Éducation international ni de la CCI Paris Île-de-France. Chaque fiche donne le site, le téléphone et l'e-mail du centre ; pour le TEF, le lien « Contact (CCI) » ouvre la page du centre sur la plateforme de la CCI."),
         ("Cette liste est-elle à jour ?", "Elle reprend les listes officielles lues le {date} — France Éducation international pour le TCF et le DELF-DALF, la CCI Paris Île-de-France pour le TEF — et celle du {date_civ} pour l'examen civique. Les centres changent au fil des agréments : en cas de doute, la liste officielle fait foi."),
         ("Ma position est-elle envoyée quelque part ?", "Non. « Autour de moi » ne demande votre position au navigateur que lorsque vous touchez le bouton, et les distances sont calculées dans la page : ni la position ni la recherche ne quittent votre appareil. La page n'appelle aucun service tiers.")],
    also=[("/centres/", "L'annuaire des centres d'examen", "La liste par pays, région et ville, avec les relevés de prix et de dates."),
          ("/ou-passer/", "Où passer le DELF, le TCF ou le TEF ?", "Les guides par pays : prix relevés, dates de session, inscription."),
          ("/blog/prix-tcf-tef/", "Combien coûte vraiment le TCF ou le TEF ?", "Aucun tarif national : les prix relevés centre par centre."),
          ("/blog/diplome-ou-test-delf-tcf/", "Diplôme ou test : lequel vous faut-il ?", "")],
    cta_h2="Le centre vous donne la date ; le score, c'est vous",
    cta_p="""Une session se paie en entier et se repasse après un délai. Les examens blancs de l'app
«&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent le format officiel de chaque déclinaison, avec
la notation du vrai test et la correction IA de l'écrit et de l'oral.""",
    sources="""<strong>Sources.</strong> <a href="{fei}" rel="noopener">Liste des centres d'examen de France Éducation
international</a> (TCF, DELF-DALF), lue pays par pays le {date}, et liste des centres d'examen civique lue le {date_civ} ;
<a href="{cci}" rel="noopener">carte des centres TEF du Français des affaires</a> (CCI Paris Île-de-France), lue le {date}.
Coordonnées telles que publiées, adresses e-mail génériques seulement. Noms de lieux et coordonnées des villes :
{geonames}. Les distances sont calculées à vol d'oiseau depuis le centre de la ville.""",
)

TEXT["en"] = dict(
    path="/en/test-centre-near-me/", crumb="Test centre near me", home=("Home", "/en/"),
    title="TCF & DELF Test Centre Near Me: Search by City",
    desc="Find the nearest approved TCF, DELF-DALF or TEF test centre: {n} centres in {p} countries and territories, with distance, address and phone.",
    h1="Find a TCF, DELF or TEF test centre near you",
    intro="""Type your city, your country or a centre’s name — or tap “Near me” — to see the nearest approved test
centres, with the distance, address, phone number and website: <strong>{n} TCF, DELF-DALF, TEF and French civics test
centres in {p} countries and territories</strong>, from the official lists read on {date}.""",
    facts=["<strong>{n} approved centres</strong> in {p} countries and territories: {tcf} TCF centres, {delf} DELF-DALF centres, {tef} TEF centres and {civ} French civics test centres in France.",
           "Official lists read on {date} — France Éducation international for the TCF and DELF-DALF, CCI Paris Île-de-France for the TEF; civics test: FEI list of {date_civ}.",
           "The search runs in your browser: neither your position nor what you type is sent to any third party."],
    tool_h2="Search for a test centre", label="City, country or centre name", ph="Toronto, Dubai, London…", go="Search",
    legend="Exam", all="All", ex={"tcf": "TCF", "delf": "DELF-DALF", "civique": "Civics test (France)", "tef": "TEF"},
    near="Near me", privacy="Your position is only used to compute distances in this page: it never leaves your browser.",
    note="""<strong>TCF:</strong> France Éducation international’s list doesn’t say whether a centre runs the TCF Canada,
the TCF IRN or the TCF Québec — check the centre’s website; <a href="/en/">our country and city guides</a> checked it for
the main centres, and <a href="/en/tcf-canada-test-centres/">all of Canada’s centres</a>. <strong>TEF:</strong> the CCI map
shows sessions open on the day we read it, not which tests a centre is approved for. This page calls no third-party
service — no map, no font, no analytics. Place names: {geonames}.""",
    noscript="The search needs JavaScript; the full list of countries and cities is further down.",
    sections=[
        ("choose", "TCF Canada, TCF IRN, DELF or TEF: which one?", """<ul class="decision">
<li><b><a href="/en/tcf-canada/">TCF Canada</a> — Canadian immigration</b><span>Accepted by IRCC, like the TEF Canada; results are valid for two years. Use the “TCF” filter, then check on the centre’s website that it offers the Canada version.</span></li>
<li><b><a href="/en/tcf-quebec/">TCF Québec</a> — immigration to Quebec</b><span>Tests of your choice; same TCF centres, same check to make.</span></li>
<li><b><a href="/en/tcf-irn/">TCF IRN</a> — French citizenship, resident card</b><span>The test for French procedures: B2 is required for citizenship since 2026, B1 for the resident card.</span></li>
<li><b><a href="/en/delf-b2/">DELF</a> and <a href="/en/dalf-c1/">DALF</a> — a diploma</b><span>Diplomas valid for life, taken level by level; adults take the DELF tout public. Use the “DELF-DALF” filter.</span></li>
<li><b><a href="/en/tef-canada/">TEF Canada, TEF IRN</a> — the other family of tests</b><span>Run by the Le français des affaires network (CCI Paris Île-de-France): use the “TEF” filter. <a href="/en/tcf-vs-tef-canada/">TCF vs TEF Canada</a>.</span></li>
<li><b><a href="/en/french-civics-test/">French civics test</a> — residence permits, citizenship</b><span>Required since 2026 alongside the French test; the “Civics test” filter shows the centres approved by FEI in France.</span></li>
</ul>"""),
        ("official-list", "What the official list doesn’t tell you", """<p>The official lists say that a centre is
<strong>approved</strong>. They don’t say which version of the TCF it runs (Canada, Québec, IRN), nor its
<strong>dates</strong> or <strong>fees</strong>: there is no national fee, and two centres in the same city can have
unrelated sessions and prices. For the TEF, the CCI map shows the sessions open on the day it was read, not the tests a
centre is approved for. What we checked centre by centre is in <a href="/en/">our country and city guides</a>,
<a href="/en/tcf-canada-test-centres/">the TCF Canada centres in Canada</a> and <a href="/en/tcf-canada-test-dates-2026/">TCF
Canada test dates</a>. An organisation that is not on these lists is not approved.</p>"""),
    ],
    list_h2="Every country and city",
    list_intro="The {p} countries and territories with at least one centre, and the number of centres in each city ({cities} cities). A linked city has a detailed page on this site.",
    ours="Our guides", official="Official lists",
    faq=[("Is there a TCF Canada test centre near me?", "Type your city or tap “Near me” with the TCF filter: the nearest approved TCF centres appear, with the distance. France Éducation international’s list doesn’t say which ones offer the TCF Canada: check the centre’s website — our country and city guides checked it for the main centres. The TEF Canada, which IRCC also accepts, is taken at the centres under the TEF filter."),
         ("Can adults take the DELF?", "Yes: the DELF tout public is the version for adults. The DELF junior and DELF scolaire are for teenagers — in France, the education authority centres (CASNAV) focus on the DELF scolaire. Ask the centre which version it runs before you register."),
         ("How do I book a test date?", "Directly with the centre, usually online — never with France Éducation international or CCI Paris Île-de-France. Each card gives the centre’s website, phone number and email; for the TEF, the “Contact page (CCI)” link opens the centre’s page on the CCI platform."),
         ("How up to date is this list?", "It reproduces the official lists read on {date} — France Éducation international for the TCF and DELF-DALF, CCI Paris Île-de-France for the TEF — and the list of {date_civ} for the civics test. Centres come and go as approvals change: if in doubt, the official list is the reference."),
         ("Is my location sent anywhere?", "No. “Near me” asks your browser for your position only when you tap the button, and distances are computed in the page: neither your position nor your search leaves your device. The page calls no third-party service.")],
    also=[("/en/", "TCF Canada & DELF test centres by country", "Fees, dates and registration, checked centre by centre."),
          ("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "All approved centres, province by province."),
          ("/en/tcf-vs-tef-canada/", "TCF vs TEF Canada", "The two French tests IRCC accepts, side by side."),
          ("/en/tcf-canada-test-dates-2026/", "TCF Canada test dates", "There is no national calendar: each centre sets its own dates.")],
    cta_h2="The centre gives you the date; the score is up to you",
    cta_p="""You pay the full fee for each session, and you can’t retake the test right away. The mock exams in the
“TCF DELF TEF: Tests 2026” app follow the official format of each test, scored like the real thing, with AI feedback
on writing and speaking.""",
    sources="""<strong>Sources.</strong> <a href="{fei}" rel="noopener">France Éducation international’s list of exam
centres</a> (TCF, DELF-DALF), read country by country on {date}, and its list of civics test centres read on {date_civ};
<a href="{cci}" rel="noopener">map of TEF centres of Le français des affaires</a> (CCI Paris Île-de-France), read on
{date}. Contact details as published, generic email addresses only. Place names and city coordinates: {geonames}.
Distances are straight-line distances from the city centre.""",
)

TEXT["es"] = dict(
    path="/es/centro-de-examen-cerca-de-mi/", crumb="Centro cerca de mí", home=("Inicio", "/es/"),
    title="Centro de examen DELF y TCF cerca de mí: buscador",
    desc="El centro de examen DELF, TCF o TEF más cercano: {n} centros autorizados en {p} países y territorios, con distancia, dirección y teléfono.",
    h1="Encuentra un centro de examen DELF, TCF o TEF cerca de ti",
    intro="""Escribe tu ciudad, tu país o el nombre de un centro —o toca «Cerca de mí»— para ver los centros de examen
autorizados más cercanos, con la distancia, la dirección, el teléfono y el sitio web: <strong>{n} centros de TCF,
DELF-DALF, TEF y examen cívico en {p} países y territorios</strong>, según las listas oficiales consultadas el {date}.""",
    facts=["<strong>{n} centros autorizados</strong> en {p} países y territorios: {tcf} centros de TCF, {delf} de DELF-DALF, {tef} de TEF y {civ} centros de examen cívico en Francia.",
           "Listas oficiales consultadas el {date}: France Éducation international para el TCF y el DELF-DALF, la CCI Paris Île-de-France para el TEF; examen cívico: lista de FEI del {date_civ}.",
           "La búsqueda se hace en tu navegador: ni tu ubicación ni lo que escribes se envían a un servicio externo."],
    tool_h2="Buscar un centro", label="Ciudad, país o nombre del centro", ph="Sevilla, Bogotá, Madrid…", go="Buscar",
    legend="Examen", all="Todos", ex={"tcf": "TCF", "delf": "DELF-DALF", "civique": "Examen cívico (Francia)", "tef": "TEF"},
    near="Cerca de mí", privacy="Tu ubicación solo sirve para calcular distancias en esta página: no sale de tu navegador.",
    note="""<strong>TCF:</strong> la lista de France Éducation international no dice si un centro organiza el TCF Canada,
el TCF IRN o el TCF Québec: compruébalo en su web; <a href="/es/">nuestras guías por país y ciudad</a> lo revisaron para
los centros principales. <strong>TEF:</strong> el mapa de la CCI muestra las sesiones abiertas el día de la consulta, no
las pruebas autorizadas. Esta página no llama a ningún servicio externo: ni mapas, ni fuentes, ni estadísticas. Nombres
de lugares: {geonames}.""",
    noscript="La búsqueda necesita JavaScript; la lista completa de países y ciudades está más abajo.",
    sections=[
        ("elegir", "TCF Canada, TCF IRN, DELF o TEF: ¿cuál buscar?", """<ul class="decision">
<li><b><a href="/es/tcf-canada/">TCF Canada</a> — inmigración a Canadá</b><span>Aceptado por IRCC, igual que el TEF Canada; el resultado vale dos años. Usa el filtro «TCF» y comprueba en la web del centro que ofrece la versión Canadá.</span></li>
<li><b><a href="/tcf-quebec/" hreflang="fr">TCF Québec</a> (en francés) — inmigración a Quebec</b><span>Pruebas a elección; mismos centros TCF, misma comprobación.</span></li>
<li><b><a href="/tcf-irn/" hreflang="fr">TCF IRN</a> (en francés) — nacionalidad francesa, tarjeta de residente</b><span>El test de los trámites franceses: B2 para la nacionalidad desde 2026, B1 para la tarjeta de residente.</span></li>
<li><b><a href="/es/delf-b2/">DELF</a> y <a href="/es/dalf-c1/">DALF</a> — un diploma</b><span>Diplomas válidos de por vida, nivel por nivel; los adultos hacen el DELF tout public. Usa el filtro «DELF-DALF».</span></li>
<li><b><a href="/es/examen-de-frances-para-canada/">TEF Canada</a> — la otra familia de exámenes</b><span>Los organiza la red de Le français des affaires (CCI Paris Île-de-France): filtro «TEF».</span></li>
<li><b><a href="/blog/ou-passer-l-examen-civique/" hreflang="fr">Examen cívico</a> (en francés) — permisos de residencia, nacionalidad</b><span>Obligatorio desde 2026 junto con el examen de francés; el filtro «Examen cívico» muestra los centros autorizados por FEI en Francia.</span></li>
</ul>
<p>¿Diploma o test? Las diferencias están en <a href="/es/certificado-de-frances/">¿qué certificado de francés?</a>.</p>"""),
        ("lista-oficial", "Lo que la lista oficial no dice", """<p>Las listas oficiales dicen que un centro está
<strong>autorizado</strong>. No dicen qué versión del TCF organiza (Canadá, Quebec, IRN), ni sus <strong>fechas</strong>,
ni sus <strong>precios</strong>: no hay tarifa nacional, y dos centros de la misma ciudad pueden tener sesiones y precios
sin relación. Para el TEF, el mapa de la CCI muestra las sesiones abiertas el día de la consulta, no las pruebas
autorizadas. Lo que revisamos centro por centro está en <a href="/es/">nuestras guías por país y ciudad</a> y en las
<a href="/es/fechas-delf-2027/">fechas del DELF</a>. Un organismo que no figura en estas listas no está autorizado.</p>"""),
    ],
    list_h2="Todos los países y ciudades",
    list_intro="Los {p} países y territorios con al menos un centro, y el número de centros por ciudad ({cities} ciudades). Una ciudad con enlace tiene su página detallada en este sitio.",
    ours="Nuestras guías", official="Listas oficiales",
    faq=[("¿Hay un centro de TCF Canada cerca de mí?", "Escribe tu ciudad o toca «Cerca de mí» con el filtro TCF: aparecen los centros TCF autorizados más cercanos, con la distancia. La lista de France Éducation international no dice cuáles ofrecen el TCF Canada: compruébalo en la web del centro; nuestras guías por país y ciudad lo revisaron para los centros principales. El TEF Canada, que IRCC también acepta, se hace en los centros del filtro TEF."),
         ("¿Un adulto puede hacer el DELF?", "Sí: el DELF tout public es la versión para adultos. El DELF junior y el DELF scolaire son para adolescentes; en Francia, los centros de la administración educativa (CASNAV) se orientan al DELF scolaire. Pregunta al centro qué versión organiza antes de inscribirte."),
         ("¿Cómo reservo una fecha?", "Directamente con el centro, casi siempre en línea; nunca con France Éducation international ni con la CCI Paris Île-de-France. Cada ficha da la web, el teléfono y el correo del centro; para el TEF, el enlace «Contacto (CCI)» abre la página del centro en la plataforma de la CCI."),
         ("¿Esta lista está al día?", "Reproduce las listas oficiales consultadas el {date} —France Éducation international para el TCF y el DELF-DALF, la CCI Paris Île-de-France para el TEF— y la del {date_civ} para el examen cívico. Los centros cambian a lo largo del año: en caso de duda, vale la lista oficial."),
         ("¿Se envía mi ubicación a algún sitio?", "No. «Cerca de mí» solo pide tu ubicación al navegador cuando tocas el botón, y las distancias se calculan en la página: ni la ubicación ni la búsqueda salen de tu dispositivo. La página no llama a ningún servicio externo.")],
    also=[("/es/", "Centros de examen DELF y TCF por país", "Precios, fechas e inscripción, revisados centro por centro."),
          ("/es/certificado-de-frances/", "¿Qué certificado de francés?", "DELF, DALF, TCF o TEF: para qué sirve cada uno."),
          ("/es/examen-de-frances-para-canada/", "¿TCF o TEF Canada?", "Los dos exámenes de francés que acepta IRCC."),
          ("/es/fechas-delf-2027/", "Fechas del DELF 2027", "El calendario nacional y las convocatorias.")],
    cta_h2="El centro te da la fecha; el nivel depende de ti",
    cta_p="""Cada sesión se paga completa y no se puede repetir de inmediato. Los simulacros de la app «TCF DELF TEF:
Tests 2026» reproducen el formato oficial de cada examen, con la puntuación del examen real y corrección con IA de la
expresión escrita y oral.""",
    sources="""<strong>Fuentes.</strong> <a href="{fei}" rel="noopener">Lista de centros de examen de France Éducation
international</a> (TCF, DELF-DALF), consultada país por país el {date}, y lista de centros de examen cívico consultada el
{date_civ}; <a href="{cci}" rel="noopener">mapa de centros TEF de Le français des affaires</a> (CCI Paris Île-de-France),
consultado el {date}. Datos de contacto tal como se publican, solo correos genéricos. Nombres de lugares y coordenadas de
las ciudades: {geonames}. Las distancias son en línea recta desde el centro de la ciudad.""",
)

TEXT["ar"] = dict(
    path="/ar/test-centre-near-me/", crumb="مركز قريب منك", home=("الرئيسية", "/ar/"),
    title="مركز امتحان TCF أو DELF قريب منك: ابحث باسم مدينتك",
    desc="أقرب مركز امتحان TCF أو DELF-DALF أو TEF إليك: {n} مركزًا معتمدًا في {p} بلدًا وإقليمًا، مع المسافة والعنوان والهاتف، ويعمل بخيار «بالقرب مني».",
    h1="ابحث عن مركز امتحان TCF أو DELF أو TEF قريب منك",
    intro="""اكتب اسم مدينتك أو بلدك أو اسم مركز، أو اضغط «بالقرب مني»، لترى أقرب مراكز الامتحان المعتمدة مع المسافة
والعنوان ورقم الهاتف والموقع الإلكتروني: <strong>{n} مركزًا لامتحانات TCF وDELF-DALF وTEF والامتحان المدني في {p} بلدًا وإقليمًا</strong>،
بحسب القوائم الرسمية التي اطّلعنا عليها في {date}.""",
    facts=["<strong>{n} مركزًا معتمدًا</strong> في {p} بلدًا وإقليمًا: {tcf} مركزًا لامتحان TCF، و{delf} مركزًا لـ DELF-DALF، و{tef} مركزًا لامتحان TEF، و{civ} مركزًا للامتحان المدني في فرنسا.",
           "قوائم رسمية اطّلعنا عليها في {date}: قائمة <bdi>France Éducation international</bdi> لامتحانَي TCF وDELF-DALF، وقائمة <bdi>CCI Paris Île-de-France</bdi> لامتحان TEF؛ أما الامتحان المدني فقائمة FEI بتاريخ {date_civ}.",
           "يجري البحث داخل متصفحك: لا يُرسَل موقعك ولا ما تكتبه إلى أي جهة خارجية."],
    tool_h2="ابحث عن مركز", label="المدينة أو البلد أو اسم المركز", ph="الجزائر، دبي، القاهرة…", go="ابحث",
    legend="الامتحان", all="الكل", ex={"tcf": "TCF", "delf": "DELF-DALF", "civique": "الامتحان المدني (فرنسا)", "tef": "TEF"},
    near="بالقرب مني", privacy="يُستخدم موقعك لحساب المسافات داخل هذه الصفحة فقط، ولا يغادر متصفحك.",
    note="""<strong>TCF:</strong> لا تذكر قائمة <bdi>France Éducation international</bdi> إن كان المركز ينظّم TCF Canada أو
TCF IRN أو TCF Québec، فتحقّق من ذلك على موقعه؛ وقد راجعت <a href="/ar/#centres">صفحاتنا عن الخليج والمشرق</a> ذلك لأهم
المراكز. <strong>TEF:</strong> تعرض خريطة CCI الجلسات المفتوحة يوم اطّلاعنا عليها، لا الامتحانات المعتمدة لكل مركز. لا تستدعي
هذه الصفحة أي خدمة خارجية: لا خرائط ولا خطوط ولا إحصاءات. أسماء الأماكن: {geonames}.""",
    noscript="يحتاج البحث إلى JavaScript؛ القائمة الكاملة للبلدان والمدن في أسفل الصفحة.",
    sections=[
        ("choose", "TCF Canada أم TCF IRN أم DELF أم TEF؟", """<ul class="decision">
<li><b><a href="/ar/tcf-canada/">TCF كندا</a> — الهجرة إلى كندا</b><span>تقبله IRCC مثل TEF Canada، وتبقى نتيجته صالحة سنتين. اختر عامل التصفية «TCF» ثم تحقّق على موقع المركز من أنه ينظّم نسخة كندا.</span></li>
<li><b><a href="/en/tcf-quebec/" hreflang="en" lang="en" dir="ltr">TCF Québec</a> (بالإنجليزية) — الهجرة إلى كيبيك</b><span>اختبارات تختارها بنفسك، في مراكز TCF نفسها، مع التحقّق نفسه.</span></li>
<li><b><a href="/en/tcf-irn/" hreflang="en" lang="en" dir="ltr">TCF IRN</a> (بالإنجليزية) — الجنسية الفرنسية وبطاقة الإقامة</b><span>اختبار الإجراءات الفرنسية: المستوى B2 مطلوب للجنسية منذ 2026، وB1 لبطاقة المقيم.</span></li>
<li><b><a href="/en/delf-b2/" hreflang="en" lang="en" dir="ltr">DELF</a> (بالإنجليزية) — شهادة دبلوم</b><span>شهادات صالحة مدى الحياة تُجتاز مستوى بعد مستوى، والكبار يجتازون DELF tout public. اختر «DELF-DALF».</span></li>
<li><b><a href="/ar/tcf-or-tef-canada/">TCF أم TEF كندا؟</a> — العائلة الأخرى من الاختبارات</b><span>تنظّم امتحانات TEF شبكة <bdi>Le français des affaires</bdi> التابعة لـ <bdi>CCI Paris Île-de-France</bdi>: اختر «TEF».</span></li>
<li><b><a href="/en/french-civics-test/" hreflang="en" lang="en" dir="ltr">French civics test</a> (بالإنجليزية) — الإقامة والجنسية في فرنسا</b><span>إلزامي منذ 2026 إلى جانب اختبار الفرنسية؛ يعرض عامل التصفية «الامتحان المدني» المراكز التي اعتمدتها FEI في فرنسا.</span></li>
</ul>"""),
        ("official-list", "ما لا تقوله القائمة الرسمية", """<p>تقول القوائم الرسمية إن المركز <strong>معتمد</strong>، لكنها لا
تذكر أي نسخة من TCF ينظّم (كندا أو كيبيك أو IRN)، ولا <strong>مواعيده</strong>، ولا <strong>أسعاره</strong>: لا توجد تعرفة
وطنية، وقد تختلف جلسات مركزين في المدينة نفسها وأسعارهما تمامًا. أما في TEF فتعرض خريطة CCI الجلسات المفتوحة يوم الاطّلاع
عليها، لا الامتحانات المعتمدة. ما راجعناه مركزًا مركزًا موجود في <a href="/ar/tcf-canada-price/">أسعار TCF Canada بلدًا بلدًا</a>
و<a href="/ar/#centres">صفحاتنا عن مراكز الخليج والمشرق</a>. الجهة غير المدرجة في هذه القوائم ليست معتمدة.</p>"""),
    ],
    list_h2="جميع البلدان والمدن",
    list_intro="البلدان والأقاليم التي يوجد فيها مركز واحد على الأقل، وعددها {p}، مع عدد المراكز في كل مدينة (عدد المدن: {cities}). المدينة التي تحمل رابطًا لها صفحة مفصّلة على هذا الموقع.",
    ours="أدلّتنا", official="القوائم الرسمية",
    faq=[("هل يوجد مركز TCF Canada قريب مني؟", "اكتب اسم مدينتك أو اضغط «بالقرب مني» مع عامل التصفية TCF: تظهر أقرب مراكز TCF المعتمدة مع المسافة. لا تذكر قائمة France Éducation international أيها ينظّم TCF Canada، فتحقّق من ذلك على موقع المركز؛ وقد راجعت أدلّتنا ذلك لأهم المراكز. أما TEF Canada، الذي تقبله IRCC أيضًا، فيُجتاز في مراكز عامل التصفية TEF."),
         ("هل يمكن للكبار اجتياز DELF؟", "نعم: DELF tout public هو النسخة المخصّصة للكبار، أما DELF junior وDELF scolaire فللمراهقين؛ وفي فرنسا تتجه مراكز الإدارة التعليمية (CASNAV) إلى DELF scolaire. اسأل المركز عن النسخة التي ينظّمها قبل التسجيل."),
         ("كيف أحجز موعدًا؟", "مباشرة لدى المركز، وغالبًا عبر الإنترنت، وليس لدى France Éducation international ولا لدى CCI Paris Île-de-France. تعرض كل بطاقة موقع المركز وهاتفه وبريده الإلكتروني؛ وفي TEF يفتح رابط «صفحة الاتصال (CCI)» صفحة المركز على منصة CCI."),
         ("هل هذه القائمة محدّثة؟", "تنقل القوائم الرسمية التي اطّلعنا عليها في {date}، أي قائمة France Éducation international لامتحانَي TCF وDELF-DALF وقائمة CCI Paris Île-de-France لامتحان TEF، وقائمة {date_civ} للامتحان المدني. تتغيّر المراكز مع تغيّر الاعتمادات، وعند الشك فالمرجع هو القائمة الرسمية."),
         ("هل يُرسَل موقعي إلى أي جهة؟", "لا. لا يطلب «بالقرب مني» موقعك من المتصفح إلا عند الضغط على الزر، وتُحسب المسافات داخل الصفحة: لا يغادر موقعك ولا بحثك جهازك، ولا تستدعي الصفحة أي خدمة خارجية.")],
    also=[("/ar/", "الصفحة الرئيسية بالعربية", "دليل TCF Canada والمراكز والأسعار."),
          ("/ar/tcf-canada-price/", "سعر امتحان TCF Canada", "الرسوم بلدًا بلدًا وطريقة الحجز."),
          ("/ar/tcf-or-tef-canada/", "TCF أم TEF كندا؟", "الاختباران اللذان تقبلهما IRCC."),
          ("/ar/tcf-canada/", "امتحان TCF كندا", "الأقسام والدرجات ومستويات NCLC.")],
    cta_h2="المركز يحدّد لك الموعد، والدرجة تعتمد عليك",
    cta_p="""تدفع رسوم كل جلسة كاملةً، ولا يمكنك إعادة الامتحان فورًا. الامتحانات التجريبية في تطبيق
«<bdi>TCF DELF TEF: Tests 2026</bdi>» تتبع الصيغة الرسمية لكل امتحان وتُصحَّح كالامتحان الحقيقي، مع ملاحظات بالذكاء
الاصطناعي على التعبير الكتابي والشفهي.""",
    sources="""<strong>المصادر.</strong> <a href="{fei}" rel="noopener">قائمة مراكز الامتحان لدى <bdi>France Éducation
international</bdi></a> (TCF وDELF-DALF)، اطّلعنا عليها بلدًا بلدًا في {date}، وقائمة مراكز الامتحان المدني في {date_civ}؛
و<a href="{cci}" rel="noopener">خريطة مراكز TEF لدى <bdi>Le français des affaires</bdi></a> (<bdi>CCI Paris Île-de-France</bdi>)
في {date}. بيانات الاتصال كما نُشرت، والعناوين البريدية العامة فقط. أسماء الأماكن وإحداثيات المدن: {geonames}. المسافات
خطوط مستقيمة من وسط المدينة.""",
)


# Petit formulaire des hubs (accueil, /centres/, /ou-passer/, /en/, /es/, /ar/…) : un GET vers la page du chercheur,
# qui lance la recherche à l'ouverture (?q=…). Aucun script. Recopié tel quel dans les sources des hubs.
WIDGET = {
    "fr": """<form class="finder-mini" action="/trouver-un-centre/" method="get" role="search">
<label for="finder-mini-q">Trouver un centre d'examen près de chez vous</label>
<div class="finder-row"><input id="finder-mini-q" name="q" type="search" placeholder="Ville, pays ou nom du centre" autocomplete="off" enterkeyhint="search"><button type="submit">Chercher</button></div>
<p>TCF, DELF-DALF, TEF et examen civique : les centres agréés les plus proches, avec la distance. <a href="/trouver-un-centre/">Ou autour de moi →</a></p>
</form>""",
    "en": """<form class="finder-mini" action="/en/test-centre-near-me/" method="get" role="search">
<label for="finder-mini-q">Find a test centre near you</label>
<div class="finder-row"><input id="finder-mini-q" name="q" type="search" placeholder="City, country or centre name" autocomplete="off" enterkeyhint="search"><button type="submit">Search</button></div>
<p>TCF, DELF-DALF and TEF: the nearest approved centres, with the distance. <a href="/en/test-centre-near-me/">Or use your location →</a></p>
</form>""",
    "es": """<form class="finder-mini" action="/es/centro-de-examen-cerca-de-mi/" method="get" role="search">
<label for="finder-mini-q">Encuentra un centro de examen cerca de ti</label>
<div class="finder-row"><input id="finder-mini-q" name="q" type="search" placeholder="Ciudad, país o nombre del centro" autocomplete="off" enterkeyhint="search"><button type="submit">Buscar</button></div>
<p>DELF-DALF, TCF y TEF: los centros autorizados más cercanos, con la distancia. <a href="/es/centro-de-examen-cerca-de-mi/">O usa tu ubicación →</a></p>
</form>""",
    "ar": """<form class="finder-mini" action="/ar/test-centre-near-me/" method="get" role="search">
<label for="finder-mini-q">ابحث عن مركز امتحان قريب منك</label>
<div class="finder-row"><input id="finder-mini-q" name="q" type="search" placeholder="المدينة أو البلد أو اسم المركز" autocomplete="off" enterkeyhint="search"><button type="submit">ابحث</button></div>
<p>TCF وDELF-DALF وTEF: أقرب المراكز المعتمدة مع المسافة. <a href="/ar/test-centre-near-me/">أو استخدم موقعك ←</a></p>
</form>""",
}
