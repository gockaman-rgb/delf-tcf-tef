#!/usr/bin/env python3
"""Pages d'examen en « hub + modules » (19/09/2026).

Chaque examen du menu (TCF Canada, TCF IRN, TCF Québec, TEF Canada, DELF B1, DELF B2, DALF) a :
  - une page d'accueil COURTE à son URL historique (/tcf-canada/…) : ce qu'est l'examen, pour qui,
    chiffres-clés, parcours en 5 étapes, grille des modules, FAQ courte ;
  - des sous-pages (« modules ») qui reprennent, section par section, le texte vérifié de l'ancien
    pilier : /tcf-canada/format/, /tcf-canada/score-nclc/, … rendues par article_template.

Source du texte : `_build/data/pillars_src/<slug>.html` (les piliers tels qu'ils étaient le
19/09/2026, avec les blocs modules/centres). Ne pas éditer les pages générées à la main :
modifier la source ou la configuration (exam_hubs_config.py) puis relancer.

Usage : python3 _build/exam_hubs.py
"""

import os
import re
import sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from article_template import render  # noqa: E402
from pillar_modules import PILLARS, stats, steps  # noqa: E402
from exam_hubs_config import EXAMS  # noqa: E402

DATE = "2026-09-19"
DATE_FR = "19 septembre 2026"
SRC = os.path.join(HERE, "data", "pillars_src")


def parse_pillar(slug):
    s = open(os.path.join(SRC, slug + ".html"), encoding="utf-8").read()
    d = {
        "title": re.search(r"<title>(.*?)</title>", s).group(1),
        "desc": re.search(r'name="description" content="(.*?)"', s).group(1),
        "h1": re.search(r"<h1>(.*?)</h1>", s, re.S).group(1).strip(),
        "accent": re.search(r'<body class="([^"]*)"', s).group(1),
        "published": re.search(r'"datePublished":\s?"([^"]+)"', s).group(1),
        "intro": re.search(r'<p class="intro">(.*?)</p>', s, re.S).group(1).strip(),
        "facts": re.findall(r"<li>(.*?)</li>", re.search(r'<div class="facts">(.*?)</ul></div>', s, re.S).group(1), re.S),
    }
    body = s[s.index("</ol></details>") + len("</ol></details>"):]
    body = re.sub(r"<!-- modules:start -->.*?<!-- modules:end -->\n?", "", body, flags=re.S)
    body = body[: body.index('<footer class="site">')]
    # sections h2 → html, hors faq / a-lire
    parts = re.split(r'(?=<h2 id="[^"]+">)', body)
    secs = OrderedDict()
    for part in parts:
        m = re.match(r'<h2 id="([^"]+)">(.*?)</h2>', part, re.S)
        if not m or m.group(1) in ("faq", "a-lire"):
            continue
        html_ = part[m.end():]
        html_ = re.sub(r'<div class="cta-band">.*?</div>\n?', "", html_, flags=re.S)
        html_ = re.sub(r'<aside class="cta-inline">.*?</aside>\n?', "", html_, flags=re.S)
        secs[m.group(1)] = (m.group(2).strip(), html_.strip())
    d["sections"] = secs
    faq_html = re.search(r'<div class="faq">(.*?)</div>\s*<h2 id="a-lire">', body, re.S).group(1)
    d["faq"] = [(q.strip(), re.sub(r"\s+", " ", a).strip()) for q, a in
                re.findall(r"<details><summary>(.*?)</summary>\s*<p>(.*?)</p></details>", faq_html, re.S)]
    also_html = re.search(r'<h2 id="a-lire">.*?<ul class="posts">(.*?)</ul>', body, re.S).group(1)
    d["also"] = [(u, t.strip(), re.sub(r"\s+", " ", de).strip()) for u, t, de in
                 re.findall(r'<li><a href="([^"]+)">(.*?)</a>\s*<p>(.*?)</p></li>', also_html, re.S)]
    cta = re.search(r'<div class="cta-band">\s*<h2>(.*?)</h2>\s*<p>(.*?)</p>', body, re.S)
    d["cta_h2"], d["cta_p"] = cta.group(1).strip(), re.sub(r"\s+", " ", cta.group(2)).strip()
    notes = re.findall(r'<div class="note">\s*<p>(.*?)</p>\s*</div>', body, re.S)
    d["sources"] = re.sub(r"\s+", " ", notes[-1]).strip() if notes else ""
    return d


def remap(html_, amap, keep):
    """href="#id" → URL absolue quand l'ancre n'est pas sur la page."""
    def rep(m):
        anchor = m.group(1)
        if anchor in keep or anchor not in amap:
            return m.group(0)
        return f'href="{amap[anchor]}"'
    return re.sub(r'href="#([^"]+)"', rep, html_)


def words(html_):
    return len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", html_)))


def build_exam(slug, cfg):
    src = parse_pillar(slug)
    pil = PILLARS[slug]
    name = cfg["name"]
    spokes = cfg["spokes"]
    # carte des ancres : section id → URL du module qui la porte
    amap = {}
    for sp in spokes:
        for sec in sp["sections"]:
            amap[sec] = f"/{slug}/{sp['slug']}/#{sec}"
    for sp in spokes:
        amap.setdefault(sp["slug"], f"/{slug}/{sp['slug']}/")
    # ancres présentes DANS les sections (h3 id=…) : rattachées au module
    for sp in spokes:
        for sec in sp["sections"]:
            for hid in re.findall(r'\sid="([^"]+)"', src["sections"][sec][1]):
                amap.setdefault(hid, f"/{slug}/{sp['slug']}/#{hid}")
    faq_used = set()
    out = []
    # --- modules (sous-pages)
    for sp in spokes:
        keep = set(sp["sections"]) | {"faq", "a-lire"}
        for sec in sp["sections"]:
            keep |= set(re.findall(r'\sid="([^"]+)"', src["sections"][sec][1]))
        body = "\n\n".join(f'<h2 id="{sec}">{src["sections"][sec][0]}</h2>\n{src["sections"][sec][1]}' for sec in sp["sections"])
        body = remap(body, amap, keep)
        if sp.get("extra_top"):
            body = sp["extra_top"] + "\n" + body
        faq = [src["faq"][i] for i in sp["faq"]] + [(q, a) for q, a in sp.get("faq_extra", [])]
        faq_used.update(sp["faq"])
        siblings = [(f"/{slug}/{o['slug']}/", o["crumb"], o["desc_short"]) for o in spokes if o is not sp]
        also = [(f"/{slug}/", f"{name} : la page d'accueil", cfg["landing_short"])] + siblings[:3]
        toc = list(sp.get("toc_top", [])) + [(sec, re.sub(r"<[^>]+>", "", src["sections"][sec][0])) for sec in sp["sections"]]
        a = {
            "section": slug, "section_name": name, "og_slug": slug,
            "slug": sp["slug"], "accent": src["accent"], "crumb": sp["crumb"],
            "title": sp["title"], "desc": sp["desc"], "h1": sp["h1"],
            "published": DATE, "modified": DATE, "date_fr": DATE_FR,
            "read": max(3, (words(body) + 200) // 200),
            "intro": remap(sp["intro"], amap, keep),
            "facts": [remap(f, amap, keep) for f in sp["facts"]],
            "toc": toc, "body": body,
            "cta_h2": src["cta_h2"], "cta_p": src["cta_p"],
            "faq": faq, "also": also, "sources": src["sources"],
        }
        assert len(a["title"]) <= 60, (slug, sp["slug"], len(a["title"]))
        assert len(a["desc"]) <= 158, (slug, sp["slug"], len(a["desc"]))
        assert faq, (slug, sp["slug"], "FAQ vide")
        out.append(a)
    # --- page d'accueil de l'examen
    keep = {"faq", "a-lire", "parcours", "modules", "quest-ce"}
    mods = '<div class="grid c2 modules">\n' + "\n".join(
        f'<div class="card card-link"><span class="tag">{t}</span><h3><a href="{h}">{ti}</a></h3><p>{d}</p></div>'
        for t, ti, h, d in cfg["modules"]) + "\n</div>"
    if cfg.get("villes"):
        from villes_config import VILLES
        by = {v["slug"]: v for v in VILLES}
        mods += ('\n<p class="serie-label">Où passer, ville par ville</p>\n<div class="chips">\n'
                 + "\n".join(f'<a class="chip" href="/centres/{sl}/">{by[sl]["crumb"]}</a>' for sl in cfg["villes"])
                 + '\n<a class="chip" href="/centres/">Toutes les villes →</a>\n</div>')
    body = (f"{stats(pil['stats'])}\n\n<h2 id=\"quest-ce\">{cfg['what_h2']}</h2>\n{cfg['what']}\n\n"
            f"<h2 id=\"parcours\">Votre parcours en 5 étapes</h2>\n{steps(pil['steps'])}\n\n"
            f"<h2 id=\"modules\">Le dossier, module par module</h2>\n{mods}\n")
    body = remap(body, amap, keep)
    landing_faq = [(q, a) for q, a in cfg["faq"]] + [src["faq"][i] for i in range(len(src["faq"])) if i not in faq_used]
    a = {
        "section": "", "slug": slug, "accent": src["accent"], "crumb": name,
        "title": cfg.get("title", src["title"]), "desc": cfg.get("desc", src["desc"]), "h1": cfg.get("h1", src["h1"]),
        "published": src["published"], "modified": DATE, "date_fr": DATE_FR,
        "read": max(4, (words(body) + 200) // 200),
        "intro": remap(cfg.get("intro", src["intro"]), amap, keep),
        "facts": [remap(f, amap, keep) for f in src["facts"]],
        "toc": [("quest-ce", cfg["what_h2"]), ("parcours", "Votre parcours en 5 étapes"), ("modules", "Le dossier, module par module")],
        "body": body,
        "cta_h2": src["cta_h2"], "cta_p": src["cta_p"],
        "faq": landing_faq, "also": src["also"], "sources": src["sources"],
    }
    assert len(a["title"]) <= 60 and len(a["desc"]) <= 165, (slug, len(a["title"]), len(a["desc"]))
    out.append(a)
    return out


def main():
    for slug, cfg in EXAMS.items():
        for a in build_exam(slug, cfg):
            path, w = render(a, overwrite=True)
            print(f"  ✓ {path[len(ROOT):-len('index.html')]} — {w} mots")


if __name__ == "__main__":
    main()
