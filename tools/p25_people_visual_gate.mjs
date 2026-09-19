import { chromium } from 'playwright';

const base = process.env.P25_BASE_URL || 'http://127.0.0.1:4173';
const browser = await chromium.launch({headless:true});
const page = await browser.newPage({viewport:{width:390,height:844}, reducedMotion:'reduce'});
const fail = msg => { throw new Error('P25 People gate: '+msg); };
await page.goto(base + '/game-premium.html', {waitUntil:'networkidle'});
await page.evaluate(() => { const s=document.createElement('style'); s.textContent='*,*::before,*::after{animation:none!important;transition:none!important}'; document.head.appendChild(s); document.body.classList.add('reduce'); localStorage.removeItem('ck-p25-v2'); localStorage.removeItem('ck-p25-v2-prefs'); });
await page.getByRole('button',{name:'Start a new run'}).click();
const choice = page.locator('#choices .choice').filter({hasText:'Open the Hall'}).first();
if (!(await choice.isVisible())) fail('Open the Hall choice not visible');
await choice.click();
await page.getByRole('button',{name:'Kingdom',exact:true}).click();
await page.getByRole('button',{name:'People',exact:true}).click();
const cards = page.locator('#people [data-kind="person"]');
if (await cards.count() !== 6) fail('expected 6 People cards');
for (const name of ['Mara','Rowan','Seris','Ivo','Amara','Toma']) if (!(await page.getByText(name,{exact:true}).count())) fail('missing '+name);
const images = page.locator('#people .person-portrait');
if (await images.count() !== 6) fail('expected 6 portrait images');
for (let i=0;i<await images.count();i++) { const img=images.nth(i); await img.waitFor({state:'visible'}); const ok=await img.evaluate(el=>({complete:el.complete,naturalWidth:el.naturalWidth,naturalHeight:el.naturalHeight,src:el.currentSrc||el.src})); if (!ok.complete || ok.naturalWidth < 2 || ok.naturalHeight < 2) fail('portrait '+i+' did not load: '+JSON.stringify(ok)); }
await page.screenshot({path:'p25-people-visual.png',fullPage:true});
console.log('P25 People gate PASS', {base, portraits:6});
await browser.close();