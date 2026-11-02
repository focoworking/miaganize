# Publicar miagazine.com y conectar integraciones

## 0. Hostinger (opción elegida) — configuración única, ≈10 min
La web publicada vive en la rama **`hostinger`** del repo (solo el contenido de `site/`, con `.htaccess` incluido). Cada cambio se hace desde la sesión de Claude con `./scripts/publish.sh`, que regenera la web y actualiza esa rama. Hostinger la descarga sola.

1. hPanel → **Sitios web → miagazine.com → Avanzado → GIT**.
2. En **Repositorio privado** copia la **clave SSH** que muestra Hostinger.
3. GitHub → repo `focoworking/miaganize` → **Settings → Deploy keys → Add deploy key** → pega la clave, solo lectura → Add.
4. De vuelta en hPanel → **Crear repositorio nuevo**:
   - Repositorio: `git@github.com:focoworking/miaganize.git`
   - Rama: `hostinger`
   - Directorio: *(vacío → public_html)*. **public_html debe estar vacío**: borra `default.php` desde el Administrador de archivos.
   - Crear → **Desplegar**.
5. En el mismo panel activa **Implementación automática** y copia la **URL del webhook**.
6. GitHub → **Settings → Webhooks → Add webhook** → Payload URL = esa URL · Content type `application/json` · solo evento *push* → Add.
7. hPanel → **Seguridad → SSL** → instala el SSL gratis para miagazine.com y www. El `.htaccess` ya fuerza HTTPS y www.
8. Verifica: https://www.miagazine.com, /es/, /media-kit, /blog/.

Desde ahí: **todos los cambios se hacen desde la sesión de Claude**. No edites archivos en el Administrador de archivos de Hostinger: el siguiente despliegue los sobrescribe.

---
## Alternativa: Cloudflare Pages

Todo lo técnico ya está listo en el repo. Solo faltan tus cuentas.

1. Crear cuenta en dash.cloudflare.com → **Workers & Pages → Create → Pages → Connect to Git**.
2. Elegir el repo `focoworking/miaganize`, rama `main` (primero hacer merge de `claude/miagazine-launch`).
3. Configuración de build:
   - Framework preset: **None**
   - Build command: *(vacío)* — el sitio ya va generado en `site/`
   - Build output directory: **`site`**
4. Deploy. Queda en `miaganize.pages.dev`.
5. **Custom domains → Set up a domain → `miagazine.com` y `www.miagazine.com`.** Si el dominio está en otro registrador, cambiar los nameservers a Cloudflare (Cloudflare te muestra cuáles).
6. Ya incluidos: `site/_headers` (seguridad y caché) y `site/_redirects` (`/media-kit`, `/kit`, `/es`).

## 2. Email del dominio (obligatorio antes de enviar outreach)
- Recibir: Cloudflare **Email Routing** (gratis) → reenvía hello@, partners@, editorial@, legal@, privacy@, careers@, dmca@ a tu bandeja.
- Enviar desde partners@: Google Workspace o Zoho Mail.
- Activar **SPF, DKIM y DMARC** (el proveedor te da los registros DNS; se pegan en Cloudflare DNS).

## 3. Integraciones → un solo archivo
Abrir `config/integrations.json`, pegar los links y correr:
```
pip install markdown pyyaml
python3 build/build.py
```
El generador reemplaza los placeholders en todas las páginas (ES y EN). Hacer commit y push: Cloudflare publica solo.

| Clave | Dónde se obtiene |
|---|---|
| `BEEHIIV_FORM_ACTION` | beehiiv → Grow → Subscribe forms → embed → URL del `action` del formulario |
| `TALLY_FORM_URL` | tally.so → formulario de envíos (campos en `docs/02-PROGRAMA-FOTOGRAFOS.md`) → Share link |
| `CALENDLY_URL` | Calendly (o Cal.com gratis) → evento "Llamada 15 min MIAGAZINE" |
| `WHATSAPP_URL` | `https://wa.me/1XXXXXXXXXX` (número de negocio, solo dígitos) |
| `STRIPE_*` | Stripe → Payment Links: uno por producto (ver tabla abajo) |

### Payment Links de Stripe a crear
| Clave | Producto | Precio |
|---|---|---|
| STRIPE_NEWSLETTER | Newsletter Sponsor | $150 |
| STRIPE_HOMEPAGE | Homepage Feature (1 semana) | $250 |
| STRIPE_SELECTS | MIA Selects | $99 / mes (suscripción) |
| STRIPE_STORY | Branded Story | $650 |
| STRIPE_REEL | Branded Reel | $450 |
| STRIPE_EVENT | Event Coverage | $900 |
| STRIPE_FILM | Event Recap Film | $1,200 |
| STRIPE_ISSUE | Issue Sponsor | $500 |
| STRIPE_FOUNDING | Founding Partner | $1,500 / año |
| STRIPE_FOUNDING_QUARTERLY | Founding Partner trimestral | $400 cada 3 meses × 4 (suscripción con fin) |
| STRIPE_BUNDLE_ARTWEEK | Art Week Bundle | $1,200 |
| STRIPE_BUNDLE_ARTDECO | Art Deco Weekend Bundle | $950 |
| STRIPE_BUNDLE_BOATSHOW | Boat Show Bundle | $1,400 |

## 4. Después de publicar
- Google Search Console + Bing Webmaster → enviar `https://www.miagazine.com/sitemap.xml`.
- Cloudflare Web Analytics (sin cookies) → activar en el panel de Pages.
- Registrar el agente DMCA en copyright.gov (DMCA Designated Agent Directory) y completar el nombre en las páginas legales.
- Rellenar `[RAZÓN SOCIAL]` / `[LEGAL ENTITY NAME]` y `[DIRECCIÓN POSTAL]` en `content/pages/*.md`, `contracts/build_io.py` y `outreach/build_emails.py`, y regenerar.

## Regenerar materiales
| Qué | Comando |
|---|---|
| Web | `python3 build/build.py` |
| Media kit PDF | `python3 media-kit/build_kit.py` y copiar los PDF a `site/media-kit/` |
| Emails | `python3 outreach/build_emails.py` |
| Orden de publicidad | `python3 contracts/build_io.py` |
