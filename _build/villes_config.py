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
       title="TCF à Rennes : centres agréés, prix CLPS et inscription",
       desc="Les 2 centres TCF agréés à Rennes avec contacts — CLPS, Langue et Communication —, les tarifs du CLPS (IRN 180 €, Canada 285 €), Brest, Saint-Brieuc, Vannes.",

       h1="Passer le TCF à Rennes : centres agréés, prix et inscription",
       intro="""À Rennes, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international :
le <strong>CLPS L'Enjeu Compétences</strong>, qui publie une grille complète — TCF IRN <strong>180 €</strong>,
TCF Canada <strong>285 €</strong>, tout public 110 € plus 52 € par expression — et organise aussi l'IRN à
Brest, Saint-Brieuc et Vannes et le TCF Canada à Brest, et Langue et Communication. Les centres avec leurs
contacts, le relevé, et l'inscription.""",
       facts=["<strong>2 centres agréés</strong> à Rennes : CLPS L'Enjeu Compétences (ordinateur) et Langue et Communication.",
              "<strong>CLPS : TCF IRN 180 €, TCF Canada 285 €, TCF tout public 110 € + 52 € par expression, TCF Québec à partir de 71 € l'épreuve.</strong>",
              "Le CLPS fait passer le TCF IRN à Rennes, Brest, Saint-Brieuc et Vannes, et le TCF Canada à Rennes et Brest.",
              "Inscription par fiche en ligne, sur clps.net.",
              "285 € : le TCF Canada le plus cher relevé en France — pour un test identique à celui d'ACTE à 195 €."],
       releve=[("CLPS L'Enjeu Compétences", "IRN (Rennes, Brest, Saint-Brieuc, Vannes), Canada (Rennes, Brest), Québec, tout public", "IRN <strong>180 €</strong> · Canada <strong>285 €</strong> · TP 110 € + 52 € + 52 € · Québec CO 71 €", "Fiches d'inscription en ligne ; sur ordinateur."),
               ("Langue et Communication", NR, NR, "Page « centre d'examen du TCF » du site.")],
       faq=[("Où passer le TCF Canada à Rennes ?", "Au CLPS L'Enjeu Compétences (285 €, inscription par fiche en ligne, aussi à Brest) ou chez Langue et Communication, tous deux agréés par France Éducation international."),
            ("Combien coûte le TCF à Rennes ?", "Au CLPS (17 septembre 2026) : 180 € le TCF IRN, 285 € le TCF Canada, 110 € les épreuves obligatoires du tout public plus 52 € par expression. Langue et Communication ne publie pas de tarif lisible."),
            ("Peut-on passer le TCF ailleurs en Bretagne ?", "Oui : le CLPS organise le TCF IRN à Brest, Saint-Brieuc et Vannes, et le TCF Canada à Brest ; l'Alliance française Saint-Malo Bretagne est aussi agréée.")]),
    mk("tcf-strasbourg", "Strasbourg", "fr", ["Strasbourg"],
       title="TCF à Strasbourg : 3 centres agréés, contacts, inscription",
       desc="Les 3 centres TCF agréés à Strasbourg avec contacts — Alliance française (IRN et tout public seulement), CIEL, Stralang —, ce qu'ils proposent.",

       h1="Passer le TCF à Strasbourg : les 3 centres agréés et l'inscription",
       intro="""À Strasbourg, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international,
tous avec des sessions sur ordinateur : l'<strong>Alliance française Strasbourg Europe</strong> — qui ne
propose que le TCF IRN et le tout public, pas le TCF Canada —, le CIEL et l'Institut Stralang. Les centres
avec leurs contacts, ce que nous avons relevé, et l'inscription.""",
       facts=["<strong>3 centres agréés</strong> : Alliance française Strasbourg Europe, CIEL, Institut Stralang.",
              "<strong>Alliance française : TCF IRN (papier et ordinateur) et TCF tout public seulement</strong> — pas de TCF Canada.",
              "Pour le TCF Canada, vérifiez le CIEL et Stralang, ou les centres de Nancy, Metz et Mulhouse.",
              "L'Alliance propose des cours de préparation au TCF IRN (2 séances de 2 h).",
              "20 à 30 jours entre deux passations ; attestation valable 2 ans."],
       releve=[("Alliance française Strasbourg Europe", "IRN (papier et ordinateur), tout public — pas de Canada", NR, "Pages « Examen TCF » et « TCF IRN sur ordinateur » du site."),
               ("CIEL · Institut Stralang", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le TCF Canada à Strasbourg ?", "Pas à l'Alliance française Strasbourg Europe, qui ne propose que le TCF IRN et le tout public ; le CIEL et l'Institut Stralang sont agréés — vérifiez sur leur site qu'ils organisent la déclinaison Canada."),
            ("Où passer le TCF IRN à Strasbourg ?", "À l'Alliance française Strasbourg Europe, sur papier ou sur ordinateur, au CIEL ou chez Stralang."),
            ("Combien coûte le TCF à Strasbourg ?", "Les centres strasbourgeois ne publient pas de tarif lisible en ligne ; en France, un TCF IRN va de 140 à 220 € selon le centre.")]),
    mk("tcf-lille", "Lille", "fr", ["Lille"],
       title="TCF à Lille : centres agréés, contacts et inscription",
       desc="Les 2 centres TCF agréés à Lille avec adresse, téléphone et site — E2LF et Institut Langues et Savoirs (ISPA), sur ordinateur — et l'inscription.",

       h1="Passer le TCF à Lille : les centres agréés et l'inscription",
       intro="""À Lille, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international,
tous deux avec des sessions sur ordinateur : l'École lilloise de langue française (E2LF) et l'Institut
Langues et Savoirs (ISPA). Ni l'un ni l'autre ne publie de tarif lisible en ligne. Les centres avec leurs
contacts, et l'inscription — et pour le DELF, l'Alliance française de Lille Métropole.""",
       facts=["<strong>2 centres agréés</strong> : E2LF et ISPA, sur ordinateur.",
              "Vérifiez la déclinaison — IRN, Canada — sur le site de chaque centre.",
              "Pour le DELF, c'est l'Alliance française de Lille Métropole (B2 à 180 €).",
              "Maubeuge (ID Formation) est aussi agréé dans le Nord.",
              "20 à 30 jours entre deux passations ; attestation valable 2 ans."],
       releve=[("E2LF · Institut Langues et Savoirs (ISPA)", NR, NR, "Sur le site du centre ; sessions sur ordinateur déclarées à FEI.")],
       faq=[("Où passer le TCF Canada à Lille ?", "Chez E2LF ou à l'Institut Langues et Savoirs (ISPA), tous deux agréés et sur ordinateur, après vérification sur leur site qu'ils organisent la déclinaison Canada."),
            ("Combien coûte le TCF à Lille ?", "Les deux centres lillois ne publient pas de tarif lisible en ligne ; en France, un TCF IRN va de 140 à 220 € et un TCF Canada de 195 à 285 €."),
            ("Où passer le DELF à Lille ?", "À l'Alliance française de Lille Métropole : A1 120 €, A2 130 €, B1 160 €, B2 180 €, C1 200 €, C2 210 €, session de novembre 2026 avec inscriptions du 30 septembre au 7 octobre.")]),
    mk("tcf-nice", "Nice", "fr", ["Nice"],
       title="TCF à Nice : 3 centres agréés, contacts et inscription",
       desc="Les 3 centres TCF agréés à Nice avec adresse, téléphone et site — Alliance française Nice Côte d'Azur, Les Ateliers FL, FOLAM — et l'inscription.",

       h1="Passer le TCF à Nice : les 3 centres agréés et l'inscription",
       intro="""À Nice, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation international, dont
%(so)d avec des sessions sur ordinateur : l'Alliance française Nice Côte d'Azur, Les Ateliers FL et la
Ligue de l'enseignement (FOLAM). Cagnes-sur-Mer et Valbonne comptent deux centres de plus. Les centres avec
leurs contacts, et l'inscription.""",
       facts=["<strong>3 centres agréés</strong> dans Nice, 2 sur ordinateur ; 2 autres à Cagnes-sur-Mer et Valbonne.",
              "Vérifiez la déclinaison — IRN, Canada — sur le site de chaque centre.",
              "Aucun tarif lisible en ligne relevé pour Nice.",
              "Pour le DELF, le CUEFLE de l'Université Côte d'Azur.",
              "20 à 30 jours entre deux passations ; attestation valable 2 ans."],
       releve=[("Alliance française Nice Côte d'Azur · Les Ateliers FL · FOLAM", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le TCF Canada à Nice ?", "À l'Alliance française Nice Côte d'Azur, aux Ateliers FL ou à la FOLAM, tous trois agréés, après vérification sur leur site qu'ils organisent la déclinaison Canada."),
            ("Combien coûte le TCF à Nice ?", "Les centres niçois ne publient pas de tarif lisible en ligne ; en France, un TCF IRN va de 140 à 220 € et un TCF Canada de 195 à 285 €."),
            ("Comment s'inscrire au TCF à Nice ?", "En ligne, sur le site du centre choisi, quelques jours avant la session, avec une pièce d'identité et un paiement par carte.")]),
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
       desc="Les 2 centres TCF agréés dans la ville de Québec avec contacts — Collège Stanislas (Sainte-Foy), Université Laval —, leurs règles et l'inscription.",

       h1="Passer le TCF à Québec : les deux centres agréés et l'inscription",
       intro="""Dans la ville de Québec, le TCF se passe dans <strong>%(n)d centres agréés</strong> par France Éducation
international, tous deux sur ordinateur : le <strong>Collège Stanislas</strong> (Sainte-Foy) et
l'<strong>École de langues de l'Université Laval</strong>. Ils proposent le TCF Canada et le TCF Québec —
attention à la case cochée : seul le TCF Canada sert à Entrée express. Les centres, leurs contacts, les
règles relevées, et l'inscription.""",
       facts=["<strong>2 centres agréés</strong> : Collège Stanislas (1605, chemin Sainte-Foy) et Université Laval (pavillon Charles-De Koninck).",
              "<strong>Collège Stanislas</strong> : Québec, Canada, tout public, IRN ; 15 $ retenus par épreuve si annulation à plus de 15 jours ; 20 jours entre deux passations.",
              "Autres centres du Québec : Trois-Rivières (UQTR, 440 $), Chicoutimi, Sherbrooke, Rouyn-Noranda, Gaspé, Sept-Îles, Baie-Comeau…",
              "Résultats par e-mail sous 2 à 4 semaines ; attestation valable 2 ans.",
              "Le TCF Canada est aussi reconnu par le MIFI depuis 2022."],
       releve=[("Collège Stanislas (Québec)", "Québec, Canada, tout public, IRN", NR, "Paiement complet à l'inscription ; report gratuit à plus de 15 jours ; 15 $ par épreuve si annulation ; 20 jours entre deux passations."),
               ("Université Laval (ELUL)", NR, NR, "Page « tests de langues » de l'École de langues.")],
       faq=[("Où passer le TCF Canada à Québec ?", "Au Collège Stanislas de Québec (Sainte-Foy) ou à l'Université Laval, tous deux agréés et sur ordinateur ; inscription en ligne sur leur site."),
            ("Combien coûte le TCF à Québec ?", "Aucun des deux centres ne publie de tarif lisible sur la page consultée ; à l'UQTR, à Trois-Rivières, le TCF Canada coûte 440 $ et le TCF Québec 105 à 125 $ par épreuve (30 juillet 2026)."),
            ("TCF Canada ou TCF Québec à Québec ?", "Pour un programme du Québec, les deux sont acceptés ; pour Entrée express ou la citoyenneté, seul le TCF Canada. Le TCF Québec permet de ne passer que les épreuves exigées.")]),
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
       desc="TCF à Annaba : rendez-vous sur la plateforme IFAL (VFS), TCF Canada 37 500 DA, examen au « Majestic », 36 jours entre deux inscriptions, contacts.",
       h1="Passer le TCF à Annaba : l'antenne de l'Institut français et l'inscription",
       intro="""À Annaba, le TCF — Canada, Québec, IRN, tout public, DAP — se passe dans <strong>un seul centre agréé</strong>
par France Éducation international : l'antenne de l'<strong>Institut français d'Algérie</strong>, 6, route
de l'Avant-Port, avec des sessions sur ordinateur. Le rendez-vous se prend exclusivement en ligne, sur la
plateforme IFAL opérée par VFS Global ; selon la page de l'antenne relue le 17 octobre 2026, le TCF Canada coûte
<strong>37 500 DA</strong> et se passe à l'Institut français d'Annaba, « Majestic ». Le centre, ses contacts, et
l'inscription.""",
       facts=["<strong>1 centre agréé</strong> : Institut français d'Algérie, antenne d'Annaba, 6 route de l'Avant-Port.",
              "Lieu de passation indiqué pour le TCF Canada : « <strong>Institut Français d'Annaba, Majestic</strong> ».",
              "Rendez-vous <strong>en ligne uniquement</strong> sur la plateforme IFAL (VFS Global), depuis if-algerie.com ; assistance VFS : info.tcfalg@vfshelpline.com, 021 99 60 08.",
              "<strong>TCF Canada : 37 500 DA</strong> TTC (17 octobre 2026).",
              "Sessions <strong>chaque mois</strong> ; <strong>36 jours</strong> entre deux inscriptions selon la page de l'antenne (26 sur la page nationale).",
              "⚠️ if-algerie.fr est une escroquerie ; l'officiel est if-algerie.com."],
       releve=[("Institut français d'Algérie — antenne d'Annaba", "Canada, Québec, IRN, tout public, DAP", "Canada <strong>37 500 DA</strong> · autres déclinaisons : non relevé", "Plateforme IFAL, sessions mensuelles, 36 jours entre deux inscriptions ; passation au « Majestic » ; rubrique calendrier vide ; examens.annaba@if-algerie.com.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       stat3=("37 500 DA", "TCF Canada", "tarif de l'antenne, 17 oct. 2026"),
       faq=[("Où passer le TCF Canada à Annaba ?", "Auprès de l'antenne de l'Institut français d'Algérie d'Annaba (6, route de l'Avant-Port), seul centre agréé de la ville. Le 17 octobre 2026, sa page indiquait comme lieu de passation « Institut Français d'Annaba, Majestic » : vérifiez l'adresse sur votre convocation."),
            ("Comment s'inscrire au TCF à Annaba ?", "Exclusivement en ligne, sur la plateforme IFAL (VFS Global), depuis la page TCF de if-algerie.com. Assistance VFS : info.tcfalg@vfshelpline.com, 021 99 60 08 ; pour le reste, examens.annaba@if-algerie.com."),
            ("Combien coûte le TCF à Annaba ?", "37 500 DA TTC pour le TCF Canada, selon la page de l'antenne relue le 17 octobre 2026. Les autres antennes affichent 19 500 DA pour le TCF DAP et 13 000 DA pour le TCF tout public ; le montant exact s'affiche sur la plateforme IFAL au moment de payer."),
            ("Combien de jours entre deux inscriptions ?", "36 jours, selon la page de l'antenne d'Annaba relue le 17 octobre 2026 ; la page nationale de l'Institut écrit 26. Par prudence, comptez 36 jours.")]),
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
       desc="TCF Canada à Rabat : 2 900 Dhs à l'Institut français, 8 sessions ouvertes du 22 octobre au 10 décembre 2026, inscription en ligne, Kénitra à 40 km.",
       h1="Passer le TCF Canada à Rabat : l'Institut français, le prix et les dates",
       intro="""À Rabat, le TCF se passe à l'<strong>Institut français</strong>, 15 rue Al Madina (quartier Hassan) — seul
centre agréé de la ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada. Le 17 octobre 2026,
son site listait <strong>huit sessions ouvertes</strong>, du 22 octobre au 10 décembre (le 23 octobre complet).
Kénitra, à 40 km, a son propre Institut, et treize dates ouvertes. Le centre, ses contacts, le relevé, et
l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> à Rabat : Institut français, 15 rue Al Madina, Hassan ; Kénitra à 40 km.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; IRN et tout public 1 900 Dhs.",
              "<strong>8 sessions ouvertes</strong> le 17 octobre 2026 : 22, 29 et 30 octobre, 13, 19 et 24 novembre, 4 et 10 décembre ; 23 octobre complet.",
              "<a href=\"/centres/tcf-kenitra/\">Kénitra</a> : 21 et 27 octobre, puis onze dates du 10 novembre au 18 décembre (24 et 30 octobre complets).",
              "Moins de 20 jours entre deux TCF : inscription annulée sans remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français de Rabat", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong> · IRN et TP 1 900 Dhs", "22, 29, 30 oct., 13, 19, 24 nov., 4, 10 déc. 2026 ; 23 oct. complet ; panier en ligne."),
               ("Institut français de Kénitra", "Canada, Québec, IRN, tout public", "2 900 Dhs", "21, 27 oct. ; 10, 13, 17, 20, 25 nov. ; 1<sup>er</sup>, 3, 8, 11, 15, 18 déc. ; 24 et 30 oct. complets.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       stat3=("22 oct.", "prochaine session", "8 dates ouvertes au 17 oct."),
       faq=[("Où passer le TCF Canada à Rabat ?", "À l'Institut français de Rabat, 15 rue Al Madina, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams ; l'Institut de Kénitra est à 40 km."),
            ("Quelles dates pour le TCF Canada à Rabat ?", "Le 17 octobre 2026, huit sessions étaient ouvertes : 22, 29 et 30 octobre, 13, 19 et 24 novembre, 4 et 10 décembre (le 23 octobre complet). À Kénitra, treize dates ouvertes jusqu'au 18 décembre. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à Rabat ?", "En ligne, sur if-maroc.org/rabat, page TCF Canada : choix de la session, panier, paiement ; le TCF IRN s'inscrit à l'accueil.")]),
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
       desc="TCF Canada à Tanger : 2 900 Dhs à l'Institut français, sessions des 12, 19 et 26 novembre 2026, inscription en ligne ; Tétouan : 22 oct., 12 nov., 17 déc.",
       h1="Passer le TCF Canada à Tanger : l'Institut français, le prix et les dates",
       intro="""À Tanger, le TCF se passe à l'<strong>Institut français</strong>, 41 rue Hassan-Ibn-Ouazzane — seul centre
agréé de la ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada ; le 17 octobre 2026, son
site proposait les sessions des <strong>12, 19 et 26 novembre</strong> (9 h-12 h 30), lieu indiqué « Beckett ».
Tétouan, à 60 km, a son propre Institut (22 octobre, 12 novembre, 17 décembre). Le centre, ses contacts, le
relevé, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> à Tanger : Institut français, 41 rue Hassan-Ibn-Ouazzane ; Tétouan à 60 km.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; sessions des <strong>12, 19 et 26 novembre 2026</strong>.",
              "<a href=\"/centres/tcf-tetouan/\">Tétouan</a> : 22 octobre, 12 novembre et 17 décembre 2026.",
              "Inscription en ligne (panier) ; convocation dès l'inscription ; moins de 20 jours entre deux TCF : inscription annulée.",
              "Aucun remboursement ; report sur justificatif facturé 500 Dhs ; attestation à retirer à l'accueil du centre."],
       releve=[("Institut français de Tanger", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong>", "12, 19 et 26 novembre 2026, 9 h-12 h 30, lieu « Beckett » ; panier en ligne."),
               ("Institut français de Tétouan", "Canada, Québec, IRN, tout public", "2 900 Dhs", "22 octobre, 12 novembre, 17 décembre 2026.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       stat3=("12 nov.", "prochaine session", "relevé du 17 oct. 2026"),
       faq=[("Où passer le TCF Canada à Tanger ?", "À l'Institut français de Tanger, 41 rue Hassan-Ibn-Ouazzane, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams — sessions des 12, 19 et 26 novembre 2026 relevées le 17 octobre ; l'Institut de Tétouan est à 60 km."),
            ("Comment s'inscrire au TCF à Tanger ?", "En ligne, sur if-maroc.org/tanger, page TCF Canada : choix de la session, panier, paiement."),
            ("Combien coûte le TCF à Tanger ?", "2 900 dirhams pour le TCF Canada, tarif national de l'Institut français du Maroc (17 octobre 2026).")]),
    mk("tcf-fes", "Fès", "ma", ["Fès"], nearby=["Meknès"],
       title="TCF Fès 2026 : 2 900 Dhs, dates oct.-déc., inscription",
       desc="TCF Canada à Fès : 2 900 Dhs à l'Institut français, sessions des 29 oct., 12 et 26 nov., 17 déc. 2026, inscription en ligne ; Meknès à 60 km.",
       h1="Passer le TCF Canada à Fès : l'Institut français, le prix et l'inscription",
       intro="""À Fès, le TCF se passe à l'<strong>Institut français</strong>, 12 rue Serghini (ville nouvelle) — seul centre
agréé de la ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada, tarif national de
l'Institut français du Maroc. Le 17 octobre 2026, son site listait quatre sessions : <strong>29 octobre, 12 et
26 novembre, 17 décembre</strong> (8 h 45-12 h 15), à l'Espace Langues. Meknès, à 60 km, a son propre Institut
(29 octobre, 19 novembre, 17 décembre). Le centre, ses contacts, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> à Fès : Institut français, 12 rue Serghini ; Meknès à 60 km.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; IRN et tout public 1 900 Dhs.",
              "Sessions du <strong>29 octobre, 12 et 26 novembre, 17 décembre 2026</strong>, à l'Espace Langues (relevé du 17 octobre).",
              "<a href=\"/centres/tcf-meknes/\">Meknès</a> : 29 octobre, 19 novembre et 17 décembre 2026.",
              "Moins de 20 jours entre deux TCF : inscription annulée ; aucun remboursement ; report facturé 500 Dhs."],
       releve=[("Institut français de Fès", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong>", "29 oct., 12 et 26 nov., 17 déc. 2026, 8 h 45-12 h 15, Espace Langues ; panier en ligne."),
               ("Institut français de Meknès", "Canada, Québec, IRN, tout public", "2 900 Dhs", "29 oct., 19 nov., 17 déc. 2026.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       stat3=("29 oct.", "prochaine session", "4 dates au 17 oct. 2026"),
       faq=[("Où passer le TCF Canada à Fès ?", "À l'Institut français de Fès, 12 rue Serghini, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams ; l'Institut de Meknès est à 60 km."),
            ("Quelles dates pour le TCF Canada à Fès ?", "Le 17 octobre 2026 : 29 octobre, 12 et 26 novembre, 17 décembre, de 8 h 45 à 12 h 15. À Meknès : 29 octobre, 19 novembre, 17 décembre. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à Fès ?", "En ligne, sur if-maroc.org/fes, page TCF Canada : choix de la session, panier, paiement."),
            ("Combien coûte le TCF à Fès ?", "2 900 dirhams pour le TCF Canada, 1 900 pour le TCF IRN et le tout public — tarif national de l'Institut français du Maroc.")]),
    mk("tcf-agadir", "Agadir", "ma", ["Agadir"],
       title="TCF Agadir 2026 : 2 900 Dhs, dates nov.-déc., inscription",
       desc="TCF Canada à Agadir : 2 900 Dhs à l'Institut français, sessions des 27 novembre, 9 et 18 décembre 2026 (30 oct. et 13 nov. complets), inscription en ligne.",
       h1="Passer le TCF Canada à Agadir : l'Institut français, le prix et l'inscription",
       intro="""À Agadir, le TCF se passe à l'<strong>Institut français</strong>, rue de l'Entraide (Talborjt) — seul centre
agréé de la ville et du Sud marocain —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada,
tarif national de l'Institut français du Maroc. Le 17 octobre 2026, les sessions des 30 octobre et
13 novembre affichaient complet ; restaient les <strong>27 novembre, 9 et 18 décembre</strong> (9 h-12 h). Le
centre, ses contacts, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> à Agadir : Institut français, rue de l'Entraide, Talborjt ; lieu indiqué pour les sessions : rue Chenguit, Nouveau Talborjt.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; IRN et tout public 1 900 Dhs.",
              "Places libres le 17 octobre 2026 : <strong>27 novembre, 9 et 18 décembre</strong> ; 30 octobre et 13 novembre complets.",
              "Moins de 20 jours entre deux TCF : inscription annulée ; aucun remboursement ; report facturé 500 Dhs.",
              "Attestation à retirer à l'accueil du centre."],
       releve=[("Institut français d'Agadir", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong>", "27 nov., 9 et 18 déc. 2026, 9 h-12 h ; 30 oct. et 13 nov. complets ; panier en ligne.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       stat3=("27 nov.", "prochaine place libre", "relevé du 17 oct. 2026"),
       faq=[("Où passer le TCF Canada à Agadir ?", "À l'Institut français d'Agadir (Talborjt), seul centre agréé de la ville, sur ordinateur à 2 900 dirhams."),
            ("Quelles dates pour le TCF Canada à Agadir ?", "Le 17 octobre 2026, les 30 octobre et 13 novembre étaient complets ; il restait des places les 27 novembre, 9 et 18 décembre, de 9 h à 12 h. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à Agadir ?", "En ligne, sur if-maroc.org/agadir, page TCF Canada : choix de la session, panier, paiement."),
            ("Combien coûte le TCF à Agadir ?", "2 900 dirhams pour le TCF Canada, 1 900 pour le TCF IRN et le tout public — tarif national de l'Institut français du Maroc.")]),
    mk("tcf-kenitra", "Kénitra", "ma", ["Kenitra"],
       title="TCF Kénitra 2026 : 2 900 Dhs, 13 dates jusqu'au 18 décembre",
       desc="TCF Canada à Kénitra : 2 900 Dhs à l'Institut français (rue Khalid-Ibn-Walid), 13 sessions ouvertes du 21 octobre au 18 décembre 2026, inscription.",
       h1="Passer le TCF Canada à Kénitra : l'Institut français, le prix et les dates",
       intro="""À Kénitra, le TCF se passe à l'<strong>Institut français</strong>, rue Khalid-Ibn-Walid — seul centre agréé de la
ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada, tarif national de l'Institut français du Maroc.
Le 17 octobre 2026, son site affichait <strong>treize sessions ouvertes</strong>, du 21 octobre au 18 décembre — plus
que Rabat, à 40 km. Le centre, ses contacts, le relevé, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> : Institut français de Kénitra, rue Khalid-Ibn-Walid ; <a href=\"/centres/tcf-rabat/\">Rabat</a> à 40 km.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; TCF IRN et tout public 1 900 Dhs.",
              "Sessions ouvertes le 17 octobre 2026 : <strong>21 et 27 octobre</strong>, puis <strong>10, 13, 17, 20 et 25 novembre, 1<sup>er</sup>, 3, 8, 11, 15 et 18 décembre</strong> (9 h-14 h) ; 24 et 30 octobre complets.",
              "Inscription en ligne sur le site de l'Institut de Kénitra (if-maroc.org/kenitra), session par session, avec un panier ; le TCF IRN s'inscrit à l'accueil.",
              "Moins de 20 jours entre deux TCF, toutes versions confondues : inscription annulée sans remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français de Kénitra", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong>", "21 oct. (9 h-13 h), 27 oct. ; 10, 13, 17, 20, 25 nov. ; 1<sup>er</sup>, 3, 8, 11, 15, 18 déc. 2026 (9 h-14 h) ; 24 et 30 oct. complets ; panier en ligne.")],
       releve_date="17 octobre 2026", published="2026-10-18", modified=("2026-10-18", "18 octobre 2026"),
       stat3=("21 oct.", "prochaine session", "13 dates ouvertes au 17 oct."),
       faq=[("Où passer le TCF Canada à Kénitra ?", "À l'Institut français de Kénitra, rue Khalid-Ibn-Walid, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams. Rabat, à 40 km, a son propre Institut."),
            ("Quelles dates pour le TCF Canada à Kénitra ?", "Le 17 octobre 2026, treize sessions étaient ouvertes : 21 et 27 octobre, 10, 13, 17, 20 et 25 novembre, 1er, 3, 8, 11, 15 et 18 décembre ; les 24 et 30 octobre étaient complets. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à Kénitra ?", "En ligne, sur if-maroc.org/kenitra, page TCF Canada : choix de la session, panier, paiement. Le TCF IRN s'inscrit à l'accueil."),
            ('Combien de jours entre deux TCF ?', "Vingt au minimum : « Le candidat ne peut se présenter deux fois à un test du TCF toute version confondue dans un délai inférieur à 20 jours », sinon l'inscription est annulée sans remboursement.")]),
    mk("tcf-meknes", "Meknès", "ma", ["Meknès"],
       title="TCF Meknès 2026 : 2 900 Dhs, sessions oct.-déc., inscription",
       desc="TCF Canada à Meknès : 2 900 Dhs à l'Institut français (rue Ferhat-Hachad), sessions des 29 octobre, 19 novembre et 17 décembre 2026, inscription en ligne.",
       h1="Passer le TCF Canada à Meknès : l'Institut français, le prix et les dates",
       intro="""À Meknès, le TCF se passe à l'<strong>Institut français</strong>, rue Ferhat-Hachad — seul centre agréé de la
ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada, tarif national de l'Institut français du Maroc.
Le 17 octobre 2026, son site listait trois sessions : <strong>29 octobre, 19 novembre et 17 décembre</strong>
(9 h-14 h). Fès, à 60 km, en proposait quatre. Le centre, ses contacts, le relevé, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> : Institut français de Meknès, rue Ferhat-Hachad ; <a href=\"/centres/tcf-fes/\">Fès</a> à 60 km.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; TCF IRN et tout public 1 900 Dhs.",
              "Sessions du <strong>29 octobre, 19 novembre et 17 décembre 2026</strong>, de 9 h à 14 h (relevé du 17 octobre).",
              "Fès : 29 octobre, 12 et 26 novembre, 17 décembre 2026.",
              "Moins de 20 jours entre deux TCF, toutes versions confondues : inscription annulée sans remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français de Meknès", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong>", "29 oct., 19 nov., 17 déc. 2026, 9 h-14 h ; panier en ligne.")],
       releve_date="17 octobre 2026", published="2026-10-18", modified=("2026-10-18", "18 octobre 2026"),
       stat3=("29 oct.", "prochaine session", "3 dates au 17 oct. 2026"),
       faq=[("Où passer le TCF Canada à Meknès ?", "À l'Institut français de Meknès, rue Ferhat-Hachad, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams ; l'Institut de Fès est à 60 km."),
            ("Quelles dates pour le TCF Canada à Meknès ?", "Le 17 octobre 2026 : 29 octobre, 19 novembre et 17 décembre, de 9 h à 14 h. À Fès : 29 octobre, 12 et 26 novembre, 17 décembre. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à Meknès ?", "En ligne, sur if-maroc.org/meknes, page TCF Canada : choix de la session, panier, paiement. Le TCF IRN s'inscrit à l'accueil."),
            ('Combien de jours entre deux TCF ?', "Vingt au minimum : « Le candidat ne peut se présenter deux fois à un test du TCF toute version confondue dans un délai inférieur à 20 jours », sinon l'inscription est annulée sans remboursement.")]),
    mk("tcf-el-jadida", "El Jadida", "ma", ["El Jadida"],
       title="TCF El Jadida 2026 : 2 900 Dhs, 8 dates d'ici fin novembre",
       desc="TCF Canada à El Jadida : 2 900 Dhs à l'Institut français (3 rue du Caire), 8 sessions ouvertes du 23 octobre au 28 novembre 2026, inscription en ligne.",
       h1="Passer le TCF Canada à El Jadida : l'Institut français, le prix et les dates",
       intro="""À El Jadida, le TCF se passe à l'<strong>Institut français</strong>, 3, rue du Caire — seul centre agréé de la
ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada, tarif national de l'Institut français du Maroc.
Le 17 octobre 2026, son site affichait <strong>huit sessions ouvertes</strong> : 23, 27 et 30 octobre, puis 7, 14, 19,
26 et 28 novembre — aucune encore en décembre. Le centre, ses contacts, le relevé, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> : Institut français d'El Jadida, 3 rue du Caire.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; TCF IRN et tout public 1 900 Dhs.",
              "Sessions ouvertes le 17 octobre 2026 : <strong>23, 27 et 30 octobre</strong> (8 h 45-17 h 30 ; un des deux créneaux du 30 complet), <strong>7, 14, 19, 26 et 28 novembre</strong> (8 h 30-12 h).",
              "Inscription en ligne sur le site de l'Institut d'El Jadida (if-maroc.org/eljadida), avec un panier ; le TCF IRN s'inscrit à l'accueil.",
              "Moins de 20 jours entre deux TCF, toutes versions confondues : inscription annulée sans remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français d'El Jadida", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong>", "23, 27, 30 oct. (8 h 45-17 h 30 ; un créneau du 30 complet) ; 7, 14, 19, 26, 28 nov. (8 h 30-12 h) ; aucune date de décembre affichée ; panier en ligne.")],
       releve_date="17 octobre 2026", published="2026-10-18", modified=("2026-10-18", "18 octobre 2026"),
       stat3=("23 oct.", "prochaine session", "8 dates ouvertes au 17 oct."),
       faq=[("Où passer le TCF Canada à El Jadida ?", "À l'Institut français d'El Jadida, 3 rue du Caire, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams."),
            ("Quelles dates pour le TCF Canada à El Jadida ?", "Le 17 octobre 2026, huit sessions étaient ouvertes : 23, 27 et 30 octobre, de 8 h 45 à 17 h 30, puis 7, 14, 19, 26 et 28 novembre, de 8 h 30 à 12 h ; aucune date de décembre n'était encore affichée. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à El Jadida ?", "En ligne, sur if-maroc.org/eljadida, page TCF Canada : choix de la session, panier, paiement. Le TCF IRN s'inscrit à l'accueil."),
            ('Combien de jours entre deux TCF ?', "Vingt au minimum : « Le candidat ne peut se présenter deux fois à un test du TCF toute version confondue dans un délai inférieur à 20 jours », sinon l'inscription est annulée sans remboursement.")]),
    mk("tcf-tetouan", "Tétouan", "ma", ["Tétouan"],
       title="TCF Tétouan 2026 : 2 900 Dhs, dates oct.-déc., inscription",
       desc="TCF Canada à Tétouan : 2 900 Dhs à l'Institut français (13 rue Chakib-Arsalane), sessions des 22 octobre, 12 novembre et 17 décembre 2026 ; Tanger.",
       h1="Passer le TCF Canada à Tétouan : l'Institut français, le prix et les dates",
       intro="""À Tétouan, le TCF se passe à l'<strong>Institut français</strong>, 13, rue Chakib-Arsalane — seul centre agréé de
la ville —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF Canada, tarif national de l'Institut français du
Maroc. Le 17 octobre 2026, son site listait trois sessions : <strong>22 octobre, 12 novembre et 17 décembre</strong>
(8 h 30-12 h 30). Tanger, à 60 km, propose les 12, 19 et 26 novembre. Le centre, ses contacts, le relevé, et
l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> : Institut français de Tétouan, 13 rue Chakib-Arsalane ; <a href=\"/centres/tcf-tanger/\">Tanger</a> à 60 km.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; TCF IRN et tout public 1 900 Dhs.",
              "Sessions du <strong>22 octobre, 12 novembre et 17 décembre 2026</strong>, de 8 h 30 à 12 h 30 (relevé du 17 octobre).",
              "Tanger : 12, 19 et 26 novembre 2026.",
              "Moins de 20 jours entre deux TCF, toutes versions confondues : inscription annulée sans remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français de Tétouan", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong>", "22 oct., 12 nov., 17 déc. 2026, 8 h 30-12 h 30 ; panier en ligne.")],
       releve_date="17 octobre 2026", published="2026-10-18", modified=("2026-10-18", "18 octobre 2026"),
       stat3=("22 oct.", "prochaine session", "3 dates au 17 oct. 2026"),
       faq=[("Où passer le TCF Canada à Tétouan ?", "À l'Institut français de Tétouan, 13 rue Chakib-Arsalane, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams ; l'Institut de Tanger est à 60 km."),
            ("Quelles dates pour le TCF Canada à Tétouan ?", "Le 17 octobre 2026 : 22 octobre, 12 novembre et 17 décembre, de 8 h 30 à 12 h 30. À Tanger : 12, 19 et 26 novembre. La page TCF Canada du site fait foi."),
            ("Comment s'inscrire au TCF à Tétouan ?", "En ligne, sur if-maroc.org/tetouan, page TCF Canada : choix de la session, panier, paiement. Le TCF IRN s'inscrit à l'accueil."),
            ('Combien de jours entre deux TCF ?', "Vingt au minimum : « Le candidat ne peut se présenter deux fois à un test du TCF toute version confondue dans un délai inférieur à 20 jours », sinon l'inscription est annulée sans remboursement.")]),
    mk("tcf-oujda", "Oujda", "ma", ["Oujda"], nearby=["Nador"],
       title="TCF Oujda 2026 : 2 900 Dhs, session du 10 novembre, Nador",
       desc="TCF Canada à Oujda : 2 900 Dhs à l'Institut français, une seule session affichée, le 10 novembre 2026, inscription en ligne ; Nador, rattaché à Oujda.",
       h1="Passer le TCF Canada à Oujda : l'Institut français, le prix et les dates",
       intro="""À Oujda, le TCF se passe à l'<strong>Institut français</strong> — seul centre agréé de la ville, auquel est
rattaché le centre de Nador (école française Paul-Riquet) —, sur ordinateur, à <strong>2 900 Dhs</strong> pour le TCF
Canada. Le 17 octobre 2026, son site ne listait qu'une session, le <strong>mardi 10 novembre</strong>, de 8 h 30 à
18 h, au 9-11, lot Chabab (Hay Al Qods). Le centre, ses contacts, le relevé, et l'inscription en ligne.""",
       facts=["<strong>1 centre agréé</strong> à Oujda : Institut français, espace langue, 16 rue Imam-Echafii ; Nador : école française Paul-Riquet, rattachée à Oujda.",
              "<strong>TCF Canada 2 900 Dhs</strong>, sur ordinateur ; TCF IRN et tout public 1 900 Dhs.",
              "Une seule session affichée le 17 octobre 2026 : <strong>mardi 10 novembre</strong>, 8 h 30-18 h, lieu indiqué : 9-11 lot Chabab, Hay Al Qods.",
              "Inscription en ligne sur le site de l'Institut d'Oujda (if-maroc.org/oujda), avec un panier ; le TCF IRN s'inscrit à l'accueil.",
              "Moins de 20 jours entre deux TCF, toutes versions confondues : inscription annulée sans remboursement ; report sur justificatif facturé 500 Dhs."],
       releve=[("Institut français d'Oujda", "Canada, Québec, IRN (sur place), tout public", "Canada <strong>2 900 Dhs</strong>", "Mardi 10 novembre 2026, 8 h 30-18 h, seule session listée ; panier en ligne."),
               ("Nador (école Paul-Riquet, rattachée à Oujda)", "Canada", NR, "Sessions à vérifier auprès de l'Institut d'Oujda.")],
       releve_date="17 octobre 2026", published="2026-10-18", modified=("2026-10-18", "18 octobre 2026"),
       stat3=("10 nov.", "seule session affichée", "relevé du 17 oct. 2026"),
       faq=[("Où passer le TCF Canada à Oujda ?", "À l'Institut français d'Oujda, seul centre agréé de la ville, sur ordinateur à 2 900 dirhams ; le 17 octobre 2026, sa session du 10 novembre était annoncée au 9-11, lot Chabab (Hay Al Qods). Le centre de Nador, à l'école Paul-Riquet, lui est rattaché."),
            ("Quelles dates pour le TCF Canada à Oujda ?", "Le 17 octobre 2026, une seule session était listée : le mardi 10 novembre, de 8 h 30 à 18 h. La page TCF Canada du site fait foi ; Fès et Meknès en proposaient d'autres en novembre et en décembre."),
            ("Comment s'inscrire au TCF à Oujda ?", "En ligne, sur if-maroc.org/oujda, page TCF Canada : choix de la session, panier, paiement. Le TCF IRN s'inscrit à l'accueil."),
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
       desc="TCF Canada à Sfax : 880 DT à l'Institut français, tests des 27 novembre et 19 décembre 2026, rendez-vous en ligne du 2 au 8 nov., inscription sur place.",
       h1="Passer le TCF Canada à Sfax : l'Institut français et l'inscription",
       intro="""À Sfax, le TCF se passe au <strong>centre de langue de l'Institut français</strong>, 9 avenue Habib-Bourguiba —
seul centre agréé de la ville —, sur ordinateur, à <strong>880 DT</strong> pour le TCF Canada, avec un rendez-vous en
ligne puis l'inscription et le paiement sur place. Le 17 octobre 2026, le calendrier du pôle annonçait les
tests des 30 octobre (rendez-vous clos), <strong>27 novembre</strong> (rendez-vous en ligne du 2 au 8 novembre)
et <strong>19 décembre</strong> (du 1<sup>er</sup> au 6 décembre). Le centre, ses contacts, et la procédure.""",
       facts=["<strong>1 centre agréé</strong> à Sfax : Institut français, centre de langue, 9 avenue Habib-Bourguiba.",
              "<strong>TCF Canada 880 DT</strong> ; TCF Québec 880 DT ; TCF IRN 625 DT.",
              "Tests du <strong>27 novembre</strong> (rendez-vous en ligne 2-8 novembre, inscription le 12) et du <strong>19 décembre</strong> (rendez-vous 1<sup>er</sup>-6 décembre, inscription le 8).",
              "Paiement en espèces ; frais non remboursables.",
              "Résultats 5 semaines après ; 30 jours entre deux sessions."],
       releve=[("IFT — centre de langue de Sfax", "Canada, Québec, IRN, tout public", "Canada <strong>880 DT</strong>", "RDV 02-08/11 → inscription 12/11 → test 27/11 ; 01-06/12 → 08/12 → 19/12 ; test du 30/10 : rendez-vous clos.")],
       releve_date="17 octobre 2026", modified=("2026-10-17", "17 octobre 2026"),
       stat3=("27 nov.", "prochain test ouvert", "rendez-vous du 2 au 8 nov."),
       faq=[("Où passer le TCF Canada à Sfax ?", "Au centre de langue de l'Institut français de Sfax, 9 avenue Habib-Bourguiba, seul centre agréé de la ville."),
            ("Quelles dates pour le TCF Canada à Sfax ?", "Le 17 octobre 2026 : 27 novembre (rendez-vous en ligne du 2 au 8 novembre, inscription sur place le 12 novembre) et 19 décembre (rendez-vous du 1er au 6 décembre, inscription le 8 décembre). Le test du 30 octobre n'acceptait plus de rendez-vous."),
            ("Comment s'inscrire au TCF à Sfax ?", "Rendez-vous en ligne sur la page TCF Canada de l'Institut pendant la fenêtre de la session, puis inscription et paiement sur place, en espèces, le jour fixé."),
            ("Combien coûte le TCF à Sfax ?", "880 dinars pour le TCF Canada et le TCF Québec, 625 dinars pour le TCF IRN, à l'Institut français de Tunisie (17 octobre 2026).")]),
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
       title="DELF à Lille : Alliance française, prix (B2 180 €), session",
       desc="Où passer le DELF à Lille : l'Alliance française de Lille Métropole, seul centre agréé, ses tarifs (A1 120 € à C2 210 €), la session de novembre 2026.",

       h1="Passer le DELF à Lille : l'Alliance française, ses prix et sa session de novembre",
       intro="""À Lille, le DELF et le DALF se passent à l'<strong>Alliance française de Lille Métropole</strong> — seul
centre agréé de la ville — pour <strong>180 €</strong> le DELF B2 (120 € le A1, 210 € le C2). Sa session de
novembre 2026 s'inscrit <strong>du 30 septembre au 7 octobre</strong> : une semaine, pas plus. Le centre, ses
contacts, le relevé, et l'inscription.""",
       facts=["<strong>1 centre agréé</strong> : Alliance française de Lille Métropole.",
              "<strong>A1 120 € · A2 130 € · B1 160 € · B2 180 € · C1 200 € · C2 210 €.</strong>",
              "Session de novembre 2026 : écrits du 3 au 5 novembre, oraux jusqu'au 18 ; <strong>inscriptions du 30 septembre (10 h) au 7 octobre (23 h 59)</strong>.",
              "Deux sessions relevées en 2026 : juin et novembre.",
              "Maubeuge et Valenciennes n'ont pas de centre DELF : Lille est le centre du Nord."],
       releve=[("Alliance française de Lille Métropole", "DELF A1-B2, DALF C1-C2", "A1 120 · A2 130 · B1 160 · <strong>B2 180</strong> · C1 200 · C2 210 €", "Nov. 2026 : inscriptions 30 sept.-7 oct., écrits 3-5 nov., oraux jusqu'au 18 nov. ; juin 2026 : inscriptions 29 avril-6 mai.")],
       faq=[("Où passer le DELF B2 à Lille ?", "À l'Alliance française de Lille Métropole, seul centre agréé de Lille : 180 €, session de novembre 2026 avec inscriptions du 30 septembre au 7 octobre."),
            ("Combien coûte le DELF à Lille ?", "120 € le A1, 130 € le A2, 160 € le B1, 180 € le B2, 200 € le C1, 210 € le C2 à l'Alliance française de Lille Métropole (17 septembre 2026)."),
            ("Quand s'inscrire au DELF à Lille ?", "Pendant la fenêtre d'une semaine ouverte par l'Alliance : du 30 septembre à 10 h au 7 octobre à 23 h 59 pour la session de novembre 2026.")]),
    mk("delf-nantes", "Nantes", "fr", ["Nantes"], exam="delf",
       title="DELF à Nantes : Nantes Université, 125 €, sessions 2026-27",

       desc="Où passer le DELF à Nantes : l'i-FLE de Nantes Université, seul centre agréé, le DELF B1-B2 à 125 € — le moins cher relevé —, les sessions 2026-2027.",

       h1="Passer le DELF à Nantes : Nantes Université, 125 € et des inscriptions en deux jours",
       intro="""À Nantes, le DELF et le DALF se passent à l'<strong>Institut de français langue étrangère de Nantes
Université</strong> (i-FLE) — seul centre agréé de la ville — pour <strong>125 €</strong> le DELF B1 ou B2 et
145 € le DALF, le tarif le plus bas relevé en France. Contrepartie : les inscriptions n'ouvrent que
<strong>deux jours, à partir de 7 h</strong>, « dans la limite des places disponibles ». Le centre, ses
contacts, le calendrier, et l'inscription.""",
       facts=["<strong>1 centre agréé</strong> : Nantes Université, i-FLE (Service universitaire des langues).",
              "<strong>DELF B1 et B2 : 125 € · DALF C1 et C2 : 145 €.</strong>",
              "Sessions : 2-4 décembre 2026 (inscriptions 22-23 septembre), 17-19 mars 2027 (9-10 février), 26-28 mai 2027 (20-21 avril), 16-18 juin 2027 (11-12 mai).",
              "Inscriptions <strong>sur deux jours à partir de 7 h</strong>, en ligne, paiement par carte ; droits non remboursables.",
              "Ouvert « à toute personne de nationalité étrangère » ; aménagements à déclarer deux mois avant."],
       releve=[("Nantes Université — i-FLE", "DELF B1, B2, DALF C1, C2", "<strong>B1-B2 125 €</strong> · C1-C2 145 €", "2-4 déc. 2026 (inscr. 22-23 sept.) ; 17-19 mars 2027 (9-10 févr.) ; 26-28 mai 2027 (20-21 avril) ; 16-18 juin 2027 (11-12 mai) — dès 7 h, places limitées.")],
       faq=[("Où passer le DELF B2 à Nantes ?", "À Nantes Université (i-FLE), seul centre agréé de la ville : 125 €, sessions des 2-4 décembre 2026, 17-19 mars, 26-28 mai et 16-18 juin 2027."),
            ("Combien coûte le DELF à Nantes ?", "125 € pour le DELF B1 ou B2, 145 € pour le DALF C1 ou C2 — le tarif le plus bas relevé en France (page mise à jour le 14 septembre 2026)."),
            ("Comment s'inscrire au DELF à Nantes ?", "En ligne, pendant les deux jours d'ouverture, à partir de 7 h — les 22 et 23 septembre 2026 pour la session de décembre —, avec une pièce d'identité et un paiement par carte ; les places partent vite et les droits ne sont pas remboursables.")]),
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
       title="DELF à Marseille et Aix : 5 centres agréés, inscription",
       desc="Où passer le DELF à Marseille et Aix : 5 centres agréés avec contacts — Alliance française, Aix-Marseille Université, IS Aix, EPFF, E2C —, les délais.",

       h1="Passer le DELF à Marseille et Aix-en-Provence : les 5 centres agréés",
       intro="""À Marseille et Aix-en-Provence, le DELF et le DALF se passent dans <strong>%(n)d centres agréés</strong> par
France Éducation international : l'Alliance française Aix-Marseille Provence, le Service universitaire des
langues d'Aix-Marseille Université, IS Aix-en-Provence, l'EPFF et l'École de la deuxième chance. L'Alliance
rend ses résultats sous quatre à six semaines, à retirer sur place, et propose des épreuves d'entraînement
officielles à Aix. Les centres, leurs contacts, et l'inscription.""",
       facts=["<strong>5 centres agréés</strong> à Marseille et Aix.",
              "<strong>Alliance française Aix-Marseille</strong> : tarif non affiché en ligne ; résultats en 4 à 6 semaines, à retirer sur place.",
              "« Il n'est pas possible de se réinscrire au DELF/DALF du même niveau tant que les résultats de la session précédente n'ont pas été annoncés. »",
              "Épreuves d'entraînement officielles A2-B2 (sujets réels) à Aix, résultats sous 10 jours ouvrés.",
              "Aménagements : à signaler à l'inscription avec un certificat médical."],
       releve=[("Alliance française Aix-Marseille Provence", "DELF A1-B2, DALF, épreuves d'entraînement", "non affiché en ligne", "Inscription en ligne ; résultats 4-6 semaines sur place."),
               ("Aix-Marseille Université (SUL) · IS Aix · EPFF · E2C", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le DELF B2 à Marseille ?", "À l'Alliance française Aix-Marseille Provence (Marseille ou Aix), au Service universitaire des langues d'Aix-Marseille Université, chez IS Aix-en-Provence, à l'EPFF ou à l'École de la deuxième chance — cinq centres agréés."),
            ("Combien coûte le DELF à Marseille ?", "L'Alliance française n'affiche pas ses tarifs DELF en ligne ; ailleurs en France, un DELF B2 va de 125 à 280 € selon le centre."),
            ("Peut-on s'entraîner au DELF à Marseille ?", "Oui : l'Alliance française propose à Aix-en-Provence les épreuves d'entraînement officielles de FEI (compréhensions A2, B1, B2, sujets réels), avec des résultats sous dix jours ouvrés, sans obligation de s'inscrire à l'examen.")]),
    mk("delf-toulouse", "Toulouse", "fr", ["Toulouse"], exam="delf",
       title="DELF à Toulouse : 5 centres agréés, contacts, inscription",
       desc="Où passer le DELF à Toulouse : 5 centres agréés avec contacts — Université Toulouse Jean Jaurès, Alliance française, CREPT, Langue Onze, SPLE —, les sessions.",

       h1="Passer le DELF à Toulouse : les 5 centres agréés et l'inscription",
       intro="""À Toulouse, le DELF et le DALF se passent dans <strong>%(n)d centres agréés</strong> par France Éducation
international : le DEFLE de l'université Toulouse Jean Jaurès, l'Alliance française de Toulouse, CREPT
Formation, Langue Onze et le SPLE Vidal. Chacun choisit ses sessions parmi les dix du calendrier national et
fixe son tarif. Les centres, leurs contacts, et l'inscription.""",
       facts=["<strong>5 centres agréés</strong> à Toulouse.",
              "L'université Toulouse Jean Jaurès est le centre universitaire, souvent le moins cher.",
              "Prochaines sessions nationales : 6-8 octobre, 3-5 novembre, 1-3 décembre 2026 ; chaque centre n'en ouvre qu'une partie.",
              "Inscriptions closes quatre à dix semaines avant l'écrit.",
              "Diplôme valable à vie ; résultats en 4 à 6 semaines."],
       releve=[("Université Toulouse Jean Jaurès (DEFLE) · Alliance française de Toulouse · CREPT · Langue Onze · SPLE Vidal", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le DELF B2 à Toulouse ?", "Au DEFLE de l'université Toulouse Jean Jaurès, à l'Alliance française de Toulouse, chez CREPT Formation, Langue Onze ou SPLE Vidal — cinq centres agréés par France Éducation international."),
            ("Combien coûte le DELF à Toulouse ?", "Nous n'avons pas relevé les tarifs des centres toulousains ; ailleurs en France, un DELF B2 va de 125 € (Nantes Université) à 280 € (Alliance française de Paris), les universités étant presque toujours les moins chères."),
            ("Quand s'inscrire au DELF à Toulouse ?", "Quatre à dix semaines avant l'écrit de la session choisie — les prochaines sont les 6-8 octobre, 3-5 novembre et 1-3 décembre 2026 —, sur le site ou à l'accueil du centre.")]),
    mk("delf-montpellier", "Montpellier", "fr", ["Montpellier"], exam="delf",
       title="DELF à Montpellier : Paul-Valéry et GRETA, inscription",

       desc="Où passer le DELF à Montpellier : le centre DELF-DALF de l'Université Paul-Valéry (IEFE) et le GRETA CFA Montpellier Littoral, avec contacts, les sessions.",

       h1="Passer le DELF à Montpellier : les centres agréés et l'inscription",
       intro="""À Montpellier, le DELF et le DALF se passent dans <strong>%(n)d centres agréés</strong> par France Éducation
international : le <strong>centre DELF-DALF de l'université Paul-Valéry</strong> (IEFE, route de Mende) et
le GRETA CFA Montpellier Littoral. L'Alliance française de Montpellier n'est pas centre DELF : c'est le
centre TCF le plus documenté de la ville. Les centres, leurs contacts, et l'inscription.""",
       facts=["<strong>2 centres agréés</strong> DELF-DALF à Montpellier : Université Paul-Valéry (IEFE) et GRETA CFA Montpellier Littoral.",
              "Prochaines sessions nationales : 6-8 octobre, 3-5 novembre, 1-3 décembre 2026.",
              "Inscriptions closes quatre à dix semaines avant l'écrit.",
              "Pour le TCF, l'Alliance française de Montpellier publie une grille complète (IRN 185 €, Canada 200 €).",
              "Diplôme valable à vie ; résultats en 4 à 6 semaines."],
       releve=[("Université Paul-Valéry Montpellier 3 — IEFE", "DELF A1-B2, DALF", NR, "Sur le site de l'IEFE."),
               ("GRETA CFA Montpellier Littoral", "DELF-DALF", NR, "Sur le site du GRETA.")],
       faq=[("Où passer le DELF B2 à Montpellier ?", "Au centre DELF-DALF de l'université Paul-Valéry (IEFE, route de Mende) ou au GRETA CFA Montpellier Littoral, les deux centres agréés par France Éducation international ; l'Alliance française de Montpellier, elle, n'organise que le TCF et l'examen civique."),
            ("Combien coûte le DELF à Montpellier ?", "Nous n'avons pas relevé les tarifs DELF montpelliérains ; ailleurs en France, un DELF B2 va de 125 à 280 € selon le centre."),
            ("Quand s'inscrire au DELF à Montpellier ?", "Quatre à dix semaines avant l'écrit de la session choisie — 6-8 octobre, 3-5 novembre ou 1-3 décembre 2026 —, sur le site ou à l'accueil du centre.")]),
    mk("delf-strasbourg", "Strasbourg", "fr", ["Strasbourg"], exam="delf",
       title="DELF à Strasbourg : 3 centres agréés, contacts, inscription",
       desc="Où passer le DELF à Strasbourg : 3 centres agréés avec contacts — Alliance française Strasbourg Europe, École européenne, Pôle FLE Unistra —, les sessions.",

       h1="Passer le DELF à Strasbourg : les 3 centres agréés et l'inscription",
       intro="""À Strasbourg, le DELF et le DALF se passent dans <strong>%(n)d centres agréés</strong> par France Éducation
international : l'Alliance française Strasbourg Europe, l'École européenne de Strasbourg et le Pôle FLE de
l'Université de Strasbourg. Chacun choisit ses sessions parmi les dix du calendrier national et fixe son
tarif. Les centres, leurs contacts, et l'inscription.""",
       facts=["<strong>3 centres agréés</strong> à Strasbourg.",
              "Prochaines sessions nationales : 6-8 octobre, 3-5 novembre, 1-3 décembre 2026.",
              "Inscriptions closes quatre à dix semaines avant l'écrit.",
              "Pour un TCF IRN, l'Alliance française Strasbourg Europe est aussi agréée (pas de TCF Canada).",
              "Diplôme valable à vie ; résultats en 4 à 6 semaines."],
       releve=[("Alliance française Strasbourg Europe · École européenne · Pôle FLE Unistra", NR, NR, "Sur le site du centre.")],
       faq=[("Où passer le DELF B2 à Strasbourg ?", "À l'Alliance française Strasbourg Europe, à l'École européenne de Strasbourg ou au Pôle FLE de l'Université de Strasbourg — trois centres agréés par France Éducation international."),
            ("Combien coûte le DELF à Strasbourg ?", "Nous n'avons pas relevé les tarifs strasbourgeois ; ailleurs en France, un DELF B2 va de 125 à 280 € selon le centre."),
            ("Quand s'inscrire au DELF à Strasbourg ?", "Quatre à dix semaines avant l'écrit de la session choisie — 6-8 octobre, 3-5 novembre ou 1-3 décembre 2026 —, sur le site ou à l'accueil du centre.")]),
]
