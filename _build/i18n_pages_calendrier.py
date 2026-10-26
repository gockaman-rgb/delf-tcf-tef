# -*- coding: utf-8 -*-
"""Calendrier DELF-DALF 2026-2027 en anglais et en espagnol (17/10/2026), ajouté à i18n_pages_en.py et i18n_pages_es.py — traductions de
/blog/calendrier-delf-dalf-2026-2027/ (articles_dates.py, relevés du 17/09/2026).

Aucun fait nouveau : chaque date vient de la page française, avec sa date de relevé. Le calendrier français est
celui de la France ; hors de France, chaque pays fixe ses dates. Sections ajoutées, faites de faits déjà publiés :
en anglais, « DELF dates outside France » (/en/delf-usa/ et /en/delf-uk/ relevés le 08/10/2026, /en/delf-dubai/ le
13/10/2026) ; en espagnol, « Las fechas del DELF en España » (calendrier 2027 de /es/delf-espana/, PDF du CNE du
22/09/2026 consulté le 08/10/2026).
"""
from pays_config import table

PAGES = []
FR = "/blog/calendrier-delf-dalf-2026-2027/"


# ===========================================================================
# ENGLISH — DELF exam dates 2027 (from /blog/calendrier-delf-dalf-2026-2027/)
# ===========================================================================
PAGES.append(dict(
    fr_path=FR, lang="en", variant="en-GB", section="en", slug="delf-exam-dates-2027", accent="accent-delf",
    crumbs=[("Home", "/en/")], crumb="DELF exam dates 2027", inline_cta=False,
    published="2026-10-17", modified="2026-10-26", date_label="26 October 2026",
    title="DELF exam dates 2027: sessions in France and by country",
    desc="DELF and DALF exam dates 2027, A1 to C2: France’s ten sessions, then Korea, Japan, Taiwan, Hong Kong, Turkey, Vietnam, India, Lebanon — and how to book.",
    h1="DELF and DALF exam dates 2026–2027: France’s calendar and the dates country by country",
    intro="""<strong>DELF exam dates are set country by country.</strong> In France, the DELF and DALF <em lang="fr">tout
public</em> — the versions for adults — have <strong>ten national sessions a year</strong>, set by France Éducation
international: in 2027 the written papers start on <strong>12–14 January</strong>, then 2–4 February and 16–18 March.
Abroad, <strong>Taiwan</strong> has published 2027 (10 January in Taipei, then May and November); Korea, Japan, Hong Kong,
Turkey, Vietnam, India and Lebanon had not on 26 October 2026 — see the <a href="#by-country">dates by country</a>. You
book with an approved centre, never with FEI. In France, sessions are <strong>never in April or September</strong>; the
last three of 2026 have their written papers on <strong>6–8 October, 3–5 November and 1–3 December</strong>, and each
centre opens only some of them and closes registration <strong>four to ten weeks before the written papers</strong> —
sometimes over just two days.""",
    facts=["<strong>By country</strong>: Taiwan (from 10 January), Germany, Switzerland, Italy, Greece and Ireland had published their 2027 sessions; South Korea, Japan, Hong Kong, mainland China, Singapore, Turkey, Vietnam, India, Lebanon, Thailand, Egypt, Nigeria, the US and the UAE had published only 2026 on 26 October 2026 — <a href=\"#by-country\">the table</a>.",
           "<strong>10 national sessions a year</strong> in France: January, February, March, May, June, July, August, October, November, December.",
           "<strong>2026</strong>: 6–8 October, 3–5 November, 1–3 December. <strong>2027</strong>: 12–14 Jan, 2–4 Feb, 16–18 Mar, 25–27 May, 15–17 Jun, 6–8 Jul, 3–5 Aug, 5–7 Oct, 16–18 Nov, 7–9 Dec.",
           "Each centre <strong>chooses its sessions</strong>: Nantes Université opens four a year, the Alliance française de Lyon all ten.",
           "Registration closes <strong>4 to 10 weeks before</strong>: until 4 October for November at the Alliance française de Paris, just two days (22–23 September) for December in Nantes.",
           "Results within <strong>4 to 6 weeks</strong>; the diploma is <strong>valid for life</strong>.",
           "<strong>Adults</strong> take the DELF-DALF <em lang=\"fr\">tout public</em>, with no upper age limit; you book with an approved centre in your country — <a href=\"#booking\">how</a>."],
    toc=[("by-country", "DELF 2027 dates by country"), ("adults", "Can adults take the DELF?"),
         ("booking", "How do I book the DELF?"),
         ("calendar", "France’s national calendar, 2026–2027"),
         ("centres", "What centres do with it: the sessions we found"),
         ("registration", "Registration windows"), ("choosing", "Choosing your session"),
         ("outside-france", "The UK, the US and the UAE in detail")],
    body="""
<div class="stats">
<div class="stat"><b>10</b><span>sessions a year</span><em>never in April or September</em></div>
<div class="stat"><b>3</b><span>autumn 2026 sessions</span><em>6–8 Oct, 3–5 Nov, 1–3 Dec</em></div>
<div class="stat"><b>4–10</b><span>weeks before</span><em>to register</em></div>
<div class="stat"><b>Lifetime</b><span>diploma validity</span><em>results within 4 to 6 weeks</em></div>
</div>

<h2 id="by-country">DELF 2027 dates by country</h2>
<p>France’s calendar does not apply abroad: each country’s DELF-DALF body sets its own sessions, and the dates rarely
match. What the official sites showed on 26 October 2026 — when 2027 was not yet published, the table gives the next
2026 session:</p>
""" + table("Next DELF-DALF tout public sessions by country (written papers), from the official sites checked on 26 October 2026; the UK and the US from our country pages (8 October 2026), Spain from our Spanish page (8 October 2026). “Not published”: no 2027 date on the official site that day.",
            ["Country", "Next sessions", "Registration", "Official site", "Our page"],
            [("France", "2027: 12–14 Jan, 2–4 Feb, 16–18 Mar, then May to December", "At each centre, 4 to 10 weeks before", "france-education-international.fr", "<a href=\"#calendar\">Below</a>"),
             ("<strong>Taiwan</strong>", "<strong>2027 published</strong>: B1, B2 10 Jan (Taipei) · 7 and 14 May · C2 27 Jun · Taichung 3–4 Jul · 12 and 19 Nov", "3–17 Nov 2026 for January", "alliancefrancaise.org.tw", "<a href=\"/en/delf-exam-dates-2027-taiwan/\">Taiwan</a>"),
             ("South Korea", "2027 not published · B1, B2 7–8 Nov; A1, A2, DALF 21–22 Nov 2026", "Closed 14 Oct 2026", "delf-dalf.co.kr", "<a href=\"/en/delf-exam-dates-2027-south-korea/\">South Korea</a>"),
             ("Japan", "2027 not published · 7–8 Nov 2026", "Closed 3 Oct 2026", "delfdalf.jp", "<a href=\"/en/delf-exam-dates-2027-japan/\">Japan</a>"),
             ("Hong Kong", "2027 not published · DELF Junior 1–8 Dec 2026", "Junior: until 30 Oct 2026", "afhongkong.org", "<a href=\"/en/delf-exam-dates-2027-hong-kong/\">Hong Kong</a>"),
             ("Turkey", "2027 not published · B2 16 Nov, C1 17 Nov 2026", "Closed 9 Oct 2026", "ifturquie.org", "<a href=\"/en/delf-exam-dates-2027-turkey/\">Turkey</a>"),
             ("Vietnam", "2027 not published · 14–22 Nov 2026", "19–30 Oct 2026", "ifv.vn", "<a href=\"/en/delf-exam-dates-2027-vietnam/\">Vietnam</a>"),
             ("India", "2027 not published · 7–11 Dec 2026", "9–24 Nov 2026", "Alliances Françaises (afdelhi.org)", "<a href=\"/en/delf-exam-dates-2027-india/\">India</a>"),
             ("Lebanon", "2027 not published · B1 to C2 24–27 Nov 2026", "Until 30 Oct 2026", "institutfrancais-liban.com", "<a href=\"/en/delf-exam-dates-2027-lebanon/\">Lebanon</a>"),
             ("China (mainland)", "2027 not published · DALF 7–8 Nov, B2 14–15 Nov, A1 to B1 21–22 Nov 2026", "Closed 22 Sep 2026", "delf-dalf.neea.edu.cn", "<a href=\"/en/delf-exam-dates-2027-china/\">China</a>"),
             ("Singapore", "2027 not published · 23–27 Nov 2026", "Closed 18 Oct 2026", "alliancefrancaise.org.sg", "<a href=\"/en/delf-exam-dates-2027-singapore/\">Singapore</a>"),
             ("Thailand", "2027 not published · 2026 adult sessions on 8 Mar, 7 Jun and 1 Nov (Bangkok)", "Closed 27 Sep 2026", "afthailande.org", "<a href=\"/en/delf-exam-dates-2027-thailand/\">Thailand</a>"),
             ("Egypt", "2027 not published · C1 7 Nov to B1 28 Nov 2026", "Closed 1 Oct 2026", "ifegypte.com", "<a href=\"/en/delf-exam-dates-2027-egypt/\">Egypt</a>"),
             ("Nigeria", "2027 not published · 8–11 Dec 2026 (Lagos)", "1 Oct – 27 Nov 2026", "afnigeria.org/lagos", "<a href=\"/en/delf-exam-dates-2027-nigeria/\">Nigeria</a>"),
             ("Madagascar", "Adult dates not published online · DELF Prim April 2027 (Antananarivo)", "Ask your Alliance française", "afantananarivo.mg", "<a href=\"/en/delf-exam-dates-2027-madagascar/\">Madagascar</a>"),
             ("United Arab Emirates", "2027 not published · 11 Dec 2026 (Dubai)", "Online, first come, first served", "afdubai.org", "<a href=\"/en/delf-dubai/\">Dubai</a>"),
             ("United Kingdom", "B1 10 Mar, B2 15 Mar, C1 18 Mar 2027 · B1 2 Jun, B2 7 Jun, C1 10 Jun 2027", "At each centre", "—", "<a href=\"/en/delf-uk/\">UK</a>"),
             ("United States", "2027 not published · 7–11 Dec 2026", "Until 7–30 Nov 2026, by centre", "—", "<a href=\"/en/delf-usa/\">USA</a>"),
             ("Spain", "10–12 Feb 2027, then June, September, October", "1 Dec 2026 – 9 Jan 2027", "delf-dalf.es", "<a href=\"/es/fechas-delf-2027/\" hreflang=\"es\" lang=\"es\">Fechas DELF 2027</a>"),
             ("<strong>Germany</strong>", "<strong>2027 published</strong>: B2 22 Jan, 12 Mar, 11 Jun, 24 Sep, 19 Nov 2027 · next 20 Nov 2026", "At each Institut français", "institutfrancais.de", "<a href=\"/en/delf-germany/\">Germany</a>"),
             ("<strong>Switzerland</strong>", "<strong>2027 published</strong>: 20 Mar, 22 May, 19 Jun, 18 Sep, 13 Nov 2027", "For March: until 8 Jan 2027", "delfdalf.ch", "<a href=\"/en/delf-switzerland/\">Switzerland</a>"),
             ("<strong>Italy</strong>", "<strong>2027 published</strong>: B2 25 Feb, 8 Apr, 16 Jun 2027", "For February: 2 Nov – 4 Dec 2026", "Instituts français, Alliances françaises", "<a href=\"/en/delf-italy/\">Italy</a>"),
             ("<strong>Greece</strong>", "<strong>2027 published</strong>: B2 Saturday 15 May 2027 · December 2026 session closed", "1–15 Feb 2027", "ifg.gr", "<a href=\"/en/delf-greece/\">Greece</a>"),
             ("<strong>Ireland</strong>", "<strong>2027 published</strong> (Limerick): B2 18 Feb, 22 Apr, 24 Jun, 23 Sep, 25 Nov 2027 · Dublin 24–27 Nov 2026", "At each Alliance française", "alliance-francaise.ie", "<a href=\"/en/delf-ireland/\">Ireland</a>"),
             ("Netherlands", "2027 partly published: Amsterdam 9–11 Mar and 7–11 Jun 2027", "At each Alliance française", "afamsterdam.nl", "<a href=\"/en/delf-netherlands/\">Netherlands</a>"),
             ("Austria", "Vienna 27–29 Jan 2027 (B2 on the 29th) · Graz in May 2027", "At the Institut français", "institutfrancais.at", "<a href=\"/en/tcf-canada-austria/#delf\">Austria</a>"),
             ("Belgium", "2027 not set · 17–26 Nov 2026 (B2 on the 19th)", "Ghent: until 3 Nov 2026", "alliancefr.be", "<a href=\"/en/delf-belgium/\">Belgium</a>"),
             ("Romania", "2027 not published · 14–15 Nov 2026", "Until 3 Nov 2026", "institutfrancais.ro", "<a href=\"/en/delf-romania/\">Romania</a>"),
             ("Poland", "2027 not published · 16–20 Nov 2026 (B2 on the 18th)", "Until 6 Nov 2026 (Alliances)", "institutfrancais.pl", "<a href=\"/en/delf-poland/\">Poland</a>"),
             ("Portugal", "2027 not published · 19–20 Nov 2026", "Until 6 Nov 2026", "ifp-lisboa.com", "<a href=\"/en/delf-portugal/\">Portugal</a>"),
             ("Sweden", "2027 not published · 2026 sessions in March, May and 3–5 Nov", "At each centre", "ifsuede.com", "<a href=\"/en/delf-sweden/\">Sweden</a>"),
             ("Luxembourg", "B2 9–11 Nov 2026 (full) · A2 in Feb 2027", "At the Institut national des langues", "inll.lu", "<a href=\"/en/tcf-canada-luxembourg/#delf\">Luxembourg</a>")]) + """
<p>Fees differ as much as dates: for the DELF B2, 290,000 won in Korea, ¥24,500 in Japan, NTD 5,000 in Taiwan (2027),
HK$2,300 in Hong Kong, 5,850 TL in Turkey, 2,900,000 VND in Vietnam, ₹13,263 at the Alliance Française de Delhi, 170 €
in Lebanon, 3,600 THB in Bangkok, 5,265 EGP in Egypt, 2,000 yuan in mainland China, S$380 in Singapore and ₦80,000 at
the Alliance Française de Lagos. In Europe: €201 at the Instituts français in Germany, CHF 370 to 390 in Switzerland, €160
in Italy and Greece, €145 in Dublin, €175 in Amsterdam, €191 in Ghent, 620 zł in Poland, €140 in Portugal and SEK 1,450
in Sweden. Latin America has its own calendars, in Spanish:
<a href="/es/delf-mexico/" hreflang="es" lang="es">México</a>, <a href="/es/delf-colombia/" hreflang="es" lang="es">Colombia</a>,
<a href="/es/delf-argentina/" hreflang="es" lang="es">Argentina</a>, <a href="/es/delf-chile/" hreflang="es" lang="es">Chile</a>,
<a href="/es/delf-peru/" hreflang="es" lang="es">Perú</a>, <a href="/es/delf-ecuador/" hreflang="es" lang="es">Ecuador</a>.
For any other country, France Éducation international’s list of approved centres names the national body that publishes
the dates.</p>

<h2 id="adults">Can adults take the DELF?</h2>
<p>Yes. The DELF and DALF <em lang="fr">tout public</em> are the versions for adults, with <strong>no upper age
limit</strong>; teenagers can take the DELF junior and children the DELF Prim, which lead to the same diploma, valid for
life. Some countries reserve the junior for school-age candidates — in South Korea, every candidate of secondary-school
age is counted as a junior — and the Alliance Française de Dubai’s adult session is for candidates aged 18 and over.</p>

<h2 id="booking">How do I book the DELF?</h2>
<p>With an <strong>approved centre</strong>, never with France Éducation international. In France, on the centre’s
website or at its desk. Abroad, through the country’s DELF-DALF body, Institut français or Alliance française: online in
South Korea (delf-dalf.co.kr), Hong Kong and Dubai; at the desk or in an online shop in Japan; in person or online in
Taiwan; with a form and a copy of your ID or passport in Vietnam. Registration closes weeks before the written papers,
places are limited, and fees are generally non-refundable — book as soon as the window opens. Then prepare on the real
format: <a href="/en/delf-b2-practice-test/">DELF B2 practice test and official sample papers</a>.</p>

<h2 id="calendar">France’s national DELF-DALF calendar, 2026–2027</h2>
<p>Every year, France Éducation international publishes the calendar of the DELF-DALF <strong><em lang="fr">tout
public</em></strong> sessions in France (the Prim, junior and school versions have their own dates). The dates below
are those of the <strong>group written papers</strong>; the individual speaking test is held around the written
papers, on a notice from the centre — up to two weeks later in Lille or Bordeaux.</p>
""" + table("National DELF-DALF tout public sessions in France. Source: France Éducation international’s 2026 and 2027 calendars, checked on 17 September 2026. Each centre chooses which sessions it opens.",
            ["Month", "2026 (written papers)", "2027 (written papers)"],
            [("January", "13–15 January", "12–14 January"), ("February", "3–5 February", "2–4 February"),
             ("March", "3–5 March", "16–18 March"), ("April", "—", "—"), ("May", "19–21 May", "25–27 May"),
             ("June", "9–11 June", "15–17 June"), ("July", "7–9 July", "6–8 July"), ("August", "18–20 August", "3–5 August"),
             ("September", "—", "—"), ("October", "<strong>6–8 October</strong>", "<strong>5–7 October</strong>"),
             ("November", "<strong>3–5 November</strong>", "<strong>16–18 November</strong>"),
             ("December", "<strong>1–3 December</strong>", "<strong>7–9 December</strong>")], wide=False) + """
<p>Within a session, each level has its own day: at the DEFLE in Bordeaux, in December 2026, A1 and A2 candidates sit
on the 1st, B1 and B2 on the 2nd, the DALF on the 3rd. The DALF C1 and every DELF level, from A1 to B2, therefore share
these ten sessions, each on its own day.</p>

<p><strong>This calendar is France’s.</strong> Outside France, the dates are set country by country, and they don’t
necessarily match: in the UK, for example, the December 2026 written papers run from 2 to 14 December depending on the
level. See the <a href="#by-country">dates by country</a>.</p>

<h2 id="centres">What centres do with it: the sessions we found</h2>
<p>The national calendar is a <strong>menu</strong>, not a promise: each centre picks the sessions it opens and
announces them on its website. What the main centres in France showed on 17 September 2026:</p>
""" + table("Sessions opened by a few approved centres in France, according to their websites on 17 September 2026.",
            ["Centre", "Sessions", "Next written paper found", "Registration"],
            [("<strong>Alliance française de Lyon</strong>", "All ten sessions of the year", "2 December 2026 (October and November full)", "As early as possible: full two months ahead"),
             ("<strong>Alliance française de Paris</strong>", "Several a year", "3–4 November 2026, speaking tests 13–20 November", "Until 4 October"),
             ("<strong>Cours de civilisation française de la Sorbonne</strong>", "June, July, October, December", "2 December 2026", "From 12 October to 8 November"),
             ("<strong>Université Sorbonne Nouvelle</strong>", "Two a year (February, May)", "February 2027", "Three weeks, ten weeks before"),
             ("<strong>Nantes Université</strong>", "Four a year", "2–4 December 2026, then 17–19 March, 26–28 May, 16–18 June 2027", "Two days, from 7 am: 22–23 Sept, 9–10 Feb, 20–21 April, 11–12 May"),
             ("<strong>Alliance française de Lille</strong>", "June and November found", "3–5 November 2026, speaking tests until the 18th", "From 30 September (10 am) to 7 October (11:59 pm)"),
             ("<strong>DEFLE Bordeaux Montaigne</strong>", "—", "1–3 December 2026, speaking test between the 1st and the 15th", "From 2 October to 4 November")]) + """
<p>Several of these windows have closed since 17 September: the centre’s website is always the reference. Our city
pages, in French, detail each centre with its contacts and fees:
<a href="/centres/delf-paris/" hreflang="fr" lang="fr">Paris</a>, <a href="/centres/delf-lyon/" hreflang="fr" lang="fr">Lyon</a>,
<a href="/centres/delf-lille/" hreflang="fr" lang="fr">Lille</a>, <a href="/centres/delf-nantes/" hreflang="fr" lang="fr">Nantes</a>,
<a href="/centres/delf-bordeaux/" hreflang="fr" lang="fr">Bordeaux</a>, <a href="/centres/delf-marseille/" hreflang="fr" lang="fr">Marseille</a>,
<a href="/centres/delf-toulouse/" hreflang="fr" lang="fr">Toulouse</a>, <a href="/centres/delf-montpellier/" hreflang="fr" lang="fr">Montpellier</a>,
<a href="/centres/delf-strasbourg/" hreflang="fr" lang="fr">Strasbourg</a>.</p>

<h2 id="registration">Registration windows</h2>
<p>This is the real constraint of the calendar. A DELF centre orders its exam papers from FEI several weeks before the
written papers, so registration closes <strong>four to ten weeks before</strong>, and some centres open only a
<strong>short window</strong> — a week in Lille, three weeks at the Sorbonne Nouvelle, <strong>two days in
Nantes</strong>, “subject to available places”. At others, the window is long but the session fills up: at the
Alliance française de Lyon, October and November 2026 were already full on 17 September.</p>

<p>Documents and payment are the same everywhere: a valid ID, your candidate number if you have already taken a DELF,
payment by card, and <strong>non-refundable</strong> fees. One more rule at the Alliance française Aix-Marseille:
“you cannot re-register for the DELF/DALF at the same level until the results of the previous session have been
announced”.</p>

<h2 id="choosing">Choosing your session</h2>
<p>Count backwards from the date by which you need the diploma. <strong>Results</strong> arrive within four to six
weeks (six at the Alliance française de Paris and in Lyon), and with them the provisional pass certificate
(<em lang="fr">attestation de réussite</em>), which is enough for most authorities; the diploma itself comes later. So a
<strong>December 2026</strong> session gives you a result in January 2027: for a French citizenship or resident-card
application to be filed in the spring, it is the last stress-free one.</p>

<p>If the date is too close to register — or if your centre’s sessions are full — there are two ways out: another
approved centre in the region, which won’t necessarily have the same sessions or the same fees (from €125 to €280 for a
B2: see <a href="/en/delf-b2/#dates-fees">DELF B2 dates and fees</a>), or a test — the <a href="/en/tcf-irn/">TCF
IRN</a> is held almost every week, but its results certificate is valid for two years, whereas the DELF is valid for
life (<a href="/en/delf-b1/#diploma-or-test">diploma or test: which to choose</a>). The level pages explain each exam:
<a href="/en/delf-b1/">DELF B1</a>, <a href="/en/delf-b2/">DELF B2</a>, <a href="/en/dalf-c1/">DALF C1 and C2</a>;
our guide to where to take the DELF in France,
<a href="/blog/ou-passer-le-delf-en-france/" hreflang="fr" lang="fr">Où passer le DELF en France ?</a>, is in
French.</p>

<h2 id="outside-france">The UK, the US and the UAE in detail</h2>
<p>France’s calendar doesn’t apply abroad: each country sets its own session dates, and you register with a centre
there. Our pages for the UK, the US and the UAE give more detail (the other countries have their own pages:
<a href="#by-country">dates by country</a>):</p>
<ul>
<li><strong>United Kingdom</strong>: the written papers fall on the same days at every centre — December 2026 (B1 on
the 2nd, B2 on the 3rd, C1 on the 9th; registration in London from 15 to 29 October), then March 2027 (B1 on 10 March,
B2 on 15 March, C1 on 18 March) and June 2027 (B1 on 2 June, B2 on 7 June, C1 on 10 June), as the centres’ websites
showed on 8 October 2026. <a href="/en/delf-uk/">DELF in the UK</a>.</li>
<li><strong>United States</strong>: the next <em lang="fr">tout public</em> session runs from 7 to 11 December 2026 — A1
and A2 on Monday, B1 on Tuesday, B2 on Wednesday, C1 on Thursday, C2 on Friday — with registration closing between
7 November (Houston) and 30 November (Chicago); no 2027 dates had been published on 8 October 2026.
<a href="/en/delf-usa/">DELF in the USA</a>.</li>
<li><strong>United Arab Emirates</strong>: the Alliance Française de Dubai’s next adult session is on Friday
11 December 2026, as published on 13 October 2026 and still on 26 October 2026, with no 2027 session yet.
<a href="/en/delf-dubai/">DELF in Dubai and the UAE</a>.</li>
</ul>
""",
    faq=[("What are the DELF exam dates for autumn 2026?", "In France, the written papers of 6–8 October, 3–5 November and 1–3 December 2026, according to France Éducation international’s national calendar — each centre opens only some of these sessions, and its registration closes four to ten weeks before. Other countries set their own dates."),
         ("What are the DELF exam dates in 2027?", "In France: 12–14 January, 2–4 February, 16–18 March, 25–27 May, 15–17 June, 6–8 July, 3–5 August, 5–7 October, 16–18 November and 7–9 December 2027 (written papers), according to FEI’s 2027 calendar checked on 17 September 2026. Each centre opens only some of these sessions."),
         ("When are the DALF C1 and DELF B1 exam dates in 2027?", "In France, the DALF and every DELF level share the same ten national sessions, so the 2027 dates are the ones above; within a session, each level has its own day (at the DEFLE in Bordeaux in December 2026: B1 and B2 on the 2nd, the DALF on the 3rd). Abroad, the dates differ: in the UK, for example, the B1 falls on 10 March and 2 June 2027, the C1 on 18 March and 10 June 2027."),
         ("Why is there no DELF in April or September in France?", "FEI’s national calendar has no tout public session in those two months, in 2026 as in 2027: ten sessions a year, one a month the rest of the year."),
         ("When should I register for the DELF?", "As soon as your centre opens registration: four to ten weeks before the written papers, with windows that are sometimes very short — two days at Nantes Université, a week at the Alliance française de Lille — and sessions full two months ahead in Lyon."),
         ("What are the DELF exam dates 2027 outside France?", "Each country sets its own. On 26 October 2026, Taiwan had published its 2027 sessions (B1 and B2 on 10 January in Taipei, then May, June, July and November); South Korea, Japan, Hong Kong, mainland China, Singapore, Turkey, Vietnam, India, Lebanon, Thailand, Egypt, Nigeria, the US and the UAE had published only 2026. In the UK, the B1 falls on 10 March and 2 June 2027; in Spain, the February 2027 written papers run from 10 to 12 February."),
         ("Can adults take the DELF?", "Yes. The DELF and DALF tout public are the versions for adults, with no upper age limit; teenagers can take the DELF junior and children the DELF Prim, which lead to the same diploma. Some countries reserve the junior for school-age candidates — in South Korea, every candidate of secondary-school age is a junior — and the Alliance Française de Dubai’s adult session is for candidates aged 18 and over."),
         ("How do I book the DELF?", "With an approved centre, never with France Éducation international: in France, on the centre’s website or at its desk; abroad, through the country’s DELF-DALF body, Institut français or Alliance française — online in South Korea, Hong Kong and Dubai, at the desk or in an online shop in Japan, with a form and a copy of your ID in Vietnam. Registration closes weeks before the written papers, and fees are generally non-refundable."),
         ("Are DELF dates the same outside France?", "Not necessarily: the calendar on this page is France’s, and each country sets its own dates. In the UK, the December 2026 written papers run from 2 to 14 December depending on the level; in the US, the next session is from 7 to 11 December 2026; in Dubai, on 11 December 2026. The exact date and registration window are always the centre’s: check its website.")],
    also=[("/en/delf-b2/", "DELF B2 exam: format, scoring, dates", "The four sections, the 50/100 pass mark, and fees in France, the UK and the US."),
          ("/en/delf-b1/", "DELF B1 exam", "The threshold level: format, scoring, and the French resident card."),
          ("/en/dalf-c1/", "DALF C1 and C2", "The advanced level: format, the synthesis task, dates and fees."),
          ("/en/delf-uk/", "DELF in the UK", "The approved centres, the sessions to June 2027 and the fees.")],
    sources="""<strong>Sources.</strong> France Éducation international’s calendars of the 2026 and 2027 DELF-DALF
<em lang="fr">tout public</em> sessions, checked on 17 September 2026; the DELF-DALF pages of the centres cited — the
Alliance française de Paris, the Alliance française de Lyon, the Cours de civilisation française de la Sorbonne, the
Université Sorbonne Nouvelle, Nantes Université (page dated 14 September 2026), the Alliance française de Lille
Métropole, the DEFLE at Université Bordeaux Montaigne, the Alliance française Aix-Marseille Provence — checked on
17 September 2026. Dates outside France come from our country pages: the UK and the US, checked on 8 October 2026; the
UAE, on 13 October 2026 and again on 26 October 2026. The dates by country come from the official sites, checked on
26 October 2026: delf-dalf.co.kr (South Korea), delfdalf.jp (Japan), the Alliance française de Taiwan, the Alliance
Française de Hong Kong, the Institut français de Turquie, the Institut français du Vietnam, the Alliance Française de
Delhi (India), the Institut français du Liban, the Alliance Française de Bangkok, the Institut français d’Égypte and the
Alliance Française de Dubai; Spain from our Spanish page (Centro Nacional de Exámenes, 8 October 2026). Dates and
registration windows change: the centre’s website is the reference.""",
))


# ===========================================================================
# ESPAÑOL — Fechas DELF 2027 (de /blog/calendrier-delf-dalf-2026-2027/ + calendario de /es/delf-espana/)
# ===========================================================================
PAGES.append(dict(
    fr_path=FR, lang="es", variant="es-ES", section="es", slug="fechas-delf-2027", accent="accent-delf",
    crumbs=[("Inicio", "/es/")], crumb="Fechas DELF 2027", inline_cta=False,
    published="2026-10-17", modified="2026-10-26", date_label="26 de octubre de 2026",
    title="Fechas DELF 2027: calendario de convocatorias DELF-DALF",
    desc="Fechas DELF y DALF 2027: las diez convocatorias de Francia, el calendario de España, América Latina y Asia, los plazos y cómo inscribirse.",
    h1="Fechas del DELF y el DALF 2026-2027: Francia, España y los demás países",
    intro="""<strong>Las fechas del DELF dependen del país.</strong> En Francia, el DELF y el DALF <em lang="fr">tout
public</em> —las versiones para adultos, sin límite de edad— tienen <strong>diez convocatorias nacionales al año</strong>
(en 2027, el escrito empieza el 12-14 de enero); en España, la próxima es la de <strong>febrero de 2027</strong>, con
matrícula del 1 de diciembre de 2026 al 9 de enero de 2027; en América Latina y en Asia, <a href="#por-pais">cada país
publica la suya</a>. Te inscribes en un centro autorizado, nunca en France Éducation international. En Francia, las
convocatorias las fija France Éducation international: una al mes, <strong>nunca en abril ni en septiembre</strong>. Las tres últimas de 2026 tienen sus pruebas escritas el
<strong>6-8 de octubre, el 3-5 de noviembre y el 1-3 de diciembre</strong>; 2027 empieza el 12-14 de enero. Pero cada
centro abre solo una parte de esas convocatorias y cierra la matrícula <strong>de cuatro a diez semanas antes del
escrito</strong>, a veces en solo dos días. Ese es el calendario de Francia: <strong>cada país fija sus
fechas</strong>, y España tiene el suyo, con la próxima convocatoria en <strong>febrero de 2027</strong>. El
calendario francés completo, los plazos de matrícula que encontramos, el calendario español y cómo no perder tu
convocatoria.""",
    facts=["<strong>10 convocatorias al año</strong> en Francia, nacionales: enero, febrero, marzo, mayo, junio, julio, agosto, octubre, noviembre y diciembre.",
           "<strong>2026</strong>: 6-8 de octubre, 3-5 de noviembre, 1-3 de diciembre. <strong>2027</strong>: 12-14 de enero, 2-4 de febrero, 16-18 de marzo, 25-27 de mayo, 15-17 de junio, 6-8 de julio, 3-5 de agosto, 5-7 de octubre, 16-18 de noviembre y 7-9 de diciembre.",
           "Cada centro <strong>elige sus convocatorias</strong>: Nantes Université abre cuatro al año; la Alliance française de Lyon, las diez.",
           "Matrícula cerrada <strong>de 4 a 10 semanas antes</strong>: hasta el 4 de octubre para noviembre en la Alliance française de Paris; solo dos días (22-23 de septiembre) para diciembre en Nantes.",
           "Resultados en un plazo de <strong>4 a 6 semanas</strong>; diploma <strong>válido de por vida</strong>.",
           "⚠️ <strong>En España, otro calendario</strong>: próxima convocatoria en febrero de 2027 (pruebas escritas del 10 al 12 de febrero), "
           "con matrícula del <strong>1 de diciembre de 2026 al 9 de enero de 2027</strong>.",
           "<strong>Otros países</strong>: Taiwán ya publicó 2027 (desde el 10 de enero); México, Colombia, Argentina, Chile, Perú, Ecuador y los países de Asia aún no, el 26 de octubre de 2026 — <a href=\"#por-pais\">la tabla</a>."],
    toc=[("calendario", "El calendario nacional de Francia, 2026-2027"),
         ("espana", "Las fechas del DELF en España"),
         ("por-pais", "Las fechas del DELF en otros países"), ("adultos", "Adultos e inscripción"),
         ("centros", "Lo que hacen los centros en Francia: las convocatorias que encontramos"),
         ("matricula", "Los plazos de matrícula"), ("elegir", "Elegir tu convocatoria")],
    body="""
<div class="stats">
<div class="stat"><b>10</b><span>convocatorias al año en Francia</span><em>nunca en abril ni en septiembre</em></div>
<div class="stat"><b>3</b><span>convocatorias en otoño de 2026</span><em>6-8 oct., 3-5 nov., 1-3 dic.</em></div>
<div class="stat"><b>4-10</b><span>semanas antes</span><em>para matricularse</em></div>
<div class="stat"><b>De por vida</b><span>validez del diploma</span><em>resultados en 4 a 6 semanas</em></div>
</div>

<h2 id="calendario">El calendario nacional de Francia, 2026-2027</h2>
<p>France Éducation international publica cada año el calendario de las convocatorias DELF-DALF <strong><em
lang="fr">tout public</em></strong> en Francia (las versiones Prim, junior y escolar tienen sus propias fechas). Las
fechas de la tabla son las de las <strong>pruebas escritas colectivas</strong>; el oral individual se celebra en torno
al escrito, con la citación del centro: hasta dos semanas después en Lille o en Burdeos.</p>
""" + table("Convocatorias nacionales DELF-DALF tout public en Francia. Fuente: calendarios de 2026 y 2027 de France Éducation international, consultados el 17 de septiembre de 2026. Cada centro elige las convocatorias que abre.",
            ["Mes", "2026 (escritos)", "2027 (escritos)"],
            [("Enero", "13-15 de enero", "12-14 de enero"), ("Febrero", "3-5 de febrero", "2-4 de febrero"),
             ("Marzo", "3-5 de marzo", "16-18 de marzo"), ("Abril", "—", "—"), ("Mayo", "19-21 de mayo", "25-27 de mayo"),
             ("Junio", "9-11 de junio", "15-17 de junio"), ("Julio", "7-9 de julio", "6-8 de julio"),
             ("Agosto", "18-20 de agosto", "3-5 de agosto"), ("Septiembre", "—", "—"),
             ("Octubre", "<strong>6-8 de octubre</strong>", "<strong>5-7 de octubre</strong>"),
             ("Noviembre", "<strong>3-5 de noviembre</strong>", "<strong>16-18 de noviembre</strong>"),
             ("Diciembre", "<strong>1-3 de diciembre</strong>", "<strong>7-9 de diciembre</strong>")], wide=False) + """
<p>Dentro de una convocatoria, cada nivel tiene su día: en el DEFLE de Burdeos, en diciembre de 2026, los A1 y A2 se
examinan el día 1, los B1 y B2 el 2 y el DALF el 3. <strong>Este calendario es el de Francia</strong>: fuera de Francia,
cada país fija sus fechas, y no tienen por qué coincidir. España es el ejemplo más claro.</p>

<h2 id="espana">Las fechas del DELF en España</h2>
<p>En España, el DELF y el DALF tienen <strong>un calendario nacional propio</strong>: el Centro Nacional de Exámenes
(delf-dalf.es), vinculado a la Embajada de Francia, fija los mismos días, las mismas horas y los mismos plazos de
matrícula en los 32 centros de examen (lista de FEI del 8 de octubre de 2026), con cuatro convocatorias al año para
adultos: febrero, junio, septiembre y octubre. La convocatoria de octubre de 2026 (pruebas escritas del 19 al 24 de
octubre) está cerrada; sus resultados se publican el 10 de diciembre de 2026. La próxima es la de <strong>febrero de
2027</strong>, con matrícula del <strong>1 de diciembre de 2026 al 9 de enero de 2027</strong>.</p>
""" + table("Calendario DELF-DALF 2027 del Centro Nacional de Exámenes (PDF del 22 de septiembre de 2026), consultado el 8 de octubre de 2026: fechas de las pruebas escritas del DELF tout public y del DALF.",
            ["Convocatoria", "Matrícula", "A1", "A2", "B1", "B2", "C1", "C2", "Resultados"],
            [("<strong>Febrero de 2027</strong>", "<strong>1 dic. 2026 – 9 ene. 2027</strong>", "10/02", "12/02", "12/02", "11/02", "10/02", "11/02", "17 de marzo"),
             ("Junio de 2027", "1 de marzo – 16 de abril", "01/06", "03/06", "03/06", "02/06", "01/06", "02/06", "19 de julio"),
             ("Septiembre de 2027", "1 de julio – 1 de sept.", "28/09", "29/09", "29/09", "28/09", "27/09", "30/09", "2 de noviembre"),
             ("Octubre de 2027", "30 de agosto – 22 de sept.", "21/10", "21/10", "20/10", "19/10", "18/10", "21/10", "13 de diciembre")]) + """
<p>Las pruebas orales se reparten a lo largo de varias semanas en torno a las escritas. La convocatoria de septiembre
está reservada a los adultos y al DALF. No todos los centros abren todas las convocatorias, y algunos tienen su propia
fecha de cierre: la Universidad de Castilla-La Mancha cierra la de febrero el 2 de enero, y el Institut français de
Barcelona, el 10 de enero. Te matriculas en un centro, nunca en el CNE, y la matrícula solo es efectiva con el pago.
Precios de 2027, centros y forma de matricularse: <a href="/es/delf-espana/">DELF en España</a>, y por ciudad,
<a href="/es/delf-madrid/">Madrid</a>, <a href="/es/delf-barcelona/">Barcelona</a>,
<a href="/es/delf-sevilla/">Sevilla</a>, <a href="/es/delf-valencia/">Valencia</a> y
<a href="/es/delf-granada/">Granada</a>.</p>

<h2 id="por-pais">Las fechas del DELF en otros países</h2>
<p>En América Latina, Europa y Asia, cada país también fija sus fechas. Las próximas convocatorias tout public publicadas, y
lo que todavía no lo estaba:</p>
""" + table("Próximas convocatorias DELF-DALF tout public por país (pruebas escritas). América Latina: nuestras páginas por país, consultadas el 8 de octubre de 2026; Europa, Asia, Oriente Medio y África: sitios oficiales consultados el 26 de octubre de 2026.",
            ["País", "Próxima convocatoria", "Matrícula", "Más información"],
            [("México", "9-13 de noviembre de 2026; resultados el 14 de diciembre", "Del 5 al 23 de octubre (cerrada)", "<a href=\"/es/delf-mexico/\">DELF en México</a>"),
             ("Colombia", "3-6 de noviembre de 2026; 2027 no publicado el 8 de octubre", "Cerrada el 9 de octubre", "<a href=\"/es/delf-colombia/\">DELF en Colombia</a>"),
             ("Argentina", "4-5 de diciembre de 2026; 2027 no publicado el 8 de octubre", "Hasta el 5 de noviembre", "<a href=\"/es/delf-argentina/\">DELF en Argentina</a>"),
             ("Chile", "DELF B2: 4-5 de diciembre de 2026", "Hasta el 30 de octubre", "<a href=\"/es/delf-chile/\">DELF en Chile</a>"),
             ("Perú", "28 de noviembre de 2026; 2027 no publicado el 8 de octubre", "Cerrada el 16 de octubre", "<a href=\"/es/delf-peru/\">DELF en Perú</a>"),
             ("Ecuador", "23-27 de noviembre y 8-14 de diciembre de 2026", "Quito: hasta el 6 y el 13 de noviembre", "<a href=\"/es/delf-ecuador/\">DELF en Ecuador</a>"),
             ("<strong>Taiwán</strong>", "<strong>2027 publicado</strong>: B1 y B2 el 10 de enero (Taipéi); mayo, junio, julio y noviembre", "Del 3 al 17 de noviembre de 2026", "<a href=\"/en/delf-exam-dates-2027-taiwan/\" hreflang=\"en\" lang=\"en\">Taiwan</a>"),
             ("Corea del Sur", "2027 no publicado; 7-8 y 21-22 de noviembre de 2026", "Cerrada el 14 de octubre", "<a href=\"/en/delf-exam-dates-2027-south-korea/\" hreflang=\"en\" lang=\"en\">South Korea</a>"),
             ("Japón", "2027 no publicado; 7-8 de noviembre de 2026", "Cerrada el 3 de octubre", "<a href=\"/en/delf-exam-dates-2027-japan/\" hreflang=\"en\" lang=\"en\">Japan</a>"),
             ("Hong Kong", "2027 no publicado; DELF junior 1-8 de diciembre de 2026", "Hasta el 30 de octubre", "<a href=\"/en/delf-exam-dates-2027-hong-kong/\" hreflang=\"en\" lang=\"en\">Hong Kong</a>"),
             ("Turquía", "2027 no publicado; B2 el 16 y C1 el 17 de noviembre de 2026", "Cerrada el 9 de octubre", "<a href=\"/en/delf-exam-dates-2027-turkey/\" hreflang=\"en\" lang=\"en\">Turkey</a>"),
             ("Vietnam", "2027 no publicado; 14-22 de noviembre de 2026", "Del 19 al 30 de octubre", "<a href=\"/en/delf-exam-dates-2027-vietnam/\" hreflang=\"en\" lang=\"en\">Vietnam</a>"),
             ("India", "2027 no publicado; 7-11 de diciembre de 2026", "Del 9 al 24 de noviembre", "<a href=\"/en/delf-exam-dates-2027-india/\" hreflang=\"en\" lang=\"en\">India</a>"),
             ("Líbano", "2027 no publicado; 24-27 de noviembre de 2026", "Hasta el 30 de octubre", "<a href=\"/en/delf-exam-dates-2027-lebanon/\" hreflang=\"en\" lang=\"en\">Lebanon</a>"),
             ("China continental", "2027 no publicado; DALF el 7-8, B2 el 14-15, A1 a B1 el 21-22 de noviembre de 2026", "Cerrada el 22 de septiembre", "<a href=\"/en/delf-exam-dates-2027-china/\" hreflang=\"en\" lang=\"en\">China</a>"),
             ("Singapur", "2027 no publicado; 23-27 de noviembre de 2026", "Cerrada el 18 de octubre", "<a href=\"/en/delf-exam-dates-2027-singapore/\" hreflang=\"en\" lang=\"en\">Singapore</a>"),
             ("Tailandia", "2027 no publicado; 1 de noviembre de 2026 (Bangkok)", "Cerrada el 27 de septiembre", "<a href=\"/en/delf-exam-dates-2027-thailand/\" hreflang=\"en\" lang=\"en\">Thailand</a>"),
             ("Egipto", "2027 no publicado; del 7 (C1) al 28 (B1) de noviembre de 2026", "Cerrada el 1 de octubre", "<a href=\"/en/delf-exam-dates-2027-egypt/\" hreflang=\"en\" lang=\"en\">Egypt</a>"),
             ("Nigeria", "2027 no publicado; 8-11 de diciembre de 2026 (Lagos)", "Del 1 de octubre al 27 de noviembre", "<a href=\"/en/delf-exam-dates-2027-nigeria/\" hreflang=\"en\" lang=\"en\">Nigeria</a>"),
             ("Madagascar", "Fechas para adultos no publicadas en línea; DELF Prim en abril de 2027 (Antananarivo)", "En cada Alliance française", "<a href=\"/en/delf-exam-dates-2027-madagascar/\" hreflang=\"en\" lang=\"en\">Madagascar</a>"),
             ("<strong>Alemania</strong>", "<strong>2027 publicado</strong>: B2 el 22 de enero, 12 de marzo, 11 de junio, 24 de septiembre y 19 de noviembre de 2027", "En cada Institut français", "<a href=\"/en/delf-germany/\" hreflang=\"en\" lang=\"en\">Germany</a>"),
             ("<strong>Suiza</strong>", "<strong>2027 publicado</strong>: 20 de marzo, 22 de mayo, 19 de junio, 18 de septiembre y 13 de noviembre de 2027", "Para marzo: hasta el 8 de enero de 2027", "<a href=\"/en/delf-switzerland/\" hreflang=\"en\" lang=\"en\">Switzerland</a>"),
             ("<strong>Italia</strong>", "<strong>2027 publicado</strong>: B2 el 25 de febrero, 8 de abril y 16 de junio de 2027", "Para febrero: del 2 de noviembre al 4 de diciembre de 2026", "<a href=\"/en/delf-italy/\" hreflang=\"en\" lang=\"en\">Italy</a>"),
             ("<strong>Grecia</strong>", "<strong>2027 publicado</strong>: B2 el sábado 15 de mayo de 2027", "Del 1 al 15 de febrero de 2027", "<a href=\"/en/delf-greece/\" hreflang=\"en\" lang=\"en\">Greece</a>"),
             ("<strong>Irlanda</strong>", "<strong>2027 publicado</strong> (Limerick): B2 el 18 de febrero, 22 de abril, 24 de junio, 23 de septiembre y 25 de noviembre de 2027", "En cada Alliance française", "<a href=\"/en/delf-ireland/\" hreflang=\"en\" lang=\"en\">Ireland</a>"),
             ("Países Bajos", "2027 publicado en parte: Ámsterdam, 9-11 de marzo y 7-11 de junio de 2027", "En cada Alliance française", "<a href=\"/en/delf-netherlands/\" hreflang=\"en\" lang=\"en\">Netherlands</a>"),
             ("Austria", "Viena, 27-29 de enero de 2027 (B2 el 29); Graz en mayo de 2027", "En el Institut français", "<a href=\"/en/tcf-canada-austria/#delf\" hreflang=\"en\" lang=\"en\">Austria</a>"),
             ("Bélgica", "2027 no fijado; 17-26 de noviembre de 2026 (B2 el 19)", "Gante: hasta el 3 de noviembre", "<a href=\"/en/delf-belgium/\" hreflang=\"en\" lang=\"en\">Belgium</a>"),
             ("Rumanía", "2027 no publicado; 14-15 de noviembre de 2026", "Hasta el 3 de noviembre", "<a href=\"/en/delf-romania/\" hreflang=\"en\" lang=\"en\">Romania</a>"),
             ("Polonia", "2027 no publicado; 16-20 de noviembre de 2026 (B2 el 18)", "Hasta el 6 de noviembre (Alliances)", "<a href=\"/en/delf-poland/\" hreflang=\"en\" lang=\"en\">Poland</a>"),
             ("Portugal", "2027 no publicado; 19-20 de noviembre de 2026", "Hasta el 6 de noviembre", "<a href=\"/en/delf-portugal/\" hreflang=\"en\" lang=\"en\">Portugal</a>"),
             ("Suecia", "2027 no publicado; en 2026, marzo, mayo y 3-5 de noviembre", "En cada centro", "<a href=\"/en/delf-sweden/\" hreflang=\"en\" lang=\"en\">Sweden</a>"),
             ("Luxemburgo", "B2 del 9 al 11 de noviembre de 2026 (completo); A2 en febrero de 2027", "En el Institut national des langues", "<a href=\"/en/tcf-canada-luxembourg/#delf\" hreflang=\"en\" lang=\"en\">Luxembourg</a>")]) + """
<p>Las páginas de Europa, Asia, Oriente Medio y África están en inglés; para Estados Unidos, el Reino Unido y los Emiratos, consulta
<a href="/en/delf-exam-dates-2027/#by-country" hreflang="en">la tabla por países, en inglés</a>.</p>

<h2 id="adultos">Adultos e inscripción</h2>
<p><strong>¿Pueden los adultos presentar el DELF?</strong> Sí: el DELF y el DALF <em lang="fr">tout public</em> son las
versiones para adultos, sin límite de edad; los adolescentes pueden presentar el DELF junior y los niños el DELF Prim,
con el mismo diploma, válido de por vida. <strong>¿Cómo inscribirse?</strong> En un centro autorizado —en España, el que
elijas de la red del Centro Nacional de Exámenes; en América Latina, la Alianza Francesa o el Instituto Francés de tu
ciudad—, durante el plazo de matrícula, que se cierra semanas antes del escrito; las tasas no suelen ser
reembolsables.</p>

<h2 id="centros">Lo que hacen los centros en Francia: las convocatorias que encontramos</h2>
<p>El calendario nacional francés es un <strong>menú</strong>, no una promesa: cada centro elige las convocatorias que
abre y las anuncia en su web. Esto es lo que mostraban los principales centros de Francia el 17 de septiembre de
2026:</p>
""" + table("Convocatorias abiertas por algunos centros autorizados de Francia, según su web el 17 de septiembre de 2026.",
            ["Centro", "Convocatorias", "Próximo escrito encontrado", "Matrícula"],
            [("<strong>Alliance française de Lyon</strong>", "Las diez del año", "2 de diciembre de 2026 (octubre y noviembre completos)", "Cuanto antes: completo dos meses antes"),
             ("<strong>Alliance française de Paris</strong>", "Varias al año", "3-4 de noviembre de 2026, orales del 13 al 20 de noviembre", "Hasta el 4 de octubre"),
             ("<strong>Cours de civilisation française de la Sorbonne</strong>", "Junio, julio, octubre, diciembre", "2 de diciembre de 2026", "Del 12 de octubre al 8 de noviembre"),
             ("<strong>Université Sorbonne Nouvelle</strong>", "Dos al año (febrero, mayo)", "Febrero de 2027", "Tres semanas, diez semanas antes"),
             ("<strong>Nantes Université</strong>", "Cuatro al año", "2-4 de diciembre de 2026; después, 17-19 de marzo, 26-28 de mayo y 16-18 de junio de 2027", "Dos días, desde las 7 h: 22-23 de sept., 9-10 de febr., 20-21 de abril, 11-12 de mayo"),
             ("<strong>Alliance française de Lille</strong>", "Junio y noviembre encontrados", "3-5 de noviembre de 2026, orales hasta el 18", "Del 30 de septiembre (10 h) al 7 de octubre (23.59 h)"),
             ("<strong>DEFLE Bordeaux Montaigne</strong>", "—", "1-3 de diciembre de 2026, oral entre el 1 y el 15", "Del 2 de octubre al 4 de noviembre")]) + """
<p>Varios de esos plazos ya se han cerrado desde el 17 de septiembre: la web del centro es siempre la que vale. Nuestras
páginas por ciudad, en francés, detallan cada centro con sus datos de contacto y sus precios:
<a href="/centres/delf-paris/" hreflang="fr" lang="fr">Paris</a>, <a href="/centres/delf-lyon/" hreflang="fr" lang="fr">Lyon</a>,
<a href="/centres/delf-lille/" hreflang="fr" lang="fr">Lille</a>, <a href="/centres/delf-nantes/" hreflang="fr" lang="fr">Nantes</a>,
<a href="/centres/delf-bordeaux/" hreflang="fr" lang="fr">Bordeaux</a>, <a href="/centres/delf-marseille/" hreflang="fr" lang="fr">Marseille</a>,
<a href="/centres/delf-toulouse/" hreflang="fr" lang="fr">Toulouse</a>, <a href="/centres/delf-montpellier/" hreflang="fr" lang="fr">Montpellier</a>,
<a href="/centres/delf-strasbourg/" hreflang="fr" lang="fr">Strasbourg</a>.</p>

<h2 id="matricula">Los plazos de matrícula</h2>
<p>Es la verdadera limitación del calendario. Un centro DELF encarga sus exámenes a FEI varias semanas antes del
escrito: por eso la matrícula se cierra <strong>de cuatro a diez semanas antes</strong>, y algunos centros solo abren
un <strong>plazo corto</strong> —una semana en Lille, tres semanas en la Sorbonne Nouvelle, <strong>dos días en
Nantes</strong>, «hasta agotar las plazas disponibles»—. En otros, el plazo es largo pero la convocatoria se llena: en
la Alliance française de Lyon, octubre y noviembre de 2026 ya estaban completos el 17 de septiembre.</p>

<p>Los documentos y el pago son iguales en todas partes: un documento de identidad en vigor, tu número de candidato si
ya te has presentado a un DELF, pago con tarjeta y unas tasas <strong>no reembolsables</strong>. Una norma más en la
Alliance française Aix-Marseille: «no es posible volver a matricularse en el DELF/DALF del mismo nivel mientras no se
hayan anunciado los resultados de la convocatoria anterior».</p>

<h2 id="elegir">Elegir tu convocatoria</h2>
<p>Cuenta hacia atrás desde la fecha en la que necesitas el diploma. <strong>Los resultados</strong> llegan en un plazo
de cuatro a seis semanas (seis en la Alliance française de Paris y en Lyon) y, con ellos, el certificado provisional
de aprobado (<em lang="fr">attestation de réussite</em>), que basta para la mayoría de las administraciones; el diploma
llega más tarde. Una convocatoria de <strong>diciembre de 2026</strong> da, por tanto, un resultado en enero de 2027:
para un expediente de nacionalidad francesa o de tarjeta de residente que haya que presentar en primavera, es la
última sin agobios.</p>

<p>Si la fecha está demasiado cerca para matricularte —o si las convocatorias de tu centro están completas—, hay dos
salidas: otro centro autorizado de la región, que no tiene por qué tener las mismas convocatorias ni los mismos precios
(de 125 € a 280 € por un B2 en Francia, según nuestra guía en francés
<a href="/blog/ou-passer-le-delf-en-france/" hreflang="fr" lang="fr">Où passer le DELF en France ?</a>), o un
<a href="/es/certificado-de-frances/">test</a>: el TCF IRN se presenta casi todas las semanas, pero su certificado vale
dos años, mientras que el DELF vale de por vida. Cada examen, en detalle: <a href="/es/delf-b1/">DELF B1</a>,
<a href="/es/delf-b2/">DELF B2</a> y <a href="/es/dalf-c1/">DALF C1 y C2</a>.</p>
""",
    faq=[("¿Cuáles son las fechas del DELF en el otoño de 2026?", "En Francia, las pruebas escritas del 6-8 de octubre, el 3-5 de noviembre y el 1-3 de diciembre de 2026, según el calendario nacional de France Éducation international; cada centro abre solo una parte de esas convocatorias y cierra la matrícula de cuatro a diez semanas antes. En España, la convocatoria de octubre de 2026 está cerrada y la próxima es la de febrero de 2027."),
         ("¿Cuáles son las fechas del DELF en 2027?", "En Francia: 12-14 de enero, 2-4 de febrero, 16-18 de marzo, 25-27 de mayo, 15-17 de junio, 6-8 de julio, 3-5 de agosto, 5-7 de octubre, 16-18 de noviembre y 7-9 de diciembre de 2027 (pruebas escritas), según el calendario 2027 de FEI consultado el 17 de septiembre de 2026. En España, el Centro Nacional de Exámenes fija cuatro convocatorias (pruebas escritas del DELF tout public y del DALF): del 10 al 12 de febrero, del 1 al 3 de junio, del 27 al 30 de septiembre y del 18 al 21 de octubre de 2027."),
         ("¿Cuándo es la próxima convocatoria del DELF en España?", "En febrero de 2027: DALF C1 y DELF A1 el 10 de febrero, B2 y C2 el 11, B1 y A2 el 12. La matrícula está abierta del 1 de diciembre de 2026 al 9 de enero de 2027 —algunos centros tienen su propia fecha de cierre, como la Universidad de Castilla-La Mancha (2 de enero) o el Institut français de Barcelona (10 de enero)—, y los resultados se publican el 17 de marzo de 2027."),
         ("¿Por qué no hay DELF en abril ni en septiembre en Francia?", "El calendario nacional de FEI no prevé convocatoria tout public esos dos meses, ni en 2026 ni en 2027: diez convocatorias al año, una al mes el resto del año. En España sí hay convocatoria en septiembre, reservada a los adultos y al DALF."),
         ("¿Cuándo hay que matricularse en el DELF?", "En cuanto tu centro abra la matrícula: de cuatro a diez semanas antes del escrito en Francia, con plazos a veces muy cortos —dos días en Nantes Université, una semana en la Alliance française de Lille— y convocatorias completas dos meses antes en Lyon. En España, la matrícula para febrero de 2027 va del 1 de diciembre de 2026 al 9 de enero de 2027."),
         ("¿Pueden los adultos presentar el DELF?", "Sí. El DELF y el DALF tout public son las versiones para adultos, sin límite de edad; los adolescentes pueden presentar el DELF junior y los niños el DELF Prim, que dan el mismo diploma."),
         ("¿Cómo me inscribo en el DELF?", "En un centro autorizado, nunca en France Éducation international ni en el Centro Nacional de Exámenes: en España, en uno de los centros de la red; en América Latina, en la Alianza Francesa o el Instituto Francés de tu ciudad. La matrícula se cierra semanas antes del escrito y solo es efectiva con el pago."),
         ("¿Las fechas del DELF son las mismas fuera de Francia?", "No necesariamente: el calendario de esta página es el de Francia, y cada país fija sus fechas. En España, el Centro Nacional de Exámenes publica un calendario propio, con convocatorias en febrero, junio, septiembre y octubre de 2027; para México, Colombia o Argentina, consulta la página de cada país. La fecha exacta y el plazo de matrícula son siempre los del centro: compruébalos en su web.")],
    also=[("/es/delf-espana/", "DELF en España: fechas 2027, precios y centros", "El calendario nacional, las tarifas de 2027 y los centros, comunidad por comunidad."),
          ("/es/delf-b2/", "Examen DELF B2", "Las cuatro pruebas, el aprobado con 50/100 y las fechas país por país."),
          ("/es/delf-b1/", "Examen DELF B1", "Estructura, puntuación y fechas por país."),
          ("/es/dalf-c1/", "DALF C1 y C2", "El nivel avanzado: las pruebas, la síntesis y las sesiones por país.")],
    sources="""<strong>Fuentes.</strong> Calendarios de las convocatorias DELF-DALF <em lang="fr">tout public</em> 2026 y
2027 de France Éducation international, consultados el 17 de septiembre de 2026; páginas DELF-DALF de los centros
citados —Alliance française de Paris, Alliance française de Lyon, Cours de civilisation française de la Sorbonne,
Université Sorbonne Nouvelle, Nantes Université (página del 14 de septiembre de 2026), Alliance française de Lille
Métropole, DEFLE de la Université Bordeaux Montaigne, Alliance française Aix-Marseille Provence—, consultadas el 17 de
septiembre de 2026. Para España, calendario DELF-DALF 2027 del Centro Nacional de Exámenes (PDF del 22 de septiembre de
2026), consultado el 8 de octubre de 2026, tal como figura en nuestra página DELF en España. América Latina: nuestras
páginas por país, consultadas el 8 de octubre de 2026; Asia, Oriente Medio y África: los sitios oficiales citados en nuestras páginas en
inglés, consultados el 26 de octubre de 2026. Las fechas y los plazos de matrícula cambian: la web del centro es la que
vale.""",
))
