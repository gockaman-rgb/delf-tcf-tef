#!/usr/bin/env python3
"""Lot « Où passer l'examen » — 17/09/2026.

Quatre articles + le hub /ou-passer/. Tous les chiffres viennent de deux
sources lues le 17 septembre 2026 : la liste officielle des centres de France
Éducation international (navigateur, par pays) et les pages inscription /
tarifs des centres eux-mêmes. Aucun prix d'agrégateur.

Usage : python3 _build/articles_ou_passer.py   (refuse d'écraser l'existant)
        python3 _build/articles_ou_passer.py --force
"""

import re
import sys
from article_template import build, APP

DATE = "2026-09-17"
DATE_FR = "17 septembre 2026"
FEI_LISTE = "https://www.france-education-international.fr/centres-d-examen/liste?pays=73&type-centre="
FEI_CARTE = "https://www.france-education-international.fr/centres-d-examen/carte?type-centre="
FDA_CENTRES = "https://www.lefrancaisdesaffaires.fr/trouver-un-centre-agree/"

SERIE = [
    ("/ou-passer/", "Tous les guides « Où passer »"),
    ("/blog/ou-passer-le-delf-en-france/", "DELF en France"),
    ("/blog/ou-passer-le-tcf-irn-en-france/", "TCF IRN en France"),
    ("/blog/ou-passer-l-examen-civique/", "Examen civique"),
    ("/blog/ou-passer-le-tcf-canada-en-france/", "TCF Canada en France"),
    ("/blog/ou-passer-le-tcf-canada-au-canada/", "TCF Canada au Canada"),
    ("/blog/tcf-canada-algerie/", "TCF Canada en Algérie"),
    ("/blog/tcf-canada-maroc/", "TCF Canada au Maroc"),
    ("/blog/tcf-canada-tunisie/", "TCF Canada en Tunisie"),
]


def serie(current):
    """Barre de la série, sans lien sur la page courante."""
    chips = []
    for url, label in SERIE:
        if url == current:
            chips.append(f'<span class="chip" aria-current="page">{label}</span>')
        else:
            chips.append(f'<a class="chip" href="{url}">{label}</a>')
    return '<p class="serie-label">Dans la même série</p>\n<div class="chips serie">\n' + "\n".join(chips) + "\n</div>"


def stats(items):
    """Bandeau de quatre tuiles (composant .stats de l'accueil)."""
    return '<div class="stats">\n' + "\n".join(
        f"<div class=\"stat\"><b>{b}</b><span>{s}</span>{('<em>' + e + '</em>') if e else ''}</div>"
        for b, s, e in items) + "\n</div>"


# ---------------------------------------------------------------------------
# 1. Où passer le DELF en France ?
# ---------------------------------------------------------------------------
DELF = {
    "slug": "ou-passer-le-delf-en-france",
    "accent": "accent-delf",
    "crumb": "Où passer le DELF en France",
    "title": "Où passer le DELF en France ? Centres, dates, inscription",
    "desc": "143 centres agréés, 10 sessions par an, un DELF B2 de 125 à 280 € selon le centre : où passer le DELF en France et comment s'inscrire, ville par ville.",
    "og_title": "Où passer le DELF en France ? Centres, dates, inscription",
    "og_desc": "143 centres agréés, 10 sessions par an, un B2 de 125 à 280 € selon le centre. Où et comment s'inscrire, ville par ville.",
    "h1": "Où passer le DELF en France&nbsp;? Les centres, les dates et l'inscription",
    "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": 11,
    "intro": """Le DELF se passe dans l'un des <strong>143 centres d'examen agréés</strong> par France
Éducation international en France — universités, Alliances françaises, GRETA, écoles de langue —,
lors de l'une des <strong>dix sessions nationales</strong> de l'année. On s'inscrit <strong>auprès du
centre</strong>, jamais auprès de FEI ni du rectorat, et c'est le centre qui fixe son prix, les
sessions qu'il ouvre et sa fenêtre d'inscription. Sept centres à Paris, un à sept par grande ville
en région — et des fenêtres d'inscription qui se referment parfois en deux jours.""",
    "facts": [
        "<strong>143 centres agréés</strong> en France (liste officielle FEI, relevée le 17 septembre 2026) : 7 à Paris, 7 à Lyon, 5 à Toulouse, 3 à Marseille, Bordeaux et Strasbourg.",
        "<strong>10 sessions par an</strong>, en 2026 comme en 2027 — jamais en avril ni en septembre. Prochaines : <strong>6-8 octobre, 3-5 novembre, 1-3 décembre 2026</strong>.",
        "Prix libre, fixé par chaque centre : <strong>DELF B2 de 125 € à 280 €</strong>, B1 de 125 € à 230 €, sur les centres relevés.",
        "⚠️ <strong>L'inscription ferme tôt</strong> : quatre à huit semaines avant l'écrit, parfois sur deux jours seulement — et des sessions affichent complet des mois à l'avance.",
        "Un centre n'ouvre pas forcément les dix sessions : de <strong>2 par an</strong> (Sorbonne Nouvelle) à 10 (Alliance française de Lyon).",
        "Résultats en <strong>4 à 6 semaines</strong> ; le diplôme est <strong>valable à vie</strong>.",
    ],
    "toc": [
        ("qui-fait-quoi", "Qui organise quoi : FEI, le rectorat, le centre"),
        ("calendrier", "Le calendrier 2026-2027 des sessions"),
        ("paris", "Passer le DELF à Paris : les 7 centres"),
        ("villes", "Les centres ville par ville"),
        ("inscription", "S'inscrire, pas à pas"),
        ("prix", "Combien ça coûte, centre par centre"),
        ("pieges", "Les pièges qui font perdre une session"),
        ("apres", "Après l'examen : résultats et diplôme"),
    ],
    "body": """
<h2 id="qui-fait-quoi">Qui organise quoi : FEI, le rectorat, le centre</h2>

<p>Trois acteurs, et un seul à contacter. <strong>France Éducation international</strong> (FEI)
conçoit les sujets, forme les correcteurs et délivre le diplôme au nom du ministère de
l'Éducation nationale. Le <strong>rectorat</strong> de chaque académie encadre les sessions sur son
territoire — les Cours de civilisation française de la Sorbonne le rappellent sur leur page :
« chaque année, un arrêté du Rectorat précise les dates des sessions du DELF-DALF […] ainsi que la
composition du jury ». Et le <strong>centre d'examen</strong> fait tout le reste : il ouvre ou non
telle session, fixe son tarif, prend les inscriptions, convoque, fait passer l'oral, remet les
résultats.</p>

<p>La page pratique de FEI est sans ambiguïté : « Pour m'inscrire à un diplôme, je dois contacter
un centre d'examen. Le centre d'examen me renseigne sur les coûts d'inscription, les dates, les
lieux d'examen. » Il n'existe donc <strong>ni inscription centrale, ni tarif national, ni
calendrier unique par centre</strong> — seulement un calendrier national de dates possibles, dans
lequel chaque centre pioche.</p>

<p>Les 143 centres agréés en France se répartissent en quatre familles : les
<strong>universités</strong> (services universitaires de langues, comme le DEFLE de Bordeaux
Montaigne ou l'i-FLE de Nantes Université), les <strong>Alliances françaises</strong> (Paris, Lyon,
Lille, Bordeaux, Grenoble, Strasbourg, Aix-Marseille, Toulouse…), les <strong>GRETA</strong> et
organismes de formation continue, et les <strong>écoles de langue privées</strong>. La liste
officielle, avec adresse, téléphone et site de chaque centre, est sur
<a href="%(liste)sdelf_dalf" rel="noopener">la liste des centres DELF-DALF de FEI</a> (filtre
« France »), doublée d'une <a href="%(carte)sdelf_dalf" rel="noopener">carte</a>. Une règle simple :
si un organisme n'y figure pas, il ne peut pas vous faire passer le DELF.</p>

%(serie)s

<h2 id="calendrier">Le calendrier 2026-2027 des sessions</h2>

<p>FEI publie chaque année le calendrier national des sessions « tout public » en France. Le
rythme est immuable : le <strong>mardi</strong> pour les DELF A1 (10 h) et A2 (14 h), le
<strong>mercredi</strong> pour les DELF B1 (10 h) et B2 (14 h), le <strong>jeudi</strong> pour
les DALF C1 (9 h) et C2 (14 h 30). Ce sont les horaires des épreuves collectives ; l'oral est
fixé par le centre, après l'écrit, dans les 30 jours qui suivent et avant le 15 du mois suivant.</p>

<div class="tablewrap">
<table>
<caption>Sessions nationales DELF-DALF tout public en France. Source : calendriers 2026 et 2027 de France Éducation international, consultés le 17 septembre 2026. Chaque centre choisit les sessions qu'il ouvre.</caption>
<thead><tr><th>Mois</th><th>2026 (écrits)</th><th>2027 (écrits)</th></tr></thead>
<tbody>
<tr><td>Janvier</td><td>13-15 janvier</td><td>12-14 janvier</td></tr>
<tr><td>Février</td><td>3-5 février</td><td>2-4 février</td></tr>
<tr><td>Mars</td><td>3-5 mars</td><td>16-18 mars</td></tr>
<tr><td>Avril</td><td>—</td><td>—</td></tr>
<tr><td>Mai</td><td>19-21 mai</td><td>25-27 mai</td></tr>
<tr><td>Juin</td><td>9-11 juin</td><td>15-17 juin</td></tr>
<tr><td>Juillet</td><td>7-9 juillet</td><td>6-8 juillet</td></tr>
<tr><td>Août</td><td>18-20 août</td><td>3-5 août</td></tr>
<tr><td>Septembre</td><td>—</td><td>—</td></tr>
<tr><td>Octobre</td><td><strong>6-8 octobre</strong></td><td>5-7 octobre</td></tr>
<tr><td>Novembre</td><td><strong>3-5 novembre</strong></td><td>16-18 novembre</td></tr>
<tr><td>Décembre</td><td><strong>1-3 décembre</strong></td><td>7-9 décembre</td></tr>
</tbody>
</table>
</div>

<p>Dix sessions par an, donc, mais <strong>rarement dix dans un même centre</strong>. Sur les
centres relevés : l'Alliance française de Lyon ouvre les dix ; les Cours de civilisation française
de la Sorbonne en ouvrent quatre (juin, juillet, octobre, décembre) ; Nantes Université, quatre
(décembre, mars, mai, juin) ; l'Alliance française de Lille, deux (juin, novembre) ; la Sorbonne
Nouvelle, deux (février, mai). Si votre dossier a une échéance, le calendrier de <em>votre</em>
centre compte plus que le calendrier national.</p>

<h2 id="paris">Passer le DELF à Paris : les 7 centres</h2>

<p>Sept centres agréés dans Paris intra-muros : deux universités, une Alliance française, trois
écoles privées ou associatives et le centre de l'académie. Les tarifs et dates ci-dessous ont été lus sur le site de chaque centre le
17 septembre 2026 ; ils changent chaque année.</p>

<div class="tablewrap wide">
<table>
<caption>Centres DELF-DALF agréés à Paris (liste FEI du 17 septembre 2026) et ce que leur site affichait ce jour-là. « Non relevé » = le centre ne publie pas l'information, ou nous ne l'avons pas vérifiée.</caption>
<thead><tr><th>Centre</th><th>Tarifs DELF</th><th>Sessions et inscription</th></tr></thead>
<tbody>
<tr><td><strong>Alliance française Paris Île-de-France</strong> (6<sup>e</sup>)</td><td>A2 190 € · B1 230 € · <strong>B2 280 €</strong> · DALF 290 € (20 € de frais de dossier inclus)</td><td>Session de novembre 2026 : écrit le 3 (A2) ou 4 (B1, B2) novembre, oraux du 13 au 20 ; <strong>inscription jusqu'au 4 octobre</strong>. Résultats par e-mail sous six semaines.</td></tr>
<tr><td><strong>Université Sorbonne Nouvelle</strong>, Campus Nation (12<sup>e</sup>)</td><td>B1 194 € · <strong>B2 249 €</strong> · C1 249 € · C2 290 € (tarif réduit pour ses étudiants)</td><td><strong>Deux sessions par an</strong> seulement, février et mai ; inscriptions en ligne sur trois semaines, dix semaines avant l'écrit (24 novembre-17 décembre pour février, 23 mars-17 avril pour mai).</td></tr>
<tr><td><strong>Cours de civilisation française de la Sorbonne</strong> (17<sup>e</sup>)</td><td>B1 214 € · <strong>B2 269 €</strong> · C1 279 €</td><td>Sessions de juin, juillet, octobre et décembre 2026. Pour l'écrit du 2 décembre, <strong>inscriptions du 12 octobre au 8 novembre</strong>.</td></tr>
<tr><td><strong>SELFEE – Sorbonne Université</strong>, Faculté des Lettres (5<sup>e</sup>)</td><td>Non relevé</td><td>Sur le site de la faculté.</td></tr>
<tr><td><strong>Prosodia</strong> (20<sup>e</sup>)</td><td>Non relevé</td><td>Sur le site du centre.</td></tr>
<tr><td><strong>THOT</strong> (1<sup>er</sup>)</td><td>Non relevé</td><td>École de français pour personnes réfugiées et demandeuses d'asile.</td></tr>
<tr><td><strong>CASNAV de Paris</strong> (19<sup>e</sup>)</td><td>—</td><td>Centre de l'académie, orienté DELF scolaire.</td></tr>
</tbody>
</table>
</div>

<p>Deux enseignements. D'abord, pour un DELF B2 identique, l'écart dans Paris va de
<strong>249 € à 280 €</strong> — et à 125 € à Nantes ou 159 € à Lyon. Ensuite, la fenêtre
d'inscription se referme <strong>quatre à dix semaines avant l'écrit</strong> : l'Alliance
française de Paris ferme celle de sa session de novembre le 4 octobre, et les Cours de
civilisation française de la Sorbonne celle de leur écrit du 2 décembre le 8 novembre. Qui
cherche un centre parisien mi-novembre pour un B2 avant Noël n'en trouvera pas.</p>

<h2 id="villes">Les centres ville par ville</h2>

<p>En région, un centre par ville moyenne, plusieurs dans les métropoles. Voici les centres de la
liste officielle pour les grandes villes, et ce que nous avons pu lire sur leurs sites le
17 septembre 2026.</p>

<div class="tablewrap wide">
<table>
<caption>Centres DELF-DALF agréés par ville (liste FEI du 17 septembre 2026). Les tarifs cités sont ceux du DELF B2 affichés par le centre ce jour-là.</caption>
<thead><tr><th>Ville</th><th>Centres agréés</th><th>Ce que nous avons relevé</th></tr></thead>
<tbody>
<tr><td><strong>Lyon</strong></td><td>Alliance française de Lyon · ALPES Formation · GRETA CFA Lyon Métropole · Inflexyon (Lyon Exam) · ILCF – UCLy · Lyon Bleu International · REN Formation</td><td>AF Lyon : <strong>B2 159 €</strong>, les dix sessions de l'année ; le 17 septembre, octobre et novembre affichaient déjà <strong>complet</strong>, il restait décembre. Résultats par courrier sous 6 semaines.</td></tr>
<tr><td><strong>Marseille · Aix</strong></td><td>Alliance française Aix-Marseille Provence · Université d'Aix-Marseille (SUL) · IS Aix-en-Provence · EPFF · École de la 2<sup>e</sup> chance</td><td>AF Aix-Marseille : tarif non affiché en ligne ; résultats en 4 à 6 semaines, à retirer sur place ; épreuves d'entraînement officielles A2-B2 à Aix.</td></tr>
<tr><td><strong>Toulouse</strong></td><td>Université Toulouse Jean Jaurès (DEFLE) · Alliance française de Toulouse · CREPT Formation · Langue Onze · SPLE Vidal</td><td>Non relevé.</td></tr>
<tr><td><strong>Bordeaux</strong></td><td>Université Bordeaux Montaigne (DEFLE, Pessac) · Alliance française Bordeaux Nouvelle-Aquitaine · Newdeal Institut</td><td>DEFLE : session du 1<sup>er</sup>-3 décembre 2026, <strong>inscriptions du 2 octobre au 4 novembre</strong> ; l'oral entre le 1<sup>er</sup> et le 15 décembre, date communiquée deux semaines avant.</td></tr>
<tr><td><strong>Lille</strong></td><td>Alliance française de Lille Métropole</td><td>A1 120 € · A2 130 € · B1 160 € · <strong>B2 180 €</strong> · C1 200 € · C2 210 €. Session de novembre 2026 : <strong>inscriptions du 30 septembre (10 h) au 7 octobre</strong>, écrits du 3 au 5 novembre.</td></tr>
<tr><td><strong>Nantes</strong></td><td>Nantes Université (i-FLE)</td><td><strong>B1 et B2 125 €</strong>, C1-C2 145 € — le moins cher relevé. Inscriptions sur <strong>deux jours, à partir de 7 h</strong>, « dans la limite des places disponibles » : 22-23 septembre 2026 pour la session du 2-4 décembre, puis 9-10 février, 20-21 avril et 11-12 mai 2027.</td></tr>
<tr><td><strong>Strasbourg</strong></td><td>Alliance française Strasbourg Europe · École européenne de Strasbourg · Pôle FLE de l'Université de Strasbourg</td><td>Non relevé.</td></tr>
<tr><td><strong>Montpellier</strong></td><td>Université Paul-Valéry (IEFE)</td><td>Non relevé.</td></tr>
<tr><td><strong>Nice</strong></td><td>CUEFLE – Université Côte d'Azur · Centre international de Valbonne</td><td>Non relevé.</td></tr>
<tr><td><strong>Grenoble</strong></td><td>Alliance française Grenoble Alpes · CUEF – Université Grenoble Alpes (Saint-Martin-d'Hères) · GRETA Nord-Isère (Bourgoin)</td><td>Non relevé.</td></tr>
<tr><td><strong>Rennes</strong></td><td>Université Rennes 2 (CIREFE) · Alliance française Saint-Malo Bretagne</td><td>Non relevé.</td></tr>
<tr><td><strong>Rouen</strong></td><td>Alliance française de Normandie · Université de Rouen (Maison des langues) · Éducation et Formation · RECIFE (Le Havre)</td><td>Non relevé.</td></tr>
</tbody>
</table>
</div>

<p>Pour toute autre ville, la <a href="%(liste)sdelf_dalf" rel="noopener">liste officielle</a>
donne le centre le plus proche avec son téléphone et son site. Comptez un centre dans presque
chaque préfecture ; dans les départements ruraux, c'est souvent le GRETA.</p>

<h2 id="inscription">S'inscrire, pas à pas</h2>

<ol>
<li><strong>Choisissez le niveau, pas le diplôme le plus haut.</strong> Les quatre DELF sont
indépendants : on s'inscrit directement au B2 sans avoir le B1. Pour la naturalisation, c'est le
<a href="/delf-b2/">B2</a> ; pour la carte de résident, le <a href="/delf-b1/">B1</a>. Un examen
blanc noté vous évite de payer un niveau que vous n'avez pas encore — ou d'en viser un trop bas.</li>
<li><strong>Repérez votre centre sur la liste officielle</strong> et lisez sa page DELF : sessions
ouvertes, tarif, mode d'inscription. Deux centres voisins peuvent avoir des calendriers sans
rapport.</li>
<li><strong>Notez la fenêtre d'inscription</strong>, pas la date de l'examen. Elle ferme quatre à
dix semaines avant l'écrit, et s'ouvre parfois sur deux jours seulement. Les centres
universitaires publient leurs dates d'inscription à l'année : c'est <em>celles-là</em> qu'il faut
mettre dans votre agenda.</li>
<li><strong>Remplissez le formulaire en ligne et payez.</strong> Pièce d'identité en cours de
validité (scan), parfois votre numéro de candidat si vous avez déjà passé un DELF, paiement par
carte. Nantes Université prévient : « Les droits d'inscription aux examens ne sont pas
remboursables. »</li>
<li><strong>Attendez la convocation</strong>, envoyée par e-mail une à deux semaines avant. Elle
porte la date de votre oral, que vous ne choisissez pas.</li>
<li><strong>Le jour J</strong> : convocation et pièce d'identité officielle avec photo, valide.
Sans les deux, l'accès à la salle est refusé.</li>
</ol>

<p>Un point que peu de candidats anticipent : les <strong>aménagements</strong> (tiers-temps,
aide humaine, adaptation d'épreuve) se demandent <strong>deux mois avant</strong> l'examen, avec
un certificat médical — Nantes Université et l'Alliance française de Bordeaux l'écrivent
noir sur blanc.</p>

<h2 id="prix">Combien ça coûte, centre par centre</h2>

<p>Aucun texte ne fixe le prix du DELF ; chaque centre vote ou décide le sien. Sur les centres
relevés le 17 septembre 2026, un même DELF B2 coûte :</p>

<div class="tablewrap">
<table>
<caption>Tarifs du DELF B1 et du DELF B2 affichés sur le site de chaque centre le 17 septembre 2026. Indicatif : les centres révisent leurs tarifs chaque année.</caption>
<thead><tr><th>Centre</th><th>DELF B1</th><th>DELF B2</th></tr></thead>
<tbody>
<tr><td>Nantes Université (i-FLE)</td><td>125 €</td><td><strong>125 €</strong></td></tr>
<tr><td>Alliance française de Lyon</td><td>non relevé</td><td><strong>159 €</strong></td></tr>
<tr><td>Alliance française de Lille Métropole</td><td>160 €</td><td><strong>180 €</strong></td></tr>
<tr><td>Université Sorbonne Nouvelle, Paris</td><td>194 €</td><td><strong>249 €</strong></td></tr>
<tr><td>Cours de civilisation française de la Sorbonne, Paris</td><td>214 €</td><td><strong>269 €</strong></td></tr>
<tr><td>Alliance française Paris Île-de-France</td><td>230 €</td><td><strong>280 €</strong></td></tr>
</tbody>
</table>
</div>

<p>Du simple au double, et plus, pour un diplôme strictement identique — le sujet est national,
le jury est habilité par FEI, le diplôme porte la même signature. Les universités sont
presque toujours les moins chères, et proposent souvent un tarif réduit à leurs propres
étudiants (134 € au lieu de 249 € à la Sorbonne Nouvelle). Si vous êtes en Île-de-France,
Nantes ou Lille sont à moins de deux heures de train : pour un B2, le billet est vite amorti.
Notre article sur <a href="/blog/prix-tcf-tef/">le prix des tests</a> détaille la même logique
pour le TCF et le TEF.</p>

<h2 id="pieges">Les pièges qui font perdre une session</h2>

<div class="warn"><strong>Le piège n° 1 est le calendrier, pas le niveau.</strong> Entre une
fenêtre d'inscription de deux jours (Nantes), d'une semaine (Lille) ou de trois semaines
(Sorbonne Nouvelle), une fermeture six semaines avant l'écrit (Paris) et des sessions
complètes deux mois à l'avance (Lyon), le candidat qui « verra le mois prochain » perd
facilement un trimestre. Inscrivez-vous dès l'ouverture, et à la session que vous pouvez
préparer, pas à la plus proche.</div>

<ul>
<li><strong>Le même niveau, deux fois de suite.</strong> L'Alliance française Aix-Marseille
prévient : « Il n'est pas possible de se réinscrire au DELF/DALF du même niveau tant que les
résultats de la session précédente n'ont pas été annoncés. » Avec des résultats à six semaines,
rater une session coûte deux mois minimum.</li>
<li><strong>« Tout public », pas « junior » ni « scolaire ».</strong> Le DELF junior et le DELF
scolaire ont leur propre calendrier (mai, juin, novembre) et sont réservés aux élèves et jeunes
adolescents. Un adulte passe le DELF tout public — c'est celui de ce guide.</li>
<li><strong>Le DELF s'arrête au B2.</strong> Au-delà, c'est le <a href="/dalf/">DALF C1 ou C2</a>,
même centre, même session, le jeudi.</li>
<li><strong>Les offres « à distance ».</strong> Le DELF se passe en centre, sur convocation, avec
contrôle d'identité. Un site qui promet un diplôme sans passer en centre vend un faux — et la
fraude aux certifications est un délit que FEI poursuit.</li>
<li><strong>Diplôme ou test ?</strong> Le DELF prend un trimestre à obtenir mais ne périme
jamais ; un TCF IRN se passe en une matinée, presque chaque semaine à Paris, mais expire au bout
de deux ans. Pour choisir, lisez <a href="/blog/diplome-ou-test-delf-tcf/">diplôme ou test : lequel
vous faut-il&nbsp;?</a> — et pour le test, <a href="/blog/ou-passer-le-tcf-irn-en-france/">où passer le
TCF IRN en France</a>.</li>
</ul>

<h2 id="apres">Après l'examen : résultats et diplôme</h2>

<p>Les copies sont corrigées par des correcteurs habilités par FEI, puis un jury valide les
résultats — c'est le <strong>centre</strong> qui vous les communique, par e-mail ou par
courrier, sous <strong>quatre à six semaines</strong> selon les centres relevés (six à l'Alliance
française de Paris et à celle de Lyon, quatre à six à Aix-Marseille). Le seuil d'admission est
de 50 sur 100, avec une note éliminatoire à 5 sur 25 par épreuve — le détail est dans notre
guide du <a href="/delf-b2/">DELF B2</a>.</p>

<p>« Les décisions des jurys sont sans appel : les candidats ne peuvent pas contester leurs
notes », précise FEI ; vous pouvez en revanche demander à consulter votre copie auprès du
centre. En cas de réussite, le diplôme — imprimé par FEI — vous est remis par le centre, valable
à vie ; en cas d'échec, un relevé de notes. Un dysfonctionnement dans l'organisation (accueil,
surveillance, épreuve individuelle) se signale directement à FEI, à l'adresse
<em>signalement.dilfdelfdalftcf@france-education-international.fr</em>.</p>
""" % {"liste": FEI_LISTE, "carte": FEI_CARTE, "serie": serie("/blog/ou-passer-le-delf-en-france/")},
    "cta_h2": "Sachez si vous avez le niveau avant de payer la session",
    "cta_p": """Un DELF B2 coûte de 125 à 280 €, se prépare sur un trimestre et ne se repasse pas avant
la publication des résultats. Les examens blancs de l'app «&nbsp;TCF DELF TEF&nbsp;: Tests
2026&nbsp;» reproduisent les quatre épreuves au format officiel, avec la note sur 100, le seuil
de 50 et la correction IA de la production écrite et de l'oral.""",
    "faq": [
        ("Où s'inscrire au DELF en France&nbsp;?",
         "Uniquement auprès d'un centre d'examen agréé par France Éducation international — il y en a 143 en France, dont sept à Paris. C'est le centre qui prend l'inscription, fixe le tarif et convoque ; ni FEI ni le rectorat n'inscrivent de candidats. La liste officielle des centres, avec téléphone et site, est publiée par FEI."),
        ("Quand ont lieu les sessions du DELF en 2026 et 2027&nbsp;?",
         "Dix sessions par an, jamais en avril ni en septembre. En 2026, il reste les sessions des 6-8 octobre, 3-5 novembre et 1-3 décembre ; en 2027 : 12-14 janvier, 2-4 février, 16-18 mars, 25-27 mai, 15-17 juin, 6-8 juillet, 3-5 août, 5-7 octobre, 16-18 novembre et 7-9 décembre. Le DELF B1 et le DELF B2 se passent toujours le mercredi. Chaque centre choisit les sessions qu'il ouvre."),
        ("Combien coûte le DELF B2&nbsp;?",
         "Il n'y a pas de tarif national. Sur les centres relevés le 17 septembre 2026 : 125 € à Nantes Université, 159 € à l'Alliance française de Lyon, 180 € à Lille, 249 € à la Sorbonne Nouvelle, 269 € aux Cours de civilisation française de la Sorbonne et 280 € à l'Alliance française de Paris. Les universités sont presque toujours les moins chères."),
        ("Peut-on passer le DELF en ligne ou à distance&nbsp;?",
         "Non. Les quatre épreuves se passent dans le centre d'examen, sur convocation, avec contrôle d'identité, aux dates du calendrier national. Toute offre de DELF « à distance » ou « sans déplacement » est une fraude, et les dossiers de naturalisation et de titre de séjour exigent de toute façon une passation en présentiel."),
        ("Quelle est la date limite d'inscription&nbsp;?",
         "Elle dépend du centre et ferme bien avant l'examen : le 4 octobre pour la session de novembre à l'Alliance française de Paris, du 12 octobre au 8 novembre pour le 2 décembre à la Sorbonne, deux jours seulement (22-23 septembre) à Nantes Université pour décembre. Comptez quatre à dix semaines avant l'écrit, et inscrivez-vous dès l'ouverture : plusieurs centres affichent complet des mois à l'avance."),
        ("Combien de temps pour recevoir les résultats et le diplôme&nbsp;?",
         "Les résultats sont communiqués par le centre, généralement sous quatre à six semaines. Le diplôme lui-même, imprimé par France Éducation international, est remis ensuite par le centre ; il est valable à vie. En cas d'échec, le centre fournit un relevé de notes, et l'on ne peut pas se réinscrire au même niveau tant que les résultats de la session précédente ne sont pas publiés."),
        ("Faut-il avoir le DELF B1 pour passer le B2&nbsp;?",
         "Non. Les quatre diplômes du DELF sont indépendants : on s'inscrit directement au niveau visé. Pour la naturalisation, c'est le B2 à l'oral comme à l'écrit ; pour la carte de résident, le B1. Passez un examen blanc noté avant de choisir : une inscription à un niveau trop haut se paie plein tarif, et il faut attendre la session suivante."),
    ],
    "also": [
        ("/blog/diplome-ou-test-delf-tcf/", "Diplôme ou test : DELF, DALF, TCF ou TEF, lequel vous faut-il&nbsp;?", "Un diplôme s'obtient à vie et peut se rater ; un test vous situe pour deux ans. Ce que chacun prouve et qui l'accepte."),
        ("/delf-b2/", "DELF B2 : format, notation et préparation", "Les quatre épreuves, le seuil de 50 sur 100, la note éliminatoire et la méthode."),
        ("/blog/naturalisation-2026-niveau-b2/", "Naturalisation 2026 : le niveau B2 est devenu obligatoire", "Ce qui change depuis janvier 2026, les justificatifs recevables, le régime transitoire."),
        ("/blog/ou-passer-le-tcf-irn-en-france/", "Où passer le TCF IRN en France&nbsp;?", "L'alternative au diplôme pour un dossier pressé : centres, prix, sessions hebdomadaires."),
    ],
    "sources": """<strong>Sources.</strong> Liste et carte des centres d'examen DELF-DALF de France
Éducation international (filtre « France »), page « Informations pratiques pour les candidats au
DELF-DALF » et calendriers 2026 et 2027 des sessions en France, consultés le 17 septembre 2026 ;
pages DELF-DALF et formulaires d'inscription de l'Alliance française Paris Île-de-France, de
l'Université Sorbonne Nouvelle (brochure « Session 2026 »), des Cours de civilisation française
de la Sorbonne, de l'Alliance française de Lyon, de Nantes Université (i-FLE, mise à jour du
14 septembre 2026), du DEFLE de l'Université Bordeaux Montaigne, de l'Alliance française de Lille
Métropole et de l'Alliance française Aix-Marseille Provence, consultées le 17 septembre 2026.
Les tarifs et dates changent chaque année : vérifiez-les sur le site de votre centre avant de
payer.""",
}


# ---------------------------------------------------------------------------
# 2. Où passer le TCF IRN en France ?
# ---------------------------------------------------------------------------
IRN = {
    "slug": "ou-passer-le-tcf-irn-en-france",
    "accent": "accent-irn",
    "crumb": "Où passer le TCF IRN en France",
    "title": "Où passer le TCF IRN en France ? Centres et inscription",
    "desc": "251 centres TCF en France, pas tous en IRN. Les centres relevés à Paris et en région, leurs prix de 140 à 220 €, leurs dates et le pas-à-pas d'inscription.",
    "og_title": "Où passer le TCF IRN en France ? Centres et inscription",
    "og_desc": "Les centres relevés à Paris et en région, leurs prix de 140 à 220 €, leurs dates et le pas-à-pas d'inscription.",
    "h1": "Où passer le TCF IRN en France&nbsp;? Les centres, les prix et l'inscription",
    "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": 10,
    "intro": """Le TCF IRN se passe dans un <strong>centre agréé par France Éducation international</strong>
— 251 centres TCF en France, dont sept à Paris — sur papier ou sur ordinateur, avec des sessions
<strong>chaque semaine dans les grandes villes</strong>. On s'inscrit <strong>en ligne auprès du
centre</strong>, on paie entre <strong>140 € et 220 €</strong> selon l'adresse, et l'attestation
arrive <strong>deux à trois semaines</strong> plus tard. Voici où, comment, à quel prix — et ce
qu'il faut éviter, à commencer par les offres « à distance ».""",
    "facts": [
        "<strong>251 centres TCF</strong> en France (liste FEI, 17 septembre 2026), 126 avec des sessions sur ordinateur — mais <strong>tous ne proposent pas l'IRN</strong> : vérifiez la déclinaison sur le site du centre.",
        "À Paris, <strong>7 centres</strong> ; ACTE affiche une session IRN par semaine, ACCORD deux par mois.",
        "Prix libre : <strong>140 € (ACTE, Paris) à 220 € (ACCORD, Paris)</strong> ; 169 € à Lyon, 180 € à Rennes, 185 € à Montpellier.",
        "Inscription <strong>en ligne, en quelques minutes</strong>, jusqu'à 2 à 10 jours avant la session ; pièce d'identité valide obligatoire le jour J.",
        "Résultats en <strong>2 à 3 semaines</strong> ; sur ordinateur, certains centres remettent une attestation provisoire immédiate pour les QCM.",
        "⚠️ <strong>20 à 30 jours</strong> obligatoires entre deux passations, et l'attestation vaut <strong>2 ans</strong>. L'<strong>examen civique</strong> est un autre examen, souvent dans les mêmes centres.",
    ],
    "toc": [
        ("reseau", "Qui peut vous faire passer le TCF IRN"),
        ("paris", "Passer le TCF IRN à Paris : 7 centres"),
        ("villes", "En région : les centres relevés"),
        ("inscription", "S'inscrire, pas à pas"),
        ("ordinateur", "Sur papier ou sur ordinateur&nbsp;?"),
        ("prix", "Combien ça coûte"),
        ("civique", "Et l'examen civique&nbsp;?"),
        ("pieges", "Les pièges : « à distance », mauvais TCF, délais"),
    ],
    "body": """
<h2 id="reseau">Qui peut vous faire passer le TCF IRN</h2>

<p>Le TCF IRN — <a href="/tcf-irn/">Intégration, Résidence et Nationalité</a> — est conçu par
France Éducation international et <strong>administré par des centres agréés</strong> : Alliances
françaises, écoles de langue, organismes de formation, GRETA, quelques universités. FEI n'inscrit
personne directement ; c'est le centre qui ouvre les sessions, fixe son tarif, vous convoque et vous
remet l'attestation. Sa liste officielle compte, au 17 septembre 2026, <strong>251 centres de
passation en France</strong>, dont 126 proposent des sessions sur ordinateur.</p>

<p>Une subtilité qui coûte des semaines aux candidats : la liste de FEI dit qu'un centre est agréé
TCF, <strong>pas quelle déclinaison il organise</strong>. L'Alliance française de Strasbourg fait
passer le TCF IRN et le TCF tout public, mais pas le TCF Canada ; Etoile Institut, à Paris, affiche
l'IRN, le tout public et le Québec. Avant de vous déplacer, ouvrez la page « TCF » du centre et
cherchez les trois lettres <strong>IRN</strong>. La liste officielle est
<a href="%(liste)stcf" rel="noopener">ici</a> (filtre « France »), avec l'adresse, le téléphone et
le site de chaque centre ; si un organisme n'y figure pas, son « TCF » n'en est pas un.</p>

%(serie)s

<h2 id="paris">Passer le TCF IRN à Paris : 7 centres</h2>

<p>Sept centres agréés TCF dans Paris. Pour cinq d'entre eux nous avons pu lire, le 17 septembre
2026, le tarif et le calendrier du TCF IRN sur leur propre site.</p>

<div class="tablewrap wide">
<table>
<caption>Centres TCF agréés à Paris (liste FEI du 17 septembre 2026) et ce que leur site affichait ce jour-là pour le TCF IRN. « Non relevé » = information non publiée ou non vérifiée.</caption>
<thead><tr><th>Centre</th><th>TCF IRN</th><th>Sessions et inscription</th></tr></thead>
<tbody>
<tr><td><strong>ACTE</strong> (10<sup>e</sup>, rue du Buisson-Saint-Louis)</td><td><strong>140 €</strong>, papier ou ordinateur (45 € de frais d'inscription non remboursables inclus)</td><td>Presque <strong>une session par semaine</strong> : 14, 21 et 28 octobre, 18 et 25 novembre, 9 et 16 décembre 2026 sur papier, plus le calendrier sur ordinateur. Résultats « au minimum 3 semaines » après, par e-mail ou sur place.</td></tr>
<tr><td><strong>ACCORD</strong> (15<sup>e</sup>, examensparis.fr)</td><td><strong>220 €</strong>, sur ordinateur</td><td>Deux sessions par mois (14 et 21 octobre, 18 et 25 novembre 2026), inscription close <strong>5 jours avant</strong> par bulletin envoyé par e-mail, paiement par carte ou espèces. Attestation provisoire immédiate pour les QCM, définitive sous 2 semaines.</td></tr>
<tr><td><strong>Etoile Institut de langue</strong> (7<sup>e</sup>)</td><td><strong>160 €</strong> en semaine, <strong>170 €</strong> le samedi (TCF ou TEF IRN)</td><td>Calendrier et inscription en ligne sur etoilecertifications.com.</td></tr>
<tr><td><strong>Cours de civilisation française de la Sorbonne</strong> (17<sup>e</sup>)</td><td>Sur ordinateur (tarif non relevé)</td><td>Page « TCF IRN sur ordinateur » du centre.</td></tr>
<tr><td><strong>Alliance française Paris Île-de-France</strong> (6<sup>e</sup>)</td><td>Non relevé</td><td>Le centre met en avant le DELF, le TEF et l'examen civique ; vérifiez l'IRN sur alliancefr.org.</td></tr>
<tr><td><strong>ELFE</strong> (1<sup>er</sup>)</td><td>Non relevé</td><td>Sur le site du centre.</td></tr>
<tr><td><strong>ILE International</strong> (12<sup>e</sup>)</td><td>Non relevé</td><td>Sur le site du centre.</td></tr>
</tbody>
</table>
</div>

<p>Le point à retenir : à Paris, le TCF IRN se passe <strong>toutes les semaines</strong>, et
l'inscription ferme quelques jours avant. Contrairement au <a href="/blog/ou-passer-le-delf-en-france/">DELF</a>,
ce n'est pas la place qui manque, c'est l'écart de prix qui surprend — <strong>140 € contre
220 €</strong> pour le même test, à trois stations de métro.</p>

<h2 id="villes">En région : les centres relevés</h2>

<div class="tablewrap wide">
<table>
<caption>Centres proposant le TCF IRN en région, avec le tarif et les informations lues sur leur site le 17 septembre 2026. Les autres centres agréés de chaque ville figurent sur la liste FEI.</caption>
<thead><tr><th>Ville</th><th>Centre</th><th>TCF IRN relevé</th></tr></thead>
<tbody>
<tr><td><strong>Lyon</strong></td><td>Alliance française de Lyon</td><td><strong>169 €</strong> sur ordinateur ; sessions des 9 et 17 septembre et du 22 octobre complètes le 17 septembre, 19 novembre ouvert ; inscriptions closes 48 h avant ; résultats par courriel sous 2 à 3 semaines. Aussi : Lyon Exam (Inflexyon), Lyon Bleu, KLF.</td></tr>
<tr><td><strong>Montpellier</strong></td><td>Alliance française de Montpellier</td><td><strong>185 €</strong>, papier ou ordinateur ; résultats définitifs sous 2 semaines sur ordinateur. Aussi : LSF, INFREP, KLF.</td></tr>
<tr><td><strong>Rennes · Brest · Saint-Brieuc · Vannes</strong></td><td>CLPS L'Enjeu Compétences</td><td><strong>180 €</strong> ; inscription par fiche en ligne. À Rennes aussi : Langue et Communication.</td></tr>
<tr><td><strong>Nantes</strong></td><td>Espaces Formation</td><td>Papier ou ordinateur, inscription et paiement en ligne, résultats sous 2 à 3 semaines ; sessions « en urgence » sur ordinateur selon disponibilités. Aussi : Institut Fonelia.</td></tr>
<tr><td><strong>Strasbourg</strong></td><td>Alliance française Strasbourg Europe</td><td>Papier et ordinateur ; le centre ne propose que l'IRN et le tout public. Aussi : CIEL, Stralang.</td></tr>
<tr><td><strong>Bordeaux · Toulouse · Annecy</strong></td><td>KLF (klf-examen.fr)</td><td>Sur ordinateur (papier à Annecy) ; résultats « entre 10 jours et 3 semaines », attestation à retirer au centre. Bordeaux aussi : Alliance française, INFREP, Newdeal ; Toulouse : Alliance française, CREPT, Langue Onze, AMS Grand Sud.</td></tr>
<tr><td><strong>Marseille · Aix</strong></td><td>Alliance française Aix-Marseille Provence</td><td>Sur ordinateur uniquement ; inscription deux semaines à l'avance, résultats en 15 jours. Aussi : Atout Langues Sud, Sud Formation, IS Aix.</td></tr>
<tr><td><strong>Lille</strong></td><td>E2LF · Institut Langues et Savoirs (ISPA)</td><td>Non relevé.</td></tr>
<tr><td><strong>Nice</strong></td><td>Alliance française Nice Côte d'Azur · Les Ateliers FL · FOLAM</td><td>Non relevé.</td></tr>
</tbody>
</table>
</div>

<p>Le maillage est dense : au 17 septembre 2026, la liste compte cinq centres en Moselle, cinq en
Seine-Maritime, trois dans le Loiret, trois dans le Puy-de-Dôme. Pour votre ville, la
<a href="%(liste)stcf" rel="noopener">liste officielle</a> reste la seule source complète ;
appelez ensuite le centre pour confirmer qu'il ouvre bien des sessions <em>IRN</em>.</p>

<h2 id="inscription">S'inscrire, pas à pas</h2>

<ol>
<li><strong>Vérifiez que c'est bien l'IRN qu'il vous faut.</strong> Naturalisation, carte de
résident, carte de séjour pluriannuelle : oui. Immigration au Canada : non, c'est le
<a href="/blog/ou-passer-le-tcf-canada-en-france/">TCF Canada</a>. Études : TCF tout public. Le
détail des niveaux exigés depuis janvier 2026 est dans notre guide du
<a href="/tcf-irn/">TCF IRN</a>.</li>
<li><strong>Choisissez le centre et la date</strong> sur son site — pas sur un comparateur. Les
sessions se remplissent, mais à Paris ou Lyon vous en trouverez une dans les deux à trois
semaines.</li>
<li><strong>Remplissez le formulaire en ligne et payez.</strong> Identité, nationalité, motif
(naturalisation, carte de résident…), date choisie, paiement par carte. ACTE confirme
l'inscription « dans les 72 heures » ; ACCORD la considère définitive « à réception du
règlement ». Le prix comprend souvent des frais non remboursables.</li>
<li><strong>Recevez la convocation</strong> une à deux semaines avant. Sans convocation à quinze
jours de la date, écrivez au centre.</li>
<li><strong>Le jour J</strong> : une <strong>pièce d'identité officielle en cours de validité,
avec photo</strong>, et la convocation. Les quatre épreuves s'enchaînent en une demi-journée, en
présentiel — c'est une exigence de l'arrêté qui encadre les tests de naturalisation.</li>
<li><strong>Récupérez l'attestation</strong> deux à trois semaines plus tard, par e-mail ou sur
place. C'est le seul document valable ; aucun duplicata n'est délivré par la plupart des
centres, conservez-le.</li>
</ol>

<h2 id="ordinateur">Sur papier ou sur ordinateur&nbsp;?</h2>

<p>Même test, même échelle, même attestation. Sur papier, vous répondez aux QCM sur une feuille
et rédigez l'expression écrite sur un livret ; sur ordinateur, les QCM et l'écrit se font sur un
poste fourni par le centre — ACTE précise que l'expression orale est identique dans les deux
cas. Deux différences pratiques : les centres sur ordinateur rendent souvent les résultats plus
vite (attestation provisoire immédiate pour les QCM chez ACCORD, définitive « sous 2 semaines » à
Montpellier), et il faut être à l'aise au clavier — l'Alliance française Aix-Marseille, qui ne
propose que l'ordinateur, prévient qu'elle ne remboursera pas un candidat qui découvre qu'il ne
sait pas s'en servir. Pas de correcteur orthographique.</p>

<h2 id="prix">Combien ça coûte</h2>

<div class="tablewrap">
<table>
<caption>Tarifs du TCF IRN affichés par les centres le 17 septembre 2026. Aucun tarif national n'existe ; ces prix changent sans préavis.</caption>
<thead><tr><th>Centre</th><th>Ville</th><th>TCF IRN</th></tr></thead>
<tbody>
<tr><td>ACTE</td><td>Paris 10<sup>e</sup></td><td><strong>140 €</strong></td></tr>
<tr><td>Etoile Institut</td><td>Paris 7<sup>e</sup></td><td><strong>160 €</strong> (170 € le samedi)</td></tr>
<tr><td>Alliance française de Lyon</td><td>Lyon</td><td><strong>169 €</strong></td></tr>
<tr><td>CLPS</td><td>Rennes, Brest, Saint-Brieuc, Vannes</td><td><strong>180 €</strong></td></tr>
<tr><td>Alliance française de Montpellier</td><td>Montpellier</td><td><strong>185 €</strong></td></tr>
<tr><td>ACCORD</td><td>Paris 15<sup>e</sup></td><td><strong>220 €</strong></td></tr>
</tbody>
</table>
</div>

<p>Le TCF IRN est <strong>éligible au CPF</strong> (fiche RS6643, valable jusqu'au 31 mai 2027) ;
notre article sur <a href="/blog/cpf-test-francais/">le CPF et les tests de français</a> explique
pourquoi les offres de Mon Compte Formation sont souvent des forfaits « préparation + examen » à
plus de 400 €, sans rapport avec le prix de l'examen seul. Et gardez en tête qu'<strong>un test
raté se repaie en entier</strong> : il n'existe aucune reprise partielle.</p>

<h2 id="civique">Et l'examen civique&nbsp;?</h2>

<p>Depuis le 1<sup>er</sup> janvier 2026, la naturalisation, la carte de résident et la carte de
séjour pluriannuelle exigent, en plus du niveau de français, la réussite à un <strong>examen
civique</strong> — un test distinct, conçu par le ministère de l'Intérieur, qui se passe lui aussi
dans un centre agréé, sur ordinateur, et qui figure désormais comme catégorie à part sur la carte
des centres de FEI. Beaucoup de centres TCF l'organisent : ACCORD à Paris (110 €, attestation
« sous 12 heures »), l'Alliance française de Montpellier (75 €), Espaces Formation à Nantes
(70 €, résultats « sous 12 heures »), l'Alliance française de Lyon. Le 17 septembre 2026,
l'Alliance française de Paris affichait : « Toutes nos sessions sont complètes pour le moment. »
Deux inscriptions, deux dates, deux attestations à joindre au dossier.</p>

<h2 id="pieges">Les pièges : « à distance », mauvais TCF, délais</h2>

<div class="warn"><strong>Aucun TCF ne se passe à distance.</strong> L'arrêté du 22 décembre 2025
exige, pour la naturalisation, quatre épreuves distinctes passées « en présentiel, en centre
d'examen, le même jour et en session unique », avec contrôle d'identité. Une attestation obtenue
« en ligne », « depuis chez vous » ou « avec un candidat partenaire » n'est pas un TCF : c'est
une fraude, invérifiable sur la plateforme d'authentification du ministère, et un délit.</div>

<ul>
<li><strong>Le mauvais TCF.</strong> Le TCF tout public à 80-120 € (« trois QCM ») ne prouve ni
l'écrit ni l'oral : les préfectures le refusent. Un TCF Canada ou Québec n'est pas fait pour un
dossier français. Cherchez « IRN » sur votre convocation.</li>
<li><strong>Le délai entre deux passations.</strong> FEI annonce 20 jours sur ses pages et 30 sur
plusieurs de ses fiches ; l'Alliance française de Lyon applique « un délai minimum de 20 jours ».
Si vous devez repasser, prévoyez 30 jours et lisez <a href="/blog/repasser-tcf-tef/">repasser le
TCF : délais et reprise</a>.</li>
<li><strong>La validité.</strong> Deux ans à compter de la délivrance. Un dossier déposé tard avec
une attestation ancienne peut être rejeté : <a href="/blog/validite-attestation-tcf-tef/">deux ans
à partir de quand&nbsp;?</a></li>
<li><strong>Le niveau.</strong> Depuis 2026, la naturalisation exige le <strong>B2</strong> à
l'oral comme à l'écrit, sur une échelle qui plafonne à 499. S'inscrire « pour voir » coûte une
session entière. Un <a href="/examens-blancs/">examen blanc noté au format IRN</a> coûte une
matinée ; une seconde session coûte 140 à 220 €.</li>
<li><strong>Le diplôme, plutôt ?</strong> Si vous avez trois mois devant vous, le
<a href="/blog/ou-passer-le-delf-en-france/">DELF B2</a> ne périme jamais — mais il faut attraper
une session et une fenêtre d'inscription. Pour trancher : <a href="/blog/diplome-ou-test-delf-tcf/">diplôme
ou test&nbsp;?</a></li>
</ul>
""" % {"liste": FEI_LISTE, "serie": serie("/blog/ou-passer-le-tcf-irn-en-france/")},
    "cta_h2": "Le B2 avant de payer la session",
    "cta_p": """Un TCF IRN se passe presque chaque semaine, mais se repaie en entier à chaque tentative,
avec 20 à 30 jours d'attente. Les examens blancs de l'app «&nbsp;TCF DELF TEF&nbsp;: Tests
2026&nbsp;» reproduisent les quatre épreuves au format IRN, notées sur 499 avec le niveau
atteint, et corrigent votre écrit et votre oral sur les critères du test.""",
    "faq": [
        ("Où passer le TCF IRN à Paris&nbsp;?",
         "Dans l'un des sept centres agréés de la liste de France Éducation international. Le 17 septembre 2026, ACTE (10e) proposait une session presque chaque semaine à 140 €, ACCORD (15e) deux par mois à 220 € sur ordinateur, Etoile Institut (7e) à 160 € en semaine et 170 € le samedi ; les Cours de civilisation française de la Sorbonne, l'Alliance française Paris Île-de-France, ELFE et ILE International sont aussi agréés."),
        ("Combien coûte le TCF IRN&nbsp;?",
         "Il n'existe aucun tarif national. Sur les centres relevés le 17 septembre 2026 : 140 € chez ACTE et 220 € chez ACCORD à Paris, 160 € chez Etoile Institut, 169 € à l'Alliance française de Lyon, 180 € au CLPS de Rennes, 185 € à l'Alliance française de Montpellier. Le test est éligible au CPF."),
        ("Le TCF IRN se passe-t-il sur papier ou sur ordinateur&nbsp;?",
         "Les deux existent et donnent la même attestation ; c'est le centre qui propose l'un, l'autre ou les deux. Sur ordinateur, les QCM et l'expression écrite se font sur un poste du centre, et les résultats sont souvent plus rapides — attestation provisoire immédiate pour les QCM dans certains centres, définitive sous deux semaines. Sans correcteur orthographique."),
        ("Combien de temps pour recevoir l'attestation&nbsp;?",
         "Deux à trois semaines dans la plupart des centres relevés : « au minimum 3 semaines » chez ACTE, « sous 2 semaines » à l'Alliance française de Montpellier sur ordinateur, « entre 10 jours et 3 semaines » chez KLF, 2 à 3 semaines à l'Alliance française de Lyon et à Espaces Formation. L'attestation est ensuite valable deux ans."),
        ("Peut-on passer le TCF IRN en ligne&nbsp;?",
         "Non. Pour la naturalisation, l'arrêté du 22 décembre 2025 impose quatre épreuves passées en présentiel, en centre d'examen, le même jour et en session unique, avec contrôle d'identité. Toute offre de TCF « à distance » ou « sans se déplacer » est une fraude, et son attestation ne sera pas authentifiable par la préfecture."),
        ("Quel délai pour repasser le TCF IRN&nbsp;?",
         "France Éducation international indique 20 jours sur ses pages de test et 30 jours sur plusieurs de ses fiches ; les centres appliquent généralement 20 jours. Aucune reprise partielle n'existe : on repasse les quatre épreuves et on repaie le tarif complet. Faites confirmer le délai par votre centre avant de vous réinscrire."),
        ("L'examen civique se passe-t-il au même endroit&nbsp;?",
         "C'est un examen distinct, obligatoire depuis le 1er janvier 2026 pour la naturalisation, la carte de résident et la carte pluriannuelle, passé sur ordinateur dans un centre agréé. Beaucoup de centres TCF l'organisent aussi — 110 € chez ACCORD à Paris, 75 € à l'Alliance française de Montpellier, 70 € à Espaces Formation à Nantes — mais il faut une inscription séparée, et les sessions affichent vite complet."),
    ],
    "also": [
        ("/tcf-irn/", "TCF IRN : le test de français pour votre naturalisation", "Niveaux exigés depuis 2026, format des quatre épreuves, échelle sur 499, prix et CPF."),
        ("/blog/tcf-irn-ou-tef-irn/", "TCF IRN ou TEF IRN : le comparatif", "Même usage, même échelle, deux réseaux de centres — et un test adaptatif de l'autre côté."),
        ("/blog/exercices-tcf-irn/", "Exercices TCF IRN : les 4 épreuves corrigées", "Un exercice corrigé par épreuve, au niveau B2 exigé pour la naturalisation."),
        ("/blog/ou-passer-le-delf-en-france/", "Où passer le DELF en France&nbsp;?", "Le diplôme valable à vie : 143 centres, dix sessions par an, et des fenêtres d'inscription à ne pas manquer."),
    ],
    "sources": """<strong>Sources.</strong> Liste des centres de passation TCF de France Éducation
international (filtre « France ») et page « TCF IRN », consultées le 17 septembre 2026 ; pages
et formulaires d'inscription d'ACTE (calendriers papier et ordinateur, inscription TCF IRN),
grille « Tarifs 2026 des examens » et « Calendrier examens TCF septembre-novembre 2026 » d'ACCORD
(examensparis.fr), page tarifs d'Etoile Institut, produits TCF de l'Alliance française de Lyon,
page tarifs de l'Alliance française de Montpellier, pages TCF de l'Alliance française Aix-Marseille
Provence, de l'Alliance française Strasbourg Europe, de KLF, d'Espaces Formation et du CLPS,
consultées le 17 septembre 2026 ; arrêté du 22 décembre 2025 (critères des tests linguistiques).
Ces prix et dates changent sans préavis : vérifiez-les sur le site de votre centre.""",
}


# ---------------------------------------------------------------------------
# 3. Où passer le TCF Canada en France ?
# ---------------------------------------------------------------------------
CAN_FR = {
    "slug": "ou-passer-le-tcf-canada-en-france",
    "accent": "accent-tcf",
    "crumb": "Où passer le TCF Canada en France",
    "title": "Où passer le TCF Canada en France ? Centres et inscription",
    "desc": "Les centres agréés qui proposent le TCF Canada à Paris et en région, leurs prix de 195 à 285 €, leurs sessions mensuelles et le pas-à-pas d'inscription.",
    "og_title": "Où passer le TCF Canada en France ? Centres et inscription",
    "og_desc": "Les centres qui proposent le TCF Canada à Paris et en région, leurs prix de 195 à 285 €, leurs dates et le pas-à-pas d'inscription.",
    "h1": "Où passer le TCF Canada en France&nbsp;? Les centres, les prix et l'inscription",
    "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": 10,
    "intro": """Le TCF Canada se passe en France dans un <strong>centre agréé par France Éducation
international qui a choisi d'organiser cette déclinaison</strong> — ce n'est pas le cas des
251 centres TCF du pays. À Paris, au moins trois centres le proposent <strong>chaque mois</strong> ;
en région, les Alliances françaises de Lyon, Montpellier ou Aix-Marseille, les centres KLF, CLPS…
Comptez <strong>195 à 285 €</strong>, une inscription <strong>en ligne</strong> qui ferme quelques
jours avant la session, et <strong>deux à trois semaines</strong> pour l'attestation.""",
    "facts": [
        "<strong>Pas tous les centres TCF</strong> : Etoile Institut à Paris ou l'Alliance française de Strasbourg n'organisent pas le TCF Canada. Cherchez « TCF Canada » sur la page du centre.",
        "Prix libre : <strong>195 € (ACTE, Paris) à 285 € (CLPS, Rennes et Brest)</strong> ; 200 € à Montpellier, 220 € à Lyon et chez ACCORD, 240 € à Aix-Marseille.",
        "Sessions <strong>mensuelles</strong> dans chaque centre relevé — donc plusieurs par mois à Paris — et <strong>complètes tôt</strong> : à Lyon, celles de septembre l'étaient le 17 septembre.",
        "<strong>Sur ordinateur</strong> dans la plupart des centres (Aix-Marseille : ordinateur uniquement) ; ACTE propose le papier.",
        "Résultats en <strong>2 à 3 semaines</strong> ; attestation valable <strong>2 ans</strong>, et IRCC veut des résultats de moins de 2 ans au dépôt.",
        "⚠️ Depuis les sessions du <strong>1<sup>er</sup> septembre 2026</strong>, FEI n'accepte plus de demande de recorrection.",
    ],
    "toc": [
        ("reseau", "Quels centres proposent le TCF Canada"),
        ("paris", "À Paris : trois centres relevés"),
        ("villes", "En région : les centres relevés"),
        ("calendrier", "Les dates de session relevées"),
        ("inscription", "S'inscrire, pas à pas"),
        ("prix", "Combien ça coûte"),
        ("pieges", "Les pièges : mauvais TCF, délais, recorrection"),
    ],
    "body": """
<h2 id="reseau">Quels centres proposent le TCF Canada</h2>

<p>Le <a href="/tcf-canada/">TCF Canada</a> est l'un des deux tests acceptés par Immigration,
Réfugiés et Citoyenneté Canada pour prouver son français — l'autre est le TEF Canada. Il est conçu
par France Éducation international et <strong>organisé par des centres agréés</strong> qui décident,
chacun, des déclinaisons qu'ils ouvrent. La liste officielle de FEI compte 251 centres TCF en
France au 17 septembre 2026, mais elle ne dit pas lesquels font passer le <em>Canada</em> : il
faut lire la page du centre. Sur ceux que nous avons ouverts, l'Alliance française de Strasbourg et
Etoile Institut (Paris) n'en proposent pas ; ACTE, ACCORD, les Alliances françaises de Lyon, de
Montpellier et d'Aix-Marseille, KLF, CLPS et Espaces Formation, oui.</p>

<p>Trois conséquences pratiques. Le TCF Canada est <strong>moins fréquent que le TCF IRN</strong> :
mensuel là où l'IRN est hebdomadaire. Il se passe <strong>surtout sur ordinateur</strong>. Et les
places se prennent tôt, parce qu'un dossier Entrée express a une date et que les candidats
s'inscrivent dès l'ouverture. La <a href="%(liste)stcf" rel="noopener">liste des centres agréés</a>
reste le point de départ : si un organisme n'y figure pas, son « TCF Canada » ne sera pas reconnu
par IRCC.</p>

%(serie)s

<h2 id="paris">À Paris : trois centres relevés</h2>

<div class="tablewrap wide">
<table>
<caption>Centres parisiens dont le site affichait un TCF Canada le 17 septembre 2026. Les quatre autres centres TCF de Paris (Cours de civilisation française de la Sorbonne, Alliance française Paris Île-de-France, ELFE, ILE International) sont à vérifier sur leur site.</caption>
<thead><tr><th>Centre</th><th>TCF Canada</th><th>Sessions et inscription</th></tr></thead>
<tbody>
<tr><td><strong>ACTE</strong> (10<sup>e</sup>)</td><td><strong>195 €</strong> sur papier (45 € de frais d'inscription non remboursables inclus) ; version ordinateur aussi</td><td>Papier : <strong>4 novembre et 2 décembre 2026</strong>. Résultats « au minimum 3 semaines » après, attestation par e-mail ou à retirer sur place.</td></tr>
<tr><td><strong>ACCORD</strong> (15<sup>e</sup>, examensparis.fr)</td><td><strong>220 €</strong> sur ordinateur</td><td><strong>23 septembre et 28 octobre 2026</strong> ; inscription par bulletin envoyé par e-mail, close cinq jours avant ; paiement par carte ou espèces. Attestation provisoire immédiate pour les compréhensions, définitive sous 2 semaines.</td></tr>
<tr><td><strong>Etoile Institut</strong> (7<sup>e</sup>)</td><td>—</td><td>Propose le TCF Québec, le TEF Canada et le TEFAQ, pas le TCF Canada (page tarifs du 17 septembre 2026).</td></tr>
</tbody>
</table>
</div>

<h2 id="villes">En région : les centres relevés</h2>

<div class="tablewrap wide">
<table>
<caption>Centres proposant le TCF Canada en région, avec les informations lues sur leur site le 17 septembre 2026.</caption>
<thead><tr><th>Ville</th><th>Centre</th><th>TCF Canada relevé</th></tr></thead>
<tbody>
<tr><td><strong>Lyon</strong></td><td>Alliance française de Lyon</td><td><strong>220 €</strong> ; une session par mois — 21 octobre, 25 novembre, 16 décembre 2026 encore ouvertes le 17 septembre, celles des 10 et 23 septembre complètes ; inscriptions closes 48 h avant ; résultats par courriel sous 2 à 3 semaines. Aussi : KLF Lyon.</td></tr>
<tr><td><strong>Montpellier</strong></td><td>Alliance française de Montpellier</td><td><strong>200 €</strong> sur ordinateur ; 23 septembre (inscription jusqu'au 13) et 13 novembre 2026 (jusqu'au 3 novembre) ; résultats définitifs sous 2 semaines. Aussi : KLF Montpellier.</td></tr>
<tr><td><strong>Marseille · Aix</strong></td><td>Alliance française Aix-Marseille Provence</td><td><strong>60 € par épreuve, soit 240 €</strong> ; sur ordinateur uniquement ; inscription deux semaines à l'avance ; résultats en 15 jours ; 20 jours minimum entre deux examens.</td></tr>
<tr><td><strong>Rennes · Brest</strong></td><td>CLPS L'Enjeu Compétences</td><td><strong>285 €</strong> ; inscription par fiche en ligne ; TCF Canada à Rennes et à Brest.</td></tr>
<tr><td><strong>Nantes</strong></td><td>Espaces Formation</td><td>Papier ou ordinateur, inscription et paiement en ligne, résultats sous 2 à 3 semaines.</td></tr>
<tr><td><strong>Bordeaux · Toulouse · Annecy</strong></td><td>KLF (klf-examen.fr)</td><td>Sur ordinateur (papier à Annecy) ; résultats « entre 10 jours et 3 semaines » ; attestation à retirer au centre.</td></tr>
<tr><td><strong>Strasbourg</strong></td><td>Alliance française Strasbourg Europe</td><td>Pas de TCF Canada — IRN et tout public seulement. Voir CIEL et Stralang.</td></tr>
</tbody>
</table>
</div>

<h2 id="calendrier">Les dates de session relevées</h2>

<p>Il n'existe pas de calendrier national du TCF Canada : chaque centre publie le sien. Au
17 septembre 2026, voici ce qui restait ouvert d'ici la fin de l'année dans les centres relevés
— à confirmer sur leur site, les places partent.</p>

<div class="tablewrap wide">
<table>
<caption>Sessions de TCF Canada affichées par les centres le 17 septembre 2026. Une session indiquée « complète » l'était ce jour-là.</caption>
<thead><tr><th>Centre</th><th>Septembre</th><th>Octobre</th><th>Novembre</th><th>Décembre</th></tr></thead>
<tbody>
<tr><td>ACTE, Paris (papier)</td><td>—</td><td>—</td><td>4 nov.</td><td>2 déc.</td></tr>
<tr><td>ACCORD, Paris (ordinateur)</td><td>23 sept.</td><td>28 oct.</td><td>calendrier suivant</td><td>calendrier suivant</td></tr>
<tr><td>AF Lyon</td><td>10 et 23 sept. (complètes)</td><td>21 oct.</td><td>25 nov.</td><td>16 déc.</td></tr>
<tr><td>AF Montpellier</td><td>23 sept.</td><td>—</td><td>13 nov.</td><td>—</td></tr>
</tbody>
</table>
</div>

<p>Lecture : un candidat parisien qui découvre le 20 septembre qu'il lui faut un TCF Canada
trouve encore ACCORD le 28 octobre et ACTE le 4 novembre ; un Lyonnais attend le 21 octobre. Un
mois d'attente, c'est un mois de préparation — c'est exactement le temps qu'il faut pour
travailler le format des <a href="/blog/exercices-comprehension-orale-tcf-canada/">39 questions
d'écoute</a> et des <a href="/blog/sujets-expression-ecrite-tcf-canada/">trois tâches d'écrit</a>.</p>

<h2 id="inscription">S'inscrire, pas à pas</h2>

<ol>
<li><strong>Vérifiez que c'est le TCF <em>Canada</em> qu'il vous faut</strong> — pas le TCF tout
public, refusé par IRCC, ni le TCF Québec, réservé aux programmes du Québec. Le TEF Canada est
l'alternative : <a href="/blog/tcf-ou-tef-canada/">TCF ou TEF Canada, lequel choisir&nbsp;?</a></li>
<li><strong>Fixez le score à atteindre avant de choisir la date.</strong> Pour Entrée express, le
NCLC 7 demande 458 en compréhension orale et 453 à l'écrit — le détail est dans
<a href="/blog/tcf-canada-nclc-7/">NCLC 7 au TCF Canada</a>. Un examen blanc noté sur 699 vous
dit si un mois suffit ou s'il en faut trois.</li>
<li><strong>Repérez le centre sur la liste FEI, puis sa page « TCF Canada ».</strong> Comparez
les dates ouvertes et le mode (papier ou ordinateur) plutôt que le prix : l'écart maximal relevé
est de 90 €, une session manquée coûte un mois.</li>
<li><strong>Inscrivez-vous en ligne et payez</strong> — formulaire du centre, pièce d'identité,
paiement par carte. La date limite va de 48 heures (Lyon) à dix jours (Montpellier) avant la
session ; ACCORD ferme cinq jours avant. Les frais d'inscription sont en général non
remboursables.</li>
<li><strong>Convocation</strong> une à deux semaines avant, avec l'horaire de l'oral. Réservez la
journée : les quatre épreuves durent 2 h 47 au total, mais l'expression orale est planifiée à
part.</li>
<li><strong>Le jour J</strong> : pièce d'identité officielle valide avec photo — de préférence le
passeport que vous utiliserez dans votre dossier IRCC, pour que l'identité de l'attestation
corresponde — et la convocation. Sur ordinateur, le clavier est fourni par le centre ; pas de
correcteur orthographique.</li>
<li><strong>Attestation</strong> deux à trois semaines après. Vérifiez immédiatement l'orthographe
de vos nom, prénom et date de naissance : c'est ce document, tel quel, qu'IRCC lira.</li>
</ol>

<h2 id="prix">Combien ça coûte</h2>

<div class="tablewrap">
<table>
<caption>Tarifs du TCF Canada affichés par les centres le 17 septembre 2026. Aucun tarif national ; ces prix changent sans préavis.</caption>
<thead><tr><th>Centre</th><th>Ville</th><th>TCF Canada</th></tr></thead>
<tbody>
<tr><td>ACTE</td><td>Paris 10<sup>e</sup></td><td><strong>195 €</strong> (papier)</td></tr>
<tr><td>Alliance française de Montpellier</td><td>Montpellier</td><td><strong>200 €</strong></td></tr>
<tr><td>ACCORD</td><td>Paris 15<sup>e</sup></td><td><strong>220 €</strong></td></tr>
<tr><td>Alliance française de Lyon</td><td>Lyon</td><td><strong>220 €</strong></td></tr>
<tr><td>Alliance française Aix-Marseille Provence</td><td>Marseille, Aix</td><td><strong>240 €</strong> (4 × 60 €)</td></tr>
<tr><td>CLPS</td><td>Rennes, Brest</td><td><strong>285 €</strong></td></tr>
</tbody>
</table>
</div>

<p>De 195 € à 285 € pour le même test — et au Canada, 390 à 440 $CA, comme le montre notre guide
<a href="/blog/ou-passer-le-tcf-canada-au-canada/">où passer le TCF Canada au Canada</a>. Le TCF
Canada n'est <strong>pas éligible au CPF</strong>, contrairement au TCF IRN et au TCF tout public.
Et il n'existe aucune reprise partielle : un score insuffisant à une seule épreuve, c'est quatre
épreuves à repasser et le tarif complet à repayer.</p>

<h2 id="pieges">Les pièges : mauvais TCF, délais, recorrection</h2>

<div class="warn"><strong>Plus de recorrection depuis le 1<sup>er</sup> septembre 2026.</strong>
L'Alliance française de Toronto l'annonce sur sa page TCF : « France Education International will
no longer accept requests for recorrection for exam sessions held on or after September 1,
2026 » ; l'Alliance française de Montpellier précise que le dispositif est « suspendu
temporairement » avec une reprise « prévue à l'automne 2027 ». Concrètement : le score que vous
recevez est définitif, et la seule façon de l'améliorer est de repasser le test.</div>

<ul>
<li><strong>Le mauvais TCF.</strong> Un TCF tout public, même complet avec ses cinq épreuves, ne
vaut rien pour IRCC ; un TCF Québec non plus. Vérifiez la mention <em>Canada</em> sur la
convocation et sur l'attestation.</li>
<li><strong>Le délai entre deux passations.</strong> 20 jours selon les pages de FEI, 30 selon
plusieurs de ses fiches ; l'Alliance française Aix-Marseille applique « un délai minimum de
20 jours ». Détails dans <a href="/blog/repasser-tcf-tef/">repasser le TCF ou le TEF</a>.</li>
<li><strong>La double règle des deux ans.</strong> L'attestation vaut deux ans, et IRCC exige des
résultats de moins de deux ans au moment de créer le profil <em>et</em> au dépôt de la demande :
<a href="/blog/validite-attestation-tcf-tef/">deux ans à partir de quand&nbsp;?</a></li>
<li><strong>Le B2 qui n'est pas un NCLC 7.</strong> Un « B2 » sur l'attestation peut ne valoir que
NCLC 6 en compréhension orale : ce qu'IRCC lit, c'est le score sur 699 converti en NCLC, pas la
lettre.</li>
<li><strong>Le prix comme critère.</strong> 90 € d'écart entre le centre le moins cher et le plus
cher relevés, contre un mois perdu si vous attendez la session « bon marché » qui est déjà
complète.</li>
</ul>
""" % {"liste": FEI_LISTE, "serie": serie("/blog/ou-passer-le-tcf-canada-en-france/")},
    "cta_h2": "Le score, avant la date",
    "cta_p": """Un TCF Canada se repaie en entier et son score est désormais définitif. Les examens
blancs de l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent les quatre épreuves
au format officiel, notées sur 699 et converties en NCLC, avec la correction IA de l'écrit et de
l'oral — pour savoir, avant de payer 195 à 285 €, si la session du mois prochain est la bonne.""",
    "faq": [
        ("Où passer le TCF Canada à Paris&nbsp;?",
         "Sur les sept centres TCF agréés de Paris, trois affichaient un TCF Canada le 17 septembre 2026 : ACTE (10e) à 195 € sur papier, avec des sessions les 4 novembre et 2 décembre 2026 ; ACCORD (15e) à 220 € sur ordinateur, les 23 septembre et 28 octobre ; les Cours de civilisation française de la Sorbonne, l'Alliance française Paris Île-de-France, ELFE et ILE International sont agréés mais à vérifier. Etoile Institut ne le propose pas."),
        ("Combien coûte le TCF Canada en France&nbsp;?",
         "Il n'existe aucun tarif national. Sur les centres relevés le 17 septembre 2026 : 195 € chez ACTE à Paris, 200 € à l'Alliance française de Montpellier, 220 € chez ACCORD et à l'Alliance française de Lyon, 240 € à l'Alliance française Aix-Marseille (60 € par épreuve), 285 € au CLPS de Rennes et Brest. Le TCF Canada n'est pas éligible au CPF."),
        ("Tous les centres TCF proposent-ils le TCF Canada&nbsp;?",
         "Non. La liste officielle de France Éducation international recense les centres agréés TCF sans préciser leurs déclinaisons ; chaque centre choisit celles qu'il organise. L'Alliance française de Strasbourg et Etoile Institut à Paris, par exemple, ne proposent pas le TCF Canada. Vérifiez la mention « TCF Canada » sur la page du centre avant de vous inscrire."),
        ("Le TCF Canada se passe-t-il sur ordinateur&nbsp;?",
         "Dans la plupart des centres relevés, oui : ACCORD, les Alliances françaises de Lyon, de Montpellier et d'Aix-Marseille (ordinateur uniquement), KLF. ACTE à Paris et Espaces Formation à Nantes proposent aussi le papier. L'attestation est la même ; sur ordinateur, les résultats arrivent souvent plus vite, et il faut être à l'aise au clavier, sans correcteur orthographique."),
        ("Combien de temps pour recevoir les résultats&nbsp;?",
         "Deux à trois semaines dans les centres relevés : « au minimum 3 semaines » chez ACTE, « sous 2 semaines » à Montpellier, 15 jours à Aix-Marseille, 2 à 3 semaines à Lyon, « entre 10 jours et 3 semaines » chez KLF. L'attestation est valable deux ans à compter de sa délivrance."),
        ("Peut-on demander une recorrection du TCF Canada&nbsp;?",
         "Plus depuis les sessions du 1er septembre 2026 : France Éducation international n'accepte plus de demande de recorrection, comme l'indiquent l'Alliance française de Toronto et l'Alliance française de Montpellier, qui annonce une reprise du dispositif à l'automne 2027. Le score reçu est définitif ; pour l'améliorer, il faut repasser les quatre épreuves après le délai de 20 à 30 jours."),
        ("Peut-on passer le TEF Canada à la place&nbsp;?",
         "Oui, c'est l'autre test accepté par IRCC, organisé par Le français des affaires (CCI Paris Île-de-France) dans son propre réseau de centres — souvent les mêmes Alliances françaises. Les deux tests ont des formats différents et deux tables de conversion NCLC distinctes ; notre comparatif TCF ou TEF Canada les met côte à côte."),
    ],
    "also": [
        ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", "Les quatre épreuves, la conversion NCLC, les seuils pour Entrée express."),
        ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", "458 en compréhension orale, 453 à l'écrit, 10/20 en expression — et pourquoi un B2 ne vaut pas toujours NCLC 7."),
        ("/blog/ou-passer-le-tcf-canada-au-canada/", "Où passer le TCF Canada au Canada&nbsp;?", "Les 47 centres agréés, de Montréal à Iqaluit, et comment obtenir une place."),
        ("/blog/prix-tcf-tef/", "Combien coûte vraiment le TCF ou le TEF&nbsp;?", "Aucun tarif national : les prix relevés centre par centre, en France et au Canada."),
    ],
    "sources": """<strong>Sources.</strong> Liste des centres de passation TCF de France Éducation
international (filtre « France »), consultée le 17 septembre 2026 ; pages et formulaires
d'inscription TCF Canada d'ACTE, grille « Tarifs 2026 » et calendrier septembre-novembre 2026
d'ACCORD (examensparis.fr), page tarifs d'Etoile Institut, produit « Examen TCF Canada » de
l'Alliance française de Lyon, pages tarifs et TCF Canada de l'Alliance française de Montpellier,
page « TCF Québec et Canada » de l'Alliance française Aix-Marseille Provence, pages TCF de KLF,
d'Espaces Formation, du CLPS et de l'Alliance française Strasbourg Europe, page TCF de
l'Alliance française de Toronto (fin des recorrections), consultées le 17 septembre 2026.
Ces prix et dates changent sans préavis : vérifiez-les sur le site de votre centre.""",
}


# ---------------------------------------------------------------------------
# 4. Où passer le TCF Canada au Canada ?
# ---------------------------------------------------------------------------
CAN_CA = {
    "slug": "ou-passer-le-tcf-canada-au-canada",
    "accent": "accent-tcf",
    "crumb": "Où passer le TCF Canada au Canada",
    "title": "Où passer le TCF Canada au Canada ? Centres et inscription",
    "desc": "47 centres agréés de Montréal à Iqaluit, des sessions complètes en minutes, 390 à 440 $ : où passer le TCF Canada au Canada et comment obtenir une place.",
    "og_title": "Où passer le TCF Canada au Canada ? Les 47 centres agréés",
    "og_desc": "47 centres agréés, de Montréal à Iqaluit, des sessions complètes en quelques minutes, 390 à 440 $ : où passer le TCF Canada et comment obtenir une place.",
    "h1": "Où passer le TCF Canada au Canada&nbsp;? Les 47 centres agréés et l'inscription",
    "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": 11,
    "intro": """Au Canada, le TCF Canada se passe dans l'un des <strong>47 centres agréés</strong> par France
Éducation international — le réseau des Alliances françaises, des universités et des cégeps —,
présents dans <strong>neuf provinces et au Nunavut</strong>. Montréal en compte sept, Toronto quatre
sites. On s'inscrit <strong>en ligne, centre par centre</strong>, entre <strong>390 et 440 $CA</strong>,
et la vraie difficulté n'est pas le prix : c'est la <strong>place</strong>, les sessions se
remplissant en quelques minutes à Toronto et Vancouver.""",
    "facts": [
        "<strong>47 centres agréés</strong> au Canada (liste FEI du 17 septembre 2026), dont 44 avec des sessions sur ordinateur : 23 au Québec, 7 en Ontario, 5 en Colombie-Britannique, 3 en Alberta, 2 en Saskatchewan, 3 au Nouveau-Brunswick, 1 au Manitoba, en Nouvelle-Écosse, à Terre-Neuve et au Nunavut.",
        "Prix libre et <strong>souvent non publié</strong> : 390 $ à l'Alliance française de Vancouver, 400 $ à Edmonton, 440 $ à l'UQTR ; l'Alliance française de Montréal n'affiche aucun tarif.",
        "⚠️ <strong>Les places partent en minutes.</strong> À Toronto, sessions trimestrielles, inscription ouverte un mois avant à 10 h — « si une session n'est pas listée, elle est complète », pas de liste d'attente. À Vancouver, toutes les sessions affichaient complet le 17 septembre.",
        "Inscription <strong>en ligne uniquement</strong>, définitive : annulation à plus de 15 jours moyennant 75 $ (Montréal) ou 15 $ par épreuve (Stanislas), rien en deçà.",
        "<strong>20 jours</strong> minimum entre deux passations, « quel que soit le centre » ; résultats en <strong>2 à 4 semaines</strong> ; attestation valable 2 ans.",
        "Depuis les sessions du 1<sup>er</sup> septembre 2026, <strong>plus aucune recorrection</strong> : le score est définitif.",
    ],
    "toc": [
        ("reseau", "47 centres, neuf provinces et le Nunavut"),
        ("montreal", "Montréal et le Québec"),
        ("ontario", "Toronto, Ottawa et l'Ontario"),
        ("ouest", "Vancouver, Calgary, Edmonton et les Prairies"),
        ("est", "Provinces atlantiques et Nunavut"),
        ("place", "Obtenir une place : comment font ceux qui y arrivent"),
        ("inscription", "S'inscrire, pas à pas"),
        ("prix", "Combien ça coûte"),
        ("pieges", "Les pièges : TCF Québec, annulation, recorrection"),
    ],
    "body": """
<h2 id="reseau">47 centres, neuf provinces et le Nunavut</h2>

<p>La liste officielle de France Éducation international recense, au 17 septembre 2026,
<strong>48 entrées « Canada »</strong> — 47 centres distincts, l'un d'eux apparaissant deux fois.
Trois familles : les <strong>Alliances françaises</strong> (Montréal, Toronto et ses campus,
Ottawa, Vancouver, Victoria, Calgary, Edmonton, Winnipeg, Halifax, Moncton), les
<strong>universités et cégeps</strong> (UQAM, Concordia, Laval, UQTR, UQAC, UQAT, Sherbrooke,
Memorial, Lethbridge, Victoria, Cégep Marie-Victorin, de la Gaspésie…) et des <strong>écoles et
centres de formation</strong> (Collège Stanislas, Collège Mathieu, FrancoLangues, Ashton
Testing…). Quarante-quatre proposent des sessions sur ordinateur.</p>

<p>Ce que la liste ne dit pas : <strong>quelles déclinaisons</strong> chaque centre organise, ni
<strong>quand</strong>, ni <strong>à quel prix</strong>. Au Canada, presque tous font passer le
TCF Canada et le TCF Québec ; le tout public et l'IRN sont plus rares. Les tableaux ci-dessous
reprennent la liste officielle, province par province, avec ce que nous avons lu sur les sites
des principaux centres le 17 septembre 2026. La liste complète, avec adresses et téléphones, est
<a href="https://www.france-education-international.fr/centres-d-examen/liste?pays=112&type-centre=tcf" rel="noopener">sur le site de FEI</a>.</p>

%(stats)s

%(serie)s

<h2 id="montreal">Montréal et le Québec</h2>

<p>Vingt-trois centres au Québec, dont sept dans Montréal — c'est, de loin, la ville la mieux
dotée du pays. Attention au vocabulaire local : le « TCF pour le Québec » (TCF Q) sert aux
programmes du <a href="/tcf-quebec/">ministère de l'Immigration du Québec</a> ; le TCF
<em>Canada</em>, lui, est le test d'IRCC, et il est aussi reconnu par le MIFI « depuis fin
janvier 2022 », rappelle l'Alliance française de Montréal.</p>

<div class="tablewrap wide">
<table>
<caption>Centres TCF agréés au Québec (liste FEI du 17 septembre 2026). SO = sessions sur ordinateur disponibles.</caption>
<thead><tr><th>Ville</th><th>Centre</th><th>SO</th><th>Relevé le 17 septembre 2026</th></tr></thead>
<tbody>
<tr><td rowspan="7"><strong>Montréal</strong></td><td>Alliance Française de Montréal (Vieux-Montréal)</td><td><span class="badge ok">oui</span></td><td><strong>Aucun tarif publié</strong> ; inscription en ligne « dans la limite des places disponibles » ; 75 $ retenus si annulation à plus de 15 jours, rien après ; horaires envoyés 7 jours avant, « réserver la journée entière ».</td></tr>
<tr><td>Collège Stanislas (Outremont)</td><td><span class="badge ok">oui</span></td><td>TCF Québec, Canada, tout public et IRN ; 15 $ retenus par épreuve si annulation à plus de 15 jours ; « 20 jours entre deux passations, quel que soit le centre ».</td></tr>
<tr><td>UQAM – francisation</td><td><span class="badge ok">oui</span></td><td>TCF Canada ; inscription en ligne.</td></tr>
<tr><td>Université Concordia</td><td><span class="badge ok">oui</span></td><td>Page « TCF test » du centre.</td></tr>
<tr><td>Cégep Marie-Victorin</td><td><span class="badge ok">oui</span></td><td>Formation continue.</td></tr>
<tr><td>Centre Yves-Thériault (CSSDM)</td><td><span class="badge ok">oui</span></td><td>Centre d'éducation des adultes.</td></tr>
<tr><td>Collège ELC (Jean-Talon)</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td rowspan="2"><strong>Québec</strong></td><td>Collège Stanislas (Sainte-Foy)</td><td><span class="badge ok">oui</span></td><td>Mêmes règles qu'à Montréal.</td></tr>
<tr><td>Université Laval (ELUL)</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>Trois-Rivières · Drummondville</strong></td><td>École internationale de français – UQTR</td><td><span class="badge ok">oui</span></td><td>TCF Canada <strong>440 $</strong> ; TCF Québec à la carte 105 $ (CO, CE, EE) et 125 $ (EO) — relevé le 30 juillet 2026.</td></tr>
<tr><td><strong>Laval</strong></td><td>Centre de formation Les Berges</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>Kirkland</strong></td><td>Kuper Academy</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>Saint-Constant</strong></td><td>Complexe X</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>Sherbrooke</strong></td><td>Centre de langues – Université de Sherbrooke</td><td><span class="badge no">non</span></td><td>Papier.</td></tr>
<tr><td><strong>Chicoutimi</strong></td><td>UQAC</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>Rouyn-Noranda</strong></td><td>UQAT – formation continue</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>Saint-Félicien · Chibougamau</strong></td><td>Cégep de Saint-Félicien</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>Gaspé</strong></td><td>Cégep de la Gaspésie et des Îles</td><td><span class="badge ok">oui</span></td><td>Listé deux fois par FEI.</td></tr>
<tr><td><strong>Sept-Îles</strong></td><td>Centre alpha LIRA</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>Baie-Comeau</strong></td><td>Maison Alpha ABC Côte-Nord</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>La Pocatière</strong></td><td>Collège de Sainte-Anne-de-la-Pocatière</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
</tbody>
</table>
</div>

<h2 id="ontario">Toronto, Ottawa et l'Ontario</h2>

<div class="tablewrap wide">
<table>
<caption>Centres TCF agréés en Ontario (liste FEI du 17 septembre 2026).</caption>
<thead><tr><th>Ville</th><th>Centre</th><th>SO</th><th>Relevé le 17 septembre 2026</th></tr></thead>
<tbody>
<tr><td><strong>Toronto</strong></td><td>Alliance française de Toronto – campus Spadina</td><td><span class="badge ok">oui</span></td><td rowspan="4">Quatre sites, papier ou ordinateur ; <strong>sessions trimestrielles</strong>, inscription ouverte <strong>un mois avant, à 10 h</strong> — pour 2027 : 1<sup>er</sup> décembre 2026 (T1), 2 mars (T2), 20 mai (T3), 17 août 2027 (T4). « Si une session n'est pas listée, elle est complète » ; pas de liste d'attente, une seule inscription à la fois.</td></tr>
<tr><td><strong>North York</strong></td><td>Alliance française de Toronto – campus North York</td><td><span class="badge ok">oui</span></td></tr>
<tr><td><strong>Mississauga</strong></td><td>Alliance française de Toronto – campus Mississauga</td><td><span class="badge ok">oui</span></td></tr>
<tr><td><strong>Oakville</strong></td><td>Alliance française de Toronto – campus Oakville</td><td><span class="badge ok">oui</span></td></tr>
<tr><td><strong>North York</strong></td><td>GB Language Centre</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>Ottawa</strong></td><td>Alliance française Ottawa</td><td><span class="badge ok">oui</span></td><td>Ordinateur ou papier ; <strong>passeport valide et convocation imprimée</strong> obligatoires, « aucune exception » ; résultats par e-mail sous 2 à 3 semaines.</td></tr>
<tr><td><strong>Ottawa (Kanata)</strong></td><td>FrancoLangues</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
</tbody>
</table>
</div>

<h2 id="ouest">Vancouver, Calgary, Edmonton et les Prairies</h2>

<div class="tablewrap wide">
<table>
<caption>Centres TCF agréés en Colombie-Britannique, en Alberta, en Saskatchewan et au Manitoba (liste FEI du 17 septembre 2026).</caption>
<thead><tr><th>Ville</th><th>Centre</th><th>SO</th><th>Relevé le 17 septembre 2026</th></tr></thead>
<tbody>
<tr><td><strong>Vancouver</strong></td><td>Alliance française Canada Pacific (Cambie St.)</td><td><span class="badge ok">oui</span></td><td><strong>390 $</strong>, 10 %% de remise aux membres ; <strong>toutes les sessions listées « SOLD OUT »</strong> le 17 septembre ; inscription en ligne seulement, « définitive, ni remboursement ni crédit » ; résultats par e-mail sous 3 à 4 semaines ; clavier QWERTY, accents via la plateforme de FEI.</td></tr>
<tr><td><strong>Vancouver</strong></td><td>Ashton Testing Services</td><td><span class="badge ok">oui</span></td><td>Centre de tests privé.</td></tr>
<tr><td><strong>New Westminster</strong></td><td>Alliance française Canada Pacific</td><td><span class="badge ok">oui</span></td><td>Second site de l'Alliance de Vancouver.</td></tr>
<tr><td><strong>Victoria</strong></td><td>Alliance française de Victoria</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>Victoria</strong></td><td>Université de Victoria (French Department)</td><td><span class="badge no">non</span></td><td>Papier.</td></tr>
<tr><td><strong>Calgary</strong></td><td>Alliance française de Calgary</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>Edmonton</strong></td><td>Alliance française d'Edmonton</td><td><span class="badge ok">oui</span></td><td>TCF Canada complet <strong>400 $</strong> (relevé le 30 juillet 2026).</td></tr>
<tr><td><strong>Lethbridge</strong></td><td>French Language Centre – University of Lethbridge</td><td><span class="badge no">non</span></td><td>Papier.</td></tr>
<tr><td><strong>Regina</strong></td><td>Collège Mathieu</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>Saskatoon</strong></td><td>Collège Mathieu</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
<tr><td><strong>Winnipeg</strong></td><td>Alliance française du Manitoba</td><td><span class="badge ok">oui</span></td><td>—</td></tr>
</tbody>
</table>
</div>

<h2 id="est">Provinces atlantiques et Nunavut</h2>

<div class="tablewrap wide">
<table>
<caption>Centres TCF agréés au Nouveau-Brunswick, en Nouvelle-Écosse, à Terre-Neuve-et-Labrador et au Nunavut (liste FEI du 17 septembre 2026).</caption>
<thead><tr><th>Ville</th><th>Centre</th><th>SO</th></tr></thead>
<tbody>
<tr><td><strong>Moncton</strong></td><td>Alliance française de Moncton</td><td><span class="badge ok">oui</span></td></tr>
<tr><td><strong>Bathurst</strong></td><td>CCNB – campus de Bathurst</td><td><span class="badge ok">oui</span></td></tr>
<tr><td><strong>Edmundston</strong></td><td>CCNB – campus d'Edmundston</td><td><span class="badge ok">oui</span></td></tr>
<tr><td><strong>Halifax</strong></td><td>Alliance française de Halifax</td><td><span class="badge ok">oui</span></td></tr>
<tr><td><strong>St. John's</strong></td><td>Memorial University</td><td><span class="badge ok">oui</span></td></tr>
<tr><td><strong>Iqaluit</strong></td><td>Ikajunga Services</td><td><span class="badge ok">oui</span></td></tr>
</tbody>
</table>
</div>

<p>Aucun centre à l'Île-du-Prince-Édouard, au Yukon ni aux Territoires du Nord-Ouest : les
candidats y passent le test dans la province voisine — Moncton ou Halifax, Vancouver ou
Edmonton.</p>

<h2 id="place">Obtenir une place : comment font ceux qui y arrivent</h2>

<p>Le TCF Canada a été passé par 124 667 candidats en 2025, quinze fois plus qu'en 2019. Les
grands centres n'ont pas suivi : à Toronto comme à Vancouver, les sessions sont
<strong>complètes en quelques minutes</strong>. Ce n'est pas une rumeur de forum, c'est ce
qu'écrivent les centres eux-mêmes.</p>

<div class="note">
<p>L'Alliance française de Toronto : « Our exam sessions are held quarterly, with registration
opening one month before each session. […] If a session is not listed, it is full. There is no
waiting list. » L'Alliance française de Vancouver : « Opening multiple tabs or repeatedly
refreshing the page may cancel your reservation […] Tip: Log in to your account in advance and
have your passport number ready before registration opens. »</p>
</div>

<ul>
<li><strong>Créez votre compte sur le site du centre avant le jour d'ouverture</strong>, passeport
sous la main. Le jour J, à l'heure exacte — 10 h à Toronto —, un seul onglet.</li>
<li><strong>Notez les dates d'ouverture</strong>, pas les dates d'examen : 1<sup>er</sup> décembre
2026 à Toronto pour les sessions de janvier-mars 2027.</li>
<li><strong>Élargissez le rayon.</strong> Les sept centres montréalais, les quatre campus
torontois et les universités régionales n'ont pas les mêmes files. L'Alliance française de
Montréal prévient toutefois que « les candidats s'inscrivant à un test malgré un éloignement
géographique important le font à leurs propres risques ».</li>
<li><strong>Revenez régulièrement</strong> : des places se libèrent et sont réattribuées
« premier arrivé, premier servi » (Toronto).</li>
<li><strong>Pas de double inscription</strong> : une seule session à la fois à Toronto, et la
règle des 20 jours entre deux passations s'applique « quel que soit le centre » (Stanislas) —
une inscription non conforme est annulée avec des frais.</li>
</ul>

<h2 id="inscription">S'inscrire, pas à pas</h2>

<ol>
<li><strong>Le bon test.</strong> Entrée express, citoyenneté : TCF Canada (ou TEF Canada). Programme
du Québec : TCF Québec ou TCF Canada, selon ce que demande votre volet — lisez
<a href="/tcf-quebec/">notre guide du TCF Québec</a>. L'Alliance française d'Ottawa le dit sans
détour : « It is the sole responsibility of the candidate to ensure that they are registered for
the appropriate exam. »</li>
<li><strong>Le bon score, avant la date.</strong> NCLC 7 exige 458 en compréhension orale et 453 à
l'écrit ; NCLC 9, 523 et 524. Un examen blanc noté sur 699 vous dit s'il faut viser la session
du trimestre ou celle d'après.</li>
<li><strong>Inscription en ligne</strong> sur le site du centre, avec le passeport que vous
utiliserez pour votre dossier IRCC. Paiement immédiat ; l'inscription est définitive.</li>
<li><strong>Convocation</strong> une semaine avant (Montréal, Vancouver), avec les horaires,
« ni flexibles, ni modifiables ». Les épreuves peuvent être réparties sur la journée.</li>
<li><strong>Le jour J</strong> : passeport valide et convocation imprimée — à Ottawa, « candidates
without valid identification and a printed convocation will be refused ». Compréhensions et
expression écrite sur ordinateur, clavier QWERTY ; l'oral face à un examinateur.</li>
<li><strong>Attestation</strong> par e-mail sous 2 à 4 semaines. Vérifiez l'orthographe de votre
nom : IRCC lira ce document tel quel, et « no duplicate of the certificate of results will be
delivered » (Ottawa).</li>
</ol>

<h2 id="prix">Combien ça coûte</h2>

<div class="tablewrap">
<table>
<caption>Tarifs du TCF Canada complet lus sur le site des centres (dates de relevé indiquées). Aucun tarif national ; « prices are subject to change without notice » (Alliance française de Vancouver).</caption>
<thead><tr><th>Centre</th><th>TCF Canada</th><th>Relevé</th></tr></thead>
<tbody>
<tr><td>Alliance française de Vancouver</td><td><strong>390 $</strong> (351 $ pour les membres)</td><td>17 septembre 2026</td></tr>
<tr><td>Alliance française d'Edmonton</td><td><strong>400 $</strong></td><td>30 juillet 2026</td></tr>
<tr><td>École internationale de français – UQTR</td><td><strong>440 $</strong></td><td>30 juillet 2026</td></tr>
<tr><td>Alliance française de Montréal</td><td><span class="badge part">non publié</span></td><td>17 septembre 2026</td></tr>
<tr><td>Alliance française de Toronto</td><td><span class="badge part">non publié</span> sur la page TCF</td><td>17 septembre 2026</td></tr>
</tbody>
</table>
</div>

<p>Comptez 390 à 440 $CA, soit nettement plus qu'en France (195 à 285 €) — les candidats qui
prévoient un séjour en Europe font parfois le calcul. Beaucoup de grands centres ne publient
aucun tarif : le prix apparaît au moment de réserver. Les chiffres des comparateurs qui affichent
un prix pour l'Alliance française de Montréal ne viennent pas de son site. Le détail, et ce que
coûte le TEF Canada, est dans <a href="/blog/prix-tcf-tef/">combien coûte vraiment le TCF ou le
TEF</a>.</p>

<h2 id="pieges">Les pièges : TCF Québec, annulation, recorrection</h2>

<div class="warn"><strong>Plus de recorrection depuis le 1<sup>er</sup> septembre 2026.</strong>
L'Alliance française de Toronto l'affiche : « France Education International will no longer
accept requests for recorrection for exam sessions held on or after September 1, 2026. » Des
pages de centres mentionnent encore la procédure à 100 $ par épreuve — elle ne s'applique plus
aux sessions récentes. Le score reçu est définitif.</div>

<ul>
<li><strong>TCF Québec ≠ TCF Canada.</strong> Le TCF pour le Québec est modulaire et sert aux
programmes du MIFI ; IRCC ne l'accepte pas. Dans un centre qui propose les deux, l'erreur de case
se paie plein tarif.</li>
<li><strong>L'annulation.</strong> À plus de 15 jours : 75 $ retenus à l'Alliance française de
Montréal, 15 $ par épreuve chez Stanislas. À moins de 15 jours : rien n'est remboursé, « même si
vous présentez un justificatif professionnel ou médical » (Montréal). À Vancouver, aucun
remboursement, jamais.</li>
<li><strong>Le délai de 20 jours</strong> entre deux passations, « quel que soit le centre » : une
inscription qui le viole est annulée avec des frais. Détails dans
<a href="/blog/repasser-tcf-tef/">repasser le TCF ou le TEF</a>.</li>
<li><strong>La double règle des deux ans</strong> d'IRCC — résultats de moins de deux ans à la
création du profil <em>et</em> au dépôt : <a href="/blog/validite-attestation-tcf-tef/">deux ans à
partir de quand&nbsp;?</a></li>
<li><strong>Le clavier.</strong> QWERTY canadien, accents via l'interface de FEI : entraînez-vous
à taper vos 180 mots d'expression écrite dans ces conditions, ou choisissez un centre qui propose
le papier (Ottawa, Toronto, Sherbrooke, Lethbridge, Victoria).</li>
</ul>
""" % {"serie": serie("/blog/ou-passer-le-tcf-canada-au-canada/"),
       "stats": stats([("47", "centres agréés", "dans 9 provinces et au Nunavut"),
                       ("44", "sur ordinateur", "les autres sur papier"),
                       ("390-440 $", "le test complet", "sur les centres qui publient un prix"),
                       ("20 jours", "entre deux passations", "quel que soit le centre")])},
    "cta_h2": "La place est rare, le score doit être prêt",
    "cta_p": """Quand une session s'ouvre un mois avant et se remplit en minutes, on ne s'inscrit pas
« pour voir ». Les examens blancs de l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;»
reproduisent les quatre épreuves du TCF Canada au format officiel, notées sur 699 et converties
en NCLC, avec la correction IA de l'écrit et de l'oral — pour arriver à la session avec le score
qu'il faut, pas avec l'espoir de l'avoir.""",
    "faq": [
        ("Où passer le TCF Canada à Montréal&nbsp;?",
         "Sept centres agréés dans Montréal au 17 septembre 2026 : l'Alliance Française de Montréal, le Collège Stanislas (Outremont), l'UQAM, l'Université Concordia, le Cégep Marie-Victorin, le Centre Yves-Thériault et le Collège ELC — tous avec des sessions sur ordinateur. S'y ajoutent Laval, Kirkland et Saint-Constant en banlieue. L'inscription se fait en ligne, centre par centre."),
        ("Où passer le TCF Canada à Toronto&nbsp;?",
         "À l'Alliance française de Toronto, sur quatre campus : Spadina (centre-ville), North York, Mississauga et Oakville, sur papier ou sur ordinateur ; GB Language Centre à North York est aussi agréé. Les sessions sont trimestrielles, l'inscription ouvre un mois avant à 10 h, et une session qui n'apparaît plus est complète — il n'y a pas de liste d'attente."),
        ("Combien coûte le TCF Canada au Canada&nbsp;?",
         "Il n'existe aucun tarif national, et beaucoup de centres ne publient pas le leur. Prix lus sur les sites des centres : 390 $ à l'Alliance française de Vancouver (17 septembre 2026), 400 $ à l'Alliance française d'Edmonton et 440 $ à l'École internationale de français de l'UQTR (30 juillet 2026). L'Alliance française de Montréal n'affiche aucun tarif."),
        ("Comment obtenir une place quand tout est complet&nbsp;?",
         "En s'inscrivant à l'ouverture, pas à la date de l'examen : créez votre compte à l'avance, ayez votre numéro de passeport sous la main, connectez-vous à l'heure exacte avec un seul onglet. À Toronto, les inscriptions pour 2027 ouvrent le 1er décembre 2026, puis les 2 mars, 20 mai et 17 août 2027. Revenez ensuite régulièrement : les places libérées sont réattribuées dans l'ordre d'arrivée, sans liste d'attente."),
        ("TCF Canada ou TCF Québec&nbsp;?",
         "Le TCF Canada est le test d'Immigration, Réfugiés et Citoyenneté Canada — Entrée express, citoyenneté — et il est aussi reconnu par le ministère de l'Immigration du Québec depuis janvier 2022. Le TCF pour le Québec, modulaire, ne sert qu'aux programmes québécois et n'est pas accepté par IRCC. Presque tous les centres canadiens proposent les deux : vérifiez la case cochée avant de payer."),
        ("Combien de temps pour les résultats&nbsp;?",
         "Deux à quatre semaines selon le centre : 2 à 3 semaines par e-mail à l'Alliance française d'Ottawa, 3 à 4 semaines à Vancouver. L'attestation officielle est le seul document valable pour IRCC, aucun duplicata n'est délivré, et elle vaut deux ans à compter de sa délivrance."),
        ("Quels documents apporter le jour de l'examen&nbsp;?",
         "Un passeport valide — le même que dans votre dossier d'immigration — et la convocation imprimée. L'Alliance française d'Ottawa refuse l'accès sans les deux, « sans exception », et l'identité est contrôlée pendant toute la durée des épreuves. Téléphone éteint et rangé ; sur ordinateur, le clavier QWERTY est fourni par le centre."),
    ],
    "also": [
        ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", "Les quatre épreuves, la conversion NCLC, les seuils pour Entrée express."),
        ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", "458 en compréhension orale, 453 à l'écrit — la table de conversion officielle complète."),
        ("/tcf-quebec/", "TCF Québec : le test modulaire", "La version où l'on ne paie que les épreuves dont on a besoin — et pourquoi IRCC ne l'accepte pas."),
        ("/blog/ou-passer-le-tcf-canada-en-france/", "Où passer le TCF Canada en France&nbsp;?", "Les centres qui le proposent, de 195 à 285 €, et leurs dates de session."),
    ],
    "sources": """<strong>Sources.</strong> Liste des centres de passation TCF de France Éducation
international (filtre « Canada », 48 entrées), consultée le 17 septembre 2026 ; pages TCF de
l'Alliance Française de Montréal, du Collège Stanislas (Montréal et Québec), de l'Alliance
française de Toronto, de l'Alliance française Ottawa et de l'Alliance française de Vancouver
(page TCF Canada et calendrier des sessions), consultées le 17 septembre 2026 ; tarifs de
l'Alliance française d'Edmonton et de l'École internationale de français de l'UQTR relevés le
30 juillet 2026 ; chiffres 2025 des certifications de France Éducation international. Les prix,
dates et règles d'annulation changent sans préavis : vérifiez-les sur le site de votre centre.""",
}


# ---------------------------------------------------------------------------
# 5. Le hub /ou-passer/
# ---------------------------------------------------------------------------
FEI_L = "https://www.france-education-international.fr/centres-d-examen/liste?pays=%s&type-centre=%s"
HUB = {
    "section": "",
    "slug": "ou-passer",
    "accent": "accent-delf",
    "crumb": "Où passer l'examen",
    "title": "Où passer le DELF, le TCF ou le TEF ? Centres par pays",
    "desc": "Où passer le DELF, le TCF IRN, le TCF Canada et l'examen civique en France, au Canada et au Maghreb : centres agréés, inscription, prix relevés, pièges.",
    "og_title": "Où passer le DELF, le TCF ou le TEF ? Centres par pays",
    "og_desc": "Les centres agréés, l'inscription, les prix relevés et les pièges — en France, au Canada et au Maghreb.",
    "h1": "Où passer le DELF, le TCF ou le TEF&nbsp;?",
    "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": 6,
    "intro": """Tous ces examens se passent <strong>en présentiel, dans un centre agréé</strong> — par
France Éducation international pour le DELF, le DALF et le TCF, par Le français des affaires
(CCI Paris Île-de-France) pour le TEF. Il n'existe <strong>aucune passation en ligne</strong>. On
s'inscrit auprès du centre, qui fixe ses dates et son prix ; ni FEI ni la CCI n'inscrivent de
candidats. Choisissez votre examen et votre pays : chaque guide donne les centres, les prix
relevés, les dates et le pas-à-pas.""",
    "facts": [
        "<strong>143 centres DELF-DALF</strong> et <strong>251 centres TCF</strong> en France, <strong>47 centres TCF</strong> au Canada, 16 au Maroc, 14 en Tunisie, 5 en Algérie (liste FEI, 17 septembre 2026).",
        "Un centre est agréé ou ne l'est pas : la seule preuve est la <strong>liste officielle</strong> de FEI (DELF, DALF, TCF) ou du Français des affaires (TEF).",
        "<strong>Aucun tarif national</strong> : du simple au double pour le même examen, parfois dans la même ville.",
        "⚠️ La <strong>place</strong> est le vrai goulot : fenêtres d'inscription de deux jours pour le DELF, sessions complètes en minutes pour le TCF Canada à Toronto ou Vancouver.",
        "Un diplôme (DELF, DALF) est <strong>valable à vie</strong> ; un test (TCF, TEF) vaut <strong>2 ans</strong> et se repasse après 20 à 30 jours.",
        "Toute offre « à distance », « sans déplacement » ou « avec un candidat partenaire » est une <strong>fraude</strong>.",
    ],
    "toc": [
        ("guides", "Les guides par examen et par pays"),
        ("listes", "L'annuaire des centres, avec leurs contacts"),
        ("regles", "Les cinq règles qui valent partout"),
        ("fraude", "Reconnaître un faux centre"),
    ],
    "body": """
%(stats)s

<h2 id="guides">Les guides par examen et par pays</h2>

<p>Le tableau croise l'examen et le pays de passation. Les cases avec un lien renvoient à un guide
détaillé — centres relevés un par un, prix lus sur leurs sites, dates de session, procédure
d'inscription ; les autres renvoient directement à la liste officielle des centres du pays.</p>

<div class="tablewrap matrix">
<table>
<caption>Où passer chaque examen, pays par pays. Les guides sont datés ; les listes officielles de France Éducation international sont mises à jour par FEI.</caption>
<thead><tr><th>Examen</th><th>France</th><th>Canada</th><th>Algérie</th><th>Maroc</th><th>Tunisie</th></tr></thead>
<tbody>
<tr><td><strong>DELF · DALF</strong> (diplômes, à vie)</td><td><a href="/blog/ou-passer-le-delf-en-france/">Guide : 143 centres, 10 sessions par an</a></td><td><a href="%(ca_delf)s" rel="noopener">Liste FEI</a></td><td><a href="%(dz_delf)s" rel="noopener">Liste FEI</a></td><td><a href="%(ma_delf)s" rel="noopener">Liste FEI</a></td><td><a href="%(tn_delf)s" rel="noopener">Liste FEI</a></td></tr>
<tr><td><strong>TCF IRN</strong> (naturalisation, titres de séjour)</td><td><a href="/blog/ou-passer-le-tcf-irn-en-france/">Guide : centres, 140 à 220 €</a></td><td>—</td><td><a href="/blog/tcf-canada-algerie/#inscription">Mêmes antennes, plateforme IFAL</a></td><td><a href="/blog/tcf-canada-maroc/#prix">1 900 Dhs, sur place</a></td><td><a href="/blog/tcf-canada-tunisie/#prix">625 DT à l'Institut</a></td></tr>
<tr><td><strong>Examen civique</strong> (France, depuis 2026)</td><td><a href="/blog/ou-passer-l-examen-civique/">Guide : 244 centres FEI + réseau CCIP</a></td><td>—</td><td><a href="/blog/ou-passer-l-examen-civique/#etranger">IF Alger, 9 000 DA</a></td><td><a href="%(civ_carte)s" rel="noopener">Carte FEI</a></td><td><a href="%(civ_carte)s" rel="noopener">Carte FEI</a></td></tr>
<tr><td><strong>TCF Canada</strong> (IRCC)</td><td><a href="/blog/ou-passer-le-tcf-canada-en-france/">Guide : centres, 195 à 285 €</a></td><td><a href="/blog/ou-passer-le-tcf-canada-au-canada/">Guide : les 47 centres</a></td><td><a href="/blog/tcf-canada-algerie/">Guide : 5 antennes, plateforme IFAL</a></td><td><a href="/blog/tcf-canada-maroc/">Guide : 16 centres, 2 900 Dhs</a></td><td><a href="/blog/tcf-canada-tunisie/">Guide : 14 centres, 880 DT</a></td></tr>
<tr><td><strong>TCF Québec</strong> (MIFI)</td><td>Mêmes centres que le TCF Canada</td><td><a href="/blog/ou-passer-le-tcf-canada-au-canada/">Mêmes centres</a></td><td><a href="/blog/tcf-canada-algerie/">Mêmes antennes</a></td><td><a href="/blog/tcf-canada-maroc/#prix">Mêmes centres, 2 900 Dhs</a></td><td><a href="/blog/tcf-canada-tunisie/#prix">Mêmes pôles, 880 DT</a></td></tr>
<tr><td><strong>TEF</strong> (Canada, IRN, Québec)</td><td colspan="5"><a href="%(fda)s" rel="noopener">Annuaire des centres agréés du Français des affaires</a>, tous pays</td></tr>
</tbody>
</table>
</div>

<div class="grid c2 guides">
<div class="card card-link"><span class="tag">France · diplôme</span><h3><a href="/blog/ou-passer-le-delf-en-france/">Où passer le DELF en France&nbsp;?</a></h3><p>143 centres, le calendrier 2026-2027, les 7 centres parisiens, un B2 de 125 à 280 € et des fenêtres d'inscription de deux jours.</p></div>
<div class="card card-link"><span class="tag">France · naturalisation</span><h3><a href="/blog/ou-passer-le-tcf-irn-en-france/">Où passer le TCF IRN en France&nbsp;?</a></h3><p>Des sessions chaque semaine à Paris, 140 à 220 € selon le centre, papier ou ordinateur, et l'examen civique à ne pas oublier.</p></div>
<div class="card card-link"><span class="tag">France · Canada</span><h3><a href="/blog/ou-passer-le-tcf-canada-en-france/">Où passer le TCF Canada en France&nbsp;?</a></h3><p>Les centres qui le proposent — pas tous —, 195 à 285 €, des sessions mensuelles et la fin des recorrections.</p></div>
<div class="card card-link"><span class="tag">Canada</span><h3><a href="/blog/ou-passer-le-tcf-canada-au-canada/">Où passer le TCF Canada au Canada&nbsp;?</a></h3><p>Les 47 centres agréés par province, 390 à 440 $, et la méthode pour décrocher une place quand tout affiche complet.</p></div>
<div class="card card-link"><span class="tag">Algérie</span><h3><a href="/blog/tcf-canada-algerie/">TCF Canada en Algérie</a></h3><p>Les cinq antennes de l'Institut français, l'inscription sur la plateforme IFAL, la règle des 26 jours — et le faux site qui imite l'Institut.</p></div>
<div class="card card-link"><span class="tag">Maroc</span><h3><a href="/blog/tcf-canada-maroc/">TCF Canada au Maroc</a></h3><p>Seize centres, 2 900 dirhams partout, des sessions plusieurs fois par semaine à Casablanca et l'inscription en ligne site par site.</p></div>
<div class="card card-link"><span class="tag">Tunisie</span><h3><a href="/blog/tcf-canada-tunisie/">TCF Canada en Tunisie</a></h3><p>880 dinars, un rendez-vous en ligne puis l'inscription sur place, une session par mois par pôle et des résultats en cinq semaines.</p></div>
<div class="card card-link"><span class="tag">France · titres et nationalité</span><h3><a href="/blog/ou-passer-l-examen-civique/">Où passer l'examen civique&nbsp;?</a></h3><p>Deux réseaux agréés, la pré-inscription sur test-civique.fr, 70 à 110 € selon le centre et des résultats sous 12 heures.</p></div>
</div>

<h2 id="listes">L'annuaire des centres, avec leurs contacts</h2>

<p>Nous avons repris la liste officielle de France Éducation international, pays par pays, avec
l'adresse, le téléphone, l'e-mail et le site de chaque centre — <strong>830 centres dans 32 pays</strong>
au 19 septembre 2026 — dans un <a href="/centres/">annuaire des centres</a> :
<a href="/centres/tcf-france/">TCF en France</a> (251), <a href="/centres/delf-france/">DELF-DALF en
France</a> (143), <a href="/centres/examen-civique-france/">examen civique en France</a> (245),
<a href="/centres/tcf-canada/">TCF au Canada</a> (47), <a href="/centres/tcf-maroc/">Maroc</a> (16),
<a href="/centres/tcf-tunisie/">Tunisie</a> (14), <a href="/centres/tcf-algerie/">Algérie</a> (5),
<a href="/centres/tcf-afrique/">Afrique subsaharienne</a> (23), <a href="/centres/tcf-europe/">Belgique,
Suisse, Royaume-Uni</a> (12), <a href="/centres/tcf-ameriques/">États-Unis et Amérique latine</a> (51),
<a href="/centres/tcf-moyen-orient/">Liban, Émirats, Égypte, Turquie</a> (16), <a href="/centres/tcf-inde/">Inde</a> (7).</p>

<p>Les listes officielles restent la référence en cas de doute :</p>
<ul>
<li><strong>DELF, DALF, TCF</strong> — France Éducation international :
<a href="https://www.france-education-international.fr/centres-d-examen/liste?type-centre=delf_dalf" rel="noopener">liste des centres DELF-DALF</a>,
<a href="https://www.france-education-international.fr/centres-d-examen/liste?type-centre=tcf" rel="noopener">liste des centres TCF</a>, par pays, et une
<a href="%(carte)stcf" rel="noopener">carte</a>. FEI recensait 1 182 centres DELF-DALF et 768 centres TCF dans le monde en 2024.</li>
<li><strong>TEF</strong> — Le français des affaires :
<a href="%(fda)s" rel="noopener">trouver un centre agréé</a>.</li>
<li><strong>Examen civique</strong> (France, depuis 2026) — catégorie à part sur la
<a href="https://www.france-education-international.fr/centres-d-examen/carte?type-centre=examen_civique" rel="noopener">carte des centres de FEI</a>.</li>
</ul>

<p>Ces listes disent qu'un centre est agréé, pas quelles déclinaisons il organise ni à quel prix :
c'est sur le site du centre que se lit le reste — et c'est le travail que font nos guides.</p>

<h2 id="regles">Les cinq règles qui valent partout</h2>

<ol>
<li><strong>Le centre décide.</strong> Sessions ouvertes, tarif, mode (papier ou ordinateur),
fenêtre d'inscription, délai de résultats : tout varie d'un centre à l'autre, y compris dans la
même ville. Deux appels valent mieux qu'un comparateur.</li>
<li><strong>Le prix est libre.</strong> DELF B2 de 125 à 280 € en France ; TCF IRN de 140 à
220 € ; TCF Canada de 195 à 285 € en France et de 390 à 440 $ au Canada ; et beaucoup de centres
ne publient rien. Notre article <a href="/blog/prix-tcf-tef/">sur les prix</a> explique pourquoi.</li>
<li><strong>La place avant le prix.</strong> Fenêtres d'inscription de deux jours pour le DELF à
Nantes, sessions complètes deux mois à l'avance à Lyon, en minutes pour le TCF Canada à Toronto.
Inscrivez-vous à l'ouverture, à une session que vous aurez le temps de préparer.</li>
<li><strong>Diplôme ou test.</strong> Le DELF et le DALF sont valables à vie ; les attestations
TCF et TEF expirent au bout de deux ans, et l'on attend 20 à 30 jours entre deux passations.
Pour choisir : <a href="/blog/diplome-ou-test-delf-tcf/">diplôme ou test&nbsp;?</a></li>
<li><strong>Le bon examen, la bonne déclinaison.</strong> TCF IRN pour la France, TCF Canada pour
IRCC, TCF Québec pour le MIFI, TCF tout public pour les études : une case cochée de travers se
paie plein tarif. Le comparatif <a href="/blog/difference-tcf-tef/">des neuf versions du TCF et
du TEF</a> les met côte à côte.</li>
</ol>

<h2 id="fraude">Reconnaître un faux centre</h2>

<div class="warn"><strong>Le 17 septembre 2026, un site imitant l'Institut français d'Algérie</strong>
— sous un nom de domaine en <em>.fr</em> alors que l'officiel est <em>if-algerie.com</em> —
proposait, pour 70 000 à 100 000 dinars, qu'« un candidat partenaire se présente à votre place
pour passer l'examen, en toute discrétion ». Il figurait en troisième position sur Google pour
« inscription TCF Algérie ». C'est une escroquerie et un délit ; une attestation ainsi obtenue
n'existe pas dans les registres de FEI et sera détectée à l'authentification. Le détail est dans
notre <a href="/blog/tcf-canada-algerie/#faux-site">guide Algérie</a>.</div>

<p>Les signes qui ne trompent pas : une passation « à distance » ou « depuis chez vous », un
paiement demandé avant tout choix de date et de centre, un nom de domaine différent de celui de
la liste officielle, une adresse e-mail générique, une « attestation provisoire sous 24 heures »
pour un test qui n'a pas eu lieu. Le bon réflexe tient en une étape : partir de la liste de FEI ou
du Français des affaires, et ne cliquer que sur le site qui y figure. FEI rappelle que « la fraude
et la tentative de fraude à un examen ou un test officiel du gouvernement français sont des délits
qui entraînent des sanctions disciplinaires et des procédures pénales ».</p>
""" % {"stats": stats([("143", "centres DELF en France", "liste FEI du 17/09/2026"),
                       ("251", "centres TCF en France", "dont 126 sur ordinateur"),
                       ("47", "centres TCF au Canada", "neuf provinces et le Nunavut"),
                       ("35", "centres TCF au Maghreb", "Maroc 16 · Tunisie 14 · Algérie 5")]),
       "carte": FEI_CARTE, "fda": FDA_CENTRES,
       "ca_delf": FEI_L % (112, "delf_dalf"), "dz_delf": FEI_L % (115, "delf_dalf"),
       "ma_delf": FEI_L % (117, "delf_dalf"), "tn_delf": FEI_L % (118, "delf_dalf"),
       "dz_tcf": FEI_L % (115, "tcf"), "ma_tcf": FEI_L % (117, "tcf"), "tn_tcf": FEI_L % (118, "tcf"),
       "civ_carte": FEI_CARTE + "examen_civique"},
    "cta_h2": "Le centre vous donne la date ; le niveau, c'est vous",
    "cta_p": """Une session se paie en entier et, pour un test, ne se repasse pas avant trois semaines.
Les examens blancs de l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent le format
officiel de chaque déclinaison — DELF, DALF, TCF IRN, TCF Canada, TCF Québec, TEF — avec la
notation du vrai test et la correction IA de l'écrit et de l'oral.""",
    "faq": [
        ("Comment savoir si un centre d'examen est agréé&nbsp;?",
         "En le cherchant dans la liste officielle de l'organisme qui délivre l'examen : France Éducation international pour le DELF, le DALF et le TCF (liste par pays, avec adresse, téléphone et site), Le français des affaires pour le TEF. Un organisme absent de ces listes ne peut pas vous faire passer l'examen, quel que soit son site ou son nom."),
        ("Peut-on passer le DELF, le TCF ou le TEF en ligne&nbsp;?",
         "Non. Toutes ces certifications se passent en présentiel, dans un centre agréé, sur convocation et avec contrôle d'identité. Pour la naturalisation française, un arrêté du 22 décembre 2025 l'impose expressément. Toute offre « à distance », « sans déplacement » ou par « candidat partenaire » est une fraude."),
        ("Où passer le TEF&nbsp;?",
         "Dans un centre agréé par Le français des affaires (CCI Paris Île-de-France), qui publie un annuaire « trouver un centre agréé » couvrant tous les pays. Ce sont souvent les mêmes Alliances françaises et écoles que pour le TCF, mais l'agrément est distinct : un centre TCF n'est pas automatiquement un centre TEF."),
        ("Quel examen est valable toute la vie&nbsp;?",
         "Le DELF et le DALF, qui sont des diplômes du ministère de l'Éducation nationale. Les attestations du TCF et du TEF, elles, valent deux ans à compter de leur délivrance, et l'on ne peut repasser un test qu'après 20 à 30 jours. Le diplôme prend plus de temps à obtenir — dix sessions par an, inscription des semaines à l'avance — mais ne se repaie jamais."),
        ("Combien de temps à l'avance faut-il s'inscrire&nbsp;?",
         "Pour le DELF en France, la fenêtre d'inscription ferme quatre à dix semaines avant l'écrit, et s'ouvre parfois sur deux jours seulement. Pour le TCF IRN à Paris, quelques jours suffisent, avec des sessions chaque semaine. Pour le TCF Canada au Canada, il faut s'inscrire à l'ouverture des inscriptions, un mois avant chaque trimestre à Toronto, les places partant en quelques minutes."),
    ],
    "also": [
        ("/blog/diplome-ou-test-delf-tcf/", "Diplôme ou test : DELF, DALF, TCF ou TEF, lequel vous faut-il&nbsp;?", "Un diplôme s'obtient à vie et peut se rater ; un test vous situe pour deux ans."),
        ("/blog/prix-tcf-tef/", "Combien coûte vraiment le TCF ou le TEF&nbsp;?", "Aucun tarif national : les prix relevés centre par centre, en France et au Canada."),
        ("/blog/difference-tcf-tef/", "TCF ou TEF : les 9 versions comparées", "Formats, échelles, reconnaissance administrative de chaque déclinaison."),
        ("/centres/", "L'annuaire des centres d'examen", "830 centres agréés dans 32 pays, avec adresse, téléphone, e-mail et site."),
    ],
    "sources": """<strong>Sources.</strong> Listes et carte des centres d'examen de France Éducation
international (DELF-DALF, TCF, examen civique), par pays, consultées le 17 septembre 2026 ;
« Les chiffres 2024 des certifications » de FEI (lettre du 31 mars 2025) ; annuaire « Trouver un
centre agréé » du Français des affaires ; page « Informations pratiques pour les candidats au
DELF-DALF » de FEI (sanctions en cas de fraude) ; site frauduleux constaté le 17 septembre 2026
et signalé. Les guides liés citent leurs propres sources, centre par centre.""",
}


# ---------------------------------------------------------------------------
# 6. TCF Canada en Algérie
# ---------------------------------------------------------------------------
DZ = {
    "slug": "tcf-canada-algerie",
    "accent": "accent-tcf",
    "crumb": "TCF Canada en Algérie",
    "title": "TCF Canada en Algérie : où le passer, comment s'inscrire",
    "desc": "Cinq antennes de l'Institut français, l'inscription en ligne sur la plateforme IFAL, 26 jours entre deux inscriptions et un faux site à éviter.",
    "og_title": "TCF Canada en Algérie : où le passer, comment s'inscrire",
    "og_desc": "Cinq antennes de l'Institut français, l'inscription sur la plateforme IFAL, 26 jours entre deux inscriptions, et un faux site à éviter.",
    "h1": "TCF Canada en Algérie : où le passer et comment s'inscrire",
    "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": 9,
    "intro": """En Algérie, le TCF Canada se passe dans les <strong>cinq antennes de l'Institut français
d'Algérie</strong> — Alger, Oran, Constantine, Annaba et Tlemcen — et nulle part ailleurs : ce sont
les seuls centres agréés par France Éducation international dans le pays. L'inscription et le
paiement se font <strong>exclusivement en ligne</strong>, sur la plateforme IFAL opérée par VFS
Global, avec des sessions <strong>ouvertes chaque mois</strong>. Un site frauduleux imite
l'Institut : voici comment le reconnaître, et le vrai chemin, étape par étape.""",
    "facts": [
        "<strong>5 centres agréés</strong> en Algérie, tous des antennes de l'Institut français : Alger (Hydra), Oran, Constantine, Annaba, Tlemcen — liste FEI du 17 septembre 2026, sessions sur ordinateur partout.",
        "Inscription <strong>en ligne uniquement</strong>, sur la plateforme <strong>IFAL</strong> (forms.vfsglobal.com.dz/IFAL) : « Les inscriptions et les paiements se font exclusivement en ligne. »",
        "<strong>Des sessions chaque mois</strong> sur les cinq antennes ; <strong>26 jours</strong> obligatoires entre deux inscriptions au TCF.",
        "Pièce d'identité : <strong>carte d'identité biométrique ou passeport</strong> pour les Algériens ; passeport biométrique ou carte consulaire pour les autres.",
        "Le <strong>tarif n'est pas publié</strong> sur le site de l'Institut : il s'affiche sur la plateforme au moment de l'inscription.",
        "⚠️ <strong>if-algerie.fr est une escroquerie</strong> ; le site officiel est <strong>if-algerie.com</strong>. Aucun TCF ne se passe « à distance » ni par « candidat partenaire ».",
    ],
    "toc": [
        ("centres", "Les cinq centres agréés"),
        ("inscription", "S'inscrire sur la plateforme IFAL, pas à pas"),
        ("quand", "Quand : sessions mensuelles et règle des 26 jours"),
        ("prix", "Combien ça coûte"),
        ("resultats", "Résultats et attestation"),
        ("faux-site", "Le faux site qui imite l'Institut français"),
        ("pieges", "Les autres pièges"),
    ],
    "body": """
<h2 id="centres">Les cinq centres agréés</h2>

<p>La liste officielle de France Éducation international ne compte, en Algérie, que
<strong>cinq centres de passation du TCF</strong>, et ce sont les cinq antennes de l'Institut
français d'Algérie. Chacune propose l'option « sessions sur ordinateur ». Aucune école privée,
aucun centre de langues n'est agréé : un organisme qui vous propose un TCF Canada ailleurs que
dans l'une de ces cinq adresses ne peut pas vous délivrer une attestation reconnue par IRCC.</p>

<div class="tablewrap wide">
<table>
<caption>Centres de passation TCF en Algérie, liste officielle de France Éducation international consultée le 17 septembre 2026.</caption>
<thead><tr><th>Ville</th><th>Centre</th><th>Adresse</th><th>Contact</th></tr></thead>
<tbody>
<tr><td><strong>Alger</strong></td><td>Institut français d'Algérie, antenne d'Alger</td><td>30, rue des Frères-Kadri, Hydra</td><td>Assistance VFS : 021 99 60 08 · examens@if-algerie.com</td></tr>
<tr><td><strong>Oran</strong></td><td>Institut français d'Algérie, antenne d'Oran</td><td>112, rue Larbi-Ben-M'hidi</td><td>041 70 73 73 · bureau-examens.oran@if-algerie.com</td></tr>
<tr><td><strong>Constantine</strong></td><td>Institut français d'Algérie, antenne de Constantine</td><td>1, boulevard de l'Indépendance</td><td>031 91 25 91 · examens.constantine@if-algerie.com</td></tr>
<tr><td><strong>Annaba</strong></td><td>Institut français d'Algérie, antenne d'Annaba</td><td>6, route de l'Avant-Port</td><td>038 45 12 49</td></tr>
<tr><td><strong>Tlemcen</strong></td><td>Institut français d'Algérie, antenne de Tlemcen</td><td>1, rue du Commandant-Djaber</td><td>043 26 17 22 · examens.tlemcen@if-algerie.com</td></tr>
</tbody>
</table>
</div>

<p>L'Institut organise toutes les déclinaisons du TCF : Canada, Québec, tout public, DAP et IRN.
Pour un dossier d'immigration fédérale — Entrée express, citoyenneté —, c'est le <strong>TCF
Canada</strong> qu'il faut cocher, pas le tout public ; pour un programme du Québec, le
<a href="/tcf-quebec/">TCF Québec</a> ou le TCF Canada selon ce que demande votre volet.</p>

%(serie)s

<h2 id="inscription">S'inscrire sur la plateforme IFAL, pas à pas</h2>

<p>La page TCF de l'Institut est sans ambiguïté : « Les inscriptions au TCF toutes déclinaisons
se font en ligne sur la plateforme IFAL. » Et sa FAQ ferme la porte aux autres voies : « Peut-on
prendre un rendez-vous TCF sur place sans passer par le site ? — Les inscriptions et les paiements
se font exclusivement en ligne. » La plateforme, <strong>forms.vfsglobal.com.dz/IFAL</strong>, est
opérée par VFS Global, le prestataire qui gère aussi les rendez-vous de visa ; c'est lui qui
assure l'assistance (info.tcfalg@vfshelpline.com, 021 99 60 08).</p>

<ol>
<li><strong>Partez du site officiel</strong>, if-algerie.com, rubrique « Tests et examens › TCF »,
et cliquez sur « Je m'inscris au TCF ». N'entrez jamais l'adresse de la plateforme depuis un lien
reçu par messagerie ou trouvé dans une publicité.</li>
<li><strong>Créez votre compte</strong> sur la plateforme IFAL avec une adresse e-mail que vous
consultez : convocation et attestation y seront envoyées.</li>
<li><strong>Choisissez la déclinaison</strong> — TCF Canada —, l'antenne et la session. Les
sessions sont ouvertes chaque mois sur les cinq antennes ; quand une date n'apparaît plus, elle est
pleine.</li>
<li><strong>Payez en ligne.</strong> Le tarif s'affiche à cette étape ; il n'est publié nulle part
ailleurs.</li>
<li><strong>Le jour J</strong>, présentez-vous avec la convocation et votre pièce d'identité : carte
d'identité biométrique ou passeport si vous êtes algérien, passeport biométrique ou carte consulaire
sinon. Les quatre épreuves — 2 h 47 au total — se passent sur ordinateur, à l'antenne choisie ;
l'expression orale, individuelle, a son propre créneau, indiqué sur la convocation.</li>
</ol>

<div class="note">
<p><strong>Une seule exception au tout-en-ligne :</strong> les épreuves complémentaires du TCF tout
public (expression écrite ou orale ajoutées à un TCF déjà passé) s'inscrivent directement auprès
des antennes, hors plateforme — mais cela ne concerne pas le TCF Canada, dont les quatre épreuves
sont indissociables.</p>
</div>

<h2 id="quand">Quand : sessions mensuelles et règle des 26 jours</h2>

<p>« Des sessions TCF sont ouvertes tous les mois sur les cinq antennes de l'Institut français
d'Algérie », indique la FAQ. Il n'y a pas de calendrier annuel publié : les dates apparaissent sur
la plateforme à l'ouverture des inscriptions, et une session complète disparaît de la liste.
Concrètement, si votre dossier a une échéance, connectez-vous dès le début du mois précédent, et
acceptez l'antenne qui a de la place plutôt que d'attendre la vôtre.</p>

<p>Une règle propre à l'Institut : « Vous devez respecter un <strong>délai de 26 jours entre deux
inscriptions TCF</strong>. » C'est plus que les 20 jours qu'annoncent les pages de France
Éducation international, moins que les 30 jours de ses fiches — et c'est la règle que la
plateforme appliquera. Ne réservez pas une seconde session « au cas où » à moins de 26 jours de
la première : l'inscription serait invalide. Pour le détail des règles de reprise, lisez
<a href="/blog/repasser-tcf-tef/">repasser le TCF ou le TEF</a>.</p>

<h2 id="prix">Combien ça coûte</h2>

<p>L'Institut français d'Algérie ne publie <strong>aucun tarif</strong> sur son site : le prix du
TCF Canada s'affiche sur la plateforme IFAL au moment de choisir la session, et il se paie en
ligne. Nous ne le reproduisons donc pas ici — tout chiffre que vous lirez ailleurs vient d'un
candidat ou d'un comparateur, jamais de l'Institut. Un repère officiel existe tout de même :
l'examen civique français, organisé par le même Institut à Alger, coûte <strong>9 000 DA</strong>
(page « Examen civique » de l'IFA, 17 septembre 2026). Méfiez-vous en revanche des tarifs à
70 000 ou 100 000 DA « selon le niveau garanti » : ils ne sont pas ceux d'un test, ils sont ceux
d'une fraude, et nous y revenons plus bas.</p>

<p>Chaque tentative se paie en entier — il n'existe aucune reprise partielle au TCF Canada — et
l'attestation vaut deux ans. Le vrai coût d'un test raté, c'est donc une seconde inscription et
au moins 26 jours de plus. Nos <a href="/examens-blancs/">examens blancs au format officiel</a>
servent à ça : savoir si le NCLC visé est atteint avant de payer la session.</p>

<h2 id="resultats">Résultats et attestation</h2>

<p>Pour le TCF tout public, la FAQ de l'Institut décrit une attestation provisoire remise à
l'issue de la passation, puis « l'attestation originale envoyée par mail une quinzaine de
jours » plus tard — et précise qu'« aucune attestation version papier n'est remise depuis mars
2023 ». Le TCF Canada suit le même circuit numérique : l'attestation arrive dans votre
messagerie, et c'est ce PDF, tel quel, que vous téléverserez dans votre dossier IRCC. Vérifiez
immédiatement l'orthographe de votre nom et votre date de naissance. « Tous les TCF ont une
validité de 2 ans » — et IRCC exige des résultats de moins de deux ans au moment de créer le
profil <em>et</em> au dépôt de la demande : <a href="/blog/validite-attestation-tcf-tef/">deux ans à
partir de quand&nbsp;?</a></p>

<p>Depuis les sessions du 1<sup>er</sup> septembre 2026, France Éducation international n'accepte
plus de demande de recorrection : le score est définitif. Ce qu'il vaut en NCLC — 458 en
compréhension orale et 453 à l'écrit pour le NCLC 7 — est dans notre guide
<a href="/blog/tcf-canada-nclc-7/">NCLC 7 au TCF Canada</a>.</p>

<h2 id="faux-site">Le faux site qui imite l'Institut français</h2>

<div class="warn"><strong>if-algerie.fr n'est pas l'Institut français d'Algérie.</strong> Le
17 septembre 2026, ce site — classé en troisième position sur Google pour « inscription TCF
Algérie » — proposait un « TCF Canada » à 70 000, 80 000 ou 100 000 DA « selon le niveau », avec
cette promesse : « Un candidat partenaire se présente à votre place pour passer l'examen, en
toute discrétion », une « attestation provisoire sous 24 heures » et l'envoi de vos papiers
d'identité, photo et signature par e-mail. Le site officiel est <strong>if-algerie.com</strong>,
et le seul lieu d'inscription est la plateforme IFAL.</div>

<p>Ce que cette offre vous ferait perdre : l'argent, évidemment ; vos documents d'identité,
remis à des inconnus ; et votre dossier canadien, puisqu'une attestation qui n'existe pas dans
les registres de France Éducation international est détectée à la vérification — IRCC peut
contrôler les résultats auprès de l'organisme. La substitution de personne est en outre une fraude que
FEI sanctionne par une interdiction de se présenter à ses tests. Les signes qui ne trompent pas :
un domaine différent de celui de la liste officielle, une adresse e-mail générique, un prix « selon
le niveau », un paiement demandé avant toute date, une passation « à distance » ou « discrète ».
Le bon réflexe : partir de la <a href="https://www.france-education-international.fr/centres-d-examen/liste?pays=115&type-centre=tcf" rel="noopener">liste
officielle des centres</a> et ne cliquer que sur le site qui y figure.</p>

<h2 id="pieges">Les autres pièges</h2>

<ul>
<li><strong>Le mauvais TCF.</strong> La plateforme propose cinq déclinaisons ; seul le TCF
<em>Canada</em> est accepté par IRCC. Le TCF tout public, même complet, ne vaut rien pour Entrée
express, et le TCF Québec ne sert qu'aux programmes du MIFI. Vérifiez la mention sur votre
convocation.</li>
<li><strong>La double inscription.</strong> 26 jours minimum entre deux inscriptions : une
réservation « de sécurité » trop proche est annulée.</li>
<li><strong>Le B2 qui n'est pas un NCLC 7.</strong> IRCC lit le score sur 699 converti en NCLC,
pas la lettre : un 420 en compréhension orale est un « B2 » sur l'attestation, mais seulement un
NCLC 6.</li>
<li><strong>L'échéance.</strong> Deux ans de validité, comptés deux fois par IRCC ; et 15 jours
environ pour recevoir l'attestation. Un test passé trop tard bloque un dossier autant qu'un test
raté.</li>
<li><strong>Le TEF Canada.</strong> C'est l'autre test accepté par IRCC ; en Algérie, il relève du
réseau du Français des affaires (CCI Paris Île-de-France), avec son propre
<a href="%(fda)s" rel="noopener">annuaire de centres</a>. Notre comparatif
<a href="/blog/tcf-ou-tef-canada/">TCF ou TEF Canada</a> aide à choisir.</li>
</ul>
""" % {"serie": serie("/blog/tcf-canada-algerie/"), "fda": FDA_CENTRES},
    "cta_h2": "Le score, avant la session",
    "cta_p": """Une session par mois, 26 jours entre deux inscriptions, un score désormais définitif :
en Algérie, on ne passe pas le TCF Canada « pour voir ». Les examens blancs de l'app «&nbsp;TCF
DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent les quatre épreuves au format officiel, notées sur
699 et converties en NCLC, avec la correction IA de l'écrit et de l'oral.""",
    "faq": [
        ("Où passer le TCF Canada en Algérie&nbsp;?",
         "Dans l'une des cinq antennes de l'Institut français d'Algérie — Alger (Hydra), Oran, Constantine, Annaba et Tlemcen —, seuls centres agréés par France Éducation international dans le pays au 17 septembre 2026. Toutes proposent des sessions sur ordinateur. Aucune école privée n'est agréée."),
        ("Comment s'inscrire au TCF Canada à l'Institut français d'Algérie&nbsp;?",
         "Uniquement en ligne, sur la plateforme IFAL (forms.vfsglobal.com.dz/IFAL), opérée par VFS Global, accessible depuis la page TCF de if-algerie.com : création de compte, choix de la déclinaison, de l'antenne et de la session, paiement en ligne. L'Institut précise que « les inscriptions et les paiements se font exclusivement en ligne » ; aucune inscription sur place n'est possible."),
        ("Combien coûte le TCF Canada en Algérie&nbsp;?",
         "L'Institut français d'Algérie ne publie pas le tarif sur son site : le prix s'affiche sur la plateforme IFAL au moment de choisir la session et se paie en ligne. Les montants de 70 000 à 100 000 DA « selon le niveau » qui circulent sont ceux d'un site frauduleux, pas ceux du test. Pour repère, l'examen civique organisé par le même Institut coûte 9 000 DA."),
        ("Quand ont lieu les sessions&nbsp;?",
         "« Des sessions TCF sont ouvertes tous les mois sur les cinq antennes », indique la FAQ de l'Institut. Il n'y a pas de calendrier annuel : les dates apparaissent sur la plateforme à l'ouverture des inscriptions et disparaissent quand la session est pleine. Un délai de 26 jours est obligatoire entre deux inscriptions."),
        ("Quelle pièce d'identité faut-il&nbsp;?",
         "Pour les candidats algériens, la carte d'identité biométrique ou le passeport ; pour les autres nationalités, le passeport biométrique ou la carte consulaire. La pièce présentée à l'inscription doit être celle du jour de l'examen, et c'est son identité qui figurera sur l'attestation lue par IRCC."),
        ("Comment reconnaître le faux site if-algerie.fr&nbsp;?",
         "Par son domaine, différent du site officiel if-algerie.com ; par son offre — un « candidat partenaire » qui passe l'examen à votre place, une attestation « sous 24 heures », un prix de 70 000 à 100 000 DA « selon le niveau » — et par la demande d'envoyer vos papiers d'identité par e-mail. Une attestation ainsi obtenue n'existe pas dans les registres de FEI et sera détectée par IRCC."),
        ("Combien de temps pour recevoir l'attestation, et combien de temps est-elle valable&nbsp;?",
         "L'Institut envoie l'attestation originale par e-mail, environ quinze jours après la passation pour le TCF tout public ; aucune version papier n'est remise depuis mars 2023. Elle est valable deux ans, et IRCC exige des résultats de moins de deux ans à la création du profil Entrée express comme au dépôt de la demande."),
    ],
    "also": [
        ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", "Les quatre épreuves, la conversion NCLC, les seuils pour Entrée express."),
        ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", "458 en compréhension orale, 453 à l'écrit — la table de conversion officielle complète."),
        ("/blog/tcf-canada-maroc/", "TCF Canada au Maroc : les 16 centres et l'inscription", "2 900 dirhams, des sessions plusieurs fois par semaine à Casablanca, l'inscription en ligne."),
        ("/blog/ou-passer-le-tcf-canada-en-france/", "Où passer le TCF Canada en France&nbsp;?", "Les centres qui le proposent, de 195 à 285 €, et leurs dates de session."),
    ],
    "sources": """<strong>Sources.</strong> Liste des centres de passation TCF de France Éducation
international (filtre « Algérie »), consultée le 17 septembre 2026 ; site de l'Institut français
d'Algérie (if-algerie.com) — pages « TCF », « FAQ » et « Examen civique », consultées le
17 septembre 2026 ; plateforme d'inscription IFAL (forms.vfsglobal.com.dz/IFAL), page d'accueil
consultée le 17 septembre 2026 ; site frauduleux if-algerie.fr constaté le 17 septembre 2026.
Les modalités et tarifs changent sans préavis : vérifiez-les sur if-algerie.com avant de payer.""",
}

# ---------------------------------------------------------------------------
# 7. TCF Canada au Maroc
# ---------------------------------------------------------------------------
MA = {
    "slug": "tcf-canada-maroc",
    "accent": "accent-tcf",
    "crumb": "TCF Canada au Maroc",
    "title": "TCF Canada au Maroc : les 16 centres et l'inscription",
    "desc": "2 900 dirhams, des sessions plusieurs fois par semaine à Casablanca, l'inscription en ligne sur le site de chaque Institut : le guide des 16 centres.",
    "og_title": "TCF Canada au Maroc : les 16 centres et l'inscription",
    "og_desc": "2 900 dirhams, des sessions plusieurs fois par semaine à Casablanca, l'inscription en ligne sur le site de chaque Institut français.",
    "h1": "TCF Canada au Maroc : les 16 centres agréés, le prix et l'inscription",
    "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": 9,
    "intro": """Au Maroc, le TCF Canada se passe dans le réseau de l'<strong>Institut français du Maroc</strong>
— douze sites, de Tanger à Agadir — et dans deux Alliances françaises, Safi et Ouarzazate : seize
centres agréés par France Éducation international. Le tarif est le même partout,
<strong>2 900 dirhams</strong>, le test se passe <strong>sur ordinateur</strong>, et l'inscription se
fait <strong>en ligne, sur le site de l'Institut de votre ville</strong>, session par session. À
Casablanca, il y en a plusieurs par semaine.""",
    "facts": [
        "<strong>16 centres agréés</strong> (liste FEI du 17 septembre 2026) : les Instituts français d'Agadir, Béni Mellal, Casablanca, El Jadida, Essaouira, Fès, Kénitra, Marrakech, Meknès, Nador, Oujda, Rabat, Tanger et Tétouan, plus les Alliances françaises de Safi et de Ouarzazate.",
        "<strong>2 900 Dhs</strong> pour le TCF Canada, tarif national de l'Institut français du Maroc (relevé à Casablanca et Rabat le 17 septembre 2026) ; TCF Québec et TEF Canada au même prix, TCF IRN et tout public à 1 900 Dhs.",
        "Inscription <strong>en ligne, sur le site de l'Institut de votre ville</strong> : on choisit la session et on paie dans le panier ; seul le TCF IRN s'inscrit sur place.",
        "<strong>Plusieurs sessions par semaine à Casablanca</strong> (mardi, jeudi, samedi, deux créneaux), neuf à Rabat d'ici fin novembre ; certaines affichaient déjà « complet » le 17 septembre.",
        "<strong>20 jours</strong> minimum entre deux TCF, « toute version confondue », sous peine d'annulation sans remboursement.",
        "⚠️ Frais <strong>non remboursables</strong> ; report possible uniquement sur justificatif, sous 5 jours ouvrés, et <strong>facturé 500 Dhs</strong>.",
    ],
    "toc": [
        ("centres", "Les seize centres agréés"),
        ("inscription", "S'inscrire en ligne, pas à pas"),
        ("sessions", "Les sessions relevées : Casablanca, Rabat, Tanger, Marrakech"),
        ("prix", "Combien ça coûte"),
        ("regles", "Les règles à connaître avant de payer"),
        ("pieges", "Les pièges"),
    ],
    "body": """
<h2 id="centres">Les seize centres agréés</h2>

<p>Au 17 septembre 2026, la liste de France Éducation international compte seize centres de
passation du TCF au Maroc. Quatorze appartiennent au réseau de l'Institut français du Maroc — dont
Béni Mellal, hébergé par Universal Sup et rattaché à Casablanca, et Nador, rattaché à Oujda — ;
les deux autres sont les Alliances françaises de Safi et de Ouarzazate. Tous proposent des sessions
sur ordinateur, sauf Ouarzazate.</p>

<div class="tablewrap wide">
<table>
<caption>Centres de passation TCF au Maroc, liste officielle de FEI consultée le 17 septembre 2026. SO = sessions sur ordinateur.</caption>
<thead><tr><th>Ville</th><th>Centre</th><th>SO</th><th>Relevé le 17 septembre 2026</th></tr></thead>
<tbody>
<tr><td><strong>Casablanca</strong></td><td>Institut français, 123 bd Zerktouni</td><td><span class="badge ok">oui</span></td><td>TCF Canada 2 900 Dhs ; sessions les mardis, jeudis et samedis, deux créneaux (8 h 30 et 10 h), du 26 septembre à décembre 2026 ; trois affichaient « complet ».</td></tr>
<tr><td><strong>Rabat</strong></td><td>Institut français, 15 rue Al Madina, Hassan</td><td><span class="badge ok">oui</span></td><td>2 900 Dhs ; neuf sessions du 25 septembre au 24 novembre 2026, toutes ouvertes.</td></tr>
<tr><td><strong>Marrakech</strong></td><td>Institut français, route de Targa, Guéliz</td><td><span class="badge ok">oui</span></td><td>2 900 Dhs ; session du mardi 20 octobre 2026, 9 h-12 h 30.</td></tr>
<tr><td><strong>Tanger</strong></td><td>Institut français, 41 rue Hassan-Ibn-Ouazzane</td><td><span class="badge ok">oui</span></td><td>2 900 Dhs ; session du jeudi 15 octobre 2026.</td></tr>
<tr><td><strong>Béni Mellal</strong></td><td>Universal Sup, 210 bd Ibn-Khaldoun (via IF Casablanca)</td><td><span class="badge ok">oui</span></td><td>Sessions des samedis 24 octobre et 14 novembre 2026, à réserver sur le site de Casablanca.</td></tr>
<tr><td><strong>Fès</strong></td><td>Institut français, 12 rue Serghini</td><td><span class="badge ok">oui</span></td><td>Page TCF Canada du site.</td></tr>
<tr><td><strong>Agadir</strong></td><td>Institut français, rue de l'Entraide, Talborjt</td><td><span class="badge ok">oui</span></td><td>Page TCF Canada du site.</td></tr>
<tr><td><strong>Meknès</strong></td><td>Institut français, rue Ferhat-Hachad</td><td><span class="badge ok">oui</span></td><td>Page TCF Canada du site.</td></tr>
<tr><td><strong>Oujda · Nador</strong></td><td>Institut français d'Oujda (Nador : école Paul-Riquet)</td><td><span class="badge ok">oui</span></td><td>Page TCF Canada du site d'Oujda.</td></tr>
<tr><td><strong>Kénitra</strong></td><td>Institut français, rue Khalid-Ibn-Walid</td><td><span class="badge ok">oui</span></td><td>Page TCF Canada du site.</td></tr>
<tr><td><strong>Tétouan</strong></td><td>Institut français, 13 rue Chakib-Arsalane</td><td><span class="badge ok">oui</span></td><td>Page TCF Canada du site.</td></tr>
<tr><td><strong>El Jadida</strong></td><td>Institut français, 3 rue du Caire</td><td><span class="badge ok">oui</span></td><td>Page TCF Canada du site.</td></tr>
<tr><td><strong>Essaouira</strong></td><td>Institut français, 9 rue Mohammed-Diouri</td><td><span class="badge ok">oui</span></td><td>Page TCF Canada du site.</td></tr>
<tr><td><strong>Safi</strong></td><td>Alliance française de Safi</td><td><span class="badge ok">oui</span></td><td>Page TCF Canada sur if-maroc.org/safi.</td></tr>
<tr><td><strong>Ouarzazate</strong></td><td>Alliance française de Ouarzazate</td><td><span class="badge no">non</span></td><td>Papier ; contact par le centre.</td></tr>
</tbody>
</table>
</div>

%(serie)s

<h2 id="inscription">S'inscrire en ligne, pas à pas</h2>

<p>La consigne de l'Institut est la même sur tous ses sites : « Pour les TCF et TEF :
simplifiez-vous la vie et inscrivez-vous exclusivement en ligne sur le site web de l'IF où vous
souhaitez passer votre examen. » Chaque site — if-maroc.org/casablanca, /rabat, /marrakech… — a sa
page « TCF Canada » avec ses propres sessions et un panier.</p>

<ol>
<li><strong>Ouvrez la page « TCF Canada » de l'Institut de votre ville</strong> (menu
« Certifications »). Elle affiche la prochaine session — date, horaire, adresse, prix — et un
lien « Choisissez une autre session » qui liste toutes les dates ouvertes, avec la mention
« Complet » pour celles qui le sont.</li>
<li><strong>Ajoutez la session au panier et payez en ligne.</strong> L'inscription n'est
définitive qu'une fois payée. Les conditions d'inscription de l'Institut demandent une
<strong>pièce d'identité</strong> et une <strong>photo format passeport</strong>, et vous
remettent une convocation personnelle dès l'inscription.</li>
<li><strong>Vérifiez vos données.</strong> Nom, prénom, date de naissance : ils figureront tels
quels sur l'attestation, et l'Institut facture <strong>110 Dhs</strong> toute modification après
l'épreuve.</li>
<li><strong>Le jour J</strong>, la convocation et la carte d'identité nationale (ou le passeport)
sont exigées à l'entrée ; « les candidats sans pièce d'identité avec photo ne seront pas
acceptés ». Le test se passe sur ordinateur, dans les locaux de l'Institut ; les créneaux de
Casablanca s'étendent de 8 h 30 à 15 h, l'expression orale étant planifiée dans la journée.</li>
<li><strong>Récupérez l'attestation</strong> à l'accueil de votre centre : « Chaque candidat
présent aux épreuves se verra remettre une attestation ou un diplôme nominatif en se rendant à
l'accueil de son centre d'examen de rattachement. »</li>
</ol>

<div class="note">
<p><strong>Deux exceptions à l'inscription en ligne :</strong> le TCF IRN — « inscription
uniquement sur place, à l'accueil de l'Institut français » — et les candidats à besoins
spécifiques (tiers-temps, aménagements), qui doivent s'inscrire à l'accueil avec un certificat
médical, « pas d'inscription en ligne possible ».</p>
</div>

<h2 id="sessions">Les sessions relevées : Casablanca, Rabat, Tanger, Marrakech</h2>

<p>Contrairement à l'Algérie, où les places sont comptées, le Maroc offre de la
<strong>fréquence</strong>. Le 17 septembre 2026, le site de Casablanca listait des sessions de
TCF Canada sur ordinateur <strong>les mardis, jeudis et samedis</strong>, avec deux créneaux
chacune (8 h 30-15 h et 10 h-15 h), du 26 septembre jusqu'en décembre — soit plus de vingt-quatre
sessions d'ici la fin novembre —, trois seulement affichant « Complet » (le 26 septembre à 10 h,
le 10 octobre aux deux créneaux). Le même site vend les sessions de Béni Mellal, les samedis
24 octobre et 14 novembre.</p>

<p>Rabat listait <strong>neuf sessions</strong>, toutes ouvertes, du vendredi 25 septembre au
mardi 24 novembre ; Tanger, le jeudi 15 octobre ; Marrakech, le mardi 20 octobre. Le calendrier
annuel 2026 publié par l'Institut ne couvre que le DELF-DALF et le TCF tout public : pour le TCF
Canada, la seule source est la page de chaque site, et elle change chaque semaine.</p>

<h2 id="prix">Combien ça coûte</h2>

<div class="tablewrap">
<table>
<caption>Grille de l'Institut français du Maroc, relevée sur les pages « Certifications » de Casablanca et de Rabat le 17 septembre 2026 — identique sur les deux sites.</caption>
<thead><tr><th>Test</th><th>Tarif</th><th>Inscription</th></tr></thead>
<tbody>
<tr><td><strong>TCF Canada</strong></td><td><strong>2 900 Dhs</strong></td><td>En ligne, sur ordinateur</td></tr>
<tr><td><a href="/tcf-quebec/">TCF Québec</a></td><td>2 900 Dhs</td><td>En ligne</td></tr>
<tr><td><a href="/tef-canada/">TEF Canada</a></td><td>2 900 Dhs</td><td>En ligne</td></tr>
<tr><td><a href="/tcf-irn/">TCF IRN</a></td><td>1 900 Dhs</td><td>Sur place uniquement</td></tr>
<tr><td>TCF tout public</td><td>1 900 Dhs</td><td>En ligne</td></tr>
</tbody>
</table>
</div>

<p>Soit de l'ordre de 270 € pour le TCF Canada — entre le tarif d'un
centre français (195 à 285 €) et celui d'un centre canadien (390 à 440 $). Un TCF raté se repaie
en entier : il n'existe aucune reprise partielle, et le report d'une session est lui-même payant
(voir ci-dessous). Nos <a href="/examens-blancs/">examens blancs</a> notés sur 699 et convertis en
NCLC vous disent si la session de la semaine prochaine est la bonne.</p>

<h2 id="regles">Les règles à connaître avant de payer</h2>

<ul>
<li><strong>Vingt jours de carence.</strong> « Le candidat ne peut se présenter deux fois à un test
du TCF toute version confondue dans un délai inférieur à 20 jours. Si un candidat contrevient à
cette règle, son inscription sera annulée sans remboursement possible. » Cet avertissement est en
tête de chaque page TCF Canada.</li>
<li><strong>Aucun remboursement.</strong> « En cas d'annulation d'inscription, le candidat ne
pourra, en aucun cas, être remboursé des frais d'inscription versés. »</li>
<li><strong>Changement de date : avant la clôture seulement.</strong> Tant que la période
d'inscription de la session n'est pas close, on peut changer de date ou de version ; après, plus
rien — sauf maladie, décès d'un proche, accident ou examen officiel, sur justificatif envoyé
« au plus tard dans les 5 jours ouvrés suivant le jour de l'épreuve », et « ce report de session
d'examen sera facturé à 500,00 Dhs au candidat ».</li>
<li><strong>Les résultats.</strong> L'attestation se retire à l'accueil du centre. L'Institut ne
donne pas de délai précis pour le TCF Canada ; son calendrier 2026 annonce « 1 mois plus tard »
pour le TCF tout public sur papier. Comptez donc un mois, et calez votre date d'examen sur
l'échéance de votre dossier en conséquence.</li>
<li><strong>Plus de recorrection</strong> pour les sessions à partir du 1<sup>er</sup> septembre
2026 : le score est définitif.</li>
</ul>

<h2 id="pieges">Les pièges</h2>

<ul>
<li><strong>TCF Canada ou TCF Québec ?</strong> Même prix, même plateforme, deux tests : le TCF
Québec, modulaire, sert aux programmes du MIFI ; IRCC ne l'accepte pas. Pour Entrée express,
c'est le TCF Canada, ou le TEF Canada.</li>
<li><strong>Le B2 qui n'est pas un NCLC 7.</strong> IRCC convertit le score sur 699 en NCLC : il faut
458 en compréhension orale et 453 à l'écrit pour le NCLC 7, pas « un B2 ». Le détail est dans
<a href="/blog/tcf-canada-nclc-7/">NCLC 7 au TCF Canada</a>.</li>
<li><strong>La validité.</strong> Deux ans, et IRCC les compte à la création du profil comme au
dépôt : <a href="/blog/validite-attestation-tcf-tef/">deux ans à partir de quand&nbsp;?</a></li>
<li><strong>Les intermédiaires.</strong> L'inscription se fait sur if-maroc.org, sans frais de
dossier ni « agent ». Un site qui vous vend une place, une attestation « garantie » ou un TCF
« à distance » vend une fraude — voir notre guide sur
<a href="/blog/tcf-canada-algerie/#faux-site">le faux Institut français d'Algérie</a>, dont le
modèle circule aussi au Maroc.</li>
</ul>
""" % {"serie": serie("/blog/tcf-canada-maroc/")},
    "cta_h2": "2 900 dirhams par tentative, et un score définitif",
    "cta_p": """Les sessions ne manquent pas au Maroc ; ce qui manque, c'est la certitude d'avoir le score.
Les examens blancs de l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent les quatre
épreuves du TCF Canada au format officiel, notées sur 699 et converties en NCLC, avec la
correction IA de l'écrit et de l'oral — pour choisir sa date en connaissance de cause.""",
    "faq": [
        ("Où passer le TCF Canada au Maroc&nbsp;?",
         "Dans l'un des seize centres agréés par France Éducation international : les Instituts français d'Agadir, Béni Mellal, Casablanca, El Jadida, Essaouira, Fès, Kénitra, Marrakech, Meknès, Nador, Oujda, Rabat, Tanger et Tétouan, et les Alliances françaises de Safi et de Ouarzazate. Tous le proposent sur ordinateur, sauf Ouarzazate."),
        ("Combien coûte le TCF Canada au Maroc&nbsp;?",
         "2 900 dirhams, tarif de l'Institut français du Maroc relevé à Casablanca et à Rabat le 17 septembre 2026 — identique pour le TCF Québec et le TEF Canada. Le TCF IRN et le TCF tout public coûtent 1 900 dirhams. Les frais ne sont pas remboursables, et un report de session sur justificatif est facturé 500 dirhams."),
        ("Comment s'inscrire&nbsp;?",
         "En ligne, sur le site de l'Institut français de votre ville (if-maroc.org/casablanca, /rabat, etc.), page « TCF Canada » : on choisit une session dans la liste, on l'ajoute au panier et on paie. Une convocation est remise dès l'inscription ; pièce d'identité et photo format passeport sont demandées. Seuls le TCF IRN et les candidats à besoins spécifiques s'inscrivent sur place."),
        ("Quand ont lieu les sessions&nbsp;?",
         "Elles dépendent de chaque site. Le 17 septembre 2026, Casablanca proposait des sessions les mardis, jeudis et samedis jusqu'en décembre, avec deux créneaux par jour ; Rabat neuf sessions entre le 25 septembre et le 24 novembre ; Tanger le 15 octobre ; Marrakech le 20 octobre. Il n'existe pas de calendrier annuel du TCF Canada : la page du site fait foi."),
        ("Peut-on repasser le TCF Canada rapidement&nbsp;?",
         "Pas avant vingt jours : « Le candidat ne peut se présenter deux fois à un test du TCF toute version confondue dans un délai inférieur à 20 jours », sous peine d'annulation sans remboursement. Et depuis les sessions du 1er septembre 2026, aucune recorrection n'est possible : améliorer son score, c'est repasser les quatre épreuves et repayer 2 900 dirhams."),
        ("Combien de temps pour les résultats&nbsp;?",
         "L'attestation se retire à l'accueil du centre d'examen. L'Institut ne publie pas de délai pour le TCF Canada ; son calendrier 2026 indique « 1 mois plus tard » pour le TCF tout public. Comptez un mois, puis deux ans de validité — qu'IRCC exige à la création du profil et au dépôt de la demande."),
        ("Quels documents apporter le jour de l'examen&nbsp;?",
         "La convocation et une pièce d'identité avec photo — carte d'identité nationale ou passeport — sont obligatoires ; sans elles, l'accès à la salle est refusé. Vérifiez avant l'épreuve l'orthographe de vos nom, prénom et date de naissance : toute modification ultérieure sur l'attestation est facturée 110 dirhams."),
    ],
    "also": [
        ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", "Les quatre épreuves, la conversion NCLC, les seuils pour Entrée express."),
        ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir pour votre dossier&nbsp;?", "Les deux tables NCLC, le comparatif de format, et le piège de l'« ancien score »."),
        ("/blog/tcf-canada-algerie/", "TCF Canada en Algérie : où le passer, comment s'inscrire", "Cinq antennes, la plateforme IFAL, 26 jours entre deux inscriptions et un faux site à éviter."),
        ("/blog/tcf-canada-tunisie/", "TCF Canada en Tunisie : centres, calendrier, inscription", "880 dinars, un rendez-vous en ligne puis l'inscription sur place, des résultats en cinq semaines."),
    ],
    "sources": """<strong>Sources.</strong> Liste des centres de passation TCF de France Éducation
international (filtre « Maroc »), consultée le 17 septembre 2026 ; site de l'Institut français du
Maroc (if-maroc.org) — page nationale « TCF Canada », pages « Certifications » et « TCF Canada » des
sites de Casablanca, Rabat, Marrakech et Tanger, liste des sessions de Casablanca, Rabat et
Marrakech, « Conditions d'inscription à un examen TCF, TEF, DELF/DALF » (juillet 2024) et
calendrier des certifications 2026, consultés le 17 septembre 2026. Les tarifs et sessions
changent sans préavis : vérifiez-les sur le site de votre Institut avant de payer.""",
}

# ---------------------------------------------------------------------------
# 8. TCF Canada en Tunisie
# ---------------------------------------------------------------------------
TN = {
    "slug": "tcf-canada-tunisie",
    "accent": "accent-tcf",
    "crumb": "TCF Canada en Tunisie",
    "title": "TCF Canada en Tunisie : centres, calendrier, inscription",
    "desc": "880 dinars, un rendez-vous en ligne puis l'inscription sur place, une session par mois dans sept pôles, des résultats en cinq semaines : le guide vérifié.",
    "og_title": "TCF Canada en Tunisie : centres, calendrier, inscription",
    "og_desc": "880 dinars, un rendez-vous en ligne puis l'inscription sur place, une session par mois dans sept pôles, des résultats en cinq semaines.",
    "h1": "TCF Canada en Tunisie : les centres, le calendrier et l'inscription",
    "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": 9,
    "intro": """En Tunisie, le TCF Canada se passe à l'<strong>Institut français de Tunisie</strong> — sept
pôles, de Tunis à Kébili — et dans le réseau des <strong>Alliances françaises</strong> (Tunis,
Bizerte, Djerba, Gabès, Gafsa, Kairouan) : quatorze centres agréés par France Éducation
international. À l'Institut, le test coûte <strong>880 dinars</strong>, se réserve <strong>en
ligne</strong> puis se finalise <strong>sur place</strong> à une date d'inscription fixée par pôle,
avec <strong>une session par mois</strong> et des résultats <strong>cinq semaines</strong> plus tard.""",
    "facts": [
        "<strong>14 centres agréés</strong> (liste FEI du 17 septembre 2026) : 8 pôles de l'Institut français de Tunisie et 6 Alliances françaises, tous avec des sessions sur ordinateur.",
        "<strong>880 DT</strong> à l'Institut français pour le TCF Canada (17 septembre 2026) ; TCF Québec 880 DT, TCF IRN 625 DT, TCF tout public 335 DT + 220 DT par épreuve d'expression.",
        "Procédure en deux temps : <strong>rendez-vous en ligne</strong> pendant une fenêtre d'une semaine, puis <strong>inscription et paiement sur place</strong> le jour fixé — un mandataire muni d'une copie de votre carte d'identité peut y aller pour vous.",
        "<strong>Une session par mois</strong> dans chaque pôle : à Tunis, 24-25 septembre, 22-23 octobre, 26-27 novembre et 16-18 décembre 2026.",
        "Résultats <strong>cinq semaines</strong> après la passation ; <strong>30 jours</strong> entre deux sessions de TCF ou de TEF.",
        "⚠️ Frais <strong>non remboursables</strong> ; paiement en espèces (carte bancaire à Tunis seulement), chèques suspendus.",
    ],
    "toc": [
        ("centres", "Les quatorze centres agréés"),
        ("inscription", "S'inscrire à l'Institut français, pas à pas"),
        ("calendrier", "Le calendrier 2026 de Tunis, et le rythme des autres pôles"),
        ("prix", "Combien ça coûte"),
        ("resultats", "Résultats, délais et reprise"),
        ("alliances", "Les Alliances françaises"),
        ("pieges", "Les pièges"),
    ],
    "body": """
<h2 id="centres">Les quatorze centres agréés</h2>

<p>La liste officielle de France Éducation international recense quatorze centres de passation
du TCF en Tunisie. Huit relèvent de l'Institut français de Tunisie (IFT) — le centre de langue de
Tunis, avenue de Paris, et ses pôles d'El Mourouj, Nabeul-Hammamet, Béja, Sousse, Sfax, Kébili
et Médenine — et six sont des Alliances françaises : Tunis (Ariana), Bizerte, Djerba, Gabès,
Gafsa et Kairouan. Sur le site de l'IFT, le <strong>TCF Canada</strong> est proposé dans sept
pôles ; Médenine n'apparaît que pour le TCF tout public.</p>

<div class="tablewrap wide">
<table>
<caption>Centres de passation TCF en Tunisie, liste officielle de FEI consultée le 17 septembre 2026, et ce que le site de l'Institut français indiquait ce jour-là.</caption>
<thead><tr><th>Ville</th><th>Centre</th><th>TCF Canada</th><th>Relevé le 17 septembre 2026</th></tr></thead>
<tbody>
<tr><td><strong>Tunis</strong></td><td>Institut français de Tunisie, centre de langue, 20-22 av. de Paris</td><td><span class="badge ok">oui</span></td><td>880 DT ; sessions 24-25 sept., 22-23 oct., 26-27 nov., 16 et 18 déc. 2026 ; paiement espèces ou carte.</td></tr>
<tr><td><strong>El Mourouj</strong></td><td>IFT, pôle d'El Mourouj 1</td><td><span class="badge ok">oui</span></td><td>880 DT ; sessions mensuelles ; paiement en espèces.</td></tr>
<tr><td><strong>Nabeul · Hammamet</strong></td><td>IFT, pôle de Nabeul-Hammamet</td><td><span class="badge ok">oui</span></td><td>880 DT ; sessions mensuelles ; espèces.</td></tr>
<tr><td><strong>Sousse</strong></td><td>IFT, pôle de Sousse, 15 rue Hamed-El-Ghazeli</td><td><span class="badge ok">oui</span></td><td>880 DT ; sessions mensuelles ; espèces.</td></tr>
<tr><td><strong>Sfax</strong></td><td>IFT, centre de langue, 9 av. Habib-Bourguiba</td><td><span class="badge ok">oui</span></td><td>880 DT ; sessions mensuelles.</td></tr>
<tr><td><strong>Béja</strong></td><td>IFT, pôle de Béja (lycée privé L'Avenir)</td><td><span class="badge ok">oui</span></td><td>880 DT ; sessions mensuelles ; espèces.</td></tr>
<tr><td><strong>Kébili</strong></td><td>IFT, pôle de Kébili (lycée privé Ibnou-Khaldoun)</td><td><span class="badge ok">oui</span></td><td>880 DT ; sessions mensuelles.</td></tr>
<tr><td><strong>Médenine</strong></td><td>IFT, pôle de Médenine-Tataouine (centre TUTECH)</td><td><span class="badge part">TP seulement</span></td><td>Pas de TCF Canada dans la liste des pôles du site.</td></tr>
<tr><td><strong>Tunis (Ariana)</strong></td><td>Alliance française de Tunis, El Menzah 6</td><td><span class="badge ok">oui</span></td><td>TCF Canada, Québec et tout public ; calendrier sur alliancefr.tn ; tarif non relevé.</td></tr>
<tr><td><strong>Bizerte</strong></td><td>Alliance française de Bizerte</td><td>—</td><td>Sur le site du centre.</td></tr>
<tr><td><strong>Djerba</strong></td><td>Alliance française de Djerba (Houmt Souk)</td><td>—</td><td>Sur le site du centre.</td></tr>
<tr><td><strong>Gabès</strong></td><td>Alliance française de Gabès</td><td>—</td><td>Contact par le centre.</td></tr>
<tr><td><strong>Gafsa</strong></td><td>Alliance française de Gafsa</td><td>—</td><td>Contact par le centre.</td></tr>
<tr><td><strong>Kairouan</strong></td><td>Alliance française de Kairouan</td><td>—</td><td>Page Facebook du centre.</td></tr>
</tbody>
</table>
</div>

%(serie)s

<h2 id="inscription">S'inscrire à l'Institut français, pas à pas</h2>

<p>L'Institut a un système en deux temps, différent de tout ce qui se fait en France ou au
Maroc : « Prenez un rendez-vous en ligne pour réserver votre test et finaliser votre inscription
sur place. » Chaque session a donc trois dates, publiées à l'avance sur la page TCF Canada de
l'IFT : une fenêtre de <strong>prise de rendez-vous en ligne</strong>, un <strong>jour
d'inscription</strong> au pôle, et les <strong>jours du test</strong>.</p>

<ol>
<li><strong>Choisissez votre pôle</strong> sur la page « TCF Canada » de institutfrancais-tunisie.com
et lisez son tableau « Sessions 2026 » : dates de rendez-vous, d'inscription, de test.</li>
<li><strong>Réservez en ligne pendant la fenêtre de rendez-vous</strong> (environ une semaine, trois
à quatre semaines avant le test). « Les inscriptions sont ouvertes dans la limite des places
disponibles » : une fenêtre passée, c'est la session suivante.</li>
<li><strong>Le jour d'inscription, présentez-vous au pôle</strong> avec votre pièce d'identité et
le montant — <strong>880 DT</strong>, en espèces ou par carte bancaire à Tunis, en espèces
seulement dans les autres pôles ; « le paiement par chèque est suspendu temporairement ».
Vous ne pouvez pas venir ? « Le candidat peut être représenté par une autre personne munie de la
photocopie de la carte d'identité du candidat. »</li>
<li><strong>Le jour du test</strong>, convocation et pièce d'identité. La session s'étend sur deux
jours ; votre convocation précise vos créneaux.</li>
<li><strong>Cinq semaines plus tard</strong>, les résultats — puis l'attestation, valable deux
ans.</li>
</ol>

<h2 id="calendrier">Le calendrier 2026 de Tunis, et le rythme des autres pôles</h2>

<div class="tablewrap">
<table>
<caption>Sessions de TCF Canada du pôle de Tunis, page « TCF Canada » de l'Institut français de Tunisie consultée le 17 septembre 2026.</caption>
<thead><tr><th>Session</th><th>Rendez-vous en ligne</th><th>Inscription sur place</th><th>Test</th></tr></thead>
<tbody>
<tr><td>Septembre 2026</td><td>24-30 août</td><td>3 septembre</td><td><strong>24 et 25 septembre</strong></td></tr>
<tr><td>Octobre 2026</td><td>14-20 septembre</td><td>24 septembre</td><td><strong>22 et 23 octobre</strong></td></tr>
<tr><td>Novembre 2026</td><td>26-31 octobre</td><td>5 novembre</td><td><strong>26 et 27 novembre</strong></td></tr>
<tr><td>Décembre 2026</td><td>9-15 novembre</td><td>19 novembre</td><td><strong>16 et 18 décembre</strong></td></tr>
</tbody>
</table>
</div>

<p>Le mécanisme est le même dans les six autres pôles, avec leurs propres dates — Sousse, Sfax,
Nabeul-Hammamet, El Mourouj, Béja et Kébili affichent chacun une session par mois jusqu'en
décembre, parfois jusqu'en janvier 2027. Un rendez-vous manqué se rattrape le mois suivant, dans
le même pôle ou dans un autre. Le tableau de chaque pôle indique aussi les dates de l'atelier de
préparation de 20 heures que l'Institut propose avant chaque session (270 DT, ou 1 100 DT avec le
test).</p>

<h2 id="prix">Combien ça coûte</h2>

<div class="tablewrap">
<table>
<caption>Frais d'inscription de l'Institut français de Tunisie, pages TCF Canada, TCF Québec et TCF TP-SO / IRN, consultées le 17 septembre 2026.</caption>
<thead><tr><th>Test</th><th>Tarif IFT</th></tr></thead>
<tbody>
<tr><td><strong>TCF Canada</strong>, 4 épreuves</td><td><strong>880 DT</strong></td></tr>
<tr><td><a href="/tcf-quebec/">TCF Québec</a>, 4 épreuves</td><td>880 DT (packs à 2 ou 3 épreuves avec atelier : 660 et 880 DT)</td></tr>
<tr><td><a href="/tcf-irn/">TCF IRN</a></td><td>625 DT</td></tr>
<tr><td>TCF tout public sur ordinateur, épreuves obligatoires</td><td>335 DT (+ 220 DT par épreuve d'expression)</td></tr>
<tr><td>Atelier de préparation (20 h)</td><td>270 DT</td></tr>
</tbody>
</table>
</div>

<p>Soit de l'ordre de 260 € pour le TCF Canada — comparable au Maroc (2 900 Dhs) et à la France
(195 à 285 €). Les frais « ne sont pas remboursables » ; seul un cas de force majeure — maladie,
décès d'un proche, grève — justifié « dans un délai de 48 heures » ouvre droit à un report.</p>

<h2 id="resultats">Résultats, délais et reprise</h2>

<p>« Les résultats sont disponibles 5 semaines après la date de passation », indique la FAQ de
l'Institut — c'est le délai le plus long que nous ayons relevé, deux fois celui des centres
français. Avec une session par mois, un candidat qui rate son NCLC en septembre ne connaît son
score que fin octobre, se réinscrit pour décembre, et reçoit la nouvelle attestation fin janvier.
Prévoyez cette chaîne dans le calendrier de votre dossier — d'autant qu'IRCC exige des résultats
de moins de deux ans à deux moments, comme l'explique
<a href="/blog/validite-attestation-tcf-tef/">deux ans à partir de quand&nbsp;?</a></p>

<p>Entre deux tests, l'Institut applique <strong>30 jours</strong> — « il faut respecter un délai
de 30 jours entre deux sessions de TCF ou de TEF » —, le chiffre haut de la fourchette de FEI. Et
depuis les sessions du 1<sup>er</sup> septembre 2026, aucune recorrection n'est possible : le
score est définitif. Ce qu'il vaut en NCLC — 458 en compréhension orale, 453 à l'écrit pour le
NCLC 7 — est dans <a href="/blog/tcf-canada-nclc-7/">NCLC 7 au TCF Canada</a>.</p>

<h2 id="alliances">Les Alliances françaises</h2>

<p>L'Alliance française de Tunis, à El Menzah 6 (Ariana), « propose le TCF Canada, le TCF Québec et
le TCF tout public », avec un calendrier des examens sur son site ; les Alliances de Bizerte,
Djerba, Gabès, Gafsa et Kairouan figurent sur la liste de FEI avec l'option « sessions sur
ordinateur ». Leur procédure et leurs tarifs ne sont pas publiés de façon lisible en ligne : appelez
le centre. Pour un candidat de Bizerte ou de Djerba, c'est l'alternative aux déplacements vers
Tunis ou Sfax.</p>

<h2 id="pieges">Les pièges</h2>

<ul>
<li><strong>Manquer la fenêtre de rendez-vous.</strong> Une semaine, un mois avant le test : c'est
elle qu'il faut noter, pas la date de l'examen.</li>
<li><strong>Venir sans espèces.</strong> Hors Tunis, l'inscription se paie en espèces ; les chèques
sont refusés.</li>
<li><strong>Confondre TCF Canada et TCF Québec.</strong> Même prix à l'Institut, deux usages : le
Québec pour le MIFI, le Canada pour IRCC.</li>
<li><strong>Sous-estimer le délai.</strong> Cinq semaines de résultats plus 30 jours de carence :
une deuxième tentative, c'est deux à trois mois.</li>
<li><strong>Les intermédiaires.</strong> L'Institut n'a ni agent ni revendeur ; toute offre de
place « garantie » ou de TCF « à distance » est une fraude — voir
<a href="/blog/tcf-canada-algerie/#faux-site">le faux Institut français d'Algérie</a>.</li>
</ul>
""" % {"serie": serie("/blog/tcf-canada-tunisie/")},
    "cta_h2": "Cinq semaines de résultats : pas de place pour l'essai",
    "cta_p": """En Tunisie, un score insuffisant se découvre cinq semaines après, et la session suivante
est un mois plus loin. Les examens blancs de l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;»
reproduisent les quatre épreuves du TCF Canada au format officiel, notées sur 699 et converties en
NCLC, avec la correction IA de l'écrit et de l'oral — pour ne réserver que la session utile.""",
    "faq": [
        ("Où passer le TCF Canada en Tunisie&nbsp;?",
         "Dans l'un des quatorze centres agréés par France Éducation international : l'Institut français de Tunisie — Tunis, El Mourouj, Nabeul-Hammamet, Sousse, Sfax, Béja et Kébili pour le TCF Canada — et les Alliances françaises de Tunis (Ariana), Bizerte, Djerba, Gabès, Gafsa et Kairouan. Le pôle de Médenine ne figure pas parmi ceux qui proposent le TCF Canada sur le site de l'Institut."),
        ("Combien coûte le TCF Canada en Tunisie&nbsp;?",
         "880 dinars à l'Institut français de Tunisie, relevés le 17 septembre 2026 — le même prix que le TCF Québec. Le TCF IRN coûte 625 dinars, le TCF tout public sur ordinateur 335 dinars pour les épreuves obligatoires. Les frais ne sont pas remboursables. Les Alliances françaises ne publient pas de tarif lisible en ligne."),
        ("Comment s'inscrire&nbsp;?",
         "En deux temps : un rendez-vous en ligne pendant la fenêtre ouverte pour la session (environ une semaine, un mois avant le test), puis l'inscription et le paiement sur place, au pôle choisi, le jour fixé — en espèces, ou par carte à Tunis. Le candidat peut se faire représenter par une personne munie de la photocopie de sa carte d'identité."),
        ("Quand ont lieu les sessions&nbsp;?",
         "Une par mois dans chaque pôle. À Tunis en 2026 : 24-25 septembre, 22-23 octobre, 26-27 novembre, 16 et 18 décembre, avec des rendez-vous en ligne respectivement du 24 au 30 août, du 14 au 20 septembre, du 26 au 31 octobre et du 9 au 15 novembre. Les autres pôles publient leurs propres dates sur la même page."),
        ("Combien de temps pour les résultats&nbsp;?",
         "« Les résultats sont disponibles 5 semaines après la date de passation », indique l'Institut français de Tunisie — le délai le plus long relevé dans nos guides. L'attestation est ensuite valable deux ans, et IRCC exige des résultats de moins de deux ans à la création du profil et au dépôt de la demande."),
        ("Peut-on repasser le test rapidement&nbsp;?",
         "Non : l'Institut impose « un délai de 30 jours entre deux sessions de TCF ou de TEF », et avec des résultats à cinq semaines et une session par mois, une seconde tentative prend deux à trois mois. Depuis le 1er septembre 2026, aucune recorrection n'est possible ; le score est définitif."),
        ("Que se passe-t-il si je ne peux pas venir le jour du test&nbsp;?",
         "Les frais ne sont pas remboursés. En cas de force majeure — maladie, décès d'un proche, grève —, un report est possible à condition d'adresser un justificatif au centre de langue dans un délai de 48 heures."),
    ],
    "also": [
        ("/tcf-canada/", "TCF Canada 2026 : format, scores NCLC et préparation", "Les quatre épreuves, la conversion NCLC, les seuils pour Entrée express."),
        ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", "458 en compréhension orale, 453 à l'écrit — la table de conversion officielle complète."),
        ("/blog/tcf-canada-maroc/", "TCF Canada au Maroc : les 16 centres et l'inscription", "2 900 dirhams, des sessions plusieurs fois par semaine à Casablanca, l'inscription en ligne."),
        ("/blog/tcf-canada-algerie/", "TCF Canada en Algérie : où le passer, comment s'inscrire", "Cinq antennes, la plateforme IFAL, 26 jours entre deux inscriptions et un faux site à éviter."),
    ],
    "sources": """<strong>Sources.</strong> Liste des centres de passation TCF de France Éducation
international (filtre « Tunisie »), consultée le 17 septembre 2026 ; site de l'Institut français de
Tunisie — pages « TCF-Canada » (présentation, calendrier par pôle, réservation en ligne, frais
d'inscription, frais de paiement, FAQ), « TCF-Québec » et « TCF/TP-SO & TCF/IRN », consultées le
17 septembre 2026 ; site de l'Alliance française de Tunis (pages TCF et calendriers des examens),
consulté le 17 septembre 2026. Tarifs et dates changent sans préavis : vérifiez-les sur le site de
l'Institut avant de vous déplacer.""",
}

# ---------------------------------------------------------------------------
# 9. Où passer l'examen civique ?
# ---------------------------------------------------------------------------
CIV = {
    "slug": "ou-passer-l-examen-civique",
    "accent": "accent-irn",
    "crumb": "Où passer l'examen civique",
    "title": "Où passer l'examen civique ? Centres et inscription 2026",
    "desc": "Deux réseaux agréés, 244 centres FEI, une pré-inscription en ligne, 70 à 110 € selon le centre, des résultats sous 12 heures : où passer l'examen civique.",
    "og_title": "Où passer l'examen civique ? Centres et inscription 2026",
    "og_desc": "Deux réseaux agréés, 244 centres FEI, une pré-inscription en ligne, 70 à 110 € selon le centre : où et comment passer l'examen civique.",
    "h1": "Où passer l'examen civique&nbsp;? Les centres, l'inscription et le prix",
    "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": 10,
    "intro": """L'examen civique se passe <strong>sur ordinateur, dans un centre agréé</strong> par l'un des
deux organismes habilités par le ministère de l'Intérieur : <strong>France Éducation international</strong>
— 244 centres en France, pré-inscription sur test-civique.fr — et la <strong>CCI Paris
Île-de-France</strong>, dont l'outil « Trouver une session » liste les dates centre par centre.
Obligatoire depuis le 1<sup>er</sup> janvier 2026 pour une première carte de séjour pluriannuelle,
une première carte de résident et la naturalisation, il coûte <strong>70 à 110 €</strong> selon le
centre et se repasse sans limite.""",
    "facts": [
        "<strong>Deux réseaux agréés</strong> : France Éducation international (<strong>244 centres</strong> dans 94 départements au 17 septembre 2026, dont 7 à Paris) et la CCI Paris Île-de-France (Le français des affaires).",
        "<strong>Trois mentions</strong> — carte de séjour pluriannuelle, carte de résident, naturalisation — à choisir à l'inscription ; la mention « carte de résident » vaut pour la carte pluriannuelle.",
        "<strong>40 questions</strong> à choix multiples (28 de connaissances, 12 de mise en situation), <strong>45 minutes</strong>, <strong>32 bonnes réponses</strong> pour réussir.",
        "Inscription FEI : <strong>pré-inscription en ligne sur test-civique.fr</strong>, avec votre numéro étranger (AGDREF) ; inscription CCIP : par le centre, via « Trouver une session ».",
        "Prix libre : <strong>70 € (Nantes), 75 € (Montpellier), 80-90 € (Etoile, Paris), 110 € (ACCORD, Paris)</strong> ; résultats « sous 12 heures » dans plusieurs centres.",
        "Attestation <strong>sans durée de validité</strong>, tentatives <strong>illimitées</strong> ; la préparation officielle est <strong>gratuite</strong>.",
    ],
    "toc": [
        ("qui", "Qui doit le passer, et lequel"),
        ("reseaux", "Deux organismes, deux réseaux de centres"),
        ("fei", "S'inscrire dans un centre FEI : test-civique.fr"),
        ("ccip", "S'inscrire dans un centre CCIP : « Trouver une session »"),
        ("paris", "À Paris : les centres et leurs sessions"),
        ("prix", "Combien ça coûte"),
        ("etranger", "Le passer à l'étranger"),
        ("pieges", "Les pièges : préparation payante, mauvaise mention, fraude"),
    ],
    "body": """
<h2 id="qui">Qui doit le passer, et lequel</h2>

<p>Depuis le 1<sup>er</sup> janvier 2026, l'attestation de réussite à l'examen civique est exigée
pour trois démarches : une <strong>première carte de séjour pluriannuelle</strong>, une
<strong>première carte de résident</strong>, et la <strong>naturalisation</strong> par décret.
Le ministère de l'Intérieur le précise : « Tout étranger majeur, signataire du contrat
d'intégration républicaine (CIR), qui souhaite s'installer en France durablement. » Il n'est pas
exigé pour un renouvellement, ni des bénéficiaires d'une protection internationale, ni des
ressortissants relevant de certains accords bilatéraux. Notre guide sur
<a href="/blog/carte-de-resident-b1-2026/">la carte de résident</a> et celui sur
<a href="/blog/naturalisation-2026-niveau-b2/">la naturalisation</a> détaillent qui est concerné
et les cas de dispense.</p>

<p>L'examen existe en <strong>trois mentions</strong>, fixées par l'arrêté du 10 octobre 2025 :
« carte de séjour pluriannuelle », « carte de résident » et « naturalisation ». On choisit la
sienne à l'inscription. Le niveau de difficulté diffère, pas le seuil : dans les trois cas,
<strong>40 questions</strong> — 28 de connaissances, 12 de mise en situation, une seule bonne
réponse sur quatre —, <strong>45 minutes</strong> au plus, sur tablette ou ordinateur, et
<strong>32 bonnes réponses</strong> pour réussir. Une règle utile : « L'attestation de réussite à
l'examen civique mention CR vaut attestation de réussite mention CSP. » L'inverse n'est pas
vrai.</p>

<h2 id="reseaux">Deux organismes, deux réseaux de centres</h2>

<p>« Deux organismes ont été agréés par le ministère de l'Intérieur pour la mise en œuvre de
l'examen civique », indique le site officiel formation-civique.interieur.gouv.fr : la
<strong>Chambre de commerce et d'industrie de Paris Île-de-France</strong> — l'opérateur du TEF —
et <strong>France Éducation international</strong> — l'opérateur du TCF et du DELF. Chacun a son
réseau de centres agréés, souvent les mêmes écoles de langue et Alliances françaises que pour les
tests de français, et sa propre procédure d'inscription. L'attestation vaut la même chose dans les
deux cas.</p>

<p>Au 17 septembre 2026, la liste de FEI comptait <strong>244 centres d'examen civique en
France</strong>, dans 94 départements — sept à Paris, huit dans le Rhône, sept dans les
Bouches-du-Rhône, six en Haute-Garonne, dans l'Hérault et en Moselle. Le réseau CCIP se consulte
session par session, ville par ville, dans son outil de recherche. Un organisme absent de ces
deux listes ne peut pas vous délivrer d'attestation.</p>

%(serie)s

<h2 id="fei">S'inscrire dans un centre FEI : test-civique.fr</h2>

<p>Pour les centres de France Éducation international, le ministère renvoie vers un formulaire
unique de pré-inscription : <strong>test-civique.fr/inscription</strong>. Vous y choisissez le
<strong>département</strong>, la <strong>ville</strong> et le <strong>centre</strong>, puis l'examen
souhaité — carte de résident, carte de séjour pluriannuelle ou naturalisation, chacun avec ou sans
aménagements — et vous renseignez vos coordonnées, votre <strong>numéro étranger (AGDREF)</strong>,
votre date et lieu de naissance. Le formulaire affiche les coordonnées du centre choisi ; c'est lui
qui vous propose ensuite une date et encaisse le paiement. Les candidats en situation de handicap
doivent contacter le centre <em>avant</em> toute inscription pour les aménagements.</p>

<div class="note">
<p><strong>Où trouver les centres FEI.</strong> Sur la
<a href="https://www.france-education-international.fr/centres-d-examen/carte?type-centre=examen_civique" rel="noopener">carte
des centres de passation de l'examen civique</a>, catégorie à part sur le site de FEI, avec
l'adresse, le téléphone et le site de chaque centre. Le formulaire de test-civique.fr reprend la
même liste, département par département.</p>
</div>

<h2 id="ccip">S'inscrire dans un centre CCIP : « Trouver une session »</h2>

<p>Le réseau de la CCI Paris Île-de-France fonctionne par sessions : sur
<strong>francais.cci-paris-idf.fr</strong>, l'outil « Trouver une session » demande une ville et
l'examen — « Examen civique mention carte de résident », « … carte de séjour pluriannuelle » ou
« … naturalisation » — et affiche les centres avec leur nombre de sessions disponibles, une
carte, et deux boutons : « Contacter le centre » et « Choisir ». L'inscription et le paiement se
font ensuite auprès du centre. Le même outil sert au TEF : les centres TEF IRN sont souvent aussi
centres d'examen civique CCIP.</p>

<h2 id="paris">À Paris : les centres et leurs sessions</h2>

<p>Paris est la ville la mieux dotée, et aussi celle où l'on trouve des sessions
<strong>complètes</strong>. Côté FEI, les sept centres agréés sont ceux du TCF : ACTE (10<sup>e</sup>),
ILE International (12<sup>e</sup>), l'Alliance française Paris Île-de-France (6<sup>e</sup>), les
Cours de civilisation française de la Sorbonne (17<sup>e</sup>), ELFE (1<sup>er</sup>), Etoile Institut
(7<sup>e</sup>) et ACCORD (15<sup>e</sup>). Le 17 septembre 2026, l'Alliance française affichait sur sa
page examen civique : « Toutes nos sessions sont complètes pour le moment. » Côté CCIP, la
recherche « mention naturalisation » à Paris renvoyait, pour septembre-décembre 2026 :</p>

<div class="tablewrap wide">
<table>
<caption>Centres CCIP proposant l'examen civique mention « naturalisation » à Paris, outil « Trouver une session » du Français des affaires, sessions de septembre à décembre 2026, consulté le 17 septembre 2026.</caption>
<thead><tr><th>Centre</th><th>Arrondissement</th><th>Sessions affichées</th></tr></thead>
<tbody>
<tr><td>Emploi Services Formation (ESF)</td><td>19<sup>e</sup>, rue d'Hautpoul</td><td><strong>300</strong></td></tr>
<tr><td>ASPLEF</td><td>10<sup>e</sup>, boulevard de Magenta</td><td>44</td></tr>
<tr><td>AVD Formation</td><td>17<sup>e</sup>, rue Catulle-Mendès</td><td>34</td></tr>
<tr><td>Kangourou</td><td>16<sup>e</sup>, rue du Général-Clergerie</td><td>11</td></tr>
<tr><td>ALIP</td><td>15<sup>e</sup>, rue Ginoux</td><td>5</td></tr>
<tr><td>Etoile Institut de langue</td><td>7<sup>e</sup>, boulevard Raspail</td><td>3</td></tr>
<tr><td>CCI Paris République</td><td>10<sup>e</sup>, rue Léon-Jouhaux</td><td>2</td></tr>
<tr><td>Institut Aritas Formation</td><td>17<sup>e</sup>, rue Cardinet</td><td>1</td></tr>
</tbody>
</table>
</div>

<p>Etoile Institut, agréé par les deux organismes, organisait des sessions <strong>presque tous
les jours</strong> en septembre 2026, à 80 € en semaine et 90 € le samedi. Avec des sessions de
40 questions en 45 minutes, un centre peut en enchaîner plusieurs par jour : la rareté que
connaissent le DELF ou le TCF Canada n'a pas lieu d'être ici, sauf dans les centres qui n'ouvrent
que quelques dates par mois.</p>

<h2 id="prix">Combien ça coûte</h2>

<p>Aucun texte ne fixe le prix de l'examen civique — ni l'arrêté du 10 octobre 2025, ni les fiches
de Service-Public, ni le site du ministère. Chaque centre agréé décide. Sur les centres relevés le
17 septembre 2026 :</p>

<div class="tablewrap">
<table>
<caption>Tarifs de l'examen civique affichés par les centres le 17 septembre 2026. Prix libre ; ces tarifs changent sans préavis.</caption>
<thead><tr><th>Centre</th><th>Ville</th><th>Tarif</th><th>Résultats</th></tr></thead>
<tbody>
<tr><td>Espaces Formation</td><td>Nantes</td><td><strong>70 €</strong></td><td>« généralement sous 12 heures »</td></tr>
<tr><td>Alliance française de Montpellier</td><td>Montpellier</td><td><strong>75 €</strong></td><td>non relevé</td></tr>
<tr><td>Etoile Institut de langue</td><td>Paris 7<sup>e</sup></td><td><strong>80 €</strong> (90 € le samedi)</td><td>non relevé</td></tr>
<tr><td>ACCORD</td><td>Paris 15<sup>e</sup></td><td><strong>110 €</strong></td><td>« attestation définitive sous 12 heures »</td></tr>
<tr><td>Alliance française Paris Île-de-France</td><td>Paris 6<sup>e</sup></td><td>non relevé</td><td>« toutes nos sessions sont complètes »</td></tr>
</tbody>
</table>
</div>

<p>Du simple au presque double pour un examen strictement identique, et des résultats souvent
le jour même : l'attestation est délivrée par l'organisme agréé, sans durée de validité — « elle
n'a pas de durée de validité », écrit le ministère —, et « il est possible de passer l'examen
civique à tout moment et autant de fois que nécessaire ». Chaque tentative se paie.</p>

<h2 id="etranger">Le passer à l'étranger</h2>

<p>L'examen civique se passe aussi hors de France, dans les Instituts français, les Alliances
françaises et auprès des autorités consulaires — utile pour une demande de naturalisation ou de
titre préparée depuis l'étranger. L'Institut français d'Algérie, par exemple, l'organise à
Alger (30, rue des Frères-Kadri, Hydra) : pré-inscription sur test-civique.fr via son lien dédié,
<strong>9 000 DA</strong> payables par carte bancaire ou Dahabia sur place ou par virement,
confirmation sous 48 heures, convocation par e-mail, carte d'identité biométrique ou passeport
le jour J. La carte des centres de FEI a un filtre par pays pour l'examen civique.</p>

<h2 id="pieges">Les pièges : préparation payante, mauvaise mention, fraude</h2>

<div class="warn"><strong>La préparation est gratuite.</strong> Le ministère l'écrit en gras :
« La préparation à l'examen civique peut se faire de manière totalement gratuite. Il n'est pas
nécessaire de payer pour accéder à des questions ou à des tests d'entraînement. » Le site
formation-civique.interieur.gouv.fr publie le programme, les fiches par thème et la
<strong>liste officielle des questions de connaissance</strong> pour les mentions carte de séjour
pluriannuelle et carte de résident ; celle de la mention naturalisation est sur le site du
ministère. Seules les 12 questions de mise en situation ne sont pas publiées.</div>

<ul>
<li><strong>La mauvaise mention.</strong> Une attestation « carte de séjour pluriannuelle » ne
vaut pas pour la carte de résident ni pour la naturalisation ; l'inverse fonctionne pour la carte
de résident vers la pluriannuelle. En cas de doute, passez la mention la plus haute dont vous
aurez besoin.</li>
<li><strong>Le test de français, en plus.</strong> L'examen civique ne remplace pas le niveau de
langue : A2 pour la carte pluriannuelle, B1 pour la carte de résident, B2 pour la naturalisation,
à prouver par un <a href="/blog/ou-passer-le-tcf-irn-en-france/">TCF IRN</a>, un TEF IRN ou un
<a href="/blog/ou-passer-le-delf-en-france/">diplôme DELF</a>. Deux inscriptions, deux dates.</li>
<li><strong>L'attestation de complaisance.</strong> Les centres contrôlent l'identité ; l'arrêté du
10 octobre 2025 prévoit qu'en cas de fraude ou de tentative de fraude, le candidat ne peut plus se
présenter pendant deux ans, et l'examen est annulé en cas de fausse identité ou de substitution
de personne. Un site qui promet une attestation « sans passer l'examen » vend un faux.</li>
<li><strong>Le mauvais réseau.</strong> Un centre TCF n'est pas automatiquement un centre d'examen
civique, et réciproquement : vérifiez la catégorie « examen civique » sur la carte de FEI ou la
présence du centre dans l'outil de la CCIP.</li>
</ul>
""" % {"serie": serie("/blog/ou-passer-l-examen-civique/")},
    "cta_h2": "Le civique se prépare gratuitement ; le B2, lui, se travaille",
    "cta_p": """L'examen civique a ses questions publiées ; le test de français qui l'accompagne, non. Les
examens blancs de l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent le TCF IRN, le
TEF IRN et le DELF au format officiel, avec la correction IA de l'écrit et de l'oral — pour arriver
au B2 exigé depuis 2026 avant de payer la session.""",
    "faq": [
        ("Où passer l'examen civique&nbsp;?",
         "Dans un centre agréé par l'un des deux organismes habilités par le ministère de l'Intérieur : France Éducation international — 244 centres en France au 17 septembre 2026, sur sa carte des centres « examen civique », pré-inscription sur test-civique.fr — ou la CCI Paris Île-de-France, dont l'outil « Trouver une session » liste les centres et leurs dates. L'examen se passe sur place, sur ordinateur ou tablette."),
        ("Comment s'inscrire à l'examen civique&nbsp;?",
         "Pour un centre FEI, par le formulaire de pré-inscription test-civique.fr : département, ville, centre, mention (carte de séjour pluriannuelle, carte de résident ou naturalisation), coordonnées et numéro étranger AGDREF ; le centre vous propose ensuite une date et encaisse le paiement. Pour un centre CCIP, par l'outil « Trouver une session » de francais.cci-paris-idf.fr, puis auprès du centre."),
        ("Combien coûte l'examen civique&nbsp;?",
         "Aucun texte ne fixe de tarif : chaque centre décide. Relevés le 17 septembre 2026 : 70 € à Espaces Formation (Nantes), 75 € à l'Alliance française de Montpellier, 80 € en semaine et 90 € le samedi chez Etoile Institut (Paris), 110 € chez ACCORD (Paris). La préparation, elle, est gratuite sur le site du ministère."),
        ("Quelle mention choisir&nbsp;?",
         "Celle de votre démarche : « carte de séjour pluriannuelle », « carte de résident » ou « naturalisation ». La mention carte de résident vaut aussi pour la carte pluriannuelle, mais pas l'inverse, et aucune des deux ne vaut pour la naturalisation. Le format est le même — 40 questions, 45 minutes, 32 bonnes réponses —, seule la difficulté change."),
        ("Combien de temps pour recevoir l'attestation, et combien de temps est-elle valable&nbsp;?",
         "Plusieurs centres annoncent l'attestation « sous 12 heures » (ACCORD à Paris, Espaces Formation à Nantes). Elle n'a pas de durée de validité, et l'examen peut être repassé « à tout moment et autant de fois que nécessaire » — chaque passage étant payant."),
        ("Peut-on passer l'examen civique à l'étranger&nbsp;?",
         "Oui, dans les Instituts français, les Alliances françaises et auprès des autorités consulaires. L'Institut français d'Algérie l'organise à Alger pour 9 000 dinars, avec une pré-inscription sur test-civique.fr et un paiement sur place ou par virement. La carte des centres de FEI se filtre par pays."),
        ("Faut-il aussi passer un test de français&nbsp;?",
         "Oui, l'examen civique s'ajoute au niveau de langue exigé : A2 pour une première carte pluriannuelle, B1 pour une première carte de résident, B2 pour la naturalisation. Le niveau se prouve par un TCF IRN, un TEF IRN ou un diplôme DELF-DALF — dans un centre qui n'est pas forcément le même."),
    ],
    "also": [
        ("/blog/naturalisation-2026-niveau-b2/", "Naturalisation 2026 : le niveau B2 est devenu obligatoire", "Ce qui change depuis janvier 2026, les justificatifs, l'examen civique, le régime transitoire."),
        ("/blog/carte-de-resident-b1-2026/", "Carte de résident : le B1 exigé depuis janvier 2026", "Qui est concerné, les dispenses, l'examen civique et le coût réel de la démarche."),
        ("/blog/ou-passer-le-tcf-irn-en-france/", "Où passer le TCF IRN en France&nbsp;?", "Sept centres à Paris, des sessions chaque semaine, 140 à 220 € selon le centre."),
        ("/tcf-irn/", "TCF IRN : le test de français pour votre naturalisation", "Niveaux exigés depuis 2026, format des quatre épreuves, échelle sur 499."),
    ],
    "sources": """<strong>Sources.</strong> Ministère de l'Intérieur, formation-civique.interieur.gouv.fr,
page « Informations générales sur l'examen civique » (organismes agréés, liens d'inscription,
format, seuil, validité, gratuité de la préparation), consultée le 17 septembre 2026 ; arrêté du
10 octobre 2025 relatif au programme, aux épreuves et aux modalités d'organisation de l'examen
civique (Légifrance) ; fiches Service-Public F39426 et F39530 ; liste et carte des centres
d'examen civique de France Éducation international (filtre « France ») et formulaire de
pré-inscription test-civique.fr, consultés le 17 septembre 2026 ; outil « Trouver une session »
du Français des affaires (CCI Paris Île-de-France), recherche « Paris, examen civique mention
naturalisation », consulté le 17 septembre 2026 ; pages examen civique d'ACCORD (grille tarifaire
2026), d'Etoile Institut, de l'Alliance française de Montpellier, d'Espaces Formation, de
l'Alliance française Paris Île-de-France et de l'Institut français d'Algérie, consultées le
17 septembre 2026. Les tarifs et sessions changent sans préavis.""",
}


ARTICLES = [DELF, IRN, CAN_FR, CAN_CA, HUB, DZ, MA, TN, CIV]

# Pages par ville (make_villes.py) reliées depuis chaque guide : (pays, examen) → chips en fin de corps.
VILLES_DE = {"ou-passer-le-delf-en-france": [("fr", "delf")], "ou-passer-le-tcf-irn-en-france": [("fr", "tcf")],
             "ou-passer-le-tcf-canada-en-france": [("fr", "tcf")], "ou-passer-le-tcf-canada-au-canada": [("ca", "tcf")],
             "tcf-canada-algerie": [("dz", "tcf")], "tcf-canada-maroc": [("ma", "tcf")], "tcf-canada-tunisie": [("tn", "tcf")],
             "ou-passer-l-examen-civique": [("fr", "tcf")],
             "ou-passer": [("fr", "tcf"), ("fr", "delf"), ("ca", "tcf"), ("dz", "tcf"), ("ma", "tcf"), ("tn", "tcf")]}
VILLES_LABEL = {("fr", "tcf"): "TCF en France", ("fr", "delf"): "DELF en France", ("ca", "tcf"): "TCF au Canada",
                ("dz", "tcf"): "TCF en Algérie", ("ma", "tcf"): "TCF au Maroc", ("tn", "tcf"): "TCF en Tunisie"}

# Carte « Entraînez-vous » insérée avant le 3e h2 de chaque guide (le hub n'en a pas).
CTA_INLINE = ('<aside class="cta-inline"><img src="/img/favicon-192.png" alt="" width="44" height="44" loading="lazy"><div>'
              '<b>Entraînez-vous dans les conditions réelles</b><span>Examens blancs au format officiel et correction IA de l\'écrit '
              'et de l\'oral, dans l\'app TCF DELF TEF — sans compte.</span></div>'
              '<a class="btn" href="https://apps.apple.com/fr/app/tcf-delf-tef-tests-2026/id6790412304">Télécharger</a></aside>\n')


def villes_chips(slug):
    from villes_config import VILLES
    keys = VILLES_DE.get(slug, [])
    blocks = []
    for key in keys:
        items = [(f"/centres/{v['slug']}/", v["crumb"]) for v in VILLES if (v["country"], v["exam"]) == key]
        if not items:
            continue
        head = f'<p class="serie-label">{VILLES_LABEL[key]}</p>\n' if len(keys) > 1 else ""
        blocks.append(head + '<div class="chips">\n' + "\n".join(f'<a class="chip" href="{u}">{t}</a>' for u, t in items) + "\n</div>")
    if not blocks:
        return ""
    return ('\n<h2 id="guides-villes">Les guides par ville</h2>\n<p>Pour les grandes villes, une page réunit les centres agréés avec '
            'leurs contacts, ce que leurs sites affichaient le 17 septembre 2026 — examens proposés, prix, dates — et la '
            'procédure d\'inscription :</p>\n' + "\n".join(blocks) + "\n")


def finalize(a):
    a = dict(a)
    vc = villes_chips(a["slug"])
    if vc:
        a["body"] = a["body"].rstrip() + "\n" + vc
        a["toc"] = list(a.get("toc", [])) + [("guides-villes", "Les guides par ville")]
    if a["slug"] != "ou-passer" and "cta-inline" not in a["body"]:
        parts = re.split(r'(?=<h2 id=")', a["body"])
        if len(parts) > 3:
            parts[3] = CTA_INLINE + parts[3]
            a["body"] = "".join(parts)
    return a


if __name__ == "__main__":
    force = "--force" in sys.argv
    for a in ARTICLES:
        assert len(a["title"]) <= 60, (a["slug"], len(a["title"]))
        assert len(a["desc"]) <= 160, (a["slug"], len(a["desc"]))
    build([finalize(a) for a in ARTICLES], overwrite=force)
