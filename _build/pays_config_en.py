# -*- coding: utf-8 -*-
"""Pages pays en anglais (/en/, make_pays.py) — traductions des pages /centres/ du 08/10/2026.

Même règle que pays_config.py : aucun fait nouveau. Les pages États-Unis et Royaume-Uni traduisent le
relevé du 8 octobre 2026 (anglais américain pour les États-Unis, britannique pour le Royaume-Uni) ; les
pages Canada traduisent /centres/tcf-canada/ et les cinq pages ville (liste FEI du 19/09/2026, relevé du
17/09), en anglais canadien. Glossaire : i18n_glossary.md.
"""
from pays_i18n import NR as _NR, canada, from_fr, releve, table

NR = _NR["en"]

PAGES = []

# ===========================================================================
# UNITED STATES
# ===========================================================================
PAGES.append(from_fr(
    "tcf-etats-unis", "en", "en-US", "États-Unis",
    slug="tcf-canada-usa", country_name="United States",
    crumb="TCF Canada in the USA",
    title="TCF Canada in the USA: 12 test centers, prices, dates",
    desc="Where to take the TCF Canada in the US: 12 of the 18 approved centers offer it, for $330 to $505. Houston, Los Angeles, Boston… Open dates, registration.",
    modified="2026-10-26", date_label="October 26, 2026", list_date="October 8, 2026", releve_date="October 8 and 18, 2026",
    h1="TCF Canada in the USA: the test centers that offer it, prices and open seats",
    intro="""In the United States, {n} centers are approved for the TCF by France Éducation international, but
<strong>twelve offer the TCF Canada</strong> according to their websites — nine found on October 8, 2026, plus Los
Angeles, Pasadena and San Diego, checked on October 18 — from <strong>$330</strong> in Detroit to <strong>$505</strong> in
Los Angeles. Four don’t, despite being on the list:
Atlanta, Chicago, Seattle and Washington, which point candidates to the TEF Canada. And seats are scarce: San
Francisco, Philadelphia, Denver and Kansas City were full for the rest of 2026, Detroit until April 2027; by October 18,
New York and San Diego were full too, while Houston, Boston and Los Angeles still had dates.""",
    facts=["<strong>{n} approved centers</strong> (FEI list of October 8, 2026), <strong>12 offering the TCF Canada</strong>: Detroit, Boston (International School), New York, Denver (Alliance and Pluma Academy), Philadelphia, Kansas City, Houston, San Francisco and — checked on October 18 — Los Angeles, Pasadena and San Diego.",
           "<strong>No TCF Canada</strong> in Atlanta (no TCF at all), Chicago (tout public and IRN), Seattle (no TCF) or Washington (DAP only): these Alliances point candidates to the TEF Canada.",
           "TCF Canada fees: <strong>$330 to $505</strong> — Detroit $330, Boston $350, New York $350 (members) or $399, Denver and Philadelphia $360, Kansas City $370, Houston $400, Pluma Academy $435, San Diego $450, Pasadena and San Francisco $460, Los Angeles $505.",
           "⚠️ <strong>Full</strong> for the rest of 2026 in San Francisco, Philadelphia, Denver (Alliance) and Kansas City (October 8), New York and San Diego (October 18); until April 2027 in Detroit.",
           "Still open: <strong>Houston every Wednesday</strong> until January 27, 2027 and Pluma Academy (October 8); <strong>Boston</strong> November 21 and December 12, <strong>Los Angeles</strong> November 20 and December 18, <strong>New York</strong> from January 25, 2027 in Montclair (October 18).",
           "October 26, 2026: <a href=\"/en/tcf-canada-detroit/\">Detroit</a> full until May 13, 2027 (June 10 open); <a href=\"/en/tcf-canada-houston/\">Houston</a>’s TCF page listed no session (TEF Canada $380, seats open); <a href=\"/en/tcf-canada-san-francisco/\">San Francisco</a> November 6 on waitlist, no 2027 date; <a href=\"/en/tcf-canada-denver/\">Denver</a>: the Alliance sold out to December 7, Pluma Academy dates to March 27, 2027.",
           "Waiting period between two attempts: from 20 days (Detroit) to one month (New York, Denver), depending on the center."],
    stats=[("12", "TCF Canada centers", "out of {n} approved"), ("$330-505", "TCF Canada fee", "depending on the center"),
           ("4", "centers full", "for the rest of 2026"), ("2 years", "validity", "results in 10 days to 6 weeks")],
    sections=[
        ("tcf-canada-centers", "Who offers the TCF Canada in the USA", releve([
            ("Alliance française de Detroit (Bingham Farms, Michigan)", "<strong>Canada</strong>, IRN, tout public, DAP",
             "Canada <strong>$330</strong> · IRN $300 ($280 members) · tout public $190 to $350",
             "Monthly, on Thursdays: Nov 12 and Dec 10, 2026, and every session through Apr 15, 2027, <strong>full</strong>; May 13 and Jun 10, 2027 open. Computer-based; results within 10 days. Oct 26: full until May 13, Jun 10 open — <a href=\"/en/tcf-canada-detroit/\">Detroit page</a>."),
            ("International School of Boston (Cambridge, Massachusetts)", "<strong>Canada</strong>, IRN, Québec, tout public",
             "Canada <strong>$350</strong> · IRN $350 · +$60 on weekdays",
             "Saturdays: Oct 10 full (waitlist), <strong>Nov 21</strong> (deadline Nov 17), <strong>Dec 12</strong> (deadline Dec 8), and a January Saturday (Oct 18). Card payment at registration. <a href=\"/en/tcf-canada-boston/\">Boston page</a>."),
            ("L'Alliance New York", "<strong>Canada</strong>, IRN", "<strong>$350</strong> members · $399 non-members, + $15 fee",
             "Oct 26 and Nov 16 and Dec 14 in Montclair, NJ, Nov 6 in Manhattan: all <strong>full</strong> on Oct 18; 2027: Jan 25, Feb 22, Mar 22, Apr 19, May 17, Jun 14, in Montclair. Computer-based. <a href=\"/en/tcf-canada-new-york/\">New York page</a>."),
            ("Alliance française de Denver", "<strong>Canada</strong>; IRN and tout public on request", "Canada <strong>$360</strong> · IRN $360",
             "Nov 16, Nov 30 and Dec 7, 2026 <strong>full</strong>; no 2027 dates. Registration closes seven business days before; passport required. <a href=\"/en/tcf-canada-denver/\">Denver page</a>."),
            ("Alliance Française de Philadelphie", "<strong>Canada</strong>, IRN, tout public", "Canada <strong>$360</strong> ($340 members) · IRN $300",
             "Oct 16 and Dec 18, 2026 <strong>full</strong>; waitlist; registration closes one month before. Paper-based."),
            ("Alliance française de Kansas City", "<strong>Canada</strong>, IRN, tout public, Québec", "Canada <strong>$370</strong> ($380 in 2027) · IRN $370",
             "2026 <strong>full</strong>; 2027: Jan 14 (one seat), Jan 28, Feb 4, Feb 18, Mar 4… through Jun 24, four seats per session. Computer-based."),
            ("Alliance française de Houston", "<strong>Canada</strong> (IRN, tout public and Québec announced, no dates)", "Canada <strong>$400</strong>",
             "<strong>Every Wednesday</strong>, ten seats: Oct 14, 21, 28, Nov 4, Dec 2, 9, 16, 2026, then Jan 6 to 27, 2027; registration closes three days before. Computer-based. Oct 26: no session listed — <a href=\"/en/tcf-canada-houston/\">Houston page</a>."),
            ("Pluma Academy (Denver)", "<strong>Canada</strong>, IRN, tout public", "Canada <strong>$435</strong> · IRN $435 · tout public $255 to $435",
             "Individual sessions, about twenty dates a month from October to March; callback within 24 hours of registering. Computer-based (paper: +$70). Oct 26: dates listed to Mar 27, 2027."),
            ("Alliance française de San Francisco", "<strong>Canada</strong>, IRN, tout public", "Canada <strong>$460</strong> · IRN $550 · tout public $250 + $180 per writing or speaking test",
             "TCF Canada <strong>full</strong> through the end of 2026 (waitlist); no 2027 dates. Passport required; 25 days between two TCF attempts. <a href=\"/en/tcf-canada-san-francisco/\">San Francisco page</a>."),
            ("Alliance française d'Atlanta", "<strong>no TCF</strong>", "—", "“We do NOT currently offer TCF or TEF exams,” the Alliance says."),
            ("Alliance française de Chicago", "tout public and IRN — <strong>no Canada</strong>", "tout public $215 to $385", "Points candidates to the TEF Canada ($415): full until Dec 15, open from Jan 5, 2027 (Oct 18). <a href=\"/en/tcf-canada-chicago/\">Chicago page</a>."),
            ("Alliance française de Seattle", "<strong>no TCF</strong> on its website", "—", "Points candidates to the TEF (TEF Canada $365). <a href=\"/en/tcf-canada-seattle/\">Seattle page</a>."),
            ("Alliance française de Washington", "DAP only — <strong>no Canada</strong>", "DAP $350", "For Canadian immigration, the Alliance refers candidates to the TEF Canada."),
            ("Alliance française de Los Angeles", "<strong>Canada</strong>, tout public, IRN, Québec, DAP", "Canada <strong>$505</strong> (same fee for every version)",
             "Nov 20 and Dec 18, 2026, then Jan 22 to Jun 11, 2027, monthly; apply by email at least 15 days before (Oct 18). <a href=\"/en/tcf-canada-los-angeles/\">Los Angeles page</a>."),
            ("Alliance française de Pasadena", "<strong>Canada</strong>, tout public", "Canada <strong>$460</strong> + 3.5% by card",
             "Nov 12, 2026, deadline Oct 20; no 2027 date (Oct 18)."),
            ("Alliance française de San Diego", "<strong>Canada</strong>", "Canada <strong>$450</strong>",
             "Oct 20 closed, Nov 4 and 10 <strong>sold out</strong>, no later date listed; waitlist (Oct 18). Computer-based written part. <a href=\"/en/tcf-canada-san-diego/\">San Diego page</a>."),
            ("French American School of Puget Sound; Wesleyan University", NR, NR, "Approved by FEI, not checked: see their websites."),
        ], "en-US", "What each center’s website showed on October 8, 2026, and on October 18 for Los Angeles, Pasadena, San Diego and the updates marked (Oct 18) or (Oct 26). “No data”: not published, or not checked — the center’s website is the reference.")),
        ("registration", "Registering — and finding a seat", """<p>Each center sells the test on its own website — online store, session picker, or a form followed by card
payment — and your registration is only final once paid. Enter your name exactly as it appears on your passport:
for the TCF Canada, Detroit reports your passport number to FEI, San Francisco and Denver require a valid passport,
and the ID you show on test day must be the one you registered with. Cancellation rules are strict: nothing is
refunded in Houston or Denver; Detroit keeps $40 up to ten business days before, San Francisco $60 more than 30
days out, New York $80 before the deadline — and San Francisco accepts no changes at all in the eight days before
the test.</p>

<p>The waiting period between two attempts depends on the center: 20 days in Detroit, 21 at Pluma Academy, 25 in
San Francisco, one month in New York and Denver. Results arrive by email or on FEI’s platform, from 10 days
(Detroit) to five or six weeks (New York); the results certificate is valid for two years, and since September 1,
2026, FEI no longer accepts re-marking requests.</p>

<p>With four centers full for the rest of the year, <strong>getting a seat</strong> is what matters. Houston was
opening a session every Wednesday until January 27, 2027, Kansas City was selling dates through June 2027, and
Pluma Academy tests candidates one at a time: it may be worth taking the test in another city. The TEF Canada,
the other French test accepted by IRCC, is offered by the Alliances that don’t run the TCF Canada — Chicago,
Seattle, Washington, and also Dallas and Miami.</p>"""),
        ("city-pages", "City by city", """<p>One page per city, with the center, the fee and the dates —
the newest checked on October 26, 2026: <a href="/en/tcf-canada-new-york/">New York</a> ·
<a href="/en/tcf-canada-boston/">Boston</a> · <a href="/en/tcf-canada-detroit/">Detroit</a> ·
<a href="/en/tcf-canada-chicago/">Chicago</a> (TEF Canada only) · <a href="/en/tcf-canada-houston/">Houston</a> ·
<a href="/en/tcf-canada-denver/">Denver</a> · <a href="/en/tcf-canada-seattle/">Seattle</a> (TEF Canada only) ·
<a href="/en/tcf-canada-san-francisco/">San Francisco</a> · <a href="/en/tcf-canada-los-angeles/">Los Angeles</a> ·
<a href="/en/tcf-canada-san-diego/">San Diego</a>.</p>"""),
    ],
    list_title="The {n} approved TCF test centers, state by state",
    faq=[("Where can I take the TCF Canada in the USA?", "At one of twelve centers: the Alliances Françaises in Detroit, New York, Denver, Philadelphia, Kansas City, Houston and San Francisco, the International School of Boston and Pluma Academy in Denver (October 8, 2026), and the Alliances in Los Angeles, Pasadena and San Diego (October 18). Atlanta, Chicago, Seattle and Washington are approved for the TCF but don’t offer the TCF Canada."),
         ("How much does the TCF Canada cost in the USA?", "From $330 (Detroit) to $505 (Los Angeles): $350 in Boston, $350 for members or $399 in New York, $360 in Denver and Philadelphia, $370 in Kansas City, $400 in Houston, $435 at Pluma Academy, $450 in San Diego, $460 in Pasadena and San Francisco. Prices checked on October 8 and 18, 2026."),
         ("Where can I find a seat quickly?", "On October 8, 2026, the Alliance française de Houston was opening a session every Wednesday until January 27, 2027, and Pluma Academy in Denver runs individual sessions several times a week. On October 18, Boston had November 21 and December 12, Los Angeles November 20 and December 18; New York was full for 2026, with dates from January 25, 2027. San Francisco, Philadelphia, Denver (Alliance) and Kansas City were full for 2026."),
         ("Can I take the TCF Canada in Washington, DC or Chicago?", "No: the Alliance française de Washington now offers only the TCF DAP, and Chicago only the TCF tout public and IRN. Both refer immigration candidates to the TEF Canada, which IRCC also accepts."),
         ("Does IRCC accept a TCF Canada taken in the USA?", "Yes: the results certificate is issued by France Éducation international whichever approved center you test at, and it is valid for two years. IRCC requires results less than two years old both when you create your Express Entry profile and when you submit your application.")],
    also=[("/en/delf-usa/", "DELF and DALF in the USA", "The December 2026 session and the shared fee schedule."),
          ("/en/tcf-canada-test-centres/", "TCF Canada test centers in Canada", "The 48 approved centers, province by province."),
          ("/en/tcf-canada-uk/", "TCF Canada in the UK", "London (£260) and Glasgow (£325).")],
    sources="the websites of the Alliances Françaises of Detroit, Atlanta, Chicago, Denver, Houston, Kansas City, New York, Philadelphia, San Francisco, Seattle and Washington, the International School of Boston and Pluma Academy (TCF pages, online stores and session pickers, exam terms and policies), checked on October 8, 2026; those of L'Alliance New York, the International School of Boston, the Alliances Françaises of Chicago, Los Angeles, Pasadena and San Diego, checked on October 18, 2026; those of the Alliances Françaises of Detroit, Houston, San Francisco, Seattle and Denver and of Pluma Academy, checked on October 26, 2026 for the city pages.",
    notes={"cambridge-lycee-international-de-boston": "Now the International School of Boston (ISB Extension, open to adults).",
           "philadelphie-alliance-francaise": "Paper-based test, according to the Alliance."},
))


# ===========================================================================
# UNITED STATES — DELF-DALF (en-US), from /centres/delf-etats-unis/
# ===========================================================================
PAGES.append(from_fr(
    "delf-etats-unis", "en", "en-US", "États-Unis",
    slug="delf-usa", country_name="United States",
    crumb="DELF in the USA",
    title="DELF exam in the USA: 2026 dates, cost, {n} test centers",
    desc="DELF exam dates and cost in the USA: the December 7–11, 2026 session, a shared fee schedule (B2 $190) plus extra fees, 40 approved centers, registration.",
    h1="DELF and DALF in the USA: the {n} exam centers, dates and fees",
    intro="""In the United States, the DELF and DALF are held at <strong>{n} approved centers</strong> — mostly Alliances
Françaises, but also international schools and universities — overseen by Villa Albertine, the cultural service of
the French Embassy, which publishes neither a calendar nor fees: the centers do. Yet they show the same weeks —
<strong>October 19–23</strong> and <strong>December 7–11, 2026</strong> — and the same fee schedule:
<strong>B2 $190</strong>, to which some add fees. For December, registration closes between November 7 (Houston)
and November 30 (Chicago).""",
    facts=["<strong>{n} exam centers</strong> (FEI list of October 8, 2026): Alliances Françaises, international and immersion schools, universities; Villa Albertine, in Washington, is the central management body.",
           "Next tout public session: <strong>December 7–11, 2026</strong> — A1 and A2 on Monday, B1 on Tuesday, B2 on Wednesday, C1 on Thursday, C2 on Friday.",
           "Shared fee schedule: <strong>A1 $135 · A2 $145 · B1 $155 · B2 $190 · C1 and C2 $245</strong>; extra fees in New York (+$50), San Francisco (+$60), Miami (+$50) and Dallas (+$30).",
           "December registration deadlines: Houston November 7, New York 12, Washington 13, San Francisco 15, Seattle 25, Dallas and St. Louis 27, Chicago November 30.",
           "⚠️ Already full on October 8: B2 and C1 in Chicago; B1, B2 and C1 in Philadelphia; C1 in Denver and Miami; B2 in Boston.",
           "No 2027 dates published; the diploma, printed in France, arrives three to six months after the session."],
    stats=[("{n}", "exam centers", "FEI list of October 8, 2026"), ("$190", "DELF B2", "shared schedule, before extra fees"),
           ("Dec 7–11", "next session", "deadlines November 7 to 30"), ("Lifetime", "diploma validity", "same diploma as in France")],
    sections=[
        ("december-2026-session", "The December 2026 session, center by center", table(
            "Our check of the centers’ websites on October 8, 2026. Shared fee schedule: A1 $135, A2 $145, B1 $155, B2 $190, C1 and C2 $245.",
            ["Center", "Levels in December", "Registration", "Price"],
            [("<strong>L'Alliance New York</strong>", "A1 to C2", "until Nov 12", "shared schedule + $50 fee"),
             ("<strong>Alliance française de Washington</strong>", "A1 to C2; only one session a year", "Nov 9 (9 a.m.) to Nov 13", "shared schedule"),
             ("<strong>Alliance française de Chicago</strong>", "A1, A2, B1, C2; B2 and C1 full", "until Nov 30", "shared schedule"),
             ("<strong>Alliance française de Houston</strong>", "A1 to C2", "until Nov 7", "shared schedule; date change $50"),
             ("<strong>Alliance française de Dallas</strong>", "A1 to C2", "Oct 19 to Nov 27", "shared schedule + $30"),
             ("<strong>Alliance française Miami Metro</strong>", "A1, A2, B1, B2, C2; C1 full", "until Nov 27", "shared schedule + $50"),
             ("<strong>Alliance française de San Francisco</strong>", "A1 to C2; junior Dec 1 to 4", "until Nov 15", "shared schedule + $60 ($30 members)"),
             ("<strong>Alliance française de Seattle</strong>", "A1 to C2", "Oct 19 to Nov 25 (9 a.m.)", "shared schedule"),
             ("<strong>Alliance française de Denver</strong>", "B1, B2, C2; C1 full", "Sep 1 to Nov 20", "own schedule: B1 $217, B2 $270, C1 and C2 $334"),
             ("<strong>Alliance française de Philadelphie</strong>", "A1, A2; B1, B2, C1 full; no C2", "open since Oct 5", "shared schedule; diploma mailing $8"),
             ("<strong>Alliance française de Saint-Louis</strong>", "A1 to C2", "until Nov 27", "shared schedule; increase announced for 2027"),
             ("<strong>Alliance française de La Nouvelle-Orléans</strong>", "A1 to B2", "Oct 19 to Nov 27", "shared schedule"),
             ("<strong>International School of Boston</strong>", "A1 to C2, one level a day from Dec 7 to 12; B2 full", "until Nov 15", "shared schedule + $50"),
             ("<strong>Alliance française de Porto Rico</strong>", "A1 to C2", "until Nov 21", "shared schedule; 5% off for members"),
             ("<strong>Alliance française d'Atlanta</strong>", "A1 to C2", "not yet open online", "shared schedule")]) + """
<p>Villa Albertine publishes no national calendar: according to the Alliance française de Charlotte, dates and fees
are set by the French Embassy in Washington and France Éducation international. In practice, the centers show the
same weeks — March, April, June, October and December in 2026 — and each opens only some of them: Washington just
one a year, in December; Charlotte, Milwaukee and New Orleans only A1 to B2. The DELF junior takes place December
1–4, 2026, in San Francisco; elsewhere, mostly in March — Chicago announces a session in March 2027, with
registration opening in November. No tout public dates for 2027 had been published as of October 8, 2026.</p>"""),
        ("fees", "How much does the DELF cost in the USA?", table(
            "Shared fee schedule found at most centers on October 8, 2026, excluding each center’s own administrative fees.",
            ["Level", "Tout public", "Junior", "Prim"],
            [("A1.1", "—", "—", "$125"), ("A1", "$135", "$135", "$135"), ("A2", "$145", "$145", "$145"),
             ("B1", "$155", "$155", "—"), ("<strong>B2</strong>", "<strong>$190</strong>", "$190", "—"),
             ("C1 (DALF)", "$245", "—", "—"), ("C2 (DALF)", "$245", "—", "—")], wide=False) + """
<p>Several centers add fees: $50 in New York, in Miami and at the International School of Boston, $60 in San
Francisco ($30 for members), $30 in Dallas from December 2026 — which brings a DELF B2 to $240 in New York. Chicago,
on the other hand, charges less for the DELF Prim ($110 to $130). The Alliance française de Denver has its own,
higher schedule: B1 $217, B2 $270, C1 and C2 $334.</p>"""),
        ("registration", "Registration, results and diploma", """<p>There is no national platform: you register with a
center — through an online store (Dallas, Houston, Seattle, Philadelphia, St. Louis, San Francisco), an external
platform (New York, Chicago, and Washington, where you first create an account), or a form plus payment by phone or by check (Minneapolis,
St. Louis). Photo ID: passport, ID card or driver’s license. The test-day notice arrives one week before in New York
and Washington, ten days before in Seattle.</p>

<p>Fees are rarely refundable: never in Houston, Chicago, Miami or San Francisco; before the registration deadline,
minus $80 in New York and Atlanta, $40 in Seattle, $50 in Denver. Results arrive by email from two weeks
(Minneapolis) to six or eight weeks (Philadelphia, Milwaukee, San Francisco) after the exam; the diploma, printed in
France, follows three to six months after the session. In Washington, it can only be picked up in person; San
Francisco offers mailing for $30.</p>

<p>In the United States, the DELF is also used for TAPIF, the program for language assistants in France, which asks
for at least level B1; and the DELF B2, the Alliance française de Washington points out, gives access to French
universities without a prior language test.</p>"""),
    ],
    list_title="The {n} exam centers, state by state",
    faq=[("When is the next DELF exam in the USA?", "December 7–11, 2026, at most centers: A1 and A2 on Monday, December 7, B1 on the 8th, B2 on the 9th, C1 on the 10th, C2 on the 11th. Registration closes between November 7 (Houston) and November 30 (Chicago); no 2027 dates had been published as of October 8, 2026."),
         ("How much does the DELF B2 exam cost in the USA?", "$190 on the centers’ shared fee schedule, to which some add fees: $240 in total in New York and Miami, $250 in San Francisco ($220 for members), $220 in Dallas. The Alliance française de Denver uses its own schedule: $270."),
         ("Where can I take the DELF in New York?", "At L'Alliance New York (22 East 60th Street), which runs the DELF and DALF tout public in June and December: the December 2026 session takes place December 7–11, with registration until November 12, for $135 to $245 plus a $50 administrative fee. The Alliance française de Westchester was not running any session in 2026."),
         ("Can I take the DELF junior in the USA?", "Yes, at Alliances and international schools: San Francisco runs it December 1–4, 2026 (registration until November 15); most other centers offer it in March — Chicago announces a session in March 2027, with registration opening in November. Fees: $135 to $190 depending on the level."),
         ("When do I get my DELF diploma?", "Results arrive by email two to eight weeks after the exam, depending on the center; the diploma, printed in France, three to six months after the session. In Washington, it can only be picked up in person; San Francisco offers mailing for $30.")],
    also=[("/en/tcf-canada-usa/", "TCF Canada in the USA", "Nine centers, from $330 to $460, and the seats still open."),
          ("/en/delf-uk/", "DELF and DALF in the UK", "Sessions from December 2026 to June 2027, B2 at £160."),
          ("/en/", "TCF Canada and DELF, country by country", "Canada, the United States and the United Kingdom.")],
    sources="Villa Albertine’s “Language Certifications” page; the websites of the Alliances Françaises of New York, Washington, Chicago, Houston, Dallas, Miami, San Francisco, Seattle, Denver, Philadelphia, St. Louis, New Orleans, Atlanta, Charlotte, Milwaukee, Minneapolis, Westchester and Puerto Rico, and of the International School of Boston (DELF-DALF calendars, fees and terms), checked on October 8, 2026.",
    notes={"mamaroneck-alliance-francaise-de-westchester": "No DELF session in 2026; the Alliance announces a reorganization.",
           "denver-pluma-academy": "Its website doesn’t mention the DELF.",
           "cambridge-lycee-international-de-boston": "Now the International School of Boston; open to adults through ISB Extension."},
))

# ===========================================================================
# UNITED KINGDOM — TCF (en-GB), from /centres/tcf-royaume-uni/
# ===========================================================================
PAGES.append(from_fr(
    "tcf-royaume-uni", "en", "en-GB", "Royaume-Uni",
    slug="tcf-canada-uk", country_name="United Kingdom",
    crumb="TCF Canada in the UK",
    title="TCF Canada in London and the UK: test centres, fees, dates",
    desc="TCF Canada test centres in the UK: the Institut français in London (£260) and the Alliance française de Glasgow (£325); London full until April 2027.",
    h1="TCF Canada in London and the UK: the test centres, fees and dates",
    intro="""In the United Kingdom, {n} centres are approved for the TCF by France Éducation international, but only two
run it: the <strong>Institut français du Royaume-Uni</strong> in London (TCF Canada <strong>£260</strong>) and the
<strong>Alliance française de Glasgow</strong> (<strong>£325</strong>) — the Alliance française de Jersey publishes no
TCF sessions. On 8 October 2026, places were scarce: in London, the TCF Canada sessions of 20 November and 5 February
were full, and the first open date was <strong>23 April 2027</strong>; in Glasgow, 25 November was full. Here are the
two centres, their rules, and the fallback options.""",
    facts=["<strong>{n} approved centres</strong> (FEI list of 8 October 2026), <strong>2 that run the TCF</strong>: the Institut français in London and the Alliance française de Glasgow; the Alliance française de Jersey publishes no TCF sessions.",
           "<strong>TCF Canada: £260 in London, £325 in Glasgow</strong>; TCF IRN £215 and £245.",
           "⚠️ London: TCF Canada sessions of 20 November 2026 and 5 February 2027 <strong>full</strong>; first open date <strong>23 April 2027</strong> (registration until 18 March). Glasgow: 25 November full, 2027 dates not published.",
           "Both centres run a <strong>paper-based</strong> TCF.",
           "14-day cooling-off period; after that, no refund or postponement, barring exceptions (£38 fee in London).",
           "Results on FEI’s platform, 15 working days after the test in London; digital results certificate, valid for two years."],
    stats=[("{n}", "approved centres", "2 run the TCF"), ("£260", "TCF Canada in London", "£325 in Glasgow"),
           ("23 Apr", "first available place", "in London, in 2027"), ("2 years", "validity", "results in 15 working days")],
    sections=[
        ("tcf-centres", "The TCF in the UK, centre by centre", releve([
            ("Institut français du Royaume-Uni (London)", "<strong>Canada</strong>, IRN, tout public, Québec",
             "Canada <strong>£260</strong> · IRN £215 · tout public £145 + £85 per optional test · Québec £85 per test",
             "Canada about one Friday a month, 35 to 36 places: 20 Nov 2026 and 5 Feb 2027 <strong>full</strong> (on 18 October: 20 Nov registration closed, and a new 15 Jan 2027 session already full); <strong>23 Apr 2027</strong> open (registration until 18 Mar), then May, June, July, September and November 2027. IRN: 29 Jan 2027. No Québec session open. Paper-based."),
            ("Alliance française de Glasgow", "<strong>Canada</strong>, IRN, tout public",
             "Canada <strong>£325</strong> · IRN £245 · tout public £195",
             "Five Canada sessions a year (September, November, March, May, July): 25 Nov 2026 <strong>full</strong>; 2027 dates not published. Tout public 18 Nov and IRN 27 Nov 2026, registration until 15 Oct. Paper-based."),
            ("Alliance française de Jersey", "no TCF session published", "—",
             "The website mentions the TCF only for a preparation course: check with the Alliance."),
        ], "en-GB", "What each centre’s website showed on 8 October 2026. “No data”: not published, or not checked — the centre’s website is the reference.") + """
<p>In London, the Institut’s page and its booking module don’t always match: on 8 October, the TCF Canada sessions of
15 January and 22 October 2027 appeared on the page but not in the module (by 18 October, 15 January was in the module,
already full), and the page dates the February session
“Friday 2 February 2027”, which is a Tuesday — the actual session is on Friday 5 February. The module, where you
pay, is the reference.</p>"""),
        ("registration", "Registering — and getting a place", """<p>In London as in Glasgow, you book and pay
<strong>online</strong>, from the exam page. Enter your name exactly as it appears on your passport — any difference
can get you refused entry to the exam room. The test-day notice arrives two weeks before; on the day, you need an
original photo ID: passport, national identity card, driving licence or residence permit. Latecomers are not
admitted. In Glasgow, a registration is only valid with the confirmation email and the invoice, and it must be sent
to FEI at least 25 days before the exam: nothing is accepted after registration closes.</p>

<p>Both centres give a <strong>14-day</strong> cooling-off period; after that, there is no refund or postponement,
except for documented force majeure — in which case the Institut in London keeps £38, and it only accepts a
transfer before registration closes. Results are posted on France Éducation international’s platform, 15 working
days after the test in London; the results certificate is digital and valid for two years, and FEI has not accepted
re-marking requests since 1 September 2026.</p>

<p>The real issue is getting a <strong>place</strong>: on 8 October 2026, the first open TCF Canada session in
London was on 23 April 2027 — registration for the Institut’s 2027 sessions has been open since 18 August 2026. If your
deadline is sooner, the TEF Canada, the other test accepted by IRCC, is offered at the Institut français d’Écosse
and at the Alliances in Manchester, Cambridge and Oxford; and neighbouring France has 247 TCF centres.</p>"""),
    ],
    list_title="The {n} approved TCF test centres in the UK",
    faq=[("Where can I take the TCF Canada in London?", "At the Institut français du Royaume-Uni, 14 Cromwell Place (South Kensington), the only centre in London approved for the TCF. It offers the TCF Canada for £260, about one Friday a month; on 8 October 2026, its sessions of 20 November 2026 and 5 February 2027 were full, and the first open date was 23 April 2027."),
         ("How much does the TCF Canada cost in the UK?", "£260 at the Institut français in London (the fee since 1 July 2026) and £325 at the Alliance française de Glasgow, as checked on 8 October 2026."),
         ("Is the TCF computer-based in London?", "No: both the Institut français in London and the Alliance française de Glasgow announce a paper-based exam, even though France Éducation international’s list mentions a computer option for London."),
         ("Can I cancel or postpone my TCF?", "Yes, within 14 days of registering. After that, neither centre refunds or postpones, except for documented force majeure; the Institut in London then keeps £38 and only accepts a transfer before registration closes."),
         ("What if all TCF sessions are full?", "Book early: in London, the 2027 sessions have been open since 18 August 2026. Otherwise, the TEF Canada, also accepted by IRCC, is offered at the Institut français d’Écosse and at the Alliances in Manchester, Cambridge and Oxford; France also has 247 TCF centres.")],
    also=[("/en/delf-uk/", "DELF and DALF in the UK", "Sessions from December 2026 to June 2027, B2 at £160."),
          ("/en/tcf-canada-usa/", "TCF Canada in the USA", "Nine centres offer it, from $330 to $460."),
          ("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 48 approved centres, province by province.")],
    sources="the websites of the Institut français du Royaume-Uni (TCF Canada, TCF IRN, TCF tout public and TCF Québec pages, booking modules, terms and conditions) and of the Alliance française de Glasgow (TCF pages, sessions, TCF terms); the website and 2026-2027 brochure of the Alliance française de Jersey, checked on 8 October 2026.",
    notes={"londres-institut-francais-du-royaume-uni": "Computer option according to FEI; the Institut announces a paper-based exam."},
))

# ===========================================================================
# UNITED KINGDOM — DELF-DALF (en-GB), from /centres/delf-royaume-uni/
# ===========================================================================
PAGES.append(from_fr(
    "delf-royaume-uni", "en", "en-GB", "Royaume-Uni",
    slug="delf-uk", country_name="United Kingdom",
    crumb="DELF in the UK",
    title="DELF exam London and UK: {n} centres, 2026-2027 dates, fees",
    desc="DELF and DALF exam dates in London and the UK, December 2026 to June 2027, and fees (B2 £160, £170 in 2027): Edinburgh, Manchester, Glasgow…",
    h1="DELF and DALF in the UK: the {n} exam centres, 2026-2027 dates and fees",
    intro="""In the United Kingdom, the DELF and DALF are held at <strong>{n} approved centres</strong> — the
Institut français in London and the Institut français d’Écosse, the Alliances Françaises of Manchester, Glasgow,
Oxford, Cambridge, Milton Keynes, Leeds and Jersey, and the universities of Exeter and Cardiff. No national calendar is
published, but the written papers fall on the same days everywhere: the next session is in <strong>December
2026</strong> (registration until <strong>29 October</strong> in London), then March and June 2027. The DELF B2 costs
<strong>£160</strong> in 2026 and £170 in 2027, at every centre we checked.""",
    facts=["<strong>{n} exam centres</strong> (FEI list of 8 October 2026), coordinated by the language and education cooperation office of the Institut français du Royaume-Uni.",
           "<strong>December 2026</strong> session: B1 on the 2nd, B2 on the 3rd, A2 on the 7th, C1 on the 9th, C2 on the 10th, A1 on the 14th; registration from 15 to <strong>29 October</strong> in London (31 October in Glasgow, 2 November in Manchester).",
           "Same fees everywhere: <strong>A1 £100 · A2 £105 · B1 £145 · B2 £160 · C1 £205 · C2 £235</strong> in 2026, £5 to £10 more in 2027.",
           "⚠️ December 2026 already full in places on 8 October: B2 in Glasgow, Oxford and Milton Keynes; A2 and B1 in Oxford — and on 18 October, B2 in London too.",
           "The DELF junior appears on the UCAS form: according to the Institut, it is the gateway to French universities.",
           "Diploma three to four months after the results; in London, it is collected on site, by appointment."],
    stats=[("{n}", "exam centres", "FEI list of 8 October 2026"), ("£160", "DELF B2", "£170 for 2027 sessions"),
           ("29 Oct", "London deadline", "for the December session"), ("4", "sessions a year", "roughly, depending on the centre")],
    sections=[
        ("exam-dates", "DELF sessions from December 2026 to June 2027", table(
            "Dates of the DELF-DALF tout public written papers, identical from one centre to the next, as shown on the websites of the Institut français in London, the Institut français d’Écosse and the Alliances in Glasgow, Manchester, Oxford, Milton Keynes and Jersey on 8 October 2026.",
            ["Session", "A1", "A2", "B1", "B2", "C1", "C2", "Registration", "Results"],
            [("<strong>December 2026</strong>", "14 Dec", "7 Dec", "2 Dec", "3 Dec", "9 Dec", "10 Dec", "London 15–29 Oct; Jersey, Milton Keynes 29 Oct; Glasgow 31 Oct; Manchester 2 Nov", "2 Feb 2027 (London)"),
             ("January 2027 (London)", "—", "—", "18 Jan", "21 Jan", "—", "—", "23 Nov – 11 Dec 2026", "26 Feb 2027"),
             ("March 2027", "22 Mar", "23 Mar", "10 Mar", "15 Mar", "18 Mar", "11 Mar", "until 4 Feb 2027", "21 May 2027"),
             ("June 2027", "14 Jun", "15 Jun", "2 Jun", "7 Jun", "10 Jun", "3 Jun", "until 26 Apr 2027", "26 Aug 2027")]) + """
<p>The speaking tests take place on dates set by each centre; London announces them at least two weeks in advance.
No national calendar is published online, even though several sets of terms and conditions refer to one: these
dates are the ones the centres display, identical everywhere. Each centre opens only some levels — the Institut
français d’Écosse holds no tout public session in December, and Oxford only offers A2 to B2. DELF junior: 24 to 30
November 2026 (registration closes on 15 October in London and Jersey, on the 13th in Manchester), then March and
June 2027; DELF Prim: 4 to 6 May 2027, registration until 5 February.</p>"""),
        ("fees", "How much does the DELF cost in the UK?", table(
            "Fees found at ten centres on 8 October 2026 (London, Edinburgh, Glasgow, Manchester, Jersey, Oxford, Milton Keynes, Cambridge, Leeds, Exeter).",
            ["Level", "2026 sessions", "2027 sessions"],
            [("DELF A1", "£100", "£105"), ("DELF A2", "£105", "£110"), ("DELF B1", "£145", "£155"),
             ("<strong>DELF B2</strong>", "<strong>£160</strong>", "<strong>£170</strong>"), ("DALF C1", "£205", "£215"), ("DALF C2", "£235", "£245"),
             ("DELF Prim A1.1 · A1 · A2", "£65 · £70 · £75", "£70 · £75 · £80")], wide=False) + """
<p>The DELF junior costs the same as the tout public version, from A1 to B2. The only exception we found: the
October 2026 A1 at £95 in Milton Keynes. In London, the fee for the December 2026 session was not yet displayed on
8 October (the page shows the 2027 fees, and the booking module opens on 15 October).</p>"""),
        ("registration", "Registration, results and diploma", """<p>There is no national platform: each centre handles its own
registrations. Online booking in London (the “Register here” module), Glasgow, Oxford, Cambridge and Milton Keynes;
payment then form in Manchester; form and payment at the Institut français d’Écosse, in Jersey and in Leeds (by bank
transfer). The name must be the one on your passport; the test-day notice arrives two weeks before; on the day,
bring an original photo ID. Most centres give a 14-day cooling-off period after registration; after that, no refund
or postponement, barring exceptions.</p>

<p>Results arrive by email on a date set for each session in London (2 February 2027 for December), four to eight
weeks after the exam in Manchester and Leeds, and three months after in Cambridge. The diploma follows three to four
months later; in London, it is collected at 14 Cromwell Place by appointment, with no postal delivery, whereas
Glasgow posts it for £5. For French citizenship, the Institut in London points out that B2 is now required; a page
on the Alliance de Leeds website still says B1, which has not been true since 1 January 2026.</p>"""),
    ],
    list_title="The {n} approved exam centres, city by city",
    faq=[("When is the next DELF exam in London?", "In December 2026: B1 on the 2nd, B2 on the 3rd, A2 on the 7th, C1 on the 9th, C2 on the 10th and A1 on 14 December, with registration at the Institut français from 15 to 29 October 2026. A B1-B2 session follows in January 2027, then March and June 2027."),
         ("How much does the DELF B2 exam cost in the UK?", "£160 for 2026 sessions and £170 for 2027 sessions, at every centre checked on 8 October 2026. The DALF costs £205 (C1) and £235 (C2) in 2026, £215 and £245 in 2027."),
         ("Are there still places for the December 2026 DELF?", "On 8 October 2026, the December B2 was full in Glasgow, Oxford and Milton Keynes, as were A2 and B1 in Oxford. London was due to open registration on 15 October; Glasgow still had places in A1, A2 and C1, and Milton Keynes in A1 and A2."),
         ("Does the DELF count for UCAS?", "According to the Institut français du Royaume-Uni, the DELF junior appears on the UCAS application form and serves as a gateway to French universities."),
         ("When will I receive my DELF diploma?", "Results arrive by email on a date set for each session (2 February 2027 for December 2026 in London); the diploma follows three to four months later. In London, it is collected by appointment, with no postal delivery; Glasgow posts it for £5.")],
    also=[("/en/tcf-canada-uk/", "TCF Canada in the UK", "London £260, Glasgow £325; places are scarce."),
          ("/en/delf-usa/", "DELF and DALF in the USA", "The 7–11 December 2026 session; B2 at $190."),
          ("/en/", "TCF Canada and DELF, country by country", "Canada, the United States and the United Kingdom.")],
    sources="the websites of the Institut français du Royaume-Uni (DELF-DALF tout public, junior and Prim pages, booking modules, terms and conditions, “French Diplomas” page), the Institut français d’Écosse, the Alliances Françaises of Glasgow, Manchester, Cambridge, Oxford, Milton Keynes, Jersey and Leeds, and the University of Exeter’s language centre, checked on 8 October 2026.",
    notes={"leeds-leeds-af": "The Alliance’s website (afleeds.org.uk) gives a different address: Brownberrie Lane, LS18 5SB.",
           "exeter-university-of-exeter": "Open to external candidates; 2026-2027 calendar not published on 8 October 2026.",
           "edimbourg-institut-francais-d-ecosse": "Three sessions a year (March, June, October); no tout public session in December 2026.",
           "oxford-alliance-francaise-d-oxford": "A2 to B2 only; December 2026 A2, B1 and B2 full on 8 October."},
))


# ===========================================================================
# CANADA — all provinces
# ===========================================================================
PAGES.append(canada(
    "tcf-canada", slug="tcf-canada-test-centres",
    crumb="TCF Canada test centres",
    title="TCF Canada test centres 2026: 48 in Canada, fees, booking",
    desc="The 48 approved TCF Canada test centres in Canada — Montreal, Toronto, Vancouver, Ottawa… — province by province, with contacts, fees and booking rules.",
    h1="TCF Canada test centres in Canada: the 48 approved centres, province by province",
    modified="2026-10-26", date_label="26 October 2026",   # seats of 26/10/2026 and the new province pages (package F)
    intro="""In Canada, you can take the TCF Canada and the TCF Québec at one of <strong>{n} test centres approved</strong> by
France Éducation international (49 entries on its list of 26 October 2026, one centre appearing twice) —
Alliances Françaises, universities, CEGEPs and training centres — in <strong>nine provinces and Nunavut</strong>,
{so} of them with computer-based sessions. Below: the list by province and city, with the contact details FEI
publishes, and the registration rules we found at the main centres.""",
    facts=["<strong>{n} approved centres</strong> (49 FEI entries, with Gaspé listed twice), list of 26 October 2026: 23 in Quebec, including 7 in Montreal, 8 in Ontario, 5 in British Columbia, 3 in Alberta.",
           "<strong>45 entries with computer-based sessions</strong>; paper-based only in Sherbrooke, in Lethbridge, in Windsor (Collège Boréal) and at the University of Victoria.",
           "Each centre sets its own price, often unpublished: $390 (Alliance française, Vancouver), $400 (Alliance française, Edmonton), $440 (UQTR); nothing posted at the Alliance Française de Montréal.",
           "⚠️ Sessions in Toronto and Vancouver <strong>fill up within minutes</strong>: register the moment registration opens, not as your test date approaches.",
           "Seats on 26 October 2026: open in <a href=\"/en/tcf-canada-new-brunswick/\">New Brunswick</a> ($390: Moncton, Edmundston, Bathurst) and <a href=\"/en/tcf-canada-ottawa/\">Ottawa</a> ($400, 10 November); sold out to December in Calgary, Edmonton, Halifax, Winnipeg and Vancouver; Toronto opens January–March 2027 on 1 December at 10 am.",
           "<strong>20 days</strong> between two attempts, whichever centre you test at; results in 2 to 4 weeks.",
           "No centre in Prince Edward Island, Yukon or the Northwest Territories."],
    stats=[("{n}", "approved centres", "FEI list of 26 October 2026"), ("{so}", "computer-based", "the others paper-based"),
           ("{ncity}", "cities", "from Montreal to Iqaluit"), ("9 + 1", "provinces + Nunavut", "none in P.E.I.")],
    sections=[
        ("registration", "How to register for the TCF Canada in Canada", """<p>FEI’s list doesn’t say which
<em>versions</em> a centre runs (Canada, Québec, tout public, IRN), or its dates and fees: you check those on the
centre’s website or by phone — our city guides below did it for the main centres.</p>

<p>In Canada, each centre handles its own registrations <strong>online, on its own website</strong>, with the
passport you’ll use for your IRCC application. Registration is final, and cancelling costs money: the Alliance Française de Montréal
keeps $75 if you cancel more than 15 days ahead, and refunds nothing after that. In the big cities, sessions
<strong>fill up within minutes</strong>: create your account in advance and log in the moment registration opens.
Allow at least <strong>20 days</strong> between two attempts, whichever centre you test at. Results arrive by email
within 2 to 4 weeks and are valid for two years. On test day, bring a valid passport and your printed test-day
notice (admission letter).</p>"""),
        ("city-guides", "City and province guides: Montreal, Toronto, Ottawa, Vancouver, Alberta, Ontario, New Brunswick…", """<p>For the largest cities, one
page brings together the approved TCF centres with their contacts, what their websites showed on 17 September 2026
— versions, prices, dates — and how to register; the pages dated 26 October 2026 add the next sessions and the
booking windows:</p>
<ul class="posts">
<li><a href="/en/tcf-canada-ontario/">TCF Canada in Ontario</a>
<p>Toronto, North York, Mississauga, Oakville, Ottawa, Kanata, Windsor: $390 to $452; Ottawa open on 10 November (26 October).</p></li>
<li><a href="/en/tcf-canada-alberta/">TCF Canada in Alberta</a>
<p>Calgary and Edmonton, $400, sold out to December; Lethbridge offers only the DELF (26 October).</p></li>
<li><a href="/en/tcf-canada-new-brunswick/">TCF Canada in New Brunswick</a>
<p>Moncton, Edmundston and Bathurst, $390, with open weekend dates to 20 December (26 October).</p></li>
<li><a href="/en/tcf-canada-halifax/">TCF Canada in Halifax</a>
<p>The Alliance Française, $400; the one session listed, 8 December, full (26 October).</p></li>
<li><a href="/en/tcf-canada-winnipeg/">TCF Canada in Winnipeg</a>
<p>The Alliance Française du Manitoba, $400; 9, 11 and 14 December sold out (26 October).</p></li>
<li><a href="/en/tcf-canada-montreal/">TCF Canada in Montreal</a>
<p>Seven approved centres, all computer-based, plus Laval, Kirkland and Saint-Constant; fees rarely published.</p></li>
<li><a href="/en/tcf-canada-toronto/">TCF Canada in Toronto</a>
<p>Four Alliance française campuses and GB Language Centre; quarterly sessions, registration at 10 am a month before.</p></li>
<li><a href="/en/tcf-canada-quebec-city/">TCF Canada in Quebec City</a>
<p>Collège Stanislas and Université Laval, both computer-based, for the TCF Canada and the TCF Québec.</p></li>
<li><a href="/en/tcf-canada-calgary/">TCF Canada in Calgary</a>
<p>The Alliance Française at the Kahanoff Centre, $400, 14 seats a session; sold out to December 2026 (18 October).</p></li>
<li><a href="/en/tcf-canada-edmonton/">TCF Canada in Edmonton</a>
<p>The Alliance Française, $400; each session goes on sale for about an hour (18 October).</p></li>
<li><a href="/en/tcf-canada-ottawa/">TCF Canada in Ottawa</a>
<p>Alliance française Ottawa (computer or paper) and FrancoLangues in Kanata; no entry without a passport and a printed notice.</p></li>
<li><a href="/en/tcf-canada-vancouver/">TCF Canada in Vancouver</a>
<p>$390 at the Alliance française Canada Pacific, where every listed session was sold out on 17 September 2026.</p></li>
</ul>"""),
    ],
    list_title="The {n} approved centres, province by province",
    list_intro="""<form class="finder-mini" action="/en/test-centre-near-me/" method="get" role="search">
<label for="finder-mini-q">Find a test centre near you</label>
<div class="finder-row"><input id="finder-mini-q" name="q" type="search" placeholder="City, country or centre name" autocomplete="off" enterkeyhint="search"><button type="submit">Search</button></div>
<p>TCF, DELF-DALF and TEF: the nearest approved centres, with the distance. <a href="/en/test-centre-near-me/">Or use your location →</a></p>
</form>
<p><strong>New since the 19 September list:</strong> <strong>Collège Boréal</strong> in Windsor, Ontario (7515 Forest Glade
Drive; paper-based, according to FEI), listed below.</p>""",
    faq=[("Where can I take the TCF Canada in Montreal?", "At one of the seven approved centres in Montreal — Alliance Française de Montréal, Collège Stanislas, UQAM, Concordia University, Cégep Marie-Victorin, Centre Yves-Thériault, Collège ELC — or in the suburbs, in Laval, Kirkland and Saint-Constant. All of them offer computer-based sessions."),
         ("Where can I take the TCF Canada in Toronto?", "At the Alliance française de Toronto (Spadina, North York, Mississauga and Oakville campuses) or at GB Language Centre in North York. The Alliance’s sessions are quarterly; registration opens a month before, at 10 am, and fills up within minutes."),
         ("How much does the TCF Canada cost in Canada?", "There is no national fee, and many centres publish nothing: $390 at the Alliance française in Vancouver, $400 in Edmonton, $440 at UQTR among the centres we checked; the Alliance Française de Montréal posts no price."),
         ("Do all these centres offer both the TCF Canada and the TCF Québec?", "Most offer both, but FEI’s list doesn’t say: check which test you tick when you register — the TCF Québec, which is modular, is not accepted by IRCC."),
         ("What do I need to bring on test day?", "A valid passport and your printed test-day notice — no exceptions in Ottawa; your identity is checked throughout the test. For computer-based tests, the centre provides a QWERTY keyboard.")],
    also=[("/en/tcf-canada-usa/", "TCF Canada in the USA", "12 of the 18 approved US centres offer it, from US$330 to US$505."),
          ("/en/tcf-canada/fees-registration/", "TCF Canada fees 2026", "The fee country by country and city by city, each with its date."),
          ("/en/", "All locations", "Every country and city page in English.")],
    sources="the websites of the Alliances Françaises in Montreal, Toronto, Ottawa and Vancouver (Alliance française Canada Pacific) — TCF pages, registration and cancellation terms — checked on 17 September 2026; the city and province pages linked above, checked on 26 October 2026, for the seats open that day.",
))

# ===========================================================================
# TORONTO
# ===========================================================================
PAGES.append(canada(
    "tcf-toronto", slug="tcf-canada-toronto",
    crumb="TCF Canada in Toronto",
    title="TCF Canada Toronto: exam booking, test dates, $390 fee",
    desc="TCF Canada exam booking in Toronto: $390 at the Alliance française (Spadina, North York, Mississauga, Oakville), $452 at GB Language; 2027 opens 1 Dec.",
    h1="Booking the TCF Canada in Toronto: the approved centres, the fees and the 2027 dates",
    modified="2026-10-26", date_label="26 October 2026",   # fees and booking rules read on 26/10/2026 (package F)
    intro="""To book the TCF Canada in Toronto, you have <strong>{n} centres approved</strong> by France Éducation
international: the four campuses of the <strong>Alliance française de Toronto</strong> — Spadina, North York,
Mississauga, Oakville — at <strong>$390</strong>, and <strong>GB Language Centre</strong> in North York, at
<strong>$452</strong> (26 October 2026), all computer-based (paper is also possible at the Alliance). The Alliance’s
sessions are <strong>quarterly</strong>: registration opens a month before at 10 am — for January to March 2027, on
<strong>1 December 2026 at 10 am</strong> — and “If a session is not listed, it is full.” Below: the centres, their
contacts, and how to get a seat.""",
    facts=["<strong>{n} approved centres</strong> in the area: Alliance française de Toronto (Spadina, North York, Mississauga, Oakville) and GB Language Centre.",
           "Fees on 26 October 2026: <strong>$390</strong> at the Alliance française de Toronto, <strong>$452</strong> at GB Language Centre (North York).",
           "<strong>Quarterly sessions</strong> at the Alliance; registration opens <strong>one month before, at 10 am</strong>.",
           "Registration openings for 2027: <strong>1 December 2026</strong> (January to March), 2 March, 20 May, 17 August 2027.",
           "“If a session is not listed, it is full”; no waitlist; one registration at a time; no refunds, a transfer costs $100.",
           "FEI has dropped re-marking for sessions held since 1 September 2026."],
    stats=[("{n}", "approved centres", "FEI list of 26 October 2026"), ("$390", "TCF Canada", "Alliance française, 26 Oct 2026"),
           ("1 Dec", "next booking opening", "10 am, January–March 2027"), ("2 years", "validity", "20 to 30 days between two attempts")],
    sections=[
        ("what-we-found", "What we found, centre by centre", releve([
            ("Alliance française de Toronto (4 campuses)", "Canada (paper or computer-based), Québec", "<strong>$390</strong> (26 Oct 2026; not published on 17 Sept)",
             "Quarterly; registration 1 month before, at 10 am; 2027: 1 Dec 2026, 2 Mar, 20 May, 17 Aug; no waitlist; one registration at a time; transfer up to 15 days before (computer) or 30 days (paper) for $100; no refunds."),
            ("GB Language Centre (North York)", "Canada, tout public, TEF Canada", "<strong>$452</strong> (26 Oct 2026)", "Online booking on its website; TCF tout public $520."),
        ], "en-CA", "What each centre’s website showed on 17 September 2026, updated on 26 October 2026 (fees, transfers). “No data”: not published, or not checked — the centre’s website is the reference.")),
        ("booking-2027", "Booking the January–March 2027 sessions", """<p>The Alliance française de Toronto sells the
TCF Canada <strong>only online</strong>: you create an account on its booking platform beforehand, then, when
registration opens, choose a date — computer-based (E-TCF Canada) or paper-based (P-TCF Canada) — fill in a questionnaire
and pay. For January to March 2027, that is <strong>1 December 2026 at 10 am</strong>; the next openings are 2 March,
20 May and 17 August 2027. Log in before 10 am with your passport at hand: “If a session is not listed, it is full”, and
“There is no waiting list for fully booked sessions”. You may hold only one registration at a time across the four
campuses. Refunds are “not possible under any circumstances”; a transfer costs $100 and must be asked at least 15 days
before a computer session, 30 days before a paper one. Results arrive by email two weeks after a computer-based test,
four weeks after a paper one. Questions about dates go to toronto.exam@alliance-francaise.ca.</p>
<p>GB Language Centre, 716 Gordon Baker Road in North York, sells its TCF Canada sessions on its own website for $452.
If you can travel, the Alliance Française Ottawa ($400) had a computer-based session open on 10 November 2026, and
New Brunswick ($390) had weekend dates until 20 December: see <a href="/en/tcf-canada-ontario/">TCF Canada in
Ontario</a> and <a href="/en/tcf-canada-new-brunswick/">New Brunswick</a>.</p>"""),
        ("registration", "How to book the TCF Canada in Toronto", """<p>In Canada, each centre handles its own registrations
<strong>online, on its own website</strong>, with the passport you’ll use for your IRCC application. Registration is
final, and cancelling costs money: the Alliance Française de Montréal keeps $75 if you cancel more than 15 days ahead,
and refunds nothing after that. In the big cities, sessions <strong>fill up within minutes</strong>: create your
account in advance and log in the moment registration opens. Allow at least <strong>20 days</strong> between two
attempts, whichever centre you test at. Results arrive by email within 2 to 4 weeks and are valid for two years. On
test day, bring a valid passport and your printed test-day notice (admission letter).</p>
<p>For the whole country — the 48 approved centres, province by province, with contacts — see
<a href="/en/tcf-canada-test-centres/">TCF Canada test centres in Canada</a>.</p>"""),
    ],
    list_title="The {n} approved centres in Toronto and the surrounding area",
    faq=[("Where can I take the TCF Canada in Toronto?", "At the Alliance française de Toronto, on four campuses — Spadina (downtown), North York, Mississauga, Oakville — or at GB Language Centre in North York. Registration is online only."),
         ("When does TCF Canada registration open in Toronto?", "A month before each quarter, at 10 am: for 2027, on 1 December 2026 (sessions from January to March), then on 2 March, 20 May and 17 August 2027. Seats go within minutes; there is no waitlist, so check back regularly — seats do free up."),
         ("How much does the TCF Canada cost in Toronto?", "$390 at the Alliance française de Toronto and $452 at GB Language Centre in North York (26 October 2026); on 17 September, the Alliance’s TCF page showed no fee. For reference: $390 in Vancouver, $400 in Edmonton, $440 at UQTR."),
         ("How do I book the TCF Canada exam in Toronto?", "Online only: create an account on the Alliance française de Toronto’s booking platform in advance, then log in when registration opens — 1 December 2026 at 10 am for January to March 2027 — choose a computer or paper session, answer the questionnaire and pay. GB Language Centre takes bookings on its own website."),
         ("Can I take the TCF Canada in North York or Mississauga?", "Yes: the Alliance française de Toronto runs sessions at its North York (47 Sheppard Avenue East) and Mississauga campuses, as well as Spadina and Oakville, for $390; GB Language Centre is also in North York ($452)."),
         ("Paper or computer-based in Toronto?", "The Alliance française offers both formats; GB Language Centre lists computer-based sessions.")],
    also=[("/en/tcf-canada-ontario/", "TCF Canada in Ontario", "Toronto, North York, Ottawa, Kanata, Windsor: fees and next dates."),
          ("/en/tcf-canada-ottawa/", "TCF Canada in Ottawa", "Alliance française Ottawa and FrancoLangues; strict test-day rules."),
          ("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 48 approved centres, province by province, with contacts.")],
    sources="the website of the Alliance française de Toronto (TCF page and registration calendar), checked on 17 September 2026; its TCF Canada pages (fee, 2027 calendar, transfer rules) and GB Language Centre’s website (gblc.ca), checked on 26 October 2026.",
))

# ===========================================================================
# MONTREAL
# ===========================================================================
PAGES.append(canada(
    "tcf-montreal", slug="tcf-canada-montreal",
    crumb="TCF Canada in Montreal",
    modified="2026-10-26", date_label="26 October 2026",   # FEI list read again on 26/10/2026 (contacts)
    title="TCF Canada Montreal: Collège Stanislas, Alliance, 7 centres",
    desc="TCF Canada in Montreal: Collège Stanislas (Outremont), the Alliance Française, UQAM, Concordia and 3 more centres — fees, cancellation, registration.",
    h1="Taking the TCF Canada in Montreal: the 7 approved centres, their rules and registration",
    intro="""In Montreal, the best-served city in Canada, you can take the TCF Canada at <strong>{n} centres approved</strong>
by France Éducation international — Alliance Française de Montréal, Collège Stanislas, UQAM, Concordia University,
Cégep Marie-Victorin, Centre Yves-Thériault, Collège ELC — all with computer-based sessions, plus Laval, Kirkland
and Saint-Constant in the suburbs. Fees, however, are rarely published: the Alliance Française posts none. Below:
the centres with their contacts, the rules we found, and how to register.""",
    facts=["<strong>{n} approved centres</strong> in Montreal, 3 in the suburbs (Laval, Kirkland, Saint-Constant).",
           "<strong>Alliance Française de Montréal: no fee published</strong>; online registration, subject to available seats; $75 kept if you cancel more than 15 days ahead, nothing refunded after that.",
           "<strong>Collège Stanislas</strong>: TCF Québec, Canada, tout public and IRN; $15 per test kept if you cancel more than 15 days ahead.",
           "20 days between two attempts, whichever centre you test at; schedules sent 7 days before — keep the whole day free.",
           "For comparison: $440 at UQTR (Trois-Rivières), $390 in Vancouver, $400 in Edmonton."],
    stats=[("{n}", "approved centres", "FEI list of 26 October 2026"), ("{so}", "computer-based", "all centres in the city"),
           ("checked", "17 Sept 2026", "prices and dates read on the websites"), ("2 years", "validity", "20 to 30 days between two attempts")],
    sections=[
        ("what-we-found", "What we found, centre by centre", releve([
            ("Alliance Française de Montréal", "Canada, Québec", "<strong>not published</strong>",
             "Online registration, subject to available seats; one change allowed, more than 15 days ahead; cancellation: $75 kept; schedules 7 days before."),
            ("Collège Stanislas (Outremont)", "Québec, Canada, tout public, IRN", NR,
             "Full payment at registration; free rescheduling more than 15 days ahead; $15 per test kept on cancellation."),
            ("UQAM (francization) · Concordia · Cégep Marie-Victorin · Centre Yves-Thériault · Collège ELC", NR, NR, "On the centre’s website."),
        ], "en-CA", "What each centre’s website showed on 17 September 2026. “No data”: not published, or not checked — the centre’s website is the reference.")),
        ("registration", "How to register in Montreal", """<p>In Canada, each centre handles its own registrations
<strong>online, on its own website</strong>, with the passport you’ll use for your IRCC application. Registration is
final, and cancelling costs money: the Alliance Française de Montréal keeps $75 if you cancel more than 15 days ahead,
and refunds nothing after that. In the big cities, sessions <strong>fill up within minutes</strong>: create your
account in advance and log in the moment registration opens. Allow at least <strong>20 days</strong> between two
attempts, whichever centre you test at. Results arrive by email within 2 to 4 weeks and are valid for two years. On
test day, bring a valid passport and your printed test-day notice (admission letter).</p>
<p>For the whole country — the 48 approved centres, province by province, with contacts — see
<a href="/en/tcf-canada-test-centres/">TCF Canada test centres in Canada</a>.</p>"""),
    ],
    list_title="The {n} approved centres in Montreal",
    faq=[("Where can I take the TCF Canada in Montreal?", "At one of the seven approved centres — Alliance Française de Montréal, Collège Stanislas, UQAM, Concordia University, Cégep Marie-Victorin, Centre Yves-Thériault, Collège ELC — or in the suburbs, in Laval, Kirkland and Saint-Constant, all computer-based. You register online, centre by centre."),
         ("How much does the TCF Canada cost in Montreal?", "Montreal’s main centres don’t publish their fees: the Alliance Française de Montréal posts no price, and the amount appears when you book. For reference: $440 at UQTR, $390 at the Alliance française in Vancouver, $400 in Edmonton."),
         ("Can I cancel or reschedule a TCF session in Montreal?", "At the Alliance Française, one change is allowed more than 15 days ahead, and $75 is kept if you cancel; nothing is refunded after that. At Collège Stanislas, rescheduling is free more than 15 days ahead, and $15 per test is kept on cancellation. And whichever centre you choose, allow at least 20 days between two attempts."),
         ("TCF Canada or TCF Québec in Montreal?", "The same centres offer both. For a federal application — Express Entry, citizenship — only the TCF Canada is accepted; for a Quebec program, the TCF Québec, which is modular, lets you take only the required tests.")],
    also=[("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 48 approved centres, province by province, with contacts."),
          ("/en/tcf-canada-quebec-city/", "TCF Canada in Quebec City", "Collège Stanislas and Université Laval, both computer-based."),
          ("/en/tcf-canada-ottawa/", "TCF Canada in Ottawa", "Alliance française Ottawa and FrancoLangues; strict test-day rules.")],
    sources="the websites of the Alliance Française de Montréal and Collège Stanislas (TCF pages, registration and cancellation terms), checked on 17 September 2026.",
))

# ===========================================================================
# QUEBEC CITY
# ===========================================================================
PAGES.append(canada(
    "tcf-quebec-ville", slug="tcf-canada-quebec-city",
    crumb="TCF Canada in Quebec City",
    modified="2026-10-29", date_label="29 October 2026",   # centres' websites read again on 29/10/2026 (Laval: $405 and dates; Stanislas: weekly morning sessions)
    title="TCF Canada in Quebec City: Stanislas and Université Laval",
    desc="The 2 approved TCF centres in Quebec City: Collège Stanislas (Sainte-Foy, weekday mornings) and Université Laval ($405, Friday-Saturday); dates and rules.",
    h1="Taking the TCF in Quebec City: the two approved centres and registration",
    intro="""In Quebec City, you can take the TCF at <strong>{n} centres approved</strong> by France Éducation international, both
computer-based: <strong>Collège Stanislas</strong> (1605, chemin Sainte-Foy), which runs TCF Canada sessions almost every
weekday morning until 16 December 2026, and the <strong>École de langues de l’Université Laval</strong> (Pavillon
Charles-De Koninck), at <strong>$405</strong> for the four tests, one Friday-Saturday a week until 12 December. Check which
box you tick: only the TCF Canada counts for Express Entry. Below: the centres, their dates and rules as read on
29 October 2026, and how to register.""",
    facts=["<strong>{n} approved centres</strong>: Collège Stanislas (1605, chemin Sainte-Foy; 418 527-9998, ext. 3239; tcfquebec@stanislas.qc.ca) and Université Laval (Pavillon Charles-De Koninck, 1030 avenue des Sciences-Humaines).",
           "<strong>Université Laval: $405</strong> for the four tests; sessions open to the public on 29 October 2026: 20-21 and 27-28 November, 4-5 and 11-12 December (speaking on Friday, the three other tests on Saturday); no refund and no date change.",
           "<strong>Collège Stanislas</strong>: TCF Canada in the morning, Monday to Thursday (and some Saturdays), every week from 2 November to 16 December 2026; TCF Québec on Saturdays 7 and 21 November, 5 and 12 December; fee not posted (administrative fee + exam fee, paid at registration).",
           "Stanislas: free rescheduling more than 15 days ahead, cancellation refunded minus $15 per test; under 15 days, nothing, except documented force majeure; 20 days between two attempts at the same test, whichever centre.",
           "Université Laval: photo ID with signature (driver’s licence, health-insurance card or passport — not the student card) and your registration receipt; two blocks: a 20-minute speaking interview, then listening, reading and writing on computer; accommodations on a medical certificate sent two months ahead.",
           "Re-marking of the speaking and writing tests: suspended by France Éducation international for sessions from 1 September 2026, “for about a year”.",
           "The TCF Canada has also been recognized by the MIFI since 2022; results by email within 2 to 4 weeks; certificate valid for 2 years."],
    stats=[("{n}", "approved centres", "FEI list of 26 October 2026"), ("{so}", "computer-based", "all centres in the city"),
           ("$405", "TCF Canada at Université Laval", "read on 29 Oct 2026"), ("2 years", "validity", "20 to 30 days between two attempts")],
    sections=[
        ("what-we-found", "What we found, centre by centre", releve([
            ("Collège Stanislas (Quebec City)", "Québec, Canada, tout public (on request), IRN", "not posted (administrative fee + exam fee)",
             "TCF Canada in the morning, Monday-Thursday and some Saturdays, from 2 Nov to 16 Dec 2026; TCF Québec Sat 7 and 21 Nov, 5 and 12 Dec; online registration; $15 per test kept if you cancel more than 15 days ahead."),
            ("Université Laval (ELUL)", "Canada, tout public", "Canada <strong>$405</strong>",
             "Public sessions: 20-21 Nov, 27-28 Nov, 4-5 Dec, 11-12 Dec 2026 (speaking Friday, other tests Saturday); extra sessions reserved for the ULaval community; online registration (Brio platform); no refund."),
        ], "en-CA", "What each centre’s website showed on 29 October 2026. “No data”: not published, or not checked — the centre’s website is the reference.")),
        ("registration", "How to register in Quebec City", """<p>In Canada, each centre handles its own registrations
<strong>online, on its own website</strong>, with the passport you’ll use for your IRCC application. Registration is
final, and cancelling costs money: the Alliance Française de Montréal keeps $75 if you cancel more than 15 days ahead,
and refunds nothing after that. In the big cities, sessions <strong>fill up within minutes</strong>: create your
account in advance and log in the moment registration opens. Allow at least <strong>20 days</strong> between two
attempts, whichever centre you test at. Results arrive by email within 2 to 4 weeks and are valid for two years. On
test day, bring a valid passport and your printed test-day notice (admission letter).</p>
<p>For the whole country — the 48 approved centres, province by province, with contacts — see
<a href="/en/tcf-canada-test-centres/">TCF Canada test centres in Canada</a>.</p>"""),
    ],
    list_title="The {n} approved centres in Quebec City",
    faq=[("Where can I take the TCF Canada in Quebec City?", "At Collège Stanislas (1605, chemin Sainte-Foy) or at Université Laval’s École de langues (Pavillon Charles-De Koninck), both approved and computer-based; you register online, on their websites. Stanislas opens sessions almost every weekday morning, Laval one Friday-Saturday a week."),
         ("How much does the TCF cost in Quebec City?", "$405 for the four tests at Université Laval (29 October 2026), with no refund and no date change. Collège Stanislas does not post its fee: an administrative fee, never refunded, plus an exam fee, paid in full at registration. At UQTR, in Trois-Rivières, the TCF Canada costs $440."),
         ("When are the TCF Canada sessions in Quebec City?", "On 29 October 2026: at Stanislas, every week from 2 November to 16 December, Monday to Thursday in the morning, plus Saturdays 14 and 28 November; at Université Laval, 20-21 November, 27-28 November, 4-5 December and 11-12 December, speaking on Friday and the other tests on Saturday. The centres’ websites are the reference."),
         ("TCF Canada or TCF Québec in Quebec City?", "For a Quebec program, both are accepted; for Express Entry or citizenship, only the TCF Canada. The TCF Québec is modular and lets you take only the required tests; the TCF Canada cannot be split: all four tests together.")],
    also=[("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 48 approved centres, province by province, with contacts."),
          ("/en/tcf-canada-montreal/", "TCF Canada in Montreal", "Seven approved centres, plus Laval, Kirkland and Saint-Constant."),
          ("/en/tcf-canada-ottawa/", "TCF Canada in Ottawa", "Alliance française Ottawa and FrancoLangues; strict test-day rules.")],
    sources="the websites of Collège Stanislas (TCF page: sessions, registration, cancellation and refund terms) and of Université Laval’s École de langues (TCF Canada and TCF tout public pages: fee, public sessions, ID rules, accommodations), and France Éducation international’s TCF Canada page (re-marking notice), read on 29 October 2026.",
))

# ===========================================================================
# OTTAWA
# ===========================================================================
PAGES.append(canada(
    "tcf-ottawa", slug="tcf-canada-ottawa",
    crumb="TCF Canada in Ottawa",
    title="TCF Canada Ottawa: dates, $400 fee, FrancoLangues Kanata",
    desc="TCF Canada in Ottawa: the Alliance Française ($400; 10 November and January dates open on 26 October 2026) and FrancoLangues in Kanata. How to book.",
    h1="Taking the TCF Canada in Ottawa: the two approved centres, the next dates and booking",
    modified="2026-10-26", date_label="26 October 2026",   # fee, sessions and FrancoLangues rules read on 26/10/2026 (package F)
    intro="""In Ottawa, you can take the TCF Canada at <strong>{n} centres approved</strong> by France Éducation international,
both computer-based: the <strong>Alliance française Ottawa</strong> (352 MacLaren Street), which also offers it on
paper, and <strong>FrancoLangues</strong> in Kanata. On 26 October 2026, the Alliance charged <strong>$400</strong> and
had seats on <strong>10 November 2026</strong> and on 6 and 8 January 2027 (computer), and on 14 January 2027 (paper).
It is strict on test day — a valid passport and the printed test-day notice, with no exceptions — and sends results by
email within two to three weeks. Below: the centres, their contacts, and how to book.""",
    facts=["<strong>{n} approved centres</strong>: Alliance française Ottawa and FrancoLangues (Kanata).",
           "<strong>Alliance française Ottawa: $400</strong>; open on 26 October 2026: <strong>10 November 2026</strong>, 6 and 8 January 2027 (computer), 14 January 2027 (paper); further January dates on sale from 1 November.",
           "<strong>Alliance française Ottawa</strong>: TCF Canada computer-based or paper-based; a valid passport and the printed test-day notice are mandatory, with no exceptions.",
           "<strong>FrancoLangues</strong> (105 Schneider Road, Kanata): booking through its online appointment page; no refunds or date changes; 30 days between two tests.",
           "Results by email within 2 to 3 weeks; no duplicate of the results certificate.",
           "Accommodations: request them before you register, with medical documentation.",
           "FEI has dropped re-marking for sessions held since 1 September 2026."],
    stats=[("{n}", "approved centres", "FEI list of 26 October 2026"), ("$400", "TCF Canada", "Alliance française, 26 Oct 2026"),
           ("10 Nov", "next open date", "computer-based, 2026"), ("2 years", "validity", "20 to 30 days between two attempts")],
    sections=[
        ("what-we-found", "What we found, centre by centre", releve([
            ("Alliance française Ottawa", "Canada (computer or paper-based), other versions", "<strong>$400</strong> (26 Oct 2026)",
             "Computer: 10 Nov 2026, 6 and 8 Jan 2027 open; paper: 14 Jan 2027 open (26 Oct); «No dates will be communicated by email or phone»; passport + printed test-day notice mandatory; identity checked during the test; results in 2–3 weeks."),
            ("FrancoLangues (Kanata)", "Canada, Québec", NR,
             "Online appointment page; fee given by the centre; no refunds or date changes; 30 days between two tests; certificate 4 to 8 weeks after the test (26 Oct)."),
        ], "en-CA", "What each centre’s website showed on 17 September 2026, updated on 26 October 2026. “No data”: not published, or not checked — the centre’s website is the reference.")),
        ("booking", "Booking the next sessions in Ottawa", """<p>The <strong>Alliance française Ottawa</strong> lists its
TCF Canada sessions on its TCF page, each with its price and either an «Add to cart» button or the date its sales open;
«No dates will be communicated by email or phone», so the page is the only place to watch. On 26 October 2026, the
computer-based sessions of 10 November 2026 and 6 and 8 January 2027 were open, the paper-based session of 14 January
2027 too, and later January dates were to go on sale on 1 November 2026 — all at $400.</p>
<p><strong>FrancoLangues</strong>, at 105 Schneider Road in Kanata, takes TCF bookings through its online appointment
page and gives its fee when you book. Its rules are strict: «No refunds or test date changes will be accepted under any
circumstances», 30 days between two tests, and the certificate arrives four to eight weeks after the test. Every
centre in the province: <a href="/en/tcf-canada-ontario/">TCF Canada in Ontario</a>.</p>"""),
        ("registration", "How to register in Ottawa", """<p>In Canada, each centre handles its own registrations
<strong>online, on its own website</strong>, with the passport you’ll use for your IRCC application. Registration is
final, and cancelling costs money: the Alliance Française de Montréal keeps $75 if you cancel more than 15 days ahead,
and refunds nothing after that. In the big cities, sessions <strong>fill up within minutes</strong>: create your
account in advance and log in the moment registration opens. Allow at least <strong>20 days</strong> between two
attempts, whichever centre you test at. Results arrive by email within 2 to 4 weeks and are valid for two years. On
test day, bring a valid passport and your printed test-day notice (admission letter).</p>
<p>For the whole country — the 48 approved centres, province by province, with contacts — see
<a href="/en/tcf-canada-test-centres/">TCF Canada test centres in Canada</a>.</p>"""),
    ],
    list_title="The {n} approved centres in Ottawa",
    faq=[("Where can I take the TCF Canada in Ottawa?", "At the Alliance française Ottawa (352 MacLaren Street), computer-based or on paper, or at FrancoLangues in Kanata; both are approved."),
         ("What should I bring on test day in Ottawa?", "A valid passport and your printed test-day notice: the Alliance française refuses entry without both, with no exceptions, and checks identity throughout the test."),
         ("How much does the TCF Canada cost in Ottawa?", "$400 at the Alliance française Ottawa, for the computer-based or the paper-based test (26 October 2026); on 17 September its TCF page showed no fee. FrancoLangues gives its fee when you book. For reference: $390 in Vancouver, $400 in Edmonton, $440 at UQTR."),
         ("When is the next TCF Canada in Ottawa?", "On 26 October 2026, the Alliance française Ottawa had seats on 10 November 2026 and on 6 and 8 January 2027 (computer), and on 14 January 2027 (paper); further January sessions were to go on sale on 1 November."),
         ("How do I book the TCF at FrancoLangues in Kanata?", "Through FrancoLangues’ online appointment page, linked from its TCF page; the test takes place at 105 Schneider Road, Kanata. No refunds or date changes are accepted, and you must wait 30 days between two tests.")],
    also=[("/en/tcf-canada-ontario/", "TCF Canada in Ontario", "Toronto, North York, Ottawa, Kanata, Windsor: fees and next dates."),
          ("/en/tcf-canada-toronto/", "TCF Canada in Toronto", "$390; 2027 bookings open on 1 December at 10 am."),
          ("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 48 approved centres, province by province, with contacts.")],
    sources="the website of the Alliance française Ottawa (TCF page and test-day rules), checked on 17 September 2026; its TCF Canada session list and FrancoLangues’ TCF page (francolangues.com), checked on 26 October 2026.",
))

# ===========================================================================
# VANCOUVER
# ===========================================================================
PAGES.append(canada(
    "tcf-vancouver", slug="tcf-canada-vancouver",
    crumb="TCF Canada in Vancouver",
    title="TCF Canada Vancouver: booking, $390, New Westminster",
    desc="TCF Canada in Vancouver and New Westminster: $390 at the Alliance française; December sold out on 26 October, sales open ~10 weeks ahead. Booking tips.",
    h1="Booking the TCF Canada in Vancouver and New Westminster: the centres, the fee, the sales windows",
    modified="2026-10-26", date_label="26 October 2026",   # December sessions and sales windows read on 26/10/2026 (package F)
    intro="""In Vancouver, you can take the TCF Canada at <strong>{n} centres approved</strong> by France Éducation international,
all computer-based: the <strong>Alliance française Canada Pacific</strong> — on Cambie Street, with a second site at
320 Columbia Street in <strong>New Westminster</strong> — and Ashton Testing Services. The Alliance charges
<strong>$390</strong>, with 10% off for members and no refunds, and on 17 September 2026 <strong>every session it listed
was “SOLD OUT”</strong>. On 26 October, its December sessions at both sites were sold out too: each one went on sale
about ten weeks ahead, for one week. Below: the centres, their contacts, and how to get a seat.""",
    facts=["<strong>{n} approved centres</strong>: Alliance française Canada Pacific (Vancouver and New Westminster), Ashton Testing Services.",
           "<strong>Alliance française: $390</strong>, 10% off for members; online registration only, and final — no refund, no credit.",
           "Every listed session “SOLD OUT” on 17 September 2026: log in when registration opens, in a single tab, with your passport at hand.",
           "26 October 2026: the December sessions (2, 4, 7, 9, 11, 14, 16, 18 December…) <strong>sold out</strong> in Vancouver and in New Westminster; Vancouver’s were sold from 15 to 22 September, New Westminster’s from 29 September to 6 October.",
           "Results by email within 3 to 4 weeks; QWERTY keyboard, accents through FEI’s platform.",
           "Victoria has two more approved centres (Alliance française de Victoria, University of Victoria)."],
    stats=[("{n}", "approved centres", "FEI list of 26 October 2026"), ("$390", "TCF Canada", "$351 for members"),
           ("~10 weeks", "sales open ahead", "for one week"), ("2 years", "validity", "20 to 30 days between two attempts")],
    sections=[
        ("what-we-found", "What we found, centre by centre", releve([
            ("Alliance française Canada Pacific (Vancouver and New Westminster)", "Canada (+ TEF)", "<strong>$390</strong> ($351 for members)",
             "Online registration only, final; sessions full; December 2026 sold out at both sites (26 Oct); results in 3–4 weeks; QWERTY."),
            ("Ashton Testing Services", NR, NR, "Private testing centre, computer-based."),
        ], "en-CA", "What each centre’s website showed on 17 September 2026, updated on 26 October 2026. “No data”: not published, or not checked — the centre’s website is the reference.")),
        ("sales-windows", "When TCF Canada bookings open in Vancouver", """<p>The Alliance française Canada Pacific
lists each session with its <strong>registration dates</strong>, its site and the seats left. On 26 October 2026, the
December 2026 sessions — at 6161 Cambie Street in Vancouver and at 320 Columbia Street in New Westminster — were all
“SOLD OUT”. Their sales windows show how early you must be ready: about <strong>ten weeks before the test, for one
week</strong> — from 15 to 22 September for the Vancouver sessions, from 29 September to 6 October for New Westminster.
Log in to your account before the window opens, keep your passport number at hand and use a single tab: “Opening multiple
tabs or repeatedly refreshing the page may cancel your reservation”. The Alliance also gives TCF workshop participants
<strong>priority access</strong> to some exam seats, on dates it assigns. The exam location is shown when you buy, and
you get your exact time about a week before the test; the passport is the only ID accepted.</p>
<p><strong>TEF Canada in Vancouver.</strong> IRCC also accepts the TEF Canada, and the same Alliance runs it: on
26 October 2026, the map of TEF centres of Le français des affaires (CCI Paris Île-de-France) showed TEF Canada
sessions published at its Cambie Street site; Collège Éducacentre, also in Vancouver, is an approved TEF centre. The
Alliance sends TEF results within about two weeks, and prefers the TEF for candidates who need accommodations
(<a href="/en/tcf-vs-tef-canada/">TCF vs TEF Canada</a>).</p>"""),
        ("registration", "How to book the TCF Canada in Vancouver", """<p>In Canada, each centre handles its own registrations
<strong>online, on its own website</strong>, with the passport you’ll use for your IRCC application. Registration is
final, and cancelling costs money: the Alliance Française de Montréal keeps $75 if you cancel more than 15 days ahead,
and refunds nothing after that. In the big cities, sessions <strong>fill up within minutes</strong>: create your
account in advance and log in the moment registration opens. Allow at least <strong>20 days</strong> between two
attempts, whichever centre you test at. Results arrive by email within 2 to 4 weeks and are valid for two years. On
test day, bring a valid passport and your printed test-day notice (admission letter).</p>
<p>For the whole country — the 48 approved centres, province by province, with contacts — see
<a href="/en/tcf-canada-test-centres/">TCF Canada test centres in Canada</a>.</p>"""),
    ],
    list_title="The {n} approved centres in Vancouver and New Westminster",
    faq=[("Where can I take the TCF Canada in Vancouver?", "At the Alliance française Canada Pacific (6161 Cambie Street, and New Westminster) or at Ashton Testing Services, all approved and computer-based; you register online, centre by centre."),
         ("How much does the TCF Canada cost in Vancouver?", "$390 at the Alliance française Canada Pacific on 17 September 2026 ($351 for members), and “prices are subject to change without notice”; Ashton doesn’t publish a clear fee."),
         ("How do I get a TCF Canada test date in Vancouver?", "By registering the moment registration opens: the Alliance advises logging in ahead of time with your passport number ready and opening a single tab — “opening multiple tabs or repeatedly refreshing the page may cancel your reservation”."),
         ("When do TCF Canada bookings open in Vancouver?", "About ten weeks before each session, for one week: the December 2026 sessions were sold from 15 to 22 September (Vancouver) and from 29 September to 6 October (New Westminster), and were all sold out on 26 October 2026."),
         ("Can I take the TCF Canada in New Westminster?", "Yes: the Alliance française Canada Pacific holds sessions at #101-320 Columbia Street, New Westminster, at the same $390 fee; the site is shown when you book."),
         ("Can I take the TEF Canada in Vancouver?", "Yes: the Alliance française Canada Pacific runs the TEF Canada too, and on 26 October 2026 the map of Le français des affaires (CCI Paris Île-de-France) showed TEF Canada sessions published there; Collège Éducacentre is also an approved TEF centre.")],
    also=[("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 48 approved centres, province by province, with contacts."),
          ("/en/tcf-canada-alberta/", "TCF Canada in Alberta", "Calgary and Edmonton, $400; Lethbridge DELF only."),
          ("/en/tcf-vs-tef-canada/", "TCF vs TEF Canada", "The two French tests IRCC accepts, side by side.")],
    sources="the websites of the Alliance française Canada Pacific and Ashton Testing Services, checked on 17 September 2026; the Alliance’s TEF & TCF and TCF Canada pages (session table and registration dates) and the map of TEF centres of Le français des affaires, checked on 26 October 2026.",
))


# ===========================================================================
# INDIA (FEI list and centre websites read on 8 October 2026)
# ===========================================================================
_CA = [("ok", "TCF Canada")]
PAGES.append(dict(
    lang="en", variant="en-GB", og_locale="en_IN", fr_path="/centres/tcf-inde/", slug="tcf-canada-india",
    country_name="India", exam="tcf", file="tcf_inde", layout="cities",
    modified="2026-10-26", date_label="26 October 2026", list_date="26 October 2026", releve_date="8 October 2026",   # FEI list read again on 26/10/2026
    crumb="TCF Canada in India",
    title="TCF Canada exam in India: centres, ₹26,000 fee, dates",
    desc="TCF Canada exam centres in India: New Delhi, Kolkata, Ahmedabad, Bangalore, Bhopal. Fee ₹26,000 where published; next dates and how to register.",
    h1="TCF Canada in India: the centres that offer it, the fee and the next dates",
    intro="""In India, {n} Alliances Françaises are approved for the TCF by France Éducation international, but on 8 October
2026 <strong>five offered the TCF Canada</strong> on their websites: New Delhi, Kolkata, Ahmedabad, Bangalore and Bhopal.
Where the fee is published, it is <strong>₹26,000</strong> (GST included in New Delhi and Kolkata). Seats are scarce: Delhi’s October sessions and
Bangalore’s 14 November session were full; the next dates were <strong>18 and 25 November</strong> in Delhi (registration
4–11 November) and <strong>4 December</strong> in Bhopal (one seat left). Lucknow points Canada candidates to the TEF
Canada, and Trivandrum announces the TCF as “coming soon”.""",
    facts=["<strong>{n} approved centres</strong> (FEI list of 26 October 2026), all Alliances Françaises; <strong>5 offer the TCF Canada</strong>: New Delhi, Kolkata, Ahmedabad, Bangalore and Bhopal.",
           "Fee: <strong>₹26,000</strong> in New Delhi, Kolkata and Bhopal (GST included in New Delhi and Kolkata; Bhopal doesn’t say); not published in Ahmedabad or Bangalore.",
           "Next dates on 8 October 2026: New Delhi <strong>18 and 25 November</strong> (registration 4–11 November), then 16 December; Bhopal <strong>4 December</strong> (one seat left), then February–March 2027; Ahmedabad “to be confirmed”.",
           "⚠️ <strong>Full</strong>: New Delhi on 14 and 28 October, Bangalore on 14 November.",
           "No TCF Canada in Lucknow (TEF Canada only) or Trivandrum (“TCF Exam Coming Soon!”, e-TEF Canada for now); Mumbai and Chennai are not on FEI’s TCF list.",
           "Computer-based in New Delhi, Kolkata and Ahmedabad, paper-based in Bhopal; re-marking has stopped for sessions held since 1 September 2026."],
    stats=[("5", "centres offering the TCF Canada", "out of {n} approved"), ("₹26,000", "TCF Canada fee", "where published"),
           ("18 Nov", "next date in New Delhi", "registration 4–11 Nov"), ("2 years", "validity", "results in 2 to 8 weeks")],
    sections=[
        ("tcf-canada-centres", "Who offers the TCF Canada in India", releve([
            ("Alliance Française de Delhi (New Delhi)", "<strong>Canada</strong> only", "<strong>₹26,000</strong> incl. GST",
             "14 and 28 Oct <strong>full</strong>; <strong>18 and 25 Nov</strong> (registration 4–11 Nov, “to be confirmed”), 16 Dec (registration 2–9 Dec). Computer-based; a valid passport is required at registration; results in 2–4 weeks."),
            ("Alliance Française du Bengale (Kolkata)", "<strong>Canada</strong>, Québec, tout public, IRN",
             "Canada <strong>₹26,000</strong> incl. GST · Québec ₹6,500 per test · tout public ₹13,000 (+ ₹6,500 per optional test)",
             "Dates on an external booking calendar; register at least 15 days before; computer-based; for sessions from January 2027, one postponement of up to 3 months for 50% of the fee (₹13,000)."),
            ("Alliance Française d’Ahmedabad", "<strong>Canada</strong>", "not published",
             "“New upcoming sessions to be confirmed”; online form, then a payment link by email; computer-based; certificate within 15 working days."),
            ("Alliance Française de Bangalore", "<strong>Canada</strong>", "not published",
             "14 Nov 2026 <strong>full</strong>; no other date published; at least 20 days between attempts."),
            ("Alliance Française de Bhopal", "<strong>Canada</strong>", "<strong>₹26,000</strong>",
             "<strong>4 Dec 2026</strong> (one seat left), then 12, 19, 26 Feb and 12, 19, 25 Mar 2027; registration closes one month before; paper-based; 30 days between attempts; results in 4–8 weeks."),
            ("Alliance Française de Lucknow", "no TCF page — <strong>TEF Canada</strong>", "TEF Canada ₹26,000 incl. GST",
             "Presents the TEF Canada as its test for Canadian immigration."),
            ("Alliance Française de Trivandrum", "“TCF Exam Coming Soon!”", "—", "e-TEF Canada on computer for now."),
        ], "en-GB", "What each centre’s website showed on 8 October 2026, fees in Indian rupees. “No data”: not published, or not checked — the centre’s website is the reference.")),
        ("registration", "Registering for the TCF Canada in India", """<p>Each Alliance sells the test itself: an online
shop in Bhopal, an online form followed by a payment link in Ahmedabad, an online form that includes payment in Kolkata, an online account or the front desk
in New Delhi — and a seat only counts once it is paid. Register with the passport you will use for your IRCC
application: New Delhi has accepted <strong>only a valid passport</strong> since January 2026; Bhopal asks for a scanned
photo ID (passport or Aadhaar). In Delhi, registration opens at 9:30 am online and 9 am at the desk, and the page warns
that seats “often fill within minutes”.</p>

<p>Refunds are rare: Ahmedabad and New Delhi refund nothing once you are registered (unless Delhi cancels the session),
and Bhopal refunds nothing if you arrive late or without your original photo ID. Leave <strong>20 to 30 days</strong>
between two attempts — 20 in Bangalore and Kolkata, 30 in Bhopal. Results take 15 working days in Ahmedabad, 2 to 4
weeks in Delhi and 4 to 8 weeks in Bhopal; the results certificate is valid for two years, and re-marking has stopped
for sessions held since 1 September 2026. For Express Entry, aim for CLB 7: 458 in listening, 453 in reading.</p>

<p>The <a href="/en/tcf-vs-tef-canada/">TEF Canada</a>, the other French test IRCC accepts, is the alternative where the TCF
is full or not offered: Lucknow and Trivandrum (e-TEF) run it, and Ahmedabad and Bhopal offer it alongside the TCF.
Lucknow’s page says the TEF Canada fee — ₹26,000 including GST — is the same at every Alliance Française in India.</p>"""),
        ("cities", "City by city", """<p>One page per city, with the centre, the fee and the dates:
<a href="/en/tcf-canada-new-delhi/">New Delhi</a> · <a href="/en/tcf-canada-kolkata/">Kolkata</a> ·
<a href="/en/tcf-canada-ahmedabad/">Ahmedabad</a> · <a href="/en/tcf-canada-bangalore/">Bangalore</a> ·
<a href="/en/tcf-canada-bhopal/">Bhopal</a>.</p>"""),
    ],
    list_title="The {n} approved TCF centres in India, city by city",
    faq=[("Where can I take the TCF Canada in India?", "At one of the five Alliances Françaises that offered it on 8 October 2026: New Delhi, Kolkata, Ahmedabad, Bangalore and Bhopal. Lucknow and Trivandrum are approved for the TCF but only offer the TEF Canada for now; Mumbai and Chennai are not on France Éducation international’s TCF list."),
         ("How much does the TCF Canada cost in India?", "₹26,000 at New Delhi, Kolkata and Bhopal (GST included in Delhi and Kolkata), as published on 8 October 2026; Ahmedabad and Bangalore don’t show their fee. Kolkata also lists the TCF Québec at ₹6,500 per test."),
         ("When are the next TCF Canada dates in India?", "On 8 October 2026: 18 and 25 November in New Delhi (registration 4–11 November, marked “to be confirmed”) and 16 December; 4 December in Bhopal (one seat left), then six dates in February and March 2027. Delhi’s October sessions and Bangalore’s 14 November session were full."),
         ("Is the TCF Canada computer-based in India?", "In New Delhi, Kolkata and Ahmedabad, yes. Bhopal runs a paper-based (“Pen & Paper”) TCF Canada."),
         ("Is a TCF Canada taken in India accepted by IRCC?", "Yes: the results certificate is issued by France Éducation international whichever approved centre you test at, and it is valid for two years.")],
    also=[("/en/tcf-canada-dubai/", "TCF Canada in Dubai and Abu Dhabi", "1,800 AED, sessions from 23 October 2026."),
          ("/en/tcf-canada/fees-registration/", "TCF Canada fees and registration", "Fees country by country, and how booking works."),
          ("/en/tcf-vs-tef-canada/", "TCF vs TEF Canada", "The two French tests IRCC accepts, side by side.")],
    sources="the websites of the Alliances Françaises of New Delhi (afdelhi.org), Kolkata, Ahmedabad, Bangalore, Bhopal, Lucknow and Trivandrum (TCF and TEF pages, schedules, registration forms and online shops), checked on 8 October 2026.",
    badges={"ahmedabad-alliance-francaise": _CA + [("part", "dates to be confirmed")],
            "bangalore-alliance-francaise": _CA + [("part", "14 Nov full")],
            "bhopal-alliance-francaise": _CA, "calcutta-alliance-francaise-du-bengale": _CA, "new-delhi-alliance-francaise": _CA,
            "lucknow-alliance-francaise": [("no", "TEF Canada only")],
            "trivandrum-alliance-francaise-de-trivandrum": [("part", "TCF coming soon")]},
    urls={"ahmedabad-alliance-francaise": "https://ahmedabad.afindia.org/tcf/",
          "bangalore-alliance-francaise": "https://bangalore.afindia.org/tcf-cannada/",
          "bhopal-alliance-francaise": "https://bhopal.afindia.org/tcfcanada/",
          "calcutta-alliance-francaise-du-bengale": "https://bengale.afindia.org/tcf/",
          "lucknow-alliance-francaise": "https://lucknow.afindia.org/",
          "new-delhi-alliance-francaise": "https://afdelhi.org/tcf-exams/"},
))

# ===========================================================================
# INDIA — city pages (17/10/2026): «tcf kolkata», «tcf ahmedabad», «tcf bangalore», «tcf bhopal» landed on the single
# India page. Facts: the 8 October 2026 check already on /en/tcf-canada-india/ (no new research).
# ===========================================================================
def _india_city(slug, match, city, title, desc, h1, intro, facts, stats, sections, faq, key, url):
    return dict(lang="en", variant="en-GB", og_locale="en_IN", fr_path=None, slug=slug, country_name="India", exam="tcf",
                file="tcf_inde", layout="city", match=match, crumb=f"TCF Canada in {city}", published="2026-10-17",
                date_label="17 October 2026", list_date="8 October 2026", releve_date="8 October 2026",
                title=title, desc=desc, h1=h1, intro=intro, facts=facts, stats=stats, sections=sections,
                list_title=f"The approved TCF centre in {city}", faq=faq,
                also=[("/en/tcf-canada-india/", "TCF Canada in India", "All approved centres, fees and the next dates."),
                      ("/en/tcf-canada/score-clb/", "TCF Canada scores and CLB", "CLB 7 is 458 in listening and 453 in reading."),
                      ("/en/tcf-canada-practice-test/", "Free TCF Canada practice test", "Check your level before you pay ₹26,000.")],
                sources="the website of the Alliance Française concerned (TCF pages, schedules, registration form or shop), checked on 8 October 2026.",
                badges={key: _CA}, urls={key: url})


PAGES.append(_india_city(
    "tcf-canada-new-delhi", ["New Delhi"], "New Delhi",
    title="TCF Canada in New Delhi: ₹26,000, test dates, booking",
    desc="TCF Canada at the Alliance Française de Delhi: ₹26,000 including GST, computer-based, the November and December dates, and how booking works.",
    h1="TCF Canada in New Delhi: the Alliance Française de Delhi, the fee and the dates",
    intro="""In New Delhi, the TCF Canada is held by the <strong>Alliance Française de Delhi</strong>, on computer, for
<strong>₹26,000 including GST</strong>. On 8 October 2026, the 14 and 28 October sessions were <strong>full</strong>;
the next dates were <strong>18 and 25 November</strong> (registration 4–11 November, marked “to be confirmed”) and
<strong>16 December</strong> (registration 2–9 December). Seats “often fill within minutes”.""",
    facts=["Alliance Française de Delhi: the <strong>TCF Canada only</strong>, computer-based, <strong>₹26,000</strong> including GST.",
           "8 October 2026: 14 and 28 October <strong>full</strong>; next dates <strong>18 and 25 November</strong> (registration 4–11 November, “to be confirmed”) and <strong>16 December</strong> (registration 2–9 December).",
           "A <strong>valid passport</strong> is required at registration (since January 2026).",
           "Registration opens at 9:30 am online and 9 am at the desk; no refund once registered, unless the Alliance cancels the session.",
           "Results in 2–4 weeks; the results certificate is valid for two years."],
    stats=[("₹26,000", "TCF Canada", "GST included"), ("18 Nov", "next date", "registration 4–11 Nov"),
           ("2–4 weeks", "results", "certificate valid 2 years"), ("{n}", "approved centre", "in New Delhi")],
    sections=[("booking", "Booking the TCF Canada in New Delhi", """<p>The Alliance sells the test itself: an online account or
the front desk, and a seat only counts once it is paid. Register with the passport you will use for your IRCC
application — the Alliance has accepted <strong>only a valid passport</strong> since January 2026. Registration opens at
9:30 am online and 9 am at the desk, and the page warns that seats “often fill within minutes”. Once registered there is
no refund, unless the Alliance cancels the session. Results take two to four weeks. For Express Entry, aim for CLB 7:
458 in listening, 453 in reading. Other cities: <a href="/en/tcf-canada-india/">all TCF Canada centres in India</a>.</p>""")],
    faq=[("Where can I take the TCF Canada in New Delhi?", "At the Alliance Française de Delhi, which holds it on computer for ₹26,000 including GST (8 October 2026)."),
         ("When are the next TCF Canada dates in New Delhi?", "On 8 October 2026: 18 and 25 November (registration 4–11 November, marked “to be confirmed”) and 16 December (registration 2–9 December); the 14 and 28 October sessions were full."),
         ("What do I need to register?", "A valid passport — the only identity document the Alliance has accepted since January 2026 — and the full payment; a seat only counts once it is paid.")],
    key="new-delhi-alliance-francaise", url="https://afdelhi.org/tcf-exams/"))

PAGES.append(_india_city(
    "tcf-canada-kolkata", ["Calcutta"], "Kolkata",
    title="TCF Canada in Kolkata: ₹26,000, Alliance Française, booking",
    desc="TCF Canada in Kolkata at the Alliance Française du Bengale: ₹26,000 incl. GST, computer-based, TCF Québec and tout public fees, booking rules.",
    h1="TCF Canada in Kolkata: the Alliance Française du Bengale, the fees and the rules",
    intro="""In Kolkata, the TCF is held by the <strong>Alliance Française du Bengale</strong>, which offers the TCF Canada,
the TCF Québec, the TCF tout public and the TCF IRN, on computer. On 8 October 2026 the TCF Canada cost
<strong>₹26,000 including GST</strong>; dates are on an external booking calendar, and you must register at least
<strong>15 days</strong> before the test.""",
    facts=["Alliance Française du Bengale: TCF <strong>Canada</strong>, Québec, tout public and IRN, computer-based.",
           "Fees: TCF Canada <strong>₹26,000</strong> incl. GST · TCF Québec ₹6,500 per test · TCF tout public ₹13,000 (+ ₹6,500 per optional test).",
           "Dates on an external booking calendar; register at least <strong>15 days</strong> before the test.",
           "For sessions from January 2027: one postponement of up to 3 months for 50% of the fee (₹13,000).",
           "At least 20 days between two attempts."],
    stats=[("₹26,000", "TCF Canada", "GST included"), ("15 days", "minimum before the test", "to register"),
           ("₹6,500", "TCF Québec", "per test"), ("{n}", "approved centre", "in Kolkata")],
    sections=[("fees", "Fees and booking in Kolkata", """<p>The Alliance Française du Bengale publishes its fees: the
<strong>TCF Canada at ₹26,000</strong> including GST, the <strong>TCF Québec at ₹6,500 per test</strong> — useful if a
Quebec programme only asks for the oral tests — and the TCF tout public at ₹13,000 plus ₹6,500 per optional test. You
book on an external calendar, with an online form that includes payment, at least 15 days before the test. For sessions
from January 2027, one postponement of up to three months is possible for 50% of the fee (₹13,000). Leave at least 20
days between two attempts. Other cities: <a href="/en/tcf-canada-india/">all TCF Canada centres in India</a>.</p>""")],
    faq=[("Where can I take the TCF Canada in Kolkata?", "At the Alliance Française du Bengale, on computer, for ₹26,000 including GST (8 October 2026)."),
         ("How much is the TCF Québec in Kolkata?", "₹6,500 per test at the Alliance Française du Bengale, so you pay only for the tests your Quebec programme requires."),
         ("Can I postpone my TCF in Kolkata?", "For sessions from January 2027, once, by up to three months, for 50% of the fee (₹13,000).")],
    key="calcutta-alliance-francaise-du-bengale", url="https://bengale.afindia.org/tcf/"))

PAGES.append(_india_city(
    "tcf-canada-ahmedabad", ["Ahmedabad"], "Ahmedabad",
    title="TCF Canada in Ahmedabad: Alliance Française, booking",
    desc="TCF Canada at the Alliance Française d’Ahmedabad: computer-based, sessions to be confirmed, an online form then a payment link, results in 15 days.",
    h1="TCF Canada in Ahmedabad: the Alliance Française and how to book",
    intro="""In Ahmedabad, the <strong>Alliance Française d’Ahmedabad</strong> offers the TCF Canada on computer. On 8 October
2026 its page announced “new upcoming sessions to be confirmed” and published no fee. You register with an online form,
then pay through a link sent by email; the certificate comes within 15 working days.""",
    facts=["Alliance Française d’Ahmedabad: the <strong>TCF Canada</strong>, computer-based; the TEF Canada is offered too.",
           "8 October 2026: “new upcoming sessions to be confirmed”; <strong>no fee published</strong>.",
           "Registration: online form, then a payment link by email; no refund once registered.",
           "Certificate within <strong>15 working days</strong>; valid two years for IRCC.",
           "Where the fee is published in India (New Delhi, Kolkata, Bhopal), the TCF Canada costs ₹26,000."],
    stats=[("TBC", "next sessions", "8 Oct 2026"), ("15 days", "certificate", "working days"),
           ("₹26,000", "TCF Canada elsewhere in India", "where published"), ("{n}", "approved centre", "in Ahmedabad")],
    sections=[("booking", "Booking in Ahmedabad", """<p>The Alliance takes registrations through an online form, then sends a
payment link by email; nothing is refunded once you are registered. The test is computer-based and the certificate
comes within 15 working days. With dates still “to be confirmed” on 8 October, check the page before planning your
application — or look at <a href="/en/tcf-canada-new-delhi/">New Delhi</a> and <a href="/en/tcf-canada-bhopal/">Bhopal</a>,
which published dates. The Alliance also offers the <a href="/en/tef-canada/">TEF Canada</a>.</p>""")],
    faq=[("Can I take the TCF Canada in Ahmedabad?", "Yes, at the Alliance Française d’Ahmedabad, on computer. On 8 October 2026 its next sessions were “to be confirmed”."),
         ("How much is the TCF Canada in Ahmedabad?", "The Alliance did not publish its fee on 8 October 2026. Where the fee is published in India — New Delhi, Kolkata, Bhopal — it is ₹26,000."),
         ("How long do results take in Ahmedabad?", "The Alliance issues the certificate within 15 working days.")],
    key="ahmedabad-alliance-francaise", url="https://ahmedabad.afindia.org/tcf/"))

PAGES.append(_india_city(
    "tcf-canada-bangalore", ["Bangalore"], "Bangalore",
    title="TCF Canada in Bangalore: Alliance Française, test dates",
    desc="TCF Canada at the Alliance Française de Bangalore: the 14 November session was full on 8 October 2026; no other date or fee published.",
    h1="TCF Canada in Bangalore: the Alliance Française and its sessions",
    intro="""In Bangalore, the <strong>Alliance Française de Bangalore</strong> offers the TCF Canada. On 8 October 2026 its
<strong>14 November session was full</strong>, and it published no other date and no fee. Leave at least 20 days
between two attempts.""",
    facts=["Alliance Française de Bangalore: the <strong>TCF Canada</strong>.",
           "8 October 2026: the <strong>14 November 2026</strong> session <strong>full</strong>; no other date published.",
           "<strong>No fee published</strong>; where the fee is published in India, the TCF Canada costs ₹26,000.",
           "At least <strong>20 days</strong> between two attempts.",
           "Nearest centres with published dates: New Delhi and Bhopal."],
    stats=[("14 Nov", "session", "full on 8 Oct"), ("20 days", "between attempts", "minimum"),
           ("₹26,000", "TCF Canada elsewhere in India", "where published"), ("{n}", "approved centre", "in Bangalore")],
    sections=[("dates", "Dates and alternatives", """<p>With the 14 November session full and no other date published on
8 October, plan ahead: watch the Alliance’s page, or look at the centres that published dates —
<a href="/en/tcf-canada-new-delhi/">New Delhi</a> (18 and 25 November, 16 December) and
<a href="/en/tcf-canada-bhopal/">Bhopal</a> (4 December, then February and March 2027). Leave at least 20 days between
two attempts.</p>""")],
    faq=[("Can I take the TCF Canada in Bangalore?", "Yes, at the Alliance Française de Bangalore. On 8 October 2026 its 14 November session was full and no other date was published."),
         ("How much is the TCF Canada in Bangalore?", "The Alliance did not publish its fee on 8 October 2026; where it is published in India, it is ₹26,000."),
         ("How long must I wait between two attempts?", "At least 20 days, according to the Alliance Française de Bangalore.")],
    key="bangalore-alliance-francaise", url="https://bangalore.afindia.org/tcf-cannada/"))

PAGES.append(_india_city(
    "tcf-canada-bhopal", ["Bhopal"], "Bhopal",
    title="TCF Canada in Bhopal: ₹26,000, dates to March 2027",
    desc="TCF Canada at the Alliance Française de Bhopal: ₹26,000, paper-based, 4 December 2026 then six dates in February and March 2027, booking rules.",
    h1="TCF Canada in Bhopal: the Alliance Française, the fee and the dates",
    intro="""In Bhopal, the <strong>Alliance Française de Bhopal</strong> holds a paper-based TCF Canada for
<strong>₹26,000</strong>. On 8 October 2026 its next session was <strong>4 December</strong> (one seat left), then
<strong>12, 19, 26 February and 12, 19, 25 March 2027</strong>; registration closes one month before each date.""",
    facts=["Alliance Française de Bhopal: the <strong>TCF Canada</strong>, <strong>paper-based</strong>, <strong>₹26,000</strong>.",
           "8 October 2026: <strong>4 December 2026</strong> (one seat left), then 12, 19, 26 February and 12, 19, 25 March 2027.",
           "Registration closes <strong>one month</strong> before; online shop; scanned photo ID (passport or Aadhaar).",
           "No refund if you arrive late or without your original photo ID.",
           "30 days between two attempts; results in 4–8 weeks."],
    stats=[("₹26,000", "TCF Canada", "paper-based"), ("4 Dec", "next session", "one seat left on 8 Oct"),
           ("4–8 weeks", "results", "certificate valid 2 years"), ("{n}", "approved centre", "in Bhopal")],
    sections=[("booking", "Booking in Bhopal", """<p>You book and pay in the Alliance’s online shop, with a scanned photo ID
(passport or Aadhaar), and registration closes one month before each date. On test day, arriving late or without your
original photo ID means no refund. Leave 30 days between two attempts; results take four to eight weeks. The Alliance
also offers the <a href="/en/tef-canada/">TEF Canada</a>. Other cities:
<a href="/en/tcf-canada-india/">all TCF Canada centres in India</a>.</p>""")],
    faq=[("When is the next TCF Canada in Bhopal?", "On 8 October 2026: 4 December 2026 (one seat left), then 12, 19 and 26 February and 12, 19 and 25 March 2027."),
         ("How much is the TCF Canada in Bhopal?", "₹26,000 at the Alliance Française de Bhopal, paper-based."),
         ("Is the TCF Canada computer-based in Bhopal?", "No: Bhopal runs a paper-based (“Pen & Paper”) TCF Canada.")],
    key="bhopal-alliance-francaise", url="https://bhopal.afindia.org/tcfcanada/"))


# ===========================================================================
# UNITED ARAB EMIRATES (no French equivalent page: no hreflang)
# ===========================================================================
PAGES.append(dict(
    lang="en", variant="en-GB", og_locale="en_AE", fr_path=None, slug="tcf-canada-dubai",
    list_date="8 October 2026", releve_date="8 October 2026", date_label="13 October 2026", modified="2026-10-13",
    country_name="United Arab Emirates", exam="tcf", file="tcf_emirats", layout="cities",
    crumb="TCF Canada in Dubai and Abu Dhabi",
    title="TCF Canada in Dubai and Abu Dhabi: 1,800 AED, dates",
    desc="TCF Canada in the UAE: the Alliance Française de Dubai (two centres) and Abu Dhabi, 1,800 AED, on computer. Next open sessions, deadlines, booking rules.",
    h1="TCF Canada in Dubai and Abu Dhabi: the centres, the fee and the dates",
    intro="""In the United Arab Emirates, {n} centres are approved for the TCF by France Éducation international, and on
8 October 2026 the TCF Canada was offered by the <strong>Alliance Française de Dubai</strong> — at Oud Metha and Dubai
Knowledge Park — and the <strong>Alliance Française Abu Dhabi</strong>: <strong>1,800 AED</strong> everywhere, on
computer. In Dubai, the 20, 21 and 27 October sessions were full and the first open date was <strong>Friday 30
October</strong> (registration until 21 October); in Abu Dhabi, the next session was <strong>Friday 23 October</strong>
(registration until 12 October). The 2026 calendar lists the TCF only at the Abu Dhabi centre, not at Al Ain.""",
    facts=["<strong>{n} approved centres</strong> (FEI list of 8 October 2026); the TCF Canada is held in <strong>Dubai</strong> (Oud Metha, Dubai Knowledge Park) and <strong>Abu Dhabi</strong>; Al Ain is on FEI’s list, but the Alliance’s 2026 calendar doesn’t schedule the TCF there.",
           "Fee: <strong>1,800 AED</strong> in Dubai and in Abu Dhabi (TCF IRN 1,380 AED, TCF tout public 900 AED in Abu Dhabi).",
           "Dubai: 20, 21 and 27 October <strong>full</strong>; nine open sessions from <strong>30 October</strong> to 22 December 2026.",
           "Abu Dhabi: <strong>23 October</strong> (registration until 12 October), 20 November, 16 December.",
           "Computer-based in both cities; in Dubai, no re-marking and no refund once the registration period has closed."],
    stats=[("1,800 AED", "TCF Canada", "Dubai and Abu Dhabi"), ("30 Oct", "first open date in Dubai", "registration until 21 Oct"),
           ("23 Oct", "next date in Abu Dhabi", "registration until 12 Oct"), ("2 years", "validity", "results a few weeks later")],
    sections=[
        ("dubai", "Alliance Française de Dubai: the sessions", table(
            "TCF Canada sessions on the Alliance Française de Dubai booking page on 8 October 2026. OM = Oud Metha (18th Street), DKP = Dubai Knowledge Park (Block 2B).",
            ["Date", "Centre", "Registration until", "Status"],
            [("Tue 20 Oct 2026", "OM", "11 Oct", "<strong>full</strong>"), ("Wed 21 Oct", "DKP", "11 Oct", "<strong>full</strong>"),
             ("Tue 27 Oct", "OM", "18 Oct", "<strong>full</strong>"), ("<strong>Fri 30 Oct</strong>", "OM", "21 Oct", "open"),
             ("Tue 3 Nov", "OM", "25 Oct", "open"), ("Tue 10 Nov", "OM", "1 Nov", "open"), ("Tue 24 Nov", "OM", "15 Nov", "open"),
             ("Wed 25 Nov", "DKP", "15 Nov", "open"), ("Tue 8 Dec", "OM", "29 Nov", "open"), ("Tue 15 Dec", "OM", "6 Dec", "open"),
             ("Wed 16 Dec", "OM", "6 Dec", "open"), ("Tue 22 Dec", "OM", "13 Dec", "open")], wide=False) + """
<p>The Alliance’s PDF calendar (dated 24 September) doesn’t yet show the 30 October session and puts 16 December at
Dubai Knowledge Park: when they differ, the booking page — where you pay — is the one to trust. You book online or at the
offices, during the registration window only; registration is confirmed once you have paid and uploaded a copy of your
passport, and the test-day notice is emailed a week before. Fees are refundable only if you cancel during the
registration period; after it closes, there is no refund or credit, including if you are absent, and re-marking is not
accepted.</p>"""),
        ("abu-dhabi", "Alliance Française Abu Dhabi", """<p>The Alliance Française Abu Dhabi holds the TCF Canada at its
Abu Dhabi centre (Al Bateen), on computer, for <strong>1,800 AED</strong>: <strong>Friday 23 October</strong>
(registration 1 September–12 October), <strong>Friday 20 November</strong> (1 October–9 November) and
<strong>Wednesday 16 December 2026</strong> (15 October–6 December). Its calendar also lists the TCF IRN (1,380 AED) and
the TCF tout public (900 AED). You pick a date and book online; results come “a few weeks later”. The site publishes no
cancellation or re-marking rule. The TCF row of its calendar lists only the Abu Dhabi centre. The dates checked on
18 October 2026: <a href="/en/tcf-canada-abu-dhabi/">TCF Canada in Abu Dhabi</a>.</p>"""),
        ("tef-canada", "TEF Canada in Dubai and Abu Dhabi", """<p>The <a href="/en/tef-canada/">TEF Canada</a> — the
other French test IRCC accepts — is run by Le français des affaires (CCI Paris Île-de-France), not by France Éducation
international, so its centres are not on the list below. On 13 October 2026, the <strong>Alliance Française de
Dubai</strong> listed the TEF Canada among its “accepted tests”, next to the TCF Canada and the TCF Québec, with a booking
button, and the <strong>Alliance Française Abu Dhabi</strong> had a TEF Canada page. Neither page showed a date or a fee
that day, and we did not search the official TEF Canada directory (it shows results only after a search form is submitted): check dates and fees on
the Alliances’ booking pages. Which of the two tests suits you is on our <a href="/en/tcf-vs-tef-canada/">TCF vs TEF
Canada</a> page.</p>"""),
    ],
    list_title="The {n} approved TCF centres in the UAE",
    faq=[("Where can I take the TCF Canada in Dubai?", "At the Alliance Française de Dubai, which holds it at Oud Metha (18th Street) and Dubai Knowledge Park (Block 2B), on computer, for 1,800 AED. On 8 October 2026 the 20, 21 and 27 October sessions were full; the first open session was Friday 30 October, with registration until 21 October."),
         ("How much does the TCF Canada cost in the UAE?", "1,800 AED at the Alliance Française de Dubai and at the Alliance Française Abu Dhabi, as published on 8 October 2026."),
         ("Can I take the TCF Canada in Abu Dhabi or Al Ain?", "In Abu Dhabi, yes: 23 October, 20 November and 16 December 2026 at the Alliance Française Abu Dhabi. Its 2026 calendar doesn’t list the TCF at the Al Ain branch."),
         ("Can I get a refund if I can’t attend?", "In Dubai, only if you cancel during the registration period; after it closes, there is no refund or credit, including if you are absent. Abu Dhabi publishes no rule."),
         ("Is a TCF Canada taken in the UAE accepted by IRCC?", "Yes: the results certificate is issued by France Éducation international whichever approved centre you test at, and it is valid for two years.")],
    also=[("/en/tcf-canada-india/", "TCF Canada in India", "Five Alliances, ₹26,000, the next dates."),
          ("/en/tcf-canada/fees-registration/", "TCF Canada fees and registration", "Fees country by country, and how booking works."),
          ("/en/tcf-canada-practice-test/", "Free TCF Canada practice test", "Measure your level before you pay 1,800 AED.")],
    sources="the websites of the Alliance Française de Dubai (Canada immigration exams page, TCF Canada booking page, September–December 2026 calendar) and of the Alliance Française Abu Dhabi (TCF page, TCF Canada booking page, 2026 exam calendar), checked on 8 October 2026; their TEF Canada pages (afdubai.org Canada immigration exams page, afabudhabi.org/tef/), checked on 13 October 2026.",
    badges={"abou-dhabi-french-ambassy-institut-francais-antenne-afad": _CA,
            "dubai-alliance-francaise-de-dubai-centre-1": _CA, "dubai-alliance-francaise-de-dubai-centre-2": _CA,
            "al-ain-alliance-francais-d-abu-dhabi-antenne-al-ain": [("part", "TCF not listed at Al Ain")]},
    urls={"abou-dhabi-french-ambassy-institut-francais-antenne-afad": "https://www.afabudhabi.org/tcf/",
          "dubai-alliance-francaise-de-dubai-centre-1": "https://www.afdubai.org/canada-immigration-exams-alliance-francaise-dubai/tcf-canada-exam/",
          "dubai-alliance-francaise-de-dubai-centre-2": "https://www.afdubai.org/canada-immigration-exams-alliance-francaise-dubai/tcf-canada-exam/"},
))


# ===========================================================================
# GULF AND LEVANT (13/10/2026) — no French equivalent page; paired with the Arabic pages (pair=…)
# FEI list read on 13 October 2026 (ids: Égypte 116, Liban 106, Arabie saoudite 100) ; centres' websites read the same day.
# ===========================================================================
ME = dict(list_date="13 October 2026", releve_date="13 October 2026", date_label="13 October 2026", published="2026-10-13")

PAGES.append(dict(ME,
    lang="en", variant="en-GB", og_locale="en_SA", fr_path=None, slug="tcf-canada-saudi-arabia",
    country_name="Saudi Arabia", exam="tcf", file="tcf_arabie_saoudite", layout="cities",
    crumb="TCF Canada in Saudi Arabia",
    title="TCF Canada in Saudi Arabia: Jeddah, Riyadh, 1,950 SAR",
    desc="TCF Canada in Saudi Arabia: the Alliance française d’Arabie Saoudite (Al Khobar, Jeddah, Riyadh), 1,950 SAR, the next sessions and the booking rules.",
    h1="TCF Canada in Saudi Arabia: the centres, the fee and the next sessions",
    intro="""Yes, you can take the TCF Canada in Saudi Arabia. On 13 October 2026, France Éducation international listed
{n} approved TCF centres in the country, all run by the <strong>Alliance française d’Arabie Saoudite</strong> (AFAS):
Al Khobar, Jeddah and Riyadh. Its booking platform showed a <strong>TCF Canada in Jeddah on Tuesday 20 October</strong>,
on computer, and an <strong>e-TCF Canada in Riyadh on Thursday 12 November</strong>, already marked “Full” — both at
<strong>1,950 SAR</strong>; the Jeddah listing states “No postponement, no refund, no change of date allowed.”""",
    facts=["<strong>{n} approved TCF centres</strong> (FEI list of 13 October 2026), all Alliance française d’Arabie Saoudite: Al Khobar, Jeddah, Riyadh; computer sessions in Jeddah and Riyadh.",
           "Fee: <strong>1,950 SAR</strong> for the TCF Canada, the e-TCF Canada, the TCF tout public and the e-TEF Canada.",
           "Jeddah: TCF Canada on <strong>Tuesday 20 October 2026</strong>, 10:00 to 15:00, computer-based.",
           "Riyadh: e-TCF Canada on <strong>Thursday 12 November 2026</strong> at the Ar-Rabih venue — <strong>full</strong> on 13 October; registration closes 7 working days before the test.",
           "Jeddah TCF Canada: “No postponement, no refund, no change of date allowed.” We did not find the results delay on the AFAS site or platform."],
    stats=[("{n}", "approved TCF centres", "Al Khobar, Jeddah, Riyadh"), ("1,950 SAR", "TCF Canada", "Jeddah and Riyadh"),
           ("20 Oct", "TCF Canada in Jeddah", "computer-based"), ("12 Nov", "e-TCF Canada in Riyadh", "full on 13 Oct")],
    sections=[
        ("sessions", "The sessions on the AFAS platform", table(
            "French test sessions on the booking platform of the Alliance française d’Arabie Saoudite (afas.extranet-aec.com), read on 13 October 2026. Fees in Saudi riyals.",
            ["Date", "Test", "Venue", "Fee", "Status"],
            [("<strong>Tue 20 Oct 2026</strong>, 10:00–15:00", "<strong>TCF Canada</strong>, computer-based", "Jeddah (Hayy Jameel, Mohammadiyah)", "1,950 SAR", "listed"),
             ("Thu 22 Oct 2026, 10:00–13:00", "TCF tout public", "Jeddah", "1,950 SAR", "listed"),
             ("<strong>Thu 12 Nov 2026</strong>, 13:00–17:30", "<strong>e-TCF Canada</strong>, computer-based", "Riyadh (Ar-Rabih)", "1,950 SAR", "<strong>full</strong>"),
             ("Thu 19 Nov 2026, 12:30–17:30", "e-TEF Canada", "Riyadh (Ar-Rabih)", "1,950 SAR", "<strong>full</strong>")], wide=False) + """
<p>You register online, on the AFAS platform linked from the exams page of
<a href="https://www.af-ksa.org/en/exams/" rel="noopener">af-ksa.org</a>. Read the conditions before paying: the Jeddah TCF Canada
listing states “No postponement, no refund, no change of date allowed”, and for the e-TCF Canada, registration closes
<strong>7 working days before the test date</strong> — earlier if all places are taken. One detail to know: the Ar-Rabih
venue where AFAS schedules its e-TCF and e-TEF Canada sessions in Riyadh is not on France Éducation international’s list,
which gives the AFAS Riyadh centre at Al Kindi Plaza (Gate 14, As-Safarat); ask AFAS if in doubt. No TCF session was
listed for Al Khobar on 13 October.</p>"""),
        ("gulf", "Elsewhere in the Gulf and the Levant", """<p>If the Saudi sessions are full, the nearest TCF Canada
sessions in the Gulf are in <a href="/en/tcf-canada-qatar/">Qatar</a> (Institut français, Doha: 1,300 QAR, 16 December
2026, marked “registration closed” on 26 October) and the <a href="/en/tcf-canada-dubai/">United Arab Emirates</a> (Dubai
and Abu Dhabi, 1,800 AED). In <a href="/en/tcf-canada-kuwait/">Kuwait</a>, the Institut français published no TCF Canada
session on 26 October 2026, only the TEF Canada (130 KD); in <a href="/en/tcf-canada-jordan/">Jordan</a>, the Institut
français in Amman holds three TCF Canada sessions a year. Bahrain has one approved TCF centre (Alliance française, Isa
Town), whose website did not open on 26 October; Oman has none, but the Centre franco-omanais in Muscat had TEF Canada
sessions on the CCI Paris centre map that day. See also <a href="/en/tcf-canada-egypt/">Egypt</a> and
<a href="/en/tcf-canada-lebanon/">Lebanon</a>.</p>"""),
    ],
    list_title="The {n} approved TCF centres in Saudi Arabia",
    faq=[("Can I take the TCF Canada in Saudi Arabia?", "Yes. The Alliance française d’Arabie Saoudite runs it: on 13 October 2026 its platform listed a TCF Canada in Jeddah on Tuesday 20 October (computer-based) and an e-TCF Canada in Riyadh on Thursday 12 November, which was already full."),
         ("How much does the TCF Canada cost in Saudi Arabia?", "1,950 SAR, as published on the AFAS booking platform on 13 October 2026 — the same fee as the TCF tout public and the e-TEF Canada."),
         ("Can I get a refund or change my date?", "Not for the Jeddah TCF Canada: its listing states “No postponement, no refund, no change of date allowed.” For the e-TCF Canada, registration closes 7 working days before the test."),
         ("Is the TEF Canada available in Saudi Arabia?", "AFAS listed an e-TEF Canada in Riyadh on Thursday 19 November 2026, at 1,950 SAR; it was full on 13 October."),
         ("Is a TCF Canada taken in Saudi Arabia accepted by IRCC?", "Yes: the results certificate is issued by France Éducation international whichever approved centre you test at, and it is valid for two years.")],
    also=[("/en/tcf-canada-dubai/", "TCF Canada in Dubai and Abu Dhabi", "Four centres, 1,800 AED."),
          ("/en/tcf-canada/fees-registration/", "TCF Canada fees and registration", "Fees country by country, and how booking works."),
          ("/en/tcf-canada-practice-test/", "Free TCF Canada practice test", "Measure your level before you pay 1,950 SAR.")],
    sources="the website of the Alliance française d’Arabie Saoudite (af-ksa.org, exams page) and its booking platform afas.extranet-aec.com (TCF, TCF Canada, e-TCF Canada and e-TEF Canada sessions), checked on 13 October 2026.",
    badges={"djeddah-alliance-francaise": _CA,
            "riyadh-alliance-francaise-d-arabie-saoudite": [("ok", "e-TCF Canada (Ar-Rabih)"), ("part", "12 Nov full")],
            "al-khobar-alliance-francaise-d-arabie-saoudite": [("part", "no TCF session listed")]},
    urls={"djeddah-alliance-francaise": "https://www.af-ksa.org/en/exams/",
          "riyadh-alliance-francaise-d-arabie-saoudite": "https://www.af-ksa.org/en/exams/",
          "al-khobar-alliance-francaise-d-arabie-saoudite": "https://www.af-ksa.org/en/exams/"},
))

PAGES.append(dict(ME,
    lang="en", variant="en-GB", og_locale="en_EG", fr_path=None, slug="tcf-canada-egypt",
    date_label="26 October 2026", modified="2026-10-26",   # 2026 calendar and fee read on 26/10/2026 (FEI list unchanged)
    country_name="Egypt", exam="tcf", file="tcf_egypte_v2", layout="cities",
    crumb="TCF Canada in Egypt",
    title="TCF Canada in Egypt: Cairo, 8 Dec 2026, register 2–12 Nov",
    desc="TCF Canada in Egypt: Institut français d’Égypte, Cairo (Mounira), 8 December 2026, registration 2–12 November; how the fee in Egyptian pounds is set.",
    h1="TCF Canada in Egypt: the Institut français centres and the next session",
    intro="""In Egypt, France Éducation international lists {n} approved TCF centres, all part of the <strong>Institut
français d’Égypte</strong>: Cairo (Mounira and Heliopolis) and Alexandria. Its 2026 TCF calendar, read on 26 October
2026, gives the next TCF Canada at Mounira on <strong>Tuesday 8 December 2026</strong>, with registration from
<strong>2 to 12 November</strong>. It gives no fee: the institute’s last published fee list (2024) set the TCF Canada at the
equivalent of €250, paid in Egyptian pounds at the exchange rate of the month you pay. Results come in about four weeks.""",
    facts=["<strong>{n} approved TCF centres</strong> (FEI list of 13 October 2026): Cairo – Mounira, Cairo – Heliopolis, Alexandria; computer sessions at Mounira and Alexandria.",
           "TCF Canada: next session <strong>Tuesday 8 December 2026</strong> at Mounira; registration <strong>2 to 12 November 2026</strong> (2026 calendar, read on 26 October).",
           "Fee: <strong>not published for 2026</strong> — the 2026 “Dates et tarifs du TCF” calendar lists dates only; the 2024 fee list said the equivalent of <strong>€250</strong>, paid in Egyptian pounds.",
           "Registration: an online form for each version, a copy of your passport, payment, then your exam invitation by email.",
           "Results in about <strong>4 weeks</strong>; <strong>30 days</strong> between two TCF attempts."],
    stats=[("{n}", "approved TCF centres", "Cairo and Alexandria"), ("8 Dec", "next TCF Canada session", "registration 2–12 Nov 2026"),
           ("~4 weeks", "results", "Institut français d’Égypte"), ("30 days", "between two attempts", "TCF")],
    sections=[
        ("sessions", "The TCF Canada at the Institut français d’Égypte", table(
            "TCF Canada sessions in the Institut français d’Égypte’s 2026 TCF calendar (“Calendrier TCF 2026 – IF Mounira”, PDF dated 4 February 2026), read on 26 October 2026.",
            ["Session", "Registration", "Status on 26 October 2026"],
            [("Tue 10 Feb 2026", "5–15 Jan", "past"), ("Tue 5 May 2026", "5–16 Apr", "past"),
             ("Tue 21 Jul 2026", "1–11 Jun", "past"), ("Tue 22 Sep 2026", "9–20 Aug", "past"),
             ("<strong>Tue 8 Dec 2026</strong>", "<strong>2–12 Nov</strong>", "next session")], wide=False) + """
<p>The Institut français d’Égypte publishes its sessions for all its centres on one page, with a link to its 2026 TCF
calendar (<a href="https://www.ifegypte.com/wp-content/uploads/2026/02/Calendrier-TCF-2026-IF-Mounira-VF-04.02.2026.pdf" rel="noopener">“Dates et tarifs du TCF”, PDF</a>). On 26 October 2026 the page
still said that TCF Canada registration was closed and that the next session was in December; the calendar gives the
date — <strong>Tuesday 8 December 2026</strong>, at the Mounira centre in Cairo — and the registration period,
<strong>2 to 12 November 2026</strong>. Despite its title, it gives no fee.</p>

<p>Which centre runs it? The Mounira centre in Cairo has published TCF Canada results for past sessions; the TCF Canada
results sections of Alexandria and Heliopolis were empty on 13 October, so we have not confirmed that they hold the TCF
Canada. You register with an online form for the version you want, then send a copy of your passport and pay; your exam
invitation arrives by email. Results come “within about 4 weeks” of the test, and you must wait 30 days between two
TCF attempts. The institute also offers the e-TEF Canada: its own 2026 calendar lists 10 February, 30 April and
22 October, yet on 26 October 2026 the TEF centre map of Le français des affaires (CCI Paris) still showed TEF Canada
sessions for the Cairo institute — check the next date with the institute.</p>"""),
        ("fee", "The fee in Egyptian pounds", """<p>The Institut français d’Égypte has not published its 2026 TCF fees: the
2026 calendar lists dates only, and no web page gives a price. The last fee list it published, in its 2024 TCF flyer, set
the TCF Canada at the <strong>equivalent of €250</strong> (the TCF tout public at €200, the TCF IRN at €175), paid in
<strong>Egyptian pounds at the exchange rate of the month of payment</strong>, rounded up. So the amount in pounds is not
fixed: it follows the euro rate of the month you pay, and the 2026 base may differ from 2024’s. Ask the institute for
the exact amount when registration opens on 2 November, before you pay.</p>"""),
    ],
    list_title="The {n} approved TCF centres in Egypt",
    faq=[("Where can I take the TCF Canada in Egypt?", "At the Institut français d’Égypte. FEI lists three approved TCF centres (Cairo – Mounira, Cairo – Heliopolis, Alexandria); Mounira has published TCF Canada results, while the TCF Canada results sections of the other two were empty on 13 October 2026."),
         ("When is the next TCF Canada session in Egypt?", "Tuesday 8 December 2026, at the Mounira centre in Cairo; registration runs from 2 to 12 November 2026 (the Institut français d’Égypte’s 2026 TCF calendar, read on 26 October 2026)."),
         ("How much does the TCF Canada cost in Egypt, in Egyptian pounds?", "The 2026 fee is not published: the 2026 calendar lists dates only. The institute’s last fee list (2024) set the TCF Canada at the equivalent of €250, paid in Egyptian pounds at the exchange rate of the month of payment, rounded up — so the amount in pounds changes from month to month. Ask the institute before paying."),
         ("How do I register?", "With the online form for the TCF Canada, a copy of your passport and the payment; your exam invitation is then sent by email."),
         ("How long do results take?", "About four weeks after the test, according to the institute’s FAQ. The results certificate is valid for two years for IRCC.")],
    also=[("/en/tcf-canada-lebanon/", "TCF Canada in Lebanon", "Six Institut français centres."),
          ("/en/tcf-canada-saudi-arabia/", "TCF Canada in Saudi Arabia", "Jeddah and Riyadh, 1,950 SAR."),
          ("/en/tcf-canada-practice-test/", "Free TCF Canada practice test", "Check your level before the December session.")],
    sources="the website of the Institut français d’Égypte (ifegypte.com: upcoming sessions, exam results by centre, FAQ), checked on 13 October 2026; its 2026 TCF and TEF calendars (PDF, dated 4 February 2026) and its 2024 TCF flyer (fees), read on 26 October 2026.",
    badges={"le-caire-institut-francais-d-egypte": _CA,
            "le-caire-heliopolis-institut-francais": [("part", "TCF Canada not confirmed")],
            "alexandrie-institut-francais-d-egypte-a-alexandrie": [("part", "TCF Canada not confirmed")]},
    urls={k: "https://www.ifegypte.com/prochaines-sessions/" for k in
          ("le-caire-institut-francais-d-egypte", "le-caire-heliopolis-institut-francais", "alexandrie-institut-francais-d-egypte-a-alexandrie")},
))

PAGES.append(dict(ME,
    lang="en", variant="en-GB", og_locale="en_LB", fr_path=None, slug="tcf-canada-lebanon",
    country_name="Lebanon", exam="tcf", file="tcf_liban_v2", layout="cities",
    crumb="TCF Canada in Lebanon",
    title="TCF Canada in Lebanon: six Institut français centres",
    desc="TCF Canada in Lebanon: the six Institut français du Liban centres (Beirut, Deir El Kamar, Jounieh, Saida, Tripoli, Zahlé), results delay and contacts.",
    h1="TCF Canada in Lebanon: the six Institut français centres",
    intro="""In Lebanon, the TCF is run by the <strong>Institut français du Liban</strong>, and France Éducation
international lists {n} approved centres: Beirut, Deir El Kamar, Jounieh, Saida, Tripoli and Zahlé. On 13 October 2026,
each of their exam pages named the <strong>TCF Canada</strong> among the versions offered, “as part of the Canadian immigration
process”. Session dates are only in PDF calendars, and no fee is published as text; results arrive about six weeks after
the test.""",
    facts=["<strong>{n} approved centres</strong> (FEI list of 13 October 2026), all Institut français du Liban; computer sessions in Beirut, Deir El Kamar and Tripoli.",
           "The <strong>TCF Canada</strong> is listed on all six exam pages, with the TCF tout public, the TCF Québec and the TCF IRN.",
           "Results in about <strong>6 weeks</strong>; the certificate is collected in person at the Institut.",
           "Dates: in PDF calendars only (Beirut, Jounieh and Saida for 2026; Zahlé’s is the 2024 one; none linked for Deir El Kamar and Tripoli); no fee published as text.",
           "The results certificate is valid for two years for IRCC."],
    stats=[("{n}", "centres", "TCF Canada listed at each"), ("3", "with computer sessions", "Beirut, Deir El Kamar, Tripoli"),
           ("~6 weeks", "results", "collected in person"), ("2 years", "validity", "for IRCC")],
    sections=[
        ("centres", "What the Institut français du Liban publishes", """<p>Each of the six centres has its own exam page on
institutfrancais-liban.com, with the same TCF text: the TCF tout public, the TCF Québec, the <strong>TCF Canada</strong>
— “as part of the Canadian immigration process” — and the TCF IRN. The results are sent “about 6 weeks after
the exams”, and the certificate is collected in person at the Institut.</p>

<p>The calendars, however, are PDFs: Beirut, Jounieh and the South (Saida) link a 2026 TCF calendar, Zahlé still links
its 2024 one, and Deir El Kamar and Tripoli link none. The pages don’t say how to register or by when, and publish no
fee as text — so contact your centre (Beirut gives 01 420 272/3 on its page) before planning your application. If you
prefer the other test IRCC accepts, see <a href="/en/tcf-vs-tef-canada/">TCF vs TEF Canada</a>.</p>"""),
    ],
    list_title="The {n} approved TCF centres in Lebanon",
    faq=[("Where can I take the TCF Canada in Lebanon?", "At the Institut français du Liban, in any of its six approved centres: Beirut, Deir El Kamar, Jounieh, Saida, Tripoli and Zahlé. All six exam pages listed the TCF Canada on 13 October 2026."),
         ("How much does the TCF Canada cost in Lebanon?", "The Institut français du Liban doesn’t publish its TCF fees as text on its exam pages; ask your centre (Beirut: 01 420 272/3)."),
         ("Is the TCF Canada computer-based in Lebanon?", "FEI’s list shows computer sessions in Beirut, Deir El Kamar and Tripoli; the other three centres don’t declare that option."),
         ("How long do results take?", "About six weeks after the test; the certificate is collected in person at the Institut français du Liban.")],
    also=[("/en/tcf-canada-egypt/", "TCF Canada in Egypt", "Institut français d’Égypte, next session December 2026."),
          ("/en/tcf-canada-dubai/", "TCF Canada in Dubai and Abu Dhabi", "Four centres, 1,800 AED."),
          ("/en/tcf-canada/score-clb/", "TCF Canada scores and CLB", "The calculator and IRCC’s table.")],
    sources="the exam pages of the six Institut français du Liban centres (institutfrancais-liban.com/examens/…), checked on 13 October 2026.",
    badges={k: _CA for k in ("beyrouth-institut-francais-du-liban", "deir-el-kamar-institut-francais", "jounieh-institut-francais",
                              "saida-institut-francais", "tripoli-institut-francais", "zahle-institut-francais")},
    urls={"beyrouth-institut-francais-du-liban": "https://institutfrancais-liban.com/examens/beyrouth/",
          "deir-el-kamar-institut-francais": "https://institutfrancais-liban.com/examens/deir-el-qamar/",
          "jounieh-institut-francais": "https://institutfrancais-liban.com/examens/jounieh/",
          "saida-institut-francais": "https://institutfrancais-liban.com/examens/sud/",
          "tripoli-institut-francais": "https://institutfrancais-liban.com/examens/tripoli/",
          "zahle-institut-francais": "https://institutfrancais-liban.com/examens/baalbeck-zahle/"},
))

PAGES.append(dict(ME,
    lang="en", variant="en-GB", og_locale="en_AE", fr_path=None, slug="delf-dubai",
    country_name="United Arab Emirates", exam="delf", file="delf_emirats", layout="cities",
    crumb="DELF in Dubai and Abu Dhabi",
    title="DELF in Dubai: 11 December 2026 session, DELF B2 680 AED",
    desc="DELF and DALF in the UAE: the Alliance Française de Dubai’s 11 December 2026 session (B2 680 AED, C1 875 AED), the other approved centres, how to register.",
    h1="DELF and DALF in Dubai and Abu Dhabi: the centres, the next session and the fees",
    intro="""In the United Arab Emirates, France Éducation international lists {n} approved DELF-DALF centres —
the Alliances Françaises of Dubai, Abu Dhabi and Sharjah and the Institut français des Émirats arabes unis — under a
central body in Abu Dhabi. On 13 October 2026, the <strong>Alliance Française de Dubai</strong> published its next adult
session: <strong>Friday 11 December 2026</strong>, at <strong>560 AED</strong> for A1 and A2, <strong>680 AED</strong>
for B1 and B2 and <strong>875 AED</strong> for C1 and C2, with online registration. We found no adult date or fee on the
other centres’ web pages that day.""",
    facts=["<strong>{n} approved centres</strong> (FEI list of 13 October 2026): Alliance Française de Dubai, Alliance Française d’Abu Dhabi, Institut français des Émirats arabes unis (Abu Dhabi), Alliance Française de Sharjah.",
           "Dubai, adults: <strong>Friday 11 December 2026</strong> — DELF A1 and A2 <strong>560 AED</strong>, DELF B1 and B2 <strong>680 AED</strong>, DALF C1 and C2 <strong>875 AED</strong>.",
           "Registration online in Dubai (form and passport copy, first come, first served); fees non-refundable once registration has closed.",
           "Alliance Française d’Abu Dhabi: DELF-DALF for adults, DELF Junior and DELF Prim; dates and fees in a PDF calendar only. No 2027 session published.",
           "A DELF or DALF diploma is valid for life — but it is not accepted by IRCC for Express Entry (TCF Canada or TEF Canada only)."],
    stats=[("{n}", "approved centres", "Dubai, Abu Dhabi, Sharjah"), ("11 Dec", "next adult session in Dubai", "2026"),
           ("680 AED", "DELF B2 in Dubai", "560 AED for A1–A2"), ("875 AED", "DALF C1 or C2", "Dubai")],
    sections=[
        ("dubai", "The Alliance Française de Dubai session", table(
            "DELF-DALF adult session on the Alliance Française de Dubai website, read on 13 October 2026 (Oud Metha, 18th Street). Fees in UAE dirhams.",
            ["Exam", "Fee", "Session"],
            [("DELF A1", "560 AED", "Fri 11 Dec 2026"), ("DELF A2", "560 AED", "Fri 11 Dec 2026"),
             ("DELF B1", "680 AED", "Fri 11 Dec 2026"), ("<strong>DELF B2</strong>", "<strong>680 AED</strong>", "Fri 11 Dec 2026"),
             ("DALF C1", "875 AED", "Fri 11 Dec 2026"), ("DALF C2", "875 AED", "Fri 11 Dec 2026")], wide=False) + """
<p>The session is for adults only; you register online with the form and a copy of your passport, places are allocated
first come, first served, and fees are not refundable once registration has closed. The DELF Prim and DELF Junior have
their own pages. The written and spoken tests follow the official format: see our pages on the
<a href="/en/delf-b2/">DELF B2</a>, the <a href="/en/delf-b1/">DELF B1</a> and the <a href="/en/dalf-c1/">DALF C1</a>.</p>"""),
        ("abu-dhabi", "Abu Dhabi and Sharjah", """<p>The <strong>Alliance Française d’Abu Dhabi</strong> offers the DELF-DALF for
adults, the DELF Junior and the DELF Prim (“register online or at our center”), but its dates and fees are only in a PDF
calendar — the 180 AED shown on its page is a preparation kit, not an exam fee. The <strong>Institut français des Émirats
arabes unis</strong> published only DELF Junior pages, and the <strong>Alliance Française de Sharjah</strong> has no
website on FEI’s list. The central body’s website on that list did not open on 13 October.</p>

<p><strong>For Express Entry, the DELF won’t do.</strong> IRCC accepts only the TCF Canada and the TEF Canada: see <a href="/en/tcf-canada-dubai/">TCF Canada in Dubai and Abu Dhabi</a>.</p>"""),
    ],
    list_title="The {n} approved DELF-DALF centres in the UAE",
    faq=[("When is the next DELF session in Dubai?", "Friday 11 December 2026 for adults at the Alliance Française de Dubai (Oud Metha), as published on 13 October 2026 and unchanged on 26 October 2026, when the Alliance described the exam as for adults aged 18 and above. No 2027 date had been published by then; for other countries, see <a href=\"/en/delf-exam-dates-2027/#by-country\">DELF exam dates 2027 by country</a>."),
         ("How much does the DELF B2 cost in Dubai?", "680 AED at the Alliance Française de Dubai (13 October 2026); DELF B1 is also 680 AED, A1 and A2 560 AED, DALF C1 and C2 875 AED."),
         ("Where can I take the DELF in Abu Dhabi?", "At the Alliance Française d’Abu Dhabi or the Institut français des Émirats arabes unis, both approved by FEI (on 13 October 2026 the Institut’s website showed only the DELF Junior). That day, the Alliance’s dates and fees were only in a PDF calendar."),
         ("Can I use a DELF for Canadian immigration?", "No: for Express Entry, IRCC accepts only the TCF Canada and the TEF Canada. The DELF is valid for life and is accepted by French universities, for French residence and citizenship applications and, under certain conditions, for Quebec.")],
    also=[("/en/tcf-canada-dubai/", "TCF Canada in Dubai and Abu Dhabi", "Four centres, 1,800 AED."),
          ("/en/delf-b2/", "DELF B2 exam", "Format, scoring and preparation."),
          ("/en/delf-b2-practice-test/", "DELF B2 practice test", "One exercise per section, with answers.")],
    sources="the websites of the Alliance Française de Dubai (DELF-DALF exam page) and of the Alliance Française d’Abu Dhabi (DELF-DALF page), and the Institut français des Émirats arabes unis, checked on 13 October 2026; the Alliance Française de Dubai’s DELF-DALF page again on 26 October 2026 (same session and fees, still no 2027 date).",
    org_url="",
    urls={"dubai-alliance-francaise-dubai": "https://www.afdubai.org/french-diplomas-exams-learning-french-with-alliance-francaise-dubai/delf-dalf-exam/",
          "abu-dhabi-alliance-francaise-d-abu-dhabi": "https://www.afabudhabi.org/delf-dalf/"},
))


# ===========================================================================
# /en/ — landing page (make_pays.hub("en")). Figures taken from each country page.
# ===========================================================================
def _hub_table():
    from pays_i18n import table
    fei_ca_delf = "https://www.france-education-international.fr/centres-d-examen/liste?pays=112&type-centre=delf_dalf"
    rows = [("Canada", '<a href="/en/tcf-canada-test-centres/">48 centres, $390 to $452</a> — <a href="/en/tcf-canada-toronto/">Toronto</a>, '
                       '<a href="/en/tcf-canada-montreal/">Montreal</a>, <a href="/en/tcf-canada-vancouver/">Vancouver</a>, '
                       '<a href="/en/tcf-canada-ottawa/">Ottawa</a>, <a href="/en/tcf-canada-quebec-city/">Quebec City</a>, '
                       '<a href="/en/tcf-canada-calgary/">Calgary</a>, <a href="/en/tcf-canada-edmonton/">Edmonton</a>, '
                       '<a href="/en/tcf-canada-halifax/">Halifax</a>, <a href="/en/tcf-canada-winnipeg/">Winnipeg</a>; provinces: '
                       '<a href="/en/tcf-canada-ontario/">Ontario</a>, <a href="/en/tcf-canada-alberta/">Alberta</a>, '
                       '<a href="/en/tcf-canada-new-brunswick/">New Brunswick</a>',
             f'<a href="{fei_ca_delf}" rel="noopener">FEI’s official list</a>'),
            ("United States", '<a href="/en/tcf-canada-usa/">12 of 18 centres, US$330 to US$505</a> — <a href="/en/tcf-canada-new-york/">New York</a>, '
                              '<a href="/en/tcf-canada-boston/">Boston</a>, <a href="/en/tcf-canada-chicago/">Chicago</a>, '
                              '<a href="/en/tcf-canada-los-angeles/">Los Angeles</a>, <a href="/en/tcf-canada-san-diego/">San Diego</a>, '
                              '<a href="/en/tcf-canada-san-francisco/">San Francisco</a>, <a href="/en/tcf-canada-seattle/">Seattle</a>, '
                              '<a href="/en/tcf-canada-detroit/">Detroit</a>, <a href="/en/tcf-canada-houston/">Houston</a>, '
                              '<a href="/en/tcf-canada-denver/">Denver</a>',
             '<a href="/en/delf-usa/">40 centres, B2 US$190</a>'),
            ("United Kingdom", '<a href="/en/tcf-canada-uk/">London £260, Glasgow £325</a>', '<a href="/en/delf-uk/">11 centres, B2 £160</a>'),
            ("India", '<a href="/en/tcf-canada-india/">5 Alliances, ₹26,000</a>', "—"),
            ("United Arab Emirates", '<a href="/en/tcf-canada-dubai/">Dubai and Abu Dhabi, 1,800 AED</a> — <a href="/en/tcf-canada-abu-dhabi/">Abu Dhabi</a>', '<a href="/en/delf-dubai/">Dubai 11 Dec, B2 680 AED</a>'),
            ("Saudi Arabia", '<a href="/en/tcf-canada-saudi-arabia/">Jeddah and Riyadh, 1,950 SAR</a>', "—"),
            ("Egypt", '<a href="/en/tcf-canada-egypt/">Institut français d’Égypte, Cairo 8 Dec 2026</a>', "—"),
            ("Lebanon", '<a href="/en/tcf-canada-lebanon/">6 Institut français centres</a>', "—"),
            ("Qatar", '<a href="/en/tcf-canada-qatar/">Doha, 1,300 QAR</a>', "—"),
            ("Jordan", '<a href="/en/tcf-canada-jordan/">Amman, 3 sessions a year</a>', "—"),
            ("Kuwait", '<a href="/en/tcf-canada-kuwait/">no TCF Canada listed; TEF Canada 130 KD</a>', "—")]
    return table("The TCF Canada and the DELF-DALF, from each centre’s website (Canada: 17 September 2026; United States, "
                 "United Kingdom, India and the UAE TCF: 8 October 2026; UAE DELF, Saudi Arabia, Egypt, Lebanon: 13 October 2026; the US, Alberta and Abu Dhabi city pages: 18 October 2026; Qatar, Jordan, Kuwait and Egypt’s 2026 calendar, the North American city and province pages: 26 October 2026). "
                 "Fees in local currency, for an individual candidate.",
                 ["Country", "TCF Canada", "DELF · DALF"], [(f"<strong>{p}</strong>", a, b) for p, a, b in rows], wide=False)


HUB = dict(
    variant="en-CA", accent="accent-tcf", crumb="Test centres", read=3,
    title="TCF Canada & DELF test centres: Canada, USA, UK (2026)",
    desc="Where to take the TCF Canada or the DELF in Canada, the United States and the United Kingdom: approved test centres, fees and dates, checked in 2026.",
    h1="TCF Canada and DELF test centres in Canada, the US and the UK",
    lang_links='<p class="langs"><a href="/es/" hreflang="es" lang="es">En español</a> · <a href="/centres/" hreflang="fr" lang="fr">En français</a> · <a href="/ar/" hreflang="ar" lang="ar" dir="rtl">بالعربية</a></p>',
    intro="""For the <strong>TCF Canada</strong> — one of the two French tests IRCC accepts — and for the
<strong>DELF</strong> and <strong>DALF</strong> diplomas, each page lists the test centres approved by France
Éducation international in one country or city, what each centre’s website showed when we checked — fees, dates,
versions — and how to register. Canada: all 48 centres, plus Toronto, Montreal, Vancouver, Ottawa, Quebec City,
Calgary, Edmonton, Halifax and Winnipeg, and Ontario, Alberta and New Brunswick province by province. The United
States — with New York, Boston, Chicago, Detroit, Houston, Denver, Seattle, San Francisco, Los Angeles and San Diego —
and the United Kingdom: the TCF Canada and the DELF.""",
    facts=["<strong>Canada: 48 approved TCF centres</strong> in nine provinces and Nunavut (FEI list of 26 October 2026); fees seen: $390 (Alliance française, Vancouver), $400 (Alliance française, Edmonton), $440 (UQTR).",
           "⚠️ Sessions in Toronto and Vancouver <strong>fill up within minutes</strong>: register the moment bookings open.",
           "Seats on 26 October 2026: <a href=\"/en/tcf-canada-new-brunswick/\">New Brunswick</a> ($390, weekends to 20 December and Moncton from 1 December) and <a href=\"/en/tcf-canada-ottawa/\">Ottawa</a> ($400, 10 November); <a href=\"/en/tcf-canada-toronto/\">Toronto</a> opens January–March 2027 on 1 December at 10 am.",
           "<strong>United States</strong>: 12 of the 18 approved TCF centres offer the TCF Canada, for US$330 to US$505 (8 and 18 October 2026).",
           "<strong>United Kingdom</strong>: the TCF Canada at the Institut français in London (£260) and the Alliance française de Glasgow (£325); when we checked on 8 October 2026, the earliest free seat in London was on 23 April 2027.",
           "<strong>India</strong>: 5 Alliances Françaises offer the TCF Canada (₹26,000 where published); <strong>UAE</strong>: Dubai and Abu Dhabi, 1,800 AED; <strong>Saudi Arabia</strong>: Jeddah and Riyadh, 1,950 SAR; Egypt and Lebanon: Institut français centres.",
           "A DELF or DALF diploma is valid for life; TCF Canada results, for two years."],
    toc=[("countries", "Where to take the exams"), ("prepare", "Prepare for the TCF Canada"), ("tcf-canada", "TCF Canada"),
         ("delf", "DELF and DALF"), ("france", "Living in France")],
    body="""
<div class="stats">
<div class="stat"><b>48</b><span>TCF centres in Canada</span><em>nine provinces and Nunavut</em></div>
<div class="stat"><b>12 of 18</b><span>US centres</span><em>offer the TCF Canada</em></div>
<div class="stat"><b>£260</b><span>TCF Canada in London</span><em>earliest free seat: 23 April 2027</em></div>
</div>

<form class="finder-mini" action="/en/test-centre-near-me/" method="get" role="search">
<label for="finder-mini-q">Find a test centre near you</label>
<div class="finder-row"><input id="finder-mini-q" name="q" type="search" placeholder="City, country or centre name" autocomplete="off" enterkeyhint="search"><button type="submit">Search</button></div>
<p>TCF, DELF-DALF and TEF: the nearest approved centres, with the distance. <a href="/en/test-centre-near-me/">Or use your location →</a></p>
</form>

<h2 id="countries">Where to take the exams</h2>
""" + _hub_table() + """

<h2 id="prepare">Prepare for the TCF Canada</h2>
<p>The guides behind the scores: what each of the four tests looks like, how scores convert to CLB levels, and practice
material in the official format.</p>
<ul class="posts">
<li><a href="/en/tcf-canada/">The TCF Canada exam</a><p>What it is, who it is for, the four tests and the CLB levels IRCC reads.</p></li>
<li><a href="/en/tcf-canada/score-clb/">Score chart and CLB calculator</a><p>CLB 7 is 458 in listening, 453 in reading, 10/20 in speaking and writing.</p></li>
<li><a href="/en/tcf-canada-practice-test/">Free TCF Canada practice test</a><p>Measure your level on the real format before you book.</p></li>
<li><a href="/en/tcf-canada-writing-tasks/">Writing tasks 1, 2 and 3</a><p>Word limits, sample topics and how to split the 60 minutes.</p></li>
<li><a href="/en/tcf-canada-speaking-topics/">Speaking topics</a><p>The three tasks in 12 minutes.</p></li>
<li><a href="/en/tcf-vs-tef-canada/">TCF vs TEF Canada</a><p>The two French tests IRCC accepts, side by side.</p></li>
<li><a href="/en/tef-canada/">TEF Canada</a><p>The other test: format, scoring and CLB levels.</p></li>
<li><a href="/en/tcf-quebec/">TCF Québec</a><p>The modular test for Quebec immigration, compared with the TCF Canada.</p></li>
</ul>

<h2 id="tcf-canada">TCF Canada: before you register</h2>
<p>The TCF Canada is a <strong>test</strong>, not a diploma: there is no pass or fail — it places your level in each
section, and IRCC converts the result into NCLC (CLB) levels. The results certificate is issued by France Éducation
international, whichever centre you test at, and is valid for two years. Two things to know before you pay:
<strong>a centre approved for the TCF doesn’t necessarily offer the Canada version</strong> — each page shows which
centres advertised it on their website — and seats are scarce in the big cities. IRCC also accepts the TEF Canada.</p>

<h2 id="delf">DELF and DALF: the diploma</h2>
<p>The DELF (A1 to B2) and the DALF (C1, C2) are official <strong>diplomas</strong> of the French Ministry of
Education: you pass them level by level, and they are valid for life. In each country, a central management body
sets the session calendar, and you register directly with a centre — an Alliance française, an Institut français, a
university. Guides: <a href="/en/delf-b2/">DELF B2 exam</a> · <a href="/en/delf-b1/">DELF B1</a> ·
<a href="/en/dalf-c1/">DALF C1</a> · <a href="/en/delf-b2-practice-test/">DELF B2 practice test</a>. Centres:
<a href="/en/delf-usa/">DELF in the USA</a> · <a href="/en/delf-uk/">DELF in the UK</a>.</p>

<h2 id="france">Living in France: residence and citizenship</h2>
<p>Since 2026, French citizenship requires B2 in French, and the resident card B1. What the rules ask for, and the
tests that prove it: <a href="/en/french-citizenship-b2/">French citizenship language requirement: B2</a> ·
<a href="/en/tcf-irn/">TCF IRN</a>.</p>

<p>Spain and Latin America, in Spanish: <a href="/es/" lang="es">TCF Canada y DELF en español</a>.</p>
""",
    faq=[("Where can I take the TCF Canada in Canada?", "At one of the 48 centres approved by France Éducation international, in nine provinces and Nunavut — 23 in Quebec (7 in Montreal), 8 in Ontario, 5 in British Columbia, 3 in Alberta. Sessions in Toronto and Vancouver fill up within minutes: register the moment bookings open."),
         ("How much does the TCF Canada cost?", "There is no national fee. In Canada: $390 in Vancouver, Toronto, Moncton and at the CCNB, $400 in Ottawa, Calgary, Edmonton, Halifax and Winnipeg, $440 at UQTR, $452 at GB Language Centre (26 October 2026; UQTR 17 September). In the United States: US$330 to US$505. In the United Kingdom: £260 in London, £325 in Glasgow. All countries: <a href=\"/en/tcf-canada/fees-registration/\">TCF Canada fees 2026</a>."),
         ("TCF Canada or DELF: which one do I need?", "For Canadian immigration, IRCC accepts two French tests: the TCF Canada and the TEF Canada, with results valid for two years. The DELF and DALF are diplomas, passed level by level and valid for life."),
         ("Can I take the TCF Canada at any TCF centre?", "No: a centre approved for the TCF doesn’t necessarily offer the Canada version — in the United States, Atlanta, Chicago, Seattle and Washington don’t. Each page shows which centres advertised it on their website.")],
    also=[("/es/", "TCF Canada y DELF en español", "Spain and Latin America: seven countries, fourteen pages."),
          ("/ou-passer/", "All countries (in French)", "1,265 centres in 46 countries, with their contact details."),
          ("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 48 approved centres, province by province.")],
    sources="""<strong>Sources.</strong> France Éducation international’s lists of exam centres (by country; types “TCF”
and “DELF-DALF”), read on 26 October 2026 for Canada and on 8 October 2026 for the United States and the United
Kingdom, and the websites of the centres named on each page, checked on 17 September 2026 (Canada) and 8 October
2026. Fees and dates change without notice: check them on the centre’s website before paying.""",
    cta_h2="The centre gives you the date; the score is up to you",
    cta_p="""You pay the full fee for each session, and you can’t retake the test right away. The mock exams in the
“TCF DELF TEF: Tests 2026” app follow the official format of each test — TCF Canada, TCF Québec, DELF B2 — scored
like the real thing, with AI feedback on writing and speaking.""",
)


# ===========================================================================
# CITY PAGES (18/10/2026): searches «tcf canada new york», «boston», «chicago», «san diego», «tcf alberta»,
# «tcf abu dhabi» landed on country pages. Facts: each centre's own website and booking page, read on 18 October 2026
# (scratchpad en_cities/research.md); FEI lists of 8 October (US, UAE) and 19 September 2026 (Canada).
# ===========================================================================
def _city_page(slug, file, variant, og_locale, country_name, match, city, list_date, title, desc, h1, intro, facts, stats,
               sections, faq, also, sources, badges, urls, nearby=None, list_title=None):
    return dict(lang="en", variant=variant, og_locale=og_locale, fr_path=None, slug=slug, country_name=country_name,
                exam="tcf", file=file, layout="city", match=match, nearby=nearby or [], crumb=f"TCF Canada in {city}",
                published="2026-10-18", date_label="18 October 2026", list_date=list_date, releve_date="18 October 2026",
                title=title, desc=desc, h1=h1, intro=intro, facts=facts, stats=stats, sections=sections,
                list_title=list_title or f"The approved TCF {'center' if variant == 'en-US' else 'centre'} in {city}",
                faq=faq, also=also, sources=sources, badges=badges, urls=urls)


_US = ("/en/tcf-canada-usa/", "TCF Canada in the USA", "Every approved center, fees from $330, and where the seats are.")
_CAN = ("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 48 approved centres, province by province.")
_PRACTICE = ("/en/tcf-canada-practice-test/", "Free TCF Canada practice test", "Check your level before you pay for a session.")
_FULL26 = [("ok", "TCF Canada"), ("part", "2026 full")]

# ---------------------------------------------------------------------------- NEW YORK
PAGES.append(_city_page(
    "tcf-canada-new-york", "tcf_etats_unis", "en-US", "en_US", "United States", ["New York"], "New York", "October 8, 2026",
    title="TCF Canada in New York: $399, 2027 dates in Montclair, NJ",
    desc="TCF Canada at L'Alliance New York: $350 for members, $399 otherwise; every 2026 session full, six 2027 dates in Montclair, NJ, from January 25.",
    h1="TCF Canada in New York: L'Alliance New York, the fee and the 2027 dates",
    intro="""In New York, the TCF Canada is held by <strong>L'Alliance New York</strong>, the only approved TCF center in the
city on France Éducation international's list — in Manhattan (22 East 60th Street) or at its Montclair campus in New
Jersey. It costs <strong>$350 for members, $399 otherwise</strong>, plus a $15 administrative fee. On October 18, 2026,
its booking platform showed <strong>every remaining 2026 session full</strong> — October 26, November 6, November 16
and December 14 — and <strong>six 2027 sessions open in Montclair</strong>, from January 25 to June 14.""",
    facts=["<strong>{n} approved center</strong>: L'Alliance New York, 22 East 60th Street, Manhattan; sessions also at its Montclair campus, New Jersey.",
           "Fee: <strong>$350</strong> for L'Alliance members, <strong>$399</strong> otherwise, plus a non-refundable $15 administrative fee.",
           "⚠️ October 18, 2026: <strong>every remaining 2026 session full</strong> — Oct 26 (Montclair), Nov 6 (Manhattan), Nov 16 and Dec 14 (Montclair).",
           "Open: <strong>Jan 25, Feb 22, Mar 22, Apr 19, May 17 and Jun 14, 2027</strong>, all in Montclair; no Manhattan date listed for 2027.",
           "Computer-based, with a 12-minute face-to-face oral; one month between two attempts; certificate in 5 to 6 weeks."],
    stats=[("$399", "TCF Canada", "$350 for members"), ("Jan 25", "next open date", "2027, Montclair NJ"),
           ("1 month", "between two attempts", "L'Alliance's rule"), ("5–6 weeks", "for the certificate", "valid two years")],
    sections=[("booking", "Booking the TCF Canada in New York", """<p>L'Alliance sells the test on its booking platform, linked
from its TCF Canada page on <strong>lallianceny.org</strong> — not lalliance.org, a parked domain that has nothing to do
with the school. Each session has a registration deadline about two weeks before: for 2027, January 25 (by January 12),
February 22 (by February 9), March 22 (by March 9), April 19 (by April 6), May 17 (by May 4) and June 14 (by June 1),
all at the Montclair campus. Keep the day free — L'Alliance asks you to «be available between 9am and 6pm».</p>

<p>The test is computer-based for listening, reading and writing; the speaking test is «individual face-to-face …
with an examiner – 3 exercises – 12 minutes». Before the deadline, a cancellation is refunded «minus an $80
cancellation fee», and a transfer costs $50. L'Alliance requires «a one-month waiting period … between two successive
tests», and the certificate takes «5-6 weeks from the test date». With 2026 full, the nearest center with seats in
December was <a href="/en/tcf-canada-boston/">Boston</a>; other cities are on our <a href="/en/tcf-canada-usa/">USA
page</a>.</p>""")],
    faq=[("Where can I take the TCF Canada in New York?", "At L'Alliance New York, in Manhattan (22 East 60th Street) or at its Montclair campus in New Jersey; it is the only approved TCF center in the city. In 2027, every session listed is in Montclair."),
         ("When is the next TCF Canada in New York?", "On October 18, 2026, every remaining 2026 session was full (October 26, November 6 and 16, December 14). The next open dates were January 25, February 22, March 22, April 19, May 17 and June 14, 2027, in Montclair, NJ."),
         ("How much does the TCF Canada cost in New York?", "$350 for L'Alliance members and $399 for non-members, plus a non-refundable $15 administrative fee (October 18, 2026)."),
         ("Is lalliance.org L'Alliance New York's website?", "No: lalliance.org is a parked domain for sale. L'Alliance New York's website is lallianceny.org, and its TCF Canada page links to the booking platform."),
         ("How long between two attempts in New York?", "One month: «a one-month waiting period is required between two successive tests», according to L'Alliance. FEI no longer accepts re-marking requests for sessions held since September 1, 2026.")],
    also=[_US, ("/en/tcf-canada-boston/", "TCF Canada in Boston", "$350, Saturday sessions in Cambridge, MA."), _PRACTICE],
    sources="L'Alliance New York's TCF Canada page (lallianceny.org) and its booking platform, checked on October 18, 2026.",
    badges={"new-york-lalliance-new-york": _FULL26}, urls={"new-york-lalliance-new-york": "https://lallianceny.org/exams/tcf-canada/"}))

# ---------------------------------------------------------------------------- BOSTON
PAGES.append(_city_page(
    "tcf-canada-boston", "tcf_etats_unis", "en-US", "en_US", "United States", ["Cambridge"], "Boston", "October 8, 2026",
    title="TCF Canada in Boston: $350, Nov 21, Dec 12 and January dates",
    desc="TCF Canada near Boston at the International School of Boston in Cambridge, MA: $350, Saturday sessions on November 21 and December 12, deadlines, January.",
    h1="TCF Canada in Boston: the International School of Boston, the fee and the dates",
    intro="""Near Boston, the TCF Canada is held by the <strong>International School of Boston</strong> — formerly the Lycée
International de Boston —, 45 Matignon Road in Cambridge, the only approved TCF center in Massachusetts. It costs
<strong>$350</strong>, on Saturdays: on October 18, 2026, the next sessions were <strong>November 21</strong> (deadline
November 17) and <strong>December 12</strong> (deadline December 8), and a January Saturday was listed. A weekday date is
possible for $60 more.""",
    facts=["<strong>{n} approved center</strong>: the International School of Boston (ISB Extension, open to adults), 45 Matignon Road, Cambridge, MA.",
           "TCF Canada <strong>$350</strong>; a weekday date costs $60 more (deadline a week before the test).",
           "Saturdays: <strong>November 21</strong> (deadline November 17) and <strong>December 12</strong> (deadline December 8); October 10 was full, with a waitlist.",
           "Also listed: «Saturday, January 9th, 2026 (Deadline January 5th)» — January 9 falls on a Saturday in 2027: confirm the year with the school.",
           "Registration and payment by card on the school's online form; results certificate valid for two years."],
    stats=[("$350", "TCF Canada", "+$60 on a weekday"), ("Nov 21", "next session", "deadline Nov 17"),
           ("Dec 12", "following session", "deadline Dec 8"), ("{n}", "approved center", "in Massachusetts")],
    sections=[("booking", "Booking the TCF Canada in Boston", """<p>The school registers candidates through a <strong>TCF Test
Registration</strong> form on its Extension pages (isbos.org): you choose the session and the test — «TCF Canada
($350)» — and pay by card. Besides the Saturday dates, the form offers a weekday date for $60 more (state your preferred
date in the comments, at least a week ahead) and a private Saturday session for $100 more; a $100 retake fee applies only
to excused candidates, and returning ISB candidates may get $50 off, subject to eligibility. The form doesn't say whether
the test is on paper or on computer, nor how long you must wait between two attempts: ask the school, at the general
Extension address adulted@isbos.org. Other centers and dates: our <a href="/en/tcf-canada-usa/">USA page</a> and
<a href="/en/tcf-canada-new-york/">New York</a>.</p>""")],
    faq=[("Where can I take the TCF Canada in Boston?", "At the International School of Boston (formerly the Lycée International de Boston), 45 Matignon Road in Cambridge, the only approved TCF center in Massachusetts."),
         ("When is the next TCF Canada in Boston?", "On October 18, 2026: Saturday, November 21 (deadline November 17) and Saturday, December 12 (deadline December 8). A January 9 session was also listed, dated 2026 on the form — January 9 is a Saturday in 2027."),
         ("How much does the TCF Canada cost in Boston?", "$350 for a Saturday session; a weekday date costs $60 more, and a private Saturday session $100 more (October 18, 2026)."),
         ("Can I take the TCF Canada in Boston on a weekday?", "Yes, for $60 more: indicate your preferred date in the comments of the registration form, at least a week before the test.")],
    also=[_US, ("/en/tcf-canada-new-york/", "TCF Canada in New York", "$399, 2026 full, 2027 dates in Montclair, NJ."), _PRACTICE],
    sources="the International School of Boston's Extension pages and TCF registration form (isbos.org), checked on October 18, 2026.",
    badges={"cambridge-lycee-international-de-boston": [("ok", "TCF Canada")]},
    urls={"cambridge-lycee-international-de-boston": "https://www.isbos.org/community/extension/exams-certifications"}))

# ---------------------------------------------------------------------------- CHICAGO
PAGES.append(_city_page(
    "tcf-canada-chicago", "tcf_etats_unis", "en-US", "en_US", "United States", ["Chicago"], "Chicago", "October 8, 2026",
    title="TCF Canada in Chicago? Not offered: the TEF Canada, $415",
    desc="There is no TCF Canada in Chicago: the Alliance Française offers the TEF Canada ($415), full until mid-December, with open dates from January 5, 2027.",
    h1="TCF Canada in Chicago: not offered — the TEF Canada instead, and the nearest TCF centers",
    intro="""If you are looking for the TCF Canada in Chicago, the answer is no: the <strong>Alliance Française de
Chicago</strong> — «Illinois' only official French examination center» — offers the TCF tout public and the TCF IRN, but
<strong>not the TCF Canada</strong>. For Canadian immigration it offers the <strong>TEF Canada</strong>, the other French
test IRCC accepts, for <strong>$415</strong>: on October 18, 2026, every session until December 15 was full, and five
January 2027 dates were open. Here are the dates, and the nearest TCF Canada centers.""",
    facts=["<strong>{n} approved TCF center</strong> in Illinois: the Alliance Française de Chicago, 810 North Dearborn Street — <strong>no TCF Canada</strong> (TCF tout public and IRN only).",
           "<strong>TEF Canada: $415</strong>, accepted by IRCC like the TCF Canada; on site only, for the whole day (9 am–5 pm); results in 1 to 10 business days.",
           "⚠️ TEF Canada <strong>full</strong> on Oct 27, Nov 10, 17 and 24, Dec 1 and 15, 2026; open on <strong>Jan 5, 12, 15, 19 and 22, 2027</strong>.",
           "At least 30 days between two TEF Canada sessions.",
           "Nearest TCF Canada centers on October 8: Detroit ($330, full until April 2027) and Kansas City ($370, 2027 dates on sale)."],
    stats=[("0", "TCF Canada sessions", "in Chicago"), ("$415", "TEF Canada", "at the Alliance Française"),
           ("Jan 5", "next open TEF date", "2027"), ("30 days", "between two TEF sessions", "the Alliance's rule")],
    sections=[("tef-or-tcf", "TEF Canada in Chicago, or the TCF Canada elsewhere", """<p>For Express Entry or Canadian
citizenship, IRCC accepts <strong>either</strong> the TCF Canada or the TEF Canada: the score tables differ, but both
convert to CLB levels (<a href="/en/tcf-vs-tef-canada/">TCF vs TEF Canada</a>). In Chicago, only the TEF Canada is on
offer: «The entirety of this exam takes place on-site at the Alliance Française de Chicago … The TEF Canada exam cannot be
taken remotely», and the Alliance asks you to reserve the whole day. On October 18, 2026, its sessions of October 27,
November 10, 17 and 24, December 1 and December 15 were full; January 5, 12, 15, 19 and 22, 2027 were open. Results come
in 1 to 10 business days, and you must wait at least 30 days before another session.</p>

<p>If you have prepared for the TCF Canada specifically, the nearest centers were Detroit ($330, monthly, but full until
April 2027 on October 8) and Kansas City ($370, 2027 dates on sale on October 8); Houston was opening a session every
Wednesday. Fees and dates for each: our <a href="/en/tcf-canada-usa/">USA page</a>. To prepare for the TEF, see
<a href="/en/tef-canada/">TEF Canada: format and scores</a>.</p>""")],
    faq=[("Can I take the TCF Canada in Chicago?", "No: on October 18, 2026, the Alliance Française de Chicago — the only approved center in Illinois — offered the TCF tout public and the TCF IRN, but not the TCF Canada. For immigration, it offers the TEF Canada."),
         ("How much does the TEF Canada cost in Chicago?", "$415 for the full exam needed for immigration, at the Alliance Française de Chicago (October 18, 2026)."),
         ("When is the next TEF Canada in Chicago?", "On October 18, 2026, every session until December 15 was full; the open dates were January 5, 12, 15, 19 and 22, 2027."),
         ("Does IRCC accept the TEF Canada instead of the TCF Canada?", "Yes: IRCC accepts both for Express Entry and citizenship, each with its own conversion table to CLB levels.")],
    also=[_US, ("/en/tcf-vs-tef-canada/", "TCF vs TEF Canada", "The two French tests IRCC accepts, side by side."),
          ("/en/tef-canada-practice-test/", "TEF Canada practice test", "The format, with exercises.")],
    sources="the Alliance Française de Chicago's exams, TEF Canada and TCF tout public pages (af-chicago.org), checked on October 18, 2026; the October 8, 2026 check of the other US centers.",
    badges={"chicago-alliance-francaise": [("no", "no TCF Canada")]}, urls={"chicago-alliance-francaise": "https://www.af-chicago.org/tef/"},
    list_title="The approved TCF center in Chicago"))

# ---------------------------------------------------------------------------- LOS ANGELES (+ PASADENA)
PAGES.append(_city_page(
    "tcf-canada-los-angeles", "tcf_etats_unis", "en-US", "en_US", "United States", ["Los Angeles"], "Los Angeles", "October 8, 2026",
    title="TCF Canada in Los Angeles: $505, monthly dates, Pasadena",
    desc="TCF Canada at the Alliance Française de Los Angeles: $505, Nov 20 and Dec 18, then monthly to June 2027; Pasadena on Nov 12 ($460). How to apply.",
    h1="TCF Canada in Los Angeles: the Alliance Française, Pasadena, the fees and the dates",
    intro="""In Los Angeles, the TCF Canada is held by the <strong>Alliance Française de Los Angeles</strong> (10390 Santa
Monica Blvd, Suite 300) for <strong>$505</strong> — and, nearby, by the <strong>Alliance Française de Pasadena</strong>
for $460. On October 18, 2026, Los Angeles listed <strong>November 20 and December 18</strong>, then one session a month
from January 22 to June 11, 2027, none marked full; you apply by email at least 15 days before the test. Pasadena had a
single date, <strong>November 12</strong> (deadline October 20).""",
    facts=["Alliance Française de Los Angeles: <strong>TCF Canada $505</strong> (the same fee for the TCF tout public, IRN, Québec and DAP); no member rate shown.",
           "Los Angeles: <strong>Nov 20</strong> (apply by Nov 6) and <strong>Dec 18</strong> (by Dec 4); 2027: Jan 22, Feb 26, Mar 19, Apr 23, May 21, Jun 11. Oct 23 closed on Oct 9.",
           "Apply by email to tcf@afdela.org «no later than 15 days before the exam date»; pay on receipt of your written convocation.",
           "Pasadena: <strong>Nov 12, 2026</strong> (deadline Oct 20), <strong>$460</strong> «Registration fees included», plus 3.5% for card payments; not refundable once registered.",
           "⚠️ The official sites are afdela.org and afdepasadena.org — afla.org and afpasadena.org belong to other organizations."],
    stats=[("$505", "TCF Canada", "in Los Angeles"), ("Nov 20", "next open date", "apply by Nov 6"),
           ("$460", "in Pasadena", "Nov 12, deadline Oct 20"), ("6", "dates in 2027", "January to June")],
    sections=[("booking", "Applying in Los Angeles or Pasadena", """<p>The Alliance Française de Los Angeles doesn't sell the
test online: you «email your application to our TCF administrator at tcf@afdela.org — no later than 15 days before the
exam date», and «payment must be made upon receipt of your written convocation». The test takes place at the Alliance,
10390 Santa Monica Blvd, Suite 300; reading and listening results are given «as soon as you finish the test». Its page
doesn't say how long you must wait between two attempts.</p>

<p>In <strong>Pasadena</strong> (232 N. Lake Avenue), the Alliance Française listed one TCF Canada session on October 18,
2026: <strong>November 12</strong>, with registration until October 20, for $460 including registration fees, plus a
non-refundable 3.5% for card payments. «The exam fee is not refundable once registered», and results arrive «within four to
six weeks of the test date», by email. No 2027 session was listed. Further south, <a href="/en/tcf-canada-san-diego/">San
Diego</a> was sold out; other states are on our <a href="/en/tcf-canada-usa/">USA page</a>.</p>""")],
    faq=[("Where can I take the TCF Canada in Los Angeles?", "At the Alliance Française de Los Angeles (10390 Santa Monica Blvd, Suite 300), or nearby at the Alliance Française de Pasadena (232 N. Lake Avenue); both are approved by France Éducation international."),
         ("When is the next TCF Canada in Los Angeles?", "On October 18, 2026: November 20 (apply by November 6) and December 18 (by December 4), then January 22, February 26, March 19, April 23, May 21 and June 11, 2027. Pasadena: November 12, deadline October 20."),
         ("How much does the TCF Canada cost in Los Angeles?", "$505 at the Alliance Française de Los Angeles and $460 at the Alliance Française de Pasadena, plus 3.5% for card payments there (October 18, 2026)."),
         ("How do I register in Los Angeles?", "By email to tcf@afdela.org, at least 15 days before the exam date; you pay once you receive your written convocation.")],
    also=[_US, ("/en/tcf-canada-san-diego/", "TCF Canada in San Diego", "$450, every listed session sold out."), _PRACTICE],
    sources="the TCF pages of the Alliance Française de Los Angeles (afdela.org) and of the Alliance Française de Pasadena (afdepasadena.org), checked on October 18, 2026.",
    badges={"los-angeles-alliance-francaise": [("ok", "TCF Canada")], "pasadena-alliance-francaise": [("ok", "TCF Canada")]},
    urls={"los-angeles-alliance-francaise": "https://www.afdela.org/certifications/tcf",
          "pasadena-alliance-francaise": "https://www.afdepasadena.org/learn-french/certifications/tcf/"},
    nearby=["Pasadena"]))

# ---------------------------------------------------------------------------- SAN DIEGO
PAGES.append(_city_page(
    "tcf-canada-san-diego", "tcf_etats_unis", "en-US", "en_US", "United States", ["San Diego"], "San Diego", "October 8, 2026",
    title="TCF Canada in San Diego: $450, sessions sold out, waitlist",
    desc="TCF Canada at the Alliance Française de San Diego: $450, written part on computer; Oct 20 closed, Nov 4 and 10 sold out, no later date yet. Waitlist.",
    h1="TCF Canada in San Diego: the Alliance Française, the fee and the sessions",
    intro="""In San Diego, the TCF Canada is held by the <strong>Alliance Française de San Diego</strong> (6390 Greenwich Dr,
#185) for <strong>$450</strong>, with the written part on computer. On October 18, 2026, every listed session was closed:
October 20 (registration ended October 14), then November 4 and November 10, both <strong>sold out</strong> — and no
December or 2027 date was listed yet. A waitlist is open; Los Angeles had dates every month.""",
    facts=["<strong>{n} approved center</strong>: the Alliance Française de San Diego, 6390 Greenwich Dr, #185 (UTC area).",
           "TCF Canada <strong>$450</strong>; no member rate shown.",
           "«The written part is a computer-based format»; about 3 hours for the written part and 15 minutes for the oral, in person only.",
           "⚠️ October 18, 2026: <strong>Oct 20 closed</strong>, <strong>Nov 4 and Nov 10 sold out</strong>; no December or 2027 session listed.",
           "Waitlist: «If a session is already full, you can join the waitlist at this link.»"],
    stats=[("$450", "TCF Canada", "written part on computer"), ("0", "open sessions", "on October 18, 2026"),
           ("3 h 15", "test length", "written + oral"), ("{n}", "approved center", "in San Diego")],
    sections=[("booking", "Getting a seat in San Diego", """<p>The Alliance publishes its sessions in a table on its TCF Canada
page, with a registration window for each: the November 4 and 10 sessions opened on July 13, 2026 and were sold out by
mid-October. Written test and oral take place on the same day — for November, written 8:40 am to 12 pm, oral 12:30 to
2 pm — at the Alliance, «in person only». If a session is full, join the waitlist from the page, and watch for the next
sessions, not yet published on October 18. In the meantime, the <a href="/en/tcf-canada-los-angeles/">Alliance Française
de Los Angeles</a> listed November 20, December 18 and monthly 2027 dates; its official site is afsandiego.org — afsd.org
is a parked page, not the Alliance.</p>""")],
    faq=[("Where can I take the TCF Canada in San Diego?", "At the Alliance Française de San Diego, 6390 Greenwich Dr, #185, in person only, with the written part on computer."),
         ("When is the next TCF Canada in San Diego?", "On October 18, 2026, none was open: October 20 had closed, November 4 and 10 were sold out, and no December or 2027 date was listed. A waitlist is available."),
         ("How much does the TCF Canada cost in San Diego?", "$450 at the Alliance Française de San Diego (October 18, 2026)."),
         ("Where else in California?", "In Los Angeles ($505; November 20, December 18 and monthly 2027 dates) and Pasadena ($460; November 12), on October 18, 2026.")],
    also=[_US, ("/en/tcf-canada-los-angeles/", "TCF Canada in Los Angeles", "$505, monthly dates to June 2027, and Pasadena."), _PRACTICE],
    sources="the Alliance Française de San Diego's TCF and TCF Canada pages (afsandiego.org), checked on October 18, 2026.",
    badges={"san-diego-alliance-francaise": _FULL26}, urls={"san-diego-alliance-francaise": "https://www.afsandiego.org/certifications/tcf/tcf-canada/"}))

# ---------------------------------------------------------------------------- CALGARY
PAGES.append(_city_page(
    "tcf-canada-calgary", "tcf_canada", "en-CA", "en_CA", "Canada", ["Calgary"], "Calgary", "19 September 2026",
    title="TCF Canada in Calgary: $400, sessions sold out to December",
    desc="TCF Canada at the Alliance Française de Calgary: $400, computer-based, 14 seats a session at the Kahanoff Centre; October to December 2026 sold out.",
    h1="TCF Canada in Calgary: the Alliance Française, the fee and the sessions",
    intro="""In Calgary, the TCF Canada is held by the <strong>Alliance Française de Calgary</strong> for <strong>$400</strong>, on
computer, at its testing centre in the <strong>Kahanoff Centre</strong> (#315, 105 12 Avenue SE) — not at its office on
29th Avenue SW. Each session has 14 seats, first come, first served, and on 18 October 2026 <strong>every session from
October to December was sold out</strong>; no 2027 date was published. The Alliance says it is «working with our partners
in Paris to open additional sessions».""",
    facts=["<strong>{n} approved centre</strong> in Calgary: the Alliance Française; Alberta's other approved centres are in Edmonton and Lethbridge.",
           "<strong>TCF Canada $400</strong>; «no refund or deferment is possible».",
           "Test venue: <strong>Kahanoff Centre, #315, 105 12 Avenue SE</strong>; computer-based with a QWERTY keyboard, except the speaking test.",
           "⚠️ 18 October 2026: <strong>October, November and all ten December sessions sold out</strong>; no 2027 date published.",
           "14 seats per session; at least 20 days between two attempts, «in any location»."],
    stats=[("$400", "TCF Canada", "no refund or deferment"), ("14", "seats per session", "first come, first served"),
           ("0", "open sessions", "October to December 2026"), ("20 days", "between two attempts", "in any location")],
    sections=[("booking", "Getting a seat in Calgary", """<p>The Alliance publishes its dates on its TCF registration page —
«All 2026 exam dates will be published on this page» — and sells them «on a first-come, first-served basis». In
December 2026 it scheduled ten test days (1, 2, 3, 8, 9, 10, 15, 16, 17 and 22 December): all were sold out on
18 October. Watch the page for the additional sessions it is negotiating, and for the 2027 calendar; questions go to the
generic address tests@afcalgary.ca. The University of Lethbridge is on FEI's list, but its exam pages showed only the
DELF on 18 October. In <a href="/en/tcf-canada-edmonton/">Edmonton</a>, sessions open for about an hour each; the other
provinces are on our <a href="/en/tcf-canada-test-centres/">list of centres in Canada</a>.</p>""")],
    faq=[("Where can I take the TCF Canada in Calgary?", "At the Alliance Française de Calgary, whose tests take place at its testing centre in the Kahanoff Centre (#315, 105 12 Avenue SE), on computer."),
         ("When is the next TCF Canada in Calgary?", "On 18 October 2026, every session from October to December 2026 was sold out and no 2027 date was published; the Alliance was working to open additional sessions."),
         ("How much does the TCF Canada cost in Calgary?", "$400 at the Alliance Française de Calgary, with no refund or deferment possible (18 October 2026)."),
         ("Where else can I take the TCF in Alberta?", "At the Alliance Française d'Edmonton ($400). The University of Lethbridge is on FEI's list, but its pages showed only the DELF on 18 October 2026.")],
    also=[("/en/tcf-canada-edmonton/", "TCF Canada in Edmonton", "$400; each session opens for about an hour."),
          ("/en/tcf-canada-alberta/", "TCF Canada in Alberta", "Calgary, Edmonton, Lethbridge: fees, dates, where seats are."), _PRACTICE],
    sources="the Alliance Française de Calgary's TCF and registration pages (afcalgary.ca) and the University of Lethbridge's exam pages, checked on 18 October 2026.",
    badges={"calgary-alliance-francaise": [("ok", "TCF Canada"), ("part", "sold out to December")]},
    urls={"calgary-alliance-francaise": "https://www.afcalgary.ca/exams/tcf/"}))

# ---------------------------------------------------------------------------- EDMONTON
PAGES.append(_city_page(
    "tcf-canada-edmonton", "tcf_canada", "en-CA", "en_CA", "Canada", ["Edmonton"], "Edmonton", "19 September 2026",
    title="TCF Canada in Edmonton: $400, how the one-hour sales work",
    desc="TCF Canada at the Alliance Française d'Edmonton: $400; every session to November 20 sold out, each opened for about an hour on one day. How booking works.",
    h1="TCF Canada in Edmonton: the Alliance Française, the fee and how to get a seat",
    intro="""In Edmonton, the TCF Canada is held by the <strong>Alliance Française d'Edmonton</strong> for <strong>$400</strong>,
at its new annex (100, 11812–121 St NW, Kingsway). On 18 October 2026, every listed session — a morning and an
afternoon on each date from 19 October to 20 November — was <strong>sold out or closed</strong>, and no December or 2027
date was listed. Each session's sales open for <strong>about an hour on a single day</strong>: to get a seat, you have to
be online at that moment.""",
    facts=["<strong>{n} approved centre</strong> in Edmonton: the Alliance Française; tests at its annex, 100, 11812–121 St NW (Kingsway).",
           "<strong>TCF Canada $400</strong> for the full exam.",
           "⚠️ 18 October 2026: every session from <strong>19 October to 20 November</strong> sold out or closed; no December or 2027 date listed.",
           "Each session goes on sale for about an hour on one day — the 16 November sessions, for example, from 3:09 to 4:15 pm on 14 October.",
           "20 days before you can retake the test; score re-evaluations suspended since 1 September 2026."],
    stats=[("$400", "TCF Canada", "full exam"), ("~1 hour", "sales window", "per session"),
           ("0", "open sessions", "on 18 October 2026"), ("20 days", "before a retake", "the Alliance's rule")],
    sections=[("booking", "Getting a seat in Edmonton", """<p>The Alliance lists its sessions in a table on its TCF page, each with
a written test in the morning (9:20 am) or the afternoon (1:30 pm) and an oral «to be confirmed». Registration is online
only, «enable only during registration period. Seats are limited.»: each session's window lasted about an hour, on a
single day, and every session up to 20 November was sold out by 18 October. The Alliance warns that if your request
concerns TEF or TCF dates, «you will not receive an individual response either by email or by phone»: watch the page
for the next windows. If you fail, you may retake the test 20 days later; «as of September 1, 2026, TCF score
re-evaluations are no longer available until further notice». <a href="/en/tcf-canada-calgary/">Calgary</a> was sold out
to December; the other provinces are on our <a href="/en/tcf-canada-test-centres/">list of centres in Canada</a>.</p>""")],
    faq=[("Where can I take the TCF Canada in Edmonton?", "At the Alliance Française d'Edmonton, whose tests take place at its new annex, 100, 11812–121 St NW, in Kingsway."),
         ("When is the next TCF Canada in Edmonton?", "On 18 October 2026, every listed session up to 20 November was sold out or closed, and no December or 2027 date was listed. Each session goes on sale for about an hour on a single day."),
         ("How much does the TCF Canada cost in Edmonton?", "$400 for the full exam at the Alliance Française d'Edmonton (18 October 2026)."),
         ("How soon can I retake the TCF Canada in Edmonton?", "20 days after your last attempt, according to the Alliance; score re-evaluations have been suspended since 1 September 2026.")],
    also=[("/en/tcf-canada-calgary/", "TCF Canada in Calgary", "$400, 14 seats a session, sold out to December."),
          ("/en/tcf-canada-alberta/", "TCF Canada in Alberta", "Calgary, Edmonton, Lethbridge: fees, dates, where seats are."), _PRACTICE],
    sources="the Alliance Française d'Edmonton's TCF page and session table (afedmonton.com), checked on 18 October 2026.",
    badges={"edmonton-alliance-francaise": [("ok", "TCF Canada"), ("part", "sold out to 20 Nov")]},
    urls={"edmonton-alliance-francaise": "https://www.afedmonton.com/en/exams/tcf/"}))

# ---------------------------------------------------------------------------- ABU DHABI
PAGES.append(_city_page(
    "tcf-canada-abu-dhabi", "tcf_emirats", "en-GB", "en_AE", "United Arab Emirates", ["Abou Dhabi"], "Abu Dhabi", "8 October 2026",
    title="TCF Canada in Abu Dhabi: 1,800 AED, 20 Nov and 16 Dec dates",
    desc="TCF Canada at the Alliance Française Abu Dhabi (Al Bateen): 1,800 AED, on computer; 20 November and 16 December open, deadlines 9 Nov and 6 Dec.",
    h1="TCF Canada in Abu Dhabi: the Alliance Française, the fee and the dates",
    intro="""In Abu Dhabi, the TCF Canada is held by the <strong>Alliance Française Abu Dhabi</strong> — listed by FEI as the
«Institut français – Antenne AFAD» — at 99 Al Qouʻ Street in Al Bateen, on computer, for <strong>1,800 AED</strong>. On
18 October 2026, two sessions were open: <strong>Friday 20 November</strong> (registration until 9 November) and
<strong>Wednesday 16 December</strong> (until 6 December). Its Al Ain branch held no TCF Canada session.""",
    facts=["<strong>{n} approved centre</strong> in Abu Dhabi: the Alliance Française Abu Dhabi, 99 Al Qouʻ St, Al Bateen; Al Ain is on FEI's list too, but showed no TCF Canada session.",
           "<strong>TCF Canada 1,800 AED</strong>, «Exam done at our center on computer»; TCF IRN 1,380 AED.",
           "Open on 18 October 2026: <strong>Friday 20 November</strong> (deadline 9 November) and <strong>Wednesday 16 December</strong> (deadline 6 December).",
           "Register online or at the Alliance's offices, during the registration period only; a passport copy is required.",
           "⚠️ Fees «will NOT be refunded or transferred under ANY circumstances» once registration is done."],
    stats=[("1,800 AED", "TCF Canada", "on computer"), ("20 Nov", "next session", "deadline 9 Nov"),
           ("16 Dec", "following session", "deadline 6 Dec"), ("0", "sessions in Al Ain", "on 18 October 2026")],
    sections=[("booking", "Booking the TCF Canada in Abu Dhabi", """<p>The Alliance sells its sessions on its online booking
platform, linked from its TCF Canada page (afabudhabi.org), and at its offices: «Candidates can register only during the
registration period online or by visiting our offices», and «Seats are limited … first-come first-serve basis». Bring a
copy of your passport. Once registered, the fee is neither refunded nor transferred. All its TCF sessions are held at
the Al Bateen centre — the TCF tout public on 18 November, the TCF IRN on 19 November, the TCF Canada on 20 November —
and none at Al Ain. In Dubai, the Alliance Française also holds the TCF Canada at 1,800 AED:
<a href="/en/tcf-canada-dubai/">TCF Canada in Dubai and the UAE</a>.</p>""")],
    faq=[("Where can I take the TCF Canada in Abu Dhabi?", "At the Alliance Française Abu Dhabi (FEI lists it as «Institut français – Antenne AFAD»), 99 Al Qouʻ Street, Al Bateen, on computer."),
         ("When is the next TCF Canada in Abu Dhabi?", "On 18 October 2026: Friday 20 November (registration until 9 November) and Wednesday 16 December (until 6 December)."),
         ("How much does the TCF Canada cost in Abu Dhabi?", "1,800 AED, the same as in Dubai; the TCF IRN costs 1,380 AED (18 October 2026)."),
         ("Can I take the TCF Canada in Al Ain?", "Not on 18 October 2026: the Al Ain branch of the Alliance Française Abu Dhabi listed no TCF Canada session; all TCF sessions were at the Al Bateen centre.")],
    also=[("/en/tcf-canada-dubai/", "TCF Canada in Dubai and the UAE", "Both Dubai centres and Abu Dhabi, 1,800 AED."),
          ("/en/delf-dubai/", "DELF in Dubai", "The 11 December 2026 session, DELF B2 680 AED."), _PRACTICE],
    sources="the Alliance Française Abu Dhabi's TCF and Al Ain pages (afabudhabi.org) and its booking platform, checked on 18 October 2026.",
    badges={"abou-dhabi-french-ambassy-institut-francais-antenne-afad": [("ok", "TCF Canada")],
            "al-ain-alliance-francais-d-abu-dhabi-antenne-al-ain": [("no", "no TCF Canada session")]},
    urls={"abou-dhabi-french-ambassy-institut-francais-antenne-afad": "https://www.afabudhabi.org/tcf/"},
    nearby=["Al Ain"]))

from pays_config_en_arab import PAGES as _ARAB; PAGES += _ARAB  # Jordan, Qatar, Kuwait (26/10/2026)
from pays_config_en_na import PAGES as _NA; PAGES += _NA  # North America: US cities, Alberta, Ontario, New Brunswick, Halifax, Winnipeg (26/10/2026)
from pays_config_en_eu import PAGES as _EU, hub_patch as _eu_hub; PAGES += _EU; _eu_hub(HUB)  # Europe: Germany, Switzerland, Belgium, Italy, Netherlands, Portugal, Romania, Poland, Greece, Ireland (26/10/2026)
