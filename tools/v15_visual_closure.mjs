import { chromium } from 'playwright';
import fs from 'node:fs';

const pages = [
  'index.html',
  'game-flow.html',
  'artwork-preview.html',
  'design-art-direction.html',
  'design-asset-production.html',
  'design-accessibility-final.html',
  'design-character-faction-final.html',
  'design-relationships-p13-premium.html',
  'design-investigation-p14-premium.html',
  'design-crisis-p15-premium.html',
  'design-ending-p16-premium.html',
  'design-replay-p17-premium.html',
  'design-navigation-p19-premium.html'
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

const p1AssetFiles = [
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
      const visible = interactive.filter(el => {
        const r = el.getBoundingClientRect();
        const style = getComputedStyle(el);
        return r.width > 0 && r.height > 0 && style.visibility !== 'hidden' && style.display !== 'none' && r.bottom >= 0 && r.right >= 0 && r.top <= window.innerHeight && r.left <= window.innerWidth;
      });
      const smallTargets = visible.filter(el => { const r = el.getBoundingClientRect(); return r.width < 48 || r.height < 48; });
      const unlabeled = interactive.filter(el => !((el.innerText || '').trim() || el.getAttribute('aria-label') || el.getAttribute('aria-labelledby') || el.getAttribute('title')));
      const textNodes = [...document.querySelectorAll('p,h1,h2,h3,button,.choice,.panel')];
      const clippedText = textNodes.filter(el => {
        const style = getComputedStyle(el);
        return (style.overflow === 'hidden' || style.overflow === 'clip' || style.overflowX === 'hidden' || style.overflowY === 'hidden') && el.scrollHeight > el.clientHeight + 1;
      });
      const focusRules = [...document.querySelectorAll('style')].some(s => /:focus-visible/.test(s.textContent || ''));
      const html = document.documentElement.outerHTML;
      const isAppFlow = location.pathname.endsWith('/game-flow.html');
      const isLauncher = location.pathname.endsWith('/index.html');
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
        visibleInteractiveCount: visible.length,
        pageType: isAppFlow ? 'app-flow' : isLauncher ? 'launcher' : 'design-surface'
      };
    });
    const commonPass = Boolean(response?.ok()) && !metrics.horizontalOverflow && metrics.text > 0 && metrics.brokenImages === 0 && metrics.smallTargets === 0 && metrics.unlabeledControls === 0 && metrics.clippedText === 0 && consoleErrors.length === 0 && pageErrors.length === 0 && failedRequests.length === 0;
    const appPass = metrics.pageType !== 'app-flow' || (metrics.hasSkipLink && metrics.hasLiveRegion && metrics.hasNavLabel && metrics.hasFocusVisible && metrics.hasReducedMotion && metrics.hasThemeState && metrics.hasRtl && metrics.hasViewportMeta);
    const launcherPass = metrics.pageType !== 'launcher' || (metrics.hasThemeState && metrics.hasViewportMeta);
    let p21Pass = true;
    if (file === 'design-accessibility-final.html') {
      p21Pass = await page.evaluate(() => {
        const large = document.querySelector('#largeToggle');
        const rtl = document.querySelector('#rtlToggle');
        const motion = document.querySelector('#motionToggle');
        if (!large || !rtl || !motion) return false;
        const before = getComputedStyle(document.documentElement).fontSize;
        large.click();
        const after = getComputedStyle(document.documentElement).fontSize;
        const largePass = large.getAttribute('aria-pressed') === 'true' && before !== after;
        rtl.click();
        const rtlPass = rtl.getAttribute('aria-pressed') === 'true' && document.documentElement.dir === 'rtl';
        rtl.click();
        const rtlResetPass = document.documentElement.dir === 'ltr';
        motion.click();
        const motionPass = motion.getAttribute('aria-pressed') === 'true' && document.documentElement.classList.contains('reduce-motion');
        return largePass && rtlPass && rtlResetPass && motionPass;
      });
    }
    let p19Pass = true;
    if (file === 'design-navigation-p19-premium.html') {
      p19Pass = await page.evaluate(() => {
        const nav = document.querySelector('#nav-content');
        const title = document.querySelector('#navigation-title');
        const context = document.querySelector('#navigation-context');
        const current = document.querySelector('[aria-current="page"]');
        const back = document.querySelector('.back');
        if (!nav || !title || !context || !current || !back) return false;
        if (nav.getAttribute('aria-labelledby') !== 'navigation-title') return false;
        if (nav.getAttribute('aria-describedby') !== 'navigation-context') return false;
        if (current.classList.contains('item') === false) return false;
        const backRect = back.getBoundingClientRect();
        if (backRect.height < 48 || backRect.width < 48) return false;
        const items = [...document.querySelectorAll('.item')];
        if (items.length < 6) return false;
        const heading = current.querySelector('h2');
        if (!heading) return false;
        const originalHeading = heading.textContent;
        heading.textContent = originalHeading.repeat(8);
        const longLabelSafe = current.scrollWidth <= current.clientWidth + 1;
        heading.textContent = originalHeading;
        return longLabelSafe && items.every(item => {
          const rect = item.getBoundingClientRect();
          return rect.width > 0 && rect.height >= 48;
        });
      });
    }
    let p1Pass = true;
    if (file === 'design-art-direction.html') {
      p1Pass = await page.evaluate(() => {
        const large = document.querySelector('#largeToggle');
        const rtl = document.querySelector('#rtlToggle');
        if (!large || !rtl || large.tagName !== 'BUTTON' || rtl.tagName !== 'BUTTON') return false;
        if (large.getAttribute('aria-pressed') !== 'false' || rtl.getAttribute('aria-pressed') !== 'false') return false;
        const main = document.querySelector('main');
        const before = getComputedStyle(main).fontSize;
        large.click();
        const after = getComputedStyle(main).fontSize;
        const largePass = main.classList.contains('large') && large.getAttribute('aria-pressed') === 'true' && before !== after;
        rtl.click();
        const rtlPass = main.classList.contains('rtl') && rtl.getAttribute('aria-pressed') === 'true' && document.documentElement.dir === 'rtl';
        rtl.click();
        const resetPass = !main.classList.contains('rtl') && document.documentElement.dir === 'ltr';
        return largePass && rtlPass && resetPass;
      });
    }
    const pass = commonPass && appPass && launcherPass && p1Pass && p21Pass && p19Pass;
    if (!pass) failures += 1;
    results.push({ file, viewport: vp.name, pass, p19Pass, p21Pass, ...metrics, consoleErrors, pageErrors, failedRequests });
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

const p1AssetAudit = [];
for (const asset of p1AssetFiles) {
  const context = await chromium.launch({ headless: true });
  const page = await context.newPage({ viewport: { width: 360, height: 800 } });
  const response = await page.goto(`http://127.0.0.1:4173/${asset}`, { waitUntil: 'networkidle' });
  const audit = await page.evaluate(() => {
    const svg = document.querySelector('svg');
    const title = svg?.querySelector('title');
    const desc = svg?.querySelector('desc');
    const viewBox = svg?.getAttribute('viewBox');
    return {
      svg: Boolean(svg),
      title: Boolean(title?.textContent?.trim()),
      desc: Boolean(desc?.textContent?.trim()),
      viewBox: Boolean(viewBox),
      textLength: document.body.innerText.trim().length
    };
  });
  const pass = Boolean(response?.ok()) && audit.svg && audit.title && audit.desc && audit.viewBox;
  if (!pass) failures += 1;
  p1AssetAudit.push({ asset, pass, httpStatus: response?.status() ?? null, ...audit });
  await context.close();
}

await browser.close();
fs.mkdirSync('artifacts/visual-regression', { recursive: true });
const manifest = { gate: 'V15', generatedAt: new Date().toISOString(), pages, viewports, requiredArtwork, results, artworkResults, p1AssetAudit, failures };
fs.writeFileSync('artifacts/visual-regression/v15-closure.json', JSON.stringify(manifest, null, 2));

for (const failure of results.filter(r => !r.pass)) console.error('V15_PAGE_FAILURE', JSON.stringify(failure));
for (const failure of artworkResults.filter(r => !r.pass)) console.error('V15_ARTWORK_FAILURE', JSON.stringify(failure));
for (const failure of p1AssetAudit.filter(r => !r.pass)) console.error('V15_P1_ASSET_AUDIT_FAILURE', JSON.stringify(failure));
if (results.length !== pages.length * viewports.length) throw new Error('Incomplete V15 page/viewport matrix');
if (results.some(r => !r.pass)) throw new Error(`V15 page/viewport failures: ${results.filter(r => !r.pass).length}`);
if (artworkResults.some(r => !r.pass)) throw new Error(`V15 artwork failures: ${artworkResults.filter(r => !r.pass).length}`);
if (p1AssetAudit.some(r => !r.pass)) throw new Error(`V15 P1 asset audit failures: ${p1AssetAudit.filter(r => !r.pass).length}`);
if (failures !== 0) throw new Error(`V15 failures=${failures}`);
console.log(`V15 VISUAL CLOSURE PASS: ${results.length} page/viewport checks + ${artworkResults.length} artwork checks`);