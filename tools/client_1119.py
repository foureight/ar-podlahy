# Doplnění podle Google Docu klienta „AR podlahy – co doplnit a opravit“ (vyplněno 19. 11. 2026).
# Ceny bez DPH. Na podstránkách se ve viditelném textu nepíše „v Praze“ (přání klienta).
import re
from landing import CONF, COMMON_FAQ_ZARUKA, COMMON_FAQ_TERMIN, STERKA, LISTY

IND = 'individuálně po zaměření'
VZORKY = ('Můžu si materiál prohlédnout?', 'Ano, vzorky máte k dispozici ve vzorkovně v Praze-Radotíně. Nebo vám je přivezeme na zaměření.')
B3 = lambda price: ['Zaměření zdarma do 48 hodin', price, 'Záruka až 12 let na materiál, 24 měsíců na práci']
PODKLAD_CARD = ('Příprava podkladu', 'Podklad změříme a nerovnosti vyrovnáme samonivelační stěrkou, aby se nic nepropsalo do nové podlahy.', f'stěrka od {STERKA} Kč/m² (5 mm)')
LISTY_CARD = ('Lišty a přechody', 'Soklové lišty v dekoru podlahy nebo bílé, přechodové a ukončovací profily u dveří.', f'od {LISTY} Kč/bm')

U = {}

U['drevo'] = dict(
    title='Dřevěné podlahy Praha – od 933 Kč/m², pokládka od 249 Kč/m² | AR podlahy',
    desc='Pokládka masivních a vícevrstvých dřevěných podlah v Praze a Středočeském kraji. Vícevrstvá podlaha od 933 Kč/m², masiv od 1 595 Kč/m², pokládka od 249 Kč/m². Zaměření zdarma do 48 hodin.',
    minprice=249,
    h1='Dřevěné podlahy – masiv i vícevrstvé', sub='Masivní a vícevrstvé dřevěné podlahy do bytu, domu i kanceláře, které vydrží generace.',
    bullets=B3('Vícevrstvá od 933 Kč/m², pokládka od 249 Kč/m²'),
    h2='Dřevěná podlaha pro byt, dům i kancelář',
    cards=[
      ('Masivní dřevěné podlahy', 'Poctivá prkna z masivu, nejčastěji dub. Celoplošně lepená vydrží generace, zvládnou i podlahové topení a dají se opakovaně brousit.', 'materiál od 1 595 · pokládka lepená od 295 Kč/m²'),
      ('Vícevrstvé (třívrstvé) podlahy', 'Nášlapná vrstva z ušlechtilého dřeva na stabilním nosiči. Rychlá pokládka, stabilní rozměr a ideální volba na podlahové topení.', 'materiál od 933 · pokládka plovoucí od 249, lepená od 269 Kč/m²'),
      PODKLAD_CARD, LISTY_CARD,
    ],
    calc=[('Vícevrstvá podlaha – plovoucí', 933, 249, 'Dřevěná vícevrstvá podlaha'), ('Vícevrstvá podlaha – lepená', 933, 269, 'Dřevěná vícevrstvá podlaha'),
          ('Masivní podlaha – lepená', 1595, 295, 'Dřevěná vícevrstvá podlaha')],
    faq=[
      ('Kolik stojí dřevěná podlaha?', 'Vícevrstvá dřevěná podlaha začíná od 933 Kč/m², masivní od 1 595 Kč/m². Pokládka vícevrstvé podlahy stojí od 249 Kč/m² (plovoucí) nebo od 269 Kč/m² (lepená), masiv lepíme od 295 Kč/m². Ceny jsou bez DPH, přesnou nabídku dostanete po bezplatném zaměření.'),
      ('Masiv, nebo vícevrstvá podlaha?', 'Masiv je jedno poctivé prkno, které lze mnohokrát přebrousit. Vícevrstvá podlaha má nášlapnou vrstvu z ušlechtilého dřeva na stabilním nosiči, méně pracuje a je ideální na podlahové topení. Poradíme podle místnosti a vytápění.'),
      ('Co zahrnuje zaměření zdarma?', 'Přijedeme do 48 hodin, přivezeme vzorky, změříme vlhkost podkladu a skutečné metry. Teprve pak počítáme cenu.'),
      ('Lze dát masivní dřevo na podlahové topení?', 'Ano, když víte jak. V praxi rozhoduje stabilní dřevina a vhodný poměr šíře a tloušťky prkna, změřená vlhkost a vytopený potěr podle protokolu a celoplošné lepení bez vzduchové mezery pro dobrý prostup tepla. Ve vile v Černošicích leží 245 m² masivního dubu na vodním podlahovém topení a funguje bez prasklin.'),
      COMMON_FAQ_TERMIN,
      ('Jezdíte i mimo Prahu?', 'Ano, pokládáme po celé Praze a ve Středočeském kraji. Vzorkovnu máme v Radotíně, takže jsme rychle třeba v Černošicích, Dobřichovicích, Řevnicích nebo na Berounsku.'),
      COMMON_FAQ_ZARUKA,
    ])

U['parkety'] = dict(
    title='Parkety Praha – materiál od 585 Kč/m², renovace od 600 Kč/m² | AR podlahy',
    desc='Pokládka, broušení a renovace parket v Praze a Středočeském kraji. Vlysy, rybí kost, mozaika i historické vzory. Parkety od 585 Kč/m², pokládka od 399 Kč/m², renovace od 600 Kč/m².',
    h1='Parkety – pokládka, broušení a renovace',
    bullets=B3('Parkety od 585 Kč/m², renovace od 600 Kč/m²'),
    cards=[
      ('Pokládka parket', 'Vlysy, rybí kost (stromeček), řemen i mozaika. Celoplošně lepené na připravený podklad, pak broušení a lak nebo olej.', 'materiál od 585 · pokládka 399–429 Kč/m²'),
      ('Renovace a broušení parket', 'Broušení do čistého dřeva, tmelení spar a nový lak nebo olej. Vhodné pro parkety v činžácích i rodinných domech.', 'od 600 Kč/m²'),
      ('Oprava a doplnění', 'Výměna poškozených a doplnění chybějících vlysů, oprava míst po příčkách nebo kamnech, aby oprava nebyla vidět.', IND),
      ('Historické vzory', 'Vídeňské a benátské čtverce, kazetové parkety a intarzie. Rozebrání, doplnění a znovusložení původního vzoru.', 'individuálně'),
    ],
    calc=[('Pokládka parket', 585, 399, 'Parkety'), ('Renovace parket (broušení, tmel, lak/olej)', 0, 600, 'Renovace parket'), ('Historické vzory', None, None, 'Parkety')],
    faq=[
      ('Kolik stojí renovace parket za m²?', 'Renovace – broušení, tmelení spar a nový lak nebo olej – stojí od 600 Kč/m² bez DPH. Doplnění chybějících vlysů a opravy naceníme po zaměření.'),
      ('Vyplatí se staré parkety renovovat?', 'Renovace starých parket se vyplatí. Získáte podlahu jako novou za zlomek ceny masivního dřeva a zároveň si v bytě udržíte poctivý přírodní materiál, který vydrží desítky let. Při zaměření posoudíme stav a uchycení vlysů.'),
      ('Lak, nebo olej?', 'Lak vytvoří odolnou vrstvu a snadno se udržuje – hodí se do bytů s velkým provozem. Olej zachová přirozený vzhled dřeva a dá se opravovat lokálně. Poradíme podle provozu a toho, jak má podlaha vypadat.'),
      ('Kolik stojí nové parkety?', 'Parkety začínají od 585 Kč/m², pokládka stojí 399–429 Kč/m² podle vzoru. Ceny jsou bez DPH.'),
      COMMON_FAQ_TERMIN, COMMON_FAQ_ZARUKA,
    ])

U['vinyl'] = dict(
    title='Vinylové podlahy Praha – od 410 Kč/m², pokládka od 180 Kč/m² | AR podlahy',
    desc='Lepený i zámkový vinyl v Praze a Středočeském kraji včetně přípravy podkladu. Lepený vinyl od 410 Kč/m², zámkový od 799 Kč/m², pokládka od 180 Kč/m². Zaměření zdarma do 48 hodin.',
    minprice=410,
    h1='Vinylové podlahy – prodej a pokládka',
    bullets=B3('Vinyl od 410 Kč/m², pokládka od 180 Kč/m²'),
    cards=[
      ('Lepený vinyl', 'Tenké dílce lepené celoplošně k podkladu. Stabilní, tichý a ideální na podlahové topení i velké plochy bez přechodových lišt.', 'materiál od 410 · pokládka 230 Kč/m²'),
      ('Zámkový (plovoucí) vinyl', 'Dílce se zacvaknou do sebe bez lepení. Rychlá montáž, vhodný i na renovace přes stávající rovnou podlahu.', 'materiál od 799 · pokládka 180 Kč/m²'),
      PODKLAD_CARD, LISTY_CARD,
    ],
    calc=[('Vinyl lepený', 410, 230, 'Vinyl'), ('Vinyl zámkový (plovoucí)', 799, 180, 'Vinyl')],
    faq=[
      ('Kolik stojí vinylová podlaha s pokládkou?', f'Lepený vinyl začíná od 410 Kč/m² a pokládka stojí 230 Kč/m². Zámkový vinyl začíná od 799 Kč/m², pokládka 180 Kč/m². Vyrovnání podkladu stěrkou stojí od {STERKA} Kč/m² při 5 mm a lišty od {LISTY} Kč/bm. Ceny jsou bez DPH.'),
      ('Lepený, nebo zámkový vinyl?', 'Lepený vinyl je stabilnější, tišší a lépe vede teplo – je nejlepší volbou na podlahové topení a velké plochy. Zámkový se položí rychleji a dá se dát i přes stávající rovnou podlahu.'),
      ('Proč je tak důležitá příprava podkladu?', 'Špatně položená vinylová podlaha se většinou pozná podle podkladu – nerovnosti, praskliny a hrboly se časem propíšou. Proto podklad měříme a vyrovnáváme samonivelační stěrkou.'),
      ('Můžu si vinyl prohlédnout?', 'Ano, vzorky máte k dispozici ve vzorkovně v Praze-Radotíně. Nebo vám je přivezeme na zaměření.'),
      COMMON_FAQ_TERMIN, COMMON_FAQ_ZARUKA,
    ])

U['pvc'] = dict(
    title='PVC a lino Praha – od 330 Kč/m², pokládka od 150 Kč/m² | AR podlahy',
    desc='PVC v rolích 2, 3 i 4 m pro byty, kuchyně i zátěžové prostory v Praze a Středočeském kraji. Materiál od 330 Kč/m², pokládka od 150 Kč/m², zaměření zdarma do 48 hodin.',
    h1='PVC a lino – prodej a pokládka',
    bullets=B3('PVC od 330 Kč/m², pokládka od 150 Kč/m²'),
    cards=[
      ('Bytové PVC v rolích', 'Měkké a teplé na chůzi, tlumí kroky a snadno se uklízí. Role 2, 3 i 4 m široké znamenají méně spojů.', 'materiál od 330 · pokládka od 150 Kč/m²'),
      ('Zátěžové PVC', 'Do kanceláří, obchodů, škol a chodeb. Odolná nášlapná vrstva pro velký provoz.', 'pokládka od 150 Kč/m², materiál po zaměření'),
      PODKLAD_CARD,
      ('Lišty a zakončení', 'Soklové lišty a přechodové profily, v koupelnách a kuchyních s vytaženým soklem.', f'od {LISTY} Kč/bm'),
    ],
    calc=[('PVC v roli – bytové', 330, 150, 'Vinyl'), ('PVC zátěžové', None, 150, 'Vinyl')],
    faq=[
      ('Kolik stojí PVC s pokládkou?', f'PVC v rolích začíná od 330 Kč/m², pokládka od 150 Kč/m². Vyrovnání podkladu stěrkou stojí od {STERKA} Kč/m² při 5 mm a lišty od {LISTY} Kč/bm. Ceny jsou bez DPH.'),
      ('Jaký je rozdíl mezi PVC a linem?', 'Lidově se „linem“ říká PVC v rolích. Přírodní linoleum je jiný materiál vyrobený z lněného oleje. Poradíme, co se hodí do vašeho prostoru.'),
      ('Lepit, nebo položit volně?', 'Volná pokládka je možná, ale nedoporučujeme ji. PVC lepíme celoplošně – podlaha se nevlní, nehýbe se a vydrží déle.'),
      ('Jak široké role máte?', 'PVC dodáváme v šířích 2, 3 i 4 m, takže většinu místností pokryjeme bez spoje.'),
      COMMON_FAQ_TERMIN, COMMON_FAQ_ZARUKA,
    ])

U['koberce'] = dict(
    title='Koberce Praha – od 154 Kč/m², pokládka od 228 Kč/m² | AR podlahy',
    desc='Metrážové a zátěžové koberce v rolích i čtvercích pro byty, kanceláře i schodiště v Praze a Středočeském kraji. Koberce od 154 Kč/m², pokládka od 228 Kč/m².',
    h1='Koberce – prodej a pokládka',
    bullets=B3('Koberce od 154 Kč/m², pokládka od 228 Kč/m²'),
    cards=[
      ('Bytové metrážové koberce', 'Do ložnic, dětských pokojů i obýváků. Teplé, tlumí hluk a kroky, široký výběr barev a struktur.', 'materiál od 154 · pokládka od 228 Kč/m²'),
      ('Zátěžové koberce a čtverce', 'Do kanceláří, hotelů a společných prostor. Kobercové čtverce fixujeme tekutou fixací a poškozený kus se dá snadno vyměnit.', 'pokládka od 228 Kč/m², materiál po zaměření'),
      ('Koberce na schody', 'Koberce lepíme na schodiště včetně bočnic, s pevně zakončenými hranami.', IND),
      PODKLAD_CARD,
    ],
    calc=[('Koberec bytový (metráž)', 154, 228, 'Koberec'), ('Koberec zátěžový / čtverce', None, 228, 'Koberec')],
    faq=[
      ('Kolik stojí koberec s pokládkou?', f'Koberce začínají od 154 Kč/m², pokládka od 228 Kč/m². Vyrovnání podkladu stojí od {STERKA} Kč/m² při 5 mm a lišty od {LISTY} Kč/bm. Ceny jsou bez DPH.'),
      ('Role, nebo čtverce?', 'Metrážový koberec z role je ideální do bytu – je bez spojů a příjemný. Kobercové čtverce se hodí do kanceláří, protože se poškozený kus dá snadno vyměnit.'),
      ('Lepí se koberec, nebo jen pokládá?', 'Koberce lepíme celoplošně disperzním lepidlem, aby se nevlnily a vydržely provoz. Kobercové čtverce fixujeme tekutou fixací.'),
      ('Pokládáte koberce i na schody?', 'Ano, koberce lepíme na schody i bočnice.'),
      ('Můžu si koberce prohlédnout?', 'Ano, vzorky máme ve vzorkovně v Praze-Radotíně. Nebo vám je přivezeme na zaměření.'),
      COMMON_FAQ_TERMIN, COMMON_FAQ_ZARUKA,
    ])

U['historicke'] = dict(
    h1='Historické podlahy – obnova a renovace',
    bullets=B3('Renovace od 600 Kč/m², obnova vzoru individuálně'),
    faq=[
      ('Kolik stojí obnova historické podlahy?', 'Ke každé historické podlaze přistupujeme individuálně. Samotná renovace (broušení, tmel, lak nebo olej) začíná od 600 Kč/m² bez DPH, rozebrání, doplnění a znovusložení vzoru naceníme po prohlídce.'),
      ('Dá se zachránit i hodně poškozená podlaha?', 'Ve většině případů ano. Poškozené dílce vyměníme nebo vyrobíme nové, zbytek původní podlahy zachováme. Při zaměření posoudíme, co je reálné.'),
      ('Pracujete i v památkově chráněných objektech?', 'Ano, s individuálním přístupem ke každému objektu. Renovovali jsme například kazetové parkety na Apoštolské nunciatuře, mozaikové parkety na Ministerstvu pro místní rozvoj nebo podlahy ve Staroměstské radnici.'),
      ('Lak, nebo olej?', 'U historických podlah často volíme olej nebo vosk, které zachovají přirozený vzhled. V místech s velkým provozem doporučíme odolný lak.'),
      COMMON_FAQ_TERMIN, COMMON_FAQ_ZARUKA])

U['laminat'] = dict(
    title='Laminátové podlahy Praha – od 499 Kč/m² | AR podlahy',
    desc='Laminátové plovoucí podlahy v Praze a Středočeském kraji. Od 499 Kč/m² bez DPH, pokládka včetně podložky a lišt, zaměření zdarma do 48 hodin.',
    minprice=499,
    h1='Laminátové podlahy – prodej a pokládka',
    bullets=B3('Laminát od 499 Kč/m²'),
    cards=[
      ('Laminátové podlahy', 'Odolný povrch proti poškrábání, široký výběr dekorů dřeva i kamene. Vhodné do bytů, domů i kanceláří.', 'od 499 Kč/m²'),
      ('Plovoucí pokládka', 'Dílce se spojí zámkem bez lepení na podložku. Rychlá montáž a čistá práce.', 'po zaměření'),
      PODKLAD_CARD, LISTY_CARD,
    ],
    calc=[('Laminátová podlaha', 499, None, 'Laminátová podlaha')],
    faq=[
      ('Kolik stojí laminátová podlaha?', f'Laminátové podlahy u nás začínají od 499 Kč/m². Stěrka stojí od {STERKA} Kč/m² při 5 mm a lišty od {LISTY} Kč/bm. Ceny jsou bez DPH.'),
      ('Laminát, nebo vinyl?', 'Laminátové podlahy dnes ustupují vinylu, ale jejich kvalita je na vysoké úrovni a na trhu stále mají své místo. Laminát je odolný proti poškrábání, vinyl lépe snáší vodu a je tišší. Poradíme podle místnosti a provozu.'),
      ('Lze laminát na podlahové topení?', 'Ano, většina laminátů je pro podlahové topení vhodná. Důležitá je správná podložka a vysušený podklad.'),
      VZORKY, COMMON_FAQ_TERMIN, COMMON_FAQ_ZARUKA])

U['korek'] = dict(
    title='Korkové podlahy Praha – lepený i plovoucí korek | AR podlahy',
    desc='Korkové podlahy v Praze a Středočeském kraji – teplé, tiché a příjemné na chůzi. Lepený korek i do koupelny a na podlahové topení. Cena na dotaz, zaměření zdarma do 48 hodin.',
    minprice=0,
    h1='Korkové podlahy – prodej a pokládka',
    bullets=B3('Cena na dotaz'),
    cards=[
      ('Korkové podlahy', 'Teplé na dotek, pružné a tiché. Ideální do dětských pokojů, ložnic a všude, kde chodíte bosí.', 'na dotaz'),
      ('Celoplošně lepený korek', 'Jediná správná volba do koupelny a na podlahové topení – odolá vlhkosti a dobře vede teplo.', 'na dotaz'),
      ('Plovoucí korek', 'Systém se zámkem do suchých místností. Do koupelny se nehodí a na topení má horší prostupnost tepla.', 'na dotaz'),
      PODKLAD_CARD,
    ],
    calc=None, note='Korkové podlahy naceníme na dotaz, u materiálu platí minimální prodej. Ceny jsou bez DPH.',
    faq=[
      ('Kolik stojí korková podlaha?', 'Korkové podlahy naceníme na dotaz, u materiálu platí minimální prodej. Napište nám nebo zavolejte a připravíme nabídku.'),
      ('Je korek vhodný do koupelny a na podlahové topení?', 'Pro koupelnu i podlahové topení jednoznačně vyberte celoplošně lepený korek. Běžný plovoucí korek se do koupelny nehodí a na topení má horší prostupnost tepla.'),
      VZORKY, COMMON_FAQ_TERMIN, COMMON_FAQ_ZARUKA])

U['sterky'] = dict(
    title='Lité epoxidové stěrky Praha – od 900 Kč/m² | AR podlahy',
    desc='Lité epoxidové, polyuretanové a dekorativní stěrky v Praze a Středočeském kraji – do bytů, garáží, dílen i hal. Přibližně 900–2 500 Kč/m² bez DPH, zaměření zdarma do 48 hodin.',
    minprice=900,
    h1='Lité epoxidové stěrky',
    bullets=B3('Přibližně 900–2 500 Kč/m² podle systému'),
    cards=[
      ('Epoxidové stěrky (EP)', 'Tvrdé, mechanicky i chemicky velmi odolné. Do garáží, dílen, technických místností a hal, ale i do moderních interiérů v lesku nebo matu. Bez UV stabilního laku mohou časem lehce žloutnout.', 'od 900 Kč/m²'),
      ('Polyuretanové stěrky (PU)', 'Pružnější a houževnatější než epoxid, lépe tlumí kročejový hluk a přirozeně odolávají UV záření. Do bytů, domů, kanceláří a na podlahové topení.', 'od 900 Kč/m²'),
      ('Dekorativní stěrky', 'Betonový a mramorový (žíhaný) efekt, stěrky s barevnými chipsy s efektem žuly nebo terazza, 3D podlahy a kamenný koberec z oblázků a čiré pryskyřice i do exteriéru.', 'až 2 500 Kč/m²'),
      ('Příprava podkladu', 'Broušení, penetrace a vyrovnání podkladu – základ trvanlivosti stěrky.', f'vyrovnání od {STERKA} Kč/m² (5 mm)'),
    ],
    calc=None, note='Lité stěrky stojí přibližně od 900 do 2 500 Kč/m² podle tloušťky vrstvy, systému a stavu podkladu. Ceny jsou bez DPH.',
    faq=[
      ('Kolik stojí litá stěrka?', 'Přibližně od 900 do 2 500 Kč/m² bez DPH. Cena závisí na tloušťce vrstvy, zvoleném systému a stavu podkladu. Přesnou nabídku připravíme po zaměření.'),
      ('Epoxid, nebo polyuretan?', 'Epoxid je tvrdší a odolnější vůči chemii – hodí se do garáží, dílen a hal. Polyuretan je pružnější, tišší, nežloutne a lépe snáší podlahové topení, proto ho doporučujeme do bytů a kanceláří.'),
      ('Jak dlouho stěrka vytvrzuje?', 'Orientačně při 20 °C: chodit opatrně v ponožkách můžete po 12–24 hodinách, nábytek a běžný provoz za 2–3 dny. Plné mechanické a chemické zatížení (vjezd aut, mytí chemií) snese epoxid po 7 dnech, polyuretan po 5–7 dnech. Rychlost zrání závisí na teplotě, vlhkosti a typu pryskyřice.'),
      ('Jaké dekorativní stěrky děláte?', 'Žíhané stěrky s betonovým nebo mramorovým efektem, stěrky s barevnými chipsy (efekt žuly či terazza), 3D podlahy se zalitou grafikou nebo přírodninami a kamenný koberec z oblázků a čiré pryskyřice, vhodný i do exteriéru.'),
      COMMON_FAQ_TERMIN, COMMON_FAQ_ZARUKA])

U['terasy'] = dict(
    title='Terasy Praha – WPC, exotické dřevo i jehličnany, montáž od 850 Kč/m² | AR podlahy',
    desc='Stavba a pokládka teras v Praze a Středočeském kraji: WPC, exotické dřeviny a jehličnany. Montáž včetně podkladní konstrukce od 850 Kč/m² bez materiálu, zaměření zdarma do 48 hodin.',
    minprice=850,
    h1='Terasy – WPC, exotika i jehličnany',
    bullets=B3('Montáž od 850 Kč/m² bez materiálu'),
    cards=[
      ('Dřevoplastové (WPC) terasy', 'Směs dřeva a plastu s dlouhou životností, barevnou stálostí na slunci a odolností proti mechanickému poškození. Na terasy, balkony i kolem bazénů.', 'montáž od 850 Kč/m²'),
      ('Exotické dřeviny', 'Teak, merbau, massaranduba, ipe, garapa nebo bangkirai. Přirozeně trvanlivé, tvrdé a odolné proti povětrnosti i vlhkosti, proto vhodné i k bazénům.', 'montáž od 850 Kč/m²'),
      ('Jehličnaté dřeviny', 'Borovice a modřín – přírodní vzhled a nižší pořizovací cena. Ošetřují se olejem.', 'montáž od 850 Kč/m²'),
      ('Podkladní konstrukce', 'Rošt, terče a odvodnění – správná konstrukce rozhoduje o životnosti terasy. Je součástí ceny montáže.', 'v ceně montáže'),
    ],
    calc=[('Terasa – montáž vč. podkladní konstrukce', None, 850, 'Potřebuji poradit s technickým řešením')],
    note='Montáž terasy včetně podkladní konstrukce od 850 Kč/m² bez materiálu. Materiál naceníme podle zvoleného typu. Ceny jsou bez DPH.',
    faq=[
      ('Kolik stojí terasa?', 'Montáž terasy včetně podkladní konstrukce stojí od 850 Kč/m² bez materiálu. Materiál naceníme podle zvoleného typu – WPC, exotické dřevo nebo jehličnany. Ceny jsou bez DPH.'),
      ('WPC, nebo dřevo?', 'WPC je téměř bezúdržbové a drží barvu. Exotické dřevo je přirozeně trvanlivé a krásně stárne, jehličnany jsou cenově nejdostupnější. Dřevo potřebuje pravidelné ošetření olejem.'),
      ('Jak se o terasu starat?', 'WPC stačí umýt. Dřevěnou terasu doporučujeme jednou až dvakrát ročně ošetřit olejem.'),
      VZORKY, COMMON_FAQ_TERMIN, COMMON_FAQ_ZARUKA])

U['podklad'] = dict(
    desc='Příprava podkladu pod podlahy v Praze a Středočeském kraji: demontáž staré podlahy, měření vlhkosti, penetrace od 25 Kč/m², samonivelační stěrka od 250 Kč/m². Zaměření zdarma do 48 hodin.',
    h1='Příprava podkladu',
    cards=[
      ('Měření vlhkosti', 'Vlhkost podkladu měříme vždy před pokládkou. Příliš vlhký podklad je nejčastější příčina problémů s podlahou.', 'v rámci zaměření zdarma'),
      ('Samonivelační stěrky', 'Vyrovnání nerovností litou stěrkou – nutné hlavně pod vinyl, PVC a lepené dřevo.', f'od {STERKA} Kč/m² (5 mm)'),
      ('Penetrace a opravy', 'Zpevnění podkladu penetrací, oprava prasklin a výtluků.', 'penetrace od 25 Kč/m²'),
      ('Demontáž staré podlahy', 'Odstranění původních krytin a lepidel, aby nová podlaha měla pevný základ.', IND),
    ],
    faq=[
      ('Kolik stojí příprava podkladu?', f'Penetrace stojí od 25 Kč/m², samonivelační stěrka od {STERKA} Kč/m² při tloušťce 5 mm. Opravy a demontáž staré podlahy naceníme po zaměření. Ceny jsou bez DPH.'),
      ('Děláte i demontáž staré podlahy?', 'Ano, děláme vše spojené s demontáží a přípravou podkladu – od odstranění staré krytiny a lepidel přes opravy a penetraci až po vyrovnání stěrkou.'),
      ('Proč je příprava podkladu tak důležitá?', 'Nerovnosti a vlhkost se propíšou do každé podlahy – vinyl ukáže hrboly, dřevo se může zvlnit. Dobře připravený podklad prodlouží životnost podlahy o roky.'),
      ('Musím vyrovnávat podklad vždy?', 'Ne vždy. Při zaměření změříme rovinnost a řekneme, jestli je stěrka potřeba.'),
      COMMON_FAQ_TERMIN, COMMON_FAQ_ZARUKA])

U['dvere'] = dict(
    title='Interiérové dveře Praha – od 3 940 Kč, prodej a montáž | AR podlahy',
    desc='Interiérové dveře a zárubně v Praze a Středočeském kraji: dveře od 3 940 Kč, zárubeň od 3 200 Kč, montáž od 1 600 Kč bez DPH. Dveře sladěné s podlahou, zaměření zdarma do 48 hodin.',
    minprice=3940,
    h1='Interiérové dveře – prodej a montáž',
    bullets=['Zaměření zdarma do 48 hodin', 'Dveře od 3 940 Kč, zárubeň od 3 200 Kč, montáž od 1 600 Kč', 'Záruka až 12 let na materiál, 24 měsíců na práci'],
    cards=[
      ('Rámové dveře', 'Rámy i příčky z plného masivu, bez viditelných spojů, s dvoučepovými závěsy. Pevná konstrukce a dlouhá životnost.', 'od 3 940 Kč'),
      ('Povrch Greko', 'Zvýrazněná struktura dřeva a vyšší odolnost proti poškrábání. Nejlepší poměr cena/kvalita.', 'od 3 940 Kč'),
      ('Povrch CPL', 'Laminát 0,2 mm odolný proti nárazům, oděru, teplu a UV záření. Do náročných prostor.', 'od 3 940 Kč'),
      ('Zárubně a montáž', 'Obložkové i ocelové zárubně, zaměření a montáž vlastním týmem.', 'zárubeň od 3 200 · montáž od 1 600 Kč'),
    ],
    note='Dveře od 3 940 Kč, zárubeň od 3 200 Kč, montáž od 1 600 Kč za kus. Ceny jsou bez DPH.',
    faq=[
      ('Kolik stojí interiérové dveře s montáží?', 'Dveře začínají od 3 940 Kč, zárubeň od 3 200 Kč a montáž od 1 600 Kč. Ceny jsou bez DPH a za kus. Konečná cena záleží na modelu, povrchu a typu zárubně.'),
      ('Jaký povrch zvolit?', 'Greko má nejlepší poměr cena/kvalita a věrnou strukturu dřeva. CPL laminát je nejodolnější – vhodný do chodeb, dětských pokojů a kanceláří.'),
      ('Sladíte dveře s podlahou?', 'Ano, dveře a podlahu vybíráme společně, aby k sobě ladily odstínem i strukturou.'),
      ('Můžu si dveře prohlédnout?', 'Ano, ve vzorkovně v Praze-Radotíně. Nebo vám katalog a vzorky přivezeme na zaměření.'),
      COMMON_FAQ_TERMIN, COMMON_FAQ_ZARUKA])

U['vchodove'] = dict(
    title='Vchodové dveře Praha – od 39 550 Kč, prodej a montáž | AR podlahy',
    desc='Vchodové dveře do bytů a rodinných domů v Praze a Středočeském kraji od 39 550 Kč bez DPH – zaměření, dodání a montáž. Zaměření zdarma do 48 hodin.',
    minprice=39550,
    h1='Vchodové dveře – prodej a montáž',
    bullets=['Zaměření zdarma do 48 hodin', 'Dveře od 39 550 Kč, montáž individuálně', 'Záruka až 12 let na materiál, 24 měsíců na práci'],
    cards=[
      ('Bytové vchodové dveře', 'Bezpečnostní dveře do bytů s lepší zvukovou izolací.', 'od 39 550 Kč'),
      ('Dveře do rodinného domu', 'Tepelně izolační vchodové dveře s kvalitním kováním.', 'od 39 550 Kč'),
      ('Zárubně a demontáž', 'Výměna starých dveří včetně zárubně a odvozu, s co nejmenším zásahem do zdi.', IND),
      ('Montáž', 'Zaměření a montáž vlastním týmem, včetně seřízení a dotěsnění.', 'individuálně'),
    ],
    note='Vchodové dveře od 39 550 Kč, montáž naceníme individuálně po zaměření. Ceny jsou bez DPH.',
    faq=[
      ('Kolik stojí vchodové dveře s montáží?', 'Vchodové dveře začínají od 39 550 Kč bez DPH. Montáž naceníme individuálně podle typu, rozměru a stavu otvoru po bezplatném zaměření.'),
      ('Vyměníte i zárubeň?', 'Ano, pokud je to potřeba. Starou zárubeň vybouráme a osadíme novou, nebo dveře přizpůsobíme stávající.'),
      ('Jak dlouho trvá výměna dveří?', 'Samotná montáž obvykle zabere jeden den. Dodací lhůtu dveří upřesníme v nabídce.'),
      ('Můžu si dveře prohlédnout?', 'Ano, katalog vám ukážeme ve vzorkovně v Praze-Radotíně nebo ho přivezeme na zaměření.'),
      COMMON_FAQ_TERMIN, COMMON_FAQ_ZARUKA])

U['rekonstrukce'] = dict(
    desc='Rekonstrukce bytů, domů a interiérů v Praze a Středočeském kraji. Podlahy, dveře, malířské a lakýrnické práce vlastním týmem, koupelny se subdodavatelem a kuchyně ve spolupráci se Siko.',
    h1='Rekonstrukce a stavby na klíč',
    sub='Podlahy, dveře, malování, koupelny i kuchyně – vše koordinujeme za vás.',
    cards=[
      ('Podlahy a dveře', 'Všechny druhy podlah, renovace parket a interiérové i vchodové dveře. Děláme vlastním týmem.', IND),
      ('Malířské a lakýrnické práce', 'Malování stěn a stropů, lakování dveří, zárubní a dalších prvků. Vlastním týmem.', IND),
      ('Koupelny', 'Rekonstrukce koupelen ve spolupráci s ověřeným subdodavatelem, termíny koordinujeme my.', IND),
      ('Kuchyně', 'Koordinace a prodej kuchyní ve spolupráci se Siko, včetně sladění s podlahou.', IND),
    ],
    faq=[
      ('Kolik stojí rekonstrukce bytu?', 'Cena záleží na rozsahu, stavu a zvolených materiálech. Po prohlídce připravíme rozpočet po jednotlivých položkách.'),
      ('Co děláte vlastními lidmi?', 'Vlastním týmem děláme podlahy a dveře, malířské a lakýrnické práce. Koupelny realizujeme se subdodavatelem a kuchyně koordinujeme a prodáváme ve spolupráci se Siko.'),
      ('Jak dlouho rekonstrukce trvá?', 'Záleží na rozsahu. Harmonogram dostanete spolu s rozpočtem a budeme se ho držet.'),
      ('Kde pracujete?', 'V celé Praze a ve Středočeském kraji. Vzorkovnu máme v Praze-Radotíně.'),
      COMMON_FAQ_ZARUKA])

for k, v in U.items():
    CONF[k].update(v)

# „v Praze“ pryč z viditelných textů podstránek (title a description pro Google zůstávají)
NOPRAHA = re.compile(r' v Praze(?![-–])(?: a (?:ve )?Středočeském kraji)?')
def _clean(x):
    if isinstance(x, str): return re.sub(r'(\d) (\d{3})', '\\1\u00a0\\2', NOPRAHA.sub('', x))
    if isinstance(x, tuple): return tuple(_clean(i) for i in x)
    if isinstance(x, list): return [_clean(i) for i in x]
    return x
for k, c in CONF.items():
    for f in ('h1', 'sub', 'h2', 'bullets', 'cards', 'faq', 'note'):
        if f in c: c[f] = _clean(c[f])
