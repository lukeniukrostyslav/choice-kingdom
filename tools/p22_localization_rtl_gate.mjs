import { chromium } from 'playwright';
const browser=await chromium.launch({headless:true});
const checks=[];
for(const vp of [{w:360,h:800},{w:412,h:915},{w:1440,h:900}]){
 const c=await browser.newContext({reducedMotion:'reduce'}); const p=await c.newPage({viewport:{width:vp.w,height:vp.h}});
 const res=await p.goto('http://127.0.0.1:4173/design-v2/p22-localization-rtl-proof.html',{waitUntil:'networkidle'});
 const x=await p.evaluate(()=>{
  const s=[...document.querySelectorAll('style')].map(x=>x.textContent||'').join('\n');
  const bs=[...document.querySelectorAll('.locale')];
  const base=()=>document.documentElement.scrollWidth<=innerWidth+1 && [...document.querySelectorAll('.locale')].every(b=>b.getBoundingClientRect().height>=48);
  bs.find(b=>b.dataset.lang==='it').click(); const it=document.documentElement.lang==='it'&&document.documentElement.dir==='ltr'&&document.querySelector('#status').textContent.includes('Italiano');
  bs.find(b=>b.dataset.lang==='uk').click(); const uk=document.documentElement.lang==='uk'&&document.documentElement.dir==='ltr'&&document.querySelector('#sample-title').textContent.includes('Рада');
  bs.find(b=>b.dataset.lang==='ar').click(); const ar=document.documentElement.lang==='ar'&&document.documentElement.dir==='rtl'&&document.querySelector('#sample-title').textContent.includes('ينتظر')&&document.querySelector('#status').textContent.includes('العربية');
  bs.find(b=>b.dataset.lang==='en').click(); const reset=document.documentElement.lang==='en'&&document.documentElement.dir==='ltr';
  const exclusive=bs.filter(b=>b.getAttribute('aria-pressed')==='true').length===1;
  const long=document.querySelector('#sample-copy'); const old=long.textContent; long.textContent=old.repeat(20); const noOverflow=document.documentElement.scrollWidth<=innerWidth+1; long.textContent=old;
  return {base,it,uk,ar,reset,exclusive,noOverflow,responsive:/@media\(max-width:760px\)/.test(s)&&/@media\(max-width:420px\)/.test(s),rtl:/html\[dir=rtl\]/.test(s),safe:/safe-area-inset/.test(s),reduced:/prefers-reduced-motion:reduce/.test(s),focus:/:focus-visible/.test(s),serif:/var\(--ck-serif\)/.test(s),cinematic:/radial-gradient/.test(s)&&/linear-gradient/.test(s),allText:[...document.querySelectorAll('h1,h2,h3,p,button')].every(e=>e.scrollWidth<=e.clientWidth+1||getComputedStyle(e).overflow!=='hidden')};
 });
 checks.push({vp,res:res?.ok()&&Object.values(x).every(Boolean),x}); await c.close();
}
await browser.close();
if(checks.some(x=>!x.res)) throw new Error('P22 localization/RTL closure failed: '+JSON.stringify(checks));
console.log('P22 LOCALIZATION/RTL CLOSURE PASS: '+checks.length+' responsive viewport checks');
