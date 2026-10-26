#!/usr/bin/env python3
"""Liens de pied de page ajoutés le 26/10/2026 : « Trouver un centre » dans les quatre langues, les calendriers DELF,
les frais du TCF Canada, l'Europe, et la Jordanie, le Qatar, le Koweït en arabe.

Les pieds de page sont recopiés dans chaque page publiée et dans plusieurs sources (article_template.py, generate.py,
make_questions_hub.py, data/pillars_src/*.html, index.html, 404.html). Le script travaille dans chaque bloc
<footer class="site">…</footer> (un par page, un par langue dans article_template.py) : il ajoute la ligne à côté de
la ligne d'ancrage, avec la même indentation, et ne fait rien si le bloc contient déjà le lien (idempotent). Dans les
chaînes Python d'une ligne (FOOTER_ES/EN/AR), le saut de ligne est la séquence « \\n ».

Usage : python3 _build/nav_finder_links.py [--check]
"""
import glob
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

# (ancre, nouvelle ligne, "after" | "before") — appliquées dans l'ordre : une règle peut s'ancrer sur la précédente.
RULES = [
    # Français — colonne « Examens »
    ('<li><a href="/centres/">Annuaire des centres</a></li>',
     '<li><a href="/trouver-un-centre/">Trouver un centre près de chez vous</a></li>', "after"),
    ('<li><a href="/dalf/">DALF C1 · C2</a></li>',
     '<li><a href="/blog/calendrier-delf-dalf-2026-2027/">Calendrier DELF-DALF 2027</a></li>', "after"),
    # Anglais
    ('<li><a href="/en/tcf-canada/score-clb/">Scores and CLB calculator</a></li>',
     '<li><a href="/en/tcf-canada/fees-registration/">Fees and registration</a></li>', "after"),
    ('<li><a href="/en/dalf-c1/">DALF C1</a></li>',
     '<li><a href="/en/delf-exam-dates-2027/">DELF exam dates 2027</a></li>', "after"),
    ('<li><a href="/en/tcf-canada-test-centres/">Canada: all provinces</a></li>',
     '<li><a href="/en/test-centre-near-me/">Find a test centre near you</a></li>', "before"),
    ('<li><a href="/en/tcf-canada-uk/">United Kingdom</a></li>',
     '<li><a href="/en/#europe">Europe</a></li>', "after"),
    # Espagnol
    ('<li><a href="/es/dalf-c1/">DALF C1</a></li>',
     '<li><a href="/es/fechas-delf-2027/">Fechas DELF 2027</a></li>', "after"),
    ('<li><a href="/es/">Centros de examen</a></li>',
     '<li><a href="/es/centro-de-examen-cerca-de-mi/">Buscar un centro cerca de mí</a></li>', "after"),
    # Arabe — colonne « مراكز الامتحان »
    ('<li><a href="/ar/tcf-canada-uae/">الإمارات</a></li>',
     '<li><a href="/ar/test-centre-near-me/">ابحث عن مركز قريب منك</a></li>', "before"),
    ('<li><a href="/ar/tcf-canada-saudi-arabia/">السعودية</a></li>',
     '<li><a href="/ar/tcf-canada-jordan/">الأردن</a></li>', "after"),
    ('<li><a href="/ar/tcf-canada-jordan/">الأردن</a></li>',
     '<li><a href="/ar/tcf-canada-qatar/">قطر</a></li>', "after"),
    ('<li><a href="/ar/tcf-canada-qatar/">قطر</a></li>',
     '<li><a href="/ar/tcf-canada-kuwait/">الكويت</a></li>', "after"),
]


def patch(text):
    """Applique RULES à un bloc de pied de page ; renvoie (texte, nombre d'insertions)."""
    n = 0
    for anchor, line, where in RULES:
        href = re.search(r'href="([^"]+)"', line).group(1)
        if anchor not in text or f'href="{href}"' in text:
            continue

        def one(m, line=line, where=where, anchor=anchor):
            esc, ind = m.group("esc") or "", m.group("ind")
            sep = (esc or "\n") + ind
            return esc + ind + (anchor + sep + line if where == "after" else line + sep + anchor)
        text, k = re.subn(r"(?P<esc>\\n)?(?P<ind>[ \t]*)" + re.escape(anchor), one, text)
        n += k
    return text, n


def patch_file(t):
    """Chaque bloc <footer class="site">…</footer> du fichier, et lui seul (la même ligne peut exister dans le
    corps d'un hub)."""
    out, n, pos = [], 0, 0
    for m in re.finditer(r'<footer class="site".*?</footer>', t, flags=re.S):
        out.append(t[pos:m.start()])
        block, k = patch(m.group(0))
        out.append(block)
        n += k
        pos = m.end()
    out.append(t[pos:])
    return "".join(out), n


def main():
    check = "--check" in sys.argv
    files = [f for f in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True) if "/_build/out/" not in f]
    files += [os.path.join(ROOT, "_build", p) for p in ("article_template.py", "generate.py", "make_questions_hub.py")]
    changed = inserted = 0
    for f in sorted(files):
        with open(f, encoding="utf-8") as fh:
            t = fh.read()
        t2, n = patch_file(t)
        if n:
            changed += 1
            inserted += n
            if not check:
                with open(f, "w", encoding="utf-8") as fh:
                    fh.write(t2)
    print(("à modifier" if check else "modifiés") + f" : {changed} fichiers, {inserted} liens")
    sys.exit(1 if check and changed else 0)


if __name__ == "__main__":
    main()
