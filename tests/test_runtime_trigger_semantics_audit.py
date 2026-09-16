from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_runtime_trigger_semantics_audit_is_deterministic() -> None:
    command = [sys.executable, "tools/audit_runtime_trigger_semantics.py"]
    first = subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)
    second = subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)
    assert first.stdout == second.stdout
    report = json.loads((ROOT / "docs/MACHINE_RUNTIME_TRIGGER_SEMANTICS_AUDIT_01.json").read_text())
    assert report["scope"] == "E01-E272"
    assert report["audit_only"] is True
    assert report["opaque_or_partial_count"] == 154
    assert sum(report["counts"].values()) == 272
