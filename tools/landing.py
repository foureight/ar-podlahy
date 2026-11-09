# Landing pages pro jednotlivé materiály (Dřevěné podlahy, Parkety, Vinyl, PVC, Koberce)
# Fakta podle listu faktů od klienta (PDF SEORadar, vyplněno 11/2026). Ceny bez DPH.
import re
from pages import EYE, H2, P, WRAP, CARD, I_CHECK, sec

STERKA = 250   # Kč/m² při 5 mm
LISTY = 59     # Kč/bm
NOTE = 'Ceny jsou bez DPH.'

COMMON_FAQ_ZARUKA = ('Jakou dáváte záruku?', 'Záruka až 12 let na materiál, 24 měsíců na práci. Ke každé zakázce nad 100 m² přidáme sadu na údržbu podlahy zdarma.')
COMMON_FAQ_TERMIN = ('Jak rychle to stihnete?', 'Na zaměření přijedeme do 48 hodin. Samotná montáž 100 m² trvá do 7 pracovních dní včetně úpravy podkladu. Celkově od poptávky do 6 týdnů u materiálů na objednávku, u materiálu skladem i dříve.')

CONF = {
 'drevo': dict(
    slug='drevene-podlahy-praha', design='Drevene-podlahy', crumb='Dřevěné podlahy Praha', form='Dřevěná vícevrstvá podlaha',
    title='Dřevěné podlahy Praha – materiál od 569 Kč/m², pokládka od 249 Kč/m² | AR podlahy',
    desc='Pokládka dřevěných podlah v Praze a Středočeském kraji: masiv, vícevrstvé podlahy, parkety a renovace. Materiál od 569 Kč/m², pokládka od 249 Kč/m², zaměření zdarma do 48 hodin.',
    service='Pokládka dřevěných podlah', minprice=249,
    h1='Dřevěné podlahy v Praze a Středočeském kraji', sub='Masivní, vícevrstvé podlahy i parkety, které vydrží generace.',
    bullets=['Zaměření zdarma do 48 hodin', 'Materiál od 569 Kč/m², pokládka od 249 Kč/m²', 'Záruka až 12 let na materiál, 24 měsíců na práci'],
    eyebrow='Co pokládáme', h2='Dřevěná podlaha pro byt, dům i památku',
    cards=[
      ('Masivní dřevěné podlahy', 'Poctivá prkna z masivu, nejčastěji dub. Celoplošně lepená vydrží generace, zvládnou i podlahové topení a dají se opakovaně brousit.', 'pokládka lepená od 295 Kč/m²'),
      ('Vícevrstvé (třívrstvé) podlahy', 'Nášlapná vrstva z ušlechtilého dřeva na stabilním nosiči. Rychlá pokládka, stabilní rozměr a ideální volba na podlahové topení.', 'materiál od 569 · pokládka plovoucí od 249, lepená od 269 Kč/m²'),
      ('Parkety a historické vzory', 'Vlysy, rybí kost, mozaika i vídeňské a benátské čtverce. Zkušenost z památek, jako je Apoštolská nunciatura.', 'pokládka parket od 399 Kč/m² · historické vzory individuálně'),
      ('Renovace parket', 'Broušení, tmelení spar, doplnění dílců a nový lak nebo olej. Stará podlaha pak vypadá jako nová.', 'od 600 Kč/m²'),
    ],
    calc=[('Vícevrstvá podlaha – plovoucí', 569, 249, 'Dřevěná vícevrstvá podlaha'), ('Vícevrstvá podlaha – lepená', 569, 269, 'Dřevěná vícevrstvá podlaha'),
          ('Masivní podlaha – lepená', None, 295, 'Dřevěná vícevrstvá podlaha'), ('Parkety', 569, 399, 'Parkety'), ('Renovace parket', 0, 600, 'Renovace parket')],
    refs=True,
    faq=[
      ('Kolik stojí dřevěná podlaha v Praze?', 'Materiál – vícevrstvé podlahy a parkety – začíná od 569 Kč/m². Pokládka vícevrstvé podlahy stojí od 249 Kč/m² (plovoucí) nebo od 269 Kč/m² (lepená), masiv lepíme od 295 Kč/m². Ceny jsou bez DPH, přesnou nabídku dostanete po bezplatném zaměření.'),
      ('Co zahrnuje zaměření zdarma?', 'Přijedeme do 48 hodin, přivezeme vzorky, změříme vlhkost podkladu a skutečné metry. Teprve pak počítáme cenu.'),
      ('Lze dát masivní dřevo na podlahové topení?', 'Ano, když víte jak. V praxi rozhoduje stabilní dřevina a vhodný poměr šíře a tloušťky prkna, změřená vlhkost a vytopený potěr podle protokolu a celoplošné lepení bez vzduchové mezery pro dobrý prostup tepla. Ve vile v Černošicích leží 245 m² masivního dubu na vodním podlahovém topení a funguje bez prasklin.'),
      COMMON_FAQ_TERMIN,
      ('Jezdíte i mimo Prahu?', 'Ano, pokládáme po celé Praze a ve Středočeském kraji. Showroom máme v Radotíně, takže jsme rychle třeba v Černošicích, Dobřichovicích, Řevnicích nebo na Berounsku.'),
      COMMON_FAQ_ZARUKA,
    ]),
 'parkety': dict(
    slug='parkety-praha', design='Parkety', crumb='Parkety Praha', form='Parkety',
    title='Parkety Praha – pokládka od 399 Kč/m², renovace od 600 Kč/m² | AR podlahy',
    desc='Pokládka, broušení a renovace parket v Praze a Středočeském kraji. Vlysy, rybí kost, mozaika i historické vzory. Pokládka od 399 Kč/m², renovace od 600 Kč/m², zaměření zdarma.',
    service='Pokládka a renovace parket', minprice=399,
    h1='Parkety v Praze – pokládka, broušení a renovace', sub='Klasické vlysy, rybí kost i mozaika. A staré parkety vrátíme do původní krásy.',
    bullets=['Zaměření zdarma do 48 hodin', 'Pokládka od 399 Kč/m², renovace od 600 Kč/m²', 'Záruka až 12 let na materiál, 24 měsíců na práci'],
    eyebrow='Co s parketami děláme', h2='Nové parkety i renovace starých',
    cards=[
      ('Pokládka parket', 'Vlysy, rybí kost (stromeček), řemen i mozaika. Celoplošně lepené na připravený podklad, pak broušení a lak nebo olej.', 'materiál od 569 · pokládka 399–429 Kč/m²'),
      ('Renovace a broušení parket', 'Broušení do čistého dřeva, tmelení spar a nový lak nebo olej. Vhodné pro parkety v činžácích i rodinných domech.', 'od 600 Kč/m²'),
      ('Oprava a doplnění', 'Výměna poškozených a doplnění chybějících vlysů, oprava míst po příčkách nebo kamnech, aby oprava nebyla vidět.', 'individuálně po zaměření'),
      ('Historické vzory', 'Vídeňské a benátské čtverce, kazetové parkety a intarzie. Rozebrání, doplnění a znovusložení původního vzoru.', 'individuálně'),
    ],
    calc=[('Pokládka parket', 569, 399, 'Parkety'), ('Renovace parket (broušení, tmel, lak/olej)', 0, 600, 'Renovace parket'), ('Historické vzory', None, None, 'Parkety')],
    refs=True,
    faq=[
      ('Kolik stojí renovace parket za m²?', 'Renovace – broušení, tmelení spar a nový lak nebo olej – stojí od 600 Kč/m² bez DPH. Doplnění chybějících vlysů a opravy naceníme po zaměření.'),
      ('Vyplatí se staré parkety renovovat?', 'Většinou ano. Masivní parkety mají silnou nášlapnou vrstvu, kterou lze brousit opakovaně. Při zaměření posoudíme stav, uchycení vlysů a vlhkost a řekneme, jestli je lepší renovace, nebo nová podlaha.'),
      ('Lak, nebo olej?', 'Lak vytvoří odolnou vrstvu a snadno se udržuje – hodí se do bytů s velkým provozem. Olej zachová přirozený vzhled dřeva a dá se opravovat lokálně. Poradíme podle provozu a toho, jak má podlaha vypadat.'),
      ('Kolik stojí pokládka nových parket?', 'Pokládka parket stojí 399–429 Kč/m² podle vzoru, materiál začíná od 569 Kč/m². Ceny jsou bez DPH.'),
      COMMON_FAQ_TERMIN,
      COMMON_FAQ_ZARUKA,
    ]),
 'vinyl': dict(
    slug='vinylove-podlahy-praha', design='Vinylove-podlahy', crumb='Vinylové podlahy Praha', form='Vinyl',
    title='Vinylové podlahy Praha – prodej a pokládka, od 482 Kč/m² | AR podlahy',
    desc='Vinylové podlahy v Praze a Středočeském kraji: lepený i zámkový vinyl včetně přípravy podkladu. Materiál od 482 Kč/m², stěrka od 250 Kč/m², zaměření zdarma do 48 hodin.',
    service='Prodej a pokládka vinylových podlah', minprice=482,
    h1='Vinylové podlahy v Praze – prodej a pokládka', sub='Lepený i zámkový vinyl do bytu, domu i kanceláře. Vhodný i na podlahové topení.',
    bullets=['Zaměření zdarma do 48 hodin', 'Vinylové dílce od 482 Kč/m²', 'Záruka až 12 let na materiál, 24 měsíců na práci'],
    eyebrow='Co pokládáme', h2='Vinyl, který vypadá jako dřevo a vydrží provoz',
    cards=[
      ('Lepený vinyl', 'Tenké dílce lepené celoplošně k podkladu. Stabilní, tichý a ideální na podlahové topení i velké plochy bez přechodových lišt.', 'materiál od 482 Kč/m²'),
      ('Zámkový (plovoucí) vinyl', 'Dílce se zacvaknou do sebe bez lepení. Rychlá montáž, vhodný i na renovace přes stávající rovnou podlahu.', 'materiál od 482 Kč/m²'),
      ('Příprava podkladu', 'Vinyl kopíruje každou nerovnost. Podklad proto vyrovnáme samonivelační stěrkou, aby se nic nepropsalo.', f'stěrka od {STERKA} Kč/m² (5 mm)'),
      ('Lišty a přechody', 'Soklové lišty v dekoru podlahy nebo bílé, přechodové a ukončovací profily u dveří.', f'od {LISTY} Kč/bm'),
    ],
    calc=[('Vinyl lepený', 482, None, 'Vinyl'), ('Vinyl zámkový (plovoucí)', 482, None, 'Vinyl')],
    refs=False,
    faq=[
      ('Kolik stojí vinylová podlaha s pokládkou?', f'Vinylové dílce začínají od 482 Kč/m², vyrovnání podkladu stěrkou stojí od {STERKA} Kč/m² při 5 mm a lišty od {LISTY} Kč/bm. Cenu pokládky upřesníme po zaměření podle podkladu. Ceny jsou bez DPH.'),
      ('Lepený, nebo zámkový vinyl?', 'Lepený vinyl je stabilnější, tišší a lépe vede teplo – je nejlepší volbou na podlahové topení a velké plochy. Zámkový se položí rychleji a dá se dát i přes stávající rovnou podlahu.'),
      ('Proč je tak důležitá příprava podkladu?', 'Špatně položená vinylová podlaha se většinou pozná podle podkladu – nerovnosti, praskliny a hrboly se časem propíšou. Proto podklad měříme a vyrovnáváme samonivelační stěrkou.'),
      ('Můžu si vinyl prohlédnout?', 'Ano, vzorky máte k dispozici v showroomu v Praze-Radotíně. Nebo vám je přivezeme na zaměření.'),
      COMMON_FAQ_TERMIN,
      COMMON_FAQ_ZARUKA,
    ]),
 'pvc': dict(
    slug='pvc-podlahy-praha', design='PVC-podlahy', crumb='PVC a lino Praha', form='Vinyl',
    title='PVC a lino Praha – prodej a pokládka, od 330 Kč/m² | AR podlahy',
    desc='PVC v rolích 2, 3 i 4 m pro byty, kuchyně i zátěžové prostory v Praze a Středočeském kraji. Materiál od 330 Kč/m², stěrka od 250 Kč/m², zaměření zdarma do 48 hodin.',
    service='Prodej a pokládka PVC', minprice=330,
    h1='PVC a lino v Praze – prodej a pokládka', sub='PVC v rolích 2, 3 i 4 m široké – do bytu, kuchyně, koupelny i do zátěžových prostor.',
    bullets=['Zaměření zdarma do 48 hodin', 'PVC v rolích od 330 Kč/m²', 'Záruka až 12 let na materiál, 24 měsíců na práci'],
    eyebrow='Co pokládáme', h2='Praktická podlaha za rozumnou cenu',
    cards=[
      ('Bytové PVC v rolích', 'Měkké a teplé na chůzi, tlumí kroky a snadno se uklízí. Role 2, 3 i 4 m široké znamenají méně spojů.', 'materiál od 330 Kč/m²'),
      ('Zátěžové PVC', 'Do kanceláří, obchodů, škol a chodeb. Odolná nášlapná vrstva pro velký provoz.', 'individuálně po zaměření'),
      ('Příprava podkladu', 'PVC kopíruje podklad. Nerovnosti vyrovnáme samonivelační stěrkou, aby podlaha byla hladká.', f'stěrka od {STERKA} Kč/m² (5 mm)'),
      ('Lišty a zakončení', 'Soklové lišty a přechodové profily, v koupelnách a kuchyních s vytaženým soklem.', f'od {LISTY} Kč/bm'),
    ],
    calc=[('PVC v roli – bytové', 330, None, 'Vinyl'), ('PVC zátěžové', None, None, 'Vinyl')],
    refs=False,
    faq=[
      ('Kolik stojí PVC s pokládkou?', f'PVC v rolích začíná od 330 Kč/m². Vyrovnání podkladu stěrkou stojí od {STERKA} Kč/m² při 5 mm a lišty od {LISTY} Kč/bm. Pokládku naceníme po zaměření. Ceny jsou bez DPH.'),
      ('Jaký je rozdíl mezi PVC a linem?', 'Lidově se „linem“ říká PVC v rolích. Přírodní linoleum je jiný materiál vyrobený z lněného oleje. Poradíme, co se hodí do vašeho prostoru.'),
      ('Lepit, nebo položit volně?', 'Do menších místností lze PVC položit volně nebo fixovat páskou. V kuchyni, chodbě a všude s větším provozem doporučujeme celoplošné lepení – podlaha se nevlní a vydrží déle.'),
      ('Jak široké role máte?', 'PVC dodáváme v šířích 2, 3 i 4 m, takže většinu místností pokryjeme bez spoje.'),
      COMMON_FAQ_TERMIN,
      COMMON_FAQ_ZARUKA,
    ]),
 'koberce': dict(
    slug='koberce-praha', design='Koberce', crumb='Koberce Praha', form='Koberec',
    title='Koberce Praha – prodej a pokládka, od 154 Kč/m² | AR podlahy',
    desc='Metrážové a zátěžové koberce v rolích i čtvercích pro byty a kanceláře v Praze a Středočeském kraji. Koberce od 154 Kč/m², zaměření zdarma do 48 hodin.',
    service='Prodej a pokládka koberců', minprice=154,
    h1='Koberce v Praze – prodej a pokládka', sub='Metrážové koberce do bytu i zátěžové koberce a čtverce do kanceláří.',
    bullets=['Zaměření zdarma do 48 hodin', 'Koberce od 154 Kč/m²', 'Záruka až 12 let na materiál, 24 měsíců na práci'],
    eyebrow='Co pokládáme', h2='Teplo a ticho pod nohama',
    cards=[
      ('Bytové metrážové koberce', 'Do ložnic, dětských pokojů i obýváků. Teplé, tlumí hluk a kroky, široký výběr barev a struktur.', 'od 154 Kč/m²'),
      ('Zátěžové koberce a čtverce', 'Do kanceláří, hotelů a společných prostor. Kobercové čtverce se snadno vymění po kusech.', 'individuálně po zaměření'),
      ('Příprava podkladu', 'Koberec potřebuje rovný a suchý podklad. Nerovnosti vyrovnáme samonivelační stěrkou.', f'stěrka od {STERKA} Kč/m² (5 mm)'),
      ('Lišty a zakončení', 'Soklové lišty, přechody ke dveřím a zakončení hran, aby se koberec nezvedal.', f'od {LISTY} Kč/bm'),
    ],
    calc=[('Koberec bytový (metráž)', 154, None, 'Koberec'), ('Koberec zátěžový / čtverce', None, None, 'Koberec')],
    refs=False,
    faq=[
      ('Kolik stojí koberec s pokládkou?', f'Koberce začínají od 154 Kč/m². Vyrovnání podkladu stojí od {STERKA} Kč/m² při 5 mm a lišty od {LISTY} Kč/bm. Pokládku naceníme po zaměření. Ceny jsou bez DPH.'),
      ('Role, nebo čtverce?', 'Metrážový koberec z role je ideální do bytu – je bez spojů a příjemný. Kobercové čtverce se hodí do kanceláří, protože se poškozený kus dá snadno vyměnit.'),
      ('Lepí se koberec, nebo jen pokládá?', 'Záleží na prostoru. V bytě koberec často fixujeme páskou, zátěžové koberce v kancelářích lepíme celoplošně, aby se nevlnily a vydržely provoz.'),
      ('Můžu si koberce prohlédnout?', 'Ano, vzorky máme v showroomu v Praze-Radotíně. Nebo vám je přivezeme na zaměření.'),
      COMMON_FAQ_TERMIN,
      COMMON_FAQ_ZARUKA,
    ]),
}
ORDER = ['drevo', 'parkety', 'vinyl', 'pvc', 'koberce']

def li(t):
    return f'<li style="display: flex; gap: 10px; align-items: center;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#c9a46a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5 9-10"></path></svg>{t}</li>'

def hero(c, L):
    return f'''<div style="max-width: 1240px; margin: 0 auto; padding: clamp(36px, 5vw, 64px) 24px clamp(40px, 5vw, 64px); display: flex; flex-direction: column; gap: 20px; align-items: flex-start;">
<nav aria-label="Drobečková navigace" style="font-size: 13px; color: rgba(255,255,255,.65);"><a href="{L["home"]}" style="color: rgba(255,255,255,.8);">Úvod</a> <span aria-hidden="true">/</span> <span aria-current="page">{c["crumb"]}</span></nav>
<h1 style="margin: 0; font-size: clamp(34px, 4.8vw, 64px); line-height: 1.06; font-weight: 900; letter-spacing: -.02em; max-width: 900px;">{c["h1"]}</h1>
<p style="margin: 0; font-size: clamp(17px, 1.5vw, 21px); line-height: 1.5; color: rgba(255,255,255,.88); max-width: 700px; font-weight: 600;">{c["sub"]}</p>
<ul style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 16px; color: rgba(255,255,255,.88);">{"".join(li(b) for b in c["bullets"])}</ul>
<div style="display: flex; flex-wrap: wrap; gap: 14px; margin-top: 6px;"><a href="#poptavka" style="background: {{{{accent}}}}; color: #fff; text-decoration: none; padding: 18px 28px; border-radius: 8px; font-weight: 800; font-size: 16px;">Chci nabídku</a><a href="tel:+420605257236" style="border: 1px solid rgba(255,255,255,.45); color: #fff; text-decoration: none; padding: 18px 28px; border-radius: 8px; font-weight: 700; font-size: 16px;">Zavolat +420 605 257 236</a></div>
</div>
<div style="border-top: 1px solid rgba(255,255,255,.12); background: rgba(10,10,10,.55);">
<div style="max-width: 1240px; margin: 0 auto; padding: 22px 24px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; text-align: center;">
<div><div style="font-size: clamp(22px, 2.4vw, 32px); font-weight: 900; color: #c9a46a; line-height: 1;">1991</div><div style="font-size: 13px; color: rgba(255,255,255,.72); margin-top: 6px;">na trhu od roku</div></div>
<div><div style="font-size: clamp(22px, 2.4vw, 32px); font-weight: 900; color: #c9a46a; line-height: 1;">13</div><div style="font-size: 13px; color: rgba(255,255,255,.72); margin-top: 6px;">lidí v týmu</div></div>
<div><div style="font-size: clamp(22px, 2.4vw, 32px); font-weight: 900; color: #c9a46a; line-height: 1;">48 h</div><div style="font-size: 13px; color: rgba(255,255,255,.72); margin-top: 6px;">do zaměření</div></div>
</div>
</div>
'''

def cards_section(c):
    cards = ''.join(f'<div style="{CARD}"><strong style="font-size: 19px;">{t}</strong><p style="margin: 0; font-size: 15px; line-height: 1.65; color: #4a443b;">{d}</p><span style="margin-top: auto; padding-top: 6px; font-size: 14px; font-weight: 800; color: #8a6a3f;">{p}</span></div>' for t, d, p in c['cards'])
    return f'''<!-- CO POKLÁDÁME -->
<section style="{WRAP} display: flex; flex-direction: column; gap: 28px;">
<div style="max-width: 760px; display: flex; flex-direction: column; gap: 12px;"><span style="{EYE}">{c["eyebrow"]}</span><h2 style="{H2}">{c["h2"]}</h2></div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">{cards}</div>
<p style="margin: 0; font-size: 13px; color: #6b655b;">{c.get('note', NOTE + ' Materiál se počítá včetně prořezu, pokládka z čisté plochy.')}</p>
</section>

'''

def calc_section(c):
    opts = ''.join(f'<option value="{i}" data-mat="{m if m is not None else ""}" data-lab="{l if l is not None else ""}" data-form="{f}">{t}</option>' for i, (t, m, l, f) in enumerate(c['calc']))
    INP = 'border: 1px solid #d6cdbf; border-radius: 8px; padding: 14px; font-size: 16px; background: #fff; width: 100%; box-sizing: border-box;'
    LB = 'display: flex; flex-direction: column; gap: 8px; font-size: 14px; font-weight: 700;'
    ROW = 'display: flex; justify-content: space-between; gap: 12px; font-size: 15px;'
    t, m, l, f = c['calc'][0]
    q = 54
    mat = f'{q * m:,}'.replace(',', ' ') + ' Kč' if m else ('–' if m == 0 else 'po zaměření')
    lab = f'{50 * l:,}'.replace(',', ' ') + ' Kč' if l else 'po zaměření'
    tot = (q * (m or 0)) + (50 * (l or 0))
    tot_s = (('' if (m is not None and l) else 'od ') + f'{tot:,}'.replace(',', ' ') + ' Kč') if tot else 'po zaměření'
    return f'''<!-- KALKULAČKA -->
<section id="kalkulacka" style="background: #1a1a1a; color: #fff;">
<div style="{WRAP} display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px 64px; align-items: center;">
<div style="display: flex; flex-direction: column; gap: 14px;">
<span style="font-size: 13px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; color: #c9a46a;">Kalkulačka</span>
<h2 style="margin: 0; font-size: clamp(30px, 3.4vw, 46px); line-height: 1.1; font-weight: 900;">Spočítejte si orientační cenu</h2>
<p style="margin: 0; font-size: 17px; line-height: 1.7; color: rgba(255,255,255,.78);">Vyberte druh podlahy a zadejte plochu. Pevnou cenu dostanete po bezplatném zaměření. {NOTE}</p>
</div>
<form id="calc" onsubmit="return false" style="background: #fff; color: #1a1a1a; border-radius: 18px; padding: clamp(22px, 3vw, 34px); display: flex; flex-direction: column; gap: 16px;">
<label style="{LB}">Druh podlahy<select id="calc-typ" style="{INP}">{opts}</select></label>
<label style="{LB}">Čistá plocha v m²<input id="calc-m2" type="number" min="1" step="1" value="50" inputmode="numeric" style="{INP}"></label>
<label style="display: flex; gap: 10px; align-items: center; font-size: 15px; font-weight: 600;"><input id="calc-sterka" type="checkbox" style="width: 20px; height: 20px; accent-color: #8a6a3f;">Vyrovnat podklad stěrkou (od {STERKA} Kč/m², 5 mm)</label>
<div style="background: #f5f1ea; border-radius: 12px; padding: 18px 20px; display: flex; flex-direction: column; gap: 8px;">
<div style="{ROW}"><span>Materiál <small id="calc-mat-d" style="color: #6b655b;">(54 m² s prořezem 8 %)</small></span><strong id="calc-mat">{mat}</strong></div>
<div style="{ROW}"><span>Pokládka <small id="calc-lab-d" style="color: #6b655b;">(50 m²)</small></span><strong id="calc-lab">{lab}</strong></div>
<div id="calc-st-row" style="{ROW} display: none;"><span>Stěrka <small id="calc-st-d" style="color: #6b655b;"></small></span><strong id="calc-st">–</strong></div>
<div style="{ROW} border-top: 1px solid #e0d6c6; padding-top: 10px; font-size: 18px;"><span style="font-weight: 800;">Celkem orientačně</span><strong id="calc-total" style="font-size: 22px; font-weight: 900;">{tot_s}</strong></div>
<small style="color: #6b655b; font-size: 12px;">{NOTE} Lišty (od {LISTY} Kč/bm) a dopravu upřesníme po zaměření.</small>
</div>
<a id="calc-cta" href="#poptavka" style="background: #8a6a3f; color: #fff; text-align: center; text-decoration: none; padding: 16px; border-radius: 8px; font-weight: 800; font-size: 16px;">Chci přesnou nabídku</a>
</form>
</div>
</section>

'''

def refs_section(src, c):
    line = '<p style="margin: 0; font-size: 17px; line-height: 1.6; color: #3d3830; font-weight: 600;">Pracovali jsme také pro Úřad vlády, Kramářovu vilu, Pražský hrad a ministerstva.</p>'
    if not c['refs']:
        return f'''<!-- REFERENCE -->
<section style="max-width: 1240px; margin: 0 auto; padding: 0 24px clamp(48px, 6vw, 72px);">
<div style="border-left: 3px solid #c9a46a; padding: 6px 0 6px 20px; display: flex; flex-direction: column; gap: 8px;"><span style="{EYE}">Od roku 1991</span><p style="margin: 0; font-size: 17px; line-height: 1.6; color: #3d3830; font-weight: 600;">Podlahy pokládáme v bytech, domech, kancelářích i v objektech, jako je Úřad vlády, Kramářova vila nebo Pražský hrad.</p></div>
</section>

'''
    st = sec(src, 'PŘÍPADOVÉ STUDIE', 'GARANCE')
    st = re.sub(r'<a href="#" style="color: #1a1a1a; font-weight: 800; font-size: 15px;">Celá případová studie →</a>', '', st)
    i = st.rindex('</section>')
    return st[:i] + line + '\n' + st[i:]

def promise_section():
    pts = [('Záruka až 12 let', 'na materiál, 24 měsíců na práci'), ('Montáž do 7 dní', 'u 100 m² včetně úpravy podkladu'),
           ('Zaměření zdarma', 'do 48 hodin, se vzorky u vás'), ('Sada na údržbu', 'zdarma u zakázek nad 100 m²')]
    cards = ''.join(f'<div style="background: #fff; border-radius: 14px; padding: 24px; display: flex; flex-direction: column; gap: 8px;">{I_CHECK}<div style="font-size: 22px; font-weight: 900;">{a}</div><div style="font-size: 15px; line-height: 1.55; color: #5b554c;">{b}</div></div>' for a, b in pts)
    return f'''<!-- SLIBUJEME -->
<section style="background: #ece5d8;">
<div style="{WRAP} display: flex; flex-direction: column; gap: 24px;">
<div style="display: flex; flex-direction: column; gap: 12px;"><span style="{EYE}">Co vám slíbíme</span><h2 style="{H2}">Na čem se můžete spolehnout</h2></div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px;">{cards}</div>
<p style="{P}">Pokládáme v celé Praze a ve Středočeském kraji – z Radotína jsme rychle třeba v Černošicích, Dobřichovicích, Řevnicích nebo na Berounsku.</p>
</div>
</section>

'''

def faq_section(c):
    faq = ''.join(f'<details style="border-bottom: 1px solid #e4ddd2; padding: 16px 0;"><summary style="display: flex; justify-content: space-between; gap: 20px; align-items: center; font-size: 17px; font-weight: 700; min-height: 44px; cursor: pointer;">{q}<span class="plus" style="font-size: 26px; color: #8a6a3f; font-weight: 400;">+</span></summary><p style="margin: 10px 0 0; font-size: 16px; line-height: 1.7; color: #5b554c;">{a}</p></details>' for q, a in c['faq'])
    return f'''<!-- FAQ -->
<section style="background: #fff; border-top: 1px solid #e4ddd2;">
<div style="max-width: 1240px; margin: 0 auto; padding: clamp(48px, 6vw, 80px) 24px; display: flex; flex-direction: column; gap: 14px;">
<span style="{EYE}">Časté dotazy</span>
<h2 style="{H2} margin-bottom: 6px;">Na co se ptáte</h2>
{faq}
</div>
</section>

'''

def form_section(c, kind):
    Lb = 'display: flex; flex-direction: column; gap: 8px; font-size: 14px; font-weight: 700;'
    I = 'border: 1px solid #d6cdbf; border-radius: 8px; padding: 14px; font-size: 16px;'
    what = c.get('what') or {'drevo': 'dřevěnou podlahu', 'parkety': 'parkety', 'vinyl': 'vinylovou podlahu', 'pvc': 'PVC', 'koberce': 'koberec'}[kind]
    return f'''<!-- POPTÁVKA -->
<section id="poptavka" class="hero" style="color: #fff;">
<div style="max-width: 1240px; margin: 0 auto; padding: clamp(48px, 6vw, 80px) 24px; display: flex; flex-wrap: wrap; gap: 40px; align-items: flex-start;">
<div style="flex: 1 1 340px; display: flex; flex-direction: column; gap: 16px; min-width: 0;">
<span style="font-size: 13px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; color: #c9a46a;">Zaměření zdarma do 48 hodin</span>
<h2 style="margin: 0; font-size: clamp(30px, 3.4vw, 48px); line-height: 1.08; font-weight: 900;">Chci nabídku na {what}</h2>
<p style="margin: 0; font-size: 17px; line-height: 1.65; color: rgba(255,255,255,.8);">Stačí jméno a telefon. Zavoláme vám, doptáme se na detaily a domluvíme zaměření.</p>
<a href="tel:+420605257236" style="color: #fff; font-weight: 800; font-size: 22px; text-decoration: none;">+420 605 257 236</a>
</div>
<form id="poptavka-form" method="post" action="" style="flex: 999 1 480px; background: #fff; color: #1a1a1a; border-radius: 18px; padding: clamp(22px, 3vw, 36px); display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; box-sizing: border-box; min-width: 0;">
<label style="{Lb}">Jméno a příjmení *<input type="text" name="jmeno" autocomplete="name" required style="{I}"></label>
<label style="{Lb}">Telefon *<input type="tel" name="telefon" autocomplete="tel" required style="{I}"></label>
<label style="{Lb}">E-mail<input type="email" name="email" autocomplete="email" style="{I}"></label>
<label style="{Lb}">Lokalita<input type="text" name="lokalita" placeholder="např. Praha 5" style="{I}"></label>
<label style="{Lb} grid-column: 1 / -1;">Zpráva (nepovinné)<textarea name="zprava" rows="3" style="{I} resize: vertical;"></textarea></label>
<input type="hidden" name="typ" value="{c["form"]}"><input type="hidden" name="plocha" value=""><input type="hidden" name="zdroj" value="landing-{c["slug"]}">
<button type="submit" style="grid-column: 1 / -1; background: {{{{accent}}}}; color: #fff; border: 0; border-radius: 8px; padding: 17px; font-size: 17px; font-weight: 800; cursor: pointer;">Odeslat – ozveme se do 48 hodin</button>
<p id="poptavka-stav" role="status" style="grid-column: 1 / -1; margin: 0; font-size: 13px; line-height: 1.5; color: #6b655b;">Odesláním souhlasíte se zpracováním osobních údajů za účelem vyřízení poptávky. <a href="#" style="color: #8a6a3f;">Zásady ochrany osobních údajů</a></p>
</form>
</div>
</section>

<!-- MOBILNÍ LIŠTA -->
<div class="mbar" style="display: none; position: fixed; left: 0; right: 0; bottom: 0; z-index: 40; background: #0e0e0e; padding: 10px 12px calc(10px + env(safe-area-inset-bottom)); gap: 10px; box-shadow: 0 -6px 20px rgba(0,0,0,.25);"><a href="tel:+420605257236" style="flex: 1; text-align: center; border: 1px solid rgba(255,255,255,.4); color: #fff; text-decoration: none; padding: 14px; border-radius: 8px; font-weight: 800;">Zavolat</a><a href="#poptavka" style="flex: 1; text-align: center; background: #8a6a3f; color: #fff; text-decoration: none; padding: 14px; border-radius: 8px; font-weight: 800;">Nabídka</a></div>

'''

MBAR_CSS = '@media (max-width:700px){.mbar{display:flex !important}body{padding-bottom:72px}}'

FORM_ENDPOINT = ''  # doplnit služby pro odesílání formuláře; prázdné = otevře e-mail
JS = """<script>
(function(){
var t=document.getElementById('calc-typ'),m=document.getElementById('calc-m2'),s=document.getElementById('calc-sterka'),ST=%d;
function f(n){return Math.round(n).toLocaleString('cs-CZ')+' Kč'}
function g(id){return document.getElementById(id)}
function u(){if(!t)return;var o=t.options[t.selectedIndex],a=Math.max(0,parseFloat(m.value)||0),ms=o.getAttribute('data-mat'),ls=o.getAttribute('data-lab'),mat=+ms||0,lab=+ls||0,q=Math.ceil(a*1.08),exact=true;
if(ms==='0'){g('calc-mat').textContent='–';g('calc-mat-d').textContent='(bez materiálu)'}else if(mat){g('calc-mat').textContent=f(q*mat);g('calc-mat-d').textContent='('+q+' m² s prořezem 8 %%)'}else{g('calc-mat').textContent='po zaměření';g('calc-mat-d').textContent='';exact=false}
g('calc-lab-d').textContent='('+a+' m²)';if(lab){g('calc-lab').textContent=f(a*lab)}else{g('calc-lab').textContent='po zaměření';exact=false}
var st=s&&s.checked?a*ST:0;g('calc-st-row').style.display=st?'flex':'none';g('calc-st').textContent=f(st);g('calc-st-d').textContent='('+a+' m²)';
var sum=(ms==='0'?0:q*mat)+a*lab+st;g('calc-total').textContent=sum?(exact?'':'od ')+f(sum):'po zaměření'}
if(t){[t,m,s].forEach(function(e){if(e){e.addEventListener('input',u);e.addEventListener('change',u)}});u();
g('calc-cta').addEventListener('click',function(){var F=g('poptavka-form');F.typ.value=t.options[t.selectedIndex].text;F.plocha.value=m.value+' m²'+(s&&s.checked?' + stěrka':'')})}
var F=g('poptavka-form'),S=g('poptavka-stav'),EP='__EP__';
if(F)F.addEventListener('submit',function(e){e.preventDefault();var d=new FormData(F);
if(EP){fetch(EP,{method:'POST',body:d,headers:{'Accept':'application/json'}}).then(function(r){if(!r.ok)throw 0;F.reset();S.textContent='Děkujeme, ozveme se do 48 hodin.'}).catch(function(){S.textContent='Odeslání se nepovedlo, zavolejte nám prosím na +420 605 257 236.'});return}
var b=[];d.forEach(function(v,k){if(v)b.push(k+': '+v)});location.href='mailto:info@ar-podlahy.cz?subject='+encodeURIComponent('Poptávka – '+(F.typ.value||'podlaha'))+'&body='+encodeURIComponent(b.join('\\n'))});
})();
</script>""".replace('__EP__', FORM_ENDPOINT) % STERKA

PHOTOS = {
 'drevo': [('drevo-tmave.jpg','Tmavá dřevěná podlaha v obývacím pokoji'),('drevo-sklo.jpg','Dřevěná podlaha s prosklenou částí'),('parkety-rybi-kost-2.jpg','Parkety v kladu rybí kost')],
 'parkety': [('parkety-rybi-kost-1.jpg','Parkety rybí kost po pokládce'),('parkety-rybi-kost-2.jpg','Lakované parkety rybí kost'),('parkety-mozaika.jpg','Mozaikové parkety')],
 'historicke': [('historicka-1.jpg','Obnovená historická parketová podlaha'),('historicka-2.jpg','Reprezentativní interiér s historickými parketami'),('parkety-mozaika.jpg','Mozaikový vzor parket')],
 'pvc': [('pvc-1.jpg','Celoplošně lepené PVC'),('pvc-vzor.jpg','PVC v chodbě'),('schody-pvc.jpg','PVC na schodech')],
 'koberce': [('koberec-1.jpg','Zátěžový koberec v kanceláři'),('koberec-pokladka.jpg','Pokládka koberce'),('koberec-sal.jpg','Koberec v konferenčním sále')],
 'terasy': [('terasa-1.jpg','Dřevěná terasa'),('terasa-2.jpg','Terasa z prken')],
 'podklad': [('podklad-sterka-1.jpg','Vyrovnání podkladu stěrkou'),('podklad-sterka-2.jpg','Příprava podkladu před pokládkou')],
 'rekonstrukce': [('kavarna-1.jpg','Rekonstrukce kavárny'),('kavarna-2.jpg','Interiér kavárny po rekonstrukci'),('kavarna-3.jpg','Kavárna – dřevěné obklady a podlaha')],
}
def photos_section(kind):
    ph = PHOTOS.get(kind)
    if not ph: return ''
    items = ''.join(f'<figure style="margin: 0; display: flex; flex-direction: column; gap: 8px;"><img src="REALIMG/{f}" alt="{a}" loading="lazy" style="width: 100%; aspect-ratio: 4 / 3; object-fit: cover; border-radius: 14px; display: block;"><figcaption style="font-size: 14px; color: #5b554c;">{a}</figcaption></figure>' for f, a in ph)
    return f'''<!-- REALIZACE -->
<style>@media (max-width: 640px) {{ .photogrid {{ display: flex !important; overflow-x: auto; scroll-snap-type: x mandatory; margin: 0 -24px; padding: 0 24px; }} .photogrid figure {{ flex: 0 0 78%; scroll-snap-align: start; }} }}</style>
<section style="max-width: 1240px; margin: 0 auto; padding: 0 24px clamp(48px, 6vw, 72px); display: flex; flex-direction: column; gap: 20px;">
<span style="{EYE}">Z našich realizací</span>
<div class="refgrid photogrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px;">{items}</div>
</section>

'''

def build(kind, src, L):
    c = CONF[kind]
    body = cards_section(c) + photos_section(kind) + (calc_section(c) if c.get('calc') else '') + refs_section(src, c) + promise_section() + faq_section(c) + form_section(c, kind)
    return hero(c, L), body

import landing_more  # registers further pages into CONF
