#!/usr/bin/env python3
"""Final executable scenario gate for S11-S13."""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def run(args: list[str]) -> tuple[bool, str]:
    result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    return result.returncode == 0, result.stdout + result.stderr

def main() -> int:
    checks = []
    ok, output = run([sys.executable, "tools/validate_causal_reachability_contract.py"])
    report_path = ROOT / "docs/MACHINE_CAUSAL_REACHABILITY_01.json"
    report = json.loads(report_path.read_text(encoding="utf-8")) if report_path.exists() else {}
    checks.append({"id":"S12.graph_integrity","status":"PASS" if ok else "FAIL","causal_edges":report.get("causal_edge_count"),"causal_nodes":report.get("causal_node_count"),"unreachable_causal_nodes":report.get("causal_nodes_unreachable_from_structural_root")})
    ok_tests, test_output = run([sys.executable, "-m", "pytest", "-q", "tests/test_replay_meta_runtime.py", "tests/test_scenario_final_gate.py", "tests/test_ending_resolver.py", "tests/test_ending_qa_p01_p30_runtime.py"])
    checks.append({"id":"S11.replay_and_S13.ending_runtime","status":"PASS" if ok_tests else "FAIL","test_output_tail":test_output[-1200:]})
    full_ok, full_output = run([sys.executable, "-m", "pytest", "-q"])
    checks.append({"id":"S13.full_regression","status":"PASS" if full_ok else "FAIL","test_output_tail":full_output[-1200:]})
    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    result = {"schema_version":"1.0","contract":"choice_kingdom.final_scenario_runtime_gate","scope":"E01-E272","status":status,"blocks":{"S11":"100%" if checks[1]["status"]=="PASS" else "BLOCKED","S12":"100%" if checks[0]["status"]=="PASS" else "BLOCKED","S13":"100%" if checks[2]["status"]=="PASS" else "BLOCKED"},"checks":checks,"closure_boundary":["S11 proves runtime replay reset/import isolation for canonical meta.* state.","S12 proves frozen graph integrity and rooted structural reachability; it does not claim every conditional gameplay path is feasible.","S13 proves the current executable Python scenario regression surface is green, including ending resolution and persistence.","Android UI, physical-device QA, APK/AAB and store release remain later product gates."]}
    (ROOT/"docs/MACHINE_FINAL_SCENARIO_RUNTIME_GATE_01.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"status":status,"blocks":result["blocks"]},indent=2,sort_keys=True))
    return 0 if status == "PASS" else 1
if __name__ == "__main__": raise SystemExit(main())
