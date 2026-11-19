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
'- Masivní dřevěná podlaha: materiál od 1 136 Kč/m², pokládka lepená od 295 Kč/m²',
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
