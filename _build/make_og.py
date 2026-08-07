#!/usr/bin/env python3
"""Génère les images Open Graph 1200x630 du site, au gabarit des visuels existants.

Repris de la charte de img/og/tcf-quebec.png : fond #0E1420, accent #34C47C,
barre supérieure, filet vertical, chiffre-clé en gros à gauche de son libellé.

Usage :
    python3 _build/make_og.py            # ne réécrit que les images manquantes
    python3 _build/make_og.py --force    # régénère tout

Ajouter une image = ajouter une entrée dans PAGES, avec :
    slug, title, stat, label
`stat` peut être None : le bloc chiffre est alors simplement omis.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (14, 20, 32)
ACCENT = (52, 196, 124)
TITLE = (232, 237, 245)
MUTED = (154, 168, 189)

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "img", "og")

# slug, titre, chiffre-clé, libellé du chiffre
PAGES = [
    ("home", "DELF · TCF · TEF", "15", "examens couverts · correction IA"),
    ("tcf-canada", "TCF Canada", "458", "en compréhension orale pour NCLC 7"),
    ("tef-canada", "TEF Canada · TEFAQ", "2 h 55", "4 épreuves · conversion NCLC"),
    ("delf-b2", "DELF B2", "50", "sur 100 pour être admis"),
    ("delf-b1", "DELF B1", "B1", "exigé pour la carte de résident"),
    ("dalf", "DALF C1 · C2", "200", "mots : la synthèse du C1"),
    ("examens-blancs", "Examens blancs", "11", "formats officiels chronométrés"),
    ("tcf-irn", "TCF IRN", "499", "l'échelle du test de naturalisation"),
    ("plan-etude", "Plan d'étude", None, "Un coach calé sur votre date d'examen"),
    # articles du blog
    ("b1-ou-b2-nationalite-francaise", "B1 ou B2 ?", "B2", "pour la nationalité française"),
    ("tcf-irn-ou-tef-irn", "TCF IRN ou TEF IRN", "499", "la même échelle pour les deux"),
    ("prix-tcf-tef", "Prix du TCF et du TEF", "× 2", "d'écart entre deux centres"),
    ("cpf-test-francais", "Le CPF et les tests", "2", "versions du TCF finançables sur 4"),
    ("diplome-ou-test-delf-tcf", "Diplôme ou test ?", "2 ans", "contre à vie : ce qui les sépare"),
    ("repasser-tcf-tef", "Repasser le TCF ou le TEF", "20", "jours — mais la source se contredit"),
    ("validite-attestation-tcf-tef", "Validité : 2 ans", "2 ans", "oui, mais à partir de quand ?"),
    ("production-ecrite-delf-b2", "Production écrite B2", "250", "mots minimum, en 60 minutes"),
    ("synthese-dalf-c1", "La synthèse du C1", "200", "à 240 mots, sans aucune citation"),
    ("tefaq-oral-quebec", "TEFAQ", "1→4", "épreuves au choix · Échelle québécoise"),
    # cluster « exercices »
    ("exercices-comprehension-orale-tcf-canada", "Compréhension orale", "39", "questions en 35 min · 1 seule écoute"),
    ("exercices-comprehension-ecrite-tcf-canada", "Compréhension écrite", "39", "questions en 60 min · navigation libre"),
    ("sujets-expression-ecrite-tcf-canada", "Expression écrite", "3", "tâches · de 60 à 180 mots"),
    ("sujets-expression-orale-tcf-canada", "Expression orale", "12", "minutes pour 3 tâches"),
    ("exercices-tcf-irn", "Exercices TCF IRN", "499", "l'échelle du test de naturalisation"),
    ("exercices-tef-canada", "Exercices TEF Canada", "A+B", "deux sections par expression"),
    ("exercices-delf-b2", "Exercices DELF B2", "5", "sur 25 : la note éliminatoire"),
    ("exercices-structures-langue-tcf", "Structures de la langue", "18", "QCM en 15 min · TCF Tout Public"),
    ("questions", "Toutes vos questions", "217", "réponses sourcées et datées"),
    ("blog", "Le blog", None, "DELF · TCF · TEF — guides sourcés 2026"),
    ("a-propos", "À propos", None, "Méthode éditoriale et sources"),
    ("support", "Support", None, "Contact et questions fréquentes"),
    ("confidentialite", "Confidentialité", None, "Aucun compte, aucun serveur de profil"),
    # visuels d'origine (juillet), repris pour tenir dans le recadrage carré
    ("difference-tcf-tef", "TCF ou TEF ?", "9", "versions comparées, épreuve par épreuve"),
    ("tcf-canada-nclc-7", "NCLC 7 au TCF Canada", "458", "en compréhension orale"),
    ("tcf-ou-tef-canada", "TCF ou TEF Canada", "2", "seuls tests acceptés par IRCC"),
    ("examen-blanc-tcf-gratuit", "Examen blanc gratuit", "2", "ressources officielles, et leurs limites"),
    ("naturalisation-2026-niveau-b2", "Naturalisation 2026", "B2", "obligatoire depuis le 1er janvier"),
    ("carte-de-resident-b1-2026", "Carte de résident", "B1", "exigé depuis janvier 2026"),
    ("tcf-quebec", "TCF Québec", "1→4", "épreuves au choix · Échelle québécoise"),
    ("score-tcf-699", "Le score TCF", "699", "l'échelle officielle expliquée"),
    ("examens", "Les examens couverts", "15", "variantes, du DELF A1 au DALF C2"),
    ("contenu", "Le contenu de l'app", "20 000+", "questions et exercices originaux"),
    ("correction-ia", "La correction IA", "20", "vos productions notées sur 20"),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def fit(draw, text, path, start, max_w, floor=22):
    """Réduit la taille jusqu'à ce que `text` tienne dans `max_w`."""
    size = start
    while size > floor:
        f = font(path, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(path, floor)


# Facebook, WhatsApp, Slack et LinkedIn affichent souvent un aperçu CARRÉ :
# ils recadrent le 1200×630 au centre et ne gardent que la bande x 285→915.
# Tout le contenu est donc centré et calibré pour tenir dans cette bande —
# sinon le début des titres, le chiffre-clé et le domaine disparaissent.
SAFE = H            # 630 px : largeur conservée par un recadrage carré centré
PAD = 16            # marge de sécurité à l'intérieur de la bande


def centered(d, text, f, y, fill):
    """Écrit `text` centré horizontalement sur toute la largeur."""
    d.text(((W - d.textlength(text, font=f)) / 2, y), text, font=f, fill=fill)


def build(slug, title, stat, label):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    box = SAFE - 2 * PAD          # largeur utile réelle : 598 px

    # bandeau supérieur, pleine largeur (survit à tout recadrage)
    d.rectangle([0, 0, W, 10], fill=ACCENT)

    # surtitre
    centered(d, "DELF · TCF · TEF", fit(d, "DELF · TCF · TEF", FONT_BOLD, 30, box), 74, MUTED)

    # titre
    f_title = fit(d, title, FONT_BOLD, 70, box)
    centered(d, title, f_title, 150, TITLE)

    # filet d'accent centré, sous le titre
    d.rectangle([W // 2 - 46, 258, W // 2 + 46, 264], fill=ACCENT)

    if stat:
        f_stat = fit(d, stat, FONT_BOLD, 112, box)
        centered(d, stat, f_stat, 310, ACCENT)
        centered(d, label, fit(d, label, FONT_REG, 34, box), 452, MUTED)
    else:
        centered(d, label, fit(d, label, FONT_REG, 36, box), 330, MUTED)

    # domaine
    centered(d, "delf-tcf-tef.fr", font(FONT_REG, 28), 556, ACCENT)

    path = os.path.normpath(os.path.join(OUT_DIR, slug + ".png"))
    im.save(path, optimize=True)
    return path


def main():
    force = "--force" in sys.argv
    made, skipped = [], []
    for slug, title, stat, label in PAGES:
        path = os.path.normpath(os.path.join(OUT_DIR, slug + ".png"))
        if os.path.exists(path) and not force:
            skipped.append(slug)
            continue
        build(slug, title, stat, label)
        made.append(slug)
    print("générées :", ", ".join(made) if made else "(aucune)")
    if skipped:
        print("déjà présentes :", ", ".join(skipped))


if __name__ == "__main__":
    main()
