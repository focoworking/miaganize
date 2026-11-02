#!/usr/bin/env python3
"""Genera docs/10-EMAILS-MEDIA-KIT.md y outreach/emails-media-kit.csv (para mail merge)."""
import csv, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIG = {'en': "{{sender_name}}\nPartnerships · MIAGAZINE\nmiagazine.com · @miagazine\n[MAILING ADDRESS], Miami, FL\n\nNot interested? Reply \"no thanks\" and we won't email you again.",
       'es': "{{sender_name}}\nAlianzas · MIAGAZINE\nmiagazine.com/es · @miagazine\n[DIRECCIÓN POSTAL], Miami, FL\n\n¿No te interesa? Responde \"no, gracias\" y no te volveremos a escribir."}

# (segment, step, day, lang, subject A, subject B, body)
E = []
def add(seg, step, day, en, es):
    E.append((seg, step, day, 'en', *en)); E.append((seg, step, day, 'es', *es))

# ---------- SECUENCIA BASE (cualquier marca) ----------
add('General', '1 · Media kit', 0,
 ("{{company}} in MIAGAZINE's Art Week edition?", "Founding Partner spot for {{company}}",
  "Hi {{first_name}},\n\n{{detail}} — that's exactly the Miami we want to show.\n\nWe're launching MIAGAZINE, a bilingual visual luxury magazine made by Miami photographers, during Miami Art Week (Dec 4–6). We're opening 10 Founding Partner spots: a full year of presence — weekly newsletter, a professionally photographed story about {{company}} and a listing in our Miami guide — for $1,500.\n\nMedia kit attached (8 pages). Formats start at $150.\n\nWould a 15-minute call this week make sense?"),
 ("¿{{company}} en la edición de Art Week de MIAGAZINE?", "Un cupo de Socio Fundador para {{company}}",
  "Hola {{first_name}}:\n\n{{detail}}: justo el Miami que queremos mostrar.\n\nEstamos lanzando MIAGAZINE, una revista visual de lujo bilingüe hecha por fotógrafos de Miami, durante Miami Art Week (4–6 dic). Abrimos 10 cupos de Socio Fundador: un año completo de presencia (newsletter semanal, una historia fotografiada profesionalmente sobre {{company}} y una ficha en nuestra guía de Miami) por $1,500.\n\nTe adjunto el media kit (8 páginas). Los formatos empiezan en $150.\n\n¿Te sirve una llamada de 15 minutos esta semana?"))
add('General', '2 · Seguimiento', 3,
 ("Re: {{company}} in MIAGAZINE", "Quick question, {{first_name}}",
  "Hi {{first_name}},\n\nQuick follow-up on the media kit. One idea for {{company}}: a Branded Story ($650) — our photographer shoots {{company}}, we publish it on web, newsletter and social in English and Spanish, and you get a performance report in 14 days.\n\nWant me to send two concept options?"),
 ("Re: {{company}} en MIAGAZINE", "Una pregunta rápida, {{first_name}}",
  "Hola {{first_name}}:\n\nSigo con lo del media kit. Una idea para {{company}}: una Historia de marca ($650). Nuestro fotógrafo hace el shoot, la publicamos en web, newsletter y redes en español e inglés, y recibes un reporte de resultados en 14 días.\n\n¿Te mando dos propuestas de concepto?"))
add('General', '3 · Urgencia', 7,
 ("{{spots_left}} Founding spots left", "Holding a spot for {{company}}?",
  "Hi {{first_name}},\n\n{{spots_left}} of our 10 Founding Partner spots are still open, and the Art Week edition closes on Nov 25. Happy to hold one for {{company}} until Friday — no payment needed to hold it.\n\nShould I?"),
 ("Quedan {{spots_left}} cupos de Socio Fundador", "¿Reservo un cupo para {{company}}?",
  "Hola {{first_name}}:\n\nQuedan {{spots_left}} de los 10 cupos de Socio Fundador y la edición de Art Week cierra el 25 de noviembre. Con gusto te guardo uno para {{company}} hasta el viernes, sin pago para reservarlo.\n\n¿Lo aparto?"))
add('General', '4 · Cierre', 14,
 ("Should I close your file?", "Last note from MIAGAZINE",
  "Hi {{first_name}},\n\nI haven't heard back, so I'll assume the timing isn't right. I'll close the file for now.\n\nIf it helps later, our next editions are Art Deco at 50 (January) and Waterfront (February, Boat Show). Just reply \"later\" and I'll check in then."),
 ("¿Cierro tu ficha?", "Última nota de MIAGAZINE",
  "Hola {{first_name}}:\n\nNo he tenido respuesta, así que asumo que no es el momento. Cierro la ficha por ahora.\n\nPor si te sirve más adelante, nuestras próximas ediciones son Art Deco at 50 (enero) y Waterfront (febrero, Boat Show). Responde \"más adelante\" y te escribo entonces."))

# ---------- PRIMER EMAIL POR SEGMENTO ----------
add('Hoteles y hospitalidad', '1 · Media kit', 0,
 ("Your terrace, through our lens", "{{company}} × Miami Art Week",
  "Hi {{first_name}},\n\nArt Week brings the world to Miami Beach for one week — and most of it is looking for where to stay, eat and be seen.\n\nMIAGAZINE is a new bilingual visual luxury magazine made by Miami photographers. We'd love to feature {{company}} in our Art Week edition: an editorial shoot on property, a story in English and Spanish, our Thursday newsletter and social coverage.\n\nMedia kit attached. Founding Partner: $1,500/year (10 spots). Event Coverage: $900.\n\nOpen to a 15-minute call?"),
 ("Tu terraza, a través de nuestro lente", "{{company}} × Miami Art Week",
  "Hola {{first_name}}:\n\nArt Week trae al mundo a Miami Beach por una semana, y casi todos buscan dónde dormir, comer y dejarse ver.\n\nMIAGAZINE es una nueva revista visual de lujo bilingüe hecha por fotógrafos de Miami. Nos encantaría incluir a {{company}} en nuestra edición de Art Week: un shoot editorial en la propiedad, una historia en español e inglés, el newsletter de los jueves y cobertura en redes.\n\nTe adjunto el media kit. Socio Fundador: $1,500/año (10 cupos). Cobertura de evento: $900.\n\n¿Hablamos 15 minutos?"))
add('Restaurantes y bares', '1 · Media kit', 0,
 ("One dish, one photograph", "{{company}} in MIAGAZINE",
  "Hi {{first_name}},\n\nWe just published our guide to Michelin in Miami, and {{company}} is the kind of table our readers ask about.\n\nMIAGAZINE is a new bilingual visual luxury magazine. For restaurants we offer a listing in our curated Miami guide (MIA Selects, $99/month) and photographed Branded Stories ($650) — one beautiful image of your best dish can travel further than a month of ads.\n\nMedia kit attached. Can I send you a concept?"),
 ("Un plato, una fotografía", "{{company}} en MIAGAZINE",
  "Hola {{first_name}}:\n\nAcabamos de publicar nuestra guía Michelin de Miami, y {{company}} es justo el tipo de mesa por la que preguntan nuestros lectores.\n\nMIAGAZINE es una nueva revista visual de lujo bilingüe. Para restaurantes ofrecemos una ficha en nuestra guía curada de Miami (MIA Selects, $99/mes) e Historias de marca fotografiadas ($650): una imagen hermosa de tu mejor plato llega más lejos que un mes de anuncios.\n\nTe adjunto el media kit. ¿Te mando un concepto?"))
add('Real estate y desarrolladores', '1 · Media kit', 0,
 ("{{company}} for bilingual buyers", "Logos in the sky — and your project",
  "Hi {{first_name}},\n\nOur Journal just covered Miami's luxury market in 2026 — branded residences, foreign buyers (led by Colombia and Argentina) and what post-Surfside rules mean for owners.\n\nMIAGAZINE reaches bilingual, high-net-worth readers in English and Spanish, with stories built to rank on Google and to be cited by AI search. For {{company}} we'd suggest an architectural Branded Story ($650) plus newsletter placements, or a Founding Partner year ($1,500).\n\nMedia kit attached. Worth a short call?"),
 ("{{company}} para compradores bilingües", "Logos en el cielo, y tu proyecto",
  "Hola {{first_name}}:\n\nNuestro Journal acaba de publicar el panorama del lujo inmobiliario en Miami 2026: residencias de marca, compradores extranjeros (liderados por Colombia y Argentina) y lo que cambian las leyes post-Surfside.\n\nMIAGAZINE llega a lectores bilingües de alto poder adquisitivo en español e inglés, con historias hechas para posicionar en Google y ser citadas por buscadores de IA. Para {{company}} proponemos una Historia de marca arquitectónica ($650) más envíos de newsletter, o un año de Socio Fundador ($1,500).\n\nTe adjunto el media kit. ¿Vale una llamada corta?"))
add('Moda, swim y joyería', '1 · Media kit', 0,
 ("An editorial for {{company}}", "{{company}}, shot in Miami light",
  "Hi {{first_name}},\n\nMIAGAZINE is a new bilingual visual luxury magazine made by Miami's fashion photographers. Our next editions are Art Week (December) and Art Deco at 50 (January) — both natural stages for {{company}}.\n\nIdea: a Branded Story ($650) shot on location with our network — styled, credited and published on web, newsletter and Instagram, labeled Partner. We can also cover a launch or trunk show ($900).\n\nMedia kit attached. Shall I send a moodboard?"),
 ("Un editorial para {{company}}", "{{company}}, con luz de Miami",
  "Hola {{first_name}}:\n\nMIAGAZINE es una nueva revista visual de lujo bilingüe hecha por fotógrafos de moda de Miami. Nuestras próximas ediciones son Art Week (diciembre) y Art Deco at 50 (enero), escenarios naturales para {{company}}.\n\nIdea: una Historia de marca ($650) fotografiada en locación con nuestra red, con estilismo, créditos y publicada en web, newsletter e Instagram, etiquetada Partner. También podemos cubrir un lanzamiento o trunk show ($900).\n\nTe adjunto el media kit. ¿Te mando un moodboard?"))
add('Galerías y arte', '1 · Media kit', 0,
 ("{{company}} during Art Week", "Art Week coverage for {{company}}",
  "Hi {{first_name}},\n\nDuring Miami Art Week our photographers will be covering fairs, openings and public programs every day, in English and Spanish.\n\nWe'd like to include {{company}}: Event Coverage of your opening ($900 — photographer, edited gallery and recap story) or a newsletter feature in our Art Week issues ($150). Our free Art Week guide is already live on the Journal.\n\nMedia kit attached. Can we put your opening on our calendar?"),
 ("{{company}} durante Art Week", "Cobertura de Art Week para {{company}}",
  "Hola {{first_name}}:\n\nDurante Miami Art Week nuestros fotógrafos cubrirán ferias, inauguraciones y programas públicos cada día, en español e inglés.\n\nNos gustaría incluir a {{company}}: cobertura de tu inauguración ($900: fotógrafo, galería editada e historia recap) o un destacado en los newsletters de Art Week ($150). Nuestra guía gratuita de Art Week ya está publicada en el Journal.\n\nTe adjunto el media kit. ¿Ponemos tu inauguración en nuestro calendario?"))
add('Náutica, autos y relojes', '1 · Media kit', 0,
 ("Waterfront edition: Boat Show 2027", "{{company}} on the water",
  "Hi {{first_name}},\n\nOur February edition, Waterfront, is built around the Miami International Boat Show (Feb 10–14, 2027) and the bay itself.\n\nFor {{company}} we'd propose an aerial and on-deck Branded Story ($650) or a Founding Partner year ($1,500) that covers Waterfront and our May \"Speed & Style\" edition (F1 Miami). Bilingual, photographed, built to be found on Google and AI search.\n\nMedia kit attached. Interested in early placement?"),
 ("Edición Waterfront: Boat Show 2027", "{{company}} en el agua",
  "Hola {{first_name}}:\n\nNuestra edición de febrero, Waterfront, gira en torno al Miami International Boat Show (10–14 feb 2027) y la bahía.\n\nPara {{company}} proponemos una Historia de marca aérea y a bordo ($650) o un año de Socio Fundador ($1,500) que cubre Waterfront y nuestra edición de mayo \"Speed & Style\" (F1 Miami). Bilingüe, fotografiada y hecha para aparecer en Google y en buscadores de IA.\n\nTe adjunto el media kit. ¿Te interesa reservar temprano?"))
add('Wellness y med spa', '1 · Media kit', 0,
 ("Quiet luxury, photographed", "{{company}} in our 2027 trends story",
  "Hi {{first_name}},\n\nOur Journal piece on luxury trends for 2027 puts wellness and longevity at the center of what Miami wants next.\n\nMIAGAZINE can feature {{company}} with a calm, minimal Branded Story ($650) and a listing in our curated Miami guide ($99/month), in English and Spanish, clearly labeled Partner.\n\nMedia kit attached. Open to a short call?"),
 ("Lujo silencioso, fotografiado", "{{company}} en nuestras tendencias 2027",
  "Hola {{first_name}}:\n\nNuestro artículo sobre tendencias de lujo 2027 pone el bienestar y la longevidad en el centro de lo que Miami quiere.\n\nMIAGAZINE puede presentar a {{company}} con una Historia de marca serena y minimalista ($650) y una ficha en nuestra guía curada de Miami ($99/mes), en español e inglés, etiquetada Partner.\n\nTe adjunto el media kit. ¿Hablamos un momento?"))
add('Noche y eventos', '1 · Media kit', 0,
 ("{{company}} after dark", "Event coverage for {{company}}",
  "Hi {{first_name}},\n\nMIAGAZINE covers Miami's nights the way they deserve: photographed beautifully, published fast, in English and Spanish.\n\nFor your next event at {{company}} we offer Event Coverage ($900): photographer on site, edited gallery, recap story, newsletter and social. Our March edition, After Dark, is built around Miami Music Week.\n\nMedia kit attached. What's your next date?"),
 ("{{company}} de noche", "Cobertura de eventos para {{company}}",
  "Hola {{first_name}}:\n\nMIAGAZINE cubre las noches de Miami como se merecen: bien fotografiadas, publicadas rápido, en español e inglés.\n\nPara tu próximo evento en {{company}} ofrecemos Cobertura de evento ($900): fotógrafo en sitio, galería editada, historia recap, newsletter y redes. Nuestra edición de marzo, After Dark, gira en torno a Miami Music Week.\n\nTe adjunto el media kit. ¿Cuál es tu próxima fecha?"))

# ---------- CONTACTO CÁLIDO ----------
add('Cálido: nos conocimos en evento', '1 · Media kit', 1,
 ("Great meeting you at {{event}}", "From {{event}}: the MIAGAZINE media kit",
  "Hi {{first_name}},\n\nGreat meeting you at {{event}}. As promised, here's the MIAGAZINE media kit.\n\nThe short version: a bilingual visual luxury magazine made by Miami photographers; formats from $150; 10 Founding Partner spots at $1,500/year. I also have a few frames from {{event}} that would suit {{company}} — happy to share them.\n\nCoffee next week?"),
 ("Un gusto conocerte en {{event}}", "De {{event}}: el media kit de MIAGAZINE",
  "Hola {{first_name}}:\n\nUn gusto conocerte en {{event}}. Como te prometí, aquí va el media kit de MIAGAZINE.\n\nEn corto: una revista visual de lujo bilingüe hecha por fotógrafos de Miami; formatos desde $150; 10 cupos de Socio Fundador a $1,500/año. También tengo algunas fotos de {{event}} que le quedarían muy bien a {{company}}; con gusto te las comparto.\n\n¿Un café la próxima semana?"))
add('Cálido: venue fotografiado', '1 · Media kit', 0,
 ("{{company}} goes live in MIAGAZINE on {{date}}", "Your share kit + a quick idea",
  "Hi {{first_name}},\n\n{{photographer}} shot a story at {{company}} and it goes live in MIAGAZINE on {{date}}. We'll send you the share kit that morning — please tag @miagazine.\n\nIf you'd like to amplify it, our partner rate for a newsletter feature plus a homepage week is $350. Media kit attached for everything else."),
 ("{{company}} sale en MIAGAZINE el {{date}}", "Tu kit para compartir + una idea",
  "Hola {{first_name}}:\n\n{{photographer}} hizo una historia en {{company}} y se publica en MIAGAZINE el {{date}}. Esa mañana te enviamos el kit para compartir; por favor etiqueta a @miagazine.\n\nSi quieres amplificarla, nuestra tarifa de socio para destacado en newsletter más una semana en la home es de $350. Te adjunto el media kit para todo lo demás."))
add('Cálido: referido por fotógrafo', '1 · Media kit', 0,
 ("{{photographer}} suggested I write", "Via {{photographer}}: MIAGAZINE",
  "Hi {{first_name}},\n\n{{photographer}}, who's part of our photographer network, suggested {{company}} would be a natural fit for MIAGAZINE.\n\nWe're a new bilingual visual luxury magazine about Miami. {{photographer}} would love to shoot a story at {{company}} — as a Branded Story ($650) or within a Founding Partner year ($1,500).\n\nMedia kit attached. Can we set up a quick call with the three of us?"),
 ("{{photographer}} me sugirió escribirte", "De parte de {{photographer}}: MIAGAZINE",
  "Hola {{first_name}}:\n\n{{photographer}}, que forma parte de nuestra red de fotógrafos, nos sugirió que {{company}} encaja perfecto con MIAGAZINE.\n\nSomos una nueva revista visual de lujo bilingüe sobre Miami. A {{photographer}} le encantaría hacer una historia en {{company}}, como Historia de marca ($650) o dentro de un año de Socio Fundador ($1,500).\n\nTe adjunto el media kit. ¿Armamos una llamada rápida los tres?"))

# ---------- RESPUESTAS ----------
add('Respuestas', 'Si pide precio especial', None,
 ("Re: rates", "Re: rates",
  "Hi {{first_name}},\n\nThanks for the interest. Our founding rates are already our lowest, and we keep them the same for every partner. What I can do is add a bonus: an extra newsletter placement in the Art Week issue if you confirm by {{date}}."),
 ("Re: tarifas", "Re: tarifas",
  "Hola {{first_name}}:\n\nGracias por el interés. Las tarifas fundadoras ya son las más bajas y son iguales para todos los socios. Lo que sí puedo hacer es sumarte un envío extra de newsletter en la edición de Art Week si confirmas antes del {{date}}."))
add('Respuestas', 'Si pregunta por audiencia', None,
 ("Re: audience", "Re: audience",
  "Hi {{first_name}},\n\nFair question. We're a launching publication, so we don't sell inflated numbers: Founding Partners get our launch rate and a real report after every placement (reach, clicks, engagement). Our reach comes from the website, the newsletter, social and our photographer network, who share every story they appear in."),
 ("Re: audiencia", "Re: audiencia",
  "Hola {{first_name}}:\n\nBuena pregunta. Somos una publicación en lanzamiento, así que no vendemos números inflados: los Socios Fundadores pagan la tarifa de lanzamiento y reciben un reporte real después de cada publicación (alcance, clics, interacción). Nuestro alcance viene de la web, el newsletter, las redes y la red de fotógrafos, que comparten cada historia en la que aparecen."))
add('Respuestas', 'Si dice "sí"', None,
 ("Welcome, {{company}}", "Next steps",
  "Hi {{first_name}},\n\nWonderful — welcome to MIAGAZINE. Next steps:\n1. Payment link to confirm your date: {{stripe_link}}\n2. Logo (SVG/PNG) and 60-word copy, 7 days before publication\n3. A 15-minute brief for your Branded Story: {{calendar_link}}\n\nAll paid content is labeled \"Partner\"."),
 ("Bienvenida, {{company}}", "Próximos pasos",
  "Hola {{first_name}}:\n\nExcelente, bienvenidos a MIAGAZINE. Próximos pasos:\n1. Link de pago para confirmar la fecha: {{stripe_link}}\n2. Logo (SVG/PNG) y texto de 60 palabras, 7 días antes de la publicación\n3. Brief de 15 minutos para tu Historia de marca: {{calendar_link}}\n\nTodo contenido pagado se etiqueta \"Partner\"."))

# ---------- OUTPUT ----------
os.makedirs(os.path.join(R, 'outreach'), exist_ok=True)
with open(os.path.join(R, 'outreach/emails-media-kit.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['segment', 'step', 'send_day', 'lang', 'subject_a', 'subject_b', 'body'])
    for seg, step, day, lang, sa, sb, body in E:
        w.writerow([seg, step, '' if day is None else day, lang, sa, sb, body + '\n\n' + SIG[lang]])

md = ['# Emails para enviar el media kit a marcas', '',
'Plantillas listas para copiar o para mail merge (`outreach/emails-media-kit.csv`). Cada email existe en **EN** y **ES**. Adjuntar el PDF del idioma correspondiente: `media-kit/MIAGAZINE-Media-Kit-2026-EN.pdf` o `-ES.pdf`.', '',
'## Cómo usarlas', '',
'| Variable | Qué poner |', '|---|---|',
'| `{{first_name}}` | Nombre del contacto (marketing, PR o dueño) |', '| `{{company}}` | Marca, hotel, restaurante, galería |',
'| `{{detail}}` | **Obligatorio y real**: algo específico que viste (\"Your new rooftop menu\", \"La terraza nueva de su hotel\"). Sin esto, no se envía. |',
'| `{{spots_left}}` | Cupos de Socio Fundador que quedan (dato real, actualizar) |', '| `{{event}}` | Evento donde se conocieron |',
'| `{{photographer}}` | Fotógrafo de la red que hizo o hará la historia |', '| `{{date}}` | Fecha de publicación o límite |',
'| `{{stripe_link}}`, `{{calendar_link}}` | Link de pago y link de agenda |', '| `{{sender_name}}` | Quien firma (usar email de dominio: partners@miagazine.com) |', '',
'## Cadencia', '',
'| Día | Email | Nota |', '|---|---|---|',
'| 0 | Email 1 del **segmento** (o el General) + PDF adjunto | Martes a jueves, 9–11 am hora de Miami |',
'| 3 | Seguimiento (responder en el mismo hilo) | Sin adjunto |', '| 7 | Urgencia (cupos reales) | Solo si es verdad |', '| 14 | Cierre | Después, pausa 60 días |', '',
'Metas: 20 emails personalizados por día · tasa de respuesta objetivo 8–12% · 1 cierre por cada 25–30 envíos.', '',
'## Reglas (CAN-SPAM y buena reputación)', '',
'- Enviar solo desde dominio propio autenticado (SPF, DKIM, DMARC). Nunca desde Gmail personal.',
'- Asunto honesto, remitente real, dirección postal física y opción clara para darse de baja (ya está en la firma). Respetar bajas de inmediato.',
'- B2B 1 a 1, personalizado. Nada de listas compradas ni envíos masivos sin opt-in.',
'- No prometer cifras de audiencia que no existen. Los cupos y fechas del email de urgencia deben ser reales.',
'- Registrar cada envío y respuesta en el CRM (Notion: Advertisers).', '']
cur = None
for seg, step, day, lang, sa, sb, body in E:
    if seg != cur:
        md += ['---', '', f'## {seg}', '']; cur = seg
    tag = 'EN' if lang == 'en' else 'ES'
    dd = f' · día {day}' if day is not None else ''
    md += [f'### {step}{dd} · {tag}', '', f'**Asunto A:** {sa}  ', f'**Asunto B:** {sb}', '', '```', body, '', SIG[lang], '```', '']
open(os.path.join(R, 'docs/10-EMAILS-MEDIA-KIT.md'), 'w').write('\n'.join(md))
print(len(E), 'emails')
