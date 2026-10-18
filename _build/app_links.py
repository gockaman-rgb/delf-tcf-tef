#!/usr/bin/env python3
"""Liens App Store mesurés (18/10/2026) : pose pt / ct / mt sur chaque lien vers l'app.

Pourquoi : sans eux, App Store Connect (App Analytics → Acquisition → Campaigns) ne dit pas quelle partie du site amène
des téléchargements. Avant (17/09-16/10/2026, « Web Referrers ») : delf-tcf-tef.fr = 53 vues de la fiche, 34
téléchargements, sans détail par page.

Campagnes PAR GROUPE de pages, pas par page : Apple n'affiche une campagne qu'à partir de 5 installations, et limite
son nom à 30 caractères. Groupes : web-fr-accueil, web-fr-maghreb (pages Algérie, Maroc, Tunisie, guide IFAL),
web-fr-centres (autres centres, où passer, dates, prix), web-fr-entrainement (exercices, sujets, examens blancs,
logiciel, questions), web-fr-examens (pages TCF Canada, IRN, Québec, TEF, DELF, DALF), web-fr-blog (le reste) ;
web-<en|es|ar>-accueil, -centres (pages pays et ville), -preparation (le reste).

PT : provider token d'App Store Connect (le nombre après pt= dans un lien de campagne généré). Lancer ce script en
DERNIER, après tous les générateurs : ils réécrivent les liens nus, et check_site.py signale toute page oubliée.
Seuls les liens vers l'app TCF DELF TEF (id6790412304) sont touchés. Idempotent : remplace pt/ct/mt existants.

Usage : python3 _build/app_links.py
"""
import glob
import os
import re
import sys
from urllib.parse import parse_qsl, urlencode

PT = "128697232"  # provider token App Store Connect (lu le 18/10/2026 dans le générateur de liens de campagne)
APP_ID = "id6790412304"
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LINK = re.compile(r'href="(https://apps\.apple\.com/[^"]*' + APP_ID + r')(\?[^"#]*)?"')


MAGHREB_BLOG = {"tcf-canada-algerie", "tcf-canada-maroc", "tcf-canada-tunisie", "ifal-tcf-rendez-vous"}
CENTRES_BLOG = {"tcf-canada-dates-2026", "calendrier-delf-dalf-2026-2027", "prix-tcf-tef"}
TRAINING_FR = {"examens-blancs", "examens", "logiciel-tcf", "plan-etude", "questions", "contenu", "correction-ia", "audio"}
EXAMS_FR = {"tcf-canada", "tcf-irn", "tcf-quebec", "tef-canada", "delf-b1", "delf-b2", "dalf", "score-tcf-699"}
_LOC = {}


def _maghreb_centres():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from villes_config import VILLES
    return {v["slug"] for v in VILLES if v["country"] in ("dz", "ma", "tn")} | {"tcf-algerie", "tcf-maroc", "tcf-tunisie"}


def _loc(lang):
    """Slugs des pages pays et ville d'une langue (pays_config_<lang>)."""
    if lang not in _LOC:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        _LOC[lang] = {p["slug"] for p in __import__("pays_config_" + lang).PAGES}
    return _LOC[lang]


def campaign(rel_path):
    """Chemin d'une page (« centres/tcf-alger/index.html ») → nom de campagne (≤ 30 caractères)."""
    parts = [x for x in rel_path.replace(os.sep, "/").split("/") if x and x != "index.html"]
    if not parts:
        return "web-fr-accueil"
    head = parts[0]
    if head in ("en", "es", "ar"):
        if len(parts) == 1:
            return f"web-{head}-accueil"
        return f"web-{head}-" + ("centres" if parts[1] in _loc(head) else "preparation")
    slug = parts[1] if len(parts) > 1 else ""
    if head == "centres":
        return "web-fr-maghreb" if slug in _maghreb_centres() else "web-fr-centres"
    if head == "blog":
        if slug in MAGHREB_BLOG:
            return "web-fr-maghreb"
        if slug in CENTRES_BLOG or slug.startswith("ou-passer"):
            return "web-fr-centres"
        if slug.startswith(("exercices-", "sujets-", "examen-blanc", "production-ecrite", "synthese-", "tefaq-")):
            return "web-fr-entrainement"
        return "web-fr-blog"
    if head == "ou-passer":
        return "web-fr-centres"
    if head in TRAINING_FR:
        return "web-fr-entrainement"
    if head in EXAMS_FR:
        return "web-fr-examens"
    return "web-fr-blog"


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
