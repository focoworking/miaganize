#!/usr/bin/env python3
"""Insertion Order / Orden de publicidad MIAGAZINE -> HTML + PDF (Letter). Usage: python3 contracts/build_io.py"""
import os, json, subprocess
D = os.path.dirname(os.path.abspath(__file__))
T = {
'en': dict(file='MIAGAZINE-Insertion-Order-EN', title='Insertion Order', sub='Advertising & Branded Content Agreement',
 no='IO No.', date='Date', between='This Insertion Order ("IO") is entered into between [LEGAL ENTITY NAME], a Florida limited liability company doing business as MIAGAZINE ("MIAGAZINE"), and the client identified below ("Client").',
 client=['Client legal name','Brand / trade name','Contact name & title','Email · Phone','Billing address'],
 camp='1. Campaign', th=['Item / package','Publication dates','Deliverables','Price (USD)'],
 total='Total', pay_t='2. Payment', pay=['Payment by the secure link sent by MIAGAZINE (Stripe). The publication date is confirmed once payment is received.','Founding Partner: paid upfront, or in 4 quarterly installments of $400 (first due at signing, then every 90 days). If an installment is more than 15 days late, MIAGAZINE may pause deliverables until paid.','Prices exclude any applicable taxes. Paid ad spend (boosting) is not included unless stated above.'],
 sections=[
  ('3. Materials & approvals',['Client delivers logo, copy, links and access details at least 7 days before publication.','Client may review one round for factual accuracy (names, dates, prices) within 48 hours. MIAGAZINE keeps editorial voice, image selection and final layout.']),
  ('4. Disclosure',['All paid content is labeled “Partner” or “Paid partnership”, as required by the FTC Act and the FTC Endorsement Guides (16 CFR Part 255). Client will not ask MIAGAZINE or its creators to hide or remove the disclosure.']),
  ('5. Ownership & usage rights',['Photos and video remain the property of MIAGAZINE and/or the credited photographer or filmmaker.','Client receives a non-exclusive license to share the published content and the delivered files on its own website and organic social media for 12 months from publication, with credit “@miagazine / photographer”.','Paid advertising, whitelisting, print, out-of-home or use beyond 12 months require a separate written license and fee. Client may not alter content in a way that changes its meaning or use it to train AI systems.']),
  ('6. Client warranties',['Client owns or is authorized to use the trademarks, logos and materials it supplies, and grants MIAGAZINE a limited license to use them for this campaign.','Client secures venue access and any permits for its own events, and obtains releases from its staff appearing in content.']),
  ('7. Cancellation & rescheduling',['Cancellation 7 or more days before publication: full refund. Less than 7 days: no refund; MIAGAZINE may offer one new date within 60 days.','If an event is cancelled or weather or force majeure prevents production, the parties will reschedule or MIAGAZINE will issue a credit of equal value.']),
  ('8. Reporting',['MIAGAZINE sends a performance report (reach, clicks, engagement) within 14 days of publication. Specific audience results are not guaranteed.']),
  ('9. Liability',['Each party’s total liability under this IO is limited to the fees paid under it. Neither party is liable for indirect, incidental or consequential damages.']),
  ('10. General',['This IO incorporates MIAGAZINE’s Terms of Use and Editorial Policy (miagazine.com/legal). It is governed by the laws of the State of Florida, with venue in Miami-Dade County. This IO is the entire agreement for this campaign and may be signed electronically.'])],
 sig=['For MIAGAZINE','For Client'], sig_f=['Name','Title','Signature','Date'],
 disc='Template for informational purposes; not legal advice. Have it reviewed by a Florida-licensed attorney before use.'),
'es': dict(file='MIAGAZINE-Orden-de-Publicidad-ES', title='Orden de publicidad', sub='Acuerdo de publicidad y contenido de marca',
 no='Orden N.º', date='Fecha', between='Esta Orden de Publicidad (la “Orden”) se celebra entre [RAZÓN SOCIAL], compañía de responsabilidad limitada de Florida que opera como MIAGAZINE (“MIAGAZINE”), y el cliente identificado abajo (el “Cliente”).',
 client=['Razón social del cliente','Marca / nombre comercial','Contacto y cargo','Email · Teléfono','Dirección de facturación'],
 camp='1. Campaña', th=['Ítem / paquete','Fechas de publicación','Entregables','Precio (USD)'],
 total='Total', pay_t='2. Pago', pay=['Pago por el link seguro que envía MIAGAZINE (Stripe). La fecha de publicación se confirma al recibir el pago.','Socio Fundador: pago único, o 4 cuotas trimestrales de $400 (la primera al firmar y luego cada 90 días). Si una cuota se atrasa más de 15 días, MIAGAZINE puede pausar los entregables hasta el pago.','Los precios no incluyen impuestos aplicables. La inversión en pauta pagada (boost) no está incluida salvo que se indique arriba.'],
 sections=[
  ('3. Materiales y aprobaciones',['El Cliente entrega logo, textos, links y datos de acceso al menos 7 días antes de la publicación.','El Cliente puede revisar una vez la exactitud de los datos (nombres, fechas, precios) dentro de 48 horas. MIAGAZINE conserva la voz editorial, la selección de imágenes y el diseño final.']),
  ('4. Divulgación',['Todo contenido pagado se etiqueta “Partner” o “Colaboración pagada”, según la Ley de la FTC y las Guías de Respaldo de la FTC (16 CFR Parte 255). El Cliente no pedirá a MIAGAZINE ni a sus creadores ocultar o retirar la divulgación.']),
  ('5. Propiedad y derechos de uso',['Las fotos y videos son propiedad de MIAGAZINE y/o del fotógrafo o filmmaker acreditado.','El Cliente recibe una licencia no exclusiva para compartir el contenido publicado y los archivos entregados en su web y redes sociales orgánicas durante 12 meses desde la publicación, con crédito “@miagazine / fotógrafo”.','Publicidad pagada, whitelisting, impresión, exteriores o uso por más de 12 meses requieren licencia escrita y pago aparte. El Cliente no puede alterar el contenido cambiando su sentido ni usarlo para entrenar sistemas de IA.']),
  ('6. Garantías del Cliente',['El Cliente es titular o está autorizado a usar las marcas, logos y materiales que entrega, y otorga a MIAGAZINE una licencia limitada para usarlos en esta campaña.','El Cliente garantiza el acceso al lugar y los permisos de sus propios eventos, y obtiene los releases de su personal que aparezca en el contenido.']),
  ('7. Cancelación y reprogramación',['Cancelación con 7 días o más de anticipación: reembolso completo. Con menos de 7 días: sin reembolso; MIAGAZINE puede ofrecer una nueva fecha dentro de 60 días.','Si un evento se cancela o el clima o fuerza mayor impiden la producción, las partes reprogramarán o MIAGAZINE emitirá un crédito por el mismo valor.']),
  ('8. Reporte',['MIAGAZINE envía un reporte de resultados (alcance, clics, interacción) dentro de 14 días desde la publicación. No se garantizan resultados de audiencia específicos.']),
  ('9. Responsabilidad',['La responsabilidad total de cada parte bajo esta Orden se limita a los honorarios pagados bajo ella. Ninguna parte responde por daños indirectos, incidentales o consecuentes.']),
  ('10. General',['Esta Orden incorpora los Términos de Uso y la Política Editorial de MIAGAZINE (miagazine.com/es/legal). Se rige por las leyes del Estado de Florida, con jurisdicción en el condado de Miami-Dade. Es el acuerdo completo para esta campaña y puede firmarse electrónicamente.'])],
 sig=['Por MIAGAZINE','Por el Cliente'], sig_f=['Nombre','Cargo','Firma','Fecha'],
 disc='Plantilla informativa; no constituye asesoría legal. Debe revisarla un abogado licenciado en Florida antes de usarla.'),
}
CSS = '''@page{size:8.5in 11in;margin:.55in .6in}
*{box-sizing:border-box;margin:0;padding:0}
body{font:8.6pt/1.42 "Inter",sans-serif;color:#0e0e0e;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.top{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:1.5px solid #0e0e0e;padding-bottom:.1in}
.logo{font-family:"Cormorant Garamond",serif;font-weight:600;letter-spacing:.32em;font-size:20pt}
h1{font-family:"Cormorant Garamond",serif;font-weight:500;font-size:22pt;line-height:1;text-align:right}
.sub{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;color:#b08d57;text-align:right;margin-top:3px}
.meta{display:flex;gap:.4in;margin:.12in 0 .08in;font-size:8pt}.meta span{border-bottom:1px solid #999;min-width:1.4in;display:inline-block}
.lead{margin:.06in 0 .1in}
.grid{display:grid;grid-template-columns:1.3in 1fr;border:1px solid #d9d3c9}
.grid div{padding:5px 8px;border-bottom:1px solid #d9d3c9;min-height:.26in}.grid div:nth-child(odd){background:#f6f3ee;font-size:7.5pt;color:#6b665f}
h2{font-family:"Cormorant Garamond",serif;font-weight:600;font-size:12.5pt;margin:.13in 0 .04in}
table{width:100%;border-collapse:collapse}th{text-align:left;font-size:6.8pt;letter-spacing:.14em;text-transform:uppercase;color:#6b665f;border-bottom:1px solid #0e0e0e;padding:4px 6px;font-weight:500}
td{border-bottom:1px solid #d9d3c9;padding:5px 6px;height:.3in}
td.tot{font-weight:600;text-align:right}
ul{padding-left:14px}li{margin:2px 0}
.cols{columns:2;column-gap:.3in}.cols section{break-inside:avoid}
.sig{display:grid;grid-template-columns:1fr 1fr;gap:.4in;margin-top:.18in}
.sig b{display:block;font-size:8pt;letter-spacing:.14em;text-transform:uppercase;margin-bottom:.05in}
.sig div div{border-bottom:1px solid #999;height:.3in;font-size:6.8pt;color:#6b665f;display:flex;align-items:flex-end;padding-bottom:2px}
.disc{margin-top:.15in;font-size:6.8pt;color:#6b665f;font-style:italic;border-top:1px solid #d9d3c9;padding-top:.06in}'''
def doc(L):
    t = T[L]
    rows = ''.join('<tr><td></td><td></td><td></td><td></td></tr>' for _ in range(4))
    secs = ''.join(f'<section><h2>{h}</h2><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></section>' for h, items in t['sections'])
    sig = ''.join(f'<div><b>{s}</b>{"".join(f"<div>{f}</div>" for f in t["sig_f"])}</div>' for s in t['sig'])
    return f'''<!doctype html><html lang="{L}"><head><meta charset="utf-8"><title>MIAGAZINE {t['title']}</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>
<div class="top"><div class="logo">MIAGAZINE</div><div><h1>{t['title']}</h1><div class="sub">{t['sub']}</div></div></div>
<div class="meta"><div>{t['no']} <span></span></div><div>{t['date']} <span></span></div></div>
<p class="lead">{t['between']}</p>
<div class="grid">{"".join(f"<div>{c}</div><div></div>" for c in t['client'])}</div>
<h2>{t['camp']}</h2><table><thead><tr>{"".join(f"<th>{x}</th>" for x in t['th'])}</tr></thead><tbody>{rows}<tr><td colspan="3" class="tot">{t['total']}</td><td></td></tr></tbody></table>
<h2>{t['pay_t']}</h2><ul>{"".join(f"<li>{x}</li>" for x in t['pay'])}</ul>
<div class="cols">{secs}</div>
<div class="sig">{sig}</div><p class="disc">{t['disc']}</p></body></html>'''
if __name__ == '__main__':
    files = []
    for L in T:
        f = os.path.join(D, T[L]['file']); open(f + '.html', 'w').write(doc(L)); files.append(f)
    js = r'''const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();for(const f of %s){const p=await b.newPage();await p.goto('file://'+f+'.html',{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.pdf({path:f+'.pdf',width:'8.5in',height:'11in',printBackground:true,preferCSSPageSize:true});console.log('ok',f)}await b.close()})();''' % json.dumps(files)
    open(os.path.join(D, '_pdf.js'), 'w').write(js); subprocess.run(['node', os.path.join(D, '_pdf.js')], check=True)
