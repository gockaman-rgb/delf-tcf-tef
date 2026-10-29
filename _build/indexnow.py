#!/usr/bin/env python3
"""IndexNow (29/10/2026) : signale à Bing, Yandex et les moteurs partenaires les URL créées ou modifiées, sans compte.

La clé est dans _build/indexnow_key.txt et doit être servie telle quelle à https://delf-tcf-tef.fr/<clé>.txt (fichier à la
racine du site, versionné). Protocole : POST JSON sur https://api.indexnow.org/indexnow ; 200 ou 202 = accepté.

Usage : python3 _build/indexnow.py            → toutes les URL du sitemap (max 10 000 par envoi)
        python3 _build/indexnow.py /a/ /b/    → ces chemins seulement
        python3 _build/indexnow.py --changed  → les URL dont le lastmod du sitemap est à la date du jour
"""
import datetime
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
HOST = "delf-tcf-tef.fr"
BASE = f"https://{HOST}"


def sitemap_urls(today_only=False):
    sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    today = datetime.date.today().isoformat()
    out = []
    for m in re.finditer(r"<url>\s*<loc>([^<]+)</loc>(?:\s*<lastmod>([^<]*)</lastmod>)?", sm):
        if not today_only or m.group(2) == today:
            out.append(m.group(1))
    return out


def main():
    key = open(os.path.join(HERE, "indexnow_key.txt"), encoding="utf-8").read().strip()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if args:
        urls = [BASE + a if a.startswith("/") else a for a in args]
    else:
        urls = sitemap_urls(today_only="--changed" in sys.argv)
    if not urls:
        print("indexnow : rien à envoyer")
        return
    body = json.dumps({"host": HOST, "key": key, "keyLocation": f"{BASE}/{key}.txt", "urlList": urls[:10000]}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"indexnow : {len(urls)} URL envoyées, réponse {r.status}")
    except urllib.error.HTTPError as e:
        print(f"indexnow : refus {e.code} — {e.read()[:200]!r}")
        sys.exit(1)


if __name__ == "__main__":
    main()
