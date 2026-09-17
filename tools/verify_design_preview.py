from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "web-preview" / "game-flow.html"
text = HTML.read_text(encoding="utf-8")

required = [
    'id="event"', 'id="consequence"', 'id="investigation"', 'id="realm"',
    'id="characters"', 'id="history"', 'id="ending"', 'id="settings"',
    "localStorage.getItem('ck-state')", 'prefers-reduced-motion',
    'aria-live', 'data-theme', 'data-choice="granary"',
    'data-choice="guild"', 'data-choice="ration"',
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("Missing design-preview contract markers:\n- " + "\n- ".join(missing))

if not re.search(r'<a[^>]+class=["\'][^"\']*\bskip\b[^"\']*["\'][^>]+href=["\']#main["\']', text):
    raise SystemExit("Missing accessible skip-to-content link")

ids = re.findall(r'\bid=["\']([^"\']+)["\']', text)
duplicates = sorted({x for x in ids if ids.count(x) > 1})
if duplicates:
    raise SystemExit("Duplicate HTML ids: " + ", ".join(duplicates))

if text.count('<section id=') < 8:
    raise SystemExit("Expected all primary visual screens to exist")

assets = [
    'artwork/event-empty-granary.svg',
    'artwork/queen-elira.svg',
    'artwork/lord-cael.svg',
    'artwork/river-compact.svg',
    'artwork/ending-chronicle.svg',
]
missing_assets = [a for a in assets if not (ROOT / 'web-preview' / a).is_file()]
if missing_assets:
    raise SystemExit("Missing authored visual assets:\n- " + "\n- ".join(missing_assets))

refs = re.findall(r'(?:src|href)=["\'](artwork/[^"\']+)["\']', text)
broken_refs = sorted(set(r for r in refs if not (ROOT / 'web-preview' / r).is_file()))
if broken_refs:
    raise SystemExit("Broken local artwork references:\n- " + "\n- ".join(broken_refs))

if 'min-height:48px' not in text or 'min-height:56px' not in text:
    raise SystemExit("Interactive target sizing contract is not explicit for navigation/choices")

if 'aria-label="Prototype navigation"' not in text:
    raise SystemExit("Primary navigation accessibility label missing")

print("Choice Kingdom design preview smoke check: PASS")
print(f"Primary screens: {text.count('<section id=')}")
print(f"Authored assets: {len(assets)}")
print(f"Artwork references checked: {len(set(refs))}")
print("State continuity markers: PASS")
print("Accessibility markers: PASS")
print("Interactive target contract: PASS")
print("Reduced-motion marker: PASS")
