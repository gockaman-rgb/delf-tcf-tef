# -*- coding: utf-8 -*-
"""Pages pays (make_pays.py) — liste FEI et relevés des sites des centres du 08/10/2026.

Une entrée par page : le texte rédigé (titre, intro, faits, sections, FAQ) et, par centre, les
badges et notes tirés du relevé. Les {n}, {so}, {ncity}, {paper} sont calculés sur la liste FEI.
Clés des centres : python3 _build/make_pays.py --keys <fichier>.

Règle de rédaction : un prix, une date, une règle n'entrent ici que lus sur le site du centre ou de
l'organisme de gestion le 8 octobre 2026 ; sinon « non publié » / « non relevé ». Jamais d'adresse
e-mail prénom.nom.
"""

NR = "non relevé"
OK_CA = [("ok", "TCF Canada")]
NO_CA = [("no", "pas de TCF Canada")]


def table(caption, head, rows, wide=True):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = "\n".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return (f'<div class="tablewrap{" wide" if wide else ""}">\n<table>\n<caption>{caption}</caption>\n'
            f"<thead><tr>{th}</tr></thead>\n<tbody>\n{body}\n</tbody>\n</table>\n</div>")


def releve(rows, caption="Ce que le site de chaque centre affichait le 8 octobre 2026. « Non relevé » : non publié, ou non vérifié — le site du centre fait foi."):
    return table(caption, ["Centre", "Déclinaisons", "Prix", "Sessions et inscription"],
                 [(f"<strong>{a}</strong>", b, c, d) for a, b, c, d in rows])


# Liens communs
A_TCF = ("/tcf-canada/", "TCF Canada : la page d'accueil", "Les quatre épreuves, la notation sur 699 et la conversion NCLC.")
A_NCLC = ("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement", "458 en compréhension orale, 453 à l'écrit.")
A_TEF = ("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?", "Les deux tests acceptés par IRCC, côte à côte.")
A_DELF = ("/delf-b2/", "DELF B2 : la page d'accueil", "Le format, le barème (50 sur 100) et la préparation.")
A_DIPL = ("/blog/diplome-ou-test-delf-tcf/", "Diplôme ou test : lequel vous faut-il ?", "Un diplôme s'obtient à vie ; un test vous situe pour deux ans.")

PAGES = []

# ===========================================================================
# CHILI
# ===========================================================================
PAGES.append(dict(
    slug="tcf-chili", exam="tcf", file="tcf_chili", layout="cities", chip="Chili",
    crumb="TCF au Chili",
    pointer="Institut français de Santiago et Alliance française de Concepción : TCF Canada à 299 000 pesos, prochaines dates en novembre 2026.",
    title="TCF Canada au Chili : les 2 centres, prix et dates",
    desc="TCF Canada au Chili : Institut français de Santiago et Alliance française de Concepción, 299 000 pesos, les dates de novembre 2026 et l'inscription.",
    h1="TCF Canada au Chili : les 2 centres agréés, le prix et les dates",
    intro="""Au Chili, le TCF — Canada, Québec, IRN ou tout public — se passe dans <strong>deux centres agréés</strong>
par France Éducation international : l'<strong>Institut français du Chili</strong>, à Santiago, et l'<strong>Alliance
française de Concepción</strong>. Le TCF Canada y coûte <strong>299 000 pesos</strong> dans les deux. Le 8 octobre 2026,
il restait deux dates à Santiago, les 19 et 27 novembre, et une à Concepción, le 11 novembre — inscriptions jusqu'au
13 octobre. Les deux centres, ce que leurs sites affichaient, et comment s'inscrire.""",
    facts=["<strong>2 centres agréés</strong> (liste FEI du 8 octobre 2026) : l'Institut français du Chili à Santiago, avec des sessions sur ordinateur, et l'Alliance française de Concepción.",
           "<strong>TCF Canada : 299 000 pesos</strong> dans les deux centres ; aucune remise ne s'applique au TCF.",
           "Santiago : <strong>19 et 27 novembre 2026</strong> (inscriptions jusqu'au 26 octobre et au 9 novembre) ; Concepción : <strong>11 novembre 2026</strong> (jusqu'au 13 octobre).",
           "Inscription <strong>uniquement en ligne</strong> à Santiago, paiement par carte ; sur place ou par e-mail à Concepción.",
           "Aucun remboursement en cas de désistement ; un seul report, demandé au moins 30 jours (Santiago) ou un mois (Concepción) avant.",
           "Attestation en PDF par e-mail, valable deux ans ; plus aucune recorrection pour les tests passés depuis le 1<sup>er</sup> septembre 2026."],
    stats=[("{n}", "centres agréés", "liste FEI du 8 octobre 2026"), ("299 000", "pesos le TCF Canada", "dans les deux centres"),
           ("3", "dates TCF Canada", "d'ici fin novembre 2026"), ("2 ans", "de validité", "attestation PDF par e-mail")],
    sections=[
        ("releve", "Le TCF Canada au Chili, centre par centre", releve([
            ("Institut français du Chili (Santiago)", "<strong>Canada</strong>, Québec, IRN, tout public, DAP",
             "Canada <strong>299 000 CLP</strong> · IRN 245 000 · tout public : obligatoires 172 000, complet 295 000",
             "Canada : <strong>19/11/2026</strong> (inscriptions jusqu'au 26/10) et <strong>27/11/2026</strong> (jusqu'au 09/11), en vente le 8 octobre ; IRN 20/11 et 17/12 ; aucune session Québec en vente. Date hors calendrier : +15 %, demandée au moins 30 jours avant."),
            ("Alliance française de Concepción", "<strong>Canada</strong>, Québec, IRN, tout public, DAP",
             "Canada <strong>299 000 CLP</strong> · IRN 245 000 · Québec 85 000 par épreuve",
             "Sept sessions en 2026, le TCF Canada le premier des deux jours : prochaine le <strong>11/11/2026</strong> (inscriptions du 21/09 au 13/10). Calendrier 2027 non publié."),
        ]) + """
<p>Les deux centres appliquent la même grille 2026. La FAQ de l'Institut affiche encore une grille plus ancienne
(TCF IRN 236 000 pesos, Québec 82 000 par épreuve) : c'est la plateforme d'inscription, où se paie l'examen, qui fait foi.</p>"""),
        ("inscription", "S'inscrire au TCF Canada au Chili", """<p>À Santiago, l'Institut français du Chili prend les inscriptions <strong>exclusivement en ligne</strong> :
on crée sa fiche sur sa plateforme (icf.extranet-aec.com), on ajoute la date au panier, on paie par carte de débit ou
de crédit ; la convocation arrive par e-mail au plus tard une semaine avant. À Concepción, l'Alliance française
inscrit sur place (Colo Colo 1) ou par e-mail, et ferme ses inscriptions trois à cinq semaines avant l'épreuve.</p>

<p>Le jour J : carte d'identité (<em>cédula</em>) ou passeport en cours de validité, et la convocation — pour le
TCF Canada, prenez la pièce de votre dossier IRCC. Aucun des deux centres ne rembourse un désistement ; un seul
report est possible, demandé au moins 30 jours avant à Santiago, un mois avant à Concepción. L'attestation, valable
deux ans, arrive en PDF par e-mail : il n'y a plus de version papier. Le délai annoncé par l'Institut varie selon la
page — 10 à 15 jours ouvrés sur la page TCF Canada, 3 à 5 semaines dans les conditions générales — : comptez un mois
si votre dossier a une échéance. Depuis les tests du 1<sup>er</sup> septembre 2026, plus de recorrection : l'Institut
l'annonce suspendue jusqu'à la fin de 2027.</p>"""),
    ],
    list_title="Les {n} centres TCF agréés au Chili",
    faq=[("Où passer le TCF Canada au Chili ?", "À l'Institut français du Chili, à Santiago (Providencia), ou à l'Alliance française de Concepción : ce sont les deux seuls centres TCF agréés par France Éducation international dans le pays au 8 octobre 2026, et les deux proposent le TCF Canada."),
         ("Combien coûte le TCF Canada au Chili ?", "299 000 pesos chiliens dans les deux centres (grille 2026 relevée le 8 octobre 2026). Aucune remise ne s'applique au TCF ; à l'Institut français, une date hors calendrier coûte 15 % de plus."),
         ("Quelles sont les prochaines dates ?", "À Santiago, le 19 novembre 2026 (inscriptions jusqu'au 26 octobre) et le 27 novembre 2026 (jusqu'au 9 novembre) ; à Concepción, le 11 novembre 2026, inscriptions jusqu'au 13 octobre. Aucun calendrier 2027 n'était publié le 8 octobre 2026."),
         ("Combien de temps pour les résultats ?", "L'attestation arrive en PDF par e-mail. L'Institut français annonce 10 à 15 jours ouvrés sur sa page TCF Canada, mais 3 à 5 semaines dans ses conditions générales : comptez un mois si votre dossier IRCC a une échéance."),
         ("Le TCF Canada passé au Chili est-il accepté par IRCC ?", "Oui : l'attestation est délivrée par France Éducation international quel que soit le centre agréé, et vaut deux ans. Choisissez bien le TCF Canada, pas le tout public, qui n'est pas accepté pour Entrée express.")],
    also=[("/centres/delf-chili/", "DELF et DALF au Chili", "Le calendrier national 2026 et les prix de l'Institut français."),
          ("/centres/tcf-perou/", "TCF Canada au Pérou", "Un seul centre, l'Alliance française de Lima."), A_TCF, A_NCLC],
    sources="sites de l'Institut français du Chili (pages TCF, conditions générales, FAQ, calendrier TCF 2026, plateforme d'inscription) et de l'Alliance française de Concepción (pages TCF, calendrier et grille 2026, conditions générales), consultés le 8 octobre 2026.",
    badges={"santiago-institut-francais-du-chili": OK_CA, "concepcion-alliance-francaise": OK_CA},
))

PAGES.append(dict(
    slug="delf-chili", exam="delf", file="delf_chili", layout="cities", chip="Chili",
    crumb="DELF au Chili",
    pointer="",
    title="DELF au Chili : centres, calendrier 2026 et prix",
    desc="DELF et DALF au Chili : le calendrier national 2026 de l'Institut français, la session B2 des 4 et 5 décembre, les prix (B2 137 000 pesos) et les centres.",
    h1="DELF et DALF au Chili : les centres d'examen, le calendrier 2026 et les prix",
    intro="""Au Chili, le DELF et le DALF suivent un <strong>calendrier national</strong> fixé par l'Institut français du Chili,
qui gère les certifications : un niveau par semaine, à Santiago, Antofagasta, Concepción, Osorno ou Talca selon les
niveaux. Le 8 octobre 2026, une seule session tout public restait ouverte : le <strong>DELF B2 des 4 et 5 décembre</strong>,
inscriptions jusqu'au <strong>30 octobre</strong>, à <strong>137 000 pesos</strong>. Le calendrier, les prix et la marche
à suivre, puis les {n} centres d'examen de la liste officielle.""",
    facts=["<strong>{n} centres d'examen</strong> sur la liste FEI du 8 octobre 2026 — Santiago, Concepción, Osorno, Antofagasta —, coordonnés par l'Institut français du Chili.",
           "Calendrier national : B1-B2 en avril, C1-C2 en mai, A1 à B2 en août, DALF en septembre, B2 en décembre ; résultats environ <strong>trois mois</strong> plus tard.",
           "Seule session tout public encore ouverte le 8 octobre 2026 : <strong>DELF B2 les 4 et 5 décembre</strong>, inscriptions jusqu'au <strong>30 octobre</strong> (Santiago, Antofagasta, Osorno).",
           "Prix à l'Institut : <strong>A1 107 000 · A2 117 000 · B1 127 000 · B2 137 000 · C1 167 000 · C2 187 000 pesos</strong>.",
           "Examen <strong>sur papier</strong>, en présentiel ; diplôme imprimé en France, trois à quatre mois après les résultats.",
           "Selon l'Institut, le DELF est au Chili « une option plus économique que le TCF »."],
    stats=[("{n}", "centres d'examen", "liste FEI du 8 octobre 2026"), ("137 000", "pesos le DELF B2", "grille de l'Institut français"),
           ("4-5 déc.", "DELF B2 tout public", "inscriptions jusqu'au 30 octobre"), ("à vie", "validité du diplôme", "résultats en trois mois environ")],
    sections=[
        ("calendrier", "Le calendrier national 2026", table(
            "Calendrier DELF-DALF tout public 2026 de l'Institut français du Chili, consulté le 8 octobre 2026.",
            ["Niveau", "Épreuves", "Inscriptions", "Résultats", "Villes"],
            [("B1", "17 avril", "15 janv. – 15 mars", "juillet", "Antofagasta, Santiago"),
             ("B2", "24-25 avril", "15 janv. – 15 mars", "juillet", "Antofagasta, Santiago"),
             ("C2 · C1", "15 mai · 22-23 mai", "15 janv. – 15 avril", "août", "Antofagasta, Santiago"),
             ("A1 · A2 · B1", "7 · 14 · 21 août", "15 janv. – 30 juin", "novembre", "Antofagasta, Santiago, Talca, Concepción, Osorno"),
             ("B2", "28-29 août", "15 janv. – 30 juin", "novembre", "Antofagasta, Santiago, Concepción, Osorno"),
             ("C1 · C2", "4-5 sept. · 25-26 sept.", "jusqu'au 30 juillet", "décembre", "Antofagasta, Concepción"),
             ("<strong>B2</strong>", "<strong>4-5 décembre</strong>", "<strong>15 janv. – 30 oct.</strong>", "février 2027", "Antofagasta, Osorno, Santiago")]) + """
<p>La partie collective du tout public a lieu le vendredi, l'oral le vendredi ou le samedi selon le nombre
d'inscrits. Le DELF junior (octobre et novembre 2026) et le DELF Prim (5 au 7 novembre) avaient clos leurs
inscriptions le 14 août et le 11 septembre ; leurs résultats sont attendus en février 2027. Le calendrier 2027
n'était pas publié le 8 octobre 2026.</p>"""),
        ("prix", "Combien coûte le DELF au Chili ?", table(
            "Grilles 2026 de l'Institut français du Chili et de l'Alliance française de Concepción, en pesos chiliens, consultées le 8 octobre 2026.",
            ["Niveau", "Institut français (Santiago)", "AF Concepción, tarif réduit"],
            [("DELF A1", "107 000", "96 300"), ("DELF A2", "117 000", "105 300"), ("DELF B1", "127 000", "114 300"),
             ("<strong>DELF B2</strong>", "<strong>137 000</strong>", "123 300"), ("DALF C1", "167 000", "150 300"), ("DALF C2", "187 000", "168 300")], wide=False) + """
<p>L'Alliance française de Concepción applique le même tarif normal que l'Institut ; le tarif réduit vaut pour ses
élèves, ceux du Lycée Charles de Gaulle et des établissements affiliés. L'Institut accorde des remises par code
(réseau « Le français au Chili », élèves des Alliances et de l'Institut…), à demander par formulaire avant de
s'inscrire ; il ne publie ni leur montant, ni de prix pour le DELF junior et Prim.</p>"""),
        ("inscription", "S'inscrire et recevoir son diplôme", """<p>À Santiago, on s'inscrit en ligne sur la plateforme de l'Institut français du Chili (fiche élève, puis
panier) ; pour Antofagasta, Osorno et Concepción, l'Institut renvoie directement à l'Alliance française de la ville.
La convocation arrive par e-mail au plus tard cinq jours avant l'épreuve ; présentez-la avec votre carte d'identité
ou votre passeport. Les épreuves se passent <strong>sur papier</strong>, en présentiel.</p>

<p>Les résultats sont publiés sur le site de l'Institut <strong>environ trois mois</strong> après l'épreuve — une
attestation provisoire est délivrée sur demande. Le diplôme, imprimé en France, arrive au Chili trois à quatre
mois plus tard ; il se retire avec une pièce d'identité, ou par un tiers muni d'une copie de votre carte et d'une
procuration simple. Pour une demande de nationalité française, précise l'Institut, c'est ce diplôme physique qui
est exigé : anticipez.</p>"""),
    ],
    list_title="Les {n} centres d'examen agréés, ville par ville",
    faq=[("Quand a lieu la prochaine session du DELF au Chili ?", "Pour le tout public, le DELF B2 des 4 et 5 décembre 2026 à Santiago, Antofagasta et Osorno, avec des inscriptions jusqu'au 30 octobre 2026 : c'était la seule session tout public encore ouverte le 8 octobre 2026. Le calendrier 2027 n'était pas publié."),
         ("Combien coûte le DELF B2 au Chili ?", "137 000 pesos chiliens à l'Institut français du Chili (grille 2026) ; même tarif normal à l'Alliance française de Concepción, qui applique 123 300 pesos à ses élèves et à ceux du Lycée Charles de Gaulle. Le DALF coûte 167 000 pesos (C1) et 187 000 pesos (C2)."),
         ("Comment s'inscrire au DELF au Chili ?", "À Santiago, en ligne sur la plateforme de l'Institut français du Chili, avec paiement par carte ; à Antofagasta, Osorno et Concepción, directement auprès de l'Alliance française. La convocation arrive par e-mail au plus tard cinq jours avant l'épreuve."),
         ("Quand arrivent les résultats et le diplôme ?", "Environ trois mois après l'épreuve pour les résultats, publiés sur le site de l'Institut français (attestation provisoire sur demande) ; le diplôme, imprimé en France, arrive au Chili trois à quatre mois plus tard. Pour une demande de nationalité française, c'est ce diplôme physique qu'il faut."),
         ("Le DELF passé au Chili est-il le même qu'en France ?", "Oui : c'est le même diplôme du ministère français de l'Éducation nationale, valable à vie, délivré par France Éducation international quel que soit le pays de passation.")],
    also=[("/centres/tcf-chili/", "TCF Canada au Chili", "Deux centres, 299 000 pesos, les dates de novembre 2026."),
          ("/centres/delf-perou/", "DELF et DALF au Pérou", "Cinq sessions par an dans les six Alliances françaises."), A_DELF, A_DIPL],
    sources="site de l'Institut français du Chili (calendriers DELF-DALF tout public, junior et Prim 2026, pages par niveau, conditions générales, résultats, plateforme d'inscription) et de l'Alliance française de Concepción (calendrier et grille DELF-DALF 2026), consultés le 8 octobre 2026.",
    notes={"antofagasta-alianza-francesa-de-antofagasta": "Pas de site : l'Institut français renvoie à son compte Instagram. Sessions tout public, junior et Prim du calendrier national.",
           "osorno-alliance-francaise-d-osorno": "Site afosorno.cl encore aux calendriers 2025 le 8 octobre 2026 ; B2 du 4-5 décembre au calendrier national."},
))

# ===========================================================================
# PÉROU
# ===========================================================================
PAGES.append(dict(
    slug="tcf-perou", exam="tcf", file="tcf_perou", layout="cities", chip="Pérou",
    crumb="TCF au Pérou",
    pointer="Un seul centre, l'Alliance française de Lima : TCF Canada à 1 240 soles, neuf dates en 2026, la dernière complète le 8 octobre.",
    title="TCF Canada au Pérou : un seul centre, à Lima",
    desc="Le TCF Canada au Pérou se passe à l'Alliance française de Lima, seul centre agréé : 1 240 soles, neuf dates en 2026, la dernière déjà complète.",
    h1="TCF Canada au Pérou : un seul centre, l'Alliance française de Lima",
    intro="""Au Pérou, le TCF ne se passe qu'à un endroit : l'<strong>Alliance française de Lima</strong>, à Miraflores, seul
centre TCF agréé par France Éducation international au 8 octobre 2026. Elle propose le TCF Canada, le TCF Québec,
l'IRN, le DAP et le tout public. Le TCF Canada y coûte <strong>1 240 soles</strong> (992 au tarif membre), avec neuf
dates en 2026 — mais la dernière, le <strong>11 décembre</strong>, affichait déjà <strong>complet</strong> le 8 octobre.
Le relevé, les dates, et que faire quand il n'y a plus de place.""",
    facts=["<strong>1 seul centre TCF</strong> au Pérou : l'Alliance française de Lima, avenue Arequipa 4595, Miraflores. Les autres Alliances du pays font passer le DELF, et certaines le TEF, pas le TCF.",
           "<strong>TCF Canada : 1 240 soles</strong> (992 au tarif membre) ; TCF Québec 1 240 soles les quatre épreuves ; TCF tout public complet 1 600 soles.",
           "<strong>Neuf dates TCF Canada en 2026</strong>, à peu près une par mois sauf en juillet, août et novembre ; inscriptions closes deux à trois semaines avant.",
           "⚠️ Le <strong>11 décembre 2026</strong>, dernière date de l'année, était <strong>complet</strong> le 8 octobre ; aucune date 2027 n'était publiée.",
           "Inscription et paiement <strong>en ligne</strong>, sur la plateforme de l'Alliance ; 16 ans minimum.",
           "Résultats en <strong>3 à 4 semaines</strong> ; <strong>30 jours</strong> à attendre entre deux sessions."],
    stats=[("1", "centre TCF", "Alliance française de Lima"), ("1 240", "soles le TCF Canada", "992 au tarif membre"),
           ("9", "dates TCF Canada", "en 2026"), ("30 jours", "entre deux sessions", "résultats en 3 à 4 semaines")],
    sections=[
        ("releve", "Le TCF à l'Alliance française de Lima : prix et dates 2026", table(
            "Calendrier des inscriptions 2026 et plateforme d'inscription de l'Alliance française de Lima, consultés le 8 octobre 2026 ; date limite d'inscription entre parenthèses. Le calendrier imprimé affiche les prix en dollars (TCF Canada 310 $) ; la plateforme facture en soles exactement quatre fois ces montants.",
            ["Déclinaison", "Prix (public · membre)", "Dates 2026", "Le 8 octobre"],
            [("<strong>TCF Canada</strong>", "<strong>1 240 S/</strong> · 992 S/ ; modules seuls : compréhension orale 320, expression orale 300", "23/01, 13/02, 05/03, 10/04, 22/05, 05/06, 11/09, 07/10, <strong>11/12</strong> (27/11)", "<strong>complet</strong> ; aucune date 2027"),
             ("TCF Québec", "1 240 S/ les quatre épreuves ; 300 à 320 S/ l'épreuve", "20/02, 13/03, 14/05, 10/07, <strong>26/11</strong> (03/11)", "en vente"),
             ("TCF tout public", "complet 1 600 S/ · obligatoires 1 000 S/ · une expression 300 S/", "22/01, 09/04, 03/07, 02/10, <strong>04/12</strong> (21/11)", "en vente"),
             ("TCF DAP", "1 240 S/", "<strong>04/12</strong> (21/11)", "en vente"),
             ("TCF IRN (« TCF ANF »)", "310 $ au calendrier", "15/05, <strong>06/11</strong> (10/10)", "absent de la plateforme")])),
        ("inscription", "S'inscrire, et que faire si c'est complet", """<p>L'inscription se fait <strong>directement en ligne</strong>, sur la plateforme de l'Alliance française de
Lima (aflima.extranet-aec.com) : on choisit l'examen et la date, on paie, et une session pleine s'affiche « Lleno ».
Les tests se passent uniquement en présentiel, dès 16 ans. L'Alliance ne publie ni ses moyens de paiement, ni de
règle d'annulation, de remboursement ou de report : demandez-les avant de payer, au service des examens
(examenes.intafl@alianzafrancesa.org.pe, ou le (511) 610-8000, option 3).</p>

<p>Avec un seul centre et neuf dates par an, la <strong>place</strong> est le vrai goulot. Le 8 octobre 2026, la
session TCF Canada du 11 décembre était complète et le calendrier 2027 n'était pas publié : surveillez la
plateforme à sa parution, comme le font les candidats des autres pays où les sessions partent vite. Le TCF Québec du
26 novembre, encore en vente, ne remplace pas le TCF Canada : IRCC ne l'accepte pas. L'autre test reconnu par IRCC
est le <a href="/tef-canada/">TEF Canada</a>, vendu par la même Alliance — sa session complète du 9 novembre était
encore en vente le 8 octobre — et par des Alliances de province, comme celle d'Arequipa, qui propose « le TEF et le TEFAQ ».</p>

<p>Les résultats arrivent trois à quatre semaines après l'épreuve ; l'attestation vaut deux ans. Il faut attendre
<strong>30 jours</strong> entre deux sessions : avec une date par mois environ, une seconde tentative prend au moins
un mois, souvent deux.</p>"""),
    ],
    list_title="Le centre TCF agréé au Pérou",
    faq=[("Où passer le TCF Canada au Pérou ?", "À l'Alliance française de Lima (avenue Arequipa 4595, Miraflores), seul centre TCF agréé par France Éducation international au Pérou au 8 octobre 2026. Les Alliances d'Arequipa, Cusco, Trujillo, Chiclayo et Piura font passer le DELF, et certaines le TEF, mais pas le TCF."),
         ("Combien coûte le TCF Canada au Pérou ?", "1 240 soles, ou 992 soles au tarif membre de l'Alliance française de Lima (plateforme d'inscription, 8 octobre 2026). Le calendrier imprimé l'affiche à 310 dollars."),
         ("Quand est la prochaine session du TCF Canada à Lima ?", "Le 8 octobre 2026, la dernière date de l'année — le 11 décembre, inscriptions jusqu'au 27 novembre — était complète, et le calendrier 2027 n'était pas publié. En 2026, l'Alliance a proposé neuf dates : janvier, février, mars, avril, deux fois mai-juin, septembre, octobre et décembre."),
         ("Combien de temps faut-il attendre entre deux sessions ?", "Trente jours, selon l'Alliance française de Lima. Avec une session par mois environ, une seconde tentative prend donc au moins un mois, souvent deux."),
         ("TCF Canada ou TEF Canada au Pérou ?", "IRCC accepte les deux. Au Pérou, le TCF Canada n'existe qu'à Lima, alors que le TEF Canada est aussi proposé par des Alliances de province, comme Arequipa. Notre comparatif TCF ou TEF Canada met les deux formats côte à côte.")],
    also=[("/centres/delf-perou/", "DELF et DALF au Pérou", "Cinq sessions par an, la prochaine le 28 novembre 2026."),
          ("/centres/tcf-chili/", "TCF Canada au Chili", "Deux centres, 299 000 pesos."), A_TEF, A_NCLC],
    sources="site et plateforme d'inscription de l'Alliance française de Lima (pages « Exámenes internacionales » et « Certificaciones internacionales », calendrier des inscriptions 2026) et site de l'Alliance française d'Arequipa, consultés le 8 octobre 2026.",
    badges={"lima-alliance-francaise": OK_CA},
))

PAGES.append(dict(
    slug="delf-perou", exam="delf", file="delf_perou", layout="cities", chip="Pérou",
    crumb="DELF au Pérou",
    pointer="",
    title="DELF au Pérou : centres, dates 2026 et prix",
    desc="DELF et DALF au Pérou : 6 Alliances françaises, la session du 28 novembre 2026 (inscriptions jusqu'au 16 octobre), les prix (B2 461 soles), l'inscription.",
    h1="DELF et DALF au Pérou : les 6 centres d'examen, les dates 2026 et les prix",
    intro="""Au Pérou, le DELF et le DALF se passent dans les <strong>six Alliances françaises</strong> du pays — Lima, Arequipa,
Cusco, Trujillo, Chiclayo, Piura —, sous la gestion centrale de l'Alliance française de Lima. Cinq sessions tout
public par an, le samedi : la prochaine a lieu le <strong>28 novembre 2026</strong>, inscriptions jusqu'au <strong>16
octobre</strong>. Le DELF B2 coûte <strong>461 soles</strong> (369 avec une convention Alliance), et les élèves des
Alliances passent l'examen de leur niveau gratuitement.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 8 octobre 2026), tous des Alliances françaises ; gestion centrale à l'Alliance française de Lima.",
           "<strong>Cinq sessions tout public en 2026</strong>, le samedi : 7 mars, 9 mai, 4 juillet, 5 septembre et <strong>28 novembre</strong> (inscriptions du 8 septembre au 16 octobre).",
           "Prix pour un candidat libre : <strong>A1 286 · A2 345 · B1 385 · B2 461 · C1 543 · C2 618 soles</strong> ; 20 % de moins avec une convention Alliance.",
           "Tarif <strong>Campus France</strong> : B2 276 soles, C1 326 soles (Trujillo, Arequipa).",
           "Résultats en quatre à cinq semaines ; diplôme, imprimé en France, quatre à cinq mois après la session.",
           "Les élèves des Alliances peuvent s'inscrire <strong>gratuitement</strong> à l'examen de leur niveau."],
    stats=[("{n}", "Alliances françaises", "liste FEI du 8 octobre 2026"), ("461", "soles le DELF B2", "369 avec une convention AF"),
           ("28 nov.", "prochaine session", "inscriptions jusqu'au 16 oct."), ("à vie", "validité du diplôme", "cinq sessions par an")],
    sections=[
        ("calendrier", "Les sessions 2026", table(
            "Calendriers DELF-DALF, DELF junior et DELF Prim 2026 de l'Alliance française de Lima (gestion centrale), consultés le 8 octobre 2026.",
            ["Examen", "Dates 2026", "Inscriptions pour la dernière session"],
            [("DELF-DALF tout public", "samedis 7 mars, 9 mai, 4 juillet, 5 septembre, <strong>28 novembre</strong>", "<strong>8 septembre – 16 octobre 2026</strong>"),
             ("DELF junior", "vendredis 6 mars, 3 juillet, 4 septembre, <strong>13 et 20 novembre</strong>", "17 août – 18 septembre (close ; 25 septembre à Arequipa)"),
             ("DELF Prim", "vendredis 8 mai et <strong>23 octobre</strong>", "3 août – 11 septembre (close)")], wide=False) + """
<p>L'oral n'a pas forcément lieu le jour de l'écrit : à Arequipa, il se passe la veille (vendredi 27 novembre). Les
Alliances de Cusco et de Trujillo reprennent le même calendrier ; à Trujillo, les inscriptions ferment le 16 octobre
à 13 h. Le calendrier 2027 n'était publié par aucune Alliance le 8 octobre 2026.</p>"""),
        ("prix", "Combien coûte le DELF au Pérou ?", table(
            "Grille 2026 de l'Alliance française de Lima, identique à Arequipa et Trujillo, en soles, consultée le 8 octobre 2026.",
            ["Niveau", "Candidat libre", "Convention Alliance"],
            [("DELF A1", "286", "229"), ("DELF A2", "345", "276"), ("DELF B1", "385", "307"),
             ("<strong>DELF B2</strong>", "<strong>461</strong>", "369"), ("DALF C1", "543", "435"), ("DALF C2", "618", "494")], wide=False) + """
<p>Le DELF junior va de 257 soles (A1) à 420 soles (B2) pour un candidat libre, le DELF Prim de 242 soles (A1.1) à
303 soles (A2), avec des tarifs réduits pour les élèves des Alliances et des collèges partenaires. Les candidats
<strong>Campus France</strong> paient 276 soles le B2 et 326 soles le C1, selon les Alliances de Trujillo et
d'Arequipa.</p>"""),
        ("inscription", "S'inscrire et recevoir son diplôme", """<p>À Lima, on s'inscrit <strong>en ligne</strong>, sur la plateforme de l'Alliance française
(aflima.extranet-aec.com) ; à Arequipa, en ligne ou au bureau (calle Santa Catalina 208) ; à Trujillo, par e-mail
au bureau des examens, avec un nombre de places limité. Les pages examens de Chiclayo et de Piura n'étaient pas à
jour le 8 octobre 2026 — celles de Piura renvoient à la boutique de Lima. La convocation arrive par e-mail une
semaine avant ; l'écrit et l'oral peuvent avoir lieu à des jours et dans des lieux différents.</p>

<p>Les résultats tombent <strong>quatre à cinq semaines</strong> après la session — pour celle de novembre 2026,
Arequipa annonce le 31 janvier 2027 — et une attestation de réussite est délivrée sur demande. Le diplôme, imprimé
en France, arrive quatre à cinq mois après la session (environ trois mois selon Arequipa). Ne le laissez pas
traîner : l'Alliance de Lima facture 100 soles la garde d'un diplôme de plus de trois ans.</p>"""),
    ],
    list_title="Les {n} centres d'examen agréés, ville par ville",
    faq=[("Quand a lieu la prochaine session du DELF au Pérou ?", "Le samedi 28 novembre 2026 pour le DELF et le DALF tout public, dans les Alliances françaises du pays, avec des inscriptions du 8 septembre au 16 octobre 2026. L'oral peut avoir lieu un autre jour — la veille à Arequipa. Le calendrier 2027 n'était pas publié le 8 octobre 2026."),
         ("Combien coûte le DELF B2 au Pérou ?", "461 soles pour un candidat libre, 369 soles avec une convention Alliance française (grille 2026 de Lima, Arequipa et Trujillo). Les candidats Campus France paient 276 soles le B2 et 326 soles le C1."),
         ("Comment s'inscrire au DELF au Pérou ?", "À Lima, en ligne sur la plateforme de l'Alliance française ; à Arequipa, en ligne ou au bureau ; à Trujillo, par e-mail au bureau des examens, avec un nombre de places limité. La convocation arrive par e-mail une semaine avant l'examen."),
         ("Quand arrivent les résultats ?", "Quatre à cinq semaines après la session, selon l'Alliance française de Lima — pour la session de novembre 2026, Arequipa annonce le 31 janvier 2027. Le diplôme, imprimé en France, suit quatre à cinq mois après la session."),
         ("Les élèves de l'Alliance française paient-ils le DELF ?", "Non : l'Alliance française de Lima permet à ses élèves de s'inscrire gratuitement à l'examen DELF-DALF de leur niveau. À Trujillo, il faut avoir suivi tous les cycles du niveau à l'Alliance et s'inscrire dans les six mois.")],
    also=[("/centres/tcf-perou/", "TCF Canada au Pérou", "Un seul centre, l'Alliance française de Lima."),
          ("/centres/delf-equateur/", "DELF et DALF en Équateur", "Les sessions de novembre et décembre 2026, B2 à 200 dollars."), A_DELF, A_DIPL],
    sources="sites des Alliances françaises de Lima (pages examens, calendriers DELF-DALF, junior et Prim 2026, plateforme d'inscription), d'Arequipa, de Cusco, de Trujillo, de Chiclayo et de Piura, consultés le 8 octobre 2026.",
))

# ===========================================================================
# ÉQUATEUR
# ===========================================================================
PAGES.append(dict(
    slug="tcf-equateur", exam="tcf", file="tcf_equateur", layout="cities", chip="Équateur",
    crumb="TCF en Équateur",
    pointer="Cuenca (200 $, sessions sur demande) et Guayaquil (300 $) publient le TCF Canada ; Quito oriente vers le TEF Canada.",
    title="TCF Canada en Équateur : 3 centres, prix et dates",
    desc="TCF Canada en Équateur : l'Alliance française de Cuenca (200 $, sur demande), celle de Guayaquil (300 $), Quito qui oriente vers le TEF, l'inscription.",
    h1="TCF Canada en Équateur : les 3 centres agréés, leurs prix et leurs dates",
    intro="""En Équateur, trois Alliances françaises sont agréées pour le TCF — <strong>Quito, Guayaquil et Cuenca</strong> —,
toutes avec des sessions sur ordinateur selon France Éducation international. Le 8 octobre 2026, seules deux
publiaient le TCF Canada : <strong>Cuenca, à 200 dollars</strong>, avec une session ouverte sur demande quinze jours
à l'avance, et <strong>Guayaquil, à 300 dollars</strong>, sans date affichée. Quito ne proposait que le TCF tout
public et oriente vers le TEF Canada pour l'immigration.""",
    facts=["<strong>3 centres agréés</strong> (liste FEI du 8 octobre 2026) : les Alliances françaises de Quito, Guayaquil et Cuenca.",
           "<strong>Cuenca : TCF Canada 200 $</strong>, sans calendrier — une session s'ouvre sur demande, au moins <strong>15 jours</strong> avant, un mardi, un mercredi ou un jeudi.",
           "<strong>Guayaquil : TCF Canada 300 $</strong> ; aucune date publiée ni en vente le 8 octobre 2026.",
           "<strong>Quito</strong> : TCF tout public seulement (220 $, 300 $ avec l'oral) ; pour le Canada, l'Alliance propose le <strong>TEF Canada</strong> (300 $).",
           "L'Équateur est dollarisé : tous les prix sont en dollars américains.",
           "Aucune des trois Alliances ne publie de règle d'annulation ou de remboursement : demandez-la avant de payer."],
    stats=[("{n}", "centres agréés", "liste FEI du 8 octobre 2026"), ("200 $", "le TCF Canada à Cuenca", "300 $ à Guayaquil"),
           ("15 jours", "de préavis", "sessions sur demande à Cuenca"), ("2 ans", "de validité", "résultats en 15 jours à Cuenca")],
    sections=[
        ("releve", "Le TCF Canada en Équateur, centre par centre", releve([
            ("Alliance française de Cuenca", "<strong>Canada</strong>, Québec, IRN, DAP, tout public",
             "Canada <strong>200 $</strong> · IRN 200 · DAP 250 · Québec 70 par épreuve · tout public : obligatoires 150, +50 par expression",
             "Pas de calendrier : session ouverte sur demande, au moins 15 jours avant, un mardi, un mercredi ou un jeudi ; résultats « après 15 jours »."),
            ("Alliance française de Guayaquil", "<strong>Canada</strong>, tout public, complet",
             "Canada <strong>300 $</strong> · tout public 160 · complet 300 · épreuve optionnelle 80",
             "Aucune date publiée ; aucune session TCF sur la plateforme le 8 octobre 2026, et des boutons d'inscription sans lien : passez par l'Alliance."),
            ("Alliance française de Quito", "tout public seulement ; TEF Canada et TEFAQ pour l'immigration",
             "TCF tout public 220 $ · avec l'expression orale 300 $ (TEF Canada 300 $)",
             "TCF tout public le 24 avril et le 2 octobre 2026, deux sessions passées ; plateforme : « aucun examen en vente »."),
        ])),
        ("inscription", "S'inscrire au TCF Canada en Équateur", """<p>À <strong>Cuenca</strong>, la procédure est la plus claire : on remplit le formulaire d'inscription TCF 2026
(type de TCF, date souhaitée — au moins quinze jours plus tard —, numéro de cédula ou de passeport, motif
« Inmigración a Canadá »), on vérifie que la date est disponible <em>avant</em> de payer, on règle par virement ou
dépôt sur le compte de l'Alliance, puis on envoie le formulaire et le justificatif à coordo.peda@afcuenca.org.ec,
avec info@afcuenca.org.ec en copie. L'Alliance annonce les résultats après quinze jours et une attestation valable
deux ans.</p>

<p>À <strong>Guayaquil</strong>, la page TCF affiche les prix, mais ses boutons « Inscríbete » ne mènent nulle part et
la plateforme ne vendait que du DELF le 8 octobre 2026 : demandez une date à info@afguayaquil.org.ec. À
<strong>Quito</strong>, pas de TCF Canada : l'Alliance oriente vers le <a href="/tef-canada/">TEF Canada</a>, l'autre
test accepté par IRCC.</p>

<p>Partout, inscrivez-vous avec la pièce d'identité de votre dossier IRCC et respectez au moins 20 jours entre
deux passations, la règle de France Éducation international. Méfiez-vous des pages qui proposent d'« acheter » une
attestation TCF, que l'on voit remonter dans les résultats de recherche : une attestation ne s'obtient qu'en passant
le test dans un centre agréé.</p>"""),
    ],
    list_title="Les {n} centres TCF agréés en Équateur",
    faq=[("Où passer le TCF Canada en Équateur ?", "À l'Alliance française de Cuenca, qui ouvre une session sur demande, ou à celle de Guayaquil, qui affiche le TCF Canada à 300 dollars sans date publiée au 8 octobre 2026. L'Alliance française de Quito, troisième centre agréé, ne proposait que le TCF tout public."),
         ("Combien coûte le TCF Canada en Équateur ?", "200 dollars à l'Alliance française de Cuenca (document « INFO DELF | DALF | TCF 2026 »), 300 dollars à celle de Guayaquil (page TCF), relevés le 8 octobre 2026."),
         ("Faut-il attendre une session à Cuenca ?", "Non : il n'y a pas de calendrier, l'Alliance ouvre une session à la demande, au moins quinze jours à l'avance, un mardi, un mercredi ou un jeudi. Vérifiez la disponibilité de la date avant de payer."),
         ("Peut-on passer le TCF Canada à Quito ?", "Pas le 8 octobre 2026 : l'Alliance française de Quito ne publiait que le TCF tout public (220 dollars, deux sessions en 2026). Pour l'immigration au Canada, elle propose le TEF Canada, que IRCC accepte au même titre que le TCF Canada."),
         ("Le TCF Canada passé en Équateur est-il accepté par IRCC ?", "Oui : l'attestation est délivrée par France Éducation international quel que soit le centre agréé, et vaut deux ans. Vérifiez seulement que c'est bien le TCF Canada, et non le tout public, qui figure sur votre convocation.")],
    also=[("/centres/delf-equateur/", "DELF et DALF en Équateur", "Les sessions de novembre et décembre 2026, B2 à 200 dollars."),
          ("/centres/tcf-perou/", "TCF Canada au Pérou", "Un seul centre, l'Alliance française de Lima."), A_TEF, A_TCF],
    sources="sites des Alliances françaises de Cuenca (pages TCF, document « INFO DELF | DALF | TCF 2026 », formulaire d'inscription TCF 2026), de Guayaquil (page TCF, agenda, plateforme d'inscription) et de Quito (page Diplomas, calendrier des épreuves 2026, plateforme d'inscription), consultés le 8 octobre 2026.",
    badges={"cuenca-alliance-francaise": OK_CA + [("part", "sur demande")], "guayaquil-alliance-francaise": OK_CA, "quito-alliance-francaise": NO_CA},
))

PAGES.append(dict(
    slug="delf-equateur", exam="delf", file="delf_equateur", layout="cities", chip="Équateur",
    crumb="DELF en Équateur",
    pointer="",
    title="DELF en Équateur : centres, dates 2026 et prix",
    desc="DELF et DALF en Équateur : les sessions de novembre et décembre 2026 à Quito, Guayaquil et Cuenca, les prix (B2 200 $, moitié prix pour les élèves AF).",
    h1="DELF et DALF en Équateur : les 5 centres d'examen, les dates 2026 et les prix",
    intro="""En Équateur, le DELF et le DALF se passent dans cinq Alliances françaises — Quito, Guayaquil, Cuenca, Loja,
Portoviejo —, sous la gestion centrale de l'Alliance française de Quito. Le 8 octobre 2026, il restait deux sessions
tout public : <strong>du 23 au 27 novembre</strong> (inscriptions jusqu'au 6 novembre à Quito, au 26 octobre à
Guayaquil) et <strong>du 8 au 14 décembre</strong> (jusqu'au 13 novembre). Le DELF B2 coûte <strong>200
dollars</strong> — moitié prix pour les élèves des Alliances.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 8 octobre 2026), tous des Alliances françaises ; gestion centrale à Quito.",
           "Sessions tout public 2026 : mars, juin, <strong>23-27 novembre</strong> et <strong>8-14 décembre</strong> ; Cuenca a ajouté une session en septembre.",
           "Grille commune, en dollars : <strong>A1 96 · A2 120 · B1 160 · B2 200 · C1 et C2 240</strong> ; élèves des Alliances : <strong>50 % de remise</strong>.",
           "DELF junior : du 1<sup>er</sup> au 4 décembre 2026, inscriptions du 19 octobre au 13 novembre.",
           "Inscription en ligne à Guayaquil, par formulaire et virement à Cuenca, en contactant le service des examens à Quito.",
           "Délais des résultats et du diplôme : non publiés par les trois grandes Alliances."],
    stats=[("{n}", "Alliances françaises", "liste FEI du 8 octobre 2026"), ("200 $", "le DELF B2", "100 $ pour les élèves AF"),
           ("23-27 nov.", "prochaine session", "puis du 8 au 14 décembre"), ("à vie", "validité du diplôme", "même diplôme qu'en France")],
    sections=[
        ("calendrier", "Les sessions de fin 2026", table(
            "Calendrier des épreuves 2026 de l'Alliance française de Quito (gestion centrale), complété par Guayaquil et Cuenca, consulté le 8 octobre 2026.",
            ["Session", "Inscriptions", "A1", "A2", "B1", "B2", "C1", "C2"],
            [("<strong>Tout public, novembre</strong>", "5 oct. – 6 nov. (Quito) · 28 sept. – 26 oct. (Guayaquil)", "23/11", "23/11", "24/11", "25/11", "26/11", "27/11"),
             ("<strong>Tout public, décembre</strong>", "5 oct. – 13 nov.", "08/12", "08/12", "09/12", "10/12", "11/12", "14/12"),
             ("Junior, décembre", "19 oct. – 13 nov.", "01/12", "02/12", "03/12", "04/12", "—", "—")]) + """
<p>Plus tôt en 2026, les sessions tout public avaient eu lieu en mars et en juin, avec une session junior et une
session Prim en juin ; Cuenca a ajouté une session tout public du 21 au 25 septembre et une session Prim et junior
en janvier. Le calendrier 2027 n'était publié par aucune Alliance le 8 octobre 2026.</p>"""),
        ("prix", "Combien coûte le DELF en Équateur ?", table(
            "Grille commune des Alliances françaises de Quito, Cuenca et Guayaquil, en dollars américains, consultée le 8 octobre 2026.",
            ["Niveau", "Public", "Élèves des Alliances"],
            [("DELF A1 (Prim A1.1)", "96", "48"), ("DELF A2 (Prim A1)", "120", "60"), ("DELF B1 (Prim A2)", "160", "80"),
             ("<strong>DELF B2</strong>", "<strong>200</strong>", "100"), ("DALF C1", "240", "120"), ("DALF C2", "240", "120")], wide=False) + """
<p>Le DELF junior suit la même grille, niveau par niveau. La grille affichée par l'Alliance de Loja date de 2024 ;
celle de Portoviejo n'est publiée nulle part — l'Alliance n'a pas de site.</p>"""),
        ("inscription", "S'inscrire", """<p>À <strong>Guayaquil</strong>, l'inscription se fait en ligne, sur la plateforme de l'Alliance
(afguayaquil.extranet-aec.com) : on ajoute la session au panier et on paie. À <strong>Cuenca</strong>, on remplit le
formulaire DELF-DALF, on paie par virement ou dépôt sur le compte de l'Alliance, puis on envoie formulaire et
justificatif à la coordination pédagogique (coordo.peda@afcuenca.org.ec). À <strong>Quito</strong>, la plateforme
n'affichait aucun examen en vente le 8 octobre 2026 : contactez le service des examens (page « Diplomas » du site,
02 224 6589, poste 116), qui accompagne l'inscription.</p>

<p>Aucune des trois Alliances ne publie le délai des résultats ni celui de la remise du diplôme : posez la question
à l'inscription si votre dossier — admission à l'université, demande de visa — a une échéance.</p>"""),
    ],
    list_title="Les {n} centres d'examen agréés, ville par ville",
    faq=[("Quand a lieu la prochaine session du DELF en Équateur ?", "Du 23 au 27 novembre 2026 pour le tout public (A1 et A2 le 23, B1 le 24, B2 le 25, C1 le 26, C2 le 27), avec des inscriptions jusqu'au 6 novembre à Quito et au 26 octobre à Guayaquil ; puis du 8 au 14 décembre 2026, inscriptions jusqu'au 13 novembre."),
         ("Combien coûte le DELF B2 en Équateur ?", "200 dollars, selon la grille commune des Alliances françaises de Quito, Guayaquil et Cuenca ; 100 dollars pour leurs élèves, qui ont 50 % de remise. Le DALF C1 ou C2 coûte 240 dollars."),
         ("Comment s'inscrire au DELF en Équateur ?", "À Guayaquil, en ligne sur la plateforme de l'Alliance ; à Cuenca, avec le formulaire DELF-DALF, un virement ou un dépôt bancaire, puis un e-mail à la coordination pédagogique ; à Quito, en contactant le service des examens, la plateforme n'affichant aucun examen en vente le 8 octobre 2026."),
         ("Y a-t-il un DELF junior en Équateur ?", "Oui : du 1er au 4 décembre 2026 (A1 le 1er, A2 le 2, B1 le 3, B2 le 4), avec des inscriptions du 19 octobre au 13 novembre 2026, au même prix que le tout public. Le DELF Prim n'a eu qu'une session en 2026, en juin."),
         ("Le DELF passé en Équateur est-il valable en France ?", "Oui : c'est le même diplôme, délivré par le ministère français de l'Éducation nationale et valable à vie, quel que soit le pays de passation.")],
    also=[("/centres/tcf-equateur/", "TCF Canada en Équateur", "Cuenca et Guayaquil le proposent, de 200 à 300 dollars."),
          ("/centres/delf-perou/", "DELF et DALF au Pérou", "Cinq sessions par an, B2 à 461 soles."), A_DELF, A_DIPL],
    sources="sites des Alliances françaises de Quito (page Diplomas, calendrier des épreuves 2026, plateforme d'inscription), de Guayaquil (page des certificats, annonce des inscriptions DELF-DALF, plateforme d'inscription), de Cuenca (document « INFO DELF | DALF | TCF 2026 ») et de Loja (page certifications), consultés le 8 octobre 2026.",
))

# ===========================================================================
# ROYAUME-UNI
# ===========================================================================
PAGES.append(dict(
    slug="tcf-royaume-uni", exam="tcf", file="tcf_royaume_uni", layout="cities", chip="Royaume-Uni",
    crumb="TCF au Royaume-Uni",
    pointer="Institut français de Londres (£260) et Alliance française de Glasgow (£325) ; à Londres, première place libre le 23 avril 2027.",
    title="TCF Canada à Londres et au Royaume-Uni : prix, dates",
    desc="TCF Canada au Royaume-Uni : l'Institut français de Londres (£260) et l'Alliance française de Glasgow (£325), des sessions complètes jusqu'en avril 2027.",
    h1="TCF Canada à Londres et au Royaume-Uni : les centres, les prix, les dates",
    intro="""Au Royaume-Uni, {n} centres sont agréés pour le TCF par France Éducation international, mais deux seulement le
font passer : l'<strong>Institut français du Royaume-Uni</strong>, à Londres (TCF Canada <strong>£260</strong>), et
l'<strong>Alliance française de Glasgow</strong> (<strong>£325</strong>) — celle de Jersey ne publie aucune session.
Le 8 octobre 2026, les places manquaient : à Londres, les sessions TCF Canada du 20 novembre et du 5 février
étaient complètes, la première date ouverte étant le <strong>23 avril 2027</strong> ; à Glasgow, le 25 novembre
affichait complet. Les deux centres, leurs règles, et les solutions de repli.""",
    facts=["<strong>{n} centres agréés</strong> (liste FEI du 8 octobre 2026), <strong>2 qui organisent le TCF</strong> : l'Institut français de Londres et l'Alliance française de Glasgow ; celle de Jersey n'en publie aucune session.",
           "<strong>TCF Canada : £260 à Londres, £325 à Glasgow</strong> ; TCF IRN £215 et £245.",
           "⚠️ Londres : sessions TCF Canada du 20 novembre 2026 et du 5 février 2027 <strong>complètes</strong> ; première date ouverte le <strong>23 avril 2027</strong> (inscriptions jusqu'au 18 mars). Glasgow : 25 novembre complet, dates 2027 non publiées.",
           "Les deux centres font passer le TCF <strong>sur papier</strong>.",
           "Délai de rétractation de 14 jours ; ensuite ni remboursement ni report, sauf exception (£38 de frais à Londres).",
           "Résultats sur la plateforme de FEI, 15 jours ouvrés après le test à Londres ; attestation numérique, valable deux ans."],
    stats=[("{n}", "centres agréés", "2 organisent le TCF"), ("£260", "le TCF Canada à Londres", "£325 à Glasgow"),
           ("23 avr.", "première place libre", "à Londres, en 2027"), ("2 ans", "de validité", "résultats en 15 jours ouvrés")],
    sections=[
        ("releve", "Le TCF au Royaume-Uni, centre par centre", releve([
            ("Institut français du Royaume-Uni (Londres)", "<strong>Canada</strong>, IRN, tout public, Québec",
             "Canada <strong>£260</strong> · IRN £215 · tout public £145 + £85 par épreuve facultative · Québec £85 par épreuve",
             "Canada un vendredi par mois environ, 35 à 36 places : 20/11/2026 et 05/02/2027 <strong>complets</strong> ; <strong>23/04/2027</strong> ouvert (jusqu'au 18/03), puis mai, juin, juillet, septembre et novembre 2027. IRN : 29/01/2027. Aucune session Québec ouverte. Sur papier."),
            ("Alliance française de Glasgow", "<strong>Canada</strong>, IRN, tout public",
             "Canada <strong>£325</strong> · IRN £245 · tout public £195",
             "Cinq sessions Canada par an (septembre, novembre, mars, mai, juillet) : 25/11/2026 <strong>complet</strong> ; dates 2027 non publiées. Tout public 18/11 et IRN 27/11/2026, inscriptions jusqu'au 15/10. Sur papier."),
            ("Alliance française de Jersey", "aucune session TCF publiée", "—",
             "Le site ne cite le TCF que pour un cours de préparation : à confirmer auprès de l'Alliance."),
        ]) + """
<p>À Londres, la page de l'Institut et son module d'inscription ne concordent pas toujours : les sessions TCF
Canada du 15 janvier et du 22 octobre 2027 figurent sur la page mais pas dans le module, et la page date la session
de février au « Friday 2 February 2027 », un mardi — la session réelle est le vendredi 5 février. C'est le module,
où l'on paie, qui fait foi.</p>"""),
        ("inscription", "S'inscrire, et décrocher une place", """<p>À Londres comme à Glasgow, on réserve et on paie <strong>en ligne</strong>, depuis la page de l'examen.
Le nom doit être saisi exactement comme sur le passeport — une différence peut vous faire refuser l'accès à la
salle. La convocation arrive deux semaines avant ; le jour J, il faut une pièce originale : passeport, carte
nationale d'identité, permis de conduire ou titre de séjour avec photo. Les retardataires ne sont pas admis. À
Glasgow, l'inscription n'est valable qu'avec l'e-mail de confirmation et la facture, et doit être transmise à FEI
au moins 25 jours avant l'examen : rien n'est accepté après la clôture.</p>

<p>Les deux centres accordent un délai de rétractation de <strong>14 jours</strong> ; passé ce délai, ni remboursement
ni report, sauf force majeure justifiée — l'Institut de Londres retient alors £38, et n'accepte un transfert
qu'avant la clôture des inscriptions. Les résultats arrivent sur la plateforme de France Éducation international,
15 jours ouvrés après le test à Londres ; l'attestation est numérique, valable deux ans, et FEI n'accepte plus de
recorrection depuis le 1<sup>er</sup> septembre 2026.</p>

<p>Le vrai sujet, c'est la <strong>place</strong> : le 8 octobre 2026, la première session TCF Canada ouverte à
Londres était celle du 23 avril 2027 — les inscriptions 2027 de l'Institut sont ouvertes depuis le 18 août 2026.
Si votre échéance est plus proche, le <a href="/tef-canada/">TEF Canada</a>, l'autre test accepté par IRCC, se passe
à l'Institut français d'Écosse et dans les Alliances de Manchester, Cambridge et Oxford ; et la France voisine
compte 251 <a href="/centres/tcf-france/">centres TCF</a>.</p>"""),
    ],
    list_title="Les {n} centres TCF agréés au Royaume-Uni",
    faq=[("Où passer le TCF Canada à Londres ?", "À l'Institut français du Royaume-Uni, 14 Cromwell Place (South Kensington), seul centre londonien agréé pour le TCF. Il propose le TCF Canada à £260, environ un vendredi par mois ; le 8 octobre 2026, ses sessions du 20 novembre 2026 et du 5 février 2027 étaient complètes, et la première date ouverte était le 23 avril 2027."),
         ("Combien coûte le TCF Canada au Royaume-Uni ?", "£260 à l'Institut français de Londres (tarif en vigueur depuis le 1er juillet 2026) et £325 à l'Alliance française de Glasgow, relevés le 8 octobre 2026."),
         ("Le TCF se passe-t-il sur ordinateur à Londres ?", "Non : l'Institut français de Londres comme l'Alliance française de Glasgow annoncent un examen sur papier, même si la liste de France Éducation international mentionne une option ordinateur pour Londres."),
         ("Peut-on annuler ou reporter son TCF ?", "Pendant les 14 jours qui suivent l'inscription, oui. Ensuite, les deux centres ne remboursent ni ne reportent, sauf force majeure justifiée ; l'Institut de Londres retient alors £38 et n'accepte un transfert qu'avant la clôture des inscriptions."),
         ("Que faire si toutes les sessions sont complètes ?", "Réserver tôt : à Londres, les sessions 2027 sont ouvertes depuis le 18 août 2026. Sinon, le TEF Canada, également accepté par IRCC, se passe à l'Institut français d'Écosse et dans les Alliances de Manchester, Cambridge et Oxford ; la France compte par ailleurs 251 centres TCF.")],
    also=[("/centres/delf-royaume-uni/", "DELF et DALF au Royaume-Uni", "Les sessions de décembre 2026 à juin 2027, B2 à £160."),
          ("/centres/tcf-france/", "Centres TCF en France", "251 centres agréés, de l'autre côté de la Manche."), A_TEF, A_NCLC],
    sources="sites de l'Institut français du Royaume-Uni (pages TCF Canada, TCF IRN, TCF tout public et TCF Québec, modules d'inscription, conditions générales) et de l'Alliance française de Glasgow (pages TCF, sessions, conditions TCF) ; site et brochure 2026-2027 de l'Alliance française de Jersey, consultés le 8 octobre 2026.",
    badges={"londres-institut-francais-du-royaume-uni": OK_CA, "glasgow-alliance-francaise": OK_CA,
            "saint-helier-jersey-alliance-francaise-de-jersey": [("no", "aucune session TCF publiée")]},
    notes={"londres-institut-francais-du-royaume-uni": "Option ordinateur selon FEI ; l'Institut annonce un examen sur papier."},
    urls={"londres-institut-francais-du-royaume-uni": "https://www.institut-francais.org.uk/certificates/"},
))

PAGES.append(dict(
    slug="delf-royaume-uni", exam="delf", file="delf_royaume_uni", layout="cities", chip="Royaume-Uni",
    crumb="DELF au Royaume-Uni",
    pointer="",
    title="DELF au Royaume-Uni : {n} centres, dates 2026-2027, prix",
    desc="DELF et DALF au Royaume-Uni : Londres, Édimbourg, Manchester, Glasgow… Les sessions de décembre 2026 à juin 2027, les prix (B2 £160, £170 en 2027).",
    h1="DELF et DALF au Royaume-Uni : les {n} centres, les dates 2026-2027 et les prix",
    intro="""Au Royaume-Uni, le DELF et le DALF se passent dans <strong>{n} centres agréés</strong> — les Instituts français de
Londres et d'Écosse, les Alliances françaises de Manchester, Glasgow, Oxford, Cambridge, Milton Keynes, Leeds et
Jersey, les universités d'Exeter et de Cardiff. Aucun calendrier national n'est publié, mais les écrits tombent les
mêmes jours partout : la prochaine session a lieu en <strong>décembre 2026</strong> (inscriptions jusqu'au <strong>29
octobre</strong> à Londres), puis en mars et en juin 2027. Le DELF B2 coûte <strong>£160</strong> en 2026 et £170 en
2027, dans tous les centres relevés.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 8 octobre 2026), sous la coordination du bureau de coopération linguistique et éducative de l'Institut français du Royaume-Uni.",
           "Session de <strong>décembre 2026</strong> : B1 le 2, B2 le 3, A2 le 7, C1 le 9, C2 le 10, A1 le 14 ; inscriptions du 15 au <strong>29 octobre</strong> à Londres (31 octobre à Glasgow, 2 novembre à Manchester).",
           "Même grille partout : <strong>A1 £100 · A2 £105 · B1 £145 · B2 £160 · C1 £205 · C2 £235</strong> en 2026, £5 à £10 de plus en 2027.",
           "⚠️ Décembre 2026 déjà complet par endroits le 8 octobre : B2 à Glasgow, Oxford et Milton Keynes ; A2 et B1 à Oxford.",
           "Le DELF junior figure sur le formulaire UCAS : selon l'Institut, c'est la porte d'entrée vers les universités françaises.",
           "Diplôme trois à quatre mois après les résultats ; à Londres, il se retire sur place, sur rendez-vous."],
    stats=[("{n}", "centres d'examen", "liste FEI du 8 octobre 2026"), ("£160", "le DELF B2", "£170 pour les sessions 2027"),
           ("29 oct.", "clôture à Londres", "pour la session de décembre"), ("4", "sessions par an", "environ, selon les centres")],
    sections=[
        ("calendrier", "Les sessions de décembre 2026 à juin 2027", table(
            "Dates des écrits du DELF-DALF tout public, identiques d'un centre à l'autre, relevées sur les sites de l'Institut français de Londres, de l'Institut français d'Écosse et des Alliances de Glasgow, Manchester, Oxford, Milton Keynes et Jersey le 8 octobre 2026.",
            ["Session", "A1", "A2", "B1", "B2", "C1", "C2", "Inscriptions", "Résultats"],
            [("<strong>Déc. 2026</strong>", "14/12", "07/12", "02/12", "03/12", "09/12", "10/12", "Londres 15-29/10 ; Jersey, Milton Keynes 29/10 ; Glasgow 31/10 ; Manchester 02/11", "02/02/2027 (Londres)"),
             ("Janv. 2027 (Londres)", "—", "—", "18/01", "21/01", "—", "—", "23/11 – 11/12/2026", "26/02/2027"),
             ("Mars 2027", "22/03", "23/03", "10/03", "15/03", "18/03", "11/03", "jusqu'au 04/02/2027", "21/05/2027"),
             ("Juin 2027", "14/06", "15/06", "02/06", "07/06", "10/06", "03/06", "jusqu'au 26/04/2027", "26/08/2027")]) + """
<p>Les oraux ont lieu à des dates propres à chaque centre ; Londres les communique au moins deux semaines avant.
Aucun calendrier national n'est publié en ligne, alors que plusieurs conditions générales y renvoient : ces dates
sont celles que les centres affichent, identiques partout. Chaque centre n'ouvre que certains niveaux — l'Institut
français d'Écosse n'organise pas de session tout public en décembre, Oxford ne propose que l'A2 au B2. DELF junior :
du 24 au 30 novembre 2026 (inscriptions closes le 15 octobre à Londres et Jersey, le 13 à Manchester), puis en mars
et juin 2027 ; DELF Prim : du 4 au 6 mai 2027, inscriptions jusqu'au 5 février.</p>"""),
        ("prix", "Combien coûte le DELF au Royaume-Uni ?", table(
            "Grille relevée dans dix centres le 8 octobre 2026 (Londres, Édimbourg, Glasgow, Manchester, Jersey, Oxford, Milton Keynes, Cambridge, Leeds, Exeter).",
            ["Niveau", "Sessions 2026", "Sessions 2027"],
            [("DELF A1", "£100", "£105"), ("DELF A2", "£105", "£110"), ("DELF B1", "£145", "£155"),
             ("<strong>DELF B2</strong>", "<strong>£160</strong>", "<strong>£170</strong>"), ("DALF C1", "£205", "£215"), ("DALF C2", "£235", "£245"),
             ("DELF Prim A1.1 · A1 · A2", "£65 · £70 · £75", "£70 · £75 · £80")], wide=False) + """
<p>Le DELF junior coûte le même prix que le tout public, de l'A1 au B2. Seule exception relevée : l'A1 d'octobre
2026 à £95 à Milton Keynes. À Londres, le tarif de la session de décembre 2026 n'était pas encore affiché le
8 octobre (la page montre la grille 2027, le module d'inscription ouvre le 15 octobre).</p>"""),
        ("inscription", "S'inscrire, résultats et diplôme", """<p>Pas de plateforme nationale : chaque centre gère ses inscriptions. Réservation en ligne à Londres
(module « Register here »), Glasgow, Oxford, Cambridge et Milton Keynes ; paiement puis formulaire à Manchester ;
formulaire et paiement à l'Institut français d'Écosse, à Jersey et à Leeds (par virement). Le nom doit être celui
du passeport ; la convocation arrive deux semaines avant ; le jour J, pièce originale avec photo. La plupart des
centres accordent 14 jours de rétractation après l'inscription ; ensuite, ni remboursement ni report, sauf
exception.</p>

<p>Les résultats arrivent par e-mail à une date fixée pour chaque session à Londres (le 2 février 2027 pour
décembre), quatre à huit semaines après l'examen à Manchester et à Leeds, trois mois après à Cambridge. Le diplôme
suit trois à quatre mois plus tard ; à Londres, il se retire au 14 Cromwell Place sur rendez-vous, sans envoi
postal, quand Glasgow l'expédie pour £5. Pour la nationalité française, l'Institut de Londres rappelle que le B2 est
désormais exigé ; une page de l'Alliance de Leeds indique encore le B1, ce qui n'est plus vrai depuis le
1<sup>er</sup> janvier 2026.</p>"""),
    ],
    list_title="Les {n} centres d'examen agréés, ville par ville",
    faq=[("Quand a lieu la prochaine session du DELF à Londres ?", "En décembre 2026 : B1 le 2, B2 le 3, A2 le 7, C1 le 9, C2 le 10 et A1 le 14 décembre, avec des inscriptions à l'Institut français du 15 au 29 octobre 2026. Suivent une session B1-B2 en janvier 2027, puis mars et juin 2027."),
         ("Combien coûte le DELF B2 au Royaume-Uni ?", "£160 pour les sessions de 2026 et £170 pour celles de 2027, dans tous les centres relevés le 8 octobre 2026. Le DALF coûte £205 (C1) et £235 (C2) en 2026, £215 et £245 en 2027."),
         ("Reste-t-il des places en décembre 2026 ?", "Le 8 octobre 2026, le B2 de décembre était complet à Glasgow, Oxford et Milton Keynes, et les A2 et B1 à Oxford. Londres ouvrait ses inscriptions le 15 octobre ; Glasgow avait encore de la place en A1, A2 et C1, Milton Keynes en A1 et A2."),
         ("Le DELF compte-t-il pour UCAS ?", "Selon l'Institut français du Royaume-Uni, le DELF junior figure sur le formulaire de candidature UCAS et sert de porte d'entrée vers les universités françaises."),
         ("Quand reçoit-on le diplôme ?", "Les résultats arrivent par e-mail, à une date fixée par session (le 2 février 2027 pour décembre 2026 à Londres) ; le diplôme suit trois à quatre mois plus tard. À Londres, il se retire sur rendez-vous, sans envoi postal ; Glasgow l'envoie pour £5.")],
    also=[("/centres/tcf-royaume-uni/", "TCF Canada au Royaume-Uni", "Londres £260, Glasgow £325, des places rares."),
          ("/centres/delf-espagne/", "DELF et DALF en Espagne", "Le calendrier national 2027 et la grille unique."), A_DELF, A_DIPL],
    sources="sites de l'Institut français du Royaume-Uni (pages DELF-DALF tout public, junior et Prim, modules d'inscription, conditions générales, page « French Diplomas »), de l'Institut français d'Écosse, des Alliances françaises de Glasgow, Manchester, Cambridge, Oxford, Milton Keynes, Jersey et Leeds, et du centre de langues de l'université d'Exeter, consultés le 8 octobre 2026.",
    notes={"leeds-leeds-af": "Le site de l'Alliance (afleeds.org.uk) donne une autre adresse : Brownberrie Lane, LS18 5SB.",
           "exeter-university-of-exeter": "Ouvert aux candidats extérieurs ; calendrier 2026-2027 non publié le 8 octobre 2026.",
           "edimbourg-institut-francais-d-ecosse": "Trois sessions par an (mars, juin, octobre) ; pas de session tout public en décembre 2026.",
           "oxford-alliance-francaise-d-oxford": "A2 à B2 seulement ; A2, B1 et B2 de décembre 2026 complets le 8 octobre."},
    urls={"exeter-university-of-exeter": "https://language-centre.exeter.ac.uk/exams/delf/",
          "cardiff-cardiff-university": "https://www.cardiff.ac.uk/modern-languages/about-us/international-language-qualifications/french-delf-dalf",
          "londres-institut-francais": "https://www.institut-francais.org.uk/certificates/delf-dalf-tout-public/",
          "leeds-leeds-af": "https://afleeds.org.uk/delfdalf"},
))

# ===========================================================================
# ESPAGNE
# ===========================================================================
ES_CA = ["barcelone-institut-francais", "bilbao-institut-francais-d-espagne-delegation-de-bilbao", "carthagene-alliance-francaise-de-cartagena",
         "madrid-alliance-francaise", "madrid-institut-francais", "malaga-alliance-francaise", "oviedo-alliance-francaise",
         "seville-celf-sevilla", "seville-instituto-de-lengua-francesa", "valence-institut-francais", "valladolid-alliance-francaise"]
PAGES.append(dict(
    slug="tcf-espagne", exam="tcf", file="tcf_espagne", layout="cities", chip="Espagne",
    crumb="TCF en Espagne",
    pointer="11 des 14 centres agréés proposent le TCF Canada, de 275 à 287 € ; des sessions chaque semaine à Valladolid et Séville.",
    title="TCF Canada en Espagne : 11 centres, 281 à 287 €, dates",
    desc="TCF Canada en Espagne : 11 des 14 centres agréés le proposent, de 275 à 287 €, à Madrid, Barcelone, Valence, Séville… Prochaines dates et inscription.",
    h1="TCF Canada en Espagne : les centres, les prix et les prochaines dates",
    intro="""En Espagne, {n} centres sont agréés pour le TCF par France Éducation international, et <strong>onze proposent
le TCF Canada</strong> d'après leur site au 8 octobre 2026 : les Instituts français de Madrid, Barcelone, Valence et
Bilbao, les Alliances françaises de Madrid, Málaga, Oviedo, Cartagena et Valladolid, le CELF et l'ILF à Séville.
Trois grilles de prix : <strong>287 €</strong> dans les Instituts et à l'ILF, <strong>281 €</strong> dans les
Alliances, <strong>275 €</strong> au CELF. La fréquence va d'une session par semaine — Valladolid, Séville — à quatre
ou cinq par an.""",
    facts=["<strong>{n} centres agréés</strong> (liste FEI du 8 octobre 2026), dont <strong>11 qui proposent le TCF Canada</strong> ; pas de TCF Canada à l'Alliance de Saint-Jacques-de-Compostelle, et rien de publié pour 2026 à Vigo ni à l'Université publique de Navarre.",
           "Prix 2026 du TCF Canada : <strong>287 €</strong> (Instituts français, ILF Séville), <strong>281 €</strong> (Alliances françaises), <strong>275 €</strong> (CELF Séville) ; TCF IRN 278, 269 et 260 €.",
           "Fréquence : <strong>chaque semaine</strong> à Valladolid, chaque lundi et vendredi à l'ILF Séville, deux fois par mois au CELF, tous les mois à Oviedo ; quatre à dix sessions par an ailleurs.",
           "Prochaines dates TCF Canada : Barcelone 10-13 novembre, Málaga 11-13 novembre, Valence 12-13 novembre, Oviedo 13 novembre, Alliance de Madrid 19 novembre, Cartagena 23 et 25 novembre, Institut de Madrid 17-18 décembre 2026.",
           "<strong>30 jours</strong> entre deux sessions, rappelle le centre national des examens ; photo du candidat prise le jour du TCF Canada.",
           "Certificat en PDF par e-mail, deux à trois semaines après l'examen ; résultat provisoire le jour même sur ordinateur dans plusieurs centres."],
    stats=[("11", "centres TCF Canada", "sur {n} centres agréés"), ("281-287 €", "le TCF Canada", "275 € au CELF Séville"),
           ("30 jours", "entre deux sessions", "règle du centre national"), ("2-3 sem.", "pour le certificat", "PDF par e-mail")],
    sections=[
        ("releve", "Qui fait passer le TCF Canada en Espagne : le relevé", releve([
            ("Institut français de Barcelone", "<strong>Canada</strong>, tout public (option DAP), IRN", "Canada <strong>287 €</strong> · IRN 278 € · tout public 125 € + 75 € par épreuve",
             "<strong>10-13 novembre</strong> (inscriptions du 1er au 19 octobre ; au 11 pour l'écrit sur papier) ; pas de session en décembre. Sur ordinateur, jour imposé."),
            ("Institut français de Bilbao", "<strong>Canada</strong>, tout public, IRN, Québec", "Canada <strong>287 €</strong> · IRN 278 € · tout public 125 €",
             "Vendredi <strong>13 novembre</strong> (inscriptions du 1er au 13 octobre) ; le 8 octobre, la boutique ne vendait que le tout public. Sur papier."),
            ("Alliance française de Cartagena", "<strong>Canada</strong>, tout public, IRN, Québec", "Canada <strong>281 €</strong> · IRN 269 € · tout public 123 € + 73 €",
             "Neuf sessions en 2026 ; prochaine les <strong>23 et 25 novembre</strong> (inscriptions du 3 au 10 novembre) : fiche, virement et copie du DNI par e-mail."),
            ("Alliance française de Madrid", "<strong>Canada</strong>, tout public, IRN", "Canada <strong>281 €</strong> · IRN 269 € · tout public 123 € + 73 €",
             "Jeudi <strong>19 novembre</strong> (inscriptions du 2 au 13 novembre) ; septembre affichait complet. Sur ordinateur."),
            ("Institut français de Madrid", "<strong>Canada</strong>, tout public, IRN, Québec", "Canada <strong>287 €</strong> · IRN 278 € · tout public 125 € + 75 €",
             "Six sessions par an : <strong>17-18 décembre</strong> (inscriptions du 15 au 30 novembre). Résultat provisoire le jour même ; sur ordinateur."),
            ("Alliance française de Málaga", "<strong>Canada</strong>, tout public, IRN", "Canada <strong>281 €</strong> · IRN 269 € · tout public 123 €",
             "<strong>11-13 novembre</strong> (inscriptions du 1er au 31 octobre) et 9-11 décembre (du 2 au 30 novembre). Carte, espèces ou virement. Sur ordinateur."),
            ("Alliance française d'Oviedo", "<strong>Canada</strong>, tout public, IRN, Québec", "Canada <strong>281 €</strong> · IRN 269 € · tout public 123 €",
             "Une session par mois sauf en août : 16 octobre, <strong>13 novembre</strong> (inscriptions du 27 octobre au 7 novembre), 11 décembre. Sur ordinateur."),
            ("Université publique de Navarre (Pampelune)", "aucun TCF sur son site", NR, "Le TCF n'apparaît nulle part sur le site de l'université : à confirmer auprès d'elle."),
            ("Alliance française de Saint-Jacques-de-Compostelle", "tout public, IRN, Québec — <strong>pas de Canada</strong>", "IRN 269 € · tout public 123 €", "Sessions à la demande, par téléphone ou par e-mail."),
            ("CELF Sevilla", "<strong>Canada</strong>, tout public, IRN, Québec", "Canada <strong>275 €</strong> · IRN 260 € · tout public 120 € (240 € complet)",
             "Deux dates par mois sur ordinateur jusqu'en mars 2027 (9 et 23 octobre, 6 et 27 novembre, 11 décembre…), papier le 20 novembre ; inscription en contactant le centre."),
            ("Instituto de Lengua Francesa (Séville)", "<strong>Canada</strong>, tout public, IRN, Québec", "Canada <strong>287 €</strong> · IRN 278 € · tout public 125 €",
             "<strong>Tous les lundis et vendredis</strong> ; clôture le lundi précédant l'examen. Formulaire, virement et e-mail. Sur ordinateur."),
            ("Institut français de Valence", "<strong>Canada</strong>, tout public, IRN, Québec", "Canada <strong>287 €</strong> · IRN 278 € · tout public 125 € + 75 €",
             "Dix sessions en 2026 : <strong>12-13 novembre</strong> (inscriptions du 14 octobre au 4 novembre), 14-15 décembre (du 14 novembre au 3 décembre). Paiement en ligne ; sur ordinateur."),
            ("Alliance française de Valladolid", "<strong>Canada</strong>, tout public, IRN, Québec", "Canada <strong>281 €</strong> · IRN 269 € · Québec 291 €",
             "<strong>Chaque semaine</strong>, hors vacances ; inscription par e-mail, au moins 10 jours avant. Sur ordinateur."),
            ("Alliance française de Vigo", "rien de publié pour 2026", NR, "Page TCF restée au calendrier 2025 : à confirmer auprès de l'Alliance."),
        ]) + """
<p>Aucun centre, sauf le CELF, ne publiait de date 2027 le 8 octobre 2026. Le Centre de langues modernes de
l'université de Grenade fait aussi passer le TCF (205 €, prochaine date le 25 janvier 2027) sans figurer sur la
liste TCF de FEI : demandez-lui quelle déclinaison il organise avant de vous inscrire.</p>"""),
        ("inscription", "S'inscrire au TCF Canada en Espagne", """<p>Deux modes coexistent. Les Instituts français (Madrid, Barcelone, Valence, Bilbao) et l'Alliance de
Málaga vendent l'examen dans une <strong>boutique en ligne</strong>, avec paiement par carte ; les Alliances de
Cartagena, Oviedo et Saint-Jacques, comme l'ILF Séville, demandent une <strong>fiche d'inscription, un virement et une
copie de la pièce d'identité</strong> par e-mail ; Valladolid et le CELF inscrivent sur simple contact. Pour le TCF
Canada, inscrivez-vous avec le passeport de votre dossier IRCC : le centre national des examens impose une photo du
candidat le jour de l'épreuve, et aucune épreuve ne peut être dispensée.</p>

<p>Les règles se ressemblent : pas de remboursement après la clôture des inscriptions ; report sur certificat
médical seulement (à demander dans les 3 jours suivant l'absence à Barcelone) ; frais de gestion de 30 € à Valence et
de 40 € à l'ILF quand une annulation est acceptée. Il faut <strong>30 jours</strong> entre deux sessions du même
test. Le certificat arrive en PDF par e-mail, deux à trois semaines après l'examen le plus souvent, et plusieurs
centres remettent un résultat provisoire dès la fin de l'épreuve sur ordinateur. Depuis le 1<sup>er</sup> septembre
2026, FEI n'accepte plus de recorrection.</p>

<p>Méfiez-vous des sites qui proposent d'« acheter » un certificat TCF « sans examen », avec un « score garanti » :
nous en avons croisé un en relevant ces prix. C'est une fraude ; un certificat ne s'obtient qu'en passant le test
dans un centre agréé.</p>"""),
    ],
    list_title="Les {n} centres TCF agréés, ville par ville",
    faq=[("Où passer le TCF Canada à Madrid ?", "À l'Institut français de Madrid (calle Marqués de la Ensenada, 12 ; 287 €, prochaine session les 17 et 18 décembre 2026, inscriptions du 15 au 30 novembre) ou à l'Alliance française de Madrid (Cuesta de Santo Domingo, 13 ; 281 €, prochaine session le 19 novembre, inscriptions du 2 au 13 novembre). Relevé le 8 octobre 2026."),
         ("Où passer le TCF Canada à Barcelone ?", "À l'Institut français de Barcelone (carrer Moià, 8), seul centre TCF de la ville : 287 €, sur ordinateur, prochaine session du 10 au 13 novembre 2026, inscriptions du 1er au 19 octobre. Pas de session en décembre 2026, et aucune date 2027 publiée le 8 octobre."),
         ("Combien coûte le TCF Canada en Espagne ?", "287 € dans les Instituts français et à l'ILF Séville, 281 € dans les Alliances françaises, 275 € au CELF Séville (tarifs 2026 relevés le 8 octobre 2026)."),
         ("Où passer le TCF Canada le plus vite ?", "À l'Alliance française de Valladolid, qui ouvre une session chaque semaine (inscription au moins 10 jours avant), ou à l'ILF Séville, qui en organise tous les lundis et vendredis. Le CELF Séville propose deux dates par mois sur ordinateur."),
         ("Combien de temps faut-il attendre entre deux passations ?", "Trente jours entre deux sessions du même test, selon le centre national des examens, rappelé par l'Institut français de Madrid, celui de Valence et le CELF Séville.")],
    also=[("/centres/delf-espagne/", "DELF et DALF en Espagne", "Le calendrier national 2027 et une grille de prix unique."),
          ("/centres/tcf-france/", "Centres TCF en France", "251 centres agréés, région par région."), A_TEF, A_NCLC],
    sources="sites des 14 centres de la liste — Instituts français de Barcelone, Bilbao, Madrid et Valence ; Alliances françaises de Cartagena, Madrid, Málaga, Oviedo, Saint-Jacques-de-Compostelle, Valladolid et Vigo ; CELF et ILF Séville ; Université publique de Navarre (pages TCF, calendriers et tarifs 2026, boutiques, conditions générales) — et du Centro Nacional de Exámenes (delf-dalf.es), consultés le 8 octobre 2026.",
    badges=dict({k: OK_CA for k in ES_CA}, **{"saint-jacques-de-compostelle-alliance-francaise": NO_CA,
                                             "vigo-alliance-francaise": [("part", "rien de publié pour 2026")],
                                             "pampelune-pampelune-universite-publique-de-navarre": [("part", "TCF absent de son site")]}),
    notes={"bilbao-institut-francais-d-espagne-delegation-de-bilbao": "Sur papier ; le 8 octobre, la boutique ne vendait que le tout public pour le 13 novembre."},
))

PAGES.append(dict(
    slug="delf-espagne", exam="delf", file="delf_espagne", layout="regions", chip="Espagne",
    crumb="DELF en Espagne",
    pointer="",
    title="DELF en Espagne : {n} centres, calendrier 2027 et prix",
    desc="DELF et DALF en Espagne : un calendrier national (février, juin, septembre, octobre 2027), des prix identiques partout (B2 192 € en 2027) et les 32 centres.",
    h1="DELF et DALF en Espagne : les {n} centres, le calendrier 2027 et les prix",
    intro="""En Espagne, le DELF et le DALF ont un <strong>calendrier et des prix nationaux</strong> : le Centro Nacional
de Exámenes (delf-dalf.es), rattaché à l'ambassade de France, fixe les mêmes dates et les mêmes tarifs dans les {n}
centres d'examen. La session d'octobre 2026 est close ; la prochaine est celle de <strong>février 2027</strong>, avec
des inscriptions du <strong>1<sup>er</sup> décembre 2026 au 9 janvier 2027</strong>. En 2027, le DELF B2 coûte
<strong>192 €</strong>, le B1 162 €, le DALF C1 249 €. Le calendrier, la grille, l'inscription, puis les centres,
communauté par communauté.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 8 octobre 2026), coordonnés par le Centro Nacional de Exámenes de l'Institut français d'Espagne.",
           "Un <strong>calendrier national</strong> : mêmes jours, mêmes heures, mêmes fenêtres d'inscription partout — quatre sessions adultes par an, trois junior, deux Prim, une scolaire.",
           "Prochaine session : <strong>février 2027</strong> (écrits du 10 au 13 février), inscriptions du <strong>1<sup>er</sup> décembre 2026 au 9 janvier 2027</strong> ; puis juin, septembre et octobre 2027.",
           "Prix nationaux 2027 : <strong>A1 89 · A2 118 · B1 162 · B2 192 · C1 249 · C2 259 €</strong> (de 87 à 256 € en 2026).",
           "Les diplômes sont reconnus par la <strong>CRUE</strong>, la conférence des recteurs, pour l'accréditation de langue des universités espagnoles.",
           "Résultats à date fixe (17 mars 2027 pour février) ; diplôme deux à trois mois après la session."],
    stats=[("{n}", "centres d'examen", "liste FEI du 8 octobre 2026"), ("192 €", "le DELF B2 en 2027", "même prix dans tous les centres"),
           ("9 janv.", "clôture des inscriptions", "pour la session de février 2027"), ("4", "sessions adultes par an", "février, juin, septembre, octobre")],
    sections=[
        ("calendrier", "Le calendrier national 2027", table(
            "Calendrier DELF-DALF 2027 du Centro Nacional de Exámenes (PDF du 22 septembre 2026), consulté le 8 octobre 2026 : dates des écrits du DELF tout public et du DALF.",
            ["Session", "Inscriptions", "A1", "A2", "B1", "B2", "C1", "C2", "Résultats"],
            [("<strong>Février 2027</strong>", "<strong>1er déc. 2026 – 9 janv. 2027</strong>", "10/02", "12/02", "12/02", "11/02", "10/02", "11/02", "17 mars"),
             ("Juin 2027", "1er mars – 16 avril", "01/06", "03/06", "03/06", "02/06", "01/06", "02/06", "19 juillet"),
             ("Septembre 2027", "1er juillet – 1er sept.", "28/09", "29/09", "29/09", "28/09", "27/09", "30/09", "2 novembre"),
             ("Octobre 2027", "30 août – 22 sept.", "21/10", "21/10", "20/10", "19/10", "18/10", "21/10", "13 décembre")]) + """
<p>Les oraux s'étalent sur plusieurs semaines autour des écrits. La session de septembre est réservée aux adultes et
au DALF. DELF junior : 13 février, 5 et 12 juin, 23 octobre 2027 ; DELF Prim : 21 mai ou 10 juin 2027 (inscriptions
du 1<sup>er</sup> mars au 16 avril) ; DELF scolaire : 28 et 29 avril 2027, réservé aux élèves des établissements
publics sous convention. Tous les centres n'ouvrent pas toutes les sessions, et certains ont leur propre date de
clôture : l'université de Castille-La Manche clôt février le 2 janvier, l'Institut français de Barcelone le 10 janvier. La
session d'octobre 2026 (écrits du 19 au 24 octobre) est close ; ses résultats tombent le 10 décembre 2026.</p>"""),
        ("prix", "Combien coûte le DELF en Espagne ?", table(
            "Tarifs nationaux du Centro Nacional de Exámenes : grille 2027 (PDF du 22 septembre 2026) et grille 2026 relevée dans les documents de plusieurs centres, consultés le 8 octobre 2026.",
            ["Examen", "2026", "2027"],
            [("DELF A1", "87 €", "89 €"), ("DELF A2", "115 €", "118 €"), ("DELF B1", "160 €", "162 €"),
             ("<strong>DELF B2</strong>", "<strong>188 €</strong>", "<strong>192 €</strong>"), ("DALF C1", "244 €", "249 €"), ("DALF C2", "256 €", "259 €"),
             ("DELF Prim A1.1 · A1 · A2", "68 · 87 · 115 €", "69 · 89 · 118 €"),
             ("DELF scolaire A1 · A2 · B1 · B2", "—", "66,75 · 88,50 · 121,50 · 144 €")], wide=False) + """
<p>Ce sont « exactement les mêmes tarifs, fixés au niveau national » par le service de coopération de l'ambassade,
précise le CNE ; le DELF junior coûte le prix du tout public. Des réductions existent localement — l'université de
Cadix fait payer 94 € le B2 à ses étudiants de dernière année. Seul écart relevé : l'Alliance de Vigo affichait pour
octobre 2026 un junior B1 à 157 € et un B2 à 184 €.</p>"""),
        ("inscription", "S'inscrire, résultats et diplôme", """<p>On s'inscrit <strong>auprès d'un centre</strong>, jamais auprès du CNE : en ligne pour les Instituts français,
les Alliances de Madrid et de Málaga, les universités de Navarre et de Cadix ; par fiche et virement envoyés par
e-mail à Burgos, Gijón, Salamanque, Las Palmas, Oviedo ou Vigo ; sur place seulement à Santander. L'inscription
n'est effective qu'avec le paiement. Le jour J : DNI, NIE, passeport ou permis de conduire, et la convocation
imprimée — aucun candidat n'est admis après le début des épreuves.</p>

<p>Les résultats sont publiés à la date fixée pour chaque session ; le diplôme arrive deux à trois mois après la
session selon le CNE (trois à quatre selon certains centres), et un certificat provisoire peut être demandé. Il faut
50 points sur 100, sans note inférieure à 5 sur 25 dans une épreuve ; le dictionnaire est interdit au DELF. La règle
la plus répandue : pas de remboursement, mais un report sur la session suivante pour un motif médical ou de force
majeure justifié — les Instituts français de Madrid et de Bilbao accordent 14 jours de rétractation, celui de
Valence rembourse jusqu'à la clôture, moins 30 €.</p>

<p>Le CNE met en avant les usages du diplôme en Espagne : il est reconnu par la CRUE pour l'accréditation de langue
des universités ; selon lui, le B1 permet de valider le niveau exigé pour le diplôme de <em>grado</em> dans la plupart
des communautés autonomes, et le B2 est le minimum requis pour une bourse Erasmus.</p>"""),
    ],
    list_title="Les {n} centres d'examen, communauté par communauté",
    toc_regions=6,
    faq=[("Quand a lieu la prochaine session du DELF en Espagne ?", "En février 2027 : DALF C1 et DELF A1 le 10 février, B2 et C2 le 11, B1 et A2 le 12, DELF junior le 13. Les inscriptions sont ouvertes du 1er décembre 2026 au 9 janvier 2027 — quelques centres ont leur propre date de clôture, comme l'université de Castille-La Manche (2 janvier) ou l'Institut français de Barcelone (10 janvier) —, et les résultats sont publiés le 17 mars 2027."),
         ("Combien coûte le DELF B2 en Espagne ?", "192 € en 2027 (188 € en 2026), dans tous les centres : le tarif est fixé au niveau national par le service de coopération de l'ambassade de France. Le DALF C1 coûte 249 €, le C2 259 €."),
         ("Le prix du DELF change-t-il d'un centre à l'autre en Espagne ?", "Non : le Centro Nacional de Exámenes applique exactement les mêmes tarifs partout. Seules varient les réductions propres à un centre, comme les 94 € de l'université de Cadix pour ses étudiants de dernière année."),
         ("Le DELF est-il reconnu par les universités espagnoles ?", "Oui : les diplômes DELF et DALF figurent dans la table d'équivalences de la CRUE, la conférence des recteurs des universités espagnoles, qui retient aussi le TCF tout public par tranches de points. Seuls les examens passés en présentiel sont acceptés."),
         ("Quand reçoit-on le diplôme du DELF en Espagne ?", "Deux à trois mois après la session, selon le Centro Nacional de Exámenes (trois à quatre selon certains centres). Un certificat provisoire peut être demandé dès la publication des résultats.")],
    also=[("/centres/tcf-espagne/", "TCF Canada en Espagne", "11 centres, de 275 à 287 €, les prochaines dates."),
          ("/blog/calendrier-delf-dalf-2026-2027/", "Calendrier DELF-DALF 2026-2027 en France", "Les dix sessions nationales françaises."), A_DELF, A_DIPL],
    sources="site du Centro Nacional de Exámenes (delf-dalf.es : calendriers 2026 et 2027, tarifs, FAQ, inscription, DELF scolaire), table d'équivalences de la CRUE pour le français, et sites des centres d'examen (calendriers, tarifs et conditions DELF-DALF), consultés le 8 octobre 2026.",
    notes={"carthagene-alliance-francaise-de-cartagena": "Le site indiqué par FEI (afcartagena.org) renvoyait le 8 octobre 2026 vers une page sans rapport, sur le transfert d'argent : ne l'utilisez pas. Sessions aussi à Molina de Segura et Alicante.",
           "vitoria-gasteiz-alliance-francaise-de-vitoria": "Le site indiqué par FEI ne répond plus, et le centre national des examens masque cette Alliance dans sa liste : statut à vérifier.",
           "ciudad-real-universidad-de-castilla-la-mancha": "Quatre campus : Albacete, Ciudad Real, Cuenca, Tolède ; inscriptions de février 2027 closes dès le 2 janvier.",
           "santander-alliance-francaise-de-santander": "Inscriptions sur place uniquement.",
           "logrono-fundacion-universidad-de-la-rioja": "En 2027, session de juin seulement ; inscriptions par e-mail."},
    urls={"carthagene-alliance-francaise-de-cartagena": "https://www.alianzafrancesacartagena.org/delf-dalf/",
          "ciudad-real-universidad-de-castilla-la-mancha": "https://www.uclm.es/misiones/internacional/inmersion_linguistica/centro-de-lenguas/delf",
          "saint-sebastien-alliance-francaise-de-san-sebastian": "https://afdonostiasansebastian.org/diplomas-delf-dalf/",
          "gerone-alliance-francaise-de-girona": "https://examensdelf.cat/",
          "granollers-alliance-francaise-de-granollers": "https://examensdelf.cat/",
          "logrono-fundacion-universidad-de-la-rioja": "https://www.unirioja.es/facultades-escuelas-y-centros/casa-de-las-lenguas/delf-dalf/",
          "vitoria-gasteiz-alliance-francaise-de-vitoria": ""},
))

# ===========================================================================
# ÉTATS-UNIS
# ===========================================================================
US_CA = ["detroit-bingham-farms-alliance-francaise-detroit-french-institute", "cambridge-lycee-international-de-boston",
         "new-york-lalliance-new-york", "denver-alliance-francaise", "denver-pluma-academy", "philadelphie-alliance-francaise",
         "kansas-city-alliance-francaise", "houston-alliance-francaise", "san-francisco-alliance-francaise"]
US_NO = ["atlanta-alliance-francaise", "chicago-alliance-francaise", "seattle-alliance-francaise", "washington-alliance-francaise"]
PAGES.append(dict(
    slug="tcf-etats-unis", exam="tcf", file="tcf_etats_unis", layout="regions", chip="États-Unis",
    crumb="TCF aux États-Unis",
    pointer="9 des 18 centres agréés proposent le TCF Canada, de 330 à 460 $ ; Houston, New York et Boston avaient encore des places.",
    title="TCF Canada aux États-Unis : 9 centres, prix et dates",
    desc="TCF Canada aux États-Unis : 9 des 18 centres agréés le proposent, de 330 à 460 $ — Houston, New York, Detroit… Places restantes et inscription.",
    h1="TCF Canada aux États-Unis : les centres qui le proposent, les prix et les places",
    intro="""Aux États-Unis, {n} centres sont agréés pour le TCF par France Éducation international, mais <strong>neuf
seulement proposaient le TCF Canada</strong> le 8 octobre 2026 d'après leur site — de <strong>330 $</strong> à Detroit à
<strong>460 $</strong> à San Francisco. Quatre ne le font pas, malgré la liste : Atlanta, Chicago, Seattle et Washington,
qui orientent vers le TEF Canada. Et les places sont rares : San Francisco, Philadelphie, Denver et Kansas City
affichaient complet pour le reste de 2026, Detroit jusqu'en avril 2027 ; Houston, New York et Boston avaient encore
des dates.""",
    facts=["<strong>{n} centres agréés</strong> (liste FEI du 8 octobre 2026), <strong>9 qui proposent le TCF Canada</strong> : Detroit, Boston (International School), New York, Denver (Alliance et Pluma Academy), Philadelphie, Kansas City, Houston et San Francisco.",
           "<strong>Pas de TCF Canada</strong> à Atlanta (aucun TCF), Chicago (tout public et IRN), Seattle (aucun TCF) ni Washington (DAP seulement) : ces Alliances orientent vers le TEF Canada.",
           "Prix du TCF Canada : <strong>330 à 460 $</strong> — Detroit 330, Boston 350, New York 350 (membres) ou 399, Denver et Philadelphie 360, Kansas City 370, Houston 400, Pluma Academy 435, San Francisco 460.",
           "⚠️ <strong>Complet</strong> pour le reste de 2026 à San Francisco, Philadelphie, Denver (Alliance) et Kansas City ; jusqu'en avril 2027 à Detroit.",
           "Encore des places le 8 octobre : <strong>Houston chaque mercredi</strong> jusqu'au 27 janvier 2027, <strong>New York</strong> (26 octobre, 6 et 16 novembre, 14 décembre), <strong>Boston</strong> (21 novembre, 12 décembre), Pluma Academy (sessions individuelles).",
           "Délai entre deux passations : de 20 jours (Detroit) à un mois (New York, Denver) selon le centre."],
    stats=[("9", "centres TCF Canada", "sur {n} centres agréés"), ("330-460 $", "le TCF Canada", "selon le centre"),
           ("4", "centres complets", "pour le reste de 2026"), ("2 ans", "de validité", "résultats en 10 jours à 6 semaines")],
    sections=[
        ("releve", "Qui fait passer le TCF Canada aux États-Unis : le relevé", releve([
            ("Alliance française de Detroit (Bingham Farms, Michigan)", "<strong>Canada</strong>, IRN, tout public, DAP", "Canada <strong>330 $</strong> · IRN 300 $ (280 $ membres) · tout public 190 à 350 $",
             "Mensuel, le jeudi : 12/11 et 10/12/2026, puis jusqu'au 15/04/2027 <strong>complets</strong> ; 13/05 et 10/06/2027 ouverts. Sur ordinateur ; résultats sous 10 jours."),
            ("International School of Boston (Cambridge, Massachusetts)", "<strong>Canada</strong>, IRN, Québec, tout public", "Canada <strong>350 $</strong> · IRN 350 $ · +60 $ en semaine",
             "Le samedi : 10/10 complet (liste d'attente), <strong>21/11</strong> (limite 17/11), <strong>12/12</strong> (limite 08/12), janvier. Paiement par carte à l'inscription."),
            ("L'Alliance New York", "<strong>Canada</strong>, IRN", "<strong>350 $</strong> membres · 399 $ non-membres, + 15 $ de frais",
             "Quasi mensuel : <strong>26/10</strong> à Montclair, New Jersey (limite 13/10), <strong>06/11</strong> à Manhattan (limite 26/10), 16/11 et 14/12 à Montclair. Sur ordinateur."),
            ("Alliance française de Denver", "<strong>Canada</strong> ; IRN et tout public sur demande", "Canada <strong>360 $</strong> · IRN 360 $",
             "16/11, 30/11 et 07/12/2026 <strong>complets</strong> ; aucune date 2027. Clôture sept jours ouvrés avant ; passeport obligatoire."),
            ("Alliance française de Philadelphie", "<strong>Canada</strong>, IRN, tout public", "Canada <strong>360 $</strong> (340 $ membres) · IRN 300 $",
             "16/10 et 18/12/2026 <strong>complets</strong> ; liste d'attente ; inscriptions closes un mois avant. Sur papier."),
            ("Alliance française de Kansas City", "<strong>Canada</strong>, IRN, tout public, Québec", "Canada <strong>370 $</strong> (380 $ en 2027) · IRN 370 $",
             "2026 <strong>complet</strong> ; 2027 : 14/01 (une place), 28/01, 04/02, 18/02, 04/03… jusqu'au 24/06, quatre places par session. Sur ordinateur."),
            ("Alliance française de Houston", "<strong>Canada</strong> (IRN, tout public et Québec annoncés, sans date)", "Canada <strong>400 $</strong>",
             "<strong>Chaque mercredi</strong>, dix places : 14, 21, 28/10, 04/11, 02, 09, 16/12/2026, puis du 06 au 27/01/2027 ; clôture trois jours avant. Sur ordinateur."),
            ("Pluma Academy (Denver)", "<strong>Canada</strong>, IRN, tout public", "Canada <strong>435 $</strong> · IRN 435 $ · tout public 255 à 435 $",
             "Sessions individuelles, une vingtaine de dates par mois d'octobre à mars ; rappel sous 24 h après l'inscription. Sur ordinateur (papier : +70 $)."),
            ("Alliance française de San Francisco", "<strong>Canada</strong>, IRN, tout public", "Canada <strong>460 $</strong> · IRN 550 $ · tout public 250 $ + 180 $ par expression",
             "TCF Canada <strong>complet</strong> jusqu'à fin 2026 (liste d'attente) ; aucune date 2027. Passeport obligatoire ; 25 jours entre deux TCF."),
            ("Alliance française d'Atlanta", "<strong>aucun TCF</strong>", "—", "« We do NOT currently offer TCF or TEF exams », écrit l'Alliance."),
            ("Alliance française de Chicago", "tout public et IRN — <strong>pas de Canada</strong>", "tout public 215 à 385 $", "Oriente vers le TEF Canada (415 $), presque complet jusqu'à mi-décembre."),
            ("Alliance française de Seattle", "<strong>aucun TCF</strong> sur son site", "—", "Oriente vers le TEF (TEF Canada 365 $)."),
            ("Alliance française de Washington", "DAP seulement — <strong>pas de Canada</strong>", "DAP 350 $", "Pour l'immigration au Canada, l'Alliance renvoie au TEF Canada."),
            ("Alliances de Los Angeles, Pasadena et San Diego ; French American School of Puget Sound ; Wesleyan University", NR, NR, "Agréés par FEI, non vérifiés le 8 octobre 2026 : consultez leur site."),
        ])),
        ("inscription", "S'inscrire, et trouver une place", """<p>Chaque centre vend l'examen sur son site — boutique en ligne, sélecteur de sessions ou formulaire suivi d'un
paiement par carte — et l'inscription n'est ferme qu'une fois payée. Saisissez votre nom exactement comme sur le
passeport : pour le TCF Canada, Detroit déclare le numéro de passeport à FEI, San Francisco et Denver exigent un
passeport valide, et la pièce présentée le jour J doit être celle de l'inscription. Les règles d'annulation sont
strictes : rien n'est remboursé à Houston ni à Denver ; Detroit retient 40 $ jusqu'à dix jours ouvrés avant, San
Francisco 60 $ à plus de 30 jours, New York 80 $ avant la clôture — et San Francisco n'accepte plus aucun changement
dans les huit jours qui précèdent l'examen.</p>

<p>Le délai entre deux passations dépend du centre : 20 jours à Detroit, 21 chez Pluma Academy, 25 à San Francisco,
un mois à New York et à Denver. Les résultats arrivent par e-mail ou sur la plateforme de FEI, de 10 jours (Detroit)
à cinq ou six semaines (New York) ; l'attestation vaut deux ans, et depuis le 1<sup>er</sup> septembre 2026, FEI
n'accepte plus de recorrection.</p>

<p>Avec quatre centres complets pour le reste de l'année, la <strong>place</strong> décide de tout. Houston ouvrait une
session chaque mercredi jusqu'au 27 janvier 2027, Kansas City vendait ses dates jusqu'en juin 2027, Pluma Academy
reçoit les candidats un par un : il peut valoir la peine de passer le test dans une autre ville. Le
<a href="/tef-canada/">TEF Canada</a>, l'autre test accepté par IRCC, se passe dans les Alliances qui ne font pas le
TCF Canada — Chicago, Seattle, Washington, mais aussi Dallas et Miami.</p>"""),
    ],
    list_title="Les {n} centres TCF agréés, État par État",
    toc_regions=6,
    faq=[("Où passer le TCF Canada aux États-Unis ?", "Dans l'un des neuf centres qui le proposaient le 8 octobre 2026 : les Alliances françaises de Detroit, New York, Denver, Philadelphie, Kansas City, Houston et San Francisco, l'International School of Boston et Pluma Academy, à Denver. Atlanta, Chicago, Seattle et Washington, pourtant agréés pour le TCF, ne font pas le TCF Canada."),
         ("Combien coûte le TCF Canada aux États-Unis ?", "De 330 $ (Detroit) à 460 $ (San Francisco) : 350 $ à Boston, 350 $ pour les membres ou 399 $ à New York, 360 $ à Denver et à Philadelphie, 370 $ à Kansas City, 400 $ à Houston, 435 $ chez Pluma Academy. Relevé le 8 octobre 2026."),
         ("Où trouver une place rapidement ?", "Le 8 octobre 2026, l'Alliance française de Houston ouvrait une session chaque mercredi jusqu'au 27 janvier 2027, New York avait quatre dates d'ici décembre, Boston deux, et Pluma Academy, à Denver, organise des sessions individuelles plusieurs fois par semaine. San Francisco, Philadelphie, Denver (Alliance) et Kansas City étaient complets pour 2026."),
         ("Peut-on passer le TCF Canada à Washington ou à Chicago ?", "Non : l'Alliance française de Washington ne propose plus que le TCF DAP, celle de Chicago le TCF tout public et l'IRN. Toutes deux orientent les candidats à l'immigration vers le TEF Canada, également accepté par IRCC."),
         ("Le TCF Canada passé aux États-Unis est-il accepté par IRCC ?", "Oui : l'attestation est délivrée par France Éducation international quel que soit le centre agréé, et vaut deux ans. IRCC exige des résultats de moins de deux ans à la création du profil Entrée express comme au dépôt de la demande.")],
    also=[("/centres/delf-etats-unis/", "DELF et DALF aux États-Unis", "La session de décembre 2026 et la grille commune."),
          ("/centres/tcf-canada/", "Centres TCF au Canada", "Les 47 centres agréés, province par province."), A_TEF, A_NCLC],
    sources="sites des Alliances françaises de Detroit, Atlanta, Chicago, Denver, Houston, Kansas City, New York, Philadelphie, San Francisco, Seattle et Washington, de l'International School of Boston et de Pluma Academy (pages TCF, boutiques et sélecteurs de sessions, conditions et politiques d'examen), consultés le 8 octobre 2026.",
    badges=dict({k: OK_CA for k in US_CA}, **{k: NO_CA for k in US_NO}),
    notes={"cambridge-lycee-international-de-boston": "Devenu l'International School of Boston (ISB Extension, ouvert aux adultes).",
           "philadelphie-alliance-francaise": "Examen sur papier, selon l'Alliance."},
))

PAGES.append(dict(
    slug="delf-etats-unis", exam="delf", file="delf_etats_unis", layout="regions", chip="États-Unis",
    crumb="DELF aux États-Unis",
    pointer="",
    title="DELF aux États-Unis : {n} centres, dates et prix 2026",
    desc="DELF et DALF aux États-Unis : la session du 7 au 11 décembre 2026, une grille commune (B2 190 $) et ses frais en sus, les 40 centres agréés et l'inscription.",
    h1="DELF et DALF aux États-Unis : les {n} centres, les dates et les prix",
    intro="""Aux États-Unis, le DELF et le DALF se passent dans <strong>{n} centres agréés</strong> — surtout des Alliances
françaises, mais aussi des écoles internationales et des universités —, sous l'égide de Villa Albertine, le service
culturel de l'ambassade, qui ne publie ni calendrier ni tarifs : ce sont les centres qui le font. Ils affichent
pourtant les mêmes semaines — <strong>19-23 octobre</strong> et <strong>7-11 décembre 2026</strong> — et la même
grille : <strong>B2 190 $</strong>, auxquels certains ajoutent des frais. Pour décembre, les inscriptions ferment entre
le 7 novembre (Houston) et le 30 novembre (Chicago).""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 8 octobre 2026) : Alliances françaises, écoles internationales et d'immersion, universités ; Villa Albertine, à Washington, est l'organisme de gestion.",
           "Prochaine session tout public : <strong>7 au 11 décembre 2026</strong> — A1 et A2 le lundi, B1 le mardi, B2 le mercredi, C1 le jeudi, C2 le vendredi.",
           "Grille commune : <strong>A1 135 · A2 145 · B1 155 · B2 190 · C1 et C2 245 $</strong> ; frais en sus à New York (+50 $), San Francisco (+60 $), Miami (+50 $), Dallas (+30 $).",
           "Clôture des inscriptions de décembre : Houston 7 novembre, New York 12, Washington 13, San Francisco 15, Seattle 25, Dallas et Saint-Louis 27, Chicago 30 novembre.",
           "⚠️ Déjà complets le 8 octobre : B2 et C1 à Chicago ; B1, B2 et C1 à Philadelphie ; C1 à Denver et à Miami ; B2 à Boston.",
           "Aucune date 2027 publiée ; le diplôme, imprimé en France, arrive trois à six mois après la session."],
    stats=[("{n}", "centres d'examen", "liste FEI du 8 octobre 2026"), ("190 $", "le DELF B2", "grille commune, hors frais"),
           ("7-11 déc.", "prochaine session", "clôtures du 7 au 30 novembre"), ("à vie", "validité du diplôme", "même diplôme qu'en France")],
    sections=[
        ("calendrier", "La session de décembre 2026, centre par centre", table(
            "Relevé des sites des centres le 8 octobre 2026. Grille commune : A1 135 $, A2 145 $, B1 155 $, B2 190 $, C1 et C2 245 $.",
            ["Centre", "Niveaux en décembre", "Inscriptions", "Prix"],
            [("<strong>L'Alliance New York</strong>", "A1 à C2", "jusqu'au 12 novembre", "grille + 50 $ de frais"),
             ("<strong>Alliance française de Washington</strong>", "A1 à C2 ; une seule session par an", "du 9 (9 h) au 13 novembre", "grille"),
             ("<strong>Alliance française de Chicago</strong>", "A1, A2, B1, C2 ; B2 et C1 complets", "jusqu'au 30 novembre", "grille"),
             ("<strong>Alliance française de Houston</strong>", "A1 à C2", "jusqu'au 7 novembre", "grille ; changement de date 50 $"),
             ("<strong>Alliance française de Dallas</strong>", "A1 à C2", "du 19 octobre au 27 novembre", "grille + 30 $"),
             ("<strong>Alliance française Miami Metro</strong>", "A1, A2, B1, B2, C2 ; C1 complet", "jusqu'au 27 novembre", "grille + 50 $"),
             ("<strong>Alliance française de San Francisco</strong>", "A1 à C2 ; junior du 1er au 4 décembre", "jusqu'au 15 novembre", "grille + 60 $ (30 $ membres)"),
             ("<strong>Alliance française de Seattle</strong>", "A1 à C2", "du 19 octobre au 25 novembre (9 h)", "grille"),
             ("<strong>Alliance française de Denver</strong>", "B1, B2, C2 ; C1 complet", "du 1er septembre au 20 novembre", "grille propre : B1 217, B2 270, C1 et C2 334 $"),
             ("<strong>Alliance française de Philadelphie</strong>", "A1, A2 ; B1, B2, C1 complets ; pas de C2", "ouvertes depuis le 5 octobre", "grille ; envoi du diplôme 8 $"),
             ("<strong>Alliance française de Saint-Louis</strong>", "A1 à C2", "jusqu'au 27 novembre", "grille ; hausse annoncée en 2027"),
             ("<strong>Alliance française de La Nouvelle-Orléans</strong>", "A1 à B2", "du 19 octobre au 27 novembre", "grille"),
             ("<strong>International School of Boston</strong>", "A1 à C2, un niveau par jour du 7 au 12 ; B2 complet", "jusqu'au 15 novembre", "grille + 50 $"),
             ("<strong>Alliance française de Porto Rico</strong>", "A1 à C2", "jusqu'au 21 novembre", "grille ; −5 % pour les membres"),
             ("<strong>Alliance française d'Atlanta</strong>", "A1 à C2", "pas encore ouvertes en ligne", "grille")]) + """
<p>Villa Albertine ne publie pas de calendrier national : selon l'Alliance de Charlotte, les dates et les tarifs
sont fixés « par l'ambassade de France à Washington et France Éducation international ». En pratique, les centres
affichent les mêmes semaines — mars, avril, juin, octobre et décembre en 2026 — et chacun n'en ouvre qu'une partie :
Washington une seule par an, en décembre ; Charlotte, Milwaukee et La Nouvelle-Orléans de l'A1 au B2 seulement. Le
DELF junior a lieu du 1<sup>er</sup> au 4 décembre 2026 à San Francisco ; ailleurs, plutôt en mars — Chicago annonce
une session en mars 2027, inscriptions ouvertes en novembre. Aucune date tout public 2027 n'était publiée le 8
octobre 2026.</p>"""),
        ("prix", "Combien coûte le DELF aux États-Unis ?", table(
            "Grille commune relevée dans la plupart des centres le 8 octobre 2026, hors frais administratifs propres à chaque centre.",
            ["Niveau", "Tout public", "Junior", "Prim"],
            [("A1.1", "—", "—", "125 $"), ("A1", "135 $", "135 $", "135 $"), ("A2", "145 $", "145 $", "145 $"),
             ("B1", "155 $", "155 $", "—"), ("<strong>B2</strong>", "<strong>190 $</strong>", "190 $", "—"),
             ("C1 (DALF)", "245 $", "—", "—"), ("C2 (DALF)", "245 $", "—", "—")], wide=False) + """
<p>Plusieurs centres ajoutent des frais : 50 $ à New York, à Miami et à l'International School of Boston, 60 $ à San
Francisco (30 $ pour les membres), 30 $ à Dallas à partir de décembre 2026 — soit un DELF B2 à 240 $ à New York. À
l'inverse, Chicago facture le DELF Prim moins cher (110 à 130 $). L'Alliance française de Denver applique sa propre
grille, plus chère : B1 217 $, B2 270 $, C1 et C2 334 $.</p>"""),
        ("inscription", "S'inscrire, résultats et diplôme", """<p>Pas de plateforme nationale : on s'inscrit auprès d'un centre — boutique en ligne (Dallas, Houston,
Seattle, Philadelphie, Saint-Louis, San Francisco), plateforme externe (New York, Chicago, Washington avec un compte),
formulaire et paiement par téléphone ou par chèque (Minneapolis, Saint-Louis). Pièce d'identité : passeport, carte
d'identité ou permis de conduire avec photo. La convocation arrive une semaine avant à New York et à Washington,
dix jours avant à Seattle.</p>

<p>Les frais sont rarement remboursables : jamais à Houston, Chicago, Miami ou San Francisco ; avant la clôture,
moins 80 $ à New York et à Atlanta, 40 $ à Seattle, 50 $ à Denver. Les résultats arrivent par e-mail de deux
semaines (Minneapolis) à six ou huit semaines (Philadelphie, Milwaukee, San Francisco) après l'examen ; le diplôme,
imprimé en France, suit trois à six mois après la session. À Washington, il se retire uniquement en personne ; San
Francisco propose un envoi pour 30 $.</p>

<p>Aux États-Unis, le DELF sert aussi au programme TAPIF d'assistants de langue en France, qui demande au moins le
niveau B1 ; et le DELF B2, rappelle l'Alliance de Washington, ouvre l'accès aux universités françaises sans test de
langue préalable.</p>"""),
    ],
    list_title="Les {n} centres d'examen, État par État",
    toc_regions=6,
    faq=[("Quand a lieu la prochaine session du DELF aux États-Unis ?", "Du 7 au 11 décembre 2026 dans la plupart des centres : A1 et A2 le lundi 7, B1 le 8, B2 le 9, C1 le 10, C2 le 11. Les inscriptions ferment entre le 7 novembre (Houston) et le 30 novembre (Chicago) ; aucune date 2027 n'était publiée le 8 octobre 2026."),
         ("Combien coûte le DELF B2 aux États-Unis ?", "190 $ selon la grille commune des centres, auxquels certains ajoutent des frais : 240 $ au total à New York et à Miami, 250 $ à San Francisco (220 $ pour les membres), 220 $ à Dallas. L'Alliance française de Denver applique sa propre grille : 270 $."),
         ("Où passer le DELF à New York ?", "À L'Alliance New York (22 East 60th Street), qui organise le DELF et le DALF tout public en juin et en décembre : la session de décembre 2026 a lieu du 7 au 11 décembre, inscriptions jusqu'au 12 novembre, 135 à 245 $ plus 50 $ de frais administratifs. L'Alliance de Westchester n'organisait aucune session en 2026."),
         ("Peut-on passer le DELF junior aux États-Unis ?", "Oui, dans les Alliances et les écoles internationales : San Francisco l'organise du 1er au 4 décembre 2026 (inscriptions jusqu'au 15 novembre) ; la plupart des autres centres le proposent en mars — Chicago annonce une session en mars 2027, inscriptions ouvertes en novembre. Prix : 135 à 190 $ selon le niveau."),
         ("Quand arrive le diplôme du DELF ?", "Les résultats arrivent par e-mail deux à huit semaines après l'examen selon le centre ; le diplôme, imprimé en France, trois à six mois après la session. À Washington, il se retire uniquement en personne ; San Francisco propose un envoi pour 30 $.")],
    also=[("/centres/tcf-etats-unis/", "TCF Canada aux États-Unis", "Neuf centres, de 330 à 460 $, et les places restantes."),
          ("/centres/delf-mexique/", "DELF et DALF au Mexique", "Un calendrier et une grille nationaux, 71 centres."), A_DELF, A_DIPL],
    sources="page « Language Certifications » de Villa Albertine ; sites des Alliances françaises de New York, Washington, Chicago, Houston, Dallas, Miami, San Francisco, Seattle, Denver, Philadelphie, Saint-Louis, La Nouvelle-Orléans, Atlanta, Charlotte, Milwaukee, Minneapolis, Westchester et Porto Rico, et de l'International School of Boston (calendriers, tarifs et conditions DELF-DALF), consultés le 8 octobre 2026.",
    notes={"mamaroneck-alliance-francaise-de-westchester": "Aucune session DELF en 2026 ; l'Alliance annonce une réorganisation.",
           "denver-pluma-academy": "Son site ne mentionne pas le DELF.",
           "cambridge-lycee-international-de-boston": "Devenu l'International School of Boston ; ouvert aux adultes via l'ISB Extension."},
))

# ===========================================================================
# MEXIQUE
# ===========================================================================
PAGES.append(dict(
    slug="tcf-mexique", exam="tcf", file="tcf_mexique", layout="cities", chip="Mexique",
    crumb="TCF au Mexique",
    pointer="5 des 11 centres agréés affichent le TCF Canada, de 4 800 à 6 500 pesos : IFAL à Mexico, Guadalajara, Puebla, Pachuca, Aguascalientes.",
    title="TCF Canada au Mexique : 5 centres, 4 800 à 6 500 pesos",
    desc="TCF Canada au Mexique : l'IFAL à Mexico (5 150 pesos), les Alliances de Guadalajara (4 950) et Puebla (4 800), l'UAEH… Dates et inscription.",
    h1="TCF Canada au Mexique : les centres qui le proposent, les prix et les dates",
    intro="""Au Mexique, {n} centres sont agréés pour le TCF par France Éducation international, et <strong>cinq
affichaient le TCF Canada</strong> le 8 octobre 2026 : l'<strong>IFAL</strong> à Mexico (5 150 pesos en session de
calendrier, 6 500 à une date sur demande), l'<strong>Alliance française de Guadalajara</strong> (4 950), celle de
<strong>Puebla</strong> (4 800, sur demande), l'université autonome d'Hidalgo à Pachuca (5 800) et l'Alliance
d'Aguascalientes. Prochaines sessions de calendrier : le <strong>27 octobre</strong> à Guadalajara, le
<strong>28 octobre</strong> et le 2 décembre à l'IFAL.""",
    facts=["<strong>{n} centres agréés</strong> (liste FEI du 8 octobre 2026), <strong>5 qui affichent le TCF Canada</strong> : l'IFAL (Mexico), les Alliances de Guadalajara, Puebla et Aguascalientes, l'UAEH (Pachuca).",
           "Prix du TCF Canada : <strong>4 800 pesos</strong> à Puebla, <strong>4 950</strong> à Guadalajara, <strong>5 150</strong> à l'IFAL (6 500 sur demande), <strong>5 800</strong> à l'UAEH.",
           "Sessions de calendrier : Guadalajara un mardi par mois (<strong>27 octobre, 24 novembre, 15 décembre</strong>) ; IFAL <strong>28 octobre</strong> (inscriptions du 5 au 21 octobre) et <strong>2 décembre</strong> (du 9 au 25 novembre).",
           "<strong>Sur demande</strong> : à l'IFAL, à Puebla (dix jours d'avance, jamais le week-end), à l'UAEH ; à Aguascalientes, à partir de cinq inscrits.",
           "Le TCF Canada n'apparaît ni chez Proulex, ni dans les Alliances de Guanajuato, Mexicali, San Luis Potosí et Zacatecas, ni au CCLT de Tepic.",
           "Résultats à date fixe à l'IFAL (environ quatre semaines), en 15 jours à trois semaines à Guadalajara ; 20 jours après les résultats pour s'y réinscrire."],
    stats=[("5", "centres TCF Canada", "sur {n} centres agréés"), ("4 800-6 500", "pesos le TCF Canada", "selon le centre et la formule"),
           ("27 oct.", "prochaine session", "Guadalajara ; IFAL le 28"), ("2 ans", "de validité", "résultats en 2 à 4 semaines")],
    sections=[
        ("releve", "Qui fait passer le TCF Canada au Mexique : le relevé", releve([
            ("IFAL — Institut français d'Amérique latine (Mexico)", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>5 150</strong> (session) · <strong>6 500</strong> (sur demande) · IRN 4 800 · Québec 1 700 par épreuve",
             "<strong>28/10</strong> (inscriptions du 5 au 21/10, résultats le 23/11) et <strong>02/12/2026</strong> (du 9 au 25/11, résultats le 04/01/2027) ; IRN et Québec sur demande. Sur ordinateur."),
            ("Alliance française de Guadalajara (Ciudad del Sol, Zapopan)", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>4 950</strong> · IRN 4 250 · Québec 5 000 · date hors calendrier +750",
             "Dix mardis en 2026 : <strong>27/10, 24/11, 15/12</strong> ; Québec le 10/11. Inscription par WhatsApp ou par e-mail. Sur ordinateur."),
            ("Alliance française de Puebla", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>4 800</strong> · IRN 3 600 · Québec 1 200 par épreuve",
             "Sur demande, au moins dix jours avant, jamais le week-end ; paiement dans la boutique en ligne ; droits non remboursables. Sur ordinateur."),
            ("UAEH — université autonome d'Hidalgo (Pachuca)", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>5 800</strong> · IRN 4 600 · Québec 1 800 par épreuve",
             "Sur demande ; formulaire et preuve de paiement à déposer sur place, au Centro de Lenguas."),
            ("Alliance française d'Aguascalientes", "<strong>Canada</strong>, tout public, IRN, Québec", "aucun tarif publié",
             "Session ouverte à partir de cinq inscrits ; aucune date publiée."),
            ("Proulex (Guadalajara)", "tout public seulement", "tarifs affichés datés de 2020", "Pages examens anciennes : à confirmer auprès du centre."),
            ("Alliance française de Guanajuato", "TCF, Québec, IRN — <strong>pas de Canada</strong>", "aucun tarif publié", "Sessions personnalisées toute l'année, selon la Fédération des Alliances."),
            ("Alliance française de San Luis Potosí", "TCF, Québec, IRN — <strong>pas de Canada</strong>", "aucun tarif publié", "Sessions personnalisées et calendrier défini, selon la Fédération : dates à confirmer."),
            ("Alliance française de Zacatecas", "TCF, Québec, IRN — <strong>pas de Canada</strong>", "aucun tarif publié", "Sessions personnalisées toute l'année."),
            ("Alliance française de Mexicali", "aucun TCF sur son site", "—", "Le site ne parle que du DELF ; ses coordonnées diffèrent de celles de FEI."),
            ("Colegio de Ciencias y Letras de Tepic", "aucun TCF sur son site", "—", "Le site ne cite que des certifications d'anglais."),
        ], caption="Ce que le site de chaque centre affichait le 8 octobre 2026, prix en pesos mexicains. « Non relevé » : non publié, ou non vérifié — le site du centre fait foi.")),
        ("inscription", "S'inscrire au TCF Canada au Mexique", """<p>La procédure tient en trois temps : <strong>fixer la date</strong> avec le centre — ou s'inscrire pendant
la période d'une session de calendrier —, <strong>remplir le formulaire</strong> — l'IFAL et l'UAEH demandent le
numéro de passeport pour le TCF Canada —, puis <strong>payer</strong> : virement ou dépôt bancaire à l'IFAL, boutique
en ligne à Puebla, dossier déposé sur place à l'UAEH. À Puebla, l'inscription se finalise sous 72 heures avec le scan
du passeport, dont l'original se présente le jour de l'examen. Le TCF se passe sur ordinateur à l'IFAL, à Guadalajara
et à Puebla ; l'oral, en face-à-face.</p>

<p>Puebla précise que les droits ne sont pas remboursables — report à la session suivante sur certificat médical ;
les autres centres ne publient pas de règle. À Guadalajara, il faut attendre 20 jours après les résultats pour se
réinscrire. Les résultats tombent à une date fixe à l'IFAL — le 23 novembre pour la session du 28 octobre —, en 15
jours à trois semaines à Guadalajara. L'attestation vaut deux ans ; depuis le 1<sup>er</sup> septembre 2026, FEI
n'accepte plus de recorrection.</p>

<p>Le choix se joue sur le calendrier : une session de calendrier coûte moins cher qu'une date sur demande — 5 150
contre 6 500 pesos à l'IFAL, 750 pesos de plus hors calendrier à Guadalajara —, mais une date sur demande s'obtient
en dix jours à Puebla. Le <a href="/tef-canada/">TEF Canada</a>, l'autre test accepté par IRCC, est proposé selon la
Fédération par les Alliances de Mexico, Monterrey, Puebla, Oaxaca, Cuernavaca, San Luis Potosí et Texcoco.</p>"""),
    ],
    list_title="Les {n} centres TCF agréés, ville par ville",
    faq=[("Où passer le TCF Canada à Mexico ?", "À l'IFAL, l'Institut français d'Amérique latine (Río Nazas 43, colonia Cuauhtémoc) : 5 150 pesos en session de calendrier — prochaines le 28 octobre (inscriptions du 5 au 21 octobre) et le 2 décembre 2026 (du 9 au 25 novembre) —, 6 500 pesos à une date sur demande. L'Alliance française de Mexico ne fait pas passer le TCF."),
         ("Combien coûte le TCF Canada au Mexique ?", "De 4 800 pesos (Alliance française de Puebla) à 6 500 pesos (IFAL, date sur demande) : 4 950 à l'Alliance de Guadalajara, 5 150 à l'IFAL en session de calendrier, 5 800 à l'UAEH. Relevé le 8 octobre 2026."),
         ("Où passer le TCF Canada à Guadalajara ?", "À l'Alliance française de Guadalajara, au centre Ciudad del Sol (Zapopan) : 4 950 pesos, un mardi par mois — 27 octobre, 24 novembre et 15 décembre 2026 —, inscription par WhatsApp ou par e-mail. Proulex, l'autre centre agréé de la ville, ne publie que le TCF tout public."),
         ("Peut-on passer le TCF Canada à une date de son choix ?", "Oui, à l'IFAL (6 500 pesos), à l'Alliance française de Puebla (au moins dix jours à l'avance, du lundi au vendredi) et à l'UAEH ; à Guadalajara, une date hors calendrier coûte 750 pesos de plus. Aguascalientes ouvre une session dès cinq inscrits."),
         ("Le TCF Canada passé au Mexique est-il accepté par IRCC ?", "Oui : l'attestation est délivrée par France Éducation international quel que soit le centre agréé, et vaut deux ans. Vérifiez seulement que c'est le TCF Canada, et non le tout public, qui figure sur votre inscription.")],
    also=[("/centres/delf-mexique/", "DELF et DALF au Mexique", "Le calendrier et les tarifs nationaux, 71 centres."),
          ("/centres/tcf-colombie/", "TCF Canada en Colombie", "Les sept Alliances françaises agréées."), A_TEF, A_NCLC],
    sources="sites de l'IFAL, des Alliances françaises de Guadalajara, Puebla, Aguascalientes, Guanajuato, Mexicali, San Luis Potosí et Zacatecas, de la Fédération des Alliances françaises du Mexique, de Proulex, de l'UAEH et du CCLT de Tepic (pages TCF, tarifs et calendriers 2026, formulaires, boutiques), consultés le 8 octobre 2026.",
    badges={"mexico-institut-francais-amerique-latine": OK_CA, "guadalajara-alliance-francaise-de-guadalajara": OK_CA,
            "puebla-alliance-francaise": OK_CA + [("part", "sur demande")], "pachuca-mineral-de-la-reforma-centre-pachuca-universite-autonome": OK_CA + [("part", "sur demande")],
            "aguascalientes-alliance-francaise": OK_CA + [("part", "dès 5 inscrits")],
            "guanajuato-alliance-francaise": NO_CA, "san-luis-potosi-alliance-francaise": NO_CA, "zacatecas-alliance-francaise": NO_CA,
            "guadalajara-proulex-universite-de-guadalajara": [("part", "tout public seulement")],
            "mexicali-alliance-francaise": [("part", "TCF absent du site")], "tepic-nayarit-colegio-de-ciencas-y-letras-de-tepic": [("part", "TCF absent du site")]},
    urls={"mexico-institut-francais-amerique-latine": "https://ifal.mx/certificaciones/tcfcanada",
          "guadalajara-proulex-universite-de-guadalajara": "http://cei.proulex.com/"},
))

PAGES.append(dict(
    slug="delf-mexique", exam="delf", file="delf_mexique", layout="regions", chip="Mexique",
    crumb="DELF au Mexique",
    pointer="",
    title="DELF au Mexique : {n} centres, calendrier et prix 2026",
    desc="DELF et DALF au Mexique : calendrier et tarifs nationaux fixés par l'IFAL, la session de novembre 2026 (inscriptions jusqu'au 23 octobre), B2 2 500 pesos.",
    h1="DELF et DALF au Mexique : les {n} centres, le calendrier et les prix 2026",
    intro="""Au Mexique, le DELF et le DALF ont un calendrier et des tarifs <strong>nationaux</strong>, fixés chaque année
par l'IFAL (Institut français d'Amérique latine) et appliqués par les {n} centres d'examen — Alliances françaises,
universités, écoles. Prochaine session tout public : écrits du <strong>9 au 13 novembre 2026</strong>, inscriptions du
<strong>5 au 23 octobre</strong>, résultats le 14 décembre. Le DELF B2 coûte <strong>2 500 pesos</strong> partout,
1 500 pour les étudiants des universités technologiques et des écoles normales de la SEP.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 8 octobre 2026) : une trentaine d'Alliances françaises, l'IFAL, des universités (UNAM, IPN, universités d'État et technologiques) et des écoles.",
           "Calendrier national : tout public en février, juin, septembre et <strong>novembre</strong> ; junior en mars, avril, mai et octobre ; Prim en juin.",
           "Session de novembre 2026 : inscriptions du <strong>5 au 23 octobre</strong>, écrits du 9 au 13 novembre (A1 et C2 le 9, A2 le 10, B1 le 11, B2 le 12, C1 le 13), résultats le <strong>14 décembre</strong>.",
           "Tarifs nationaux 2026 : <strong>A1 1 445 · A2 1 575 · B1 1 800 · B2 2 500 · C1 3 500 · C2 4 000 pesos</strong> ; tarifs réduits pour les universités technologiques et les écoles normales.",
           "Selon la Fédération des Alliances françaises, les diplômes DELF-DALF sont reconnus par la SEP à travers la norme CENNI.",
           "Ni remboursement ni transfert ; diplôme à retirer en personne, ou par un tiers muni d'une procuration simple."],
    stats=[("{n}", "centres d'examen", "liste FEI du 8 octobre 2026"), ("2 500", "pesos le DELF B2", "tarif national 2026"),
           ("23 oct.", "clôture des inscriptions", "session du 9 au 13 novembre"), ("14 déc.", "résultats", "de la session de novembre")],
    sections=[
        ("calendrier", "Le calendrier national 2026", table(
            "Calendrier des sessions DELF-DALF 2026 au Mexique (version 2 du document de l'IFAL), consulté le 8 octobre 2026. Les oraux s'étalent sur trois semaines autour des écrits.",
            ["Session", "Inscriptions", "Écrits", "Résultats"],
            [("Tout public, février", "5-31 janvier", "16-20 février", "13 mars"),
             ("Junior, mars", "26 janvier – 13 février", "2-5 mars", "13 avril"),
             ("Junior, avril", "16 février – 6 mars", "20-23 avril", "14 mai"),
             ("Junior et scolaire, mai", "17-30 avril", "18-21 mai", "26 juin"),
             ("Prim, juin", "27 avril – 15 mai", "1er-3 juin", "3 juillet"),
             ("Tout public, juin", "11-29 mai", "15-19 juin", "24 juillet"),
             ("Tout public, septembre", "10-28 août", "21-25 septembre", "23 octobre"),
             ("Junior et scolaire, octobre", "7-25 septembre", "12-15 octobre", "20 novembre"),
             ("<strong>Tout public, novembre</strong>", "<strong>5-23 octobre</strong>", "<strong>9-13 novembre</strong>", "<strong>14 décembre</strong>")], wide=False) + """
<p>« Ce calendrier est établi chaque année au niveau national par l'IFAL et s'applique dans tout le Mexique »,
écrit l'Alliance de Guadalajara ; « les dates et les tarifs ne peuvent pas être modifiés », ajoute celle de San Luis
Potosí. Tous les centres n'ouvrent pas toutes les sessions — l'IFAL, lui, les ouvre toutes ; à l'ENALLT-UNAM, la
session de novembre ne propose que le B1, le B2 et le C1. Le calendrier 2027 n'était pas publié le 8 octobre
2026.</p>"""),
        ("prix", "Combien coûte le DELF au Mexique ?", table(
            "Grille nationale « Tarifs 2026 – Mexique », en pesos, reprise par l'IFAL, les Alliances de Mexico, Guadalajara, Aguascalientes et Puebla, l'ENALLT-UNAM et l'UAEH, consultée le 8 octobre 2026.",
            ["Examen", "Tarif standard", "Universités technologiques et écoles normales", "DELF scolaire"],
            [("DELF Prim A1.1", "1 325", "—", "—"), ("DELF A1", "1 445", "1 012", "340"), ("DELF A2", "1 575", "1 103", "450"),
             ("DELF B1", "1 800", "1 080", "570"), ("<strong>DELF B2</strong>", "<strong>2 500</strong>", "1 500", "685"),
             ("DALF C1", "3 500", "—", "—"), ("DALF C2", "4 000", "—", "—")]) + """
<p>Le DELF junior et le Prim coûtent le même prix que le tout public, niveau par niveau. Le tarif scolaire vaut pour
les élèves des établissements sous convention avec l'ambassade ; certains centres réservent des sessions aux
étudiants des universités technologiques et des écoles normales. Réédition ou duplicata du diplôme : 900 pesos.</p>"""),
        ("inscription", "S'inscrire, résultats et diplôme", """<p>On s'inscrit <strong>au centre</strong>, pendant la période fixée par le calendrier national : ni paiement ni
dossier ne sont acceptés après le dernier jour. À l'IFAL : formulaire, virement ou dépôt bancaire, documents par
e-mail. À l'Alliance française de Mexico (San Ángel, Del Valle, Polanco, Interlomas) : formulaire à demander à
l'accueil, paiement au centre — jamais dans une autre Alliance que celle de l'examen —, puis formulaire et reçu par
e-mail. À Puebla : paiement dans la boutique en ligne, formulaire et règlement signé envoyés par e-mail,
confirmation sous quatre jours ouvrés. À l'ENALLT-UNAM : dossier papier au guichet et paiement à la caisse, avec une
copie de l'INE.</p>

<p>Le jour J : la convocation imprimée et une pièce d'identité officielle avec photo — aucune version numérique
n'est acceptée. Ni remboursement ni transfert, sauf annulation de la session par le centre. Les résultats sont
publiés à la date nationale (le 14 décembre 2026 pour novembre), souvent sous forme de liste des numéros de
candidats admis, et jamais par téléphone ; l'attestation de réussite vaut jusqu'à la remise du diplôme, qui se retire
en personne ou par un tiers muni d'une procuration simple.</p>"""),
    ],
    list_title="Les {n} centres d'examen, État par État",
    toc_regions=6,
    region_sort="count",
    faq=[("Quand a lieu la prochaine session du DELF au Mexique ?", "Du 9 au 13 novembre 2026 pour le tout public : A1 et C2 le 9, A2 le 10, B1 le 11, B2 le 12, C1 le 13. Les inscriptions sont ouvertes du 5 au 23 octobre 2026 dans les centres qui ouvrent la session, et les résultats sont publiés le 14 décembre 2026."),
         ("Combien coûte le DELF B2 au Mexique ?", "2 500 pesos, tarif national 2026 appliqué par tous les centres ; 1 500 pesos pour les étudiants des universités technologiques et des écoles normales de la SEP. Le DALF coûte 3 500 pesos (C1) et 4 000 pesos (C2)."),
         ("Où passer le DELF à Mexico ?", "À l'IFAL (Río Nazas 43), qui ouvre toutes les sessions nationales ; dans les quatre centres de l'Alliance française de Mexico (San Ángel, Del Valle, Polanco, Interlomas) ; à l'ENALLT-UNAM (B1, B2 et C1 en novembre) ; ou dans d'autres établissements de l'UNAM et de l'IPN. Les dates et les prix sont les mêmes partout."),
         ("Le DELF est-il reconnu au Mexique ?", "La Fédération des Alliances françaises du Mexique indique que les diplômes DELF et DALF sont reconnus par la SEP à travers la norme CENNI, ainsi que par des entreprises et des chambres de commerce. Le diplôme est le même qu'en France, et valable à vie."),
         ("Peut-on se faire rembourser son inscription au DELF ?", "Non : les fiches d'inscription officielles excluent tout remboursement ou transfert, sauf annulation de la session par le centre. Inscrivez-vous seulement si vous pouvez passer l'examen aux dates prévues.")],
    also=[("/centres/tcf-mexique/", "TCF Canada au Mexique", "Cinq centres, de 4 800 à 6 500 pesos."),
          ("/centres/delf-colombie/", "DELF et DALF en Colombie", "Un calendrier et une grille nationaux, B2 à 490 000 pesos."), A_DELF, A_DIPL],
    sources="calendrier des sessions 2026 et grille « Tarifs 2026 – Mexique » de l'IFAL (publiés par les Alliances françaises), sites de l'IFAL, de la Fédération des Alliances françaises du Mexique, des Alliances de Mexico, Guadalajara, Puebla, Monterrey, Aguascalientes et San Luis Potosí, de l'ENALLT-UNAM et de l'UAEH (fiches d'inscription 2026), consultés le 8 octobre 2026.",
    org_url="https://ifal.mx/certificaciones",
    urls={"mexico-institut-francais-d-amerique-latine-ifal": "https://ifal.mx/certificaciones"},
))

# ===========================================================================
# COLOMBIE — le domaine alianzafrancesa.org.co de la liste FEI est mort : sites en <ville>.alianzafrancesa.edu.co
# ===========================================================================
CO = "https://%s.alianzafrancesa.edu.co/"
PAGES.append(dict(
    slug="tcf-colombie", exam="tcf", file="tcf_colombie", layout="cities", chip="Colombie",
    crumb="TCF en Colombie",
    pointer="Les 7 Alliances françaises agréées proposent le TCF Canada, de 1 050 000 à 1 247 000 pesos ; une session par mois à Pereira.",
    title="TCF Canada en Colombie : 7 Alliances, prix et dates",
    desc="TCF Canada en Colombie : les 7 Alliances françaises agréées le proposent, de 1 050 000 à 1 247 000 pesos. Dates à Medellín, Pereira, Bogotá et inscription.",
    h1="TCF Canada en Colombie : les 7 centres agréés, leurs prix et leurs dates",
    intro="""En Colombie, le TCF se passe dans les <strong>sept Alliances françaises</strong> agréées par France Éducation
international — Bogotá, Medellín, Cali, Barranquilla, Carthagène, Manizales, Pereira —, et <strong>toutes proposent le
TCF Canada</strong>, de <strong>1 050 000 pesos</strong> à Medellín et Pereira à <strong>1 247 000</strong> à Bogotá. Les
rythmes diffèrent : une session par mois à Pereira, à la demande à Cali, quatre ou cinq par an ailleurs. Prochaines
dates relevées le 8 octobre 2026 : Medellín le 23 octobre, Pereira du 27 au 29 octobre, Barranquilla début
décembre, Bogotá le 10 décembre.""",
    facts=["<strong>{n} centres agréés</strong> (liste FEI du 8 octobre 2026), tous des Alliances françaises : <strong>tous proposent le TCF Canada</strong>, le TCF Québec et le tout public ; aucun ne mentionne le TCF IRN.",
           "Prix 2026 du TCF Canada : <strong>1 050 000 pesos</strong> à Medellín et Pereira, 1 080 000 à Manizales, 1 199 000 à Barranquilla, <strong>1 247 000</strong> à Bogotá.",
           "Prochaines dates : Medellín <strong>23 octobre</strong> (inscriptions jusqu'au 14) et 2 décembre ; Pereira <strong>27-29 octobre</strong>, 24-26 novembre, 9-10 décembre ; Barranquilla 1er-3 décembre ; Bogotá <strong>10 décembre</strong> (inscriptions du 27 octobre au 19 novembre).",
           "<strong>Cali</strong> fait passer le TCF à la demande : « preséntalo cuando quieras ».",
           "Pas de remboursement après l'inscription (Cali, Carthagène, Medellín, Pereira) ; un mois d'attente entre deux sessions à Medellín.",
           "Résultats en 10 jours ouvrés selon le réseau des Alliances, jusqu'à cinq semaines selon Medellín ; certificat numérique, valable deux ans."],
    stats=[("{n}", "Alliances agréées", "toutes avec le TCF Canada"), ("1 050 000", "pesos au minimum", "le TCF Canada à Medellín et Pereira"),
           ("23 oct.", "prochaine date", "Medellín ; Pereira le 27"), ("10 jours", "ouvrés pour les résultats", "selon le réseau des Alliances")],
    sections=[
        ("releve", "Le TCF Canada en Colombie, Alliance par Alliance", releve([
            ("Alliance française de Bogotá (sede Chicó)", "<strong>Canada</strong>, Québec, tout public (DAP)",
             "Canada <strong>1 247 000</strong> · Québec 424 000 par épreuve · tout public 835 000 + 267 000 par épreuve",
             "Canada : 30/04, 16/07, 01/10 et <strong>10/12/2026</strong> (inscriptions du 27/10 au 19/11) ; Québec le 25/11 (jusqu'au 17/10). Boutique en ligne."),
            ("Alliance française de Medellín (sede Centro)", "<strong>Canada</strong>, Québec, tout public (DAP)",
             "Canada <strong>1 050 000</strong> · Québec 280 000 à 345 000 par épreuve · tout public 650 000",
             "Canada <strong>23/10</strong> (inscriptions jusqu'au 14/10) et <strong>02/12</strong> (du 26/10 au 23/11). Formulaire, paiement, copie de la cédula ; sur ordinateur."),
            ("Alliance française de Cali", "<strong>Canada</strong>, Québec, tout public",
             "Canada <strong>1 138 800</strong> probablement — la page inverse ses colonnes, à confirmer · −10 % pour les élèves",
             "<strong>À la demande</strong> ; pré-inscription sur la plateforme Q10 de l'Alliance, puis paiement."),
            ("Alliance française de Barranquilla", "<strong>Canada</strong>, Québec, tout public (DAP)",
             "Canada <strong>1 199 000</strong> · Québec 316 000 à 343 000 par épreuve · tout public 605 000",
             "Quatre sessions en 2026 : <strong>1er-3 décembre</strong> (inscriptions du 19/10 au 13/11). Pré-inscription sur Q10."),
            ("Alliance française de Carthagène des Indes", "<strong>Canada</strong>, Québec, tout public",
             "325 000 affichés pour le TCF Canada : montant anormal, à confirmer · Québec 382 000 par épreuve · tout public 576 000",
             "Dates publiées jusqu'en juin 2026 seulement ; inscription au TCF Canada par WhatsApp."),
            ("Alliance française de Manizales", "<strong>Canada</strong>, Québec, tout public",
             "Canada <strong>1 080 000</strong> (tableau titré 2025) · Québec 390 000 à 410 000 par épreuve · tout public complet 1 100 000",
             "Canada « entre le 5 et le 7 novembre », inscriptions du 1er au 24 octobre, sous un titre 2025 : à confirmer."),
            ("Alliance française de Pereira", "<strong>Canada</strong>, Québec, tout public (DAP)", "Canada <strong>1 050 000</strong>",
             "<strong>Chaque mois</strong> : 27-29/10 (inscriptions du 1er au 15/10), 24-26/11 (du 1er au 15/11), 09-10/12 (du 1er au 7/12). Formulaire en ligne, photo numérique, paiement."),
        ], caption="Ce que le site de chaque Alliance affichait le 8 octobre 2026, prix en pesos colombiens. « À confirmer » : montant ou date incohérents sur le site — l'Alliance fait foi.")),
        ("inscription", "S'inscrire au TCF Canada en Colombie", """<p>Chaque Alliance a sa porte d'entrée : boutique en ligne à Bogotá et Pereira, plateforme Q10 à Cali et à
Barranquilla, formulaire PDF à Medellín, formulaire en ligne et paiement Davivienda à Manizales, WhatsApp à
Carthagène. Partout, l'inscription se termine par le paiement et l'envoi d'une copie de la pièce d'identité — pour
le TCF Canada, celle de votre dossier IRCC ; Pereira demande aussi une photo numérique de type passeport, et Medellín
prend une photo le jour du test. Les sites du réseau ont changé d'adresse : ils sont désormais en
<em>ville</em>.alianzafrancesa.edu.co, et non plus sur le domaine qu'indique la liste de FEI.</p>

<p>Une fois inscrit, pas de retour en arrière : Cali, Carthagène, Medellín et Pereira excluent tout remboursement, et
les dates ne se modifient pas. À Medellín, il faut attendre un mois entre deux sessions, et la réévaluation est
suspendue jusqu'en octobre 2027. Les résultats arrivent en « 10 días hábiles » selon la FAQ commune du réseau, en 20
jours ouvrés à cinq semaines selon Medellín ; le certificat est numérique et vaut deux ans. Et aucune attestation ne
s'achète : les sites qui vendent un certificat TCF « sans examen » sont des fraudes.</p>

<p>Pour le Québec, l'Alliance de Bogotá a une convention avec le ministère de l'Immigration québécois : sous
conditions, les cours de français peuvent être remboursés par le programme d'apprentissage du français du Québec.</p>"""),
    ],
    list_title="Les {n} centres TCF agréés, ville par ville",
    faq=[("Où passer le TCF Canada à Bogotá ?", "À l'Alliance française de Bogotá, sede Chicó (carrera 11 # 93-40) : 1 247 000 pesos, prochaine session le 10 décembre 2026, avec des inscriptions du 27 octobre au 19 novembre dans la boutique en ligne de l'Alliance. Relevé le 8 octobre 2026."),
         ("Combien coûte le TCF Canada en Colombie ?", "De 1 050 000 pesos (Medellín, Pereira) à 1 247 000 pesos (Bogotá) : 1 080 000 à Manizales et 1 199 000 à Barranquilla. À Cali, le prix externe est probablement de 1 138 800 pesos — la page inverse ses colonnes —, et le montant affiché à Carthagène (325 000) est à confirmer auprès de l'Alliance."),
         ("Où passer le TCF Canada le plus vite en Colombie ?", "À Pereira, qui organise une session chaque mois (27-29 octobre, 24-26 novembre, 9-10 décembre 2026, inscriptions du 1er au 15 du mois), ou à Cali, qui le fait passer à la demande. Medellín a une date le 23 octobre, inscriptions jusqu'au 14."),
         ("Peut-on se faire rembourser son TCF ?", "Non : Cali, Carthagène, Medellín et Pereira excluent tout remboursement après l'inscription, et les dates ne se modifient pas. Ne vous inscrivez qu'une fois la date arrêtée."),
         ("Le TCF Canada passé en Colombie est-il accepté par IRCC ?", "Oui : l'attestation est délivrée par France Éducation international quel que soit le centre agréé, et vaut deux ans. Choisissez bien le TCF Canada, pas le tout public.")],
    also=[("/centres/delf-colombie/", "DELF et DALF en Colombie", "Le calendrier national et la grille commune, B2 à 490 000 pesos."),
          ("/centres/tcf-mexique/", "TCF Canada au Mexique", "Cinq centres, de 4 800 à 6 500 pesos."), A_TEF, A_NCLC],
    sources="sites des Alliances françaises de Bogotá, Medellín, Cali, Barranquilla, Carthagène des Indes, Manizales et Pereira (pages TCF, tarifs et calendriers 2026, boutiques, règlements des examens), consultés le 8 octobre 2026.",
    badges={"barranquilla-alliance-francaise": OK_CA, "bogota-alliance-francaise": OK_CA, "cali-alliance-francaise-de-cali": OK_CA + [("part", "à la demande")],
            "carthagene-des-indes-alliance-francaise": OK_CA, "manizales-alliance-francaise": OK_CA, "medellin-alliance-francaise": OK_CA,
            "pereira-alliance-francaise": OK_CA},
    urls={"barranquilla-alliance-francaise": CO % "barranquilla", "cali-alliance-francaise-de-cali": CO % "cali",
          "carthagene-des-indes-alliance-francaise": CO % "cartagena", "manizales-alliance-francaise": CO % "manizales",
          "pereira-alliance-francaise": CO % "pereira"},
))

PAGES.append(dict(
    slug="delf-colombie", exam="delf", file="delf_colombie", layout="cities", chip="Colombie",
    crumb="DELF en Colombie",
    pointer="",
    title="DELF en Colombie : {n} Alliances, calendrier et prix 2026",
    desc="DELF et DALF en Colombie : le calendrier national (mars, juin, août, novembre 2026), une grille commune (B2 490 000 pesos), les 15 Alliances agréées.",
    h1="DELF et DALF en Colombie : les {n} centres, le calendrier et les prix 2026",
    intro="""En Colombie, le DELF et le DALF se passent dans les {n} sites des Alliances françaises agréés par France
Éducation international, de Bogotá à Valledupar, avec un <strong>calendrier et une grille communs</strong> au réseau.
Quatre sessions tout public en 2026 — mars, juin, août, novembre — ; celle de <strong>novembre</strong> (écrits du 3 au
6, oraux du 9 au 13) fermait ses inscriptions le <strong>9 octobre</strong>. Le DELF B2 coûte <strong>490 000
pesos</strong> ; les élèves des Alliances ont 10 à 20 % de remise.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 8 octobre 2026), tous des Alliances françaises — dont trois sites à Bogotá ; gestion centrale à l'Alliance de Bogotá.",
           "Calendrier national 2026 : tout public en mars, juin, août et <strong>novembre</strong> ; junior en avril et octobre (et mai dans certains centres) ; Prim en mai et septembre.",
           "Novembre 2026 : A1 et A2 le 3, B1 le 4, B2 le 5, C1 et C2 le 6 ; inscriptions du 14 septembre au <strong>9 octobre</strong>.",
           "Grille commune 2026 : <strong>A1 248 000 · A2 263 000 · B1 383 000 · B2 490 000 · C1 591 000 · C2 643 000 pesos</strong>, junior et Prim au même prix.",
           "Pas de remboursement ; un report, une seule fois, sur certificat médical. Résultats trente jours ouvrés après les oraux à Bogotá.",
           "Le diplôme, imprimé en France, arrive en Colombie <strong>cinq à six mois</strong> après la session."],
    stats=[("{n}", "centres d'examen", "liste FEI du 8 octobre 2026"), ("490 000", "pesos le DELF B2", "grille commune 2026"),
           ("3-6 nov.", "session tout public", "inscriptions jusqu'au 9 octobre"), ("5-6 mois", "pour le diplôme", "imprimé en France")],
    sections=[
        ("calendrier", "Le calendrier national 2026", table(
            "Calendrier DELF-DALF tout public 2026 publié par les Alliances de Bogotá, Barranquilla, Bucaramanga, Cali, Carthagène, Manizales, Medellín et Pereira, consulté le 8 octobre 2026 (oraux : dates de Bogotá).",
            ["Session", "Inscriptions", "A1", "A2", "B1", "B2", "C1", "C2", "Oraux"],
            [("Mars", "19/01 – 16/02", "17/03", "17/03", "18/03", "19/03", "20/03", "20/03", "24-27/03"),
             ("Juin", "27/04 – 23/05", "16/06", "16/06", "17/06", "18/06", "19/06", "19/06", "22-26/06"),
             ("Août", "22/06 – 18/07", "11/08", "11/08", "12/08", "13/08", "14/08", "14/08", "18-21/08"),
             ("<strong>Novembre</strong>", "<strong>14/09 – 09/10</strong>", "03/11", "03/11", "04/11", "05/11", "06/11", "06/11", "09-13/11")]) + """
<p>DELF junior : avril et octobre 2026 (13 au 16 octobre, inscriptions closes le 15 septembre), plus une session en
mai à Cali, Manizales et Barranquilla ; DELF Prim : mai et septembre. Pereira a ajouté une session extraordinaire en
septembre. Aucun calendrier 2027 n'était publié le 8 octobre 2026. Les sites d'Armenia, Cúcuta, Popayán, Santa
Marta et Valledupar affichaient encore des calendriers de 2024 ou 2025 : renseignez-vous directement auprès
d'eux.</p>"""),
        ("prix", "Combien coûte le DELF en Colombie ?", table(
            "Grille 2026 commune aux Alliances de Bogotá, Barranquilla, Bucaramanga, Cali, Carthagène, Manizales, Medellín et Pereira, en pesos colombiens, consultée le 8 octobre 2026.",
            ["Niveau", "Tarif public", "Élèves des Alliances (−10 %)"],
            [("DELF A1 (et Prim A1.1)", "248 000", "223 200"), ("DELF A2", "263 000", "236 700"), ("DELF B1", "383 000", "344 700"),
             ("<strong>DELF B2</strong>", "<strong>490 000</strong>", "441 000"), ("DALF C1", "591 000", "531 900"), ("DALF C2", "643 000", "578 700")], wide=False) + """
<p>La remise des élèves est de 10 % dans la plupart des Alliances (Barranquilla, Pereira, Medellín), de 20 % à Cali.
Bogotá et Medellín vendent aussi des combinés de deux niveaux — B1 + B2 : 785 700 pesos à Bogotá.</p>"""),
        ("inscription", "S'inscrire, résultats et diplôme", """<p>On s'inscrit auprès de l'Alliance, pendant la fenêtre de la session — « aucune inscription n'est
acceptée hors de ces dates », prévient Bogotá : boutique en ligne à Bogotá, plateforme Q10 à Cali et à Barranquilla,
formulaire en ligne à Bucaramanga et à Pereira, dossier par e-mail à Medellín (formulaire, reçu, pièce d'identité,
règlement signé). Pièces acceptées le jour J : cédula de ciudadanía ou de extranjería, tarjeta de identidad ou
passeport en cours de validité.</p>

<p>Pas de remboursement ; un report, une seule fois, sur certificat médical — à justifier sous sept jours à Medellín.
À Bogotá, les résultats sont publiés trente jours ouvrés après les derniers oraux, en ligne avec le code candidat,
jamais par e-mail ni par téléphone ; Medellín annonce ceux de novembre « à partir du 14 décembre environ ». Le
diplôme, imprimé en France, arrive en Colombie cinq à six mois après la session.</p>

<p>Les Alliances présentent le DELF comme un moyen de faire valider le niveau de langue que demandent les
universités colombiennes — vérifiez auprès de la vôtre ce qu'elle accepte.</p>"""),
    ],
    list_title="Les {n} centres d'examen, ville par ville",
    faq=[("Quand a lieu la prochaine session du DELF en Colombie ?", "La session de novembre 2026 a lieu du 3 au 6 novembre pour les écrits (A1 et A2 le 3, B1 le 4, B2 le 5, C1 et C2 le 6) et du 9 au 13 novembre pour les oraux ; ses inscriptions fermaient le 9 octobre 2026. Le calendrier 2027 n'était pas publié le 8 octobre 2026."),
         ("Combien coûte le DELF B2 en Colombie ?", "490 000 pesos selon la grille 2026 commune aux Alliances françaises ; 441 000 pesos pour leurs élèves à Barranquilla et à Pereira (−10 %), 392 000 à Cali (−20 %). Le DALF coûte 591 000 pesos (C1) et 643 000 pesos (C2)."),
         ("Où passer le DELF à Bogotá ?", "Dans l'un des trois sites de l'Alliance française de Bogotá — Chicó, Centro, Cedritos —, qui gère aussi le DELF pour tout le pays. L'inscription se fait dans la boutique en ligne de l'Alliance, pendant la fenêtre de chaque session."),
         ("Peut-on se faire rembourser son inscription au DELF ?", "Non : les règlements de Bogotá, Medellín et Pereira excluent tout remboursement. Un report est possible une seule fois, pour maladie, sur certificat médical."),
         ("Quand arrive le diplôme du DELF en Colombie ?", "Les résultats sont publiés environ six semaines après la session ; le diplôme, imprimé en France, arrive en Colombie cinq à six mois après, selon la FAQ commune des Alliances. L'attestation de réussite se retire au centre avec une pièce d'identité.")],
    also=[("/centres/tcf-colombie/", "TCF Canada en Colombie", "Les sept Alliances, de 1 050 000 à 1 247 000 pesos."),
          ("/centres/delf-mexique/", "DELF et DALF au Mexique", "Le calendrier et la grille nationaux, B2 à 2 500 pesos."), A_DELF, A_DIPL],
    sources="sites des Alliances françaises de Bogotá, Medellín, Cali, Barranquilla, Carthagène des Indes, Manizales, Pereira, Bucaramanga, Armenia, Cúcuta, Popayán, Santa Marta et Valledupar (calendriers et tarifs DELF-DALF 2026, règlements des examens, FAQ), consultés le 8 octobre 2026.",
    org_url="https://bogota.alianzafrancesa.edu.co/",
    notes={"armenia-alliance-francaise-d-armenia": "Calendrier en ligne de 2025 le 8 octobre 2026 : renseignez-vous auprès de l'Alliance.",
           "cucuta-alliance-francaise-de-cucuta": "Calendrier en ligne de 2024 le 8 octobre 2026.",
           "popayan-alliance-francaise-de-popayan": "Calendrier en ligne de 2024 le 8 octobre 2026.",
           "santa-marta-alliance-francaise-de-santa-marta": "Calendrier en ligne de 2024 le 8 octobre 2026.",
           "valledupar-alliance-francaise-de-valledupar": "Calendrier en ligne de 2024 le 8 octobre 2026."},
    urls={"armenia-alliance-francaise-d-armenia": CO % "armenia",
          "bogota-alliance-francaise-de-bogota-cedritos": CO % "bogota", "bogota-alliance-francaise-de-bogota-centro": CO % "bogota",
          "bogota-alliance-francaise-de-bogota-chico": CO % "bogota", "bucaramanga-alliance-francaise-de-bucaramanga": CO % "bucaramanga",
          "cali-alliance-francaise-cali": CO % "cali", "carthagene-des-indes-alliance-francaise-de-carthagene": CO % "cartagena",
          "manizales-alliance-francaise-de-manizales": CO % "manizales", "pereira-alliance-francaise-de-pereira": CO % "pereira",
          "popayan-alliance-francaise-de-popayan": CO % "popayan", "santa-marta-alliance-francaise-de-santa-marta": CO % "santa-marta",
          "valledupar-alliance-francaise-de-valledupar": CO % "valledupar"},
))

# ===========================================================================
# ARGENTINE
# ===========================================================================
PAGES.append(dict(
    slug="tcf-argentine", exam="tcf", file="tcf_argentine", layout="cities", chip="Argentine",
    crumb="TCF en Argentine",
    pointer="Campus France à Buenos Aires et les Alliances de Córdoba et Rosario annoncent le TCF Canada ; aucun prix publié.",
    title="TCF Canada en Argentine : les centres et l'inscription",
    desc="TCF Canada en Argentine : Campus France à Buenos Aires (sessions mensuelles), les Alliances de Córdoba et Rosario, l'inscription — et aucun prix publié.",
    h1="TCF Canada en Argentine : les {n} centres agréés et l'inscription",
    intro="""En Argentine, {n} centres sont agréés pour le TCF par France Éducation international, et quatre annoncent le
TCF Canada : <strong>Campus France</strong> (Institut français) à Buenos Aires, qui ouvre des sessions tous les mois,
les <strong>Alliances françaises de Córdoba</strong> (à la demande, du lundi au vendredi) et de <strong>Rosario</strong>,
et un centre privé de Buenos Aires dont les seules dates publiées datent de 2025. Particularité du pays :
<strong>aucun centre ne publie le prix du TCF Canada</strong> — il faut le demander. L'Alliance de Buenos Aires, elle,
fait passer le TEF, pas le TCF.""",
    facts=["<strong>{n} centres agréés</strong> (liste FEI du 8 octobre 2026) ; <strong>4 annoncent le TCF Canada</strong> : Campus France (Buenos Aires), les Alliances de Córdoba et de Rosario, le Centro educativo canadiense (Buenos Aires).",
           "Le site de l'Alliance de Mendoza ne mentionne pas le TCF ; l'Alliance de Buenos Aires propose le TEF Canada, pas le TCF.",
           "<strong>Aucun prix publié</strong> pour le TCF Canada ; seul tarif TCF affiché dans le pays : le TCF DAP de Campus France, 74 €, payable en pesos.",
           "Campus France : sessions <strong>tous les mois</strong>, date fixée par e-mail, sur ordinateur ; Córdoba : <strong>à la demande</strong>, du lundi au vendredi.",
           "Inscription par e-mail (formulaire en ligne à Córdoba) ; chez Campus France, l'inscription n'est officielle qu'à réception du paiement.",
           "Résultats en <strong>15 jours ouvrables</strong> (Campus France, Córdoba), attestation électronique valable deux ans."],
    stats=[("4", "centres TCF Canada", "sur {n} centres agréés"), ("0", "prix publié", "à demander au centre"),
           ("tous les mois", "chez Campus France", "date fixée par e-mail"), ("15 jours", "ouvrables pour les résultats", "attestation électronique")],
    sections=[
        ("releve", "Le TCF Canada en Argentine, centre par centre", releve([
            ("Campus France — Institut français (Buenos Aires)", "<strong>Canada</strong>, IRN, tout public, Québec, DAP",
             "non publié (« consultar costos ») · DAP 74 €", "Sessions tous les mois, date convenue par e-mail ; DAP en une session, début décembre 2026. Sur ordinateur, dans l'immeuble du consulat (Basavilbaso 1253)."),
            ("Alliance française de Córdoba", "<strong>Canada</strong>, tout public", "non publié",
             "<strong>À la demande</strong>, du lundi au vendredi : formulaire en ligne, puis confirmation de la date ; inscription complète au moins une semaine avant. Sur ordinateur."),
            ("Alliance française de Rosario", "<strong>Canada</strong>, Québec, IRN, tout public", "non publié", "Aucune date publiée : écrire à l'Alliance (pedagogie@afrosario.org.ar)."),
            ("Centro educativo canadiense (Buenos Aires)", "<strong>Canada</strong>, Québec, IRN, tout public", "« contáctenos »",
             "Site rebaptisé « Centro Educativo ComunicAR » ; seules des dates de 2025 publiées (environ tous les deux mois). Inscription par e-mail."),
            ("Alliance française de Mendoza", "aucun TCF sur son site", "—", "Le site ne présente que le DELF-DALF : à confirmer auprès de l'Alliance."),
        ])),
        ("inscription", "S'inscrire au TCF Canada en Argentine", """<p>Partout, on commence par <strong>écrire au centre</strong> pour fixer une date et connaître le prix. Chez
Campus France (buenosaires@campusfrance.org), on envoie son état civil et son numéro de DNI ; le paiement se fait par
virement, en euros ou en pesos au taux de la chancellerie, et l'inscription n'est officielle qu'à réception du
justificatif. À Córdoba, un formulaire en ligne demande les jours et créneaux souhaités, puis l'Alliance confirme la
date ; l'inscription doit être complète au moins une semaine avant. Pour le TCF Canada, utilisez la pièce d'identité
de votre dossier IRCC.</p>

<p>Les résultats arrivent en quinze jours ouvrables, en attestation électronique valable deux ans ; Campus France
reçoit l'original papier environ un mois après. Aucun centre ne publie de règle d'annulation ou de remboursement :
posez la question avant de payer. Le <a href="/tef-canada/">TEF Canada</a>, l'autre test accepté par IRCC, se passe à
l'Alliance française de Buenos Aires.</p>"""),
    ],
    list_title="Les {n} centres TCF agréés, ville par ville",
    faq=[("Où passer le TCF Canada à Buenos Aires ?", "Chez Campus France, à l'Institut français (Basavilbaso 1253, dans l'immeuble du consulat), qui ouvre des sessions tous les mois — la date se fixe par e-mail — ; ou au Centro educativo canadiense, dont les seules dates publiées datent de 2025. L'Alliance française de Buenos Aires ne fait pas passer le TCF, mais le TEF Canada."),
         ("Combien coûte le TCF Canada en Argentine ?", "Aucun des cinq centres agréés ne publiait le prix le 8 octobre 2026 : il faut le demander. Le seul tarif TCF affiché dans le pays est celui du TCF DAP de Campus France, 74 €, payable en pesos."),
         ("Peut-on passer le TCF Canada à Córdoba ?", "Oui, à l'Alliance française de Córdoba, à la demande, du lundi au vendredi : on remplit le formulaire en ligne, l'Alliance confirme la date, et l'inscription doit être complète au moins une semaine avant. Résultats en quinze jours ouvrables environ."),
         ("Combien de temps pour les résultats ?", "Quinze jours ouvrables selon Campus France et l'Alliance de Córdoba, en attestation électronique valable deux ans."),
         ("Le TCF Canada passé en Argentine est-il accepté par IRCC ?", "Oui : l'attestation est délivrée par France Éducation international quel que soit le centre agréé, et vaut deux ans.")],
    also=[("/centres/delf-argentine/", "DELF et DALF en Argentine", "Le calendrier national et la grille de fin 2026."),
          ("/centres/tcf-chili/", "TCF Canada au Chili", "Deux centres, 299 000 pesos chiliens."), A_TEF, A_NCLC],
    sources="sites de Campus France Argentine et de l'Institut français d'Argentine, des Alliances françaises de Córdoba, Rosario, Mendoza et Buenos Aires, et du Centro educativo canadiense (pages TCF, formulaires, règlements), consultés le 8 octobre 2026.",
    badges={"buenos-aires-institut-francais-campus-france": OK_CA, "cordoba-alliance-francaise": OK_CA + [("part", "à la demande")],
            "rosario-alliance-francaise-de-rosario": OK_CA, "buenos-aires-centro-educativo-canadiense": OK_CA + [("part", "dates 2025 seulement")],
            "mendoza-alliance-francaise-de-mendoza-marc-blancpain": [("part", "TCF absent du site")]},
))

PAGES.append(dict(
    slug="delf-argentine", exam="delf", file="delf_argentine", layout="regions", chip="Argentine",
    crumb="DELF en Argentine",
    pointer="",
    title="DELF en Argentine : {n} Alliances, calendrier et prix",
    desc="DELF et DALF en Argentine : la session des 4 et 5 décembre 2026 (inscriptions jusqu'au 5 novembre), les prix en euros et en pesos, les 28 Alliances.",
    h1="DELF et DALF en Argentine : les {n} centres, le calendrier et les prix",
    intro="""En Argentine, le DELF et le DALF ne se passent que dans les <strong>Alliances françaises</strong> — {n} centres
d'examen, sous la gestion centrale de l'Alliance française de Buenos Aires. Trois sessions tout public par an ; la
prochaine a lieu les <strong>4 et 5 décembre 2026</strong>, avec des inscriptions jusqu'au <strong>5 novembre</strong>
au niveau national (plus tôt ou plus tard selon l'Alliance). Les prix sont fixés en euros et payés en pesos : le
DELF B2 coûte 163 € pour un candidat libre, soit <strong>295 030 pesos</strong> pour la session de décembre.""",
    facts=["<strong>{n} centres d'examen</strong> (liste FEI du 8 octobre 2026), exclusivement des Alliances françaises ; gestion centrale à l'Alliance de Buenos Aires.",
           "Tout public : avril, juin-juillet et <strong>4-5 décembre 2026</strong> (A1, A2, B1 le 4 ; B2, C1, C2 le 5), inscriptions jusqu'au <strong>5 novembre</strong>.",
           "Prix de la session de décembre (candidat libre) : <strong>A1-A2 125 € · B1-B2 163 € · C1 246 € · C2 277 €</strong>, soit 226 250 à 501 370 pesos.",
           "Élèves des Alliances : <strong>50 % de remise</strong> ; collèges affiliés : tarif réduit.",
           "Absence : certificat médical sous une semaine, et le droit ne vaut que pour la session suivante.",
           "Résultats en ligne environ cinq semaines après ; diplôme, envoyé de France, quatre à six mois après."],
    stats=[("{n}", "Alliances françaises", "liste FEI du 8 octobre 2026"), ("295 030", "pesos le DELF B2", "163 € pour un candidat libre"),
           ("4-5 déc.", "prochaine session", "inscriptions jusqu'au 5 novembre"), ("−50 %", "pour les élèves AF", "sur tous les niveaux")],
    sections=[
        ("calendrier", "Le calendrier national 2026", table(
            "Calendrier DELF-DALF 2026 de l'Alliance française de Buenos Aires (gestion centrale), consulté le 8 octobre 2026.",
            ["Session", "Niveaux", "Inscriptions", "Épreuves"],
            [("Avril, tout public", "A1, A2, B1 · B2, C1, C2", "4-23 mars", "24 · 25 avril"),
             ("Juin, tout public et junior", "A1, A2, B1 · B2, C1, C2", "28 avril – 20 mai", "26 · 27 juin"),
             ("Octobre, Prim", "A1.1, A1, A2", "10 août – 10 septembre", "9 octobre"),
             ("Novembre, junior", "A2, B1 · A1, B2", "1er-30 septembre", "27 · 28 novembre"),
             ("<strong>Décembre, tout public</strong>", "A1, A2, B1 · B2, C1, C2", "<strong>1er septembre – 5 novembre</strong>", "<strong>4 · 5 décembre</strong>")], wide=False) + """
<p>Les clôtures locales diffèrent : 2 novembre à Córdoba, 15 novembre à Mar del Plata pour les adultes. Rosario et
Mendoza vendent la session de décembre en ligne ; Santa Fe et Mendoza ajoutent une série junior les 2 et 3 décembre.
Aucun calendrier 2027 n'était publié le 8 octobre 2026.</p>"""),
        ("prix", "Combien coûte le DELF en Argentine ?", table(
            "Grille de la session novembre-décembre 2026 publiée par l'Alliance de Mar del Plata ; mêmes montants en pesos à Córdoba, Mendoza et Rosario, consultés le 8 octobre 2026.",
            ["Diplôme", "Candidat libre", "Collèges affiliés", "Élèves des Alliances"],
            [("DELF A1 · A2", "125 € — 226 250 $", "88 € — 159 280 $", "63 € — 114 030 $"),
             ("DELF B1 · <strong>B2</strong>", "<strong>163 € — 295 030 $</strong>", "114 € — 206 340 $", "82 € — 148 420 $"),
             ("DALF C1", "246 € — 445 260 $", "172 € — 311 320 $", "124 € — 224 440 $"),
             ("DALF C2", "277 € — 501 370 $", "195 € — 352 950 $", "140 € — 253 400 $")]) + """
<p>« Les montants de base sont fixés en euros, mais le paiement se fait en pesos » : la somme en pesos change à chaque
session. L'Alliance de Buenos Aires ne publie la sienne qu'au moment des inscriptions. Le DELF junior coûte le prix
du tout public à Córdoba et à Mendoza.</p>"""),
        ("inscription", "S'inscrire, résultats et diplôme", """<p>On s'inscrit dans une Alliance, dans les délais fixés par la gestion centrale : en ligne dans le
« kiosque » de Córdoba, Rosario et Mendoza (carte de débit ou de crédit), par e-mail, WhatsApp ou sur place à Mar del
Plata, auprès du service des inscriptions à Buenos Aires. Si vous avez déjà passé un DELF, indiquez votre numéro de
candidat. Le jour J, une pièce d'identité valide ; un retardataire n'est plus admis une fois la compréhension orale
commencée.</p>

<p>En cas d'absence, seul un certificat médical remis sous une semaine conserve le droit d'examen, et pour la session
suivante seulement ; Córdoba ne rembourse jamais, mais crédite la somme un an sur ses cours. Les résultats (admis ou
non) sont publiés sur le site de l'Alliance de Buenos Aires — environ cinq semaines après la session de juin 2026 ; le
diplôme, envoyé de France, arrive quatre à six mois après.</p>"""),
    ],
    list_title="Les {n} centres d'examen, province par province",
    toc_regions=6,
    region_sort="count",
    faq=[("Quand a lieu la prochaine session du DELF en Argentine ?", "Les 4 et 5 décembre 2026 pour le tout public (A1, A2 et B1 le 4 ; B2, C1 et C2 le 5), avec des inscriptions jusqu'au 5 novembre au niveau national — le 2 novembre à Córdoba, le 15 à Mar del Plata. Le calendrier 2027 n'était pas publié le 8 octobre 2026."),
         ("Combien coûte le DELF B2 en Argentine ?", "163 € pour un candidat libre, payés en pesos : 295 030 pesos pour la session de décembre 2026 à Córdoba, Rosario, Mendoza et Mar del Plata. Les élèves des Alliances paient moitié prix (148 420 pesos)."),
         ("Où passer le DELF à Buenos Aires ?", "À l'Alliance française de Buenos Aires (avenida Córdoba 946), gestion centrale du DELF en Argentine : seules les Alliances françaises sont centres d'examen dans le pays."),
         ("Que se passe-t-il en cas d'absence ?", "Il faut remettre un certificat médical au plus tard une semaine après l'examen : le droit est alors conservé pour la session suivante seulement, et la réinscription n'est pas automatique. Sinon, le droit est perdu."),
         ("Quand arrive le diplôme ?", "Les résultats sont publiés sur le site de l'Alliance française de Buenos Aires, environ cinq semaines après la session ; le diplôme, envoyé de France, arrive quatre à six mois après.")],
    also=[("/centres/tcf-argentine/", "TCF Canada en Argentine", "Campus France, Córdoba, Rosario : sur demande."),
          ("/centres/delf-chili/", "DELF et DALF au Chili", "Le calendrier national 2026 et la session B2 de décembre."), A_DELF, A_DIPL],
    sources="sites de l'Alliance française de Buenos Aires (pages examens et DELF-DALF, calendrier 2026, règlements), des Alliances de Córdoba, Rosario, Mendoza, Mar del Plata, Santa Fe, Olavarría et Bariloche, de Campus France et de l'Institut français d'Argentine, consultés le 8 octobre 2026.",
    notes={"resistencia-alliance-francaise-de-resistencia": "FEI lui attribue l'adresse de l'Alliance de Buenos Aires ; le téléphone (362) et la carte du réseau la situent à Resistencia (Chaco)."},
    urls={"bahia-blanca-alliance-francaise-de-bahia-blanca": "", "ushuaia-alliance-francaise-de-la-terre-de-feu": "",
          "san-salvador-de-jujuy-alliance-francaise-jujuy": "", "mendoza-alliance-francaise-de-mendoza": "https://alianzafrancesamendoza.com/"},
))
