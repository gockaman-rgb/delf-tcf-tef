# -*- coding: utf-8 -*-
"""Guides et pages d'examen en espagnol (/es/, make_i18n.py) — traductions de pages françaises, 08/10/2026.

Aucun fait nouveau : chaque chiffre, date et règle vient de la page française (fr_path) ou des pages pays
espagnoles (pays_config_es.py), avec sa date. Les exercices et sujets restent en français (examen de français) ;
consignes et explications en espagnol neutre (es-419, tú). Glossaire : i18n_glossary.md ; blocs : i18n_blocks.py.
"""
from i18n_blocks import exo, sujet  # noqa: F401
from pays_config import table  # noqa: F401

PAGES = []
INICIO = ("Inicio", "/es/")

# Fichas de países y ciudades, reutilizadas en las tres páginas de examen
CHIPS = """
<p class="serie-label">El DELF y el DALF, país por país</p>
<div class="chips">
<a class="chip" href="/es/delf-espana/">España</a>
<a class="chip" href="/es/delf-mexico/">México</a>
<a class="chip" href="/es/delf-colombia/">Colombia</a>
<a class="chip" href="/es/delf-argentina/">Argentina</a>
<a class="chip" href="/es/delf-chile/">Chile</a>
<a class="chip" href="/es/delf-peru/">Perú</a>
<a class="chip" href="/es/delf-ecuador/">Ecuador</a>
<a class="chip" href="/es/">Todos los países →</a>
</div>
<p class="serie-label">En España, ciudad por ciudad</p>
<div class="chips">
<a class="chip" href="/es/delf-madrid/">DELF en Madrid</a>
<a class="chip" href="/es/delf-barcelona/">DELF en Barcelona</a>
<a class="chip" href="/es/delf-sevilla/">DELF en Sevilla</a>
<a class="chip" href="/es/delf-valencia/">DELF en Valencia</a>
<a class="chip" href="/es/delf-granada/">DELF en Granada</a>
</div>
"""

CAP_PAIS = ("según nuestra revisión de los sitios web de los centros del 8 de octubre de 2026; precio para un candidato "
            "libre, en moneda local. El detalle, en la página de cada país.")

COMUN = """<p>Lo que se repite de un país a otro: te inscribes en el centro, dentro del plazo de la sesión —fuera de esas
fechas no se acepta ninguna inscripción—, y el día del examen necesitas la citación y un documento de identidad
oficial. En general no hay reembolso: en España, Colombia y Argentina se puede pasar a la sesión siguiente con un
certificado médico, mientras que en México no hay ni reembolso ni traspaso, salvo si el centro cancela la sesión. Los
resultados salen en la fecha que fija cada país —el 14 de diciembre de 2026 en México para la sesión de noviembre, el 17
de marzo de 2027 en España para la de febrero— y el diploma llega meses más tarde: de dos a tres meses después de la
convocatoria en España, de cinco a seis en Colombia.</p>
"""


# ===========================================================================
# DELF B2 — de /delf-b2/ y sus módulos (format-bareme, a-quoi-sert, ecrit-oral, inscription)
# ===========================================================================
PAGES.append(dict(
    fr_path="/delf-b2/", lang="es", variant="es-419", slug="delf-b2", accent="accent-delf",
    crumbs=[INICIO], crumb="Examen DELF B2", inline_cta=False,
    title="Examen DELF B2: estructura, puntuación, fechas y preparación",
    desc="Examen DELF B2: 4 pruebas en 2 h 50 min, aprobado con 50/100 y nota eliminatoria de 5/25. Para qué sirve, cómo prepararlo y fechas y precios por país.",
    h1="Examen DELF B2: las cuatro pruebas, la nota para aprobar y dónde presentarlo",
    intro="""El DELF B2 —lo que muchos llaman «certificado de francés B2»— es un <strong>diploma oficial válido de por
vida</strong>, expedido por el Ministerio de Educación Nacional de Francia. Cuatro pruebas calificadas sobre 25, un
total sobre <strong>100</strong> y el aprobado a partir de <strong>50/100</strong>, con una nota eliminatoria que cada
año deja sin diploma a candidatos cuyo promedio sí alcanzaba. Se presenta en un centro autorizado, en las fechas que
fija cada país: la próxima sesión del B2 es el <strong>12 de noviembre de 2026</strong> en México y el <strong>11 de
febrero de 2027</strong> en España. La estructura, la puntuación, para qué sirve, cómo prepararlo y las fechas, país
por país.""",
    facts=["<strong>4 pruebas de 25 puntos</strong> cada una: comprensión oral, comprensión escrita, expresión escrita y expresión oral. Total sobre <strong>100</strong>.",
           "Aprobado a partir de <strong>50/100</strong>.",
           "⚠️ Una nota inferior a <strong>5/25</strong> en una sola prueba es <strong>eliminatoria</strong>, sea cual sea el promedio.",
           "Duración: <strong>2 h 50 min</strong>, más 30 minutos de preparación antes del oral.",
           "Desde la reforma, las dos comprensiones son <strong>100 % de opción múltiple</strong> y la entrevista dirigida desapareció del oral. Formato generalizado en <strong>septiembre de 2024</strong>.",
           "<strong>Diploma de por vida</strong>: a diferencia del TCF o del TEF, no caduca nunca.",
           "Precio del B2: <strong>192 €</strong> en España (2027), <strong>2,500 pesos</strong> en México, <strong>490.000 pesos</strong> en Colombia, 137.000 pesos en Chile, 461 soles en Perú, 200 dólares en Ecuador y 163 € (295.030 pesos) en Argentina."],
    toc=[("que-es", "¿Qué es el DELF B2?"), ("recorrido", "Tu recorrido en 5 pasos"),
         ("estructura", "La estructura del examen: las cuatro pruebas"),
         ("puntuacion", "La puntuación y la trampa de la nota eliminatoria"), ("reforma", "Lo que cambió la reforma"),
         ("para-que-sirve", "¿Para qué sirve el DELF B2?"), ("escrito", "La expresión escrita, la prueba que decide"),
         ("oral", "La expresión oral: monólogo y debate"), ("preparacion", "Cómo prepararte"),
         ("fechas", "Fechas, precios e inscripción por país")],
    body="""
<div class="stats">
<div class="stat"><b>2 h 50 min</b><span>4 pruebas</span><em>CO 30 · CE 60 · EE 60 · EO 20 min</em></div>
<div class="stat"><b>50 / 100</b><span>para aprobar</span><em>promedio de las cuatro pruebas</em></div>
<div class="stat"><b>5 / 25</b><span>nota eliminatoria</span><em>en una sola prueba</em></div>
<div class="stat"><b>De por vida</b><span>validez del diploma</span><em>el TCF y el TEF valen dos años</em></div>
</div>

<h2 id="que-es">¿Qué es el DELF B2?</h2>
<p>El <strong>DELF B2</strong> es un <strong>diploma</strong> oficial del Ministerio de Educación Nacional de Francia,
expedido por France Éducation international, que certifica el nivel B2 del Marco común europeo de referencia: el de un
usuario independiente capaz de argumentar, defender una opinión y seguir un curso universitario. Se presenta en un
centro autorizado, en una de las sesiones del calendario de cada país, en <strong>cuatro pruebas</strong> calificadas
sobre 25: comprensión oral, comprensión escrita, expresión escrita de 250 palabras y expresión oral —una exposición
seguida de un debate—.</p>

<p>Se obtiene a partir de <strong>50/100</strong>, con una nota eliminatoria de 5/25, y es <strong>válido de por
vida</strong>. Es el diploma más solicitado del DELF: abre las universidades francesas y, en Francia, acredita desde el
1 de enero de 2026 el B2 exigido para la <strong>nacionalidad</strong> —de forma definitiva, mientras que un TCF IRN
caduca a los dos años—. Y es el mismo diploma en todos los países: lo expide France Éducation international, sea cual
sea el centro donde lo presentes.</p>

<h3>Para quién</h3>
<ul>
<li>Los estudiantes que apuntan a una <strong>universidad francesa o francófona</strong> —salvo las carreras que piden
el C1— o que deben acreditar su nivel de francés ante una universidad de su país.</li>
<li>Quienes quieren una prueba de nivel <strong>definitiva</strong>, sin repetir un examen cada dos años.</li>
<li>En Francia, los candidatos a la <strong>nacionalidad</strong>, que deben acreditar el B2 oral y escrito.</li>
</ul>

<h2 id="recorrido">Tu recorrido en 5 pasos</h2>
<ol class="steps">
<li><b>Verifica que el B2 es tu nivel</b><span>Universidad: B2, a veces C1; nacionalidad francesa: B2 oral y escrito desde 2026. <a href="#para-que-sirve">Para qué sirve el DELF B2.</a></span></li>
<li><b>¿Diploma o test?</b><span>El DELF B2 no caduca nunca; un TCF o un TEF vale dos años, y para Express Entry solo sirven el TCF Canada y el TEF Canada. <a href="/es/certificado-de-frances/">¿Cuál necesitas?</a></span></li>
<li><b>Prepara las cuatro pruebas</b><span>250 palabras argumentadas, un oral con debate, dos umbrales. <a href="#puntuacion">La puntuación</a>, <a href="#escrito">el escrito</a>, <a href="#oral">el oral</a> y los <a href="/es/delf-b2-ejemplos/">ejemplos resueltos</a>.</span></li>
<li><b>Inscríbete a tiempo</b><span>Cada país tiene su calendario, y las inscripciones cierran semanas antes de la prueba escrita: en México, el 23 de octubre para la sesión de noviembre de 2026. <a href="#fechas">Fechas y precios por país.</a></span></li>
<li><b>El día del examen, y después el diploma</b><span>Citación y documento de identidad; resultados en la fecha que fija cada país, diploma de por vida —y antes, un simulacro completo, para no pagar dos veces la inscripción—.</span></li>
</ol>

<h2 id="estructura">La estructura del examen: las cuatro pruebas</h2>
<p>Las tres primeras pruebas son <strong>colectivas</strong> y se encadenan en la misma media jornada. La expresión oral
es <strong>individual</strong> y puede ser otro día.</p>
""" + table("Estructura del DELF B2, versión surgida de la reforma de 2020, plenamente generalizada desde septiembre de 2024. Fuente: France Éducation international y Manual del candidato DELF B2.",
            ["Prueba", "Contenido", "Duración", "Nota"],
            [("Comprensión oral", "3 ejercicios / 5 documentos de audio", "30 min", "/25"),
             ("Comprensión escrita", "3 ejercicios / 5 documentos escritos", "60 min", "/25"),
             ("Expresión escrita", "1 ejercicio, 250 palabras como mínimo", "60 min", "/25"),
             ("Expresión oral", "2 partes: monólogo y debate", "20 min <em>(+ 30 min de preparación)</em>", "/25"),
             ("<strong>Total</strong>", "", "<strong>2 h 50 min</strong>", "<strong>/100</strong>")], wide=False) + """
<p><strong>En comprensión oral</strong>, los dos primeros ejercicios se basan en documentos de radio largos —de dos
minutos y medio a tres minutos, aproximadamente— que escuchas <strong>dos veces</strong>. El tercer ejercicio encadena
tres documentos cortos, de un minuto más o menos, que escuchas <strong>una sola vez</strong>. Esta asimetría es la
primera trampa del formato: a los candidatos acostumbrados a la doble escucha los sorprende el último ejercicio, justo
cuando la concentración ya está gastada.</p>

<p><strong>En comprensión escrita</strong>, los dos primeros ejercicios se basan en artículos largos, de unas 425 a 450
palabras. El tercero es distinto: tres documentos cortos de 100 a 120 palabras exponen tres puntos de vista sobre un
mismo tema, y tu tarea consiste en <strong>atribuir cada punto de vista a su autor</strong>. Es un ejercicio de lectura
comparativa, no de comprensión literal.</p>

<h2 id="puntuacion">La puntuación y la trampa de la nota eliminatoria</h2>
<p>El DELF no funciona como el TCF. Es un <strong>examen</strong>, no un test de nivel: se aprueba o no se aprueba. Dos
reglas deciden, y la segunda es la que los candidatos descubren demasiado tarde.</p>
""" + table("Los dos umbrales del DELF B2.", ["Regla", "Umbral", "Efecto"],
            [("Promedio general", "<strong>50/100</strong>", "Por debajo, no apruebas"),
             ("Nota mínima por prueba", "<strong>5/25</strong>", "Por debajo en <em>una sola</em> prueba, no apruebas, aunque tu promedio sea de 60/100")],
            wide=False) + """
<p>La consecuencia estratégica es clara, y va contra la intuición: <strong>una competencia muy débil te cuesta más de lo
que te aporta una competencia fuerte</strong>. Un candidato con 20/25 en comprensión escrita y 4/25 en expresión oral
no aprueba, aunque su promedio supere el umbral. El primer trabajo de preparación consiste, entonces, en <strong>sacar
tu prueba más débil de la zona eliminatoria</strong>, antes incluso de buscar puntos en otra parte.</p>

<p>Solo después viene la optimización del promedio: apuntar a 15 o más en tus pruebas fuertes para asegurar el total.
Porque en el DELF sí hay compensación entre pruebas —es lo que lo distingue del TCF y del TEF, donde la institución que
recibe tu expediente lee cada prueba por separado—.</p>

<h2 id="reforma">Lo que cambió la reforma</h2>
<p>El formato actual se generalizó por completo en <strong>septiembre de 2024</strong>. Tres cambios cuentan para tu
preparación, y dejan obsoleto cualquier modelo de examen anterior.</p>

<ul>
<li><strong>Las comprensiones pasaron a ser 100 % de opción múltiple.</strong> Desaparecieron las preguntas abiertas y
los verdadero/falso con justificación. Ya no redactas nada en estas dos pruebas, lo que cambia por completo la gestión
del tiempo: no hay redacción que cuidar, pero tampoco puedes ganar algunos puntos con una justificación parcialmente
correcta.</li>
<li><strong>Apareció el ejercicio de atribución de puntos de vista</strong> en comprensión escrita. Pide identificar una
postura argumentativa, no un dato.</li>
<li><strong>Se eliminó la entrevista dirigida</strong> del oral. La prueba empieza directamente con el monólogo. El
calentamiento amable que permitía relajarse ya no existe: entras en materia de inmediato.</li>
</ul>

<div class="note">
<p><strong>Cuidado con los recursos desactualizados.</strong> Gran parte de los modelos de examen, tutoriales y videos
que circulan en internet describe el formato anterior. Si un documento menciona una entrevista dirigida en el oral o
preguntas abiertas en comprensión, describe un examen que ya no existe. Verifica siempre la fecha de un recurso antes de
entrenar con él.</p>
</div>

<h2 id="para-que-sirve">¿Para qué sirve el DELF B2?</h2>
<p>El B2 es el nivel bisagra del sistema francés. Tres usos principales, más los que destacan los centros de cada
país.</p>

<ul>
<li><strong>La universidad francesa.</strong> La mayoría de las licenciaturas y maestrías exigen el B2. Algunas
carreras y algunas escuelas piden el C1; en ese caso, hay que apuntar al <a href="/es/dalf-c1/">DALF</a>. Lo que exige
la institución siempre prevalece sobre cualquier regla general.</li>
<li><strong>La nacionalidad francesa.</strong> Desde el <strong>1 de enero de 2026</strong>, la solicitud de
nacionalidad exige el nivel B2, oral y escrito. Un diploma DELF B2 lo acredita directamente, sin eximir del examen
cívico ni de las demás condiciones.</li>
<li><strong>Una prueba de nivel duradera.</strong> Es el argumento decisivo frente al TCF y al TEF. Una constancia de
test vale dos años; <strong>un diploma no caduca nunca</strong>. Si tu trámite va a extenderse varios años, el diploma
es, con mucho, la opción más segura.</li>
</ul>

<p>Los centros de España y de América Latina destacan otros usos. En España, los diplomas DELF y DALF están reconocidos
por la CRUE, la Conferencia de Rectores, para la acreditación de idiomas en las universidades, y según el Centro
Nacional de Exámenes el B2 es el mínimo requerido para una beca Erasmus. En México, según la Federación de Alianzas
Francesas, los diplomas DELF y DALF están reconocidos por la SEP a través de la norma CENNI. En Colombia, las Alianzas
presentan el DELF como una forma de acreditar el nivel de idioma que piden las universidades: verifica con la tuya qué
acepta.</p>

<div class="note">
<p><strong>Diploma o test: no es la misma lógica.</strong> El DELF certifica un nivel que acreditas de una vez por todas.
El TCF IRN o el TEF IRN te sitúan en una escala, con una constancia de duración limitada, pero se presentan en una
mañana y están pensados específicamente para los trámites administrativos franceses. Para un trámite en Francia, verifica en
service-public.fr la lista de justificantes aceptados antes de pagar una inscripción: además del nivel, una
certificación debe estar registrada en el repertorio específico. Y para emigrar a Canadá con Express Entry, IRCC solo
acepta el TCF Canada y el TEF Canada: el DELF no sirve. <a href="/es/certificado-de-frances/">¿Qué certificado de
francés elegir?</a></p>
</div>

<h2 id="escrito">La expresión escrita, la prueba que decide</h2>
<p>Un ejercicio, 60 minutos, <strong>250 palabras como mínimo</strong>. El tema pide una <strong>toma de posición
personal</strong>: contribución a un debate, carta formal, artículo crítico. Es la prueba más discriminante del DELF B2,
y aquella en la que la distancia entre un buen nivel de lengua y una buena nota es mayor.</p>

<p>Lo que evalúa el corrector no es tu opinión, sino tu <strong>capacidad para construirla</strong>:</p>

<ul>
<li><strong>La adecuación a la consigna y al género.</strong> Una carta formal sin fórmula de saludo ni estructura de
carta pierde puntos antes incluso de que se evalúe la lengua.</li>
<li><strong>La estructura argumentativa.</strong> Una postura clara, argumentos jerarquizados y la objeción contraria
tomada en cuenta. Acumular ideas correctas pero sin articular pone techo muy pronto a la nota.</li>
<li><strong>Los conectores lógicos.</strong> Son el marcador más visible del nivel B2, y el más fácil de trabajar de
forma mecánica.</li>
<li><strong>El registro.</strong> Pasar sin darte cuenta al registro coloquial es una pérdida de puntos frecuente entre
los candidatos que hablan bien francés en el día a día.</li>
<li><strong>La extensión.</strong> 250 palabras es un mínimo, no una meta. Por debajo, la adecuación a la consigna
falla, sea cual sea la calidad de la lengua.</li>
</ul>

<p>El plan en cinco partes, los tres géneros y los errores que más cuestan, con un tema de expresión escrita comentado,
están en los <a href="/es/delf-b2-ejemplos/">ejemplos resueltos del DELF B2</a>.</p>

<h2 id="oral">La expresión oral: monólogo y debate</h2>
<p>Treinta minutos de preparación y, después, veinte minutos de prueba en dos partes. Sacas al azar un breve documento
de partida, identificas una problemática y defiendes un punto de vista: primero solo, después frente al jurado, que te
contradice.</p>

<p>La segunda parte es la que sorprende. <strong>El jurado no está de acuerdo contigo, y es a propósito</strong>: su
papel es poner a prueba tu capacidad de sostener una postura, matizar y conceder sin ceder. Los candidatos que abandonan
su tesis a la primera objeción pierden puntos —no por la lengua, sino por la competencia evaluada—.</p>

<p>Los treinta minutos de preparación también se entrenan. No alcanzan para redactar un texto: sirven para construir un
plan y anotar palabras clave. Un candidato que redacta y lee sus notas se detecta de inmediato, y se le penaliza en
fluidez.</p>

<h2 id="preparacion">Cómo prepararte</h2>
<ol>
<li><strong>Un simulacro completo desde el principio</strong>, calificado con los baremos oficiales, para identificar tu
prueba más débil. Es la que decide, por la nota eliminatoria.</li>
<li><strong>Sacar esa prueba de la zona roja</strong> como prioridad absoluta, antes de buscar puntos en otra parte.</li>
<li><strong>Trabajar la expresión escrita por la estructura</strong>, no por el vocabulario. La mayoría de los puntos
perdidos viene del plan y de la consigna, no del léxico.</li>
<li><strong>Simular el oral en condiciones reales</strong>, con los 30 minutos de preparación incluidos y una
contradicción asumida en la segunda parte.</li>
<li><strong>Repetir simulacros cronometrados</strong> hasta que el formato ya no te sorprenda.</li>
</ol>

<p>En las dos expresiones, el punto ciego es el mismo que en todos los exámenes de francés: no puedes autoevaluarte con
criterios que no conoces. Saber si tu texto vale 9 o 13 sobre 25 es exactamente lo que resuelve la corrección con IA
según los criterios oficiales.</p>

<h2 id="fechas">Fechas, precios e inscripción por país</h2>
<p>Te inscribes <strong>en un centro autorizado</strong> —Alianza Francesa, Instituto Francés, universidad—, nunca en
France Éducation international. En cada país, un organismo de gestión central fija el calendario de sesiones y, a
menudo, las tarifas. Esto mostraban los sitios web de los centros el 8 de octubre de 2026:</p>
""" + table("DELF B2 tout public: la próxima sesión y su precio en cada país, " + CAP_PAIS,
            ["País", "Próxima sesión del B2", "Inscripción", "Precio"],
            [('<a href="/es/delf-espana/">España</a>', "11 de febrero de 2027", "del 1 de diciembre de 2026 al 9 de enero de 2027", "192 € (tarifa 2027)"),
             ('<a href="/es/delf-mexico/">México</a>', "12 de noviembre de 2026", "del 5 al 23 de octubre de 2026", "2,500 pesos"),
             ('<a href="/es/delf-colombia/">Colombia</a>', "5 de noviembre de 2026", "hasta el 9 de octubre de 2026", "490.000 pesos"),
             ('<a href="/es/delf-argentina/">Argentina</a>', "5 de diciembre de 2026", "hasta el 5 de noviembre de 2026", "163 € (295.030 pesos)"),
             ('<a href="/es/delf-chile/">Chile</a>', "4 y 5 de diciembre de 2026", "hasta el 30 de octubre de 2026", "137.000 pesos"),
             ('<a href="/es/delf-peru/">Perú</a>', "28 de noviembre de 2026", "hasta el 16 de octubre de 2026", "461 soles"),
             ('<a href="/es/delf-ecuador/">Ecuador</a>', "25 de noviembre o 10 de diciembre de 2026", "hasta el 6 de noviembre en Quito; hasta el 13 de noviembre para diciembre", "200 dólares")]) + """
""" + COMUN + CHIPS + """
<p><strong>¿Y en Francia?</strong> No hay tarifa nacional: en los 143 centros autorizados, cada uno fija su precio —de
125 a 280 € por el B2 en los centros que revisamos el 17 de septiembre de 2026—. Hay diez sesiones nacionales al año,
con el B2 siempre el miércoles a las 14:00, y las inscripciones cierran de cuatro a diez semanas antes de la prueba
escrita; algunas sesiones se llenan meses antes. Los resultados llegan en 4 a 6 semanas.</p>
""",
    cta_h2="Entrena en condiciones reales",
    cta_p="""Simulacros cronometrados con el formato reformado del DELF B2, calificados con el baremo oficial sobre 25 por
prueba y con alerta de nota eliminatoria, y corrección con IA de la expresión escrita y oral, en la app «TCF DELF TEF:
Tests 2026». La app está en español.""",
    faq=[("¿Qué es el examen DELF B2?", "Un diploma oficial del Ministerio de Educación Nacional de Francia que certifica el nivel B2 del Marco común europeo: cuatro pruebas calificadas sobre 25, aprobado a partir de 50/100 con una nota eliminatoria de 5/25, en 2 h 50 min más 30 minutos de preparación antes del oral. Es válido de por vida."),
         ("¿Cuál es la estructura del examen DELF B2?", "Cuatro pruebas: comprensión oral (30 minutos, 3 ejercicios sobre 5 documentos de audio), comprensión escrita (60 minutos, 3 ejercicios sobre 5 documentos escritos), expresión escrita (60 minutos, 250 palabras como mínimo) y expresión oral (20 minutos, monólogo y debate, después de 30 minutos de preparación). Las tres primeras son colectivas; el oral es individual y puede ser otro día."),
         ("¿Qué nota se necesita para aprobar el DELF B2?", "50 sobre 100. Las cuatro pruebas se califican sobre 25 puntos cada una y no hace falta aprobar cada una por separado, pero en cada una se necesita al menos 5: una nota inferior a 5 sobre 25 en una sola prueba es eliminatoria, sea cual sea el promedio general."),
         ("¿Qué cambió la reforma del DELF B2?", "Tres cosas. Las dos comprensiones pasaron a ser 100 % de opción múltiple: desaparecieron las preguntas abiertas y los verdadero/falso con justificación. La comprensión escrita incluye ahora un ejercicio de atribución de puntos de vista a sus autores. Y en el oral se eliminó la entrevista dirigida: solo quedan el monólogo y el debate con el jurado. Este formato se generalizó por completo en septiembre de 2024, lo que deja obsoleto cualquier modelo de examen anterior."),
         ("¿El DELF B2 es un test o un diploma?", "Un diploma: se aprueba o no se aprueba, y una vez obtenido no caduca nunca. Los tests TCF y TEF, en cambio, sitúan tu nivel sin umbral de aprobación, pero su constancia caduca a los dos años."),
         ("¿Cuántas palabras hay que escribir en la expresión escrita del DELF B2?", "250 palabras como mínimo, en un solo ejercicio, en 60 minutos. Es un mínimo, no una meta: escribir menos hace perder puntos en la adecuación a la consigna, sea cual sea la calidad de la lengua. El tema pide una toma de posición personal: contribución a un debate, carta formal o artículo crítico."),
         ("¿Cuándo es el próximo examen DELF B2?", "Depende del país. Según los sitios web de los centros el 8 de octubre de 2026: el 5 de noviembre en Colombia, el 12 de noviembre en México, el 25 de noviembre o el 10 de diciembre en Ecuador, el 28 de noviembre en Perú, el 4 y 5 de diciembre en Chile, el 5 de diciembre en Argentina y, en España, el 11 de febrero de 2027, con inscripción del 1 de diciembre de 2026 al 9 de enero de 2027."),
         ("¿Cuánto cuesta el examen DELF B2?", "Cada país fija su tarifa: 192 € en España (2027), 2,500 pesos en México, 490.000 pesos en Colombia, 137.000 pesos en Chile, 461 soles en Perú, 200 dólares en Ecuador y 163 € (295.030 pesos) en Argentina, para un candidato libre. En Francia no hay tarifa nacional: de 125 a 280 € según el centro."),
         ("¿Cuánto tiempo se necesita para pasar de B1 a B2?", "Cuenta en general de 4 a 6 meses de práctica regular. Si tu B1 es sólido y se trata sobre todo de dominar el formato del examen, de 6 a 10 semanas de entrenamiento metódico pueden bastar. La distancia entre B1 y B2 se juega sobre todo en la argumentación: en el B2 ya no basta con entender y contar, hay que tomar posición y defenderla."),
         ("¿El DELF B2 sirve para la nacionalidad francesa?", "Sí, para la condición de idioma: desde el 1 de enero de 2026, la nacionalidad francesa exige el B2, oral y escrito, y el DELF B2 lo acredita de por vida. No exime del examen cívico ni de las demás condiciones de la naturalización.")],
    also=[("/es/delf-b2-ejemplos/", "Examen DELF B2: ejemplos resueltos", "Un ejercicio corregido por prueba y el método de la expresión escrita."),
          ("/es/dalf-c1/", "Examen DALF C1 y C2", "El nivel siguiente, y la dispensa de test que da en la universidad francesa."),
          ("/es/certificado-de-frances/", "¿Qué certificado de francés elegir?", "DELF, DALF, TCF o TEF: lo que prueba cada uno y quién lo acepta.")],
    sources="""<strong>Los formatos cambian.</strong> La descripción del examen está actualizada al 7 de agosto de 2026; las
fechas y los precios por país vienen de nuestra revisión de los sitios web de los centros del 8 de octubre de 2026. Las
estructuras de las pruebas y los requisitos de las instituciones cambian con regularidad: verifica el formato en
<a href="https://www.france-education-international.fr/diplome/delf-tout-public" rel="noopener">france-education-international.fr</a>,
las fechas y el precio en el sitio web de tu centro y, para un trámite en Francia, las condiciones en
<a href="https://www.service-public.fr/" rel="noopener">service-public.fr</a> antes de inscribirte.""",
))


# ===========================================================================
# DELF B1 — de /delf-b1/ y sus módulos (format-bareme, ecrit-oral, inscription); sin el módulo carte-de-resident
# ===========================================================================
PAGES.append(dict(
    fr_path="/delf-b1/", lang="es", variant="es-419", slug="delf-b1", accent="accent-delf",
    crumbs=[INICIO], crumb="Examen DELF B1", inline_cta=False,
    title="Examen DELF B1: estructura, puntuación, fechas y preparación",
    desc="Examen DELF B1: 4 pruebas en 2 h 10 min, aprobado con 50/100, 160 palabras por escrito y un oral en 3 partes. Fechas y precios en España y América Latina.",
    h1="Examen DELF B1: acreditar el nivel umbral, de por vida",
    intro="""El DELF B1 certifica el <strong>nivel umbral</strong>: aquel en el que uno se vuelve autónomo en francés.
Cuatro pruebas en <strong>2 h 10 min</strong>, calificadas sobre 25 cada una, con el aprobado a partir de
<strong>50/100</strong>, y un diploma que no caduca nunca. Se presenta en las fechas que fija cada país —la próxima
sesión del B1 es el <strong>11 de noviembre de 2026</strong> en México y el <strong>12 de febrero de 2027</strong> en
España— y, en Francia, desde el 1 de enero de 2026 es además el nivel exigido para una primera <strong>tarjeta de
residente</strong>.""",
    facts=["<strong>4 pruebas de 25 puntos</strong> cada una, total sobre <strong>100</strong>, aprobado a partir de <strong>50/100</strong>.",
           "⚠️ Una nota inferior a <strong>5/25</strong> en una sola prueba es <strong>eliminatoria</strong>.",
           "Duración total: <strong>2 h 10 min</strong>.",
           "<strong>Diploma de por vida</strong>, expedido por el Ministerio de Educación Nacional de Francia.",
           "Precio del B1: <strong>162 €</strong> en España (2027), <strong>1,800 pesos</strong> en México, <strong>383.000 pesos</strong> en Colombia, 127.000 pesos en Chile, 385 soles en Perú, 160 dólares en Ecuador y 163 € (295.030 pesos) en Argentina.",
           "⚠️ En Francia, no confundas los tres niveles: <strong>A2</strong> para la primera tarjeta de estancia plurianual, <strong>B1</strong> para una primera tarjeta de residente —exigido desde el 1 de enero de 2026 por la orden del 22 de diciembre de 2025, en lugar del A2—, <strong>B2</strong> para la nacionalidad."],
    toc=[("que-es", "¿Qué es el DELF B1?"), ("recorrido", "Tu recorrido en 5 pasos"),
         ("estructura", "La estructura del examen: las cuatro pruebas"),
         ("puntuacion", "La puntuación y la nota eliminatoria"), ("escrito", "La expresión escrita en 160 palabras"),
         ("oral", "El oral en tres partes"), ("preparacion", "Cómo prepararte"),
         ("fechas", "Fechas, precios e inscripción por país")],
    body="""
<div class="stats">
<div class="stat"><b>2 h 10 min</b><span>4 pruebas</span><em>CO 25 · CE 45 · EE 45 · EO 15 min</em></div>
<div class="stat"><b>50 / 100</b><span>para aprobar</span><em>promedio de las cuatro pruebas</em></div>
<div class="stat"><b>5 / 25</b><span>nota eliminatoria</span><em>en una sola prueba</em></div>
<div class="stat"><b>De por vida</b><span>validez del diploma</span><em>el TCF y el TEF valen dos años</em></div>
</div>

<h2 id="que-es">¿Qué es el DELF B1?</h2>
<p>El <strong>DELF B1</strong> es un <strong>diploma</strong> oficial del Ministerio de Educación Nacional de Francia,
expedido por France Éducation international, que certifica el nivel B1 del Marco común europeo de referencia —el «nivel
umbral», el de un usuario independiente capaz de desenvolverse en la mayoría de las situaciones de la vida diaria—. Se
presenta en un centro autorizado, en una de las sesiones del calendario de cada país, en <strong>cuatro
pruebas</strong> calificadas sobre 25: comprensión oral, comprensión escrita, expresión escrita (160 palabras) y
expresión oral en tres partes.</p>

<p>Se obtiene a partir de <strong>50/100</strong>, con una nota eliminatoria de 5/25 en una sola prueba, y es
<strong>válido de por vida</strong>: un test TCF o TEF, en cambio, caduca a los dos años.</p>

<h3>Para quién</h3>
<ul>
<li>Quienes quieren una prueba de nivel <strong>definitiva</strong>, para un expediente, un CV o una formación.</li>
<li>En España, quienes deben acreditar un nivel de idioma en la universidad: según el Centro Nacional de Exámenes, el
B1 permite acreditar el nivel exigido para el título de <em>grado</em> en la mayoría de las comunidades autónomas, y los
diplomas DELF y DALF están reconocidos por la CRUE.</li>
<li>En Francia, quienes solicitan una primera <strong>tarjeta de residente</strong>, que deben acreditar el B1 oral y
escrito. No los candidatos a la nacionalidad: desde 2026, hace falta el <a href="/es/delf-b2/">B2</a>.</li>
</ul>

<h2 id="recorrido">Tu recorrido en 5 pasos</h2>
<ol class="steps">
<li><b>Verifica que el B1 es tu nivel</b><span>En Francia: tarjeta de residente, B1 desde 2026; nacionalidad, B2. Para la universidad, verifica lo que exige la tuya. <a href="/es/delf-b2/">El DELF B2.</a></span></li>
<li><b>¿Diploma o test?</b><span>El DELF no caduca nunca, pero se presenta en pocas sesiones al año —cuatro para adultos en España y en México—, con inscripciones que cierran pronto; un TCF vale dos años. <a href="/es/certificado-de-frances/">Cuál elegir.</a></span></li>
<li><b>Prepara las cuatro pruebas</b><span>160 palabras por escrito, un oral en tres partes y dos umbrales que respetar. <a href="#puntuacion">La puntuación</a>, <a href="#escrito">el escrito</a>, <a href="#oral">el oral</a>.</span></li>
<li><b>Inscríbete a tiempo</b><span>Cada país tiene su calendario: en Perú, la sesión del 28 de noviembre de 2026 cierra sus inscripciones el 16 de octubre. <a href="#fechas">Fechas y precios por país.</a></span></li>
<li><b>El día del examen, y después el diploma</b><span>Citación y documento de identidad; diploma válido de por vida —y antes, un simulacro completo, para no pagar dos veces—.</span></li>
</ol>

<h2 id="estructura">La estructura del examen: las cuatro pruebas</h2>
""" + table("Estructura del DELF B1. Fuente: France Éducation international, estructura verificada en julio de 2026.",
            ["Prueba", "Contenido", "Duración", "Nota"],
            [("Comprensión oral", "3 documentos, preguntas de opción múltiple", "25 min", "/25"),
             ("Comprensión escrita", "2 documentos, preguntas de opción múltiple", "45 min", "/25"),
             ("Expresión escrita", "1 ejercicio, 160 palabras como mínimo", "45 min", "/25"),
             ("Expresión oral", "3 partes <em>(10 min de preparación para la 3.ª)</em>", "15 min", "/25"),
             ("<strong>Total</strong>", "", "<strong>2 h 10 min</strong>", "<strong>/100</strong>")], wide=False) + """
<p>Las tres primeras pruebas son colectivas y se encadenan en la misma media jornada. La expresión oral es individual y
puede ser otro día. Es un examen corto —unos 40 minutos menos que el <a href="/es/delf-b2/">DELF B2</a>—, pero el
encadenamiento de las tres pruebas colectivas sigue siendo denso.</p>

<h2 id="puntuacion">La puntuación y la nota eliminatoria</h2>
<p>El DELF es un <strong>examen</strong>, no un test de nivel: se aprueba o no se aprueba. Dos reglas deciden el
resultado.</p>
""" + table("Los dos umbrales del DELF B1.", ["Regla", "Umbral", "Efecto"],
            [("Promedio general", "<strong>50/100</strong>", "Por debajo, no apruebas"),
             ("Nota mínima por prueba", "<strong>5/25</strong>", "Por debajo en <em>una sola</em> prueba, no apruebas, aunque tu promedio sea de 60/100")],
            wide=False) + """
<p>La consecuencia es la misma que en el B2, y orienta toda la preparación: <strong>una competencia muy débil cuesta más
de lo que aporta una competencia fuerte</strong>. Un candidato que destaca en el escrito pero se queda en 4/25 en el
oral no aprueba, sea cual sea su total. La primera prioridad es, entonces, sacar tu prueba más débil de la zona
eliminatoria, no pulir aquella en la que ya eres bueno.</p>

<p>Dicho esto, la compensación existe: por encima del mínimo de 5, los puntos se compensan de una prueba a otra. Es lo
que distingue al DELF del TCF y del TEF, donde la institución que recibe tu expediente lee cada prueba por separado, sin
compensación posible.</p>

<h2 id="escrito">La expresión escrita en 160 palabras</h2>
<p>Un ejercicio, 45 minutos, <strong>160 palabras como mínimo</strong>. El tema pide expresar una toma de posición
personal sobre un tema general: ensayo, carta, artículo. Todavía no es la argumentación estructurada del B2, pero
tampoco la descripción factual del A2.</p>

<p>Lo que marca la diferencia en este nivel:</p>

<ul>
<li><strong>Respetar el género pedido.</strong> Una carta sin fórmula de saludo ni fórmula de despedida pierde puntos
antes de que se evalúe la lengua.</li>
<li><strong>Los conectores.</strong> En el B1 se espera un encadenamiento explícito de las ideas: <em lang="fr">d'abord,
ensuite, cependant, c'est pourquoi</em>. Es el marcador más rentable de trabajar.</li>
<li><strong>Los tiempos del pasado.</strong> La alternancia entre el <em lang="fr">passé composé</em> y el
<em lang="fr">imparfait</em> es el punto gramatical más discriminante del nivel, y el que más se penaliza.</li>
<li><strong>La extensión.</strong> 160 palabras es un mínimo. Por debajo, no se respeta la consigna, sea cual sea la
calidad de la lengua.</li>
</ul>

<h2 id="oral">El oral en tres partes</h2>
<p>Quince minutos, tres ejercicios encadenados —y una sola preparación, para el último—.</p>

<ol>
<li><strong>La entrevista dirigida.</strong> Te presentas y te hacen preguntas sobre ti, tus actividades, tus proyectos.
Sin preparación. Es la parte más fácil de asegurar: es previsible y se puede ensayar con anticipación.</li>
<li><strong>El ejercicio en interacción.</strong> Representas con el examinador una situación de la vida diaria: resolver
un problema, conseguir algo, negociar. Tampoco hay preparación.</li>
<li><strong>La expresión de un punto de vista</strong> a partir de un breve documento de partida, con <strong>10 minutos
de preparación</strong>. Identificas el tema y das tu opinión.</li>
</ol>

<p>A diferencia del DELF B2, donde se eliminó la entrevista dirigida, en el B1 <strong>sigue existiendo</strong>. Es una
buena noticia para los candidatos nerviosos: la prueba empieza con el ejercicio más accesible, lo que da tiempo para
tomar confianza.</p>

<h2 id="preparacion">Cómo prepararte</h2>
<ol>
<li><strong>Un simulacro completo desde el principio</strong>, calificado con los baremos oficiales, para identificar la
prueba que puede eliminarte.</li>
<li><strong>Sacar esa prueba de la zona roja</strong> como prioridad, antes que todo lo demás.</li>
<li><strong>Ensayar las dos primeras partes del oral</strong>, que son previsibles y se preparan palabra por palabra: es
el mejor rendimiento de toda la preparación del B1.</li>
<li><strong>Trabajar los tiempos del pasado y los conectores</strong>, los dos puntos gramaticales más rentables en este
nivel.</li>
<li><strong>Simulacros cronometrados con regularidad</strong>, hasta que el encadenamiento de las tres pruebas colectivas
deje de ser una prueba de resistencia.</li>
</ol>

<p>En las dos expresiones no puedes autoevaluarte con criterios que no conoces, y es justo ahí donde se juega la nota
eliminatoria. Eso es lo que resuelve la corrección con IA según los criterios oficiales.</p>

<h2 id="fechas">Fechas, precios e inscripción por país</h2>
<p>Te inscribes <strong>en un centro autorizado</strong>, nunca en France Éducation international, dentro del plazo de
cada sesión. En cada país, un organismo de gestión central fija el calendario y, a menudo, las tarifas. Esto mostraban
los sitios web de los centros el 8 de octubre de 2026:</p>
""" + table("DELF B1 tout public: la próxima sesión y su precio en cada país, " + CAP_PAIS,
            ["País", "Próxima sesión del B1", "Inscripción", "Precio"],
            [('<a href="/es/delf-espana/">España</a>', "12 de febrero de 2027", "del 1 de diciembre de 2026 al 9 de enero de 2027", "162 € (tarifa 2027)"),
             ('<a href="/es/delf-mexico/">México</a>', "11 de noviembre de 2026", "del 5 al 23 de octubre de 2026", "1,800 pesos"),
             ('<a href="/es/delf-colombia/">Colombia</a>', "4 de noviembre de 2026", "hasta el 9 de octubre de 2026", "383.000 pesos"),
             ('<a href="/es/delf-argentina/">Argentina</a>', "4 de diciembre de 2026", "hasta el 5 de noviembre de 2026", "163 € (295.030 pesos)"),
             ('<a href="/es/delf-chile/">Chile</a>', "ninguna abierta: las de 2026 fueron en abril y agosto", "calendario 2027 sin publicar", "127.000 pesos"),
             ('<a href="/es/delf-peru/">Perú</a>', "28 de noviembre de 2026", "hasta el 16 de octubre de 2026", "385 soles"),
             ('<a href="/es/delf-ecuador/">Ecuador</a>', "24 de noviembre o 9 de diciembre de 2026", "hasta el 6 de noviembre en Quito; hasta el 13 de noviembre para diciembre", "160 dólares")]) + """
""" + COMUN + CHIPS + """
<p><strong>¿Y en Francia?</strong> El B1 se presenta en los 143 centros autorizados —universidades, Alianzas Francesas,
escuelas de idiomas—, en diez sesiones nacionales al año, siempre el miércoles a las 10:00. Cada centro fija su precio
—de 125 a 230 € en los centros que revisamos el 17 de septiembre de 2026— y su plazo de inscripción, que cierra de
cuatro a diez semanas antes de la prueba escrita, y a veces solo está abierto dos días. Los resultados llegan en 4 a 6
semanas.</p>
""",
    cta_h2="Entrena en condiciones reales",
    cta_p="""Simulacros cronometrados con el formato del DELF B1, calificados con el baremo oficial sobre 25 por prueba y
con alerta de nota eliminatoria, y corrección con IA de la expresión escrita y oral, en la app «TCF DELF TEF: Tests
2026». La app está en español.""",
    faq=[("¿Qué es el DELF B1?", "Un diploma oficial del Ministerio de Educación Nacional de Francia que certifica el nivel B1 del Marco común europeo: cuatro pruebas calificadas sobre 25, aprobado a partir de 50/100 con una nota eliminatoria de 5/25, en 2 h 10 min. Es válido de por vida y, en Francia, se exige desde enero de 2026 para una primera tarjeta de residente."),
         ("¿El DELF B1 es un test o un diploma?", "Un diploma: se aprueba o no se aprueba, y una vez obtenido no caduca nunca. Los tests TCF y TEF, en cambio, sitúan tu nivel en una escala sin umbral de aprobación, pero su constancia caduca a los dos años."),
         ("¿Cuánto dura el examen DELF B1?", "2 h 10 min: 25 minutos de comprensión oral, 45 minutos de comprensión escrita, 45 minutos de expresión escrita y 15 minutos de expresión oral, con 10 minutos de preparación para la tercera parte del oral."),
         ("¿Qué nota se necesita para aprobar el DELF B1?", "50 sobre 100. Las cuatro pruebas se califican sobre 25 puntos cada una. Una nota inferior a 5 sobre 25 en una sola prueba es eliminatoria, aunque tu promedio supere con creces el umbral."),
         ("¿Cuántas palabras hay que escribir en el DELF B1?", "160 palabras como mínimo, en un solo ejercicio, en 45 minutos. Se trata de expresar una toma de posición personal sobre un tema general: ensayo, carta o artículo. Es un mínimo: escribir menos cuesta puntos en la adecuación a la consigna."),
         ("¿En qué consiste la prueba oral del DELF B1?", "Tres partes encadenadas en 15 minutos: una entrevista dirigida en la que te presentas, un ejercicio en interacción en el que representas una situación de la vida diaria, y la expresión de un punto de vista a partir de un breve documento de partida. Solo la tercera parte tiene 10 minutos de preparación."),
         ("¿Cuándo es el próximo examen DELF B1?", "Depende del país. Según los sitios web de los centros el 8 de octubre de 2026: el 4 de noviembre en Colombia, el 11 de noviembre en México, el 24 de noviembre o el 9 de diciembre en Ecuador, el 28 de noviembre en Perú, el 4 de diciembre en Argentina y, en España, el 12 de febrero de 2027. En Chile, las sesiones de B1 de 2026 ya habían pasado."),
         ("¿Cuánto cuesta el DELF B1?", "Cada país fija su tarifa: 162 € en España (2027), 1,800 pesos en México, 383.000 pesos en Colombia, 127.000 pesos en Chile, 385 soles en Perú, 160 dólares en Ecuador y 163 € (295.030 pesos) en Argentina. En Francia no hay tarifa nacional: de 125 a 230 € según el centro."),
         ("¿B1 o B2 para la nacionalidad francesa?", "El B2, oral y escrito, desde el 1 de enero de 2026. El B1 sirve para la tarjeta de residente; el A2, para la primera tarjeta de estancia plurianual.")],
    also=[("/es/delf-b2/", "Examen DELF B2", "El nivel siguiente: estructura, puntuación y fechas por país."),
          ("/es/certificado-de-frances/", "¿Qué certificado de francés elegir?", "Diploma o test: por qué un diploma es más seguro cuando un trámite se alarga."),
          ("/es/", "TCF Canada y DELF, país por país", "Centros, precios y fechas en España y América Latina.")],
    sources="""<strong>Las normas cambian.</strong> La descripción del examen está actualizada al 7 de agosto de 2026 y no
constituye asesoría jurídica; las fechas y los precios por país vienen de nuestra revisión de los sitios web de los
centros del 8 de octubre de 2026. Los niveles exigidos y las listas de justificantes aceptados cambian: verifica tu
situación —para un trámite en Francia, en <a href="https://www.service-public.fr/" rel="noopener">service-public.fr</a>— y
el formato del examen en
<a href="https://www.france-education-international.fr/diplome/delf-tout-public" rel="noopener">france-education-international.fr</a>
antes de inscribirte.""",
))


# ===========================================================================
# DALF C1 (y C2) — de /dalf/ y sus módulos (format, synthese-preparation, c1-ou-c2, inscription)
# ===========================================================================
PAGES.append(dict(
    fr_path="/dalf/", lang="es", variant="es-419", slug="dalf-c1", accent="accent-delf",
    crumbs=[INICIO], crumb="DALF C1 y C2", inline_cta=False,
    title="Examen DALF C1 y C2: estructura, síntesis, fechas y precios",
    desc="Examen DALF C1: 4 pruebas en 4 h 30 min, síntesis de 200 a 240 palabras, aprobado con 50/100; el C2, en 2 pruebas. Convocatorias y precios por país.",
    h1="Examen DALF C1 y C2: las pruebas, la síntesis y cómo prepararte",
    intro="""El DALF —<em lang="fr">Diplôme approfondi de langue française</em>— certifica los niveles <strong>C1</strong> y
<strong>C2</strong>. Es <strong>válido de por vida</strong>, y el C1 exime de cualquier test de idioma para entrar a las
universidades francesas. El C1 y el C2 no tienen en absoluto el mismo formato: cuatro pruebas en <strong>4
horas</strong> de un lado —con una síntesis de documentos de 200 a 240 palabras—, <strong>dos pruebas
integradas</strong> del otro. Se presenta en los mismos centros y sesiones que el DELF: la próxima sesión del C1
es el <strong>13 de noviembre de 2026</strong> en México y el <strong>10 de febrero de 2027</strong> en España.""",
    facts=["<strong>DALF C1</strong>: 4 pruebas, <strong>4 h 30 min</strong> más 1 hora de preparación vigilada antes del oral. Calificadas sobre 25 cada una, total sobre 100.",
           "<strong>DALF C2</strong>: solo 2 pruebas integradas, calificadas sobre 50 cada una.",
           "Aprobado con <strong>50/100</strong> en los dos casos. Nota eliminatoria: <strong>5/25</strong> en el C1, <strong>10/50</strong> en el C2.",
           "La prueba reina del C1 es la <strong>síntesis de documentos</strong>: de 200 a 240 palabras, objetiva, totalmente reformulada.",
           "<strong>Diploma de por vida</strong>, a diferencia de las constancias del TCF y del TEF, válidas dos años.",
           "Las antiguas opciones (letras y ciencias humanas, o ciencias) se <strong>eliminaron</strong>.",
           "Precio del C1: <strong>249 €</strong> en España (2027), <strong>3,500 pesos</strong> en México, 591.000 pesos en Colombia, 167.000 pesos en Chile, 543 soles en Perú, 240 dólares en Ecuador y 246 € (445.260 pesos) en Argentina."],
    toc=[("que-es", "¿Qué es el DALF?"), ("recorrido", "Tu recorrido en 5 pasos"),
         ("c1", "El DALF C1, prueba por prueba"), ("c2", "El DALF C2: dos pruebas integradas"),
         ("puntuacion", "La puntuación y las notas eliminatorias"), ("sintesis", "La síntesis: la prueba reina del C1"),
         ("preparacion", "Cómo prepararte"), ("c1-o-c2", "¿C1 o C2? Cuál elegir"),
         ("dispensa", "Lo que el DALF te ahorra"), ("fechas", "Sesiones, precios e inscripción por país")],
    body="""
<div class="stats">
<div class="stat"><b>4 h 30 min</b><span>de pruebas en el C1</span><em>+ 1 h de preparación; 4 h en el C2</em></div>
<div class="stat"><b>C1 · C2</b><span>dos diplomas independientes</span><em>puedes inscribirte directamente en el C2</em></div>
<div class="stat"><b>50 / 100</b><span>para aprobar</span><em>5/25 eliminatorio en el C1</em></div>
<div class="stat"><b>De por vida</b><span>validez del diploma</span><em>sin test en la universidad francesa</em></div>
</div>

<h2 id="que-es">¿Qué es el DALF?</h2>
<p>El <strong>DALF</strong> es el diploma oficial del Ministerio de Educación Nacional de Francia para los dos niveles
avanzados del Marco común europeo de referencia: el <strong>C1</strong>, el de un usuario autónomo capaz de un discurso
claro y estructurado, y el <strong>C2</strong>, el del dominio. Como el DELF, lo expide France Éducation international,
se presenta en los mismos centros autorizados y en las mismas sesiones, y es <strong>válido de por vida</strong>.</p>

<p>El <strong>DALF C1</strong> tiene cuatro pruebas calificadas sobre 25, en 4 h 30 min más una hora de preparación:
comprensiones, expresión escrita —una síntesis de documentos de 200 a 240 palabras seguida de un ensayo— y exposición
oral. El <strong>DALF C2</strong> solo tiene dos pruebas integradas, calificadas sobre 50: una oral y una escrita de 700
palabras como mínimo. Se aprueba con 50/100 en los dos casos. El DALF <strong>exime de cualquier test de
francés</strong> para entrar a las universidades francesas.</p>

<h3>Para quién</h3>
<ul>
<li>Los estudiantes cuya carrera exige el <strong>C1</strong>: letras, derecho, medicina, algunas grandes escuelas.</li>
<li>Los profesionales que quieren una prueba de nivel avanzado, <strong>de por vida</strong>.</li>
<li>No para los trámites administrativos franceses, que se quedan en el B2: basta el <a href="/es/delf-b2/">DELF B2</a>.</li>
</ul>

<h2 id="recorrido">Tu recorrido en 5 pasos</h2>
<ol class="steps">
<li><b>¿C1 o C2?</b><span>El C1 basta para casi todos los trámites; el C2 es un ejercicio de dominio. <a href="#c1-o-c2">Cuál elegir.</a></span></li>
<li><b>Conoce las pruebas</b><span>Síntesis y ensayo en el C1, texto de 700 palabras en el C2, exposición después de una hora de preparación. <a href="#c1">El C1</a>, <a href="#c2">el C2</a>.</span></li>
<li><b>Trabaja la síntesis</b><span>De 200 a 240 palabras, ninguna cita, ninguna opinión: la prueba reina del C1. <a href="#sintesis">El método.</a></span></li>
<li><b>Inscríbete a tiempo</b><span>Mismos centros y mismas sesiones que el DELF; no todos los centros abren el DALF en cada sesión. <a href="#fechas">Convocatorias y precios por país.</a></span></li>
<li><b>El día del examen, y después el diploma</b><span>Diploma de por vida, y la <a href="#dispensa">dispensa de test</a> de francés que te da en la universidad francesa.</span></li>
</ol>

<h2 id="c1">El DALF C1, prueba por prueba</h2>
<p>Es el examen más largo de toda la familia DELF-DALF: <strong>cuatro horas y media de pruebas</strong>, a las que se suma
<strong>una hora de preparación vigilada</strong> antes del oral.</p>
""" + table("Estructura del DALF C1. Fuente: France Éducation international, estructura verificada en julio de 2026.",
            ["Prueba", "Contenido", "Duración", "Nota"],
            [("Comprensión oral", "2 ejercicios: 1 documento largo (≈ 8 min, 2 escuchas) + varios documentos cortos (1 escucha)", "40 min", "/25"),
             ("Comprensión escrita", "1 ejercicio: texto argumentativo de unas 1000 palabras", "50 min", "/25"),
             ("Expresión escrita", "2 ejercicios: síntesis de documentos (200-240 palabras) + ensayo argumentativo (250 palabras como mínimo)", "2 h 30 min", "/25"),
             ("Expresión oral", "Exposición a partir de un dossier, y después discusión", "30 min <em>(+ 1 h de preparación)</em>", "/25"),
             ("<strong>Total</strong>", "", "<strong>4 h 30 min</strong> <em>(+ 1 h de preparación)</em>", "<strong>/100</strong>")], wide=False) + """
<p>Dos rasgos distinguen el C1 del <a href="/es/delf-b2/">B2</a>, mucho más allá de la dificultad de la lengua. Primero,
la <strong>comprensión escrita tiene un solo texto</strong>, pero un texto argumentativo de unas mil palabras: ya no es
lectura selectiva, es lectura analítica. Después, la expresión escrita dura <strong>dos horas y media</strong> y contiene
<em>dos</em> ejercicios de naturaleza completamente distinta: una síntesis objetiva y, luego, un ensayo personal. Muchos
candidatos subestiman el cambio de mentalidad que eso exige.</p>

<h2 id="c2">El DALF C2: dos pruebas integradas</h2>
<p>El C2 no se limita a ser «más difícil». Cambia de estructura: las cuatro competencias ya no se evalúan por separado,
sino fusionadas en <strong>dos ámbitos</strong>.</p>
""" + table("Estructura del DALF C2. Fuente: France Éducation international, estructura verificada en julio de 2026.",
            ["Ámbito", "Contenido", "Duración", "Nota"],
            [("Comprensión y expresión orales", "Escucha de un documento (≈ 14 min, 2 escuchas), y después resumen, monólogo y debate con el jurado", "30 min <em>(+ 1 h de preparación)</em>", "/50"),
             ("Comprensión y expresión escritas", "Redacción de un texto estructurado de <strong>700 palabras como mínimo</strong> a partir de un dossier de unas 2000 palabras", "3 h 30 min", "/50"),
             ("<strong>Total</strong>", "", "<strong>4 h</strong> <em>(+ 1 h de preparación)</em>", "<strong>/100</strong>")], wide=False) + """
<p>La prueba escrita del C2 es el ejercicio más exigente de todo el edificio: leer un dossier de dos mil palabras y sacar
de él un texto estructurado de al menos setecientas, en tres horas y media. Ya no es un examen de lengua: es un examen de
pensamiento en francés.</p>

<h2 id="puntuacion">La puntuación y las notas eliminatorias</h2>
""" + table("Los umbrales del DALF, nivel por nivel.", ["", "DALF C1", "DALF C2"],
            [("Pruebas", "4, calificadas sobre 25", "2 ámbitos, calificados sobre 50"),
             ("Aprobado", "<strong>50/100</strong>", "<strong>50/100</strong>"),
             ("Nota eliminatoria", "menos de <strong>5/25</strong> en una prueba", "menos de <strong>10/50</strong> en un ámbito")],
            wide=False) + """
<p>El mecanismo es el mismo que en los niveles inferiores, pero sus consecuencias son más brutales en el C2: con solo dos
notas, <strong>una prueba fallida es matemáticamente imposible de compensar</strong>. Un candidato con 45/50 en el oral y
9/50 en el escrito (54/100) no aprueba, aunque solo le faltara un punto para superar el umbral eliminatorio.</p>

<h2 id="sintesis">La síntesis: la prueba reina del C1</h2>
<p>Reducir varios documentos a un texto único, objetivo, totalmente reformulado y calibrado al número de palabras: la
síntesis no se improvisa. Es una <strong>técnica</strong>, y eso es una buena noticia: una técnica se aprende, a
diferencia de un nivel de lengua, que tarda meses en subir.</p>

<p>La gobiernan tres reglas absolutas, y romperlas cuesta más caro que cualquier error de lengua:</p>

<ul>
<li><strong>Ninguna cita.</strong> Todo debe reformularse. Copiar incluso una expresión llamativa del documento original
se penaliza: es justamente la competencia evaluada.</li>
<li><strong>Ninguna opinión personal.</strong> La síntesis es neutral de principio a fin. Tú no existes en ese texto.
Para eso está el ensayo que viene después, y ese cambio de postura es justamente donde más fallan los candidatos.</li>
<li><strong>Un plan que cruza los documentos.</strong> Es el verdadero criterio discriminante. Resumir el documento 1,
luego el 2 y luego el 3 no es una síntesis: es una serie de resúmenes. Hay que identificar los ejes comunes y hacer
dialogar las fuentes dentro de cada parte.</li>
</ul>

<p>A esto se suma la restricción de extensión: <strong>de 200 a 240 palabras</strong>, muy poco para la materia que hay
que tratar. Contar las palabras es parte del ejercicio, y pasarse claramente del límite superior se penaliza.</p>

<div class="note">
<p><strong>Por qué esta prueba es tan difícil de preparar solo.</strong> No puedes juzgar tu propia neutralidad, ni ver
que tu plan sigue los documentos en lugar de cruzarlos: son exactamente los defectos invisibles desde dentro. Es también
el nivel en el que un corrector humano se vuelve escaso y caro. La evaluación con IA de nuestra app califica tus
síntesis y ensayos según los criterios oficiales y te da una retroalimentación detallada, tantas veces como haga
falta.</p>
</div>

<h2 id="preparacion">Cómo prepararte</h2>
<ol>
<li><strong>Un simulacro completo desde el principio</strong> —un modelo de examen con el formato actual—. En el C1 como
en el C2, la duración es un factor en sí mismo: aguantar cuatro horas de producción intelectual densa se prepara tanto
física como intelectualmente.</li>
<li><strong>La síntesis, en serie.</strong> Es el ejercicio con mejor rendimiento: una técnica que se domina en una
decena de entrenamientos corregidos en serio, mientras que el nivel de lengua no se mueve en diez sesiones.</li>
<li><strong>El paso de la síntesis al ensayo.</strong> Entrena los dos ejercicios seguidos, en las condiciones reales de
las dos horas y media. Lo que hace perder puntos es el cambio de postura —neutralidad y después toma de posición—, no
cada ejercicio por separado.</li>
<li><strong>La hora de preparación del oral.</strong> Es vigilada y se trabaja como una prueba en sí misma: seleccionar,
jerarquizar, anotar palabras clave, no redactar un texto para leerlo después.</li>
<li><strong>Leer prensa de opinión con regularidad.</strong> Los temas son de orden general pero intelectualmente
exigentes: debates sociales, cuestiones culturales. Es la materia prima de las cuatro pruebas.</li>
</ol>

<h2 id="c1-o-c2">¿C1 o C2? Cuál elegir</h2>
<p>Para la gran mayoría de los recorridos, la respuesta es el C1. Ya abre las puertas universitarias y profesionales, y su
formato en cuatro pruebas permite la compensación.</p>

<p>El C2 se justifica en tres casos: la <strong>enseñanza del francés</strong>, la <strong>traducción</strong> y algunos
concursos o candidaturas en los que el nivel máximo es una señal en sí misma. Súmale el desafío personal, que es una
razón perfectamente válida —pero ten en cuenta que el paso del C1 al C2 no se juega en vocabulario adicional, sino en la
capacidad de producir un discurso largo, denso y estructurado a partir de fuentes—.</p>

<p>Si tu nivel real está entre el B2 y el C1, la estrategia más segura es <strong>asegurar primero el
<a href="/es/delf-b2/">B2</a></strong> y apuntar después al C1. Los dos diplomas son de por vida y se acumulan sin
ningún inconveniente.</p>

<h2 id="dispensa">Lo que el DALF te ahorra</h2>
<p>Es el argumento económico del diploma, y conviene que sea preciso más que general.</p>

<ul>
<li><strong>Universidad francesa.</strong> El DALF C1 exime de test lingüístico para la admisión. Es el uso más directo
y mejor establecido.</li>
<li><strong>Universidades españolas.</strong> Los diplomas DELF y DALF figuran en la tabla de equivalencias de la CRUE,
la Conferencia de Rectores, para la acreditación de idiomas.</li>
<li><strong>Nacionalidad francesa.</strong> Desde el 1 de enero de 2026, la solicitud de nacionalidad exige el B2. Un
DALF C1 o C2, de nivel superior, lo acredita <em>a fortiori</em>, y a diferencia de una constancia TCF IRN válida dos
años, un diploma no caduca nunca.</li>
<li><strong>Inmigración a Quebec.</strong> Quebec acepta los diplomas DELF y DALF en lugar del TCF Québec, pero con
condiciones: una nota mínima en comprensión oral y en expresión oral, y una antigüedad de menos de dos años. Aquí, el
carácter «de por vida» del diploma no cuenta.</li>
</ul>

<div class="note">
<p><strong>Cuidado con la generalización.</strong> «El DALF exime de todo» es cierto para la universidad francesa, con
matices en otros casos. Cada trámite publica su propia lista de justificantes aceptados, con sus propias condiciones de
nota y de vigencia: para Express Entry, por ejemplo, IRCC solo acepta el TCF Canada y el TEF Canada, y ni siquiera un
DALF C2 sirve. Verifica la lista de <em>tu</em> trámite antes de renunciar a presentar un test.</p>
</div>

<h2 id="fechas">Sesiones, precios e inscripción por país</h2>
<p>El DALF se presenta en los mismos centros y en las mismas sesiones que el DELF, y te inscribes directamente en el
centro. Esto mostraban los sitios web de los centros el 8 de octubre de 2026:</p>
""" + table("DALF C1 y C2 tout public: la próxima sesión y su precio en cada país, " + CAP_PAIS,
            ["País", "Próxima sesión (C1 · C2)", "Inscripción", "Precio (C1 · C2)"],
            [('<a href="/es/delf-espana/">España</a>', "10 · 11 de febrero de 2027", "del 1 de diciembre de 2026 al 9 de enero de 2027", "249 € · 259 € (tarifa 2027)"),
             ('<a href="/es/delf-mexico/">México</a>', "13 · 9 de noviembre de 2026", "del 5 al 23 de octubre de 2026", "3,500 · 4,000 pesos"),
             ('<a href="/es/delf-colombia/">Colombia</a>', "6 de noviembre de 2026 (C1 y C2)", "hasta el 9 de octubre de 2026", "591.000 · 643.000 pesos"),
             ('<a href="/es/delf-argentina/">Argentina</a>', "5 de diciembre de 2026 (C1 y C2)", "hasta el 5 de noviembre de 2026", "246 € · 277 € (445.260 · 501.370 pesos)"),
             ('<a href="/es/delf-chile/">Chile</a>', "ninguna abierta: las de 2026 fueron en mayo y septiembre", "calendario 2027 sin publicar", "167.000 · 187.000 pesos"),
             ('<a href="/es/delf-peru/">Perú</a>', "28 de noviembre de 2026", "hasta el 16 de octubre de 2026", "543 · 618 soles"),
             ('<a href="/es/delf-ecuador/">Ecuador</a>', "26 · 27 de noviembre, u 11 · 14 de diciembre de 2026", "hasta el 6 de noviembre en Quito; hasta el 13 de noviembre para diciembre", "240 dólares (C1 o C2)")]) + """
<p>Las reglas de inscripción, de reembolso y de entrega del diploma son las del DELF de cada país: las encontrarás en la
página de cada uno.</p>
""" + CHIPS + """
<p><strong>¿Y en Francia?</strong> El DALF se presenta en los mismos 143 centros que el DELF, el jueves de cada sesión
nacional —el C1 a las 9:00, el C2 a las 14:30—, diez veces al año, nunca en abril ni en septiembre. No hay tarifa
nacional: el C1 cuesta de 145 a 290 € según el centro (precios revisados el 17 de septiembre de 2026). Los resultados
llegan en 4 a 6 semanas.</p>
""",
    cta_h2="Entrena en condiciones reales",
    cta_p="""Simulacros cronometrados con el formato del DALF C1 y C2, calificados con los baremos oficiales, y corrección
con IA de la síntesis, del ensayo y de la expresión oral según los criterios oficiales, en la app «TCF DELF TEF: Tests
2026». La app está en español.""",
    faq=[("¿Qué es el DALF?", "El <em lang=\"fr\">Diplôme approfondi de langue française</em>, diploma oficial del Ministerio de Educación Nacional de Francia para los niveles C1 y C2 del Marco común europeo. Son dos diplomas independientes, expedidos por France Éducation international en los mismos centros y en las mismas sesiones que el DELF, y válidos de por vida."),
         ("¿Hay que tener el DELF B2 para presentar el DALF?", "No: cada diploma es independiente. Puedes inscribirte directamente en el C1, o incluso en el C2, sin haber presentado los niveles anteriores."),
         ("¿Cuánto dura el examen DALF C1?", "4 h 30 min de pruebas, más 1 hora de preparación vigilada antes del oral: 40 minutos de comprensión oral, 50 minutos de comprensión escrita, 2 h 30 min de expresión escrita y 30 minutos de expresión oral. Es el examen más largo de la familia DELF-DALF."),
         ("¿Qué nota se necesita para aprobar el DALF?", "50 sobre 100 en los dos casos. En el C1, las cuatro pruebas se califican sobre 25 y una nota inferior a 5 sobre 25 en una prueba es eliminatoria. En el C2, los dos ámbitos se califican sobre 50 y el umbral eliminatorio es de 10 sobre 50 por ámbito."),
         ("¿Qué es la síntesis de documentos del DALF C1?", "El primero de los dos ejercicios de la expresión escrita: reducir varios documentos a un texto único de 200 a 240 palabras, objetivo y totalmente reformulado. La gobiernan tres reglas: ninguna cita, ninguna opinión personal y un plan que cruza los documentos en lugar de resumirlos uno tras otro. Le sigue un ensayo argumentativo de 250 palabras como mínimo."),
         ("¿Hay que elegir una especialidad en el DALF?", "No, ya no: las antiguas opciones —letras y ciencias humanas, o ciencias— se eliminaron. Los temas siguen siendo de orden general pero intelectualmente exigentes: prensa de opinión, debates sociales, cuestiones culturales."),
         ("¿Cuándo es la próxima sesión del DALF C1?", "Depende del país. Según los sitios web de los centros el 8 de octubre de 2026: el 6 de noviembre en Colombia, el 13 de noviembre en México, el 26 de noviembre o el 11 de diciembre en Ecuador, el 28 de noviembre en Perú, el 5 de diciembre en Argentina y, en España, el 10 de febrero de 2027, con inscripción del 1 de diciembre de 2026 al 9 de enero de 2027. En Chile, las sesiones de 2026 ya habían pasado."),
         ("¿Cuánto cuesta el DALF C1?", "Cada país fija su tarifa: 249 € en España (2027), 3,500 pesos en México, 591.000 pesos en Colombia, 167.000 pesos en Chile, 543 soles en Perú, 240 dólares en Ecuador y 246 € (445.260 pesos) en Argentina. En Francia no hay tarifa nacional: de 145 a 290 € según el centro."),
         ("¿DALF C1 o DELF B2 para entrar a la universidad?", "El B2 basta para la mayoría de las carreras; el C1 lo piden algunas carreras exigentes y siempre marca la diferencia en la selección. Si tu nivel real está entre los dos, asegura primero el B2 y apunta después al C1: los dos diplomas son de por vida y se acumulan sin problema."),
         ("¿Vale la pena el C2?", "Para la mayoría de los recorridos, no: el C1 ya abre todas las puertas universitarias y profesionales. El C2 se justifica para la enseñanza del francés, la traducción, algunos concursos o como desafío personal. Su formato es muy distinto del C1, con dos pruebas integradas en lugar de cuatro."),
         ("¿El DALF exime de presentar un TCF o un TEF?", "Para entrar a las universidades francesas, el DALF C1 exime de test lingüístico. Para los trámites de inmigración es más matizado: un DALF acredita a fortiori el B2 exigido para la nacionalidad francesa, y Quebec acepta los diplomas DELF y DALF en lugar del TCF Québec, con condiciones de nota y de vigencia. Para Express Entry, en cambio, IRCC solo acepta el TCF Canada y el TEF Canada. Verifica siempre la lista de justificantes de tu trámite.")],
    also=[("/es/delf-b2/", "Examen DELF B2", "El nivel anterior: estructura, puntuación y fechas por país."),
          ("/es/certificado-de-frances/", "¿Qué certificado de francés elegir?", "DELF, DALF, TCF o TEF: lo que prueba cada uno y quién lo acepta."),
          ("/es/delf-espana/", "DELF y DALF en España", "El calendario nacional de 2027 y una tarifa única.")],
    sources="""<strong>Los formatos cambian.</strong> La descripción del examen está actualizada al 7 de agosto de 2026; las
sesiones y los precios por país vienen de nuestra revisión de los sitios web de los centros del 8 de octubre de
2026. Las estructuras de las pruebas y los requisitos de las instituciones cambian con regularidad: verifica el formato
en <a href="https://www.france-education-international.fr/diplome/dalf" rel="noopener">france-education-international.fr</a>
y las condiciones de admisión con la institución o la administración correspondiente antes de inscribirte.""",
))


# ===========================================================================
# DELF B2 — EJEMPLOS: de /blog/exercices-delf-b2/ (+ /blog/production-ecrite-delf-b2/). Ejercicios en francés.
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/exercices-delf-b2/", lang="es", variant="es-419", slug="delf-b2-ejemplos", accent="accent-delf",
    crumbs=[INICIO], crumb="Ejemplos del DELF B2",
    title="Examen DELF B2: ejemplos resueltos de las 4 pruebas",
    desc="Ejemplos del examen DELF B2 con el formato reformado: un ejercicio resuelto por prueba, lo que espera el corrector y el método para la expresión escrita.",
    h1="Examen DELF B2: ejemplos de las cuatro pruebas, resueltos",
    intro="""Cuatro pruebas calificadas sobre 25, un total sobre <strong>100</strong>, el aprobado con <strong>50/100</strong>
—y una nota inferior a <strong>5/25</strong> en una sola prueba que te elimina, sea cual sea tu promedio—. Desde la
reforma, las dos comprensiones son <strong>100 % de opción múltiple</strong>. Aquí tienes un ejercicio resuelto por
prueba, con los documentos y las consignas en francés, como el día del examen, y después el método de la expresión
escrita: 250 palabras en 60 minutos, la prueba que más decide.""",
    facts=["<strong>4 pruebas sobre 25</strong> · total sobre <strong>100</strong> · aprobado con <strong>50/100</strong>.",
           "⚠️ <strong>Menos de 5/25</strong> en una sola prueba = <strong>eliminatoria</strong>.",
           "<strong>Comprensión oral 30 min · comprensión escrita 60 min · expresión escrita 60 min · expresión oral 20 min</strong> (+ 30 min de preparación).",
           "Desde la reforma: comprensiones <strong>100 % de opción múltiple</strong>, entrevista dirigida <strong>eliminada</strong> del oral.",
           "⚠️ En comprensión oral, los 2 primeros ejercicios se escuchan <strong>2 veces</strong>; el 3.º, una sola.",
           "Expresión escrita: <strong>250 palabras como mínimo</strong>, y el corrector evalúa la <strong>construcción</strong>, no tu opinión."],
    toc=[("estructura", "La estructura de las cuatro pruebas"), ("ejercicios", "Un ejercicio resuelto por prueba"),
         ("eliminatoria", "La nota eliminatoria cambia la estrategia"), ("metodo", "El método"),
         ("evalua", "Expresión escrita: lo que evalúa el corrector"), ("plan", "El plan que funciona"),
         ("generos", "Los tres géneros, y lo que exigen"), ("errores", "Los cinco errores que más cuestan"),
         ("tiempo", "Cómo repartir los 60 minutos")],
    body="""
<h2 id="estructura">La estructura de las cuatro pruebas</h2>
""" + table("DELF B2, formato surgido de la reforma de 2020, generalizado desde septiembre de 2024. Fuente: France Éducation international.",
            ["Prueba", "Contenido", "Duración", "Nota"],
            [("Comprensión oral", "3 ejercicios / 5 documentos de audio", "30 min", "/25"),
             ("Comprensión escrita", "3 ejercicios / 5 documentos escritos", "60 min", "/25"),
             ("Expresión escrita", "1 ejercicio, 250 palabras como mínimo", "60 min", "/25"),
             ("Expresión oral", "Monólogo y debate", "20 min <em>(+ 30 min de preparación)</em>", "/25")], wide=False) + """

<div class="note">
<p><strong>Cuidado con los modelos de examen desactualizados.</strong> Si un documento menciona una entrevista dirigida
en el oral o preguntas abiertas en comprensión, describe un examen que ya no existe. Gran parte de los recursos en
internet es anterior a la reforma.</p>
</div>

<h2 id="ejercicios">Un ejercicio resuelto por prueba</h2>
<p>Los documentos, las preguntas y las consignas están en francés, como el día del examen; las respuestas y las
explicaciones, en español.</p>
""" + exo("es", 1, "B2 — comprensión oral", "Entrevista",
          "« <strong>Journaliste :</strong> Vous êtes spécialiste en santé publique. La question de la santé "
          "mentale des jeunes est devenue un sujet majeur en France. Pouvez-vous nous en dire plus ?<br>"
          "<strong>Docteur Martin :</strong> Oui, effectivement, nous observons une augmentation très "
          "préoccupante des troubles psychiques chez les 15-25 ans depuis la pandémie de Covid-19. Les "
          "consultations pour anxiété et dépression ont augmenté de 40 % entre 2019 et 2024 dans cette "
          "tranche d'âge. Les tentatives de suicide chez les adolescentes ont doublé. »",
          "Quelle augmentation note-t-on pour les troubles ?",
          ["Une hausse de 20 % en cinq ans", "Une hausse de 80 % en cinq ans",
           "Une hausse de 40 % entre 2019 et 2024", "Une hausse de 60 % entre 2019 et 2024"],
          'C — <span lang="fr">Une hausse de 40 % entre 2019 et 2024</span>',
          "pregunta de localización, pero con dos cifras cercanas en el documento: el 40 % se refiere a las consultas, y "
          "el <em lang=\"fr\">ont doublé</em>, a los intentos de suicidio. <strong>Verifica siempre a qué se refiere la "
          "cifra</strong> antes de marcar: es el mecanismo de distracción más común.",
          audio="delf_co_001.m4a", duree="1 min 46 s", ecoutes=2
          ) + exo("es", 2, "B2 — comprensión escrita", "Documento — artículo de prensa:",
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
          'D — <span lang="fr">Montrer les contradictions sociales de la transition</span>',
          "la pregunta trata de la <strong>intención del autor</strong>, no del contenido. El giro está en el "
          "<em lang=\"fr\">Mais</em>: el artículo enuncia los objetivos para exponer mejor la distancia con la realidad. "
          "La opción B es el contrasentido esperado: un lector que lee rápido se queda con los <em lang=\"fr\">objectifs "
          "ambitieux</em> y concluye que el artículo los celebra."
          ) + sujet("es", "Expresión escrita", "60 minutos · 250 palabras como mínimo · calificada sobre 25",
          "Vous habitez dans une ville où la mairie a décidé de supprimer plusieurs lignes de bus pour des "
          "raisons budgétaires. En tant que président(e) d'une association de quartier, vous écrivez au "
          "maire pour protester contre cette décision. Vous expliquez les conséquences pour les habitants "
          "et vous proposez des solutions alternatives.",
          "<strong>Aquí se suman tres exigencias</strong>: el género (carta formal, con fórmula de saludo, asunto y fórmula "
          "de despedida), el papel (escribes en calidad de presidente o presidenta de la asociación, no a título personal) y las dos "
          "acciones pedidas (explicar las consecuencias <em>y</em> proponer alternativas). Omitir las propuestas es el "
          "error más frecuente: se protesta, pero no se propone ninguna alternativa. 250 palabras es un mínimo."
          ) + sujet("es", "Expresión oral", "30 minutos de preparación · 20 minutos de prueba · calificada sobre 25",
          "Vous dégagerez le problème soulevé par le document ci-dessous. Vous présenterez votre opinion sur "
          "le sujet de manière argumentée, puis vous la défendrez face à l'examinateur lors d'un débat.",
          "La prueba empieza <strong>directamente con el monólogo</strong>: la reforma eliminó la entrevista dirigida, que "
          "permitía relajarse. Los 30 minutos de preparación sirven para construir un plan y anotar palabras clave, no "
          "para redactar: un candidato que lee sus notas se detecta enseguida. En la segunda parte, <strong>el jurado no "
          "está de acuerdo contigo, y es a propósito</strong>: su papel es poner a prueba tu capacidad de sostener una "
          "postura matizándola. Abandonar tu tesis a la primera objeción cuesta puntos."
          ) + """

<h2 id="eliminatoria">La nota eliminatoria cambia la estrategia</h2>
""" + table("Los dos umbrales del DELF B2.", ["Regla", "Umbral", "Efecto"],
            [("Promedio general", "<strong>50/100</strong>", "Por debajo, no apruebas"),
             ("Nota mínima por prueba", "<strong>5/25</strong>", "Por debajo en <em>una sola</em> prueba, no apruebas, aunque tengas 60/100")],
            wide=False) + """

<p>La consecuencia va contra la intuición: <strong>una competencia muy débil cuesta más de lo que aporta una competencia
fuerte</strong>. Un candidato con 20/25 en comprensión escrita y 4/25 en expresión oral no aprueba, aunque su promedio
supere el umbral. Tu primer trabajo de preparación no es, entonces, progresar donde ya eres bueno, sino <strong>sacar tu
prueba más débil de la zona eliminatoria</strong>.</p>

<h2 id="metodo">El método</h2>
<ol>
<li><strong>Un simulacro completo desde el principio</strong>, calificado con los baremos oficiales, para identificar la
prueba que puede eliminarte.</li>
<li><strong>Saca esa prueba de la zona roja</strong> antes que cualquier otra cosa.</li>
<li><strong>Trabaja la expresión escrita por la estructura</strong>, no por el vocabulario: la mayoría de los puntos
perdidos viene del plan, del género y de la consigna.</li>
<li><strong>Simula el oral en condiciones reales</strong>, con los 30 minutos de preparación y una contradicción asumida
en la segunda parte.</li>
<li><strong>Cuidado con los recursos desactualizados</strong>: verifica siempre la fecha de aquello con lo que
entrenas.</li>
</ol>

<h2 id="evalua">Expresión escrita: lo que evalúa el corrector</h2>
<p><strong>Un ejercicio, 60 minutos, 250 palabras como mínimo.</strong> La expresión escrita es la tercera prueba
colectiva del DELF B2, justo después de las dos comprensiones: llegas a ella tras una hora y media de examen, un detalle
que cuenta para administrar la energía. Y desde la reforma es <strong>la única prueba en la que redactas</strong> antes
del oral: todo lo que tiene que ver con la expresión escrita se juega ahí, en un solo texto.</p>

<p>Es el malentendido central. El tema te pide una <strong>toma de posición personal</strong>, y muchos candidatos
concluyen que se juzga la pertinencia de su opinión. No es así: <strong>tu opinión no es ni buena ni mala</strong>. Lo
que se evalúa es la manera en que la construyes. En concreto, cinco dimensiones:</p>

<ul>
<li><strong>La adecuación a la consigna y al género.</strong> Una carta formal sin fórmula de saludo ni estructura de
carta pierde puntos antes incluso de que se evalúe la lengua. Es el punto más fácil de asegurar, y el más
descuidado.</li>
<li><strong>La estructura argumentativa.</strong> Una postura clara, argumentos jerarquizados y, sobre todo, la
<strong>objeción contraria tomada en cuenta</strong>. Es el marcador del nivel B2: en el B1 das tu opinión; en el B2 la
defiendes frente a una objeción.</li>
<li><strong>Los conectores lógicos.</strong> La señal más visible del nivel, y la más rentable de trabajar de forma
mecánica: unas pocas horas bastan para instalar un repertorio sólido.</li>
<li><strong>El registro.</strong> El deslizamiento inadvertido hacia lo coloquial es una pérdida de puntos frecuente
entre los candidatos que hablan bien francés en el día a día.</li>
<li><strong>La extensión.</strong> 250 palabras como mínimo. Por debajo, la adecuación a la consigna falla, sea cual sea
la calidad de la lengua.</li>
</ul>

<div class="note">
<p><strong>Ninguna de estas cinco dimensiones es un problema de vocabulario.</strong> Es la buena noticia de esta
prueba: la mayoría de los puntos perdidos viene del plan, del género y de la consigna, es decir, de cosas que se
corrigen en unas pocas sesiones, no en unos meses.</p>
</div>

<h2 id="plan">El plan que funciona</h2>
<p>No hay un plan oficial obligatorio. Pero una estructura cumple todas las expectativas del nivel B2 y te evita pensar
en la organización el día del examen.</p>

<ol>
<li><strong>Introducción (30-40 palabras).</strong> Reformulas lo que está en juego y anuncias tu postura. Sin rodeos:
en el B2, el corrector debe saber desde la primera frase adónde vas.</li>
<li><strong>Primer argumento (60-70 palabras).</strong> Tu razón más fuerte, ilustrada con un ejemplo concreto. Un
argumento sin ejemplo se queda en afirmación.</li>
<li><strong>Segundo argumento (60-70 palabras).</strong> Una razón de naturaleza distinta a la primera: si la primera es
económica, toma un ángulo social o práctico. Dos argumentos del mismo tipo cuentan como uno.</li>
<li><strong>Concesión y refutación (50-60 palabras).</strong> <strong>Es el párrafo que marca la diferencia.</strong>
Reconoces la fuerza de la objeción contraria y luego explicas por qué no cambia tu postura. Muchos textos lo omiten por
completo, y se quedan estancados.</li>
<li><strong>Conclusión (30-40 palabras).</strong> Recuerdas tu postura y abres una nueva perspectiva, sin introducir ninguna idea
nueva.</li>
</ol>

<p>Total: unas 250 a 280 palabras. El plan produce mecánicamente la extensión esperada, lo que resuelve la cuestión del
conteo.</p>

<h2 id="generos">Los tres géneros, y lo que exigen</h2>
""" + table("Lo que cada género exige además de la argumentación.", ["Género", "Lo que exige"],
            [("<strong>Contribución a un debate</strong><br><em>foro, cartas de los lectores</em>", "Dirigirse a una comunidad, situar tu intervención en un intercambio en curso"),
             ("<strong>Carta formal</strong>", "Fórmula de saludo, asunto, estructura de carta, fórmula de despedida y registro formal de principio a fin"),
             ("<strong>Artículo crítico</strong>", "Un título, una entrada que atrape, un tono periodístico y una postura asumida")],
            wide=False) + """

<p>La carta formal es aquella en la que más puntos se pierden gratuitamente, porque el corrector puede verificar sus
convenciones de forma mecánica. Apréndelas una vez: fórmula de saludo, asunto, cuerpo estructurado, fórmula de
despedida. Son conocimientos para toda la vida, y aparecen en casi todos los exámenes de francés.</p>

<h2 id="errores">Los cinco errores que más cuestan</h2>
<ol>
<li><strong>Escribir menos de 250 palabras.</strong> La sanción recae en la adecuación a la consigna, independientemente
de la calidad. Cuenta tus palabras de verdad: el cálculo a ojo casi siempre es optimista.</li>
<li><strong>Omitir la concesión.</strong> Sin la objeción contraria, tu texto se queda en una opinión yuxtapuesta, no en
una argumentación de nivel B2.</li>
<li><strong>Ignorar el género pedido.</strong> Un excelente texto argumentativo que debía ser una carta formal pierde
puntos estructurales irrecuperables.</li>
<li><strong>Acumular argumentos sin articularlos.</strong> Tres ideas correctas puestas una al lado de la otra valen menos
que dos ideas unidas por una progresión explícita.</li>
<li><strong>Descuidar la relectura.</strong> Las concordancias, los tiempos verbales y la puntuación se corrigen en cinco
minutos, y salen caros si se te escapan.</li>
</ol>

<h2 id="tiempo">Cómo repartir los 60 minutos</h2>
""" + table("Un reparto que deja tiempo para una relectura de verdad.", ["Tiempo", "Lo que haces"],
            [("<strong>0–10 min</strong>", "Analizar la consigna, identificar el género, fijar el plan y los dos argumentos con sus ejemplos"),
             ("<strong>10–45 min</strong>", "Redactar de un tirón, sin volver atrás"),
             ("<strong>45–52 min</strong>", "Contar las palabras, verificar que la concesión está y que se respeta el género"),
             ("<strong>52–60 min</strong>", "Releer la lengua: concordancias, tiempos, puntuación, registro")],
            wide=False) + """

<p>Los diez primeros minutos van contra la intuición: da la impresión de perder el tiempo. Y sin embargo es el único
momento en que todavía puedes cambiar la estructura de tu texto sin reescribirlo todo. Un plan fijado en diez minutos
ahorra mucho más que diez minutos de redacción.</p>

<div class="note">
<p><strong>Por qué esta prueba es difícil de preparar solo.</strong> No puedes juzgar si tu concesión es real o solo
anunciada, ni si se te coló el registro coloquial: son justamente los defectos invisibles desde dentro. Y la diferencia entre 9 y
13 sobre 25, que muchas veces decide el aprobado, no se ve al releer. Es lo que resuelve una corrección según los
criterios oficiales.</p>
</div>
""",
    cta_h2="Primero, salir de la zona eliminatoria",
    cta_p="""Simulacros con el formato reformado del DELF B2, calificados con el baremo oficial sobre 25 por prueba y con
alerta de nota eliminatoria, y corrección con IA de la expresión escrita y oral según los criterios oficiales, en la app
«TCF DELF TEF: Tests 2026». La app está en español.""",
    faq=[("¿Qué nota se necesita para aprobar el DELF B2?", "50 sobre 100. Las cuatro pruebas se califican sobre 25 cada una. Cuidado con la regla que deja sin diploma a candidatos cuyo promedio alcanzaba: una nota inferior a 5 sobre 25 en una sola prueba es eliminatoria, sea cual sea el total."),
         ("¿Las comprensiones del DELF B2 son de opción múltiple?", "Sí, al 100 % desde la reforma. Las preguntas abiertas y los verdadero/falso con justificación desaparecieron de las dos comprensiones. Ya no redactas nada en esas pruebas: cambia la gestión del tiempo, pero también desaparece la posibilidad de ganar algunos puntos con una justificación parcialmente correcta."),
         ("¿Cuántas veces se escuchan los audios del DELF B2?", "Depende del ejercicio. Los dos primeros, sobre documentos de radio largos, se escuchan dos veces. El tercero, que encadena tres documentos cortos, se escucha una sola vez. Esta asimetría sorprende justo cuando la concentración ya está gastada."),
         ("¿Cuántas palabras hay que escribir en la expresión escrita del DELF B2?", "250 palabras como mínimo, en un solo ejercicio, en 60 minutos. Es un mínimo y no una meta: escribir menos hace perder puntos en la adecuación a la consigna, sea cual sea la calidad de la lengua. Un plan en cinco partes produce mecánicamente de 250 a 280 palabras."),
         ("¿Qué tipos de temas salen en la expresión escrita?", "Tres géneros: una contribución a un debate (foro, cartas de los lectores), una carta formal o un artículo crítico. En todos los casos, el tema pide una toma de posición personal argumentada. La carta formal es aquella en la que más puntos se pierden gratuitamente, por no respetar sus convenciones."),
         ("¿El corrector juzga mi opinión?", "No. Tu opinión no es ni buena ni mala: lo que se evalúa es la manera en que la construyes —adecuación a la consigna y al género, estructura argumentativa, conectores lógicos, registro y extensión—. Ninguna de estas dimensiones es un problema de vocabulario."),
         ("¿Qué distingue el B2 del B1 en la expresión escrita?", "Tener en cuenta la objeción contraria. En el B1 das tu opinión; en el B2 la defiendes frente a una objeción que primero reconociste. El párrafo de concesión y refutación es el que más a menudo marca la diferencia, y muchos textos lo omiten por completo."),
         ("¿Cómo repartir los 60 minutos de la expresión escrita?", "Unos 10 minutos para analizar la consigna y fijar el plan, 35 minutos para redactar de un tirón, 7 minutos para verificar la extensión, la concesión y el género, y 8 minutos de relectura de la lengua. Los 10 primeros minutos parecen perdidos: son, sin embargo, el único momento en que todavía puedes cambiar la estructura sin reescribirlo todo."),
         ("¿Todavía existe la entrevista dirigida en el oral del DELF B2?", "No, la reforma la eliminó. La prueba empieza ahora directamente con el monólogo, y después viene el debate con los examinadores. El calentamiento que permitía relajarse ya no existe en el B2; en cambio, sigue existiendo en el DELF B1."),
         ("¿El jurado tiene que estar de acuerdo conmigo?", "No, y es a propósito. En la segunda parte del oral, el jurado te contradice para poner a prueba tu capacidad de sostener una postura, matizar y conceder sin ceder. Los candidatos que abandonan su tesis a la primera objeción pierden puntos en la competencia evaluada.")],
    also=[("/es/delf-b2/", "Examen DELF B2: estructura, puntuación y fechas", "El formato reformado, los dos umbrales y las fechas en cada país."),
          ("/es/dalf-c1/", "Examen DALF C1 y C2", "El nivel siguiente: la síntesis de documentos de 200 a 240 palabras."),
          ("/es/certificado-de-frances/", "¿Qué certificado de francés elegir?", "Lo que prueba el DELF, y los trámites en los que no basta.")],
    sources="""<strong>Los formatos cambian.</strong> Esta página está actualizada al 7 de agosto de 2026 y describe el formato
surgido de la reforma de 2020, generalizado desde septiembre de 2024. Los ejercicios presentados son contenidos originales
de nuestra app. Cuidado con los modelos de examen y los tutoriales anteriores, que describen un examen distinto. Verifica
el formato vigente en
<a href="https://www.france-education-international.fr/diplome/delf-tout-public" rel="noopener">france-education-international.fr</a>
antes de tu sesión.""",
))


# ===========================================================================
# ¿QUÉ CERTIFICADO DE FRANCÉS? — de /blog/diplome-ou-test-delf-tcf/
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/diplome-ou-test-delf-tcf/", lang="es", variant="es-419", slug="certificado-de-frances", accent="accent-delf",
    crumbs=[INICIO], crumb="Certificado de francés",
    title="Certificado de francés B2 o C1: ¿DELF, DALF, TCF o TEF?",
    desc="Diferencia entre DELF, DALF, TCF y TEF: diploma de por vida o test válido dos años, quién acepta cada uno (Express Entry, Quebec) y cuál elegir.",
    h1="¿Qué certificado de francés elegir? DELF, DALF, TCF o TEF: diploma o test",
    intro="""No son dos versiones de lo mismo. El <strong>DELF</strong> y el <strong>DALF</strong> son
<strong>diplomas</strong>: se aprueban o no, y son válidos <strong>de por vida</strong>. El <strong>TCF</strong> y el
<strong>TEF</strong> son <strong>tests de nivel</strong>: no se aprueban ni se reprueban, te sitúan en una escala, y su
constancia vale <strong>dos años</strong>. La elección depende menos de tu nivel que de lo que exige tu trámite y del
tiempo que va a tomar: para emigrar a Canadá con Express Entry, por ejemplo, solo sirven el TCF Canada y el TEF
Canada.""",
    facts=["<strong>Diplomas</strong> (DELF, DALF): válidos <strong>de por vida</strong>, con nota eliminatoria: se aprueban o no.",
           "<strong>Tests</strong> (TCF, TEF): constancia válida <strong>2 años</strong>, sin umbral: no se aprueban ni se reprueban.",
           "⚠️ <strong>Escuchas</strong>: 2 veces en el DELF hasta el B1, <strong>1 sola</strong> en el TCF y el TEF.",
           "⚠️ Para <strong>Express Entry</strong>, un DELF no vale nada: solo se aceptan el TCF Canada y el TEF Canada.",
           "⚠️ En <strong>Quebec</strong>, se acepta un DELF, pero debe tener <strong>menos de dos años</strong>: lo de «de por vida» no cuenta.",
           "Duración: <strong>1 h 30 min</strong> para un test IRN contra <strong>2 h 50 min</strong> para un DELF B2."],
    toc=[("naturaleza", "Dos cosas distintas: el diploma se aprueba, el test te sitúa"),
         ("vigencia", "Dos años contra toda la vida"), ("escuchas", "La diferencia de formato que nadie menciona"),
         ("reconocimiento", "Quién acepta qué"), ("quebec", "El caso en que «de por vida» no sirve de nada"),
         ("elegir", "Cómo elegir según tu situación"), ("donde", "Dónde presentarlos en España y América Latina")],
    body="""
<h2 id="naturaleza">Dos cosas distintas: el diploma se aprueba, el test te sitúa</h2>

<p>Es la distinción fundamental, y lo cambia todo.</p>

<p>El <a href="/es/delf-b2/">DELF</a> y el <a href="/es/dalf-c1/">DALF</a> son <strong>exámenes</strong>, expedidos por el
Ministerio de Educación Nacional de Francia. Cuatro pruebas calificadas sobre 25, un total sobre 100, el aprobado con
<strong>50/100</strong> —y una nota inferior a <strong>5/25</strong> en una sola prueba te elimina, sea cual sea tu
promedio—. Obtienes el diploma o no lo obtienes.</p>

<p>El TCF y el TEF son <strong>tests de nivel</strong>. No hay umbral de aprobación ni nota eliminatoria: obtienes una
puntuación por prueba, y es la institución que recibe tu expediente —una prefectura en Francia, IRCC, una universidad—
la que decide si esa puntuación basta. Un TCF no se «reprueba»: se obtiene un nivel más bajo del esperado.</p>

<div class="note">
<p><strong>Una consecuencia estratégica opuesta.</strong> En el DELF, una competencia muy débil te cuesta más de lo que
te aporta una competencia fuerte: primero hay que sacar tu prueba más débil de la zona eliminatoria, y la compensación
hará el resto. En el TCF y en el TEF <em>no hay</em> compensación: la administración lee cada prueba por separado, y tu
expediente vale tu puntuación más baja. En los dos casos manda tu punto débil, pero por razones distintas.</p>
</div>

<h2 id="vigencia">Dos años contra toda la vida</h2>

<p>Es el argumento que más se escucha, y es cierto: un diploma <strong>no caduca nunca</strong>; una constancia de test
vale <strong>dos años</strong>. Pero hay que manejarlo con precisión, porque no se aplica igual en todas partes.</p>
""" + table("Lo que obtienes, según la familia.", ["", "DELF · DALF", "TCF · TEF"],
            [("Naturaleza", "Diploma oficial del Estado francés", "Constancia de nivel"),
             ("Vigencia", "<strong>de por vida</strong>", "<strong>2 años</strong>"),
             ("¿Hay aprobado?", "sí: 50/100, eliminatoria por debajo de 5/25", "no: una puntuación, no un umbral"),
             ("Compensación entre pruebas", "sí, por encima del mínimo", "<strong>ninguna</strong>"),
             ("Duración del examen", "2 h 10 min (B1) a 4 h 30 min (DALF C1)", "1 h 30 min (IRN) a 2 h 55 min (TEF Canada)")], wide=False) + """

<p>La regla práctica se desprende sola: <strong>si vas a presentar la solicitud pronto, el test basta</strong> y te cuesta menos
tiempo. <strong>Si tu recorrido va a extenderse</strong> —y es frecuente entre una tarjeta de residente y una solicitud
de nacionalidad en Francia, o entre una candidatura y una inscripción universitaria—, el diploma te evita tener que
volver a presentar y pagar un test vencido en el peor momento.</p>

<h2 id="escuchas">La diferencia de formato que nadie menciona</h2>

<div class="note">
<p><strong>En el DELF, los documentos de los niveles A1 a B1 se escuchan dos veces. En el TCF y en el TEF hay una sola
escucha, sin vuelta atrás.</strong> Los dos organismos lo dicen explícitamente, y vale para las nueve versiones, sin
excepción.</p>
</div>

<p>Es la diferencia práctica más subestimada, y atrapa a muchos candidatos que se entrenaron con recursos del DELF —mucho
más numerosos en internet— y se presentan a un TCF. Perder el hilo en una pregunta significa perderla para siempre: lo
que importa ya no es entender, sino pasar de inmediato a la siguiente sin intentar reconstruir lo que se te escapó.</p>

<p>En el <a href="/es/delf-b2/">DELF B2</a>, el formato es además mixto desde la reforma: los dos primeros ejercicios de
comprensión oral se escuchan dos veces; el tercero, una sola. Esta asimetría sorprende justo cuando la concentración ya
está gastada.</p>

<h2 id="reconocimiento">Quién acepta qué</h2>

<p>Aquí es donde la elección se decide de verdad, y la respuesta no es simétrica.</p>
""" + table("Reconocimiento según el trámite. Fuentes: orden del 22 de diciembre de 2025 para Francia, IRCC para el nivel federal canadiense y Ministerio de Inmigración, Francización e Integración para Quebec, consultados en julio de 2026; tabla de equivalencias de la CRUE para España, consultada el 8 de octubre de 2026.",
            ["Trámite", "DELF · DALF", "TCF · TEF"],
            [("Nacionalidad francesa", "sí <em>(B2 exigido)</em>", "sí <em>(versiones IRN)</em>"),
             ("Tarjeta de residente en Francia", "sí <em>(B1 exigido)</em>", "sí <em>(versiones IRN)</em>"),
             ("<strong>Express Entry (federal, Canadá)</strong>", "<strong>no</strong>", "sí: TCF Canada y TEF Canada <strong>solamente</strong>"),
             ("Ciudadanía canadiense", "no citado <em>(cuestionario de IRCC, 8 de octubre de 2026)</em>", "sí <em>(TCF Canada, TEF Canada)</em>"),
             ("Programas de Quebec", "sí, <strong>con condiciones</strong>", "sí"),
             ("Universidad francesa", "sí: el DALF C1 exime de test", "sí <em>(TCF tout public)</em>"),
             ("Universidades españolas (CRUE)", "sí", "TCF tout public, por tramos de puntuación")]) + """

<div class="note">
<p><strong>El caso que por sí solo lo decide todo: la inmigración económica a Canadá.</strong> Para Express Entry, IRCC solo
acepta <strong>dos tests</strong>: el TCF Canada y el TEF Canada. Ni el DELF, ni el DALF, ni el TCF tout public, ni el
TEFAQ figuran en la lista. Un DALF C2, el diploma de francés más alto que existe, no vale nada para un perfil de Express
Entry. Si tu proyecto es la inmigración federal a Canadá, la pregunta «¿diploma o test?» ni se plantea.</p>
</div>

<p>Fíjate en el matiz de la <strong>ciudadanía</strong> canadiense, que a menudo se confunde con la inmigración: el
cuestionario de IRCC, consultado el 8 de octubre de 2026, menciona el TEF Canada y el TCF Canada; guías anteriores
nombraban más (DALF, DELF, TCFQ, TEFAQ, TEF IRN). Verifica la lista en el sitio de IRCC en el momento de tu
solicitud.</p>

<h2 id="quebec">El caso en que «de por vida» no sirve de nada</h2>

<p>Este es el matiz que casi ningún comparativo señala. Quebec acepta los diplomas DELF y DALF en lugar del TCF Québec,
pero <strong>con condiciones</strong>: una nota mínima en comprensión oral y en expresión oral, <em>y</em> una
antigüedad de <strong>menos de dos años</strong>.</p>

<p>Dicho de otro modo: en Quebec, tu DELF B2 obtenido hace cinco años no te exime de nada. La ventaja central del diploma
—su permanencia— queda neutralizada por una condición de vigencia. Es exactamente lo contrario de la lógica francesa,
donde un diploma, precisamente porque no caduca, es el justificante más seguro para un expediente que se alarga.</p>

<p>La lección general: <strong>«de por vida» es una propiedad del diploma, no una garantía de aceptación.</strong> Cada
trámite publica su propia lista de justificantes, con sus propias condiciones de nota y de vigencia. Verifica la de
<em>tu</em> trámite antes de apostar por la permanencia.</p>

<h2 id="elegir">Cómo elegir según tu situación</h2>

<ul>
<li><strong>Inmigración económica a Canadá</strong> → un test, y no cualquiera: TCF Canada o TEF Canada. Ninguna
alternativa.</li>
<li><strong>Nacionalidad o permiso de residencia en Francia, si vas a presentar la solicitud pronto</strong> → un test IRN:
más corto y pensado para esos trámites.</li>
<li><strong>Nacionalidad o permiso de residencia en Francia, con un recorrido de varios años</strong> → un diploma. Un
<a href="/es/delf-b1/">DELF B1</a> o un <a href="/es/delf-b2/">B2</a> no caducará entre dos etapas de tu
expediente.</li>
<li><strong>Universidad francesa</strong> → los dos sirven, pero el <a href="/es/dalf-c1/">DALF C1</a> exime de test
lingüístico y pesa más en la selección.</li>
<li><strong>Proyecto en Quebec</strong> → un test, salvo si tienes un DELF o un DALF de menos de dos años con las notas
exigidas.</li>
<li><strong>Todavía no lo sabes</strong> → el diploma es la opción más robusta, porque no caduca mientras tu proyecto se
define.</li>
</ul>

<h2 id="donde">Dónde presentarlos en España y América Latina</h2>

<p>El DELF, el DALF y el TCF se presentan en los centros autorizados por France Éducation international: Alianzas
Francesas, Institutos Franceses, universidades. En Colombia, Argentina, Perú y Ecuador, el DELF y el DALF solo se
presentan en las Alianzas Francesas, y el diploma es el mismo que en Francia, sea cual sea el país. Atención: un centro
autorizado para el TCF no ofrece necesariamente la versión Canada.</p>
""" + table("El TCF Canada y el DELF-DALF en siete países, según los sitios web de los centros el 8 de octubre de 2026. Precios en moneda local, para un candidato libre.",
            ["País", "TCF Canada", "DELF · DALF"],
            [("<strong>España</strong>", '<a href="/es/tcf-canada-espana/">11 centros de 14, de 275 a 287 €</a>', '<a href="/es/delf-espana/">32 centros, calendario nacional, B2 192 € en 2027</a>'),
             ("<strong>México</strong>", '<a href="/es/tcf-canada-mexico/">5 centros de 11, de 4,800 a 6,500 pesos</a>', '<a href="/es/delf-mexico/">71 centros, B2 2,500 pesos</a>'),
             ("<strong>Colombia</strong>", '<a href="/es/tcf-canada-colombia/">las 7 Alianzas Francesas, desde 1.050.000 pesos</a>', '<a href="/es/delf-colombia/">15 Alianzas Francesas, B2 490.000 pesos</a>'),
             ("<strong>Argentina</strong>", '<a href="/es/tcf-canada-argentina/">4 centros, precio a solicitud</a>', '<a href="/es/delf-argentina/">28 Alianzas Francesas, B2 163 € (295.030 pesos)</a>'),
             ("<strong>Chile</strong>", '<a href="/es/tcf-canada-chile/">2 centros, 299.000 pesos</a>', '<a href="/es/delf-chile/">4 centros, B2 137.000 pesos</a>'),
             ("<strong>Perú</strong>", '<a href="/es/tcf-canada-peru/">1 centro en Lima, 1,240 soles</a>', '<a href="/es/delf-peru/">6 Alianzas Francesas, B2 461 soles</a>'),
             ("<strong>Ecuador</strong>", '<a href="/es/tcf-canada-ecuador/">Cuenca 200 dólares, Guayaquil 300</a>', '<a href="/es/delf-ecuador/">5 Alianzas Francesas, B2 200 dólares</a>')],
            wide=False) + """

<p>En Chile, el Instituto Francés presenta el DELF como «una opción más económica que el TCF»: el B2 cuesta 137.000
pesos, frente a 299.000 pesos el TCF Canada.</p>
""",
    cta_h2="Diploma o test: el formato se prepara distinto",
    cta_p="""15 versiones con el formato oficial exacto: puntuación sobre 100 con nota eliminatoria para el DELF y el DALF,
escala de 699 o de 499 con el nivel del Marco común europeo por prueba para el TCF y el TEF, y el número correcto de
escuchas en cada caso. Además, corrección con IA de la expresión escrita y oral, en la app «TCF DELF TEF: Tests 2026».
La app está en español.""",
    faq=[("¿Cuál es la diferencia entre el DELF y el TCF?", "El DELF es un diploma oficial, válido de por vida, con el aprobado en 50/100 y una nota eliminatoria por debajo de 5/25: se aprueba o no. El TCF es un test de nivel válido dos años, sin umbral: te sitúa en una escala, y es la institución que recibe tu expediente la que decide si tu puntuación basta."),
         ("¿El DELF sirve para emigrar a Canadá?", "No para la inmigración económica federal. Para Express Entry, IRCC solo acepta dos tests de francés: el TCF Canada y el TEF Canada. Ni el DELF, ni el DALF, ni el TCF tout public figuran en la lista; ni siquiera un DALF C2 vale para un perfil de Express Entry. Para la solicitud de ciudadanía canadiense, el cuestionario de IRCC, consultado el 8 de octubre de 2026, menciona entre los exámenes de francés el TEF Canada y el TCF Canada; guías anteriores nombraban más, entre ellos el DELF y el DALF: verifica la lista de IRCC al presentar tu solicitud."),
         ("¿De verdad mi DELF no caduca nunca?", "El diploma en sí no tiene fecha de vencimiento, y esa es su ventaja central para un expediente francés que se alarga. Pero algunos trámites añaden su propia condición de vigencia: Quebec solo acepta los diplomas DELF y DALF en lugar del TCF Québec si tienen menos de dos años, y con una nota mínima en el oral. «De por vida» es una propiedad del diploma, no una garantía de aceptación."),
         ("¿Cuántas veces se escucha la comprensión oral?", "En el DELF, los documentos de los niveles A1 a B1 se escuchan dos veces. En el TCF y en el TEF hay una sola escucha, sin vuelta atrás, en todas las versiones sin excepción. Es la diferencia práctica más subestimada: muchos candidatos entrenados con recursos del DELF la descubren el día del examen."),
         ("¿Un test se presenta más rápido que un diploma?", "Sí, claramente, en las versiones pensadas para los trámites administrativos franceses: 1 h 30 min para un TEF IRN y 1 h 35 min para un TCF IRN, contra 2 h 10 min para un DELF B1, 2 h 50 min para un DELF B2 y 4 h 30 min para un DALF C1. Las versiones Canada son más largas: 2 h 47 min para el TCF Canada y 2 h 55 min para el TEF Canada."),
         ("¿Se pueden tener los dos?", "Nada lo impide, y a veces es lo más racional: un diploma como base permanente y un test reciente cuando un trámite concreto lo exige. Pero es pagar dos veces: empieza por identificar lo que tu expediente pide realmente antes de acumular."),
         ("¿Dónde presentar el DELF o el TCF Canada en América Latina?", "En los centros autorizados de cada país; en Colombia, Argentina, Perú y Ecuador, el DELF y el DALF se presentan en las Alianzas Francesas. El DELF B2 cuesta 2,500 pesos en México, 490.000 pesos en Colombia, 137.000 pesos en Chile, 461 soles en Perú y 200 dólares en Ecuador; el TCF Canada, de 4,800 a 6,500 pesos en México, desde 1.050.000 pesos en Colombia, 299.000 pesos en Chile y 1,240 soles en Perú. Precios revisados el 8 de octubre de 2026.")],
    also=[("/es/delf-b2/", "Examen DELF B2", "La estructura, la puntuación y las fechas por país."),
          ("/es/dalf-c1/", "Examen DALF C1 y C2", "El nivel avanzado, y lo que te exime de presentar."),
          ("/es/", "TCF Canada y DELF, país por país", "Centros, precios y fechas en España y América Latina.")],
    sources="""<strong>Las listas de justificantes cambian.</strong> Esta página está actualizada al 7 de agosto de 2026; los
precios por país vienen de nuestra revisión de los sitios web de los centros del 8 de octubre de 2026. Cada administración
publica su propia lista, con sus condiciones de nota y de vigencia: verifica la de tu trámite en
<a href="https://www.service-public.fr/" rel="noopener">service-public.fr</a>,
<a href="https://www.canada.ca/" rel="noopener">canada.ca</a> o
<a href="https://www.quebec.ca/immigration" rel="noopener">quebec.ca</a> antes de inscribirte en cualquier examen.""",
))

# ===========================================================================
# TCF CANADA — la guía (de /tcf-canada/ y sus módulos format/, score-nclc/, preparation/, prix-inscription/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/tcf-canada/", lang="es", variant="es-419", section="es", slug="tcf-canada",
    crumbs=[INICIO], crumb="TCF Canada", inline_cta=False,
    title="Examen TCF Canada: formato, puntaje NCLC y preparación",
    desc="Examen TCF Canada: 4 pruebas en 2 h 47 min, la tabla NCLC (NCLC 7 = 458 y 453), precio, validez y dónde presentarlo en México, Colombia, Chile y Perú.",
    h1="TCF Canada: cómo salir bien en el examen de francés para emigrar a Canadá",
    intro="""El TCF Canada es uno de los <strong>dos únicos exámenes de francés</strong> que IRCC reconoce para la
residencia permanente, Express Entry y la ciudadanía. Dura <strong>2 h 47 min</strong>, tiene <strong>cuatro pruebas
obligatorias</strong> que se presentan el mismo día, y tus resultados se convierten en niveles <strong>NCLC</strong>
(en inglés, CLB): cada nivel que subes puede valer decenas de puntos en la clasificación. Para el NCLC 7, el umbral más
común, necesitas <strong>458 en comprensión oral, 453 en comprensión escrita y 10/20 en cada expresión</strong>.""",
    facts=["<strong>4 pruebas obligatorias</strong>, en una sola sesión de 2 h 47 min: comprensión oral, comprensión escrita, expresión escrita y expresión oral.",
           "Comprensiones calificadas en la <strong>escala de 100 a 699</strong>, expresiones sobre <strong>20</strong>; después, cada puntaje se convierte a <a href=\"#puntaje-nclc\">NCLC</a> para tu expediente de IRCC.",
           "<strong>NCLC 7</strong> = 458 en comprensión oral, 453 en comprensión escrita y 10/20 en cada expresión. Es el umbral de referencia del programa federal de trabajadores calificados (Federal Skilled Worker Program).",
           "Constancia de resultados válida <strong>2 años</strong>, y la regla de IRCC es más estricta de lo que parece (<a href=\"#precio-validez\">ver más abajo</a>).",
           "⚠️ <strong>No hay repetición parcial</strong>: se vuelven a presentar las cuatro pruebas o nada.",
           "Para la <strong>ciudadanía</strong> canadiense, solo se exigen la comprensión oral y la expresión oral.",
           "En América Latina, el TCF Canada cuesta, por ejemplo, de 4,800 a 6,500 pesos en México, 299.000 pesos en Chile o 1,240 soles en Perú: <a href=\"#donde\">país por país</a>."],
    toc=[("que-es", "¿Qué es el TCF Canada?"), ("recorrido", "Tu recorrido en 5 pasos"),
         ("formato", "El formato, prueba por prueba"), ("puntaje-nclc", "Puntaje y niveles NCLC: la tabla de IRCC"),
         ("preparacion", "Cómo prepararte"), ("precio-validez", "Precio, validez y repetición"),
         ("donde", "Dónde presentarlo en América Latina y España")],
    body="""
<div class="stats">
<div class="stat"><b>2 h 47 min</b><span>4 pruebas, el mismo día</span><em>CO 35 · CE 60 · EE 60 · EO 12 min</em></div>
<div class="stat"><b>699</b><span>la escala de las preguntas de opción múltiple</span><em>expresiones calificadas sobre 20</em></div>
<div class="stat"><b>458</b><span>en comprensión oral</span><em>para el NCLC 7 (453 en comprensión escrita)</em></div>
<div class="stat"><b>2 años</b><span>de validez</span><em>que IRCC cuenta dos veces</em></div>
</div>

<h2 id="que-es">¿Qué es el TCF Canada?</h2>
<p>El <strong>TCF Canada</strong> es un examen de francés creado por France Éducation international y reconocido por
Inmigración, Refugiados y Ciudadanía de Canadá (IRCC) como prueba de tu nivel de francés en un trámite de
<strong>inmigración económica</strong> —Express Entry, los programas de trabajadores calificados— o de
<strong>ciudadanía</strong>. Se presenta en una sola sesión, en un centro autorizado, y tiene <strong>cuatro pruebas
obligatorias</strong>: comprensión oral, comprensión escrita, expresión escrita y expresión oral. Las dos comprensiones
se califican sobre 699 y las dos expresiones sobre 20; después, cada nota se <strong>convierte en un nivel NCLC</strong>,
la escala que IRCC usa para asignar los puntos.</p>

<p>No es un diploma ni un examen que se «aprueba»: todos salen con un nivel, de A1 a C2, y una constancia de resultados
válida <strong>dos años</strong>. Junto con el TEF Canada, es uno de los dos únicos exámenes que acepta IRCC; el TCF
tout public y el TCF Québec, que se le parecen, no se aceptan para Express Entry.</p>

<h3>Para quién</h3>
<ul>
<li>Los candidatos a <strong>Express Entry</strong> y a los programas federales, que deben alcanzar un NCLC
determinado: el NCLC 7 es el umbral más común.</li>
<li>Los solicitantes de la <strong>ciudadanía</strong>, para quienes solo cuentan las dos pruebas orales.</li>
<li>Los candidatos a los programas de <strong>Quebec</strong>, que también lo aceptan desde 2022, aunque allí el TCF
Québec, modular, suele salir más barato.</li>
</ul>

<h2 id="recorrido">Tu recorrido en 5 pasos</h2>
<ol class="steps">
<li><b>Verifica qué examen te piden</b><span>Express Entry, ciudadanía: el TCF <em>Canada</em> o el TEF Canada, nunca el TCF tout public ni el TCF Québec. <a href="/es/examen-de-frances-para-canada/">¿TCF o TEF Canada?</a></span></li>
<li><b>Fija el puntaje que necesitas</b><span>IRCC lee el NCLC, no la letra: 458 en comprensión oral y 453 en comprensión escrita para el NCLC 7; 523 y 524 para el NCLC 9. <a href="#puntaje-nclc">La tabla completa.</a></span></li>
<li><b>Mídete antes de pagar</b><span>Un simulacro calificado sobre 699 y convertido a NCLC te dice si la sesión del mes que viene es la buena; las <a href="#trampas">trampas de formato</a> se trabajan antes.</span></li>
<li><b>Reserva el centro y la fecha</b><span>En Francia, una sesión al mes por centro, de 195 a 285 €; en Canadá, de 390 a 440 dólares canadienses y cupos que se agotan en minutos. <a href="#donde">En América Latina y España</a>, país por país.</span></li>
<li><b>El día del examen, y después tu expediente</b><span>Pasaporte y citación; constancia de resultados en 2 a 4 semanas, válida dos años, y <a href="#precio-validez">IRCC cuenta esos dos años dos veces</a>.</span></li>
</ol>

<h2 id="formato">El formato, prueba por prueba</h2>
<p>Las cuatro pruebas son <strong>inseparables</strong>: se presentan en la misma sesión y no puedes elegir solo una
parte. Es la gran diferencia con el TCF Québec, que es modular.</p>
""" + table("Formato oficial del TCF Canada. Fuente: France Éducation international, estructura verificada en julio de 2026.",
            ["Prueba", "Preguntas / tareas", "Duración", "Particularidad"],
            [("Comprensión oral", "39 preguntas de opción múltiple, con 4 opciones", "35 min", "<strong>Una sola escucha</strong>, sin volver atrás"),
             ("Comprensión escrita", "39 preguntas de opción múltiple, con 4 opciones", "60 min", "Navegación libre entre las preguntas"),
             ("Expresión escrita", "3 tareas", "60 min", "60-120, luego 120-150 y luego 120-180 palabras"),
             ("Expresión oral", "3 tareas", "12 min", "Cara a cara, con 2 min de preparación para la tarea 2"),
             ("<strong>Total</strong>", "", "<strong>2 h 47 min</strong>", "")], wide=False) + """
<p>La dificultad de las preguntas de opción múltiple es <strong>progresiva, de A1 a C2</strong>: las primeras son
fáciles y las últimas corresponden a un nivel avanzado. Nadie espera que aciertes todo, y sobre todo no conviene
empeñarse en una pregunta difícil al final de la prueba: el cronómetro es el verdadero adversario.</p>

<p>Cada tarea de expresión escrita tiene su género: un <strong>mensaje</strong> (60-120 palabras), un <strong>artículo o
relato</strong> (120-150 palabras) y una <strong>comparación de dos puntos de vista con una opinión argumentada</strong>
(120-180 palabras). La tercera es la que más diferencia a los candidatos: ahí se juega el paso de 10 a 14 sobre 20. En el
oral, las tres tareas encadenan una entrevista dirigida, una interacción con preparación y la expresión de un punto de
vista.</p>

<h3 id="trampas">Las trampas de formato que cuestan puntos</h3>
<p>Los candidatos que se quedan cortos por poco son casi siempre los que descubren el formato el día del examen. Hay
cuatro trampas que se repiten.</p>
<ul>
<li><strong>Una sola escucha, sin volver atrás.</strong> En comprensión oral, el audio no se repite y no puedes regresar
a una pregunta anterior. Si te pierdes en una, está perdida: lo importante es pasar de inmediato a la siguiente, no
reconstruir lo que se te escapó.</li>
<li><strong>El conteo de palabras de las tareas escritas.</strong> Los rangos (60-120, 120-150, 120-180) no son
orientativos: escribir 90 palabras en una tarea que pide un mínimo de 120 cuesta puntos en el criterio de adecuación a la
consigna, sea cual sea la calidad del idioma.</li>
<li><strong>La progresión de la dificultad.</strong> Las últimas preguntas son de nivel C1-C2. Aferrarse a ellas a costa
del tiempo es un mal cálculo: tienen su peso en el modelo, pero no valen lo que tres preguntas de nivel B1 que se quedan
sin responder.</li>
<li><strong>Los 12 minutos del oral.</strong> Tres tareas en doce minutos es muy poco tiempo. Los candidatos sin
entrenamiento gastan su tiempo en la primera tarea, la más fácil, y resuelven a la carrera la tercera, la que más puntos
da.</li>
</ul>

<div class="note">
<p><strong>El número de preguntas en pantalla puede sorprenderte.</strong> En la modalidad en computadora, France
Éducation international agrega preguntas que no cuentan para tu puntaje: le sirven para sus análisis de validez. Que la
prueba se alargue respecto al número anunciado es normal y no anticipa nada de tu resultado.</p>
</div>

<h2 id="puntaje-nclc">Puntaje y niveles NCLC: la tabla de IRCC</h2>
<p>El TCF es un <strong>test de nivel, no un examen que se reprueba</strong>: no hay nota eliminatoria ni umbral de
aprobación. Obtienes un puntaje por prueba, y es el organismo que recibe tu expediente el que decide si te alcanza. En la
escala del TCF, el B2 va de 400 a 499 en las comprensiones y de 10 a 13 sobre 20 en las expresiones. Tu puntaje en las
comprensiones no es tu número de respuestas correctas: lo calcula un modelo que pondera la dificultad de las preguntas,
así que dos candidatos con el mismo número de aciertos pueden obtener puntajes distintos.</p>

<p>Para tu trámite en Canadá solo cuenta el <strong>NCLC</strong> (<em lang="fr">Niveaux de compétence linguistique
canadiens</em>) en el que cae cada uno de tus cuatro puntajes. Esta es la conversión oficial.</p>
""" + table("TCF Canada → NCLC. Comprensiones calificadas sobre 699, expresiones sobre 20. Fuente: tablas de equivalencia de IRCC, cotejadas en dos páginas oficiales el 27 de julio de 2026.",
            ["NCLC", "Compr. oral", "Compr. escrita", "Expr. oral", "Expr. escrita"],
            [("10 y más", "549–699", "549–699", "16–20", "16–20"), ("9", "523–548", "524–548", "14–15", "14–15"),
             ("8", "503–522", "499–523", "12–13", "12–13"),
             ("<strong>7</strong>", "<strong>458–502</strong>", "<strong>453–498</strong>", "<strong>10–11</strong>", "<strong>10–11</strong>"),
             ("6", "398–457", "406–452", "7–9", "7–9"), ("5", "369–397", "375–405", "6", "6"),
             ("4", "331–368", "342–374", "4–5", "4–5")], wide=False) + """
<div class="note">
<p><strong>«Tengo el B2, entonces tengo el NCLC 7» es falso.</strong> El B2 empieza en 400 en comprensión oral; el
NCLC 7, en 458. Entre los dos hay 58 puntos y un nivel NCLC completo: un B2 de 420 en comprensión oral solo vale NCLC 6.
Es la confusión más cara del TCF Canada.</p>
</div>

<p>Lo que manda es <strong>tu prueba más débil</strong>: IRCC toma el perfil completo, y un NCLC 9 en comprensión escrita
no compensa un NCLC 6 en el oral. Tu estrategia de preparación se desprende directamente de ahí.</p>

<h2 id="preparacion">Cómo prepararte</h2>
<p>El francés nunca había tenido tanto peso en la selección federal: las rondas de Express Entry reservadas a los
francófonos invitan con puntajes muy inferiores a los de las rondas generales. Esta tabla compara el puntaje CRS mínimo
de las rondas francófonas con el de las rondas de la categoría de experiencia canadiense, en el mismo periodo.</p>
""" + table("Rondas de invitaciones de Express Entry en 2026: categoría francófona frente a categoría de experiencia canadiense. Fuente: IRCC, datos consultados el 27 de julio de 2026.",
            ["Fecha", "Ronda francófona: CRS", "Experiencia canadiense: CRS"],
            [("22 de julio de 2026", "<strong>399</strong> (5000 invitaciones)", "—"),
             ("21 de julio de 2026", "—", "516"),
             ("9 de julio de 2026", "<strong>420</strong> (5000)", "517"),
             ("28 de mayo de 2026", "<strong>409</strong> (4500)", "518"),
             ("29 de abril de 2026", "<strong>400</strong> (4000)", "514")], wide=False) + """
<p>La diferencia es de <strong>unos 100 puntos CRS</strong>. Un mismo perfil puede ser invitado por la vía francófona
con un puntaje con el que no tendría ninguna oportunidad en la categoría general. Por eso el TCF Canada es, para un
francófono o para quien aprende francés, la inversión más rentable de todo el expediente.</p>

<p>La dificultad del TCF Canada no es solo lingüística: es un examen de <strong>formato</strong>. Preguntas que se
encadenan rápido en las comprensiones, consignas estrictas en las expresiones, cronómetro ajustado. El método que
funciona tiene tres pasos.</p>
<ol>
<li><strong>Un simulacro completo desde el principio</strong>, antes de cualquier repaso, para situar tu NCLC actual en
cada prueba. Sin ese punto de partida trabajas a ciegas, y casi siempre en la habilidad equivocada.</li>
<li><strong>Un entrenamiento enfocado en tu prueba más débil.</strong> Es la que pone el techo a tu expediente: pasar de
NCLC 7 a 8 en una prueba que ya es fuerte no cambia nada si otra se queda en 6.</li>
<li><strong>Simulacros cronometrados con regularidad</strong>, hasta que el formato ya no te sorprenda. El objetivo no es
aprenderte respuestas, sino volver mecánico el desarrollo del examen para liberar tu atención.</li>
</ol>
<p>En las expresiones escrita y oral, el punto ciego es estructural: no puedes autoevaluarte con criterios que no
conoces. Un candidato rara vez sabe si escribe para 9 o para 10 sobre 20, y esa es exactamente la frontera entre el
NCLC 6 y el NCLC 7. Es lo que resuelve una corrección con IA según los criterios oficiales.</p>

<h2 id="precio-validez">Precio, validez y repetición</h2>
<p><strong>El precio.</strong> No existe una tarifa nacional: cada centro autorizado fija la suya, y muchos —entre ellos
la Alianza Francesa de Montreal— no publican ninguna. En los centros revisados, el TCF Canada cuesta de 195 a 285 € en
Francia y de 390 a 440 dólares canadienses en Canadá; entre los que mostraban sus tarifas en julio de 2026 se observan
unos <strong>220 a 245 €</strong> en Europa y <strong>400 a 440 dólares canadienses</strong> en Canadá por el examen
completo. Desconfía de las tarifas que circulan en los comparadores: rara vez citan una fuente y suelen mezclar el TCF
Canada con el TCF Québec, que no cuestan lo mismo. Los precios de América Latina y España están
<a href="#donde">más abajo</a>.</p>

<p><strong>La validez.</strong> La constancia vale <strong>dos años a partir de su fecha de emisión</strong>. La regla de
IRCC es más estricta de lo que parece: tus resultados deben tener menos de dos años <em>cuando creas tu perfil de Express
Entry</em> <strong>y</strong> <em>cuando presentas tu solicitud de residencia permanente</em>. Un examen presentado
demasiado pronto en el trámite puede vencer entre una fecha y la otra.</p>

<p><strong>La repetición.</strong> No hay <strong>repetición parcial</strong>: se vuelven a presentar las cuatro pruebas.
El número de intentos es ilimitado, pero cada uno se paga completo. Desde las sesiones del 1 de septiembre de 2026,
France Éducation international <strong>ya no acepta solicitudes de recalificación</strong>; antes, la recalificación solo
se aplicaba a las pruebas de expresión —nunca a las preguntas de opción múltiple—, se pedía dentro del mes siguiente y la
nueva nota reemplazaba a la anterior, <strong>aunque fuera más baja</strong>.</p>

<div class="note">
<p><strong>El plazo entre dos intentos no se conoce con exactitud.</strong> Verás circular «20 días» y «30 días». Las dos
cifras vienen de la propia France Éducation international: sus páginas del examen anuncian 20 días, y varias de sus
fichas en PDF, 30. No programes un segundo intento con una fecha límite encima sin que tu centro te confirme el
plazo.</p>
</div>

<h2 id="donde">Dónde presentarlo en América Latina y España</h2>
<p>El TCF Canada se presenta en un centro autorizado por France Éducation international, pero <strong>no todos los
centros TCF ofrecen la versión Canada</strong>. La constancia la emite France Éducation international, sea cual sea el
centro, e IRCC la acepta igual: lo que cuenta es inscribirte en el TCF Canada y no en el TCF tout public. Esto es lo que
mostraban los sitios web de los centros el 8 de octubre de 2026.</p>
""" + table("El TCF Canada en América Latina y España, según los sitios web de los centros el 8 de octubre de 2026. Precio para un candidato libre, en moneda local; las fechas y el detalle, centro por centro, en la página de cada país.",
            ["País", "Dónde se presenta", "Precio del TCF Canada"],
            [('<a href="/es/tcf-canada-mexico/"><strong>México</strong></a>', "5 de 11 centros: el IFAL (Ciudad de México), las Alianzas Francesas de Guadalajara, Puebla y Aguascalientes, y la UAEH (Pachuca)", "de 4,800 a 6,500 pesos"),
             ('<a href="/es/tcf-canada-colombia/"><strong>Colombia</strong></a>', "las 7 Alianzas Francesas: Bogotá, Medellín, Cali, Barranquilla, Cartagena, Manizales y Pereira", "de 1.050.000 a 1.247.000 pesos"),
             ('<a href="/es/tcf-canada-argentina/"><strong>Argentina</strong></a>', "4 centros, entre ellos Campus France (Buenos Aires) y las Alianzas Francesas de Córdoba y de Rosario", "no publicado: hay que pedirlo"),
             ('<a href="/es/tcf-canada-chile/"><strong>Chile</strong></a>', "el Instituto Francés de Chile (Santiago) y la Alianza Francesa de Concepción", "299.000 pesos"),
             ('<a href="/es/tcf-canada-peru/"><strong>Perú</strong></a>', "un solo centro: la Alianza Francesa de Lima", "1,240 soles"),
             ('<a href="/es/tcf-canada-ecuador/"><strong>Ecuador</strong></a>', "las Alianzas Francesas de Cuenca (a solicitud) y de Guayaquil; la de Quito orienta hacia el TEF Canada", "200 dólares en Cuenca, 300 en Guayaquil"),
             ('<a href="/es/tcf-canada-espana/"><strong>España</strong></a>', "11 de 14 centros, en Madrid, Barcelona, Valencia, Bilbao, Sevilla, Málaga, Oviedo, Cartagena y Valladolid", "de 275 a 287 €")],
            wide=False) + """
<p>Las sesiones se llenan rápido en varios países: en la Alianza Francesa de Lima, el único centro de Perú, la última sesión de 2026, la del
11 de diciembre, ya estaba completa el 8 de octubre. En Canadá, el TCF Canada se presenta en 47 centros autorizados, de
390 a 440 dólares canadienses, y los cupos se agotan en minutos (<a href="/en/tcf-canada-test-centres/" hreflang="en">la
lista, en inglés</a>).</p>
<p class="serie-label">El TCF Canada, país por país</p>
<div class="chips">
<a class="chip" href="/es/tcf-canada-mexico/">México</a>
<a class="chip" href="/es/tcf-canada-colombia/">Colombia</a>
<a class="chip" href="/es/tcf-canada-argentina/">Argentina</a>
<a class="chip" href="/es/tcf-canada-chile/">Chile</a>
<a class="chip" href="/es/tcf-canada-peru/">Perú</a>
<a class="chip" href="/es/tcf-canada-ecuador/">Ecuador</a>
<a class="chip" href="/es/tcf-canada-espana/">España</a>
<a class="chip" href="/en/tcf-canada-test-centres/" hreflang="en">Canadá (en inglés)</a>
<a class="chip" href="/es/">Todos los países →</a>
</div>
""",
    cta_h2="Conoce tu nivel antes de pagar 440 dólares canadienses",
    cta_p="""Simulacros cronometrados con el formato exacto del TCF Canada, conversión automática a NCLC por prueba y
corrección con IA de la expresión escrita y oral según los criterios oficiales, en la app «TCF DELF TEF: Tests 2026».
La app está en español.""",
    faq=[("¿Qué es el examen TCF Canada?", "Un examen de francés de France Éducation international, reconocido por Inmigración, Refugiados y Ciudadanía de Canadá (IRCC) para la inmigración económica y la ciudadanía. Cuatro pruebas obligatorias en una sola sesión —comprensión oral, comprensión escrita, expresión escrita y expresión oral—, un nivel de A1 a C2 por prueba, convertido a NCLC, y una constancia de resultados válida dos años."),
         ("¿Qué diferencia hay entre el TCF Canada, el TCF tout public y el TCF Québec?", "El TCF tout public sirve para estudios y trámites personales, y el TCF Québec, para los programas del Ministerio de Inmigración de Quebec; IRCC no acepta ninguno de los dos para Express Entry. Solo acepta el TCF Canada y el TEF Canada. En cambio, Quebec también reconoce el TCF Canada desde 2022."),
         ("¿El TCF Canada se aprueba o se reprueba?", "Ni lo uno ni lo otro: no hay umbral de aprobación. Cada prueba da un nivel, de A1 a C2, convertido a NCLC; es tu programa de inmigración el que fija el nivel que debes alcanzar, casi siempre el NCLC 7. Un puntaje insuficiente se corrige volviendo a presentar las cuatro pruebas, después de 20 a 30 días."),
         ("¿Qué puntaje necesito en el TCF Canada para el NCLC 7?", "458 en comprensión oral, 453 en comprensión escrita y 10 sobre 20 tanto en expresión oral como en expresión escrita. El NCLC 7 en las cuatro pruebas es el umbral de referencia del programa federal de trabajadores calificados. Con un solo punto menos, bajas al NCLC 6."),
         ("¿Cuánto cuesta el TCF Canada?", "No hay tarifa nacional: cada centro autorizado fija su precio. Según los sitios web de los centros el 8 de octubre de 2026: de 4,800 a 6,500 pesos en México, de 1.050.000 a 1.247.000 pesos en Colombia, 299.000 pesos en Chile, 1,240 soles en Perú, de 200 a 300 dólares en Ecuador y de 275 a 287 € en España; en Argentina, ningún centro lo publica. En Canadá, de 390 a 440 dólares canadienses."),
         ("¿Dónde presentar el TCF Canada en México, Colombia, Chile o Perú?", "En <a href=\"/es/tcf-canada-mexico/\">México</a>, en 5 de los 11 centros autorizados: el IFAL en la Ciudad de México, las Alianzas Francesas de Guadalajara, Puebla y Aguascalientes, y la UAEH en Pachuca. En <a href=\"/es/tcf-canada-colombia/\">Colombia</a>, en las 7 Alianzas Francesas. En <a href=\"/es/tcf-canada-chile/\">Chile</a>, en el Instituto Francés de Chile (Santiago) y en la Alianza Francesa de Concepción. En <a href=\"/es/tcf-canada-peru/\">Perú</a>, solo en la Alianza Francesa de Lima. También en <a href=\"/es/tcf-canada-argentina/\">Argentina</a> (4 centros) y en <a href=\"/es/tcf-canada-ecuador/\">Ecuador</a> (Cuenca y Guayaquil)."),
         ("¿Cuánto tiempo son válidos los resultados del TCF Canada?", "Dos años a partir de la fecha de emisión de la constancia. La regla de IRCC es más estricta de lo que parece: tus resultados deben tener menos de dos años cuando creas tu perfil de Express Entry y cuando presentas tu solicitud de residencia permanente."),
         ("¿Puedo repetir solo la prueba que me salió mal?", "No. En el TCF Canada no hay repetición parcial: se vuelve a presentar el examen completo, con las cuatro pruebas. El número de intentos es ilimitado. Y desde las sesiones del 1 de septiembre de 2026, no se acepta ninguna solicitud de recalificación.")],
    also=[("/es/examen-de-frances-para-canada/", "¿TCF Canada o TEF Canada?", "Las dos tablas de conversión NCLC, el formato y los precios comparados, y la trampa de la columna «<span lang=\"fr\">ancien score</span>»."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina: centros, precios y fechas."),
          ("/es/certificado-de-frances/", "¿Qué certificado de francés elegir?", "DELF, DALF, TCF o TEF: diploma de por vida o test válido dos años.")],
    sources="""<strong>Las reglas cambian.</strong> Esta página está actualizada al 7 de agosto de 2026 —los centros, precios y
fechas de América Latina y España, al 8 de octubre de 2026, según los sitios web de los centros— y no constituye
asesoría migratoria: los umbrales, las tablas de conversión y las rondas de invitaciones cambian con frecuencia.
Verifica siempre tu situación en <a href="https://www.canada.ca/" rel="noopener">canada.ca</a> y el formato del examen
en <a href="https://www.france-education-international.fr/test/tcf-canada" rel="noopener">france-education-international.fr</a>
antes de inscribirte o de presentar una solicitud.""",
))


# ===========================================================================
# ¿TCF CANADA O TEF CANADA? (de /blog/tcf-ou-tef-canada/, con material de /blog/difference-tcf-tef/)
# ===========================================================================
PAGES.append(dict(
    fr_path="/blog/tcf-ou-tef-canada/", lang="es", variant="es-419", slug="examen-de-frances-para-canada",
    crumbs=[INICIO], crumb="TCF o TEF Canada",
    title="Examen de francés para la residencia en Canadá: ¿TCF o TEF?",
    desc="Diferencia entre TCF y TEF Canada para la residencia permanente: mismo NCLC, ninguno más fácil. Tablas oficiales, formato, precios y dónde presentarlos.",
    h1="TCF Canada o TEF Canada: ¿cuál elegir para tu trámite de inmigración?",
    intro="""Para la residencia permanente (PR) por Express Entry, IRCC acepta <strong>solo dos exámenes de
francés</strong>: el TCF Canada y el TEF Canada. <strong>Ninguno es más fácil</strong>: los dos llevan a la misma escala
<strong>NCLC</strong> (en inglés, CLB) y, en centros comparables, cuestan más o menos lo mismo. <strong>El único
criterio racional es tu puntaje</strong>: presenta un simulacro de cada uno y quédate con aquel en el que salgas mejor.
Aquí tienes las dos tablas de conversión oficiales, las diferencias de formato que favorecen a un perfil o a otro, y el
error al llenar el perfil que provoca rechazos.""",
    facts=["Para Express Entry, IRCC solo acepta <strong>dos</strong> exámenes de francés: el TCF Canada y el TEF Canada. Ni el DELF ni el DALF.",
           "Las escalas son distintas: TCF = comprensiones sobre <strong>699</strong>, expresiones sobre <strong>20</strong>. TEF = <strong>las cuatro pruebas sobre 699</strong>, más una columna «<span lang=\"fr\">ancien score</span>» sobre 300 / 360 / 450 / 450.",
           "⚠️ Con el TEF, ingresa en tu perfil los puntajes de la columna <strong>«<span lang=\"fr\">Équivalence ancien score</span>»</strong>, no los de la columna sobre 699, <strong>sea cual sea la fecha de tu examen</strong>.",
           "Validez de <strong>2 años</strong>, exigida dos veces: al crear el perfil <em>y</em> al presentar la solicitud.",
           "<strong>20 días</strong> de espera entre dos intentos, para los dos exámenes (algunas fichas de France Éducation international dicen 30 para el TCF).",
           "Precios observados: <strong>220–245 €</strong> en Europa y <strong>400–440 dólares canadienses</strong> en Canadá, y muchos centros no publican ninguna tarifa.",
           "En América Latina, el TEF Canada se ofrece, por ejemplo, en Alianzas Francesas de México (Ciudad de México, Monterrey, Puebla…), de Buenos Aires, de Lima y de Quito: <a href=\"#donde\">dónde presentar cada uno</a>."],
    toc=[("tablas", "Las dos tablas de conversión NCLC"),
         ("trampa", "La trampa de la columna «<span lang=\"fr\">ancien score</span>»"),
         ("formato", "Las diferencias de formato que cuentan"),
         ("precios", "Precios, plazos y disponibilidad"),
         ("donde", "Dónde presentarlos en América Latina y España"),
         ("quebec", "El caso de Quebec"),
         ("versiones", "Diferencia entre TCF y TEF: todas las versiones"),
         ("elegir", "Cómo elegir, en concreto")],
    body="""
<h2 id="tablas">Las dos tablas de conversión NCLC</h2>
<p>Es lo único que cuenta para tu expediente: tu puntaje bruto no dice nada por sí solo; lo que se toma en cuenta es el
<strong>nivel NCLC</strong> que produce. Y cada habilidad se evalúa por separado: <strong>no hay ninguna
compensación</strong>. Un excelente puntaje en comprensión no compensa una expresión oral débil: tu habilidad más baja
pone el techo a todo tu expediente.</p>
""" + table("TCF Canada → NCLC. Las comprensiones se califican sobre 699 y las expresiones sobre 20. Fuente: tablas de equivalencia de IRCC, consultadas el 27 de julio de 2026.",
            ["NCLC", "Compr. oral /699", "Compr. escrita /699", "Expr. oral /20", "Expr. escrita /20"],
            [("<strong>10 y más</strong>", "549–699", "549–699", "16–20", "16–20"), ("<strong>9</strong>", "523–548", "524–548", "14–15", "14–15"),
             ("<strong>8</strong>", "503–522", "499–523", "12–13", "12–13"), ("<strong>7</strong>", "458–502", "453–498", "10–11", "10–11"),
             ("<strong>6</strong>", "398–457", "406–452", "7–9", "7–9"), ("<strong>5</strong>", "369–397", "375–405", "6", "6"),
             ("<strong>4</strong>", "331–368", "342–374", "4–5", "4–5")], wide=False) + "\n" + \
         table('TEF Canada → NCLC: las escalas que IRCC usa en el perfil de Express Entry, es decir, las de la columna «<em lang="fr">Équivalence ancien score</em>» de tu constancia, y no la columna sobre 699. Fuente: tablas de equivalencia de IRCC, consultadas el 27 de julio de 2026.',
            ["NCLC", "Compr. escrita /300", "Compr. oral /360", "Expr. escrita /450", "Expr. oral /450"],
            [("<strong>10</strong>", "263–300", "316–360", "393–450", "393–450"), ("<strong>9</strong>", "248–262", "298–315", "371–392", "371–392"),
             ("<strong>8</strong>", "233–247", "280–297", "349–370", "349–370"), ("<strong>7</strong>", "207–232", "249–279", "310–348", "310–348"),
             ("<strong>6</strong>", "181–206", "217–248", "271–309", "271–309"), ("<strong>5</strong>", "151–180", "181–216", "226–270", "226–270"),
             ("<strong>4</strong>", "121–150", "145–180", "181–225", "181–225")], wide=False) + """
<p>Fíjate en la diferencia de estructura: en el TCF Canada, <strong>las cuatro pruebas solo usan dos escalas</strong>
(699 y 20), y los límites de las dos comprensiones están ligeramente desfasados entre sí. En el TEF Canada la lógica es
otra. Desde el <strong>1 de octubre de 2019</strong>, la constancia del TEF califica <strong>sus cuatro pruebas sobre
699</strong>: es la cifra que verás en grande en tu resultado. Pero al lado conserva una segunda columna, titulada
«<strong><em lang="fr">Équivalence ancien score</em></strong>» (equivalencia en el puntaje anterior), que retoma las
escalas vigentes antes del 30 de septiembre de 2019: 300 en comprensión escrita, 360 en comprensión oral y 450 en cada
prueba de expresión. <strong>IRCC usa esa segunda columna, y solo esa</strong>: por eso la tabla de arriba no está
sobre 699.</p>

<p>De ahí la fuente de error número 1 al leer una tabla de conversión encontrada al azar en internet: un puntaje del TEF
no tiene ningún sentido mientras no sepas <em>de qué prueba</em> y <em>de qué columna</em> sale. Un «350» puede ser
excelente o mediocre según la casilla de donde viene.</p>

<div class="note">
<p><strong>Y una trampa simétrica del lado del TCF Canada: C1 no es NCLC 10.</strong> Una constancia que muestra «C1» en
comprensión oral o escrita corresponde a un puntaje de 500 a 599 en la escala del MCER, pero <strong>el NCLC 10 empieza
en 549</strong>. Un C1 de 510 solo vale NCLC 8. IRCC cuenta el NCLC, nunca la letra.</p>
</div>

<h2 id="trampa">La trampa de la columna «<span lang="fr">ancien score</span>»</h2>
<div class="note">
<p><strong>Si te quedas con una sola cosa de este artículo, que sea esta.</strong> La constancia del TEF tiene
<em>dos</em> columnas de puntajes: una columna «<span lang="fr">Score / 699</span>» y una columna
«<strong><em lang="fr">Équivalence ancien score</em></strong>». Para llenar tu perfil de Express Entry, <strong>IRCC
espera los puntajes de la columna <em lang="fr">Équivalence ancien score</em></strong>, no los de la columna sobre 699, y
lo dice sin rodeos: ingresa solo los puntajes de esa columna; si no, tu solicitud puede ser rechazada. Dicho de otro
modo: la cifra más visible de tu constancia es justamente la que no debes copiar.</p>
</div>

<p><strong>Una precisión de fechas, porque circula equivocada casi en todas partes.</strong> Esas dos columnas no datan de
diciembre de 2023: el TEF califica cada prueba sobre 699 desde el <strong>1 de octubre de 2019</strong>. Lo que cambió la
reforma del <strong>11 de diciembre de 2023</strong> fue otra cosa. <strong>Recalibró los tramos prueba por
prueba</strong> —antes, las cuatro pruebas compartían los mismos límites; desde entonces, cada una tiene los suyos— y
<strong>redujo el número de preguntas</strong> en comprensión escrita y oral, sin tocar las duraciones. El TEF IRN no se
vio afectado por esa reforma.</p>

<p>Esa doble columna explica también por qué encontrarás en internet dos tablas TEF → NCLC que parecen contradecirse.
Las dos son correctas: la que está sobre 699 la publica Le français des affaires; la que está sobre 300/360/450 es la que
usa IRCC. Describen la misma realidad en dos unidades distintas. Para tu perfil, solo cuenta la segunda.</p>

<p>Otra sutileza, y es contraintuitiva: el TEF tiene <strong>tres tablas de IRCC según la fecha del examen</strong>
(antes del 30 de septiembre de 2019; del 1 de octubre de 2019 al 10 de diciembre de 2023; a partir del 11 de diciembre
de 2023), mientras que el TCF Canada solo tiene una. <strong>Pero para Express Entry se aplica la más antigua de las
tres</strong> —la de la columna <em lang="fr">Équivalence ancien score</em>—, <em>sea cual sea la fecha en que
presentaste el examen</em>. Así que no busques la tabla que corresponde a tu fecha de examen: son otros programas, como el
Programa Piloto de Inmigración en Comunidades Francófonas, los que usan las tablas fechadas.</p>

<h2 id="formato">Las diferencias de formato que cuentan</h2>
""" + table("Comparación de formatos, versiones de inmigración. Fuentes: France Éducation international (TCF Canada) y Le français des affaires (TEF Canada), consultadas en julio de 2026.",
            ["Prueba", "TCF Canada", "TEF Canada"],
            [("Comprensión oral", "39 preguntas de opción múltiple · 35 min", "40 preguntas · 40 min"),
             ("Comprensión escrita", "39 preguntas de opción múltiple · 60 min", "40 preguntas · 1 h"),
             ("Expresión escrita", "3 tareas · 60 min · ~300 a 450 palabras", "2 secciones · 1 h · ~280 palabras"),
             ("Expresión oral", "3 tareas · 12 min, cara a cara", "2 secciones · 15 min, cara a cara"),
             ("Duración total", "2 h 47 min", "2 h 55 min"),
             ("Modalidad", "en papel <em>o</em> en computadora, según el centro", "en computadora (oral cara a cara)"),
             ("Calificación de la expresión", "sobre 20", "sobre 699 <em>(450 en «<span lang=\"fr\">ancien score</span>»)</em>")], wide=False) + """
<p>Cuatro diferencias tienen consecuencias reales.</p>

<p><strong>La granularidad de la expresión.</strong> En el TCF Canada, la expresión se califica sobre 20: pasar de 11 a
12 te hace subir del NCLC 7 al NCLC 8. Un solo punto lo cambia todo. En el TEF, la expresión se califica sobre 699 —o
450 en la columna «<span lang="fr">ancien score</span>»—, es decir, en una escala mucho más fina y menos brusca: ahí hay
que ganar una veintena de puntos para cambiar de nivel NCLC. Si eres un candidato «al límite», esa granularidad puede
jugar a tu favor… o costarte caro.</p>

<p><strong>El volumen de escritura.</strong> El TCF Canada pide unas 300 a 450 palabras repartidas en <em>tres</em>
tareas en una hora; el TEF Canada, unas 280 palabras en <em>dos</em> secciones. Si escribes despacio, el TEF es menos
tenso. Si te sientes más cómodo con formatos cortos y variados, el TCF te convendrá más.</p>

<p><strong>La estructura del oral.</strong> Los dos exámenes te hacen hablar <em>cara a cara con un examinador</em>: en
eso no hay diferencia. Lo que cambia es la estructura: el TCF encadena <strong>tres tareas cortas en 12 minutos</strong>,
con dos minutos de preparación solo para la segunda; el TEF tiene <strong>dos secciones más largas</strong> —obtener
información y luego argumentar para convencer—, cada una con su propio tiempo de preparación. Si eres más sólido
desarrollando un argumento que encadenando intercambios rápidos, la estructura del TEF te favorece.</p>

<p><strong>Una sola escucha.</strong> En el TCF Canada, <em>cada grabación se emite una sola vez</em>, y la pregunta solo
aparece después de la escucha. Es la prueba que más sorprende a los candidatos mal preparados, y un buen argumento para
entrenar en condiciones reales antes del día del examen. El TEF funciona igual: cada audio se emite una sola vez y
respondes sobre la marcha, sin poder volver atrás, a diferencia del DELF, donde los documentos de los niveles A1 a B1 se
emiten dos veces.</p>

<div class="note">
<p><strong>Cuidado con la mención «<span lang="fr">A1 non atteint</span>» (A1 no alcanzado) en la expresión escrita del
TCF Canada.</strong> Tu prueba de expresión escrita puede anularse si la letra no es legible (en la modalidad en papel), si no respetas el
número de palabras exigido en una tarea, si tu texto está fuera de tema o si una tarea no se realizó. No son
penalizaciones de puntos: es un piso que hace caer toda la prueba.</p>
</div>

<h2 id="precios">Precios, plazos y disponibilidad</h2>
<p><strong>Ni France Éducation international ni Le français des affaires publican una tarifa nacional.</strong> Los dos
remiten explícitamente al centro autorizado, que fija libremente su precio. En Francia, en los centros verificados en
julio de 2026: TCF Canada a 220 € (Alianza Francesa de Lyon) y 200 € (Alianza Francesa de Montpellier); TEF Canada a
245 € (ALIP, París). En Canadá, las tarifas publicadas son escasas y bastante más altas: el TCF Canada completo cuesta
<strong>400 dólares canadienses</strong> en la Alianza Francesa de Edmonton y <strong>440</strong> en la École
internationale de français de la UQTR, según lo consultado el 30 de julio de 2026.</p>

<div class="note">
<p><strong>Muchos centros no publican nada</strong>: la Alianza Francesa de Montreal, por ejemplo, no muestra ningún
precio para el TCF; la inscripción se hace en línea según la disponibilidad, y la única suma indicada es un cargo por
cancelación de 75 dólares. Los comparadores que atribuyen tarifas precisas a esos centros no citan ninguna fuente y
suelen confundir el TCF Québec con el TCF Canada. Además, no encontramos <strong>ninguna tarifa canadiense verificable
para el TEF Canada</strong>: pídela al centro.</p>
</div>

<p>Dicho de otro modo, <strong>el precio no decide entre los dos exámenes</strong>: en centros comparables cuestan más o
menos lo mismo. Desconfía de cualquier sitio que anuncie una tarifa «oficial».</p>

<p>En cuanto a la red, el TEF afirma tener 500 centros en más de 110 países, y el TCF, 768 centros en el mundo. Los
resultados del TCF Canada se envían dentro de los 15 días hábiles siguientes a la recepción del material de la sesión;
los del TEF llegan en 1 a 2 semanas, aproximadamente. Para el TEF, cuidado con el punto de partida de los dos años de
validez: las condiciones de inscripción de Le français des affaires la cuentan <strong>a partir de la fecha de emisión
de la constancia</strong>, y no de la fecha del examen, pero su página de presentación del TEF habla de dos años «a
partir de la fecha del examen». La diferencia puede ser de varias semanas y contar si tu trámite se alarga: toma la fecha
menos favorable y pide confirmación a tu centro.</p>

<p>Por último, una restricción propia del TEF: <strong>todas las pruebas deben presentarse el mismo día</strong> para que
las autoridades canadienses reconozcan la constancia.</p>

<h2 id="donde">Dónde presentarlos en América Latina y España</h2>
<p>Para el TCF Canada, nuestras guías revisan los centros uno por uno, con sus precios y sus fechas: en Francia, de 195 a
285 €, con una sesión al mes por centro; en Canadá, 47 centros, de 390 a 440 dólares canadienses, con sesiones que se
llenan en minutos (<a href="/en/tcf-canada-test-centres/" hreflang="en">la lista, en inglés</a>). En América Latina y
España, según los sitios web de los centros el 8 de octubre de 2026:</p>
<ul>
<li><a href="/es/tcf-canada-mexico/"><strong>México</strong></a>: cinco centros ofrecen el TCF Canada, de 4,800 a 6,500
pesos: el IFAL en la Ciudad de México, las Alianzas Francesas de Guadalajara, Puebla y Aguascalientes, y la UAEH en
Pachuca.</li>
<li><a href="/es/tcf-canada-colombia/"><strong>Colombia</strong></a>: las siete Alianzas Francesas, Bogotá y Medellín
incluidas, ofrecen el TCF Canada, de 1.050.000 pesos en Medellín y Pereira a 1.247.000 en Bogotá.</li>
<li><a href="/es/tcf-canada-argentina/"><strong>Argentina</strong></a>: cuatro centros anuncian el TCF Canada, entre ellos
Campus France en Buenos Aires, y ninguno publica el precio.</li>
<li><a href="/es/tcf-canada-chile/"><strong>Chile</strong></a>: el Instituto Francés de Chile (Santiago) y la Alianza
Francesa de Concepción, a 299.000 pesos.</li>
<li><a href="/es/tcf-canada-peru/"><strong>Perú</strong></a>: solo la Alianza Francesa de Lima, a 1,240 soles.</li>
<li><a href="/es/tcf-canada-ecuador/"><strong>Ecuador</strong></a>: las Alianzas Francesas de Cuenca (200 dólares) y de
Guayaquil (300 dólares).</li>
<li><a href="/es/tcf-canada-espana/"><strong>España</strong></a>: 11 de los 14 centros autorizados, de 275 a 287 €.</li>
</ul>
<p>Para el TEF Canada, el directorio de Le français des affaires sigue siendo la referencia. Lo que vimos al revisar los
centros TCF: en <strong>México</strong>, según la Federación de Alianzas Francesas, el TEF Canada se ofrece en las
Alianzas Francesas de Ciudad de México, Monterrey, Puebla, Oaxaca, Cuernavaca, San Luis Potosí y Texcoco; en
<strong>Argentina</strong>, la Alianza Francesa de Buenos Aires ofrece el TEF Canada, no el TCF; en
<strong>Perú</strong>, la Alianza Francesa de Lima lo vende —su sesión con todas las pruebas del 9 de noviembre de 2026
seguía a la venta el 8 de octubre—, igual que Alianzas de provincia como la de Arequipa; en <strong>Ecuador</strong>, la
Alianza Francesa de Quito no ofrece el TCF Canada y orienta hacia el TEF Canada, a 300 dólares.</p>

<h2 id="quebec">El caso de Quebec</h2>
<p>Si tu proyecto apunta a Quebec y no al nivel federal, todo cambia, y a tu favor. El Ministerio de Inmigración,
Francización e Integración de Quebec (MIFI) acepta <strong>ocho</strong> exámenes y diplomas: TCF Québec, TCF Canada,
TCF, DALF y DELF del lado de France Éducation international; TEFAQ, TEF Canada y TEF del lado de la CCI Paris
Île-de-France. Los resultados deben tener dos años o menos.</p>

<p>Sobre todo, el <strong>TCF Québec y el TEFAQ son modulares</strong>: eliges presentar una, dos, tres o cuatro pruebas.
Y la vertiente 2 del PSTQ (el programa de selección de trabajadores calificados de Quebec) y el requisito para el cónyuge
acompañante solo se refieren al oral. <strong>Puedes, entonces, presentar solo las dos pruebas orales</strong>: menos
preparación, menos riesgo y, a menudo, menos costo. En la UQTR, por ejemplo, las dos pruebas orales del TCF Québec cuestan
230 dólares canadienses, contra 440 por un TCF Canada completo en el mismo centro (consultado el 30 de julio de 2026).</p>

<p>Los umbrales del PSTQ, en la Escala quebequense (que no hay que confundir con el NCLC): vertiente 1, francés oral de
nivel 7 o más <em>y</em> francés escrito de nivel 5 o más. La tabla quebequense es mucho menos detallada que el NCLC: en el
TEF, el TEFAQ y el TEF Canada, igual que en las comprensiones del TCF, el tramo 400–499 corresponde a los niveles 7-8
(B2). Además, el PSTQ <strong>no exige inglés</strong>.</p>

<h2 id="versiones">Diferencia entre TCF y TEF: todas las versiones</h2>
<p>«TCF» y «TEF» no designan dos exámenes, sino dos <em>familias</em> de exámenes de dos organismos competidores:
<strong>France Éducation international</strong> para el TCF y <strong>Le français des affaires</strong> (CCI Paris
Île-de-France) para el TEF. Cada familia tiene <strong>cuatro versiones</strong>, cada una pensada para un trámite: TCF
tout public, TCF Canada, TCF Québec y TCF IRN; TEF Études, TEF Canada, TEFAQ y TEF IRN. Ninguna fuente oficial dice que
uno de los dos sea más fácil, y no se publica ninguna tasa de aprobación: la verdadera diferencia es la manera de
calificar.</p>
<ul>
<li><strong>Las versiones no son intercambiables.</strong> Para Express Entry solo valen las versiones Canada: el TCF tout
public, el TCF Québec y el TEFAQ no figuran en la lista de IRCC.</li>
<li><strong>La asimetría entre Canadá y Quebec funciona en un solo sentido.</strong> Quebec acepta el TCF Canada, pero
IRCC no acepta el TCF Québec. Si tu proyecto puede cambiar, la versión Canada cubre las dos vías; al revés, no.</li>
<li><strong>Solo dos versiones son modulares</strong>: el TCF Québec y el TEFAQ, en los que eliges de una a cuatro
pruebas. Para la ciudadanía canadiense, el TEF Canada también puede presentarse solo con la comprensión oral y la
expresión oral.</li>
<li><strong>No te prepares con la versión equivocada.</strong> El TCF tout public tiene una sección de «estructuras de la
lengua» que el TCF Canada no tiene, y 29 preguntas de comprensión en lugar de 39: entrenar con uno pensando en el otro es
prepararte para un examen que no vas a presentar.</li>
</ul>

<h2 id="elegir">Cómo elegir, en concreto</h2>
<ol>
<li><strong>Primero, verifica tu trámite.</strong> Inmigración económica federal: TCF Canada o TEF Canada, y punto.
Ciudadanía canadiense: el cuestionario de IRCC, consultado el 8 de octubre de 2026, menciona el TEF Canada y el TCF Canada
(guías anteriores nombraban más: DALF, DELF, TCFQ, TEFAQ, TEF IRN), y el nivel exigido es solo NCLC 4, únicamente en las dos pruebas orales, para los solicitantes de 18 a 54 años. Quebec: ocho
exámenes aceptados, y los modulares te abren puertas.</li>
<li><strong>Presenta un simulacro completo de cada uno</strong>, cronometrado y en condiciones reales. Es la única prueba
decisiva.</li>
<li><strong>Compara los NCLC obtenidos, no los puntajes brutos.</strong> No son comparables entre los dos exámenes.</li>
<li><strong>Mira tu habilidad más débil</strong> en cada simulación: es la que decide, no tu promedio.</li>
<li><strong>Elige aquel en el que tu punto débil sale mejor parado.</strong> Eso es todo.</li>
</ol>

<p>Para profundizar en los umbrales y los puntos, consulta nuestra guía del <a href="/es/tcf-canada/">examen TCF
Canada</a>. Si tu proyecto está en Francia y no en Canadá, se aplican otros exámenes: el B2 para la nacionalidad
francesa y el B1 para la tarjeta de residente; y si dudas entre un diploma y un test, mira
<a href="/es/certificado-de-frances/">qué certificado de francés elegir</a>.</p>
""",
    cta_h2="Haz un simulacro de cada uno antes de pagar 440 dólares canadienses",
    cta_p="""Simulacros cronometrados con el formato exacto del TCF Canada y del TEF Canada, conversión inmediata a NCLC por
prueba y corrección con IA de la expresión escrita y oral, en la app «TCF DELF TEF: Tests 2026». La app está en
español.""",
    faq=[("TCF Canada o TEF Canada: ¿cuál es más fácil?", "Ninguno de los dos es más fácil en sí mismo: ninguna fuente oficial lo dice y no se publica ninguna tasa de aprobación. Los dos llevan a la misma escala NCLC. Las diferencias que cuentan son de formato: el TCF Canada califica la expresión sobre 20, así que un solo punto puede cambiar tu nivel NCLC, mientras que el TEF la califica sobre 699 (450 en la columna «ancien score»), una escala mucho más fina. El TEF pide unas 280 palabras en 2 tareas de expresión escrita; el TCF, unas 300 a 450 palabras en 3 tareas. Presenta un simulacro de cada uno y quédate con aquel en el que tu puntaje sea más alto."),
         ("¿Qué examen de francés acepta IRCC para la residencia permanente (PR) y Express Entry?","Solo dos: el TEF Canada y el TCF Canada. Ni el DELF, ni el DALF, ni el TEF tout public se aceptan para la inmigración económica. Para la ciudadanía canadiense, el cuestionario de IRCC, consultado el 8 de octubre de 2026, menciona el TEF Canada y el TCF Canada; guías anteriores nombraban más (DALF, DELF, TCFQ, TEFAQ, TEF IRN), algunos solo si ya los habías presentado en un trámite de inmigración a Quebec: verifica la lista de IRCC al presentar tu solicitud."),
         ("¿Cuál es la diferencia entre el TCF y el TEF?", "Son dos exámenes competidores que miden lo mismo y que, salvo algunas excepciones, son reconocidos por las mismas autoridades. Cambia el organismo —France Éducation international para el TCF, Le français des affaires (CCI Paris Île-de-France) para el TEF— y, sobre todo, la manera de calificar: el TCF combina dos escalas, 699 para las comprensiones y 20 para las expresiones; el TEF pone sus cuatro pruebas en una sola escala de 699 (salvo el TEF IRN, sobre 499), y su constancia lleva una segunda columna, «Équivalence ancien score». Ninguna fuente oficial permite decir que uno sea más fácil: es esa diferencia de escala, no de dificultad, la que provoca la mayoría de los errores en los expedientes."),
         ("¿Qué puntajes del TEF ingreso en mi perfil de Express Entry?", "Solo los de la columna «Équivalence ancien score» de tu constancia, sea cual sea la fecha de tu examen. La constancia del TEF también tiene una columna sobre 699 —desde el 1 de octubre de 2019, y no desde la reforma de diciembre de 2023, como se lee a menudo—, pero esos no son los puntajes que espera IRCC. Es la primera causa de errores al llenar los perfiles de Express Entry."),
         ("¿Cuánto tiempo son válidos los resultados del TCF y del TEF Canada?", "Dos años para los dos exámenes. Pero la regla de IRCC es más estricta de lo que parece: tus resultados deben tener menos de dos años cuando llenas tu perfil de Express Entry y también cuando presentas tu solicitud de residencia permanente. Para el TEF, las condiciones de inscripción de Le français des affaires cuentan la validez desde la fecha de emisión de la constancia, no desde la fecha del examen, aunque su página de presentación dice «a partir de la fecha del examen»: toma la fecha menos favorable."),
         ("¿Cuánto hay que esperar para repetir el TCF o el TEF Canada?", "Veinte días para los dos. El número de intentos es ilimitado en el TCF Canada, con un plazo obligatorio de 20 días entre dos sesiones según las páginas del examen de France Éducation international (algunas de sus fichas en PDF dicen 30: confírmalo con tu centro). El TEF impone el mismo plazo de 20 días entre dos intentos de una misma prueba, en todas sus versiones. El rumor de un plazo de 30 días en el TEF es falso: esos 30 días son, en realidad, el plazo para presentar un recurso contra un resultado del TEF."),
         ("¿Cuánto cuestan el TCF Canada y el TEF Canada?", "No hay tarifa nacional: los dos organismos dejan que cada centro autorizado fije su precio. En los centros verificados en julio de 2026 se observan unos 220 a 245 euros en Europa y de 400 a 440 dólares canadienses en Canadá por un TCF Canada completo. En América Latina, el 8 de octubre de 2026, el TCF Canada costaba de 4,800 a 6,500 pesos en México, 299.000 pesos en Chile y 1,240 soles en Perú, y el TEF Canada, 300 dólares en la Alianza Francesa de Quito. Cuidado: muchos centros —entre ellos la Alianza Francesa de Montreal— no publican ninguna tarifa, y las cifras que les atribuyen los comparadores no tienen fuente. De todos modos, el precio no debería ser tu criterio para elegir entre los dos exámenes."),
         ("¿Dónde presentar el TEF Canada en México?", "Según la Federación de Alianzas Francesas de México, en las Alianzas Francesas de Ciudad de México, Monterrey, Puebla, Oaxaca, Cuernavaca, San Luis Potosí y Texcoco. El TCF Canada, el otro examen que acepta IRCC, se presenta en cinco centros del país, de 4,800 a 6,500 pesos: el IFAL en la Ciudad de México, las Alianzas Francesas de Guadalajara, Puebla y Aguascalientes, y la UAEH en Pachuca (<a href=\"/es/tcf-canada-mexico/\">el detalle, centro por centro</a>).")],
    also=[("/es/tcf-canada/", "Examen TCF Canada: formato, puntaje NCLC y preparación", "Las cuatro pruebas, la tabla NCLC completa y dónde presentarlo."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina: centros, precios y fechas."),
          ("/es/certificado-de-frances/", "¿Qué certificado de francés elegir?", "DELF, DALF, TCF o TEF: diploma de por vida o test válido dos años.")],
    sources="""<strong>Las tablas cambian.</strong> Este artículo está actualizado al 30 de julio de 2026 —los centros de América
Latina y España, al 8 de octubre de 2026— y no constituye asesoría migratoria. IRCC y el MIFI modifican con frecuencia
las tablas de conversión, los umbrales y los programas. Verifica siempre la tabla vigente en
<a href="https://www.canada.ca/en/immigration-refugees-citizenship.html" rel="noopener">canada.ca</a> y, para Quebec, en
<a href="https://www.quebec.ca/immigration" rel="noopener">quebec.ca</a> antes de inscribirte en un examen o de crear tu
perfil.""",
))
