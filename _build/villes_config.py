# -*- coding: utf-8 -*-
"""Configuration des pages par ville (make_villes.py) — relevés du 17/09/2026, liste FEI du 19/09/2026."""

PROCEDURES = {
    "fr": {
        "tcf": """<p>En France, on s'inscrit <strong>en ligne, sur le site du centre</strong> — jamais auprès de France
Éducation international —, en général jusqu'à quelques jours avant la session : 48 heures à l'Alliance
française de Lyon, cinq jours chez ACCORD à Paris, dix jours à Montpellier. Le formulaire demande une
pièce d'identité, le motif (naturalisation, Canada…) et un paiement par carte ; les frais sont le plus
souvent non remboursables. Le jour J : pièce d'identité officielle avec photo et convocation. Comptez
<strong>20 à 30 jours</strong> entre deux passations, <strong>2 à 3 semaines</strong> pour l'attestation,
valable deux ans. Vérifiez sur la page du centre qu'il organise bien votre déclinaison — IRN, Canada,
Québec ou tout public — : la liste de FEI ne le précise pas.</p>""",
        "delf": """<p>On s'inscrit <strong>auprès du centre</strong>, jamais auprès de France Éducation international,
pour l'une des <strong>dix sessions nationales</strong> de l'année — jamais en avril ni en septembre —, et
chaque centre n'ouvre qu'une partie de ces sessions. La fenêtre d'inscription ferme <strong>quatre à dix
semaines avant l'écrit</strong>, parfois sur deux jours seulement ; pièce d'identité en cours de validité,
paiement par carte, droits non remboursables. Résultats sous quatre à six semaines, diplôme valable à vie.
Le calendrier 2026-2027 et les règles sont dans notre guide
<a href="/blog/ou-passer-le-delf-en-france/">où passer le DELF en France</a>.</p>""",
    },
    "ca": {
        "tcf": """<p>Au Canada, chaque centre gère ses inscriptions <strong>en ligne, sur son propre site</strong>, avec
le passeport que vous utiliserez dans votre dossier IRCC ; l'inscription est définitive, et les annulations
coûtent (75 $ à plus de 15 jours à l'Alliance Française de Montréal, rien remboursé après). Dans les grandes
villes, les sessions <strong>affichent complet en quelques minutes</strong> : créez votre compte à l'avance
et connectez-vous à l'ouverture des inscriptions. <strong>20 jours</strong> minimum entre deux passations,
quel que soit le centre ; résultats par e-mail sous 2 à 4 semaines, valables deux ans. Passeport valide et
convocation imprimée le jour J.</p>""",
    },
    "dz": {
        "tcf": """<p>En Algérie, l'inscription au TCF — Canada, IRN, Québec, tout public ou DAP — se fait
<strong>exclusivement en ligne</strong>, sur la plateforme <strong>IFAL</strong> (forms.vfsglobal.com.dz/IFAL),
opérée par VFS Global et accessible depuis la page TCF du site officiel <strong>if-algerie.com</strong> :
compte, choix de l'antenne et de la session, paiement en ligne. « Des sessions TCF sont ouvertes tous les
mois sur les cinq antennes » ; <strong>26 jours</strong> entre deux inscriptions selon la page nationale,
<strong>36 jours</strong> selon les pages des antennes d'Oran, Constantine, Annaba et Tlemcen ; carte
d'identité biométrique ou passeport le jour J, jamais le permis de conduire. Tarifs affichés par les antennes
le 17 octobre 2026 : <strong>37 500 DA</strong> pour le TCF Canada et le TCF Québec, 19 500 DA pour le TCF DAP,
13 000 DA pour le TCF tout public. Attention au faux site <em>if-algerie.fr</em>, qui propose un « candidat
partenaire » : c'est une escroquerie.</p>""",
    },
    "ma": {
        "tcf": """<p>Au Maroc, l'inscription se fait <strong>en ligne, sur le site de l'Institut français de la ville</strong>
(if-maroc.org/casablanca, /rabat…), page « TCF Canada » : on choisit une session dans la liste, on
l'ajoute au panier et on paie — <strong>2 900 Dhs</strong> pour le TCF Canada, 1 900 Dhs pour l'IRN, qui
s'inscrit lui à l'accueil. Pièce d'identité et photo demandées, convocation remise dès l'inscription.
<strong>20 jours</strong> de carence entre deux TCF sous peine d'annulation sans remboursement ; aucun
remboursement, report sur justificatif facturé 500 Dhs ; attestation à retirer à l'accueil du centre.</p>""",
    },
    "tn": {
        "tcf": """<p>En Tunisie, l'Institut français procède en deux temps : un <strong>rendez-vous en ligne</strong> pendant la
fenêtre ouverte pour la session (environ une semaine, un mois avant le test), puis <strong>l'inscription et
le paiement sur place</strong>, au pôle choisi, le jour fixé — <strong>880 DT</strong> pour le TCF Canada,
en espèces (carte bancaire à Tunis seulement), chèques suspendus. Un mandataire muni d'une copie de votre
carte d'identité peut s'inscrire pour vous. Frais non remboursables ; <strong>30 jours</strong> entre deux
sessions ; résultats <strong>cinq semaines</strong> après la passation.</p>""",
    },
}

GUIDES = {
    ("fr", "tcf"): [("/blog/ou-passer-le-tcf-irn-en-france/", "Où passer le TCF IRN en France ?", "Sept centres à Paris, des sessions chaque semaine, 140 à 220 €."),
                    ("/blog/ou-passer-le-tcf-canada-en-france/", "Où passer le TCF Canada en France ?", "Les centres qui le proposent, 195 à 285 €, leurs dates de session."),
                    ("/centres/tcf-france/", "Les 247 centres TCF en France", "Région par région, avec contacts.")],
    ("fr", "delf"): [("/blog/ou-passer-le-delf-en-france/", "Où passer le DELF en France ?", "Le calendrier 2026-2027, les prix relevés, les fenêtres d'inscription."),
                     ("/centres/delf-france/", "Les 143 centres DELF-DALF en France", "Région par région, avec contacts.")],
    ("ca", "tcf"): [("/blog/ou-passer-le-tcf-canada-au-canada/", "Où passer le TCF Canada au Canada ?", "Les 48 centres, 390 à 440 $, la méthode pour obtenir une place."),
                    ("/centres/tcf-canada/", "Les 48 centres TCF au Canada", "Province par province, avec contacts.")],
    ("dz", "tcf"): [("/blog/ifal-tcf-rendez-vous/", "IFAL TCF : prendre rendez-vous sur la plateforme VFS", "Les étapes, la déclinaison à choisir, les tarifs, les délais entre deux inscriptions, l'assistance VFS."),
                    ("/blog/tcf-canada-algerie/", "TCF Canada en Algérie : où le passer, comment s'inscrire", "Les cinq antennes, 37 500 DA, les résultats, le faux site à éviter."),
                    ("/centres/tcf-algerie/", "Les 5 centres TCF en Algérie", "Les antennes de l'Institut français, avec contacts.")],
    ("ma", "tcf"): [("/blog/tcf-canada-maroc/", "TCF Canada au Maroc : les 16 centres et l'inscription", "L'inscription en ligne pas à pas, les sessions d'octobre à décembre ville par ville, les règles de report."),
                    ("/centres/tcf-maroc/", "Les 16 centres TCF au Maroc", "Ville par ville, avec contacts.")],
    ("tn", "tcf"): [("/blog/tcf-canada-tunisie/", "TCF Canada en Tunisie : centres, calendrier, inscription", "Le calendrier d'octobre à décembre pôle par pôle, la procédure, les frais, les délais."),
                    ("/centres/tcf-tunisie/", "Les 14 centres TCF en Tunisie", "Ville par ville, avec contacts.")],
}
ALSO = {
    "tcf": [("/tcf-canada/", "TCF Canada : la page d'accueil", "Ce qu'est le test, pour qui, et les modules du dossier."),
            ("/tcf-irn/", "TCF IRN : la page d'accueil", "Le test de français des démarches françaises."),
            ("/blog/prix-tcf-tef/", "Combien coûte vraiment le TCF ou le TEF ?", "Aucun tarif national : les prix relevés centre par centre."),
            ("/examens-blancs/", "Examens blancs au format officiel", "")],
    "delf": [("/delf-b2/", "DELF B2 : la page d'accueil", "Ce qu'est le diplôme, pour qui, et les modules du dossier."),
             ("/delf-b1/", "DELF B1 : la page d'accueil", "Le niveau exigé pour la carte de résident."),
             ("/blog/diplome-ou-test-delf-tcf/", "Diplôme ou test : lequel vous faut-il ?", ""),
             ("/examens-blancs/", "Examens blancs au format officiel", "")],
}
OG = {"fr": "centres-tcf-france", "ca": "centres-tcf-canada", "dz": "centres-tcf-algerie", "ma": "centres-tcf-maroc", "tn": "centres-tcf-tunisie"}
DS = {"fr": ["tcf_france"], "ca": ["tcf_canada"], "dz": ["tcf_algerie"], "ma": ["tcf_maroc"], "tn": ["tcf_tunisie"]}


def mk(slug, label, country, match, title, desc, h1, intro, facts, releve, faq, exam="tcf", prep="à",
       nearby=None, stat3=None, stat4=None, centres_intro=None, releve_note="", crumb=None, h2_label=None,
       releve_date=None, modified=None, published=None):
    # releve_date : date du relevé des sites (défaut : make_villes.RELEVE) ; modified : (AAAA-MM-JJ, « 17 octobre 2026 ») ;
    # published : AAAA-MM-JJ d'une page créée après le premier lot (défaut : make_villes.DATE)
    return dict(slug=slug, label=label, h2_label=h2_label or label, prep=prep, country=country, exam=exam,
                releve_date=releve_date, modified=modified, published=published,
                datasets=DS[country] if exam == "tcf" else ["delf_france"], match=match, nearby=nearby or [],
                crumb=crumb or f"{'TCF' if exam == 'tcf' else 'DELF'} {prep} {label}",
                title=title, desc=desc, h1=h1, intro=intro, facts=facts,
                stat3=stat3 or ("relevé", "17 sept. 2026", "prix et dates lus sur les sites"),
                stat4=stat4 or (("2 ans", "de validité", "20 à 30 jours entre deux passations") if exam == "tcf" else ("à vie", "validité du diplôme", "10 sessions par an")),
                centres_intro=centres_intro or f"Les centres agréés par France Éducation international {prep} {h2_label or label}, avec les coordonnées que FEI publie (liste du {{liste_fei}}).",
                releve=releve, releve_note=releve_note, guides=GUIDES[(country, exam)], faq=faq, also=ALSO[exam], og_slug=OG[country] if exam == "tcf" else "centres-delf-france")


NR = "non relevé"

VILLES = [
    # ------------------------------------------------------------------ France, TCF
    mk("tcf-paris", "Paris", "fr", ["Paris"],
       title="TCF à Paris : 7 centres agréés, prix et dates (Canada, IRN)",
       desc="Les 7 centres TCF agréés à Paris avec contacts, les prix relevés (TCF IRN 140 à 220 €, TCF Canada 195 à 220 €), les dates de session et l'inscription.",

       h1="Passer le TCF à Paris : les 7 centres agréés, leurs prix et leurs dates",
       intro="""À Paris, le TCF — IRN pour la naturalisation, Canada pour l'immigration, tout public, Québec — se passe
dans <strong>%(n)d centres agréés</strong> par France Éducation international, tous avec des sessions sur
ordinateur. Le TCF IRN s'y organise <strong>presque chaque semaine</strong> et coûte de <strong>140 € (ACTE)
à 220 € (ACCORD)</strong> ; le TCF Canada, mensuel, de 195 à 220 €. Les sept centres avec leurs contacts,
ce que leurs sites affichaient le 17 septembre 2026, et comment s'inscrire.""",
       facts=["<strong>7 centres agréés</strong> dans Paris : ACTE (10<sup>e</sup>), ILE International (12<sup>e</sup>), Alliance française Paris Île-de-France (6<sup>e</sup>), Cours de civilisation française de la Sorbonne (17<sup>e</sup>), ELFE (1<sup>er</sup>), Etoile Institut (7<sup>e</sup>), ACCORD (15<sup>e</sup>).",
              "<strong>TCF IRN : 140 € chez ACTE, 160-170 € chez Etoile, 220 € chez ACCORD</strong> — presque une session par semaine.",
              "<strong>TCF Canada : 195 € chez ACTE (papier), 220 € chez ACCORD (ordinateur)</strong>, une à deux sessions par mois ; Etoile ne le propose pas.",
              "Examen civique aussi : 80-90 € chez Etoile, 110 € chez ACCORD ; l'Alliance française affichait complet.",
              "Résultats : « au minimum 3 semaines » chez ACTE, attestation provisoire immédiate pour les QCM chez ACCORD."],
       releve=[("ACTE", "IRN, Canada, tout public, DELF", "IRN <strong>140 €</strong> · Canada <strong>195 €</strong> (papier)", "IRN : 14, 21, 28 oct., 18, 25 nov., 9, 16 déc. 2026 ; Canada : 4 nov., 2 déc. Résultats ≥ 3 semaines."),
               ("ACCORD (examensparis.fr)", "IRN, Canada, Québec, tout public, examen civique", "IRN <strong>220 €</strong> · Canada <strong>220 €</strong> · TP 160/260 € · civique 110 €", "IRN 2 fois par mois ; Canada 23 sept., 28 oct. ; inscription close 5 jours avant, par bulletin et paiement CB ou espèces."),
               ("Etoile Institut", "IRN, tout public, Québec (+ TEF Canada, TEFAQ)", "IRN <strong>160 €</strong> semaine / 170 € samedi · TP 120 + 65 + 60 €", "Pas de TCF Canada. Examen civique 80 € (90 € le samedi), sessions presque quotidiennes."),
               ("Cours de civilisation française de la Sorbonne", "IRN et tout public sur ordinateur", NR, "Pages TCF du centre."),
               ("Alliance française Paris Île-de-France", "TEF, DELF, examen civique mis en avant", NR, "Vérifiez l'IRN sur alliancefr.org ; examen civique « complet » le 17/09."),
               ("ELFE · ILE International", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le TCF Canada à Paris ?", "Chez ACTE (10e, 195 € sur papier, sessions les 4 novembre et 2 décembre 2026) ou chez ACCORD (15e, 220 € sur ordinateur, 23 septembre et 28 octobre) — relevé le 17 septembre 2026. Les Cours de civilisation française de la Sorbonne, l'Alliance française Paris Île-de-France, ELFE et ILE International sont agréés mais à vérifier ; Etoile Institut ne propose pas le TCF Canada."),
            ("Où passer le TCF IRN à Paris ?", "Dans les sept centres agréés ; ACTE affiche presque une session par semaine à 140 €, ACCORD deux par mois à 220 €, Etoile Institut 160 € en semaine et 170 € le samedi. L'inscription se fait en ligne, quelques jours avant."),
            ("Combien coûte le TCF à Paris ?", "Aucun tarif national : pour le même TCF IRN, 140 € chez ACTE et 220 € chez ACCORD, à trois stations de métro ; TCF Canada 195 € chez ACTE et 220 € chez ACCORD ; TCF tout public 120 à 160 € pour les épreuves obligatoires. Relevé le 17 septembre 2026."),
            ("Peut-on passer l'examen civique à Paris dans les mêmes centres ?", "Oui pour plusieurs : ACCORD (110 €, attestation sous 12 heures), Etoile Institut (80-90 €), ACTE, l'Alliance française (sessions complètes le 17/09) sont agréés pour l'examen civique — mais il faut une inscription séparée, via test-civique.fr pour le réseau FEI.")]),
    mk("tcf-lyon", "Lyon", "fr", ["Lyon", "Villeurbanne"], h2_label="Lyon et Villeurbanne",
       title="TCF à Lyon : centres agréés, prix et dates (IRN, Canada)",
       desc="Les 5 centres TCF agréés à Lyon avec contacts, les prix de l'Alliance française (IRN 169 €, Canada 220 €), les sessions d'ici décembre 2026, l'inscription.",

       h1="Passer le TCF à Lyon : les centres agréés, leurs prix et leurs dates",
       intro="""À Lyon, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international
(Villeurbanne compris), dont %(so)d avec des sessions sur ordinateur. Le centre le plus documenté est
l'<strong>Alliance française de Lyon</strong> : TCF IRN sur ordinateur à <strong>169 €</strong>, TCF Canada à
<strong>220 €</strong>, une session par mois pour le Canada — et, le 17 septembre 2026, les sessions de
septembre déjà complètes. Les centres avec leurs contacts, le relevé, et l'inscription.""",
       facts=["<strong>%s centres agréés</strong> à Lyon et Villeurbanne : Alliance française, Lyon Exam (Inflexyon), Lyon Bleu, ALPADIA, FC2E." % 5,
              "<strong>Alliance française de Lyon : TCF IRN 169 € (ordinateur), TCF Canada 220 €</strong> ; inscriptions closes 48 h avant.",
              "TCF Canada : 21 octobre, 25 novembre, 16 décembre 2026 encore ouverts le 17 septembre ; TCF IRN : 19 novembre.",
              "« Délai minimum de 20 jours entre deux sessions TCF » ; résultats par courriel sous 2 à 3 semaines.",
              "KLF (klf-examen.fr) organise aussi des sessions à Lyon, sur ordinateur, résultats en 10 jours à 3 semaines."],
       releve=[("Alliance française de Lyon", "IRN (papier et ordinateur), Canada, tout public, examen civique", "IRN SO <strong>169 €</strong> · Canada <strong>220 €</strong>", "Canada : 21 oct., 25 nov., 16 déc. 2026 (10 et 23 sept. complets) ; IRN SO : 19 nov. (22 oct. complet). Clôture 48 h avant ; résultats 2-3 semaines."),
               ("KLF Lyon (klf-examen.fr)", "IRN, Canada, Québec, tout public, sur ordinateur", NR, "Réservation en ligne ; résultats « entre 10 jours et 3 semaines »."),
               ("Lyon Exam (Inflexyon) · Lyon Bleu · ALPADIA · FC2E", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le TCF Canada à Lyon ?", "À l'Alliance française de Lyon (220 €, une session par mois : 21 octobre, 25 novembre, 16 décembre 2026 encore ouverts le 17 septembre) ou chez KLF Lyon sur ordinateur ; Lyon Exam, Lyon Bleu et ALPADIA sont agréés, à vérifier sur leur site."),
            ("Où passer le TCF IRN à Lyon ?", "À l'Alliance française de Lyon, sur ordinateur à 169 € (sessions des 9 et 17 septembre et du 22 octobre complètes le 17 septembre, 19 novembre ouvert), chez KLF, ou dans l'un des autres centres agréés de la ville."),
            ("Combien coûte le TCF à Lyon ?", "169 € pour le TCF IRN sur ordinateur et 220 € pour le TCF Canada à l'Alliance française de Lyon (17 septembre 2026) ; les autres centres ne publient pas de tarif lisible en ligne."),
            ("Quel délai pour repasser le TCF à Lyon ?", "L'Alliance française de Lyon applique « un délai minimum de 20 jours entre deux sessions TCF » ; les résultats arrivent par courriel sous deux à trois semaines.")]),
    mk("tcf-marseille", "Marseille", "fr", ["Marseille", "Aix-en-Provence"], prep="à", h2_label="Marseille et Aix-en-Provence",
       title="TCF à Marseille et Aix : centres agréés, prix, dates",
       desc="Les 5 centres TCF agréés à Marseille et Aix avec contacts, le TCF Canada et Québec à 60 € par épreuve à l'Alliance française (ordinateur), l'inscription.",

       h1="Passer le TCF à Marseille et Aix-en-Provence : centres, prix et dates",
       intro="""À Marseille et Aix-en-Provence, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France
Éducation international, dont %(so)d avec des sessions sur ordinateur. L'<strong>Alliance française
Aix-Marseille Provence</strong> propose le TCF Canada et le TCF Québec <strong>à 60 € par épreuve</strong>,
sur ordinateur uniquement, avec inscription deux semaines à l'avance et résultats en quinze jours. Les
centres avec leurs contacts, le relevé, et l'inscription.""",
       facts=["<strong>5 centres agréés</strong> : Alliance française Aix-Marseille Provence (Marseille et Aix), Atout Langues Sud, Sud Formation, IS Aix.",
              "<strong>Alliance française : TCF Canada et Québec 60 € par épreuve</strong>, soit 240 € pour un TCF Canada complet.",
              "Sur ordinateur uniquement : « la maîtrise de l'informatique est obligatoire », pas de correcteur d'orthographe.",
              "Inscription deux semaines à l'avance ; convocation une semaine avant ; résultats en 15 jours.",
              "« Un délai minimum de 20 jours doit être respecté entre deux examens. »"],
       releve=[("Alliance française Aix-Marseille Provence", "IRN, tout public, Québec, Canada (ordinateur uniquement), DELF", "Canada / Québec <strong>60 € par épreuve</strong>", "Inscription 2 semaines à l'avance, résultats en 15 jours, 20 jours entre deux examens."),
               ("Atout Langues Sud · Sud Formation · IS Aix", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le TCF Canada à Marseille ?", "À l'Alliance française Aix-Marseille Provence, sur ordinateur uniquement, à 60 € par épreuve (240 € les quatre) — inscription deux semaines à l'avance, résultats en quinze jours —, ou dans l'un des autres centres agréés de Marseille et d'Aix, à vérifier sur leur site."),
            ("Combien coûte le TCF à Marseille ?", "À l'Alliance française, 60 € par épreuve pour le TCF Québec et le TCF Canada (17 septembre 2026) ; les autres centres ne publient pas de tarif lisible en ligne."),
            ("Le TCF se passe-t-il sur papier à Marseille ?", "Pas à l'Alliance française, qui ne propose que l'ordinateur et prévient qu'elle ne remboursera pas un candidat qui ne sait pas s'en servir. Atout Langues Sud ne déclare pas de sessions sur ordinateur à FEI : le papier y est probable, à confirmer ; Sud Formation, elle, en déclare dans la liste du 26 octobre 2026.")]),
    mk("tcf-toulouse", "Toulouse", "fr", ["Toulouse"],
       title="TCF à Toulouse : 5 centres agréés, contacts et inscription",
       desc="Les 5 centres TCF agréés à Toulouse avec adresse, téléphone et site — Alliance française, Langue Onze, CREPT, AMS, ICT — et l'inscription.",

       h1="Passer le TCF à Toulouse : les 5 centres agréés et l'inscription",
       intro="""À Toulouse, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international,
dont %(so)d avec des sessions sur ordinateur — Alliance française, Langue Onze, CREPT Formation, AMS Grand
Sud et l'Institut catholique. KLF y organise aussi des sessions sur
ordinateur. Les centres avec leurs contacts, ce que nous savons de leurs tarifs, et l'inscription.""",
       facts=["<strong>5 centres agréés</strong> dans Toulouse, 3 avec des sessions sur ordinateur.",
              "KLF (klf-examen.fr) réserve des sessions TCF IRN, Canada et Québec à Toulouse, sur ordinateur.",
              "L'université Toulouse Jean Jaurès a été relevée à 80 € (3 QCM) et 185 € (complet) pour le TCF tout public en juillet 2026.",
              "Vérifiez la déclinaison sur le site de chaque centre : la liste FEI ne la précise pas.",
              "Résultats en 2 à 3 semaines ; 20 à 30 jours entre deux passations."],
       releve=[("KLF Toulouse (klf-examen.fr)", "IRN, Canada, Québec, tout public, sur ordinateur", NR, "Réservation en ligne ; résultats « entre 10 jours et 3 semaines »."),
               ("Université Toulouse Jean Jaurès (DEFLE)", "TCF tout public (relevé en juillet 2026)", "3 QCM <strong>80 €</strong> · complet <strong>185 €</strong>", "Tarifs « sous réserve de validation par le CA de l'Université »."),
               ("Alliance française · Langue Onze · CREPT · AMS Grand Sud · ICT", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le TCF Canada à Toulouse ?", "Chez KLF Toulouse sur ordinateur, ou dans l'un des cinq centres agréés de la ville — Alliance française, Langue Onze, CREPT, AMS Grand Sud, ICT — après avoir vérifié sur leur site qu'ils organisent la déclinaison Canada."),
            ("Combien coûte le TCF à Toulouse ?", "Les centres toulousains publient peu de tarifs : l'université Toulouse Jean Jaurès affichait en juillet 2026 80 € pour les trois QCM du tout public et 185 € pour le test complet. Ailleurs en France, un TCF IRN va de 140 à 220 €, un TCF Canada de 195 à 285 €."),
            ("Comment s'inscrire au TCF à Toulouse ?", "En ligne, sur le site du centre choisi, quelques jours avant la session, avec une pièce d'identité et un paiement par carte ; la liste FEI ne précisant pas les déclinaisons, vérifiez « IRN » ou « Canada » sur la page du centre.")]),
    mk("tcf-montpellier", "Montpellier", "fr", ["Montpellier"],
       title="TCF à Montpellier : centres, prix et dates (IRN, Canada)",
       desc="Les 4 centres TCF agréés à Montpellier avec contacts, les tarifs de l'Alliance française (IRN 185 €, Canada 200 €, Québec 65 €/module), les dates.",

       h1="Passer le TCF à Montpellier : centres, prix et dates",
       intro="""À Montpellier, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international,
dont %(so)d avec des sessions sur ordinateur. L'<strong>Alliance française de Montpellier</strong> publie une
grille complète : TCF IRN <strong>185 €</strong>, TCF Canada <strong>200 €</strong> sur ordinateur, TCF Québec
<strong>65 € par module</strong>, examen civique 75 € — avec une session TCF Canada le 13 novembre 2026. Les
centres avec leurs contacts, le relevé, et l'inscription.""",
       facts=["<strong>4 centres agréés</strong> : Alliance française de Montpellier, LSF, INFREP, GRETA CFA Montpellier Littoral — et KLF y réserve des sessions sur ordinateur.",
              "<strong>Alliance française : IRN 185 €, Canada 200 €, Québec 65 € par module, tout public 125 € + 50 € par épreuve facultative, examen civique 75 €.</strong>",
              "TCF Canada sur ordinateur : 23 septembre (inscription jusqu'au 13) et 13 novembre 2026 (jusqu'au 3 novembre).",
              "Résultats définitifs « sous 2 semaines » sur ordinateur.",
              "Recorrection suspendue depuis les sessions du 1<sup>er</sup> septembre 2026, reprise annoncée pour l'automne 2027."],
       releve=[("Alliance française de Montpellier", "IRN (papier ou ordinateur), Canada, Québec, tout public, examen civique", "IRN <strong>185 €</strong> · Canada <strong>200 €</strong> · Québec <strong>65 €/module</strong> · TP 125 € + 50 € · civique 75 €", "Canada : 23 sept. (limite 13 sept.), 13 nov. 2026 (limite 3 nov.) ; résultats sous 2 semaines."),
               ("KLF Montpellier (klf-examen.fr)", "IRN, Canada, Québec, tout public, sur ordinateur", NR, "Réservation en ligne ; résultats 10 jours à 3 semaines."),
               ("LSF · INFREP · GRETA CFA Montpellier Littoral", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le TCF Canada à Montpellier ?", "À l'Alliance française de Montpellier, sur ordinateur, à 200 € — sessions des 23 septembre et 13 novembre 2026 relevées —, ou chez KLF Montpellier ; LSF, INFREP et le GRETA CFA Montpellier Littoral sont agréés, à vérifier."),
            ("Combien coûte le TCF à Montpellier ?", "À l'Alliance française (17 septembre 2026) : 185 € le TCF IRN, 200 € le TCF Canada, 65 € par module de TCF Québec, 125 € les épreuves obligatoires du tout public plus 50 € par épreuve facultative, 75 € l'examen civique."),
            ("Combien de temps pour les résultats à Montpellier ?", "« Sous 2 semaines » sur ordinateur à l'Alliance française, « entre 10 jours et 3 semaines » chez KLF. Depuis le 1er septembre 2026, aucune recorrection n'est possible.")]),
    mk("tcf-bordeaux", "Bordeaux", "fr", ["Bordeaux", "Pessac"], h2_label="Bordeaux et Pessac",
       title="TCF à Bordeaux : centres agréés, contacts et inscription",
       desc="Les 4 centres TCF agréés à Bordeaux et Pessac avec adresse, téléphone et site — Alliance française, Newdeal / KLF, INFREP, CLEFF — et l'inscription.",

       h1="Passer le TCF à Bordeaux : les centres agréés et l'inscription",
       intro="""À Bordeaux, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international
(Pessac compris), dont %(so)d avec des sessions sur ordinateur — l'Alliance française Bordeaux
Nouvelle-Aquitaine, Newdeal Institut, dont la marque d'examens KLF réserve en ligne des sessions IRN, Canada
et Québec sur ordinateur, INFREP et le CLEFF de l'université. Les centres avec leurs contacts, le relevé, et
l'inscription.""",
       facts=["<strong>4 centres agréés</strong> à Bordeaux et Pessac.",
              "<strong>KLF / Newdeal Institut</strong> : IRN, Canada, Québec, tout public sur ordinateur, réservation en ligne, résultats « entre 10 jours et 3 semaines ».",
              "L'attestation définitive, valable 2 ans, se retire au centre.",
              "Vérifiez la déclinaison sur le site de chaque centre : la liste FEI ne la précise pas.",
              "20 à 30 jours entre deux passations."],
       releve=[("KLF · Newdeal Institut (klf-examen.fr)", "IRN, Canada, Québec, tout public, sur ordinateur", NR, "Réservation en ligne ; résultats 10 jours à 3 semaines ; attestation à retirer au centre."),
               ("Alliance française Bordeaux Nouvelle-Aquitaine · INFREP · CLEFF (Pessac)", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le TCF Canada à Bordeaux ?", "Chez KLF / Newdeal Institut, sur ordinateur, avec réservation en ligne, ou à l'Alliance française Bordeaux Nouvelle-Aquitaine après vérification sur son site ; INFREP et le CLEFF de Pessac sont aussi agréés."),
            ("Combien coûte le TCF à Bordeaux ?", "Les centres bordelais ne publient pas de tarif lisible en ligne ; en France, un TCF IRN va de 140 à 220 € et un TCF Canada de 195 à 285 € selon le centre."),
            ("Comment s'inscrire au TCF à Bordeaux ?", "En ligne, sur le site du centre — KLF réserve les sessions en ligne —, quelques jours avant, avec une pièce d'identité et un paiement par carte.")]),
    mk("tcf-nantes", "Nantes", "fr", ["Nantes", "Saint-Nazaire"], h2_label="Nantes et Saint-Nazaire",
       title="TCF à Nantes : centres agréés, examen civique, inscription",
       desc="Les 4 centres TCF agréés à Nantes et Saint-Nazaire avec contacts — Espaces Formation en tête —, le TCF papier ou ordinateur, l'examen civique à 70 €.",

       h1="Passer le TCF à Nantes : centres agréés, examen civique et inscription",
       intro="""À Nantes, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international
(Saint-Nazaire compris), dont %(so)d avec des sessions sur ordinateur. <strong>Espaces Formation</strong> organise
le TCF IRN, le TCF Canada et le TCF Québec sur papier ou sur ordinateur, avec inscription et paiement en
ligne, des sessions « en urgence » selon disponibilités, et l'<strong>examen civique à 70 €</strong> avec des
résultats sous douze heures. Les centres avec leurs contacts, le relevé, et l'inscription.""",
       facts=["<strong>4 centres agréés</strong> : Espaces Formation, Institut Fonelia et le Service universitaire des langues de Nantes Université à Nantes, Cefol Management à Saint-Nazaire.",
              "<strong>Espaces Formation : IRN, Canada, Québec, papier ou ordinateur</strong>, inscription et paiement en ligne, résultats sous 2 à 3 semaines.",
              "<strong>Examen civique 70 €</strong>, résultats « généralement sous 12 heures ».",
              "Sessions TCF « en urgence » sur ordinateur, sous réserve des disponibilités du centre.",
              "Pour le DELF, Nantes Université est le centre le moins cher relevé en France (B1-B2 125 €)."],
       releve=[("Espaces Formation", "IRN, Canada, Québec (papier ou ordinateur), examen civique", "Civique <strong>70 €</strong> ; TCF non relevé", "Inscription et paiement en ligne ; résultats TCF sous 2 à 3 semaines, civique sous 12 heures ; sessions en urgence possibles."),
               ("Institut Fonelia · Nantes Université (SUL) · Cefol Management (Saint-Nazaire)", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le TCF Canada à Nantes ?", "Chez Espaces Formation (1, rue de la Petite-Reine), sur papier ou sur ordinateur, avec inscription en ligne ; l'Institut Fonelia, le Service universitaire des langues de Nantes Université et Cefol Management à Saint-Nazaire sont aussi agréés, à vérifier sur leur site."),
            ("Où passer l'examen civique à Nantes ?", "Chez Espaces Formation, agréé pour l'examen civique : 70 €, inscription en ligne, résultats dans votre espace candidat « généralement sous 12 heures »."),
            ("Combien coûte le TCF à Nantes ?", "Espaces Formation ne publie pas le tarif de ses TCF sur la page consultée ; en France, un TCF IRN va de 140 à 220 € et un TCF Canada de 195 à 285 €.")]),
    mk("tcf-rennes", "Rennes", "fr", ["Rennes"],
       title="TCF à Rennes : CLPS, prix et dates (IRN 180 €, Canada 285 €)",
       desc="Où passer le TCF à Rennes : CLPS (IRN 180 €, Canada 285 €, tout public 110 €, sessions du 19 nov. au 21 déc. 2026 ; Brest, Saint-Brieuc, Vannes), résultats.",
       h1="Passer le TCF à Rennes : centres agréés, prix et dates",
       intro="""À Rennes, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international. Le
<strong>CLPS L'Enjeu Compétences</strong> (5 rue Léon-Berthault) publie une grille complète — TCF IRN <strong>180 €</strong>,
TCF Canada <strong>285 €</strong>, tout public 110 € plus 52 € par expression — et son calendrier du second semestre 2026 :
IRN les 19 novembre, 26 novembre (papier), 3 et 17 décembre, Canada et tout public les 24 novembre et 21 décembre ; il
organise aussi l'IRN à Brest, Saint-Brieuc et Vannes. Le second centre de la liste FEI, Langue et Communication, renvoie
vers un site de Compiègne : à vérifier par téléphone. Les centres, le relevé du 29 octobre 2026, et l'inscription.""",
       facts=["<strong>2 centres agréés</strong> à Rennes selon FEI : CLPS L'Enjeu Compétences (ordinateur et papier) et Langue et Communication — dont le site indiqué (languesetformations.fr) est celui d'un centre de Compiègne : vérifiez avant de vous déplacer.",
              "<strong>CLPS : TCF IRN 180 €, TCF Canada 285 €, tout public 110 € + 52 € par expression, TCF Québec 71 € (CO, CE) ou 74 € (EO, EE) l'épreuve</strong> — inchangés depuis le 23 juin 2026.",
              "CLPS, Rennes, 2<sup>e</sup> semestre 2026 : IRN les jeudis <strong>19 novembre</strong> (ordinateur, limite 12 novembre), 26 novembre (papier), 3 décembre (ordinateur) et 17 décembre (papier, limite 19 novembre) ; <strong>Canada et tout public</strong> les 24 novembre (limite 17 novembre) et 21 décembre (limite 14 décembre) ; Québec à la demande ; calendrier 2027 non publié.",
              "Ailleurs en Bretagne (CLPS) : IRN à Brest (4, 13, 18 novembre, 2, 10, 16 décembre), Saint-Brieuc (6, 20 novembre, 4, 11, 18 décembre), Vannes (17 novembre, 1<sup>er</sup>, 15 décembre) ; Canada à Brest sur demande.",
              "Résultats : 10 jours ouvrés après la clôture d'une session sur ordinateur (QCM), 15 jours ouvrés après réception des copies pour le papier ; original de la pièce d'identité exigé, photo prise le jour J.",
              "285 € : le TCF Canada le plus cher relevé en France — pour un test identique à celui d'ACTE à 195 €."],
       releve=[("CLPS L'Enjeu Compétences (Rennes)", "IRN (ordinateur et papier), tout public, Canada, Québec (sur ordinateur)", "IRN <strong>180 €</strong> · Canada <strong>285 €</strong> · TP 110 € + 52 € + 52 € · Québec 71-74 € l'épreuve", "IRN 19 nov. (ordi., limite 12 nov.), 26 nov. (papier), 3 déc. (ordi.), 17 déc. 2026 (papier) ; Canada et TP 24 nov., 21 déc. 2026 ; Québec à la demande ; fiches d'inscription en ligne ; 2027 non publié."),
               ("Langue et Communication", NR, "Sur le site indiqué par FEI (Compiègne) : IRN ordinateur 200 €, papier 170 €, Canada et Québec 250 €", "Site languesetformations.fr = Espace Langues et Formations, Compiègne (Oise) ; aucune session rennaise visible ; vérifier auprès du centre.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("19 nov.", "prochaine session IRN (CLPS)", "limite 12 nov. ; Canada 24 nov."),
       faq=[("Où passer le TCF Canada à Rennes ?", "Au CLPS L'Enjeu Compétences (285 €, sur ordinateur) : 24 novembre 2026 (inscription avant le 17) et 21 décembre (avant le 14), par fiche d'inscription en ligne ; aussi à Brest sur demande. Rien de relevable chez Langue et Communication."),
            ("Combien coûte le TCF à Rennes ?", "Au CLPS (relevé du 29 octobre 2026) : 180 € le TCF IRN, 285 € le TCF Canada, 110 € les épreuves obligatoires du tout public plus 52 € par expression, 71 à 74 € chaque épreuve du TCF Québec."),
            ("Peut-on passer le TCF ailleurs en Bretagne ?", "Oui : le CLPS organise le TCF IRN à Brest, Saint-Brieuc et Vannes (plusieurs dates par mois jusqu'au 18 décembre 2026) et le TCF Canada à Brest sur demande ; l'Alliance française Saint-Malo Bretagne est aussi agréée.")]),
    mk("tcf-strasbourg", "Strasbourg", "fr", ["Strasbourg"],
       title="TCF à Strasbourg : CIEL, Stralang, AF, prix et dates",
       desc="Où passer le TCF à Strasbourg : CIEL (IRN 155 €, Canada 200 €, TP 110 €), Stralang (IRN 150 €, TP 100 €, 24 novembre 2026), Alliance française (IRN 165 €).",
       h1="Passer le TCF à Strasbourg : les trois centres agréés, leurs prix et leurs dates",
       intro="""À Strasbourg, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international : le
<strong>CIEL</strong> (CCI Campus, 234 avenue de Colmar), seul à proposer le <strong>TCF Canada</strong> (200 €, prochaine
session le 26 janvier 2027), l'<strong>Institut Stralang</strong> (TCF IRN 150 € et tout public 100 €, les deux le
24 novembre 2026) et l'<strong>Alliance française Strasbourg Europe</strong> (TCF IRN sur papier ou sur ordinateur, 165 €).
Les centres, le relevé du 29 octobre 2026, et l'inscription.""",
       facts=["<strong>3 centres agréés</strong> : CIEL (tout public, IRN, Canada, sur ordinateur), Institut Stralang (tout public, IRN, sur ordinateur), Alliance française (IRN papier et ordinateur, tout public).",
              "<strong>CIEL : TCF IRN 155 €, TCF Canada 200 €, tout public 110 €</strong> (220 € avec les deux expressions) ; résultats « 4 semaines minimum ».",
              "CIEL, dates : IRN le 1<sup>er</sup> décembre 2026 (inscriptions jusqu'au 30 octobre), puis 12 janvier, 9 février, 6 avril, 11 mai 2027 et presque chaque mois ; Canada 26 janvier, 15 juin, 19 octobre 2027 ; tout public 16 février, 13 avril, 21 septembre 2027.",
              "<strong>Stralang : TCF IRN 150 €, tout public 100 €</strong> (épreuves obligatoires seulement), tous deux le mardi 24 novembre 2026 ; 10 candidats par session tout public ; inscription par fiche envoyée par e-mail avec le paiement.",
              "Alliance française : TCF IRN sur ordinateur 165 € « pour 2026 », résultats sous 2 à 3 semaines, présence sur place pour signer ; sessions « chaque mois », dates sur son module de réservation.",
              "Pas de TCF Québec ni de DAP relevé dans la ville ; 20 jours entre deux TCF partout."],
       releve=[("CIEL Strasbourg (CCI Campus)", "TP, IRN, Canada — sur ordinateur", "TP <strong>110 €</strong> (complet 220 €) · IRN <strong>155 €</strong> · Canada <strong>200 €</strong>", "IRN 1<sup>er</sup> déc. 2026 (limite 30 oct.), 12 janv. (limite 9 déc.), 9 févr., 6 avr., 11 mai, 1<sup>er</sup> juin, 6 juil., 7 sept., 5 oct., 16 nov., 7 déc. 2027 ; Canada 26 janv. (limite 6 janv.), 15 juin, 19 oct. 2027 ; TP 17 nov. 2026 (clos), 16 févr., 13 avr., 21 sept. 2027 ; inscription en ligne ou bulletin."),
               ("Institut Stralang", "TP (3 épreuves obligatoires), IRN — sur ordinateur", "TP <strong>100 €</strong> · IRN <strong>150 €</strong>", "24 nov. 2026 : TP à 14 h ; IRN à 10 h ou 12 h, oral les 24-25 nov. ; 10 places par session TP ; fiche + paiement par e-mail ou sur place ; attestation IRN au centre sous 20 jours ouvrés."),
               ("Alliance française Strasbourg Europe", "IRN (papier ou ordinateur), tout public ; pas de Canada", "IRN ordinateur <strong>165 €</strong> (2026) · autres : non relevé", "Sessions chaque mois (dates dans le module de réservation du site) ; inscription sur place ; résultats 2-3 semaines ; désistement : 30 € retenus à plus de 6 semaines.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("24 nov.", "prochaine session (Stralang)", "IRN et TP, 10 places"),
       faq=[("Où passer le TCF Canada à Strasbourg ?", "Au CIEL (CCI Campus, 234 avenue de Colmar), seul centre de la ville à l'afficher : 200 €, sessions des 26 janvier, 15 juin et 19 octobre 2027, inscription trois semaines avant. L'Alliance française et Stralang ne proposent que l'IRN et le tout public."),
            ("Où passer le TCF IRN à Strasbourg ?", "Chez Stralang (150 €, 24 novembre 2026), au CIEL (155 €, 1er décembre 2026 puis presque chaque mois en 2027) ou à l'Alliance française (165 € sur ordinateur, sessions mensuelles). Tous exigent 20 jours entre deux TCF."),
            ("Combien coûte le TCF à Strasbourg ?", "Relevé du 29 octobre 2026 : tout public 100 € chez Stralang, 110 € au CIEL (220 € avec les expressions) ; IRN 150 € (Stralang), 155 € (CIEL), 165 € (Alliance, ordinateur) ; Canada 200 € au CIEL.")]),
    mk("tcf-lille", "Lille", "fr", ["Lille"],
       title="TCF à Lille : ISPA et E2LF, prix et dates (IRN, Canada)",
       desc="Où passer le TCF à Lille : ISPA (tout public 100 €, IRN 170 €, Canada 210 €, sessions nov.-déc. 2026), E2LF (IRN 190 €, Canada 250 €, 15 janvier 2027).",
       h1="Passer le TCF à Lille : les deux centres agréés, leurs prix et leurs dates",
       intro="""À Lille, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international, tous deux sur
ordinateur et sur papier : l'<strong>Institut Langues et Savoirs (ISPA)</strong>, 177 rue Nationale — tout public
<strong>100 €</strong>, IRN 170 €, Canada 210 €, sessions presque chaque semaine jusqu'au 17 décembre 2026 — et
l'<strong>E2LF</strong> — IRN 190 € le 18 décembre 2026, Canada <strong>250 €</strong> le 15 janvier 2027. Les centres,
le relevé du 29 octobre 2026, et l'inscription.""",
       facts=["<strong>2 centres agréés</strong> : ISPA (campus de Lille, 177 rue Nationale ; 03 20 40 56 51) et E2LF (06 51 84 47 33, contact@e2lf.fr).",
              "<strong>ISPA : tout public 100 €</strong> (+ 45 € l'expression écrite, + 55 € l'orale), <strong>IRN 170 €</strong>, <strong>Canada 210 €</strong>, examen civique 70 € ; résultats par e-mail sous 15 jours ouvrés (ordinateur) ou 30 jours (papier).",
              "ISPA, dates : tout public les jeudis 5 novembre et 10 décembre 2026 ; IRN les 12, 19 et 26 novembre, le 3 décembre (sur papier), les 12 et 17 décembre ; Canada le samedi 21 novembre — affiché « épuisé » le 29 octobre.",
              "ISPA : inscription en ligne (carte) ou à l'accueil en espèces, trois jours avant la session ; sa fiche IRN dit que les candidats libres passent à Amiens — téléphonez avant de compter sur une place IRN à Lille.",
              "<strong>E2LF : IRN 190 €</strong> (vendredi 18 décembre 2026), <strong>Canada 250 €</strong> (vendredi 15 janvier 2027), tout public et Québec sur demande ; inscription sur sa plateforme gestion-tcf, place confirmée à réception du virement ; résultats sous 15 jours.",
              "Inscription ferme dans les deux centres (report seulement sur force majeure) ; 20 jours minimum entre deux TCF."],
       releve=[("Institut Langues et Savoirs — ISPA Lille", "TP, IRN, Canada (ordinateur et papier) ; TEF, examen civique", "TP <strong>100 €</strong> (+ 45 / + 55) · IRN <strong>170 €</strong> · Canada <strong>210 €</strong>", "TP 5 nov. (inscr. avant le 2) et 10 déc. 2026 ; IRN 12, 19, 26 nov., 3 déc. (papier), 12 et 17 déc. ; Canada 21 nov. (« épuisé ») ; boutique en ligne ou accueil."),
               ("E2LF — École lilloise de langue française", "TP, IRN, Québec, Canada (papier ou ordinateur) ; examen civique, DILF", "IRN <strong>190 €</strong> · Canada <strong>250 €</strong> · TP : sur demande", "IRN ven. 18 déc. 2026 ; Canada ven. 15 janv. 2027 ; inscription sur gestion-tcf.e2lf.fr, paiement par virement ; résultats 15 jours maximum.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("5 nov.", "prochaine session (ISPA, TP)", "inscription avant le 2 nov."),
       faq=[("Où passer le TCF Canada à Lille ?", "Chez ISPA (210 €, samedi 21 novembre 2026, session affichée « épuisée » le 29 octobre ; sessions « chaque trimestre ») ou à l'E2LF (250 €, vendredi 15 janvier 2027, inscription en ligne puis virement)."),
            ("Combien coûte le TCF à Lille ?", "Relevé du 29 octobre 2026 : tout public 100 € chez ISPA (épreuves obligatoires) ; IRN 170 € chez ISPA, 190 € à l'E2LF ; Canada 210 € chez ISPA, 250 € à l'E2LF ; examen civique 70 € chez ISPA."),
            ("Où passer le DELF à Lille ?", "À l'Alliance française de Lille Métropole, seul centre DELF-DALF agréé de la ville : de 120 € (A1) à 210 € (C2), prochaine session tout public en février 2027 — voir notre page DELF à Lille.")]),
    mk("tcf-nice", "Nice", "fr", ["Nice"],
       title="TCF à Nice : IRN 170-175 €, dates 2026-2027, 3 centres",
       desc="Où passer le TCF à Nice : FOLAM (IRN 170 €, 16 nov., 4 et 16 déc. 2026, puis 2027), Les Ateliers FL (175 €, 17 déc. puis chaque mois), Alliance française.",
       h1="Passer le TCF à Nice : les trois centres agréés, leurs prix et leurs dates",
       intro="""À Nice, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international. Pour le
<strong>TCF IRN</strong>, le plus demandé, la <strong>Ligue de l'enseignement (FOLAM)</strong>, 6 rue Oscar-II, affiche 170 €
et des sessions les 16 novembre, 4 et 16 décembre 2026 puis quatre en janvier-février 2027 (les 26 octobre et 2 novembre
étaient complètes), et <strong>Les Ateliers FL</strong> 175 € avec un atelier de préparation inclus, le 17 décembre 2026
puis chaque mois. L'<strong>Alliance française Nice Côte d'Azur</strong> est la seule à annoncer le <strong>TCF Canada</strong>,
sur ordinateur — ses dates et prix ne s'affichent que dans son module de réservation. Les centres, le relevé du
29 octobre 2026, et l'inscription.""",
       facts=["<strong>3 centres agréés</strong> : Alliance française Nice Côte d'Azur (8 rue de Paris), Les Ateliers FL (04 93 13 78 88), Ligue de l'enseignement FOLAM (passation 6 rue Oscar-II).",
              "<strong>FOLAM : TCF IRN 170 €</strong>, inscription un mois à l'avance : 16 novembre (limite dépassée), 4 décembre (limite 9 novembre) et 16 décembre 2026 (limite 22 novembre), puis 6, 20 et 29 janvier et 10 février 2027 ; test civique 80 €.",
              "<strong>Les Ateliers FL : TCF IRN 175 €</strong>, atelier préparatoire de 1 h 30 inclus (130 € en réinscription) ; 17 décembre 2026, puis 21 janvier, 25 février, 25 mars, 22 avril 2027 et un jeudi par mois jusqu'en décembre ; inscription quatre semaines avant, attestation envoyée quatre semaines après.",
              "Alliance française : TCF IRN (papier ou ordinateur), tout public, Canada (sur ordinateur) et examen civique (80 €, convocation 2 rue de Paris) ; dates et tarifs TCF dans son module de réservation en ligne.",
              "TCF Canada et Québec : « nous contacter » chez FOLAM, non listés aux Ateliers FL ; l'Alliance est le seul centre niçois à l'annoncer.",
              "Pour le DELF-DALF : le CUEFLE de l'Université Côte d'Azur organise une session de DALF C1-C2 par an (27-31 mai 2027, inscriptions 1<sup>er</sup> mars-3 mai, 170 € ou 200 €)."],
       releve=[("Ligue de l'enseignement — FOLAM", "IRN ; tout public, Québec, Canada « nous contacter » ; test civique", "IRN <strong>170 €</strong> · civique 80 €", "IRN : 16 nov., 4 déc., 16 déc. 2026 ; 6, 20, 29 janv., 10 févr. 2027 ; 26 oct. et 2 nov. complets ; inscription un mois avant, définitive au paiement."),
               ("Les Ateliers FL Nice", "IRN (A1-B2) avec atelier de 1 h 30", "IRN <strong>175 €</strong> (réinscription 130 €)", "17 déc. 2026 ; 21 janv., 25 févr., 25 mars, 22 avr., 27 mai, 24 juin, 22 juil., 19 août, 23 sept., 21 oct., 18 nov., 16 déc. 2027 ; inscription 4 semaines avant ; attestation 4 semaines après ; tarifs 2027 dès le 1<sup>er</sup> nov. 2026."),
               ("Alliance française Nice Côte d'Azur", "IRN (papier ou ordinateur), tout public, Canada (ordinateur), examen civique", "civique 80 € · TCF : dans le module de réservation", "Dates dans le module en ligne (« tests à venir ») ; examen civique : pré-inscription sur le site de FEI, résultats sous 12 h.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("4 déc.", "prochaine session IRN (FOLAM)", "inscription avant le 9 nov."),
       faq=[("Où passer le TCF Canada à Nice ?", "À l'Alliance française Nice Côte d'Azur, seul centre de la ville à l'annoncer (sur ordinateur, dans ses locaux) ; ses dates et son tarif s'affichent dans son module de réservation en ligne. FOLAM répond « nous contacter » ; Les Ateliers FL ne le proposent pas."),
            ("Combien coûte le TCF à Nice ?", "Relevé du 29 octobre 2026 : TCF IRN 170 € chez FOLAM, 175 € aux Ateliers FL avec un atelier de préparation (130 € en réinscription) ; examen civique 80 € à l'Alliance et chez FOLAM ; l'Alliance affiche ses tarifs TCF dans son module de réservation."),
            ("Comment s'inscrire au TCF à Nice ?", "Un mois à l'avance chez FOLAM (formulaire en ligne, inscription définitive au paiement), quatre semaines avant aux Ateliers FL (pièce d'identité, pas de remboursement), en ligne à l'Alliance. L'examen civique se pré-inscrit sur le site de France Éducation international.")]),
    # ------------------------------------------------------------------ Canada
    mk("tcf-montreal", "Montréal", "ca", ["Montréal"], nearby=["Laval", "Kirkland", "Saint-Constant"],
       title="TCF Canada à Montréal : 7 centres agréés, prix, inscription",
       desc="Les 7 centres TCF agréés à Montréal avec contacts — Alliance Française, Stanislas, UQAM, Concordia… —, leurs règles (prix non publiés, annulation).",

       h1="Passer le TCF Canada à Montréal : les 7 centres agréés, leurs règles et l'inscription",
       intro="""Montréal est la ville la mieux dotée du Canada : <strong>%(n)d centres agréés</strong> par France Éducation
international — Alliance Française de Montréal, Collège Stanislas, UQAM, Université Concordia, Cégep
Marie-Victorin, Centre Yves-Thériault, Collège ELC —, tous avec des sessions sur ordinateur, plus Laval,
Kirkland et Saint-Constant en banlieue. Les tarifs, eux, sont rarement publiés : l'Alliance Française
n'en affiche aucun. Les centres avec leurs contacts, les règles relevées, et l'inscription.""",
       facts=["<strong>7 centres agréés</strong> dans Montréal, 3 en banlieue (Laval, Kirkland, Saint-Constant).",
              "<strong>Alliance Française de Montréal : aucun tarif publié</strong> ; inscription en ligne « dans la limite des places disponibles » ; 75 $ retenus si annulation à plus de 15 jours, rien après.",
              "<strong>Collège Stanislas</strong> : TCF Québec, Canada, tout public et IRN ; 15 $ retenus par épreuve si annulation à plus de 15 jours.",
              "« 20 jours entre deux passations, quel que soit le centre » ; horaires envoyés 7 jours avant, « réserver la journée entière ».",
              "Pour comparer : 440 $ à l'UQTR (Trois-Rivières), 390 $ à Vancouver, 400 $ à Edmonton."],
       releve=[("Alliance Française de Montréal", "Canada, Québec", "<strong>non publié</strong>", "Inscription en ligne selon les places ; une modification, à plus de 15 jours ; annulation 75 $ ; horaires 7 jours avant."),
               ("Collège Stanislas (Outremont)", "Québec, Canada, tout public, IRN", NR, "Paiement complet à l'inscription ; report gratuit à plus de 15 jours ; 15 $ par épreuve retenus si annulation."),
               ("UQAM (francisation) · Concordia · Cégep Marie-Victorin · Centre Yves-Thériault · Collège ELC", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le TCF Canada à Montréal ?", "Dans l'un des sept centres agréés — Alliance Française de Montréal, Collège Stanislas, UQAM, Université Concordia, Cégep Marie-Victorin, Centre Yves-Thériault, Collège ELC — ou en banlieue à Laval, Kirkland et Saint-Constant, tous sur ordinateur. Inscription en ligne, centre par centre."),
            ("Combien coûte le TCF Canada à Montréal ?", "Les grands centres montréalais ne publient pas leur tarif : l'Alliance Française de Montréal n'affiche aucun prix, le montant apparaît à la réservation. Pour repère, 440 $ à l'UQTR, 390 $ à l'Alliance française de Vancouver, 400 $ à Edmonton."),
            ("Peut-on annuler ou reporter une session à Montréal ?", "À l'Alliance Française, une seule modification à plus de 15 jours, et 75 $ retenus en cas d'annulation, rien après ; au Collège Stanislas, report gratuit à plus de 15 jours, 15 $ par épreuve retenus si annulation. Et 20 jours minimum entre deux passations, quel que soit le centre."),
            ("TCF Canada ou TCF Québec à Montréal ?", "Les mêmes centres proposent les deux. Pour un dossier fédéral — Entrée express, citoyenneté —, seul le TCF Canada est accepté ; pour un programme du Québec, le TCF Québec, modulaire, permet de ne passer que les épreuves exigées.")]),
    mk("tcf-toronto", "Toronto", "ca", ["Toronto", "North York", "Mississauga", "Oakville"], h2_label="Toronto et sa banlieue",
       title="TCF Canada à Toronto : 5 centres, sessions, inscription",
       desc="Les 5 centres TCF agréés à Toronto — 4 campus de l'Alliance française (Spadina, North York, Mississauga, Oakville), GB Language —, sessions trimestrielles.",

       h1="Passer le TCF Canada à Toronto : les centres agréés, les sessions et l'inscription",
       intro="""À Toronto, le TCF Canada se passe dans <strong>%(n)d centres agréés</strong> par France Éducation
international : les quatre campus de l'<strong>Alliance française de Toronto</strong> — Spadina, North York,
Mississauga, Oakville — et le GB Language Centre à North York, tous sur ordinateur (papier possible à
l'Alliance). Les sessions de l'Alliance sont <strong>trimestrielles</strong>, l'inscription ouvre un mois
avant à 10 h, et « si une session n'est pas listée, elle est complète ». Les centres, leurs contacts, et
la méthode pour décrocher une place.""",
       facts=["<strong>5 centres agréés</strong> dans la région : AF Toronto (Spadina, North York, Mississauga, Oakville) et GB Language Centre.",
              "<strong>Sessions trimestrielles</strong> à l'Alliance ; inscription ouverte <strong>un mois avant, à 10 h</strong>.",
              "Ouvertures 2027 : <strong>1<sup>er</sup> décembre 2026</strong> (janvier-mars), 2 mars, 20 mai, 17 août 2027.",
              "« If a session is not listed, it is full » ; pas de liste d'attente ; une seule inscription à la fois.",
              "Recorrection supprimée par FEI pour les sessions depuis le 1<sup>er</sup> septembre 2026."],
       releve=[("Alliance française de Toronto (4 campus)", "Canada (papier ou ordinateur), Québec", "<strong>non publié</strong> sur la page TCF", "Trimestriel ; inscription 1 mois avant à 10 h ; 2027 : 1<sup>er</sup> déc. 2026, 2 mars, 20 mai, 17 août ; pas de liste d'attente."),
               ("GB Language Centre (North York)", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le TCF Canada à Toronto ?", "À l'Alliance française de Toronto, sur quatre campus — Spadina (centre-ville), North York, Mississauga, Oakville —, ou au GB Language Centre de North York. L'inscription se fait exclusivement en ligne."),
            ("Quand ouvrent les inscriptions à Toronto ?", "Un mois avant chaque trimestre, à 10 h : pour 2027, le 1er décembre 2026 (sessions de janvier à mars), le 2 mars, le 20 mai et le 17 août 2027. Les places partent en quelques minutes ; sans liste d'attente, revenez régulièrement, des places se libèrent."),
            ("Combien coûte le TCF Canada à Toronto ?", "L'Alliance française de Toronto n'affiche pas de tarif sur sa page TCF ; le prix apparaît à la réservation. Pour repère, 390 $ à Vancouver, 400 $ à Edmonton, 440 $ à l'UQTR."),
            ("Papier ou ordinateur à Toronto ?", "Les deux formats sont proposés à l'Alliance française ; le GB Language Centre déclare des sessions sur ordinateur.")]),
    mk("tcf-quebec-ville", "Québec", "ca", ["Québec"], crumb="TCF à Québec",
       title="TCF Canada à Québec : Stanislas et Université Laval",
       desc="Les 2 centres TCF agréés à Québec : Collège Stanislas (Sainte-Foy, le matin en semaine) et Université Laval (405 $, vendredi-samedi) ; dates et règles.",
       h1="Passer le TCF à Québec : les deux centres agréés et l'inscription",
       intro="""Dans la ville de Québec, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation
international, tous deux sur ordinateur : le <strong>Collège Stanislas</strong> (1605, chemin Sainte-Foy), qui ouvre des
sessions de TCF Canada presque chaque matin de semaine jusqu'au 16 décembre 2026, et l'<strong>École de langues de
l'Université Laval</strong> (pavillon Charles-De Koninck), à <strong>405 $</strong> les quatre épreuves, un vendredi-samedi
par semaine jusqu'au 12 décembre. Attention à la case cochée : seul le TCF Canada sert à Entrée express. Les centres,
leurs dates et leurs règles relevées le 29 octobre 2026, et l'inscription.""",
       facts=["<strong>2 centres agréés</strong> : Collège Stanislas (1605, chemin Sainte-Foy ; 418 527-9998, poste 3239 ; tcfquebec@stanislas.qc.ca) et Université Laval (pavillon Charles-De Koninck, 1030 avenue des Sciences-Humaines).",
              "<strong>Université Laval : 405 $</strong> les quatre épreuves ; séances ouvertes au grand public le 29 octobre 2026 : 20-21 et 27-28 novembre, 4-5 et 11-12 décembre (oral le vendredi, écrits le samedi) ; aucun remboursement ni changement de date.",
              "<strong>Collège Stanislas</strong> : TCF Canada le matin, du lundi au jeudi (et certains samedis), chaque semaine du 2 novembre au 16 décembre 2026 ; TCF Québec les samedis 7 et 21 novembre, 5 et 12 décembre ; tarif non affiché (frais administratifs + frais d'examen, payés à l'inscription).",
              "Stanislas : report ou modification gratuits à plus de 15 jours, annulation remboursée moins 15 $ par épreuve ; à moins de 15 jours, rien, sauf force majeure justifiée ; 20 jours entre deux passations d'une même épreuve, quel que soit le centre.",
              "Université Laval : pièce d'identité avec photo et signature (permis, carte d'assurance-maladie ou passeport — pas la carte étudiante) et reçu d'inscription ; deux blocs : entrevue orale d'environ 20 minutes, puis CO, CE et EE sur ordinateur ; aménagements sur certificat médical envoyé deux mois avant.",
              "Recorrection de l'oral et de l'écrit : suspendue par France Éducation international pour les sessions à partir du 1<sup>er</sup> septembre 2026, « pour une période d'environ 1 an ».",
              "Le TCF Canada est aussi reconnu par le MIFI depuis 2022 ; résultats par e-mail sous 2 à 4 semaines ; attestation valable 2 ans."],
       releve=[("Collège Stanislas (Québec)", "Québec, Canada, tout public (sur demande), IRN", "non affiché (frais administratifs + frais d'examen)", "TCF Canada le matin, lundi-jeudi et certains samedis, du 2 nov. au 16 déc. 2026 ; TCF Québec sam. 7 et 21 nov., 5 et 12 déc. ; inscription en ligne ; 15 $ par épreuve retenus si annulation à plus de 15 jours."),
               ("Université Laval (ELUL)", "Canada, tout public", "Canada <strong>405 $</strong>", "Grand public : 20-21 nov., 27-28 nov., 4-5 déc., 11-12 déc. 2026 (oral le vendredi, écrits le samedi) ; séances réservées à la communauté ULaval en plus ; inscription en ligne (plateforme Brio) ; aucun remboursement.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("405 $", "TCF Canada à l'Université Laval", "relevé du 29 oct. 2026"),
       faq=[("Où passer le TCF Canada à Québec ?", "Au Collège Stanislas (1605, chemin Sainte-Foy) ou à l'École de langues de l'Université Laval (pavillon Charles-De Koninck), tous deux agréés et sur ordinateur ; inscription en ligne sur leur site. Stanislas ouvre des sessions presque tous les matins de semaine, Laval un vendredi-samedi par semaine."),
            ("Combien coûte le TCF à Québec ?", "405 $ les quatre épreuves à l'Université Laval (29 octobre 2026), sans remboursement ni changement de date. Le Collège Stanislas n'affiche pas son tarif : des frais administratifs, jamais remboursés, plus des frais d'examen, payés en entier à l'inscription. À l'UQTR, à Trois-Rivières, le TCF Canada coûte 440 $."),
            ("Quelles dates pour le TCF Canada à Québec ?", "Le 29 octobre 2026 : à Stanislas, chaque semaine du 2 novembre au 16 décembre, du lundi au jeudi le matin, plus les samedis 14 et 28 novembre ; à l'Université Laval, 20-21 novembre, 27-28 novembre, 4-5 décembre et 11-12 décembre, oral le vendredi et écrits le samedi. Les sites des centres font foi."),
            ("TCF Canada ou TCF Québec à Québec ?", "Pour un programme du Québec, les deux sont acceptés ; pour Entrée express ou la citoyenneté, seul le TCF Canada. Le TCF Québec, modulaire, permet de ne passer que les épreuves exigées ; le TCF Canada est insécable : les quatre épreuves ensemble.")]),
    mk("tcf-ottawa", "Ottawa", "ca", ["Ottawa"],
       title="TCF Canada à Ottawa : Alliance française et FrancoLangues",
       desc="Les 2 centres TCF agréés à Ottawa avec contacts — Alliance française Ottawa (papier ou ordinateur), FrancoLangues —, les règles du jour J, l'inscription.",

       h1="Passer le TCF Canada à Ottawa : les deux centres agréés et l'inscription",
       intro="""À Ottawa, le TCF Canada se passe dans <strong>%(n)d centres agréés</strong> par France Éducation
international, tous deux sur ordinateur : l'<strong>Alliance française Ottawa</strong> (352 MacLaren Street),
qui le propose aussi sur papier, et <strong>FrancoLangues</strong> à Kanata. L'Alliance est stricte sur le jour
J — « passeport valide et convocation imprimée, sans exception » — et rend les résultats par e-mail sous
deux à trois semaines. Les centres, leurs contacts, et l'inscription.""",
       facts=["<strong>2 centres agréés</strong> : Alliance française Ottawa et FrancoLangues (Kanata).",
              "<strong>Alliance française Ottawa</strong> : TCF Canada sur ordinateur ou sur papier ; passeport valide et convocation imprimée obligatoires, « aucune exception ».",
              "Résultats par e-mail sous 2 à 3 semaines ; aucun duplicata de l'attestation.",
              "Aménagements : à demander avant l'inscription, avec justificatif médical.",
              "Recorrection supprimée par FEI depuis les sessions du 1<sup>er</sup> septembre 2026."],
       releve=[("Alliance française Ottawa", "Canada (ordinateur ou papier), autres déclinaisons", NR, "Passeport + convocation imprimée obligatoires ; identité contrôlée pendant l'épreuve ; résultats 2-3 semaines."),
               ("FrancoLangues", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le TCF Canada à Ottawa ?", "À l'Alliance française Ottawa (352 MacLaren Street), sur ordinateur ou sur papier, ou chez FrancoLangues à Kanata, tous deux agréés."),
            ("Que faut-il apporter le jour de l'examen à Ottawa ?", "Un passeport valide et la convocation imprimée : l'Alliance française refuse l'accès sans les deux, « sans exception », et contrôle l'identité pendant toute l'épreuve."),
            ("Combien coûte le TCF Canada à Ottawa ?", "L'Alliance française Ottawa ne publie pas le tarif sur sa page TCF ; pour repère, 390 $ à Vancouver, 400 $ à Edmonton, 440 $ à l'UQTR.")]),
    mk("tcf-vancouver", "Vancouver", "ca", ["Vancouver", "New Westminster"], h2_label="Vancouver et New Westminster",
       title="TCF Canada à Vancouver : centres, prix (390 $), inscription",
       desc="Les 3 centres TCF agréés à Vancouver et New Westminster avec contacts — Alliance française Canada Pacific (390 $), Ashton —, des sessions vite complètes.",

       h1="Passer le TCF Canada à Vancouver : les centres agréés, le prix et l'inscription",
       intro="""À Vancouver, le TCF Canada se passe dans <strong>%(n)d centres agréés</strong> par France Éducation
international, tous sur ordinateur : l'<strong>Alliance française Canada Pacific</strong> — Cambie Street,
et un second site à New Westminster — et Ashton Testing Services. L'Alliance affiche <strong>390 $</strong>,
10 %% de remise aux membres, aucun remboursement, et le 17 septembre 2026 <strong>toutes ses sessions
listées étaient « SOLD OUT »</strong>. Les centres, leurs contacts, et la méthode pour obtenir une place.""",
       facts=["<strong>3 centres agréés</strong> : Alliance française Canada Pacific (Vancouver et New Westminster), Ashton Testing Services.",
              "<strong>Alliance française : 390 $</strong>, 10 % pour les membres ; inscription en ligne seulement, « définitive, ni remboursement ni crédit ».",
              "Toutes les sessions listées « SOLD OUT » le 17 septembre 2026 : connectez-vous à l'ouverture, un seul onglet, passeport sous la main.",
              "Résultats par e-mail sous 3 à 4 semaines ; clavier QWERTY, accents via la plateforme de FEI.",
              "Victoria compte deux autres centres agréés (Alliance française de Victoria, Université de Victoria)."],
       releve=[("Alliance française Canada Pacific", "Canada (+ TEF)", "<strong>390 $</strong> (351 $ membres)", "Inscription en ligne seulement, définitive ; sessions complètes ; résultats 3-4 semaines ; QWERTY."),
               ("Ashton Testing Services", NR, NR, "Centre de tests privé, sur ordinateur.")],
       faq=[("Où passer le TCF Canada à Vancouver ?", "À l'Alliance française Canada Pacific (6161 Cambie Street, et New Westminster) ou chez Ashton Testing Services, tous agréés et sur ordinateur ; inscription en ligne, centre par centre."),
            ("Combien coûte le TCF Canada à Vancouver ?", "390 $ à l'Alliance française Canada Pacific le 17 septembre 2026 (351 $ pour les membres), « prices are subject to change without notice » ; Ashton ne publie pas de tarif lisible."),
            ("Comment obtenir une place à Vancouver ?", "En s'inscrivant à l'ouverture : l'Alliance conseille de se connecter à l'avance avec son numéro de passeport prêt et de n'ouvrir qu'un seul onglet — « opening multiple tabs or repeatedly refreshing the page may cancel your reservation ».")]),
    # ------------------------------------------------------------------ Algérie
    mk("tcf-alger", "Alger", "dz", ["Alger"],
       title="TCF Alger 2026 : rendez-vous IFAL, TCF Canada 37 500 DA",
       desc="TCF à Alger : rendez-vous sur la plateforme IFAL (VFS), tarifs 2026 — Canada 37 500 DA, DAP 19 500, tout public 13 000 —, centre de Hydra, faux site.",
       h1="Passer le TCF à Alger : l'antenne de l'Institut français à Hydra et l'inscription",
       intro="""À Alger, le TCF — Canada, Québec, IRN, tout public, DAP — se passe dans <strong>un seul centre agréé</strong>
par France Éducation international : l'antenne de l'<strong>Institut français d'Algérie à Hydra</strong>, 30,
rue des Frères-Kadri, avec des sessions sur ordinateur. Le rendez-vous se prend exclusivement en ligne, sur la
plateforme IFAL opérée par VFS Global (assistance : 021 99 60 08), et le TCF Canada coûte <strong>37 500 DA</strong>,
tarif commun aux cinq antennes le 17 octobre 2026. C'est aussi ici que se passe l'examen civique français
(9 000 DA). Le centre, ses tarifs, l'inscription — et le faux site à éviter.""",
       facts=["<strong>1 centre agréé</strong> : Institut français d'Algérie, antenne d'Alger, 30 rue des Frères-Kadri, Hydra.",
              "Rendez-vous <strong>en ligne uniquement</strong> sur la plateforme IFAL (VFS Global), depuis if-algerie.com ; assistance VFS : info.tcfalg@vfshelpline.com, 021 99 60 08.",
              "Tarifs TTC : <strong>TCF Canada et TCF Québec 37 500 DA</strong>, TCF DAP 19 500 DA, TCF tout public 13 000 DA (17 octobre 2026).",
              "Sessions <strong>chaque mois</strong> ; <strong>26 jours</strong> entre deux inscriptions selon la page nationale, 36 selon les quatre autres antennes. TCF Canada sur deux jours : l'oral le lendemain des épreuves collectives.",
              "<strong>Examen civique</strong> au même centre : 9 000 DA, pré-inscription sur test-civique.fr, paiement CB/Dahabia sur place ou virement.",
              "⚠️ <strong>if-algerie.fr est une escroquerie</strong> ; l'officiel est if-algerie.com."],
       releve=[("Institut français d'Algérie — antenne d'Alger (Hydra)", "Canada, Québec, IRN, tout public, DAP ; examen civique", "Canada, Québec <strong>37 500 DA</strong> · DAP 19 500 DA · tout public 13 000 DA (examen civique 9 000 DA, relevé le 17 sept.)", "Plateforme IFAL, sessions mensuelles ; TCF Canada sur deux jours consécutifs, convocation à l'oral remise le premier jour ; inscription avec un permis de conduire annulée sans remboursement ; attestation par e-mail, aucune version papier depuis mars 2023.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       releve_note="""<p>Le 17 octobre 2026, la page TCF de l'antenne d'Alger restait bloquée au chargement : ses tarifs et
ses règles ont été lus dans le contenu qu'elle charge (mis à jour le 23 août 2026). Les mêmes montants s'affichent en
clair sur les pages d'Oran, de Constantine, d'Annaba et de Tlemcen.</p>""",
       stat3=("37 500 DA", "TCF Canada", "tarif des 5 antennes, 17 oct. 2026"),
       faq=[("Où passer le TCF Canada à Alger ?", "À l'antenne de l'Institut français d'Algérie à Hydra (30, rue des Frères-Kadri), seul centre agréé d'Alger. Les autres antennes agréées sont Oran, Constantine, Annaba et Tlemcen."),
            ("Comment prendre rendez-vous pour le TCF à Alger ?", "Uniquement en ligne, sur la plateforme IFAL (forms.vfsglobal.com.dz/IFAL), depuis la page TCF de if-algerie.com : compte, choix de la déclinaison et de la session, paiement en ligne. « Les inscriptions et les paiements se font exclusivement en ligne » ; assistance VFS : info.tcfalg@vfshelpline.com, 021 99 60 08."),
            ("Combien coûte le TCF à Alger ?", "37 500 DA pour le TCF Canada et le TCF Québec, 19 500 DA pour le TCF DAP, 13 000 DA pour le TCF tout public : ce sont les tarifs TTC communs aux antennes de l'Institut français d'Algérie au 17 octobre 2026, et ils se paient en ligne sur la plateforme IFAL. Les 70 000 à 100 000 DA qui circulent sont ceux du faux site if-algerie.fr."),
            ("Qu'est-ce que le TCF DAP ?", "Le TCF de la demande d'admission préalable : selon l'Institut, il s'adresse à « toute personne étrangère de plus de 16 ans » qui veut entrer en licence 1 ou dans une école d'architecture en France. À Alger : quatre épreuves (compréhension orale, structures de la langue, compréhension écrite, expression écrite), 2 h 25, 19 500 DA."),
            ("Que veut dire « TCF SO » ?", "« SO » signifie « sur ordinateur » : le test se passe sur les postes du centre, et non sur papier. Les cinq antennes de l'Institut français d'Algérie figurent avec l'option « sessions sur ordinateur » dans la liste de France Éducation international ; les épreuves sont les mêmes."),
            ("Combien de jours entre deux inscriptions au TCF ?", "26 jours selon la page TCF nationale de l'Institut français d'Algérie ; les pages des antennes d'Oran, Constantine, Annaba et Tlemcen écrivent 36 jours (17 octobre 2026). Par prudence, laissez 36 jours entre deux réservations."),
            ("Quelle pièce d'identité apporter ?", "Carte d'identité biométrique ou passeport biométrique pour les Algériens ; passeport biométrique ou carte consulaire pour les autres nationalités. « L'inscription avec le permis de conduire est annulée et aucun remboursement n'est possible », précise l'antenne d'Alger."),
            ("Peut-on passer l'examen civique à Alger ?", "Oui, au même centre : pré-inscription sur test-civique.fr via le lien de l'Institut, 9 000 DA par carte bancaire ou Dahabia sur place ou par virement, confirmation sous 48 heures, convocation par e-mail.")]),
    mk("tcf-oran", "Oran", "dz", ["Oran"],
       title="TCF Oran 2026 : rendez-vous IFAL, TCF Canada 37 500 DA",
       desc="TCF à Oran : rendez-vous sur la plateforme IFAL (VFS), tarifs 2026 — Canada 37 500 DA, DAP 19 500, tout public 13 000 —, examen à l'USTO, sessions.",
       h1="Passer le TCF à Oran : l'antenne de l'Institut français et l'inscription",
       intro="""À Oran, le TCF — Canada, Québec, IRN, tout public, DAP — se passe dans <strong>un seul centre agréé</strong>
par France Éducation international : l'antenne de l'<strong>Institut français d'Algérie</strong>, 112, rue
Larbi-Ben-M'hidi, avec des sessions sur ordinateur. Le rendez-vous se prend exclusivement en ligne, sur la
plateforme IFAL opérée par VFS Global, avec des sessions ouvertes chaque mois ; selon la page de l'antenne relue
le 17 octobre 2026, le TCF Canada coûte <strong>37 500 DA</strong> et se passe à l'« ELS USTO ». Le centre, ses
tarifs, et l'inscription.""",
       facts=["<strong>1 centre agréé</strong> : Institut français d'Algérie, antenne d'Oran, 112 rue Larbi-Ben-M'hidi.",
              "Lieu de passation indiqué pour le TCF Canada : « <strong>Institut Français d'Oran, ELS USTO</strong> ».",
              "Rendez-vous <strong>en ligne uniquement</strong> sur la plateforme IFAL (VFS Global), depuis if-algerie.com ; assistance VFS : info.tcfalg@vfshelpline.com, 021 99 60 08.",
              "Tarifs TTC : <strong>TCF Canada 37 500 DA</strong>, TCF DAP 19 500 DA, TCF tout public 13 000 DA (17 octobre 2026).",
              "Sessions <strong>chaque mois</strong> ; <strong>36 jours</strong> entre deux inscriptions selon la page de l'antenne (26 sur la page nationale).",
              "⚠️ if-algerie.fr est une escroquerie ; l'officiel est if-algerie.com."],
       releve=[("Institut français d'Algérie — antenne d'Oran", "Canada, Québec, IRN, tout public, DAP", "Canada <strong>37 500 DA</strong> · DAP 19 500 DA · tout public 13 000 DA", "Plateforme IFAL, sessions mensuelles, 36 jours entre deux inscriptions ; passation du TCF Canada à l'ELS USTO ; examens.oran@if-algerie.com, 041 70 73 73.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       stat3=("37 500 DA", "TCF Canada", "tarif de l'antenne, 17 oct. 2026"),
       faq=[("Où passer le TCF Canada à Oran ?", "Auprès de l'antenne de l'Institut français d'Algérie d'Oran (112, rue Larbi-Ben-M'hidi), seul centre agréé de la ville. Le 17 octobre 2026, sa page indiquait comme lieu de passation du TCF Canada « Institut Français d'Oran, ELS USTO » : vérifiez l'adresse sur votre convocation."),
            ("Comment prendre rendez-vous pour le TCF à Oran ?", "Exclusivement en ligne, sur la plateforme IFAL (VFS Global), depuis la page TCF de l'antenne sur if-algerie.com — bouton « M'inscrire au TCF Canada ». Aucune inscription sur place. Assistance VFS : info.tcfalg@vfshelpline.com, 021 99 60 08."),
            ("Combien coûte le TCF à Oran ?", "37 500 DA TTC pour le TCF Canada, 19 500 DA pour le TCF DAP, 13 000 DA pour le TCF tout public, selon la page de l'antenne relue le 17 octobre 2026 ; le paiement se fait en ligne, sur la plateforme IFAL."),
            ("Où trouver le calendrier du TCF à Oran ?", "L'Institut ne publie pas de calendrier : « des sessions TCF sont ouvertes tous les mois sur les cinq antennes », et les dates s'affichent sur la plateforme IFAL au moment de réserver. Laissez 36 jours entre deux inscriptions, délai écrit sur la page de l'antenne d'Oran."),
            ("Que veut dire « TCF SO » ?", "« SO » signifie « sur ordinateur » : le test se passe sur les postes du centre, et non sur papier. L'antenne d'Oran figure avec l'option « sessions sur ordinateur » dans la liste de France Éducation international.")]),
    mk("tcf-constantine", "Constantine", "dz", ["Constantine"],
       title="TCF Constantine 2026 : rendez-vous IFAL, Canada 37 500 DA",
       desc="TCF à Constantine : rendez-vous IFAL (VFS), tarifs 2026 — Canada 37 500 DA, DAP 19 500, IRN 14 000 —, examen à Ali Mendjeli, 36 jours entre 2 inscriptions.",
       h1="Passer le TCF à Constantine : l'antenne de l'Institut français et l'inscription",
       intro="""À Constantine, le TCF — Canada, Québec, IRN, tout public, DAP — se passe dans <strong>un seul centre
agréé</strong> par France Éducation international : l'antenne de l'<strong>Institut français d'Algérie</strong>,
1, boulevard de l'Indépendance, avec des sessions sur ordinateur. Le rendez-vous se prend exclusivement en
ligne, sur la plateforme IFAL opérée par VFS Global ; selon la page de l'antenne relue le 17 octobre 2026, le
TCF Canada coûte <strong>37 500 DA</strong> et se passe à l'<strong>annexe de la Nouvelle ville Ali Mendjeli</strong>.
Le centre, ses tarifs, et l'inscription.""",
       facts=["<strong>1 centre agréé</strong> : Institut français d'Algérie, antenne de Constantine, 1 boulevard de l'Indépendance.",
              "Lieu de passation : <strong>annexe Nouvelle ville Ali Mendjeli</strong>, UV7, lot n° 52 (station de tramway El Istiklel).",
              "Rendez-vous <strong>en ligne uniquement</strong> sur la plateforme IFAL (VFS Global) ; assistance VFS : info.tcfalg@vfshelpline.com, +213 21 99 88 03 ; autres questions : examens.constantine@if-algerie.com.",
              "Tarifs : <strong>TCF Canada et TCF Québec 37 500 DA</strong>, TCF DAP 19 500 DA, TCF IRN 14 000 DA, TCF tout public 13 000 DA (17 octobre 2026).",
              "Sessions <strong>chaque mois</strong> ; <strong>36 jours</strong> entre deux inscriptions selon la page de l'antenne (26 sur la page nationale).",
              "⚠️ if-algerie.fr est une escroquerie ; l'officiel est if-algerie.com."],
       releve=[("Institut français d'Algérie — antenne de Constantine", "Canada, Québec, IRN, tout public, DAP", "Canada, Québec <strong>37 500 DA</strong> · DAP 19 500 DA · IRN 14 000 DA · tout public 13 000 DA", "Plateforme IFAL, sessions mensuelles, 36 jours entre deux inscriptions ; passation à l'annexe d'Ali Mendjeli ; attestation par e-mail.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       stat3=("37 500 DA", "TCF Canada", "tarif de l'antenne, 17 oct. 2026"),
       faq=[("Où passer le TCF Canada à Constantine ?", "Auprès de l'antenne de l'Institut français d'Algérie de Constantine (1, boulevard de l'Indépendance), seul centre agréé de la ville ; l'examen lui-même se passe à l'annexe de la Nouvelle ville Ali Mendjeli (UV7, lot n° 52, station de tramway El Istiklel), selon la page de l'antenne relue le 17 octobre 2026."),
            ("Comment s'inscrire au TCF à Constantine ?", "Exclusivement en ligne, sur la plateforme IFAL (VFS Global), depuis la page TCF de if-algerie.com. Pour la prise de rendez-vous, l'antenne renvoie à l'assistance VFS (info.tcfalg@vfshelpline.com, +213 21 99 88 03) ; pour le reste, à examens.constantine@if-algerie.com."),
            ("Combien coûte le TCF à Constantine ?", "37 500 DA pour le TCF Canada et le TCF Québec, 19 500 DA pour le TCF DAP, 14 000 DA pour le TCF IRN, 13 000 DA pour le TCF tout public, selon la page de l'antenne relue le 17 octobre 2026."),
            ("Qu'est-ce que le TCF DAP ?", "Le TCF de la demande d'admission préalable, pour entrer en licence 1 ou dans une école d'architecture en France : selon l'Institut, il s'adresse à « toute personne étrangère de plus de 16 ans ». À Constantine, il coûte 19 500 DA et se réserve, comme les autres déclinaisons, sur la plateforme IFAL."),
            ("Combien de jours entre deux inscriptions ?", "36 jours, selon la page de l'antenne de Constantine relue le 17 octobre 2026 ; la page nationale de l'Institut écrit 26. Par prudence, comptez 36 jours.")]),
    mk("tcf-annaba", "Annaba", "dz", ["Annaba"],
       title="TCF Annaba 2026 : rendez-vous IFAL, TCF Canada 37 500 DA",
       desc="TCF à Annaba : rendez-vous sur la plateforme IFAL (VFS), TCF Canada 37 500 DA, DAP 19 500, tout public 13 000, examen au « Majestic », 36 jours.",
       h1="Passer le TCF à Annaba : l'antenne de l'Institut français et l'inscription",
       intro="""À Annaba, le TCF — Canada, Québec, IRN, tout public, DAP — se passe dans <strong>un seul centre agréé</strong>
par France Éducation international : l'antenne de l'<strong>Institut français d'Algérie</strong>, 8, boulevard du
1<sup>er</sup>-Novembre (adresse de la liste FEI relue le 29 octobre 2026 ; en septembre, elle indiquait 6, route de
l'Avant-Port), avec des sessions sur ordinateur. Le rendez-vous se prend exclusivement en ligne, sur la plateforme IFAL
opérée par VFS Global. Le 29 octobre 2026, les pages de l'antenne affichaient <strong>37 500 DA</strong> pour le TCF
Canada, 19 500 DA pour le DAP, 13 000 DA pour le tout public, et un même lieu de passation : l'Institut français
d'Annaba, « Majestic ». Le centre, ses contacts, la recorrection (suspendue), et l'inscription.""",
       facts=["<strong>1 centre agréé</strong> : Institut français d'Algérie, antenne d'Annaba, 8 boulevard du 1<sup>er</sup>-Novembre (liste FEI du 29 octobre 2026) ; l'antenne indique aussi le 038 45 12 49 et examens.annaba@if-algerie.com.",
              "Lieu de passation indiqué pour le TCF Canada, le DAP et le tout public : « <strong>Institut Français d'Annaba, Majestic</strong> ».",
              "Rendez-vous <strong>en ligne uniquement</strong> sur la plateforme IFAL (VFS Global), depuis if-algerie.com ; assistance VFS : info.tcfalg@vfshelpline.com, 021 99 60 08.",
              "Tarifs TTC affichés par l'antenne le 29 octobre 2026 : <strong>TCF Canada 37 500 DA</strong> (4 épreuves, 2 h 47), TCF DAP 19 500 DA (2 h 25), TCF tout public 13 000 DA (3 épreuves QCM) ; IRN et Québec sans prix affiché.",
              "Sessions <strong>chaque mois</strong> ; <strong>36 jours</strong> entre deux inscriptions selon la page de l'antenne (26 sur la page nationale) ; sa rubrique « Calendrier » était vide le 29 octobre.",
              "Recorrection de l'écrit ou de l'oral du TCF Canada : la procédure de l'antenne (demande dans le mois, 11 000 DA par épreuve, 10 000 DA rendus si la note change) est <strong>suspendue</strong> — FEI n'accepte plus de demande pour les sessions à partir du 1<sup>er</sup> septembre 2026, « pour une période d'environ 1 an » (relu le 29 octobre).",
              "⚠️ if-algerie.fr est une escroquerie ; l'officiel est if-algerie.com."],
       releve=[("Institut français d'Algérie — antenne d'Annaba", "Canada, Québec, IRN, tout public, DAP", "Canada <strong>37 500 DA</strong> · DAP 19 500 DA · tout public 13 000 DA · IRN, Québec : non affiché", "Plateforme IFAL, sessions mensuelles, 36 jours entre deux inscriptions ; passation au « Majestic » ; rubrique calendrier vide ; recorrection écrit/oral (11 000 DA par épreuve) suspendue par FEI pour les sessions dès le 1<sup>er</sup> septembre 2026.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("37 500 DA", "TCF Canada", "tarif de l'antenne, 29 oct. 2026"),
       faq=[("Où passer le TCF Canada à Annaba ?", "Auprès de l'antenne de l'Institut français d'Algérie d'Annaba, seul centre agréé de la ville. La liste FEI relue le 29 octobre 2026 la situe au 8, boulevard du 1er-Novembre (sa liste de septembre : 6, route de l'Avant-Port) ; les pages de l'antenne indiquent comme lieu de passation « Institut Français d'Annaba, Majestic » : vérifiez l'adresse sur votre convocation."),
            ("Comment s'inscrire au TCF à Annaba ?", "Exclusivement en ligne, sur la plateforme IFAL (VFS Global), depuis la page TCF de if-algerie.com, avec une carte d'identité biométrique ou un passeport (passeport biométrique ou carte consulaire pour les étrangers). Assistance VFS : info.tcfalg@vfshelpline.com, 021 99 60 08 ; pour le reste, examens.annaba@if-algerie.com ou 038 45 12 49."),
            ("Combien coûte le TCF à Annaba ?", "37 500 DA TTC pour le TCF Canada, 19 500 DA pour le TCF DAP et 13 000 DA pour le TCF tout public, selon les pages de l'antenne relues le 29 octobre 2026 ; l'IRN et le Québec n'y affichent pas de prix (Constantine et Tlemcen, le 17 octobre : 37 500 DA pour le Québec, 14 000 DA pour l'IRN). Le montant exact s'affiche sur la plateforme IFAL au moment de payer."),
            ("Peut-on faire recorriger son TCF Canada à Annaba ?", "Pas pour l'instant : France Éducation international n'accepte plus de demande de recorrection des épreuves d'expression orale et écrite pour les sessions du TCF à partir du 1er septembre 2026, « pour une période d'environ 1 an » (avis sur sa page TCF Canada, relu le 29 octobre 2026) ; les QCM, corrigés par FEI, ne se contestent jamais. La procédure de l'antenne d'Annaba, toujours publiée, s'appliquera de nouveau ensuite : demande dans le mois qui suit les résultats, au service des examens (au Majestic), du dimanche au jeudi, en personne ou par un mandataire muni d'une procuration légalisée — formulaire, attestation finale, pièce d'identité, RIP ou RIB, 11 000 DA par épreuve ; réponse en 3 à 4 semaines, parfois 6 ; si la note change, à la hausse comme à la baisse, 10 000 DA sont remboursés par virement et une nouvelle attestation remplace l'ancienne."),
            ("Combien de jours entre deux inscriptions ?", "36 jours, selon la page de l'antenne d'Annaba relue le 29 octobre 2026 ; la page nationale de l'Institut écrit 26. Par prudence, comptez 36 jours.")]),
    mk("tcf-tlemcen", "Tlemcen", "dz", ["Tlemcen"],
       title="TCF Tlemcen 2026 : rendez-vous IFAL, TCF Canada 37 500 DA",
       desc="TCF à Tlemcen : rendez-vous IFAL (VFS), tarifs 2026 — Canada 37 500 DA, DAP 19 500, IRN 14 000, tout public 13 000 —, lieu d'examen, 36 jours.",
       h1="Passer le TCF à Tlemcen : l'antenne de l'Institut français et l'inscription",
       intro="""À Tlemcen, le TCF — Canada, Québec, IRN, tout public, DAP — se passe dans <strong>un seul centre agréé</strong>
par France Éducation international : l'antenne de l'<strong>Institut français d'Algérie</strong>, 1, rue du
Commandant-Djaber, avec des sessions sur ordinateur. Le rendez-vous se prend exclusivement en ligne, sur la
plateforme IFAL opérée par VFS Global ; selon la page de l'antenne relue le 17 octobre 2026, le TCF Canada coûte
<strong>37 500 DA</strong> et se passe au 45, boulevard Dergal-Abdelkader (Imam Ali). Le centre, ses tarifs, et
l'inscription.""",
       facts=["<strong>1 centre agréé</strong> : Institut français d'Algérie, antenne de Tlemcen, 1 rue du Commandant-Djaber.",
              "Lieu de passation : <strong>45, boulevard Dergal-Abdelkader</strong> (Imam Ali), résidence Yasmine, Imama.",
              "Rendez-vous <strong>en ligne uniquement</strong> sur la plateforme IFAL (VFS Global) ; assistance VFS : info.tcfalg@vfshelpline.com, +213 21 99 88 03 ; autres questions : examens.tlemcen@if-algerie.com.",
              "Tarifs : <strong>TCF Canada et TCF Québec 37 500 DA</strong>, TCF DAP 19 500 DA, TCF IRN 14 000 DA, TCF tout public 13 000 DA (17 octobre 2026).",
              "TCF Canada sur <strong>toute la journée</strong> : l'oral à partir de 12 h si vous êtes convoqué à 9 h 30, à partir de 9 h si vous l'êtes à 14 h 30.",
              "Sessions <strong>chaque mois</strong> ; <strong>36 jours</strong> entre deux inscriptions selon la page de l'antenne (26 sur la page nationale)."],
       releve=[("Institut français d'Algérie — antenne de Tlemcen", "Canada, Québec, IRN, tout public, DAP", "Canada, Québec <strong>37 500 DA</strong> · DAP 19 500 DA · IRN 14 000 DA · tout public 13 000 DA", "Plateforme IFAL, sessions mensuelles, 36 jours entre deux inscriptions ; passation boulevard Dergal-Abdelkader ; attestation par e-mail.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       stat3=("37 500 DA", "TCF Canada", "tarif de l'antenne, 17 oct. 2026"),
       faq=[("Où passer le TCF Canada à Tlemcen ?", "Auprès de l'antenne de l'Institut français d'Algérie de Tlemcen (1, rue du Commandant-Djaber), seul centre agréé de la ville ; l'examen se passe au 45, boulevard Dergal-Abdelkader (Imam Ali), résidence Yasmine, selon la page de l'antenne relue le 17 octobre 2026."),
            ("Comment s'inscrire au TCF à Tlemcen ?", "Exclusivement en ligne, sur la plateforme IFAL (VFS Global), depuis la page TCF de if-algerie.com. Assistance VFS : info.tcfalg@vfshelpline.com, +213 21 99 88 03 ; pour le reste, examens.tlemcen@if-algerie.com."),
            ("Combien coûte le TCF à Tlemcen ?", "37 500 DA pour le TCF Canada et le TCF Québec, 19 500 DA pour le TCF DAP, 14 000 DA pour le TCF IRN, 13 000 DA pour le TCF tout public — rubrique « Tarifs TCF » de l'antenne, relue le 17 octobre 2026."),
            ("Combien de temps dure le TCF Canada à Tlemcen ?", "Toute la journée : l'antenne convoque à 9 h 30 ou à 14 h 30 pour les épreuves collectives, et l'expression orale a lieu l'après-midi à partir de 12 h dans le premier cas, le matin à partir de 9 h dans le second."),
            ("Combien de jours entre deux inscriptions ?", "36 jours, selon la page de l'antenne de Tlemcen relue le 17 octobre 2026 ; la page nationale de l'Institut écrit 26. Par prudence, comptez 36 jours.")]),
    # ------------------------------------------------------------------ Maroc
    mk("tcf-casablanca", "Casablanca", "ma", ["Casablanca"], nearby=["Béni Mellal"],
       title="TCF Casablanca 2026 : 2 900 Dhs, dates, inscription en ligne",
       desc="TCF Canada à Casablanca : 2 900 Dhs sur ordinateur, sessions du 3 novembre au 8 décembre 2026, Béni Mellal, janvier 2027, inscription en ligne, règles.",
       h1="Passer le TCF Canada à Casablanca : l'Institut français, le prix et les dates",
       intro="""À Casablanca, le TCF se passe à l'<strong>Institut français</strong>, 123 boulevard Zerktouni — seul centre
agréé de la ville, qui gère aussi les sessions de Béni Mellal —, sur ordinateur, au centre de langue de
Mers Sultan (1, rue Dunkerque). Le 17 octobre 2026, son site listait des sessions de TCF Canada à
<strong>2 900 Dhs</strong> du <strong>3 novembre au 8 décembre</strong>, deux à Béni Mellal et déjà cinq dates en
janvier 2027 ; le 28 novembre affichait complet. Le centre, ses contacts, le relevé, et l'inscription en
ligne.""",
       facts=["<strong>1 centre agréé</strong> : Institut français de Casablanca, 123 boulevard Zerktouni ; sessions au centre de langue de Mers Sultan, 1 rue Dunkerque (+ Béni Mellal, Universal Sup).",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; TCF Québec et TEF Canada 2 900 Dhs ; TCF IRN et tout public 1 900 Dhs.",
              "Sessions ouvertes le 17 octobre 2026 : <strong>3 (8 h 30), 5, 10 et 17 novembre, 1<sup>er</sup>, 3 et 8 décembre</strong> ; 28 novembre complet ; 2027 : 5, 7, 12, 16 et 19 janvier.",
              "Béni Mellal : <strong>14 novembre et 12 décembre</strong> (24 octobre complet), à réserver sur le site de Casablanca.",
              "Moins de 20 jours entre deux TCF, toutes versions confondues : inscription annulée sans remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français de Casablanca", "Canada, Québec, IRN (sur place), tout public, TEF Canada", "Canada <strong>2 900 Dhs</strong> · IRN et TP 1 900 Dhs", "3 (8 h 30 ; 10 h complet), 5, 10, 17 nov., 1<sup>er</sup>, 3, 8 déc. 2026 ; 28 nov. complet ; janvier 2027 en ligne ; panier ; convocation dès l'inscription."),
               ("Béni Mellal (Universal Sup, via Casablanca)", "Canada", "2 900 Dhs", "14 nov. et 12 déc. 2026 ; 24 oct. complet.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       stat3=("3 nov.", "prochaine date ouverte", "relevé du 17 oct. 2026"),
       faq=[("Où passer le TCF Canada à Casablanca ?", "À l'Institut français de Casablanca, seul centre agréé de la ville — sur ordinateur, au centre de langue de Mers Sultan (1, rue Dunkerque), à 2 900 dirhams. Le même site vend les sessions de Béni Mellal (Universal Sup)."),
            ("Comment s'inscrire au TCF Canada à Casablanca ?", "En ligne, sur if-maroc.org/casablanca, page TCF Canada : la liste montre les dates ouvertes, on ajoute au panier et on paie. Le TCF IRN, lui, s'inscrit à l'accueil."),
            ("Combien coûte le TCF à Casablanca ?", "2 900 dirhams pour le TCF Canada, le TCF Québec et le TEF Canada ; 1 900 dirhams pour le TCF IRN et le tout public (catalogue de l'Institut français de Casablanca, 17 octobre 2026)."),
            ("Quelles dates pour le TCF Canada à Casablanca ?", "Le 17 octobre 2026, le site listait les 3 (8 h 30), 5, 10 et 17 novembre, et les 1er, 3 et 8 décembre ; le 28 novembre était complet, et cinq dates de janvier 2027 étaient déjà en ligne (5, 7, 12, 16 et 19 janvier). À Béni Mellal : 14 novembre et 12 décembre. La page du site fait foi."),
            ("Combien de jours entre deux TCF ?", "Vingt au minimum : « Le candidat ne peut se présenter deux fois à un test du TCF toute version confondue dans un délai inférieur à 20 jours », sinon l'inscription est annulée sans remboursement.")]),
    mk("tcf-rabat", "Rabat", "ma", ["Rabat"], nearby=["Kenitra"],
       title="TCF Rabat 2026 : 2 900 Dhs, 8 dates oct.-déc., inscription",
       desc="TCF Canada à Rabat : 2 900 Dhs à l'Institut français (15 rue Al Madina), 5 sessions du 13 novembre au 10 décembre 2026, 9 h-17 h, inscription en ligne.",
       h1="Passer le TCF Canada à Rabat : l'Institut français, le prix et les dates",
       intro="""À Rabat, le TCF se passe à l'<strong>Institut français</strong>, 15 rue Al Madina (quartier Hassan) — seul
centre agréé de la ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada. Le 29 octobre 2026,
son site vendait <strong>cinq sessions</strong>, du 13 novembre au 10 décembre, en journée entière (9 h-17 h) ; les
trois dates d'octobre sont passées. Kénitra, à 40 km, a son propre Institut, et onze dates en vente. Le centre,
ses horaires, le relevé, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> à Rabat : Institut français, 15 rue Al Madina, Hassan (derrière le lycée Hassan-II), où se passent les sessions ; Kénitra à 40 km.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; IRN et tout public 1 900 Dhs.",
              "<strong>5 sessions en vente</strong> le 29 octobre 2026 : 13, 19 et 24 novembre, 4 et 10 décembre, de 9 h à 17 h ; aucune n'affiche complet.",
              "<a href=\"/centres/tcf-kenitra/\">Kénitra</a> : 10, 13, 17, 20 et 25 novembre, 1<sup>er</sup>, 3, 8, 11, 15 et 18 décembre (9 h-14 h).",
              "Accueil de l'Institut (1 rue Abou-Inane, tram Place Al Joulane) : fermé le lundi, ouvert du mardi au vendredi 9 h-13 h et 14 h-18 h, le samedi 9 h-13 h et 14 h-17 h ; 05 37 68 96 50 ; le TCF IRN s'inscrit sur place.",
              "Moins de 20 jours entre deux TCF : inscription annulée sans remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français de Rabat", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong> · IRN et TP 1 900 Dhs", "13, 19, 24 nov., 4, 10 déc. 2026, 9 h-17 h, 15 rue Al Madina ; aucune date complète ; panier en ligne."),
               ("Institut français de Kénitra", "Canada, Québec, IRN, tout public", "2 900 Dhs", "10, 13, 17, 20, 25 nov. ; 1<sup>er</sup>, 3, 8, 11, 15, 18 déc. 2026, 9 h-14 h.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("13 nov.", "prochaine session", "5 dates en vente au 29 oct."),
       faq=[("Où passer le TCF Canada à Rabat ?", "À l'Institut français de Rabat, 15 rue Al Madina (quartier Hassan, derrière le lycée Hassan-II), seul centre agréé de la ville, sur ordinateur à 2 900 dirhams ; l'Institut de Kénitra est à 40 km."),
            ("Quelles dates pour le TCF Canada à Rabat ?", "Le 29 octobre 2026, cinq sessions étaient en vente : 13, 19 et 24 novembre, 4 et 10 décembre, de 9 h à 17 h, aucune complète. À Kénitra, onze dates jusqu'au 18 décembre. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à Rabat ?", "En ligne, sur if-maroc.org/rabat, page TCF Canada : choix de la session, panier, paiement ; le TCF IRN s'inscrit à l'accueil, fermé le lundi, ouvert du mardi au samedi."),
            ("Combien coûte le TCF à Rabat ?", "2 900 dirhams pour le TCF Canada et le TCF Québec, 1 900 pour le TCF IRN et le tout public — tarif national de l'Institut français du Maroc, relu le 29 octobre 2026.")]),
    mk("tcf-marrakech", "Marrakech", "ma", ["Marrakech"], nearby=["Essaouira", "Safi", "Ouarzazate"],
       title="TCF Marrakech 2026 : 2 900 Dhs, session du 12 novembre",
       desc="TCF Canada à Marrakech : 2 900 Dhs à l'Institut français (route de Targa), session du 12 novembre 2026 en deux créneaux, inscription en ligne, Essaouira.",
       h1="Passer le TCF Canada à Marrakech : l'Institut français, le prix et les dates",
       intro="""À Marrakech, le TCF se passe à l'<strong>Institut français</strong>, route de Targa (Guéliz) — seul centre
agréé de la ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada ; le 17 octobre 2026, son
site proposait une seule session, le <strong>jeudi 12 novembre</strong>, en deux créneaux (9 h-12 h 30 et
13 h-16 h 30). Essaouira (5 novembre, 3 décembre), Safi et Ouarzazate ont leurs propres centres. Le centre,
ses contacts, le relevé, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> à Marrakech : Institut français, route de Targa, Jbel Guéliz.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; session du <strong>12 novembre 2026</strong> (9 h-12 h 30 ou 13 h-16 h 30).",
              "À proximité : Institut français d'Essaouira (5 novembre, 3 décembre), Alliances françaises de Safi (aucune session affichée) et de Ouarzazate (papier).",
              "Inscription en ligne (panier) ; moins de 20 jours entre deux TCF : inscription annulée.",
              "Aucun remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français de Marrakech", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong>", "Jeudi 12 novembre 2026, deux créneaux ; panier en ligne."),
               ("Institut français d'Essaouira", "Canada", "2 900 Dhs", "5 novembre et 3 décembre 2026 (9 h 30-12 h 30)."),
               ("Safi · Ouarzazate", NR, NR, "Safi : aucune session affichée le 17 octobre 2026.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       stat3=("12 nov.", "prochaine session", "relevé du 17 oct. 2026"),
       faq=[("Où passer le TCF Canada à Marrakech ?", "À l'Institut français de Marrakech, route de Targa (Guéliz), seul centre agréé de la ville, sur ordinateur à 2 900 dirhams — session du 12 novembre 2026, en deux créneaux, relevée le 17 octobre."),
            ("Comment s'inscrire au TCF à Marrakech ?", "En ligne, sur if-maroc.org/marrakech, page TCF Canada : choix de la session, panier, paiement."),
            ("Combien coûte le TCF à Marrakech ?", "2 900 dirhams pour le TCF Canada, tarif national de l'Institut français du Maroc (17 octobre 2026)."),
            ("Y a-t-il d'autres dates près de Marrakech ?", "À l'Institut français d'Essaouira, les 5 novembre et 3 décembre 2026 ; l'Alliance française de Safi n'affichait aucune session le 17 octobre 2026.")]),
    mk("tcf-tanger", "Tanger", "ma", ["Tanger"], nearby=["Tétouan"],
       title="TCF Tanger 2026 : 2 900 Dhs, dates de novembre, inscription",
       desc="TCF Canada à Tanger : 2 900 Dhs à l'Institut français, sessions des 12, 19 et 26 novembre 2026 à l'espace Beckett, inscription en ligne ; Tétouan à 60 km.",
       h1="Passer le TCF Canada à Tanger : l'Institut français, le prix et les dates",
       intro="""À Tanger, le TCF se passe à l'<strong>Institut français</strong> — seul centre agréé de la ville —, sur ordinateur,
à <strong>2 900 Dhs</strong> pour le TCF Canada. Le 29 octobre 2026, son site proposait toujours les sessions des
<strong>12, 19 et 26 novembre</strong> (9 h-12 h 30), et rien en décembre ; elles ont lieu à l'<strong>espace
Beckett</strong>, rue Okba-Ibn-Nafie, pas au siège. Tétouan, à 60 km, a son propre Institut (12 novembre,
17 décembre). Le centre, ses adresses, ses horaires, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> à Tanger : Institut français, 41 rue Hassan-Ibn-Ouazzane sur la liste FEI ; accueil et inscriptions au 2, place de France ; sessions à l'espace Beckett, rue Okba-Ibn-Nafie.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; IRN et tout public 1 900 Dhs ; sessions des <strong>12, 19 et 26 novembre 2026</strong>, 9 h-12 h 30, inchangées depuis le 17 octobre, aucune date de décembre affichée le 29.",
              "<a href=\"/centres/tcf-tetouan/\">Tétouan</a> : 12 novembre et 17 décembre 2026 (8 h 30-12 h 30).",
              "Accueil ouvert du lundi au samedi, 9 h-12 h 30 et 14 h 30-18 h (ramadan : 9 h-16 h 30) ; 05 39 94 25 89 ; espace Beckett : 05 39 94 57 00.",
              "Inscription en ligne (panier) ; convocation dès l'inscription ; moins de 20 jours entre deux TCF : inscription annulée ; aucun remboursement ; report sur justificatif facturé 500 Dhs ; attestation à retirer à l'accueil."],
       releve=[("Institut français de Tanger", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong> · IRN et TP 1 900 Dhs", "12, 19 et 26 novembre 2026, 9 h-12 h 30, espace Beckett (rue Okba-Ibn-Nafie) ; aucune date de décembre ; panier en ligne."),
               ("Institut français de Tétouan", "Canada, Québec, IRN, tout public", "2 900 Dhs", "12 novembre, 17 décembre 2026, 8 h 30-12 h 30.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("12 nov.", "prochaine session", "relevé du 29 oct. 2026"),
       faq=[("Où passer le TCF Canada à Tanger ?", "À l'Institut français de Tanger, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams. Les sessions de novembre 2026 sont annoncées à l'espace Beckett, rue Okba-Ibn-Nafie — ni au 41 rue Hassan-Ibn-Ouazzane de la liste FEI, ni à l'accueil de la place de France : lisez le lieu sur la convocation. L'Institut de Tétouan est à 60 km."),
            ("Quelles dates pour le TCF Canada à Tanger ?", "Le 29 octobre 2026 : 12, 19 et 26 novembre, de 9 h à 12 h 30, aucune complète et aucune date de décembre. À Tétouan : 12 novembre et 17 décembre. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à Tanger ?", "En ligne, sur if-maroc.org/tanger, page TCF Canada : choix de la session, panier, paiement. Le TCF IRN s'inscrit à l'accueil (2, place de France), ouvert du lundi au samedi."),
            ("Combien coûte le TCF à Tanger ?", "2 900 dirhams pour le TCF Canada et le TCF Québec, 1 900 pour le TCF IRN et le tout public — tarif national de l'Institut français du Maroc, relu le 29 octobre 2026.")]),
    mk("tcf-fes", "Fès", "ma", ["Fès"], nearby=["Meknès"],
       title="TCF Fès 2026 : 2 900 Dhs, dates oct.-déc., inscription",
       desc="TCF Canada à Fès : 2 900 Dhs à l'Institut français, sessions des 12 et 26 novembre et 17 décembre 2026 à l'Espace Langues, inscription ; Meknès à 60 km.",
       h1="Passer le TCF Canada à Fès : l'Institut français, le prix et l'inscription",
       intro="""À Fès, le TCF se passe à l'<strong>Institut français</strong>, 12 rue Serghini (ville nouvelle) — seul centre
agréé de la ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada, tarif national de
l'Institut français du Maroc. Le 29 octobre 2026, son site vendait trois sessions : <strong>12 et 26 novembre,
17 décembre</strong> (8 h 45-12 h 15), à l'Espace Langues ; celle du 29 octobre n'y figurait plus. Meknès, à 60 km,
a son propre Institut (19 novembre, 17 décembre). Le centre, ses horaires, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> à Fès : Institut français, 12 rue Serghini — l'Espace Langues, où se passent les sessions ; le siège est avenue Abou-Obeida-Ibn-Al-Jarrah ; Meknès à 60 km.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; TCF Québec 2 900 Dhs ; IRN et tout public 1 900 Dhs, l'IRN s'inscrivant à l'accueil uniquement.",
              "En vente le 29 octobre 2026 : <strong>12 et 26 novembre, 17 décembre</strong>, 8 h 45-12 h 15 ; aucune n'affiche complet.",
              "<a href=\"/centres/tcf-meknes/\">Meknès</a> : 19 novembre et 17 décembre 2026 (9 h-14 h).",
              "Accueil ouvert toute la semaine, 8 h 30-12 h 15 et 14 h 30-18 h 30 ; 05 35 62 39 21 ; l'Institut organise aussi le DELF-DALF (à partir de 600 Dhs) et Ev@lang.",
              "Moins de 20 jours entre deux TCF : inscription annulée ; aucun remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français de Fès", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong> · IRN et TP 1 900 Dhs", "12 et 26 nov., 17 déc. 2026, 8 h 45-12 h 15, Espace Langues ; aucune date complète ; panier en ligne."),
               ("Institut français de Meknès", "Canada, Québec, IRN, tout public", "2 900 Dhs", "19 nov., 17 déc. 2026, 9 h-14 h.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("12 nov.", "prochaine session", "3 dates au 29 oct. 2026"),
       faq=[("Où passer le TCF Canada à Fès ?", "À l'Institut français de Fès, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams ; les sessions ont lieu à l'Espace Langues, 12 rue Serghini (ville nouvelle). L'Institut de Meknès est à 60 km."),
            ("Quelles dates pour le TCF Canada à Fès ?", "Le 29 octobre 2026 : 12 et 26 novembre, 17 décembre, de 8 h 45 à 12 h 15, aucune date complète. À Meknès : 19 novembre et 17 décembre. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à Fès ?", "En ligne, sur if-maroc.org/fes, page TCF Canada : choix de la session, panier, paiement. Le TCF IRN s'inscrit à l'accueil, ouvert toute la semaine (8 h 30-12 h 15, 14 h 30-18 h 30)."),
            ("Combien coûte le TCF à Fès ?", "2 900 dirhams pour le TCF Canada et le TCF Québec, 1 900 pour le TCF IRN et le tout public — tarif national de l'Institut français du Maroc, relu le 29 octobre 2026.")]),
    mk("tcf-agadir", "Agadir", "ma", ["Agadir"],
       title="TCF Agadir 2026 : 2 900 Dhs, dates nov.-déc., inscription",
       desc="TCF Canada à Agadir : 2 900 Dhs à l'Institut français, sessions des 13 novembre, 2, 9 et 18 décembre 2026 (27 nov. complet), inscription en ligne, horaires.",
       h1="Passer le TCF Canada à Agadir : l'Institut français, le prix et l'inscription",
       intro="""À Agadir, le TCF se passe à l'<strong>Institut français</strong>, rue de l'Entraide (Talborjt) — seul centre
agréé de la ville et du Sud marocain —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada,
tarif national de l'Institut français du Maroc. Le 29 octobre 2026, son site vendait quatre sessions —
<strong>13 novembre, 2, 9 et 18 décembre</strong> (9 h-12 h), rue Chenguit — et affichait le 27 novembre
complet. Le centre, ses horaires, ce qui a bougé depuis le 17 octobre, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> à Agadir : Institut français, rue de l'Entraide, Talborjt ; lieu de passation annoncé pour chaque session : IF Agadir, rue Chenguit, Nouveau Talborjt.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; TCF Québec 2 900 Dhs ; IRN et tout public 1 900 Dhs, l'IRN s'inscrivant à l'accueil uniquement.",
              "En vente le 29 octobre 2026 : <strong>13 novembre, 2, 9 et 18 décembre</strong>, 9 h-12 h ; le 27 novembre affiche complet.",
              "Depuis le 17 octobre : le 13 novembre, alors complet, a rouvert ; le 27 novembre s'est rempli ; le 2 décembre s'est ajouté — une date pleine peut se libérer, revenez-y.",
              "Accueil ouvert du mardi au samedi, 8 h 30-12 h et 14 h 15-18 h 30, fermé le lundi ; 05 28 84 13 13 ; attestation à retirer à l'accueil.",
              "Moins de 20 jours entre deux TCF : inscription annulée ; aucun remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français d'Agadir", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong> · IRN et TP 1 900 Dhs", "13 nov., 2, 9 et 18 déc. 2026, 9 h-12 h, rue Chenguit (Nouveau Talborjt) ; 27 nov. complet ; panier en ligne.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("13 nov.", "prochaine place libre", "relevé du 29 oct. 2026"),
       faq=[("Où passer le TCF Canada à Agadir ?", "À l'Institut français d'Agadir, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams. Le siège est rue de l'Entraide (Talborjt) ; les sessions de TCF Canada sont annoncées rue Chenguit, Nouveau Talborjt — l'adresse exacte figure sur la convocation."),
            ("Quelles dates pour le TCF Canada à Agadir ?", "Le 29 octobre 2026, quatre sessions étaient en vente : 13 novembre, 2, 9 et 18 décembre, de 9 h à 12 h ; le 27 novembre affichait complet. Le 13 novembre, complet le 17 octobre, avait rouvert entre-temps : une date pleine peut se libérer. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à Agadir ?", "En ligne, sur if-maroc.org/agadir, page TCF Canada : choix de la session, panier, paiement. Le TCF IRN, lui, s'inscrit à l'accueil, ouvert du mardi au samedi (8 h 30-12 h et 14 h 15-18 h 30)."),
            ("Combien coûte le TCF à Agadir ?", "2 900 dirhams pour le TCF Canada et le TCF Québec, 1 900 pour le TCF IRN et le tout public — tarif national de l'Institut français du Maroc, relu le 29 octobre 2026.")]),
    mk("tcf-kenitra", "Kénitra", "ma", ["Kenitra"],
       title="TCF Kénitra 2026 : 2 900 Dhs, 13 dates jusqu'au 18 décembre",
       desc="TCF Canada à Kénitra : 2 900 Dhs à l'Institut français (rue Khalid-Ibn-Walid), 11 sessions du 10 novembre au 18 décembre 2026, 9 h-14 h, inscription.",
       h1="Passer le TCF Canada à Kénitra : l'Institut français, le prix et les dates",
       intro="""À Kénitra, le TCF se passe à l'<strong>Institut français</strong>, rue Khalid-Ibn-Walid — seul centre agréé de la
ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada, tarif national de l'Institut français du Maroc.
Le 29 octobre 2026, son site vendait <strong>onze sessions</strong>, du 10 novembre au 18 décembre (9 h-14 h), aucune
complète — plus que Rabat, à 40 km, qui en affichait cinq. Le centre, ses horaires, le relevé, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> : Institut français de Kénitra, rue Khalid-Ibn-Walid, où se passent les sessions ; <a href=\"/centres/tcf-rabat/\">Rabat</a> à 40 km.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; TCF IRN et tout public 1 900 Dhs.",
              "En vente le 29 octobre 2026 : <strong>10, 13, 17, 20 et 25 novembre, 1<sup>er</sup>, 3, 8, 11, 15 et 18 décembre</strong> (9 h-14 h) ; aucune n'affiche complet ; les deux dates d'octobre sont passées.",
              "Accueil ouvert du mardi au vendredi 9 h-12 h 45 et 14 h-17 h 45, le samedi 9 h-12 h 45 et 14 h-16 h 45 ; 05 37 36 90 55, WhatsApp 07 64 37 30 88 ; le TCF IRN s'y inscrit.",
              "Inscription en ligne sur le site de l'Institut de Kénitra (if-maroc.org/kenitra), session par session, avec un panier.",
              "Moins de 20 jours entre deux TCF, toutes versions confondues : inscription annulée sans remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français de Kénitra", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong> · IRN et TP 1 900 Dhs", "10, 13, 17, 20, 25 nov. ; 1<sup>er</sup>, 3, 8, 11, 15, 18 déc. 2026 (9 h-14 h) ; aucune date complète ; panier en ligne.")],
       releve_date="29 octobre 2026", published="2026-10-18", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("10 nov.", "prochaine session", "11 dates en vente au 29 oct."),
       faq=[("Où passer le TCF Canada à Kénitra ?", "À l'Institut français de Kénitra, rue Khalid-Ibn-Walid, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams. Rabat, à 40 km, a son propre Institut."),
            ("Quelles dates pour le TCF Canada à Kénitra ?", "Le 29 octobre 2026, onze sessions étaient en vente : 10, 13, 17, 20 et 25 novembre, 1er, 3, 8, 11, 15 et 18 décembre, de 9 h à 14 h, aucune complète. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à Kénitra ?", "En ligne, sur if-maroc.org/kenitra, page TCF Canada : choix de la session, panier, paiement. Le TCF IRN s'inscrit à l'accueil, ouvert du mardi au samedi (9 h-12 h 45, puis 14 h-17 h 45, 16 h 45 le samedi) ; WhatsApp 07 64 37 30 88."),
            ('Combien de jours entre deux TCF ?', "Vingt au minimum : « Le candidat ne peut se présenter deux fois à un test du TCF toute version confondue dans un délai inférieur à 20 jours », sinon l'inscription est annulée sans remboursement.")]),
    mk("tcf-meknes", "Meknès", "ma", ["Meknès"],
       title="TCF Meknès 2026 : 2 900 Dhs, sessions oct.-déc., inscription",
       desc="TCF Canada à Meknès : 2 900 Dhs à l'Institut français (rue Ferhat-Hachad), sessions des 19 novembre et 17 décembre 2026, 9 h-14 h, inscription ; Fès à 60 km.",
       h1="Passer le TCF Canada à Meknès : l'Institut français, le prix et les dates",
       intro="""À Meknès, le TCF se passe à l'<strong>Institut français</strong>, rue Ferhat-Hachad — seul centre agréé de la
ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada, tarif national de l'Institut français du Maroc.
Le 29 octobre 2026, son site vendait deux sessions : <strong>19 novembre et 17 décembre</strong> (9 h-14 h) ; celle du
29 octobre n'y figurait plus. Fès, à 60 km, en proposait trois. Le centre, ses contacts, le relevé, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> : Institut français de Meknès, rue Ferhat-Hachad, où se passent les sessions ; <a href=\"/centres/tcf-fes/\">Fès</a> à 60 km.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; TCF IRN et tout public 1 900 Dhs, l'IRN s'inscrivant à l'accueil.",
              "Sessions du <strong>19 novembre et du 17 décembre 2026</strong>, de 9 h à 14 h (relevé du 29 octobre) ; aucune n'affiche complet ; rien entre les deux.",
              "Fès : 12 et 26 novembre, 17 décembre 2026 (8 h 45-12 h 15, Espace Langues) — de quoi combler le creux de fin novembre.",
              "Contact : contact.meknes@institutfrancais-maroc.com, 05 35 51 65 00 ; le site de l'Institut ne publiait pas d'horaires d'accueil le 29 octobre 2026.",
              "Moins de 20 jours entre deux TCF, toutes versions confondues : inscription annulée sans remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français de Meknès", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong> · IRN et TP 1 900 Dhs", "19 nov., 17 déc. 2026, 9 h-14 h ; aucune date complète ; panier en ligne.")],
       releve_note="""<p>Deux sessions à Meknès d'ici la fin de l'année, contre trois à Fès et onze à Kénitra : si le 19 novembre se remplit,
la date la plus proche est le 26 novembre à Fès, à l'Espace Langues de la rue Serghini (60 km). La page de vente de Meknès
annonce ses sessions « Institut Français - Rue Ferhat Hachad », sans autre lieu de passation ; l'offre de l'Institut relue le
29 octobre 2026 comprend aussi le TCF Québec (2 900 Dhs), le TCF tout public (1 900 Dhs), le DELF-DALF (à partir de 600 Dhs)
et Ev@lang (75 Dhs), mais pas le TEF.</p>""",
       releve_date="29 octobre 2026", published="2026-10-18", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("19 nov.", "prochaine session", "2 dates au 29 oct. 2026"),
       faq=[("Où passer le TCF Canada à Meknès ?", "À l'Institut français de Meknès, rue Ferhat-Hachad, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams ; l'Institut de Fès est à 60 km."),
            ("Quelles dates pour le TCF Canada à Meknès ?", "Le 29 octobre 2026 : 19 novembre et 17 décembre, de 9 h à 14 h, aucune complète. À Fès : 12 et 26 novembre, 17 décembre. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à Meknès ?", "En ligne, sur if-maroc.org/meknes, page TCF Canada : choix de la session, panier, paiement. Le TCF IRN s'inscrit à l'accueil (05 35 51 65 00 pour les horaires, non publiés en ligne)."),
            ('Combien de jours entre deux TCF ?', "Vingt au minimum : « Le candidat ne peut se présenter deux fois à un test du TCF toute version confondue dans un délai inférieur à 20 jours », sinon l'inscription est annulée sans remboursement.")]),
    mk("tcf-el-jadida", "El Jadida", "ma", ["El Jadida"],
       title="TCF El Jadida 2026 : 2 900 Dhs, 8 dates d'ici fin novembre",
       desc="TCF Canada à El Jadida : 2 900 Dhs à l'Institut français (3 rue du Caire), 5 sessions du 7 au 28 novembre 2026, 8 h 30-12 h, rien en décembre ; inscription.",
       h1="Passer le TCF Canada à El Jadida : l'Institut français, le prix et les dates",
       intro="""À El Jadida, le TCF se passe à l'<strong>Institut français</strong>, 3, rue du Caire — seul centre agréé de la
ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada, tarif national de l'Institut français du Maroc.
Le 29 octobre 2026, son site vendait <strong>cinq sessions</strong>, toutes en novembre : 7, 14, 19, 26 et 28 (8 h 30-12 h),
aucune complète — et toujours aucune date de décembre. Le centre, ses horaires, le relevé, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> : Institut français d'El Jadida, 3 rue du Caire, où se passent les sessions ; l'accueil est au 22, avenue de la Marche-Verte.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; TCF IRN et tout public 1 900 Dhs.",
              "En vente le 29 octobre 2026 : <strong>7, 14, 19, 26 et 28 novembre</strong>, 8 h 30-12 h ; aucune n'affiche complet ; aucune date de décembre — Rabat en vend deux (4 et 10 décembre).",
              "Accueil ouvert du mardi au samedi, 8 h 30-12 h 30 et 14 h 30-18 h 30 (15 h-18 h 30 le vendredi), fermé le dimanche ; 05 23 35 35 29 ; le TCF IRN s'y inscrit.",
              "Inscription en ligne sur le site de l'Institut d'El Jadida (if-maroc.org/eljadida), avec un panier.",
              "Moins de 20 jours entre deux TCF, toutes versions confondues : inscription annulée sans remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français d'El Jadida", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong> · IRN et TP 1 900 Dhs", "7, 14, 19, 26, 28 nov. 2026 (8 h 30-12 h), 3 rue du Caire ; aucune date complète ; aucune date de décembre affichée ; panier en ligne.")],
       releve_date="29 octobre 2026", published="2026-10-18", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("7 nov.", "prochaine session", "5 dates en vente au 29 oct."),
       faq=[("Où passer le TCF Canada à El Jadida ?", "À l'Institut français d'El Jadida, 3 rue du Caire, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams ; l'accueil, où s'inscrit le TCF IRN, est au 22, avenue de la Marche-Verte."),
            ("Quelles dates pour le TCF Canada à El Jadida ?", "Le 29 octobre 2026, cinq sessions étaient en vente : 7, 14, 19, 26 et 28 novembre, de 8 h 30 à 12 h, aucune complète ; aucune date de décembre n'était affichée (Rabat : 4 et 10 décembre). La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à El Jadida ?", "En ligne, sur if-maroc.org/eljadida, page TCF Canada : choix de la session, panier, paiement. Le TCF IRN s'inscrit à l'accueil, ouvert du mardi au samedi."),
            ('Combien de jours entre deux TCF ?', "Vingt au minimum : « Le candidat ne peut se présenter deux fois à un test du TCF toute version confondue dans un délai inférieur à 20 jours », sinon l'inscription est annulée sans remboursement.")]),
    mk("tcf-tetouan", "Tétouan", "ma", ["Tétouan"],
       title="TCF Tétouan 2026 : 2 900 Dhs, dates oct.-déc., inscription",
       desc="TCF Canada à Tétouan : 2 900 Dhs à l'Institut français (13 rue Chakib-Arsalane), sessions des 12 novembre et 17 décembre 2026, 8 h 30-12 h 30 ; Tanger.",
       h1="Passer le TCF Canada à Tétouan : l'Institut français, le prix et les dates",
       intro="""À Tétouan, le TCF se passe à l'<strong>Institut français</strong>, 13, rue Chakib-Arsalane — seul centre agréé de
la ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada, tarif national de l'Institut français du
Maroc. Le 29 octobre 2026, son site vendait deux sessions : <strong>12 novembre et 17 décembre</strong>
(8 h 30-12 h 30) ; celle du 22 octobre est passée. Tanger, à 60 km, propose les 12, 19 et 26 novembre. Le centre,
ses contacts, le relevé, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> : Institut français de Tétouan, 13 rue Chakib-Arsalane (05 39 71 43 11, contact.tetouan@ifmaroc.com) ; <a href=\"/centres/tcf-tanger/\">Tanger</a> à 60 km.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; TCF IRN et tout public 1 900 Dhs, l'IRN s'inscrivant à l'accueil.",
              "Sessions du <strong>12 novembre et du 17 décembre 2026</strong>, de 8 h 30 à 12 h 30 (relevé du 29 octobre) ; aucune n'affiche complet ; rien entre les deux.",
              "Tanger : 12, 19 et 26 novembre 2026, à l'espace Beckett — pour qui veut une date de fin novembre.",
              "L'antenne d'Al Hoceima de l'Institut (avenue Homane-El-Fetouaki) n'est pas un centre d'examen agréé : depuis Al Hoceima, les centres les plus proches sont Tétouan et Nador (rattaché à Oujda).",
              "Moins de 20 jours entre deux TCF, toutes versions confondues : inscription annulée sans remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français de Tétouan", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong> · IRN et TP 1 900 Dhs", "12 nov., 17 déc. 2026, 8 h 30-12 h 30 ; aucune date complète ; panier en ligne.")],
       releve_note="""<p>Tétouan et Tanger, à une heure de route, se complètent : Tétouan le 12 novembre et le 17 décembre en matinée
(8 h 30-12 h 30), Tanger les 12, 19 et 26 novembre à l'espace Beckett. La page de vente de Tétouan n'indique que « IF Tétouan »
comme lieu : comptez sur le 13, rue Chakib-Arsalane, siège de l'Institut, sauf mention contraire sur la convocation. Particularité
relue le 29 octobre 2026 : l'Institut de Tétouan organise aussi le <strong>TEF Canada</strong> (2 900 Dhs), que ni Fès ni Meknès
n'affichent, en plus du TCF Québec, du TCF tout public, du DELF-DALF (à partir de 600 Dhs) et d'Ev@lang.</p>""",
       releve_date="29 octobre 2026", published="2026-10-18", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("12 nov.", "prochaine session", "2 dates au 29 oct. 2026"),
       faq=[("Où passer le TCF Canada à Tétouan ?", "À l'Institut français de Tétouan, 13 rue Chakib-Arsalane, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams ; l'Institut de Tanger est à 60 km. L'antenne d'Al Hoceima n'organise pas le TCF."),
            ("Quelles dates pour le TCF Canada à Tétouan ?", "Le 29 octobre 2026 : 12 novembre et 17 décembre, de 8 h 30 à 12 h 30, aucune complète. À Tanger : 12, 19 et 26 novembre. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à Tétouan ?", "En ligne, sur if-maroc.org/tetouan, page TCF Canada : choix de la session, panier, paiement. Le TCF IRN s'inscrit à l'accueil (05 39 71 43 11)."),
            ('Combien de jours entre deux TCF ?', "Vingt au minimum : « Le candidat ne peut se présenter deux fois à un test du TCF toute version confondue dans un délai inférieur à 20 jours », sinon l'inscription est annulée sans remboursement.")]),
    mk("tcf-oujda", "Oujda", "ma", ["Oujda"], nearby=["Nador"],
       title="TCF Oujda 2026 : 2 900 Dhs, session du 10 novembre, Nador",
       desc="TCF Canada à Oujda : 2 900 Dhs à l'Institut français, une seule session affichée, le 10 novembre 2026 (8 h 30-18 h, lot Chabab), inscription en ligne ; Nador.",
       h1="Passer le TCF Canada à Oujda : l'Institut français, le prix et les dates",
       intro="""À Oujda, le TCF se passe à l'<strong>Institut français</strong> — seul centre agréé de la ville, auquel est
rattaché le centre de Nador (école française Paul-Riquet) —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF
Canada. Le 29 octobre 2026 comme le 17, son site ne listait qu'une session, le <strong>mardi 10 novembre</strong>,
de 8 h 30 à 18 h, au 9-11, lot Chabab (Hay Al Qods) — l'adresse de l'accueil, qui n'est pas l'espace langue de la
liste FEI. Le centre, ses horaires, le relevé, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> à Oujda : Institut français — espace langue, 16 rue Imam-Echafii, sur la liste FEI ; accueil et session au 9-11, lot Chabab, Hay Al Qods. Nador : école française Paul-Riquet, rattachée à Oujda.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; TCF IRN et tout public 1 900 Dhs.",
              "Une seule session affichée le 29 octobre 2026 (déjà la seule le 17) : <strong>mardi 10 novembre</strong>, créneau de 8 h 30 à 18 h ; rien en décembre.",
              "Accueil ouvert lundi et samedi 8 h 30-12 h et 14 h 30-18 h 30, du mardi au vendredi 8 h 30-18 h 30 sans interruption ; 05 36 68 44 04 ou 05 36 70 40 00 ; le TCF IRN s'y inscrit.",
              "Inscription en ligne sur le site de l'Institut d'Oujda (if-maroc.org/oujda), avec un panier.",
              "Moins de 20 jours entre deux TCF, toutes versions confondues : inscription annulée sans remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français d'Oujda", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong> · IRN et TP 1 900 Dhs", "Mardi 10 novembre 2026, 8 h 30-18 h, 9-11 lot Chabab, seule session listée les 17 et 29 octobre ; panier en ligne."),
               ("Nador (école Paul-Riquet, rattachée à Oujda)", "Canada", NR, "Sessions à vérifier auprès de l'Institut d'Oujda.")],
       releve_date="29 octobre 2026", published="2026-10-18", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("10 nov.", "seule session affichée", "relevé du 29 oct. 2026"),
       faq=[("Où passer le TCF Canada à Oujda ?", "À l'Institut français d'Oujda, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams ; la session du 10 novembre 2026 est annoncée au 9-11, lot Chabab (Hay Al Qods), l'adresse de l'accueil. Le centre de Nador, à l'école Paul-Riquet, lui est rattaché."),
            ("Quelles dates pour le TCF Canada à Oujda ?", "Le 29 octobre 2026, une seule session était listée : le mardi 10 novembre, de 8 h 30 à 18 h, comme le 17 octobre. La page TCF Canada du site fait foi ; Fès (12 et 26 novembre, 17 décembre) et Meknès (19 novembre, 17 décembre) en proposaient d'autres."),
            ("Comment s'inscrire au TCF à Oujda ?", "En ligne, sur if-maroc.org/oujda, page TCF Canada : choix de la session, panier, paiement. Le TCF IRN s'inscrit à l'accueil, ouvert du mardi au vendredi de 8 h 30 à 18 h 30."),
            ('Combien de jours entre deux TCF ?', "Vingt au minimum : « Le candidat ne peut se présenter deux fois à un test du TCF toute version confondue dans un délai inférieur à 20 jours », sinon l'inscription est annulée sans remboursement.")]),
    # ------------------------------------------------------------------ Tunisie
    mk("tcf-tunis", "Tunis", "tn", ["Tunis", "Ariana", "El Mourouj"], h2_label="Tunis, El Mourouj et Ariana",
       title="TCF Tunis 2026 : 880 DT, rendez-vous en ligne, calendrier",
       desc="TCF Canada à Tunis : 880 DT à l'Institut français, tests des 26-27 nov. et 16 et 18 déc. 2026, rendez-vous en ligne du 26 au 31 oct. ; El Mourouj, Ariana.",
       h1="Passer le TCF Canada à Tunis : les centres agréés, le prix et le calendrier",
       intro="""À Tunis, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international :
le centre de langue de l'<strong>Institut français</strong>, 20-22 avenue de Paris, son pôle d'El Mourouj, et
l'<strong>Alliance française de Tunis</strong> à Ariana (El Menzah 6). À l'Institut, le TCF Canada coûte
<strong>880 DT</strong> et se réserve en ligne avant une inscription sur place ; le 17 octobre 2026, le calendrier
affichait les tests des 22-23 octobre (inscription close), des <strong>26-27 novembre</strong> (rendez-vous en ligne
du 26 au 31 octobre) et des <strong>16 et 18 décembre</strong> (du 9 au 15 novembre). Les centres, leurs contacts,
le relevé, et la procédure.""",
       facts=["<strong>3 centres agréés</strong> : Institut français de Tunisie (avenue de Paris), pôle d'El Mourouj 1, Alliance française de Tunis (Ariana).",
              "<strong>TCF Canada 880 DT</strong> à l'Institut ; TCF Québec 880 DT ; TCF IRN 625 DT ; tout public 335 DT + 220 DT par expression.",
              "Tunis : tests des <strong>26-27 novembre</strong> (rendez-vous en ligne du 26 au 31 octobre, inscription le 5 novembre) et des <strong>16 et 18 décembre</strong> (rendez-vous du 9 au 15 novembre, inscription le 19).",
              "El Mourouj 1 : tests des 19 et 26 novembre, 10 et 16 décembre 2026 — rendez-vous du 12 au 22 octobre pour le 26 novembre.",
              "Paiement en espèces ou par carte à Tunis (espèces seulement à El Mourouj) ; chèques suspendus ; frais non remboursables ; résultats <strong>5 semaines</strong> après ; 30 jours entre deux sessions."],
       releve=[("Institut français de Tunisie — pôle de Tunis", "Canada, Québec, IRN, tout public", "Canada <strong>880 DT</strong> · Québec 880 DT · IRN 625 DT · TP-SO 335 DT + 220 DT", "RDV en ligne 26-31/10 → inscription 05/11 → test 26-27/11 ; 09-15/11 → 19/11 → 16 et 18/12 ; test des 22-23/10 : inscription close le 24/09."),
               ("IFT — pôle d'El Mourouj 1", "Canada, Québec, tout public", "880 DT", "RDV 12-22/10 → inscription 03/11 → test 26/11 ; 01-11/11 → 12/11 → 19/11 ; 09-24/11 → 25/11 → 16/12 ; 22/11-02/12 → 03/12 → 10/12 ; espèces."),
               ("Alliance française de Tunis (Ariana)", "Canada, Québec, tout public", NR, "Calendrier des examens sur alliancefr.tn.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       stat3=("26-27 nov.", "prochain test ouvert", "rendez-vous du 26 au 31 oct."),
       faq=[("Où passer le TCF Canada à Tunis ?", "À l'Institut français de Tunisie (centre de langue, 20-22 avenue de Paris), à son pôle d'El Mourouj, ou à l'Alliance française de Tunis à Ariana — trois centres agréés par France Éducation international."),
            ("Comment prendre rendez-vous pour le TCF à Tunis ?", "Sur la page TCF Canada de institutfrancais-tunisie.com (« Réservation »), pendant la fenêtre de rendez-vous en ligne de la session, puis inscription et paiement sur place le jour fixé — un mandataire muni d'une copie de votre carte d'identité peut y aller."),
            ("Combien coûte le TCF à Tunis ?", "À l'Institut français : 880 dinars pour le TCF Canada et le TCF Québec, 625 dinars pour le TCF IRN, 335 dinars pour les épreuves obligatoires du tout public sur ordinateur (17 octobre 2026). L'Alliance française ne publie pas de tarif lisible."),
            ("Quelles dates pour le TCF Canada à Tunis ?", "Le 17 octobre 2026, à l'avenue de Paris : 22-23 octobre (inscription close), 26-27 novembre (rendez-vous en ligne du 26 au 31 octobre, inscription sur place le 5 novembre), 16 et 18 décembre (rendez-vous du 9 au 15 novembre, inscription le 19 novembre). À El Mourouj 1 : 19 et 26 novembre, 10 et 16 décembre.")]),
    mk("tcf-sousse", "Sousse", "tn", ["Sousse"],
       title="TCF Sousse 2026 : 880 DT, rendez-vous en ligne, calendrier",
       desc="TCF Canada à Sousse : 880 DT à l'Institut français, tests des 18 et 20 nov., 16 et 18 déc. 2026, rendez-vous en ligne du 19 au 22 oct., inscription.",
       h1="Passer le TCF Canada à Sousse : le pôle de l'Institut français et l'inscription",
       intro="""À Sousse, le TCF se passe au <strong>pôle de l'Institut français de Tunisie</strong>, 15 rue Hamed-El-Ghazeli
(Bouhsina) — seul centre agréé de la ville —, sur ordinateur, à <strong>880 DT</strong> pour le TCF Canada, avec un
rendez-vous en ligne puis l'inscription et le paiement sur place, en espèces. Le 17 octobre 2026, le
calendrier du pôle annonçait les tests des 28 et 30 octobre, puis des <strong>18 et 20 novembre</strong>
(rendez-vous en ligne du 19 au 22 octobre) et des <strong>16 et 18 décembre</strong> (du 9 au 12 novembre). Le
centre, ses contacts, et la procédure.""",
       facts=["<strong>1 centre agréé</strong> à Sousse : IFT, pôle de Sousse, 15 rue Hamed-El-Ghazeli, Bouhsina.",
              "<strong>TCF Canada 880 DT</strong> ; TCF Québec 880 DT ; TCF IRN 625 DT.",
              "Tests des <strong>18 et 20 novembre</strong> (rendez-vous en ligne 19-22 octobre, inscription 26-28 octobre) et des <strong>16 et 18 décembre</strong> (rendez-vous 9-12 novembre, inscription 16-18 novembre).",
              "Paiement en espèces seulement ; frais non remboursables.",
              "Résultats 5 semaines après ; 30 jours entre deux sessions."],
       releve=[("IFT — pôle de Sousse", "Canada, Québec, IRN, tout public", "Canada <strong>880 DT</strong>", "RDV 19-22/10 → inscription 26-28/10 → tests 18 et 20/11 ; 09-12/11 → 16-18/11 → 16 et 18/12 ; tests des 28 et 30/10 : rendez-vous clos ; espèces.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       stat3=("18 et 20 nov.", "prochains tests ouverts", "rendez-vous du 19 au 22 oct."),
       faq=[("Où passer le TCF Canada à Sousse ?", "Au pôle de Sousse de l'Institut français de Tunisie, 15 rue Hamed-El-Ghazeli, seul centre agréé de la ville."),
            ("Quelles dates pour le TCF Canada à Sousse ?", "Le 17 octobre 2026 : 18 et 20 novembre (rendez-vous en ligne du 19 au 22 octobre, inscription sur place du 26 au 28 octobre), 16 et 18 décembre (rendez-vous du 9 au 12 novembre, inscription du 16 au 18 novembre). Les tests des 28 et 30 octobre n'acceptaient plus de rendez-vous."),
            ("Comment s'inscrire au TCF à Sousse ?", "Rendez-vous en ligne sur la page TCF Canada de l'Institut pendant la fenêtre de la session, puis inscription et paiement sur place, en espèces, le jour fixé."),
            ("Combien coûte le TCF à Sousse ?", "880 dinars pour le TCF Canada et le TCF Québec, 625 dinars pour le TCF IRN, à l'Institut français de Tunisie (17 octobre 2026).")]),
    mk("tcf-sfax", "Sfax", "tn", ["Sfax"],
       title="TCF Sfax 2026 : 880 DT, rendez-vous en ligne, calendrier",
       desc="TCF Canada à Sfax : 880 DT à l'Institut français, tests des 27 novembre et 19 décembre 2026, rendez-vous en ligne 2-8 nov. et 1er-6 déc. ; Québec, IRN.",
       h1="Passer le TCF Canada à Sfax : l'Institut français et l'inscription",
       intro="""À Sfax, le TCF se passe au <strong>centre de langue de l'Institut français</strong>, 9 avenue Habib-Bourguiba —
seul centre agréé de la ville —, sur ordinateur, à <strong>880 DT</strong> pour le TCF Canada, avec un rendez-vous en
ligne puis l'inscription et le paiement sur place. Le 29 octobre 2026, le calendrier du pôle annonçait toujours les
tests du <strong>27 novembre</strong> (rendez-vous en ligne du 2 au 8 novembre, inscription le 12) et du
<strong>19 décembre</strong> (du 1<sup>er</sup> au 6 décembre, inscription le 8) ; le TCF Québec la veille de chacun, et
le TCF IRN presque chaque semaine de novembre. Le centre, ses contacts, ses tarifs, et la procédure.""",
       facts=["<strong>1 centre agréé</strong> à Sfax : Institut français, centre de langue, 9 avenue Habib-Bourguiba (BP 1135) ; 58 440 336 ou 74 224 205 ; centredelangue.sfax@institutfrancais-tunisie.com.",
              "<strong>TCF Canada 880 DT</strong> ; TCF Québec 880 DT ; TCF IRN 625 DT ; tout public 335 DT + 220 DT par épreuve d'expression ; paiement en espèces à Sfax ; frais non remboursables, report seulement sur justificatif de force majeure présenté sous 48 h.",
              "TCF Canada : test du <strong>27 novembre</strong> (rendez-vous en ligne 2-8 novembre, inscription le 12) et du <strong>19 décembre</strong> (rendez-vous 1<sup>er</sup>-6 décembre, inscription le 8) — calendrier inchangé entre le 17 et le 29 octobre 2026.",
              "TCF Québec à Sfax : 26 novembre et 18 décembre, mêmes fenêtres de rendez-vous ; TCF IRN et tout public : 5, 6, 11, 12, 13, 18, 20, 24 et 30 novembre (9 h ou 14 h), rendez-vous la semaine précédente.",
              "Pas d'atelier de préparation au TCF Canada à Sfax (proposé à Tunis, El Mourouj, Nabeul-Hammamet et Sousse, 270 DT les 20 h) ; le pôle vend des cours de préparation TCF Canada-Québec par session.",
              "Résultats 5 semaines après ; 30 jours entre deux sessions ; un mandataire muni d'une copie de votre carte d'identité peut vous inscrire le jour fixé."],
       releve=[("IFT — centre de langue de Sfax (TCF Canada)", "Canada, Québec, IRN, tout public ; TEF Canada et Québec, DELF-DALF", "Canada <strong>880 DT</strong> · Québec 880 DT · IRN 625 DT · TP 335 DT (+ 220 DT par expression)", "RDV 02-08/11 → inscription 12/11 → test 27/11 ; 01-06/12 → 08/12 → 19/12 ; espèces sur place ; pas d'atelier de préparation à Sfax."),
               ("Même centre — TCF Québec, IRN et tout public", "Québec ; IRN et TP (QCM + expressions)", "Québec 880 DT · IRN 625 DT", "Québec : 26/11 et 18/12 (mêmes RDV) ; IRN-TP : 05, 06, 11/11 (RDV 26/10-01/11), 12, 13, 18/11 (RDV 02-08/11), 20, 24/11 (RDV 09-15/11), 30/11 (RDV 16-22/11), 9 h ou 14 h.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("27 nov.", "prochain test ouvert", "rendez-vous du 2 au 8 nov."),
       faq=[("Où passer le TCF Canada à Sfax ?", "Au centre de langue de l'Institut français de Sfax, 9 avenue Habib-Bourguiba, seul centre agréé de la ville (liste FEI relue le 29 octobre 2026) ; 58 440 336, centredelangue.sfax@institutfrancais-tunisie.com."),
            ("Quelles dates pour le TCF Canada à Sfax ?", "Le 29 octobre 2026 : 27 novembre (rendez-vous en ligne du 2 au 8 novembre, inscription sur place le 12 novembre) et 19 décembre (rendez-vous du 1er au 6 décembre, inscription le 8 décembre), comme le 17 octobre. Le test du 30 octobre n'acceptait plus de rendez-vous."),
            ("Peut-on passer le TCF IRN ou le TCF Québec à Sfax ?", "Oui. Le TCF Québec y est programmé la veille du TCF Canada (26 novembre, 18 décembre 2026), avec les mêmes fenêtres de rendez-vous ; le TCF IRN et le TCF tout public, presque chaque semaine : 5, 6, 11, 12, 13, 18, 20, 24 et 30 novembre, à 9 h ou 14 h, rendez-vous en ligne la semaine précédente. TCF IRN 625 DT, tout public 335 DT plus 220 DT par épreuve d'expression ; pour l'IRN, l'Institut rappelle qu'il faut viser le niveau B2."),
            ("Comment s'inscrire et payer le TCF à Sfax ?", "Rendez-vous en ligne sur la page TCF Canada de l'Institut pendant la fenêtre de la session, puis inscription et paiement sur place, en espèces, le jour fixé ; vous pouvez envoyer quelqu'un avec une photocopie de votre carte d'identité. Les frais ne sont pas remboursés ; un report n'est accordé que sur justificatif de force majeure remis dans les 48 heures."),
            ("Combien coûte le TCF à Sfax ?", "880 dinars pour le TCF Canada et le TCF Québec, 625 dinars pour le TCF IRN, 335 dinars pour le tout public (plus 220 par épreuve d'expression), à l'Institut français de Tunisie (29 octobre 2026). L'atelier de préparation de 20 h à 270 DT n'existe pas à Sfax.")]),
    mk("tcf-nabeul-hammamet", "Nabeul-Hammamet", "tn", ["Nabeul"],
       title="TCF Nabeul-Hammamet 2026 : 880 DT, rendez-vous, calendrier",
       desc="TCF Canada à Nabeul-Hammamet : 880 DT à l'Institut français, test du 27 novembre 2026 (rendez-vous en ligne jusqu'au 30 octobre), puis du 18 décembre.",
       h1="Passer le TCF Canada à Nabeul-Hammamet : le pôle de l'Institut français et l'inscription",
       intro="""À Nabeul-Hammamet, le TCF se passe au <strong>pôle de l'Institut français de Tunisie</strong>, au centre de
formation touristique de Nabeul (avenue Taieb-Mehiri) — seul centre agréé —, sur ordinateur, à <strong>880 DT</strong>
pour le TCF Canada, avec un rendez-vous en ligne puis l'inscription et le paiement sur place, en espèces. Le
17 octobre 2026, le calendrier du pôle annonçait les tests du 30 octobre (rendez-vous clos), du <strong>27
novembre</strong> (rendez-vous en ligne jusqu'au 30 octobre, inscription du 4 au 9 novembre) et du <strong>18
décembre</strong> (rendez-vous du 2 au 24 novembre). Le centre, ses contacts, et la procédure.""",
       facts=["<strong>1 centre agréé</strong> : IFT, pôle de Nabeul-Hammamet, centre de formation touristique de Nabeul, avenue Taieb-Mehiri.",
              "<strong>TCF Canada 880 DT</strong>, tarif de l'Institut français de Tunisie (17 octobre 2026).",
              "Tests du <strong>27 novembre</strong> (rendez-vous en ligne jusqu'au 30 octobre, inscription du 4 au 9 novembre) et du <strong>18 décembre</strong> (rendez-vous du 2 au 24 novembre, inscription du 25 au 30 novembre).",
              "Paiement en espèces ; frais non remboursables ; un mandataire muni de la photocopie de votre carte d'identité peut s'inscrire pour vous.",
              "Résultats 5 semaines après ; 30 jours entre deux sessions de TCF ou de TEF."],
       releve=[("IFT — pôle de Nabeul-Hammamet", "Canada", "Canada <strong>880 DT</strong>", "RDV jusqu'au 30/10 → inscription 04-09/11 → test 27/11 ; 02-24/11 → 25-30/11 → 18/12 ; test du 30/10 : rendez-vous clos ; espèces.")],
       releve_date="17 octobre 2026", published="2026-10-18", modified=("2026-10-18", "18 octobre 2026"),
       stat3=("27 nov.", "prochain test ouvert", "rendez-vous jusqu'au 30 oct."),
       faq=[("Où passer le TCF Canada à Nabeul ou à Hammamet ?", "Au pôle de Nabeul-Hammamet de l'Institut français de Tunisie, installé au centre de formation touristique de Nabeul (avenue Taieb-Mehiri), seul centre agréé."),
            ("Quelles dates pour le TCF Canada à Nabeul-Hammamet ?", "Le 17 octobre 2026 : 27 novembre (rendez-vous en ligne jusqu'au 30 octobre, inscription sur place du 4 au 9 novembre) et 18 décembre (rendez-vous du 2 au 24 novembre, inscription du 25 au 30 novembre). Le test du 30 octobre n'acceptait plus de rendez-vous."),
            ("Comment s'inscrire au TCF à Nabeul-Hammamet ?", "Rendez-vous en ligne sur la page TCF Canada de l'Institut français de Tunisie (« Réservation ») pendant la fenêtre de la session, puis inscription et paiement sur place, en espèces, aux dates fixées."),
            ("Combien coûte le TCF à Nabeul-Hammamet ?", "880 dinars pour le TCF Canada, tarif de l'Institut français de Tunisie relu le 17 octobre 2026 ; paiement en espèces au pôle.")]),
    mk("tcf-beja", "Béja", "tn", ["Béja"],
       title="TCF Béja 2026 : 880 DT, rendez-vous en ligne, calendrier",
       desc="TCF Canada à Béja : 880 DT à l'Institut français (lycée privé L'Avenir), test du 26 novembre 2026, rendez-vous en ligne du 19 au 31 octobre, inscription.",
       h1="Passer le TCF Canada à Béja : le pôle de l'Institut français et l'inscription",
       intro="""À Béja, le TCF se passe au <strong>pôle de l'Institut français de Tunisie</strong>, au lycée privé L'Avenir, rue
Habib-Thameur — seul centre agréé de la ville —, sur ordinateur, à <strong>880 DT</strong> pour le TCF Canada, avec un
rendez-vous en ligne puis l'inscription et le paiement sur place, en espèces. Le 17 octobre 2026, le calendrier du
pôle annonçait les tests du 29 octobre (rendez-vous clos), du <strong>26 novembre</strong> (rendez-vous en ligne du
19 au 31 octobre, inscription les 3 et 4 novembre) et du <strong>16 décembre</strong> (rendez-vous du 16 au
30 novembre). Le centre, ses contacts, et la procédure.""",
       facts=["<strong>1 centre agréé</strong> : IFT, pôle de Béja, lycée privé L'Avenir, rue Habib-Thameur.",
              "<strong>TCF Canada 880 DT</strong>, tarif de l'Institut français de Tunisie (17 octobre 2026).",
              "Tests du <strong>26 novembre</strong> (rendez-vous en ligne du 19 au 31 octobre, inscription les 3 et 4 novembre) et du <strong>16 décembre</strong> (rendez-vous du 16 au 30 novembre, inscription les 1<sup>er</sup> et 2 décembre).",
              "Paiement en espèces ; frais non remboursables ; un mandataire muni de la photocopie de votre carte d'identité peut s'inscrire pour vous.",
              "Résultats 5 semaines après ; 30 jours entre deux sessions de TCF ou de TEF."],
       releve=[("IFT — pôle de Béja", "Canada", "Canada <strong>880 DT</strong>", "RDV 19-31/10 → inscription 03-04/11 → test 26/11 ; 16-30/11 → 01-02/12 → 16/12 ; test du 29/10 : rendez-vous clos ; espèces.")],
       releve_note="""<p>Sous ses tarifs, la page TCF Canada de l'Institut affiche aussi « Tarif (pôle de Béja) : 160 DT », sans
préciser à quoi il s'applique : demandez-le au pôle avant de payer.</p>""",
       releve_date="17 octobre 2026", published="2026-10-18", modified=("2026-10-18", "18 octobre 2026"),
       stat3=("26 nov.", "prochain test ouvert", "rendez-vous du 19 au 31 oct."),
       faq=[("Où passer le TCF Canada à Béja ?", "Au pôle de Béja de l'Institut français de Tunisie, installé au lycée privé L'Avenir, rue Habib-Thameur, seul centre agréé de la ville."),
            ("Quelles dates pour le TCF Canada à Béja ?", "Le 17 octobre 2026 : 26 novembre (rendez-vous en ligne du 19 au 31 octobre, inscription sur place les 3 et 4 novembre) et 16 décembre (rendez-vous du 16 au 30 novembre, inscription les 1er et 2 décembre). Le test du 29 octobre n'acceptait plus de rendez-vous."),
            ("Comment s'inscrire au TCF à Béja ?", "Rendez-vous en ligne sur la page TCF Canada de l'Institut français de Tunisie (« Réservation ») pendant la fenêtre de la session, puis inscription et paiement sur place, en espèces, aux dates fixées."),
            ("Combien coûte le TCF à Béja ?", "880 dinars pour le TCF Canada, tarif de l'Institut français de Tunisie relu le 17 octobre 2026. La même page affiche un « Tarif (pôle de Béja) : 160 DT » sans dire à quoi il s'applique : demandez au pôle.")]),
    # ------------------------------------------------------------------ DELF (France)
    mk("delf-paris", "Paris", "fr", ["Paris"], exam="delf",
       title="DELF à Paris : 7 centres, prix (B2 249-280 €), sessions 2026",
       desc="Où passer le DELF à Paris : 7 centres agréés avec contacts, les prix relevés (B1 194 à 230 €, B2 249 à 280 €), les sessions 2026, les fenêtres d'inscription.",

       h1="Passer le DELF à Paris : les 7 centres agréés, leurs prix et leurs sessions",
       intro="""À Paris, le DELF et le DALF se passent dans <strong>%(n)d centres agréés</strong> par France Éducation
international — deux universités, une Alliance française, trois écoles privées ou associatives et le centre
de l'académie. Pour un même DELF B2, le prix va de <strong>249 € (Sorbonne Nouvelle) à 280 € (Alliance
française)</strong>, et les inscriptions ferment quatre à dix semaines avant l'écrit. Les centres, leurs
contacts, le relevé, et les prochaines sessions.""",
       facts=["<strong>7 centres agréés</strong> : Alliance française de Paris (6<sup>e</sup>), Sorbonne Nouvelle (12<sup>e</sup>), Cours de civilisation française de la Sorbonne (17<sup>e</sup>), SELFEE Sorbonne Université (5<sup>e</sup>), Prosodia (20<sup>e</sup>), THOT (1<sup>er</sup>), CASNAV (19<sup>e</sup>).",
              "<strong>DELF B2 : 249 € Sorbonne Nouvelle · 269 € CCFS · 280 € Alliance française</strong> ; B1 : 194 · 214 · 230 €.",
              "Alliance française : session de novembre 2026 (écrit le 4, oraux 13-20), <strong>inscription jusqu'au 4 octobre</strong>.",
              "CCFS : écrit du 2 décembre, <strong>inscriptions du 12 octobre au 8 novembre</strong> ; Sorbonne Nouvelle : deux sessions par an (février, mai).",
              "Nantes (125 €) et Lyon (159 €) sont à moins de deux heures : pour un B2, le billet est vite amorti."],
       releve=[("Alliance française Paris Île-de-France", "DELF A1-B2, DALF", "A2 190 € · B1 230 € · <strong>B2 280 €</strong> · DALF 290 €", "Novembre 2026 : écrit 3-4 nov., oraux 13-20 nov., inscription jusqu'au 4 oct. ; résultats par e-mail sous 6 semaines."),
               ("Université Sorbonne Nouvelle (Campus Nation)", "DELF B1, B2, DALF C1, C2", "B1 194 € · <strong>B2 249 €</strong> · C1 249 € · C2 290 €", "2 sessions par an (février, mai) ; inscriptions en ligne sur 3 semaines, 10 semaines avant."),
               ("Cours de civilisation française de la Sorbonne", "DELF B1, B2, DALF C1", "B1 214 € · <strong>B2 269 €</strong> · C1 279 €", "Juin, juillet, octobre, décembre ; écrit du 2 déc. 2026 : inscriptions 12 oct.-8 nov."),
               ("SELFEE Sorbonne Université · Prosodia · THOT · CASNAV", NR, NR, "Sur le site du centre ; CASNAV orienté DELF scolaire.")],
       faq=[("Où passer le DELF B2 à Paris ?", "À l'Alliance française de Paris (280 €, écrit le 4 novembre 2026, inscription jusqu'au 4 octobre), aux Cours de civilisation française de la Sorbonne (269 €, écrit du 2 décembre, inscriptions du 12 octobre au 8 novembre) ou à la Sorbonne Nouvelle (249 €, sessions de février et mai) ; SELFEE, Prosodia et THOT sont aussi agréés."),
            ("Combien coûte le DELF à Paris ?", "Pour le B2 : 249 € à la Sorbonne Nouvelle, 269 € aux Cours de civilisation française de la Sorbonne, 280 € à l'Alliance française (dont 20 € de frais de dossier) ; pour le B1 : 194, 214 et 230 €. Relevé le 17 septembre 2026."),
            ("Quand s'inscrire au DELF à Paris ?", "Quatre à dix semaines avant l'écrit : le 4 octobre au plus tard pour la session de novembre à l'Alliance française, entre le 12 octobre et le 8 novembre pour l'écrit du 2 décembre aux CCFS ; la Sorbonne Nouvelle n'ouvre ses inscriptions que trois semaines, dix semaines avant chaque session."),
            ("Peut-on passer le DELF à Paris en dehors de ces dates ?", "Non : le DELF se passe aux dix sessions nationales de l'année — en 2026, il reste octobre, novembre et décembre —, et chaque centre n'en ouvre qu'une partie. Pour une date plus proche, le TCF IRN se passe chaque semaine, mais son attestation vaut deux ans.")]),
    mk("delf-lyon", "Lyon", "fr", ["Lyon"], exam="delf",
       title="DELF à Lyon : 7 centres, Alliance française à 159 €, dates",
       desc="Où passer le DELF à Lyon : 7 centres agréés avec contacts, le DELF B2 à 159 € à l'Alliance française, dix sessions par an — oct. et nov. 2026 complets.",

       h1="Passer le DELF à Lyon : les 7 centres agréés, le prix et les sessions",
       intro="""À Lyon, le DELF et le DALF se passent dans <strong>%(n)d centres agréés</strong> par France Éducation
international — l'Alliance française, ALPES Formation, le GRETA CFA Lyon Métropole, Inflexyon, l'ILCF,
Lyon Bleu, REN Formation. L'<strong>Alliance française de Lyon</strong> ouvre les dix sessions de l'année, à
<strong>159 €</strong> le DELF B2 — et le 17 septembre 2026, octobre et novembre affichaient déjà complet.
Les centres, leurs contacts, le relevé, et l'inscription.""",
       facts=["<strong>7 centres agréés</strong> à Lyon, le réseau le plus dense de France hors Paris.",
              "<strong>Alliance française de Lyon : DELF B2 159 €</strong>, les dix sessions de l'année.",
              "Le 17 septembre 2026, les sessions d'octobre et de novembre étaient complètes ; il restait décembre (écrit le 2).",
              "Résultats par courrier sous 6 semaines ; convocation par e-mail.",
              "Pièces pour l'inscription : identité, et votre numéro de candidat si vous avez déjà passé un DELF."],
       releve=[("Alliance française de Lyon", "DELF A1-B2, DALF", "<strong>B2 159 €</strong>", "Dix sessions par an ; 2026 : oct. et nov. complets le 17/09, déc. ouvert ; écrit 13 h 30-16 h 30 ; résultats 6 semaines."),
               ("ALPES Formation · GRETA CFA Lyon Métropole · Inflexyon · ILCF · Lyon Bleu · REN Formation", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le DELF B2 à Lyon ?", "À l'Alliance française de Lyon (159 €, dix sessions par an — octobre et novembre 2026 complets le 17 septembre, décembre ouvert) ou dans l'un des six autres centres agréés : ALPES Formation, GRETA CFA, Inflexyon, ILCF, Lyon Bleu, REN Formation."),
            ("Combien coûte le DELF à Lyon ?", "159 € le DELF B2 à l'Alliance française de Lyon (17 septembre 2026), l'un des prix les plus bas relevés en France ; les autres centres lyonnais ne publient pas de tarif lisible en ligne."),
            ("Quand s'inscrire au DELF à Lyon ?", "Le plus tôt possible : à l'Alliance française, les sessions d'octobre et de novembre 2026 étaient complètes deux mois avant. Chaque centre ferme ses inscriptions quatre à dix semaines avant l'écrit.")]),
    mk("delf-lille", "Lille", "fr", ["Lille"], exam="delf",
       title="DELF à Lille : Alliance française, B2 180 €, sessions 2027",
       desc="Où passer le DELF à Lille : l'Alliance française de Lille Métropole, seul centre agréé, A1 120 € à C2 210 €, novembre complet, février et juin 2027.",
       h1="Passer le DELF à Lille : l'Alliance française, ses prix et ses sessions 2027",
       intro="""À Lille, le DELF et le DALF se passent à l'<strong>Alliance française de Lille Métropole</strong> — seul
centre agréé de la ville — pour <strong>180 €</strong> le DELF B2 (120 € le A1, 210 € le C2). Le 29 octobre 2026, sa
session de novembre affichait <strong>complet</strong> ; la suivante, en <strong>février 2027</strong>, s'inscrit du
30 décembre 2026 au 6 janvier 2027, puis juin 2027 du 12 au 19 mai : une semaine, pas plus. Le centre, ses contacts,
le relevé, et l'inscription.""",
       facts=["<strong>1 centre agréé</strong> : Alliance française de Lille Métropole, 2 rue Bernos.",
              "<strong>A1 120 € · A2 130 € · B1 160 € · B2 180 € · C1 200 € · C2 210 €</strong> — inchangés depuis septembre.",
              "Novembre 2026 (écrits 3-5 novembre) : <strong>session complète</strong> dès la fermeture des inscriptions.",
              "<strong>Février 2027</strong> : inscriptions du 30 décembre 2026 (10 h) au 6 janvier 2027 (23 h 59) ; écrits A2 le 2 février à 14 h, B1 et B2 le 3 (10 h et 14 h), C1 et C2 le 4 ; oraux jusqu'au 16 février.",
              "<strong>Juin 2027</strong> : inscriptions du 12 au 19 mai ; écrits 15-17 juin, oraux jusqu'au 29 juin. Mai 2027 : DELF Junior B2 seulement (collégiens et lycéens), inscriptions 7-14 avril.",
              "Inscription par formulaire en ligne ouvert à l'heure dite ; Maubeuge et Valenciennes n'ont pas de centre DELF : Lille est le centre du Nord."],
       releve=[("Alliance française de Lille Métropole", "DELF A1-B2, DALF C1-C2 tout public ; DELF Junior B2 en mai", "A1 120 · A2 130 · B1 160 · <strong>B2 180</strong> · C1 200 · C2 210 €", "Nov. 2026 : complet (écrits 3-5 nov.) ; févr. 2027 : inscriptions 30 déc.-6 janv., écrits 2-4 févr., oraux jusqu'au 16 ; mai 2027 : Junior B2 (inscr. 7-14 avr., écrit 11 mai) ; juin 2027 : inscriptions 12-19 mai, écrits 15-17 juin, oraux jusqu'au 29.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("30 déc.", "ouverture des inscriptions", "session de février 2027"),
       faq=[("Où passer le DELF B2 à Lille ?", "À l'Alliance française de Lille Métropole, seul centre agréé de Lille : 180 €, prochaine session tout public en février 2027 (écrit le 3 février à 14 h), inscriptions du 30 décembre 2026 au 6 janvier 2027."),
            ("Combien coûte le DELF à Lille ?", "120 € le A1, 130 € le A2, 160 € le B1, 180 € le B2, 200 € le C1, 210 € le C2 à l'Alliance française de Lille Métropole (relu le 29 octobre 2026, inchangé depuis septembre)."),
            ("Quand s'inscrire au DELF à Lille ?", "Pendant la fenêtre d'une semaine ouverte par l'Alliance : du 30 décembre 2026 à 10 h au 6 janvier 2027 à 23 h 59 pour février 2027, du 12 au 19 mai pour juin 2027. La session de novembre 2026 était complète le 29 octobre : ne comptez pas sur une place tardive.")]),
    mk("delf-nantes", "Nantes", "fr", ["Nantes"], exam="delf",
       title="DELF à Nantes : Nantes Université, 125 €, sessions 2026-27",
       desc="Où passer le DELF à Nantes : l'i-FLE de Nantes Université, seul centre agréé, B1-B2 à 125 €, DALF 145 €, décembre 2026 complet, inscriptions 2027 dès février.",
       h1="Passer le DELF à Nantes : Nantes Université, ses prix et ses sessions 2027",
       intro="""À Nantes, le DELF et le DALF se passent à l'<strong>i-FLE de Nantes Université</strong> (campus Tertre) — seul
centre agréé de la ville — pour <strong>125 €</strong> le DELF B1 ou B2 et 145 € le DALF, le tarif le plus bas relevé en
France. Le 29 octobre 2026, la session des 2-4 décembre affichait <strong>complet</strong> ; les inscriptions de 2027
s'ouvrent à 7 h précises, deux jours seulement : les <strong>9-10 février</strong> (session des 17-19 mars, B1-B2), les
20-21 avril (26-28 mai, B1 à C2) et les 11-12 mai (16-18 juin, B1-B2). Le centre, le relevé, et l'inscription.""",
       facts=["<strong>1 centre agréé</strong> : Nantes Université, i-FLE (Service universitaire des langues), chemin de la Censive-du-Tertre, accueil Grand Hall, bâtiment 3 ; sul-fle@univ-nantes.fr.",
              "<strong>DELF B1 et B2 : 125 € · DALF C1 et C2 : 145 €</strong> (inchangés, page relue le 29 octobre 2026) ; ni A1 ni A2.",
              "Session des 2-4 décembre 2026 (B1 à C2) : <strong>complète</strong> ; inscriptions closes depuis les 22-23 septembre.",
              "2027 : <strong>17-19 mars</strong> (B1, B2 ; inscriptions 9-10 février), <strong>26-28 mai</strong> (B1 à C2 ; inscriptions 20-21 avril), <strong>16-18 juin</strong> (B1, B2 ; inscriptions 11-12 mai) — toujours à partir de 7 h, « dans la limite des places disponibles ».",
              "Écrits : B1 le mercredi matin, B2 le mercredi après-midi, C1 le jeudi matin, C2 le jeudi après-midi ; oraux le jour même ou les jours suivants (jamais le même jour pour B2 et C2) : restez disponible les trois jours.",
              "Inscription en ligne avec pièce d'identité jointe, paiement par carte ; convocations par e-mail seulement ; droits non remboursables ; une session peut être annulée faute de candidats."],
       releve=[("Nantes Université — i-FLE", "DELF B1, B2, DALF C1, C2 ; TCF tout public (QCM + écrit), TCF DAP", "<strong>B1-B2 125 €</strong> · C1-C2 145 €", "2-4 déc. 2026 : complet ; 17-19 mars 2027 (B1-B2, inscr. 9-10 févr. dès 7 h) ; 26-28 mai 2027 (B1-C2, inscr. 20-21 avr.) ; 16-18 juin 2027 (B1-B2, inscr. 11-12 mai) ; convocations par e-mail.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("9 févr.", "prochaine inscription", "session des 17-19 mars 2027"),
       faq=[("Où passer le DELF B2 à Nantes ?", "À l'i-FLE de Nantes Université (campus Tertre), seul centre agréé de la ville : 125 €, prochaines sessions les 17-19 mars, 26-28 mai et 16-18 juin 2027 ; celle de décembre 2026 est complète."),
            ("Combien coûte le DELF à Nantes ?", "125 € le DELF B1 ou B2, 145 € le DALF C1 ou C2 (page de l'i-FLE relue le 29 octobre 2026) : le tarif le plus bas que nous ayons relevé en France. Pas de A1 ni de A2 à Nantes."),
            ("Comment s'inscrire au DELF à Nantes ?", "En ligne, sur la plateforme de l'i-FLE, les deux jours d'ouverture à partir de 7 h (9-10 février 2027 pour mars, 20-21 avril pour mai, 11-12 mai pour juin), avec une carte d'identité ou un passeport ; paiement par carte à privilégier ; convocation par e-mail. Dans la limite des places : la session de décembre 2026 s'est remplie.")]),
    mk("delf-bordeaux", "Bordeaux", "fr", ["Bordeaux", "Pessac"], exam="delf", h2_label="Bordeaux et Pessac",
       title="DELF à Bordeaux : 3 centres, session de décembre 2026",
       desc="Où passer le DELF à Bordeaux : 3 centres agréés avec contacts — DEFLE Bordeaux Montaigne, Alliance française, Newdeal —, la session de décembre 2026.",

       h1="Passer le DELF à Bordeaux : les 3 centres agréés et la session de décembre 2026",
       intro="""À Bordeaux, le DELF et le DALF se passent dans <strong>%(n)d centres agréés</strong> par France Éducation
international : le DEFLE de l'université Bordeaux Montaigne (Pessac), l'Alliance française Bordeaux
Nouvelle-Aquitaine et Newdeal Institut. Le DEFLE ouvre la session du <strong>1<sup>er</sup> au 3 décembre 2026</strong>,
avec des <strong>inscriptions du 2 octobre au 4 novembre</strong>. Les centres, leurs contacts, le relevé, et
l'inscription.""",
       facts=["<strong>3 centres agréés</strong> : DEFLE Bordeaux Montaigne (Pessac), Alliance française Bordeaux Nouvelle-Aquitaine, Newdeal Institut.",
              "<strong>DEFLE : session de décembre 2026</strong> (A1-A2 le 1<sup>er</sup>, B1-B2 le 2, DALF le 3), inscriptions du 2 octobre au 4 novembre.",
              "L'oral du DEFLE se tient entre le 1<sup>er</sup> et le 15 décembre, date communiquée deux semaines avant.",
              "L'Alliance française publie un « calendrier et tarifs examens 2026 » et 2027 sur son site ; aménagements à signaler avant la date limite, avec certificat.",
              "Pièce d'identité en cours de validité obligatoire."],
       releve=[("Université Bordeaux Montaigne — DEFLE (Pessac)", "DELF A1-B2, DALF C1-C2", NR, "Session déc. 2026 : inscriptions 2 oct.-4 nov. ; oral entre le 1<sup>er</sup> et le 15 déc."),
               ("Alliance française Bordeaux Nouvelle-Aquitaine", "DELF A1-B2, DALF", "voir « Calendrier et tarifs examens 2026 »", "Inscription en ligne sur alliance-bordeaux.org."),
               ("Newdeal Institut", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le DELF B2 à Bordeaux ?", "Au DEFLE de l'université Bordeaux Montaigne (Pessac), avec une session du 1er au 3 décembre 2026 (inscriptions du 2 octobre au 4 novembre), à l'Alliance française Bordeaux Nouvelle-Aquitaine ou chez Newdeal Institut."),
            ("Combien coûte le DELF à Bordeaux ?", "Le DEFLE n'affiche pas son tarif sur la page consultée et l'Alliance française renvoie à son document « Calendrier et tarifs examens 2026 » ; ailleurs en France, un DELF B2 va de 125 à 280 € selon le centre."),
            ("Quand s'inscrire au DELF à Bordeaux ?", "Pour la session de décembre 2026 au DEFLE, entre le 2 octobre et le 4 novembre ; l'oral aura lieu entre le 1er et le 15 décembre.")]),
    mk("delf-marseille", "Marseille", "fr", ["Marseille", "Aix-En-Provence"], exam="delf", h2_label="Marseille et Aix-en-Provence",
       title="DELF à Marseille et Aix : 5 centres, 80 à 150 €, dates",
       desc="Où passer le DELF à Marseille et Aix : Alliance française et EPFF (A1 80 € à C1 150 €, décembre 2026 et 2027), E2C (20 places), IS Aix, DALF C1 à l'AMU.",
       h1="Passer le DELF à Marseille et Aix-en-Provence : les cinq centres agréés, leurs prix et leurs dates",
       intro="""À Marseille et à Aix-en-Provence, le DELF et le DALF se passent dans <strong>%(n)d centres agréés</strong> par France
Éducation international, aux prix les plus bas relevés : <strong>80 € le A1, 120 € le B2, 150 € le C1</strong> à
l'<strong>Alliance française Aix-Marseille Provence</strong> comme à l'<strong>EPFF</strong> (plus 15 € de dossier) et à
l'<strong>École de la 2<sup>e</sup> chance</strong>. Le 29 octobre 2026, les prochaines sessions étaient celles du 3-9 novembre
(E2C) et des 1<sup>er</sup>-3 décembre (Alliance, EPFF, IS Aix) ; l'Alliance publie déjà janvier et mars 2027. Le DALF C1 se
passe aussi à Aix-Marseille Université, une fois par an. Les centres, le relevé, et l'inscription.""",
       facts=["<strong>5 centres agréés</strong> : Alliance française Aix-Marseille Provence (72-74 rue Saint-Suffren à Marseille, 47 boulevard de la République à Aix), EPFF (21 rue Roux-de-Brignoles), École de la 2<sup>e</sup> chance (chemin de la Madrague-Ville), IS Aix-en-Provence, Aix-Marseille Université (SUL, Aix).",
              "<strong>Alliance française : A1 80 € · A2 95 € · B1 110 € · B2 120 € · C1 et C2 150 €</strong> ; tout public à Marseille les 1<sup>er</sup>-3 décembre 2026, 12-14 janvier et 16-18 mars 2027 ; à Aix les 3-5 novembre 2026 et 2-4 février 2027 ; DELF Junior à Aix seulement ; résultats en 4 à 6 semaines, à retirer sur place.",
              "<strong>EPFF : mêmes tarifs + 15 € de frais de dossier</strong> ; sessions tout public A1-B2 les 3-4 novembre et 1<sup>er</sup>-2 décembre 2026 (C1 trois fois par an), inscription trois semaines avant, sur place, par courriel ou par la poste ; résultats en 2-3 semaines ; 1 010 candidats en 2025.",
              "École de la 2<sup>e</sup> chance : DELF A1-B2 à 80, 95, 110 et 120 €, <strong>20 places par niveau</strong> dans l'ordre d'arrivée des dossiers ; session du 3 au 9 novembre 2026 (trois par an : mars, juin, novembre) ; inscription sur place les mardis et jeudis ; aucune préparation.",
              "IS Aix-en-Provence : A2 95 €, B1 110 €, B2 120 €, C1 150 € ; session des 1<sup>er</sup>-3 décembre 2026 (clôture le 2 novembre), puis dix sessions en 2027 de janvier à décembre, écrits sur trois jours.",
              "Aix-Marseille Université (SUL) : DALF C1 seulement, 150 € (étudiants AMU) ou 175 €, une session par an en mai (21-22 mai 2026, inscriptions 1<sup>er</sup>-21 avril), résultats en 2-3 semaines ; ni DELF ni C2."],
       releve=[("Alliance française Aix-Marseille Provence", "DELF A1-B2, DALF C1-C2 tout public (Marseille et Aix) ; Junior et épreuves d'entraînement à Aix", "A1 80 · A2 95 · B1 110 · <strong>B2 120</strong> · C1 150 · C2 150 €", "Marseille : 1<sup>er</sup>-3 déc. 2026 (tous niveaux), 12-14 janv. 2027, 16-18 mars 2027 ; Aix : 3-5 nov. 2026, 2-4 févr. 2027 ; inscription en ligne ; résultats 4-6 semaines sur place, diplôme 2-4 mois."),
               ("EPFF — Espace Pédagogie Formation France", "DELF tout public A1-B2, DALF C1", "A1 80 · A2 95 · B1 110 · <strong>B2 120</strong> · C1 150 € + 15 € de dossier", "3-4 nov. et 1<sup>er</sup>-2 déc. 2026 (A1-B2) ; 10 sessions par an ; clôture 3 semaines avant ; dossier sur place, courriel ou poste ; résultats 2-3 semaines."),
               ("École de la 2e chance de Marseille", "DELF tout public A1-B2", "A1 80 · A2 95 · B1 110 · B2 120 €", "3-9 nov. 2026 ; 20 places par niveau ; inscription sur place mardi et jeudi (9 h-12 h, 14 h-17 h) ; carte ou virement ; 3 sessions par an."),
               ("IS Aix-en-Provence · Aix-Marseille Université (SUL)", "IS : DELF A2-B2, DALF C1 ; SUL : DALF C1 seulement", "IS : A2 95 · B1 110 · B2 120 · C1 150 € ; SUL : C1 150 € (AMU) / 175 €", "IS : 1<sup>er</sup>-3 déc. 2026 (clôture 2 nov.), 2027 : 12-14 janv., 2-4 févr., 16-18 mars, 25-27 mai, 15-17 juin, 6-8 juil., 3-5 août, 5-7 oct., 16-18 nov., 7-9 déc. ; SUL : mai (2026 : 21-22 mai, inscr. 1<sup>er</sup>-21 avril), 2027 non publié.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("80 €", "DELF A1 (AF, EPFF, E2C)", "le moins cher relevé"),
       faq=[("Où passer le DELF B2 à Marseille ?", "À l'Alliance française (120 €, 1er-3 décembre 2026 puis 12-14 janvier et 16-18 mars 2027), à l'EPFF (120 € plus 15 € de dossier, 1er-2 décembre 2026) ou à l'École de la 2e chance (120 €, 3-9 novembre 2026, 20 places) ; à Aix, chez IS Aix-en-Provence (120 €, clôture le 2 novembre pour décembre)."),
            ("Combien coûte le DELF à Marseille ?", "Relevé du 29 octobre 2026 : 80 € le A1, 95 € le A2, 110 € le B1, 120 € le B2, 150 € le C1 dans les trois centres marseillais (l'EPFF ajoute 15 € de dossier) ; 150 € le C2 à l'Alliance ; DALF C1 à 150 ou 175 € à Aix-Marseille Université."),
            ("Peut-on s'entraîner au DELF à Marseille ?", "L'Alliance française propose des épreuves d'entraînement A2, B1 et B2 (35 €, au centre d'Aix) ; l'École de la 2e chance n'offre aucune préparation ; l'EPFF, IS Aix et l'Alliance sont aussi des écoles de langue.")]),
    mk("delf-toulouse", "Toulouse", "fr", ["Toulouse"], exam="delf",
       title="DELF à Toulouse : 5 centres, un DELF par mois, prix et dates",
       desc="Où passer le DELF à Toulouse : Alliance française (A1-B2, un DELF par mois, 160-190 €), CREPT (1er-2 décembre 2026), DEFLE (B1-C2 en mai), SPLE, Langue Onze.",
       h1="Passer le DELF à Toulouse : les cinq centres agréés, leurs prix et leurs sessions",
       intro="""À Toulouse, le DELF et le DALF se passent dans <strong>%(n)d centres agréés</strong> par France Éducation
international. L'<strong>Alliance française</strong> et le <strong>CREPT</strong> organisent un DELF tout public
<strong>chaque mois</strong> (A1 à B2) ; le <strong>DEFLE</strong> de l'Université Toulouse Jean-Jaurès, seul à proposer
le DALF, une session par an, en mai ; <strong>Langue Onze</strong> (A2-C1) et <strong>SPLE</strong> (agréé depuis 2026)
complètent l'offre. Le 29 octobre 2026, la prochaine inscription ouverte était celle du CREPT pour le 1<sup>er</sup>-2 décembre
(jusqu'au 3 novembre) ; l'Alliance ouvre le 10 novembre pour janvier 2027. Les centres, le relevé, et l'inscription.""",
       facts=["<strong>5 centres agréés</strong> : Alliance française (3 bis rue Guy-Hersant), CREPT Formation (130 rue Henri-Desbals), DEFLE de l'Université Toulouse Jean-Jaurès, Langue Onze (10 rue des Arts), SPLE Vidal (10 rue Sesquières).",
              "<strong>Alliance française : A1 et A2 160 €, B1 180 €, B2 190 €</strong> (50 € de frais d'inscription inclus, dus à la première inscription) ; un DELF par mois, deux niveaux par session ; janvier 2027 (A2 le 12, B2 le 13) s'inscrit du 10 au 27 novembre 2026, février (A2, B1) du 24 novembre au 11 décembre, mars (B1, B2) du 19 janvier au 5 février.",
              "<strong>CREPT : A1 159 €, A2 161 €, B1 183 €, B2 196 €</strong> ; session du 1<sup>er</sup>-2 décembre 2026 (inscriptions jusqu'au 3 novembre), une par mois, résultats sous 4 à 6 semaines ; 139 candidats au B2 en 2025, 73 % de réussite.",
              "<strong>DEFLE (Université) : B1 140 €, B2 150 €, C1 et C2 160 €</strong> pour les candidats extérieurs (90 à 110 € pour ses étudiants) ; une seule session par an, en mai, inscriptions en mars sur eCandidat ; session 2027 non publiée.",
              "SPLE (agréé depuis 2026) : A2 130 €, B1 165 €, B2 185 €, C1 215 €, dates à demander au centre ; Langue Onze : A2-B2 et C1, inscription sur klf-examen.fr, résultats par e-mail sous 4 à 8 semaines.",
              "Inscription en ligne à l'Alliance (boutique et bulletin signé), au DEFLE (eCandidat) et chez Langue Onze ; par dossier au CREPT et chez SPLE ; places limitées partout ; diplôme environ 2 mois après les résultats à l'Alliance, 6 mois au CREPT."],
       releve=[("Alliance française de Toulouse", "DELF tout public A1-B2 (pas de DALF) ; TCF IRN, TP, examen civique", "A1 160 · A2 160 · <strong>B1 180 · B2 190 €</strong> (frais 50 € inclus)", "Déc. 2026 (A1 1<sup>er</sup>, B2 2 déc.) clos ; janv. 2027 A2 12, B2 13 (inscr. 10-27 nov.) ; févr. A2 2, B1 3 (inscr. 24 nov.-11 déc.) ; mars B1-B2 17 (inscr. 19 janv.-5 févr.) ; résultats 4-5 semaines après."),
               ("CREPT Formation", "DELF tout public A1-B2 (papier) ; TCF IRN, TEF", "A1 159 · A2 161 · B1 183 · <strong>B2 196 €</strong>", "1<sup>er</sup>-2 déc. 2026 (A1-A2 le 1<sup>er</sup>, B1-B2 le 2 ; limite 3 nov.) ; une session par mois, limite 4 semaines avant ; calendrier 2027 non publié ; convocation 2 semaines avant."),
               ("Université Toulouse Jean-Jaurès — DEFLE", "DELF B1, B2, DALF C1, C2 (une session par an)", "B1 140 · B2 150 · C1 160 · C2 160 € (extérieurs)", "Mai 2026 : écrits 20-21 mai, inscriptions 2-27 mars (eCandidat) ; mai 2027 attendu, non publié ; aucun cours de préparation."),
               ("Langue Onze (réseau KLF) · SPLE Vidal", "Langue Onze : A2-B2, C1 ; SPLE : A2-B2, C1", "SPLE : A2 130 · B1 165 · B2 185 · C1 215 € ; Langue Onze : non relevé", "Langue Onze : inscription sur klf-examen.fr, dates dans le formulaire, « 3 à 4 semaines à l'avance » ; SPLE : dates à demander au centre.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("3 nov.", "limite CREPT", "session du 1er-2 déc. 2026"),
       faq=[("Où passer le DELF B2 à Toulouse ?", "Chaque mois à l'Alliance française (190 €, prochaine inscription du 10 au 27 novembre 2026 pour le 13 janvier 2027) ou au CREPT (196 €, 2 décembre 2026, inscriptions jusqu'au 3 novembre) ; une fois par an, en mai, au DEFLE de l'Université (150 €) ; aussi chez Langue Onze et SPLE (185 €)."),
            ("Combien coûte le DELF à Toulouse ?", "Relevé du 29 octobre 2026 : B2 de 150 € (DEFLE, candidats extérieurs) à 196 € (CREPT), 185 € chez SPLE, 190 € à l'Alliance frais inclus ; A1 159-160 € ; B1 165-183 € ; DALF C1 160 € au DEFLE, 215 € chez SPLE."),
            ("Quand s'inscrire au DELF à Toulouse ?", "Quatre à huit semaines avant l'écrit : l'Alliance ouvre chaque fenêtre deux mois avant la session (10-27 novembre pour janvier 2027), le CREPT ferme quatre semaines avant (3 novembre pour le 1er-2 décembre 2026), le DEFLE n'inscrit qu'en mars pour mai.")]),
    mk("delf-montpellier", "Montpellier", "fr", ["Montpellier"], exam="delf",
       title="DELF à Montpellier : IEFE (B2-C2), GRETA (A1-C2), dates 2027",
       desc="Où passer le DELF à Montpellier : IEFE Paul-Valéry (B2 180 €, C1-C2 200 €, session 2-4 décembre 2026) et GRETA (A1 100 € à C2 200 €, calendrier 2027 ouvert).",
       h1="Passer le DELF à Montpellier : les deux centres agréés, leurs prix et leurs sessions",
       intro="""À Montpellier, le DELF et le DALF se passent dans <strong>%(n)d centres agréés</strong> par France Éducation
international, qui se complètent : le centre DELF-DALF de l'<strong>IEFE, Université Paul-Valéry</strong> (route de Mende)
ne fait passer que le <strong>B2, le C1 et le C2</strong> — prochaine session du 2 au 4 décembre 2026, inscriptions jusqu'au
13 novembre — ; le <strong>GRETA CFA Montpellier Littoral</strong> (lycée Jean-Mermoz) couvre <strong>A1 à C2</strong> et a
ouvert le 18 octobre les inscriptions de tout son calendrier 2027. Les centres, le relevé du 29 octobre 2026, et l'inscription.""",
       facts=["<strong>2 centres agréés</strong> : IEFE Paul-Valéry (route de Mende, secrétariat bâtiment Ionesco, bureau 08) et GRETA CFA Montpellier Littoral (717 avenue Jean-Mermoz).",
              "<strong>IEFE : B2 180 €, C1 200 €, C2 200 €</strong> ; session des 2-4 décembre 2026 (B2 le 2 à 14 h, C1 le 3 à 9 h, C2 le 3 à 14 h 30, oraux du 2 au 4), <strong>inscriptions du 9 octobre au 13 novembre</strong> au secrétariat ou par courrier (bulletin, copie du passeport, règlement) ; calendrier 2027 non publié.",
              "<strong>GRETA : A1 100 €, A2 120 €, B1 160 €, B2 180 €, C1 et C2 200 €</strong> ; pré-inscription en ligne, paiement par virement ou chèque ; « tout dossier incomplet ou hors délai sera rejeté ».",
              "GRETA, calendrier 2027 (inscriptions ouvertes depuis le 18 octobre 2026) : janvier A1-B2 (écrits 12-13 janvier, inscriptions jusqu'au 11 décembre), février A1-C2 (2-4 février, jusqu'au 8 janvier), mars, mai, juin (A1-B1), juillet (A1-B2), octobre (A1-C2), novembre, décembre ; C1-C2 en février et octobre seulement.",
              "Le site de l'IEFE répond sur iefe.www.univ-montp3.fr (l'ancien hôte iefe.univ-montp3.fr renvoie une erreur de certificat) ; secrétariat ouvert du lundi au vendredi le matin, et l'après-midi sauf le jeudi.",
              "Ni A1-B1 à l'IEFE, ni session de l'IEFE en 2027 publiée le 29 octobre : pour ces niveaux et ces dates, le GRETA est le centre de la ville."],
       releve=[("Université Paul-Valéry Montpellier 3 — IEFE, centre DELF-DALF", "DELF B2, DALF C1, C2", "<strong>B2 180</strong> · C1 200 · C2 200 €", "2-4 déc. 2026 : B2 2 déc. 14 h, C1 3 déc. 9 h, C2 3 déc. 14 h 30, oraux 2-4 déc. ; inscriptions 9 oct.-13 nov. 2026 (sur place ou courrier) ; nov. 2026 close ; 2027 non publié."),
               ("GRETA CFA Montpellier Littoral", "DELF A1-B2, DALF C1-C2 tout public", "A1 100 · A2 120 · B1 160 · <strong>B2 180</strong> · C1 200 · C2 200 €", "Déc. 2026 (A1-B1) ; 2027 : janv. 12-13 (A1-B2, inscr. jusqu'au 11 déc.), févr. 2-4 (A1-C2, jusqu'au 8 janv.), mars 16-17, mai 25-26, juin 15-16, juil. 6-7, oct. 5-7 (A1-C2), nov., déc. ; pré-inscription en ligne depuis le 18 oct. 2026.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("13 nov.", "limite IEFE", "session du 2-4 déc. 2026"),
       faq=[("Où passer le DELF B2 à Montpellier ?", "À l'IEFE de l'Université Paul-Valéry (180 €, écrit le 2 décembre 2026 à 14 h, inscriptions jusqu'au 13 novembre) ou au GRETA CFA Montpellier Littoral (180 €, écrit le 13 janvier 2027 à 14 h, inscriptions jusqu'au 11 décembre, puis février, juillet, octobre)."),
            ("Combien coûte le DELF à Montpellier ?", "Relevé du 29 octobre 2026 : 180 € le B2 et 200 € le C1 ou le C2 dans les deux centres ; A1 100 €, A2 120 €, B1 160 € au GRETA, seul à les proposer. L'IEFE facture 20 € l'envoi du diplôme en recommandé."),
            ("Quand s'inscrire au DELF à Montpellier ?", "À l'IEFE, cinq semaines avant l'écrit (du 9 octobre au 13 novembre pour décembre 2026) ; au GRETA, un mois avant (11 décembre pour janvier 2027, 8 janvier pour février), toutes les fenêtres 2027 étant ouvertes depuis le 18 octobre 2026.")]),
    mk("delf-strasbourg", "Strasbourg", "fr", ["Strasbourg"], exam="delf",
       title="DELF à Strasbourg : 3 centres, B2 200 €, sessions 2026-2027",
       desc="Où passer le DELF à Strasbourg : Alliance française (A2 160 € à C2 240 €, session 1er-11 décembre, calendrier 2027), Pôle FLE-IIEF (B2, C1, C2), DELF Prim.",
       h1="Passer le DELF à Strasbourg : les trois centres agréés, leurs prix et leurs sessions",
       intro="""À Strasbourg, le DELF et le DALF se passent dans <strong>%(n)d centres agréés</strong> par France Éducation
international, qui ne se recouvrent pas : l'<strong>Alliance française Strasbourg Europe</strong> (12 rue des Pontonniers)
ouvre dix sessions tout public par an, du A2 au C2 — la prochaine du <strong>1<sup>er</sup> au 11 décembre 2026</strong>,
inscriptions dès le 2 novembre à 0 h 01 — ; le <strong>Pôle FLE-IIEF</strong> de l'Université ne propose que le DELF B2 et
le DALF C1-C2, une session en mai ; l'<strong>École européenne</strong> n'organise que le DELF Prim A2. Les centres, le
relevé du 29 octobre 2026, et l'inscription.""",
       facts=["<strong>3 centres agréés</strong> : Alliance française Strasbourg Europe (tout public A2-C2), Pôle FLE-IIEF de l'Université (B2, C1, C2), École européenne (DELF Prim A2 seulement).",
              "<strong>Alliance française : A2 160 € · B1 180 € · B2 200 € · C1 240 € · C2 240 €</strong> ; pas de A1 au calendrier.",
              "Prochaine session à l'Alliance : du <strong>1<sup>er</sup> au 11 décembre 2026</strong>, inscriptions ouvertes à partir du 2 novembre 2026 à 0 h 01 — « les places partent très vite ».",
              "Calendrier 2027 de l'Alliance (PDF officiel, 10 sessions) : A2-B1-B2 en février (inscriptions 3-17 janvier, écrits 2-3 février), mars, mai, juin, août, octobre et décembre ; C1-C2 en janvier (inscriptions 1<sup>er</sup>-20 décembre 2026, écrit le 14 janvier), juillet et novembre ; rien en avril ni en septembre.",
              "Pôle FLE-IIEF : B2 200 €, C1 250 €, C2 250 € (10 % de moins pour ses étudiants) ; inscription par bulletin envoyé par e-mail puis lien de paiement ; dernière session affichée : mai 2026, la suivante non publiée le 29 octobre.",
              "École européenne : DELF Prim A2, épreuve le 13 mai 2027, inscriptions des candidats extérieurs du 1<sup>er</sup> février au 7 mars 2027, 20 € de frais."],
       releve=[("Alliance française Strasbourg Europe", "DELF A2-B2, DALF C1-C2 tout public ; préparation B1/B2", "A2 160 · B1 180 · <strong>B2 200</strong> · C1 240 · C2 240 €", "1<sup>er</sup>-11 déc. 2026 (inscriptions dès le 2 nov., 0 h 01) ; 2027 : C1-C2 14 janv. (inscr. 1<sup>er</sup>-20 déc.), A2-B2 2-3 févr. (inscr. 3-17 janv.), 16-17 mars, 25-26 mai, 15-16 juin, 3-4 août, 5-6 oct., 7-8 déc. ; C1-C2 8 juil., 18 nov."),
               ("Pôle FLE-IIEF, Université de Strasbourg", "DELF B2, DALF C1, C2", "B2 200 · C1 250 · C2 250 € (étudiants du pôle : 180 · 225 · 225)", "Mai 2026 : inscriptions 2-27 mars, écrits 20-21 mai ; session suivante non publiée ; bulletin par e-mail, paiement en ligne, convocation 3 semaines après la clôture."),
               ("École européenne de Strasbourg", "DELF Prim A2 (élèves du primaire)", "20 € (candidats extérieurs)", "13 mai 2027 ; inscriptions externes 1<sup>er</sup> févr.-7 mars 2027 (formulaire en ligne) ; une session par an.")],
       releve_date="29 octobre 2026", modified=("2026-10-29", "29 octobre 2026"),
       stat3=("1er déc.", "prochaine session (AF)", "inscriptions dès le 2 nov."),
       faq=[("Où passer le DELF B2 à Strasbourg ?", "À l'Alliance française Strasbourg Europe (200 €, prochaine session du 1er au 11 décembre 2026, puis février 2027) ou au Pôle FLE-IIEF de l'Université (200 €, une session en mai). L'École européenne ne fait passer que le DELF Prim."),
            ("Combien coûte le DELF à Strasbourg ?", "À l'Alliance française (29 octobre 2026) : 160 € le A2, 180 € le B1, 200 € le B2, 240 € le C1 et le C2. Au Pôle FLE-IIEF : 200 € le B2, 250 € le C1 et le C2, 10 % de moins pour ses étudiants. Pas de A1 relevé dans la ville."),
            ("Quand s'inscrire au DELF à Strasbourg ?", "À l'Alliance, dès le 2 novembre 2026 à 0 h 01 pour la session de décembre, puis du 1er au 20 décembre pour le C1-C2 du 14 janvier 2027 et du 3 au 17 janvier pour les A2-B2 des 2 et 3 février ; chaque fenêtre dure deux à trois semaines et les places partent vite. Au Pôle FLE-IIEF, les inscriptions de la session de mai se font en mars.")]),
]
