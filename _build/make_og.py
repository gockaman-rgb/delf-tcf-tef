#!/usr/bin/env python3
"""Génère les images Open Graph 1200x630 du site, au gabarit des visuels existants.

Repris de la charte de img/og/tcf-quebec.png : fond #0E1420, accent #34C47C,
barre supérieure, filet vertical, chiffre-clé en gros à gauche de son libellé.

Usage :
    python3 _build/make_og.py            # ne réécrit que les images manquantes
    python3 _build/make_og.py --force    # régénère tout

Ajouter une image = ajouter une entrée dans PAGES, avec :
    slug, title, stat, label
`stat` peut être None : le bloc chiffre est alors simplement omis.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (14, 20, 32)
ACCENT = (52, 196, 124)
TITLE = (232, 237, 245)
MUTED = (154, 168, 189)

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "img", "og")

# slug, titre, chiffre-clé, libellé du chiffre
PAGES = [
    ("home", "DELF · TCF · TEF", "15", "examens couverts · correction IA"),
    ("tcf-canada", "TCF Canada", "458", "en compréhension orale pour NCLC 7"),
    ("tef-canada", "TEF Canada · TEFAQ", "2 h 55", "4 épreuves · conversion NCLC"),
    ("delf-b2", "DELF B2", "50", "sur 100 pour être admis"),
    ("delf-b1", "DELF B1", "B1", "exigé pour la carte de résident"),
    ("dalf", "DALF C1 · C2", "200", "mots : la synthèse du C1"),
    ("examens-blancs", "Examens blancs", "11", "formats officiels chronométrés"),
    ("tcf-irn", "TCF IRN", "499", "l'échelle du test de naturalisation"),
    ("plan-etude", "Plan d'étude", None, "Un coach calé sur votre date d'examen"),
    # articles du blog
    ("b1-ou-b2-nationalite-francaise", "B1 ou B2 ?", "B2", "pour la nationalité française"),
    ("tcf-irn-ou-tef-irn", "TCF IRN ou TEF IRN", "499", "la même échelle pour les deux"),
    ("prix-tcf-tef", "Prix du TCF Canada", "17", "pays · prix relevés et datés"),
    ("logiciel-tcf", "Logiciel TCF", "680", "questions gratuites, et l'app d'examens blancs"),
    ("ifal-tcf-rendez-vous", "IFAL : rendez-vous TCF", "37 500 DA", "le TCF Canada · 5 antennes, plateforme VFS"),
    ("en-delf-exam-dates-2027", "DELF exam dates 2027 · France and by country", "10", "sessions in France · Korea, Japan, India…"),
    ("es-fechas-delf-2027", "Fechas DELF 2027", "10", "convocatorias al año en Francia · España aparte"),
    ("en-tcf-canada-practice-app", "TCF Canada practice app", "15", "exam variants in the official format"),
    ("en-tcf-canada-new-delhi", "TCF Canada · New Delhi", "₹26,000", "Alliance Française de Delhi"),
    ("en-tcf-canada-kolkata", "TCF Canada · Kolkata", "₹26,000", "Alliance Française du Bengale"),
    ("en-tcf-canada-ahmedabad", "TCF Canada · Ahmedabad", "15", "working days for the certificate"),
    ("en-tcf-canada-bangalore", "TCF Canada · Bangalore", "20", "days between two attempts"),
    ("en-tcf-canada-bhopal", "TCF Canada · Bhopal", "₹26,000", "paper-based · dates to March 2027"),
    ("en-tcf-canada-new-york", "TCF Canada · New York", "$399", "2027 dates in Montclair, NJ"),
    ("en-tcf-canada-boston", "TCF Canada · Boston", "$350", "Saturday sessions in Cambridge, MA"),
    ("en-tcf-canada-chicago", "TCF Canada · Chicago", "0", "TCF Canada sessions · TEF Canada $415 instead"),
    ("en-tcf-canada-los-angeles", "TCF Canada · Los Angeles", "$505", "monthly dates · Pasadena $460"),
    ("en-tcf-canada-san-diego", "TCF Canada · San Diego", "$450", "sessions sold out · waitlist"),
    ("en-tcf-canada-calgary", "TCF Canada · Calgary", "$400", "14 seats a session · Kahanoff Centre"),
    ("en-tcf-canada-edmonton", "TCF Canada · Edmonton", "$400", "each session on sale for about an hour"),
    ("en-tcf-canada-abu-dhabi", "TCF Canada · Abu Dhabi", "1,800 AED", "20 November and 16 December"),
    ("es-delf-bilbao", "DELF en Bilbao", "192 €", "el B2 en 2027 · Institut français"),
    ("es-delf-malaga", "DELF en Málaga", "192 €", "el B2 en 2027 · también Jaén y Córdoba"),
    ("es-delf-palma", "DELF en Palma", "192 €", "el B2 en 2027 · Alianza Francesa"),
    ("es-delf-las-palmas", "DELF en Las Palmas", "192 €", "el B2 en 2027 · Alianza Francesa"),
    ("es-delf-zaragoza", "DELF en Zaragoza", "192 €", "el B2 en 2027 · Institut français"),
    ("es-delf-girona", "DELF en Girona", "192 €", "el B2 en 2027 · Alianza Francesa"),
    ("cpf-test-francais", "Le CPF et les tests", "2", "versions du TCF finançables sur 4"),
    ("diplome-ou-test-delf-tcf", "Diplôme ou test ?", "2 ans", "contre à vie : ce qui les sépare"),
    ("repasser-tcf-tef", "Repasser le TCF ou le TEF", "20", "jours — mais la source se contredit"),
    ("validite-attestation-tcf-tef", "Validité : 2 ans", "2 ans", "oui, mais à partir de quand ?"),
    ("production-ecrite-delf-b2", "Production écrite B2", "250", "mots minimum, en 60 minutes"),
    ("synthese-dalf-c1", "La synthèse du C1", "200", "à 240 mots, sans aucune citation"),
    ("tefaq-oral-quebec", "TEFAQ", "1→4", "épreuves au choix · Échelle québécoise"),
    # cluster « exercices »
    ("exercices-comprehension-orale-tcf-canada", "Compréhension orale", "39", "questions en 35 min · 1 seule écoute"),
    ("exercices-comprehension-ecrite-tcf-canada", "Compréhension écrite", "39", "questions en 60 min · navigation libre"),
    ("sujets-expression-ecrite-tcf-canada", "Expression écrite", "3", "tâches · de 60 à 180 mots"),
    ("sujets-expression-orale-tcf-canada", "Expression orale", "12", "minutes pour 3 tâches"),
    ("exercices-tcf-irn", "Exercices TCF IRN", "499", "l'échelle du test de naturalisation"),
    ("exercices-tef-canada", "Exercices TEF Canada", "A+B", "deux sections par expression"),
    ("exercices-delf-b2", "Exercices DELF B2", "5", "sur 25 : la note éliminatoire"),
    ("exercices-structures-langue-tcf", "Structures de la langue", "18", "QCM en 15 min · TCF Tout Public"),
    ("questions", "Toutes vos questions", "217", "réponses sourcées et datées"),
    ("blog", "Le blog", None, "DELF · TCF · TEF — guides sourcés 2026"),
    ("a-propos", "À propos", None, "Méthode éditoriale et sources"),
    ("support", "Support", None, "Contact et questions fréquentes"),
    ("confidentialite", "Confidentialité", None, "Aucun compte, aucun serveur de profil"),
    # visuels d'origine (juillet), repris pour tenir dans le recadrage carré
    ("difference-tcf-tef", "TCF ou TEF ?", "9", "versions comparées, épreuve par épreuve"),
    ("tcf-canada-nclc-7", "NCLC 7 au TCF Canada", "458", "en compréhension orale"),
    ("tcf-ou-tef-canada", "TCF ou TEF Canada", "2", "seuls tests acceptés par IRCC"),
    ("examen-blanc-tcf-gratuit", "Examen blanc gratuit", "2", "ressources officielles, et leurs limites"),
    ("naturalisation-2026-niveau-b2", "Naturalisation 2026", "B2", "obligatoire depuis le 1er janvier"),
    ("carte-de-resident-b1-2026", "Carte de résident", "B1", "exigé depuis janvier 2026"),
    ("tcf-quebec", "TCF Québec", "1→4", "épreuves au choix · Échelle québécoise"),
    ("score-tcf-699", "Le score TCF", "699", "l'échelle officielle expliquée"),
    ("examens", "Les examens couverts", "15", "variantes, du DELF A1 au DALF C2"),
    ("contenu", "Le contenu de l'app", "20 000+", "questions et exercices originaux"),
    ("correction-ia", "La correction IA", "20", "vos productions notées sur 20"),
    # série « Où passer » (17/09/2026)
    ("ou-passer", "Où passer l'examen ?", "144", "centres DELF et 247 centres TCF en France"),
    ("ou-passer-le-delf-en-france", "Où passer le DELF ?", "10", "sessions par an · 144 centres en France"),
    ("ou-passer-le-tcf-irn-en-france", "Où passer le TCF IRN ?", "140-220 €", "selon le centre, pour le même test"),
    ("ou-passer-le-tcf-canada-en-france", "TCF Canada en France", "195-285 €", "les centres qui le proposent, et leurs dates"),
    ("ou-passer-le-tcf-canada-au-canada", "TCF Canada au Canada", "48", "centres agréés, de Montréal à Iqaluit"),
    ("tcf-canada-algerie", "TCF Canada en Algérie", "37 500 DA", "5 antennes de l'Institut français · IFAL"),
    ("tcf-canada-maroc", "TCF Canada au Maroc", "2 900 Dhs", "dans les 16 centres agréés"),
    ("tcf-canada-tunisie", "TCF Canada en Tunisie", "880 DT", "à l'Institut français · résultats en 5 semaines"),
    ("ou-passer-l-examen-civique", "Où passer l'examen civique ?", "244", "centres FEI en France, et le réseau CCIP"),
    # annuaire des centres (19/09/2026)
    ("centres", "L'annuaire des centres", "1 265", "centres agréés · 46 pays · contacts"),
    ("centres-tcf-france", "Centres TCF en France", "247", "centres agréés, région par région"),
    ("centres-delf-france", "Centres DELF-DALF en France", "143", "centres d'examen, région par région"),
    ("centres-examen-civique-france", "Centres d'examen civique", "245", "centres FEI en France"),
    ("centres-tcf-canada", "Centres TCF au Canada", "48", "centres agréés, par province"),
    ("centres-tcf-algerie", "Centres TCF en Algérie", "5", "antennes de l'Institut français"),
    ("centres-tcf-maroc", "Centres TCF au Maroc", "16", "centres agréés, avec contacts"),
    ("centres-tcf-tunisie", "Centres TCF en Tunisie", "14", "centres agréés, avec contacts"),
    ("centres-tcf-afrique", "Centres TCF en Afrique", "23", "centres dans 12 pays"),
    ("centres-tcf-europe", "Centres TCF en Europe", "26", "Espagne · Suisse · Belgique · Royaume-Uni"),
    ("centres-tcf-ameriques", "Centres TCF aux Amériques", "62", "centres agréés dans 9 pays"),
    ("centres-tcf-moyen-orient", "Centres TCF au Moyen-Orient", "17", "Liban · Émirats · Égypte · Turquie"),
    ("centres-tcf-inde", "Centres TCF en Inde", "7", "Alliances françaises agréées"),
    # pages pays (make_pays.py, 08/10/2026)
    ("centres-tcf-etats-unis", "TCF Canada aux États-Unis", "9", "centres le proposent · 330 à 460 $"),
    ("centres-delf-etats-unis", "DELF aux États-Unis", "40", "centres d'examen · B2 190 $"),
    ("centres-tcf-royaume-uni", "TCF Canada au Royaume-Uni", "£260", "à Londres · £325 à Glasgow"),
    ("centres-delf-royaume-uni", "DELF au Royaume-Uni", "11", "centres d'examen · B2 £160"),
    ("centres-tcf-espagne", "TCF Canada en Espagne", "11", "centres le proposent · 275 à 287 €"),
    ("centres-delf-espagne", "DELF en Espagne", "192 €", "le B2 en 2027 · même prix partout"),
    ("centres-tcf-mexique", "TCF Canada au Mexique", "5", "centres · 4 800 à 6 500 pesos"),
    ("centres-delf-mexique", "DELF au Mexique", "71", "centres · calendrier national"),
    ("centres-tcf-colombie", "TCF Canada en Colombie", "7", "Alliances françaises, toutes le proposent"),
    ("centres-delf-colombie", "DELF en Colombie", "15", "Alliances · B2 490 000 pesos"),
    ("centres-tcf-argentine", "TCF Canada en Argentine", "4", "centres l'annoncent · prix sur demande"),
    ("centres-delf-argentine", "DELF en Argentine", "28", "Alliances · session des 4 et 5 décembre"),
    ("centres-tcf-chili", "TCF Canada au Chili", "299 000", "pesos · Santiago et Concepción"),
    ("centres-delf-chili", "DELF au Chili", "4", "centres · calendrier national 2026"),
    ("centres-tcf-perou", "TCF Canada au Pérou", "1", "seul centre : l'Alliance française de Lima"),
    ("centres-delf-perou", "DELF au Pérou", "6", "Alliances · B2 461 soles"),
    ("centres-tcf-equateur", "TCF Canada en Équateur", "200 $", "à Cuenca · 300 $ à Guayaquil"),
    ("centres-delf-equateur", "DELF en Équateur", "5", "Alliances · B2 200 $"),
    # pages en espagnol et en anglais (make_pays.py, 08/10/2026)
    ("es-hub", "TCF Canada y DELF en español", "7", "países · centros, precios y fechas"),
    ("es-tcf-canada-espana", "TCF Canada en España", "11", "centros lo ofrecen · de 275 a 287 €"),
    ("es-delf-espana", "DELF en España", "192 €", "el B2 en 2027 · mismo precio en todo el país"),
    ("es-tcf-canada-mexico", "TCF Canada en México", "5", "centros · de 4,800 a 6,500 pesos"),
    ("es-delf-mexico", "DELF en México", "71", "centros · calendario nacional"),
    ("es-tcf-canada-colombia", "TCF Canada en Colombia", "7", "Alianzas Francesas, todas lo ofrecen"),
    ("es-delf-colombia", "DELF en Colombia", "15", "Alianzas · B2 490.000 pesos"),
    ("es-tcf-canada-argentina", "TCF Canada en Argentina", "4", "centros lo anuncian · precio a solicitud"),
    ("es-delf-argentina", "DELF en Argentina", "28", "Alianzas · sesión del 4 y 5 de diciembre"),
    ("es-tcf-canada-chile", "TCF Canada en Chile", "299.000", "pesos · Santiago y Concepción"),
    ("es-delf-chile", "DELF en Chile", "4", "centros · calendario nacional 2026"),
    ("es-tcf-canada-peru", "TCF Canada en Perú", "1", "único centro: la Alianza Francesa de Lima"),
    ("es-delf-peru", "DELF en Perú", "6", "Alianzas · B2 461 soles"),
    ("es-tcf-canada-ecuador", "TCF Canada en Ecuador", "USD 200", "en Cuenca · USD 300 en Guayaquil"),
    ("es-delf-ecuador", "DELF en Ecuador", "5", "Alianzas · B2 USD 200"),
    ("en-hub", "TCF Canada & DELF test centres", "48", "centres in Canada · plus the US and the UK"),
    ("en-tcf-canada-usa", "TCF Canada in the USA", "9", "centers offer it · $330 to $460"),
    ("en-delf-usa", "DELF in the USA", "40", "test centers · B2 $190"),
    ("en-tcf-canada-uk", "TCF Canada in the UK", "£260", "in London · £325 in Glasgow"),
    ("en-delf-uk", "DELF in the UK", "11", "test centres · B2 £160"),
    ("en-tcf-canada-test-centres", "TCF Canada test centres", "48", "approved centres across Canada"),
    ("en-tcf-canada-toronto", "TCF Canada in Toronto", "5", "approved centres · quarterly sessions"),
    ("en-tcf-canada-montreal", "TCF Canada in Montreal", "7", "approved centres · all computer-based"),
    ("en-tcf-canada-vancouver", "TCF Canada in Vancouver", "$390", "at the Alliance française · 3 centres"),
    ("en-tcf-canada-ottawa", "TCF Canada in Ottawa", "2", "approved centres · passport required"),
    ("en-tcf-canada-quebec-city", "TCF Canada in Quebec City", "2", "Collège Stanislas · Université Laval"),
    # 2e vague (08/10/2026) : préparation TCF Canada en anglais, Inde, Dubaï, DELF en espagnol
    ("en-tcf-canada", "The TCF Canada exam", "CLB 7", "458 listening · 453 reading · 10/20 writing"),
    ("en-tcf-canada-format", "TCF Canada format", "2 h 47", "4 tests: listening, reading, writing, speaking"),
    ("en-tcf-canada-score-clb", "TCF Canada score and CLB", "458", "in listening for CLB 7 · calculator"),
    ("en-tcf-canada-preparation", "Preparing for the TCF Canada", "CLB 7", "the target, test by test"),
    ("en-tcf-canada-fees-registration", "TCF Canada fees", "$390-440", "in Canada · fees in 14 countries"),
    ("en-tcf-canada-clb-7", "TCF Canada CLB 7", "458", "listening · 453 reading · 10/20 writing, speaking"),
    ("en-tcf-vs-tef-canada", "TCF vs TEF Canada", "2", "French tests IRCC accepts, side by side"),
    ("en-tcf-canada-practice-test", "TCF Canada practice test", "Free", "on the official format"),
    ("en-tcf-canada-listening-practice", "TCF Canada listening", "39", "questions in 35 minutes · one listening"),
    ("en-tcf-canada-reading-practice", "TCF Canada reading", "39", "questions in 60 minutes"),
    ("en-tcf-canada-writing-tasks", "TCF Canada writing tasks", "3", "tasks in 60 minutes · 60 to 180 words"),
    ("en-tcf-canada-speaking-topics", "TCF Canada speaking", "3", "tasks in 12 minutes"),
    ("en-tcf-canada-test-dates-2026", "TCF Canada test dates 2026", "0", "national calendar: each centre sets its dates"),
    ("en-tcf-canada-results", "TCF Canada results", "2 years", "validity · no re-marking since Sept 2026"),
    ("en-tcf-canada-india", "TCF Canada in India", "INR 26,000", "5 Alliances Françaises offer it"),
    ("en-tcf-canada-dubai", "TCF Canada in Dubai", "1,800 AED", "Dubai and Abu Dhabi · computer-based"),
    ("es-delf-b2", "Examen DELF B2", "50/100", "para aprobar · mínimo 5/25 por prueba"),
    ("es-delf-b1", "Examen DELF B1", "50/100", "para aprobar · cuatro pruebas"),
    ("es-dalf-c1", "DALF C1", "50/100", "para aprobar · síntesis y ensayo"),
    ("es-delf-b2-ejemplos", "Ejemplos del DELF B2", "B2", "ejercicios corregidos y explicados"),
    ("es-certificado-de-frances", "¿Qué certificado de francés?", "4", "DELF, DALF, TCF o TEF"),
    ("es-delf-madrid", "DELF en Madrid", "2", "centros · B2 192 € en 2027"),
    ("es-delf-barcelona", "DELF en Barcelona", "192 €", "el B2 en 2027 · Institut français"),
    ("es-delf-sevilla", "DELF en Sevilla", "2", "centros · B2 192 € en 2027"),
    ("es-delf-valencia", "DELF en Valencia", "192 €", "el B2 en 2027 · Institut français"),
    ("es-delf-granada", "DELF en Granada", "192 €", "el B2 en 2027 · Centro de Lenguas Modernas"),
    ("en-delf-b2", "DELF B2 exam", "50/100", "to pass · 5/25 minimum per section"),
    ("en-delf-b1", "DELF B1 exam", "50/100", "to pass · four tests"),
    ("en-dalf-c1", "DALF C1 exam", "50/100", "to pass · synthesis and essay"),
    ("en-delf-b2-practice-test", "DELF B2 practice test", "B2", "exercises with answers explained"),
    ("en-french-citizenship-b2", "French citizenship", "B2", "required since 2026 · B1 for the resident card"),
    ("en-tcf-irn", "TCF IRN exam", "B2", "for French citizenship since 2026"),
    ("en-french-civics-test", "French civics test", "32/40", "to pass · 45 minutes"),
    ("en-tef-canada", "TEF Canada exam", "2 h 55", "4 tests · scores converted to CLB"),
    ("en-tef-canada-practice-test", "TEF Canada practice test", "Free", "exercises with answers explained"),
    ("en-tcf-quebec", "TCF Québec vs TCF Canada", "1 to 4", "tests of your choice · modular"),
    ("es-tcf-canada", "Examen TCF Canada", "NCLC 7", "458 oral · 453 escrita · 10/20 expresión"),
    ("es-examen-de-frances-para-canada", "¿TCF o TEF Canada?", "2", "exámenes de francés que acepta IRCC"),
    # dates (19/09/2026)
    ("tcf-canada-dates-2026", "Dates TCF Canada 2026", "0", "calendrier national : les dates sont celles des centres"),
    ("calendrier-delf-dalf-2026-2027", "Calendrier DELF-DALF 2026-2027", "10", "sessions par an, jamais en avril ni en septembre"),
    # Golfe et Levant en anglais (13/10/2026) ; les images arabes sont rendues par og_ar.swift (og_ar.json)
    ("en-tcf-canada-saudi-arabia", "TCF Canada · Saudi Arabia", "1,950", "SAR · Jeddah and Riyadh"),
    ("en-tcf-canada-egypt", "TCF Canada · Egypt", "3", "centres · Cairo and Alexandria"),
    ("en-tcf-canada-lebanon", "TCF Canada · Lebanon", "6", "Institut français centres"),
    ("en-delf-dubai", "DELF · Dubai", "680", "AED for the DELF B2 · 11 Dec 2026"),
    # Jordanie, Qatar, Koweït (26/10/2026, pays_config_en_arab.py)
    ("en-tcf-canada-jordan", "TCF Canada · Jordan", "3", "sessions a year · Amman"),
    ("en-tcf-canada-qatar", "TCF Canada · Qatar", "1,300", "QAR · Doha, computer-based"),
    ("en-tcf-canada-kuwait", "TCF Canada · Kuwait", "130", "KD for the TEF Canada"),
    # DELF exam dates 2027 by country (26/10/2026, i18n_pages_delf_dates.py)
    ("en-delf-exam-dates-2027-south-korea", "DELF dates 2027 · South Korea", "290,000", "won for the DELF B2 · six centres"),
    ("en-delf-exam-dates-2027-japan", "DELF dates 2027 · Japan", "¥24,500", "for the DELF B2 · ten centres"),
    ("en-delf-exam-dates-2027-taiwan", "DELF dates 2027 · Taiwan", "10 Jan", "first 2027 session · B1 and B2 in Taipei"),
    ("en-delf-exam-dates-2027-hong-kong", "DELF dates 2027 · Hong Kong", "HK$2,300", "for the DELF B2 · Junior on 1–8 Dec 2026"),
    ("en-delf-exam-dates-2027-turkey", "DELF dates 2027 · Turkey", "5,850 TL", "for the DELF B2 · five sessions in 2026"),
    ("en-delf-exam-dates-2027-vietnam", "DELF dates 2027 · Vietnam", "14–22 Nov", "2026 session · register by 30 October"),
    ("en-delf-exam-dates-2027-india", "DELF dates 2027 · India", "7–11 Dec", "2026 session · register 9–24 November"),
    ("en-delf-exam-dates-2027-lebanon", "DELF dates 2027 · Lebanon", "24–27 Nov", "2026 session · register by 30 October"),
    ("en-delf-exam-dates-2027-china", "DELF dates 2027 · China", "2,000", "yuan for the DELF B2 · March, June, November"),
    ("en-delf-exam-dates-2027-singapore", "DELF dates 2027 · Singapore", "S$380", "for the DELF B2 · three sessions in 2026"),
    ("en-delf-exam-dates-2027-nigeria", "DELF dates 2027 · Nigeria", "8–11 Dec", "2026 session in Lagos · register by 27 November"),
    ("en-delf-exam-dates-2027-madagascar", "DELF dates 2027 · Madagascar", "24", "Alliances françaises · DELF Prim in April 2027"),
    ("en-delf-exam-dates-2027-thailand", "DELF dates 2027 · Thailand", "3,600", "baht for the DELF B2 · Bangkok"),
    ("en-delf-exam-dates-2027-egypt", "DELF dates 2027 · Egypt", "7–28 Nov", "2026 session · B2 5,265 EGP"),
    # Amérique du Nord (26/10/2026, pays_config_en_na.py)
    ("en-tcf-canada-detroit", "TCF Canada · Detroit", "$330", "full until June 10, 2027"),
    ("en-tcf-canada-houston", "TCF Canada · Houston", "$400", "TCF Canada · TEF Canada $380"),
    ("en-tcf-canada-san-francisco", "TCF Canada · San Francisco", "$460", "full exam only · 1345 Bush Street"),
    ("en-tcf-canada-seattle", "TCF Canada · Seattle", "0", "TCF Canada sessions · TEF Canada $365 instead"),
    ("en-tcf-canada-denver", "TCF Canada · Denver", "2", "centres · Alliance $360, Pluma Academy $435"),
    ("en-tcf-canada-alberta", "TCF Canada · Alberta", "$400", "Calgary and Edmonton · Lethbridge DELF only"),
    ("en-tcf-canada-new-brunswick", "TCF Canada · New Brunswick", "$390", "Moncton, Edmundston, Bathurst · seats open"),
    ("en-tcf-canada-halifax", "TCF Canada · Halifax", "$400", "Alliance Française · 5509 Young Street"),
    ("en-tcf-canada-winnipeg", "TCF Canada · Winnipeg", "$400", "Alliance Française du Manitoba"),
    ("en-tcf-canada-ontario", "TCF Canada · Ontario", "8", "centres · Toronto, North York, Ottawa, Windsor"),
    # chercheur de centres (26/10/2026) ; l'arabe est dans og_ar.json
    ("trouver-un-centre", "Trouver un centre d'examen", "181", "pays · TCF, DELF-DALF, TEF · près de chez vous"),
    ("en-test-centre-near-me", "Test centre near me", "181", "countries · TCF, DELF-DALF, TEF centres"),
    ("es-centro-de-examen-cerca-de-mi", "Centro de examen cerca de mí", "181", "países · centros TCF, DELF-DALF y TEF"),
    # Europe (26/10/2026) : pays_config_eu.py, pays_config_en_eu.py
    ("centres-tcf-allemagne", "TCF Canada en Allemagne", "295 €", "10 centres · Berlin, Hambourg, Munich…"),
    ("centres-delf-allemagne", "DELF en Allemagne", "201 €", "le B2 · 5 sessions en 2027"),
    ("centres-tcf-suisse", "TCF en Suisse", "CHF 290", "le TCF Canada à Montreux · Zurich sur demande"),
    ("centres-delf-suisse", "DELF en Suisse", "20 mars", "première session 2027 · clôture le 8 janvier"),
    ("centres-tcf-belgique", "TCF Canada en Belgique", "268 €", "à Bruxelles · 260 € à Gand"),
    ("centres-tcf-italie", "TCF Canada en Italie", "7", "centres · de 210 à 250 €"),
    ("centres-tcf-pays-bas", "TCF Canada aux Pays-Bas", "290 €", "à Amsterdam · La Haye, Rotterdam"),
    ("centres-tcf-portugal", "TCF Canada au Portugal", "220 €", "Porto et Faro · 211 € à Viseu"),
    ("centres-tcf-roumanie", "TCF Canada en Roumanie", "3", "Instituts français · Bucarest, Cluj, Timișoara"),
    ("centres-tcf-pologne", "TCF Canada en Pologne", "27 nov.", "à Varsovie · inscriptions au 27 octobre"),
    ("centres-tcf-grece", "TCF Canada en Grèce", "19 nov.", "à Athènes · 5 sessions en 2027"),
    ("centres-tcf-irlande", "TCF Canada en Irlande", "270 €", "à Dublin et à Galway"),
    ("en-tcf-canada-germany", "TCF Canada in Germany", "€295", "10 centres · Berlin, Hamburg, Munich…"),
    ("en-delf-germany", "DELF exam dates 2027 · Germany", "€201", "DELF B2 · 5 sessions in 2027"),
    ("en-tcf-canada-switzerland", "TCF in Switzerland", "CHF 290", "TCF Canada in Montreux · Zurich on request"),
    ("en-delf-switzerland", "DELF exam dates 2027 · Switzerland", "20 Mar", "first 2027 session · deadline 8 January"),
    ("en-tcf-canada-belgium", "TCF Canada in Belgium", "€268", "in Brussels · €260 in Ghent"),
    ("en-tcf-canada-italy", "TCF Canada in Italy", "7", "centres · €210 to €250"),
    ("en-tcf-canada-netherlands", "TCF Canada in the Netherlands", "€290", "in Amsterdam · The Hague, Rotterdam"),
    ("en-tcf-canada-portugal", "TCF Canada in Portugal", "€220", "Porto and Faro · €211 in Viseu"),
    ("en-tcf-canada-romania", "TCF Canada in Romania", "3", "Instituts français · Bucharest, Cluj, Timișoara"),
    ("en-tcf-canada-poland", "TCF Canada in Poland", "27 Nov", "in Warsaw · registration until 27 October"),
    ("en-tcf-canada-greece", "TCF Canada in Greece", "19 Nov", "in Athens · 5 sessions in 2027"),
    ("en-tcf-canada-ireland", "TCF Canada in Ireland", "€270", "in Dublin and Galway"),
    # Europe, suite (26/10/2026, après-midi) : DELF par pays, TCF en Autriche et au Luxembourg
    ("centres-delf-italie", "DELF en Italie", "25 févr.", "le B2 en 2027 · 160 €"),
    ("centres-delf-roumanie", "DELF en Roumanie", "14-15 nov.", "inscriptions jusqu'au 3 novembre"),
    ("centres-delf-pays-bas", "DELF aux Pays-Bas", "9-11 mars", "première session 2027 · B2 175 €"),
    ("centres-delf-grece", "DELF en Grèce", "15 mai", "le B2 en 2027 · inscriptions en février"),
    ("centres-delf-pologne", "DELF en Pologne", "18 nov.", "le B2 · 620 zł"),
    ("centres-delf-belgique", "DELF en Belgique", "19 nov.", "le B2 · Gand jusqu'au 3 novembre"),
    ("centres-delf-portugal", "DELF au Portugal", "20 nov.", "le B2 · 140 €"),
    ("centres-delf-irlande", "DELF en Irlande", "18 févr.", "premier B2 de 2027 · 5 sessions"),
    ("centres-delf-suede", "DELF en Suède", "1 450 SEK", "le B2 · pas de centre TCF"),
    ("centres-tcf-autriche", "TCF Canada en Autriche", "295 €", "à Vienne · DELF les 27-29 janvier 2027"),
    ("centres-tcf-luxembourg", "TCF au Luxembourg", "0", "TCF Canada · TCF IRN 150 €"),
    ("en-delf-italy", "DELF exam dates 2027 · Italy", "25 Feb", "first B2 of 2027 · €160"),
    ("en-delf-romania", "DELF exam dates 2027 · Romania", "14–15 Nov", "registration until 3 November"),
    ("en-delf-netherlands", "DELF exam dates 2027 · Netherlands", "9–11 Mar", "first 2027 session · B2 €175"),
    ("en-delf-greece", "DELF exam dates 2027 · Greece", "15 May", "DELF B2 · registration in February"),
    ("en-delf-poland", "DELF exam dates 2027 · Poland", "18 Nov", "DELF B2 · 620 zł"),
    ("en-delf-belgium", "DELF exam dates 2027 · Belgium", "19 Nov", "DELF B2 · Ghent until 3 November"),
    ("en-delf-portugal", "DELF exam dates 2027 · Portugal", "20 Nov", "DELF B2 · €140"),
    ("en-delf-ireland", "DELF exam dates 2027 · Ireland", "18 Feb", "first 2027 B2 · 5 sessions"),
    ("en-delf-sweden", "DELF exam dates 2027 · Sweden", "SEK 1,450", "DELF B2 · no TCF centre"),
    ("en-tcf-canada-austria", "TCF Canada in Austria", "€295", "in Vienna · DELF on 27–29 January 2027"),
    ("en-tcf-canada-luxembourg", "TCF in Luxembourg", "0", "TCF Canada · TCF IRN €150"),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def fit(draw, text, path, start, max_w, floor=22):
    """Réduit la taille jusqu'à ce que `text` tienne dans `max_w`."""
    size = start
    while size > floor:
        f = font(path, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(path, floor)


# Facebook, WhatsApp, Slack et LinkedIn affichent souvent un aperçu CARRÉ :
# ils recadrent le 1200×630 au centre et ne gardent que la bande x 285→915.
# Tout le contenu est donc centré et calibré pour tenir dans cette bande —
# sinon le début des titres, le chiffre-clé et le domaine disparaissent.
SAFE = H            # 630 px : largeur conservée par un recadrage carré centré
PAD = 16            # marge de sécurité à l'intérieur de la bande


def centered(d, text, f, y, fill):
    """Écrit `text` centré horizontalement sur toute la largeur."""
    d.text(((W - d.textlength(text, font=f)) / 2, y), text, font=f, fill=fill)


def build(slug, title, stat, label):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    box = SAFE - 2 * PAD          # largeur utile réelle : 598 px

    # bandeau supérieur, pleine largeur (survit à tout recadrage)
    d.rectangle([0, 0, W, 10], fill=ACCENT)

    # surtitre
    centered(d, "DELF · TCF · TEF", fit(d, "DELF · TCF · TEF", FONT_BOLD, 30, box), 74, MUTED)

    # titre
    f_title = fit(d, title, FONT_BOLD, 70, box)
    centered(d, title, f_title, 150, TITLE)

    # filet d'accent centré, sous le titre
    d.rectangle([W // 2 - 46, 258, W // 2 + 46, 264], fill=ACCENT)

    if stat:
        f_stat = fit(d, stat, FONT_BOLD, 112, box)
        centered(d, stat, f_stat, 310, ACCENT)
        centered(d, label, fit(d, label, FONT_REG, 34, box), 452, MUTED)
    else:
        centered(d, label, fit(d, label, FONT_REG, 36, box), 330, MUTED)

    # domaine
    centered(d, "delf-tcf-tef.fr", font(FONT_REG, 28), 556, ACCENT)

    path = os.path.normpath(os.path.join(OUT_DIR, slug + ".png"))
    im.save(path, optimize=True)
    return path


def main():
    force = "--force" in sys.argv
    made, skipped = [], []
    for slug, title, stat, label in PAGES:
        path = os.path.normpath(os.path.join(OUT_DIR, slug + ".png"))
        if os.path.exists(path) and not force:
            skipped.append(slug)
            continue
        build(slug, title, stat, label)
        made.append(slug)
    print("générées :", ", ".join(made) if made else "(aucune)")
    if skipped:
        print("déjà présentes :", ", ".join(skipped))


if __name__ == "__main__":
    main()
