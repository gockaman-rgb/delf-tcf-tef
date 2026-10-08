# -*- coding: utf-8 -*-
"""Pages pays en espagnol (/es/, make_pays.py) — traductions des pages /centres/ du 08/10/2026.

Même règle que pays_config.py : aucun fait nouveau. Chaque prix, date ou règle vient de la page française
(relevé du 8 octobre 2026) ; on traduit, on ne recherche pas. Espagnol d'Espagne pour l'Espagne
(variant "es-ES"), espagnol neutre d'Amérique latine ailleurs ("es-419"). Glossaire : i18n_glossary.md.
"""
from pays_i18n import NR as _NR, from_fr, releve, table

NR = _NR["es"]
CAP = ("Lo que mostraba el sitio web de cada centro el 8 de octubre de 2026{extra}. «Sin datos»: no publicado o no "
       "verificado; lo que diga el sitio del centro es lo que vale.")

PAGES = []

# ===========================================================================
# MÉXICO
# ===========================================================================
PAGES.append(from_fr(
    "tcf-mexique", "es", "es-419", "Mexique",
    slug="tcf-canada-mexico", country_name="México",
    crumb="TCF Canada en México",
    title="TCF Canada en México 2026: centros, precios y fechas",
    desc="Dónde presentar el TCF Canada en México: el IFAL en CDMX (5,150 pesos), las Alianzas Francesas de Guadalajara (4,950) y Puebla (4,800), la UAEH. Fechas.",
    h1="TCF Canada en México: los centros que lo ofrecen, los precios y las fechas",
    intro="""En México, {n} centros están autorizados para el TCF por France Éducation international, y <strong>cinco
ofrecían el TCF Canada</strong> el 8 de octubre de 2026: el <strong>IFAL</strong> en la Ciudad de México (5,150 pesos
en sesión de calendario, 6,500 en una fecha a solicitud), la <strong>Alianza Francesa de Guadalajara</strong> (4,950),
la de <strong>Puebla</strong> (4,800, a solicitud), la Universidad Autónoma del Estado de Hidalgo en Pachuca (5,800) y
la Alianza Francesa de Aguascalientes. Próximas sesiones de calendario: el <strong>27 de octubre</strong> en
Guadalajara, el <strong>28 de octubre</strong> y el 2 de diciembre en el IFAL.""",
    facts=["<strong>{n} centros autorizados</strong> (lista de FEI del 8 de octubre de 2026), <strong>5 que ofrecen el TCF Canada</strong>: el IFAL (Ciudad de México), las Alianzas Francesas de Guadalajara, Puebla y Aguascalientes, y la UAEH (Pachuca).",
           "Precio del TCF Canada: <strong>4,800 pesos</strong> en Puebla, <strong>4,950</strong> en Guadalajara, <strong>5,150</strong> en el IFAL (6,500 a solicitud) y <strong>5,800</strong> en la UAEH.",
           "Sesiones de calendario: Guadalajara, un martes al mes (<strong>27 de octubre, 24 de noviembre, 15 de diciembre</strong>); IFAL, <strong>28 de octubre</strong> (inscripciones del 5 al 21 de octubre) y <strong>2 de diciembre</strong> (del 9 al 25 de noviembre).",
           "<strong>A solicitud</strong>: en el IFAL, en Puebla (con diez días de anticipación, nunca en fin de semana) y en la UAEH; en Aguascalientes, a partir de cinco inscritos.",
           "El TCF Canada no aparece ni en Proulex, ni en las Alianzas Francesas de Guanajuato, Mexicali, San Luis Potosí y Zacatecas, ni en el CCLT de Tepic.",
           "Resultados en fecha fija en el IFAL (unas cuatro semanas) y en 15 días a tres semanas en Guadalajara, donde hay que esperar 20 días después de los resultados para volver a inscribirse."],
    stats=[("5", "centros con TCF Canada", "de {n} centros autorizados"), ("4,800-6,500", "pesos el TCF Canada", "según el centro y la modalidad"),
           ("27 oct.", "próxima sesión", "Guadalajara; IFAL el 28"), ("2 años", "de validez", "resultados en 2 a 4 semanas")],
    sections=[
        ("centros-tcf-canada", "Quién aplica el TCF Canada en México", releve([
            ("IFAL — Instituto Francés de América Latina (Ciudad de México)", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>5,150</strong> (sesión) · <strong>6,500</strong> (a solicitud) · IRN 4,800 · Québec 1,700 por prueba",
             "<strong>28/10</strong> (inscripciones del 5 al 21/10, resultados el 23/11) y <strong>02/12/2026</strong> (del 9 al 25/11, resultados el 04/01/2027); IRN y Québec a solicitud. En computadora."),
            ("Alianza Francesa de Guadalajara (Ciudad del Sol, Zapopan)", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>4,950</strong> · IRN 4,250 · Québec 5,000 · fecha fuera de calendario +750",
             "Diez martes en 2026: <strong>27/10, 24/11, 15/12</strong>; Québec el 10/11. Inscripción por WhatsApp o por correo. En computadora."),
            ("Alianza Francesa de Puebla", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>4,800</strong> · IRN 3,600 · Québec 1,200 por prueba",
             "A solicitud, con al menos diez días de anticipación, nunca en fin de semana; pago en la tienda en línea; cuotas no reembolsables. En computadora."),
            ("UAEH — Universidad Autónoma del Estado de Hidalgo (Pachuca)", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>5,800</strong> · IRN 4,600 · Québec 1,800 por prueba",
             "A solicitud; el formulario y el comprobante de pago se entregan en persona, en el Centro de Lenguas."),
            ("Alianza Francesa de Aguascalientes", "<strong>Canada</strong>, tout public, IRN, Québec", "ninguna tarifa publicada",
             "Abre sesión a partir de cinco inscritos; ninguna fecha publicada."),
            ("Proulex (Guadalajara)", "solo tout public", "tarifas publicadas con fecha de 2020", "Páginas de exámenes antiguas: confírmalo con el centro."),
            ("Alianza Francesa de Guanajuato", "TCF, Québec, IRN — <strong>sin Canada</strong>", "ninguna tarifa publicada", "Sesiones personalizadas todo el año, según la Federación de Alianzas Francesas."),
            ("Alianza Francesa de San Luis Potosí", "TCF, Québec, IRN — <strong>sin Canada</strong>", "ninguna tarifa publicada", "Sesiones personalizadas y calendario definido, según la Federación: fechas por confirmar."),
            ("Alianza Francesa de Zacatecas", "TCF, Québec, IRN — <strong>sin Canada</strong>", "ninguna tarifa publicada", "Sesiones personalizadas todo el año."),
            ("Alianza Francesa de Mexicali", "ningún TCF en su sitio web", "—", "El sitio solo habla del DELF; sus datos de contacto no coinciden con los de FEI."),
            ("Colegio de Ciencias y Letras de Tepic", "ningún TCF en su sitio web", "—", "El sitio solo menciona certificaciones de inglés."),
        ], "es-419", CAP.format(extra=", precios en pesos mexicanos (MXN)"))),
        ("inscripcion", "Cómo inscribirte en el TCF Canada en México", """<p>El trámite tiene tres pasos: <strong>fijar la fecha</strong> con el centro —o inscribirte durante el periodo
de una sesión de calendario—, <strong>llenar el formulario</strong> —el IFAL y la UAEH piden el número de pasaporte
para el TCF Canada— y <strong>pagar</strong>: transferencia o depósito bancario en el IFAL, tienda en línea en Puebla,
expediente entregado en persona en la UAEH. En Puebla, la inscripción se completa en 72 horas con el pasaporte
escaneado, cuyo original se presenta el día del examen. El TCF se presenta en computadora en el IFAL, en Guadalajara
y en Puebla; la expresión oral, cara a cara.</p>

<p>Puebla precisa que las cuotas no son reembolsables —se puede pasar a la sesión siguiente con certificado
médico—; los demás centros no publican ninguna regla. En Guadalajara hay que esperar 20 días después de los
resultados para volver a inscribirse. Los resultados salen en una fecha fija en el IFAL —el 23 de noviembre para la
sesión del 28 de octubre— y en 15 días a tres semanas en Guadalajara. La constancia de resultados es válida dos
años; desde el 1 de septiembre de 2026, FEI ya no acepta solicitudes de recalificación.</p>

<p>La elección depende del calendario: una sesión de calendario cuesta menos que una fecha a solicitud —5,150
contra 6,500 pesos en el IFAL, 750 pesos más fuera de calendario en Guadalajara—, pero en Puebla una fecha a
solicitud se consigue en diez días. El TEF Canada, el otro examen aceptado por IRCC, se ofrece, según la Federación,
en las Alianzas Francesas de Ciudad de México, Monterrey, Puebla, Oaxaca, Cuernavaca, San Luis Potosí y Texcoco.</p>"""),
    ],
    list_title="Los {n} centros TCF autorizados, ciudad por ciudad",
    faq=[("¿Dónde presentar el TCF Canada en la Ciudad de México?", "En el IFAL, el Instituto Francés de América Latina (Río Nazas 43, colonia Cuauhtémoc): 5,150 pesos en sesión de calendario —las próximas, el 28 de octubre (inscripciones del 5 al 21 de octubre) y el 2 de diciembre de 2026 (del 9 al 25 de noviembre)— y 6,500 pesos en una fecha a solicitud. La Alianza Francesa de Ciudad de México no aplica el TCF."),
         ("¿Cuánto cuesta el TCF Canada en México?", "De 4,800 pesos (Alianza Francesa de Puebla) a 6,500 pesos (IFAL, fecha a solicitud): 4,950 en la Alianza Francesa de Guadalajara, 5,150 en el IFAL en sesión de calendario y 5,800 en la UAEH. Precios consultados el 8 de octubre de 2026."),
         ("¿Dónde presentar el TCF Canada en Guadalajara?", "En la Alianza Francesa de Guadalajara, en el plantel Ciudad del Sol (Zapopan): 4,950 pesos, un martes al mes —27 de octubre, 24 de noviembre y 15 de diciembre de 2026—, con inscripción por WhatsApp o por correo. Proulex, el otro centro autorizado de la ciudad, solo publica el TCF tout public."),
         ("¿Puedo presentar el TCF Canada en la fecha que yo elija?", "Sí: en el IFAL (6,500 pesos), en la Alianza Francesa de Puebla (con al menos diez días de anticipación, de lunes a viernes) y en la UAEH; en Guadalajara, una fecha fuera de calendario cuesta 750 pesos más. Aguascalientes abre una sesión desde cinco inscritos."),
         ("¿IRCC acepta el TCF Canada presentado en México?", "Sí: la constancia de resultados la emite France Éducation international, sea cual sea el centro autorizado, y es válida dos años. Solo verifica que te inscribas en el TCF Canada y no en el TCF tout public.")],
    also=[("/es/delf-mexico/", "DELF y DALF en México", "El calendario y las tarifas nacionales, 71 centros."),
          ("/es/tcf-canada-colombia/", "TCF Canada en Colombia", "Las siete Alianzas Francesas autorizadas."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="sitios del IFAL, de las Alianzas Francesas de Guadalajara, Puebla, Aguascalientes, Guanajuato, Mexicali, San Luis Potosí y Zacatecas, de la Federación de Alianzas Francesas de México, de Proulex, de la UAEH y del CCLT de Tepic (páginas del TCF, tarifas y calendarios 2026, formularios, tiendas en línea), consultados el 8 de octubre de 2026.",
))


# ===========================================================================
# ESPAÑA — TCF (es-ES)
# ===========================================================================
PAGES.append(from_fr(
    "tcf-espagne", "es", "es-ES", "Espagne",
    slug="tcf-canada-espana", country_name="España",
    crumb="TCF Canada en España",
    title="TCF Canada en España: Madrid, Barcelona, precios y fechas",
    desc="Dónde hacer el TCF Canada en España: 11 de 14 centros autorizados lo ofrecen, de 275 a 287 €, en Madrid, Barcelona, Valencia, Sevilla… Fechas y matrícula.",
    h1="TCF Canada en España: los centros, los precios y las próximas convocatorias",
    intro="""En España, {n} centros están autorizados para el TCF por France Éducation international, y <strong>once
ofrecen el TCF Canada</strong> según su web el 8 de octubre de 2026: los Institut français de Madrid, Barcelona, Valencia
y Bilbao, las Alianzas Francesas de Madrid, Málaga, Oviedo, Cartagena y Valladolid, y el CELF y el ILF en Sevilla.
Tres niveles de precio: <strong>287 €</strong> en los Institut français y en el ILF, <strong>281 €</strong> en las
Alianzas Francesas, <strong>275 €</strong> en el CELF. La frecuencia va de una convocatoria por semana —Valladolid,
Sevilla— a cuatro o cinco al año.""",
    facts=["<strong>{n} centros autorizados</strong> (lista de FEI del 8 de octubre de 2026), de los que <strong>11 ofrecen el TCF Canada</strong>; no hay TCF Canada en la Alianza Francesa de Santiago de Compostela, y no hay nada publicado para 2026 en Vigo ni en la Universidad Pública de Navarra.",
           "Precio del TCF Canada en 2026: <strong>287 €</strong> (Institut français, ILF de Sevilla), <strong>281 €</strong> (Alianzas Francesas), <strong>275 €</strong> (CELF Sevilla); TCF IRN: 278, 269 y 260 €.",
           "Frecuencia: <strong>cada semana</strong> en Valladolid, todos los lunes y viernes en el ILF de Sevilla, dos veces al mes en el CELF, una vez al mes en Oviedo; de cuatro a diez convocatorias al año en los demás centros.",
           "Próximas convocatorias del TCF Canada: Barcelona, 10-13 de noviembre; Málaga, 11-13 de noviembre; Valencia, 12-13 de noviembre; Oviedo, 13 de noviembre; Alianza Francesa de Madrid, 19 de noviembre; Cartagena, 23 y 25 de noviembre; Institut français de Madrid, 17-18 de diciembre de 2026.",
           "<strong>30 días</strong> entre dos convocatorias, recuerda el Centro Nacional de Exámenes; el día del TCF Canada se toma una foto del candidato.",
           "Certificado en PDF por correo electrónico, de dos a tres semanas después del examen; en varios centros, resultado provisional el mismo día, al terminar la prueba en ordenador."],
    stats=[("11", "centros con TCF Canada", "de {n} centros autorizados"), ("281-287 €", "el TCF Canada", "275 € en el CELF Sevilla"),
           ("30 días", "entre dos convocatorias", "norma del centro nacional"), ("2-3 sem.", "para el certificado", "PDF por correo electrónico")],
    sections=[
        ("centros-tcf-canada", "Quién organiza el TCF Canada en España", releve([
            ("Institut français de Barcelona", "<strong>Canada</strong>, tout public (opción DAP), IRN",
             "Canada <strong>287 €</strong> · IRN 278 € · tout public 125 € + 75 € por prueba",
             "<strong>10-13 de noviembre</strong> (matrícula del 1 al 19 de octubre; hasta el 11 para la expresión escrita en papel); no hay convocatoria en diciembre. En ordenador; el día lo fija el centro."),
            ("Institut français de Bilbao", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>287 €</strong> · IRN 278 € · tout public 125 €",
             "Viernes <strong>13 de noviembre</strong> (matrícula del 1 al 13 de octubre); el 8 de octubre, la tienda online solo vendía el tout public. En papel."),
            ("Alianza Francesa de Cartagena", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>281 €</strong> · IRN 269 € · tout public 123 € + 73 €",
             "Nueve convocatorias en 2026; la próxima, el <strong>23 y el 25 de noviembre</strong> (matrícula del 3 al 10 de noviembre): ficha, transferencia y copia del DNI por correo electrónico."),
            ("Alianza Francesa de Madrid", "<strong>Canada</strong>, tout public, IRN",
             "Canada <strong>281 €</strong> · IRN 269 € · tout public 123 € + 73 €",
             "Jueves <strong>19 de noviembre</strong> (matrícula del 2 al 13 de noviembre); septiembre aparecía como completo. En ordenador."),
            ("Institut français de Madrid", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>287 €</strong> · IRN 278 € · tout public 125 € + 75 €",
             "Seis convocatorias al año: <strong>17-18 de diciembre</strong> (matrícula del 15 al 30 de noviembre). Resultado provisional el mismo día; en ordenador."),
            ("Alianza Francesa de Málaga", "<strong>Canada</strong>, tout public, IRN",
             "Canada <strong>281 €</strong> · IRN 269 € · tout public 123 €",
             "<strong>11-13 de noviembre</strong> (matrícula del 1 al 31 de octubre) y 9-11 de diciembre (del 2 al 30 de noviembre). Tarjeta, efectivo o transferencia. En ordenador."),
            ("Alianza Francesa de Oviedo", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>281 €</strong> · IRN 269 € · tout public 123 €",
             "Una convocatoria al mes, salvo en agosto: 16 de octubre, <strong>13 de noviembre</strong> (matrícula del 27 de octubre al 7 de noviembre), 11 de diciembre. En ordenador."),
            ("Universidad Pública de Navarra (Pamplona)", "ningún TCF en su web", NR,
             "El TCF no aparece en ninguna parte de la web de la universidad: confírmalo con ella."),
            ("Alianza Francesa de Santiago de Compostela", "tout public, IRN, Québec — <strong>sin Canada</strong>", "IRN 269 € · tout public 123 €",
             "Convocatorias bajo petición, por teléfono o por correo electrónico."),
            ("CELF Sevilla", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>275 €</strong> · IRN 260 € · tout public 120 € (240 € el examen completo)",
             "Dos fechas al mes en ordenador hasta marzo de 2027 (9 y 23 de octubre, 6 y 27 de noviembre, 11 de diciembre…), en papel el 20 de noviembre; matrícula contactando con el centro."),
            ("Instituto de Lengua Francesa (Sevilla)", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>287 €</strong> · IRN 278 € · tout public 125 €",
             "<strong>Todos los lunes y viernes</strong>; la matrícula se cierra el lunes anterior al examen. Formulario, transferencia y correo electrónico. En ordenador."),
            ("Institut français de Valencia", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>287 €</strong> · IRN 278 € · tout public 125 € + 75 €",
             "Diez convocatorias en 2026: <strong>12-13 de noviembre</strong> (matrícula del 14 de octubre al 4 de noviembre), 14-15 de diciembre (del 14 de noviembre al 3 de diciembre). Pago online; en ordenador."),
            ("Alianza Francesa de Valladolid", "<strong>Canada</strong>, tout public, IRN, Québec",
             "Canada <strong>281 €</strong> · IRN 269 € · Québec 291 €",
             "<strong>Cada semana</strong>, salvo en vacaciones; matrícula por correo electrónico, con al menos 10 días de antelación. En ordenador."),
            ("Alianza Francesa de Vigo", "nada publicado para 2026", NR,
             "La página del TCF sigue con el calendario de 2025: confírmalo con la Alianza."),
        ], "es-ES", "Lo que mostraba la web de cada centro el 8 de octubre de 2026. «Sin datos»: no publicado o no verificado; lo que diga la web del centro es lo que vale.") + """
<p>Salvo el CELF, ningún centro publicaba fechas de 2027 el 8 de octubre de 2026. El Centro de Lenguas Modernas de la
Universidad de Granada también organiza el TCF (205 €, próxima fecha el 25 de enero de 2027) sin figurar en la lista
TCF de FEI: pregúntale qué versión organiza antes de matricularte.</p>"""),
        ("matricula", "Cómo matricularte en el TCF Canada en España", """<p>Conviven dos sistemas. Los Institut français (Madrid, Barcelona, Valencia, Bilbao) y la Alianza Francesa de
Málaga venden el examen en una <strong>tienda online</strong>, con pago con tarjeta; las Alianzas de Cartagena, Oviedo
y Santiago, igual que el ILF de Sevilla, piden una <strong>ficha de matrícula, una transferencia y una copia del
documento de identidad</strong> por correo electrónico; en Valladolid y en el CELF basta con ponerse en contacto con el
centro. Para el TCF Canada, matricúlate con el pasaporte de tu expediente de IRCC: el Centro Nacional de Exámenes exige
una foto del candidato el día del examen, y no se puede quedar exento de ninguna prueba.</p>

<p>Las normas se parecen: no se devuelve el dinero una vez cerrada la matrícula; aplazamiento solo con certificado
médico (en Barcelona, hay que pedirlo en los 3 días siguientes a la ausencia); gastos de gestión de 30 € en Valencia y
de 40 € en el ILF cuando se acepta una anulación. Tienen que pasar <strong>30 días</strong> entre dos convocatorias del
mismo examen. El certificado llega en PDF por correo electrónico, casi siempre de dos a tres semanas después del
examen, y varios centros entregan un resultado provisional nada más terminar la prueba en ordenador. Desde el 1 de
septiembre de 2026, FEI ya no acepta solicitudes de recalificación.</p>

<p>Desconfía de las webs que ofrecen «comprar» un certificado TCF «sin examen», con una «puntuación garantizada»: nos
encontramos con una al revisar estos precios. Es un fraude; un certificado solo se obtiene haciendo el examen en un
centro autorizado.</p>"""),
    ],
    list_title="Los {n} centros TCF autorizados, ciudad por ciudad",
    faq=[("¿Dónde hacer el TCF Canada en Madrid?", "En el Institut français de Madrid (calle Marqués de la Ensenada, 12; 287 €, próxima convocatoria el 17 y el 18 de diciembre de 2026, matrícula del 15 al 30 de noviembre) o en la Alianza Francesa de Madrid (Cuesta de Santo Domingo, 13; 281 €, próxima convocatoria el 19 de noviembre, matrícula del 2 al 13 de noviembre). Datos consultados el 8 de octubre de 2026."),
         ("¿Dónde hacer el TCF Canada en Barcelona?", "En el Institut français de Barcelona (carrer Moià, 8), el único centro TCF de la ciudad: 287 €, en ordenador, próxima convocatoria del 10 al 13 de noviembre de 2026, matrícula del 1 al 19 de octubre. No hay convocatoria en diciembre de 2026, y el 8 de octubre no había ninguna fecha de 2027 publicada."),
         ("¿Cuánto cuesta el TCF Canada en España?", "287 € en los Institut français y en el ILF de Sevilla, 281 € en las Alianzas Francesas y 275 € en el CELF Sevilla (tarifas de 2026 consultadas el 8 de octubre de 2026)."),
         ("¿Dónde hacer el TCF Canada lo antes posible?", "En la Alianza Francesa de Valladolid, que abre una convocatoria cada semana (matrícula con al menos 10 días de antelación), o en el ILF de Sevilla, que las organiza todos los lunes y viernes. El CELF Sevilla ofrece dos fechas al mes en ordenador."),
         ("¿Cuánto tiempo hay que esperar para repetir el TCF Canada?", "Treinta días entre dos convocatorias del mismo examen, según el Centro Nacional de Exámenes, como recuerdan el Institut français de Madrid, el de Valencia y el CELF Sevilla.")],
    also=[("/es/delf-espana/", "DELF y DALF en España", "El calendario nacional de 2027 y una tarifa única."),
          ("/es/tcf-canada-mexico/", "TCF Canada en México", "Cinco centros: el IFAL, Guadalajara, Puebla, Pachuca y Aguascalientes."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="webs de los 14 centros de la lista —Institut français de Barcelona, Bilbao, Madrid y Valencia; Alianzas Francesas de Cartagena, Madrid, Málaga, Oviedo, Santiago de Compostela, Valladolid y Vigo; CELF e ILF de Sevilla; Universidad Pública de Navarra (páginas del TCF, calendarios y tarifas de 2026, tiendas online, condiciones generales)— y del Centro Nacional de Exámenes (delf-dalf.es), consultadas el 8 de octubre de 2026.",
    notes={"bilbao-institut-francais-d-espagne-delegation-de-bilbao": "En papel; el 8 de octubre, la tienda online solo vendía el tout public para el 13 de noviembre."},
))

# ===========================================================================
# ESPAÑA — DELF (es-ES)
# ===========================================================================
PAGES.append(from_fr(
    "delf-espagne", "es", "es-ES", "Espagne",
    slug="delf-espana", country_name="España",
    crumb="DELF en España",
    title="Examen DELF en España: fechas 2027, precios y {n} centros",
    desc="Examen DELF en España: fechas 2027 y mismo precio en Madrid, Sevilla, Valencia y los 32 centros (B2: 192 €). Matrícula para febrero hasta el 9 de enero.",
    h1="DELF y DALF en España: los {n} centros, el calendario de 2027 y los precios",
    intro="""En España, el DELF y el DALF tienen <strong>un calendario y unos precios nacionales</strong>: el Centro Nacional
de Exámenes (delf-dalf.es), vinculado a la Embajada de Francia, fija las mismas fechas y las mismas tarifas en los {n}
centros de examen. La convocatoria de octubre de 2026 está cerrada; la próxima es la de <strong>febrero de 2027</strong>,
con matrícula del <strong>1 de diciembre de 2026 al 9 de enero de 2027</strong>. En 2027, el DELF B2 cuesta
<strong>192 €</strong>; el B1, 162 €, y el DALF C1, 249 €. Primero, el calendario, las tarifas y la matrícula; después,
los centros, comunidad por comunidad.""",
    facts=["<strong>{n} centros de examen</strong> (lista de FEI del 8 de octubre de 2026), coordinados por el Centro Nacional de Exámenes del Institut français de España.",
           "Un <strong>calendario nacional</strong>: mismos días, mismas horas y mismos plazos de matrícula en todas partes, con cuatro convocatorias al año para adultos, tres junior, dos Prim y una escolar.",
           "Próxima convocatoria: <strong>febrero de 2027</strong> (pruebas escritas del 10 al 13 de febrero), matrícula del <strong>1 de diciembre de 2026 al 9 de enero de 2027</strong>; después, junio, septiembre y octubre de 2027.",
           "Precios nacionales de 2027: <strong>A1 89 · A2 118 · B1 162 · B2 192 · C1 249 · C2 259 €</strong> (de 87 a 256 € en 2026).",
           "Los diplomas están reconocidos por la <strong>CRUE</strong>, la conferencia de rectores, para la acreditación de idiomas en las universidades españolas.",
           "Resultados en fecha fija (17 de marzo de 2027 para la convocatoria de febrero); el diploma llega de dos a tres meses después de la convocatoria."],
    stats=[("{n}", "centros de examen", "lista de FEI del 8 de octubre de 2026"), ("192 €", "el DELF B2 en 2027", "mismo precio en todos los centros"),
           ("9 ene.", "cierre de la matrícula", "para la convocatoria de febrero de 2027"), ("4", "convocatorias para adultos al año", "febrero, junio, septiembre, octubre")],
    sections=[
        ("calendario", "El calendario nacional de 2027", table(
            "Calendario DELF-DALF 2027 del Centro Nacional de Exámenes (PDF del 22 de septiembre de 2026), consultado el 8 de octubre de 2026: fechas de las pruebas escritas del DELF tout public y del DALF.",
            ["Convocatoria", "Matrícula", "A1", "A2", "B1", "B2", "C1", "C2", "Resultados"],
            [("<strong>Febrero de 2027</strong>", "<strong>1 dic. 2026 – 9 ene. 2027</strong>", "10/02", "12/02", "12/02", "11/02", "10/02", "11/02", "17 de marzo"),
             ("Junio de 2027", "1 de marzo – 16 de abril", "01/06", "03/06", "03/06", "02/06", "01/06", "02/06", "19 de julio"),
             ("Septiembre de 2027", "1 de julio – 1 de sept.", "28/09", "29/09", "29/09", "28/09", "27/09", "30/09", "2 de noviembre"),
             ("Octubre de 2027", "30 de agosto – 22 de sept.", "21/10", "21/10", "20/10", "19/10", "18/10", "21/10", "13 de diciembre")]) + """
<p>Las pruebas orales se reparten a lo largo de varias semanas en torno a las escritas. La convocatoria de septiembre
está reservada a los adultos y al DALF. DELF junior: 13 de febrero, 5 y 12 de junio y 23 de octubre de 2027; DELF Prim:
21 de mayo o 10 de junio de 2027 (matrícula del 1 de marzo al 16 de abril); DELF escolar: 28 y 29 de abril de 2027,
reservado al alumnado de centros públicos con convenio. No todos los centros abren todas las convocatorias, y algunos
cierran antes la matrícula: la Universidad de Castilla-La Mancha cierra la de febrero el 2 de enero, y el Institut
français de Barcelona, el 10 de enero. La convocatoria de octubre de 2026 (pruebas escritas del 19 al 24 de octubre)
está cerrada; sus resultados se publican el 10 de diciembre de 2026.</p>"""),
        ("precios", "¿Cuánto cuesta el DELF en España?", table(
            "Tarifas nacionales del Centro Nacional de Exámenes: tabla de 2027 (PDF del 22 de septiembre de 2026) y tabla de 2026 tomada de los documentos de varios centros, consultadas el 8 de octubre de 2026.",
            ["Examen", "2026", "2027"],
            [("DELF A1", "87 €", "89 €"), ("DELF A2", "115 €", "118 €"), ("DELF B1", "160 €", "162 €"),
             ("<strong>DELF B2</strong>", "<strong>188 €</strong>", "<strong>192 €</strong>"), ("DALF C1", "244 €", "249 €"), ("DALF C2", "256 €", "259 €"),
             ("DELF Prim A1.1 · A1 · A2", "68 · 87 · 115 €", "69 · 89 · 118 €"),
             ("DELF escolar A1 · A2 · B1 · B2", "—", "66,75 · 88,50 · 121,50 · 144 €")], wide=False) + """
<p>El CNE precisa que son exactamente las mismas tarifas en todos los centros, fijadas a nivel nacional por el
servicio de cooperación de la Embajada; el DELF junior cuesta lo mismo que el tout public. Hay descuentos locales: la
Universidad de Cádiz cobra 94 € por el B2 a sus estudiantes de último curso. Única diferencia encontrada: la Alianza
Francesa de Vigo anunciaba para octubre de 2026 un junior B1 a 157 € y un B2 a 184 €.</p>"""),
        ("matricula", "Matrícula, resultados y diploma", """<p>Te matriculas <strong>en un centro</strong>, nunca en el CNE: online en los Institut français, en las
Alianzas Francesas de Madrid y Málaga y en las universidades de Navarra y Cádiz; con ficha y transferencia enviadas por
correo electrónico en Burgos, Gijón, Salamanca, Las Palmas, Oviedo o Vigo; solo en persona en Santander. La matrícula
solo es efectiva con el pago. El día del examen: DNI, NIE, pasaporte o permiso de conducir, y la citación impresa; no se
admite a ningún candidato una vez empezadas las pruebas.</p>

<p>Los resultados se publican en la fecha fijada para cada convocatoria; el diploma llega de dos a tres meses después
de la convocatoria según el CNE (de tres a cuatro según algunos centros), y se puede pedir un certificado provisional.
Hacen falta 50 puntos sobre 100, sin ninguna nota inferior a 5 sobre 25 en una prueba; el diccionario está prohibido en
el DELF. La norma más extendida: no se devuelve el dinero, pero se puede pasar a la convocatoria siguiente por un
motivo médico o de fuerza mayor justificado; los Institut français de Madrid y de Bilbao conceden 14 días de
desistimiento, y el de Valencia devuelve el importe hasta el cierre de la matrícula, menos 30 €.</p>

<p>El CNE destaca los usos del diploma en España: está reconocido por la CRUE para la acreditación de idiomas en las
universidades; según el CNE, el B1 permite acreditar el nivel exigido para el título de <em>grado</em> en la mayoría de
las comunidades autónomas, y el B2 es el mínimo requerido para una beca Erasmus.</p>"""),
    ],
    list_title="Los {n} centros de examen, comunidad por comunidad",
    faq=[("¿Cuándo es la próxima convocatoria del DELF en España?", "En febrero de 2027: DALF C1 y DELF A1 el 10 de febrero, B2 y C2 el 11, B1 y A2 el 12, DELF junior el 13. La matrícula está abierta del 1 de diciembre de 2026 al 9 de enero de 2027 en todos los centros —algunos la cierran antes—, y los resultados se publican el 17 de marzo de 2027."),
         ("¿Cuánto cuesta el DELF B2 en España?", "192 € en 2027 (188 € en 2026), en todos los centros: la tarifa la fija a nivel nacional el servicio de cooperación de la Embajada de Francia. El DALF C1 cuesta 249 €, y el C2, 259 €."),
         ("¿El precio del examen DELF cambia de un centro a otro?", "No: el Centro Nacional de Exámenes aplica exactamente las mismas tarifas en todas partes. Solo cambian los descuentos propios de un centro, como los 94 € de la Universidad de Cádiz para sus estudiantes de último curso."),
         ("¿Las universidades españolas reconocen el DELF?", "Sí: los diplomas DELF y DALF figuran en la tabla de equivalencias de la CRUE, la Conferencia de Rectores de las Universidades Españolas, que también admite el TCF tout public por tramos de puntuación. Solo se aceptan los exámenes hechos de forma presencial."),
         ("¿Cuándo llega el diploma del DELF en España?", "De dos a tres meses después de la convocatoria, según el Centro Nacional de Exámenes (de tres a cuatro según algunos centros). Puedes pedir un certificado provisional en cuanto se publican los resultados.")],
    also=[("/es/tcf-canada-espana/", "TCF Canada en España", "11 centros, de 275 a 287 €, y las próximas convocatorias."),
          ("/es/delf-mexico/", "DELF y DALF en México", "El calendario y las tarifas nacionales, 71 centros."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="web del Centro Nacional de Exámenes (delf-dalf.es: calendarios de 2026 y 2027, tarifas, preguntas frecuentes, matrícula, DELF escolar), tabla de equivalencias de la CRUE para el francés y webs de los centros de examen (calendarios, tarifas y condiciones del DELF-DALF), consultadas el 8 de octubre de 2026.",
    notes={"carthagene-alliance-francaise-de-cartagena": "La web que indicaba FEI (afcartagena.org, no el enlace de arriba) llevaba el 8 de octubre de 2026 a una página sin relación, sobre transferencias de dinero: no la uses. También hay convocatorias en Molina de Segura y Alicante.",
           "vitoria-gasteiz-alliance-francaise-de-vitoria": "La web que indica FEI ya no responde, y el Centro Nacional de Exámenes oculta esta Alianza en su lista: estado por confirmar.",
           "ciudad-real-universidad-de-castilla-la-mancha": "Cuatro campus: Albacete, Ciudad Real, Cuenca y Toledo; la matrícula de febrero de 2027 se cierra ya el 2 de enero.",
           "santander-alliance-francaise-de-santander": "Matrícula solo en persona.",
           "logrono-fundacion-universidad-de-la-rioja": "En 2027, solo la convocatoria de junio; matrícula por correo electrónico."},
))

# ===========================================================================
# MÉXICO — DELF (es-419)
# ===========================================================================
PAGES.append(from_fr(
    "delf-mexique", "es", "es-419", "Mexique",
    slug="delf-mexico", country_name="México",
    crumb="DELF en México",
    title="Examen DELF en México 2026: fechas, precios y {n} centros",
    desc="Examen DELF y DALF en México: fechas y tarifas nacionales del IFAL, sesión de noviembre de 2026 (inscripciones hasta el 23 de octubre), B2 a 2,500 pesos.",
    h1="DELF y DALF en México: los {n} centros, el calendario y los precios de 2026",
    intro="""En México, el DELF y el DALF tienen un calendario y unas tarifas <strong>nacionales</strong>, que el IFAL
(Instituto Francés de América Latina) fija cada año y que aplican los {n} centros de examen: Alianzas Francesas,
universidades, escuelas. Próxima sesión tout public: pruebas escritas del <strong>9 al 13 de noviembre de 2026</strong>,
inscripciones del <strong>5 al 23 de octubre</strong>, resultados el 14 de diciembre. El DELF B2 cuesta <strong>2,500
pesos</strong> en todas partes, y 1,500 para los estudiantes de las universidades tecnológicas y de las escuelas
normales de la SEP.""",
    facts=["<strong>{n} centros de examen</strong> (lista de FEI del 8 de octubre de 2026): una treintena de Alianzas Francesas, el IFAL, universidades (UNAM, IPN, universidades estatales y tecnológicas) y escuelas.",
           "Calendario nacional: tout public en febrero, junio, septiembre y <strong>noviembre</strong>; junior en marzo, abril, mayo y octubre; Prim en junio.",
           "Sesión de noviembre de 2026: inscripciones del <strong>5 al 23 de octubre</strong>, pruebas escritas del 9 al 13 de noviembre (A1 y C2 el 9, A2 el 10, B1 el 11, B2 el 12, C1 el 13), resultados el <strong>14 de diciembre</strong>.",
           "Tarifas nacionales 2026: <strong>A1 1,445 · A2 1,575 · B1 1,800 · B2 2,500 · C1 3,500 · C2 4,000 pesos</strong>; tarifas reducidas para las universidades tecnológicas y las escuelas normales.",
           "Según la Federación de Alianzas Francesas, los diplomas DELF-DALF están reconocidos por la SEP a través de la norma CENNI.",
           "No hay reembolsos ni traspasos de la inscripción; el diploma se recoge en persona o a través de un tercero con carta poder simple."],
    stats=[("{n}", "centros de examen", "lista de FEI del 8 de octubre de 2026"), ("2,500", "pesos el DELF B2", "tarifa nacional 2026"),
           ("23 oct.", "cierre de inscripciones", "sesión del 9 al 13 de noviembre"), ("14 dic.", "resultados", "de la sesión de noviembre")],
    sections=[
        ("calendario", "El calendario nacional 2026", table(
            "Calendario de las sesiones DELF-DALF 2026 en México (versión 2 del documento del IFAL), consultado el 8 de octubre de 2026. Las pruebas orales se reparten a lo largo de tres semanas en torno a las escritas.",
            ["Sesión", "Inscripciones", "Pruebas escritas", "Resultados"],
            [("Tout public, febrero", "5-31 de enero", "16-20 de febrero", "13 de marzo"),
             ("Junior, marzo", "26 de enero – 13 de febrero", "2-5 de marzo", "13 de abril"),
             ("Junior, abril", "16 de febrero – 6 de marzo", "20-23 de abril", "14 de mayo"),
             ("Junior y escolar, mayo", "17-30 de abril", "18-21 de mayo", "26 de junio"),
             ("Prim, junio", "27 de abril – 15 de mayo", "1-3 de junio", "3 de julio"),
             ("Tout public, junio", "11-29 de mayo", "15-19 de junio", "24 de julio"),
             ("Tout public, septiembre", "10-28 de agosto", "21-25 de septiembre", "23 de octubre"),
             ("Junior y escolar, octubre", "7-25 de septiembre", "12-15 de octubre", "20 de noviembre"),
             ("<strong>Tout public, noviembre</strong>", "<strong>5-23 de octubre</strong>", "<strong>9-13 de noviembre</strong>", "<strong>14 de diciembre</strong>")], wide=False) + """
<p>La Alianza Francesa de Guadalajara explica que el IFAL establece este calendario cada año a nivel nacional y que se
aplica en todo México; la de San Luis Potosí agrega que las fechas y las tarifas no se pueden modificar. No todos los
centros abren todas las sesiones —el IFAL sí las abre todas—; en la ENALLT-UNAM, la sesión de noviembre solo ofrece el
B1, el B2 y el C1. El calendario 2027 no estaba publicado el 8 de octubre de 2026.</p>"""),
        ("precios", "¿Cuánto cuesta el DELF en México?", table(
            "Tabla nacional de tarifas 2026 para México, en pesos mexicanos (MXN), reproducida por el IFAL, las Alianzas Francesas de Ciudad de México, Guadalajara, Aguascalientes y Puebla, la ENALLT-UNAM y la UAEH, consultada el 8 de octubre de 2026.",
            ["Examen", "Tarifa estándar", "Universidades tecnológicas y escuelas normales", "DELF escolar"],
            [("DELF Prim A1.1", "1,325", "—", "—"), ("DELF A1", "1,445", "1,012", "340"), ("DELF A2", "1,575", "1,103", "450"),
             ("DELF B1", "1,800", "1,080", "570"), ("<strong>DELF B2</strong>", "<strong>2,500</strong>", "1,500", "685"),
             ("DALF C1", "3,500", "—", "—"), ("DALF C2", "4,000", "—", "—")]) + """
<p>El DELF junior y el Prim cuestan lo mismo que el tout public, nivel por nivel. La tarifa escolar es para los
alumnos de las escuelas con convenio con la Embajada; algunos centros reservan sesiones para los estudiantes de las
universidades tecnológicas y de las escuelas normales. Reimpresión o duplicado del diploma: 900 pesos.</p>"""),
        ("inscripcion", "Inscripción, resultados y diploma", """<p>Te inscribes <strong>en el centro</strong>, durante el periodo que fija el calendario nacional: después del
último día no se acepta ningún pago ni expediente. En el IFAL: formulario, transferencia o depósito bancario y
documentos por correo. En la Alianza Francesa de Ciudad de México (San Ángel, Del Valle, Polanco, Interlomas):
formulario que se pide en recepción, pago en el centro —nunca en una Alianza distinta de la del examen— y después
formulario y recibo por correo. En Puebla: pago en la tienda en línea, formulario y reglamento firmado enviados por
correo, y confirmación en un plazo de cuatro días hábiles. En la ENALLT-UNAM: expediente en papel en ventanilla y pago
en caja, con una copia de la INE.</p>

<p>El día del examen: la citación impresa y una identificación oficial con fotografía; no se acepta ninguna versión
digital. No hay reembolsos ni traspasos, salvo si el centro cancela la sesión. Los resultados se publican en la fecha
nacional (el 14 de diciembre de 2026 para la sesión de noviembre), a menudo como una lista de los números de candidato
aprobados, y nunca por teléfono; la constancia de aprobación es válida hasta la entrega del diploma, que se recoge en
persona o a través de un tercero con carta poder simple.</p>"""),
    ],
    list_title="Los {n} centros de examen, estado por estado",
    faq=[("¿Cuándo es la próxima sesión del DELF en México?", "Del 9 al 13 de noviembre de 2026 para el tout public: A1 y C2 el 9, A2 el 10, B1 el 11, B2 el 12 y C1 el 13. Las inscripciones están abiertas del 5 al 23 de octubre de 2026 en los centros que abren la sesión, y los resultados se publican el 14 de diciembre de 2026."),
         ("¿Cuánto cuesta el DELF B2 en México?", "2,500 pesos, tarifa nacional 2026 que aplican todos los centros; 1,500 pesos para los estudiantes de las universidades tecnológicas y de las escuelas normales de la SEP. El DALF cuesta 3,500 pesos (C1) y 4,000 pesos (C2)."),
         ("¿Dónde presentar el DELF en la Ciudad de México?", "En el IFAL (Río Nazas 43), que abre todas las sesiones nacionales; en los cuatro planteles de la Alianza Francesa de Ciudad de México (San Ángel, Del Valle, Polanco, Interlomas); en la ENALLT-UNAM (B1, B2 y C1 en noviembre), o en otras instituciones de la UNAM y del IPN. Las fechas y los precios son los mismos en todas partes."),
         ("¿El DELF está reconocido en México?", "La Federación de Alianzas Francesas de México indica que los diplomas DELF y DALF están reconocidos por la SEP a través de la norma CENNI, así como por empresas y cámaras de comercio. El diploma es el mismo que en Francia y es válido de por vida."),
         ("¿Me pueden reembolsar la inscripción al DELF?", "No: las fichas de inscripción oficiales excluyen cualquier reembolso o traspaso, salvo si el centro cancela la sesión. Inscríbete solo si puedes presentar el examen en las fechas previstas.")],
    also=[("/es/tcf-canada-mexico/", "TCF Canada en México", "Cinco centros, de 4,800 a 6,500 pesos."),
          ("/es/delf-colombia/", "DELF y DALF en Colombia", "El calendario nacional y una tabla de precios común a las Alianzas Francesas."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="calendario de sesiones 2026 y tabla de tarifas 2026 para México del IFAL (publicados por las Alianzas Francesas), sitios del IFAL, de la Federación de Alianzas Francesas de México, de las Alianzas Francesas de Ciudad de México, Guadalajara, Puebla, Monterrey, Aguascalientes y San Luis Potosí, de la ENALLT-UNAM y de la UAEH (fichas de inscripción 2026), consultados el 8 de octubre de 2026.",
))

# ===========================================================================
# COLOMBIA — TCF (es-419)
# ===========================================================================
PAGES.append(from_fr(
    "tcf-colombie", "es", "es-419", "Colombie",
    slug="tcf-canada-colombia", country_name="Colombia",
    crumb="TCF Canada en Colombia",
    title="TCF Canada en Colombia: Bogotá, Medellín, precios y fechas",
    desc="Dónde presentar el TCF Canada en Colombia: las 7 Alianzas Francesas autorizadas, de 1.050.000 a 1.247.000 pesos. Fechas en Medellín, Pereira y Bogotá.",
    h1="TCF Canada en Colombia: los 7 centros autorizados, sus precios y sus fechas",
    intro="""En Colombia, el TCF se presenta en las <strong>siete Alianzas Francesas</strong> autorizadas por France
Éducation international —Bogotá, Medellín, Cali, Barranquilla, Cartagena, Manizales, Pereira—, y <strong>todas ofrecen
el TCF Canada</strong>, desde <strong>1.050.000 pesos</strong> en Medellín y Pereira hasta <strong>1.247.000</strong> en
Bogotá. El ritmo varía: una sesión al mes en Pereira, a solicitud en Cali, cuatro o cinco al año en las demás. Próximas
fechas según nuestra revisión del 8 de octubre de 2026: Medellín el 23 de octubre, Pereira del 27 al 29 de octubre,
Barranquilla a principios de diciembre, Bogotá el 10 de diciembre.""",
    facts=["<strong>{n} centros autorizados</strong> (lista de FEI del 8 de octubre de 2026), todos Alianzas Francesas: <strong>todos ofrecen el TCF Canada</strong>, el TCF Québec y el tout public; ninguno menciona el TCF IRN.",
           "Precio del TCF Canada en 2026: <strong>1.050.000 pesos</strong> en Medellín y Pereira, 1.080.000 en Manizales, 1.199.000 en Barranquilla y <strong>1.247.000</strong> en Bogotá.",
           "Próximas fechas: Medellín, <strong>23 de octubre</strong> (inscripciones hasta el 14) y 2 de diciembre; Pereira, <strong>27-29 de octubre</strong>, 24-26 de noviembre y 9-10 de diciembre; Barranquilla, 1-3 de diciembre; Bogotá, <strong>10 de diciembre</strong> (inscripciones del 27 de octubre al 19 de noviembre).",
           "<strong>Cali</strong> ofrece el TCF a solicitud: «preséntalo cuando quieras».",
           "Sin reembolso después de la inscripción (Cali, Cartagena, Medellín, Pereira); en Medellín, un mes de espera entre dos sesiones.",
           "Resultados en 10 días hábiles según la red de Alianzas, y hasta en cinco semanas según Medellín; certificado digital, válido por dos años."],
    stats=[("{n}", "Alianzas autorizadas", "todas con el TCF Canada"), ("1.050.000", "pesos como mínimo", "el TCF Canada en Medellín y Pereira"),
           ("23 oct.", "próxima fecha", "Medellín; Pereira el 27"), ("10 días", "hábiles para los resultados", "según la red de Alianzas")],
    sections=[
        ("centros-tcf-canada", "El TCF Canada en Colombia, Alianza por Alianza", releve([
            ("Alianza Francesa de Bogotá (sede Chicó)", "<strong>Canada</strong>, Québec, tout public (DAP)",
             "Canada <strong>1.247.000</strong> · Québec 424.000 por prueba · tout public 835.000 + 267.000 por prueba",
             "Canada: 30/04, 16/07, 01/10 y <strong>10/12/2026</strong> (inscripciones del 27/10 al 19/11); Québec el 25/11 (hasta el 17/10). Tienda en línea."),
            ("Alianza Francesa de Medellín (sede Centro)", "<strong>Canada</strong>, Québec, tout public (DAP)",
             "Canada <strong>1.050.000</strong> · Québec 280.000 a 345.000 por prueba · tout public 650.000",
             "Canada <strong>23/10</strong> (inscripciones hasta el 14/10) y <strong>02/12</strong> (del 26/10 al 23/11). Formulario, pago y copia de la cédula; en computadora."),
            ("Alianza Francesa de Cali", "<strong>Canada</strong>, Québec, tout public",
             "Canada <strong>1.138.800</strong>, probablemente (la página invierte sus columnas; por confirmar) · −10 % para los alumnos",
             "<strong>A solicitud</strong>; preinscripción en la plataforma Q10 de la Alianza y después pago."),
            ("Alianza Francesa de Barranquilla", "<strong>Canada</strong>, Québec, tout public (DAP)",
             "Canada <strong>1.199.000</strong> · Québec 316.000 a 343.000 por prueba · tout public 605.000",
             "Cuatro sesiones en 2026: <strong>1-3 de diciembre</strong> (inscripciones del 19/10 al 13/11). Preinscripción en Q10."),
            ("Alianza Francesa de Cartagena de Indias", "<strong>Canada</strong>, Québec, tout public",
             "325.000 publicados para el TCF Canada: monto anómalo, por confirmar · Québec 382.000 por prueba · tout public 576.000",
             "Fechas publicadas solo hasta junio de 2026; inscripción al TCF Canada por WhatsApp."),
            ("Alianza Francesa de Manizales", "<strong>Canada</strong>, Québec, tout public",
             "Canada <strong>1.080.000</strong> (tabla con el título 2025) · Québec 390.000 a 410.000 por prueba · tout public, examen completo: 1.100.000",
             "Canada entre el 5 y el 7 de noviembre, inscripciones del 1 al 24 de octubre, bajo un título de 2025: por confirmar."),
            ("Alianza Francesa de Pereira", "<strong>Canada</strong>, Québec, tout public (DAP)", "Canada <strong>1.050.000</strong>",
             "<strong>Cada mes</strong>: 27-29/10 (inscripciones del 1 al 15/10), 24-26/11 (del 1 al 15/11), 09-10/12 (del 1 al 7/12). Formulario en línea, foto digital, pago."),
        ], "es-419", "Lo que mostraba el sitio web de cada Alianza el 8 de octubre de 2026, precios en pesos colombianos (COP). «Por confirmar»: monto o fecha incoherentes en el sitio; lo que diga la Alianza es lo que vale.")),
        ("inscripcion", "Cómo inscribirte en el TCF Canada en Colombia", """<p>Cada Alianza tiene su propia vía de entrada: tienda en línea en Bogotá y Pereira, plataforma Q10 en Cali y
Barranquilla, formulario PDF en Medellín, formulario en línea y pago por Davivienda en Manizales, WhatsApp en
Cartagena. En todas, la inscripción termina con el pago y el envío de una copia del documento de identidad —para el TCF
Canada, el de tu expediente de IRCC—; Pereira pide además una foto digital tipo pasaporte, y Medellín toma una foto el
día del examen. Los sitios web de la red cambiaron de dirección: ahora están en <em>ciudad</em>.alianzafrancesa.edu.co,
y ya no en el dominio que indica la lista de FEI.</p>

<p>Una vez inscrito, no hay vuelta atrás: Cali, Cartagena, Medellín y Pereira excluyen cualquier reembolso, y las
fechas no se pueden cambiar. En Medellín hay que esperar un mes entre dos sesiones, y la recalificación está suspendida
hasta octubre de 2027. Los resultados llegan en «10 días hábiles», según las preguntas frecuentes comunes de la red, y
en 20 días hábiles a cinco semanas según Medellín; el certificado es digital y vale dos años. Y ninguna constancia se
compra: los sitios que venden un certificado TCF «sin examen» son fraudes.</p>

<p>Para Quebec, la Alianza Francesa de Bogotá tiene un convenio con el Ministerio de Inmigración de Quebec: con ciertas
condiciones, el programa de aprendizaje del francés de Quebec puede reembolsar los cursos de francés.</p>"""),
    ],
    list_title="Los {n} centros TCF autorizados, ciudad por ciudad",
    faq=[("¿Dónde presentar el TCF Canada en Bogotá?", "En la Alianza Francesa de Bogotá, sede Chicó (carrera 11 # 93-40): 1.247.000 pesos, próxima sesión el 10 de diciembre de 2026, con inscripciones del 27 de octubre al 19 de noviembre en la tienda en línea de la Alianza. Datos consultados el 8 de octubre de 2026."),
         ("¿Cuánto cuesta el TCF Canada en Colombia?", "De 1.050.000 pesos (Medellín, Pereira) a 1.247.000 pesos (Bogotá): 1.080.000 en Manizales y 1.199.000 en Barranquilla. En Cali, el precio para externos es probablemente de 1.138.800 pesos —la página invierte sus columnas—, y el monto publicado en Cartagena (325.000) hay que confirmarlo con la Alianza."),
         ("¿Dónde presentar el TCF Canada lo más pronto posible en Colombia?", "En Pereira, que organiza una sesión cada mes (27-29 de octubre, 24-26 de noviembre y 9-10 de diciembre de 2026, con inscripciones del 1 al 15 del mes), o en Cali, que lo ofrece a solicitud. Medellín tiene una fecha el 23 de octubre, con inscripciones hasta el 14."),
         ("¿Me pueden reembolsar el TCF?", "No: Cali, Cartagena, Medellín y Pereira excluyen cualquier reembolso después de la inscripción, y las fechas no se pueden cambiar. Inscríbete solo cuando tengas la fecha decidida."),
         ("¿IRCC acepta el TCF Canada presentado en Colombia?", "Sí: la constancia de resultados la emite France Éducation international, sea cual sea el centro autorizado, y es válida dos años. Asegúrate de elegir el TCF Canada y no el tout public.")],
    also=[("/es/delf-colombia/", "DELF y DALF en Colombia", "El calendario nacional y la tabla común de precios, B2 a 490.000 pesos."),
          ("/es/tcf-canada-mexico/", "TCF Canada en México", "Cinco centros, en Ciudad de México, Guadalajara, Puebla, Pachuca y Aguascalientes."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="sitios web de las Alianzas Francesas de Bogotá, Medellín, Cali, Barranquilla, Cartagena de Indias, Manizales y Pereira (páginas del TCF, tarifas y calendarios 2026, tiendas en línea, reglamentos de los exámenes), consultados el 8 de octubre de 2026.",
))

# ===========================================================================
# COLOMBIA — DELF (es-419)
# ===========================================================================
PAGES.append(from_fr(
    "delf-colombie", "es", "es-419", "Colombie",
    slug="delf-colombia", country_name="Colombia",
    crumb="DELF en Colombia",
    title="Examen DELF en Colombia 2026: fechas, precios y {n} centros",
    desc="Examen DELF y DALF en Colombia: calendario nacional (marzo, junio, agosto, noviembre de 2026), una tabla común (B2: 490.000 pesos) y las 15 Alianzas.",
    h1="DELF y DALF en Colombia: los {n} centros, el calendario y los precios de 2026",
    intro="""En Colombia, el DELF y el DALF se presentan en las {n} sedes de las Alianzas Francesas autorizadas por France
Éducation international, de Bogotá a Valledupar, con un <strong>calendario y una tabla de precios comunes</strong> a la
red. Cuatro sesiones tout public en 2026 —marzo, junio, agosto y noviembre—; la de <strong>noviembre</strong> (pruebas
escritas del 3 al 6, orales del 9 al 13) cerraba sus inscripciones el <strong>9 de octubre</strong>. El DELF B2 cuesta
<strong>490.000 pesos</strong>; los alumnos de las Alianzas tienen un descuento del 10 al 20 %.""",
    facts=["<strong>{n} centros de examen</strong> (lista de FEI del 8 de octubre de 2026), todos de las Alianzas Francesas, entre ellos tres sedes en Bogotá; la gestión central está en la Alianza Francesa de Bogotá.",
           "Calendario nacional 2026: tout public en marzo, junio, agosto y <strong>noviembre</strong>; junior en abril y octubre (y en mayo en algunos centros); Prim en mayo y septiembre.",
           "Noviembre de 2026: A1 y A2 el 3, B1 el 4, B2 el 5, C1 y C2 el 6; inscripciones del 14 de septiembre al <strong>9 de octubre</strong>.",
           "Tabla común 2026: <strong>A1 248.000 · A2 263.000 · B1 383.000 · B2 490.000 · C1 591.000 · C2 643.000 pesos</strong>; junior y Prim al mismo precio.",
           "Sin reembolso; un aplazamiento, una sola vez, con certificado médico. En Bogotá, resultados treinta días hábiles después de los orales.",
           "El diploma, impreso en Francia, llega a Colombia <strong>de cinco a seis meses</strong> después de la sesión."],
    stats=[("{n}", "centros de examen", "lista de FEI del 8 de octubre de 2026"), ("490.000", "pesos el DELF B2", "tabla común 2026"),
           ("3-6 nov.", "sesión tout public", "inscripciones hasta el 9 de octubre"), ("5-6 meses", "para el diploma", "impreso en Francia")],
    sections=[
        ("calendario", "El calendario nacional 2026", table(
            "Calendario DELF-DALF tout public 2026 publicado por las Alianzas Francesas de Bogotá, Barranquilla, Bucaramanga, Cali, Cartagena, Manizales, Medellín y Pereira, consultado el 8 de octubre de 2026 (orales: fechas de Bogotá).",
            ["Sesión", "Inscripciones", "A1", "A2", "B1", "B2", "C1", "C2", "Orales"],
            [("Marzo", "19/01 – 16/02", "17/03", "17/03", "18/03", "19/03", "20/03", "20/03", "24-27/03"),
             ("Junio", "27/04 – 23/05", "16/06", "16/06", "17/06", "18/06", "19/06", "19/06", "22-26/06"),
             ("Agosto", "22/06 – 18/07", "11/08", "11/08", "12/08", "13/08", "14/08", "14/08", "18-21/08"),
             ("<strong>Noviembre</strong>", "<strong>14/09 – 09/10</strong>", "03/11", "03/11", "04/11", "05/11", "06/11", "06/11", "09-13/11")]) + """
<p>DELF junior: abril y octubre de 2026 (del 13 al 16 de octubre, inscripciones cerradas el 15 de septiembre), más una
sesión en mayo en Cali, Manizales y Barranquilla; DELF Prim: mayo y septiembre. Pereira agregó una sesión
extraordinaria en septiembre. El 8 de octubre de 2026 no había ningún calendario 2027 publicado. Los sitios web de
Armenia, Cúcuta, Popayán, Santa Marta y Valledupar todavía mostraban calendarios de 2024 o 2025: infórmate directamente
con esas Alianzas.</p>"""),
        ("precios", "¿Cuánto cuesta el DELF en Colombia?", table(
            "Tabla 2026 común a las Alianzas Francesas de Bogotá, Barranquilla, Bucaramanga, Cali, Cartagena, Manizales, Medellín y Pereira, en pesos colombianos (COP), consultada el 8 de octubre de 2026.",
            ["Nivel", "Tarifa general", "Alumnos de las Alianzas (−10 %)"],
            [("DELF A1 (y Prim A1.1)", "248.000", "223.200"), ("DELF A2", "263.000", "236.700"), ("DELF B1", "383.000", "344.700"),
             ("<strong>DELF B2</strong>", "<strong>490.000</strong>", "441.000"), ("DALF C1", "591.000", "531.900"), ("DALF C2", "643.000", "578.700")], wide=False) + """
<p>El descuento para alumnos es del 10 % en la mayoría de las Alianzas (Barranquilla, Pereira, Medellín) y del 20 % en
Cali. Bogotá y Medellín también venden combos de dos niveles: B1 + B2, 785.700 pesos en Bogotá.</p>"""),
        ("inscripcion", "Inscripción, resultados y diploma", """<p>Te inscribes en la Alianza, durante el periodo de inscripción de la sesión —Bogotá advierte que fuera de
esas fechas no se acepta ninguna inscripción—: tienda en línea en Bogotá, plataforma Q10 en Cali y Barranquilla,
formulario en línea en Bucaramanga y Pereira, documentos por correo en Medellín (formulario, recibo, documento de
identidad, reglamento firmado). Documentos aceptados el día del examen: cédula de ciudadanía o de extranjería, tarjeta
de identidad o pasaporte vigente.</p>

<p>No hay reembolso; se puede aplazar una sola vez, con certificado médico —en Medellín, hay que justificarlo en un
plazo de siete días—. En Bogotá, los resultados se publican treinta días hábiles después de los últimos orales, en
línea con el código de candidato, nunca por correo ni por teléfono; Medellín anuncia los de noviembre a partir del 14
de diciembre, aproximadamente. El diploma, impreso en Francia, llega a Colombia de cinco a seis meses después de la
sesión.</p>

<p>Las Alianzas presentan el DELF como una forma de acreditar el nivel de idioma que piden las universidades
colombianas; verifica con la tuya qué acepta.</p>"""),
    ],
    list_title="Los {n} centros de examen, ciudad por ciudad",
    faq=[("¿Cuándo es la próxima sesión del DELF en Colombia?", "La sesión de noviembre de 2026 es del 3 al 6 de noviembre para las pruebas escritas (A1 y A2 el 3, B1 el 4, B2 el 5, C1 y C2 el 6) y del 9 al 13 de noviembre para las orales; sus inscripciones cerraban el 9 de octubre de 2026. El calendario 2027 no estaba publicado el 8 de octubre de 2026."),
         ("¿Cuánto cuesta el DELF B2 en Colombia?", "490.000 pesos según la tabla 2026 común a las Alianzas Francesas; 441.000 pesos para sus alumnos en Barranquilla y Pereira (−10 %), 392.000 en Cali (−20 %). El DALF cuesta 591.000 pesos (C1) y 643.000 pesos (C2)."),
         ("¿Dónde presentar el DELF en Bogotá?", "En una de las tres sedes de la Alianza Francesa de Bogotá —Chicó, Centro, Cedritos—, que además gestiona el DELF para todo el país. La inscripción se hace en la tienda en línea de la Alianza, durante el periodo de inscripción de cada sesión."),
         ("¿Me pueden reembolsar la inscripción al DELF?", "No: los reglamentos de Bogotá, Medellín y Pereira excluyen cualquier reembolso. Se puede aplazar una sola vez, por enfermedad, con certificado médico."),
         ("¿Cuándo llega el diploma del DELF a Colombia?", "Los resultados se publican unas seis semanas después de la sesión; el diploma, impreso en Francia, llega a Colombia de cinco a seis meses después, según las preguntas frecuentes comunes de las Alianzas. La constancia de aprobación se recoge en el centro con un documento de identidad.")],
    also=[("/es/tcf-canada-colombia/", "TCF Canada en Colombia", "Las siete Alianzas, de 1.050.000 a 1.247.000 pesos."),
          ("/es/delf-mexico/", "DELF y DALF en México", "El calendario y las tarifas nacionales, 71 centros."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="sitios web de las Alianzas Francesas de Bogotá, Medellín, Cali, Barranquilla, Cartagena de Indias, Manizales, Pereira, Bucaramanga, Armenia, Cúcuta, Popayán, Santa Marta y Valledupar (calendarios y tarifas DELF-DALF 2026, reglamentos de los exámenes, preguntas frecuentes), consultados el 8 de octubre de 2026.",
    notes={"armenia-alliance-francaise-d-armenia": "El 8 de octubre de 2026, el calendario en línea era el de 2025: infórmate con la Alianza.",
           "cucuta-alliance-francaise-de-cucuta": "El 8 de octubre de 2026, el calendario en línea era el de 2024.",
           "popayan-alliance-francaise-de-popayan": "El 8 de octubre de 2026, el calendario en línea era el de 2024.",
           "santa-marta-alliance-francaise-de-santa-marta": "El 8 de octubre de 2026, el calendario en línea era el de 2024.",
           "valledupar-alliance-francaise-de-valledupar": "El 8 de octubre de 2026, el calendario en línea era el de 2024."},
))


# ===========================================================================
# ARGENTINA
# ===========================================================================
PAGES.append(from_fr(
    "tcf-argentine", "es", "es-419", "Argentine",
    slug="tcf-canada-argentina", country_name="Argentina",
    crumb="TCF Canada en Argentina",
    title="TCF Canada en Argentina: Buenos Aires, Córdoba y Rosario",
    desc="Dónde rendir el TCF Canada en Argentina: Campus France en Buenos Aires (sesiones mensuales), las Alianzas de Córdoba y Rosario. Sin precio publicado.",
    h1="TCF Canada en Argentina: los {n} centros autorizados y la inscripción",
    intro="""En Argentina, {n} centros están autorizados para el TCF por France Éducation international, y cuatro
anuncian el TCF Canada: <strong>Campus France</strong> (Instituto Francés) en Buenos Aires, que abre sesiones todos
los meses, las <strong>Alianzas Francesas de Córdoba</strong> (a solicitud, de lunes a viernes) y de
<strong>Rosario</strong>, y un centro privado de Buenos Aires cuyas únicas fechas publicadas son de 2025.
Particularidad del país: <strong>ningún centro publica el precio del TCF Canada</strong>; hay que pedirlo. La Alianza
Francesa de Buenos Aires, por su parte, ofrece el TEF, no el TCF.""",
    facts=["<strong>{n} centros autorizados</strong> (lista de FEI del 8 de octubre de 2026); <strong>4 anuncian el TCF Canada</strong>: Campus France (Buenos Aires), las Alianzas Francesas de Córdoba y de Rosario, y el Centro educativo canadiense (Buenos Aires).",
           "El sitio web de la Alianza Francesa de Mendoza no menciona el TCF; la Alianza Francesa de Buenos Aires ofrece el TEF Canada, no el TCF.",
           "<strong>Ningún precio publicado</strong> para el TCF Canada; la única tarifa de TCF publicada en el país es la del TCF DAP de Campus France: 74 €, pagaderos en pesos.",
           "Campus France: sesiones <strong>todos los meses</strong>, con fecha fijada por correo electrónico, en computadora; Córdoba: <strong>a solicitud</strong>, de lunes a viernes.",
           "Inscripción por correo electrónico (formulario en línea en Córdoba); en Campus France, la inscripción solo es oficial cuando se recibe el pago.",
           "Resultados en <strong>15 días hábiles</strong> (Campus France, Córdoba), con una constancia electrónica válida por dos años."],
    stats=[("4", "centros con TCF Canada", "de {n} centros autorizados"), ("0", "precios publicados", "hay que pedirlo al centro"),
           ("todos los meses", "en Campus France", "fecha fijada por correo"), ("15 días", "hábiles para los resultados", "constancia electrónica")],
    sections=[
        ("centros-tcf-canada", "El TCF Canada en Argentina, centro por centro", releve([
            ("Campus France — Instituto Francés (Buenos Aires)", "<strong>Canada</strong>, IRN, tout public, Québec, DAP",
             "no publicado («consultar costos») · DAP 74 €", "Sesiones todos los meses, con fecha acordada por correo electrónico; DAP en una sola sesión, a principios de diciembre de 2026. En computadora, en el edificio del consulado (Basavilbaso 1253)."),
            ("Alianza Francesa de Córdoba", "<strong>Canada</strong>, tout public", "no publicado",
             "<strong>A solicitud</strong>, de lunes a viernes: formulario en línea y luego confirmación de la fecha; inscripción completa al menos una semana antes. En computadora."),
            ("Alianza Francesa de Rosario", "<strong>Canada</strong>, Québec, IRN, tout public", "no publicado", "Ninguna fecha publicada: hay que escribir a la Alianza (pedagogie@afrosario.org.ar)."),
            ("Centro educativo canadiense (Buenos Aires)", "<strong>Canada</strong>, Québec, IRN, tout public", "«contáctenos»",
             "Sitio rebautizado «Centro Educativo ComunicAR»; solo hay fechas de 2025 publicadas (aproximadamente cada dos meses). Inscripción por correo electrónico."),
            ("Alianza Francesa de Mendoza", "ningún TCF en su sitio web", "—", "El sitio solo presenta el DELF-DALF: confírmalo con la Alianza."),
        ], "es-419", "Lo que mostraba el sitio web de cada centro el 8 de octubre de 2026. «Sin datos»: no publicado o no verificado; lo que diga el sitio del centro es lo que vale.")),
        ("inscripcion", "Cómo inscribirte en el TCF Canada en Argentina", """<p>Siempre se empieza por <strong>escribir al centro</strong> para fijar una fecha y conocer el precio. En
Campus France (buenosaires@campusfrance.org), envías tus datos personales y tu número de DNI; el pago se hace por
transferencia, en euros o en pesos al tipo de cambio de la cancillería, y la inscripción solo es oficial cuando el
centro recibe el comprobante. En Córdoba, un formulario en línea pide los días y horarios que prefieres, y luego la
Alianza confirma la fecha; la inscripción debe estar completa al menos una semana antes. Para el TCF Canada, usa el
documento de identidad de tu expediente de IRCC.</p>

<p>Los resultados llegan en quince días hábiles, en una constancia electrónica válida por dos años; Campus France
recibe el original en papel aproximadamente un mes después. Ningún centro publica reglas de cancelación o de
reembolso: pregunta antes de pagar. El TEF Canada, el otro examen aceptado por IRCC, se rinde en la Alianza Francesa
de Buenos Aires.</p>"""),
    ],
    list_title="Los {n} centros TCF autorizados, ciudad por ciudad",
    faq=[("¿Dónde rendir el TCF Canada en Buenos Aires?", "En Campus France, en el Instituto Francés (Basavilbaso 1253, en el edificio del consulado), que abre sesiones todos los meses —la fecha se fija por correo electrónico—, o en el Centro educativo canadiense, cuyas únicas fechas publicadas son de 2025. La Alianza Francesa de Buenos Aires no ofrece el TCF, sino el TEF Canada."),
         ("¿Cuánto cuesta el TCF Canada en Argentina?", "Ninguno de los cinco centros autorizados publicaba el precio el 8 de octubre de 2026: hay que pedirlo. La única tarifa de TCF publicada en el país es la del TCF DAP de Campus France, 74 €, pagaderos en pesos."),
         ("¿Se puede rendir el TCF Canada en Córdoba?", "Sí, en la Alianza Francesa de Córdoba, a solicitud, de lunes a viernes: completas el formulario en línea, la Alianza confirma la fecha y la inscripción debe estar completa al menos una semana antes. Resultados en unos quince días hábiles."),
         ("¿Cuánto tardan los resultados del TCF Canada?", "Quince días hábiles según Campus France y la Alianza Francesa de Córdoba, en una constancia electrónica válida por dos años."),
         ("¿IRCC acepta el TCF Canada rendido en Argentina?", "Sí: la constancia de resultados la emite France Éducation international, sea cual sea el centro autorizado, y es válida por dos años.")],
    also=[("/es/delf-argentina/", "DELF y DALF en Argentina", "El calendario nacional y los precios de fin de 2026."),
          ("/es/tcf-canada-chile/", "TCF Canada en Chile", "Dos centros, 299.000 pesos chilenos."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="sitios de Campus France Argentina y del Instituto Francés de Argentina, de las Alianzas Francesas de Córdoba, Rosario, Mendoza y Buenos Aires, y del Centro educativo canadiense (páginas del TCF, formularios, reglamentos), consultados el 8 de octubre de 2026.",
))

PAGES.append(from_fr(
    "delf-argentine", "es", "es-419", "Argentine",
    slug="delf-argentina", country_name="Argentina",
    crumb="DELF en Argentina",
    title="Examen DELF en Argentina: fechas 2026, precios y {n} centros",
    desc="DELF y DALF en Argentina: la sesión del 4 y 5 de diciembre de 2026 (inscripciones hasta el 5 de noviembre), precios en euros y en pesos, las 28 Alianzas.",
    h1="DELF y DALF en Argentina: los {n} centros, el calendario y los precios",
    intro="""En Argentina, el DELF y el DALF solo se rinden en las <strong>Alianzas Francesas</strong>: {n} centros de
examen, bajo la gestión central de la Alianza Francesa de Buenos Aires. Hay tres sesiones tout public al año; la
próxima será el <strong>4 y 5 de diciembre de 2026</strong>, con inscripciones hasta el <strong>5 de noviembre</strong>
a nivel nacional (antes o después según la Alianza). Los precios se fijan en euros y se pagan en pesos: el DELF B2
cuesta 163 € para un candidato libre, es decir, <strong>295.030 pesos</strong> para la sesión de diciembre.""",
    facts=["<strong>{n} centros de examen</strong> (lista de FEI del 8 de octubre de 2026), exclusivamente Alianzas Francesas; gestión central en la Alianza Francesa de Buenos Aires.",
           "Tout public: abril, junio-julio y <strong>4-5 de diciembre de 2026</strong> (A1, A2 y B1 el 4; B2, C1 y C2 el 5), inscripciones hasta el <strong>5 de noviembre</strong>.",
           "Precios de la sesión de diciembre (candidato libre): <strong>A1-A2 125 € · B1-B2 163 € · C1 246 € · C2 277 €</strong>, es decir, de 226.250 a 501.370 pesos.",
           "Alumnos de las Alianzas: <strong>50 % de descuento</strong>; colegios afiliados: tarifa reducida.",
           "Ausencia: certificado médico dentro de la semana, y el derecho solo vale para la sesión siguiente.",
           "Resultados en línea unas cinco semanas después; el diploma, enviado desde Francia, llega de cuatro a seis meses después."],
    stats=[("{n}", "Alianzas Francesas", "lista de FEI del 8 de octubre de 2026"), ("295.030", "pesos el DELF B2", "163 € para un candidato libre"),
           ("4-5 dic.", "próxima sesión", "inscripciones hasta el 5 de noviembre"), ("−50 %", "para alumnos de las Alianzas", "en todos los niveles")],
    sections=[
        ("calendario", "El calendario nacional 2026", table(
            "Calendario DELF-DALF 2026 de la Alianza Francesa de Buenos Aires (gestión central), consultado el 8 de octubre de 2026.",
            ["Sesión", "Niveles", "Inscripciones", "Pruebas"],
            [("Abril, tout public", "A1, A2, B1 · B2, C1, C2", "4-23 de marzo", "24 · 25 de abril"),
             ("Junio, tout public y junior", "A1, A2, B1 · B2, C1, C2", "28 de abril – 20 de mayo", "26 · 27 de junio"),
             ("Octubre, Prim", "A1.1, A1, A2", "10 de agosto – 10 de septiembre", "9 de octubre"),
             ("Noviembre, junior", "A2, B1 · A1, B2", "1-30 de septiembre", "27 · 28 de noviembre"),
             ("<strong>Diciembre, tout public</strong>", "A1, A2, B1 · B2, C1, C2", "<strong>1 de septiembre – 5 de noviembre</strong>", "<strong>4 · 5 de diciembre</strong>")], wide=False) + """
<p>Los cierres locales varían: 2 de noviembre en Córdoba, 15 de noviembre en Mar del Plata para los adultos. Rosario
y Mendoza venden la sesión de diciembre en línea; Santa Fe y Mendoza agregan una serie junior el 2 y 3 de diciembre.
Ningún calendario 2027 estaba publicado el 8 de octubre de 2026.</p>"""),
        ("precios", "¿Cuánto cuesta el DELF en Argentina?", table(
            "Tarifas de la sesión noviembre-diciembre de 2026 publicadas por la Alianza Francesa de Mar del Plata; los mismos montos en pesos en Córdoba, Mendoza y Rosario, consultados el 8 de octubre de 2026.",
            ["Diploma", "Candidato libre", "Colegios afiliados", "Alumnos de las Alianzas"],
            [("DELF A1 · A2", "125 € ($ 226.250)", "88 € ($ 159.280)", "63 € ($ 114.030)"),
             ("DELF B1 · <strong>B2</strong>", "<strong>163 € ($ 295.030)</strong>", "114 € ($ 206.340)", "82 € ($ 148.420)"),
             ("DALF C1", "246 € ($ 445.260)", "172 € ($ 311.320)", "124 € ($ 224.440)"),
             ("DALF C2", "277 € ($ 501.370)", "195 € ($ 352.950)", "140 € ($ 253.400)")]) + """
<p>«Los montos base se fijan en euros, pero el pago se hace en pesos»: la suma en pesos cambia en cada sesión. La
Alianza Francesa de Buenos Aires solo publica la suya al abrir las inscripciones. El DELF junior cuesta lo mismo que
el tout public en Córdoba y en Mendoza.</p>"""),
        ("inscripcion", "Inscripción, resultados y diploma", """<p>Te inscribes en una Alianza, dentro de los plazos fijados por la gestión central: en línea en el
«kiosco» de Córdoba, Rosario y Mendoza (tarjeta de débito o de crédito), por correo electrónico, WhatsApp o en persona
en Mar del Plata, y en el servicio de inscripciones en Buenos Aires. Si ya rendiste un DELF, indica tu número de
candidato. El día del examen, lleva un documento de identidad vigente; a quien llega tarde ya no se le admite una vez
comenzada la comprensión oral.</p>

<p>En caso de ausencia, solo un certificado médico entregado dentro de la semana conserva el derecho a examen, y
únicamente para la sesión siguiente; Córdoba nunca reembolsa, pero acredita el monto durante un año para sus cursos.
Los resultados (aprobado o no) se publican en el sitio web de la Alianza Francesa de Buenos Aires —unas cinco semanas
después de la sesión de junio de 2026—; el diploma, enviado desde Francia, llega de cuatro a seis meses después.</p>"""),
    ],
    list_title="Los {n} centros de examen, provincia por provincia",
    faq=[("¿Cuándo es el próximo examen DELF en Argentina?", "El 4 y 5 de diciembre de 2026 para el tout public (A1, A2 y B1 el 4; B2, C1 y C2 el 5), con inscripciones hasta el 5 de noviembre a nivel nacional —el 2 de noviembre en Córdoba, el 15 en Mar del Plata—. El calendario 2027 no estaba publicado el 8 de octubre de 2026."),
         ("¿Cuánto cuesta el DELF B2 en Argentina?", "163 € para un candidato libre, que se pagan en pesos: 295.030 pesos para la sesión de diciembre de 2026 en Córdoba, Rosario, Mendoza y Mar del Plata. Los alumnos de las Alianzas pagan la mitad (148.420 pesos)."),
         ("¿Dónde rendir el DELF en Buenos Aires?", "En la Alianza Francesa de Buenos Aires (avenida Córdoba 946), gestión central del DELF en Argentina: en el país, solo las Alianzas Francesas son centros de examen."),
         ("¿Qué pasa si faltas al examen DELF?", "Tienes que entregar un certificado médico a más tardar una semana después del examen: así conservas el derecho solo para la sesión siguiente, y la reinscripción no es automática. Si no, pierdes el derecho."),
         ("¿Cuándo llega el diploma del DELF?", "Los resultados se publican en el sitio web de la Alianza Francesa de Buenos Aires, unas cinco semanas después de la sesión; el diploma, enviado desde Francia, llega de cuatro a seis meses después.")],
    also=[("/es/tcf-canada-argentina/", "TCF Canada en Argentina", "Campus France, Córdoba y Rosario; precio a solicitud."),
          ("/es/delf-chile/", "DELF y DALF en Chile", "El calendario nacional 2026 y la sesión B2 de diciembre."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="sitios de la Alianza Francesa de Buenos Aires (páginas de exámenes y del DELF-DALF, calendario 2026, reglamentos), de las Alianzas Francesas de Córdoba, Rosario, Mendoza, Mar del Plata, Santa Fe, Olavarría y Bariloche, de Campus France y del Instituto Francés de Argentina, consultados el 8 de octubre de 2026.",
    notes={"resistencia-alliance-francaise-de-resistencia": "FEI le atribuye la dirección de la Alianza Francesa de Buenos Aires; el teléfono (362) y el mapa de la red la ubican en Resistencia (Chaco)."},
))

# ===========================================================================
# CHILE
# ===========================================================================
PAGES.append(from_fr(
    "tcf-chili", "es", "es-419", "Chili",
    slug="tcf-canada-chile", country_name="Chile",
    crumb="TCF Canada en Chile",
    title="TCF Canada en Chile: Santiago y Concepción, precio y fechas",
    desc="TCF Canada en Chile: el Instituto Francés en Santiago y la Alianza Francesa de Concepción, 299.000 pesos, fechas de noviembre de 2026 e inscripción.",
    h1="TCF Canada en Chile: los 2 centros autorizados, el precio y las fechas",
    intro="""En Chile, el TCF —Canada, Québec, IRN o tout public— se rinde en <strong>dos centros autorizados</strong> por
France Éducation international: el <strong>Instituto Francés de Chile</strong>, en Santiago, y la <strong>Alianza
Francesa de Concepción</strong>. El TCF Canada cuesta <strong>299.000 pesos</strong> en ambos. El 8 de octubre de 2026
quedaban dos fechas en Santiago, el 19 y el 27 de noviembre, y una en Concepción, el 11 de noviembre, con
inscripciones hasta el 13 de octubre. A continuación: los dos centros, lo que mostraban sus sitios web y cómo
inscribirte.""",
    facts=["<strong>2 centros autorizados</strong> (lista de FEI del 8 de octubre de 2026): el Instituto Francés de Chile en Santiago, con sesiones en computadora, y la Alianza Francesa de Concepción.",
           "<strong>TCF Canada: 299.000 pesos</strong> en los dos centros; al TCF no se le aplica ningún descuento.",
           "Santiago: <strong>19 y 27 de noviembre de 2026</strong> (inscripciones hasta el 26 de octubre y el 9 de noviembre); Concepción: <strong>11 de noviembre de 2026</strong> (hasta el 13 de octubre).",
           "Inscripción <strong>solo en línea</strong> en Santiago, con pago con tarjeta; en persona o por correo electrónico en Concepción.",
           "Sin reembolso si desistes; un solo cambio de fecha, solicitado al menos 30 días (Santiago) o un mes (Concepción) antes.",
           "Constancia en PDF por correo electrónico, válida por dos años; ya no hay recalificación para los exámenes rendidos desde el 1 de septiembre de 2026."],
    stats=[("{n}", "centros autorizados", "lista de FEI del 8 de octubre de 2026"), ("299.000", "pesos el TCF Canada", "en los dos centros"),
           ("3", "fechas de TCF Canada", "hasta fines de noviembre de 2026"), ("2 años", "de validez", "constancia en PDF por correo")],
    sections=[
        ("centros-tcf-canada", "El TCF Canada en Chile, centro por centro", releve([
            ("Instituto Francés de Chile (Santiago)", "<strong>Canada</strong>, Québec, IRN, tout public, DAP",
             "Canada <strong>299.000</strong> · IRN 245.000 · tout public: pruebas obligatorias 172.000, completo 295.000",
             "Canada: <strong>19/11/2026</strong> (inscripciones hasta el 26/10) y <strong>27/11/2026</strong> (hasta el 09/11), a la venta el 8 de octubre; IRN 20/11 y 17/12; ninguna sesión Québec a la venta. Fecha fuera de calendario: +15 %, solicitada al menos 30 días antes."),
            ("Alianza Francesa de Concepción", "<strong>Canada</strong>, Québec, IRN, tout public, DAP",
             "Canada <strong>299.000</strong> · IRN 245.000 · Québec 85.000 por prueba",
             "Siete sesiones en 2026, con el TCF Canada el primero de los dos días: la próxima, el <strong>11/11/2026</strong> (inscripciones del 21/09 al 13/10). Calendario 2027 no publicado."),
        ], "es-419", "Lo que mostraba el sitio web de cada centro el 8 de octubre de 2026, precios en pesos chilenos (CLP). «Sin datos»: no publicado o no verificado; lo que diga el sitio del centro es lo que vale.") + """
<p>Los dos centros aplican las mismas tarifas 2026. Las preguntas frecuentes del Instituto todavía muestran tarifas
anteriores (TCF IRN 236.000 pesos, Québec 82.000 por prueba): lo que vale es la plataforma de inscripción, donde se
paga el examen.</p>"""),
        ("inscripcion", "Cómo inscribirte en el TCF Canada en Chile", """<p>En Santiago, el Instituto Francés de Chile recibe las inscripciones <strong>exclusivamente en línea</strong>:
creas tu ficha en su plataforma (icf.extranet-aec.com), agregas la fecha al carrito y pagas con tarjeta de débito o
de crédito; la citación llega por correo electrónico a más tardar una semana antes. En Concepción, la Alianza
Francesa inscribe en persona (Colo Colo 1) o por correo electrónico, y cierra sus inscripciones de tres a cinco
semanas antes del examen.</p>

<p>El día del examen: cédula de identidad o pasaporte vigente, y la citación; para el TCF Canada, lleva el documento
de tu expediente de IRCC. Ninguno de los dos centros reembolsa si desistes; solo se permite un cambio de fecha,
solicitado al menos 30 días antes en Santiago y un mes antes en Concepción. La constancia, válida por dos años, llega
en PDF por correo electrónico: ya no hay versión en papel. El plazo que anuncia el Instituto varía según la página
—de 10 a 15 días hábiles en la página del TCF Canada, de 3 a 5 semanas en las condiciones generales—: calcula un
mes si tu trámite tiene una fecha límite. Desde los exámenes del 1 de septiembre de 2026 ya no hay recalificación:
el Instituto la anuncia suspendida hasta fines de 2027.</p>"""),
    ],
    list_title="Los {n} centros TCF autorizados en Chile",
    faq=[("¿Dónde rendir el TCF Canada en Chile?", "En el Instituto Francés de Chile, en Santiago (Providencia), o en la Alianza Francesa de Concepción: son los dos únicos centros TCF autorizados por France Éducation international en el país al 8 de octubre de 2026, y los dos ofrecen el TCF Canada."),
         ("¿Cuánto cuesta el TCF Canada en Chile?", "299.000 pesos chilenos en los dos centros (tarifas 2026 consultadas el 8 de octubre de 2026). Al TCF no se le aplica ningún descuento; en el Instituto Francés, una fecha fuera de calendario cuesta un 15 % más."),
         ("¿Cuáles son las próximas fechas del TCF Canada en Chile?", "En Santiago, el 19 de noviembre de 2026 (inscripciones hasta el 26 de octubre) y el 27 de noviembre de 2026 (hasta el 9 de noviembre); en Concepción, el 11 de noviembre de 2026, con inscripciones hasta el 13 de octubre. Ningún calendario 2027 estaba publicado el 8 de octubre de 2026."),
         ("¿Cuánto tardan los resultados del TCF Canada?", "La constancia llega en PDF por correo electrónico. El Instituto Francés anuncia de 10 a 15 días hábiles en su página del TCF Canada, pero de 3 a 5 semanas en sus condiciones generales: calcula un mes si tu trámite ante IRCC tiene una fecha límite."),
         ("¿IRCC acepta el TCF Canada rendido en Chile?", "Sí: la constancia la emite France Éducation international, sea cual sea el centro autorizado, y es válida por dos años. Asegúrate de elegir el TCF Canada y no el tout public, que no se acepta para Express Entry.")],
    also=[("/es/delf-chile/", "DELF y DALF en Chile", "El calendario nacional 2026 y los precios del Instituto Francés."),
          ("/es/tcf-canada-peru/", "TCF Canada en Perú", "Un solo centro, la Alianza Francesa de Lima."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="sitios del Instituto Francés de Chile (páginas del TCF, condiciones generales, preguntas frecuentes, calendario TCF 2026, plataforma de inscripción) y de la Alianza Francesa de Concepción (páginas del TCF, calendario y tarifas 2026, condiciones generales), consultados el 8 de octubre de 2026.",
))

PAGES.append(from_fr(
    "delf-chili", "es", "es-419", "Chili",
    slug="delf-chile", country_name="Chile",
    crumb="DELF en Chile",
    title="Examen DELF en Chile 2026: fechas, precios y centros",
    desc="Examen DELF y DALF en Chile: calendario nacional 2026 del Instituto Francés, sesión B2 del 4 y 5 de diciembre, precios (B2 137.000 pesos) y centros.",
    h1="DELF y DALF en Chile: los centros de examen, el calendario 2026 y los precios",
    intro="""En Chile, el DELF y el DALF siguen un <strong>calendario nacional</strong> fijado por el Instituto Francés de
Chile, que gestiona las certificaciones: un nivel por semana, en Santiago, Antofagasta, Concepción, Osorno o Talca
según el nivel. El 8 de octubre de 2026 solo quedaba abierta una sesión tout public: el <strong>DELF B2 del 4 y 5 de
diciembre</strong>, con inscripciones hasta el <strong>30 de octubre</strong>, a <strong>137.000 pesos</strong>. A
continuación: el calendario, los precios y los pasos a seguir, y luego los {n} centros de examen de la lista
oficial.""",
    facts=["<strong>{n} centros de examen</strong> en la lista de FEI del 8 de octubre de 2026 —Santiago, Concepción, Osorno, Antofagasta—, coordinados por el Instituto Francés de Chile.",
           "Calendario nacional: B1-B2 en abril, C1-C2 en mayo, de A1 a B2 en agosto, DALF en septiembre, B2 en diciembre; resultados unos <strong>tres meses</strong> después.",
           "Única sesión tout public todavía abierta el 8 de octubre de 2026: <strong>DELF B2 el 4 y 5 de diciembre</strong>, inscripciones hasta el <strong>30 de octubre</strong> (Santiago, Antofagasta, Osorno).",
           "Precios en el Instituto: <strong>A1 107.000 · A2 117.000 · B1 127.000 · B2 137.000 · C1 167.000 · C2 187.000 pesos</strong>.",
           "Examen <strong>en papel</strong> y presencial; el diploma, impreso en Francia, llega de tres a cuatro meses después de los resultados.",
           "Según el Instituto, en Chile el DELF es «una opción más económica que el TCF»."],
    stats=[("{n}", "centros de examen", "lista de FEI del 8 de octubre de 2026"), ("137.000", "pesos el DELF B2", "tarifas del Instituto Francés"),
           ("4-5 dic.", "DELF B2 tout public", "inscripciones hasta el 30 de octubre"), ("de por vida", "validez del diploma", "resultados en unos tres meses")],
    sections=[
        ("calendario", "El calendario nacional 2026", table(
            "Calendario DELF-DALF tout public 2026 del Instituto Francés de Chile, consultado el 8 de octubre de 2026.",
            ["Nivel", "Pruebas", "Inscripciones", "Resultados", "Ciudades"],
            [("B1", "17 de abril", "15 ene. – 15 mar.", "julio", "Antofagasta, Santiago"),
             ("B2", "24-25 de abril", "15 ene. – 15 mar.", "julio", "Antofagasta, Santiago"),
             ("C2 · C1", "15 de mayo · 22-23 de mayo", "15 ene. – 15 abr.", "agosto", "Antofagasta, Santiago"),
             ("A1 · A2 · B1", "7 · 14 · 21 de agosto", "15 ene. – 30 jun.", "noviembre", "Antofagasta, Santiago, Talca, Concepción, Osorno"),
             ("B2", "28-29 de agosto", "15 ene. – 30 jun.", "noviembre", "Antofagasta, Santiago, Concepción, Osorno"),
             ("C1 · C2", "4-5 sep. · 25-26 sep.", "hasta el 30 de julio", "diciembre", "Antofagasta, Concepción"),
             ("<strong>B2</strong>", "<strong>4-5 de diciembre</strong>", "<strong>15 ene. – 30 oct.</strong>", "febrero de 2027", "Antofagasta, Osorno, Santiago")]) + """
<p>La parte colectiva del tout public se rinde el viernes; la oral, el viernes o el sábado según el número de
inscritos. El DELF junior (octubre y noviembre de 2026) y el DELF Prim (del 5 al 7 de noviembre) habían cerrado sus
inscripciones el 14 de agosto y el 11 de septiembre; sus resultados se esperan para febrero de 2027. El calendario
2027 no estaba publicado el 8 de octubre de 2026.</p>"""),
        ("precios", "¿Cuánto cuesta el DELF en Chile?", table(
            "Tarifas 2026 del Instituto Francés de Chile y de la Alianza Francesa de Concepción, en pesos chilenos (CLP), consultadas el 8 de octubre de 2026.",
            ["Nivel", "Instituto Francés (Santiago)", "AF Concepción, tarifa reducida"],
            [("DELF A1", "107.000", "96.300"), ("DELF A2", "117.000", "105.300"), ("DELF B1", "127.000", "114.300"),
             ("<strong>DELF B2</strong>", "<strong>137.000</strong>", "123.300"), ("DALF C1", "167.000", "150.300"), ("DALF C2", "187.000", "168.300")], wide=False) + """
<p>La Alianza Francesa de Concepción aplica la misma tarifa normal que el Instituto; la tarifa reducida es para sus
alumnos, los del Lycée Charles de Gaulle y los de los establecimientos afiliados. El Instituto concede descuentos con
código (red «Le français au Chili», alumnos de las Alianzas y del Instituto…), que se piden mediante un formulario
antes de inscribirse; no publica ni su monto ni precios para el DELF junior y Prim.</p>"""),
        ("inscripcion", "Cómo inscribirte y recibir tu diploma", """<p>En Santiago, te inscribes en línea en la plataforma del Instituto Francés de Chile (ficha de alumno y luego
carrito); para Antofagasta, Osorno y Concepción, el Instituto remite directamente a la Alianza Francesa de la ciudad.
La citación llega por correo electrónico a más tardar cinco días antes del examen; preséntala con tu cédula de
identidad o tu pasaporte. Las pruebas se rinden <strong>en papel</strong>, de forma presencial.</p>

<p>Los resultados se publican en el sitio web del Instituto <strong>unos tres meses</strong> después del examen; a
solicitud, se entrega una constancia provisional. El diploma, impreso en Francia, llega a Chile de tres a cuatro
meses más tarde; lo retiras con un documento de identidad, o lo retira un tercero con una copia de tu cédula y un
poder simple. Para una solicitud de nacionalidad francesa, precisa el Instituto, se exige ese diploma físico:
anticípate.</p>"""),
    ],
    list_title="Los {n} centros de examen autorizados, ciudad por ciudad",
    faq=[("¿Cuándo es el próximo examen DELF en Chile?", "Para el tout public, el DELF B2 del 4 y 5 de diciembre de 2026 en Santiago, Antofagasta y Osorno, con inscripciones hasta el 30 de octubre de 2026: era la única sesión tout public todavía abierta el 8 de octubre de 2026. El calendario 2027 no estaba publicado."),
         ("¿Cuánto cuesta el DELF B2 en Chile?", "137.000 pesos chilenos en el Instituto Francés de Chile (tarifas 2026); la misma tarifa normal en la Alianza Francesa de Concepción, que cobra 123.300 pesos a sus alumnos y a los del Lycée Charles de Gaulle. El DALF cuesta 167.000 pesos (C1) y 187.000 pesos (C2)."),
         ("¿Cómo inscribirse en el DELF en Chile?", "En Santiago, en línea en la plataforma del Instituto Francés de Chile, con pago con tarjeta; en Antofagasta, Osorno y Concepción, directamente en la Alianza Francesa. La citación llega por correo electrónico a más tardar cinco días antes del examen."),
         ("¿Cuándo llegan los resultados y el diploma del DELF?", "Los resultados, unos tres meses después del examen, en el sitio web del Instituto Francés (constancia provisional a solicitud); el diploma, impreso en Francia, llega a Chile de tres a cuatro meses más tarde. Para una solicitud de nacionalidad francesa, se necesita ese diploma físico."),
         ("¿El DELF rendido en Chile es el mismo que en Francia?", "Sí: es el mismo diploma del Ministerio de Educación Nacional de Francia, válido de por vida, emitido por France Éducation international sea cual sea el país donde se rinda.")],
    also=[("/es/tcf-canada-chile/", "TCF Canada en Chile", "Dos centros, 299.000 pesos, las fechas de noviembre de 2026."),
          ("/es/delf-peru/", "DELF y DALF en Perú", "Cinco sesiones al año en las seis Alianzas Francesas."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="sitios del Instituto Francés de Chile (calendarios DELF-DALF tout public, junior y Prim 2026, páginas por nivel, condiciones generales, resultados, plataforma de inscripción) y de la Alianza Francesa de Concepción (calendario y tarifas DELF-DALF 2026), consultados el 8 de octubre de 2026.",
    notes={"antofagasta-alianza-francesa-de-antofagasta": "Sin sitio web: el Instituto Francés remite a su cuenta de Instagram. Sesiones tout public, junior y Prim del calendario nacional.",
           "osorno-alliance-francaise-d-osorno": "El sitio afosorno.cl seguía con los calendarios 2025 el 8 de octubre de 2026; B2 del 4-5 de diciembre en el calendario nacional."},
))

# ===========================================================================
# PERÚ
# ===========================================================================
PAGES.append(from_fr(
    "tcf-perou", "es", "es-419", "Pérou",
    slug="tcf-canada-peru", country_name="Perú",
    crumb="TCF Canada en Perú",
    title="TCF Canada en Lima, Perú: el único centro, precio y fechas",
    desc="El TCF Canada en Perú se presenta en la Alianza Francesa de Lima, único centro autorizado: 1,240 soles, nueve fechas en 2026, la última ya completa.",
    h1="TCF Canada en Perú: un solo centro, la Alianza Francesa de Lima",
    intro="""En Perú, el TCF solo se presenta en un lugar: la <strong>Alianza Francesa de Lima</strong>, en Miraflores, único
centro TCF autorizado por France Éducation international al 8 de octubre de 2026. Ofrece el TCF Canada, el TCF
Québec, el IRN, el DAP y el tout public. El TCF Canada cuesta <strong>1,240 soles</strong> (992 con tarifa de
miembro), con nueve fechas en 2026, pero la última, el <strong>11 de diciembre</strong>, ya figuraba como
<strong>completa</strong> el 8 de octubre. A continuación: lo que mostraba su sitio web, las fechas y qué hacer
cuando ya no hay cupo.""",
    facts=["<strong>1 solo centro TCF</strong> en Perú: la Alianza Francesa de Lima, avenida Arequipa 4595, Miraflores. Las demás Alianzas Francesas del país ofrecen el DELF, y algunas el TEF, pero no el TCF.",
           "<strong>TCF Canada: 1,240 soles</strong> (992 con tarifa de miembro); TCF Québec, 1,240 soles las cuatro pruebas; TCF tout public completo, 1,600 soles.",
           "<strong>Nueve fechas de TCF Canada en 2026</strong>, más o menos una al mes salvo en julio, agosto y noviembre; inscripciones cerradas de dos a tres semanas antes.",
           "⚠️ La sesión del <strong>11 de diciembre de 2026</strong>, última fecha del año, estaba <strong>completa</strong> el 8 de octubre; no había ninguna fecha de 2027 publicada.",
           "Inscripción y pago <strong>en línea</strong>, en la plataforma de la Alianza; edad mínima: 16 años.",
           "Resultados en <strong>3 a 4 semanas</strong>; hay que esperar <strong>30 días</strong> entre dos sesiones."],
    stats=[("1", "centro TCF", "Alianza Francesa de Lima"), ("1,240", "soles el TCF Canada", "992 con tarifa de miembro"),
           ("9", "fechas de TCF Canada", "en 2026"), ("30 días", "entre dos sesiones", "resultados en 3 a 4 semanas")],
    sections=[
        ("precios-y-fechas", "El TCF en la Alianza Francesa de Lima: precios y fechas 2026", table(
            "Calendario de inscripciones 2026 y plataforma de inscripción de la Alianza Francesa de Lima, consultados el 8 de octubre de 2026; fecha límite de inscripción entre paréntesis. El calendario impreso muestra los precios en dólares (TCF Canada 310 dólares); la plataforma cobra en soles (PEN) exactamente cuatro veces esos montos.",
            ["Versión", "Precio (público · miembro)", "Fechas 2026", "El 8 de octubre"],
            [("<strong>TCF Canada</strong>", "<strong>S/ 1,240</strong> · S/ 992; módulos por separado: comprensión oral 320, expresión oral 300", "23/01, 13/02, 05/03, 10/04, 22/05, 05/06, 11/09, 07/10, <strong>11/12</strong> (27/11)", "<strong>completo</strong>; ninguna fecha de 2027"),
             ("TCF Québec", "S/ 1,240 las cuatro pruebas; de S/ 300 a S/ 320 por prueba", "20/02, 13/03, 14/05, 10/07, <strong>26/11</strong> (03/11)", "a la venta"),
             ("TCF tout public", "completo S/ 1,600 · pruebas obligatorias S/ 1,000 · una prueba de expresión S/ 300", "22/01, 09/04, 03/07, 02/10, <strong>04/12</strong> (21/11)", "a la venta"),
             ("TCF DAP", "S/ 1,240", "<strong>04/12</strong> (21/11)", "a la venta"),
             ("TCF IRN («TCF ANF»)", "310 dólares en el calendario", "15/05, <strong>06/11</strong> (10/10)", "no figura en la plataforma")])),
        ("inscripcion", "Cómo inscribirte y qué hacer si no hay cupo", """<p>La inscripción se hace <strong>directamente en línea</strong>, en la plataforma de la Alianza Francesa de
Lima (aflima.extranet-aec.com): eliges el examen y la fecha, pagas, y una sesión llena aparece como «Lleno». Los
exámenes son solo presenciales, desde los 16 años. La Alianza no publica sus medios de pago ni reglas de cancelación,
reembolso o cambio de fecha: pregunta por ellos al servicio de exámenes antes de pagar
(examenes.intafl@alianzafrancesa.org.pe, o al (511) 610-8000, opción 3).</p>

<p>Con un solo centro y nueve fechas al año, el <strong>cupo</strong> es el verdadero cuello de botella. El 8 de
octubre de 2026, la sesión de TCF Canada del 11 de diciembre estaba completa y el calendario 2027 no estaba
publicado: vigila la plataforma cuando salga, como hacen los candidatos de otros países donde las sesiones se agotan
rápido. El TCF Québec del 26 de noviembre, todavía a la venta, no reemplaza al TCF Canada: IRCC no lo acepta. El
otro examen reconocido por IRCC es el TEF Canada, que vende la misma Alianza —su sesión con todas las pruebas del 9 de noviembre
seguía a la venta el 8 de octubre— y también Alianzas de provincia, como la de Arequipa, que ofrece «el TEF y el
TEFAQ».</p>

<p>Los resultados llegan de tres a cuatro semanas después del examen; la constancia es válida por dos años. Hay que
esperar <strong>30 días</strong> entre dos sesiones: con una fecha al mes, aproximadamente, un segundo intento toma al
menos un mes, a menudo dos.</p>"""),
    ],
    list_title="El centro TCF autorizado en Perú",
    faq=[("¿Dónde presentar el TCF Canada en Perú?", "En la Alianza Francesa de Lima (avenida Arequipa 4595, Miraflores), único centro TCF autorizado por France Éducation international en Perú al 8 de octubre de 2026. Las Alianzas Francesas de Arequipa, Cusco, Trujillo, Chiclayo y Piura ofrecen el DELF, y algunas el TEF, pero no el TCF."),
         ("¿Cuánto cuesta el TCF Canada en Perú?", "1,240 soles, o 992 soles con la tarifa de miembro de la Alianza Francesa de Lima (plataforma de inscripción, 8 de octubre de 2026). El calendario impreso lo muestra a 310 dólares."),
         ("¿Cuándo es la próxima fecha del TCF Canada en Lima?", "El 8 de octubre de 2026, la última fecha del año —el 11 de diciembre, con inscripciones hasta el 27 de noviembre— estaba completa, y el calendario 2027 no estaba publicado. En 2026, la Alianza ofreció nueve fechas: enero, febrero, marzo, abril, dos en mayo-junio, septiembre, octubre y diciembre."),
         ("¿Cuánto hay que esperar entre dos intentos del TCF?", "Treinta días, según la Alianza Francesa de Lima. Con una sesión al mes, aproximadamente, un segundo intento toma entonces al menos un mes, a menudo dos."),
         ("¿TCF Canada o TEF Canada en Perú?", "IRCC acepta los dos. En Perú, el TCF Canada solo existe en Lima, mientras que el TEF Canada también lo ofrecen Alianzas de provincia, como la de Arequipa.")],
    also=[("/es/delf-peru/", "DELF y DALF en Perú", "Cinco sesiones al año, la próxima el 28 de noviembre de 2026."),
          ("/es/tcf-canada-chile/", "TCF Canada en Chile", "Dos centros, 299.000 pesos chilenos."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="sitio web y plataforma de inscripción de la Alianza Francesa de Lima (páginas «Exámenes internacionales» y «Certificaciones internacionales», calendario de inscripciones 2026) y sitio web de la Alianza Francesa de Arequipa, consultados el 8 de octubre de 2026.",
))

PAGES.append(from_fr(
    "delf-perou", "es", "es-419", "Pérou",
    slug="delf-peru", country_name="Perú",
    crumb="DELF en Perú",
    title="Examen DELF en Perú 2026: fechas, precios y centros",
    desc="DELF y DALF en Perú: 6 Alianzas Francesas, la sesión del 28 de noviembre de 2026 (inscripciones hasta el 16 de octubre) y los precios (B2 461 soles).",
    h1="DELF y DALF en Perú: los 6 centros de examen, las fechas 2026 y los precios",
    intro="""En Perú, el DELF y el DALF se presentan en las <strong>seis Alianzas Francesas</strong> del país —Lima,
Arequipa, Cusco, Trujillo, Chiclayo, Piura—, bajo la gestión central de la Alianza Francesa de Lima. Hay cinco
sesiones tout public al año, los sábados: la próxima será el <strong>28 de noviembre de 2026</strong>, con inscripciones
hasta el <strong>16 de octubre</strong>. El DELF B2 cuesta <strong>461 soles</strong> (369 con un convenio de la
Alianza), y los alumnos de las Alianzas presentan gratis el examen de su nivel.""",
    facts=["<strong>{n} centros de examen</strong> (lista de FEI del 8 de octubre de 2026), todos Alianzas Francesas; gestión central en la Alianza Francesa de Lima.",
           "<strong>Cinco sesiones tout public en 2026</strong>, los sábados: 7 de marzo, 9 de mayo, 4 de julio, 5 de septiembre y <strong>28 de noviembre</strong> (inscripciones del 8 de septiembre al 16 de octubre).",
           "Precios para un candidato libre: <strong>A1 286 · A2 345 · B1 385 · B2 461 · C1 543 · C2 618 soles</strong>; 20 % menos con un convenio de la Alianza.",
           "Tarifa <strong>Campus France</strong>: B2 276 soles, C1 326 soles (Trujillo, Arequipa).",
           "Resultados en cuatro a cinco semanas; el diploma, impreso en Francia, llega de cuatro a cinco meses después de la sesión.",
           "Los alumnos de las Alianzas pueden inscribirse <strong>gratis</strong> al examen de su nivel."],
    stats=[("{n}", "Alianzas Francesas", "lista de FEI del 8 de octubre de 2026"), ("461", "soles el DELF B2", "369 con convenio de la Alianza"),
           ("28 nov.", "próxima sesión", "inscripciones hasta el 16 oct."), ("de por vida", "validez del diploma", "cinco sesiones al año")],
    sections=[
        ("calendario", "Las sesiones 2026", table(
            "Calendarios DELF-DALF, DELF junior y DELF Prim 2026 de la Alianza Francesa de Lima (gestión central), consultados el 8 de octubre de 2026.",
            ["Examen", "Fechas 2026", "Inscripciones para la última sesión"],
            [("DELF-DALF tout public", "sábados 7 de marzo, 9 de mayo, 4 de julio, 5 de septiembre, <strong>28 de noviembre</strong>", "<strong>8 de septiembre – 16 de octubre de 2026</strong>"),
             ("DELF junior", "viernes 6 de marzo, 3 de julio, 4 de septiembre, <strong>13 y 20 de noviembre</strong>", "17 de agosto – 18 de septiembre (cerradas; 25 de septiembre en Arequipa)"),
             ("DELF Prim", "viernes 8 de mayo y <strong>23 de octubre</strong>", "3 de agosto – 11 de septiembre (cerradas)")], wide=False) + """
<p>La prueba oral no siempre es el mismo día que la escrita: en Arequipa se presenta la víspera (viernes 27 de
noviembre). Las Alianzas de Cusco y de Trujillo siguen el mismo calendario; en Trujillo, las inscripciones cierran el
16 de octubre a las 13:00. Ninguna Alianza había publicado el calendario 2027 el 8 de octubre de 2026.</p>"""),
        ("precios", "¿Cuánto cuesta el DELF en Perú?", table(
            "Tarifas 2026 de la Alianza Francesa de Lima, idénticas en Arequipa y Trujillo, en soles (PEN), consultadas el 8 de octubre de 2026.",
            ["Nivel", "Candidato libre", "Convenio Alianza"],
            [("DELF A1", "286", "229"), ("DELF A2", "345", "276"), ("DELF B1", "385", "307"),
             ("<strong>DELF B2</strong>", "<strong>461</strong>", "369"), ("DALF C1", "543", "435"), ("DALF C2", "618", "494")], wide=False) + """
<p>El DELF junior va de 257 soles (A1) a 420 soles (B2) para un candidato libre, y el DELF Prim de 242 soles (A1.1) a
303 soles (A2), con tarifas reducidas para los alumnos de las Alianzas y de los colegios asociados. Los candidatos
<strong>Campus France</strong> pagan 276 soles por el B2 y 326 soles por el C1, según las Alianzas de Trujillo y de
Arequipa.</p>"""),
        ("inscripcion", "Cómo inscribirte y recibir tu diploma", """<p>En Lima, te inscribes <strong>en línea</strong>, en la plataforma de la Alianza Francesa
(aflima.extranet-aec.com); en Arequipa, en línea o en la oficina (calle Santa Catalina 208); en Trujillo, por correo
electrónico a la oficina de exámenes, con cupos limitados. Las páginas de exámenes de Chiclayo y de Piura no estaban
actualizadas el 8 de octubre de 2026 —las de Piura remiten a la tienda en línea de Lima—. La citación llega por
correo electrónico una semana antes; la prueba escrita y la oral pueden ser en días y lugares distintos.</p>

<p>Los resultados salen <strong>de cuatro a cinco semanas</strong> después de la sesión —para la de noviembre de 2026,
Arequipa anuncia el 31 de enero de 2027— y, a solicitud, se entrega una constancia de aprobación. El diploma, impreso
en Francia, llega de cuatro a cinco meses después de la sesión (unos tres meses según Arequipa). No tardes en retirarlo:
la Alianza Francesa de Lima cobra 100 soles por guardar un diploma de más de tres años.</p>"""),
    ],
    list_title="Los {n} centros de examen autorizados, ciudad por ciudad",
    faq=[("¿Cuándo es el próximo examen DELF en Perú?", "El sábado 28 de noviembre de 2026 para el DELF y el DALF tout public, en las Alianzas Francesas del país, con inscripciones del 8 de septiembre al 16 de octubre de 2026. La prueba oral puede ser otro día —la víspera en Arequipa—. El calendario 2027 no estaba publicado el 8 de octubre de 2026."),
         ("¿Cuánto cuesta el DELF B2 en Perú?", "461 soles para un candidato libre, 369 soles con un convenio de la Alianza Francesa (tarifas 2026 de Lima, Arequipa y Trujillo). Los candidatos Campus France pagan 276 soles por el B2 y 326 soles por el C1."),
         ("¿Cómo inscribirse en el DELF en Perú?", "En Lima, en línea en la plataforma de la Alianza Francesa; en Arequipa, en línea o en la oficina; en Trujillo, por correo electrónico a la oficina de exámenes, con cupos limitados. La citación llega por correo electrónico una semana antes del examen."),
         ("¿Cuándo salen los resultados del DELF?", "De cuatro a cinco semanas después de la sesión, según la Alianza Francesa de Lima; para la sesión de noviembre de 2026, Arequipa anuncia el 31 de enero de 2027. El diploma, impreso en Francia, llega de cuatro a cinco meses después de la sesión."),
         ("¿Los alumnos de la Alianza Francesa pagan el DELF?", "No: la Alianza Francesa de Lima permite a sus alumnos inscribirse gratis en el examen DELF-DALF de su nivel. En Trujillo, hay que haber cursado todos los ciclos del nivel en la Alianza e inscribirse dentro de los seis meses.")],
    also=[("/es/tcf-canada-peru/", "TCF Canada en Perú", "Un solo centro, la Alianza Francesa de Lima."),
          ("/es/delf-ecuador/", "DELF y DALF en Ecuador", "Las sesiones de noviembre y diciembre de 2026, B2 a 200 dólares."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="sitios de las Alianzas Francesas de Lima (páginas de exámenes, calendarios DELF-DALF, junior y Prim 2026, plataforma de inscripción), Arequipa, Cusco, Trujillo, Chiclayo y Piura, consultados el 8 de octubre de 2026.",
))

# ===========================================================================
# ECUADOR
# ===========================================================================
PAGES.append(from_fr(
    "tcf-equateur", "es", "es-419", "Équateur",
    slug="tcf-canada-ecuador", country_name="Ecuador",
    crumb="TCF Canada en Ecuador",
    title="TCF Canada en Ecuador (Quito, Guayaquil, Cuenca): precios",
    desc="TCF Canada en Ecuador: la Alianza Francesa de Cuenca (200 dólares, a solicitud), la de Guayaquil (300 dólares) y Quito, que orienta hacia el TEF.",
    h1="TCF Canada en Ecuador: los 3 centros autorizados, sus precios y sus fechas",
    intro="""En Ecuador, tres Alianzas Francesas están autorizadas para el TCF —<strong>Quito, Guayaquil y Cuenca</strong>—,
todas con sesiones en computadora según France Éducation international. El 8 de octubre de 2026, solo dos publicaban
el TCF Canada: <strong>Cuenca, a 200 dólares</strong>, con una sesión que se abre a solicitud con quince días de
anticipación, y <strong>Guayaquil, a 300 dólares</strong>, sin fecha publicada. Quito solo ofrecía el TCF tout public
y orienta hacia el TEF Canada para la inmigración.""",
    facts=["<strong>3 centros autorizados</strong> (lista de FEI del 8 de octubre de 2026): las Alianzas Francesas de Quito, Guayaquil y Cuenca.",
           "<strong>Cuenca: TCF Canada a 200 dólares</strong>, sin calendario: la sesión se abre a solicitud, al menos <strong>15 días</strong> antes, un martes, miércoles o jueves.",
           "<strong>Guayaquil: TCF Canada a 300 dólares</strong>; ninguna fecha publicada ni a la venta el 8 de octubre de 2026.",
           "<strong>Quito</strong>: solo TCF tout public (220 dólares, 300 con la prueba oral); para Canadá, la Alianza ofrece el <strong>TEF Canada</strong> (300 dólares).",
           "Ecuador está dolarizado: todos los precios están en dólares estadounidenses.",
           "Ninguna de las tres Alianzas publica reglas de cancelación o de reembolso: pregúntalas antes de pagar."],
    stats=[("{n}", "centros autorizados", "lista de FEI del 8 de octubre de 2026"), ("200 dólares", "el TCF Canada en Cuenca", "300 dólares en Guayaquil"),
           ("15 días", "de anticipación", "sesiones a solicitud en Cuenca"), ("2 años", "de validez", "resultados en 15 días en Cuenca")],
    sections=[
        ("centros-tcf-canada", "El TCF Canada en Ecuador, centro por centro", releve([
            ("Alianza Francesa de Cuenca", "<strong>Canada</strong>, Québec, IRN, DAP, tout public",
             "Canada <strong>USD 200</strong> · IRN 200 · DAP 250 · Québec 70 por prueba · tout public: pruebas obligatorias 150, +50 por cada prueba de expresión",
             "Sin calendario: sesión abierta a solicitud, al menos 15 días antes, un martes, miércoles o jueves; resultados «después de 15 días»."),
            ("Alianza Francesa de Guayaquil", "<strong>Canada</strong>, tout public, completo",
             "Canada <strong>USD 300</strong> · tout public 160 · completo 300 · prueba opcional 80",
             "Ninguna fecha publicada; ninguna sesión de TCF en la plataforma el 8 de octubre de 2026, y botones de inscripción sin enlace: contacta directamente a la Alianza."),
            ("Alianza Francesa de Quito", "solo tout public; TEF Canada y TEFAQ para la inmigración",
             "TCF tout public USD 220 · con la expresión oral USD 300 (TEF Canada USD 300)",
             "TCF tout public el 24 de abril y el 2 de octubre de 2026, dos sesiones ya pasadas; plataforma: «ningún examen a la venta»."),
        ], "es-419", "Lo que mostraba el sitio web de cada centro el 8 de octubre de 2026. «Sin datos»: no publicado o no verificado; lo que diga el sitio del centro es lo que vale.")),
        ("inscripcion", "Cómo inscribirte en el TCF Canada en Ecuador", """<p>En <strong>Cuenca</strong>, el trámite es el más claro: llenas el formulario de inscripción TCF 2026 (tipo de
TCF, fecha deseada —al menos quince días después—, número de cédula o de pasaporte, motivo «Inmigración a Canadá»),
verificas que la fecha esté disponible <em>antes</em> de pagar, pagas por transferencia o depósito en la cuenta de la
Alianza y envías el formulario y el comprobante a coordo.peda@afcuenca.org.ec, con copia a info@afcuenca.org.ec. La
Alianza anuncia los resultados después de quince días y una constancia válida por dos años.</p>

<p>En <strong>Guayaquil</strong>, la página del TCF muestra los precios, pero sus botones «Inscríbete» no llevan a
ninguna parte y la plataforma solo vendía DELF el 8 de octubre de 2026: pide una fecha a info@afguayaquil.org.ec. En
<strong>Quito</strong> no hay TCF Canada: la Alianza orienta hacia el TEF Canada, el otro examen aceptado por
IRCC.</p>

<p>En todos los centros, inscríbete con el documento de identidad de tu expediente de IRCC y respeta al menos 20 días
entre dos intentos, la regla de France Éducation international. Desconfía de las páginas que ofrecen «comprar» una
constancia del TCF y que aparecen en los resultados de búsqueda: una constancia solo se obtiene presentando el examen
en un centro autorizado.</p>"""),
    ],
    list_title="Los {n} centros TCF autorizados en Ecuador",
    faq=[("¿Dónde presentar el TCF Canada en Ecuador?", "En la Alianza Francesa de Cuenca, que abre una sesión a solicitud, o en la de Guayaquil, que anuncia el TCF Canada a 300 dólares, sin fecha publicada al 8 de octubre de 2026. La Alianza Francesa de Quito, tercer centro autorizado, solo ofrecía el TCF tout public."),
         ("¿Cuánto cuesta el TCF Canada en Ecuador?", "200 dólares en la Alianza Francesa de Cuenca (documento «INFO DELF | DALF | TCF 2026») y 300 dólares en la de Guayaquil (página del TCF), según lo consultado el 8 de octubre de 2026."),
         ("¿Hay que esperar una sesión del TCF Canada en Cuenca?", "No: no hay calendario; la Alianza abre una sesión a solicitud, con al menos quince días de anticipación, un martes, miércoles o jueves. Verifica que la fecha esté disponible antes de pagar."),
         ("¿Se puede presentar el TCF Canada en Quito?", "No, al menos al 8 de octubre de 2026: la Alianza Francesa de Quito solo publicaba el TCF tout public (220 dólares, dos sesiones en 2026). Para inmigrar a Canadá, ofrece el TEF Canada, que IRCC acepta igual que el TCF Canada."),
         ("¿IRCC acepta el TCF Canada presentado en Ecuador?", "Sí: la constancia de resultados la emite France Éducation international, sea cual sea el centro autorizado, y es válida por dos años. Solo verifica que en tu citación figure el TCF Canada y no el tout public.")],
    also=[("/es/delf-ecuador/", "DELF y DALF en Ecuador", "Las sesiones de noviembre y diciembre de 2026, B2 a 200 dólares."),
          ("/es/tcf-canada-peru/", "TCF Canada en Perú", "Un solo centro, la Alianza Francesa de Lima."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="sitios de las Alianzas Francesas de Cuenca (páginas del TCF, documento «INFO DELF | DALF | TCF 2026», formulario de inscripción TCF 2026), de Guayaquil (página del TCF, agenda, plataforma de inscripción) y de Quito (página Diplomas, calendario de pruebas 2026, plataforma de inscripción), consultados el 8 de octubre de 2026.",
))

PAGES.append(from_fr(
    "delf-equateur", "es", "es-419", "Équateur",
    slug="delf-ecuador", country_name="Ecuador",
    crumb="DELF en Ecuador",
    title="Examen DELF en Ecuador 2026: fechas, precios y centros",
    desc="DELF y DALF en Ecuador: las sesiones de noviembre y diciembre de 2026 en Quito, Guayaquil y Cuenca, los precios (B2 200 dólares, mitad para alumnos AF).",
    h1="DELF y DALF en Ecuador: los 5 centros de examen, las fechas 2026 y los precios",
    intro="""En Ecuador, el DELF y el DALF se presentan en cinco Alianzas Francesas —Quito, Guayaquil, Cuenca, Loja,
Portoviejo—, bajo la gestión central de la Alianza Francesa de Quito. El 8 de octubre de 2026 quedaban dos sesiones
tout public: <strong>del 23 al 27 de noviembre</strong> (inscripciones hasta el 6 de noviembre en Quito y hasta el 26
de octubre en Guayaquil) y <strong>del 8 al 14 de diciembre</strong> (hasta el 13 de noviembre). El DELF B2 cuesta
<strong>200 dólares</strong>; los alumnos de las Alianzas pagan la mitad.""",
    facts=["<strong>{n} centros de examen</strong> (lista de FEI del 8 de octubre de 2026), todos Alianzas Francesas; gestión central en Quito.",
           "Sesiones tout public 2026: marzo, junio, <strong>23-27 de noviembre</strong> y <strong>8-14 de diciembre</strong>; Cuenca agregó una sesión en septiembre.",
           "Tarifas comunes, en dólares: <strong>A1 96 · A2 120 · B1 160 · B2 200 · C1 y C2 240</strong>; alumnos de las Alianzas: <strong>50 % de descuento</strong>.",
           "DELF junior: del 1 al 4 de diciembre de 2026, inscripciones del 19 de octubre al 13 de noviembre.",
           "Inscripción en línea en Guayaquil, con formulario y transferencia en Cuenca, y contactando al servicio de exámenes en Quito.",
           "Plazos de los resultados y del diploma: no publicados por las tres Alianzas principales."],
    stats=[("{n}", "Alianzas Francesas", "lista de FEI del 8 de octubre de 2026"), ("200 dólares", "el DELF B2", "100 dólares para alumnos AF"),
           ("23-27 nov.", "próxima sesión", "luego del 8 al 14 de diciembre"), ("de por vida", "validez del diploma", "el mismo diploma que en Francia")],
    sections=[
        ("calendario", "Las sesiones de fines de 2026", table(
            "Calendario de pruebas 2026 de la Alianza Francesa de Quito (gestión central), completado con los de Guayaquil y Cuenca, consultado el 8 de octubre de 2026.",
            ["Sesión", "Inscripciones", "A1", "A2", "B1", "B2", "C1", "C2"],
            [("<strong>Tout public, noviembre</strong>", "5 oct. – 6 nov. (Quito) · 28 sep. – 26 oct. (Guayaquil)", "23/11", "23/11", "24/11", "25/11", "26/11", "27/11"),
             ("<strong>Tout public, diciembre</strong>", "5 oct. – 13 nov.", "08/12", "08/12", "09/12", "10/12", "11/12", "14/12"),
             ("Junior, diciembre", "19 oct. – 13 nov.", "01/12", "02/12", "03/12", "04/12", "—", "—")]) + """
<p>Antes, en 2026, las sesiones tout public se habían realizado en marzo y en junio, con una sesión junior y una
sesión Prim en junio; Cuenca agregó una sesión tout public del 21 al 25 de septiembre y una sesión Prim y junior en
enero. Ninguna Alianza había publicado el calendario 2027 el 8 de octubre de 2026.</p>"""),
        ("precios", "¿Cuánto cuesta el DELF en Ecuador?", table(
            "Tarifas comunes de las Alianzas Francesas de Quito, Cuenca y Guayaquil, en dólares estadounidenses, consultadas el 8 de octubre de 2026.",
            ["Nivel", "Público general", "Alumnos de las Alianzas"],
            [("DELF A1 (Prim A1.1)", "96", "48"), ("DELF A2 (Prim A1)", "120", "60"), ("DELF B1 (Prim A2)", "160", "80"),
             ("<strong>DELF B2</strong>", "<strong>200</strong>", "100"), ("DALF C1", "240", "120"), ("DALF C2", "240", "120")], wide=False) + """
<p>El DELF junior sigue las mismas tarifas, nivel por nivel. Las tarifas que muestra la Alianza Francesa de Loja son
de 2024; las de Portoviejo no se publican en ninguna parte: la Alianza no tiene sitio web.</p>"""),
        ("inscripcion", "Cómo inscribirte", """<p>En <strong>Guayaquil</strong>, la inscripción se hace en línea, en la plataforma de la Alianza
(afguayaquil.extranet-aec.com): agregas la sesión al carrito y pagas. En <strong>Cuenca</strong>, llenas el
formulario DELF-DALF, pagas por transferencia o depósito en la cuenta de la Alianza y envías el formulario y el
comprobante a la coordinación pedagógica (coordo.peda@afcuenca.org.ec). En <strong>Quito</strong>, la plataforma no
mostraba ningún examen a la venta el 8 de octubre de 2026: contacta al servicio de exámenes (página «Diplomas» del
sitio web, 02 224 6589, extensión 116), que te guía en la inscripción.</p>

<p>Ninguna de las tres Alianzas publica el plazo de los resultados ni el de la entrega del diploma: si tu
trámite —admisión en la universidad, solicitud de visa— tiene una fecha límite, pregunta por esos plazos al inscribirte.</p>"""),
    ],
    list_title="Los {n} centros de examen autorizados, ciudad por ciudad",
    faq=[("¿Cuándo es el próximo examen DELF en Ecuador?", "Del 23 al 27 de noviembre de 2026 para el tout public (A1 y A2 el 23, B1 el 24, B2 el 25, C1 el 26, C2 el 27), con inscripciones hasta el 6 de noviembre en Quito y hasta el 26 de octubre en Guayaquil; luego, del 8 al 14 de diciembre de 2026, con inscripciones hasta el 13 de noviembre."),
         ("¿Cuánto cuesta el DELF B2 en Ecuador?", "200 dólares, según las tarifas comunes de las Alianzas Francesas de Quito, Guayaquil y Cuenca; 100 dólares para sus alumnos, que tienen un 50 % de descuento. El DALF C1 o C2 cuesta 240 dólares."),
         ("¿Cómo inscribirse en el DELF en Ecuador?", "En Guayaquil, en línea en la plataforma de la Alianza; en Cuenca, con el formulario DELF-DALF, una transferencia o un depósito bancario y luego un correo a la coordinación pedagógica; en Quito, contactando al servicio de exámenes, ya que la plataforma no mostraba ningún examen a la venta el 8 de octubre de 2026."),
         ("¿Hay DELF junior en Ecuador?", "Sí: del 1 al 4 de diciembre de 2026 (A1 el 1, A2 el 2, B1 el 3, B2 el 4), con inscripciones del 19 de octubre al 13 de noviembre de 2026, al mismo precio que el tout public. El DELF Prim solo tuvo una sesión en 2026, en junio."),
         ("¿El DELF presentado en Ecuador es válido en Francia?", "Sí: es el mismo diploma, emitido por el Ministerio de Educación Nacional de Francia y válido de por vida, sea cual sea el país donde se presente.")],
    also=[("/es/tcf-canada-ecuador/", "TCF Canada en Ecuador", "Cuenca y Guayaquil lo ofrecen, de 200 a 300 dólares."),
          ("/es/delf-peru/", "DELF y DALF en Perú", "Cinco sesiones al año, B2 a 461 soles."),
          ("/es/", "TCF Canada y DELF, país por país", "España y América Latina.")],
    sources="sitios de las Alianzas Francesas de Quito (página Diplomas, calendario de pruebas 2026, plataforma de inscripción), de Guayaquil (página de certificados, anuncio de las inscripciones DELF-DALF, plataforma de inscripción), de Cuenca (documento «INFO DELF | DALF | TCF 2026») y de Loja (página de certificaciones), consultados el 8 de octubre de 2026.",
))


# ===========================================================================
# /es/ — página de entrada (make_pays.hub("es")). Cifras tomadas de las páginas de cada país.
# ===========================================================================
def _hub_table():
    from pays_i18n import table
    rows = [("España", "/es/tcf-canada-espana/", "11 centros de 14, de 275 a 287 €", "/es/delf-espana/", "32 centros, calendario nacional, B2 192 € en 2027"),
            ("México", "/es/tcf-canada-mexico/", "5 centros de 11, de 4,800 a 6,500 pesos", "/es/delf-mexico/", "71 centros, B2 2,500 pesos"),
            ("Colombia", "/es/tcf-canada-colombia/", "las 7 Alianzas Francesas, desde 1.050.000 pesos", "/es/delf-colombia/", "15 Alianzas Francesas, B2 490.000 pesos"),
            ("Argentina", "/es/tcf-canada-argentina/", "4 centros, precio a solicitud", "/es/delf-argentina/", "28 Alianzas Francesas, B2 163 € (295.030 pesos)"),
            ("Chile", "/es/tcf-canada-chile/", "2 centros, 299.000 pesos", "/es/delf-chile/", "4 centros, B2 137.000 pesos"),
            ("Perú", "/es/tcf-canada-peru/", "1 centro en Lima, 1,240 soles", "/es/delf-peru/", "6 Alianzas Francesas, B2 461 soles"),
            ("Ecuador", "/es/tcf-canada-ecuador/", "Cuenca 200 dólares, Guayaquil 300", "/es/delf-ecuador/", "5 Alianzas Francesas, B2 200 dólares")]
    return table("El TCF Canada y el DELF-DALF en siete países, según los sitios web de los centros el 8 de octubre de 2026. Precios en moneda local, para un candidato libre.",
                 ["País", "TCF Canada", "DELF · DALF"],
                 [(f"<strong>{p}</strong>", f'<a href="{u1}">{t1}</a>', f'<a href="{u2}">{t2}</a>') for p, u1, t1, u2, t2 in rows], wide=False)


HUB = dict(
    variant="es-419", accent="accent-tcf", crumb="Centros de examen", read=3,
    title="TCF Canada y DELF: centros de examen por país (2026)",
    desc="Dónde presentar el TCF Canada y el DELF en España, México, Colombia, Argentina, Chile, Perú y Ecuador: centros autorizados, precios y fechas de 2026.",
    h1="TCF Canada y DELF en España y América Latina: dónde presentarlos",
    lang_links='<p class="langs"><a href="/en/" hreflang="en" lang="en">In English</a> · <a href="/centres/" hreflang="fr" lang="fr">En français</a></p>',
    intro="""Para el <strong>TCF Canada</strong> —uno de los dos exámenes de francés que acepta IRCC para emigrar a
Canadá— y para los diplomas <strong>DELF</strong> y <strong>DALF</strong>, cada página reúne los centros autorizados
por France Éducation international en un país, lo que mostraba el sitio web de cada centro el 8 de octubre de 2026
—precios, fechas, versiones— y cómo inscribirte. Siete países: España, México, Colombia, Argentina, Chile, Perú y
Ecuador.""",
    facts=["<strong>No todos los centros TCF ofrecen el TCF Canada</strong>: 11 de 14 en España, 5 de 11 en México, los 7 de Colombia.",
           "TCF Canada: de 275 a 287 € en España, de 4,800 a 6,500 pesos en México, desde 1.050.000 pesos en Colombia, 299.000 pesos en Chile, 1,240 soles en Perú, 200 a 300 dólares en Ecuador.",
           "DELF B2: 192 € en España (2027), 2,500 pesos en México, 490.000 pesos en Colombia, 137.000 pesos en Chile, 461 soles en Perú, 200 dólares en Ecuador, 163 € (295.030 pesos) en Argentina.",
           "Un diploma DELF o DALF es válido de por vida; los resultados del TCF Canada, dos años."],
    toc=[("paises", "Siete países, dos exámenes"), ("tcf-canada", "TCF Canada"), ("delf", "DELF y DALF")],
    body="""
<div class="stats">
<div class="stat"><b>7</b><span>países</span><em>España y América Latina</em></div>
<div class="stat"><b>14</b><span>páginas</span><em>TCF Canada y DELF-DALF</em></div>
<div class="stat"><b>8 oct.</b><span>2026</span><em>revisión de los sitios de los centros</em></div>
</div>

<h2 id="paises">Siete países, dos exámenes</h2>
""" + _hub_table() + """

<h2 id="tcf-canada">TCF Canada: antes de inscribirte</h2>
<p>El TCF Canada es un <strong>test</strong>: no se aprueba ni se reprueba, sitúa tu nivel en cada prueba, y IRCC
convierte el resultado en niveles NCLC. La constancia de resultados la emite France Éducation international,
sea cual sea el centro, y es válida dos años. Dos cosas que conviene saber antes de pagar: <strong>un centro
autorizado para el TCF no ofrece necesariamente la versión Canada</strong> —cada página indica qué centros la
anunciaban en su sitio web—, y las sesiones se llenan rápido en varios países. IRCC acepta también el TEF Canada.</p>
<p><a href="/es/tcf-canada-espana/">España</a> · <a href="/es/tcf-canada-mexico/">México</a> ·
<a href="/es/tcf-canada-colombia/">Colombia</a> · <a href="/es/tcf-canada-argentina/">Argentina</a> ·
<a href="/es/tcf-canada-chile/">Chile</a> · <a href="/es/tcf-canada-peru/">Perú</a> ·
<a href="/es/tcf-canada-ecuador/">Ecuador</a> — y en inglés: <a href="/en/tcf-canada-test-centres/" lang="en">Canadá</a>,
<a href="/en/tcf-canada-usa/" lang="en">Estados Unidos</a>, <a href="/en/tcf-canada-uk/" lang="en">Reino Unido</a>.</p>

<h2 id="delf">DELF y DALF: el diploma</h2>
<p>El DELF (A1 a B2) y el DALF (C1, C2) son <strong>diplomas</strong> del Ministerio de Educación de Francia: se
aprueban nivel por nivel y son válidos de por vida. En cada país, un organismo de gestión central fija el
calendario de sesiones —y a menudo las tarifas—, y te inscribes directamente en un centro: Alianza Francesa,
Instituto Francés, universidad.</p>
<p><a href="/es/delf-espana/">España</a> · <a href="/es/delf-mexico/">México</a> ·
<a href="/es/delf-colombia/">Colombia</a> · <a href="/es/delf-argentina/">Argentina</a> ·
<a href="/es/delf-chile/">Chile</a> · <a href="/es/delf-peru/">Perú</a> ·
<a href="/es/delf-ecuador/">Ecuador</a> — y en inglés: <a href="/en/delf-usa/" lang="en">Estados Unidos</a>,
<a href="/en/delf-uk/" lang="en">Reino Unido</a>.</p>
""",
    faq=[("¿Dónde presentar el TCF Canada en América Latina?", "En México (5 centros, de 4,800 a 6,500 pesos), Colombia (las 7 Alianzas Francesas, desde 1.050.000 pesos), Chile (2 centros, 299.000 pesos), Perú (la Alianza Francesa de Lima, 1,240 soles), Ecuador (Cuenca 200 dólares, Guayaquil 300) y Argentina (4 centros, precio a solicitud). Precios revisados el 8 de octubre de 2026."),
         ("¿Cuál es la diferencia entre el TCF Canada y el DELF?", "El TCF Canada es un test: sitúa tu nivel, con resultados válidos dos años, y es uno de los dos exámenes de francés que acepta IRCC, junto con el TEF Canada. El DELF y el DALF son diplomas: se aprueban nivel por nivel y son válidos de por vida."),
         ("¿Cuánto cuesta el DELF B2?", "Depende del país: 192 € en España (tarifa 2027), 2,500 pesos en México, 490.000 pesos en Colombia, 137.000 pesos en Chile, 461 soles en Perú, 200 dólares en Ecuador y 163 € (295.030 pesos) en Argentina. Precios revisados el 8 de octubre de 2026."),
         ("¿Se puede presentar el TCF Canada en cualquier centro TCF?", "No: un centro autorizado para el TCF no ofrece necesariamente la versión Canada. Cada página de país indica qué centros la anunciaban en su sitio web el 8 de octubre de 2026.")],
    also=[("/en/tcf-canada-test-centres/", "TCF Canada en Canadá (en inglés)", "Los 47 centros autorizados, provincia por provincia."),
          ("/en/tcf-canada-usa/", "TCF Canada en Estados Unidos (en inglés)", "9 de los 18 centros lo ofrecen, de 330 a 460 dólares."),
          ("/ou-passer/", "Todos los países (en francés)", "1067 centros en 35 países, con sus datos de contacto.")],
    sources="""<strong>Fuentes.</strong> Listas de centros de examen de France Éducation international (filtros por país,
tipos «TCF» y «DELF-DALF»), consultadas el 8 de octubre de 2026, y los sitios web de los centros citados en cada
página, consultados el mismo día. Los precios y las fechas cambian sin aviso: verifícalos en el sitio del centro
antes de pagar.""",
    cta_h2="El centro te da la fecha; el nivel depende de ti",
    cta_p="""Cada sesión se paga completa y no se puede repetir de inmediato. Los simulacros de la app
«TCF DELF TEF: Tests 2026» reproducen el formato oficial de cada examen — TCF Canada, DELF B1, DELF B2, DALF C1 — con
la puntuación del examen real y corrección con IA de la expresión escrita y oral. La app está en español.""",
)
