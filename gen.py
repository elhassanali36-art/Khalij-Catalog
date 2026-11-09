import json, html
P = json.load(open('/tmp/products.json', encoding='utf-8'))
CATS = ['الكل'] + sorted({p['cat'] for p in P if p['cat'] != 'أخرى'}) + ['أخرى']
WA = '249903263031'
STORE = 'https://elhassanali36-art.github.io/khalij-digital-platform/products/view/?id='
SITE = 'https://elhassanali36-art.github.io/Khalij-Catalog/'

DESC = {
 'أصول إبداعية وطباعية': 'ملف عمل عربي أصلي لقوالب ومطبوعات جاهزة: خطوات تطبيقية، قوائم فحص، جداول قابلة للتعبئة، وأمثلة إرشادية. يُسلّم بصيغة Markdown سهلة الفتح والتحرير والتحويل إلى PDF.',
 'برمجيات وأكواد': 'ملف عمل عربي للمطورين وأصحاب المنتجات التقنية: مواصفات وقوالب منظمة تسرّع التخطيط والبناء والتسليم. يُسلّم بصيغة Markdown.',
 'وظائف ومسار مهني': 'ملف عمل عربي للباحثين عن عمل والمستقلين: قوالب ونماذج جاهزة للتقديم والمتابعة وتطوير المسار المهني. يُسلّم بصيغة Markdown.',
 'مواد تعليمية': 'ملف عمل عربي للمعلمين والمدربين وأولياء الأمور: أوراق عمل وقوالب تخطيط وتقييم قابلة للتعديل. يُسلّم بصيغة Markdown.',
 'مخططات ودفاتر رقمية': 'دفتر رقمي عربي قابل للتعبئة: صفحات منظمة وجداول متابعة وأمثلة إرشادية تساعدك على الالتزام. يُسلّم بصيغة Markdown.',
 'كتب إلكترونية': 'كتاب إلكتروني عربي مركّز: محاور عملية وخطوات قابلة للتطبيق فوراً، بلا حشو. يُسلّم بصيغة Markdown.',
 'الذكاء الاصطناعي': 'حزمة أوامر AI عربية جاهزة للنسخ والاستخدام: صيغ دقيقة تعطي نتائج قابلة للاستخدام مباشرة. يُسلّم بصيغة Markdown.',
 'قوالب الأعمال والجداول': 'قالب أعمال عربي جاهز: جداول وحسابات ونماذج منظمة لتشغيل مشروعك بأرقام واضحة. يُسلّم بصيغة Markdown.',
 'قوالب الإنتاجية': 'نظام إنتاجية جاهز للتطبيق: هيكل صفحات وقواعد متابعة تحوّل الفوضى إلى عمل منظم. يُسلّم بصيغة Markdown.',
 'قوالب وتصاميم': 'حزمة قوالب تصميم ومحتوى عربية: أفكار منشورات وخطط نشر جاهزة للاستخدام على السوشيال ميديا. يُسلّم بصيغة Markdown.',
 'أخرى': 'منتج رقمي يُسلّم فور تأكيد الطلب.',
}

items_json = json.dumps([{**p, 'wa': f"https://wa.me/{WA}?text=" } for p in P], ensure_ascii=False)
ld = {
 "@context":"https://schema.org","@type":"ItemList","name":"كتالوج المنتجات الرقمية — منصة الخليج",
 "numberOfItems": len(P),
 "itemListElement":[{"@type":"ListItem","position":i+1,"item":{
   "@type":"Product","name":p['title'],"category":p['cat'],
   "offers":{"@type":"Offer","price":f"{p['price']:.2f}","priceCurrency":"USD",
             "availability":"https://schema.org/InStock","url":STORE+p['id']}}} for i,p in enumerate(P)]
}

HTML = f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>منصة الخليج | كتالوج المنتجات الرقمية العربية</title>
<meta name="description" content="كتالوج منصة الخليج: {len(P)} منتجاً رقمياً عربياً جاهزاً — قوالب أعمال، كتب، حزم أوامر AI، مخططات، مواد تعليمية وتصاميم. من 8 إلى 32 دولاراً، مع رابط شراء لكل منتج.">
<meta property="og:type" content="website">
<meta property="og:title" content="منصة الخليج | كتالوج المنتجات الرقمية">
<meta property="og:description" content="{len(P)} منتجاً رقمياً عربياً جاهزاً: قوالب أعمال وكتب وحزم AI ومخططات وتصاميم.">
<meta property="og:url" content="{SITE}">
<meta name="twitter:card" content="summary">
<link rel="canonical" href="{SITE}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>
:root{{--bg:#fff;--ink:#14161b;--muted:#6b7280;--line:#e8e9ee;--accent:#5b3fd6;--accent-soft:#f2eeff;--gold:#a9741f}}
*{{box-sizing:border-box}}
html,body{{margin:0;padding:0;background:var(--bg);color:var(--ink)}}
body{{font-family:'Tajawal',Tahoma,Arial,sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased}}
a{{color:inherit;text-decoration:none}}
.wrap{{max-width:1140px;margin:0 auto;padding:0 18px}}
header{{border-bottom:1px solid var(--line);position:sticky;top:0;background:rgba(255,255,255,.94);backdrop-filter:blur(10px);z-index:20}}
.head{{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:12px 0}}
.brand{{display:flex;align-items:center;gap:10px}}
.logo{{width:38px;height:38px;border-radius:11px;background:var(--accent);color:#fff;display:grid;place-items:center;font-weight:800;font-size:17px}}
.brand h1{{font-size:16px;margin:0;font-weight:800}}
.brand p{{margin:0;font-size:11.5px;color:var(--muted)}}
.wa{{background:var(--accent);color:#fff;padding:9px 15px;border-radius:999px;font-weight:700;font-size:13.5px;white-space:nowrap}}
.hero{{padding:34px 0 10px}}
.hero h2{{font-size:clamp(24px,4vw,38px);line-height:1.3;margin:0 0 10px;letter-spacing:-.4px}}
.hero p{{color:var(--muted);margin:0;max-width:62ch;font-size:15px}}
.stats{{display:flex;gap:26px;margin:20px 0 0;flex-wrap:wrap}}
.stat b{{display:block;font-size:20px;color:var(--accent)}}
.stat span{{font-size:12px;color:var(--muted)}}
.tools{{display:flex;gap:10px;align-items:center;margin:22px 0 8px;flex-wrap:wrap}}
input[type=search]{{flex:1 1 240px;min-width:0;padding:11px 14px;border:1px solid var(--line);border-radius:12px;font:inherit;font-size:14px;background:#fbfbfd}}
input[type=search]:focus{{outline:2px solid var(--accent-soft);border-color:var(--accent)}}
select{{padding:11px 12px;border:1px solid var(--line);border-radius:12px;font:inherit;font-size:13.5px;background:#fbfbfd}}
.chips{{display:flex;gap:8px;overflow-x:auto;padding:10px 0 16px;scrollbar-width:none}}
.chips::-webkit-scrollbar{{display:none}}
.chip{{flex:0 0 auto;padding:7px 13px;border-radius:999px;border:1px solid var(--line);background:#fff;font:inherit;font-size:13px;color:#374151;cursor:pointer}}
.chip.on{{background:var(--accent);border-color:var(--accent);color:#fff;font-weight:700}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:14px;padding-bottom:34px}}
.card{{border:1px solid var(--line);border-radius:16px;padding:16px;display:flex;flex-direction:column;gap:9px;background:#fff;transition:.18s;min-width:0}}
.card:hover{{border-color:#cfc7f5;box-shadow:0 10px 28px rgba(91,63,214,.07);transform:translateY(-2px)}}
.card.target{{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}}
.emoji{{width:42px;height:42px;border-radius:12px;background:var(--accent-soft);display:grid;place-items:center;font-size:21px}}
.cat{{font-size:11.5px;color:var(--muted)}}
.title{{font-size:15px;font-weight:700;margin:0;line-height:1.5;min-height:45px}}
.price{{font-weight:800;color:var(--gold);font-size:16px;margin-top:auto}}
.actions{{display:flex;gap:8px;margin-top:6px}}
.buy{{flex:1;text-align:center;background:var(--accent);color:#fff;padding:9px 10px;border-radius:10px;font-size:13px;font-weight:700}}
.buy.wa2{{background:#1f9d55}}
.more{{border:1px solid var(--line);padding:9px 11px;border-radius:10px;font-size:12.5px;color:#4b5563;background:#fff;cursor:pointer}}
.more:hover{{border-color:var(--accent);color:var(--accent)}}
.empty{{padding:40px 0;text-align:center;color:var(--muted)}}
footer{{border-top:1px solid var(--line);padding:22px 0 40px;color:var(--muted);font-size:12.5px}}
footer a{{color:var(--accent);font-weight:700}}
.sheet{{position:fixed;inset:0;background:rgba(12,14,20,.5);display:none;align-items:flex-end;justify-content:center;z-index:40}}
.sheet.open{{display:flex}}
.panel{{background:#fff;width:100%;max-width:640px;border-radius:20px 20px 0 0;padding:22px;max-height:88vh;overflow:auto}}
.panel h3{{margin:0 0 6px;font-size:19px}}
.panel .p{{color:var(--muted);font-size:14px;margin:10px 0 16px}}
.panel .row{{display:flex;gap:10px;flex-wrap:wrap}}
.close{{margin-top:14px;width:100%;padding:11px;border:1px solid var(--line);border-radius:12px;background:#fff;font:inherit;font-weight:700;cursor:pointer}}
@media(max-width:520px){{.hero{{padding:24px 0 6px}}.title{{font-size:14.5px}}}}
</style>
</head>
<body>
<header><div class="wrap head">
  <div class="brand"><div class="logo">خ</div><div><h1>منصة الخليج — كتالوج المنتجات الرقمية</h1><p>{len(P)} منتجاً عربياً جاهزاً</p></div></div>
  <a class="wa" href="https://wa.me/{WA}?text=%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%D8%8C%20%D8%A3%D8%B1%D9%8A%D8%AF%20%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%81%D8%B3%D8%A7%D8%B1%20%D8%B9%D9%86%20%D8%A7%D9%84%D9%85%D9%86%D8%AA%D8%AC%D8%A7%D8%AA" target="_blank" rel="noopener">اطلب على واتساب</a>
</div></header>

<main class="wrap">
  <section class="hero">
    <h2>منتجات رقمية عربية جاهزة للاستخدام اليوم</h2>
    <p>قوالب أعمال وجداول، كتب إلكترونية، حزم أوامر ذكاء اصطناعي، مخططات ودفاتر رقمية، مواد تعليمية وتصاميم. كل منتج له صفحة شراء مستقلة، والتسليم رقمي بعد تأكيد الدفع.</p>
    <div class="stats">
      <div class="stat"><b>{len(P)}</b><span>منتجاً رقمياً</span></div>
      <div class="stat"><b>{len(CATS)-1}</b><span>فئة</span></div>
      <div class="stat"><b>8$ — 32$</b><span>نطاق السعر</span></div>
      <div class="stat"><b>Markdown</b><span>صيغة التسليم</span></div>
    </div>
  </section>

  <div class="tools">
    <input id="q" type="search" placeholder="ابحث عن منتج: خطة عمل، Notion، prompts، سيرة ذاتية…" aria-label="بحث">
    <select id="sort" aria-label="ترتيب">
      <option value="def">الترتيب الافتراضي</option>
      <option value="asc">الأرخص أولاً</option>
      <option value="desc">الأغلى أولاً</option>
    </select>
  </div>
  <div class="chips" id="chips"></div>
  <div class="grid" id="grid"></div>
  <div class="empty" id="empty" hidden>لا يوجد منتج مطابق. جرّب كلمة أخرى أو اسألني على واتساب.</div>
</main>

<footer><div class="wrap">
  <div>منصة الخليج للمنتجات الرقمية — الدفع عبر PayPal أو العملات الرقمية، والتسليم رقمي بعد التأكيد.</div>
  <div style="margin-top:8px">للطلب والاستفسار: <a href="https://wa.me/{WA}" target="_blank" rel="noopener">واتساب +249 90 326 3031</a> · <a href="https://elhassanali36-art.github.io/khalij-digital-platform/" target="_blank" rel="noopener">المتجر الرسمي</a></div>
  <div style="margin-top:8px">هذه صفحة كتالوج تعريفية. إتمام الشراء يتم على صفحة المنتج الرسمية.</div>
</div></footer>

<div class="sheet" id="sheet"><div class="panel" id="panel"></div></div>

<script>
const PRODUCTS = {items_json};
const WA = '{WA}';
const STORE = '{STORE}';
const DESC = {json.dumps(DESC, ensure_ascii=False)};
const CATS = {json.dumps(CATS, ensure_ascii=False)};
let cat = 'الكل', q = '', sort = 'def';

const $ = s => document.querySelector(s);
function esc(s){{ return String(s).replace(/[&<>"']/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}})[c]); }}
function money(n){{ return '$' + (Number(n) % 1 === 0 ? Number(n).toFixed(0) : Number(n).toFixed(2)); }}

function waLink(p){{
  const msg = 'مرحبا، أريد شراء: ' + p.title + ' — ' + money(p.price) + ' (من كتالوج منصة الخليج)';
  return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(msg);
}}

function renderChips(){{
  $('#chips').innerHTML = CATS.map(c =>
    '<button class="chip' + (c === cat ? ' on' : '') + '" data-cat="' + esc(c) + '">' + esc(c) + '</button>'
  ).join('');
  document.querySelectorAll('.chip').forEach(b => b.addEventListener('click', () => {{
    cat = b.getAttribute('data-cat'); renderChips(); render();
  }}));
}}

function view(){{
  let list = PRODUCTS.filter(p =>
    (cat === 'الكل' || p.cat === cat) &&
    (!q || (p.title + ' ' + p.cat).toLowerCase().includes(q))
  );
  if (sort === 'asc') list = list.slice().sort((a,b) => a.price - b.price);
  if (sort === 'desc') list = list.slice().sort((a,b) => b.price - a.price);
  return list;
}}

function render(){{
  const list = view();
  $('#empty').hidden = list.length > 0;
  $('#grid').innerHTML = list.map(p => `
    <article class="card" id="p-${{p.id}}">
      <div class="emoji">${{p.emoji}}</div>
      <div class="cat">${{esc(p.cat)}}</div>
      <h3 class="title">${{esc(p.title)}}</h3>
      <div class="price">${{money(p.price)}}</div>
      <div class="actions">
        <a class="buy wa2" href="${{waLink(p)}}" target="_blank" rel="noopener">اطلب واتساب</a>
        <a class="buy" href="${{STORE + p.id}}" target="_blank" rel="noopener">رابط الشراء</a>
      </div>
      <button class="more" data-id="${{p.id}}">التفاصيل</button>
    </article>`).join('');
  document.querySelectorAll('.more').forEach(b => b.addEventListener('click', () => openSheet(b.getAttribute('data-id'))));
}}

function openSheet(id){{
  const p = PRODUCTS.find(x => x.id === id); if (!p) return;
  $('#panel').innerHTML = `
    <div class="emoji">${{p.emoji}}</div>
    <h3>${{esc(p.title)}}</h3>
    <div class="cat">${{esc(p.cat)}} · ${{money(p.price)}}</div>
    <p class="p">${{esc(DESC[p.cat] || DESC['أخرى'])}}</p>
    <div class="row">
      <a class="buy wa2" href="${{waLink(p)}}" target="_blank" rel="noopener" style="flex:1">اطلب على واتساب</a>
      <a class="buy" href="${{STORE + p.id}}" target="_blank" rel="noopener" style="flex:1">اشترِ من المنصة</a>
    </div>
    <button class="close" id="closeSheet">إغلاق</button>`;
  $('#sheet').classList.add('open');
  $('#closeSheet').addEventListener('click', () => $('#sheet').classList.remove('open'));
}}
$('#sheet').addEventListener('click', e => {{ if (e.target.id === 'sheet') $('#sheet').classList.remove('open'); }});

$('#q').addEventListener('input', e => {{ q = e.target.value.trim().toLowerCase(); render(); }});
$('#sort').addEventListener('change', e => {{ sort = e.target.value; render(); }});

renderChips(); render();

const deep = new URLSearchParams(location.search).get('p');
if (deep) {{
  const el = document.getElementById('p-' + deep);
  if (el) {{ el.classList.add('target'); el.scrollIntoView({{behavior:'smooth', block:'center'}}); openSheet(deep); }}
}}
</script>
</body>
</html>
"""
open('/tmp/catalog/index.html','w',encoding='utf-8').write(HTML)

# sitemap + robots + indexnow key
open('/tmp/catalog/robots.txt','w').write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
open('/tmp/catalog/sitemap.xml','w').write(
 '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
 f'<url><loc>{SITE}</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>\n'
 + ''.join(f'<url><loc>{SITE}?p={p["id"]}</loc><priority>0.6</priority></url>\n' for p in P)
 + '</urlset>\n')
print('site generated; products', len(P))
