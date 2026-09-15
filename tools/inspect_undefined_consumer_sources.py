#!/usr/bin/env python3
"""Classify undefined inventory consumers by locating authoritative authored occurrences."""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
inv = json.loads((ROOT / "scenario-source-inventory.json").read_text(encoding="utf-8"))
manifest = json.loads((ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json").read_text(encoding="utf-8"))
heading_re = re.compile(r"^### (E\d{2,3}) — (.+)$", re.M)
choice_re = re.compile(r"(?:^|\n)\s*(?:-\s*)?\*\*([AB])\s*(?:—|:|-)(.*)", re.M)
undefined = inv["undefined_consumers"]
results = {}
for token in undefined:
    hits = []
    for source in manifest["source_of_truth"]["catalog_sources"]:
        text = (ROOT / source).read_text(encoding="utf-8")
        matches = list(heading_re.finditer(text))
        for i, m in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            block = text[m.start():end]
            if token not in block:
                continue
            trigger = re.search(r"^\*\*Trigger:\*\* (.*)$", block, re.M)
            trigger_hit = bool(trigger and token in trigger.group(1))
            choices = []
            for cm in choice_re.finditer(block):
                if token in cm.group(0):
                    choices.append(cm.group(1))
            hits.append({"event": m.group(1), "source": source, "trigger_hit": trigger_hit, "choice_hits": choices})
    results[token] = hits

out = ROOT / "undefined-consumer-source-inspection.json"
out.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"undefined_consumers={len(undefined)}")
print(f"tokens_with_authored_occurrences={sum(bool(v) for v in results.values())}")
for token, hits in results.items():
    if hits:
        print(f"{token}: " + "; ".join(f"{h['event']}:{'trigger' if h['trigger_hit'] else ''}{'choice=' + ','.join(h['choice_hits']) if h['choice_hits'] else ''}" for h in hits[:12]))
    else:
        print(f"{token}: NO_AUTHORED_OCCURRENCE")
