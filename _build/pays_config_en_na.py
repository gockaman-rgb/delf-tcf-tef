# -*- coding: utf-8 -*-
"""English city and province pages for North America (26/10/2026): searches with no page yet.

Search Console, 7 days to 24/10/2026: «tcf canada detroit» (pos. 5.9), «tcf canada seattle», «houston», «san francisco»,
«tcf alberta» (31 impressions), «tcf lethbridge», «tcf canada edmundston», «in moncton», «tcf exam centres in ontario»,
«tcf north york», «tcf kanata». Hooked into pays_config_en.PAGES by one line at the end of pays_config_en.py.

Facts: each centre's own website and booking page, read on 26 October 2026 (Claude in Chrome for the booking widgets of
Detroit, Halifax, Moncton, the CCNB, Ottawa, Vancouver and GB Language Centre); FEI lists of 26 October 2026
(data/fei_monde/tcf_canada.json, tcf_etats_unis.json — same centres as 8/10 and 19/09, plus Collège Boréal in Windsor).
Earlier facts kept with their own date (Houston's weekly sessions and fee, 8/10/2026). Notes: scratchpad research.md.
"""
PAGES = []    # défini avant l'import : pays_config_en importe ce module à sa dernière ligne

from pays_config_en import NR, _CAN, _PRACTICE, _US, _city_page  # noqa: E402
from pays_i18n import releve  # noqa: E402

US_FILE, CA_FILE = "fei_monde/tcf_etats_unis", "fei_monde/tcf_canada"
US_LIST, CA_LIST = "October 26, 2026", "26 October 2026"


def _page(*args, **kw):
    """_city_page (pays_config_en), daté du 26/10/2026 au lieu du 18/10."""
    extra = {k: kw.pop(k) for k in ("list_intro", "notes") if k in kw}
    d = _city_page(*args, **kw)
    d.update(extra)
    us = d["variant"] == "en-US"
    d.update(published="2026-10-26", date_label=US_LIST if us else CA_LIST, releve_date=US_LIST if us else CA_LIST)
    return d


_OK = [("ok", "TCF Canada")]
_OPEN = _OK + [("ok", "dates open")]
_TEF_US = ("/en/tcf-vs-tef-canada/", "TCF vs TEF Canada", "The two French tests IRCC accepts, side by side.")
_ALBERTA = ("/en/tcf-canada-alberta/", "TCF Canada in Alberta", "Calgary and Edmonton, $400; Lethbridge DELF only.")
_NB = ("/en/tcf-canada-new-brunswick/", "TCF Canada in New Brunswick", "$390 in Moncton, Edmundston and Bathurst — seats open.")
_ONTARIO = ("/en/tcf-canada-ontario/", "TCF Canada in Ontario", "Toronto, North York, Ottawa: $390 to $452, next dates.")

# ============================================================================ UNITED STATES
# ---------------------------------------------------------------------------- DETROIT
DET = "detroit-bingham-farms-alliance-francaise-detroit-french-institute"
PAGES.append(_page(
    "tcf-canada-detroit", US_FILE, "en-US", "en_US", "United States", ["Detroit (Bingham Farms)"], "Detroit", US_LIST,
    title="TCF Canada in Detroit: $330, sessions full until June 2027",
    desc="TCF Canada at the Alliance française de Détroit (Bingham Farms, MI): $330, on computer; every session to May 13, 2027 full, June 10 open. Booking.",
    h1="TCF Canada in Detroit: the Alliance française, the fee and the 2027 dates",
    intro="""Near Detroit, the TCF Canada is held by the <strong>Alliance française de Détroit</strong> — the French Institute
of Michigan — at 30800 Telegraph Road in Bingham Farms, the only approved TCF center in Michigan. It costs
<strong>$330</strong>, the lowest fee we have found in the United States, and is taken on computer. On October 26, 2026,
its booking page showed <strong>every session full until May 13, 2027</strong> — November 12, December 10, then one
Thursday a month — and <strong>June 10, 2027</strong> as the only open date. When a date is full, the Alliance asks you
to write: it can sometimes add exam slots.""",
    facts=["<strong>{n} approved center</strong> in Michigan: the Alliance française de Détroit / French Institute of Michigan, 30800 Telegraph Rd, Suite 2925, Bingham Farms.",
           "TCF Canada <strong>$330</strong> on October 26, 2026 — the same as on October 8; on computer, except the speaking test.",
           "⚠️ <strong>Full</strong>: Nov 12 and Dec 10, 2026, Jan 14, Feb 11, Mar 11, Apr 15 and May 13, 2027. <strong>Open: June 10, 2027.</strong>",
           "Registration deadlines: Oct 29 for Nov 12, Nov 26 for Dec 10, Jan 5 for Jan 14, Feb 1 for Feb 11, Mar 1 for Mar 11.",
           "20 days between two attempts; certificate within 10 days, valid two years."],
    stats=[("$330", "TCF Canada", "on computer"), ("Jun 10", "next open date", "2027"),
           ("7", "sessions full", "Nov 2026 to May 2027"), ("10 days", "for the certificate", "valid two years")],
    sections=[("booking", "Booking the TCF Canada in Detroit", """<p>The Alliance sells its sessions on a <strong>TCF exam
registration</strong> page (afdetroit.org/tcf-exams), linked from its TCF page: each date shows its price and either
«Full» or «Add to cart», and you can also pay at the office. Choose the TCF Canada: «You CANNOT take the TCF IRN or TP for
immigration purposes (it will NOT be accepted by IRRC)», the page warns. When a date is full, write to afd@afdetroit.org —
«We are sometimes able to add exam slots». Cancellation more than ten business days before the test is refunded minus a
$40 fee; after that, only a documented illness or emergency, sent within a month, can lead to a new date, if France
Éducation international approves it.</p>

<p>If June is too late, compare the other U.S. centers on our <a href="/en/tcf-canada-usa/">USA page</a>: on October 26,
2026, Pluma Academy in <a href="/en/tcf-canada-denver/">Denver</a> ($435) listed sessions on most weekdays until March
2027, while <a href="/en/tcf-canada-san-francisco/">San Francisco</a> had only a waitlist. Chicago, the nearest big city,
has no TCF Canada — only the <a href="/en/tcf-canada-chicago/">TEF Canada</a>, which IRCC also accepts.</p>""")],
    faq=[("Where can I take the TCF Canada in Detroit?", "At the Alliance française de Détroit (French Institute of Michigan), 30800 Telegraph Road, Suite 2925, in Bingham Farms — the only approved TCF center in Michigan. The test is on computer, except the speaking part."),
         ("When is the next TCF Canada in Detroit?", "On October 26, 2026, every session until May 13, 2027 was full (November 12, December 10, then January 14, February 11, March 11, April 15 and May 13); June 10, 2027 was open. The Alliance sometimes adds slots: ask at afd@afdetroit.org."),
         ("How much does the TCF Canada cost in Detroit?", "$330 at the Alliance française de Détroit (October 26, 2026). A cancellation more than ten business days before the test is refunded minus $40."),
         ("Can I take the TCF IRN or tout public in Detroit for Canada?", "No: the Alliance warns that the TCF IRN and the TCF tout public are not accepted by IRCC. For Express Entry or citizenship, book the TCF Canada.")],
    also=[_US, ("/en/tcf-canada-chicago/", "TCF Canada in Chicago", "No TCF Canada: the TEF Canada, $415."), _PRACTICE],
    sources="the Alliance française de Détroit's TCF page and its TCF exam registration page (afdetroit.org), checked on October 26, 2026.",
    badges={DET: [("ok", "TCF Canada"), ("part", "full until June 2027")]},
    urls={DET: "https://www.afdetroit.org/exam-center/tcf-french-exams/"}))

# ---------------------------------------------------------------------------- HOUSTON
HOU = "houston-alliance-francaise"
PAGES.append(_page(
    "tcf-canada-houston", US_FILE, "en-US", "en_US", "United States", ["Houston"], "Houston", US_LIST,
    title="TCF Canada in Houston: $400, dates, and the TEF Canada",
    desc="TCF Canada at the Alliance Française de Houston: $400 and weekly dates on October 8; none listed on October 26. TEF Canada $380, seats open to January.",
    h1="TCF Canada in Houston: the Alliance Française, the fee, the dates — and the TEF Canada",
    intro="""In Houston, the TCF Canada is held by the <strong>Alliance Française de Houston</strong>, 427 Lovett Boulevard,
the only approved TCF center in Texas. On October 8, 2026, it was selling a session <strong>every Wednesday</strong>, ten
seats each, for <strong>$400</strong>, through January 27, 2027. On October 26, its TCF page listed <strong>no session and
no fee</strong> — only the address exams@alliancehouston.org — while its <strong>TEF Canada</strong>, the other French
test IRCC accepts, had seats twice a week for <strong>$380</strong>, from October 30, 2026 to January 18, 2027.""",
    facts=["<strong>{n} approved TCF center</strong> in Texas: the Alliance Française de Houston, 427 Lovett Blvd.",
           "October 8, 2026: TCF Canada <strong>$400</strong>, every Wednesday, ten seats a session, through January 27, 2027; registration closed three days before; on computer.",
           "⚠️ October 26, 2026: the TCF page listed <strong>no session and no fee</strong>; questions go to exams@alliancehouston.org.",
           "<strong>TEF Canada $380</strong>: 14 sessions open from October 30, 2026 to January 18, 2027, on Mondays and Fridays, 1 to 10 seats left each.",
           "«Exam registrations are non-refundable for any reason.»"],
    stats=[("$400", "TCF Canada", "October 8, 2026"), ("0", "TCF sessions listed", "October 26, 2026"),
           ("$380", "TEF Canada", "14 open dates"), ("{n}", "approved TCF center", "in Texas")],
    sections=[("booking", "TCF or TEF Canada in Houston", """<p>Until mid-October, the Alliance published its TCF sessions
on its TCF page — one every Wednesday, ten seats each, registration closing three days before, $400. On October 26,
2026, that page described the four TCF versions (tout public, Canada, Québec, IRN) but listed <strong>no date and no
fee</strong>: write to exams@alliancehouston.org, or call 713-526-1121, to ask when TCF Canada sessions resume.
Whatever you book, «Exam registrations are non-refundable for any reason».</p>

<p>The Alliance's <strong>TEF Canada</strong> page, on the other hand, was selling sessions: $380, on Mondays and Fridays,
from October 30 to December 7, 2026 and from January 8 to 18, 2027, with 1 to 10 seats left. IRCC accepts the TEF Canada
like the TCF Canada, with its own conversion to CLB levels (<a href="/en/tcf-vs-tef-canada/">TCF vs TEF Canada</a>). For
the TCF Canada itself, the other U.S. centers and their fees are on our <a href="/en/tcf-canada-usa/">USA page</a>; Pluma
Academy in <a href="/en/tcf-canada-denver/">Denver</a> listed sessions on most weekdays until March 2027.</p>""")],
    faq=[("Where can I take the TCF Canada in Houston?", "At the Alliance Française de Houston, 427 Lovett Boulevard — the only approved TCF center in Texas."),
         ("When is the next TCF Canada in Houston?", "On October 26, 2026, the Alliance's TCF page listed no session. On October 8 it was selling one every Wednesday through January 27, 2027; ask exams@alliancehouston.org whether those dates still stand."),
         ("How much does the TCF Canada cost in Houston?", "$400 on October 8, 2026; on October 26 the TCF page showed no fee. The TEF Canada cost $380."),
         ("Can I take the TEF Canada in Houston instead?", "Yes: on October 26, 2026, the Alliance had 14 TEF Canada sessions open between October 30 and January 18, 2027, for $380. IRCC accepts both tests.")],
    also=[_US, _TEF_US, _PRACTICE],
    sources="the Alliance Française de Houston's TCF and TEF Canada pages (alliancehouston.org), checked on October 26, 2026; its TCF sessions and fee as published on October 8, 2026.",
    badges={HOU: [("ok", "TCF Canada"), ("part", "no date listed on Oct 26")]},
    urls={HOU: "https://www.alliancehouston.org/certifications-and-exams/tcf-canada-irn-quebec-et-tout-public/"}))

# ---------------------------------------------------------------------------- SAN FRANCISCO
SF = "san-francisco-alliance-francaise"
PAGES.append(_page(
    "tcf-canada-san-francisco", US_FILE, "en-US", "en_US", "United States", ["San Francisco"], "San Francisco", US_LIST,
    title="TCF Canada in San Francisco: $460, waitlist, no 2027 date",
    desc="TCF Canada at the Alliance française de San Francisco, 1345 Bush Street: $460, on computer; November 6 on waitlist and no 2027 date on October 26.",
    h1="TCF Canada in San Francisco: the Alliance française, the fee and the waitlist",
    intro="""In San Francisco, the TCF Canada is held by the <strong>Alliance française de San Francisco</strong>, 1345 Bush
Street — the only approved TCF center in Northern California — for <strong>$460</strong>, «Full exam only», on computer.
On October 26, 2026, its TCF calendar listed the last TCF Canada session of the year, <strong>November 6, on
waitlist</strong>, and <strong>no 2027 date</strong>; the TCF Québec had no date left in 2026. You need a valid passport
to register, and 25 days between two TCF attempts.""",
    facts=["<strong>{n} approved center</strong>: the Alliance française de San Francisco, 1345 Bush Street; exams «in digital format» since October 1, 2022.",
           "TCF Canada <strong>$460</strong>, «Full exam only».",
           "⚠️ October 26, 2026: <strong>November 6 on waitlist</strong>, like August 1, September 4 and September 25; <strong>no 2027 date</strong> listed.",
           "TCF Québec: «Plus de date en 2026» — the Alliance points candidates to the TCF Canada.",
           "Changes: up to 30 days before, a refund minus $60 or a free change; from 30 to 8 days, a change or credit minus $60, no refund; in the last 8 days, none.",
           "25 days between two TCF attempts, whatever the version; results in about two weeks."],
    stats=[("$460", "TCF Canada", "full exam only"), ("Nov 6", "last 2026 date", "on waitlist"),
           ("0", "2027 dates", "on October 26, 2026"), ("25 days", "between two attempts", "any TCF version")],
    sections=[("booking", "Booking the TCF Canada in San Francisco", """<p>The Alliance's TCF Canada page links to its
registration form: you choose the session, fill in the form and pay — the registration counts only once both are in. A
valid passport is required «at the time of registration until after the date of the exam»; no other ID is accepted, and
a lost or expired passport means a new date and the administrative fee. Within eight days of the test nothing can be
changed, and the Alliance allows at most two reschedulings a calendar year. Results come by email about two weeks
after the test.</p>

<p>With November 6 on waitlist and no 2027 date, look elsewhere in California: on October 18, 2026, the Alliance Française
de <a href="/en/tcf-canada-los-angeles/">Los Angeles</a> ($505) listed November 20, December 18 and monthly dates to June
2027, while <a href="/en/tcf-canada-san-diego/">San Diego</a> was sold out. Every U.S. center is on our
<a href="/en/tcf-canada-usa/">USA page</a>.</p>""")],
    faq=[("Where can I take the TCF Canada in San Francisco?", "At the Alliance française de San Francisco, 1345 Bush Street, on computer; it is the only approved TCF center in Northern California."),
         ("When is the next TCF Canada in San Francisco?", "On October 26, 2026, the only remaining date was November 6, on waitlist, and no 2027 session was listed. Los Angeles had dates every month to June 2027 (October 18)."),
         ("How much does the TCF Canada cost in San Francisco?", "$460 for the full exam (October 26, 2026). A refund, minus $60, is possible only up to 30 days before the test."),
         ("How long must I wait between two TCF attempts in San Francisco?", "25 days, «regardless of the version concerned», according to the Alliance's TCF policies.")],
    also=[_US, ("/en/tcf-canada-los-angeles/", "TCF Canada in Los Angeles", "$505, monthly dates to June 2027, and Pasadena."), _PRACTICE],
    sources="the Alliance française de San Francisco's TCF, TCF Canada and TCF policies pages (afsf.com), checked on October 26, 2026.",
    badges={SF: [("ok", "TCF Canada"), ("part", "waitlist, no 2027 date")]},
    urls={SF: "https://www.afsf.com/exams/tcf/canada/"}))

# ---------------------------------------------------------------------------- SEATTLE
SEA, MI = "seattle-alliance-francaise", "mercer-island-french-american-school-of-puget-sound"
PAGES.append(_page(
    "tcf-canada-seattle", US_FILE, "en-US", "en_US", "United States", ["Seattle"], "Seattle", US_LIST,
    title="TCF Canada in Seattle? Not offered: the TEF Canada, $365",
    desc="No TCF Canada in Seattle: the Alliance française runs the TEF Canada ($365), sold out to December 21; 2027 dates due late November. Nearest TCF centers.",
    h1="TCF Canada in Seattle: not offered — the TEF Canada instead, and where to take the TCF",
    intro="""If you are looking for the TCF Canada in Seattle, the answer is no: the <strong>Alliance française de
Seattle</strong>, approved by France Éducation international for the TCF, shows no TCF on its website and offers the
<strong>TEF Canada</strong> instead — the other French test IRCC accepts — for <strong>$365</strong>. On October 26, 2026,
every TEF session from October 30 to December 21 was <strong>sold out</strong>, and the January–March 2027 dates were due
«late November 2026». The other approved center in the area, the French American School of Puget Sound on Mercer
Island, publishes no TCF information.""",
    facts=["Approved TCF centers in the Seattle area: the Alliance française (4649 Sunnyside Ave N) and the French American School of Puget Sound (Mercer Island) — <strong>neither advertises the TCF Canada</strong>.",
           "<strong>TEF Canada $365</strong>, four modules; reading, listening and writing on computer, speaking with an examiner.",
           "⚠️ October 26, 2026: every TEF Canada session from <strong>October 30 to December 21</strong> sold out; «January to March 2027 dates will be published late November 2026».",
           "20 days between two TEF registrations; results by email about 1 to 10 days after the exam.",
           "Nearest TCF Canada on October 26: Vancouver ($390, December sold out), San Francisco ($460, waitlist), Pluma Academy in Denver ($435)."],
    stats=[("0", "TCF Canada sessions", "in Seattle"), ("$365", "TEF Canada", "4 modules"),
           ("late Nov", "2027 TEF dates due", "January to March"), ("20 days", "between two TEF sessions", "the Alliance's rule")],
    sections=[("tef-or-tcf", "TEF Canada in Seattle, or the TCF Canada elsewhere", """<p>For Express Entry or Canadian
citizenship, IRCC accepts <strong>either</strong> the TCF Canada or the TEF Canada; the score tables differ, but both
convert to CLB levels (<a href="/en/tcf-vs-tef-canada/">TCF vs TEF Canada</a>). In Seattle, only the TEF Canada is on
offer, at the Alliance française: $365 for the four modules, with reading, listening and writing on computer and the
speaking test with an examiner. On October 26, 2026, its sessions from October 30 to December 21 were all sold out; the
January–March 2027 dates were to be published in late November, so watch the page then.</p>

<p>If you have prepared for the TCF Canada specifically, the nearest centers on October 26 were across the border in
<a href="/en/tcf-canada-vancouver/">Vancouver</a> ($390, December sold out) and in
<a href="/en/tcf-canada-san-francisco/">San Francisco</a> ($460, waitlist); Pluma Academy in
<a href="/en/tcf-canada-denver/">Denver</a> ($435) listed sessions on most weekdays to March 2027. Every U.S. center is on
our <a href="/en/tcf-canada-usa/">USA page</a>.</p>""")],
    faq=[("Can I take the TCF Canada in Seattle?", "No: on October 26, 2026, the Alliance française de Seattle showed no TCF on its website and offered the TEF Canada instead; the French American School of Puget Sound, on Mercer Island, publishes no TCF information."),
         ("How much does the TEF Canada cost in Seattle?", "$365 for the four modules at the Alliance française de Seattle (October 26, 2026)."),
         ("When is the next TEF Canada in Seattle?", "Every session from October 30 to December 21, 2026 was sold out on October 26; the January–March 2027 dates were due in late November 2026."),
         ("Where is the nearest TCF Canada center to Seattle?", "The Alliance française in Vancouver ($390; December sold out on October 26, 2026); in the United States, San Francisco ($460, waitlist) or Pluma Academy in Denver ($435).")],
    also=[_US, _TEF_US, ("/en/tef-canada-practice-test/", "TEF Canada practice test", "The format, with exercises.")],
    sources="the Alliance française de Seattle's exam center and TEF pages (afseattle.org) and the French American School of Puget Sound's website, checked on October 26, 2026.",
    badges={SEA: [("no", "no TCF Canada")], MI: [("no", "no TCF on its website")]},
    urls={SEA: "https://www.afseattle.org/exam-center/tef/"},
    nearby=["Mercer Island"], list_title="The approved TCF centers in the Seattle area"))

# ---------------------------------------------------------------------------- DENVER
DEN, PLU = "denver-alliance-francaise", "denver-pluma-academy"
PAGES.append(_page(
    "tcf-canada-denver", US_FILE, "en-US", "en_US", "United States", ["Denver"], "Denver", US_LIST,
    title="TCF Canada in Denver: Pluma Academy $435, Alliance $360",
    desc="TCF Canada in Denver: the Alliance française ($360) is sold out to December; Pluma Academy ($435) lists sessions most weekdays to March 2027. Booking.",
    h1="TCF Canada in Denver: the Alliance française, Pluma Academy, the fees and the dates",
    intro="""Denver has <strong>two approved TCF Canada centers</strong>: the <strong>Alliance française de Denver</strong>,
at $360, and <strong>Pluma Academy</strong>, at $435. On October 26, 2026, the Alliance's three remaining sessions —
November 16, November 30 and December 7 — were <strong>sold out</strong>, with no 2027 date yet, while Pluma Academy
listed sessions on most weekdays from October 30 to March 27 and calls candidates back within 24 hours of registering.
Both test on computer.""",
    facts=["<strong>{n} approved centers</strong>: the Alliance française de Denver (7701 E 1st Place) and Pluma Academy (940 Fillmore Street).",
           "Alliance française: TCF Canada <strong>$360</strong>; ⚠️ November 16, November 30 and December 7, 2026 <strong>sold out</strong>; no 2027 date; dates posted about two months ahead; free waitlist.",
           "Pluma Academy: TCF Canada <strong>$435</strong> on computer ($70 more on paper); dates listed from October 30, 2026 to March 27, 2027, about twenty a month from January.",
           "Waiting period: 30 days at the Alliance, 21 days at Pluma Academy.",
           "No refund at either center once registered; the Alliance keeps $50 if it approves an exception."],
    stats=[("$360", "Alliance française", "sold out to December"), ("$435", "Pluma Academy", "on computer"),
           ("~20", "Pluma dates a month", "January to March 2027"), ("{n}", "approved centers", "in Denver")],
    sections=[
        ("tcf-canada-centers", "The two centers, side by side", releve([
            ("Alliance française de Denver", "<strong>Canada</strong>; IRN and tout public on request", "<strong>$360</strong>",
             "Nov 16, Nov 30 and Dec 7, 2026 <strong>sold out</strong>; no 2027 date; deadline seven business days before; 30 days between two tests; computer-based."),
            ("Pluma Academy", "<strong>Canada</strong>, IRN, tout public", "<strong>$435</strong> (paper: +$70)",
             "Dates listed from Oct 30, 2026 to Mar 27, 2027 — about twenty a month from January; callback within 24 hours; 21 days between two sessions; results in 8 to 10 days."),
        ], "en-US", "What each center's website showed on October 26, 2026. Pluma Academy's list doesn't say which dates are still free: the center confirms after you register.")),
        ("booking", "Booking in Denver", """<p>At the <strong>Alliance française</strong>, you register for a TCF Canada
session in its online exam selector and pay; the TCF IRN and tout public are on request by email. Exam dates appear
about two months before the test, and a full session has a free waiting list. The name you give must match your
passport exactly, and «There is no refund once the test is purchased». At <strong>Pluma Academy</strong>, you click
«Register Now» on its TCF page, read its exam policy, and the center calls you within 24 hours to fix the details; «No
refund will be made or credit given once the registration is processed». Pluma tests on computer, or on paper for $70
more, with results in eight to ten days on computer. For the other states, see our <a href="/en/tcf-canada-usa/">USA
page</a>.</p>""")],
    faq=[("Where can I take the TCF Canada in Denver?", "At the Alliance française de Denver (7701 E 1st Place) or at Pluma Academy (940 Fillmore Street); both are approved by France Éducation international and test on computer."),
         ("When is the next TCF Canada in Denver?", "On October 26, 2026, the Alliance française's sessions of November 16, November 30 and December 7 were sold out, with no 2027 date; Pluma Academy listed dates on most weekdays from October 30 to March 27, 2027."),
         ("How much does the TCF Canada cost in Denver?", "$360 at the Alliance française and $435 at Pluma Academy, on computer ($70 more on paper there), on October 26, 2026."),
         ("How long between two attempts in Denver?", "30 days at the Alliance française, 21 days at Pluma Academy.")],
    also=[_US, ("/en/tcf-canada-houston/", "TCF Canada in Houston", "$400 on October 8; the TEF Canada at $380."), _PRACTICE],
    sources="the Alliance française de Denver's exams, TCF and exam selector pages (afdenver.org) and Pluma Academy's TCF page (plumaacademy.com), checked on October 26, 2026.",
    badges={DEN: [("ok", "TCF Canada"), ("part", "sold out to Dec 7")], PLU: _OPEN},
    urls={DEN: "https://www.afdenver.org/library-and-services/exams/tcf/", PLU: "https://plumaacademy.com/tcf-exam/"},
    list_title="The {n} approved TCF centers in Denver"))

# ============================================================================ CANADA
# ---------------------------------------------------------------------------- ALBERTA
CAL, EDM, LET = "calgary-alliance-francaise", "edmonton-alliance-francaise", "lethbridge-french-language-centre"
PAGES.append(_page(
    "tcf-canada-alberta", CA_FILE, "en-CA", "en_CA", "Canada", ["Calgary", "Edmonton", "Lethbridge"], "Alberta", CA_LIST,
    title="TCF Canada in Alberta: Calgary, Edmonton, $400, booking",
    desc="TCF Canada in Alberta: the Alliances Françaises in Calgary and Edmonton ($400) were sold out on 26 October 2026; Lethbridge offers only the DELF.",
    h1="TCF Canada in Alberta: Calgary, Edmonton and Lethbridge — fees, dates and booking",
    intro="""In Alberta, three centres are approved for the TCF by France Éducation international, but only <strong>two run
the TCF Canada</strong>: the <strong>Alliance Française de Calgary</strong> and the <strong>Alliance Française
d'Edmonton</strong>, both at <strong>$400</strong>, on computer. On 26 October 2026, every session they listed was
<strong>sold out</strong> — in Calgary, October to December, including all ten December test days; in Edmonton, the
fifteen sessions shown, from 26 October to 13 November — and neither had published a 2027 date. The University of
Lethbridge's French Language Centre offers only the DELF-DALF.""",
    facts=["<strong>{n} approved centres</strong> in Alberta (FEI list of 26 October 2026): Calgary, Edmonton, Lethbridge — <strong>the TCF Canada in Calgary and Edmonton only</strong>.",
           "<strong>$400</strong> in both cities; in Calgary, «no refund or deferment is possible».",
           "⚠️ 26 October 2026: Calgary <strong>sold out</strong> for October, November and its ten December dates; Edmonton sold out for every session shown, 26 October to 13 November; no 2027 date in either city.",
           "Edmonton sells each session during a window of about an hour on one day; Calgary's 14-seat sessions go «first-come, first-served».",
           "Lethbridge: DELF-DALF twice a year, no TCF on its pages.",
           "20 days between two attempts in Calgary and Edmonton."],
    stats=[("$400", "TCF Canada", "Calgary and Edmonton"), ("0", "open sessions", "on 26 October 2026"),
           ("2 of 3", "approved centres", "run the TCF Canada"), ("20 days", "between two attempts", "in any location")],
    sections=[
        ("what-we-found", "What we found, centre by centre", releve([
            ("Alliance Française de Calgary", "<strong>Canada</strong>, tout public", "<strong>$400</strong>",
             "October and November <strong>sold out</strong>; December: 1, 2, 3, 8, 9, 10, 15, 16, 17 and 22 all <strong>sold out</strong>; no 2027 date. Tests at the Kahanoff Centre, #315, 105 12 Avenue SE. <a href=\"/en/tcf-canada-calgary/\">Calgary page</a>."),
            ("Alliance Française d'Edmonton", "<strong>Canada</strong>", "<strong>$400</strong>",
             "15 sessions shown, morning and afternoon, 26 October to 13 November: all <strong>sold out</strong>; no 2027 date. <a href=\"/en/tcf-canada-edmonton/\">Edmonton page</a>."),
            ("University of Lethbridge, French Language Centre", "DELF-DALF only", "—", "No TCF on its pages: DELF-DALF twice a year."),
        ], "en-CA", "What each centre's website showed on 26 October 2026.")),
        ("booking", "How to get a seat in Alberta", """<p>Neither Alliance takes bookings by phone. <strong>Calgary</strong>
publishes its dates on its TCF registration page — «All 2026 exam dates will be published on this page» — and is «working
with our partners in Paris to open additional sessions»: you pay online for a date, then receive a form to upload your ID.
<strong>Edmonton</strong> lists each session with its own sales window, often about an hour on a single day, and on
18 October it warned that requests about TEF or TCF dates get no individual answer: watch the page and be online when
the window opens. In
both cities, allow 20 days between two attempts.</p>

<p>If you only need a seat, look further east: on 26 October 2026, the TCF Canada had open dates at $390 in
<a href="/en/tcf-canada-new-brunswick/">New Brunswick</a> — every weekend to 20 December at the CCNB in Edmundston and
Bathurst, and ten dates from 1 December in Moncton — and in <a href="/en/tcf-canada-ottawa/">Ottawa</a> ($400) on
10 November. <a href="/en/tcf-canada-winnipeg/">Winnipeg</a> ($400) and <a href="/en/tcf-canada-vancouver/">Vancouver</a>
($390) were sold out for December. On the TEF side, the map of TEF centres of Le français des affaires (CCI Paris
Île-de-France) showed no TEF Canada session published for Calgary or Edmonton on 26 October. Every province is on our
<a href="/en/tcf-canada-test-centres/">list of centres in Canada</a>.</p>""")],
    faq=[("Where can I take the TCF Canada in Alberta?", "At the Alliance Française de Calgary (tests at the Kahanoff Centre, #315, 105 12 Avenue SE) or at the Alliance Française d'Edmonton, both on computer. The University of Lethbridge is approved by FEI but offers only the DELF-DALF."),
         ("When is the next TCF Canada in Alberta?", "On 26 October 2026, every session listed in Calgary (to 22 December) and in Edmonton (to 13 November) was sold out, and neither centre had published a 2027 date."),
         ("How much does the TCF Canada cost in Alberta?", "$400 in Calgary and in Edmonton (26 October 2026); Calgary allows no refund or deferment."),
         ("Can I take the TCF in Lethbridge?", "No TCF was offered on the University of Lethbridge's pages on 26 October 2026: its French Language Centre runs the DELF-DALF twice a year. The nearest TCF Canada centre is Calgary."),
         ("Where are TCF Canada seats available?", "On 26 October 2026: in New Brunswick (CCNB in Edmundston and Bathurst, every weekend to 20 December; Alliance française de Moncton from 1 December, $390) and in Ottawa (10 November, $400).")],
    also=[_NB, ("/en/tcf-canada-calgary/", "TCF Canada in Calgary", "$400, 14 seats a session at the Kahanoff Centre."),
          ("/en/tcf-canada-edmonton/", "TCF Canada in Edmonton", "$400; each session sells in about an hour.")],
    sources="the TCF and registration pages of the Alliance Française de Calgary (afcalgary.ca) and of the Alliance Française d'Edmonton (afedmonton.com), and the University of Lethbridge's French Language Centre page, checked on 26 October 2026; the map of TEF centres of Le français des affaires (CCI Paris Île-de-France), read the same day.",
    badges={CAL: [("ok", "TCF Canada"), ("part", "sold out to December")], EDM: [("ok", "TCF Canada"), ("part", "sold out to 13 Nov")],
            LET: [("no", "DELF-DALF only")]},
    urls={CAL: "https://www.afcalgary.ca/exams/tcf/", EDM: "https://www.afedmonton.com/en/exams/tcf/"},
    list_title="The {n} approved TCF centres in Alberta"))
PAGES[-1]["notes"] = {CAL: "Tests at the Kahanoff Centre, #315, 105 12 Avenue SE.",
                      EDM: "Tests at the Alliance’s annex, 100, 11812–121 St NW (Kingsway), according to its website (18 October 2026)."}

# ---------------------------------------------------------------------------- NEW BRUNSWICK
MON, EDS, BAT = "moncton-alliance-francaise-de-moncton", "edmundston-campus-d-edmundston", "bathurst-campus-de-bathurst"
CCNB = "https://ccnb.ca/admission-et-inscription/test-de-connaissance-du-francais-tcf/"
PAGES.append(_page(
    "tcf-canada-new-brunswick", CA_FILE, "en-CA", "en_CA", "Canada", ["Moncton", "Edmundston", "Bathurst"], "New Brunswick", CA_LIST,
    title="TCF Canada in New Brunswick: Moncton, Edmundston, $390",
    desc="TCF Canada in New Brunswick: $390 at the Alliance française de Moncton and at the CCNB in Edmundston and Bathurst — open dates on 26 October 2026.",
    h1="TCF Canada in New Brunswick: Moncton, Edmundston and Bathurst — dates, fees, booking",
    intro="""New Brunswick has three approved TCF centres — the <strong>Alliance française de Moncton</strong> and the
<strong>CCNB</strong> (Collège communautaire du Nouveau-Brunswick) campuses in <strong>Edmundston</strong> and
<strong>Bathurst</strong> — and, unlike Vancouver, Calgary or Halifax, <strong>they had seats</strong> on 26 October 2026.
The CCNB was selling TCF Canada sessions on weekends until 20 December, for <strong>$390</strong>; the Alliance in
Moncton, ten dates from 1 December 2026 to 9 January 2027, also at <strong>$390</strong>. All on computer, with the
speaking test in front of an examiner.""",
    facts=["<strong>{n} approved centres</strong> (FEI list of 26 October 2026): the Alliance française de Moncton and the CCNB campuses in Edmundston and Bathurst.",
           "<strong>$390</strong> at all three; on computer, speaking test with a jury.",
           "CCNB: sessions every weekend from <strong>31 October to 20 December 2026</strong> in Edmundston (Saturday and Sunday) and Bathurst; on 26 October, all but two had seats left — Bathurst on 31 October and Edmundston on 1 November were full.",
           "Moncton: <strong>1, 4, 8, 9, 11, 15 and 18 December 2026, 6, 8 and 9 January 2027</strong>, all open for booking on 26 October.",
           "20 days between two attempts in Moncton, 30 days at the CCNB; certificates in about 15 working days.",
           "No refunds; Moncton accepts one free date change up to 7 days before, requested by email."],
    stats=[("$390", "TCF Canada", "at all three centres"), ("10", "dates in Moncton", "1 Dec to 9 Jan"),
           ("Weekends", "at the CCNB", "to 20 December 2026"), ("{n}", "approved centres", "in New Brunswick")],
    sections=[
        ("what-we-found", "What we found, centre by centre", releve([
            ("Alliance française de Moncton", "<strong>Canada</strong>, tout public", "<strong>$390</strong>",
             "1, 4, 8, 9, 11, 15, 18 Dec 2026, 6, 8, 9 Jan 2027: all bookable on 26 October; on computer; 20 days between two attempts; certificate in at least 15 working days."),
            ("CCNB — Campus d'Edmundston", "<strong>Canada</strong>, Québec", "<strong>$390</strong>",
             "Saturdays and Sundays, 31 Oct to 20 Dec 2026, 8:45 am; seats left on every date except 1 November (full); 30 days between two sessions."),
            ("CCNB — Campus de Bathurst", "<strong>Canada</strong>, Québec", "<strong>$390</strong>",
             "Weekends, 7 Nov to 20 Dec 2026, 9 am, seats left; 31 October full."),
        ], "en-CA", "What each centre's website and booking page showed on 26 October 2026.")),
        ("booking", "How to book in New Brunswick", """<p>The <strong>CCNB</strong> sells its TCF sessions on an online
booking page (Bookeo), linked from its TCF page by «Inscrivez-vous ici!»: each date shows the campus, the number of seats
left and the price, $390. The reading, listening and writing tests are on computer, the speaking test «en présence d'un
jury»; allow 30 days between two sessions, and about 15 days for the results certificate. The CCNB's pages are in
French; the toll-free number is 1-800-376-5353.</p>

<p>In <strong>Moncton</strong>, the Alliance française sells its TCF Canada dates in its online store: «aucun
remboursement ne sera accordé et l'inscription est ferme et définitive». You may change the date <strong>once</strong>,
free of charge, up to 7 days before the test, by email to exams@afmoncton.ca; the registration is in your name and
cannot be moved to another test. Your test-day notice arrives at the latest a week before. Allow 20 days between two
attempts.</p>

<p>Whichever centre you choose, the results certificate is issued by France Éducation international and accepted by
IRCC like any other. Nearby: <a href="/en/tcf-canada-halifax/">Halifax</a> ($400; 8 December full on 26 October). Every
province is on our <a href="/en/tcf-canada-test-centres/">list of centres in Canada</a>.</p>""")],
    faq=[("Where can I take the TCF Canada in New Brunswick?", "At the Alliance française de Moncton (236 Rue St Georges) or at the CCNB campuses in Edmundston (35, rue du 15-Août) and Bathurst (725, rue du Collège), all approved by France Éducation international and on computer."),
         ("When is the next TCF Canada in New Brunswick?", "On 26 October 2026: CCNB sessions every weekend from 31 October to 20 December in Edmundston and Bathurst, most with seats left, and ten dates in Moncton from 1 December 2026 to 9 January 2027."),
         ("How much does the TCF Canada cost in Moncton or Edmundston?", "$390 at the Alliance française de Moncton and at the CCNB (26 October 2026)."),
         ("Can I take the TCF Canada in Edmundston?", "Yes: the CCNB's Edmundston campus holds it on Saturdays and Sundays at 8:45 am; on 26 October 2026, every date to 20 December had seats except 1 November."),
         ("Does a TCF Canada taken in New Brunswick count for Express Entry?", "Yes: the results certificate is issued by France Éducation international, whichever approved centre you test at, and is valid for two years.")],
    also=[("/en/tcf-canada-halifax/", "TCF Canada in Halifax", "$400 at the Alliance Française; 8 December full."), _CAN, _PRACTICE],
    sources="the Alliance française de Moncton's TCF Canada and registration pages (afmoncton.ca) and the CCNB's TCF page and booking page (ccnb.ca, Bookeo), checked on 26 October 2026.",
    badges={MON: _OPEN, EDS: _OPEN, BAT: _OPEN},
    urls={MON: "https://www.afmoncton.ca/en/inscription-au-tcf-canada/", EDS: CCNB, BAT: CCNB},
    list_title="The {n} approved TCF centres in New Brunswick"))
PAGES[-1]["notes"] = {EDS: "Collège communautaire du Nouveau-Brunswick (CCNB).", BAT: "Collège communautaire du Nouveau-Brunswick (CCNB)."}

# ---------------------------------------------------------------------------- HALIFAX
HAL = "halifax-halifax-alliance-francaise"
PAGES.append(_page(
    "tcf-canada-halifax", CA_FILE, "en-CA", "en_CA", "Canada", ["Halifax"], "Halifax", CA_LIST,
    title="TCF Canada in Halifax: $400, 8 December full, booking",
    desc="TCF Canada at the Alliance Française Halifax, 5509 Young Street: $400, on computer; the only session listed on 26 October 2026, 8 December, was full.",
    h1="TCF Canada in Halifax: the Alliance Française, the fee and the sessions",
    intro="""In Halifax, the TCF Canada is held by the <strong>Alliance Française Halifax</strong>, 5509 Young Street — the
only approved TCF centre in Nova Scotia — for <strong>$400</strong>, on computer. On 26 October 2026, its booking page
listed a single session, <strong>Tuesday 8 December</strong>, already <strong>full</strong>. You register online with a
scan of your passport, the fee is not refundable, and the certificate arrives by email 15 business days after the test.
The nearest open seats were in New Brunswick.""",
    facts=["<strong>{n} approved centre</strong> in Nova Scotia: the Alliance Française Halifax, 5509 Young Street.",
           "TCF Canada <strong>$400</strong> (fees «may change without notice»); the four tests on the same day, on computer.",
           "⚠️ 26 October 2026: one session listed, <strong>8 December 2026 — full</strong>.",
           "Online registration with a scanned passport; payment in the online store, by phone (Visa, Mastercard) or by Interac e-transfer.",
           "No refund; a new date only in exceptional circumstances, documented at least 7 days before; 20 days between two attempts."],
    stats=[("$400", "TCF Canada", "on computer"), ("1", "session listed", "8 December, full"),
           ("15 days", "for the certificate", "business days"), ("20 days", "between two attempts", "the Alliance's rule")],
    sections=[("booking", "Booking the TCF Canada in Halifax", """<p>The Alliance sells the TCF Canada in its online store,
on a registration page where each session shows its date, the venue and «Full» or a booking button: on 26 October 2026,
the only session listed, Tuesday 8 December at 9 am, was full. To book a future date you upload a scanned copy of your
passport, pay — online, by phone with a Visa or Mastercard, or by Interac e-transfer — and receive your official notice
7 to 10 days before the test. Dates are firm: a change is considered only for exceptional circumstances, with documents,
at least 7 days before, and a candidate turned away without a passport must wait a month to reapply. Questions go to
exam@afhalifax.ca or 902-580-8284.</p>

<p>On 26 October, the nearest open dates were in <a href="/en/tcf-canada-new-brunswick/">New Brunswick</a>: $390, every
weekend to 20 December at the CCNB in Edmundston and Bathurst, and from 1 December in Moncton.</p>""")],
    faq=[("Where can I take the TCF Canada in Halifax?", "At the Alliance Française Halifax, 5509 Young Street, the only approved TCF centre in Nova Scotia, on computer."),
         ("When is the next TCF Canada in Halifax?", "On 26 October 2026, the only session listed was Tuesday 8 December 2026, and it was full; watch the Alliance's registration page for new dates."),
         ("How much does the TCF Canada cost in Halifax?", "$400 at the Alliance Française Halifax (26 October 2026); registration fees are not refundable."),
         ("Where can I find a seat near Halifax?", "In New Brunswick, on 26 October 2026: the CCNB in Edmundston and Bathurst (every weekend to 20 December) and the Alliance française de Moncton (from 1 December), all at $390.")],
    also=[_NB, _CAN, _PRACTICE],
    sources="the Alliance Française Halifax's TCF and TCF Canada registration pages (afhalifax.ca), checked on 26 October 2026.",
    badges={HAL: [("ok", "TCF Canada"), ("part", "8 Dec full")]},
    urls={HAL: "https://afhalifax.ca/test-your-french/tcf/tcf-canada-registration/"}))

# ---------------------------------------------------------------------------- WINNIPEG
WPG = "winnipeg-alliance-francaise-du-manitoba"
PAGES.append(_page(
    "tcf-canada-winnipeg", CA_FILE, "en-CA", "en_CA", "Canada", ["Winnipeg"], "Winnipeg", CA_LIST,
    title="TCF Canada in Winnipeg: $400, December sold out, booking",
    desc="TCF Canada at the Alliance Française du Manitoba, 934 Corydon Avenue: $400, on computer; 9, 11 and 14 December 2026 sold out on 26 October.",
    h1="TCF Canada in Winnipeg: the Alliance Française du Manitoba, the fee and the dates",
    intro="""In Winnipeg, the TCF Canada is held by the <strong>Alliance Française du Manitoba</strong>, 934 Corydon Avenue —
the only approved TCF centre in Manitoba — for <strong>$400</strong>. On 26 October 2026, its TCF page listed three «new
dates», <strong>9, 11 and 14 December</strong>, all <strong>sold out</strong>, and nothing for 2027. Registration takes four
steps — the form and your ID, the payment, then a date confirmed by email — and the fee is neither refunded nor
deferred.""",
    facts=["<strong>{n} approved centre</strong> in Manitoba: the Alliance Française du Manitoba, 934 Corydon Avenue.",
           "TCF Canada <strong>$400</strong>; optional PrepMyFuture online preparation, $80.",
           "⚠️ 26 October 2026: <strong>9, 11 and 14 December sold out</strong>; no other date listed.",
           "Reading, listening and writing on computer; speaking face to face, 12 minutes; the exam day runs from 9:50 am to 6 pm.",
           "30 days between two attempts; results within 4 weeks; «No refund or deferment is possible»."],
    stats=[("$400", "TCF Canada", "full exam"), ("3", "December dates", "all sold out"),
           ("4 weeks", "for the results", "by email from FEI"), ("30 days", "between two attempts", "the Alliance's rule")],
    sections=[("booking", "Booking the TCF Canada in Winnipeg", """<p>The Alliance's TCF page sets out four steps: fill in
the TCF form with a piece of ID (passport, residence permit or national identity card), pay — online or by phone — and
wait for the email that confirms your date. «The registration is not complete until payment has been received.» The
exam day runs from 9:50 am to 6 pm; results arrive by email from France Éducation international within four weeks, and
«There is absolutely no way to speed up the process». Cancellations «for climatic or personal reasons are not possible».
For new dates, watch the page or write to info@afmanitoba.ca.</p>

<p>On 26 October 2026, the nearest centres were sold out too — <a href="/en/tcf-canada-alberta/">Calgary and Edmonton</a>
($400). Open dates were in <a href="/en/tcf-canada-new-brunswick/">New Brunswick</a> ($390) and
<a href="/en/tcf-canada-ottawa/">Ottawa</a> ($400).</p>""")],
    faq=[("Where can I take the TCF Canada in Winnipeg?", "At the Alliance Française du Manitoba, 934 Corydon Avenue, the only approved TCF centre in Manitoba."),
         ("When is the next TCF Canada in Winnipeg?", "On 26 October 2026, the three dates listed — 9, 11 and 14 December 2026 — were sold out, and no 2027 date was published."),
         ("How much does the TCF Canada cost in Winnipeg?", "$400 at the Alliance Française du Manitoba (26 October 2026); no refund or deferment is possible."),
         ("How long between two attempts in Winnipeg?", "30 days, according to the Alliance; results take up to four weeks.")],
    also=[_ALBERTA, _NB, _CAN],
    sources="the Alliance Française du Manitoba's TCF and TCF Canada registration pages (afmanitoba.ca), checked on 26 October 2026.",
    badges={WPG: [("ok", "TCF Canada"), ("part", "December sold out")]},
    urls={WPG: "https://www.afmanitoba.ca/en/exams/tcf/"}))

# ---------------------------------------------------------------------------- ONTARIO
AFT = "https://www.alliance-francaise.ca/en/exams/tests/informations-about-tcf-canada"
TOR = ["toronto-alliance-francaise", "north-york-alliance-francaise-de-toronto", "mississauga-alliance-francaise", "oakville-alliance-francaise"]
GB, OTT, FL, WIN = "north-york-gb-language-centre", "ottawa-alliance-francaise", "ottawa-francolangues", "windsor-windsor-college-boreal-windsor"
PAGES.append(_page(
    "tcf-canada-ontario", CA_FILE, "en-CA", "en_CA", "Canada", ["Toronto", "North York", "Mississauga", "Oakville", "Ottawa", "Windsor"],
    "Ontario", CA_LIST,
    title="TCF Canada test centres in Ontario: Toronto, Ottawa, fees",
    desc="The TCF Canada test centres in Ontario — Toronto, North York, Mississauga, Oakville, Ottawa, Kanata, Windsor: fees $390 to $452, next dates, booking.",
    h1="TCF Canada test centres in Ontario: where to book, the fees and the next dates",
    intro="""Ontario has <strong>{n} approved TCF centres</strong> on France Éducation international's list of 26 October
2026: the four sites of the <strong>Alliance française de Toronto</strong> (Spadina, North York, Mississauga, Oakville),
<strong>GB Language Centre</strong> in North York, the <strong>Alliance Française Ottawa</strong>,
<strong>FrancoLangues</strong> in Kanata and <strong>Collège Boréal</strong> in Windsor. On 26 October, the TCF Canada cost
<strong>$390</strong> at the Alliance in Toronto, <strong>$400</strong> in Ottawa and <strong>$452</strong> at GB Language
Centre; Ottawa had seats on <strong>10 November</strong>, and Toronto opens its January–March 2027 sessions on
<strong>1 December at 10 am</strong>.""",
    facts=["<strong>{n} approved centres</strong> (FEI, 26 October 2026): Toronto (Spadina), North York (2), Mississauga, Oakville, Ottawa (2, including FrancoLangues in Kanata) and Windsor (Collège Boréal, paper-based, new on the list since 19 September).",
           "Fees on 26 October 2026: <strong>$390</strong> Alliance française de Toronto · <strong>$400</strong> Alliance Française Ottawa · <strong>$452</strong> GB Language Centre · FrancoLangues: given when you book.",
           "Toronto: registration for January–March 2027 opens on <strong>1 December 2026 at 10 am</strong>, then on 2 March, 20 May and 17 August 2027; «If a session is not listed, it is full»; no waitlist.",
           "Ottawa: <strong>10 November 2026</strong>, 6 and 8 January 2027 open on computer, 14 January 2027 on paper; further January sessions go on sale on 1 November 2026.",
           "20 days between two attempts at the Alliance in Toronto; 30 days at FrancoLangues."],
    stats=[("$390", "Alliance française de Toronto", "4 sites in the GTA"), ("$400", "Alliance Française Ottawa", "computer or paper"),
           ("1 Dec", "Toronto opens Q1 2027", "at 10 am"), ("{n}", "approved centres", "FEI list of 26 October 2026")],
    sections=[
        ("what-we-found", "What we found, centre by centre", releve([
            ("Alliance française de Toronto (Spadina, North York, Mississauga, Oakville)", "<strong>Canada</strong> (computer or paper), Québec", "<strong>$390</strong>",
             "Registration online only, one month before each quarter at 10 am: 1 Dec 2026 (Jan–Mar 2027), 2 Mar, 20 May, 17 Aug 2027; no waitlist; one registration at a time; transfer up to 15 days before (computer) or 30 days (paper) for $100. <a href=\"/en/tcf-canada-toronto/\">Toronto page</a>."),
            ("GB Language Centre (North York)", "<strong>Canada</strong>, tout public, TEF Canada", "<strong>$452</strong>",
             "Book online on its website; TCF tout public $520, TEF Canada $452."),
            ("Alliance Française Ottawa", "<strong>Canada</strong> (computer or paper)", "<strong>$400</strong>",
             "Computer: 10 Nov 2026, 6 and 8 Jan 2027 open; further January dates on sale from 1 Nov. Paper: 14 Jan 2027 open. «No dates will be communicated by email or phone.» <a href=\"/en/tcf-canada-ottawa/\">Ottawa page</a>."),
            ("FrancoLangues (Kanata)", "<strong>Canada</strong>, Québec", NR,
             "Booking on its online appointment page; no refunds or date changes; 30 days between two tests; certificate 4 to 8 weeks after the test."),
            ("Collège Boréal (Windsor)", NR, NR, "On FEI's list since October 2026 (paper-based); no TCF page found on its website."),
        ], "en-CA", "What each centre's website showed on 26 October 2026. “No data”: not published, or not found — the centre’s website is the reference.")),
        ("booking", "How to book the TCF Canada in Ontario", """<p>In <strong>Toronto</strong>, the Alliance française
sells its sessions only online, through an account you create beforehand: registration opens one month before each
quarter at 10 am, and «If a session is not listed, it is full». Have your account and passport ready on
<strong>1 December 2026 at 10 am</strong> for the January–March 2027 sessions. «There is no waiting list», you can hold
only one registration at a time across its four sites, and refunds are «not possible under any circumstances» — a
transfer costs $100. <strong>GB Language Centre</strong>, in North York, sells the TCF Canada at $452 on its own
website.</p>

<p>In <strong>Ottawa</strong>, the Alliance Française lists each session with an «Add to cart» button or the date its sales
open; on 26 October, 10 November 2026 and 6 and 8 January 2027 were open on computer and 14 January 2027 on paper.
<strong>FrancoLangues</strong>, at 105 Schneider Road in Kanata, takes bookings through its online appointment page and
gives its fee when you book; it refunds nothing and changes no dates. In <strong>Windsor</strong>, Collège Boréal appears
on FEI's list, but we found no TCF page: ask the college. Outside Ontario, the nearest open dates were in
<a href="/en/tcf-canada-new-brunswick/">New Brunswick</a> ($390).</p>

<p>The <strong>TEF Canada</strong>, which IRCC also accepts, is another way in: on 26 October 2026, the map of TEF centres
of Le français des affaires (CCI Paris Île-de-France) showed TEF Canada sessions published at GB Language Centre and the
Montreal Language Institute in North York, Collège Boréal in Toronto and Windsor, and Algonquin College in Ottawa
(<a href="/en/tcf-vs-tef-canada/">TCF vs TEF Canada</a>).</p>""")],
    list_intro="""<p>Collège Boréal in Windsor was added to FEI's list after 19 September 2026; the other centres were
already on it.</p>""",
    faq=[("Where can I take the TCF Canada in Ontario?", "In the Toronto area, at the Alliance française de Toronto (Spadina, North York, Mississauga, Oakville) or GB Language Centre (North York); in Ottawa, at the Alliance Française (352 MacLaren Street) or FrancoLangues (Kanata); and Collège Boréal in Windsor is on FEI's list."),
         ("How much does the TCF Canada cost in Ontario?", "On 26 October 2026: $390 at the Alliance française de Toronto, $400 at the Alliance Française Ottawa, $452 at GB Language Centre; FrancoLangues gives its fee when you book."),
         ("When can I book the TCF Canada in Toronto?", "Registration for January–March 2027 opens on 1 December 2026 at 10 am, then on 2 March, 20 May and 17 August 2027. Sessions go within minutes, and there is no waitlist."),
         ("Where are TCF Canada seats available in Ontario?", "On 26 October 2026, at the Alliance Française Ottawa: 10 November 2026 and 6 and 8 January 2027 on computer, 14 January 2027 on paper, at $400."),
         ("Can I take the TCF Canada in North York?", "Yes: at the Alliance française de Toronto's North York campus (47 Sheppard Avenue East), $390, or at GB Language Centre (716 Gordon Baker Road), $452.")],
    also=[("/en/tcf-canada-toronto/", "TCF Canada in Toronto", "$390; 2027 bookings open on 1 December at 10 am."),
          ("/en/tcf-canada-ottawa/", "TCF Canada in Ottawa", "$400; 10 November and January dates open."), _CAN],
    sources="the TCF Canada pages of the Alliance française de Toronto (alliance-francaise.ca) and of the Alliance Française Ottawa (af.ca, with its session list), GB Language Centre's website (gblc.ca), FrancoLangues' TCF page (francolangues.com) and Collège Boréal's website, checked on 26 October 2026; the map of TEF centres of Le français des affaires (CCI Paris Île-de-France), read the same day.",
    badges=dict({k: _OK for k in TOR}, **{GB: _OK, OTT: _OPEN, FL: _OK}),
    urls=dict({k: AFT for k in TOR}, **{GB: "https://gblc.ca/en", OTT: "https://af.ca/ottawa/en/tests_et_examens/tcf-canada",
                                         FL: "https://francolangues.com/tcf-canada-tcf-qc-test-de-connaissance-du-francais/"}),
    list_title="The {n} approved TCF centres in Ontario"))
