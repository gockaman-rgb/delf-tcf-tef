# -*- coding: utf-8 -*-
"""Calculateur TCF Canada → NCLC, inséré en tête de /tcf-canada/score-nclc/ (exam_hubs.py, clé extra_top).

Seuils : tableaux d'équivalence IRCC tels que la page les reproduit (croisés le 27 juillet 2026) ;
niveaux CECRL : bandes officielles du TCF. Aucun autre seuil n'est affirmé ici.
"""

CALC = """<div class="calc" id="calculateur">
<h2 id="calculateur-titre">Calculateur : vos scores TCF Canada en NCLC</h2>
<p>Entrez vos quatre notes — ou celles que vous visez — : le niveau NCLC de chaque compétence s'affiche
d'après la table d'IRCC reproduite plus bas, avec le niveau CECRL correspondant.</p>
<form class="calc-form" onsubmit="return false" aria-describedby="calc-note">
<label><b>Compréhension orale <span>/699</span></b><input type="number" min="0" max="699" step="1" inputmode="numeric" data-skill="co" placeholder="ex. 458"></label>
<label><b>Compréhension écrite <span>/699</span></b><input type="number" min="0" max="699" step="1" inputmode="numeric" data-skill="ce" placeholder="ex. 453"></label>
<label><b>Expression orale <span>/20</span></b><input type="number" min="0" max="20" step="1" inputmode="numeric" data-skill="eo" placeholder="ex. 10"></label>
<label><b>Expression écrite <span>/20</span></b><input type="number" min="0" max="20" step="1" inputmode="numeric" data-skill="ee" placeholder="ex. 10"></label>
</form>
<div class="calc-out" aria-live="polite">
<table>
<thead><tr><th>Compétence</th><th>Note</th><th>CECRL</th><th>NCLC</th></tr></thead>
<tbody>
<tr><td>Compréhension orale</td><td data-out="co-note">—</td><td data-out="co-cecrl">—</td><td data-out="co-nclc">—</td></tr>
<tr><td>Compréhension écrite</td><td data-out="ce-note">—</td><td data-out="ce-cecrl">—</td><td data-out="ce-nclc">—</td></tr>
<tr><td>Expression orale</td><td data-out="eo-note">—</td><td data-out="eo-cecrl">—</td><td data-out="eo-nclc">—</td></tr>
<tr><td>Expression écrite</td><td data-out="ee-note">—</td><td data-out="ee-cecrl">—</td><td data-out="ee-nclc">—</td></tr>
</tbody>
</table>
<p class="calc-verdict" data-out="verdict">Votre profil s'affichera ici : le NCLC le plus bas des quatre compétences, celui qu'IRCC retient.</p>
</div>
<p class="calc-note" id="calc-note"><small>Le calcul reproduit les bornes des tableaux d'équivalence IRCC (ci-dessous) et
les bandes CECRL du TCF. Il ne remplace ni votre attestation ni l'outil d'IRCC ; en cas d'écart, la
table officielle fait foi. Aucune donnée n'est envoyée : tout se calcule dans votre navigateur.</small></p>
</div>
<script>
(function(){
  var T = {
    co: [[549,"10 et +"],[523,"9"],[503,"8"],[458,"7"],[398,"6"],[369,"5"],[331,"4"]],
    ce: [[549,"10 et +"],[524,"9"],[499,"8"],[453,"7"],[406,"6"],[375,"5"],[342,"4"]],
    eo: [[16,"10 et +"],[14,"9"],[12,"8"],[10,"7"],[7,"6"],[6,"5"],[4,"4"]],
    ee: [[16,"10 et +"],[14,"9"],[12,"8"],[10,"7"],[7,"6"],[6,"5"],[4,"4"]]
  };
  var C699 = [[600,"C2"],[500,"C1"],[400,"B2"],[300,"B1"],[200,"A2"],[100,"A1"]];
  var C20 = [[18,"C2"],[14,"C1"],[10,"B2"],[6,"B1"],[2,"A2"],[1,"A1"]];
  function level(tab, v, low){ for (var i=0;i<tab.length;i++){ if (v>=tab[i][0]) return tab[i][1]; } return low; }
  function nclcNum(s){ return s==="10 et +" ? 10 : (s==="< 4" ? 3 : parseInt(s,10)); }
  var box = document.getElementById("calculateur");
  var inputs = box.querySelectorAll("input[data-skill]");
  function out(k, v){ box.querySelector('[data-out="'+k+'"]').textContent = v; }
  function update(){
    var mins = [], filled = 0;
    inputs.forEach(function(inp){
      var k = inp.getAttribute("data-skill"), max = parseInt(inp.max,10);
      var v = inp.value === "" ? NaN : Number(inp.value);
      if (isNaN(v) || v < 0 || v > max) { out(k+"-note","—"); out(k+"-cecrl","—"); out(k+"-nclc","—"); return; }
      filled++;
      var cecrl = max===699 ? level(C699, v, "A1 non atteint") : level(C20, v, "A1 non atteint");
      var n = level(T[k], v, "< 4");
      out(k+"-note", String(v)); out(k+"-cecrl", cecrl); out(k+"-nclc", n === "< 4" ? "inférieur à 4" : "NCLC " + n);
      mins.push(nclcNum(n));
    });
    var vd = box.querySelector('[data-out="verdict"]');
    if (filled < 4) { vd.textContent = filled ? "Complétez les quatre notes pour voir votre profil." : "Votre profil s'affichera ici : le NCLC le plus bas des quatre compétences, celui qu'IRCC retient."; return; }
    var m = Math.min.apply(null, mins);
    var txt = m <= 3 ? "Au moins une compétence est sous le NCLC 4 : IRCC ne retient aucun niveau pour cette compétence."
            : "Votre profil : NCLC " + (m>=10 ? "10 et +" : m) + " — le NCLC le plus bas des quatre compétences, celui qu'IRCC retient. ";
    if (m >= 7) txt += "Vous atteignez le NCLC 7 dans les quatre épreuves, le seuil de référence du Programme des travailleurs qualifiés fédéraux.";
    else if (m >= 4) txt += "Le NCLC 7 dans les quatre épreuves — seuil de référence du Programme des travailleurs qualifiés fédéraux — n'est pas atteint : la table ci-dessous donne le score manquant, compétence par compétence.";
    vd.textContent = txt;
  }
  inputs.forEach(function(inp){ inp.addEventListener("input", update); });
})();
</script>
"""

CSS = """
/* Calculateur NCLC (2026-09-19) */
.calc { border: 1px solid var(--line); border-radius: 14px; padding: 18px 20px 6px; margin: 1.6em 0 2em; background: var(--bg2); }
.calc h2 { margin-top: 0; }
.calc-form { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px 18px; margin: 14px 0 18px; }
.calc-form label { display: flex; flex-direction: column; gap: 6px; font-size: .9em; font-weight: 600; }
.calc-form label b { font-weight: 600; }
.calc-form label span { font-weight: 400; color: var(--muted); font-size: .9em; }
.calc-form input { font: inherit; font-size: 1.05em; padding: 9px 12px; border: 1px solid var(--line); border-radius: 10px; background: var(--bg); color: var(--text); width: 100%; box-sizing: border-box; }
.calc-form input:focus { outline: 2px solid var(--accent); outline-offset: 1px; }
.calc-out table { margin: 0; }
.calc-out td[data-out$="-nclc"] { font-weight: 700; color: var(--accent); }
.calc-verdict { font-weight: 600; margin: 14px 0 6px; }
.calc-note { color: var(--muted); margin: 8px 0 12px; }
@media (max-width: 560px) { .calc-form { grid-template-columns: 1fr; } }
"""
