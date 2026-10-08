# Pages /es/ et /en/ — glossaire et règles de rédaction (08/10/2026)

Les pages espagnoles et anglaises traduisent les pages pays françaises (`pays_config.py`) et, pour le
Canada, `/centres/tcf-canada/` et les cinq pages ville (`make_centres.py`, `villes_config.py`). On
**traduit, on ne recherche pas** : aucun prix, date, règle ou centre qui ne soit sur la page française.
Le moteur est `make_pays.py` ; le texte, `pays_config_es.py` et `pays_config_en.py` ; le partagé
(fichier FEI, sites corrigés, badges), `pays_i18n.py`. Contrôle : `python3 _build/check_i18n.py`.

## Variantes

| Pages | Variante | Exemples |
|---|---|---|
| Espagne | `es-ES`, espagnol d'Espagne | ordenador, convocatoria, matrícula, «bajo petición», web |
| Mexique, Colombie, Argentine, Chili, Pérou, Équateur | `es-419`, espagnol neutre d'Amérique latine | computadora, inscripción, «a solicitud», sitio web |
| États-Unis | `en-US`, anglais américain | test center, October 8, 2026, $330, enroll/register |
| Royaume-Uni | `en-GB` | test centre, 8 October 2026, £260, organisation |
| Canada | `en-CA` | test centre, 8 October 2026, $390 (dollars canadiens) |

- Espagnol : **tú** (comme l'app). Verbe de l'examen : *presentar* (MX, CO, PE, EC), *rendir* (AR, CL),
  *hacer* / *presentarse a* (ES). Guillemets « » → «» sans espaces ; incises avec —.
- Anglais : guillemets “ ” et apostrophe ’. Pas de « you will » répété ; phrases courtes.
- Une page = une variante, du titre aux FAQ.

## Formats

- Dates : es « 8 de octubre de 2026 », « 27/10 » dans les tableaux (jour/mois) ; en-US « October 8,
  2026 », tableaux « Oct 27 » (jamais 10/27 ni 27/10) ; en-GB/CA « 8 October 2026 », tableaux « 27 Oct ».
- Montants : comme on les écrit dans le pays, devise lisible. Mexique « 4,950 pesos » ; Colombie
  « 1.050.000 pesos » ; Argentine « 1.234.567 pesos » ; Chili « 299.000 pesos » ; Pérou « 1,240 soles » ;
  Équateur « 200 dólares » ou « USD 200 » ; Espagne « 275 € » ; US « $330 » ; UK « £260 » ; Canada
  « $390 ». Mentionner une fois le code ISO quand c'est utile (MXN, COP, CLP, PEN).
- Heures : es « 10 h » → « 10:00 » ; en-US « 10 a.m. » ; en-GB/CA « 10 am ».

## Termes

| Français | Espagnol | Anglais |
|---|---|---|
| centre agréé (par FEI) | centro autorizado | approved test center / centre |
| la liste de FEI | la lista de FEI | FEI’s list |
| relevé (du 8 octobre) | revisión de los sitios web (del 8 de octubre) | our check of the websites (on …) |
| « non relevé » (`NR`) | «sin datos» | “no data” |
| non publié | no publicado | not published |
| déclinaisons (Canada, Québec, IRN, tout public) | versiones | versions |
| TCF Canada / TCF Québec / TCF IRN | igual (nombre del examen, sin tilde) | same |
| TCF tout public | TCF tout public | TCF tout public |
| épreuve | prueba | test / section (“the speaking test”) |
| compréhension orale / écrite | comprensión oral / escrita | listening / reading |
| expression orale / écrite | expresión oral / escrita | speaking / writing |
| session, date de session | sesión (ES : convocatoria) | session, test date |
| sur ordinateur / papier | en computadora (ES : en ordenador) / en papel | computer-based / paper-based |
| sur demande | a solicitud (ES : bajo petición) | on request |
| inscription, s'inscrire | inscripción, inscribirte (ES : matrícula, matricularte) | registration, register |
| convocation (lettre) | citación | test-day notice (admission letter) |
| attestation de résultats | constancia de resultados | results certificate |
| recorrection | recalificación | re-marking |
| délai entre deux passations | plazo entre dos intentos | waiting period between two attempts |
| complet | completo (sin plazas / sin cupo) | full |
| liste d'attente | lista de espera | waitlist |
| organisme de gestion centrale (DELF) | organismo de gestión central | central management body |
| calendrier national des sessions | calendario nacional de sesiones | national session calendar |
| tarifs nationaux | tarifas nacionales | national fees |
| Entrée express | Express Entry | Express Entry |
| NCLC | NCLC | NCLC (CLB) |
| IRCC | IRCC | IRCC |
| Alliance française de X | Alianza Francesa de X | Alliance Française de X (nom propre tel quel) |
| Institut français | Instituto Francés (si c'est son nom local), sinon Institut français | Institut français |

## Ce qui ne se traduit pas

- Les **cartes des centres** (nom, adresse, téléphone, e-mail, site) viennent de FEI et du moteur ; on
  ne les recopie pas dans la config. Le moteur traduit les villes, régions et badges.
- Les noms propres des centres dans les tableaux : on peut les écrire sous leur forme locale
  (Alianza Francesa de Puebla, Universidad de Salamanca), jamais en inventer.
- Les liens vers des pages françaises (`/tef-canada/`, `/blog/…`) : on garde le texte, sans lien. Les
  « À lire aussi » pointent vers les pages de la même langue (`/es/…`, `/en/…`).

## L'app

- Espagnol : on peut dire « La app está en español » (déjà dans le CTA du moteur).
- Anglais : **ne jamais dire que l'app est entièrement en anglais** ; le CTA du moteur n'en parle pas.

## SEO

- Titre ≤ 60 caractères, description ≤ 155, construits sur la requête : « TCF Canada en México »,
  « TCF Canada test centres Toronto », « DELF exam London » — pas une traduction littérale du titre
  français.
- La réponse en tête : l'intro dit où, combien, quand, dès la première phrase.
- FAQ : les questions telles qu'on les tape (« ¿Cuánto cuesta el TCF Canada en Colombia? »).

## Guides et pages d'examen (2e vague, 08/10/2026)

Specs dans `i18n_pages_en.py` / `i18n_pages_es.py`, rendues par `make_i18n.py` ; modèles : les deux pilotes
anglais (`/en/tcf-canada/score-clb/`, `/en/tcf-canada-writing-tasks/`).

- **Source** : la page française **publiée** (`site/<chemin>/index.html`), pas seulement son script — beaucoup ont
  été retouchées à la main après génération. Même structure (sections, tableaux, encadrés, FAQ), mêmes faits.
- **Matière d'examen en français** : énoncés, consignes, transcriptions, questions et options restent en français,
  via `exo(lang, …)` / `sujet(lang, …)` de `i18n_blocks.py` (balisés `lang="fr"`) ; titres, conseils, explications
  et réponses sont traduits. Un exemple français cité dans le texte : entre « » (anglais) ou en *cursiva* (espagnol).
- **Liens** : vers les pages de la même langue quand elles existent (liste dans la consigne), sinon le texte sans
  lien. `also` : 3 liens, même langue.
- **Carte « Entraînez-vous »** : posée automatiquement avant le 3e h2 ; `inline_cta=False` si la page française
  n'en a pas (pages modules d'examen). CTA final : celui de la page française, traduit (`cta_h2`, `cta_p`).
- **Date** : la page porte la date de la traduction (8 octobre 2026) ; les phrases datées de la page française
  (« à jour au 7 août 2026 », « vérifié en juillet 2026 ») gardent leur date.

| Français | Espagnol | Anglais |
|---|---|---|
| compréhension orale / écrite (épreuve) | comprensión oral / escrita | listening / reading (test) |
| expression orale / écrite | expresión oral / escrita | speaking / writing |
| tâche (1, 2, 3) | tarea | task |
| consigne | consigna | instructions / prompt |
| barème, notation | baremo, puntuación | scoring |
| note éliminatoire | nota eliminatoria | minimum score per section |
| seuil de réussite (DELF : 50/100) | umbral de aprobación | pass mark |
| examen blanc | simulacro (de examen) | mock exam / practice test |
| QCM | preguntas de opción múltiple | multiple-choice questions |
| conformité à la consigne | adecuación a la consigna | task completion |
| registre (soutenu, familier) | registro (formal, coloquial) | register (formal, casual) |
| connecteurs | conectores | connectors |
| attestation de résultats | constancia de resultados | results certificate |
| recorrection | recalificación | re-marking |
| carte de résident / naturalisation | tarjeta de residente / nacionalidad | resident card / citizenship |
