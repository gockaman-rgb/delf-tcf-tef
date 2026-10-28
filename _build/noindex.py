#!/usr/bin/env python3
"""Pages fermées à Google (28/10/2026) : pose ou retire <meta name="robots" content="noindex"> dans les pages publiées
d'après _build/noindex.txt (un chemin par ligne, « /en/delf-italy/ » ; lignes « # » ignorées). Idempotent : une page de
la liste reçoit la balise une fois, une page hors liste la perd. article_template.render() lit la même liste, donc une
page régénérée garde son état. sitemap_sync.py ignore les pages en noindex.

Pourquoi : le 26/10/2026, 80 pages mises en ligne le même jour ont fait déclasser tout le site (SEO_INCIDENT_2026-10-28.md).
Rouvrir une page à Google = retirer sa ligne, relancer ce script puis sitemap_sync.py.

Usage : python3 _build/noindex.py [--check]
"""
import glob
import os
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
META = '<meta name="robots" content="noindex">\n'
ANCHOR = '<meta name="viewport" content="width=device-width, initial-scale=1">\n'

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from article_template import noindex_paths  # noqa: E402


def main():
    check = "--check" in sys.argv
    wanted = noindex_paths()
    added = removed = 0
    for f in glob.glob(os.path.join(ROOT, "**", "index.html"), recursive=True):
        rel = os.path.relpath(f, ROOT)
        if rel.split(os.sep)[0].startswith(("_", ".")):
            continue
        d = os.path.dirname(rel)
        path = "/" + d.replace(os.sep, "/") + "/" if d else "/"
        with open(f, encoding="utf-8") as fh:
            t = fh.read()
        has = META in t
        if path in wanted and not has:
            if ANCHOR not in t:
                raise SystemExit(f"{rel} : pas de balise viewport, balise robots non posée")
            t = t.replace(ANCHOR, ANCHOR + META, 1)
            added += 1
        elif path not in wanted and has:
            t = t.replace(META, "", 1)
            removed += 1
        else:
            continue
        if not check:
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(t)
    print(("à poser" if check else "posées") + f" : {added} · " + ("à retirer" if check else "retirées") + f" : {removed} · liste : {len(wanted)}")
    sys.exit(1 if check and (added or removed) else 0)


if __name__ == "__main__":
    main()
