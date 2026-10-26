# -*- coding: utf-8 -*-
"""English pages for Arab countries not covered on 13/10 (26/10/2026): Jordan, Qatar, Kuwait.

Hooked into pays_config_en.PAGES by one line at the end of pays_config_en.py; paired with the Arabic pages of
pays_config_ar_world.py (pair="/en/…/"). No French original, so no fr_path.

Facts, all read on 26 October 2026:
- FEI list (data/fei_monde/tcf_<country>.json, ids Jordanie 105, Qatar 404, Koweït 369): one TCF centre each.
- Jordan: ifjordan.com/tcfexam and its 2026 exam calendar (PDF « 84b65b_84ebc563… ») — TCF Canada 17/02, 15/07, 11/11/2026,
  registration 18–20/01, 07–09/06, 04–06/10; 3 TCF Canada sessions a year; registration by email; no fee published.
- Qatar: if-qatar.com/en/events/tcf-canada-4/ (16/12/2026, 1,300 QAR, computer only, page headed « Inscriptions closes »)
  and if-qatar.com/en/examens-et-certifications/ (registration in person, cash or card, refund rules). The site carries
  hidden gambling spam (hacked); it is still the official site (linked from qa.diplomatie.gouv.fr).
- Kuwait: ifk.edu.kw (exam pages: DELF, DALF, TEF only; TEF Canada 130 KD, TEF 80, TEFAQ 70, 5 KD student discount);
  the FEI website institutfrancais-koweit.com redirects to a dead host.
Nearby countries without a page (26/10): Bahrain (AF du Bahreïn, website unreachable), Oman (no TCF centre), Iraq
(Baghdad, Erbil: TCF tout public only in Erbil, paper, May and October), Palestine (Ramallah, Bethlehem: no TCF Canada
on the websites that opened).
"""
from pays_config import table

PAGES = []
_D = dict(lang="en", variant="en-GB", fr_path=None, exam="tcf", layout="cities",
          list_date="26 October 2026", releve_date="26 October 2026", date_label="26 October 2026", published="2026-10-26")
_PRACTICE = ("/en/tcf-canada-practice-test/", "Free TCF Canada practice test", "Check your level before you pay for a session.")

JO = "amman-institut-francais-de-jordanie-ambassade-de-france-en-jordanie"
QA = "doha-institut-francais-du-qatar"
KW = "koweit-institut-francais"

# ===========================================================================
# JORDAN
# ===========================================================================
PAGES.append(dict(_D,
    og_locale="en_JO", slug="tcf-canada-jordan", country_name="Jordan", file="fei_monde/tcf_jordanie",
    crumb="TCF Canada in Jordan",
    title="TCF Canada in Jordan: Amman, 3 sessions a year (2026)",
    desc="TCF Canada in Jordan: the Institut français de Jordanie in Amman holds three sessions a year. 2026 dates, email registration; the fee is not published.",
    h1="TCF Canada in Jordan: the Institut français in Amman and its sessions",
    intro="""Yes: in Jordan, the TCF Canada is held by the <strong>Institut français de Jordanie</strong> in Amman (Jabal
Al-Weibdeh), the only approved TCF centre on France Éducation international’s list of 26 October 2026. Its 2026
calendar has three TCF Canada sessions — 17 February, 15 July and <strong>Wednesday 11 November</strong> (registration
4 to 6 October, now closed). You register by email; the fee is not published.""",
    facts=["<strong>{n} approved TCF centre</strong> in Jordan (FEI list of 26 October 2026): the Institut français de Jordanie, Amman; FEI lists no computer-based sessions for it.",
           "TCF Canada 2026: 17 February, 15 July and <strong>Wednesday 11 November</strong>; registration 18–20 January, 7–9 June and 4–6 October.",
           "<strong>Three TCF Canada sessions a year</strong> (and two each of the TCF tout public and the TCF IRN).",
           "Registration <strong>by email</strong> (cours@ifjordan.com), during a three-day window four to five weeks before the test.",
           "Fee: <strong>not published</strong> on the institute’s website on 26 October 2026; no 2027 date yet."],
    stats=[("11 Nov", "last 2026 TCF Canada session", "registration closed 6 Oct"), ("3", "TCF Canada sessions a year", "Institut français de Jordanie"),
           ("3 days", "registration window", "by email"), ("2 years", "results validity", "for IRCC")],
    sections=[
        ("sessions", "The 2026 TCF Canada calendar in Amman", table(
            "TCF Canada sessions in the Institut français de Jordanie’s 2026 exam calendar (PDF linked from ifjordan.com/tcfexam), read on 26 October 2026.",
            ["Session", "Registration", "Status on 26 October 2026"],
            [("Tue 17 Feb 2026", "18–20 Jan", "past"), ("Wed 15 Jul 2026", "7–9 Jun", "past"),
             ("<strong>Wed 11 Nov 2026</strong>", "4–6 Oct", "<strong>registration closed</strong>")], wide=False) + """
<p>The Institut français de Jordanie publishes its TCF dates in a PDF calendar linked from its TCF page. The same
calendar lists the TCF tout public on 17 February and 15 July, and the TCF IRN on 29 April and 11 November. You register
by email to cours@ifjordan.com during the registration window — three days, four to five weeks before the test. The
website gives no fee and does not say whether the test is on paper or on computer; France Éducation international’s list
shows no computer-based sessions for this centre, so ask the institute. On 26 October 2026, no 2027 date had been
published. The results certificate is valid for two years.</p>"""),
        ("nearby", "If the Amman dates don’t suit you", """<p>The nearest centres that advertised the TCF Canada when we
checked them: <a href="/en/tcf-canada-lebanon/">Lebanon</a> (six Institut français centres),
<a href="/en/tcf-canada-egypt/">Egypt</a> (Cairo, Tuesday 8 December 2026), <a href="/en/tcf-canada-saudi-arabia/">Saudi
Arabia</a> (1,950 SAR), <a href="/en/tcf-canada-qatar/">Qatar</a> (Doha, 1,300 QAR) and the
<a href="/en/tcf-canada-dubai/">United Arab Emirates</a> (1,800 AED). France Éducation international also lists TCF centres
in Iraq (Baghdad, Erbil) and the Palestinian territories (Ramallah, Bethlehem), but on 26 October 2026 none of their
websites that we could open mentioned the TCF Canada — in Erbil, the Institut français offers only the TCF tout public, on
paper, in May and October.</p>"""),
    ],
    list_title="The {n} approved TCF centre in Jordan",
    faq=[("Can I take the TCF Canada in Jordan?", "Yes, at the Institut français de Jordanie in Amman, which holds three TCF Canada sessions a year. Its 2026 calendar lists 17 February, 15 July and Wednesday 11 November (registration 4 to 6 October)."),
         ("How much does the TCF Canada cost in Jordan?", "The Institut français de Jordanie does not publish the fee on its website (26 October 2026); ask for it by email at cours@ifjordan.com before the registration window opens."),
         ("How do I register for the TCF Canada in Amman?", "By email to cours@ifjordan.com, during the registration window: three days, four to five weeks before the test."),
         ("When is the next TCF Canada in Jordan?", "Wednesday 11 November 2026, whose registration closed on 6 October. On 26 October 2026, the institute had not published its 2027 dates."),
         ("Is a TCF Canada taken in Jordan accepted by IRCC?", "Yes: the results certificate is issued by France Éducation international whichever approved centre you test at, and it is valid for two years.")],
    also=[("/en/tcf-canada-lebanon/", "TCF Canada in Lebanon", "Six Institut français centres."),
          ("/en/tcf-canada-egypt/", "TCF Canada in Egypt", "Cairo, Tuesday 8 December 2026."), _PRACTICE],
    sources="the Institut français de Jordanie’s TCF page and its 2026 exam calendar (PDF), ifjordan.com, checked on 26 October 2026.",
    badges={JO: [("ok", "TCF Canada"), ("part", "next: 11 Nov 2026")]},
    urls={JO: "https://www.ifjordan.com/tcfexam"},
    notes={JO: "The institute’s website gives +962 78 956 6622."},
))

# ===========================================================================
# QATAR
# ===========================================================================
PAGES.append(dict(_D,
    og_locale="en_QA", slug="tcf-canada-qatar", country_name="Qatar", file="fei_monde/tcf_qatar",
    crumb="TCF Canada in Qatar",
    title="TCF Canada in Qatar: Doha, 1,300 QAR, 16 December 2026",
    desc="TCF Canada in Qatar: the Institut français du Qatar in Doha, computer-based, 1,300 QAR; the 16 December 2026 session, registration and refund rules.",
    h1="TCF Canada in Qatar: the Institut français in Doha, the fee and the next session",
    intro="""Yes: in Qatar, the TCF Canada is held by the <strong>Institut français du Qatar</strong> in Doha, the only
approved TCF centre on France Éducation international’s list of 26 October 2026. That day, its website listed a session
on <strong>Wednesday 16 December 2026</strong>, on computer only, at <strong>1,300 QAR</strong> — under the heading
“Inscriptions closes” (registration closed). Exam fees are not refundable.""",
    facts=["<strong>{n} approved TCF centre</strong> in Qatar (FEI list of 26 October 2026): the Institut français du Qatar, Doha, with computer-based sessions.",
           "TCF Canada: <strong>Wednesday 16 December 2026</strong>, “computer only”, <strong>1,300 QAR</strong>; the event page was headed “Inscriptions closes” on 26 October.",
           "Registration: at the institute, with a copy of your passport and the filled-in registration form; payment in cash or by credit card.",
           "Exam fees are not refundable; a change of session or a refund is accepted once only, with a valid medical certificate.",
           "Your exam notification arrives by email before the test; the results certificate is valid for two years."],
    stats=[("1,300 QAR", "TCF Canada", "computer only"), ("16 Dec", "next session", "registration closed on 26 Oct"),
           ("{n}", "approved TCF centre", "Doha"), ("2 years", "validity", "for IRCC")],
    sections=[
        ("booking", "Booking the TCF Canada in Doha", """<p>The Institut français du Qatar publishes each exam session as
an event on its website (if-qatar.com). On 26 October 2026, its TCF Canada page announced the session of Wednesday
16 December, “computer only”, at 1,300 QAR, with a 2026 registration form and the address info@if-qatar.com — but the page
was headed “Inscriptions closes”: ask the institute about the next session. Its exams page says you register in person,
with a copy of your passport and the filled-in form, and pay in cash or by credit card; the exam notification is emailed
before the test. Registration fees are not refunded; a change of session or a refund is accepted once only, on a valid
medical certificate. One detail: the event page gives “135 Al Inshirah” as the venue, while France Éducation
international’s list gives the institute’s premises in Al Tarfa (Zone 68) — check the address on your notification.</p>"""),
        ("gulf", "Elsewhere in the Gulf", """<p>If the Doha session is closed: the TCF Canada is held in
<a href="/en/tcf-canada-saudi-arabia/">Saudi Arabia</a> (Alliance française d’Arabie Saoudite, 1,950 SAR) and in
<a href="/en/tcf-canada-dubai/">Dubai and Abu Dhabi</a> (Alliance Française, 1,800 AED). In
<a href="/en/tcf-canada-kuwait/">Kuwait</a>, the Institut français publishes no TCF Canada session, only the TEF Canada
(130 KD). France Éducation international lists a TCF centre in Bahrain (Alliance française du Bahreïn, Isa Town), but its
website did not open on 26 October 2026. Oman has no TCF centre on the list, but the Centre franco-omanais in Muscat is a TEF centre, with TEF Canada sessions published on the CCI Paris centre map on 26 October 2026. The Institut français du Qatar is also on the
TEF centre list of Le français des affaires (CCI Paris), with no session published there that day.</p>"""),
    ],
    list_title="The {n} approved TCF centre in Qatar",
    faq=[("Can I take the TCF Canada in Qatar?", "Yes, at the Institut français du Qatar in Doha, on computer only. On 26 October 2026 its website listed a session on Wednesday 16 December 2026, under the heading “Inscriptions closes” (registration closed)."),
         ("How much does the TCF Canada cost in Qatar?", "1,300 QAR at the Institut français du Qatar, as published on 26 October 2026."),
         ("Can I get a refund?", "No: exam fees are not refundable. A change of session or a refund is accepted once only, on a valid medical certificate."),
         ("How do I register?", "At the institute, with a copy of your passport and the filled-in registration form, paying in cash or by credit card; questions go to info@if-qatar.com."),
         ("Is a TCF Canada taken in Qatar accepted by IRCC?", "Yes: the results certificate is issued by France Éducation international whichever approved centre you test at, and it is valid for two years.")],
    also=[("/en/tcf-canada-saudi-arabia/", "TCF Canada in Saudi Arabia", "Jeddah and Riyadh, 1,950 SAR."),
          ("/en/tcf-canada-dubai/", "TCF Canada in Dubai and Abu Dhabi", "Four centres, 1,800 AED."), _PRACTICE],
    sources="the Institut français du Qatar’s TCF Canada event page and exams page (if-qatar.com), checked on 26 October 2026.",
    badges={QA: [("ok", "TCF Canada"), ("part", "16 Dec: registration closed")]},
    urls={QA: "https://if-qatar.com/en/examens-et-certifications/"},
))

# ===========================================================================
# KUWAIT
# ===========================================================================
PAGES.append(dict(_D,
    og_locale="en_KW", slug="tcf-canada-kuwait", country_name="Kuwait", file="fei_monde/tcf_koweit",
    crumb="TCF Canada in Kuwait",
    title="TCF Canada in Kuwait: not listed; TEF Canada is 130 KD",
    desc="TCF Canada in Kuwait: the Institut français is FEI-approved for the TCF, but its exam pages list only the TEF — TEF Canada 130 KD. Contacts and options.",
    h1="TCF Canada in Kuwait: what the Institut français offers",
    intro="""Not as far as its website shows. France Éducation international lists one approved TCF centre in Kuwait — the
<strong>Institut français du Koweït</strong>, in Jabriya — but on 26 October 2026 its exam pages offered the DELF, the DALF
and the <strong>TEF</strong>, with no TCF Canada session or fee. IRCC accepts both tests, and the <strong>TEF Canada</strong>
costs <strong>130 KD</strong> there. To ask about the TCF Canada, contact the institute.""",
    facts=["<strong>{n} approved TCF centre</strong> in Kuwait (FEI list of 26 October 2026): the Institut français, Jabriya (Hawalli); FEI shows computer-based sessions.",
           "TCF Canada: <strong>no session or fee published</strong> on the institute’s website on 26 October 2026.",
           "TEF Canada: <strong>130 KD</strong> (listening, reading, speaking, writing); TEF 80 KD, TEFAQ 70 KD; 5 KD off for the institute’s students.",
           "Registration: form, copy of the passport data page, passport photo and payment, at the institute.",
           "IRCC accepts the TCF Canada and the TEF Canada alike; results are valid for two years."],
    stats=[("130 KD", "TEF Canada", "Institut français du Koweït"), ("0", "TCF Canada sessions published", "26 October 2026"),
           ("{n}", "approved TCF centre", "Jabriya"), ("2 years", "validity", "TCF or TEF Canada")],
    sections=[
        ("tef-canada", "The TEF Canada at the Institut français du Koweït", table(
            "TEF fees on the Institut français du Koweït’s TEF page (ifk.edu.kw), read on 26 October 2026. Fees in Kuwaiti dinars.",
            ["Test", "Fee"],
            [("<strong>TEF Canada</strong> (all four sections)", "<strong>130 KD</strong>"),
             ("TEF, mandatory part (listening, reading, vocabulary and grammar)", "80 KD"),
             ("TEF, optional section (speaking or writing)", "30 KD each"),
             ("TEF Naturalisation (all four sections)", "80 KD"),
             ("TEFAQ, mandatory part (listening, speaking)", "70 KD")], wide=False) + """
<p>The institute’s current exam pages (ifk.edu.kw) cover the DELF, the DALF and the TEF, which is run by the Paris Chamber
of Commerce and Industry (Le français des affaires), not by France Éducation international. An older “Diploma &amp; Tests”
page describes TCF versions — the TCF DAP, the TCF ANF, the TCF Québec — and says the TCF can serve for “immigration to
Canada”, but it names no TCF Canada and gives no date or fee. To register for the TEF, you fill in the form (at the
institute or on its website), enclose a copy of your passport data page and a passport photo, and pay; students of the
institute get 5 KD off. The website on FEI’s list, institutfrancais-koweit.com, no longer opens: the institute’s site is
ifk.edu.kw.</p>"""),
        ("tcf", "If you need the TCF Canada itself", """<p>Contact the institute first (+965 6626 6980,
cours@ifk.edu.kw): FEI’s approval allows it to hold the TCF, but its website announced no session. Otherwise, the nearest
TCF Canada sessions we found are in <a href="/en/tcf-canada-qatar/">Doha</a> (1,300 QAR; the 16 December 2026 session
was marked “registration closed” on 26 October), <a href="/en/tcf-canada-saudi-arabia/">Saudi Arabia</a> (1,950 SAR) and
<a href="/en/tcf-canada-dubai/">Dubai and Abu Dhabi</a> (1,800 AED). Before you choose, compare the two tests:
<a href="/en/tcf-vs-tef-canada/">TCF vs TEF Canada</a>.</p>"""),
    ],
    list_title="The {n} approved TCF centre in Kuwait",
    faq=[("Can I take the TCF Canada in Kuwait?", "FEI approves the Institut français du Koweït for the TCF, but on 26 October 2026 its website published no TCF Canada session or fee — only the TEF Canada, at 130 KD. Ask the institute directly."),
         ("How much does the TEF Canada cost in Kuwait?", "130 KD for the four sections at the Institut français du Koweït (26 October 2026), with 5 KD off for the institute’s students."),
         ("Does IRCC accept the TEF Canada?", "Yes: IRCC accepts two French tests, the TCF Canada and the TEF Canada, and converts either result into CLB levels; results are valid for two years."),
         ("Where is the nearest TCF Canada session?", "In Doha at the Institut français du Qatar (1,300 QAR, 16 December 2026), in Saudi Arabia at the Alliance française d’Arabie Saoudite (1,950 SAR), and in Dubai and Abu Dhabi (1,800 AED).")],
    also=[("/en/tcf-canada-qatar/", "TCF Canada in Qatar", "Doha, 1,300 QAR."),
          ("/en/tcf-vs-tef-canada/", "TCF vs TEF Canada", "The two French tests IRCC accepts, side by side."), _PRACTICE],
    sources="the Institut français du Koweït’s exam pages (ifk.edu.kw: French exams, TEF, diplomas and tests), checked on 26 October 2026.",
    badges={KW: [("part", "TCF Canada not published"), ("ok", "TEF Canada 130 KD")]},
    urls={KW: "https://ifk.edu.kw/exams-3/french/?lang=en"},
    notes={KW: "The website on FEI’s list, institutfrancais-koweit.com, did not open on 26 October 2026; the institute’s site is ifk.edu.kw."},
))
