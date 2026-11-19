<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:s="http://www.sitemaps.org/schemas/sitemap/0.9">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>
<xsl:template match="/">
<html lang="cs"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/><meta name="robots" content="noindex"/><title>Mapa webu – AR podlahy</title>
<style>body{font-family:system-ui,sans-serif;background:#f5f1ea;color:#1a1a1a;margin:0;padding:32px 16px}main{max-width:900px;margin:0 auto}h1{margin:0 0 6px;font-size:28px}p{color:#5b554c;margin:0 0 20px}table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #e4ddd2;border-radius:10px;overflow:hidden}th,td{text-align:left;padding:10px 14px;border-bottom:1px solid #ece6dc;font-size:14px}th{background:#1a1a1a;color:#fff}a{color:#8a6a3f}</style></head>
<body><main><h1>Mapa webu AR podlahy</h1><p>Seznam stránek pro vyhledávače (<xsl:value-of select="count(s:urlset/s:url)"/> stránek).</p>
<table><tr><th>Stránka</th><th>Aktualizováno</th></tr>
<xsl:for-each select="s:urlset/s:url"><tr><td><a href="{s:loc}"><xsl:value-of select="s:loc"/></a></td><td><xsl:value-of select="s:lastmod"/></td></tr></xsl:for-each>
</table></main></body></html>
</xsl:template>
</xsl:stylesheet>
