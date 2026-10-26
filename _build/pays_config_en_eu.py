# -*- coding: utf-8 -*-
"""English country pages for Europe (/en/, make_pays.py) — translations of the /centres/ pages of pays_config_eu.py
(26/10/2026): Germany, Switzerland, Belgium, Italy, the Netherlands, Portugal, Romania, Poland, Greece, Ireland.

Same rule as pays_config_en.py: no new facts; every number of the French page is here too (check_i18n parity).
British English (en-GB). Hooked by one line at the end of pays_config_en.py, which also calls hub_patch(HUB) to add
the Europe table to /en/.
"""
from pays_config_eu import PAGES as _FR, table

FR = {p["slug"]: p for p in _FR}
D_EN = "26 October 2026"
BADGES = {"TCF Canada": "TCF Canada", "pas de TCF Canada": "no TCF Canada", "TCF absent du site": "no TCF on its website",
          "aucune session TCF publiée": "no TCF session published", "tout public seulement": "TCF tout public only",
          "dates 2025 seulement": "2025 dates only", "sur demande": "on request"}
OG = {"tcf-allemagne": "en_DE", "delf-allemagne": "en_DE", "tcf-suisse": "en_CH", "delf-suisse": "en_CH", "tcf-belgique": "en_BE",
      "tcf-italie": "en_IT", "tcf-pays-bas": "en_NL", "tcf-portugal": "en_PT", "tcf-roumanie": "en_RO", "tcf-pologne": "en_PL",
      "tcf-grece": "en_GR", "tcf-irlande": "en_IE"}


def releve(rows, caption="What each centre’s website showed on 26 October 2026. “Not published”: nothing on the website that day — the centre is the reference."):
    return table(caption, ["Centre", "Versions", "Price", "Sessions and registration"],
                 [(f"<strong>{a}</strong>", b, c, d) for a, b, c, d in rows])


def en(fr_slug, **kw):
    """Spec of the English version of /centres/<fr_slug>/: file, layout, corrected URLs and badge keys from the French."""
    f = FR[fr_slug]
    d = dict(lang="en", variant="en-GB", og_locale=OG[fr_slug], fr_path=f"/centres/{fr_slug}/", exam=f["exam"], file=f["file"],
             layout=f["layout"], published=f["published"], date_label=D_EN, list_date=D_EN, releve_date=D_EN,
             badges={k: [(kind, BADGES[label]) for kind, label in v] for k, v in f.get("badges", {}).items()})
    for k in ("urls", "org_url"):
        if k in f:
            d[k] = f[k]
    d.update(kw)
    return d


_EUR = ("/en/#europe", "TCF Canada and DELF in Europe", "Ten countries: which centres offer the TCF Canada, and fees.")
_PRACTICE = ("/en/tcf-canada-practice-test/", "Free TCF Canada practice test", "Check your level before you pay for a session.")
_CLB = ("/en/tcf-canada/score-clb/", "TCF Canada score chart and CLB calculator", "CLB 7 is 458 in listening, 453 in reading.")
_TEF = ("/en/tcf-vs-tef-canada/", "TCF vs TEF Canada", "The two French tests IRCC accepts, side by side.")
_DELF = ("/en/delf-b2/", "DELF B2 exam", "Format, scoring and preparation.")
_DATES = ("/en/delf-exam-dates-2027/", "DELF exam dates 2027", "The national sessions in France and abroad.")

PAGES = []

# ===========================================================================
# GERMANY — TCF
# ===========================================================================
PAGES.append(en("tcf-allemagne",
    slug="tcf-canada-germany", country_name="Germany", crumb="TCF Canada in Germany",
    title="TCF Canada in Germany: 10 test centres, €295, dates",
    desc="TCF Canada in Germany: Berlin, Hamburg, Munich, Stuttgart, Mainz and Bremen at €295, Erlangen at €210; sessions from November 2026 into 2027.",
    h1="TCF Canada in Germany: the test centres that offer it, fees and dates",
    intro="""In Germany, {n} centres are approved for the TCF by France Éducation international, and <strong>ten advertise the
TCF Canada</strong>: the Instituts français in Berlin, Bremen, Hamburg, Mainz, Munich and Stuttgart, which sell it through a
shared booking module at <strong>€295</strong>, the institute in Aachen (€295), the one in Bonn, the Franco-German Institute
in Erlangen (<strong>€210</strong>) and the Institut français in Mannheim. On 26 October 2026 the module listed 23 TCF
Canada sessions up to December 2027; the first with free places: Munich, on <strong>17 November</strong> (registration
until 8 November). Frankfurt, Tübingen and Dresden don’t offer it.""",
    facts=["<strong>{n} approved centres</strong> (FEI list of 26 October 2026), <strong>10 advertising the TCF Canada</strong>: Berlin, Bremen, Hamburg, Mainz, Munich, Stuttgart, Aachen, Bonn, Erlangen and Mannheim.",
           "<strong>€295</strong> at the six Instituts français of the shared module and in Aachen; <strong>€210</strong> in Erlangen (computer-based); Bonn and Mannheim don’t publish their fee.",
           "TCF Canada sessions in 2026: Munich 17 Nov and 4 Dec, Stuttgart 27 Nov, 10 Dec and 11 Dec, Hamburg 1 Dec, Berlin 2 Dec, Bremen 7 Dec, Mainz 14 Dec; ⚠️ Berlin 4 Nov <strong>full</strong>.",
           "In 2027: Berlin 20 Jan and 17 Feb; Hamburg 11 Feb, 3 Mar, 27 May, 2 Jun and 1 Jul; Mainz 18 Feb, 29 Apr, 24 Jun, 15 Jul, 21 Oct and 16 Dec.",
           "<strong>No TCF Canada</strong> at Eloquia in Frankfurt (tout public, DAP, Québec, IRN), in Tübingen (no TCF on its website) or in Dresden (no session in the module).",
           "Results within 15 working days; 30 days between two attempts; TCF IRN €280, TCF Québec €295."],
    stats=[("{n}", "approved centres", "10 advertise the TCF Canada"), ("€295", "TCF Canada", "€210 in Erlangen"),
           ("23", "TCF Canada sessions", "in the module, to Dec 2027"), ("17 Nov", "first free place", "Munich, deadline 8 Nov")],
    sections=[
        ("releve", "The TCF Canada in Germany, centre by centre", releve([
            ("Instituts français in Berlin, Bremen, Hamburg, Mainz, Munich and Stuttgart", "<strong>Canada</strong>, Québec, IRN, tout public",
             "Canada <strong>€295</strong> · Québec €295 · IRN €280 · tout public €295 (€180 for the three compulsory tests)",
             "Canada, 2026: Berlin 4 Nov <strong>full</strong>; Munich 17 Nov (deadline 8 Nov); Stuttgart 27 Nov (19 Nov); Hamburg 1 Dec (22 Nov); Berlin 2 Dec (24 Nov); Munich 4 Dec (29 Nov); Bremen 7 Dec (29 Nov); Stuttgart 10 and 11 Dec (3 Dec); Mainz 14 Dec (1 Dec). 2027: Berlin 20 Jan and 17 Feb, Hamburg 11 Feb, 3 Mar, 27 May, 2 Jun and 1 Jul, Mainz 18 Feb, 29 Apr, 24 Jun, 15 Jul, 21 Oct and 16 Dec. Book and pay online."),
            ("Institut culturel franco-allemand, Aachen", "<strong>Canada</strong>, Québec, IRN, tout public",
             "Canada <strong>€295</strong>; 15% off for its students, school pupils, university students and jobseekers",
             "6 Nov and 11 Dec 2026 (deadline 4 Dec); book online with a candidate account, or by email."),
            ("Institut français, Bonn", "<strong>Canada</strong>, Québec, IRN, tout public, DAP", "not published",
             "On Fridays: 27 Nov 2026 (deadline 26 Oct) and 18 Dec 2026 (deadline 16 Nov). A registration only counts once the fee has arrived; it is binding, except with a medical certificate (€25 kept)."),
            ("Franco-German Institute, Erlangen", "<strong>Canada</strong>, Québec, IRN, tout public — computer-based (e-TCF)",
             "Canada <strong>€210</strong> · IRN €210 · tout public €100, +€55 per optional test · Québec €50 to €55 per test",
             "Dates not published; register with a PDF form."),
            ("Institut français, Mannheim", "<strong>Canada</strong>, Québec, IRN, tout public", "not published",
             "Dates not published: write to the Institut’s TCF address."),
            ("Eloquia (Frankfurt)", "tout public, DAP, Québec, IRN — <strong>no TCF Canada</strong>", "not published", "Online booking."),
            ("Institut culturel franco-allemand, Tübingen", "no TCF on its website (DELF-DALF only)", "—", "—"),
            ("Institut français, Dresden", "listed among the TCF centres by the Institut français in Germany", "—",
             "No TCF session in the booking module on 26 October 2026."),
        ]) + """
<p>The shared module of the Instituts français (“Anmeldung für Sprachzertifikate”) listed 112 TCF sessions on 26 October
2026, each with its own registration deadline, usually one to two weeks before the test; “Keine Plätze mehr frei” means the
session is full. The TEF Canada, the other test IRCC accepts, had sessions published that day in Bonn and Erlangen on the
map of Le français des affaires.</p>"""),
        ("registration", "Registering for the TCF Canada in Germany", """<p>At the six Instituts français of the module, you pick a
session on the “Anmeldung für Sprachzertifikate” page of the Institut français in Germany (filter TCF, then the city),
create an account and pay online. In Aachen, you book online or by email, giving the version and the session; in Bonn, a
registration only counts once the fee has arrived before the deadline, and it is neither refunded nor moved, except with a
medical certificate; in Erlangen, you send back a PDF form.</p>

<p>Results arrive within 15 working days; the results certificate is digital, with a QR code and the candidate’s photo,
and is valid for two years. You must wait 30 days between two attempts, whatever the version.</p>"""),
    ],
    list_title="The {n} approved TCF test centres in Germany",
    faq=[("Where can I take the TCF Canada in Germany?", "At one of the ten centres that advertised it on 26 October 2026: the Instituts français in Berlin, Bremen, Hamburg, Mainz, Munich and Stuttgart (shared booking module, €295), the Institut culturel franco-allemand in Aachen (€295), the Institut français in Bonn, the Franco-German Institute in Erlangen (€210) and the Institut français in Mannheim."),
         ("How much does the TCF Canada cost in Germany?", "€295 at the Instituts français in Berlin, Bremen, Hamburg, Mainz, Munich and Stuttgart, as in Aachen; €210 in Erlangen. Bonn and Mannheim didn’t publish their fee on 26 October 2026."),
         ("When is the next TCF Canada in Berlin?", "The 4 November 2026 session was full on 26 October; the next ones are on 2 December 2026 (registration until 24 November), then 20 January and 17 February 2027."),
         ("Can I take the TCF Canada in Frankfurt?", "Not at Eloquia, Frankfurt’s only TCF centre: its website offers the TCF tout public, DAP, Québec and IRN, not the Canada version. The nearby centres that advertise it are Mainz (€295) and Mannheim."),
         ("Can I take the TCF IRN in Germany?", "Yes: €280 at the Instituts français in Berlin, Hamburg and Munich, with sessions up to July 2027, and €210 in Erlangen. The results certificate is the one France Éducation international issues worldwide.")],
    also=[("/en/delf-germany/", "DELF exam dates 2027 in Germany", "Sessions from November 2026, B2 at €201."),
          ("/en/tcf-canada-switzerland/", "TCF Canada in Switzerland", "Two centres advertise it, in Montreux and Zurich."), _CLB, _PRACTICE],
    sources="the booking module of the Institut français in Germany (“Anmeldung für Sprachzertifikate”, 112 TCF sessions) and its TCF pages; the websites of the Institut culturel franco-allemand in Aachen (TCF Kanada page), the Institut français in Bonn, the Franco-German Institute in Erlangen (e-TCF), the Institut français in Mannheim, Eloquia and the Institut culturel franco-allemand in Tübingen; the TEF centre map of Le français des affaires; all checked on 26 October 2026.",
    notes={"berlin-institut-francais": "TCF Canada session of 4 November 2026 full; next one on 2 December.",
           "aix-la-chapelle-institut-culturel-franco-allemand-aix-la-chapelle": "FEI puts “Centre de passation” before the address: the institute is at Lothringerstraße 62.",
           "mannheim-institut-francais": "Dates and fee not published on 26 October 2026."},
))

# ===========================================================================
# GERMANY — DELF-DALF
# ===========================================================================
PAGES.append(en("delf-allemagne",
    slug="delf-germany", country_name="Germany", crumb="DELF in Germany",
    title="DELF exam dates 2027 Germany: fees, test centres",
    desc="DELF exam dates 2027 in Germany: B2 on 22 January, 12 March, 11 June, 24 September and 19 November; fees (B2 €201) and the {n} test centres.",
    h1="DELF exam dates 2027 in Germany: sessions, fees and the {n} test centres",
    intro="""<strong>DELF exam dates 2027 in Germany</strong>: at the Instituts français, the DELF B2 written papers fall on
<strong>22 January, 12 March, 11 June, 24 September and 19 November 2027</strong>, the DALF the day after (23 September in
September). Before that, the next session is on <strong>19 and 20 November 2026</strong> (DALF on the 21st), with
registration until 8 to 13 November depending on the city. The DELF and DALF are held at <strong>{n} test centres</strong>,
nine of them Instituts français sharing one online booking module; the DELF B2 costs <strong>€201</strong>, or €170.85 with
the 15% discount for students of an Institut preparation course.""",
    facts=["<strong>{n} test centres</strong> (FEI list of 26 October 2026), coordinated by the language and education cooperation office of the Institut français in Germany.",
           "November 2026: A2 and B1 on the 19th, A1 and B2 on the 20th, DALF C1 and C2 on 21 November, at the Instituts français in Berlin, Bremen, Cologne, Düsseldorf, Hamburg, Leipzig, Mainz, Munich and Stuttgart.",
           "2027, DELF B2 written papers: <strong>22 January, 12 March, 11 June, 24 September, 19 November</strong>; DALF on 23 January, 13 March, 12 June, 23 September and 20 November.",
           "Instituts français fees: <strong>A1 €137 · A2 €161 · B1 €179 · B2 €201 · C1 €224 · C2 €253</strong>; 15% off after an Institut preparation course finished 4 months or less before the exam.",
           "The diplomas are independent: you register directly for the level you want; you need 50 points out of 100 to pass.",
           "Results within 15 working days; paper diploma about 6 months after the exam."],
    stats=[("{n}", "test centres", "FEI list of 26 October 2026"), ("€201", "DELF B2", "€170.85 with 15% off"),
           ("20 Nov", "next B2", "deadline 8 to 13 Nov"), ("5", "sessions in 2027", "Jan, Mar, Jun, Sep, Nov")],
    sections=[
        ("exam-dates", "DELF sessions from November 2026 to November 2027", table(
            "Dates of the DELF-DALF tout public written papers in the booking module of the Instituts français, checked on 26 October 2026. Deadline: the last day to register, which varies by a few days from one city to another.",
            ["Session", "A1", "A2", "B1", "B2", "DALF C1 · C2", "Instituts français", "Deadline"],
            [("<strong>Nov 2026</strong>", "20 Nov", "19 Nov", "19 Nov", "20 Nov", "21 Nov", "Berlin, Bremen, Cologne, Düsseldorf, Hamburg, Leipzig, Mainz, Munich, Stuttgart", "8 to 13 Nov"),
             ("Jan 2027", "22 Jan", "21 Jan", "21 Jan", "22 Jan", "23 Jan", "Cologne, Düsseldorf, Mainz, Stuttgart", "13 to 15 Jan"),
             ("Mar 2027", "12 Mar", "11 Mar", "11 Mar", "12 Mar", "13 Mar", "Berlin, Cologne, Düsseldorf, Hamburg, Munich, Stuttgart", "2 to 5 Mar"),
             ("Jun 2027", "11 Jun", "10 Jun", "10 Jun", "11 Jun", "12 Jun", "Berlin, Cologne, Düsseldorf, Hamburg, Mainz, Munich, Stuttgart", "1 to 4 Jun"),
             ("Sep 2027", "24 Sep", "25 Sep", "25 Sep", "24 Sep", "23 Sep", "Hamburg, Mainz, Munich, Stuttgart", "14 to 17 Sep"),
             ("Nov 2027", "19 Nov", "18 Nov", "18 Nov", "19 Nov", "20 Nov", "Hamburg, Mainz, Munich, Stuttgart", "9 to 12 Nov")]) + """
<p>Speaking tests take place on dates set by each centre. The DELF junior has two sessions in the module, on 24 April and
12 June 2027; the DELF Prim, on 23 January and 5 June 2027. The other centres on the list — Aachen, Bonn, Erlangen,
Frankfurt, Freiburg, Hanover, Heidelberg, Karlsruhe, Kiel, Mannheim, Rostock, Saarbrücken, Tübingen — handle their own
registrations: in Mannheim, the November 2026 deadline is 6 November.</p>"""),
        ("fees", "How much does the DELF cost in Germany?", table(
            "Fees in the booking module of the Instituts français, checked on 26 October 2026.",
            ["Level", "Fee", "With the 15% discount"],
            [("DELF A1", "€137", "€116.45"), ("DELF A2", "€161", "€136.85"), ("DELF B1", "€179", "€152.15"),
             ("<strong>DELF B2</strong>", "<strong>€201</strong>", "<strong>€170.85</strong>"), ("DALF C1", "€224", "€190.40"),
             ("DALF C2", "€253", "€215.05"), ("DELF junior A1 to B2", "€72 to €121", "—"), ("DELF Prim A1.1 to A2", "€40 to €66", "—")], wide=False) + """
<p>The 15% discount applies if you took an Institut français preparation course that ended four months or less before the
exam. The other centres set their own fees. The DELF scolaire, at a preferential price, is organised with schools and the
education ministries of the sixteen Länder.</p>"""),
        ("registration", "Registration, results and diploma", """<p>At the Instituts français, you pick your session on the
“Anmeldung für Sprachzertifikate” page (filter DELF or DALF, then the city), create an account and pay online; each session
shows its deadline. The diplomas are independent: you can register for B2 without having taken A1, A2 or B1. Each paper is
marked out of 25; you need 50 points out of 100, and at least 5 in each paper.</p>

<p>The centre sends the results within 15 working days of the last paper; the paper diploma arrives about 6 months after
the exam, and you can ask for a certificate of achievement in the meantime.</p>"""),
    ],
    list_title="The {n} DELF-DALF test centres, city by city",
    faq=[("What are the DELF exam dates 2027 in Germany?", "At the Instituts français, the DELF B2 is on 22 January, 12 March, 11 June, 24 September and 19 November 2027, each session in four to seven cities; the DALF C1 and C2 is the day after (23 September in September)."),
         ("When is the next DELF exam in Germany?", "On 19 and 20 November 2026 (A2 and B1 on the 19th, A1 and B2 on the 20th) and on 21 November for the DALF, at nine Instituts français; registration until 8 to 13 November depending on the city. Then January, March, June, September and November 2027."),
         ("How much does the DELF B2 cost in Germany?", "€201 at the Instituts français, or €170.85 with the 15% discount given after an Institut preparation course. The DALF costs €224 (C1) and €253 (C2)."),
         ("Do I need A1 before B2?", "No: the DELF and DALF diplomas are independent, so you register directly for the level you want. Passing B1 does not award A1 and A2."),
         ("When do I get my DELF diploma?", "Results arrive within 15 working days of the last paper; the paper diploma, about 6 months after the exam. You can ask for a certificate of achievement before that.")],
    also=[("/en/tcf-canada-germany/", "TCF Canada in Germany", "Ten centres, €295, 23 sessions in the module."),
          ("/en/delf-switzerland/", "DELF exam dates 2027 in Switzerland", "The national calendar, B2 from CHF 370 to 390."), _DATES, _DELF],
    sources="the booking module of the Institut français in Germany (“Anmeldung für Sprachzertifikate”, DELF and DALF filters) and its “DELF DALF für Erwachsene” page; the website of the Institut français in Mannheim; all checked on 26 October 2026.",
    notes={"mannheim-institut-francais-mannheim": "November 2026 DELF-DALF registration deadline: 6 November (Institut website).",
           "berlin-institut-francais-d-allemagne-antenne-de-berlin": "Sessions and registration in the shared module of the Instituts français."},
))

# ===========================================================================
# SWITZERLAND — TCF
# ===========================================================================
PAGES.append(en("tcf-suisse",
    slug="tcf-canada-switzerland", country_name="Switzerland", crumb="TCF Canada in Switzerland",
    title="TCF Canada in Switzerland: Montreux, Zurich, CHF fees",
    desc="TCF in Switzerland: only ALPADIA (Montreux, CHF 290) and the Alliance française de Zurich advertise the TCF Canada; Swiss Exams and Fribourg, tout public.",
    h1="TCF Canada in Switzerland: test centres, CHF fees and the next sessions",
    intro="""In Switzerland, {n} centres are approved for the TCF, but <strong>only two advertise the TCF Canada</strong>: ALPADIA
Language Schools in Montreux (<strong>CHF 290</strong>, but no 2026 dates published) and the Alliance française de Zurich
(dates and quotes by email). Swiss Exams — Bern, Geneva, Lausanne, Winterthur — and the University of Fribourg’s language
centre only run the <strong>TCF tout public</strong>, on computer, at CHF 320 and CHF 300. Next session: Fribourg on
12 November 2026. For a Canadian application, the TEF Canada also had sessions published in Geneva on 26 October 2026.""",
    facts=["<strong>{n} approved centres</strong> (FEI list of 26 October 2026): Swiss Exams in four cities, the University of Fribourg, ALPADIA in Montreux and the Alliance française de Zurich.",
           "<strong>TCF Canada</strong>: ALPADIA (Montreux), <strong>CHF 290</strong>, dates published for 2025 only; the Alliance française de Zurich, on request.",
           "Computer-based TCF tout public: <strong>CHF 320</strong> at Swiss Exams (CHF 160 for the three compulsory tests), <strong>CHF 300</strong> in Fribourg (CHF 155).",
           "Next tout public sessions: Fribourg 12 Nov 2026 (deadline 29 Oct), Lausanne 21 Nov (deadline 23 Oct), Geneva 4 Dec and Bern 5 Dec 2026 (deadline 6 Nov).",
           "According to the University of Fribourg, the TCF tout public counts for French citizenship if all five tests are taken in the same session.",
           "TEF Canada, the other test IRCC accepts: sessions published at IFAGE in Geneva on 26 October 2026."],
    stats=[("{n}", "approved centres", "2 advertise the TCF Canada"), ("CHF 290", "TCF Canada", "ALPADIA, Montreux"),
           ("CHF 320", "TCF tout public", "Swiss Exams; CHF 300 in Fribourg"), ("12 Nov", "next session", "Fribourg, deadline 29 Oct")],
    sections=[
        ("releve", "The TCF in Switzerland, centre by centre", releve([
            ("ALPADIA Language Schools (Montreux)", "<strong>Canada</strong> and Québec, tout public and IRN",
             "Canada and Québec <strong>CHF 290</strong> (CHF 65 to 80 per test) · tout public and IRN CHF 280",
             "Seven to eight sessions a year announced, but only 2025 dates are online. Register by phone at least one month before; pay in cash on arrival."),
            ("Alliance française de Zurich", "tout public, Québec, <strong>Canada</strong>, IRN", "not published (quote on request)",
             "“Fixed dates” given by email: information, quotes and registration through the Alliance’s school."),
            ("Swiss Exams (Bern, Geneva, Lausanne, Winterthur)", "tout public only, computer-based",
             "CHF 320 · CHF 160 for the three compulsory tests · CHF 105 for writing or speaking alone",
             "Lausanne 21 Nov 2026 (deadline 23 Oct); Geneva 4 Dec and Bern 5 Dec (deadline 6 Nov); 2027: Lausanne 30 Jan and 27 Feb, Geneva 6 Feb, Bern 20 Feb. Results three weeks later. Online registration."),
            ("University of Fribourg language centre", "tout public only, computer-based; external candidates welcome",
             "CHF 300 · CHF 155 for the compulsory tests · CHF 90 per optional test",
             "12 Nov 2026 (deadline 29 Oct), 12 Jan 2027 (4 Jan), 4 Mar (18 Feb), 29 Apr (15 Apr), 6 Jul (22 Jun), 31 Aug 2027 (17 Aug). Online form and ID."),
        ]) + """
<p>Swiss Exams points out that re-marking requests are suspended for sessions after 31 August 2026, until autumn 2027: report
any incident during the tests to the centre on the day. France Éducation international’s list shows a computer option for
five centres; ALPADIA and the Alliance in Zurich declare none.</p>"""),
    ],
    list_title="The {n} approved TCF test centres in Switzerland",
    faq=[("Where can I take the TCF Canada in Switzerland?", "On 26 October 2026, two approved centres advertised it: ALPADIA Language Schools in Montreux (CHF 290, 2026 dates not published: call the school) and the Alliance française de Zurich (dates and quotes by email). Swiss Exams and the University of Fribourg only run the TCF tout public."),
         ("How much does the TCF cost in Switzerland?", "CHF 320 for the full TCF tout public at Swiss Exams (CHF 160 for the three compulsory tests), CHF 300 at the University of Fribourg, CHF 290 for the TCF Canada at ALPADIA in Montreux."),
         ("When is the next TCF in Geneva or Lausanne?", "At Swiss Exams: Lausanne on 21 November 2026 (deadline 23 October) and Geneva on 4 December 2026 (deadline 6 November), then Lausanne on 30 January and 27 February 2027 and Geneva on 6 February 2027 — TCF tout public, on computer."),
         ("Is the TCF tout public enough for French citizenship?", "According to the University of Fribourg’s language centre, it counts for a citizenship application if the compulsory tests and both optional tests are taken in the same session. For a Canadian application, you need the TCF Canada or the TEF Canada."),
         ("Where can I take the TEF Canada in Switzerland?", "The map of Le français des affaires showed TEF Canada sessions at IFAGE in Geneva on 26 October 2026. The TEF Canada is the other French test IRCC accepts.")],
    also=[("/en/delf-switzerland/", "DELF exam dates 2027 in Switzerland", "The national calendar and fees by centre."),
          ("/en/tcf-canada-germany/", "TCF Canada in Germany", "Ten centres, €295, sessions every month."), _TEF, _PRACTICE],
    sources="the Swiss Exams booking module (inscription-tcf.swiss-exams.ch) and its TCF page; the TCF and “Dates d’examens et inscription” pages of the University of Fribourg’s language centre; ALPADIA’s exam centres page; the “Examens TEF et TCF” page of the Alliance française de Zurich; the TEF centre map of Le français des affaires; all checked on 26 October 2026.",
    notes={"montreux-alpadia-language-schools": "Exam registration: ALPADIA gives +41 21 621 84 48; the number published by FEI is incomplete."},
))

# ===========================================================================
# SWITZERLAND — DELF-DALF
# ===========================================================================
PAGES.append(en("delf-suisse",
    slug="delf-switzerland", country_name="Switzerland", crumb="DELF in Switzerland",
    title="DELF exam dates 2027 Switzerland: CHF fees, centres",
    desc="DELF exam dates 2027 in Switzerland: 20 March, 22 May, 19 June, 18 September and 13 November, registration deadlines and fees (B2 CHF 370 to 390).",
    h1="DELF exam dates 2027 in Switzerland: the national calendar, fees and the {n} centres",
    intro="""<strong>DELF exam dates 2027 in Switzerland</strong>: the DELF and DALF tout public follow a <strong>national
calendar</strong>, published on delfdalf.ch by the Fondation Esprit Francophonie. In 2027 the written papers are on
<strong>Saturday 20 March</strong> (registration until <strong>8 January</strong>), then 22 May, 19 June, 18 September and
13 November. You register online with one of the regional centres, where the DELF B2 costs <strong>CHF 370 to 390</strong>.
The 14 November 2026 session has been closed since 11 September.""",
    facts=["<strong>{n} test centres</strong> (FEI list of 26 October 2026), managed by the cooperation and cultural action service named on FEI’s list (Zurich); calendar and registration on delfdalf.ch.",
           "2027: <strong>20 March</strong> (deadline 8 January), <strong>22 May</strong> (12 March), <strong>19 June</strong> (9 April), <strong>18 September</strong> (6 August), <strong>13 November</strong> (10 September).",
           "Speaking tests during the session month, depending on the centre; DALF C2 speaking test the day before the written papers.",
           "DELF B2: <strong>CHF 370</strong> in Neuchâtel, 375 in Geneva and Lausanne, 380 in Bern and Liestal, 390 in Zurich (KV Zürich).",
           "September: four centres only (Geneva, Liestal, Lugano, St. Gallen); DELF junior in March, May, June and November; DELF Prim in May and June.",
           "Exam programme sent by email at least two weeks before the first paper."],
    stats=[("{n}", "test centres", "FEI list of 26 October 2026"), ("20 Mar", "first 2027 session", "deadline 8 January"),
           ("CHF 370-390", "DELF B2", "depending on the centre"), ("5", "sessions a year", "Mar, May, Jun, Sep, Nov")],
    sections=[
        ("exam-dates", "The 2027 national calendar", table(
            "2027 exam calendar for Switzerland (version of 29 September 2026, delfdalf.ch), “subject to change”. Not every level is open at every centre.",
            ["Session", "Written papers", "Speaking tests", "C2 speaking", "Registration deadline"],
            [("<strong>March 2027</strong>", "Saturday 20 Mar", "1 to 31 Mar", "Friday 19 Mar", "<strong>Friday 8 Jan 2027</strong>"),
             ("May 2027", "Saturday 22 May", "1 to 31 May", "Friday 21 May", "Friday 12 Mar"),
             ("June 2027", "Saturday 19 Jun", "1 to 30 Jun", "Friday 18 Jun", "Friday 9 Apr"),
             ("September 2027", "Saturday 18 Sep", "1 to 30 Sep", "Friday 17 Sep", "Friday 6 Aug"),
             ("November 2027", "Saturday 13 Nov", "1 to 30 Nov", "Friday 12 Nov", "Friday 10 Sep")]) + """
<p>The March and November sessions bring together the most centres — Aarau, Bellinzona, Bern, Geneva, Lausanne, Liestal,
Lucerne, Neuchâtel, St. Gallen, Sierre, Weinfelden and the two Zurich centres; the September session is held only in
Geneva, Liestal, Lugano and St. Gallen. The 2026 calendar put the last session of the year on Saturday 14 November 2026,
with a deadline of 11 September.</p>"""),
        ("fees", "How much does the DELF cost in Switzerland?", table(
            "Registration fees shown by the centres on delfdalf.ch on 26 October 2026.",
            ["Level", "Geneva · Lausanne", "Bern", "Liestal", "Zurich (KV Zürich)", "Neuchâtel"],
            [("DELF A1", "CHF 205", "CHF 200", "CHF 190", "CHF 200", "—"), ("DELF A2", "CHF 235", "CHF 230", "CHF 240", "CHF 230", "—"),
             ("DELF B1", "CHF 285", "CHF 290", "CHF 280", "CHF 290", "CHF 280"),
             ("<strong>DELF B2</strong>", "<strong>CHF 375</strong>", "<strong>CHF 380</strong>", "<strong>CHF 380</strong>", "<strong>CHF 390</strong>", "<strong>CHF 370</strong>"),
             ("DALF C1", "CHF 415", "CHF 410", "CHF 415", "CHF 420", "CHF 410"), ("DALF C2", "CHF 435", "CHF 430", "CHF 430", "CHF 430", "CHF 430")]) + """
<p>In Bern and Zurich, a change requested after you receive your exam programme is only granted exceptionally, for CHF 50;
in Zurich, moving to a later session after the deadline also costs CHF 50.</p>"""),
        ("registration", "Registration", """<p>You register online from delfdalf.ch, choosing your regional centre. Your personal exam
programme — with the addresses of the papers, which are not always held in the same building — arrives by email at least
two weeks before the first paper; the programme and the results are only sent electronically, hence the advice to give a
private email address.</p>"""),
    ],
    list_title="The {n} approved DELF-DALF test centres in Switzerland",
    faq=[("What are the DELF exam dates 2027 in Switzerland?", "The written papers are on Saturday 20 March, 22 May, 19 June, 18 September and 13 November 2027; the registration deadlines are 8 January, 12 March, 9 April, 6 August and 10 September 2027."),
         ("How much does the DELF B2 cost in Switzerland?", "CHF 370 to CHF 390 depending on the centre: CHF 370 in Neuchâtel, 375 in Geneva and Lausanne, 380 in Bern and Liestal, 390 at KV Zürich. The DALF C1 costs CHF 410 to 420."),
         ("Can I still register for November 2026?", "No: registration for the 14 November 2026 session closed on 11 September. The next session is on 20 March 2027, with a deadline of 8 January 2027."),
         ("Where can I take the DELF in Geneva or Lausanne?", "At the Lac Léman exam centre, run by IFAGE (place des Augustins 19, Geneva), which also organises the Lausanne sessions: DELF B2 at CHF 375."),
         ("When do I get my exam programme?", "By email, at least two weeks before the first paper. It gives the addresses of the papers, which sometimes change from one session to the next.")],
    also=[("/en/tcf-canada-switzerland/", "TCF Canada in Switzerland", "Montreux and Zurich; tout public elsewhere."),
          ("/en/delf-germany/", "DELF exam dates 2027 in Germany", "Six sessions from November 2026 to November 2027."), _DATES, _DELF],
    sources="the 2026 and 2027 exam calendars for Switzerland (PDFs of 21 April and 29 September 2026) and the exam centre pages of delfdalf.ch (Geneva-Lausanne, Bern, Liestal, Zurich Limmat, Neuchâtel), checked on 26 October 2026.",
    notes={"geneve-ifage-fondation-pour-la-formation-des-adultes": "Lac Léman exam centre: also runs the Lausanne sessions.",
           "zurich-wirtschaftschule-kv-zurich": "“Zurich Limmat” exam centre on delfdalf.ch."},
))

# ===========================================================================
# BELGIUM — TCF (+ DELF in brief)
# ===========================================================================
PAGES.append(en("tcf-belgique",
    slug="tcf-canada-belgium", country_name="Belgium", crumb="TCF Canada in Belgium",
    title="TCF Canada in Belgium: Brussels €268, Ghent €260",
    desc="TCF Canada in Belgium: the Alliance française de Bruxelles-Europe (€268, session on 9 December 2026) and the Alliance in Ghent (€260), on computer.",
    h1="TCF Canada in Belgium: the two test centres, fees and dates",
    intro="""In Belgium, two centres are approved for the TCF, and <strong>both run the TCF Canada</strong>, on computer: the
<strong>Alliance française de Bruxelles-Europe</strong> (<strong>€268</strong>, next session on <strong>Wednesday
9 December 2026</strong>) and the <strong>Alliance française de Flandre orientale</strong> in Ghent (<strong>€260</strong>,
three sessions a year, with no 2027 calendar published on 26 October 2026). You book and pay online, on each Alliance’s
website; the speaking test takes place on the same day as the written tests.""",
    facts=["<strong>2 approved centres</strong> (FEI list of 26 October 2026), both offering the TCF Canada, on computer.",
           "Brussels: TCF Canada <strong>€268</strong> on 9 December 2026; TCF tout public €258 on 10 December, TCF IRN €220 on 14 December.",
           "Ghent: TCF Canada <strong>€260</strong>, tout public €250; three sessions a year (February, May, August-September); 2027 not published.",
           "Brussels hands out a provisional certificate on the day; Ghent shows the multiple-choice results at the end of the test, the full results within 15 working days.",
           "30 days between two attempts; every registration is in the candidate’s name.",
           "DELF-DALF: 6 centres in Belgium; the November 2026 session is closed, and 2027 sessions are not yet scheduled."],
    stats=[("2", "approved centres", "both with the TCF Canada"), ("€268", "TCF Canada in Brussels", "€260 in Ghent"),
           ("9 Dec", "next session", "Brussels, 2026"), ("30 days", "between two attempts", "")],
    sections=[
        ("releve", "The TCF in Belgium, centre by centre", releve([
            ("Alliance française de Bruxelles-Europe", "<strong>Canada</strong>, IRN, tout public — computer-based",
             "Canada <strong>€268</strong> · tout public €258 · IRN €220",
             "Canada Wednesday 9 Dec 2026 (10:00–12:40, speaking in the afternoon); tout public 10 Dec; IRN 14 Dec 2026. Test-day notice by email at least 5 days before; provisional certificate on the day, FEI certificate within two weeks."),
            ("Alliance française de Flandre orientale (Ghent)", "<strong>Canada</strong>, IRN, tout public — computer-based",
             "Canada <strong>€260</strong> · tout public €250",
             "Three sessions a year (February, May, August-September): in 2026, Canada on 12 and 16 Feb and from 20 Aug to 17 Sep; 2027 not published. Pay when registering: the form alone is not a registration. Full results within 15 working days."),
        ]) + """
<p>In Brussels, a request for a particular speaking-test time goes to the exams office before registration closes; candidates
are photographed on the test day. In Ghent, a cancellation after the deadline is only refunded with proof (a medical
certificate, for example), minus an administration fee of about €2.</p>"""),
        ("delf", "The DELF and DALF in Belgium", """<p>The DELF and DALF are held at 6 centres (FEI list of 26 October 2026) — the
Alliances françaises of Bruxelles-Europe, Antwerp and Flandre orientale, KU Leuven Kulak in Kortrijk, the Institut supérieur
des langues vivantes of the University of Liège and the European School in Mol —, under the central management of the
Alliance de Bruxelles-Europe. It holds four tout public sessions a year: in 2026, March, June, September and November, with
written papers from 17 to 26 November and registration closed on 24 October. On 26 October 2026, no 2027 session was on
sale yet and fees were not shown; the Alliance’s students get 10% off.</p>"""),
    ],
    list_title="The {n} approved TCF test centres in Belgium",
    faq=[("Where can I take the TCF Canada in Belgium?", "At the Alliance française de Bruxelles-Europe, avenue des Arts 46 (€268), or at the Alliance française de Flandre orientale, Henleykaai 86 in Ghent (€260): they are the country’s two approved TCF centres, and both offer the Canada version, on computer."),
         ("When is the next TCF Canada in Brussels?", "On Wednesday 9 December 2026, from 10:00 to 12:40 for the written tests, with the speaking test in the afternoon. Ghent had not published its 2027 sessions on 26 October 2026."),
         ("How much does the TCF Canada cost in Belgium?", "€268 in Brussels and €260 in Ghent. The TCF tout public costs €258 in Brussels and €250 in Ghent, the TCF IRN €220 in Brussels."),
         ("When will I get my results?", "In Brussels, a provisional certificate is handed out on the test day and the France Éducation international certificate arrives within two weeks; in Ghent, the full results arrive within 15 working days."),
         ("Can I take the DELF in Brussels in 2027?", "Yes, but the 2027 sessions were not yet scheduled on 26 October 2026. In 2026, the Alliance de Bruxelles-Europe held four: March, June, September and November.")],
    also=[("/en/tcf-canada-netherlands/", "TCF Canada in the Netherlands", "Amsterdam €290, The Hague, Rotterdam."),
          ("/en/tcf-canada-uk/", "TCF Canada in the UK", "London £260, Glasgow £325."), _CLB, _PRACTICE],
    sources="the websites of the Alliance française de Bruxelles-Europe (TCF Canada, TCF IRN, TCF tout public and DELF-DALF tout public pages, Calendar and Register tabs) and of the Alliance française de Flandre orientale (TCF page), checked on 26 October 2026; FEI’s DELF-DALF list for Belgium, read the same day.",
))

# ===========================================================================
# ITALY — TCF
# ===========================================================================
PAGES.append(en("tcf-italie",
    slug="tcf-canada-italy", country_name="Italy", crumb="TCF Canada in Italy",
    title="TCF Canada in Italy: 7 test centres, €210 to €250",
    desc="TCF Canada in Italy: Turin €220, Genoa €210, Milan €240, Venice €250, Bari, Aosta, Latina; sessions from November 2026 into 2027.",
    h1="TCF Canada in Italy: the test centres that offer it, fees and dates",
    intro="""In Italy, {n} centres are approved for the TCF; on 26 October 2026, <strong>seven advertised the TCF Canada</strong>
on their websites: the Alliances françaises in Turin (<strong>€220</strong>), Genoa (<strong>€210</strong>), Venice
(<strong>€250</strong>), Bari (€220), Aosta and Latina, and the Institut français in Milan (<strong>€240</strong>). Next
sessions: Latina on 13 November, Turin on 1 December, Milan on 10 December, Venice on 16 December 2026, Genoa on 16 January
2027. The Centre Saint-Louis in Rome only offers the tout public, IRN and Québec versions.""",
    facts=["<strong>{n} approved centres</strong> (FEI list of 26 October 2026), <strong>7 advertising the TCF Canada</strong>: Turin, Genoa, Venice, Bari, Aosta, Latina and the Institut français in Milan.",
           "TCF Canada: <strong>€210</strong> in Genoa, <strong>€220</strong> in Turin and Bari, <strong>€240</strong> in Milan, <strong>€250</strong> in Venice; Aosta and Latina don’t publish their fee.",
           "Sessions: Latina 13 Nov and 11 Dec; Turin 1 Dec (deadline 6 Nov); Milan 10 Dec (registration until 30 Oct); Venice 16 Dec 2026 (deadline 13 Nov); Genoa 16 Jan 2027 (deadline 21 Dec).",
           "In 2027: Milan 9 Mar; Turin 16 Mar and 6 Jul; Genoa 6 Mar, 8 May and 10 Jul.",
           "<strong>No TCF Canada</strong> at the Centre Saint-Louis in Rome (tout public, IRN, Québec) or at the Alliance in Padua (tout public only).",
           "TEF Canada, the other test IRCC accepts: sessions published by the Alliance française in Vicenza on 26 October 2026."],
    stats=[("{n}", "approved centres", "7 advertise the TCF Canada"), ("€210–250", "TCF Canada", "depending on the centre"),
           ("13 Nov", "next session", "Latina; Turin on 1 Dec"), ("2 years", "validity", "")],
    sections=[
        ("releve", "The TCF Canada in Italy, centre by centre", releve([
            ("Alliance française, Turin", "<strong>Canada</strong>, Québec, IRN, tout public — computer-based (QWERTY keyboard)",
             "Canada <strong>€220</strong>", "Tuesday 1 Dec 2026 (deadline 6 Nov), 16 Mar 2027 (19 Feb), 6 Jul 2027 (4 Jun). Online form, then bank transfer."),
            ("Alliance française, Genoa", "<strong>Canada</strong>, Québec, IRN, tout public — paper-based",
             "Canada <strong>€210</strong> · IRN €160 · tout public €100 (+€50 per optional test)",
             "16 Jan 2027 (deadline 21 Dec 2026), 6 Mar (10 Feb), 8 May (13 Apr), 10 Jul 2027 (6 Jun). Register by email or in person; results in about twenty days."),
            ("Institut français, Milan", "<strong>Canada</strong>, Québec, tout public", "Canada <strong>€240</strong>",
             "10 Dec 2026 (registration 5 to 30 Oct) and 9 Mar 2027 (11 to 31 Jan). Photo taken on the test day."),
            ("Alliance française, Venice", "<strong>Canada</strong>, Québec, IRN, tout public",
             "Canada <strong>€250</strong> · IRN €160 · tout public €110 (+€65 per optional test)",
             "18 Nov 2026 (deadline 16 Oct) and 16 Dec 2026 (deadline 13 Nov)."),
            ("Alliance française, Bari", "<strong>Canada</strong>, Québec, IRN, tout public", "Canada <strong>€220</strong> (4 × €55) · IRN €140",
             "Dates not published on the TCF Canada page."),
            ("Alliance française Sud Latium (Latina)", "<strong>Canada</strong>, Québec, IRN, tout public — computer-based", "not published",
             "Canada and IRN: 13 Nov and 11 Dec 2026; 2027 not published."),
            ("Alliance française, Aosta", "<strong>Canada</strong>, tout public", "not published", "Dates not published."),
            ("Institut français – Centre Saint-Louis (Rome)", "tout public, IRN, Québec — <strong>no TCF Canada</strong>", "not published",
             "30 Nov 2026; registration opens the month before and closes 10 working days before; results in two weeks."),
            ("Alliance française, Padua", "tout public only", "not published", "Form, then bank transfer."),
            ("Alliance française, Vicenza", "TCF (version not specified)", "not published", "Extra DFP-TEF-TCF session on 18 Dec 2026 (registration until 26 Oct); other dates on request."),
        ]) + """
<p>Bologna (website not accessible), Naples (the university language centre, website unreachable), Palermo (no TCF page) and
Trieste (empty website) could not be checked on 26 October 2026: their contact details are in the list below. Each centre
sets its own dates, as the Alliance in Venice points out.</p>"""),
    ],
    list_title="The {n} approved TCF test centres in Italy",
    faq=[("Where can I take the TCF Canada in Italy?", "On 26 October 2026, seven approved centres advertised it: the Alliances françaises in Turin, Genoa, Venice, Bari, Aosta and Latina, and the Institut français in Milan. The Centre Saint-Louis in Rome does not offer it."),
         ("How much does the TCF Canada cost in Italy?", "€210 in Genoa, €220 in Turin and Bari, €240 at the Institut français in Milan, €250 in Venice. Aosta and Latina didn’t publish their fee."),
         ("Can I take the TCF Canada in Rome?", "Not at the Centre Saint-Louis, the Institut français in Rome: it offers the TCF tout public, the TCF IRN and the TCF Québec. The nearest centre that advertises it is the Alliance française Sud Latium, in Latina."),
         ("When is the next TCF Canada in Milan?", "On 10 December 2026, with registration from 5 to 30 October, then on 9 March 2027 (registration from 11 to 31 January), at €240."),
         ("Is the TCF computer-based in Italy?", "It depends on the centre: Turin and Latina run it on computer; Genoa, for now, only on paper.")],
    also=[("/en/tcf-canada-switzerland/", "TCF Canada in Switzerland", "ALPADIA (Montreux) and the Alliance in Zurich."),
          ("/en/tcf-canada-greece/", "TCF Canada in Greece", "Athens, six sessions to June 2027."), _CLB, _PRACTICE],
    sources="the 2026-2027 TCF Canada calendar (PDF) of the Alliance française in Turin; the TCF pages of the Alliances françaises in Genoa, Venice, Bari (TCF Canada), Latina (Sud Latium), Aosta, Padua and Vicenza; the 2026-2027 TCF calendar of the Institut français in Milan; the TCF page of the Institut français – Centre Saint-Louis in Rome; the TEF centre map of Le français des affaires; all checked on 26 October 2026.",
    notes={"genes-alliance-francaise": "Paper-based TCF only for now (Alliance website).",
           "bologne-alliance-francaise": "Website not accessible on 26 October 2026: not checked.",
           "naples-centro-linguistico-di-ateneo": "Website unreachable on 26 October 2026: not checked."},
))

# ===========================================================================
# NETHERLANDS — TCF
# ===========================================================================
PAGES.append(en("tcf-pays-bas",
    slug="tcf-canada-netherlands", country_name="Netherlands", crumb="TCF Canada in the Netherlands",
    title="TCF Canada in the Netherlands: Amsterdam €290, dates",
    desc="TCF Canada in the Netherlands: the Alliances françaises in Amsterdam (€290, next place on 13 January 2027), The Hague and Rotterdam.",
    h1="TCF Canada in the Netherlands: test centres, fees and dates",
    intro="""In the Netherlands, {n} centres are approved for the TCF, and the <strong>three Alliances françaises</strong> —
Amsterdam, The Hague and Rotterdam — advertise the TCF Canada. Amsterdam runs it on computer for <strong>€290</strong>: its
25 November 2026 session was full on 26 October, and the next one is on <strong>13 January 2027</strong> (register before
29 December). The Hague sells its sessions through its online booking module; Rotterdam shows €75 to €300 depending on the
version. The four other centres are higher-education institutions.""",
    facts=["<strong>{n} approved centres</strong> (FEI list of 26 October 2026): three Alliances françaises, the Institut français des Pays-Bas in Groningen and three universities of applied sciences (Leeuwarden, Nijmegen, Utrecht).",
           "<strong>TCF Canada in Amsterdam: €290</strong>; ⚠️ 25 Nov 2026 full; 13 Jan 2027 open, register before 29 Dec 2026.",
           "TCF IRN in Amsterdam: €205, on 16 Dec 2026 (register before 1 Dec); TCF Québec: €75 per test, dates on request.",
           "The Hague: TCF Canada, Québec, IRN and tout public, sessions booked online; results certificate within 15 working days.",
           "Rotterdam: TCF tout public, Québec, Canada and IRN, €75 to €300 depending on the version.",
           "TEF Canada, the other test IRCC accepts: sessions published by the Alliance française in The Hague on 26 October 2026."],
    stats=[("{n}", "approved centres", "3 Alliances with the TCF Canada"), ("€290", "TCF Canada", "in Amsterdam"),
           ("13 Jan", "next free place", "Amsterdam, 2027"), ("€205", "TCF IRN", "in Amsterdam")],
    sections=[
        ("releve", "The TCF in the Netherlands, centre by centre", releve([
            ("Alliance française, Amsterdam", "<strong>Canada</strong>, Québec, IRN, tout public — computer-based",
             "Canada <strong>€290</strong> · IRN €205 · Québec €75 per test",
             "Canada: 25 Nov 2026 <strong>full</strong>; 13 Jan 2027 (register before 29 Dec 2026). IRN: 16 Dec 2026 (before 1 Dec). Tout public: 27 Jan 2027 (before 12 Jan). Québec on request. Test-day notice by email."),
            ("Alliance française, The Hague", "<strong>Canada</strong>, Québec, IRN, tout public", "not checked (online module)",
             "Sessions booked in the Alliance’s module; results certificate within 15 working days, valid for two years."),
            ("Alliance française, Rotterdam", "<strong>Canada</strong>, Québec, IRN, tout public", "€75 to €300 depending on the version",
             "Dates not published on the TCF page."),
            ("Institut français des Pays-Bas (Groningen), NHL Stenden (Leeuwarden), HAN (Nijmegen), Hogeschool Utrecht",
             "not published", "—", "No TCF page found on 26 October 2026: contact the institution."),
        ])),
    ],
    list_title="The {n} approved TCF test centres in the Netherlands",
    faq=[("Where can I take the TCF Canada in the Netherlands?", "At one of the three Alliances françaises, which advertised it on 26 October 2026: Amsterdam (€290, on computer), The Hague and Rotterdam."),
         ("When is the next TCF Canada in Amsterdam?", "The 25 November 2026 session was full on 26 October; the next one is on 13 January 2027, with registration before 29 December 2026."),
         ("How much does the TCF Canada cost in the Netherlands?", "€290 at the Alliance française in Amsterdam. Rotterdam shows €75 to €300 depending on the version; The Hague sells its sessions through its online module."),
         ("Where can I take the TCF IRN for French citizenship in the Netherlands?", "At the Alliance française in Amsterdam, €205, on 16 December 2026 (register before 1 December), or at the Alliances in The Hague and Rotterdam.")],
    also=[("/en/tcf-canada-belgium/", "TCF Canada in Belgium", "Brussels €268, Ghent €260."),
          ("/en/tcf-canada-germany/", "TCF Canada in Germany", "Ten centres, €295."), _TEF, _PRACTICE],
    sources="the TCF pages of the Alliances françaises in Amsterdam, The Hague and Rotterdam, and the TEF centre map of Le français des affaires, checked on 26 October 2026.",
    notes={"amsterdam-alliance-francaise": "TCF Canada session of 25 November 2026 full; next one on 13 January 2027."},
))

# ===========================================================================
# PORTUGAL — TCF
# ===========================================================================
PAGES.append(en("tcf-portugal",
    slug="tcf-canada-portugal", country_name="Portugal", crumb="TCF Canada in Portugal",
    title="TCF Canada in Portugal: Porto, Faro, Viseu, fees",
    desc="TCF Canada in Portugal: €220 in Porto and in Faro (Algarve, your choice of date, on computer), €211 in Viseu; Lisbon and Coimbra on request.",
    h1="TCF Canada in Portugal: test centres, fees and sessions",
    intro="""In Portugal, {n} centres are approved for the TCF. On 26 October 2026, three Alliances françaises showed a TCF
Canada fee: <strong>Porto</strong> and <strong>Faro</strong> (Algarve), <strong>€220</strong>, and <strong>Viseu</strong>,
<strong>€211</strong>. In Faro, the test is taken on computer on any working day, on a date the candidate chooses at least
7 days ahead; elsewhere, no dates are online: contact the Alliance. Lisbon and Coimbra state neither the version nor the
fee.""",
    facts=["<strong>{n} approved centres</strong> (FEI list of 26 October 2026): the Alliances françaises of Lisbon, Porto, Coimbra, Viseu and the Algarve (Faro), and the language institute of Universidade Nova de Lisboa.",
           "TCF Canada: <strong>€220</strong> in Porto and Faro, <strong>€211</strong> in Viseu.",
           "Faro: computer-based TCF on demand, any working day except 8 to 21 August and the second half of December, booked at least 7 days ahead.",
           "TCF IRN €220 in Faro and Porto; TCF tout public €100 for the compulsory tests in Faro.",
           "Lisbon: TCF presented with no version or fee, contact form; Coimbra: calendar and fees on request."],
    stats=[("{n}", "approved centres", "3 show the TCF Canada"), ("€220", "TCF Canada", "Porto and Faro; €211 in Viseu"),
           ("7 days", "notice in Faro", "date chosen by the candidate"), ("2 years", "validity", "")],
    sections=[
        ("releve", "The TCF in Portugal, centre by centre", releve([
            ("Alliance française de l’Algarve (Faro)", "<strong>Canada</strong>, Québec, IRN, tout public — computer-based",
             "Canada or Québec <strong>€220</strong> · IRN €220 · tout public €100 (+€65 writing, +€55 speaking)",
             "Any working day, except 8 to 21 August and the second half of December, on a date set by the candidate at least 7 days ahead. Online registration form."),
            ("Alliance française, Porto", "<strong>Canada</strong>, IRN, Québec, tout public", "Canada <strong>€220</strong> · IRN €220",
             "Dates not published."),
            ("Alliance française, Viseu", "<strong>Canada</strong>, Québec", "Canada <strong>€211</strong>",
             "Dates online out of date; register at least 7 days ahead, with a form and proof of payment; extra sessions on request, at a supplement."),
            ("Alliance française, Coimbra", "computer-based TCF (versions not specified)", "on request",
             "Calendar and fees on request; register in person."),
            ("Alliance française, Lisbon", "TCF (versions not specified)", "not published", "Contact form on the exams page."),
            ("Instituto de Línguas – Universidade Nova de Lisboa", "not checked", "—", "Website unreachable on 26 October 2026."),
        ])),
    ],
    list_title="The {n} approved TCF test centres in Portugal",
    faq=[("Where can I take the TCF Canada in Portugal?", "On 26 October 2026, three Alliances françaises showed a TCF Canada fee: Porto (€220), Faro in the Algarve (€220) and Viseu (€211). Lisbon and Coimbra run the TCF without listing the versions online."),
         ("How much does the TCF Canada cost in Portugal?", "€220 in Porto and Faro, €211 in Viseu, for the four tests."),
         ("Can I choose my TCF Canada date in Portugal?", "In Faro, yes: the Alliance de l’Algarve runs the TCF on computer on any working day, except 8 to 21 August and the second half of December, as long as you book at least 7 days ahead."),
         ("Where can I take the TCF in Lisbon?", "At the Alliance française in Lisbon, which lists neither version nor fee online: use its contact form. The language institute of Universidade Nova de Lisboa is also approved.")],
    also=[("/en/tcf-canada-italy/", "TCF Canada in Italy", "Seven centres, €210 to €250."),
          ("/en/tcf-canada-ireland/", "TCF Canada in Ireland", "Dublin and Galway, €270."), _CLB, _PRACTICE],
    sources="the TCF pages of the Alliances françaises of the Algarve, Porto, Viseu, Coimbra and Lisbon, checked on 26 October 2026.",
    notes={"lisbonne-instituto-de-linguas-da-universidade-nova-de-lisbo": "Website unreachable on 26 October 2026.",
           "faro-alliance-francaise-de-l-algarve": "Computer-based TCF on the date the candidate chooses (at least 7 days ahead)."},
))

# ===========================================================================
# ROMANIA — TCF
# ===========================================================================
PAGES.append(en("tcf-roumanie",
    slug="tcf-canada-romania", country_name="Romania", crumb="TCF Canada in Romania",
    title="TCF Canada in Romania: Bucharest, Cluj, Timișoara",
    desc="TCF Canada in Romania: the Instituts français in Bucharest, Cluj-Napoca and Timișoara, on computer; in Timișoara, 4 November and December 2026.",
    h1="TCF Canada in Romania: the three Instituts français, sessions and registration",
    intro="""In Romania, the three centres approved for the TCF are branches of the <strong>Institut français</strong> —
<strong>Bucharest</strong>, <strong>Cluj-Napoca</strong> and <strong>Timișoara</strong> —, and all three present the TCF
Canada, on computer. Timișoara publishes a calendar: <strong>4 November</strong> (registration until 27 October),
18 November, 9 and 16 December 2026. In Cluj-Napoca, you set your date with the office at least 10 working days ahead;
Bucharest refers candidates to its registration office. None of the three published its fee on 26 October 2026.""",
    facts=["<strong>3 approved centres</strong> (FEI list of 26 October 2026), all Instituts français, all computer-based, all with the TCF Canada on offer.",
           "Timișoara: sessions on 4 Nov (deadline 27 Oct), 18 Nov (10 Nov), 9 Dec (1 Dec) and 16 Dec 2026 (8 Dec).",
           "Cluj-Napoca: date by appointment, register at least 10 working days ahead; test-day notice by email two days before.",
           "Fees not published: ask the Institut.",
           "The four versions are presented everywhere: tout public, Canada, Québec, IRN."],
    stats=[("3", "approved centres", "Bucharest, Cluj-Napoca, Timișoara"), ("4 Nov", "next session", "Timișoara, deadline 27 Oct"),
           ("10 days", "notice in Cluj", "working days, by appointment"), ("2 years", "validity", "")],
    sections=[
        ("releve", "The TCF in Romania, centre by centre", releve([
            ("Institut français, Timișoara", "tout public, <strong>Canada</strong>, Québec, IRN", "not published",
             "September-December 2026 calendar: 4 Nov (deadline 27 Oct), 18 Nov (10 Nov), 9 Dec (1 Dec), 16 Dec (8 Dec)."),
            ("Institut français, Cluj-Napoca", "tout public, <strong>Canada</strong>, Québec, IRN — computer-based", "not published",
             "By appointment: register at least 10 working days before your chosen date, after contacting the office; test-day notice by email two days before. Writing test on an AZERTY keyboard."),
            ("Institut français, Bucharest", "tout public, <strong>Canada</strong>, Québec, IRN", "not published",
             "No dates online on 26 October 2026: contact the registration office (courses and certifications)."),
        ])),
    ],
    list_title="The {n} approved TCF test centres in Romania",
    faq=[("Where can I take the TCF Canada in Romania?", "At the Institut français, in one of its three approved branches: Bucharest, Cluj-Napoca or Timișoara. All three present the TCF Canada, on computer."),
         ("When is the next TCF in Timișoara?", "On 4 November 2026 (registration until 27 October), then 18 November, 9 and 16 December 2026."),
         ("How much does the TCF Canada cost in Romania?", "The Instituts français did not publish their fee on 26 October 2026: ask the registration office."),
         ("How do I register in Cluj-Napoca?", "Agree on a date with the Institut’s office, at least 10 working days ahead; the test-day notice arrives by email two days before the exam.")],
    also=[("/en/tcf-canada-poland/", "TCF Canada in Poland", "Warsaw and Kraków."), ("/en/tcf-canada-greece/", "TCF Canada in Greece", "Athens, six sessions to June 2027."), _CLB, _PRACTICE],
    sources="the TCF-TEF pages of the Instituts français in Bucharest, Cluj-Napoca and Timișoara (institutfrancais.ro), checked on 26 October 2026.",
))

# ===========================================================================
# POLAND — TCF
# ===========================================================================
PAGES.append(en("tcf-pologne",
    slug="tcf-canada-poland", country_name="Poland", crumb="TCF Canada in Poland",
    title="TCF Canada in Poland: Warsaw, Kraków, dates",
    desc="TCF Canada in Poland: the Institut français in Warsaw (session on 27 November 2026, registration until 27 October) and in Kraków.",
    h1="TCF Canada in Poland: Warsaw and Kraków, sessions and registration",
    intro="""In Poland, the TCF is held at the <strong>Institut français de Pologne</strong>, in <strong>Warsaw</strong> and
<strong>Kraków</strong>. In Warsaw, each of the 8 sessions of 2026 included the TCF Canada; the last one of the year is on
<strong>27 November 2026</strong>, with registration until <strong>27 October</strong>, and the 2027 calendar was not yet
published on 26 October 2026. Kraków also presents the TCF Canada. Fees are not online; you register with a downloadable
form.""",
    facts=["<strong>2 approved centres</strong> (FEI list of 26 October 2026), the two branches of the Institut français de Pologne.",
           "Warsaw: 8 sessions in 2026, all with the TCF Canada, alternating with the TCF Québec or the TCF IRN; registration closes one month before.",
           "Last 2026 session: <strong>27 Nov</strong> (tout public, DAP, IRN, Canada), registration until <strong>27 Oct</strong>.",
           "Registration: form to download from the Institut’s TCF Canada page; fee not published.",
           "Kraków: TCF Canada, Québec, IRN, tout public and DAP pages; dates not published.",
           "TEF Canada, the other test IRCC accepts: sessions published by the Alliance française in Łódź on 26 October 2026."],
    stats=[("2", "approved centres", "Warsaw and Kraków"), ("27 Nov", "last 2026 session", "in Warsaw"),
           ("27 Oct", "registration deadline", "one month before"), ("8", "sessions in 2026", "all with the TCF Canada")],
    sections=[
        ("releve", "The TCF in Poland", releve([
            ("Institut français de Pologne – Warsaw", "<strong>Canada</strong>, Québec, IRN, tout public, DAP", "not published",
             "2026: 27 Feb, 27 Mar, 17 Apr, 29 May, 19 Jun, 25 Sep, 23 Oct and <strong>27 Nov</strong> (registration until 27 Oct), TCF Canada every time; 2027 not published. Downloadable registration form."),
            ("Institut français de Pologne – Kraków", "<strong>Canada</strong>, Québec, IRN, tout public, DAP", "not published", "Dates not published."),
        ])),
    ],
    list_title="The {n} approved TCF test centres in Poland",
    faq=[("Where can I take the TCF Canada in Poland?", "At the Institut français de Pologne, in Warsaw (Plac Europejski 3) or Kraków: they are the two approved TCF centres, and both present the Canada version."),
         ("When is the next TCF Canada in Warsaw?", "On 27 November 2026, with registration until 27 October 2026. The 2027 calendar was not published on 26 October 2026; in 2026, the Institut held 8 sessions, all with the TCF Canada."),
         ("How much does the TCF Canada cost in Poland?", "The Institut français did not publish its fee on 26 October 2026: it appears on the registration form or can be obtained from the exams office."),
         ("Where can I take the TEF Canada in Poland?", "The map of Le français des affaires showed TEF Canada sessions at the Alliance française in Łódź on 26 October 2026.")],
    also=[("/en/tcf-canada-germany/", "TCF Canada in Germany", "Berlin, €295, sessions every month."), ("/en/tcf-canada-romania/", "TCF Canada in Romania", "Bucharest, Cluj, Timișoara."), _TEF, _PRACTICE],
    sources="the TCF pages of the Institut français de Pologne (Warsaw and Kraków) and its 2026 TCF session calendar (PDF), and the TEF centre map of Le français des affaires, checked on 26 October 2026.",
))

# ===========================================================================
# GREECE — TCF
# ===========================================================================
PAGES.append(en("tcf-grece",
    slug="tcf-canada-greece", country_name="Greece", crumb="TCF Canada in Greece",
    title="TCF Canada in Greece: Athens, 2026-2027 dates",
    desc="TCF Canada in Greece: the Institut français in Athens, on 19 November 2026 (registration 2 to 5 November), then five sessions up to June 2027.",
    h1="TCF Canada in Greece: Athens and Thessaloniki, dates and registration",
    intro="""In Greece, the TCF Canada is held at the <strong>Institut français de Grèce</strong> in Athens: its 2026-2027
calendar brings together the TCF tout public, TCF Québec, TCF Canada and TCF IRN on <strong>19 November 2026</strong> —
registration from <strong>2 to 5 November</strong> only —, then on 21 January, 25 February, 24 March, 22 April and 17 June
2027. The Institut français in Thessaloniki presents the TCF at €100, without mentioning the Canada version. In Athens,
each registration window lasts only four days.""",
    facts=["<strong>2 approved centres</strong> (FEI list of 26 October 2026): the Instituts français in Athens and Thessaloniki, on computer.",
           "Athens: 6 TCF sessions, TCF Canada included, from November 2026 to June 2027; a 4-day registration window, set for each session.",
           "Next: <strong>19 Nov 2026</strong>, registration 2 to 5 Nov; then 21 Jan 2027, registration 30 Nov to 3 Dec 2026.",
           "2027: 25 Feb (registration 1 to 4 Feb), 24 Mar (1 to 4 Mar), 22 Apr (5 to 8 Apr), 17 Jun (31 May to 3 Jun).",
           "TCF Canada fee not published in Athens; Thessaloniki shows €100 for the TCF, without specifying the version."],
    stats=[("2", "approved centres", "Athens and Thessaloniki"), ("19 Nov", "next session", "Athens"),
           ("4 days", "to register", "2 to 5 November"), ("6", "sessions", "Nov 2026 to Jun 2027")],
    sections=[
        ("releve", "The TCF in Greece", releve([
            ("Institut français de Grèce (Athens)", "tout public, Québec, <strong>Canada</strong>, IRN", "not published",
             "19 Nov 2026 (registration 2 to 5 Nov), 21 Jan 2027 (30 Nov to 3 Dec 2026), 25 Feb (1 to 4 Feb), 24 Mar (1 to 4 Mar), 22 Apr (5 to 8 Apr), 17 Jun 2027 (31 May to 3 Jun). Registration file to download."),
            ("Institut français, Thessaloniki", "TCF (version not specified)", "€100", "Dates not published: contact the exams office."),
        ])),
    ],
    list_title="The {n} approved TCF test centres in Greece",
    faq=[("Where can I take the TCF Canada in Greece?", "At the Institut français de Grèce, 31 Sina Street in Athens: its 2026-2027 calendar includes the TCF Canada at every session. The Institut français in Thessaloniki presents the TCF without specifying the Canada version."),
         ("When is the next TCF Canada in Athens?", "On 19 November 2026, with registration from 2 to 5 November only; then on 21 January 2027 (registration from 30 November to 3 December 2026)."),
         ("What are the 2027 TCF dates in Greece?", "In Athens: 21 January, 25 February, 24 March, 22 April and 17 June 2027, each with a four-day registration window."),
         ("How much does the TCF cost in Greece?", "Thessaloniki shows €100 for the TCF; the Institut français in Athens does not publish its fee in its calendar.")],
    also=[("/en/tcf-canada-italy/", "TCF Canada in Italy", "Seven centres, €210 to €250."), ("/en/tcf-canada-romania/", "TCF Canada in Romania", "Bucharest, Cluj, Timișoara."), _CLB, _PRACTICE],
    sources="the “Examens du TCF – sessions 2026-2027” calendar (PDF) and the exams page of the Institut français de Grèce (ifg.gr); the TCF page of the Institut français in Thessaloniki (ift.gr); all checked on 26 October 2026.",
    notes={"athenes-institut-francais": "FEI gives ifa.gr, which redirects to ifg.gr."},
))

# ===========================================================================
# IRELAND — TCF
# ===========================================================================
PAGES.append(en("tcf-irlande",
    slug="tcf-canada-ireland", country_name="Ireland", crumb="TCF Canada in Ireland",
    title="TCF Canada in Ireland: Dublin and Galway, €270",
    desc="TCF Canada in Ireland: €270 at the Alliance française in Dublin, with sessions every month, and at the French Institute in Galway. Registration, results.",
    h1="TCF Canada in Ireland: Dublin and Galway, fees and registration",
    intro="""In Ireland, two centres are approved for the TCF, and <strong>both show the TCF Canada at €270</strong>: the
<strong>Alliance française de Dublin</strong>, which holds TEF and TCF sessions every month on its computers, and
<strong>The French Institute in Galway</strong>. In Dublin, you register by email with a copy of your passport, no later than
one month before the exam; results arrive in two to three weeks. In Galway, dates are given on request.""",
    facts=["<strong>2 approved centres</strong> (FEI list of 26 October 2026): the Alliance française de Dublin and The French Institute (Galway).",
           "<strong>TCF Canada: €270</strong> at both; in Dublin, TCF IRN €270, TCF Québec €270 (all four tests), TCF tout public €300.",
           "Dublin: sessions “every month”; registration closes one month before each exam; the test is taken on the centre’s computers.",
           "Results in 2 to 3 weeks in Dublin; results certificate valid for 2 years.",
           "Galway: dates on request."],
    stats=[("2", "approved centres", "Dublin and Galway"), ("€270", "TCF Canada", "at both centres"),
           ("1 month", "notice in Dublin", "deadline before the exam"), ("2 to 3 wks", "for results", "in Dublin")],
    sections=[
        ("releve", "The TCF in Ireland", releve([
            ("Alliance française de Dublin", "<strong>Canada</strong>, Québec, IRN, tout public — on the centre’s computers",
             "Canada <strong>€270</strong> · IRN €270 · Québec €270 (€60 to €90 per test) · tout public €300 (€150 for the compulsory tests)",
             "Sessions every month; register by email with the exams office, with a copy of your passport, no later than one month before; results in 2 to 3 weeks."),
            ("The French Institute (Galway)", "<strong>Canada</strong>, Québec, IRN, tout public", "Canada <strong>€270</strong>", "Dates on request."),
        ])),
    ],
    list_title="The {n} approved TCF test centres in Ireland",
    faq=[("Where can I take the TCF Canada in Ireland?", "At the Alliance française de Dublin, 1 Kildare Street, or at The French Institute in Galway: both approved centres show the TCF Canada at €270."),
         ("How much does the TCF Canada cost in Ireland?", "€270 in Dublin and in Galway, as checked on 26 October 2026. In Dublin, the TCF IRN also costs €270 and the full TCF tout public €300."),
         ("When is the next TCF Canada in Dublin?", "The Alliance française de Dublin holds TEF and TCF sessions every month; registration closes one month before each exam. You book by email with the exams office."),
         ("When do the results arrive?", "Two to three weeks after the exam in Dublin; the results certificate is valid for two years.")],
    also=[("/en/tcf-canada-uk/", "TCF Canada in the UK", "London £260, Glasgow £325."), ("/en/tcf-canada-belgium/", "TCF Canada in Belgium", "Brussels €268, Ghent €260."), _CLB, _PRACTICE],
    sources="the “Exams & Certification” and “TEF-TCF” pages of the Alliance française de Dublin and the TCF page of The French Institute in Galway, checked on 26 October 2026.",
))


# ===========================================================================
# /en/ hub: a Europe section (called from pays_config_en.py, after HUB is defined).
# ===========================================================================
def hub_patch(hub):
    rows = [("Germany", '<a href="/en/tcf-canada-germany/">10 centres, €295 (Erlangen €210)</a>', '<a href="/en/delf-germany/">2027 dates, B2 €201</a>'),
            ("Switzerland", '<a href="/en/tcf-canada-switzerland/">Montreux CHF 290, Zurich</a>', '<a href="/en/delf-switzerland/">2027 dates, B2 CHF 370–390</a>'),
            ("Belgium", '<a href="/en/tcf-canada-belgium/">Brussels €268, Ghent €260</a>', '<a href="/en/tcf-canada-belgium/#delf">6 centres</a>'),
            ("Italy", '<a href="/en/tcf-canada-italy/">7 centres, €210 to €250</a>', "—"),
            ("Netherlands", '<a href="/en/tcf-canada-netherlands/">Amsterdam €290, The Hague, Rotterdam</a>', "—"),
            ("Portugal", '<a href="/en/tcf-canada-portugal/">Porto and Faro €220, Viseu €211</a>', "—"),
            ("Romania", '<a href="/en/tcf-canada-romania/">Bucharest, Cluj-Napoca, Timișoara</a>', "—"),
            ("Poland", '<a href="/en/tcf-canada-poland/">Warsaw, Kraków</a>', "—"),
            ("Greece", '<a href="/en/tcf-canada-greece/">Athens, 6 sessions to June 2027</a>', "—"),
            ("Ireland", '<a href="/en/tcf-canada-ireland/">Dublin and Galway, €270</a>', "—")]
    block = ('\n<h2 id="europe">Europe: TCF Canada and DELF, country by country</h2>\n'
             "<p>Ten more countries, checked on 26 October 2026 against France Éducation international’s list and each centre’s "
             "website: which centres advertise the TCF Canada, their fees in local currency, the next sessions — and, for Germany "
             "and Switzerland, the 2027 DELF calendar.</p>\n"
             + table("TCF Canada and DELF-DALF in Europe, from each centre’s website on 26 October 2026. Spain, in Spanish: "
                     "<a href=\"/es/tcf-canada-espana/\" lang=\"es\">TCF Canada en España</a>.",
                     ["Country", "TCF Canada", "DELF · DALF"], [(f"<strong>{p}</strong>", a, b) for p, a, b in rows], wide=False) + "\n")
    marker = '\n<h2 id="prepare">'
    if 'id="europe"' not in hub["body"] and marker in hub["body"]:
        hub["body"] = hub["body"].replace(marker, block + marker, 1)
        keys = [k for k, _ in hub["toc"]]
        i = keys.index("countries") + 1 if "countries" in keys else len(keys)
        hub["toc"] = hub["toc"][:i] + [("europe", "Europe")] + hub["toc"][i:]
    return hub
