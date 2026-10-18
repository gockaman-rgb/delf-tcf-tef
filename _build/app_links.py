#!/usr/bin/env python3
"""Liens App Store mesurés (18/10/2026) : pose pt / ct / mt sur chaque lien vers l'app, page par page.

Pourquoi : sans eux, App Store Connect (App Analytics → Sources → Campagnes) ne dit pas quelle page du site amène des
téléchargements. Avec eux, chaque page a sa campagne : ct = « web-<chemin> » (40 caractères au plus, la limite
d'Apple), par exemple /centres/tcf-alger/ → web-centres-tcf-alger, / → web-home.

PT : le « provider token » d'App Store Connect (App Analytics → Sources → Campagnes → « Générer un lien de
campagne » : le nombre après pt= dans le lien généré). Tant qu'il est vide, ce script ne touche à rien, et
check_site.py ne contrôle rien. Une fois rempli, lancer ce script en DERNIER, après tous les générateurs : ils
réécrivent les liens nus, et check_site.py signale toute page oubliée.

Seuls les liens vers l'app TCF DELF TEF (id6790412304) sont touchés ; l'autre app (id6761140087) n'a pas de campagne.
Le script est idempotent : il remplace pt/ct/mt existants et garde les autres paramètres (l, see-all…).

Usage : python3 _build/app_links.py
"""
import glob
import os
import re
import sys
from urllib.parse import parse_qsl, urlencode

PT = ""  # ← coller ici le provider token d'App Store Connect (chiffres seulement)
APP_ID = "id6790412304"
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LINK = re.compile(r'href="(https://apps\.apple\.com/[^"]*' + APP_ID + r')(\?[^"#]*)?"')


def campaign(rel_path):
    """/centres/tcf-alger/index.html → web-centres-tcf-alger ; index.html → web-home."""
    p = rel_path.replace(os.sep, "/")
    p = p[:-len("index.html")] if p.endswith("index.html") else p
    p = p.strip("/")
    slug = re.sub(r"[^a-z0-9-]+", "-", p.lower()).strip("-") or "home"
    return ("web-" + slug)[:40].rstrip("-")


def with_campaign(base, query, ct):
    keep = [(k, v) for k, v in parse_qsl((query or "").lstrip("?").replace("&amp;", "&"), keep_blank_values=True)
            if k not in ("pt", "ct", "mt")]
    q = urlencode(keep + [("pt", PT), ("ct", ct), ("mt", "8")])
    return f'href="{base}?{q.replace("&", "&amp;")}"'


def main():
    if not PT:
        print("app_links : PT vide — rien à faire (voir l'en-tête du script).")
        return 0
    n_files = n_links = 0
    for f in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        rel = os.path.relpath(f, ROOT)
        if rel.startswith(("_build", ".git")):
            continue
        s = open(f, encoding="utf-8").read()
        ct = campaign(rel)
        new, k = LINK.subn(lambda m: with_campaign(m.group(1), m.group(2), ct), s)
        if k and new != s:
            open(f, "w", encoding="utf-8").write(new)
            n_files += 1
        n_links += k
    print(f"app_links : {n_links} liens, {n_files} fichiers réécrits (pt={PT}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
