#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pages « À propos » en anglais, espagnol et arabe (29/10/2026) : /en/about/, /es/acerca-de/, /ar/about/.

Traductions de /a-propos/ (méthode éditoriale, sources, ce qui n'est pas publié, limites, mentions légales), avec
l'en-tête et le pied de page de la langue (copiés depuis /en/, /es/, /ar/) et les hreflang entre les quatre pages ;
pose aussi les hreflang et la ligne de langues sur /a-propos/. Idempotent. Usage : python3 _build/make_about_i18n.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
BASE = "https://delf-tcf-tef.fr"
PATHS = {"fr": "/a-propos/", "en": "/en/about/", "es": "/es/acerca-de/", "ar": "/ar/about/"}
LABEL = {"fr": "Lire en français", "es": "Leer en español", "en": "Read in English", "ar": "اقرأ بالعربية"}
TITLE = {
    "en": "About this site and its editorial method — delf-tcf-tef.fr",
    "es": "Acerca de este sitio y su método editorial — delf-tcf-tef.fr",
    "ar": "عن هذا الموقع ومنهجه التحريري — delf-tcf-tef.fr",
}
DESC = {
    "en": "Who publishes this site, how the information is verified, which sources are used and what we do not publish. Legal notice included.",
    "es": "Quién edita este sitio, cómo se verifica la información, qué fuentes se usan y qué no publicamos. Aviso legal incluido.",
    "ar": "من ينشر هذا الموقع، وكيف نتحقق من المعلومات، وما المصادر التي نعتمدها، وما الذي لا ننشره. مع البيانات القانونية.",
}
HOME = {"en": ("/en/", "Home"), "es": ("/es/", "Inicio"), "ar": ("/ar/", "الرئيسية")}
CRUMB = {"en": "About", "es": "Acerca de", "ar": "عن الموقع"}
LOCALE = {"en": "en_US", "es": "es_ES", "ar": "ar_AR"}

BODY = {}
BODY["en"] = """<h1>About this site and its editorial method</h1>
<p class="meta">Updated 29 October 2026 · translated from the French page of 27 July 2026</p>
{langs}
<p class="intro">This site is published by <strong>Augusto Grone</strong>. It publishes guides on the French
exams — DELF, DALF, TCF, TEF — and on the language levels required for immigration and citizenship procedures.
This page explains how that information is established, checked and corrected.</p>

<details class="toc"><summary>Contents</summary><ol>
<li><a href="#why">Why this site exists</a></li>
<li><a href="#method">How we verify</a></li>
<li><a href="#sources">The sources we use</a></li>
<li><a href="#not">What we do not publish</a></li>
<li><a href="#limits">Our limits, stated plainly</a></li>
<li><a href="#error">Report an error</a></li>
<li><a href="#legal">Legal notice</a></li>
</ol></details>

<h2 id="why">Why this site exists</h2>
<p>Searching for “what TCF score for NCLC 7” or “what level for French citizenship” returns a mix of consultants'
blogs, dated forum threads and automatic summaries that are sometimes wrong. In July 2026 we saw results displayed at
the top of search engines giving <strong>incorrect</strong> NCLC conversion ranges.</p>
<p>For a reader preparing an immigration or citizenship file, wrong information does not only cost time: it costs exam
fees, months of delay, and sometimes a refusal. This site starts from there.</p>

<h2 id="method">How we verify</h2>
<p>Every article follows the same chain, and we keep to it even when it is slower.</p>
<ol>
<li><strong>Primary-source collection.</strong> Official pages are opened and read, never summarised from a search-result snippet.</li>
<li><strong>Cross-checking.</strong> Every binding figure — threshold, marking scale, duration, score range — is confirmed on at least two official pages.</li>
<li><strong>Adversarial re-reading.</strong> The collected facts are then re-examined from three angles: conformity with the reference text, currency of the data (a repealed rule stays online for years), and the arithmetic consistency of tables — overlapping ranges or gaps signal a copying error.</li>
<li><strong>Rejection.</strong> A fact we cannot reopen at its source is not published “subject to confirmation”: it is dropped, and the article sends the reader explicitly to the official source.</li>
</ol>
<p>This method has a visible effect: our articles contain sentences such as “we could not verify this point, confirm
it on service-public.fr”. That is deliberate. An article that claims to know everything about immigration law is lying.</p>

<h2 id="sources">The sources we use</h2>
<div class="tablewrap">
<table>
<caption>Primary reference sources, by domain.</caption>
<thead><tr><th>Domain</th><th>Sources used</th></tr></thead>
<tbody>
<tr><td>French immigration law</td><td>Légifrance, service-public.fr, Ministry of the Interior (DGEF)</td></tr>
<tr><td>DELF, DALF and TCF exams</td><td>France Éducation international</td></tr>
<tr><td>TEF and TEFAQ exams</td><td>Le français des affaires — CCI Paris Île-de-France</td></tr>
<tr><td>Canadian federal immigration</td><td>IRCC / canada.ca</td></tr>
<tr><td>Quebec immigration</td><td>MIFI / quebec.ca</td></tr>
<tr><td>Exam centres, dates and fees</td><td>France Éducation international's list of approved centres, then each centre's own website, on the date given at the foot of the page</td></tr>
</tbody>
</table>
</div>
<p>Lawyers' blogs, consultants' sites and aggregators can give us a <em>lead</em> on a topic. They are never the final
source for a figure.</p>

<h2 id="not">What we do not publish</h2>
<ul>
<li><strong>No “leaked” exam papers.</strong> TCF papers are strictly confidential. Sites selling “this month's predictions” distribute forgeries or documents obtained illegally — a needless risk for your file.</li>
<li><strong>No individual legal advice.</strong> We explain general rules. We do not take a position on your personal situation: that is for a lawyer or the competent administration.</li>
<li><strong>No promise of results.</strong> No method guarantees a score.</li>
<li><strong>No unsourced figure.</strong> If we cannot tie it to a dated official source, it is not in the article.</li>
</ul>

<h2 id="limits">Our limits, stated plainly</h2>
<p>This site is published independently. It is <strong>neither official nor affiliated</strong> with France Éducation
international (DELF, DALF, TCF) or with Le français des affaires — CCI Paris Île-de-France (TEF). Exam names are cited
only to describe the content covered.</p>
<p>The site is backed by a mobile exam-preparation app, which is its business model: some articles link to it. That
changes nothing in the rule above — we explicitly recommend the free official resources when they meet the need, and we
describe their limits without playing them down.</p>
<p>Finally, <strong>regulations change</strong>. An article that was accurate in July 2026 can stop being so. Every page
carries its update date and points to the official source to consult before any binding step.</p>

<h2 id="error">Report an error</h2>
<p>If you find an inaccuracy, write to us: <strong>gockaman@gmail.com</strong>. If possible, name the page concerned and
the official source that makes you think we are wrong. Substantive corrections are applied and the article's update
date is changed accordingly.</p>
<p>It is the best service you can do us — and every reader after you.</p>

<h2 id="legal">Legal notice</h2>
<div class="tablewrap">
<table>
<caption>Publisher's legal information.</caption>
<thead><tr><th>Item</th><th>Detail</th></tr></thead>
<tbody>
<tr><td>Publisher and publication director</td><td><strong>Augusto Grone</strong></td></tr>
<tr><td>Contact</td><td>gockaman@gmail.com</td></tr>
<tr><td>Hosting</td><td>GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, United States</td></tr>
<tr><td>Intellectual property</td><td>Original content © 2026 delf-tcf-tef.fr</td></tr>
<tr><td>Personal data</td><td>See the <a href="/confidentialite/" hreflang="fr">privacy policy</a> (in French)</td></tr>
</tbody>
</table>
</div>
<div class="note">
<p><strong>Marks cited.</strong> DELF, DALF and TCF are marks of France Éducation international. TEF, TEFAQ and TEF Canada
are marks of Le français des affaires — CCI Paris Île-de-France. NCLC and CLB are frameworks of the Government of
Canada. These names are used purely descriptively, to name the exams this site covers.</p>
</div>

<h2>Our guides</h2>
<ul class="posts">
<li><a href="/en/">All English pages</a>
<p>Sourced guides on the TCF Canada and its CLB scores, the DELF and DALF, exam dates and centres by country.</p></li>
</ul>
"""

BODY["es"] = """<h1>Acerca de este sitio y su método editorial</h1>
<p class="meta">Actualizado el 29 de octubre de 2026 · traducción de la página francesa del 27 de julio de 2026</p>
{langs}
<p class="intro">Este sitio lo edita <strong>Augusto Grone</strong>. Publica guías sobre los exámenes de francés
— DELF, DALF, TCF, TEF — y sobre los niveles de idioma exigidos en los trámites de inmigración y nacionalidad. Aquí
se explica cómo se establece, se verifica y se corrige esa información.</p>

<details class="toc"><summary>Contenido</summary><ol>
<li><a href="#por-que">Por qué existe este sitio</a></li>
<li><a href="#metodo">Nuestro método de verificación</a></li>
<li><a href="#fuentes">Las fuentes que usamos</a></li>
<li><a href="#no">Lo que no publicamos</a></li>
<li><a href="#limites">Nuestros límites, dichos con claridad</a></li>
<li><a href="#error">Avisar de un error</a></li>
<li><a href="#legal">Aviso legal</a></li>
</ol></details>

<h2 id="por-que">Por qué existe este sitio</h2>
<p>Buscar «qué puntuación del TCF para NCLC 7» o «qué nivel para la nacionalidad francesa» devuelve hoy una mezcla de
blogs de consultores, foros antiguos y resúmenes automáticos a veces falsos. En julio de 2026 comprobamos que resultados
mostrados en lo alto de los buscadores daban rangos de conversión NCLC <strong>erróneos</strong>.</p>
<p>Para quien prepara un expediente de inmigración o de nacionalidad, una información falsa no cuesta solo tiempo:
cuesta tasas de examen, meses de retraso y, a veces, una denegación. Este sitio parte de ahí.</p>

<h2 id="metodo">Nuestro método de verificación</h2>
<p>Cada artículo sigue la misma cadena, y la respetamos incluso cuando es más lenta.</p>
<ol>
<li><strong>Recogida en fuente primaria.</strong> Las páginas oficiales se abren y se leen; nunca se resumen a partir de un fragmento de resultado de búsqueda.</li>
<li><strong>Contraste.</strong> Toda cifra vinculante — umbral, baremo, duración, rango de puntuación — se confirma en al menos dos páginas oficiales.</li>
<li><strong>Relectura contradictoria.</strong> Los datos recogidos se reexaminan desde tres ángulos: la conformidad con el texto de referencia, la vigencia del dato (una norma derogada sigue en línea durante años) y la coherencia aritmética de las tablas — rangos que se solapan o dejan huecos señalan un error de copia.</li>
<li><strong>Rechazo.</strong> Un dato que no logramos reabrir en su fuente no se publica «con reservas»: se descarta, y el artículo remite explícitamente al lector a la fuente oficial.</li>
</ol>
<p>Este método tiene un efecto visible: nuestros artículos contienen frases como «no hemos podido verificar este punto,
confírmalo en service-public.fr». Es deliberado. Un artículo que pretende saberlo todo sobre el derecho de extranjería
miente.</p>

<h2 id="fuentes">Las fuentes que usamos</h2>
<div class="tablewrap">
<table>
<caption>Fuentes primarias de referencia, por ámbito.</caption>
<thead><tr><th>Ámbito</th><th>Fuentes utilizadas</th></tr></thead>
<tbody>
<tr><td>Derecho francés de extranjería</td><td>Légifrance, service-public.fr, Ministerio del Interior (DGEF)</td></tr>
<tr><td>Exámenes DELF, DALF y TCF</td><td>France Éducation international</td></tr>
<tr><td>Exámenes TEF y TEFAQ</td><td>Le français des affaires — CCI Paris Île-de-France</td></tr>
<tr><td>Inmigración federal canadiense</td><td>IRCC / canada.ca</td></tr>
<tr><td>Inmigración de Quebec</td><td>MIFI / quebec.ca</td></tr>
<tr><td>Centros, fechas y tarifas</td><td>Lista de centros autorizados de France Éducation international y, después, la web de cada centro, en la fecha indicada al pie de cada página</td></tr>
</tbody>
</table>
</div>
<p>Los blogs de abogados, las webs de consultores y los agregadores pueden servirnos de <em>pista</em> para detectar un
tema. Nunca son la fuente final de una cifra.</p>

<h2 id="no">Lo que no publicamos</h2>
<ul>
<li><strong>Ningún examen «filtrado».</strong> Las pruebas del TCF son estrictamente confidenciales. Las webs que venden «las predicciones del mes» difunden falsificaciones o documentos obtenidos ilegalmente — un riesgo inútil para tu expediente.</li>
<li><strong>Ningún consejo jurídico individual.</strong> Explicamos reglas generales. No nos pronunciamos sobre tu situación personal: eso corresponde a un abogado o a la administración competente.</li>
<li><strong>Ninguna promesa de resultado.</strong> Ningún método garantiza una puntuación.</li>
<li><strong>Ninguna cifra sin fuente.</strong> Si no podemos vincularla a una fuente oficial fechada, no aparece en el artículo.</li>
</ul>

<h2 id="limites">Nuestros límites, dichos con claridad</h2>
<p>Este sitio se edita de forma independiente. <strong>No es oficial ni está afiliado</strong> a France Éducation
international (DELF, DALF, TCF) ni a Le français des affaires — CCI Paris Île-de-France (TEF). Los nombres de los
exámenes se citan únicamente para describir el contenido tratado.</p>
<p>El sitio se apoya en una aplicación móvil de preparación de exámenes, que es su modelo económico: algunos artículos
remiten a ella. Eso no cambia la regla anterior — recomendamos explícitamente los recursos oficiales gratuitos cuando
responden a la necesidad, y describimos sus límites sin minimizarlos.</p>
<p>Por último, <strong>la normativa cambia</strong>. Un artículo exacto en julio de 2026 puede dejar de serlo. Cada
página lleva su fecha de actualización y remite a la fuente oficial que conviene consultar antes de cualquier trámite
vinculante.</p>

<h2 id="error">Avisar de un error</h2>
<p>Si detectas una inexactitud, escríbenos: <strong>gockaman@gmail.com</strong>. Indica, si es posible, la página
afectada y la fuente oficial que te hace pensar que nos equivocamos. Las correcciones de fondo se aplican y la fecha de
actualización del artículo se modifica en consecuencia.</p>
<p>Es el mejor servicio que puedes hacernos — y a todos los lectores que vengan después.</p>

<h2 id="legal">Aviso legal</h2>
<div class="tablewrap">
<table>
<caption>Información legal del editor.</caption>
<thead><tr><th>Elemento</th><th>Detalle</th></tr></thead>
<tbody>
<tr><td>Editor y director de la publicación</td><td><strong>Augusto Grone</strong></td></tr>
<tr><td>Contacto</td><td>gockaman@gmail.com</td></tr>
<tr><td>Alojamiento</td><td>GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, Estados Unidos</td></tr>
<tr><td>Propiedad intelectual</td><td>Contenidos originales © 2026 delf-tcf-tef.fr</td></tr>
<tr><td>Datos personales</td><td>Ver la <a href="/confidentialite/" hreflang="fr">política de privacidad</a> (en francés)</td></tr>
</tbody>
</table>
</div>
<div class="note">
<p><strong>Marcas citadas.</strong> DELF, DALF y TCF son marcas de France Éducation international. TEF, TEFAQ y TEF Canada
son marcas de Le français des affaires — CCI Paris Île-de-France. NCLC y CLB son marcos de referencia del Gobierno de
Canadá. Estos nombres se emplean de forma puramente descriptiva, para designar los exámenes que trata este sitio.</p>
</div>

<h2>Nuestras guías</h2>
<ul class="posts">
<li><a href="/es/">Todas las páginas en español</a>
<p>Guías con fuentes sobre el TCF Canada, el DELF B2 y el DELF B1, las fechas de examen y los centros por país.</p></li>
</ul>
"""

BODY["ar"] = """<h1>عن هذا الموقع ومنهجه التحريري</h1>
<p class="meta">آخر تحديث 29 أكتوبر 2026 · ترجمة للصفحة الفرنسية الصادرة في 27 يوليو 2026</p>
{langs}
<p class="intro">يصدر هذا الموقع عن <strong><bdi>Augusto Grone</bdi></strong>. ينشر أدلة عن امتحانات اللغة الفرنسية
— <bdi>DELF</bdi> و<bdi>DALF</bdi> و<bdi>TCF</bdi> و<bdi>TEF</bdi> — وعن مستويات اللغة المطلوبة في إجراءات الهجرة
والتجنّس. تشرح هذه الصفحة كيف تُجمع هذه المعلومات وتُراجع وتُصحَّح.</p>

<details class="toc"><summary>المحتويات</summary><ol>
<li><a href="#why">لماذا وُجد هذا الموقع</a></li>
<li><a href="#method">منهجنا في التحقق</a></li>
<li><a href="#sources">المصادر التي نعتمدها</a></li>
<li><a href="#not">ما لا ننشره</a></li>
<li><a href="#limits">حدودنا، بوضوح</a></li>
<li><a href="#error">الإبلاغ عن خطأ</a></li>
<li><a href="#legal">البيانات القانونية</a></li>
</ol></details>

<h2 id="why">لماذا وُجد هذا الموقع</h2>
<p>البحث عن «ما درجة <bdi>TCF</bdi> المطلوبة لـ<bdi>NCLC 7</bdi>» أو «ما المستوى المطلوب للتجنّس» يعيد اليوم خليطًا من
مدوّنات المستشارين ومنتديات قديمة وملخّصات آلية خاطئة أحيانًا. في يوليو 2026 لاحظنا بأنفسنا أن نتائج معروضة في صدارة
محركات البحث تعطي نطاقات تحويل <bdi>NCLC</bdi> <strong>خاطئة</strong>.</p>
<p>بالنسبة لقارئ يُعدّ ملف هجرة أو جنسية، لا تكلّف المعلومة الخاطئة الوقت فقط: بل تكلّف رسوم امتحان، وأشهرًا من التأخير،
وأحيانًا رفضًا. من هنا ينطلق هذا الموقع.</p>

<h2 id="method">منهجنا في التحقق</h2>
<p>يتبع كل مقال السلسلة نفسها، ونلتزم بها حتى حين تكون أبطأ.</p>
<ol>
<li><strong>الجمع من المصدر الأول.</strong> تُفتح الصفحات الرسمية وتُقرأ، ولا تُلخَّص أبدًا من مقتطف في نتائج البحث.</li>
<li><strong>المقاطعة.</strong> كل رقم ملزم — عتبة، سلّم تنقيط، مدة، نطاق درجات — يُؤكَّد في صفحتين رسميتين على الأقل.</li>
<li><strong>مراجعة نقدية.</strong> تُعاد دراسة الوقائع المجموعة من ثلاث زوايا: مطابقتها للنص المرجعي، وحداثة المعطى (قاعدة ملغاة تبقى منشورة سنوات)، والاتساق الحسابي للجداول — فالنطاقات المتداخلة أو الفجوات تدل على خطأ في النقل.</li>
<li><strong>الاستبعاد.</strong> الواقعة التي لا نستطيع إعادة فتحها في مصدرها لا تُنشر «مع التحفظ»: تُستبعد، ويحيل المقال القارئ صراحةً إلى المصدر الرسمي.</li>
</ol>
<p>لهذا المنهج أثر ظاهر: تتضمن مقالاتنا جملًا مثل «لم نتمكن من التحقق من هذه النقطة، فتأكد منها على
<bdi>service-public.fr</bdi>». وهذا مقصود. فالمقال الذي يدّعي معرفة كل شيء عن قانون الأجانب يكذب.</p>

<h2 id="sources">المصادر التي نعتمدها</h2>
<div class="tablewrap">
<table>
<caption>المصادر الأولية المرجعية، حسب المجال.</caption>
<thead><tr><th>المجال</th><th>المصادر المعتمدة</th></tr></thead>
<tbody>
<tr><td>قانون الأجانب الفرنسي</td><td><bdi>Légifrance</bdi>، <bdi>service-public.fr</bdi>، وزارة الداخلية (<bdi>DGEF</bdi>)</td></tr>
<tr><td>امتحانات <bdi>DELF</bdi> و<bdi>DALF</bdi> و<bdi>TCF</bdi></td><td><bdi>France Éducation international</bdi></td></tr>
<tr><td>امتحانات <bdi>TEF</bdi> و<bdi>TEFAQ</bdi></td><td><bdi>Le français des affaires — CCI Paris Île-de-France</bdi></td></tr>
<tr><td>الهجرة الفدرالية الكندية</td><td><bdi>IRCC / canada.ca</bdi></td></tr>
<tr><td>الهجرة إلى كيبيك</td><td><bdi>MIFI / quebec.ca</bdi></td></tr>
<tr><td>المراكز والمواعيد والرسوم</td><td>قائمة المراكز المعتمدة لدى <bdi>France Éducation international</bdi>، ثم موقع كل مركز، في التاريخ المذكور أسفل كل صفحة</td></tr>
</tbody>
</table>
</div>
<p>قد تفيدنا مدوّنات المحامين ومواقع المستشارين والمواقع التجميعية <em>كخيط</em> لرصد موضوع ما. لكنها لا تكون أبدًا
المصدر النهائي لأي رقم.</p>

<h2 id="not">ما لا ننشره</h2>
<ul>
<li><strong>لا أسئلة امتحان «مسرّبة».</strong> أسئلة <bdi>TCF</bdi> سرية تمامًا. المواقع التي تبيع «توقعات الشهر» تنشر تزييفات أو وثائق حُصل عليها بطرق غير قانونية — وهي مخاطرة لا داعي لها بملفك.</li>
<li><strong>لا استشارة قانونية فردية.</strong> نشرح القواعد العامة. ولا نبدي رأيًا في وضعك الشخصي: فذلك شأن محامٍ أو الإدارة المختصة.</li>
<li><strong>لا وعد بنتيجة.</strong> لا توجد طريقة تضمن درجة.</li>
<li><strong>لا رقم دون مصدر.</strong> إن لم نستطع ربطه بمصدر رسمي مؤرَّخ، فلا يرد في المقال.</li>
</ul>

<h2 id="limits">حدودنا، بوضوح</h2>
<p>يُحرَّر هذا الموقع بشكل مستقل. فهو <strong>ليس رسميًا ولا تابعًا</strong> لـ<bdi>France Éducation international</bdi>
(<bdi>DELF</bdi>، <bdi>DALF</bdi>، <bdi>TCF</bdi>) ولا لـ<bdi>Le français des affaires — CCI Paris Île-de-France</bdi>
(<bdi>TEF</bdi>). تُذكر أسماء الامتحانات لوصف المحتوى المتناول فقط.</p>
<p>يستند الموقع إلى تطبيق للهاتف للتحضير للامتحانات، وهو نموذجه الاقتصادي: تحيل بعض المقالات إليه. وهذا لا يغيّر
القاعدة أعلاه — فنحن نوصي صراحةً بالموارد الرسمية المجانية حين تلبّي الحاجة، ونصف حدودها دون التقليل منها.</p>
<p>وأخيرًا، <strong>الأنظمة تتغيّر</strong>. المقال الدقيق في يوليو 2026 قد لا يبقى كذلك. تحمل كل صفحة تاريخ تحديثها
وتحيل إلى المصدر الرسمي الذي ينبغي مراجعته قبل أي خطوة ملزمة.</p>

<h2 id="error">الإبلاغ عن خطأ</h2>
<p>إذا لاحظت خطأً، فراسلنا: <strong><bdi>gockaman@gmail.com</bdi></strong>. اذكر إن أمكن الصفحة المعنية والمصدر الرسمي
الذي يجعلك تعتقد أننا أخطأنا. تُطبَّق التصحيحات الجوهرية ويُعدَّل تاريخ تحديث المقال تبعًا لذلك.</p>
<p>هذه أفضل خدمة يمكنك تقديمها لنا — ولكل القرّاء من بعدك.</p>

<h2 id="legal">البيانات القانونية</h2>
<div class="tablewrap">
<table>
<caption>المعلومات القانونية للناشر.</caption>
<thead><tr><th>العنصر</th><th>التفصيل</th></tr></thead>
<tbody>
<tr><td>الناشر ومدير النشر</td><td><strong><bdi>Augusto Grone</bdi></strong></td></tr>
<tr><td>التواصل</td><td><bdi>gockaman@gmail.com</bdi></td></tr>
<tr><td>الاستضافة</td><td><bdi>GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107</bdi>، الولايات المتحدة</td></tr>
<tr><td>الملكية الفكرية</td><td>محتوى أصلي © 2026 <bdi>delf-tcf-tef.fr</bdi></td></tr>
<tr><td>البيانات الشخصية</td><td>انظر <a href="/confidentialite/" hreflang="fr">سياسة الخصوصية</a> (بالفرنسية)</td></tr>
</tbody>
</table>
</div>
<div class="note">
<p><strong>العلامات المذكورة.</strong> <bdi>DELF</bdi> و<bdi>DALF</bdi> و<bdi>TCF</bdi> علامات لـ<bdi>France Éducation
international</bdi>. و<bdi>TEF</bdi> و<bdi>TEFAQ</bdi> و<bdi>TEF Canada</bdi> علامات لـ<bdi>Le français des affaires — CCI
Paris Île-de-France</bdi>. و<bdi>NCLC</bdi> و<bdi>CLB</bdi> إطاران مرجعيان لحكومة كندا. تُستعمل هذه الأسماء وصفًا فقط،
لتسمية الامتحانات التي يتناولها هذا الموقع.</p>
</div>

<h2>أدلّتنا</h2>
<ul class="posts">
<li><a href="/ar/">كل الصفحات بالعربية</a>
<p>أدلة موثّقة عن امتحان <bdi>TCF Canada</bdi> ودرجات <bdi>NCLC</bdi>، والتحضير، والأسعار، ومراكز الامتحان في الخليج ومصر ولبنان.</p></li>
</ul>
"""


def block(html, tag):
    m = re.search(rf'<{tag} class="site".*?</{tag}>', html, flags=re.S)
    if not m:
        raise SystemExit(f"pas de <{tag} class=site>")
    return m.group(0)


def alternates():
    alts = [(l, PATHS[l]) for l in ("fr", "en", "es", "ar")] + [("x-default", PATHS["fr"])]
    return "".join(f'<link rel="alternate" hreflang="{h}" href="{BASE}{p}">\n' for h, p in alts)


def langs(current):
    return '<p class="langs">' + " · ".join(
        f'<a href="{PATHS[l]}" hreflang="{l}" lang="{l}"' + (' dir="rtl"' if l == "ar" else "") + f">{LABEL[l]}</a>"
        for l in ("fr", "en", "es", "ar") if l != current) + "</p>"


def page(lang):
    src = open(os.path.join(ROOT, lang, "index.html"), encoding="utf-8").read()
    header, footer = block(src, "header"), block(src, "footer")
    path, title, desc = PATHS[lang], TITLE[lang], DESC[lang]
    home_path, home_label = HOME[lang]
    rtl = ' dir="rtl"' if lang == "ar" else ""
    crumb = f'<p class="crumb"><a href="{home_path}">{home_label}</a> › {CRUMB[lang]}</p>'
    ld = ('{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ['
          f'{{"@type": "ListItem", "position": 1, "name": "{home_label}", "item": "{BASE}{home_path}"}}, '
          f'{{"@type": "ListItem", "position": 2, "name": "{CRUMB[lang]}", "item": "{BASE}{path}"}}]}}')
    body = BODY[lang].replace("{langs}", langs(lang))
    return f"""<!DOCTYPE html>
<html lang="{lang}"{rtl}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{path}">
{alternates()}<link rel="stylesheet" href="/style.css">
<link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">
<link rel="icon" type="image/png" sizes="48x48" href="/img/favicon-48-v2.png">
<link rel="icon" type="image/png" sizes="96x96" href="/img/favicon-96-v2.png">
<link rel="icon" type="image/png" sizes="192x192" href="/img/favicon-192-v2.png">
<link rel="apple-touch-icon" href="/img/icon-180-v2.png">
<meta name="apple-itunes-app" content="app-id=6790412304">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}/img/og/a-propos.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{LOCALE[lang]}">
<meta property="og:site_name" content="delf-tcf-tef.fr">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{BASE}/img/og/a-propos.png">
<script type="application/ld+json">{ld}</script>
</head>
<body class="">
{header}
<article class="page"><div class="wrap narrow">
{crumb}
{body}
</div></article>
{footer}
</body>
</html>
"""


def write(path, text):
    f = os.path.join(ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(f), exist_ok=True)
    old = open(f, encoding="utf-8").read() if os.path.exists(f) else None
    if old != text:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(text)
    return old != text


def patch_fr():
    f = os.path.join(ROOT, "a-propos", "index.html")
    html = open(f, encoding="utf-8").read()
    canon = re.search(r'<link rel="canonical" href="[^"]+">\n', html)
    head, rest = html[:canon.end()], html[canon.end():]
    rest = re.sub(r'^(<link rel="alternate" hreflang="[^"]+" href="[^"]+">\n)+', "", rest)
    html = head + alternates() + rest
    meta = re.search(r'<p class="meta">.*?</p>\n', html)
    head, rest = html[:meta.end()], html[meta.end():]
    rest = re.sub(r'^<p class="langs">.*?</p>\n', "", rest, flags=re.S)
    html = head + langs("fr") + "\n" + rest
    return write("/a-propos/", html)


if __name__ == "__main__":
    for lang in ("en", "es", "ar"):
        print(f"{PATHS[lang]} : {'écrite' if write(PATHS[lang], page(lang)) else 'inchangée'}")
    print(f"/a-propos/ : {'hreflang posés' if patch_fr() else 'inchangée'}")
