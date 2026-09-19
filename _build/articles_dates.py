#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deux pages « dates » (19/09/2026) : les sessions TCF Canada relevées centre par centre, et le
calendrier national DELF-DALF 2026-2027. Rien d'inventé : relevés du 17/09/2026 (sites des centres)
et calendriers FEI déjà cités dans la série « Où passer ».

Usage : python3 _build/articles_dates.py [--force]
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from article_template import build  # noqa: E402
from articles_ou_passer import stats  # noqa: E402

DATE = "2026-09-19"
DATE_FR = "19 septembre 2026"

TCF_DATES = {
    "slug": "tcf-canada-dates-2026",
    "accent": "accent-tcf",
    "crumb": "Dates TCF Canada 2026",
    "title": "Dates TCF Canada 2026 : les sessions, centre par centre",
    "desc": "Pas de calendrier national : les dates du TCF Canada d'ici décembre 2026 lues sur les sites des centres — Paris, Lyon, Casablanca, Rabat, Tunis, Toronto.",
    "og_title": "Dates TCF Canada 2026 : les sessions, centre par centre",
    "og_desc": "Aucun calendrier national : les dates d'ici décembre 2026 lues sur les sites des centres, en France, au Canada et au Maghreb.",
    "h1": "Dates du TCF Canada en 2026 : les sessions relevées, centre par centre",
    "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": 7,
    "intro": """Il n'existe <strong>aucun calendrier national du TCF Canada</strong> : chaque centre agréé fixe ses
sessions et les publie — ou non — sur son site. Nous avons donc lu, le 17 septembre 2026, les pages
d'inscription des principaux centres de France, du Canada, d'Algérie, du Maroc et de Tunisie. Ce que
nous y avons trouvé : des sessions <strong>trois fois par semaine à Casablanca</strong>, mensuelles à Lyon,
trimestrielles et prises d'assaut à Toronto, « SOLD OUT » à Vancouver. Les dates, ce qu'elles coûtent, et
la règle pour ne pas rater la prochaine.""",
    "facts": [
        "<strong>Pas de calendrier national</strong> : la date est celle du centre, l'inscription aussi — jamais auprès de France Éducation international.",
        "<strong>France</strong> : ACTE Paris 4 nov. et 2 déc. ; ACCORD Paris 23 sept. et 28 oct. ; Alliance française de Lyon 21 oct., 25 nov., 16 déc. ; Montpellier 23 sept. et 13 nov. 2026.",
        "<strong>Maghreb</strong> : Casablanca mardi, jeudi et samedi jusqu'en décembre ; Rabat 9 sessions du 25 sept. au 24 nov. ; Tunis 24-25 sept., 22-23 oct., 26-27 nov., 16 et 18 déc. ; Algérie chaque mois.",
        "<strong>Canada</strong> : Toronto ouvre ses inscriptions un mois avant chaque trimestre (prochaine ouverture le 1<sup>er</sup> décembre 2026 pour janvier-mars 2027) ; Vancouver affichait complet.",
        "Entre deux passations : <strong>20 jours</strong> en France et au Canada, 26 en Algérie, 30 en Tunisie ; résultats sous 2 à 5 semaines selon le pays.",
    ],
    "toc": [
        ("regle", "La règle : la date est celle du centre"),
        ("france", "France : les sessions relevées"),
        ("maghreb", "Maroc, Tunisie, Algérie : les sessions relevées"),
        ("canada", "Canada : des ouvertures plutôt que des dates"),
        ("planifier", "Planifier sa date : délais, résultats, seconde chance"),
    ],
    "body": """
%(stats)s

<h2 id="regle">La règle : la date est celle du centre</h2>
<p>Le TCF Canada est conçu par France Éducation international, mais <strong>FEI n'organise aucune
session</strong> : il agrée des centres, qui choisissent leurs dates, leur support (papier ou
ordinateur), leur tarif et leur délai d'inscription. Deux conséquences. D'abord, la seule source fiable
est la page d'inscription du centre — c'est elle que nous avons lue, le 17 septembre 2026, et c'est
elle qui fait foi le jour où vous payez. Ensuite, deux centres de la même ville peuvent proposer des
dates sans rapport : à Paris, ACCORD avait une session le 23 septembre, ACTE la suivante le
4 novembre.</p>
<p>Ce que les dates ont en commun, en revanche, vient du règlement de FEI : un délai de
<strong>20 jours minimum entre deux passations</strong> (26 en Algérie, 30 en Tunisie, fixés par
l'Institut français local), une attestation <strong>valable deux ans</strong>, et — depuis les sessions
du 1<sup>er</sup> septembre 2026 — <strong>aucune recorrection possible</strong> : la seule façon
d'améliorer un score est de repasser le test, donc de retrouver une date.</p>

<h2 id="france">France : les sessions relevées</h2>
<p>En France, le TCF Canada est <strong>mensuel ou bimensuel</strong> dans les centres qui le proposent —
beaucoup moins fréquent que le TCF IRN, presque hebdomadaire à Paris. Ce que les sites affichaient le
17 septembre 2026 :</p>
<div class="tablewrap wide">
<table>
<caption>Sessions de TCF Canada affichées par les centres français le 17 septembre 2026. Les dates barrées de « complet » sur le site ne sont pas reprises.</caption>
<thead><tr><th>Centre</th><th>Dates relevées</th><th>Prix</th><th>Inscription</th></tr></thead>
<tbody>
<tr><td><strong>ACTE</strong>, Paris 10<sup>e</sup></td><td>4 novembre, 2 décembre 2026 (papier)</td><td>195 €</td><td>En ligne ; résultats « au minimum 3 semaines »</td></tr>
<tr><td><strong>ACCORD</strong>, Paris 15<sup>e</sup></td><td>23 septembre, 28 octobre 2026 (ordinateur)</td><td>220 €</td><td>Close 5 jours avant</td></tr>
<tr><td><strong>Alliance française de Lyon</strong></td><td>21 octobre, 25 novembre, 16 décembre 2026 — 10 et 23 septembre complets</td><td>220 €</td><td>Close 48 h avant ; résultats 2-3 semaines</td></tr>
<tr><td><strong>Alliance française de Montpellier</strong></td><td>23 septembre (limite 13 sept.), 13 novembre 2026 (limite 3 nov.), ordinateur</td><td>200 €</td><td>Dix jours avant ; résultats sous 2 semaines</td></tr>
<tr><td><strong>Alliance française Aix-Marseille</strong></td><td>Dates sur la page du centre ; ordinateur uniquement</td><td>60 € par épreuve</td><td>Deux semaines avant ; résultats en 15 jours</td></tr>
<tr><td><strong>KLF</strong> (Lyon, Montpellier, Bordeaux, Toulouse, Annecy)</td><td>Réservation en ligne par ville</td><td>non relevé</td><td>Résultats 10 jours à 3 semaines</td></tr>
<tr><td><strong>CLPS</strong>, Rennes et Brest</td><td>Fiche d'inscription en ligne</td><td>285 €</td><td>Sur clps.net</td></tr>
</tbody>
</table>
</div>
<p>Les pages par ville détaillent chaque centre, avec ses contacts :
<a href="/centres/tcf-paris/">Paris</a>, <a href="/centres/tcf-lyon/">Lyon</a>,
<a href="/centres/tcf-montpellier/">Montpellier</a>, <a href="/centres/tcf-marseille/">Marseille</a>,
<a href="/centres/tcf-bordeaux/">Bordeaux</a>, <a href="/centres/tcf-toulouse/">Toulouse</a>,
<a href="/centres/tcf-nantes/">Nantes</a>, <a href="/centres/tcf-rennes/">Rennes</a> — et le guide
<a href="/blog/ou-passer-le-tcf-canada-en-france/">Où passer le TCF Canada en France ?</a> compare les
prix.</p>

<h2 id="maghreb">Maroc, Tunisie, Algérie : les sessions relevées</h2>
<p>C'est au Maghreb que le TCF Canada est le plus fréquent — et le mieux affiché. Au <strong>Maroc</strong>,
chaque Institut français publie ses sessions avec un panier en ligne : le 17 septembre, Casablanca en
listait <strong>les mardis, jeudis et samedis</strong>, deux créneaux par jour, du 26 septembre à décembre
2026 (trois déjà complètes) ; Rabat <strong>neuf sessions</strong>, toutes ouvertes, du 25 septembre au
24 novembre ; Marrakech le 20 octobre, Tanger le 15 octobre, Béni Mellal les 24 octobre et 14 novembre —
à <strong>2 900 dirhams</strong> partout.</p>
<p>En <strong>Tunisie</strong>, l'Institut français publie un calendrier par pôle, en deux temps : une fenêtre
de rendez-vous en ligne, puis l'inscription sur place. À Tunis en 2026 : <strong>24-25 septembre</strong>
(rendez-vous du 24 au 30 août), <strong>22-23 octobre</strong> (14-20 septembre), <strong>26-27
novembre</strong> (26-31 octobre) et <strong>16 et 18 décembre</strong> (9-15 novembre), à 880 dinars ;
Sousse, Sfax et El Mourouj ont une session par mois.</p>
<p>En <strong>Algérie</strong>, l'Institut français ne publie pas de dates sur son site : « des sessions TCF
sont ouvertes tous les mois sur les cinq antennes » — Alger, Oran, Constantine, Annaba, Tlemcen —, et le
calendrier réel s'affiche sur la plateforme IFAL (VFS Global) au moment de l'inscription, avec le tarif.
Comptez <strong>26 jours</strong> entre deux inscriptions.</p>
<div class="tablewrap wide">
<table>
<caption>Sessions relevées au Maghreb le 17 septembre 2026, sur les sites des Instituts français.</caption>
<thead><tr><th>Centre</th><th>Dates relevées</th><th>Prix</th><th>Inscription</th></tr></thead>
<tbody>
<tr><td><strong>Casablanca</strong></td><td>Mardis, jeudis, samedis (8 h 30 et 10 h), du 26 sept. à déc. 2026</td><td>2 900 Dhs</td><td>Panier en ligne, if-maroc.org/casablanca</td></tr>
<tr><td><strong>Rabat</strong></td><td>9 sessions du 25 sept. au 24 nov. 2026</td><td>2 900 Dhs</td><td>Panier en ligne</td></tr>
<tr><td><strong>Marrakech · Tanger · Béni Mellal</strong></td><td>20 oct. · 15 oct. · 24 oct. et 14 nov. 2026</td><td>2 900 Dhs</td><td>Panier en ligne</td></tr>
<tr><td><strong>Tunis</strong> (IFT)</td><td>24-25 sept., 22-23 oct., 26-27 nov., 16 et 18 déc. 2026</td><td>880 DT</td><td>Rendez-vous en ligne 3-4 semaines avant, puis sur place</td></tr>
<tr><td><strong>Sousse · Sfax · El Mourouj</strong></td><td>Une session par mois (calendrier par pôle)</td><td>880 DT</td><td>Idem</td></tr>
<tr><td><strong>Alger, Oran, Constantine, Annaba, Tlemcen</strong></td><td>« Tous les mois » ; dates sur la plateforme</td><td>non publié</td><td>IFAL (VFS), 26 jours entre deux inscriptions</td></tr>
</tbody>
</table>
</div>
<p>Par ville : <a href="/centres/tcf-casablanca/">Casablanca</a>, <a href="/centres/tcf-rabat/">Rabat</a>,
<a href="/centres/tcf-marrakech/">Marrakech</a>, <a href="/centres/tcf-tanger/">Tanger</a>,
<a href="/centres/tcf-fes/">Fès</a>, <a href="/centres/tcf-agadir/">Agadir</a>,
<a href="/centres/tcf-tunis/">Tunis</a>, <a href="/centres/tcf-sousse/">Sousse</a>,
<a href="/centres/tcf-sfax/">Sfax</a>, <a href="/centres/tcf-alger/">Alger</a>,
<a href="/centres/tcf-oran/">Oran</a>, <a href="/centres/tcf-constantine/">Constantine</a>.</p>

<h2 id="canada">Canada : des ouvertures plutôt que des dates</h2>
<p>Au Canada, le problème n'est pas de trouver une date mais une <strong>place</strong>. L'Alliance
française de Toronto organise des sessions <strong>trimestrielles</strong> et ouvre les inscriptions
<strong>un mois avant chaque trimestre, à 10 h</strong> : le 17 septembre, le site annonçait les
ouvertures du <strong>1<sup>er</sup> décembre 2026</strong> (sessions de janvier à mars 2027), puis des 2 mars,
20 mai et 17 août 2027. « Si une session n'est pas listée, elle est complète » ; pas de liste d'attente.
À Vancouver, l'Alliance française Canada Pacific affichait <strong>toutes ses sessions « SOLD OUT »</strong>
(390 $) et conseille de se connecter à l'ouverture, passeport en main, sur un seul onglet. À Montréal,
l'Alliance Française inscrit « dans la limite des places disponibles », sans publier de tarif.</p>
<p>Les dates elles-mêmes sont sur les pages de chaque centre : <a href="/centres/tcf-montreal/">Montréal</a>
(sept centres), <a href="/centres/tcf-toronto/">Toronto</a>, <a href="/centres/tcf-quebec-ville/">Québec</a>,
<a href="/centres/tcf-ottawa/">Ottawa</a>, <a href="/centres/tcf-vancouver/">Vancouver</a> — et le guide
<a href="/blog/ou-passer-le-tcf-canada-au-canada/">Où passer le TCF Canada au Canada ?</a> donne la
méthode pour décrocher une place.</p>

<h2 id="planifier">Planifier sa date : délais, résultats, seconde chance</h2>
<p>Trois durées à mettre bout à bout avant de choisir une session. <strong>L'inscription</strong> ferme de
48 heures (Lyon) à deux semaines (Marseille) avant le test en France, un mois avant au Canada ; au Maghreb,
tant qu'il reste des places. <strong>Les résultats</strong> arrivent sous deux semaines à Montpellier,
deux à trois à Lyon et Ottawa, trois à quatre à Vancouver, <strong>cinq semaines</strong> en Tunisie.
<strong>Une seconde passation</strong> exige 20 jours d'écart en France et au Canada, 26 en Algérie, 30
en Tunisie — et, sans recorrection depuis septembre 2026, c'est la seule voie de recours.</p>
<p>Si votre dossier a une échéance — un profil Entrée express à déposer, une invitation à honorer —,
comptez donc <strong>au moins deux mois</strong> entre la première session et un résultat utilisable après
un éventuel second passage, et visez la première date disponible plutôt que la plus commode : à Toronto
comme à Casablanca, les sessions se remplissent dans cet ordre.</p>
""" % {"stats": stats([("0", "calendrier national", "chaque centre fixe ses dates"),
                       ("3/sem.", "à Casablanca", "mardi, jeudi, samedi"),
                       ("1/mois", "à Lyon", "21 oct., 25 nov., 16 déc."),
                       ("20 j", "entre deux passations", "26 en Algérie, 30 en Tunisie")])},
    "cta_h2": "La date, c'est le centre ; le score, c'est vous",
    "cta_p": """Une session se paie en entier et se repasse après vingt jours. Les examens blancs de l'app
«&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent le format officiel du TCF Canada — quatre épreuves,
notation sur 699 et sur 20, conversion NCLC — avec la correction IA de l'écrit et de l'oral.""",
    "faq": [
        ("Quand a lieu le prochain TCF Canada ?", "Cela dépend du centre : le 17 septembre 2026, ACCORD à Paris avait une session le 23 septembre, l'Alliance française de Montpellier le 23 septembre puis le 13 novembre, ACTE à Paris le 4 novembre, l'Alliance française de Lyon le 21 octobre ; Casablanca en proposait trois par semaine et Tunis les 24-25 septembre. Il n'existe pas de calendrier national : la page d'inscription du centre fait foi."),
        ("Y a-t-il un calendrier officiel des dates du TCF Canada ?", "Non. France Éducation international agrée les centres mais n'organise aucune session : chaque centre publie ses propres dates, souvent à un ou deux mois d'horizon, et les met à jour au fil des inscriptions. Les listes de FEI ne donnent que les coordonnées des centres."),
        ("Combien de sessions de TCF Canada par mois ?", "De trois par semaine à Casablanca à une par mois à Lyon ou à Sousse, et une par trimestre à Toronto. En France, le TCF Canada est bien moins fréquent que le TCF IRN, qui se passe presque chaque semaine à Paris."),
        ("Que faire si toutes les sessions sont complètes ?", "Créer son compte à l'avance et se connecter à l'ouverture des inscriptions — à Toronto, un mois avant le trimestre, à 10 h ; à Vancouver, avec son passeport prêt et un seul onglet ouvert. Sans liste d'attente, revenir régulièrement : des places se libèrent. En France, changer de centre — les centres d'une même ville n'ont pas les mêmes dates."),
        ("Combien de temps entre deux passations du TCF Canada ?", "Vingt jours minimum en France et au Canada (règle de FEI appliquée par tous les centres), 26 jours en Algérie et 30 jours en Tunisie, fixés par les Instituts français. Depuis les sessions du 1er septembre 2026, aucune recorrection n'est possible : repasser le test est le seul recours."),
    ],
    "also": [
        ("/blog/ou-passer-le-tcf-canada-en-france/", "Où passer le TCF Canada en France ?", "Les centres qui le proposent, 195 à 285 €, leurs dates."),
        ("/blog/ou-passer-le-tcf-canada-au-canada/", "Où passer le TCF Canada au Canada ?", "Les 47 centres, 390 à 440 $, la méthode pour obtenir une place."),
        ("/blog/tcf-canada-maroc/", "TCF Canada au Maroc : les 16 centres et l'inscription", "L'inscription en ligne, les sessions relevées, les règles de report."),
        ("/centres/", "L'annuaire des centres d'examen", "830 centres, 32 pays, et les guides par ville."),
    ],
    "sources": """<strong>Sources.</strong> Pages TCF Canada des centres cités — ACTE, ACCORD (examensparis.fr), Alliances
françaises de Lyon, Montpellier et Aix-Marseille, KLF, CLPS, Alliance française de Toronto, Alliance
française Canada Pacific, Alliance Française de Montréal, Instituts français de Casablanca, Rabat,
Marrakech, Tanger, Tunis (calendrier 2026) et d'Algérie —, consultées le 17 septembre 2026 ; règlement
du TCF (France Éducation international) pour le délai de 20 jours et la validité de deux ans ; note de
FEI sur la fin de la recorrection au 1<sup>er</sup> septembre 2026. Les dates et les prix changent sans
préavis : vérifiez-les sur le site du centre avant de payer.""",
}

DELF_CAL = {
    "slug": "calendrier-delf-dalf-2026-2027",
    "accent": "accent-delf",
    "crumb": "Calendrier DELF 2026-2027",
    "title": "Calendrier DELF-DALF 2026-2027 : les dates des sessions",
    "desc": "Les dix sessions nationales DELF-DALF par an : dates des écrits 2026 et 2027 (jamais en avril ni en septembre), fenêtres d'inscription et prochaines sessions.",
    "og_title": "Calendrier DELF-DALF 2026-2027 : les dates des sessions",
    "og_desc": "Les dix sessions par an, les écrits 2026 et 2027, les fenêtres d'inscription — et pourquoi chaque centre n'en ouvre qu'une partie.",
    "h1": "Calendrier DELF-DALF 2026-2027 : les dates des sessions et des inscriptions",
    "published": DATE, "modified": DATE, "date_fr": DATE_FR, "read": 6,
    "intro": """Le DELF et le DALF tout public se passent à <strong>dix sessions nationales par an</strong>, fixées par
France Éducation international — une par mois, <strong>jamais en avril ni en septembre</strong>. En 2026, il
reste les écrits des <strong>6-8 octobre, 3-5 novembre et 1<sup>er</sup>-3 décembre</strong> ; 2027 commence
les 12-14 janvier. Mais chaque centre n'ouvre qu'une partie de ces sessions et ferme ses inscriptions
<strong>quatre à dix semaines avant l'écrit</strong> — parfois sur deux jours. Le calendrier complet, les
fenêtres d'inscription relevées, et la méthode pour ne pas rater la vôtre.""",
    "facts": [
        "<strong>10 sessions par an</strong>, nationales : janvier, février, mars, mai, juin, juillet, août, octobre, novembre, décembre.",
        "<strong>2026</strong> : 6-8 octobre, 3-5 novembre, 1<sup>er</sup>-3 décembre. <strong>2027</strong> : 12-14 janv., 2-4 févr., 16-18 mars, 25-27 mai, 15-17 juin, 6-8 juil., 3-5 août, 5-7 oct., 16-18 nov., 7-9 déc.",
        "Chaque centre <strong>choisit ses sessions</strong> : Nantes Université en ouvre quatre par an, l'Alliance française de Lyon les dix.",
        "Inscriptions closes <strong>4 à 10 semaines avant</strong> : jusqu'au 4 octobre pour novembre à l'Alliance française de Paris, deux jours seulement (22-23 septembre) pour décembre à Nantes.",
        "Résultats sous <strong>4 à 6 semaines</strong> ; diplôme <strong>valable à vie</strong>.",
    ],
    "toc": [
        ("calendrier", "Le calendrier national 2026-2027"),
        ("centres", "Ce que les centres en font : les sessions relevées"),
        ("inscription", "Les fenêtres d'inscription"),
        ("choisir", "Choisir sa session"),
    ],
    "body": """
%(stats)s

<h2 id="calendrier">Le calendrier national 2026-2027</h2>
<p>France Éducation international publie chaque année le calendrier des sessions DELF-DALF
<strong>tout public</strong> (les versions Prim, junior et scolaire ont leurs propres dates). Les dates
ci-dessous sont celles des <strong>épreuves écrites collectives</strong> ; l'oral individuel se tient
autour de l'écrit, sur convocation du centre — jusqu'à deux semaines après à Lille ou à Bordeaux.</p>
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
<tr><td>Octobre</td><td><strong>6-8 octobre</strong></td><td><strong>5-7 octobre</strong></td></tr>
<tr><td>Novembre</td><td><strong>3-5 novembre</strong></td><td><strong>16-18 novembre</strong></td></tr>
<tr><td>Décembre</td><td><strong>1<sup>er</sup>-3 décembre</strong></td><td><strong>7-9 décembre</strong></td></tr>
</tbody>
</table>
</div>
<p>À l'intérieur d'une session, chaque niveau a son jour : au DEFLE de Bordeaux, en décembre 2026, les A1
et A2 passent le 1<sup>er</sup>, les B1 et B2 le 2, les DALF le 3. Les centres hors de France suivent le
même calendrier, à quelques exceptions locales près.</p>

<h2 id="centres">Ce que les centres en font : les sessions relevées</h2>
<p>Le calendrier national est un <strong>menu</strong>, pas une promesse : chaque centre y choisit les sessions
qu'il ouvre, et les annonce sur son site. Ce que les principaux centres affichaient le 17 septembre
2026 :</p>
<div class="tablewrap wide">
<table>
<caption>Sessions ouvertes par quelques centres agréés, d'après leur site le 17 septembre 2026.</caption>
<thead><tr><th>Centre</th><th>Sessions</th><th>Prochain écrit relevé</th><th>Inscriptions</th></tr></thead>
<tbody>
<tr><td><strong>Alliance française de Lyon</strong></td><td>Les dix sessions de l'année</td><td>2 décembre 2026 (octobre et novembre complets)</td><td>Dès que possible : complet deux mois avant</td></tr>
<tr><td><strong>Alliance française de Paris</strong></td><td>Plusieurs par an</td><td>3-4 novembre 2026, oraux 13-20 novembre</td><td>Jusqu'au 4 octobre</td></tr>
<tr><td><strong>Cours de civilisation française de la Sorbonne</strong></td><td>Juin, juillet, octobre, décembre</td><td>2 décembre 2026</td><td>Du 12 octobre au 8 novembre</td></tr>
<tr><td><strong>Université Sorbonne Nouvelle</strong></td><td>Deux par an (février, mai)</td><td>Février 2027</td><td>Trois semaines, dix semaines avant</td></tr>
<tr><td><strong>Nantes Université</strong></td><td>Quatre par an</td><td>2-4 décembre 2026, puis 17-19 mars, 26-28 mai, 16-18 juin 2027</td><td>Deux jours à partir de 7 h : 22-23 sept., 9-10 févr., 20-21 avril, 11-12 mai</td></tr>
<tr><td><strong>Alliance française de Lille</strong></td><td>Juin et novembre relevés</td><td>3-5 novembre 2026, oraux jusqu'au 18</td><td>Du 30 septembre (10 h) au 7 octobre (23 h 59)</td></tr>
<tr><td><strong>DEFLE Bordeaux Montaigne</strong></td><td>—</td><td>1<sup>er</sup>-3 décembre 2026, oral entre le 1<sup>er</sup> et le 15</td><td>Du 2 octobre au 4 novembre</td></tr>
</tbody>
</table>
</div>
<p>Les pages par ville détaillent chaque centre, avec ses contacts et ses prix :
<a href="/centres/delf-paris/">Paris</a>, <a href="/centres/delf-lyon/">Lyon</a>,
<a href="/centres/delf-lille/">Lille</a>, <a href="/centres/delf-nantes/">Nantes</a>,
<a href="/centres/delf-bordeaux/">Bordeaux</a>, <a href="/centres/delf-marseille/">Marseille</a>,
<a href="/centres/delf-toulouse/">Toulouse</a>, <a href="/centres/delf-montpellier/">Montpellier</a>,
<a href="/centres/delf-strasbourg/">Strasbourg</a>.</p>

<h2 id="inscription">Les fenêtres d'inscription</h2>
<p>C'est la vraie contrainte du calendrier. Un centre DELF commande ses sujets à FEI plusieurs semaines
avant l'écrit : les inscriptions ferment donc <strong>quatre à dix semaines avant</strong>, et certains
centres n'ouvrent qu'une <strong>fenêtre courte</strong> — une semaine à Lille, trois semaines à la Sorbonne
Nouvelle, <strong>deux jours à Nantes</strong>, « dans la limite des places disponibles ». Chez d'autres, la
fenêtre est longue mais la session se remplit : à l'Alliance française de Lyon, octobre et novembre 2026
étaient complets dès le 17 septembre.</p>
<p>Pièces et paiement sont partout les mêmes : une pièce d'identité en cours de validité, votre numéro de
candidat si vous avez déjà passé un DELF, un paiement par carte, des droits <strong>non remboursables</strong>.
Une règle de plus à l'Alliance française Aix-Marseille : « il n'est pas possible de se réinscrire au
DELF/DALF du même niveau tant que les résultats de la session précédente n'ont pas été annoncés ».</p>

<h2 id="choisir">Choisir sa session</h2>
<p>Comptez à rebours depuis la date à laquelle il vous faut le diplôme. <strong>Les résultats</strong> arrivent
sous quatre à six semaines (six à l'Alliance française de Paris et à Lyon), et l'attestation de réussite
provisoire, qui suffit à la plupart des administrations, avec eux ; le diplôme lui-même vient plus tard.
Une session de <strong>décembre 2026</strong> donne donc un résultat en janvier 2027 ; pour un dossier de
naturalisation ou de carte de résident à déposer au printemps, c'est la dernière sans stress.</p>
<p>Si la date est trop proche pour une inscription — ou si les sessions de votre centre sont complètes —,
deux issues : un autre centre agréé de la région, qui n'a pas forcément les mêmes sessions ni les mêmes
prix (<a href="/blog/ou-passer-le-delf-en-france/">de 125 € à 280 € pour un B2</a>), ou un
<a href="/blog/diplome-ou-test-delf-tcf/">test</a> — le TCF IRN se passe presque chaque semaine, mais son
attestation vaut deux ans quand le DELF vaut à vie.</p>
""" % {"stats": stats([("10", "sessions par an", "jamais en avril ni en septembre"),
                       ("3", "sessions d'ici fin 2026", "6-8 oct., 3-5 nov., 1-3 déc."),
                       ("4-10", "semaines avant", "pour s'inscrire"),
                       ("à vie", "validité du diplôme", "résultats sous 4 à 6 semaines")])},
    "cta_h2": "La session est fixée ; le niveau, c'est vous",
    "cta_p": """Un DELF se prépare sur un format précis — quatre épreuves, des consignes qui ne changent pas. Les
examens blancs de l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;» reproduisent le DELF B1, le DELF B2 et
le DALF C1 au format officiel, avec la correction IA de l'écrit et de l'oral.""",
    "faq": [
        ("Quelles sont les prochaines dates du DELF en 2026 ?", "Les écrits des 6-8 octobre, 3-5 novembre et 1er-3 décembre 2026, selon le calendrier national de France Éducation international — chaque centre n'ouvre qu'une partie de ces sessions, et ses inscriptions ferment quatre à dix semaines avant."),
        ("Quelles sont les dates du DELF en 2027 ?", "12-14 janvier, 2-4 février, 16-18 mars, 25-27 mai, 15-17 juin, 6-8 juillet, 3-5 août, 5-7 octobre, 16-18 novembre et 7-9 décembre 2027 (écrits), d'après le calendrier 2027 de FEI consulté le 17 septembre 2026."),
        ("Pourquoi n'y a-t-il pas de DELF en avril ni en septembre ?", "Le calendrier national de FEI ne prévoit pas de session tout public ces deux mois-là, en 2026 comme en 2027 : dix sessions par an, une par mois le reste de l'année."),
        ("Quand s'inscrire au DELF ?", "Dès l'ouverture des inscriptions de votre centre : quatre à dix semaines avant l'écrit, avec des fenêtres parfois très courtes — deux jours à Nantes Université, une semaine à l'Alliance française de Lille — et des sessions complètes deux mois avant à Lyon."),
        ("Les dates du DELF sont-elles les mêmes à l'étranger ?", "Les centres hors de France suivent le calendrier national de FEI, avec quelques aménagements locaux ; la date exacte et la fenêtre d'inscription sont toujours celles du centre, à vérifier sur son site."),
    ],
    "also": [
        ("/blog/ou-passer-le-delf-en-france/", "Où passer le DELF en France ?", "Les prix relevés, les fenêtres d'inscription, les centres par ville."),
        ("/delf-b2/", "DELF B2 : la page d'accueil", "Ce qu'est le diplôme, pour qui, et les modules du dossier."),
        ("/blog/diplome-ou-test-delf-tcf/", "Diplôme ou test : lequel vous faut-il ?", "DELF à vie, TCF deux ans — et des dates très différentes."),
        ("/centres/delf-france/", "Les 143 centres DELF-DALF en France", "Région par région, avec contacts."),
    ],
    "sources": """<strong>Sources.</strong> Calendriers des sessions DELF-DALF tout public 2026 et 2027 de France Éducation
international, consultés le 17 septembre 2026 ; pages DELF-DALF des centres cités — Alliance française de
Paris, Alliance française de Lyon, Cours de civilisation française de la Sorbonne, Université Sorbonne
Nouvelle, Nantes Université (page du 14 septembre 2026), Alliance française de Lille Métropole, DEFLE de
l'université Bordeaux Montaigne, Alliance française Aix-Marseille Provence —, consultées le 17 septembre
2026. Les dates et fenêtres d'inscription changent : le site du centre fait foi.""",
}

ARTICLES = [TCF_DATES, DELF_CAL]

if __name__ == "__main__":
    force = "--force" in sys.argv
    for a in ARTICLES:
        assert len(a["title"]) <= 60, (a["slug"], len(a["title"]))
        assert len(a["desc"]) <= 158, (a["slug"], len(a["desc"]))
    build(ARTICLES, overwrite=force)
