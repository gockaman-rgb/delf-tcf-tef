#!/usr/bin/env python3
"""Applique la coupe (coupe_config.py) au site publié ; idempotent, à lancer après les générateurs, avant app_links.py.

1. Page de renvoi pour chaque chemin de REDIRECTS : meta refresh + canonical vers la cible (pas de 301 sur GitHub Pages).
2. Dans toutes les pages publiées, y compris celles écrites à la main, et dans les données du moteur de centres : un lien
   vers une page coupée pointe directement vers sa cible.

Usage : python3 _build/coupe.py
"""
import glob
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from article_template import BASE, redirect_map, retarget_links  # noqa: E402
from coupe_config import TITRES_CIBLES  # noqa: E402

TEXTES = {
    "fr": ("Page regroupée", "Cette page a été regroupée", "{label} : les centres, les prix et les dates sont maintenant sur la page"),
    "es": ("Página reagrupada", "Esta página se ha reagrupado", "{label}: los centros, los precios y las fechas están ahora en la página"),
}


def stub(path, target, label, lang):
    hub = target.split("#")[0]
    title, h1, phrase = TEXTES[lang]
    name = TITRES_CIBLES[hub]
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url={html.escape(target)}">
<title>{title} : {html.escape(label)}</title>
<link rel="canonical" href="{BASE}{hub}">
<link rel="stylesheet" href="/style.css">
<link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">
</head>
<body>
<article class="page"><div class="wrap narrow">
<h1>{h1}</h1>
<p>{phrase.format(label=html.escape(label))} <a href="{html.escape(target)}">{html.escape(name)}</a>.</p>
</div></article>
</body>
</html>
"""


def main():
    rd = redirect_map()
    n_stub = n_files = 0
    for path, (target, label, lang) in rd.items():
        f = os.path.join(ROOT, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(f), exist_ok=True)
        new = stub(path, target, label, lang)
        old = open(f, encoding="utf-8").read() if os.path.exists(f) else ""
        if old != new:
            open(f, "w", encoding="utf-8").write(new)
            n_stub += 1
    for f in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        rel = os.path.relpath(f, ROOT)
        if rel.split(os.sep)[0].startswith(("_", ".")):
            continue
        t = open(f, encoding="utf-8").read()
        if 'http-equiv="refresh"' in t[:1000]:
            continue
        new = retarget_links(t)
        if new != t:
            open(f, "w", encoding="utf-8").write(new)
            n_files += 1
    # Moteur de centres : ses fiches portent des liens vers les pages de ville
    n_json = 0
    for f in glob.glob(os.path.join(ROOT, "data", "finder", "**", "*.json"), recursive=True):
        t = open(f, encoding="utf-8").read()
        new = t
        for p, (target, _, _) in rd.items():
            new = new.replace(f'"{p}"', f'"{target}"')
        if new != t:
            open(f, "w", encoding="utf-8").write(new)
            n_json += 1
    print(f"coupe : {len(rd)} renvois ({n_stub} écrits), liens retournés dans {n_files} pages et {n_json} fichiers du moteur")


if __name__ == "__main__":
    main()
