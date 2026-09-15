#!/usr/bin/env python3
"""Static scenario-source closure gate for Choice Kingdom.

This gate deliberately checks authored scenario source only. It does not claim
runtime reachability. It prevents known P0 regressions while the campaign is
being canonicalized.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CATALOGS = [
    DOCS / "EVENT_CATALOG.md",
    DOCS / "EVENT_EXPANSION_071_110.md",
    DOCS / "EVENT_CATALOG_EXPANSION_111_150.md",
    DOCS / "EVENT_CATALOG_EXPANSION_151_210.md",
    DOCS / "EVENT_CATALOG_EXPANSION_211_270.md",
]

errors = []
all_events = []
texts = {}
for path in CATALOGS:
    if not path.exists():
        errors.append(f"missing catalog: {path}")
        continue
    text = path.read_text(encoding="utf-8")
    texts[path.name] = text
    all_events.extend(re.findall(r"^### (E\d{2,3}) —", text, re.M))

# Every production event ID must exist exactly once across the authored catalogs.
for event_id in [f"E{i:02d}" for i in range(1, 271)]:
    count = all_events.count(event_id)
    if count != 1:
        errors.append(f"{event_id}: expected exactly one authored heading, found {count}")

# Known source-level P0 contracts.
required_fragments = {
    "EVENT_CATALOG.md": [
        "### E19 — Price Fixing",
        "Producer: establishes `pred.market_pressure`",
        "### E29 — First Snow",
        "Producer: establishes `pred.winter_severe`",
        "### E32 — Three Fires",
        "E32 explicitly establishes `pred.transport_disruption`",
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
        "### E168 — The Guild Tribunal",
        "`guild_tribunal_independent`",
        "### E192 — The Broken Cart",
        "**Trigger:** `pred.transport_disruption`.",
        "### E194 — The Guild Convoy",
        "`history.guild_logistics_cooperation`",
        "must not self-produce that qualified predicate",
        "### E197 — The Succession Test",
        "### E200 — The Merchant Oath",
        "### E207 — The Founder Question",
        "### E209 — The Dawn Charter",
        "### E210 — Last Decision Is Not a Choice",
    ],
    "EVENT_CATALOG_EXPANSION_211_270.md": [
        "### E261 — The Four-Way Bargain",
        "### E267",
        "### E268",
        "### E269",
        "### E270",
    ],
}

for filename, fragments in required_fragments.items():
    text = texts.get(filename, "")
    for fragment in fragments:
        if fragment not in text:
            errors.append(f"{filename}: missing required source contract: {fragment}")

# Machine contract regression guard: coalition qualification must have one
# explicit producer/key and an independently checked participant threshold.
contract_path = DOCS / "MACHINE_PREDICATE_COMPOSITE_CONTRACT_01.json"
if not contract_path.exists():
    errors.append("missing machine predicate composite contract")
else:
    try:
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        coalition = contract["predicates"]["pred.coalition_cooperation"]
        if coalition.get("producer") != "E148-A":
            errors.append("coalition contract: producer must remain E148-A")
        if coalition.get("key") != "history.cross_faction_package":
            errors.append("coalition contract: canonical key mismatch")
        if coalition.get("minimum_distinct_faction_identities") != 3:
            errors.append("coalition contract: minimum distinct faction threshold must be 3")
        participants = coalition.get("participant_identities", [])
        expected = {"Mara", "Rowan", "Seris", "Ivo", "Amara", "Toma"}
        if set(participants) != expected:
            errors.append("coalition contract: participant identity set mismatch")
        if "E261 four_way_bargain is support evidence only" not in coalition.get("non_alias_rules", []):
            errors.append("coalition contract: E261 support-only boundary missing")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"coalition contract: invalid machine contract: {exc}")

# Regression guard: E192 must never reintroduce the undefined numeric resource.
e192 = texts.get("EVENT_CATALOG_EXPANSION_151_210.md", "")
if "+4 food stability" in e192 or "+4 food" in e192 and "food_logistics_stabilized" not in e192:
    errors.append("E192: undefined numeric food-stability effect detected")

# Regression guard: E139 is warning infrastructure, not a border-crisis producer.
e111_150 = texts.get("EVENT_CATALOG_EXPANSION_111_150.md", "")
e139 = re.search(r"### E139 —.*?(?=\n### E140 —)", e111_150, re.S)
if e139 and "does **not** by itself declare or resolve `pred.border_crisis`" not in e139.group(0):
    errors.append("E139: border-crisis producer boundary missing")

# Regression guard: E194 cannot manufacture its own qualified cooperation predicate.
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
print("coalition_machine_contract=PASS")
print("anti_circularity_guards=PASS")
print("numeric_resource_regression=PASS")
print("NOTE: fresh-run reachability and runtime semantics remain separate gates")
