#!/usr/bin/env python3
"""Données du chercheur de centres (26/10/2026) : gazetier GeoNames + index des centres d'examen.

Entrées
  - GeoNames (CC BY 4.0), téléchargé à part dans un dossier vide et lu comme une donnée : cities1000 (.txt ou
    .zip), alternateNamesV2 (.txt ou .zip, noms étiquetés par langue), admin1CodesASCII.txt, countryInfo.txt.
    Lancer en mode isolé, chemins en arguments :
        python3 -I _build/make_gazetteer.py <cities1000.zip> <alternateNamesV2.zip> <admin1CodesASCII.txt> <countryInfo.txt>
  - les centres : _build/data/fei_monde/<type>_<pays>.json quand ils existent (liste FEI mondiale), sinon les
    fichiers historiques _build/data/<tcf|delf|civique>_<pays>.json ; _build/data/tef_monde/*.json si présent.
  - les noms de pays fr/en/es/ar : _build/data/country_names.json (swift _build/country_names.swift).
  - les pages du site (liens « Notre guide ») : make_centres.PAGES, villes_config.VILLES, pays_config*.py et le
    registre des traductions (i18n_registry) — une page n'est liée que si son index.html existe.

Sorties (écrasées à chaque passage, jamais retouchées à la main)
  - site/data/geo/<clé>.json : gazetier découpé par les premiers caractères du nom normalisé (2, plus si le
    morceau dépasse 80 Ko) ; une ligne = [noms|…, lat, lon, iso2, population en milliers, noms affichés
    fr|en|es|ar (vide = premier nom), région admin1 si le nom existe deux fois dans le pays].
  - site/data/finder/index.json : une ligne par ville de centres, les pays, les clés du gazetier, la date.
  - site/data/finder/names.json : noms des centres → ligne de ville (recherche par nom de centre).
  - site/data/finder/c/<ISO2>.json : les fiches complètes d'un pays (chargées à la demande).
  - --report <fichier> : les centres que le géocodage n'a pas placés (cherchables par texte, sans distance).

La normalisation (norm) est la même, caractère pour caractère, que celle de js/finder.js.
"""
import glob
import html
import io
import json
import math
import os
import re
import sys
import unicodedata
import zipfile
from collections import Counter, OrderedDict, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)          # en mode -I, seuls nos propres modules (jamais le dossier des téléchargements)
ROOT = os.path.normpath(os.path.join(HERE, ".."))
DATA = os.path.join(HERE, "data")
OUT_GEO = os.path.join(ROOT, "data", "geo")
OUT_FIND = os.path.join(ROOT, "data", "finder")

POP_MIN = 5000                    # villes du gazetier ; les villes des centres y entrent quelle que soit leur taille
SHARD_MAX = 80_000                # octets par morceau
LANGS = ("fr", "en", "es", "ar")
EXAMS = ("tcf", "delf", "civique", "tef")

# Domaines à ne jamais lier (SEO_ANALYSE_ET_PLAN_2026-10-26, règle 8) : site retiré, adresse et e-mail compris.
BLOCKED = ("if-algerie.fr", "afcartagena.org", "lalliance.org", "afla.org", "afpasadena.org", "afsd.org",
           "afgirona.org", "alianzafrancesapalma.com", "alianzafrancesa.org.co", "ambafrance-mx.org", "if-uae.com",
           "tcfcad.com")


# ---------------------------------------------------------------------------
# Normalisation (identique à js/finder.js)
# ---------------------------------------------------------------------------
FOLD = {"ø": "o", "đ": "d", "ł": "l", "æ": "ae", "œ": "oe", "ı": "i", "ß": "ss", "ð": "d", "þ": "th", "ħ": "h",
        "ŀ": "l", "ŧ": "t", "ĸ": "k", "ŋ": "n",
        "ٱ": "ا", "ة": "ه", "ى": "ي", "ی": "ي", "ک": "ك", "ـ": ""}
for _i in range(10):
    FOLD[chr(0x660 + _i)] = str(_i)
    FOLD[chr(0x6F0 + _i)] = str(_i)
APOS = "'’ʼ`´ʻ‘"
SPACE_RX = re.compile(r"[^\w]+|_", re.U)


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.category(c).startswith("M"))
    s = unicodedata.normalize("NFC", s).lower()
    s = "".join(FOLD.get(c, c) for c in s)
    s = "".join(c for c in s if c not in APOS)
    s = SPACE_RX.sub(" ", s).strip()
    toks = s.split()
    for i, t in enumerate(toks[:-1]):          # « st » / « ste » suivis d'un autre mot : saint / sainte
        if t == "st":
            toks[i] = "saint"
        elif t == "ste":
            toks[i] = "sainte"
    return " ".join(toks)


def fname(key):
    """Clé de morceau → nom de fichier ASCII (lettres et chiffres gardés, le reste en _hex)."""
    return "".join(c if ("a" <= c <= "z" or "0" <= c <= "9") else f"_{ord(c):x}" for c in key)


def dl(a, b, k):
    """Distance de Damerau-Levenshtein (transpositions adjacentes), ou k+1 dès qu'elle dépasse k."""
    la, lb = len(a), len(b)
    if abs(la - lb) > k:
        return k + 1
    prev2, prev = None, list(range(lb + 1))
    for i in range(1, la + 1):
        cur = [i] + [0] * lb
        best = cur[0]
        for j in range(1, lb + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            v = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost)
            if i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                v = min(v, prev2[j - 2] + 1)
            cur[j] = v
            best = min(best, v)
        if best > k:
            return k + 1
        prev2, prev = prev, cur
    return prev[lb]


def tol(n):
    return 0 if n < 4 else 1 if n < 8 else 2


# ---------------------------------------------------------------------------
# Écritures
# ---------------------------------------------------------------------------
ARABIC_OK = re.compile(r"^[ء-غف-يً-ٰٟٱـ \-'()]+$")
LATIN_OK = re.compile(r"^[A-Za-zÀ-ɏḀ-ỿ][A-Za-zÀ-ɏḀ-ỿ̀-ͯ' ’.\-]*$")
CJK = re.compile(r"^[぀-ヿ㐀-鿿가-힯]+$")


def script(n):
    if LATIN_OK.match(n):
        return "latn"
    if ARABIC_OK.match(n):
        return "arab"
    if CJK.match(n):
        return "cjk"
    return None


# ---------------------------------------------------------------------------
# GeoNames
# ---------------------------------------------------------------------------
def open_text(path, inner=None):
    if path.endswith(".zip"):
        z = zipfile.ZipFile(path)
        name = inner or next(n for n in z.namelist() if n.endswith(".txt") and "iso-language" not in n)
        return io.TextIOWrapper(z.open(name), encoding="utf-8")
    return open(path, encoding="utf-8")


def classify(paths):
    out = {}
    for p in paths:
        b = os.path.basename(p).lower()
        if b.startswith("cities"):
            out["cities"] = p
        elif b.startswith("alternatenames"):
            out["alt"] = p
        elif b.startswith("admin1"):
            out["admin1"] = p
        elif b.startswith("countryinfo"):
            out["countries"] = p
    missing = {"cities", "alt", "admin1", "countries"} - set(out)
    if missing:
        raise SystemExit(f"fichiers GeoNames manquants : {sorted(missing)}")
    return out


SKIP_FCODE = {"PPLH", "PPLQ", "PPLW", "PPLCH"}


def read_cities(path):
    cities = {}
    with open_text(path) as fh:
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) < 19 or f[7] in SKIP_FCODE:
                continue
            gid = int(f[0])
            cities[gid] = dict(gid=gid, name=f[1], ascii=f[2], alts=[a for a in f[3].split(",") if a],
                               lat=float(f[4]), lon=float(f[5]), fcode=f[7], cc=f[8], a1=f[10], a2=f[11],
                               pop=int(f[14] or 0), tags=defaultdict(list))
    return cities


def read_countries(path):
    info = {}
    with open_text(path) as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            f = line.rstrip("\n").split("\t")
            langs = {l.split("-")[0] for l in f[15].split(",") if l}
            info[f[0]] = dict(name=f[4], continent=f[8], phone=re.sub(r"\D", "", f[12].split(" and ")[0]), langs=langs)
    return info


def read_admin1(path):
    out = {}
    with open_text(path) as fh:
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) >= 3:
                out[f[0]] = f[2] or f[1]
    return out


TAG_LANGS = {"fr", "en", "es", "ar", "de", "it", "pt", "nl", "ca", "eu", "gl", "zh", "ja", "ko"}


def read_alternates(path, cities, countries):
    off = {cc: v["langs"] for cc, v in countries.items()}
    n = 0
    with open_text(path, "alternateNamesV2.txt") as fh:
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) < 4:
                continue
            gid = int(f[1])
            c = cities.get(gid)
            if c is None:
                continue
            lang = f[2]
            if not lang or (lang not in TAG_LANGS and lang not in off.get(c["cc"], ())):
                continue
            hist = len(f) > 7 and f[7] == "1"
            colloq = len(f) > 6 and f[6] == "1"
            if hist:
                continue
            pref = len(f) > 4 and f[4] == "1"
            short = len(f) > 5 and f[5] == "1"
            c["tags"][lang].append((f[3], pref, short, colloq))
            n += 1
    return n


def display_names(c):
    """Nom affiché par langue : nom préféré de la langue, sinon le premier nom courant, sinon le nom GeoNames."""
    out = []
    for l in LANGS:
        cand = [t for t in c["tags"].get(l, []) if not t[3] and script(t[0]) == ("arab" if l == "ar" else "latn")
                and len(t[0]) >= 3]
        # GeoNames marque parfois « Dubai City » ou « إمارة الشارقة » comme préférés : le nom court d'abord, puis le
        # nom principal s'il est étiqueté dans la langue, puis le préféré, puis le plus court.
        main = [t for t in cand if t[0] == c["name"]]
        pick = ([t for t in cand if t[2] and t[1]] or [t for t in cand if t[2]] or main
                or [t for t in cand if t[1]] or sorted(cand, key=lambda t: len(t[0])))
        out.append(pick[0][0] if pick else ("" if l == "ar" else c["name"]))
    return out                              # arabe vide : finder.js affiche le nom anglais, isolé


NOISE = re.compile(r"^(Lungsod ng|Cathair|Bandar ?[Rr]aya|Kota|Jiji la|Thanh pho|Thành phố|Altepetl|Siudad ti|Ciutat de|"
                   r"Città di|Comune di|Municipio|Gemeente|Stad|City of|Ville de|Mdynt|Byen)\b")


def search_names(c, countries, big, centre=False):
    """Noms cherchables d'une ville : (forme originale, norm) dédoublonnés, plafonnés par écriture."""
    seen, out = [], []

    def add(n, cap_kind):
        n = n.strip()
        if not n or len(n) > 40 or " - " in n or (not cap_kind and NOISE.match(n)):
            return
        k = script(n)
        if k is None or (k == "cjk" and not big):
            return
        nn = norm(n)
        if len(nn) < 2 or nn in seen:
            return
        if k == "latn" and len(nn) >= 6 and any(len(s) >= 6 and dl(nn, s, 1) <= 1 for s in seen):
            return                          # variante à une lettre près : la tolérance aux fautes la couvre
        pop = c["pop"]
        caps = {"latn": 12 if big else 8 if pop >= 100_000 else 5 if (pop >= 20_000 or centre) else 3,
                "arab": 3 if big else 2, "cjk": 2}
        if sum(1 for _, _, kk in out if kk == k) >= caps[k]:
            return
        seen.append(nn)
        out.append((n, nn, k))

    add(c["name"], "")
    add(c["ascii"], "")
    for l in LANGS:
        tags = sorted(c["tags"].get(l, []), key=lambda t: (not t[1], t[2], t[3]))
        for t in tags:
            add(t[0], l)
    off = countries.get(c["cc"], {}).get("langs", set())
    for l in sorted(set(c["tags"]) - set(LANGS)):
        if l in off or l in {"de", "it", "pt", "nl", "ca"} or (big and l in {"zh", "ja", "ko"}):
            for t in sorted(c["tags"][l], key=lambda t: (not t[1], t[2])):
                add(t[0], l)
    if c["pop"] < 20_000 and not centre:
        return out                          # petite ville : noms étiquetés seulement
    for a in c["alts"]:                    # noms non étiquetés : seulement ceux qui ont une majuscule (les
        if a[:1].isupper() and not re.match(r"^[A-Z]{2,4}$", a):   # translittérations en minuscules et les codes
            add(a, "")                     # d'aéroport sont écartés)
    for a in c["alts"]:
        if script(a) in ("arab", "cjk"):
            add(a, "")
    return out


# ---------------------------------------------------------------------------
# Centres
# ---------------------------------------------------------------------------
NAME_FIX = {"CN": {"fr": "Chine", "en": "China", "es": "China", "ar": "الصين"},
            "CD": {"fr": "République démocratique du Congo", "en": "Democratic Republic of the Congo",
                   "es": "República Democrática del Congo", "ar": "جمهورية الكونغو الديمقراطية"},
            "CG": {"fr": "République du Congo", "en": "Republic of the Congo", "es": "República del Congo", "ar": "جمهورية الكونغو"},
            "CI": {"es": "Costa de Marfil"}, "VA": {"fr": "Vatican"}, "MF": {"en": "Saint Martin"},
            "BL": {"en": "Saint Barthélemy"}, "PS": {"fr": "Palestine", "en": "Palestine", "es": "Palestina", "ar": "فلسطين"}}


def country_table():
    names = json.load(open(os.path.join(DATA, "country_names.json"), encoding="utf-8"))
    for cc, fix in NAME_FIX.items():         # noms de Foundation trop administratifs (« Chine continentale »)
        if cc in names:
            names[cc] = dict(names[cc], **fix)
    by_norm = {}
    for cc, d in names.items():
        for v in d.values():
            by_norm.setdefault(norm(v), cc)
    for k, cc in {"Republique democratique du Congo": "CD", "RDC": "CD", "Congo": "CG", "Congo Brazzaville": "CG",
                  "Etats Unis": "US", "USA": "US", "Royaume Uni": "GB", "UK": "GB", "Emirats arabes unis": "AE",
                  "EAU": "AE", "UAE": "AE", "Coree du Sud": "KR", "Coree": "KR", "Maurice": "MU", "Ile Maurice": "MU",
                  "Haiti": "HT", "Cote d Ivoire": "CI", "Cote dIvoire": "CI", "Ivory Coast": "CI", "Hong Kong": "HK",
                  "Taiwan": "TW", "Macedoine du Nord": "MK", "Republique tcheque": "CZ", "Tchequie": "CZ",
                  "Turquie": "TR", "Turkiye": "TR", "Palestine": "PS", "Territoires palestiniens": "PS",
                  "Birmanie": "MM", "Myanmar": "MM", "Vatican": "VA", "Saint Siege": "VA", "Cap Vert": "CV",
                  "Russie": "RU", "Swaziland": "SZ", "Eswatini": "SZ", "Laos": "LA", "Syrie": "SY", "Iran": "IR",
                  "Vietnam": "VN", "Viet Nam": "VN", "Bolivie": "BO", "Venezuela": "VE", "Moldavie": "MD",
                  "Kosovo": "XK", "Angleterre": "GB", "Grande Bretagne": "GB", "Amerique": "US"}.items():
        by_norm[norm(k)] = cc
    return names, by_norm


# Aliases cherchables des pays (en plus des quatre noms localisés).
COUNTRY_ALIASES = {"US": ["USA", "US", "America", "Amérique", "EEUU", "EE UU", "Estados Unidos de America"],
                   "GB": ["UK", "Angleterre", "England", "Inglaterra", "Grande-Bretagne", "Great Britain", "Scotland", "Écosse"],
                   "AE": ["UAE", "EAU", "Emirates", "Émirats", "Dubai"], "CD": ["RDC", "DRC", "République démocratique du Congo", "Democratic Republic of the Congo"],
                   "CG": ["Congo-Brazzaville", "Republic of the Congo"], "CI": ["Ivory Coast", "Costa de Marfil"],
                   "KR": ["Korea", "Corée", "Corea"], "MU": ["Île Maurice", "Mauritius"], "NL": ["Holland", "Hollande", "Holanda"],
                   "CZ": ["Tchéquie", "Czechia"], "TR": ["Türkiye", "Turkey"], "SA": ["KSA", "Saudi"], "MA": ["المغرب"],
                   "BE": ["Belgie", "België"], "CN": ["Chine continentale", "China mainland"], "CD": ["Congo-Kinshasa", "Congo Kinshasa"],
                   "CG": ["Congo", "Congo-Brazzaville"], "CH": ["Schweiz", "Svizzera"], "DE": ["Deutschland"]}


def exam_of(t):
    t = (t or "").lower()
    if t.startswith("tcf"):
        return "tcf"
    if t.startswith("delf") or "dalf" in t:
        return "delf"
    if "civi" in t:
        return "civique"
    if t.startswith("tef"):
        return "tef"
    return None


def file_date(d):
    return (d.get("date") or "")[:10]


def load_sources(by_norm):
    """[(iso2, exam, date, data, origin)] : fei_monde d'abord, les anciens fichiers pour le reste."""
    srcs, have = [], set()
    for sub, forced in (("fei_monde", None), ("tef_monde", "tef")):
        for f in sorted(glob.glob(os.path.join(DATA, sub, "*.json"))):
            if os.path.basename(f) in ("manifest.json",):
                continue
            try:
                d = json.load(open(f, encoding="utf-8"))
            except Exception:
                continue
            if not isinstance(d, dict) or not isinstance(d.get("centres"), list):
                continue
            ex = forced or exam_of(d.get("type") or os.path.basename(f))
            iso = (d.get("iso2") or "").upper() or by_norm.get(norm(d.get("country", "")))
            if not ex or not iso:
                print(f"  ! ignoré (type ou pays inconnu) : {sub}/{os.path.basename(f)}")
                continue
            srcs.append((iso, ex, file_date(d), d, f"{sub}/{os.path.basename(f)}"))
            have.add((iso, ex))
    best = {}
    for f in sorted(glob.glob(os.path.join(DATA, "*.json"))):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict) or "centres" not in d or "country" not in d:
            continue
        ex = exam_of(d.get("type") or os.path.basename(f))
        iso = by_norm.get(norm(d["country"]))
        if not ex or not iso:
            print(f"  ! ignoré (type ou pays inconnu) : {os.path.basename(f)}")
            continue
        if (iso, ex) in have:
            continue
        v2 = any("address_lines" in c for c in d["centres"])
        rank = (file_date(d), v2, len(d["centres"]))
        if (iso, ex) not in best or rank > best[(iso, ex)][0]:
            best[(iso, ex)] = (rank, d, os.path.basename(f))
    for (iso, ex), (rank, d, name) in sorted(best.items()):
        srcs.append((iso, ex, rank[0], d, name))
    return srcs


def host(u):
    return re.sub(r"^https?://(www\.)?", "", u.strip().lower()).split("/")[0].split(":")[0]


def blocked(h):
    return any(h == b or h.endswith("." + b) for b in BLOCKED)


_FEI = None


def personal(e):
    """Adresse e-mail personnelle (prénom.nom) ou refusée par parse_fei_v2 : jamais publiée."""
    global _FEI
    if _FEI is None:
        from data import parse_fei_v2 as _m
        _FEI = _m
    ALLOW, DENY, GENERIC = _FEI.ALLOW, _FEI.DENY, _FEI.GENERIC
    e = e.strip().lower()
    if e in ALLOW:
        return False
    if e in DENY:
        return True
    local = e.split("@")[0]
    return bool(re.match(r"^[a-z]+[._][a-z]+\d*$", local) and not GENERIC.search(local))


CEDEX = re.compile(r"[\s-]*cedex(?:\b|\d).*$", re.I)
# Codes postaux des États-Unis : trois premiers chiffres → État (code admin1 de GeoNames)
_ZIP = [(5, 5, "NY"), (6, 9, "PR"), (10, 27, "MA"), (28, 29, "RI"), (30, 38, "NH"), (39, 49, "ME"), (50, 54, "VT"),
        (55, 55, "MA"), (56, 59, "VT"), (60, 69, "CT"), (70, 89, "NJ"), (100, 149, "NY"), (150, 196, "PA"),
        (197, 199, "DE"), (200, 205, "DC"), (206, 219, "MD"), (220, 246, "VA"), (247, 268, "WV"), (270, 289, "NC"),
        (290, 299, "SC"), (300, 319, "GA"), (320, 349, "FL"), (350, 369, "AL"), (370, 385, "TN"), (386, 397, "MS"),
        (398, 399, "GA"), (400, 427, "KY"), (430, 458, "OH"), (460, 479, "IN"), (480, 499, "MI"), (500, 528, "IA"),
        (530, 549, "WI"), (550, 567, "MN"), (570, 577, "SD"), (580, 588, "ND"), (590, 599, "MT"), (600, 629, "IL"),
        (630, 658, "MO"), (660, 679, "KS"), (680, 693, "NE"), (700, 714, "LA"), (716, 729, "AR"), (730, 749, "OK"),
        (750, 799, "TX"), (800, 816, "CO"), (820, 831, "WY"), (832, 838, "ID"), (840, 847, "UT"), (850, 865, "AZ"),
        (870, 884, "NM"), (885, 885, "TX"), (889, 898, "NV"), (900, 961, "CA"), (967, 968, "HI"), (970, 979, "OR"),
        (980, 994, "WA"), (995, 999, "AK")]


def us_state(zip5):
    z = int(zip5[:3])
    return next((st for a, b, st in _ZIP if a <= z <= b), None)


OVERSEAS = {"971": "GP", "972": "MQ", "973": "GF", "974": "RE", "975": "PM", "976": "YT", "977": "BL", "978": "MF",
            "986": "WF", "987": "PF", "988": "NC"}
RELATED = {"FR": ["GP", "MQ", "GF", "RE", "YT", "PM", "NC", "PF", "WF", "BL", "MF"], "CN": ["HK", "MO"], "RS": ["XK"],
           "GB": ["JE", "GG", "IM"], "US": ["PR", "VI", "GU"], "NL": ["CW", "AW", "SX", "BQ"], "DK": ["GL", "FO"]}
CA_PROV = {"quebec": "10", "ontario": "08", "colombie britannique": "02", "alberta": "01", "saskatchewan": "11",
           "manitoba": "03", "nouveau brunswick": "04", "nouvelle ecosse": "07", "terre neuve et labrador": "05",
           "nunavut": "14", "ile du prince edouard": "09", "yukon": "12", "territoires du nord ouest": "13"}
REGION_FR_EN = {"caroline du nord": "north carolina", "caroline du sud": "south carolina", "etat de washington": "washington",
                "etat de new york": "new york", "district de columbia": "washington, d.c.", "nouveau mexique": "new mexico",
                "virginie occidentale": "west virginia", "dakota du nord": "north dakota", "dakota du sud": "south dakota",
                "floride": "florida", "louisiane": "louisiana", "porto rico": "puerto rico"}


SMALL = {"de", "du", "des", "la", "le", "les", "et", "en", "d", "l", "y", "of", "the", "and", "a", "à", "au", "aux", "sur"}
SHORT_WORDS = {"bay", "leo", "san", "rio", "del", "los", "las", "mar", "sur", "new", "old", "sao", "rue", "ile", "ste",
               "art", "lab", "one", "top", "pro", "via", "est", "max", "box", "cap", "dar", "bel", "air", "mon", "sud", "the"}


def tidy_name(n):
    """Nom tout en capitales (liste CCI) → casse de titre ; les sigles de trois lettres et moins restent en capitales."""
    if not n.isupper() or len(n) < 5:
        return n
    def part(w, first):
        core = re.sub(r"[^\w]", "", w)
        m = re.match(r"^([dDlL])['’](.+)$", w)
        if m:                                # D'ALGÉRIE → d'Algérie
            return m.group(1).lower() + "'" + part(m.group(2), False)
        if core.lower() in SMALL and not first:
            return w.lower()
        if len(core) <= 3 and core.isalpha() and core.lower() not in SHORT_WORDS:
            return w                         # sigle : CCI, ABC, IFM
        return w[:1].upper() + w[1:].lower()

    def word(w, first):
        return "-".join(part(x, first and i == 0) for i, x in enumerate(w.split("-")))
    return " ".join(word(w, i == 0) for i, w in enumerate(n.split()))


def centre_rows(srcs, cnames):
    """Les centres, une entrée par fiche FEI, avec ville affichée (fr) et indices de géocodage."""
    import make_centres as MC
    import make_pays as MP
    rows = []
    fr_name = {cc: d["fr"] for cc, d in cnames.items()}
    for iso, ex, date, d, origin in srcs:
        country = d.get("country") or fr_name.get(iso, iso)
        cs = d["centres"]
        seen = set()
        for c in cs:
            k = (c.get("name", "").lower(), c.get("city", "").lower(), c.get("address", "").lower())
            if k in seen:
                continue
            seen.add(k)
            c = dict(c)
            c.setdefault("cp", "")
            c.setdefault("city_cp", "")
            v1 = "address_lines" not in c and "fei_id" not in c
            raw_city = c.get("city", "") or ""
            if v1:
                city = MC.clean_city(raw_city)
                addr = " ".join(x for x in [c.get("address", ""), (c["cp"] + " " + MC.clean_city(c["city_cp"])).strip()] if x).strip()
                addr = re.sub(r"\s+-\s*$", "", addr)
            else:
                try:
                    city = MP.city_of(c, country)
                except Exception:
                    city = re.sub(r"\s+", " ", raw_city).strip().rstrip(",")
                addr = c.get("address", "")
            curated = v1 or re.sub(r"\s+", " ", raw_city).strip().rstrip(",") in MP.CITY.get(country, {}) \
                or (country, c.get("name", "")) in MP.CITY_BY_NAME
            if "CARTE LISTE" in (c.get("address") or ""):
                continue                    # reste de la page FEI (liste des pays), pas un centre
            city = CEDEX.sub("", city).strip()
            if city.isupper():
                city = city.title()             # CCI : « AGEN BOE »
            hints = [h.strip() for h in re.findall(r"\(([^)]*)\)", raw_city)]
            geo_cc = [iso] + RELATED.get(iso, [])
            cp = c["cp"]
            if iso == "FR" and not cp:
                m = re.findall(r"\b((?:0[1-9]|[1-8]\d|9[0-8])\d{3})\b", c.get("address", ""))
                cp = m[-1] if m else ""             # le dernier : « CS 71003, 97743 Saint-Denis »
            if iso == "FR" and cp[:2] in ("97", "98"):
                first = {"97133": "BL", "97150": "MF"}.get(cp, OVERSEAS.get(cp[:3], "RE"))
                geo_cc = [first] + [x for x in RELATED["FR"] if x != first] + ["FR"]
            c["cp"] = cp
            rows.append(dict(iso=iso, exam=ex, date=date, country_fr=country, name=tidy_name(c.get("name", "").strip()),
                             city=city.strip() or raw_city.strip(), raw_city=raw_city, hints=hints, cp=c["cp"],
                             addr=re.sub(r"\s+", " ", addr).strip(), phone=c.get("phone", "") or "",
                             emails=[e for e in c.get("emails", []) or [] if "@" in e], url=(c.get("url") or "").strip().rstrip("﻿"),
                             so=bool(c.get("so")), fei_id=c.get("fei_id"), origin=origin, raw=c, v1=v1,
                             lat=c.get("lat"), lon=c.get("lon"), geo_cc=geo_cc, curated=curated and not v1,
                             products=c.get("products") or [], contact=c.get("contact") or "", cci_id=c.get("cci_id"),
                             v1_city=v1))
    return rows


# ---------------------------------------------------------------------------
# Géocodage : ville FEI → ville GeoNames du même pays
# ---------------------------------------------------------------------------
# Restes relus à la main (orthographes françaises de FEI, quartiers, villes rattachées).
ALIAS = {("FR", "saint denis de la reunion"): "saint denis", ("CA", "st john s nl"): "st john s",
         ("CA", "sept iles"): "sept iles", ("US", "detroit bingham farms"): "bingham farms",
         ("MX", "pachuca mineral de la reforma"): "pachuca", ("MX", "monterrey san pedro garza garcia"): "san pedro garza garcia",
         ("IN", "calcutta"): "kolkata", ("IN", "pondichery"): "puducherry", ("IN", "bombay"): "mumbai",
         ("IN", "madras"): "chennai", ("IN", "bangalore"): "bengaluru", ("IN", "new delhi"): "new delhi",
         ("GB", "saint helier jersey"): "saint helier", ("EG", "heliopolis"): "cairo", ("LB", "beyrouth"): "beirut",
         ("TN", "el mourouj"): "el mourouj", ("SA", "djeddah"): "jeddah", ("AE", "abou dhabi"): "abu dhabi",
         ("MA", "fes"): "fes", ("DZ", "alger"): "algiers", ("MA", "kenitra"): "kenitra",
         ("CD", "kinshasa gombe"): "kinshasa", ("CI", "abidjan cocody"): "abidjan",
         ("CA", "north york"): "toronto", ("MU", "rose hill"): 934765, ("AR", "bernal"): 3429652,
         ("US", "south freeport"): 4964867, ("SE", "jarfalla"): "jakobsberg", ("MY", "bandar baru bangi"): "bangi",
         ("MG", "nosy be"): "hell ville", ("MG", "sainte marie"): "ambodifotatra", ("VC", "north union"): 3577887,
         ("CN", "shandong province"): 1805753, ("FR", "bourgoin jallieu"): (45.586, 5.274),
         ("FR", "baie mahault pointe a pitre"): "baie mahault", ("FR", "saint martin"): "marigot", ("RU", "yakoutsk"): 2013159,
         ("LB", "deir el kamar"): (33.698, 35.561), ("CA", "columbia"): "new westminster", ("IT", "lancenigo tv"): "villorba", ("MY", "setiu"): 6862363, ("BR", "guanabara sp"): "campinas"}


class Geocoder:
    def __init__(self, cities, admin1):
        self.cities = cities
        self.by = defaultdict(list)
        self.by_cc = defaultdict(list)
        self.admin1 = admin1
        for gid, c in cities.items():
            names = {norm(c["name"]), norm(c["ascii"])}
            names |= {norm(a) for a in c["alts"]}
            for l, ts in c["tags"].items():
                names |= {norm(t[0]) for t in ts}
            names.discard("")
            c["_norms"] = names
            for n in names:
                self.by[(c["cc"], n)].append(gid)
            self.by_cc[c["cc"]].append(gid)

    def nearest(self, ll, ccs, radius=15):
        """La ville du pays la plus peuplée à moins de 15 km d'un point (centres TEF placés par la carte CCI)."""
        best = None
        for cc in ccs:
            for gid in self.by_cc.get(cc, []):
                c = self.cities[gid]
                if abs(c["lat"] - ll[0]) > 0.2 or abs(c["lon"] - ll[1]) > 0.3 or c["fcode"] == "PPLX":
                    continue
                if km(c["lat"], c["lon"], *ll) <= radius and (best is None or c["pop"] > best["pop"]):
                    best = c
            if best:
                return best
        return None

    def admin_ok(self, c, row):
        if row["iso"] == "US" and c["cc"] == "US":
            z = re.findall(r"\b(\d{5})(?:-\d{4})?\b", row["addr"])
            st = us_state(z[-1]) if z else None
            if st:
                return c["a1"] == st
        if row["iso"] == "CA" and row["hints"]:
            code = CA_PROV.get(norm(row["hints"][-1]))
            return code is None or c["a1"] == code
        if row["iso"] == "FR" and row["cp"][:2].isdigit() and row["cp"][:3] not in OVERSEAS:
            dep = row["cp"][:2]
            return not c["a2"] or c["a2"] == dep or c["cc"] != "FR"
        if row["hints"]:
            for h in row["hints"]:
                hn = norm(h)
                hn = REGION_FR_EN.get(hn, hn)
                a1 = norm(self.admin1.get(f"{c['cc']}.{c['a1']}", ""))
                if a1 and (a1 == hn or dl(a1, hn, 2) <= 2 or hn in a1):
                    return True
            return None                     # indice illisible : ni pour ni contre
        return None

    def pick(self, gids, row, n=""):
        if not gids:
            return None
        cands = [self.cities[g] for g in dict.fromkeys(gids)]
        ok = [c for c in cands if self.admin_ok(c, row) is True]
        not_bad = [c for c in cands if self.admin_ok(c, row) is not False]
        pool = ok or not_bad or cands
        # le nom principal d'abord (« New Delhi », pas Delhi dont c'est un autre nom), puis capitale, puis taille
        top = max(c["pop"] for c in pool)
        best = max(pool, key=lambda c: (n in (norm(c["name"]), norm(c["ascii"])) and c["pop"] * 100 >= top,
                                        c["fcode"] in ("PPLC", "PPLA"), c["pop"]))
        others = [c for c in cands if c is not best and c["pop"] >= 5000]
        if others and not ok:
            row["_amb"] = f"{best['name']} ({self.admin1.get(best['cc'] + '.' + best['a1'], best['a1'])}, {best['pop']}) parmi " + \
                ", ".join(f"{c['name']} ({self.admin1.get(c['cc'] + '.' + c['a1'], c['a1'])}, {c['pop']})" for c in others[:3])
        return best

    def lookup(self, n, row):
        n2 = ALIAS.get((row["iso"], n), n)
        for cc in row["geo_cc"]:
            hit = self.pick(self.by.get((cc, n2)), row, n2)
            if hit:
                return hit, "exact"
            n3 = re.sub(r"^(le|la|les|l|el|al|the)\s+", "", n2)
            if n3 != n2:
                hit = self.pick(self.by.get((cc, n3)), row, n3)
                if hit:
                    return hit, "article"
        return None

    def find(self, row):
        a = ALIAS.get((row["iso"], norm(row["city"])))
        if isinstance(a, int) and a in self.cities:
            return self.cities[a], "alias"
        if isinstance(a, tuple):
            return dict(gid=None, lat=a[0], lon=a[1], pop=0), "alias"
        tries = [row["city"]]
        tries += [re.sub(r"\s*\(.*?\)\s*", " ", row["city"]).strip()]
        tries += re.findall(r"\(([^)]*)\)", row["city"])
        tries += [row["raw_city"], re.sub(r"\s*\(.*?\)\s*", " ", row["raw_city"]).strip()]
        tries += [x for x in re.split(r"\s*[-,/]\s*", row["city"]) if len(x) > 2]
        base = re.sub(r"\s*\(.*?\)\s*", " ", row["city"]).strip()
        toks = base.split()
        drop = {"ville", "ciudad", "city", "cidade", "kaupunki", "province", "town", "centre", "center", "centro"}
        kept = [t for t in toks if t.lower() not in drop and not (t.isupper() and len(t) <= 3 and len(toks) > 1)]
        if kept != toks:
            tries.append(" ".join(kept))
        # premiers mots seuls (« Bukavu Kivu Sud » → Bukavu) : essayés après les fautes de frappe, et marqués
        partial = [" ".join(kept[:i]) for i in range(len(kept) - 1, 0, -1)]
        seen = []
        for t in tries:
            n = norm(t)
            if not n or n in seen:
                continue
            seen.append(n)
            hit = self.lookup(n, row)
            if hit:
                return hit
        # fautes de frappe : distance ≤ 1 (≤ 2 au-delà de 8 lettres), même pays
        for n in seen[:2]:
            k = tol(len(n))
            if not k:
                continue
            for cc in row["geo_cc"]:
                best, best_key = None, None
                for gid in self.by_cc.get(cc, []):
                    c = self.cities[gid]
                    if c["pop"] < 1000 and c["fcode"] == "PPLX":
                        continue
                    dmin = min((dl(n, nn, k) for nn in c["_norms"] if abs(len(nn) - len(n)) <= k), default=k + 1)
                    if dmin <= k and self.admin_ok(c, row) is not False:
                        key = (dmin, -c["pop"])          # la plus proche d'abord, puis la plus peuplée
                        if best_key is None or key < best_key:
                            best, best_key = c, key
                if best:
                    return best, "fuzzy"
        for t in partial:
            n = norm(t)
            if len(n) >= 4 and n not in seen:
                hit = self.lookup(n, row)
                if hit:
                    return hit[0], "partial"
        # dernière chance : un morceau de l'adresse (« 28004 Madrid », « …, Sevilla »)
        parts = [re.sub(r"\d+", " ", p).strip() for p in re.split(r"[,\n]|\s-\s", row["addr"])]
        for p in reversed(parts):
            n = norm(p)
            if len(n) < 3:
                continue
            for cc in row["geo_cc"]:
                hit = self.pick(self.by.get((cc, n)), row, n)
                if hit:
                    return hit, "address"
        return None, "none"


# ---------------------------------------------------------------------------
# Téléphones : la logique des pages (make_pays.national / make_centres.tel_href)
# ---------------------------------------------------------------------------
def phone_of(row, countries):
    import make_centres as MC
    import make_pays as MP
    raw = re.sub(r"\s+", " ", row["phone"]).strip()
    if not raw or re.sub(r"\D", "", raw) in MP.BAD_PHONES:
        return None
    country = row["country_fr"]
    if country in MP.PHONE:
        x = MP.national(raw, country)
        # Longueurs nationales des tables européennes du 26/10/2026 (Luxembourg : 6 chiffres) : 3 + 3, et toute autre
        # longueur affichée d'un bloc plutôt que de faire échouer la construction.
        groups = {6: (3, 3), 7: (1, 3, 3), 8: (4, 4), 9: (3, 3, 3), 10: (3, 3, 4), 11: (1, 2, 4, 4)}.get(len(x or ""), (len(x or ""),))
        if x:
            cc = MP.PHONE[country][0]
            parts, i = [], 0
            for g in groups:
                parts.append(x[i:i + g])
                i += g
            return [f"+{cc}{x}", f"+{cc} " + " ".join(parts)]
        return raw
    if country not in MC.CC:
        code = countries.get(row["iso"], {}).get("phone", "")
        if code:
            MC.CC[country] = code
    href = MC.tel_href(raw, country)
    return [href, raw] if href else raw


# ---------------------------------------------------------------------------
# Liens vers nos pages
# ---------------------------------------------------------------------------
def page_exists(path):
    return os.path.exists(os.path.join(ROOT, path.strip("/"), "index.html"))


def site_links(by_norm):
    """{(iso2, exam, 'c', ville fr) ou (iso2, exam, 'p', ''): {lang: chemin}} — d'après les configurations."""
    import make_centres as MC
    import make_pays as MP
    from i18n_registry import path_of, specs as tr_specs
    links = defaultdict(dict)
    files_country = {}

    def country_of(file):
        if file not in files_country:
            try:
                d = json.load(open(os.path.join(DATA, file + ".json"), encoding="utf-8"))
                files_country[file] = (d.get("iso2") or by_norm.get(norm(d.get("country", ""))), d.get("country", ""))
            except Exception:
                files_country[file] = (None, "")
        return files_country[file]

    def put(key, lang, path, prio):
        if not page_exists(path.split("#")[0]):
            return
        cur = links[key].get(lang)
        if cur is None or prio < cur[1]:
            links[key][lang] = (path, prio)

    # 1. pages ville FR (make_villes)
    try:
        from villes_config import VILLES
        for v in VILLES:
            for city in v["match"]:
                put((v["country"].upper(), v["exam"], "c", city), "fr", f"/centres/{v['slug']}/", 0)
    except Exception as e:
        print("  ! villes_config :", e)
    # 2. pages pays (make_pays) en toutes langues, et pages ville traduites (layout « city »)
    pays = []
    for mod in sorted({os.path.basename(p)[:-3] for p in glob.glob(os.path.join(HERE, "pays_config*.py"))}):
        try:
            pays += [dict(s, _fr=True) if "lang" not in s else s for s in __import__(mod).PAGES]
        except Exception as e:
            print(f"  ! {mod} :", e)
    try:
        pays += [s for s in tr_specs() if s not in pays]
    except Exception as e:
        print("  ! registre :", e)
    for s in pays:
        if "file" not in s or "exam" not in s or "slug" not in s:
            continue
        iso, cname = country_of(s["file"])
        if not iso:
            continue
        lang = s.get("lang", "fr")
        path = f"/centres/{s['slug']}/" if lang == "fr" else path_of(s)
        if s.get("layout") == "city":
            for city in s.get("match", []):
                put((iso, s["exam"], "c", city), lang, path, 0)
        else:
            put((iso, s["exam"], "p", ""), lang, path, 0)
    # 3. annuaire FR (make_centres) : pages pays, puis pages régionales avec ancre
    for p in MC.PAGES:
        exam = {"TCF": "tcf", "DELF": "delf"}.get(p["exam"], "civique")
        multi = p["layout"] == "multi"
        for f in p["files"]:
            iso, cname = country_of(f)
            if not iso:
                continue
            path = f"/centres/{p['slug']}/" + (f"#pays-{MC.slug(cname)}" if multi else "")
            put((iso, exam, "p", ""), "fr", path, 2 if multi else 1)
    return {k: {l: p for l, (p, _) in v.items()} for k, v in links.items()}


# ---------------------------------------------------------------------------
# Programme
# ---------------------------------------------------------------------------
def r3(x):
    return round(x, 3)


def km(a, b, c, d):
    p = math.pi / 180
    x = math.sin((c - a) * p / 2) ** 2 + math.cos(a * p) * math.cos(c * p) * math.sin((d - b) * p / 2) ** 2
    return 12742 * math.asin(math.sqrt(x))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    report = tef_map = None
    if "--report" in sys.argv:
        report = sys.argv[sys.argv.index("--report") + 1]
        args = [a for a in args if a != report]
    if "--tef-map" in sys.argv:            # carte CCI brute (coordonnées des centres TEF, par cci_id) : donnée lue
        tef_map = sys.argv[sys.argv.index("--tef-map") + 1]
        args = [a for a in args if a != tef_map]
    paths = classify(args)
    cnames, by_norm = country_table()

    print("GeoNames : villes…")
    cities = read_cities(paths["cities"])
    countries = read_countries(paths["countries"])
    admin1 = read_admin1(paths["admin1"])
    print(f"  {len(cities)} villes ; noms étiquetés…")
    n = read_alternates(paths["alt"], cities, countries)
    print(f"  {n} noms étiquetés gardés")

    # --- centres ---
    srcs = load_sources(by_norm)
    rows = centre_rows(srcs, cnames)
    print(f"Centres : {len(rows)} fiches, {len(srcs)} listes ({sum(1 for s in srcs if s[4].startswith('fei_monde'))} fei_monde)")
    cci_ll = {}
    if tef_map:
        try:
            raw = json.load(open(tef_map, encoding="utf-8")).get("centers", {})
            for k, v in raw.items():
                la, lo = v.get("lat") or v.get("autoLat"), v.get("lng") or v.get("autoLng")
                if isinstance(la, (int, float)) and isinstance(lo, (int, float)) and (la or lo):
                    cci_ll[int(v.get("tc_id") or k)] = (float(la), float(lo), v.get("geo_iso") or "")
        except Exception as e:
            print("  ! carte TEF illisible :", e)
    geo = Geocoder(cities, admin1)
    unmatched, decisions, far_tef = [], [], []
    how = Counter()
    for r in rows:
        if isinstance(r.get("lat"), (int, float)) and isinstance(r.get("lon"), (int, float)):
            r["gid"], r["glat"], r["glon"] = None, float(r["lat"]), float(r["lon"])
            how["source"] += 1
            continue
        c, kind = geo.find(r)
        how[kind] += 1
        if c and kind not in ("exact",):
            r["_how"] = f"{kind} → {c.get('name', '(coordonnées)')} ({c.get('cc', '')} {c.get('pop', 0)})"
            decisions.append(r)
        # Centres TEF : la carte CCI donne un point, géocodé automatiquement (parfois au Burkina pour San José du
        # Costa Rica). Il ne sert que s'il tombe dans le pays du centre, et ne l'emporte sur le nom de ville que si
        # celui-ci a été deviné (faute, morceau d'adresse) ou si une autre ville de l'adresse est à côté du point.
        ll = cci_ll.get(r.get("cci_id"))
        if ll and ll[2] and ll[2] not in r["geo_cc"]:
            ll = None
        ll = ll[:2] if ll else None
        if c and ll and km(c["lat"], c["lon"], *ll) > 40:
            alt = None
            if kind in ("exact", "article", "alias"):
                for part in re.split(r"[,\n(]|\s-\s", r["addr"]):
                    toks = norm(re.sub(r"\d+", " ", part)).split()
                    subs = {" ".join(toks[a:b]) for a in range(len(toks)) for b in range(a + 1, min(len(toks), a + 4) + 1)}
                    for n_ in subs:
                        for cc in r["geo_cc"]:
                            for gid in geo.by.get((cc, n_), []):
                                g_ = cities[gid]
                                if km(g_["lat"], g_["lon"], *ll) <= 15 and (alt is None or g_["pop"] > alt["pop"]):
                                    alt = g_
                if alt is None:
                    ll = None               # le nom de ville exact l'emporte sur un point automatique lointain
            if ll is not None:
                far_tef.append((r, c, ll, alt))
                c = alt
        if c:
            r["gid"], r["glat"], r["glon"] = c["gid"], c["lat"], c["lon"]
            r["gid"] = r["gid"] or None
        elif ll:
            near = geo.nearest(ll, r["geo_cc"])
            if near:
                r["gid"], r["glat"], r["glon"] = near["gid"], near["lat"], near["lon"]
                how["carte CCI → ville"] += 1
            else:
                r["gid"], r["glat"], r["glon"] = None, ll[0], ll[1]
                how["carte CCI"] += 1
        else:
            r["gid"] = r["glat"] = r["glon"] = None
            unmatched.append(r)
    print("  géocodage :", dict(how))

    # --- fusion : un même centre dans plusieurs listes (TCF + DELF + civique) ---
    parent = list(range(len(rows)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    # Même lieu + même début d'adresse (« 6161 Cambie Street ») = même centre. Même nom : fusionné aussi, sauf si
    # les adresses diffèrent (deux antennes du même organisme dans une ville restent deux fiches).
    STOP = {"de", "du", "des", "la", "le", "les", "d", "l", "of", "the", "del", "et", "and", "y", "e", "a", "au", "aux"}

    def akey(r):
        """« 11, rue Pierre Bourdan, 69003 Lyon » → « 11 rue pierre » : numéro et début de la voie, sans code postal."""
        drop = set(norm(r["city"]).split()) | STOP
        # « 01 RUE COMMANDANT DJABER » ≡ « 1, rue du commandant Djaber » (Tlemcen, listes TCF et DELF) : sans zéro de tête.
        toks = [(t.lstrip("0") or "0") if t.isdigit() else t
                for t in norm(r["addr"]).split() if t not in drop and not (t.isdigit() and len(t) >= 4)]
        k = toks[:3]
        return " ".join(k) if len(k) == 3 and any(t.isdigit() for t in k[:2]) else ""

    def nkey(r):
        """« Alliance Française de Lyon » ≡ « Alliance française » à Lyon : sans la ville, le pays ni les mots-outils."""
        drop = set(norm(r["city"]).split()) | set(norm(r["country_fr"]).split()) | STOP
        return " ".join(t for t in norm(r["name"]).split() if t not in drop) or norm(r["name"])

    keys, by_name = {}, defaultdict(list)
    for i, r in enumerate(rows):
        place = r["gid"] or norm(r["city"])
        r["_ak"] = akey(r)
        if r["_ak"]:
            k = ("a", r["iso"], place, r["_ak"])
            if k in keys:
                parent[find(i)] = find(keys[k])
            else:
                keys[k] = i
        by_name[(r["iso"], place, nkey(r))].append(i)
    for ids in by_name.values():
        aks = {rows[i]["_ak"] for i in ids if rows[i]["_ak"]}
        if len(aks) <= 1:
            for i in ids[1:]:
                parent[find(i)] = find(ids[0])
        else:
            for i in ids:
                if not rows[i]["_ak"]:
                    parent[find(i)] = find(ids[0])
    # Même lieu + même téléphone (8 derniers chiffres) ou même e-mail : le même centre écrit autrement d'une liste à
    # l'autre (« Rue de l'entraide, Talborjt » côté TCF, « Rue Chenguit, nouveau Talborjt » côté DELF, à Agadir). Seulement
    # entre listes différentes : deux fiches d'une même liste (« Alliance française de Dubai (centre 1) » et « (centre 2) »,
    # les trois sites DELF de Bogota) sont deux lieux et le restent (26/10/2026).
    exams_of = defaultdict(set)
    for i, r in enumerate(rows):
        exams_of[find(i)].add(r["exam"])
    contact = defaultdict(list)
    for i, r in enumerate(rows):
        place = r["gid"] or norm(r["city"])
        digits = [re.sub(r"\D", "", p) for p in re.split(r"\s*/\s*", r["phone"])]
        for k in {"p" + d[-8:] for d in digits if len(d) >= 8} | {"e" + e.lower() for e in r["emails"]}:
            contact[(r["iso"], place, k)].append(i)
    for ids in contact.values():
        for i in ids[1:]:
            a, b = find(ids[0]), find(i)
            if a != b and not (exams_of[a] & exams_of[b]):
                parent[b] = a
                exams_of[a] |= exams_of.pop(b)
    groups = OrderedDict()
    for i in range(len(rows)):
        groups.setdefault(find(i), []).append(rows[i])

    # --- sites corrigés des pages pays (spec["urls"]) ---
    import make_pays as MP
    url_fix = {}
    for mod in sorted({os.path.basename(p)[:-3] for p in glob.glob(os.path.join(HERE, "pays_config*.py"))}):
        try:
            for s in __import__(mod).PAGES:
                for k, u in s.get("urls", {}).items():
                    url_fix[(s.get("file"), k)] = u
        except Exception:
            pass
    file_iso = {}

    links = site_links(by_norm)

    # --- villes de centres ---
    city_key = {}
    cities_rows = []          # [ {key, iso, gid, lat, lon, names(fr→), pop, centres:[...]} ]
    centres_out = []
    order = {"tcf": 0, "delf": 1, "civique": 2, "tef": 3}
    for g in groups.values():
        g.sort(key=lambda r: order[r["exam"]])
        base = g[0]
        exams = sorted({r["exam"] for r in g}, key=order.get)
        so = any(r["so"] for r in g if r["exam"] == "tcf")
        emails = []
        for r in g:
            for e in r["emails"]:
                h = e.split("@")[-1].lower()
                if not personal(e) and not blocked(h) and e.lower() not in [x.lower() for x in emails]:
                    emails.append(e)
        url = ""
        for r in g:
            u = r["url"]
            src_file = os.path.splitext(os.path.basename(r["origin"]))[0]
            try:
                r_city = MP.city_of(dict(r["raw"], cp=r["raw"].get("cp", ""), city_cp=r["raw"].get("city_cp", "")), r["country_fr"])
            except Exception:
                r_city = r["city"]
            k = MP.slug(r_city + " " + r["name"])
            if (src_file, k) in url_fix:          # site corrigé sur nos pages pays ("" = pas de lien)
                u = url_fix[(src_file, k)]
            if u:
                uu = u if u.startswith("http") else "http://" + u
                if not blocked(host(uu)):
                    url = uu
                    break
        phone = next((p for p in (phone_of(r, countries) for r in g) if p), None)
        addr = next((r["addr"] for r in g if r["addr"]), "")
        place = base["gid"] or ("x", base["iso"], norm(base["city"]))
        ck = (base["iso"], place)
        if ck not in city_key:
            city_key[ck] = len(cities_rows)
            gc = cities.get(base["gid"]) if base["gid"] else None
            cities_rows.append(dict(iso=base["iso"], gid=base["gid"], lat=base["glat"], lon=base["glon"],
                                    pop=gc["pop"] if gc else 0, fr_names=Counter(), curated=Counter(), centres=[], gc=gc))
        crow = cities_rows[city_key[ck]]
        for r in g:
            crow["fr_names"][r["city"]] += 1
            if r["curated"]:
                crow["curated"][r["city"]] += 1
        names_fr = MP.disp_name(base["name"], base["country_fr"], {"lang": "fr"})
        names_en = MP.disp_name(base["name"], base["country_fr"], {"lang": "en"})
        names_es = MP.disp_name(base["name"], base["country_fr"], {"lang": "es"}) \
            if base["iso"] in ("ES", "MX", "CO", "AR", "CL", "PE", "EC", "UY", "PY", "BO", "VE", "CR", "PA", "GT", "HN",
                               "SV", "NI", "DO", "CU", "PR") else names_fr
        tef = [r for r in g if r["exam"] == "tef"]
        alias = []                          # les autres noms du même centre dans les autres listes (recherche par nom)
        for r in g:
            if norm(r["name"]) not in {norm(names_fr)} | {norm(x) for x in alias}:
                alias.append(r["name"])
        cen = dict(n=names_fr, a=addr, exams=exams, so=so, emails=emails[:2], url=url, phone=phone, alias=alias,
                   tp=sorted({p for r in tef for p in r["products"]}), tc=next((r["contact"] for r in tef if r["contact"]), ""),
                   city_fr=base["city"], iso=base["iso"], dates={r["exam"]: r["date"] for r in g},
                   fei_ids=[r["fei_id"] for r in g if r.get("fei_id")])
        if names_en != names_fr:
            cen["ne"] = names_en
        if names_es != names_fr:
            cen["ns"] = names_es
        crow["centres"].append(cen)
        centres_out.append(cen)

    # --- gazetier ---
    centre_gids = {c["gid"] for c in cities_rows if c["gid"]}
    keep = [c for c in cities.values()
            if (c["pop"] >= POP_MIN and c["fcode"] != "PPLX") or c["gid"] in centre_gids or c["fcode"] == "PPLC"]
    print(f"Gazetier : {len(keep)} villes")
    disp = {c["gid"]: display_names(c) for c in keep}
    # région admin1 quand le nom affiché existe deux fois dans le pays
    dup = Counter((c["cc"], norm(disp[c["gid"]][0])) for c in keep)
    entries = []          # (norm, original, gid)
    for c in keep:
        big = c["pop"] >= 1_000_000
        for orig, nn, kind in search_names(c, countries, big, c["gid"] in centre_gids):
            entries.append((nn, orig, c["gid"]))

    def row_for(gid, names):
        c = cities[gid]
        d = disp[gid]
        n0 = names[0]
        # noms affichés par langue : seulement pour les villes de plus de 30 000 habitants et celles des centres
        dd = [x if x != n0 else "" for x in d] if (c["pop"] >= 30_000 or gid in centre_gids) else ["", "", "", ""]
        row = ["|".join(names), r3(c["lat"]), r3(c["lon"]), c["cc"], round(c["pop"] / 1000)]
        a1 = admin1.get(f"{c['cc']}.{c['a1']}", "") if dup[(c["cc"], norm(d[0]))] > 1 else ""
        if any(dd) or a1:
            row.append("|".join(dd) if any(dd) else 0)
        if a1:
            row.append(a1)
        return row

    def size_of(items):
        by_gid = OrderedDict()
        for nn, orig, gid in items:
            by_gid.setdefault(gid, []).append(orig)
        rows_ = [row_for(g, ns) for g, ns in by_gid.items()]
        return len(json.dumps(rows_, ensure_ascii=False, separators=(",", ":")).encode()), rows_

    buckets = defaultdict(list)
    for e in entries:
        buckets[e[0][:2]].append(e)
    final = {}
    stack = list(buckets.items())
    while stack:
        key, items = stack.pop()
        size, rows_ = size_of(items)
        longer = [e for e in items if len(e[0]) > len(key)]
        if size <= SHARD_MAX or not longer:
            final[key] = rows_
            continue
        exact = [e for e in items if len(e[0]) <= len(key)]
        sub = defaultdict(list)
        for e in longer:
            sub[e[0][:len(key) + 1]].append(e)
        if exact:                           # le nom qui est exactement la clé reste dans le morceau parent
            final[key] = size_of(exact)[1]
        stack += list(sub.items())
    # Les petits morceaux voisins partagent un fichier ({clé: lignes}) : moins de fichiers, même règle de lecture.
    os.makedirs(OUT_GEO, exist_ok=True)
    for f in glob.glob(os.path.join(OUT_GEO, "*.json")):
        os.remove(f)
    enc = {k: json.dumps(v, ensure_ascii=False, separators=(",", ":")) for k, v in final.items()}
    files, cur, cur_size = [], [], 0
    for k in sorted(final):
        b = len(enc[k].encode()) + len(k.encode()) + 4
        if cur and cur_size + b > SHARD_MAX * 3 // 4:
            files.append(cur)
            cur, cur_size = [], 0
        cur.append(k)
        cur_size += b
    if cur:
        files.append(cur)
    total, biggest, manifest = 0, (0, ""), []
    for ks in files:
        name = "k" + fname(ks[0])           # jamais de « _ » en tête : Jekyll (GitHub Pages) écarterait le fichier
        s = "{" + ",".join(json.dumps(k, ensure_ascii=False) + ":" + enc[k] for k in ks) + "}"
        with open(os.path.join(OUT_GEO, name + ".json"), "w", encoding="utf-8") as fh:
            fh.write(s)
        b = len(s.encode())
        total += b
        biggest = max(biggest, (b, name))
        manifest.append([name, "|".join(ks)])
    keys_sorted = manifest
    print(f"  {len(final)} morceaux dans {len(files)} fichiers, {total / 1e6:.2f} Mo, le plus gros : {biggest[1]!r} "
          f"{biggest[0] / 1000:.1f} Ko, {len(entries)} noms")

    # --- index du chercheur ---
    os.makedirs(os.path.join(OUT_FIND, "c"), exist_ok=True)
    for f in glob.glob(os.path.join(OUT_FIND, "c", "*.json")):
        os.remove(f)
    import make_pays as MP2
    by_country = defaultdict(list)
    for i, cr in enumerate(cities_rows):
        by_country[cr["iso"]].append(i)
    # villes triées par pays puis nom, pour un index stable
    order_rows = sorted(range(len(cities_rows)), key=lambda i: (cities_rows[i]["iso"], norm(cities_rows[i]["fr_names"].most_common(1)[0][0])))
    remap = {old: new for new, old in enumerate(order_rows)}
    cities_rows = [cities_rows[i] for i in order_rows]
    index_rows, names_rows = [], []
    for ri, cr in enumerate(cities_rows):
        fr = cr["fr_names"].most_common(1)[0][0]
        if cr["gc"]:
            d = disp.get(cr["gid"]) or display_names(cr["gc"])
            en, es, ar = d[1], d[2], d[3]
            # le nom français de GeoNames (« Anvers », « Saint-Martin-d'Hères ») sauf quand nos pages ont fixé le leur
            fr = cr["curated"].most_common(1)[0][0] if cr["curated"] else (d[0] if norm(d[0]) else fr)
        else:
            en = es = ar = fr
        country_fr = cnames.get(cr["iso"], {}).get("fr", cr["iso"])
        # traductions déjà relues sur nos pages
        en = MP2.CITY_T.get("en", {}).get(country_fr, {}).get(fr, en)
        es = MP2.CITY_T.get("es", {}).get(country_fr, {}).get(fr, es)
        ar = MP2.CITY_T.get("ar", {}).get(country_fr, {}).get(fr, ar)
        names = [fr, en, es, ar]
        nstr = fr if len(set(names)) == 1 else "|".join(x if (i == 0 or x != fr) else "" for i, x in enumerate(names))
        cnt = [len(cr["centres"])] + [sum(1 for c in cr["centres"] if e in c["exams"]) for e in EXAMS]
        while cnt and cnt[-1] == 0:
            cnt.pop()                       # « total,tcf,delf,civique,tef » sans les zéros de fin
        lat = r3(cr["lat"]) if cr["lat"] is not None else None
        lon = r3(cr["lon"]) if cr["lon"] is not None else None
        index_rows.append([nstr, lat, lon, cr["iso"], ",".join(map(str, cnt)), round(cr["pop"] / 1000)])
        cr["_fr"] = fr
        cr["names"] = names
        for c in cr["centres"]:
            names_rows.append([c["n"], ri])
            for al in c["alias"]:
                names_rows.append([al, ri, c["n"]])
    # deux villes de même nom dans un pays (Saint-Denis 93 / La Réunion) : la région ou le territoire en plus
    # et toute ville d'outre-mer listée sous la France (Papeete) : « @PF », que finder.js traduit
    same = Counter((cr["iso"], norm(cr["_fr"])) for cr in cities_rows)
    for ri, cr in enumerate(cities_rows):
        gc = cr["gc"]
        if gc and gc["cc"] != cr["iso"] and gc["cc"] in cnames:
            index_rows[ri].append("@" + gc["cc"])
        elif gc and same[(cr["iso"], norm(cr["_fr"]))] > 1:
            q = admin1.get(f"{gc['cc']}.{gc['a1']}", "")
            if q:
                index_rows[ri].append(q)
    # pays
    countries_out = {}
    present = {cr["iso"] for cr in cities_rows}
    for cc, d in sorted(cnames.items()):
        al = [a for a in COUNTRY_ALIASES.get(cc, []) if norm(a) not in {norm(x) for x in d.values()}]
        countries_out[cc] = [d["fr"], d["en"], d["es"], d["ar"]] + al
    import make_centres as MC
    fei_ids = dict(MC.PAYS_ID)
    fei_ids.update(MP2.PAYS_ID)
    fei_country = {}
    for iso, ex, date, dd, origin in srcs:
        pid = dd.get("fei_id") or dd.get("pays_id") or dd.get("fei_pays_id")
        if pid:
            fei_country[iso] = pid
        elif dd.get("country") in fei_ids:
            fei_country[iso] = fei_ids[dd["country"]]
    dates = sorted({s[2] for s in srcs if s[2]})
    exams_present = [e for e in EXAMS if any(e in c["exams"] for c in centres_out)]
    # grande région de chaque pays (celle du manifeste FEI, sinon le continent de GeoNames)
    region = {}
    try:
        for c in json.load(open(os.path.join(DATA, "fei_monde", "manifest.json"), encoding="utf-8")).get("countries", []):
            if c.get("iso2") and c.get("region"):
                region[c["iso2"]] = c["region"]
    except Exception:
        pass
    arab = set("DZ BH KM DJ EG IQ JO KW LB LY MR MA OM PS QA SA SO SD SY TN AE YE".split())
    cont = {"EU": "europe", "AF": "afrique", "AS": "asie_oceanie", "OC": "asie_oceanie", "AN": "asie_oceanie",
            "NA": "ameriques", "SA": "ameriques"}
    for cc in present:
        if cc not in region:
            region[cc] = "monde_arabe" if cc in arab else cont.get(countries.get(cc, {}).get("continent"), "asie_oceanie")
    dates_by_exam = defaultdict(set)
    for iso_, ex, date, dd, origin in srcs:
        if date:
            dates_by_exam[ex].add(date)
    index = {"v": 1, "d": [dates[0], dates[-1]] if dates else [], "x": exams_present, "k": keys_sorted,
             "D": {ex: [min(v), max(v)] for ex, v in dates_by_exam.items()},
             "f": fei_country, "g": {cc: region[cc] for cc in sorted(present)}, "C": countries_out, "r": index_rows}
    with open(os.path.join(OUT_FIND, "index.json"), "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(OUT_FIND, "names.json"), "w", encoding="utf-8") as fh:
        json.dump(names_rows, fh, ensure_ascii=False, separators=(",", ":"))

    # fiches par pays
    for iso in sorted(present):
        L, Lidx = [], {}
        out_c = []
        cdates = {}
        for ri, cr in enumerate(cities_rows):
            if cr["iso"] != iso:
                continue
            for c in sorted(cr["centres"], key=lambda c: norm(c["n"])):
                g = []
                for ex in c["exams"]:
                    for scope, key in (("c", (iso, ex, "c", c["city_fr"])), ("p", (iso, ex, "p", ""))):
                        urls = links.get(key)
                        if not urls:
                            continue
                        rec = (ex, scope, urls.get("fr", ""), urls.get("en", ""), urls.get("es", ""), urls.get("ar", ""))
                        if rec not in Lidx:
                            Lidx[rec] = len(L)
                            L.append(list(rec))
                        g.append(Lidx[rec])
                for ex, dt in c["dates"].items():
                    cdates[ex] = max(cdates.get(ex, ""), dt)
                o = {"r": ri, "n": c["n"]}
                for k in ("ne", "ns"):
                    if k in c:
                        o[k] = c[k]
                if c["a"]:
                    o["a"] = c["a"]
                if c["phone"]:
                    o["p"] = c["phone"]
                if c["emails"]:
                    o["e"] = c["emails"]
                if c["url"]:
                    o["w"] = c["url"]
                if c["so"]:
                    o["s"] = 1
                if c["tp"]:
                    o["tp"] = c["tp"]           # épreuves TEF avec des sessions publiées sur la carte CCI (date : d.tef)
                if c["tc"] and not blocked(host(c["tc"])):
                    o["tc"] = c["tc"]
                o["x"] = ",".join(c["exams"])
                if g:
                    o["g"] = g
                out_c.append(o)
        with open(os.path.join(OUT_FIND, "c", f"{iso}.json"), "w", encoding="utf-8") as fh:
            json.dump({"i": iso, "d": cdates, "L": L, "c": out_c}, fh, ensure_ascii=False, separators=(",", ":"))

    # rapport
    sz = lambda p: os.path.getsize(p)
    print(f"Index : {len(index_rows)} villes de centres, {len(centres_out)} centres (après fusion), "
          f"{sum(1 for r in index_rows if r[1] is None)} villes sans coordonnées")
    print(f"  index.json {sz(os.path.join(OUT_FIND, 'index.json')) / 1000:.1f} Ko · names.json "
          f"{sz(os.path.join(OUT_FIND, 'names.json')) / 1000:.1f} Ko · {len(present)} fichiers pays")
    if report:
        with open(report, "w", encoding="utf-8") as fh:
            fh.write(f"# Centres non géocodés ({len(unmatched)})\n")
            for r in unmatched:
                fh.write(f"{r['iso']}\t{r['exam']}\t{r['city']!r}\t(raw {r['raw_city']!r})\t{r['name']}\t{r['addr']}\t[{r['origin']}]\n")
            amb = [r for r in rows if r.get("_amb")]
            fh.write(f"\n# Homonymes départagés par la population ({len(amb)}) : à relire\n")
            for r in amb:
                fh.write(f"{r['iso']}\t{r['city']!r}\t{r['_amb']}\t{r['addr'][:90]}\n")
            fh.write(f"\n# TEF : ville trouvée à plus de 40 km du point de la carte CCI ({len(far_tef)}) — point CCI retenu\n")
            for r, c, ll, alt in far_tef:
                fh.write(f"{r['iso']}\t{r['city']!r}\tGeoNames {c['name']} ({c['lat']:.2f},{c['lon']:.2f}) / CCI {ll[0]:.2f},{ll[1]:.2f}"
                         f" → {alt['name'] if alt else 'ville la plus proche du point CCI'}\t{r['name']}\n")
            fh.write(f"\n# Placés autrement que par le nom exact ({len(decisions)}) : à relire\n")
            for r in decisions:
                fh.write(f"{r['iso']}\t{r['city']!r}\t{r['_how']}\t{r['name']}\t{r['addr'][:80]}\n")
        print(f"  rapport : {report} ({len(unmatched)} fiches non placées)")


if __name__ == "__main__":
    main()
