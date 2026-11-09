import re, json, sys, os
SP = '/tmp/claude-0/-home-claude/a1dc3947-88ac-503c-910c-cbe14d93fb1b/scratchpad'
DESIGN = SP + '/web/project'
STATIC = '/home/claude/ar-podlahy/site'
BASE = 'https://www.ar-podlahy.cz'

def sec(s, name, nxt):
    a = s.index('<!-- %s -->' % name); b = s.index('<!-- %s -->' % nxt, a)
    return s[a:b]

EYE = 'font-size: 13px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; color: #8a6a3f;'
H2 = 'margin: 0; font-size: clamp(30px, 3.4vw, 46px); line-height: 1.1; font-weight: 900;'
P = 'margin: 0; font-size: 17px; line-height: 1.7; color: #3d3830;'
WRAP = 'max-width: 1240px; margin: 0 auto; padding: clamp(56px, 6vw, 80px) 24px;'
CARD = 'background: #fff; border: 1px solid #e6ddcf; border-radius: 14px; padding: 28px; display: flex; flex-direction: column; gap: 10px;'
ICON = lambda d: f'<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#8a6a3f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
I_PHONE = ICON('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"></path>')
I_MAIL = ICON('<rect x="2" y="4" width="20" height="16" rx="2"></rect><path d="m22 7-10 6L2 7"></path>')
I_PIN = ICON('<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"></path><circle cx="12" cy="10" r="3"></circle>')
I_CLOCK = ICON('<circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path>')
I_CHECK = ICON('<path d="m5 12 5 5 9-10"></path>')

MAPQ = 'Karlick%C3%A1+834%2F10%2C+153+00+Praha+16'

def subhero(eyebrow, h1, lead, crumbs, L):
    bc = f'<nav aria-label="Drobečková navigace" style="font-size: 13px; color: rgba(255,255,255,.65);"><a href="{L["home"]}" style="color: rgba(255,255,255,.8);">Úvod</a> <span aria-hidden="true">/</span> <span aria-current="page">{crumbs}</span></nav>'
    return f'''<div style="max-width: 1240px; margin: 0 auto; padding: clamp(40px, 5vw, 64px) 24px clamp(48px, 6vw, 80px); display: flex; flex-direction: column; gap: 22px; align-items: flex-start;">
{bc}
<span style="font-size: 13px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; color: #c9a46a;">{eyebrow}</span>
<h1 style="margin: 0; font-size: clamp(36px, 4.8vw, 64px); line-height: 1.06; font-weight: 900; letter-spacing: -.02em; max-width: 900px;">{h1}</h1>
<p style="margin: 0; font-size: clamp(16px, 1.4vw, 19px); line-height: 1.65; color: rgba(255,255,255,.82); max-width: 700px;">{lead}</p>
</div>
'''

def kontakty_body(L):
    cards = f'''<!-- KONTAKTNÍ ÚDAJE -->
<section style="{WRAP} display: flex; flex-direction: column; gap: 32px;">
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
<div style="{CARD}">{I_PHONE}<strong style="font-size: 18px;">Telefon</strong><a href="tel:+420605257236" style="font-size: 22px; font-weight: 900; color: #1a1a1a; text-decoration: none;">+420 605 257 236</a><span style="font-size: 14px; color: #6b655b; line-height: 1.6;">Nejrychlejší cesta k termínu zaměření.</span></div>
<div style="{CARD}">{I_MAIL}<strong style="font-size: 18px;">E-mail</strong><a href="mailto:info@ar-podlahy.cz" style="font-size: 20px; font-weight: 800; color: #1a1a1a; text-decoration: none;">info@ar-podlahy.cz</a><span style="font-size: 14px; color: #6b655b; line-height: 1.6;">Pošlete půdorys, fotky nebo počet m². Ozveme se s návrhem postupu.</span></div>
<div style="{CARD}">{I_PIN}<strong style="font-size: 18px;">Showroom</strong><address style="font-style: normal; font-size: 17px; font-weight: 700; line-height: 1.5;">Karlická 834/10<br>153 00 Praha 16 – Radotín</address><a href="https://maps.google.com/?q={MAPQ}" target="_blank" rel="noopener" style="font-size: 14px; font-weight: 700; color: #8a6a3f;">Navigovat do showroomu →</a><a href="https://www.facebook.com/Podlahy-Praha-349586465068872/" target="_blank" rel="noopener" style="font-size: 14px; font-weight: 700; color: #8a6a3f;">Facebook Podlahy Praha →</a><a href="https://maps.google.com/?cid=7053343600020491698" target="_blank" rel="noopener" style="font-size: 14px; font-weight: 700; color: #8a6a3f;">Recenze na Google Maps · 5,0 ★ →</a></div>
<div style="{CARD}">{I_CLOCK}<strong style="font-size: 18px;">Otevírací doba</strong>
<dl style="margin: 0; display: grid; grid-template-columns: auto 1fr; gap: 6px 16px; font-size: 15px; line-height: 1.5;">
<dt style="font-weight: 700;">Po</dt><dd style="margin: 0;">zavřeno</dd>
<dt style="font-weight: 700;">Út</dt><dd style="margin: 0;">10–12, 13–17</dd>
<dt style="font-weight: 700;">St–Čt</dt><dd style="margin: 0;">10–12, 13–19</dd>
<dt style="font-weight: 700;">Pá</dt><dd style="margin: 0;">10–12</dd>
</dl><span style="font-size: 14px; color: #6b655b;">Jindy po předchozí domluvě.</span></div>
</div>
</section>

<!-- MAPA -->
<section style="max-width: 1240px; margin: 0 auto; padding: 0 24px 32px; display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px 48px; align-items: end;">
<div style="display: flex; flex-direction: column; gap: 16px;">
<span style="{EYE}">Vzorkovna v Radotíně</span>
<h2 style="{H2}">Podlahy si v showroomu můžete prohlédnout i osahat</h2>
</div>
<div style="display: flex; flex-direction: column; gap: 18px;">
<p style="{P}">Ve vzorkovně máme dřevěné, vinylové a PVC podlahy, parkety i interiérové dveře. Poradíme s výběrem dřeviny, povrchové úpravy i s tím, co snese podlahové topení. Pokud nestíháte přijet, vzorky vám přivezeme rovnou na zaměření.</p>
<div style="display: flex; flex-wrap: wrap; gap: 12px;">
<a href="#poptavka" style="background: {{{{accent}}}}; color: #fff; text-decoration: none; padding: 16px 24px; border-radius: 8px; font-weight: 800;">Domluvit návštěvu</a>
<a href="https://maps.google.com/?q={MAPQ}" target="_blank" rel="noopener" style="border: 1px solid #1a1a1a; color: #1a1a1a; text-decoration: none; padding: 16px 24px; border-radius: 8px; font-weight: 700;">Otevřít v Google Maps</a>
</div>
</div>
</section>
<div style="position: relative; margin-bottom: clamp(56px, 6vw, 80px);"><iframe title="Mapa – AR podlahy showroom, Karlická 834/10, Praha 16" src="https://maps.google.com/maps?q={MAPQ}&amp;z=15&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" style="display: block; width: 100%; height: clamp(360px, 42vw, 520px); border: 0; background: #ece5d8; filter: grayscale(1) contrast(.85) brightness(1.12);"></iframe><div aria-hidden="true" style="position: absolute; inset: 0; background: #f3eadb; mix-blend-mode: multiply; pointer-events: none;"></div><svg aria-hidden="true" width="44" height="58" viewBox="0 0 44 58" style="position: absolute; left: 50%; top: 50%; transform: translate(-50%, -100%); pointer-events: none; filter: drop-shadow(0 4px 6px rgba(0,0,0,.3));"><path d="M22 2C11 2 2 10.8 2 21.7 2 36.5 22 56 22 56s20-19.5 20-34.3C42 10.8 33 2 22 2z" fill="#2f6b3a" stroke="#fff" stroke-width="3"></path><circle cx="22" cy="21.5" r="7" fill="#fff"></circle></svg></div>

<!-- SORTIMENT -->
<section style="max-width: 1240px; margin: 0 auto; padding: 0 24px clamp(56px, 6vw, 80px); display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px 64px; align-items: start;">
<div style="display: flex; flex-direction: column; gap: 16px;">
<span style="{EYE}">Sortiment ve vzorkovně</span>
<h2 style="{H2}">Přes 1 000 produktů a vzorů na jednom místě</h2>
<p style="{P}">Materiály si u nás osaháte a porovnáte vedle sebe. Ceny jsou orientační ceny materiálu, přesnou nabídku včetně pokládky připravíme po zaměření. K tomu lité epoxidové stěrky, schody, interiérové i vchodové dveře a rekonstrukce na klíč.</p>
</div>
<div style="display: flex; flex-direction: column;"><div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px; padding: 16px 0; border-bottom: 1px solid #e0d6c6;"><div style="display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 17px;">PVC v rolích</strong><span style="font-size: 14px; color: #6b655b;">Novilon Nova a Viva, šíře 2, 3 a 4 m</span></div><span style="font-size: 17px; font-weight: 800; white-space: nowrap; color: #8a6a3f;">od 330 Kč/m²</span></div><div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px; padding: 16px 0; border-bottom: 1px solid #e0d6c6;"><div style="display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 17px;">Vinylové dílce</strong><span style="font-size: 14px; color: #6b655b;">Thermofix, Fatraclic, Imperio</span></div><span style="font-size: 17px; font-weight: 800; white-space: nowrap; color: #8a6a3f;">od 482 Kč/m²</span></div><div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px; padding: 16px 0; border-bottom: 1px solid #e0d6c6;"><div style="display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 17px;">Dřevěné podlahy</strong><span style="font-size: 14px; color: #6b655b;">vícevrstvé podlahy a parkety</span></div><span style="font-size: 17px; font-weight: 800; white-space: nowrap; color: #8a6a3f;">od 569 Kč/m²</span></div><div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px; padding: 16px 0; border-bottom: 1px solid #e0d6c6;"><div style="display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 17px;">Laminátové podlahy</strong><span style="font-size: 14px; color: #6b655b;">Haro, Egger</span></div><span style="font-size: 17px; font-weight: 800; white-space: nowrap; color: #8a6a3f;">od 223 Kč/m²</span></div><div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px; padding: 16px 0; border-bottom: 1px solid #e0d6c6;"><div style="display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 17px;">Korkové podlahy</strong><span style="font-size: 14px; color: #6b655b;">Haro</span></div><span style="font-size: 17px; font-weight: 800; white-space: nowrap; color: #8a6a3f;">od 662 Kč/m²</span></div><div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px; padding: 16px 0; border-bottom: 1px solid #e0d6c6;"><div style="display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 17px;">Koberce</strong><span style="font-size: 14px; color: #6b655b;">v rolích i ve čtvercích</span></div><span style="font-size: 17px; font-weight: 800; white-space: nowrap; color: #8a6a3f;">od 154 Kč/m²</span></div><div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px; padding: 16px 0; border-bottom: 1px solid #e0d6c6;"><div style="display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 17px;">Terasy</strong><span style="font-size: 14px; color: #6b655b;">WPC, exotika, jehličnany</span></div><span style="font-size: 17px; font-weight: 800; white-space: nowrap; color: #8a6a3f;">od 399 Kč/m²</span></div></div>
</section>

<!-- FIREMNÍ ÚDAJE -->
<section style="background: #ece5d8;">
<div style="max-width: 1240px; margin: 0 auto; padding: 40px 24px; display: flex; flex-wrap: wrap; gap: 16px 48px; align-items: center; justify-content: space-between; font-size: 15px;">
<strong style="font-size: 18px;">Fakturační údaje</strong>
<span>AR-Podlahy &amp; Dveře</span>
<span>IČO 125 848 78</span>
<span>DIČ CZ5906111046</span>
<span>Karlická 834/10, 153 00 Praha 16 – Radotín</span>
</div>
</section>

'''
    return cards

def onas_body(L, src):
    stats = src[src.index('<!-- STATS -->'):src.index('</section>', src.index('<!-- STATS -->'))]
    vals = [
        (I_CHECK, 'Zaměření zdarma do 48 hodin', 'Přijedeme, změříme vlhkost podkladu a skutečné metry. Teprve pak počítáme cenu.'),
        (I_CHECK, 'Vzorky přivezeme k vám', 'Dřevinu a odstín vybíráte u sebe doma, ve světle, ve kterém bude podlaha ležet.'),
        (I_CHECK, 'Vlastní realizační tým', '13 lidí, kteří podlahy pokládají a renovují každý den. Práci nepřeprodáváme subdodavatelům.'),
        (I_CHECK, 'Záruka a péče po předání', 'Záruka až 12 let na materiál, 24 měsíců na práci. Sada na údržbu zdarma u zakázek nad 100 m².'),
    ]
    vcards = ''.join(f'<div style="{CARD}">{i}<strong style="font-size: 18px;">{t}</strong><p style="margin: 0; font-size: 15px; line-height: 1.65; color: #4a443b;">{d}</p></div>' for i, t, d in vals)
    return f'''<!-- PŘÍBĚH -->
<section style="{WRAP} display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: clamp(28px, 4vw, 56px); align-items: center;">
<div style="display: flex; flex-direction: column; gap: 18px;">
<span style="{EYE}">Kdo jsme</span>
<h2 style="{H2}">Rodinná podlahářská firma z Radotína, od roku 1991</h2>
<p style="{P}">AR podlahy pokládá a renovuje podlahy už 35 let. Dnes máme vlastní showroom v Praze-Radotíně a třináctičlenný realizační tým. Za tu dobu jsme položili a zrenovovali přes 1 000 000 m² podlah.</p>
<p style="{P}">Děláme dřevěné, vinylové a PVC podlahy, parkety, laminát, korek i koberce, renovace a broušení parket a interiérové i vchodové dveře. Jako generální dodavatel zajistíme i rekonstrukce a stavby na klíč. Pracujeme v rodinných domech a bytech v Praze a Středočeském kraji, ale i v památkových objektech, kde se historická podlaha nesmí poškodit.</p>
</div>
<img src="/_blob/0275d72697c972c8689368790242b52b" alt="Zrenovovaná parketová podlaha od AR podlahy" style="width: 100%; aspect-ratio: 4 / 3; object-fit: cover; border-radius: 14px; display: block;">
</section>

<!-- VÝZNAMNÉ ZAKÁZKY -->
<section style="max-width: 1240px; margin: 0 auto; padding: clamp(56px, 6vw, 80px) 24px clamp(56px, 6vw, 80px); display: flex; flex-direction: column; gap: 24px;">
<div style="display: flex; flex-direction: column; gap: 14px;"><span style="{EYE}">Významné zakázky</span><h2 style="{H2}">Kde všude už naše podlahy leží</h2></div>
<ul style="margin: 0; padding: 0; list-style: none; display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); column-gap: 40px;"><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Pražský hrad</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Úřad vlády ČR</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Kramářova vila</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Apoštolská nunciatura</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Palác Myslbek</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Fotbalový stadion AC Sparta Praha</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Řízení letového provozu Ruzyně</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Síť prodejen O2 po celé ČR</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Metropole Zličín</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Český statistický úřad</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Knihovna-depozitář MFF UK</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Budova Geofyziky Barrandov</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Slepecký areál Řepy</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Budova firmy ZEPTER</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Restaurace Pod křídlem tmy</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Ministerstvo místního rozvoje</li><li style="padding: 14px 0; border-bottom: 1px solid #e0d6c6; font-size: 16px; font-weight: 700;">Ministerstvo zemědělství</li></ul>
</section>

<!-- JAK PRACUJEME -->
<section style="background: #ece5d8;">
<div style="{WRAP} display: flex; flex-direction: column; gap: 32px;">
<div style="max-width: 720px; display: flex; flex-direction: column; gap: 14px;">
<span style="{EYE}">Jak pracujeme</span>
<h2 style="{H2}">Na čem si zakládáme</h2>
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">{vcards}</div>
</div>
</section>

'''

DFAQ = [
    ('Kolik stojí dřevěná podlaha v Praze?', 'Materiál – vícevrstvé dřevěné podlahy a parkety – začíná u nás od 569 Kč/m². Cena pokládky záleží na stavu podkladu, způsobu pokládky (plovoucí nebo celoplošně lepená) a povrchové úpravě. Přesnou nabídku pošleme po bezplatném zaměření.'),
    ('Jezdíte i mimo Prahu?', 'Ano. Pokládáme po celé Praze a ve Středočeském kraji. Showroom máme v Radotíně, takže jsme rychle třeba v Černošicích, Dobřichovicích, Řevnicích nebo na Berounsku.'),
    ('Lze dát dřevěnou podlahu na podlahové topení?', 'Ano, při správně zvolené dřevině a rozměru prken, vysušeném podkladu a celoplošném lepení. Ve vile v Černošicích jsme takto položili 245 m² masivního dubu na vodní podlahové topení.'),
    ('Jak dlouho trvá pokládka dřevěné podlahy?', 'Od poptávky po montáž obvykle do 6 týdnů. Samotná pokládka bytu trvá několik dní, dvoupodlažní vilu s 245 m² masivu jsme dokončili za 14 dní včetně vytvrzení laku.'),
    ('Jakou dáváte záruku?', 'Záruka až 12 let na materiál, 24 měsíců na práci. Ke každé zakázce nad 100 m² přidáme sadu na údržbu podlahy zdarma.'),
]
TOWNS = ['Praha 1–22', 'Černošice', 'Dobřichovice', 'Řevnice', 'Beroun', 'Jesenice', 'Průhonice', 'Říčany', 'Hostivice', 'Kladno', 'Mníšek pod Brdy', 'Jílové u Prahy']

def drevo_body(L):
    types = [
        ('Masivní dřevěné podlahy', 'Poctivá prkna z masivu, nejčastěji dub. Celoplošně lepená vydrží generace a dají se opakovaně brousit.'),
        ('Vícevrstvé (třívrstvé) podlahy', 'Nášlapná vrstva z ušlechtilého dřeva na stabilním nosiči. Rychlá pokládka a ideální volba na podlahové topení.'),
        ('Parkety', 'Klasické vlysy, rybí kost i mozaika. Pokládka, broušení a lak nebo olej podle toho, jak má podlaha vypadat.'),
        ('Historické podlahy', 'Vídeňské a benátské čtverce a kazetové parkety. Zkušenost z památek, jako je Apoštolská nunciatura.'),
    ]
    cards = ''.join(f'<div style="{CARD}"><strong style="font-size: 19px;">{t}</strong><p style="margin: 0; font-size: 15px; line-height: 1.65; color: #4a443b;">{d}</p></div>' for t, d in types)
    towns = ''.join(f'<li style="background: #fff; border: 1px solid #e6ddcf; border-radius: 999px; padding: 10px 18px; font-size: 15px; font-weight: 700;">{t}</li>' for t in TOWNS)
    faq = ''.join(f'<details style="border-bottom: 1px solid #e4ddd2; padding: 18px 0;"><summary style="display: flex; justify-content: space-between; gap: 20px; align-items: center; font-size: 17px; font-weight: 700; min-height: 44px; cursor: pointer;">{q}<span class="plus" style="font-size: 26px; color: #8a6a3f; font-weight: 400;">+</span></summary><p style="margin: 10px 0 0; font-size: 16px; line-height: 1.7; color: #5b554c;">{a}</p></details>' for q, a in DFAQ)
    return f'''<!-- TYPY PODLAH -->
<section style="{WRAP} display: flex; flex-direction: column; gap: 32px;">
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px 64px; align-items: end;">
<div style="display: flex; flex-direction: column; gap: 14px;"><span style="{EYE}">Co pokládáme</span><h2 style="{H2}">Dřevěná podlaha pro byt, dům i památku</h2></div>
<p style="{P}">Poradíme s dřevinou, formátem i povrchovou úpravou. Ve vzorkovně v Radotíně si podlahy osaháte, nebo vám vzorky přivezeme na zaměření. Materiál od <strong>569 Kč/m²</strong>, pokládku naceníme po zaměření.</p>
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">{cards}</div>
</section>

''' + calc_section() + f'''<!-- LOKALITA -->
<section style="background: #ece5d8;">
<div style="{WRAP} display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px 64px; align-items: center;">
<div style="display: flex; flex-direction: column; gap: 16px;"><span style="{EYE}">Kde pokládáme</span><h2 style="{H2}">Praha a celý Středočeský kraj</h2><p style="{P}">Vyrážíme z Prahy-Radotína. Na zaměření přijedeme do 48 hodin, ať bydlíte v centru Prahy, nebo za ní.</p></div>
<ul style="margin: 0; padding: 0; list-style: none; display: flex; flex-wrap: wrap; gap: 10px;">{towns}<li style="padding: 10px 6px; font-size: 15px; color: #6b655b;">a okolí</li></ul>
</div>
</section>

'''

def drevo_faq():
    faq = ''.join(f'<details style="border-bottom: 1px solid #e4ddd2; padding: 18px 0;"><summary style="display: flex; justify-content: space-between; gap: 20px; align-items: center; font-size: 17px; font-weight: 700; min-height: 44px; cursor: pointer;">{q}<span class="plus" style="font-size: 26px; color: #8a6a3f; font-weight: 400;">+</span></summary><p style="margin: 10px 0 0; font-size: 16px; line-height: 1.7; color: #5b554c;">{a}</p></details>' for q, a in DFAQ)
    return f'''<!-- FAQ DŘEVO -->
<section style="background: #fff; border-top: 1px solid #e4ddd2;">
<div style="max-width: 1240px; margin: 0 auto; padding: clamp(56px, 6vw, 80px) 24px; display: flex; flex-direction: column; gap: 18px;">
<span style="{EYE}">Časté dotazy</span>
<h2 style="{H2} margin-bottom: 8px;">Dřevěné podlahy – na co se ptáte</h2>
{faq}
</div>
</section>

'''

CALC_TYPES = [('Dřevěná vícevrstvá podlaha / parkety', 569, 'Dřevěná vícevrstvá podlaha'), ('Vinylové dílce (Thermofix, Fatraclic, Imperio)', 482, 'Vinyl'),
              ('PVC v rolích (Novilon)', 330, 'Vinyl'), ('Laminátová podlaha (Haro, Egger)', 223, 'Laminátová podlaha'),
              ('Korková podlaha (Haro)', 662, 'Potřebuji poradit s technickým řešením'), ('Koberec', 154, 'Koberec'), ('Terasa (WPC, exotika, jehličnany)', 399, 'Potřebuji poradit s technickým řešením')]
def calc_section():
    opts = ''.join(f'<option value="{p}" data-form="{f}">{t} – od {p} Kč/m²</option>' for t, p, f in CALC_TYPES)
    INP = 'border: 1px solid #d6cdbf; border-radius: 8px; padding: 14px; font-size: 16px; background: #fff; width: 100%; box-sizing: border-box;'
    LB = 'display: flex; flex-direction: column; gap: 8px; font-size: 14px; font-weight: 700;'
    return f'''<!-- KALKULAČKA -->
<section id="kalkulacka" style="background: #1a1a1a; color: #fff;">
<div style="{WRAP} display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px 64px; align-items: center;">
<div style="display: flex; flex-direction: column; gap: 16px;">
<span style="font-size: 13px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; color: #c9a46a;">Kalkulačka</span>
<h2 style="margin: 0; font-size: clamp(30px, 3.4vw, 46px); line-height: 1.1; font-weight: 900;">Spočítejte si orientační cenu podlahy</h2>
<p style="margin: 0; font-size: 17px; line-height: 1.7; color: rgba(255,255,255,.78);">Vyberte druh podlahy a zadejte plochu. Kalkulačka spočítá orientační cenu materiálu podle našeho ceníku. Pokládku a přípravu podkladu naceníme po bezplatném zaměření, protože záleží na stavu podkladu.</p>
</div>
<form id="calc" onsubmit="return false" style="background: #fff; color: #1a1a1a; border-radius: 18px; padding: clamp(24px, 3vw, 36px); display: flex; flex-direction: column; gap: 18px;">
<label style="{LB}">Druh podlahy<select id="calc-typ" style="{INP}">{opts}</select></label>
<label style="{LB}">Plocha v m²<input id="calc-m2" type="number" min="1" step="1" value="50" inputmode="numeric" style="{INP}"></label>
<label style="display: flex; gap: 10px; align-items: center; font-size: 15px; font-weight: 600;"><input id="calc-prorez" type="checkbox" checked style="width: 20px; height: 20px; accent-color: #8a6a3f;">Připočítat prořez 8 %</label>
<div style="background: #f5f1ea; border-radius: 12px; padding: 20px; display: flex; flex-direction: column; gap: 6px;">
<span style="font-size: 14px; color: #6b655b;">Materiál orientačně od</span>
<strong id="calc-vysledek" style="font-size: clamp(32px, 3.4vw, 44px); font-weight: 900; line-height: 1.1; color: #1a1a1a;">30 726 Kč</strong>
<span id="calc-detail" style="font-size: 13px; color: #6b655b;">54 m² × 569 Kč/m² · bez pokládky a přípravy podkladu</span>
</div>
<a id="calc-cta" href="#poptavka" style="background: #8a6a3f; color: #fff; text-align: center; text-decoration: none; padding: 17px; border-radius: 8px; font-weight: 800; font-size: 16px;">Chci přesnou nabídku včetně pokládky</a>
<span style="font-size: 12px; color: #8a8378; line-height: 1.5;">Orientační výpočet z ceníku materiálu „od“. Konečná cena závisí na konkrétním výrobku, stavu podkladu a rozsahu prací.</span>
</form>
</div>
</section>

'''
CALC_JS = """<script>
(function(){var t=document.getElementById('calc-typ'),m=document.getElementById('calc-m2'),p=document.getElementById('calc-prorez'),r=document.getElementById('calc-vysledek'),d=document.getElementById('calc-detail'),c=document.getElementById('calc-cta');if(!t)return;
function f(n){return Math.round(n).toLocaleString('cs-CZ')}
function u(){var a=Math.max(0,parseFloat(m.value)||0),k=p.checked?1.08:1,cena=+t.value,q=Math.ceil(a*k);r.textContent=f(q*cena)+' Kč';d.textContent=q+' m² × '+cena+' Kč/m² · bez pokládky a přípravy podkladu'}
[t,m,p].forEach(function(e){e.addEventListener('input',u);e.addEventListener('change',u)});u();
c.addEventListener('click',function(){var pl=document.querySelector('#poptavka input[name=plocha]'),ty=document.querySelector('#poptavka select[name=typ]');if(pl)pl.value=m.value;if(ty){var want=t.options[t.selectedIndex].getAttribute('data-form');for(var i=0;i<ty.options.length;i++){if(ty.options[i].text===want){ty.selectedIndex=i;break}}}});})();
</script>"""

MORE = [
    ('7da54f6bdfc063aa6c80facd6b1e189f', 'ref-urad-vlady.jpg', 'Úřad vlády ČR – Strakova akademie', 'Památkový objekt · Praha 1', 'Podlahářské práce v sídle vlády. [DOPLNIT: typ podlahy, rozsah v m², co bylo potřeba vyřešit]', 'Foto: Packa · CC BY-SA 3.0'),
    ('26c18642d9614617608a571fe31a65c2', 'ref-kramarova-vila.jpg', 'Kramářova vila', 'Památkový objekt · Praha 1', 'Podlahy v reprezentační vile předsedy vlády. [DOPLNIT: renovace / nové podlahy, dřevina, rozsah]', 'Foto: Jan Polák · CC BY-SA 3.0'),
    ('27288c1abe1664a724e15f614fbf6c25', 'ref-prazsky-hrad.jpg', 'Pražský hrad', 'Památkový objekt · Praha 1', 'Práce v areálu Pražského hradu. [DOPLNIT: které prostory, typ podlahy, rozsah]', 'Foto: Mgimelfarb · CC BY-SA 4.0'),
]
def more_studies():
    cards = ''.join(f'''<article style="background: #fff; border: 1px solid #e6ddcf; border-radius: 16px; overflow: hidden; display: flex; flex-direction: column;"><img src="/_blob/{b}" alt="{t}" style="width: 100%; aspect-ratio: 16 / 10; object-fit: cover; display: block;"><div style="padding: 24px; display: flex; flex-direction: column; gap: 10px; flex-grow: 1;"><span style="font-size: 12px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; color: #8a6a3f;">{tag}</span><h3 style="margin: 0; font-size: 20px; line-height: 1.25; font-weight: 900;">{t}</h3><p style="margin: 0; font-size: 15px; line-height: 1.65; color: #4a443b;">{d}</p><span style="margin-top: auto; font-size: 11px; color: #8a8378;">{c}</span></div></article>''' for b, f, t, tag, d, c in MORE)
    return f'''<!-- DALŠÍ STUDIE -->
<section style="max-width: 1240px; margin: 0 auto; padding: 0 24px clamp(56px, 6vw, 80px); display: flex; flex-direction: column; gap: 24px;">
<h3 style="margin: 0; font-size: clamp(22px, 2.2vw, 28px); font-weight: 900;">Další realizace</h3>
<div class="refgrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">{cards}</div>
</section>

'''

LANDS = ['drevo', 'parkety', 'vinyl', 'pvc', 'koberce', 'historicke', 'laminat', 'korek', 'sterky', 'terasy', 'podklad', 'dvere', 'vchodove', 'rekonstrukce']

def page(kind, src, target):
    L = {'home': 'Main.dc.html', 'kont': 'Kontakty.dc.html', 'onas': 'O-nas.dc.html'} if target == 'design' else {'home': '/', 'kont': '/kontakty/', 'onas': '/o-nas/'}
    if kind == 'kontakty':
        title = 'Kontakty a showroom Praha-Radotín | AR podlahy'
        desc = 'Kontakt na AR podlahy: +420 605 257 236, info@ar-podlahy.cz. Showroom Karlická 834/10, Praha 16 – Radotín. Otevírací doba a mapa.'
        path = '/kontakty/'; crumb = 'Kontakty'
        hero = subhero('Kontakty', 'Zavolejte nám nebo přijďte do showroomu v Radotíně', 'Zaměření a konzultace jsou zdarma. Ozveme se do 48 hodin a vzorky vám rádi přivezeme až domů.', crumb, L)
        body = kontakty_body(L)
        ptype = 'ContactPage'
        keep_stats = False
        extra = sec(src, 'POPTÁVKA', 'FOOTER')
    elif kind in LANDS:
        import landing
        c = landing.CONF[kind]
        title, desc, crumb = c['title'], c['desc'], c['crumb']
        path = '/' + c['slug'] + '/'
        hero, body = landing.build(kind, src, L)
        ptype = 'WebPage'
        keep_stats = False
        extra = ''
    else:
        title = 'O nás – rodinná podlahářská firma od roku 1991 | AR podlahy'
        desc = 'AR podlahy je rodinná podlahářská firma z Prahy-Radotína. 35 let praxe, 13 lidí v týmu, přes 1 000 000 m² podlah a reference od Pražského hradu po rodinné domy.'
        path = '/o-nas/'; crumb = 'O nás'
        hero = subhero('O nás', 'Podlahy děláme poctivě už od roku 1991', 'Jsme rodinná firma z Prahy-Radotína. Každou podlahu bereme jako by ležela u nás doma, ať jde o byt, vilu, nebo Pražský hrad.', crumb, L)
        body = onas_body(L, src)
        ptype = 'AboutPage'
        keep_stats = True
        extra = sec(src, 'TRUST STRIP', 'SLUŽBY') + sec(src, 'GARANCE', 'PODLAHOVÉ TOPENÍ (odborný obsah)') + sec(src, 'REFERENCE BUDOVY', 'RECENZE + FAQ') + sec(src, 'POPTÁVKA', 'FOOTER')
    url = BASE + path
    # head
    head_end = src.index('</head>')
    head = src[:head_end]
    head = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', head)
    head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + desc, head)
    head = head.replace(f'<link rel="canonical" href="{BASE}/">', f'<link rel="canonical" href="{url}">')
    head = head.replace(f'<meta property="og:url" content="{BASE}/">', f'<meta property="og:url" content="{url}">')
    for p in ['og:title', 'og:description']:
        head = re.sub(r'(<meta property="%s" content=")[^"]*' % p, lambda m: m.group(1) + (title if 'title' in p else desc), head)
    for p in ['twitter:title', 'twitter:description']:
        head = re.sub(r'(<meta name="%s" content=")[^"]*' % p, lambda m: m.group(1) + (title if 'title' in p else desc), head)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": ptype, "@id": url + "#stranka", "url": url, "name": title, "description": desc, "inLanguage": "cs",
         "isPartOf": {"@id": BASE + "/#web"}, "about": {"@id": BASE + "/#firma"}, "mainEntity": {"@id": BASE + "/#firma"},
         "breadcrumb": {"@id": url + "#drobecky"}},
        {"@type": "BreadcrumbList", "@id": url + "#drobecky", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Úvod", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": crumb, "item": url}]},
        {"@type": "HomeAndConstructionBusiness", "@id": BASE + "/#firma", "name": "AR podlahy", "url": BASE + "/", "description": "Pokládka a renovace dřevěných podlah, parket, vinylu, PVC a koberců v Praze a Středočeském kraji od roku 1991.", "hasMap": "https://www.google.com/maps?cid=7053343600020491698", "sameAs": ["https://www.facebook.com/Podlahy-Praha-349586465068872/", "https://www.google.com/maps?cid=7053343600020491698"], "areaServed": [{"@type": "City", "name": "Praha"}, {"@type": "AdministrativeArea", "name": "Středočeský kraj"}],
         "telephone": "+420605257236", "email": "info@ar-podlahy.cz", "foundingDate": "1991", "taxID": "12584878",
         "address": {"@type": "PostalAddress", "streetAddress": "Karlická 834/10", "addressLocality": "Praha 16 – Radotín", "postalCode": "153 00", "addressCountry": "CZ"},
         "openingHoursSpecification": [
             {"@type": "OpeningHoursSpecification", "dayOfWeek": "Tuesday", "opens": "10:00", "closes": "17:00"},
             {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Wednesday", "Thursday"], "opens": "10:00", "closes": "19:00"},
             {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "10:00", "closes": "12:00"}]}]}
    if kind in LANDS:
        c = __import__('landing').CONF[kind]
        ld["@graph"].append({"@type": "Service", "@id": url + "#sluzba", "name": c['service'], "serviceType": c['service'],
            "provider": {"@id": BASE + "/#firma"}, "areaServed": [{"@type": "City", "name": "Praha"}, {"@type": "AdministrativeArea", "name": "Středočeský kraj"}],
            **({"offers": {"@type": "Offer", "priceSpecification": {"@type": "UnitPriceSpecification", "minPrice": c['minprice'], "priceCurrency": "CZK", "unitText": "m²", "valueAddedTaxIncluded": False}}} if c.get('minprice') else {})})
        ld["@graph"].append({"@type": "FAQPage", "@id": url + "#dotazy", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c['faq']]})
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=2) + '\n</script>', head, flags=re.S)
    # body parts
    hs = src.index('<!-- HERO + HEADER -->')
    pre = src[head_end:hs]
    header = src[src.index('<header', hs):src.index('</header>', hs) + 9]
    stats = src[src.index('<!-- STATS -->'):src.index('</section>', src.index('<!-- STATS -->'))] if keep_stats else ''
    heros = f'<!-- HERO + HEADER -->\n<section class="hero" style="color: #fff;">\n{header}\n{hero}{stats}</section>\n\n'
    rest = src[src.index('<!-- FOOTER -->'):]
    out = head + pre + heros + body + extra + rest
    if kind in LANDS:
        import landing as drevo2
        out = re.sub(r'<nav aria-label="Odkazy v patičce"[^>]*>\s*<strong[^>]*>Menu</strong>.*?</nav>', '', out, flags=re.S)
        out = re.sub(r'<details[^>]*>\s*<summary[^>]*>\s*Menu.*?</details>', '', out, count=1, flags=re.S)
        out = out.replace('</style>', drevo2.MBAR_CSS + '\n</style>', 1)
    # links
    out = out.replace('href="#sluzby"', f'href="{L["home"]}#sluzby"').replace('href="#reference"', f'href="{L["home"]}#reference"')
    out = out.replace('href="#kontakt"', f'href="{L["kont"]}"').replace('<a href="#">O nás</a>', f'<a href="{L["onas"]}">O nás</a>')
    out = out.replace('REALIMG/', 'img/real/' if target == 'design' else '/img/real/')
    if target == 'design':
        out = out.replace('<a href="/" aria-label="AR podlahy – úvod"', '<a href="Main.dc.html" aria-label="AR podlahy – úvod"')
        out = re.sub(r'"\$preview":\{"width":1440,"height":\d+\}', '"$preview":{"width":1440,"height":%d}' % {'onas': 4650, 'kontakty': 3700, 'drevo': 6200, 'parkety': 6100, 'pvc': 5050, 'koberce': 5050, **{"historicke": 5500, "laminat": 4500, "korek": 4500, "sterky": 3850, "terasy": 5050, "podklad": 5050, "dvere": 3800, "vchodove": 3800, "rekonstrukce": 5500}}.get(kind, 4550), out)
    else:
        if kind in LANDS:
            out = out.replace('</body>', __import__('landing').JS + '\n</body>', 1)
        out = out.replace('/_blob/0275d72697c972c8689368790242b52b', '/img/po-parkety.jpg').replace('{{accent}}', '#8a6a3f')
    return out

if __name__ == '__main__':
    target = sys.argv[1]
    if target == 'design':
        src = open(DESIGN + '/Main.dc.html', encoding='utf-8').read()
        open(DESIGN + '/Kontakty.dc.html', 'w', encoding='utf-8').write(page('kontakty', src, 'design'))
        open(DESIGN + '/O-nas.dc.html', 'w', encoding='utf-8').write(page('onas', src, 'design'))
        import landing
        for k in LANDS: open(DESIGN + '/' + landing.CONF[k]['design'] + '.dc.html', 'w', encoding='utf-8').write(page(k, src, 'design'))
    else:
        src = open(STATIC + '/index.html', encoding='utf-8').read()
        import landing
        for k, d in [('kontakty', 'kontakty'), ('onas', 'o-nas')] + [(k, landing.CONF[k]['slug']) for k in LANDS]:
            os.makedirs(STATIC + '/' + d, exist_ok=True)
            open(STATIC + '/' + d + '/index.html', 'w', encoding='utf-8').write(page(k, src, 'static'))
    print('ok')
