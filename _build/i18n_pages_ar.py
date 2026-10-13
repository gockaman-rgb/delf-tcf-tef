# -*- coding: utf-8 -*-
"""Guides et pages d'examen en arabe (/ar/, make_i18n.py) — traductions de pages françaises, 13/10/2026.

Arabe standard moderne (فصحى). Aucun fait nouveau : chaque chiffre, date et règle vient de la page française
(fr_path), avec sa date. Les exercices et sujets restent en français (examen de français, dir="ltr") ;
consignes et explications en arabe. Chiffres occidentaux (0-9), comme dans l'app.

Bidi — ce qui se renverse en droite-à-gauche et que check_i18n.py refuse hors isolat :
- une plage « 458–502 » : dans un tableau, ltr("458–502") ; dans une phrase, « من 458 إلى 502 » ;
- « 10+ » : « 10 فأكثر » ;
- un téléphone : <bdi dir="ltr">…</bdi>.
Une note « 10/20 » ou « 458/699 » ne bouge pas. Un en-tête de colonne écrit « (على 699) », pas « /699 ».
App : l'interface de l'app iOS est traduite en arabe ; jamais « entièrement en arabe », rien sur Android.
Glossaire : i18n_glossary.md (section arabe) ; blocs : i18n_blocks.py (CALC_AR, exo/sujet avec lang="ar").
"""
from i18n_blocks import CALC_AR, exo, sujet  # noqa: F401
from pays_config import table

PAGES = []
HOME = ("الرئيسية", "/ar/")
TCF = ("TCF كندا", "/ar/tcf-canada/")


def ltr(x):
    """Isolat gauche-à-droite : plages de nombres, téléphones, codes."""
    return f'<bdi dir="ltr">{x}</bdi>'


# ===========================================================================
# TCF CANADA — الدرجات وحاسبة NCLC (de /tcf-canada/score-nclc/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/tcf-canada/score-nclc/", lang="ar", variant="ar", slug="tcf-canada-nclc",
    crumbs=[HOME, TCF], crumb="الدرجات وNCLC", inline_cta=False,
    title="درجات TCF Canada وحاسبة NCLC: الجدول الرسمي 2026",
    desc="حوّل درجاتك في TCF Canada إلى مستويات NCLC بالحاسبة وجدول IRCC: يتطلب NCLC 7 درجة 458 في فهم المسموع و453 في فهم المقروء و10/20 في التعبير.",
    h1="درجات TCF Canada ومستويات NCLC: الحاسبة والجدول",
    intro="""في TCF Canada، يُقيَّم فهم المسموع وفهم المقروء على مقياس من 100 إلى 699، والتعبير الشفهي والتعبير الكتابي
من 1 إلى 20؛ وتقابل كل درجة مستوى في الإطار الأوروبي المرجعي، ثم <strong>مستوى NCLC</strong> (مستويات الكفاءة اللغوية
الكندية)، وهو المستوى الوحيد الذي تعتمده دائرة الهجرة واللاجئين والمواطنة الكندية (IRCC). يتطلب NCLC 7 درجة 458 في فهم المسموع و453 في فهم
المقروء و10 من 20 في التعبير الشفهي والكتابي — لذلك لا يكفي دائمًا مستوى «B2» المكتوب في شهادة نتائجك. إليك الجدولين،
وما يعنيانه لملفك.""",
    facts=["يُقيَّم فهم المسموع وفهم المقروء على <strong>699</strong>، والتعبير الشفهي والكتابي على <strong>20</strong>.",
           "<strong>NCLC 7</strong> = 458 في فهم المسموع، و453 في فهم المقروء، و10/20 في التعبير الشفهي وفي التعبير الكتابي.",
           "<strong>NCLC 9</strong> = 523 في فهم المسموع، و524 في فهم المقروء، و14/20 في التعبير الشفهي وفي التعبير الكتابي.",
           "⚠️ يبدأ مستوى B2 عند 400: فدرجة B2 قدرها 420 في فهم المسموع لا تساوي إلا NCLC 6.",
           "للجلسات المنعقدة منذ 1 سبتمبر 2026، لم تعد إعادة التصحيح ممكنة."],
    toc=[("calculator-title", "حاسبة تحويل درجات TCF Canada إلى NCLC"), ("scoring", "كيف تُحتسب درجاتك"),
         ("tcf-to-nclc", "من درجة TCF إلى مستوى NCLC")],
    body=CALC_AR + """
<h2 id="scoring">كيف تُحتسب درجاتك</h2>
<p>إن TCF <strong>اختبار لتحديد المستوى، لا امتحان يمكن الرسوب فيه</strong>. لا توجد درجة دنيا لكل اختبار ولا علامة
نجاح: تحصل على درجة لكل اختبار، والجهة التي تتلقى ملفك هي التي تقرر إن كانت هذه الدرجة كافية.</p>
""" + table("نطاقات درجات TCF ومستويات الإطار الأوروبي المرجعي المقابلة لها. المصدر: الوثائق الرسمية لاختبار TCF، "
            "<bdi>France Éducation international</bdi>.",
            ["مستوى الإطار الأوروبي", "فهم المسموع والمقروء (على 699)", "التعبير الشفهي والكتابي (على 20)"],
            [("دون A1", ltr("0–99"), "—"), ("A1", ltr("100–199"), "1"), ("A2", ltr("200–299"), ltr("2–5")),
             ("B1", ltr("300–399"), ltr("6–9")), ("B2", ltr("400–499"), ltr("10–13")), ("C1", ltr("500–599"), ltr("14–17")),
             ("C2", ltr("600–699"), ltr("18–20"))], wide=False) + """
<p>درجتك في فهم المسموع وفهم المقروء ليست عدد إجاباتك الصحيحة: بل يحسبها نموذج يراعي صعوبة الأسئلة التي طُرحت عليك.
وقد يحصل مرشحان لهما العدد نفسه من الإجابات الصحيحة على درجتين مختلفتين.</p>

<h2 id="tcf-to-nclc">من درجة TCF إلى مستوى NCLC</h2>
<p>في ملفك الكندي، الشيء الوحيد الذي يُحتسب هو مستوى NCLC — <em lang="fr">Niveaux de compétence linguistique
canadiens</em>، أي مستويات الكفاءة اللغوية الكندية — الذي تقع فيه كل درجة من درجاتك الأربع. إليك جدول التحويل الرسمي.</p>
""" + table("تحويل درجات TCF Canada إلى NCLC: فهم المسموع والمقروء على 699، والتعبير الشفهي والكتابي على 20. المصدر: "
            "جداول المعادلة لدى IRCC، طابقناها مع صفحتين رسميتين في 27 يوليو 2026.",
            ["NCLC", "فهم المسموع", "فهم المقروء", "التعبير الشفهي", "التعبير الكتابي"],
            [("10 فأكثر", ltr("549–699"), ltr("549–699"), ltr("16–20"), ltr("16–20")),
             ("9", ltr("523–548"), ltr("524–548"), ltr("14–15"), ltr("14–15")),
             ("8", ltr("503–522"), ltr("499–523"), ltr("12–13"), ltr("12–13")),
             ("<strong>7</strong>", "<strong>" + ltr("458–502") + "</strong>", "<strong>" + ltr("453–498") + "</strong>",
              "<strong>" + ltr("10–11") + "</strong>", "<strong>" + ltr("10–11") + "</strong>"),
             ("6", ltr("398–457"), ltr("406–452"), ltr("7–9"), ltr("7–9")), ("5", ltr("369–397"), ltr("375–405"), "6", "6"),
             ("4", ltr("331–368"), ltr("342–374"), ltr("4–5"), ltr("4–5"))], wide=False) + """
<p><strong>«لديّ B2، إذن لديّ NCLC 7» خطأ.</strong> يبدأ B2 عند 400 في فهم المسموع، ويبدأ NCLC 7 عند 458: بينهما 58
نقطة ومستوى NCLC كامل. إنه أغلى سوء فهم في TCF Canada، وله صفحة مفصّلة بالإنجليزية:
<a href="/en/tcf-canada-clb-7/" lang="en">TCF Canada CLB 7: the exact scores to aim for</a>، اختبارًا اختبارًا.</p>

<p><strong>أضعف اختبار لديك هو الذي يحسم.</strong> تنظر IRCC إلى ملفك كاملًا، ومستوى NCLC 9 في فهم المقروء لا يعوّض
NCLC 6 في فهم المسموع. ومن هنا تنبع استراتيجية تحضيرك مباشرة.</p>
""",
    cta_h2="اعرف مستواك قبل أن تدفع 440 دولارًا كنديًا",
    cta_p="""امتحانات تجريبية محدَّدة الوقت بالصيغة الدقيقة لاختبار TCF Canada، وتحويل تلقائي إلى NCLC لكل اختبار، وملاحظات بالذكاء
الاصطناعي على التعبير الكتابي والشفهي وفق المعايير الرسمية — في تطبيق «<bdi>TCF DELF TEF: Tests 2026</bdi>». واجهة
التطبيق على iPhone متاحة بالعربية.""",
    faq=[("ما الدرجة المطلوبة في TCF Canada لبلوغ NCLC 7؟", "458 في فهم المسموع، و453 في فهم المقروء، و10 من 20 في كلٍّ من التعبير الشفهي والتعبير الكتابي. وبلوغ NCLC 7 في المهارات الأربع هو الحد المرجعي لبرنامج العمال المهرة الفيدرالي. وبنقطة واحدة أقل تنزل إلى NCLC 6.")],
    also=[("/ar/tcf-canada/", "امتحان TCF كندا", "الاختبارات الأربعة ومدتها والدرجات المطلوبة للهجرة."),
          ("/ar/tcf-canada-practice-test/", "امتحان TCF Canada تجريبي مجاني", "تحقّق من مستواك بالصيغة الحقيقية قبل الحجز."),
          ("/ar/tcf-canada-preparation/", "التحضير لاختبار TCF Canada", "كم من الوقت تحتاج، ومن أين تبدأ.")],
    sources="""<strong>القواعد تتغيّر.</strong> هذه الصفحة محدّثة حتى 7 أغسطس 2026 وليست استشارة في الهجرة: الحدود وجداول
التحويل وجولات الدعوات تتغيّر بانتظام. تحقّق دائمًا من وضعك على <a href="https://www.canada.ca/" rel="noopener">canada.ca</a>
ومن صيغة الامتحان على <a href="https://www.france-education-international.fr/" rel="noopener">france-education-international.fr</a>
قبل التسجيل أو تقديم الطلب.""",
))


# ===========================================================================
# Lots traduits le 13/10/2026, chacun dans son module (ses aides ltr/b/fr restent locales) :
# page pilier TCF Canada, préparation, prix et inscription, TCF ou TEF (core) ; examen blanc, expression écrite,
# expression orale (practice).
# ===========================================================================
from i18n_pages_ar_core import PAGES as _CORE  # noqa: E402
from i18n_pages_ar_practice import PAGES as _PRACTICE  # noqa: E402

PAGES += _CORE + _PRACTICE
