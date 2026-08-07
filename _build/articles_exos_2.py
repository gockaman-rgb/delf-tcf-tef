#!/usr/bin/env python3
"""Cluster « exercices » — expression TCF Canada, TCF IRN, TEF Canada, DELF B2,
Structures de la langue.

Échantillons réels des banques de l'app, avec leurs corrigés d'origine.

⚠️ Deux garde-fous d'exactitude :
 · EE TCF Canada — sujets sans nombre de mots dans l'énoncé (filtre
   `embedsWordCount`), présentés avec les fenêtres Canada 60-120/120-150/120-180.
 · TCF IRN EE — aucune borne de mots officielle publiée : on n'en annonce
   aucune, seulement la durée de 30 min.
"""

from article_template import build

def exo(n, niveau, source_label, source, question, options, bonne, expl):
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

def sujet(titre, meta, consigne, conseil):
    return f"""
<div class="note">
<p><strong>{titre}</strong> — <em>{meta}</em></p>
<p>{consigne}</p>
</div>
<div class="faq"><details><summary>Ce que le correcteur attend</summary>
<p>{conseil}</p></details></div>
"""

ARTICLES = [

# ═══════════════════════════════════════════ 3. EE TCF CANADA
{
"slug": "sujets-expression-ecrite-tcf-canada",
"title": "Expression écrite TCF Canada : les 3 sujets types",
"desc": "Trois tâches en 60 minutes, de 60-120 à 120-180 mots. Un sujet type par tâche, ce que le correcteur attend et la répartition du temps qui évite de bâcler la troisième.",
"og_title": "Expression écrite TCF Canada : les 3 sujets types",
"og_desc": "Trois tâches en 60 minutes, de 60-120 à 120-180 mots. Un sujet type par tâche et ce que le correcteur attend.",
"crumb": "Expression écrite TCF Canada",
"h1": "Expression écrite du TCF Canada : les trois tâches, avec sujets types",
"date_fr": "7 août 2026",
"read": 8,
"accent": "accent-tcf",
"intro": """<strong>Trois tâches en 60 minutes</strong>, de longueurs croissantes : un message de
<strong>60-120 mots</strong>, un article ou récit de <strong>120-150</strong>, puis une comparaison
de deux points de vue avec avis argumenté de <strong>120-180</strong>. La troisième est celle qui
décide de votre note — et celle que les candidats bâclent, faute d'avoir géré le temps.""",
"facts": [
"<strong>3 tâches · 60 minutes au total</strong>, notées sur <strong>20</strong>.",
"<strong>Tâche 1</strong> : message · <strong>60-120 mots</strong>.",
"<strong>Tâche 2</strong> : article ou récit · <strong>120-150 mots</strong>.",
"<strong>Tâche 3</strong> : comparaison de deux points de vue + avis argumenté · <strong>120-180 mots</strong>.",
"⚠️ Les fourchettes ne sont pas indicatives : écrire en dessous coûte des points de conformité.",
"<strong>NCLC 7</strong> demande <strong>10/20</strong> — la frontière se joue souvent sur la tâche 3.",
],
"toc": [
("format", "Les trois tâches"),
("sujets", "Un sujet type par tâche"),
("temps", "Répartir les 60 minutes"),
("criteres", "Ce qui est évalué"),
("erreurs", "Les erreurs qui coûtent le plus"),
],
"body": """
<h2 id="format">Les trois tâches</h2>

<div class="tablewrap">
<table>
<caption>Expression écrite du TCF Canada. Source : France Éducation international, structure vérifiée en juillet 2026.</caption>
<thead><tr><th>Tâche</th><th>Genre</th><th>Longueur</th></tr></thead>
<tbody>
<tr><td><strong>1</strong></td><td>Message</td><td><strong>60 à 120 mots</strong></td></tr>
<tr><td><strong>2</strong></td><td>Article ou récit</td><td><strong>120 à 150 mots</strong></td></tr>
<tr><td><strong>3</strong></td><td>Comparaison de deux points de vue, avec avis argumenté</td><td><strong>120 à 180 mots</strong></td></tr>
<tr><td colspan="2"><strong>Total</strong></td><td><strong>60 minutes</strong></td></tr>
</tbody>
</table>
</div>

<p>Les trois tâches montent en exigence : la première relève de la communication courante, la
deuxième de la narration structurée, la troisième de l'argumentation. Et comme les points sont
répartis sur l'ensemble, <strong>bâcler la tâche 3 plafonne mécaniquement votre note</strong>.</p>

<div class="note">
<p><strong>Ces fourchettes sont propres au TCF Canada.</strong> Ne vous entraînez pas sur des
sujets de TCF Tout Public sans ajuster : les longueurs demandées y sont différentes. Un texte
calibré pour un autre format sera pénalisé sur la conformité à la consigne, quelle que soit la
qualité de la langue.</p>
</div>

<h2 id="sujets">Un sujet type par tâche</h2>

""" + sujet("Tâche 1 — Message", "60 à 120 mots · registre à adapter au destinataire",
"Vous avez acheté un produit en ligne mais il est arrivé abîmé. Écrivez un email au service client "
"pour expliquer le problème, décrire le défaut et demander un échange ou un remboursement.",
"<strong>Trois actions sont demandées : expliquer, décrire, demander.</strong> Le correcteur "
"vérifie que les trois sont présentes — c'est le critère de conformité, et il se perd sans "
"faute de langue. Ajoutez les conventions du genre : objet, formule d'appel, formule de "
"politesse. Le registre attendu ici est <em>formel</em> : « je vous écris », pas « je vous "
"écris pour vous dire que »."
) + sujet("Tâche 2 — Article ou récit", "120 à 150 mots · narration structurée",
"Le maire de votre ville souhaite recueillir l'avis des habitants sur les transports en commun. "
"Écrivez une lettre au maire pour donner votre avis : ce qui fonctionne bien, ce qui doit être "
"amélioré, et vos propositions.",
"Là encore, <strong>trois volets explicites</strong> : le positif, le négatif, les propositions. "
"Un plan en trois paragraphes suit la consigne et vous évite de réfléchir à l'organisation. "
"L'erreur classique est de consacrer 100 mots aux critiques et 10 aux propositions — le "
"déséquilibre est visible et sanctionné. Registre formel, destinataire institutionnel."
) + sujet("Tâche 3 — Comparaison et avis argumenté", "120 à 180 mots · l'épreuve dans l'épreuve",
"Le gouvernement propose de rendre le vote obligatoire en France pour lutter contre l'abstention. "
"Écrivez un essai argumentatif pour exprimer votre position sur cette proposition. Présentez des "
"arguments pour et contre, puis donnez votre avis personnel en le justifiant.",
"<strong>La structure est imposée par la consigne : pour, contre, puis votre position.</strong> "
"Sauter la partie « contre » est l'erreur la plus fréquente et la plus coûteuse — c'est "
"précisément la compétence B2 évaluée. En 180 mots maximum, comptez environ 50 mots par "
"argument adverse, 50 pour le vôtre, et 40 pour trancher. Les connecteurs font le reste : "
"« certes… toutefois », « d'une part… d'autre part »."
) + """

<h2 id="temps">Répartir les 60 minutes</h2>

<p>C'est là que tout se joue. La tâche 3 est la plus longue et la plus exigeante, et elle arrive
en dernier : sans répartition décidée à l'avance, elle est écrite dans l'urgence.</p>

<div class="tablewrap">
<table>
<caption>Une répartition qui protège la tâche 3.</caption>
<thead><tr><th>Temps</th><th>Tâche</th><th>Ce que vous faites</th></tr></thead>
<tbody>
<tr><td><strong>0 – 12 min</strong></td><td>Tâche 1</td><td>Rédiger et relire. Ne pas dépasser : c'est la tâche la moins rentable.</td></tr>
<tr><td><strong>12 – 32 min</strong></td><td>Tâche 2</td><td>Plan en 3 paragraphes, puis rédaction.</td></tr>
<tr><td><strong>32 – 55 min</strong></td><td>Tâche 3</td><td>5 min de plan, 18 min de rédaction.</td></tr>
<tr><td><strong>55 – 60 min</strong></td><td>Les trois</td><td>Compter les mots, vérifier les formules d'appel et de politesse.</td></tr>
</tbody>
</table>
</div>

<p><strong>Le piège de la tâche 1.</strong> Elle est facile, donc on la soigne — et on y passe
vingt minutes. C'est du temps pris à la tâche 3, qui vaut davantage. Un message correct en douze
minutes suffit largement.</p>

<h2 id="criteres">Ce qui est évalué</h2>

<ul>
<li><strong>La conformité à la consigne.</strong> Le premier critère, et le plus mécanique : les
actions demandées sont-elles toutes traitées ? Le genre est-il respecté ?</li>
<li><strong>Le volume.</strong> Les fourchettes sont des <strong>planchers et des plafonds</strong>.
En dessous du minimum, la consigne n'est pas remplie ; très au-dessus du maximum, la capacité de
synthèse est prise en défaut.</li>
<li><strong>La cohérence et la cohésion.</strong> Un plan lisible, des connecteurs explicites. À
ce niveau, c'est le marqueur le plus visible.</li>
<li><strong>Le lexique et la grammaire.</strong> Évalués, mais moins discriminants que les trois
premiers points : un texte correct mais hors consigne perd plus qu'un texte bien construit avec
quelques fautes.</li>
<li><strong>Le registre.</strong> Un message à un ami et une lettre à un maire ne s'écrivent pas
pareil. Le glissement au familier dans un courrier institutionnel est immédiatement visible.</li>
</ul>

<h2 id="erreurs">Les erreurs qui coûtent le plus</h2>

<ol>
<li><strong>Ne pas compter ses mots.</strong> L'estimation à l'œil est presque toujours optimiste.
Comptez réellement, au moins sur la tâche 3.</li>
<li><strong>Omettre la partie adverse en tâche 3.</strong> C'est la compétence évaluée : donner
son avis sans avoir présenté le point de vue opposé, c'est répondre à côté.</li>
<li><strong>Négliger les conventions du genre.</strong> Une lettre sans formule d'appel ni formule
de politesse perd des points avant l'évaluation de la langue.</li>
<li><strong>Traiter deux des trois actions demandées.</strong> Relisez la consigne à la fin :
chaque verbe d'action y est un point à cocher.</li>
<li><strong>Passer trop de temps sur la tâche 1.</strong> Elle est courte et facile ; elle ne
justifie pas le tiers de l'épreuve.</li>
</ol>

<div class="note">
<p><strong>Pourquoi cette épreuve est difficile à préparer seul.</strong> Vous ne pouvez pas
juger si votre argumentation est réellement équilibrée, ni si votre registre a glissé — ce sont
les défauts invisibles de l'intérieur. Et savoir si vous écrivez à 9 ou à 11 sur 20, c'est savoir
si vous avez NCLC 6 ou NCLC 7 : <a href="/correction-ia/">une correction sur les critères
officiels</a> est le seul moyen de le mesurer.</p>
</div>
""",
"cta_h2": "Savoir si votre tâche 3 vaut 9 ou 11 sur 20",
"cta_p": """Des centaines de sujets d'expression écrite au format exact du TCF Canada, avec les
fenêtres de mots officielles par tâche, chronomètre réel et correction IA sur les critères
officiels — conformité, cohérence, lexique, grammaire. Dans l'app
«&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Combien de mots faut-il écrire à l'expression écrite du TCF Canada ?",
 """Trois tâches de longueurs croissantes : 60 à 120 mots pour le message, 120 à 150 pour l'article
ou récit, 120 à 180 pour la comparaison de deux points de vue avec avis argumenté. Ces fourchettes
sont des planchers et des plafonds, pas des indications."""),
("Combien de temps dure l'épreuve ?",
 """60 minutes pour les trois tâches. Une répartition qui fonctionne : 12 minutes pour la tâche 1,
20 pour la tâche 2, 23 pour la tâche 3 et 5 minutes de vérification finale. Le piège est de soigner
la tâche 1, facile, au détriment de la tâche 3, qui vaut davantage."""),
("Quelle est la tâche la plus importante ?",
 """La tâche 3, la comparaison de deux points de vue avec avis argumenté. C'est elle qui mobilise la
compétence B2 et qui fait la différence entre 10 et 14 sur 20 — donc entre NCLC 7 et NCLC 8. Sauter
la présentation du point de vue adverse est l'erreur la plus coûteuse de l'épreuve."""),
("Que se passe-t-il si j'écris moins que le minimum ?",
 """Vous perdez des points sur la conformité à la consigne, indépendamment de la qualité de votre
langue. C'est un critère mécanique que le correcteur applique avant même d'évaluer le lexique et la
grammaire. Comptez réellement vos mots plutôt que de les estimer."""),
("Peut-on s'entraîner sur des sujets de TCF Tout Public ?",
 """Avec précaution : les longueurs demandées ne sont pas les mêmes. Un texte calibré pour un autre
format sera pénalisé sur la conformité. Si vous utilisez de tels sujets, imposez-vous les fenêtres
du TCF Canada — 60-120, 120-150 et 120-180 mots."""),
("Quel score faut-il en expression écrite pour NCLC 7 ?",
 """10 sur 20. La note d'expression est sur 20, contrairement aux compréhensions qui sont sur 699.
NCLC 7 correspond à 10-11 sur 20, NCLC 8 à 12-13. Un seul point peut donc faire changer de
niveau."""),
],
"also": [
("/blog/sujets-expression-orale-tcf-canada/", "Expression orale TCF Canada : les 3 tâches",
 "L'autre épreuve d'expression, en 12 minutes seulement."),
("/blog/exercices-comprehension-ecrite-tcf-canada/", "Exercices de compréhension écrite TCF Canada",
 "39 QCM en 60 minutes, corrigés et expliqués."),
("/correction-ia/", "La correction IA de l'écrit et de l'oral",
 "Comment vos productions sont notées sur les critères officiels."),
("/tcf-canada/", "TCF Canada : format, scores NCLC et préparation",
 "Le guide complet des quatre épreuves."),
],
"sources": """<strong>Les formats évoluent.</strong> Cette page est à jour au 7 août 2026. Les
sujets présentés sont des contenus originaux de notre application, conçus au format officiel — il
n'existe aucune annale officielle du TCF en accès libre. Vérifiez la structure en vigueur sur
<a href="https://www.france-education-international.fr/test/tcf-canada" target="_blank" rel="noopener">france-education-international.fr</a>
avant votre session.""",
},

# ═══════════════════════════════════════════ 4. EO TCF CANADA
{
"slug": "sujets-expression-orale-tcf-canada",
"title": "Expression orale TCF Canada : les 3 tâches",
"desc": "Trois tâches en 12 minutes seulement, dont 2 minutes de préparation. Les sujets types de chaque tâche, ce que le jury attend et la gestion du temps qui évite de bâcler la fin.",
"og_title": "Expression orale TCF Canada : les 3 tâches",
"og_desc": "Trois tâches en 12 minutes, dont 2 de préparation. Les sujets types, ce que le jury attend et la gestion du temps.",
"crumb": "Expression orale TCF Canada",
"h1": "Expression orale du TCF Canada : les trois tâches, avec sujets types",
"date_fr": "7 août 2026",
"read": 7,
"accent": "accent-tcf",
"intro": """<strong>Trois tâches en 12 minutes</strong>, en face à face, dont seulement
<strong>2 minutes de préparation</strong> pour la deuxième. C'est l'épreuve la plus courte du TCF
Canada — et la plus mal gérée : les candidats non entraînés consomment leur temps sur la tâche 1,
la plus facile, et bâclent la tâche 3, celle qui rapporte le plus.""",
"facts": [
"<strong>3 tâches · 12 minutes au total</strong>, en face à face, notées sur <strong>20</strong>.",
"<strong>Tâche 1</strong> : entretien dirigé — <strong>sans préparation</strong>.",
"<strong>Tâche 2</strong> : exercice en interaction — <strong>2 minutes de préparation</strong>.",
"<strong>Tâche 3</strong> : expression d'un point de vue à partir d'un document.",
"⚠️ La tâche 1 est <strong>prévisible</strong> : elle se prépare mot pour mot à l'avance.",
"<strong>NCLC 7</strong> demande <strong>10/20</strong> en expression orale.",
],
"toc": [
("format", "Les trois tâches"),
("sujets", "Un sujet type par tâche"),
("temps", "Gérer douze minutes"),
("criteres", "Ce que le jury évalue"),
("erreurs", "Les erreurs qui coûtent le plus"),
],
"body": """
<h2 id="format">Les trois tâches</h2>

<div class="tablewrap">
<table>
<caption>Expression orale du TCF Canada. Source : France Éducation international, structure vérifiée en juillet 2026.</caption>
<thead><tr><th>Tâche</th><th>Nature</th><th>Préparation</th></tr></thead>
<tbody>
<tr><td><strong>1</strong></td><td>Entretien dirigé — vous vous présentez, l'examinateur relance</td><td><strong>aucune</strong></td></tr>
<tr><td><strong>2</strong></td><td>Exercice en interaction — situation à résoudre</td><td><strong>2 minutes</strong></td></tr>
<tr><td><strong>3</strong></td><td>Expression d'un point de vue à partir d'un document</td><td>—</td></tr>
<tr><td colspan="2"><strong>Total</strong></td><td><strong>12 minutes</strong>, préparation comprise</td></tr>
</tbody>
</table>
</div>

<p>Douze minutes pour trois tâches, c'est très court : environ trois à quatre minutes de parole
par tâche. La contrainte n'est donc pas de tenir la durée, c'est d'être <strong>immédiatement
productif</strong> — un candidat qui met une minute à démarrer a perdu un quart de sa tâche.</p>

<h2 id="sujets">Un sujet type par tâche</h2>

""" + sujet("Tâche 1 — Entretien dirigé", "sans préparation · l'échauffement, à sécuriser",
"Présentez-vous : votre nom, votre âge, votre nationalité, votre situation familiale et votre "
"métier ou vos études.",
"<strong>C'est la tâche la plus rentable de toute votre préparation</strong>, parce qu'elle est "
"entièrement prévisible. Préparez et répétez à voix haute une présentation de 60 à 90 secondes, "
"puis anticipez les relances classiques : pourquoi apprenez-vous le français, quel est votre "
"projet au Canada, depuis combien de temps étudiez-vous. Le jury évalue ici surtout la fluidité "
"et la prononciation — pas la profondeur des idées. Ne récitez pas de façon mécanique : "
"apprenez la structure, pas le texte."
) + sujet("Tâche 2 — Exercice en interaction", "2 minutes de préparation · une situation à résoudre",
"Racontez un voyage ou une visite que vous avez fait(e) en France. Décrivez l'endroit, ce que vous "
"avez fait, ce qui vous a plu et ce qui vous a moins plu. Expliquez pourquoi vous recommanderiez "
"ou non cet endroit.",
"Les deux minutes de préparation servent à noter des <strong>mots-clés, pas des phrases</strong>. "
"Un candidat qui rédige puis lit ses notes est immédiatement repérable et pénalisé sur la "
"fluidité. La consigne contient ici quatre éléments — décrire, raconter, nuancer, recommander : "
"traitez-les tous, dans cet ordre, c'est votre plan tout fait. Les temps du passé (passé "
"composé et imparfait) sont le point grammatical le plus observé sur ce type de tâche."
) + sujet("Tâche 3 — Expression d'un point de vue", "à partir d'un document · la tâche qui rapporte le plus",
"<em>Document :</em> « Selon une étude récente, 65 % des Français estiment que l'immigration est "
"trop importante en France. Pourtant, les économistes soulignent que l'immigration contribue "
"positivement à la croissance économique et compense le vieillissement de la population. »<br>"
"Donnez votre avis argumenté sur ce décalage entre perception et réalité économique.",
"<strong>Ne résumez pas le document, exploitez-le.</strong> Le jury a le texte sous les yeux : "
"le paraphraser consomme votre temps sans rapporter de points. Attaquez directement par votre "
"position, puis argumentez. Ici, la consigne pointe un <em>décalage</em> : c'est lui qu'il faut "
"expliquer, pas l'immigration en général. Répondre à côté du sujet est la faute la plus "
"coûteuse, avant même la langue."
) + """

<h2 id="temps">Gérer douze minutes</h2>

<ul>
<li><strong>Démarrez immédiatement.</strong> Il n'y a pas de temps pour un silence de réflexion :
commencez par une phrase d'accroche préparée, elle vous donne trois secondes pour organiser la
suite.</li>
<li><strong>Ne surinvestissez pas la tâche 1.</strong> Elle est facile et rassurante, donc on
s'y installe. Une présentation de 90 secondes suffit ; le reste du temps appartient aux tâches 2
et 3.</li>
<li><strong>Utilisez vos deux minutes de préparation</strong> pour la tâche 2 : trois ou quatre
mots-clés dans l'ordre du plan, rien de plus.</li>
<li><strong>Gardez de l'énergie pour la tâche 3.</strong> C'est la plus exigeante, et elle arrive
en dernier, au moment où la fatigue et le stress sont maximaux.</li>
<li><strong>Acceptez les relances.</strong> L'examinateur qui vous interrompt ou vous contredit
ne vous sanctionne pas : il teste votre capacité à réagir. Céder immédiatement coûte des
points.</li>
</ul>

<h2 id="criteres">Ce que le jury évalue</h2>

<div class="tablewrap">
<table>
<caption>Les critères d'évaluation de l'expression orale.</caption>
<thead><tr><th>Critère</th><th>Ce que cela signifie concrètement</th></tr></thead>
<tbody>
<tr><td><strong>Contenu</strong></td><td>Avez-vous traité tous les éléments de la consigne ?</td></tr>
<tr><td><strong>Vocabulaire</strong></td><td>Étendue et précision, pas rareté des mots</td></tr>
<tr><td><strong>Grammaire</strong></td><td>Temps du passé, accords, structures complexes</td></tr>
<tr><td><strong>Cohérence</strong></td><td>Un plan audible, des connecteurs explicites</td></tr>
<tr><td><strong>Prononciation</strong></td><td>Intelligibilité, rythme, intonation</td></tr>
</tbody>
</table>
</div>

<p>Notez que <strong>la prononciation est un critère à part entière</strong>, et c'est celui que
les candidats préparent le moins. Un discours riche mais difficile à suivre plafonne : le jury
évalue ce qu'il comprend, pas ce que vous vouliez dire.</p>

<h2 id="erreurs">Les erreurs qui coûtent le plus</h2>

<ol>
<li><strong>Réciter la tâche 1.</strong> Une présentation apprise par cœur s'entend, et le jury
relance immédiatement hors du script. Apprenez la structure, pas les phrases.</li>
<li><strong>Rédiger pendant les deux minutes de préparation.</strong> Vous n'aurez pas le temps
de tout dire, et la lecture de notes se repère.</li>
<li><strong>Paraphraser le document en tâche 3.</strong> Le jury l'a sous les yeux. Attaquez par
votre position.</li>
<li><strong>Répondre à côté de la consigne.</strong> C'est la faute la plus coûteuse, et elle n'a
rien à voir avec le niveau de langue.</li>
<li><strong>Ne pas s'entraîner à voix haute.</strong> Préparer l'oral en lisant est le meilleur
moyen de découvrir le jour J qu'on ne tient pas trois minutes.</li>
</ol>
""",
"cta_h2": "L'oral ne se prépare pas en lisant",
"cta_p": """Des centaines de sujets d'expression orale au format exact du TCF Canada, avec
chronomètre et temps de préparation réels. Vous parlez, l'app transcrit et note — prononciation et
fluidité comprises — sur les critères officiels, autant de fois que nécessaire. Dans l'app
«&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Combien de temps dure l'expression orale du TCF Canada ?",
 """12 minutes au total pour les trois tâches, en face à face, dont 2 minutes de préparation pour la
deuxième tâche. C'est très court : comptez environ trois à quatre minutes de parole par tâche, sans
temps mort possible."""),
("En quoi consistent les trois tâches ?",
 """Un entretien dirigé où vous vous présentez et où l'examinateur relance, sans préparation ; un
exercice en interaction avec 2 minutes de préparation ; puis l'expression d'un point de vue à
partir d'un document déclencheur."""),
("Comment préparer la première tâche ?",
 """C'est la tâche la plus rentable de toute votre préparation, parce qu'elle est entièrement
prévisible. Répétez à voix haute une présentation de 60 à 90 secondes et anticipez les relances
classiques : pourquoi vous apprenez le français, votre projet, depuis quand vous étudiez. Apprenez
la structure, jamais le texte — une récitation s'entend."""),
("Que faire pendant les deux minutes de préparation ?",
 """Noter trois ou quatre mots-clés dans l'ordre de votre plan, rien de plus. Rédiger des phrases
est contre-productif : vous n'aurez pas le temps de tout dire, et la lecture de notes se repère
immédiatement et coûte des points sur la fluidité."""),
("Faut-il résumer le document de la tâche 3 ?",
 """Non. Le jury l'a sous les yeux : le paraphraser consomme votre temps sans rapporter de points.
Attaquez directement par votre position, puis argumentez — en répondant précisément à la question
posée, qui porte souvent sur un aspect particulier du document."""),
("Que faire si l'examinateur me contredit ?",
 """Tenez votre position en la nuançant. L'examinateur qui relance ou objecte ne vous sanctionne
pas : il teste votre capacité à réagir et à défendre un point de vue. Céder immédiatement à la
première objection coûte des points sur le critère de contenu."""),
],
"also": [
("/blog/sujets-expression-ecrite-tcf-canada/", "Expression écrite TCF Canada : les 3 sujets types",
 "L'autre épreuve d'expression, avec ses trois fenêtres de mots."),
("/correction-ia/", "La correction IA de l'écrit et de l'oral",
 "Vous parlez, l'app transcrit et note prononciation et fluidité comprises."),
("/tcf-canada/", "TCF Canada : format, scores NCLC et préparation",
 "Le guide complet des quatre épreuves et de la conversion NCLC."),
("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement",
 "10/20 en expression orale — et pourquoi un seul point change de niveau."),
],
"sources": """<strong>Les formats évoluent.</strong> Cette page est à jour au 7 août 2026. Les
sujets présentés sont des contenus originaux de notre application, conçus au format officiel — il
n'existe aucune annale officielle du TCF en accès libre. Vérifiez la structure en vigueur sur
<a href="https://www.france-education-international.fr/test/tcf-canada" target="_blank" rel="noopener">france-education-international.fr</a>
avant votre session.""",
},

# ═══════════════════════════════════════════ 5. TCF IRN
{
"slug": "exercices-tcf-irn",
"title": "Exercices TCF IRN : les 4 épreuves corrigées",
"desc": "1 h 35, quatre épreuves insécables et une échelle sur 499. Un exercice corrigé par épreuve, au niveau B2 exigé pour la naturalisation depuis 2026.",
"og_title": "Exercices TCF IRN : les 4 épreuves corrigées",
"og_desc": "1 h 35, quatre épreuves insécables, échelle sur 499. Un exercice corrigé par épreuve, au niveau B2 exigé depuis 2026.",
"crumb": "Exercices TCF IRN",
"h1": "Exercices du TCF IRN : les quatre épreuves, corrigées",
"date_fr": "7 août 2026",
"read": 8,
"accent": "accent-tcf",
"intro": """<strong>Quatre épreuves insécables en 1 h 35</strong>, notées sur une échelle de
<strong>499</strong> — et non sur 699. Depuis 2026, la naturalisation exige le <strong>B2</strong>,
c'est-à-dire un score entre <strong>400 et 499</strong> aux QCM et au moins <strong>10/20</strong>
aux expressions. Voici un exercice corrigé par épreuve, exactement à ce niveau.""",
"facts": [
"<strong>4 épreuves · 1 h 35</strong> : CO 25 QCM/20 min · CE 25 QCM/35 min · EE 30 min · EO 10 min.",
"⚠️ Noté sur <strong>499</strong>, pas sur 699 : votre B2 se joue entre <strong>400 et 499</strong>.",
"Épreuves <strong>insécables</strong> : on ne peut pas en passer une partie.",
"⚠️ <strong>Présentiel obligatoire</strong> — aucun test en ligne n'est recevable.",
"Naturalisation : <strong>B2</strong> · carte de résident : <strong>B1</strong> · carte pluriannuelle : <strong>A2</strong>.",
"Une seule écoute en compréhension orale, sans retour arrière.",
],
"toc": [
("format", "Le format des quatre épreuves"),
("exercices", "Un exercice corrigé par épreuve"),
("b2", "Viser le B2, concrètement"),
("methode", "La méthode de préparation"),
],
"body": """
<h2 id="format">Le format des quatre épreuves</h2>

<div class="tablewrap">
<table>
<caption>TCF IRN depuis la réforme du 12 mai 2025. Source : France Éducation international, structure vérifiée en juillet 2026.</caption>
<thead><tr><th>Épreuve</th><th>Contenu</th><th>Durée</th><th>Notation</th></tr></thead>
<tbody>
<tr><td>Compréhension orale</td><td>25 QCM</td><td>20 min</td><td>100–499</td></tr>
<tr><td>Compréhension écrite</td><td>25 QCM</td><td>35 min</td><td>100–499</td></tr>
<tr><td>Expression écrite</td><td>—</td><td>30 min</td><td>/20</td></tr>
<tr><td>Expression orale</td><td>—</td><td>10 min</td><td>/20</td></tr>
<tr><td colspan="2"><strong>Total</strong></td><td><strong>1 h 35</strong></td><td></td></tr>
</tbody>
</table>
</div>

<p>C'est un test nettement plus court que le <a href="/tcf-canada/">TCF Canada</a> (2 h 47),
parce qu'il ne vise pas les mêmes niveaux : il s'arrête au B2 là où le TCF Canada mesure jusqu'au
C2. Les 25 questions de compréhension orale en 20 minutes laissent environ
<strong>48 secondes par question</strong>.</p>

<h2 id="exercices">Un exercice corrigé par épreuve</h2>

<p>Les quatre exercices ci-dessous sont au <strong>niveau B2</strong> — celui exigé pour la
naturalisation depuis le 1<sup>er</sup> janvier 2026.</p>

""" + exo(1, "B2 — compréhension orale", "Ce que vous entendez — interview, 2 locuteurs :",
"« <strong>Intervieweur :</strong> Vous êtes spécialiste en psychologie organisationnelle. Comment "
"les entreprises peuvent-elles mieux gérer le télétravail ?<br>"
"<strong>Psychologue :</strong> Le télétravail a créé des défis uniques. Le sentiment d'isolement "
"affecte la productivité et le bien-être des employés. Les entreprises doivent créer des "
"structures pour maintenir la collaboration et la connexion sociale. Des réunions régulières, des "
"espaces virtuels informels et des jours de présence occasionnels en bureaux physiques aident à "
"renforcer la culture d'entreprise. »",
"Quel est le principal défi du télétravail identifié ?",
["Communication défaillante avec les clients", "Distractions fréquentes à la maison",
 "Technologie insuffisante au domicile", "Isolement affectant la productivité"],
"D — Isolement affectant la productivité",
"la psychologue nomme explicitement « le sentiment d'isolement » comme ce qui « affecte la "
"productivité et le bien-être ». Les trois autres options sont des difficultés <em>plausibles</em> "
"du télétravail, mais absentes du document : <strong>le plausible n'est pas le dit</strong>."
) + exo(2, "B2 — compréhension écrite", "Document — texte d'idées :",
"« Si Victor Hugo revenait parmi nous, il serait sans doute stupéfait de constater que la misère "
"qu'il dénonçait avec tant de force au XIX<sup>e</sup> siècle n'a pas disparu de France. Certes, "
"les formes ont changé : on ne meurt plus de faim dans les rues de Paris, et les enfants ne "
"travaillent plus dans les mines. Mais la pauvreté persiste, simplement elle a changé de visage. "
"Aujourd'hui, être pauvre en France, c'est souvent avoir un toit mais ne pas pouvoir le chauffer "
"correctement. C'est travailler mais ne pas gagner assez pour vivre dignement. »",
"Quel est le rôle de la référence à Victor Hugo dans ce texte ?",
["Dénoncer les inégalités sous l'Ancien Régime",
 "Établir une comparaison entre pauvres urbains et ruraux",
 "Illustrer la persistance de la misère sous des formes nouvelles",
 "Honorer un grand écrivain du XIX<sup>e</sup> siècle"],
"C — Illustrer la persistance de la misère sous des formes nouvelles",
"la question ne porte pas sur le contenu mais sur la <strong>fonction rhétorique</strong> d'un "
"élément du texte. C'est typiquement B2 : Victor Hugo n'est pas le sujet, il est l'instrument "
"d'une comparaison entre deux époques. L'option D est vraie au premier degré et fausse comme "
"réponse."
) + sujet("Expression écrite — 30 minutes", "contribution argumentée à un dossier",
"Un magazine lance un dossier sur le thème : « Les tiers-lieux (espaces de coworking, fab labs, "
"cafés associatifs) transforment-ils la vie sociale en France ? ». Écrivez votre contribution.",
"Le sujet demande une <strong>position argumentée</strong>, pas une description des tiers-lieux. "
"En 30 minutes, comptez 5 minutes de plan et 20 de rédaction. Structure attendue au B2 : "
"position claire d'entrée, deux arguments illustrés, prise en compte d'une objection, "
"conclusion. C'est la présence de l'objection qui distingue le B2 du B1 — sans elle, votre "
"texte reste une opinion juxtaposée."
) + sujet("Expression orale — 10 minutes", "opinion argumentée à partir d'un document · 3 min de préparation",
"<em>Document :</em> « De plus en plus de communes françaises instaurent des budgets "
"participatifs, permettant aux habitants de décider directement de l'affectation d'une partie du "
"budget municipal. Certains y voient un renouveau démocratique, d'autres s'inquiètent du manque "
"de compétence technique des citoyens pour prendre ces décisions. »<br>"
"Donnez votre avis argumenté sur les budgets participatifs.",
"Le document vous <strong>donne déjà les deux camps</strong> : ne les redécouvrez pas, "
"positionnez-vous. Les trois minutes de préparation servent à noter des mots-clés, pas des "
"phrases. Attaquez par votre position, traitez l'objection mentionnée dans le document, puis "
"concluez. Paraphraser le texte consomme votre temps sans rapporter de points."
) + """

<h2 id="b2">Viser le B2, concrètement</h2>

<div class="tablewrap">
<table>
<caption>Ce que vaut votre score au TCF IRN. Source : grille officielle des niveaux du TCF.</caption>
<thead><tr><th>Niveau</th><th>QCM</th><th>Expressions /20</th><th>Suffit pour</th></tr></thead>
<tbody>
<tr><td>A2</td><td>200–299</td><td>2–5</td><td>carte de séjour pluriannuelle</td></tr>
<tr><td>B1</td><td>300–399</td><td>6–9</td><td>carte de résident</td></tr>
<tr><td><strong>B2</strong></td><td><strong>400–499</strong></td><td><strong>10–13</strong></td><td><strong>naturalisation</strong></td></tr>
</tbody>
</table>
</div>

<div class="note">
<p><strong>L'erreur qu'on lit partout : « au TCF IRN, le B2 correspond à 500-599 ».</strong> C'est
faux — 500-599 correspond au C1, un niveau que le TCF IRN ne délivre même pas. Son échelle
s'arrête à 499 parce qu'il plafonne au B2. Nous détaillons ce point sur notre page
<a href="/tcf-irn/">TCF IRN</a>.</p>
</div>

<h2 id="methode">La méthode de préparation</h2>

<ol>
<li><strong>Un examen blanc complet dès le départ</strong>, avant toute révision, pour savoir où
vous en êtes sur les quatre épreuves. Les épreuves étant insécables, c'est votre note la plus
basse qui décide.</li>
<li><strong>Ciblez l'écrit argumenté en priorité.</strong> Beaucoup de candidats à la
naturalisation ont un oral fluide, acquis par des années en France, et un écrit resté au B1 —
faute d'avoir jamais eu à argumenter par écrit. C'est là que se perdent les dossiers.</li>
<li><strong>Entraînez-vous en une seule écoute.</strong> Réécouter « juste une fois » invalide la
mesure et vous prépare à un examen qui n'existe pas.</li>
<li><strong>Chronométrez.</strong> 48 secondes par question en compréhension orale, ce n'est pas
une contrainte théorique.</li>
<li><strong>Faites corriger vos expressions sur les critères officiels.</strong> Savoir si vous
écrivez à 9 ou à 11 sur 20, c'est savoir si vous avez le B2 ou non.</li>
</ol>

<div class="note">
<p><strong>Et l'examen civique ?</strong> Le TCF IRN ne couvre que la condition de langue. Depuis
2026, un examen civique s'ajoute au dossier — 40 questions, 32 bonnes réponses exigées. Notre app
sœur <a href="https://naturalisationfrancefacile.fr">Naturalisation France Facile</a> le prépare avec les thèmes officiels
en QCM expliqués — <a href="https://apps.apple.com/fr/app/naturalisation-france-facile/id6761140087">disponible sur l'App&nbsp;Store</a>.</p>
</div>
""",
"cta_h2": "Savoir si vous avez le B2 avant de payer votre test",
"cta_p": """Examens blancs au format exact du TCF IRN, notation sur l'échelle 499 avec niveau CECRL
par épreuve, exercices par compétence et correction IA de l'expression écrite et orale sur les
critères officiels. Dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Combien de questions y a-t-il au TCF IRN ?",
 """25 questions en compréhension orale (20 minutes) et 25 en compréhension écrite (35 minutes),
auxquelles s'ajoutent une épreuve d'expression écrite de 30 minutes et une expression orale de
10 minutes. Total : 1 h 35, en une seule session avec quatre épreuves insécables."""),
("Quel score faut-il au TCF IRN pour la naturalisation ?",
 """Le niveau B2, soit un score entre 400 et 499 aux QCM et au moins 10 sur 20 aux épreuves
d'expression. Attention : l'échelle du TCF IRN s'arrête à 499 parce que le test plafonne au B2 —
les sources qui annoncent 500-599 pour le B2 se trompent, cette bande correspond au C1."""),
("Le TCF IRN est-il noté sur 699 ?",
 """Non, sur 499. Comme le test plafonne au niveau B2 et que le B2 s'arrête à 499 sur la grille du
TCF, ses QCM sont notés de 100 à 499. Les pages officielles de France Éducation international
décrivent d'ailleurs encore un test plafonné au B1 et noté sur 399 : c'est la documentation qui n'a
pas suivi la réforme de mai 2025."""),
("Peut-on ne passer qu'une épreuve ?",
 """Non. Les quatre épreuves du TCF IRN sont officiellement décrites comme « insécables » : elles se
passent ensemble, le même jour. Il n'existe aucune reprise partielle non plus — en cas de score
insuffisant, c'est le test complet qu'il faut repasser."""),
("Quelle épreuve fait le plus échouer ?",
 """L'expression écrite. Beaucoup de candidats à la naturalisation ont un français oral fluide,
acquis par des années de vie en France, et un écrit resté au niveau B1 faute d'avoir jamais eu à
rédiger un texte argumenté. Votre aisance quotidienne ne prédit pas votre score."""),
("Peut-on passer le TCF IRN en ligne ?",
 """Non. L'arrêté du 22 décembre 2025 impose quatre épreuves distinctes passées en présentiel, le
même jour, en une session unique, avec surveillance anti-fraude et vérification d'identité. Les
tests passés en ligne depuis chez soi ne sont pas recevables pour un titre de séjour."""),
],
"also": [
("/tcf-irn/", "TCF IRN : le test de français pour votre naturalisation",
 "Le guide complet : échelle 499, présentiel obligatoire, prix et CPF."),
("/blog/b1-ou-b2-nationalite-francaise/", "B1 ou B2 pour la nationalité française ?",
 "Quel niveau pour quelle démarche, et comment le prouver."),
("/blog/tcf-irn-ou-tef-irn/", "TCF IRN ou TEF IRN : le comparatif",
 "L'autre test de naturalisation, adaptatif sur ses deux compréhensions."),
("/correction-ia/", "La correction IA de l'écrit et de l'oral",
 "Le seul moyen de savoir si votre écrit argumenté atteint vraiment le B2."),
],
"sources": """<strong>Les formats évoluent.</strong> Cette page est à jour au 7 août 2026. Les
exercices présentés sont des contenus originaux de notre application, conçus au format officiel —
il n'existe aucune annale officielle du TCF en accès libre. Vérifiez la structure en vigueur
auprès de votre centre agréé et les exigences de votre démarche sur
<a href="https://www.service-public.fr/" target="_blank" rel="noopener">service-public.fr</a>.""",
},

# ═══════════════════════════════════════════ 6. TEF CANADA
{
"slug": "exercices-tef-canada",
"title": "Exercices TEF Canada : les épreuves corrigées",
"desc": "40 questions par compréhension, deux sections par épreuve d'expression. Des exercices corrigés et les consignes typées du TEF, sans équivalent au TCF.",
"og_title": "Exercices TEF Canada : les épreuves corrigées",
"og_desc": "40 questions par compréhension, deux sections par expression. Exercices corrigés et consignes typées du TEF.",
"crumb": "Exercices TEF Canada",
"h1": "Exercices du TEF Canada : les épreuves, corrigées",
"date_fr": "7 août 2026",
"read": 8,
"accent": "accent-tef",
"intro": """Le TEF Canada dure <strong>2 h 55</strong> et impose quatre épreuves. Ses compréhensions
comptent <strong>40 questions</strong> chacune, et ses épreuves d'expression sont organisées en
<strong>deux sections</strong> aux consignes très typées — écrire la suite d'un texte, poser des
questions à l'examinateur — qui n'ont <strong>aucun équivalent au TCF</strong>. Voici des exercices
corrigés et ce que chaque section attend.""",
"facts": [
"<strong>CE 40 questions/60 min · CO 40 questions/40 min · EE 2 sections/60 min · EO 2 sections/15 min.</strong>",
"⚠️ IRCC lit la colonne <strong>« équivalence ancien score »</strong>, pas celle sur 699.",
"<strong>NCLC 7</strong> = 207 en CE, 249 en CO, 310 aux deux expressions sur ces échelles.",
"⚠️ <strong>EE section A</strong> : écrire la <em>suite</em> d'un texte — exercice sans équivalent au TCF.",
"⚠️ <strong>EO section A</strong> : c'est <em>vous</em> qui posez les questions.",
"Une seule écoute, sans retour arrière.",
],
"toc": [
("format", "Le format des épreuves"),
("exercices", "Deux exercices de compréhension corrigés"),
("sections", "Les quatre sections d'expression"),
("ancien-score", "Le piège de la colonne « ancien score »"),
("methode", "La méthode"),
],
"body": """
<h2 id="format">Le format des épreuves</h2>

<div class="tablewrap">
<table>
<caption>TEF Canada. Source : Le français des affaires — CCI Paris Île-de-France, structure vérifiée en juillet 2026.</caption>
<thead><tr><th>Épreuve</th><th>Contenu</th><th>Durée</th></tr></thead>
<tbody>
<tr><td>Compréhension écrite</td><td>40 questions</td><td>60 min</td></tr>
<tr><td>Compréhension orale</td><td>40 questions</td><td>40 min</td></tr>
<tr><td>Expression écrite</td><td>2 sections — A : 80 mots min · B : 200 mots min</td><td>60 min</td></tr>
<tr><td>Expression orale</td><td>2 sections — A : 5 min · B : 10 min</td><td>15 min</td></tr>
<tr><td colspan="2"><strong>Total</strong></td><td><strong>2 h 55</strong></td></tr>
</tbody>
</table>
</div>

<p>Quarante questions en 40 minutes à l'oral, c'est <strong>une minute par question</strong> —
donc un rythme légèrement plus confortable que le <a href="/tcf-canada/">TCF Canada</a> et ses
54 secondes, mais sur davantage de questions.</p>

<h2 id="exercices">Deux exercices de compréhension corrigés</h2>

""" + exo(1, "B2 — compréhension orale", "Ce que vous entendez — débat, plusieurs intervenants :",
"« <strong>Lucas Berger :</strong> La France consacre environ un pour cent de son budget à la "
"culture, un modèle envié dans le monde entier. Le ministère de la Culture, créé par Malraux en "
"mille neuf cent cinquante-neuf, a démocratisé l'accès aux arts. Cependant, les pratiques "
"culturelles restent très inégales. Selon les enquêtes, les cadres supérieurs vont quatre fois "
"plus au théâtre que les ouvriers. »",
"Que révèle la précision « un modèle envié dans le monde entier » ?",
["Que les autres pays ont tenté de copier le modèle français sans succès",
 "Que le budget culturel français est le plus élevé du monde en valeur absolue",
 "Que la France exporte ses politiques culturelles vers les pays en développement",
 "Que l'orateur cherche à légitimer le niveau de dépenses en invoquant une reconnaissance externe"],
"D — Que l'orateur cherche à légitimer le niveau de dépenses",
"la question porte sur la <strong>fonction argumentative</strong> d'une formule, pas sur son "
"contenu. Dire qu'un modèle est « envié » est un <em>argument d'autorité</em> : plutôt que de "
"justifier la dépense en interne, l'orateur la valide par une reconnaissance extérieure. Les "
"trois autres options prennent la formule au premier degré."
) + exo(2, "B2 — compréhension écrite", "Document — texte institutionnel :",
"« La protection de l'enfance en France repose sur un principe fondamental : l'intérêt supérieur "
"de l'enfant, inscrit dans la Convention internationale des droits de l'enfant ratifiée en 1990. "
"Ce principe guide les décisions des juges des enfants et des travailleurs sociaux lorsqu'un "
"conflit apparaît entre le maintien de l'enfant dans sa famille et sa protection face aux risques "
"de maltraitance. »",
"Quel conflit apparaît dans les décisions des acteurs de la protection de l'enfance ?",
["Le conflit entre les préférences des parents et celles des enfants",
 "Le conflit entre les services départementaux et les autorités nationales",
 "Le conflit entre la protection de l'enfant et le maintien en famille",
 "Le conflit entre les théories juridiques et les pratiques psychologiques"],
"C — Entre la protection de l'enfant et le maintien en famille",
"la phrase le dit presque littéralement — « lorsqu'un conflit apparaît entre le maintien de "
"l'enfant dans sa famille et sa protection ». La difficulté vient de la <strong>densité "
"syntaxique</strong> : la réponse est enfouie dans une longue subordonnée. Au TEF, les textes "
"institutionnels sont fréquents et exigent une lecture lente."
) + """

<h2 id="sections">Les quatre sections d'expression</h2>

<p>C'est ici que le TEF se distingue vraiment du TCF. Les quatre sections ont des consignes très
typées, qu'un candidat entraîné sur des annales de TCF découvre le jour J.</p>

<div class="tablewrap">
<table>
<caption>Ce que chaque section demande.</caption>
<thead><tr><th>Section</th><th>Consigne</th><th>Le piège</th></tr></thead>
<tbody>
<tr><td><strong>Écrit A</strong><br>25 min · 80 mots min</td><td>Écrire la <em>suite</em> d'un article ou fait divers dont on vous donne le début</td><td>Rupture de registre ou de temps verbal avec l'amorce</td></tr>
<tr><td><strong>Écrit B</strong><br>35 min · 200 mots min</td><td>Point de vue argumenté</td><td>Écrire moins de 200 mots</td></tr>
<tr><td><strong>Oral A</strong><br>5 min</td><td><em>Obtenir des informations</em> en posant des questions à l'examinateur</td><td>Rester en position d'interrogé</td></tr>
<tr><td><strong>Oral B</strong><br>10 min</td><td>Argumenter pour convaincre, double évaluation</td><td>Exposer sans chercher à convaincre</td></tr>
</tbody>
</table>
</div>

""" + sujet("Écrit section B — sujet type", "35 minutes · 200 mots minimum",
"Sur un forum de parents d'élèves, un débat s'est ouvert autour de la question suivante : faut-il "
"interdire les devoirs à la maison à l'école primaire ? Rédigez une contribution argumentée en "
"présentant les avantages et les inconvénients de cette mesure, puis exprimez clairement votre "
"position.",
"<strong>200 mots est un plancher</strong>, et c'est le premier point vérifié. La consigne "
"impose une structure en trois temps — avantages, inconvénients, position — qui est votre plan "
"tout fait. Le genre « contribution à un forum » autorise un registre un peu moins soutenu "
"qu'une lettre formelle, mais reste écrit et argumenté : pas d'abréviations, pas d'oral."
) + sujet("Oral section B — sujet type", "10 minutes · argumenter pour convaincre",
"Devrait-on rendre les transports en commun gratuits dans les grandes villes ? Présentez une "
"argumentation équilibrée en examinant les conséquences économiques, sociales et écologiques de "
"cette mesure.",
"Le mot important est <strong>« convaincre »</strong> : il ne s'agit pas d'exposer les deux "
"côtés puis de conclure, mais de défendre une position en anticipant les objections. La consigne "
"nomme trois angles — économique, social, écologique : les traiter tous les trois est le moyen "
"le plus simple de remplir les dix minutes avec une structure audible."
) + """

<h2 id="ancien-score">Le piège de la colonne « ancien score »</h2>

<div class="note">
<p><strong>Votre attestation TEF affiche deux colonnes de notes.</strong> IRCC convertit en NCLC à
partir de la colonne <strong>« équivalence ancien score »</strong> — sur 300 en compréhension
écrite, sur 360 en compréhension orale, sur 450 pour chaque expression — et <em>non</em> de la
colonne sur 699. Se tromper de colonne fait croire à un NCLC très supérieur ou très inférieur au
vôtre. C'est l'erreur de lecture la plus fréquente du TEF, détaillée sur notre page
<a href="/tef-canada/">TEF Canada</a>.</p>
</div>

<p>Concrètement, pour <strong>NCLC 7</strong> : 207 en compréhension écrite, 249 en compréhension
orale, et 310 en expression écrite comme en expression orale, sur ces échelles-là.</p>

<h2 id="methode">La méthode</h2>

<ol>
<li><strong>Travaillez les quatre sections d'expression séparément.</strong> Elles n'ont rien en
commun : la section A de l'oral, où c'est vous qui interrogez, se prépare comme un exercice à
part entière.</li>
<li><strong>Répétez la section A de l'écrit sur des amorces variées.</strong> Capter un registre
et un temps verbal imposés est une compétence mécanique, qui s'acquiert vite.</li>
<li><strong>Chronométrez à une minute par question</strong> en compréhension orale.</li>
<li><strong>Vérifiez toujours quelle colonne vous lisez</strong> quand vous convertissez un score
d'entraînement en NCLC.</li>
<li><strong>Passez un blanc de TCF Canada aussi</strong> avant de choisir : aucune règle générale
ne dit que l'un est plus facile, seul votre score dans chaque format tranche.</li>
</ol>
""",
"cta_h2": "Les sections A et B, ça se répète",
"cta_p": """Examens blancs au format exact du TEF Canada — sections A et B de l'écrit comme de
l'oral —, conversion NCLC automatique depuis la bonne colonne, et correction IA sur les critères
officiels. Dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Combien de questions y a-t-il au TEF Canada ?",
 """40 questions en compréhension écrite (60 minutes) et 40 en compréhension orale (40 minutes),
soit environ une minute par question à l'oral. S'y ajoutent l'expression écrite en deux sections
(60 minutes) et l'expression orale en deux sections (15 minutes), pour un total de 2 h 55."""),
("Qu'est-ce que la section A de l'expression écrite ?",
 """Un exercice sans équivalent au TCF : on vous donne le début d'un article ou d'un fait divers et
vous devez en écrire la suite, en 25 minutes et 80 mots minimum. La note sanctionne la rupture de
cohérence avec l'amorce — registre, temps verbal et point de vue sont imposés par le début
fourni."""),
("Qu'est-ce que la section A de l'expression orale ?",
 """Une section où c'est vous qui posez les questions : vous devez obtenir des informations de
l'examinateur, en 5 minutes. Cette inversion de rôle est contre-intuitive et beaucoup de candidats
restent en position d'interrogé, produisent trop peu, et perdent des points sur une section
pourtant courte et prévisible."""),
("Quel score faut-il pour NCLC 7 au TEF Canada ?",
 """207 à 232 en compréhension écrite, 249 à 279 en compréhension orale, et 310 à 348 en expression
écrite comme en expression orale — sur les échelles « équivalence ancien score » utilisées par
IRCC, et non sur la colonne sur 699 de votre attestation."""),
("Pourquoi mon attestation affiche-t-elle deux scores ?",
 """Parce que le TEF Canada publie un score sur 699 et une colonne « équivalence ancien score ».
IRCC convertit en NCLC à partir de la seconde. Vérifiez toujours quelle colonne vous lisez avant de
comparer votre score à un tableau de conversion."""),
("Le TEF est-il plus facile que le TCF ?",
 """Aucune source officielle ne permet de l'affirmer. Les compétences évaluées sont les mêmes, les
exercices non : le TEF propose deux sections longues et typées là où le TCF propose trois tâches
courtes. Le seul critère fiable est votre propre score dans chaque format — passez un examen blanc
de chacun."""),
],
"also": [
("/tef-canada/", "TEF Canada et TEFAQ : format, NCLC et préparation",
 "Le guide complet, avec la table de conversion NCLC sur les bonnes échelles."),
("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?",
 "Le comparatif des deux tests acceptés par IRCC."),
("/blog/tefaq-oral-quebec/", "TEFAQ : le test modulaire où l'oral suffit souvent",
 "La version québécoise, avec les mêmes épreuves mais modulaires."),
("/examens-blancs/", "Examens blancs au format officiel",
 "Le protocole de passation pour que votre score veuille dire quelque chose."),
],
"sources": """<strong>Les formats évoluent.</strong> Cette page est à jour au 7 août 2026. Les
exercices présentés sont des contenus originaux de notre application, conçus au format officiel.
Vérifiez la structure en vigueur sur
<a href="https://www.lefrancaisdesaffaires.fr/" target="_blank" rel="noopener">lefrancaisdesaffaires.fr</a>
avant votre session.""",
},

# ═══════════════════════════════════════════ 7. DELF B2
{
"slug": "exercices-delf-b2",
"title": "Exercices DELF B2 : les 4 épreuves corrigées",
"desc": "Format réformé, 100 % QCM aux compréhensions et note éliminatoire à 5/25. Un exercice corrigé par épreuve et ce que le correcteur attend vraiment.",
"og_title": "Exercices DELF B2 : les 4 épreuves corrigées",
"og_desc": "Format réformé, 100 % QCM aux compréhensions, note éliminatoire à 5/25. Un exercice corrigé par épreuve.",
"crumb": "Exercices DELF B2",
"h1": "Exercices du DELF B2 : les quatre épreuves, corrigées",
"date_fr": "7 août 2026",
"read": 8,
"accent": "accent-delf",
"intro": """Quatre épreuves notées sur 25, un total sur <strong>100</strong>, l'admission à
<strong>50/100</strong> — et une note inférieure à <strong>5/25</strong> à une seule épreuve qui
vous élimine, quelle que soit votre moyenne. Depuis la réforme, les deux compréhensions sont
<strong>100 % QCM</strong>. Voici un exercice corrigé par épreuve.""",
"facts": [
"<strong>4 épreuves sur 25</strong> · total sur <strong>100</strong> · admission à <strong>50/100</strong>.",
"⚠️ <strong>Moins de 5/25</strong> à une seule épreuve = <strong>éliminatoire</strong>.",
"<strong>CO 30 min · CE 60 min · PE 60 min · PO 20 min</strong> (+ 30 min de préparation).",
"Depuis la réforme : compréhensions <strong>100 % QCM</strong>, entretien dirigé <strong>supprimé</strong> à l'oral.",
"⚠️ En CO, les 2 premiers exercices sont diffusés <strong>2 fois</strong>, le 3<sup>e</sup> une seule.",
"Production écrite : <strong>250 mots minimum</strong>.",
],
"toc": [
("format", "Le format des quatre épreuves"),
("exercices", "Un exercice corrigé par épreuve"),
("eliminatoire", "La note éliminatoire change la stratégie"),
("methode", "La méthode"),
],
"body": """
<h2 id="format">Le format des quatre épreuves</h2>

<div class="tablewrap">
<table>
<caption>DELF B2, format issu de la réforme 2020, généralisé depuis septembre 2024. Source : France Éducation international.</caption>
<thead><tr><th>Épreuve</th><th>Contenu</th><th>Durée</th><th>Note</th></tr></thead>
<tbody>
<tr><td>Compréhension de l'oral</td><td>3 exercices / 5 documents audio</td><td>30 min</td><td>/25</td></tr>
<tr><td>Compréhension des écrits</td><td>3 exercices / 5 documents écrits</td><td>60 min</td><td>/25</td></tr>
<tr><td>Production écrite</td><td>1 exercice, 250 mots minimum</td><td>60 min</td><td>/25</td></tr>
<tr><td>Production orale</td><td>Monologue suivi + débat</td><td>20 min <em>(+ 30 min de préparation)</em></td><td>/25</td></tr>
</tbody>
</table>
</div>

<div class="note">
<p><strong>Attention aux annales périmées.</strong> Si un document mentionne un entretien dirigé à
l'oral ou des questions ouvertes en compréhension, il décrit un examen qui n'existe plus. Une
grande partie des ressources en ligne est antérieure à la réforme.</p>
</div>

<h2 id="exercices">Un exercice corrigé par épreuve</h2>

""" + exo(1, "B2 — compréhension de l'oral", "Ce que vous entendez — interview :",
"« <strong>Journaliste :</strong> Vous êtes spécialiste en santé publique. La question de la santé "
"mentale des jeunes est devenue un sujet majeur en France. Pouvez-vous nous en dire plus ?<br>"
"<strong>Docteur Martin :</strong> Oui, effectivement, nous observons une augmentation très "
"préoccupante des troubles psychiques chez les 15-25 ans depuis la pandémie de Covid-19. Les "
"consultations pour anxiété et dépression ont augmenté de 40 % entre 2019 et 2024 dans cette "
"tranche d'âge. Les tentatives de suicide chez les adolescentes ont doublé. »",
"Quelle augmentation note-t-on pour les troubles ?",
["Une hausse de 20 % en cinq ans", "Une hausse de 80 % en cinq ans",
 "Une hausse de 40 % entre 2019 et 2024", "Une hausse de 60 % entre 2019 et 2024"],
"C — Une hausse de 40 % entre 2019 et 2024",
"question de repérage, mais avec deux chiffres proches dans le document : les 40 % concernent les "
"consultations, le « doublé » concerne les tentatives de suicide. <strong>Vérifiez toujours à quoi "
"se rapporte le chiffre</strong> avant de cocher — c'est le mécanisme de distraction le plus "
"courant."
) + exo(2, "B2 — compréhension des écrits", "Document — article de presse :",
"« <strong>La transition écologique en France : un défi collectif.</strong> Depuis l'Accord de "
"Paris en 2015, la France s'est engagée dans une transformation profonde de son modèle économique "
"et énergétique. Le plan national bas-carbone fixe des objectifs ambitieux : réduire les émissions "
"de gaz à effet de serre de 40 % d'ici 2030 par rapport aux niveaux de 1990. Mais entre les "
"annonces politiques et la réalité du terrain, le fossé reste considérable. »",
"Quel est le but principal de cet article ?",
["Favoriser les initiatives locales sur le plan national",
 "Célébrer les succès climatiques français récents",
 "Comparer la France aux autres pays européens",
 "Montrer les contradictions sociales de la transition"],
"D — Montrer les contradictions sociales de la transition",
"la question porte sur l'<strong>intention de l'auteur</strong>, pas sur le contenu. Le pivot est "
"le « Mais » : l'article énonce les objectifs pour mieux exposer l'écart avec la réalité. "
"L'option B est le contresens attendu — un lecteur pressé retient les « objectifs ambitieux » et "
"conclut à une célébration."
) + sujet("Production écrite", "60 minutes · 250 mots minimum · noté sur 25",
"Vous habitez dans une ville où la mairie a décidé de supprimer plusieurs lignes de bus pour des "
"raisons budgétaires. En tant que président(e) d'une association de quartier, vous écrivez au "
"maire pour protester contre cette décision. Vous expliquez les conséquences pour les habitants "
"et vous proposez des solutions alternatives.",
"<strong>Trois contraintes se cumulent ici</strong> : le genre (lettre formelle, donc formule "
"d'appel, objet, formule de politesse), le rôle (vous écrivez ès qualités, pas en votre nom), et "
"les deux actions demandées (expliquer les conséquences <em>et</em> proposer des alternatives). "
"Omettre les propositions est l'erreur la plus fréquente : on proteste, on n'alterne pas. "
"250 mots est un plancher."
) + sujet("Production orale", "30 minutes de préparation · 20 minutes de passation · noté sur 25",
"Vous dégagerez le problème soulevé par le document ci-dessous. Vous présenterez votre opinion sur "
"le sujet de manière argumentée, puis vous la défendrez face à l'examinateur lors d'un débat.",
"L'épreuve commence <strong>directement par le monologue</strong> : l'entretien dirigé, qui "
"permettait de se détendre, a été supprimé par la réforme. Les 30 minutes de préparation servent "
"à construire un plan et noter des mots-clés, pas à rédiger — un candidat qui lit ses notes est "
"repérable. En seconde partie, <strong>le jury n'est pas d'accord avec vous, et c'est voulu</strong> : "
"son rôle est de tester votre capacité à tenir une position en la nuançant. Abandonner sa thèse "
"à la première objection coûte des points."
) + """

<h2 id="eliminatoire">La note éliminatoire change la stratégie</h2>

<div class="tablewrap">
<table>
<caption>Les deux seuils du DELF B2.</caption>
<thead><tr><th>Règle</th><th>Seuil</th><th>Effet</th></tr></thead>
<tbody>
<tr><td>Moyenne générale</td><td><strong>50/100</strong></td><td>En dessous, échec</td></tr>
<tr><td>Note plancher par épreuve</td><td><strong>5/25</strong></td><td>En dessous sur <em>une seule</em> épreuve, échec — même avec 60/100</td></tr>
</tbody>
</table>
</div>

<p>La conséquence est contre-intuitive : <strong>une compétence très faible coûte plus qu'une
compétence forte ne rapporte</strong>. Un candidat à 20/25 en compréhension écrite et 4/25 en
production orale échoue, alors que sa moyenne dépasse le seuil. Votre premier travail de
préparation n'est donc pas de progresser là où vous êtes bon, mais de
<strong>sortir votre épreuve la plus faible de la zone éliminatoire</strong>.</p>

<h2 id="methode">La méthode</h2>

<ol>
<li><strong>Un examen blanc complet dès le départ</strong>, noté sur les barèmes officiels, pour
identifier l'épreuve qui risque de vous éliminer.</li>
<li><strong>Sortez cette épreuve de la zone rouge</strong> avant toute autre chose.</li>
<li><strong>Travaillez la production écrite à la structure</strong>, pas au vocabulaire :
l'essentiel des points perdus vient du plan, du genre et de la consigne.</li>
<li><strong>Simulez l'oral en conditions réelles</strong>, avec les 30 minutes de préparation et
une contradiction assumée en seconde partie.</li>
<li><strong>Attention aux ressources périmées</strong> : vérifiez toujours la date de ce sur quoi
vous vous entraînez.</li>
</ol>
""",
"cta_h2": "Sortir de la zone éliminatoire, d'abord",
"cta_p": """Examens blancs au format DELF B2 réformé, notation sur le barème officiel /25 par
épreuve avec alerte sur la note éliminatoire, et correction IA de la production écrite et orale sur
les critères officiels. Dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Quelle note faut-il pour obtenir le DELF B2 ?",
 """50 sur 100. Les quatre épreuves sont notées sur 25 chacune. Attention à la règle qui fait
échouer des candidats dont la moyenne suffisait : une note inférieure à 5 sur 25 à une seule
épreuve est éliminatoire, quel que soit le total."""),
("Les compréhensions sont-elles en QCM ?",
 """Oui, à 100 % depuis la réforme. Les questions ouvertes et les vrai/faux avec justification ont
disparu des deux compréhensions. Vous ne rédigez donc plus rien dans ces épreuves — ce qui change
la gestion du temps, mais supprime aussi la possibilité de grappiller des points par une
justification partiellement juste."""),
("Combien de fois entend-on les documents audio ?",
 """Cela dépend de l'exercice. Les deux premiers exercices, portant sur des documents radio longs,
sont diffusés deux fois. Le troisième, qui enchaîne trois courts documents, n'est diffusé qu'une
seule fois. Cette asymétrie surprend au moment où la concentration est déjà entamée."""),
("Combien de mots faut-il à la production écrite ?",
 """250 mots minimum, en un seul exercice, en 60 minutes. C'est un plancher : écrire en dessous fait
perdre des points sur le respect de la consigne, quelle que soit la qualité de la langue."""),
("L'entretien dirigé existe-t-il encore à l'oral ?",
 """Non, il a été supprimé par la réforme. L'épreuve commence désormais directement par le monologue
suivi, puis vient le débat avec les examinateurs. La mise en jambes qui permettait de se détendre
n'existe plus au B2 — elle subsiste en revanche au DELF B1."""),
("Le jury est-il censé être d'accord avec moi ?",
 """Non, et c'est voulu. En seconde partie de l'oral, le jury vous contredit pour tester votre
capacité à tenir une position, à nuancer et à concéder sans céder. Les candidats qui abandonnent
leur thèse à la première objection perdent des points sur la compétence évaluée."""),
],
"also": [
("/delf-b2/", "DELF B2 : épreuves, barème et méthode pour réussir",
 "Le guide complet du format réformé et des deux seuils."),
("/blog/production-ecrite-delf-b2/", "Production écrite du DELF B2 : la méthode",
 "Le plan en cinq parties et les cinq erreurs qui coûtent le plus."),
("/blog/diplome-ou-test-delf-tcf/", "Diplôme ou test : lequel vous faut-il ?",
 "Ce que le DELF prouve, et les démarches où il ne suffit pas."),
("/examens-blancs/", "Examens blancs au format officiel",
 "Le protocole de passation, barèmes officiels compris."),
],
"sources": """<strong>Les formats évoluent.</strong> Cette page est à jour au 7 août 2026 et décrit
le format issu de la réforme 2020, généralisé depuis septembre 2024. Les exercices présentés sont
des contenus originaux de notre application. Vérifiez le format en vigueur sur
<a href="https://www.france-education-international.fr/diplome/delf-tout-public" target="_blank" rel="noopener">france-education-international.fr</a>
avant votre session.""",
},

# ═══════════════════════════════════════════ 8. STRUCTURES
{
"slug": "exercices-structures-langue-tcf",
"title": "Structures de la langue TCF : exercices corrigés",
"desc": "18 QCM en 15 minutes, exclusifs au TCF Tout Public : cinq exercices corrigés du B1 au C1, les dix catégories testées, et pourquoi le TCF Canada ne comporte pas cette épreuve.",
"og_title": "Structures de la langue TCF : exercices corrigés",
"og_desc": "18 QCM en 15 minutes, exclusifs au TCF Tout Public. Cinq exercices corrigés du B1 au C1 et les dix catégories testées.",
"crumb": "Structures de la langue",
"h1": "Structures de la langue du TCF : exercices corrigés",
"date_fr": "7 août 2026",
"read": 7,
"accent": "accent-tcf",
"intro": """<strong>18 questions en 15 minutes</strong>, soit <strong>50 secondes par
question</strong> — de la grammaire et du lexique évalués pour eux-mêmes. C'est la seule épreuve du
TCF qui teste la langue hors contexte de communication. Et c'est surtout la seule qui soit
<strong>exclusive au TCF Tout Public</strong> : si vous préparez le TCF Canada, le TCF Québec ou le
TCF IRN, <strong>vous ne la passerez jamais</strong>.""",
"facts": [
"<strong>18 QCM · 15 minutes</strong> — environ <strong>50 secondes par question</strong>.",
"⚠️ <strong>Exclusive au TCF Tout Public</strong> : absente du TCF Canada, Québec et IRN.",
"Dix catégories : temps, subjonctif, pronoms, relatifs, prépositions, accord du participe passé, passif, discours indirect, hypothèse, argumentation.",
"Notée sur l'échelle <strong>699</strong>, comme les deux compréhensions.",
"Format à trou : une phrase, un blanc, quatre propositions.",
"C'est l'épreuve la plus <strong>rentable à travailler</strong> : des règles finies, mécanisables.",
],
"toc": [
("qui", "Qui passe cette épreuve — et qui ne la passe pas"),
("format", "Le format"),
("exercices", "Cinq exercices corrigés"),
("categories", "Les dix catégories testées"),
("methode", "Pourquoi c'est l'épreuve la plus rentable"),
],
"body": """
<h2 id="qui">Qui passe cette épreuve — et qui ne la passe pas</h2>

<div class="note">
<p><strong>C'est le point le plus important de cette page.</strong> La section « maîtrise des
structures de la langue » n'existe que dans le <strong>TCF Tout Public</strong>. Les versions
Canada, Québec et IRN ne la comportent pas. Un candidat qui s'entraîne sur des annales de TCF
Tout Public en visant le <a href="/tcf-canada/">TCF Canada</a> travaille donc une épreuve qu'il ne
passera jamais — et découvrira le jour J un format de compréhension différent, avec 39 questions
au lieu de 29.</p>
</div>

<div class="tablewrap">
<table>
<caption>Présence de la section « structures » selon la version du TCF.</caption>
<thead><tr><th>Version</th><th>Section structures</th></tr></thead>
<tbody>
<tr><td><strong>TCF Tout Public</strong></td><td><strong>oui</strong> — 18 QCM / 15 min</td></tr>
<tr><td><a href="/tcf-canada/">TCF Canada</a></td><td>non</td></tr>
<tr><td><a href="/tcf-quebec/">TCF Québec</a></td><td>non</td></tr>
<tr><td><a href="/tcf-irn/">TCF IRN</a></td><td>non</td></tr>
</tbody>
</table>
</div>

<p>Si vous visez le TCF Tout Public — preuve de niveau générale, études en France, ou la voie DAP —
cette épreuve compte dans votre score obligatoire, au même titre que les deux compréhensions.</p>

<h2 id="format">Le format</h2>

<p>Une phrase, un blanc, quatre propositions. Aucun contexte, aucun document : la question porte
sur un point de langue précis. Les 18 questions montent en difficulté, du B1 au C1.</p>

<h2 id="exercices">Cinq exercices corrigés</h2>

""" + exo(1, "B1 — temps du passé", "Complétez :",
"Quand il a appris la nouvelle, il <strong>______</strong> une grande joie.",
"Quelle forme convient ?",
["ressentait", "a ressenti", "avait ressenti", "aurait ressenti"],
"B — a ressenti",
"pour une action <strong>ponctuelle et terminée</strong> dans le passé, on emploie le passé "
"composé. L'imparfait « ressentait » décrirait un état durable, le plus-que-parfait une "
"antériorité. Repère : « Quand il a appris » situe un moment précis. <em>Exemple : j'ai vu ce "
"film hier soir.</em>"
) + exo(2, "B1 — imparfait ou passé composé", "Complétez :",
"Hier, pendant que je <strong>______</strong> mes devoirs, ma mère a appelé.",
"Quelle forme convient ?",
["ai fait", "fais", "faisais", "ferai"],
"C — faisais",
"« pendant que » introduit une action <strong>en cours</strong>, interrompue par une autre : c'est "
"l'imparfait. La règle est mécanique — action de fond à l'imparfait, action ponctuelle qui "
"l'interrompt au passé composé. <em>Exemple : je lisais quand le téléphone a sonné.</em>"
) + exo(3, "B2 — subjonctif", "Complétez :",
"Pourvu qu'il <strong>______</strong> à l'heure pour le départ !",
"Quelle forme convient ?",
["soit", "est", "sera", "serait"],
"A — soit",
"« <strong>pourvu que</strong> » exprime un souhait et commande le subjonctif. L'indicatif et le "
"conditionnel sont exclus. Ce type de question teste la <strong>reconnaissance du déclencheur</strong> : "
"la locution seule impose la forme, indépendamment du sens. <em>Exemple : pourvu qu'il fasse "
"beau !</em>"
) + exo(4, "B2 — subjonctif après locution", "Complétez :",
"À moins que vous n'<strong>______</strong> une bonne raison, nous refusons.",
"Quelle forme convient ?",
["ayez", "eussiez", "auriez", "avez"],
"A — ayez",
"« <strong>à moins que</strong> » signifie « sauf si » et demande le subjonctif présent. Piège "
"supplémentaire : le « ne » qui suit est un <strong>ne explétif</strong> — il n'a aucune valeur "
"négative. Beaucoup de candidats le lisent comme une négation et changent de forme. <em>Exemple : "
"on part demain, à moins que tu préfères rester.</em>"
) + exo(5, "C1 — plus-que-parfait et inversion", "Complétez :",
"À peine avait-il <strong>______</strong> la porte que le téléphone sonna.",
"Quelle forme convient ?",
["ouvert", "ouvrira", "ouverte", "ouvre"],
"A — ouvert",
"« <strong>à peine… que</strong> » marque une antériorité immédiate : plus-que-parfait pour "
"l'action antérieure, passé simple pour la suivante. Le participe reste <strong>invariable</strong> "
"— « ouverte » serait un accord fautif, l'auxiliaire étant <em>avoir</em> et le complément placé "
"après. <em>Exemple : à peine avait-il ouvert la porte que le téléphone sonna.</em>"
) + """

<h2 id="categories">Les dix catégories testées</h2>

<div class="tablewrap">
<table>
<caption>Ce que couvre la section, et ce qu'il faut y travailler.</caption>
<thead><tr><th>Catégorie</th><th>Le déclencheur à reconnaître</th></tr></thead>
<tbody>
<tr><td><strong>Temps</strong></td><td>Marqueurs de durée ou de ponctualité : pendant que, quand, soudain</td></tr>
<tr><td><strong>Subjonctif</strong></td><td>Locutions : bien que, pourvu que, à moins que, avant que</td></tr>
<tr><td><strong>Pronoms</strong></td><td>Place et forme selon la fonction : en, y, lui, le</td></tr>
<tr><td><strong>Relatifs</strong></td><td>qui / que / dont / où / lequel selon la fonction</td></tr>
<tr><td><strong>Prépositions</strong></td><td>Verbes à construction fixe : penser à, dépendre de</td></tr>
<tr><td><strong>Accord du participe passé</strong></td><td>Auxiliaire et place du complément</td></tr>
<tr><td><strong>Passif</strong></td><td>Transformation et accord</td></tr>
<tr><td><strong>Discours indirect</strong></td><td>Concordance des temps et changement de repères</td></tr>
<tr><td><strong>Hypothèse</strong></td><td>Les trois systèmes en « si »</td></tr>
<tr><td><strong>Argumentation</strong></td><td>Connecteurs logiques : cependant, néanmoins, or</td></tr>
</tbody>
</table>
</div>

<h2 id="methode">Pourquoi c'est l'épreuve la plus rentable</h2>

<p>Contrairement aux compréhensions, qui dépendent d'un niveau global mettant des mois à monter,
cette section porte sur un <strong>ensemble fini de règles</strong>. Dix catégories, quelques
dizaines de déclencheurs : c'est mécanisable.</p>

<ol>
<li><strong>Travaillez par déclencheur, pas par règle.</strong> « À moins que → subjonctif » est
une association à installer, pas une théorie à comprendre. La question ne vous demande jamais
d'expliquer, seulement de reconnaître.</li>
<li><strong>Faites des séries courtes et fréquentes.</strong> Dix questions par jour valent mieux
qu'une heure hebdomadaire : c'est de la mémorisation, pas de la compréhension.</li>
<li><strong>Notez vos erreurs par catégorie.</strong> Vous découvrirez presque toujours que deux
ou trois catégories concentrent l'essentiel de vos points perdus.</li>
<li><strong>Chronométrez à 50 secondes.</strong> Une question de structures qui résiste plus
d'une minute ne se débloquera pas : cochez et passez.</li>
<li><strong>Ne travaillez pas cette épreuve si vous visez le Canada, le Québec ou l'IRN.</strong>
C'est du temps entièrement perdu — mieux vaut le mettre sur l'expression écrite.</li>
</ol>
""",
"cta_h2": "Dix catégories, ça se mécanise",
"cta_p": """Des milliers d'exercices de structures classés par catégorie et par niveau, avec
explication et exemple après chaque réponse, plus la répétition espacée qui fait revenir vos
erreurs au bon moment. Dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Qu'est-ce que la section « structures de la langue » du TCF ?",
 """Une épreuve de 18 questions à choix multiples en 15 minutes, qui évalue la grammaire et le
lexique pour eux-mêmes, hors contexte de communication. Le format est celui du texte à trou : une
phrase, un blanc, quatre propositions."""),
("Le TCF Canada comporte-t-il cette épreuve ?",
 """Non. La section « structures de la langue » est exclusive au TCF Tout Public. Les versions
Canada, Québec et IRN ne la comportent pas. Un candidat qui s'entraîne dessus en visant le TCF
Canada travaille une épreuve qu'il ne passera jamais."""),
("Combien de temps par question ?",
 """Environ 50 secondes : 18 questions en 15 minutes. C'est suffisant pour une question dont on
reconnaît le déclencheur, et insuffisant pour une question qu'on essaie de raisonner. Si une
question résiste plus d'une minute, cochez et passez."""),
("Quelles catégories sont testées ?",
 """Dix : les temps, le subjonctif, les pronoms, les relatifs, les prépositions, l'accord du
participe passé, le passif, le discours indirect, l'hypothèse en « si » et les connecteurs
d'argumentation."""),
("Comment travailler cette épreuve efficacement ?",
 """Par déclencheur plutôt que par règle : « à moins que → subjonctif » est une association à
installer, pas une théorie à comprendre. Faites des séries courtes et fréquentes plutôt qu'une
longue séance hebdomadaire, et notez vos erreurs par catégorie — deux ou trois d'entre elles
concentrent en général l'essentiel des points perdus."""),
("Cette épreuve est-elle notée comme les autres ?",
 """Oui, sur l'échelle 699, au même titre que les deux compréhensions. Elle fait partie des trois
épreuves obligatoires du TCF Tout Public, dont la durée totale est de 1 h 25."""),
],
"also": [
("/blog/difference-tcf-tef/", "TCF ou TEF : toutes les versions comparées",
 "Pour vérifier quelle épreuve comporte votre déclinaison avant de vous entraîner."),
("/blog/exercices-comprehension-ecrite-tcf-canada/", "Exercices de compréhension écrite TCF Canada",
 "Si vous visez le Canada : l'épreuve à travailler à la place."),
("/score-tcf-699/", "Score TCF : comprendre l'échelle 699",
 "Comment vos réponses deviennent un score, et pourquoi il varie."),
("/contenu/", "Le contenu de l'app en détail",
 "Le décompte banque par banque, structures comprises."),
],
"sources": """<strong>Les formats évoluent.</strong> Cette page est à jour au 7 août 2026. Les
exercices présentés sont des contenus originaux de notre application. Vérifiez la structure de
votre déclinaison sur
<a href="https://www.france-education-international.fr/" target="_blank" rel="noopener">france-education-international.fr</a>
avant de caler votre entraînement.""",
},

]

if __name__ == "__main__":
    print("Exercices — expression TCF Canada, IRN, TEF, DELF B2, Structures :")
    build(ARTICLES)
