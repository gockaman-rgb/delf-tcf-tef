#!/usr/bin/env python3
"""Avertissement du pied de page étendu au site lui-même (06/11/2026, SEO_PLAN_CORRECTION_2026-11-03.md §3 B).

Le paragraphe <p class="legal"> est recopié dans chaque page publiée et dans les sources (article_template.py, generate.py,
make_questions_hub.py, data/pillars_src/*.html). Ce script remplace l'ancien texte par le nouveau, langue par langue ;
idempotent.

Usage : python3 _build/legal_footer.py [--check]
"""
import glob
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

LEGAL = [
    (r"Application non officielle, non affiliée à France Éducation International\s+\(DELF, DALF, TCF\) ni au Français des affaires — CCI Paris Île-de-France \(TEF\)\. Les noms\s+d'examens sont cités uniquement pour décrire le contenu de préparation\.",
     "Site et application indépendants et non officiels : ni France Éducation international (DELF, DALF, TCF), ni le Français des "
     "affaires — CCI Paris Île-de-France (TEF), ni les Instituts français, ni VFS Global. Nous ne vendons aucune place d'examen. "
     "Les noms d'examens et de centres sont cités uniquement pour informer."),
    (r"Aplicación no oficial, sin vínculo con France Éducation international(?:\\n|\s)+\(DELF, DALF, TCF\) ni con Le français des affaires — CCI Paris Île-de-France \(TEF\)\. Los nombres(?:\\n|\s)+de los exámenes se citan solo para describir el contenido de preparación\.",
     "Sitio y aplicación independientes y no oficiales: no somos France Éducation international (DELF, DALF, TCF), ni Le français "
     "des affaires — CCI Paris Île-de-France (TEF), ni los Institut français, ni VFS Global. No vendemos plazas de examen. "
     "Los nombres de exámenes y centros se citan solo para informar."),
    (r"Unofficial app, not affiliated with France Éducation international(?:\\n|\s)+\(DELF, DALF, TCF\) or Le français des affaires — CCI Paris Île-de-France \(TEF\)\. Exam names(?:\\n|\s)+are cited only to describe the preparation content\.",
     "Independent, unofficial site and app: we are not France Éducation international (DELF, DALF, TCF), Le français des "
     "affaires — CCI Paris Île-de-France (TEF), the Instituts français or VFS Global. We sell no exam places. "
     "Exam and centre names are cited for information only."),
    (r"تطبيق غير رسمي، لا علاقة له بـ<bdi>France Éducation international</bdi>(?:\\n|\s)+\(DELF وDALF وTCF\) ولا بـ<bdi>Le français des affaires — CCI Paris Île-de-France</bdi> \(TEF\)\. تُذكر أسماء(?:\\n|\s)+الامتحانات لوصف محتوى التحضير فقط\.",
     "موقع وتطبيق مستقلان وغير رسميين: لسنا <bdi>France Éducation international</bdi> (DELF وDALF وTCF) ولا "
     "<bdi>Le français des affaires — CCI Paris Île-de-France</bdi> (TEF) ولا <bdi>Instituts français</bdi> ولا <bdi>VFS Global</bdi>. "
     "لا نبيع أماكن في الامتحانات. تُذكر أسماء الامتحانات والمراكز للإعلام فقط."),
]


def main():
    check = "--check" in sys.argv
    files = [f for f in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True) if "/_build/out/" not in f]
    files += [os.path.join(ROOT, "_build", p) for p in ("article_template.py", "generate.py", "make_questions_hub.py")]
    changed = 0
    for f in sorted(files):
        t = open(f, encoding="utf-8").read()
        new = t
        for rx, repl in LEGAL:
            new = re.sub(rx, repl, new)
        if new != t:
            changed += 1
            if not check:
                open(f, "w", encoding="utf-8").write(new)
    print(("à modifier" if check else "modifiés") + f" : {changed} fichiers")
    sys.exit(1 if check and changed else 0)


if __name__ == "__main__":
    main()
