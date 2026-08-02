#!/usr/bin/env python3
"""Génère les pages intérieures du site (piliers, blog, support, 404).
Usage : python3 generate.py — écrit les index.html dans les dossiers du site.
La landing (index.html racine) et /confidentialite/ sont gérées à part.

⚠️  ATTENTION (02/08/2026) : ce générateur a DÉRIVÉ des pages en ligne.
Le relancer tel quel écrase du contenu écrit à la main — constaté :
/blog/ (−89 lignes), /tcf-irn/ (−53), /tef-canada/ (−33), /tcf-canada/ (−29),
et sitemap.xml retombe de 18 à 11 URLs (les pages /examens/, /contenu/,
/correction-ia/, /plan-etude/, /score-tcf-699/, /tcf-quebec/, /a-propos/
et les articles de blog disparaissent).
Resynchroniser PAGES[] sur les fichiers réels avant tout nouvel usage,
et vérifier `git diff` après exécution."""
import html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://delf-tcf-tef.fr"
APP_ID = "6790412304"
APP_URL = f"https://apps.apple.com/fr/app/tcf-delf-tef-tests-2026/id{APP_ID}"

HEAD = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{base}{url}">
<link rel="stylesheet" href="/style.css">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/img/favicon-96.png" sizes="96x96" type="image/png">
<link rel="icon" href="/img/favicon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="/img/icon-180.png">
<meta name="apple-itunes-app" content="app-id=6790412304">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{base}/img/favicon-512.png">
<meta property="og:url" content="{base}{url}">
<meta property="og:type" content="article">
{jsonld}</head>
<body class="{accent}">
<header class="site"><div class="wrap">
  <a class="logo" href="/"><img src="/img/icon-180.png" alt="" width="30" height="30">DELF&nbsp;·&nbsp;TCF&nbsp;·&nbsp;TEF</a>
  <nav class="main">
    <a href="/tcf-canada/">TCF Canada</a>
    <a href="/tcf-irn/">TCF IRN</a>
    <a href="/delf-b2/">DELF</a>
    <a href="/examens-blancs/">Examens blancs</a>
    <a href="/blog/">Blog</a>
  </nav>
</div></header>
<article class="page"><div class="wrap narrow">
<p class="crumb"><a href="/">Accueil</a> › {crumb}</p>
<h1>{h1}</h1>
<p class="intro">{intro}</p>
"""

CTA = f"""<div class="cta-band">
<h2>Entraînez-vous en conditions réelles</h2>
<p>Examens blancs chronométrés au format officiel, correction IA de l'écrit et de
l'oral, plan d'étude personnalisé — dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».</p>
<a class="btn" href="{APP_URL}">Télécharger sur l'App&nbsp;Store</a>
</div>
"""

FOOT = """</div></article>
<footer class="site"><div class="wrap">
  <div class="cols">
    <div><h4>Examens</h4><ul>
      <li><a href="/tcf-canada/">TCF Canada</a></li>
      <li><a href="/tcf-irn/">TCF IRN (naturalisation)</a></li>
      <li><a href="/tef-canada/">TEF Canada · TEFAQ</a></li>
      <li><a href="/delf-b2/">DELF B2</a></li>
      <li><a href="/delf-b1/">DELF B1</a></li>
      <li><a href="/dalf/">DALF C1 · C2</a></li>
    </ul></div>
    <div><h4>Ressources</h4><ul>
      <li><a href="/examens-blancs/">Examens blancs</a></li>
      <li><a href="/blog/">Blog</a></li>
      <li><a href="https://naturalisationfrancefacile.fr">Naturalisation France Facile</a></li>
    </ul></div>
    <div><h4>Application</h4><ul>
      <li><a href="https://apps.apple.com/fr/app/tcf-delf-tef-tests-2026/id6790412304">Télécharger sur l'App&nbsp;Store</a></li>
      <li><a href="/support/">Support / Contact</a></li>
      <li><a href="/confidentialite/">Politique de confidentialité</a></li>
    </ul></div>
  </div>
  <p class="legal">Application non officielle, non affiliée à France Éducation International
  (DELF, DALF, TCF) ni au Français des affaires — CCI Paris Île-de-France (TEF). Les noms
  d'examens sont cités uniquement pour décrire le contenu de préparation.
  © 2026 delf-tcf-tef.fr</p>
</div></footer>
</body>
</html>
"""

def faq_block(faq):
    if not faq:
        return "", ""
    items = "\n".join(
        f"<details><summary>{q}</summary>\n<p>{a}</p></details>" for q, a in faq)
    strip = lambda s: html.unescape(re.sub(r"<[^>]+>", "", s))
    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": strip(q),
                          "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
                         for q, a in faq]}
    return (f'<h2>Questions fréquentes</h2>\n<div class="faq">\n{items}\n</div>\n',
            '<script type="application/ld+json">\n'
            + json.dumps(ld, ensure_ascii=False) + "\n</script>\n")

def breadcrumb_ld(p):
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList",
          "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE + "/"},
              {"@type": "ListItem", "position": 2, "name": p["crumb"],
               "item": BASE + p["url"]}]}
    return ('<script type="application/ld+json">\n'
            + json.dumps(ld, ensure_ascii=False) + "\n</script>\n")

def write_page(p):
    faq_html, faq_ld = faq_block(p.get("faq"))
    out = (HEAD.format(base=BASE, title=p["title"], desc=p["desc"], url=p["url"],
                       accent=p.get("accent", ""), crumb=p["crumb"], h1=p["h1"],
                       intro=p["intro"], jsonld=faq_ld + breadcrumb_ld(p))
           + p["body"] + (CTA if p.get("cta", True) else "") + faq_html + FOOT)
    path = os.path.join(ROOT, p["url"].strip("/"), "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    print("écrit :", p["url"])

PAGES = [
# ---------------------------------------------------------------- TCF Canada
{"url": "/tcf-canada/", "accent": "accent-tcf", "crumb": "TCF Canada",
 "title": "TCF Canada 2026 : format, scores NCLC et préparation",
 "desc": "Le guide du TCF Canada : les 4 épreuves, la conversion des scores en NCLC, les seuils pour Entrée express et comment vous préparer efficacement.",
 "h1": "TCF Canada : réussir le test pour votre immigration au Canada",
 "intro": "Le TCF Canada est l'un des deux tests de français reconnus par IRCC (Immigration, Réfugiés et Citoyenneté Canada) pour la résidence permanente, Entrée express et la citoyenneté. Vos résultats sont convertis en niveaux NCLC — et chaque niveau gagné peut valoir des dizaines de points.",
 "body": """<div class="facts"><strong>L'essentiel</strong><ul>
<li>4 épreuves obligatoires : compréhension orale, compréhension écrite, expression écrite, expression orale.</li>
<li>Résultats sur l'échelle TCF (100–699), convertis en <strong>NCLC</strong> pour votre dossier IRCC.</li>
<li>Attestation valable <strong>2 ans</strong> pour les démarches d'immigration.</li>
<li>NCLC 7 est le seuil visé par la plupart des candidats ; les points bonus du français montent fortement jusqu'à NCLC 9.</li>
</ul></div>
<h2>Comment se préparer efficacement</h2>
<p>La difficulté du TCF Canada n'est pas seulement linguistique : c'est un test de
<em>format</em>. Questions à enchaînement rapide en compréhension, consignes strictes en
expression, chronomètre serré. Les candidats qui échouent de peu sont presque toujours
ceux qui découvrent le format le jour de l'examen.</p>
<p>La méthode qui fonctionne :</p>
<ol>
<li><strong>Un examen blanc complet dès le départ</strong> pour situer votre NCLC actuel par épreuve.</li>
<li><strong>Un entraînement ciblé sur votre épreuve faible</strong> — c'est elle qui plafonne votre dossier, car IRCC retient le profil complet.</li>
<li><strong>Des examens blancs chronométrés réguliers</strong> jusqu'à ce que le format ne vous surprenne plus.</li>
</ol>""",
 "faq": [
  ("TCF Canada ou TEF Canada : lequel choisir ?",
   "Les deux sont acceptés par IRCC et testent les mêmes compétences. Le TCF est souvent perçu comme plus direct en compréhension (QCM), le TEF a des formats de tâches différents à l'écrit. Essayez un examen blanc de chaque et choisissez celui où votre score est le plus haut — c'est le seul critère qui compte. Voir aussi <a href=\"/tef-canada/\">notre page TEF Canada</a>."),
  ("Quel score faut-il pour Entrée express ?",
   "Cela dépend de votre programme et de votre profil. NCLC 7 dans les 4 épreuves est le seuil de référence du Programme des travailleurs qualifiés, et les points du facteur langue augmentent jusqu'à NCLC 9-10. Vérifiez toujours le seuil exact de votre programme sur le site d'IRCC."),
  ("Combien de temps de préparation prévoir ?",
   "Avec un niveau B1-B2 réel, comptez 4 à 8 semaines d'entraînement régulier axé sur le format pour stabiliser un NCLC 7+. L'app calcule votre score de préparation et adapte le plan à votre date d'examen."),
 ]},
# ---------------------------------------------------------------- TCF IRN
{"url": "/tcf-irn/", "accent": "accent-irn", "crumb": "TCF IRN",
 "title": "TCF IRN 2026 : le test pour la naturalisation — guide",
 "desc": "TCF IRN : niveaux exigés depuis 2026 (B2 naturalisation, B1 carte de résident), format réformé 2025 et méthode de préparation pour réussir du premier coup.",
 "h1": "TCF IRN : le test de français pour votre naturalisation",
 "intro": "Le TCF IRN (Intégration, Résidence, Nationalité) atteste votre niveau de français pour les démarches en France : naturalisation, carte de résident, carte pluriannuelle. Depuis le 1er janvier 2026, les niveaux exigés ont été relevés — bien se préparer n'a jamais été aussi important.",
 "body": """<div class="facts"><strong>Les niveaux exigés depuis le 1<sup>er</sup> janvier 2026</strong><ul>
<li><strong>Naturalisation française : niveau B2</strong> (oral et écrit) — c'était B1 auparavant.</li>
<li><strong>Carte de résident (10 ans) : niveau B1</strong> — c'était A2.</li>
<li><strong>Carte de séjour pluriannuelle : niveau A2.</strong></li>
<li>Ces exigences résultent de la loi immigration du 26 janvier 2024, applicable aux demandes déposées depuis 2026.</li>
</ul></div>
<h2>Un test réformé en 2025</h2>
<p>Le TCF IRN a été réformé en mai 2025 pour accompagner ces nouvelles exigences :
4 épreuves (compréhension orale, compréhension écrite, expression écrite, expression
orale) qui évaluent désormais jusqu'au niveau B2. L'attestation est valable 2 ans.</p>
<h2>Le piège du passage à B2</h2>
<p>La marche entre B1 et B2 est la plus haute de l'échelle CECRL : argumenter à l'écrit,
développer un point de vue à l'oral, comprendre des documents plus abstraits. Beaucoup de
candidats à la naturalisation ont un français oral fluide du quotidien mais échouent sur
l'écrit argumenté. Le diagnostic honnête — un examen blanc complet noté sur les grilles
officielles — est la première étape ; l'entraînement ciblé sur l'expression écrite fait
ensuite la différence.</p>
<p>Vous préparez aussi l'entretien de naturalisation et l'examen civique ? Notre app sœur
<a href="https://naturalisationfrancefacile.fr">Naturalisation France Facile</a> couvre
cette partie de votre dossier.</p>""",
 "faq": [
  ("TCF IRN ou TEF IRN : quelle différence ?",
   "Les deux sont acceptés par l'administration française et couvrent les mêmes niveaux. Ils diffèrent par l'opérateur (France Éducation International vs Le français des affaires), les centres disponibles et le format des tâches. Choisissez selon les dates et centres près de chez vous — et entraînez-vous au format exact du test choisi."),
  ("Mon DELF B1 obtenu il y a des années est-il encore valable ?",
   "Le DELF est un diplôme valable à vie, et il reste accepté comme preuve de niveau — mais attention : pour la naturalisation, c'est désormais le niveau B2 qui est exigé pour les demandes déposées depuis le 1er janvier 2026. Un DELF B1 suffit en revanche pour la carte de résident."),
  ("Que se passe-t-il si j'échoue ?",
   "Vous pouvez repasser le test (délai d'attente entre deux sessions et nouveaux frais d'inscription). D'où l'intérêt de ne s'inscrire qu'une fois prêt : un examen blanc noté vous dit précisément où vous en êtes avant de payer."),
 ]},
# ---------------------------------------------------------------- TEF Canada
{"url": "/tef-canada/", "accent": "accent-tef", "crumb": "TEF Canada · TEFAQ",
 "title": "TEF Canada et TEFAQ 2026 : format, CLB et préparation",
 "desc": "TEF Canada pour Entrée express, TEFAQ pour le Québec (PEQ, Arrima) : épreuves, conversion CLB/NCLC et méthode de préparation efficace.",
 "h1": "TEF Canada et TEFAQ : le français qui ouvre le Canada et le Québec",
 "intro": "Le TEF Canada est reconnu par IRCC pour la résidence permanente et la citoyenneté ; le TEFAQ est la version acceptée par le Québec (Arrima, PEQ). Dans les deux cas, vos résultats se convertissent en niveaux CLB/NCLC — le nerf de la guerre de votre dossier.",
 "body": """<div class="facts"><strong>L'essentiel</strong><ul>
<li><strong>TEF Canada</strong> : 4 épreuves (compréhension et expression, écrites et orales) pour IRCC.</li>
<li><strong>TEFAQ</strong> : le Québec exige surtout l'oral (compréhension + expression) ; l'écrit peut s'ajouter selon votre programme.</li>
<li>Résultats convertis en <strong>NCLC/CLB</strong> ; attestation valable 2 ans.</li>
<li>Le TEF IRN (démarches en France) a été réformé en avril 2025 — compréhension orale portée à 30 minutes en deux blocs adaptatifs.</li>
</ul></div>
<h2>La spécificité du TEF : des formats de tâches à apprivoiser</h2>
<p>Le TEF a ses propres codes : tâches d'expression écrite normées (fait divers à
compléter, argumentation), épreuve orale structurée en interactions simulées. Ces
formats se travaillent — un candidat entraîné gagne régulièrement un niveau CLB complet
par rapport à son premier essai, à français égal.</p>
<p>Notre app propose les variantes TEF Canada, TEFAQ, TEF IRN et TEF Études avec
épreuves au format exact, notation sur l'échelle officielle et conversion NCLC/CLB et
Échelle québécoise automatique.</p>""",
 "faq": [
  ("Quel niveau CLB pour immigrer au Québec ?",
   "Arrima et le PEQ valorisent un oral de niveau 7+ ; les seuils exacts dépendent du programme et évoluent. Vérifiez les exigences en vigueur sur le site du MIFI, puis entraînez-vous jusqu'à dépasser le seuil avec de la marge en examen blanc."),
  ("Le TEF est-il plus facile que le TCF ?",
   "Ni plus facile ni plus difficile : les deux évaluent les mêmes compétences sur les mêmes échelles. La vraie question est : dans quel format êtes-vous le plus à l'aise ? Faites un examen blanc de chaque et comparez vos scores."),
  ("Puis-je passer uniquement l'oral au TEFAQ ?",
   "Oui, le TEFAQ permet de ne passer que les épreuves orales si votre programme ne demande que cela — c'est le cas le plus courant pour Arrima. Confirmez les épreuves requises pour votre situation avant de vous inscrire."),
 ]},
# ---------------------------------------------------------------- DELF B2
{"url": "/delf-b2/", "accent": "accent-delf", "crumb": "DELF B2",
 "title": "DELF B2 2026 : épreuves, barème et méthode pour réussir",
 "desc": "Tout sur le DELF B2 : les 4 épreuves sur 100 points, les seuils à connaître, le format 2020 en QCM et une méthode de préparation épreuve par épreuve.",
 "h1": "DELF B2 : le diplôme qui ouvre les universités françaises",
 "intro": "Le DELF B2 est le sésame le plus demandé : admission à l'université française, candidatures, preuve de niveau valable à vie. C'est aussi un examen exigeant, où la méthode compte autant que le niveau de langue.",
 "body": """<div class="facts"><strong>L'essentiel</strong><ul>
<li>4 épreuves notées chacune sur 25 : compréhension orale, compréhension écrite, production écrite, production orale. Total sur <strong>100</strong>.</li>
<li>Admission à partir de <strong>50/100</strong> — mais une note inférieure à <strong>5/25</strong> à une épreuve est éliminatoire.</li>
<li>Depuis la réforme 2020, les compréhensions sont <strong>100 % QCM</strong>.</li>
<li>Diplôme <strong>valable à vie</strong>, délivré par le ministère de l'Éducation nationale.</li>
</ul></div>
<h2>Où se joue la réussite</h2>
<p>La production écrite (prise de position argumentée : lettre formelle, essai, article)
est l'épreuve la plus discriminante : structure attendue, connecteurs logiques, registre
formel. À l'oral, vous défendez un point de vue à partir d'un court document, puis
débattez avec le jury — la préparation en temps limité se travaille spécifiquement.</p>
<p>La stratégie gagnante : viser 15+/25 sur vos épreuves fortes pour sécuriser la
moyenne, et entraîner l'épreuve faible jusqu'à la sortir de la zone éliminatoire. Un
examen blanc noté sur les barèmes officiels vous situe précisément — c'est exactement ce
que fait notre app, correction IA de l'écrit et de l'oral comprise.</p>""",
 "faq": [
  ("Quelle est la durée totale du DELF B2 ?",
   "Environ 3 heures pour les épreuves collectives (compréhensions + production écrite), plus l'épreuve orale individuelle avec temps de préparation surveillé. Les durées exactes figurent sur votre convocation."),
  ("Le DELF B2 suffit-il pour entrer à l'université en France ?",
   "Dans la majorité des cas oui : la plupart des licences et masters demandent B2. Certaines filières (lettres, droit, médecine) ou écoles demandent C1 — vérifiez sur le site de l'établissement visé. Pour le C1, voir <a href=\"/dalf/\">notre page DALF</a>."),
  ("Combien de temps pour passer de B1 à B2 ?",
   "Comptez généralement 4 à 6 mois de pratique régulière. Si votre B1 est solide et qu'il s'agit surtout d'apprivoiser le format de l'examen, 6 à 10 semaines d'entraînement méthodique peuvent suffire."),
 ]},
# ---------------------------------------------------------------- DELF B1
{"url": "/delf-b1/", "accent": "accent-delf", "crumb": "DELF B1",
 "title": "DELF B1 2026 : épreuves, carte de résident et préparation",
 "desc": "Le DELF B1 : format des épreuves, à quoi il sert en 2026 (carte de résident, études) et comment le préparer efficacement.",
 "h1": "DELF B1 : valider le niveau seuil, à vie",
 "intro": "Le DELF B1 atteste le « niveau seuil » : celui où l'on se débrouille dans la plupart des situations de la vie courante. Diplôme valable à vie, il sert notamment de preuve de français pour la carte de résident — et de tremplin vers le B2.",
 "body": """<div class="facts"><strong>L'essentiel</strong><ul>
<li>4 épreuves sur 25 points chacune, total sur 100, admission à 50 — note éliminatoire sous 5/25.</li>
<li>Compréhensions 100 % QCM depuis la réforme 2020.</li>
<li><strong>Carte de résident : le B1 est le niveau exigé</strong> pour les demandes déposées depuis le 1<sup>er</sup> janvier 2026.</li>
<li>Pour la <strong>naturalisation</strong>, attention : c'est désormais le <strong>B2</strong> qui est demandé — voir <a href="/tcf-irn/">notre page TCF IRN</a>.</li>
</ul></div>
<h2>Comment le préparer</h2>
<p>Au B1, l'écart entre réussite confortable et échec se joue sur la régularité :
vocabulaire du quotidien, compréhension de documents authentiques (annonces, articles
courts, conversations), et une production écrite structurée simple mais correcte
(raconter, exprimer une opinion). Quinze minutes par jour d'exercices variés battent
une journée de révision par semaine — c'est précisément la logique du plan d'étude et
des défis quotidiens de notre app.</p>""",
 "faq": [
  ("Le DELF B1 suffit-il pour la naturalisation ?",
   "Non, plus depuis le 1er janvier 2026 : la naturalisation exige le niveau B2 (loi du 26 janvier 2024). Le DELF B1 reste suffisant pour la carte de résident. Si vous visez la naturalisation, orientez-vous vers un B2 ou un test TCF/TEF IRN."),
  ("DELF B1 ou TCF : que choisir pour la carte de résident ?",
   "Les deux sont acceptés. Le DELF est un diplôme à vie mais avec des sessions moins fréquentes ; le TCF IRN est plus rapide à obtenir mais valable 2 ans. Si vous pensez viser la naturalisation ensuite, un TCF IRN attestant le B2 fait d'une pierre deux coups."),
  ("Quelles sont les épreuves de l'oral B1 ?",
   "Trois parties : entretien dirigé (se présenter), exercice en interaction (jeu de rôle du quotidien) et expression d'un point de vue à partir d'un court document. L'app vous entraîne aux trois avec transcription et évaluation IA de votre oral."),
 ]},
# ---------------------------------------------------------------- DALF
{"url": "/dalf/", "accent": "accent-dalf", "crumb": "DALF C1 · C2",
 "title": "DALF C1 et C2 : épreuves, synthèse et préparation 2026",
 "desc": "DALF C1 et C2 : format des épreuves, la synthèse de documents, la dispense de test linguistique pour l'université et la méthode de préparation.",
 "h1": "DALF C1 · C2 : le niveau avancé qui dispense de tout autre test",
 "intro": "Le DALF (Diplôme approfondi de langue française) atteste les niveaux C1 et C2. Valable à vie, il dispense de tout test linguistique pour l'admission dans les universités françaises — et reste le diplôme de français le plus prestigieux pour un CV.",
 "body": """<div class="facts"><strong>L'essentiel</strong><ul>
<li><strong>C1</strong> : compréhension orale et écrite exigeantes, <strong>synthèse de documents</strong> + essai argumenté à l'écrit, exposé à partir d'un dossier à l'oral (avec une heure de préparation surveillée).</li>
<li><strong>C2</strong> : deux épreuves intégrées lecture/écriture et écoute/expression, sur des sujets intellectuellement denses.</li>
<li>Diplôme <strong>valable à vie</strong> ; C1 dispense de test linguistique à l'université.</li>
</ul></div>
<h2>La synthèse : l'épreuve reine du C1</h2>
<p>Réduire plusieurs documents en un texte unique, objectif, reformulé et calibré au
nombre de mots près : la synthèse ne s'improvise pas. C'est une technique — repérage des
idées communes, plan croisé, neutralité absolue, zéro citation — qui se maîtrise en une
dizaine d'entraînements corrigés sérieusement.</p>
<p>C'est le niveau où un correcteur humain devient rare et cher : l'évaluation IA de
notre app note vos synthèses et essais sur les critères officiels et vous rend un
feedback détaillé, autant de fois que nécessaire.</p>""",
 "faq": [
  ("DALF C1 ou DELF B2 pour mon dossier universitaire ?",
   "Le B2 suffit pour la plupart des formations ; le C1 est demandé par certaines filières exigeantes et fait toujours la différence en sélection. Si votre niveau réel est entre les deux, sécurisez d'abord le B2, puis visez le C1."),
  ("Faut-il choisir des spécialités au DALF ?",
   "Non, plus maintenant : les anciennes options (lettres/sciences humaines vs sciences) ont été supprimées. Les sujets restent d'ordre général mais intellectuellement exigeants — presse d'idées, débats de société."),
  ("Le C2 vaut-il l'investissement ?",
   "Pour la plupart des parcours, non : le C1 ouvre déjà toutes les portes. Le C2 se justifie pour l'enseignement du français, la traduction ou par défi personnel."),
 ]},
# ---------------------------------------------------------------- Examens blancs
{"url": "/examens-blancs/", "accent": "accent-delf", "crumb": "Examens blancs",
 "title": "Examen blanc DELF, TCF, TEF au format officiel 2026",
 "desc": "L'examen blanc chronométré est le meilleur prédicteur de votre note. Comment passer des examens blancs DELF, TCF et TEF au format officiel, sur iPhone.",
 "h1": "Examens blancs DELF, TCF, TEF : la répétition générale qui change tout",
 "intro": "Un examen de français coûte de 100 à 400 €, et une session ratée peut retarder un dossier d'immigration de plusieurs mois. L'examen blanc en conditions réelles est le seul moyen fiable de savoir, avant de payer, si vous êtes prêt.",
 "body": """<h2>Pourquoi ça marche</h2>
<p>Trois raisons, toutes documentées par la recherche sur l'apprentissage :</p>
<ol>
<li><strong>L'effet de test</strong> : se faire interroger ancre mieux la langue que relire des cours.</li>
<li><strong>La gestion du temps</strong> : la moitié des points perdus le jour J le sont par mauvaise gestion du chronomètre, pas par manque de niveau.</li>
<li><strong>Le diagnostic</strong> : un score par épreuve révèle précisément où investir vos heures de préparation.</li>
</ol>
<h2>Ce qu'un bon examen blanc doit respecter</h2>
<ul>
<li>Les <strong>durées et consignes officielles</strong>, épreuve par épreuve (formats 2025-2026, réformes TCF/TEF IRN incluses) ;</li>
<li>le <strong>barème officiel</strong> : sur 100 avec seuils éliminatoires pour le DELF, échelle 699 avec niveau CECRL par épreuve pour TCF et TEF ;</li>
<li>des <strong>sujets originaux</strong> — s'entraîner sur des sujets « fuités » est le meilleur moyen de surestimer son niveau (et un risque pour un dossier d'immigration) ;</li>
<li>une vraie <strong>correction de l'écrit et de l'oral</strong>, pas seulement des QCM auto-corrigés.</li>
</ul>
<p>C'est le cahier des charges exact des examens blancs de notre app : 15 variantes
d'examens, chronomètre réel, notation officielle, correction IA des productions écrites
et orales sur les grilles officielles, et conversion NCLC/CLB pour les dossiers Canada
et Québec.</p>""",
 "faq": [
  ("À quelle fréquence passer un examen blanc ?",
   "Un au tout début pour le diagnostic, puis un par semaine environ en phase de préparation, et deux ou trois complets dans les dix derniers jours. Entre les examens blancs, travaillez en exercices ciblés — c'est plus efficace que d'enchaîner les simulations."),
  ("Mon score d'examen blanc prédit-il vraiment ma note ?",
   "S'il respecte le format et le barème officiels, oui, à un demi-niveau près. La nervosité du jour J coûte en général quelques points — d'où l'intérêt de viser votre seuil avec de la marge."),
  ("Les examens blancs de l'app sont-ils gratuits ?",
   "L'essentiel de l'app est utilisable gratuitement chaque jour ; l'accès à l'ensemble des examens blancs et aux évaluations IA à volonté fait partie de l'abonnement Premium."),
 ]},
# ---------------------------------------------------------------- Blog
{"url": "/blog/", "accent": "", "crumb": "Blog", "cta": False,
 "title": "Blog — préparer le DELF, le TCF et le TEF",
 "desc": "Guides et méthodes pour préparer le DELF, le DALF, le TCF et le TEF : scores NCLC, naturalisation 2026, examens blancs, méthodes par épreuve.",
 "h1": "Le blog de la préparation DELF · TCF · TEF",
 "intro": "Guides pratiques, décryptage des réformes et méthodes par épreuve. Les premiers articles arrivent — voici ce qui est en préparation.",
 "body": """<h2>Prochains articles</h2>
<h3>Immigration Canada &amp; Québec</h3>
<ul>
<li>TCF Canada 2026 : format, durée, notation — le guide complet</li>
<li>TCF ou TEF Canada : lequel choisir pour Entrée express ?</li>
<li>NCLC 7 : quel score viser au TCF Canada (tableau de conversion complet)</li>
<li>TEFAQ 2026 : réussir l'épreuve orale pour le PEQ et Arrima</li>
</ul>
<h3>Naturalisation &amp; titres de séjour</h3>
<ul>
<li>Naturalisation 2026 : le niveau B2 devient obligatoire — ce qui change pour vous</li>
<li>TCF IRN ou TEF IRN : prix, délais, difficulté — le comparatif</li>
<li>Carte de résident : le niveau B1 exigé depuis janvier 2026</li>
</ul>
<h3>DELF · DALF</h3>
<ul>
<li>Production écrite DELF B2 : méthode et sujets types corrigés</li>
<li>DALF C1 : la méthode de la synthèse pas à pas</li>
<li>DELF vs TCF vs TEF : quel examen passer selon votre objectif ?</li>
</ul>
<p>En attendant, les guides par examen sont déjà en ligne :
<a href="/tcf-canada/">TCF Canada</a>, <a href="/tcf-irn/">TCF IRN</a>,
<a href="/tef-canada/">TEF Canada</a>, <a href="/delf-b2/">DELF B2</a>,
<a href="/delf-b1/">DELF B1</a>, <a href="/dalf/">DALF</a> et
<a href="/examens-blancs/">examens blancs</a>.</p>"""},
# ---------------------------------------------------------------- Support
{"url": "/support/", "accent": "", "crumb": "Support", "cta": False,
 "title": "Support — TCF DELF TEF : Tests 2026",
 "desc": "Support et contact de l'application iOS TCF DELF TEF : Tests 2026 : questions fréquentes, abonnement Premium, confidentialité.",
 "h1": "Support de l'application",
 "intro": "Une question, un problème, une suggestion sur l'app « TCF DELF TEF : Tests 2026 » ? Écrivez-nous : nous répondons généralement sous 48 heures.",
 "body": """<div class="facts"><strong>Contact</strong>
<p><a href="mailto:gockaman@gmail.com">gockaman@gmail.com</a></p></div>
<h2>Questions fréquentes</h2>
<div class="faq">
<details><summary>Comment restaurer mon abonnement Premium ?</summary>
<p>Réglages de l'application → « Restaurer les achats ». L'abonnement est lié à votre
identifiant Apple : réinstaller l'app ou changer d'iPhone ne le fait pas perdre.</p></details>
<details><summary>Comment gérer ou résilier mon abonnement ?</summary>
<p>Les abonnements sont gérés par Apple : Réglages iOS → votre nom → Abonnements.
La résiliation prend effet à la fin de la période en cours.</p></details>
<details><summary>Mes données sont-elles collectées ?</summary>
<p>Non : pas de compte, pas de publicité, pas de tracking. Vos résultats restent sur
votre iPhone (sauvegarde iCloud privée en option). Détails dans notre
<a href="/confidentialite/">politique de confidentialité</a>.</p></details>
<details><summary>L'app fonctionne-t-elle hors ligne ?</summary>
<p>Oui pour l'entraînement et les examens blancs. Seules les évaluations IA de l'écrit
et de l'oral nécessitent une connexion.</p></details>
</div>"""},
# ---------------------------------------------------------------- 404
{"url": "/404.html", "accent": "", "crumb": "Page introuvable", "cta": False,
 "title": "Page introuvable — delf-tcf-tef.fr",
 "desc": "Cette page n'existe pas ou plus.",
 "h1": "Page introuvable",
 "intro": "Cette page n'existe pas ou a été déplacée.",
 "body": """<p>Reprenez depuis <a href="/">l'accueil</a> ou consultez nos guides :
<a href="/tcf-canada/">TCF Canada</a>, <a href="/tcf-irn/">TCF IRN</a>,
<a href="/delf-b2/">DELF B2</a>, <a href="/examens-blancs/">examens blancs</a>.</p>"""},
]

def write_404(p):
    faq_html, faq_ld = "", ""
    out = (HEAD.format(base=BASE, title=p["title"], desc=p["desc"], url="/404.html",
                       accent="", crumb=p["crumb"], h1=p["h1"], intro=p["intro"],
                       jsonld="") + p["body"] + FOOT)
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(out)
    print("écrit : /404.html")

for p in PAGES:
    if p["url"] == "/404.html":
        write_404(p)
    else:
        write_page(p)

urls = ["/"] + [p["url"] for p in PAGES if p["url"] != "/404.html"] + ["/confidentialite/"]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sm += [f"  <url><loc>{BASE}{u}</loc></url>" for u in urls]
sm.append("</urlset>")
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write("\n".join(sm) + "\n")
print("écrit : /sitemap.xml —", len(urls), "URLs")
