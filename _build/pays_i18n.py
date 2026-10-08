# -*- coding: utf-8 -*-
"""Pages pays traduites (/es/, /en/ — 08/10/2026) : ce qu'elles partagent avec la page française.

Une traduction reprend de sa page française la structure et les faits — fichier FEI, mise en page, sites
corrigés (urls, org_url), clés des badges — et réécrit le texte dans pays_config_es.py / pays_config_en.py.
Les libellés des badges se traduisent par BADGES : un libellé absent fait échouer la génération plutôt
que de laisser du français sur la page. Glossaire et règles de rédaction : _build/i18n_glossary.md.
"""
from pays_config import PAGES as _FR, table
from villes_config import VILLES as _VILLES

FR = {p["slug"]: p for p in _FR}
VILLES = {v["slug"]: v for v in _VILLES}

BADGES = {
    "es-ES": {"TCF Canada": "TCF Canada", "pas de TCF Canada": "sin TCF Canada", "sur demande": "bajo petición",
              "à la demande": "bajo petición", "TCF absent du site": "sin TCF en su web", "TCF absent de son site": "sin TCF en su web",
              "aucune session TCF publiée": "ninguna convocatoria de TCF publicada", "rien de publié pour 2026": "nada publicado para 2026",
              "dès 5 inscrits": "desde 5 inscritos", "tout public seulement": "solo TCF tout public", "dates 2025 seulement": "solo fechas de 2025"},
    "es-419": {"TCF Canada": "TCF Canada", "pas de TCF Canada": "sin TCF Canada", "sur demande": "a solicitud",
               "à la demande": "a solicitud", "TCF absent du site": "sin TCF en su sitio web", "TCF absent de son site": "sin TCF en su sitio web",
               "aucune session TCF publiée": "ninguna sesión de TCF publicada", "rien de publié pour 2026": "nada publicado para 2026",
               "dès 5 inscrits": "desde 5 inscritos", "tout public seulement": "solo TCF tout public", "dates 2025 seulement": "solo fechas de 2025"},
    "en": {"TCF Canada": "TCF Canada", "pas de TCF Canada": "no TCF Canada", "sur demande": "on request", "à la demande": "on request",
           "TCF absent du site": "no TCF on its website", "TCF absent de son site": "no TCF on its website",
           "aucune session TCF publiée": "no TCF session published", "rien de publié pour 2026": "nothing published for 2026",
           "dès 5 inscrits": "from 5 candidates", "tout public seulement": "TCF tout public only", "dates 2025 seulement": "2025 dates only"},
}

# « Non relevé » : non publié, ou non vérifié.
NR = {"es": "sin datos", "en": "no data"}

OG_LOCALE = {"Espagne": "es_ES", "Mexique": "es_MX", "Colombie": "es_CO", "Argentine": "es_AR", "Chili": "es_CL",
             "Pérou": "es_PE", "Équateur": "es_EC", "États-Unis": "en_US", "Royaume-Uni": "en_GB", "Canada": "en_CA"}


def from_fr(fr_slug, lang, variant, country, **kw):
    """Spec d'une traduction de /centres/<fr_slug>/ : partagé avec le français, puis le texte (kw)."""
    f = FR[fr_slug]
    t = BADGES.get(variant) or BADGES[lang]
    d = dict(lang=lang, variant=variant, fr_path=f"/centres/{fr_slug}/", exam=f["exam"], file=f["file"], layout=f["layout"],
             og_locale=OG_LOCALE[country],
             badges={k: [(kind, t[label]) for kind, label in v] for k, v in f.get("badges", {}).items()})
    for k in ("urls", "org_url", "region_sort", "toc_regions"):
        if k in f:
            d[k] = f[k]
    d.update(kw)
    return d


def canada(fr_slug, **kw):
    """Pages anglaises du Canada : liste FEI du 19/09/2026 et relevé du 17/09, comme les pages françaises.
    Une page ville reprend les villes (match) et les voisines (nearby) de villes_config."""
    d = dict(lang="en", variant="en-CA", fr_path=f"/centres/{fr_slug}/", exam="tcf", file="tcf_canada",
             og_locale="en_CA", list_date="19 September 2026", releve_date="17 September 2026", country_name="Canada")
    if fr_slug in VILLES:
        v = VILLES[fr_slug]
        d.update(layout="city", match=v["match"], nearby=v["nearby"])
    else:
        d.update(layout="regions", region_sort="count")
    d.update(kw)
    return d


def releve(rows, variant, caption):
    head = (["Centro", "Versiones", "Precio", "Convocatorias y matrícula" if variant == "es-ES" else "Sesiones e inscripción"]
            if variant.startswith("es") else
            ["Center" if variant == "en-US" else "Centre", "Versions", "Price", "Sessions and registration"])
    return table(caption, head, [(f"<strong>{a}</strong>", b, c, d) for a, b, c, d in rows])
