#!/usr/bin/env python3
"""Contrôle des pages traduites (/es/, /en/ — 08/10/2026), sur le site généré.

Pour chaque paire page française ↔ traduction (fr_path des specs de pays_config_es / pays_config_en) :
- parité des faits : chaque nombre de la partie rédigée française (intro, faits, chiffres, sections, FAQ)
  doit se retrouver dans la traduction, séparateurs de milliers normalisés et mois des dates jj/mm
  ignorés. C'est la garde contre un prix ou une date mis à jour d'un seul côté ; les écarts de forme
  (« 1er » → « first ») se relisent et se tolèrent ;
- hreflang : alternates réciproques, cibles existantes ;
- restes de français dans le texte espagnol ou anglais (mots-outils ; avertissement à relire) ;
- titre ≤ 60, description ≤ 155.

Usage : python3 _build/check_i18n.py [--strict]   (--strict : les écarts de parité comptent comme erreurs)
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
BASE = "https://delf-tcf-tef.fr"
sys.path.insert(0, HERE)

FR_WORDS = {
    "es": {"et", "ou", "avec", "pour", "dans", "des", "du", "aux", "au", "est", "sont", "une", "qui", "pas", "selon",
           "aussi", "chaque", "depuis", "jusqu'au", "jusqu'à", "après", "leur", "leurs", "centre", "centres", "agréé",
           "agréés", "relevé", "inscription", "sessions", "tarif", "prix", "dates", "mois", "jours", "semaines"},
    "en": {"le", "les", "des", "du", "aux", "au", "et", "ou", "avec", "pour", "dans", "sur", "est", "sont", "une", "qui",
           "que", "pas", "selon", "aussi", "chaque", "depuis", "après", "leur", "leurs", "agréé", "agréés", "relevé",
           "tarif", "prix", "mois", "jours", "semaines"},
}
# Noms propres qui contiennent des mots-outils français : retirés avant la recherche des restes.
NAMES = re.compile(r"(Alliance [Ff]ran[çc]aise|Institut [Ff]ran[çc]ais|Lyc[ée]e|Coll[èe]ge|C[ée]gep|Universit[ée]|"
                   r"L'Alliance|Centre|École|Maison|France [ÉE]ducation|Le français des affaires|Le français au|(?:Bureau|Service) de [Cc]oop[ée]ration)[^,.;:()<«»“”]*")


def path_file(p):
    return os.path.join(ROOT, p.strip("/"), "index.html")


def read(p):
    with open(path_file(p), encoding="utf-8") as fh:
        return fh.read()


def editorial(h):
    """La partie rédigée : de l'intro à « À lire aussi », sans les cartes des centres (données FEI)."""
    a = h.find('<p class="intro">')
    g = h.find('<h2 id="a-lire">')
    part = h[a:g if g > 0 else len(h)]
    return re.sub(r'<div class="card centre">.*?</div>', " ", part, flags=re.S)


def text(h):
    t = re.sub(r"<sup>(er|re|e)</sup>", "", h)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def numbers(t):
    t = re.sub(r"\b(\d{1,2})/(\d{1,2})(/\d{4})?\b", lambda m: m.group(1) + (" " + m.group(3)[1:] if m.group(3) else ""), t)
    out = set()
    # (?<!\w) : « B2 190 $ » ou « A1 135 » ne se lisent pas 2 190 ni 1 135 — un niveau n'est pas un nombre
    for m in re.finditer(r"(?<!\w)(?:\d{1,3}(?:[   .,]\d{3})+(?!\d)|\d+)", t):
        out.add(re.sub(r"\D", "", m.group(0)).lstrip("0") or "0")
    return out


def alternates(h):
    return re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">', h)


def pairs():
    import pays_config_en
    import pays_config_es
    out = []
    for p in pays_config_es.PAGES + pays_config_en.PAGES:
        out.append((p["fr_path"], f"/{p['lang']}/{p['slug']}/", p["lang"]))
    return out


def main():
    strict = "--strict" in sys.argv
    errors, warns = [], []
    for fr, tr, lang in pairs():
        if not os.path.exists(path_file(tr)):
            errors.append(f"{tr} : page absente (make_pays.py --force)")
            continue
        hf, ht = read(fr), read(tr)
        # Parité des nombres
        miss = sorted(numbers(text(editorial(hf))) - numbers(text(editorial(ht))), key=lambda x: (len(x), x))
        if miss:
            (errors if strict else warns).append(f"{tr} : nombres du français absents de la traduction : {', '.join(miss)}")
        # hreflang réciproques
        for src, h in ((fr, hf), (tr, ht)):
            alts = alternates(h)
            if not alts:
                errors.append(f"{src} : aucune balise hreflang")
            for lang_code, href in alts:
                p = href.replace(BASE, "")
                if not os.path.exists(path_file(p)):
                    errors.append(f"{src} : hreflang {lang_code} → {p} n'existe pas")
                elif BASE + src not in [u for _, u in alternates(read(p))]:
                    errors.append(f"{src} : {p} ne la déclare pas en retour")
        # Titre, description
        t = html.unescape(re.search(r"<title>(.*?)</title>", ht).group(1))
        d = html.unescape(re.search(r'<meta name="description" content="(.*?)">', ht).group(1))
        if len(t) > 60:
            errors.append(f"{tr} : titre de {len(t)} caractères")
        if len(d) > 155:
            errors.append(f"{tr} : description de {len(d)} caractères")
        # Restes de français
        body = NAMES.sub(" ", text(editorial(ht)))
        hits = []
        for m in re.finditer(r"[A-Za-zÀ-ÿ']+", body):
            w = m.group(0).lower()
            if w in FR_WORDS[lang]:
                hits.append(body[max(0, m.start() - 30):m.end() + 30])
        if hits:
            warns.append(f"{tr} : {len(hits)} mot(s) français possibles — " + " | ".join(hits[:4]))
        if "{" in text(re.sub(r"<script.*?</script>", "", ht, flags=re.S)):
            errors.append(f"{tr} : accolade restée dans le texte (format non appliqué ?)")
    for w in warns:
        print("  ~ " + w)
    for e in errors:
        print("  ✗ " + e)
    n = len(pairs())
    print(f"{n} paires contrôlées — {len(errors)} erreur(s), {len(warns)} avertissement(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
