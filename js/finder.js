/* Chercheur de centres — delf-tcf-tef.fr (26/10/2026). Aucune requête tierce : index des villes de centres
   (/data/finder/index.json), fiches par pays (/data/finder/c/), gazetier GeoNames découpé (/data/geo/), chargés à la
   demande. La position reste dans le navigateur. Test : ?lat=45.76&lon=4.84 simule « autour de moi ».
   norm() = make_gazetteer.norm, caractère pour caractère. */
(function () {
  'use strict';
  var root = document.getElementById('finder');
  if (!root || !window.fetch || !''.normalize) return;

  var T = {
    fr: { hint: 'Tapez une ville ou touchez « Autour de moi ».', ph: 'Ville, pays ou centre', go: 'Chercher', near: 'Autour de moi', all: 'Tous', loading: 'Chargement de la liste…',
      locating: 'Recherche de votre position…', denied: 'Position refusée : tapez plutôt une ville.',
      unavail: 'Position indisponible : tapez plutôt une ville.', timeout: 'Position trop lente : réessayez ou tapez une ville.',
      none: 'Aucun lieu trouvé pour « %s » : vérifiez l’orthographe.',
      nearest: 'Centres les plus proches : %s', far: '%s : aucun centre à moins de 300 km. Les plus proches :',
      inCountry: 'Centres du pays : %s', noCountry: '%s : aucun centre %e dans notre liste pour l’instant.',
      fei: 'Liste officielle de FEI', more: 'Afficher plus de centres',
      dir: 'Itinéraire', so: 'sessions sur ordinateur', guide: 'Notre guide : %e %p', you: 'votre position', country: 'pays',
      centres: function (n) { return n + (n > 1 ? ' centres' : ' centre'); }, found: function (n) { return n + ' résultat' + (n > 1 ? 's' : ''); },
      ex: { tcf: 'TCF', delf: 'DELF-DALF', civique: 'Examen civique', tef: 'TEF' }, inl: { en: ' (en anglais)', es: ' (en espagnol)', ar: ' (en arabe)', fr: '' },
      at: function (p, scope) { return scope === 'c' ? 'à ' + p : '— ' + p; }, error: 'La liste n’a pas pu être chargée. Rechargez la page.',
      tefS: 'Sessions TEF publiées sur la carte de la CCI le %d : %l', tefN: 'Centre TEF (réseau CCI) : demandez-lui ses prochaines sessions.',
      tefC: 'Contact (CCI)', cci: 'Carte officielle des centres TEF (CCI)' },
    en: { hint: 'Type a city or tap “Near me”.', ph: 'City, country or centre', go: 'Search', near: 'Near me', all: 'All', loading: 'Loading the list…',
      locating: 'Finding your position…', denied: 'Location permission denied: type a city instead.',
      unavail: 'Your position is unavailable: type a city instead.', timeout: 'Location timed out: try again or type a city.',
      none: 'No place found for “%s”: check the spelling.',
      nearest: 'Test centres nearest to %s', far: 'No test centre within 300 km of %s. The nearest:',
      inCountry: 'Test centres in %s', noCountry: 'No %e test centre in %s in our list yet.',
      fei: 'FEI’s official list', more: 'Show more centres',
      dir: 'Directions', so: 'computer-based sessions', guide: 'Our guide: %e %p', you: 'your position', country: 'country',
      centres: function (n) { return n + (n > 1 ? ' centres' : ' centre'); }, found: function (n) { return n + ' result' + (n > 1 ? 's' : ''); },
      ex: { tcf: 'TCF', delf: 'DELF-DALF', civique: 'Civics test (France)', tef: 'TEF' }, inl: { fr: ' (in French)', es: ' (in Spanish)', ar: ' (in Arabic)', en: '' },
      at: function (p) { return 'in ' + p; }, error: 'The list could not be loaded. Reload the page.',
      tefS: 'TEF sessions published on the CCI map on %d: %l', tefN: 'TEF centre (CCI network): ask it for its next sessions.',
      tefC: 'Contact page (CCI)', cci: 'Official map of TEF centres (CCI)' },
    es: { hint: 'Escribe una ciudad o toca «Cerca de mí».', ph: 'Ciudad, país o centro', go: 'Buscar', near: 'Cerca de mí', all: 'Todos', loading: 'Cargando la lista…',
      locating: 'Buscando tu ubicación…', denied: 'Ubicación denegada: escribe una ciudad.',
      unavail: 'Ubicación no disponible: escribe una ciudad.', timeout: 'La ubicación tardó demasiado: reintenta o escribe una ciudad.',
      none: 'Ningún lugar para «%s»: revisa la ortografía.',
      nearest: 'Los centros más cercanos a %s', far: 'Ningún centro a menos de 300 km de %s. Los más cercanos:',
      inCountry: 'Los centros en %s', noCountry: 'Todavía no hay ningún centro %e en %s en nuestra lista.',
      fei: 'Lista oficial de FEI', more: 'Mostrar más centros',
      dir: 'Cómo llegar', so: 'sesiones en computadora', guide: 'Nuestra guía: %e %p', you: 'tu ubicación', country: 'país',
      centres: function (n) { return n + (n > 1 ? ' centros' : ' centro'); }, found: function (n) { return n + ' resultado' + (n > 1 ? 's' : ''); },
      ex: { tcf: 'TCF', delf: 'DELF-DALF', civique: 'Examen cívico (Francia)', tef: 'TEF' }, inl: { fr: ' (en francés)', en: ' (en inglés)', ar: ' (en árabe)', es: '' },
      at: function (p) { return 'en ' + p; }, error: 'No se pudo cargar la lista. Vuelve a cargar la página.',
      tefS: 'Sesiones TEF publicadas en el mapa de la CCI el %d: %l', tefN: 'Centro TEF (red CCI): pregúntale por sus próximas sesiones.',
      tefC: 'Contacto (CCI)', cci: 'Mapa oficial de centros TEF (CCI)' },
    ar: { hint: 'اكتب اسم مدينة أو اضغط «بالقرب مني».', ph: 'مدينة أو بلد أو مركز', go: 'ابحث', near: 'بالقرب مني', all: 'الكل', loading: 'جارٍ تحميل القائمة…',
      locating: 'جارٍ تحديد موقعك…', denied: 'رُفض الوصول إلى الموقع: اكتب اسم مدينة بدلًا من ذلك.',
      unavail: 'موقعك غير متاح: اكتب اسم مدينة بدلًا من ذلك.', timeout: 'تأخّر تحديد الموقع: أعد المحاولة أو اكتب اسم مدينة.',
      none: 'لم نجد مكانًا باسم «%s»: تحقّق من الكتابة.',
      nearest: 'أقرب مراكز الامتحان إلى %s', far: 'لا يوجد مركز على بُعد أقل من 300 كم من %s. الأقرب:',
      inCountry: 'مراكز الامتحان في %s', noCountry: 'لا يوجد في قائمتنا حتى الآن مركز %e في %s.',
      fei: 'القائمة الرسمية لدى FEI', more: 'اعرض مزيدًا من المراكز',
      dir: 'الاتجاهات', so: 'جلسات على الحاسوب', guide: 'دليلنا: %e %p', you: 'موقعك', country: 'بلد',
      centres: function (n) { return n === 1 ? 'مركز واحد' : n === 2 ? 'مركزان' : n + (n <= 10 ? ' مراكز' : ' مركزًا'); },
      found: function (n) { return 'النتائج: ' + n; },
      ex: { tcf: 'TCF', delf: 'DELF-DALF', civique: 'الامتحان المدني (فرنسا)', tef: 'TEF' }, inl: { fr: ' (بالفرنسية)', en: ' (بالإنجليزية)', es: ' (بالإسبانية)', ar: '' },
      at: function (p) { return 'في ' + p; }, error: 'تعذّر تحميل القائمة. أعد تحميل الصفحة.',
      tefS: 'جلسات TEF المنشورة على خريطة CCI في %d: %l', tefN: 'مركز TEF (شبكة CCI): اسأله عن جلساته القادمة.',
      tefC: 'صفحة الاتصال (CCI)', cci: 'الخريطة الرسمية لمراكز TEF (CCI)' }
  };
  var LANG = (document.documentElement.lang || 'fr').slice(0, 2);
  if (!T[LANG]) LANG = 'fr';
  var S = T[LANG], LI = { fr: 0, en: 1, es: 2, ar: 3 }[LANG], RTL = LANG === 'ar', COMMA = RTL ? '، ' : ', ';
  var EXAMS = ['tcf', 'delf', 'civique', 'tef'];
  var V = root.getAttribute('data-v') || '';
  var FEI = 'https://www.france-education-international.fr/centres-d-examen/liste', CCI = 'https://francais.cci-paris-idf.fr/candidat';

  var MARK, NONW;
  try { MARK = new RegExp('\\p{M}', 'gu'); NONW = new RegExp('[^\\p{L}\\p{N}]+', 'gu'); } catch (e) { return; }   // très vieux navigateur : la liste statique suffit
  var FOLD = { 'ø': 'o', 'đ': 'd', 'ł': 'l', 'æ': 'ae', 'œ': 'oe', 'ı': 'i', 'ß': 'ss', 'ð': 'd', 'þ': 'th', 'ħ': 'h', 'ŀ': 'l',
    'ŧ': 't', 'ĸ': 'k', 'ŋ': 'n', 'ٱ': 'ا', 'ة': 'ه', 'ى': 'ي', 'ی': 'ي', 'ک': 'ك', 'ـ': '' };
  for (var d = 0; d < 10; d++) { FOLD[String.fromCharCode(0x660 + d)] = '' + d; FOLD[String.fromCharCode(0x6f0 + d)] = '' + d; }
  function norm(s) {
    s = String(s || '').normalize('NFKD').replace(MARK, '').normalize('NFC').toLowerCase();
    var o = '';
    for (var i = 0; i < s.length; i++) { var c = s[i]; o += FOLD.hasOwnProperty(c) ? FOLD[c] : c; }
    o = o.replace(/['’ʼ`´ʻ‘]/g, '').replace(NONW, ' ').replace(/_/g, ' ').trim();
    var t = o.split(/\s+/);
    for (var j = 0; j < t.length - 1; j++) { if (t[j] === 'st') t[j] = 'saint'; else if (t[j] === 'ste') t[j] = 'sainte'; }
    return t.join(' ');
  }
  function dl(a, b, k) {          // Damerau-Levenshtein, abandon au-delà de k
    var la = a.length, lb = b.length;
    if (Math.abs(la - lb) > k) return k + 1;
    var p2 = null, p = [], i, j;
    for (j = 0; j <= lb; j++) p.push(j);
    for (i = 1; i <= la; i++) {
      var c = [i], best = i;
      for (j = 1; j <= lb; j++) {
        var v = Math.min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
        if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) v = Math.min(v, p2[j - 2] + 1);
        c.push(v); if (v < best) best = v;
      }
      if (best > k) return k + 1;
      p2 = p; p = c;
    }
    return p[lb];
  }
  var WORDS = /\b(tcf|tef|delf|dalf|irn|exams?|examen|examens|tests?|centres?|centers?|centros?|near|me|nearest|cerca|mi|autour|moi|pres|chez|proche|de|du|d|of|the|in|en|a|booking|book)\b/g;
  function tol(n) { return n < 4 ? 0 : n < 8 ? 1 : 2; }
  // 0 exact · 1 début du nom · 2 début d'un mot · 3 faute de frappe
  function tier(q, n) {
    if (n === q) return 0;
    if (n.lastIndexOf(q, 0) === 0) return 1;
    if (q.length >= 3 && n.indexOf(' ' + q) >= 0) return 2;
    var k = tol(q.length);
    if (k && (dl(q, n, k) <= k || (q.length >= 5 && n.length > q.length && dl(q, n.slice(0, q.length), k) <= k))) return 3;
    return -1;
  }

  var IX = null, IXp = null, KEYS = {}, NAMES = null, SHARDS = {}, COUNTRY = {};
  function get(u) { return fetch(u + (V ? '?v=' + V : '')).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }); }
  function index() {
    if (!IXp) {
      IXp = get('/data/finder/index.json').then(function (ix) {
        ix.rows = ix.r.map(function (r, i) {
          var n = r[0].split('|'), shown = [n[0], n[1] || n[0], n[2] || n[0], n[3] || n[1] || n[0]];
          var cnt = String(r[4]).split(',').map(Number);   // total, puis tcf, delf, civique, tef
          return { i: i, names: shown, lat: r[1], lon: r[2], cc: r[3], cnt: cnt, pop: r[5] || 0, q: r[6] || '',
            keys: shown.map(norm).filter(function (x, j, a) { return x && a.indexOf(x) === j; }) };
        });
        ix.ckeys = {};
        Object.keys(ix.C).forEach(function (cc) { ix.ckeys[cc] = ix.C[cc].map(norm); });
        ix.k.forEach(function (f) { f[1].split('|').forEach(function (k) { KEYS[k] = f[0]; }); });
        if (ix.x.indexOf('tef') < 0) { var t = root.querySelector('input[value="tef"]'); if (t) t.parentNode.hidden = true; }
        IX = ix;
        return ix;
      });
      IXp.catch(function () { status(S.error); IXp = null; });
    }
    return IXp;
  }
  function shardKey(q) {          // plus longue clé qui commence la requête
    for (var l = Math.min(q.length, 8); l >= 2; l--) if (KEYS.hasOwnProperty(q.slice(0, l))) return q.slice(0, l);
    return null;
  }
  function variants(q) {          // faute dans les premières lettres : morceaux voisins
    var v = [], n = Math.min(q.length - 1, 4);
    for (var i = 0; i < n; i++) {
      v.push(q.slice(0, i) + q[i] + q.slice(i), q.slice(0, i) + q.slice(i + 1), q.slice(0, i) + q[i + 1] + q[i] + q.slice(i + 2));
    }
    return v;
  }
  function shard(k) {
    if (!k) return Promise.resolve([]);
    var f = KEYS[k];
    if (!SHARDS[f]) SHARDS[f] = get('/data/geo/' + f + '.json').catch(function () { return {}; });
    return SHARDS[f].then(function (o) { return o[k] || []; });
  }
  function names() {
    if (!NAMES) NAMES = Promise.all([get('/data/finder/names.json'), index()]).then(function (a) {
      return a[0].map(function (x) { var n = norm(x[0]); return [x[2] || x[0], n, x[1], n + ' ' + a[1].rows[x[1]].keys[0]]; });   // + ville
    }).catch(function () { return []; });
    return NAMES;
  }
  function country(cc) {
    if (!COUNTRY[cc]) COUNTRY[cc] = get('/data/finder/c/' + cc + '.json').catch(function () { return { c: [], L: [] }; });
    return COUNTRY[cc];
  }
  function cname(cc) { var c = IX.C[cc]; return c ? c[LI] : cc; }
  function rowName(r) { return r.names[LI] + (r.q ? ' (' + (r.q[0] === '@' ? cname(r.q.slice(1)) : r.q) + ')' : ''); }

  function suggest(raw) {
    var q = norm(raw);
    if (!q) return Promise.resolve([]);
    return index().then(function (ix) {
      var out = [], k = q.length >= 2 ? shardKey(q) : null;
      Object.keys(ix.ckeys).forEach(function (cc) {
        var best = -1;
        ix.ckeys[cc].forEach(function (n) { var t = tier(q, n); if (t >= 0 && (best < 0 || t < best)) best = t; });
        if (best >= 0) out.push({ type: 'country', t: best, cc: cc, label: cname(cc), w: 1e7, n: ix.rows.filter(function (r) { return r.cc === cc; }).reduce(function (s, r) { return s + total(r); }, 0) });
      });
      ix.rows.forEach(function (r) {
        var best = -1;
        r.keys.forEach(function (n) { var t = tier(q, n); if (t >= 0 && (best < 0 || t < best)) best = t; });
        if (best >= 0) out.push({ type: 'city', t: best, row: r, label: rowName(r), sub: cname(r.cc), w: 2 * (r.pop + 1), n: total(r) });
      });
      var jobs = [shard(k), q.length >= 3 ? names() : null];
      return Promise.all(jobs).then(function (res) {
        places(res[0], q, out);
        (res[1] || []).forEach(function (c) {
          var t = tier(q, c[1]), t2 = tier(q, c[3].replace(/ (de|d|du|of) /g, ' '));
          if (t < 0 || t === 3 || (t2 >= 0 && t2 < t)) t = t2;
          if (t < 0 || t === 3 || out.some(function (o) { return o.type === 'centre' && o.name === c[0] && o.row === ix.rows[c[2]]; })) return;
          var r = ix.rows[c[2]];
          out.push({ type: 'centre', t: t + 0.5, row: r, label: c[0], sub: rowName(r) + COMMA + cname(r.cc), w: 0, name: c[0] });
        });
        if (out.length || q.length < 4) return out;
        var alt = variants(q).map(shardKey).filter(function (x, i, a) { return x && x !== k && a.indexOf(x) === i; }).slice(0, 4);
        return Promise.all(alt.map(shard)).then(function (more) { more.forEach(function (rows) { places(rows, q, out); }); return out; });
      }).then(function (out) {
        var RANK = { city: 0, country: 1, place: 2, centre: 3 };
        out.sort(function (a, b) { return a.t - b.t || RANK[a.type] - RANK[b.type] || b.w - a.w; });
        return out.slice(0, 8);
      });
    });
  }
  function places(rows, q, out) {
    (rows || []).forEach(function (g) {
      var ns = g[0].split('|'), best = -1, hit = '';
      ns.forEach(function (n) { var t = tier(q, norm(n)); if (t >= 0 && (best < 0 || t < best)) { best = t; hit = n; } });
      if (best < 0) return;
      var dd = g[5] ? String(g[5]).split('|') : [], name = dd[LI] || (LI === 3 && dd[1]) || ns[0];
      if (out.some(function (o) { return (o.type === 'city' && o.row.lat !== null && Math.abs(o.row.lat - g[1]) < 0.06 && Math.abs(o.row.lon - g[2]) < 0.08)
        || (o.type === 'place' && o.lat === g[1] && o.lon === g[2]); })) return;
      // trouvé par un autre nom (« Brüx » pour Most) : après les villes de centres
      out.push({ type: 'place', t: best + (norm(hit) !== norm(name) ? 1.5 : 0), lat: g[1], lon: g[2], cc: g[3], label: name + (g[6] ? ' (' + g[6] + ')' : ''),
        alias: norm(hit) !== norm(name) ? hit : '', sub: cname(g[3]), w: g[4] || 0 });
    });
  }
  function total(r) { var x = exam(); return r.cnt[x === 'all' ? 0 : EXAMS.indexOf(x) + 1] || 0; }

  var form = root.querySelector('form'), input = root.querySelector('#finder-q'), list = root.querySelector('#finder-list');
  var nearBtn = root.querySelector('#finder-near'), stat = root.querySelector('#finder-status'), out = root.querySelector('#finder-results');
  var opts = [], active = -1, timer = 0, seq = 0, current = null, limit = 10;
  function exam() { var c = root.querySelector('input[name="exam"]:checked'); return c ? c.value : 'all'; }
  function status(t) { stat.textContent = t || ''; }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function iso(text, ltr) { var b = el('bdi', null, text); if (ltr) b.dir = 'ltr'; return b; }
  function line(box, node) { var p = el('p', 'contact'), b = iso(null, true); b.appendChild(node); p.appendChild(b); box.appendChild(p); }
  function moreBtn(fn) { var m = el('button', 'btn ghost finder-more', S.more); m.type = 'button'; m.addEventListener('click', fn); out.appendChild(m); }
  function fill(tpl, map) {   // « %s » → nœud isolé (bdi)
    var f = document.createDocumentFragment(), parts = tpl.split(/(%[a-z])/);
    parts.forEach(function (p) { if (map.hasOwnProperty(p)) f.appendChild(typeof map[p] === 'string' ? iso(map[p]) : map[p]); else if (p) f.appendChild(document.createTextNode(p)); });
    return f;
  }
  function close() { list.hidden = true; list.textContent = ''; input.setAttribute('aria-expanded', 'false'); input.removeAttribute('aria-activedescendant'); active = -1; }
  function show(items) {
    opts = items; list.textContent = ''; active = -1;
    if (!items.length) return close();
    items.forEach(function (o, i) {
      var li = el('li', 'finder-opt'); li.id = 'finder-opt-' + i; li.setAttribute('role', 'option'); li.setAttribute('aria-selected', 'false');
      var b = el('span', 'finder-opt-main'); b.appendChild(iso(o.label));
      if (o.alias) { b.appendChild(document.createTextNode(' · ')); b.appendChild(iso(o.alias)); }
      li.appendChild(b);
      var meta = o.type === 'country' ? S.country + (o.n ? ' · ' + S.centres(o.n) : '') : (o.sub || '') + (o.type === 'city' && o.n ? ' · ' + S.centres(o.n) : '');
      li.appendChild(iso(meta)).className = 'finder-opt-sub';
      li.addEventListener('mousedown', function (e) { e.preventDefault(); pick(o); });
      list.appendChild(li);
    });
    list.hidden = false; input.setAttribute('aria-expanded', 'true');
  }
  function move(n) {
    if (list.hidden || !opts.length) return;
    active = (active + n + opts.length) % opts.length;
    [].forEach.call(list.children, function (li, i) { li.setAttribute('aria-selected', i === active ? 'true' : 'false'); });
    input.setAttribute('aria-activedescendant', 'finder-opt-' + active);
    list.children[active].scrollIntoView({ block: 'nearest' });
  }
  function pick(o) {
    close(); limit = 10;
    input.value = o.label;
    current = o; run();
    setURL(o.type === 'point' ? '' : o.label);
  }
  function submit() {
    var raw = input.value.trim();
    if (!raw) return;
    var my = ++seq;
    status(IX ? '' : S.loading);
    // « tcf montreal » : filtre TCF, lieu Montreal
    var q = norm(raw), ex = (q.match(/\b(tcf|delf|dalf|tef)\b/) || [])[1], rest = q.replace(WORDS, ' ').trim().replace(/\s+/g, ' '),
      bare = rest.replace(/\b(canada|quebec)\b/g, '').trim();
    suggest(raw).then(function (items) {
      return items.length || !rest || rest === q ? items : suggest(rest);
    }).then(function (items) {
      return items.length || !bare || bare === rest ? items : suggest(bare);
    }).then(function (items) {
      if (my !== seq) return;
      if (!items.length) { close(); out.textContent = ''; status(rest ? S.none.replace('%s', raw) : S.hint); return; }
      if (ex && rest !== q) { var r = root.querySelector('input[value="' + (ex === 'dalf' ? 'delf' : ex) + '"]'); if (r) r.checked = true; }
      pick(items[0]);
    });
  }
  function setURL(q) {
    try {
      var u = new URL(location.href); u.searchParams.delete('lat'); u.searchParams.delete('lon');
      if (q) u.searchParams.set('q', q); else u.searchParams.delete('q');
      if (exam() !== 'all') u.searchParams.set('exam', exam()); else u.searchParams.delete('exam');
      history.replaceState(null, '', u.pathname + u.search + u.hash);
    } catch (e) { /* vieux navigateurs */ }
  }

  function km(a, b, c, d) {
    var R = 6371, p = Math.PI / 180, x = Math.sin((c - a) * p / 2), y = Math.sin((d - b) * p / 2);
    return 2 * R * Math.asin(Math.sqrt(x * x + Math.cos(a * p) * Math.cos(c * p) * y * y));
  }
  var NF = (function () { try { return new Intl.NumberFormat(RTL ? 'ar-u-nu-latn' : LANG); } catch (e) { return { format: String }; } })();
  function day(iso) {
    try { return new Intl.DateTimeFormat(RTL ? 'ar-u-nu-latn' : LANG, { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' }).format(new Date(iso + 'T12:00:00Z')); }
    catch (e) { return iso; }
  }
  function dist(k) { return k < 1 ? '< 1 km' : NF.format(Math.round(k)) + ' km'; }
  function run() {
    var o = current;
    if (!o) return;
    var my = ++seq;
    index().then(function () {
      if (o.type === 'country') return byCountry(o.cc, my);
      var lat = o.row ? o.row.lat : o.lat, lon = o.row ? o.row.lon : o.lon;
      if (lat === null || lat === undefined) return byCountry(o.row.cc, my, o.row);
      return nearest(lat, lon, o.type === 'point' ? S.you : o.label, my, o.name);
    });
  }
  function nearest(lat, lon, label, my, first) {
    var x = exam(), rows = IX.rows.filter(function (r) { return r.lat !== null && total(r) > 0; });
    rows.forEach(function (r) { r.d = km(lat, lon, r.lat, r.lon); });
    rows.sort(function (a, b) { return a.d - b.d; });
    var far = !rows.length || rows[0].d > 300, want = far ? 5 : limit, take = [], n = 0;
    for (var i = 0; i < rows.length && n < want; i++) { take.push(rows[i]); n += total(rows[i]); }
    var ccs = take.map(function (r) { return r.cc; }).filter(function (c, i, a) { return a.indexOf(c) === i; });
    Promise.all(ccs.map(country)).then(function (files) {
      if (my !== seq) return;
      var cards = [];
      take.forEach(function (r) {
        var f = files[ccs.indexOf(r.cc)];
        f.c.forEach(function (c) { if (c.r === r.i && match(c, x)) cards.push({ c: c, r: r, f: f, d: r.d }); });
      });
      if (first) cards.sort(function (a, b) { return (b.c.n === first) - (a.c.n === first) || a.d - b.d; });
      cards = cards.slice(0, want);
      out.textContent = '';
      var h = el('h3', 'finder-h');
      h.appendChild(fill(far ? S.far : S.nearest, { '%s': label }));
      out.appendChild(h);
      if (!cards.length) { out.appendChild(el('p', null, S.none.replace('%s', label))); return status(''); }
      var ol = el('ol', 'finder-list-res');
      cards.forEach(function (k) { var li = el('li'); li.appendChild(card(k.c, k.r, k.f, k.d)); ol.appendChild(li); });
      out.appendChild(ol);
      if (!far && (n > want || take.length < rows.length)) moreBtn(function () { limit += 10; nearest(lat, lon, label, ++seq, first); });
      status(S.found(cards.length));
    });
  }
  function match(c, x) { return x === 'all' || c.x.split(',').indexOf(x) >= 0; }
  function byCountry(cc, my, onlyRow) {
    var x = exam(), rows = IX.rows.filter(function (r) { return r.cc === cc && (!onlyRow || r === onlyRow); });
    out.textContent = '';
    var h = el('h3', 'finder-h');
    h.appendChild(fill(S.inCountry, { '%s': cname(cc) }));
    out.appendChild(h);
    if (!rows.some(function (r) { return total(r) > 0; })) {
      var p = el('p');
      p.appendChild(fill(S.noCountry, { '%e': x === 'all' ? '' : S.ex[x], '%s': cname(cc) }));
      p.appendChild(document.createTextNode(' '));
      var a = el('a', null, x === 'tef' ? S.cci : S.fei);
      a.href = x === 'tef' ? CCI : IX.f[cc] ? FEI + '?pays=' + IX.f[cc] + '&type-centre=' + (x === 'delf' ? 'delf_dalf' : 'tcf') : FEI;
      a.rel = 'noopener'; p.appendChild(a); out.appendChild(p);
      return status('');
    }
    country(cc).then(function (f) {
      if (my !== seq) return;
      rows.sort(function (a, b) { return total(b) - total(a) || a.names[LI].localeCompare(b.names[LI]); });
      var n = 0, all = rows.reduce(function (s, r) { return s + total(r); }, 0);
      rows.forEach(function (r) {
        var cs = f.c.filter(function (c) { return c.r === r.i && match(c, x); });
        if (!cs.length || n >= limit * 6) return;    // 60 fiches, puis « plus »
        var h4 = el('h4', 'finder-city'); h4.appendChild(iso(rowName(r))); h4.appendChild(el('span', 'count', ' (' + cs.length + ')'));
        out.appendChild(h4);
        var ol = el('ol', 'finder-list-res');
        cs.forEach(function (c) { var li = el('li'); li.appendChild(card(c, r, f, null)); ol.appendChild(li); n++; });
        out.appendChild(ol);
      });
      if (n < all) moreBtn(function () { limit += 10; byCountry(cc, ++seq, onlyRow); });
      status(S.found(n));
    });
  }
  function card(c, r, f, d) {
    var box = el('div', 'card centre finder-card');
    var h = el('h5'); h.appendChild(iso(LANG === 'es' && c.ns || (LANG === 'en' || RTL) && c.ne || c.n)); box.appendChild(h);
    var where = el('p', 'finder-where'); where.appendChild(iso(rowName(r) + COMMA + cname(r.cc)));
    if (d !== null) { where.appendChild(document.createTextNode(' · ')); where.appendChild(iso(dist(d), true)).className = 'finder-dist'; }
    box.appendChild(where);
    if (c.a) { var a = el('p', 'addr'); a.appendChild(iso(c.a)); box.appendChild(a); }
    if (c.p) { var tel = Array.isArray(c.p), t = el(tel ? 'a' : 'span', null, tel ? c.p[1] : c.p); if (tel) t.href = 'tel:' + c.p[0]; line(box, t); }
    (c.e || []).forEach(function (m) { var a = el('a', null, m); a.href = 'mailto:' + m; line(box, a); });
    if (c.w) { var w = el('a', null, c.w.replace(/^https?:\/\/(www\.)?/, '').replace(/\/$/, '')); w.href = c.w; w.rel = 'noopener nofollow'; line(box, w); }
    var badges = el('p', 'badges');
    c.x.split(',').forEach(function (x) { badges.appendChild(el('span', 'badge exam', S.ex[x])); badges.appendChild(document.createTextNode(' ')); });
    if (c.s) badges.appendChild(el('span', 'badge ok', S.so));
    box.appendChild(badges);
    if (c.x.indexOf('tef') >= 0) {   // sessions ouvertes sur la carte CCI, pas des agréments
      var tp = el('p', 'finder-tef');
      tp.appendChild(c.tp ? fill(S.tefS, { '%d': day(f.d.tef), '%l': c.tp.join(COMMA) }) : document.createTextNode(S.tefN));
      if (c.tc) { tp.appendChild(document.createTextNode(' ')); var ca = el('a', null, S.tefC); ca.href = c.tc; ca.rel = 'noopener nofollow'; tp.appendChild(ca); }
      box.appendChild(tp);
    }
    var act = el('p', 'finder-actions');
    var dir = el('a', null, S.dir);
    dir.href = 'https://www.openstreetmap.org/search?query=' + encodeURIComponent([c.a || c.n, r.names[0], IX.C[r.cc] ? IX.C[r.cc][1] : r.cc].join(', '));
    dir.rel = 'noopener nofollow'; dir.target = '_blank'; act.appendChild(dir);
    var g = guide(c, r, f);
    if (g) { act.appendChild(document.createTextNode(' · ')); act.appendChild(g); }
    box.appendChild(act);
    return box;
  }
  function guide(c, r, f) {
    if (!c.g) return null;
    var x = exam(), order = (x === 'all' ? EXAMS : [x].concat(EXAMS)), recs = c.g.map(function (i) { return f.L[i]; });
    var langs = [LANG, 'fr', 'en', 'es', 'ar'].filter(function (l, i, a) { return a.indexOf(l) === i; });
    for (var li = 0; li < langs.length; li++) {
      var col = 2 + ['fr', 'en', 'es', 'ar'].indexOf(langs[li]);
      for (var e = 0; e < order.length; e++) for (var s = 0; s < 2; s++) {
        var rec = recs.filter(function (q) { return q[0] === order[e] && q[1] === (s ? 'p' : 'c') && q[col]; })[0];
        if (!rec) continue;
        var place = rec[1] === 'c' ? r.names[LI] : cname(r.cc);
        var a = el('a'); a.href = rec[col];
        a.appendChild(fill(S.guide, { '%e': S.ex[rec[0]], '%p': S.at(place, rec[1]) }));
        if (langs[li] !== LANG) { a.hreflang = langs[li]; a.appendChild(document.createTextNode(S.inl[langs[li]])); }
        return a;
      }
    }
    return null;
  }

  input.addEventListener('focus', index, { once: true });
  root.addEventListener('pointerdown', index, { once: true });
  if (window.requestIdleCallback) requestIdleCallback(index, { timeout: 4000 }); else setTimeout(index, 2500);
  input.addEventListener('input', function () {
    clearTimeout(timer);
    var v = input.value;
    timer = setTimeout(function () {
      var my = ++seq;
      if (!norm(v)) return close();
      suggest(v).then(function (items) { if (my === seq && input.value === v && document.activeElement === input) show(items); });
    }, 140);
  });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowDown') { e.preventDefault(); if (list.hidden) input.dispatchEvent(new Event('input')); else move(1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
    else if (e.key === 'Escape') { if (!list.hidden) { e.preventDefault(); close(); } else input.value = ''; }
    else if (e.key === 'Enter' && !list.hidden && active >= 0) { e.preventDefault(); pick(opts[active]); }
  });
  input.addEventListener('blur', function () { setTimeout(close, 120); });
  form.addEventListener('submit', function (e) { e.preventDefault(); clearTimeout(timer); submit(); });
  [].forEach.call(root.querySelectorAll('input[name="exam"]'), function (r) {
    r.addEventListener('change', function () {
      limit = 10;
      if (current) { run(); setURL(current.type === 'point' ? '' : current.label); }
      else setURL('');
    });
  });
  function locate(lat, lon) { current = { type: 'point', lat: lat, lon: lon, label: S.you }; limit = 10; input.value = ''; run(); }
  if (nearBtn && navigator.geolocation) {
    nearBtn.hidden = false;
    var note = root.querySelector('.finder-privacy'); if (note) note.hidden = false;
    nearBtn.addEventListener('click', function () {
      status(S.locating); index();
      navigator.geolocation.getCurrentPosition(function (pos) {
        status(''); setURL(''); locate(pos.coords.latitude, pos.coords.longitude);
      }, function (err) {
        status(err.code === 1 ? S.denied : err.code === 3 ? S.timeout : S.unavail);
      }, { timeout: 12000, maximumAge: 600000 });
    });
  }
  // État dans l'adresse : ?q=lyon&exam=tcf (partageable) ; ?lat=…&lon=… pour tester « autour de moi »
  var P = new URLSearchParams(location.search), ex = P.get('exam');
  if (ex && EXAMS.indexOf(ex) >= 0) { var r0 = root.querySelector('input[name="exam"][value="' + ex + '"]'); if (r0) r0.checked = true; }
  var la = parseFloat(P.get('lat')), lo = parseFloat(P.get('lon'));
  if (isFinite(la) && isFinite(lo) && Math.abs(la) <= 90 && Math.abs(lo) <= 180) { out.style.minHeight = '30em'; /* place réservée : la page ne saute pas */ index().then(function () { locate(la, lo); }); }
  else if (P.get('q')) { input.value = P.get('q'); out.style.minHeight = '30em'; submit(); }
})();
