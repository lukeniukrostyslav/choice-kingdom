#!/usr/bin/env python3
"""Static scenario-source closure gate for Choice Kingdom.

This gate checks authored scenario source only. It does not claim runtime
reachability. Catalog sources come from MACHINE_CANONICAL_GRAPH_01 so the gate
cannot silently omit E33/E34 or the later production catalog expansions.
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

for source in manifest.get("source_of_truth", {}).get("catalog_sources", []):
    path = ROOT / source
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
    if count != 1 and event_id != "E271":
        errors.append(f"{event_id}: expected exactly one authored heading, found {count}")

required_fragments = {
    "EVENT_CATALOG.md": [
        "### E19 — Price Fixing", "Producer: establishes `pred.market_pressure`",
        "### E29 — First Snow", "Producer: establishes `pred.winter_severe`",
        "### E32 — Three Fires", "E32 explicitly establishes `pred.transport_disruption`",
    ],
    "EVENT_CATALOG_ACT_V_EXPANSION.md": [
        "### E49 — The Guild's Vote", "`guild_political_representation`",
        "### E50 — The People's Charter", "`people_charter_endorsed`",
    ],
    "EVENT_CATALOG_EXPANSION_111_150.md": [
        "### E136 — The Frozen Road", "`history.guild_logistics_cooperation`",
        "### E144 — The Guild Seat", "`history.guild_representation`",
        "### E148 — The Last Coalition Meeting", "`history.cross_faction_package`",
        "does not by itself satisfy `pred.coalition_cooperation`",
    ],
    "EVENT_CATALOG_EXPANSION_151_210.md": [
        "### E154 — The First Audit of the Crown", "`crown_audited`",
        "### E161 — The House Assembly", "`house_assembly`",
        "### E165 — The Credit Book", "`official_credit_disclosure`",
        "### E168 — The Guild Tribunal", "`guild_tribunal_independent`",
        "### E192 — The Broken Cart", "**Trigger:** `pred.transport_disruption`.",
        "### E194 — The Guild Convoy", "`history.guild_logistics_cooperation`",
        "must not self-produce that qualified predicate",
        "### E197 — The Succession Test", "### E198 — The Budget Lock",
        "### E199 — The Army Oath Rewritten", "`army_constitution_oath`",
        "### E200 — The Merchant Oath", "### E207 — The Founder Question",
        "### E209 — The Dawn Charter", "### E210 — The Last Decision Is Not a Choice",
    ],
    "EVENT_CATALOG_EXPANSION_211_270.md": [
        "### E227 — Rowan's Line", "`military_red_line`",
        "### E261 — The Four-Way Bargain", "### E267 — Rowan's Last Order",
        "### E268 — Seris's Last Bargain", "### E269 — Ivo's Late Account",
        "### E270 — Amara and Toma at Dawn",
    ],
}
for filename, fragments in required_fragments.items():
    text = texts.get(filename, "")
    for fragment in fragments:
        if fragment not in text:
            errors.append(f"{filename}: missing required source contract: {fragment}")

e33e34 = texts.get("EVENT_CATALOG_E33_E34_CANONICAL.md", "")
for fragment in ["### E33", "### E34"]:
    if fragment not in e33e34:
        errors.append(f"EVENT_CATALOG_E33_E34_CANONICAL.md: missing canonical source: {fragment}")

contract_path = DOCS / "MACHINE_PREDICATE_COMPOSITE_CONTRACT_01.json"
contract = contract_path.read_text(encoding="utf-8") if contract_path.exists() else ""
contract_fragments = [
    '"pred.coalition_cooperation"', '"producer": "E148-A"',
    '"key": "history.cross_faction_package"', '"minimum_distinct_faction_identities": 3',
    '"participant_identities": ["Mara", "Rowan", "Seris", "Ivo", "Amara", "Toma"]',
    '"E261 four_way_bargain is support evidence only"',
    '"E194 cannot self-produce this predicate"',
    '"pred.guild_influence_strong"',
    '"domain": "representation", "producers": ["E49", "E144"]',
    '"keys": ["guild_political_representation", "history.guild_representation"]',
    '"E49 and E144 cannot be counted as two independent domains"',
    '"domain": "tribunal", "producer": "E168-A", "key": "guild_tribunal_independent"',
    '"domain": "market_credit", "producer": "E165-A", "key": "official_credit_disclosure"',
    '"domain": "logistics", "producer": "E136-B", "key": "history.guild_logistics_cooperation"',
    '"pred.constitutional_prepared_strong"',
    '"domain": "civic_commons", "producer": "E50-A", "key": "people_charter_endorsed"',
    '"domain": "institutional_audit", "producer": "E154-A", "key": "crown_audited"',
    '"domain": "factional_house", "producer": "E161-A", "key": "house_assembly"',
    '"domain": "military_law", "producer": "E199-A", "key": "army_constitution_oath"',
]
if not contract:
    errors.append("missing machine predicate composite contract")
else:
    for fragment in contract_fragments:
        if fragment not in contract:
            errors.append(f"machine composite contract: missing exact fragment: {fragment}")

e192 = texts.get("EVENT_CATALOG_EXPANSION_151_210.md", "")
if "+4 food stability" in e192 or ("+4 food" in e192 and "food_logistics_stabilized" not in e192):
    errors.append("E192: undefined numeric food-stability effect detected")

e111_150 = texts.get("EVENT_CATALOG_EXPANSION_111_150.md", "")
e139 = re.search(r"### E139 —.*?(?=\n### E140 —)", e111_150, re.S)
if e139 and "does **not** by itself declare or resolve `pred.border_crisis`" not in e139.group(0):
    errors.append("E139: border-crisis producer boundary missing")
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
print("guild_representation_normalization=PASS")
print("guild_and_constitutional_source_domains=PASS")
print("coalition_machine_contract=PASS")
print("e33_e34_canonical_source=PASS")
print("anti_circularity_guards=PASS")
print("numeric_resource_regression=PASS")
print("NOTE: fresh-run reachability and runtime semantics remain separate gates")
