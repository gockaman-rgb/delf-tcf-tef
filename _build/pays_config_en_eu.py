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


_EUR = ("/en/#europe", "TCF Canada and DELF in Europe", "Country by country: who offers the TCF Canada, and fees.")
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
           "DELF-DALF: 6 centres in Belgium; session from 17 to 26 November 2026, registration until 3 November in Ghent (closed in Brussels); 2027 not yet scheduled."],
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
sale yet and fees were not shown; the Alliance’s students get 10% off. In Ghent, November registration stays open until
3 November: dates, fees and centres on our page <a href="/en/delf-belgium/">DELF exam dates 2027 in Belgium</a>.</p>"""),
    ],
    list_title="The {n} approved TCF test centres in Belgium",
    faq=[("Where can I take the TCF Canada in Belgium?", "At the Alliance française de Bruxelles-Europe, avenue des Arts 46 (€268), or at the Alliance française de Flandre orientale, Henleykaai 86 in Ghent (€260): they are the country’s two approved TCF centres, and both offer the Canada version, on computer."),
         ("When is the next TCF Canada in Brussels?", "On Wednesday 9 December 2026, from 10:00 to 12:40 for the written tests, with the speaking test in the afternoon. Ghent had not published its 2027 sessions on 26 October 2026."),
         ("How much does the TCF Canada cost in Belgium?", "€268 in Brussels and €260 in Ghent. The TCF tout public costs €258 in Brussels and €250 in Ghent, the TCF IRN €220 in Brussels."),
         ("When will I get my results?", "In Brussels, a provisional certificate is handed out on the test day and the France Éducation international certificate arrives within two weeks; in Ghent, the full results arrive within 15 working days."),
         ("Can I take the DELF in Brussels in 2027?", "Yes, but the 2027 sessions were not yet scheduled on 26 October 2026. In 2026, the Alliance de Bruxelles-Europe held four: March, June, September and November.")],
    also=[("/en/delf-belgium/", "DELF exam dates 2027 in Belgium", "17 to 26 November 2026, B2 €191 in Ghent."),
          ("/en/tcf-canada-netherlands/", "TCF Canada in the Netherlands", "Amsterdam €290, The Hague, Rotterdam."),
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
    also=[("/en/delf-italy/", "DELF exam dates 2027 in Italy", "February, April and June 2027, B2 €160."),
          ("/en/tcf-canada-switzerland/", "TCF Canada in Switzerland", "ALPADIA (Montreux) and the Alliance in Zurich."),
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
    also=[("/en/delf-netherlands/", "DELF exam dates 2027 in the Netherlands", "March and June 2027 in Amsterdam, B2 €175."),
          ("/en/tcf-canada-belgium/", "TCF Canada in Belgium", "Brussels €268, Ghent €260."),
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
    also=[("/en/delf-portugal/", "DELF exam dates 2027 in Portugal", "The national calendar, B2 €140."),
          ("/en/tcf-canada-italy/", "TCF Canada in Italy", "Seven centres, €210 to €250."),
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
    also=[("/en/delf-romania/", "DELF exam dates 2027 in Romania", "14 and 15 November 2026, registration until 3 November."),
          ("/en/tcf-canada-poland/", "TCF Canada in Poland", "Warsaw and Kraków."), ("/en/tcf-canada-greece/", "TCF Canada in Greece", "Athens, six sessions to June 2027."), _CLB, _PRACTICE],
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
    also=[("/en/delf-poland/", "DELF exam dates 2027 in Poland", "16 to 20 November 2026, B2 at 620 zł."),
          ("/en/tcf-canada-germany/", "TCF Canada in Germany", "Berlin, €295, sessions every month."), ("/en/tcf-canada-romania/", "TCF Canada in Romania", "Bucharest, Cluj, Timișoara."), _TEF, _PRACTICE],
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
    also=[("/en/delf-greece/", "DELF exam dates 2027 in Greece", "B2 on 15 May 2027, registration 1 to 15 February."),
          ("/en/tcf-canada-italy/", "TCF Canada in Italy", "Seven centres, €210 to €250."), ("/en/tcf-canada-romania/", "TCF Canada in Romania", "Bucharest, Cluj, Timișoara."), _CLB, _PRACTICE],
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
    also=[("/en/delf-ireland/", "DELF exam dates 2027 in Ireland", "Five sessions in 2027, B2 €145 in Dublin."),
          ("/en/tcf-canada-uk/", "TCF Canada in the UK", "London £260, Glasgow £325."), ("/en/tcf-canada-belgium/", "TCF Canada in Belgium", "Brussels €268, Ghent €260."), _CLB, _PRACTICE],
    sources="the “Exams & Certification” and “TEF-TCF” pages of the Alliance française de Dublin and the TCF page of The French Institute in Galway, checked on 26 October 2026.",
))


# ===========================================================================
# /en/ hub: a Europe section (called from pays_config_en.py, after HUB is defined).
# ===========================================================================
def hub_patch(hub):
    rows = [("Germany", '<a href="/en/tcf-canada-germany/">10 centres, €295 (Erlangen €210)</a>', '<a href="/en/delf-germany/">2027 dates, B2 €201</a>'),
            ("Switzerland", '<a href="/en/tcf-canada-switzerland/">Montreux CHF 290, Zurich</a>', '<a href="/en/delf-switzerland/">2027 dates, B2 CHF 370–390</a>'),
            ("Belgium", '<a href="/en/tcf-canada-belgium/">Brussels €268, Ghent €260</a>', '<a href="/en/delf-belgium/">17–26 Nov 2026, B2 €191 in Ghent</a>'),
            ("Italy", '<a href="/en/tcf-canada-italy/">7 centres, €210 to €250</a>', '<a href="/en/delf-italy/">2027 dates, B2 €160</a>'),
            ("Netherlands", '<a href="/en/tcf-canada-netherlands/">Amsterdam €290, The Hague, Rotterdam</a>', '<a href="/en/delf-netherlands/">March and June 2027, B2 €175</a>'),
            ("Portugal", '<a href="/en/tcf-canada-portugal/">Porto and Faro €220, Viseu €211</a>', '<a href="/en/delf-portugal/">National calendar, B2 €140</a>'),
            ("Romania", '<a href="/en/tcf-canada-romania/">Bucharest, Cluj-Napoca, Timișoara</a>', '<a href="/en/delf-romania/">14–15 Nov 2026</a>'),
            ("Poland", '<a href="/en/tcf-canada-poland/">Warsaw, Kraków</a>', '<a href="/en/delf-poland/">16–20 Nov 2026, B2 620 zł</a>'),
            ("Greece", '<a href="/en/tcf-canada-greece/">Athens, 6 sessions to June 2027</a>', '<a href="/en/delf-greece/">15 May 2027, B2 €160</a>'),
            ("Ireland", '<a href="/en/tcf-canada-ireland/">Dublin and Galway, €270</a>', '<a href="/en/delf-ireland/">2027 dates, B2 €145 in Dublin</a>'),
            ("Austria", '<a href="/en/tcf-canada-austria/">Vienna €295</a>', '<a href="/en/tcf-canada-austria/#delf">27–29 Jan 2027 (Vienna)</a>'),
            ("Luxembourg", '<a href="/en/tcf-canada-luxembourg/">Not offered (TCF IRN €150)</a>', '<a href="/en/tcf-canada-luxembourg/#delf">B2 €186</a>'),
            ("Sweden", '<a href="/en/delf-sweden/#tcf">No TCF centre; TEF Canada SEK 2,900</a>', '<a href="/en/delf-sweden/">3 sessions a year, B2 SEK 1,450</a>')]
    block = ('\n<h2 id="europe">Europe: TCF Canada and DELF, country by country</h2>\n'
             "<p>Thirteen more countries, checked on 26 October 2026 against France Éducation international’s list and each "
             "centre’s website: which centres advertise the TCF Canada, their fees in local currency, the next sessions — and the "
             "DELF dates, for 2027 where they are published.</p>\n"
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


# ###########################################################################
# CONTINUED (26/10/2026, afternoon): DELF-DALF in Italy, Romania, the Netherlands, Greece, Poland, Belgium, Portugal,
# Ireland and Sweden; TCF (and DELF) in Austria and Luxembourg. Translations of the specs appended to pays_config_eu.py.
# ###########################################################################
BADGES.update({"pas de TCF Canada": "no TCF Canada"})
OG.update({"delf-italie": "en_IT", "delf-roumanie": "en_RO", "delf-pays-bas": "en_NL", "delf-grece": "en_GR", "delf-pologne": "en_PL",
           "delf-belgique": "en_BE", "delf-portugal": "en_PT", "delf-irlande": "en_IE", "delf-suede": "en_SE",
           "tcf-autriche": "en_AT", "tcf-luxembourg": "en_LU"})
_NO_LINK = "Website listed by FEI unreachable on 26 October 2026."

# ===========================================================================
# ITALY — DELF-DALF
# ===========================================================================
PAGES.append(en("delf-italie",
    slug="delf-italy", country_name="Italy", crumb="DELF in Italy",
    title="DELF exam dates 2027 Italy: fees, test centres",
    desc="DELF exam dates 2027 in Italy: B2 on 25 February, 8 April and 16 June, registration windows, fees (B2 €160, €144 reduced) and the {n} centres.",
    h1="DELF exam dates 2027 in Italy: the 2026-2027 calendar, fees and the {n} centres",
    intro="""<strong>DELF exam dates 2027 in Italy</strong> (<span lang="it">date esami DELF 2027</span>): the DELF B2 written
paper is on <strong>25 February</strong>, 8 April and 16 June 2027, in the calendar published identically by the Institut
français in Milan and the Alliance française in Turin. Registration for February runs from <strong>2 November to
4 December 2026</strong>; the November 2026 session (10 to 13 November) closed on 2 October. The DELF B2 costs
<strong>€160</strong>, or €144 at the reduced rate, in Milan, Turin and Rome.""",
    facts=["<strong>{n} test centres</strong> (FEI list of 26 October 2026): the Instituts français in Milan, Florence, Naples and Palermo, the Centre Saint-Louis in Rome, the Lycée Victor-Hugo in Florence and twenty Alliances françaises.",
           "February 2027: C2 on the 18th, C1 on the 19th, A1 and A2 on the 23rd, B1 on the 24th, <strong>B2 on 25 February</strong>; registration from 2 November to 4 December 2026 (same dates in Naples).",
           "April 2027: C1 on the 5th, C2 on the 6th, B1 on the 7th, <strong>B2 on the 8th</strong>, A1 and A2 on 9 April; registration until 19 February. In Milan, April only opens B2, C1 and C2.",
           "June 2027: C2 on the 14th, C1 on the 15th, <strong>B2 on the 16th</strong>, B1 on the 17th, A1 and A2 on 18 June; registration until 23 April 2027.",
           "Fees in Milan, Turin and Rome: <strong>A1 €80 · A2 €90 · B1 €125 · B2 €160 · C1 and C2 €195</strong>; reduced rate €72 to €176.",
           "The calendar covers the 2026-2027 year: the November 2027 session was not published on 26 October 2026."],
    stats=[("{n}", "test centres", "FEI list of 26 October 2026"), ("€160", "DELF B2", "€144 at the reduced rate"),
           ("25 Feb", "next B2", "registration until 4 Dec"), ("3", "sessions in 2027", "February, April, June")],
    sections=[
        ("exam-dates", "The 2026-2027 DELF-DALF calendar", table(
            "Dates of the collective written papers, identical in the 2026-2027 calendars of the Institut français in Milan and the Alliance française in Turin, checked on 26 October 2026. Speaking tests take place during the session month.",
            ["Session", "A1", "A2", "B1", "B2", "C1", "C2", "Registration"],
            [("Nov 2026", "10 Nov", "11 Nov", "11 Nov", "10 Nov", "12 Nov", "13 Nov", "closed on 2 Oct"),
             ("<strong>Feb 2027</strong>", "23 Feb", "23 Feb", "24 Feb", "<strong>25 Feb</strong>", "19 Feb", "18 Feb", "2 Nov to 4 Dec 2026"),
             ("Apr 2027", "9 Apr", "9 Apr", "7 Apr", "8 Apr", "5 Apr", "6 Apr", "until 19 Feb (Milan: 1 to 19 Feb)"),
             ("Jun 2027", "18 Jun", "18 Jun", "17 Jun", "16 Jun", "15 Jun", "14 Jun", "until 23 Apr (Milan: 1 to 23 Apr)")]) + """
<p>Speaking tests run from 2 to 30 November 2026, 1 to 26 February, 1 to 30 April and 1 to 30 June 2027. The Alliance in
Turin warns that registration closes well ahead of the papers. The Institut français in Naples announces four sessions a
year (November, February, March-April, June) with the same February window; the Centre Saint-Louis in Rome gives the same
months and warns that the speaking test may come before the written papers. Not every centre opens every level at every
session.</p>"""),
        ("fees", "How much does the DELF cost in Italy?", table(
            "2026-2027 fees of the Alliance française in Turin, the same as at the Institut français in Milan and the Centre Saint-Louis in Rome, checked on 26 October 2026.",
            ["Level", "Full fee", "Reduced fee"],
            [("DELF A1", "€80", "€72"), ("DELF A2", "€90", "€81"), ("DELF B1", "€125", "€113"),
             ("<strong>DELF B2</strong>", "<strong>€160</strong>", "<strong>€144</strong>"), ("DALF C1", "€195", "€176"),
             ("DALF C2", "€195", "€176"), ("DELF scolaire A1 to B2 (Turin)", "€68 to €135", "—"), ("DELF Prim A1.1 to A2 (Turin)", "€50 to €78", "—")], wide=False) + """
<p>Depending on the centre, the reduced rate is for under-18s, secondary-school pupils, the centre’s own students and
students of partner universities (in Milan: Insubria, Pavia, Bicocca, as well as French teachers). The Centre Saint-Louis
does not refund exam fees.</p>"""),
        ("registration", "Registration, results and diploma", """<p>You register with your chosen centre — online at the
Institut français in Milan, with the exams office elsewhere — during the session’s window. The diplomas are independent:
you register directly for the level you want, and you need 50 points out of 100 to pass.</p>

<p>The DELF scolaire, at a preferential fee (€68 for A1, €135 for B2 in Turin), is organised with schools; the DELF Prim
is for children. Centres publish each session’s results on their websites.</p>"""),
    ],
    list_title="The {n} DELF-DALF test centres, city by city",
    faq=[("What are the DELF exam dates 2027 in Italy?", "According to the 2026-2027 calendar of the Institut français in Milan and the Alliance française in Turin, the DELF B2 is on 25 February, 8 April and 16 June 2027; registration for February runs from 2 November to 4 December 2026. The November 2027 session was not published on 26 October 2026."),
         ("How much does the DELF B2 cost in Italy?", "€160, or €144 at the reduced rate, in Milan, Turin and Rome. The DALF C1 and DALF C2 cost €195 (€176 at the reduced rate)."),
         ("Can I still register for November 2026?", "No: registration for the November 2026 session (written papers from 10 to 13 November) closed on 2 October. The next one is February 2027, with registration from 2 November to 4 December 2026."),
         ("Where can I take the DELF in Rome or Milan?", "In Rome, at the Institut français – Centre Saint-Louis (Largo Toniolo); in Milan, at the Institut français (Corso Magenta 63). Both charge the same fees, €160 for B2."),
         ("Do I need A1 before B2?", "No: the DELF and DALF diplomas are independent, so you register directly for the level you want.")],
    also=[("/en/tcf-canada-italy/", "TCF Canada in Italy", "Seven centres advertise it, €210 to €250."),
          ("/en/delf-switzerland/", "DELF exam dates 2027 in Switzerland", "The national calendar, B2 from CHF 370 to 390."), _DATES, _DELF],
    sources="the 2026-2027 DELF-DALF tout public calendar (PDF) and “DELF DALF – tout public” page of the Institut français in Milan; the 2026-2027 DELF-DALF tout public calendar and 2026-2027 fees (PDFs) of the Alliance française in Turin; the DELF-DALF pages of the Institut français in Naples and the Centre Saint-Louis in Rome; all checked on 26 October 2026.",
    notes={"cagliari-alliance-francaise-de-cagliari": "Website listed by FEI out of service on 26 October 2026.",
           "sassari-alliance-francaise-sassari-c-o-liceo-statale-margherita-di-castelvi": "Website listed by FEI restricted to Google accounts on 26 October 2026.",
           "vintimille-alliance-francaise-vintimille": "FEI gives no valid website address.",
           "trieste-alliance-francaise-trieste": "Empty website on 26 October 2026."},
))

# ===========================================================================
# ROMANIA — DELF-DALF
# ===========================================================================
PAGES.append(en("delf-roumanie",
    slug="delf-romania", country_name="Romania", crumb="DELF in Romania",
    title="DELF exam dates 2027 Romania: sessions, centres",
    desc="DELF and DALF in Romania: 2027 dates not yet published; the 14–15 November 2026 session (registration until 3 November), results, the {n} centres.",
    h1="DELF exam dates 2027 in Romania: sessions, registration and the {n} centres",
    intro="""The <strong>DELF exam dates 2027 in Romania</strong> (<span lang="ro">date examen DELF 2027</span>) were not yet
published on 26 October 2026. The next session is on <strong>14 and 15 November 2026</strong>, with online registration
open until <strong>3 November</strong> and results on 17 December. The DELF and DALF are held at <strong>{n} centres</strong>
— the Institut français branches in Bucharest, Cluj-Napoca, Iași and Timișoara and six Alliances françaises —, under the
central management of the Institut français de Roumanie; in 2026, Bucharest held four sessions (February, April, June,
November).""",
    facts=["<strong>{n} test centres</strong> (FEI list of 26 October 2026): the Instituts français in Bucharest, Cluj-Napoca, Iași and Timișoara, and the Alliances françaises in Brașov, Constanța, Craiova, Pitești, Ploiești and Suceava.",
           "November 2026: papers on <strong>14 and 15 November</strong>, registration from 14 September to <strong>3 November</strong>, results on 17 December (Bucharest, Cluj-Napoca, Iași).",
           "Bucharest, 2026: 14–15 February, 4–5 April, 6–7 June and 14–15 November; Cluj-Napoca and Iași: 14–15 March, 6–7 June and 14–15 November.",
           "In November 2026, the Institut in Cluj-Napoca also runs the exam in Oradea; in March, it went to Bistrița, Satu Mare, Sibiu and Târgu Mureș.",
           "Fees not shown on the Instituts’ DELF-DALF pages on 26 October 2026: ask the office.",
           "Diploma 4 to 5 months after the results are posted (Iași); online registration, with a tutorial."],
    stats=[("{n}", "test centres", "4 Instituts français, 6 Alliances"), ("14–15 Nov", "next session", "2026"),
           ("3 Nov", "registration deadline", "online"), ("17 Dec", "results", "November session")],
    sections=[
        ("exam-dates", "The Instituts français’ 2026 sessions", table(
            "DELF-DALF tout public sessions published by the Instituts français in Bucharest, Cluj-Napoca and Iași, checked on 26 October 2026. The 2027 calendar was not online yet.",
            ["Session", "Papers", "Registration", "Results", "Where"],
            [("February 2026", "14–15 Feb", "1 Jan – 4 Feb", "12 Mar", "Bucharest"),
             ("March 2026", "14–15 Mar", "1 Jan – 2 Mar", "16 Apr", "Cluj-Napoca (and Bistrița, Satu Mare, Sibiu, Târgu Mureș), Iași"),
             ("April 2026", "4–5 Apr", "2 Mar – 25 Mar", "16 Apr", "Bucharest"),
             ("June 2026", "6–7 Jun", "20 Apr – 26 May", "18 Jun", "Bucharest, Cluj-Napoca, Iași"),
             ("<strong>November 2026</strong>", "<strong>14–15 Nov</strong>", "14 Sep – <strong>3 Nov</strong>", "17 Dec", "Bucharest, Cluj-Napoca (and Oradea), Iași")]) + """
<p>The DELF junior has its own calendar: in Iași, 14–15 March, 23–24 May and 14–15 November 2026, with spring papers in
Piatra-Neamț, Focșani and Galați. Timișoara and the six Alliances françaises on the list were not checked: their contact
details are below.</p>"""),
        ("registration", "Registration and diploma", """<p>You register online, on the website of your chosen Institut français
branch, which publishes a tutorial; the DELF-DALF rules are attached to each page. The diplomas are independent: you
register directly for the level you want, and you need 50 points out of 100 to pass.</p>

<p>In Bucharest, you collect the diploma from the registration office (courses and exams) with an ID; in Iași, it arrives
4 to 5 months after the results are posted. Fees are not on these pages: ask the registration office of your chosen
branch.</p>"""),
    ],
    list_title="The {n} DELF-DALF test centres, city by city",
    faq=[("What are the DELF exam dates 2027 in Romania?", "Not yet published: on 26 October 2026, the Instituts français in Romania only listed their 2026 sessions. Bucharest held four (February, April, June, November), Cluj-Napoca and Iași three (March, June, November)."),
         ("When is the next DELF exam in Romania?", "On 14 and 15 November 2026, at the Instituts français in Bucharest, Cluj-Napoca and Iași; online registration stays open until 3 November, and results are announced on 17 December 2026."),
         ("How much does the DELF cost in Romania?", "The Instituts français did not show their fees on their DELF-DALF pages on 26 October 2026: ask the registration office of your chosen branch."),
         ("When do I get my DELF diploma?", "Results for the November 2026 session are announced on 17 December; in Iași, the diploma arrives 4 to 5 months after the results are posted. In Bucharest, you collect it with an ID.")],
    also=[("/en/tcf-canada-romania/", "TCF Canada in Romania", "Bucharest, Cluj-Napoca, Timișoara."),
          ("/en/delf-poland/", "DELF exam dates 2027 in Poland", "16 to 20 November 2026, B2 at 620 zł."), _DATES, _DELF],
    sources="the adult DELF-DALF pages of the Instituts français in Bucharest, Cluj-Napoca and Iași (institutfrancais.ro) and the DELF junior “Calendar și tarife” page in Iași, checked on 26 October 2026.",
))

# ===========================================================================
# NETHERLANDS — DELF-DALF
# ===========================================================================
PAGES.append(en("delf-pays-bas",
    slug="delf-netherlands", country_name="Netherlands", crumb="DELF in the Netherlands",
    title="DELF exam dates 2027 Netherlands: fees, centres",
    desc="DELF exam dates 2027 in the Netherlands: 9–11 March and 7–11 June in Amsterdam, the November 2026 session, fees (B2 €175) and the {n} centres.",
    h1="DELF exam dates 2027 in the Netherlands: sessions, fees and the {n} centres",
    intro="""<strong>DELF exam dates 2027 in the Netherlands</strong> (<span lang="nl">DELF examendata 2027</span>): the
Alliance française in Amsterdam announces two sessions, from <strong>9 to 11 March</strong> (registration from January) and
from <strong>7 to 11 June 2027</strong> (from April). The November 2026 session, 9 to 13 November, closed registration on
25 and 26 October. The DELF and DALF are held at <strong>{n} centres</strong>, including the Alliances françaises in
Amsterdam, The Hague and Rotterdam and the Institut français in Groningen; the DELF B2 costs <strong>€175</strong>.""",
    facts=["<strong>{n} test centres</strong> (FEI list of 26 October 2026), managed by the Institut français des Pays-Bas (The Hague): three Alliances françaises, the Institut français in Groningen and The Hague, the Lycée français Van Gogh and HAN in Arnhem.",
           "2027 in Amsterdam: <strong>9–11 March</strong> and <strong>7–11 June</strong>; registration opens in January and April 2027. The Hague announces sessions in March, June and November.",
           "November 2026: A1 and A2 on the 9th, B1 on the 10th, B2 on the 11th, C1 on the 12th, C2 on 13 November; registration closed on 25 October in Amsterdam, on 26 October at the Institut français.",
           "Fees (Amsterdam, Institut français): <strong>A1 €110 · A2 €110 · B1 €155 · B2 €175 · C1 €220 · C2 €230</strong>.",
           "DELF junior in Amsterdam: A1 and A2 on 12 April, B1 and B2 on 13 April 2027 (B2 €180); DELF Prim on 26 May 2027.",
           "Rotterdam runs exams “throughout the year”; dates on request."],
    stats=[("{n}", "test centres", "FEI list of 26 October 2026"), ("€175", "DELF B2", "C1 €220, C2 €230"),
           ("9–11 Mar", "first 2027 session", "Amsterdam"), ("2", "sessions announced", "March and June 2027")],
    sections=[
        ("exam-dates", "Sessions 2026-2027", table(
            "DELF-DALF tout public sessions published by the Institut français des Pays-Bas and the Alliance française in Amsterdam, checked on 26 October 2026.",
            ["Session", "Written papers", "Registration", "Where"],
            [("June 2026", "A1 and A2 1 Jun, B1 2 Jun, B2 3 Jun, C1 4 Jun, C2 5 Jun", "12 Jan – 18 May 2026", "Institut français (Groningen)"),
             ("November 2026", "A1 and A2 9 Nov, B1 10 Nov, <strong>B2 11 Nov</strong>, C1 12 Nov, C2 13 Nov", "until 25 Oct (Amsterdam); 1 Jul – 26 Oct (Institut français)", "Amsterdam, Groningen"),
             ("<strong>March 2027</strong>", "9 to 11 March", "from January 2027", "Amsterdam"),
             ("<strong>June 2027</strong>", "7 to 11 June", "from April 2027", "Amsterdam")]) + """
<p>The level-by-level dates for 2027 were not published on 26 October 2026. The Alliance française in The Hague sells its
March, June and November sessions on its website, with no dates or fees spelled out that day; the one in Rotterdam offers
exams throughout the year and points to its DELF-DALF product page.</p>"""),
        ("fees", "How much does the DELF cost in the Netherlands?", table(
            "Fees shown by the Alliance française in Amsterdam and the Institut français des Pays-Bas on 26 October 2026.",
            ["Level", "Tout public", "DELF junior (Amsterdam)"],
            [("A1", "€110", "€110"), ("A2", "€110", "€110"), ("B1", "€155", "€155"),
             ("<strong>B2</strong>", "<strong>€175</strong>", "€180"), ("DALF C1", "€220", "—"), ("DALF C2", "€230", "—"),
             ("DELF Prim A1.1 · A1 · A2 (Amsterdam)", "€65 · €90 · €90", "—")], wide=False)),
        ("registration", "Registration", """<p>Each centre handles its own registrations: in Amsterdam, they open in January for
March and in April for June; in The Hague, one button per session (March, June, November) leads to the Alliance’s booking
module; in Groningen, the Institut français answers by email. The diplomas are independent: you register directly for the
level you want, and you need 50 points out of 100 to pass.</p>"""),
    ],
    list_title="The {n} DELF-DALF test centres, city by city",
    faq=[("What are the DELF exam dates 2027 in the Netherlands?", "The Alliance française in Amsterdam announces two tout public sessions in 2027: 9 to 11 March (registration from January) and 7 to 11 June (from April). The Hague plans sessions in March, June and November; the level-by-level dates were not published on 26 October 2026."),
         ("How much does the DELF B2 cost in the Netherlands?", "€175 at the Alliance française in Amsterdam and the Institut français des Pays-Bas; €110 for A1 or A2, €155 for B1, €220 for the DALF C1 and €230 for C2. The DELF junior B2 costs €180 in Amsterdam."),
         ("Can I still register for November 2026?", "Not in Amsterdam, where registration closed on 25 October; the Institut français took registrations until 26 October 2026. The papers run from 9 to 13 November."),
         ("Where can I take the DELF in The Hague?", "At the Alliance française in The Hague, which runs sessions in March, June and November. The Institut français des Pays-Bas and the Lycée français Van Gogh are also on FEI’s list.")],
    also=[("/en/tcf-canada-netherlands/", "TCF Canada in the Netherlands", "Amsterdam €290, The Hague, Rotterdam."),
          ("/en/delf-belgium/", "DELF exam dates 2027 in Belgium", "17 to 26 November 2026, B2 €191 in Ghent."), _DATES, _DELF],
    sources="the DELF-DALF pages of the Alliance française in Amsterdam, the Alliance française in The Hague, the Alliance française in Rotterdam (exams) and the Institut français des Pays-Bas (DELF-DALF tout public), checked on 26 October 2026.",
    notes={"la-haye-lycee-francais-van-gogh": _NO_LINK},
))

# ===========================================================================
# GREECE — DELF-DALF
# ===========================================================================
PAGES.append(en("delf-grece",
    slug="delf-greece", country_name="Greece", crumb="DELF in Greece",
    title="DELF exam dates 2027 Greece: May session, fees",
    desc="DELF exam dates 2027 in Greece: B2 on Saturday 15 May (registration 1 to 15 February), the 4–5 December 2026 session, fees (B1 and B2 €160).",
    h1="DELF exam dates 2027 in Greece: the December and May sessions, fees and registration",
    intro="""<strong>DELF exam dates 2027 in Greece</strong> (<span lang="el">εξετάσεις DELF 2027</span>): the DELF B1 and B2
are on <strong>Saturday 15 May 2027</strong>, the A1, A2 and DALF on Friday 14 May, with online registration from
<strong>1 to 15 February 2027</strong>. Before that, the December session is on <strong>4 and 5 December 2026</strong>
(registration closed on 11 October). The <strong>Institut français de Grèce</strong>, the only centre on FEI’s list, runs
both sessions in Athens, Thessaloniki and regional centres; the DELF B1 and B2 cost <strong>€160</strong>.""",
    facts=["<strong>1 approved centre</strong> (FEI list of 26 October 2026), the Institut français de Grèce, which sets each session’s exam centres according to the number of candidates per region.",
           "May 2027: A1, A2, C1 and C2 on Friday 14 May; <strong>B1 and B2 on Saturday 15 May</strong>; registration from 1 to 15 February 2027, online only.",
           "December 2026: A1, A2, C1 and C2 on 4 December, B1 and B2 on 5 December; registration closed on 11 October.",
           "2026 fees: <strong>A1 and A2 €75 · B1 and B2 €160 · C1 €180 · C2 €200</strong>.",
           "Speaking tests in Athens and Thessaloniki in the days after the written papers; in regional centres, on the written-paper weekend.",
           "The programme states that no request to change a written or speaking test is accepted."],
    stats=[("1", "approved centre", "the Institut français de Grèce"), ("15 May", "DELF B2 2027", "Saturday, 18:30"),
           ("1–15 Feb", "registration", "online"), ("€160", "DELF B2", "same as B1")],
    sections=[
        ("exam-dates", "The December 2026 and May 2027 sessions", table(
            "DELF-DALF programme of the Institut français de Grèce (versions of 22 July and 14 October 2026), checked on 26 October 2026. Speaking tests in Athens and Thessaloniki; in regional centres, the speaking test is on the written-paper weekend.",
            ["Diploma", "Written, Dec 2026", "Speaking, Dec (Athens, Thess.)", "Written, May 2027", "Speaking, May (Athens, Thess.)"],
            [("DELF A1", "Fri 4 Dec, 17:00", "Mon 7 Dec", "Fri 14 May, 17:00", "10 or 12 May"),
             ("DELF A2", "Fri 4 Dec, 19:00", "Tue 8 Dec", "Fri 14 May, 19:00", "11 or 13 May"),
             ("DELF B1", "Sat 5 Dec, 16:00", "Wed 9 Dec", "Sat 15 May, 16:00", "17 or 18 May"),
             ("<strong>DELF B2</strong>", "<strong>Sat 5 Dec, 18:30</strong>", "Thu 10 Dec", "<strong>Sat 15 May, 18:30</strong>", "19 or 20 May"),
             ("DALF C1", "Fri 4 Dec, 17:00", "Fri 11 Dec", "Fri 14 May, 17:00", "Thu 27 May"),
             ("DALF C2", "Fri 4 Dec, 17:00", "Mon 14 Dec", "Fri 14 May, 17:00", "Sun 23 May")]) + """
<p>Registration: 1 to 11 October 2026 for December (closed), <strong>1 to 15 February 2027</strong> for May. You cannot
register for two diplomas whose times overlap: A1 and C1, for example, both start on Friday at 17:00. The DELF Prim A1 and
A2, for under-12s, follow the A1 and A2 times. The Institut also runs the Sorbonne exams at the same sessions.</p>"""),
        ("fees", "How much does the DELF cost in Greece?", table(
            "2026 exam fees of the Institut français de Grèce (DELF, DALF and Sorbonne), checked on 26 October 2026.",
            ["Level", "Fee"],
            [("DELF A1 · A2", "€75"), ("<strong>DELF B1 · B2</strong>", "<strong>€160</strong>"), ("DALF C1", "€180"), ("DALF C2", "€200")], wide=False) + """
<p>You pay when registering, online by card or at a bank with the payment code the platform issues. These are the fees
shown for 2026; those for the May 2027 session were not published yet.</p>"""),
        ("registration", "Registration and test day", """<p>Registration is online only, on the eservices.ifg.gr platform, which
issues a payment code; it assumes you have read the exam programme and rules. Each session’s exam centres — Athens,
Thessaloniki and regional towns — are only announced when registration closes, according to the number of candidates per
region. You print the test-day notice, with your speaking-test time, from the Institut’s website.</p>

<p>The exams office of the Institut français de Grèce is at 31 Sina Street, Athens; the Institut français in Thessaloniki
also advises candidates in the north. The diplomas are independent: you register directly for the level you want, and you
need 50 points out of 100 to pass.</p>"""),
    ],
    list_title="The approved DELF-DALF test centre in Greece",
    faq=[("What are the DELF exam dates 2027 in Greece?", "For the May 2027 session: DELF A1, A2 and DALF C1, C2 on Friday 14 May, DELF B1 and B2 on Saturday 15 May 2027, with registration from 1 to 15 February 2027. The December 2027 session was not published on 26 October 2026."),
         ("When is the DELF B2 in December 2026?", "On Saturday 5 December 2026, 18:30 to 21:00; the speaking test is on 10 December in Athens and Thessaloniki, on 6 December in regional centres. Registration closed on 11 October."),
         ("How much does the DELF B2 cost in Greece?", "€160, like B1, according to the Institut français de Grèce’s 2026 fees; €75 for A1 or A2, €180 for the DALF C1 and €200 for C2."),
         ("Where is the DELF held in Greece?", "In Athens, Thessaloniki or a regional centre: the Institut français de Grèce, the country’s only approved centre, sets each session’s list of centres when registration closes, according to the number of candidates per region."),
         ("Do I need A1 before B2?", "No: the DELF and DALF diplomas are independent, so you register directly for the level you want. The only rule in Greece: don’t pick two diplomas whose times overlap.")],
    also=[("/en/tcf-canada-greece/", "TCF Canada in Greece", "Athens, six sessions to June 2027."),
          ("/en/delf-italy/", "DELF exam dates 2027 in Italy", "February, April and June 2027, B2 €160."), _DATES, _DELF],
    sources="the December 2026 and May 2027 DELF-DALF-Sorbonne exam programmes (PDFs), the 2026-2027 exam calendar, the 2026 exam fees and the exam pages of the Institut français de Grèce (ifg.gr), checked on 26 October 2026.",
))

# ===========================================================================
# POLAND — DELF-DALF
# ===========================================================================
PAGES.append(en("delf-pologne",
    slug="delf-poland", country_name="Poland", crumb="DELF in Poland",
    title="DELF exam dates 2027 Poland: sessions, fees (zł)",
    desc="DELF and DALF in Poland: 2027 dates not yet published; the 16–20 November 2026 session (B2 on the 18th), registration to 6 November, B2 620 zł.",
    h1="DELF exam dates 2027 in Poland: sessions, fees in złoty and the {n} centres",
    intro="""The <strong>DELF exam dates 2027 in Poland</strong> (<span lang="pl">terminy egzaminów DELF 2027</span>) were not
yet published on 26 October 2026. The next session runs from <strong>16 to 20 November 2026</strong>, with the DELF B2 on
<strong>18 November</strong>; the Alliances françaises take registrations until <strong>6 November</strong>, while at the
Institut français in Warsaw they closed on 18 October. The DELF and DALF are held at <strong>{n} centres</strong> on the
same dates; the B2 costs <strong>620 zł</strong> (527 zł at the reduced rate).""",
    facts=["<strong>{n} test centres</strong> (FEI list of 26 October 2026), under the central management of the Institut français de Pologne: the Institut in Warsaw and Kraków, eight Alliances françaises, the Lycée français de Varsovie, Adam Mickiewicz University in Poznań and three associations.",
           "November 2026: A1 and A2 on the 16th, B1 on the 17th, <strong>B2 on the 18th</strong>, C1 on the 19th, C2 on 20 November; speaking tests from 13 to 25 November at the Alliances.",
           "Registration: until <strong>6 November 2026</strong> at the Alliances françaises; 21 September to 18 October at the Institut français in Warsaw (closed).",
           "In 2026, three tout public sessions: February (B2 on the 4th), June (B2 on the 24th) and November; 2027 dates not published.",
           "2026 fees: <strong>A1 300 zł · A2 380 zł · B1 520 zł · B2 620 zł · C1 750 zł · C2 800 zł</strong>, 15% less at the reduced rate.",
           "Results about one month after the session; diploma about three months after (Alliances françaises)."],
    stats=[("{n}", "test centres", "FEI list of 26 October 2026"), ("18 Nov", "next B2", "2026"),
           ("6 Nov", "deadline", "at the Alliances françaises"), ("620 zł", "DELF B2", "527 zł at the reduced rate")],
    sections=[
        ("exam-dates", "The 2026 sessions", table(
            "Written-paper dates of the DELF-DALF tout public published by the Alliances françaises in Poland; the Institut français in Warsaw shows the same for November. Checked on 26 October 2026.",
            ["Session", "A1 · A2", "B1", "B2", "C1", "C2", "Registration (Alliances)"],
            [("February 2026", "2 Feb", "3 Feb", "4 Feb", "5 Feb", "6 Feb", "1 Dec 2025 – 23 Jan 2026"),
             ("June 2026", "22 Jun", "23 Jun", "24 Jun", "25 Jun", "26 Jun", "1 Apr – 12 Jun"),
             ("<strong>November 2026</strong>", "16 Nov", "17 Nov", "<strong>18 Nov</strong>", "19 Nov", "20 Nov", "1 Sep – <strong>6 Nov</strong>")]) + """
<p>At the Institut français in Warsaw, November registration ran from 21 September to 18 October 2026. Neither the Institut
nor the Alliances had published a 2027 calendar on 26 October 2026; the Institut in Kraków announced a 2027 fee list without
making it readable. The Alliances françaises in Poland advise checking that your chosen centre runs the session before you
register.</p>"""),
        ("fees", "How much does the DELF cost in Poland?", table(
            "2026 fees, identical at the Institut français in Warsaw and the Alliances françaises in Poland, checked on 26 October 2026.",
            ["Level", "Fee", "Reduced fee"],
            [("DELF A1", "300 zł", "255 zł"), ("DELF A2", "380 zł", "323 zł"), ("DELF B1", "520 zł", "442 zł"),
             ("<strong>DELF B2</strong>", "<strong>620 zł</strong>", "<strong>527 zł</strong>"), ("DALF C1", "750 zł", "637.50 zł"),
             ("DALF C2", "800 zł", "680 zł"), ("DELF junior A1 to B2", "280 to 580 zł", "238 to 493 zł"),
             ("DELF Prim A1.1 to A2", "260 to 350 zł", "221 to 297.50 zł")], wide=False) + """
<p>At the Institut français in Warsaw, the reduced fee is for its students (enrolled in the term or semester before the
session) and for candidates entered by their school or institution, five or more; at the Alliances, ask the office for the
conditions.</p>"""),
        ("registration", "Registration", """<p>At the Institut français, you register online on the session page, in Warsaw or
Kraków; at the Alliances françaises — Gdańsk, Katowice, Lublin, Łódź, Rzeszów, Toruń, Wrocław —, with your chosen
Alliance’s form. A certificate of achievement must be requested in writing when you register. The diplomas are
independent: you register directly for the level you want, and you need 50 points out of 100 to pass.</p>"""),
    ],
    list_title="The {n} DELF-DALF test centres, city by city",
    faq=[("What are the DELF exam dates 2027 in Poland?", "Not yet published: on 26 October 2026, neither the Institut français nor the Alliances françaises had released their 2027 calendar. In 2026, the tout public sessions were in February, June and November."),
         ("When is the next DELF exam in Poland?", "From 16 to 20 November 2026: A1 and A2 on the 16th, B1 on the 17th, B2 on the 18th, DALF C1 on the 19th and C2 on 20 November. The Alliances françaises take registrations until 6 November; at the Institut français in Warsaw, registration closed on 18 October."),
         ("How much does the DELF B2 cost in Poland?", "620 zł, or 527 zł at the reduced rate, at the Institut français and at the Alliances françaises alike (2026 fees). The DALF C1 costs 750 zł and C2 800 zł."),
         ("Where can I take the DELF in Warsaw?", "At the Institut français de Pologne, which runs the November session (online registration, closed on 18 October 2026), or at the Lycée français de Varsovie, also on FEI’s list.")],
    also=[("/en/tcf-canada-poland/", "TCF Canada in Poland", "Warsaw and Kraków."),
          ("/en/delf-romania/", "DELF exam dates 2027 in Romania", "14 and 15 November 2026."), _DATES, _DELF],
    sources="the autumn DELF-DALF tout public session page and the 2026 DELF-DALF fee list of the Institut français de Pologne (Warsaw); the DELF-DALF certificates page and 2026 fees (PDF) of the Alliances françaises in Poland (afpolska.pl); all checked on 26 October 2026.",
    notes={"katowice-alliance": "Website listed by FEI unreachable on 26 October 2026: the Alliance’s page on afpolska.pl.",
           "wrocaw-alliance-francaise-stowarzyszenie-wroclaw": "Page listed by FEI not found on 26 October 2026: the Alliance’s page on afpolska.pl.",
           "varsovie-institut-francais-de-pologne": "The Institut receives visitors at Plac Europejski 3; FEI gives the Widok Street address."},
))

# ===========================================================================
# BELGIUM — DELF-DALF
# ===========================================================================
PAGES.append(en("delf-belgique",
    slug="delf-belgium", country_name="Belgium", crumb="DELF in Belgium",
    title="DELF exam dates 2027 Belgium: sessions, fees",
    desc="DELF and DALF in Belgium: 2027 dates not yet set; the 17–26 November 2026 session (B2 on the 19th), Ghent registration to 3 November, fees.",
    h1="DELF exam dates 2027 in Belgium: sessions, fees and the {n} centres",
    intro="""The <strong>DELF exam dates 2027 in Belgium</strong> were not yet set on 26 October 2026: the Alliance française
in Ghent announces a March session (registration from 1 December 2026 to 3 March 2027) and a June session. Before that,
the DELF and DALF run from <strong>17 to 26 November 2026</strong> in Brussels and Ghent, with the DELF B2 on
<strong>19 November</strong>; Ghent takes registrations until <strong>3 November</strong>, while Brussels closed on
24 October. The B2 costs <strong>€191</strong> in Ghent; Belgium has <strong>{n} centres</strong>.""",
    facts=["<strong>{n} test centres</strong> (FEI list of 26 October 2026): the Alliances françaises of Bruxelles-Europe, Antwerp and Flandre orientale (Ghent), KU Leuven Kulak in Kortrijk, the Institut supérieur des langues vivantes of the University of Liège and the European School in Mol.",
           "November 2026: A1 and A2 on the 17th, B1 on the 18th, <strong>B2 on the 19th</strong>, C1 on the 24th, C2 on 26 November; speaking tests from 16 to 20 and 23 to 27 November in Brussels.",
           "Registration: until <strong>3 November 2026</strong> in Ghent; closed on 24 October in Brussels; results at the end of December in Ghent.",
           "2027 in Ghent: March (registration from 1 December 2026 to 3 March 2027) and June (30 March to 24 May 2027); Brussels had not scheduled any 2027 session yet.",
           "Fees in Ghent: <strong>A1 €117 · A2 €127 · B1 €149 · B2 €191 · C1 €238 · C2 €254</strong>; Brussels does not show its fees, 10% off for its students.",
           "In 2026, Brussels held four sessions: March, June, September and November; diploma available 3 months after the exam."],
    stats=[("{n}", "test centres", "FEI list of 26 October 2026"), ("19 Nov", "next B2", "Brussels and Ghent"),
           ("3 Nov", "deadline in Ghent", "Brussels: 24 Oct"), ("€191", "DELF B2 in Ghent", "€172.40 for its students")],
    sections=[
        ("exam-dates", "The 2026 and 2027 sessions", table(
            "DELF-DALF tout public sessions of the Alliance française de Bruxelles-Europe (2026) and the Alliance française de Flandre orientale (2027), checked on 26 October 2026.",
            ["Session", "A1 · A2", "B1", "B2", "C1", "C2", "Registration"],
            [("March 2026", "17 Mar", "18 Mar", "19 Mar", "24 Mar", "26 Mar", "1 Dec 2025 – 20 Feb 2026"),
             ("June 2026", "9 Jun", "10 Jun", "11 Jun", "16 Jun", "18 Jun", "22 Feb – 16 May"),
             ("September 2026", "15 Sep", "16 Sep", "17 Sep", "22 Sep", "24 Sep", "17 May – 22 Aug"),
             ("<strong>November 2026</strong>", "17 Nov", "18 Nov", "<strong>19 Nov</strong>", "24 Nov", "26 Nov", "Brussels 23 Aug – 24 Oct; Ghent 13 Jul – <strong>3 Nov</strong>"),
             ("March 2027 (Ghent)", "not set", "not set", "not set", "not set", "not set", "1 Dec 2026 – 3 Mar 2027"),
             ("June 2027 (Ghent)", "not set", "not set", "not set", "not set", "not set", "30 Mar – 24 May 2027")]) + """
<p>Speaking tests are held in the week of the written papers: in Brussels, 16 to 20 November for A1 to B2, 23 to
27 November for the DALF. Ghent’s page shows 29 November for B2 in its calendar and the 19th in the level details;
Brussels, the managing centre, gives the 19th. Antwerp, Kortrijk, Liège and Mol were not checked: their contact details are
in the list.</p>"""),
        ("fees", "How much does the DELF cost in Belgium?", table(
            "November 2026 fees at the Alliance française de Flandre orientale (Ghent), checked on 26 October 2026.",
            ["Level", "Fee", "Students of an Alliance course"],
            [("DELF A1", "€117.00", "—"), ("DELF A2", "€127.00", "—"), ("DELF B1", "€149.00", "€134.60"),
             ("<strong>DELF B2</strong>", "<strong>€191.00</strong>", "<strong>€172.40</strong>"), ("DALF C1", "€238.00", "€215.60"),
             ("DALF C2", "€254.00", "€230.00")], wide=False) + """
<p>In Ghent, you pay online when registering; no refund, level change or postponement after the deadline. The Alliance de
Bruxelles-Europe did not show its fees on 26 October 2026; its students get 10% off, and the diploma is available at its
reception three months after the exam.</p>"""),
        ("registration", "Registration", """<p>You register online on your chosen Alliance’s website, level by level; the
registration is in your name and cannot be transferred. In Ghent, test-day notices go out by email between 3 and
13 November 2026; if you have heard nothing a week before the exam, contact the centre. The diplomas are independent: you
register directly for the level you want, and you need 50 points out of 100 to pass.</p>"""),
    ],
    list_title="The {n} DELF-DALF test centres in Belgium",
    faq=[("What are the DELF exam dates 2027 in Belgium?", "They were not set on 26 October 2026. The Alliance française de Flandre orientale announces a session in March 2027 (registration from 1 December 2026 to 3 March 2027) and one in June (30 March to 24 May 2027); Bruxelles-Europe had not scheduled anything yet."),
         ("When is the next DELF exam in Belgium?", "From 17 to 26 November 2026 in Brussels and Ghent: A1 and A2 on the 17th, B1 on the 18th, B2 on the 19th, DALF C1 on the 24th and C2 on 26 November. Ghent takes registrations until 3 November; in Brussels, registration closed on 24 October."),
         ("How much does the DELF B2 cost in Belgium?", "€191 at the Alliance française in Ghent, €172.40 for its students. The Alliance de Bruxelles-Europe did not show its fees on 26 October 2026; its students get 10% off."),
         ("Where can I take the DELF in Brussels?", "At the Alliance française de Bruxelles-Europe, avenue des Arts 46, which also manages the DELF-DALF for the whole of Belgium. In 2026, it held four sessions: March, June, September and November."),
         ("When do I get my DELF diploma?", "In Ghent, the November 2026 results arrive at the end of December; in Brussels, the diploma is available at reception three months after the exam, and a certificate is given when results are announced.")],
    also=[("/en/tcf-canada-belgium/", "TCF Canada in Belgium", "Brussels €268, Ghent €260."),
          ("/en/delf-netherlands/", "DELF exam dates 2027 in the Netherlands", "March and June 2027 in Amsterdam, B2 €175."), _DATES, _DELF],
    sources="the DELF-DALF tout public pages of the Alliance française de Bruxelles-Europe (Calendar and Register tabs) and the DELF-DALF page of the Alliance française de Flandre orientale (Ghent), checked on 26 October 2026.",
))

# ===========================================================================
# PORTUGAL — DELF-DALF
# ===========================================================================
PAGES.append(en("delf-portugal",
    slug="delf-portugal", country_name="Portugal", crumb="DELF in Portugal",
    title="DELF exam dates 2027 Portugal: calendar, fees",
    desc="DELF and DALF in Portugal: 2027 calendar not yet published; the 19–20 November 2026 session (registration until 6 November), fees (B2 €140).",
    h1="DELF exam dates 2027 in Portugal: the national calendar, fees and the {n} centres",
    intro="""The <strong>DELF exam dates 2027 in Portugal</strong> (<span lang="pt">datas exames DELF 2027</span>) were not yet
published on 26 October 2026. Portugal follows a <strong>national calendar</strong> from the Institut français du Portugal:
five sessions in 2026, the last on <strong>19 and 20 November</strong> (A1, B1 and C1 on the 19th; A2, B2 and C2 on the
20th), with registration until <strong>6 November</strong> at seven Alliances françaises. The DELF B2 costs
<strong>€140</strong>, or €126 at the reduced rate.""",
    facts=["<strong>{n} test centres</strong> (FEI list of 26 October 2026), managed by the language and education cooperation service (Lisbon): nine Alliances françaises, the universities of Aveiro, Porto and the Azores, two French lycées, an international school and the Academia de Línguas da Madeira.",
           "November 2026: A1, B1 and C1 on the 19th; A2, <strong>B2</strong> and C2 on <strong>20 November</strong>; speaking tests from 16 to 27 November; registration until <strong>6 November</strong>; results on 15 December.",
           "Where, in November: the Alliances françaises in Porto, Guimarães, Coimbra, Faro, Viseu, Setúbal and Leiria.",
           "In 2026: February, April, June, September and November; 2027 not published.",
           "Fees: <strong>A1 €65 · A2 €75 · B1 €110 · B2 €140 · C1 €177 · C2 €190</strong>; reduced, €59 to €171.",
           "The DELF Prim, DELF junior and DELF escolar have their own calendar."],
    stats=[("{n}", "test centres", "FEI list of 26 October 2026"), ("20 Nov", "next B2", "2026"),
           ("6 Nov", "registration deadline", "seven Alliances"), ("€140", "DELF B2", "€126 at the reduced rate")],
    sections=[
        ("exam-dates", "The 2026 national calendar", table(
            "2026 DELF-DALF calendar of the Institut français du Portugal (PDF), checked on 26 October 2026. The 2027 calendar was not published yet.",
            ["Session", "A1 · B1 · C1", "A2 · B2 · C2", "Speaking", "Registration", "Results"],
            [("February", "12 Feb", "13 Feb", "9 Feb – 20 Feb", "2 Dec 2025 – 30 Jan", "16 Mar"),
             ("April", "9 Apr", "10 Apr", "1 Apr – 17 Apr", "1 Jan – 27 Mar", "11 May"),
             ("June", "25 Jun", "26 Jun", "22 Jun – 3 Jul", "1 Jan – 15 Jun", "21 Jul"),
             ("September", "24 Sep", "25 Sep", "21 Sep – 2 Oct", "1 Jan – 11 Sep", "20 Oct"),
             ("<strong>November</strong>", "19 Nov", "<strong>20 Nov</strong>", "16 Nov – 27 Nov", "1 Jan – <strong>6 Nov</strong>", "15 Dec")]) + """
<p>Not every town opens every session: in February and September, the Alliances in Lisbon, Porto, Guimarães, Coimbra, Faro,
Viseu, Setúbal and Leiria and the universities of Porto and Aveiro; in June, the same plus the Academia de Línguas da
Madeira; in November, only the Alliances in Porto, Guimarães, Coimbra, Faro, Viseu, Setúbal and Leiria.</p>"""),
        ("fees", "How much does the DELF cost in Portugal?", table(
            "2026 fees of the Institut français du Portugal, checked on 26 October 2026.",
            ["Level", "Fee", "Reduced fee"],
            [("DELF A1", "€65", "€59"), ("DELF A2", "€75", "€68"), ("DELF B1", "€110", "€99"),
             ("<strong>DELF B2</strong>", "<strong>€140</strong>", "<strong>€126</strong>"), ("DALF C1", "€177", "€160"),
             ("DALF C2", "€190", "€171")], wide=False) + """
<p>The reduced fee applies to candidates enrolled at the centres named in the calendar and to group registrations of ten
or more candidates per level. The DELF-DALF tout public is for candidates aged 18 and over; younger candidates take the
DELF junior or DELF escolar (primary and secondary pupils) or the DELF Prim.</p>"""),
        ("registration", "Registration", """<p>You register with one of the centres of your chosen session; the Institut
français du Portugal keeps the calendar and publishes, for each diploma, a PDF of dates and fees. After an IT incident, it
extended the deadlines for changing or cancelling a registration by 14 days. The diplomas are independent: you register
directly for the level you want, and you need 50 points out of 100 to pass.</p>"""),
    ],
    list_title="The {n} DELF-DALF test centres, city by city",
    faq=[("What are the DELF exam dates 2027 in Portugal?", "Not yet published: on 26 October 2026, the Institut français du Portugal only showed its 2026 calendar of five sessions (February, April, June, September, November)."),
         ("When is the next DELF exam in Portugal?", "On 19 and 20 November 2026: A1, B1 and DALF C1 on the 19th, A2, B2 and C2 on the 20th, at the Alliances françaises in Porto, Guimarães, Coimbra, Faro, Viseu, Setúbal and Leiria. Registration until 6 November, results on 15 December 2026."),
         ("How much does the DELF B2 cost in Portugal?", "€140, or €126 at the reduced rate (2026 fees of the Institut français du Portugal). The DALF C1 costs €177 and C2 €190."),
         ("Can I take the DELF in Lisbon in November?", "No: in November 2026, the national calendar only holds the exam at the Alliances in Porto, Guimarães, Coimbra, Faro, Viseu, Setúbal and Leiria. The Alliance française in Lisbon hosts the February, June and September sessions.")],
    also=[("/en/tcf-canada-portugal/", "TCF Canada in Portugal", "Porto and Faro €220, Viseu €211."),
          ("/es/fechas-delf-2027/", "Fechas DELF 2027 (España)", "El calendario nacional español, en español."), _DATES, _DELF],
    sources="the 2026 DELF-DALF calendar and fees (PDF) and the official exams page of the Institut français du Portugal (ifp-lisboa.com), checked on 26 October 2026.",
    notes={"lisbonne-lycee-francais-charles-lepierre": "Website listed by FEI out of service on 26 October 2026: the lycée’s current website."},
))

# ===========================================================================
# IRELAND — DELF-DALF
# ===========================================================================
PAGES.append(en("delf-irlande",
    slug="delf-ireland", country_name="Ireland", crumb="DELF in Ireland",
    title="DELF exam dates 2027 Ireland: fees, test centres",
    desc="DELF exam dates 2027 in Ireland: B2 on 18 February, 22 April, 24 June, 23 September and 25 November; registration windows and fees (B2 €145 in Dublin).",
    h1="DELF exam dates 2027 in Ireland: the calendar, fees and the {n} Alliances françaises",
    intro="""<strong>DELF exam dates 2027 in Ireland</strong>: the 2027 calendar published by the Alliance française de Limerick
puts the DELF B2 on <strong>18 February</strong>, 22 April, 24 June, 23 September and 25 November 2027, with the DALF C1
and C2 the next day in Dublin; registration for February runs from <strong>11 November 2026 to 11 January 2027</strong>.
Before that, Dublin holds its session from 24 to 27 November 2026, B2 on the 26th. The DELF and DALF are held at Ireland’s
<strong>{n} Alliances françaises</strong> — Dublin, Cork, Kilkenny, Limerick, Waterford-Wexford —, managed by the Alliance in
Dublin.""",
    facts=["<strong>{n} test centres</strong> (FEI list of 26 October 2026): the Alliances françaises in Dublin, Cork, Kilkenny, Limerick and Waterford-Wexford.",
           "2027 (Limerick): A1 and A2 on Tuesday, B1 on Wednesday, B2 on Thursday, C1 and C2 on Friday — the weeks of 16 February, 20 April, 22 June, 21 September and 23 November.",
           "The DALF C1 and C2 are taken in Dublin, the Alliance in Limerick points out.",
           "November 2026 in Dublin: A1 and A2 on the 24th, B1 on the 25th, <strong>B2 on the 26th</strong>, C1 and C2 on 27 November.",
           "Fees: <strong>B2 €145 in Dublin</strong>, <strong>€170 in Limerick</strong> (2027 fees); DALF C1 €195 and €220.",
           "Results about one month after the exam; diploma 3 to 4 months after (Limerick)."],
    stats=[("{n}", "test centres", "the Alliances françaises"), ("18 Feb", "first 2027 B2", "registration until 11 Jan"),
           ("5", "sessions in 2027", "Feb, Apr, Jun, Sep, Nov"), ("€145", "DELF B2 in Dublin", "€170 in Limerick")],
    sections=[
        ("exam-dates", "The 2027 calendar", table(
            "2027 DELF-DALF calendar of the Alliance française de Limerick (page updated on 19 October 2026), “subject to change”, checked on 26 October 2026. Dates of the collective written papers.",
            ["Session", "A1 · A2", "B1", "B2", "C1 · C2 (in Dublin)", "Registration"],
            [("<strong>February 2027</strong>", "Tue 16 Feb", "Wed 17 Feb", "<strong>Thu 18 Feb</strong>", "Fri 19 Feb", "11 Nov 2026 – 11 Jan 2027"),
             ("April 2027", "Tue 20 Apr", "Wed 21 Apr", "Thu 22 Apr", "Fri 23 Apr", "18 Jan – 18 Mar"),
             ("June 2027", "Tue 22 Jun", "Wed 23 Jun", "Thu 24 Jun", "Fri 25 Jun", "15 Mar – 17 May"),
             ("September 2027", "Tue 21 Sep", "Wed 22 Sep", "Thu 23 Sep", "Fri 24 Sep", "16 May – 16 Aug"),
             ("November 2027", "Tue 23 Nov", "Wed 24 Nov", "Thu 25 Nov", "Fri 26 Nov", "18 Aug – 18 Oct")]) + """
<p>The individual speaking test may be on a different day from the written papers. The Alliance française de Dublin, the
managing centre, showed three sessions for 2026 — February, June and November —, the last from 24 to 27 November 2026; it
had not put its 2027 dates online on 26 October. The DELF junior and DELF scolaire have their own sessions (January, March
and May 2027 in Limerick), the DELF Prim in May and June.</p>"""),
        ("fees", "How much does the DELF cost in Ireland?", table(
            "Fees shown on 26 October 2026 by the Alliance française de Dublin (tout public) and the Alliance française de Limerick (2027 fees).",
            ["Level", "Dublin", "Limerick 2027", "Limerick, reduced"],
            [("DELF A1", "€90", "€115", "€103.50"), ("DELF A2", "€100", "€115", "€103.50"), ("DELF B1", "€125", "€150", "€135"),
             ("<strong>DELF B2</strong>", "<strong>€145</strong>", "<strong>€170</strong>", "€153"), ("DALF C1", "€195", "€220", "€198"),
             ("DALF C2", "€205", "€230", "€207")]) + """
<p>In Limerick, the reduced fee (10% off) is for the Alliance’s students and for learners from partner organisations —
schools, higher-education institutions, public administrations. The DELF junior there costs €95 to €145, the DELF scolaire
€50 to €75, the DELF Prim €45 to €65.</p>"""),
        ("registration", "Registration", """<p>In Limerick, you download the form for your exam, email it to the Alliance, then
pay; for under-18s, a parent signs it. In Dublin, the test-day notice arrives one week before the exam. The diplomas are
independent: you register directly for the level you want, and you need 50 points out of 100 to pass.</p>"""),
    ],
    list_title="The {n} DELF-DALF test centres in Ireland",
    faq=[("What are the DELF exam dates 2027 in Ireland?", "According to the 2027 calendar of the Alliance française de Limerick, the DELF B2 is on 18 February, 22 April, 24 June, 23 September and 25 November 2027, with the DALF C1 and C2 the next day, in Dublin. For February, registration runs from 11 November 2026 to 11 January 2027."),
         ("When is the next DELF exam in Dublin?", "From 24 to 27 November 2026: A1 and A2 on the 24th, B1 on the 25th, B2 on the 26th, DALF C1 and C2 on 27 November, according to the Alliance française de Dublin’s page."),
         ("How much does the DELF B2 cost in Ireland?", "€145 at the Alliance française de Dublin, according to the fees shown on 26 October 2026; €170 in Limerick in 2027, €153 at the reduced rate."),
         ("Where can I take the DALF C1 in Ireland?", "In Dublin: the Alliance française de Limerick points out that all DALF C1 and C2 papers are held there. The C1 costs €195 in Dublin.")],
    also=[("/en/tcf-canada-ireland/", "TCF Canada in Ireland", "Dublin and Galway, €270."),
          ("/en/delf-uk/", "DELF in the UK", "Test centres and sessions across the UK."), _DATES, _DELF],
    sources="the DELF & DALF page of the Alliance française de Dublin and the DELF Exams page of the Alliance française de Limerick (2027 calendar and fees), checked on 26 October 2026.",
    notes={"limerick-alliance-francaise-de-limerick": "Website not given by FEI: the Alliance’s own, checked on 26 October 2026."},
))

# ===========================================================================
# SWEDEN — DELF-DALF (no TCF centre: TEF Canada and nearby centres)
# ===========================================================================
PAGES.append(en("delf-suede",
    slug="delf-sweden", country_name="Sweden", crumb="DELF in Sweden",
    title="DELF exam dates 2027 Sweden: fees in SEK, centres",
    desc="DELF and DALF in Sweden: 2027 dates not yet published; three sessions a year in Stockholm, Uppsala, Borås, Växjö; B2 SEK 1,450; TEF Canada, no TCF.",
    h1="DELF exam dates 2027 in Sweden: sessions, fees and the {n} centres",
    intro="""The <strong>DELF exam dates 2027 in Sweden</strong> were not yet published on 26 October 2026. The
<strong>Institut français de Suède</strong> runs the DELF and DALF tout public three times a year in Stockholm, Uppsala,
Borås and Växjö (Gothenburg in spring): in 2026, 11–13 March, 6–8 May and <strong>3–5 November</strong>, with
registration closed on 9 October. The DELF B2 costs <strong>SEK 1,450</strong>. Sweden has <strong>no TCF centre</strong>:
for Canada, the Institut runs the TEF Canada (SEK 2,900).""",
    facts=["<strong>{n} test centres</strong> (FEI list of 26 October 2026), mostly schools; for the tout public, the Institut français de Suède lists Stockholm, Uppsala, Borås, Växjö and Gothenburg.",
           "2026: 11–13 March (registration 30 January to 13 February), 6–8 May (27 March – 10 April), 3–5 November (25 September – 9 October).",
           "Fees since 1 January 2026: <strong>A1 SEK 800 · A2 SEK 900 · B1 SEK 950 · B2 SEK 1,450 · C1 SEK 2,500 · C2 SEK 2,800</strong>.",
           "Stockholm (Institut français) and Uppsala (university): A1 to C2; Borås and Växjö: A1 to B2; Gothenburg (Hvitfeldtska): B1, B2 and C1 in spring.",
           "<strong>No TCF centre in Sweden</strong>: TEF Canada at the Institut français de Suède, SEK 2,900, next session on 25 November 2026 (registration 28 October to 11 November).",
           "Nearest TCF Canada: Fransk kulturhus in Oslo (NOK 3,150); Institut français du Danemark in Copenhagen."],
    stats=[("{n}", "test centres", "FEI list of 26 October 2026"), ("3", "sessions a year", "March, May, November"),
           ("SEK 1,450", "DELF B2", "C1 SEK 2,500"), ("0", "TCF centres", "TEF Canada in Stockholm")],
    sections=[
        ("exam-dates", "The 2026 sessions", table(
            "DELF-DALF tout public sessions of the Institut français de Suède, checked on 26 October 2026. Registration while places last.",
            ["Session", "Papers", "Registration", "Where"],
            [("Winter 2026", "11, 12 and 13 March", "30 Jan – 13 Feb", "Stockholm, Uppsala, Borås, Växjö"),
             ("Spring 2026", "6, 7 and 8 May", "27 Mar – 10 Apr", "Stockholm, Uppsala, Borås, Växjö, Gothenburg"),
             ("<strong>Autumn 2026</strong>", "<strong>3, 4 and 5 November</strong>", "25 Sep – 9 Oct", "Stockholm, Uppsala, Borås, Växjö")]) + """
<p>The 2027 dates were not published yet on 26 October 2026; in 2026, each registration window lasted two weeks and closed
a little less than a month before the papers. The DELF-DALF tout public is for those aged 18 and over; younger candidates
take the DELF Prim or DELF junior, presented on a separate page of the Institut.</p>"""),
        ("fees", "How much does the DELF cost in Sweden?", table(
            "Fees of the Institut français de Suède, in force since 1 January 2026, checked on 26 October 2026.",
            ["Level", "Fee"],
            [("DELF A1", "SEK 800"), ("DELF A2", "SEK 900"), ("DELF B1", "SEK 950"), ("<strong>DELF B2</strong>", "<strong>SEK 1,450</strong>"),
             ("DALF C1", "SEK 2,500"), ("DALF C2", "SEK 2,800")], wide=False) + """
<p>Once the test-day notice has been sent, your place is booked and the fee is no longer refunded, except for exceptional
reasons.</p>"""),
        ("tcf", "No TCF in Sweden: the TEF Canada and nearby centres", """<p>No TCF centre is approved in Sweden (FEI list of
26 October 2026). For a Canadian application, the Institut français de Suède runs the other test IRCC accepts, the
<strong>TEF Canada</strong>: SEK 2,900, plus SEK 100 registration; next session on <strong>25 November 2026</strong>,
registration from 28 October to 11 November 2026; five sessions in 2026 (January, April, June, September, November). The TEF
for French citizenship costs SEK 2,000 there.</p>

<p>The nearest TCF Canada is in Oslo, at Fransk kulturhus (NOK 3,150, several sessions a year, register at least 5 weeks
ahead), or at the Institut français du Danemark in Copenhagen, whose 30 October 2026 TCF Canada session closed registration
on 18 September; the TCF tout public and TCF IRN are held there on 15 and 16 March 2027.</p>"""),
    ],
    list_title="The {n} DELF-DALF test centres, city by city",
    faq=[("What are the DELF exam dates 2027 in Sweden?", "Not yet published on 26 October 2026. In 2026, the Institut français de Suède held three sessions — 11–13 March, 6–8 May and 3–5 November —, each with a two-week registration window closing a little less than a month before."),
         ("How much does the DELF B2 cost in Sweden?", "SEK 1,450 at the Institut français de Suède (fees in force since 1 January 2026); SEK 950 for B1, SEK 2,500 for the DALF C1."),
         ("Can I take the TCF Canada in Sweden?", "No: no TCF centre is approved in Sweden. The Institut français de Suède runs the TEF Canada (SEK 2,900, session on 25 November 2026); the nearest TCF Canada is in Oslo (Fransk kulturhus, NOK 3,150) or Copenhagen."),
         ("Where can I take the DELF outside Stockholm?", "At Uppsala University (A1 to C2), in Borås (Bodaskolan) and Växjö (Linnaeus University), A1 to B2, and in Gothenburg (Hvitfeldtska gymnasiet) for B1, B2 and C1 in spring.")],
    also=[("/en/#europe", "TCF Canada and DELF in Europe", "Country by country: who offers the TCF Canada, and fees."),
          ("/en/delf-germany/", "DELF exam dates 2027 in Germany", "Sessions from November 2026, B2 at €201."), _TEF, _DELF],
    sources="the DELF and DALF exams page and TEF exam page of the Institut français de Suède (ifsuede.com); the TCF pages of Fransk kulturhus (Oslo) and the Institut français du Danemark; all checked on 26 October 2026.",
    notes={"hallsberg-alleskolan": _NO_LINK},
))

# ===========================================================================
# AUSTRIA — TCF (+ DELF-DALF)
# ===========================================================================
PAGES.append(en("tcf-autriche",
    slug="tcf-canada-austria", country_name="Austria", crumb="TCF Canada in Austria",
    title="TCF Canada in Austria: Vienna €295, DELF 2027 dates",
    desc="TCF Canada in Austria: €295 at the Institut français in Vienna, TCF IRN €225, session on 4 December 2026; DELF-DALF on 27, 28 and 29 January 2027.",
    h1="TCF Canada and DELF in Austria: the Institut français in Vienna, fees and dates",
    intro="""In Austria, one centre is approved for the TCF: the <strong>Institut français d’Autriche</strong> in Vienna. It shows
the <strong>TCF Canada at €295</strong>, the TCF IRN at €225 and the TCF tout public from €135 to €295; its only published
TCF session is on <strong>4 December 2026</strong>, with registration closing on <strong>4 November</strong>. For the DELF
and DALF, the Institut’s next session falls on <strong>27, 28 and 29 January 2027</strong>; the Institut culturel
franco-autrichien in Graz holds its own in May 2027.""",
    facts=["<strong>1 approved TCF centre</strong> (FEI list of 26 October 2026): the Institut français d’Autriche, Praterstraße 38, Vienna.",
           "TCF Canada <strong>€295</strong> · TCF IRN €225 · TCF tout public €135 (compulsory tests), €235 with writing or speaking, €295 in full · TCF Québec on request.",
           "TCF session: <strong>4 Dec 2026</strong>, registration until 4 Nov; photo ID compulsory, photo taken on the test day.",
           "No re-marking requests for sessions after 1 August 2026.",
           "DELF-DALF in Vienna, January 2027: A2 and B1 on the 27th, C1 and C2 on the 28th, <strong>A1 and B2 on 29 January</strong>; fees €130 to €220, €104 at the student rate; papers also in Salzburg and Innsbruck.",
           "Graz: DELF-DALF tout public in May 2027; DELF scolaire on 9 and 10 March 2027 (deadline 29 January)."],
    stats=[("1", "approved TCF centre", "Vienna"), ("€295", "TCF Canada", "TCF IRN €225"),
           ("4 Dec", "TCF session", "deadline 4 Nov"), ("27–29 Jan", "DELF-DALF 2027", "Vienna")],
    sections=[
        ("releve", "The TCF at the Institut français in Vienna", releve([
            ("Institut français d’Autriche (Vienna)", "<strong>Canada</strong>, IRN, tout public (and DAP); Québec on request",
             "Canada <strong>€295</strong> · IRN €225 · tout public €135, €235 or €295",
             "4 Dec 2026 (deadline 4 Nov); 2027 not published. Online registration on the Institut’s exam portal; photo ID compulsory."),
        ]) + """
<p>According to the Institut, the “compulsory tests + writing” option is the official test for the DAP procedure (prior
admission request to a French university). No re-marking requests are accepted for sessions after 1 August 2026. The TEF
Canada, the other test IRCC accepts, has no centre in Austria on the map of Le français des affaires read on 26 October
2026.</p>"""),
        ("delf", "The DELF and DALF in Austria", """<p>Two centres run the DELF and DALF tout public (FEI list of 26 October
2026): the <strong>Institut français d’Autriche</strong> in Vienna, the country’s managing body, which also holds papers in
Salzburg and Innsbruck, and the <strong>Institut culturel franco-autrichien in Graz</strong>, which handles its own
registrations. You can sit the exams from the age of 16.</p>
""" + table("January 2027 DELF-DALF session of the Institut français d’Autriche, checked on 26 October 2026.",
            ["Date", "Written papers"],
            [("Wednesday 27 Jan 2027", "DELF A2 and B1"), ("Thursday 28 Jan 2027", "DALF C1 and C2"),
             ("<strong>Friday 29 Jan 2027</strong>", "<strong>DELF A1 and B2</strong>")], wide=False) + """
<p>Speaking-test dates are sent after registration closes, at least one week before the written papers. Fees range from
€130 to €220 depending on the level, €104 at the student rate; a registration only counts once the fee has arrived, and is
only refunded with a medical certificate. In Graz, the DELF-DALF tout public is in May 2027 (deadline not yet set) and the
DELF scolaire on 9 and 10 March 2027, with registration and payment by 29 January 2027.</p>"""),
    ],
    list_title="The approved TCF test centre in Austria",
    faq=[("Where can I take the TCF Canada in Austria?", "At the Institut français d’Autriche in Vienna (Praterstraße 38): it is the country’s only approved TCF centre, and it shows the TCF Canada at €295."),
         ("When is the next TCF in Vienna?", "On 4 December 2026, with registration closing on 4 November; it was the only TCF session published on 26 October 2026. The TCF Québec is held on a date set on request."),
         ("How much does the TCF IRN cost in Austria?", "€225 at the Institut français in Vienna; the TCF tout public costs €135 for the compulsory tests and €295 with both expression tests."),
         ("What are the DELF exam dates 2027 in Austria?", "At the Institut français in Vienna: DELF A2 and B1 on 27 January, DALF C1 and C2 on 28 January, DELF A1 and B2 on 29 January 2027. In Graz, the tout public session is in May 2027."),
         ("How much does the DELF cost in Austria?", "€130 to €220 at the Institut français in Vienna depending on the level, €104 at the student rate; Graz sets its own fees.")],
    also=[("/en/tcf-canada-germany/", "TCF Canada in Germany", "Munich, €295, sessions every month."),
          ("/en/tcf-canada-switzerland/", "TCF Canada in Switzerland", "Montreux and Zurich."), _CLB, _PRACTICE],
    sources="the TCF and DELF-DALF pages of the Institut français d’Autriche (institutfrancais.at) and the DELF-DALF page of the Institut culturel franco-autrichien in Graz (franceautriche.at), checked on 26 October 2026; the TEF centre map of Le français des affaires, read the same day.",
    notes={"vienne-institut-francais": "The link published by FEI no longer works: the Institut’s TCF page, checked on 26 October 2026."},
))

# ===========================================================================
# LUXEMBOURG — TCF (+ DELF-DALF)
# ===========================================================================
PAGES.append(en("tcf-luxembourg",
    slug="tcf-canada-luxembourg", country_name="Luxembourg", crumb="TCF in Luxembourg",
    title="TCF in Luxembourg: no TCF Canada, TCF IRN €150, DELF",
    desc="TCF Canada in Luxembourg: not offered. The Institut national des langues runs the TCF tout public (€120) and TCF IRN (€150); DELF B2 at €186.",
    h1="TCF and DELF in Luxembourg: the Institut national des langues, fees and sessions",
    intro="""<strong>TCF Canada in Luxembourg: not offered.</strong> The country’s two approved TCF centres are the sites of the
<strong>Institut national des langues Luxembourg</strong> (INLL), in Luxembourg City and Esch-sur-Alzette (Belval), and its
calendar only lists the <strong>TCF tout public</strong> (€120 for the compulsory tests) and the <strong>TCF IRN</strong>
(€150), on paper. The 2026 sessions are closed; for Canada, the nearest centres are in Brussels (€268), Aachen and Mainz
(€295). The INLL also runs the DELF A2 to B2 and the DALF C1.""",
    facts=["<strong>{n} approved TCF centres</strong> (FEI list of 26 October 2026): the INLL on boulevard de la Foire in Luxembourg City and its Belval site in Esch-sur-Alzette.",
           "Paper-based TCF tout public: <strong>€120</strong> for the compulsory tests, +€55 for writing, +€55 for speaking; TCF IRN: <strong>€150</strong>.",
           "2026 sessions: TCF IRN on 19 Oct (deadline 14 Sep), TCF tout public on 23 Nov (deadline 12 Oct); 2027 not published.",
           "<strong>No TCF Canada</strong>: the INLL’s 2026 TCF registration form only offers tout public and IRN.",
           "The exam only goes ahead with at least 5 candidates per level; otherwise the fee is refunded.",
           "DELF-DALF at the INLL: B1 €145, B2 €186, C1 €232 (session from 9 to 11 November 2026, B2 full); A2 €124 in February 2027."],
    stats=[("{n}", "approved centres", "the INLL’s two sites"), ("0", "TCF Canada", "tout public and IRN only"),
           ("€150", "TCF IRN", "on paper"), ("€186", "DELF B2", "November session full")],
    sections=[
        ("releve", "The TCF at the Institut national des langues", releve([
            ("Institut national des langues Luxembourg (Luxembourg City and Belval)", "tout public and IRN, on paper — <strong>no TCF Canada</strong>",
             "tout public €120 (+€55 per expression test) · IRN €150",
             "IRN 19 Oct 2026 (deadline 14 Sep); tout public 23 Nov 2026 (deadline 12 Oct); 2027 not published. Send the file by email or post: form, ID, proof of payment."),
        ]) + """
<p>The 2026 tests are held at the Glacis site, boulevard de la Foire. Registration may close before the deadline shown;
the test-day notice arrives at least two weeks before the first test. In case of force majeure, the INLL can move the
registration to a later session, within 12 months, with proof sent within five days. For the TCF IRN, the form asks for
the purpose: citizenship, resident card or multi-year residence permit in France.</p>"""),
        ("canada", "Where to take the TCF Canada near Luxembourg?", """<p>On 26 October 2026, the INLL did not offer the Canada
version. The nearest centres that advertise it: the Alliance française de Bruxelles-Europe (<strong>€268</strong>, session
on 9 December 2026), the Institut culturel franco-allemand in Aachen and the Institut français in Mainz
(<strong>€295</strong>), in Germany. The TEF Canada, the other test IRCC accepts, has one centre in Luxembourg on the map of
Le français des affaires — inlingua Luxembourg —, with no session published on 26 October 2026.</p>"""),
        ("delf", "The DELF and DALF in Luxembourg", """<p>Two centres run the DELF-DALF (FEI list of 26 October 2026): the
INLL, the country’s managing body, and the Lycée Michel-Lucius in Luxembourg City. The INLL offers the DELF A2, B1 and B2 and
the DALF C1:</p>
""" + table("2026 exam calendar of the INLL (version of 10 September 2026), checked on 26 October 2026.",
            ["Level", "Fee", "Papers", "Deadline"],
            [("DELF A2", "€124", "February 2027", "—"), ("DELF B1", "€145", "9–11 Nov 2026", "18 Sep 2026"),
             ("<strong>DELF B2</strong>", "<strong>€186</strong>", "9–11 Nov 2026", "no places left"),
             ("DALF C1", "€232", "9–11 Nov 2026", "18 Sep 2026")], wide=False) + """
<p>The November 2026 session is closed; the 2027 dates for B1, B2 and C1 were not published on 26 October 2026.</p>"""),
    ],
    list_title="The {n} approved TCF test centres in Luxembourg",
    faq=[("Can I take the TCF Canada in Luxembourg?", "No, not on 26 October 2026: the Institut national des langues, the country’s only TCF provider, only offers the TCF tout public and the TCF IRN. The nearest centres that advertise the TCF Canada are Brussels (€268), Aachen and Mainz (€295)."),
         ("How much does the TCF IRN cost in Luxembourg?", "€150 at the INLL, on paper. The 2026 session was on 19 October (deadline 14 September); the 2027 ones were not published."),
         ("How much does the TCF tout public cost in Luxembourg?", "€120 for the compulsory tests at the INLL, plus €55 for writing and €55 for speaking. Session on 23 November 2026, registration closed on 12 October."),
         ("Where can I take the DELF B2 in Luxembourg?", "At the Institut national des langues, €186; the 9 to 11 November 2026 session had no places left on 26 October. The Lycée Michel-Lucius is also a DELF-DALF centre.")],
    also=[("/en/tcf-canada-belgium/", "TCF Canada in Belgium", "Brussels €268, Ghent €260."),
          ("/en/tcf-canada-germany/", "TCF Canada in Germany", "Aachen and Mainz, €295."), _CLB, _TEF],
    sources="the 2026 TCF registration form (PDF), the 2026 exam and test calendar (version of 10 September 2026) and the certifications page of the Institut national des langues Luxembourg (inll.lu), checked on 26 October 2026; the TEF centre map of Le français des affaires, read the same day.",
    notes={"luxembourg-institut-national-des-langues": "FEI lists computer-based sessions; the INLL’s 2026 calendar announces a paper-based TCF."},
))
