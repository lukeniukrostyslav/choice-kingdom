import { chromium } from 'playwright';
const browser=await chromium.launch({headless:true});
const checks=[];
for(const vp of [{w:360,h:800},{w:412,h:915},{w:1440,h:900}]){
 const c=await browser.newContext({reducedMotion:'reduce'}); const p=await c.newPage({viewport:{width:vp.w,height:vp.h}});
 await p.goto('http://127.0.0.1:4173/design-v2/p23-audio-haptics-premium-feedback-proof.html',{waitUntil:'networkidle'});
 const x=await p.evaluate(()=>{
  const s=[...document.querySelectorAll('style')].map(x=>x.textContent||'').join('\n');
  const bs=[...document.querySelectorAll('.action')];
  const base=document.documentElement.scrollWidth<=innerWidth+1&&bs.every(b=>b.getBoundingClientRect().height>=56);
  const kinds=['confirm','warning','error','ambient'];
  const states=kinds.every(k=>{const b=bs.find(x=>x.dataset.kind===k);b.click();return b.getAttribute('aria-pressed')==='true'&&document.querySelector('#status').textContent.length>0&&bs.filter(x=>x.getAttribute('aria-pressed')==='true').length===1});
  return {base,states,responsive:/@media\(max-width:760px\)/.test(s)&&/@media\(max-width:420px\)/.test(s),safe:/safe-area-inset/.test(s),reduced:/prefers-reduced-motion:reduce/.test(s),focus:/:focus-visible/.test(s),rtl:/html\[dir=rtl\]/.test(s),serif:/var\(--serif\)/.test(s),cinematic:/radial-gradient/.test(s)&&/linear-gradient/.test(s),accessible:/aria-live/.test(document.body.innerHTML)&&/aria-label/.test(document.body.innerHTML),quiet:/optional/.test(document.body.innerText)&&/visual state/.test(document.body.innerText)};
 });
 checks.push({vp,res:Object.values(x).every(Boolean),x}); await c.close();
}
await browser.close();
if(checks.some(x=>!x.res)) throw new Error('P23 premium feedback closure failed: '+JSON.stringify(checks));
console.log('P23 PREMIUM FEEDBACK CLOSURE PASS: '+checks.length+' responsive viewport checks');