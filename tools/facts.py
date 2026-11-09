import re
SP='/tmp/claude-0/-home-claude/a1dc3947-88ac-503c-910c-cbe14d93fb1b/scratchpad'
FILES=[SP+'/web/project/Main.dc.html',SP+'/web/project/Mobil-1.dc.html',SP+'/web/project/Mobil-2.dc.html','/home/claude/ar-podlahy/site/index.html']
R=[
 ('záruka na materiál 6 let','záruka na materiál 12 let'),
 ('na materiál dáváme záruku 6 let','na materiál dáváme záruku 12 let'),
 ('Na materiál 6 let, na naši práci 24 měsíců. Ke každé realizaci přidáme sadu na údržbu podlahy zdarma.','Na materiál 12 let, na naši práci 24 měsíců. Ke každé zakázce nad 100 m² přidáme sadu na údržbu podlahy zdarma.'),
 ('>6 let</div>','>12 let</div>'),
 ('sada na údržbu podlahy ke každé realizaci, ať vydrží co nejdéle jako nová.','sada na údržbu podlahy u zakázek nad 100 m², ať vydrží co nejdéle jako nová.'),
 ('Od poptávky po montáž do 6 týdnů','Montáž do 7 pracovních dní (100 m² vč. podkladu)'),
 ("I historické vzory a intarzie.', price: 'cena po zaměření'","I historické vzory a intarzie.', price: 'od 600 Kč/m²'"),
 ("Základ, který rozhoduje.', price: 'cena po zaměření'","Základ, který rozhoduje.', price: 'stěrka od 250 Kč/m²'"),
]
NAV_OLD='Vinylové a PVC podlahy'
LINKS={'design':{'Dřevěné podlahy':'Drevene-podlahy.dc.html','Parkety':'Parkety.dc.html','Renovace a broušení parket':'Parkety.dc.html','Vinylové podlahy':'Vinylove-podlahy.dc.html','PVC a lino':'PVC-podlahy.dc.html','Koberce':'Koberce.dc.html','Historické podlahy':'Historicke-podlahy.dc.html','Laminátové podlahy':'Laminatove-podlahy.dc.html','Korkové podlahy':'Korkove-podlahy.dc.html','Lité epoxidové stěrky':'Lite-sterky.dc.html','Terasy':'Terasy.dc.html','Příprava podkladu':'Priprava-podkladu.dc.html','Interiérové dveře':'Interierove-dvere.dc.html','Vchodové dveře':'Vchodove-dvere.dc.html','Rekonstrukce a stavby na klíč':'Rekonstrukce.dc.html'},
       'static':{'Dřevěné podlahy':'/drevene-podlahy-praha/','Parkety':'/parkety-praha/','Renovace a broušení parket':'/parkety-praha/','Vinylové podlahy':'/vinylove-podlahy-praha/','PVC a lino':'/pvc-podlahy-praha/','Koberce':'/koberce-praha/','Historické podlahy':'/historicke-podlahy-praha/','Laminátové podlahy':'/laminatove-podlahy-praha/','Korkové podlahy':'/korkove-podlahy-praha/','Lité epoxidové stěrky':'/lite-epoxidove-sterky-praha/','Terasy':'/terasy-praha/','Příprava podkladu':'/priprava-podkladu-praha/','Interiérové dveře':'/interierove-dvere-praha/','Vchodové dveře':'/vchodove-dvere-praha/','Rekonstrukce a stavby na klíč':'/rekonstrukce-praha/'}}
def fix(f, target, mobile=False):
    s=open(f,encoding='utf-8').read(); n0=s
    for a,b in R: s=s.replace(a,b)
    # static rendered services prices (2x 'cena po zaměření' in services grid order: renovace, podklad)
    if target=='static':
        i=[0]
        def rp(m):
            i[0]+=1; return ['od 600 Kč/m²','stěrka od 250 Kč/m²'][i[0]-1] if i[0]<=2 else m.group(0)
        s=re.sub(r'cena po zaměření',rp,s)
    # split vinyl/pvc menu item: <a href="X"(style)?>Vinylové a PVC podlahy</a>
    s=re.sub(r'<a href="[^"]*"( style="[^"]*")?>Vinylové a PVC podlahy</a>',lambda m:f'<a href="#"{m.group(1) or ""}>Vinylové podlahy</a><a href="#"{m.group(1) or ""}>PVC a lino</a>',s)
    L=dict(LINKS[target])
    if mobile: L={k:(v.replace('.dc.html','-mobil.dc.html') if k in ('Dřevěné podlahy',) else v) for k,v in L.items()}
    for name,url in L.items():
        s=re.sub(r'<a href="[^"]*"( style="[^"]*")?>%s</a>'%re.escape(name),lambda m:f'<a href="{url}"{m.group(1) or ""}>{name}</a>',s)
    open(f,'w',encoding='utf-8').write(s); print(f.split('/')[-1], s!=n0)
for f in FILES[:3]: fix(f,'design')
fix(SP+'/web/project/Mobil-menu.dc.html','design',mobile=True)
fix(FILES[3],'static')
