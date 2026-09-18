import { chromium } from 'playwright';

const base = process.env.P25_BASE_URL || 'http://127.0.0.1:4173';
const browser = await chromium.launch({headless:true});
const page = await browser.newPage({viewport:{width:390,height:844}, reducedMotion:'reduce'});
const fail = msg => { throw new Error('P25 gate: '+msg); };

await page.goto(base+'/index.html', {waitUntil:'networkidle'});
if (!(await page.getByText('Enter the interactive kingdom').count())) fail('launcher missing interactive entry');
await page.getByText('Enter the interactive kingdom').click();
await page.getByRole('button',{name:'Start a new run'}).click();
if ((await page.locator('#eventTitle').textContent()) !== 'The First Petition') fail('E01 not rendered');
await page.getByRole('button',{name:/Open the Hall/}).click();
if (!(await page.locator('#consequenceText').textContent()).includes('Open the Hall')) fail('consequence not rendered');
await page.getByRole('button',{name:/Continue to E02/}).click();
if ((await page.locator('#eventTitle').textContent()) !== 'The Empty Chair') fail('E02 not reached');
await page.getByRole('button',{name:/Archive it and investigate/}).click();
await page.getByRole('button',{name:/Continue to E05/}).click();
if ((await page.locator('#eventTitle').textContent()) !== "A Captain's Warning") fail('E05 not reached');
await page.getByRole('button',{name:/Audit the guard/}).click();
await page.getByRole('button',{name:/Return to the Kingdom/}).click();
if (!(await page.locator('#kingdom').evaluate(el=>el.classList.contains('active')))) fail('kingdom not reached');

await page.getByRole('button',{name:'People'}).click();
for (const n of ['Mara','Rowan','Seris','Ivo','Amara','Toma']) if (!(await page.getByText(n,{exact:true}).count())) fail('missing canonical person '+n);
await page.getByRole('button',{name:'Factions'}).click();
for (const n of ['Crown','Commons','Noble','Guild','Border / Security','Civic / Medical']) if (!(await page.getByText(n,{exact:true}).count())) fail('missing canonical institution '+n);
await page.getByRole('button',{name:'Investigation'}).click();
for (const n of ["Mara's route","Toma's route","Seris's route","Direct account route"]) if (!(await page.getByText(n,{exact:true}).count())) fail('missing investigation route '+n);
await page.getByRole('button',{name:'History'}).click();
if (!(await page.getByText('E01 · The First Petition').count())) fail('history did not record E01');
await page.getByRole('button',{name:'Endings'}).click();
if (!(await page.getByRole('heading',{name:'Endings'}).count())) fail('endings surface missing');
if (!(await page.getByText('No ending is forced in the visual prototype.').count())) fail('ending boundary copy missing');
await page.getByRole('button',{name:'Settings'}).click();
await page.getByRole('button',{name:'Large text'}).click();
await page.getByRole('button',{name:'RTL preview'}).click();
await page.getByRole('button',{name:'Reduced motion'}).click();

const body = await page.locator('body').innerText();
for (const forbidden of ['Queen Elira','Lord Cael','River Compact','Arwen Vale','The Empty Granary','Royal Capital','Northern Marches','The Church','Trade Guilds','Southern Reach','Eastern Realms']) if (body.includes(forbidden)) fail('non-canonical legacy text leaked: '+forbidden);

await page.setViewportSize({width:1440,height:1000});
await page.goto(base+'/game-flow.html',{waitUntil:'networkidle'});
if (!(await page.locator('.app').isVisible())) fail('expanded layout failed');
await page.screenshot({path:'p25-expanded.png',fullPage:true});
await page.setViewportSize({width:360,height:800});
await page.reload({waitUntil:'networkidle'});
await page.screenshot({path:'p25-compact.png',fullPage:true});

await browser.close();
console.log('P25 interactive gate: PASS');

// P25 final-gate verification branch: execute the same frozen-reference interactive regression suite.
