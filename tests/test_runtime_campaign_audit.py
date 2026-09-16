from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_runtime_campaign_audit_is_deterministic_and_non_promotional():
    result = subprocess.run(
        [sys.executable, "tools/audit_runtime_campaign.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    report = json.loads((ROOT / "docs/MACHINE_RUNTIME_CAMPAIGN_AUDIT_01.json").read_text())
    assert report["audit_only"] is True
    assert report["scope"] == "E01-E272"
    assert report["execution_errors"] == []
    assert report["visited_event_count"] == 61
    assert report["missing_event_count"] == 211
    assert report["visited_events"][0] == "E01"
    assert report["visited_events"][-1] == "E230"
    assert "unresolved prose predicates" in report["semantic_boundary"]
