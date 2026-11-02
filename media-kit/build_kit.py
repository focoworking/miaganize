#!/usr/bin/env python3
"""MIAGAZINE media kit -> HTML -> PDF (Letter landscape). Usage: python3 media-kit/build_kit.py"""
import os, subprocess, json
D = os.path.dirname(os.path.abspath(__file__))

C = {
'en': dict(
 file='MIAGAZINE-Media-Kit-2026-EN',
 kit='Media Kit', season='2026 – 2027', tag='Miami, through the lens.', founding='Founding rates · 10 partner spots',
 web='miagazine.com', contact='partners@miagazine.com',
 p2_eye='Who we are', p2_h='A select collective that shows Miami at its most brilliant.',
 p2_p='MIAGAZINE is a bilingual digital luxury magazine born in Miami in 2026. We are publicists, reporters, photographers, filmmakers and content creators united to cover the city’s luxury, events, nightlife and public life — with real photography, verified information and impeccable taste.',
 pillars=[('Visual first','Every story starts with photography by our Miami photographer network.'),('Bilingual','English and Spanish, for Miami’s local, U.S. and Latin American audience.'),('Always there','In person at Art Week, Art Deco Weekend, Boat Show, Swim Week and the nights in between.'),('Search-ready','Built for Google, AI Overviews, ChatGPT and Perplexity: structured, sourced, cited.')],
 covers=['Art & Culture','Fashion & Models','Real Estate','Nightlife & Music','Food & Drink','Waterfront','Design','Economy & Tech'],
 dm_t='What is a digital magazine?', dm=[('Always on','Weekly publishing and real-time event coverage — not one issue a month.'),('Everywhere','Web, newsletter, social, video and downloadable editions, free on any screen.'),('Measurable','Every placement comes with clear reach, click and engagement data.')],
 p3_eye='Why Miami', p3_h='The city everyone is watching.',
 stats=[('$260.8B','Miami-Dade GDP, 2024','U.S. Bureau of Economic Analysis (via FRED)'),('28M+','visitors to Greater Miami & the Beaches, 2024','Greater Miami Convention & Visitors Bureau'),('8.56M','cruise passengers at PortMiami, FY2025','PortMiami'),('14','Michelin-starred restaurants in Greater Miami, 2026','Michelin Guide Florida 2026'),('272','galleries at Art Basel Miami Beach 2026','Art Basel'),('$4.4B','spent by international buyers on Miami real estate','MIAMI REALTORS')],
 p3_note='Figures as reported by each source; see miagazine.com/blog for full citations.',
 p4_eye='Audience & channels', p4_h='Who sees you.',
 aud=['Residents of Brickell, Miami Beach, Coral Gables, Design District and Key Biscayne','Visitors during Art Week, Boat Show, F1 and Swim Week','Bilingual and Latin American high-net-worth readers','Creative, hospitality, fashion and real estate professionals'],
 ch=[('miagazine.com','Journal, stories, city guide (EN/ES)'),('The Lens','Weekly newsletter, every Thursday'),('Instagram & TikTok','Carousels, Reels and live event coverage'),('Pinterest & LinkedIn','Evergreen traffic and B2B reach'),('Photographer network','Every story is shared by its photographers, models and venues'),('Events','On-site presence with QR capture at Miami’s key events')],
 goals_t='Launch goals · first 90 days', goals=[('1,500','newsletter subscribers'),('3,000','Instagram followers'),('300','people photographed and tagged'),('25','published stories')],
 goals_note='We are a launching publication: these are targets, not current audited figures. Partners receive real performance reports for every placement.',
 p5_eye='Formats & rates', p5_h='Be seen beautifully.',
 rows=[('Newsletter Sponsor','$150','per issue','Logo, 60 words and one link in The Lens, our Thursday newsletter.'),('Homepage Feature','$250','per week','Featured block on the miagazine.com homepage, EN + ES.'),('MIA Selects','$99','per month','Curated listing in our Miami guide with photos, map and structured data.'),('Branded Story','$650','one-time','Professional shoot by our photographer network + Partner story on web, newsletter and social.'),('Event Coverage','$900','one-time','Photographer at your event, edited gallery, recap story and social posts.'),('Issue Sponsor','$500','per edition','Back cover of our quarterly digital / print-on-demand edition.')],
 th=['Format','Rate','Term','What you get'],
 p6_eye='Founding Partner', p6_h='$1,500 / year', p6_sub='Only 10 spots. Rate locked for 12 months.',
 fp=['12 newsletter sponsorships (one per month)','1 Branded Story, professionally photographed','12 months of MIA Selects listing','Logo on our Partners page (EN + ES)','Priority invitations to MIAGAZINE events','Quarterly performance report'],
 fp_val='Equivalent value at standard rates: $3,638',
 how_t='How a Branded Story works', how=[('Brief','15-minute call: your goal, audience and dates.'),('Shoot','We assign a photographer from our network; you approve the concept.'),('Publish','Story goes live on web, newsletter and social, labeled “Partner”.'),('Report','Reach, clicks and engagement within 14 days.')],
 p7_eye='Editorial & events calendar', p7_h='Where your brand can appear.',
 cal=[('Dec 2026','Art Week Through the Lens','Miami Art Week, Nov 30 – Dec 6 · Art Basel Dec 4–6','Galleries, hotels, fashion, collectibles'),('Jan 2027','Art Deco at 50','Art Deco Weekend, Jan 15–17 · Beaux Arts Festival','Hospitality, vintage, autos, design'),('Feb 2027','Waterfront','Miami International Boat Show, Feb 10–14 · SOBEWFF Feb 25–28','Yachting, real estate, dining, spirits'),('Mar 2027','After Dark','Miami Music Week Mar 22–28 · Ultra Mar 26–28','Nightlife, beverages, fashion, tech'),('Apr 2027','Design & Interiors','Design District season','Furniture, architecture, real estate'),('May 2027','Speed & Style','F1 Miami Grand Prix · Miami Swim Week','Automotive, watches, swimwear, hospitality')],
 cal_th=['Edition','Theme','Anchor events','Ideal for'],
 cal_note='Event dates from official organizers or listings as of November 2026; subject to change.',
 p8_eye='Specs, terms & visibility', p8_h='The details.',
 specs_t='Creative specs', specs=['Logo: SVG or PNG, transparent, min. 1000 px wide','Newsletter copy: up to 60 words + 1 URL (UTM welcome)','Images we receive: JPG/WebP, min. 3000 px long side, with usage rights','Branded Story: we produce all photography; you approve facts, not editorial voice'],
 terms_t='Booking terms', terms=['Payment by secure link (Stripe) to confirm the date','Materials due 7 days before publication','Full refund if cancelled 7+ days before publication','All paid content is labeled “Partner” (FTC Endorsement Guides)','Founding rates valid for contracts signed before Feb 28, 2027'],
 vis_t='Visibility beyond social', vis=['SEO: every Partner story is indexed with structured data (schema.org)','AEO: answers formatted for Google AI Overviews and featured snippets','GEO / LLM: sourced, dated content built to be cited by ChatGPT, Perplexity and Gemini','Bilingual pages double your search footprint (EN + ES)'],
 cta='Let’s create something beautiful.', cta_sub='Book a 15-minute call or reserve a Founding Partner spot.',
 legal='MIAGAZINE · Miami, FL · Rates in USD, valid November 2026 – February 2027. Photographs © their respective authors.'),
'es': dict(
 file='MIAGAZINE-Media-Kit-2026-ES',
 kit='Media Kit', season='2026 – 2027', tag='Miami, a través del lente.', founding='Tarifas fundadoras · 10 cupos de socio',
 web='miagazine.com/es', contact='partners@miagazine.com',
 p2_eye='Quiénes somos', p2_h='Un colectivo selecto que muestra Miami en su esplendor.',
 p2_p='MIAGAZINE es una revista digital de lujo bilingüe nacida en Miami en 2026. Somos publicistas, reporteros, fotógrafos, filmmakers y creadores de contenido unidos para cubrir el lujo, los eventos, la noche y la vida pública de la ciudad, con fotografía real, información verificada y un gusto impecable.',
 pillars=[('Primero lo visual','Cada historia nace de la fotografía de nuestra red de fotógrafos de Miami.'),('Bilingüe','Español e inglés, para la audiencia local, estadounidense y latinoamericana.'),('Siempre presentes','En persona en Art Week, Art Deco Weekend, Boat Show, Swim Week y las noches entre medio.'),('Lista para buscadores','Hecha para Google, AI Overviews, ChatGPT y Perplexity: estructurada, con fuentes, citable.')],
 covers=['Arte y Cultura','Moda y Modelos','Real Estate','Noche y Música','Gastronomía','Vida en el agua','Diseño','Economía y Tech'],
 dm_t='¿Qué es una revista digital?', dm=[('Siempre activa','Publica cada semana y cubre eventos en tiempo real, no una vez al mes.'),('En todas partes','Web, newsletter, redes, video y ediciones descargables, gratis en cualquier pantalla.'),('Medible','Cada publicación incluye datos claros de alcance, clics e interacción.')],
 p3_eye='Por qué Miami', p3_h='La ciudad que todos están mirando.',
 stats=[('$260.8B','PIB de Miami-Dade, 2024','U.S. Bureau of Economic Analysis (vía FRED)'),('28M+','visitantes a Greater Miami & the Beaches, 2024','Greater Miami Convention & Visitors Bureau'),('8.56M','pasajeros de crucero en PortMiami, año fiscal 2025','PortMiami'),('14','restaurantes con estrella Michelin en Greater Miami, 2026','Guía Michelin Florida 2026'),('272','galerías en Art Basel Miami Beach 2026','Art Basel'),('$4.4B','invertidos por compradores internacionales en real estate de Miami','MIAMI REALTORS')],
 p3_note='Cifras según cada fuente; citas completas en miagazine.com/es/blog.',
 p4_eye='Audiencia y canales', p4_h='Quién te ve.',
 aud=['Residentes de Brickell, Miami Beach, Coral Gables, Design District y Key Biscayne','Visitantes en Art Week, Boat Show, F1 y Swim Week','Lectores bilingües y latinoamericanos de alto poder adquisitivo','Profesionales creativos, de hospitalidad, moda y real estate'],
 ch=[('miagazine.com','Journal, historias y guía de la ciudad (ES/EN)'),('The Lens','Newsletter semanal, cada jueves'),('Instagram y TikTok','Carruseles, Reels y cobertura de eventos en vivo'),('Pinterest y LinkedIn','Tráfico permanente y alcance B2B'),('Red de fotógrafos','Cada historia la comparten sus fotógrafos, modelos y venues'),('Eventos','Presencia en sitio con captura por QR en los eventos clave de Miami')],
 goals_t='Metas de lanzamiento · primeros 90 días', goals=[('1,500','suscriptores al newsletter'),('3,000','seguidores en Instagram'),('300','personas fotografiadas y etiquetadas'),('25','historias publicadas')],
 goals_note='Somos una publicación en lanzamiento: son metas, no cifras auditadas actuales. Cada socio recibe un reporte real de resultados por cada publicación.',
 p5_eye='Formatos y tarifas', p5_h='Hazte ver con belleza.',
 rows=[('Patrocinio Newsletter','$150','por envío','Logo, 60 palabras y un link en The Lens, nuestro newsletter de los jueves.'),('Destacado en Home','$250','por semana','Bloque destacado en la portada de miagazine.com, ES + EN.'),('MIA Selects','$99','al mes','Ficha curada en nuestra guía de Miami con fotos, mapa y datos estructurados.'),('Historia de marca','$650','único','Shoot profesional de nuestra red + historia Partner en web, newsletter y redes.'),('Cobertura de evento','$900','único','Fotógrafo en tu evento, galería editada, historia recap y posts en redes.'),('Patrocinio de edición','$500','por edición','Contraportada de la edición trimestral digital / impresa bajo demanda.')],
 th=['Formato','Tarifa','Plazo','Qué incluye'],
 p6_eye='Socio Fundador', p6_h='$1,500 / año', p6_sub='Solo 10 cupos. Tarifa congelada por 12 meses.',
 fp=['12 patrocinios de newsletter (uno al mes)','1 historia de marca fotografiada profesionalmente','12 meses de ficha en MIA Selects','Logo en nuestra página de Partners (ES + EN)','Invitaciones prioritarias a eventos MIAGAZINE','Reporte trimestral de resultados'],
 fp_val='Valor equivalente a tarifa estándar: $3,638',
 how_t='Cómo funciona una historia de marca', how=[('Brief','Llamada de 15 minutos: objetivo, audiencia y fechas.'),('Shoot','Asignamos un fotógrafo de la red; tú apruebas el concepto.'),('Publicación','La historia sale en web, newsletter y redes, etiquetada “Partner”.'),('Reporte','Alcance, clics e interacción en 14 días.')],
 p7_eye='Calendario editorial y de eventos', p7_h='Dónde puede aparecer tu marca.',
 cal=[('Dic 2026','Art Week a través del lente','Miami Art Week, 30 nov – 6 dic · Art Basel 4–6 dic','Galerías, hoteles, moda, coleccionables'),('Ene 2027','Art Deco at 50','Art Deco Weekend, 15–17 ene · Beaux Arts Festival','Hospitalidad, vintage, autos, diseño'),('Feb 2027','Waterfront','Miami International Boat Show, 10–14 feb · SOBEWFF 25–28 feb','Náutica, real estate, gastronomía, licores'),('Mar 2027','After Dark','Miami Music Week 22–28 mar · Ultra 26–28 mar','Vida nocturna, bebidas, moda, tech'),('Abr 2027','Diseño e Interiores','Temporada del Design District','Mobiliario, arquitectura, real estate'),('May 2027','Speed & Style','F1 Miami Grand Prix · Miami Swim Week','Automotriz, relojes, swimwear, hospitalidad')],
 cal_th=['Edición','Tema','Eventos ancla','Ideal para'],
 cal_note='Fechas según organizadores oficiales o listados a noviembre de 2026; sujetas a cambios.',
 p8_eye='Especificaciones, términos y visibilidad', p8_h='Los detalles.',
 specs_t='Especificaciones creativas', specs=['Logo: SVG o PNG transparente, mín. 1000 px de ancho','Texto newsletter: hasta 60 palabras + 1 URL (UTM bienvenido)','Imágenes que recibimos: JPG/WebP, mín. 3000 px lado largo, con derechos de uso','Historia de marca: producimos toda la fotografía; tú apruebas datos, no la voz editorial'],
 terms_t='Términos de reserva', terms=['Pago por link seguro (Stripe) para confirmar la fecha','Materiales 7 días antes de la publicación','Reembolso completo si cancelas 7+ días antes','Todo contenido pagado se etiqueta “Partner” (guías de la FTC)','Tarifas fundadoras válidas para contratos firmados antes del 28 feb 2027'],
 vis_t='Visibilidad más allá de redes', vis=['SEO: cada historia Partner se indexa con datos estructurados (schema.org)','AEO: respuestas preparadas para Google AI Overviews y fragmentos destacados','GEO / LLM: contenido con fuentes y fechas, hecho para ser citado por ChatGPT, Perplexity y Gemini','Páginas bilingües duplican tu presencia en buscadores (ES + EN)'],
 cta='Creemos algo hermoso.', cta_sub='Agenda una llamada de 15 minutos o reserva tu cupo de Socio Fundador.',
 legal='MIAGAZINE · Miami, FL · Tarifas en USD, válidas de noviembre 2026 a febrero 2027. Fotografías © de sus respectivos autores.'),
}

CSS = r'''
@page{size:11in 8.5in;margin:0}
:root{--ink:#0e0e0e;--paper:#f6f3ee;--muted:#6b665f;--line:#d9d3c9;--gold:#b08d57;--white:#fff}
*{box-sizing:border-box;margin:0;padding:0}
body{font:11pt/1.5 "Inter",sans-serif;color:var(--ink);background:var(--paper);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.serif,h1,h2,h3{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;letter-spacing:-.01em;line-height:1.05}
.page{width:11in;height:8.5in;position:relative;overflow:hidden;page-break-after:always;padding:.65in .75in}
.page:last-child{page-break-after:auto}
.eye{font-size:8pt;letter-spacing:.26em;text-transform:uppercase;color:var(--gold);font-weight:500}
h2{font-size:40pt;margin:.12in 0 .28in;max-width:8.5in}
.foot{position:absolute;left:.75in;right:.75in;bottom:.4in;display:flex;justify-content:space-between;font-size:7.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);border-top:1px solid var(--line);padding-top:.1in}
.logo{font-family:"Cormorant Garamond",serif;font-weight:600;letter-spacing:.32em}
/* cover */
.cover{background:var(--ink);color:var(--paper);padding:0}
.cover .art{position:absolute;inset:0;background:radial-gradient(70% 90% at 82% 18%,rgba(232,197,140,.55),transparent 60%),radial-gradient(60% 70% at 15% 105%,rgba(14,116,144,.55),transparent 70%),linear-gradient(160deg,#0e0e0e 0%,#1d2a2e 45%,#7a5a36 100%)}
.cover .art::after{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.04) 0 1px,transparent 1px 28px)}
.cover .in{position:absolute;inset:.7in .8in;display:flex;flex-direction:column;justify-content:space-between}
.cover .mast{font-size:64pt;letter-spacing:.3em;font-family:"Cormorant Garamond",serif;font-weight:600}
.cover .big{font-family:"Cormorant Garamond",serif;font-style:italic;font-size:110pt;line-height:.9;color:rgba(255,255,255,.92)}
.cover .row{display:flex;justify-content:space-between;align-items:flex-end;gap:.4in}
.cover .tag{font-family:"Cormorant Garamond",serif;font-size:26pt;font-style:italic}
.cover .meta{text-align:right;font-size:9pt;letter-spacing:.2em;text-transform:uppercase;line-height:2}
.cover .pill{display:inline-block;border:1px solid var(--gold);color:#e8cfa6;padding:.06in .16in;margin-top:.1in}
/* p2 */
.lead{font-size:13pt;line-height:1.6;max-width:6.4in;color:#2b2925}
.two{display:grid;grid-template-columns:1.15fr 1fr;gap:.55in}
.pillars{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line)}
.pillars div{background:var(--white);padding:.2in .22in}
.pillars h3{font-size:17pt;margin-bottom:.05in;color:var(--gold)}
.pillars p{font-size:9pt;color:var(--muted)}
.tags{display:flex;flex-wrap:wrap;gap:.08in;margin-top:.3in}
.tags span{border:1px solid var(--ink);padding:.05in .14in;font-size:8pt;letter-spacing:.14em;text-transform:uppercase}
/* stats */
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:.28in .4in;margin-top:.1in}
.stat{border-top:1px solid var(--ink);padding-top:.12in}
.stat .n{font-family:"Cormorant Garamond",serif;font-size:50pt;line-height:1;color:var(--ink)}
.stat .l{font-size:10pt;margin-top:.06in}
.stat .s{font-size:7pt;letter-spacing:.08em;color:var(--muted);text-transform:uppercase;margin-top:.05in}
.note{font-size:7.5pt;color:var(--muted);margin-top:.25in}
/* audience */
.list li{list-style:none;padding:.09in 0;border-bottom:1px solid var(--line);font-size:10pt}
.chan{display:grid;grid-template-columns:1fr 1fr;gap:.12in .3in}
.chan div{border-left:2px solid var(--gold);padding-left:.12in}
.chan b{display:block;font-size:10pt}.chan span{font-size:8.5pt;color:var(--muted)}
.goals{display:grid;grid-template-columns:repeat(4,1fr);gap:.2in;background:var(--ink);color:var(--paper);padding:.22in .3in;margin-top:.3in}
.goals .gt{grid-column:1/-1;font-size:7.5pt;letter-spacing:.24em;text-transform:uppercase;color:#e8cfa6}
.goals .n{font-family:"Cormorant Garamond",serif;font-size:34pt;line-height:1}
.goals .l{font-size:8.5pt;color:#c9c2b6}
.goals .gn{grid-column:1/-1;font-size:7.5pt;color:#a8a197;font-style:italic}
/* rates */
table{width:100%;border-collapse:collapse}
th{text-align:left;font-size:7.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);font-weight:500;padding:.08in .1in;border-bottom:1px solid var(--ink)}
td{padding:.13in .1in;border-bottom:1px solid var(--line);vertical-align:top;font-size:9.5pt}
td.f{font-weight:600;width:2.1in}
td.p{font-family:"Cormorant Garamond",serif;font-size:24pt;line-height:1;width:1.1in;white-space:nowrap}
td.t{color:var(--muted);width:1.1in;font-size:8.5pt}
/* founding */
.fp{display:grid;grid-template-columns:1fr 1.15fr;gap:.5in;height:6.3in}
.fp .card{background:var(--ink);color:var(--paper);padding:.45in .45in;display:flex;flex-direction:column}
.fp .card .eye{color:#e8cfa6}
.fp .card h2{font-size:58pt;margin:.1in 0 .05in;color:var(--paper)}
.fp .card .sub{font-family:"Cormorant Garamond",serif;font-style:italic;font-size:17pt;color:#e8cfa6;margin-bottom:.25in}
.fp .card li{list-style:none;padding:.07in 0;border-bottom:1px solid #2c2a27;font-size:10pt}
.fp .card li::before{content:"— ";color:var(--gold)}
.fp .card .val{margin-top:auto;font-size:8.5pt;letter-spacing:.12em;text-transform:uppercase;color:#a8a197}
.steps{display:grid;gap:.18in;margin-top:.2in}
.step{display:grid;grid-template-columns:.55in 1fr;gap:.1in;align-items:start;border-top:1px solid var(--line);padding-top:.14in}
.step .k{font-family:"Cormorant Garamond",serif;font-size:30pt;line-height:.9;color:var(--gold)}
.step b{font-size:11pt;display:block}.step span{font-size:9.5pt;color:var(--muted)}
/* calendar */
td.m{font-family:"Cormorant Garamond",serif;font-size:17pt;width:1.1in;white-space:nowrap}
td.th{font-weight:600;width:2in}
/* details */
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:.4in}
.three h3{font-size:19pt;margin-bottom:.1in;padding-bottom:.08in;border-bottom:1px solid var(--ink)}
.three li{list-style:none;font-size:9pt;padding:.06in 0;border-bottom:1px solid var(--line)}
.cta{position:absolute;left:.75in;right:.75in;bottom:.85in;background:var(--ink);color:var(--paper);padding:.3in .4in;display:flex;justify-content:space-between;align-items:center}
.cta h3{font-size:28pt;font-style:italic}
.cta p{font-size:9pt;color:#c9c2b6;margin-top:.05in}
.cta .c{text-align:right;font-size:12pt;line-height:1.7}
.cta .c b{color:#e8cfa6;font-weight:500}
.dm{position:absolute;left:.75in;right:.75in;bottom:.85in;display:grid;grid-template-columns:1.3fr 1fr 1fr 1fr;gap:.3in;border-top:1px solid var(--ink);padding-top:.2in}
.dmt{font-family:"Cormorant Garamond",serif;font-style:italic;font-size:24pt;line-height:1.1}
.dm b{display:block;font-size:10.5pt;margin-bottom:.04in}.dm span{font-size:9pt;color:var(--muted)}
.stats{gap:.5in .45in !important;margin-top:.25in !important}.stat .n{font-size:64pt !important}.stat .l{font-size:11pt !important}
.fp .card h2{font-size:46pt !important;white-space:nowrap}
'''

def li(xs): return ''.join(f'<li>{x}</li>' for x in xs)

def kit(L):
    c = C[L]
    foot = lambda n: f'<div class="foot"><span class="logo">MIAGAZINE</span><span>{c["kit"]} {c["season"]}</span><span>{n:02d} / 08</span></div>'
    pages = []
    pages.append(f'''<section class="page cover"><div class="art"></div><div class="in">
<div class="row"><div class="mast">MIAGAZINE</div><div class="meta">{c['web']}<br>{c['contact']}</div></div>
<div><div class="big">{c['kit']}<br>{c['season']}</div></div>
<div class="row"><div class="tag">{c['tag']}</div><div class="meta"><span class="pill">{c['founding']}</span></div></div></div></section>''')
    pages.append(f'''<section class="page"><div class="eye">{c['p2_eye']}</div><h2>{c['p2_h']}</h2>
<div class="two"><div><p class="lead">{c['p2_p']}</p><div class="tags">{''.join(f'<span>{x}</span>' for x in c['covers'])}</div></div>
<div class="pillars">{''.join(f'<div><h3>{a}</h3><p>{b}</p></div>' for a,b in c['pillars'])}</div></div>
<div class="dm"><div class="dmt">{c['dm_t']}</div>{''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in c['dm'])}</div>{foot(2)}</section>''')
    pages.append(f'''<section class="page"><div class="eye">{c['p3_eye']}</div><h2>{c['p3_h']}</h2>
<div class="stats">{''.join(f'<div class="stat"><div class="n">{n}</div><div class="l">{l}</div><div class="s">{s}</div></div>' for n,l,s in c['stats'])}</div>
<p class="note">{c['p3_note']}</p>{foot(3)}</section>''')
    pages.append(f'''<section class="page"><div class="eye">{c['p4_eye']}</div><h2>{c['p4_h']}</h2>
<div class="two"><ul class="list">{li(c['aud'])}</ul><div class="chan">{''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in c['ch'])}</div></div>
<div class="goals"><div class="gt">{c['goals_t']}</div>{''.join(f'<div><div class="n">{n}</div><div class="l">{l}</div></div>' for n,l in c['goals'])}<div class="gn">{c['goals_note']}</div></div>{foot(4)}</section>''')
    pages.append(f'''<section class="page"><div class="eye">{c['p5_eye']}</div><h2>{c['p5_h']}</h2>
<table><thead><tr>{''.join(f'<th>{x}</th>' for x in c['th'])}</tr></thead><tbody>{''.join(f'<tr><td class="f">{a}</td><td class="p">{b}</td><td class="t">{t}</td><td>{d}</td></tr>' for a,b,t,d in c['rows'])}</tbody></table>{foot(5)}</section>''')
    pages.append(f'''<section class="page"><div class="fp"><div class="card"><div class="eye">{c['p6_eye']}</div><h2>{c['p6_h']}</h2><div class="sub">{c['p6_sub']}</div><ul>{li(c['fp'])}</ul><div class="val">{c['fp_val']}</div></div>
<div><div class="eye">{c['how_t']}</div><div class="steps">{''.join(f'<div class="step"><div class="k">{i+1:02d}</div><div><b>{a}</b><span>{b}</span></div></div>' for i,(a,b) in enumerate(c['how']))}</div></div></div>{foot(6)}</section>''')
    pages.append(f'''<section class="page"><div class="eye">{c['p7_eye']}</div><h2>{c['p7_h']}</h2>
<table><thead><tr>{''.join(f'<th>{x}</th>' for x in c['cal_th'])}</tr></thead><tbody>{''.join(f'<tr><td class="m">{m}</td><td class="th">{t}</td><td>{e}</td><td class="t" style="width:2.2in">{f}</td></tr>' for m,t,e,f in c['cal'])}</tbody></table>
<p class="note">{c['cal_note']}</p>{foot(7)}</section>''')
    pages.append(f'''<section class="page"><div class="eye">{c['p8_eye']}</div><h2>{c['p8_h']}</h2>
<div class="three"><div><h3>{c['specs_t']}</h3><ul>{li(c['specs'])}</ul></div><div><h3>{c['terms_t']}</h3><ul>{li(c['terms'])}</ul></div><div><h3>{c['vis_t']}</h3><ul>{li(c['vis'])}</ul></div></div>
<div class="cta"><div><h3>{c['cta']}</h3><p>{c['cta_sub']}</p></div><div class="c"><b>{c['contact']}</b><br>{c['web']}<br>@miagazine</div></div>
<div class="foot"><span>{c['legal']}</span><span>08 / 08</span></div></section>''')
    return f'''<!doctype html><html lang="{L}"><head><meta charset="utf-8"><title>MIAGAZINE {c['kit']} {c['season']}</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{''.join(pages)}</body></html>'''

for L in ('en', 'es'):
    open(os.path.join(D, C[L]['file'] + '.html'), 'w').write(kit(L))

js = r'''const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for (const f of %s){const p=await b.newPage();await p.goto('file://'+f+'.html',{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:f+'.pdf',width:'11in',height:'8.5in',printBackground:true,preferCSSPageSize:true});
console.log('ok',f)}
await b.close()})();''' % json.dumps([os.path.join(D, C[L]['file']) for L in ('en','es')])
open(os.path.join(D, '_pdf.js'), 'w').write(js)
subprocess.run(['node', os.path.join(D, '_pdf.js')], check=True)
