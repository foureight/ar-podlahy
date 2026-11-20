// Poptávkový formulář AR podlahy → e-mail přes SMTP.
// Proměnné prostředí (nastavují se v Zerops, ne v kódu):
//   SMTP_HOST, SMTP_PORT (465 = SSL, 587 = STARTTLS), SMTP_USER, SMTP_PASS
//   MAIL_TO (výchozí poptavky@ar-podlahy.cz), MAIL_FROM (výchozí SMTP_USER)
//   ALLOWED_ORIGINS (čárkami oddělené domény webu)
const http = require('http');
const nodemailer = require('nodemailer');

const PORT = Number(process.env.PORT || 3000);
const MAIL_TO = process.env.MAIL_TO || 'poptavky@ar-podlahy.cz';
const MAIL_FROM = process.env.MAIL_FROM || process.env.SMTP_USER;
const ORIGINS = (process.env.ALLOWED_ORIGINS ||
  'https://redesign.ar-podlahy.cz,https://ar-podlahy.cz,https://www.ar-podlahy.cz')
  .split(',').map(s => s.trim()).filter(Boolean);

const transport = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: Number(process.env.SMTP_PORT || 465),
  secure: Number(process.env.SMTP_PORT || 465) === 465,
  requireTLS: Number(process.env.SMTP_PORT || 465) === 587,
  auth: { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS },
  connectionTimeout: 15000, greetingTimeout: 10000, socketTimeout: 20000,
});

// jednoduchý limit: max 5 poptávek z jedné IP za 10 minut
const hits = new Map();
function limited(ip) {
  const now = Date.now(), win = 10 * 60 * 1000;
  const list = (hits.get(ip) || []).filter(t => now - t < win);
  list.push(now); hits.set(ip, list);
  return list.length > 5;
}

const LABELS = {
  jmeno: 'Jméno', telefon: 'Telefon', email: 'E-mail', lokalita: 'Lokalita',
  plocha: 'Plocha', typ: 'Typ podlahy', schody: 'Schody', dvere: 'Dveře', chci: 'Chci',
  zprava: 'Zpráva', kalkulace: 'Kalkulace', zdroj: 'Zdroj', stranka: 'Stránka',
  souhlas_gdpr: 'Souhlas GDPR',
};
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const clean = (v, n = 2000) => String(v == null ? '' : v).slice(0, n).trim();

function send(res, code, obj, origin) {
  const h = { 'Content-Type': 'application/json; charset=utf-8' };
  if (origin && ORIGINS.includes(origin)) {
    h['Access-Control-Allow-Origin'] = origin;
    h['Vary'] = 'Origin';
    h['Access-Control-Allow-Methods'] = 'POST, OPTIONS';
    h['Access-Control-Allow-Headers'] = 'Content-Type, Accept';
  }
  res.writeHead(code, h); res.end(obj ? JSON.stringify(obj) : '');
}

http.createServer((req, res) => {
  const origin = req.headers.origin;
  if (req.method === 'OPTIONS') return send(res, 204, null, origin);
  if (req.method === 'GET' && req.url === '/health') return send(res, 200, { ok: true }, origin);
  if (req.method !== 'POST' || !req.url.startsWith('/poptavka')) return send(res, 404, { success: 'false' }, origin);
  if (origin && !ORIGINS.includes(origin)) return send(res, 403, { success: 'false' }, origin);

  let body = '';
  req.on('data', c => { body += c; if (body.length > 50000) req.destroy(); });
  req.on('end', async () => {
    let d;
    try { d = JSON.parse(body || '{}'); } catch { return send(res, 400, { success: 'false', message: 'bad json' }, origin); }
    if (clean(d._honey)) return send(res, 200, { success: 'true' }, origin); // robot – tváříme se, že prošlo
    const ip = String(req.headers['x-forwarded-for'] || req.socket.remoteAddress || '').split(',')[0].trim();
    if (limited(ip)) return send(res, 429, { success: 'false', message: 'too many' }, origin);
    const jmeno = clean(d.jmeno, 200), telefon = clean(d.telefon, 50), email = clean(d.email, 200);
    if (!jmeno || !telefon || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || !clean(d.souhlas_gdpr)) {
      return send(res, 400, { success: 'false', message: 'missing fields' }, origin);
    }
    const rows = Object.keys(LABELS).filter(k => clean(d[k])).map(k => [LABELS[k], clean(d[k])]);
    const subject = clean(d._subject, 200) || ('Poptávka z webu – ' + jmeno);
    const text = rows.map(([k, v]) => `${k}: ${v}`).join('\n');
    const html = '<table cellpadding="6" style="border-collapse:collapse;font-family:Arial,sans-serif;font-size:14px">' +
      rows.map(([k, v]) => `<tr><td style="border:1px solid #ddd;font-weight:bold;background:#f6f2ea">${esc(k)}</td><td style="border:1px solid #ddd">${esc(v).replace(/\n/g, '<br>')}</td></tr>`).join('') +
      '</table>';
    try {
      await transport.sendMail({ from: `"Web AR podlahy" <${MAIL_FROM}>`, to: MAIL_TO, replyTo: `"${jmeno.replace(/"/g, '')}" <${email}>`, subject, text, html });
      send(res, 200, { success: 'true' }, origin);
    } catch (e) {
      console.error('SMTP error:', e && e.message);
      send(res, 500, { success: 'false', message: 'mail failed' }, origin);
    }
  });
}).listen(PORT, () => console.log('API běží na portu ' + PORT));
