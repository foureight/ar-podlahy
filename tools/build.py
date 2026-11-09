import re,json,subprocess,html,shutil,os,sys
SRC=sys.argv[1]; OUT='site'
s=open(SRC,encoding='utf-8').read()
data=json.loads(subprocess.check_output(['node','getdata.js',SRC]))
B={'c02164ac96a8a81afbb8f064858666f7':'logo-white.png','0275d72697c972c8689368790242b52b':'po-parkety.jpg','66deb1feb22b4f44dab92d591625951f':'pred-parkety.jpg','66ac4308aa49862928b30dc823cca5f8':'nunciatura-1.jpg','a2890fa689dbd13f790bca041350895a':'nunciatura-2.jpg','23cf9375a76a7babda1e611906e080ed':'nunciatura-3.jpg','e4393400253fecc200937215c67813fe':'nunciatura-budova.jpg','27288c1abe1664a724e15f614fbf6c25':'ref-prazsky-hrad.jpg','26c18642d9614617608a571fe31a65c2':'ref-kramarova-vila.jpg','7da54f6bdfc063aa6c80facd6b1e189f':'ref-urad-vlady.jpg'}
head=s[s.index('<head>')+6:s.index('</head>')].replace('<script src="./support.js"></script>\n','')
helmet=s[s.index('<helmet>')+8:s.index('</helmet>')]
body=s[s.index('</helmet>')+9:s.index('</x-dc>')]
def loop(m):
    lst=data[re.search(r'\{\{(\w+)\}\}',m.group(1)).group(1)]; var=m.group(2); tpl=m.group(3)
    return ''.join(re.sub(r'\{\{\s*'+var+r'\.(\w+)\s*\}\}',lambda x:html.escape(str(it[x.group(1)])),tpl) for it in lst)
body=re.sub(r'<sc-for list="([^"]+)" as="(\w+)"[^>]*>(.*?)</sc-for>',loop,body,flags=re.S)
page=head+helmet
page='<!doctype html>\n<html lang="cs">\n<head>\n'+page+'\n</head>\n<body>\n'+body
page=page.replace('{{accent}}',data['accent'])
assert '{{' not in page, re.findall(r'\{\{[^}]*\}\}',page)[:5]
for k,v in B.items(): page=page.replace('/_blob/'+k,'/img/'+v)
assert '/_blob/' not in page
page=page.replace('https://www.ar-podlahy.cz/[CESTA-K-FOTCE]/po-parkety.jpg','https://www.ar-podlahy.cz/img/po-parkety.jpg').replace('https://www.ar-podlahy.cz/[CESTA-K-LOGU]/logo.png','https://www.ar-podlahy.cz/img/logo-white.png')
# working mobile menu: burger toggles overlay
menu='''<div id="mmenu" hidden style="position:fixed;inset:0;z-index:50;background:#0e0e0e;color:#fff;font-family:'Montserrat',system-ui,sans-serif;display:flex;flex-direction:column;overflow:auto">
<div style="padding:20px 24px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(255,255,255,.12)"><img src="/img/logo-white.png" alt="AR podlahy" style="height:30px;width:auto"><button id="mclose" aria-label="Zavřít menu" style="width:44px;height:44px;border:1px solid rgba(255,255,255,.3);border-radius:6px;background:transparent;color:#fff;display:flex;align-items:center;justify-content:center"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"></path></svg></button></div>
<nav aria-label="Mobilní menu" class="mnav" style="padding:12px 24px;display:flex;flex-direction:column">
<a href="/">Úvod &amp; reference</a><a href="#">Podlahy</a><a href="#">Dveře</a><a href="#">Produkty &amp; služby</a><a href="#">Projekty</a><a href="#">Blog o podlahách</a><a href="#">O nás</a><a href="#">Kontakty</a></nav>
<div style="padding:20px 24px 32px;display:flex;flex-direction:column;gap:12px"><a href="#poptavka" class="mcta" style="background:#8a6a3f;color:#fff;text-align:center;padding:17px;border-radius:8px;font-weight:800;text-decoration:none">Chci konzultaci a nabídku</a><a href="tel:+420605257236" style="border:1px solid rgba(255,255,255,.4);color:#fff;text-align:center;padding:16px;border-radius:8px;font-weight:700;text-decoration:none">Zavolat +420 605 257 236</a></div></div>
<style>.mnav a{padding:16px 0;border-bottom:1px solid rgba(255,255,255,.1);font-size:19px;font-weight:800;color:#fff;text-decoration:none}#mmenu[hidden]{display:none !important}</style>
<script>
(function(){var m=document.getElementById('mmenu'),b=document.querySelector('.burger');
function o(){m.hidden=false;document.body.style.overflow='hidden'}function c(){m.hidden=true;document.body.style.overflow=''}
if(b){b.addEventListener('click',o)}document.getElementById('mclose').addEventListener('click',c);
m.querySelectorAll('a').forEach(function(a){a.addEventListener('click',c)});
document.addEventListener('keydown',function(e){if(e.key==='Escape')c()});})();
</script>'''
page=page+menu+'\n</body>\n</html>\n'
os.makedirs(OUT+'/img',exist_ok=True)
open(OUT+'/index.html','w',encoding='utf-8').write(page)
for v in B.values(): shutil.copy('../web/img/'+v,OUT+'/img/'+v)
print('ok',len(page))
