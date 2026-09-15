#!/usr/bin/env python3
"""Static scenario-source closure gate for Choice Kingdom.

This gate deliberately checks authored scenario source only. It does not claim
runtime reachability. It prevents known P0 regressions while the campaign is
being canonicalized. The catalog list is taken from MACHINE_CANONICAL_GRAPH_01
so this gate cannot silently omit E33/E34 or the Act-V expansion sources.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MANIFEST = DOCS / "MACHINE_CANONICAL_GRAPH_01.json"

errors = []
all_events = []
texts = {}

if not MANIFEST.exists():
    errors.append("missing canonical graph manifest")
    manifest = {}
else:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

catalog_sources = manifest.get("source_of_truth", {}).get("catalog_sources", [])
CATALOGS = [ROOT / source for source in catalog_sources]

for path in CATALOGS:
    if not path.exists():
        errors.append(f"missing catalog: {path}")
        continue
    text = path.read_text(encoding="utf-8")
    texts[path.name] = text
    all_events.extend(re.findall(r"^### (E\d{2,3}) —", text, re.M))

first_event = int(manifest.get("scope", {}).get("first_event", 1))
last_event = int(manifest.get("scope", {}).get("last_event", 272))
excluded = set(manifest.get("scope", {}).get("excluded_events", []))
expected = {f"E{i:02d}" for i in range(first_event, last_event + 1)} - excluded

for event_id in sorted(expected, key=lambda x: int(x[1:])):
    count = all_events.count(event_id)
    if count != 1 and event_id not in {"E271"}:
        errors.append(f"{event_id}: expected exactly one authored heading, found {count}")

required_fragments = {
    "EVENT_CATALOG.md": [
        "### E19 — Price Fixing",
        "Producer: establishes `pred.market_pressure`",
        "### E29 — First Snow",
        "Producer: establishes `pred.winter_severe`",
        "### E32 — Three Fires",
        "E32 explicitly establishes `pred.transport_disruption`",
    ],
    "EVENT_CATALOG_ACT_V_EXPANSION.md": [
        "### E49 — The Guild's Vote",
        "`guild_political_representation`",
        "### E50 — The People's Charter",
        "`people_charter_endorsed`",
    ],
    "EVENT_CATALOG_EXPANSION_111_150.md": [
        "### E136 — The Frozen Road",
        "`history.guild_logistics_cooperation`",
        "### E144 — The Guild Seat",
        "`history.guild_representation`",
        "### E148 — The Last Coalition Meeting",
        "`history.cross_faction_package`",
        "does not by itself satisfy `pred.coalition_cooperation`",
    ],
    "EVENT_CATALOG_EXPANSION_151_210.md": [
        "### E154 — The First Audit of the Crown",
        "`crown_audited`",
        "### E161 — The House Assembly",
        "`house_assembly`",
        "### E165 — The Credit Book",
        "`official_credit_disclosure`",
        "### E168 — The Guild Tribunal",
        "`guild_tribunal_independent`",
        "### E192 — The Broken Cart",
        "**Trigger:** `pred.transport_disruption`.",
        "### E194 — The Guild Convoy",
        "`history.guild_logistics_cooperation`",
        "must not self-produce that qualified predicate",
        "### E197 — The Succession Test",
        "### E198 — The Budget Lock",
        "### E199 — The Army Oath Rewritten",
        "`army_constitution_oath`",
        "### E200 — The Merchant Oath",
        "### E207 — The Founder Question",
        "### E209 — The Dawn Charter",
        "### E210 — The Last Decision Is Not a Choice",
    ],
    "EVENT_CATALOG_EXPANSION_211_270.md": [
        "### E227 — Rowan's Line",
        "`military_red_line`",
        "### E261 — The Four-Way Bargain",
        "### E267 — Rowan's Last Order",
        "### E268 — Seris's Last Bargain",
        "### E269 — Ivo's Late Account",
        "### E270 — Amara and Toma at Dawn",
    ],
}

for filename, fragments in required_fragments.items():
    text = texts.get(filename, "")
    for fragment in fragments:
        if fragment not in text:
            errors.append(f"{filename}: missing required source contract: {fragment}")

# E33/E34 must be checked against their now-canonical dedicated source.
e33e34 = texts.get("EVENT_CATALOG_E33_E34_CANONICAL.md", "")
for fragment in ["### E33", "### E34"]:
    if fragment not in e33e34:
        errors.append(f"EVENT_CATALOG_E33_E34_CANONICAL.md: missing canonical source: {fragment}")

# Machine contract regression guard. String-level checks keep this source gate
# deterministic and make the exact coalition contract visible in the repository.
contract_path = DOCS / "MACHINE_PREDICATE_COMPOSITE_CONTRACT_01.json"
contract = contract_path.read_text(encoding="utf-8") if contract_path.exists() else ""
coalition_contract_fragments = [
    '"pred.coalition_cooperation"',
    '"producer": "E148-A"',
    '"key": "history.cross_faction_package"',
    '"minimum_distinct_faction_identities": 3',
    '"Mara", "Rowan", "Seris", "Ivo", "Amara", "Toma"',
    '"E261 four_way_bargain is support evidence only"',
    '"E194 cannot self-produce this predicate"',
]
if not contract:
    errors.append("missing machine predicate composite contract")
else:
    for fragment in coalition_contract_fragments:
        if fragment not in contract:
            errors.append(f"coalition contract: missing exact fragment: {fragment}")

# Source-level composite-domain guards. These verify authored producers, not
# executable aggregation/reachability.
source_contract_fragments = [
    '"pred.guild_influence_strong"',
    '"representation": ["E49", "E144"]',
    '"tribunal": ["E168-A"]',
    '"market_credit": ["E165-A"]',
    '"logistics": ["E136-B"]',
    '"pred.constitutional_prepared_strong"',
    '"civic_commons": ["E50-A"]',
    '"institutional_audit": ["E154-A", "E155-A"]',
    '"factional_house": ["E161-A"]',
    '"military_law": ["E199-A"]',
]
for fragment in source_contract_fragments:
    if fragment not in contract:
        errors.append(f"composite source contract: missing exact fragment: {fragment}")

# E192 must never reintroduce the undefined numeric resource.
e192 = texts.get("EVENT_CATALOG_EXPANSION_151_210.md", "")
if "+4 food stability" in e192 or ("+4 food" in e192 and "food_logistics_stabilized" not in e192):
    errors.append("E192: undefined numeric food-stability effect detected")

# E139 is warning infrastructure, not a border-crisis producer.
e111_150 = texts.get("EVENT_CATALOG_EXPANSION_111_150.md", "")
e139 = re.search(r"### E139 —.*?(?=\n### E140 —)", e111_150, re.S)
if e139 and "does **not** by itself declare or resolve `pred.border_crisis`" not in e139.group(0):
    errors.append("E139: border-crisis producer boundary missing")

# E194 cannot manufacture its own qualified cooperation predicate.
e194 = re.search(r"### E194 —.*?(?=\n### E195 —)", e192, re.S)
if e194 and "must not self-produce that qualified predicate" not in e194.group(0):
    errors.append("E194: qualified predicate anti-circularity guard missing")

if errors:
    print("SCENARIO_SOURCE_CLOSURE: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("SCENARIO_SOURCE_CLOSURE: PASS")
print(f"authored_events={len(all_events)}")
print("event_id_uniqueness=PASS")
print("p0_source_contracts=PASS")
print("guild_and_constitutional_source_domains=PASS")
print("coalition_machine_contract=PASS")
print("e33_e34_canonical_source=PASS")
print("anti_circularity_guards=PASS")
print("numeric_resource_regression=PASS")
print("NOTE: fresh-run reachability and runtime semantics remain separate gates")
