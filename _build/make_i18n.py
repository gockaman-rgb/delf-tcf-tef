#!/usr/bin/env python3
"""Guides et pages d'examen en espagnol et en anglais (08/10/2026).

Rend les specs de i18n_pages_es.py et i18n_pages_en.py avec article_template (gabarit, en-tête, pied et
libellés de la langue). Une spec est un article traduit : fr_path (l'original, s'il existe), lang, variant,
section/slug, title, desc, h1, intro, facts, toc, body, faq, also, sources — plus, au besoin, crumbs, cta_h2,
cta_p, accent, date_label/modified (par défaut le 08/10/2026, date de la traduction ; les faits gardent leur
propre date dans le texte, comme sur la page française).

Usage : python3 _build/make_i18n.py [--force]
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from article_template import build  # noqa: E402
from i18n_registry import alternates_for, path_of, translations  # noqa: E402
from make_pays import DATE_LABEL  # noqa: E402
from i18n_blocks import cta_inline  # noqa: E402

OG_LOCALE = {"es-ES": "es_ES", "es-419": "es_LA", "en-US": "en_US", "en-GB": "en_GB", "en-CA": "en_CA"}
HOME = {"es": ("Inicio", "/es/"), "en": ("Home", "/en/")}
CTA = {
    "en": ("Practise on the real format",
           "You pay the full fee for each session, and you can’t retake the test right away. The mock exams in the "
           "“TCF DELF TEF: Tests 2026” app follow the official format of each test — TCF Canada, TEF Canada, DELF, "
           "DALF — scored like the real thing, with AI feedback on writing and speaking."),
    "es": ("Entrena con el formato real",
           "Cada sesión se paga completa y no se puede repetir de inmediato. Los simulacros de la app «TCF DELF TEF: "
           "Tests 2026» reproducen el formato oficial de cada examen —TCF Canada, TEF Canada, DELF, DALF— con la "
           "puntuación del examen real y corrección con IA de la expresión escrita y oral. La app está en español."),
}


def specs():
    out = []
    for mod in ("i18n_pages_es", "i18n_pages_en"):
        try:
            out += __import__(mod).PAGES
        except ModuleNotFoundError as e:
            if e.name != mod:
                raise
    return out


def words(html_):
    return len(re.sub(r"<[^>]+>", " ", html_).split())


def article(spec, tr):
    lang, var = spec["lang"], spec["variant"]
    a = dict(spec)
    a.setdefault("section", lang)
    a.setdefault("crumbs", [HOME[lang]])
    a.setdefault("accent", "accent-tcf")
    a.setdefault("in_language", var)
    a.setdefault("og_locale", OG_LOCALE[var])
    a.setdefault("og_slug", (lang + "-" + path_of(spec).strip("/").split("/", 1)[1].replace("/", "-")))
    a.setdefault("published", "2026-10-08")
    a.setdefault("modified", a["published"])
    a["date_fr"] = a.pop("date_label", DATE_LABEL[var])
    a.setdefault("cta_h2", CTA[lang][0].replace("Practise", "Practice") if var == "en-US" else CTA[lang][0])
    a.setdefault("cta_p", CTA[lang][1])
    a.setdefault("read", max(3, round(words(a["intro"] + a["body"]) / 220)))
    # Carte « Entraînez-vous » avant le 3e h2, comme sur les articles français (sauf inline_cta=False)
    h2 = [m.start() for m in re.finditer(r"<h2[ >]", a["body"])]
    if a.pop("inline_cta", True) and len(h2) >= 3 and "cta-inline" not in a["body"]:
        a["body"] = a["body"][:h2[2]] + cta_inline(lang, var) + a["body"][h2[2]:]
    if spec.get("fr_path"):
        alts, links = alternates_for(spec["fr_path"], tr, current=lang)
        a["alternates"], a["lang_links"] = alts, links
    for k in ("fr_path", "variant"):
        a.pop(k, None)
    assert len(a["title"]) <= 60, (path_of(spec), len(a["title"]), a["title"])
    assert len(a["desc"]) <= 155, (path_of(spec), len(a["desc"]))
    return a


def main():
    tr = translations()
    build([article(s, tr) for s in specs()], overwrite="--force" in sys.argv)


if __name__ == "__main__":
    main()
