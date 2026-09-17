from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "web-preview" / "game-flow.html"
text = HTML.read_text(encoding="utf-8")

required = [
    'id="event"', 'id="consequence"', 'id="investigation"', 'id="realm"',
    'id="characters"', 'id="history"', 'id="ending"', 'id="settings"',
    'localStorage.getItem(\'ck-state\')', 'prefers-reduced-motion',
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

print("Choice Kingdom design preview smoke check: PASS")
print(f"Primary screens: {text.count('<section id=')}")
print("State continuity markers: PASS")
print("Accessibility markers: PASS")
print("Reduced-motion marker: PASS")
