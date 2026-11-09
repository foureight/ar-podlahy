import re,sys
sys.path.insert(0,'/tmp/claude-0/-home-claude/a1dc3947-88ac-503c-910c-cbe14d93fb1b/scratchpad/build')
import pages
D=pages.DESIGN+'/'
m1=open(D+'Mobil-1.dc.html',encoding='utf-8').read(); m2=open(D+'Mobil-2.dc.html',encoding='utf-8').read()
h1=m1[m1.index('<style>'):m1.index('</style>')]; h2=m2[m2.index('<style>')+7:m2.index('</style>')]
extra=[l for l in h2.split('\n') if l.strip() and l not in h1]
cut=m1.rindex('</section>',0,m1.index('</x-dc>'))+10
merged=m1[:m1.index('<!-- PŘED / PO -->')]+m1[m1.index('<!-- PŘÍPADOVÉ STUDIE -->'):cut]+'\n\n'+m2[m2.index('<!-- GARANCE -->'):]
merged=merged.replace('</style>','\n'.join(extra)+'\n</style>',1)
import landing
H={**{"historicke": 7450, "laminat": 6200, "korek": 6200, "sterky": 5250, "terasy": 6550, "podklad": 6550, "dvere": 5350, "vchodove": 5300, "rekonstrukce": 7400},"kontakty":5700,"onas":7550,"drevo":8000,"parkety":8000,"vinyl":6300,"pvc":6550,"koberce":6550}
JOBS=[("kontakty","Kontakty-mobil.dc.html"),("onas","O-nas-mobil.dc.html")]+[(k,landing.CONF[k]["design"]+"-mobil.dc.html") for k in pages.LANDS]
REN=[("Kontakty.dc.html","Kontakty-mobil.dc.html"),("O-nas.dc.html","O-nas-mobil.dc.html")]+[(landing.CONF[k]["design"]+".dc.html",landing.CONF[k]["design"]+"-mobil.dc.html") for k in pages.LANDS]
for kind,name in JOBS:
    out=pages.page(kind,merged,'design')
    for x,y in REN: out=out.replace('"'+x,'"'+y)
    out=out.replace('href="Main.dc.html','href="Mobil-1.dc.html').replace('Mobil-1.dc.html#reference','Mobil-2.dc.html#reference')
    out=out.replace('class="refgrid photogrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px;"','class="photogrid" style="display: flex; gap: 12px; overflow-x: auto; scroll-snap-type: x mandatory; margin: 0 -24px; padding: 0 24px;"').replace('<figure style="margin: 0; display: flex;','<figure style="flex: 0 0 78%; scroll-snap-align: start; margin: 0; display: flex;')
    if kind in ('drevo','parkety'): out=re.sub(r'<!-- REALIZACE -->.*?</section>\n','',out,count=1,flags=re.S)
    out=re.sub(r'"\$preview":\{"width":\d+,"height":\d+\}','"$preview":{"width":390,"height":%d}'%H.get(kind,6300),out)
    open(D+name,'w',encoding='utf-8').write(out)
# mobile menu + mobile homepage links -> mobile landings
for f in ["Mobil-menu.dc.html","Mobil-1.dc.html","Mobil-2.dc.html"]:
    s=open(D+f,encoding='utf-8').read()
    for x,y in REN[2:]: s=s.replace('href="'+x+'"','href="'+y+'"')
    open(D+f,'w',encoding='utf-8').write(s)
print('ok')
