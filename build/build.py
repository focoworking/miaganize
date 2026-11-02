#!/usr/bin/env python3
"""MIAGAZINE static site builder. EN at /, ES at /es/. Blog from content/blog/*.{en,es}.md
Usage: python3 build/build.py   -> writes ./site
"""
import os, re, glob, json, html, shutil, datetime
import markdown, yaml, importlib.util
_spec = importlib.util.spec_from_file_location('build_kit', os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media-kit', 'build_kit.py'))
KIT = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(KIT)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'site')
BASE = 'https://www.miagazine.com'
TODAY = '2026-11-01'

CATS = {  # category -> (css var color, ES label)
 'Art & Culture': ('#c2410c', 'Arte y Cultura'), 'Fashion & Models': ('#be185d', 'Moda y Modelos'),
 'Real Estate': ('#0f766e', 'Real Estate'), 'Economy': ('#1e3a8a', 'Economía'), 'Music': ('#7c3aed', 'Música'),
 'Trends': ('#b45309', 'Tendencias'), 'Food & Drink': ('#9f1239', 'Gastronomía'), 'Tech': ('#0369a1', 'Tecnología'),
 'Waterfront': ('#0e7490', 'Vida en el agua'), 'Design & Architecture': ('#57534e', 'Diseño y Arquitectura'),
 'Sports & Lifestyle': ('#15803d', 'Deporte y Lifestyle'), 'Photography': ('#a16207', 'Fotografía')}

T = {
 'en': dict(home='/', journal='Journal', stories='Stories', submit='Submit', advertise='Advertise', about='About',
   journal_url='/blog/', other='es', other_label='ES', tagline='Miami, through the lens.',
   sub_ph='Your email', sub_btn='Subscribe', sub_note='Free. One email every Thursday. Unsubscribe anytime.',
   read='min read', in30='In 30 seconds', faq='Questions people ask', sources='Sources', related='Keep reading',
   toc='In this story', all='All', latest='Latest from the Journal', journal_title='The Journal',
   journal_sub='Real estate, money, music, models, food, water, tech and the art of seeing Miami. Researched, sourced, and written to be enjoyed.',
   cta_title='Get the Thursday edition', footer='Visual luxury magazine made by Miami photographers.', updated='Updated',
   by='By MIAGAZINE Editorial', share='Share', copy='Copy link', copied='Link copied', cover='Cover photo brief',
   lang_name='English', locale='en_US', back='All stories'),
 'es': dict(home='/es/', journal='Journal', stories='Historias', submit='Publica', advertise='Anúnciate', about='Nosotros',
   journal_url='/es/blog/', other='en', other_label='EN', tagline='Miami, a través del lente.',
   sub_ph='Tu email', sub_btn='Suscribirme', sub_note='Gratis. Un email cada jueves. Te das de baja cuando quieras.',
   read='min de lectura', in30='En 30 segundos', faq='Lo que la gente pregunta', sources='Fuentes', related='Sigue leyendo',
   toc='En esta historia', all='Todo', latest='Lo último del Journal', journal_title='El Journal',
   journal_sub='Real estate, dinero, música, modelos, comida, mar, tecnología y el arte de mirar Miami. Investigado, con fuentes y escrito para disfrutarse.',
   cta_title='Recibe la edición del jueves', footer='Revista visual de lujo hecha por fotógrafos de Miami.', updated='Actualizado',
   by='Por MIAGAZINE Editorial', share='Compartir', copy='Copiar link', copied='Link copiado', cover='Brief de foto de portada',
   lang_name='Español', locale='es_US', back='Todas las historias'),
}

def esc(s): return html.escape(str(s), quote=True)
def P(lang, path):  # localized path
    return path if lang == 'en' else '/es' + path

ORG = {"@context":"https://schema.org","@type":["NewsMediaOrganization","Organization"],"name":"MIAGAZINE","url":BASE,
 "logo":BASE+"/assets/favicon.svg","slogan":"Miami, through the lens.","areaServed":{"@type":"City","name":"Miami"},
 "sameAs":["https://instagram.com/miagazine","https://pinterest.com/miagazine","https://www.linkedin.com/company/miagazine"],
 "publishingPrinciples":BASE+"/about.html"}

def head(lang, title, desc, path, alt_path=None, extra='', og_type='website'):
    canon = BASE + path.replace('index.html', '')
    alts = ''
    if alt_path is not None:
        en_p, es_p = (path, alt_path) if lang == 'en' else (alt_path, path)
        alts = (f'<link rel="alternate" hreflang="en" href="{BASE}{en_p.replace("index.html","")}">'
                f'<link rel="alternate" hreflang="es" href="{BASE}{es_p.replace("index.html","")}">'
                f'<link rel="alternate" hreflang="x-default" href="{BASE}{en_p.replace("index.html","")}">')
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{canon}">{alts}
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="MIAGAZINE"><meta property="og:locale" content="{T[lang]['locale']}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}"><meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css"><link rel="icon" href="/assets/favicon.svg">
<script type="application/ld+json">{json.dumps(ORG)}</script>{extra}</head><body>'''

def nav(lang, alt_path):
    t = T[lang]
    return f'''<header class="top"><div class="wrap"><a class="logo" href="{t['home']}">MIAGAZINE</a><nav>
<a href="{t['journal_url']}">{t['journal']}</a><a href="{P(lang,'/stories/')}" class="hide-sm">{t['stories']}</a><a href="{P(lang,'/submit.html')}">{t['submit']}</a><a href="{P(lang,'/advertise.html')}" class="hide-sm">{t['advertise']}</a><a href="{P(lang,'/about.html')}" class="hide-sm">{t['about']}</a>
<a class="lang" href="{alt_path}" hreflang="{t['other']}" lang="{t['other']}">{t['other_label']}</a></nav></div></header>'''

COOKIE_TXT = {
 'en': dict(t='We value your privacy', d='We use necessary storage to run this site and, only with your consent, analytics and marketing cookies to understand our audience and measure campaigns.', acc='Accept all', rej='Reject', cfg='Settings', save='Save preferences', nec='Necessary', nec_d='Required for the site to work (e.g., remembering this choice). Always on.', ana='Analytics', ana_d='Helps us understand which stories you read. No ads.', mkt='Marketing', mkt_d='Measures our social media campaigns (e.g., Meta, Google).', more='Cookie Policy', prefs='Cookie preferences'),
 'es': dict(t='Valoramos tu privacidad', d='Usamos almacenamiento necesario para que el sitio funcione y, solo con tu consentimiento, cookies de analítica y marketing para entender a nuestra audiencia y medir campañas.', acc='Aceptar todas', rej='Rechazar', cfg='Configurar', save='Guardar preferencias', nec='Necesarias', nec_d='Indispensables para que el sitio funcione (por ejemplo, recordar esta elección). Siempre activas.', ana='Analítica', ana_d='Nos ayuda a saber qué historias lees. Sin publicidad.', mkt='Marketing', mkt_d='Mide nuestras campañas en redes (por ejemplo, Meta, Google).', more='Política de cookies', prefs='Preferencias de cookies'),
}

def cookie_banner(lang):
    c = COOKIE_TXT[lang]
    return f"""<div class="cookie" id="cookie" role="dialog" aria-modal="false" aria-labelledby="ck-t" hidden>
<div class="ck-in"><div class="ck-text"><strong id="ck-t">{c['t']}</strong><p>{c['d']} <a href="{P(lang,'/legal/cookies.html')}">{c['more']}</a>.</p></div>
<div class="ck-opts" id="ck-opts" hidden>
<label class="ck-row"><input type="checkbox" checked disabled><span><b>{c['nec']}</b><small>{c['nec_d']}</small></span></label>
<label class="ck-row"><input type="checkbox" id="ck-ana"><span><b>{c['ana']}</b><small>{c['ana_d']}</small></span></label>
<label class="ck-row"><input type="checkbox" id="ck-mkt"><span><b>{c['mkt']}</b><small>{c['mkt_d']}</small></span></label></div>
<div class="ck-btns"><button class="btn ghost" id="ck-rej" type="button">{c['rej']}</button><button class="btn ghost" id="ck-cfg" type="button">{c['cfg']}</button><button class="btn ghost" id="ck-save" type="button" hidden>{c['save']}</button><button class="btn" id="ck-acc" type="button">{c['acc']}</button></div></div></div>
<script>(function(){{var K='mg-consent',el=document.getElementById('cookie');
function get(){{try{{var v=JSON.parse(localStorage.getItem(K));if(v&&Date.now()-v.ts<365*864e5)return v}}catch(e){{}}return null}}
function apply(v){{window.mgConsent=v;/* ANALYTICS / MARKETING TAGS: load here only if v.analytics / v.marketing */}}
function set(a,m){{var v={{necessary:true,analytics:a,marketing:m,ts:Date.now(),v:1}};try{{localStorage.setItem(K,JSON.stringify(v))}}catch(e){{}}apply(v);el.hidden=true}}
function open(){{var v=get();document.getElementById('ck-ana').checked=!!(v&&v.analytics);document.getElementById('ck-mkt').checked=!!(v&&v.marketing);el.hidden=false}}
var gpc=navigator.globalPrivacyControl===true,cur=get();
if(cur)apply(cur);else if(gpc){{set(false,false)}}else el.hidden=false;
document.getElementById('ck-acc').onclick=function(){{set(true,true)}};
document.getElementById('ck-rej').onclick=function(){{set(false,false)}};
document.getElementById('ck-cfg').onclick=function(){{document.getElementById('ck-opts').hidden=false;this.hidden=true;document.getElementById('ck-save').hidden=false}};
document.getElementById('ck-save').onclick=function(){{set(document.getElementById('ck-ana').checked,document.getElementById('ck-mkt').checked)}};
document.querySelectorAll('[data-cookie-prefs]').forEach(function(b){{b.onclick=function(e){{e.preventDefault();open();document.getElementById('ck-opts').hidden=false;document.getElementById('ck-cfg').hidden=true;document.getElementById('ck-save').hidden=false}}}});
}})();</script>"""

def footer(lang):
    t = T[lang]; c = COOKIE_TXT[lang]
    L = lambda en, es: en if lang == 'en' else es
    return f"""<footer><div class="wrap foot-grid">
<div><span class="logo" style="font-size:18px">MIAGAZINE</span><p class="small">{t['tagline']} {t['footer']}</p></div>
<div><div class="eyebrow">{L('Magazine','Revista')}</div><a href="{t['journal_url']}">{t['journal']}</a><a href="{P(lang,'/stories/')}">{t['stories']}</a><a href="{P(lang,'/submit.html')}">{t['submit']}</a><a href="{P(lang,'/advertise.html')}">{t['advertise']}</a><a href="{P(lang,'/media-kit.html')}">Media kit</a></div>
<div><div class="eyebrow">{L('Company','Compañía')}</div><a href="{P(lang,'/about.html')}">{t['about']}</a><a href="{P(lang,'/careers.html')}">{L('Careers','Vacantes')}</a><a href="https://instagram.com/miagazine">Instagram</a></div>
<div><div class="eyebrow">Legal</div><a href="{P(lang,'/legal/intellectual-property.html')}">{L('IP & Permissions','Propiedad intelectual')}</a><a href="{P(lang,'/legal/privacy.html')}">{L('Privacy','Privacidad')}</a><a href="{P(lang,'/legal/cookies.html')}">Cookies</a><a href="{P(lang,'/legal/terms.html')}">{L('Terms','Términos')}</a><a href="{P(lang,'/legal/editorial-policy.html')}">{L('Editorial policy','Política editorial')}</a><a href="#" data-cookie-prefs>{c['prefs']}</a></div>
</div><div class="wrap"><p class="small foot-copy">© 2026 MIAGAZINE · Miami, FL · {L('All rights reserved. Photographs © their respective authors.','Todos los derechos reservados. Fotografías © de sus respectivos autores.')}</p></div></footer>
{cookie_banner(lang)}
<script>document.querySelectorAll('form.sub').forEach(f=>f.addEventListener('submit',e=>{{if(f.action.includes('BEEHIIV')){{e.preventDefault();f.querySelector('button').textContent='✓'}}}}));</script>
</body></html>"""

def subform(lang):
    t = T[lang]
    return f'<form class="sub" action="BEEHIIV_FORM_ACTION" method="post"><input type="email" name="email" placeholder="{t["sub_ph"]}" required aria-label="Email"><button class="btn" type="submit">{t["sub_btn"]}</button></form>'

def write(path, s):
    full = os.path.join(OUT, path.lstrip('/'))
    if full.endswith('/'): full += 'index.html'
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w').write(s)

def page(lang, path, alt_path, title, desc, body, extra='', og_type='website'):
    write(path, head(lang, title, desc, path, alt_path, extra, og_type) + nav(lang, alt_path) + '<main>' + body + '</main>' + footer(lang))

# ---------------- BLOG -----------------
def load_posts():
    posts = {'en': [], 'es': []}
    for f in sorted(glob.glob(os.path.join(ROOT, 'content/blog/*.md'))):
        raw = open(f).read()
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', raw, re.S)
        if not m: print('skip (no front matter)', f); continue
        meta = yaml.safe_load(m.group(1)); body = m.group(2)
        lang = meta.get('lang') or f.split('.')[-2]
        meta['body'] = body; meta['lang'] = lang
        meta.setdefault('date', TODAY)
        meta['date'] = str(meta['date'])
        if meta.get('category') not in CATS: meta['category'] = 'Trends'
        posts[lang].append(meta)
    for l in posts: posts[l].sort(key=lambda p: (p['date'], p['title']), reverse=True)
    FEATURED = ['miami-art-week-2026-free-guide', 'miami-luxury-real-estate-2026', 'best-photo-spots-miami']
    for l in posts: posts[l].sort(key=lambda p: FEATURED.index(p['slug']) if p['slug'] in FEATURED else 99)
    return posts

def render_body(md_text):
    out = []
    for line in md_text.split('\n'):
        if line.startswith('!! '):
            txt = line[3:].strip()
            m = re.match(r'^\*{0,2}([^:]{1,40}?)\*{0,2}\s*[:—–-]\s+(.*)$', txt)
            if m:
                out.append(f'<div class="fact"><span class="fact-n">{markdown.markdown(m.group(1))[3:-4]}</span><span class="fact-t">{markdown.markdown(m.group(2))[3:-4]}</span></div>')
            else:
                out.append(f'<div class="fact"><span class="fact-t">{markdown.markdown(txt)[3:-4]}</span></div>')
            out.append('')
        else:
            out.append(line)
    md = markdown.Markdown(extensions=['tables', 'toc', 'sane_lists', 'attr_list'], extension_configs={'toc': {'toc_depth': '2'}})
    h = md.convert('\n'.join(out))
    h = re.sub(r'<table>', '<div class="table-wrap"><table>', h); h = h.replace('</table>', '</table></div>')
    h = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', h)
    return h, md.toc_tokens

def cat_label(lang, c): return c if lang == 'en' else CATS[c][1]
def cat_slug(c): return re.sub(r'[^a-z]+', '-', c.lower()).strip('-')

def cover(p, big=False):
    color = CATS[p['category']][0]
    if p.get('cover_image'):
        credit = f'<span class="cover-credit">{esc(p.get("cover_credit",""))}</span>' if big and p.get('cover_credit') else ''
        src = p['cover_image'] if big else p['cover_image'].replace('.webp', '-sm.webp')
        return f'<div class="cover img{" big" if big else ""}" style="--c:{color}"><img src="{esc(src)}" alt="{esc(p.get("cover_alt",""))}" style="object-position:{esc(p.get("cover_position","center"))}" loading="{"eager" if big else "lazy"}">{credit}</div>'
    word = p['category'].split(' ')[0]
    return f'<div class="cover{" big" if big else ""}" style="--c:{color}"><span class="cover-word">{esc(word)}</span><span class="cover-cat">{esc(cat_label(p["lang"], p["category"]))}</span></div>'

def card(lang, p, big=False):
    t = T[lang]
    url = f'{T[lang]["journal_url"]}{p["slug"]}.html'
    return f'''<article class="post-card{' feature' if big else ''}" data-cat="{cat_slug(p['category'])}"><a href="{url}">{cover(p, big)}
<div class="pc-body"><div class="pc-meta"><span class="chip" style="--c:{CATS[p['category']][0]}">{esc(cat_label(lang,p['category']))}</span><span>{p.get('reading_minutes','')} {t['read']}</span></div>
<h3>{esc(p['title'])}</h3><p>{esc(p.get('excerpt',''))}</p></div></a></article>'''

def build_blog(posts):
    for lang in ('en', 'es'):
        t = T[lang]; other = 'es' if lang == 'en' else 'en'
        other_slugs = {p['slug'] for p in posts[other]}
        lst = posts[lang]
        # index
        cats = []
        for p in lst:
            if p['category'] not in cats: cats.append(p['category'])
        chips = f'<button class="filter on" data-f="all">{t["all"]}</button>' + ''.join(
            f'<button class="filter" data-f="{cat_slug(c)}" style="--c:{CATS[c][0]}">{esc(cat_label(lang,c))}</button>' for c in cats)
        feat = card(lang, lst[0], True) if lst else ''
        grid = ''.join(card(lang, p) for p in lst[1:])
        idx_path = t['journal_url']; idx_alt = T[other]['journal_url']
        itemlist = {"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"url":BASE+t['journal_url']+p['slug']+'.html',"name":p['title']} for i,p in enumerate(lst)]}
        body = f'''<div class="journal-hero wrap"><div class="eyebrow">MIAGAZINE · {t['journal']}</div><h1>{t['journal_title']}</h1><p>{t['journal_sub']}</p></div>
<div class="wrap"><div class="filters" role="group">{chips}</div>{feat}<div class="post-grid">{grid}</div></div>
<section class="cta-band"><div class="wrap"><h2>{t['cta_title']}</h2>{subform(lang)}<p class="small">{t['sub_note']}</p></div></section>
<script>document.querySelectorAll('.filter').forEach(b=>b.onclick=()=>{{document.querySelectorAll('.filter').forEach(x=>x.classList.toggle('on',x===b));const f=b.dataset.f;document.querySelectorAll('.post-card').forEach(c=>c.hidden=!(f==='all'||c.dataset.cat===f))}})</script>'''
        page(lang, idx_path, idx_alt, f"{t['journal_title']} — MIAGAZINE", t['journal_sub'], body, f'<script type="application/ld+json">{json.dumps(itemlist)}</script>')
        # posts
        for i, p in enumerate(lst):
            path = f"{t['journal_url']}{p['slug']}.html"
            alt = f"{T[other]['journal_url']}{p['slug']}.html" if p['slug'] in other_slugs else T[other]['journal_url']
            body_html, toc = render_body(p['body'])
            words = len(re.sub(r'<[^>]+>', ' ', body_html).split())
            mins = p.get('reading_minutes') or max(3, round(words / 230))
            tldr = ''.join(f'<li>{markdown.markdown(str(x))[3:-4]}</li>' for x in p.get('tldr', []) or [])
            faq = p.get('faq', []) or []
            faq_html = ''.join(f'<details><summary>{esc(q["q"])}</summary><p>{esc(q["a"])}</p></details>' for q in faq)
            srcs = p.get('sources', []) or []
            src_html = ''.join(f'<li><a href="{esc(s["url"])}" target="_blank" rel="noopener">{esc(s["title"])}</a></li>' for s in srcs)
            toc_html = ''.join(f'<li><a href="#{x["id"]}">{esc(html.unescape(x["name"]))}</a></li>' for x in toc)
            rel = [x for x in lst if x is not p and x['category'] == p['category']] + [x for x in lst if x is not p and x['category'] != p['category']]
            rel_html = ''.join(card(lang, x) for x in rel[:3])
            color = CATS[p['category']][0]
            ld = [{"@context":"https://schema.org","@type":"Article","headline":p['title'],"description":p.get('excerpt',''),"inLanguage":lang,
                   "datePublished":p['date'],"dateModified":p['date'],"articleSection":p['category'],"wordCount":words,
                   "author":{"@type":"Organization","name":"MIAGAZINE Editorial","url":BASE+P(lang,'/about.html')},
                   "publisher":{"@type":"NewsMediaOrganization","name":"MIAGAZINE","url":BASE},"mainEntityOfPage":BASE+path,
                   "citation":[s['url'] for s in srcs]},
                  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
                   {"@type":"ListItem","position":1,"name":"MIAGAZINE","item":BASE+t['home']},
                   {"@type":"ListItem","position":2,"name":t['journal'],"item":BASE+t['journal_url']},
                   {"@type":"ListItem","position":3,"name":p['title'],"item":BASE+path}]}]
            if faq: ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q['q'],"acceptedAnswer":{"@type":"Answer","text":q['a']}} for q in faq]})
            extra = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
            d = datetime.date.fromisoformat(p['date'])
            dstr = d.strftime('%b %d, %Y') if lang == 'en' else f"{d.day} {['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'][d.month-1]} {d.year}"
            body = f'''<div class="progress" aria-hidden="true"><span id="prog" style="background:{color}"></span></div>
<article class="post" style="--c:{color}">
<header class="post-head wrap"><a class="back" href="{t['journal_url']}">← {t['back']}</a>
<div class="pc-meta"><span class="chip" style="--c:{color}">{esc(cat_label(lang,p['category']))}</span><span>{mins} {t['read']}</span><span>{t['updated']} {dstr}</span></div>
<h1>{esc(p['title'])}</h1><p class="dek">{esc(p.get('excerpt',''))}</p><p class="small">{t['by']}</p></header>
<div class="wrap">{cover(p, True)}</div>
<div class="post-layout wrap"><aside class="toc"><div class="eyebrow">{t['toc']}</div><ol>{toc_html}</ol>
<div class="share"><div class="eyebrow">{t['share']}</div><button class="btn ghost" id="copy" type="button">{t['copy']}</button></div></aside>
<div class="post-main"><div class="tldr"><div class="eyebrow">{t['in30']}</div><ul>{tldr}</ul></div>
<div class="article-body">{body_html}</div>
{f'<section class="faq"><h2>{t["faq"]}</h2>{faq_html}</section>' if faq else ''}
<section class="sources"><h2>{t['sources']}</h2><ol>{src_html}</ol></section>
{f'<p class="small cover-brief"><strong>{t["cover"]}:</strong> {esc(p["cover_hint"])}</p>' if p.get('cover_hint') else ''}
</div></div></article>
<section class="cta-band"><div class="wrap"><h2>{t['cta_title']}</h2>{subform(lang)}<p class="small">{t['sub_note']}</p></div></section>
<section><div class="wrap"><div class="eyebrow">{t['related']}</div><div class="post-grid" style="margin-top:24px">{rel_html}</div></div></section>
<script>const pr=document.getElementById('prog');addEventListener('scroll',()=>{{const a=document.querySelector('.post');const r=a.getBoundingClientRect();const tot=a.offsetHeight-innerHeight;pr.style.width=Math.min(100,Math.max(0,-r.top/tot*100))+'%'}},{{passive:true}});
document.getElementById('copy').onclick=async e=>{{try{{await navigator.clipboard.writeText(location.href);e.target.textContent='{t['copied']}'}}catch(_){{}}}};</script>'''
            if p.get('cover_image'): extra += f'<meta property="og:image" content="{BASE}{esc(p["cover_image"])}">'
            page(lang, path, alt, f"{p['title']} | MIAGAZINE", p.get('excerpt', ''), body, extra, 'article')
    return posts

# ---------------- STATIC PAGES -----------------
def build_pages(posts):
    for lang in ('en', 'es'):
        t = T[lang]; o = 'es' if lang == 'en' else 'en'
        L = lambda en, es: en if lang == 'en' else es
        latest = ''.join(card(lang, p) for p in posts[lang][:6])
        home = f'''<div class="hero wrap"><div class="eyebrow">{L('Miami · Visual Luxury Magazine','Miami · Revista visual de lujo')}</div><h1>{t['tagline']}</h1>
<p>{L('Fashion, design, real estate, music, food and life on the water — photographed by the people who live it. One beautiful email every Thursday.','Moda, diseño, real estate, música, gastronomía y vida en el agua, fotografiados por quienes los viven. Un email hermoso cada jueves.')}</p>
{subform(lang)}<p class="small" style="margin-top:10px">{t['sub_note']}</p></div>
<div class="wrap"><figure class="home-feature"><img src="/assets/img/edition-02-art-deco-at-50-cover.webp" alt="{L('A model in a white linen suit and straw hat leans on a mint vintage convertible in front of a pink and mint Art Deco facade.','Una modelo con traje de lino blanco y sombrero de paja se apoya en un convertible vintage menta frente a una fachada Art Deco rosa y menta.')}" style="object-position:center 60%">
<figcaption><span class="eyebrow">{L('Coming in January','Llega en enero')}</span><strong>Art Deco at 50</strong><span>{L('Edition #02 · Art Deco Weekend, Jan 15–17, 2027','Edición #02 · Art Deco Weekend, 15–17 ene 2027')}</span></figcaption><small>{L('AI-generated illustration','Ilustración generada con IA')}</small></figure></div>
<section><div class="wrap"><div class="eyebrow">{t['journal']}</div><h2>{t['latest']}</h2><div class="post-grid">{latest}</div>
<div class="ctas" style="justify-content:flex-start"><a class="btn ghost" href="{t['journal_url']}">{L('Read the Journal','Leer el Journal')} →</a></div></div></section>
<section class="dark"><div class="wrap split"><div><div class="eyebrow">{L('For photographers','Para fotógrafos')}</div><h2>{L('Made by the lens collective.','Hecha por el colectivo del lente.')}</h2><p>{L('Submit your editorial, get published with full credit and a link to your portfolio, and earn 20% on every partnership you bring.','Envía tu editorial, publica con crédito completo y link a tu portafolio, y gana 20% de cada alianza que traigas.')}</p><div class="ctas" style="justify-content:flex-start"><a class="btn light" href="{P(lang,'/submit.html')}">{t['submit']}</a></div></div>
<div><div class="eyebrow">{L('For brands','Para marcas')}</div><h2>{L('Be seen beautifully.','Hazte ver con belleza.')}</h2><p>{L('Newsletter sponsorships, photographed brand stories, event coverage and a place in our Miami guide. Founding rates for our first 10 partners.','Patrocinio de newsletter, historias de marca fotografiadas, cobertura de eventos y un lugar en nuestra guía de Miami. Tarifas fundadoras para los primeros 10 socios.')}</p><div class="ctas" style="justify-content:flex-start"><a class="btn light" href="{P(lang,'/advertise.html')}">{t['advertise']}</a></div></div></div></section>
<section class="jobs-band"><div class="wrap"><div><div class="eyebrow">{L('Careers','Vacantes')}</div><h2>{L('Join the collective.','Únete al colectivo.')}</h2><p class="small">{L('Photographers, filmmakers, bilingual reporters, creators, sales and PR. Interviews by appointment only.','Fotógrafos, filmmakers, reporteros bilingües, creadores, ventas y relaciones públicas. Entrevistas solo con previa cita.')}</p></div><a class="btn" href="{P(lang,'/careers.html')}">{L('See open positions','Ver vacantes')}</a></div></section>'''
        page(lang, P(lang, '/'), P(o, '/'), f"MIAGAZINE — {t['tagline']}", L("Miami's visual luxury magazine: fashion, design, real estate, music, food and waterfront living, photographed by Miami photographers. Free weekly newsletter.", "La revista visual de lujo de Miami: moda, diseño, real estate, música, gastronomía y vida en el agua, fotografiada por fotógrafos de Miami. Newsletter semanal gratis."), home)

        stories = f'''<div class="hero wrap"><div class="eyebrow">{t['stories']}</div><h1>{L('The edition','La edición')}</h1><p>{L('Photographic editorials from our photographer network. First stories land during Miami Art Week.','Editoriales fotográficos de nuestra red de fotógrafos. Las primeras historias llegan en Miami Art Week.')}</p></div>
<div class="wrap"><figure class="page-hero short"><img src="/assets/img/stories-open-call-hero.webp" alt="{L('Film negatives on a light table with one frame circled in orange.','Negativos sobre una mesa de luz con un cuadro marcado en naranja.')}" style="object-position:center 55%"><figcaption>{L('AI-generated illustration','Ilustración generada con IA')}</figcaption></figure></div>
<section><div class="wrap grid"><article class="card"><a href="/stories/golden-hour-key-biscayne.html"><div class="ph"><span>Waterfront</span></div><h3>Golden Hour, Key Biscayne</h3><p>{L('Story template','Plantilla de historia')}</p></a></article>
<article class="card"><a href="{P(lang,'/submit.html')}"><div class="ph c"><span>Open call</span></div><h3>{L('Your story here','Tu historia aquí')}</h3><p>{L('Submit an editorial','Envía un editorial')}</p></a></article></div></section>'''
        page(lang, P(lang, '/stories/'), P(o, '/stories/'), f"{t['stories']} — MIAGAZINE", L('Photographic editorials from Miami.','Editoriales fotográficos de Miami.'), stories)

        li = lambda items: ''.join(f'<li>{x}</li>' for x in items)
        submit = f'''<div class="hero wrap"><div class="eyebrow">{L('Open call · Nov–Dec 2026','Convocatoria · nov–dic 2026')}</div><h1>{L('Art Week Through the Lens','Art Week a través del lente')}</h1><p>{L('Free to submit. Full credit. A link to your portfolio. 20% of every partnership you bring.','Gratis. Crédito completo. Link a tu portafolio. 20% de cada alianza que traigas.')}</p><div class="ctas"><a class="btn" href="TALLY_FORM_URL">{L('Submit an editorial','Enviar editorial')}</a></div></div>
<div class="wrap"><figure class="page-hero short"><img src="/assets/img/social-open-call-story.webp" alt="{L('A photographer holds a vintage camera against an orange and pink wall.','Un fotógrafo sostiene una cámara vintage frente a un muro naranja y rosa.')}" style="object-position:center 55%"><figcaption>{L('AI-generated illustration','Ilustración generada con IA')}</figcaption></figure></div>
<section><div class="wrap split"><div><h2>{L('What you get','Qué recibes')}</h2><ul class="list">{li(L(['Publication on miagazine.com, in The Lens newsletter and on our social channels','Full credits for your team and a photographer profile linked to your portfolio','A share kit and a “Published in MIAGAZINE” badge','20% commission on any brand or venue you refer that becomes a partner','Priority for paid assignments and invitations to our events'],['Publicación en miagazine.com, en el newsletter The Lens y en nuestras redes','Créditos completos para tu equipo y perfil de fotógrafo con link a tu portafolio','Kit para compartir y badge “Published in MIAGAZINE”','20% de comisión por cada marca o venue que refieras y se vuelva socio','Prioridad en encargos pagados e invitaciones a nuestros eventos']))}</ul></div>
<div><h2>{L('Guidelines','Requisitos')}</h2><ul class="list">{li(L(['8–20 images, minimum 3000px long side, sRGB JPG, no watermarks','Unpublished in other magazines (your own social is fine)','Shot in Miami or South Florida, or with a clear Miami connection','Title, 80–150 words of story, and complete credits','Model and location releases where applicable','Real photography only — no generative AI imagery'],['8–20 imágenes, mínimo 3000 px lado largo, JPG sRGB, sin marca de agua','Inéditas en otras revistas (tus redes sí cuentan)','Hechas en Miami o South Florida, o con conexión clara con Miami','Título, 80–150 palabras de historia y créditos completos','Releases de modelo y locación cuando aplique','Solo fotografía real, sin imágenes de IA generativa']))}</ul></div></div></section>
<section><div class="wrap prose"><h2>{L('Rights','Derechos')}</h2><p>{L('You keep your copyright. By submitting, you grant MIAGAZINE a non-exclusive license to publish your images with credit on our website, newsletter, social channels, quarterly issues and promotion. Any commercial use by a third-party brand requires your separate agreement and payment.','Conservas tu copyright. Al enviar, das a MIAGAZINE una licencia no exclusiva para publicar tus imágenes con crédito en web, newsletter, redes, ediciones trimestrales y promoción. Cualquier uso comercial de una marca requiere tu acuerdo aparte y pago.')}</p><p>{L('We reply to every submission within 48 hours.','Respondemos cada envío en 48 horas.')}</p></div></section>'''
        page(lang, P(lang, '/submit.html'), P(o, '/submit.html'), L('Submit Your Work — Open Call for Miami Photographers | MIAGAZINE','Publica tu trabajo — Convocatoria para fotógrafos de Miami | MIAGAZINE'), L('Open call for Miami photographers: free to submit, full credit, 20% partner commission.','Convocatoria para fotógrafos de Miami: envío gratis, crédito completo, 20% de comisión.'), submit)

        K = KIT.C[lang]
        keys = ['STRIPE_NEWSLETTER','STRIPE_HOMEPAGE','STRIPE_SELECTS','STRIPE_STORY','STRIPE_REEL','STRIPE_EVENT','STRIPE_FILM','STRIPE_ISSUE']
        tr = ''.join(f'<tr><td><strong>{a}</strong><br><span class="small">{d}</span></td><td class="price">{b}</td><td class="small">{c}</td><td><a class="btn ghost" href="{k}">{L("Book","Reservar")}</a></td></tr>' for (a,b,c,d),k in zip(K['rows'], keys))
        bkeys = ['STRIPE_BUNDLE_ARTWEEK','STRIPE_BUNDLE_ARTDECO','STRIPE_BUNDLE_BOATSHOW']
        bundles_html = ''.join(f'<article class="bundle"><img src="/assets/img/{img}-sm.webp" alt="" loading="lazy"><div class="bi"><div class="eyebrow">{dt}</div><h3>{n}</h3><div class="bp">{pr}</div><ul>{"".join(f"<li>{x}</li>" for x in inc)}</ul><p class="small">{K["b_val"]}: <s>{val}</s> · {K["b_book"]} {bk}</p><a class="btn" href="{k}">{L("Book","Reservar")}</a></div></article>' for (n,pr,dt,inc,val,bk,img),k in zip(K['bundles'], bkeys))
        founding_html = f'<div class="founding"><div><div class="eyebrow" style="color:#e8cfa6">{K["p6_eye"]}</div><h2>{K["p6_h"]}</h2><p>{K["p6_sub"]}</p><ul>{"".join(f"<li>{x}</li>" for x in K["fp"])}</ul><p class="small">{K["fp_val"]}</p></div><div class="ctas" style="flex-direction:column;align-items:stretch"><a class="btn light" href="STRIPE_FOUNDING">{L("Pay $1,500 / year","Pagar $1,500 / año")}</a><a class="btn light" href="STRIPE_FOUNDING_QUARTERLY">{L("4 × $400 quarterly","4 × $400 trimestral")}</a><a class="btn light" href="CALENDLY_URL">{L("Book a 15-min call","Agendar llamada de 15 min")}</a></div></div>'
        adv = f'''<div class="hero wrap"><div class="eyebrow">{L('Partners · Founding rates','Socios · Tarifas fundadoras')}</div><h1>{L('Be seen beautifully.','Hazte ver con belleza.')}</h1><p>{L('MIAGAZINE puts Miami brands in front of an affluent, bilingual, design-minded audience — through photography, not banners.','MIAGAZINE pone a las marcas de Miami frente a una audiencia bilingüe, de alto poder adquisitivo y amante del diseño, con fotografía, no con banners.')}</p></div>
<section><div class="wrap"><div class="answer" style="margin-bottom:32px"><strong>{L('How much does it cost to advertise in MIAGAZINE?','¿Cuánto cuesta anunciarse en MIAGAZINE?')}</strong> {L('Founding rates start at $150 per newsletter sponsorship, $99/month for a guide listing, $450 for a Branded Reel and $650 for a photographed brand story. Event bundles start at $950. Ten Founding Partner spots are available at $1,500 per year or 4 quarterly payments of $400.','Las tarifas fundadoras empiezan en $150 por patrocinio de newsletter, $99/mes por ficha en la guía, $450 por Reel de marca y $650 por historia de marca fotografiada. Los paquetes por evento empiezan en $950. Hay 10 cupos de Socio Fundador a $1,500 al año o 4 pagos trimestrales de $400.')}</div>
<div class="ctas" style="justify-content:flex-start;margin:0 0 28px"><a class="btn" href="{P(lang,'/media-kit.html')}">{L('View the media kit','Ver el media kit')}</a><a class="btn ghost" href="/media-kit/MIAGAZINE-Media-Kit-2026-{'EN' if lang=='en' else 'ES'}.pdf">{L('Download PDF','Descargar PDF')}</a><a class="btn ghost" href="CALENDLY_URL">{L('Book a call','Agendar llamada')}</a></div>
<div class="table-wrap"><table><thead><tr><th>{L('Package','Paquete')}</th><th>{L('Rate','Tarifa')}</th><th>{L('Term','Plazo')}</th><th></th></tr></thead><tbody>{tr}</tbody></table></div></div></section>
<section><div class="wrap"><div class="eyebrow">{K['b_eye']}</div><h2>{K['b_h']}</h2><p class="small" style="margin:-12px 0 28px">{K['b_sub']}</p><div class="bundles">{bundles_html}</div></div></section>
<section class="dark"><div class="wrap">{founding_html}
<p class="small" style="margin-top:18px">{L('All paid content is labeled “Partner”. Questions: partners@miagazine.com','Todo contenido pagado se etiqueta “Partner”. Preguntas: partners@miagazine.com')}</p></div></section>'''
        page(lang, P(lang, '/advertise.html'), P(o, '/advertise.html'), L('Advertise in a Miami Luxury Magazine — Founding Rates | MIAGAZINE','Anúnciate en una revista de lujo de Miami — Tarifas fundadoras | MIAGAZINE'), L('Newsletter sponsorships from $150, Branded Reels, photographed brand stories, event coverage, event bundles and Founding Partner packages.','Patrocinios de newsletter desde $150, Reels de marca, historias fotografiadas, cobertura de eventos, paquetes por evento y Socio Fundador.'), adv)

        page(lang, P(lang, '/404.html'), P(o, '/404.html'), '404 — MIAGAZINE', 'Not found', f'<div class="hero wrap"><h1>{L("Out of frame.","Fuera de cuadro.")}</h1><p><a href="{t["home"]}">MIAGAZINE</a></p></div>')

LEGAL_ORDER = ['intellectual-property', 'privacy', 'cookies', 'terms', 'editorial-policy']

def page_path(slug):
    return f'/legal/{slug}.html' if slug in LEGAL_ORDER else f'/{slug}.html'

def render_page_body(md_text):
    out, kp = [], []
    def flush():
        if kp:
            out.append('<div class="keypoints">' + ''.join(kp) + '</div>'); out.append(''); kp.clear()
    for line in md_text.split('\n'):
        if line.startswith('!! '):
            txt = line[3:].strip(); m = re.match(r'^\*{0,2}([^:]{1,60}?)\*{0,2}:\s+(.*)$', txt)
            kp.append(f'<div><strong>{esc(m.group(1))}</strong><span>{markdown.markdown(m.group(2))[3:-4]}</span></div>' if m else f'<div><span>{markdown.markdown(txt)[3:-4]}</span></div>')
        else:
            flush(); out.append(line)
    flush()
    md = markdown.Markdown(extensions=['tables', 'toc', 'sane_lists', 'attr_list'], extension_configs={'toc': {'toc_depth': '2'}})
    h = md.convert('\n'.join(out))
    h = h.replace('<table>', '<div class="table-wrap"><table>').replace('</table>', '</table></div>')
    h = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener">', h).replace('rel="noopener">>', 'rel="noopener">')
    return h, md.toc_tokens

def build_content_pages():
    pages = {'en': {}, 'es': {}}
    for f in sorted(glob.glob(os.path.join(ROOT, 'content/pages/*.md'))):
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', open(f).read(), re.S)
        if not m: print('skip', f); continue
        meta = yaml.safe_load(m.group(1)); meta['body'] = m.group(2)
        lang = meta.get('lang') or f.split('.')[-2]; pages[lang][meta['slug']] = meta
    for lang in ('en', 'es'):
        t = T[lang]; o = 'es' if lang == 'en' else 'en'
        L = lambda en, es: en if lang == 'en' else es
        for slug, p in pages[lang].items():
            path = P(lang, page_path(slug)); alt = P(o, page_path(slug)) if slug in pages[o] else P(o, '/')
            body, toc = render_page_body(p['body'])
            d = datetime.date.fromisoformat(str(p.get('updated', TODAY)))
            dstr = d.strftime('%B %d, %Y') if lang == 'en' else f"{d.day} de {['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'][d.month-1]} de {d.year}"
            is_legal = slug in LEGAL_ORDER
            eyebrow = p.get('eyebrow') or ('Legal' if is_legal else 'MIAGAZINE')
            cta = f'<div class="ctas" style="justify-content:flex-start"><a class="btn" href="{esc(p["cta_url"])}">{esc(p["cta_label"])}</a><a class="btn ghost" href="mailto:careers@miagazine.com">careers@miagazine.com</a></div>' if p.get('cta_url') else ''
            legal_nav = ''
            if is_legal:
                items = ''.join(f'<li><a href="{P(lang, page_path(x))}"{" aria-current=page" if x == slug else ""}>{esc(pages[lang][x]["title"]) if x in pages[lang] else x}</a></li>' for x in LEGAL_ORDER)
                legal_nav = f'<div class="eyebrow" style="margin-top:28px">{L("Legal center","Centro legal")}</div><ol class="legal-list">{items}</ol>'
            toc_html = ''.join(f'<li><a href="#{x["id"]}">{esc(html.unescape(x["name"]))}</a></li>' for x in toc)
            hero_img = f'<div class="wrap"><figure class="page-hero"><img src="{esc(p["hero_image"])}" alt="{esc(p.get("hero_alt",""))}" style="object-position:{esc(p.get("hero_position","center"))}"><figcaption>{"AI-generated illustration" if lang=="en" else "Ilustración generada con IA"}</figcaption></figure></div>' if p.get('hero_image') else ''
            aside = f'<aside class="toc"><div class="eyebrow">{L("On this page","En esta página")}</div><ol>{toc_html}</ol>{legal_nav}</aside>' if is_legal else ''
            cls = 'post-layout wrap legal' if is_legal else 'wrap feature-page'
            html_body = f"""<article class="post" style="--c:{'#57534e' if is_legal else '#b08d57'}"><header class="post-head wrap"><div class="eyebrow">{esc(eyebrow)}</div><h1>{esc(p['title'])}</h1><p class="dek">{esc(p.get('summary',''))}</p>
<p class="small">{t['updated']}: {dstr}</p>{cta}</header>
{hero_img}<div class="{cls}">{aside}<div class="post-main page-body">{body}</div></div></article>"""
            ld = {"@context":"https://schema.org","@type":"AboutPage" if slug=='about' else "WebPage","name":p['title'],"inLanguage":lang,"dateModified":str(p.get('updated',TODAY)),"url":BASE+path,"isPartOf":{"@type":"WebSite","name":"MIAGAZINE","url":BASE}}
            extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
            if slug == 'careers':
                extra += f'<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"ItemList","name":p["title"],"itemListElement":[{"@type":"ListItem","position":i+1,"name":r} for i,r in enumerate(L(["Event & editorial photographer","Videographer / filmmaker","Bilingual reporter – writer","Content creator & social media","Partnerships executive","Publicist / PR","Model & talent casting","Internships"],["Fotógrafo/a de eventos y editorial","Videógrafo/a / filmmaker","Reportero/a – redactor/a bilingüe","Creador/a de contenido y social media","Ejecutivo/a de alianzas comerciales","Publicista / relaciones públicas","Casting de modelos y talento","Pasantías"]))]}, ensure_ascii=False)}</script>'
            page(lang, path, alt, f"{p['title']} | MIAGAZINE", p.get('summary', ''), html_body, extra)
        # legal hub
        cards = ''.join(f'<a class="legal-card" href="{P(lang, page_path(x))}"><h3>{esc(pages[lang][x]["title"])}</h3><p>{esc(pages[lang][x].get("summary",""))}</p><span>→</span></a>' for x in LEGAL_ORDER if x in pages[lang])
        hub = f"""<div class="post-head wrap"><div class="eyebrow">Legal</div><h1>{L('Legal center','Centro legal')}</h1><p class="dek">{L('How we protect creators, readers and partners: intellectual property, permissions, privacy, cookies, terms and editorial standards.','Cómo protegemos a creadores, lectores y marcas: propiedad intelectual, permisos, privacidad, cookies, términos y estándares editoriales.')}</p></div>
<div class="wrap"><figure class="page-hero short"><img src="/assets/img/legal-hero.webp" alt="{L('A brass camera-shaped paperweight and a fountain pen on cream paper.','Un pisapapeles de latón con forma de cámara y una pluma fuente sobre papel crema.')}" style="object-position:center 55%"><figcaption>{L('AI-generated illustration','Ilustración generada con IA')}</figcaption></figure></div>
<section><div class="wrap legal-grid">{cards}<a class="legal-card" href="#" data-cookie-prefs><h3>{COOKIE_TXT[lang]['prefs']}</h3><p>{L('Change your cookie choices at any time.','Cambia tu elección de cookies cuando quieras.')}</p><span>→</span></a></div>
<div class="wrap"><p class="small" style="margin-top:28px">{L('Legal requests: legal@miagazine.com · Privacy: privacy@miagazine.com · Copyright (DMCA): dmca@miagazine.com','Solicitudes legales: legal@miagazine.com · Privacidad: privacy@miagazine.com · Derechos de autor (DMCA): dmca@miagazine.com')}</p></div></section>"""
        page(lang, P(lang, '/legal/'), P(o, '/legal/'), f"{L('Legal center','Centro legal')} | MIAGAZINE", L('Intellectual property, permissions, privacy, cookies, terms and editorial policy.','Propiedad intelectual, permisos, privacidad, cookies, términos y política editorial.'), hub)
    return pages

def build_media_kit_page():
    for lang in ('en','es'):
        K = KIT.C[lang]; o = 'es' if lang == 'en' else 'en'; L = lambda en, es: en if lang == 'en' else es
        pdf = f"/media-kit/MIAGAZINE-Media-Kit-2026-{'EN' if lang=='en' else 'ES'}.pdf"
        stats = ''.join(f'<div class="mk-stat"><div class="n">{n}</div><div>{l}</div><span>{s_}</span></div>' for n,l,s_ in K['stats'])
        pill = ''.join(f'<div><h3>{a}</h3><p>{b}</p></div>' for a,b in K['pillars'])
        ch = ''.join(f'<li><strong>{a}</strong> — {b}</li>' for a,b in K['ch'])
        goals = ''.join(f'<div><b>{n}</b><span>{l}</span></div>' for n,l in K['goals'])
        rows = ''.join(f'<tr><td><strong>{a}</strong><br><span class="small">{d}</span></td><td class="price">{b}</td><td class="small">{c}</td></tr>' for a,b,c,d in K['rows'])
        bund = ''.join(f'<article class="bundle"><img src="/assets/img/{img}-sm.webp" alt="" loading="lazy"><div class="bi"><div class="eyebrow">{dt}</div><h3>{n}</h3><div class="bp">{pr}</div><ul>{"".join(f"<li>{x}</li>" for x in inc)}</ul><p class="small">{K["b_val"]}: <s>{val}</s> · {K["b_book"]} {bk}</p></div></article>' for n,pr,dt,inc,val,bk,img in K['bundles'])
        cal = ''.join(f'<tr><td class="price" style="font-size:20px">{m}</td><td><strong>{t}</strong></td><td>{e}</td><td class="small">{f}</td></tr>' for m,t,e,f in K['cal'])
        body = f'''<div class="mk-hero"><img src="/assets/img/edition-02-art-deco-at-50-cover.webp" alt=""><div class="wrap"><div class="eyebrow" style="color:#f2d8ae">MIAGAZINE · {K['kit']} {K['season']}</div><h1>{K['kit']}</h1><p>{K['tag']} {K['founding']}</p>
<div class="ctas" style="justify-content:flex-start"><a class="btn light" href="CALENDLY_URL">{L('Book a 15-min call','Agendar llamada de 15 min')}</a><a class="btn light" href="{pdf}">{L('Download PDF','Descargar PDF')}</a></div></div><small>{K['credit']}</small></div>
<section><div class="wrap split"><div><div class="eyebrow">{K['p2_eye']}</div><h2>{K['p2_h']}</h2><p>{K['p2_p']}</p></div><div class="mk-pill">{pill}</div></div></section>
<section><div class="wrap"><div class="eyebrow">{K['p3_eye']}</div><h2>{K['p3_h']}</h2><div class="mk-stats">{stats}</div><p class="small">{K['p3_note']}</p></div></section>
<section><div class="wrap split"><div><div class="eyebrow">{K['p4_eye']}</div><h2>{K['p4_h']}</h2><ul class="list">{"".join(f"<li>{x}</li>" for x in K['aud'])}</ul></div><div><ul class="list">{ch}</ul></div></div>
<div class="wrap"><div class="mk-goals"><div class="eyebrow" style="color:#e8cfa6">{K['goals_t']}</div><div class="g">{goals}</div><p>{K['goals_note']}</p></div></div></section>
<section><div class="wrap"><div class="eyebrow">{K['p5_eye']}</div><h2>{K['p5_h']}</h2><div class="table-wrap"><table><tbody>{rows}</tbody></table></div></div></section>
<section><div class="wrap"><div class="eyebrow">{K['b_eye']}</div><h2>{K['b_h']}</h2><p class="small" style="margin:-12px 0 28px">{K['b_sub']}</p><div class="bundles">{bund}</div></div></section>
<section><div class="wrap"><div class="eyebrow">{K['s_eye']}</div><h2>{K['s_h']}</h2><div class="mock-web">{KIT.mock(K, '/assets/img/', '-sm.webp')}</div><p class="small">{K['s_note']}</p></div></section>
<section class="dark"><div class="wrap">{'<div class="founding"><div><div class="eyebrow" style="color:#e8cfa6">'+K['p6_eye']+'</div><h2>'+K['p6_h']+'</h2><p>'+K['p6_sub']+'</p><ul>'+''.join(f"<li>{x}</li>" for x in K['fp'])+'</ul><p class="small">'+K['fp_val']+'</p></div><div><div class="eyebrow" style="color:#e8cfa6">'+K['how_t']+'</div><ol class="how">'+''.join(f"<li><strong>{a}</strong> {b}</li>" for a,b in K['how'])+'</ol></div></div>'}</div></section>
<section><div class="wrap"><div class="eyebrow">{K['p7_eye']}</div><h2>{K['p7_h']}</h2><div class="table-wrap"><table><tbody>{cal}</tbody></table></div><p class="small">{K['cal_note']}</p></div></section>
<section><div class="wrap three-col"><div><h3>{K['specs_t']}</h3><ul class="list">{"".join(f"<li>{x}</li>" for x in K['specs'])}</ul></div><div><h3>{K['terms_t']}</h3><ul class="list">{"".join(f"<li>{x}</li>" for x in K['terms'])}</ul></div><div><h3>{K['vis_t']}</h3><ul class="list">{"".join(f"<li>{x}</li>" for x in K['vis'])}</ul></div></div></section>
<section class="cta-band"><div class="wrap"><h2>{K['cta']}</h2><p class="small">{K['cta_sub']}</p><div class="ctas"><a class="btn light" href="CALENDLY_URL">{L('Book a call','Agendar llamada')}</a><a class="btn light" href="mailto:partners@miagazine.com">partners@miagazine.com</a><a class="btn light" href="WHATSAPP_URL">WhatsApp</a></div></div></section>'''
        page(lang, P(lang,'/media-kit.html'), P(o,'/media-kit.html'), f"{K['kit']} {K['season']} | MIAGAZINE", L('MIAGAZINE media kit: audience, formats and rates, Branded Reels, event bundles for Art Week, Art Deco Weekend and the Boat Show, and Founding Partner offer.','Media kit de MIAGAZINE: audiencia, formatos y tarifas, Reels de marca, paquetes para Art Week, Art Deco Weekend y Boat Show, y oferta de Socio Fundador.'), body)

def apply_integrations():
    cfg = os.path.join(ROOT, 'config', 'integrations.json')
    if not os.path.exists(cfg): return
    raw = json.load(open(cfg))
    if raw.get('PREVIEW_NOINDEX'):
        for f in glob.glob(os.path.join(OUT, '**/*.html'), recursive=True):
            h = open(f).read()
            if 'name="robots"' not in h:
                open(f, 'w').write(h.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex, nofollow">', 1))
        open(os.path.join(OUT, 'robots.txt'), 'w').write('# Preview on temporary domain: not for indexing\nUser-agent: *\nDisallow: /\n')
    else:
        shutil.copy(os.path.join(ROOT, 'build', 'robots.prod.txt'), os.path.join(OUT, 'robots.txt'))
    vals = {k: v for k, v in raw.items() if not k.startswith('_') and isinstance(v, str) and v}
    if not vals: return
    for f in glob.glob(os.path.join(OUT, '**/*.html'), recursive=True):
        h = open(f).read(); n = h
        for k, v in sorted(vals.items(), key=lambda kv: -len(kv[0])): n = n.replace(k, v)
        if n != h: open(f, 'w').write(n)

def build_meta(posts):
    urls = []
    for lang in ('en','es'):
        for p in ['/', '/stories/', '/submit.html', '/advertise.html', '/media-kit.html', '/about.html', '/careers.html', '/legal/'] + [f'/legal/{x}.html' for x in LEGAL_ORDER]: urls.append((P(lang,p), TODAY))
        urls.append((T[lang]['journal_url'], TODAY))
        for x in posts[lang]: urls.append((T[lang]['journal_url']+x['slug']+'.html', x['date']))
    urls += [('/stories/golden-hour-key-biscayne.html', TODAY), ('/guides/miami-art-week-2026.html', TODAY)]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{BASE}{u}</loc><lastmod>{d}</lastmod></url>\n' for u,d in urls) + '</urlset>\n'
    write('/sitemap.xml', sm)
    lines = ['# MIAGAZINE', '', '> MIAGAZINE is a bilingual (English/Spanish) digital luxury magazine about Miami, founded in 2026. It publishes photographic editorials by a curated network of Miami photographers and a researched, sourced Journal on fashion & models, real estate, economy, music, trends, food & drink, tech, waterfront, design & architecture and photography, plus a free weekly newsletter, The Lens (Thursdays).', '',
             'Key facts:', '- Coverage: Miami and South Florida: luxury, events, nightlife, public events, art, fashion, real estate, economy, music, tech.', '- Team: a select collective of publicists, reporters, photographers, filmmakers and content creators. Open positions by appointment only (careers page).', '- Photographers submit for free, keep copyright, get full credit and earn 20% on partnerships they refer.',
             '- Advertising founding rates: newsletter sponsorship $150/issue, MIA Selects listing $99/month, Branded Reel $450, Branded Story $650, Event Coverage $900, Event Recap Film $1,200, event bundles from $950, Founding Partner $1,500/year or 4 x $400.',
             '- Editorial policy: real photography only; paid content labeled "Partner"; speculative pieces labeled as fiction.', '',
             '## Main pages', f'- [Home]({BASE}/)', f'- [Inicio (ES)]({BASE}/es/)', f'- [Submit]({BASE}/submit.html)', f'- [Advertise]({BASE}/advertise.html)', f'- [Media kit]({BASE}/media-kit.html)', f'- [About]({BASE}/about.html)', f'- [Careers]({BASE}/careers.html)', f'- [Legal center]({BASE}/legal/)', f'- [Intellectual property & permissions]({BASE}/legal/intellectual-property.html)', f'- [Editorial policy]({BASE}/legal/editorial-policy.html)', '', '## Journal (English)']
    lines += [f"- [{x['title']}]({BASE}/blog/{x['slug']}.html): {x.get('excerpt','')}" for x in posts['en']]
    lines += ['', '## Journal (Español)'] + [f"- [{x['title']}]({BASE}/es/blog/{x['slug']}.html): {x.get('excerpt','')}" for x in posts['es']]
    write('/llms.txt', '\n'.join(lines) + '\n')

def refresh_legacy():
    # hand-made EN pages: swap in current nav
    for f in ['/stories/golden-hour-key-biscayne.html', '/guides/miami-art-week-2026.html']:
        full = os.path.join(OUT, f.lstrip('/'))
        if os.path.exists(full):
            h = open(full).read()
            h = re.sub(r'<header class="top">.*?</header>', nav('en', '/es/blog/'), h, flags=re.S)
            open(full, 'w').write(h)

if __name__ == '__main__':
    posts = load_posts(); refresh_legacy()
    build_blog(posts); build_pages(posts); build_content_pages(); build_media_kit_page(); build_meta(posts); apply_integrations()
    print('posts en/es:', len(posts['en']), len(posts['es']))
