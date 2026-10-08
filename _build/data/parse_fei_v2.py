#!/usr/bin/env python3
"""Liste FEI v2 (08/10/2026) : extraction structurée du navigateur → data/<type>_<pays>.json.

La v1 (parse_fei.py) découpait le texte de la page et prenait tout nombre de 4-5 chiffres en tête
de ligne pour un code postal — juste en France, faux aux États-Unis (« 30800 Telegraph Rd »). La
v2 lit les champs de chaque fiche (adresse ligne par ligne, téléphone, e-mail, site, option
« sessions sur ordinateur ») et garde l'adresse telle que FEI l'écrit.

Entrée : JSON {"date": iso, "data": {"<Pays>|<tcf|delf_dalf>": [fiche…]}} produit par le JS
d'extraction (champs k, h, a, t, m, w, so). Sortie : un fichier par pays et par type, même schéma
que la v1 (name, city, cp, city_cp, address, phone, emails, url, so) + « org » pour l'organisme
de gestion centrale DELF-DALF, rangé à part.

Usage : python3 _build/data/parse_fei_v2.py <extraction.json>
"""
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
FILE = {"Argentine": "argentine", "Chili": "chili", "Colombie": "colombie", "Équateur": "equateur",
        "Espagne": "espagne", "États-Unis": "etats_unis", "Mexique": "mexique", "Pérou": "perou",
        "Royaume-Uni": "royaume_uni", "Brésil": "bresil", "Haïti": "haiti", "Belgique": "belgique", "Suisse": "suisse",
        "Inde": "inde", "Émirats arabes unis": "emirats"}   # 08/10 : tcf_emirats.json (la page Moyen-Orient garde tcf_emirats_arabes_unis.json du 19/09)

# Jetons d'une adresse de service (jamais un prénom.nom) : seule une adresse qui en contient un est publiée.
GENERIC = re.compile(r"(info|contact|exam|certif|delf|dalf|tcf|direc|director|dir\.|dirpedag|pedagog|secretar|recep|admin|"
                     r"informes|idiomas|lenguas|languages|frances|alianza|alliance|^af|programs|courses|cursos|bonjour|"
                     r"oficina|cultural|centro|centre|coordinat|coordinacion|mediateca|immersion|cel_|campusfrance|"
                     r"buenosaires|^afd|^afno|afpalma|aft|afs|afm|afg|afc|afj|afr|afp|afv|aflp|^dir)", re.I)


# Relu à la main le 08/10/2026 : adresses de service que les jetons ne reconnaissent pas, et
# adresses qui les contiennent mais portent un prénom.
ALLOW = {"adulted@isbos.org", "barranquilla@alianzafrancesa.edu.co", "barranquilla@alianzafrancesa.org.co",
         "cartagena@alianzafrancesa.edu.co", "manizales@alianzafrancesa.edu.co", "oviedo@alianzafrancesa.com",
         "languagecenter@lallianceny.org", "cei.proulex@proulex.udg.mx", "coursonlignemza@gmail.com",
         "sanmigueldeallende@enes.unam.mx", "laic.lasalle@ulsavictoria.edu.mx", "president@flamusa.org",
         "contatos@afbelem.com", "coursesdir.blr@afindia.org", "course.assistant.kolkata@afindia.org",
         "director.lucknow@afindia.org", "academic_coord@afdelhi.org", "courses.trivandrum@afindia.org", "adminalain@afabudhabi.org",
         "ahmedabad@afindia.org", "bhopal@afindia.org", "escola@afbahia.com.br", "atendimento@afsaocarlos.com.br", "midiateca@afcampinas.com.br",
         "montreux@alpadia.com", "ecole@afzurich.ch"}
DENY = {"inesqaftandil@hotmail.com", "angelaalianza@yahoo.com.ar"}


def ok_email(e):
    e = e.strip()
    if not e or e.lower() == "null" or "@" not in e:
        return False
    if e.lower() in ALLOW:
        return True
    if e.lower() in DENY:
        return False
    local = e.split("@")[0]
    if re.match(r"^[a-z]+[._][a-z]+\d*$", local, re.I) and not GENERIC.search(local):
        return False          # prénom.nom, prénom_nom
    return bool(GENERIC.search(local))


def clean(s):
    s = re.sub(r"\s+", " ", s or "").strip()
    return "" if s.lower() == "null" else s


def norm(r):
    h = clean(r["h"])
    br = re.match(r"^(.*?) - ([A-Z]{2}) - (.*)$", h)       # Brésil : « Belém - PA - Alliance française »
    if br:
        city, name = f"{br.group(1)} - {br.group(2)}", br.group(3)
    else:
        city, name = (h.split(" - ", 1) + [""])[:2] if " - " in h else ("", h)
    lines = [clean(x) for x in r["a"] if clean(x) and clean(x) not in ("-",)]
    lines = [re.sub(r"\s+Null$", "", re.sub(r"^-\s*", "", x)) for x in lines]
    emails = []
    for m in r["m"]:
        for e in re.split(r"[,;\s]+", m):
            if ok_email(e) and e.lower() not in [x.lower() for x in emails]:
                emails.append(e)
    phones = [clean(t) for t in r["t"] if clean(t)]
    url = next((clean(w) for w in r["w"] if clean(w) and "@" not in w), "")
    return {"name": clean(name), "city": clean(city).rstrip(","), "cp": "", "city_cp": "",
            "address": ", ".join(lines), "address_lines": lines,
            "phone": " / ".join(phones), "emails": emails, "url": url, "so": bool(r["so"])}


def main():
    src = json.load(open(sys.argv[1], encoding="utf-8"))
    date = src["date"][:10]
    for key, rows in src["data"].items():
        pays, typ = key.split("|")
        t = "tcf" if typ == "tcf" else "delf"
        org = [norm(r) for r in rows if r["k"].startswith("Organisme")]
        cs = [norm(r) for r in rows if not r["k"].startswith("Organisme")]
        out = {"country": pays, "type": t, "key": "Centre de passation" if t == "tcf" else "Centre d'examen",
               "n": len(cs), "date": date, "source": "FEI, liste par pays (extraction structurée v2)",
               "org": org[0] if org else None, "centres": cs}
        path = os.path.join(HERE, f"{t}_{FILE[pays]}.json")
        json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        dropped = sum(len([e for m in r["m"] for e in re.split(r"[,;\s]+", m) if e and "@" in e]) for r in rows) - sum(len(c["emails"]) for c in cs + org)
        print(f"{pays:12} {t:5} {len(cs):3} centres  org={'oui' if org else 'non'}  so={sum(c['so'] for c in cs):2}  e-mails gardés={sum(len(c['emails']) for c in cs):3}  écartés={dropped}")


if __name__ == "__main__":
    main()
