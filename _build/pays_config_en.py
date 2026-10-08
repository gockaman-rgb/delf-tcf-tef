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
    title="TCF Canada in the USA: 9 test centers, prices, dates",
    desc="Where to take the TCF Canada in the US: 9 of the 18 approved centers offer it, for $330 to $460. Houston, New York, Detroit… Open dates and registration.",
    h1="TCF Canada in the USA: the test centers that offer it, prices and open seats",
    intro="""In the United States, {n} centers are approved for the TCF by France Éducation international, but
<strong>only nine offered the TCF Canada</strong> on October 8, 2026, according to their websites — from
<strong>$330</strong> in Detroit to <strong>$460</strong> in San Francisco. Four don’t, despite being on the list:
Atlanta, Chicago, Seattle and Washington, which point candidates to the TEF Canada. And seats are scarce: San
Francisco, Philadelphia, Denver and Kansas City were full for the rest of 2026, Detroit until April 2027; Houston,
New York and Boston still had dates.""",
    facts=["<strong>{n} approved centers</strong> (FEI list of October 8, 2026), <strong>9 offering the TCF Canada</strong>: Detroit, Boston (International School), New York, Denver (Alliance and Pluma Academy), Philadelphia, Kansas City, Houston and San Francisco.",
           "<strong>No TCF Canada</strong> in Atlanta (no TCF at all), Chicago (tout public and IRN), Seattle (no TCF) or Washington (DAP only): these Alliances point candidates to the TEF Canada.",
           "TCF Canada fees: <strong>$330 to $460</strong> — Detroit $330, Boston $350, New York $350 (members) or $399, Denver and Philadelphia $360, Kansas City $370, Houston $400, Pluma Academy $435, San Francisco $460.",
           "⚠️ <strong>Full</strong> for the rest of 2026 in San Francisco, Philadelphia, Denver (Alliance) and Kansas City; until April 2027 in Detroit.",
           "Still open on October 8: <strong>Houston every Wednesday</strong> until January 27, 2027, <strong>New York</strong> (October 26, November 6 and 16, December 14), <strong>Boston</strong> (November 21, December 12), Pluma Academy (individual sessions).",
           "Waiting period between two attempts: from 20 days (Detroit) to one month (New York, Denver), depending on the center."],
    stats=[("9", "TCF Canada centers", "out of {n} approved"), ("$330-460", "TCF Canada fee", "depending on the center"),
           ("4", "centers full", "for the rest of 2026"), ("2 years", "validity", "results in 10 days to 6 weeks")],
    sections=[
        ("tcf-canada-centers", "Who offers the TCF Canada in the USA", releve([
            ("Alliance française de Detroit (Bingham Farms, Michigan)", "<strong>Canada</strong>, IRN, tout public, DAP",
             "Canada <strong>$330</strong> · IRN $300 ($280 members) · tout public $190 to $350",
             "Monthly, on Thursdays: Nov 12 and Dec 10, 2026, and every session through Apr 15, 2027, <strong>full</strong>; May 13 and Jun 10, 2027 open. Computer-based; results within 10 days."),
            ("International School of Boston (Cambridge, Massachusetts)", "<strong>Canada</strong>, IRN, Québec, tout public",
             "Canada <strong>$350</strong> · IRN $350 · +$60 on weekdays",
             "Saturdays: Oct 10 full (waitlist), <strong>Nov 21</strong> (deadline Nov 17), <strong>Dec 12</strong> (deadline Dec 8), January. Card payment at registration."),
            ("L'Alliance New York", "<strong>Canada</strong>, IRN", "<strong>$350</strong> members · $399 non-members, + $15 fee",
             "Almost monthly: <strong>Oct 26</strong> in Montclair, New Jersey (deadline Oct 13), <strong>Nov 6</strong> in Manhattan (deadline Oct 26), Nov 16 and Dec 14 in Montclair. Computer-based."),
            ("Alliance française de Denver", "<strong>Canada</strong>; IRN and tout public on request", "Canada <strong>$360</strong> · IRN $360",
             "Nov 16, Nov 30 and Dec 7, 2026 <strong>full</strong>; no 2027 dates. Registration closes seven business days before; passport required."),
            ("Alliance Française de Philadelphie", "<strong>Canada</strong>, IRN, tout public", "Canada <strong>$360</strong> ($340 members) · IRN $300",
             "Oct 16 and Dec 18, 2026 <strong>full</strong>; waitlist; registration closes one month before. Paper-based."),
            ("Alliance française de Kansas City", "<strong>Canada</strong>, IRN, tout public, Québec", "Canada <strong>$370</strong> ($380 in 2027) · IRN $370",
             "2026 <strong>full</strong>; 2027: Jan 14 (one seat), Jan 28, Feb 4, Feb 18, Mar 4… through Jun 24, four seats per session. Computer-based."),
            ("Alliance française de Houston", "<strong>Canada</strong> (IRN, tout public and Québec announced, no dates)", "Canada <strong>$400</strong>",
             "<strong>Every Wednesday</strong>, ten seats: Oct 14, 21, 28, Nov 4, Dec 2, 9, 16, 2026, then Jan 6 to 27, 2027; registration closes three days before. Computer-based."),
            ("Pluma Academy (Denver)", "<strong>Canada</strong>, IRN, tout public", "Canada <strong>$435</strong> · IRN $435 · tout public $255 to $435",
             "Individual sessions, about twenty dates a month from October to March; callback within 24 hours of registering. Computer-based (paper: +$70)."),
            ("Alliance française de San Francisco", "<strong>Canada</strong>, IRN, tout public", "Canada <strong>$460</strong> · IRN $550 · tout public $250 + $180 per writing or speaking test",
             "TCF Canada <strong>full</strong> through the end of 2026 (waitlist); no 2027 dates. Passport required; 25 days between two TCF attempts."),
            ("Alliance française d'Atlanta", "<strong>no TCF</strong>", "—", "“We do NOT currently offer TCF or TEF exams,” the Alliance says."),
            ("Alliance française de Chicago", "tout public and IRN — <strong>no Canada</strong>", "tout public $215 to $385", "Points candidates to the TEF Canada ($415), almost full until mid-December."),
            ("Alliance française de Seattle", "<strong>no TCF</strong> on its website", "—", "Points candidates to the TEF (TEF Canada $365)."),
            ("Alliance française de Washington", "DAP only — <strong>no Canada</strong>", "DAP $350", "For Canadian immigration, the Alliance refers candidates to the TEF Canada."),
            ("Alliances in Los Angeles, Pasadena and San Diego; French American School of Puget Sound; Wesleyan University", NR, NR, "Approved by FEI, not checked on October 8, 2026: see their websites."),
        ], "en-US", "What each center’s website showed on October 8, 2026. “No data”: not published, or not checked — the center’s website is the reference.")),
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
    ],
    list_title="The {n} approved TCF test centers, state by state",
    faq=[("Where can I take the TCF Canada in the USA?", "At one of the nine centers that offered it on October 8, 2026: the Alliances Françaises in Detroit, New York, Denver, Philadelphia, Kansas City, Houston and San Francisco, the International School of Boston, and Pluma Academy in Denver. Atlanta, Chicago, Seattle and Washington are approved for the TCF but don’t offer the TCF Canada."),
         ("How much does the TCF Canada cost in the USA?", "From $330 (Detroit) to $460 (San Francisco): $350 in Boston, $350 for members or $399 in New York, $360 in Denver and Philadelphia, $370 in Kansas City, $400 in Houston, $435 at Pluma Academy. Prices checked on October 8, 2026."),
         ("Where can I find a seat quickly?", "On October 8, 2026, the Alliance française de Houston was opening a session every Wednesday until January 27, 2027, New York had four dates before the end of December, Boston two, and Pluma Academy in Denver runs individual sessions several times a week. San Francisco, Philadelphia, Denver (Alliance) and Kansas City were full for 2026."),
         ("Can I take the TCF Canada in Washington, DC or Chicago?", "No: the Alliance française de Washington now offers only the TCF DAP, and Chicago only the TCF tout public and IRN. Both refer immigration candidates to the TEF Canada, which IRCC also accepts."),
         ("Does IRCC accept a TCF Canada taken in the USA?", "Yes: the results certificate is issued by France Éducation international whichever approved center you test at, and it is valid for two years. IRCC requires results less than two years old both when you create your Express Entry profile and when you submit your application.")],
    also=[("/en/delf-usa/", "DELF and DALF in the USA", "The December 2026 session and the shared fee schedule."),
          ("/en/tcf-canada-test-centres/", "TCF Canada test centers in Canada", "The 47 approved centers, province by province."),
          ("/en/tcf-canada-uk/", "TCF Canada in the UK", "London (£260) and Glasgow (£325).")],
    sources="the websites of the Alliances Françaises of Detroit, Atlanta, Chicago, Denver, Houston, Kansas City, New York, Philadelphia, San Francisco, Seattle and Washington, the International School of Boston and Pluma Academy (TCF pages, online stores and session pickers, exam terms and policies), checked on October 8, 2026.",
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
             "Canada about one Friday a month, 35 to 36 places: 20 Nov 2026 and 5 Feb 2027 <strong>full</strong>; <strong>23 Apr 2027</strong> open (registration until 18 Mar), then May, June, July, September and November 2027. IRN: 29 Jan 2027. No Québec session open. Paper-based."),
            ("Alliance française de Glasgow", "<strong>Canada</strong>, IRN, tout public",
             "Canada <strong>£325</strong> · IRN £245 · tout public £195",
             "Five Canada sessions a year (September, November, March, May, July): 25 Nov 2026 <strong>full</strong>; 2027 dates not published. Tout public 18 Nov and IRN 27 Nov 2026, registration until 15 Oct. Paper-based."),
            ("Alliance française de Jersey", "no TCF session published", "—",
             "The website mentions the TCF only for a preparation course: check with the Alliance."),
        ], "en-GB", "What each centre’s website showed on 8 October 2026. “No data”: not published, or not checked — the centre’s website is the reference.") + """
<p>In London, the Institut’s page and its booking module don’t always match: the TCF Canada sessions of 15 January
and 22 October 2027 appear on the page but not in the module, and the page dates the February session
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
and at the Alliances in Manchester, Cambridge and Oxford; and neighbouring France has 251 TCF centres.</p>"""),
    ],
    list_title="The {n} approved TCF test centres in the UK",
    faq=[("Where can I take the TCF Canada in London?", "At the Institut français du Royaume-Uni, 14 Cromwell Place (South Kensington), the only centre in London approved for the TCF. It offers the TCF Canada for £260, about one Friday a month; on 8 October 2026, its sessions of 20 November 2026 and 5 February 2027 were full, and the first open date was 23 April 2027."),
         ("How much does the TCF Canada cost in the UK?", "£260 at the Institut français in London (the fee since 1 July 2026) and £325 at the Alliance française de Glasgow, as checked on 8 October 2026."),
         ("Is the TCF computer-based in London?", "No: both the Institut français in London and the Alliance française de Glasgow announce a paper-based exam, even though France Éducation international’s list mentions a computer option for London."),
         ("Can I cancel or postpone my TCF?", "Yes, within 14 days of registering. After that, neither centre refunds or postpones, except for documented force majeure; the Institut in London then keeps £38 and only accepts a transfer before registration closes."),
         ("What if all TCF sessions are full?", "Book early: in London, the 2027 sessions have been open since 18 August 2026. Otherwise, the TEF Canada, also accepted by IRCC, is offered at the Institut français d’Écosse and at the Alliances in Manchester, Cambridge and Oxford; France also has 251 TCF centres.")],
    also=[("/en/delf-uk/", "DELF and DALF in the UK", "Sessions from December 2026 to June 2027, B2 at £160."),
          ("/en/tcf-canada-usa/", "TCF Canada in the USA", "Nine centres offer it, from $330 to $460."),
          ("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 47 approved centres, province by province.")],
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
           "⚠️ December 2026 already full in places on 8 October: B2 in Glasgow, Oxford and Milton Keynes; A2 and B1 in Oxford.",
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
    title="TCF Canada test centres: the 47 approved centres in Canada",
    desc="The 47 approved TCF Canada test centres in Canada — Montreal, Toronto, Vancouver, Ottawa… — province by province, with address, phone, email and website.",
    h1="TCF Canada test centres in Canada: the 47 approved centres, province by province",
    intro="""In Canada, you can take the TCF Canada and the TCF Québec at one of <strong>{n} test centres approved</strong> by
France Éducation international (48 entries on its list of 19 September 2026, one centre appearing twice) —
Alliances Françaises, universities, CEGEPs and training centres — in <strong>nine provinces and Nunavut</strong>,
{so} of them with computer-based sessions. Below: the list by province and city, with the contact details FEI
publishes, and the registration rules we found at the main centres.""",
    facts=["<strong>{n} approved centres</strong> (48 FEI entries, with Gaspé listed twice), list of 19 September 2026: 23 in Quebec, including 7 in Montreal, 7 in Ontario, 5 in British Columbia, 3 in Alberta.",
           "<strong>45 entries with computer-based sessions</strong>; paper-based only in Sherbrooke, in Lethbridge and at the University of Victoria.",
           "Each centre sets its own price, often unpublished: $390 (Alliance française, Vancouver), $400 (Alliance française, Edmonton), $440 (UQTR); nothing posted at the Alliance Française de Montréal.",
           "⚠️ Sessions in Toronto and Vancouver <strong>fill up within minutes</strong>: register the moment registration opens, not as your test date approaches.",
           "<strong>20 days</strong> between two attempts, whichever centre you test at; results in 2 to 4 weeks.",
           "No centre in Prince Edward Island, Yukon or the Northwest Territories."],
    stats=[("{n}", "approved centres", "FEI list of 19 September 2026"), ("{so}", "computer-based", "the others paper-based"),
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
        ("city-guides", "City guides: Montreal, Toronto, Quebec City, Ottawa, Vancouver", """<p>For the largest cities, one
page brings together the approved TCF centres with their contacts, what their websites showed on 17 September 2026
— versions, prices, dates — and how to register:</p>
<ul class="posts">
<li><a href="/en/tcf-canada-montreal/">TCF Canada in Montreal</a>
<p>Seven approved centres, all computer-based, plus Laval, Kirkland and Saint-Constant; fees rarely published.</p></li>
<li><a href="/en/tcf-canada-toronto/">TCF Canada in Toronto</a>
<p>Four Alliance française campuses and GB Language Centre; quarterly sessions, registration at 10 am a month before.</p></li>
<li><a href="/en/tcf-canada-quebec-city/">TCF Canada in Quebec City</a>
<p>Collège Stanislas and Université Laval, both computer-based, for the TCF Canada and the TCF Québec.</p></li>
<li><a href="/en/tcf-canada-ottawa/">TCF Canada in Ottawa</a>
<p>Alliance française Ottawa (computer or paper) and FrancoLangues in Kanata; no entry without a passport and a printed notice.</p></li>
<li><a href="/en/tcf-canada-vancouver/">TCF Canada in Vancouver</a>
<p>$390 at the Alliance française Canada Pacific, where every listed session was sold out on 17 September 2026.</p></li>
</ul>"""),
    ],
    list_title="The {n} approved centres, province by province",
    list_intro="""<p><strong>One addition since:</strong> read again on 8 October 2026, FEI’s list includes one centre that is
not on the 19 September list used below — <strong>Collège Boréal</strong> in Windsor, Ontario (7515 Forest Glade
Drive; paper-based, according to FEI).</p>""",
    faq=[("Where can I take the TCF Canada in Montreal?", "At one of the seven approved centres in Montreal — Alliance Française de Montréal, Collège Stanislas, UQAM, Concordia University, Cégep Marie-Victorin, Centre Yves-Thériault, Collège ELC — or in the suburbs, in Laval, Kirkland and Saint-Constant. All of them offer computer-based sessions."),
         ("Where can I take the TCF Canada in Toronto?", "At the Alliance française de Toronto (Spadina, North York, Mississauga and Oakville campuses) or at GB Language Centre in North York. The Alliance’s sessions are quarterly; registration opens a month before, at 10 am, and fills up within minutes."),
         ("How much does the TCF Canada cost in Canada?", "There is no national fee, and many centres publish nothing: $390 at the Alliance française in Vancouver, $400 in Edmonton, $440 at UQTR among the centres we checked; the Alliance Française de Montréal posts no price."),
         ("Do all these centres offer both the TCF Canada and the TCF Québec?", "Most offer both, but FEI’s list doesn’t say: check which test you tick when you register — the TCF Québec, which is modular, is not accepted by IRCC."),
         ("What do I need to bring on test day?", "A valid passport and your printed test-day notice — no exceptions in Ottawa; your identity is checked throughout the test. For computer-based tests, the centre provides a QWERTY keyboard.")],
    also=[("/en/tcf-canada-usa/", "TCF Canada in the USA", "9 of the 18 approved US centres offer it, from US$330 to US$460."),
          ("/en/tcf-canada-uk/", "TCF Canada in the UK", "London (£260) and Glasgow (£325)."),
          ("/en/", "All locations", "Every country and city page in English.")],
    sources="the websites of the Alliances Françaises in Montreal, Toronto, Ottawa and Vancouver (Alliance française Canada Pacific) — TCF pages, registration and cancellation terms — checked on 17 September 2026.",
))

# ===========================================================================
# TORONTO
# ===========================================================================
PAGES.append(canada(
    "tcf-toronto", slug="tcf-canada-toronto",
    crumb="TCF Canada in Toronto",
    title="TCF Canada in Toronto: test centres, dates and booking",
    desc="TCF Canada in Toronto: 5 approved centres — 4 Alliance française campuses (Spadina, North York, Mississauga, Oakville), GB Language — quarterly sessions.",
    h1="Taking the TCF Canada in Toronto: the approved centres, the sessions and registration",
    intro="""In Toronto, you can take the TCF Canada at <strong>{n} centres approved</strong> by France Éducation
international: the four campuses of the <strong>Alliance française de Toronto</strong> — Spadina, North York,
Mississauga, Oakville — and GB Language Centre in North York, all computer-based (paper is also possible at the
Alliance). The Alliance’s sessions are <strong>quarterly</strong>, registration opens a month before at 10 am, and
“If a session is not listed, it is full.” Below: the centres, their contacts, and how to get a seat.""",
    facts=["<strong>{n} approved centres</strong> in the area: Alliance française de Toronto (Spadina, North York, Mississauga, Oakville) and GB Language Centre.",
           "<strong>Quarterly sessions</strong> at the Alliance; registration opens <strong>one month before, at 10 am</strong>.",
           "Registration openings for 2027: <strong>1 December 2026</strong> (January to March), 2 March, 20 May, 17 August 2027.",
           "“If a session is not listed, it is full”; no waitlist; one registration at a time.",
           "FEI has dropped re-marking for sessions held since 1 September 2026."],
    stats=[("{n}", "approved centres", "FEI list of 19 September 2026"), ("{so}", "computer-based", "all centres in the area"),
           ("checked", "17 Sept 2026", "prices and dates read on the websites"), ("2 years", "validity", "20 to 30 days between two attempts")],
    sections=[
        ("what-we-found", "What we found, centre by centre", releve([
            ("Alliance française de Toronto (4 campuses)", "Canada (paper or computer-based), Québec", "<strong>not published</strong> on the TCF page",
             "Quarterly; registration 1 month before, at 10 am; 2027: 1 Dec 2026, 2 Mar, 20 May, 17 Aug; no waitlist."),
            ("GB Language Centre (North York)", NR, NR, "On the centre’s website."),
        ], "en-CA", "What each centre’s website showed on 17 September 2026. “No data”: not published, or not checked — the centre’s website is the reference.")),
        ("registration", "How to book the TCF Canada in Toronto", """<p>In Canada, each centre handles its own registrations
<strong>online, on its own website</strong>, with the passport you’ll use for your IRCC application. Registration is
final, and cancelling costs money: the Alliance Française de Montréal keeps $75 if you cancel more than 15 days ahead,
and refunds nothing after that. In the big cities, sessions <strong>fill up within minutes</strong>: create your
account in advance and log in the moment registration opens. Allow at least <strong>20 days</strong> between two
attempts, whichever centre you test at. Results arrive by email within 2 to 4 weeks and are valid for two years. On
test day, bring a valid passport and your printed test-day notice (admission letter).</p>
<p>For the whole country — the 47 approved centres, province by province, with contacts — see
<a href="/en/tcf-canada-test-centres/">TCF Canada test centres in Canada</a>.</p>"""),
    ],
    list_title="The {n} approved centres in Toronto and the surrounding area",
    faq=[("Where can I take the TCF Canada in Toronto?", "At the Alliance française de Toronto, on four campuses — Spadina (downtown), North York, Mississauga, Oakville — or at GB Language Centre in North York. Registration is online only."),
         ("When does TCF Canada registration open in Toronto?", "A month before each quarter, at 10 am: for 2027, on 1 December 2026 (sessions from January to March), then on 2 March, 20 May and 17 August 2027. Seats go within minutes; there is no waitlist, so check back regularly — seats do free up."),
         ("How much does the TCF Canada cost in Toronto?", "The Alliance française de Toronto doesn’t post a fee on its TCF page; the price appears when you book. For reference: $390 in Vancouver, $400 in Edmonton, $440 at UQTR."),
         ("Paper or computer-based in Toronto?", "The Alliance française offers both formats; GB Language Centre lists computer-based sessions.")],
    also=[("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 47 approved centres, province by province, with contacts."),
          ("/en/tcf-canada-ottawa/", "TCF Canada in Ottawa", "Alliance française Ottawa and FrancoLangues; strict test-day rules."),
          ("/en/tcf-canada-montreal/", "TCF Canada in Montreal", "Seven approved centres, plus Laval, Kirkland and Saint-Constant.")],
    sources="the website of the Alliance française de Toronto (TCF page and registration calendar), checked on 17 September 2026.",
))

# ===========================================================================
# MONTREAL
# ===========================================================================
PAGES.append(canada(
    "tcf-montreal", slug="tcf-canada-montreal",
    crumb="TCF Canada in Montreal",
    title="TCF Canada in Montreal: 7 test centres, fees, registration",
    desc="Montreal’s 7 approved TCF test centres with contacts — Alliance Française, Stanislas, UQAM, Concordia… — and their rules (unpublished fees, cancellation).",
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
    stats=[("{n}", "approved centres", "FEI list of 19 September 2026"), ("{so}", "computer-based", "all centres in the city"),
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
<p>For the whole country — the 47 approved centres, province by province, with contacts — see
<a href="/en/tcf-canada-test-centres/">TCF Canada test centres in Canada</a>.</p>"""),
    ],
    list_title="The {n} approved centres in Montreal",
    faq=[("Where can I take the TCF Canada in Montreal?", "At one of the seven approved centres — Alliance Française de Montréal, Collège Stanislas, UQAM, Concordia University, Cégep Marie-Victorin, Centre Yves-Thériault, Collège ELC — or in the suburbs, in Laval, Kirkland and Saint-Constant, all computer-based. You register online, centre by centre."),
         ("How much does the TCF Canada cost in Montreal?", "Montreal’s main centres don’t publish their fees: the Alliance Française de Montréal posts no price, and the amount appears when you book. For reference: $440 at UQTR, $390 at the Alliance française in Vancouver, $400 in Edmonton."),
         ("Can I cancel or reschedule a TCF session in Montreal?", "At the Alliance Française, one change is allowed more than 15 days ahead, and $75 is kept if you cancel; nothing is refunded after that. At Collège Stanislas, rescheduling is free more than 15 days ahead, and $15 per test is kept on cancellation. And whichever centre you choose, allow at least 20 days between two attempts."),
         ("TCF Canada or TCF Québec in Montreal?", "The same centres offer both. For a federal application — Express Entry, citizenship — only the TCF Canada is accepted; for a Quebec program, the TCF Québec, which is modular, lets you take only the required tests.")],
    also=[("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 47 approved centres, province by province, with contacts."),
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
    title="TCF Canada in Quebec City: Stanislas and Université Laval",
    desc="The 2 approved TCF test centres in Quebec City with contacts — Collège Stanislas (Sainte-Foy) and Université Laval — their rules and how to register.",
    h1="Taking the TCF in Quebec City: the two approved centres and registration",
    intro="""In Quebec City, you can take the TCF at <strong>{n} centres approved</strong> by France Éducation international, both
computer-based: <strong>Collège Stanislas</strong> (Sainte-Foy) and the <strong>École de langues de l’Université Laval</strong>.
They offer the TCF Canada and the TCF Québec — check which box you tick: only the TCF Canada counts for Express
Entry. Below: the centres, their contacts, the rules we found, and how to register.""",
    facts=["<strong>{n} approved centres</strong>: Collège Stanislas (1605, chemin Sainte-Foy) and Université Laval (Pavillon Charles-De Koninck).",
           "<strong>Collège Stanislas</strong>: Québec, Canada, tout public, IRN; $15 per test kept if you cancel more than 15 days ahead; 20 days between two attempts.",
           "Other centres in the province: Trois-Rivières (UQTR, $440), Chicoutimi, Sherbrooke, Rouyn-Noranda, Gaspé, Sept-Îles, Baie-Comeau…",
           "Results by email within 2 to 4 weeks; results certificate valid for 2 years.",
           "The TCF Canada has also been recognized by the MIFI since 2022."],
    stats=[("{n}", "approved centres", "FEI list of 19 September 2026"), ("{so}", "computer-based", "all centres in the city"),
           ("checked", "17 Sept 2026", "prices and dates read on the websites"), ("2 years", "validity", "20 to 30 days between two attempts")],
    sections=[
        ("what-we-found", "What we found, centre by centre", releve([
            ("Collège Stanislas (Quebec City)", "Québec, Canada, tout public, IRN", NR,
             "Full payment at registration; free rescheduling more than 15 days ahead; $15 per test on cancellation; 20 days between two attempts."),
            ("Université Laval (ELUL)", NR, NR, "The École de langues’ “tests de langues” page."),
        ], "en-CA", "What each centre’s website showed on 17 September 2026. “No data”: not published, or not checked — the centre’s website is the reference.")),
        ("registration", "How to register in Quebec City", """<p>In Canada, each centre handles its own registrations
<strong>online, on its own website</strong>, with the passport you’ll use for your IRCC application. Registration is
final, and cancelling costs money: the Alliance Française de Montréal keeps $75 if you cancel more than 15 days ahead,
and refunds nothing after that. In the big cities, sessions <strong>fill up within minutes</strong>: create your
account in advance and log in the moment registration opens. Allow at least <strong>20 days</strong> between two
attempts, whichever centre you test at. Results arrive by email within 2 to 4 weeks and are valid for two years. On
test day, bring a valid passport and your printed test-day notice (admission letter).</p>
<p>For the whole country — the 47 approved centres, province by province, with contacts — see
<a href="/en/tcf-canada-test-centres/">TCF Canada test centres in Canada</a>.</p>"""),
    ],
    list_title="The {n} approved centres in Quebec City",
    faq=[("Where can I take the TCF Canada in Quebec City?", "At Collège Stanislas in Quebec City (Sainte-Foy) or at Université Laval, both approved and computer-based; you register online, on their websites."),
         ("How much does the TCF cost in Quebec City?", "Neither centre posts a clear fee on the page we checked; at UQTR, in Trois-Rivières, the TCF Canada costs $440 and the TCF Québec $105 to $125 per test (30 July 2026)."),
         ("TCF Canada or TCF Québec in Quebec City?", "For a Quebec program, both are accepted; for Express Entry or citizenship, only the TCF Canada. The TCF Québec lets you take only the required tests.")],
    also=[("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 47 approved centres, province by province, with contacts."),
          ("/en/tcf-canada-montreal/", "TCF Canada in Montreal", "Seven approved centres, plus Laval, Kirkland and Saint-Constant."),
          ("/en/tcf-canada-ottawa/", "TCF Canada in Ottawa", "Alliance française Ottawa and FrancoLangues; strict test-day rules.")],
    sources="the websites of Collège Stanislas and of Université Laval’s École de langues, checked on 17 September 2026.",
))

# ===========================================================================
# OTTAWA
# ===========================================================================
PAGES.append(canada(
    "tcf-ottawa", slug="tcf-canada-ottawa",
    crumb="TCF Canada in Ottawa",
    title="TCF Canada in Ottawa: Alliance française and FrancoLangues",
    desc="The 2 approved TCF test centres in Ottawa with contacts — Alliance française Ottawa (paper or computer), FrancoLangues — test-day rules and registration.",
    h1="Taking the TCF Canada in Ottawa: the two approved centres and registration",
    intro="""In Ottawa, you can take the TCF Canada at <strong>{n} centres approved</strong> by France Éducation international,
both computer-based: the <strong>Alliance française Ottawa</strong> (352 MacLaren Street), which also offers it on
paper, and <strong>FrancoLangues</strong> in Kanata. The Alliance is strict on test day — a valid passport and the
printed test-day notice, with no exceptions — and sends results by email within two to three weeks. Below: the
centres, their contacts, and how to register.""",
    facts=["<strong>{n} approved centres</strong>: Alliance française Ottawa and FrancoLangues (Kanata).",
           "<strong>Alliance française Ottawa</strong>: TCF Canada computer-based or paper-based; a valid passport and the printed test-day notice are mandatory, with no exceptions.",
           "Results by email within 2 to 3 weeks; no duplicate of the results certificate.",
           "Accommodations: request them before you register, with medical documentation.",
           "FEI has dropped re-marking for sessions held since 1 September 2026."],
    stats=[("{n}", "approved centres", "FEI list of 19 September 2026"), ("{so}", "computer-based", "all centres in the city"),
           ("checked", "17 Sept 2026", "prices and dates read on the websites"), ("2 years", "validity", "20 to 30 days between two attempts")],
    sections=[
        ("what-we-found", "What we found, centre by centre", releve([
            ("Alliance française Ottawa", "Canada (computer or paper-based), other versions", NR,
             "Passport + printed test-day notice mandatory; identity checked during the test; results in 2–3 weeks."),
            ("FrancoLangues", NR, NR, "On the centre’s website."),
        ], "en-CA", "What each centre’s website showed on 17 September 2026. “No data”: not published, or not checked — the centre’s website is the reference.")),
        ("registration", "How to register in Ottawa", """<p>In Canada, each centre handles its own registrations
<strong>online, on its own website</strong>, with the passport you’ll use for your IRCC application. Registration is
final, and cancelling costs money: the Alliance Française de Montréal keeps $75 if you cancel more than 15 days ahead,
and refunds nothing after that. In the big cities, sessions <strong>fill up within minutes</strong>: create your
account in advance and log in the moment registration opens. Allow at least <strong>20 days</strong> between two
attempts, whichever centre you test at. Results arrive by email within 2 to 4 weeks and are valid for two years. On
test day, bring a valid passport and your printed test-day notice (admission letter).</p>
<p>For the whole country — the 47 approved centres, province by province, with contacts — see
<a href="/en/tcf-canada-test-centres/">TCF Canada test centres in Canada</a>.</p>"""),
    ],
    list_title="The {n} approved centres in Ottawa",
    faq=[("Where can I take the TCF Canada in Ottawa?", "At the Alliance française Ottawa (352 MacLaren Street), computer-based or on paper, or at FrancoLangues in Kanata; both are approved."),
         ("What should I bring on test day in Ottawa?", "A valid passport and your printed test-day notice: the Alliance française refuses entry without both, with no exceptions, and checks identity throughout the test."),
         ("How much does the TCF Canada cost in Ottawa?", "The Alliance française Ottawa doesn’t publish the fee on its TCF page; for reference: $390 in Vancouver, $400 in Edmonton, $440 at UQTR.")],
    also=[("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 47 approved centres, province by province, with contacts."),
          ("/en/tcf-canada-montreal/", "TCF Canada in Montreal", "Seven approved centres, plus Laval, Kirkland and Saint-Constant."),
          ("/en/tcf-canada-toronto/", "TCF Canada in Toronto", "Five centres, quarterly sessions, registration at 10 am a month before.")],
    sources="the website of the Alliance française Ottawa (TCF page and test-day rules), checked on 17 September 2026.",
))

# ===========================================================================
# VANCOUVER
# ===========================================================================
PAGES.append(canada(
    "tcf-vancouver", slug="tcf-canada-vancouver",
    crumb="TCF Canada in Vancouver",
    title="TCF Canada in Vancouver: test centres, $390 fee, booking",
    desc="The 3 approved TCF test centres in Vancouver and New Westminster — Alliance française Canada Pacific ($390), Ashton — and test dates that sell out fast.",
    h1="Taking the TCF Canada in Vancouver: the approved centres, the fee and registration",
    intro="""In Vancouver, you can take the TCF Canada at <strong>{n} centres approved</strong> by France Éducation international,
all computer-based: the <strong>Alliance française Canada Pacific</strong> — on Cambie Street, with a second site in
New Westminster — and Ashton Testing Services. The Alliance charges <strong>$390</strong>, with 10% off for members
and no refunds, and on 17 September 2026 <strong>every session it listed was “SOLD OUT”</strong>. Below: the
centres, their contacts, and how to get a seat.""",
    facts=["<strong>{n} approved centres</strong>: Alliance française Canada Pacific (Vancouver and New Westminster), Ashton Testing Services.",
           "<strong>Alliance française: $390</strong>, 10% off for members; online registration only, and final — no refund, no credit.",
           "Every listed session “SOLD OUT” on 17 September 2026: log in when registration opens, in a single tab, with your passport at hand.",
           "Results by email within 3 to 4 weeks; QWERTY keyboard, accents through FEI’s platform.",
           "Victoria has two more approved centres (Alliance française de Victoria, University of Victoria)."],
    stats=[("{n}", "approved centres", "FEI list of 19 September 2026"), ("{so}", "computer-based", "all centres in the area"),
           ("checked", "17 Sept 2026", "prices and dates read on the websites"), ("2 years", "validity", "20 to 30 days between two attempts")],
    sections=[
        ("what-we-found", "What we found, centre by centre", releve([
            ("Alliance française Canada Pacific", "Canada (+ TEF)", "<strong>$390</strong> ($351 for members)",
             "Online registration only, final; sessions full; results in 3–4 weeks; QWERTY."),
            ("Ashton Testing Services", NR, NR, "Private testing centre, computer-based."),
        ], "en-CA", "What each centre’s website showed on 17 September 2026. “No data”: not published, or not checked — the centre’s website is the reference.")),
        ("registration", "How to book the TCF Canada in Vancouver", """<p>In Canada, each centre handles its own registrations
<strong>online, on its own website</strong>, with the passport you’ll use for your IRCC application. Registration is
final, and cancelling costs money: the Alliance Française de Montréal keeps $75 if you cancel more than 15 days ahead,
and refunds nothing after that. In the big cities, sessions <strong>fill up within minutes</strong>: create your
account in advance and log in the moment registration opens. Allow at least <strong>20 days</strong> between two
attempts, whichever centre you test at. Results arrive by email within 2 to 4 weeks and are valid for two years. On
test day, bring a valid passport and your printed test-day notice (admission letter).</p>
<p>For the whole country — the 47 approved centres, province by province, with contacts — see
<a href="/en/tcf-canada-test-centres/">TCF Canada test centres in Canada</a>.</p>"""),
    ],
    list_title="The {n} approved centres in Vancouver and New Westminster",
    faq=[("Where can I take the TCF Canada in Vancouver?", "At the Alliance française Canada Pacific (6161 Cambie Street, and New Westminster) or at Ashton Testing Services, all approved and computer-based; you register online, centre by centre."),
         ("How much does the TCF Canada cost in Vancouver?", "$390 at the Alliance française Canada Pacific on 17 September 2026 ($351 for members), and “prices are subject to change without notice”; Ashton doesn’t publish a clear fee."),
         ("How do I get a TCF Canada test date in Vancouver?", "By registering the moment registration opens: the Alliance advises logging in ahead of time with your passport number ready and opening a single tab — “opening multiple tabs or repeatedly refreshing the page may cancel your reservation”.")],
    also=[("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 47 approved centres, province by province, with contacts."),
          ("/en/tcf-canada-toronto/", "TCF Canada in Toronto", "Five centres, quarterly sessions, registration at 10 am a month before."),
          ("/en/tcf-canada-montreal/", "TCF Canada in Montreal", "Seven approved centres, plus Laval, Kirkland and Saint-Constant.")],
    sources="the websites of the Alliance française Canada Pacific and Ashton Testing Services, checked on 17 September 2026.",
))


# ===========================================================================
# INDIA (FEI list and centre websites read on 8 October 2026)
# ===========================================================================
_CA = [("ok", "TCF Canada")]
PAGES.append(dict(
    lang="en", variant="en-GB", og_locale="en_IN", fr_path="/centres/tcf-inde/", slug="tcf-canada-india",
    country_name="India", exam="tcf", file="tcf_inde", layout="cities",
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
    facts=["<strong>{n} approved centres</strong> (FEI list of 8 October 2026), all Alliances Françaises; <strong>5 offer the TCF Canada</strong>: New Delhi, Kolkata, Ahmedabad, Bangalore and Bhopal.",
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
# UNITED ARAB EMIRATES (no French equivalent page: no hreflang)
# ===========================================================================
PAGES.append(dict(
    lang="en", variant="en-GB", og_locale="en_AE", fr_path=None, slug="tcf-canada-dubai",
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
cancellation or re-marking rule. The TCF row of its calendar lists only the Abu Dhabi centre.</p>"""),
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
    sources="the websites of the Alliance Française de Dubai (Canada immigration exams page, TCF Canada booking page, September–December 2026 calendar) and of the Alliance Française Abu Dhabi (TCF page, TCF Canada booking page, 2026 exam calendar), checked on 8 October 2026.",
    badges={"abou-dhabi-french-ambassy-institut-francais-antenne-afad": _CA,
            "dubai-alliance-francaise-de-dubai-centre-1": _CA, "dubai-alliance-francaise-de-dubai-centre-2": _CA,
            "al-ain-alliance-francais-d-abu-dhabi-antenne-al-ain": [("part", "TCF not listed at Al Ain")]},
    urls={"abou-dhabi-french-ambassy-institut-francais-antenne-afad": "https://www.afabudhabi.org/tcf/",
          "dubai-alliance-francaise-de-dubai-centre-1": "https://www.afdubai.org/canada-immigration-exams-alliance-francaise-dubai/tcf-canada-exam/",
          "dubai-alliance-francaise-de-dubai-centre-2": "https://www.afdubai.org/canada-immigration-exams-alliance-francaise-dubai/tcf-canada-exam/"},
))


# ===========================================================================
# /en/ — landing page (make_pays.hub("en")). Figures taken from each country page.
# ===========================================================================
def _hub_table():
    from pays_i18n import table
    fei_ca_delf = "https://www.france-education-international.fr/centres-d-examen/liste?pays=112&type-centre=delf_dalf"
    rows = [("Canada", '<a href="/en/tcf-canada-test-centres/">47 centres, $390 to $440</a> — <a href="/en/tcf-canada-toronto/">Toronto</a>, '
                       '<a href="/en/tcf-canada-montreal/">Montreal</a>, <a href="/en/tcf-canada-vancouver/">Vancouver</a>, '
                       '<a href="/en/tcf-canada-ottawa/">Ottawa</a>, <a href="/en/tcf-canada-quebec-city/">Quebec City</a>',
             f'<a href="{fei_ca_delf}" rel="noopener">FEI’s official list</a>'),
            ("United States", '<a href="/en/tcf-canada-usa/">9 of 18 centres, US$330 to US$460</a>', '<a href="/en/delf-usa/">40 centres, B2 US$190</a>'),
            ("United Kingdom", '<a href="/en/tcf-canada-uk/">London £260, Glasgow £325</a>', '<a href="/en/delf-uk/">11 centres, B2 £160</a>'),
            ("India", '<a href="/en/tcf-canada-india/">5 Alliances, ₹26,000</a>', "—"),
            ("United Arab Emirates", '<a href="/en/tcf-canada-dubai/">Dubai and Abu Dhabi, 1,800 AED</a>', "—")]
    return table("The TCF Canada and the DELF-DALF, from each centre’s website (Canada: 17 September 2026; United States, "
                 "United Kingdom, India and the UAE: 8 October 2026). Fees in local currency, for an individual candidate.",
                 ["Country", "TCF Canada", "DELF · DALF"], [(f"<strong>{p}</strong>", a, b) for p, a, b in rows], wide=False)


HUB = dict(
    variant="en-CA", accent="accent-tcf", crumb="Test centres", read=3,
    title="TCF Canada & DELF test centres: Canada, USA, UK (2026)",
    desc="Where to take the TCF Canada or the DELF in Canada, the United States and the United Kingdom: approved test centres, fees and dates, checked in 2026.",
    h1="TCF Canada and DELF test centres in Canada, the US and the UK",
    lang_links='<p class="langs"><a href="/es/" hreflang="es" lang="es">En español</a> · <a href="/centres/" hreflang="fr" lang="fr">En français</a></p>',
    intro="""For the <strong>TCF Canada</strong> — one of the two French tests IRCC accepts — and for the
<strong>DELF</strong> and <strong>DALF</strong> diplomas, each page lists the test centres approved by France
Éducation international in one country or city, what each centre’s website showed when we checked — fees, dates,
versions — and how to register. Canada: all 47 centres, plus Toronto, Montreal, Vancouver, Ottawa and Quebec City.
The United States and the United Kingdom: the TCF Canada and the DELF.""",
    facts=["<strong>Canada: 47 approved TCF centres</strong> in nine provinces and Nunavut (FEI list of 19 September 2026); fees seen: $390 (Alliance française, Vancouver), $400 (Alliance française, Edmonton), $440 (UQTR).",
           "⚠️ Sessions in Toronto and Vancouver <strong>fill up within minutes</strong>: register the moment bookings open.",
           "<strong>United States</strong>: 9 of the 18 approved TCF centres offer the TCF Canada, for US$330 to US$460 (8 October 2026).",
           "<strong>United Kingdom</strong>: the TCF Canada at the Institut français in London (£260) and the Alliance française de Glasgow (£325); when we checked on 8 October 2026, the earliest free seat in London was on 23 April 2027.",
           "<strong>India</strong>: 5 Alliances Françaises offer the TCF Canada (₹26,000 where published); <strong>UAE</strong>: Dubai and Abu Dhabi, 1,800 AED.",
           "A DELF or DALF diploma is valid for life; TCF Canada results, for two years."],
    toc=[("countries", "Where to take the exams"), ("prepare", "Prepare for the TCF Canada"), ("tcf-canada", "TCF Canada"),
         ("delf", "DELF and DALF"), ("france", "Living in France")],
    body="""
<div class="stats">
<div class="stat"><b>47</b><span>TCF centres in Canada</span><em>nine provinces and Nunavut</em></div>
<div class="stat"><b>9 of 18</b><span>US centres</span><em>offer the TCF Canada</em></div>
<div class="stat"><b>£260</b><span>TCF Canada in London</span><em>earliest free seat: 23 April 2027</em></div>
</div>

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
    faq=[("Where can I take the TCF Canada in Canada?", "At one of the 47 centres approved by France Éducation international, in nine provinces and Nunavut — 23 in Quebec (7 in Montreal), 7 in Ontario, 5 in British Columbia, 3 in Alberta. Sessions in Toronto and Vancouver fill up within minutes: register the moment bookings open."),
         ("How much does the TCF Canada cost?", "There is no national fee. In Canada: $390 at the Alliance française in Vancouver, $400 in Edmonton, $440 at UQTR. In the United States: US$330 to US$460. In the United Kingdom: £260 in London, £325 in Glasgow."),
         ("TCF Canada or DELF: which one do I need?", "For Canadian immigration, IRCC accepts two French tests: the TCF Canada and the TEF Canada, with results valid for two years. The DELF and DALF are diplomas, passed level by level and valid for life."),
         ("Can I take the TCF Canada at any TCF centre?", "No: a centre approved for the TCF doesn’t necessarily offer the Canada version — in the United States, Atlanta, Chicago, Seattle and Washington don’t. Each page shows which centres advertised it on their website.")],
    also=[("/es/", "TCF Canada y DELF en español", "Spain and Latin America: seven countries, fourteen pages."),
          ("/ou-passer/", "All countries (in French)", "1,067 centres in 35 countries, with their contact details."),
          ("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 47 approved centres, province by province.")],
    sources="""<strong>Sources.</strong> France Éducation international’s lists of exam centres (by country; types “TCF”
and “DELF-DALF”), read on 19 September 2026 for Canada and on 8 October 2026 for the United States and the United
Kingdom, and the websites of the centres named on each page, checked on 17 September 2026 (Canada) and 8 October
2026. Fees and dates change without notice: check them on the centre’s website before paying.""",
    cta_h2="The centre gives you the date; the score is up to you",
    cta_p="""You pay the full fee for each session, and you can’t retake the test right away. The mock exams in the
“TCF DELF TEF: Tests 2026” app follow the official format of each test — TCF Canada, TCF Québec, DELF B2 — scored
like the real thing, with AI feedback on writing and speaking.""",
)
