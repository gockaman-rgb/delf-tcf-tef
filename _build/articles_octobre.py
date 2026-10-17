#!/usr/bin/env python3
"""Articles d'octobre 2026 (17/10), après lecture de Search Console.

- /blog/prix-tcf-tef/ réécrit : « prix tcf », « tcf prix », « prix tcf canada » se classaient de la 17e à la 58e
  place ; la page ne couvrait que la France et le Canada (relevé de juillet) alors que le site a des prix datés pour
  une quinzaine de pays. Aucun fait nouveau : chaque prix vient d'une page du site, avec sa date de relevé.
  (L'ancienne version vient de articles_batch1.py, qui refuse d'écraser ; c'est ce module qui fait foi désormais.)
- /logiciel-tcf/ (nouveau) : « tcf logiciel », « télécharger tcf logiciel », « tcf blanc » — pas de logiciel
  officiel, les deux ressources gratuites reconnues, et ce que fait l'app (faits de /contenu/, /examens-blancs/,
  /correction-ia/, /blog/examen-blanc-tcf-gratuit/).

Usage : python3 _build/articles_octobre.py   (réécrit ces pages : elles appartiennent à ce module)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from article_template import build  # noqa: E402
from pays_config import table  # noqa: E402

ARTICLES = []

# ===========================================================================
# Prix du TCF et du TEF, pays par pays
# ===========================================================================
PAYS = [
    ('<a href="/centres/tcf-france/">France</a>', "195 à 285 €", "de 195 € chez ACTE (Paris) à 285 € au CLPS (Rennes et Brest)", "17 sept. 2026"),
    ('<a href="/centres/tcf-canada/">Canada</a>', "390 à 440 $CA", "390 $ à l'Alliance française de Vancouver, 400 $ à Edmonton, 440 $ à l'UQTR ; aucun prix publié par l'Alliance Française de Montréal", "17 sept. 2026"),
    ('<a href="/centres/tcf-maroc/">Maroc</a>', "<strong>2 900 Dhs</strong>", "tarif national de l'Institut français du Maroc, affiché dans douze villes", "17 oct. 2026"),
    ('<a href="/centres/tcf-tunisie/">Tunisie</a>', "<strong>880 DT</strong>", "Institut français de Tunisie", "17 oct. 2026"),
    ('<a href="/centres/tcf-algerie/">Algérie</a>', "<strong>37 500 DA</strong>", "les cinq antennes de l'Institut français d'Algérie, payé en ligne sur la plateforme IFAL — les « 70 000 à 100 000 DA » qui circulent viennent d'un faux site", "17 oct. 2026"),
    ('<a href="/centres/tcf-etats-unis/">États-Unis</a>', "330 à 460 $US", "de 330 $ à Detroit à 460 $ à San Francisco", "8 oct. 2026"),
    ('<a href="/centres/tcf-royaume-uni/">Royaume-Uni</a>', "260 à 325 £", "260 £ à l'Institut français de Londres, 325 £ à l'Alliance française de Glasgow", "8 oct. 2026"),
    ('<a href="/centres/tcf-espagne/">Espagne</a>', "275 à 287 €", "287 € dans les Instituts français et à l'ILF (Séville), 281 € dans les Alliances françaises, 275 € au CELF (Séville)", "8 oct. 2026"),
    ('<a href="/centres/tcf-mexique/">Mexique</a>', "4 800 à 6 500 pesos", "Puebla 4 800, Guadalajara 4 950, IFAL à Mexico 5 150 (6 500 pour une date à la demande), UAEH à Pachuca 5 800", "8 oct. 2026"),
    ('<a href="/centres/tcf-colombie/">Colombie</a>', "dès 1 050 000 pesos", "1 050 000 à Medellín et Pereira, jusqu'à 1 247 000 à Bogotá", "8 oct. 2026"),
    ('<a href="/centres/tcf-chili/">Chili</a>', "299 000 pesos", "même tarif à l'Institut français du Chili (Santiago) et à l'Alliance française de Concepción", "8 oct. 2026"),
    ('<a href="/centres/tcf-perou/">Pérou</a>', "1 240 soles", "Alliance française de Lima, seul centre ; 992 soles au tarif adhérent", "8 oct. 2026"),
    ('<a href="/centres/tcf-equateur/">Équateur</a>', "200 à 300 $US", "200 $ à Cuenca, 300 $ à Guayaquil", "8 oct. 2026"),
    ('<a href="/centres/tcf-inde/">Inde</a>', "26 000 ₹", "New Delhi, Calcutta et Bhopal (TVA comprise à New Delhi et à Calcutta) ; Ahmedabad et Bangalore ne publient pas de prix", "8 oct. 2026"),
    ('<a href="/en/tcf-canada-dubai/" lang="en">Émirats arabes unis</a>', "1 800 AED", "Alliance Française de Dubaï (deux centres) et d'Abou Dhabi", "8 oct. 2026"),
    ('<a href="/en/tcf-canada-saudi-arabia/" lang="en">Arabie saoudite</a>', "1 950 SAR", "Alliance française d'Arabie Saoudite : Djeddah (20 octobre) et Riyad (12 novembre, complet)", "13 oct. 2026"),
    ('<a href="/centres/tcf-moyen-orient/">Égypte, Liban</a>', "non publié", "Instituts français : TCF Canada proposé, tarifs dans des calendriers PDF seulement", "13 oct. 2026"),
]

ARTICLES.append(dict(
    slug="prix-tcf-tef",
    title="Prix du TCF Canada 2026 : tous les pays (€, $, DA, Dhs, DT)",
    desc="Prix du TCF Canada pays par pays : 195 à 285 € en France, 390 à 440 $ au Canada, 37 500 DA en Algérie, 2 900 Dhs au Maroc, 880 DT en Tunisie. TCF IRN, TEF.",
    og_title="Prix du TCF Canada et du TEF 2026, pays par pays",
    og_desc="195 à 285 € en France, 390 à 440 $ au Canada, 2 900 Dhs au Maroc, 880 DT en Tunisie : les prix relevés sur les sites des centres, avec leurs dates.",
    crumb="Prix du TCF et du TEF",
    h1="Prix du TCF et du TEF en 2026 : ce que coûte chaque version, pays par pays",
    date_fr="17 octobre 2026", published="2026-08-07", modified="2026-10-17",
    read=8, accent="accent-tcf",
    intro="""Il n'existe <strong>aucun tarif officiel</strong> : ni France Éducation international ni Le français des
affaires ne publient de prix national, et c'est chaque <strong>centre agréé</strong> qui fixe le sien. D'où des
écarts du simple au double dans un même pays. Voici les prix que les centres affichaient sur leurs sites quand nous
les avons relevés : <strong>195 à 285 €</strong> en France pour le TCF Canada, <strong>390 à 440 $CA</strong> au
Canada, <strong>37 500 DA</strong> en Algérie, <strong>2 900 Dhs</strong> au Maroc, <strong>880 DT</strong> en
Tunisie — et une douzaine d'autres pays, chacun avec sa date.""",
    facts=["<strong>Aucun tarif national</strong>, aucun plafond : le prix est libre, fixé par chaque centre agréé.",
           "TCF Canada : <strong>195 à 285 €</strong> en France et <strong>390 à 440 $CA</strong> au Canada (17 septembre 2026), <strong>2 900 Dhs</strong> au Maroc, <strong>880 DT</strong> en Tunisie (17 septembre), <strong>1 800 AED</strong> aux Émirats et <strong>26 000 ₹</strong> en Inde (8 octobre).",
           "Algérie : <strong>37 500 DA</strong> pour le TCF Canada aux cinq antennes de l'Institut français (17 octobre 2026) ; les « 70 000 à 100 000 DA » qui circulent viennent d'un faux site.",
           "TCF IRN : <strong>140 € à 220 €</strong> à Paris (17 septembre 2026) ; TEF Canada : <strong>245 €</strong> relevé chez ALIP à Paris fin juillet 2026.",
           "⚠️ Le <strong>prix d'appel</strong> à 80–110 € correspond à la formule « 3 QCM » du TCF tout public, pas au test complet.",
           "Le vrai levier d'économie : le <strong>nombre d'épreuves</strong> (TCF Québec, TEFAQ), pas le choix du test."],
    toc=[("pays", "Le prix du TCF Canada, pays par pays"), ("pas-de-tarif", "Ce qui n'existe pas : le tarif officiel"),
         ("france", "France : toutes les versions"), ("appel", "Le piège du prix d'appel"), ("canada", "Canada"),
         ("maghreb", "Maghreb : des tarifs nationaux"), ("modularite", "Le vrai levier : le nombre d'épreuves"),
         ("cpf", "Ce que le CPF change à la facture")],
    body="""
<div class="stats">
<div class="stat"><b>195–285 €</b><span>TCF Canada en France</span><em>17 sept. 2026</em></div>
<div class="stat"><b>2 900 Dhs</b><span>TCF Canada au Maroc</span><em>tarif national</em></div>
<div class="stat"><b>880 DT</b><span>TCF Canada en Tunisie</span><em>tarif national</em></div>
</div>

<h2 id="pays">Le prix du TCF Canada, pays par pays</h2>
<p>Le tableau reprend les prix que nous avons lus sur les sites des centres, pays par pays, avec la date du relevé.
Chaque pays renvoie à sa page : les centres, leurs contacts et le détail centre par centre.</p>
""" + table("Prix du TCF Canada par pays, dans la monnaie locale, tels que les centres les affichaient à la date indiquée. "
            "Aucun tarif national : vérifiez sur la page du centre avant de payer.",
            ["Pays", "TCF Canada", "Détail", "Relevé le"], PAYS) + """
<p>Deux écarts sautent aux yeux. Dans les pays où un seul réseau organise le test — l'Institut français au Maroc,
en Tunisie, en Algérie —, <strong>le prix est national</strong> : le même partout. Là où plusieurs centres se
partagent le marché — la France, le Canada, les États-Unis, l'Amérique latine —, il varie d'un centre à l'autre,
parfois du simple au double. Et dans plusieurs pays, le prix n'est tout simplement pas publié : il ne s'affiche
qu'au moment de payer, ou dans un calendrier PDF.</p>

<h2 id="pas-de-tarif">Ce qui n'existe pas : le tarif officiel</h2>

<p>Aucun texte ne fixe ni ne plafonne le prix d'un TCF ou d'un TEF : c'est un <strong>prix libre</strong>, régi
par le droit commun de la concurrence. Méfiez-vous donc de tout site annonçant un tarif « officiel » ou une
« fourchette encadrée » — cette dernière formule, qui circule beaucoup, ne correspond à rien.</p>

<p>Ce que fait France Éducation international, sur chacune de ses pages de test, c'est vous renvoyer au centre :
c'est lui qui vous renseignera sur les dates, la procédure d'inscription, le lieu et le support de passation,
<em>ainsi que le tarif</em>. Le formulaire de demande d'agrément comporte d'ailleurs une case de tarif à remplir pour
chaque déclinaison et chaque formule. Certains centres le confirment à leur manière — l'université Toulouse Jean
Jaurès précise que ses tarifs de TCF sont votés « sous réserve de validation par le CA de l'Université ».</p>

<h2 id="france">France : toutes les versions</h2>

<div class="tablewrap">
<table>
<caption>Amplitude des tarifs relevés en France : une dizaine de centres agréés fin juillet 2026 ; TCF IRN et TCF Canada à Paris mis à jour le 17 septembre 2026. Indicatif : ces prix changent, et plusieurs centres précisent qu'ils sont modifiables sans préavis.</caption>
<thead><tr><th>Version</th><th>Le moins cher relevé</th><th>Le plus cher relevé</th><th>Écart</th></tr></thead>
<tbody>
<tr><td>TCF tout public — 3 QCM seuls</td><td>80 € <em>(Toulouse UT2J)</em></td><td>160 € <em>(ACCORD Paris)</em></td><td><strong>× 2</strong></td></tr>
<tr><td>TCF tout public — complet, 5 épreuves</td><td>185 € <em>(Toulouse UT2J)</em></td><td>260 € <em>(ACCORD Paris)</em></td><td>× 1,4</td></tr>
<tr><td><a href="/tcf-irn/">TCF IRN</a></td><td>140 € <em>(ACTE Paris)</em></td><td>220 € <em>(ACCORD Paris)</em></td><td><strong>× 1,6</strong></td></tr>
<tr><td><a href="/tcf-canada/">TCF Canada</a></td><td>195 € <em>(ACTE Paris)</em></td><td>285 € <em>(CLPS)</em></td><td>× 1,5</td></tr>
</tbody>
</table>
</div>

<p>Autres repères : le TCF Canada à <strong>220 €</strong> à l'Alliance Française de Lyon et <strong>200 €</strong> à
Montpellier (fin juillet) ; à Paris, 195 € chez ACTE et 220 € chez ACCORD, et le TCF IRN à 160 € chez Etoile Institut
(17 septembre). Le <a href="/tef-canada/">TEF Canada</a> était à <strong>245 €</strong> chez ALIP à Paris, et le TEF
IRN autour de <strong>155 à 205 €</strong> (fin juillet). Les centres de chaque grande ville, avec leurs prix :
<a href="/centres/tcf-paris/">Paris</a>, <a href="/centres/tcf-lyon/">Lyon</a>,
<a href="/centres/tcf-marseille/">Marseille</a>, <a href="/centres/tcf-montpellier/">Montpellier</a>.</p>

<p>La conclusion tient en une phrase : <strong>le prix ne départage pas le TCF et le TEF, il départage les centres et
les formules.</strong> Avant de choisir un test parce qu'il serait « moins cher », comparez deux ou trois centres
autour de vous — l'écart que vous y trouverez dépassera largement l'écart entre les deux familles.</p>

<h2 id="appel">Le piège du prix d'appel</h2>

<div class="note">
<p><strong>Les tarifs de TCF tout public les plus bas que vous verrez annoncés — 80 à 110 € — correspondent à la
formule « trois QCM seulement »</strong>, sans expression écrite ni orale. La version complète coûte à peu près le
double. Comparez toujours des formules identiques, pas des chiffres d'affiche.</p>
</div>

<p>Ce piège est d'autant plus coûteux que la formule courte ne convient pas à la plupart des démarches : dès qu'un
dossier exige une preuve d'expression écrite ou orale — et c'est le cas de la naturalisation, de l'immigration
canadienne et de l'admission universitaire —, les trois QCM ne suffisent pas. Payer 80 € pour un test inutilisable
revient plus cher que payer 185 € pour le bon.</p>

<h2 id="canada">Canada</h2>

<p>Au Canada, les tarifs publiés sont rares, et plus élevés qu'en France. Le 17 septembre 2026, nous avons lu
<strong>390 $</strong> à l'Alliance française de Vancouver, <strong>400 $</strong> à l'Alliance Française d'Edmonton
et <strong>440 $</strong> à l'EIF de l'UQTR, à Trois-Rivières ; l'Alliance Française de Montréal, elle, ne publie
aucun tarif — la seule somme affichée est un frais d'annulation de 75 $. À l'UQTR, le
<a href="/tcf-quebec/">TCF Québec</a> se paie à la carte : 105 $ par épreuve écrite ou de compréhension, 125 $ pour
l'expression orale (relevé du 30 juillet 2026). Les 47 centres canadiens, province par province, sont sur
<a href="/centres/tcf-canada/">notre page des centres au Canada</a>.</p>

<div class="note">
<p><strong>Une mise en garde.</strong> Les prix attribués aux grands centres canadiens par les comparateurs ne sont
pas sourcés, et mélangent souvent TCF Québec et TCF Canada — deux versions aux prix différents. Et nous n'avons
trouvé <strong>aucun prix canadien vérifiable pour le TEF Canada</strong> : ne croyez pas les tableaux qui affirment
que les deux tests y sont « au même prix ».</p>
</div>

<h2 id="maghreb">Maghreb : des tarifs nationaux, en dirhams et en dinars</h2>

<p>C'est l'exception : au Maroc et en Tunisie, le TCF Canada n'est organisé que par les Instituts français, qui
appliquent <strong>un tarif unique dans tout le pays</strong> et le publient. En Algérie aussi, l'Institut français a le
monopole et un tarif commun à ses cinq antennes, que leurs pages affichaient le 17 octobre 2026. Relevés :</p>

<div class="tablewrap">
<table>
<caption>Tarifs des Instituts français au Maghreb, lus sur leurs sites le 17 septembre 2026 (Maroc, Tunisie) et le 17 octobre 2026 (Algérie). Vérifiez sur la page du centre avant de payer.</caption>
<thead><tr><th>Pays</th><th>Version</th><th>Tarif</th></tr></thead>
<tbody>
<tr><td>Maroc — Institut français (Casablanca, Rabat, Marrakech, Tanger, Fès, Agadir…)</td><td>TCF Canada, TCF Québec, TEF Canada</td><td><strong>2 900 Dhs</strong></td></tr>
<tr><td>Maroc — Institut français</td><td>TCF IRN, TCF tout public</td><td><strong>1 900 Dhs</strong></td></tr>
<tr><td>Tunisie — Institut français (Tunis, Sousse, Sfax, El Mourouj…)</td><td>TCF Canada, TCF Québec</td><td><strong>880 DT</strong></td></tr>
<tr><td>Tunisie — Institut français</td><td>TCF IRN</td><td><strong>625 DT</strong></td></tr>
<tr><td>Tunisie — Institut français</td><td>TCF tout public sur ordinateur</td><td>335 DT + 220 DT par expression</td></tr>
<tr><td>Algérie — Institut français (Alger, Oran, Constantine, Annaba, Tlemcen)</td><td>TCF Canada, TCF Québec</td><td><strong>37 500 DA</strong></td></tr>
<tr><td>Algérie — Institut français</td><td>TCF DAP</td><td><strong>19 500 DA</strong></td></tr>
<tr><td>Algérie — Institut français</td><td>TCF tout public</td><td><strong>13 000 DA</strong></td></tr>
</tbody>
</table>
</div>

<div class="warn">
<p><strong>Algérie : les prix qui circulent viennent d'un faux site.</strong> Les « 70 000 à 100 000 DA » cités sur
les réseaux sont ceux d'un site frauduleux qui imite l'Institut français (if-algerie<em>.fr</em>) et propose un
« candidat partenaire ». Le seul site officiel est <strong>if-algerie.com</strong>, et la seule inscription passe par
la plateforme IFAL de VFS Global, où se paient les 37 500 DA du TCF Canada. Détails dans
<a href="/blog/tcf-canada-algerie/">notre guide algérien</a> et, pour la réservation,
<a href="/blog/ifal-tcf-rendez-vous/">IFAL TCF : prendre rendez-vous</a>.</p>
</div>

<p>Au Maroc, les règles sont aussi nationales : aucun remboursement, report sur justificatif facturé 500 Dhs, 20 jours
de carence entre deux TCF. En Tunisie, l'inscription se paie sur place, en espèces (carte bancaire à Tunis
seulement), après un rendez-vous en ligne ; les frais ne sont pas remboursables. Les guides par pays donnent la
procédure pas à pas : <a href="/blog/tcf-canada-maroc/">Maroc</a>, <a href="/blog/tcf-canada-tunisie/">Tunisie</a>,
<a href="/blog/tcf-canada-algerie/">Algérie</a> — et les pages par ville, les centres avec leurs contacts :
<a href="/centres/tcf-casablanca/">Casablanca</a>, <a href="/centres/tcf-rabat/">Rabat</a>,
<a href="/centres/tcf-tunis/">Tunis</a>, <a href="/centres/tcf-alger/">Alger</a>.</p>

<h2 id="modularite">Le vrai levier : le nombre d'épreuves</h2>

<p>Si vous cherchez à réduire la facture, ce n'est pas sur le choix du test qu'il faut jouer, c'est sur le
<strong>nombre d'épreuves que vous passez</strong>. Et là, les versions ne sont pas égales.</p>

<div class="tablewrap">
<table>
<caption>Modularité par version : combien d'épreuves êtes-vous obligé de passer.</caption>
<thead><tr><th>Régime</th><th>Versions</th><th>Conséquence sur le prix</th></tr></thead>
<tbody>
<tr><td><strong>Vraiment modulaire</strong></td><td>TCF Québec · TEFAQ</td><td>Vous payez 1 à 4 épreuves au choix</td></tr>
<tr><td>Modulaire par ajout</td><td>TCF tout public · TEF Études</td><td>Socle obligatoire, expressions en option</td></tr>
<tr><td><strong>Non modulaire</strong></td><td>TCF Canada · TEF Canada · TCF IRN · TEF IRN</td><td>Les 4 épreuves, toujours</td></tr>
</tbody>
</table>
</div>

<p>L'exemple le plus parlant vient du Québec. Plusieurs programmes n'exigent que l'oral — le PSTQ volet 2, la
condition faite au conjoint accompagnateur. À l'EIF de l'UQTR, ne passer que les deux épreuves orales du TCF Québec
revient à <strong>230 $CA</strong>, contre <strong>440 $CA</strong> pour un TCF Canada complet dans ce même centre.
À peu près la moitié, pour deux épreuves à préparer au lieu de quatre. En France, l'Alliance Française de
Montpellier applique <strong>65 € par module</strong> et Aix-Marseille <strong>60 € par épreuve</strong>, soit 130 €
ou 120 € pour les deux orales.</p>

<h2 id="cpf">Ce que le CPF change à la facture</h2>

<p>En France, le compte personnel de formation peut couvrir tout ou partie du coût — mais seulement pour les versions
<strong>enregistrées au répertoire spécifique</strong> de France compétences. Deux le sont : le <strong>TCF tout
public</strong> et le <strong>TCF IRN</strong>. Le TCF Canada n'est pas enregistré, et l'enregistrement du TCF
Québec a expiré fin 2021.</p>

<div class="note">
<p><strong>Méfiez-vous des comparaisons sur Mon Compte Formation.</strong> Les offres qu'on y trouve sont souvent des
<strong>forfaits préparation + examen</strong> : on rencontre par exemple 430 € pour un TCF IRN accompagné de
14 heures de préparation, contre 155 à 180 € pour l'examen seul ailleurs. Ce ne sont pas les mêmes produits. Le détail
version par version est dans notre article <a href="/blog/cpf-test-francais/">quels tests de français le CPF
finance</a>.</p>
</div>

<p>Dernier point à intégrer au budget : <strong>chaque tentative se paie</strong>. Il n'existe aucune reprise partielle
au TCF Canada ni aux versions IRN — on repasse les quatre épreuves. Savoir où l'on en est <em>avant</em> de s'inscrire
est donc, très concrètement, une décision financière : un <a href="/examens-blancs/">examen blanc au format
officiel</a> coûte le temps d'une matinée, une seconde tentative coûte le prix du test.</p>
""",
    cta_h2="Un test raté se repaie en entier",
    cta_p="""Examens blancs chronométrés au format officiel de chaque déclinaison, notation sur l'échelle du test que vous
passez, conversion NCLC, CLB et Échelle québécoise, correction IA de l'écrit et de l'oral. Savoir où vous en êtes
avant de payer 200 € ou 440 $ — dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
    faq=[("Combien coûte le TCF Canada ?", "Il n'y a pas de prix unique : en France, de 195 € à 285 € selon le centre ; au Canada, de 390 à 440 $CA (relevé du 17 septembre 2026) ; 2 900 Dhs au Maroc et 880 DT en Tunisie, tarifs nationaux des Instituts français ; 1 800 AED aux Émirats, 26 000 ₹ en Inde (8 octobre 2026). Vérifiez toujours le prix sur la page du centre avant de payer."),
         ("Combien coûte le TCF au Maroc, en Tunisie ou en Algérie ?", "Au Maroc, 2 900 Dhs pour le TCF Canada, le TCF Québec et le TEF Canada, 1 900 Dhs pour le TCF IRN et le TCF tout public. En Tunisie, 880 DT pour le TCF Canada et le TCF Québec, 625 DT pour le TCF IRN (relevé du 17 septembre 2026). En Algérie, 37 500 DA pour le TCF Canada et le TCF Québec, 19 500 DA pour le DAP et 13 000 DA pour le tout public, d'après les pages des antennes de l'Institut français (17 octobre 2026) — et les « 70 000 à 100 000 DA » qui circulent viennent d'un faux site."),
         ("Existe-t-il un tarif officiel pour le TCF ou le TEF ?", "Non. Ni France Éducation international ni Le français des affaires ne publient de tarif national, et aucun texte ne fixe ni ne plafonne ce prix : il est libre et fixé par chaque centre agréé. Méfiez-vous des sites annonçant un tarif « officiel »."),
         ("Combien coûte le TCF IRN ?", "À Paris, 140 € chez ACTE et 220 € chez ACCORD le 17 septembre 2026, 160 € chez Etoile Institut. Ailleurs en France, l'écart est du même ordre : demandez le tarif à votre centre avant de vous inscrire."),
         ("Combien coûte le TEF Canada ?", "Nous avons relevé 245 € chez ALIP à Paris fin juillet 2026 ; au Maroc, le TEF Canada est au tarif national de 2 900 Dhs. Au Canada, nous n'avons trouvé aucun tarif TEF Canada vérifiable."),
         ("Pourquoi vois-je des TCF annoncés à 80 € ?", "Parce qu'il s'agit de la formule « trois QCM seulement » du TCF tout public, sans expression écrite ni orale. La version complète coûte à peu près le double, et la formule courte ne convient pas aux démarches qui exigent une preuve d'expression."),
         ("Comment payer moins cher ?", "En passant moins d'épreuves, quand votre démarche le permet : le TCF Québec et le TEFAQ sont modulaires (1 à 4 épreuves au choix). Les versions Canada et IRN imposent les quatre épreuves — et chaque tentative se paie en entier, d'où l'intérêt d'un examen blanc avant de s'inscrire."),
         ("Le CPF peut-il financer mon test ?", "Seulement pour les versions enregistrées au répertoire spécifique de France compétences : le TCF tout public et le TCF IRN. Le TCF Canada n'est pas enregistré, et l'enregistrement du TCF Québec a expiré fin 2021.")],
    also=[("/tcf-canada/prix-inscription/", "TCF Canada : prix, inscription, validité", "Comment s'inscrire, la double règle des deux ans et le délai entre deux tentatives."),
          ("/blog/tcf-canada-maroc/", "TCF Canada au Maroc", "Le tarif national, les centres et la procédure, ville par ville."),
          ("/logiciel-tcf/", "Logiciel TCF : s'entraîner sur ordinateur et mobile", "Ce qui existe vraiment pour s'entraîner au format officiel."),
          ("/blog/cpf-test-francais/", "Quels tests de français le CPF finance en 2026", "Version par version : ce qui est enregistré, ce qui ne l'est plus.")],
    sources="""<strong>Ces prix changent.</strong> Les tarifs cités ont été relevés sur les sites des centres eux-mêmes, à la
date indiquée pour chacun (de fin juillet au 17 octobre 2026), et plusieurs centres précisent qu'ils sont modifiables
sans préavis. Ils sont donnés à titre indicatif et non comme un barème : vérifiez le tarif en vigueur sur la page du
centre où vous comptez vous inscrire.""",
))


# ===========================================================================
# Logiciel TCF : ce qui existe pour s'entraîner (nouveau, 17/10/2026)
# ===========================================================================
ARTICLES.append(dict(
    slug="logiciel-tcf", section="", crumb="Logiciel TCF",
    title="Logiciel TCF 2026 : s'entraîner sur ordinateur et mobile",
    desc="Il n'existe pas de logiciel TCF officiel à télécharger. Les deux entraînements gratuits reconnus, et une app d'examens blancs au format officiel.",
    h1="Logiciel TCF : ce qui existe vraiment pour s'entraîner",
    date_fr="17 octobre 2026", published="2026-10-17", modified="2026-10-17",
    read=5, accent="accent-tcf",
    intro="""Inutile de chercher à <strong>télécharger « le logiciel du TCF »</strong> : il n'existe pas. Le TCF se passe
dans un centre agréé, souvent <strong>sur ordinateur</strong> — mais sur les postes du centre, avec des sujets
confidentiels que personne n'a le droit de diffuser. Ce qui existe, en revanche : <strong>deux entraînements gratuits
reconnus</strong> par France Éducation international, et des <strong>applications d'examens blancs</strong> qui
reproduisent le format officiel. Voici ce que chacun couvre, et ce qu'il ne couvre pas.""",
    facts=["<strong>Aucun logiciel officiel à télécharger</strong> : les sujets du TCF sont confidentiels, toute reproduction est interdite.",
           "« TCF sur ordinateur » (TCF SO) : la session se passe sur les postes du centre ; le centre indique s'il la propose.",
           "Gratuit et officiel : <strong>TV5MONDE</strong> (17 séries, 680 questions) et <strong>RFI</strong> (12 sessions de compréhension orale de 16 questions).",
           "Ce que le gratuit ne couvre pas : l'<strong>expression écrite et orale</strong>, et l'examen blanc complet chronométré.",
           "L'app « TCF DELF TEF : Tests 2026 » (iPhone) : 16 547 items, 1 320 fichiers audio natifs, examens blancs au format officiel, correction IA de l'écrit et de l'oral."],
    toc=[("officiel", "Pas de logiciel officiel : pourquoi"), ("ordinateur", "Le TCF sur ordinateur"),
         ("gratuit", "Les deux entraînements gratuits reconnus"), ("app", "Une app d'examens blancs"),
         ("choisir", "Comment s'entraîner, concrètement")],
    body="""
<h2 id="officiel">Pas de logiciel officiel : pourquoi</h2>
<p>Les sujets du TCF sont <strong>strictement confidentiels</strong> : toute reproduction ou diffusion, partielle ou
totale — question, image ou son — est interdite. Il n'existe donc ni annales officielles, ni « logiciel du TCF » à
installer chez soi. Un site qui propose de télécharger « le vrai TCF » ou les « sujets du mois » diffuse soit des
contrefaçons, soit des documents obtenus illégalement — un risque parfaitement inutile quand un dossier d'immigration
ou de naturalisation est en jeu.</p>
<p>Le TCF est un test standardisé, calibré et certifié ISO 9001 : chaque question est prétestée puis pondérée selon sa
difficulté. Vous n'avez pas besoin des vrais sujets — vous avez besoin de <strong>maîtriser le format</strong>. Et
le format, lui, s'apprend librement.</p>

<h2 id="ordinateur">Le TCF sur ordinateur</h2>
<p>Beaucoup de centres agréés proposent des <strong>sessions sur ordinateur</strong> — c'est ce que désigne le « TCF SO »,
par opposition au TCF papier. La liste officielle de France Éducation international indique, centre par
centre, s'il propose cette option : nos pages par ville la reprennent, par exemple <a href="/centres/tcf-paris/">Paris</a>
(sept centres, tous sur ordinateur), <a href="/centres/tcf-alger/">Alger</a> ou
<a href="/centres/tcf-casablanca/">Casablanca</a>. Le jour J, vous travaillez sur les postes du centre : rien à
installer, rien à télécharger. Le format des épreuves, lui, est le même sur papier et sur ordinateur — ce qui compte,
c'est de s'y être entraîné.</p>

<h2 id="gratuit">Les deux entraînements gratuits reconnus</h2>
<p>France Éducation international cite deux ressources gratuites, et deux seulement :</p>
<ul>
<li><strong>TV5MONDE</strong> : 17 séries d'entraînement, soit 680 questions de compréhension orale, de structures de la
langue et de compréhension écrite, rédigées par les concepteurs des épreuves officielles.</li>
<li><strong>RFI</strong> (« Le français facile avec RFI ») : 12 sessions de compréhension orale de 16 questions, signées
France Éducation international.</li>
</ul>
<p>Elles sont excellentes pour la compréhension. Ce qu'elles ne couvrent pas — <strong>l'expression écrite et
orale</strong>, et la simulation complète chronométrée — est justement ce qui fait perdre le plus de points le jour J.
Le détail, et comment les transformer en vrai examen blanc : <a href="/blog/examen-blanc-tcf-gratuit/">examen blanc TCF
gratuit : les vraies ressources</a>.</p>

<h2 id="app">Une app d'examens blancs au format officiel</h2>
<p>L'application <strong>« TCF DELF TEF : Tests 2026 »</strong> (sur iPhone, dans l'App Store) est construite pour
combler ce que le gratuit ne couvre pas :</p>
<ul>
<li><strong>15 variantes d'examens au format officiel</strong> — TCF Canada, TCF IRN, TCF Québec, TEF, DELF, DALF —,
chronométrées, avec la notation de l'échelle du test (<a href="/examens-blancs/">ce qu'un examen blanc
doit respecter</a>) ;</li>
<li><strong>une correction IA de l'écrit et de l'oral</strong> sur les critères officiels : pertinence, cohérence,
lexique, grammaire, orthographe, et pour l'oral prononciation et fluidité (<a href="/correction-ia/">comment elle
fonctionne</a>) ; la correction nécessite une connexion ;</li>
<li><strong>16 547 items</strong> dans les banques principales et <strong>1 320 fichiers audio natifs</strong> — pas de
synthèse vocale sur les épreuves d'écoute (décompte du 29 juillet 2026, <a href="/contenu/">banque par banque</a>) ;</li>
<li>des sujets <strong>100 % originaux</strong>, chaque réponse expliquée, et vos erreurs qui reviennent en
répétition espacée ;</li>
<li>le reste <strong>hors ligne</strong>, sans compte.</li>
</ul>

<h2 id="choisir">Comment s'entraîner, concrètement</h2>
<ol>
<li><strong>Un premier examen blanc complet</strong>, chronométré, avant toute révision : c'est le diagnostic qui décide
du reste.</li>
<li><strong>La compréhension sur les ressources gratuites</strong> : TV5MONDE et RFI, en écoute unique, comme le jour J.</li>
<li><strong>L'expression avec une correction</strong> : c'est là que se jouent les points — un seul point sur 20 peut
faire changer de niveau NCLC.</li>
<li><strong>Environ un examen blanc par semaine</strong> en phase de préparation, puis <strong>deux ou trois complets
dans les dix derniers jours</strong>, pour l'endurance et la gestion du temps (<a href="/examens-blancs/#calendrier">à quel
rythme en passer</a>).</li>
</ol>
""",
    cta_h2="S'entraîner au format officiel, sur iPhone",
    cta_p="""Examens blancs chronométrés de chaque déclinaison, correction IA de l'écrit et de l'oral sur les critères
officiels, 1 320 fichiers audio natifs et le reste hors ligne — dans l'app «&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;».""",
    faq=[("Existe-t-il un logiciel TCF officiel à télécharger ?", "Non. Les sujets du TCF sont confidentiels et leur reproduction est interdite : il n'existe ni logiciel officiel à installer, ni annales. Les sites qui proposent de « télécharger le TCF » diffusent des contrefaçons ou des documents obtenus illégalement."),
         ("Qu'est-ce que le TCF sur ordinateur (TCF SO) ?", "Une session du TCF passée sur les postes informatiques du centre agréé, plutôt que sur papier. La liste officielle de France Éducation international indique, centre par centre, si cette option existe ; le format des épreuves est le même."),
         ("Où trouver un TCF blanc gratuit ?", "Sur TV5MONDE (17 séries, 680 questions) et sur RFI (12 sessions de compréhension orale de 16 questions), les deux ressources citées par France Éducation international. Elles ne couvrent ni l'expression écrite et orale, ni l'examen complet chronométré."),
         ("Existe-t-il une application pour s'entraîner au TCF ?", "Oui : l'app « TCF DELF TEF : Tests 2026 », sur iPhone, propose des examens blancs au format officiel de chaque déclinaison et une correction IA de l'écrit et de l'oral ; elle n'utilise que des sujets originaux.")],
    also=[("/blog/examen-blanc-tcf-gratuit/", "Examen blanc TCF gratuit : les vraies ressources", "Ce que couvrent TV5MONDE et RFI, et comment en faire un vrai examen blanc."),
          ("/examens-blancs/", "Examens blancs au format officiel", "Durées officielles, barèmes et protocole de passation, examen par examen."),
          ("/blog/prix-tcf-tef/", "Prix du TCF Canada, pays par pays", "Ce que coûte une tentative — et pourquoi il vaut mieux être prêt.")],
    sources="""<strong>Sources.</strong> Les pages TCF de France Éducation international (ressources d'entraînement citées,
liste des centres et option « sessions sur ordinateur ») ; pour l'app, le décompte direct des fichiers de contenu du
29 juillet 2026 (page <a href="/contenu/">Contenu de l'app</a>).""",
))


# ===========================================================================
# IFAL : prendre rendez-vous pour le TCF en Algérie (nouveau, 17/10/2026)
# « ifal tcf », « ifal », « tcf ifal », « ifal vfs », « rendez-vous tcf alger 2026 » — faits relevés le 17/10/2026
# sur if-algerie.com (page nationale, FAQ, pages des antennes) et la page d'accueil publique d'IFAL, sans connexion.
# ===========================================================================
ARTICLES.append(dict(
    slug="ifal-tcf-rendez-vous", crumb="IFAL : rendez-vous TCF",
    title="IFAL TCF 2026 : prendre rendez-vous sur la plateforme VFS",
    desc="Rendez-vous TCF sur la plateforme IFAL (VFS Global) : les étapes, les tarifs 2026 (Canada 37 500 DA), les pièces, 26 ou 36 jours, les lieux, l'assistance.",
    h1="IFAL : prendre rendez-vous pour le TCF en Algérie, étape par étape",
    date_fr="17 octobre 2026", published="2026-10-17", modified="2026-10-17",
    read=6, accent="accent-tcf",
    intro="""En Algérie, tous les TCF — Canada, Québec, DAP, tout public, IRN — se réservent sur une seule plateforme :
<strong>IFAL</strong>, opérée par <strong>VFS Global</strong> pour l'Institut français d'Algérie, à l'adresse
forms.vfsglobal.com.dz/IFAL. « Les inscriptions et les paiements se font exclusivement en ligne » : pas de guichet,
pas d'intermédiaire. Voici comment prendre rendez-vous, quelle déclinaison choisir et ce qu'elle coûte (relevé du
17 octobre 2026), où se passe l'examen dans les cinq antennes, et qui contacter quand ça bloque.""",
    facts=["Plateforme unique : <strong>IFAL</strong> (forms.vfsglobal.com.dz/IFAL), opérée par VFS Global, à ouvrir depuis la page TCF de <strong>if-algerie.com</strong>.",
           "Sans compte, la plateforme n'affiche ni session ni prix : seulement « Connexion » et « Créer un compte ».",
           "Tarifs TTC des antennes (17 octobre 2026) : <strong>TCF Canada et TCF Québec 37 500 DA</strong>, TCF DAP 19 500 DA, TCF tout public 13 000 DA.",
           "<strong>26 jours</strong> entre deux inscriptions selon la page nationale, <strong>36</strong> selon les pages d'Oran, Constantine, Annaba et Tlemcen.",
           "Assistance VFS : <strong>info.tcfalg@vfshelpline.com</strong>, 021 99 60 08 ; centre d'appel +213 21 99 88 03.",
           "⚠️ Le site officiel est <strong>if-algerie.com</strong> ; if-algerie.fr est une escroquerie."],
    toc=[("etapes", "Prendre rendez-vous, étape par étape"), ("declinaisons", "Quelle déclinaison choisir, et à quel prix"),
         ("sigles", "DAP, TP, SO : les sigles"), ("delai", "26 ou 36 jours entre deux inscriptions"),
         ("lieux", "Où se passe l'examen, antenne par antenne"), ("aide", "Qui contacter quand ça bloque"),
         ("fraude", "Le faux site à éviter")],
    body="""
<h2 id="etapes">Prendre rendez-vous, étape par étape</h2>
<p>L'Institut résume la démarche en une phrase : « Pour vous inscrire, connectez-vous sur la plateforme VFS, et
suivez les étapes d'inscription. » Sans compte, la page d'accueil d'IFAL n'affiche que « Inscription au TCF »,
« Connexion » et « Créer un compte » — ni session, ni prix : ils n'apparaissent qu'une fois connecté. Le chemin
sûr :</p>
<ol>
<li><strong>Partez de if-algerie.com</strong>, rubrique « Tests et examens › TCF » ou page TCF de votre antenne, et
suivez le lien d'inscription : il mène à forms.vfsglobal.com.dz/IFAL. N'ouvrez jamais la plateforme depuis un lien
reçu par messagerie ou trouvé dans une publicité.</li>
<li><strong>Créez votre compte</strong> avec une adresse e-mail que vous consultez : la convocation et l'attestation
y arriveront — l'Institut ne remet plus d'attestation papier depuis mars 2023.</li>
<li><strong>Choisissez la déclinaison</strong> (tableau ci-dessous), <strong>l'antenne</strong> et <strong>la
session</strong>. « Des sessions TCF sont ouvertes tous les mois sur les cinq antennes », mais aucune ne publie de
calendrier sur son site : les dates n'existent que sur la plateforme.</li>
<li><strong>Payez en ligne</strong> : « Les inscriptions et les paiements se font exclusivement en ligne. »</li>
<li><strong>Le jour J</strong>, venez avec votre convocation et la pièce déclarée : carte d'identité biométrique ou
passeport pour les Algériens, passeport biométrique ou carte consulaire pour les autres. Jamais le permis de
conduire : à Alger, « l'inscription avec le PERMIS DE CONDUIRE est annulée et aucun remboursement n'est
possible ».</li>
</ol>

<h2 id="declinaisons">Quelle déclinaison choisir, et à quel prix</h2>
<p>La plateforme propose toutes les versions du TCF, et se tromper de case coûte une session : pour Entrée express
ou la citoyenneté canadienne, IRCC n'accepte que le <strong>TCF Canada</strong>.</p>
""" + table("Déclinaisons du TCF réservables sur IFAL et tarifs TTC lus sur les pages TCF des antennes de l'Institut français d'Algérie le 17 octobre 2026. La plateforme fait foi au moment de payer.",
            ["Déclinaison", "Pour quoi faire", "Épreuves", "Tarif"],
            [("<strong>TCF Canada</strong>", "Immigration ou citoyenneté canadienne (IRCC)", "Compréhension orale 35 min, compréhension écrite 60 min, expression écrite 60 min, expression orale 12 min", "<strong>37 500 DA</strong>"),
             ("TCF Québec", "Dossier d'immigration au Québec (MIFI)", "Mêmes durées que le TCF Canada", "37 500 DA"),
             ("TCF DAP", "Demande d'admission préalable : licence 1 ou école d'architecture en France, dès 16 ans", "Trois QCM (25, 15 et 45 min) et une expression écrite de 60 min", "19 500 DA"),
             ("TCF tout public (TP)", "Faire reconnaître son niveau, poursuite d'études", "Trois QCM : compréhension orale, structures de la langue, compréhension écrite", "13 000 DA"),
             ("TCF IRN", "Nationalité française, carte de résident, carte de séjour pluriannuelle", "Quatre épreuves", "14 000 DA (Constantine, Tlemcen)")]) + """
<p>Les épreuves d'expression ajoutées à un TCF tout public coûtent 7 000 DA chacune à Alger ; elles ne remplacent pas
les épreuves d'expression du TCF Canada, précise l'antenne.</p>

<h2 id="sigles">DAP, TP, SO : les sigles</h2>
<ul>
<li><strong>DAP</strong> : demande d'admission préalable. Le TCF DAP s'adresse, selon l'Institut, à « toute personne
étrangère de plus de 16 ans » qui veut entrer en licence 1 ou dans une école d'architecture en France.</li>
<li><strong>TP</strong> : tout public — le TCF qui atteste un niveau de français, sans démarche précise.</li>
<li><strong>SO</strong> : sur ordinateur. Le sigle n'apparaît pas sur les pages de l'Institut français d'Algérie ;
l'Institut français de Tunisie, lui, écrit « TCF/TP-SO » pour le TCF « tout public – sur ordinateur ». Les cinq
antennes algériennes figurent avec l'option « sessions sur ordinateur » dans la liste de France Éducation
international, et l'Institut indique que le TCF DAP et le tout public existent « en version électronique et sur
papier ».</li>
</ul>

<h2 id="delai">26 ou 36 jours entre deux inscriptions</h2>
<p>La page TCF nationale de l'Institut écrit : « vous devez respecter un délai de 26 jours entre 2 inscriptions
TCF ». Le 17 octobre 2026, les pages des antennes d'Oran, de Constantine, d'Annaba et de Tlemcen écrivaient
<strong>36 jours</strong> ; celle d'Alger n'en donnait pas. Tant que les deux chiffres coexistent, comptez 36 jours
avant de réserver une seconde session — et souvenez-vous qu'aucune recorrection n'est possible pour les sessions
tenues depuis le 1<sup>er</sup> septembre 2026 : améliorer un score, c'est repasser le test.</p>
<p>En cas d'empêchement, à Alger, « seules les absences justifiées (certificat médical, décès d'un proche, problème
de transport ou obligation professionnelle) transmises à l'IFA dans un délai de 5 semaines après la session seront
acceptées ».</p>

<h2 id="lieux">Où se passe l'examen, antenne par antenne</h2>
<p>Le lieu de passation n'est pas toujours l'adresse de l'antenne. Ce qu'indiquaient leurs pages TCF le 17 octobre
2026 — l'adresse qui fait foi reste celle de votre convocation :</p>
""" + table("Lieux de passation du TCF indiqués par les antennes de l'Institut français d'Algérie, 17 octobre 2026.",
            ["Antenne", "Lieu de passation", "Contact examens", "Page de la ville"],
            [("<strong>Alger</strong>", "30, rue des Frères-Kadri, Hydra — TCF Canada sur deux jours, l'oral le lendemain", "Assistance VFS", '<a href="/centres/tcf-alger/">TCF à Alger</a>'),
             ("<strong>Oran</strong>", "« Institut Français d'Oran, ELS USTO »", "examens.oran@if-algerie.com · 041 70 73 73", '<a href="/centres/tcf-oran/">TCF à Oran</a>'),
             ("<strong>Constantine</strong>", "Annexe Nouvelle ville Ali Mendjeli, UV7, lot n° 52 (tramway El Istiklel)", "examens.constantine@if-algerie.com", '<a href="/centres/tcf-constantine/">TCF à Constantine</a>'),
             ("<strong>Annaba</strong>", "« Institut Français d'Annaba, Majestic »", "examens.annaba@if-algerie.com", '<a href="/centres/tcf-annaba/">TCF à Annaba</a>'),
             ("<strong>Tlemcen</strong>", "45, boulevard Dergal-Abdelkader (Imam Ali), résidence Yasmine — TCF Canada sur toute la journée", "examens.tlemcen@if-algerie.com", '<a href="/centres/tcf-tlemcen/">TCF à Tlemcen</a>')]) + """

<h2 id="aide">Qui contacter quand ça bloque</h2>
<ul>
<li><strong>Rendez-vous, compte, paiement</strong> : le service d'assistance VFS, <strong>info.tcfalg@vfshelpline.com</strong>,
021 99 60 08 — le numéro de la page nationale. Les pages de Constantine et de Tlemcen donnent le centre d'appel VFS,
+213 21 99 88 03.</li>
<li><strong>Besoins spécifiques</strong> (handicap, aménagement, dispense) : écrire à VFS « au moins deux (2) mois
avant la passation », avec le dossier médical, la carte de handicap et le certificat médical.</li>
<li><strong>Convocation, attestation, lieu</strong> : l'adresse « examens » de votre antenne, dans le tableau
ci-dessus.</li>
</ul>

<h2 id="fraude">Le faux site à éviter</h2>
<div class="warn"><strong>if-algerie.fr n'est pas l'Institut français d'Algérie.</strong> Le 17 septembre 2026, ce site
proposait un « TCF Canada » à 70 000, 80 000 ou 100 000 DA « selon le niveau », avec un « candidat partenaire » qui
passe l'examen à votre place. Le seul site officiel est <strong>if-algerie.com</strong>, et la seule inscription passe
par la plateforme IFAL. Le détail, et ce que la fraude vous ferait perdre :
<a href="/blog/tcf-canada-algerie/#faux-site">notre guide du TCF Canada en Algérie</a>.</div>
""",
    cta_h2="37 500 DA la tentative : arrivez prêt",
    cta_p="""Une session par mois, 26 à 36 jours avant de pouvoir repasser, un score définitif : les examens blancs de l'app
«&nbsp;TCF DELF TEF&nbsp;: Tests 2026&nbsp;», sur iPhone, reproduisent les quatre épreuves du TCF Canada au format
officiel, notées sur 699 et converties en NCLC, avec la correction IA de l'écrit et de l'oral.""",
    faq=[("Comment prendre rendez-vous pour le TCF sur IFAL ?", "En ligne uniquement : depuis la page TCF de if-algerie.com, ouvrez la plateforme IFAL (forms.vfsglobal.com.dz/IFAL), créez un compte, choisissez la déclinaison, l'antenne et la session, puis payez en ligne. Sans compte, la plateforme n'affiche ni session ni prix."),
         ("Combien coûte le TCF en Algérie en 2026 ?", "37 500 DA pour le TCF Canada et le TCF Québec, 19 500 DA pour le TCF DAP, 13 000 DA pour le TCF tout public : tarifs TTC affichés par les antennes de l'Institut français d'Algérie le 17 octobre 2026. Le TCF IRN est affiché à 14 000 DA à Constantine et à Tlemcen."),
         ("Qui contacter en cas de problème sur la plateforme IFAL ?", "Le service d'assistance VFS : info.tcfalg@vfshelpline.com, 021 99 60 08 ; certaines antennes donnent aussi le centre d'appel VFS, +213 21 99 88 03. Pour la convocation ou l'attestation, l'adresse « examens » de l'antenne."),
         ("Combien de jours entre deux inscriptions au TCF ?", "26 jours selon la page TCF nationale de l'Institut français d'Algérie, 36 selon les pages des antennes d'Oran, Constantine, Annaba et Tlemcen (17 octobre 2026). Par prudence, comptez 36 jours."),
         ("Peut-on s'inscrire au TCF sur place, dans une antenne ?", "Non : « Les inscriptions et les paiements se font exclusivement en ligne », répond la FAQ de l'Institut français d'Algérie."),
         ("Pourquoi je ne vois aucune date sur IFAL ?", "Sans compte, la plateforme n'en affiche aucune, et aucune antenne ne publie de calendrier sur son site : « des sessions TCF sont ouvertes tous les mois sur les cinq antennes », indique l'Institut. Une fois connecté, si votre antenne est pleine, essayez-en une autre."),
         ("Que veut dire TCF DAP ?", "Le TCF de la demande d'admission préalable, exigé pour entrer en licence 1 ou dans une école d'architecture en France ; il s'adresse aux étrangers de plus de 16 ans et coûte 19 500 DA en Algérie (17 octobre 2026).")],
    also=[("/blog/tcf-canada-algerie/", "TCF Canada en Algérie : où le passer, comment s'inscrire", "Les cinq antennes, les résultats, le faux site à éviter."),
          ("/centres/tcf-algerie/", "Les 5 centres TCF en Algérie", "Les antennes de l'Institut français, avec leurs contacts."),
          ("/centres/tcf-alger/", "TCF à Alger", "L'antenne de Hydra, ses tarifs, l'examen civique."),
          ("/blog/prix-tcf-tef/", "Prix du TCF Canada 2026, pays par pays", "Ce que coûte une tentative ailleurs.")],
    sources="""<strong>Sources.</strong> Site de l'Institut français d'Algérie (if-algerie.com) — page TCF nationale, FAQ, page
« TCF pour les candidats ayant des besoins spécifiques », présentation des tests, pages TCF des antennes d'Oran, de
Constantine, d'Annaba et de Tlemcen, et contenu de la page TCF d'Alger, qui ne s'affichait pas ce jour-là ; page
d'accueil de la plateforme IFAL, sans connexion ; tous consultés le 17 octobre 2026. Liste des centres TCF de France
Éducation international (filtre « Algérie »), 19 septembre 2026. Tarifs et délais changent sans préavis : la
plateforme fait foi au moment de payer.""",
))


def main():
    build(ARTICLES, overwrite=True)


if __name__ == "__main__":
    main()
