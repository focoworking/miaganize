# Prompts de imagen — Portadas MIAGAZINE

Sistema visual para generar portadas en alta definición. Estilo minimalista, editorial, muy estilizado. Nada de stock genérico.
Prompts en inglés (los modelos rinden mejor). Sirven para Midjourney, Adobe Firefly, Imagen, Flux o DALL·E.

> **Regla de marca:** nuestra política dice "solo fotografía real como editorial". Estas imágenes se usan como **portadas ilustrativas del Journal** y **referencias de dirección de arte**, con el crédito visible: *"Illustration: AI-generated / Ilustración generada con IA"*. Los editoriales fotográficos y la cobertura de eventos siempre son foto real. Cuando tengas la foto real, reemplaza la imagen (campo `cover_image` en el `.md`).

---

## 1. ADN visual (aplicar a todo)

**Lo que SÍ:**
- Un solo sujeto. Mucho espacio negativo (40–60% del cuadro) para poner el titular.
- Paleta reducida: 2 tonos + el color de la categoría como acento.
- Luz natural dura de Miami o luz azul de la hora azul. Sombras gráficas y geométricas.
- Look de película de formato medio: grano fino, contraste suave, color sobrio.
- Texturas reales: terrazo, travertino, concreto, lino, agua, vidrio, cromo.
- Composición de revista: horizonte bajo, simetría o regla de tercios estricta, encuadres arquitectónicos.

**Lo que NO (prompt negativo base):**
`no text, no letters, no logos, no watermarks, no brand names, no recognizable people or celebrities, no famous artworks, no neon "Miami Vice" clichés, no sunset-palm-tree postcard, no oversaturated HDR, no lens flare, no clutter, no extra fingers, no distorted architecture, no stock-photo look, no 3D render look, no plastic skin`

**Sufijo de estilo (pegar al final de cada prompt):**
`— editorial photography for a luxury magazine, minimalist composition, generous negative space, medium-format film look (Hasselblad, Kodak Portra 400), fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K`

**Parámetros sugeridos (Midjourney):** `--style raw --stylize 150 --q 1` + relación de aspecto de la tabla.

## 2. Formatos por uso

| Uso | Relación | Px recomendados |
|---|---|---|
| Portada de artículo (web) | 2:1 | 3200 × 1600 |
| Tarjeta del Journal | 4:3 | 2400 × 1800 |
| Instagram carrusel/post | 4:5 | 2160 × 2700 |
| Story / Reel cover | 9:16 | 2160 × 3840 |
| Portada de edición (revista) | 3:4 | 2550 × 3400 (8.5×11 in a 300 dpi aprox.) |
| Pinterest | 2:3 | 2000 × 3000 |

Genera siempre en 2:1 y 4:5. El 4:3 sale recortando el 2:1.

---

## 3. Portadas de artículos (12)

Color de acento = color de la categoría en la web.

### 01 · Miami Art Week 2026 gratis — Arte y Cultura · acento #c2410c (naranja quemado)
**Concepto:** "La mesa como obra." Una mesa de ping-pong esculpida, sola, en un jardín vacío al amanecer.
```
A single sculptural ping-pong table painted in burnt orange stands alone on a manicured lawn at dawn, long diagonal shadow of a palm crossing the frame, one white ball resting at the net, pale limestone museum wall blurred in the far background, nobody around, quiet anticipation before an art fair, top 50% of the frame empty pale sky — editorial photography for a luxury magazine, minimalist composition, generous negative space, medium-format film look (Hasselblad, Kodak Portra 400), fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 2:1 --style raw
```

### 02 · Real estate de lujo 2026 — Real Estate · acento #0f766e (verde azulado)
**Concepto:** "Logos en el cielo, grietas abajo." Fachada de vidrio impecable arriba; concreto agrietado y una regla de inspección abajo.
```
Vertical split composition: upper two thirds a flawless teal-tinted glass curtain wall of a new waterfront tower reflecting a clean cobalt sky and a single construction crane; lower third weathered 1970s concrete balcony slab with a fine hairline crack and a yellow inspector's folding ruler resting on it, hard Miami noon light, crisp architectural lines, no people — editorial photography for a luxury magazine, minimalist composition, generous negative space, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 2:1 --style raw
```

### 03 · Wall Street South — Economía · acento #1e3a8a (azul marino)
**Concepto:** "El dinero madruga." Un traje azul marino doblado sobre una baranda frente a la bahía, 6 am.
```
A navy wool suit jacket neatly folded over a brushed-steel railing of a high-rise terrace at 6 a.m., a closed leather portfolio and a small espresso cup beside it, below and far away a calm bay with a single cruise ship silhouette in the haze, glass towers catching the first cold blue light, extreme order and stillness, upper half empty sky gradient from navy to pale gold — editorial photography for a luxury magazine, minimalist composition, generous negative space, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 2:1 --style raw
```

### 04 · Escena musical 2027 — Música · acento #7c3aed (violeta)
**Concepto:** "24 horas." Un vinilo girando sobre una consola junto a una ventana; afuera, el amanecer después de la fiesta.
```
Close still life of a black vinyl record spinning on a minimalist DJ turntable placed by a floor-to-ceiling window at dawn, violet stage-light haze fading inside the room, outside the bay and a distant skyline turning pale pink after an all-night party, a single pair of headphones resting on the deck, motion blur only on the record label, quiet afterglow mood — editorial photography for a luxury magazine, minimalist composition, generous negative space, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 2:1 --style raw
```

### 05 · Guía de modelaje y Swim Week — Moda y Modelos · acento #be185d (magenta)
**Concepto:** "La pasarela es agua." Una figura de espaldas en traje de baño escultórico, de pie al borde de una piscina, sombras geométricas.
```
Back view of an anonymous model in a sculptural magenta one-piece swimsuit standing at the edge of a geometric terrazzo pool, face not visible, strong midday shadows from a pastel Art Deco balustrade forming stripes across her body and the water, caustic light reflections on her skin, perfect symmetry, the rest of the frame clean pale pink wall and turquoise water — editorial fashion photography for a luxury magazine, minimalist composition, generous negative space, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 2:1 --style raw
```

### 06 · Tendencias de lujo 2027 — Tendencias · acento #b45309 (ámbar)
**Concepto:** "Lujo silencioso." Bodegón: reloj de acero de segunda mano, bolso vintage y un vaso de agua fría sobre travertino.
```
Minimal still life on a raw travertine table on a beach balcony at sunrise: a pre-owned steel wristwatch without visible logo, a small vintage cognac leather bag with no branding, a glass of ice water with condensation, one amber long shadow per object, background a soft-focus calm sea and pale apricot sky, extreme restraint, quiet luxury — editorial still-life photography for a luxury magazine, minimalist composition, generous negative space, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 2:1 --style raw
```

### 07 · Michelin Miami 2026 — Gastronomía · acento #9f1239 (carmesí)
**Concepto:** "Una sola pieza." Un nigiri en cerámica oscura con un rayo de luz, todo lo demás en sombra.
```
Overhead shot of a single piece of nigiri on a matte charcoal ceramic plate placed on a pale wood omakase counter, one sharp diagonal beam of late-afternoon Miami sunlight hitting only the fish, a tiny drop of crimson sauce beside it, chef's hand just leaving the edge of the frame, everything else falling into deep shadow, chiaroscuro, culinary precision — editorial food photography for a luxury magazine, minimalist composition, generous negative space, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 2:1 --style raw
```

### 08 · Vida en el agua / Boat Show 2027 — Vida en el agua · acento #0e7490 (cian)
**Concepto:** "Dibujar con estela." Vista cenital: un solo yate blanco trazando una curva perfecta en agua turquesa.
```
Top-down aerial photograph of a single white motor yacht drawing a perfect curved wake across flat turquoise and cyan water, a pale sandbar shape in the lower corner, no other boats, the wake forming an elegant calligraphic line, shallow water gradients from emerald to deep teal, midday light, graphic and abstract — editorial aerial photography for a luxury magazine, minimalist composition, generous negative space, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 2:1 --style raw
```

### 09 · Escena tech e IA 2026 — Tecnología · acento #0369a1 (azul)
**Concepto:** "Código en el reflejo." Una laptop cerrada sobre mármol; en el vidrio de la baranda se refleja una cuadrícula de luz.
```
A closed aluminum laptop and a single espresso cup on a white marble table on a high terrace at dusk, the glass railing in front faintly reflecting a soft grid of blue light like abstract data, glass towers blurred into cool blue bokeh behind, calm and precise, no screens visible, cold blue and warm white contrast — editorial photography for a luxury magazine, minimalist composition, generous negative space, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 2:1 --style raw
```

### 10 · Miami 2035 (ficción especulativa) — Tecnología · acento #0369a1
**Concepto:** "Mañana, en calma." Un water taxi autónomo sin piloto cruzando una bahía espejo hacia una ciudad con jardines verticales.
```
Speculative near-future scene: a sleek driverless electric water taxi with a translucent canopy gliding across a mirror-flat bay at pre-dawn, a thin light trail behind it, on the horizon a quiet skyline of towers with vertical gardens and a small rooftop vertiport glowing softly, living seawall with coral textures along the near shore, believable and understated, not sci-fi spectacle, pale blue and pearl palette — cinematic editorial photography for a luxury magazine, minimalist composition, generous negative space, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 2:1 --style raw
```
*(Etiqueta obligatoria: "Ilustración conceptual generada con IA".)*

### 11 · Nuevo skyline y arquitectura — Diseño y Arquitectura · acento #57534e (piedra)
**Concepto:** "Déco contra el cielo." Una curva de fachada Art Deco pastel en primer plano y, muy atrás, una torre de vidrio nueva.
```
Low-angle architectural photograph: in the foreground the rounded corner of a pastel Art Deco building with horizontal eyebrow ledges and a thin vertical fin, crisp shadows, in the far background one slender contemporary glass supertall rising into a clean pale sky, the two eras in dialogue, stone, cream and soft mint tones, no people, no signage — editorial architecture photography for a luxury magazine, minimalist composition, generous negative space, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 2:1 --style raw
```

### 12 · Mejores spots para fotografiar — Fotografía · acento #a16207 (ocre)
**Concepto:** "El que mira." Un trípode solo en la arena frente a una torre de salvavidas pastel, antes del amanecer.
```
An empty camera tripod standing alone on smooth sand facing a pastel lifeguard tower at blue hour just before sunrise, footprints leading to it, the Atlantic horizon low in the frame, the sky a gradient from deep ochre at the horizon to pale blue, absolute stillness, the photographer absent — editorial photography for a luxury magazine, minimalist composition, generous negative space, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 2:1 --style raw
```

---

## 4. Portadas de edición (revista)

Relación 3:4. Dejar el **tercio superior limpio** para el logotipo MIAGAZINE y el **tercio inferior izquierdo** para titulares.

### Edición #01 — "Art Week Through the Lens" (dic 2026)
```
Magazine cover photograph, portrait orientation: a woman seen from behind in a sharply tailored burnt-orange coat stands in front of a vast white gallery wall where a single small framed artwork hangs, her shadow cast long across the polished concrete floor, clean empty upper third for a masthead, extreme minimalism, quiet tension between viewer and art, no recognizable artwork — editorial cover photography for a luxury magazine, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 3:4 --style raw
```

### Edición #02 — "Art Deco at 50" (ene 2027)
```
Magazine cover photograph, portrait orientation: a vintage pastel mint convertible parked alone in front of a symmetrical cream and pink Art Deco facade at early morning, a model in a white 1930s-inspired linen suit and wide-brim hat leaning on the car, face turned away, crisp geometric shadows, empty pale sky in the upper third for the masthead, no signage, no license plate text — editorial cover photography for a luxury magazine, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 3:4 --style raw
```

### Edición #03 — "Waterfront" (feb 2027, Boat Show)
```
Magazine cover photograph, portrait orientation: aerial view straight down at the polished teak deck bow of a white yacht cutting through deep cyan water, a single folded white towel and a pair of sunglasses on the deck, the wake spreading below like a lace pattern, upper third pure open water texture for the masthead — editorial cover photography for a luxury magazine, medium-format film look, fine grain, soft contrast, muted refined palette, precise geometry, high-end art direction, ultra-detailed, 8K --ar 3:4 --style raw
```

---

## 5. Páginas del sitio

| Página | Prompt (añadir sufijo de estilo) | Formato |
|---|---|---|
| Home (hero) | `A camera lens resting on a terrazzo ledge, its glass reflecting a miniature Miami skyline at golden hour, everything else soft cream and shadow` | 2:1 y 4:5 |
| Quiénes somos | `Five empty director's chairs in a row on a white seamless studio backdrop, each with a different object on the seat: a camera, a notebook, a microphone, a phone, a fountain pen, warm side light` | 2:1 |
| Vacantes | `An open studio door with afternoon light spilling onto a concrete floor, a single unoccupied chair and a camera bag inside, invitation mood` | 2:1 |
| Historias / Open call | `A contact sheet of black-and-white film negatives on a light table, one frame circled in orange grease pencil, all images unreadable abstract shapes` | 2:1 |
| Centro legal | `A brass paperweight shaped like a camera on a stack of cream paper, a fountain pen beside it, strong window shadow, calm and authoritative` | 2:1 |
| Newsletter "The Lens" | `A single cream envelope on a sun-striped terrazzo floor, one palm-leaf shadow crossing it` | 3:1 |

---

## 6. Flujo de trabajo

1. Generar 4 variaciones por prompt (2:1). Elegir 1.
2. Pasar a 4:5 con "outpaint/expand" (no recortar la cara del concepto).
3. Escalar a 3200 px de ancho, exportar WebP (calidad 82) + JPG de respaldo.
4. Nombrar archivos: `slug-cover.webp`, `slug-cover-4x5.webp`.
5. Guardar en `site/assets/covers/` y añadir al `.md` del artículo:
   ```
   cover_image: "/assets/covers/slug-cover.webp"
   cover_alt: "Descripción literal de la imagen"
   cover_credit: "Ilustración generada con IA / AI-generated illustration"
   ```
6. `python3 build/build.py` → la web usa la imagen y el crédito automáticamente.
7. Cuando exista la foto real del fotógrafo, reemplazar y cambiar `cover_credit` por el nombre del fotógrafo.

## 7. Control de calidad (antes de publicar)
- ¿Hay texto, logos o marcas visibles? → regenerar.
- ¿Manos, caras o arquitectura deformes? → regenerar.
- ¿Se parece a una obra de arte o edificio protegido de forma identificable? → regenerar.
- ¿Respira? (40% de espacio negativo) → si no, recortar.
- ¿El acento de color coincide con la categoría? → ajustar en edición.
