#!/usr/bin/env python3
"""Articles 5 à 7. Faits repris des articles publiés et sourcés du site."""

from article_template import build

ARTICLES = [

# ─────────────────────────────────────────────────────────────────────────────
{
"slug": "diplome-ou-test-delf-tcf",
"title": "Diplôme ou test : DELF ou TCF, lequel choisir ?",
"desc": "Le DELF est un diplôme acquis à vie, le TCF un test valable deux ans. Ce que chacun prouve, qui les accepte, et la différence de format que personne ne mentionne.",
"og_title": "Diplôme ou test : DELF ou TCF, lequel choisir ?",
"og_desc": "Le DELF est un diplôme à vie, le TCF un test valable deux ans. Ce que chacun prouve, qui les accepte, et la différence de format que personne ne mentionne.",
"crumb": "Diplôme ou test",
"h1": "Diplôme ou test : DELF, DALF, TCF ou TEF, lequel vous faut-il ?",
"date_fr": "7 août 2026",
"read": 7,
"accent": "accent-delf",
"intro": """Ce ne sont pas deux versions de la même chose. Le <strong>DELF</strong> et le
<strong>DALF</strong> sont des <strong>diplômes</strong> : on les obtient ou on les rate, et ils
sont acquis <strong>à vie</strong>. Le <strong>TCF</strong> et le <strong>TEF</strong> sont des
<strong>tests de positionnement</strong> : on ne les rate pas, ils vous situent sur une échelle,
et leur attestation vaut <strong>deux ans</strong>. Le choix se joue moins sur votre niveau que
sur ce que votre dossier exige et sur le temps qu'il va prendre.""",
"facts": [
"<strong>Diplômes</strong> (DELF, DALF) : acquis <strong>à vie</strong>, avec note éliminatoire — on peut les rater.",
"<strong>Tests</strong> (TCF, TEF) : attestation <strong>2 ans</strong>, aucun seuil — on ne les rate pas.",
"⚠️ <strong>Écoutes</strong> : 2 fois au DELF jusqu'au B1, <strong>1 seule</strong> au TCF et au TEF.",
"⚠️ Pour <strong>Entrée express</strong>, un DELF ne vaut rien : seuls le TCF Canada et le TEF Canada sont acceptés.",
"⚠️ Au <strong>Québec</strong>, un DELF est accepté mais doit dater de <strong>moins de deux ans</strong> — le « à vie » ne joue pas.",
"Durée : <strong>1 h 30</strong> pour un test IRN contre <strong>2 h 50</strong> pour un DELF B2.",
],
"toc": [
("nature", "Deux objets différents : on rate un diplôme, pas un test"),
("duree-vie", "Deux ans contre à vie"),
("ecoutes", "La différence de format que personne ne mentionne"),
("reconnaissance", "Qui accepte quoi"),
("quebec", "Le cas où « à vie » ne sert à rien"),
("choisir", "Comment choisir selon votre situation"),
],
"body": """
<h2 id="nature">Deux objets différents : on rate un diplôme, pas un test</h2>

<p>C'est la distinction fondatrice, et elle change tout le reste.</p>

<p>Le <a href="/delf-b2/">DELF</a> et le <a href="/dalf/">DALF</a> sont des
<strong>examens</strong>, délivrés par le ministère de l'Éducation nationale. Quatre épreuves
notées sur 25, un total sur 100, une admission à <strong>50/100</strong> — et une note inférieure
à <strong>5/25</strong> à une seule épreuve qui vous élimine, quelle que soit votre moyenne.
Vous obtenez le diplôme ou vous ne l'obtenez pas.</p>

<p>Le <a href="/tcf-canada/">TCF</a> et le <a href="/tef-canada/">TEF</a> sont des <strong>tests
de positionnement</strong>. Il n'y a ni seuil d'admission ni note éliminatoire : vous obtenez un
score par épreuve, et c'est l'organisme qui reçoit votre dossier — préfecture, IRCC, université —
qui décide si ce score suffit. On ne « rate » pas un TCF ; on obtient un niveau plus bas
qu'espéré.</p>

<div class="note">
<p><strong>Une conséquence stratégique opposée.</strong> Au DELF, une compétence très faible vous
coûte plus qu'une compétence forte ne vous rapporte : il faut d'abord sortir votre épreuve la
plus faible de la zone éliminatoire, la compensation fera le reste. Au TCF et au TEF, il n'y a
<em>aucune</em> compensation : l'administration lit chaque épreuve séparément, et votre dossier
vaut votre score le plus bas. Dans les deux cas, c'est votre point faible qui commande — mais pour
des raisons différentes.</p>
</div>

<h2 id="duree-vie">Deux ans contre à vie</h2>

<p>C'est l'argument que l'on entend le plus, et il est vrai : un diplôme <strong>n'expire
jamais</strong>, une attestation de test vaut <strong>deux ans</strong>. Mais il faut le manier
avec précision, parce qu'il ne s'applique pas partout de la même façon.</p>

<div class="tablewrap">
<table>
<caption>Ce que vous obtenez, selon la famille.</caption>
<thead><tr><th></th><th>DELF · DALF</th><th>TCF · TEF</th></tr></thead>
<tbody>
<tr><td>Nature</td><td>Diplôme d'État</td><td>Attestation de niveau</td></tr>
<tr><td>Durée de validité</td><td><strong>à vie</strong></td><td><strong>2 ans</strong></td></tr>
<tr><td>Peut-on échouer ?</td><td>oui — 50/100, éliminatoire sous 5/25</td><td>non — un score, pas un seuil</td></tr>
<tr><td>Compensation entre épreuves</td><td>oui, au-delà du plancher</td><td><strong>aucune</strong></td></tr>
<tr><td>Durée de l'examen</td><td>2 h 10 (B1) à 4 h (DALF)</td><td>1 h 30 (IRN) à 2 h 55 (TEF Canada)</td></tr>
</tbody>
</table>
</div>

<p>La règle pratique en découle : <strong>si votre dossier part vite, le test suffit</strong> et
vous coûte moins de temps. <strong>Si votre parcours doit s'étaler</strong> — et c'est fréquent
entre une carte de résident et une demande de nationalité, ou entre une candidature et une
inscription universitaire — le diplôme évite d'avoir à repasser et repayer un test expiré au
mauvais moment.</p>

<h2 id="ecoutes">La différence de format que personne ne mentionne</h2>

<div class="note">
<p><strong>Au DELF, les documents des niveaux A1 à B1 sont diffusés deux fois. Au TCF comme au
TEF, il n'y a qu'une seule écoute, sans retour arrière.</strong> Les deux organismes l'écrivent
explicitement, et cela vaut pour les neuf versions, sans exception.</p>
</div>

<p>C'est la différence pratique la plus sous-estimée, et elle piège quantité de candidats
entraînés sur des ressources DELF — largement plus nombreuses en ligne — qui se présentent à un
TCF. Décrocher sur une question signifie la perdre définitivement : l'enjeu n'est plus de
comprendre, c'est de passer immédiatement à la suivante sans essayer de reconstituer ce qu'on
vient de manquer.</p>

<p>Au <a href="/delf-b2/">DELF B2</a>, le format est d'ailleurs mixte depuis la réforme : les deux
premiers exercices de compréhension orale sont diffusés deux fois, le troisième une seule fois.
Cette asymétrie surprend au moment précis où la concentration est déjà entamée.</p>

<h2 id="reconnaissance">Qui accepte quoi</h2>

<p>C'est ici que le choix se tranche vraiment, et la réponse n'est pas symétrique.</p>

<div class="tablewrap">
<table>
<caption>Reconnaissance selon la démarche. Sources : arrêté du 22 décembre 2025 pour la France, IRCC pour le fédéral canadien, ministère de l'Immigration, de la Francisation et de l'Intégration pour le Québec. Consultés en juillet 2026.</caption>
<thead><tr><th>Démarche</th><th>DELF · DALF</th><th>TCF · TEF</th></tr></thead>
<tbody>
<tr><td>Naturalisation française</td><td>oui <em>(B2 exigé)</em></td><td>oui <em>(versions IRN)</em></td></tr>
<tr><td>Carte de résident française</td><td>oui <em>(B1 exigé)</em></td><td>oui <em>(versions IRN)</em></td></tr>
<tr><td><strong>Entrée express (fédéral canadien)</strong></td><td><strong>non</strong></td><td>oui — TCF Canada et TEF Canada <strong>seulement</strong></td></tr>
<tr><td>Citoyenneté canadienne</td><td>oui</td><td>oui <em>(liste plus large)</em></td></tr>
<tr><td>Programmes québécois</td><td>oui, <strong>sous conditions</strong></td><td>oui</td></tr>
<tr><td>Université française</td><td>oui — le DALF C1 dispense de test</td><td>oui <em>(TCF Tout Public)</em></td></tr>
</tbody>
</table>
</div>

<div class="note">
<p><strong>Le cas qui tranche tout seul : l'immigration économique canadienne.</strong> Pour
Entrée express, IRCC n'accepte que <strong>deux tests</strong> — le TCF Canada et le TEF Canada.
Ni le DELF, ni le DALF, ni le TCF Tout Public, ni le TEFAQ n'y figurent. Un DALF C2, le plus haut
diplôme de français existant, ne vaut rien pour un profil Entrée express. Si votre projet est
l'immigration fédérale canadienne, la question « diplôme ou test » ne se pose pas.</p>
</div>

<p>Notez la nuance pour la <strong>citoyenneté</strong> canadienne, souvent confondue avec
l'immigration : la liste y est plus large et comprend le DALF, le DELF, le TCF, le TCFQ, le TEF
Canada, le TEFAQ et le TEF IRN. Vérifiez-la sur le site d'IRCC au moment de votre demande, car
elle désigne des noms de tests qui ne recouvrent pas exactement les noms commerciaux des
déclinaisons.</p>

<h2 id="quebec">Le cas où « à vie » ne sert à rien</h2>

<p>Voici la nuance que presque aucun comparatif ne relève. Le Québec accepte bien les diplômes
DELF et DALF en remplacement du <a href="/tcf-quebec/">TCF Québec</a> — mais
<strong>sous conditions</strong> : une note minimale en compréhension orale et en expression
orale, <em>et</em> une validité de <strong>moins de deux ans</strong>.</p>

<p>Autrement dit : au Québec, votre DELF B2 obtenu il y a cinq ans ne vous dispense de rien.
L'avantage central du diplôme — sa permanence — est neutralisé par une condition de fraîcheur.
C'est exactement l'inverse de la logique française, où un diplôme, précisément parce qu'il
n'expire pas, est le justificatif le plus sûr pour un dossier qui traîne.</p>

<p>La leçon générale : <strong>« à vie » est une propriété du diplôme, pas une garantie
d'acceptation.</strong> Chaque démarche publie sa propre liste de justificatifs, avec ses propres
conditions de note et de validité. Vérifiez celle de <em>votre</em> démarche avant de miser sur la
permanence.</p>

<h2 id="choisir">Comment choisir selon votre situation</h2>

<ul>
<li><strong>Immigration économique canadienne</strong> → un test, et pas n'importe lequel :
<a href="/tcf-canada/">TCF Canada</a> ou <a href="/tef-canada/">TEF Canada</a>. Aucune
alternative.</li>
<li><strong>Naturalisation ou titre de séjour français, dossier qui part vite</strong> → un test
IRN. Plus court, conçu pour ces démarches, et le
<a href="/blog/cpf-test-francais/">TCF IRN est finançable par le CPF</a>.</li>
<li><strong>Naturalisation ou titre de séjour, parcours étalé sur plusieurs années</strong> → un
diplôme. Un <a href="/delf-b1/">DELF B1</a> ou <a href="/delf-b2/">B2</a> ne périmera pas entre
deux étapes de votre dossier.</li>
<li><strong>Université française</strong> → les deux fonctionnent, mais le
<a href="/dalf/">DALF C1</a> dispense de test linguistique et pèse davantage en sélection.</li>
<li><strong>Projet québécois</strong> → un test, sauf si vous avez un DELF ou un DALF de moins de
deux ans avec les notes requises.</li>
<li><strong>Vous ne savez pas encore</strong> → le diplôme est le choix le plus robuste, parce
qu'il ne se périme pas pendant que votre projet se précise.</li>
</ul>
""",
"cta_h2": "Diplôme ou test, le format se prépare différemment",
"cta_p": """15 variantes couvertes au format officiel exact : barème sur 100 avec note
éliminatoire pour le DELF et le DALF, échelle 699 ou 499 avec niveau CECRL par épreuve pour le TCF
et le TEF, et le bon nombre d'écoutes dans chaque cas. Plus la correction IA de l'écrit et de
l'oral — dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Quelle est la différence entre le DELF et le TCF ?",
 """Le DELF est un diplôme d'État, acquis à vie, avec une note d'admission à 50/100 et une note
éliminatoire sous 5/25 : on peut le rater. Le TCF est un test de positionnement valable deux ans,
sans seuil : il vous situe sur une échelle et c'est l'organisme recevant votre dossier qui décide
si votre score suffit."""),
("Le DELF est-il accepté pour immigrer au Canada ?",
 """Pas pour l'immigration économique fédérale. Pour Entrée express, IRCC n'accepte que deux tests
de français : le TCF Canada et le TEF Canada. Ni le DELF, ni le DALF, ni le TCF Tout Public n'y
figurent — même un DALF C2 ne vaut rien pour un profil Entrée express. Pour la demande de
citoyenneté canadienne, en revanche, la liste est plus large et comprend le DELF et le DALF."""),
("Mon DELF ne périme-t-il vraiment jamais ?",
 """Le diplôme lui-même n'a pas de date d'expiration, et c'est son avantage central pour un dossier
français qui s'étale. Mais certaines démarches ajoutent leur propre condition de fraîcheur : le
Québec accepte les diplômes DELF et DALF en remplacement du TCF Québec seulement s'ils datent de
moins de deux ans, et avec une note minimale à l'oral. Le « à vie » est une propriété du diplôme,
pas une garantie d'acceptation."""),
("Combien d'écoutes a-t-on en compréhension orale ?",
 """Au DELF, les documents des niveaux A1 à B1 sont diffusés deux fois. Au TCF comme au TEF, il n'y
a qu'une seule écoute, sans retour arrière, dans toutes les versions sans exception. C'est la
différence pratique la plus sous-estimée : beaucoup de candidats entraînés sur des ressources DELF
la découvrent le jour de l'examen."""),
("Un test est-il plus rapide à passer qu'un diplôme ?",
 """Oui, nettement, pour les versions conçues pour les démarches administratives : 1 h 30 pour un
TEF IRN et 1 h 35 pour un TCF IRN, contre 2 h 10 pour un DELF B1, 2 h 50 pour un DELF B2 et 4 h
pour un DALF C1. Les versions Canada, elles, sont plus longues : 2 h 47 pour le TCF Canada et
2 h 55 pour le TEF Canada."""),
("Peut-on avoir les deux ?",
 """Rien ne l'interdit, et c'est même parfois rationnel : un diplôme comme socle permanent, et un
test récent quand une démarche précise l'exige. Mais c'est payer deux fois — commencez par
identifier ce que votre dossier demande réellement avant de cumuler."""),
],
"also": [
("/examens/", "Les 15 variantes d'examens couvertes",
 "Le panorama complet : à quoi sert chaque diplôme et chaque test."),
("/blog/difference-tcf-tef/", "TCF ou TEF : toutes les versions comparées",
 "Si vous avez tranché pour un test : les neuf versions côte à côte."),
("/blog/b1-ou-b2-nationalite-francaise/", "B1 ou B2 pour la nationalité française ?",
 "Quel niveau pour quelle démarche française, et comment le prouver."),
("/delf-b2/", "DELF B2 : le diplôme qui ouvre les universités françaises",
 "Format réformé, barème sur 100 et méthode épreuve par épreuve."),
],
"sources": """<strong>Les listes de justificatifs évoluent.</strong> Cette page est à jour au
7 août 2026. Chaque administration publie sa propre liste, avec ses conditions de note et de
validité — vérifiez celle de votre démarche sur
<a href="https://www.service-public.fr/" target="_blank" rel="noopener">service-public.fr</a>,
<a href="https://www.canada.ca/fr/services/immigration-citoyennete.html" target="_blank" rel="noopener">canada.ca</a>
ou <a href="https://www.quebec.ca/immigration" target="_blank" rel="noopener">quebec.ca</a>
avant de vous inscrire à quoi que ce soit.""",
},

# ─────────────────────────────────────────────────────────────────────────────
{
"slug": "repasser-tcf-tef",
"title": "Repasser le TCF ou le TEF : délais et reprise",
"desc": "Combien de temps attendre, peut-on repasser une seule épreuve, faut-il demander une nouvelle correction ? Les règles réelles, et là où les sources se contredisent.",
"og_title": "Repasser le TCF ou le TEF : délais et reprise",
"og_desc": "Combien de temps attendre, peut-on repasser une seule épreuve, et faut-il demander une nouvelle correction ? Les règles réelles.",
"crumb": "Repasser le TCF ou le TEF",
"h1": "Repasser le TCF ou le TEF : délais, reprise partielle et recours",
"date_fr": "7 août 2026",
"read": 6,
"accent": "accent-tcf",
"intro": """Trois réponses courtes. <strong>Le nombre de tentatives est illimité.</strong> La
<strong>reprise partielle n'existe pas</strong> sur les versions Canada et IRN : on repasse les
quatre épreuves. Et le délai d'attente est de <strong>20 jours</strong> — sauf que, côté TCF, la
documentation officielle se contredit elle-même. Voici ce qui est établi et ce qui ne l'est
pas.""",
"facts": [
"<strong>Tentatives illimitées</strong> au TCF comme au TEF.",
"⚠️ <strong>Aucune reprise partielle</strong> au TCF Canada ni aux versions IRN : les 4 épreuves, toujours.",
"<strong>TEF : 20 jours</strong> entre deux passations d'une même épreuve — sans ambiguïté.",
"⚠️ <strong>TCF : 20 ou 30 jours</strong> selon la page de FEI consultée. Faites confirmer par votre centre.",
"La <strong>nouvelle correction</strong> ne porte que sur les expressions — et la note peut <strong>baisser</strong>.",
"Seules les versions <strong>modulaires</strong> permettent de ne repasser qu'une épreuve.",
],
"toc": [
("delai", "Le délai entre deux passations"),
("contradiction", "Pourquoi le délai du TCF n'est pas fiable"),
("partielle", "Peut-on repasser une seule épreuve ?"),
("correction", "La nouvelle correction, et son risque"),
("combien", "Combien de fois peut-on repasser ?"),
("avant", "Ce qu'il faut faire avant de se réinscrire"),
],
"body": """
<h2 id="delai">Le délai entre deux passations</h2>

<p>Côté <strong>TEF</strong>, la règle est simple et documentée sans ambiguïté :
<strong>vingt jours</strong> entre deux passations d'une même épreuve, toutes versions
confondues. La rumeur d'un délai de 30 jours au TEF, qu'on lit régulièrement sur les forums, est
<strong>fausse</strong> : elle vient d'une confusion avec certaines fiches du TCF.</p>

<p>Côté <strong>TCF</strong>, c'est plus compliqué — et il faut le savoir avant de réserver un
vol ou de caler un dépôt de dossier.</p>

<h2 id="contradiction">Pourquoi le délai du TCF n'est pas fiable</h2>

<div class="note">
<p><strong>Les deux chiffres viennent de France Éducation international elle-même.</strong> Ses
pages de test annoncent <strong>20 jours</strong> pour le TCF Tout Public, le TCF Canada et le
TCF Québec. Plusieurs de ses fiches PDF et son Manuel du candidat annoncent
<strong>30 jours</strong>. Et pour le <a href="/tcf-irn/">TCF IRN</a>, la page et la fiche,
presque contemporaines, se contredisent.</p>
</div>

<p>Ce n'est pas une querelle d'experts : quinze jours d'écart peuvent faire manquer une échéance
de dossier. La conduite à tenir est donc simple, et elle vaut mieux que n'importe quel chiffre lu
en ligne :</p>

<ul>
<li><strong>Ne calez jamais une seconde tentative à la semaine près</strong> sur un délai trouvé
sur internet — le nôtre compris.</li>
<li><strong>Faites confirmer le délai par votre centre</strong> au moment où vous envisagez de
repasser. C'est lui qui gère les inscriptions et qui appliquera la règle en vigueur.</li>
<li><strong>Prévoyez la marge la plus défavorable</strong> — 30 jours — si votre dossier a une
date limite.</li>
</ul>

<h2 id="partielle">Peut-on repasser une seule épreuve ?</h2>

<p>Cela dépend entièrement de la version, et c'est un critère de choix qu'on néglige au moment de
l'inscription initiale.</p>

<div class="tablewrap">
<table>
<caption>Reprise partielle selon la version.</caption>
<thead><tr><th>Version</th><th>Peut-on ne repasser qu'une épreuve ?</th></tr></thead>
<tbody>
<tr><td><a href="/tcf-canada/">TCF Canada</a></td><td><strong>Non</strong> — les 4 épreuves, toujours</td></tr>
<tr><td><a href="/tef-canada/">TEF Canada</a></td><td><strong>Non</strong> pour l'immigration <em>(CO + EO seules pour la citoyenneté)</em></td></tr>
<tr><td><a href="/tcf-irn/">TCF IRN</a> · TEF IRN</td><td><strong>Non</strong> — épreuves officiellement « insécables »</td></tr>
<tr><td><a href="/tcf-quebec/">TCF Québec</a> · TEFAQ</td><td><strong>Oui</strong> — versions modulaires, 1 à 4 épreuves au choix</td></tr>
</tbody>
</table>
</div>

<p>La conséquence financière est directe. Sur une version non modulaire, une seule épreuve
décevante vous oblige à repayer et repasser l'intégralité du test. Sur le TCF Québec ou le TEFAQ,
vous vous réinscrivez à la seule épreuve que vous voulez améliorer — c'est un avantage
considérable, et l'une des raisons de préférer ces versions quand votre démarche le permet.</p>

<div class="note">
<p><strong>Attention à ne pas confondre modularité et reprise.</strong> Le TEF Canada permet de
ne s'inscrire qu'à la compréhension orale et à l'expression orale — mais uniquement si votre
démarche est une <em>demande de citoyenneté canadienne</em>. Pour l'immigration économique, les
quatre épreuves restent obligatoires.</p>
</div>

<h2 id="correction">La nouvelle correction, et son risque</h2>

<p>Il existe une voie de recours qui n'implique pas de repasser le test : la <strong>demande de
nouvelle correction</strong>. Elle est utile à connaître, et dangereuse à utiliser sans réfléchir.</p>

<ul>
<li>Elle ne porte que sur les <strong>épreuves d'expression</strong> — écrite et orale. Jamais sur
les QCM, qui sont corrigés automatiquement.</li>
<li>Elle doit être déposée <strong>dans le mois</strong> suivant l'envoi des attestations au
centre.</li>
<li><strong>La nouvelle note remplace l'ancienne, même si elle est plus basse.</strong></li>
</ul>

<div class="note">
<p><strong>C'est un pari, pas un recours gratuit.</strong> Vous ne demandez pas un avis
supplémentaire : vous demandez une <em>nouvelle</em> note qui écrasera la précédente. Ne l'engagez
que si vous avez une raison sérieuse de penser que votre production a été sous-évaluée — par
exemple un écart franc avec vos résultats d'entraînement corrigés sur les mêmes critères. Un
simple « j'espérais mieux » n'en est pas une.</p>
</div>

<h2 id="combien">Combien de fois peut-on repasser ?</h2>

<p><strong>Autant de fois que vous le souhaitez.</strong> Ni le TCF ni le TEF ne limitent le
nombre de tentatives — la seule contrainte est le délai entre deux passations, et le fait que
chaque tentative se paie plein tarif.</p>

<p>C'est précisément là que se situe le vrai coût. Un TCF Canada, c'est 195 à 285 € en France et
400 à 440 $CA au Canada ; un <a href="/tcf-irn/">TCF IRN</a>, de 135 à 220 €. Repasser trois fois
un test qu'on n'était pas prêt à réussir revient plus cher que n'importe quelle préparation. Le
détail des tarifs relevés est dans notre article
<a href="/blog/prix-tcf-tef/">combien coûte vraiment le TCF ou le TEF</a>.</p>

<h2 id="avant">Ce qu'il faut faire avant de se réinscrire</h2>

<p>Repasser le même test dans les mêmes conditions donne généralement le même résultat. Trois
étapes changent réellement l'issue.</p>

<ol>
<li><strong>Identifier l'épreuve qui a plafonné votre dossier</strong>, pas celle qui vous a déçu.
Au TCF et au TEF, il n'y a aucune compensation : c'est votre score le plus bas qui compte. Si vous
avez raté votre objectif d'un point en expression écrite, tout le reste est du bruit.</li>
<li><strong>Travailler cette épreuve spécifiquement</strong>, pas le français en général. Entre
deux tentatives séparées de vingt à trente jours, seul un travail ciblé peut produire un écart
mesurable.</li>
<li><strong>Vérifier le gain avant de payer</strong>, avec un examen blanc noté au format et au
barème officiels. Si votre score simulé n'a pas bougé, votre score réel ne bougera pas non
plus.</li>
</ol>

<p>Sur les expressions, le point aveugle est structurel : vous ne pouvez pas vous auto-évaluer sur
des critères que vous ne connaissez pas. Savoir si vous êtes passé de 9 à 11 sur 20 — soit,
souvent, d'un niveau à l'autre — demande une correction sur les grilles officielles.</p>
""",
"cta_h2": "Vérifiez le gain avant de repayer le test",
"cta_p": """Examens blancs chronométrés au format officiel de votre déclinaison, score par épreuve
sur l'échelle réelle, conversion NCLC ou Échelle québécoise, et correction IA de l'écrit et de
l'oral sur les critères officiels. Pour savoir si votre niveau a bougé — avant de repayer 200 € ou
440 $. Dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Combien de temps faut-il attendre pour repasser le TCF ?",
 """Les pages de test de France Éducation international annoncent 20 jours, mais plusieurs de ses
fiches PDF et son Manuel du candidat annoncent 30 jours — et pour le TCF IRN, la page et la fiche
se contredisent. Ne calez pas une seconde tentative à la semaine près : faites confirmer le délai
par votre centre, et prévoyez la marge la plus défavorable si votre dossier a une date limite."""),
("Combien de temps faut-il attendre pour repasser le TEF ?",
 """Vingt jours entre deux passations d'une même épreuve, toutes versions du TEF confondues. Ici,
contrairement au TCF, la documentation est sans ambiguïté. La rumeur d'un délai de 30 jours au TEF
est fausse : elle vient d'une confusion avec certaines fiches du TCF."""),
("Puis-je repasser seulement l'épreuve que j'ai ratée ?",
 """Pas au TCF Canada ni aux versions IRN, dont les épreuves sont officiellement insécables : c'est
le test complet ou rien. En revanche, le TCF Québec et le TEFAQ sont modulaires — vous vous
inscrivez à 1 à 4 épreuves au choix, donc vous pouvez ne repasser que celle que vous voulez
améliorer."""),
("Combien de fois peut-on repasser le TCF ou le TEF ?",
 """Autant de fois que vous le souhaitez : ni l'un ni l'autre ne limite le nombre de tentatives.
Les seules contraintes sont le délai entre deux passations et le fait que chaque tentative se paie
plein tarif — de 135 à 285 € en France selon la version et le centre."""),
("Qu'est-ce que la demande de nouvelle correction ?",
 """Une voie de recours qui ne porte que sur les épreuves d'expression, jamais sur les QCM, et
qu'il faut déposer dans le mois suivant l'envoi des attestations au centre. Attention : la
nouvelle note remplace l'ancienne, même si elle est plus basse. Ce n'est pas un avis
supplémentaire, c'est un pari."""),
("Faut-il repasser le test ou demander une nouvelle correction ?",
 """La nouvelle correction n'a de sens que si vous avez une raison sérieuse de penser que votre
production a été sous-évaluée — par exemple un écart franc avec vos résultats d'entraînement
corrigés sur les mêmes critères. Si votre niveau réel est simplement en dessous de l'objectif,
c'est un travail ciblé puis une nouvelle passation qu'il faut, pas un recours."""),
],
"also": [
("/blog/prix-tcf-tef/", "Combien coûte vraiment le TCF ou le TEF ?",
 "Chaque tentative se paie plein tarif : les prix relevés centre par centre."),
("/blog/validite-attestation-tcf-tef/", "Validité de l'attestation : 2 ans à partir de quand ?",
 "L'autre horloge à surveiller quand un dossier s'étale."),
("/examens-blancs/", "Examens blancs au format officiel",
 "Le protocole pour vérifier que votre niveau a réellement bougé."),
("/blog/tcf-canada-nclc-7/", "NCLC 7 au TCF Canada : quel score viser exactement",
 "Les seuils par épreuve, pour savoir laquelle a réellement plafonné votre dossier."),
],
"sources": """<strong>Les règles de passation évoluent, et se contredisent parfois.</strong> Cette
page est à jour au 7 août 2026 et signale explicitement les points où la documentation officielle
n'est pas cohérente avec elle-même. Faites confirmer les délais et les modalités de reprise par
votre centre agréé avant de planifier une seconde tentative.""",
},

# ─────────────────────────────────────────────────────────────────────────────
{
"slug": "validite-attestation-tcf-tef",
"title": "Validité du TCF et du TEF : 2 ans à partir de quand",
"desc": "Deux ans, oui — mais à compter de quelle date ? Les pages officielles du TEF se contredisent, et la règle IRCC est plus stricte qu'il n'y paraît. Ce qu'il faut anticiper.",
"og_title": "Validité du TCF et du TEF : 2 ans à partir de quand",
"og_desc": "Deux ans, mais à compter de quelle date ? Les pages officielles du TEF se contredisent, et la règle IRCC est plus stricte qu'il n'y paraît.",
"crumb": "Validité de l'attestation",
"h1": "Validité du TCF et du TEF : deux ans, mais à partir de quand ?",
"date_fr": "7 août 2026",
"read": 6,
"accent": "accent-tcf",
"intro": """<strong>Deux ans</strong> pour le TCF comme pour le TEF. La question qui compte
vraiment, et à laquelle presque personne ne répond correctement, c'est <strong>à partir de quelle
date</strong> ce délai court — et pour le TEF, les pages officielles ne disent pas la même chose.
S'y ajoute une règle IRCC qui piège les dossiers canadiens longs.""",
"facts": [
"<strong>2 ans</strong> pour le TCF et le TEF. Les diplômes DELF et DALF, eux, <strong>n'expirent pas</strong>.",
"TCF : à compter de la <strong>date de délivrance de l'attestation</strong>.",
"⚠️ TEF : les pages officielles disent <strong>« date d'édition »</strong> <em>ou</em> <strong>« date de passation »</strong> selon celle qu'on lit.",
"⚠️ <strong>IRCC</strong> : résultats de moins de 2 ans à la création du profil Entrée express <strong>et</strong> au dépôt de la demande.",
"⚠️ <strong>Québec</strong> : un DELF ou DALF doit dater de moins de 2 ans — le « à vie » ne joue pas.",
"En cas de doute, retenez <strong>la date la plus défavorable</strong> pour vous.",
],
"toc": [
("principe", "Le principe : deux ans"),
("tef", "Le TEF : deux dates de départ selon la page"),
("ircc", "La règle IRCC, plus stricte qu'il n'y paraît"),
("quebec", "Au Québec, même les diplômes ont une date"),
("france", "Côté français : ce qui n'expire pas"),
("planifier", "Comment planifier sans se faire piéger"),
],
"body": """
<h2 id="principe">Le principe : deux ans</h2>

<p>Le TCF et le TEF sont des <strong>tests de positionnement</strong>, pas des diplômes : ils
photographient votre niveau à un instant donné, et cette photographie est réputée valable
<strong>deux ans</strong>. Passé ce délai, l'attestation ne prouve plus rien, quelle que soit la
qualité de votre score.</p>

<p>Pour le <strong>TCF</strong>, le point de départ est clair : la <strong>date de délivrance de
l'attestation</strong>. Pour le TEF, c'est là que ça se complique.</p>

<h2 id="tef">Le TEF : deux dates de départ selon la page</h2>

<div class="note">
<p><strong>Sur ce point précis, les pages du Français des affaires ne disent pas la même
chose.</strong> Ses <em>conditions d'inscription</em> font courir la validité « à compter de la
date d'édition » de l'attestation, tandis que sa <em>page de présentation</em> du TEF parle de
deux ans « à partir de la date de passation ».</p>
</div>

<p>L'écart entre les deux peut atteindre <strong>plusieurs semaines</strong> — le temps qui sépare
le jour de l'examen de l'émission du document. La plupart du temps, cela n'a aucune conséquence.
Mais si votre dossier est déposé juste avant l'échéance, c'est exactement le genre de détail qui
décide de sa recevabilité.</p>

<p><strong>La conduite à tenir</strong> : retenez la <strong>date la plus défavorable pour
vous</strong> — donc la date de passation, qui est la plus ancienne — et faites confirmer par
votre centre si l'échéance est serrée. Mieux vaut repasser un test un mois trop tôt que voir un
dossier rejeté pour une attestation périmée de dix jours.</p>

<h2 id="ircc">La règle IRCC, plus stricte qu'il n'y paraît</h2>

<p>Pour un dossier d'immigration canadienne, la règle des deux ans ne s'applique pas une fois,
mais <strong>deux</strong>. Vos résultats doivent avoir moins de deux ans :</p>

<ol>
<li><strong>au moment où vous créez votre profil Entrée express</strong>, <em>et</em></li>
<li><strong>au moment où vous déposez votre demande de résidence permanente</strong>.</li>
</ol>

<div class="note">
<p><strong>Le piège des dossiers longs.</strong> Entre la création d'un profil et l'invitation à
présenter une demande, il peut s'écouler de nombreux mois. Un test passé trop tôt dans la démarche
<strong>peut expirer entre les deux étapes</strong> — et il faut alors le repasser en entier,
puisqu'il n'existe aucune reprise partielle au <a href="/tcf-canada/">TCF Canada</a> ni au
<a href="/tef-canada/">TEF Canada</a>.</p>
</div>

<p>La conséquence pratique est contre-intuitive : <strong>passer son test le plus tôt possible
n'est pas la bonne stratégie</strong> pour un dossier canadien. Mieux vaut le passer quand votre
profil est prêt à être créé, de façon à disposer de la plus grande fenêtre possible avant le dépôt
de la demande de résidence permanente.</p>

<h2 id="quebec">Au Québec, même les diplômes ont une date</h2>

<p>Voici la nuance que presque aucun comparatif ne relève. Pour les programmes québécois, les
résultats doivent dater de <strong>deux ans ou moins à la date de votre demande de sélection
permanente</strong>. Jusqu'ici, rien d'inhabituel.</p>

<p>Mais le Québec accepte aussi les <strong>diplômes DELF et DALF</strong> en remplacement du
<a href="/tcf-quebec/">TCF Québec</a> — et il leur applique la même condition : une note minimale
en compréhension orale et en expression orale, <em>et</em> une validité de <strong>moins de deux
ans</strong>.</p>

<p>Autrement dit : au Québec, <strong>l'avantage du diplôme disparaît</strong>. Votre DELF B2
obtenu il y a cinq ans ne vous dispense de rien, alors qu'il resterait pleinement valable pour un
dossier français. C'est une exception importante à la règle générale du « diplôme à vie ».</p>

<h2 id="france">Côté français : ce qui n'expire pas</h2>

<p>Pour les démarches françaises, la logique s'inverse et joue en faveur des diplômes.</p>

<div class="tablewrap">
<table>
<caption>Durée de vie des justificatifs selon leur nature.</caption>
<thead><tr><th>Justificatif</th><th>Durée de validité</th></tr></thead>
<tbody>
<tr><td>Attestation <a href="/tcf-irn/">TCF IRN</a> ou TEF IRN</td><td><strong>2 ans</strong></td></tr>
<tr><td>Diplôme <a href="/delf-b1/">DELF</a> ou <a href="/dalf/">DALF</a></td><td><strong>aucune expiration</strong></td></tr>
<tr><td>Diplôme français (brevet, CAP…)</td><td><strong>aucune expiration</strong></td></tr>
</tbody>
</table>
</div>

<p>C'est décisif quand un parcours administratif s'étale. Un candidat qui obtient une carte de
résident avec un <a href="/delf-b1/">DELF B1</a>, puis demande la nationalité cinq ans plus tard,
n'a pas à s'inquiéter de la péremption de son premier justificatif — il devra en revanche
justifier du <a href="/blog/b1-ou-b2-nationalite-francaise/">B2 exigé depuis 2026</a>, ce qui est
une autre question.</p>

<h2 id="planifier">Comment planifier sans se faire piéger</h2>

<ul>
<li><strong>Datez votre échéance à l'envers.</strong> Partez de la date probable de dépôt de votre
dossier, retirez deux ans : c'est la date la plus ancienne à laquelle votre test peut avoir été
passé.</li>
<li><strong>Pour un dossier canadien, comptez deux échéances</strong>, pas une : création du
profil <em>et</em> dépôt de la demande de résidence permanente.</li>
<li><strong>Retenez la date de passation, pas celle d'édition</strong>, quand la source est
ambiguë. Vous perdez quelques semaines de validité théorique et vous gagnez la certitude.</li>
<li><strong>Si votre parcours doit durer, préférez un diplôme</strong> — sauf pour un projet
québécois, où la condition de fraîcheur s'applique aussi aux diplômes.</li>
<li><strong>Ne passez pas votre test « pour être tranquille ».</strong> Un test passé deux ans
trop tôt est un test à repayer. Vérifiez plutôt votre niveau avec un
<a href="/examens-blancs/">examen blanc au format officiel</a>, qui ne périme pas, lui.</li>
</ul>
""",
"cta_h2": "Un test périmé se repasse en entier",
"cta_p": """Aucune reprise partielle n'existe au TCF Canada ni aux versions IRN : une attestation
expirée, c'est quatre épreuves à repasser et à repayer. Examens blancs au format officiel, score
par épreuve et correction IA de l'écrit et de l'oral — pour ne passer le vrai test qu'une seule
fois, au bon moment. Dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
"faq": [
("Combien de temps une attestation TCF ou TEF est-elle valable ?",
 """Deux ans dans les deux cas. Pour le TCF, le délai court à compter de la date de délivrance de
l'attestation. Pour le TEF, les pages officielles se contredisent : les conditions d'inscription
parlent de la date d'édition, la page de présentation de la date de passation. Retenez la date la
plus défavorable pour vous."""),
("À partir de quelle date court la validité du TEF ?",
 """Cela dépend de la page que vous consultez, et c'est un vrai problème : les conditions
d'inscription du Français des affaires font courir la validité à compter de la date d'édition de
l'attestation, tandis que sa page de présentation parle de la date de passation. L'écart peut
atteindre plusieurs semaines. Prenez la date de passation, la plus ancienne, et faites confirmer
par votre centre si l'échéance est serrée."""),
("Mon test doit-il être valide au dépôt de ma demande canadienne ?",
 """Oui, et à deux moments plutôt qu'un : vos résultats doivent avoir moins de deux ans au moment
où vous créez votre profil Entrée express et au moment où vous déposez votre demande de résidence
permanente. Comme plusieurs mois peuvent s'écouler entre les deux, un test passé trop tôt peut
expirer en cours de route."""),
("Faut-il passer son test le plus tôt possible ?",
 """Non, et c'est contre-intuitif. Pour un dossier canadien, un test passé très en amont risque
d'expirer entre la création du profil et le dépôt de la demande. Mieux vaut le passer quand votre
profil est prêt à être créé, pour disposer de la plus grande fenêtre possible ensuite."""),
("Un DELF ou un DALF expire-t-il ?",
 """Le diplôme lui-même n'a pas de date d'expiration, et c'est son avantage pour les démarches
françaises. Mais le Québec applique sa propre condition : un DELF ou un DALF n'y est accepté en
remplacement du TCF Québec que s'il date de moins de deux ans, avec une note minimale à l'oral.
L'avantage du diplôme disparaît donc pour un projet québécois."""),
("Que se passe-t-il si mon attestation expire en cours de dossier ?",
 """Il faut repasser le test — et en entier, puisqu'il n'existe aucune reprise partielle au TCF
Canada ni aux versions IRN. C'est quatre épreuves à repasser et le tarif complet à repayer, entre
135 et 285 € en France selon la version et le centre."""),
],
"also": [
("/blog/repasser-tcf-tef/", "Repasser le TCF ou le TEF : délais et reprise",
 "Ce qu'il faut savoir si votre attestation a expiré ou si votre score est insuffisant."),
("/blog/diplome-ou-test-delf-tcf/", "Diplôme ou test : lequel vous faut-il ?",
 "Le critère décisif quand un parcours administratif doit s'étaler dans le temps."),
("/blog/tcf-ou-tef-canada/", "TCF ou TEF Canada : lequel choisir ?",
 "Les tables NCLC, les formats et les délais des deux tests acceptés par IRCC."),
("/blog/b1-ou-b2-nationalite-francaise/", "B1 ou B2 pour la nationalité française ?",
 "Quel niveau pour quelle démarche, et quel justificatif choisir."),
],
"sources": """<strong>Les règles de validité évoluent, et se contredisent parfois.</strong> Cette
page est à jour au 7 août 2026 et signale explicitement les points où la documentation officielle
n'est pas cohérente avec elle-même. Vérifiez la date de départ exacte auprès de votre centre et
les exigences de votre démarche sur
<a href="https://www.canada.ca/fr/services/immigration-citoyennete.html" target="_blank" rel="noopener">canada.ca</a>,
<a href="https://www.quebec.ca/immigration" target="_blank" rel="noopener">quebec.ca</a> ou
<a href="https://www.service-public.fr/" target="_blank" rel="noopener">service-public.fr</a>.""",
},

]

if __name__ == "__main__":
    print("Batch 2 :")
    build(ARTICLES)
