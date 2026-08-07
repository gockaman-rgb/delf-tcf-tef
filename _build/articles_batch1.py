#!/usr/bin/env python3
"""Articles 1 à 4. Tous les chiffres proviennent des articles déjà publiés et
sourcés du site, ou d'EXAM_SPECS_AUDIT_2026.md (recoupé FEI/CCIP)."""

from article_template import build

ARTICLES = [

# ─────────────────────────────────────────────────────────────────────────────
{
"slug": "b1-ou-b2-nationalite-francaise",
"title": "B1 ou B2 pour la nationalité française en 2026 ?",
"desc": "B2 pour la naturalisation, B1 pour la carte de résident, A2 pour la première carte pluriannuelle : le tableau des trois niveaux et comment les prouver.",
"og_title": "B1 ou B2 pour la nationalité française en 2026 ?",
"og_desc": "B2 pour la naturalisation, B1 pour la carte de résident, A2 pour la première carte pluriannuelle. Le tableau complet et comment prouver son niveau.",
"crumb": "B1 ou B2 pour la nationalité",
"h1": "B1 ou B2 pour la nationalité française ? La réponse dépend de votre démarche",
"date_fr": "7 août 2026",
"read": 7,
"accent": "accent-tcf",
"intro": """Pour la <strong>nationalité française</strong>, c'est le <strong>B2</strong> — à l'oral
comme à l'écrit, pour toute demande déposée depuis le 1<sup>er</sup> janvier 2026. Le B1, lui,
concerne la <strong>carte de résident</strong>. Ces deux niveaux répondent à deux démarches
différentes, et les confondre coûte soit un test inutile, soit un dossier refusé.""",
"facts": [
"<strong>Naturalisation : B2</strong>, à l'oral <em>et</em> à l'écrit — c'était B1 avant 2026.",
"<strong>Première carte de résident : B1</strong> — c'était A2.",
"<strong>Première carte de séjour pluriannuelle : A2.</strong>",
"Origine : loi immigration du 26 janvier 2024 et <strong>arrêté du 22 décembre 2025</strong>.",
"⚠️ Un <strong>examen civique</strong> s'ajoute au test de langue : 40 questions, 45 minutes, <strong>32 bonnes réponses exigées</strong>.",
"Le critère d'application est la <strong>date de dépôt</strong> de votre demande.",
],
"toc": [
("trois-niveaux", "Trois démarches, trois niveaux"),
("j-ai-le-b1", "« J'ai le B1, puis-je demander la nationalité ? »"),
("prouver", "Comment prouver son niveau : tests ou diplômes"),
("civique", "L'examen civique s'ajoute au test de langue"),
("transitoire", "Ma demande est déjà déposée : suis-je concerné ?"),
("erreurs", "Les trois confusions les plus coûteuses"),
],
"body": """
<h2 id="trois-niveaux">Trois démarches, trois niveaux</h2>

<p>C'est le tableau à retenir. Chaque ligne est une démarche distincte, avec sa propre exigence
de français — il n'existe pas de « niveau pour les étrangers » unique.</p>

<div class="tablewrap">
<table>
<caption>Niveau de français exigé selon la démarche, situation au 7 août 2026. Sources : arrêté du 22 décembre 2025 et article L. 433-4 du CESEDA.</caption>
<thead><tr><th>Votre démarche</th><th>Niveau exigé</th><th>Avant 2026</th></tr></thead>
<tbody>
<tr><td>Première carte de séjour pluriannuelle</td><td><strong>A2</strong></td><td>A2 <em>(inchangé)</em></td></tr>
<tr><td>Première carte de résident (10 ans)</td><td><strong>B1</strong></td><td>A2</td></tr>
<tr><td><strong>Naturalisation française</strong></td><td><strong>B2</strong> — oral <em>et</em> écrit</td><td>B1</td></tr>
</tbody>
</table>
</div>

<p>Deux des trois exigences ont donc été relevées d'un cran en 2026, en application de la loi
immigration du 26 janvier 2024. Le A2 de la carte pluriannuelle, lui, n'a pas bougé.</p>

<div class="note">
<p><strong>Le piège de la carte de résident.</strong> Passer d'une carte de séjour pluriannuelle
à une carte de résident <strong>n'est pas un renouvellement</strong> : c'est une
<em>première délivrance</em> de carte de résident. Le B1 et l'examen civique sont donc exigés,
même si vous vivez en France depuis des années avec un titre valide.</p>
</div>

<h2 id="j-ai-le-b1">« J'ai le B1, puis-je demander la nationalité ? »</h2>

<p>C'est la question la plus fréquente, et la réponse est <strong>non</strong> pour toute demande
déposée depuis le 1<sup>er</sup> janvier 2026. Le B1 était suffisant auparavant ; il ne l'est
plus. Il faut désormais le B2, <strong>à l'oral comme à l'écrit</strong>.</p>

<p>La précision « oral <em>et</em> écrit » n'est pas décorative. Beaucoup de candidats ont un
français oral fluide, acquis par des années de vie en France, et un écrit resté au niveau B1 —
faute d'avoir jamais eu à rédiger un texte argumenté. Or c'est bien sur les
<strong>quatre épreuves</strong> que le niveau est mesuré.</p>

<p>Votre B1 n'est pas perdu pour autant : il reste exactement ce qu'il faut pour une
<a href="/blog/carte-de-resident-b1-2026/">première carte de résident</a>. Si votre parcours
passe par cette étape avant la naturalisation, vous êtes déjà au niveau requis pour la première,
et il vous reste une marche à franchir pour la seconde.</p>

<div class="note">
<p><strong>La marche B1 → B2 est la plus haute du CECRL.</strong> Au B1, il suffit de comprendre
et de raconter. Au B2, il faut argumenter, défendre un point de vue et comprendre des documents
abstraits. Comptez 4 à 6 mois de pratique régulière — et sachez que votre aisance quotidienne ne
prédit pas votre score : c'est l'écrit argumenté qui fait échouer, pas la conversation. D'où
l'intérêt d'un <a href="/examens-blancs/">examen blanc au format officiel</a> et d'une
<a href="/correction-ia/">correction de votre écrit sur les critères officiels</a> avant de vous
inscrire.</p>
</div>

<h2 id="prouver">Comment prouver son niveau : tests ou diplômes</h2>

<p>Deux familles de justificatifs existent, et elles n'ont pas la même durée de vie.</p>

<div class="tablewrap">
<table>
<caption>Les deux voies pour justifier de son niveau de français.</caption>
<thead><tr><th></th><th>Les tests</th><th>Les diplômes</th></tr></thead>
<tbody>
<tr><td>Lesquels</td><td><a href="/tcf-irn/">TCF IRN</a> · TEF IRN</td><td><a href="/delf-b1/">DELF</a> · <a href="/dalf/">DALF</a></td></tr>
<tr><td>Durée</td><td>1 h 30 à 1 h 35</td><td>2 h 10 à 4 h selon le niveau</td></tr>
<tr><td>Validité</td><td><strong>2 ans</strong></td><td><strong>à vie</strong></td></tr>
<tr><td>Conçu pour</td><td>ces démarches administratives</td><td>l'usage académique et professionnel</td></tr>
</tbody>
</table>
</div>

<p>Les tests IRN — « Intégration, Résidence, Nationalité » — sont taillés pour ces dossiers : plus
courts, sessions plus fréquentes, résultats rapides. Les diplômes demandent un examen plus long
mais <strong>n'expirent jamais</strong>. Le DELF B1 relève explicitement du <strong>4° de
l'article 3</strong> de l'arrêté du 22 décembre 2025, qui admet tout diplôme attestant d'un
niveau au moins équivalent au B1 ; un DELF B2, un DALF C1 ou C2 attestent
<em>a fortiori</em> du B2 exigé pour la naturalisation.</p>

<p>La règle pratique : si votre dossier part vite, le test suffit. Si votre parcours doit
s'étaler sur plusieurs années — ce qui est fréquent entre une carte de résident et une demande de
nationalité — le diplôme évite d'avoir à repasser et repayer un test expiré au mauvais moment.</p>

<div class="note">
<p><strong>Deux conditions que l'on oublie.</strong> D'abord, le test doit être passé
<strong>en présentiel</strong> : l'arrêté impose quatre épreuves distinctes, le même jour, en une
session unique, avec surveillance anti-fraude et vérification d'identité. Les tests en ligne
depuis chez soi ne sont pas recevables. Ensuite, au-delà du niveau, la certification doit être
<strong>enregistrée au répertoire spécifique</strong> — raison de plus pour vérifier qu'un test
acheté en ligne est bien recevable avant de le passer.</p>
</div>

<h2 id="civique">L'examen civique s'ajoute au test de langue</h2>

<p>Depuis 2026, la langue ne suffit plus : un <strong>examen civique</strong> s'ajoute au dossier.
Son format est précis — <strong>40 questions</strong>, <strong>45 minutes</strong> maximum, et
<strong>32 bonnes réponses exigées</strong>, soit un seuil de 80 %.</p>

<p>C'est un seuil élevé : huit erreurs suffisent à faire échouer. Il porte sur les valeurs, les
institutions et l'histoire de la République, et se prépare séparément du test de langue — les
deux n'ont ni le même contenu ni le même format. Notre app sœur
<a href="https://naturalisationfrancefacile.fr">Naturalisation France Facile</a> couvre cette
partie du dossier.</p>

<p>Notez aussi le coût administratif, souvent sous-estimé : le timbre fiscal de première
délivrance d'une carte de résident est passé à <strong>350 €</strong> depuis le
1<sup>er</sup> mai 2026, contre 225 € auparavant.</p>

<h2 id="transitoire">Ma demande est déjà déposée : suis-je concerné ?</h2>

<p>Le critère annoncé par l'administration est la <strong>date de dépôt</strong> : les nouvelles
exigences s'appliquent aux demandes déposées à partir du 1<sup>er</sup> janvier 2026. Une demande
déposée avant cette date relève du régime antérieur.</p>

<p>C'est un point où il ne faut pas se fier à une lecture rapide : « déposée » n'est pas
« préparée » ni « prise de rendez-vous ». En cas de doute sur votre situation précise — dossier
en cours d'instruction, rendez-vous pris avant mais dépôt effectif après —, faites confirmer par
la préfecture ou la plateforme instruisant votre demande. Le détail du régime transitoire est
dans notre article <a href="/blog/naturalisation-2026-niveau-b2/">Naturalisation 2026 : le niveau
B2 est devenu obligatoire</a>.</p>

<h2 id="erreurs">Les trois confusions les plus coûteuses</h2>

<ol>
<li><strong>Confondre les démarches.</strong> Passer un test visant le B1 alors qu'on prépare une
naturalisation, c'est payer deux fois. Vérifiez la ligne du tableau qui correspond
<em>exactement</em> à votre demande avant de vous inscrire.</li>
<li><strong>Croire qu'un oral fluide suffit.</strong> Le B2 est exigé sur les quatre épreuves.
Un candidat parfaitement à l'aise en conversation peut rester au B1 à l'écrit argumenté — et
c'est le cas le plus fréquent des échecs.</li>
<li><strong>Laisser expirer son attestation.</strong> Deux ans passent vite quand un dossier
s'étale. Si votre démarche risque de durer, le diplôme, qui n'expire pas, est le choix le plus
sûr.</li>
</ol>
""",
"cta_h2": "Sachez si vous avez vraiment le B2 avant de payer votre test",
"cta_p": """Examens blancs chronométrés au format exact du TCF IRN et du TEF IRN, notation sur
l'échelle 499 avec niveau CECRL par épreuve, et correction IA de l'expression écrite et orale sur
les critères officiels — c'est là que se joue la frontière entre B1 et B2. Dans l'app
«&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Faut-il le B1 ou le B2 pour la nationalité française ?",
 """Le B2, à l'oral comme à l'écrit, pour toute demande déposée depuis le 1<sup>er</sup> janvier
2026. Le B1 était suffisant auparavant, il ne l'est plus. Le B1 reste en revanche le niveau exigé
pour une première carte de résident, et le A2 pour une première carte de séjour pluriannuelle."""),
("Mon DELF B1 est-il encore utile pour la naturalisation ?",
 """Pas directement : il n'atteste pas le B2 désormais exigé. Il reste pleinement valable pour une
première carte de résident, où le B1 est le niveau requis, et un diplôme n'expire jamais —
contrairement à une attestation TCF ou TEF, valable deux ans. Pour la nationalité, il faudra
justifier du B2, par un test IRN ou par un DELF B2."""),
("Quel niveau pour une première carte de séjour pluriannuelle ?",
 """Le A2, en application de l'article L. 433-4 du CESEDA. C'est la seule des trois exigences qui
n'a pas été relevée en 2026."""),
("Passer d'une carte pluriannuelle à une carte de résident, est-ce un renouvellement ?",
 """Non, et c'est un piège fréquent : c'est une première délivrance de carte de résident. Le
niveau B1 et l'examen civique sont donc exigés, même si vous vivez en France depuis des années
avec un titre de séjour valide."""),
("En quoi consiste l'examen civique ?",
 """40 questions, 45 minutes maximum, et 32 bonnes réponses exigées — soit 80 %. Il porte sur les
valeurs, les institutions et l'histoire de la République, et se prépare séparément du test de
langue : les deux n'ont ni le même contenu ni le même format."""),
("Ma demande déposée avant le 1er janvier 2026 est-elle concernée ?",
 """Le critère annoncé par l'administration est la date de dépôt : les nouvelles exigences
s'appliquent aux demandes déposées à partir du 1<sup>er</sup> janvier 2026. Attention, « déposée »
n'est ni « préparée » ni « rendez-vous pris » — faites confirmer votre situation précise par la
préfecture ou la plateforme qui instruit votre dossier."""),
("Peut-on passer le test de français en ligne depuis chez soi ?",
 """Non. L'arrêté du 22 décembre 2025 impose quatre épreuves distinctes passées en présentiel, le
même jour, en une session unique, avec surveillance anti-fraude et vérification de votre identité
sur un document officiel en cours de validité. Les tests passés en ligne depuis chez soi ne sont
pas recevables pour un titre de séjour."""),
],
"also": [
("/blog/naturalisation-2026-niveau-b2/", "Naturalisation 2026 : le niveau B2 est devenu obligatoire",
 "Le détail de la démarche nationalité : justificatifs, examen civique, régime transitoire."),
("/blog/carte-de-resident-b1-2026/", "Carte de résident : le B1 exigé depuis janvier 2026",
 "Qui est concerné, les cas de dispense et le coût réel de la démarche."),
("/tcf-irn/", "TCF IRN : le test de français pour votre naturalisation",
 "Format, échelle sur 499, prix et CPF du test conçu pour ces démarches."),
("/blog/tcf-irn-ou-tef-irn/", "TCF IRN ou TEF IRN : lequel choisir ?",
 "Les deux tests de naturalisation comparés, format et prix à l'appui."),
("/delf-b2/", "DELF B2 : le diplôme qui ouvre les universités françaises",
 "L'alternative « diplôme » : plus longue à passer, mais elle n'expire jamais."),
],
"sources": """<strong>La réglementation évolue.</strong> Cette page est à jour au 7 août 2026 et ne
constitue pas un conseil juridique. Les niveaux exigés et la liste des justificatifs recevables
sont modifiés régulièrement — vérifiez votre situation sur
<a href="https://www.service-public.fr/" target="_blank" rel="noopener">service-public.fr</a>
avant de vous inscrire à un test ou de déposer une demande.""",
},

# ─────────────────────────────────────────────────────────────────────────────
{
"slug": "tcf-irn-ou-tef-irn",
"title": "TCF IRN ou TEF IRN : lequel choisir en 2026 ?",
"desc": "Les deux tests de naturalisation comparés : formats, durées, échelles sur 499, réformes 2025, prix relevés et financement CPF. Et le seul critère qui départage.",
"og_title": "TCF IRN ou TEF IRN : lequel choisir en 2026 ?",
"og_desc": "Formats, durées, échelles sur 499, réformes 2025, prix relevés et CPF. Et le seul critère qui départage vraiment les deux tests.",
"crumb": "TCF IRN ou TEF IRN",
"h1": "TCF IRN ou TEF IRN : le comparatif des deux tests de naturalisation",
"date_fr": "7 août 2026",
"read": 7,
"accent": "accent-tcf",
"intro": """Les deux tests servent <strong>exactement la même démarche</strong> — intégration,
résidence, nationalité française — couvrent tous deux jusqu'au <strong>B2</strong> et sont notés
sur la même échelle de <strong>499</strong>. Aucune source officielle ne permet de dire que l'un
est plus facile. Ce qui les sépare tient au format des épreuves, au prix de votre centre, et à
une différence technique que peu de candidats connaissent : <strong>le TEF IRN est
adaptatif</strong>.""",
"facts": [
"<strong>Même usage</strong> : les deux sont acceptés par l'administration française et couvrent jusqu'au B2.",
"<strong>Même échelle</strong> : QCM notés sur <strong>499</strong>, pas sur 699.",
"<strong>TCF IRN</strong> : 1 h 35, réformé le <strong>12 mai 2025</strong> (échelle étendue au B2).",
"<strong>TEF IRN</strong> : 1 h 30, réformé le <strong>1<sup>er</sup> avril 2025</strong> — et <strong>adaptatif</strong> sur les deux compréhensions.",
"⚠️ Les deux imposent <strong>4 épreuves insécables</strong>, en présentiel, une seule écoute.",
"Le seul critère fiable : <strong>votre score dans chaque format</strong>, et les dates de session près de chez vous.",
],
"toc": [
("meme-usage", "Deux tests, un seul usage"),
("format", "Les deux formats côte à côte"),
("adaptatif", "L'adaptatif du TEF IRN : ce que ça change"),
("reformes", "Deux réformes en 2025, à six semaines d'écart"),
("prix", "Prix et financement"),
("choisir", "Comment choisir, concrètement"),
],
"body": """
<h2 id="meme-usage">Deux tests, un seul usage</h2>

<p>Commençons par ce qui ne les distingue pas, parce que c'est l'essentiel. Le TCF IRN, proposé
par <strong>France Éducation international</strong>, et le TEF IRN, proposé par <strong>Le
français des affaires</strong> (CCI Paris Île-de-France), servent la même démarche : prouver
votre niveau de français pour une carte de séjour, une carte de résident ou une demande de
nationalité.</p>

<p>Ils partagent en outre quatre caractéristiques qui pèsent lourd dans la préparation :</p>

<ul>
<li><strong>Quatre épreuves imposées</strong>, insécables : on ne peut pas en passer une partie.</li>
<li><strong>Une seule écoute</strong> en compréhension orale, sans retour arrière.</li>
<li><strong>Présentiel obligatoire</strong> : l'arrêté du 22 décembre 2025 impose une session
unique, le même jour, avec surveillance anti-fraude et vérification d'identité.</li>
<li><strong>Attestation valable deux ans</strong> dans les deux cas.</li>
</ul>

<h2 id="format">Les deux formats côte à côte</h2>

<div class="tablewrap">
<table>
<caption>TCF IRN et TEF IRN, formats 2026. Sources : France Éducation international et Le français des affaires, structures vérifiées en juillet 2026.</caption>
<thead><tr><th>Épreuve</th><th>TCF IRN</th><th>TEF IRN</th></tr></thead>
<tbody>
<tr><td>Compréhension orale</td><td>25 QCM · 20 min</td><td>20 questions · 20 min <strong>· adaptatif</strong></td></tr>
<tr><td>Compréhension écrite</td><td>25 QCM · 35 min</td><td>20 questions · 30 min <strong>· adaptatif</strong></td></tr>
<tr><td>Expression écrite</td><td>30 min</td><td>30 min</td></tr>
<tr><td>Expression orale</td><td>10 min</td><td>10 min</td></tr>
<tr><td><strong>Durée totale</strong></td><td><strong>1 h 35</strong></td><td><strong>1 h 30</strong></td></tr>
<tr><td>Notation des QCM</td><td>100–499</td><td>/499</td></tr>
<tr><td>Écoutes</td><td>1 seule</td><td>1 seule</td></tr>
</tbody>
</table>
</div>

<p>Les deux tests durent donc pratiquement le même temps, et la répartition entre compréhension
et expression est identique. La différence de volume de questions — 25 contre 20 par
compréhension — s'explique par la logique adaptative du TEF, détaillée ci-dessous.</p>

<h2 id="adaptatif">L'adaptatif du TEF IRN : ce que ça change</h2>

<p>C'est la vraie différence technique entre les deux, et elle est passée largement inaperçue.
Depuis sa réforme d'avril 2025, le TEF IRN est <strong>adaptatif sur ses deux
compréhensions</strong> : la difficulté des questions s'ajuste à vos réponses au fil de
l'épreuve. Le TCF IRN, lui, est linéaire.</p>

<p>Concrètement, pour un candidat :</p>

<ul>
<li><strong>En adaptatif, l'épreuve ne « devient pas plus facile » si vous vous trompez.</strong>
Elle se recalibre pour cerner votre niveau plus vite. Sentir les questions durcir est bon signe,
pas mauvais.</li>
<li><strong>Moins de questions suffisent</strong> pour estimer un niveau — d'où les 20 items du
TEF contre 25 au TCF.</li>
<li><strong>Chaque réponse pèse davantage</strong>, mécaniquement, puisqu'elles sont moins
nombreuses. Répondre au hasard en début d'épreuve oriente la suite.</li>
</ul>

<p>Aucun des deux formats n'est objectivement plus favorable : cela dépend de votre profil. Un
candidat régulier, dont le niveau est homogène, s'en sort bien en adaptatif. Un candidat
irrégulier, qui a besoin de se chauffer, peut préférer la progression linéaire du TCF.</p>

<h2 id="reformes">Deux réformes en 2025, à six semaines d'écart</h2>

<p>Les deux tests ont été refondus la même année, pour la même raison : accompagner le relèvement
des exigences au <strong>B2</strong> pour la naturalisation.</p>

<div class="tablewrap">
<table>
<caption>Les deux réformes IRN de 2025.</caption>
<thead><tr><th></th><th>Date</th><th>Ce qui a changé</th></tr></thead>
<tbody>
<tr><td><strong>TEF IRN</strong></td><td>1<sup>er</sup> avril 2025</td><td>Durée portée de 1 h 20 à 1 h 30, passage à l'adaptatif sur les deux compréhensions, section argumentée de l'expression écrite portée à 100 mots</td></tr>
<tr><td><strong>TCF IRN</strong></td><td>12 mai 2025</td><td>Échelle étendue jusqu'au <strong>B2</strong>, alors qu'elle plafonnait au B1</td></tr>
</tbody>
</table>
</div>

<div class="note">
<p><strong>Toute ressource antérieure à 2025 décrit un examen qui n'existe plus.</strong> Et le
problème va plus loin : les pages de France Éducation international décrivent encore, à ce jour,
un TCF IRN plafonné au B1 et noté sur 399. C'est la documentation officielle qui n'a pas suivi sa
propre réforme. Vérifiez systématiquement la date des ressources sur lesquelles vous vous
entraînez.</p>
</div>

<h2 id="prix">Prix et financement</h2>

<p>Aucun des deux organismes ne publie de tarif national : chaque centre agréé fixe son prix.
Sur les centres français relevés fin juillet 2026, les fourchettes se chevauchent largement.</p>

<div class="tablewrap">
<table>
<caption>Fourchettes relevées sur des centres agréés français, fin juillet 2026. Indicatif : plusieurs centres précisent que leurs tarifs sont modifiables sans préavis.</caption>
<thead><tr><th>Test</th><th>Fourchette relevée en France</th></tr></thead>
<tbody>
<tr><td><strong>TCF IRN</strong></td><td>135 € à 220 €</td></tr>
<tr><td><strong>TEF IRN</strong></td><td>environ 155 € à 205 €</td></tr>
</tbody>
</table>
</div>

<p>Le prix ne départage donc pas les deux tests : <strong>il départage les centres</strong>. Un
TCF IRN peut coûter moins cher qu'un TEF IRN, ou l'inverse, selon l'établissement — dans la même
ville.</p>

<p><strong>Côté CPF</strong>, le TCF IRN est enregistré au répertoire spécifique de France
compétences sous la fiche <strong>RS6643, valable jusqu'au 31 mai 2027</strong>, ce qui le rend
finançable par le compte personnel de formation. Notre <a href="/blog/cpf-test-francais/">état
des lieux du financement CPF</a> détaille version par version ce qui est enregistré et ce qui ne
l'est pas — et les enregistrements expirent, donc vérifiez la fiche en vigueur avant de monter un
dossier.</p>

<h2 id="choisir">Comment choisir, concrètement</h2>

<p>Puisque l'usage est identique, le niveau couvert identique et le prix dicté par le centre, la
décision se prend sur trois critères, dans cet ordre.</p>

<ol>
<li><strong>Les dates et les centres près de chez vous.</strong> C'est le critère n°1 dans les
faits : un test disponible dans trois semaines à trente minutes de chez vous bat un test
théoriquement préférable à deux heures de route dans deux mois.</li>
<li><strong>Votre score dans chaque format.</strong> Le seul critère objectif. Passez un examen
blanc de chacun et retenez celui où vous marquez le plus — l'écart entre les deux est très
variable d'un candidat à l'autre, selon qu'il est plus à l'aise en QCM linéaire ou en adaptatif.
Notre page <a href="/examens-blancs/">examens blancs</a> détaille le protocole de passation à
respecter pour que la comparaison ait un sens.</li>
<li><strong>Le financement.</strong> Si vous comptez mobiliser votre CPF, vérifiez que la version
visée est bien enregistrée au répertoire spécifique au moment de votre inscription.</li>
</ol>

<p>Une fois le choix fait, <strong>entraînez-vous au format exact du test choisi</strong>. C'est
là que se joue l'essentiel : les consignes d'expression écrite ne sont pas les mêmes, et un
candidat qui découvre le jour J une section argumentée de 100 mots au TEF, ou la structure des
tâches du TCF, perd des points qui n'ont rien à voir avec son niveau de français.</p>
""",
"cta_h2": "Passez un blanc de chacun avant de choisir",
"cta_p": """Examens blancs chronométrés au format exact du TCF IRN <em>et</em> du TEF IRN,
notation sur l'échelle 499 avec niveau CECRL par épreuve, correction IA de l'expression écrite et
orale sur les critères officiels. Le seul moyen de savoir lequel vous réussit le mieux — dans
l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Le TCF IRN et le TEF IRN sont-ils équivalents ?",
 """Pour l'administration française, oui : les deux sont acceptés pour les démarches
d'intégration, de résidence et de nationalité, et couvrent tous deux jusqu'au niveau B2. Ils
diffèrent par l'opérateur, le format des tâches et la façon de conduire les compréhensions — le
TEF IRN est adaptatif, le TCF IRN linéaire."""),
("Lequel est le plus facile ?",
 """Aucune source officielle ne permet de l'affirmer, et la question est mal posée : la difficulté
ressentie dépend de votre profil. Un candidat au niveau homogène s'en sort souvent mieux en
adaptatif, un candidat qui a besoin de se chauffer préfère la progression linéaire. Le seul
critère fiable est votre propre score dans chaque format."""),
("Qu'est-ce qu'un test adaptatif ?",
 """Un test dont la difficulté des questions s'ajuste à vos réponses au fil de l'épreuve, afin de
cerner votre niveau avec moins de questions. Depuis avril 2025, le TEF IRN est adaptatif sur ses
deux compréhensions. Sentir les questions durcir est bon signe : cela veut dire que vous
réussissez."""),
("Les deux sont-ils notés sur 499 ?",
 """Oui. Les deux versions IRN plafonnent au niveau B2, et le B2 s'arrête à 499 sur la grille du
TCF : leurs QCM sont donc notés sur 499, et non sur 699 comme le TCF Canada ou le TCF Tout
Public. Méfiez-vous des sources qui annoncent 500–599 pour le B2 : cette bande correspond au C1,
un niveau que les versions IRN ne délivrent pas."""),
("Combien de temps durent-ils ?",
 """1 h 35 pour le TCF IRN et 1 h 30 pour le TEF IRN, dans les deux cas en une session unique avec
quatre épreuves insécables. C'est nettement plus court que les versions Canada, qui dépassent
2 h 45, parce que les versions IRN s'arrêtent au B2."""),
("Le TEF IRN est-il finançable par le CPF ?",
 """Le TCF IRN l'est, via la fiche RS6643 valable jusqu'au 31 mai 2027. Pour le TEF IRN,
vérifiez la fiche en vigueur sur France compétences au moment de votre inscription : les
enregistrements au répertoire spécifique ont une date d'expiration et ne sont pas toujours
renouvelés. Sans enregistrement actif, aucun financement CPF n'est possible."""),
("Puis-je passer les deux ?",
 """Rien ne l'interdit, mais c'est payer deux fois pour prouver la même chose. La démarche
rationnelle est de passer un examen blanc de chacun — gratuitement ou dans une app de préparation
— puis de ne s'inscrire qu'au test où votre score est le plus haut."""),
],
"also": [
("/tcf-irn/", "TCF IRN : le test de français pour votre naturalisation",
 "Le guide complet : format, échelle 499, présentiel obligatoire, prix et CPF."),
("/blog/b1-ou-b2-nationalite-francaise/", "B1 ou B2 pour la nationalité française ?",
 "Quel niveau pour quelle démarche, et comment le prouver."),
("/blog/difference-tcf-tef/", "TCF ou TEF : toutes les versions comparées",
 "Les neuf versions des deux familles, leurs échelles et qui accepte quoi."),
("/blog/prix-tcf-tef/", "Combien coûte vraiment le TCF ou le TEF ?",
 "Les prix relevés centre par centre, et pourquoi l'écart va du simple au double."),
],
"sources": """<strong>Les formats évoluent.</strong> Cette page est à jour au 7 août 2026. Les deux
tests ont été réformés en 2025 et la documentation officielle accuse parfois du retard sur ses
propres réformes. Vérifiez le format et le tarif auprès de votre centre agréé, et les conditions
de votre démarche sur
<a href="https://www.service-public.fr/" target="_blank" rel="noopener">service-public.fr</a>,
avant de vous inscrire.""",
},

# ─────────────────────────────────────────────────────────────────────────────
{
"slug": "prix-tcf-tef",
"title": "Combien coûte le TCF ou le TEF ? Les prix relevés",
"desc": "Il n'existe aucun tarif national : l'écart entre centres va du simple au double. Les prix relevés en France et au Canada, centre par centre, avec leurs dates.",
"og_title": "Combien coûte le TCF ou le TEF ? Les prix relevés",
"og_desc": "Aucun tarif national n'existe : l'écart entre centres va du simple au double. Prix relevés en France et au Canada, centre par centre.",
"crumb": "Prix du TCF et du TEF",
"h1": "Combien coûte vraiment le TCF ou le TEF ?",
"date_fr": "7 août 2026",
"read": 8,
"accent": "accent-tcf",
"intro": """Commençons par ce qui n'existe pas : <strong>il n'y a aucun tarif officiel</strong>.
Ni France Éducation international ni Le français des affaires ne publient de prix national, et
aucun texte ne l'encadre. C'est le <strong>centre</strong> qui décide — et pour un test
rigoureusement identique, en France, à la même période, l'écart d'un centre à l'autre va
<strong>du simple au double</strong>.""",
"facts": [
"<strong>Aucun tarif national</strong>, aucun plafond : le prix est libre, fixé par chaque centre agréé.",
"En France, <strong>TCF IRN 135–220 €</strong> · <strong>TCF Canada 195–285 €</strong> · <strong>TEF Canada 245 €</strong> relevé chez ALIP Paris.",
"Au Canada, <strong>TCF Canada 400 à 440 $CA</strong> — et très peu de centres publient un prix.",
"⚠️ Le <strong>prix d'appel</strong> à 80–110 € correspond à la formule « 3 QCM », pas au test complet.",
"⚠️ Nous n'avons trouvé <strong>aucun tarif canadien vérifiable pour le TEF Canada</strong>.",
"Le vrai levier d'économie : le <strong>nombre d'épreuves</strong>, pas le choix du test.",
],
"toc": [
("pas-de-tarif", "Ce qui n'existe pas : le tarif officiel"),
("france", "Les prix relevés en France"),
("appel", "Le piège du prix d'appel"),
("canada", "Au Canada, très peu de prix publiés"),
("modularite", "Le vrai levier : le nombre d'épreuves"),
("cpf", "Ce que le CPF change à la facture"),
],
"body": """
<h2 id="pas-de-tarif">Ce qui n'existe pas : le tarif officiel</h2>

<p>Aucun texte ne fixe ni ne plafonne le prix d'un TCF ou d'un TEF : c'est un
<strong>prix libre</strong>, régi par le droit commun de la concurrence. Méfiez-vous donc de tout
site annonçant un tarif « officiel » ou une « fourchette encadrée » — cette dernière formule, qui
circule beaucoup, ne correspond à rien.</p>

<p>Ce que fait France Éducation international, sur chacune de ses pages de test, c'est vous
renvoyer au centre : c'est lui qui vous renseignera sur les dates, la procédure d'inscription, le
lieu et le support de passation, <em>ainsi que le tarif</em>. Et c'est bien le centre qui décide :
le formulaire de demande d'agrément comporte une case de tarif à remplir pour chaque déclinaison
et chaque formule, et l'organisme fournit même aux centres candidats un calculateur de rentabilité
de session. Certains centres le confirment à leur manière — l'université Toulouse Jean Jaurès
précise que ses tarifs de TCF sont votés « sous réserve de validation par le CA de
l'Université ».</p>

<h2 id="france">Les prix relevés en France</h2>

<div class="tablewrap">
<table>
<caption>Amplitude des tarifs relevés sur une dizaine de centres agréés français, fin juillet 2026. Indicatif : ces prix changent, et plusieurs centres précisent qu'ils sont modifiables sans préavis.</caption>
<thead><tr><th>Version</th><th>Le moins cher relevé</th><th>Le plus cher relevé</th><th>Écart</th></tr></thead>
<tbody>
<tr><td>TCF Tout Public — 3 QCM seuls</td><td>80 € <em>(Toulouse UT2J)</em></td><td>160 € <em>(ACCORD Paris)</em></td><td><strong>× 2</strong></td></tr>
<tr><td>TCF Tout Public — complet, 5 épreuves</td><td>185 € <em>(Toulouse UT2J)</em></td><td>260 € <em>(ACCORD Paris)</em></td><td>× 1,4</td></tr>
<tr><td><a href="/tcf-irn/">TCF IRN</a></td><td>135 € <em>(ACTE Paris)</em></td><td>220 € <em>(ACCORD Paris)</em></td><td><strong>× 1,6</strong></td></tr>
<tr><td><a href="/tcf-canada/">TCF Canada</a></td><td>195 € <em>(ACTE Paris)</em></td><td>285 € <em>(CLPS)</em></td><td>× 1,5</td></tr>
</tbody>
</table>
</div>

<p>Deux repères complémentaires relevés à la même période : le TCF Canada est à
<strong>220 €</strong> à l'Alliance Française de Lyon et <strong>200 €</strong> à Montpellier ;
le <a href="/tef-canada/">TEF Canada</a> à <strong>245 €</strong> chez ALIP à Paris. Le TEF IRN,
lui, se situe autour de <strong>155 à 205 €</strong>.</p>

<p>La conclusion tient en une phrase : <strong>le prix ne départage pas le TCF et le TEF, il
départage les centres et les formules.</strong> Avant de choisir un test parce qu'il serait « moins
cher », appelez deux ou trois centres autour de vous — l'écart que vous y trouverez dépassera
largement l'écart entre les deux familles.</p>

<h2 id="appel">Le piège du prix d'appel</h2>

<div class="note">
<p><strong>Les tarifs de TCF Tout Public les plus bas que vous verrez annoncés — 80 à 110 € —
correspondent à la formule « trois QCM seulement »</strong>, sans expression écrite ni orale. La
version complète coûte à peu près le double. Comparez toujours des formules identiques, pas des
chiffres d'affiche.</p>
</div>

<p>Ce piège est d'autant plus coûteux que la formule courte ne convient pas à la plupart des
démarches : dès qu'un dossier exige une preuve d'expression écrite ou orale — et c'est le cas de
la naturalisation, de l'immigration canadienne et de l'admission universitaire —, les trois QCM
ne suffisent pas. Payer 80 € pour un test inutilisable revient plus cher que payer 185 € pour le
bon.</p>

<h2 id="canada">Au Canada, très peu de prix publiés</h2>

<p>Côté canadien, les tarifs publiés sont rares — et plus élevés que ce qu'on lit d'ordinaire.
Voici ceux que nous avons pu vérifier.</p>

<div class="tablewrap">
<table>
<caption>Tarifs canadiens vérifiés le 30 juillet 2026. À titre indicatif — vérifiez auprès de votre centre avant de vous inscrire.</caption>
<thead><tr><th>Centre</th><th>Version</th><th>Tarif</th></tr></thead>
<tbody>
<tr><td>Alliance Française d'Edmonton</td><td>TCF Canada complet</td><td><strong>400 $CA</strong></td></tr>
<tr><td>EIF – UQTR, Trois-Rivières</td><td>TCF Canada complet</td><td><strong>440 $CA</strong></td></tr>
<tr><td>EIF – UQTR, Trois-Rivières</td><td><a href="/tcf-quebec/">TCF Québec</a>, à la carte</td><td>CO 105 $ · CE 105 $ · EE 105 $ · EO 125 $</td></tr>
<tr><td>Alliance Française de Montréal</td><td>toutes</td><td><strong>aucun prix publié</strong></td></tr>
</tbody>
</table>
</div>

<div class="note">
<p><strong>Deux mises en garde.</strong> D'abord, beaucoup de grands centres, dont l'Alliance
Française de Montréal, ne publient <em>aucun</em> tarif : l'inscription se fait en ligne selon
les disponibilités, et la seule somme affichée est un frais d'annulation de 75 $. Les prix
attribués à ces centres par les comparateurs ne sont pas sourcés, et mélangent souvent TCF Québec
et TCF Canada — deux versions aux prix différents. Ensuite, nous n'avons trouvé
<strong>aucun prix canadien vérifiable pour le TEF Canada</strong> : ne croyez pas les tableaux
qui affirment que les deux tests y sont « au même prix ».</p>
</div>

<p>Nous n'avons par ailleurs trouvé aucun tarif vérifiable pour le Maghreb, l'Afrique de l'Ouest,
le Liban, l'Inde ou le Brésil. <strong>N'extrapolez pas les chiffres européens ou canadiens à
votre pays.</strong></p>

<h2 id="modularite">Le vrai levier : le nombre d'épreuves</h2>

<p>Si vous cherchez à réduire la facture, ce n'est pas sur le choix du test qu'il faut jouer,
c'est sur le <strong>nombre d'épreuves que vous passez</strong>. Et là, les versions ne sont pas
égales.</p>

<div class="tablewrap">
<table>
<caption>Modularité par version : combien d'épreuves êtes-vous obligé de passer.</caption>
<thead><tr><th>Régime</th><th>Versions</th><th>Conséquence sur le prix</th></tr></thead>
<tbody>
<tr><td><strong>Vraiment modulaire</strong></td><td>TCF Québec · TEFAQ</td><td>Vous payez 1 à 4 épreuves au choix</td></tr>
<tr><td>Modulaire par ajout</td><td>TCF Tout Public · TEF Études</td><td>Socle obligatoire, expressions en option</td></tr>
<tr><td><strong>Non modulaire</strong></td><td>TCF Canada · TEF Canada · TCF IRN · TEF IRN</td><td>Les 4 épreuves, toujours</td></tr>
</tbody>
</table>
</div>

<p>L'exemple le plus parlant vient du Québec. Plusieurs programmes n'exigent que l'oral — le PSTQ
volet 2, la condition faite au conjoint accompagnateur. À l'EIF de l'UQTR, ne passer que les deux
épreuves orales du TCF Québec revient à <strong>230 $CA</strong>, contre <strong>440 $CA</strong>
pour un TCF Canada complet dans ce même centre. À peu près la moitié, pour deux épreuves à
préparer au lieu de quatre. En France, l'Alliance Française de Montpellier applique
<strong>65 € par module</strong> et Aix-Marseille <strong>60 € par épreuve</strong>, soit 130 € ou
120 € pour les deux orales.</p>

<h2 id="cpf">Ce que le CPF change à la facture</h2>

<p>En France, le compte personnel de formation peut couvrir tout ou partie du coût — mais
seulement pour les versions <strong>enregistrées au répertoire spécifique</strong> de France
compétences. Deux le sont : le <strong>TCF Tout Public</strong> et le <strong>TCF IRN</strong>.
Le TCF Canada n'est pas enregistré, et l'enregistrement du TCF Québec a expiré fin 2021.</p>

<div class="note">
<p><strong>Méfiez-vous des comparaisons sur Mon Compte Formation.</strong> Les offres qu'on y
trouve sont souvent des <strong>forfaits préparation + examen</strong> : on rencontre par exemple
430 € pour un TCF IRN accompagné de 14 heures de préparation, contre 155 à 180 € pour l'examen
seul ailleurs. Ce ne sont pas les mêmes produits. Le détail version par version est dans notre
article <a href="/blog/cpf-test-francais/">quels tests de français le CPF finance</a>.</p>
</div>

<p>Dernier point à intégrer au budget : <strong>chaque tentative se paie</strong>. Il n'existe
aucune reprise partielle au TCF Canada ni aux versions IRN — on repasse les quatre épreuves.
Savoir où l'on en est <em>avant</em> de s'inscrire est donc, très concrètement, une décision
financière : un <a href="/examens-blancs/">examen blanc au format officiel</a> coûte le temps
d'une matinée, une seconde tentative coûte le prix du test.</p>
""",
"cta_h2": "Un test raté se repaie en entier",
"cta_p": """Examens blancs chronométrés au format officiel de chaque déclinaison, notation sur
l'échelle du test que vous passez, conversion NCLC, CLB et Échelle québécoise, correction IA de
l'écrit et de l'oral. Savoir où vous en êtes avant de payer 200 € ou 440 $ — dans l'app
«&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Existe-t-il un tarif officiel pour le TCF ou le TEF ?",
 """Non. Ni France Éducation international ni Le français des affaires ne publient de tarif
national, et aucun texte ne fixe ni ne plafonne ce prix : il est libre et fixé par chaque centre
agréé. Méfiez-vous des sites annonçant un tarif « officiel » ou une « fourchette encadrée » —
cette formule ne correspond à rien."""),
("Combien coûte le TCF IRN ?",
 """Sur les centres français relevés fin juillet 2026, de 135 € chez ACTE à Paris à 220 € chez
ACCORD, également à Paris — un rapport de 1 à 1,6 pour un test rigoureusement identique, dans la
même ville. Demandez le tarif à votre centre avant de vous inscrire."""),
("Combien coûte le TCF Canada ?",
 """En France, de 195 € à 285 € selon le centre. Au Canada, nous avons vérifié 400 $CA à
l'Alliance Française d'Edmonton et 440 $CA à l'EIF de l'UQTR le 30 juillet 2026. Beaucoup de
grands centres canadiens, dont l'Alliance Française de Montréal, ne publient aucun tarif."""),
("Pourquoi vois-je des TCF annoncés à 80 € ?",
 """Parce qu'il s'agit de la formule « trois QCM seulement » du TCF Tout Public, sans expression
écrite ni orale. La version complète coûte à peu près le double. Cette formule courte ne convient
pas aux démarches qui exigent une preuve d'expression — naturalisation, immigration canadienne,
admission universitaire."""),
("Le TEF est-il moins cher que le TCF ?",
 """Non, et la question est mal posée : le prix ne départage pas les deux familles, il départage
les centres. En France, les fourchettes se chevauchent largement. Au Canada, nous n'avons trouvé
aucun tarif TEF Canada vérifiable — méfiez-vous des tableaux qui affirment que les deux tests y
sont au même prix."""),
("Comment payer moins cher ?",
 """En passant moins d'épreuves, quand votre démarche le permet. Le TCF Québec et le TEFAQ sont
modulaires : vous choisissez 1 à 4 épreuves. Plusieurs programmes québécois n'exigeant que
l'oral, ne passer que les deux épreuves orales revient à environ la moitié du prix d'un test
complet. Les versions Canada et IRN, elles, imposent les quatre épreuves."""),
("Le CPF peut-il financer mon test ?",
 """Seulement pour les versions enregistrées au répertoire spécifique de France compétences : le
TCF Tout Public et le TCF IRN. Le TCF Canada n'est pas enregistré, et l'enregistrement du TCF
Québec a expiré fin 2021. Attention aux offres de Mon Compte Formation, souvent des forfaits
préparation plus examen bien plus chers que l'examen seul."""),
],
"also": [
("/blog/cpf-test-francais/", "Quels tests de français le CPF finance en 2026",
 "Version par version : ce qui est enregistré, ce qui ne l'est plus, et jusqu'à quand."),
("/blog/difference-tcf-tef/", "TCF ou TEF : toutes les versions comparées",
 "Les neuf versions, leurs formats et leurs échelles — pour choisir la bonne avant de payer."),
("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?",
 "Les tables de conversion NCLC, le comparatif de format et le piège de l'« ancien score »."),
("/tcf-quebec/", "TCF Québec : le test modulaire",
 "La version où l'on ne paie que les épreuves dont on a besoin."),
],
"sources": """<strong>Ces prix changent.</strong> Les tarifs cités ont été relevés en juillet 2026
sur les sites des centres eux-mêmes, et plusieurs centres précisent qu'ils sont modifiables sans
préavis. Ils sont donnés à titre indicatif et non comme un barème : demandez systématiquement
le tarif en vigueur au centre où vous comptez vous inscrire.""",
},

# ─────────────────────────────────────────────────────────────────────────────
{
"slug": "cpf-test-francais",
"title": "Quels tests de français le CPF finance en 2026",
"desc": "Seules deux versions du TCF sont finançables par le compte personnel de formation. Le tableau des enregistrements, leurs dates d'expiration et le piège des forfaits.",
"og_title": "Quels tests de français le CPF finance en 2026",
"og_desc": "Seules deux versions du TCF sont finançables par le CPF. Les enregistrements, leurs dates d'expiration et le piège des forfaits Mon Compte Formation.",
"crumb": "Le CPF et les tests de français",
"h1": "Quels tests de français le CPF finance vraiment",
"date_fr": "7 août 2026",
"read": 6,
"accent": "accent-tcf",
"intro": """La réponse tient en une condition : le test doit être <strong>enregistré au
répertoire spécifique</strong> de France compétences. Sur les quatre versions du TCF,
<strong>deux seulement</strong> le sont — le TCF Tout Public et le TCF IRN. Le TCF Canada n'a
jamais été enregistré, et l'enregistrement du TCF Québec a expiré fin 2021.""",
"facts": [
"Condition unique : l'<strong>enregistrement au répertoire spécifique</strong> de France compétences.",
"✅ <strong>TCF Tout Public</strong> — fiche RS6460, jusqu'au <strong>21 décembre 2026</strong>.",
"✅ <strong>TCF IRN</strong> — fiche RS6643, jusqu'au <strong>31 mai 2027</strong>.",
"❌ <strong>TCF Québec</strong> — fiche RS1646, <strong>expirée fin 2021</strong>.",
"❌ <strong>TCF Canada</strong> — <strong>non enregistrée</strong>.",
"⚠️ L'enregistrement porte sur le <strong>test complet</strong> : la formule « 3 QCM » n'est pas finançable.",
],
"toc": [
("condition", "La condition unique : le répertoire spécifique"),
("tableau", "Version par version, ce qui est finançable"),
("complet", "L'enregistrement porte sur le test complet"),
("forfaits", "Le piège des forfaits Mon Compte Formation"),
("double", "Le répertoire compte deux fois"),
("expirations", "Les dates d'expiration à surveiller"),
],
"body": """
<h2 id="condition">La condition unique : le répertoire spécifique</h2>

<p>Pour mobiliser votre compte personnel de formation sur une certification, celle-ci doit être
<strong>enregistrée au répertoire spécifique</strong> tenu par France compétences. C'est une
condition binaire : sans enregistrement actif, aucun financement CPF n'est possible, quel que
soit le sérieux du test ou du centre.</p>

<p>Cet enregistrement porte un numéro de fiche — de la forme <strong>RS suivi de quatre
chiffres</strong> — et, surtout, une <strong>date d'expiration</strong>. C'est ce second point que
presque personne ne vérifie, et il explique l'essentiel des mauvaises surprises : une version
finançable il y a deux ans peut ne plus l'être aujourd'hui.</p>

<h2 id="tableau">Version par version, ce qui est finançable</h2>

<div class="tablewrap">
<table>
<caption>Enregistrement au répertoire spécifique de France compétences, consulté fin juillet 2026. Sans enregistrement actif, pas de financement CPF.</caption>
<thead><tr><th>Version</th><th>Fiche</th><th>Éligible au CPF</th></tr></thead>
<tbody>
<tr><td><strong>TCF Tout Public</strong></td><td>RS6460, jusqu'au 21 décembre 2026</td><td><strong>oui</strong></td></tr>
<tr><td><strong><a href="/tcf-irn/">TCF IRN</a></strong></td><td>RS6643, jusqu'au 31 mai 2027</td><td><strong>oui</strong></td></tr>
<tr><td><a href="/tcf-quebec/">TCF Québec</a></td><td>RS1646, <strong>expirée fin 2021</strong></td><td>non</td></tr>
<tr><td><a href="/tcf-canada/">TCF Canada</a></td><td>non enregistrée</td><td>non</td></tr>
</tbody>
</table>
</div>

<p>Le constat est net et il a une conséquence financière directe : <strong>si votre projet est
l'immigration canadienne, votre test n'est pas finançable</strong>. Le TCF Canada, obligatoire
pour Entrée express avec le TEF Canada, ne figure pas au répertoire. Il faudra donc le financer
sur vos fonds propres — un point à intégrer au budget d'un dossier qui coûte déjà cher.</p>

<p>À l'inverse, si votre démarche est française — naturalisation, carte de résident, carte de
séjour —, le <a href="/tcf-irn/">TCF IRN</a> est enregistré, et c'est une vraie économie sur un
test facturé entre 135 et 220 € selon le centre.</p>

<div class="note">
<p><strong>Le cas du TEF.</strong> Un « TEF tout public » a longtemps existé et reste vendu par
certains centres, mais il ne figure plus dans les déclinaisons officielles et son enregistrement
au répertoire de France compétences a <strong>expiré fin 2021</strong>. Pour les autres versions
du TEF, vérifiez la fiche en vigueur sur France compétences au moment de votre inscription plutôt
que de vous fier à une page commerciale.</p>
</div>

<h2 id="complet">L'enregistrement porte sur le test complet</h2>

<p>Voici une subtilité qui coûte cher aux candidats du TCF Tout Public. France Éducation
international indique qu'il <strong>n'est pas possible de mobiliser son CPF pour un test
incomplet</strong>. Or le TCF Tout Public se vend en deux formules : les trois QCM obligatoires
seuls, ou le test complet avec les expressions écrite et orale.</p>

<p>Conséquence : <strong>la formule « trois QCM » n'est pas finançable</strong>. Le prix d'appel
à 80 ou 110 € que vous voyez annoncé sort donc du champ du CPF, et le test finançable est la
version complète, à 185–260 € selon le centre. C'est une bonne nouvelle déguisée — la formule
courte ne convient de toute façon pas aux démarches qui exigent une preuve d'expression.</p>

<h2 id="forfaits">Le piège des forfaits Mon Compte Formation</h2>

<div class="note">
<p><strong>Les offres visibles sur Mon Compte Formation ne sont pas comparables aux prix des
centres.</strong> Beaucoup sont des <strong>forfaits préparation + examen</strong> : on rencontre
par exemple <strong>430 €</strong> pour un TCF IRN accompagné de 14 heures de préparation, contre
<strong>155 à 180 €</strong> pour l'examen seul ailleurs. Ce ne sont pas les mêmes produits.</p>
</div>

<p>Cela ne veut pas dire que ces forfaits sont mauvais : quatorze heures d'accompagnement ont une
valeur réelle, surtout pour un candidat qui part de loin. Mais il faut savoir ce que l'on achète.
Avant de valider, posez-vous deux questions : <strong>ai-je besoin de la préparation, ou
seulement du test ?</strong> Et <strong>quelle part du forfait couvre réellement l'examen ?</strong></p>

<p>Si vous êtes déjà proche du niveau visé, l'examen seul dans un centre bon marché, complété par
un entraînement autonome — <a href="/examens-blancs/">examens blancs au format officiel</a> et
<a href="/correction-ia/">correction de vos productions</a> —, revient nettement moins cher, même
en payant de votre poche.</p>

<h2 id="double">Le répertoire compte deux fois</h2>

<p>C'est le point que presque aucune source ne relie, et il est important. Le répertoire
spécifique ne sert pas seulement à débloquer un financement : il conditionne aussi la
<strong>recevabilité administrative</strong> de votre test.</p>

<p>L'arrêté du 22 décembre 2025, qui encadre les certifications acceptées pour les titres de
séjour, prévoit qu'au-delà du niveau atteint, la certification doit notamment être
<strong>enregistrée au répertoire spécifique</strong>. Autrement dit, un test non enregistré est
non seulement non finançable, mais potentiellement <strong>non recevable</strong> pour votre
dossier.</p>

<div class="note">
<p><strong>La conséquence pratique.</strong> Avant d'acheter un test de français en ligne —
particulièrement auprès d'un opérateur que vous ne connaissez pas —, vérifiez son enregistrement
au répertoire spécifique. C'est le même contrôle qui vous dit s'il est finançable et s'il sera
accepté. Deux minutes de vérification contre le risque de payer un test inutilisable.</p>
</div>

<h2 id="expirations">Les dates d'expiration à surveiller</h2>

<p>Les enregistrements ne sont pas éternels et ne sont pas toujours renouvelés — l'exemple du TCF
Québec, dont la fiche a expiré fin 2021 sans reconduction, le montre bien.</p>

<p>Deux échéances sont à connaître aujourd'hui :</p>

<ul>
<li><strong>TCF Tout Public — 21 décembre 2026.</strong> Si vous comptez financer ce test par le
CPF, ne repoussez pas indéfiniment : l'échéance est dans les mois qui viennent.</li>
<li><strong>TCF IRN — 31 mai 2027.</strong> Plus de marge, mais la même logique s'applique.</li>
</ul>

<p>Ces dates sont celles relevées fin juillet 2026. Un enregistrement peut être renouvelé — comme
il peut ne pas l'être. <strong>Vérifiez la fiche en vigueur sur France compétences au moment de
monter votre dossier</strong>, pas au moment où vous lisez cet article.</p>
""",
"cta_h2": "Ne financez pas un test que vous n'êtes pas prêt à réussir",
"cta_p": """Le CPF paie l'inscription, pas la seconde tentative. Examens blancs chronométrés au
format officiel, notation sur l'échelle du test visé, correction IA de l'écrit et de l'oral sur
les critères officiels — pour arriver au test en sachant déjà votre niveau. Dans l'app
«&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Le TCF est-il finançable par le CPF ?",
 """Deux versions le sont : le TCF Tout Public, fiche RS6460 valable jusqu'au 21 décembre 2026, et
le TCF IRN, fiche RS6643 valable jusqu'au 31 mai 2027. Le TCF Canada n'est pas enregistré au
répertoire spécifique et l'enregistrement du TCF Québec a expiré fin 2021 : ni l'un ni l'autre
n'est finançable."""),
("Le TCF Canada est-il finançable par le CPF ?",
 """Non. Le TCF Canada n'est pas enregistré au répertoire spécifique de France compétences, ce qui
est la condition nécessaire pour mobiliser le compte personnel de formation. Un candidat à
l'immigration canadienne doit donc financer son test sur ses fonds propres."""),
("Puis-je financer la formule « 3 QCM » du TCF Tout Public ?",
 """Non. France Éducation international indique qu'il n'est pas possible de mobiliser son CPF pour
un test incomplet. Seule la version complète, avec les épreuves d'expression, est finançable —
soit 185 à 260 € selon le centre, et non le prix d'appel à 80 ou 110 €."""),
("Pourquoi les prix sur Mon Compte Formation sont-ils plus élevés ?",
 """Parce que ce sont souvent des forfaits préparation + examen, et non l'examen seul. On rencontre
par exemple 430 € pour un TCF IRN accompagné de 14 heures de préparation, contre 155 à 180 € pour
l'examen seul dans un centre. Ce ne sont pas les mêmes produits : vérifiez ce que couvre
réellement l'offre avant de valider."""),
("Comment vérifier qu'un test est bien enregistré ?",
 """Cherchez son numéro de fiche — de la forme RS suivi de quatre chiffres — sur le site de France
compétences, et regardez surtout la date d'expiration. C'est le point que presque personne ne
vérifie, et il explique l'essentiel des mauvaises surprises : une version finançable il y a deux
ans peut ne plus l'être aujourd'hui."""),
("L'enregistrement sert-il à autre chose qu'au financement ?",
 """Oui, et c'est un point rarement relié. L'arrêté du 22 décembre 2025 prévoit qu'au-delà du
niveau atteint, une certification doit notamment être enregistrée au répertoire spécifique pour
être recevable dans un dossier de titre de séjour. Un test non enregistré est donc non seulement
non finançable, mais potentiellement non recevable."""),
],
"also": [
("/blog/prix-tcf-tef/", "Combien coûte vraiment le TCF ou le TEF ?",
 "Les prix relevés centre par centre en France et au Canada, et le piège du prix d'appel."),
("/tcf-irn/", "TCF IRN : le test de français pour votre naturalisation",
 "La version finançable la plus utile pour une démarche française."),
("/blog/tcf-irn-ou-tef-irn/", "TCF IRN ou TEF IRN : lequel choisir ?",
 "Les deux tests de naturalisation comparés, format, prix et financement."),
("/blog/b1-ou-b2-nationalite-francaise/", "B1 ou B2 pour la nationalité française ?",
 "Quel niveau pour quelle démarche, avant de choisir quel test financer."),
],
"sources": """<strong>Les enregistrements expirent.</strong> Les fiches et dates citées ont été
relevées fin juillet 2026 sur le répertoire spécifique de France compétences. Un enregistrement
peut être renouvelé comme il peut ne pas l'être — vérifiez la fiche en vigueur au moment de monter
votre dossier de financement, et non à la date de lecture de cet article.""",
},

]

if __name__ == "__main__":
    print("Batch 1 :")
    build(ARTICLES)
