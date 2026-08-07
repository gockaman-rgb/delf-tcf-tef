#!/usr/bin/env python3
"""Articles 8 à 10. Formats issus d'EXAM_SPECS_AUDIT_2026.md (recoupé FEI/CCIP) ;
exigences québécoises reprises des articles publiés et sourcés du site."""

from article_template import build

ARTICLES = [

# ─────────────────────────────────────────────────────────────────────────────
{
"slug": "production-ecrite-delf-b2",
"title": "Production écrite DELF B2 : la méthode en 250 mots",
"desc": "Un exercice, 60 minutes, 250 mots minimum. Ce que le correcteur évalue vraiment, le plan qui fonctionne et les erreurs qui coûtent le plus de points.",
"og_title": "Production écrite DELF B2 : la méthode en 250 mots",
"og_desc": "Un exercice, 60 minutes, 250 mots minimum. Ce que le correcteur évalue vraiment, le plan qui fonctionne et les erreurs qui coûtent le plus cher.",
"crumb": "Production écrite DELF B2",
"h1": "Production écrite du DELF B2 : la méthode, épreuve la plus discriminante",
"date_fr": "7 août 2026",
"read": 7,
"accent": "accent-delf",
"intro": """<strong>Un exercice, 60 minutes, 250 mots minimum.</strong> C'est l'épreuve où l'écart
entre un bon niveau de langue et une bonne note est le plus grand — parce que le correcteur
n'évalue pas votre français, il évalue votre <strong>capacité à construire une position</strong>.
Et cela s'apprend beaucoup plus vite qu'un niveau de langue.""",
"facts": [
"<strong>1 exercice · 60 minutes · 250 mots minimum</strong>, noté sur <strong>25</strong>.",
"Trois genres possibles : <strong>contribution à un débat, lettre formelle, article critique</strong>.",
"⚠️ Une note sous <strong>5/25</strong> est <strong>éliminatoire</strong>, quelle que soit votre moyenne.",
"250 mots est un <strong>plancher</strong>, pas une cible : en dessous, la consigne n'est pas respectée.",
"Le correcteur évalue la <strong>construction</strong>, pas votre opinion.",
"Depuis la réforme, c'est la <strong>seule épreuve rédigée</strong> : les compréhensions sont 100 % QCM.",
],
"toc": [
("format", "Le format exact"),
("evalue", "Ce que le correcteur évalue vraiment"),
("plan", "Le plan qui fonctionne"),
("genres", "Les trois genres, et ce qu'ils imposent"),
("erreurs", "Les cinq erreurs qui coûtent le plus"),
("chrono", "Comment répartir les 60 minutes"),
],
"body": """
<h2 id="format">Le format exact</h2>

<p>La production écrite est la troisième épreuve collective du <a href="/delf-b2/">DELF B2</a>,
juste après les deux compréhensions. Vous arrivez donc dessus après une heure et demie
d'examen — un détail qui compte pour la gestion de l'énergie.</p>

<div class="tablewrap">
<table>
<caption>La production écrite dans l'ensemble du DELF B2. Source : France Éducation international, format issu de la réforme 2020, généralisé en septembre 2024.</caption>
<thead><tr><th>Épreuve</th><th>Durée</th><th>Note</th></tr></thead>
<tbody>
<tr><td>Compréhension de l'oral</td><td>30 min</td><td>/25</td></tr>
<tr><td>Compréhension des écrits</td><td>60 min</td><td>/25</td></tr>
<tr><td><strong>Production écrite</strong></td><td><strong>60 min</strong></td><td><strong>/25</strong></td></tr>
<tr><td>Production orale</td><td>20 min <em>(+ 30 min de préparation)</em></td><td>/25</td></tr>
</tbody>
</table>
</div>

<p>Depuis la réforme, les deux compréhensions sont passées en <strong>QCM intégral</strong> : les
questions ouvertes et les vrai/faux avec justification ont disparu. La production écrite est donc
devenue <strong>la seule épreuve où vous rédigez</strong> avant l'oral. Tout ce qui relève de
l'expression écrite se joue là, sur une seule copie.</p>

<h2 id="evalue">Ce que le correcteur évalue vraiment</h2>

<p>C'est le malentendu central. Le sujet vous demande une <strong>prise de position
personnelle</strong>, et beaucoup de candidats en concluent qu'on juge la pertinence de leur avis.
Ce n'est pas le cas : <strong>votre opinion n'est ni bonne ni mauvaise</strong>. Ce qui est évalué,
c'est la manière dont vous la construisez.</p>

<p>Concrètement, cinq dimensions :</p>

<ul>
<li><strong>Le respect de la consigne et du genre.</strong> Une lettre formelle sans formule
d'appel ni structure de lettre perd des points avant même la première phrase évaluée sur la
langue. C'est le point le plus facile à sécuriser, et le plus souvent négligé.</li>
<li><strong>La structure argumentative.</strong> Une position claire, des arguments hiérarchisés,
et surtout la <strong>prise en compte de l'objection adverse</strong>. C'est le marqueur du niveau
B2 : au B1, on donne son avis ; au B2, on le défend contre une objection.</li>
<li><strong>Les connecteurs logiques.</strong> Le signal le plus visible du niveau, et le plus
rentable à travailler mécaniquement — quelques heures suffisent à en installer un répertoire
solide.</li>
<li><strong>Le registre.</strong> Le glissement inaperçu vers le familier est une perte de points
fréquente chez les candidats qui parlent bien français au quotidien.</li>
<li><strong>Le volume.</strong> 250 mots minimum. En dessous, la conformité à la consigne est
prise en défaut, quelle que soit la qualité de la langue.</li>
</ul>

<div class="note">
<p><strong>Aucune de ces cinq dimensions n'est un problème de vocabulaire.</strong> C'est la bonne
nouvelle de cette épreuve : l'essentiel des points perdus vient du plan, du genre et de la
consigne — c'est-à-dire de choses qui se corrigent en quelques séances, pas en quelques mois.</p>
</div>

<h2 id="plan">Le plan qui fonctionne</h2>

<p>Il n'existe pas de plan officiel imposé. Mais une structure remplit toutes les attentes du
niveau B2 et vous évite de réfléchir à l'organisation le jour J.</p>

<ol>
<li><strong>Introduction (30-40 mots).</strong> Vous reformulez l'enjeu et vous annoncez votre
position. Pas de suspense : au B2, le correcteur doit savoir dès la première phrase où vous
allez.</li>
<li><strong>Premier argument (60-70 mots).</strong> Votre raison la plus forte, illustrée par un
exemple concret. Un argument sans exemple reste une affirmation.</li>
<li><strong>Deuxième argument (60-70 mots).</strong> Une raison d'une autre nature que la
première — si le premier est économique, prenez un angle social ou pratique. Deux arguments du
même type comptent pour un.</li>
<li><strong>Concession et réfutation (50-60 mots).</strong> <strong>C'est le paragraphe qui fait
la différence.</strong> Vous reconnaissez la force de l'objection adverse, puis vous expliquez
pourquoi elle ne renverse pas votre position. Beaucoup de copies l'omettent entièrement — et
plafonnent.</li>
<li><strong>Conclusion (30-40 mots).</strong> Vous rappelez votre position et vous ouvrez, sans
introduire d'idée neuve.</li>
</ol>

<p>Total : environ 250 à 280 mots. Le plan produit mécaniquement le volume attendu, ce qui règle
la question du décompte.</p>

<h2 id="genres">Les trois genres, et ce qu'ils imposent</h2>

<div class="tablewrap">
<table>
<caption>Ce que chaque genre exige en plus de l'argumentation.</caption>
<thead><tr><th>Genre</th><th>Ce qu'il impose</th></tr></thead>
<tbody>
<tr><td><strong>Contribution à un débat</strong><br><em>forum, courrier des lecteurs</em></td><td>S'adresser à une communauté, situer sa parole dans un échange en cours</td></tr>
<tr><td><strong>Lettre formelle</strong></td><td>Formule d'appel, objet, structure de lettre, formule de politesse finale, registre soutenu tenu de bout en bout</td></tr>
<tr><td><strong>Article critique</strong></td><td>Un titre, une accroche, un ton journalistique — et une position assumée</td></tr>
</tbody>
</table>
</div>

<p>La lettre formelle est celle où l'on perd le plus de points gratuitement, parce que ses
conventions sont vérifiables mécaniquement par le correcteur. Apprenez-les une fois : formule
d'appel, objet, corps structuré, formule de politesse. Ces éléments sont acquis à vie et se
présentent dans à peu près tous les examens de français.</p>

<h2 id="erreurs">Les cinq erreurs qui coûtent le plus</h2>

<ol>
<li><strong>Écrire moins de 250 mots.</strong> La sanction porte sur le respect de la consigne,
indépendamment de la qualité. Comptez vos mots, réellement — l'estimation à l'œil est presque
toujours optimiste.</li>
<li><strong>Omettre la concession.</strong> Sans prise en compte de l'objection adverse, votre
copie reste une opinion juxtaposée, pas une argumentation de niveau B2.</li>
<li><strong>Ignorer le genre demandé.</strong> Un excellent texte argumentatif qui devait être une
lettre formelle perd des points structurels irrécupérables.</li>
<li><strong>Accumuler des arguments sans les articuler.</strong> Trois idées justes mais posées
côte à côte valent moins que deux idées reliées par une progression explicite.</li>
<li><strong>Négliger la relecture.</strong> Les accords, les temps et la ponctuation se corrigent
en cinq minutes et se paient cher s'ils restent.</li>
</ol>

<h2 id="chrono">Comment répartir les 60 minutes</h2>

<div class="tablewrap">
<table>
<caption>Une répartition qui laisse une vraie relecture.</caption>
<thead><tr><th>Temps</th><th>Ce que vous faites</th></tr></thead>
<tbody>
<tr><td><strong>0–10 min</strong></td><td>Analyser la consigne, identifier le genre, poser le plan et les deux arguments avec leurs exemples</td></tr>
<tr><td><strong>10–45 min</strong></td><td>Rédiger d'une traite, sans revenir en arrière</td></tr>
<tr><td><strong>45–52 min</strong></td><td>Compter les mots, vérifier que la concession est présente et que le genre est respecté</td></tr>
<tr><td><strong>52–60 min</strong></td><td>Relire pour la langue : accords, temps, ponctuation, registre</td></tr>
</tbody>
</table>
</div>

<p>Les dix premières minutes sont contre-intuitives : on a l'impression de perdre du temps.
C'est pourtant le seul moment où l'on peut encore changer la structure de sa copie sans tout
réécrire. Un plan posé en dix minutes fait gagner bien plus que dix minutes de rédaction.</p>

<div class="note">
<p><strong>Pourquoi cette épreuve est difficile à préparer seul.</strong> Vous ne pouvez pas juger
si votre concession est réelle ou seulement annoncée, ni si votre registre a glissé — ce sont
précisément les défauts invisibles de l'intérieur. Et l'écart entre 9 et 13 sur 25, qui décide
souvent de l'admission, ne se voit pas à la relecture. C'est ce que règle
<a href="/correction-ia/">une correction sur les critères officiels</a>.</p>
</div>
""",
"cta_h2": "Savoir si votre copie vaut 9 ou 13 sur 25",
"cta_p": """Sujets originaux au format DELF B2, chronomètre réel, et correction IA de votre
production écrite sur les critères officiels : respect de la consigne, cohérence, structure
argumentative, lexique, grammaire. Un feedback détaillé après chaque essai, autant de fois que
nécessaire — dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Combien de mots faut-il écrire à la production écrite du DELF B2 ?",
 """250 mots minimum, en un seul exercice, en 60 minutes. C'est un plancher et non une cible :
écrire en dessous fait perdre des points sur le respect de la consigne, quelle que soit la qualité
de la langue. Un plan en cinq parties produit mécaniquement 250 à 280 mots."""),
("Quels types de sujets tombent ?",
 """Trois genres : une contribution à un débat (forum, courrier des lecteurs), une lettre formelle,
ou un article critique. Dans tous les cas, le sujet demande une prise de position personnelle
argumentée. La lettre formelle est celle où l'on perd le plus de points gratuitement, faute d'en
respecter les conventions."""),
("Le correcteur juge-t-il mon opinion ?",
 """Non. Votre opinion n'est ni bonne ni mauvaise : ce qui est évalué, c'est la façon dont vous la
construisez — respect de la consigne et du genre, structure argumentative, connecteurs logiques,
registre et volume. Aucune de ces dimensions n'est un problème de vocabulaire."""),
("Qu'est-ce qui distingue le B2 du B1 à l'écrit ?",
 """La prise en compte de l'objection adverse. Au B1, on donne son avis ; au B2, on le défend
contre une objection qu'on a d'abord reconnue. C'est le paragraphe de concession et réfutation qui
fait le plus souvent la différence — et beaucoup de copies l'omettent entièrement."""),
("Quelle note faut-il à la production écrite ?",
 """Il n'y a pas de note minimale par épreuve au DELF, à une exception près : une note inférieure à
5 sur 25 est éliminatoire, quelle que soit votre moyenne générale. L'admission se joue à 50 sur
100 au total, les quatre épreuves étant notées sur 25 chacune."""),
("Comment répartir les 60 minutes ?",
 """Environ 10 minutes pour analyser la consigne et poser le plan, 35 minutes pour rédiger d'une
traite, 7 minutes pour vérifier le volume, la concession et le genre, et 8 minutes de relecture
sur la langue. Les 10 premières minutes semblent perdues : c'est pourtant le seul moment où l'on
peut encore changer la structure sans tout réécrire."""),
],
"also": [
("/delf-b2/", "DELF B2 : épreuves, barème et méthode pour réussir",
 "Le format complet des quatre épreuves, le barème et la note éliminatoire."),
("/blog/synthese-dalf-c1/", "La synthèse du DALF C1 : méthode pas à pas",
 "Le cran au-dessus : réduire plusieurs documents en un texte objectif de 200 à 240 mots."),
("/correction-ia/", "La correction IA de l'écrit et de l'oral",
 "Comment vos productions sont évaluées sur les critères officiels."),
("/examens-blancs/", "Examens blancs au format officiel",
 "Le protocole de passation pour s'entraîner en conditions réelles."),
],
"sources": """<strong>Les formats évoluent.</strong> Cette page est à jour au 7 août 2026 et décrit
le format issu de la réforme 2020, pleinement généralisé depuis septembre 2024. Attention aux
annales et tutoriels antérieurs, qui décrivent un examen différent. Vérifiez le format en vigueur
sur
<a href="https://www.france-education-international.fr/diplome/delf-tout-public" target="_blank" rel="noopener">france-education-international.fr</a>
avant votre session.""",
},

# ─────────────────────────────────────────────────────────────────────────────
{
"slug": "synthese-dalf-c1",
"title": "La synthèse du DALF C1 : méthode pas à pas",
"desc": "200 à 240 mots, aucune citation, aucun avis personnel, et un plan qui croise les documents. La technique de l'épreuve reine du DALF C1, étape par étape.",
"og_title": "La synthèse du DALF C1 : méthode pas à pas",
"og_desc": "200 à 240 mots, aucune citation, aucun avis personnel, un plan qui croise les documents. La technique de l'épreuve reine du C1.",
"crumb": "La synthèse du DALF C1",
"h1": "La synthèse de documents du DALF C1, pas à pas",
"date_fr": "7 août 2026",
"read": 7,
"accent": "accent-delf",
"intro": """Réduire plusieurs documents en un texte unique, <strong>objectif, entièrement
reformulé et calibré entre 200 et 240 mots</strong> : la synthèse ne s'improvise pas. Bonne
nouvelle — c'est une <strong>technique</strong>, pas un niveau de langue. Elle se maîtrise en une
dizaine d'entraînements sérieusement corrigés, là où un niveau met des mois à monter.""",
"facts": [
"<strong>200 à 240 mots</strong>, premier des deux exercices de la production écrite du DALF C1.",
"L'épreuve entière dure <strong>2 h 30</strong> : synthèse <em>puis</em> essai argumenté de 250 mots minimum.",
"⚠️ <strong>Aucune citation</strong> : tout doit être reformulé.",
"⚠️ <strong>Aucun avis personnel</strong> : vous n'existez pas dans ce texte.",
"⚠️ Le plan doit <strong>croiser les documents</strong>, pas les résumer l'un après l'autre.",
"La bascule synthèse → essai est ce que les candidats ratent le plus.",
],
"toc": [
("place", "Où se situe la synthèse dans l'épreuve"),
("regles", "Les trois règles absolues"),
("plan", "Le plan croisé, vrai discriminant"),
("etapes", "La méthode en six étapes"),
("bascule", "La bascule vers l'essai"),
("erreurs", "Les erreurs typiques"),
],
"body": """
<h2 id="place">Où se situe la synthèse dans l'épreuve</h2>

<p>La production écrite du <a href="/dalf/">DALF C1</a> dure <strong>2 h 30</strong> et contient
<strong>deux exercices de nature opposée</strong>. C'est cette opposition qui fait sa difficulté,
bien plus que le niveau de langue exigé.</p>

<div class="tablewrap">
<table>
<caption>Les deux exercices de la production écrite du DALF C1. Source : France Éducation international, critères d'évaluation officiels.</caption>
<thead><tr><th>Exercice</th><th>Volume</th><th>Posture attendue</th></tr></thead>
<tbody>
<tr><td><strong>1. Synthèse de documents</strong></td><td>200 à 240 mots</td><td><strong>Neutralité totale</strong> — vous n'existez pas</td></tr>
<tr><td><strong>2. Essai argumenté</strong></td><td>250 mots minimum</td><td><strong>Position assumée</strong> — vous prenez parti</td></tr>
</tbody>
</table>
</div>

<p>Deux heures et demie, deux exercices, deux postures inverses. Beaucoup de candidats préparent
chacun séparément et découvrent le jour J que <strong>le vrai obstacle est le passage de l'un à
l'autre</strong>.</p>

<h2 id="regles">Les trois règles absolues</h2>

<p>Leur violation coûte plus cher que n'importe quelle faute de langue, parce qu'elles portent
sur la compétence même que l'exercice évalue.</p>

<ol>
<li><strong>Aucune citation.</strong> Tout doit être reformulé. Recopier même une expression
frappante du document original est sanctionné — reformuler <em>est</em> l'exercice.</li>
<li><strong>Aucun avis personnel.</strong> La synthèse est neutre de bout en bout. Pas de « il
semble que », pas de « on peut regretter », pas de conclusion qui tranche. L'essai qui suit est
là pour ça.</li>
<li><strong>Un plan qui croise les documents.</strong> Résumer le document 1, puis le 2, puis le
3 n'est pas une synthèse : c'est une suite de résumés. Il faut dégager les axes communs et faire
dialoguer les sources <em>à l'intérieur</em> de chaque partie.</li>
</ol>

<p>S'y ajoute la contrainte de volume — <strong>200 à 240 mots</strong> —, très courte pour la
matière à traiter. Le comptage fait partie de l'exercice, et dépasser franchement la borne haute
est pénalisé.</p>

<h2 id="plan">Le plan croisé, vrai discriminant</h2>

<div class="note">
<p><strong>C'est ici que se jouent les points.</strong> Un correcteur repère en dix secondes si
votre plan suit les documents ou s'il les croise : il suffit de regarder si vos paragraphes
portent des noms de documents ou des noms d'idées.</p>
</div>

<p>La différence, concrètement :</p>

<div class="tablewrap">
<table>
<caption>Deux organisations, un seul dossier de documents.</caption>
<thead><tr><th>Plan suiviste <em>(à éviter)</em></th><th>Plan croisé <em>(attendu)</em></th></tr></thead>
<tbody>
<tr><td>§1 — Ce que dit le document A</td><td>§1 — Premier axe : les partisans et leurs raisons <em>(A et C)</em></td></tr>
<tr><td>§2 — Ce que dit le document B</td><td>§2 — Deuxième axe : les objections <em>(B, nuancé par A)</em></td></tr>
<tr><td>§3 — Ce que dit le document C</td><td>§3 — Troisième axe : les points d'accord <em>(A, B et C)</em></td></tr>
</tbody>
</table>
</div>

<p>Le plan croisé oblige à <strong>lire les documents ensemble</strong> plutôt que l'un après
l'autre, et c'est bien la compétence visée : montrer que vous avez saisi le débat, pas seulement
compris chaque texte.</p>

<h2 id="etapes">La méthode en six étapes</h2>

<ol>
<li><strong>Lire les documents en repérant les positions</strong>, pas les informations. Notez en
marge, pour chacun : qui parle, quelle thèse, quel angle.</li>
<li><strong>Lister les idées, sans mentionner les documents.</strong> Une idée par ligne. À cette
étape, oubliez d'où elles viennent.</li>
<li><strong>Regrouper ces idées en deux ou trois axes.</strong> Ce sont vos futurs paragraphes.
Un axe qui ne contient qu'une idée n'est pas un axe.</li>
<li><strong>Vérifier que chaque axe convoque au moins deux documents.</strong> Si l'un de vos axes
ne s'appuie que sur une source, votre plan est encore suiviste.</li>
<li><strong>Rédiger sans jamais rouvrir les documents.</strong> C'est le meilleur moyen de ne pas
recopier : si vous ne relisez pas, vous ne pouvez pas citer.</li>
<li><strong>Compter, puis élaguer.</strong> Les premiers jets font 300 mots. Coupez les exemples
redondants et les formules d'annonce — pas les idées.</li>
</ol>

<div class="note">
<p><strong>L'astuce de l'étape 5.</strong> Rédiger documents fermés est la seule technique qui
garantit mécaniquement le respect de la première règle. Si vous avez besoin de rouvrir un texte
pour écrire une phrase, c'est que vous ne l'avez pas assimilé — et vous êtes sur le point de le
paraphraser de trop près.</p>
</div>

<h2 id="bascule">La bascule vers l'essai</h2>

<p>Une fois la synthèse rendue neutre, vous devez produire, dans la même épreuve, un
<strong>essai argumenté de 250 mots minimum</strong> où vous prenez position. Le changement de
posture est brutal, et c'est le point que les candidats ratent le plus.</p>

<p>Deux échecs symétriques :</p>

<ul>
<li><strong>La contamination de la synthèse par l'opinion.</strong> On a préparé un avis en lisant
les documents, il déborde dans la synthèse. Résultat : la neutralité est prise en défaut.</li>
<li><strong>L'essai qui reste neutre.</strong> On a tellement retenu son avis pendant la synthèse
qu'on écrit un second résumé. Résultat : l'essai n'argumente pas.</li>
</ul>

<p><strong>Entraînez toujours les deux exercices à la suite</strong>, dans les conditions réelles
des 2 h 30. C'est le seul moyen de travailler la bascule elle-même, qui n'existe pas quand on
prépare chaque exercice isolément.</p>

<h2 id="erreurs">Les erreurs typiques</h2>

<ul>
<li><strong>Introduire une idée absente des documents.</strong> Même juste, même pertinente : elle
n'a rien à faire dans une synthèse.</li>
<li><strong>Conserver la structure d'un document dominant.</strong> Le texte le plus long ou le
plus clair aspire souvent le plan. Vérifiez que vos axes ne sont pas simplement ses parties.</li>
<li><strong>Annoncer au lieu de synthétiser.</strong> « Le premier document aborde… » consomme des
mots sans transmettre d'idée — et vous n'en avez que 240.</li>
<li><strong>Dépasser largement le volume.</strong> La contrainte fait partie de l'évaluation : une
synthèse à 320 mots n'a pas fait le travail de réduction.</li>
<li><strong>Négliger la langue en croyant que seule la technique compte.</strong> Au C1, la
correction lexicale et syntaxique reste évaluée — la technique s'ajoute aux exigences, elle ne
les remplace pas.</li>
</ul>

<div class="note">
<p><strong>Pourquoi elle est difficile à préparer seul.</strong> Vous ne pouvez pas juger de votre
propre neutralité, ni voir que votre plan suit les documents au lieu de les croiser : ce sont
exactement les défauts invisibles de l'intérieur. C'est aussi le niveau où un correcteur humain
devient rare et cher.</p>
</div>
""",
"cta_h2": "Une technique se corrige, un niveau se travaille",
"cta_p": """Sujets de synthèse et d'essai au format DALF C1, chronomètre réel sur les 2 h 30, et
correction IA sur les critères officiels — neutralité, reformulation, structure, langue. Autant
d'essais que nécessaire pour installer la technique. Dans l'app
«&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Combien de mots fait la synthèse du DALF C1 ?",
 """200 à 240 mots. C'est très court pour la matière à traiter, et le comptage fait partie de
l'exercice : dépasser franchement la borne haute est pénalisé, parce que la réduction est
précisément la compétence évaluée. La synthèse est suivie d'un essai argumenté de 250 mots
minimum, dans la même épreuve de 2 h 30."""),
("Peut-on citer les documents dans une synthèse ?",
 """Non. Tout doit être reformulé, et recopier même une expression frappante du document original
est sanctionné : reformuler est l'exercice. La meilleure technique pour s'en garantir est de
rédiger sans jamais rouvrir les documents — si vous ne relisez pas, vous ne pouvez pas citer."""),
("Peut-on donner son avis dans la synthèse ?",
 """Non, jamais. La synthèse est neutre de bout en bout : pas de « il semble que », pas de « on
peut regretter », pas de conclusion qui tranche. L'essai argumenté qui suit dans la même épreuve
est là pour votre position — et c'est justement cette bascule que les candidats ratent le plus."""),
("Qu'est-ce qu'un plan croisé ?",
 """Un plan organisé par idées et non par documents. Résumer le document 1, puis le 2, puis le 3
n'est pas une synthèse mais une suite de résumés. Un plan croisé dégage deux ou trois axes
thématiques et fait dialoguer les sources à l'intérieur de chaque partie — vérifiez que chaque axe
convoque au moins deux documents."""),
("Combien de temps faut-il pour maîtriser la synthèse ?",
 """C'est une technique, pas un niveau de langue : une dizaine d'entraînements sérieusement
corrigés suffisent généralement à l'installer, là où un niveau de langue met des mois à monter.
C'est l'exercice au meilleur rendement de toute la préparation au DALF C1."""),
("Faut-il s'entraîner à la synthèse et à l'essai séparément ?",
 """Non, entraînez-les toujours à la suite, dans les conditions réelles des 2 h 30. Le vrai
obstacle n'est pas chaque exercice pris isolément, mais le changement de posture entre la
neutralité totale de la synthèse et la position assumée de l'essai."""),
],
"also": [
("/dalf/", "DALF C1 · C2 : épreuves, synthèse et préparation",
 "Le format complet des deux niveaux, le barème et les notes éliminatoires."),
("/blog/production-ecrite-delf-b2/", "Production écrite DELF B2 : la méthode",
 "Le cran en dessous : 250 mots, prise de position argumentée."),
("/correction-ia/", "La correction IA de l'écrit et de l'oral",
 "Comment votre neutralité et votre structure sont évaluées sur les critères officiels."),
("/blog/diplome-ou-test-delf-tcf/", "Diplôme ou test : lequel vous faut-il ?",
 "Ce que le DALF prouve, et les démarches où il ne suffit pas."),
],
"sources": """<strong>Les critères évoluent.</strong> Cette page est à jour au 7 août 2026. La
borne de 200 à 240 mots correspond aux critères d'évaluation officiels utilisés par les
correcteurs ; certaines pages de présentation mentionnent 220 mots comme borne basse. Vérifiez le
format en vigueur sur
<a href="https://www.france-education-international.fr/diplome/dalf" target="_blank" rel="noopener">france-education-international.fr</a>
avant votre session.""",
},

# ─────────────────────────────────────────────────────────────────────────────
{
"slug": "tefaq-oral-quebec",
"title": "TEFAQ : l'oral qui suffit pour le Québec",
"desc": "Le TEFAQ est modulaire : plusieurs programmes québécois n'exigent que l'oral. Format, épreuves à choisir selon votre volet, et pourquoi il n'ouvre pas Entrée express.",
"og_title": "TEFAQ : l'oral qui suffit pour le Québec",
"og_desc": "Le TEFAQ est modulaire : plusieurs programmes québécois n'exigent que l'oral. Format, épreuves à choisir, et pourquoi il n'ouvre pas Entrée express.",
"crumb": "TEFAQ",
"h1": "TEFAQ : le test modulaire où l'oral suffit souvent",
"date_fr": "7 août 2026",
"read": 7,
"accent": "accent-tef",
"intro": """Le TEFAQ — dénomination officielle actuelle « TEF Québec » — reprend
<strong>exactement les épreuves du <a href="/tef-canada/">TEF Canada</a></strong>, mais il est
<strong>modulaire</strong> : vous choisissez d'en passer 1, 2, 3 ou 4. Comme plusieurs programmes
québécois n'exigent que l'oral, beaucoup de candidats ne s'inscrivent qu'à deux épreuves — moins
de préparation, moins de risque, et une facture réduite d'autant.""",
"facts": [
"<strong>Mêmes épreuves que le TEF Canada</strong> : mêmes durées, mêmes tâches, mêmes consignes.",
"<strong>Modulaire</strong> : 1 à 4 épreuves au choix, dès la première inscription.",
"Résultats lus sur l'<strong>Échelle québécoise</strong> du MIFI, pas sur les NCLC fédéraux.",
"⚠️ <strong>Non accepté par IRCC</strong> pour Entrée express — le TEF Canada, lui, l'est.",
"Plusieurs volets québécois n'exigent que l'<strong>oral</strong> : deux épreuves suffisent.",
"⚠️ Ne confondez pas <strong>niveau québécois</strong> et <strong>NCLC</strong> : mêmes numéros, seuils différents.",
],
"toc": [
("format", "Le format, identique au TEF Canada"),
("modulaire", "La modularité, et ce qu'elle fait gagner"),
("programmes", "Quel volet exige quoi"),
("taches", "Les tâches TEF, à apprivoiser"),
("ircc", "Le piège : le TEFAQ n'ouvre pas Entrée express"),
("choisir", "TEFAQ, TEF Canada ou TCF Québec ?"),
],
"body": """
<h2 id="format">Le format, identique au TEF Canada</h2>

<p>Première chose à savoir : il n'y a <strong>aucune différence d'épreuves</strong> entre le
TEFAQ et le <a href="/tef-canada/">TEF Canada</a>. Mêmes durées, mêmes tâches, mêmes consignes.
Ce qui change est administratif — la modularité et le référentiel de lecture — pas le contenu.</p>

<div class="tablewrap">
<table>
<caption>Format des épreuves du TEFAQ. Source : Le français des affaires — CCI Paris Île-de-France, structure vérifiée en juillet 2026.</caption>
<thead><tr><th>Épreuve</th><th>Questions / tâches</th><th>Durée</th></tr></thead>
<tbody>
<tr><td>Compréhension écrite</td><td>40 questions</td><td>60 min</td></tr>
<tr><td>Compréhension orale</td><td>40 questions</td><td>40 min</td></tr>
<tr><td><strong>Expression écrite</strong></td><td>2 sections — A : 80 mots min · B : 200 mots min</td><td>60 min</td></tr>
<tr><td><strong>Expression orale</strong></td><td>2 sections — A : 5 min · B : 10 min</td><td>15 min</td></tr>
</tbody>
</table>
</div>

<p>Comme partout au TEF et au TCF, la compréhension orale se fait avec <strong>une seule
écoute</strong>, sans retour arrière.</p>

<h2 id="modulaire">La modularité, et ce qu'elle fait gagner</h2>

<p>C'est la caractéristique décisive, et elle est sous-exploitée. Avec le TEFAQ, vous vous
inscrivez à <strong>1, 2, 3 ou 4 épreuves</strong>, librement, dès la première inscription. Deux
versions seulement le permettent : le TEFAQ et le <a href="/tcf-quebec/">TCF Québec</a>. Le TEF
Canada, le TCF Canada et les deux versions IRN imposent les quatre épreuves.</p>

<p>Le gain est triple, et il ne se limite pas au prix :</p>

<ul>
<li><strong>Moins de préparation.</strong> Travailler deux épreuves au lieu de quatre concentre
l'effort là où il compte.</li>
<li><strong>Moins de risque.</strong> Vous ne pouvez pas être plafonné par une épreuve que vous
n'avez pas passée.</li>
<li><strong>Une facture réduite.</strong> Les centres facturent à l'épreuve — à titre de repère,
sur le TCF Québec, ne passer que les deux orales revient à peu près à la moitié du prix d'un test
complet.</li>
</ul>

<div class="note">
<p><strong>La modularité rend aussi la reprise moins douloureuse.</strong> Sur une version non
modulaire, une seule épreuve décevante oblige à repasser et repayer l'intégralité du test. Sur le
TEFAQ, vous vous réinscrivez à la seule épreuve que vous voulez améliorer.</p>
</div>

<h2 id="programmes">Quel volet exige quoi</h2>

<p>Les exigences québécoises s'expriment en niveaux de l'<strong>Échelle québécoise</strong>, un
cadre gouvernemental gradué de 1 à 12. Voici ce que demande chaque programme — c'est ce tableau
qui détermine les épreuves à passer.</p>

<div class="tablewrap">
<table>
<caption>Exigences de français par programme québécois, sur l'Échelle québécoise. Source : ministère de l'Immigration, de la Francisation et de l'Intégration.</caption>
<thead><tr><th>Programme / volet</th><th>Oral</th><th>Écrit</th><th>Épreuves à passer</th></tr></thead>
<tbody>
<tr><td><strong>PSTQ volet 1</strong> — haute qualification</td><td>niveau <strong>7</strong> ou plus</td><td>niveau <strong>5</strong> ou plus</td><td>les 4</td></tr>
<tr><td><strong>PSTQ volet 2</strong> — compétences intermédiaires et manuelles</td><td>niveau <strong>5</strong> ou plus</td><td>aucune exigence</td><td><strong>l'oral seul</strong></td></tr>
<tr><td><strong>PSTQ volet 3</strong> — professions réglementées</td><td>7 ou 5 selon le FEER</td><td>5 si FEER 0-2</td><td>selon le FEER</td></tr>
<tr><td><strong>PEQ</strong> — diplômés du Québec</td><td>—</td><td>niveau <strong>5</strong></td><td>l'écrit seul</td></tr>
<tr><td><strong>Conjoint accompagnateur</strong></td><td>niveau <strong>4</strong> ou plus</td><td>aucune exigence</td><td><strong>l'oral seul</strong></td></tr>
</tbody>
</table>
</div>

<p>Deux situations très courantes — le <strong>PSTQ volet 2</strong> et la condition faite au
<strong>conjoint accompagnateur</strong> — ne portent donc que sur l'oral. Dans ces cas,
s'inscrire aux seules compréhension orale et expression orale est parfaitement suffisant. Le
seuil du conjoint est d'ailleurs volontairement bas : le niveau 4 correspond au A2.</p>

<div class="note">
<p><strong>Pour convertir vos scores en niveaux de l'Échelle québécoise</strong>, appuyez-vous sur
la table publiée par le MIFI pour le test que vous passez. Nous détaillons celle du
<a href="/tcf-quebec/">TCF Québec</a>, vérifiée et sourcée, sur sa page dédiée. Vérifiez la table
correspondant au TEFAQ auprès du ministère ou de votre centre : les échelles diffèrent d'un test
à l'autre, et une conversion appliquée au mauvais barème donne un résultat faux.</p>
</div>

<h2 id="taches">Les tâches TEF, à apprivoiser</h2>

<p>Si vous hésitez encore entre le TEFAQ et le TCF Québec, retenez ceci : <strong>les compétences
évaluées sont les mêmes, les exercices ne le sont pas</strong>. Les deux sections d'expression du
TEF ont des consignes très typées, sans équivalent au TCF.</p>

<ul>
<li><strong>Expression orale, section A — obtenir des informations.</strong> Vous devez
<em>poser</em> des questions à l'examinateur, pas y répondre. Cette inversion de rôle est
contre-intuitive : beaucoup de candidats restent en position d'interrogé, produisent trop peu, et
perdent des points sur une section pourtant courte et prévisible.</li>
<li><strong>Expression orale, section B — argumenter pour convaincre.</strong> Dix minutes en
face à face, avec double évaluation.</li>
<li><strong>Expression écrite, section A — écrire la suite d'un texte.</strong> On vous donne le
début d'un article ou d'un fait divers ; vous devez en capter le registre, le temps verbal et le
point de vue. La note sanctionne la rupture de cohérence avec l'amorce.</li>
<li><strong>Expression écrite, section B — un point de vue argumenté</strong>, 200 mots minimum.</li>
</ul>

<p>Les minimums de mots — 80 et 200 — sont des <strong>planchers</strong>, pas des cibles : en
dessous, la conformité à la consigne est prise en défaut quelle que soit la qualité de la langue.</p>

<h2 id="ircc">Le piège : le TEFAQ n'ouvre pas Entrée express</h2>

<div class="note">
<p><strong>Malgré son nom, le TEFAQ n'est pas accepté par IRCC pour l'immigration économique
fédérale.</strong> Pour Entrée express, seuls deux tests comptent : le <strong>TEF Canada</strong>
et le <strong>TCF Canada</strong>. Le TEFAQ, le TCF Québec, le TCF Tout Public et les versions IRN
n'y figurent pas.</p>
</div>

<p>L'asymétrie est totale, et elle doit guider votre choix :</p>

<div class="tablewrap">
<table>
<caption>Acceptation croisée des deux versions TEF.</caption>
<thead><tr><th></th><th>Accepté par le Québec (MIFI)</th><th>Accepté par le fédéral (IRCC)</th></tr></thead>
<tbody>
<tr><td><strong>TEFAQ</strong></td><td>oui</td><td><strong>non</strong></td></tr>
<tr><td><strong>TEF Canada</strong></td><td>oui</td><td>oui</td></tr>
</tbody>
</table>
</div>

<p>Autre confusion coûteuse : <strong>le niveau 7 québécois n'est pas le NCLC 7 fédéral</strong>.
Les deux référentiels portent les mêmes numéros et ne recouvrent pas les mêmes scores. Règle
simple : si le texte dit « NCLC », c'est fédéral ; s'il dit « niveau » ou « Échelle québécoise »,
c'est le Québec. Le détail des seuils fédéraux est dans notre article
<a href="/blog/tcf-canada-nclc-7/">NCLC 7 au TCF Canada</a>.</p>

<h2 id="choisir">TEFAQ, TEF Canada ou TCF Québec ?</h2>

<ul>
<li><strong>Projet strictement québécois, et seul l'oral est exigé</strong> → TEFAQ ou
<a href="/tcf-quebec/">TCF Québec</a>. Deux épreuves, environ la moitié du prix.</li>
<li><strong>Projet québécois susceptible de basculer vers le fédéral</strong> →
<a href="/tef-canada/">TEF Canada</a>. Les quatre épreuves coûtent plus cher, mais vous couvrez
les deux voies.</li>
<li><strong>Vous hésitez entre les familles TCF et TEF</strong> → la réponse ne se déduit pas : le
seul critère fiable est votre score dans chaque format. Passez un
<a href="/examens-blancs/">examen blanc de chacun</a>, puis voyez notre comparatif
<a href="/blog/difference-tcf-tef/">TCF ou TEF, toutes les versions comparées</a>.</li>
</ul>

<p>Un dernier repère pratique : la déclaration d'intérêt se dépose gratuitement en ligne sur la
plateforme <strong>Arrima</strong>. Il faut avoir 18 ans ou plus et l'intention de résider et
travailler au Québec. Et pour le PSTQ, il n'y a <strong>aucune exigence de connaissance de
l'anglais</strong> — il peut seulement être déclaré facultativement, le seul test accepté pour le
valoriser étant l'IELTS.</p>
""",
"cta_h2": "Deux épreuves à passer, deux épreuves à réussir",
"cta_p": """Quand votre programme n'exige que l'oral, tout se joue sur deux épreuves — et
l'expression orale est celle qu'on ne peut pas s'auto-évaluer. Examens blancs au format exact du
TEF, sections A et B de l'oral comme de l'écrit, et correction IA sur les critères officiels, dans
l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Quelle différence entre le TEFAQ et le TEF Canada ?",
 """Les épreuves sont identiques — mêmes durées, mêmes tâches, mêmes consignes. Deux choses
changent : le TEFAQ est modulaire, vous choisissez 1 à 4 épreuves, alors que le TEF Canada les
impose toutes les quatre ; et les résultats du TEFAQ sont lus sur l'Échelle québécoise du MIFI,
pas sur les NCLC fédéraux."""),
("Le TEFAQ est-il accepté pour Entrée express ?",
 """Non, malgré son nom. Pour l'immigration économique fédérale, IRCC n'accepte que le TEF Canada
et le TCF Canada. Le TEFAQ, le TCF Québec, le TCF Tout Public et les versions IRN ne figurent pas
sur la liste fédérale. Si votre projet peut basculer vers le fédéral, passez le TEF Canada."""),
("Puis-je ne passer que l'oral au TEFAQ ?",
 """Oui. Le TEFAQ est modulaire : vous vous inscrivez à 1, 2, 3 ou 4 épreuves dès la première
inscription. Plusieurs situations québécoises ne portent que sur l'oral — le PSTQ volet 2 et la
condition faite au conjoint accompagnateur — et deux épreuves suffisent alors."""),
("Quel niveau faut-il pour le PSTQ ?",
 """Cela dépend du volet. Le volet 1, haute qualification, demande le niveau 7 à l'oral et le
niveau 5 à l'écrit sur l'Échelle québécoise. Le volet 2 demande le niveau 5 à l'oral et n'a aucune
exigence écrite. Le volet 3 varie selon le FEER de la profession. Le conjoint accompagnateur,
lui, doit atteindre le niveau 4 à l'oral."""),
("Le niveau 7 québécois est-il le même que le NCLC 7 ?",
 """Non, et les confondre est une erreur fréquente : les deux référentiels portent les mêmes
numéros sans recouvrir les mêmes scores. Règle simple : si le texte dit « NCLC », c'est fédéral ;
s'il dit « niveau » ou « Échelle québécoise », c'est le Québec."""),
("Faut-il parler anglais pour le PSTQ ?",
 """Non. Le ministère indique qu'il n'y a aucune exigence de connaissance de l'anglais dans le
PSTQ. L'anglais peut être déclaré facultativement dans la déclaration d'intérêt, et le seul test
accepté pour le valoriser est l'IELTS."""),
("En quoi consiste l'expression orale du TEF ?",
 """Deux sections en 15 minutes. Dans la section A, 5 minutes, vous devez obtenir des informations
en posant des questions à l'examinateur — c'est vous qui interrogez, ce qui est contre-intuitif et
se travaille. Dans la section B, 10 minutes, vous argumentez pour convaincre, avec double
évaluation."""),
],
"also": [
("/tef-canada/", "TEF Canada et TEFAQ : format, NCLC et préparation",
 "La page de référence des deux versions, avec la table de conversion NCLC."),
("/tcf-quebec/", "TCF Québec : le test modulaire pour l'immigration québécoise",
 "L'autre option modulaire, avec sa table de conversion vers l'Échelle québécoise."),
("/blog/difference-tcf-tef/", "TCF ou TEF : toutes les versions comparées",
 "Les neuf versions côte à côte, pour choisir la bonne famille avant de payer."),
("/blog/prix-tcf-tef/", "Combien coûte vraiment le TCF ou le TEF ?",
 "Ce que la modularité fait réellement gagner, chiffres de centres à l'appui."),
],
"sources": """<strong>La réglementation évolue.</strong> Cette page est à jour au 7 août 2026 et ne
constitue pas un conseil en immigration. Les seuils, tables de conversion et calendriers des
programmes québécois sont modifiés régulièrement. Vérifiez votre situation sur
<a href="https://www.quebec.ca/immigration" target="_blank" rel="noopener">quebec.ca</a> et le
format de l'examen sur
<a href="https://www.lefrancaisdesaffaires.fr/" target="_blank" rel="noopener">lefrancaisdesaffaires.fr</a>
avant de vous inscrire ou de déposer une demande.""",
},

]

if __name__ == "__main__":
    print("Batch 3 :")
    build(ARTICLES)
