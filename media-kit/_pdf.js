const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for (const f of ["/home/user/miaganize/media-kit/MIAGAZINE-Media-Kit-2026-EN", "/home/user/miaganize/media-kit/MIAGAZINE-Media-Kit-2026-ES"]){const p=await b.newPage();await p.goto('file://'+f+'.html',{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:f+'.pdf',width:'11in',height:'8.5in',printBackground:true,preferCSSPageSize:true});
console.log('ok',f)}
await b.close()})();