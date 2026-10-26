#!/usr/bin/env python3
"""Chercheur de centres (26/10/2026) : /trouver-un-centre/, /en/test-centre-near-me/, /es/centro-de-examen-cerca-de-mi/,
/ar/test-centre-near-me/.

Les textes vivent dans finder_pages.py ; les chiffres, la date des listes et la liste statique des pays et des villes
(le contenu lu sans JavaScript, et par les moteurs) sont tirés de site/data/finder/, que produit make_gazetteer.py :
relancer celui-ci d'abord quand les listes changent. Rendu par article_template.render() (en-tête, pied, JSON-LD,
hreflang, OG) ; l'outil de recherche est placé juste après l'introduction, avant « L'essentiel » et le sommaire.

Usage : ONLY=/trouver-un-centre/,/en/test-centre-near-me/,/es/centro-de-examen-cerca-de-mi/,/ar/test-centre-near-me/ \\
        python3 _build/make_finder.py
"""
import glob
import hashlib
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from article_template import ROOT, build  # noqa: E402
from finder_pages import (CCI_CARTE, EXAM_LABEL, FEI_LISTE, GEONAMES, REGION_ORDER, REGIONS, TEXT,  # noqa: E402
                          centres_word, date_label)
from make_gazetteer import norm  # noqa: E402

FIND = os.path.join(ROOT, "data", "finder")
LANGS = ("fr", "en", "es", "ar")
LI = {"fr": 0, "en": 1, "es": 2, "ar": 3}
EXAMS = ("tcf", "delf", "civique", "tef")
FEI_TYPE = {"tcf": "tcf", "delf": "delf_dalf", "civique": "examen_civique"}
MARK = "<!-- /finder -->"
esc = lambda s: html.escape(s, quote=True)


class Safe(dict):
    def __missing__(self, k):
        return "{" + k + "}"


def load():
    ix = json.load(open(os.path.join(FIND, "index.json"), encoding="utf-8"))
    files = {os.path.basename(f)[:-5]: json.load(open(f, encoding="utf-8")) for f in glob.glob(os.path.join(FIND, "c", "*.json"))}
    v = hashlib.sha1(open(os.path.join(FIND, "index.json"), "rb").read()).hexdigest()[:10]
    return ix, files, v


def numbers(ix, files, lang):
    cs = [c for f in files.values() for c in f["c"]]
    per = {e: sum(1 for c in cs if e in c["x"].split(",")) for e in EXAMS}
    fei_dates = [ix["D"][e][1] for e in ("tcf", "delf", "tef") if e in ix["D"]]
    fmt = (lambda n: f"{n:,}".replace(",", " ")) if lang == "fr" else (lambda n: f"{n:,}") if lang == "en" else str
    return Safe(n=fmt(len(cs)), p=len(files), tcf=fmt(per["tcf"]), delf=fmt(per["delf"]), civ=fmt(per["civique"]), tef=fmt(per["tef"]),
                cities=fmt(sum(1 for r in ix["r"] if any(int(x) for x in str(r[4]).split(",") if x))),
                date=date_label(max(fei_dates), lang), date_civ=date_label(ix["D"].get("civique", ["2026-09-19"])[0], lang),
                geonames=GEONAMES, fei=FEI_LISTE, cci=CCI_CARTE)


def tool(lang, T, ix, v):
    chips = "\n".join(
        f'<label><input type="radio" name="exam" value="{e}"{" checked" if e == "all" else ""}><span>{esc(T["all"] if e == "all" else T["ex"][e])}</span></label>'
        for e in ("all",) + tuple(x for x in EXAMS if x in ix["x"]))
    return f"""<section class="finder" id="finder" data-v="{v}" aria-labelledby="finder-title">
<h2 id="finder-title">{T['tool_h2']}</h2>
<form class="finder-form" action="{T['path']}" method="get" role="search" autocomplete="off">
<label class="finder-label" for="finder-q">{T['label']}</label>
<div class="finder-row">
<div class="finder-field">
<input id="finder-q" name="q" type="search" placeholder="{esc(T['ph'])}" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="finder-list" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="search">
<ul id="finder-list" class="finder-list" role="listbox" aria-label="{esc(T['label'])}" hidden></ul>
</div>
<button type="submit">{T['go']}</button>
</div>
<div class="finder-tools">
<fieldset class="finder-exams"><legend class="finder-vh">{T['legend']}</legend>
{chips}
</fieldset>
<button type="button" class="finder-near" id="finder-near" hidden>{T['near']}</button>
</div>
<p class="finder-privacy" hidden>{T['privacy']}</p>
</form>
<p class="finder-status" id="finder-status" role="status" aria-live="polite"></p>
<div class="finder-results" id="finder-results"></div>
<noscript><p class="finder-privacy">{T['noscript']}</p></noscript>
<p class="finder-note">{T['note'].format_map(Safe(geonames=GEONAMES))}</p>
</section>
<script src="/js/finder.js" defer></script>
{MARK}"""


def pick_url(rec, lang):
    """rec = [examen, portée, fr, en, es, ar] → (chemin, langue) dans la langue de la page, sinon fr, en, es."""
    for l in (lang, "fr", "en", "es", "ar"):
        u = rec[2 + LI[l]]
        if u:
            return u, l
    return None, None


def link(url, l, lang, text):
    extra = f' hreflang="{l}"' if l != lang else ""
    return f'<a href="{esc(url)}"{extra}>{text}</a>'


def static_list(lang, T, ix, files):
    """Tous les pays et toutes les villes, par grande région : le contenu de la page sans JavaScript."""
    ar = lang == "ar"
    iso = (lambda s: f"<bdi>{s}</bdi>") if ar else (lambda s: s)
    rows = ix["r"]
    by_country = {}
    for i, r in enumerate(rows):
        by_country.setdefault(r[3], []).append(i)
    cname = lambda cc: ix["C"].get(cc, [cc] * 4)[LI[lang]]
    out = []
    for reg in REGION_ORDER[lang]:
        ccs = sorted((cc for cc in files if ix["g"].get(cc) == reg), key=lambda cc: norm(cname(cc)))
        if not ccs:
            continue
        out.append(f'<h3 id="region-{reg.replace("_", "-")}">{REGIONS[lang][reg]} <span class="count">({len(ccs)})</span></h3>')
        for cc in ccs:
            f = files[cc]
            n = len(f["c"])
            per = {e: sum(1 for c in f["c"] if e in c["x"].split(",")) for e in EXAMS}
            # villes : nombre de centres, lien vers notre page de ville quand elle existe
            city_n, city_link = {}, {}
            for c in f["c"]:
                city_n[c["r"]] = city_n.get(c["r"], 0) + 1
                for gi in c.get("g", []):
                    rec = f["L"][gi]
                    if rec[1] == "c" and c["r"] not in city_link:
                        u, l = pick_url(rec, lang)
                        if u:
                            city_link[c["r"]] = (u, l)
            names = lambda ri: (rows[ri][0].split("|") + ["", "", ""])[:4]
            shown = lambda ri: (names(ri)[LI[lang]] or (names(ri)[1] if lang == "ar" else "") or names(ri)[0]) + \
                (f" ({cname(rows[ri][6][1:]) if rows[ri][6].startswith('@') else rows[ri][6]})" if len(rows[ri]) > 6 else "")
            order = sorted(city_n, key=lambda ri: (-city_n[ri], norm(shown(ri))))
            def city_html(ri):
                t = iso(esc(shown(ri)))
                if ri in city_link:
                    t = link(*city_link[ri], lang, t)
                return f"{t} ({city_n[ri]})"
            cities = " · ".join(city_html(ri) for ri in order)
            ours = []
            for e in EXAMS:
                recs = [rec for rec in f["L"] if rec[0] == e and rec[1] == "p"]
                if recs:
                    u, l = pick_url(recs[0], lang)
                    if u:
                        ours.append(link(u, l, lang, EXAM_LABEL[lang][e]))
            official = []
            for e in ("tcf", "delf", "civique"):
                if per[e]:
                    u = FEI_LISTE + (f"?pays={ix['f'][cc]}&amp;type-centre={FEI_TYPE[e]}" if ix["f"].get(cc) else "")
                    official.append(f'<a href="{u}" rel="noopener">FEI · {EXAM_LABEL[lang][e]}</a>')
            if per["tef"]:
                official.append(f'<a href="{CCI_CARTE}" rel="noopener">CCI · TEF</a>')
            ex = " · ".join(f"{EXAM_LABEL[lang][e]} {per[e]}" for e in EXAMS if per[e])
            links = (f"{T['ours']} : " if lang == "fr" else f"{T['ours']}: ") + " · ".join(ours) + " — " if ours else ""
            links += (f"{T['official']} : " if lang == "fr" else f"{T['official']}: ") + " · ".join(official)
            out.append(f"""<details class="finder-country"><summary>{esc(cname(cc))} <span class="count">— {centres_word(n, lang)}</span></summary>
<p class="finder-ex">{ex}</p>
<p class="finder-cities">{cities}</p>
<p class="finder-links">{links}</p>
</details>""")
    return "\n".join(out)


def article(lang, ix, files, v):
    T = TEXT[lang]
    vals = numbers(ix, files, lang)
    fmt = lambda s: s.format_map(vals)
    sections = "\n\n".join(f'<h2 id="{sid}">{title}</h2>\n{body}' for sid, title, body in T["sections"])
    list_id = {"fr": "pays", "en": "countries", "es": "paises", "ar": "countries"}[lang]
    body = f"""
{tool(lang, T, ix, v)}

{sections}

<h2 id="{list_id}">{T['list_h2']}</h2>
<p>{fmt(T['list_intro'])}</p>
<div class="finder-static">
{static_list(lang, T, ix, files)}
</div>
"""
    date_iso = max(ix["D"][e][1] for e in ("tcf", "delf", "tef") if e in ix["D"])
    a = dict(
        section="", slug=T["path"].strip("/"), accent="accent-delf", crumb=T["crumb"],
        title=fmt(T["title"]), desc=fmt(T["desc"]), h1=T["h1"],
        published="2026-10-26", modified=date_iso, date_fr=date_label(date_iso, lang), read=4,
        intro=fmt(T["intro"]), facts=[fmt(f) for f in T["facts"]],
        toc=[(sid, re.sub(r"<[^>]+>", "", t)) for sid, t, _ in T["sections"]] + [(list_id, T["list_h2"])],
        body=body, cta_h2=T["cta_h2"], cta_p=T["cta_p"],
        faq=[(fmt(q), fmt(r)) for q, r in T["faq"]], also=T["also"], sources=fmt(T["sources"]),
        og_slug="trouver-un-centre" if lang == "fr" else f"{lang}-{T['path'].strip('/').split('/')[-1]}",
    )
    if lang != "fr":
        from i18n_registry import alternates_for
        alts, links = alternates_for(TEXT["fr"]["path"], current=lang)
        a.update(lang=lang, crumbs=[T["home"]], alternates=alts, lang_links=links)
    assert len(a["title"]) <= 60, (lang, len(a["title"]), a["title"])
    assert len(html.unescape(a["desc"])) <= 155, (lang, len(a["desc"]), a["desc"])
    return a


def place_tool_first(path):
    """Déplace « L'essentiel » et le sommaire après l'outil : la recherche suit directement l'introduction."""
    f = os.path.join(ROOT, path.strip("/"), "index.html")
    s = open(f, encoding="utf-8").read()
    m = re.search(r'\n<div class="facts">.*?</details>\n', s, re.S)
    if not m or MARK not in s or s.index(MARK) < m.start():
        return
    block = m.group(0)
    s = s[:m.start()] + "\n" + s[m.end():]
    s = s.replace(MARK, MARK + "\n" + block.strip("\n") + "\n", 1)
    open(f, "w", encoding="utf-8").write(s)


def main():
    ix, files, v = load()
    arts = [article(l, ix, files, v) for l in LANGS]
    build(arts, overwrite="--force" in sys.argv)
    only = [p for p in os.environ.get("ONLY", "").split(",") if p]
    for l in LANGS:
        path = TEXT[l]["path"]
        if not only or any(p in path for p in only):
            place_tool_first(path)


if __name__ == "__main__":
    main()
