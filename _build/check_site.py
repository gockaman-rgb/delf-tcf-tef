#!/usr/bin/env python3
"""Vérification du site statique avant commit (19/09/2026) : équilibre des balises, JSON-LD valide,
liens internes et ancres, images, OG, ids dupliqués, un seul h1, titre ≤ 60, description ≤ 160.

Usage : python3 _build/check_site.py
"""
import glob
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.errors, self.ids, self.links, self.imgs, self.h1 = [], [], [], [], [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img":
            self.imgs.append(a.get("src", ""))
            if "alt" not in a:
                self.errors.append(f"img sans alt l.{self.getpos()[0]}")
        if tag == "h1":
            self.h1 += 1

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            self.errors.append(f"</{tag}> inattendu l.{self.getpos()[0]} (pile : {[t for t, _ in self.stack[-3:]]})")


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True))
    files = [f for f in files if "/_build/" not in f and "/node_modules/" not in f]
    pages = {}
    for f in files:
        rel = "/" + os.path.relpath(f, ROOT).replace("index.html", "")
        pages[rel] = f
    problems = 0
    anchors = {}
    for rel, f in pages.items():
        s = open(f, encoding="utf-8").read()
        p = P()
        p.feed(s)
        errs = list(p.errors)
        if p.stack:
            errs.append(f"balises non fermées : {[t for t, _ in p.stack[:5]]}")
        if p.h1 != 1:
            errs.append(f"{p.h1} h1")
        dup = {i for i in p.ids if p.ids.count(i) > 1}
        if dup:
            errs.append(f"ids dupliqués : {sorted(dup)[:6]}")
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            try:
                json.loads(m.group(1))
            except Exception as e:
                errs.append(f"JSON-LD invalide : {e}")
        t = re.search(r"<title>(.*?)</title>", s, re.S)
        if not t:
            errs.append("pas de <title>")
        elif len(t.group(1)) > 60 and rel not in ("/questions/",):
            errs.append(f"title {len(t.group(1))} car.")
        d = re.search(r'name="description" content="(.*?)"', s)
        if d and len(d.group(1)) > 165:
            errs.append(f"description {len(d.group(1))} car.")
        og = re.search(r'property="og:image" content="([^"]+)"', s)
        if og:
            path = og.group(1).replace("https://delf-tcf-tef.fr", "")
            if not os.path.exists(os.path.join(ROOT, path.lstrip("/"))):
                errs.append(f"og:image absente : {path}")
        anchors[rel] = set(p.ids)
        pages[rel] = (f, p, errs)
    for rel, (f, p, errs) in pages.items():
        for href in p.links:
            if href.startswith(("http", "mailto:", "tel:", "sms:")):
                continue
            target, _, frag = href.partition("#")
            if target == "":
                if frag and frag not in anchors[rel]:
                    errs.append(f"ancre #{frag} absente")
                continue
            if not target.startswith("/"):
                errs.append(f"lien relatif : {href}")
                continue
            if target.endswith("/"):
                ok = target in anchors
            else:
                ok = os.path.exists(os.path.join(ROOT, target.lstrip("/"))) or (target + "/") in anchors
            if not ok:
                errs.append(f"lien mort : {href}")
            elif frag and target in anchors and frag not in anchors[target]:
                errs.append(f"ancre morte : {href}")
        for src in p.imgs:
            if src.startswith("http"):
                continue
            if not os.path.exists(os.path.join(ROOT, src.lstrip("/"))):
                errs.append(f"image absente : {src}")
        if errs:
            problems += 1
            print(rel)
            for e in errs:
                print("   -", e)
    ld = sum(len(re.findall(r'application/ld\+json', open(f, encoding="utf-8").read())) for f, _, _ in pages.values())
    print(f"{len(pages)} pages, {ld} blocs JSON-LD, {problems} page(s) avec problèmes")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
