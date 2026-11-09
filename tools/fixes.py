import re, sys
SP = '/tmp/claude-0/-home-claude/a1dc3947-88ac-503c-910c-cbe14d93fb1b/scratchpad'
FILES = [SP + '/web/project/Main.dc.html', SP + '/web/project/Mobil-1.dc.html', SP + '/web/project/Mobil-2.dc.html',
         SP + '/web/project/Mobil-menu.dc.html', '/home/claude/ar-podlahy/site/index.html']
FB = 'https://www.facebook.com/Podlahy-Praha-349586465068872/'

SIMPLE = [
    ('záruka na materiál až 12 let', 'záruka na materiál 6 let'),
    ('na materiál dáváme záruku až 12 let', 'na materiál dáváme záruku 6 let'),
    ('Na materiál až 12 let podle výrobce, na naši práci 24 měsíců', 'Na materiál 6 let, na naši práci 24 měsíců'),
    ('>Až 12 let<', '>6 let<'),
    ('"sameAs": ["https://www.facebook.com/[PROFIL]"]', '"sameAs": ["%s"]' % FB),
    ('"taxID": "12584878",', '"taxID": "12584878",\n      "vatID": "CZ5906111046",'),
    # services data (design)
    ("text: 'Lepený i zámkový vinyl, PVC v rolích. Podklad vyrovnáme samonivelační stěrkou.'", "text: 'Vinylové dílce Thermofix, Fatraclic a Imperio, PVC v rolích Novilon. Podklad vyrovnáme samonivelační stěrkou.'"),
    ("text: 'Dveře a zárubně sladěné s podlahou, včetně montáže a obložek.'", "text: 'Rámové dveře STILE z plného masivu, povrchy Greko a CPL. Zárubně a obložky sladěné s podlahou, včetně montáže.'"),
    # services rendered (static)
    ('Lepený i zámkový vinyl, PVC v rolích. Podklad vyrovnáme samonivelační stěrkou.', 'Vinylové dílce Thermofix, Fatraclic a Imperio, PVC v rolích Novilon. Podklad vyrovnáme samonivelační stěrkou.'),
    ('Dveře a zárubně sladěné s podlahou, včetně montáže a obložek.', 'Rámové dveře STILE z plného masivu, povrchy Greko a CPL. Zárubně a obložky sladěné s podlahou, včetně montáže.'),
    ('<span>IČO 125 848 78</span>', '<span>IČO 125 848 78 · DIČ CZ5906111046</span>'),
]
PRICES = ['od 569 Kč/m²', 'cena po zaměření', 'od 330 Kč/m²', 'cena dle katalogu', 'cena po zaměření']

CHECK = '<li style="display: flex; gap: 10px; align-items: center;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#c9a46a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5 9-10"></path></svg>'
HERO_OLD = CHECK + 'Vzorky přivezeme až k vám domů</li>'
HERO_NEW = HERO_OLD + '\n' + CHECK + 'Od poptávky po montáž do 6 týdnů</li>'

FLOORS = ['Dřevěné podlahy', 'Vinylové a PVC podlahy', 'Parkety', 'Renovace a broušení parket', 'Historické podlahy',
          'Laminátové podlahy', 'Korkové podlahy', 'Koberce', 'Lité epoxidové stěrky', 'Terasy', 'Příprava podkladu']
DOORS = ['Interiérové dveře', 'Vchodové dveře']
STAVBY = ['Rekonstrukce a stavby na klíč']

DD_OLD_RE = r'<div class="ddm"><div>.*?</div></div></div>'
def dd_new():
    lab = '<span class="ddl">{}</span>'
    c1 = lab.format('Podlahy') + ''.join(f'<a href="#">{x}</a>' for x in FLOORS)
    c2 = lab.format('Dveře') + ''.join(f'<a href="#">{x}</a>' for x in DOORS) + lab.format('Stavby') + ''.join(f'<a href="#">{x}</a>' for x in STAVBY)
    return f'<div class="ddm"><div><div class="ddc">{c1}</div><div class="ddc">{c2}</div></div></div></div>'
DD_CSS_OLD = '.ddm>div{background:#141414;border:1px solid rgba(255,255,255,.14);border-radius:8px;padding:8px;display:flex;flex-direction:column;'
DD_CSS_NEW = '.ddc{display:flex;flex-direction:column;min-width:230px}.ddc~.ddc{border-left:1px solid rgba(255,255,255,.1);padding-left:8px}.ddc .ddl~.ddl{margin-top:6px;border-top:1px solid rgba(255,255,255,.1);padding-top:12px}.ddm>div{background:#141414;border:1px solid rgba(255,255,255,.14);border-radius:8px;padding:8px;display:flex;flex-direction:row;gap:8px;'

def mobile_menu(s, sub_style, lab_style, wrap_re):
    m = re.search(wrap_re, s, re.S)
    if not m: return s, 0
    old = m.group(0)
    head = old[:old.index('>') + 1]
    lab = lambda t: f'<span style="{lab_style}">{t}</span>'
    items = lambda L: ''.join(f'<a href="#" style="{sub_style}">{x}</a>' for x in L)
    new = head + lab('Podlahy') + items(FLOORS) + lab('Dveře') + items(DOORS) + lab('Stavby') + items(STAVBY) + '</div>'
    return s.replace(old, new), 1

FORM_FIELDS_OLD_RE = r'<label style="display: flex; flex-direction: column; gap: 8px; font-size: 14px; font-weight: 700;">Mám zájem o<select.*?</label>\n<label style="display: flex; flex-direction: column; gap: 8px; font-size: 14px; font-weight: 700; grid-column: 1 / -1;">Zpráva \(plocha, místo, termín\)<textarea.*?</label>'
L = 'display: flex; flex-direction: column; gap: 8px; font-size: 14px; font-weight: 700;'
INP = 'border: 1px solid #d6cdbf; border-radius: 8px; padding: 14px; font-size: 16px;'
SEL = INP + ' background: #fff;'
FORM_NEW = '\n'.join([
    f'<label style="{L}">Lokalita<input type="text" name="lokalita" placeholder="např. Praha 5" style="{INP}"></label>',
    f'<label style="{L}">Plocha v m² / odhad<input type="text" name="plocha" inputmode="decimal" style="{INP}"></label>',
    f'<label style="{L}">Typ podlahy<select name="typ" style="{SEL}"><option>Dřevěná vícevrstvá podlaha</option><option>Parkety</option><option>Renovace parket</option><option>Vinyl</option><option>Laminátová podlaha</option><option>Koberec</option><option>Litá epoxidová stěrka</option><option>Potřebuji poradit s technickým řešením</option></select></label>',
    f'<label style="{L}">Schody<select name="schody" style="{SEL}"><option>Ne</option><option>Ano</option></select></label>',
    f'<label style="{L}">Dveře<select name="dvere" style="{SEL}"><option>Ne</option><option>Interiérové</option><option>Vchodové</option><option>Interiérové i vchodové</option></select></label>',
    f'<label style="{L}">Chci<select name="zajem" style="{SEL}"><option>Konzultaci a zaměření</option><option>Cenovou nabídku</option></select></label>',
    f'<label style="{L} grid-column: 1 / -1;">Stav podkladu a zpráva (termín, přání)<textarea name="zprava" rows="3" style="{INP} resize: vertical;"></textarea></label>',
])

def apply(s, f):
    log = []
    for a, b in SIMPLE:
        n = s.count(a)
        if n: s = s.replace(a, b); log.append((a[:30], n))
    # prices
    if "price: 'od [CENA]" in s:
        i = 0
        def rp(m):
            nonlocal i; v = PRICES[i]; i += 1; return f"price: '{v}'"
        s = re.sub(r"price: 'od \[CENA\] Kč/(?:m²|ks)'", rp, s); log.append(('price-data', i))
    elif 'od [CENA] Kč/' in s:
        i = 0
        def rp2(m):
            nonlocal i; v = PRICES[i]; i += 1; return v
        s = re.sub(r'od \[CENA\] Kč/(?:m²|ks)', rp2, s); log.append(('price-static', i))
    if HERO_OLD in s and 'do 6 týdnů</li>' not in s:
        s = s.replace(HERO_OLD, HERO_NEW); log.append(('hero', 1))
    if re.search(DD_OLD_RE, s, re.S):
        s = re.sub(DD_OLD_RE, lambda m: dd_new(), s, count=1, flags=re.S); log.append(('dd', 1))
    if DD_CSS_OLD in s:
        s = s.replace(DD_CSS_OLD, DD_CSS_NEW); log.append(('ddcss', 1))
    if re.search(FORM_FIELDS_OLD_RE, s, re.S):
        s = re.sub(FORM_FIELDS_OLD_RE, lambda m: FORM_NEW, s, flags=re.S); log.append(('form', 1))
    # design mobile menu
    s, n = mobile_menu(s, 'padding: 9px 0 9px 16px; font-size: 15px; font-weight: 600; color: rgba(255,255,255,.8);',
                       'padding: 10px 0 4px 16px; font-size: 11px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: #c9a46a;',
                       r'<div style="display: flex; flex-direction: column; border-bottom: 1px solid rgba\(255,255,255,.1\); padding-bottom: 8px; border-left: 2px solid #c9a46a; margin-left: 2px;">.*?</div>')
    if n: log.append(('mmenu-design', n))
    s, n = mobile_menu(s, 'padding:9px 0 9px 16px;font-size:15px;font-weight:600;color:rgba(255,255,255,.8);border:0',
                       'padding:10px 0 4px 16px;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#c9a46a',
                       r'<div style="display:flex;flex-direction:column;border-bottom:1px solid rgba\(255,255,255,.1\);padding-bottom:8px;border-left[^>]*>.*?</div>')
    if n: log.append(('mmenu-static', n))
    # offer catalog
    s = re.sub(r'"hasOfferCatalog": \{.*?\n      \},', lambda m: OFFERS, s, count=1, flags=re.S)
    return s, log

def off(name, price=None):
    o = {"@type": "Offer", "itemOffered": {"@type": "Service", "name": name}}
    if price: o["priceSpecification"] = {"@type": "UnitPriceSpecification", "minPrice": price, "priceCurrency": "CZK", "unitText": "m²"}
    import json
    return '          ' + json.dumps(o, ensure_ascii=False)
OFFERS = '"hasOfferCatalog": {\n        "@type": "OfferCatalog",\n        "name": "Podlahy, dveře a rekonstrukce",\n        "itemListElement": [\n' + ',\n'.join([
    off('Dřevěné vícevrstvé podlahy a parkety', 569), off('Renovace a broušení parket'), off('PVC v rolích Novilon', 330),
    off('Vinylové dílce Thermofix, Fatraclic, Imperio', 482), off('Laminátové podlahy Haro, Egger', 223), off('Korkové podlahy Haro', 662),
    off('Koberce v rolích a čtvercích', 154), off('Terasy WPC, exotika, jehličnany', 399), off('Lité epoxidové stěrky'),
    off('Interiérové a vchodové dveře'), off('Příprava podkladu a stěrky'), off('Renovace historických podlah'), off('Rekonstrukce a stavby na klíč')]) + '\n        ]\n      },'

if __name__ == '__main__':
    for f in FILES:
        s = open(f, encoding='utf-8').read()
        s2, log = apply(s, f)
        open(f, 'w', encoding='utf-8').write(s2)
        print(f.split('/')[-1], log)
