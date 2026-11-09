# SEO/GEO úpravy homepage (idempotentní): python3 seo.py <soubor.html> [--static]
import sys, re, json
f = sys.argv[1]; static = '--static' in sys.argv
s = open(f, encoding='utf-8').read()
MAPS = 'https://www.google.com/maps?cid=7053343600020491698'
ANS = {
 'Kolik stojí renovace parket za m²?': 'Renovace parket stojí od 600 Kč/m² bez DPH. Zahrnuje broušení, tmelení spar a tři vrstvy laku nebo olej. Konečná cena záleží na stavu parket a rozsahu oprav, přesnou pošleme po bezplatném zaměření.',
 'Jak dlouho trvá pokládka?': 'Podlahu o 100 m² položíme do 7 pracovních dní včetně přípravy podkladu. U materiálu na objednávku je celkový termín do 6 týdnů. Dvoupodlažní vilu s 245 m² masivu jsme dokončili za 14 dní včetně vytvrzení laku.',
}
NEW = [
 ('Kolik stojí pokládka dřevěné podlahy?', 'Práce na vícevrstvé plovoucí podlaze stojí 249 Kč/m² bez DPH, lepená 269 Kč/m², masivní lepená 295 Kč/m² a parkety 399–429 Kč/m². Přesnou cenu spočítáme po bezplatném zaměření.'),
 ('Jaké podlahy pokládáte?', 'Dřevěné podlahy (masiv i vícevrstvé), parkety, historické podlahy, vinyl, PVC a lino, koberce, laminát, korek, lité epoxidové stěrky a terasy. Děláme i přípravu podkladu a montáž interiérových a vchodových dveří.'),
 ('Kde pracujete?', 'V celé Praze a ve Středočeském kraji. Vzorkovna je na adrese Karlická 834/10, 153 00 Praha 16 – Radotín.'),
]
# viditelné FAQ
for q, a in ANS.items():
    s = re.sub(r'(%s<span class="plus".*?</summary>\s*<p[^>]*>)[^<]*' % re.escape(q), lambda m: m.group(1) + a, s, flags=re.S)
m = re.search(r'<details style="border-bottom[^>]*>\s*<summary[^>]*>Jakou dáváte záruku\?.*?</details>', s, flags=re.S)
tpl = m.group(0)
for q, a in NEW:
    if q in s: continue
    item = re.sub(r'(<summary[^>]*>)Jakou dáváte záruku\?', lambda x: x.group(1) + q, tpl)
    item = re.sub(r'(<p[^>]*>)[^<]*', lambda x: x.group(1) + a, item, count=1)
    end = s.index('</details>', s.index('Jakou dáváte záruku?')) + 10
    # vložit za poslední FAQ položku
    last = max(s.rfind('</details>', 0, s.index('<!-- POPTÁVKA -->')) + 10, end)
    s = s[:last] + '\n\n' + item + s[last:]
# JSON-LD (jen statický web)
if static:
    i = s.index('<script type="application/ld+json">') + len('<script type="application/ld+json">'); j = s.index('</script>', i)
    ld = json.loads(s[i:j])
    for n in ld['@graph']:
        if n['@type'] == 'HomeAndConstructionBusiness':
            n['description'] = 'Pokládka a renovace dřevěných podlah, parket, vinylu, PVC a koberců v Praze a Středočeském kraji od roku 1991. Zaměření zdarma do 48 hodin, montáž 100 m² do 7 pracovních dní, záruka až 12 let na materiál a 24 měsíců na práci. Reference: Úřad vlády, Kramářova vila, Pražský hrad.'
            n['hasMap'] = MAPS
            n['sameAs'] = sorted(set(n.get('sameAs', []) + [MAPS]))
        if n['@type'] == 'FAQPage':
            qs = re.findall(r'<summary[^>]*>([^<]*)<span class="plus".*?</summary>\s*<p[^>]*>([^<]*)', s[s.index('<!-- RECENZE + FAQ -->'):s.index('<!-- POPTÁVKA -->')], flags=re.S)
            n['mainEntity'] = [{"@type": "Question", "name": q.strip(), "acceptedAnswer": {"@type": "Answer", "text": a.strip()}} for q, a in qs]
    s = s[:i] + '\n' + json.dumps(ld, ensure_ascii=False, indent=2) + '\n' + s[j:]
    T = 'Podlahy Praha – pokládka a renovace od 1991 | AR podlahy'
    D = 'Pokládka dřevěných podlah, parket, vinylu, PVC a koberců v Praze a okolí. Zaměření zdarma do 48 hodin, záruka až 12 let. Vzorkovna v Radotíně.'
    s = re.sub(r'<title>.*?</title>', f'<title>{T}</title>', s, count=1)
    for k in ['name="description"', 'property="og:description"', 'name="twitter:description"']:
        s = re.sub(r'(<meta %s content=")[^"]*' % k, lambda m: m.group(1) + D, s)
    for k in ['property="og:title"', 'name="twitter:title"']:
        s = re.sub(r'(<meta %s content=")[^"]*' % k, lambda m: m.group(1) + T, s)
    s = s.replace('"name": "Pokládka dřevěných podlah a vinylu Praha | AR podlahy"', '"name": "%s"' % T)
open(f, 'w', encoding='utf-8').write(s)
print('ok', f)
