# Brief para escribir blogs MIAGAZINE

MIAGAZINE = revista digital (y futura impresa) de lujo de Miami. "Miami, through the lens." Visual, editorial, sofisticada pero muy entretenida de leer: ritmo, datos sorprendentes, escenas, voz con personalidad (tipo Monocle / Robb Report / Vanity Fair, nunca corporativo ni de agencia SEO). Hoy es 1 nov 2026.

## Entregable por tema
Dos archivos por artículo, MISMO slug (en inglés, kebab-case):
- /home/user/miaganize/content/blog/<slug>.es.md  (español neutro latino, natural, no traducido literal)
- /home/user/miaganize/content/blog/<slug>.en.md  (inglés americano)

Largo: 1,100–1,800 palabras de cuerpo cada idioma.

## Formato exacto (YAML front matter + markdown)
```
---
title: "Título atractivo (máx 70 caracteres)"
slug: "mismo-slug-en-ambos"
lang: "es"            # o "en"
category: "Real Estate"   # una de: Art & Culture, Fashion & Models, Real Estate, Economy, Music, Trends, Food & Drink, Tech, Waterfront, Design & Architecture, Sports & Lifestyle, Photography
date: "2026-11-01"
excerpt: "1–2 frases que den ganas de leer (máx 180 caracteres)."
reading_minutes: 7
cover_hint: "descripción de la foto de portada ideal (para el fotógrafo)"
tldr:
  - "Respuesta directa 1 (frase con dato)"
  - "Respuesta directa 2"
  - "Respuesta directa 3"
faq:
  - q: "Pregunta que la gente busca en Google/ChatGPT"
    a: "Respuesta directa 40–60 palabras."
  - q: "..."
    a: "..."
sources:
  - title: "Nombre de la fuente oficial"
    url: "https://..."
---
Cuerpo en markdown.
```
(category siempre en inglés en ambos idiomas, tal cual la lista.)

## Reglas del cuerpo
- Abrir con escena o gancho (2–4 frases), luego un párrafo que responda directo la pregunta principal (AEO).
- H2 (##) frecuentes, varios en forma de pregunta. Opcional H3.
- Al menos 1 pull quote: línea que empieza con `> ` (frase memorable, no cita inventada de persona real).
- 2–4 "datos" destacados: línea propia que empieza con `!! ` seguido del dato corto con cifra (ej. `!! 2,500 millones de dólares: ...`).
- Al menos una tabla o lista útil.
- Una sección final "Through the lens" / "A través del lente": cómo fotografiar/vivir el tema en Miami (tips para fotógrafos y lectores).
- Links en texto a fuentes oficiales cuando cites cifras.
- Fuentes: 4–8, priorizando oficiales (gobierno, organizaciones del evento, asociaciones, reportes de la industria, medios serios). Verifica con WebSearch; NO inventes cifras, citas, ni URLs. Si un dato no se puede verificar, no lo uses. Fecha cada dato ("según X, 2025").
- Nada de citas textuales atribuidas a personas reales salvo que la verifiques en la fuente.
- No mencionar datos personales de nadie del equipo.
- Excepción: si el brief del tema pide una pieza especulativa, debe declararse claramente como ficción/concepto en el primer párrafo y en el título o excerpt.
