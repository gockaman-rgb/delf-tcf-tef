#!/usr/bin/env python3
"""Cluster « exercices » — TCF Canada, une page par épreuve.

Les échantillons sont de VRAIS items des banques de l'app (tcf_listening.json,
tcf_reading.json, tcf_writing.json, tcf_speaking.json), avec leurs corrigés et
leurs explications d'origine.

⚠️ Expression écrite : les sujets retenus sont ceux qui n'embarquent PAS de
nombre de mots dans leur énoncé (même filtre que `embedsWordCount` dans
MockExamViewModel), et ils sont présentés avec les fenêtres du TCF Canada
(60-120 / 120-150 / 120-180) et non celles du pool générique — sans quoi
l'article contredirait /tcf-canada/.
"""

from article_template import build

def exo(n, niveau, source_label, source, question, options, bonne, expl):
    """Un exercice : énoncé visible + corrigé repliable."""
    opts = "\n".join(f"<li>{o}</li>" for o in options)
    return f"""
<div class="note">
<p><strong>Exercice {n} — niveau {niveau}</strong></p>
<p><em>{source_label}</em></p>
<p>{source}</p>
<p><strong>Question :</strong> {question}</p>
<ol type="A">
{opts}
</ol>
</div>
<div class="faq"><details><summary>Voir la réponse et l'explication</summary>
<p><strong>Réponse : {bonne}</strong> — {expl}</p></details></div>
"""

ARTICLES = [

# ═══════════════════════════════════════════ 1. COMPRÉHENSION ORALE
{
"slug": "exercices-comprehension-orale-tcf-canada",
"title": "Exercices de compréhension orale TCF Canada",
"desc": "39 questions en 35 minutes, une seule écoute : 4 exercices corrigés du niveau B1 au B2, le calcul du temps par question et la méthode qui évite de décrocher.",
"og_title": "Exercices de compréhension orale TCF Canada",
"og_desc": "39 questions en 35 minutes, une seule écoute. 4 exercices corrigés du B1 au B2 et la méthode qui évite de décrocher.",
"crumb": "Exercices de compréhension orale",
"h1": "Exercices de compréhension orale du TCF Canada, corrigés",
"date_fr": "7 août 2026",
"read": 8,
"accent": "accent-tcf",
"intro": """<strong>39 questions à choix multiples en 35 minutes</strong>, soit environ
<strong>54 secondes par question</strong> — et <strong>une seule écoute</strong>, sans retour
arrière possible. C'est l'épreuve où l'on perd le plus de points sans être en cause sur la langue.
Voici quatre exercices corrigés, du B1 au B2, et la méthode pour ne pas décrocher.""",
"facts": [
"<strong>39 QCM à 4 choix · 35 minutes</strong> — environ <strong>54 secondes par question</strong>.",
"⚠️ <strong>Une seule écoute</strong>, aucun retour arrière : une question manquée est perdue.",
"Difficulté <strong>progressive A1 → C2</strong> : vous n'êtes pas censé tout réussir.",
"Types de documents : dialogue, exposé, interview, annonce, message.",
"Le saut B1 → B2 se joue sur les questions d'<strong>attitude et d'intention</strong>, pas de repérage.",
"<strong>NCLC 7</strong> commence à <strong>458</strong> sur 699 en compréhension orale.",
],
"toc": [
("format", "Le format de l'épreuve"),
("exercices", "Quatre exercices corrigés"),
("saut", "Ce qui change vraiment entre B1 et B2"),
("methode", "La méthode pour ne pas décrocher"),
("erreurs", "Les erreurs qui coûtent le plus"),
],
"body": """
<h2 id="format">Le format de l'épreuve</h2>

<div class="tablewrap">
<table>
<caption>Compréhension orale du TCF Canada. Source : France Éducation international, structure vérifiée en juillet 2026.</caption>
<thead><tr><th>Paramètre</th><th>Valeur</th></tr></thead>
<tbody>
<tr><td>Questions</td><td><strong>39 QCM</strong> à 4 choix</td></tr>
<tr><td>Durée</td><td><strong>35 minutes</strong></td></tr>
<tr><td>Temps moyen par question</td><td><strong>≈ 54 secondes</strong>, audio compris</td></tr>
<tr><td>Écoutes</td><td><strong>1 seule</strong>, sans retour arrière</td></tr>
<tr><td>Difficulté</td><td>progressive, de A1 à C2</td></tr>
<tr><td>Notation</td><td>de 100 à 699 → <a href="/blog/tcf-canada-nclc-7/">NCLC</a></td></tr>
</tbody>
</table>
</div>

<p>Ces 54 secondes sont le chiffre à garder en tête : elles incluent l'écoute du document, la
lecture des quatre propositions et le choix. Autant dire qu'il n'y a <strong>aucun temps mort</strong>,
et qu'une seule hésitation prolongée décale tout ce qui suit.</p>

<p>Les documents s'enchaînent sans transition et changent de nature : un dialogue de trente
secondes peut être suivi d'un exposé de deux minutes, puis d'une interview à plusieurs voix. C'est
cette variété qui fatigue, plus que la difficulté linguistique elle-même.</p>

<h2 id="exercices">Quatre exercices corrigés</h2>

<p>Les quatre exercices ci-dessous suivent la progression réelle de l'épreuve. Les deux premiers
sont de niveau B1, les deux suivants de niveau B2 — c'est-à-dire au-dessus du seuil NCLC 7.
Lisez le document une seule fois, comme le jour J.</p>

""" + exo(1, "B1", "Ce que vous entendez — exposé radiophonique, 1 locuteur :",
"« Bonjour à tous et bienvenue dans notre émission <em>Vie Quotidienne</em>. Aujourd'hui, nous "
"allons parler du tri des déchets en France. Depuis plusieurs années, le tri sélectif est "
"obligatoire dans toutes les communes françaises. Mais savez-vous vraiment dans quelle poubelle "
"mettre vos déchets ? La poubelle jaune est destinée aux emballages : bouteilles en plastique, "
"cartons, conserves métalliques. La poubelle verte ou blanche reçoit le verre : bouteilles, pots, "
"bocaux. Attention, la vaisselle cassée ne va pas dans le bac à verre. La poubelle grise ou noire "
"est pour les ordures ménagères, c'est-à-dire tout le reste. »",
"Où doit-on mettre les bouteilles en plastique ?",
["Dans la poubelle verte", "Dans la poubelle blanche", "Dans la poubelle jaune", "Dans la poubelle grise"],
"C — Dans la poubelle jaune",
"la poubelle jaune est destinée aux emballages, dont les bouteilles en plastique. "
"C'est une question de <strong>repérage d'information</strong> : la réponse est dite textuellement.") + exo(
2, "B1", "Ce que vous entendez — dialogue, 3 locuteurs :",
"« <strong>Karim :</strong> Alors Ahmed, tu en es où avec ta demande de naturalisation ?<br>"
"<strong>Ahmed :</strong> J'ai déposé mon dossier il y a six mois à la préfecture. On m'a dit que "
"le délai moyen était de dix-huit mois.<br>"
"<strong>Sophie :</strong> C'est long !<br>"
"<strong>Ahmed :</strong> Et tu as déjà passé l'entretien ?<br>"
"<strong>Karim :</strong> Pas encore, j'attends la convocation. Mais j'ai déjà passé le test de "
"français, le TCF. »",
"Quel est le délai moyen pour une demande de naturalisation ?",
["Six mois", "Dix-huit mois", "Douze mois", "Vingt-quatre mois"],
"B — Dix-huit mois",
"le piège est le « six mois », qui est mentionné juste avant mais désigne le temps écoulé "
"<em>depuis le dépôt</em>, pas le délai moyen. En dialogue, <strong>deux chiffres proches se "
"télescopent</strong> : c'est le mécanisme de distraction le plus courant.") + exo(
3, "B2", "Ce que vous entendez — interview, plusieurs intervenants :",
"« <strong>Pierre Martineau :</strong> L'abstention n'a cessé d'augmenter en France depuis les "
"années mille neuf cent quatre-vingts. Aux dernières élections législatives, près de la moitié des "
"électeurs inscrits ne se sont pas déplacés.<br>"
"<strong>Yasmine Karim :</strong> Mais il faut nuancer. L'abstention n'est pas uniforme. Elle est "
"beaucoup plus forte chez les jeunes de dix-huit à vingt-quatre ans, où elle dépasse souvent les "
"soixante pour cent, et dans les quartiers populaires. »",
"Quelle est l'abstention chez les jeunes ?",
["Plus de 60 pour cent", "Près de 80 pour cent", "Environ 30 pour cent", "Environ 45 pour cent"],
"A — Plus de 60 pour cent",
"c'est Yasmine Karim, et non l'invité principal, qui donne le chiffre. En interview à plusieurs "
"voix, <strong>il faut suivre qui dit quoi</strong> : « près de la moitié » énoncé juste avant "
"concerne l'ensemble des électeurs, pas les jeunes.") + exo(
4, "B2", "Ce que vous entendez — conférence, 1 locutrice :",
"« Les prédictions les plus alarmistes estiment que l'intelligence artificielle pourrait remplacer "
"trente à quarante pour cent des emplois actuels d'ici deux mille quarante. Mais je voudrais "
"apporter un éclairage plus nuancé. L'histoire des révolutions technologiques nous enseigne que la "
"destruction d'emplois s'accompagne toujours de la création de nouveaux métiers, souvent "
"impossibles à imaginer à l'avance. Cependant, et c'est là que les choses se compliquent, cette "
"transition ne se fait pas sans douleur. »",
"Quelle est son attitude envers les prédictions sur l'IA ?",
["Elle accepte complètement et sans réserve les projections les plus alarmistes",
 "Elle estime que les prédictions sous-évaluent le phénomène",
 "Elle reconnaît les chiffres mais les contextualise",
 "Elle conteste les données statistiques présentées"],
"C — Elle reconnaît les chiffres mais les contextualise",
"<strong>voilà le vrai niveau B2.</strong> Aucune phrase ne donne la réponse : il faut suivre le "
"mouvement argumentatif. Elle cite les chiffres, puis « je voudrais apporter un éclairage plus "
"nuancé », puis « cependant ». Elle ne rejette rien et ne valide rien : elle contextualise.") + """

<h2 id="saut">Ce qui change vraiment entre B1 et B2</h2>

<p>Comparez les exercices 1-2 et 3-4 : la difficulté ne vient pas du vocabulaire, elle vient de la
<strong>nature de la question</strong>.</p>

<div class="tablewrap">
<table>
<caption>Ce que la question vous demande, selon le niveau.</caption>
<thead><tr><th></th><th>Questions B1</th><th>Questions B2</th></tr></thead>
<tbody>
<tr><td>Ce qu'on cherche</td><td>Une information <strong>dite</strong></td><td>Une <strong>attitude</strong>, une intention, un point de vue</td></tr>
<tr><td>Où est la réponse</td><td>Dans une phrase du document</td><td><strong>Nulle part</strong> — elle se déduit</td></tr>
<tr><td>Le piège</td><td>Un chiffre voisin, un mot proche</td><td>Une reformulation plausible mais trop tranchée</td></tr>
<tr><td>Ce qu'il faut suivre</td><td>Le contenu</td><td>Les <strong>connecteurs</strong> : mais, cependant, pourtant</td></tr>
</tbody>
</table>
</div>

<p>La conséquence est directe : au B2, ce sont les <strong>mots de liaison qui portent la
réponse</strong>. « Je voudrais apporter un éclairage plus nuancé » vaut plus que trois phrases de
contenu. Un candidat qui écoute les informations sans écouter l'articulation plafonne autour de
NCLC 6, quelle que soit la richesse de son vocabulaire.</p>

<h2 id="methode">La méthode pour ne pas décrocher</h2>

<ol>
<li><strong>Lisez les propositions avant l'audio</strong> quand le temps le permet. Vous saurez
alors quoi guetter — un chiffre, un lieu, une opinion — au lieu d'essayer de tout retenir.</li>
<li><strong>Abandonnez immédiatement une question perdue.</strong> C'est la règle la plus
importante et la plus difficile à appliquer. Une seule écoute signifie qu'une question manquée
est <em>définitivement</em> perdue : s'y accrocher fait manquer la suivante, puis la troisième.
Un décrochage en cascade coûte cinq questions, pas une.</li>
<li><strong>Notez qui parle</strong> dès qu'il y a plus de deux voix. Les questions B2 portent
souvent sur l'attribution d'un propos, comme dans l'exercice 3.</li>
<li><strong>Ne cherchez pas la certitude sur les dernières questions.</strong> Elles sont de
niveau C1-C2 et valent leur poids dans le calcul, mais elles ne valent pas trois questions B1
laissées sans réponse.</li>
<li><strong>Répondez toujours.</strong> Il n'y a pas de point négatif : une case vide vaut zéro,
une case cochée au hasard vaut une chance sur quatre.</li>
</ol>

<div class="note">
<p><strong>Le nombre d'items affichés peut vous surprendre.</strong> En passation informatisée,
France Éducation international ajoute des items qui n'entrent pas dans le calcul de votre score :
ils servent à ses analyses de validité. Voir l'épreuve s'allonger par rapport aux 39 annoncés est
normal et ne présage rien de votre résultat.</p>
</div>

<h2 id="erreurs">Les erreurs qui coûtent le plus</h2>

<ul>
<li><strong>Vouloir tout comprendre.</strong> L'objectif n'est pas de comprendre le document, c'est
de répondre à la question posée. Beaucoup d'informations sont là pour occuper l'attention.</li>
<li><strong>Choisir la proposition la plus tranchée.</strong> Aux questions d'attitude, les
options extrêmes — « accepte complètement », « conteste » — sont presque toujours fausses. Le
locuteur nuance : la bonne réponse nuance aussi.</li>
<li><strong>S'entraîner sur des ressources DELF.</strong> Au DELF, les documents des niveaux A1 à
B1 sont diffusés <strong>deux fois</strong>. Au TCF, jamais. Un candidat entraîné en double écoute
découvre la règle le jour de l'examen — voir notre comparatif
<a href="/blog/diplome-ou-test-delf-tcf/">diplôme ou test</a>.</li>
<li><strong>Confondre les déclinaisons.</strong> Le TCF Tout Public a 29 questions en 25 minutes,
le TCF Canada 39 en 35. S'entraîner sur la mauvaise version, c'est se préparer à un autre rythme.</li>
</ul>
""",
"cta_h2": "39 questions, une seule écoute : ça se répète",
"cta_p": """Des centaines d'exercices de compréhension orale au format exact du TCF Canada, audio
en une seule écoute et chronomètre réel, avec explication détaillée après chaque réponse et
conversion NCLC automatique par épreuve — dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Combien de questions y a-t-il en compréhension orale au TCF Canada ?",
 """39 questions à choix multiples, en 35 minutes, soit environ 54 secondes par question — audio,
lecture des quatre propositions et choix compris. La difficulté est progressive, de A1 à C2 : vous
n'êtes pas censé tout réussir."""),
("Peut-on réécouter un enregistrement au TCF Canada ?",
 """Non. Chaque document n'est diffusé qu'une seule fois et il n'y a aucun retour arrière possible.
C'est une différence majeure avec le DELF, où les documents des niveaux A1 à B1 sont diffusés deux
fois : beaucoup de candidats entraînés sur des ressources DELF découvrent cette règle le jour de
l'examen."""),
("Que faire si je manque une question ?",
 """Passez immédiatement à la suivante. Une question manquée est définitivement perdue puisqu'il n'y
a qu'une écoute — s'y accrocher fait manquer la suivante, puis la troisième. Un décrochage en
cascade coûte cinq questions au lieu d'une."""),
("Quel score faut-il en compréhension orale pour NCLC 7 ?",
 """458 sur 699. Attention à la confusion la plus coûteuse du TCF Canada : la bande B2 commence à
400, alors que NCLC 7 commence à 458. Un score de 430 est étiqueté B2 sur votre attestation mais ne
vaut que NCLC 6."""),
("Qu'est-ce qui distingue une question B1 d'une question B2 ?",
 """La nature de ce qu'on cherche. Au B1, la réponse est dite textuellement dans le document : c'est
du repérage. Au B2, elle ne figure nulle part et se déduit du mouvement argumentatif — ce sont les
connecteurs comme « mais », « cependant », « pourtant » qui portent la réponse."""),
("Faut-il répondre au hasard quand on ne sait pas ?",
 """Oui. Il n'y a pas de point négatif au TCF : une case vide vaut zéro, une case cochée au hasard
vaut une chance sur quatre. Ne laissez jamais de question sans réponse, surtout sur les dernières,
de niveau C1-C2."""),
],
"also": [
("/blog/exercices-comprehension-ecrite-tcf-canada/", "Exercices de compréhension écrite TCF Canada",
 "L'autre épreuve à 39 QCM, mais en 60 minutes et avec navigation libre."),
("/tcf-canada/", "TCF Canada : format, scores NCLC et préparation",
 "Le guide complet des quatre épreuves, de la notation et de l'inscription."),
("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement",
 "458 en compréhension orale — et pourquoi un « B2 » ne vaut pas toujours NCLC 7."),
("/examens-blancs/", "Examens blancs au format officiel",
 "Le protocole de passation pour que votre score d'entraînement veuille dire quelque chose."),
],
"sources": """<strong>Les formats évoluent.</strong> Cette page est à jour au 7 août 2026. Les
exercices présentés sont des contenus originaux de notre application, conçus au format officiel —
il n'existe aucune annale officielle du TCF en accès libre. Vérifiez la structure en vigueur sur
<a href="https://www.france-education-international.fr/test/tcf-canada" target="_blank" rel="noopener">france-education-international.fr</a>
avant votre session.""",
},

# ═══════════════════════════════════════════ 2. COMPRÉHENSION ÉCRITE
{
"slug": "exercices-comprehension-ecrite-tcf-canada",
"title": "Exercices de compréhension écrite TCF Canada",
"desc": "39 questions en 60 minutes avec navigation libre : 4 exercices corrigés du B1 au B2, la gestion du temps et les pièges de reformulation à repérer.",
"og_title": "Exercices de compréhension écrite TCF Canada",
"og_desc": "39 questions en 60 minutes, navigation libre. 4 exercices corrigés du B1 au B2 et les pièges de reformulation.",
"crumb": "Exercices de compréhension écrite",
"h1": "Exercices de compréhension écrite du TCF Canada, corrigés",
"date_fr": "7 août 2026",
"read": 8,
"accent": "accent-tcf",
"intro": """<strong>39 questions en 60 minutes</strong>, soit <strong>1 minute 32 par
question</strong> — et, contrairement à la compréhension orale, une <strong>navigation
libre</strong> entre les questions. C'est l'épreuve la plus confortable du TCF Canada, et donc
celle où il faut aller chercher des points. Quatre exercices corrigés, du B1 au B2.""",
"facts": [
"<strong>39 QCM à 4 choix · 60 minutes</strong> — environ <strong>1 min 32 par question</strong>.",
"<strong>Navigation libre</strong> : vous pouvez revenir en arrière, contrairement à l'oral.",
"Difficulté <strong>progressive A1 → C2</strong>.",
"Documents : annonces, articles de presse, textes d'idées, courriers.",
"Le saut B1 → B2 se joue sur l'<strong>intention de l'auteur</strong>, pas sur l'information.",
"<strong>NCLC 7</strong> commence à <strong>453</strong> sur 699 en compréhension écrite.",
],
"toc": [
("format", "Le format de l'épreuve"),
("exercices", "Quatre exercices corrigés"),
("temps", "Ce que la navigation libre change"),
("pieges", "Les quatre pièges de reformulation"),
("methode", "La méthode"),
],
"body": """
<h2 id="format">Le format de l'épreuve</h2>

<div class="tablewrap">
<table>
<caption>Compréhension écrite du TCF Canada. Source : France Éducation international, structure vérifiée en juillet 2026.</caption>
<thead><tr><th>Paramètre</th><th>Valeur</th></tr></thead>
<tbody>
<tr><td>Questions</td><td><strong>39 QCM</strong> à 4 choix</td></tr>
<tr><td>Durée</td><td><strong>60 minutes</strong></td></tr>
<tr><td>Temps moyen par question</td><td><strong>≈ 1 min 32</strong></td></tr>
<tr><td>Navigation</td><td><strong>libre</strong> — retour arrière possible</td></tr>
<tr><td>Difficulté</td><td>progressive, de A1 à C2</td></tr>
<tr><td>Notation</td><td>de 100 à 699 → <a href="/blog/tcf-canada-nclc-7/">NCLC</a></td></tr>
</tbody>
</table>
</div>

<p>Une minute trente par question paraît confortable, et ça l'est — <strong>à condition de ne pas
relire</strong>. Les documents s'allongent au fil de l'épreuve : une annonce de cinq lignes au
début, un texte d'idées de plusieurs paragraphes à la fin. Le temps se consomme sur les derniers
documents, pas sur les premiers.</p>

<h2 id="exercices">Quatre exercices corrigés</h2>

<p>Comme pour l'oral, la progression ci-dessous est celle de l'épreuve réelle : deux documents de
niveau B1, puis deux de niveau B2. Chronométrez-vous à 1 min 30 par question.</p>

""" + exo(1, "B1", "Document — article informatif :",
"« La laïcité est un principe fondamental de la République française, inscrit dans la Constitution "
"depuis 1958. Ce principe garantit la liberté de conscience et la liberté de religion pour tous "
"les citoyens. L'État ne reconnaît, ne salarie ni ne subventionne aucun culte, conformément à la "
"loi de séparation des Églises et de l'État de 1905. Contrairement à certaines idées reçues, la "
"laïcité n'est pas dirigée contre les religions. Elle vise au contraire à garantir à chacun le "
"droit de croire ou de ne pas croire. »",
"Selon le texte, que garantit la laïcité ?",
["L'obligation d'être athée pour tous", "La suprématie d'une religion étatique",
 "La liberté de conscience religieuse", "L'interdiction de toutes les religions"],
"C — La liberté de conscience religieuse",
"le texte l'énonce directement : « garantit la liberté de conscience et la liberté de religion ». "
"Les trois autres options sont des <strong>contresens classiques</strong> sur la laïcité, que le "
"texte prend explicitement soin de désamorcer.") + exo(
2, "B1", "Document — article informatif :",
"« Le fonctionnement est simple : lorsqu'un assuré consulte un médecin ou achète des médicaments, "
"la Sécurité sociale rembourse une partie des frais. Pour le reste, appelé le <em>ticket "
"modérateur</em>, la plupart des Français souscrivent une mutuelle ou complémentaire santé. Le "
"médecin traitant joue un rôle central dans ce système. Chaque assuré de plus de 16 ans doit "
"déclarer un médecin traitant auprès de sa caisse d'assurance maladie. »",
"Qu'est-ce que le ticket modérateur ?",
["Le salaire net du médecin traitant", "Le prix total de la consultation",
 "La part non remboursée par la Sécurité sociale", "Le coût annuel de la carte Vitale"],
"C — La part non remboursée par la Sécurité sociale",
"le texte définit le terme par apposition : « Pour le reste, appelé le ticket modérateur ». "
"C'est un exercice de <strong>lecture de définition en contexte</strong> — très fréquent au TCF, "
"et payant : la réponse est toujours dans la phrase qui contient le terme.") + exo(
3, "B2", "Document — article d'opinion :",
"« L'idée que la France serait un pays foncièrement hostile à l'immigration est un cliché qui "
"mérite d'être nuancé. Si les débats publics sur l'immigration sont souvent virulents et "
"passionnés, la réalité du terrain est bien plus complexe qu'un simple rejet. Historiquement, la "
"France est une terre d'immigration depuis la fin du XIX<sup>e</sup> siècle. Des vagues "
"successives de migrants italiens, polonais, espagnols, portugais, puis maghrébins et "
"subsahariens ont contribué à façonner la société française d'aujourd'hui. »",
"L'idée que la France est hostile à l'immigration est, selon l'auteur :",
["Parfaitement exacte aujourd'hui", "Entièrement fausse en réalité",
 "Un cliché à nuancer largement", "Une invention des médias actuels"],
"C — Un cliché à nuancer largement",
"le piège est l'option B. L'auteur ne dit <em>pas</em> que l'idée est fausse : il dit qu'elle "
"« mérite d'être nuancé ». <strong>Nuancer n'est pas réfuter.</strong> C'est le piège de "
"reformulation le plus fréquent au niveau B2 — une option correcte mais trop tranchée.") + exo(
4, "B2", "Document — article d'opinion :",
"« Il est tentant de croire que la langue française est un bloc monolithique, un monument immuable "
"dont l'Académie française serait la gardienne infaillible. La réalité est tout autre. Le français "
"est une langue vivante, en perpétuelle évolution, qui s'enrichit constamment de mots nouveaux, "
"d'emprunts et de créations. Chaque année, les dictionnaires accueillent des centaines de mots "
"nouveaux. »",
"Quelle est la vision courante du français que l'auteur conteste ?",
["Le français devrait bannir complètement tous les emprunts étrangers",
 "Le français provient exclusivement de l'anglais et des emprunts étrangers",
 "Le français est un bloc monolithique défendu par l'Académie française",
 "Le français est une langue morte et disparue comme le latin"],
"C — Le français est un bloc monolithique défendu par l'Académie française",
"la question ne demande pas la thèse de l'auteur mais <strong>la thèse qu'il combat</strong>. "
"C'est une question d'architecture argumentative : « Il est tentant de croire que… La réalité est "
"tout autre. » Beaucoup de candidats répondent avec la position de l'auteur et se trompent.") + """

<h2 id="temps">Ce que la navigation libre change</h2>

<p>C'est l'atout de cette épreuve, et il est sous-exploité. Vous pouvez <strong>revenir en
arrière</strong> — donc adopter une stratégie que l'oral interdit.</p>

<ol>
<li><strong>Premier passage rapide.</strong> Traitez toutes les questions dont la réponse est
immédiate, sans forcer. Vous sécurisez ainsi l'essentiel des points en une trentaine de minutes.</li>
<li><strong>Marquez les questions douteuses</strong> au lieu de vous y enliser. Une question B2
qui résiste trente secondes en résistera trois minutes.</li>
<li><strong>Second passage</strong> sur les questions marquées, avec le temps restant et l'esprit
plus clair.</li>
<li><strong>Dernières minutes : remplissez tout.</strong> Aucune case ne doit rester vide, il n'y
a pas de point négatif.</li>
</ol>

<div class="note">
<p><strong>Ne relisez pas les documents entiers.</strong> C'est le réflexe qui consomme le temps.
Une question porte sur un passage précis : retrouvez le passage, pas le texte. Les mots de la
question vous y conduisent presque toujours.</p>
</div>

<h2 id="pieges">Les quatre pièges de reformulation</h2>

<p>Au niveau B2, les mauvaises réponses ne sont pas fausses au hasard : elles sont
<strong>construites</strong> selon quatre schémas récurrents.</p>

<div class="tablewrap">
<table>
<caption>Comment sont fabriquées les mauvaises réponses.</caption>
<thead><tr><th>Piège</th><th>À quoi ça ressemble</th><th>Comment le repérer</th></tr></thead>
<tbody>
<tr><td><strong>Trop tranché</strong></td><td>« entièrement faux » quand le texte dit « à nuancer »</td><td>Cherchez les absolus : totalement, jamais, exclusivement</td></tr>
<tr><td><strong>Vrai mais hors sujet</strong></td><td>Une information exacte du texte, qui ne répond pas à la question</td><td>Relisez la question, pas le texte</td></tr>
<tr><td><strong>Inversion de rôle</strong></td><td>La thèse de l'auteur donnée comme la thèse qu'il combat</td><td>Repérez « il est tentant de croire », « contrairement à »</td></tr>
<tr><td><strong>Mot-crochet</strong></td><td>Reprend un mot rare du texte pour attirer l'œil</td><td>Un mot identique n'est pas un argument</td></tr>
</tbody>
</table>
</div>

<h2 id="methode">La méthode</h2>

<ul>
<li><strong>Lisez la question avant le document</strong> pour les textes longs. Vous saurez ce que
vous cherchez et éviterez la lecture intégrale.</li>
<li><strong>Sur les questions d'opinion, cherchez les connecteurs d'opposition</strong> — mais,
pourtant, contrairement à, il est tentant de croire. Ils marquent l'endroit exact où l'auteur
prend position.</li>
<li><strong>Méfiez-vous des options qui reprennent les mots du texte.</strong> C'est souvent le
signe d'un mot-crochet, pas d'une bonne réponse.</li>
<li><strong>Gardez dix minutes</strong> pour le second passage et le remplissage final.</li>
<li><strong>Entraînez-vous sur la bonne déclinaison.</strong> Le TCF Tout Public a 29 questions en
45 minutes et une section <a href="/blog/exercices-structures-langue-tcf/">« structures de la
langue »</a> que le TCF Canada ne comporte pas. Le protocole complet de passation est sur notre
page <a href="/examens-blancs/">examens blancs</a>.</li>
</ul>
""",
"cta_h2": "1 min 32 par question, ça se chronomètre",
"cta_p": """Des centaines d'exercices de compréhension écrite au format exact du TCF Canada,
chronomètre réel et navigation libre comme le jour J, avec explication détaillée après chaque
réponse et conversion NCLC par épreuve — dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Combien de questions en compréhension écrite au TCF Canada ?",
 """39 questions à choix multiples en 60 minutes, soit environ 1 minute 32 par question. La
navigation est libre : contrairement à la compréhension orale, vous pouvez revenir en arrière sur
les questions précédentes."""),
("Peut-on revenir en arrière pendant l'épreuve ?",
 """Oui, en compréhension écrite la navigation est libre. C'est l'atout de cette épreuve : faites un
premier passage rapide sur les questions immédiates, marquez les douteuses, puis revenez-y avec le
temps restant. En compréhension orale, au contraire, aucun retour n'est possible."""),
("Quel score faut-il en compréhension écrite pour NCLC 7 ?",
 """453 sur 699 — un seuil légèrement différent de celui de la compréhension orale, qui est à 458.
Attention : la bande B2 commence à 400, donc un score étiqueté B2 sur votre attestation ne garantit
pas NCLC 7."""),
("Comment sont fabriquées les mauvaises réponses ?",
 """Selon quatre schémas récurrents : une option trop tranchée quand le texte nuance, une
information vraie mais qui ne répond pas à la question, une inversion entre la thèse de l'auteur et
celle qu'il combat, et le mot-crochet qui reprend un terme rare du texte pour attirer l'œil."""),
("Faut-il lire le document en entier ?",
 """Pas sur les textes longs. Lisez d'abord la question, puis retrouvez le passage concerné : les
mots de la question y conduisent presque toujours. Relire les documents entiers est le réflexe qui
consomme le temps sans rapporter de points."""),
("Combien de temps garder pour la fin ?",
 """Une dizaine de minutes. Elles servent au second passage sur les questions marquées et au
remplissage final : aucune case ne doit rester vide, puisqu'il n'y a pas de point négatif au
TCF."""),
],
"also": [
("/blog/exercices-comprehension-orale-tcf-canada/", "Exercices de compréhension orale TCF Canada",
 "L'épreuve sœur, en 35 minutes et avec une seule écoute."),
("/blog/sujets-expression-ecrite-tcf-canada/", "Expression écrite TCF Canada : les 3 sujets types",
 "Les trois tâches, leurs fenêtres de mots et un sujet corrigé pour chacune."),
("/tcf-canada/", "TCF Canada : format, scores NCLC et préparation",
 "Le guide complet des quatre épreuves et de la conversion NCLC."),
("/blog/examen-blanc-tcf-gratuit/", "Examen blanc TCF gratuit : les vraies ressources",
 "Les deux seules ressources gratuites officielles, et ce qu'elles ne couvrent pas."),
],
"sources": """<strong>Les formats évoluent.</strong> Cette page est à jour au 7 août 2026. Les
exercices présentés sont des contenus originaux de notre application, conçus au format officiel —
il n'existe aucune annale officielle du TCF en accès libre. Vérifiez la structure en vigueur sur
<a href="https://www.france-education-international.fr/test/tcf-canada" target="_blank" rel="noopener">france-education-international.fr</a>
avant votre session.""",
},

]

if __name__ == "__main__":
    print("Exercices TCF Canada — CO et CE :")
    build(ARTICLES)
