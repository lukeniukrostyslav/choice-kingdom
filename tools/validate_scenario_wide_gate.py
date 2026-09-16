#!/usr/bin/env python3
"""Validate the scenario-wide source/contract integration gate for E01-E272.

This gate deliberately does not promote runtime gameplay readiness. It proves that
frozen scenario scope, canonical graph/reachability, replay meta-state, delayed
lifecycle, and ending contracts agree at the source/contract boundary. Runtime
Decision Engine execution remains a separate downstream gate.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"
CAUSAL = ROOT / "docs/MACHINE_CAUSAL_REACHABILITY_01.json"
REPLAY = ROOT / "docs/MACHINE_REPLAY_CONTRACT_01.json"
DELAY = ROOT / "docs/MACHINE_DELAY_CONTRACT_01.json"
ENDING = ROOT / "docs/MACHINE_ENDING_QUALIFICATION_01.json"
PRECEDENCE = ROOT / "docs/MACHINE_ENDING_PRECEDENCE_01.json"
OUT = ROOT / "docs/MACHINE_SCENARIO_WIDE_GATE_01.json"

EXPECTED = {f"E{i:02d}" for i in range(1, 273)}
EXCLUDED = {f"E{i:02d}" for i in range(273, 278)}
REPLAY_EVENTS = {"E186", "E247", "E248"}
DELAY_EVENTS = {f"E{i:02d}" for i in range(181, 186)} | {f"E{i:02d}" for i in range(242, 247)}


def load(path: Path):
    if not path.exists():
        raise FileNotFoundError(str(path))
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    checks: dict[str, str] = {}

    try:
        graph = load(GRAPH)
        scope = graph.get("scope", {})
        if scope.get("first_event") != "E01" or scope.get("last_event") != "E272":
            errors.append("canonical graph scope drift")
        if set(scope.get("excluded_events", [])) != EXCLUDED:
            errors.append("canonical graph excluded-event boundary drift")
        nodes = graph.get("nodes", [])
        node_ids = {n.get("event_id") for n in nodes if isinstance(n, dict)}
        if EXPECTED - node_ids:
            errors.append("canonical graph missing frozen events")
        if EXCLUDED & node_ids:
            errors.append("excluded expansion events leaked into canonical graph")
        checks["canonical_scope"] = "PASS" if not errors else "FAIL"
    except Exception as exc:
        errors.append(f"canonical graph unreadable: {exc}")
        checks["canonical_scope"] = "FAIL"

    try:
        causal = load(CAUSAL)
        ok = (
            causal.get("scope") == "E01-E272"
            and causal.get("source_level_causal_reachability_closed") is True
            and (causal.get("causal_nodes_unreachable_from_structural_root") in (0, [], None))
        )
        if not ok:
            errors.append("source-level causal reachability is not closed")
        checks["causal_reachability"] = "PASS" if ok else "FAIL"
    except Exception as exc:
        errors.append(f"causal report unreadable: {exc}")
        checks["causal_reachability"] = "FAIL"

    try:
        replay = load(REPLAY)
        contracts = {c.get("event_id"): c for c in replay.get("contracts", [])}
        if set(contracts) != REPLAY_EVENTS:
            errors.append("replay contract event surface drift")
        for event_id in REPLAY_EVENTS:
            c = contracts.get(event_id, {})
            if not str(c.get("canonical_meta_key", "")).startswith("meta.replay."):
                errors.append(f"{event_id}: non-canonical replay meta key")
            if c.get("producer_scope") != "completed_prior_run_meta_export":
                errors.append(f"{event_id}: replay producer boundary drift")
            if c.get("exactly_once_import") is not True:
                errors.append(f"{event_id}: exactly-once replay import not enforced")
            if not c.get("reset"):
                errors.append(f"{event_id}: replay reset rule missing")
        checks["replay_meta_state"] = "PASS" if not errors else "FAIL"
    except Exception as exc:
        errors.append(f"replay contract unreadable: {exc}")
        checks["replay_meta_state"] = "FAIL"

    try:
        delay = load(DELAY)
        entries = delay.get("contracts", delay.get("callbacks", []))
        ids = {c.get("event_id") for c in entries if isinstance(c, dict)}
        if not DELAY_EVENTS <= ids:
            errors.append("frozen delayed lifecycle surface is incomplete")
        checks["delayed_lifecycle"] = "PASS" if DELAY_EVENTS <= ids else "FAIL"
    except Exception as exc:
        errors.append(f"delayed lifecycle contract unreadable: {exc}")
        checks["delayed_lifecycle"] = "FAIL"

    for name, path in (("ending_qualification", ENDING), ("ending_precedence", PRECEDENCE)):
        try:
            data = load(path)
            if not data:
                raise ValueError("empty contract")
            checks[name] = "PASS"
        except Exception as exc:
            errors.append(f"{name} contract unreadable: {exc}")
            checks[name] = "FAIL"

    runtime_blocks = {
        "decision_engine_execution": False,
        "fresh_run_gameplay_reachability": False,
        "replay_gameplay_reachability": False,
        "runtime_ending_resolution": False,
        "save_load_gameplay_equivalence": False,
    }
    result = {
        "schema_version": "1.0",
        "contract": "choice-kingdom.scenario-wide-gate",
        "scope": "E01-E272",
        "excluded_events": sorted(EXCLUDED),
        "source_contract_gate": "PASS" if not errors else "FAIL",
        "checks": checks,
        "replay_meta_events": sorted(REPLAY_EVENTS),
        "delayed_lifecycle_events": sorted(DELAY_EVENTS),
        "runtime_blocks": runtime_blocks,
        "decision_engine_promotion_authorized": False,
        "errors": errors,
        "boundary": "Source/contract integration GREEN does not claim runtime gameplay completion. Decision Engine remains downstream until runtime gates are implemented and verified.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"source_contract_gate": result["source_contract_gate"], "errors": len(errors), "decision_engine_promotion_authorized": False}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
