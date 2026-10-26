#!/usr/bin/env python3
"""Sitemap ↔ pages publiées (26/10/2026).

Invariant constaté le 26/10/2026 : chaque index.html publié (hors _build/) est dans sitemap.xml, et rien d'autre ;
chaque entrée porte <lastmod> et <priority>. Ce script le rétablit sans toucher à l'ordre ni aux entrées existantes :
les pages nouvelles s'ajoutent à la fin (triées, lastmod = aujourd'hui, priority 0.8), une page modifiée dans l'arbre
de travail (git) reçoit le lastmod du jour, une URL dont la page a disparu est retirée et signalée. Une page en
noindex n'entre pas. generate.py réécrit sitemap.xml avec ses seules pages : ne jamais le relancer.

Usage : python3 _build/sitemap_sync.py [--check]   (--check : n'écrit rien, code 1 si le sitemap n'est pas à jour)
"""
import datetime
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
BASE = "https://delf-tcf-tef.fr"
SITEMAP = os.path.join(ROOT, "sitemap.xml")
TODAY = datetime.date.today().isoformat()


def url_of(rel):
    d = os.path.dirname(rel)
    return "/" + d.replace(os.sep, "/") + "/" if d else "/"


def published_pages():
    pages = set()
    for f in glob.glob(os.path.join(ROOT, "**", "index.html"), recursive=True):
        rel = os.path.relpath(f, ROOT)
        if rel.split(os.sep)[0].startswith(("_", ".")):
            continue
        with open(f, encoding="utf-8") as fh:
            head = fh.read(4000)
        if re.search(r'<meta name="robots" content="[^"]*noindex', head):
            continue
        pages.add(url_of(rel))
    return pages


def _content(t):
    """Ce qui compte pour <lastmod> : la page sans son pied de page ni les paramètres de campagne App Store."""
    t = re.sub(r'<footer class="site".*?</footer>', "", t, flags=re.S)
    return re.sub(r"(apps\.apple\.com/[^\"']*?)\?[^\"']*", r"\1", t)


def modified_pages():
    """Pages publiées dont le contenu a changé dans l'arbre de travail par rapport à HEAD (un pied de page ou un lien
    App Store retouché sur tout le site ne date pas 300 pages du jour)."""
    out = subprocess.run(["git", "-C", ROOT, "diff", "--name-only", "HEAD"], capture_output=True, text=True).stdout
    changed = set()
    for p in out.split():
        if not p.endswith("index.html") or not os.path.exists(os.path.join(ROOT, p)):
            continue
        old = subprocess.run(["git", "-C", ROOT, "show", f"HEAD:{p}"], capture_output=True, text=True).stdout
        with open(os.path.join(ROOT, p), encoding="utf-8") as fh:
            new = fh.read()
        if _content(old) != _content(new):
            changed.add(url_of(p))
    return changed


def main():
    with open(SITEMAP, encoding="utf-8") as fh:
        blocks = re.findall(r"<url>.*?</url>", fh.read(), flags=re.S)
    current = [(re.search(r"<loc>" + re.escape(BASE) + r"([^<]*)</loc>", b).group(1), b) for b in blocks]
    pages, touched = published_pages(), modified_pages()
    kept, gone, bumped = [], [], []
    for u, b in current:
        if u not in pages:
            gone.append(u)
            continue
        if u in touched and f"<lastmod>{TODAY}</lastmod>" not in b:
            b = re.sub(r"<lastmod>[^<]*</lastmod>", f"<lastmod>{TODAY}</lastmod>", b)
            bumped.append(u)
        kept.append(b)
    added = sorted(pages - {u for u, _ in current})
    new = [f"<url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod><priority>0.8</priority></url>" for u in added]
    if "--check" in sys.argv:
        print(f"sitemap : {len(current)} URL ; à ajouter {len(added)}, à retirer {len(gone)}, lastmod à dater {len(bumped)}")
        for u in added:
            print("  +", u)
        for u in gone:
            print("  -", u)
        sys.exit(1 if added or gone or bumped else 0)
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += ["  " + b for b in kept + new]
    sm.append("</urlset>")
    with open(SITEMAP, "w", encoding="utf-8") as fh:
        fh.write("\n".join(sm) + "\n")
    print(f"sitemap.xml : {len(kept) + len(new)} URL (+{len(added)}, -{len(gone)}, lastmod du jour sur {len(bumped)})")
    for u in added:
        print("  +", u)
    for u in gone:
        print("  - (page disparue)", u)


if __name__ == "__main__":
    main()
