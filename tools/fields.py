# Rozdělí "Jméno a příjmení" na Jméno + Příjmení a "Lokalita" na Místo + Kraj (vše povinné).
import re, sys
KRAJE = ['Hlavní město Praha','Středočeský','Jihočeský','Plzeňský','Karlovarský','Ústecký','Liberecký',
         'Královéhradecký','Pardubický','Vysočina','Jihomoravský','Olomoucký','Zlínský','Moravskoslezský']
def tr(h):
    h = re.sub(r'<label style="([^"]*)">Jméno a příjmení \*<input type="text" name="jmeno" autocomplete="name" required style="([^"]*)"></label>',
        lambda m: f'<label style="{m[1]}">Jméno *<input type="text" name="jmeno" autocomplete="given-name" required style="{m[2]}"></label>'
                  f'<label style="{m[1]}">Příjmení *<input type="text" name="prijmeni" autocomplete="family-name" required style="{m[2]}"></label>', h)
    def lok(m):
        opts = '<option value="" disabled selected>Vyberte kraj</option>' + ''.join(f'<option>{k}</option>' for k in KRAJE)
        return (f'<label style="{m[1]}">Místo *<input type="text" name="misto" placeholder="obec / část Prahy" autocomplete="address-level2" required style="{m[2]}"></label>'
                f'<label style="{m[1]}">Kraj *<select name="kraj" required style="{m[2]} background: #fff; color: #1f1b16;">{opts}</select></label>')
    h = re.sub(r'<label style="([^"]*)">Lokalita<input type="text" name="lokalita" placeholder="např. Praha 5" style="([^"]*)"></label>', lok, h)
    return h
for f in sys.argv[1:]:
    s = open(f, encoding='utf-8').read(); n = tr(s)
    print(f, 'změněno' if n != s else 'BEZ ZMĚNY'); open(f, 'w', encoding='utf-8').write(n)
