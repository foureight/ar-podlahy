# Vygeneruje site/llms.txt z aktuálních dat landing pages
import sys
sys.path.insert(0, '/home/claude/work/build')
import landing, pages
B = 'https://www.ar-podlahy.cz'
L = ['# AR podlahy', '',
'> Pokládka a renovace dřevěných podlah, parket, vinylu, PVC a koberců v Praze a Středočeském kraji od roku 1990. Rodinná firma se vzorkovnou v Praze-Radotíně.', '',
'## Základní fakta',
'- Název: AR podlahy',
'- Založeno: květen 1990, zakladatel Aleš Sebastianides; ve firmě působí i Lukáš Sebastianides',
'- Vzorkovna: Karlická 834/10, 153 00 Praha 16 – Radotín',
'- Otevírací doba vzorkovny: út 10–17, st–čt 10–19, pá 10–12',
'- Telefon: +420 605 257 236',
'- E-mail: info@ar-podlahy.cz, poptávky: poptavka@ar-podlahy.cz',
'- IČO 12584878, DIČ CZ5906111046',
'- Oblast působnosti: Praha a Středočeský kraj',
'- Tým: 13 stálých podlahářů; přes 1 000 000 m² podlah; přes 280 zakázek pro stát a samosprávy',
'- Záruka až 12 let na materiál, 24 měsíců na práci',
'- Montáž podlahy o 100 m² do 7 pracovních dní včetně přípravy podkladu; materiál na objednávku celkem do 6 týdnů',
'- Zaměření zdarma do 48 hodin, vzorky přivezeme s sebou',
'- Sada na údržbu zdarma u zakázek nad 100 m²',
'- Reference: Staroměstská radnice, Apoštolská nunciatura, Ministerstvo pro místní rozvoj, Kramářova vila, Goethe-Institut, Národní muzeum, Úřad vlády, Pražský hrad, Hlavní město Praha, AC Sparta Praha, obytný komplex Gutova (31 725 m²)',
'- Google recenze: https://www.google.com/maps?cid=7053343600020491698', '',
'## Ceny (bez DPH)',
'- Masivní dřevěná podlaha: materiál od 1 595 Kč/m², pokládka lepená od 295 Kč/m²',
'- Vícevrstvá dřevěná podlaha: materiál od 933 Kč/m², pokládka plovoucí od 249 Kč/m², lepená od 269 Kč/m²',
'- Parkety: materiál od 585 Kč/m², pokládka 399–429 Kč/m²; renovace parket od 600 Kč/m²',
'- Vinyl: lepený od 410 Kč/m² (pokládka 230 Kč/m²), zámkový od 799 Kč/m² (pokládka 180 Kč/m²)',
'- PVC: od 330 Kč/m², pokládka od 150 Kč/m²',
'- Koberce: od 154 Kč/m², pokládka od 228 Kč/m²',
'- Laminátové podlahy: od 499 Kč/m²',
'- Korkové podlahy: na dotaz (minimální prodej)',
'- Terasy: montáž včetně podkladní konstrukce od 850 Kč/m² bez materiálu',
'- Lité epoxidové a polyuretanové stěrky: přibližně 900–2 500 Kč/m²',
'- Historické podlahy: individuálně',
'- Penetrace podkladu od 25 Kč/m², samonivelační stěrka (5 mm) od 250 Kč/m², lišty od 59 Kč/bm',
'- Lepidlo u lepených podlah (dřevo, parkety, vinyl, PVC, bytové i zátěžové koberce): 95 Kč/m²; tekutá fixace kobercových čtverců: 75 Kč/m²',
'- Interiérové dveře od 3 940 Kč, zárubeň od 3 200 Kč, montáž od 1 600 Kč',
'- Vchodové dveře od 39 550 Kč, montáž individuálně', '',
'## Služby']
for k in pages.LANDS:
    c = landing.CONF[k]
    L.append(f"- [{c['crumb']}]({B}/{c['slug']}/): {c['desc']}")
L += ['', '## Firma', f'- [O nás]({B}/o-nas/): příběh firmy od roku 1990, tým a reference', f'- [Kontakty]({B}/kontakty/): telefon, e-mail, vzorkovna a mapa', '',
'## Časté dotazy',
'- Kolik stojí pokládka dřevěné podlahy? Vícevrstvá plovoucí 249 Kč/m², lepená 269 Kč/m², masiv lepený 295 Kč/m², parkety 399–429 Kč/m² (bez DPH).',
'- Jak rychle položíte podlahu? 100 m² do 7 pracovních dní včetně přípravy podkladu.',
'- Jakou dáváte záruku? Až 12 let na materiál, 24 měsíců na práci.',
'- Přijedete se zaměřením? Ano, zdarma do 48 hodin a se vzorky.', '']
open('/home/claude/ar-podlahy/site/llms.txt', 'w', encoding='utf-8').write('\n'.join(L))
print('llms ok')

# Strojově čitelný ceník a přehled služeb (pro AI a vyhledávače)
import json, datetime
svc = []
for k in pages.LANDS:
    c = landing.CONF[k]
    rows = []
    for r in (c.get('calc') or []):
        r = tuple(r) + (0,) * (5 - len(r))
        t, m, l, f, g = r
        rows.append({k2: v for k2, v in {'polozka': t, 'material_od_kc_m2': m or None, 'pokladka_od_kc_m2': l or None, 'lepidlo_kc_m2': g or None}.items() if v})
    svc.append({'sluzba': c['service'], 'url': f"{B}/{c['slug']}/", 'popis': c['desc'], 'cena_od': c.get('minprice') or None, 'kalkulace': rows or None, 'poznamka': c.get('note')})
data = {
  'firma': 'AR podlahy', 'web': B + '/', 'zalozeno': '1990-05', 'telefon': '+420605257236', 'email': 'info@ar-podlahy.cz', 'poptavky': 'poptavka@ar-podlahy.cz',
  'adresa': 'Karlická 834/10, 153 00 Praha 16 – Radotín', 'ico': '12584878', 'dic': 'CZ5906111046', 'oblast': ['Praha', 'Středočeský kraj'],
  'oteviraci_doba': {'út': '10–17', 'st': '10–19', 'čt': '10–19', 'pá': '10–12'},
  'zaruka': 'až 12 let na materiál, 24 měsíců na práci', 'termin': 'montáž 100 m² do 7 pracovních dní', 'zamereni': 'zdarma do 48 hodin',
  'prorez_procent': 15, 'stěrka_kc_m2_5mm': 250, 'listy_od_kc_bm': 59, 'ceny': 'bez DPH',
  'aktualizovano': datetime.date.today().isoformat(), 'sluzby': svc}
open('/home/claude/ar-podlahy/site/cenik.json', 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, indent=2))
s = open('/home/claude/ar-podlahy/site/llms.txt', encoding='utf-8').read()
if 'cenik.json' not in s:
    s = s.replace('## Firma', f'## Data\n- [Ceník a služby v JSON]({B}/cenik.json): strojově čitelný přehled cen a služeb\n\n## Firma', 1)
    open('/home/claude/ar-podlahy/site/llms.txt', 'w', encoding='utf-8').write(s)
print('cenik ok')
