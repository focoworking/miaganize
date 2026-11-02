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
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Oswald:wght@400;500;600&family=Lora:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet"><script>document.documentElement.classList.add("js")</script>
<link rel="stylesheet" href="/assets/style.css"><link rel="icon" href="/assets/favicon.svg">
<script type="application/ld+json">{json.dumps(ORG)}</script>{extra}</head><body>'''

def nav(lang, alt_path):
    t = T[lang]; L = lambda en, es: en if lang == 'en' else es
    links = [(t['home'], L('Home','Inicio')), (t['journal_url'], 'Journal'), (P(lang,'/stories/'), t['stories']), (P(lang,'/submit.html'), t['submit']),
             (P(lang,'/advertise.html'), t['advertise']), (P(lang,'/media-kit.html'), 'Media kit'), (P(lang,'/about.html'), t['about']), (P(lang,'/careers.html'), L('Careers','Vacantes'))]
    oc = ''.join(f'<a href="{u}">{esc(n)}</a>' for u, n in links)
    return f"""<header class="hdr" id="hdr"><nav class="tabs" aria-label="{L('Audiences','Audiencias')}"><a class="on" href="{t['journal_url']}">{L('Read','Lee')}</a><a href="{P(lang,'/advertise.html')}">{L('Brands','Marcas')}</a><a href="{P(lang,'/submit.html')}">{L('Create','Crea')}</a></nav>
<a class="hdr-logo" href="{t['home']}">MIAGAZINE</a>
<div class="hdr-r"><a class="hdr-lang" href="{alt_path}" hreflang="{t['other']}" lang="{t['other']}">{t['other_label']}</a><button class="burger" id="burger" type="button" aria-controls="oc" aria-expanded="false" aria-label="{L('Open menu','Abrir menú')}"><i></i><i></i><i></i></button></div></header>
<div class="oc-shade" id="oc-shade"></div>
<aside class="oc" id="oc" aria-label="{L('Menu','Menú')}"><button class="oc-x" id="oc-x" type="button" aria-label="{L('Close menu','Cerrar menú')}">×</button>
<a class="oc-logo" href="{t['home']}"><span>MIAGAZINE</span><em>{L('through the lens','a través del lente')}</em></a>
<nav class="oc-links">{oc}</nav><div class="oc-sub"><a href="{P(lang,'/legal/')}">Legal</a><a href="{alt_path}">{t['lang_name'] if False else ('Español' if lang=='en' else 'English')}</a><a href="https://instagram.com/miagazine">Instagram</a></div></aside>"""

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
    return f"""<footer class="ft"><div class="ft-in">
<div class="ft-ack"><h3>{L('Welcome to Miami','Bienvenidos a Miami')}</h3><p>{L('We acknowledge the Tequesta, Miccosukee and Seminole peoples, original stewards of the lands and waters of South Florida.','Reconocemos a los pueblos Tequesta, Miccosukee y Seminola, custodios originales de las tierras y aguas del sur de Florida.')}</p><p>{t['tagline']} {t['footer']}</p></div>
<div class="ft-cols"><div><h4>MIAGAZINE</h4><a href="{t['journal_url']}">{t['journal']}</a><a href="{P(lang,'/stories/')}">{t['stories']}</a><a href="{P(lang,'/submit.html')}">{t['submit']}</a><a href="{P(lang,'/advertise.html')}">{t['advertise']}</a><a href="{P(lang,'/media-kit.html')}">Media kit</a><a href="{P(lang,'/about.html')}">{t['about']}</a><a href="{P(lang,'/careers.html')}">{L('Careers','Vacantes')}</a></div>
<div><h4>Legal</h4><a href="{P(lang,'/legal/intellectual-property.html')}">{L('IP & Permissions','Propiedad intelectual')}</a><a href="{P(lang,'/legal/privacy.html')}">{L('Privacy','Privacidad')}</a><a href="{P(lang,'/legal/cookies.html')}">Cookies</a><a href="{P(lang,'/legal/terms.html')}">{L('Terms','Términos')}</a><a href="{P(lang,'/legal/editorial-policy.html')}">{L('Editorial policy','Política editorial')}</a><a href="#" data-cookie-prefs>{c['prefs']}</a></div>
<div><h4>{L('Contact','Contacto')}</h4><span>editorial@miagazine.com</span><span>partners@miagazine.com</span><span>careers@miagazine.com</span><span>Miami, FL</span></div></div>
<div class="ft-brand"><h4>{L('Find us on','Síguenos')}</h4><div class="ft-soc"><a href="https://instagram.com/miagazine" aria-label="Instagram">IG</a><a href="https://www.tiktok.com/@miagazine" aria-label="TikTok">TT</a><a href="https://pinterest.com/miagazine" aria-label="Pinterest">PI</a><a href="https://www.linkedin.com/company/miagazine" aria-label="LinkedIn">IN</a></div>
<a class="ft-lock" href="{t['home']}"><span>MIAGAZINE</span><em>{L('through the lens','a través del lente')}</em></a><p class="ft-copy">© 2026 MIAGAZINE · {L('Photographs © their respective authors.','Fotografías © de sus autores.')}</p></div>
</div></footer><div class="scrollbar" aria-hidden="true"><span id="scrollbar"></span></div>
{cookie_banner(lang)}
<script>(function(){{
var h=document.getElementById('hdr'),oc=document.getElementById('oc'),sh=document.getElementById('oc-shade'),bu=document.getElementById('burger'),sb=document.getElementById('scrollbar'),hb=document.querySelector('.hero-bg');
function tog(o){{document.body.classList.toggle('oc-open',o);bu.setAttribute('aria-expanded',o)}}
bu.onclick=function(){{tog(!document.body.classList.contains('oc-open'))}};sh.onclick=function(){{tog(false)}};document.getElementById('oc-x').onclick=function(){{tog(false)}};
addEventListener('keydown',function(e){{if(e.key==='Escape')tog(false)}});
var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
function onS(){{var y=scrollY,m=document.documentElement.scrollHeight-innerHeight;h.classList.toggle('solid',y>60);sb.style.width=(m>0?y/m*100:0)+'%';if(hb&&!rm&&y<innerHeight*1.2)hb.style.transform='translate3d(0,'+(y*.28)+'px,0)'}}
addEventListener('scroll',onS,{{passive:true}});onS();
if('IntersectionObserver'in window){{var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{rootMargin:'0px 0px -8% 0px'}});document.querySelectorAll('.rv,.band,.mosaic .tile').forEach(function(el){{io.observe(el)}})}}else document.querySelectorAll('.rv,.band,.tile').forEach(function(el){{el.classList.add('in')}});
document.querySelectorAll('.finder').forEach(function(f){{var s=f.querySelector('select'),a=f.querySelector('a');s.onchange=function(){{a.href=a.dataset.base+(s.value?'#'+s.value:'')}}}});
document.querySelectorAll('[data-car]').forEach(function(c){{var tr=c.querySelector('.car-tr');c.querySelector('.car-n').onclick=function(){{tr.scrollBy({{left:tr.clientWidth*.8,behavior:'smooth'}})}};c.querySelector('.car-p').onclick=function(){{tr.scrollBy({{left:-tr.clientWidth*.8,behavior:'smooth'}})}}}});
document.querySelectorAll('form.sub').forEach(function(f){{f.addEventListener('submit',function(e){{if(f.action.indexOf('BEEHIIV')>-1||f.action.indexOf('FORM_')>-1){{e.preventDefault();f.querySelector('button').textContent='✓'}}}})}});
}})();</script>
</body></html>"""

# ---------- theme components ----------
CREDIT = {'en': 'AI-generated illustration', 'es': 'Ilustración generada con IA'}

def hero(lang, img=None, title=None, sub=None, eyebrow=None, pos='center', finder=False, cats=None, color='#16110f', size='full', credit=True, home=False):
    L = lambda en, es: en if lang == 'en' else es
    bg = f'<div class="hero-bgw"><img class="hero-bg" src="{esc(img)}" alt="" style="object-position:{esc(pos)}"></div>' if img else f'<div class="hero-bgw"><div class="hero-bg topo-bg" style="--c:{color}"></div></div>'
    if home:
        lock = f'<h1 class="lockup"><span class="lk-1">MIAGAZINE</span><span class="lk-2">{L("through the lens","a través del lente")}</span><span class="lk-3">Miami</span></h1>'
    else:
        lock = f'<div class="lockup page">{f"<span class=lk-e>{esc(eyebrow)}</span>" if eyebrow else ""}<h1 class="lk-t">{esc(title)}</h1>{f"<p class=lk-s>{esc(sub)}</p>" if sub else ""}</div>'
    fd = ''
    if finder:
        opts = ''.join(f'<option value="{cat_slug(c)}">{esc(cat_label(lang, c))}</option>' for c in (cats or CATS))
        fd = f'<div class="finder"><label for="fd-{lang}">{L("I am looking for","Busco")}</label><select id="fd-{lang}"><option value="">{L("Everything","Todo")}</option>{opts}</select><a class="btn" data-base="{T[lang]["journal_url"]}" href="{T[lang]["journal_url"]}">{L("Show me","Ver")}</a></div>'
    cr = f'<small class="hero-cr">{CREDIT[lang]}</small>' if (img and credit) else ''
    return f'<section class="hero-full {size}">{bg}<div class="hero-shade"></div>{lock}{fd}{cr}</section>'

def band(text, color=None):
    st = f' style="--band:{color}"' if color else ''
    return f'<div class="band"{st}><h2>{esc(text)}</h2></div>'

def tile(href, label, img=None, color='#0b5d68', sub=None, cls='', pos='center'):
    im = f'<img src="{esc(img)}" alt="" loading="lazy" style="object-position:{esc(pos)}">' if img else ''
    sb = f'<small>{esc(sub)}</small>' if sub else ''
    return f'<a class="tile {cls}{"" if img else " noimg"}" href="{href}" style="--c:{color}">{im}<span class="tl">{sb}{esc(label)}</span></a>'

def fill(color):
    return f'<div class="tile fill" style="--c:{color}" aria-hidden="true"></div>'

def mosaic(tiles, cols=5, cls=''):
    return f'<div class="mosaic c{cols} {cls}">{"".join(tiles)}</div>'

def carousel(tiles, lang):
    L = lambda en, es: en if lang == 'en' else es
    return f'<div class="car" data-car><button class="car-p" type="button" aria-label="{L("Previous","Anterior")}">‹</button><div class="car-tr">{"".join(tiles)}</div><button class="car-n" type="button" aria-label="{L("Next","Siguiente")}">›</button></div>'

def newsletter(lang):
    t = T[lang]; L = lambda en, es: en if lang == 'en' else es
    return f"""<section class="topo"><div class="topo-in rv"><h2>{L('Stay connected','Mantente conectado')}</h2><p>{L('Subscribe to The Lens and get what is happening in Miami every Thursday.','Suscríbete a The Lens y recibe lo que pasa en Miami cada jueves.')}</p>
<form class="sub nl" action="BEEHIIV_FORM_ACTION" method="post"><input type="email" name="email" placeholder="{L('Enter your email address','Escribe tu email')}" required aria-label="Email">
<fieldset><legend>{L("I'm interested in:","Me interesa:")}</legend><label><input type="checkbox" name="i_reader"> {L('Reading Miami','Leer sobre Miami')}</label><label><input type="checkbox" name="i_brand"> {L('Partnering as a brand','Anunciar mi marca')}</label><label><input type="checkbox" name="i_creator"> {L('Creating with MIAGAZINE','Crear con MIAGAZINE')}</label></fieldset>
<button class="btn" type="submit">{t['sub_btn']}</button></form><p class="small">{t['sub_note']}</p></div></section>"""

def post_tile(lang, p, cls=''):
    img = p.get('cover_image', '').replace('.webp', '-sm.webp') if p.get('cover_image') else None
    return tile(f"{T[lang]['journal_url']}{p['slug']}.html", p['title'], img, CATS[p['category']][0], cat_label(lang, p['category']), cls + ' post', p.get('cover_position', 'center')).replace('<a class="tile', '<a data-c="' + cat_slug(p['category']) + '" class="tile', 1)

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
        t = T[lang]; other = 'es' if lang == 'en' else 'en'; L = lambda en, es: en if lang == 'en' else es
        other_slugs = {p['slug'] for p in posts[other]}
        lst = posts[lang]
        # index
        cats = []
        for p in lst:
            if p['category'] not in cats: cats.append(p['category'])
        chips = f'<button class="filter on" data-f="all">{t["all"]}</button>' + ''.join(
            f'<button class="filter" data-f="{cat_slug(c)}" style="--c:{CATS[c][0]}">{esc(cat_label(lang,c))}</button>' for c in cats)
        tiles_ = [post_tile(lang, x, 'big' if i == 0 else '') for i, x in enumerate(lst)]
        rem = (5 - ((len(lst) + 3) % 5)) % 5
        tiles_ += [fill(c) for c in ['#e0602a', '#0b5d68', '#5c1230', '#c8283f', '#16110f'][:rem]]
        idx_path = t['journal_url']; idx_alt = T[other]['journal_url']
        itemlist = {"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"url":BASE+t['journal_url']+p['slug']+'.html',"name":p['title']} for i,p in enumerate(lst)]}
        script = "<script>(function(){function run(f){document.querySelectorAll('.filter').forEach(function(x){x.classList.toggle('on',x.dataset.f===f)});document.querySelectorAll('.mosaic.journal .tile').forEach(function(c){var m=c.dataset.c;c.hidden=!(f==='all'||m===f)})}document.querySelectorAll('.filter').forEach(function(b){b.onclick=function(){run(b.dataset.f)}});var h=location.hash.slice(1);if(h)run(h)})();</script>"
        body = (hero(lang, '/assets/img/miami-skyline-architecture-2026-cover.webp', t['journal_title'], t['journal_sub'], 'MIAGAZINE', 'center 38%', finder=True, cats=cats)
          + band(L('Miami stories, researched and sourced','Historias de Miami, investigadas y con fuentes'))
          + '<div class="filters-bar"><div class="filters" role="group">' + chips + '</div></div>'
          + mosaic(tiles_, cls='journal') + newsletter(lang) + script)
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
            rel_tiles = [post_tile(lang, x) for x in rel[:8]]
            faq_sec = ('<section class="faq"><h2>' + t['faq'] + '</h2>' + faq_html + '</section>') if faq else ''
            brief = ('<p class="small cover-brief"><strong>' + t['cover'] + ':</strong> ' + esc(p['cover_hint']) + '</p>') if p.get('cover_hint') else ''
            body = (hero(lang, p.get('cover_image'), p['title'], p.get('excerpt',''), cat_label(lang,p['category']) + ' · ' + str(mins) + ' ' + t['read'], p.get('cover_position','center'), color=color)
              + band(cat_label(lang,p['category']) + ' · ' + t['updated'] + ' ' + dstr, color)
              + f"""<article class="post cream" style="--c:{color}">
<div class="post-layout wrap"><aside class="toc"><div class="eyebrow">{t['toc']}</div><ol>{toc_html}</ol>
<div class="share"><div class="eyebrow">{t['share']}</div><button class="btn ghost" id="copy" type="button">{t['copy']}</button></div><a class="back" href="{t['journal_url']}">← {t['back']}</a></aside>
<div class="post-main"><p class="small byline">{t['by']}</p><div class="tldr rv"><div class="eyebrow">{t['in30']}</div><ul>{tldr}</ul></div>
<div class="article-body">{body_html}</div>{faq_sec}
<section class="sources"><h2>{t['sources']}</h2><ol>{src_html}</ol></section>{brief}
</div></div></article>"""
              + band(t['related'], '#0b5d68') + carousel(rel_tiles, lang) + newsletter(lang)
              + "<script>document.getElementById('copy').onclick=async e=>{try{await navigator.clipboard.writeText(location.href);e.target.textContent='" + t['copied'] + "'}catch(_){}};</script>")
            if p.get('cover_image'): extra += f'<meta property="og:image" content="{BASE}{esc(p["cover_image"])}">'
            page(lang, path, alt, f"{p['title']} | MIAGAZINE", p.get('excerpt', ''), body, extra, 'article')
    return posts

# ---------------- STATIC PAGES -----------------
def build_pages(posts):
    for lang in ('en', 'es'):
        t = T[lang]; o = 'es' if lang == 'en' else 'en'
        L = lambda en, es: en if lang == 'en' else es
        J = t['journal_url']; IMG = '/assets/img/'
        catimg = {'Art & Culture':('miami-art-week-2026-free-guide-cover','center 60%'),'Fashion & Models':('miami-modeling-swim-week-guide-cover','center 40%'),'Real Estate':('miami-luxury-real-estate-2026-cover','center 60%'),
                  'Food & Drink':('michelin-guide-miami-2026-cover','center 62%'),'Tech':('miami-tech-ai-scene-2026-cover','center 70%'),'Waterfront':('miami-2035-speculative-future-cover','center 70%'),
                  'Design & Architecture':('miami-skyline-architecture-2026-cover','center 40%'),'Photography':('best-photo-spots-miami-cover','center 70%')}
        order = ['Art & Culture','Fashion & Models','Real Estate','Design & Architecture','Food & Drink','Waterfront','Music','Economy','Tech','Trends','Photography','Sports & Lifestyle']
        ctiles = []
        for i, c in enumerate(order):
            im = catimg.get(c)
            ctiles.append(tile(f'{J}#{cat_slug(c)}', cat_label(lang, c), IMG + im[0] + '-sm.webp' if im else None, CATS[c][0], None, 'big' if i == 0 else '', im[1] if im else 'center'))
        ltiles = [post_tile(lang, x) for x in posts[lang][:5]]
        ev = [('Miami Art Week', L('Nov 30 – Dec 6','30 nov – 6 dic'), J + 'miami-art-week-2026-free-guide.html', 'miami-art-week-2026-free-guide-cover', '#c2410c'),
              ('Miami Book Fair', L('Nov 15–22','15–22 nov'), J, None, '#0b5d68'),
              (L("New Year's Eve on Ocean Drive",'Nochevieja en Ocean Drive'), L('Dec 31','31 dic'), J, None, '#5c1230'),
              (L('Art Deco Weekend · 50 years','Art Deco Weekend · 50 años'), L('Jan 15–17','15–17 ene'), J + 'miami-skyline-architecture-2026.html', 'edition-02-art-deco-at-50-cover', '#57534e'),
              ('Miami International Boat Show', L('Feb 10–14','10–14 feb'), J + 'miami-yachting-boat-show-2027.html', 'best-photo-spots-miami-cover', '#0e7490')]
        etiles = [tile(u, n, IMG + im + '-sm.webp' if im else None, c, d) for n, d, u, im, c in ev]
        home = (hero(lang, IMG+'edition-02-art-deco-at-50-cover.webp', pos='center 55%', finder=True, home=True)
          + band(L('Explore Miami through the lens','Explora Miami a través del lente')) + mosaic(ctiles)
          + band(L('Latest from the Journal','Lo último del Journal'), '#0b5d68') + mosaic(ltiles, cls='row')
          + '<div class="more rv"><a class="btn" href="' + J + '">' + L('Read the Journal','Leer el Journal') + '</a></div>'
          + band(L("What's on in Miami",'Qué pasa en Miami'), '#5c1230') + mosaic(etiles, cls='row')
          + '<section class="split2">'
          + '<a class="sp" href="' + P(lang,'/advertise.html') + '"><img src="' + IMG + 'social-agenda-story-sm.webp" alt="" loading="lazy"><div class="sp-box"><small>' + L('For brands','Para marcas') + '</small><strong>' + L('Be seen beautifully','Hazte ver con belleza') + '</strong><span>' + L('Stories, Reels, event bundles from $950','Historias, Reels y paquetes por evento desde $950') + '</span></div></a>'
          + '<a class="sp alt" href="' + P(lang,'/submit.html') + '"><img src="' + IMG + 'social-open-call-story-sm.webp" alt="" loading="lazy"><div class="sp-box"><small>' + L('For photographers','Para fotógrafos') + '</small><strong>' + L('Get published','Publica tu trabajo') + '</strong><span>' + L('Free to submit · full credit · 20% on partnerships','Envío gratis · crédito completo · 20% por alianzas') + '</span></div></a>'
          + '<a class="sp alt2" href="' + P(lang,'/careers.html') + '"><img src="' + IMG + 'careers-hero-sm.webp" alt="" loading="lazy"><div class="sp-box"><small>' + L('Careers','Vacantes') + '</small><strong>' + L('Join the collective','Únete al colectivo') + '</strong><span>' + L('Interviews by appointment only','Entrevistas solo con previa cita') + '</span></div></a>'
          + '</section>' + newsletter(lang))
        page(lang, P(lang, '/'), P(o, '/'), f"MIAGAZINE — {t['tagline']}", L("Miami's visual luxury magazine: fashion, design, real estate, music, food and waterfront living, photographed by Miami photographers. Free weekly newsletter.", "La revista visual de lujo de Miami: moda, diseño, real estate, música, gastronomía y vida en el agua, fotografiada por fotógrafos de Miami. Newsletter semanal gratis."), home)

        stories = (hero(lang, '/assets/img/stories-open-call-hero.webp', L('The edition','La edición'), L('Photographic editorials from our photographer network. First stories land during Miami Art Week.','Editoriales fotográficos de nuestra red de fotógrafos. Las primeras historias llegan en Miami Art Week.'), t['stories'], 'center 55%')
          + band(L('Editorials through the lens','Editoriales a través del lente'))
          + mosaic([tile('/stories/golden-hour-key-biscayne.html', 'Golden Hour, Key Biscayne', '/assets/img/best-photo-spots-miami-cover-sm.webp', '#0e7490', L('Story template','Plantilla'), 'big', 'center 70%'),
                    tile(P(lang,'/submit.html'), L('Your story here','Tu historia aquí'), None, '#e0602a', 'Open call'),
                    tile(P(lang,'/submit.html'), 'Art Week Through the Lens', None, '#c2410c', L('Open call · Dec','Convocatoria · dic')),
                    tile(P(lang,'/submit.html'), 'Art Deco at 50', None, '#57534e', L('Open call · Jan','Convocatoria · ene')),
                    tile(P(lang,'/submit.html'), 'Waterfront', None, '#0b5d68', L('Open call · Feb','Convocatoria · feb')),
                    fill('#5c1230'), fill('#c8283f'), fill('#e0602a'), fill('#0b5d68'), fill('#16110f'), fill('#c2410c'), fill('#57534e')])
          + newsletter(lang))
        page(lang, P(lang, '/stories/'), P(o, '/stories/'), f"{t['stories']} — MIAGAZINE", L('Photographic editorials from Miami.','Editoriales fotográficos de Miami.'), stories)

        li = lambda items: ''.join(f'<li>{x}</li>' for x in items)
        submit = (hero(lang, '/assets/img/social-open-call-story.webp', L('Art Week Through the Lens','Art Week a través del lente'), L('Free to submit. Full credit. A link to your portfolio. 20% of every partnership you bring.','Gratis. Crédito completo. Link a tu portafolio. 20% de cada alianza que traigas.'), L('Open call · Nov–Dec 2026','Convocatoria · nov–dic 2026'), 'center 55%')
          + band(L('Submit your editorial','Envía tu editorial'))
          + '<div class="cream-sec"><div class="ctas rv" style="justify-content:center;margin:0"><a class="btn big" href="TALLY_FORM_URL">' + L('Submit an editorial','Enviar editorial') + '</a></div></div>') + f'''<section class="cream-sec"><div class="wrap split"><div><h2>{L('What you get','Qué recibes')}</h2><ul class="list">{li(L(['Publication on miagazine.com, in The Lens newsletter and on our social channels','Full credits for your team and a photographer profile linked to your portfolio','A share kit and a “Published in MIAGAZINE” badge','20% commission on any brand or venue you refer that becomes a partner','Priority for paid assignments and invitations to our events'],['Publicación en miagazine.com, en el newsletter The Lens y en nuestras redes','Créditos completos para tu equipo y perfil de fotógrafo con link a tu portafolio','Kit para compartir y badge “Published in MIAGAZINE”','20% de comisión por cada marca o venue que refieras y se vuelva socio','Prioridad en encargos pagados e invitaciones a nuestros eventos']))}</ul></div>
<div><h2>{L('Guidelines','Requisitos')}</h2><ul class="list">{li(L(['8–20 images, minimum 3000px long side, sRGB JPG, no watermarks','Unpublished in other magazines (your own social is fine)','Shot in Miami or South Florida, or with a clear Miami connection','Title, 80–150 words of story, and complete credits','Model and location releases where applicable','Real photography only — no generative AI imagery'],['8–20 imágenes, mínimo 3000 px lado largo, JPG sRGB, sin marca de agua','Inéditas en otras revistas (tus redes sí cuentan)','Hechas en Miami o South Florida, o con conexión clara con Miami','Título, 80–150 palabras de historia y créditos completos','Releases de modelo y locación cuando aplique','Solo fotografía real, sin imágenes de IA generativa']))}</ul></div></div></section>
<section class="cream-sec"><div class="wrap prose"><h2>{L('Rights','Derechos')}</h2><p>{L('You keep your copyright. By submitting, you grant MIAGAZINE a non-exclusive license to publish your images with credit on our website, newsletter, social channels, quarterly issues and promotion. Any commercial use by a third-party brand requires your separate agreement and payment.','Conservas tu copyright. Al enviar, das a MIAGAZINE una licencia no exclusiva para publicar tus imágenes con crédito en web, newsletter, redes, ediciones trimestrales y promoción. Cualquier uso comercial de una marca requiere tu acuerdo aparte y pago.')}</p><p>{L('We reply to every submission within 48 hours.','Respondemos cada envío en 48 horas.')}</p></div></section>''' + newsletter(lang)
        page(lang, P(lang, '/submit.html'), P(o, '/submit.html'), L('Submit Your Work — Open Call for Miami Photographers | MIAGAZINE','Publica tu trabajo — Convocatoria para fotógrafos de Miami | MIAGAZINE'), L('Open call for Miami photographers: free to submit, full credit, 20% partner commission.','Convocatoria para fotógrafos de Miami: envío gratis, crédito completo, 20% de comisión.'), submit)

        K = KIT.C[lang]
        keys = ['STRIPE_NEWSLETTER','STRIPE_HOMEPAGE','STRIPE_SELECTS','STRIPE_STORY','STRIPE_REEL','STRIPE_EVENT','STRIPE_FILM','STRIPE_ISSUE']
        tr = ''.join(f'<tr><td><strong>{a}</strong><br><span class="small">{d}</span></td><td class="price">{b}</td><td class="small">{c}</td><td><a class="btn ghost" href="{k}">{L("Book","Reservar")}</a></td></tr>' for (a,b,c,d),k in zip(K['rows'], keys))
        bkeys = ['STRIPE_BUNDLE_ARTWEEK','STRIPE_BUNDLE_ARTDECO','STRIPE_BUNDLE_BOATSHOW']
        bundles_html = ''.join(f'<article class="bundle"><img src="/assets/img/{img}-sm.webp" alt="" loading="lazy"><div class="bi"><div class="eyebrow">{dt}</div><h3>{n}</h3><div class="bp">{pr}</div><ul>{"".join(f"<li>{x}</li>" for x in inc)}</ul><p class="small">{K["b_val"]}: <s>{val}</s> · {K["b_book"]} {bk}</p><a class="btn" href="{k}">{L("Book","Reservar")}</a></div></article>' for (n,pr,dt,inc,val,bk,img),k in zip(K['bundles'], bkeys))
        founding_html = f'<div class="founding"><div><div class="eyebrow" style="color:#e8cfa6">{K["p6_eye"]}</div><h2>{K["p6_h"]}</h2><p>{K["p6_sub"]}</p><ul>{"".join(f"<li>{x}</li>" for x in K["fp"])}</ul><p class="small">{K["fp_val"]}</p></div><div class="ctas" style="flex-direction:column;align-items:stretch"><a class="btn light" href="STRIPE_FOUNDING">{L("Pay $1,500 / year","Pagar $1,500 / año")}</a><a class="btn light" href="STRIPE_FOUNDING_QUARTERLY">{L("4 × $400 quarterly","4 × $400 trimestral")}</a><a class="btn light" href="CALENDLY_URL">{L("Book a 15-min call","Agendar llamada de 15 min")}</a></div></div>'
        adv = hero(lang, '/assets/img/social-agenda-story.webp', L('Be seen beautifully.','Hazte ver con belleza.'), L('MIAGAZINE puts Miami brands in front of an affluent, bilingual, design-minded audience — through photography, not banners.','MIAGAZINE pone a las marcas de Miami frente a una audiencia bilingüe, de alto poder adquisitivo y amante del diseño, con fotografía, no con banners.'), L('Partners · Founding rates','Socios · Tarifas fundadoras'), 'center 60%') + band(L('Formats & rates','Formatos y tarifas')) + f'''<section class="cream-sec"><div class="wrap"><div class="answer" style="margin-bottom:32px"><strong>{L('How much does it cost to advertise in MIAGAZINE?','¿Cuánto cuesta anunciarse en MIAGAZINE?')}</strong> {L('Founding rates start at $150 per newsletter sponsorship, $99/month for a guide listing, $450 for a Branded Reel and $650 for a photographed brand story. Event bundles start at $950. Ten Founding Partner spots are available at $1,500 per year or 4 quarterly payments of $400.','Las tarifas fundadoras empiezan en $150 por patrocinio de newsletter, $99/mes por ficha en la guía, $450 por Reel de marca y $650 por historia de marca fotografiada. Los paquetes por evento empiezan en $950. Hay 10 cupos de Socio Fundador a $1,500 al año o 4 pagos trimestrales de $400.')}</div>
<div class="ctas" style="justify-content:flex-start;margin:0 0 28px"><a class="btn" href="{P(lang,'/media-kit.html')}">{L('View the media kit','Ver el media kit')}</a><a class="btn ghost" href="/media-kit/MIAGAZINE-Media-Kit-2026-{'EN' if lang=='en' else 'ES'}.pdf">{L('Download PDF','Descargar PDF')}</a><a class="btn ghost" href="CALENDLY_URL">{L('Book a call','Agendar llamada')}</a></div>
<div class="table-wrap"><table><thead><tr><th>{L('Package','Paquete')}</th><th>{L('Rate','Tarifa')}</th><th>{L('Term','Plazo')}</th><th></th></tr></thead><tbody>{tr}</tbody></table></div></div></section>
{band(K['b_eye'] + ' · ' + K['b_h'], '#5c1230')}<section class="cream-sec"><div class="wrap"><p class="small" style="margin:0 0 28px">{K['b_sub']}</p><div class="bundles">{bundles_html}</div></div></section>
<section class="dark teal"><div class="wrap">{founding_html}
<p class="small" style="margin-top:18px">{L('All paid content is labeled “Partner”. Questions: partners@miagazine.com','Todo contenido pagado se etiqueta “Partner”. Preguntas: partners@miagazine.com')}</p></div></section>''' + band(L('Find out more','Cuéntanos de tu marca'), '#0b5d68') + f'''<section class="wine"><form class="wform sub rv" action="FORM_ENQUIRY_ACTION" method="post">
<label>{L('First name','Nombre')}<input name="first_name" required></label><label>{L('Last name','Apellido')}<input name="last_name"></label>
<label>{L('Email address','Email')}<input type="email" name="email" required></label><label>{L('Brand / company','Marca / empresa')}<input name="company"></label><label>{L('Phone (optional)','Teléfono (opcional)')}<input name="phone"></label>
<fieldset><legend>{L("I'm interested in:","Me interesa:")}</legend><label><input type="checkbox" name="int_founding"> {L('Founding Partner','Socio Fundador')}</label><label><input type="checkbox" name="int_bundle"> {L('Event bundles','Paquetes por evento')}</label><label><input type="checkbox" name="int_story"> {L('Branded Story / Reel','Historia / Reel de marca')}</label><label><input type="checkbox" name="int_newsletter"> Newsletter</label></fieldset>
<label>{L('Additional information (optional)','Información adicional (opcional)')}<textarea name="message" rows="5"></textarea></label>
<button class="btn" type="submit">{L('Send enquiry','Enviar consulta')}</button></form></section>''' + newsletter(lang)
        page(lang, P(lang, '/advertise.html'), P(o, '/advertise.html'), L('Advertise in a Miami Luxury Magazine — Founding Rates | MIAGAZINE','Anúnciate en una revista de lujo de Miami — Tarifas fundadoras | MIAGAZINE'), L('Newsletter sponsorships from $150, Branded Reels, photographed brand stories, event coverage, event bundles and Founding Partner packages.','Patrocinios de newsletter desde $150, Reels de marca, historias fotografiadas, cobertura de eventos, paquetes por evento y Socio Fundador.'), adv)

        page(lang, P(lang, '/404.html'), P(o, '/404.html'), '404 — MIAGAZINE', 'Not found', hero(lang, '/assets/img/miami-2035-speculative-future-cover.webp', L('Out of frame.','Fuera de cuadro.'), L('This page does not exist.','Esta página no existe.'), '404', 'center 60%') + band(L('Back to MIAGAZINE','Volver a MIAGAZINE')) + '<div class="more"><a class="btn" href="' + t['home'] + '">MIAGAZINE</a></div>')

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
            himg = p.get('hero_image') or '/assets/img/legal-hero.webp'
            accent = '#57534e' if is_legal else '#e0602a'
            html_body = (hero(lang, himg, p['title'], p.get('summary',''), eyebrow, p.get('hero_position','center 55%'), size='tall' if is_legal else 'full')
              + band((t['updated'] + ': ' + dstr) if is_legal else (eyebrow + ' · MIAGAZINE'), '#57534e' if is_legal else None)
              + '<article class="post cream" style="--c:' + accent + '">' + (('<div class="wrap page-cta">' + cta + '</div>') if cta else '')
              + '<div class="' + cls + '">' + aside + '<div class="post-main page-body">' + body + '</div></div></article>' + newsletter(lang))
            ld = {"@context":"https://schema.org","@type":"AboutPage" if slug=='about' else "WebPage","name":p['title'],"inLanguage":lang,"dateModified":str(p.get('updated',TODAY)),"url":BASE+path,"isPartOf":{"@type":"WebSite","name":"MIAGAZINE","url":BASE}}
            extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
            if slug == 'careers':
                extra += f'<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"ItemList","name":p["title"],"itemListElement":[{"@type":"ListItem","position":i+1,"name":r} for i,r in enumerate(L(["Event & editorial photographer","Videographer / filmmaker","Bilingual reporter – writer","Content creator & social media","Partnerships executive","Publicist / PR","Model & talent casting","Internships"],["Fotógrafo/a de eventos y editorial","Videógrafo/a / filmmaker","Reportero/a – redactor/a bilingüe","Creador/a de contenido y social media","Ejecutivo/a de alianzas comerciales","Publicista / relaciones públicas","Casting de modelos y talento","Pasantías"]))]}, ensure_ascii=False)}</script>'
            page(lang, path, alt, f"{p['title']} | MIAGAZINE", p.get('summary', ''), html_body, extra)
        # legal hub
        cards = ''.join(f'<a class="legal-card" href="{P(lang, page_path(x))}"><h3>{esc(pages[lang][x]["title"])}</h3><p>{esc(pages[lang][x].get("summary",""))}</p><span>→</span></a>' for x in LEGAL_ORDER if x in pages[lang])
        hub = hero(lang, '/assets/img/legal-hero.webp', L('Legal center','Centro legal'), L('How we protect creators, readers and partners: intellectual property, permissions, privacy, cookies, terms and editorial standards.','Cómo protegemos a creadores, lectores y marcas: propiedad intelectual, permisos, privacidad, cookies, términos y estándares editoriales.'), 'Legal', 'center 55%', size='tall') + band(L('Law, permissions & privacy','Derecho, permisos y privacidad'), '#57534e') + f"""<section class="cream-sec"><div class="wrap legal-grid">{cards}<a class="legal-card" href="#" data-cookie-prefs><h3>{COOKIE_TXT[lang]['prefs']}</h3><p>{L('Change your cookie choices at any time.','Cambia tu elección de cookies cuando quieras.')}</p><span>→</span></a></div>
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
        body = hero(lang, '/assets/img/edition-02-art-deco-at-50-cover.webp', K['kit'] + ' ' + K['season'], K['tag'] + ' ' + K['founding'], 'MIAGAZINE', 'center 55%') + band(K['p2_eye']) + f'''<div class="cream-sec"><div class="ctas rv" style="justify-content:center;margin:0"><a class="btn big" href="CALENDLY_URL">{L('Book a 15-min call','Agendar llamada de 15 min')}</a><a class="btn big ghost" href="{pdf}">{L('Download PDF','Descargar PDF')}</a></div></div>
<section class="cream-sec"><div class="wrap split"><div><div class="eyebrow">{K['p2_eye']}</div><h2>{K['p2_h']}</h2><p>{K['p2_p']}</p></div><div class="mk-pill">{pill}</div></div></section>
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
            h = re.sub(r'<header class="(?:top|hdr)".*?</aside>|<header class="top">.*?</header>', nav('en', '/es/blog/'), h, count=1, flags=re.S)
            open(full, 'w').write(h)

if __name__ == '__main__':
    posts = load_posts(); refresh_legacy()
    build_blog(posts); build_pages(posts); build_content_pages(); build_media_kit_page(); build_meta(posts); apply_integrations()
    print('posts en/es:', len(posts['en']), len(posts['es']))
