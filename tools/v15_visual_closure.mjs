import { chromium } from 'playwright';
import fs from 'node:fs';

const pages = [
  'index.html',
  'game-flow.html',
  'artwork-preview.html',
  'design-art-direction.html',
  'design-asset-production.html',
  'design-accessibility-final.html',
  'design-character-faction-final.html'
];
const viewports = [
  { name: '360x800', width: 360, height: 800 },
  { name: '412x915', width: 412, height: 915 },
  { name: '412x1000', width: 412, height: 1000 },
  { name: '1440x900', width: 1440, height: 900 }
];
const requiredArtwork = [
  'artwork/event-empty-granary.svg',
  'artwork/queen-elira.svg',
  'artwork/lord-cael.svg',
  'artwork/river-compact.svg',
  'artwork/ending-chronicle.svg'
];

const browser = await chromium.launch({ headless: true });
const results = [];
let failures = 0;

for (const file of pages) {
  for (const vp of viewports) {
    const context = await browser.newContext({ deviceScaleFactor: 1, reducedMotion: 'reduce' });
    const page = await context.newPage({ viewport: { width: vp.width, height: vp.height } });
    const consoleErrors = [];
    const pageErrors = [];
    const failedRequests = [];
    page.on('console', m => { if (m.type() === 'error') consoleErrors.push(m.text()); });
    page.on('pageerror', e => pageErrors.push(String(e)));
    page.on('requestfailed', r => failedRequests.push(r.url()));
    const response = await page.goto(`http://127.0.0.1:4173/${file}`, { waitUntil: 'networkidle' });
    const metrics = await page.evaluate(() => {
      const interactive = [...document.querySelectorAll('a,button,input,select,textarea,[role="button"]')];
      const visible = interactive.filter(el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
      const smallTargets = visible.filter(el => { const r = el.getBoundingClientRect(); return r.width < 48 || r.height < 48; });
      const unlabeled = interactive.filter(el => !((el.innerText || '').trim() || el.getAttribute('aria-label') || el.getAttribute('aria-labelledby') || el.getAttribute('title')));
      const textNodes = [...document.querySelectorAll('p,h1,h2,h3,button,.choice,.panel')];
      const clippedText = textNodes.filter(el => el.scrollHeight > el.clientHeight + 1);
      const focusRules = [...document.querySelectorAll('style')].some(s => /:focus-visible/.test(s.textContent || ''));
      const html = document.documentElement.outerHTML;
      return {
        horizontalOverflow: document.documentElement.scrollWidth > window.innerWidth + 1,
        text: document.body.innerText.length,
        brokenImages: [...document.images].filter(i => !i.complete || i.naturalWidth === 0).length,
        smallTargets: smallTargets.length,
        unlabeledControls: unlabeled.length,
        clippedText: clippedText.length,
        hasSkipLink: Boolean(document.querySelector('a[href="#main"]')),
        hasLiveRegion: Boolean(document.querySelector('[aria-live]')),
        hasNavLabel: Boolean(document.querySelector('[aria-label="Prototype navigation"]')),
        hasFocusVisible: focusRules,
        hasReducedMotion: /prefers-reduced-motion/.test(html),
        hasThemeState: document.querySelector('[data-theme]') !== null || html.includes('data-theme'),
        hasRtl: /dir=|RTL/.test(html),
        hasViewportMeta: Boolean(document.querySelector('meta[name="viewport"][content*="viewport-fit=cover"]')),
        visibleInteractiveCount: visible.length
      };
    });
    const pass = Boolean(response?.ok()) && !metrics.horizontalOverflow && metrics.text > 0 && metrics.brokenImages === 0 && metrics.smallTargets === 0 && metrics.unlabeledControls === 0 && metrics.clippedText === 0 && metrics.hasSkipLink && metrics.hasLiveRegion && metrics.hasNavLabel && metrics.hasFocusVisible && metrics.hasReducedMotion && metrics.hasThemeState && metrics.hasRtl && metrics.hasViewportMeta && consoleErrors.length === 0 && pageErrors.length === 0 && failedRequests.length === 0;
    if (!pass) failures += 1;
    results.push({ file, viewport: vp.name, pass, ...metrics, consoleErrors, pageErrors, failedRequests });
    await context.close();
  }
}

const artworkResults = [];
for (const asset of requiredArtwork) {
  const context = await browser.newContext({ deviceScaleFactor: 1 });
  const page = await context.newPage({ viewport: { width: 360, height: 800 } });
  const response = await page.goto(`http://127.0.0.1:4173/${asset}`, { waitUntil: 'networkidle' });
  const brokenImages = await page.evaluate(() => [...document.images].filter(i => !i.complete || i.naturalWidth === 0).length);
  const pass = Boolean(response?.ok()) && brokenImages === 0;
  if (!pass) failures += 1;
  artworkResults.push({ asset, pass, httpStatus: response?.status() ?? null, brokenImages });
  await context.close();
}

await browser.close();
fs.mkdirSync('artifacts/visual-regression', { recursive: true });
const manifest = { gate: 'V15', generatedAt: new Date().toISOString(), pages, viewports, requiredArtwork, results, artworkResults, failures };
fs.writeFileSync('artifacts/visual-regression/v15-closure.json', JSON.stringify(manifest, null, 2));

if (results.length !== pages.length * viewports.length) throw new Error('Incomplete V15 page/viewport matrix');
if (results.some(r => !r.pass)) throw new Error(`V15 page/viewport failures: ${results.filter(r => !r.pass).length}`);
if (artworkResults.some(r => !r.pass)) throw new Error(`V15 artwork failures: ${artworkResults.filter(r => !r.pass).length}`);
if (failures !== 0) throw new Error(`V15 failures=${failures}`);
console.log(`V15 VISUAL CLOSURE PASS: ${results.length} page/viewport checks + ${artworkResults.length} artwork checks`);
