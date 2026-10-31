# AR podlahy – redesign (redesign.ar-podlahy.cz)

Statický web vyexportovaný z návrhu. Náhledová verze: má `noindex` (meta, robots.txt i hlavička X-Robots-Tag),
aby ji Google neindexoval vedle www.ar-podlahy.cz.

## Nasazení na Zerops
1. V Zerops vytvořte projekt a v něm službu typu **Static** s názvem (hostname) `web`.
2. Ve službě `web` → Build & deploy pipeline → propojte GitHub repo `foureight/ar-podlahy`,
   větev `main` (deploy po každém pushi). Alternativně z lokální kopie: `zcli push`.
3. Ve službě web → Public access → Add domain → `redesign.ar-podlahy.cz`.
4. V DNS domény ar-podlahy.cz přidejte záznam, který Zerops zobrazí (A/AAAA na IP projektu,
   případně CNAME). SSL certifikát vystaví Zerops sám.

## Před ostrým spuštěním na www
- odstranit noindex (index.html, site/robots.txt, zerops.yml)
- doplnit ceny [CENA] a odkaz na Facebook (JSON-LD sameAs)
- napojit formulář na backend (zatím nikam neodesílá)
