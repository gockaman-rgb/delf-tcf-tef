#!/usr/bin/env python3
"""Les sept pages piliers en « modules » (19/09/2026).

Injecte dans chaque pilier, entre des marqueurs HTML (idempotent) :
  1. après le sommaire : bandeau de chiffres, « Votre parcours en 5 étapes », grille des modules ;
  2. dans la section « Où passer » : les principaux centres avec leurs contacts (données
     `_build/data/*.json`, liste FEI du 19/09/2026) et le lien vers l'annuaire.
Le contenu rédigé des piliers n'est pas touché.

Usage : python3 _build/pillar_modules.py
"""

import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
DATA = os.path.join(HERE, "data")
sys.path.insert(0, HERE)
from make_centres import card, load  # noqa: E402


def pick(dataset, name_part, city_part=""):
    d = load(dataset)
    for c in d["centres"]:
        if name_part.lower() in c["name"].lower() and city_part.lower() in c["city"].lower():
            return card(c, d["country"])
    raise SystemExit(f"centre introuvable : {dataset} / {name_part} / {city_part}")


def stats(items):
    return '<div class="stats">\n' + "\n".join(
        f"<div class=\"stat\"><b>{b}</b><span>{s}</span>{('<em>' + e + '</em>') if e else ''}</div>"
        for b, s, e in items) + "\n</div>"


def steps(items):
    return '<ol class="steps">\n' + "\n".join(f"<li><b>{t}</b><span>{d}</span></li>" for t, d in items) + "\n</ol>"


def modules(items):
    return '<div class="grid c2 modules">\n' + "\n".join(
        f'<div class="card card-link"><span class="tag">{t}</span><h3><a href="{h}">{ti}</a></h3><p>{d}</p></div>'
        for t, ti, h, d in items) + "\n</div>"


APP = "https://apps.apple.com/fr/app/tcf-delf-tef-tests-2026/id6790412304"

PILLARS = {
    "tcf-canada": dict(
        stats=[("2 h 47", "4 épreuves, le même jour", "CO 35 · CE 60 · EE 60 · EO 12 min"),
               ("699", "l'échelle des QCM", "expressions notées sur 20"),
               ("458", "en compréhension orale", "pour le NCLC 7 (453 à l'écrit)"),
               ("2 ans", "de validité", "comptés deux fois par IRCC")],
        steps=[("Vérifiez le test exigé", "Entrée express, citoyenneté : TCF <em>Canada</em> ou TEF Canada — jamais le TCF tout public ni le TCF Québec. <a href=\"/blog/tcf-ou-tef-canada/\">TCF ou TEF Canada ?</a>"),
               ("Fixez le score à atteindre", "IRCC lit le NCLC, pas la lettre : 458 en compréhension orale et 453 à l'écrit pour le NCLC 7, 523 et 524 pour le NCLC 9. <a href=\"/blog/tcf-canada-nclc-7/\">La table complète.</a>"),
               ("Mesurez-vous avant de payer", "Un <a href=\"/examens-blancs/\">examen blanc noté sur 699</a> et converti en NCLC dit si la session du mois prochain est la bonne ; les <a href=\"#erreurs\">pièges de format</a> se travaillent avant."),
               ("Réservez le centre et la date", "En France, une session par mois par centre, 195 à 285 € ; au Canada, 390 à 440 $ et des places parties en minutes. <a href=\"#ou-passer\">Les centres</a>, avec contacts."),
               ("Le jour J, puis le dossier", "Passeport et convocation ; attestation sous 2 à 4 semaines, valable deux ans — et <a href=\"/blog/validite-attestation-tcf-tef/\">IRCC compte ces deux ans deux fois</a>.")],
        modules=[("Les épreuves", "Le format, épreuve par épreuve", "#format", "39 + 39 questions, 3 tâches d'écrit, 3 tâches d'oral : durées, consignes, particularités."),
                 ("La notation", "Du score sur 699 au NCLC", "#nclc", "Les bandes de scores, la table de conversion IRCC et le B2 qui ne vaut pas toujours NCLC 7."),
                 ("Où passer", "Les centres, en France et au Canada", "#ou-passer", "Adresses, téléphones, prix relevés, méthode pour obtenir une place."),
                 ("S'entraîner", "Exercices corrigés, épreuve par épreuve", "/blog/exercices-comprehension-orale-tcf-canada/", "Compréhension orale, compréhension écrite, expression écrite, expression orale : des items réels expliqués."),
                 ("Les guides", "Prix, délais, validité, TCF ou TEF", "#a-lire", "Ce qu'il faut savoir avant de s'inscrire, article par article."),
                 ("Examen blanc", "Le test complet, chronométré, noté", "/examens-blancs/", "Dans l'app : les quatre épreuves au format officiel, converties en NCLC.")],
        centres_intro="Six centres relevés dans nos guides, parmi les 251 agréés en France et les 47 au Canada :",
        centres=[("tcf_france", "ACTE", "Paris"), ("tcf_france", "Alliance française", "Lyon"), ("tcf_france", "Alliance française de Montpellier", "Montpellier"),
                 ("tcf_canada", "Alliance Française de Montréal", "Montréal"), ("tcf_canada", "Alliance française", "Toronto"), ("tcf_canada", "Alliance française Canada Pacific", "Vancouver (")],
        directory=[("/centres/tcf-france/", "Les 251 centres TCF en France"), ("/centres/tcf-canada/", "Les 47 centres TCF au Canada"),
                   ("/centres/tcf-maroc/", "Maroc"), ("/centres/tcf-algerie/", "Algérie"), ("/centres/tcf-tunisie/", "Tunisie"), ("/centres/", "tous les pays")]),
    "tcf-irn": dict(
        stats=[("1 h 35", "4 épreuves insécables", "CO 20 · CE 35 · EE 30 · EO 10 min"),
               ("499", "l'échelle des QCM", "B2 = 400 à 499"),
               ("B2", "pour la naturalisation", "B1 carte de résident · A2 carte pluriannuelle"),
               ("2 ans", "de validité", "éligible au CPF")],
        steps=[("Identifiez le niveau exigé", "A2 pour une première carte pluriannuelle, B1 pour la carte de résident, B2 à l'oral comme à l'écrit pour la naturalisation. <a href=\"#niveaux\">Le tableau depuis 2026.</a>"),
               ("Diplôme ou test ?", "Le TCF IRN se passe chaque semaine mais expire au bout de deux ans ; le DELF ne périme jamais mais prend un trimestre. <a href=\"/blog/diplome-ou-test-delf-tcf/\">Lequel vous faut-il ?</a>"),
               ("Vérifiez que vous avez le niveau", "Un <a href=\"/examens-blancs/\">examen blanc au format IRN</a>, noté sur 499, avant de payer 140 à 220 € — et les <a href=\"/blog/exercices-tcf-irn/\">quatre épreuves corrigées</a>."),
               ("Inscrivez-vous dans un centre agréé", "En ligne, quelques jours avant la session ; sept centres à Paris. <a href=\"#ou-passer\">Les centres, avec contacts</a> — et l'<a href=\"/blog/ou-passer-l-examen-civique/\">examen civique</a>, à réserver à part."),
               ("Après le test", "Attestation sous 2 à 3 semaines, valable deux ans ; en cas d'échec, 20 à 30 jours avant de repasser les quatre épreuves. <a href=\"/blog/repasser-tcf-tef/\">Les règles de reprise.</a>")],
        modules=[("Les épreuves", "Le format, épreuve par épreuve", "#format", "25 + 25 questions, un écrit de 30 minutes, un oral de 10 : le test réformé de 2025."),
                 ("La notation", "L'échelle sur 499, pas sur 699", "#499", "Pourquoi votre B2 se joue entre 400 et 499, et l'erreur qu'on lit partout."),
                 ("Où passer", "Les centres et l'inscription", "#ou-passer", "Adresses, téléphones, prix relevés, papier ou ordinateur."),
                 ("S'entraîner", "Les 4 épreuves corrigées", "/blog/exercices-tcf-irn/", "Un exercice corrigé par épreuve, au niveau B2 exigé depuis 2026."),
                 ("Examen civique", "L'autre examen obligatoire", "/blog/ou-passer-l-examen-civique/", "Deux réseaux de centres, une pré-inscription en ligne, 70 à 110 €."),
                 ("Les guides", "Naturalisation, carte de résident, B1 ou B2", "#a-lire", "Les démarches, les justificatifs, les dispenses.")],
        centres_intro="Six centres relevés dans notre guide, parmi les 251 agréés en France :",
        centres=[("tcf_france", "ACTE", "Paris"), ("tcf_france", "Forum ACCORD", "Paris"), ("tcf_france", "Etoile Institut", "Paris"),
                 ("tcf_france", "Alliance française", "Lyon"), ("tcf_france", "Alliance française de Montpellier", "Montpellier"), ("tcf_france", "CLPS", "Rennes")],
        directory=[("/centres/tcf-france/", "Les 251 centres TCF en France"), ("/centres/examen-civique-france/", "Les 245 centres d'examen civique"), ("/centres/", "tous les pays")]),
    "tcf-quebec": dict(
        stats=[("1 à 4", "épreuves au choix", "on ne paie que ce qu'on passe"),
               ("699 / 20", "compréhensions / expressions", "convertis en Échelle québécoise"),
               ("7-8", "niveau québécois = B2", "≠ NCLC 7-8 fédéral"),
               ("2 ans", "de validité", "à la date de la demande")],
        steps=[("Vérifiez votre programme", "PSTQ, PEQ, conjoint : chaque volet exige des épreuves et des niveaux différents. <a href=\"#programmes\">Quel niveau pour quel programme.</a>"),
               ("Choisissez vos épreuves", "Le TCF Québec est modulaire : souvent, les deux orales suffisent. <a href=\"#modulaire\">Pourquoi ça change tout.</a>"),
               ("Lisez le bon référentiel", "Un niveau 7 québécois n'est pas un NCLC 7. <a href=\"#echelle\">La table de conversion officielle.</a>"),
               ("Mesurez-vous", "Un <a href=\"/examens-blancs/\">examen blanc</a> noté sur 699 et converti en Échelle québécoise, épreuve par épreuve."),
               ("Inscrivez-vous", "Mêmes centres que le TCF Canada, au Québec comme en France ; TCF Québec à 65 € par module à Montpellier, 105 à 125 $ par épreuve à l'UQTR. <a href=\"#ou-passer\">Les centres.</a>")],
        modules=[("Les épreuves", "Le format modulaire", "#modulaire", "29 + 29 questions, 3 exercices d'écrit, 3 d'oral : chaque épreuve est indépendante."),
                 ("La notation", "L'Échelle québécoise", "#echelle", "La table de conversion et le piège du niveau 7 qui n'est pas un NCLC 7."),
                 ("Où passer", "Les centres, au Québec et en France", "#ou-passer", "Adresses, téléphones, prix à la carte relevés."),
                 ("TCF Québec ou Canada ?", "Le bon test pour votre dossier", "#choisir", "Le TCF Canada est aussi reconnu par le MIFI depuis 2022 — quand le préférer."),
                 ("S'entraîner", "Expression orale et écrite corrigées", "/blog/sujets-expression-orale-tcf-canada/", "Les mêmes tâches que le TCF Canada, corrigées et expliquées."),
                 ("Les guides", "TEFAQ, prix, validité", "#a-lire", "L'autre test modulaire, et ce qu'il faut savoir avant de payer.")],
        centres_intro="Six centres relevés dans nos guides, parmi les 47 agréés au Canada et les 251 en France :",
        centres=[("tcf_canada", "Alliance Française de Montréal", "Montréal"), ("tcf_canada", "Collège Stanislas", "Montréal"), ("tcf_canada", "Collège Stanislas", "Québec"),
                 ("tcf_canada", "Université du Québec à Trois-Rivières", "Trois-Rivières"), ("tcf_france", "Alliance française de Montpellier", "Montpellier"), ("tcf_france", "Alliance française Aix-Marseille", "Marseille")],
        directory=[("/centres/tcf-canada/", "Les 47 centres TCF au Canada"), ("/centres/tcf-france/", "Les 251 centres TCF en France"), ("/centres/", "tous les pays")]),
    "tef-canada": dict(
        stats=[("2 h 55", "4 épreuves", "CE 60 · CO 40 · EE 60 · EO 15 min"),
               ("40 + 40", "questions de compréhension", "2 sections par expression"),
               ("NCLC 7", "= 207 en CE, 249 en CO", "310 en EE et en EO"),
               ("2 ans", "de validité", "comptés deux fois par IRCC")],
        steps=[("TEF ou TCF ?", "Les deux sont acceptés par IRCC ; ils n'ont ni le même format ni la même table. <a href=\"/blog/tcf-ou-tef-canada/\">Le comparatif.</a>"),
               ("Fixez votre NCLC cible", "Sur les échelles TEF utilisées par IRCC — pas sur la colonne « ancien score ». <a href=\"#nclc\">La table de conversion.</a>"),
               ("Apprivoisez les tâches TEF", "Écrire la suite d'un fait divers, poser les questions à l'examinateur : des formats propres au TEF. <a href=\"#taches\">Les tâches</a> et les <a href=\"/blog/exercices-tef-canada/\">exercices corrigés</a>."),
               ("Mesurez-vous", "Un <a href=\"/examens-blancs/\">examen blanc TEF Canada</a> chronométré, noté sur les échelles du test et converti en NCLC."),
               ("Inscrivez-vous dans un centre agréé", "Par le Français des affaires (CCI Paris Île-de-France), pas par FEI : son annuaire couvre tous les pays. <a href=\"#ou-passer\">Les centres.</a>")],
        modules=[("Les épreuves", "Le format, épreuve par épreuve", "#format", "40 questions par compréhension, deux sections par expression : durées et particularités."),
                 ("La notation", "La table de conversion NCLC", "#nclc", "Les seuils par épreuve, et le piège de l'« ancien score »."),
                 ("Où passer", "Les centres agréés par la CCIP", "#ou-passer", "L'annuaire officiel, et les centres relevés à Paris."),
                 ("TEFAQ", "La version québécoise, modulaire", "#tefaq", "Deux épreuves suffisent souvent — mais IRCC ne l'accepte pas."),
                 ("S'entraîner", "Les épreuves corrigées", "/blog/exercices-tef-canada/", "Un exercice corrigé par épreuve, au format TEF."),
                 ("Les guides", "TCF ou TEF, prix, validité", "#a-lire", "Ce qu'il faut savoir avant de s'inscrire.")],
        centres_intro="Le TEF relève d'un autre réseau que le TCF : celui du Français des affaires, dont l'annuaire fait foi. Trois centres parisiens relevés sur leurs propres sites :",
        centres=[("tcf_france", "Alliance française Paris", "Paris"), ("tcf_france", "Etoile Institut", "Paris")],
        extra_cards=['<div class="card centre"><h4>ALIP</h4>\n<p class="addr">27, rue Ginoux 75015 Paris</p>\n<p class="contact"><a href="https://www.alip.fr" rel="noopener nofollow">alip.fr</a></p>\n<p class="badges"><span class="badge ok">TEF Canada relevé à 245 €</span></p></div>'],
        directory=[("https://www.lefrancaisdesaffaires.fr/trouver-un-centre-agree/", "Annuaire officiel des centres TEF (Français des affaires)"), ("/centres/", "Les centres TCF, DELF et examen civique")]),
    "delf-b1": dict(
        stats=[("2 h 10", "4 épreuves", "CO 25 · CE 45 · PE 45 · PO 15 min"),
               ("50 / 100", "pour être admis", "moyenne des quatre épreuves"),
               ("5 / 25", "note éliminatoire", "sur une seule épreuve"),
               ("À vie", "validité du diplôme", "résultats en 4 à 6 semaines")],
        steps=[("Vérifiez que le B1 est votre niveau", "Carte de résident : B1 depuis 2026 ; naturalisation : B2. <a href=\"#carte-resident\">Le B1 et la carte de résident</a> — <a href=\"/blog/b1-ou-b2-nationalite-francaise/\">B1 ou B2 ?</a>"),
               ("Diplôme ou test ?", "Le DELF ne périme jamais mais se passe dix fois par an, avec des inscriptions qui ferment tôt ; le TCF IRN se passe chaque semaine mais vaut deux ans. <a href=\"#diplome-ou-test\">Lequel choisir.</a>"),
               ("Préparez les quatre épreuves", "160 mots à l'écrit, un oral en trois parties, et deux seuils à respecter. <a href=\"#bareme\">Le barème</a>, <a href=\"#ecrit\">l'écrit</a>, <a href=\"#oral\">l'oral</a>."),
               ("Inscrivez-vous à temps", "143 centres, 10 sessions par an, une fenêtre d'inscription de quelques jours à quelques semaines. <a href=\"/blog/ou-passer-le-delf-en-france/\">Le calendrier 2026-2027</a> et <a href=\"#ou-passer\">les centres</a>."),
               ("Le jour J, puis le diplôme", "Convocation et pièce d'identité ; résultats sous 4 à 6 semaines, diplôme valable à vie — un <a href=\"/examens-blancs/\">examen blanc</a> avant, pour ne pas payer deux fois.")],
        modules=[("Les épreuves", "Le format des quatre épreuves", "#format", "Compréhensions à QCM, 160 mots d'écrit, oral en trois parties : durées et notes."),
                 ("Le barème", "50/100 et la note éliminatoire", "#bareme", "Les deux seuils, et la stratégie qu'ils imposent."),
                 ("Où passer", "Les centres et le calendrier", "#ou-passer", "Adresses, téléphones, prix relevés, fenêtres d'inscription."),
                 ("S'entraîner", "La production écrite en 160 mots", "#ecrit", "Ce que le correcteur évalue, le plan qui fonctionne."),
                 ("La démarche", "Le B1 pour la carte de résident", "/blog/carte-de-resident-b1-2026/", "Qui est concerné, les justificatifs, les dispenses depuis janvier 2026."),
                 ("Examen blanc", "Le DELF B1 complet, noté sur 100", "/examens-blancs/", "Dans l'app : les quatre épreuves, le seuil de 50 et la correction IA.")],
        centres_intro="Six centres relevés dans notre guide, parmi les 143 agréés en France :",
        centres=[("delf_france", "Alliance Française de Paris", "PARIS"), ("delf_france", "Sorbonne Nouvelle", "Paris"), ("delf_france", "Cours de Civilisation Française de la Sorbonne", "Paris"),
                 ("delf_france", "Alliance Française de Lyon", "Lyon"), ("delf_france", "NANTES UNIVERSITE", "Nantes"), ("delf_france", "Alliance Française de Lille", "Lille")],
        directory=[("/centres/delf-france/", "Les 143 centres DELF-DALF en France"), ("/centres/", "tous les centres")]),
    "delf-b2": dict(
        stats=[("2 h 50", "4 épreuves", "CO 30 · CE 60 · PE 60 · PO 20 min"),
               ("50 / 100", "pour être admis", "moyenne des quatre épreuves"),
               ("5 / 25", "note éliminatoire", "sur une seule épreuve"),
               ("À vie", "validité du diplôme", "exigé pour la naturalisation")],
        steps=[("Vérifiez que le B2 est votre niveau", "Naturalisation : B2 à l'oral comme à l'écrit depuis 2026 ; université : B2, parfois C1. <a href=\"#a-quoi-sert\">À quoi sert le DELF B2.</a>"),
               ("Diplôme ou test ?", "Le DELF B2 ne périme jamais ; le TCF IRN se passe chaque semaine mais vaut deux ans. <a href=\"/blog/diplome-ou-test-delf-tcf/\">Lequel vous faut-il ?</a>"),
               ("Préparez les quatre épreuves", "250 mots argumentés, un oral avec débat, deux seuils. <a href=\"#bareme\">Le barème</a>, <a href=\"#ecrit\">l'écrit</a>, <a href=\"#oral\">l'oral</a>, les <a href=\"/blog/exercices-delf-b2/\">exercices corrigés</a>."),
               ("Inscrivez-vous à temps", "Le B2 se passe le mercredi à 14 h, dix fois par an ; les inscriptions ferment quatre à dix semaines avant. <a href=\"/blog/ou-passer-le-delf-en-france/\">Le calendrier</a> et <a href=\"#ou-passer\">les centres</a>."),
               ("Le jour J, puis le diplôme", "Convocation et pièce d'identité ; résultats sous 4 à 6 semaines, diplôme à vie — et un <a href=\"/examens-blancs/\">examen blanc</a> avant, pour ne pas payer 125 à 280 € deux fois.")],
        modules=[("Les épreuves", "Le format des quatre épreuves", "#format", "Compréhensions 100 % QCM, 250 mots d'écrit, monologue et débat : durées et notes."),
                 ("Le barème", "50/100 et la note éliminatoire", "#bareme", "Les deux seuils, et pourquoi 60/100 ne suffit pas toujours."),
                 ("Où passer", "Les centres et le calendrier", "#ou-passer", "Adresses, téléphones, prix relevés de 125 à 280 €, fenêtres d'inscription."),
                 ("S'entraîner", "Les 4 épreuves corrigées", "/blog/exercices-delf-b2/", "Un exercice corrigé par épreuve, au format réformé."),
                 ("La production écrite", "250 mots, 60 minutes, la méthode", "/blog/production-ecrite-delf-b2/", "Ce que le correcteur évalue et le plan qui fonctionne."),
                 ("Examen blanc", "Le DELF B2 complet, noté sur 100", "/examens-blancs/", "Dans l'app : les quatre épreuves, le seuil de 50 et la correction IA de l'écrit et de l'oral.")],
        centres_intro="Six centres relevés dans notre guide, parmi les 143 agréés en France — le même B2 y coûte de 125 à 280 € :",
        centres=[("delf_france", "Alliance Française de Paris", "PARIS"), ("delf_france", "Sorbonne Nouvelle", "Paris"), ("delf_france", "Cours de Civilisation Française de la Sorbonne", "Paris"),
                 ("delf_france", "Alliance Française de Lyon", "Lyon"), ("delf_france", "NANTES UNIVERSITE", "Nantes"), ("delf_france", "Alliance Française de Lille", "Lille")],
        directory=[("/centres/delf-france/", "Les 143 centres DELF-DALF en France"), ("/centres/", "tous les centres")]),
    "dalf": dict(
        stats=[("4 h", "+ 1 h de préparation", "C1 comme C2"),
               ("C1 · C2", "deux diplômes indépendants", "on s'inscrit directement au C2"),
               ("50 / 100", "pour être admis", "5/25 éliminatoire au C1"),
               ("À vie", "validité du diplôme", "dispense de test à l'université")],
        steps=[("C1 ou C2 ?", "Le C1 suffit à presque toutes les démarches ; le C2 est un exercice de maîtrise. <a href=\"#c1-ou-c2\">Lequel viser.</a>"),
               ("Connaissez les épreuves", "Synthèse et essai au C1, texte de 700 mots au C2, exposé après une heure de préparation. <a href=\"#c1\">Le C1</a>, <a href=\"#c2\">le C2</a>."),
               ("Travaillez la synthèse", "200 à 240 mots, aucune citation, aucun avis : l'épreuve reine du C1. <a href=\"/blog/synthese-dalf-c1/\">La méthode pas à pas.</a>"),
               ("Inscrivez-vous à temps", "Mêmes centres et mêmes sessions que le DELF, le jeudi ; tous les centres n'ouvrent pas le DALF à chaque session. <a href=\"/blog/ou-passer-le-delf-en-france/\">Le calendrier</a> et <a href=\"#ou-passer\">les centres</a>."),
               ("Le jour J, puis le diplôme", "Résultats sous 4 à 6 semaines, diplôme à vie, et la <a href=\"#dispense\">dispense de test</a> de français qu'il donne à l'université.")],
        modules=[("Les épreuves", "Le DALF C1, épreuve par épreuve", "#c1", "Compréhensions, synthèse + essai, exposé : durées et notes."),
                 ("Le C2", "Le format en deux domaines", "#c2", "Oral et écrit intégrés, 700 mots minimum, notés sur 50."),
                 ("Où passer", "Les centres et le calendrier", "#ou-passer", "Les mêmes 143 centres que le DELF, le jeudi de chaque session."),
                 ("La synthèse", "200 à 240 mots, la méthode", "/blog/synthese-dalf-c1/", "Croiser les documents sans citer ni juger."),
                 ("Le barème", "50/100 et la note éliminatoire", "#bareme", "Les seuils du C1 et du C2."),
                 ("Examen blanc", "Le DALF C1 complet, noté sur 100", "/examens-blancs/", "Dans l'app : les quatre épreuves et la correction IA de la synthèse.")],
        centres_intro="Six centres relevés dans notre guide DELF, parmi les 143 agréés en France — le DALF s'y passe le jeudi :",
        centres=[("delf_france", "Alliance Française de Paris", "PARIS"), ("delf_france", "Sorbonne Nouvelle", "Paris"), ("delf_france", "Cours de Civilisation Française de la Sorbonne", "Paris"),
                 ("delf_france", "Alliance Française de Lyon", "Lyon"), ("delf_france", "NANTES UNIVERSITE", "Nantes"), ("delf_france", "Alliance Française de Lille", "Lille")],
        directory=[("/centres/delf-france/", "Les 143 centres DELF-DALF en France"), ("/centres/", "tous les centres")]),
}

M_START, M_END = "<!-- modules:start -->", "<!-- modules:end -->"
C_START, C_END = "<!-- centres:start -->", "<!-- centres:end -->"


def strip(s, a, b):
    return re.sub(re.escape(a) + r".*?" + re.escape(b) + r"\n?", "", s, flags=re.S)


def inject(slug, spec):
    p = os.path.join(ROOT, slug, "index.html")
    s = open(p, encoding="utf-8").read()
    s = strip(s, M_START, M_END)
    s = strip(s, C_START, C_END)
    s = s.replace('<li><a href="#parcours">Votre parcours en 5 étapes</a></li>\n', '').replace('<li><a href="#modules">Le dossier, module par module</a></li>\n', '')
    # 1. bloc modules après le sommaire
    block = (f"{M_START}\n{stats(spec['stats'])}\n\n<h2 id=\"parcours\">Votre parcours en 5 étapes</h2>\n{steps(spec['steps'])}\n\n"
             f"<h2 id=\"modules\">Le dossier, module par module</h2>\n{modules(spec['modules'])}\n{M_END}\n")
    i = s.index("</ol></details>") + len("</ol></details>")
    s = s[:i] + "\n\n" + block + s[i:]
    # sommaire
    s = re.sub(r'(<details class="toc"><summary>Au sommaire</summary><ol>\n)',
               r'\1<li><a href="#parcours">Votre parcours en 5 étapes</a></li>\n<li><a href="#modules">Le dossier, module par module</a></li>\n', s, count=1)
    # 2. centres dans la section « Où passer »
    cards = [pick(*c) for c in spec["centres"]] + spec.get("extra_cards", [])
    links = " · ".join(f'<a href="{u}">{t}</a>' for u, t in spec["directory"])
    cblock = (f"{C_START}\n<p>{spec['centres_intro']}</p>\n<div class=\"grid c2 centres\">\n" + "\n".join(cards) +
              f"\n</div>\n<p class=\"more\">Annuaire complet, avec adresses et téléphones : {links}.</p>\n{C_END}\n")
    j = s.index('<div class="cta-band">')
    s = s[:j] + cblock + s[j:]
    open(p, "w", encoding="utf-8").write(s)
    print("✓", slug)


if __name__ == "__main__":
    for slug, spec in PILLARS.items():
        inject(slug, spec)
