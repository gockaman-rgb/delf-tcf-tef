# -*- coding: utf-8 -*-
"""Registre des traductions (08/10/2026) : quelle page française a quelle version /es/ ou /en/.

Chaque spec traduite porte le chemin de son original (fr_path). Les sources : pays_config_es / pays_config_en
(pages pays, make_pays.py) et i18n_pages_es / i18n_pages_en (guides et pages d'examen, make_i18n.py). Une page
traduite sans équivalent français (hubs /es/ et /en/, villes d'Espagne, Dubaï) n'a pas de fr_path et n'entre pas
au registre.

article_template.render() s'en sert pour les pages françaises générées ; i18n_static.py pour les pages
françaises écrites à la main ; check_i18n.py pour contrôler les paires.
"""
import importlib

SOURCES = ("pays_config_es", "pays_config_en", "i18n_pages_es", "i18n_pages_en")
LINK_LABEL = {"fr": "Lire en français", "es": "Leer en español", "en": "Read in English"}


def specs():
    """Toutes les specs traduites, toutes sources confondues (une source absente est ignorée)."""
    out = []
    for mod in SOURCES:
        try:
            out += importlib.import_module(mod).PAGES
        except ModuleNotFoundError as e:
            if e.name != mod:
                raise
    return out


def path_of(spec):
    """Chemin publié d'une spec traduite : /<section>/<slug>/ (section = lang par défaut)."""
    return f"/{spec.get('section', spec['lang'])}/{spec['slug']}/"


def translations():
    """{chemin français: [(lang, chemin traduit), …]}"""
    tr = {}
    for p in specs():
        if p.get("fr_path"):
            tr.setdefault(p["fr_path"], []).append((p["lang"], path_of(p)))
    return tr


def alternates_for(fr_path, tr=None, current="fr"):
    """([(hreflang, chemin)], <p class="langs">…</p>) pour une page et ses traductions, ou (None, None)."""
    tr = translations() if tr is None else tr
    if fr_path not in tr:
        return None, None
    alts = [("fr", fr_path)] + tr[fr_path] + [("x-default", fr_path)]
    others = [("fr", fr_path)] + tr[fr_path]
    links = '<p class="langs">' + " · ".join(f'<a href="{p}" hreflang="{l}" lang="{l}">{LINK_LABEL[l]}</a>'
                                            for l, p in others if l != current) + "</p>"
    return alts, links
