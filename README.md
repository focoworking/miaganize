# MIAGAZINE — miagazine.com

Revista digital de lujo de Miami. "Miami, through the lens."

## Estructura
- `docs/01-ESTRATEGIA.md` — plan maestro: modelo, ingresos, distribución, eventos, 360 SEO/AEO/GEO/LLM/AI, stack, KPIs
- `docs/02-PROGRAMA-FOTOGRAFOS.md` — programa de fotógrafos, licencia, open calls, respuestas tipo
- `docs/03-MEDIA-KIT.md` — paquetes y precios founding
- `docs/04-OUTREACH.md` — plantillas email/DM para marcas, fotógrafos y swaps
- `docs/05-ROADMAP-90-DIAS.md` — checklist 1 nov 2026 → 31 ene 2027
- `docs/06-SOCIAL-MEDIA.md` — sistema de social media + calendario de arranque
- `docs/07-PLAN-VISITAS.md` — plan de visitas nov 2026–ene 2027
- `content/research/eventos-nov2026-ene2027.md` — 57 eventos con fuentes
- `content/blog/*.{es,en}.md` — Journal bilingüe (12 artículos × 2 idiomas)
- `build/build.py` — genera `site/` (ES en /es/, EN en /). Correr: `pip install markdown pyyaml && python3 build/build.py`
- `site/` — web estática generada, lista para deploy

## Deploy (gratis)
Cloudflare Pages → conectar repo → build command: vacío → output directory: `site`. Agregar dominio miagazine.com.

## Placeholders a reemplazar en `site/`
- `BEEHIIV_FORM_ACTION` → URL del formulario embebido de beehiiv
- `TALLY_FORM_URL` → formulario de submissions (Tally)
- `STRIPE_LINK_1..7` → Payment Links de Stripe (orden de la tabla en advertise.html)
- Imágenes `.ph` → fotos reales (WebP, alt descriptivo)
- Handles sociales en JSON-LD `sameAs`
