# -*- coding: utf-8 -*-
"""La coupe du 06/11/2026 (SEO_PLAN_CORRECTION_2026-11-03.md, §3 A) : 43 pages sur 222 quittent l'index.

REDIRECTS : chemin coupé → (cible, libellé, langue). GitHub Pages n'a pas de 301 : la page reste une page de renvoi
(meta refresh + canonical vers la cible), écrite par coupe.py. article_template.build() ne rend plus ces pages, et
renvoie tout lien interne vers la cible, de sorte qu'une régénération ne les rouvre pas. Les faits de ces pages vivent
maintenant dans la cible (hubs_absorbes.py) : les fiches de villes_config.py et d'articles_*.py restent comme données.

Les pages coupées par noindex (FEI, /en/tcf-canada-lebanon/, /questions/) sont dans noindex.txt, pas ici.
Rouvrir une page : retirer sa ligne ici, relancer le générateur, coupe.py, sitemap_sync.py.
"""
MA = "/centres/tcf-maroc/"
DZ = "/centres/tcf-algerie/"
TN = "/centres/tcf-tunisie/"
TCF_FR = "/blog/ou-passer-le-tcf-canada-en-france/"
DELF_FR = "/blog/ou-passer-le-delf-en-france/"
DELF_ES = "/es/delf-espana/"

REDIRECTS = {
    # Maroc : 11 villes
    "/centres/tcf-casablanca/": (MA + "#casablanca", "TCF à Casablanca", "fr"),
    "/centres/tcf-rabat/": (MA + "#rabat", "TCF à Rabat", "fr"),
    "/centres/tcf-marrakech/": (MA + "#marrakech", "TCF à Marrakech", "fr"),
    "/centres/tcf-tanger/": (MA + "#tanger", "TCF à Tanger", "fr"),
    "/centres/tcf-fes/": (MA + "#fes", "TCF à Fès", "fr"),
    "/centres/tcf-agadir/": (MA + "#agadir", "TCF à Agadir", "fr"),
    "/centres/tcf-kenitra/": (MA + "#kenitra", "TCF à Kénitra", "fr"),
    "/centres/tcf-meknes/": (MA + "#meknes", "TCF à Meknès", "fr"),
    "/centres/tcf-el-jadida/": (MA + "#el-jadida", "TCF à El Jadida", "fr"),
    "/centres/tcf-tetouan/": (MA + "#tetouan", "TCF à Tétouan", "fr"),
    "/centres/tcf-oujda/": (MA + "#oujda", "TCF à Oujda", "fr"),
    # Algérie hors Alger : Tlemcen d'office ; Oran, Constantine et Annaba selon le test du plan (voir ANTENNES_A_TESTER)
    "/centres/tcf-tlemcen/": (DZ + "#tlemcen", "TCF à Tlemcen", "fr"),
    # Tunisie
    "/centres/tcf-sousse/": (TN + "#sousse", "TCF à Sousse", "fr"),
    "/centres/tcf-beja/": (TN + "#beja", "TCF à Béja", "fr"),
    # France, TCF hors Paris
    "/centres/tcf-lyon/": (TCF_FR + "#lyon", "TCF à Lyon", "fr"),
    "/centres/tcf-montpellier/": (TCF_FR + "#montpellier", "TCF à Montpellier", "fr"),
    "/centres/tcf-rennes/": (TCF_FR + "#rennes", "TCF à Rennes", "fr"),
    "/centres/tcf-strasbourg/": (TCF_FR + "#strasbourg", "TCF à Strasbourg", "fr"),
    "/centres/tcf-lille/": (TCF_FR + "#lille", "TCF à Lille", "fr"),
    "/centres/tcf-nice/": (TCF_FR + "#nice", "TCF à Nice", "fr"),
    # France, DELF
    "/centres/delf-lyon/": (DELF_FR + "#lyon", "DELF à Lyon", "fr"),
    "/centres/delf-lille/": (DELF_FR + "#lille", "DELF à Lille", "fr"),
    "/centres/delf-nantes/": (DELF_FR + "#nantes", "DELF à Nantes", "fr"),
    "/centres/delf-montpellier/": (DELF_FR + "#montpellier", "DELF à Montpellier", "fr"),
    "/centres/delf-strasbourg/": (DELF_FR + "#strasbourg", "DELF à Strasbourg", "fr"),
    # Espagne, DELF par ville
    "/es/delf-madrid/": (DELF_ES + "#madrid", "DELF en Madrid", "es"),
    "/es/delf-barcelona/": (DELF_ES + "#barcelona", "DELF en Barcelona", "es"),
    "/es/delf-sevilla/": (DELF_ES + "#sevilla", "DELF en Sevilla", "es"),
    "/es/delf-valencia/": (DELF_ES + "#valencia", "DELF en Valencia", "es"),
    "/es/delf-granada/": (DELF_ES + "#granada", "DELF en Granada", "es"),
    "/es/delf-malaga/": (DELF_ES + "#malaga", "DELF en Málaga", "es"),
    "/es/delf-zaragoza/": (DELF_ES + "#zaragoza", "DELF en Zaragoza", "es"),
    # Guides sur la même requête que le hub du pays
    "/blog/tcf-canada-maroc/": (MA, "TCF Canada au Maroc", "fr"),
    "/blog/tcf-canada-algerie/": (DZ, "TCF Canada en Algérie", "fr"),
    "/blog/tcf-canada-tunisie/": (TN, "TCF Canada en Tunisie", "fr"),
    "/blog/ifal-tcf-rendez-vous/": (DZ, "Rendez-vous TCF en Algérie", "fr"),
}

# Antennes que le plan demande de tester avant de les couper : gardées si elles passent sous 40 % de phrases partagées.
# Voir le résultat dans SEO_CORRECTION_2026-11-03_EXECUTION.md.
ANTENNES_A_TESTER = {
    "/centres/tcf-oran/": (DZ + "#oran", "TCF à Oran", "fr"),
    "/centres/tcf-constantine/": (DZ + "#constantine", "TCF à Constantine", "fr"),
    "/centres/tcf-annaba/": (DZ + "#annaba", "TCF à Annaba", "fr"),
}

TITRES_CIBLES = {
    MA: "Centres TCF au Maroc", DZ: "Centres TCF en Algérie", TN: "Centres TCF en Tunisie",
    TCF_FR: "Où passer le TCF Canada en France ?", DELF_FR: "Où passer le DELF en France ?",
    DELF_ES: "DELF y DALF en España",
}
