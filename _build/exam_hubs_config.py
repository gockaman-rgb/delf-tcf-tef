# -*- coding: utf-8 -*-
"""Contenu des pages d'accueil d'examen et découpage des piliers en modules (19/09/2026).

Pour chaque examen : le texte explicatif de la page d'accueil (« Qu'est-ce que … »), sa FAQ
courte, la grille des modules, puis les modules eux-mêmes — chacun reprend des sections du
pilier source (ids d'origine), avec un titre, une description, un chapô et des faits propres.
Les indices `faq` renvoient à la FAQ du pilier source (ordre d'origine) ; une question ne
figure que sur une page.
"""

EXAMS = {}

# ---------------------------------------------------------------------------
EXAMS["tcf-canada"] = dict(
    name="TCF Canada",
    landing_short="Ce qu'est le test, pour qui, et les modules du dossier.",
    what_h2="Qu'est-ce que le TCF Canada ?",
    what="""<p>Le <strong>TCF Canada</strong> est un test de français conçu par France Éducation international
et reconnu par Immigration, Réfugiés et Citoyenneté Canada (IRCC) pour prouver son niveau de français
dans une démarche d'<strong>immigration économique</strong> — Entrée express, programmes des travailleurs
qualifiés — ou de <strong>citoyenneté</strong>. Il se passe en une session, dans un centre agréé, et
comporte <strong>quatre épreuves obligatoires</strong> : compréhension orale, compréhension écrite,
expression écrite, expression orale. Les deux compréhensions sont notées sur 699, les deux expressions
sur 20, puis chaque note est <strong>convertie en niveau NCLC</strong>, l'échelle qu'IRCC utilise pour
attribuer les points.</p>

<p>Ce n'est ni un diplôme ni un examen que l'on « réussit » : chacun repart avec un niveau, de A1 à C2,
et une attestation valable <strong>deux ans</strong>. C'est l'un des deux seuls tests acceptés par IRCC
avec le TEF Canada ; le TCF tout public et le TCF Québec, qui lui ressemblent, ne sont pas acceptés
pour Entrée express.</p>

<h3>Pour qui</h3>
<ul>
<li>Les candidats à <strong>Entrée express</strong> et aux programmes fédéraux, qui doivent atteindre un
NCLC donné — le NCLC 7 est le seuil le plus courant.</li>
<li>Les candidats à la <strong>citoyenneté</strong>, pour qui seules les deux épreuves orales comptent.</li>
<li>Les candidats aux programmes du <strong>Québec</strong>, qui l'acceptent aussi depuis 2022 — mais le
<a href="/tcf-quebec/">TCF Québec</a>, modulaire, y est souvent moins cher.</li>
</ul>""",
    faq=[
        ("Qu'est-ce que le TCF Canada ?",
         "Un test de français de France Éducation international, reconnu par Immigration, Réfugiés et Citoyenneté Canada pour l'immigration économique et la citoyenneté. Quatre épreuves obligatoires en une session — compréhension orale, compréhension écrite, expression écrite, expression orale —, un niveau de A1 à C2 par épreuve, converti en NCLC, et une attestation valable deux ans."),
        ("Quelle différence avec le TCF tout public et le TCF Québec ?",
         "Le TCF tout public sert aux études et aux démarches personnelles, le TCF Québec aux programmes du ministère de l'Immigration du Québec ; ni l'un ni l'autre n'est accepté par IRCC pour Entrée express. Seuls le TCF Canada et le TEF Canada le sont. Le TCF Canada est en revanche aussi reconnu par le Québec depuis 2022."),
        ("Le TCF Canada se réussit-il ou se rate-t-il ?",
         "Ni l'un ni l'autre : il n'y a pas de seuil de réussite. Chaque épreuve donne un niveau, de A1 à C2, converti en NCLC ; c'est votre programme d'immigration qui fixe le niveau à atteindre — NCLC 7 le plus souvent. Un score insuffisant se corrige en repassant les quatre épreuves après 20 à 30 jours."),
    ],
    modules=[
        ("Les épreuves", "Le format, épreuve par épreuve", "/tcf-canada/format/", "39 + 39 questions, 3 tâches d'écrit, 3 tâches d'oral, et les pièges de format qui coûtent des points."),
        ("La notation", "Du score sur 699 au NCLC", "/tcf-canada/score-nclc/", "Les bandes de scores, la table de conversion IRCC, et le B2 qui ne vaut pas toujours NCLC 7."),
        ("Se préparer", "Méthode et ressources", "/tcf-canada/preparation/", "Pourquoi le français vaut si cher en 2026, et comment travailler chaque épreuve."),
        ("Prix et inscription", "Prix, centres, validité, reprise", "/tcf-canada/prix-inscription/", "195 à 285 € en France, 390 à 440 $ au Canada, six centres avec contacts, la double règle des deux ans."),
        ("S'entraîner", "Exercices corrigés, épreuve par épreuve", "/blog/exercices-comprehension-orale-tcf-canada/", "Compréhension orale, compréhension écrite, expression écrite, expression orale : des items réels expliqués."),
        ("Examen blanc", "Le test complet, chronométré, noté", "/examens-blancs/", "Dans l'app : les quatre épreuves au format officiel, notées sur 699 et converties en NCLC."),
    ],
    spokes=[
        dict(slug="format", crumb="Format et épreuves", sections=["format", "erreurs"],
             title="Format du TCF Canada : les 4 épreuves et leurs pièges",
             desc="Les quatre épreuves du TCF Canada, leur durée exacte — 2 h 47 au total —, le nombre de questions et de tâches, et les pièges de format qui coûtent des points.",
             desc_short="Les quatre épreuves, leurs durées et les pièges de format.",
             h1="Le format du TCF Canada, épreuve par épreuve",
             intro="""Le TCF Canada, ce sont <strong>quatre épreuves obligatoires</strong> passées le même jour, en
<strong>2 h 47</strong> : 39 questions de compréhension orale en 35 minutes, 39 questions de compréhension
écrite en 60 minutes, trois tâches d'expression écrite en 60 minutes et trois tâches d'expression orale
en 12 minutes. Voici le format officiel, épreuve par épreuve, et les pièges de format qui font perdre des
points avant même que le niveau de français n'entre en jeu.""",
             facts=["<strong>4 épreuves en 2 h 47</strong>, le même jour, dans un centre agréé.",
                    "Compréhension orale : <strong>39 QCM, une seule écoute</strong>, pas de retour arrière.",
                    "Compréhension écrite : 39 QCM en 60 minutes, navigation libre.",
                    "Expression écrite : <strong>3 tâches</strong> de 60 à 180 mots ; expression orale : 3 tâches en 12 minutes, dont 2 de préparation.",
                    "Pour la citoyenneté, seules les deux épreuves orales sont exigées."],
             faq=[0, 6]),
        dict(slug="score-nclc", crumb="Score et NCLC", sections=["notation", "nclc"],
             title="Score TCF Canada et NCLC : la table de conversion",
             desc="Compréhensions sur 699, expressions sur 20, et la table officielle de conversion en NCLC : 458 en compréhension orale et 453 à l'écrit pour le NCLC 7.",
             desc_short="Les bandes de scores et la conversion en NCLC.",
             h1="Score TCF Canada et niveau NCLC : comment vous êtes noté",
             intro="""Au TCF Canada, les deux compréhensions sont notées de <strong>100 à 699</strong> et les deux
expressions de <strong>1 à 20</strong> ; chaque note correspond à un niveau du CECRL, puis à un
<strong>niveau NCLC</strong>, le seul qu'IRCC lise. Le NCLC 7 exige <strong>458 en compréhension orale,
453 en compréhension écrite et 10/20</strong> à chaque expression — un « B2 » sur l'attestation ne suffit
donc pas toujours. Les deux tables, et ce qu'elles impliquent pour votre dossier.""",
             facts=["Compréhensions notées sur <strong>699</strong>, expressions sur <strong>20</strong>.",
                    "<strong>NCLC 7</strong> = 458 en compréhension orale, 453 en compréhension écrite, 10/20 aux expressions.",
                    "<strong>NCLC 9</strong> = 523 et 524 aux compréhensions, 14/20 aux expressions.",
                    "⚠️ Le B2 commence à 400 : un B2 à 420 en compréhension orale ne vaut que NCLC 6.",
                    "Depuis les sessions du 1<sup>er</sup> septembre 2026, aucune recorrection n'est possible."],
             faq=[1]),
        dict(slug="preparation", crumb="Préparation", sections=["pourquoi", "preparer"],
             title="Se préparer au TCF Canada : méthode et ressources",
             desc="Pourquoi le français pèse autant dans Entrée express, et comment se préparer au TCF Canada épreuve par épreuve : format, exercices corrigés, examen blanc.",
             desc_short="Pourquoi le français vaut si cher, et comment travailler chaque épreuve.",
             h1="Se préparer au TCF Canada : la méthode, épreuve par épreuve",
             intro="""Le français n'a jamais autant pesé dans la sélection fédérale : les rondes francophones
d'Entrée express invitent à des scores bien inférieurs aux rondes générales. Se préparer au TCF Canada,
c'est d'abord <strong>connaître le format</strong> de chaque épreuve — une seule écoute, des tâches
d'écrit calibrées en mots, un oral de 12 minutes — puis <strong>se mesurer en conditions réelles</strong>
avant de payer une session. Voici pourquoi, et comment.""",
             facts=["Les <strong>rondes francophones</strong> d'Entrée express invitent à des scores nettement plus bas que les rondes générales.",
                    "Le format se travaille avant le niveau : une seule écoute, pas de retour arrière, des fenêtres de mots imposées.",
                    "Un <strong>examen blanc noté sur 699</strong> et converti en NCLC dit si la session du mois prochain est la bonne.",
                    "Chaque tentative se paie en entier et impose 20 à 30 jours d'attente.",
                    "Exercices corrigés, épreuve par épreuve, dans nos guides."],
             faq=[2]),
        dict(slug="prix-inscription", crumb="Prix, inscription, centres", sections=["inscription", "ou-passer"],
             title="TCF Canada : prix, inscription, validité et reprise",
             desc="195 à 285 € en France, 390 à 440 $ au Canada : le prix du TCF Canada, où s'inscrire, six centres avec contacts, la validité et les règles de reprise.",
             desc_short="Prix relevés, centres avec contacts, validité, reprise.",
             h1="TCF Canada : prix, inscription, centres, validité et reprise",
             intro="""Il n'existe <strong>aucun tarif national</strong> pour le TCF Canada : chaque centre agréé fixe
le sien — <strong>195 à 285 € en France</strong>, <strong>390 à 440 $ au Canada</strong>, et beaucoup de
grands centres ne publient rien. L'attestation vaut <strong>deux ans</strong>, comptés deux fois par
IRCC ; aucune reprise partielle n'existe, et 20 à 30 jours séparent deux passations. Voici les prix
relevés, les centres avec leurs contacts, et les règles à connaître avant de payer.""",
             facts=["<strong>Aucun tarif national</strong> : 195 à 285 € en France, 390 à 440 $ au Canada sur les centres relevés.",
                    "Attestation valable <strong>2 ans</strong> — et IRCC exige des résultats de moins de deux ans à la création du profil et au dépôt.",
                    "⚠️ <strong>Aucune reprise partielle</strong> : on repasse les quatre épreuves, après 20 à 30 jours.",
                    "Six centres relevés ci-dessous avec adresse, téléphone et site ; l'annuaire complet en compte 251 en France et 47 au Canada.",
                    "Le TCF Canada n'est pas éligible au CPF."],
             faq=[3, 4, 5]),
    ],
)

# ---------------------------------------------------------------------------
EXAMS["tcf-irn"] = dict(
    name="TCF IRN",
    landing_short="Ce qu'est le test de naturalisation, pour qui, et les modules du dossier.",
    what_h2="Qu'est-ce que le TCF IRN ?",
    what="""<p>Le <strong>TCF IRN</strong> — Intégration, Résidence, Nationalité — est le test de français de France
Éducation international destiné aux <strong>démarches françaises</strong> : demande de naturalisation,
première carte de résident, première carte de séjour pluriannuelle. Il remplace depuis 2022 les anciens
TCF ANF et CRF, et a été <strong>réformé en mai 2025</strong> pour mesurer jusqu'au niveau B2, devenu
obligatoire pour la naturalisation le 1<sup>er</sup> janvier 2026.</p>

<p>Le test dure <strong>1 h 35</strong> et comporte quatre épreuves insécables — compréhension orale,
compréhension écrite, expression écrite, expression orale — passées le même jour, en présentiel, dans un
centre agréé. Les QCM sont notés sur <strong>499</strong> (et non sur 699 comme les autres TCF), les
expressions sur 20 ; l'attestation vaut <strong>deux ans</strong>. Depuis 2026, la naturalisation exige
aussi un <a href="/blog/ou-passer-l-examen-civique/">examen civique</a>, distinct.</p>

<h3>Pour qui</h3>
<ul>
<li>Les candidats à la <strong>naturalisation</strong>, qui doivent prouver le B2 à l'oral comme à l'écrit.</li>
<li>Les demandeurs d'une première <strong>carte de résident</strong> (B1) ou d'une première <strong>carte de
séjour pluriannuelle</strong> (A2).</li>
<li>Ceux qui préfèrent un test rapide, chaque semaine, à un <a href="/delf-b2/">diplôme DELF</a> valable à vie
mais plus long à obtenir.</li>
</ul>""",
    faq=[
        ("Qu'est-ce que le TCF IRN ?",
         "Le test de connaissance du français « Intégration, Résidence et Nationalité » de France Éducation international, destiné aux démarches françaises : naturalisation, carte de résident, carte de séjour pluriannuelle. Quatre épreuves en 1 h 35, en présentiel, notées sur 499 pour les QCM et sur 20 pour les expressions ; attestation valable deux ans."),
        ("TCF IRN ou DELF : lequel choisir pour la naturalisation ?",
         "Les deux prouvent le B2. Le TCF IRN se passe presque chaque semaine dans les grandes villes et se corrige en trois semaines, mais expire au bout de deux ans ; le DELF B2 ne périme jamais, mais se passe dix fois par an avec des inscriptions qui ferment des semaines avant. Si votre dossier est proche, le TCF IRN ; si vous avez un trimestre, le DELF."),
        ("Le TCF IRN suffit-il pour être naturalisé ?",
         "Non : il prouve seulement la condition de langue. Depuis le 1er janvier 2026, la naturalisation exige aussi la réussite à l'examen civique, un test distinct passé dans un autre réseau de centres, ainsi que les conditions de résidence, de ressources et d'insertion."),
    ],
    modules=[
        ("Les niveaux", "A2, B1 ou B2 : ce que votre démarche exige", "/tcf-irn/niveaux/", "Le tableau depuis janvier 2026, et le piège du passage à B2."),
        ("Les épreuves", "Le format, l'échelle sur 499, le présentiel", "/tcf-irn/format/", "25 + 25 questions, un écrit de 30 minutes, un oral de 10 — et pourquoi votre B2 se joue entre 400 et 499."),
        ("Prix et inscription", "Prix, CPF, centres avec contacts", "/tcf-irn/prix-inscription/", "140 à 220 € selon le centre, l'inscription en ligne, six centres relevés."),
        ("Examen civique", "L'autre examen obligatoire depuis 2026", "/blog/ou-passer-l-examen-civique/", "Deux réseaux de centres, une pré-inscription en ligne, 70 à 110 €."),
        ("S'entraîner", "Les 4 épreuves corrigées", "/blog/exercices-tcf-irn/", "Un exercice corrigé par épreuve, au niveau B2 exigé pour la naturalisation."),
        ("Examen blanc", "Le TCF IRN complet, noté sur 499", "/examens-blancs/", "Dans l'app : les quatre épreuves au format réformé, avec la correction IA de l'écrit et de l'oral."),
    ],
    spokes=[
        dict(slug="niveaux", crumb="Niveaux exigés", sections=["niveaux", "b2"],
             title="TCF IRN : les niveaux exigés depuis 2026 (A2, B1, B2)",
             desc="A2 pour la carte pluriannuelle, B1 pour la carte de résident, B2 à l'oral et à l'écrit pour la naturalisation : les niveaux exigés depuis janvier 2026.",
             desc_short="Le tableau des niveaux par démarche depuis 2026.",
             h1="TCF IRN : les niveaux de français exigés depuis janvier 2026",
             intro="""Depuis le 1<sup>er</sup> janvier 2026, chaque démarche française a vu son niveau de français
relevé d'un cran : <strong>A2</strong> pour une première carte de séjour pluriannuelle, <strong>B1</strong>
pour une première carte de résident, <strong>B2 à l'oral comme à l'écrit</strong> pour la naturalisation.
Le TCF IRN mesure ces trois niveaux ; encore faut-il savoir lequel viser, et comprendre pourquoi le passage
de B1 à B2 est la marche la plus haute.""",
             facts=["<strong>Naturalisation : B2</strong> à l'oral et à l'écrit — c'était B1 avant 2026.",
                    "<strong>Carte de résident : B1</strong> — c'était A2.",
                    "<strong>Carte de séjour pluriannuelle : A2.</strong>",
                    "Le B2 se joue <strong>entre 400 et 499</strong> sur l'échelle du TCF IRN.",
                    "Un diplôme DELF du niveau exigé dispense du test, quel que soit son âge."],
             faq=[2, 6]),
        dict(slug="format", crumb="Format et épreuves", sections=["format", "reforme", "499", "presentiel"],
             title="Format du TCF IRN : 4 épreuves, échelle sur 499, présentiel",
             desc="Les quatre épreuves du TCF IRN réformé en 2025 — 1 h 35 —, l'échelle sur 499 que presque personne ne cite bien, et pourquoi il ne se passe pas en ligne.",
             desc_short="Les épreuves, la réforme de 2025, l'échelle sur 499.",
             h1="Le format du TCF IRN : les épreuves, l'échelle sur 499, le présentiel",
             intro="""Le TCF IRN, ce sont <strong>quatre épreuves insécables en 1 h 35</strong> : 25 questions de
compréhension orale en 20 minutes, 25 de compréhension écrite en 35 minutes, une expression écrite de
30 minutes et un oral de 10. Réformé le 12 mai 2025 pour mesurer jusqu'au B2, il est noté <strong>sur
499</strong> — pas sur 699 — et se passe obligatoirement <strong>en présentiel</strong>, dans un centre
agréé. Le format, la réforme, l'échelle et ce qu'elle change pour votre B2.""",
             facts=["<strong>4 épreuves en 1 h 35</strong>, insécables, le même jour.",
                    "Compréhensions : <strong>25 QCM</strong> chacune ; expressions écrite (30 min) et orale (10 min) notées sur 20.",
                    "⚠️ <strong>Noté sur 499</strong>, pas sur 699 : le B2 = 400 à 499.",
                    "Réformé le <strong>12 mai 2025</strong> pour mesurer jusqu'au B2 ; avant, il s'arrêtait à 399.",
                    "<strong>Présentiel obligatoire</strong> : l'arrêté du 22 décembre 2025 l'impose ; toute offre « en ligne » est une fraude."],
             faq=[0, 1, 3]),
        dict(slug="prix-inscription", crumb="Prix, inscription, centres", sections=["prix", "ou-passer"],
             title="TCF IRN : prix, CPF, inscription et centres agréés",
             desc="140 à 220 € selon le centre, éligible au CPF, chaque semaine à Paris : les prix relevés du TCF IRN, les pièges des forfaits, six centres avec contacts.",
             desc_short="Prix relevés, CPF, centres avec contacts.",
             h1="TCF IRN : prix, CPF, inscription et centres agréés",
             intro="""Il n'existe <strong>aucun tarif national</strong> pour le TCF IRN : sur les centres relevés, le
même test coûte <strong>140 € chez ACTE et 220 € chez ACCORD</strong>, à Paris, et 169 à 185 € à Lyon,
Rennes ou Montpellier. Il est <strong>éligible au CPF</strong> — attention aux forfaits « préparation +
examen » à plus de 400 € — et s'organise presque chaque semaine dans les grandes villes. Les prix, les
pièges, et six centres avec leurs contacts.""",
             facts=["<strong>140 à 220 €</strong> selon le centre, pour un test identique.",
                    "<strong>Éligible au CPF</strong> (fiche RS6643, jusqu'au 31 mai 2027) — mais les offres de Mon Compte Formation sont souvent des forfaits.",
                    "Sessions <strong>hebdomadaires</strong> à Paris, inscription en ligne quelques jours avant.",
                    "Résultats sous 2 à 3 semaines ; attestation valable 2 ans.",
                    "Chaque tentative se paie en entier : aucune reprise partielle."],
             faq=[4, 5, 7]),
    ],
)

# ---------------------------------------------------------------------------
EXAMS["tcf-quebec"] = dict(
    name="TCF Québec",
    landing_short="Ce qu'est le test modulaire du Québec, pour qui, et les modules du dossier.",
    what_h2="Qu'est-ce que le TCF Québec ?",
    what="""<p>Le <strong>TCF Québec</strong> — « TCF pour le Québec », TCF Q — est la version du test de
connaissance du français conçue pour les <strong>programmes d'immigration du Québec</strong> : ceux du
ministère de l'Immigration, de la Francisation et de l'Intégration (MIFI), dont le Programme de sélection
des travailleurs qualifiés. Sa particularité : il est <strong>modulaire</strong>. On s'inscrit à une, deux,
trois ou quatre épreuves — compréhension orale, compréhension écrite, expression orale, expression
écrite —, et l'on ne paie que celles que l'on passe.</p>

<p>Les compréhensions sont notées sur 699, les expressions sur 20, puis converties sur l'<strong>Échelle
québécoise</strong> des niveaux de compétence, graduée de 1 à 12 — un référentiel distinct des NCLC
fédéraux, avec lequel il est souvent confondu. Le TCF Québec <strong>n'est pas accepté par IRCC</strong>
pour Entrée express : pour un dossier fédéral, c'est le <a href="/tcf-canada/">TCF Canada</a>, que le
Québec reconnaît lui aussi depuis 2022.</p>

<h3>Pour qui</h3>
<ul>
<li>Les candidats aux programmes du <strong>Québec</strong> — PSTQ, PEQ — et leurs conjoints, dont plusieurs
volets n'exigent que l'oral.</li>
<li>Ceux qui veulent <strong>payer à la carte</strong> : deux épreuves orales coûtent environ la moitié
d'un TCF Canada complet.</li>
<li>Pas les candidats à Entrée express, ni à la citoyenneté canadienne.</li>
</ul>""",
    faq=[
        ("Qu'est-ce que le TCF Québec ?",
         "La version modulaire du test de connaissance du français conçue pour les programmes d'immigration du Québec (MIFI) : on s'inscrit à une, deux, trois ou quatre épreuves au choix. Les scores sont convertis sur l'Échelle québécoise, graduée de 1 à 12, distincte des NCLC fédéraux."),
        ("TCF Québec ou TCF Canada : lequel passer ?",
         "Pour un dossier fédéral — Entrée express, citoyenneté —, seul le TCF Canada est accepté. Pour un programme du Québec, les deux le sont : le TCF Québec permet de ne passer que les épreuves exigées et coûte moins cher ; le TCF Canada, complet, sert aux deux niveaux de sélection à la fois."),
        ("Le TCF Québec est-il valable partout au Canada ?",
         "Non. Il n'est reconnu que par le ministère de l'Immigration du Québec. IRCC ne l'accepte ni pour Entrée express ni pour la citoyenneté."),
    ],
    modules=[
        ("Les épreuves", "Le format modulaire, et le bon test", "/tcf-quebec/format-modulaire/", "29 + 29 questions, 3 exercices d'écrit, 3 d'oral, chaque épreuve indépendante — et quand préférer le TCF Canada."),
        ("La notation", "L'Échelle québécoise et ses pièges", "/tcf-quebec/echelle-quebecoise/", "La table de conversion, le niveau 7 qui n'est pas un NCLC 7, les seuils par programme, les points."),
        ("Prix et inscription", "Prix à la carte, dispenses, centres", "/tcf-quebec/prix-inscription/", "65 € par module à Montpellier, 105 à 125 $ par épreuve à l'UQTR, six centres avec contacts."),
        ("TEFAQ", "L'autre test modulaire du Québec", "/blog/tefaq-oral-quebec/", "Mêmes usages, autre réseau, souvent deux épreuves suffisent."),
        ("S'entraîner", "Expression orale et écrite corrigées", "/blog/sujets-expression-orale-tcf-canada/", "Les mêmes tâches que le TCF Canada, corrigées et expliquées."),
        ("Examen blanc", "Chaque épreuve, notée et convertie", "/examens-blancs/", "Dans l'app : le format officiel, la note sur 699 ou sur 20, l'Échelle québécoise."),
    ],
    spokes=[
        dict(slug="format-modulaire", crumb="Format modulaire", sections=["modulaire", "choisir"],
             title="TCF Québec : le format modulaire, épreuve par épreuve",
             desc="Le TCF Québec se passe épreuve par épreuve — 29 questions en 25 min, 29 en 45, 3 exercices d'écrit, 3 d'oral —, de 12 min à 2 h 22. Ou le TCF Canada ?",
             desc_short="Chaque épreuve, ses durées, et le choix TCF Québec ou Canada.",
             h1="Le format modulaire du TCF Québec, épreuve par épreuve",
             intro="""Le TCF Québec est le seul TCF où l'on choisit ses épreuves : <strong>29 questions</strong> de
compréhension orale en 25 minutes, 29 de compréhension écrite en 45, <strong>trois exercices</strong>
d'expression écrite en 60 minutes, trois d'expression orale en 12 — chacune indépendante, de
<strong>12 minutes à 2 h 22</strong> selon ce que votre programme exige. Ce que la modularité change au
prix et à la préparation, et quand le TCF Canada reste le meilleur choix.""",
             facts=["<strong>Modulaire</strong> : de 12 minutes (une épreuve) à 2 h 22 (les quatre).",
                    "Compréhensions : <strong>29 QCM</strong> chacune ; expressions : 3 exercices chacune.",
                    "Plusieurs volets québécois n'exigent que <strong>l'oral</strong> : deux épreuves suffisent.",
                    "⚠️ <strong>Pas accepté par IRCC</strong> pour Entrée express.",
                    "Le TCF Canada, complet, est reconnu par le Québec depuis 2022."],
             faq=[0, 1]),
        dict(slug="echelle-quebecoise", crumb="Échelle québécoise", sections=["echelle", "piege", "programmes", "points"],
             title="Échelle québécoise : convertir son score TCF Québec",
             desc="La table de conversion du TCF Québec vers l'Échelle québécoise (1 à 12), le piège du niveau 7 qui n'est pas un NCLC 7, les niveaux exigés par programme.",
             desc_short="La table de conversion, le piège du niveau 7, les seuils par programme.",
             h1="L'Échelle québécoise : convertir son score TCF Québec, programme par programme",
             intro="""Le Québec ne lit pas les NCLC : il convertit vos scores sur l'<strong>Échelle québécoise</strong>
des niveaux de compétence en français, graduée de <strong>1 à 12</strong>. Un niveau 7 québécois
correspond à 400 en compréhension orale — quand le NCLC 7 fédéral en exige 458 : les deux échelles
portent les mêmes numéros et ne recouvrent pas les mêmes scores. La table officielle, le piège, les
niveaux exigés par programme et ce que le français rapporte en points.""",
             facts=["Échelle québécoise : <strong>12 niveaux</strong> ; 7-8 = B2, 9-10 = C1.",
                    "⚠️ <strong>Niveau 7 québécois ≠ NCLC 7</strong> : 400 contre 458 en compréhension orale.",
                    "Compréhensions sur 699, expressions sur 20, converties épreuve par épreuve.",
                    "Les niveaux exigés varient par programme et par volet — l'oral compte souvent seul.",
                    "Aucune exigence d'anglais dans le PSTQ."],
             faq=[2, 4, 5]),
        dict(slug="prix-inscription", crumb="Prix, inscription, centres", sections=["prix", "ou-passer"],
             title="TCF Québec : prix à la carte, dispenses et centres",
             desc="Le TCF Québec se paie épreuve par épreuve — 65 € par module à Montpellier, 105 à 125 $ à l'UQTR : prix relevés, dispenses, six centres avec contacts.",
             desc_short="Prix à la carte, dispenses, centres avec contacts.",
             h1="TCF Québec : prix à la carte, dispenses, alternatives et centres",
             intro="""Parce qu'il est modulaire, le TCF Québec est le TCF le moins cher quand une démarche n'exige que
l'oral : <strong>65 € par module</strong> à l'Alliance française de Montpellier, <strong>105 à 125 $ par
épreuve</strong> à l'UQTR, contre 440 $ pour un TCF Canada complet dans le même centre. Les prix relevés,
les cas de dispense, les alternatives — TEFAQ, TCF Canada — et six centres avec leurs contacts.""",
             facts=["<strong>Prix à la carte</strong> : ne passer que l'oral coûte environ moitié moins qu'un TCF Canada complet.",
                    "Montpellier : 65 € par module ; Aix-Marseille : 60 € par épreuve ; UQTR : 105 $ (CO, CE, EE) et 125 $ (EO).",
                    "Beaucoup de grands centres canadiens ne publient aucun tarif.",
                    "Mêmes centres que le TCF Canada, au Québec comme en France.",
                    "Résultats valables 2 ans à la date de la demande."],
             faq=[3]),
    ],
)

# ---------------------------------------------------------------------------
EXAMS["tef-canada"] = dict(
    name="TEF Canada",
    landing_short="Ce qu'est le TEF Canada, le TEFAQ, pour qui, et les modules du dossier.",
    what_h2="Qu'est-ce que le TEF Canada ?",
    what="""<p>Le <strong>TEF Canada</strong> — test d'évaluation de français — est conçu par Le français des
affaires, l'organisme de la CCI Paris Île-de-France, et reconnu par Immigration, Réfugiés et Citoyenneté
Canada au même titre que le <a href="/tcf-canada/">TCF Canada</a>. Il comporte <strong>quatre épreuves</strong>
en <strong>2 h 55</strong> : compréhension écrite et compréhension orale à 40 questions, expression écrite
et expression orale en deux sections chacune. Chaque épreuve est notée sur sa propre échelle, puis
convertie en <strong>NCLC</strong> par IRCC.</p>

<p>Sa version québécoise, le <strong>TEFAQ</strong>, a exactement les mêmes épreuves mais elle est
modulaire — on n'y passe que ce que le programme exige — et se lit sur l'Échelle québécoise ; elle n'est
pas acceptée par IRCC. Les attestations valent <strong>deux ans</strong>, et l'on peut repasser une
épreuve après 20 jours.</p>

<h3>Pour qui</h3>
<ul>
<li>Les candidats à <strong>Entrée express</strong> et à la <strong>citoyenneté</strong> qui préfèrent le
format TEF — deux sections par expression, dont « écrire la suite d'un fait divers » — au format TCF.</li>
<li>Les candidats aux programmes du <strong>Québec</strong>, avec le TEFAQ, souvent en deux épreuves.</li>
<li>Ceux qui ont un centre TEF plus proche ou plus disponible qu'un centre TCF : les deux réseaux diffèrent.</li>
</ul>""",
    faq=[
        ("Qu'est-ce que le TEF Canada ?",
         "Un test de français de la CCI Paris Île-de-France (Le français des affaires), reconnu par IRCC pour l'immigration économique et la citoyenneté au même titre que le TCF Canada. Quatre épreuves en 2 h 55, notées chacune sur leur propre échelle puis converties en NCLC ; attestation valable deux ans."),
        ("TEF Canada ou TCF Canada ?",
         "Les deux sont acceptés par IRCC et valent la même chose. Ils diffèrent par le format — 40 questions par compréhension et deux sections par expression au TEF, contre 39 questions et trois tâches au TCF —, par leurs tables de conversion et par leurs réseaux de centres. Choisissez celui dont le format vous convient et dont un centre est disponible près de chez vous."),
        ("Le TEFAQ est-il un TEF Canada ?",
         "Non. Le TEFAQ a les mêmes épreuves, mais il est modulaire, se lit sur l'Échelle québécoise et ne sert qu'aux programmes du Québec. IRCC ne l'accepte pas pour Entrée express."),
    ],
    modules=[
        ("Les épreuves", "Le format et les tâches TEF", "/tef-canada/format/", "40 questions par compréhension, deux sections par expression : durées, particularités, et les tâches propres au TEF."),
        ("La notation", "Le score, l'ancien score, le NCLC", "/tef-canada/score-nclc/", "La table de conversion NCLC et le piège de la colonne « équivalence ancien score »."),
        ("TEFAQ", "La version québécoise, modulaire", "/tef-canada/tefaq/", "Mêmes épreuves, Échelle québécoise, deux épreuves souvent suffisantes — pas pour IRCC."),
        ("Préparation et inscription", "Méthode, prix, centres, validité", "/tef-canada/preparation-inscription/", "Comment se préparer, 245 € relevés à Paris, le réseau du Français des affaires, deux ans de validité."),
        ("S'entraîner", "Les épreuves corrigées", "/blog/exercices-tef-canada/", "Un exercice corrigé par épreuve, dont la suite du fait divers et les questions à l'examinateur."),
        ("Examen blanc", "Le TEF Canada complet, converti en NCLC", "/examens-blancs/", "Dans l'app : les quatre épreuves au format officiel, notées sur les échelles du test."),
    ],
    spokes=[
        dict(slug="format", crumb="Format et tâches", sections=["format", "taches"],
             title="Format du TEF Canada : les 4 épreuves et leurs tâches",
             desc="Les quatre épreuves du TEF Canada — 40 questions par compréhension, deux sections par expression, 2 h 55 — et les tâches propres au TEF à apprivoiser.",
             desc_short="Les quatre épreuves, leurs durées, et les tâches propres au TEF.",
             h1="Le format du TEF Canada, épreuve par épreuve — et les tâches à apprivoiser",
             intro="""Le TEF Canada, ce sont <strong>quatre épreuves en 2 h 55</strong> : 40 questions de compréhension
écrite en 60 minutes, 40 de compréhension orale en 40 minutes, une expression écrite en deux sections
(80 puis 200 mots minimum) et une expression orale en deux sections, en face à face. Le format officiel,
épreuve par épreuve, puis les tâches typiquement TEF — écrire la suite d'un fait divers, poser les
questions à l'examinateur — qu'on ne rencontre dans aucun autre test.""",
             facts=["<strong>4 épreuves en 2 h 55</strong> ; pour la citoyenneté, seules les deux orales.",
                    "Compréhensions : <strong>40 questions</strong> chacune ; une seule écoute à l'oral.",
                    "Expression écrite : section A 80 mots minimum (25 min), section B 200 mots (35 min).",
                    "Expression orale : 15 minutes en deux sections, dont les questions à poser à l'examinateur.",
                    "Format linéaire à l'écrit, sans retour arrière à l'oral."],
             faq=[0]),
        dict(slug="score-nclc", crumb="Score et NCLC", sections=["ancien-score", "nclc"],
             title="Score TEF Canada et NCLC : la table, l'ancien score",
             desc="Lire une attestation TEF Canada — IRCC convertit en NCLC la colonne « équivalence ancien score » — avec la table officielle : 207, 249 et 310 pour le NCLC 7.",
             desc_short="La table NCLC et le piège de la colonne « ancien score ».",
             h1="Score TEF Canada et niveau NCLC : lire son attestation sans se tromper",
             intro="""Une attestation TEF Canada affiche <strong>deux scores par épreuve</strong> : le score sur
l'échelle actuelle et son « équivalence ancien score » — et c'est cette seconde colonne qu'IRCC convertit
en NCLC. Sur ces échelles, le NCLC 7 exige <strong>207 en compréhension écrite, 249 en compréhension
orale, 310 à chaque expression</strong>. Le piège, la table officielle, et ce qu'un niveau de moins
coûte à un profil Entrée express.""",
             facts=["⚠️ IRCC lit la colonne <strong>« équivalence ancien score »</strong>, pas le score principal.",
                    "<strong>NCLC 7</strong> = 207 (CE), 249 (CO), 310 (EE et EO) sur ces échelles.",
                    "<strong>NCLC 9</strong> = 248, 298, 371 ; NCLC 10 = 263, 316, 393.",
                    "Chaque épreuve est convertie séparément : le NCLC le plus bas limite les points.",
                    "Attestation valable deux ans, comptés deux fois par IRCC."],
             faq=[1, 2]),
        dict(slug="tefaq", crumb="TEFAQ", sections=["tefaq"],
             title="TEFAQ : la version québécoise et modulaire du TEF",
             desc="Mêmes épreuves que le TEF Canada, mais modulaire et lu sur l'Échelle québécoise : à quoi sert le TEFAQ, ses seuils, et pourquoi IRCC ne l'accepte pas.",
             desc_short="Mêmes épreuves, Échelle québécoise, usage québécois seulement.",
             h1="TEFAQ : la version québécoise, modulaire, du TEF",
             intro="""Le <strong>TEFAQ</strong> — TEF pour l'accès au Québec — reprend exactement les quatre épreuves du TEF
Canada, mais on n'y passe que celles que son programme exige, et les résultats se lisent sur
l'<strong>Échelle québécoise</strong>, pas en NCLC. Plusieurs volets québécois ne demandant que l'oral,
deux épreuves suffisent souvent. Ce qu'il sert, ce qu'il ne sert pas, et comment le lire.""",
             facts=["<strong>Mêmes épreuves</strong> que le TEF Canada, mais modulaires.",
                    "Résultats sur l'<strong>Échelle québécoise</strong>, graduée de 1 à 12.",
                    "⚠️ <strong>Pas accepté par IRCC</strong> pour Entrée express ni pour la citoyenneté.",
                    "Deux épreuves orales suffisent à plusieurs volets du PSTQ et au conjoint accompagnateur.",
                    "Alternative : le <a href=\"/tcf-quebec/\">TCF Québec</a>, modulaire lui aussi."],
             faq=[3]),
        dict(slug="preparation-inscription", crumb="Préparation, prix, inscription", sections=["preparer", "inscription", "ou-passer"],
             title="TEF Canada : préparation, prix, inscription, validité",
             desc="Se préparer au TEF Canada, son prix (245 € relevés à Paris), où s'inscrire dans le réseau du Français des affaires, la validité et la reprise à 20 jours.",
             desc_short="Méthode, prix relevés, centres, validité, reprise.",
             h1="TEF Canada : se préparer, s'inscrire, et ce que ça coûte",
             intro="""Le TEF Canada se prépare sur son format — deux sections par expression, une seule écoute — plus que
sur le niveau, et s'organise dans un réseau propre, celui du <strong>Français des affaires</strong>, dont
l'annuaire de centres couvre tous les pays. Il n'existe aucun tarif national : <strong>245 €</strong> relevés
chez ALIP à Paris, aucun prix canadien vérifiable. L'attestation vaut deux ans, et une épreuve se repasse
après <strong>20 jours</strong>, sans ambiguïté. La méthode, les prix, l'inscription et trois centres
parisiens relevés.""",
             facts=["Le format se travaille avant le niveau : sections A et B, questions à poser, fait divers à poursuivre.",
                    "<strong>Aucun tarif national</strong> : 245 € relevés à Paris ; aucun prix canadien vérifiable pour le TEF Canada.",
                    "Inscription dans un centre agréé par <strong>Le français des affaires</strong> — pas par FEI.",
                    "Attestation valable <strong>2 ans</strong> — à compter de la date d'édition ou de passation selon la page officielle consultée.",
                    "Reprise après <strong>20 jours</strong>, épreuve par épreuve."],
             faq=[4, 5, 6]),
    ],
)

# ---------------------------------------------------------------------------
EXAMS["delf-b1"] = dict(
    name="DELF B1",
    landing_short="Ce qu'est le diplôme de niveau seuil, pour qui, et les modules du dossier.",
    what_h2="Qu'est-ce que le DELF B1 ?",
    what="""<p>Le <strong>DELF B1</strong> est un <strong>diplôme</strong> officiel du ministère de l'Éducation
nationale, délivré par France Éducation international, qui atteste le niveau B1 du Cadre européen — le
« niveau seuil », celui d'un utilisateur indépendant capable de se débrouiller dans la plupart des
situations de la vie quotidienne. Il se passe dans un centre agréé, lors de l'une des dix sessions
nationales de l'année, en <strong>quatre épreuves</strong> notées sur 25 : compréhension de l'oral,
compréhension des écrits, production écrite (160 mots), production orale en trois parties.</p>

<p>On l'obtient à partir de <strong>50/100</strong>, avec une note éliminatoire à 5/25 sur une seule
épreuve — et il est <strong>valable à vie</strong>. Depuis le 1<sup>er</sup> janvier 2026, le B1 est le
niveau exigé pour une première <strong>carte de résident</strong> : le DELF B1 le prouve définitivement,
là où un test TCF ou TEF expire au bout de deux ans.</p>

<h3>Pour qui</h3>
<ul>
<li>Les demandeurs d'une première <strong>carte de résident</strong>, qui doivent justifier du B1 à l'oral et à l'écrit.</li>
<li>Ceux qui veulent une preuve de niveau <strong>définitive</strong>, pour un dossier, un CV ou une formation.</li>
<li>Pas les candidats à la naturalisation : depuis 2026, c'est le <a href="/delf-b2/">B2</a> qu'il faut.</li>
</ul>""",
    faq=[
        ("Qu'est-ce que le DELF B1 ?",
         "Un diplôme officiel du ministère de l'Éducation nationale attestant le niveau B1 du Cadre européen : quatre épreuves notées sur 25, admission à partir de 50/100 avec une note éliminatoire à 5/25, en 2 h 10. Il est valable à vie et exigé, depuis janvier 2026, pour une première carte de résident."),
        ("Le DELF B1 est-il un test ou un diplôme ?",
         "Un diplôme : on le réussit ou on l'échoue, et une fois obtenu il ne périme jamais. Les tests TCF et TEF, eux, situent votre niveau sur une échelle sans seuil de réussite, mais leur attestation expire au bout de deux ans."),
        ("Faut-il le B1 ou le B2 pour la nationalité française ?",
         "Le B2, à l'oral comme à l'écrit, depuis le 1er janvier 2026. Le B1 concerne la carte de résident ; le A2, la première carte de séjour pluriannuelle."),
    ],
    modules=[
        ("Les épreuves", "Le format et le barème", "/delf-b1/format-bareme/", "Quatre épreuves en 2 h 10, 50/100 pour être admis, la note éliminatoire à 5/25."),
        ("La démarche", "Le B1 et la carte de résident", "/delf-b1/carte-de-resident/", "Le niveau exigé depuis 2026, et diplôme ou test : lequel choisir."),
        ("Réussir l'écrit et l'oral", "160 mots, trois parties, la méthode", "/delf-b1/ecrit-oral/", "Ce que le correcteur évalue à l'écrit, le déroulé de l'oral, comment se préparer."),
        ("Inscription", "Centres, sessions, prix", "/delf-b1/inscription/", "Dix sessions par an, 125 à 230 € selon le centre, six centres avec contacts."),
        ("Où passer le DELF", "Le calendrier 2026-2027 et les centres", "/blog/ou-passer-le-delf-en-france/", "143 centres, les fenêtres d'inscription, les prix relevés ville par ville."),
        ("Examen blanc", "Le DELF B1 complet, noté sur 100", "/examens-blancs/", "Dans l'app : les quatre épreuves, le seuil de 50 et la correction IA de l'écrit et de l'oral."),
    ],
    spokes=[
        dict(slug="format-bareme", crumb="Format et barème", sections=["format", "bareme"],
             title="Format et barème du DELF B1 : 4 épreuves, 50/100",
             desc="Les quatre épreuves du DELF B1 — 2 h 10 —, leur contenu et leur durée, le barème sur 100 points, le seuil d'admission à 50 et la note éliminatoire à 5/25.",
             desc_short="Les quatre épreuves, le barème sur 100, la note éliminatoire.",
             h1="Le format et le barème du DELF B1, épreuve par épreuve",
             intro="""Le DELF B1 se compose de <strong>quatre épreuves notées sur 25</strong> : compréhension de l'oral
(25 min), compréhension des écrits (45 min), production écrite de 160 mots (45 min) et production orale en
trois parties (15 min, dont 10 de préparation pour la troisième). On est admis à partir de
<strong>50 sur 100</strong> — sauf si une seule épreuve descend sous <strong>5/25</strong>, note
éliminatoire même avec 60 de moyenne. Le format officiel, puis le barème et la stratégie qu'il impose.""",
             facts=["<strong>4 épreuves</strong> sur 25 points, total sur 100, en <strong>2 h 10</strong>.",
                    "Admission à partir de <strong>50/100</strong>.",
                    "⚠️ Une note inférieure à <strong>5/25</strong> à une seule épreuve est éliminatoire.",
                    "Production écrite : <strong>160 mots minimum</strong> ; production orale : 3 parties.",
                    "Diplôme valable à vie, résultats en 4 à 6 semaines."],
             faq=[0, 1]),
        dict(slug="carte-de-resident", crumb="Carte de résident", sections=["carte-resident", "diplome-ou-test"],
             title="DELF B1 et carte de résident : le niveau exigé en 2026",
             desc="Depuis 2026, une première carte de résident exige le B1 à l'oral et à l'écrit : ce que le DELF B1 prouve, les justificatifs, diplôme ou test.",
             desc_short="Le B1 exigé depuis 2026, et diplôme ou test.",
             h1="Le DELF B1 et la carte de résident : le niveau exigé depuis 2026",
             intro="""Depuis le 1<sup>er</sup> janvier 2026, une première <strong>carte de résident</strong> exige le niveau
<strong>B1</strong> à l'oral comme à l'écrit — c'était A2 avant. Le DELF B1 le prouve, définitivement ;
un TCF IRN ou un TEF IRN le prouvent aussi, pour deux ans. Ce que dit l'arrêté du 22 décembre 2025, les
justificatifs recevables, les trois niveaux à ne pas confondre, et le choix entre diplôme et test selon
votre calendrier.""",
             facts=["<strong>Carte de résident : B1</strong> depuis le 1<sup>er</sup> janvier 2026 (arrêté du 22 décembre 2025).",
                    "⚠️ Trois niveaux à ne pas confondre : A2 carte pluriannuelle, B1 carte de résident, B2 naturalisation.",
                    "Le DELF B1 vaut <strong>à vie</strong> ; une attestation TCF ou TEF IRN vaut deux ans.",
                    "Dispense de niveau à partir de 65 ans pour les titres de séjour.",
                    "Un diplôme obtenu il y a des années reste recevable."],
             faq=[2, 5, 6]),
        dict(slug="ecrit-oral", crumb="Écrit et oral", sections=["ecrit", "oral", "preparer"],
             title="DELF B1 : réussir la production écrite et l'oral",
             desc="La production écrite du DELF B1 en 160 mots — ce que le correcteur évalue —, l'oral en trois parties et ses 10 minutes de préparation, et comment se préparer.",
             desc_short="L'écrit de 160 mots, l'oral en trois parties, la préparation.",
             h1="DELF B1 : réussir la production écrite et la production orale",
             intro="""Deux épreuves départagent les candidats au DELF B1 : la <strong>production écrite</strong>, un texte de
<strong>160 mots minimum</strong> en 45 minutes où le respect de la consigne et de la longueur pèse autant
que la langue, et la <strong>production orale</strong>, en trois parties — entretien, exercice en
interaction, expression d'un point de vue après 10 minutes de préparation. Ce que le correcteur évalue,
le déroulé exact, et la méthode pour arriver prêt.""",
             facts=["Production écrite : <strong>160 mots minimum</strong>, 45 minutes, notée sur 25.",
                    "Production orale : <strong>3 parties</strong>, 15 minutes, 10 minutes de préparation pour la troisième.",
                    "Écrire en dessous de la longueur coûte des points sur le respect de la consigne.",
                    "Les compréhensions sont à questions à choix multiples.",
                    "Un examen blanc noté sur 100, avec correction de l'écrit et de l'oral, avant de payer la session."],
             faq=[3, 4]),
        dict(slug="inscription", crumb="Inscription et centres", sections=["ou-passer"],
             title="S'inscrire au DELF B1 : centres, sessions, prix",
             desc="Où s'inscrire au DELF B1 : 143 centres agréés, dix sessions par an, des inscriptions qui ferment tôt, 125 à 230 € selon le centre, six centres avec contacts.",
             desc_short="Centres avec contacts, sessions, prix relevés.",
             h1="S'inscrire au DELF B1 : centres, sessions et prix",
             intro="""Le DELF B1 se passe dans l'un des <strong>143 centres agréés</strong> en France, lors de l'une des
<strong>dix sessions</strong> nationales de l'année — toujours le mercredi à 10 h —, et l'on s'inscrit
auprès du centre, jamais auprès de FEI. Chaque centre fixe son prix, de <strong>125 € à 230 €</strong> sur
ceux relevés, et sa fenêtre d'inscription, qui ferme quatre à dix semaines avant l'écrit. Les prochaines
sessions, six centres avec leurs contacts, et le chemin vers l'annuaire complet.""",
             facts=["<strong>143 centres agréés</strong> en France ; l'inscription se fait auprès du centre.",
                    "<strong>10 sessions par an</strong> ; le B1 se passe le mercredi à 10 h.",
                    "Prix libre : <strong>125 € (Nantes Université) à 230 € (Alliance française de Paris)</strong>.",
                    "⚠️ Les inscriptions ferment 4 à 10 semaines avant l'écrit, parfois sur deux jours.",
                    "Résultats en 4 à 6 semaines ; diplôme à vie."],
             faq=[],
             faq_extra=[("Quand ont lieu les prochaines sessions du DELF B1 ?",
                         "Le DELF B1 se passe le mercredi à 10 h de chaque session nationale : en 2026, les 7 octobre, 4 novembre et 2 décembre ; en 2027, dix sessions de janvier à décembre, jamais en avril ni en septembre. Chaque centre choisit les sessions qu'il ouvre et ferme ses inscriptions quatre à dix semaines avant."),
                        ("Combien coûte le DELF B1 ?",
                         "Il n'y a pas de tarif national. Sur les centres relevés le 17 septembre 2026 : 125 € à Nantes Université, 160 € à l'Alliance française de Lille, 194 € à la Sorbonne Nouvelle, 214 € aux Cours de civilisation française de la Sorbonne, 230 € à l'Alliance française de Paris.")]),
    ],
)

# ---------------------------------------------------------------------------
EXAMS["delf-b2"] = dict(
    name="DELF B2",
    landing_short="Ce qu'est le diplôme B2, pour qui, et les modules du dossier.",
    what_h2="Qu'est-ce que le DELF B2 ?",
    what="""<p>Le <strong>DELF B2</strong> est un <strong>diplôme</strong> officiel du ministère de l'Éducation
nationale, délivré par France Éducation international, qui atteste le niveau B2 du Cadre européen : celui
d'un utilisateur indépendant capable d'argumenter, de défendre une opinion et de suivre un cours
universitaire. Il se passe dans un centre agréé, lors de l'une des dix sessions nationales de l'année, en
<strong>quatre épreuves</strong> notées sur 25 : compréhension de l'oral, compréhension des écrits,
production écrite de 250 mots, production orale — un exposé suivi d'un débat.</p>

<p>On l'obtient à partir de <strong>50/100</strong>, avec une note éliminatoire à 5/25, et il est
<strong>valable à vie</strong>. C'est le diplôme le plus demandé du DELF : il ouvre les universités
françaises, et depuis le 1<sup>er</sup> janvier 2026 il prouve le B2 exigé pour la
<strong>naturalisation</strong> — définitivement, là où un TCF IRN expire au bout de deux ans.</p>

<h3>Pour qui</h3>
<ul>
<li>Les candidats à la <strong>naturalisation</strong>, qui doivent prouver le B2 à l'oral et à l'écrit.</li>
<li>Les étudiants qui visent une <strong>université française ou francophone</strong> — sous réserve des
filières qui demandent le C1.</li>
<li>Ceux qui veulent une preuve de niveau <strong>définitive</strong>, sans repasser un test tous les deux ans.</li>
</ul>""",
    faq=[
        ("Qu'est-ce que le DELF B2 ?",
         "Un diplôme officiel du ministère de l'Éducation nationale attestant le niveau B2 du Cadre européen : quatre épreuves notées sur 25, admission à partir de 50/100 avec une note éliminatoire à 5/25, en 2 h 50 plus 30 minutes de préparation avant l'oral. Il est valable à vie."),
        ("Le DELF B2 est-il un test ou un diplôme ?",
         "Un diplôme : on le réussit ou on l'échoue, et une fois obtenu il ne périme jamais. Les tests TCF et TEF, eux, situent votre niveau sans seuil de réussite, mais leur attestation expire au bout de deux ans."),
        ("Le DELF B2 remplace-t-il le TCF IRN pour la naturalisation ?",
         "Oui pour la condition de langue : le DELF B2 prouve le B2 exigé depuis 2026, à vie. Il ne dispense pas de l'examen civique ni des autres conditions de la naturalisation."),
    ],
    modules=[
        ("Les épreuves", "Le format, le barème, la réforme", "/delf-b2/format-bareme/", "Quatre épreuves en 2 h 50, 50/100 pour être admis, la note éliminatoire, ce que la réforme a changé."),
        ("À quoi il sert", "Université, naturalisation, à vie", "/delf-b2/a-quoi-sert/", "Ce que le DELF B2 ouvre en 2026, et les cas où il faut viser le C1."),
        ("Réussir l'écrit et l'oral", "250 mots, monologue puis débat", "/delf-b2/ecrit-oral/", "L'épreuve qui départage, l'oral en deux parties, et comment se préparer."),
        ("Inscription", "Centres, sessions, prix", "/delf-b2/inscription/", "Dix sessions par an, 125 à 280 € selon le centre, six centres avec contacts."),
        ("S'entraîner", "Les 4 épreuves corrigées", "/blog/exercices-delf-b2/", "Un exercice corrigé par épreuve, au format réformé, et la stratégie du seuil."),
        ("Examen blanc", "Le DELF B2 complet, noté sur 100", "/examens-blancs/", "Dans l'app : les quatre épreuves, le seuil de 50 et la correction IA de l'écrit et de l'oral."),
    ],
    spokes=[
        dict(slug="format-bareme", crumb="Format et barème", sections=["format", "bareme", "reforme"],
             title="Format et barème du DELF B2 : épreuves, 50/100, réforme",
             desc="Les quatre épreuves du DELF B2 réformé — 2 h 50 plus 30 minutes de préparation —, le barème sur 100, le seuil de 50, la note éliminatoire à 5/25, la réforme.",
             desc_short="Les quatre épreuves, le barème, la note éliminatoire, la réforme.",
             h1="Le format et le barème du DELF B2, épreuve par épreuve",
             intro="""Le DELF B2 se compose de <strong>quatre épreuves notées sur 25</strong> : compréhension de l'oral
(30 min), compréhension des écrits (60 min), production écrite de 250 mots (60 min) et production orale —
monologue suivi puis débat, 20 minutes après 30 de préparation. On est admis à partir de
<strong>50 sur 100</strong>, sauf note inférieure à <strong>5/25</strong> à une seule épreuve. Depuis la
réforme, les compréhensions sont 100 % QCM et l'entretien dirigé a disparu. Le format, le barème, la
réforme.""",
             facts=["<strong>4 épreuves</strong> sur 25 points, total sur 100, en <strong>2 h 50</strong> plus 30 minutes de préparation.",
                    "Admission à partir de <strong>50/100</strong>.",
                    "⚠️ Une note inférieure à <strong>5/25</strong> à une seule épreuve est éliminatoire, quelle que soit la moyenne.",
                    "Compréhensions <strong>100 % QCM</strong> depuis la réforme ; format généralisé depuis septembre 2024.",
                    "Diplôme valable à vie."],
             faq=[0, 1, 2]),
        dict(slug="a-quoi-sert", crumb="À quoi il sert", sections=["a-quoi-sert"],
             title="À quoi sert le DELF B2 : université, naturalisation, à vie",
             desc="Ce que le DELF B2 ouvre en 2026 — l'université, la condition de langue de la naturalisation —, les cas où viser le C1, et l'avantage d'un diplôme à vie.",
             desc_short="Université, naturalisation, et les cas où le C1 s'impose.",
             h1="À quoi sert le DELF B2 en 2026",
             intro="""Le DELF B2 est le diplôme de français le plus demandé parce qu'il ouvre deux portes à la fois :
l'<strong>université</strong> — la plupart des licences et masters l'exigent, certaines filières demandant
le C1 — et, depuis le 1<sup>er</sup> janvier 2026, la <strong>naturalisation</strong>, dont il prouve la
condition de langue à vie. Ce qu'il permet, ce qu'il ne permet pas, et les cas où c'est le
<a href="/dalf/">DALF C1</a> qu'il faut viser.""",
             facts=["<strong>Université</strong> : le B2 est le niveau standard d'admission ; certaines filières exigent le C1.",
                    "<strong>Naturalisation</strong> : le DELF B2 prouve le B2 exigé depuis 2026 — sans dispenser de l'examen civique.",
                    "<strong>Valable à vie</strong>, contrairement aux attestations TCF et TEF.",
                    "L'exigence de l'établissement prime toujours sur le diplôme.",
                    "Passer de B1 à B2 prend en général plusieurs mois de travail régulier."],
             faq=[3, 4, 5]),
        dict(slug="ecrit-oral", crumb="Écrit et oral", sections=["ecrit", "oral", "preparer"],
             title="DELF B2 : réussir la production écrite et l'oral",
             desc="La production écrite du DELF B2 — 250 mots argumentés en 60 minutes, l'épreuve qui départage —, l'oral en monologue puis débat, et comment se préparer.",
             desc_short="L'écrit de 250 mots, le monologue et le débat, la préparation.",
             h1="DELF B2 : réussir la production écrite et la production orale",
             intro="""Au DELF B2, c'est la <strong>production écrite</strong> qui départage : un texte argumenté de
<strong>250 mots minimum</strong> en 60 minutes, évalué sur le respect de la consigne, la cohérence et la
langue. L'<strong>oral</strong>, lui, se joue en deux temps — un monologue suivi préparé pendant 30 minutes,
puis un débat avec le jury. Ce que le correcteur évalue, le déroulé exact de chaque épreuve, et la
méthode pour arriver prêt.""",
             facts=["Production écrite : <strong>250 mots minimum</strong>, 60 minutes, prise de position argumentée.",
                    "Production orale : <strong>monologue puis débat</strong>, 20 minutes après 30 de préparation.",
                    "Écrire en dessous de 250 mots coûte des points sur le respect de la consigne.",
                    "La note éliminatoire à 5/25 impose de ne négliger aucune épreuve.",
                    "Un examen blanc noté sur 100, avec correction de l'écrit et de l'oral, avant de payer la session."],
             faq=[6]),
        dict(slug="inscription", crumb="Inscription et centres", sections=["ou-passer"],
             title="S'inscrire au DELF B2 : centres, sessions, prix",
             desc="Où s'inscrire au DELF B2 : 143 centres agréés, dix sessions par an, des inscriptions qui ferment tôt, 125 à 280 € selon le centre, six centres avec contacts.",
             desc_short="Centres avec contacts, sessions, prix relevés.",
             h1="S'inscrire au DELF B2 : centres, sessions et prix",
             intro="""Le DELF B2 se passe dans l'un des <strong>143 centres agréés</strong> en France, lors de l'une des
<strong>dix sessions</strong> nationales de l'année — toujours le mercredi à 14 h —, et l'on s'inscrit
auprès du centre, jamais auprès de FEI. Chaque centre fixe son prix, de <strong>125 € à 280 €</strong> sur
ceux relevés, et sa fenêtre d'inscription, qui ferme quatre à dix semaines avant l'écrit. Les prochaines
sessions, six centres avec leurs contacts, et le chemin vers l'annuaire complet.""",
             facts=["<strong>143 centres agréés</strong> en France ; l'inscription se fait auprès du centre.",
                    "<strong>10 sessions par an</strong> ; le B2 se passe le mercredi à 14 h.",
                    "Prix libre : <strong>125 € (Nantes Université) à 280 € (Alliance française de Paris)</strong>.",
                    "⚠️ Les inscriptions ferment 4 à 10 semaines avant l'écrit ; des sessions affichent complet des mois avant.",
                    "Résultats en 4 à 6 semaines ; diplôme à vie."],
             faq=[],
             faq_extra=[("Quand ont lieu les prochaines sessions du DELF B2 ?",
                         "Le DELF B2 se passe le mercredi à 14 h de chaque session nationale : en 2026, les 7 octobre, 4 novembre et 2 décembre ; en 2027, dix sessions de janvier à décembre, jamais en avril ni en septembre. Chaque centre choisit les sessions qu'il ouvre et ferme ses inscriptions quatre à dix semaines avant."),
                        ("Combien coûte le DELF B2 ?",
                         "Il n'y a pas de tarif national. Sur les centres relevés le 17 septembre 2026 : 125 € à Nantes Université, 159 € à l'Alliance française de Lyon, 180 € à Lille, 249 € à la Sorbonne Nouvelle, 269 € aux Cours de civilisation française de la Sorbonne, 280 € à l'Alliance française de Paris.")]),
    ],
)

# ---------------------------------------------------------------------------
EXAMS["dalf"] = dict(
    name="DALF C1 · C2",
    landing_short="Ce que sont les diplômes avancés, pour qui, et les modules du dossier.",
    what_h2="Qu'est-ce que le DALF ?",
    what="""<p>Le <strong>DALF</strong> — diplôme approfondi de langue française — est le diplôme officiel du ministère
de l'Éducation nationale pour les deux niveaux avancés du Cadre européen : le <strong>C1</strong>, celui
d'un utilisateur autonome capable d'un discours clair et structuré, et le <strong>C2</strong>, celui de
la maîtrise. Comme le DELF, il est délivré par France Éducation international, se passe dans les mêmes
centres agréés, aux mêmes sessions — le jeudi —, et il est <strong>valable à vie</strong>.</p>

<p>Le <strong>DALF C1</strong> comporte quatre épreuves notées sur 25, en 4 heures plus une heure de
préparation : compréhensions, production écrite — une synthèse de documents de 200 à 240 mots suivie d'un
essai —, exposé oral. Le <strong>DALF C2</strong> n'a que deux épreuves intégrées, notées sur 50 : une
orale et une écrite de 700 mots minimum. Admission à 50/100 dans les deux cas. Le DALF <strong>dispense
de tout test de français</strong> à l'entrée des universités françaises.</p>

<h3>Pour qui</h3>
<ul>
<li>Les étudiants dont la filière exige le <strong>C1</strong> — lettres, droit, médecine, certaines grandes écoles.</li>
<li>Les professionnels qui veulent une preuve de niveau avancé, <strong>à vie</strong>.</li>
<li>Pas les démarches administratives françaises, qui s'arrêtent au B2 : le <a href="/delf-b2/">DELF B2</a> suffit.</li>
</ul>""",
    faq=[
        ("Qu'est-ce que le DALF ?",
         "Le diplôme approfondi de langue française, diplôme officiel du ministère de l'Éducation nationale pour les niveaux C1 et C2 du Cadre européen. Deux diplômes indépendants, délivrés par France Éducation international dans les mêmes centres et aux mêmes sessions que le DELF, valables à vie."),
        ("Faut-il avoir le DELF B2 pour passer le DALF ?",
         "Non : chaque diplôme est indépendant. On s'inscrit directement au C1, ou même au C2, sans avoir passé les niveaux précédents."),
        ("Le DALF sert-il pour la naturalisation ?",
         "Il prouve largement le B2 exigé, mais il n'est pas nécessaire : le DELF B2 suffit pour la condition de langue. Le DALF vise surtout l'université et les usages professionnels."),
    ],
    modules=[
        ("Les épreuves", "Le C1, le C2, le barème", "/dalf/format/", "Quatre épreuves au C1, deux au C2, 4 heures plus 1 de préparation, 50/100 et les notes éliminatoires."),
        ("C1 ou C2", "Lequel viser, ce qu'il dispense", "/dalf/c1-ou-c2/", "Le C1 suffit presque partout ; le C2 est un exercice de maîtrise. Et la dispense de test à l'université."),
        ("La synthèse", "L'épreuve reine du C1, et la préparation", "/dalf/synthese-preparation/", "200 à 240 mots, aucune citation, aucun avis : la méthode, et comment se préparer aux quatre épreuves."),
        ("Inscription", "Centres, sessions, prix", "/dalf/inscription/", "Les mêmes centres que le DELF, le jeudi ; 145 à 290 € selon le centre ; six centres avec contacts."),
        ("S'entraîner", "La synthèse de documents pas à pas", "/blog/synthese-dalf-c1/", "Les trois règles absolues, le plan croisé et la méthode en six étapes."),
        ("Examen blanc", "Le DALF C1 complet, noté sur 100", "/examens-blancs/", "Dans l'app : les quatre épreuves et la correction IA de la synthèse et de l'essai."),
    ],
    spokes=[
        dict(slug="format", crumb="Format et barème", sections=["c1", "c2", "bareme"],
             title="Format du DALF C1 et C2 : épreuves, durées, barème",
             desc="Les quatre épreuves du DALF C1 — synthèse, essai, exposé, 4 h plus 1 de préparation —, les deux du C2, et le barème : 50/100, 5/25 et 10/50 éliminatoires.",
             desc_short="Les épreuves du C1 et du C2, les durées, le barème.",
             h1="Le format du DALF C1 et du DALF C2, épreuve par épreuve",
             intro="""Le <strong>DALF C1</strong> comporte quatre épreuves notées sur 25 : compréhension de l'oral (40 min),
compréhension des écrits (50 min), production écrite — synthèse de 200 à 240 mots puis essai de 250 mots —
en 2 h 30, et un exposé oral de 30 minutes après une heure de préparation. Le <strong>DALF C2</strong> n'en
a que deux, intégrées et notées sur 50 : une orale, une écrite de 700 mots minimum. Admission à
<strong>50/100</strong>, note éliminatoire à 5/25 au C1 et 10/50 au C2. Le détail, épreuve par épreuve.""",
             facts=["<strong>DALF C1 : 4 épreuves</strong> sur 25, 4 heures plus 1 heure de préparation.",
                    "<strong>DALF C2 : 2 épreuves intégrées</strong> sur 50, 4 heures plus 1 heure de préparation.",
                    "Admission à <strong>50/100</strong> ; éliminatoire à <strong>5/25</strong> au C1, <strong>10/50</strong> au C2.",
                    "C1 : synthèse de 200-240 mots + essai de 250 mots ; C2 : texte de 700 mots minimum.",
                    "Les anciennes options (lettres / sciences) ont été supprimées."],
             faq=[0, 2, 4]),
        dict(slug="synthese-preparation", crumb="Synthèse et préparation", sections=["synthese", "preparer"],
             title="DALF C1 : la synthèse de documents et la préparation",
             desc="La synthèse de documents du DALF C1 — 200 à 240 mots, aucune citation, aucun avis —, ses trois règles, et comment se préparer aux quatre épreuves du diplôme.",
             desc_short="L'épreuve reine du C1, et la méthode de préparation.",
             h1="DALF C1 : la synthèse, épreuve reine, et comment se préparer",
             intro="""La <strong>synthèse de documents</strong> est l'épreuve qui fait la différence au DALF C1 : reformuler
en <strong>200 à 240 mots</strong>, sans citer ni juger, l'essentiel de plusieurs documents, avec un plan
qui les croise. Ses trois règles absolues, ce que le correcteur sanctionne, puis la méthode pour préparer
les quatre épreuves — compréhensions, écrit, exposé — sur les semaines qui précèdent la session.""",
             facts=["Synthèse : <strong>200 à 240 mots</strong>, objective, entièrement reformulée.",
                    "Trois règles : <strong>aucune citation, aucun avis, un plan qui croise</strong> les documents.",
                    "L'essai de 250 mots suit la synthèse, dans les mêmes 2 h 30.",
                    "L'exposé oral se prépare pendant une heure surveillée, à partir d'un dossier.",
                    "Un examen blanc noté sur 100, avec correction de la synthèse, avant de payer la session."],
             faq=[1]),
        dict(slug="c1-ou-c2", crumb="C1 ou C2", sections=["c1-ou-c2", "dispense"],
             title="DALF C1 ou C2 : lequel viser, et ce qu'il dispense",
             desc="Le C1 suffit à presque toutes les démarches, le C2 est un exercice de maîtrise : comment choisir, et la dispense de test que le DALF donne à l'université.",
             desc_short="Choisir son niveau, et la dispense de test à l'université.",
             h1="DALF C1 ou C2 : lequel viser, et ce que le diplôme vous dispense de passer",
             intro="""Le <strong>C1</strong> suffit à presque tout : universités, grandes écoles, usages professionnels. Le
<strong>C2</strong> est un exercice de maîtrise que peu de démarches exigent. Et l'un comme l'autre
<strong>dispense de tout test de français</strong> à l'entrée des établissements français — là où un
DELF B2 peut ne pas suffire à certaines filières. Comment choisir son niveau, et ce que le diplôme vous
évite ensuite.""",
             facts=["Le <strong>C1</strong> répond à presque toutes les exigences ; le <strong>C2</strong> est rarement demandé.",
                    "Diplômes indépendants : on s'inscrit directement au niveau visé.",
                    "Le DALF <strong>dispense de tout test de français</strong> à l'entrée des universités françaises.",
                    "Diplôme valable <strong>à vie</strong>, contrairement aux attestations TCF et TEF.",
                    "Pour un dossier universitaire, vérifiez l'exigence de l'établissement : B2, parfois C1."],
             faq=[3, 5, 6]),
        dict(slug="inscription", crumb="Inscription et centres", sections=["ou-passer"],
             title="S'inscrire au DALF : centres, sessions, prix",
             desc="Où s'inscrire au DALF C1 ou C2 : les mêmes 143 centres que le DELF, le jeudi de chaque session, 145 à 290 € selon le centre, six centres avec contacts.",
             desc_short="Centres avec contacts, sessions, prix relevés.",
             h1="S'inscrire au DALF : centres, sessions et prix",
             intro="""Le DALF se passe dans les <strong>mêmes 143 centres agréés</strong> que le DELF, aux mêmes sessions —
le <strong>jeudi</strong>, C1 à 9 h, C2 à 14 h 30 —, dix fois par an. Tous les centres n'ouvrent pas le
DALF à chaque session, et chacun fixe son prix : de <strong>145 € à 290 €</strong> pour le C1 sur ceux
relevés. Les prochaines sessions, six centres avec leurs contacts, et l'annuaire complet.""",
             facts=["Mêmes centres et mêmes sessions que le DELF ; le DALF se passe le <strong>jeudi</strong>.",
                    "<strong>10 sessions par an</strong>, jamais en avril ni en septembre.",
                    "Prix libre : <strong>145 € (Nantes Université) à 290 € (Alliance française de Paris)</strong> pour le C1.",
                    "⚠️ Tous les centres n'ouvrent pas le DALF à chaque session : lisez le calendrier du centre.",
                    "Résultats en 4 à 6 semaines ; diplôme à vie."],
             faq=[],
             faq_extra=[("Quand ont lieu les prochaines sessions du DALF ?",
                         "Le DALF se passe le jeudi de chaque session nationale — C1 à 9 h, C2 à 14 h 30 : en 2026, les 8 octobre, 5 novembre et 3 décembre ; en 2027, dix sessions de janvier à décembre. Tous les centres n'ouvrent pas le DALF à chaque session : le calendrier du centre fait foi."),
                        ("Combien coûte le DALF ?",
                         "Il n'y a pas de tarif national. Sur les centres relevés le 17 septembre 2026 : 145 € à Nantes Université pour le C1 ou le C2, 200 € et 210 € à l'Alliance française de Lille, 249 € (C1) et 290 € (C2) à la Sorbonne Nouvelle, 279 € (C1) aux Cours de civilisation française de la Sorbonne, 290 € à l'Alliance française de Paris.")]),
    ],
)
