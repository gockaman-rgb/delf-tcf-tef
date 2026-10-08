# -*- coding: utf-8 -*-
"""Blocs des pages traduites (08/10/2026) : exercices, sujets, calculateur NCLC en anglais.

exo() et sujet() reprennent le balisage de articles_exos_tcf_canada.py / articles_exos_2.py : l'exercice
(texte, audio, question, options) reste en FRANÇAIS — c'est un examen de français — ; consignes et
explications sont dans la langue de la page. CALC_EN est le calculateur de nclc_calc.py, mêmes bornes IRCC,
libellés anglais (le NCLC s'y appelle CLB, comme dans les recherches anglophones).
"""

TXT = {
    "en": dict(once="once", times="up to {n} times",
               listen="🎧 Listen {mot}</strong>, as on exam day — without reading the transcript.",
               nofmt="Your browser can’t play this audio format. An excerpt of the transcript is available just below.",
               rule1="In the TCF, the TEF and their IRN versions, the recording is played <strong>only once</strong> "
                     "and you get <strong>no transcript</strong>.",
               rule2="In the DELF B2, the first two exercises are played <strong>twice</strong> — but never with a transcript.",
               show_tr="Show an excerpt of the transcript — open it only after listening",
               warn="⚠️ <strong>This is a listening exercise.</strong> {regle} Reading the text before listening turns it "
                    "into a reading exercise and completely skews the measure of your level.",
               exo="Exercise {n} — level {niveau}", question="Question:", show_ans="Show the answer and the explanation",
               answer="Answer: {bonne}", expects="What the examiner expects"),
    "es": dict(once="una sola vez", times="como máximo {n} veces",
               listen="🎧 Escucha {mot}</strong>, como el día del examen, sin leer la transcripción.",
               nofmt="Tu navegador no reproduce este formato de audio. Hay un extracto de la transcripción justo debajo.",
               rule1="En el TCF, el TEF y sus versiones IRN, la grabación se emite <strong>una sola vez</strong> "
                     "y no tienes <strong>ninguna transcripción</strong>.",
               rule2="En el DELF B2, los dos primeros ejercicios se emiten <strong>dos veces</strong>, pero nunca con transcripción.",
               show_tr="Mostrar un extracto de la transcripción (ábrelo solo después de escuchar)",
               warn="⚠️ <strong>Es un ejercicio de comprensión oral.</strong> {regle} Leer el texto antes de escuchar lo "
                    "convierte en un ejercicio de comprensión escrita y falsea por completo la medida de tu nivel.",
               exo="Ejercicio {n} — nivel {niveau}", question="Pregunta:", show_ans="Ver la respuesta y la explicación",
               answer="Respuesta: {bonne}", expects="Lo que espera el corrector"),
}


def exo(lang, n, niveau, source_label, source, question, options, bonne, expl, audio=None, duree=None, ecoutes=1):
    """Un exercice : énoncé, question et options en français (l'examen), le reste dans la langue de la page."""
    t = TXT[lang]
    opts = "\n".join(f"<li>{o}</li>" for o in options)
    if audio:
        mot = t["once"] if ecoutes == 1 else t["times"].format(n=ecoutes)
        enonce = f"""<p class="listen"><strong>{t['listen'].format(mot=mot)}</p>
<audio controls preload="none" src="/audio/{audio}">{t['nofmt']}</audio>
<p class="listen">{source_label} · {duree}</p>"""
        regle = t["rule1"] if ecoutes == 1 else t["rule2"]
        transcription = f"""
<details><summary>{t['show_tr']}</summary>
<p class="warn">{t['warn'].format(regle=regle)}</p>
<p lang="fr">{source}</p></details>"""
    else:
        enonce = f"<p><em>{source_label}</em></p>\n<p lang=\"fr\">{source}</p>"
        transcription = ""
    return f"""
<div class="note">
<p><strong>{t['exo'].format(n=n, niveau=niveau)}</strong></p>
{enonce}
<p><strong>{t['question']}</strong> <span lang="fr">{question}</span></p>
<ol type="A" lang="fr">
{opts}
</ol>
</div>
<div class="faq">{transcription}
<details><summary>{t['show_ans']}</summary>
<p><strong>{t['answer'].format(bonne=bonne)}</strong> — {expl}</p></details></div>
"""


def sujet(lang, titre, meta, consigne, conseil):
    """Un sujet d'expression : la consigne reste en français, le conseil est traduit."""
    return f"""
<div class="note">
<p><strong>{titre}</strong> — <em>{meta}</em></p>
<p lang="fr">{consigne}</p>
</div>
<div class="faq"><details><summary>{TXT[lang]['expects']}</summary>
<p>{conseil}</p></details></div>
"""


CALC_EN = """<div class="calc" id="calculator">
<h2 id="calculator-title">Calculator: your TCF Canada scores in CLB</h2>
<p>Enter your four scores — or the ones you are aiming for: the CLB level for each skill appears, based on the IRCC
table reproduced below, with the matching CEFR level.</p>
<form class="calc-form" onsubmit="return false" aria-describedby="calc-note">
<label><b>Listening <span>/699</span></b><input type="number" min="0" max="699" step="1" inputmode="numeric" data-skill="co" placeholder="e.g. 458"></label>
<label><b>Reading <span>/699</span></b><input type="number" min="0" max="699" step="1" inputmode="numeric" data-skill="ce" placeholder="e.g. 453"></label>
<label><b>Speaking <span>/20</span></b><input type="number" min="0" max="20" step="1" inputmode="numeric" data-skill="eo" placeholder="e.g. 10"></label>
<label><b>Writing <span>/20</span></b><input type="number" min="0" max="20" step="1" inputmode="numeric" data-skill="ee" placeholder="e.g. 10"></label>
</form>
<div class="calc-out" aria-live="polite">
<table>
<thead><tr><th>Skill</th><th>Score</th><th>CEFR</th><th>CLB</th></tr></thead>
<tbody>
<tr><td>Listening</td><td data-out="co-note">—</td><td data-out="co-cecrl">—</td><td data-out="co-nclc">—</td></tr>
<tr><td>Reading</td><td data-out="ce-note">—</td><td data-out="ce-cecrl">—</td><td data-out="ce-nclc">—</td></tr>
<tr><td>Speaking</td><td data-out="eo-note">—</td><td data-out="eo-cecrl">—</td><td data-out="eo-nclc">—</td></tr>
<tr><td>Writing</td><td data-out="ee-note">—</td><td data-out="ee-cecrl">—</td><td data-out="ee-nclc">—</td></tr>
</tbody>
</table>
<p class="calc-verdict" data-out="verdict">Your profile will appear here: the lowest CLB of the four skills, the one IRCC uses.</p>
</div>
<p class="calc-note" id="calc-note"><small>The calculator reproduces the thresholds of the IRCC equivalency tables (below) and
the TCF’s CEFR bands. It replaces neither your results certificate nor IRCC’s own tool; if they differ, the official
table is the reference. No data is sent anywhere: everything is calculated in your browser.</small></p>
</div>
<script>
(function(){
  var T = {
    co: [[549,"10+"],[523,"9"],[503,"8"],[458,"7"],[398,"6"],[369,"5"],[331,"4"]],
    ce: [[549,"10+"],[524,"9"],[499,"8"],[453,"7"],[406,"6"],[375,"5"],[342,"4"]],
    eo: [[16,"10+"],[14,"9"],[12,"8"],[10,"7"],[7,"6"],[6,"5"],[4,"4"]],
    ee: [[16,"10+"],[14,"9"],[12,"8"],[10,"7"],[7,"6"],[6,"5"],[4,"4"]]
  };
  var C699 = [[600,"C2"],[500,"C1"],[400,"B2"],[300,"B1"],[200,"A2"],[100,"A1"]];
  var C20 = [[18,"C2"],[14,"C1"],[10,"B2"],[6,"B1"],[2,"A2"],[1,"A1"]];
  function level(tab, v, low){ for (var i=0;i<tab.length;i++){ if (v>=tab[i][0]) return tab[i][1]; } return low; }
  function clbNum(s){ return s==="10+" ? 10 : (s==="< 4" ? 3 : parseInt(s,10)); }
  var box = document.getElementById("calculator");
  var inputs = box.querySelectorAll("input[data-skill]");
  function out(k, v){ box.querySelector('[data-out="'+k+'"]').textContent = v; }
  function update(){
    var mins = [], filled = 0;
    inputs.forEach(function(inp){
      var k = inp.getAttribute("data-skill"), max = parseInt(inp.max,10);
      var v = inp.value === "" ? NaN : Number(inp.value);
      if (isNaN(v) || v < 0 || v > max) { out(k+"-note","—"); out(k+"-cecrl","—"); out(k+"-nclc","—"); return; }
      filled++;
      var cefr = max===699 ? level(C699, v, "below A1") : level(C20, v, "below A1");
      var n = level(T[k], v, "< 4");
      out(k+"-note", String(v)); out(k+"-cecrl", cefr); out(k+"-nclc", n === "< 4" ? "below 4" : "CLB " + n);
      mins.push(clbNum(n));
    });
    var vd = box.querySelector('[data-out="verdict"]');
    if (filled < 4) { vd.textContent = filled ? "Fill in all four scores to see your profile." : "Your profile will appear here: the lowest CLB of the four skills, the one IRCC uses."; return; }
    var m = Math.min.apply(null, mins);
    var txt = m <= 3 ? "At least one skill is below CLB 4: IRCC gives no level for that skill."
            : "Your profile: CLB " + (m>=10 ? "10+" : m) + " — the lowest CLB of the four skills, the one IRCC uses. ";
    if (m >= 7) txt += "You reach CLB 7 in all four skills, the reference threshold of the Federal Skilled Worker Program.";
    else if (m >= 4) txt += "CLB 7 in all four skills — the reference threshold of the Federal Skilled Worker Program — is not reached: the table below shows the missing score, skill by skill.";
    vd.textContent = txt;
  }
  inputs.forEach(function(inp){ inp.addEventListener("input", update); });
})();
</script>
"""


APP = "https://apps.apple.com/app/id6790412304"
CTA_INLINE = {
    "en": ("Practise in real exam conditions", "Mock exams in the official format and AI feedback on writing and speaking, "
           "in the TCF DELF TEF app — no account needed.", "Download"),
    "es": ("Entrena en condiciones reales", "Simulacros en el formato oficial y corrección con IA de la expresión escrita "
           "y oral, en la app TCF DELF TEF, sin crear cuenta.", "Descargar"),
}


def cta_inline(lang, variant=""):
    """La carte « Entraînez-vous » des articles français (README : avant le 3e h2), dans la langue de la page."""
    b, span, btn = CTA_INLINE[lang]
    if variant == "en-US":
        b = b.replace("Practise", "Practice")
    return (f'<aside class="cta-inline"><img src="/img/favicon-192.png" alt="" width="44" height="44" loading="lazy">'
            f'<div><b>{b}</b><span>{span}</span></div><a class="btn" href="{APP}">{btn}</a></aside>\n')
