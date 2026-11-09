# Předávka – redesign webu AR podlahy (stav 9. 11. 2026)

## Projekt
- Klient: AR podlahy (Lukáš / Aleš Sebastianides), www.ar-podlahy.cz. **Informace z ar-podlahy.cz platí vždy.**
- Design (Claude Design artifact): https://claude.ai/code/artifact/2999c7a1-a211-4579-a5bc-73105fa42362
- Živý náhled: https://redesign.ar-podlahy.cz (Zerops, skrytý před Googlem)
- Repo: GitHub `foureight/ar-podlahy`, branch main, statický web ve složce `site/`
- Zerops redeploy (bez auto-deploye): přes Chrome otevřít https://app.zerops.io/service-stack/ywkPXF09TBmBV8pRlsTh3A/deploy → „Trigger re-deploy“ → „Re-trigger pipeline“ → po ~70 s ověřit web.
- Google Doc pro klienta „co doplnit a opravit“: https://docs.google.com/document/d/1mmqknveG032SdpGa2ZgzdJ17enROZxIn4FfSz0ArPQ8/edit

## Co je hotové
- Homepage (desktop + mobil), Kontakty, O nás, menu „Co děláme“ (logo vede na homepage).
- 14 landing pages: dřevěné podlahy, parkety, vinyl, PVC, koberce, historické podlahy, laminát, korek, lité stěrky, terasy, příprava podkladu, interiérové dveře, vchodové dveře, rekonstrukce – každá desktop + mobil.
- Kalkulačka orientační ceny (ceny bez DPH, stěrka 250 Kč/m², lišty od 59 Kč/bm), poptávkový formulář (zatím jen otevře e-mail).
- Sjednocená fakta: „Záruka až 12 let na materiál, 24 měsíců na práci“; montáž do 7 pracovních dní (100 m² vč. podkladu); sada na údržbu zdarma nad 100 m²; tel. +420 605 257 236, info@ar-podlahy.cz.
- Google mapa (béžová, zelený špendlík), Google recenze (10 hodnocení, 5,0 – texty recenzí se nekopírují).
- Fotky budov z Wikimedie (Úřad vlády, Kramářova vila, Pražský hrad) – zůstávají i s řádkem kreditu v patičce.
- 22 vlastních fotek z ar-podlahy.cz/projekty → sekce „Z našich realizací“ na 8 landing pages (v mobilním návrhu drevo/parkety vynecháno kvůli limitu výšky plátna ~8192 px; živý web je má).

## Co zbývá / nabídnuto
- Doplnit od klienta: chybějící ceny (vinyl, PVC, koberce, laminát, korek, terasy, stěrky, dveře…), texty vchodových dveří a rekonstrukcí, vlastní fotky referencí.
- Kam posílat poptávky z formuláře (endpoint).
- GDPR, obchodní podmínky, cookies (odkazy v patičce zatím nikam).
- Blog – přenést nebo skrýt.
- Automatické načítání Google recenzí (potřeba Places API klíč).
- Napojení domény ar-podlahy.cz a přesměrování starých URL po schválení.

## Poznámka k nástrojům
Generátory stránek (pages.py, landing.py, landing_more.py, mobile.py, facts.py) jsou zkopírované v repu ve složce `tools/` (cesty v nich vedou do dočasného prostoru staré konverzace – při dalším použití je upravit). Design soubory (.dc.html, canvas.json) jdou stáhnout z design artifactu.
