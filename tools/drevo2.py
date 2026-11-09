# Zjednodušená landing page Dřevěné podlahy (podle zjednoduseni-drevene-podlahy.md)
import re
from pages import EYE, H2, P, WRAP, CARD, I_CHECK, sec

X = '[DOPLNIT]'
# cenik: material / pokladka Kč/m² (None = neznámé → doplnit)
TYPES = [
    # key, title, text, mat, lab, form value
    ('masiv', 'Masivní dřevěné podlahy', 'Poctivá prkna z masivu, nejčastěji dub. Celoplošně lepená vydrží generace, zvládnou i podlahové topení a dají se opakovaně brousit.', None, None, 'Dřevěná podlaha – masiv'),
    ('vicevrstva', 'Vícevrstvé (třívrstvé) podlahy', 'Nášlapná vrstva z ušlechtilého dřeva na stabilním nosiči. Rychlá pokládka, stabilní rozměr a ideální volba na podlahové topení.', 569, None, 'Dřevěná vícevrstvá podlaha'),
    ('parkety', 'Parkety a historické vzory', 'Vlysy, rybí kost, mozaika i vídeňské a benátské čtverce. Zkušenost z památek, jako je Apoštolská nunciatura.', 569, None, 'Parkety'),
    ('renovace', 'Renovace parket', 'Broušení, tmelení spar, doplnění dílců a nový lak nebo olej. Stará podlaha pak vypadá jako nová.', 0, None, 'Renovace parket'),
]
def price_line(key, mat, lab):
    if key == 'renovace':
        return f'od {lab if lab else X} Kč/m²'
    if key == 'parkety':
        return f'materiál od {mat} Kč/m² · historické vzory individuálně'
    return f'materiál {"od " + str(mat) if mat else X} · pokládka {"od " + str(lab) if lab else X} Kč/m²'

FAQ = [
    ('Kolik stojí dřevěná podlaha v Praze?', 'Materiál – vícevrstvé podlahy a parkety – začíná od 569 Kč/m². Cena pokládky záleží na stavu podkladu, způsobu pokládky a povrchové úpravě. Po bezplatném zaměření dostanete pevnou cenu.'),
    ('Co zahrnuje zaměření zdarma?', 'Přijedeme do 48 hodin, přivezeme vzorky, změříme vlhkost podkladu a skutečné metry. Teprve pak počítáme cenu.'),
    ('Lze dát masivní dřevo na podlahové topení?', 'Ano, když víte jak. Často slyšíte, že na podlahové topení patří jen třívrstvá podlaha. V praxi rozhoduje stabilní dřevina a vhodný poměr šíře a tloušťky prkna, změřená vlhkost a vytopený potěr podle protokolu a celoplošné lepení bez vzduchové mezery pro dobrý prostup tepla. Ve vile v Černošicích leží 245 m² masivního dubu na vodním podlahovém topení a funguje bez prasklin.'),
    ('Jak dlouho trvá pokládka dřevěné podlahy?', 'Od poptávky po montáž obvykle do 6 týdnů. Samotná pokládka bytu trvá několik dní, dvoupodlažní vilu s 245 m² masivu jsme dokončili za 14 dní včetně vytvrzení laku.'),
    ('Jezdíte i mimo Prahu?', 'Ano, pokládáme po celé Praze a ve Středočeském kraji. Showroom máme v Radotíně, takže jsme rychle třeba v Černošicích, Dobřichovicích, Řevnicích nebo na Berounsku.'),
    ('Jakou dáváte záruku?', 'Na materiál 6 let, na naši práci 24 měsíců. Ke každé realizaci přidáme sadu na údržbu podlahy zdarma.'),
]

def hero(crumb, L):
    li = lambda t: f'<li style="display: flex; gap: 10px; align-items: center;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#c9a46a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5 9-10"></path></svg>{t}</li>'
    bullets = li('Zaměření zdarma do 48 hodin') + li(f'Materiál od 569 Kč/m², pokládka od {X} Kč/m²') + li('Záruka 6 let na materiál, 24 měsíců na práci')
    return f'''<div style="max-width: 1240px; margin: 0 auto; padding: clamp(36px, 5vw, 64px) 24px clamp(40px, 5vw, 64px); display: flex; flex-direction: column; gap: 20px; align-items: flex-start;">
<nav aria-label="Drobečková navigace" style="font-size: 13px; color: rgba(255,255,255,.65);"><a href="{L["home"]}" style="color: rgba(255,255,255,.8);">Úvod</a> <span aria-hidden="true">/</span> <span aria-current="page">{crumb}</span></nav>
<h1 style="margin: 0; font-size: clamp(34px, 4.8vw, 64px); line-height: 1.06; font-weight: 900; letter-spacing: -.02em; max-width: 900px;">Dřevěné podlahy v Praze a Středočeském kraji</h1>
<p style="margin: 0; font-size: clamp(17px, 1.5vw, 21px); line-height: 1.5; color: rgba(255,255,255,.88); max-width: 700px; font-weight: 600;">Masivní, vícevrstvé podlahy i parkety, které vydrží generace.</p>
<ul style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 16px; color: rgba(255,255,255,.88);">{bullets}</ul>
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

def types_section():
    cards = ''.join(f'<div style="{CARD}"><strong style="font-size: 19px;">{t}</strong><p style="margin: 0; font-size: 15px; line-height: 1.65; color: #4a443b;">{d}</p><span style="margin-top: auto; padding-top: 6px; font-size: 14px; font-weight: 800; color: #8a6a3f;">{price_line(k, m, l)}</span></div>' for k, t, d, m, l, _ in TYPES)
    return f'''<!-- CO POKLÁDÁME -->
<section style="{WRAP} display: flex; flex-direction: column; gap: 28px;">
<div style="max-width: 760px; display: flex; flex-direction: column; gap: 12px;"><span style="{EYE}">Co pokládáme</span><h2 style="{H2}">Dřevěná podlaha pro byt, dům i památku</h2></div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">{cards}</div>
</section>

'''

def calc_section():
    opts = ''.join(f'<option value="{k}" data-mat="{m or ""}" data-lab="{l or ""}" data-form="{f}"{" selected" if k == "vicevrstva" else ""}>{t}</option>' for k, t, d, m, l, f in TYPES)
    INP = 'border: 1px solid #d6cdbf; border-radius: 8px; padding: 14px; font-size: 16px; background: #fff; width: 100%; box-sizing: border-box;'
    LB = 'display: flex; flex-direction: column; gap: 8px; font-size: 14px; font-weight: 700;'
    ROW = 'display: flex; justify-content: space-between; gap: 12px; font-size: 15px;'
    return f'''<!-- KALKULAČKA -->
<section id="kalkulacka" style="background: #1a1a1a; color: #fff;">
<div style="{WRAP} display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px 64px; align-items: center;">
<div style="display: flex; flex-direction: column; gap: 14px;">
<span style="font-size: 13px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; color: #c9a46a;">Kalkulačka</span>
<h2 style="margin: 0; font-size: clamp(30px, 3.4vw, 46px); line-height: 1.1; font-weight: 900;">Spočítejte si orientační cenu</h2>
<p style="margin: 0; font-size: 17px; line-height: 1.7; color: rgba(255,255,255,.78);">Vyberte druh podlahy a zadejte plochu. Pevnou cenu dostanete po bezplatném zaměření.</p>
</div>
<form id="calc" onsubmit="return false" style="background: #fff; color: #1a1a1a; border-radius: 18px; padding: clamp(22px, 3vw, 34px); display: flex; flex-direction: column; gap: 16px;">
<label style="{LB}">Druh podlahy<select id="calc-typ" style="{INP}">{opts}</select></label>
<label style="{LB}">Čistá plocha v m²<input id="calc-m2" type="number" min="1" step="1" value="50" inputmode="numeric" style="{INP}"></label>
<div style="background: #f5f1ea; border-radius: 12px; padding: 18px 20px; display: flex; flex-direction: column; gap: 8px;">
<div style="{ROW}"><span>Materiál <small id="calc-mat-d" style="color: #6b655b;">(54 m² s prořezem 8 %)</small></span><strong id="calc-mat">30 726 Kč</strong></div>
<div style="{ROW}"><span>Pokládka <small id="calc-lab-d" style="color: #6b655b;">(50 m²)</small></span><strong id="calc-lab">po zaměření</strong></div>
<div style="{ROW} border-top: 1px solid #e0d6c6; padding-top: 10px; font-size: 18px;"><span style="font-weight: 800;">Celkem orientačně</span><strong id="calc-total" style="font-size: 22px; font-weight: 900;">od 30 726 Kč</strong></div>
</div>
<a id="calc-cta" href="#poptavka" style="background: #8a6a3f; color: #fff; text-align: center; text-decoration: none; padding: 16px; border-radius: 8px; font-weight: 800; font-size: 16px;">Chci přesnou nabídku</a>
</form>
</div>
</section>

'''

def refs_section(src):
    st = sec(src, 'PŘÍPADOVÉ STUDIE', 'GARANCE')
    st = re.sub(r'<a href="#" style="color: #1a1a1a; font-weight: 800; font-size: 15px;">Celá případová studie →</a>', '', st)
    line = '<p style="margin: 0; font-size: 17px; line-height: 1.6; color: #3d3830; font-weight: 600;">Pracovali jsme také pro Úřad vlády, Kramářovu vilu, Pražský hrad a ministerstva.</p>'
    i = st.rindex('</section>')
    return st[:i] + line + '\n' + st[i:]

def promise_section():
    pts = [('Záruka 6 let', 'na materiál a 24 měsíců na naši práci'), ('Do 6 týdnů', 'od poptávky po hotovou podlahu'),
           ('Pevná cena', 'po zaměření – bez překvapení na konci'), ('Úklid po práci', 'předáme čisté a hotové')]
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

def faq_section():
    faq = ''.join(f'<details style="border-bottom: 1px solid #e4ddd2; padding: 16px 0;"><summary style="display: flex; justify-content: space-between; gap: 20px; align-items: center; font-size: 17px; font-weight: 700; min-height: 44px; cursor: pointer;">{q}<span class="plus" style="font-size: 26px; color: #8a6a3f; font-weight: 400;">+</span></summary><p style="margin: 10px 0 0; font-size: 16px; line-height: 1.7; color: #5b554c;">{a}</p></details>' for q, a in FAQ)
    return f'''<!-- FAQ DŘEVO -->
<section style="background: #fff; border-top: 1px solid #e4ddd2;">
<div style="max-width: 1240px; margin: 0 auto; padding: clamp(48px, 6vw, 80px) 24px; display: flex; flex-direction: column; gap: 14px;">
<span style="{EYE}">Časté dotazy</span>
<h2 style="{H2} margin-bottom: 6px;">Dřevěné podlahy – na co se ptáte</h2>
{faq}
</div>
</section>

'''

def form_section():
    L = 'display: flex; flex-direction: column; gap: 8px; font-size: 14px; font-weight: 700;'
    I = 'border: 1px solid #d6cdbf; border-radius: 8px; padding: 14px; font-size: 16px;'
    return f'''<!-- POPTÁVKA -->
<section id="poptavka" class="hero" style="color: #fff;">
<div style="max-width: 1240px; margin: 0 auto; padding: clamp(48px, 6vw, 80px) 24px; display: flex; flex-wrap: wrap; gap: 40px; align-items: flex-start;">
<div style="flex: 1 1 340px; display: flex; flex-direction: column; gap: 16px; min-width: 0;">
<span style="font-size: 13px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; color: #c9a46a;">Zaměření zdarma do 48 hodin</span>
<h2 style="margin: 0; font-size: clamp(30px, 3.4vw, 48px); line-height: 1.08; font-weight: 900;">Chci nabídku na dřevěnou podlahu</h2>
<p style="margin: 0; font-size: 17px; line-height: 1.65; color: rgba(255,255,255,.8);">Stačí jméno a telefon. Zavoláme vám, doptáme se na detaily a domluvíme zaměření.</p>
<a href="tel:+420605257236" style="color: #fff; font-weight: 800; font-size: 22px; text-decoration: none;">+420 605 257 236</a>
</div>
<form id="poptavka-form" method="post" action="" style="flex: 999 1 480px; background: #fff; color: #1a1a1a; border-radius: 18px; padding: clamp(22px, 3vw, 36px); display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; box-sizing: border-box; min-width: 0;">
<label style="{L}">Jméno a příjmení<input type="text" name="jmeno" autocomplete="name" style="{I}"></label>
<label style="{L}">Telefon *<input type="tel" name="telefon" autocomplete="tel" required style="{I}"></label>
<label style="{L}">E-mail<input type="email" name="email" autocomplete="email" style="{I}"></label>
<label style="{L}">Lokalita<input type="text" name="lokalita" placeholder="např. Praha 5" style="{I}"></label>
<label style="{L} grid-column: 1 / -1;">Zpráva (nepovinné)<textarea name="zprava" rows="3" style="{I} resize: vertical;"></textarea></label>
<input type="hidden" name="typ" value=""><input type="hidden" name="plocha" value=""><input type="hidden" name="zdroj" value="landing-drevene-podlahy">
<button type="submit" style="grid-column: 1 / -1; background: {{{{accent}}}}; color: #fff; border: 0; border-radius: 8px; padding: 17px; font-size: 17px; font-weight: 800; cursor: pointer;">Odeslat – ozveme se do 48 hodin</button>
<p id="poptavka-stav" role="status" style="grid-column: 1 / -1; margin: 0; font-size: 13px; line-height: 1.5; color: #6b655b;">Odesláním souhlasíte se zpracováním osobních údajů za účelem vyřízení poptávky. <a href="#" style="color: #8a6a3f;">Zásady ochrany osobních údajů</a></p>
</form>
</div>
</section>

<!-- MOBILNÍ LIŠTA -->
<div class="mbar" style="display: none; position: fixed; left: 0; right: 0; bottom: 0; z-index: 40; background: #0e0e0e; padding: 10px 12px calc(10px + env(safe-area-inset-bottom)); gap: 10px; box-shadow: 0 -6px 20px rgba(0,0,0,.25);"><a href="tel:+420605257236" style="flex: 1; text-align: center; border: 1px solid rgba(255,255,255,.4); color: #fff; text-decoration: none; padding: 14px; border-radius: 8px; font-weight: 800;">Zavolat</a><a href="#poptavka" style="flex: 1; text-align: center; background: #8a6a3f; color: #fff; text-decoration: none; padding: 14px; border-radius: 8px; font-weight: 800;">Nabídka</a></div>

'''

MBAR_CSS = '@media (max-width:700px){.mbar{display:flex !important}body{padding-bottom:72px}}'

# Endpoint pro odeslání formuláře – doplnit (např. Web3Forms / Formspree / vlastní funkce). Prázdné = otevře e-mail.
FORM_ENDPOINT = ''
JS = """<script>
(function(){
var t=document.getElementById('calc-typ'),m=document.getElementById('calc-m2');
function f(n){return Math.round(n).toLocaleString('cs-CZ')+' Kč'}
function u(){if(!t)return;var o=t.options[t.selectedIndex],a=Math.max(0,parseFloat(m.value)||0),mat=+o.getAttribute('data-mat')||0,lab=+o.getAttribute('data-lab')||0,q=Math.ceil(a*1.08);
var M=document.getElementById('calc-mat'),Md=document.getElementById('calc-mat-d'),La=document.getElementById('calc-lab'),Ld=document.getElementById('calc-lab-d'),T=document.getElementById('calc-total');
if(o.value==='renovace'){M.textContent='–';Md.textContent='(bez materiálu)'}else if(mat){M.textContent=f(q*mat);Md.textContent='('+q+' m² s prořezem 8 %)'}else{M.textContent='po zaměření';Md.textContent=''}
Ld.textContent='('+a+' m²)';La.textContent=lab?f(a*lab):'po zaměření';
var sum=(o.value==='renovace'?0:(mat?q*mat:0))+(lab?a*lab:0);T.textContent=sum?((mat||o.value==='renovace')&&lab?'':'od ')+f(sum):'po zaměření'}
if(t){[t,m].forEach(function(e){e.addEventListener('input',u);e.addEventListener('change',u)});u();
document.getElementById('calc-cta').addEventListener('click',function(){var F=document.getElementById('poptavka-form');F.typ.value=t.options[t.selectedIndex].getAttribute('data-form');F.plocha.value=m.value+' m²'})}
var F=document.getElementById('poptavka-form'),S=document.getElementById('poptavka-stav'),EP='__EP__';
if(F)F.addEventListener('submit',function(e){e.preventDefault();var d=new FormData(F);
if(EP){fetch(EP,{method:'POST',body:d,headers:{'Accept':'application/json'}}).then(function(r){if(!r.ok)throw 0;F.reset();S.textContent='Děkujeme, ozveme se do 48 hodin.'}).catch(function(){S.textContent='Odeslání se nepovedlo, zavolejte nám prosím na +420 605 257 236.'});return}
var b=[];d.forEach(function(v,k){if(v)b.push(k+': '+v)});location.href='mailto:info@ar-podlahy.cz?subject='+encodeURIComponent('Poptávka – dřevěná podlaha')+'&body='+encodeURIComponent(b.join('\\n'))});
})();
</script>""".replace('__EP__', FORM_ENDPOINT)

def build(src, L, crumb):
    body = types_section() + calc_section() + refs_section(src) + promise_section() + faq_section() + form_section()
    return hero(crumb, L), body
