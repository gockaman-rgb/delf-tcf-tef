#!/usr/bin/env python3
"""hreflang et lien de langue sur les pages françaises qu'aucun générateur ne réécrit (08/10/2026).

Beaucoup de pages françaises ont été écrites ou retouchées à la main (README : ne pas relancer generate.py ;
les scripts articles_batch*.py refusent de réécrire l'existant). Pour chaque page française du registre
(i18n_registry), ce script pose — ou remplace — exactement ce que article_template.render() écrit pour une
page générée :
  - les <link rel="alternate" hreflang> juste après la balise canonical ;
  - la ligne <p class="langs"> juste après la ligne de méta (« Par … · Mis à jour le … »).
Rien d'autre ne bouge ; relancé sur une page déjà à jour, il ne change pas un octet.

Usage : python3 _build/i18n_static.py [--check]   (--check : signale sans écrire, code 1 s'il y a à faire)
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
BASE = "https://delf-tcf-tef.fr"
sys.path.insert(0, HERE)
from i18n_registry import alternates_for, translations  # noqa: E402

ALT = re.compile(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+">\n')
LANGS = re.compile(r'<p class="langs">.*?</p>\n')


def fix(html, alts, links):
    canon = re.search(r'<link rel="canonical" href="[^"]+">\n', html)
    if not canon:
        raise ValueError("pas de balise canonical")
    head, rest = html[:canon.end()], html[canon.end():]
    while ALT.match(rest):                       # anciennes alternates, remplacées
        rest = rest[ALT.match(rest).end():]
    html = head + "".join(f'<link rel="alternate" hreflang="{h}" href="{BASE}{p}">\n' for h, p in alts) + rest
    meta = re.search(r'<p class="meta">.*?</p>\n', html)
    if not meta:
        meta = re.search(r'</h1>\n', html)
    if not meta:
        raise ValueError("ni méta ni h1")
    head, rest = html[:meta.end()], html[meta.end():]
    if LANGS.match(rest):
        rest = rest[LANGS.match(rest).end():]
    return head + links + "\n" + rest


def main():
    check = "--check" in sys.argv
    tr = translations()
    todo = 0
    for fr_path in sorted(tr):
        f = os.path.join(ROOT, fr_path.strip("/"), "index.html")
        if not os.path.exists(f):
            print(f"  ✗ {fr_path} : page française absente")
            todo += 1
            continue
        html = open(f, encoding="utf-8").read()
        alts, links = alternates_for(fr_path, tr)
        new = fix(html, alts, links)
        if new != html:
            todo += 1
            print(f"  {'~' if check else '✓'} {fr_path}")
            if not check:
                with open(f, "w", encoding="utf-8") as fh:
                    fh.write(new)
    print(f"{len(tr)} pages françaises traduites — {todo} {'à mettre à jour' if check else 'mise(s) à jour'}")
    sys.exit(1 if check and todo else 0)


if __name__ == "__main__":
    main()
