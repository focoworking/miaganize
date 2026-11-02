# Emails para enviar el media kit a marcas

Plantillas listas para copiar o para mail merge (`outreach/emails-media-kit.csv`). Cada email existe en **EN** y **ES**. Adjuntar el PDF del idioma correspondiente: `media-kit/MIAGAZINE-Media-Kit-2026-EN.pdf` o `-ES.pdf`.

## Cómo usarlas

| Variable | Qué poner |
|---|---|
| `{{first_name}}` | Nombre del contacto (marketing, PR o dueño) |
| `{{company}}` | Marca, hotel, restaurante, galería |
| `{{detail}}` | **Obligatorio y real**: algo específico que viste ("Your new rooftop menu", "La terraza nueva de su hotel"). Sin esto, no se envía. |
| `{{spots_left}}` | Cupos de Socio Fundador que quedan (dato real, actualizar) |
| `{{event}}` | Evento donde se conocieron |
| `{{photographer}}` | Fotógrafo de la red que hizo o hará la historia |
| `{{date}}` | Fecha de publicación o límite |
| `{{stripe_link}}`, `{{calendar_link}}` | Link de pago y link de agenda |
| `{{sender_name}}` | Quien firma (usar email de dominio: partners@miagazine.com) |

## Cadencia

| Día | Email | Nota |
|---|---|---|
| 0 | Email 1 del **segmento** (o el General) + PDF adjunto | Martes a jueves, 9–11 am hora de Miami |
| 3 | Seguimiento (responder en el mismo hilo) | Sin adjunto |
| 7 | Urgencia (cupos reales) | Solo si es verdad |
| 14 | Cierre | Después, pausa 60 días |

Metas: 20 emails personalizados por día · tasa de respuesta objetivo 8–12% · 1 cierre por cada 25–30 envíos.

## Reglas (CAN-SPAM y buena reputación)

- Enviar solo desde dominio propio autenticado (SPF, DKIM, DMARC). Nunca desde Gmail personal.
- Asunto honesto, remitente real, dirección postal física y opción clara para darse de baja (ya está en la firma). Respetar bajas de inmediato.
- B2B 1 a 1, personalizado. Nada de listas compradas ni envíos masivos sin opt-in.
- No prometer cifras de audiencia que no existen. Los cupos y fechas del email de urgencia deben ser reales.
- Registrar cada envío y respuesta en el CRM (Notion: Advertisers).

---

## General

### 1 · Media kit · día 0 · EN

**Asunto A:** {{company}} in MIAGAZINE's Art Week edition?  
**Asunto B:** Founding Partner spot for {{company}}

```
Hi {{first_name}},

{{detail}} — that's exactly the Miami we want to show.

We're launching MIAGAZINE, a bilingual visual luxury magazine made by Miami photographers, during Miami Art Week (Dec 4–6). We're opening 10 Founding Partner spots: a full year of presence — weekly newsletter, a professionally photographed story about {{company}} and a listing in our Miami guide — for $1,500.

Media kit attached (8 pages). Formats start at $150.

Would a 15-minute call this week make sense?

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 1 · Media kit · día 0 · ES

**Asunto A:** ¿{{company}} en la edición de Art Week de MIAGAZINE?  
**Asunto B:** Un cupo de Socio Fundador para {{company}}

```
Hola {{first_name}}:

{{detail}}: justo el Miami que queremos mostrar.

Estamos lanzando MIAGAZINE, una revista visual de lujo bilingüe hecha por fotógrafos de Miami, durante Miami Art Week (4–6 dic). Abrimos 10 cupos de Socio Fundador: un año completo de presencia (newsletter semanal, una historia fotografiada profesionalmente sobre {{company}} y una ficha en nuestra guía de Miami) por $1,500.

Te adjunto el media kit (8 páginas). Los formatos empiezan en $150.

¿Te sirve una llamada de 15 minutos esta semana?

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

### 2 · Seguimiento · día 3 · EN

**Asunto A:** Re: {{company}} in MIAGAZINE  
**Asunto B:** Quick question, {{first_name}}

```
Hi {{first_name}},

Quick follow-up on the media kit. One idea for {{company}}: a Branded Story ($650) — our photographer shoots {{company}}, we publish it on web, newsletter and social in English and Spanish, and you get a performance report in 14 days.

Want me to send two concept options?

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 2 · Seguimiento · día 3 · ES

**Asunto A:** Re: {{company}} en MIAGAZINE  
**Asunto B:** Una pregunta rápida, {{first_name}}

```
Hola {{first_name}}:

Sigo con lo del media kit. Una idea para {{company}}: una Historia de marca ($650). Nuestro fotógrafo hace el shoot, la publicamos en web, newsletter y redes en español e inglés, y recibes un reporte de resultados en 14 días.

¿Te mando dos propuestas de concepto?

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

### 3 · Urgencia · día 7 · EN

**Asunto A:** {{spots_left}} Founding spots left  
**Asunto B:** Holding a spot for {{company}}?

```
Hi {{first_name}},

{{spots_left}} of our 10 Founding Partner spots are still open, and the Art Week edition closes on Nov 25. Happy to hold one for {{company}} until Friday — no payment needed to hold it.

Should I?

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 3 · Urgencia · día 7 · ES

**Asunto A:** Quedan {{spots_left}} cupos de Socio Fundador  
**Asunto B:** ¿Reservo un cupo para {{company}}?

```
Hola {{first_name}}:

Quedan {{spots_left}} de los 10 cupos de Socio Fundador y la edición de Art Week cierra el 25 de noviembre. Con gusto te guardo uno para {{company}} hasta el viernes, sin pago para reservarlo.

¿Lo aparto?

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

### 4 · Cierre · día 14 · EN

**Asunto A:** Should I close your file?  
**Asunto B:** Last note from MIAGAZINE

```
Hi {{first_name}},

I haven't heard back, so I'll assume the timing isn't right. I'll close the file for now.

If it helps later, our next editions are Art Deco at 50 (January) and Waterfront (February, Boat Show). Just reply "later" and I'll check in then.

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 4 · Cierre · día 14 · ES

**Asunto A:** ¿Cierro tu ficha?  
**Asunto B:** Última nota de MIAGAZINE

```
Hola {{first_name}}:

No he tenido respuesta, así que asumo que no es el momento. Cierro la ficha por ahora.

Por si te sirve más adelante, nuestras próximas ediciones son Art Deco at 50 (enero) y Waterfront (febrero, Boat Show). Responde "más adelante" y te escribo entonces.

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

---

## Hoteles y hospitalidad

### 1 · Media kit · día 0 · EN

**Asunto A:** Your terrace, through our lens  
**Asunto B:** {{company}} × Miami Art Week

```
Hi {{first_name}},

Art Week brings the world to Miami Beach for one week — and most of it is looking for where to stay, eat and be seen.

MIAGAZINE is a new bilingual visual luxury magazine made by Miami photographers. We'd love to feature {{company}} in our Art Week edition: an editorial shoot on property, a story in English and Spanish, our Thursday newsletter and social coverage.

Media kit attached. Founding Partner: $1,500/year (10 spots). Event Coverage: $900.

Open to a 15-minute call?

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 1 · Media kit · día 0 · ES

**Asunto A:** Tu terraza, a través de nuestro lente  
**Asunto B:** {{company}} × Miami Art Week

```
Hola {{first_name}}:

Art Week trae al mundo a Miami Beach por una semana, y casi todos buscan dónde dormir, comer y dejarse ver.

MIAGAZINE es una nueva revista visual de lujo bilingüe hecha por fotógrafos de Miami. Nos encantaría incluir a {{company}} en nuestra edición de Art Week: un shoot editorial en la propiedad, una historia en español e inglés, el newsletter de los jueves y cobertura en redes.

Te adjunto el media kit. Socio Fundador: $1,500/año (10 cupos). Cobertura de evento: $900.

¿Hablamos 15 minutos?

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

---

## Restaurantes y bares

### 1 · Media kit · día 0 · EN

**Asunto A:** One dish, one photograph  
**Asunto B:** {{company}} in MIAGAZINE

```
Hi {{first_name}},

We just published our guide to Michelin in Miami, and {{company}} is the kind of table our readers ask about.

MIAGAZINE is a new bilingual visual luxury magazine. For restaurants we offer a listing in our curated Miami guide (MIA Selects, $99/month) and photographed Branded Stories ($650) — one beautiful image of your best dish can travel further than a month of ads.

Media kit attached. Can I send you a concept?

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 1 · Media kit · día 0 · ES

**Asunto A:** Un plato, una fotografía  
**Asunto B:** {{company}} en MIAGAZINE

```
Hola {{first_name}}:

Acabamos de publicar nuestra guía Michelin de Miami, y {{company}} es justo el tipo de mesa por la que preguntan nuestros lectores.

MIAGAZINE es una nueva revista visual de lujo bilingüe. Para restaurantes ofrecemos una ficha en nuestra guía curada de Miami (MIA Selects, $99/mes) e Historias de marca fotografiadas ($650): una imagen hermosa de tu mejor plato llega más lejos que un mes de anuncios.

Te adjunto el media kit. ¿Te mando un concepto?

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

---

## Real estate y desarrolladores

### 1 · Media kit · día 0 · EN

**Asunto A:** {{company}} for bilingual buyers  
**Asunto B:** Logos in the sky — and your project

```
Hi {{first_name}},

Our Journal just covered Miami's luxury market in 2026 — branded residences, foreign buyers (led by Colombia and Argentina) and what post-Surfside rules mean for owners.

MIAGAZINE reaches bilingual, high-net-worth readers in English and Spanish, with stories built to rank on Google and to be cited by AI search. For {{company}} we'd suggest an architectural Branded Story ($650) plus newsletter placements, or a Founding Partner year ($1,500).

Media kit attached. Worth a short call?

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 1 · Media kit · día 0 · ES

**Asunto A:** {{company}} para compradores bilingües  
**Asunto B:** Logos en el cielo, y tu proyecto

```
Hola {{first_name}}:

Nuestro Journal acaba de publicar el panorama del lujo inmobiliario en Miami 2026: residencias de marca, compradores extranjeros (liderados por Colombia y Argentina) y lo que cambian las leyes post-Surfside.

MIAGAZINE llega a lectores bilingües de alto poder adquisitivo en español e inglés, con historias hechas para posicionar en Google y ser citadas por buscadores de IA. Para {{company}} proponemos una Historia de marca arquitectónica ($650) más envíos de newsletter, o un año de Socio Fundador ($1,500).

Te adjunto el media kit. ¿Vale una llamada corta?

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

---

## Moda, swim y joyería

### 1 · Media kit · día 0 · EN

**Asunto A:** An editorial for {{company}}  
**Asunto B:** {{company}}, shot in Miami light

```
Hi {{first_name}},

MIAGAZINE is a new bilingual visual luxury magazine made by Miami's fashion photographers. Our next editions are Art Week (December) and Art Deco at 50 (January) — both natural stages for {{company}}.

Idea: a Branded Story ($650) shot on location with our network — styled, credited and published on web, newsletter and Instagram, labeled Partner. We can also cover a launch or trunk show ($900).

Media kit attached. Shall I send a moodboard?

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 1 · Media kit · día 0 · ES

**Asunto A:** Un editorial para {{company}}  
**Asunto B:** {{company}}, con luz de Miami

```
Hola {{first_name}}:

MIAGAZINE es una nueva revista visual de lujo bilingüe hecha por fotógrafos de moda de Miami. Nuestras próximas ediciones son Art Week (diciembre) y Art Deco at 50 (enero), escenarios naturales para {{company}}.

Idea: una Historia de marca ($650) fotografiada en locación con nuestra red, con estilismo, créditos y publicada en web, newsletter e Instagram, etiquetada Partner. También podemos cubrir un lanzamiento o trunk show ($900).

Te adjunto el media kit. ¿Te mando un moodboard?

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

---

## Galerías y arte

### 1 · Media kit · día 0 · EN

**Asunto A:** {{company}} during Art Week  
**Asunto B:** Art Week coverage for {{company}}

```
Hi {{first_name}},

During Miami Art Week our photographers will be covering fairs, openings and public programs every day, in English and Spanish.

We'd like to include {{company}}: Event Coverage of your opening ($900 — photographer, edited gallery and recap story) or a newsletter feature in our Art Week issues ($150). Our free Art Week guide is already live on the Journal.

Media kit attached. Can we put your opening on our calendar?

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 1 · Media kit · día 0 · ES

**Asunto A:** {{company}} durante Art Week  
**Asunto B:** Cobertura de Art Week para {{company}}

```
Hola {{first_name}}:

Durante Miami Art Week nuestros fotógrafos cubrirán ferias, inauguraciones y programas públicos cada día, en español e inglés.

Nos gustaría incluir a {{company}}: cobertura de tu inauguración ($900: fotógrafo, galería editada e historia recap) o un destacado en los newsletters de Art Week ($150). Nuestra guía gratuita de Art Week ya está publicada en el Journal.

Te adjunto el media kit. ¿Ponemos tu inauguración en nuestro calendario?

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

---

## Náutica, autos y relojes

### 1 · Media kit · día 0 · EN

**Asunto A:** Waterfront edition: Boat Show 2027  
**Asunto B:** {{company}} on the water

```
Hi {{first_name}},

Our February edition, Waterfront, is built around the Miami International Boat Show (Feb 10–14, 2027) and the bay itself.

For {{company}} we'd propose an aerial and on-deck Branded Story ($650) or a Founding Partner year ($1,500) that covers Waterfront and our May "Speed & Style" edition (F1 Miami). Bilingual, photographed, built to be found on Google and AI search.

Media kit attached. Interested in early placement?

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 1 · Media kit · día 0 · ES

**Asunto A:** Edición Waterfront: Boat Show 2027  
**Asunto B:** {{company}} en el agua

```
Hola {{first_name}}:

Nuestra edición de febrero, Waterfront, gira en torno al Miami International Boat Show (10–14 feb 2027) y la bahía.

Para {{company}} proponemos una Historia de marca aérea y a bordo ($650) o un año de Socio Fundador ($1,500) que cubre Waterfront y nuestra edición de mayo "Speed & Style" (F1 Miami). Bilingüe, fotografiada y hecha para aparecer en Google y en buscadores de IA.

Te adjunto el media kit. ¿Te interesa reservar temprano?

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

---

## Wellness y med spa

### 1 · Media kit · día 0 · EN

**Asunto A:** Quiet luxury, photographed  
**Asunto B:** {{company}} in our 2027 trends story

```
Hi {{first_name}},

Our Journal piece on luxury trends for 2027 puts wellness and longevity at the center of what Miami wants next.

MIAGAZINE can feature {{company}} with a calm, minimal Branded Story ($650) and a listing in our curated Miami guide ($99/month), in English and Spanish, clearly labeled Partner.

Media kit attached. Open to a short call?

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 1 · Media kit · día 0 · ES

**Asunto A:** Lujo silencioso, fotografiado  
**Asunto B:** {{company}} en nuestras tendencias 2027

```
Hola {{first_name}}:

Nuestro artículo sobre tendencias de lujo 2027 pone el bienestar y la longevidad en el centro de lo que Miami quiere.

MIAGAZINE puede presentar a {{company}} con una Historia de marca serena y minimalista ($650) y una ficha en nuestra guía curada de Miami ($99/mes), en español e inglés, etiquetada Partner.

Te adjunto el media kit. ¿Hablamos un momento?

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

---

## Noche y eventos

### 1 · Media kit · día 0 · EN

**Asunto A:** {{company}} after dark  
**Asunto B:** Event coverage for {{company}}

```
Hi {{first_name}},

MIAGAZINE covers Miami's nights the way they deserve: photographed beautifully, published fast, in English and Spanish.

For your next event at {{company}} we offer Event Coverage ($900): photographer on site, edited gallery, recap story, newsletter and social. Our March edition, After Dark, is built around Miami Music Week.

Media kit attached. What's your next date?

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 1 · Media kit · día 0 · ES

**Asunto A:** {{company}} de noche  
**Asunto B:** Cobertura de eventos para {{company}}

```
Hola {{first_name}}:

MIAGAZINE cubre las noches de Miami como se merecen: bien fotografiadas, publicadas rápido, en español e inglés.

Para tu próximo evento en {{company}} ofrecemos Cobertura de evento ($900): fotógrafo en sitio, galería editada, historia recap, newsletter y redes. Nuestra edición de marzo, After Dark, gira en torno a Miami Music Week.

Te adjunto el media kit. ¿Cuál es tu próxima fecha?

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

---

## Cálido: nos conocimos en evento

### 1 · Media kit · día 1 · EN

**Asunto A:** Great meeting you at {{event}}  
**Asunto B:** From {{event}}: the MIAGAZINE media kit

```
Hi {{first_name}},

Great meeting you at {{event}}. As promised, here's the MIAGAZINE media kit.

The short version: a bilingual visual luxury magazine made by Miami photographers; formats from $150; 10 Founding Partner spots at $1,500/year. I also have a few frames from {{event}} that would suit {{company}} — happy to share them.

Coffee next week?

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 1 · Media kit · día 1 · ES

**Asunto A:** Un gusto conocerte en {{event}}  
**Asunto B:** De {{event}}: el media kit de MIAGAZINE

```
Hola {{first_name}}:

Un gusto conocerte en {{event}}. Como te prometí, aquí va el media kit de MIAGAZINE.

En corto: una revista visual de lujo bilingüe hecha por fotógrafos de Miami; formatos desde $150; 10 cupos de Socio Fundador a $1,500/año. También tengo algunas fotos de {{event}} que le quedarían muy bien a {{company}}; con gusto te las comparto.

¿Un café la próxima semana?

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

---

## Cálido: venue fotografiado

### 1 · Media kit · día 0 · EN

**Asunto A:** {{company}} goes live in MIAGAZINE on {{date}}  
**Asunto B:** Your share kit + a quick idea

```
Hi {{first_name}},

{{photographer}} shot a story at {{company}} and it goes live in MIAGAZINE on {{date}}. We'll send you the share kit that morning — please tag @miagazine.

If you'd like to amplify it, our partner rate for a newsletter feature plus a homepage week is $350. Media kit attached for everything else.

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 1 · Media kit · día 0 · ES

**Asunto A:** {{company}} sale en MIAGAZINE el {{date}}  
**Asunto B:** Tu kit para compartir + una idea

```
Hola {{first_name}}:

{{photographer}} hizo una historia en {{company}} y se publica en MIAGAZINE el {{date}}. Esa mañana te enviamos el kit para compartir; por favor etiqueta a @miagazine.

Si quieres amplificarla, nuestra tarifa de socio para destacado en newsletter más una semana en la home es de $350. Te adjunto el media kit para todo lo demás.

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

---

## Cálido: referido por fotógrafo

### 1 · Media kit · día 0 · EN

**Asunto A:** {{photographer}} suggested I write  
**Asunto B:** Via {{photographer}}: MIAGAZINE

```
Hi {{first_name}},

{{photographer}}, who's part of our photographer network, suggested {{company}} would be a natural fit for MIAGAZINE.

We're a new bilingual visual luxury magazine about Miami. {{photographer}} would love to shoot a story at {{company}} — as a Branded Story ($650) or within a Founding Partner year ($1,500).

Media kit attached. Can we set up a quick call with the three of us?

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### 1 · Media kit · día 0 · ES

**Asunto A:** {{photographer}} me sugirió escribirte  
**Asunto B:** De parte de {{photographer}}: MIAGAZINE

```
Hola {{first_name}}:

{{photographer}}, que forma parte de nuestra red de fotógrafos, nos sugirió que {{company}} encaja perfecto con MIAGAZINE.

Somos una nueva revista visual de lujo bilingüe sobre Miami. A {{photographer}} le encantaría hacer una historia en {{company}}, como Historia de marca ($650) o dentro de un año de Socio Fundador ($1,500).

Te adjunto el media kit. ¿Armamos una llamada rápida los tres?

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

---

## Respuestas

### Si pide precio especial · EN

**Asunto A:** Re: rates  
**Asunto B:** Re: rates

```
Hi {{first_name}},

Thanks for the interest. Our founding rates are already our lowest, and we keep them the same for every partner. What I can do is add a bonus: an extra newsletter placement in the Art Week issue if you confirm by {{date}}.

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### Si pide precio especial · ES

**Asunto A:** Re: tarifas  
**Asunto B:** Re: tarifas

```
Hola {{first_name}}:

Gracias por el interés. Las tarifas fundadoras ya son las más bajas y son iguales para todos los socios. Lo que sí puedo hacer es sumarte un envío extra de newsletter en la edición de Art Week si confirmas antes del {{date}}.

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

### Si pregunta por audiencia · EN

**Asunto A:** Re: audience  
**Asunto B:** Re: audience

```
Hi {{first_name}},

Fair question. We're a launching publication, so we don't sell inflated numbers: Founding Partners get our launch rate and a real report after every placement (reach, clicks, engagement). Our reach comes from the website, the newsletter, social and our photographer network, who share every story they appear in.

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### Si pregunta por audiencia · ES

**Asunto A:** Re: audiencia  
**Asunto B:** Re: audiencia

```
Hola {{first_name}}:

Buena pregunta. Somos una publicación en lanzamiento, así que no vendemos números inflados: los Socios Fundadores pagan la tarifa de lanzamiento y reciben un reporte real después de cada publicación (alcance, clics, interacción). Nuestro alcance viene de la web, el newsletter, las redes y la red de fotógrafos, que comparten cada historia en la que aparecen.

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```

### Si dice "sí" · EN

**Asunto A:** Welcome, {{company}}  
**Asunto B:** Next steps

```
Hi {{first_name}},

Wonderful — welcome to MIAGAZINE. Next steps:
1. Payment link to confirm your date: {{stripe_link}}
2. Logo (SVG/PNG) and 60-word copy, 7 days before publication
3. A 15-minute brief for your Branded Story: {{calendar_link}}

All paid content is labeled "Partner".

{{sender_name}}
Partnerships · MIAGAZINE
miagazine.com · @miagazine
[MAILING ADDRESS], Miami, FL

Not interested? Reply "no thanks" and we won't email you again.
```

### Si dice "sí" · ES

**Asunto A:** Bienvenida, {{company}}  
**Asunto B:** Próximos pasos

```
Hola {{first_name}}:

Excelente, bienvenidos a MIAGAZINE. Próximos pasos:
1. Link de pago para confirmar la fecha: {{stripe_link}}
2. Logo (SVG/PNG) y texto de 60 palabras, 7 días antes de la publicación
3. Brief de 15 minutos para tu Historia de marca: {{calendar_link}}

Todo contenido pagado se etiqueta "Partner".

{{sender_name}}
Alianzas · MIAGAZINE
miagazine.com/es · @miagazine
[DIRECCIÓN POSTAL], Miami, FL

¿No te interesa? Responde "no, gracias" y no te volveremos a escribir.
```
