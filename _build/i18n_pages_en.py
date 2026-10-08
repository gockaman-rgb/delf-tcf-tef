# -*- coding: utf-8 -*-
"""Guides et pages d'examen en anglais (/en/, make_i18n.py) — traductions de pages françaises, 08/10/2026.

Aucun fait nouveau : chaque chiffre, date et règle vient de la page française (fr_path), avec sa date. Les
exercices et sujets restent en français (examen de français) ; consignes et explications en anglais. Anglais
canadien pour le TCF Canada (centre, practise, program), américain pour les pages DELF des États-Unis.
Glossaire : i18n_glossary.md ; blocs : i18n_blocks.py.
"""
from i18n_blocks import CALC_EN, exo, sujet  # noqa: F401
from pays_config import table

PAGES = []
TCF = ("TCF Canada", "/en/tcf-canada/")
HOME = ("Home", "/en/")

# ===========================================================================
# TCF CANADA — score chart and CLB calculator (from /tcf-canada/score-nclc/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/tcf-canada/score-nclc/", lang="en", variant="en-CA", section="en/tcf-canada", slug="score-clb",
    crumbs=[HOME, TCF], crumb="Score and CLB", inline_cta=False,
    title="TCF Canada score chart and CLB calculator (2026)",
    desc="Convert your TCF Canada scores to CLB with the calculator and IRCC’s chart: CLB 7 is 458 in listening, 453 in reading, 10/20 in speaking and writing.",
    h1="TCF Canada scores and CLB levels: the calculator and the chart",
    intro="""In the TCF Canada, listening and reading are scored from 100 to 699, and speaking and writing from 1 to 20;
each score maps to a CEFR level, then to a <strong>CLB level</strong> (NCLC in French) — the only one IRCC reads.
CLB 7 requires 458 in listening, 453 in reading and 10/20 in both speaking and writing — so a “B2” on your results
certificate isn’t always enough. Here are both tables, and what they mean for your application.""",
    facts=["Listening and reading scored out of <strong>699</strong>, speaking and writing out of <strong>20</strong>.",
           "<strong>CLB 7</strong> = 458 in listening, 453 in reading, 10/20 in speaking and in writing.",
           "<strong>CLB 9</strong> = 523 in listening and 524 in reading, 14/20 in speaking and in writing.",
           "⚠️ B2 starts at 400: a B2 of 420 in listening is only worth CLB 6.",
           "For sessions held since 1 September 2026, re-marking is no longer possible."],
    toc=[("calculator-title", "TCF Canada → CLB calculator"), ("scoring", "How you are scored"),
         ("tcf-to-clb", "From TCF score to CLB level")],
    body=CALC_EN + """
<h2 id="scoring">How you are scored</h2>
<p>The TCF is a <strong>placement test, not an exam you can fail</strong>. There is no minimum score per section and
no pass mark: you get a score for each test, and the organization that receives your application decides whether
that score is enough.</p>
""" + table("TCF score bands and the matching CEFR levels. Source: official TCF documentation, France Éducation international.",
            ["CEFR level", "Listening and reading /699", "Speaking and writing /20"],
            [("Below A1", "0–99", "—"), ("A1", "100–199", "1"), ("A2", "200–299", "2–5"), ("B1", "300–399", "6–9"),
             ("B2", "400–499", "10–13"), ("C1", "500–599", "14–17"), ("C2", "600–699", "18–20")], wide=False) + """
<p>Your listening and reading score is not your number of correct answers: it is calculated by a model that weights
the difficulty of the questions you were given. Two candidates with the same number of correct answers can get
different scores.</p>

<h2 id="tcf-to-clb">From TCF score to CLB level</h2>
<p>For your Canadian application, the only thing that counts is the CLB level — <em>Niveaux de compétence linguistique
canadiens</em> (NCLC) in French — that each of your four scores falls into. Here is the official conversion.</p>
""" + table("TCF Canada → CLB. Listening and reading out of 699, speaking and writing out of 20. Source: IRCC equivalency tables, cross-checked on two official pages on 27 July 2026.",
            ["CLB", "Listening", "Reading", "Speaking", "Writing"],
            [("10+", "549–699", "549–699", "16–20", "16–20"), ("9", "523–548", "524–548", "14–15", "14–15"),
             ("8", "503–522", "499–523", "12–13", "12–13"), ("<strong>7</strong>", "<strong>458–502</strong>", "<strong>453–498</strong>", "<strong>10–11</strong>", "<strong>10–11</strong>"),
             ("6", "398–457", "406–452", "7–9", "7–9"), ("5", "369–397", "375–405", "6", "6"),
             ("4", "331–368", "342–374", "4–5", "4–5")], wide=False) + """
<p><strong>“I have B2, so I have CLB 7” is wrong.</strong> B2 starts at 400 in listening; CLB 7 starts at 458. Between
the two there are 58 points and a whole CLB level. It is the most expensive misunderstanding of the TCF Canada — it has
its own page: <a href="/en/tcf-canada-clb-7/">TCF Canada CLB 7: the exact scores to aim for</a>, test by test.</p>

<p><strong>Your weakest test decides.</strong> IRCC looks at your full profile, and CLB 9 in reading doesn’t make up for
CLB 6 in listening. Your preparation strategy follows directly from this.</p>
""",
    cta_h2="Know where you stand before paying $440",
    cta_p="""Timed mock exams in the exact TCF Canada format, an automatic CLB conversion for each test, and AI feedback on
writing and speaking against the official criteria — in the “TCF DELF TEF: Tests 2026” app.""",
    faq=[("What score do I need for CLB 7 in the TCF Canada?", "458 in listening, 453 in reading, and 10 out of 20 in both speaking and writing. CLB 7 in all four skills is the reference threshold of the Federal Skilled Worker Program. One point lower and you drop to CLB 6.")],
    also=[("/en/tcf-canada-clb-7/", "TCF Canada CLB 7: the exact scores", "458 in listening, 453 in reading — and why B2 isn’t always enough."),
          ("/en/tcf-canada/format/", "TCF Canada format", "The four tests, how long they take, and the format traps."),
          ("/en/tcf-canada-practice-test/", "Free TCF Canada practice test", "Check your level in the real format before you book.")],
    sources="""<strong>Rules change.</strong> This page is up to date as of 7 August 2026 and is not immigration advice:
thresholds, conversion tables and invitation rounds change regularly. Always check your situation on
<a href="https://www.canada.ca/" rel="noopener">canada.ca</a> and the exam format on
<a href="https://www.france-education-international.fr/" rel="noopener">france-education-international.fr</a> before you
register or apply.""",
))


# ===========================================================================
# TCF CANADA — writing tasks (from /blog/sujets-expression-ecrite-tcf-canada/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/sujets-expression-ecrite-tcf-canada/", lang="en", variant="en-CA", slug="tcf-canada-writing-tasks",
    crumbs=[HOME, TCF], crumb="Writing tasks",
    title="TCF Canada writing tasks 1, 2 and 3: topics, word limits",
    desc="TCF Canada writing: three tasks in 60 minutes, from 60–120 to 120–180 words. One sample topic per task, what the examiner expects, how to split your time.",
    h1="TCF Canada writing: the three tasks, with sample topics",
    intro="""<strong>Three tasks in 60 minutes</strong>, each longer than the last: a message of <strong>60–120
words</strong>, an article or story of <strong>120–150</strong>, then a comparison of two points of view with a
reasoned opinion of <strong>120–180</strong>. The third is the one that decides your score — and the one candidates
rush, because they haven’t managed their time.""",
    facts=["<strong>3 tasks · 60 minutes in total</strong>, scored out of <strong>20</strong>.",
           "<strong>Task 1</strong>: message · <strong>60–120 words</strong>.",
           "<strong>Task 2</strong>: article or story · <strong>120–150 words</strong>.",
           "<strong>Task 3</strong>: comparison of two points of view + reasoned opinion · <strong>120–180 words</strong>.",
           "⚠️ The word ranges are not guidelines: writing less costs you task-completion points.",
           "<strong>CLB 7</strong> requires <strong>10/20</strong> — and task 3 often decides whether you reach it."],
    toc=[("format", "The three tasks"), ("topics", "One sample topic per task"), ("timing", "Splitting the 60 minutes"),
         ("criteria", "What is assessed"), ("mistakes", "The most costly mistakes")],
    body="""
<h2 id="format">The three tasks</h2>
""" + table("TCF Canada writing test. Source: France Éducation international, structure checked in July 2026.",
            ["Task", "Type of text", "Length"],
            [("<strong>1</strong>", "Message", "<strong>60 to 120 words</strong>"),
             ("<strong>2</strong>", "Article, letter or story", "<strong>120 to 150 words</strong>"),
             ("<strong>3</strong>", "Comparison of two points of view, with a reasoned opinion", "<strong>120 to 180 words</strong>"),
             ("<strong>Total</strong>", "", "<strong>60 minutes</strong>")], wide=False) + """
<p>The three tasks get harder: the first is everyday communication, the second structured narration, the third
argumentation. And since the points are spread across all three, <strong>rushing task 3 mechanically caps your
score</strong>.</p>

<div class="note">
<p><strong>These word ranges are specific to the TCF Canada.</strong> Don’t practise on TCF Tout Public topics without
adjusting: the required lengths are different there. A text sized for another format is penalized on task completion,
whatever the quality of the language.</p>
</div>

<h2 id="topics">One sample topic per task</h2>
<p>The instructions are in French, as on exam day; what the examiner looks for is explained underneath.</p>
""" + sujet("en", "Task 1 — Message", "60 to 120 words · register adapted to the recipient",
            "Vous avez acheté un produit en ligne mais il est arrivé abîmé. Écrivez un email au service client "
            "pour expliquer le problème, décrire le défaut et demander un échange ou un remboursement.",
            "<strong>Three actions are required: explain, describe, request.</strong> The examiner checks that all "
            "three are there — that is the task-completion criterion, and you can lose it without a single language "
            "mistake. Add the conventions of the genre: subject line, greeting and sign-off. The register "
            "expected here is <em>formal</em>: « je vous écris », not « je vous écris pour vous dire que ».") + \
         sujet("en", "Task 2 — Article, letter or story", "120 to 150 words · structured narration",
            "Le maire de votre ville souhaite recueillir l'avis des habitants sur les transports en commun. "
            "Écrivez une lettre au maire pour donner votre avis : ce qui fonctionne bien, ce qui doit être "
            "amélioré, et vos propositions.",
            "Again, <strong>three explicit parts</strong>: the positive, the negative, the proposals. A three-paragraph "
            "plan follows the instructions and saves you from thinking about structure. The classic mistake is 100 "
            "words of criticism and 10 of proposals — the imbalance shows, and it is penalized. Formal register, "
            "institutional recipient.") + \
         sujet("en", "Task 3 — Comparison and reasoned opinion", "120 to 180 words · the test within the test",
            "Le gouvernement propose de rendre le vote obligatoire en France pour lutter contre l'abstention. "
            "Écrivez un essai argumentatif pour exprimer votre position sur cette proposition. Présentez des "
            "arguments pour et contre, puis donnez votre avis personnel en le justifiant.",
            "<strong>The structure is set by the instructions: for, against, then your position.</strong> Skipping "
            "the “against” part is the most frequent and most costly mistake — it is precisely the B2 skill being "
            "assessed. In 180 words at most, allow about 50 words for the opposing argument, 50 for yours and 40 to "
            "conclude. Connectors do the rest: « certes… toutefois », « d'une part… d'autre part ».") + """

<h2 id="timing">Splitting the 60 minutes</h2>
<p>This is where it all happens. Task 3 is the longest and the most demanding, and it comes last: without a split
decided in advance, you write it in a rush.</p>
""" + table("A split that protects task 3.", ["Time", "Task", "What you do"],
            [("<strong>0 – 12 min</strong>", "Task 1", "Write and reread. Don’t go over: it is the least rewarding task."),
             ("<strong>12 – 32 min</strong>", "Task 2", "A three-paragraph plan, then write."),
             ("<strong>32 – 55 min</strong>", "Task 3", "5 minutes of planning, 18 minutes of writing."),
             ("<strong>55 – 60 min</strong>", "All three", "Count your words, check the greeting and sign-off.")],
            wide=False) + """
<p><strong>The task 1 trap.</strong> It is easy, so you polish it — and spend twenty minutes on it. That is time taken
from task 3, which is worth more. A correct message in twelve minutes is plenty.</p>

<h2 id="criteria">What is assessed</h2>
<ul>
<li><strong>Task completion.</strong> The first criterion, and the most mechanical: are all the required actions
covered? Is the genre respected?</li>
<li><strong>Length.</strong> The word ranges are <strong>floors and ceilings</strong>. Below the minimum, the task is not
completed; far above the maximum, your ability to be concise is called into question.</li>
<li><strong>Coherence and cohesion.</strong> A clear plan, explicit connectors. At this level, it is the most visible
marker.</li>
<li><strong>Vocabulary and grammar.</strong> Assessed, but they make less difference than the first three: a correct text
that misses the instructions loses more than a well-built text with a few mistakes.</li>
<li><strong>Register.</strong> A message to a friend and a letter to a mayor aren’t written the same way. Slipping into
casual language in an institutional letter is immediately visible.</li>
</ul>

<h2 id="mistakes">The most costly mistakes</h2>
<ol>
<li><strong>Not counting your words.</strong> An estimate by eye is almost always optimistic. Actually count, at least
on task 3.</li>
<li><strong>Leaving out the opposing view in task 3.</strong> It is the skill being assessed: giving your opinion
without presenting the other side means not answering the question.</li>
<li><strong>Ignoring the conventions of the genre.</strong> A letter with no greeting or sign-off loses points
before the language is even assessed.</li>
<li><strong>Covering two of the three required actions.</strong> Reread the instructions at the end: each action verb in
them is a box to tick.</li>
<li><strong>Spending too long on task 1.</strong> It is short and easy; it doesn’t deserve a third of the test.</li>
</ol>

<div class="note">
<p><strong>Why this test is hard to prepare for on your own.</strong> You can’t judge whether your argument is really
balanced, or whether your register has slipped — those flaws are invisible from the inside. And knowing whether you
write at 9 or 11 out of 20 means knowing whether you have CLB 6 or CLB 7: a correction against the official criteria is
the only way to measure it.</p>
</div>
""",
    cta_h2="Find out whether your task 3 is worth 9 or 11 out of 20",
    cta_p="""Hundreds of writing topics in the exact TCF Canada format, with the official word ranges for each task, a real
timer and AI feedback against the official criteria — task completion, coherence, vocabulary, grammar. In the
“TCF DELF TEF: Tests 2026” app.""",
    faq=[("How many words do you write in the TCF Canada writing test?", "Three tasks of increasing length: 60 to 120 words for the message, 120 to 150 for the article or story, 120 to 180 for the comparison of two points of view with a reasoned opinion. These ranges are floors and ceilings, not guidelines."),
         ("How long is the writing test?", "60 minutes for the three tasks. A split that works: 12 minutes for task 1, 20 for task 2, 23 for task 3 and 5 minutes of final checking. The trap is polishing task 1, which is easy, at the expense of task 3, which is worth more."),
         ("Which task matters most?", "Task 3, the comparison of two points of view with a reasoned opinion. It calls on the B2 skill and makes the difference between 10 and 14 out of 20 — so between CLB 7 and CLB 9. Skipping the opposing point of view is the most costly mistake in the test."),
         ("What happens if I write less than the minimum?", "You lose points on task completion, regardless of the quality of your language. It is a mechanical criterion the examiner applies before even assessing vocabulary and grammar. Actually count your words rather than estimating them."),
         ("Can I practise with TCF Tout Public topics?", "Carefully: the required lengths are not the same. A text sized for another format is penalized on task completion. If you use such topics, hold yourself to the TCF Canada ranges — 60–120, 120–150 and 120–180 words."),
         ("What writing score do I need for CLB 7?", "10 out of 20. Writing is scored out of 20, unlike listening and reading, which are scored out of 699. CLB 7 is 10–11 out of 20, CLB 8 is 12–13. A single point can therefore change your level.")],
    also=[("/en/tcf-canada-speaking-topics/", "TCF Canada speaking: the 3 tasks", "The other productive test, in only 12 minutes."),
          ("/en/tcf-canada-reading-practice/", "TCF Canada reading practice", "39 multiple-choice questions in 60 minutes, with answers explained."),
          ("/en/tcf-canada/", "TCF Canada exam: format, scores, CLB", "The complete guide to the four tests.")],
    sources="""<strong>Formats change.</strong> This page is up to date as of 7 August 2026. The topics shown are original
content from our app, designed in the official format — there are no official past TCF papers freely available. Check
the current structure on <a href="https://www.france-education-international.fr/test/tcf-canada" rel="noopener">france-education-international.fr</a>
before your session.""",
))

CTA_H2 = "Know where you stand before paying $440"
CTA_P = """Timed mock exams in the exact TCF Canada format, an automatic CLB conversion for each test, and AI feedback on
writing and speaking against the official criteria — in the “TCF DELF TEF: Tests 2026” app."""
SOURCES = """<strong>Rules change.</strong> This page is up to date as of 7 August 2026 and is not immigration advice:
thresholds, conversion tables and invitation rounds change regularly. Always check your situation on
<a href="https://www.canada.ca/" rel="noopener">canada.ca</a> and the exam format on
<a href="https://www.france-education-international.fr/test/tcf-canada" rel="noopener">france-education-international.fr</a>
before you register or apply."""

# ===========================================================================
# TCF CANADA — the hub (from /tcf-canada/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/tcf-canada/", lang="en", variant="en-CA", section="en", slug="tcf-canada",
    crumbs=[HOME], crumb="TCF Canada", inline_cta=False,
    title="TCF Canada exam 2026: format, CLB scores, preparation",
    desc="What the TCF Canada test is: 4 tests in 2 h 47 min, scores converted to CLB, the Express Entry thresholds, fees and the waiting period before a retake.",
    h1="TCF Canada: how to get the score you need to immigrate to Canada",
    intro="""The TCF Canada is one of the <strong>only two French tests</strong> recognized by IRCC for permanent residence,
Express Entry and citizenship. It lasts <strong>2 hours 47 minutes</strong>, has <strong>four compulsory tests</strong>
taken on the same day, and your results are converted into <strong>CLB levels</strong> (NCLC in French) — each level
you gain can be worth dozens of CRS points.""",
    facts=["<strong>4 compulsory tests</strong>, in a single 2 h 47 min session: listening, reading, writing, speaking.",
           "Listening and reading scored on the <strong>100–699 scale</strong>, speaking and writing out of <strong>20</strong>, "
           "then converted to <a href=\"/en/tcf-canada-clb-7/\">CLB levels</a> for your IRCC application.",
           "<strong>CLB 7</strong> = 458 in listening, 453 in reading, 10/20 in speaking and in writing. It is the reference "
           "threshold of the Federal Skilled Worker Program.",
           "Results certificate valid for <strong>2 years</strong> — and IRCC’s rule is stricter than it looks (see below).",
           "⚠️ <strong>No partial retakes</strong>: you retake all four tests or nothing.",
           "For Canadian <strong>citizenship</strong>, only listening and speaking are required."],
    toc=[("what-is", "What is the TCF Canada?"), ("steps", "Your path in 5 steps"),
         ("modules", "The guide, module by module")],
    body="""
<div class="stats">
<div class="stat"><b>2 h 47</b><span>4 tests, the same day</span><em>listening 35 · reading 60 · writing 60 · speaking 12 min</em></div>
<div class="stat"><b>699</b><span>the multiple-choice scale</span><em>speaking and writing scored out of 20</em></div>
<div class="stat"><b>458</b><span>in listening</span><em>for CLB 7 (453 in reading)</em></div>
<div class="stat"><b>2 years</b><span>of validity</span><em>checked twice by IRCC</em></div>
</div>

<h2 id="what-is">What is the TCF Canada?</h2>
<p>The <strong>TCF Canada</strong> is a French test designed by France Éducation international and recognized by
Immigration, Refugees and Citizenship Canada (IRCC) as proof of your French level for <strong>economic
immigration</strong> — Express Entry, the skilled worker programs — or for <strong>citizenship</strong>. You take it in
one session, at an approved test centre, and it has <strong>four compulsory tests</strong>: listening, reading, writing
and speaking. Listening and reading are scored out of 699, speaking and writing out of 20, and each score is then
<strong>converted into a CLB level</strong>, the scale IRCC uses to award points.</p>

<p>It is neither a diploma nor an exam you “pass”: everyone leaves with a level, from A1 to C2, and a results
certificate valid for <strong>two years</strong>. Along with the TEF Canada, it is one of the only two tests IRCC
accepts; the TCF tout public and the TCF Québec, which look similar, are not accepted for Express Entry.</p>

<h3>Who it’s for</h3>
<ul>
<li>Candidates for <strong>Express Entry</strong> and the federal programs, who must reach a set CLB level — CLB 7 is
the most common threshold.</li>
<li>Applicants for <strong>citizenship</strong>, for whom only the two oral tests count: listening and speaking.</li>
<li>Candidates for <strong>Quebec</strong>’s programs, which have also accepted it since 2022 — but the modular TCF
Québec is often cheaper there.</li>
</ul>

<h2 id="steps">Your path in 5 steps</h2>
<ol class="steps">
<li><b>Check which test you need</b><span>Express Entry, citizenship: the TCF <em>Canada</em> or the TEF Canada — never the TCF tout public or the TCF Québec. <a href="/en/tcf-vs-tef-canada/">TCF or TEF Canada?</a></span></li>
<li><b>Set your target score</b><span>IRCC reads the CLB level, not the CEFR letter: 458 in listening and 453 in reading for CLB 7, 523 and 524 for CLB 9. <a href="/en/tcf-canada-clb-7/">The full table.</a></span></li>
<li><b>Test yourself before you pay</b><span>A <a href="/en/tcf-canada-practice-test/">mock exam scored out of 699</a> and converted to CLB tells you whether next month’s session is the right one; work on the <a href="/en/tcf-canada/format/#traps">format traps</a> beforehand.</span></li>
<li><b>Book the centre and the date</b><span>In France, one session a month per centre, €195 to €285; in Canada, $390 to $440, and seats gone within minutes. <a href="/en/tcf-canada/fees-registration/#where">The centres</a> and their contacts.</span></li>
<li><b>Test day, then your application</b><span>Passport and test-day notice; results certificate within 2 to 4 weeks, valid for two years — and IRCC counts those two years twice.</span></li>
</ol>

<h2 id="modules">The guide, module by module</h2>
<div class="grid c2 modules">
<div class="card card-link"><span class="tag">The tests</span><h3><a href="/en/tcf-canada/format/">The format, test by test</a></h3><p>39 + 39 questions, 3 writing tasks, 3 speaking tasks, and the format traps that cost points.</p></div>
<div class="card card-link"><span class="tag">Scoring</span><h3><a href="/en/tcf-canada/score-clb/">From the score out of 699 to CLB</a></h3><p>The score bands, IRCC’s conversion table, and the B2 that isn’t always worth CLB 7.</p></div>
<div class="card card-link"><span class="tag">Preparing</span><h3><a href="/en/tcf-canada/preparation/">Method and resources</a></h3><p>Why French is worth so much in 2026, and how to work on each test.</p></div>
<div class="card card-link"><span class="tag">Fees and registration</span><h3><a href="/en/tcf-canada/fees-registration/">Fees, centres, validity, retakes</a></h3><p>€195 to €285 in France, $390 to $440 in Canada, fees in other countries, the double two-year rule.</p></div>
<div class="card card-link"><span class="tag">Practice</span><h3><a href="/en/tcf-canada-listening-practice/">Exercises with answers, test by test</a></h3><p>Listening, reading, writing, speaking: exam-format items, explained.</p></div>
<div class="card card-link"><span class="tag">Mock exam</span><h3><a href="/en/tcf-canada-practice-test/">The full test, timed and scored</a></h3><p>In the app: the four tests in the official format, scored out of 699 and converted to CLB.</p></div>
</div>
<p class="serie-label">Where to take it, city by city</p>
<div class="chips">
<a class="chip" href="/en/tcf-canada-montreal/">TCF in Montreal</a>
<a class="chip" href="/en/tcf-canada-toronto/">TCF in Toronto</a>
<a class="chip" href="/en/tcf-canada-quebec-city/">TCF in Quebec City</a>
<a class="chip" href="/en/tcf-canada-ottawa/">TCF in Ottawa</a>
<a class="chip" href="/en/tcf-canada-vancouver/">TCF in Vancouver</a>
<a class="chip" href="/en/tcf-canada-test-centres/">All of Canada →</a>
</div>
<p class="serie-label">TCF Canada outside Canada, country by country</p>
<div class="chips">
<a class="chip" href="/en/tcf-canada-usa/">United States</a>
<a class="chip" href="/en/tcf-canada-uk/">United Kingdom</a>
<a class="chip" href="/en/tcf-canada-india/">India</a>
<a class="chip" href="/en/">All locations →</a>
</div>
""",
    cta_h2=CTA_H2, cta_p=CTA_P,
    faq=[("What is the TCF Canada test?", "A French test by France Éducation international, recognized by Immigration, Refugees and Citizenship Canada for economic immigration and citizenship. Four compulsory tests in one session — listening, reading, writing, speaking — a level from A1 to C2 for each, converted to CLB, and a results certificate valid for two years."),
         ("How is it different from the TCF tout public and the TCF Québec?", "The TCF tout public is for studies and personal matters, the TCF Québec for the programs of Quebec’s immigration ministry; IRCC accepts neither for Express Entry. Only the TCF Canada and the TEF Canada are accepted. The TCF Canada, on the other hand, has also been recognized by Quebec since 2022."),
         ("Is the TCF Canada a pass-or-fail exam?", "No: there is no pass mark. Each test gives you a level, from A1 to C2, converted to CLB; your immigration program sets the level you need — most often CLB 7. If your score falls short, you fix it by retaking all four tests after 20 to 30 days.")],
    also=[("/en/tcf-canada-clb-7/", "TCF Canada CLB 7: the exact scores", "458 in listening, 453 in reading — and why a “B2” isn’t always worth CLB 7."),
          ("/en/tcf-vs-tef-canada/", "TCF or TEF Canada: which one to choose?", "The two CLB conversion tables, the format and fee comparison, and the “old score” column trap."),
          ("/en/tcf-canada-practice-test/", "Free TCF Canada practice test", "The only two free resources officially recognized, their limits, and how to turn them into a real simulation.")],
    sources=SOURCES,
))


# ===========================================================================
# TCF CANADA — format (from /tcf-canada/format/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/tcf-canada/format/", lang="en", variant="en-CA", section="en/tcf-canada", slug="format",
    crumbs=[HOME, TCF], crumb="Format", inline_cta=False,
    title="TCF Canada exam format and pattern: 4 tests in 2 h 47 min",
    desc="The TCF Canada exam structure: listening, reading, writing and speaking, their exact timing (2 h 47 min in all), questions, tasks and the format traps.",
    h1="The TCF Canada format, test by test",
    intro="""The TCF Canada is <strong>four compulsory tests</strong> taken on the same day, in <strong>2 hours 47
minutes</strong>: 39 listening questions in 35 minutes, 39 reading questions in 60 minutes, three writing tasks in 60
minutes and three speaking tasks in 12 minutes. Here is the official format, test by test, and the format traps that
cost you points before your level of French even comes into play.""",
    facts=["<strong>4 tests in 2 h 47 min</strong>, on the same day, at an approved test centre.",
           "Listening: <strong>39 multiple-choice questions, audio played once</strong>, no going back.",
           "Reading: 39 multiple-choice questions in 60 minutes, free navigation.",
           "Writing: <strong>3 tasks</strong> of 60 to 180 words; speaking: 3 tasks in 12 minutes, including 2 minutes of preparation.",
           "For citizenship, only the two oral tests are required: listening and speaking."],
    toc=[("format", "The official format, test by test"), ("traps", "The format traps that cost points")],
    body="""
<h2 id="format">The official format, test by test</h2>
<p>The four tests <strong>can’t be split</strong>: you take them in the same session, and you can’t pick just some of
them. That is the major difference with the TCF Québec, which is modular.</p>
""" + table("Official TCF Canada format. Source: France Éducation international, structure checked in July 2026.",
            ["Test", "Questions / tasks", "Time", "What’s specific"],
            [("Listening", "39 multiple-choice questions, 4 options", "35 min", "<strong>Audio played only once</strong>, no going back"),
             ("Reading", "39 multiple-choice questions, 4 options", "60 min", "Free navigation between questions"),
             ("Writing", "3 tasks", "60 min", "60–120, then 120–150, then 120–180 words"),
             ("Speaking", "3 tasks", "12 min", "Face to face, including 2 min of preparation for task 2"),
             ("<strong>Total</strong>", "", "<strong>2 h 47 min</strong>", "")], wide=False) + """

<p>The multiple-choice questions get <strong>progressively harder, from A1 to C2</strong>: the first questions are easy,
the last ones are advanced level. So you aren’t expected to get everything right — and above all, don’t dig in on a
hard question at the end of a test: the clock is the real opponent.</p>

<p>Each of the three writing tasks has its own genre: a <strong>message</strong> (60–120 words), an <strong>article or
story</strong> (120–150 words), then a <strong>comparison of two points of view with a reasoned opinion</strong>
(120–180 words). The third is the one that separates candidates most — it is where the jump from 10 to 14 out of 20
is decided. In speaking, the three tasks follow one another: a guided interview, an interaction with preparation time,
and expressing a point of view.</p>

<h2 id="traps">The format traps that cost points</h2>
<p>Candidates who narrowly miss their target are almost always the ones who discover the format on exam day. Four
traps come up again and again.</p>

<ul>
<li><strong>Audio played once, with no going back.</strong> In listening, the audio isn’t replayed and you can’t go
back. If you lose the thread on a question, it is lost — what matters is moving on to the next one immediately, not
reconstructing what you missed.</li>
<li><strong>The word count in the writing tasks.</strong> The ranges (60–120, 120–150, 120–180) are not guidelines.
Writing 90 words for a task that requires at least 120 costs you points on task completion, whatever the quality of
your language.</li>
<li><strong>The rising difficulty.</strong> The last multiple-choice questions are C1–C2 level. Hanging on to them at
the expense of time is a bad bet: they carry their weight in the scoring model, but they aren’t worth three B1-level
questions left unanswered.</li>
<li><strong>The 12 minutes of speaking.</strong> Three tasks in twelve minutes is very short. Candidates who haven’t
practised use up their time on the first task, the easiest, and rush the third, the one worth the most.</li>
</ul>

<div class="note">
<p><strong>The number of items on screen may surprise you.</strong> In the computer-based test, France Éducation
international adds items that don’t count toward your score: they are used for its validity analyses. Seeing a test
run longer than the announced number of questions is normal and says nothing about your result.</p>
</div>
""",
    cta_h2=CTA_H2, cta_p=CTA_P,
    faq=[("How long is the TCF Canada exam?", "2 hours 47 minutes in total, in a single session: 35 minutes of listening, 60 minutes of reading, 60 minutes of writing and 12 minutes of speaking. All four tests are compulsory and taken on the same day."),
         ("Do I need to take all four tests for Canadian citizenship?", "No. For a citizenship application, only listening and speaking are required. All four tests are compulsory only for economic immigration, Express Entry included.")],
    also=[("/en/tcf-canada-listening-practice/", "TCF Canada listening practice", "39 questions in 35 minutes, audio played once: four exercises with answers, from B1 to B2."),
          ("/en/tcf-canada-writing-tasks/", "TCF Canada writing: the 3 tasks", "One sample topic per task, with the official word ranges and how to split the 60 minutes."),
          ("/en/tcf-canada-speaking-topics/", "TCF Canada speaking: the 3 tasks", "The other productive test, in only 12 minutes.")],
    sources=SOURCES,
))


# ===========================================================================
# TCF CANADA — preparation (from /tcf-canada/preparation/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/tcf-canada/preparation/", lang="en", variant="en-CA", section="en/tcf-canada", slug="preparation",
    crumbs=[HOME, TCF], crumb="Preparation", inline_cta=False,
    title="TCF Canada preparation: method and resources, test by test",
    desc="How to prepare for the TCF Canada, test by test: the format, exercises with answers, a mock exam — and why French counts for so much in Express Entry.",
    h1="Preparing for the TCF Canada: the method, test by test",
    intro="""Preparing for the TCF Canada means first <strong>knowing the format</strong> of each test — audio played
once, writing tasks with set word counts, a 12-minute speaking test — then <strong>testing yourself under exam
conditions</strong> before paying for a session. It is worth the effort: French has never counted for so much in federal
selection, and Express Entry’s French-language rounds invite candidates at much lower scores than the general rounds.
Here is why, and how.""",
    facts=["Express Entry’s <strong>French-language rounds</strong> invite candidates at clearly lower scores than the general rounds.",
           "Work on the format before the level: audio played once, no going back, set word ranges.",
           "A <strong>mock exam scored out of 699</strong> and converted to CLB (NCLC in French) tells you whether next "
           "month’s session is the right one.",
           "Each attempt is paid in full and means waiting 20 to 30 days.",
           "Exercises with answers, test by test, in our guides."],
    toc=[("why", "Why French is worth so much in 2026"), ("how", "How to prepare effectively")],
    body="""
<h2 id="why">Why French is worth so much in 2026</h2>
<p>The reason it pays to invest in your score fits in this table — it compares the CRS cut-off of the rounds reserved
for French speakers with that of the general category rounds, over the same period.</p>
""" + table("Express Entry invitation rounds in 2026: French-language category versus Canadian Experience Class. Source: IRCC, data consulted on 27 July 2026.",
            ["Date", "French-language round — CRS", "Canadian Experience Class — CRS"],
            [("22 Jul 2026", "<strong>399</strong> (5,000 invitations)", "—"),
             ("21 Jul 2026", "—", "516"),
             ("9 Jul 2026", "<strong>420</strong> (5,000)", "517"),
             ("28 May 2026", "<strong>409</strong> (4,500)", "518"),
             ("29 Apr 2026", "<strong>400</strong> (4,000)", "514")], wide=False) + """

<p>The gap is <strong>about 100 CRS points</strong>. The same profile gets invited through the French-language route at
a score that would stand no chance in the general category. That is what makes the TCF Canada, for a French speaker or
learner, the most profitable investment in the whole application.</p>

<h2 id="how">How to prepare effectively</h2>
<p>Is the TCF Canada hard? Yes, and not only because of the language: it is also a test of <strong>format</strong>. Questions in
quick succession in listening and reading, strict instructions in writing and speaking, a tight clock. The method that
works has three stages.</p>

<ol>
<li><strong>A full mock exam right at the start</strong>, before any revision, to find your current CLB level in each
test. Without that starting point, you are working blind — and usually on the wrong skill.</li>
<li><strong>Targeted practice on your weakest test.</strong> It is the one that caps your application. Going from CLB 7
to 8 on a test that is already strong changes nothing if another stays at 6.</li>
<li><strong>Regular timed mock exams</strong> until the format no longer surprises you. The goal isn’t to learn
answers; it is to make the sequence automatic and free up your attention.</li>
</ol>

<p>In writing and speaking, the blind spot is structural: you can’t assess yourself against criteria you don’t know. A
candidate rarely knows whether they write at 9 or at 10 out of 20 — yet that is exactly the line between CLB 6 and
CLB 7. That is what AI feedback against the official criteria solves.</p>
""",
    cta_h2=CTA_H2, cta_p=CTA_P,
    faq=[("TCF Canada or TEF Canada: which should I choose?", "Both are accepted by IRCC and test the same skills. The TCF is often seen as more direct in listening and reading; the TEF has different task formats in writing and speaking. No general rule decides between the two: take a mock exam of each and choose the one where your score is higher — it is the only criterion that counts. Our detailed comparison: <a href=\"/en/tcf-vs-tef-canada/\">TCF or TEF Canada</a>.")],
    also=[("/en/tcf-canada/format/", "TCF Canada format", "The four tests, how long they take, and the format traps."),
          ("/en/tcf-canada/score-clb/", "TCF Canada score and CLB", "The calculator, the score bands and the CLB table."),
          ("/en/tcf-canada-practice-test/", "Free TCF Canada practice test", "Check your level in the real format before you book.")],
    sources=SOURCES,
))


# ===========================================================================
# TCF CANADA — fees and registration (from /tcf-canada/prix-inscription/)
# + “TCF Canada fees by country”: figures from the French country pages and guides, with their check dates
#   (centres/tcf-canada, tcf-etats-unis, tcf-royaume-uni, tcf-espagne, tcf-mexique, tcf-colombie, tcf-chili,
#    tcf-perou, tcf-equateur; blog/ou-passer-le-tcf-canada-en-france, tcf-canada-maroc, tcf-canada-tunisie).
# ===========================================================================
PAGES.append(dict(
    fr_path="/tcf-canada/prix-inscription/", lang="en", variant="en-CA", section="en/tcf-canada", slug="fees-registration",
    crumbs=[HOME, TCF], crumb="Fees and registration", inline_cta=False,
    title="TCF Canada exam fees 2026: cost by country, registration",
    desc="TCF Canada fees: $390 to $440 in Canada, €195 to €285 in France, and the cost in other countries. How to register, validity and retake rules.",
    h1="TCF Canada fees and registration: centres, validity, retakes",
    intro="""There is <strong>no national fee</strong> for the TCF Canada: each approved centre sets its own —
<strong>€195 to €285 in France</strong>, <strong>$390 to $440 in Canada</strong> — and many large centres publish
nothing. The results certificate is valid for <strong>two years</strong>, checked twice by IRCC; there are no partial
retakes, and 20 to 30 days must pass between two attempts. Here are the fees we found, in Canada, in France and in
other countries, the centres, and the rules to know before you pay.""",
    facts=["<strong>No national fee</strong>: €195 to €285 in France, $390 to $440 in Canada at the centres we checked.",
           "Results certificate valid for <strong>2 years</strong> — and IRCC requires results less than two years old "
           "when you create your profile and when you apply.",
           "⚠️ <strong>No partial retakes</strong>: you retake all four tests, after 20 to 30 days.",
           "Six centres we checked are listed below; the full directory lists 251 in France and "
           "<a href=\"/en/tcf-canada-test-centres/\">47 in Canada</a>, with addresses and phone numbers.",
           "Fees in other countries — the United States, the United Kingdom, Spain, Latin America, Morocco, Tunisia — "
           "in the <a href=\"#by-country\">table by country</a>.",
           "The TCF Canada is not eligible for the CPF (France’s personal training account)."],
    toc=[("fees", "Fees, validity, retakes"), ("by-country", "TCF Canada fees by country"),
         ("where", "Where to take the TCF Canada?")],
    body="""
<h2 id="fees">Fees, validity, retakes</h2>
<p><strong>The fee.</strong> There is no national fee: each approved centre sets its own, and many — including the
Alliance Française de Montréal — publish none. At the centres that posted a fee schedule in July 2026, a full test
cost about <strong>€220 to €245</strong> in Europe and <strong>$400 to $440 (CAD)</strong> in Canada. Be wary of the fees
quoted on comparison sites: they are rarely sourced and often mix up the TCF Canada and the TCF Québec, which don’t
cost the same.</p>

<p><strong>Validity.</strong> The results certificate is valid for <strong>two years from its date of issue</strong>.
IRCC’s rule is stricter than it looks: your results must be less than two years old <em>when you create your Express
Entry profile</em> <strong>and</strong> <em>when you submit your application for permanent residence</em>. A test taken
too early in the process can expire in between.</p>

<p><strong>Retakes.</strong> There are <strong>no partial retakes</strong>: you retake all four tests. The number of
attempts is unlimited. For sessions held since 1 September 2026, France Éducation international <strong>no longer
accepts re-marking requests</strong>; before that, re-marking covered only the writing and speaking tests — never the
multiple-choice questions — had to be requested within a month, and the new score replaced the old one, <strong>even
if it was lower</strong>.</p>

<div class="note">
<p><strong>The waiting period between two attempts can’t be pinned down to the week.</strong> You will see both “20 days” and
“30 days” quoted. Both figures come from France Éducation international itself: its test pages say 20 days, several of
its PDF information sheets say 30. Don’t plan a second attempt around a deadline without having your centre confirm
the waiting period.</p>
</div>

<h2 id="by-country">TCF Canada fees by country</h2>
<p>Outside Canada and France, the fee depends just as much on the centre. Here are the figures published in our
country guides, in the local currency, each with the date we checked it.</p>
""" + table("TCF Canada fee by country, in the local currency, as the centres posted it on the date shown. There is no national fee: confirm it with your centre before paying.",
            ["Country", "TCF Canada fee", "Details", "Checked on"],
            [("<a href=\"/en/tcf-canada-test-centres/\">Canada</a>", "<strong>$390 to $440</strong>", "$390 at the Alliance française in Vancouver, $400 in Edmonton, $440 at UQTR; no fee posted by the Alliance Française de Montréal", "17 Sept 2026"),
             ("<a href=\"/en/tcf-canada-usa/\">United States</a>", "<strong>US$330 to US$460</strong>", "From $330 in Detroit to $460 in San Francisco", "8 Oct 2026"),
             ("<a href=\"/en/tcf-canada-uk/\">United Kingdom</a>", "<strong>£260 to £325</strong>", "£260 at the Institut français in London, £325 at the Alliance française de Glasgow", "8 Oct 2026"),
             ("France", "<strong>€195 to €285</strong>", "From €195 at ACTE (Paris) to €285 at CLPS (Rennes and Brest)", "17 Sept 2026"),
             ("Spain", "<strong>€275 to €287</strong>", "€287 at the Instituts français and ILF (Seville), €281 at the Alliances françaises, €275 at CELF (Seville)", "8 Oct 2026"),
             ("Mexico", "<strong>4,800 to 6,500 pesos</strong> (MXN)", "Puebla 4,800, Guadalajara 4,950, IFAL in Mexico City 5,150 (6,500 for a date on request), UAEH in Pachuca 5,800", "8 Oct 2026"),
             ("Colombia", "<strong>From 1,050,000 pesos</strong> (COP)", "1,050,000 in Medellín and Pereira, up to 1,247,000 in Bogotá", "8 Oct 2026"),
             ("Chile", "<strong>299,000 pesos</strong> (CLP)", "The same fee at the Institut français du Chili (Santiago) and the Alliance française de Concepción", "8 Oct 2026"),
             ("Peru", "<strong>1,240 soles</strong> (PEN)", "Alliance française de Lima, the only centre; 992 soles at the member rate", "8 Oct 2026"),
             ("Ecuador", "<strong>US$200 to US$300</strong>", "US$200 in Cuenca, US$300 in Guayaquil", "8 Oct 2026"),
             ("Morocco", "<strong>2,900 dirhams</strong> (MAD)", "National fee of the Institut français du Maroc, checked in Casablanca and Rabat", "17 Sept 2026"),
             ("Tunisia", "<strong>880 dinars</strong> (TND)", "Institut français de Tunisie", "17 Sept 2026"),
             ("<a href=\"/en/tcf-canada-india/\">India</a>", "<strong>₹26,000</strong>", "New Delhi, Kolkata and Bhopal (GST included in New Delhi and Kolkata); Ahmedabad and Bangalore publish no fee", "8 Oct 2026"),
             ("<a href=\"/en/tcf-canada-dubai/\">United Arab Emirates</a>", "<strong>1,800 AED</strong>", "Alliance Française de Dubai and Alliance Française Abu Dhabi", "8 Oct 2026")], wide=True) + """

<h2 id="where">Where to take the TCF Canada?</h2>
<p>In France, at an approved centre that has chosen to run this version — not all of them do: as of 17 September
2026, ACTE (€195) and ACCORD (€220) in Paris, the Alliances françaises in Lyon (€220), Montpellier (€200) and
Aix-Marseille (€240), KLF, CLPS (€285)… with about one session a month. In Canada, at one of the 47 approved centres,
for $390 to $440, where seats go within minutes. Our guides on where to take the TCF Canada in France and
<a href="/en/tcf-canada-test-centres/">in Canada</a> check the centres one by one, with their fees, dates and
procedure. In North Africa, same method: Algeria (five branches of the Institut français, IFAL platform), Morocco
(sixteen centres, 2,900 dirhams) and Tunisia (880 dinars, results in five weeks).</p>

<p>Six centres we checked in our guides, among the 251 approved in France and the 47 in Canada — all six with
computer-based sessions: ACTE (Paris), the Alliance française in Lyon, the Alliance française de Montpellier, the
Alliance Française de Montréal, the Alliance française in Toronto (Spadina campus) and the Alliance française Canada
Pacific (Vancouver).</p>
<p class="more">Full directory, with addresses and phone numbers: <a href="/en/tcf-canada-test-centres/">the 47 TCF
centres in Canada</a> · <a href="/en/">all locations in English</a>. The directories for France, Morocco, Algeria and
Tunisia are in French.</p>
""",
    cta_h2=CTA_H2, cta_p=CTA_P,
    faq=[("How much does the TCF Canada exam cost?", "There is no national fee: each approved centre sets its own, and many don’t publish it. At the centres that posted a fee schedule in July 2026, a full test cost about 220 to 245 euros in Europe and 400 to 440 Canadian dollars in Canada. Ask your centre for its fee: the figures quoted on comparison sites are generally not sourced."),
         ("How long are my results valid?", "Two years from the date the results certificate is issued. IRCC’s rule is stricter than it looks: your results must be less than two years old when you create your Express Entry profile and when you submit your application for permanent residence."),
         ("Can I retake only the test I did badly on?", "No. There are no partial retakes in the TCF Canada: it is the full test, with all four sections. The number of attempts is unlimited. And for sessions held since 1 September 2026, re-marking requests are no longer accepted.")],
    also=[("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 47 approved centres, province by province."),
          ("/en/tcf-canada-usa/", "TCF Canada in the USA", "9 of the 18 approved US centres offer it, from US$330 to US$460."),
          ("/en/tcf-canada-uk/", "TCF Canada in the UK", "London (£260) and Glasgow (£325).")],
    sources=SOURCES + """ The table of fees by country brings together the figures from our country guides, each dated as
checked; fees change without notice, so check them on the centre’s website before paying.""",
))

# ===========================================================================
# TCF CANADA — listening practice (from /blog/exercices-comprehension-orale-tcf-canada/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/exercices-comprehension-orale-tcf-canada/", lang="en", variant="en-CA",
    slug="tcf-canada-listening-practice",
    crumbs=[HOME, TCF], crumb="Listening practice",
    title="TCF Canada listening practice: sample questions and tips",
    desc="TCF Canada listening: 39 questions in 35 minutes, each recording played once. 4 practice exercises from B1 to B2 with answers, timing and tips.",
    h1="TCF Canada listening practice: four exercises, with answers",
    intro="""<strong>39 multiple-choice questions in 35 minutes</strong> — about <strong>54 seconds per question</strong> —
and <strong>each recording is played once</strong>, with no going back. This is the test where candidates lose the most
points for reasons that have nothing to do with their French. Here are four practice exercises with answers, from B1 to
B2, and a method that keeps you from losing track.""",
    facts=["<strong>39 multiple-choice questions, 4 options each · 35 minutes</strong> — about <strong>54 seconds per question</strong>.",
           "⚠️ <strong>One listening only</strong>, no going back: a missed question is lost.",
           "Difficulty is <strong>progressive, A1 → C2</strong>: you aren’t expected to get everything right.",
           "Types of recordings: dialogue, talk, interview, announcement, message.",
           "The jump from B1 to B2 comes down to questions on <strong>attitude and intention</strong>, not on spotting information.",
           "<strong>CLB 7</strong> starts at <strong>458</strong> out of 699 in listening."],
    toc=[("format", "The test format"), ("exercises", "Four sample exercises, with answers"),
         ("b1-b2", "What really changes between B1 and B2"), ("tips", "Tips: how not to lose track"),
         ("mistakes", "The most costly mistakes")],
    body="""
<h2 id="format">The test format</h2>
""" + table("TCF Canada listening test. Source: France Éducation international, structure checked in July 2026.",
            ["Parameter", "Value"],
            [("Questions", "<strong>39 multiple-choice questions</strong>, 4 options each"),
             ("Duration", "<strong>35 minutes</strong>"),
             ("Average time per question", "<strong>≈ 54 seconds</strong>, audio included"),
             ("Times each recording is played", "<strong>Once only</strong>, no going back"),
             ("Difficulty", "progressive, from A1 to C2"),
             ("Scoring", """from 100 to 699 → <a href="/en/tcf-canada-clb-7/">CLB</a> (NCLC in French)""")],
            wide=False) + """
<p>Those 54 seconds are the number to keep in mind: they include listening to the recording, reading the four options
and choosing. In other words, there is <strong>no downtime</strong>, and a single long hesitation throws off everything
that follows.</p>

<p>The recordings follow one another without transition and change type: a thirty-second dialogue can be followed by a
two-minute talk, then an interview with several voices. It is this variety that wears you out, more than the difficulty
of the language itself.</p>

<h2 id="exercises">Four sample exercises, with answers</h2>

<p>The four exercises below follow the real progression of the test. The first two are B1, the next two B2 — the
level where CLB 7 is decided. The recordings, questions and options are in French, as on exam day; the answers are
explained underneath.</p>

<div class="warn">
<p><strong>Listen before you read.</strong> These four exercises are listening tests: the audio is there to be played
<strong>once</strong>, without a transcript, exactly as on exam day. An excerpt of the transcript is available under
each exercise, but opening it before you listen turns the test into a reading exercise — and gives you a result that
means nothing.</p>
</div>
""" + exo("en", 1, "B1", "Radio talk, 1 speaker",
          "« Bonjour à tous et bienvenue dans notre émission <em>Vie Quotidienne</em>. Aujourd'hui, nous "
          "allons parler du tri des déchets en France. Depuis plusieurs années, le tri sélectif est "
          "obligatoire dans toutes les communes françaises. Mais savez-vous vraiment dans quelle poubelle "
          "mettre vos déchets ? La poubelle jaune est destinée aux emballages : bouteilles en plastique, "
          "cartons, conserves métalliques. La poubelle verte ou blanche reçoit le verre : bouteilles, pots, "
          "bocaux. Attention, la vaisselle cassée ne va pas dans le bac à verre. La poubelle grise ou noire "
          "est pour les ordures ménagères, c'est-à-dire tout le reste. »",
          "Où doit-on mettre les bouteilles en plastique ?",
          ["Dans la poubelle verte", "Dans la poubelle blanche", "Dans la poubelle jaune", "Dans la poubelle grise"],
          """C — <span lang="fr">Dans la poubelle jaune</span> (in the yellow bin)""",
          "the yellow bin is for packaging, including plastic bottles. This is an <strong>information-spotting</strong> "
          "question: the answer is said word for word.",
          audio="tcf_co_019.m4a", duree="1 min 07 s", ecoutes=1) + exo(
    "en", 2, "B1", "Dialogue, 3 speakers",
    "« <strong>Karim :</strong> Alors Ahmed, tu en es où avec ta demande de naturalisation ?<br>"
    "<strong>Ahmed :</strong> J'ai déposé mon dossier il y a six mois à la préfecture. On m'a dit que "
    "le délai moyen était de dix-huit mois.<br>"
    "<strong>Sophie :</strong> C'est long !<br>"
    "<strong>Ahmed :</strong> Et tu as déjà passé l'entretien ?<br>"
    "<strong>Karim :</strong> Pas encore, j'attends la convocation. Mais j'ai déjà passé le test de "
    "français, le TCF. »",
    "Quel est le délai moyen pour une demande de naturalisation ?",
    ["Six mois", "Dix-huit mois", "Douze mois", "Vingt-quatre mois"],
    """B — <span lang="fr">Dix-huit mois</span> (eighteen months)""",
    "the trap is « six mois », which is mentioned just before but refers to the time elapsed <em>since the "
    "application was submitted</em>, not the average processing time. In a dialogue, <strong>two close numbers "
    "collide</strong>: it is the most common distraction mechanism.",
    audio="tcf_co_020.m4a", duree="54 s", ecoutes=1) + exo(
    "en", 3, "B2", "Interview, several speakers",
    "« <strong>Pierre Martineau :</strong> L'abstention n'a cessé d'augmenter en France depuis les "
    "années mille neuf cent quatre-vingts. Aux dernières élections législatives, près de la moitié des "
    "électeurs inscrits ne se sont pas déplacés.<br>"
    "<strong>Yasmine Karim :</strong> Mais il faut nuancer. L'abstention n'est pas uniforme. Elle est "
    "beaucoup plus forte chez les jeunes de dix-huit à vingt-quatre ans, où elle dépasse souvent les "
    "soixante pour cent, et dans les quartiers populaires. »",
    "Quelle est l'abstention chez les jeunes ?",
    ["Plus de 60 pour cent", "Près de 80 pour cent", "Environ 30 pour cent", "Environ 45 pour cent"],
    """A — <span lang="fr">Plus de 60 pour cent</span> (more than 60 percent)""",
    "it is Yasmine Karim, not the main guest, who gives the figure. In an interview with several voices, "
    "<strong>you have to follow who says what</strong>: « près de la moitié », said just before, refers to all "
    "voters, not to young people.",
    audio="tcf_co_029.m4a", duree="1 min 49 s", ecoutes=1) + exo(
    "en", 4, "B2", "Lecture, 1 female speaker",
    "« Les prédictions les plus alarmistes estiment que l'intelligence artificielle pourrait remplacer "
    "trente à quarante pour cent des emplois actuels d'ici deux mille quarante. Mais je voudrais "
    "apporter un éclairage plus nuancé. L'histoire des révolutions technologiques nous enseigne que la "
    "destruction d'emplois s'accompagne toujours de la création de nouveaux métiers, souvent "
    "impossibles à imaginer à l'avance. Cependant, et c'est là que les choses se compliquent, cette "
    "transition ne se fait pas sans douleur. »",
    "Quelle est son attitude envers les prédictions sur l'IA ?",
    ["Elle accepte complètement et sans réserve les projections les plus alarmistes",
     "Elle estime que les prédictions sous-évaluent le phénomène",
     "Elle reconnaît les chiffres mais les contextualise",
     "Elle conteste les données statistiques présentées"],
    """C — <span lang="fr">Elle reconnaît les chiffres mais les contextualise</span> (she acknowledges the figures but puts them in context)""",
    "<strong>this is what B2 really looks like.</strong> No sentence gives the answer: you have to follow the line "
    "of argument. She quotes the figures, then « je voudrais apporter un éclairage plus nuancé », then "
    "« cependant ». She rejects nothing and endorses nothing: she puts things in context.",
    audio="tcf_co_030.m4a", duree="1 min 29 s", ecoutes=1) + """

<h2 id="b1-b2">What really changes between B1 and B2</h2>

<p>Compare exercises 1–2 with 3–4: the difficulty doesn’t come from the vocabulary, it comes from the <strong>nature of
the question</strong>.</p>
""" + table("What the question asks of you, by level.", ["", "B1 questions", "B2 questions"],
            [("What you are looking for", "A piece of information that is <strong>stated</strong>",
              "An <strong>attitude</strong>, an intention, a point of view"),
             ("Where the answer is", "In one sentence of the recording", "<strong>Nowhere</strong> — you infer it"),
             ("The trap", "A nearby number, a similar word", "A plausible rewording that is too categorical"),
             ("What to follow", "The content", "The <strong>connectors</strong>: « mais », « cependant », « pourtant »")],
            wide=False) + """
<p>The consequence is direct: at B2, it is the <strong>linking words that carry the answer</strong>. « Je voudrais
apporter un éclairage plus nuancé » is worth more than three sentences of content. A candidate who listens to the
information without listening to how it is linked together plateaus around CLB 6, however rich their vocabulary.</p>

<h2 id="tips">Tips: how not to lose track</h2>

<ol>
<li><strong>Read the options before the audio</strong> when time allows. You will then know what to listen for — a
number, a place, an opinion — instead of trying to remember everything.</li>
<li><strong>Drop a lost question immediately.</strong> This is the most important rule, and the hardest to apply. A
single listening means a missed question is <em>permanently</em> lost: hanging on to it makes you miss the next one,
then the third. Losing track in a cascade costs five questions, not one.</li>
<li><strong>Note who is speaking</strong> as soon as there are more than two voices. B2 questions are often about who
said what, as in exercise 3.</li>
<li><strong>Don’t look for certainty on the last questions.</strong> They are C1–C2 level and carry their weight in the
calculation, but they aren’t worth three B1 questions left unanswered.</li>
<li><strong>Always answer.</strong> There are no negative points: a blank answer is worth zero, a random guess gives you
a one-in-four chance.</li>
</ol>

<div class="note">
<p><strong>The number of items on screen may surprise you.</strong> On the computer-based test, France Éducation
international adds items that don’t count towards your score: they are used for its validity analyses. Seeing the test
run longer than the announced 39 is normal and says nothing about your result.</p>
</div>

<h2 id="mistakes">The most costly mistakes</h2>

<ul>
<li><strong>Trying to understand everything.</strong> The goal isn’t to understand the recording, it is to answer the
question asked. A lot of the information is there to take up your attention.</li>
<li><strong>Choosing the most categorical option.</strong> In attitude questions, the extreme options — « accepte
complètement », « conteste » — are almost always wrong. The speaker qualifies what they say; so does the right answer.</li>
<li><strong>Practising with DELF resources.</strong> In the DELF, recordings at levels A1 to B1 are played
<strong>twice</strong>. In the TCF, never. A candidate trained on two listenings discovers the rule on exam day — see
our “diploma or test” comparison (in French).</li>
<li><strong>Mixing up the versions.</strong> The TCF Tout Public has 29 questions in 25 minutes, the TCF Canada 39 in 35.
Practising on the wrong version means preparing for a different pace.</li>
</ul>
""",
    cta_h2="39 questions, one listening: you can rehearse that",
    cta_p="""Hundreds of listening exercises in the exact TCF Canada format, with audio played once and a real timer, a
detailed explanation after each answer and an automatic CLB conversion for each test — in the
“TCF DELF TEF: Tests 2026” app.""",
    faq=[("How many questions are in the TCF Canada listening test?", "39 multiple-choice questions in 35 minutes, or about 54 seconds per question — including the audio, reading the four options and choosing. The difficulty is progressive, from A1 to C2: you aren’t expected to get everything right."),
         ("Can you replay a recording in the TCF Canada listening test?", "No. Each recording is played only once and there is no going back. This is a major difference from the DELF, where recordings at levels A1 to B1 are played twice: many candidates who trained with DELF resources discover this rule on exam day."),
         ("What should I do if I miss a question?", "Move on to the next one immediately. A missed question is permanently lost, since there is only one listening — hanging on to it makes you miss the next one, then the third. Losing track in a cascade costs five questions instead of one."),
         ("What TCF Canada listening score do I need for CLB 7?", "458 out of 699. Watch out for the most costly misunderstanding of the TCF Canada: the B2 band starts at 400, while CLB 7 starts at 458. A score of 430 is labelled B2 on your results certificate but is only worth CLB 6."),
         ("What is the difference between a B1 and a B2 listening question?", "What you are looking for. At B1, the answer is said word for word in the recording: it is about spotting information. At B2, it appears nowhere and has to be inferred from the line of argument — connectors such as « mais », « cependant », « pourtant » carry the answer."),
         ("Should I guess when I don’t know the answer?", "Yes. There are no negative points in the TCF: a blank answer is worth zero, a random guess gives you a one-in-four chance. Never leave a question unanswered, especially the last ones, which are C1–C2 level.")],
    also=[("/en/tcf-canada-reading-practice/", "TCF Canada reading practice", "The other 39-question multiple-choice test, but in 60 minutes and with free navigation."),
          ("/en/tcf-canada/", "TCF Canada exam: format, scores, CLB", "The complete guide to the four tests, scoring and registration."),
          ("/en/tcf-canada-clb-7/", "TCF Canada CLB 7: the exact scores", "458 in listening — and why a “B2” isn’t always CLB 7.")],
    sources="""<strong>Formats change.</strong> This page is up to date as of 7 August 2026. The exercises shown are original
content from our app, designed in the official format — there are no official past TCF papers freely available. Check
the current structure on <a href="https://www.france-education-international.fr/test/tcf-canada" rel="noopener">france-education-international.fr</a>
before your session.""",
))


# ===========================================================================
# TCF CANADA — reading practice (from /blog/exercices-comprehension-ecrite-tcf-canada/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/exercices-comprehension-ecrite-tcf-canada/", lang="en", variant="en-CA",
    slug="tcf-canada-reading-practice",
    crumbs=[HOME, TCF], crumb="Reading practice",
    title="TCF Canada reading practice: sample questions with answers",
    desc="TCF Canada reading: 39 questions in 60 minutes, with free navigation. 4 practice exercises from B1 to B2 with answers, timing and rewording traps.",
    h1="TCF Canada reading practice: four exercises, with answers",
    intro="""<strong>39 questions in 60 minutes</strong> — <strong>1 minute 32 seconds per question</strong> — and,
unlike the listening test, <strong>free navigation</strong> between questions. It is the most comfortable test in the
TCF Canada, and so the one where you must pick up points. Four practice exercises with answers, from B1 to
B2.""",
    facts=["<strong>39 multiple-choice questions, 4 options each · 60 minutes</strong> — about <strong>1 min 32 s per question</strong>.",
           "<strong>Free navigation</strong>: you can go back, unlike in the listening test.",
           "Difficulty is <strong>progressive, A1 → C2</strong>.",
           "Documents: announcements, press articles, argumentative texts, letters.",
           "The jump from B1 to B2 comes down to the <strong>author’s intention</strong>, not the information.",
           "<strong>CLB 7</strong> starts at <strong>453</strong> out of 699 in reading."],
    toc=[("format", "The test format"), ("exercises", "Four sample exercises, with answers"),
         ("navigation", "What free navigation changes"), ("traps", "The four rewording traps"),
         ("method", "The method: reading tips")],
    body="""
<h2 id="format">The test format</h2>
""" + table("TCF Canada reading test. Source: France Éducation international, structure checked in July 2026.",
            ["Parameter", "Value"],
            [("Questions", "<strong>39 multiple-choice questions</strong>, 4 options each"),
             ("Duration", "<strong>60 minutes</strong>"),
             ("Average time per question", "<strong>≈ 1 min 32 s</strong>"),
             ("Navigation", "<strong>free</strong> — you can go back"),
             ("Difficulty", "progressive, from A1 to C2"),
             ("Scoring", """from 100 to 699 → <a href="/en/tcf-canada-clb-7/">CLB</a> (NCLC in French)""")],
            wide=False) + """
<p>A minute and a half per question seems comfortable, and it is — <strong>as long as you don’t reread</strong>. The
documents get longer as the test goes on: a five-line announcement at the start, an argumentative text several
paragraphs long at the end. The time goes on the last documents, not the first ones.</p>

<h2 id="exercises">Four sample exercises, with answers</h2>

<p>As in the listening test, the progression below is that of the real test: two B1 documents, then two B2. Time
yourself at 1 min 30 s per question. The documents, questions and options are in French, as on exam day; the answers
are explained underneath.</p>
""" + exo("en", 1, "B1", "Document — informative article:",
          "« La laïcité est un principe fondamental de la République française, inscrit dans la Constitution "
          "depuis 1958. Ce principe garantit la liberté de conscience et la liberté de religion pour tous "
          "les citoyens. L'État ne reconnaît, ne salarie ni ne subventionne aucun culte, conformément à la "
          "loi de séparation des Églises et de l'État de 1905. Contrairement à certaines idées reçues, la "
          "laïcité n'est pas dirigée contre les religions. Elle vise au contraire à garantir à chacun le "
          "droit de croire ou de ne pas croire. »",
          "Selon le texte, que garantit la laïcité ?",
          ["L'obligation d'être athée pour tous", "La suprématie d'une religion étatique",
           "La liberté de conscience religieuse", "L'interdiction de toutes les religions"],
          """C — <span lang="fr">La liberté de conscience religieuse</span> (freedom of religious conscience)""",
          "the text states it directly: « garantit la liberté de conscience et la liberté de religion ». The other "
          "three options are <strong>classic misconceptions</strong> about <em>laïcité</em>, which the text "
          "explicitly takes care to defuse.") + exo(
    "en", 2, "B1", "Document — informative article:",
    "« Le fonctionnement est simple : lorsqu'un assuré consulte un médecin ou achète des médicaments, "
    "la Sécurité sociale rembourse une partie des frais. Pour le reste, appelé le <em>ticket "
    "modérateur</em>, la plupart des Français souscrivent une mutuelle ou complémentaire santé. Le "
    "médecin traitant joue un rôle central dans ce système. Chaque assuré de plus de 16 ans doit "
    "déclarer un médecin traitant auprès de sa caisse d'assurance maladie. »",
    "Qu'est-ce que le ticket modérateur ?",
    ["Le salaire net du médecin traitant", "Le prix total de la consultation",
     "La part non remboursée par la Sécurité sociale", "Le coût annuel de la carte Vitale"],
    """C — <span lang="fr">La part non remboursée par la Sécurité sociale</span> (the share not reimbursed by social security)""",
    "the text defines the term in apposition: « Pour le reste, appelé le ticket modérateur ». This is a "
    "<strong>definition-in-context</strong> exercise — very common in the TCF, and rewarding: the answer is always "
    "in the sentence that contains the term.") + exo(
    "en", 3, "B2", "Document — opinion article:",
    "« L'idée que la France serait un pays foncièrement hostile à l'immigration est un cliché qui "
    "mérite d'être nuancé. Si les débats publics sur l'immigration sont souvent virulents et "
    "passionnés, la réalité du terrain est bien plus complexe qu'un simple rejet. Historiquement, la "
    "France est une terre d'immigration depuis la fin du XIX<sup>e</sup> siècle. Des vagues "
    "successives de migrants italiens, polonais, espagnols, portugais, puis maghrébins et "
    "subsahariens ont contribué à façonner la société française d'aujourd'hui. »",
    "L'idée que la France est hostile à l'immigration est, selon l'auteur :",
    ["Parfaitement exacte aujourd'hui", "Entièrement fausse en réalité",
     "Un cliché à nuancer largement", "Une invention des médias actuels"],
    """C — <span lang="fr">Un cliché à nuancer largement</span> (a cliché that calls for a lot of nuance)""",
    "the trap is option B. The author does <em>not</em> say the idea is false, but that it « mérite d'être "
    "nuancé ». <strong>Qualifying a claim is not refuting it.</strong> It is the most frequent rewording trap at B2 — an option "
    "that is correct but too categorical.") + exo(
    "en", 4, "B2", "Document — opinion article:",
    "« Il est tentant de croire que la langue française est un bloc monolithique, un monument immuable "
    "dont l'Académie française serait la gardienne infaillible. La réalité est tout autre. Le français "
    "est une langue vivante, en perpétuelle évolution, qui s'enrichit constamment de mots nouveaux, "
    "d'emprunts et de créations. Chaque année, les dictionnaires accueillent des centaines de mots "
    "nouveaux. »",
    "Quelle est la vision courante du français que l'auteur conteste ?",
    ["Le français devrait bannir complètement tous les emprunts étrangers",
     "Le français provient exclusivement de l'anglais et des emprunts étrangers",
     "Le français est un bloc monolithique défendu par l'Académie française",
     "Le français est une langue morte et disparue comme le latin"],
    """C — <span lang="fr">Le français est un bloc monolithique défendu par l'Académie française</span> (French is a monolithic block defended by the Académie française)""",
    "the question doesn’t ask for the author’s thesis but for <strong>the thesis the author argues against</strong>. "
    "It is a question about the structure of the argument: « Il est tentant de croire que… La réalité est tout "
    "autre. » Many candidates answer with the author’s position and get it wrong.") + """

<h2 id="navigation">What free navigation changes</h2>

<p>It is this test’s great advantage, and it is underused. You can <strong>go back</strong> — so you can adopt a
strategy that the listening test rules out.</p>

<ol>
<li><strong>A quick first pass.</strong> Answer all the questions whose answer is immediate, without forcing. That way
you secure most of the points in about thirty minutes.</li>
<li><strong>Flag the doubtful questions</strong> instead of getting bogged down. A B2 question that resists for thirty
seconds will resist for three minutes.</li>
<li><strong>A second pass</strong> on the flagged questions, with the remaining time and a clearer head.</li>
<li><strong>Last minutes: fill in everything.</strong> No answer should be left blank; there are no negative
points.</li>
</ol>

<div class="note">
<p><strong>Don’t reread whole documents.</strong> That is the habit that eats up the time. A question is about a
specific passage: find the passage, not the text. The words of the question almost always lead you to it.</p>
</div>

<h2 id="traps">The four rewording traps</h2>

<p>At B2, the wrong answers aren’t wrong at random: they are <strong>built</strong> on four recurring patterns.</p>
""" + table("How the wrong answers are made.", ["Trap", "What it looks like", "How to spot it"],
            [("<strong>Too categorical</strong>", "« entièrement faux » when the text says « à nuancer »",
              "Look for absolutes: « totalement », « jamais », « exclusivement »"),
             ("<strong>True but off-topic</strong>", "Accurate information from the text that doesn’t answer the question",
              "Reread the question, not the text"),
             ("<strong>Role reversal</strong>", "The author’s thesis presented as the thesis they argue against",
              "Spot « il est tentant de croire », « contrairement à »"),
             ("<strong>Hook word</strong>", "Reuses a rare word from the text to catch your eye",
              "An identical word is not an argument")], wide=False) + """

<h2 id="method">The method: reading tips</h2>

<ul>
<li><strong>Read the question before the document</strong> for long texts. You will know what you are looking for and
avoid reading the whole text.</li>
<li><strong>On opinion questions, look for connectors of contrast</strong> — « mais », « pourtant », « contrairement
à », « il est tentant de croire ». They mark the exact point where the author takes a position.</li>
<li><strong>Be wary of options that reuse the words of the text.</strong> It is often the sign of a hook word, not of a
right answer.</li>
<li><strong>Keep ten minutes</strong> for the second pass and the final fill-in.</li>
<li><strong>Practise on the right version.</strong> The TCF Tout Public has 29 questions in 45 minutes and a “language
structures” section (« structures de la langue ») that the TCF Canada doesn’t have. The full protocol for taking a mock
exam is on our <a href="/en/tcf-canada-practice-test/">practice test page</a>.</li>
</ul>
""",
    cta_h2="1 min 32 s per question: practise against the clock",
    cta_p="""Hundreds of reading exercises in the exact TCF Canada format, with a real timer and free navigation as on
exam day, a detailed explanation after each answer and a CLB conversion for each test — in the
“TCF DELF TEF: Tests 2026” app.""",
    faq=[("How many questions are in the TCF Canada reading test?", "39 multiple-choice questions in 60 minutes, or about 1 minute 32 seconds per question. Navigation is free: unlike in the listening test, you can go back to earlier questions."),
         ("Can you go back to previous questions in the TCF Canada reading test?", "Yes, in the reading test navigation is free. It is this test’s great advantage: do a quick first pass on the immediate questions, flag the doubtful ones, then come back to them with the remaining time. In the listening test, by contrast, there is no going back."),
         ("What TCF Canada reading score do I need for CLB 7?", "453 out of 699 — a slightly different threshold from the listening test, which is 458. Careful: the B2 band starts at 400, so a score labelled B2 on your results certificate doesn’t guarantee CLB 7."),
         ("How are the wrong answers built?", "On four recurring patterns: an option that is too categorical when the text is nuanced, true information that doesn’t answer the question, a reversal between the author’s thesis and the one they argue against, and the hook word that reuses a rare term from the text to catch your eye."),
         ("Do I need to read the whole document?", "Not for long texts. Read the question first, then find the relevant passage: the words of the question almost always lead you there. Rereading whole documents is the habit that eats up time without earning points."),
         ("How much time should I keep for the end?", "About ten minutes. They are for the second pass on the flagged questions and the final fill-in: no answer should be left blank, since there are no negative points in the TCF.")],
    also=[("/en/tcf-canada-listening-practice/", "TCF Canada listening practice", "The sister test, in 35 minutes and with a single listening."),
          ("/en/tcf-canada-writing-tasks/", "TCF Canada writing: the 3 tasks", "The three tasks, their word ranges and a sample topic for each."),
          ("/en/tcf-canada-practice-test/", "Free TCF Canada practice test", "The only two official free resources, and what they don’t cover.")],
    sources="""<strong>Formats change.</strong> This page is up to date as of 7 August 2026. The exercises shown are original
content from our app, designed in the official format — there are no official past TCF papers freely available. Check
the current structure on <a href="https://www.france-education-international.fr/test/tcf-canada" rel="noopener">france-education-international.fr</a>
before your session.""",
))


# ===========================================================================
# TCF CANADA — speaking topics (from /blog/sujets-expression-orale-tcf-canada/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/sujets-expression-orale-tcf-canada/", lang="en", variant="en-CA",
    slug="tcf-canada-speaking-topics",
    crumbs=[HOME, TCF], crumb="Speaking topics",
    title="TCF Canada speaking topics and format: tasks 1, 2 and 3",
    desc="TCF Canada speaking: 3 tasks in 12 minutes, with 2 minutes to prepare task 2. A sample topic per task, what the examiner expects, and time management.",
    h1="TCF Canada speaking: the three tasks, with sample topics",
    intro="""<strong>Three tasks in 12 minutes</strong>, face to face, including just <strong>2 minutes of
preparation</strong> for the second task. It is the shortest test in the TCF Canada — and the worst managed: untrained
candidates use up their time on task 1, the easiest, and rush task 3, the one that earns the most.""",
    facts=["<strong>3 tasks · 12 minutes in total</strong>, face to face, scored out of <strong>20</strong>.",
           "<strong>Task 1</strong>: guided interview — <strong>no preparation</strong>.",
           "<strong>Task 2</strong>: interaction exercise — <strong>2 minutes of preparation</strong>.",
           "<strong>Task 3</strong>: expressing a point of view based on a document.",
           "⚠️ Task 1 is <strong>predictable</strong>: you can prepare it in advance — the structure, not the text.",
           "<strong>CLB 7</strong> (NCLC 7 in French) requires <strong>10/20</strong> in speaking."],
    toc=[("format", "The three tasks"), ("topics", "One sample topic per task"), ("timing", "Managing twelve minutes"),
         ("criteria", "What the examiner assesses"), ("mistakes", "The most costly mistakes")],
    body="""
<h2 id="format">The three tasks</h2>
""" + table("TCF Canada speaking test. Source: France Éducation international, structure checked in July 2026.",
            ["Task", "Type", "Preparation"],
            [("<strong>1</strong>", "Guided interview — you introduce yourself, the examiner asks follow-up questions", "<strong>none</strong>"),
             ("<strong>2</strong>", "Interaction exercise — a situation to resolve", "<strong>2 minutes</strong>"),
             ("<strong>3</strong>", "Expressing a point of view based on a document", "—"),
             ("<strong>Total</strong>", "", "<strong>12 minutes</strong>, preparation included")], wide=False) + """
<p>Twelve minutes for three tasks is very short: about three to four minutes of speaking per task. So the challenge
isn’t lasting the distance, it is being <strong>productive immediately</strong> — a candidate who takes a minute to get
going has lost a quarter of their task.</p>

<h2 id="topics">One sample topic per task</h2>
<p>The instructions are in French, as on exam day; what the examiner looks for is explained underneath.</p>
""" + sujet("en", "Task 1 — Guided interview", "no preparation · the warm-up, one to lock in",
            "Présentez-vous : votre nom, votre âge, votre nationalité, votre situation familiale et votre "
            "métier ou vos études.",
            "<strong>This is the most rewarding task of your whole preparation</strong>, because it is entirely "
            "predictable. Prepare and rehearse out loud a presentation of 60 to 90 seconds, then anticipate the usual "
            "follow-up questions: why are you learning French, what are your plans in Canada, how long have you been "
            "studying. Here the examiner mainly assesses fluency and pronunciation — not the depth of your ideas. "
            "Don’t recite mechanically: learn the structure, not the text.") + \
         sujet("en", "Task 2 — Interaction exercise", "2 minutes of preparation · a situation to resolve",
            "Racontez un voyage ou une visite que vous avez fait(e) en France. Décrivez l'endroit, ce que vous "
            "avez fait, ce qui vous a plu et ce qui vous a moins plu. Expliquez pourquoi vous recommanderiez "
            "ou non cet endroit.",
            "The two minutes of preparation are for noting <strong>keywords, not sentences</strong>. A candidate who "
            "writes sentences and then reads their notes is spotted immediately and penalized on fluency. The "
            "instructions here contain four elements — describe, narrate, nuance, recommend: cover them all, in that "
            "order, and you have a ready-made plan. Past tenses (<em>passé composé</em> and <em>imparfait</em>) are "
            "the grammar point most closely watched in this type of task.") + \
         sujet("en", "Task 3 — Expressing a point of view", "based on a document · the task that earns the most",
            "<em>Document :</em> « Selon une étude récente, 65 % des Français estiment que l'immigration est "
            "trop importante en France. Pourtant, les économistes soulignent que l'immigration contribue "
            "positivement à la croissance économique et compense le vieillissement de la population. »<br>"
            "Donnez votre avis argumenté sur ce décalage entre perception et réalité économique.",
            "<strong>Don’t summarize the document — use it.</strong> The examiner has the text in front of them: "
            "paraphrasing it uses up your time without earning points. Start straight away with your position, then "
            "argue it. Here, the instructions point to a « décalage », a gap: that is what you have to explain, not "
            "immigration in general. Going off-topic is the most costly mistake, even more than language "
            "errors.") + """

<h2 id="timing">Managing twelve minutes</h2>

<ul>
<li><strong>Start immediately.</strong> There is no time for a silence while you think: start with a prepared hook
sentence; it gives you three seconds to organize what comes next.</li>
<li><strong>Don’t over-invest in task 1.</strong> It is easy and reassuring, so candidates settle into it. A 90-second
presentation is enough; the rest of the time belongs to tasks 2 and 3.</li>
<li><strong>Use your two minutes of preparation</strong> for task 2: three or four keywords in the order of your plan,
nothing more.</li>
<li><strong>Save energy for task 3.</strong> It is the most demanding, and it comes last, when fatigue and stress are at
their peak.</li>
<li><strong>Accept the follow-up questions.</strong> An examiner who interrupts or contradicts you isn’t penalizing
you: they are testing your ability to react. Giving in immediately costs points.</li>
</ul>

<h2 id="criteria">What the examiner assesses</h2>
""" + table("Speaking assessment criteria.", ["Criterion", "What it means in practice"],
            [("<strong>Content</strong>", "Have you covered all the elements of the instructions?"),
             ("<strong>Vocabulary</strong>", "Range and precision, not rare words"),
             ("<strong>Grammar</strong>", "Past tenses, agreement, complex structures"),
             ("<strong>Coherence</strong>", "A plan the listener can hear, explicit connectors"),
             ("<strong>Pronunciation</strong>", "Intelligibility, rhythm, intonation")], wide=False) + """
<p>Note that <strong>pronunciation is a criterion in its own right</strong>, and it is the one candidates prepare
least. A rich answer that is hard to follow hits a ceiling: the examiner assesses what they understand, not what you
meant to say.</p>

<h2 id="mistakes">The most costly mistakes</h2>

<ol>
<li><strong>Reciting task 1.</strong> A presentation learned by heart can be heard, and the examiner immediately asks
questions off your script. Learn the structure, not the sentences.</li>
<li><strong>Writing sentences during the two minutes of preparation.</strong> You won’t have time to say it all, and
reading from notes is easy to spot.</li>
<li><strong>Paraphrasing the document in task 3.</strong> The examiner has it in front of them. Open with your
position.</li>
<li><strong>Not answering the question asked.</strong> It is the most costly mistake, and it has nothing to do with
your level of French.</li>
<li><strong>Not practising out loud.</strong> Preparing for the speaking test by reading is the best way to find out on
exam day that you can’t keep going for three minutes.</li>
</ol>
""",
    cta_h2="You don’t prepare for the speaking test by reading",
    cta_p="""Hundreds of speaking topics in the exact TCF Canada format, with a real timer and real preparation time.
You speak, the app transcribes and scores — pronunciation and fluency included — against the official criteria, as
many times as you need. In the “TCF DELF TEF: Tests 2026” app.""",
    faq=[("How long is the TCF Canada speaking test?", "12 minutes in total for the three tasks, face to face, including 2 minutes of preparation for the second task. That is very short: count on about three to four minutes of speaking per task, with no downtime."),
         ("What are the three TCF Canada speaking tasks?", "A guided interview in which you introduce yourself and the examiner asks follow-up questions, with no preparation; an interaction exercise with 2 minutes of preparation; then expressing a point of view based on a prompt document."),
         ("How do I prepare for TCF Canada speaking task 1?", "It is the most rewarding task of your whole preparation, because it is entirely predictable. Rehearse a presentation of 60 to 90 seconds out loud and anticipate the usual follow-up questions: why you are learning French, your plans, how long you have been studying. Learn the structure, never the text — a recitation can be heard."),
         ("What should I do during the two minutes of preparation for task 2?", "Note three or four keywords in the order of your plan, nothing more. Writing sentences is counterproductive: you won’t have time to say it all, and reading from notes is spotted immediately and costs points on fluency."),
         ("Should I summarize the document in speaking task 3?", "No. The examiner has it in front of them: paraphrasing it uses up your time without earning points. Start straight away with your position, then argue it — answering precisely the question asked, which is often about one particular aspect of the document."),
         ("What if the examiner contradicts me?", "Hold your position, but qualify it. An examiner who follows up or objects isn’t penalizing you: they are testing your ability to react and to defend a point of view. Giving in at the first objection costs points on the content criterion.")],
    also=[("/en/tcf-canada-writing-tasks/", "TCF Canada writing: the 3 tasks", "The other productive test, with its three word ranges."),
          ("/en/tcf-canada/", "TCF Canada exam: format, scores, CLB", "The complete guide to the four tests and the CLB conversion."),
          ("/en/tcf-canada-clb-7/", "TCF Canada CLB 7: the exact scores", "10/20 in speaking — and why a single point changes your level.")],
    sources="""<strong>Formats change.</strong> This page is up to date as of 7 August 2026. The topics shown are original
content from our app, designed in the official format — there are no official past TCF papers freely available. Check
the current structure on <a href="https://www.france-education-international.fr/test/tcf-canada" rel="noopener">france-education-international.fr</a>
before your session.""",
))


# ===========================================================================
# TCF CANADA — free practice test (from /blog/examen-blanc-tcf-gratuit/, with the mock-exam
# criteria, protocol and app facts of /examens-blancs/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/examen-blanc-tcf-gratuit/", lang="en", variant="en-CA",
    slug="tcf-canada-practice-test",
    crumbs=[HOME, TCF], crumb="Free practice test",
    title="Free TCF Canada practice test: resources and mock exams",
    desc="No official past papers exist. The two free official TCF resources (TV5MONDE, RFI), what they really cover, and how to take a real TCF Canada mock exam.",
    h1="Free TCF Canada practice test: training in real exam conditions",
    intro="""There are <strong>two</strong> free TCF practice resources officially recognized by France Éducation
international: <strong>TV5MONDE</strong> and <strong>RFI</strong>. They are excellent, and enough for the listening and
reading tests. What they don’t cover — writing and speaking, and a full timed simulation — is exactly what costs the
most points on exam day. And both follow the TCF tout public format, not the TCF Canada one.""",
    facts=["<strong>No official past papers exist</strong>: TCF topics are strictly confidential.",
           "TV5MONDE: <strong>17 practice sets, 680 questions</strong>, written by the designers of the official tests.",
           "RFI: <strong>12 listening sessions</strong> of 16 questions, signed by France Éducation international.",
           "FEI’s official sample page has only <strong>14 questions and no audio</strong>.",
           "In the exam, <strong>each recording is played only once</strong>.",
           "The score is <strong>not</strong> a simple proportion of correct answers: a scoring scale weights each question by its difficulty.",
           "A real TCF Canada mock exam: <strong>all four tests, 2 hours 47 minutes</strong>, in one sitting, against the clock."],
    toc=[("past-papers", "Why there are no official past papers"), ("free-resources", "The two free official resources"),
         ("fei", "What FEI’s website really offers"), ("format", "The exact format of your version"),
         ("scoring", "Understanding the score out of 699"), ("method", "Turning these resources into a real mock exam"),
         ("limits", "What free resources don’t cover"), ("real-mock-exam", "What a real mock exam must respect"),
         ("app", "How the app’s mock exams work")],
    body="""
<h2 id="past-papers">Why there are no official past papers</h2>

<p>Let’s start by clearing away a costly illusion. <strong>TCF topics are strictly confidential</strong>, and any
reproduction or distribution, partial or total — question, image or sound — is prohibited. So there are no official
published past papers, and there won’t be.</p>

<p>Any site that claims to sell you “the real topics from the exam” or “this month’s predictions” is distributing either
counterfeits or documents obtained illegally. For a candidate whose immigration or citizenship application is at stake,
it is a completely unnecessary risk.</p>

<p>The good news: the TCF is a <strong>standardized, calibrated, ISO 9001-certified</strong> test. Every question is
pretested, analyzed psychometrically, then calibrated. So you don’t need the real topics — you need to master the
<em>format</em>, and that is available for free.</p>

<h2 id="free-resources">The two free official resources</h2>

<p>France Éducation international cites two, and only two, across all its TCF pages.</p>

<h3>TV5MONDE — the most complete practice</h3>

<p>It is the most solid resource, by far. It offers <strong>17 practice sets, or 680 questions</strong>, covering
listening, language structures and reading.</p>

<p>Its decisive argument: the questions are <strong>“written by the designers of the official tests and validated by
the TCF office of France Éducation international”</strong>. You aren’t practising on imitations, but on material
produced by the same people as the exam. About 200,000 candidates a year prepare for it.</p>

<p>TV5MONDE also offers a <strong>free timed simulator</strong> — a 90-minute test that, in its own words, “brings
together the same conditions as an official session”. And <strong>downloadable PDF practice booklets</strong>, with the
680 questions, their answers and their audio.</p>

<p>→ <a href="https://apprendre.tv5monde.com/fr/tcf" rel="noopener">apprendre.tv5monde.com/fr/tcf</a></p>

<h3>RFI — listening, in the exact format</h3>

<p><em lang="fr">Le français facile avec RFI</em> offers <strong>12 practice sessions for the listening test</strong>,
signed “France Éducation international”, of <strong>16 questions</strong> each, from A2 to B2.</p>

<p>Two strengths that TV5MONDE doesn’t have. First, RFI explicitly states the single-listening rule — “in real exam
conditions, you will hear the document and the question only once” — and provides the <strong>transcripts</strong> so
you can work on them afterwards. Second, a <strong>self-assessment scale</strong> for its 16 questions:</p>
""" + table("""Level self-assessment scale provided by RFI for its 16-question listening sets. Source: <span lang="fr">Le français facile avec RFI</span>, in collaboration with France Éducation international.""",
            ["Score out of 16", "Estimated level"],
            [("from 2", "A2"), ("from 6", "B1"), ("from 10", "<strong>B2</strong>"), ("from 14", "C1"),
             ("16", "C1 and above")], wide=False) + """

<div class="note">
<p><strong>Two practical warnings about RFI.</strong> The exercises rely on a technology (H5P) that <strong>doesn’t
display if you refuse audience-measurement and advertising cookies</strong> — if the page looks empty, that is why.
Also, the URL printed in the official candidate handbook doesn’t lead directly to the practice exercises; go through
the site’s search.</p>
</div>

<h2 id="fei">What FEI’s website really offers</h2>

<p>Many candidates look for a mock exam on the official TCF website. Let’s be clear, to spare you the disappointment:
<strong>the « Exemples d'épreuves du TCF » page contains only 14 questions in total</strong> — 7 in listening, 3 in
language structures, 4 in reading.</p>

<p>Above all, <strong>it has no audio files</strong>: the seven listening examples are given as written transcripts
(« Vous entendez : … »). For the test where candidates struggle most, that is obviously not enough.</p>

<p>On the other hand, FEI publishes two free documents that are genuinely useful: the <strong>« Grilles de niveaux du
TCF »</strong> (level grids) and a <strong>sample results certificate</strong> for each version (TCF Canada, TCF IRN,
TCF Québec, TCF tout public). Knowing what your future certificate looks like avoids a lot of unpleasant surprises.</p>

<p>As for <span lang="fr">Le Point du FLE</span>, often cited: its TCF section <strong>hosts no content of its
own</strong> — it consists only of outbound links to the same two official resources.</p>

<h2 id="format">The exact format of your version</h2>

<p>A classic mistake: practising on the TCF tout public format when you are taking the TCF Canada. The tests have
neither the same number of questions nor the same duration.</p>
""" + table("Official formats of the main TCF versions. Source: France Éducation international, checked in July 2026.",
            ["Test", "TCF tout public", "TCF Canada", "TCF Québec", "TCF IRN"],
            [("Listening", "29 MCQs · 25 min", "<strong>39 MCQs · 35 min</strong>", "29 MCQs · 25 min", "25 MCQs · 20 min"),
             ("Language structures", "18 MCQs · 15 min", "—", "—", "—"),
             ("Reading", "29 MCQs · 45 min", "<strong>39 MCQs · 60 min</strong>", "29 MCQs · 45 min", "25 MCQs · 35 min"),
             ("Writing", "3 tasks · 60 min", "3 tasks · 60 min", "3 tasks · 60 min", "3 tasks · 30 min"),
             ("Speaking", "3 tasks · 12 min", "3 tasks · 12 min", "3 tasks · 12 min", "3 tasks · 10 min")],
            wide=False) + """
<p>The <a href="/en/tcf-canada/">TCF Canada</a> requires all four tests; the TCF Québec is <strong>modular</strong>
(you choose 1, 2, 3 or 4 tests); the TCF IRN was shortened when it changed on 12 May 2025 and has <strong>no
preparation time</strong> in the speaking test, whereas the other versions allow 2 minutes for the second task.</p>

<p>A detail worth knowing if you take the test on a computer: the multiple-choice part then has <strong>91 items
instead of 76</strong> in the TCF tout public. The 15 extra items (5 per skill) <strong>don’t count towards your
score</strong> — they are used for FEI’s validity analyses. Don’t panic when you see the test run longer.</p>

<h2 id="scoring">Understanding the score out of 699</h2>
""" + table("TCF scoring scale and the matching CEFR levels. Source: official TCF documentation, France Éducation international.",
            ["CEFR level", "Score /699 (listening, reading)", "Score /20 (writing, speaking)"],
            [("A1 not reached", "0–99", "—"), ("A1", "100–199", "1"), ("A2", "200–299", "2–5"), ("B1", "300–399", "6–9"),
             ("B2", "400–499", "10–13"), ("C1", "500–599", "14–17"), ("C2", "600–699", "18–20")], wide=False) + """
<p>Three things to remember. First, <strong>the TCF has no “pass” mark</strong>: the lowest result is “A1 not
reached”, so you can’t “fail” the TCF in the strict sense — you get a level.</p>

<p>Second, <strong>the score is not the number of correct answers</strong>. A scoring scale takes the difficulty of
each question into account and turns your total into a calibrated score. So you can’t predict your score by counting
your points on a practice test.</p>

<p>Finally, <strong>gaps between skills are normal</strong> and officially expected. FEI also acknowledges variability
between sessions: a candidate on the borderline of a level can get 304 points one time and 295 the next. If you are
aiming for a precise threshold — for example <a href="/en/tcf-canada-clb-7/">CLB 7 (NCLC 7 in French) for Express
Entry</a> — always leave a margin.</p>

<h2 id="method">Turning these resources into a real mock exam</h2>

<p>Doing random multiple-choice questions doesn’t prepare you for the TCF. Here is how to turn the free material into a
useful simulation.</p>

<ol>
<li><strong>One listening, no exceptions.</strong> This is the format rule that costs the most points. If you practise
by replaying, you are preparing for an exam that doesn’t exist. Play the audio once, answer, move on.</li>
<li><strong>Time yourself to YOUR version’s format</strong>, not the simulator’s. The TV5MONDE simulator lasts 90
minutes; the three compulsory tests of the TCF tout public take 85 (25 + 15 + 45).</li>
<li><strong>Do the tests back to back, without a break</strong>, in the real order. The fatigue of the reading test
after 35 minutes of listening is part of the exam.</li>
<li><strong>Write by hand if you are taking the paper-based test.</strong> An illegible paper is marked “A1 not
reached”, whatever its content.</li>
<li><strong>Count your words.</strong> Not respecting the required word count on a single task is enough to drop the
whole writing test to “A1 not reached”.</li>
<li><strong>Use the RFI transcripts afterwards</strong>, never during. That is where you understand <em>why</em> you
missed a question.</li>
</ol>

<div class="note">
<p><strong>Five things get a writing paper marked “A1 not reached”</strong>, regardless of your real level: illegible
handwriting on the paper-based test, not respecting the word count on a task, an off-topic answer, a task not done,
and a blank paper. Note too that <strong>your draft is never marked</strong> — only what is in the answer booklet
counts.</p>
</div>

<h2 id="limits">What free resources don’t cover</h2>

<p>Let’s be honest: the free official resources are good, and you should use them. But they stop where the exam
becomes decisive.</p>

<ul>
<li><strong>No correction of writing or speaking.</strong> Yet these are the two tests scored out of 20, where a single
point moves you from one CLB level to the next. Nobody will tell you for free whether your work is worth 9 or 11.</li>
<li><strong>No full simulation of the four tests.</strong> The TV5MONDE simulator only covers the three compulsory
tests of the TCF tout public.</li>
<li><strong>Limited volume.</strong> 680 TV5MONDE questions and 12 RFI sessions is substantial — but you get through
them in a few weeks of serious preparation.</li>
<li><strong>No practice in the Canada, Québec or IRN format specifically.</strong> The sets follow the TCF tout public
format.</li>
</ul>

<p>For the full specification of a reliable simulation — official durations, scoring, test-taking protocol — see
<a href="#real-mock-exam">the next section</a>; and for the blind spot of free resources, writing and speaking, see
<a href="#app">how the app’s AI correction works</a>.</p>

<h2 id="real-mock-exam">What a real mock exam must respect</h2>

<p>A mock exam is the only reliable way to know, before you pay, whether you are ready — provided it really follows the
official format. Four criteria, in order of importance:</p>

<ol>
<li><strong>The official durations and instructions</strong>, test by test, in the 2025–2026 formats. A mock exam
built on an old format trains you for an exam that no longer exists.</li>
<li><strong>The official scoring</strong>: for the TCF, the 699 scale with a CEFR level for each test. For the TCF
Canada, that means all four tests, <strong>2 hours 47 minutes</strong> in total, scored out of 699 in listening and
reading and out of 20 in writing and speaking, then converted to CLB.</li>
<li><strong>Original topics.</strong> Practising on “leaked” topics is the best way to overestimate your level — and a
real risk for an immigration application.</li>
<li><strong>A real correction of writing and speaking</strong>, not just self-marking multiple-choice questions. It is
the criterion most often missing, and the most decisive.</li>
</ol>

<p>A badly taken mock exam gives a reassuring, false result. Five rules are enough to keep it honest:</p>

<ul>
<li><strong>In one sitting.</strong> On exam day, the listening, reading and writing tests run back to back. The fatigue of the third hour is
part of what you are testing.</li>
<li><strong>A visible timer — and stick to it.</strong> When the time for a test is up, you stop, even mid-sentence. That
is exactly what will happen.</li>
<li><strong>One listening when the format requires it.</strong> In the TCF, as in the TEF, listening recordings are not
replayed and you can’t go back. Replaying “just once” invalidates the measure.</li>
<li><strong>No outside tools.</strong> No dictionary, spellchecker or translator. You won’t have any on exam day.</li>
<li><strong>Speaking too.</strong> It is the test everyone skips when practising alone, and often the one that caps the
result. Record yourself, respect the planned preparation time, and speak out loud even without anyone to talk to.</li>
</ul>

<p>As for pace: one full mock exam before any revision — it is your diagnostic — then about one a week while you
prepare, with targeted exercises on your weakest test in between, and two or three full ones in the last ten days.</p>

<h2 id="app">How the app’s mock exams work</h2>

<p>What the mock exams in the “TCF DELF TEF: Tests 2026” app offer:</p>

<ul>
<li><strong>15 exam variants in the exact official format</strong>, the TCF Canada among them, with a real timer.</li>
<li><strong>Scoring on the official scales</strong>, with an immediate CLB and CEFR conversion for each test.</li>
<li><strong>AI correction of writing and speaking</strong> against the official criteria. In speaking, you talk, and the
app transcribes and scores — pronunciation and fluency included.</li>
<li><strong>Hundreds of exercises</strong> in the exact TCF Canada format: listening with the audio played once,
reading with free navigation as on exam day, and a detailed explanation after each answer.</li>
<li><strong>Original topics</strong>, designed in the official format. No account needed.</li>
</ul>

<p><strong>Is it free?</strong> Most of the app can be used for free every day. Access to all the mock exams and to
unlimited AI assessments is part of the Premium subscription.</p>
""",
    cta_h2="What free resources don’t do: correct your writing and speaking",
    cta_p="""Timed mock exams in the exact format of each version, AI correction of writing and speaking against the
official criteria, an immediate CLB and CEFR conversion for each test — in the “TCF DELF TEF: Tests 2026” app.""",
    faq=[("Are there official TCF Canada past papers?", "No. TCF topics are strictly confidential and any reproduction is prohibited, so there are no official published past papers. Any site that claims to sell “real topics from the exam” is distributing either counterfeits or documents obtained illegally — a real risk for an immigration or citizenship application."),
         ("Is there a free TCF Canada practice test?", "Not in the TCF Canada format specifically. France Éducation international cites two free resources, and only two, on all its TCF pages: listening practice on <em lang=\"fr\">Le français facile avec RFI</em>, and practice for the compulsory tests on TV5MONDE’s learning site, whose questions are written by the designers of the official tests and validated by the TCF office. Both follow the TCF tout public format, and neither corrects writing or speaking."),
         ("Where can I find official TCF sample questions?", "On FEI’s « Exemples d'épreuves du TCF » page — but it has only 14 questions in total (7 in listening, 3 in language structures, 4 in reading) and no audio: the listening examples are written transcripts. TV5MONDE offers 680 questions in 17 sets, and RFI 12 listening sessions of 16 questions."),
         ("Does TV5MONDE’s free simulator replace a real mock exam?", "It comes close to the conditions: it is a 90-minute timed test that recreates the conditions of an official session, for the three compulsory tests of the TCF tout public. But it covers neither writing nor speaking, and its length differs slightly from the real 85 minutes. It is an excellent starting point, not a full simulation."),
         ("Can I calculate my TCF score myself after a practice test?", "Not exactly. The TCF score isn’t a simple proportion of your correct answers: a scoring scale weights each question by its difficulty and turns the total into a calibrated score from 100 to 699. You can estimate a trend, not predict a score. RFI does, however, provide a useful self-assessment scale for its 16-question sets."),
         ("Why does my TCF score vary from one session to the next?", "It is officially acknowledged. France Éducation international explains that a candidate on the borderline of a level can get 304 points in one session and 295 in the next — and so change level without any change in ability. The practical conclusion: never aim for the exact threshold of the level you need; leave a margin."),
         ("How many times can I listen to a recording in the exam?", "Once. It is the rule that costs the most points for anyone who practised with exercises they could replay at will. Each recording is played only once, and the question is asked after listening. Make sure you practise under this condition."),
         ("Is the TCF Canada practice test in the app free?", "Most of the app can be used for free every day. Access to all the mock exams and to unlimited AI assessments is part of the Premium subscription.")],
    also=[("/en/tcf-canada-listening-practice/", "TCF Canada listening practice", "Four sample exercises with audio, played once, and the answers explained."),
          ("/en/tcf-canada-reading-practice/", "TCF Canada reading practice", "39 multiple-choice questions in 60 minutes, with answers explained."),
          ("/en/tcf-canada-speaking-topics/", "TCF Canada speaking: the 3 tasks", "The test free resources don’t correct, in only 12 minutes.")],
    sources="""<strong>Formats change.</strong> This article is up to date as of 27 July 2026 and describes the official
formats in force on that date — the TCF IRN, for example, changed on 12 May 2025. The sections on what a mock exam must
respect and on the app’s mock exams are up to date as of 7 August 2026. Always check the format and durations of your
version on <a href="https://www.france-education-international.fr/test/tcf" rel="noopener">france-education-international.fr</a>
before your session, and with your test centre for the delivery mode (paper-based or computer-based).""",
))

# Traductions en-CA (08/10/2026) de quatre guides du blog. Aucun fait nouveau : chaque chiffre, date et règle vient
# des pages françaises publiées, avec sa date. Fusions : tcf-vs-tef-canada = tcf-ou-tef-canada + difference-tcf-tef ;
# tcf-canada-results = validite-attestation-tcf-tef + repasser-tcf-tef (+ délais de résultats de tcf-canada-nclc-7,
# tcf-ou-tef-canada et tcf-canada-dates-2026, fin de la recorrection au 1er septembre 2026 de tcf-canada-dates-2026).


# ===========================================================================
# TCF CANADA — CLB 7 (from /blog/tcf-canada-nclc-7/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/tcf-canada-nclc-7/", lang="en", variant="en-CA", slug="tcf-canada-clb-7",
    crumbs=[HOME, TCF], crumb="CLB 7",
    title="TCF Canada CLB 7: the score you need in each test",
    desc="TCF Canada CLB 7 (NCLC 7): 458 in listening, 453 in reading, 10/20 in speaking and writing. Why B2 isn’t enough, and what CLB 7 earns in Express Entry.",
    h1="TCF Canada CLB 7: exactly what score to aim for",
    intro="""To reach <strong>CLB 7</strong> on the TCF Canada — NCLC 7 in French — you need <strong>458</strong> in
listening, <strong>453</strong> in reading and <strong>10 out of 20</strong> in both speaking and writing. Each skill
counts separately: <strong>no compensation</strong> is possible, and your lowest score decides.""",
    facts=["CLB 7: listening <strong>458–502</strong> · reading <strong>453–498</strong> · speaking and writing <strong>10–11/20</strong>.",
           "⚠️ A <strong>“B2” on your results certificate doesn’t guarantee CLB 7</strong>: the B2 band starts at 400, CLB 7 at 453.",
           "Your results certificate <strong>shows no CLB level</strong> — the conversion is up to you.",
           "<strong>A single point</strong> separates CLB 6 from CLB 7: 457 versus 458 in listening.",
           "CLB 7 in all 4 skills = <strong>25 or 50 additional CRS points</strong>.",
           "The 2026 French-language Express Entry rounds closed at a CRS of <strong>399 to 420</strong>, versus 514–518 for the Canadian Experience Class."],
    toc=[("table", "The complete official conversion table"), ("b2-trap", "The “B2” trap"),
         ("one-point", "One point separates CLB 6 from CLB 7"), ("points", "What CLB 7 is really worth"),
         ("quebec", "Federal CLB 7 ≠ Quebec level 7"), ("format-retakes", "Format, timelines, retakes")],
    body="""
<h2 id="table">The complete official conversion table</h2>
<p>Here is the equivalency chart published by IRCC. It is the one that counts for your Express Entry profile — and the
only one.</p>
""" + table("TCF Canada → CLB. Listening and reading scored out of 699, speaking and writing out of 20. Source: IRCC equivalency tables, cross-checked on two official pages on 27 July 2026.",
            ["CLB", "Listening", "Reading", "Speaking", "Writing"],
            [("<strong>10+</strong>", "549–699", "549–699", "16–20", "16–20"), ("<strong>9</strong>", "523–548", "524–548", "14–15", "14–15"),
             ("<strong>8</strong>", "503–522", "499–523", "12–13", "12–13"), ("<strong>7</strong>", "458–502", "453–498", "10–11", "10–11"),
             ("<strong>6</strong>", "398–457", "406–452", "7–9", "7–9"), ("<strong>5</strong>", "369–397", "375–405", "6", "6"),
             ("<strong>4</strong>", "331–368", "342–374", "4–5", "4–5")], wide=False) + """
<div class="note">
<p><strong>Beware of figures you find online.</strong> While checking this table, we found that results shown at the top
of search engines gave <em>wrong</em> ranges for CLB 7. Never copy a conversion table without checking IRCC’s official
page: your application depends on it.</p>
</div>

<h2 id="b2-trap">The “B2” trap: when B2 isn’t enough</h2>
<p>It is the most expensive mistake in the TCF Canada, and every year it catches candidates who thought they had
made it.</p>
<p><strong>Your TCF Canada results certificate shows no CLB level.</strong> It gives a score out of 699 for listening
and reading, a mark out of 20 for speaking and writing, and the equivalent of each as a <strong>CEFR</strong> level —
from “below A1” up to C2. Converting to CLB is up to you.</p>
<p>But the two scales don’t line up. The TCF’s CEFR bands are wide:</p>
""" + table("TCF score bands and the matching CEFR levels. Source: official TCF documentation, France Éducation international.",
            ["CEFR level", "Score /699", "Speaking and writing /20"],
            [("Below A1", "0–99", "—"), ("A1", "100–199", "1"), ("A2", "200–299", "2–5"), ("B1", "300–399", "6–9"),
             ("<strong>B2</strong>", "<strong>400–499</strong>", "<strong>10–13</strong>"), ("C1", "500–599", "14–17"),
             ("C2", "600–699", "18–20")], wide=False) + """
<p>Now compare with the CLB table. In reading, <strong>CLB 6 runs from 406 to 452 — and that whole range is labelled
B2</strong> on your certificate. A score of 430 proudly displays “B2” and is still only worth CLB 6.</p>
<p>In other words: <strong>some B2s are not worth CLB 7.</strong> If you are aiming for Express Entry, never rely on
the CEFR level printed on your certificate — look up your raw scores in the CLB table above, skill by skill.</p>

<h2 id="one-point">One point separates CLB 6 from CLB 7</h2>
<p>The boundary is unforgiving, and you need to know it before you register:</p>
<ul>
<li>Listening: <strong>457 = CLB 6</strong>, <strong>458 = CLB 7</strong></li>
<li>Reading: <strong>452 = CLB 6</strong>, <strong>453 = CLB 7</strong></li>
<li>Speaking and writing: <strong>9/20 = CLB 6</strong>, <strong>10/20 = CLB 7</strong></li>
</ul>
<p>One point. And that margin matters all the more because <strong>the TCF score is not a simple proportion</strong> of
your correct answers: a scoring model weights each question by its difficulty and converts the total into a calibrated
score. So you can’t predict your score by counting your right answers.</p>
<p>France Éducation international even officially acknowledges some variability: the same candidate on the edge of a
level can score 304 points at one session and 295 at the next — and so change level without any change in ability. The
practical conclusion is simple: <strong>never aim for the exact threshold</strong>. If you need CLB 7, train for
CLB 8.</p>

<h2 id="points">What CLB 7 is really worth</h2>
<p>CLB 7 in all four skills is the threshold that unlocks three things.</p>
<p><strong>1. The French bonus points.</strong> You get <strong>25 additional CRS points</strong> if your English is
at CLB 4 or lower — or if you haven’t taken any English test — and <strong>50 points</strong> if you have CLB 5 or
higher in all four skills in English. These points come on top of those for the language factor itself.</p>
<p>This bonus carries more weight today than it used to: since 25 March 2025, <strong>IRCC has removed all points
for a job offer</strong>. The 50 French points therefore make up a much larger share of your score.</p>
<p><strong>2. Access to the “French-language proficiency” rounds.</strong> That is where the real advantage lies, and
the figures speak for themselves:</p>
""" + table("2026 Express Entry rounds of invitations: French-language proficiency category versus Canadian Experience Class. Source: IRCC, data checked on 27 July 2026.",
            ["Date", "French-language proficiency round — CRS", "Canadian Experience Class — CRS"],
            [("22 July 2026", "<strong>399</strong> (5,000 invitations)", "—"), ("21 July 2026", "—", "516"),
             ("9 July 2026", "<strong>420</strong> (5,000)", "517"), ("28 May 2026", "<strong>409</strong> (4,500)", "518"),
             ("29 April 2026", "<strong>400</strong> (4,000)", "514"), ("15 April 2026", "<strong>419</strong> (4,000)", "—")],
            wide=False) + """
<p><strong>A gap of about 100 to 120 points.</strong> A French-speaking candidate with 410 points is invited; the same
profile without French would be waiting for a cut-off above 500. It is by far the most powerful lever in an economic
immigration application to Canada today.</p>
<p><strong>3. The post-graduation work permit.</strong> For applications submitted since 1 November, the
post-graduation work permit (PGWP) requires <strong>CLB 7</strong> in all four skills for a university degree
(bachelor’s, master’s, doctorate) and CLB 5 for a college or other non-university program.</p>

<h2 id="quebec">Federal CLB 7 ≠ Quebec level 7</h2>
<div class="note">
<p>Quebec doesn’t use CLB levels but the <em lang="fr">Échelle québécoise des niveaux de compétence en français</em>
(the Quebec scale of French proficiency levels), graded from 1 to 12. The two frameworks use identical numbers and
don’t cover the same scores.</p>
</div>
<p>In listening, <strong>Quebec level 7 starts at 400</strong>, whereas <strong>federal CLB 7 starts at 458</strong>. A
score of 430 therefore gives you level 7 in Quebec, and only CLB 6 at the federal level. On the Quebec scale, the
400–499 band corresponds to levels 7–8.</p>
<p>Two things to remember about the two systems: the <strong>TCF Canada is accepted by Quebec</strong> (MIFI) for the
PSTQ, its skilled worker selection program, but <strong>the reverse isn’t true</strong> — the TCF Québec is not accepted
by IRCC for Express Entry. IRCC accepts only two tests: the TCF Canada and the <a href="/en/tef-canada/">TEF Canada</a>.
Neither the TCF tout public nor the TCF IRN will do.</p>
<p>For stream 1 of the PSTQ, Quebec requires level 7 or higher in oral French and level 5 or higher in written French.
An accompanying spouse must reach level 4 in oral French. If you are torn between the two tests, our comparison
<a href="/en/tcf-vs-tef-canada/">TCF or TEF Canada</a> sets out both charts.</p>

<h2 id="format-retakes">Format, timelines, retakes</h2>
<p>The TCF Canada has <strong>four compulsory tests</strong>, for a total of <strong>2 hours 47 minutes</strong>:
listening (39 multiple-choice questions, 35 min), reading (39 multiple-choice questions, 60 min), writing (3 tasks,
60 min) and speaking (3 tasks).</p>
<p>Results are published within <strong>15 business days</strong> of France Éducation international receiving the
session materials, and the results certificate is <strong>valid for 2 years</strong> from the date it is issued. Watch
out for IRCC’s rule, which is stricter than it looks: your results must be less than two years old <strong>when you
create your Express Entry profile</strong> <em>and</em> when you submit your application for permanent residence.</p>
<p><strong>There is no partial retake.</strong> You can’t retake only the test that went wrong: it’s the full test
again, with a compulsory <strong>20-day</strong> wait between two attempts. The number of attempts, on the other hand,
is unlimited.</p>
<p>For sessions held since 1 September 2026, France Éducation international <strong>no longer accepts re-marking
requests</strong>; before that, re-marking covered only speaking and writing — never the multiple-choice tests — had to be
requested within a month of the results certificates being sent to the centre, and the new mark replaced the old one,
<strong>even if it was lower</strong>.</p>
<p>The practical conclusion: every attempt costs money, so test yourself <em>before</em> you register. A
<a href="/en/tcf-canada-practice-test/">practice test in the official format</a> shows where you stand test by test,
and AI feedback tells you whether your speaking or writing is worth 9 or 11 out of 20 — precisely the line between
CLB 6 and CLB 7.</p>
<p>Then you need a session: in France, the centres that offer the TCF Canada open about one date a month, from €195 to
€285; in Canada, the 47 approved centres are often full within minutes, from $390 to $440. Our guides to where to take
the TCF Canada in France and <a href="/en/tcf-canada-test-centres/">in Canada</a> list the centres, their prices and
their dates — as do our guides for Algeria, Morocco and Tunisia.</p>
""",
    cta_h2="Know where you stand before paying $440",
    cta_p="""Timed mock exams in the exact TCF Canada format, an automatic CLB conversion for each test, and AI feedback on
writing and speaking against the official criteria — in the “TCF DELF TEF: Tests 2026” app.""",
    faq=[("What TCF Canada score do I need for CLB 7?", "458 to 502 in listening, 453 to 498 in reading, and 10 to 11 out of 20 in both speaking and writing. The four skills are assessed separately: there is no compensation between them, and your lowest skill is the one that determines your application."),
         ("I have B2 on my results certificate. Do I have CLB 7?", "Not necessarily, and it’s the costliest trap in the TCF Canada. The TCF’s B2 band runs from 400 to 499, whereas CLB 7 starts at 458 in listening and 453 in reading. A score of 430 is therefore labelled B2 on your certificate but is only worth CLB 6. Your certificate shows no CLB level: you have to do the conversion yourself."),
         ("How many CRS points is CLB 7 in French worth in Express Entry?", "With CLB 7 or higher in all four skills, you get 25 additional points if your English is at CLB 4 or lower (or if you haven’t taken any English test), and 50 additional points if you have CLB 5 or higher in all four skills in English. These points come on top of those for the language factor itself."),
         ("Is the TCF Québec accepted for Express Entry?", "No. IRCC accepts only two French tests for Express Entry: the TCF Canada and the TEF Canada. The TCF Québec, the TCF tout public and the TCF IRN are not on the list. Quebec, on the other hand, accepts the TCF Canada for its own programs, including the PSTQ."),
         ("Is Quebec level 7 the same as CLB 7?", "No, and mixing them up is a common mistake. On the Quebec scale, level 7 in listening starts at 400, whereas federal CLB 7 starts at 458. A score of 430 therefore gives you level 7 in Quebec but only CLB 6 at the federal level. They are two separate frameworks."),
         ("Can I retake only the section I failed?", "No. The TCF Canada has four compulsory tests taken together; there is no partial retake. You can retake the test as many times as you like, with a compulsory 20-day wait between two attempts. And for sessions held since 1 September 2026, re-marking requests are no longer accepted.")],
    also=[("/en/tcf-canada/score-clb/", "TCF Canada score chart and CLB calculator", "Enter your four scores and see your CLB level, skill by skill."),
          ("/en/tcf-vs-tef-canada/", "TCF or TEF Canada: which to choose?", "The two tests IRCC accepts, with both CLB tables."),
          ("/en/tcf-canada-results/", "TCF Canada results: timeline and validity", "When results arrive, the two-year rule, and retakes.")],
    sources="""<strong>Scoring rules change.</strong> This article is up to date as of 27 July 2026, except for re-marking,
updated for sessions held from 1 September 2026. It is not immigration advice. Conversion tables, CRS cut-offs and
program requirements change regularly. Always check the current chart on
<a href="https://www.canada.ca/en/immigration-refugees-citizenship.html" rel="noopener">canada.ca</a> before you
register for a test or create your profile.""",
))


# ===========================================================================
# TCF CANADA vs TEF CANADA (from /blog/tcf-ou-tef-canada/, with material from /blog/difference-tcf-tef/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/tcf-ou-tef-canada/", lang="en", variant="en-CA", slug="tcf-vs-tef-canada",
    crumbs=[HOME, TCF], crumb="TCF vs TEF Canada",
    title="TCF vs TEF Canada: which is easier for PR in 2026?",
    desc="TCF vs TEF Canada for PR: same CLB levels, neither is easier. Both official conversion tables, speaking and listening compared, fees, the TEF score trap.",
    h1="TCF or TEF Canada: which one should you take for your application?",
    intro="""<strong>Neither is easier.</strong> Both are accepted by IRCC, lead to the same <strong>CLB</strong> levels
(NCLC in French) and cost the same. <strong>The only rational criterion is your score</strong>: take a practice test
of each and keep the one where you score higher. This article gives you both official conversion tables, the format
differences that favour one profile or another, and the data-entry trap that gets profiles rejected.""",
    facts=["For Express Entry, IRCC accepts only <strong>two</strong> French tests: the TCF Canada and the TEF Canada. Not the DELF, not the DALF.",
           "The scales differ: TCF = listening and reading out of <strong>699</strong>, speaking and writing out of <strong>20</strong>. TEF = <strong>all four tests out of 699</strong>, plus an “old score” column out of 300 / 360 / 450 / 450.",
           '⚠️ With the TEF, enter the <strong><em lang="fr">Équivalence ancien score</em></strong> column, not the 699 column — <strong>whatever the date of your test</strong>.',
           "Valid for <strong>2 years</strong> — required twice: when you create your profile <em>and</em> when you submit your application.",
           "<strong>20 days</strong> between two attempts, for both tests.",
           "Fees found: <strong>€220–245</strong> in Europe, <strong>$400–440</strong> in Canada — and many centres publish no fee at all."],
    toc=[("tables", "The two CLB conversion tables"), ("old-score", "The “old score” column trap"),
         ("format", "Format differences that matter: speaking, listening, writing"),
         ("fees", "Fees, timelines and availability"), ("quebec", "The Quebec case"), ("choose", "How to choose, in practice")],
    body="""
<h2 id="tables">The two CLB conversion tables</h2>
<p>This is the only thing that counts for your application: your raw score means nothing in itself — only the
<strong>CLB level</strong> it produces is used. And each skill is assessed separately: <strong>there is no
compensation</strong>. An excellent listening or reading score won’t make up for weak speaking: your lowest skill caps
your application.</p>
""" + table("TCF Canada → CLB. Listening and reading are scored out of 699, speaking and writing out of 20. Source: IRCC equivalency tables, checked on 27 July 2026.",
            ["CLB", "Listening /699", "Reading /699", "Speaking /20", "Writing /20"],
            [("<strong>10+</strong>", "549–699", "549–699", "16–20", "16–20"), ("<strong>9</strong>", "523–548", "524–548", "14–15", "14–15"),
             ("<strong>8</strong>", "503–522", "499–523", "12–13", "12–13"), ("<strong>7</strong>", "458–502", "453–498", "10–11", "10–11"),
             ("<strong>6</strong>", "398–457", "406–452", "7–9", "7–9"), ("<strong>5</strong>", "369–397", "375–405", "6", "6"),
             ("<strong>4</strong>", "331–368", "342–374", "4–5", "4–5")], wide=False) + "\n" + \
         table('TEF Canada → CLB: the scales IRCC uses in the Express Entry profile — that is, those of the <em lang="fr">Équivalence ancien score</em> column of your results certificate, not the 699 column. Source: IRCC equivalency tables, checked on 27 July 2026.',
            ["CLB", "Reading /300", "Listening /360", "Writing /450", "Speaking /450"],
            [("<strong>10</strong>", "263–300", "316–360", "393–450", "393–450"), ("<strong>9</strong>", "248–262", "298–315", "371–392", "371–392"),
             ("<strong>8</strong>", "233–247", "280–297", "349–370", "349–370"), ("<strong>7</strong>", "207–232", "249–279", "310–348", "310–348"),
             ("<strong>6</strong>", "181–206", "217–248", "271–309", "271–309"), ("<strong>5</strong>", "151–180", "181–216", "226–270", "226–270"),
             ("<strong>4</strong>", "121–150", "145–180", "181–225", "181–225")], wide=False) + """
<p>Notice the difference in structure: in the TCF Canada, <strong>the four tests use only two scales</strong> (699 and
20), and the listening and reading thresholds are slightly offset from each other. The TEF Canada works differently.
Since <strong>1 October 2019</strong>, the TEF results certificate scores <strong>all four tests out of 699</strong> —
that’s the number you’ll see in large print on your results. But next to it, the certificate keeps a second column,
headed “<strong><em lang="fr">Équivalence ancien score</em></strong>” (old-score equivalent), which uses the scales in
force before 30 September 2019: 300 in reading, 360 in listening, 450 for each of writing and speaking. <strong>It is
this second column, and only this one, that IRCC uses</strong> — which is why the table above is not out of 699.</p>
<p>Hence the No. 1 source of error when reading a conversion table picked up online: a TEF score means nothing
until you know <em>which test</em> and <em>which column</em> it comes from. A “350” can be excellent or mediocre
depending on the box it comes from.</p>
<div class="note">
<p><strong>And a mirror-image trap on the TCF Canada side: C1 isn’t CLB 10.</strong> A results certificate showing
“C1” in listening or reading means a score of 500 to 599 on the CEFR scale — but <strong>CLB 10 starts at
549</strong>. A C1 at 510 is therefore only CLB 8. IRCC counts the CLB level, never the letter.</p>
</div>

<h2 id="old-score">The “old score” column trap</h2>
<div class="note">
<p><strong>If you remember only one thing from this article, make it this.</strong> The TEF results certificate has
<em>two</em> score columns: a “Score / 699” column and an “<strong><em lang="fr">Équivalence ancien score</em></strong>”
column. To fill in your Express Entry profile, <strong>IRCC expects the scores from the <em lang="fr">Équivalence
ancien score</em> column</strong>, not those from the 699 column, and says so bluntly: enter only the scores from that
column, or your application may be refused. In other words, the most visible number on your certificate is precisely
the one you must not copy.</p>
</div>
<p><strong>A point about dates, because it’s wrong almost everywhere.</strong> These two columns don’t date from
December 2023: the TEF has scored each test out of 699 since <strong>1 October 2019</strong>. What the reform of
<strong>11 December 2023</strong> changed was something else. It <strong>recalibrated the bands test by test</strong> —
before, the four tests shared the same thresholds; since then, each has its own — and <strong>reduced the number of
questions</strong> in reading and listening, without changing how long they last. The TEF IRN was not affected by this
reform.</p>
<p>This double column also explains why you’ll find two TEF → CLB tables online that seem to contradict each other.
Both are correct: the one out of 699 is published by Le français des affaires, the one out of 300/360/450 is the one
IRCC uses. They describe the same reality in two different units. For your profile, only the second one counts.</p>
<p>Another subtlety, and a counter-intuitive one: the TEF has <strong>three IRCC charts depending on the test
date</strong> (before 30 September 2019; from 1 October 2019 to 10 December 2023; from 11 December 2023), whereas the
TCF Canada has only one. <strong>But for Express Entry, the oldest of the three applies</strong> — the one in the
<em lang="fr">Équivalence ancien score</em> column — <em>whatever date you took the test</em>. So don’t look for the
chart that matches your test date: it’s other programs, such as the Francophone Community Immigration Pilot, that use
the dated charts.</p>

<h2 id="format">Format differences that matter: speaking, listening, writing</h2>
""" + table("Format comparison, immigration versions. Sources: France Éducation international (TCF Canada) and Le français des affaires (TEF Canada), checked in July 2026.",
            ["Test", "TCF Canada", "TEF Canada"],
            [("Listening", "39 multiple-choice questions · 35 min", "40 questions · 40 min"),
             ("Reading", "39 multiple-choice questions · 60 min", "40 questions · 1 hour"),
             ("Writing", "3 tasks · 60 min · ~300 to 450 words", "2 sections · 1 hour · ~280 words"),
             ("Speaking", "3 tasks · 12 min, face to face", "2 sections · 15 min, face to face"),
             ("Total time", "2 hours 47 minutes", "2 hours 55 minutes"),
             ("Format", "paper-based <em>or</em> computer-based, depending on the centre", "computer-based (speaking face to face)"),
             ("Speaking and writing scored", "out of 20", "out of 699 <em>(450 as “old score”)</em>")], wide=False) + """
<p>Four format points have real consequences.</p>
<p><strong>How finely speaking and writing are scored.</strong> In the TCF Canada, speaking and writing are scored out
of 20: going from 11 to 12 moves you from CLB 7 to CLB 8. A single point changes everything. In the TEF, they are
scored out of 699 — or 450 in the “old score” column — so on a much finer, less abrupt scale: there, you need to gain
around twenty points to change CLB level. If you are a borderline candidate, this granularity can work in your favour —
or cost you dearly.</p>
<p><strong>How much you write.</strong> The TCF Canada asks for about 300 to 450 words spread over <em>three</em> tasks
in one hour; the TEF Canada, about 280 words over <em>two</em> sections. If you write slowly, the TEF is less
stressful. If you are more comfortable with short, varied formats, the TCF will suit you better.</p>
<p><strong>How the speaking test is split.</strong> Both tests have you speak <em>face to face with an examiner</em> —
no difference there. What differs is the structure: the TCF runs <strong>three short tasks in 12 minutes</strong>, with
two minutes of preparation for the second task only; the TEF has <strong>two longer sections</strong> — getting
information, then arguing to convince — each with its own preparation time. If you are stronger at building a developed
argument than at quick back-and-forth, the TEF’s structure works for you.</p>
<p><strong>You hear each recording once.</strong> In the TCF Canada, <em>each recording is played only once</em>, and
the question is asked only after you’ve listened. It’s the test that surprises poorly prepared candidates the most, and
a real argument for practising in real conditions before test day. The TEF works the same way: each audio is played
only once and you answer as you go, with no going back — unlike the DELF, where documents at levels A1 to B1 are played
twice.</p>
<div class="note">
<p><strong>Watch out for a “below A1” (<em lang="fr">A1 non atteint</em>) result in TCF Canada writing.</strong> Your
paper can be cancelled if your handwriting is illegible (paper-based test), if the required word count isn’t met on a
task, if your answer is off topic, or if a task isn’t done. These aren’t point penalties: it’s a floor that sinks the
whole writing test.</p>
</div>

<h2 id="fees">Fees, timelines and availability</h2>
<p><strong>Neither France Éducation international nor Le français des affaires publishes a national fee.</strong> Both
explicitly refer you to the approved centre, which sets its own price. In France, among the centres checked in July
2026: TCF Canada at €220 (Alliance Française de Lyon) and €200 (Alliance Française de Montpellier); TEF Canada at €245
(ALIP, Paris). In Canada, published fees are rare and noticeably higher: the full TCF Canada costs <strong>$400</strong>
at the Alliance Française d’Edmonton and <strong>$440</strong> at the École internationale de français at UQTR, as
checked on 30 July 2026.</p>
<div class="note">
<p><strong>Many centres publish nothing at all</strong> — the Alliance Française de Montréal, for example, posts no
TCF fee: registration is online, subject to availability, and the only amount shown is a $75 cancellation fee.
Comparison sites that attribute precise fees to these centres cite no source, and often confuse the TCF Québec with the
TCF Canada. We also found <strong>no verifiable Canadian fee for the TEF Canada</strong>: ask the centre.</p>
</div>
<p>In other words, <strong>price doesn’t decide between the two tests</strong>: at comparable centres, they cost about
the same. Be wary of any website announcing an “official” fee.</p>
<p>As for networks, the TEF claims 500 centres in more than 110 countries, the TCF 768 centres worldwide. TCF Canada
results are sent within 15 business days of the session materials being received; TEF results arrive in about 1 to 2
weeks. For the TEF, note that the registration conditions of Le français des affaires <strong>start the two-year
validity from the date the results certificate is issued</strong>, not the test date — but its TEF presentation page
speaks of two years “from the test date”. The gap can reach several weeks, which can matter if your application drags on: go by
the less favourable date and have your centre confirm.</p>
<p>Finally, a constraint specific to the TEF: <strong>all the tests must be taken on the same day</strong> for the
results certificate to be recognized by the Canadian authorities.</p>
<p>For the TCF Canada, our guides to where to take it in France (€195 to €285, one session a month per centre) and
<a href="/en/tcf-canada-test-centres/">in Canada</a> (47 centres, $390 to $440, sessions full within minutes) list the
centres one by one — as do our guides for Algeria, Morocco and Tunisia; for the TEF Canada, the directory of Le
français des affaires remains the reference.</p>

<h2 id="quebec">The Quebec case</h2>
<p>If your plans are aimed at Quebec rather than at the federal level, everything changes — in your favour. Quebec’s
immigration ministry (MIFI) accepts <strong>eight</strong> tests and diplomas: TCF-Québec, TCF Canada, TCF, DALF and
DELF from France Éducation international; TEFAQ, TEF Canada and TEF from the CCI Paris Île-de-France. Results must be
two years old or less.</p>
<p>Above all, the <strong>TCF Québec and the TEFAQ are modular</strong>: you choose to take one, two, three or four
tests. And stream 2 of the PSTQ (Quebec’s skilled worker selection program) and the requirement for an accompanying
spouse only cover oral skills. <strong>So you can take just the two oral tests</strong> — less preparation, less risk,
often cheaper. At UQTR, for example, the two oral tests of the TCF Québec cost $230, against $440 for a full TCF Canada
at the same centre (checked on 30 July 2026).</p>
<p>PSTQ thresholds, on the Quebec scale (not to be confused with CLB): stream 1, oral French at level 7 or higher
<em>and</em> written French at level 5 or higher. The Quebec table is much coarser than the CLB: in the TEF, TEFAQ and
TEF Canada, as in TCF listening and reading, the 400–499 band corresponds to levels 7–8 (B2). There is also
<strong>no English requirement in the PSTQ</strong>.</p>

<h2 id="choose">How to choose, in practice</h2>
<ol>
<li><strong>First, check your process.</strong> Federal economic immigration: TCF Canada or TEF Canada, full stop.
Canadian citizenship: IRCC’s eligibility questionnaire, checked on 8 October 2026, names the TEF Canada and the TCF
Canada among French tests (older guides listed more: DALF, DELF, TCFQ, TEFAQ, TEF IRN), and the level required is only
CLB 4, in listening and speaking only, for applicants aged 18 to 54 — the TEF Canada can then be
taken as those two tests alone. Quebec: eight tests accepted, and the modular versions open doors for you.</li>
<li><strong>Take a full practice test of each</strong>, timed, in real conditions. It’s the only decisive test.</li>
<li><strong>Compare the CLB levels you get, not the raw scores.</strong> They can’t be compared between the two
tests.</li>
<li><strong>Look at your weakest skill</strong> in each simulation: it decides, not your average.</li>
<li><strong>Pick the one where your weak spot does best.</strong> That’s it.</li>
</ol>
<p>To go further on thresholds and points, see our <a href="/en/tcf-canada/">TCF Canada</a> guide, our
<a href="/en/tef-canada/">TEF Canada and TEFAQ</a> page, and our <a href="/en/tcf-canada-practice-test/">practice
tests</a>. If your plans are in France rather than Canada, other tests apply: B2 for French citizenship, B1 for the
resident card.</p>
""",
    cta_h2="Take a practice test of each before paying $440",
    cta_p="""Timed mock exams in the exact TCF Canada and TEF Canada formats, an instant CLB conversion for each test, and AI
feedback on writing and speaking — in the “TCF DELF TEF: Tests 2026” app.""",
    faq=[("TCF or TEF Canada: which is easier?", "Neither is inherently easier: no official source says one is, and no pass rates are published. Both lead to the same CLB scale. The differences that matter are in the format: the TCF Canada scores speaking and writing out of 20, so a single point can change your CLB level, whereas the TEF scores them out of 699 (450 in the “old score” column), which is much more granular. The TEF asks for about 280 words over 2 writing tasks, the TCF about 300 to 450 words over 3 tasks. Take a practice test of each and keep the one where you score higher."),
         ("Which French tests does IRCC accept for Express Entry and PR?", "Only two: the TEF Canada and the TCF Canada. Neither the DELF, the DALF nor the TEF tout public is accepted for economic immigration. For a Canadian citizenship application, IRCC’s eligibility questionnaire, checked on 8 October 2026, names the TEF Canada and the TCF Canada; older guides listed more (DALF, DELF, TCFQ, TEFAQ, TEF IRN), so check IRCC’s list when you apply."),
         ("Which TEF scores do I enter in my Express Entry profile?", "Only the scores in the “Équivalence ancien score” column of your results certificate, whatever the date of your test. The TEF certificate also has a column out of 699 — since 1 October 2019, not since the December 2023 reform as is often said — but those aren’t the scores IRCC expects. It is the leading cause of data-entry errors in Express Entry profiles."),
         ("How do the TCF and TEF speaking tests differ?", "Both are face to face with an examiner. The TCF Canada runs three short tasks in 12 minutes, with two minutes of preparation for the second task only; the TEF Canada has two longer sections — getting information, then arguing to convince — each with its own preparation time. If you build a developed argument better than you handle quick exchanges, the TEF’s structure suits you."),
         ("How many times is the listening played in the TCF and the TEF?", "Once, in both tests. France Éducation international states that each recording is played only once; Le français des affaires, that each audio is played only once and that you answer as you go, with no going back. It’s a major difference from the DELF, where documents at levels A1 to B1 are played twice."),
         ("How long are TCF and TEF Canada results valid?", "Two years for both tests. But IRCC’s rule is stricter than it looks: your results must be less than two years old when you fill in your Express Entry profile AND when you submit your application for permanent residence. For the TEF, the registration conditions of Le français des affaires count validity from the date the certificate is issued, not the test date — though its presentation page says “from the test date”: go by the less favourable date."),
         ("How long do you have to wait to retake the TCF or TEF Canada?", "Twenty days for both. The number of attempts is unlimited for the TCF Canada, with a compulsory 20-day wait between two sessions. The TEF imposes the same 20-day wait between two attempts at the same test, all versions combined. The rumour of a 30-day wait for the TEF is false."),
         ("How much do the TCF Canada and the TEF Canada cost?", "There is no national fee: both organizations let each approved centre set its price. Among the centres checked in July 2026, we found about €220 to €245 in Europe, and $400 to $440 in Canada for a full TCF Canada. Beware: many centres — including the Alliance Française de Montréal — publish no fee, and the figures comparison sites attribute to them are unsourced. In any case, price shouldn’t be your criterion for choosing between the two tests.")],
    also=[("/en/tcf-canada-clb-7/", "TCF Canada CLB 7: the exact scores", "458 in listening, 453 in reading — and why B2 isn’t always enough."),
          ("/en/tef-canada/", "TEF Canada", "The other French test IRCC accepts for Express Entry."),
          ("/en/tcf-canada-practice-test/", "Free TCF Canada practice test", "Check your level in the real format before you book.")],
    sources="""<strong>Scoring rules change.</strong> This article is up to date as of 30 July 2026 and is not immigration
advice. Conversion tables, thresholds and programs are changed regularly by IRCC and by MIFI. Always check the current
chart on <a href="https://www.canada.ca/en/immigration-refugees-citizenship.html" rel="noopener">canada.ca</a> and, for
Quebec, on <a href="https://www.quebec.ca/immigration" rel="noopener">quebec.ca</a> before you register for a test or
create your profile.""",
))


# ===========================================================================
# TCF CANADA — test dates 2026 (from /blog/tcf-canada-dates-2026/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/tcf-canada-dates-2026/", lang="en", variant="en-CA", slug="tcf-canada-test-dates-2026",
    crumbs=[HOME, TCF], crumb="Test dates 2026", inline_cta=False,
    title="TCF Canada test dates 2026: sessions, centre by centre",
    desc="No national calendar: TCF Canada test dates to December 2026, as listed by the centres — Paris, Lyon, Casablanca, Rabat, Tunis, Toronto, Vancouver.",
    h1="TCF Canada test dates in 2026: the sessions we found, centre by centre",
    intro="""There is <strong>no national TCF Canada calendar</strong>: each approved centre sets its own sessions and
publishes them — or not — on its website. So on 17 September 2026, we read the registration pages of the main centres
in France, Canada, Algeria, Morocco and Tunisia. What we found: sessions <strong>three times a week in
Casablanca</strong>, monthly in Lyon, quarterly and snapped up in Toronto, “SOLD OUT” in Vancouver. The dates, what
they cost, and the rule for not missing the next one.""",
    facts=["<strong>No national calendar</strong>: dates and registration are handled by each centre — never by France Éducation international.",
           "<strong>France</strong>: ACTE Paris 4 Nov and 2 Dec; ACCORD Paris 23 Sept and 28 Oct; Alliance française de Lyon 21 Oct, 25 Nov, 16 Dec; Montpellier 23 Sept and 13 Nov 2026.",
           "<strong>North Africa</strong>: Casablanca on Tuesdays, Thursdays and Saturdays until December; Rabat 9 sessions from 25 Sept to 24 Nov; Tunis 24–25 Sept, 22–23 Oct, 26–27 Nov, 16 and 18 Dec; Algeria every month.",
           "<strong>Canada</strong>: Toronto opens registration a month before each quarter (next opening on 1 December 2026, for January to March 2027); Vancouver showed every session full.",
           "Between two attempts: <strong>20 days</strong> in France and Canada, 26 in Algeria, 30 in Tunisia; results within 2 to 5 weeks, depending on the country."],
    toc=[("rule", "The rule: each centre sets its own dates"), ("france", "France: the sessions we found"),
         ("north-africa", "Morocco, Tunisia, Algeria: the sessions we found"),
         ("canada", "Canada: registration openings rather than dates"),
         ("plan", "Planning your date: deadlines, results, second chances")],
    body="""
<div class="stats">
<div class="stat"><b>0</b><span>national calendar</span><em>each centre sets its dates</em></div>
<div class="stat"><b>3/week</b><span>in Casablanca</span><em>Tuesday, Thursday, Saturday</em></div>
<div class="stat"><b>1/month</b><span>in Lyon</span><em>21 Oct, 25 Nov, 16 Dec</em></div>
<div class="stat"><b>20 days</b><span>between two attempts</span><em>26 in Algeria, 30 in Tunisia</em></div>
</div>

<h2 id="rule">The rule: each centre sets its own dates</h2>
<p>The TCF Canada is designed by France Éducation international, but <strong>FEI doesn’t run any sessions</strong>: it
approves centres, which choose their dates, their format (paper or computer), their fee and their registration
deadline. Two consequences. First, the only reliable source is the centre’s registration page — that’s what we read on
17 September 2026, and that’s what counts on the day you pay. Second, two centres in the same city can offer completely
unrelated dates: in Paris, ACCORD had a session on 23 September, while ACTE’s next one was on 4 November.</p>
<p>What the dates have in common, on the other hand, comes from FEI’s rules: a minimum of <strong>20 days between two
attempts</strong> (26 in Algeria, 30 in Tunisia, set by the local Institut français), a results certificate
<strong>valid for two years</strong>, and — for sessions held since 1 September 2026 — <strong>no re-marking</strong>:
the only way to improve a score is to retake the test — which means finding another date.</p>

<h2 id="france">France: the sessions we found</h2>
<p>In France, the TCF Canada is held <strong>monthly or twice a month</strong> at the centres that offer it — far less
often than the TCF IRN, which runs almost weekly in Paris. What the websites showed on 17 September 2026:</p>
""" + table("TCF Canada sessions shown by French centres on 17 September 2026. Dates marked “full” on the website are not included.",
            ["Centre", "Dates found", "Fee", "Registration"],
            [("<strong>ACTE</strong>, Paris (10th arrondissement)", "4 November, 2 December 2026 (paper-based)", "€195", "Online; results in “at least 3 weeks”"),
             ("<strong>ACCORD</strong>, Paris (15th arrondissement)", "23 September, 28 October 2026 (computer-based)", "€220", "Closes 5 days before"),
             ("<strong>Alliance française de Lyon</strong>", "21 October, 25 November, 16 December 2026 — 10 and 23 September full", "€220", "Closes 48 hours before; results in 2–3 weeks"),
             ("<strong>Alliance française de Montpellier</strong>", "23 September (deadline 13 Sept), 13 November 2026 (deadline 3 Nov), computer-based", "€200", "Ten days before; results within 2 weeks"),
             ("<strong>Alliance française Aix-Marseille</strong>", "Dates on the centre’s page; computer-based only", "€60 per test", "Two weeks before; results in 15 days"),
             ("<strong>KLF</strong> (Lyon, Montpellier, Bordeaux, Toulouse, Annecy)", "Online booking by city", "no data", "Results in 10 days to 3 weeks"),
             ("<strong>CLPS</strong>, Rennes and Brest", "Online registration form", "€285", "On clps.net")]) + """
<p>Our city pages, in French, detail each centre with its contacts — Paris, Lyon, Montpellier, Marseille, Bordeaux,
Toulouse, Nantes, Rennes — and our guide to where to take the TCF Canada in France compares fees.</p>

<h2 id="north-africa">Morocco, Tunisia, Algeria: the sessions we found</h2>
<p>It is in North Africa that the TCF Canada is most frequent — and best advertised. In <strong>Morocco</strong>, each
Institut français publishes its sessions with an online cart: on 17 September, Casablanca listed sessions on
<strong>Tuesdays, Thursdays and Saturdays</strong>, two slots a day, from 26 September to December 2026 (three already
full); Rabat <strong>nine sessions</strong>, all open, from 25 September to 24 November; Marrakech on 20 October,
Tangier on 15 October, Béni Mellal on 24 October and 14 November — at <strong>2,900 dirhams</strong> everywhere.</p>
<p>In <strong>Tunisia</strong>, the Institut français publishes a calendar by hub, in two stages: an online appointment
window, then registration in person. In Tunis in 2026: <strong>24–25 September</strong> (appointments from 24 to 30
August), <strong>22–23 October</strong> (14–20 September), <strong>26–27 November</strong> (26–31 October) and
<strong>16 and 18 December</strong> (9–15 November), at 880 dinars; Sousse, Sfax and El Mourouj have one session a
month.</p>
<p>In <strong>Algeria</strong>, the Institut français doesn’t publish dates on its website: “TCF sessions are open every
month at the five branches” — Algiers, Oran, Constantine, Annaba, Tlemcen — and the actual calendar appears on the IFAL
platform (VFS Global) when you register, with the fee. Allow <strong>26 days</strong> between two registrations.</p>
""" + table("Sessions found in North Africa on 17 September 2026, on the websites of the Instituts français.",
            ["Centre", "Dates found", "Fee", "Registration"],
            [("<strong>Casablanca</strong>", "Tuesdays, Thursdays, Saturdays (8:30 am and 10 am), from 26 Sept to Dec 2026", "2,900 MAD", "Online cart, if-maroc.org/casablanca"),
             ("<strong>Rabat</strong>", "9 sessions from 25 Sept to 24 Nov 2026", "2,900 MAD", "Online cart"),
             ("<strong>Marrakech · Tangier · Béni Mellal</strong>", "20 Oct · 15 Oct · 24 Oct and 14 Nov 2026", "2,900 MAD", "Online cart"),
             ("<strong>Tunis</strong> (IFT)", "24–25 Sept, 22–23 Oct, 26–27 Nov, 16 and 18 Dec 2026", "880 TND", "Online appointment 3–4 weeks before, then in person"),
             ("<strong>Sousse · Sfax · El Mourouj</strong>", "One session a month (calendar by hub)", "880 TND", "Same"),
             ("<strong>Algiers, Oran, Constantine, Annaba, Tlemcen</strong>", "“Every month”; dates on the platform", "not published", "IFAL (VFS), 26 days between two registrations")]) + """
<p>Our city pages, in French: Casablanca, Rabat, Marrakech, Tangier, Fez, Agadir, Tunis, Sousse, Sfax, Algiers, Oran,
Constantine.</p>

<h2 id="canada">Canada: registration openings rather than dates</h2>
<p>In Canada, the problem isn’t finding a date but a <strong>seat</strong>. The Alliance française de Toronto runs
<strong>quarterly</strong> sessions and opens registration <strong>one month before each quarter, at 10 am</strong>:
on 17 September, its website announced openings on <strong>1 December 2026</strong> (sessions from January to March
2027), then on 2 March, 20 May and 17 August 2027. “If a session is not listed, it is full”; there is no waitlist. In
Vancouver, the Alliance française Canada Pacific showed <strong>every session “SOLD OUT”</strong> ($390) and advises
logging in the moment registration opens, passport in hand, in a single tab. In Montreal, the Alliance Française
registers candidates “subject to available seats”, without publishing a fee.</p>
<p>The dates themselves are on each centre’s page: <a href="/en/tcf-canada-montreal/">Montreal</a> (seven centres),
<a href="/en/tcf-canada-toronto/">Toronto</a>, <a href="/en/tcf-canada-quebec-city/">Quebec City</a>,
<a href="/en/tcf-canada-ottawa/">Ottawa</a>, <a href="/en/tcf-canada-vancouver/">Vancouver</a> — and our guide to
<a href="/en/tcf-canada-test-centres/">TCF Canada test centres in Canada</a> explains how to get a seat.</p>

<h2 id="plan">Planning your date: deadlines, results, second chances</h2>
<p>Three time spans to add up before you choose a session. <strong>Registration</strong> closes from 48 hours (Lyon) to
two weeks (Marseille) before the test in France, a month before in Canada; in North Africa, as long as seats remain.
<strong>Results</strong> arrive within two weeks in Montpellier, two to three in Lyon and Ottawa, three to four in
Vancouver, <strong>five weeks</strong> in Tunisia. <strong>A second attempt</strong> requires a 20-day gap in France and
Canada, 26 in Algeria, 30 in Tunisia — and with no re-marking since September 2026, it’s the only recourse.</p>
<p>If your application has a deadline — an Express Entry profile to submit, an invitation to respond to — allow
<strong>at least two months</strong> between the first session and a usable result after a possible second attempt, and
aim for the first available date rather than the most convenient one: in Toronto as in Casablanca, sessions fill up in
that order.</p>
""",
    cta_h2="The centre sets the date; the score is up to you",
    cta_p="""A session is paid in full and can only be retaken after twenty days. The mock exams in the “TCF DELF TEF: Tests
2026” app follow the official TCF Canada format — four tests, scored out of 699 and out of 20, with CLB (NCLC)
conversion — with AI feedback on writing and speaking.""",
    faq=[("When is the next TCF Canada test date?", "It depends on the centre: on 17 September 2026, ACCORD in Paris had a session on 23 September, the Alliance française de Montpellier on 23 September then 13 November, ACTE in Paris on 4 November, the Alliance française de Lyon on 21 October; Casablanca offered three a week and Tunis 24–25 September. There is no national calendar: the centre’s registration page is the reference."),
         ("Is there an official TCF Canada test date calendar?", "No. France Éducation international approves centres but runs no sessions: each centre publishes its own dates, often one or two months ahead, and updates them as registrations come in. FEI’s lists only give the centres’ contact details."),
         ("How many TCF Canada sessions are there per month?", "From three a week in Casablanca to one a month in Lyon or Sousse, and one a quarter in Toronto. In France, the TCF Canada is much less frequent than the TCF IRN, which is held almost every week in Paris."),
         ("What if all TCF Canada sessions are full?", "Create your account in advance and log in the moment registration opens — in Toronto, a month before the quarter, at 10 am; in Vancouver, with your passport ready and a single tab open. With no waitlist, check back regularly: seats do free up. In France, try another centre — centres in the same city don’t have the same dates."),
         ("How long between two TCF Canada attempts?", "At least twenty days in France and Canada (an FEI rule applied by every centre), 26 days in Algeria and 30 days in Tunisia, set by the Instituts français. For sessions held since 1 September 2026, no re-marking is possible: retaking the test is the only recourse.")],
    also=[("/en/tcf-canada-test-centres/", "TCF Canada test centres in Canada", "The 47 approved centres, $390 to $440, and how to get a seat."),
          ("/en/tcf-canada-results/", "TCF Canada results: timeline and validity", "How long results take, the two-year rule, and retakes."),
          ("/en/", "All locations", "Every country and city page in English.")],
    sources="""<strong>Sources.</strong> The TCF Canada pages of the centres cited — ACTE, ACCORD (examensparis.fr), the
Alliances françaises of Lyon, Montpellier and Aix-Marseille, KLF, CLPS, the Alliance française de Toronto, the
Alliance française Canada Pacific, the Alliance Française de Montréal, and the Instituts français of Casablanca, Rabat,
Marrakech, Tangier, Tunis (2026 calendar) and Algeria — checked on 17 September 2026; the TCF rules (France Éducation
international) for the 20-day wait and the two-year validity; FEI’s note on the end of re-marking from 1 September
2026. Dates and fees change without notice: check them on the centre’s website before you pay.""",
))


# ===========================================================================
# TCF CANADA — results: timeline, validity, re-marking, retakes
# (from /blog/validite-attestation-tcf-tef/ + the retake rules of /blog/repasser-tcf-tef/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/validite-attestation-tcf-tef/", lang="en", variant="en-CA", slug="tcf-canada-results",
    crumbs=[HOME, TCF], crumb="Results and validity",
    title="TCF Canada results: how long they take and stay valid",
    desc="TCF Canada results take 2 to 5 weeks and stay valid for 2 years — which IRCC checks twice. The TEF date trap, the end of re-marking, and retake rules.",
    h1="TCF Canada results: when they arrive, how long they’re valid, and retaking the test",
    intro="""TCF Canada results are published within <strong>15 business days</strong> of France Éducation international
receiving the session materials — two to five weeks in practice, depending on the country — and, like TEF results,
they are valid for <strong>two years</strong>. The question that really matters, and that almost nobody answers
correctly, is <strong>from what date</strong> those two years run — for the TEF, the official pages don’t agree — and
an IRCC rule catches long Canadian applications out. If your score falls short, re-marking is gone for sessions held
since 1 September 2026: retaking is the only way, and it has its own rules.""",
    facts=["Results: within <strong>15 business days</strong> of FEI receiving the session materials; <strong>2 to 5 weeks</strong> in practice, depending on the country.",
           "Valid for <strong>2 years</strong>, TCF and TEF alike. DELF and DALF diplomas, on the other hand, <strong>don’t expire</strong>.",
           "TCF: from the <strong>date the results certificate is issued</strong>.",
           "⚠️ TEF: the official pages say <strong>“date of issue”</strong> <em>or</em> <strong>“test date”</strong>, depending on which one you read.",
           "⚠️ <strong>IRCC</strong>: results less than 2 years old when you create your Express Entry profile <strong>and</strong> when you submit your application.",
           "⚠️ <strong>Quebec</strong>: a DELF or DALF must be less than 2 years old — “for life” doesn’t apply.",
           "Re-marking: <strong>none</strong> for sessions held since 1 September 2026. Retakes: <strong>unlimited</strong>, always the full TCF Canada.",
           "If in doubt, go by <strong>the least favourable date</strong> for you."],
    toc=[("timeline", "When TCF Canada results arrive"), ("validity", "Validity: two years"),
         ("tef", "The TEF: two start dates, depending on the page"), ("ircc", "IRCC’s rule is stricter than it looks"),
         ("diplomas", "DELF and DALF: valid for life, except in Quebec"), ("re-marking", "Re-marking: over since September 2026"),
         ("wait", "How long to wait before retaking"), ("how-many-times", "How many times can you take the TCF Canada?"),
         ("plan", "How to plan without getting caught")],
    body="""
<h2 id="timeline">When TCF Canada results arrive</h2>
<p>Results are published within <strong>15 business days</strong> of France Éducation international receiving the
session materials. In practice, the timeline depends on where you take the test: within two weeks in Montpellier, two to
three weeks in Lyon and Ottawa, three to four in Vancouver, <strong>five weeks</strong> in Tunisia. TEF results arrive
in about 1 to 2 weeks.</p>
<p>Your results certificate gives a score out of 699 for listening and reading and a mark out of 20 for speaking and
writing, each with its CEFR level — but <strong>no CLB level</strong> (NCLC in French): the conversion is up to you,
using IRCC’s chart. And a “B2” isn’t always worth CLB 7.</p>

<h2 id="validity">Validity: two years</h2>
<p>The TCF and the TEF are <strong>placement tests</strong>, not diplomas: they capture your level at a given moment,
and that snapshot is considered valid for <strong>two years</strong>. After that, the results certificate proves
nothing, however good your score.</p>
<p>For the <strong>TCF</strong>, the starting point is clear: the <strong>date the results certificate is
issued</strong>. For the TEF, this is where it gets complicated.</p>

<h2 id="tef">The TEF: two start dates, depending on the page</h2>
<div class="note">
<p><strong>On this precise point, the pages of Le français des affaires don’t say the same thing.</strong> Its
<em>registration conditions</em> start validity “from the date of issue” of the results certificate, while its TEF
<em>presentation page</em> speaks of two years “from the test date”.</p>
</div>
<p>The gap between the two can reach <strong>several weeks</strong> — the time between test day and the document being
issued. Most of the time, it makes no difference. But if your application is submitted just before the deadline, it’s
exactly the kind of detail that decides whether it is accepted.</p>
<p><strong>What to do</strong>: go by the <strong>least favourable date for you</strong> — the test date, which is the
earlier one — and have your centre confirm if the deadline is tight. Better to retake a test a month too early than to
see an application rejected because of a certificate that expired ten days before.</p>

<h2 id="ircc">IRCC’s rule is stricter than it looks</h2>
<p>For a Canadian immigration application, the two-year rule applies not once but <strong>twice</strong>. Your results
must be less than two years old:</p>
<ol>
<li><strong>when you create your Express Entry profile</strong>, <em>and</em></li>
<li><strong>when you submit your application for permanent residence</strong>.</li>
</ol>
<div class="note">
<p><strong>The long-application trap.</strong> Many months can pass between creating a profile and being invited to
apply. A test taken too early in the process <strong>can expire between the two steps</strong> — and then it has to be
retaken in full, since there is no partial retake for the <a href="/en/tcf-canada/">TCF Canada</a> or the
<a href="/en/tef-canada/">TEF Canada</a>.</p>
</div>
<p>The practical consequence is counter-intuitive: <strong>taking your test as early as possible isn’t the right
strategy</strong> for a Canadian application. Better to take it when your profile is ready to be created, so you have
the widest possible window before you submit your application for permanent residence.</p>

<h2 id="diplomas">DELF and DALF: valid for life, except in Quebec</h2>
<p>Here is the nuance that almost no comparison picks up. For Quebec programs, results must be <strong>two years old
or less on the date of your application for permanent selection</strong>. Nothing unusual so far.</p>
<p>But Quebec also accepts <strong>DELF and DALF diplomas</strong> in place of the TCF Québec — and applies the same
condition to them: a minimum mark in listening and speaking, <em>and</em> a validity of <strong>less than two
years</strong>.</p>
<p>In other words: in Quebec, <strong>the diploma’s advantage disappears</strong>. A DELF B2 you passed five years ago
exempts you from nothing, whereas it would remain fully valid for an application in France. It’s an important exception
to the general “diploma for life” rule.</p>
<p>For procedures in France, the logic is reversed and works in favour of diplomas:</p>
""" + table("How long each proof of French lasts, by type.", ["Proof", "Validity"],
            [("TCF IRN or TEF IRN results certificate", "<strong>2 years</strong>"),
             ("DELF or DALF diploma", "<strong>no expiry</strong>"),
             ("French school diploma (brevet, CAP…)", "<strong>no expiry</strong>")], wide=False) + """
<p>That’s decisive when an administrative process stretches out. A candidate who gets a French resident card with a
DELF B1, then applies for French citizenship five years later, doesn’t have to worry about their first proof expiring —
they will, however, have to prove the B2 required since 2026, which is another matter.</p>

<h2 id="re-marking">Re-marking: over since September 2026</h2>
<p>For sessions held since <strong>1 September 2026</strong>, re-marking is <strong>no longer possible</strong>: the
only way to improve a score is to retake the test — which means finding another date.</p>
<p>For earlier sessions, the rule as of 7 August 2026 was this — an avenue of appeal that didn’t involve retaking the
test, useful to know about and risky to use without thinking:</p>
<ul>
<li>it covered only the <strong>speaking and writing tests</strong> — never the multiple-choice tests, which are marked
automatically;</li>
<li>it had to be requested <strong>within a month</strong> of the results certificates being sent to the centre;</li>
<li><strong>the new mark replaced the old one, even if it was lower.</strong></li>
</ul>
<div class="note">
<p><strong>A gamble, not a free appeal.</strong> You weren’t asking for a second opinion: you were asking for a
<em>new</em> mark that would overwrite the previous one — only worth it with a serious reason to think your work had
been underrated, such as a clear gap with your practice results marked against the same criteria. A mere “I was hoping
for better” wasn’t one.</p>
</div>

<h2 id="wait">How long to wait before retaking</h2>
<p>On the <strong>TEF</strong> side, the rule is simple and documented without ambiguity: <strong>twenty days</strong>
between two attempts at the same test, all versions combined. The rumour of a 30-day wait for the TEF, which you’ll
often read on forums, is <strong>false</strong>: it comes from a confusion with some TCF sheets.</p>
<p>On the <strong>TCF</strong> side, it’s more complicated — and you need to know it before you book a flight or time
an application.</p>
<div class="note">
<p><strong>Both figures come from France Éducation international itself.</strong> Its test pages state <strong>20
days</strong> for the TCF tout public, the TCF Canada and the TCF Québec. Several of its PDF sheets and its candidate
handbook state <strong>30 days</strong>. And for the TCF IRN, the page and the sheet, published almost at the same time,
contradict each other.</p>
</div>
<p>This isn’t an expert quibble: two weeks’ difference can make you miss an application deadline. What to do is simple,
and it’s worth more than any figure you read online:</p>
<ul>
<li><strong>Never time a second attempt to the week</strong> on the strength of a waiting period found online — ours
included.</li>
<li><strong>Have your centre confirm the waiting period</strong> when you plan to retake. It handles registrations and
will apply the rule in force.</li>
<li><strong>Allow for the least favourable margin</strong> — 30 days — if your application has a deadline.</li>
</ul>

<h2 id="how-many-times">How many times can you take the TCF Canada?</h2>
<p><strong>As many times as you like.</strong> Neither the TCF nor the TEF limits the number of attempts — the only
constraints are the waiting period between two attempts, and the fact that each attempt is paid at full price.</p>
<p>Whether you can retake just one test depends entirely on the version — a criterion people overlook when they first
register:</p>
""" + table("Partial retakes, by version.", ["Version", "Can you retake just one test?"],
            [('<a href="/en/tcf-canada/">TCF Canada</a>', "<strong>No</strong> — all 4 tests, every time"),
             ('<a href="/en/tef-canada/">TEF Canada</a>', "<strong>No</strong> for immigration <em>(listening + speaking only for citizenship)</em>"),
             ("TCF IRN · TEF IRN", "<strong>No</strong> — officially “indivisible” tests"),
             ("TCF Québec · TEFAQ", "<strong>Yes</strong> — modular versions, 1 to 4 tests of your choice")], wide=False) + """
<p>The financial consequence is direct. On a non-modular version, a single disappointing test means paying for and
retaking the whole thing. With the TCF Québec or the TEFAQ, you re-register only for the test you want to improve — a
considerable advantage, and one of the reasons to prefer these versions when your process allows it.</p>
<div class="note">
<p><strong>Don’t confuse modularity with retakes.</strong> The TEF Canada lets you register for listening and speaking
only — but only if your process is an <em>application for Canadian citizenship</em>. For economic immigration, all four
tests remain compulsory.</p>
</div>
<p>That’s where the real cost lies. A TCF Canada costs €195 to €285 in France and $400 to $440 in Canada; a TCF IRN,
€135 to €220. Retaking a test three times when you weren’t ready for it costs more than any preparation. For fees, see
<a href="/en/tcf-canada/fees-registration/">TCF Canada fees and registration</a>.</p>

<h2 id="plan">How to plan without getting caught</h2>
<ul>
<li><strong>Count backwards from your deadline.</strong> Start from the likely date you’ll submit your application and
subtract two years: that’s the earliest date your test can have been taken.</li>
<li><strong>For a Canadian application, count two deadlines</strong>, not one: creating the profile <em>and</em>
submitting the application for permanent residence.</li>
<li><strong>Go by the test date, not the date of issue</strong>, when the source is ambiguous. You lose a few weeks of
theoretical validity and gain certainty.</li>
<li><strong>If your process will take a long time, prefer a diploma</strong> — except for a Quebec project, where the
freshness condition applies to diplomas too.</li>
<li><strong>Don’t take your test “just to be safe”.</strong> A test taken two years too early is a test you pay for
again. Check your level instead with a <a href="/en/tcf-canada-practice-test/">practice test in the official
format</a> — which doesn’t expire.</li>
</ul>
<p>And if you have to retake, remember that retaking the same test in the same conditions usually gives the same
result. Three steps really change the outcome:</p>
<ol>
<li><strong>Identify the test that capped your application</strong>, not the one that disappointed you. In the TCF and
the TEF, there is no compensation: your lowest score is what counts. If you missed your target by one point in writing,
everything else is noise.</li>
<li><strong>Work on that test specifically</strong>, not on French in general. Between two attempts twenty to thirty
days apart, only targeted work can produce a measurable gap.</li>
<li><strong>Check the gain before you pay</strong>, with a practice test marked in the official format and scoring. If
your simulated score hasn’t moved, your real score won’t either.</li>
</ol>
<p>For speaking and writing, the blind spot is structural: you can’t assess yourself against criteria you don’t know.
Knowing whether you’ve gone from 9 to 11 out of 20 — often, from one level to the next — takes marking against the
official grids.</p>
""",
    cta_h2="An expired test is retaken in full",
    cta_p="""There is no partial retake for the TCF Canada or the IRN versions: an expired results certificate means four
tests to take and pay for again. Mock exams in the official format, a score for each test, and AI feedback on writing
and speaking — so you take the real test only once, at the right time. In the “TCF DELF TEF: Tests 2026” app.""",
    faq=[("How long does it take to get TCF Canada results?", "Results are published within 15 business days of France Éducation international receiving the session materials. In practice, that means within two weeks in Montpellier, two to three weeks in Lyon and Ottawa, three to four in Vancouver and five weeks in Tunisia. TEF results arrive in about 1 to 2 weeks."),
         ("How long are TCF Canada results valid?", "Two years, as with the TEF. For the TCF, the period runs from the date the results certificate is issued. For the TEF, the official pages contradict each other: the registration conditions say the date of issue, the presentation page the test date — the gap can reach several weeks. Go by the less favourable date, the test date, and have your centre confirm if the deadline is tight."),
         ("Do my results need to be valid when I submit my PR application?", "Yes, and at two points rather than one: your results must be less than two years old when you create your Express Entry profile and when you submit your application for permanent residence. As several months can pass between the two, a test taken too early can expire along the way. So don’t take it as early as possible: take it when your profile is ready to be created."),
         ("Can I get my TCF Canada results re-marked?", "Not for sessions held since 1 September 2026: re-marking is no longer possible, and retaking the test is the only recourse. For earlier sessions, re-marking covered only speaking and writing, never the multiple-choice tests, had to be requested within a month of the certificates being sent to the centre, and the new mark replaced the old one, even if it was lower."),
         ("How many times can you take the TCF Canada?", "As many times as you like: neither the TCF nor the TEF limits the number of attempts. The only constraints are the waiting period between two attempts and the fact that each attempt is paid at full price — from €135 to €285 in France depending on the version and the centre, and $400 to $440 for a TCF Canada in Canada."),
         ("How long do you have to wait to retake the TCF Canada?", "France Éducation international’s test pages state 20 days, but several of its PDF sheets and its candidate handbook state 30 days — and for the TCF IRN, the page and the sheet contradict each other. Don’t time a second attempt to the week: have your centre confirm the waiting period, and plan for the least favourable margin if your application has a deadline. For the TEF, it’s 20 days between two attempts at the same test, with no ambiguity."),
         ("Can I retake only the section I failed?", "Not in the TCF Canada or the IRN versions, whose tests are officially indivisible: it’s the full test or nothing. The TCF Québec and the TEFAQ, however, are modular — you register for 1 to 4 tests of your choice, so you can retake just the one you want to improve."),
         ("What happens if my results certificate expires during my application?", "You have to retake the test — in full, since there is no partial retake for the TCF Canada or the IRN versions. That’s four tests to take again and the full fee to pay again: between €135 and €285 in France, depending on the version and the centre."),
         ("Do DELF and DALF diplomas expire?", "The diploma itself has no expiry date, which is its advantage for procedures in France. But Quebec applies its own condition: a DELF or DALF is accepted there in place of the TCF Québec only if it is less than two years old, with a minimum mark in speaking and listening. So the diploma’s advantage disappears for a Quebec project.")],
    also=[("/en/tcf-canada-test-dates-2026/", "TCF Canada test dates 2026", "Sessions centre by centre, to plan a first attempt or a retake."),
          ("/en/tcf-canada-clb-7/", "TCF Canada CLB 7: the exact scores", "The thresholds test by test, to see which one capped your application."),
          ("/en/tcf-vs-tef-canada/", "TCF or TEF Canada: which to choose?", "The CLB tables, formats and timelines of the two tests IRCC accepts.")],
    sources="""<strong>Validity and retake rules change, and sometimes contradict each other.</strong> This page is up to
date as of 7 August 2026 for validity, waiting periods and retakes, and flags the points where the official
documentation isn’t consistent with itself; the results timelines by centre and the end of re-marking were checked on
17 September 2026. Check the exact start date with your centre, have it confirm waiting periods and retake arrangements
before you plan a second attempt, and check the requirements of your process on
<a href="https://www.canada.ca/en/services/immigration-citizenship.html" rel="noopener">canada.ca</a>,
<a href="https://www.quebec.ca/immigration" rel="noopener">quebec.ca</a> or
<a href="https://www.service-public.fr/" rel="noopener">service-public.fr</a>.""",
))

# Country chips shared by the three exam pages (only the English country pages exist)
CHIPS = """
<p class="serie-label">DELF and DALF outside France, country by country</p>
<div class="chips">
<a class="chip" href="/en/delf-uk/">United Kingdom</a>
<a class="chip" href="/en/delf-usa/">United States</a>
<a class="chip" href="/en/">All locations →</a>
</div>
"""

CTA_DELF_H2 = "Practise in real exam conditions"


# ===========================================================================
# DELF B2 — from /delf-b2/ and its modules (format-bareme, a-quoi-sert, ecrit-oral, inscription)
# ===========================================================================
PAGES.append(dict(
    fr_path="/delf-b2/", lang="en", variant="en-GB", section="en", slug="delf-b2", accent="accent-delf",
    crumbs=[HOME], crumb="DELF B2 exam", inline_cta=False,
    title="DELF B2 exam 2026: format, scoring, dates and preparation",
    desc="DELF B2 exam: 4 sections in 2 h 50, pass mark 50/100, minimum 5/25 per section. What it’s for, how to prepare, dates and fees in France, the UK and the US.",
    h1="DELF B2 exam: the lifetime diploma for French citizenship, residence and university",
    intro="""The DELF B2 is a <strong>French state diploma, valid for life</strong>, awarded by France’s Ministry of National
Education. Four sections scored out of 25, a total out of <strong>100</strong>, and a pass from <strong>50/100</strong>
— with a minimum score per section that, every year, fails candidates whose total was otherwise high enough. Here is
the format, the scoring, what the diploma is for, how to prepare, and the dates and fees in France, the UK and the
US.""",
    facts=["<strong>4 sections scored out of 25</strong> each: listening, reading, writing and speaking. Total out of <strong>100</strong>.",
           "Pass mark: <strong>50/100</strong>.",
           "⚠️ A score below <strong>5/25</strong> in any one section means you <strong>fail</strong>, whatever your total.",
           "Length: <strong>2 h 50 min</strong>, plus 30 minutes of preparation before the speaking test.",
           "Since the reform, listening and reading are <strong>100% multiple-choice</strong> and the guided interview has "
           "gone from the speaking test. Format in place everywhere since <strong>September 2024</strong>.",
           "<strong>A diploma for life</strong>: unlike the TCF or the TEF, it never expires.",
           "In France, <strong>ten sessions a year</strong>, the B2 always on a Wednesday at 2 pm; in the UK and the US, the "
           "next session is in <strong>December 2026</strong>.",
           "Fees: <strong>€125 to €280</strong> in France depending on the centre, <strong>£160</strong> in the UK (£170 for "
           "2027 sessions), <strong>US$190</strong> in the US on the centres’ shared fee schedule."],
    toc=[("what-is", "What is the DELF B2?"), ("steps", "Your path in 5 steps"),
         ("format", "The exam format: four sections"), ("scoring", "Scoring and the minimum-score trap"),
         ("reform", "What the reform changed"), ("what-for", "What the DELF B2 is for"),
         ("writing", "The writing test, the one that decides"), ("speaking", "The speaking test: monologue, then debate"),
         ("prepare", "How to prepare"), ("dates-fees", "Dates and fees: France, the UK, the US")],
    body="""
<div class="stats">
<div class="stat"><b>2 h 50</b><span>4 sections</span><em>listening 30 · reading 60 · writing 60 · speaking 20 min</em></div>
<div class="stat"><b>50 / 100</b><span>to pass</span><em>the four sections combined</em></div>
<div class="stat"><b>5 / 25</b><span>minimum score</span><em>in any one section</em></div>
<div class="stat"><b>Lifetime</b><span>diploma validity</span><em>the level required for French citizenship</em></div>
</div>

<h2 id="what-is">What is the DELF B2?</h2>
<p>The <strong>DELF B2</strong> is an official <strong>diploma</strong> of France’s Ministry of National Education,
awarded by France Éducation international, that certifies level B2 of the Common European Framework of Reference
(CEFR): the level of an independent user who can argue a case, defend an opinion and follow a university course. You
take it at an approved test centre — in France, at one of the ten national sessions of the year — in <strong>four
sections</strong> scored out of 25: listening, reading, writing (250 words) and speaking (a presentation followed by a
debate).</p>

<p>You pass from <strong>50/100</strong>, with a minimum score of 5/25 per section, and the diploma is <strong>valid
for life</strong>. It is the most sought-after DELF diploma: it opens the doors of French universities, and since
1 January 2026 it proves the B2 level required for <strong>French citizenship</strong> — permanently, whereas a
<a href="/en/tcf-irn/">TCF IRN</a> expires after two years.</p>

<h3>Who it’s for</h3>
<ul>
<li>Applicants for <strong>French citizenship</strong>, who must prove B2 in speaking and in writing.</li>
<li>Students aiming for a <strong>French or French-speaking university</strong> — except on the courses that ask for
C1.</li>
<li>Anyone who wants <strong>permanent</strong> proof of their level, without retaking a test every two years.</li>
</ul>

<h2 id="steps">Your path in 5 steps</h2>
<ol class="steps">
<li><b>Check that B2 is your level</b><span>French citizenship: B2 in speaking and in writing since 2026; university: B2, sometimes C1. <a href="#what-for">What the DELF B2 is for.</a></span></li>
<li><b>Diploma or test?</b><span>The DELF B2 never expires; the <a href="/en/tcf-irn/">TCF IRN</a> is held every week but is valid for two years. <a href="/en/french-citizenship-b2/">B2 for French citizenship.</a></span></li>
<li><b>Prepare for the four sections</b><span>250 words of argument, a speaking test with a debate, two thresholds. <a href="#scoring">The scoring</a>, <a href="#writing">the writing</a>, <a href="#speaking">the speaking</a>, and <a href="/en/delf-b2-practice-test/">practice exercises with answers</a>.</span></li>
<li><b>Register in time</b><span>In France, the B2 is held on a Wednesday at 2 pm, ten times a year, and registration closes four to ten weeks before. <a href="#dates-fees">The calendar and the centres</a>, in France and beyond.</span></li>
<li><b>Exam day, then the diploma</b><span>Test-day notice and ID; results within 4 to 6 weeks, a diploma for life — and a <a href="/en/delf-b2-practice-test/">mock exam</a> beforehand, so you don’t pay the fee (€125 to €280 in France) twice.</span></li>
</ol>

<h2 id="format">The DELF B2 exam format: four sections</h2>
<p>The first three sections are <strong>group tests</strong>, taken one after another in the same half-day. The speaking
test is <strong>individual</strong> and can take place on another day.</p>
""" + table("DELF B2 format, the version that came out of the 2020 reform, fully in place since September 2024. Source: France Éducation international and the DELF B2 candidate handbook.",
            ["Section", "Content", "Time", "Score"],
            [("Listening", "3 exercises / 5 audio documents", "30 min", "/25"),
             ("Reading", "3 exercises / 5 written documents", "60 min", "/25"),
             ("Writing", "1 task, 250 words minimum", "60 min", "/25"),
             ("Speaking", "2 parts: sustained monologue + debate", "20 min <em>(+ 30 min of preparation)</em>", "/25"),
             ("<strong>Total</strong>", "", "<strong>2 h 50</strong>", "<strong>/100</strong>")], wide=False) + """

<p><strong>In listening</strong>, the first two exercises are based on long radio documents — around two and a half to
three minutes — which you hear <strong>twice</strong>. The third exercise strings together three short documents, about
a minute each, which you hear <strong>only once</strong>. This asymmetry is the first trap of the format: candidates used
to hearing everything twice are caught out on the last exercise, just when their concentration is already
flagging.</p>

<p><strong>In reading</strong>, the first two exercises are based on long articles, around 425 to 450 words. The third
is different: three short documents of 100 to 120 words set out three points of view on the same topic, and your task is
to <strong>match each point of view to its author</strong>. It is an exercise in comparative reading, not literal
comprehension.</p>

<h2 id="scoring">Scoring and the minimum-score trap</h2>
<p>The DELF doesn’t work like the TCF. It is an <strong>exam</strong>, not a placement test: you can fail it. Two rules
decide, and the second is the one candidates discover too late.</p>
""" + table("The two DELF B2 thresholds.", ["Rule", "Threshold", "Effect"],
            [("Overall score", "<strong>50/100</strong>", "Below it, you fail"),
             ("Minimum score per section", "<strong>5/25</strong>", "Below it in <em>a single</em> section, you fail — even with 60/100 overall")],
            wide=False) + """

<p>The strategic consequence is clear, and counter-intuitive: <strong>a very weak skill costs you more than a strong one
earns you</strong>. A candidate with 20/25 in reading and 4/25 in speaking fails, even though their total is above the
pass mark. So the first job in your preparation is to <strong>get your weakest section out of the danger zone</strong>,
before you even try to gain points elsewhere.</p>

<p>Only then comes the balancing act on the total: aim for 15 or more in your strong sections to secure it. Points do
offset each other in the DELF — that is what sets it apart from the TCF and the TEF, where the authority that receives
your application reads each test separately.</p>

<h2 id="reform">What the reform changed</h2>
<p>The current format has been fully in place since <strong>September 2024</strong>. Three changes matter for your
preparation — and make any earlier past paper obsolete.</p>

<ul>
<li><strong>Listening and reading became entirely multiple-choice.</strong> Open questions and true/false with
justification have gone. You no longer write anything in these two sections, which completely changes how you manage
your time: no more written answers to polish, but no chance of picking up points with a partly correct justification
either.</li>
<li><strong>The point-of-view matching exercise</strong> appeared in reading. It asks you to identify an argumentative
position, not a factual piece of information.</li>
<li><strong>The guided interview was removed</strong> from the speaking test. The test now starts straight away with the
sustained monologue. The friendly warm-up that used to help you relax no longer exists: you get to the heart of the
matter immediately.</li>
</ul>

<div class="note">
<p><strong>Beware of out-of-date resources.</strong> Many of the past papers, tutorials and videos available online
describe the old format. If a document mentions a guided interview in the speaking test or open questions in listening
or reading, it describes an exam that no longer exists. Always check the date of a resource before you practise on
it.</p>
</div>

<h2 id="what-for">What the DELF B2 is for</h2>
<p>The DELF B2 is the most sought-after French diploma because it opens two doors at once: <strong>university</strong>
— most bachelor’s and master’s degrees require it, with some courses asking for C1 — and, since 1 January 2026,
<strong>French citizenship</strong>, for which it proves the language requirement for life. B2 is the pivotal level of
the French system, with three main uses, one of which has become crucial this year.</p>

<ul>
<li><strong>French universities.</strong> Most bachelor’s and master’s degrees require B2. Some courses and some
<em>grandes écoles</em> ask for C1 — in which case it is the <a href="/en/dalf-c1/">DALF</a> you should aim for. The
institution’s requirement always takes precedence over any general rule.</li>
<li><strong>French citizenship.</strong> Since <strong>1 January 2026</strong>, an application for French nationality
requires level B2, in speaking and in writing. A DELF B2 diploma proves it directly — see our page on
<a href="/en/french-citizenship-b2/">the B2 level for French citizenship</a>.</li>
<li><strong>Lasting proof of your level.</strong> This is the decisive argument against the TCF and the TEF. A test’s
results certificate is valid for two years; <strong>a diploma never expires</strong>. If your administrative journey is
going to stretch over several years, the diploma is by far the safest option.</li>
</ul>

<div class="note">
<p><strong>Diploma or test: not the same logic.</strong> The DELF certifies your level once and for all.
The <a href="/en/tcf-irn/">TCF IRN</a> or the TEF IRN place you on a scale, with a results certificate of limited
validity, but they take a single morning and are designed specifically for administrative procedures. Check the list of
accepted proofs on service-public.fr before paying for any registration: beyond the level, a certification must also be
listed in France Compétences’ specific register (<em lang="fr">répertoire spécifique</em>).</p>
</div>

<h2 id="writing">The writing test, the one that decides</h2>
<p>One task, 60 minutes, <strong>250 words minimum</strong>. The topic asks for a <strong>personal position</strong>: a
contribution to a debate, a formal letter, a critical article. It is the most selective section of the DELF B2, and the
one where the gap between a good level of French and a good mark is widest.</p>

<p>What the examiner assesses is not your opinion but your <strong>ability to build it</strong>:</p>

<ul>
<li><strong>Following the instructions and the genre.</strong> A formal letter with no greeting and no letter
structure loses points before the first sentence is even assessed for language.</li>
<li><strong>The structure of the argument.</strong> A clear position, ranked arguments, the opposing objection taken into
account. Piling up correct but unconnected ideas quickly hits a ceiling.</li>
<li><strong>Logical connectors.</strong> They are the most visible marker of B2 — and the easiest to work on
mechanically.</li>
<li><strong>Register.</strong> Slipping unnoticed into casual language is a frequent loss of points for candidates who
speak French well day to day.</li>
<li><strong>Length.</strong> 250 words is a floor, not a target. Below it, task completion is marked down, whatever the
quality of the language.</li>
</ul>

<h2 id="speaking">The speaking test: monologue, then debate</h2>
<p>Thirty minutes of preparation, then twenty minutes in front of the examiners, in two parts. You draw a short prompt
document, you identify the issue it raises, and you defend a point of view — first on your own, then facing examiners
who contradict you.</p>

<p>The second part is the one that takes candidates by surprise. <strong>The examiners don’t agree with you, and that is
deliberate</strong>: their role is to test your ability to hold a position, to qualify it, to concede without giving in.
Candidates who abandon their argument at the first objection lose points — not on language, but on the skill being
assessed.</p>

<p>The thirty minutes of preparation need specific practice too. They aren’t enough to write out a text: they are for
building a plan and noting keywords. A candidate who writes out sentences and then reads their notes is spotted
immediately, and penalised on fluency.</p>

<h2 id="prepare">How to prepare</h2>
<ol>
<li><strong>A full mock exam right at the start</strong>, scored on the official scales, to identify your weakest
section. Because of the minimum score, that is the one that decides.</li>
<li><strong>Get that section out of the danger zone</strong> as your absolute priority, before looking for points
elsewhere.</li>
<li><strong>Work on the writing test through structure</strong>, not vocabulary. Most lost points come from the plan and
the instructions, not from your vocabulary.</li>
<li><strong>Simulate the speaking test in real conditions</strong>, the 30 minutes of preparation included, with someone
deliberately contradicting you in the second part.</li>
<li><strong>Repeat timed mock exams</strong> until the format no longer surprises you.</li>
</ol>

<p>For both the writing and the speaking test, the blind spot is the same as in every French exam: you can’t assess
yourself against criteria you don’t know. Knowing whether your text is worth 9 or 13 out of 25 is exactly what AI
feedback against the official criteria solves. One exercise per section, in the reformed format and with the answers
explained, is on our <a href="/en/delf-b2-practice-test/">DELF B2 practice test page</a>.</p>

<h2 id="dates-fees">DELF B2 dates and fees: France, the UK and the US</h2>
<p><strong>In France</strong>, you take the DELF B2 at one of the <strong>143 approved centres</strong>, during one of
the year’s <strong>ten national sessions</strong> — always on a Wednesday at 2 pm — and you register with the centre,
never with France Éducation international. The autumn 2026 sessions fall on <strong>7 October, 4 November and
2 December</strong>; in 2027, there are ten sessions from January to December, never in April or September. Each centre
chooses which sessions it opens and closes registration <strong>four to ten weeks</strong> before the written papers —
some sessions are full months ahead.</p>

<p>Each centre also sets its own fee. At the centres we checked on 17 September 2026, the same B2 cost €125 at Nantes
Université, €159 at the Alliance Française de Lyon, €180 in Lille, €249 at the Sorbonne Nouvelle, €269 at the Cours de
civilisation française de la Sorbonne and €280 at the Alliance Française de Paris. Results arrive within <strong>4 to 6
weeks</strong>, and the diploma is valid for life.</p>

<p>Six centres from our guide, among the 143 approved in France: the Alliance Française de Paris, the Université
Sorbonne Nouvelle, the Cours de Civilisation Française de la Sorbonne (CCFS), the Alliance Française de Lyon, Nantes
Université and the Alliance Française de Lille Métropole. Our directory of the 143 centres, with addresses and phone
numbers, our guide to where to take the DELF in France, with the 2026-2027 calendar, and our city pages — Paris, Lyon,
Lille, Nantes, Bordeaux, Marseille, Toulouse, Montpellier, Strasbourg — are in French.</p>

<p><strong>In the UK</strong>, the DELF B2 costs <strong>£160</strong> for 2026 sessions and <strong>£170</strong> for
2027 sessions, and the next session is in December 2026: dates, centres and registration deadlines are on our
<a href="/en/delf-uk/">DELF in the UK</a> page. <strong>In the US</strong>, the next session runs from <strong>7 to 11
December 2026</strong>, and the DELF B2 costs <strong>US$190</strong> on the centres’ shared fee schedule, before any
extra fees: see <a href="/en/delf-usa/">DELF in the USA</a>. Both pages were checked on 8 October 2026.</p>
""" + CHIPS,
    cta_h2=CTA_DELF_H2,
    cta_p="""Timed mock exams in the reformed DELF B2 format, scored on the official scale out of 25 per section with a
warning when you fall below the minimum score, and AI feedback on writing and speaking — in the “TCF DELF TEF: Tests
2026” app.""",
    faq=[("What is the DELF B2 exam, and what does B2 mean?", "An official diploma of France’s Ministry of National Education certifying level B2 of the Common European Framework of Reference (CEFR) — the level of an independent user who can argue a case, defend an opinion and follow a university course. Four sections scored out of 25, a pass from 50/100 with a minimum of 5/25 per section, in 2 h 50 min plus 30 minutes of preparation before the speaking test. It is valid for life."),
         ("Is the DELF B2 certificate a test or a diploma?", "A diploma: you pass or fail it, and once you have it, it never expires. The TCF and TEF tests, by contrast, place your level without a pass mark, but their results certificate expires after two years."),
         ("What is the DELF B2 exam pattern, and how long is it?", "2 hours 50 minutes for the three group sections and the speaking test: 30 minutes of listening, 60 minutes of reading, 60 minutes of writing and 20 minutes of speaking. On top of that come 30 minutes of preparation before the speaking test, which don’t count in the official length of the exam."),
         ("What score do you need to pass the DELF B2?", "50 out of 100. The four sections are scored out of 25 each, and there is only one minimum per section: a score below 5 out of 25 in any single section means you fail, whatever your total."),
         ("What did the 2020 reform change in the DELF B2?", "Three things. Listening and reading became entirely multiple-choice: open questions and true/false with justification have gone. Reading now includes an exercise in matching points of view to their authors. And in the speaking test, the guided interview was removed: only the sustained monologue and the debate with the examiners remain. This format has been fully in place since September 2024, which makes any earlier past paper obsolete."),
         ("How many words do you write in the DELF B2 writing test?", "250 words minimum, in a single task, in 60 minutes. It is a floor, not a target: writing less costs you points on task completion, whatever the quality of your French. The topic asks for a personal position — a contribution to a debate, a formal letter or a critical article."),
         ("Is the DELF B2 enough for a French university?", 'In most cases, yes: most bachelor’s and master’s degrees ask for B2. Some courses and some schools ask for C1 — always check the requirement of the institution you are applying to, which takes precedence over any general rule. For C1, see our <a href="/en/dalf-c1/">DALF C1 page</a>.'),
         ("Is the DELF B2 accepted for French citizenship instead of the TCF IRN?", "Yes, for the language requirement: since 1 January 2026, French citizenship requires level B2, and a DELF B2 diploma proves it directly — for life, whereas a TCF or TEF results certificate is valid for two years. It is the safest option if your administrative journey is going to take time. It doesn’t exempt you from the civics exam or the other conditions for citizenship. Check the list of accepted proofs on service-public.fr before paying for any registration."),
         ("How long does it take to go from B1 to B2?", 'Generally 4 to 6 months of regular practice. If your <a href="/en/delf-b1/">B1</a> is solid and it is mostly a matter of getting used to the exam format, 6 to 10 weeks of methodical practice can be enough. The gap between B1 and B2 is mostly about argument: at B2, understanding and narrating are no longer enough — you have to take a position and defend it.'),
         ("When are the DELF B2 exam dates in 2026 and 2027?", "In France, the DELF B2 is held at 2 pm on the Wednesday of each national session: in autumn 2026, on 7 October, 4 November and 2 December; in 2027, ten sessions from January to December, never in April or September. Each centre chooses which sessions it opens and closes registration four to ten weeks before. In the UK, the next session is in December 2026; in the US, from 7 to 11 December 2026."),
         ("How much does the DELF B2 exam cost?", "There is no national fee. In France, at the centres we checked on 17 September 2026: €125 at Nantes Université, €159 at the Alliance Française de Lyon, €180 in Lille, €249 at the Sorbonne Nouvelle, €269 at the Cours de civilisation française de la Sorbonne and €280 at the Alliance Française de Paris. In the UK, £160 for 2026 sessions and £170 for 2027 sessions; in the US, US$190 on the centres’ shared fee schedule, before any extra fees.")],
    also=[("/en/delf-b2-practice-test/", "DELF B2 practice test, with answers", "One exercise per section, with answers, and the strategy the minimum score imposes."),
          ("/en/french-citizenship-b2/", "French citizenship: the B2 level", "What has changed since 1 January 2026: B2 in speaking and in writing, the civics exam, the transitional rules."),
          ("/en/dalf-c1/", "DALF C1 and C2: the advanced level", "The level above, and the exemption from language tests it gives you at university.")],
    sources="""<strong>Formats change.</strong> This page is up to date as of 7 August 2026; the dates and fees for France were
checked on 17 September 2026, and those for the UK and the US come from our country pages, checked on 8 October 2026.
Exam structures and institutions’ requirements change regularly — check the format on
<a href="https://www.france-education-international.fr/diplome/delf-tout-public" rel="noopener">france-education-international.fr</a>
and the conditions of your administrative procedure on
<a href="https://www.service-public.fr/" rel="noopener">service-public.fr</a> before you register.""",
))


# ===========================================================================
# DELF B1 — from /delf-b1/ and its modules (format-bareme, carte-de-resident, ecrit-oral, inscription)
# ===========================================================================
PAGES.append(dict(
    fr_path="/delf-b1/", lang="en", variant="en-GB", section="en", slug="delf-b1", accent="accent-delf",
    crumbs=[HOME], crumb="DELF B1 exam", inline_cta=False,
    title="DELF B1 exam: format, scoring, 2026 dates and fees",
    desc="DELF B1 exam: 4 sections in 2 h 10, pass mark 50/100, minimum 5/25 per section. Required for a French resident card since 2026; dates, fees, preparation.",
    h1="DELF B1 exam: the threshold level, certified for life",
    intro="""The DELF B1 certifies the <strong>threshold level</strong>: the point at which you become independent in
French. Four sections in <strong>2 h 10</strong>, each scored out of 25, with a pass at <strong>50/100</strong>. Since
1 January 2026, it is also the level required for a <strong>first French resident card</strong> — and a diploma, unlike a
test result, never expires. Here is the format, the scoring, the resident card, how to prepare, and the dates and fees
in France, the UK and the US.""",
    facts=["<strong>4 sections scored out of 25</strong> each, total out of <strong>100</strong>, pass from <strong>50/100</strong>.",
           "⚠️ A score below <strong>5/25</strong> in any one section means you <strong>fail</strong>.",
           "Total length: <strong>2 h 10</strong>.",
           "<strong>A diploma for life</strong>, awarded by France’s Ministry of National Education.",
           "Since 1 January 2026, <strong>B1 is required</strong> for a first resident card in France (order of 22 December "
           "2025), up from A2 before.",
           "⚠️ Don’t mix up the three levels: <strong>A2</strong> for the first multi-year residence permit, <strong>B1</strong> "
           "for the resident card, <strong>B2</strong> for citizenship.",
           "In France, <strong>ten sessions a year</strong>, the B1 always on a Wednesday at 10 am, from <strong>€125 to "
           "€230</strong> depending on the centre; results in 4 to 6 weeks."],
    toc=[("what-is", "What is the DELF B1?"), ("steps", "Your path in 5 steps"),
         ("format", "The exam format: four sections"), ("scoring", "Scoring and the minimum score"),
         ("resident-card", "The DELF B1 and the French resident card"), ("diploma-or-test", "Diploma or test: which to choose"),
         ("writing", "The writing test in 160 words"), ("speaking", "The speaking test in three parts"),
         ("prepare", "How to prepare"), ("dates-fees", "Dates and fees: France, the UK, the US")],
    body="""
<div class="stats">
<div class="stat"><b>2 h 10</b><span>4 sections</span><em>listening 25 · reading 45 · writing 45 · speaking 15 min</em></div>
<div class="stat"><b>50 / 100</b><span>to pass</span><em>the four sections combined</em></div>
<div class="stat"><b>5 / 25</b><span>minimum score</span><em>in any one section</em></div>
<div class="stat"><b>Lifetime</b><span>diploma validity</span><em>results in 4 to 6 weeks</em></div>
</div>

<h2 id="what-is">What is the DELF B1?</h2>
<p>The <strong>DELF B1</strong> is an official <strong>diploma</strong> of France’s Ministry of National Education,
awarded by France Éducation international, that certifies level B1 of the Common European Framework of Reference
(CEFR) — the “threshold level”, that of an independent user who can get by in most everyday situations. You take it at
an approved test centre — in France, at one of the ten national sessions of the year — in <strong>four sections</strong>
scored out of 25: listening, reading, writing (160 words) and speaking, in three parts.</p>

<p>You pass from <strong>50/100</strong>, with a minimum of 5/25 in each section — and the diploma is <strong>valid for
life</strong>. Since 1 January 2026, B1 is the level required for a first <strong>resident card</strong> in France: the
DELF B1 proves it permanently, whereas a TCF or TEF test result expires after two years.</p>

<h3>Who it’s for</h3>
<ul>
<li>Applicants for a first <strong>French resident card</strong>, who must prove B1 in speaking and in writing.</li>
<li>Anyone who wants <strong>permanent</strong> proof of their level, for an application, a CV or a training course.</li>
<li>Not applicants for French citizenship: since 2026, they need <a href="/en/delf-b2/">B2</a>.</li>
</ul>

<h2 id="steps">Your path in 5 steps</h2>
<ol class="steps">
<li><b>Check that B1 is your level</b><span>Resident card: B1 since 2026; citizenship: B2. <a href="#resident-card">The B1 and the resident card</a> — <a href="/en/french-citizenship-b2/">B2 for citizenship</a>.</span></li>
<li><b>Diploma or test?</b><span>The DELF never expires but is held ten times a year in France, with registration that closes early; the <a href="/en/tcf-irn/">TCF IRN</a> is held every week but is valid for two years. <a href="#diploma-or-test">Which to choose.</a></span></li>
<li><b>Prepare for the four sections</b><span>160 words in writing, a speaking test in three parts, and two thresholds to clear. <a href="#scoring">The scoring</a>, <a href="#writing">the writing</a>, <a href="#speaking">the speaking</a>.</span></li>
<li><b>Register in time</b><span>In France, 143 centres, 10 sessions a year, a registration window of a few days to a few weeks. <a href="#dates-fees">The dates and the centres.</a></span></li>
<li><b>Exam day, then the diploma</b><span>Test-day notice and ID; results within 4 to 6 weeks, a diploma valid for life — and a mock exam beforehand, so you don’t pay twice.</span></li>
</ol>

<h2 id="format">The DELF B1 exam format: four sections</h2>
""" + table("DELF B1 format. Source: France Éducation international, structure checked in July 2026.",
            ["Section", "Content", "Time", "Score"],
            [("Listening", "3 documents, multiple-choice questions", "25 min", "/25"),
             ("Reading", "2 documents, multiple-choice questions", "45 min", "/25"),
             ("Writing", "1 task, 160 words minimum", "45 min", "/25"),
             ("Speaking", "3 parts <em>(10 min of preparation for the 3rd)</em>", "15 min", "/25"),
             ("<strong>Total</strong>", "", "<strong>2 h 10</strong>", "<strong>/100</strong>")], wide=False) + """

<p>The first three sections are group tests, taken one after another in the same half-day. The speaking test is
individual and can take place on another day. It is a short exam — about 40 minutes shorter than the
<a href="/en/delf-b2/">DELF B2</a> — but the three group sections in a row are still demanding.</p>

<h2 id="scoring">Scoring and the minimum score</h2>
<p>The DELF is an <strong>exam</strong>, not a placement test: you can fail it. Two rules decide the result.</p>
""" + table("The two DELF B1 thresholds.", ["Rule", "Threshold", "Effect"],
            [("Overall score", "<strong>50/100</strong>", "Below it, you fail"),
             ("Minimum score per section", "<strong>5/25</strong>", "Below it in <em>a single</em> section, you fail — even with 60/100 overall")],
            wide=False) + """

<p>The consequence is the same as at B2, and it shapes your whole preparation: <strong>a very weak skill costs more than
a strong one earns</strong>. A candidate who excels in writing but is stuck at 4/25 in speaking fails, whatever their
total. Your first priority is therefore to get your weakest section out of the danger zone — not to polish the one you
are already good at.</p>

<p>That said, points do offset each other: above the floor of 5, they balance out from one section to another. That is
what sets the DELF apart from the <a href="/en/tcf-canada/">TCF</a> and the TEF, where the authority that receives your
application reads each test separately, with no offsetting possible.</p>

<h2 id="resident-card">The DELF B1 and the French resident card</h2>
<p>This is the change that made demand for B1 soar this year. Since <strong>1 January 2026</strong>, a <strong>first
resident card</strong> (<em lang="fr">carte de résident</em>) in France requires level B1, up from A2 before — under the
<strong>order of 22 December 2025</strong> (<em lang="fr">arrêté du 22 décembre 2025</em>).</p>

<div class="note">
<p><strong>The DELF B1 is explicitly accepted.</strong> It falls under <strong>point 4 of Article 3</strong> of that
order, which accepts any diploma certifying a level of French at least equivalent to B1. And unlike a TCF or TEF results
certificate, valid for two years, <strong>a diploma has no expiry date</strong>: one obtained years ago is still
accepted.</p>
</div>

<p>One point catches many applicants out: moving from a multi-year residence permit to a resident card <strong>is not a
renewal</strong> — it is a first issue of a resident card. So B1 and the civics exam are required. For residence
permits, applicants over 65 are exempt from the language requirement. Our article on the resident card, in French,
covers the whole procedure — exemptions, the civics exam, the real cost.</p>

<p>Don’t mix up the three levels, which correspond to three separate procedures:</p>
""" + table("Level of French required by procedure, as of 7 August 2026. Sources: the order of 22 December 2025 and Article L. 433-4 of the CESEDA, France’s code on the entry and residence of foreign nationals.",
            ["Procedure", "Level required"],
            [("First multi-year residence permit", "<strong>A2</strong>"),
             ("First resident card", "<strong>B1</strong>"),
             ("French citizenship", "<strong>B2</strong>")], wide=False) + """

<h2 id="diploma-or-test">Diploma or test: which to choose</h2>
<p>To prove B1 to the French authorities, there are two routes, and they don’t follow the same logic.</p>

<ul>
<li><strong>Tests</strong> — the <a href="/en/tcf-irn/">TCF IRN</a> and the TEF IRN — are designed specifically for these
procedures. They take a single morning, are shorter, and give you a results certificate valid for <strong>two
years</strong>.</li>
<li><strong>Diplomas</strong> — DELF, DALF — involve a longer exam and less frequent sessions, but they are
<strong>yours for good</strong>.</li>
</ul>

<p>The rule of thumb: if your application is going in soon, a test is enough and takes less time. If your
administrative journey is going to stretch over several years — which is common — the diploma saves you from having to
retake, and pay again for, a test that expires at the wrong moment.</p>

<h2 id="writing">The writing test in 160 words</h2>
<p>One task, 45 minutes, <strong>160 words minimum</strong>. The topic asks you to express a personal position on a
general theme: an essay, a letter, an article. It isn’t yet the structured argument of B2, but it is no longer the
factual description of A2.</p>

<p>What makes the difference at this level:</p>

<ul>
<li><strong>Respecting the genre asked for.</strong> A letter with no greeting and no sign-off loses points
before the language is even assessed.</li>
<li><strong>Connectors.</strong> At B1, ideas are expected to be explicitly linked: « d'abord », « ensuite »,
« cependant », « c'est pourquoi ». It is the most rewarding marker to work on.</li>
<li><strong>Past tenses.</strong> Switching between the <em lang="fr">passé composé</em> and the
<em lang="fr">imparfait</em> is the most discriminating grammar point at this level, and the one most often
penalised.</li>
<li><strong>Length.</strong> 160 words is a floor. Below it, the instructions aren’t followed, regardless of the quality
of the language.</li>
</ul>

<h2 id="speaking">The speaking test in three parts</h2>
<p>Fifteen minutes, three exercises in a row — and only one preparation time, for the last one.</p>

<ol>
<li><strong>The guided interview.</strong> You introduce yourself and are asked questions about yourself, your
activities, your plans. No preparation. It is the easiest part to secure: it is predictable and can be rehearsed in
advance.</li>
<li><strong>The interaction exercise.</strong> You act out an everyday situation with the examiner: solving a problem,
getting something, negotiating. No preparation either.</li>
<li><strong>Expressing a point of view</strong> based on a short prompt document, with <strong>10 minutes of
preparation</strong>. You identify the theme and give your opinion.</li>
</ol>

<p>Unlike the DELF B2, where the guided interview was removed, it is <strong>still part of B1</strong>. Good news for
nervous candidates: the test starts with the most approachable exercise, which gives you time to settle in.</p>

<h2 id="prepare">How to prepare</h2>
<ol>
<li><strong>A full mock exam right at the start</strong>, scored on the official scales, to identify the section that
could make you fail.</li>
<li><strong>Get that section out of the danger zone</strong> first, before anything else.</li>
<li><strong>Rehearse the first two parts of the speaking test</strong>, which are predictable and can be prepared word for
word — the best return in your whole B1 preparation.</li>
<li><strong>Work on past tenses and connectors</strong>, the two most rewarding grammar points at this level.</li>
<li><strong>Regular timed mock exams</strong> until the three group sections in a row are no longer an endurance
test.</li>
</ol>

<p>For both the writing and the speaking test, you can’t assess yourself against criteria you don’t know — and that is
exactly where the minimum score comes into play. That is what AI feedback against the official criteria solves.</p>

<h2 id="dates-fees">DELF B1 dates and fees: France, the UK and the US</h2>
<p><strong>In France</strong>, you take the DELF B1 at one of the <strong>143 approved centres</strong> — universities,
Alliances Françaises, GRETA adult-education centres, language schools — during one of the year’s <strong>ten national
sessions</strong>, always on a Wednesday at 10 am. You register with the centre, never with France Éducation
international. Registration windows last from a few days — sometimes just two — to a few weeks, and close
<strong>four to ten weeks</strong> before the written papers. The autumn 2026 sessions fall on <strong>7 October,
4 November and 2 December</strong>; in 2027, there are ten sessions from January to December, never in April or
September.</p>

<p>Each centre sets its own fee. At the centres we checked on 17 September 2026: €125 at Nantes Université, €160 at the
Alliance Française de Lille, €194 at the Sorbonne Nouvelle, €214 at the Cours de civilisation française de la Sorbonne
and €230 at the Alliance Française de Paris. Results arrive within 4 to 6 weeks. Our directory of the 143 centres in
France and our guide to where to take the DELF in France, with the 2026-2027 calendar, are in French.</p>

<p><strong>In the UK and the US</strong>, the next DELF session is in December 2026 — from 7 to 11 December in the US.
The dates, centres and fees for each level are on our <a href="/en/delf-uk/">DELF in the UK</a> and
<a href="/en/delf-usa/">DELF in the USA</a> pages, checked on 8 October 2026.</p>
""" + CHIPS,
    cta_h2=CTA_DELF_H2,
    cta_p="""Timed mock exams in the DELF B1 format, scored on the official scale out of 25 per section with a warning when
you fall below the minimum score, and AI feedback on writing and speaking — in the “TCF DELF TEF: Tests 2026” app.""",
    faq=[("What is the DELF B1 exam?", "An official diploma of France’s Ministry of National Education certifying level B1 of the Common European Framework: four sections scored out of 25, a pass from 50/100 with a minimum of 5/25 per section, in 2 h 10. It is valid for life and, since January 2026, required for a first French resident card."),
         ("Is the DELF B1 a test or a diploma?", "A diploma: you pass or fail it, and once you have it, it never expires. The TCF and TEF tests, by contrast, place your level on a scale with no pass mark, but their results certificate expires after two years."),
         ("What is the DELF B1 exam format, and how long is it?", "2 h 10: 25 minutes of listening, 45 minutes of reading, 45 minutes of writing and 15 minutes of speaking, with 10 minutes of preparation for the third part of the speaking test."),
         ("What score do you need to pass the DELF B1?", "50 out of 100. The four sections are scored out of 25 each. A score below 5 out of 25 in any single section means you fail, even if your total is well above the pass mark."),
         ("Is the DELF B1 accepted for the French resident card?", "Yes. The DELF B1 falls under point 4 of Article 3 of the order of 22 December 2025, which accepts any diploma certifying a level of French at least equivalent to B1. Unlike a TCF or TEF results certificate, valid for two years, a diploma has no expiry date."),
         ("DELF B1 or TCF IRN for a French residence permit?", 'Both are accepted, but they follow different logic. The <a href="/en/tcf-irn/">TCF IRN</a> and the TEF IRN are designed for these procedures, take a single morning and give you a results certificate valid for two years. The DELF B1 is a longer exam, but it gives you a diploma that never expires. If your administrative journey is going to take time, the diploma is safer.'),
         ("Do you need B1 or B2 for French citizenship?", "B2, in speaking and in writing, since 1 January 2026. B1 is for the resident card; A2 for the first multi-year residence permit, under Article L. 433-4 of the CESEDA. Don’t mix up these three levels: they correspond to three separate procedures."),
         ("How many words do you write in the DELF B1 writing test?", "160 words minimum, in a single task, in 45 minutes. You express a personal position on a general topic — an essay, a letter or an article. It is a floor: writing less costs you points on task completion."),
         ("What happens in the DELF B1 speaking test?", "Three parts in a row in 15 minutes: a guided interview in which you introduce yourself, an interaction exercise in which you act out an everyday situation, and expressing a point of view based on a short prompt document. Only the third part comes with preparation time: 10 minutes."),
         ("When are the DELF B1 exam dates in 2026?", "In France, the DELF B1 is held at 10 am on the Wednesday of each national session: in autumn 2026, on 7 October, 4 November and 2 December; in 2027, ten sessions from January to December, never in April or September. Each centre chooses which sessions it opens and closes registration four to ten weeks before. In the UK and the US, the next session is in December 2026 — from 7 to 11 December in the US."),
         ("How much does the DELF B1 exam cost?", "There is no national fee. In France, at the centres we checked on 17 September 2026: €125 at Nantes Université, €160 at the Alliance Française de Lille, €194 at the Sorbonne Nouvelle, €214 at the Cours de civilisation française de la Sorbonne and €230 at the Alliance Française de Paris. For the UK and the US, see our country pages.")],
    also=[("/en/delf-b2/", "DELF B2 exam: format, scoring, dates", "The level above, required for French citizenship since January 2026."),
          ("/en/tcf-irn/", "TCF IRN", "The “test” alternative to the diploma, designed for French administrative procedures."),
          ("/en/french-citizenship-b2/", "French citizenship: the B2 level", "Your B1 is enough for the resident card — not for citizenship since 2026.")],
    sources="""<strong>Regulations change.</strong> This page is up to date as of 7 August 2026, and the dates and fees for France
were checked on 17 September 2026; it is not legal advice. The levels required and the list of accepted proofs change —
check your situation on <a href="https://www.service-public.fr/" rel="noopener">service-public.fr</a> and the exam
format on <a href="https://www.france-education-international.fr/diplome/delf-tout-public" rel="noopener">france-education-international.fr</a>
before you register.""",
))


# ===========================================================================
# DALF C1 · C2 — from /dalf/ and its modules (format, synthese-preparation, c1-ou-c2, inscription)
# ===========================================================================
PAGES.append(dict(
    fr_path="/dalf/", lang="en", variant="en-GB", section="en", slug="dalf-c1", accent="accent-delf",
    crumbs=[HOME], crumb="DALF C1 and C2", inline_cta=False,
    title="DALF C1 exam: format, scoring, preparation, C1 vs C2",
    desc="DALF C1 exam: 4 sections in 4 h 30 plus 1 hour of preparation, pass mark 50/100, the 200–240-word synthesis. C1 vs C2, how to prepare, dates and fees.",
    h1="DALF C1 and C2 exam: the advanced level that exempts you from university language tests",
    intro="""The DALF — <em lang="fr">diplôme approfondi de langue française</em>, the advanced diploma in French —
certifies levels <strong>C1</strong> and <strong>C2</strong>. It is <strong>valid for life</strong>, and the C1 exempts
you from any language test for admission to French universities. C1 and C2 don’t have the same format at all: four
sections on one side, <strong>two integrated sections</strong> on the other. Here is the format, the scoring, the
synthesis, how to prepare, C1 versus C2, and the dates and fees.""",
    facts=["<strong>DALF C1</strong>: 4 sections, <strong>4 h 30</strong> plus 1 hour of supervised preparation before the "
           "speaking test. Each scored out of 25, total out of 100.",
           "<strong>DALF C2</strong>: just 2 integrated sections, each scored out of 50.",
           "Pass mark: <strong>50/100</strong> in both cases. Minimum score: <strong>5/25</strong> per section in C1, "
           "<strong>10/50</strong> in C2.",
           "The key C1 task is the <strong>synthesis of documents</strong>: 200 to 240 words, objective, entirely reworded.",
           "<strong>A diploma for life</strong> — unlike TCF and TEF results certificates, valid for two years.",
           "The old options (humanities and social sciences versus sciences) have been <strong>abolished</strong>.",
           "In France, the same centres and sessions as the DELF, on Thursdays; the C1 costs <strong>€145 to €290</strong> "
           "depending on the centre."],
    toc=[("what-is", "What is the DALF?"), ("steps", "Your path in 5 steps"),
         ("c1", "The DALF C1 exam format, section by section"), ("c2", "The DALF C2: two integrated sections"),
         ("scoring", "Scoring and minimum scores"), ("synthesis", "The synthesis: the key C1 task"),
         ("prepare", "How to prepare for the DALF"), ("c1-or-c2", "DALF C1 vs C2: which to aim for"),
         ("exemption", "What the DALF exempts you from"), ("dates-fees", "Dates and fees: France, the UK, the US")],
    body="""
<div class="stats">
<div class="stat"><b>4 h 30</b><span>of tests for C1</span><em>+ 1 h of preparation; 4 h for C2</em></div>
<div class="stat"><b>C1 · C2</b><span>two independent diplomas</span><em>you can register directly for C2</em></div>
<div class="stat"><b>50 / 100</b><span>to pass</span><em>5/25 minimum per section in C1</em></div>
<div class="stat"><b>Lifetime</b><span>diploma validity</span><em>no language test for university</em></div>
</div>

<h2 id="what-is">What is the DALF?</h2>
<p>The <strong>DALF</strong> — <em lang="fr">diplôme approfondi de langue française</em> — is the official diploma of
France’s Ministry of National Education for the two advanced levels of the Common European Framework of Reference:
<strong>C1</strong>, that of a proficient user capable of clear, well-structured discourse, and <strong>C2</strong>,
that of mastery. Like the DELF, it is awarded by France Éducation international and taken at the same approved centres,
at the same sessions — on Thursdays, in France — and it is <strong>valid for life</strong>.</p>

<p>The <strong>DALF C1</strong> has four sections scored out of 25, in 4 h 30 plus an hour of preparation: listening and
reading, writing — a synthesis of documents of 200 to 240 words followed by an essay — and a spoken presentation. The
<strong>DALF C2</strong> has only two integrated sections, scored out of 50: a spoken one, and a written one of 700 words
minimum. A pass at 50/100 in both cases. The DALF <strong>exempts you from any French test</strong> for entry to French
universities.</p>

<h3>Who it’s for</h3>
<ul>
<li>Students whose course requires <strong>C1</strong> — literature, law, medicine, some <em>grandes écoles</em>.</li>
<li>Professionals who want proof of an advanced level, <strong>for life</strong>.</li>
<li>Not French administrative procedures, which stop at B2: the <a href="/en/delf-b2/">DELF B2</a> is enough.</li>
</ul>

<h2 id="steps">Your path in 5 steps</h2>
<ol class="steps">
<li><b>C1 or C2?</b><span>C1 is enough for almost every purpose; C2 is an exercise in mastery. <a href="#c1-or-c2">Which to aim for.</a></span></li>
<li><b>Know the sections</b><span>A synthesis and an essay in C1, a 700-word text in C2, a presentation after an hour of preparation. <a href="#c1">The C1</a>, <a href="#c2">the C2</a>.</span></li>
<li><b>Work on the synthesis</b><span>200 to 240 words, no quotations, no opinion: the key C1 task. <a href="#synthesis">The method.</a></span></li>
<li><b>Register in time</b><span>Same centres and same sessions as the DELF — on Thursdays in France; not every centre opens the DALF at every session. <a href="#dates-fees">The calendar and the centres.</a></span></li>
<li><b>Exam day, then the diploma</b><span>Results within 4 to 6 weeks, a diploma for life, and the <a href="#exemption">exemption from French tests</a> it gives you at university.</span></li>
</ol>

<h2 id="c1">The DALF C1 exam format, section by section</h2>
<p>It is the longest exam in the whole DELF-DALF family: <strong>four and a half hours of tests</strong>, plus <strong>an hour of
supervised preparation</strong> before the speaking test.</p>
""" + table("DALF C1 format. Source: France Éducation international, structure checked in July 2026.",
            ["Section", "Content", "Time", "Score"],
            [("Listening", "2 exercises: 1 long document (≈ 8 min, played twice) + several short documents (played once)", "40 min", "/25"),
             ("Reading", "1 exercise: an argumentative text of about 1,000 words", "50 min", "/25"),
             ("Writing", "2 tasks: synthesis of documents (200–240 words) + argumentative essay (250 words min)", "2 h 30", "/25"),
             ("Speaking", "Presentation based on a file of documents, then discussion", "30 min <em>(+ 1 h of preparation)</em>", "/25"),
             ("<strong>Total</strong>", "", "<strong>4 h 30</strong> <em>(+ 1 h of preparation)</em>", "<strong>/100</strong>")],
            wide=False) + """

<p>Two features set the C1 apart from the <a href="/en/delf-b2/">B2</a>, well beyond the difficulty of the language.
First, <strong>reading has only one text</strong>, but an argumentative text of about a thousand words: this is no longer
selective reading, it is analytical reading. Second, the writing section lasts <strong>two and a half hours</strong> and
contains <em>two</em> tasks of a completely different nature — an objective synthesis, then a personal essay. Many
candidates underestimate the mental switch this requires.</p>

<h2 id="c2">The DALF C2: two integrated sections</h2>
<p>The C2 isn’t just “harder”. It changes structure: the four skills are no longer assessed separately but merged into
<strong>two areas</strong>.</p>
""" + table("DALF C2 format. Source: France Éducation international, structure checked in July 2026.",
            ["Area", "Content", "Time", "Score"],
            [("Listening and speaking", "Listening to a document (≈ 14 min, played twice), then a report, a monologue and a debate with the examiners", "30 min <em>(+ 1 h of preparation)</em>", "/50"),
             ("Reading and writing", "Writing a structured text of <strong>700 words minimum</strong> based on a file of about 2,000 words", "3 h 30", "/50"),
             ("<strong>Total</strong>", "", "<strong>4 h</strong> <em>(+ 1 h of preparation)</em>", "<strong>/100</strong>")],
            wide=False) + """

<p>The C2 written paper is the most demanding exercise of the whole system: reading a two-thousand-word file and drawing
from it a structured text of at least seven hundred words, in three and a half hours. It is no longer a language test;
it is a test of thinking in French.</p>

<h2 id="scoring">Scoring and minimum scores</h2>
""" + table("The DALF thresholds, level by level.", ["", "DALF C1", "DALF C2"],
            [("Sections", "4, scored /25", "2 areas, scored /50"),
             ("Pass mark", "<strong>50/100</strong>", "<strong>50/100</strong>"),
             ("Minimum score", "below <strong>5/25</strong> in one section means you fail", "below <strong>10/50</strong> in one area means you fail")],
            wide=False) + """

<p>The mechanism is the same as at the lower levels, but its consequences are harsher at C2: with only two marks,
<strong>a failed section is mathematically impossible to make up for</strong>. A candidate with 45/50 in the spoken
section and 9/50 in the written one — 54 out of 100 — fails, one point short of the minimum.</p>

<h2 id="synthesis">The synthesis: the key C1 task</h2>
<p>The <strong>synthesis of documents</strong> is the section that makes the difference in the DALF C1: rewording, in
<strong>200 to 240 words</strong>, without quoting or judging, the essentials of several documents, with a plan that
cross-references them. Reducing several documents to a single text — objective, entirely reworded and calibrated to the
exact word count — can’t be improvised. It is a <strong>technique</strong>, and that is good news: a technique can be
learned, unlike a level of French, which takes months to rise.</p>

<p>Three absolute rules govern it, and breaking them costs more than any language mistake:</p>

<ul>
<li><strong>No quotations.</strong> Everything must be reworded. Copying even a striking phrase from the original
document is penalised — rewording is precisely the skill being assessed.</li>
<li><strong>No personal opinion.</strong> The synthesis is neutral from start to finish. You don’t exist in this text.
The essay that follows is there for that — and that switch is precisely what candidates most often get wrong.</li>
<li><strong>A plan that cross-references the documents.</strong> This is the real differentiator. Summarising document 1,
then document 2, then document 3 isn’t a synthesis: it is a series of summaries. You need to draw out the common threads
and make the sources talk to each other within each part.</li>
</ul>

<p>Add to that the length constraint: <strong>200 to 240 words</strong>, which is very short for the material to cover.
Counting is part of the exercise, and going well over the upper limit is penalised. The 250-word essay follows the
synthesis, within the same 2 h 30.</p>

<div class="note">
<p><strong>Why this section is so hard to prepare on your own.</strong> You can’t judge your own neutrality, or see that
your plan follows the documents instead of cross-referencing them — those are exactly the flaws that are invisible from
the inside. It is also the level at which a human marker becomes rare and expensive. The AI assessment in our app scores
your syntheses and essays against the official criteria and gives detailed feedback, as many times as you need.</p>
</div>

<h2 id="prepare">How to prepare for the DALF</h2>
<ol>
<li><strong>A full mock exam right at the start.</strong> At C1 as at C2, length is a factor in its own right: keeping up
four hours of dense intellectual work takes physical as much as intellectual preparation.</li>
<li><strong>The synthesis, over and over.</strong> It is the exercise with the best return: a technique you can master in
about ten seriously corrected practice runs, whereas your level of French won’t move in ten sessions.</li>
<li><strong>The synthesis → essay switch.</strong> Practise both tasks back to back, in the real conditions of the two and
a half hours. It is the change of stance — neutrality, then taking a position — that costs points, not each task taken
separately.</li>
<li><strong>The hour of preparation for the speaking test.</strong> It is supervised and needs practising like a section
in its own right: selecting, ranking, noting keywords — not writing out a text you will then read.</li>
<li><strong>Read opinion journalism regularly.</strong> The topics are general but intellectually demanding: social
debates, cultural questions. That is the raw material of all four sections.</li>
</ol>

<h2 id="c1-or-c2">DALF C1 vs C2: which to aim for</h2>
<p><strong>C1</strong> meets almost every requirement — universities, <em>grandes écoles</em>, professional uses;
<strong>C2</strong> is an exercise in mastery that few procedures require. For the vast majority of paths, the answer is
C1: it already opens university and professional doors, and its four-section format lets points offset each
other.</p>

<p>C2 makes sense in three cases: <strong>teaching French</strong>, <strong>translation</strong>, and some competitive
exams or applications where the highest level is a signal in itself. Add personal challenge, which is a perfectly valid
reason — but be aware that going from C1 to C2 isn’t about extra vocabulary: it is about the ability to produce long,
dense, structured discourse from sources.</p>

<p>The two are independent diplomas: you register directly for the level you are aiming for. If your real level is
somewhere between B2 and C1, the safest strategy is to <strong>secure the <a href="/en/delf-b2/">B2</a> first</strong>,
then aim for C1. Both diplomas are yours for life and can be held together with no drawback.</p>

<h2 id="exemption">What the DALF exempts you from</h2>
<p>This is the economic argument for the diploma, and it deserves to be precise rather than general.</p>

<ul>
<li><strong>French universities.</strong> The DALF C1 exempts you from a language test for admission — whereas a DELF B2
may not be enough for some courses. It is the most direct and best-established use.</li>
<li><strong>French citizenship.</strong> Since 1 January 2026, an application for French nationality requires B2. A DALF
C1 or C2, a higher level, proves it <em>a fortiori</em> — and unlike a <a href="/en/tcf-irn/">TCF IRN</a> results
certificate, valid for two years, a diploma never expires.</li>
<li><strong>Immigration to Quebec.</strong> Quebec accepts DELF and DALF diplomas in place of the TCF Québec, but with
conditions — a minimum score in listening and in speaking, and a validity of less than two years. Here, the “for life”
nature of the diploma doesn’t apply.</li>
</ul>

<div class="note">
<p><strong>Beware of generalising.</strong> “The DALF exempts you from everything” is true for university, less clear-cut
elsewhere. Each procedure publishes its own list of accepted proofs, with its own conditions on scores and validity.
Check the list for <em>your</em> procedure before deciding not to take a test.</p>
</div>

<h2 id="dates-fees">DALF dates and fees: France, the UK and the US</h2>
<p><strong>In France</strong>, the DALF is held at the <strong>same 143 approved centres</strong> as the DELF, at the same
sessions — on <strong>Thursdays</strong>, the day after the DELF B1 and B2, with C1 at 9 am and C2 at 2.30 pm — ten times a
year, never in April or September. The autumn 2026 sessions fall on <strong>8 October, 5 November and 3 December</strong>;
in 2027, there are ten sessions from January to December. Not every centre opens the DALF at every session: the centre’s
own calendar is what counts.</p>

<p>Each centre sets its own fee. At the centres we checked on 17 September 2026: €145 at Nantes Université for C1 or C2,
€200 and €210 at the Alliance Française de Lille, €249 (C1) and €290 (C2) at the Sorbonne Nouvelle, €279 (C1) at the
Cours de civilisation française de la Sorbonne, and €290 at the Alliance Française de Paris — so <strong>€145 to
€290</strong> for the C1. Results arrive within 4 to 6 weeks. Our directory of the 143 centres in France and our guide to
where to take the DELF and DALF in France are in French.</p>

<p><strong>In the UK and the US</strong>, the next DELF-DALF session is in December 2026 — from 7 to 11 December in the US.
The dates, centres and fees for the C1 and the C2 are on our <a href="/en/delf-uk/">DELF in the UK</a> and
<a href="/en/delf-usa/">DELF in the USA</a> pages, checked on 8 October 2026.</p>
""" + CHIPS,
    cta_h2=CTA_DELF_H2,
    cta_p="""Timed mock exams in the DALF C1 and C2 formats, scored on the official scales, with AI feedback on the synthesis,
the essay and the speaking test against the official criteria — in the “TCF DELF TEF: Tests 2026” app.""",
    faq=[("What is the DALF C1 exam?", "The DALF — diplôme approfondi de langue française — is the official diploma of France’s Ministry of National Education for levels C1 and C2 of the Common European Framework: two independent diplomas, awarded by France Éducation international at the same centres and sessions as the DELF, and valid for life. The C1 has four sections scored out of 25, in 4 hours plus 1 hour of preparation; you pass from 50/100."),
         ("DALF C1 vs C2: what is the difference, and is C2 worth it?", "C1 has four sections scored out of 25 — listening, reading, writing (a synthesis, then an essay) and speaking — and lets points offset each other; C2 has only two integrated sections scored out of 50, a spoken one and a written one of 700 words minimum. For most paths, C2 isn’t worth the investment: C1 already opens every university and professional door. C2 makes sense for teaching French, translation, some competitive exams, or as a personal challenge."),
         ("Do you need the DELF B2 before taking the DALF?", "No: each diploma is independent. You can register directly for C1, or even C2, without having taken the levels below."),
         ("How long is the DALF C1 exam?", "4 h 30 of tests, plus 1 hour of supervised preparation before the speaking test: 40 minutes of listening, 50 minutes of reading, 2 h 30 of writing and 30 minutes of speaking. It is the longest exam in the DELF-DALF family."),
         ("What score do you need to pass the DALF?", "50 out of 100 in both cases. In C1, the four sections are scored out of 25, and a score below 5 out of 25 in any section means you fail. In C2, the two areas are scored out of 50, and the minimum is 10 out of 50 per area."),
         ("What is the DALF C1 synthesis?", "The first of the two writing tasks: reducing several documents to a single text of 200 to 240 words, objective and entirely reworded. Three rules govern it: no quotations, no personal opinion, and a plan that cross-references the documents instead of summarising them one after another. It is followed by an argumentative essay of 250 words minimum."),
         ("Do you have to choose a specialism for the DALF?", "No, not any more: the old options — humanities and social sciences versus sciences — have been abolished. The topics remain general but intellectually demanding: opinion journalism, social debates, cultural questions."),
         ("DALF C1 or DELF B2 for a university application?", 'B2 is enough for most courses; C1 is required by some demanding courses and always makes a difference in selection. If your real level is between the two, secure the <a href="/en/delf-b2/">B2</a> first, then aim for C1: both diplomas are yours for life and can be held together without any problem.'),
         ("Does the DALF exempt you from the TCF or the TEF?", "For admission to French universities, the DALF C1 exempts you from a language test. For immigration procedures, it is less clear-cut: a DALF proves a fortiori the B2 level required for French citizenship, and Quebec accepts DELF and DALF diplomas in place of the TCF Québec, subject to conditions on scores and validity. Always check the list of accepted proofs for your specific procedure before deciding not to take a test."),
         ("Is the DALF useful for French citizenship?", "It amply proves the B2 required, but it isn’t necessary: the DELF B2 is enough for the language requirement. The DALF is mainly aimed at university and professional uses."),
         ("When are the DALF exam dates?", "In France, the DALF is held on the Thursday of each national session — C1 at 9 am, C2 at 2.30 pm: in autumn 2026, on 8 October, 5 November and 3 December; in 2027, ten sessions from January to December. Not every centre opens the DALF at every session: the centre’s calendar is what counts. In the UK and the US, the next session is in December 2026 — from 7 to 11 December in the US."),
         ("How much does the DALF cost?", "There is no national fee. In France, at the centres we checked on 17 September 2026: €145 at Nantes Université for C1 or C2, €200 and €210 at the Alliance Française de Lille, €249 (C1) and €290 (C2) at the Sorbonne Nouvelle, €279 (C1) at the Cours de civilisation française de la Sorbonne, €290 at the Alliance Française de Paris. For the UK and the US, see our country pages.")],
    also=[("/en/delf-b2/", "DELF B2 exam: format, scoring, dates", "The level below: the reformed format, scoring out of 100 and the method, section by section."),
          ("/en/french-citizenship-b2/", "French citizenship: the B2 level", "What has changed since 1 January 2026: B2 in speaking and in writing, the civics exam, the transitional rules."),
          ("/en/delf-b1/", "DELF B1 exam and the resident card", "The levels required procedure by procedure, and the proofs accepted.")],
    sources="""<strong>Formats change.</strong> This page is up to date as of 7 August 2026; the dates and fees for France were
checked on 17 September 2026. Exam structures and institutions’ requirements change regularly — check the format on
<a href="https://www.france-education-international.fr/diplome/dalf" rel="noopener">france-education-international.fr</a>
and the admission conditions with the institution or authority concerned before you register.""",
))


# ===========================================================================
# DELF B2 — practice test (from /blog/exercices-delf-b2/, with the writing method of /blog/production-ecrite-delf-b2/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/exercices-delf-b2/", lang="en", variant="en-GB", slug="delf-b2-practice-test", accent="accent-delf",
    crumbs=[HOME], crumb="DELF B2 practice test",
    title="DELF B2 practice test and sample papers, with answers",
    desc="DELF B2 practice test: one exercise per section with answers — listening, reading, writing, speaking — plus the writing method and the 5/25 minimum score.",
    h1="DELF B2 practice test: the four sections, with answers",
    intro="""Four sections scored out of 25, a total out of <strong>100</strong>, a pass at <strong>50/100</strong> — and a
score below <strong>5/25</strong> in any one section that fails you, whatever your total. Since the reform, listening
and reading are <strong>100% multiple-choice</strong>. Here is one exercise per section, with the answers explained,
then the method for the writing test, the section that separates candidates most.""",
    facts=["<strong>4 sections out of 25</strong> · total out of <strong>100</strong> · pass at <strong>50/100</strong>.",
           "⚠️ <strong>Below 5/25</strong> in a single section = <strong>fail</strong>.",
           "<strong>Listening 30 min · reading 60 min · writing 60 min · speaking 20 min</strong> (+ 30 min of preparation).",
           "Since the reform: listening and reading <strong>100% multiple-choice</strong>, guided interview <strong>removed</strong> from the speaking test.",
           "⚠️ In listening, the first 2 exercises are played <strong>twice</strong>, the 3rd only once.",
           "Writing: <strong>250 words minimum</strong>, in one of three genres — a contribution to a debate, a formal letter, a critical article."],
    toc=[("format", "The format of the four sections"), ("exercises", "One exercise per section, with answers"),
         ("minimum-score", "The minimum score changes the strategy"), ("method", "The method"),
         ("writing-assessed", "Writing: what the examiner really assesses"), ("plan", "The plan that works"),
         ("genres", "The three genres and what they require"), ("mistakes", "The five most costly mistakes"),
         ("timing", "How to split the 60 minutes")],
    body="""
<h2 id="format">The format of the four sections</h2>
""" + table("DELF B2, format from the 2020 reform, in place everywhere since September 2024. Source: France Éducation international.",
            ["Section", "Content", "Time", "Score"],
            [("Listening", "3 exercises / 5 audio documents", "30 min", "/25"),
             ("Reading", "3 exercises / 5 written documents", "60 min", "/25"),
             ("Writing", "1 task, 250 words minimum", "60 min", "/25"),
             ("Speaking", "Sustained monologue + debate", "20 min <em>(+ 30 min of preparation)</em>", "/25")],
            wide=False) + """

<div class="note">
<p><strong>Beware of out-of-date past papers.</strong> If a document mentions a guided interview in the speaking test or
open questions in listening or reading, it describes an exam that no longer exists. A large share of the resources
online predate the reform.</p>
</div>

<h2 id="exercises">One exercise per section, with answers</h2>
<p>The recordings, documents, questions and topics are in French, as on exam day; the answers and what the examiner
expects are explained underneath.</p>
""" + exo("en", 1, "B2 — listening", "Interview",
          "« <strong>Journaliste :</strong> Vous êtes spécialiste en santé publique. La question de la santé "
          "mentale des jeunes est devenue un sujet majeur en France. Pouvez-vous nous en dire plus ?<br>"
          "<strong>Docteur Martin :</strong> Oui, effectivement, nous observons une augmentation très "
          "préoccupante des troubles psychiques chez les 15-25 ans depuis la pandémie de Covid-19. Les "
          "consultations pour anxiété et dépression ont augmenté de 40 % entre 2019 et 2024 dans cette "
          "tranche d'âge. Les tentatives de suicide chez les adolescentes ont doublé. »",
          "Quelle augmentation note-t-on pour les troubles ?",
          ["Une hausse de 20 % en cinq ans", "Une hausse de 80 % en cinq ans",
           "Une hausse de 40 % entre 2019 et 2024", "Une hausse de 60 % entre 2019 et 2024"],
          """C — <span lang="fr">Une hausse de 40 % entre 2019 et 2024</span> (a 40% rise between 2019 and 2024)""",
          "a spotting question, but with two close figures in the document: the 40% refers to the consultations, "
          "« doublé » (doubled) to suicide attempts. <strong>Always check what a figure refers to</strong> before you "
          "tick — it is the most common distraction mechanism.",
          audio="delf_co_001.m4a", duree="1 min 46 s", ecoutes=2) + exo(
    "en", 2, "B2 — reading", "Document — press article:",
    "« <strong>La transition écologique en France : un défi collectif.</strong> Depuis l'Accord de "
    "Paris en 2015, la France s'est engagée dans une transformation profonde de son modèle économique "
    "et énergétique. Le plan national bas-carbone fixe des objectifs ambitieux : réduire les émissions "
    "de gaz à effet de serre de 40 % d'ici 2030 par rapport aux niveaux de 1990. Mais entre les "
    "annonces politiques et la réalité du terrain, le fossé reste considérable. »",
    "Quel est le but principal de cet article ?",
    ["Favoriser les initiatives locales sur le plan national",
     "Célébrer les succès climatiques français récents",
     "Comparer la France aux autres pays européens",
     "Montrer les contradictions sociales de la transition"],
    """D — <span lang="fr">Montrer les contradictions sociales de la transition</span> (to show the social contradictions of the transition)""",
    "the question is about the <strong>author’s intention</strong>, not the content. The pivot is « Mais »: the "
    "article states the objectives the better to expose the gap with reality. Option B is the expected misreading — "
    "a hurried reader remembers the « objectifs ambitieux » and concludes that the article is a celebration.") + \
    sujet("en", "Writing", "60 minutes · 250 words minimum · scored out of 25",
          "Vous habitez dans une ville où la mairie a décidé de supprimer plusieurs lignes de bus pour des "
          "raisons budgétaires. En tant que président(e) d'une association de quartier, vous écrivez au "
          "maire pour protester contre cette décision. Vous expliquez les conséquences pour les habitants "
          "et vous proposez des solutions alternatives.",
          "<strong>Three constraints combine here</strong>: the genre (a formal letter, so a greeting, a subject "
          "line and a sign-off), the role (you are writing in your official capacity, not in your own name), and "
          "the two actions required (explaining the consequences <em>and</em> proposing alternatives). Leaving out the "
          "proposals is the most frequent mistake: candidates protest but offer no alternative. 250 words is a "
          "floor.") + \
    sujet("en", "Speaking", "30 minutes of preparation · 20 minutes in front of the examiners · scored out of 25",
          "Vous dégagerez le problème soulevé par le document ci-dessous. Vous présenterez votre opinion sur "
          "le sujet de manière argumentée, puis vous la défendrez face à l'examinateur lors d'un débat.",
          "The test starts <strong>straight away with the monologue</strong>: the guided interview, which used to help "
          "you relax, was removed by the reform. The 30 minutes of preparation are for building a plan and noting "
          "keywords, not for writing — a candidate who reads their notes is easy to spot. In the second part, "
          "<strong>the examiners don’t agree with you, and that is deliberate</strong>: their role is to test your "
          "ability to hold a position while qualifying it. Abandoning your argument at the first objection costs "
          "points.") + """

<h2 id="minimum-score">The minimum score changes the strategy</h2>
""" + table("The two DELF B2 thresholds.", ["Rule", "Threshold", "Effect"],
            [("Overall score", "<strong>50/100</strong>", "Below it, you fail"),
             ("Minimum score per section", "<strong>5/25</strong>", "Below it in <em>a single</em> section, you fail — even with 60/100")],
            wide=False) + """

<p>The consequence is counter-intuitive: <strong>a very weak skill costs you more than a strong one earns you</strong>. A
candidate with 20/25 in reading and 4/25 in speaking fails, even though their total is above the pass mark. So your first
job is not to improve where you are already good, but to <strong>get your weakest section out of the danger
zone</strong>.</p>

<h2 id="method">The method</h2>
<ol>
<li><strong>A full mock exam right at the start</strong>, scored on the official scales, to identify the section that
could make you fail.</li>
<li><strong>Get that section out of the danger zone</strong> before anything else.</li>
<li><strong>Work on the writing test through structure</strong>, not vocabulary: most lost points come from the plan, the
genre and the instructions.</li>
<li><strong>Simulate the speaking test in real conditions</strong>, with the 30 minutes of preparation and someone
deliberately contradicting you in the second part.</li>
<li><strong>Beware of out-of-date resources</strong>: always check the date of whatever you practise on.</li>
</ol>

<h2 id="writing-assessed">Writing: what the examiner really assesses</h2>
<p><strong>One task, 60 minutes, 250 words minimum.</strong> The writing test is the third group section of the
<a href="/en/delf-b2/">DELF B2</a>, right after listening and reading — so you reach it after an hour and a half of the
exam, a detail that matters for managing your energy. And since listening and reading became entirely multiple-choice,
it is <strong>the only section in which you write</strong> before the speaking test: everything to do with written
expression is played out there, on a single paper. It is the section where the gap between a good level of French and a
good mark is widest — and what it takes can be learned much faster than a level of French.</p>

<p>Here lies the central misunderstanding. The topic asks for a <strong>personal position</strong>, and many candidates
conclude that the relevance of their opinion is being judged. It isn’t: <strong>your opinion is neither right nor
wrong</strong>. What is assessed is how you build it. In practice, five dimensions:</p>

<ul>
<li><strong>Following the instructions and the genre.</strong> A formal letter with no greeting and no letter
structure loses points before the first sentence is even assessed for language. It is the easiest point to secure, and
the most often neglected.</li>
<li><strong>The structure of the argument.</strong> A clear position, ranked arguments, and above all <strong>taking the
opposing objection into account</strong>. That is the marker of B2: at B1, you give your opinion; at B2, you defend it
against an objection.</li>
<li><strong>Logical connectors.</strong> The most visible signal of your level, and the most rewarding to work on
mechanically — a few hours are enough to build a solid repertoire.</li>
<li><strong>Register.</strong> An unnoticed slide into casual language is a frequent loss of points for candidates who
speak French well day to day.</li>
<li><strong>Length.</strong> 250 words minimum. Below it, task completion is marked down, whatever the quality of the
language.</li>
</ul>

<div class="note">
<p><strong>None of these five dimensions is a vocabulary problem.</strong> That is the good news about this section: most
lost points come from the plan, the genre and the instructions — things you can fix in a few sessions, not a few
months.</p>
</div>

<h2 id="plan">The plan that works</h2>
<p>There is no official set plan. But one structure meets every expectation of B2 and saves you from thinking about
organisation on the day.</p>

<ol>
<li><strong>Introduction (30–40 words).</strong> You restate what is at stake and announce your position. No suspense: at
B2, the examiner must know where you are going from the first sentence.</li>
<li><strong>First argument (60–70 words).</strong> Your strongest reason, illustrated with a concrete example. An argument
without an example remains an assertion.</li>
<li><strong>Second argument (60–70 words).</strong> A reason of a different kind from the first — if the first is
economic, take a social or practical angle. Two arguments of the same type count as one.</li>
<li><strong>Concession and rebuttal (50–60 words).</strong> <strong>This is the paragraph that makes the
difference.</strong> You acknowledge the strength of the opposing objection, then explain why it doesn’t overturn your
position. Many papers leave it out entirely — and hit a ceiling.</li>
<li><strong>Conclusion (30–40 words).</strong> You restate your position and open up the topic, without introducing a new
idea.</li>
</ol>

<p>Total: about 250 to 280 words. The plan produces the expected length mechanically — but still count
your words.</p>

<h2 id="genres">The three genres and what they require</h2>
""" + table("What each genre requires on top of the argument.", ["Genre", "What it requires"],
            [("<strong>Contribution to a debate</strong><br><em>forum, letters to the editor</em>", "Addressing a community, placing what you say within an ongoing exchange"),
             ("<strong>Formal letter</strong>", "Greeting, subject line, letter structure, sign-off, formal register kept up from start to finish"),
             ("<strong>Critical article</strong>", "A title, a hook, a journalistic tone — and a position you stand by")],
            wide=False) + """

<p>The formal letter is where most points are lost for nothing, because the examiner can check its conventions
mechanically. Learn them once: greeting, subject line, structured body, sign-off. They are yours for life
and come up in almost every French exam.</p>

<h2 id="mistakes">The five most costly mistakes</h2>
<ol>
<li><strong>Writing fewer than 250 words.</strong> The penalty is on task completion, regardless of quality. Actually count
your words — an estimate by eye is almost always optimistic.</li>
<li><strong>Leaving out the concession.</strong> Without taking the opposing objection into account, your paper remains a
string of opinions, not a B2-level argument.</li>
<li><strong>Ignoring the genre asked for.</strong> An excellent argumentative text that should have been a formal letter
loses structural points it can’t recover.</li>
<li><strong>Piling up arguments without linking them.</strong> Three correct ideas placed side by side are worth less than
two ideas linked by an explicit progression.</li>
<li><strong>Skipping the final reread.</strong> Agreements, tenses and punctuation take five minutes to correct and cost
dearly if they stay.</li>
</ol>

<h2 id="timing">How to split the 60 minutes</h2>
""" + table("A split that leaves time for a real reread.", ["Time", "What you do"],
            [("<strong>0–10 min</strong>", "Analyse the instructions, identify the genre, set out the plan and the two arguments with their examples"),
             ("<strong>10–45 min</strong>", "Write in one go, without going back"),
             ("<strong>45–52 min</strong>", "Count the words, check that the concession is there and that the genre is respected"),
             ("<strong>52–60 min</strong>", "Reread for language: agreements, tenses, punctuation, register")],
            wide=False) + """

<p>The first ten minutes are counter-intuitive: it feels like wasted time. Yet it is the only moment when you can still
change the structure of your paper without rewriting everything. A plan set out in ten minutes saves far more than ten
minutes of writing.</p>

<div class="note">
<p><strong>Why this section is hard to prepare for on your own.</strong> You can’t judge whether your concession is real
or merely announced, or whether your register has slipped — those are precisely the flaws that are invisible from the
inside. And the gap between 9 and 13 out of 25, which often decides whether you pass, doesn’t show when you reread. That
is what marking against the official criteria solves.</p>
</div>
""",
    cta_h2="First, get out of the danger zone",
    cta_p="""Mock exams in the reformed DELF B2 format, scored on the official scale out of 25 per section with a warning
when you fall below the minimum score, and AI feedback on writing and speaking against the official criteria. In the
“TCF DELF TEF: Tests 2026” app.""",
    faq=[("What score do you need to pass the DELF B2?", "50 out of 100. The four sections are scored out of 25 each. Watch out for the rule that fails candidates whose average was enough: a score below 5 out of 25 in any single section means you fail, whatever your total — it is the only minimum per section, in the writing test as in the others."),
         ("Are the DELF B2 listening and reading questions multiple choice?", "Yes, 100% since the reform. Open questions and true/false with justification have gone from both sections. So you no longer write anything in them — which changes how you manage your time, but also removes the chance of picking up points with a partly correct justification."),
         ("How many times do you hear the recordings in the DELF B2?", "It depends on the exercise. The first two exercises, based on long radio documents, are played twice. The third, which strings together three short documents, is played only once. This asymmetry catches candidates out just when their concentration is already flagging."),
         ("How many words do you write in the DELF B2 writing test?", "250 words minimum, in a single task, in 60 minutes. It is a floor, not a target: writing less costs you points on task completion, whatever the quality of your French. A five-part plan produces 250 to 280 words mechanically."),
         ("What kinds of DELF B2 writing topics come up?", "Three genres: a contribution to a debate (a forum, letters to the editor), a formal letter or a critical article. In every case, the topic asks for a reasoned personal position. The formal letter is where most points are lost for nothing, by not following its conventions."),
         ("Does the examiner judge my opinion?", "No. Your opinion is neither right nor wrong: what is assessed is how you build it — following the instructions and the genre, the structure of the argument, logical connectors, register and length. None of these is a vocabulary problem."),
         ("What is the difference between B1 and B2 in writing?", "Taking the opposing objection into account. At B1, you give your opinion; at B2, you defend it against an objection you have first acknowledged. The concession-and-rebuttal paragraph is most often what makes the difference — and many papers leave it out entirely."),
         ("How should I split the 60 minutes of the writing test?", "About 10 minutes to analyse the instructions and set out the plan, 35 minutes to write in one go, 7 minutes to check the length, the concession and the genre, and 8 minutes to reread for language. The first 10 minutes seem wasted, yet they are the only moment when you can still change the structure without rewriting everything."),
         ("Is there still a guided interview in the DELF B2 speaking test?", "No, it was removed by the reform. The test now starts straight away with the sustained monologue, followed by the debate with the examiners. The warm-up that used to help you relax no longer exists at B2 — it does remain in the DELF B1."),
         ("Are the examiners supposed to agree with me?", "No, and that is deliberate. In the second part of the speaking test, the examiners contradict you to test your ability to hold a position, to qualify it and to concede without giving in. Candidates who abandon their argument at the first objection lose points on the skill being assessed."),
         ("Can I practise with old DELF B2 sample papers?", "Check their date first. The current format comes from the 2020 reform and has been in place everywhere since September 2024: if a paper mentions a guided interview in the speaking test, or open questions in listening or reading, it describes an exam that no longer exists — and a large share of the resources online predate the reform. The exercises on this page are original content from our app, in the reformed format.")],
    also=[("/en/delf-b2/", "DELF B2 exam: format, scoring, dates", "The complete guide to the reformed format and the two thresholds."),
          ("/en/dalf-c1/", "DALF C1: the synthesis of documents", "The level above: reducing several documents to an objective text of 200 to 240 words."),
          ("/en/french-citizenship-b2/", "French citizenship: the B2 level", "What has changed since 1 January 2026: B2 in speaking and in writing, the civics exam, the transitional rules.")],
    sources="""<strong>Formats change.</strong> This page is up to date as of 7 August 2026 and describes the format that came out
of the 2020 reform, fully in place since September 2024; beware of older past papers and tutorials, which describe a
different exam. The exercises and topics shown are original content from our app. Check the current format on
<a href="https://www.france-education-international.fr/diplome/delf-tout-public" rel="noopener">france-education-international.fr</a>
before your session.""",
))

# Traductions en-GB (08/10/2026) pour les anglophones qui vivent en France : nationalité, titres de séjour, TCF IRN,
# examen civique. Aucun fait nouveau : chaque chiffre, date et règle vient des pages françaises publiées, avec sa date.
# Fusions : french-citizenship-b2 = naturalisation-2026-niveau-b2 (+ b1-ou-b2-nationalite-francaise et
# carte-de-resident-b1-2026 : tableau tests/diplômes, présentiel, piège du renouvellement, décret ou mariage, barème
# TEF IRN, timbres, ressortissants algériens, tentatives illimitées de l'examen civique) ; tcf-irn = /tcf-irn/ +
# niveaux/ + format/ + prix-inscription/ ; french-civics-test = ou-passer-l-examen-civique (+ liste FEI du 19/09
# de centres/examen-civique-france, et « en français », « valeurs, institutions, histoire » des deux guides ci-dessus).


# ===========================================================================
# FRENCH CITIZENSHIP — B2 (from /blog/naturalisation-2026-niveau-b2/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/naturalisation-2026-niveau-b2/", lang="en", variant="en-GB", slug="french-citizenship-b2",
    crumbs=[HOME], crumb="French citizenship: B2", accent="accent-irn",
    title="French citizenship language requirement 2026: B2",
    desc="Since 1 January 2026, French citizenship requires B2 French in speaking and writing (B1 before), plus a civics test. Which tests count, who is affected.",
    h1="French citizenship in 2026: B2 French is now required",
    intro="""Since <strong>1 January 2026</strong>, applying for French citizenship (<em lang="fr">naturalisation</em>)
requires proof of French at <strong>B2</strong> level, <strong>in both speaking and writing</strong>. The level required
before was B1. On top of that comes a <strong>civics test</strong> on the values and institutions of the Republic.
Complete applications submitted before 31 December 2025 are still assessed under the old rules.""",
    facts=["Citizenship: <strong>B2</strong> required since 1 January 2026 (B1 before).",
           "B2 covers <strong>speaking and writing</strong>, whereas the old B1 requirement covered speaking only.",
           "A <strong>civics test</strong> (<em lang=\"fr\">examen civique</em>) becomes compulsory, on top of the language "
           "test: 40 questions, 32 correct answers to pass.",
           "Transitional rule: a <strong>complete application submitted before 31 December 2025</strong> = old rules.",
           "Two other levels change at the same time: <strong>B1</strong> for the resident card (<em lang=\"fr\">carte de "
           "résident</em>), <strong>A2</strong> for the first multi-year residence permit (<em lang=\"fr\">carte de séjour "
           "pluriannuelle</em>).",
           "<strong>62,235</strong> acquisitions of French nationality in 2025, down 6.8% (source: Ministry of the Interior)."],
    toc=[("what-changes", "What exactly has changed"), ("three-levels", "Don’t mix up the three levels"),
         ("proof", "How to prove your B2 level"), ("civics", "The civics test"),
         ("transition", "Who is affected: the transitional rule"), ("b1-to-b2", "How long to get from B1 to B2")],
    body="""
<h2 id="what-changes">What exactly has changed</h2>
<p>The reform that stems from the immigration law of 26 January 2024 raises the level of French expected at each stage
of the integration path. For citizenship, two changes add up — and the second is often overlooked.</p>

<p><strong>First change: the level goes up a notch</strong>, from B1 to B2 on the scale of the Common European Framework
of Reference for Languages (CEFR).</p>

<p><strong>Second change, more demanding in practice: the scope widens.</strong> The old B1 requirement covered speaking.
The new B2 requirement covers speaking <em>and</em> writing. In other words, an applicant who spoke well but wrote poorly
could meet the old condition; that is no longer the case. For many applications, this — not the move from B1 to B2 — is
the real jump.</p>

<p>In concrete terms, B2 means being able to understand the main content of concrete or abstract topics, to interact
with a native speaker with spontaneity and ease, and to produce clear, detailed text on a wide range of subjects.</p>

<p>The requirement is the same whether you apply for citizenship by decree or through marriage, and the level is measured
on all <strong>four tests</strong> — listening, reading, writing and speaking.</p>

<h2 id="three-levels">Don’t mix up the three levels</h2>
<p>It is the most widespread mistake on this subject, including in press articles: the reform sets <strong>three
different levels for three different procedures</strong>. Mixing them up can lead you to take the wrong exam.</p>
""" + table("Levels of French required before and since 1 January 2026. Source: reform under the immigration law of 26 January 2024.",
            ["Procedure", "Before 2026", "Since 1 January 2026"],
            [("First multi-year residence permit", "No level required", "<strong>A2</strong>"),
             ("Resident card (10 years)", "A2", "<strong>B1</strong>"),
             ("French citizenship", "B1 (speaking)", "<strong>B2</strong> (speaking and writing)")], wide=False) + """
<p>If your immediate goal is the resident card rather than citizenship, <strong>B1</strong> is the level to aim for —
our article on the B1 required for the resident card since January 2026 is in French. B2 only concerns applications for
French citizenship.</p>

<div class="note">
<p><strong>The resident card trap.</strong> Moving from a multi-year residence permit to a resident card <strong>is not a
renewal</strong>: it is a <em>first issue</em> of a resident card. B1 and the civics test are therefore required, even if
you have lived in France for years with a valid permit. Renewing a resident card, on the other hand, requires
neither.</p>
</div>

<p>The costs have risen too: the tax stamp (<em lang="fr">timbre fiscal</em>) for a first resident card has cost
<strong>€350</strong> since 1 May 2026, up from €225, and the naturalisation fee has gone up to <strong>€255</strong>
(€127.50 in French Guiana).</p>

<h3>“I have B1 — can I apply for citizenship?”</h3>
<p>It is the most frequent question, and the answer is <strong>no</strong> for any application submitted since 1 January
2026. B1 used to be enough; it isn’t any more. You now need B2, <strong>in both speaking and writing</strong>.</p>
<p>The words “speaking <em>and</em> writing” aren’t decorative. Many applicants have fluent spoken French, picked up over
years of living in France, and writing that has stayed at B1 — because they have never had to write an argued text. Yet
the level is measured on all four tests.</p>
<p>Your B1 isn’t wasted, though: it is exactly what you need for a first resident card. If your path goes through that
step before citizenship, you already have the level for the first, and one more step to climb for the second.</p>

<h2 id="proof">How to prove your B2 level</h2>
<p>There are two kinds of proof: <strong>tests</strong>, which give you a results certificate with limited validity, and
<strong>diplomas</strong>, which are yours for good.</p>
""" + table("The two ways to prove your level of French.",
            ["", "Tests", "Diplomas"],
            [("Which ones", '<a href="/en/tcf-irn/">TCF IRN</a> · TEF IRN', '<a href="/en/delf-b2/">DELF</a> · DALF'),
             ("Length", "1 h 30 to 1 h 35", "2 h 10 to 4 h 30, depending on the level"),
             ("Validity", "<strong>2 years</strong>", "<strong>for life</strong>"),
             ("Designed for", "these administrative procedures", "academic and professional use")], wide=False) + """
<p>The tests designed specifically for these administrative procedures are the <strong>TCF IRN</strong>, from France
Éducation international, and the <strong>TEF IRN</strong>, from Le français des affaires (CCI Paris Île-de-France). IRN
stands for “Intégration, Résidence, Nationalité” (integration, residence, nationality): these versions replaced
<em>two</em> former separate tests, the TCF ANF (for access to French nationality) and the TCF CRF (for the resident
card), merged into a single test. They are shorter, with more frequent sessions and quick results; our
<a href="/en/tcf-irn/">TCF IRN page</a> details the format. Diplomas mean a longer exam, but they <strong>never
expire</strong>.</p>

<p>An important point, often badly worded: a DELF B2 doesn’t “give” you French citizenship. It lets you <strong>meet the
language condition</strong>, which is only one of the conditions for citizenship, alongside residence, lawful stay,
assimilation and resources.</p>

<p>An order of 22 December 2025 also governs which certifications are accepted: beyond the level, the certification must
in particular be <strong>registered in France compétences’ specific register</strong> (<em lang="fr">répertoire
spécifique</em>). And the test must be taken <strong>in person</strong>: the order requires four separate tests, on the
same day, in a single session, with anti-fraud supervision and an identity check. Tests taken online from home are not
accepted — one more reason to check that a test bought online is accepted before you take it.</p>

<p>On the diploma side, a <a href="/en/delf-b2/">DELF B2</a> directly proves the required level. A DALF C1 or C2, at a
higher level, proves it all the more. These diplomas are awarded for life, which makes them the safest option if your
administrative path is going to stretch over several years.</p>

<div class="note">
<p><strong>The calculation that saves hundreds of euros.</strong> A TCF or TEF certificate dies after 2 years; a diploma
doesn’t. If your plan is a resident card now and citizenship in a few years, taking a DELF B2 straight away covers both
procedures, with no test to retake or pay for again. A TCF at B1 taken in 2026 will be out of date in 2028.</p>
</div>

<p><strong>On the TEF IRN, there is no overall score</strong>: each test is scored separately, and the level is
awarded under a double rule. B2 requires at least <strong>400 points in three tests</strong> and at least
<strong>367 in the fourth</strong> (for B1: 300 and 267), according to Le français des affaires’ TEF IRN page,
consulted on 27 July 2026. Aiming for an average without looking at your weakest test is a mistake.</p>

<div class="note">
<p><strong>Check before you pay for registration.</strong> The exact list of accepted proofs, how long they are valid and
the cases of <strong>exemption</strong> (age, health, a diploma obtained at a French-speaking institution, refugee status)
depend on implementing texts that may still be clarified. Don’t rely on a blog article — ours included — for this
precise point: confirm on <a href="https://www.service-public.fr/particuliers/vosdroits/F2213" rel="noopener">service-public.fr</a>
or with the platform handling your application. Registering for an exam costs anywhere from several tens to several
hundreds of euros; checking takes five minutes.</p>
</div>

<h2 id="civics">The civics test</h2>
<p>It is the least discussed new requirement, and it catches many applicants off guard: since 1 January 2026, a
<strong>civics test</strong> on knowledge of the values and institutions of the Republic has been added to the
conditions. It applies to citizenship, but also to the resident card and the first multi-year residence permit.</p>

<p>It is a test <strong>separate from the language test</strong>: passing the TCF IRN or the TEF IRN doesn’t exempt you
from it, and vice versa. You prepare for it separately, on a civic-culture programme — institutions, symbols, republican
principles, rights and duties.</p>

<p>A concrete point that is rarely mentioned: for the “citizenship” version, the order of 10 October 2025 sets the pass
mark at <strong>80% correct answers</strong> — <strong>32 out of 40 questions</strong>, in 45 minutes at most. It is a
high bar that leaves no room for improvisation: you revise for the civics test; you can’t guess your way through it.
Format, centres and fees: <a href="/en/french-civics-test/">the French civics test</a>.</p>

<div class="note">
<p><strong>For this part of the application, we have a dedicated app.</strong>
<a href="https://naturalisationfrancefacile.fr">Naturalisation France Facile</a>, our sister app, prepares the civics
test: institutions, symbols, republican principles, rights and duties, with multiple-choice questions in the test format
— <a href="https://apps.apple.com/app/id6761140087">available on the App&nbsp;Store</a>. The “TCF DELF TEF: Tests 2026”
app covers the language test; between them, the two apps cover both conditions.</p>
</div>

<div class="note">
<p><strong>What no official text sets.</strong> No official text sets the fee for the civics test — neither the order of
10 October 2025 nor the matching Service-Public pages. Be wary of sites that announce a precise price, and ask your test
centre: each centre sets its own, from €70 to €110 at the centres we checked on 17 September 2026. As for attempts, the
Ministry of the Interior says the test can be taken “at any time and as many times as necessary” — each attempt is paid
for.</p>
</div>

<h2 id="transition">Who is affected: the transitional rule</h2>
<p>The rule is simple, but its condition less so: <strong>complete</strong> applications submitted <strong>before
31 December 2025</strong> continue to be assessed under the previous rules. The word that matters is “complete”.</p>

<p>An application submitted in 2025 but missing a document isn’t necessarily protected by this transitional rule. If you
are in that situation, get written confirmation of the date your complete application was registered: that date
determines which rules apply, and so the level of French you will be held to.</p>

<p>Don’t rely on a quick reading either: “submitted” doesn’t mean “prepared”, nor “appointment booked”. If in doubt about
your exact situation — an application being processed, an appointment made before the deadline but the actual submission
after it — ask the prefecture or the platform handling your application to confirm.</p>

<div class="note">
<p><strong>Algerian nationals: residence isn’t citizenship.</strong> Some prefectures (Loiret, Côte-d’Or) say the new
requirements for residence permits don’t apply to Algerian nationals, whose stay is governed by the Franco-Algerian
agreement of 27 December 1968. The legal reasoning holds, but no national source confirms it explicitly: ask your
prefecture for written confirmation. And that exemption covers
<strong>residence</strong>, not <strong>citizenship</strong>: an Algerian applicant for French citizenship must prove B2
and pass the civics test in its citizenship version.</p>
</div>

<h2 id="b1-to-b2">How long to get from B1 to B2</h2>
<p>The step from B1 to B2 is reputed to be the longest on the CEFR scale. It is the point where you stop progressing by
piling up vocabulary and have to gain grammatical precision, nuance and ease. Language centres’ usual estimates are
around <strong>150 to 200 hours</strong> of work — count on 4 to 6 months of regular practice — but this varies
enormously with your mother tongue, your daily exposure to French and how regularly you work.</p>

<p>At B1, understanding and narrating are enough. At B2, you have to argue, defend a point of view and understand abstract
documents. One thing is certain: <strong>writing is the weak point of most applicants</strong> in this situation,
precisely because the old B1 requirement didn’t assess it. Many people who are perfectly at ease speaking discover how
far behind their writing is on exam day.</p>

<p>Hence the only really reliable way to find out where you stand: <strong>a full, timed mock exam</strong> at the start
of your preparation, rather than at the end. It doesn’t tell you “your level” in general, but your level <em>test by
test</em> — and it is your weakest test that caps your application.</p>

<p>The context, to put the stakes in perspective: France recorded <strong>62,235 acquisitions of French nationality in
2025</strong>, down 6.8% in a year, according to figures published by the Ministry of the Interior on 27 January 2026.
The tightening of the language criteria comes on top of an already more selective context.</p>

<p>Where to take the test or the diploma? The TCF IRN runs almost every week in Paris, at seven approved centres, for €140
to €220 — see <a href="/en/tcf-irn/#where">where to take the TCF IRN</a>; the DELF B2, valid for life, ten times a year at
143 centres, with registration windows that close weeks before the written exams (our guide to the DELF in France is in
French). And for the civics test — two networks of centres, online pre-registration, €70 to €110 — see
<a href="/en/french-civics-test/">the French civics test</a>.</p>
""",
    cta_h2="Find out your real B2 level before you pay for the exam",
    cta_p="""Timed mock exams in the official TCF IRN and TEF IRN formats, AI feedback on writing and speaking against the
official criteria, and a study plan built around your exam date — in the “TCF DELF TEF: Tests 2026” app.""",
    faq=[("What level of French is required for French citizenship?", "B2 on the CEFR scale, in both speaking and writing, since 1 January 2026. Before that, the level required was B1, and it covered speaking only."),
         ("What are the language requirements for French citizenship by marriage?", "B2 in speaking and writing, as for citizenship by decree, for applications submitted since 1 January 2026 — B1 was enough before (Service-Public’s page on proving your French, verified on 1 January 2026). The civics test is different: Service-Public’s page on declarations by marriage, verified on 1 May 2026 and read on 8 October 2026, does not list it among the conditions; your integration is checked at an interview."),
         ("I submitted my application in 2025. Does the B2 requirement apply to me?", "No, if your application was complete and submitted before 31 December 2025: it is still assessed under the previous rules. An incomplete application, or one submitted from 1 January 2026, falls under the new rules. If in doubt, ask the platform handling your application to confirm the date it was registered."),
         ("Is the civics test really compulsory?", "Yes. Since 1 January 2026, a civics test on the values and institutions of the Republic has been added to the conditions, for citizenship as well as for the resident card and the first multi-year residence permit. It is separate from the language test and you prepare for it separately: 40 questions, 45 minutes at most, 32 correct answers — 80% — to pass."),
         ("Which test proves B2 for French citizenship?", 'The tests designed for these procedures are the <a href="/en/tcf-irn/">TCF IRN</a> (France Éducation international) and the TEF IRN (Le français des affaires). A <a href="/en/delf-b2/">DELF B2</a>, DALF C1 or DALF C2 diploma is also proof of level. Check the exact list of accepted proofs and how long they are valid on service-public.fr before paying for any registration.'),
         ("What level of French do I need for a French resident card?", 'B1 for a first resident card since 1 January 2026 — A2 was enough before. Moving from a multi-year residence permit to a resident card is a first issue, not a renewal, so B1 and the civics test apply; renewing a resident card requires neither. A2 is the level for a first multi-year residence permit. A <a href="/en/delf-b1/">DELF B1</a> is accepted for the resident card, and a diploma never expires.'),
         ("Is my DELF B1 still useful for citizenship?", "Not directly: it doesn’t prove the B2 now required. It remains fully valid for a first resident card, where B1 is the level required, and a diploma never expires — unlike a TCF or TEF certificate, which is valid for two years. For citizenship, you need to prove B2, with an IRN test or a DELF B2."),
         ("Can I take the French test online from home?", "No. The order of 22 December 2025 requires four separate tests taken in person, on the same day, in a single session, with anti-fraud supervision and an identity check against a valid official document. Tests taken online from home are not accepted."),
         ("How long does it take to go from B1 to B2?", "The step from B1 to B2 is the longest on the CEFR scale. Language centres’ usual estimates are around 150 to 200 hours of work, but it depends heavily on your profile, your mother tongue and your daily exposure to French. A timed mock exam is the most reliable way to find out your real starting level.")],
    also=[("/en/tcf-irn/", "TCF IRN: the French test for residence and citizenship", "Four tests in 1 h 35 min, scored out of 499: your B2 is decided between 400 and 499."),
          ("/en/french-civics-test/", "The French civics test", "40 questions, 32 correct answers to pass, €70 to €110: the centres and how to register."),
          ("/en/delf-b2/", "DELF B2", "The diploma alternative: longer to take, but it never expires.")],
    sources="""<strong>Regulations change.</strong> This article is up to date as of 27 July 2026 and is not legal advice.
The conditions for citizenship, the list of accepted proofs of level and the cases of exemption are set by texts that may
be amended. Always check your situation on
<a href="https://www.service-public.fr/particuliers/vosdroits/F2213" rel="noopener">service-public.fr</a> before starting
an application or paying for an exam. The material taken from our French guides to the resident card and to B1 or B2 is
up to date as of 27 July and 7 August 2026; the civics test fees were checked at the centres on 17 September 2026.""",
))


# ===========================================================================
# TCF IRN — hub + levels, format, fees and registration
# (from /tcf-irn/, /tcf-irn/niveaux/, /tcf-irn/format/, /tcf-irn/prix-inscription/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/tcf-irn/", lang="en", variant="en-GB", section="en", slug="tcf-irn",
    crumbs=[HOME], crumb="TCF IRN", inline_cta=False,
    title="TCF IRN exam 2026: format, B2 score, fees, preparation",
    desc="The TCF IRN for French citizenship and residence: B2, B1 or A2 since 2026, 4 tests in 1 h 35 scored out of 499 (B2 = 400–499), €140 to €220, CPF-eligible.",
    h1="TCF IRN: the French test for residence and citizenship",
    intro="""The TCF IRN — <strong>Intégration, Résidence, Nationalité</strong> — certifies your level of French for French
administrative procedures: citizenship (<em lang="fr">naturalisation</em>), the resident card (<em lang="fr">carte de
résident</em>), the multi-year residence permit (<em lang="fr">carte de séjour pluriannuelle</em>). It lasts
<strong>1 hour 35 minutes</strong>, has four tests that can’t be split, and is scored <strong>out of 499</strong>, not
699. Since 1 January 2026, the levels required are <strong>B2</strong> in speaking and writing for citizenship (B1
before), <strong>B1</strong> for a first resident card (A2 before) and <strong>A2</strong> for a first multi-year
permit.""",
    facts=["<strong>Citizenship: B2</strong> (speaking and writing) — it was B1 before 2026.",
           "<strong>Resident card: B1</strong> — it was A2.",
           "<strong>Multi-year residence permit: A2.</strong>",
           "⚠️ The TCF IRN is scored <strong>out of 499</strong>, not 699: your B2 is decided between <strong>400 and "
           "499</strong>.",
           "<strong>4 tests in 1 h 35 min</strong> that can’t be split, taken <strong>in person</strong> only — any "
           "“online” offer is a fraud.",
           "Results certificate valid for <strong>2 years</strong> · <strong>eligible for the CPF</strong>, France’s "
           "personal training account (listing RS6643).",
           "<strong>€140 to €220</strong> depending on the centre, for an identical test; sessions almost every week in Paris."],
    toc=[("what-is", "What is the TCF IRN?"), ("steps", "Your path in 5 steps"),
         ("levels", "The levels required since January 2026"), ("b2-step", "The B1 → B2 trap"),
         ("format", "The format, test by test"), ("reform", "A test reformed in 2025"),
         ("scale", "The 499 scale, and the mistake you read everywhere"), ("in-person", "Why you can’t take it online"),
         ("fees", "Fees, the CPF and misleading offers"), ("where", "Where to take the TCF IRN")],
    body="""
<div class="stats">
<div class="stat"><b>1 h 35</b><span>4 tests that can’t be split</span><em>listening 20 · reading 35 · writing 30 · speaking 10 min</em></div>
<div class="stat"><b>499</b><span>the multiple-choice scale</span><em>B2 = 400 to 499</em></div>
<div class="stat"><b>B2</b><span>for citizenship</span><em>B1 resident card · A2 multi-year permit</em></div>
<div class="stat"><b>2 years</b><span>of validity</span><em>eligible for the CPF</em></div>
</div>

<h2 id="what-is">What is the TCF IRN?</h2>
<p>The <strong>TCF IRN</strong> — Intégration, Résidence, Nationalité (integration, residence, nationality) — is France
Éducation international’s French test for <strong>French administrative procedures</strong>: a citizenship application,
a first resident card, a first multi-year residence permit. Since 2022 it has replaced the former TCF ANF and TCF CRF,
and it was <strong>reformed in May 2025</strong> to measure up to B2, the level that became compulsory for citizenship on
1 January 2026.</p>

<p>The test lasts <strong>1 hour 35 minutes</strong> and has four tests that can’t be split — listening, reading, writing,
speaking — taken on the same day, in person, at an approved centre. The multiple-choice tests are scored out of
<strong>499</strong> (not 699 as in the other TCF versions), writing and speaking out of 20; the results certificate is
valid for <strong>two years</strong>. Since 2026, citizenship also requires a separate
<a href="/en/french-civics-test/">civics test</a> — two networks of centres, online pre-registration, €70 to €110.</p>

<h3>Who it’s for</h3>
<ul>
<li>Applicants for <strong>French citizenship</strong>, who must prove B2 in both speaking and writing.</li>
<li>Applicants for a first <strong>resident card</strong> (B1) or a first <strong>multi-year residence permit</strong>
(A2).</li>
<li>People who prefer a quick test, held every week, to a <a href="/en/delf-b2/">DELF diploma</a> that is valid for life
but takes longer to get.</li>
</ul>

<h2 id="steps">Your path in 5 steps</h2>
<ol class="steps">
<li><b>Identify the level you need</b><span>A2 for a first multi-year permit, B1 for the resident card, B2 in speaking and writing for citizenship. <a href="#levels">The table since 2026.</a></span></li>
<li><b>Diploma or test?</b><span>The TCF IRN runs every week but expires after two years; the DELF never expires but takes three months. <a href="/en/delf-b2/">The DELF B2.</a></span></li>
<li><b>Check you have the level</b><span>A <strong>mock exam in the IRN format</strong>, scored out of 499, before you pay €140 to €220 — and practise all four tests; our exercises with answers are in French.</span></li>
<li><b>Register at an approved centre</b><span>Online, a few days before the session; seven centres in Paris. <a href="#where">The centres</a> — and the <a href="/en/french-civics-test/">civics test</a>, booked separately.</span></li>
<li><b>After the test</b><span>Results certificate within 2 to 3 weeks, valid for two years; if you fall short, 20 to 30 days before you can retake all four tests.</span></li>
</ol>

<h2 id="levels">The levels required since January 2026</h2>
<p>These requirements stem from the immigration law of 26 January 2024 and apply to applications submitted since 2026.
Each procedure has its own threshold — mixing them up is the most common mistake, and an expensive one when you prepare
for the wrong level.</p>
""" + table("Level of French required by procedure, as of 7 August 2026. Sources: order of 22 December 2025 and article L. 433-4 of the immigration code (CESEDA).",
            ["Procedure", "Level required"],
            [("First multi-year residence permit", "<strong>A2</strong>"),
             ("First resident card (10 years)", "<strong>B1</strong> — A2 before 2026"),
             ("French citizenship", "<strong>B2</strong>, speaking <em>and</em> writing — B1 before 2026")], wide=False) + """
<p>A trap with the resident card: moving from a multi-year residence permit to a resident card <strong>is not a
renewal</strong>, it is a first issue. B1 and the civics test are therefore required. The resident card procedure is
detailed in our French guide; the citizenship side, in <a href="/en/french-citizenship-b2/">French citizenship: the B2
requirement</a>.</p>

<div class="note">
<p><strong>The test isn’t your whole application.</strong> Since 2026, a <strong>civics test</strong> comes on top of the
language test: 40 questions, 45 minutes at most, and <strong>32 correct answers required</strong>, i.e. 80%. Our sister
app <a href="https://naturalisationfrancefacile.fr">Naturalisation France Facile</a> covers that part: the official
civic-culture questions, explained one by one — <a href="https://apps.apple.com/app/id6761140087">available on the
App&nbsp;Store</a>.</p>
</div>

<h2 id="b2-step">The B1 → B2 trap</h2>
<p>The step between B1 and B2 is the highest on the CEFR scale, and the 2026 reform turned it into the main obstacle in
citizenship applications.</p>

<p>At B1, understanding and narrating are enough. At B2, you must <strong>argue in writing</strong>, <strong>develop and
defend a point of view when speaking</strong>, and understand much more abstract documents. Many citizenship applicants
speak fluent everyday French — sometimes after fifteen years in France — and fall short on argued writing, which they
have never had the chance to practise.</p>

<p>The practical consequence: <strong>how comfortable you are day to day doesn’t predict your score</strong>. An honest
diagnosis — a full mock exam marked against the official grids — is the first step, and targeted practice on writing then
makes most of the difference. It is precisely the test you can’t assess yourself on: knowing whether you write at 9 or
11 out of 20 means knowing whether you have B2 or not. That is what AI feedback against the official criteria solves.</p>

<h2 id="format">The format, test by test</h2>
""" + table("TCF IRN format since the reform of 12 May 2025. Source: France Éducation international, structure checked in July 2026.",
            ["Test", "Questions / tasks", "Time", "Scoring"],
            [("Listening", "25 multiple-choice questions", "20 min", "100–499"),
             ("Reading", "25 multiple-choice questions", "35 min", "100–499"),
             ("Writing", "—", "30 min", "/20"),
             ("Speaking", "—", "10 min", "/20"),
             ("<strong>Total</strong>", "", "<strong>1 h 35 min</strong>", "")], wide=False) + """
<p>The four tests are officially described as <strong>indivisible</strong>: you take them together, on the same day, and
you can’t pick only some of them. It is a much shorter test than the <a href="/en/tcf-canada/">TCF Canada</a>
(2 h 47 min), because it doesn’t target the same levels: it stops at B2, whereas the TCF Canada measures up to C2.</p>

<p>Note too that the TCF IRN <strong>has no</strong> “language structures” section (« maîtrise des structures de la
langue »), unlike the TCF tout public. Practising on TCF tout public papers when you are aiming for the TCF IRN means
working on a test you will never take — and discovering a different comprehension format on the day.</p>

<h2 id="reform">A test reformed in 2025</h2>
<p>The TCF IRN was reformed on <strong>12 May 2025</strong> to keep up with the new requirements. The major change: the
test <strong>now assesses up to B2</strong>, whereas it used to stop at B1. It had to — otherwise it would have been
impossible to prove the B2 required for citizenship since 2026.</p>

<p>The TEF IRN went through a parallel reform on 1 April 2025, a few weeks earlier: its length went from 1 h 20 to
1 h 30, both comprehension tests became adaptive, and the argued section of the writing test went up to 100 words.</p>

<div class="note">
<p><strong>Any resource from before 2025 describes an exam that no longer exists.</strong> Practice papers, tutorials,
videos: if the material presents a TCF IRN capped at B1, or scored out of 399, it is out of date. Always check the date of
what you practise on.</p>
</div>

<h2 id="scale">The 499 scale, and the mistake you read everywhere</h2>
<p><strong>The TCF IRN is scored out of 499, not 699.</strong> It is a direct consequence of the reform, and almost no
source says it correctly.</p>

<p>The reasoning is simple: on the official TCF grid, B2 runs from <strong>400 to 499</strong>. Since the TCF IRN stops at
B2, its scale stops there too. The multiple-choice tests are therefore scored <strong>from 100 to 499</strong>, not out
of 699 as in the TCF tout public or the TCF Canada. Writing and speaking are still scored <strong>out of 20</strong>, with
at least 10 for B2. Before May 2025, when the test stopped at B1, the scale ended at 399. The <strong>TEF IRN</strong>
is also scored out of 499.</p>
""" + table("What your TCF IRN score is worth, on the test’s scale. Source: official TCF level grid, France Éducation international.",
            ["CEFR level", "Multiple-choice tests", "Writing and speaking /20", "Enough for"],
            [("A1", "100–199", "1", "—"),
             ("<strong>A2</strong>", "200–299", "2–5", "multi-year residence permit"),
             ("<strong>B1</strong>", "300–399", "6–9", "resident card"),
             ("<strong>B2</strong>", "<strong>400–499</strong>", "<strong>10–13</strong>", "<strong>citizenship</strong>")],
            wide=False) + """
<div class="note">
<p><strong>The mistake you read everywhere: “in the TCF IRN, B2 means 500–599”.</strong> It’s wrong — a confusion
between the scale and the level. On the official grid, <strong>500–599 is C1</strong>, a level the TCF IRN doesn’t even
award. Your B2 is decided between <strong>400 and 499</strong>. And if you check at the source, be aware that France
Éducation international’s pages still describe, to date, a TCF IRN capped at B1 and scored out of 399: it is the official
documentation that hasn’t caught up with its own reform.</p>
</div>

<p>The two IRN versions are compared test by test in our French comparison of all the TCF and TEF versions.</p>

<h2 id="in-person">Why you can’t take it online</h2>
<p>It’s a question that comes up all the time, and the answer is clear: <strong>no</strong>. The order of 22 December
2025 requires four separate tests taken <strong>in person, on the same day, in a single session</strong>, under
anti-fraud supervision and with an identity check against a valid official document.</p>

<p>French tests taken online from home <strong>are not accepted</strong> for a residence permit. Be wary of offers
promising a “remote” certificate: at best you lose the price of the test, at worst you weaken your application. The
order also governs which certifications are accepted — beyond the level, the certification must in particular be
<strong>registered in the specific register</strong> (<em lang="fr">répertoire spécifique</em>). One more reason to
check that a test bought online is accepted <em>before</em> you take it.</p>

<h2 id="fees">Fees, the CPF and misleading offers</h2>
<p><strong>The fee.</strong> There is no national fee: each approved centre sets its own, and the gap is wide. At the
French centres we checked on 17 September 2026, the TCF IRN cost from <strong>€140</strong> (ACTE, Paris) to
<strong>€220</strong> (ACCORD, Paris) — a ratio of 1 to 1.6 for exactly the same test, in the same city.</p>

<p><strong>The CPF.</strong> Good news, and far from true of every TCF version: the TCF IRN is <strong>registered in the
specific register</strong> of France compétences under listing <strong>RS6643, valid until 31 May 2027</strong> — a
precondition for using France’s personal training account (<em lang="fr">compte personnel de formation</em>, CPF). By
comparison, the TCF Canada isn’t registered, so the CPF can’t pay for it.</p>

<div class="note">
<p><strong>Careful with comparisons on Mon Compte Formation.</strong> The offers you find there are often
<strong>preparation + exam packages</strong>: for example, €430 for a TCF IRN with 14 hours of preparation, against €155
to €180 for the exam alone elsewhere. They aren’t the same products — compare like with like, not headline figures.</p>
</div>

<h2 id="where">Where to take the TCF IRN</h2>
<p>At one of the 251 approved TCF centres in France — provided it actually runs the IRN version. In Paris, seven centres,
with a session almost every week at ACTE (€140) and two a month at ACCORD (€220); elsewhere, the Alliances françaises in
Lyon (€169) and Montpellier (€185), CLPS in Brittany (€180), KLF, Espaces Formation… Our French guide to where to take the
TCF IRN in France lists the centres we checked, their fees and dates, and the registration steps; the civics test that
comes on top since 2026 has its own guide: <a href="/en/french-civics-test/">the French civics test</a>.</p>

<p>Six centres we checked, among the 251 approved in France — all six with computer-based sessions: ACTE, Forum ACCORD
and Etoile Institut de Langue in Paris, the Alliance française in Lyon, the Alliance française de Montpellier, and CLPS
L’Enjeu Compétences in Rennes.</p>
<p class="more">Full directory, with addresses and phone numbers: the 251 TCF centres in France, and our city pages for
Paris, Lyon, Marseille, Toulouse, Montpellier, Bordeaux, Nantes, Rennes, Strasbourg, Lille and Nice — all in French.</p>
""",
    cta_h2="Find out whether you have B2 before you pay to register",
    cta_p="""Timed mock exams in the exact TCF IRN format, scored on the 499 scale with a CEFR level for each test, and AI
feedback on writing and speaking against the official criteria — in the “TCF DELF TEF: Tests 2026” app.""",
    faq=[("What is the TCF IRN exam?", "France Éducation international’s test of French for integration, residence and nationality, designed for French administrative procedures: citizenship, the resident card, the multi-year residence permit. Four tests in 1 h 35 min, in person, scored out of 499 for the multiple-choice tests and out of 20 for writing and speaking; the results certificate is valid for two years."),
         ("What TCF IRN score do I need for French citizenship?", "B2: 400 to 499 in the multiple-choice tests (listening and reading), and 10 to 13 out of 20 in writing and speaking — at least 10 for B2. For a resident card, B1 means 300 to 399 and 6 to 9 out of 20; for a multi-year residence permit, A2 means 200 to 299 and 2 to 5 out of 20. The TCF IRN is a placement test: you don’t fail it, it places you on the scale. If your level is below what your procedure requires, you can retake it, after a waiting period and with a new registration fee."),
         ("Is the TCF IRN scored out of 699 or 499?", "Out of 499. Since the TCF IRN stops at B2 and B2 ends at 499 on the official TCF grid, its multiple-choice tests are scored from 100 to 499, not out of 699 as in the TCF tout public or the TCF Canada. Writing and speaking are still scored out of 20. Careful: France Éducation international’s pages still describe, to date, a TCF IRN capped at B1 and scored out of 399 — the documentation hasn’t caught up with the May 2025 reform."),
         ("How long is the TCF IRN?", "1 h 35 min in total, in a single session: 20 minutes of listening (25 questions), 35 minutes of reading (25 questions), 30 minutes of writing and 10 minutes of speaking. The four tests can’t be split: you can’t take only some of them."),
         ("Can I take the TCF IRN online from home?", "No. The order of 22 December 2025 requires four separate tests taken in person, on the same day, in a single session, with anti-fraud supervision and an identity check against a valid official document. French tests taken online from home are not accepted for a residence permit."),
         ("How much does the TCF IRN cost, and can the CPF pay for it?", "There is no national fee: the exam alone costs between €140 and €220 depending on the centre. Yes, the CPF can fund it: the TCF IRN is registered in France compétences’ specific register under listing RS6643, valid until 31 May 2027 — a precondition for using the personal training account. Careful with Mon Compte Formation offers: many are preparation-plus-exam packages, at around €430."),
         ("TCF IRN or DELF: which should I take for citizenship?", "Both prove B2. The TCF IRN is held almost every week in large cities and marked within three weeks, but it expires after two years; the DELF B2 never expires, but it is held ten times a year, with registration closing weeks in advance. If your application is close, take the TCF IRN; if you have three months, the DELF."),
         ("TCF IRN or TEF IRN: what’s the difference?", "Both are accepted by the French authorities, cover the same levels and are both scored out of 499. They differ in their operator — France Éducation international versus Le français des affaires —, in the centres available and in the task format: the TEF IRN is adaptive in its two comprehension tests, the TCF IRN isn’t. Choose by the dates and centres near you, then practise on the exact format of the test you chose."),
         ("Is the TCF IRN enough to get French citizenship?", 'No: it only proves the language condition. Since 1 January 2026, citizenship also requires passing the <a href="/en/french-civics-test/">civics test</a>, a separate test taken in another network of centres, as well as the conditions of residence, resources and integration.'),
         ("Is there a TCF IRN practice test?", "In our app: the full TCF IRN mock exam, all four tests in the reformed format, scored out of 499, with AI feedback on writing and speaking. Whatever you practise on, check its date: material from before 2025 describes a TCF IRN capped at B1 and scored out of 399, and TCF tout public papers include a “language structures” section that the TCF IRN doesn’t have.")],
    also=[("/en/french-citizenship-b2/", "French citizenship: the B2 requirement", "What changed on 1 January 2026: B2 in speaking and writing, the civics test, the transitional rule."),
          ("/en/french-civics-test/", "The French civics test", "The other compulsory test since 2026: two networks of centres, online pre-registration, €70 to €110."),
          ("/en/delf-b2/", "DELF B2", "The diploma alternative to the test: longer to take, but it never expires.")],
    sources="""<strong>Regulations change.</strong> This page is up to date as of 7 August 2026 and is not legal advice. The
levels required, the accepted certifications and the scoring change regularly — and the official documentation itself
sometimes lags behind the reforms. Check your situation on
<a href="https://www.service-public.fr/" rel="noopener">service-public.fr</a> and the exam format with your approved
centre before you register or apply. Fees were checked at the centres at the end of July 2026; they change without
notice.""",
))


# ===========================================================================
# FRENCH CIVICS TEST (from /blog/ou-passer-l-examen-civique/, with the FEI list of 19 September 2026 from
# /centres/examen-civique-france/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/ou-passer-l-examen-civique/", lang="en", variant="en-GB", slug="french-civics-test",
    crumbs=[HOME], crumb="French civics test", accent="accent-irn",
    title="French citizenship test: civics exam, questions, centres",
    desc="The French civics test (examen civique): 40 questions in French, 45 minutes, 32 correct to pass; 244 approved centres, €70 to €110, free official prep.",
    h1="The French civics test: format, centres, registration and fees",
    intro="""The civics test (<em lang="fr">examen civique</em>) is a <strong>40-question multiple-choice test, in
French</strong>: 45 minutes at most, and <strong>32 correct answers</strong> to pass. You take it <strong>on a computer,
at an approved centre</strong> of one of the two bodies authorised by the Ministry of the Interior: <strong>France
Éducation international</strong> — 244 centres in France, pre-registration on test-civique.fr — and the <strong>CCI Paris
Île-de-France</strong>, whose « Trouver une session » (find a session) tool lists dates centre by centre. Compulsory since
1 January 2026 for a first multi-year residence permit (<em lang="fr">carte de séjour pluriannuelle</em>), a first
resident card (<em lang="fr">carte de résident</em>) and citizenship, it costs <strong>€70 to €110</strong> depending on
the centre, and you can retake it as many times as you need.""",
    facts=["<strong>Two approved networks</strong>: France Éducation international (<strong>244 centres</strong> in 94 "
           "départements on 17 September 2026, 7 of them in Paris) and the CCI Paris Île-de-France (Le français des affaires).",
           "<strong>Three versions</strong> — multi-year residence permit, resident card, citizenship — chosen when you "
           "register; the resident card version also counts for the multi-year permit.",
           "<strong>40 multiple-choice questions</strong> (28 on knowledge, 12 real-life scenarios), <strong>45 minutes</strong>, "
           "<strong>32 correct answers</strong> to pass.",
           "FEI registration: <strong>online pre-registration on test-civique.fr</strong>, with your foreign national number "
           "(AGDREF); CCIP registration: through the centre, via « Trouver une session ».",
           "Fees set by each centre: <strong>€70 (Nantes), €75 (Montpellier), €80–90 (Etoile, Paris), €110 (ACCORD, "
           "Paris)</strong>; results “within 12 hours” at several centres.",
           "Certificate with <strong>no expiry date</strong>, <strong>unlimited</strong> attempts; the official preparation "
           "is <strong>free</strong>."],
    toc=[("who", "Who has to take it, and which version"), ("networks", "Two bodies, two networks of centres"),
         ("fei", "Registering at an FEI centre: test-civique.fr"), ("ccip", "Registering at a CCIP centre"),
         ("paris", "In Paris: the centres and their sessions"), ("fees", "How much it costs"),
         ("abroad", "Taking it abroad"), ("pitfalls", "The traps: paid preparation, the wrong version, fraud")],
    body="""
<h2 id="who">Who has to take it, and which version</h2>
<p>Since 1 January 2026, a pass certificate for the civics test has been required for three procedures: a <strong>first
multi-year residence permit</strong>, a <strong>first resident card</strong>, and <strong>citizenship</strong> by decree
(<em lang="fr">naturalisation</em>). The Ministry of the Interior puts it this way: “Any adult foreign national who has
signed the republican integration contract (CIR) and wishes to settle in France for the long term.” It isn’t required
for a renewal, nor from beneficiaries of international protection, nor from nationals covered by certain bilateral
agreements. Our guide to <a href="/en/french-citizenship-b2/">French citizenship</a> and our French guide to the resident
card detail who is affected and the exemptions.</p>

<p>The test comes in <strong>three versions</strong> (« mentions »), set by the order of 10 October 2025: “multi-year
residence permit”, “resident card” and “citizenship”. You choose yours when you register. The difficulty differs, not the
pass mark: in all three cases, <strong>40 questions</strong> — 28 on knowledge, 12 real-life scenarios, with a single
right answer out of four — <strong>45 minutes</strong> at most, on a tablet or computer, and <strong>32 correct
answers</strong> to pass. A useful rule: “A pass certificate for the civics test, CR version, counts as a pass
certificate for the CSP version” — CR being the resident card, CSP the multi-year permit. The reverse isn’t true.</p>

<p>The questions are <strong>in French</strong> and cover the values, the institutions and the history of the Republic.
The civics test doesn’t replace the language level: it comes on top of it, and the two are prepared separately — they
share neither content nor format.</p>

<h2 id="networks">Two bodies, two networks of centres</h2>
<p>“Two bodies have been approved by the Ministry of the Interior to run the civics test,” says the official website
formation-civique.interieur.gouv.fr: the <strong>Paris Île-de-France Chamber of Commerce and Industry</strong> (CCI Paris
Île-de-France) — the TEF’s operator — and <strong>France Éducation international</strong> — the operator of the TCF and
the DELF. Each has its own network of approved centres, often the same language schools and Alliances françaises as for
the French tests, and its own registration procedure. The certificate is worth the same in both cases.</p>

<p>On 17 September 2026, FEI’s list counted <strong>244 civics test centres in France</strong>, in 94 départements — seven
in Paris, eight in the Rhône, seven in the <span lang="fr">Bouches-du-Rhône</span>, six each in Haute-Garonne, Hérault and
Moselle. The list of
19 September 2026 had 245, in 187 towns: FEI adds and removes centres as approvals come in. The CCIP network is searched
session by session, town by town, in its search tool. A body that is on neither list can’t give you a certificate.</p>

<p class="more">Our French directory lists the FEI centres region by region, with address, phone number and website, and
our French city pages — Paris, Lyon, Marseille, Toulouse, Montpellier, Bordeaux, Nantes, Rennes, Strasbourg, Lille, Nice
— add what each centre’s website showed on 17 September 2026 (exams offered, fees, dates) and how to register.</p>

<h2 id="fei">Registering at an FEI centre: test-civique.fr</h2>
<p>For France Éducation international centres, the ministry points to a single pre-registration form:
<strong>test-civique.fr/inscription</strong>. There you choose the <strong>département</strong>, the <strong>town</strong>
and the <strong>centre</strong>, then the test you want — resident card, multi-year residence permit or citizenship, each
with or without special arrangements — and you enter your contact details, your <strong>foreign national number</strong>
(<em lang="fr">numéro étranger</em>, AGDREF), and your date and place of birth. The form shows the contact details of the
centre you chose; the centre then offers you a date and takes payment. Candidates with a disability must contact the
centre <em>before</em> registering, to arrange adjustments.</p>

<div class="note">
<p><strong>Where to find FEI centres.</strong> On the
<a href="https://www.france-education-international.fr/centres-d-examen/carte?type-centre=examen_civique" rel="noopener">map
of civics test centres</a>, a separate category on FEI’s website, with each centre’s address, phone number and website.
The test-civique.fr form uses the same list, département by département.</p>
</div>

<h2 id="ccip">Registering at a CCIP centre: « Trouver une session »</h2>
<p>The CCI Paris Île-de-France network works by session: on <strong>francais.cci-paris-idf.fr</strong>, the « Trouver une
session » tool asks for a town and the exam — « Examen civique mention carte de résident », « … carte de séjour
pluriannuelle » or « … naturalisation » — and shows the centres with their number of available sessions, a map, and two
buttons: « Contacter le centre » (contact the centre) and « Choisir » (choose). You then register and pay with the
centre. The same tool is used for the TEF: TEF IRN centres are often CCIP civics test centres too.</p>

<h2 id="paris">In Paris: the centres and their sessions</h2>
<p>Paris is the best-served city, and also the one where you find <strong>full</strong> sessions. On the FEI side, the
seven approved centres are those of the TCF: ACTE (10th arrondissement), ILE International (12th), the Alliance française
Paris Île-de-France (6th), the Cours de civilisation française de la Sorbonne (17th), ELFE (1st), Etoile Institut (7th) and
ACCORD (15th). On 17 September 2026, the Alliance française showed on its civics test page: “All our sessions are full for
the moment.” On the CCIP side, a search for the citizenship version in Paris returned, for September to December
2026:</p>
""" + table("CCIP centres offering the civics test, citizenship version (« mention naturalisation »), in Paris: Le français des affaires’ « Trouver une session » tool, sessions from September to December 2026, consulted on 17 September 2026.",
            ["Centre", "Arrondissement", "Sessions shown"],
            [("Emploi Services Formation (ESF)", "19th, rue d’Hautpoul", "<strong>300</strong>"),
             ("ASPLEF", "10th, boulevard de Magenta", "44"),
             ("AVD Formation", "17th, rue Catulle-Mendès", "34"),
             ("Kangourou", '16th, <span lang="fr">rue du Général-Clergerie</span>', "11"),
             ("ALIP", "15th, rue Ginoux", "5"),
             ("Etoile Institut de langue", "7th, boulevard Raspail", "3"),
             ("CCI Paris République", "10th, rue Léon-Jouhaux", "2"),
             ("Institut Aritas Formation", "17th, rue Cardinet", "1")], wide=True) + """
<p>Etoile Institut, approved by both bodies, ran sessions <strong>almost every day</strong> in September 2026, at €80 on
weekdays and €90 on Saturdays. With sessions of 40 questions in 45 minutes, a centre can run several a day: the scarcity
you find with the DELF or the TCF Canada has no reason to exist here, except at centres that open only a few dates a
month.</p>

<h2 id="fees">How much it costs</h2>
<p>No text sets the price of the civics test — not the order of 10 October 2025, not the Service-Public fact sheets, not
the ministry’s website. Each approved centre decides. At the centres we checked on 17 September 2026:</p>
""" + table("Civics test fees shown by the centres on 17 September 2026. Fees are set freely and change without notice.",
            ["Centre", "Town", "Fee", "Results"],
            [("Espaces Formation", "Nantes", "<strong>€70</strong>", "“usually within 12 hours”"),
             ("Alliance française de Montpellier", "Montpellier", "<strong>€75</strong>", "no data"),
             ("Etoile Institut de langue", "Paris (7th)", "<strong>€80</strong> (€90 on Saturdays)", "no data"),
             ("ACCORD", "Paris (15th)", "<strong>€110</strong>", "“final certificate within 12 hours”"),
             ("Alliance française Paris Île-de-France", "Paris (6th)", "no data", "“all our sessions are full”")],
            wide=False) + """
<p>Fees vary by a factor of almost two for exactly the same test, and results often arrive the same day: the certificate
is issued by the approved body, with no expiry date — “it has no period of validity”, the ministry writes — and “the civics
test can be taken at any time and as many times as necessary”. Each attempt is paid for.</p>

<h2 id="abroad">Taking it abroad</h2>
<p>The civics test can also be taken outside France, at Instituts français, Alliances françaises and consular authorities
— useful for a citizenship or residence permit application prepared from abroad. The Institut français d’Algérie, for
example, runs it in Algiers (30, <span lang="fr">rue des Frères-Kadri</span>, Hydra): pre-registration on test-civique.fr
through its dedicated link, <strong>9,000 DA</strong> (Algerian dinars) payable by bank card or Dahabia card on site, or by
bank transfer, confirmation within 48 hours, test-day notice by email, biometric ID card or passport on the day. FEI’s
centre map has a country filter for the civics test.</p>

<h2 id="pitfalls">The traps: paid preparation, the wrong version, fraud</h2>
<div class="warn">
<p><strong>Preparation is free.</strong> The ministry says so in bold: “Preparing for the civics test can be done
completely free of charge. There is no need to pay to access questions or practice tests.” The
formation-civique.interieur.gouv.fr website publishes the programme, theme-by-theme fact sheets and the <strong>official
list of knowledge questions</strong> for the multi-year residence permit and resident card versions; the list for the
citizenship version is on the ministry’s website. Only the 12 real-life scenario questions aren’t published. Many paying
sites resell exactly these questions. And you don’t register for the test on formation-civique.interieur.gouv.fr: it is
only for preparation.</p>
</div>

<ul>
<li><strong>The wrong version.</strong> A “multi-year residence permit” certificate isn’t valid for the resident card or
for citizenship; the reverse works from the resident card to the multi-year permit. If in doubt, take the highest version
you will need.</li>
<li><strong>The French test, on top.</strong> The civics test doesn’t replace the language level: A2 for the multi-year
permit, B1 for the resident card, B2 for citizenship, to be proved with a <a href="/en/tcf-irn/">TCF IRN</a>, a TEF IRN or
a <a href="/en/delf-b2/">DELF diploma</a>. Two registrations, two dates.</li>
<li><strong>Bogus certificates.</strong> Centres check identity; the order of 10 October 2025 provides that,
in the event of fraud or attempted fraud, the candidate can’t sit the test again for two years, and the test is cancelled
in the event of false identity or impersonation. A website promising a certificate “without taking the test” is selling
a fake.</li>
<li><strong>The wrong network.</strong> A TCF centre isn’t automatically a civics test centre, and vice versa: check the
“examen civique” category on FEI’s map, or that the centre appears in the CCIP’s tool.</li>
</ul>
""",
    cta_h2="The civics test is free to prepare; B2 takes work",
    cta_p="""The civics test has its questions published; the French test that comes with it doesn’t. The mock exams in the
“TCF DELF TEF: Tests 2026” app reproduce the TCF IRN, the TEF IRN and the DELF in the official format, with AI feedback on
writing and speaking — so you reach the B2 required since 2026 before you pay for the session.""",
    faq=[("What is the French citizenship test?", 'Since 1 January 2026, French citizenship requires two separate things: passing the civics test (examen civique) in its citizenship version — 40 multiple-choice questions on the values, institutions and history of the Republic, 45 minutes at most, 32 correct answers to pass — and proving French at B2 level, with a test such as the <a href="/en/tcf-irn/">TCF IRN</a> or a diploma such as the <a href="/en/delf-b2/">DELF B2</a>.'),
         ("Is the French civics test in English?", "No. It is a multiple-choice test of 40 questions in French, taken on a tablet or computer at an approved centre, with a single right answer out of four for each question."),
         ("Where can I find civics test questions to practise?", "On the ministry’s official website, free: formation-civique.interieur.gouv.fr publishes the programme, theme-by-theme fact sheets and the official list of knowledge questions for the multi-year residence permit and resident card versions; the list for the citizenship version is on the ministry’s website. Only the 12 real-life scenario questions aren’t published. Many paying sites resell exactly these questions."),
         ("Where can I take the civics test?", "At a centre approved by one of the two bodies authorised by the Ministry of the Interior: France Éducation international — 244 centres in France on 17 September 2026, on its map of civics test centres, pre-registration on test-civique.fr — or the CCI Paris Île-de-France, whose « Trouver une session » tool lists the centres and their dates. You take the test on site, on a computer or tablet."),
         ("How do I register for the civics test?", "For an FEI centre, with the test-civique.fr pre-registration form: département, town, centre, version (multi-year residence permit, resident card or citizenship), contact details and AGDREF foreign national number; the centre then offers you a date and takes payment. For a CCIP centre, through the « Trouver une session » tool on francais.cci-paris-idf.fr, then with the centre."),
         ("How much does the civics test cost?", "No text sets a fee: each centre decides. Checked on 17 September 2026: €70 at Espaces Formation (Nantes), €75 at the Alliance française de Montpellier, €80 on weekdays and €90 on Saturdays at Etoile Institut (Paris), €110 at ACCORD (Paris). Preparation, on the other hand, is free on the ministry’s website."),
         ("Which version should I choose?", "The one for your procedure: “multi-year residence permit”, “resident card” or “citizenship”. The resident card version also counts for the multi-year permit, but not the reverse, and neither counts for citizenship. The format is the same (40 questions, 45 minutes, 32 correct answers); only the difficulty changes."),
         ("How quickly do I get the certificate, and how long is it valid?", "Several centres announce the certificate “within 12 hours” (ACCORD in Paris, Espaces Formation in Nantes). It has no period of validity, and the test can be retaken “at any time and as many times as necessary” — each attempt being paid for."),
         ("Can I take the civics test abroad?", "Yes, at Instituts français, Alliances françaises and consular authorities. The Institut français d’Algérie runs it in Algiers for 9,000 dinars, with pre-registration on test-civique.fr and payment on site or by bank transfer. FEI’s centre map can be filtered by country."),
         ("Do I also need to take a French language test?", "Yes, the civics test comes on top of the language level required: A2 for a first multi-year residence permit, B1 for a first resident card, B2 for citizenship. The level is proved with a TCF IRN, a TEF IRN or a DELF or DALF diploma — at a centre that isn’t necessarily the same one.")],
    also=[("/en/french-citizenship-b2/", "French citizenship: the B2 requirement", "What changed in January 2026, the accepted proofs of level, the transitional rule."),
          ("/en/tcf-irn/", "TCF IRN: the French test for residence and citizenship", "The levels required since 2026, the four tests, the 499 scale."),
          ("/en/delf-b1/", "DELF B1", "The diploma that proves B1, the resident card level — and never expires.")],
    sources="""<strong>Sources.</strong> Ministry of the Interior, formation-civique.interieur.gouv.fr, “General information
about the civics test” page (approved bodies, registration links, format, pass mark, validity, free preparation),
consulted on 17 September 2026; order of 10 October 2025 on the programme, tests and organisation of the civics test
(Légifrance); Service-Public fact sheets F39426 and F39530; France Éducation international’s list and map of civics test
centres (“France” filter) and the test-civique.fr pre-registration form, consulted on 17 September 2026, and FEI’s list
of 19 September 2026 for the 245 centres; Le français des affaires’ (CCI Paris Île-de-France) « Trouver une session »
tool, search “Paris, civics test, citizenship version”, consulted on 17 September 2026; the civics test pages of ACCORD
(2026 fee schedule), Etoile Institut, the Alliance française de Montpellier, Espaces Formation, the Alliance française
Paris Île-de-France and the Institut français d’Algérie, consulted on 17 September 2026. That the test is in French and
what it covers come from our French guides to the resident card and to B1 or B2, up to date as of 27 July and 7 August
2026. Fees and sessions change without notice. This page is not legal advice.""",
))

# Traductions en-CA (08/10/2026). Aucun fait nouveau : chaque chiffre, date et règle vient des pages françaises
# publiées, avec sa date. Fusions : /en/tef-canada/ = /tef-canada/ + format, score-nclc, tefaq, preparation-inscription ;
# /en/tcf-quebec/ = /tcf-quebec/ + format-modulaire, echelle-quebecoise, prix-inscription.
# Liens anglais : seulement ceux de la consigne ; cibles françaises = texte sans lien.

TEF_CTA_H2 = "Know where you stand before you register"
TEF_CTA_P = """Timed mock exams in the exact TEF Canada format (sections A and B of both writing and speaking), an automatic
CLB conversion for each test and AI feedback against the official criteria, in the “TCF DELF TEF: Tests 2026” app."""

TEF_CLB = table("TEF Canada → CLB, on the scales IRCC uses in the Express Entry profile — those of the "
                "<em lang=\"fr\">Équivalence ancien score</em> column, not the 699 column. Source: IRCC equivalency tables, "
                "checked on 27 July 2026.",
                ["CLB", "Reading /300", "Listening /360", "Writing /450", "Speaking /450"],
                [("10", "263–300", "316–360", "393–450", "393–450"), ("9", "248–262", "298–315", "371–392", "371–392"),
                 ("8", "233–247", "280–297", "349–370", "349–370"),
                 ("<strong>7</strong>", "<strong>207–232</strong>", "<strong>249–279</strong>", "<strong>310–348</strong>", "<strong>310–348</strong>"),
                 ("6", "181–206", "217–248", "271–309", "271–309"), ("5", "151–180", "181–216", "226–270", "226–270"),
                 ("4", "121–150", "145–180", "181–225", "181–225")], wide=False)


# ===========================================================================
# TEF CANADA — hub + modules (from /tef-canada/, /tef-canada/format/, /tef-canada/score-nclc/,
# /tef-canada/tefaq/, /tef-canada/preparation-inscription/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/tef-canada/", lang="en", variant="en-CA", section="en", slug="tef-canada",
    crumbs=[HOME], crumb="TEF Canada", inline_cta=False, accent="accent-tef",
    title="TEF Canada exam: format, score chart and CLB levels",
    desc="TEF Canada: 4 tests in 2 h 55 min, the CLB chart IRCC uses (CLB 7 = 207 in reading, 249 in listening, 310 in writing and speaking), TEFAQ, fees.",
    h1="TEF Canada and TEFAQ: the French test that opens the door to Canada and Quebec",
    intro="""The TEF Canada is, along with the <a href="/en/tcf-canada/">TCF Canada</a>, one of the <strong>only two
tests</strong> IRCC accepts for federal economic immigration. It lasts <strong>2 h 55 min</strong>, with four tests on the
same day. What sets it apart — and its trap — is the way it shows your scores: <strong>your results certificate has two
columns of scores, and IRCC doesn’t read the one you think</strong>. Here is the format, the CLB chart on the right
scale, the TEFAQ, and how to prepare and register.""",
    facts=["<strong>4 compulsory tests</strong> for immigration, in 2 h 55 min. For <strong>citizenship</strong>, only "
           "listening and speaking are required.",
           "⚠️ IRCC converts to CLB levels (NCLC in French) from the <strong><em lang=\"fr\">Équivalence ancien score</em></strong> "
           "(old-score equivalent) column of your results certificate, <strong>not</strong> from the column out of 699.",
           "<strong>CLB 7</strong> = 207 in reading, 249 in listening, 310 in writing and in speaking, on these “old score” scales.",
           "<strong>CLB 9</strong> = 248 in reading, 298 in listening, 371 in writing and speaking; CLB 10 = 263, 316 and 393.",
           "The <strong>TEFAQ</strong> has exactly the same tests, but it is <strong>modular</strong> and read on the Quebec scale.",
           "⚠️ The TEFAQ is <strong>not accepted</strong> by IRCC for Express Entry.",
           "<strong>No national fee</strong>: €245 found in Paris; no verifiable Canadian fee for the TEF Canada.",
           "Retake waiting period: <strong>20 days</strong>, with no ambiguity (the 30-day rumour is false for the TEF)."],
    toc=[("what-is", "What is the TEF Canada?"), ("steps", "Your path in 5 steps"),
         ("format", "The TEF Canada exam format, test by test"), ("tasks", "The TEF tasks to get used to"),
         ("old-score", "The “old score” column trap"), ("clb", "TEF Canada score chart: the CLB table"),
         ("tefaq", "TEFAQ: the modular Quebec version"), ("preparation", "How to prepare for the TEF Canada"),
         ("fees", "Fees, validity, retakes"), ("where", "Where to take the TEF Canada?")],
    body="""
<div class="stats">
<div class="stat"><b>2 h 55</b><span>4 tests</span><em>reading 60 · listening 40 · writing 60 · speaking 15 min</em></div>
<div class="stat"><b>40 + 40</b><span>reading and listening questions</span><em>2 sections each in writing and speaking</em></div>
<div class="stat"><b>CLB 7</b><span>= 207 in reading, 249 in listening</span><em>310 in writing and in speaking</em></div>
<div class="stat"><b>2 years</b><span>of validity</span><em>checked twice by IRCC</em></div>
</div>

<h2 id="what-is">What is the TEF Canada?</h2>
<p>The <strong>TEF Canada</strong> — <em lang="fr">test d’évaluation de français</em> — is designed by Le français des
affaires, the organization of the CCI Paris Île-de-France (the Paris Île-de-France chamber of commerce and industry), and
recognized by Immigration, Refugees and Citizenship Canada on the same footing as the
<a href="/en/tcf-canada/">TCF Canada</a>. It has <strong>four tests</strong> in <strong>2 h 55 min</strong>: reading and
listening, with 40 questions each, and writing and speaking, in two sections each. Each test is scored on its own scale,
then converted into <strong>CLB levels</strong> by IRCC.</p>

<p>Its Quebec version, the <strong>TEFAQ</strong>, has exactly the same tests, but it is modular — you take only what your
program requires — and it is read on the Quebec scale; IRCC doesn’t accept it. Results certificates are valid for
<strong>two years</strong>, and you can retake a test after 20 days.</p>

<h3>Who it’s for</h3>
<ul>
<li>Candidates for <strong>Express Entry</strong> and <strong>citizenship</strong> who prefer the TEF format — two sections
each in writing and speaking, including “write the continuation of a news story” — to the TCF format.</li>
<li>Candidates for <strong>Quebec</strong>’s programs, with the TEFAQ, often in two tests.</li>
<li>Those who have a TEF centre that is closer, or has more availability, than a TCF centre: the two networks are
different.</li>
</ul>

<h2 id="steps">Your path in 5 steps</h2>
<ol class="steps">
<li><b>TEF or TCF?</b><span>IRCC accepts both; they have neither the same format nor the same conversion table. <a href="/en/tcf-vs-tef-canada/">The comparison.</a></span></li>
<li><b>Set your target CLB</b><span>On the TEF scales IRCC uses. <a href="#clb">The conversion table.</a></span></li>
<li><b>Get used to the TEF tasks</b><span>Writing the continuation of a news story, asking the examiner questions: formats specific to the TEF. <a href="#tasks">The tasks</a> and the <a href="/en/tef-canada-practice-test/">exercises with answers</a>.</span></li>
<li><b>Test your level</b><span>A timed TEF Canada mock exam, scored on the test’s scales and converted to CLB.</span></li>
<li><b>Register at an approved centre</b><span>Through Le français des affaires (CCI Paris Île-de-France), not through FEI (France Éducation international): its directory covers every country. <a href="#where">The centres.</a></span></li>
</ol>

<h2 id="format">The TEF Canada exam format, test by test</h2>
<p>The TEF Canada is <strong>four tests in 2 h 55 min</strong>: 40 reading questions in 60 minutes, 40 listening
questions in 40 minutes, writing in two sections (80, then 200 words minimum) and speaking in two sections, face to
face.</p>
""" + table("Official TEF Canada format. Source: Le français des affaires — CCI Paris Île-de-France, structure checked in July 2026.",
            ["Test", "Questions / tasks", "Time", "What’s specific"],
            [("Reading", "40 questions", "60 min", "Free navigation, linear format"),
             ("Listening", "40 questions", "40 min", "<strong>Played only once</strong>, no going back"),
             ("Writing", "2 sections", "60 min", "A: 80 words min (25 min) · B: 200 words min (35 min)"),
             ("Speaking", "2 sections", "15 min", "A: 5 min · B: 10 min, face to face"),
             ("<strong>Total</strong>", "", "<strong>2 h 55 min</strong>", "")], wide=False) + """

<p>The TEF differs from the TCF in the <strong>structure of its writing and speaking tests</strong>. Where the TCF Canada
has three short tasks, the TEF has two, longer and more specific:</p>

<ul>
<li><strong>Writing, section A</strong> — you write the <em>continuation</em> of an article or news story whose beginning
you are given. 80 words minimum, 25 minutes. The exercise has no equivalent in the TCF, and it throws candidates who
discover the instructions on exam day.</li>
<li><strong>Writing, section B</strong> — a reasoned point of view, 200 words minimum, 35 minutes. It is the part that
separates candidates most in the whole test.</li>
<li><strong>Speaking, section A</strong> — you have to <em>obtain information</em> by asking the examiner questions. So you
are the one asking, not the one answering: it is counter-intuitive, and it takes practice.</li>
<li><strong>Speaking, section B</strong> — you argue to convince the other person. Ten minutes, face to face, with double
marking.</li>
</ul>

<h2 id="tasks">The TEF tasks to get used to</h2>
<p>This is the point to remember if you are still torn between the two tests: <strong>the skills assessed are the same;
the exercises are not</strong>. A candidate trained on TCF practice material who sits the TEF discovers four sets of
instructions they have never practised.</p>

<ul>
<li><strong>Writing the continuation of a text</strong> (writing, section A) means picking up a register, a verb tense and
a point of view set by the opening. It isn’t free writing: the mark penalizes any break in coherence with the beginning
you are given.</li>
<li><strong>Asking questions</strong> (speaking, section A) reverses the candidate’s usual role. Many stay in the position
of the one being questioned, say too little, and lose points on a section that is short and predictable.</li>
<li><strong>The word minimums</strong> — 80 and 200 — are floors, not targets. Below them, task completion is marked
down, whatever the quality of your language.</li>
<li><strong>One listening only, no going back</strong>, as in the TCF. Losing track of a question means losing it: what
matters is moving on to the next one immediately.</li>
</ul>

<h2 id="old-score">The “old score” column trap</h2>
<div class="note">
<p><strong>This is the most expensive mistake in the TEF Canada.</strong> Your results certificate shows your results
<em>out of 699</em>, like the TCF. But IRCC doesn’t convert those scores: the federal equivalency tables are based on the
<strong><em lang="fr">Équivalence ancien score</em></strong> (old-score equivalent) column, whose scales are completely
different — out of 300 in reading, out of 360 in listening, out of 450 for each of writing and speaking.</p>
</div>

<p>In practice: a candidate who reads “450” in the 699 column and looks up what 450 is worth in a CLB table will find
nothing consistent — or worse, a plausible but wrong match. First find the right column on the certificate, then
convert. It is the only number that counts for your Express Entry profile.</p>

<p>This double scoring doesn’t exist in the TCF Canada, where reading and listening are scored out of 699 and writing
and speaking out of 20, with no alternative column. It is a practical reason — not a linguistic one — to sometimes prefer
the TCF: one scale to read, one less risk of error in an application where every point counts.</p>

<h2 id="clb">TEF Canada score chart: the CLB table</h2>
""" + TEF_CLB + """

<p>As in the TCF, it is your <strong>weakest test that decides</strong>: IRCC looks at your full profile, and CLB 9 in a
comprehension test doesn’t make up for CLB 6 in speaking. Each test is converted separately, and the lowest CLB limits
your points. For what each level earns in the ranking, see our comparison
<a href="/en/tcf-vs-tef-canada/">TCF or TEF Canada</a>.</p>

<h2 id="tefaq">TEFAQ: the modular Quebec version</h2>
<p>The TEFAQ — <em lang="fr">TEF pour l’accès au Québec</em>, whose current official name is “TEF Québec” — has
<strong>exactly the same tests</strong> as the TEF Canada: same durations, same tasks, same instructions. Only two things
change, and they change a lot: you take only the tests your program requires, and the results are read on the
<strong>Quebec scale</strong>, graded from 1 to 12, not in CLB.</p>
""" + table("What sets the TEFAQ apart from the TEF Canada.", ["", "TEF Canada", "TEFAQ (TEF Québec)"],
            [("Tests", "4 compulsory", "<strong>1 to 4, your choice</strong>"),
             ("Scale used", "CLB 4 to 10", "Quebec scale, 1 to 12"),
             ("Accepted by IRCC (federal)", "yes", "<strong>no</strong>"),
             ("Accepted by Quebec (MIFI)", "yes", "yes")], wide=False) + """

<p>Modularity is the real lever. Several Quebec requirements cover <strong>only oral skills</strong> — stream 2 of the
PSTQ, Quebec’s skilled worker selection program, and the condition set for an accompanying spouse. In those cases,
registering for the oral tests alone is enough: less preparation, less risk, and a bill reduced accordingly.</p>

<p>The asymmetry in acceptance, on the other hand, deserves some thought: <strong>the TEF Canada is accepted everywhere,
the TEFAQ only in Quebec</strong>, by its immigration ministry (MIFI) — IRCC accepts it neither for Express Entry nor for
citizenship. If your plans might shift to the federal route, taking the four tests of the TEF Canada costs more but
covers both routes. The same reasoning applies to the <a href="/en/tcf-quebec/">TCF Québec</a>, which we cover on its
own page.</p>

<h2 id="preparation">How to prepare for the TEF Canada</h2>
<p>You prepare for the TEF Canada on its format — two sections each in writing and speaking, a single listening — more
than on your level. The method that works is the same as for the TCF, with one nuance on the first step: in the TEF, the
initial mock exam is as much about <strong>discovering the task formats</strong> as about measuring your level.</p>

<ol>
<li><strong>A full mock exam right at the start</strong>, before any revision, to find your current CLB level in each test —
and so you don’t discover the “continue the article” section on exam day.</li>
<li><strong>Targeted practice on your weakest test</strong>, the one that caps your application.</li>
<li><strong>Regular timed mock exams</strong> until the two sections of writing and of speaking have become automatic.</li>
</ol>

<p>In writing and speaking, the blind spot is structural: you can’t assess yourself against criteria you don’t know.
Knowing whether your section B is worth CLB 6 or CLB 7 is exactly what AI feedback against the official criteria solves.
To practise each section, see our <a href="/en/tef-canada-practice-test/">TEF Canada practice test</a>, with answers.</p>

<div class="note">
<p><strong>Take a mock exam of each before choosing.</strong> No general rule says the TEF is easier than the TCF, or the
other way round. The only reliable criterion is your own score in each format — and it varies a lot from one candidate to
another, depending on whether you are more at ease with quick multiple-choice questions or with long tasks.</p>
</div>

<h2 id="fees">Fees, validity, retakes</h2>
<p><strong>The fee.</strong> There is no national fee: each approved centre sets its own. In France, we found
<strong>€245</strong> at ALIP in Paris at the end of July 2026 — close to TCF Canada fees elsewhere in France (€200 to €220
in Montpellier and Lyon). In Canada, on the other hand, <strong>we found no verifiable TEF Canada fee</strong>: be wary of
tables claiming the two tests cost “the same” there. The fee doesn’t decide between the TCF and the TEF; it decides
between centres.</p>

<p><strong>Validity.</strong> Two years — but the starting point is ambiguous. The registration conditions of Le français
des affaires run the period <em>from the date the results certificate is issued</em>, while its presentation page speaks
of two years <em>from the test date</em>. The gap can reach several weeks, and it matters if your application is
submitted just before the deadline. <strong>Go by the less favourable date</strong> and have your centre confirm it.</p>

<p><strong>Retakes.</strong> Twenty days between two attempts at the same test, all versions of the TEF combined — and here,
unlike with the TCF, there is no ambiguity in the official documentation. The rumour of a 30-day wait for the TEF comes
from a confusion with some TCF information sheets.</p>

<h2 id="where">Where to take the TEF Canada?</h2>
<p>At a centre approved by Le français des affaires, whose
<a href="https://www.lefrancaisdesaffaires.fr/trouver-un-centre-agree/" rel="noopener">official directory</a> covers every
country — often the same Alliances françaises as for the TCF, but the approval is separate. To compare with the TCF
network, its fees and its timelines, see our guide to <a href="/en/tcf-canada-test-centres/">TCF Canada test centres in
Canada</a>; our guides for France, and our hub on where to take each exam, are in French.</p>

<p>The TEF belongs to a different network from the TCF — that of Le français des affaires, whose directory is the
reference. Three Paris centres we checked on their own websites: the Alliance française Paris Île-de-France
(computer-based), Etoile Institut de Langue (computer-based) and ALIP, where we found the TEF Canada at €245.</p>
<p class="more">Full directory, with addresses and phone numbers:
<a href="https://www.lefrancaisdesaffaires.fr/trouver-un-centre-agree/" rel="noopener">the official directory of TEF
centres (Le français des affaires)</a>. Our directory of TCF, DELF and civics test centres is in French.</p>
""",
    cta_h2=TEF_CTA_H2, cta_p=TEF_CTA_P,
    faq=[("What is the TEF Canada test?", "A French test by the CCI Paris Île-de-France (Le français des affaires), recognized by IRCC for economic immigration and citizenship on the same footing as the TCF Canada. Four tests in 2 h 55 min, each scored on its own scale, then converted to CLB; the results certificate is valid for two years."),
         ("What is the TEF Canada exam format, and how long is it?", "2 h 55 min in total: 60 minutes of reading, 40 minutes of listening, 60 minutes of writing in two sections and 15 minutes of speaking in two sections. All four tests are compulsory for economic immigration; for a citizenship application, only listening and speaking are required."),
         ("What TEF Canada score do I need for CLB 7?", "On the “old score” scales IRCC uses: 207 to 232 in reading, 249 to 279 in listening, and 310 to 348 in both writing and speaking. CLB 7 in all four tests is the reference threshold of the Federal Skilled Worker Program."),
         ("Why does my TEF results certificate show two different scores?", "Because the TEF Canada publishes two columns: a score out of 699 and an “Équivalence ancien score” (old-score equivalent) column. IRCC converts your results to CLB from the “old score” column, not from the one out of 699. Reading the wrong column makes you think your CLB is much higher or much lower than it really is — it is the most frequent reading error with the TEF."),
         ("TEF Canada or TCF Canada: which one should I take?", "Both are accepted by IRCC and are worth the same. They differ in format (40 questions per comprehension test and two sections each in writing and speaking for the TEF, versus 39 questions and three tasks for the TCF), in their conversion tables and in their networks of centres. Choose the one whose format suits you and that has a centre available near you."),
         ("Is the TEFAQ the same as the TEF Canada?", "No. The tests are identical — same durations, same tasks — but two things change: the TEFAQ is modular, you choose 1 to 4 tests, whereas the TEF Canada requires all four; and TEFAQ results are read on MIFI’s Quebec scale, not on the federal CLB. The TEFAQ is used only for Quebec’s programs: IRCC doesn’t accept it for Express Entry."),
         ("How do I prepare for the TEF Canada?", "Start with a full mock exam before any revision, to find your current CLB level in each test and discover the TEF task formats; then do targeted practice on your weakest test, the one that caps your application; then take regular timed mock exams until the two sections of writing and of speaking are automatic. Take a TCF mock exam too before choosing: no general rule says one test is easier than the other."),
         ("How much does the TEF Canada cost?", "There is no national fee: each approved centre sets its own. In France, we found 245 euros at ALIP in Paris at the end of July 2026, close to TCF Canada fees elsewhere in France. In Canada, we found no verifiable TEF Canada fee — be wary of tables claiming the two tests cost the same there."),
         ("How long do I have to wait to retake the TEF?", "Twenty days between two attempts at the same test, all versions of the TEF combined. The rumour of a 30-day wait for the TEF is false: it comes from a confusion with some TCF information sheets."),
         ("When do the two years of TEF validity start?", "The pages of Le français des affaires don’t say the same thing: its registration conditions run validity from the date the results certificate is issued, while its presentation page speaks of two years from the test date. The gap can reach several weeks. Go by the date that is less favourable to you, and have your centre confirm it.")],
    also=[("/en/tcf-vs-tef-canada/", "TCF or TEF Canada: which one to choose?", "Both CLB conversion tables side by side, the format and fee comparison, and the “old score” column trap."),
          ("/en/tef-canada-practice-test/", "TEF Canada practice test", "A listening and a reading exercise with answers, and the section A and B tasks explained."),
          ("/en/tcf-quebec/", "TCF Québec: the modular test for Quebec", "The other modular option for a Quebec project, and its conversion table.")],
    sources="""<strong>Rules change.</strong> This page is up to date as of 7 August 2026 and is not immigration advice. Thresholds,
conversion tables and registration conditions change regularly. Always check your situation on
<a href="https://www.canada.ca/en/services/immigration-citizenship.html" rel="noopener">canada.ca</a> and the exam format on
<a href="https://www.lefrancaisdesaffaires.fr/" rel="noopener">lefrancaisdesaffaires.fr</a> before you register or apply.""",
))


# ===========================================================================
# TEF CANADA — practice test (from /blog/exercices-tef-canada/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/exercices-tef-canada/", lang="en", variant="en-CA", slug="tef-canada-practice-test",
    crumbs=[HOME], crumb="TEF Canada practice test", accent="accent-tef",
    title="TEF Canada practice test: sample questions with answers",
    desc="Free TEF Canada practice: a listening and a reading question with answers, sample section B topics for writing and speaking, and the CLB 7 scores.",
    h1="TEF Canada practice test: the sections, with answers explained",
    intro="""The TEF Canada lasts <strong>2 h 55 min</strong> and requires four tests. Reading and listening have
<strong>40 questions</strong> each, and the writing and speaking tests are organized in <strong>two sections</strong> with
very specific instructions — writing the continuation of a text, asking the examiner questions — that have <strong>no
equivalent in the TCF</strong>. Here are practice exercises with answers, and what each section expects.""",
    facts=["<strong>Reading 40 questions/60 min · listening 40 questions/40 min · writing 2 sections/60 min · speaking 2 sections/15 min.</strong>",
           "⚠️ IRCC reads the <strong><em lang=\"fr\">Équivalence ancien score</em></strong> (old-score equivalent) column, not the 699 one.",
           "<strong>CLB 7</strong> (NCLC 7 in French) = 207 in reading, 249 in listening, 310 in writing and in speaking, on these scales.",
           "⚠️ <strong>Writing, section A</strong>: write the <em>continuation</em> of a text — an exercise with no equivalent in the TCF.",
           "⚠️ <strong>Speaking, section A</strong>: <em>you</em> are the one asking the questions.",
           "One listening only, no going back."],
    toc=[("format", "The test format"), ("exercises", "Two sample questions with answers: listening and reading"),
         ("sections", "The four writing and speaking sections"), ("old-score", "The “old score” column trap"),
         ("method", "The method")],
    body="""
<h2 id="format">The test format</h2>
""" + table("TEF Canada. Source: Le français des affaires — CCI Paris Île-de-France, structure checked in July 2026.",
            ["Test", "Content", "Time"],
            [("Reading", "40 questions", "60 min"),
             ("Listening", "40 questions", "40 min"),
             ("Writing", "2 sections — A: 80 words min · B: 200 words min", "60 min"),
             ("Speaking", "2 sections — A: 5 min · B: 10 min", "15 min"),
             ("<strong>Total</strong>", "", "<strong>2 h 55 min</strong>")], wide=False) + """

<p>Forty questions in 40 minutes in listening is <strong>one minute per question</strong> — a slightly more comfortable
pace than the <a href="/en/tcf-canada/">TCF Canada</a> and its 54 seconds, but over more questions.</p>

<h2 id="exercises">Two sample questions with answers: listening and reading</h2>

<p>The recording, the document, the questions and the options are in French, as on exam day; the answers are explained
underneath.</p>
""" + exo("en", 1, "B2 — listening", "Debate, several speakers",
          "« <strong>Lucas Berger :</strong> La France consacre environ un pour cent de son budget à la "
          "culture, un modèle envié dans le monde entier. Le ministère de la Culture, créé par Malraux en "
          "mille neuf cent cinquante-neuf, a démocratisé l'accès aux arts. Cependant, les pratiques "
          "culturelles restent très inégales. Selon les enquêtes, les cadres supérieurs vont quatre fois "
          "plus au théâtre que les ouvriers. »",
          "Que révèle la précision « un modèle envié dans le monde entier » ?",
          ["Que les autres pays ont tenté de copier le modèle français sans succès",
           "Que le budget culturel français est le plus élevé du monde en valeur absolue",
           "Que la France exporte ses politiques culturelles vers les pays en développement",
           "Que l'orateur cherche à légitimer le niveau de dépenses en invoquant une reconnaissance externe"],
          """D — <span lang="fr">Que l'orateur cherche à légitimer le niveau de dépenses</span> (that the speaker is trying to justify the level of spending)""",
          "the question is about the <strong>argumentative function</strong> of a phrase, not its content. Saying "
          "that a model is « envié » (envied) is an <em>argument from authority</em>: rather than justifying the "
          "spending on its own merits, the speaker validates it through outside recognition. The other three options "
          "take the phrase at face value.",
          audio="tcf_co_113.m4a", duree="51 s", ecoutes=1) + exo(
    "en", 2, "B2 — reading", "Document — institutional text:",
    "« La protection de l'enfance en France repose sur un principe fondamental : l'intérêt supérieur "
    "de l'enfant, inscrit dans la Convention internationale des droits de l'enfant ratifiée en 1990. "
    "Ce principe guide les décisions des juges des enfants et des travailleurs sociaux lorsqu'un "
    "conflit apparaît entre le maintien de l'enfant dans sa famille et sa protection face aux risques "
    "de maltraitance. »",
    "Quel conflit apparaît dans les décisions des acteurs de la protection de l'enfance ?",
    ["Le conflit entre les préférences des parents et celles des enfants",
     "Le conflit entre les services départementaux et les autorités nationales",
     "Le conflit entre la protection de l'enfant et le maintien en famille",
     "Le conflit entre les théories juridiques et les pratiques psychologiques"],
    """C — <span lang="fr">Entre la protection de l'enfant et le maintien en famille</span> (between protecting the child and keeping them in the family)""",
    "the sentence says it almost word for word: « lorsqu'un conflit apparaît entre le maintien de l'enfant dans "
    "sa famille et sa protection ». The difficulty comes from the <strong>syntactic density</strong>: the answer is "
    "buried in a long subordinate clause. In the TEF, institutional texts are common and call for slow reading.") + """

<h2 id="sections">The four writing and speaking sections</h2>

<p>This is where the TEF really differs from the TCF. The four sections have very specific instructions, which a
candidate trained on TCF practice material discovers on exam day.</p>
""" + table("What each section asks of you.", ["Section", "Instructions", "The trap"],
            [("<strong>Writing A</strong><br>25 min · 80 words min",
              "Write the <em>continuation</em> of an article or news story whose beginning you are given",
              "Breaking the register or the verb tense of the opening"),
             ("<strong>Writing B</strong><br>35 min · 200 words min", "A reasoned point of view", "Writing fewer than 200 words"),
             ("<strong>Speaking A</strong><br>5 min", "<em>Obtain information</em> by asking the examiner questions",
              "Staying in the position of the one being questioned"),
             ("<strong>Speaking B</strong><br>10 min", "Argue to convince, double marking", "Presenting without trying to convince")],
            wide=False) + """

<p>The topics are in French, as on exam day; what the examiner looks for is explained underneath.</p>
""" + sujet("en", "Writing, section B — sample topic", "35 minutes · 200 words minimum",
            "Sur un forum de parents d'élèves, un débat s'est ouvert autour de la question suivante : faut-il "
            "interdire les devoirs à la maison à l'école primaire ? Rédigez une contribution argumentée en "
            "présentant les avantages et les inconvénients de cette mesure, puis exprimez clairement votre "
            "position.",
            "<strong>200 words is a floor</strong>, and it is the first thing checked. The instructions set a "
            "three-part structure — advantages, disadvantages, position — which is your ready-made plan. The “forum "
            "contribution” genre allows a slightly less formal register than a formal letter, but it remains written "
            "and argued: no abbreviations, no spoken style.") + \
         sujet("en", "Speaking, section B — sample topic", "10 minutes · argue to convince",
            "Devrait-on rendre les transports en commun gratuits dans les grandes villes ? Présentez une "
            "argumentation équilibrée en examinant les conséquences économiques, sociales et écologiques de "
            "cette mesure.",
            "This section rewards <strong>convincing</strong> (« convaincre »): weigh both sides, as the instructions ask, then "
            "defend one while anticipating objections. The instructions name three angles — "
            "economic, social, environmental: covering all three is the simplest way to fill the ten minutes with a "
            "structure the examiner can hear.") + """

<h2 id="old-score">The “old score” column trap</h2>

<div class="note">
<p><strong>Your TEF results certificate shows two columns of scores.</strong> IRCC converts to CLB from the
<strong><em lang="fr">Équivalence ancien score</em></strong> (old-score equivalent) column — out of 300 in reading, out of
360 in listening, out of 450 for each of writing and speaking — and <em>not</em> from the column out of 699. Reading the
wrong column makes you think your CLB is much higher or much lower than it really is. It is the most frequent reading
error with the TEF, explained in detail on our <a href="/en/tef-canada/">TEF Canada</a> page.</p>
</div>

<p>In practice, for <strong>CLB 7</strong>: 207 in reading, 249 in listening, and 310 in both writing and speaking, on
those scales.</p>

<h2 id="method">The method</h2>

<ol>
<li><strong>Work on the four writing and speaking sections separately.</strong> They have nothing in common: speaking
section A, where you are the one asking the questions, has to be prepared as an exercise in its own right.</li>
<li><strong>Practise writing section A on varied openings.</strong> Picking up an imposed register and verb tense is a
mechanical skill, and one you acquire quickly.</li>
<li><strong>Time yourself at one minute per question</strong> in listening.</li>
<li><strong>Always check which column you are reading</strong> when you convert a practice score to CLB.</li>
<li><strong>Take a <a href="/en/tcf-canada-practice-test/">TCF Canada mock exam</a> too</strong> before choosing: no general
rule says one is easier; only your score in each format decides.</li>
</ol>
""",
    cta_h2="Sections A and B are something you can rehearse",
    cta_p="""Mock exams in the exact TEF Canada format (sections A and B of both writing and speaking), an automatic CLB
conversion from the right column, and AI feedback against the official criteria. In the “TCF DELF TEF: Tests 2026”
app.""",
    faq=[("How many questions are in the TEF Canada test?", "40 questions in reading (60 minutes) and 40 in listening (40 minutes), or about one minute per question in listening. Then come writing in two sections (60 minutes) and speaking in two sections (15 minutes), for a total of 2 h 55 min."),
         ("What is section A of the TEF Canada writing test?", "An exercise with no equivalent in the TCF: you are given the beginning of an article or news story and you have to write what comes next, in 25 minutes and at least 80 words. The mark penalizes any break in coherence with the opening — the register, verb tense and point of view are set by the beginning provided."),
         ("What is section A of the TEF Canada speaking test?", "A section where you are the one asking the questions: you have to obtain information from the examiner, in 5 minutes. This role reversal is counter-intuitive, and many candidates stay in the position of the one being questioned, say too little, and lose points on a section that is short and predictable."),
         ("What TEF Canada score do I need for CLB 7?", "207 to 232 in reading, 249 to 279 in listening, and 310 to 348 in both writing and speaking — on the “Équivalence ancien score” scales IRCC uses, not on the 699 column of your results certificate."),
         ("Why does my TEF results certificate show two scores?", "Because the TEF Canada publishes a score out of 699 and an “Équivalence ancien score” (old-score equivalent) column. IRCC converts to CLB from the second one. Always check which column you are reading before comparing your score with a conversion table."),
         ("Is the TEF easier than the TCF?", "No official source supports that claim. The skills assessed are the same, the exercises are not: the TEF has two long, specific sections where the TCF has three short tasks. The only reliable criterion is your own score in each format — take a mock exam of each.")],
    also=[("/en/tef-canada/", "TEF Canada: format, score chart and CLB levels", "The complete guide, with the CLB conversion table on the right scales."),
          ("/en/tcf-vs-tef-canada/", "TCF or TEF Canada: which one to choose?", "The comparison of the two tests IRCC accepts."),
          ("/en/tcf-canada-practice-test/", "Free TCF Canada practice test", "To take a TCF mock exam too before you choose.")],
    sources="""<strong>Formats change.</strong> This page is up to date as of 7 August 2026. The exercises shown are original
content from our app, designed in the official format. Check the current structure on
<a href="https://www.lefrancaisdesaffaires.fr/" rel="noopener">lefrancaisdesaffaires.fr</a> before your session.""",
))


# ===========================================================================
# TCF QUÉBEC — hub + modules (from /tcf-quebec/, /tcf-quebec/format-modulaire/,
# /tcf-quebec/echelle-quebecoise/, /tcf-quebec/prix-inscription/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/tcf-quebec/", lang="en", variant="en-CA", section="en", slug="tcf-quebec",
    crumbs=[HOME], crumb="TCF Québec", inline_cta=False,
    title="TCF Québec vs TCF Canada: format, score chart, fees",
    desc="TCF Québec: take 1 to 4 tests, scored on the Quebec scale (level 7 = 400 in listening, while CLB 7 = 458). Program thresholds, fees per test, centres.",
    h1="TCF Québec: the modular test for Quebec immigration",
    intro="""The TCF Québec is <strong>modular</strong>: you choose to take <strong>1, 2, 3 or 4 tests</strong>, instead of
the four required by the TCF Canada. Since several Quebec programs require only oral skills, many candidates take just
two tests — less preparation, less risk, and about half the price. Here is how it differs from the TCF Canada, the Quebec
scale it is scored on, the level each program requires, and what it costs.""",
    facts=["<strong>Modular</strong>: from 12 minutes (one test) to 2 h 22 min (all four).",
           "Quebec doesn’t use <strong>CLB levels</strong> (NCLC in French) but the <strong>Quebec scale</strong>, graded from 1 to 12.",
           "⚠️ <strong>Quebec level 7 ≠ CLB 7</strong>: 400 versus 458 in listening.",
           "⚠️ The TCF Québec <strong>is not accepted by IRCC</strong> for Express Entry; the full TCF Canada, on the other "
           "hand, has been recognized by Quebec since 2022.",
           "<strong>No English requirement</strong> in the PSTQ.",
           "Pay per test: €65 per module in Montpellier, €60 per test in Aix-Marseille, $105 to $125 per test at UQTR — taking "
           "only the oral tests costs about <strong>half</strong> as much as a full TCF Canada.",
           "Results must be under <strong>2 years</strong> old when you apply."],
    toc=[("what-is", "What is the TCF Québec?"), ("steps", "Your path in 5 steps"),
         ("modular", "The modular format, test by test"), ("vs-tcf-canada", "TCF Québec vs TCF Canada: which one?"),
         ("scale", "TCF Québec score chart: the Quebec scale"), ("level-7", "The trap: Quebec level 7 ≠ CLB 7"),
         ("programs", "Which level for which program"), ("points", "French points in the selection"),
         ("fees", "Fees, exemptions and alternatives"), ("where", "Where to take and book the TCF Québec?")],
    body="""
<div class="stats">
<div class="stat"><b>1 to 4</b><span>tests, your choice</span><em>you pay only for what you take</em></div>
<div class="stat"><b>699 / 20</b><span>listening and reading / writing and speaking</span><em>converted to the Quebec scale</em></div>
<div class="stat"><b>7–8</b><span>Quebec level = B2</span><em>≠ federal CLB 7–8</em></div>
<div class="stat"><b>2 years</b><span>maximum age of your results</span><em>when you apply</em></div>
</div>

<h2 id="what-is">What is the TCF Québec?</h2>
<p>The <strong>TCF Québec</strong> — « TCF pour le Québec », or TCF Q — is the version of the <em lang="fr">test de
connaissance du français</em> designed for <strong>Quebec’s immigration programs</strong>: those of Quebec’s immigration
ministry (MIFI, <em lang="fr">ministère de l’Immigration, de la Francisation et de l’Intégration</em>), including the
skilled worker selection program (PSTQ). What sets it apart: it is <strong>modular</strong>. You register for one, two,
three or four tests — listening, reading, speaking, writing — and you pay only for the ones you take.</p>

<p>Listening and reading are scored out of 699, writing and speaking out of 20, then converted onto the <strong>Quebec
scale</strong> of French proficiency levels, graded from 1 to 12 — a framework separate from the federal CLB, with which
it is often confused. The TCF Québec <strong>is not accepted by IRCC</strong> for Express Entry: for a federal application,
you need the <a href="/en/tcf-canada/">TCF Canada</a>, which Quebec has also recognized since 2022.</p>

<h3>Who it’s for</h3>
<ul>
<li>Candidates for <strong>Quebec</strong>’s programs — the PSTQ, the PEQ (Quebec Experience Program) — and their spouses:
several streams require only oral skills.</li>
<li>Those who want to <strong>pay per test</strong>: two oral tests cost about half as much as a full TCF Canada.</li>
<li>Not candidates for Express Entry, nor for Canadian citizenship.</li>
</ul>

<h2 id="steps">Your path in 5 steps</h2>
<ol class="steps">
<li><b>Check your program</b><span>PSTQ, PEQ, spouse: each stream requires different tests and levels. <a href="#programs">Which level for which program.</a></span></li>
<li><b>Choose your tests</b><span>The TCF Québec is modular: the two oral tests are often enough. <a href="#modular">Why it changes everything.</a></span></li>
<li><b>Read the right scale</b><span>A Quebec level 7 isn’t CLB 7. <a href="#scale">The official conversion table.</a></span></li>
<li><b>Test your level</b><span>A mock exam scored out of 699 and converted to the Quebec scale, test by test.</span></li>
<li><b>Register</b><span>The same centres as the TCF Canada, in Quebec as in France; the TCF Québec costs €65 per module in Montpellier and $105 to $125 per test at UQTR. <a href="#where">The centres.</a></span></li>
</ol>

<h2 id="modular">The modular format, test by test</h2>
<p>The TCF Québec is the only TCF where you choose your tests: <strong>29 questions</strong> in listening in 25 minutes, 29
in reading in 45, <strong>three exercises</strong> in writing in 60 minutes, three in speaking in 12 — each one independent.
It is the feature that really sets the TCF Québec apart, and candidates underuse it.</p>
""" + table("Official TCF Québec format. Each test is independent. Source: France Éducation international, consulted in July 2026.",
            ["Test", "Questions", "Time"],
            [("Listening", "29 multiple-choice questions", "25 min"),
             ("Reading", "29 multiple-choice questions", "45 min"),
             ("Writing", "3 exercises", "60 min"),
             ("Speaking", "3 exercises", "12 min <em>(including 2 min of preparation for task 2)</em>")], wide=False) + """

<p>In total: from <strong>12 minutes to 2 h 22 min</strong>, depending on what you choose. And several Quebec requirements
cover <strong>only oral skills</strong> — stream 2 of the PSTQ, and the condition set for an accompanying spouse. In those
cases, registering for the oral tests alone is perfectly sufficient. The writing and speaking tasks are the same as in
the TCF Canada.</p>

<p>That isn’t possible with the <a href="/en/tcf-canada/">TCF Canada</a> or with the TEF Canada, which require all four
tests. Only the TCF Québec and the TEFAQ are modular.</p>

<div class="note">
<p><strong>If you take the test on a computer</strong>, listening and reading have <strong>34 items instead of
29</strong>. The 5 extra items per skill <strong>don’t count towards your score</strong> — they are used for validity
analyses. Don’t worry if the test seems to run longer.</p>
</div>

<h2 id="vs-tcf-canada">TCF Québec vs TCF Canada: which one?</h2>
<p>The question comes up as soon as your plans aren’t set in stone, and the answer comes down to an asymmetry you need to
keep in mind.</p>
""" + table("Cross-acceptance of the two versions.", ["", "Accepted by Quebec (MIFI)", "Accepted by the federal government (IRCC)"],
            [("<strong>TCF Québec</strong>", "yes", "<strong>no</strong>"),
             ("<strong>TCF Canada</strong>", "yes", "yes")], wide=False) + """

<p><strong>The TCF Canada is accepted everywhere; the TCF Québec only in Quebec.</strong> The rule of thumb:</p>

<ul>
<li><strong>A strictly Quebec project, and only oral skills are required</strong> → TCF Québec. You take only two tests, for
about half the price.</li>
<li><strong>A Quebec project that might shift to Express Entry</strong> → TCF Canada. Taking all four tests costs more, but
it covers both routes.</li>
<li><strong>You are torn between the TCF and the TEF</strong> → see our comparison
<a href="/en/tcf-vs-tef-canada/">TCF or TEF Canada</a>, which sets out both conversion grids and the Quebec case.</li>
</ul>

<p>One last practical point: the waiting period between two attempts is <strong>20 days</strong>, and the number of
attempts is unlimited. But every attempt is paid for — hence the value of knowing where you stand <em>before</em> you
register, with a mock exam in the official format and feedback on your speaking against the official criteria: on
Quebec’s points grid, oral skills earn seven times more than written skills.</p>

<h2 id="scale">TCF Québec score chart: the Quebec scale</h2>
<p>Quebec doesn’t use the Canadian Language Benchmarks. It applies the <strong>Quebec scale of French proficiency
levels</strong> (<em lang="fr">Échelle québécoise des niveaux de compétence en français</em>), a government framework with
<strong>twelve levels</strong> in three stages: beginner (1 to 4), intermediate (5 to 8) and advanced (9 to 12).</p>
""" + table("TCF Québec → Quebec scale. Listening and reading scored out of 699, writing and speaking out of 20. Source: official table "
            "of Quebec’s immigration ministry (MIFI).",
            ["Quebec scale", "CEFR", "Listening and reading /699", "Writing and speaking /20"],
            [("1–2", "A1", "101–199", "1"), ("3", "A2", "200–259", "2–3"), ("<strong>4</strong>", "A2", "260–299", "4–5"),
             ("<strong>5–6</strong>", "B1", "300–399", "6–9"), ("<strong>7–8</strong>", "B2", "400–499", "10–13"),
             ("9–10", "C1", "500–599", "14–17"), ("11–12", "C2", "600–699", "18–20")], wide=False) + """

<p>Notice that <strong>the Quebec scale is much coarser than CLB</strong>: a 100-point band covers two levels at once.
That’s good news — the boundary is less abrupt than at the federal level, where a single point sometimes separates two
levels.</p>

<h2 id="level-7">The trap: Quebec level 7 ≠ CLB 7</h2>
<div class="note">
<p><strong>The two frameworks use the same numbers and don’t cover the same scores.</strong> In listening, <strong>Quebec
level 7 starts at 400</strong>, whereas <strong>federal CLB 7 starts at 458</strong>. A score of 430 therefore gives you
level 7 in Quebec — and only CLB 6 at the federal level.</p>
</div>

<p>This confusion is costly for candidates preparing both routes in parallel, or reading a forum without checking which
framework is meant. Remember the simple rule: if the text says “CLB”, it’s federal; if it says “level” or “Quebec scale”,
it’s Quebec. For the federal thresholds in detail, see our article <a href="/en/tcf-canada-clb-7/">TCF Canada CLB 7</a>.</p>

<h2 id="programs">Which level for which program</h2>
""" + table("French requirements by Quebec program, on the Quebec scale. Source: Quebec’s immigration ministry (MIFI).",
            ["Program / stream", "Oral", "Written"],
            [("<strong>PSTQ stream 1</strong> — highly skilled (TEER 0, 1, 2)", "level <strong>7</strong> or higher", "level <strong>5</strong> or higher"),
             ("<strong>PSTQ stream 2</strong> — intermediate and manual skills (TEER 3, 4, 5)", "level <strong>5</strong> or higher", "no requirement"),
             ("<strong>PSTQ stream 3</strong> — regulated professions", "7 (TEER 0–2) · 5 (TEER 3–5)", "5 if TEER 0–2"),
             ("<strong>PEQ</strong> — Quebec graduates stream", "—", "level <strong>5</strong>"),
             ("<strong>Accompanying spouse</strong>", "level <strong>4</strong> or higher", "no requirement")], wide=False) + """

<p>In concrete TCF Québec scores:</p>

<ul>
<li><strong>Oral level 7</strong> = at least <strong>400/699</strong> in listening and <strong>10/20</strong> in
speaking.</li>
<li><strong>Written level 5</strong> = at least <strong>300/699</strong> in reading and <strong>6/20</strong> in
writing.</li>
<li><strong>Spouse, oral level 4</strong> = <strong>260/699</strong> in listening and <strong>4/20</strong> in
speaking.</li>
</ul>

<p>The spouse threshold is deliberately low: two modular tests are enough, and the level required remains A2. It’s the
textbook case where the TCF Québec saves time and money compared with a full test.</p>

<p><strong>Good to know:</strong> there is <strong>no English requirement in the PSTQ</strong>. English can optionally be
declared in the expression of interest, and the only test accepted to earn credit for it is IELTS.</p>

<h2 id="points">French points in the selection</h2>
<p>Beyond the eligibility thresholds, French earns points — and the grid is heavily weighted towards oral skills.</p>
""" + table("MIFI points grid based on the CEFR levels obtained in the TCF. Source: Quebec’s immigration ministry (MIFI).",
            ["Test", "A1 to B1", "B2", "C1", "C2"],
            [("Listening", "0", "<strong>5</strong>", "<strong>6</strong>", "<strong>7</strong>"),
             ("Speaking", "0", "<strong>5</strong>", "<strong>6</strong>", "<strong>7</strong>"),
             ("Reading", "0", "1", "1", "1"),
             ("Writing", "0", "1", "1", "1")], wide=False) + """

<p><strong>Oral skills are worth up to 14 points, written skills only 2</strong>, for a maximum of 16. In other words: if
you have to divide your preparation time, <strong>oral skills earn seven times more than written skills</strong>. That
is the opposite of what many candidates assume — they spend most of their preparation on written grammar.</p>

<p>Note the abrupt threshold, too: below B2, a test earns <strong>zero points</strong>. Going from B1 to B2 in speaking
means going from 0 to 5 points.</p>

<h2 id="fees">Fees, exemptions and alternatives</h2>
<p>Because it is modular, the TCF Québec is the cheapest TCF when your process requires only oral skills:
<strong>€65 per module</strong> at the Alliance française de Montpellier, <strong>$105 to $125 per test</strong> at UQTR,
versus $440 for a full TCF Canada at the same centre. There is <strong>no national fee</strong>: each approved centre sets
its own, and many don’t publish it at all. Here are three centres that post their per-test fees, checked on 30 July
2026.</p>
""" + table("TCF Québec fees per test at three centres that publish their fee schedule, checked on 30 July 2026. For guidance only — "
            "check with your centre before you register.",
            ["Centre", "Per test", "The two oral tests"],
            [("<strong>EIF – UQTR</strong><br>Trois-Rivières, Quebec", "Listening $105 · reading $105 · writing $105 · speaking $125", "<strong>$230 (CAD)</strong>"),
             ("<strong>AF Montpellier</strong><br>France", "€65 per module", "<strong>€130</strong>"),
             ("<strong>AF Aix-Marseille</strong><br>France", "€60 per test", "<strong>€120</strong>")], wide=False) + """

<p>The gain from modularity shows directly in these figures. At the same Quebec centre, the
<a href="/en/tcf-canada/">TCF Canada</a> has a <strong>fixed fee: $440 (CAD)</strong> for the four compulsory tests.
Taking only the oral tests of the TCF Québec therefore costs <strong>$230 instead of $440</strong> — roughly half, with two
tests to prepare instead of four.</p>

<div class="note">
<p><strong>Be wary of the fees circulating online.</strong> Many centres, including the <strong>Alliance Française de
Montréal</strong>, publish <em>no</em> fee for the TCF: registration is online, subject to availability, and the only
amount shown is a $75 cancellation fee. The fees that aggregator and comparison sites attribute to these centres are
unsourced, and often mix up the TCF Québec and the TCF Canada — two versions with different fees. Ask the centre itself
for its fee before you commit.</p>
</div>

<p><strong>Exemptions.</strong> Quebec also recognizes, in place of the TCF Québec: the <strong>TCF tout public together
with the speaking test</strong>, as well as the DELF and DALF diplomas — provided you have a minimum mark in listening and
in speaking, and that they are less than two years old. A DELF or DALF you already hold can therefore spare you a
test.</p>

<p><strong>The full list of tests accepted by MIFI</strong> has eight entries: TCF Québec, TCF Canada, TCF, DALF and DELF
from France Éducation international; TEFAQ, <a href="/en/tef-canada/">TEF Canada</a> and TEF from the CCI Paris
Île-de-France. Results must be <strong>two years old or less</strong> on the date of the application for permanent
selection, and a full scan of the results certificate is required.</p>

<p>Finally, the expression of interest is submitted free of charge online, on the <strong>Arrima</strong> platform. You
must be 18 or older and intend to live and work in Quebec.</p>

<h2 id="where">Where to take and book the TCF Québec?</h2>
<p>At the same approved centres as the TCF Canada: in Canada, almost all of the 47 centres on France Éducation
international’s list offer both (Alliance Française de Montréal, Collège Stanislas, UQTR, UQAM…); in France, the Alliance
française de Montpellier (€65 per module), Aix-Marseille (€60 per test), ACCORD in Paris, CLPS in Rennes… Our guides to
where to take the TCF Canada <a href="/en/tcf-canada-test-centres/">in Canada</a> and in France (in French) list these
centres with their registration and cancellation rules; in North Africa, our guides for Morocco (TCF Québec at 2,900
dirhams) and Tunisia (880 dinars, or 2 to 3 tests as a package), in French, apply to both tests.</p>

<p>Centres we checked in our guides, among the 47 approved in Canada and the 251 in France — all with computer-based
sessions: the Alliance Française de Montréal, Collège Stanislas (Montreal), the Université du Québec à Trois-Rivières
(École internationale de français), the Alliance française de Montpellier and the Alliance française Aix-Marseille
Provence.</p>
<p class="more">Full directory, with addresses and phone numbers: <a href="/en/tcf-canada-test-centres/">the 47 TCF centres
in Canada</a> · <a href="/en/">all locations in English</a>. The directory of the 251 centres in France is in French.</p>
<p class="serie-label">Where to take it, city by city</p>
<div class="chips">
<a class="chip" href="/en/tcf-canada-montreal/">TCF in Montreal</a>
<a class="chip" href="/en/tcf-canada-quebec-city/">TCF in Quebec City</a>
<a class="chip" href="/en/tcf-canada-test-centres/">All of Canada →</a>
</div>
""",
    cta_h2="Find out whether you have level 7 before paying to register",
    cta_p="""Timed mock exams in the exact TCF Québec format, an immediate conversion to the Quebec scale and the CEFR for each
test, and AI feedback on writing and speaking against the official criteria — in the “TCF DELF TEF: Tests 2026” app.""",
    faq=[("What is the TCF Québec?", "The modular version of the <em lang=\"fr\">Test de connaissance du français</em> designed for the immigration programs of Quebec (MIFI): you register for one, two, three or four tests of your choice. Scores are converted onto the Quebec scale, graded from 1 to 12, which is separate from the federal CLB."),
         ("TCF Québec vs TCF Canada: which one should I take?", "For a federal application — Express Entry, citizenship — only the TCF Canada is accepted. For a Quebec program, both are: the TCF Québec lets you take only the tests required and costs less; the full TCF Canada works for both levels of selection at once."),
         ("Is the TCF Québec valid everywhere in Canada?", "No. It is recognized only by Quebec’s immigration ministry. IRCC accepts it neither for Express Entry nor for citizenship."),
         ("Can I take only the TCF Québec speaking test?", "Yes. The TCF Québec is modular: you choose to take 1, 2, 3 or 4 tests. That is its major difference from the TCF Canada, where all four tests are compulsory. Since stream 2 of the PSTQ and the requirement for an accompanying spouse cover only oral skills, many candidates register only for listening and speaking."),
         ("Is the TCF Québec accepted for Express Entry?", "No. IRCC accepts only the TCF Canada and the TEF Canada for federal economic immigration. The TCF Québec, the TCF tout public and the TCF IRN aren’t on the federal list. Quebec, on the other hand, accepts the TCF Canada. If your plans might shift to the federal route, the TCF Canada is therefore the safest choice."),
         ("What score do I need for level 7 on the Quebec scale?", "In the TCF Québec, level 7 corresponds to 400 out of 699 in listening and 10 out of 20 in speaking. Don’t confuse it with federal CLB 7, which starts at 458 in listening: a score of 430 gives you level 7 in Quebec but only CLB 6 at the federal level."),
         ("Which tests does Quebec accept for the PSTQ?", "Eight: the TCF Québec, the TCF Canada, the TCF, the DALF and the DELF from France Éducation international; the TEFAQ, the TEF Canada and the TEF from the CCI Paris Île-de-France. Results must be two years old or less on the date of your application for permanent selection."),
         ("Do I need English for the PSTQ?", "No. The ministry states that there is no English requirement in the PSTQ. English can optionally be declared in the expression of interest, and the only test accepted to earn credit for it is IELTS."),
         ("How much does the TCF Québec cost?", "Each approved centre sets the fee; there is no national fee — and many centres don’t publish it. Among those that do, checked on 30 July 2026: the École internationale de français at UQTR, in Trois-Rivières, charges $105 (CAD) for listening, $105 for reading, $105 for writing and $125 for speaking; the Alliance française de Montpellier charges €65 per module. Taking only the two oral tests therefore comes to $230 (CAD) at UQTR, or €130 in Montpellier — versus $440 (CAD) for a full TCF Canada at the same Quebec centre. Be wary of unsourced fees on comparison sites: several large centres, including the Alliance Française de Montréal, publish no fee."),
         ("How do I book the TCF Québec exam?", "With an approved centre — the same ones as for the TCF Canada: in Canada, almost all of the 47 centres on France Éducation international’s list offer both; in France, for example, the Alliance française de Montpellier, Aix-Marseille, ACCORD in Paris or CLPS in Rennes. Each centre has its own registration and cancellation rules: at the Alliance Française de Montréal, registration is online, subject to availability, and the only amount shown is a $75 cancellation fee. Ask the centre for its fee before you commit.")],
    also=[("/en/tcf-canada-clb-7/", "TCF Canada CLB 7: the exact scores", "The federal thresholds — not to be confused with the Quebec scale."),
          ("/en/tcf-vs-tef-canada/", "TCF or TEF Canada: which one to choose?", "The full comparison, with a section on Quebec and the TEFAQ."),
          ("/en/tef-canada/", "TEF Canada and TEFAQ", "The TEFAQ, the TCF Québec’s direct competitor: the same program requirements, in the TEF format.")],
    sources="""<strong>Rules change.</strong> This page is up to date as of 30 July 2026 and is not immigration advice. The
thresholds, points grids and calendars of Quebec’s programs change regularly. Always check your situation on
<a href="https://www.quebec.ca/immigration" rel="noopener">quebec.ca</a> and the exam format on
<a href="https://www.france-education-international.fr/test/tcf-quebec" rel="noopener">france-education-international.fr</a>
before you register or apply.""",
))
