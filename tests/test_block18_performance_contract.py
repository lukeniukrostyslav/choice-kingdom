from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_block18_performance_contract_is_present() -> None:
    benchmark = ROOT / "tools" / "block18_performance_benchmark.py"
    workflow = ROOT / ".github" / "workflows" / "block18-performance.yml"
    doc = ROOT / "docs" / "BLOCK18_PERFORMANCE.md"
    assert benchmark.exists()
    assert workflow.exists()
    assert doc.exists()


def test_block18_benchmark_has_deterministic_budget_and_runtime_path() -> None:
    text = (ROOT / "tools" / "block18_performance_benchmark.py").read_text(encoding="utf-8")
    assert "perf_counter" in text
    assert "ITERATIONS" in text
    assert "MAX_SECONDS" in text
    assert "DecisionEngine" in text
    assert "GameState.fresh" in text
    assert "engine.execute" in text
