#!/usr/bin/env python3
"""Liste FEI monde (26/10/2026) : tous les pays de la liste officielle FEI → data/fei_monde/<type>_<slug>.json.

Même entrée que parse_fei_v2.py (JSON {"date", "data": {"<Pays>|<tcf|delf_dalf>": [fiche…]}}, fiches
k, h, a, t, m, w, so, plus p = pays écrit sur la fiche et pid = son id FEI), produite par le JS
d'extraction lancé dans le navigateur intégré sur france-education-international.fr (fetch
séquentiel de /centres-d-examen/liste?pays=<id>&type-centre=<tcf|delf_dalf>, DOMParser).

Sortie : le schéma exact de data/tcf_suisse.json (country, type, key, n, date, source, org,
centres[name, city, cp, city_cp, address, address_lines, phone, emails, url, so]) + « iso2 » et
« fei_id » ; manifest.json. Réutilise parse_fei_v2 (norm : nom, ville, adresse, téléphone, site)
sans le modifier ; seul le tri des e-mails est plus strict ici (liste blanche de jetons de service
entiers, jamais un prénom.nom ; dans le doute, l'adresse est écartée).

Usage : python3 _build/data/parse_fei_monde.py <brut1.json> [<brut2.json> …]
        (les fichiers bruts sont cumulés ; le manifeste décrit tous les pays lus)
        python3 _build/data/parse_fei_monde.py --tef <tef_carte.json> <tef_fiches.json>   → data/tef_monde/
"""
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import parse_fei_v2 as v2  # noqa: E402  (norm, clean, ALLOW, DENY : inchangés)

OUT = os.path.join(HERE, "fei_monde")
DATE = "2026-10-26"
SOURCE = "FEI, liste par pays (extraction structurée v2, monde)"
URL_PATTERN = "https://www.france-education-international.fr/centres-d-examen/liste?pays=<fei_id>&type-centre=<tcf|delf_dalf>"

# Les 176 pays des deux menus FEI (TCF : 126, DELF-DALF : 175) au 26/10/2026 → ISO 3166-1 alpha-2.
ISO2 = {
    "Afghanistan": "AF", "Afrique du Sud": "ZA", "Albanie": "AL", "Algérie": "DZ", "Allemagne": "DE",
    "Andorre": "AD", "Angola": "AO", "Arabie saoudite": "SA", "Argentine": "AR", "Arménie": "AM",
    "Australie": "AU", "Autriche": "AT", "Azerbaïdjan": "AZ", "Bahamas": "BS", "Bahreïn": "BH",
    "Bangladesh": "BD", "Barbade": "BB", "Belgique": "BE", "Bénin": "BJ", "Biélorussie": "BY",
    "Birmanie": "MM", "Bolivie": "BO", "Bosnie-Herzégovine": "BA", "Botswana": "BW", "Brésil": "BR",
    "Brunéi Darussalam": "BN", "Bulgarie": "BG", "Burkina Faso": "BF", "Burundi": "BI", "Cambodge": "KH",
    "Cameroun": "CM", "Canada": "CA", "Cap Vert": "CV", "Chili": "CL", "Chine": "CN", "Chine (Taïwan)": "TW",
    "Chypre": "CY", "Colombie": "CO", "Comores": "KM", "Congo": "CG", "Corée du Sud": "KR",
    "Costa Rica": "CR", "Côte d'Ivoire": "CI", "Croatie": "HR", "Cuba": "CU", "Danemark": "DK",
    "Djibouti": "DJ", "Dominique": "DM", "Égypte": "EG", "Émirats arabes unis": "AE", "Équateur": "EC",
    "Érythrée": "ER", "Espagne": "ES", "Estonie": "EE", "Eswatini": "SZ", "États-Unis": "US",
    "Éthiopie": "ET", "Fidji": "FJ", "Finlande": "FI", "France": "FR", "Gabon": "GA", "Gambie": "GM",
    "Géorgie": "GE", "Ghana": "GH", "Grèce": "GR", "Grenade": "GD", "Guatemala": "GT", "Guinée": "GN",
    "Guinée Équatoriale": "GQ", "Guinée-Bissau": "GW", "Guyana": "GY", "Haïti": "HT", "Honduras": "HN",
    "Hongrie": "HU", "Inde": "IN", "Indonésie": "ID", "Irak": "IQ", "Iran": "IR", "Irlande": "IE",
    "Islande": "IS", "Israël": "IL", "Italie": "IT", "Jamaïque": "JM", "Japon": "JP", "Jordanie": "JO",
    "Kazakhstan": "KZ", "Kenya": "KE", "Kirghizistan": "KG", "Koweït": "KW",
    "Lao, République Démocratique populaire": "LA", "Lesotho": "LS", "Lettonie": "LV", "Liban": "LB",
    "Lituanie": "LT", "Luxembourg": "LU", "Macédoine du nord": "MK", "Madagascar": "MG", "Malaisie": "MY",
    "Malawi": "MW", "Maldives": "MV", "Mali": "ML", "Malte": "MT", "Maroc": "MA", "Maurice": "MU",
    "Mauritanie": "MR", "Mexique": "MX", "Moldavie": "MD", "Monaco": "MC", "Mongolie": "MN",
    "Monténégro": "ME", "Mozambique": "MZ", "Namibie": "NA", "Népal": "NP", "Nicaragua": "NI",
    "Niger": "NE", "Nigéria": "NG", "Norvège": "NO", "Nouvelle-Zélande": "NZ", "Oman": "OM",
    "Ouganda": "UG", "Ouzbékistan": "UZ", "Pakistan": "PK", "Palestine": "PS", "Panama": "PA",
    "Paraguay": "PY", "Pays-Bas": "NL", "Pérou": "PE", "Philippines": "PH", "Pologne": "PL",
    "Porto Rico": "PR", "Portugal": "PT", "Qatar": "QA", "République Centrafricaine (RCA)": "CF",
    "République Tchèque": "CZ", "République démocratique du Congo": "CD", "République dominicaine": "DO",
    "Roumanie": "RO", "Royaume-Uni": "GB", "Russie": "RU", "Rwanda": "RW", "Saint-Kitts-et-Nevis": "KN",
    "Saint-Vincent-et-les-Grenadines": "VC", "Sainte-Lucie et les états membres de l'OECO": "LC",
    "Salvador": "SV", "Sao Tomé-et-Principe": "ST", "Sénégal": "SN", "Serbie": "RS", "Seychelles": "SC",
    "Sierra Leone": "SL", "Singapour": "SG", "Slovaquie": "SK", "Slovénie": "SI", "Somalie": "SO",
    "Soudan": "SD", "Soudan du Sud": "SS", "Sri Lanka": "LK", "Suède": "SE", "Suisse": "CH",
    "Suriname": "SR", "Tadjikistan": "TJ", "Tanzanie": "TZ", "Tchad": "TD", "Thaïlande": "TH",
    "Togo": "TG", "Tonga": "TO", "Trinité et Tobago": "TT", "Tunisie": "TN", "Turkménistan": "TM",
    "Turquie": "TR", "Ukraine": "UA", "Uruguay": "UY", "Vanuatu": "VU", "Venezuela": "VE",
    "Vietnam": "VN", "Zambie": "ZM", "Zimbabwe": "ZW",
}

EUROPE = {"Albanie", "Allemagne", "Andorre", "Arménie", "Autriche", "Azerbaïdjan", "Belgique", "Biélorussie",
          "Bosnie-Herzégovine", "Bulgarie", "Chypre", "Croatie", "Danemark", "Espagne", "Estonie", "Finlande",
          "France", "Géorgie", "Grèce", "Hongrie", "Irlande", "Islande", "Italie", "Lettonie", "Lituanie",
          "Luxembourg", "Macédoine du nord", "Malte", "Moldavie", "Monaco", "Monténégro", "Norvège", "Pays-Bas",
          "Pologne", "Portugal", "République Tchèque", "Roumanie", "Royaume-Uni", "Russie", "Serbie",
          "Slovaquie", "Slovénie", "Suède", "Suisse", "Turquie", "Ukraine"}
# Les membres de la Ligue arabe que FEI liste (Libye, Syrie et Yémen n'y sont pas au 26/10/2026).
MONDE_ARABE = {"Algérie", "Arabie saoudite", "Bahreïn", "Comores", "Djibouti", "Égypte", "Émirats arabes unis",
               "Irak", "Jordanie", "Koweït", "Liban", "Maroc", "Mauritanie", "Oman", "Palestine", "Qatar",
               "Somalie", "Soudan", "Tunisie"}
AMERIQUES = {"Argentine", "Bahamas", "Barbade", "Bolivie", "Brésil", "Canada", "Chili", "Colombie", "Costa Rica",
             "Cuba", "Dominique", "Équateur", "États-Unis", "Grenade", "Guatemala", "Guyana", "Haïti", "Honduras",
             "Jamaïque", "Mexique", "Nicaragua", "Panama", "Paraguay", "Pérou", "Porto Rico",
             "République dominicaine", "Saint-Kitts-et-Nevis", "Saint-Vincent-et-les-Grenadines",
             "Sainte-Lucie et les états membres de l'OECO", "Salvador", "Suriname", "Trinité et Tobago",
             "Uruguay", "Venezuela"}
ASIE_OCEANIE = {"Afghanistan", "Australie", "Bangladesh", "Birmanie", "Brunéi Darussalam", "Cambodge", "Chine",
                "Chine (Taïwan)", "Corée du Sud", "Fidji", "Inde", "Indonésie", "Japon", "Kazakhstan",
                "Kirghizistan", "Lao, République Démocratique populaire", "Malaisie", "Maldives", "Mongolie",
                "Népal", "Nouvelle-Zélande", "Ouzbékistan", "Pakistan", "Philippines", "Singapour", "Sri Lanka",
                "Tadjikistan", "Thaïlande", "Tonga", "Turkménistan", "Vanuatu", "Vietnam"}
MOYEN_ORIENT = {"Iran", "Israël"}


def region(pays):
    for name, s in (("europe", EUROPE), ("monde_arabe", MONDE_ARABE), ("ameriques", AMERIQUES),
                    ("asie_oceanie", ASIE_OCEANIE), ("moyen_orient", MOYEN_ORIENT)):
        if pays in s:
            return name
    return "afrique"


def fold(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def slug(pays):
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", fold(pays))).strip("_")


# --- E-mails -------------------------------------------------------------------------------------
# Plus strict que v2.ok_email : un jeton ENTIER de la partie locale (découpée sur . _ - + et les
# chiffres) doit être un mot de service, ou bien la partie locale entière est un nom de ville /
# d'antenne de la fiche (« ahmedabad@afindia.org »). Un prénom.nom n'a aucun de ces jetons → écarté.
SERVICE = {
    # français
    "info", "infos", "information", "informations", "contact", "contacts", "examen", "examens", "exam",
    "exams", "certif", "certification", "certifications", "delf", "dalf", "delfdalf", "dalfdelf", "tcf",
    "dilf", "test", "tests", "testing", "secretariat", "secretaire", "accueil", "reception", "admin",
    "administration", "administratif", "administrative", "direction", "directeur", "directrice", "dir",
    "pedagogie", "pedagogique", "cours", "inscription", "inscriptions", "inscri", "etudiants", "alliance",
    "alliancefrancaise", "alliancefr", "af", "if", "ifa", "idf", "institut", "institutfrancais",
    "campusfrance", "campus", "centre", "cdl", "cla", "cel", "cuef", "fle", "defle", "langues", "francais",
    "bureau", "mediatheque", "bibliotheque", "culture", "culturel", "ecole", "academie", "education",
    "formation", "formations", "coordination", "coordinateur", "coordinatrice", "programmes", "bonjour",
    "service", "services", "courriel", "general", "communication", "scac", "scelf", "scel", "bcle",
    "cooperation", "ambafrance", "consulat", "presidence", "president", "departement", "faculte",
    "universite", "lycee", "college", "proviseur", "proviseure", "censeur", "commercial", "international",
    "internationale", "intl", "relations", "assistant", "assistante", "gestion", "gestioncentrale",
    "casnav", "greta", "centredexamen", "centredexamens", "scolarite", "sco", "list", "plateforme",
    "agence", "primaire", "elementaire", "secondaire", "maternelle", "ce", "association", "ressources",
    "france", "teacher", "teachers", "enseignants", "vie", "scolaire", "tef", "tefaq", "dfp", "coordo", "queries", "query",
    # anglais
    "examination", "examinations", "registration", "registrations", "register", "enrolment",
    "enrollment", "admissions", "students", "student", "languages", "language", "french", "office",
    "library", "school", "academy", "training", "learning", "coordinator", "programs", "courses",
    "course", "classes", "hello", "welcome", "enquiries", "enquiry", "inquiries", "inquiry", "help",
    "helpdesk", "support", "mail", "email", "department", "dept", "faculty", "university", "uni",
    "center", "examcentre", "examcenter", "examoffice", "examsoffice", "testcentre", "testcenter",
    "languagecenter", "languagecentre", "langcenter", "secretary", "reception", "principal", "head",
    # espagnol, portugais, italien
    "informes", "informacion", "informaciones", "contacto", "examenes", "certificacion",
    "certificaciones", "secretaria", "secretariado", "recepcion", "administracion", "direccion",
    "director", "directora", "cursos", "curso", "inscripciones", "idiomas", "lenguas", "frances",
    "alianza", "alianzafrancesa", "instituto", "centro", "oficina", "biblioteca", "mediateca", "cultura",
    "cultural", "escuela", "academia", "educacion", "coordinacion", "programas", "hola", "servicios",
    "atencion", "departamento", "facultad", "universidad", "colegio", "admisiones", "dele",
    "informacoes", "contato", "contatos", "exames", "exame", "certificacao", "secretaria", "recepcao",
    "administracao", "direcao", "diretoria", "escola", "educacao", "coordenacao", "servicos",
    "atendimento", "geral", "aliancafrancesa", "esami", "esame", "certificazioni", "certificazione",
    "segreteria", "direzione", "corsi", "lingue", "ufficio", "scuola", "pedagogia", "didattica",
    "amministrazione", "informazioni",
    # langues d'Europe centrale et du Nord, turc, russe translittéré
    "kontakt", "pruefung", "prufung", "pruefungen", "prufungen", "sekretariat", "kurse", "sprachen",
    "schule", "kultur", "buero", "buro", "verwaltung", "anmeldung", "egzaminy", "egzamin", "kursy",
    "kurs", "biuro", "informacja", "sinavlar", "sinav", "kurslar", "bilgi", "iletisim", "cursus",
    "cursussen", "opleiding", "secretariaat", "administratie", "examene", "cursuri", "inscrieri",
    "kurzy", "zkousky", "titkarsag", "vizsga", "kurzus", "kansli", "expedition", "kurser", "kanslia",
    "toimisto", "kursevi", "ispiti", "ekzamen", "ekzameny", "lukio", "koulu", "gymnasium", "gymnasiet",
    "skola", "skole", "liceo", "liceum", "lyceum", "gimnazjum", "scoala", "aliantafranceza",
    "aleancafranceze", "francuski", "francais", "francuskizaodrasle",
}
PARTICLES = {"de", "du", "des", "di", "del", "da", "la", "le", "les", "do", "dos", "das", "et", "of"}
# Mots de service qui commencent aussi des prénoms (« francesca », « delfina ») : jamais suivis d'un code.
NAMEY = {"frances", "france", "franco", "francais", "academia", "general", "centro", "centre", "delf",
         "dalf", "info", "dir", "uni", "head", "vie", "kurs", "if", "af", "ifa", "ce", "sco"}
STOP = PARTICLES | {"d", "l", "the", "and", "fur", "y", "e", "en", "a", "au", "aux"}

# Revu à la main le 26/10/2026 : clés ajoutées après lecture de la liste « à revoir » imprimée par
# ce script. ALLOW_MONDE : adresses de service que les règles ne reconnaissent pas (acronymes,
# langues locales) ; DENY_MONDE : adresses que les règles gardent mais qui portent un nom de personne.
ALLOW_MONDE = {
    # Europe
    "info.muenchen@institutfrancais.de", "info.hamburg@institutfrancais.de", "puc@kuleuven.be",
    "examens.barcelona@institutfrancais.es", "examenes.valencia@institutfrancais.es", "lukio.sampo@tampere.fi",
    "mlangues-delfdalf@unilim.fr", "ief@unistra.fr", "sec-sel@univ-paris13.fr", "infrep6f@infrep.org",
    "commercial.greta.agence-larochelle@ac-poitiers.fr", "contact.infrepdordogne@infrep.org",
    "idf.developpement@leolagrange.org", "esami-milano@institutfrancais.it", "ifm@institutfrancais.me",
    "opleiding.leraarfrans@han.nl", "scc@ifrussie.ru", "direction.bohemedusud@alliancefrancaise.cz",
    "proviseur.adjoint@lfp.cz",
    # Monde arabe
    "info.tcfalg@vfshelpline.com", "certifications.casa@ifmaroc.com", "certification.eljadida@ifmaroc.com",
    "contact.af.ozte@gmail.com", "contact.oujda@ifmaroc.com", "afm.atar@gmail.com",
    "direction.afmkiffa03@gmail.com", "afk.kairouan@gmail.com", "accueil.alex@ifegypte.com",
    "cours.alex@ifegypte.com",
    # Reste du monde
    "directrice.bloem@alliancefr.co.za", "alianzafrancesa.cdelu@gmail.com", "asistente.afcochabamba@gmail.com",
    "adjoint.proviseur@francobolivien.edu.bo", "coordopeda.afcochabamba@gmail.com",
    "executive.director@afbrunei.org", "dri@ufu.br", "exames.oficiais@affortaleza.com",
    "education.saskatoon@collegemathieu.sk.ca", "lesberges-tcf_tef@csslaval.gouv.qc.ca", "fc@uqat.ca",
    "info2.nanjing@afchine.org", "examens.beijing@afchine.org", "accueil.xian@afchine.org",
    "test.guangzhou@campusfrancechine.org", "test.beijing@campusfrancechine.org", "examens.xian@afchine.org",
    "secretariat1.afstgo@gmail.com", "pedagogie.afdominique@gmail.com", "director.afgrenada@gmail.com",
    "directeur.afpondy@afindia.org", "ifjrg.exam@gmail.com", "fr-off@gakushuin.ac.jp",
    "peda.afambositra@gmail.com", "direction.afdiego@gmail.com", "delfdalf.malaisie@gmail.com",
    "peb1097@moe.edu.my", "cra5001@moe.edu.my", "bra7011@moe.edu.my", "bra6001@moe.edu.my",
    "tea6090@moe.edu.my", "aea6050@moe.edu.my",            # boîtes d'établissement du ministère malaisien
    "certificaciones.ceicln@uas.edu.mx", "resp.delfdalf@alianzafrancesagdl.mx",
    "centroidiomas.valla@gmail.com", "coord.dpto.idiomas.sria.acad@umich.mx",
    "direction.academique@alianzafrancesa.org.pe", "coordinacion.pedagogica@afsantiago.org.do",
    "direction.afskn@gmail.com", "dg@afslu.org", "calf.ndj@gmail.com", "coordinacion.afmcbo@gmail.com",
    "immersion.programs@pgcps.org", "afd@afdetroit.org", "aef@allianceaddis.org",
    # TEF (fiches CCI)
    "da.alliance.fianar@gmail.com", "accueil.afpondy@afindia.org", "accueil.wuchang@afchine.org",
    "tef.mumbai@afindia.org", "accueil_skillfor@martinique.cci.fr", "accueil.nantes@cfp-presquile.com",
    "ctd@dawsoncollege.qc.ca", "dfp.faj@euba.sk", "par@lsi.edu", "fc@collegeboreal.ca",
    "contact.zdacademy@gmail.com", "contact.lehavre@educationetformation.fr", "pdl@leolagrange-formation.fr",
    "cvl@leolagrange-formation.fr", "afverona.dfp.tef@gmail.com", "tef-ciaf@umoncton.ca",
}
DENY_MONDE = {"mai.thi.nhi@ifv.vn"}          # prénom vietnamien sans séparateur reconnu

# Fiches FEI sans « Ville - » ni adresse : ville lue dans le nom que FEI écrit, sinon laissée vide.
CITY_FROM_NAME = {("Malaisie", "SMK St Joseph Miri"): "Miri"}


def fold2(s):
    """Translittération allemande (ü → ue) en plus du pliage simple : « muenchen » = « München »."""
    return fold(s.replace("ü", "ue").replace("ö", "oe").replace("ä", "ae").replace("Ü", "Ue")
                .replace("Ö", "Oe").replace("Ä", "Ae").replace("ß", "ss"))


def tokens(local):
    return [t for t in re.split(r"[._\-+0-9]+", fold(local)) if t]


def place_words(card):
    """Mots du lieu : l'intitulé FEI (« Ville - Nom ») et la dernière ligne d'adresse (code postal + ville),
    pas les lignes de rue (une rue porte souvent un nom de personne)."""
    words = set()
    lines = list(card.get("a", []))
    for s in [card.get("h", "")] + lines[-1:]:
        for f in (fold, fold2):
            for w in re.split(r"[^a-z]+", f(s)):
                if len(w) >= 3 and w not in STOP:
                    words.add(w)
    return words


def acronyms(card):
    h = card.get("h", "")
    parts = [p for p in re.split(r"\s+-\s+", h) if p.strip()]
    out = set()
    for seg in parts + [" ".join(parts[1:])]:
        ws = [w for w in re.split(r"[^a-z]+", fold(seg)) if w]
        for cand in ("".join(w[0] for w in ws), "".join(w[0] for w in ws if w not in STOP)):
            if len(cand) >= 2:
                out.add(cand)
    return out


def domain_words(domain):
    labels = domain.split(".")[:-1]
    out = set()
    for lab in labels:
        out.add(lab.replace("-", ""))
        out |= {p for p in lab.split("-") if len(p) >= 3}
    return {w for w in out if len(w) >= 3}


def segment(t, vocab):
    """Découpe un jeton accolé (« delfdalf », « examenscasablanca », « afdeszeged ») en mots connus."""
    best = {0: []}
    for i in range(len(t)):
        if i not in best:
            continue
        for j in range(i + 2, len(t) + 1):
            if t[i:j] in vocab and j not in best:
                best[j] = best[i] + [t[i:j]]
    return best.get(len(t))


def classify(t, places, dom, acr):
    """S = service, P = lieu/organisme, C = code court, U = inconnu (prénom, nom…)."""
    if t in SERVICE:
        return "S"
    if t in places or t in dom or t in acr:
        return "P"
    if len(t) <= 3:
        return "C"
    seg = segment(t, SERVICE | places | dom | PARTICLES)
    if seg and seg[0] not in PARTICLES and seg[-1] not in PARTICLES:
        svc = [p for p in seg if p in SERVICE]
        if svc and (any(len(p) >= 4 for p in svc) or any(p in places or p in dom for p in seg)):
            return "S"
        if all(p in places or p in dom for p in seg):
            return "P"
    for k in range(len(t) - 1, len(t) - 4, -1):            # service accolé à un code (« alliancefrancaisebv »)
        head = t[:k]
        sh = segment(head, SERVICE | PARTICLES) if len(head) >= 6 else None
        if sh and sh[-1] not in NAMEY and sh[0] not in PARTICLES and any(p in SERVICE for p in sh):
            return "S"
    return "U"


def email_verdict(e, card):
    """(garder ?, raison). 'review' = écarté mais plausible : imprimé pour relecture à la main."""
    e = e.strip().strip(".").strip()
    low = e.lower()
    if not e or low == "null" or "@" not in e or low.count("@") != 1 or "www." in low.split("@")[0]:
        return False, "malformed"
    if low in DENY_MONDE or low in v2.DENY:
        return False, "deny"
    if low in ALLOW_MONDE or low in v2.ALLOW:
        return True, "allow"
    local, domain = low.split("@")
    toks = tokens(local)
    if not toks:
        return False, "no-token"
    dom, acr = domain_words(domain), acronyms(card)
    compact = re.sub(r"[^a-z0-9]", "", fold(local))
    if compact in dom or compact in acr:
        return True, "org"               # « dsh@dsh.fi », « lcf@… » (Lycée Comte de Foix)
    cls = [classify(t, place_words(card), dom, acr) for t in toks]
    if "U" in cls:
        return False, ("review" if "S" in cls else "person-like")
    if "S" in cls:
        return True, "service"
    if all(c == "P" for c in cls):
        return True, "place"             # « montreux@alpadia.com », « ahmedabad@afindia.org »
    return False, "review"               # codes seuls (« oic@… », « ctp.mainz@… »)


def split_emails(field_values):
    out = []
    for m in field_values:
        for e in re.split(r"[,;\s/]+", m):
            if "@" in e:
                out.append(e.strip().strip(".").strip())
    return out


# --- Fiches ---------------------------------------------------------------------------------------
def city_fallback(lines):
    """Ville tirée de la dernière ligne d'adresse quand l'intitulé FEI n'a pas « Ville - Nom »."""
    if not lines:
        return ""
    last = re.sub(r"\b[A-Z]{0,3}-?\d[\d\- ]{2,}\b", " ", lines[-1])
    last = re.sub(r"\s+", " ", last).strip(" ,-")
    return last


def card_to_centre(r, log, pays=""):
    h = v2.clean(r.get("h", ""))
    if h.startswith("-"):                # « - FOURAH BAY COLLEGE » : FEI n'a pas rempli la ville
        r = {**r, "h": re.sub(r"^-\s*", "", h)}
    c = v2.norm({**r, "m": []})          # nom, ville, adresse, téléphone, site : exactement v2
    hh = v2.clean(r.get("h", ""))
    if pays != "Brésil" and re.match(r"^(.*?) - ([A-Z]{2}) - (.*)$", hh):
        # v2 lit « Ville - XX - Nom » comme un État brésilien ; ailleurs, « IS » est le début du nom
        # (« Aix-en-Provence - IS - Institut international de langue »).
        city, name = hh.split(" - ", 1)
        c["city"], c["name"] = v2.clean(city).rstrip(","), v2.clean(name)
    if not c["city"] and (pays, c["name"]) in CITY_FROM_NAME:
        c["city"] = CITY_FROM_NAME[(pays, c["name"])]
    emails = []
    for e in split_emails(r.get("m", [])):
        keep, why = email_verdict(e, r)
        log.append((e, keep, why, c["name"], c["city"]))
        if keep and e.lower() not in [x.lower() for x in emails]:
            emails.append(e)
    c["emails"] = emails
    if not c["city"] and c["address_lines"]:
        c["city"] = city_fallback(c["address_lines"])
    return c


def nkey(c):
    return (re.sub(r"[^a-z0-9]+", " ", fold(c["name"])).strip(), re.sub(r"[^a-z0-9]+", " ", fold(c["city"])).strip())


def write_country(pays, typ, rows, fei_id, email_log, anomalies):
    t = "tcf" if typ == "tcf" else "delf"
    for r in rows:
        if r.get("p") and r["p"] != pays:
            anomalies.append(f"{pays}|{typ}: fiche du pays « {r['p']} » : {r.get('h')}")
    orgs_raw = [r for r in rows if r["k"].startswith("Organisme")]
    cs_raw = [r for r in rows if not r["k"].startswith("Organisme")]
    if len(orgs_raw) > 1:
        anomalies.append(f"{pays}|{typ}: {len(orgs_raw)} organismes de gestion (seul le 1er est gardé)")
    org = [card_to_centre(r, email_log, pays) for r in orgs_raw]
    if org and not (org[0]["name"] or org[0]["address"] or org[0]["phone"] or org[0]["emails"] or org[0]["url"]):
        anomalies.append(f"{pays}|{typ}: organisme de gestion centrale affiché vide (« - ») → org = null")
        org = []
    cs, seen = [], {}
    for r in cs_raw:
        c = card_to_centre(r, email_log, pays)
        sig = (nkey(c), fold(c["address"]), c["phone"])
        if sig in seen:
            anomalies.append(f"{pays}|{typ}: doublon exact écarté : {c['city']} - {c['name']}")
            continue
        if nkey(c) in [nkey(x) for x in cs]:
            anomalies.append(f"{pays}|{typ}: même nom+ville, fiches différentes (gardées) : {c['city']} - {c['name']}")
        seen[sig] = 1
        cs.append(c)
    out = {"country": pays, "iso2": ISO2[pays], "fei_id": str(fei_id), "type": t,
           "key": "Centre de passation" if t == "tcf" else "Centre d'examen",
           "n": len(cs), "date": DATE, "source": SOURCE, "org": org[0] if org else None, "centres": cs}
    if not cs and not org:
        return out, None
    path = os.path.join(OUT, f"{t}_{slug(pays)}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out, os.path.basename(path)


def main(paths):
    os.makedirs(OUT, exist_ok=True)
    data, meta, batches = {}, {}, []
    for p in paths:
        src = json.load(open(p, encoding="utf-8"))
        data.update(src["data"])
        meta.update(src.get("meta", {}))
        batches.append(src.get("batch", os.path.basename(p)))
    unknown = sorted({k.split("|")[0] for k in data} - set(ISO2))
    if unknown:
        sys.exit(f"Pays sans code ISO : {unknown}")
    email_log, anomalies, countries = [], [], {}
    for key in sorted(data):
        pays, typ = key.split("|")
        fei_id = meta.get(key, {}).get("id", "")
        if meta.get(key, {}).get("failed"):
            anomalies.append(f"{key}: extraction en échec")
            continue
        out, fname = write_country(pays, typ, data[key], fei_id, email_log, anomalies)
        e = countries.setdefault(pays, {"name_fr": pays, "iso2": ISO2[pays], "fei_id": str(fei_id),
                                        "region": region(pays), "tcf": 0, "delf": 0, "files": []})
        e["tcf" if typ == "tcf" else "delf"] = out["n"]
        if fname:
            e["files"].append(fname)
        cards = len(data[key])
        if cards != out["n"] + (1 if out["org"] else 0):
            anomalies.append(f"{key}: {cards} fiches FEI → {out['n']} centres + org={'oui' if out['org'] else 'non'}")
        if typ == "delf_dalf" and out["n"] and not out["org"]:
            anomalies.append(f"{key}: pas d'organisme de gestion centrale affiché")
        for c in out["centres"] + ([out["org"]] if out["org"] else []):
            ph = c["phone"]
            if ph and (len(re.sub(r"\D", "", ph)) < 6 or re.search(r"[A-Za-z@]", ph)):
                anomalies.append(f"{key}: téléphone atypique « {ph} » ({c['city']} - {c['name']})")
            if not c["city"]:
                anomalies.append(f"{key}: fiche sans ville : {c['name']}")
    # Manifeste
    allc = []
    for pays, e in countries.items():
        for fn in e["files"]:
            d = json.load(open(os.path.join(OUT, fn), encoding="utf-8"))
            allc += [(pays,) + nkey(c) + (re.sub(r"[^a-z0-9]+", " ", fold(c["address"])).strip(),) for c in d["centres"]]
    man = {"date": DATE, "source": "France Éducation international, centres d'examen (liste par pays)",
           "source_url_pattern": URL_PATTERN,
           "batches": batches, "complete": {"europe", "arabe", "reste"} <= set(batches),
           "regions": {"europe": "Europe (dont France, Turquie, Russie, Caucase)", "monde_arabe": "Ligue arabe",
                       "afrique": "Afrique subsaharienne et océan Indien", "ameriques": "Amériques et Caraïbes",
                       "asie_oceanie": "Asie et Océanie", "moyen_orient": "Iran, Israël"},
           "countries": sorted(countries.values(), key=lambda e: fold(e["name_fr"])),
           "totals": {"countries": len(countries),
                      "countries_with_centres": sum(1 for e in countries.values() if e["tcf"] or e["delf"]),
                      "tcf_centres": sum(e["tcf"] for e in countries.values()),
                      "delf_centres": sum(e["delf"] for e in countries.values()),
                      "distinct_centres": len({(p, n, c) for p, n, c, a in allc})},
           "anomalies": anomalies}
    for e in man["countries"]:
        e["files"].sort()
    with open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(man, f, ensure_ascii=False, indent=1)
    # Rapport
    by = {}
    for e, keep, why, name, city in email_log:
        by.setdefault(why, []).append((e, name, city))
    print("Totaux :", man["totals"])
    reg = {}
    for e in countries.values():
        r = reg.setdefault(e["region"], [0, 0, 0])
        r[0] += 1; r[1] += e["tcf"]; r[2] += e["delf"]
    print("Par région (pays, TCF, DELF) :", reg)
    print("E-mails :", {k: len(v) for k, v in by.items()})
    for why in ("review",):
        for e, name, city in by.get(why, []):
            print(f"  à revoir (écarté) {e:45} {city} - {name}")
    if os.environ.get("SHOW_DROPPED"):
        for why in ("person-like", "single-unknown", "no-token", "malformed"):
            for e, name, city in by.get(why, []):
                print(f"  écarté [{why}] {e:45} {city} - {name}")
    for a in anomalies:
        print("  !", a)
    return man, anomalies


# --- TEF (Le français des affaires, CCI Paris Île-de-France) ---------------------------------------
# Entrées (navigateur intégré, francais.cci-paris-idf.fr, même origine) :
#  - carte : POST /candidat/search-results (une fois par produit) → attribut data-map-centers = TOUS les
#    centres du réseau TEF/DFP (tc_id, nom, adresse « rue, CP, ville », coordonnées) ; marqueur « blue » =
#    sessions disponibles pour ce produit, « grey » = pas de session publiée (« Contacter le centre »).
#  - fiche contact publique de chaque centre : /inscription-candidat/contact/<tc_id> (adresse avec le pays,
#    téléphone, e-mail, site web).
TEF_OUT = os.path.join(HERE, "tef_monde")
TEF_PRODUCTS = {"3": "TEF", "2": "TEF Canada", "4": "TEF Québec", "20": "TEF IRN"}
TEF_CONTACT = "https://francais.cci-paris-idf.fr/inscription-candidat/contact/{}"
EXTRA_ISO2 = {"Guadeloupe": "GP", "Martinique": "MQ", "Guyane française": "GF", "Guyane": "GF", "Réunion": "RE",
              "La Réunion": "RE", "Mayotte": "YT", "Polynésie française": "PF", "Nouvelle-Calédonie": "NC",
              "Saint-Pierre-et-Miquelon": "PM", "Saint-Martin": "MF", "Saint-Martin (partie française)": "MF",
              "Saint-Barthélemy": "BL", "Wallis-et-Futuna": "WF", "Kosovo": "XK", "Hong Kong": "HK", "Macao": "MO",
              "Taïwan": "TW", "Taiwan": "TW", "Corée, République de": "KR", "Corée du Sud": "KR", "Russie": "RU",
              "Fédération de Russie": "RU", "Viet Nam": "VN", "Viêt Nam": "VN", "Etats-Unis": "US", "États-Unis": "US",
              "Tchéquie": "CZ", "République tchèque": "CZ", "Macédoine du Nord": "MK", "Cap-Vert": "CV",
              "Sainte-Lucie": "LC", "Moldavie, République de": "MD", "Iran, République islamique d'": "IR",
              "Bolivie, État plurinational de": "BO", "Tanzanie, République-Unie de": "TZ", "Congo (RDC)": "CD",
              "Congo, République démocratique du": "CD", "République démocratique du Congo": "CD",
              "Eswatini": "SZ", "Myanmar": "MM", "Birmanie": "MM", "Émirats Arabes Unis": "AE",
              "Emirats arabes unis": "AE", "Bosnie-Herzégovine": "BA", "Trinité-et-Tobago": "TT",
              "Saint-Christophe-et-Niévès": "KN", "Côte d’Ivoire": "CI", "Côte-d'Ivoire": "CI",
              "Congo-Kinshasa": "CD", "Congo-Brazzaville": "CG", "Kirghizstan": "KG"}


def iso_of(name):
    table = {fold(k): v for k, v in list(ISO2.items()) + list(EXTRA_ISO2.items())}
    return table.get(fold(name))


def split_map_address(addr):
    parts = [p.strip() for p in (addr or "").split(",")]
    if len(parts) >= 3:
        street, cp, city = ", ".join(x for x in parts[:-2] if x), parts[-2], parts[-1]
    elif len(parts) == 2:
        street, cp, city = parts[0], "", parts[1]
    else:
        street, cp, city = "", "", parts[0] if parts else ""
    return v2.clean(street), v2.clean(cp), v2.clean(city)


def phone_like(s):
    return bool(s) and bool(re.fullmatch(r"[+()\d][\d\s.\-/()+]{5,}", s)) and len(re.sub(r"\D", "", s)) >= 6


def main_tef(map_path, contact_path):
    os.makedirs(TEF_OUT, exist_ok=True)
    mp = json.load(open(map_path, encoding="utf-8"))
    ct = json.load(open(contact_path, encoding="utf-8"))["res"]
    by_country, anomalies, log = {}, [], []
    for tc, m in sorted(mp["centers"].items(), key=lambda kv: int(kv[0])):
        kv = (ct.get(tc) or {}).get("kv", {})
        pre = (ct.get(tc) or {}).get("pre", "")
        caddr = kv.get("Adresse", "")
        country = caddr.rsplit(" - ", 1)[-1].strip() if " - " in caddr else ""
        iso = iso_of(country) if country else None
        if not iso:
            iso = m.get("geo_iso")
            anomalies.append(f"tc {tc} {m['label']}: pays « {country} » non reconnu → {iso} (coordonnées)")
            country = next((k for k, v in ISO2.items() if v == iso), country or iso or "?")
        fei_name = next((k for k, v in ISO2.items() if v == iso), None)
        if fei_name:
            country = fei_name           # même nom (et même slug) que les fichiers FEI du pays
        street, cp, city = split_map_address(m.get("address", ""))
        if not city:
            anomalies.append(f"tc {tc} {m['label']}: sans ville")
        name = v2.clean(pre.split(" Adresse :")[0]) if " Adresse :" in pre else v2.clean(m["label"])
        tel = kv.get("Téléphone", "")
        tel = "" if tel in ("-", "") else tel
        poste = kv.get("Poste / Contact", "")
        if not tel and phone_like(poste):
            tel = poste
        emails = []
        for e in split_emails([kv.get("Email", "")]):
            keep, why = email_verdict(e, {"h": f"{city} - {name}", "a": [street, f"{cp} {city}"]})
            log.append((e, keep, why, name, city))
            if keep and e.lower() not in [x.lower() for x in emails]:
                emails.append(e)
        url = kv.get("Site web", "")
        url = "" if url in ("-", "") else url
        lines = [x for x in (street, f"{cp} {city}".strip()) if x]
        prods = [TEF_PRODUCTS[p] for p in ("3", "2", "4", "20") if m.get("colors", {}).get(p) == "blue"]
        c = {"name": name, "city": city, "cp": cp, "city_cp": "", "address": ", ".join(lines),
             "address_lines": lines, "phone": tel, "emails": emails, "url": url, "so": False,
             "products": prods, "cci_id": int(tc), "contact": TEF_CONTACT.format(tc)}
        if not ct.get(tc):
            anomalies.append(f"tc {tc} {m['label']}: fiche contact non lue")
        by_country.setdefault((country, iso), []).append(c)
    countries = []
    for (country, iso), cs in sorted(by_country.items(), key=lambda kv: fold(kv[0][0])):
        cs.sort(key=lambda c: (fold(c["city"]), fold(c["name"])))
        out = {"country": country, "iso2": iso, "fei_id": None, "type": "tef", "key": "Centre de passation TEF",
               "n": len(cs), "date": DATE,
               "source": "Le français des affaires (CCI Paris Île-de-France), carte des centres TEF DFP et fiches contact",
               "org": None, "centres": cs}
        fn = f"tef_{slug(country)}.json"
        with open(os.path.join(TEF_OUT, fn), "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
        countries.append({"name_fr": country, "iso2": iso, "tef": len(cs), "files": [fn]})
    allc = [c for cs in by_country.values() for c in cs]
    man = {"date": DATE, "source": "Le français des affaires (CCI Paris Île-de-France)",
           "source_url_pattern": "https://francais.cci-paris-idf.fr/candidat (carte, POST /candidat/search-results) ; "
                                 "fiche : https://francais.cci-paris-idf.fr/inscription-candidat/contact/<cci_id>",
           "products_note": "« products » = épreuves pour lesquelles la carte CCI affichait des sessions disponibles le "
                            "26/10/2026 (marqueur bleu). Liste vide = aucune session publiée : la carte dit « Contacter "
                            "le centre pour connaître les prochaines dates ». La carte ne publie pas la liste des épreuves "
                            "agréées par centre (la recherche par pays renvoie tous les centres quel que soit le produit).",
           "fields_note": "url = site web déclaré par le centre ; contact = page publique « Contacter le centre » (CCI) ; "
                          "cci_id = identifiant du centre sur la plateforme CCI ; e-mails : adresses de service seulement.",
           "countries": countries,
           "totals": {"countries": len(countries), "tef_centres": len(allc),
                      "with_sessions": {p: sum(1 for c in allc if p in c["products"]) for p in TEF_PRODUCTS.values()},
                      "without_published_session": sum(1 for c in allc if not c["products"])},
           "anomalies": anomalies}
    with open(os.path.join(TEF_OUT, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(man, f, ensure_ascii=False, indent=1)
    print("TEF :", man["totals"])
    by = {}
    for e, keep, why, name, city in log:
        by.setdefault(why, []).append((e, name, city))
    print("E-mails :", {k: len(v) for k, v in by.items()})
    for e, name, city in by.get("review", []):
        print(f"  à revoir (écarté) {e:45} {city} - {name}")
    for a in anomalies:
        print("  !", a)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--tef"]:
        main_tef(sys.argv[2], sys.argv[3])
    else:
        main(sys.argv[1:])
