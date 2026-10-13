# -*- coding: utf-8 -*-
"""Pages pays en arabe (/ar/, make_pays.py) et accueil /ar/ — 13/10/2026.

Aucun fait nouveau : chaque page reprend la page anglaise appariée (pair=…), elle-même tirée de la liste FEI et des
sites des centres, avec ses dates (Émirats : relevé du 8 octobre 2026 ; Arabie saoudite, Égypte, Liban et TEF aux
Émirats : 13 octobre 2026). Arabe standard moderne, chiffres occidentaux ; bidi : plages en « من … إلى … » ou ltr(),
coordonnées isolées par make_pays.card(). Les noms d'établissement restent en caractères latins, isolés (<bdi>).
"""
from pays_i18n import NR as _NR, releve, table  # noqa: F401

NR = _NR["ar"]
PAGES = []
CA = [("ok", "TCF Canada")]
AE = dict(list_date="8 أكتوبر 2026", releve_date="8 أكتوبر 2026", date_label="13 أكتوبر 2026", published="2026-10-13")
ME = dict(list_date="13 أكتوبر 2026", releve_date="13 أكتوبر 2026", date_label="13 أكتوبر 2026", published="2026-10-13")


def b(x):
    """Isolat pour un nom latin entouré de ponctuation arabe."""
    return f"<bdi>{x}</bdi>"


def ltr(x):
    return f'<bdi dir="ltr">{x}</bdi>'


AFD, AFAD = b("Alliance Française de Dubai"), b("Alliance Française Abu Dhabi")
AFAS = b("Alliance française d’Arabie Saoudite")
IFE, IFL = b("Institut français d’Égypte"), b("Institut français du Liban")
FEI = b("France Éducation international")

# ===========================================================================
# الإمارات — appariée à /en/tcf-canada-dubai/
# ===========================================================================
PAGES.append(dict(AE,
    lang="ar", variant="ar", og_locale="ar_AE", fr_path=None, pair="/en/tcf-canada-dubai/", slug="tcf-canada-uae",
    country_name="الإمارات العربية المتحدة", exam="tcf", file="tcf_emirats", layout="cities",
    crumb="TCF Canada في الإمارات",
    title="امتحان TCF Canada في دبي وأبوظبي: 1800 درهم والمواعيد",
    desc="امتحان TCF Canada في الإمارات: مركزان لـ Alliance Française في دبي ومركز في أبوظبي، 1800 درهم على الحاسوب، أقرب الجلسات ومواعيد التسجيل وشروط الحجز.",
    h1="امتحان TCF Canada في الإمارات: المراكز والرسوم والمواعيد",
    intro=f"""في الإمارات العربية المتحدة، تعتمد {FEI} {{n}} مراكز لامتحان TCF. وفي 8 أكتوبر 2026 كانت <strong>{AFD}</strong>
— في عود ميثاء وفي دبي نولدج بارك — و<strong>{AFAD}</strong> تقدّمان TCF Canada بسعر <strong>1800 درهم</strong> في
المراكز كلها، على الحاسوب. في دبي كانت جلسات 20 و21 و27 أكتوبر مكتملة، وأول موعد متاح كان <strong>الجمعة 30 أكتوبر</strong>
(التسجيل حتى 21 أكتوبر)؛ وفي أبوظبي كانت الجلسة التالية <strong>الجمعة 23 أكتوبر</strong> (التسجيل حتى 12 أكتوبر). ولا يذكر
تقويم 2026 امتحان TCF إلا في مركز أبوظبي، لا في العين.""",
    facts=["<strong>{n} مراكز معتمدة</strong> (قائمة FEI في 8 أكتوبر 2026)؛ يُعقد TCF Canada في <strong>دبي</strong> (عود ميثاء ودبي نولدج بارك) و<strong>أبوظبي</strong>؛ أما العين فمدرجة في قائمة FEI، لكن تقويم 2026 لا يحدّد فيها أي جلسة لامتحان TCF.",
           "الرسوم: <strong>1800 درهم</strong> في دبي وأبوظبي (وفي أبوظبي: TCF IRN بـ1380 درهمًا، وTCF tout public بـ900 درهم).",
           "دبي: جلسات 20 و21 و27 أكتوبر <strong>مكتملة</strong>، وتسع جلسات متاحة من <strong>30 أكتوبر</strong> إلى 22 ديسمبر 2026.",
           "أبوظبي: <strong>23 أكتوبر</strong> (التسجيل حتى 12 أكتوبر)، ثم 20 نوفمبر و16 ديسمبر.",
           "الامتحان على الحاسوب في المدينتين؛ وفي دبي لا إعادة تصحيح ولا استرداد للرسوم بعد إغلاق فترة التسجيل."],
    stats=[("1800 درهم", "TCF Canada", "دبي وأبوظبي"), ("30 أكتوبر", "أول موعد متاح في دبي", "التسجيل حتى 21 أكتوبر"),
           ("23 أكتوبر", "الجلسة التالية في أبوظبي", "التسجيل حتى 12 أكتوبر"), ("سنتان", "مدة الصلاحية", "النتائج بعد بضعة أسابيع")],
    sections=[
        ("dubai", f"{AFD}: الجلسات", table(
            f"جلسات TCF Canada على صفحة الحجز لدى {AFD} في 8 أكتوبر 2026. OM = عود ميثاء (الشارع 18)، DKP = دبي نولدج بارك (المبنى 2B).",
            ["التاريخ", "المركز", "التسجيل حتى", "الحالة"],
            [("الثلاثاء 20 أكتوبر 2026", "OM", "11 أكتوبر", "<strong>مكتملة</strong>"), ("الأربعاء 21 أكتوبر", "DKP", "11 أكتوبر", "<strong>مكتملة</strong>"),
             ("الثلاثاء 27 أكتوبر", "OM", "18 أكتوبر", "<strong>مكتملة</strong>"), ("<strong>الجمعة 30 أكتوبر</strong>", "OM", "21 أكتوبر", "متاحة"),
             ("الثلاثاء 3 نوفمبر", "OM", "25 أكتوبر", "متاحة"), ("الثلاثاء 10 نوفمبر", "OM", "1 نوفمبر", "متاحة"),
             ("الثلاثاء 24 نوفمبر", "OM", "15 نوفمبر", "متاحة"), ("الأربعاء 25 نوفمبر", "DKP", "15 نوفمبر", "متاحة"),
             ("الثلاثاء 8 ديسمبر", "OM", "29 نوفمبر", "متاحة"), ("الثلاثاء 15 ديسمبر", "OM", "6 ديسمبر", "متاحة"),
             ("الأربعاء 16 ديسمبر", "OM", "6 ديسمبر", "متاحة"), ("الثلاثاء 22 ديسمبر", "OM", "13 ديسمبر", "متاحة")], wide=False) + """
<p>لا يُظهر تقويم الـAlliance بصيغة PDF (المؤرخ في 24 سبتمبر) جلسة 30 أكتوبر بعد، ويضع جلسة 16 ديسمبر في دبي نولدج بارك:
عند الاختلاف، صفحة الحجز — حيث تدفع — هي المرجع. تحجز عبر الإنترنت أو في المكاتب، خلال فترة التسجيل فقط؛ ويتأكد تسجيلك
بعد الدفع ورفع نسخة من جواز سفرك، ويصلك إشعار يوم الامتحان بالبريد الإلكتروني قبل أسبوع. لا تُستردّ الرسوم إلا إذا ألغيت
خلال فترة التسجيل؛ وبعد إغلاقها لا استرداد ولا رصيد، حتى في حال الغياب، ولا تُقبل إعادة التصحيح.</p>"""),
        ("abu-dhabi", AFAD, f"""<p>تعقد {AFAD} امتحان TCF Canada في مركزها بأبوظبي (البطين)، على الحاسوب، بسعر <strong>1800
درهم</strong>: <strong>الجمعة 23 أكتوبر</strong> (التسجيل من 1 سبتمبر إلى 12 أكتوبر)، و<strong>الجمعة 20 نوفمبر</strong>
(من 1 أكتوبر إلى 9 نوفمبر)، و<strong>الأربعاء 16 ديسمبر 2026</strong> (من 15 أكتوبر إلى 6 ديسمبر). ويذكر تقويمها أيضًا TCF
IRN (1380 درهمًا) وTCF tout public (900 درهم). تختار موعدًا وتحجز عبر الإنترنت، وتصدر النتائج «بعد بضعة أسابيع». لا ينشر
الموقع أي قاعدة للإلغاء أو لإعادة التصحيح، ولا يذكر سطر TCF في تقويمه إلا مركز أبوظبي.</p>"""),
        ("tef-canada", "TEF Canada في دبي وأبوظبي", f"""<p>إن <a href="/ar/tcf-or-tef-canada/">TEF Canada</a> — اختبار
الفرنسية الآخر الذي تقبله IRCC — تديره {b("Le français des affaires (CCI Paris Île-de-France)")}، لا {FEI}، لذلك لا تظهر
مراكزه في القائمة أدناه. وفي 13 أكتوبر 2026، كانت {AFD} تذكر TEF Canada ضمن «الاختبارات المقبولة» إلى جانب TCF Canada
وTCF Québec، مع زر للحجز، وكانت لدى {AFAD} صفحة خاصة بـ TEF Canada. لم تُظهر أي من الصفحتين موعدًا أو سعرًا في ذلك اليوم،
ولم نبحث في الدليل الرسمي لمراكز TEF Canada (لا يعرض النتائج إلا بعد إرسال نموذج بحث): تحقّق من المواعيد والرسوم على صفحات الحجز لدى
المركزين.</p>"""),
    ],
    list_title="المراكز المعتمدة لامتحان TCF في الإمارات ({n})",
    faq=[("أين يمكنني اجتياز TCF Canada في دبي؟", "لدى Alliance Française de Dubai، التي تعقده في عود ميثاء (الشارع 18) ودبي نولدج بارك (المبنى 2B)، على الحاسوب، بسعر 1800 درهم. في 8 أكتوبر 2026 كانت جلسات 20 و21 و27 أكتوبر مكتملة، وأول جلسة متاحة كانت الجمعة 30 أكتوبر، والتسجيل حتى 21 أكتوبر."),
         ("كم سعر امتحان TCF Canada في الإمارات؟", "1800 درهم لدى Alliance Française de Dubai ولدى Alliance Française Abu Dhabi، كما نُشر في 8 أكتوبر 2026."),
         ("هل يمكنني اجتياز TCF Canada في أبوظبي أو العين؟", "في أبوظبي، نعم: 23 أكتوبر و20 نوفمبر و16 ديسمبر 2026 لدى Alliance Française Abu Dhabi. أما تقويم 2026 فلا يذكر امتحان TCF في فرع العين."),
         ("هل يمكنني استرداد الرسوم إذا لم أحضر؟", "في دبي، فقط إذا ألغيت خلال فترة التسجيل؛ وبعد إغلاقها لا استرداد ولا رصيد، حتى في حال الغياب. ولا تنشر أبوظبي أي قاعدة."),
         ("هل تقبل IRCC امتحان TCF Canada الذي أجتازه في الإمارات؟", "نعم: تصدر شهادة النتائج عن France Éducation international أيًّا كان المركز المعتمد الذي اجتزت فيه الامتحان، وهي صالحة لمدة سنتين.")],
    also=[("/ar/tcf-canada-saudi-arabia/", "TCF Canada في السعودية", "جدة والرياض، 1950 ريالًا."),
          ("/ar/tcf-canada-price/", "سعر امتحان TCF Canada والتسجيل", "الرسوم بلدًا بلدًا وطريقة الحجز."),
          ("/ar/tcf-canada-practice-test/", "امتحان TCF Canada تجريبي مجاني", "قِس مستواك قبل أن تدفع 1800 درهم.")],
    sources=f"مواقع {AFD} (صفحة امتحانات الهجرة إلى كندا، وصفحة حجز TCF Canada، وتقويم الفترة من سبتمبر إلى ديسمبر 2026) و{AFAD} (صفحة TCF، وصفحة حجز TCF Canada، وتقويم امتحانات 2026)، كما اطّلعنا عليها في 8 أكتوبر 2026؛ وصفحتا TEF Canada لدى المركزين في 13 أكتوبر 2026.",
    badges={"abou-dhabi-french-ambassy-institut-francais-antenne-afad": CA,
            "dubai-alliance-francaise-de-dubai-centre-1": CA, "dubai-alliance-francaise-de-dubai-centre-2": CA,
            "al-ain-alliance-francais-d-abu-dhabi-antenne-al-ain": [("part", "لا جلسات TCF في العين")]},
    urls={"abou-dhabi-french-ambassy-institut-francais-antenne-afad": "https://www.afabudhabi.org/tcf/",
          "dubai-alliance-francaise-de-dubai-centre-1": "https://www.afdubai.org/canada-immigration-exams-alliance-francaise-dubai/tcf-canada-exam/",
          "dubai-alliance-francaise-de-dubai-centre-2": "https://www.afdubai.org/canada-immigration-exams-alliance-francaise-dubai/tcf-canada-exam/"},
))

# ===========================================================================
# السعودية — appariée à /en/tcf-canada-saudi-arabia/
# ===========================================================================
PAGES.append(dict(ME,
    lang="ar", variant="ar", og_locale="ar_SA", fr_path=None, pair="/en/tcf-canada-saudi-arabia/", slug="tcf-canada-saudi-arabia",
    country_name="المملكة العربية السعودية", exam="tcf", file="tcf_arabie_saoudite", layout="cities",
    crumb="TCF Canada في السعودية",
    title="اختبار TCF Canada في السعودية: جدة والرياض، 1950 ريالًا",
    desc="اختبار TCF Canada في السعودية: مراكز Alliance française d’Arabie Saoudite في الخبر وجدة والرياض، 1950 ريالًا، الجلسات القادمة وشروط الحجز.",
    h1="اختبار TCF Canada في السعودية: المراكز والرسوم والجلسات القادمة",
    intro=f"""نعم، يمكنك اجتياز TCF Canada في السعودية. ففي 13 أكتوبر 2026، كانت {FEI} تعتمد {{n}} مراكز لامتحان TCF في المملكة،
تديرها جميعها <strong>{AFAS}</strong> (AFAS): في الخبر وجدة والرياض. وكانت منصة الحجز لديها تعرض <strong>امتحان TCF Canada
في جدة يوم الثلاثاء 20 أكتوبر</strong> على الحاسوب، و<strong>امتحان e-TCF Canada في الرياض يوم الخميس 12 نوفمبر</strong>،
وقد اكتملت مقاعده — كلاهما بسعر <strong>1950 ريالًا</strong>؛ وتنص صفحة جلسة جدة على «لا تأجيل، ولا استرداد، ولا تغيير للموعد».""",
    facts=["<strong>{n} مراكز معتمدة</strong> لامتحان TCF (قائمة FEI في 13 أكتوبر 2026)، كلها تابعة لـ Alliance française d’Arabie Saoudite: الخبر وجدة والرياض؛ جلسات على الحاسوب في جدة والرياض.",
           "الرسوم: <strong>1950 ريالًا</strong> لكلٍّ من TCF Canada وe-TCF Canada وTCF tout public وe-TEF Canada.",
           "جدة: TCF Canada يوم <strong>الثلاثاء 20 أكتوبر 2026</strong>، من الساعة 10:00 إلى 15:00، على الحاسوب.",
           "الرياض: e-TCF Canada يوم <strong>الخميس 12 نوفمبر 2026</strong> في موقع الربيع — <strong>مكتمل</strong> في 13 أكتوبر؛ ويُغلق التسجيل قبل الامتحان بسبعة أيام عمل.",
           "جلسة TCF Canada في جدة: «لا تأجيل، ولا استرداد، ولا تغيير للموعد». ولم نجد مدة صدور النتائج على موقع AFAS ولا على منصتها."],
    stats=[("{n}", "مراكز معتمدة لامتحان TCF", "الخبر وجدة والرياض"), ("1950 ريالًا", "TCF Canada", "جدة والرياض"),
           ("20 أكتوبر", "TCF Canada في جدة", "على الحاسوب"), ("12 نوفمبر", "e-TCF Canada في الرياض", "مكتمل في 13 أكتوبر")],
    sections=[
        ("sessions", "الجلسات على منصة AFAS", table(
            f"جلسات امتحانات الفرنسية على منصة الحجز لدى {AFAS} ({ltr('afas.extranet-aec.com')})، كما اطّلعنا عليها في 13 أكتوبر 2026. الرسوم بالريال السعودي.",
            ["التاريخ", "الامتحان", "المكان", "الرسوم", "الحالة"],
            [("<strong>الثلاثاء 20 أكتوبر 2026</strong>، " + ltr("10:00–15:00"), "<strong>TCF Canada</strong>، على الحاسوب", "جدة (حي جميل، المحمدية)", "1950 ريالًا", "معروضة"),
             ("الخميس 22 أكتوبر 2026، " + ltr("10:00–13:00"), "TCF tout public", "جدة", "1950 ريالًا", "معروضة"),
             ("<strong>الخميس 12 نوفمبر 2026</strong>، " + ltr("13:00–17:30"), "<strong>e-TCF Canada</strong>، على الحاسوب", "الرياض (الربيع)", "1950 ريالًا", "<strong>مكتملة</strong>"),
             ("الخميس 19 نوفمبر 2026، " + ltr("12:30–17:30"), "e-TEF Canada", "الرياض (الربيع)", "1950 ريالًا", "<strong>مكتملة</strong>")], wide=False) + """
<p>تسجّل عبر الإنترنت، على منصة AFAS المرتبطة بصفحة الامتحانات في موقع
<a href="https://www.af-ksa.org/en/exams/" rel="noopener">af-ksa.org</a>. اقرأ الشروط قبل الدفع: تنص صفحة جلسة TCF Canada في جدة على «لا تأجيل، ولا
استرداد، ولا تغيير للموعد»، وفي e-TCF Canada يُغلق التسجيل <strong>قبل موعد الامتحان بسبعة أيام عمل</strong> — أو قبل ذلك
إذا امتلأت المقاعد. وتفصيل ينبغي معرفته: موقع الربيع الذي تعقد فيه AFAS جلسات e-TCF وe-TEF Canada في الرياض ليس مدرجًا
في قائمة France Éducation international، التي تذكر عنوان مركز AFAS في الرياض في Al Kindi Plaza (البوابة 14، حي السفارات)؛
اسأل AFAS عند الشك. ولم تكن هناك أي جلسة TCF معروضة في الخبر في 13 أكتوبر.</p>"""),
        ("gulf", "في بقية الخليج والمشرق", """<p>إذا كانت الجلسات في السعودية مكتملة، فأقرب المراكز المعتمدة لامتحان TCF في
قائمة France Éducation international في 13 أكتوبر 2026 توجد في البحرين (Alliance française، المنامة) وقطر (المعهد الفرنسي،
الدوحة) والكويت (المعهد الفرنسي) والأردن (المعهد الفرنسي، عمّان) — مركز واحد في كل بلد؛ ولم نتحقق مما إذا كانت تقدّم TCF
Canada نفسه، فراجع مواقعها. أما عُمان فليس فيها أي مركز TCF في القائمة. وفي <a href="/ar/tcf-canada-uae/">الإمارات</a> أربعة
مراكز، اثنان منها في دبي؛ وانظر أيضًا <a href="/ar/tcf-canada-egypt/">مصر</a> و<a href="/ar/tcf-canada-lebanon/">لبنان</a>.</p>"""),
    ],
    list_title="المراكز المعتمدة لامتحان TCF في السعودية ({n})",
    faq=[("هل يمكنني اجتياز TCF Canada في السعودية؟", "نعم. تنظّمه Alliance française d’Arabie Saoudite: في 13 أكتوبر 2026 كانت منصتها تعرض TCF Canada في جدة يوم الثلاثاء 20 أكتوبر (على الحاسوب)، وe-TCF Canada في الرياض يوم الخميس 12 نوفمبر، وكان مكتملًا."),
         ("كم سعر اختبار TCF Canada في السعودية؟", "1950 ريالًا، كما نُشر على منصة الحجز لدى AFAS في 13 أكتوبر 2026 — وهو السعر نفسه لامتحان TCF tout public وامتحان e-TEF Canada."),
         ("هل يمكنني استرداد الرسوم أو تغيير الموعد؟", "ليس في جلسة TCF Canada بجدة: تنص صفحتها على «لا تأجيل، ولا استرداد، ولا تغيير للموعد». وفي e-TCF Canada يُغلق التسجيل قبل الامتحان بسبعة أيام عمل."),
         ("هل يتوفر TEF Canada في السعودية؟", "عرضت AFAS امتحان e-TEF Canada في الرياض يوم الخميس 19 نوفمبر 2026 بسعر 1950 ريالًا، وكان مكتملًا في 13 أكتوبر."),
         ("هل تقبل IRCC امتحان TCF Canada الذي أجتازه في السعودية؟", "نعم: تصدر شهادة النتائج عن France Éducation international أيًّا كان المركز المعتمد الذي اجتزت فيه الامتحان، وهي صالحة لمدة سنتين.")],
    also=[("/ar/tcf-canada-uae/", "TCF Canada في الإمارات", "دبي وأبوظبي، 1800 درهم."),
          ("/ar/tcf-canada-price/", "سعر امتحان TCF Canada والتسجيل", "الرسوم بلدًا بلدًا وطريقة الحجز."),
          ("/ar/tcf-canada-practice-test/", "امتحان TCF Canada تجريبي مجاني", "قِس مستواك قبل أن تدفع 1950 ريالًا.")],
    sources=f"موقع {AFAS} ({ltr('af-ksa.org')}، صفحة الامتحانات) ومنصة الحجز لديها {ltr('afas.extranet-aec.com')} (جلسات TCF وTCF Canada وe-TCF Canada وe-TEF Canada)، كما اطّلعنا عليهما في 13 أكتوبر 2026.",
    badges={"djeddah-alliance-francaise": CA,
            "riyadh-alliance-francaise-d-arabie-saoudite": [("ok", "e-TCF Canada (الربيع)"), ("part", "جلسة 12 نوفمبر مكتملة")],
            "al-khobar-alliance-francaise-d-arabie-saoudite": [("part", "لا جلسة TCF معروضة")]},
    urls={"djeddah-alliance-francaise": "https://www.af-ksa.org/en/exams/",
          "riyadh-alliance-francaise-d-arabie-saoudite": "https://www.af-ksa.org/en/exams/",
          "al-khobar-alliance-francaise-d-arabie-saoudite": "https://www.af-ksa.org/en/exams/"},
))

# ===========================================================================
# مصر — appariée à /en/tcf-canada-egypt/
# ===========================================================================
PAGES.append(dict(ME,
    lang="ar", variant="ar", og_locale="ar_EG", fr_path=None, pair="/en/tcf-canada-egypt/", slug="tcf-canada-egypt",
    country_name="مصر", exam="tcf", file="tcf_egypte_v2", layout="cities",
    crumb="TCF Canada في مصر",
    title="امتحان TCF Canada في مصر 2026: القاهرة، جلسة ديسمبر",
    desc="امتحان TCF Canada في مصر: مراكز المعهد الفرنسي في القاهرة (المنيرة ومصر الجديدة) والإسكندرية، الجلسة التالية في ديسمبر 2026، التسجيل والنتائج.",
    h1="امتحان TCF Canada في مصر: مراكز المعهد الفرنسي والجلسة التالية",
    intro=f"""في مصر، تعتمد {FEI} {{n}} مراكز لامتحان TCF، كلها تابعة <strong>للمعهد الفرنسي في مصر</strong> ({IFE}): في القاهرة
(المنيرة ومصر الجديدة) وفي الإسكندرية. وفي 13 أكتوبر 2026، كان موقعه يعلن الجلسة التالية لامتحان TCF Canada في <strong>ديسمبر
2026</strong>، مع <strong>إغلاق</strong> التسجيل حاليًا. أما السعر فلا يُنشر إلا في تقويم بصيغة PDF للمواعيد والأسعار على الموقع
نفسه — تحقّق منه هناك قبل التسجيل. وتصدر النتائج بعد نحو أربعة أسابيع.""",
    facts=["<strong>{n} مراكز معتمدة</strong> لامتحان TCF (قائمة FEI في 13 أكتوبر 2026): القاهرة – المنيرة، والقاهرة – مصر الجديدة، والإسكندرية؛ جلسات على الحاسوب في المنيرة والإسكندرية.",
           "TCF Canada: الجلسة التالية في <strong>ديسمبر 2026</strong>؛ «التسجيل مغلق حاليًا» (13 أكتوبر).",
           "الرسوم: في تقويم المعهد بصيغة PDF «Dates et tarifs du TCF» فقط — غير منشورة في صفحة ويب.",
           "التسجيل: نموذج إلكتروني لكل نسخة، ونسخة من جواز السفر، ثم الدفع، ثم إشعار بالبريد الإلكتروني.",
           "النتائج بعد نحو <strong>4 أسابيع</strong>؛ و<strong>30 يومًا</strong> بين محاولتين لامتحان TCF."],
    stats=[("{n}", "مراكز معتمدة لامتحان TCF", "القاهرة والإسكندرية"), ("ديسمبر 2026", "الجلسة التالية لـ TCF Canada", "التسجيل مغلق في 13 أكتوبر"),
           ("نحو 4 أسابيع", "النتائج", "المعهد الفرنسي في مصر"), ("30 يومًا", "بين محاولتين", "TCF")],
    sections=[
        ("sessions", "امتحان TCF Canada في المعهد الفرنسي في مصر", f"""<p>ينشر المعهد الفرنسي في مصر جلساته لكل مراكزه في صفحة
واحدة: في 13 أكتوبر 2026، كان لامتحان TCF Canada قسمه الخاص — إلى جانب TCF tout public وTCF IRN وTCF Québec وe-TEF —
يعلن <strong>الجلسة التالية في ديسمبر 2026</strong> وينص على أن «التسجيل مغلق حاليًا». أما التاريخ الدقيق والسعر ففي تقويم
المعهد بصيغة PDF («Dates et tarifs du TCF»)، الذي يُنزَّل كملف بدل أن يُفتح، فلم نقرأه.</p>

<p>أي مركز يعقده؟ نشر مركز المنيرة في القاهرة نتائج TCF Canada لجلسات سابقة؛ أما قسما نتائج TCF Canada في الإسكندرية ومصر
الجديدة فكانا فارغين في 13 أكتوبر، لذلك لم نتأكد من أنهما يعقدان TCF Canada. تسجّل بنموذج إلكتروني للنسخة التي تريدها،
ثم ترسل نسخة من جواز سفرك وتدفع، ويصلك إشعار الامتحان بالبريد الإلكتروني. وتصدر النتائج «في غضون أربعة أسابيع تقريبًا»
بعد الامتحان، ويجب الانتظار 30 يومًا بين محاولتين لامتحان TCF. كما يقدّم المعهد امتحان TEF Canada (e-TEF)، وكان التسجيل
فيه مغلقًا في 13 أكتوبر.</p>"""),
    ],
    list_title="المراكز المعتمدة لامتحان TCF في مصر ({n})",
    faq=[("أين يمكنني اجتياز TCF Canada في مصر؟", "في المعهد الفرنسي في مصر. تذكر قائمة FEI ثلاثة مراكز معتمدة لامتحان TCF (القاهرة – المنيرة، والقاهرة – مصر الجديدة، والإسكندرية)؛ وقد نشر مركز المنيرة نتائج TCF Canada، بينما كان قسما نتائج TCF Canada في المركزين الآخرين فارغين في 13 أكتوبر 2026."),
         ("متى الجلسة التالية لامتحان TCF Canada في مصر؟", "في ديسمبر 2026، بحسب موقع المعهد الفرنسي في مصر في 13 أكتوبر 2026؛ وكان التسجيل مغلقًا في ذلك اليوم. التاريخ الدقيق في تقويمه بصيغة PDF."),
         ("كم سعر امتحان TCF Canada في مصر؟", "ينشر المعهد الفرنسي في مصر رسوم TCF في تقويم بصيغة PDF («Dates et tarifs du TCF»)، لا في صفحة ويب؛ لم نتمكن من قراءته، فتحقّق منه على موقع ifegypte.com قبل التسجيل."),
         ("كيف أسجّل؟", "بالنموذج الإلكتروني الخاص بامتحان TCF Canada، ونسخة من جواز سفرك، ثم الدفع؛ ويصلك بعدها إشعار الامتحان بالبريد الإلكتروني."),
         ("كم تستغرق النتائج؟", "نحو أربعة أسابيع بعد الامتحان، بحسب الأسئلة الشائعة لدى المعهد. وشهادة النتائج صالحة لمدة سنتين لدى IRCC.")],
    also=[("/ar/tcf-canada-lebanon/", "TCF Canada في لبنان", "ستة مراكز للمعهد الفرنسي."),
          ("/ar/tcf-canada-saudi-arabia/", "TCF Canada في السعودية", "جدة والرياض، 1950 ريالًا."),
          ("/ar/tcf-canada-practice-test/", "امتحان TCF Canada تجريبي مجاني", "تحقّق من مستواك قبل جلسة ديسمبر.")],
    sources=f"موقع {IFE} ({ltr('ifegypte.com')}: الجلسات القادمة، ونتائج الامتحانات حسب المركز، والأسئلة الشائعة)، كما اطّلعنا عليه في 13 أكتوبر 2026.",
    badges={"le-caire-institut-francais-d-egypte": CA,
            "le-caire-heliopolis-institut-francais": [("part", "TCF Canada غير مؤكد")],
            "alexandrie-institut-francais-d-egypte-a-alexandrie": [("part", "TCF Canada غير مؤكد")]},
    urls={k: "https://www.ifegypte.com/prochaines-sessions/" for k in
          ("le-caire-institut-francais-d-egypte", "le-caire-heliopolis-institut-francais", "alexandrie-institut-francais-d-egypte-a-alexandrie")},
))

# ===========================================================================
# لبنان — appariée à /en/tcf-canada-lebanon/
# ===========================================================================
PAGES.append(dict(ME,
    lang="ar", variant="ar", og_locale="ar_LB", fr_path=None, pair="/en/tcf-canada-lebanon/", slug="tcf-canada-lebanon",
    country_name="لبنان", exam="tcf", file="tcf_liban_v2", layout="cities",
    crumb="TCF Canada في لبنان",
    title="امتحان TCF Canada في لبنان: ستة مراكز للمعهد الفرنسي",
    desc="امتحان TCF Canada في لبنان: مراكز المعهد الفرنسي الستة (بيروت، دير القمر، جونية، صيدا، طرابلس، زحلة)، مدة النتائج وبيانات الاتصال.",
    h1="امتحان TCF Canada في لبنان: مراكز المعهد الفرنسي الستة",
    intro=f"""في لبنان، يدير امتحان TCF <strong>المعهد الفرنسي في لبنان</strong> ({IFL})، وتعتمد {FEI} {{n}} مراكز: بيروت ودير
القمر وجونية وصيدا وطرابلس وزحلة. وفي 13 أكتوبر 2026، كانت صفحة الامتحانات في كل منها تذكر <strong>TCF Canada</strong> بين
النسخ المقدّمة، «في إطار إجراءات الهجرة إلى كندا». أما مواعيد الجلسات فلا تُنشر إلا في تقويمات بصيغة PDF، ولا يُنشر أي سعر نصًّا؛ وتصل
النتائج بعد نحو ستة أسابيع من الامتحان.""",
    facts=["<strong>{n} مراكز معتمدة</strong> (قائمة FEI في 13 أكتوبر 2026)، كلها تابعة للمعهد الفرنسي في لبنان؛ جلسات على الحاسوب في بيروت ودير القمر وطرابلس.",
           "يُذكر <strong>TCF Canada</strong> في صفحات الامتحانات الست كلها، مع TCF tout public وTCF Québec وTCF IRN.",
           "النتائج بعد نحو <strong>6 أسابيع</strong>؛ وتُستلم الشهادة شخصيًا من المعهد.",
           "المواعيد: في تقويمات PDF فقط (بيروت وجونية وصيدا لعام 2026؛ وتقويم زحلة هو تقويم 2024؛ ولا تقويم لدير القمر وطرابلس)؛ ولا سعر منشورًا نصًّا.",
           "شهادة النتائج صالحة لمدة سنتين لدى IRCC."],
    stats=[("{n}", "مراكز", "TCF Canada مذكور في كلٍّ منها"), ("3", "مراكز بجلسات على الحاسوب", "بيروت ودير القمر وطرابلس"),
           ("نحو 6 أسابيع", "النتائج", "تُستلم شخصيًا"), ("سنتان", "مدة الصلاحية", "لدى IRCC")],
    sections=[
        ("centres", "ما ينشره المعهد الفرنسي في لبنان", f"""<p>لكل مركز من المراكز الستة صفحة امتحانات خاصة به على موقع
{ltr('institutfrancais-liban.com')}، بالنص نفسه عن TCF: TCF tout public وTCF Québec و<strong>TCF Canada</strong> — «في إطار
إجراءات الهجرة إلى كندا» — وTCF IRN. وتُرسَل النتائج «بعد نحو 6 أسابيع من الامتحانات»، وتُستلم الشهادة شخصيًا من المعهد.</p>

<p>غير أن التقويمات بصيغة PDF: تحيل صفحات بيروت وجونية والجنوب (صيدا) إلى تقويم TCF لعام 2026، وما زالت صفحة زحلة
تحيل إلى تقويم 2024، ولا تحيل صفحتا دير القمر وطرابلس إلى أي تقويم. ولا تذكر الصفحات طريقة التسجيل ولا موعده الأخير، ولا تنشر أي سعر نصًّا — لذلك تواصل مع
مركزك (تذكر صفحة بيروت الرقم {ltr('01 420 272/3')}) قبل التخطيط لطلبك. وإن كنت تفضّل الاختبار الآخر الذي تقبله IRCC، فانظر
صفحة <a href="/ar/tcf-or-tef-canada/">TCF أم TEF Canada</a>.</p>"""),
    ],
    list_title="المراكز المعتمدة لامتحان TCF في لبنان ({n})",
    faq=[("أين يمكنني اجتياز TCF Canada في لبنان؟", "في المعهد الفرنسي في لبنان، في أيٍّ من مراكزه الستة المعتمدة: بيروت ودير القمر وجونية وصيدا وطرابلس وزحلة. وكانت صفحات الامتحانات الست كلها تذكر TCF Canada في 13 أكتوبر 2026."),
         ("كم سعر امتحان TCF Canada في لبنان؟", "لا ينشر المعهد الفرنسي في لبنان رسوم TCF نصًّا في صفحات الامتحانات؛ اسأل مركزك (بيروت: <bdi dir='ltr'>01 420 272/3</bdi>)."),
         ("هل يُجرى TCF Canada على الحاسوب في لبنان؟", "تُظهر قائمة FEI جلسات على الحاسوب في بيروت ودير القمر وطرابلس؛ أما المراكز الثلاثة الأخرى فلا تذكر هذا الخيار."),
         ("كم تستغرق النتائج؟", "نحو ستة أسابيع بعد الامتحان؛ وتُستلم الشهادة شخصيًا من المعهد الفرنسي في لبنان.")],
    also=[("/ar/tcf-canada-egypt/", "TCF Canada في مصر", "المعهد الفرنسي في مصر، الجلسة التالية في ديسمبر 2026."),
          ("/ar/tcf-canada-uae/", "TCF Canada في الإمارات", "دبي وأبوظبي، 1800 درهم."),
          ("/ar/tcf-canada-nclc/", "درجات TCF Canada وحاسبة NCLC", "الحاسبة وجدول IRCC.")],
    sources=f"صفحات الامتحانات في مراكز {IFL} الستة ({ltr('institutfrancais-liban.com/examens/…')})، كما اطّلعنا عليها في 13 أكتوبر 2026.",
    badges={k: CA for k in ("beyrouth-institut-francais-du-liban", "deir-el-kamar-institut-francais", "jounieh-institut-francais",
                             "saida-institut-francais", "tripoli-institut-francais", "zahle-institut-francais")},
    urls={"beyrouth-institut-francais-du-liban": "https://institutfrancais-liban.com/examens/beyrouth/",
          "deir-el-kamar-institut-francais": "https://institutfrancais-liban.com/examens/deir-el-qamar/",
          "jounieh-institut-francais": "https://institutfrancais-liban.com/examens/jounieh/",
          "saida-institut-francais": "https://institutfrancais-liban.com/examens/sud/",
          "tripoli-institut-francais": "https://institutfrancais-liban.com/examens/tripoli/",
          "zahle-institut-francais": "https://institutfrancais-liban.com/examens/baalbeck-zahle/"},
))


# ===========================================================================
# /ar/ — accueil (make_pays.hub("ar")). Chiffres repris des pages pays et des guides.
# ===========================================================================
def _hub_table():
    rows = [("الإمارات", '<a href="/ar/tcf-canada-uae/">دبي وأبوظبي، 1800 درهم</a>', "8 أكتوبر 2026"),
            ("السعودية", '<a href="/ar/tcf-canada-saudi-arabia/">جدة والرياض، 1950 ريالًا</a>', "13 أكتوبر 2026"),
            ("مصر", '<a href="/ar/tcf-canada-egypt/">القاهرة (المنيرة)، الجلسة التالية في ديسمبر 2026</a>', "13 أكتوبر 2026"),
            ("لبنان", '<a href="/ar/tcf-canada-lebanon/">ستة مراكز للمعهد الفرنسي</a>', "13 أكتوبر 2026")]
    return table("TCF Canada في الخليج والمشرق، بحسب مواقع المراكز في تاريخ مراجعتنا. الرسوم بالعملة المحلية.",
                 ["البلد", "TCF Canada", "تاريخ المراجعة"], [(f"<strong>{p}</strong>", a, d) for p, a, d in rows], wide=False)


HUB = dict(
    variant="ar", accent="accent-tcf", crumb="العربية", read=3, published="2026-10-13", date_label="13 أكتوبر 2026",
    title="دليل امتحان TCF Canada بالعربية: المراكز والأسعار",
    desc="دليل امتحان TCF Canada بالعربية: الأقسام والدرجات وNCLC وامتحان تجريبي، ومراكز الامتحان في الإمارات ومصر ولبنان والسعودية بالأسعار والمواعيد.",
    h1="دليل امتحان TCF Canada بالعربية: ما تحتاجه للهجرة إلى كندا",
    lang_links='<p class="langs"><a href="/en/" hreflang="en" lang="en">Read in English</a> · <a href="/" hreflang="fr" lang="fr">Lire en français</a></p>',
    intro="""TCF Canada أحد اختبارَي اللغة الفرنسية اللذين تقبلهما دائرة الهجرة واللاجئين والمواطنة الكندية (IRCC) للهجرة
الاقتصادية، والآخر هو TEF Canada. تجد في هذه الصفحات بالعربية: صيغة الامتحان، وتحويل الدرجات إلى مستويات NCLC، وامتحانًا
تجريبيًا، ومواضيع التعبير الكتابي والشفهي، ثم مراكز الامتحان في الإمارات ومصر ولبنان والسعودية، بما نشرته مواقعها من
أسعار ومواعيد عند مراجعتنا.""",
    facts=["اختباران فقط تقبلهما IRCC لنظام الدخول السريع: <strong>TCF Canada</strong> و<strong>TEF Canada</strong>.",
           "<strong>NCLC 7</strong> = 458 في فهم المسموع، و453 في فهم المقروء، و10/20 في التعبير الشفهي والكتابي.",
           "الإمارات: 4 مراكز، وTCF Canada بسعر <strong>1800 درهم</strong> في دبي وأبوظبي (8 أكتوبر 2026).",
           "السعودية: 3 مراكز لـ Alliance française d’Arabie Saoudite، و<strong>1950 ريالًا</strong> (13 أكتوبر 2026).",
           "مصر: 3 مراكز للمعهد الفرنسي، والجلسة التالية في <strong>ديسمبر 2026</strong>؛ لبنان: 6 مراكز للمعهد الفرنسي.",
           "شهادة نتائج TCF Canada صالحة لمدة سنتين."],
    toc=[("prepare", "التحضير لامتحان TCF Canada"), ("centres", "مراكز الامتحان"), ("tcf-or-tef", "TCF أم TEF؟")],
    body="""
<div class="stats">
<div class="stat"><b>458</b><span>في فهم المسموع</span><em>لبلوغ NCLC 7</em></div>
<div class="stat"><b>4</b><span>دول في الخليج والمشرق</span><em>الإمارات والسعودية ومصر ولبنان</em></div>
<div class="stat"><b>سنتان</b><span>صلاحية النتائج</span><em>لدى IRCC</em></div>
</div>

<h2 id="prepare">التحضير لامتحان TCF Canada</h2>
<p>الأدلة التي تقف وراء الدرجات: شكل كل اختبار من الاختبارات الأربعة، وتحويل الدرجات إلى مستويات NCLC، وتمارين بالصيغة
الرسمية.</p>
<ul class="posts">
<li><a href="/ar/tcf-canada/">امتحان TCF كندا</a><p>ما هو، ولمن، والاختبارات الأربعة ومستويات NCLC التي تعتمدها IRCC.</p></li>
<li><a href="/ar/tcf-canada-nclc/">الدرجات وحاسبة NCLC</a><p>يتطلب NCLC 7 درجة 458 في فهم المسموع و453 في فهم المقروء و10/20 في التعبير.</p></li>
<li><a href="/ar/tcf-canada-practice-test/">امتحان TCF Canada تجريبي مجاني</a><p>قِس مستواك بالصيغة الحقيقية قبل الحجز.</p></li>
<li><a href="/ar/tcf-canada-preparation/">التحضير لاختبار TCF Canada</a><p>كم من الوقت تحتاج، ومن أين تبدأ.</p></li>
<li><a href="/ar/tcf-canada-writing/">التعبير الكتابي</a><p>المهام الثلاث، وعدد الكلمات، ومواضيع نموذجية.</p></li>
<li><a href="/ar/tcf-canada-speaking/">التعبير الشفهي</a><p>المهام الثلاث في 12 دقيقة.</p></li>
<li><a href="/ar/tcf-or-tef-canada/">TCF أم TEF Canada؟</a><p>اختبارا الفرنسية اللذان تقبلهما IRCC، جنبًا إلى جنب.</p></li>
<li><a href="/ar/tcf-canada-price/">السعر والتسجيل</a><p>الرسوم بلدًا بلدًا، وطريقة الحجز.</p></li>
</ul>

<h2 id="centres">مراكز الامتحان في الخليج والمشرق</h2>
""" + _hub_table() + """
<p>المراكز في بلدان أخرى بالإنجليزية أو بالفرنسية: <a href="/en/" lang="en">Canada, USA, UK, India</a> ·
<a href="/blog/tcf-canada-algerie/" lang="fr">Algérie</a> · <a href="/blog/tcf-canada-maroc/" lang="fr">Maroc</a> ·
<a href="/blog/tcf-canada-tunisie/" lang="fr">Tunisie</a>.</p>

<h2 id="tcf-or-tef">TCF أم TEF؟</h2>
<p>TCF Canada <strong>اختبار</strong> لا شهادة: لا نجاح فيه ولا رسوب — بل يحدد مستواك في كل قسم، ثم تحوّل IRCC النتيجة إلى
مستويات NCLC. تصدر شهادة النتائج عن <bdi>France Éducation international</bdi> أيًّا كان المركز الذي تجتاز فيه الامتحان، وهي
صالحة لمدة سنتين. وأمران ينبغي معرفتهما قبل الدفع: <strong>المركز المعتمد لامتحان TCF لا يقدّم بالضرورة نسخة Canada</strong>
— تبيّن كل صفحة المراكز التي كانت تعلن عنها — والمقاعد قليلة في المدن الكبرى. وتقبل IRCC أيضًا TEF Canada:
<a href="/ar/tcf-or-tef-canada/">قارن بين الاختبارين</a>.</p>
""",
    cta_h2="تدرّب على الصيغة الحقيقية للامتحان",
    cta_p="""تدفع رسوم كل جلسة كاملةً، ولا يمكنك إعادة الامتحان فورًا. الامتحانات التجريبية في تطبيق
«<bdi>TCF DELF TEF: Tests 2026</bdi>» تتبع الصيغة الرسمية لكل امتحان — TCF كندا وTEF كندا وDELF وDALF — وتُصحَّح كالامتحان
الحقيقي، مع ملاحظات بالذكاء الاصطناعي على التعبير الكتابي والشفهي. واجهة التطبيق على iPhone متاحة بالعربية، أما مواد
الامتحان فبالفرنسية كما في يوم الامتحان.""",
    faq=[("ما هو امتحان TCF Canada؟", "اختبار لتحديد مستوى اللغة الفرنسية تصدره France Éducation international، وهو أحد الاختبارين اللذين تقبلهما IRCC للهجرة الاقتصادية إلى كندا (والآخر TEF Canada). يتكون من أربعة اختبارات: فهم المسموع، وفهم المقروء، والتعبير الكتابي، والتعبير الشفهي."),
         ("أين يمكنني اجتياز TCF Canada في الخليج؟", "في الإمارات لدى Alliance Française في دبي وأبوظبي (1800 درهم، 8 أكتوبر 2026)، وفي السعودية لدى Alliance française d’Arabie Saoudite في جدة والرياض (1950 ريالًا، 13 أكتوبر 2026). وتوجد مراكز TCF معتمدة أيضًا في البحرين وقطر والكويت."),
         ("هل التطبيق متاح بالعربية؟", "واجهة التطبيق على iPhone متاحة بالعربية، أما مواد الامتحان فبالفرنسية، كما في يوم الامتحان.")],
    also=[("/ar/tcf-canada/", "امتحان TCF كندا", "الاختبارات الأربعة ومدتها والدرجات المطلوبة."),
          ("/ar/tcf-canada-nclc/", "الدرجات وحاسبة NCLC", "الحاسبة وجدول IRCC."),
          ("/ar/tcf-canada-uae/", "TCF Canada في الإمارات", "دبي وأبوظبي، 1800 درهم.")],
    sources="صفحات هذا الموقع بالفرنسية والإنجليزية، ومواقع مراكز الامتحان المذكورة في كل صفحة، كما اطّلعنا عليها بين 8 و13 أكتوبر 2026. القواعد والأسعار تتغيّر: تحقّق دائمًا من موقع المركز ومن canada.ca قبل الدفع أو تقديم الطلب.",
)
