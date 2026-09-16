#!/usr/bin/env python3
"""Validate the presentation-neutral production session boundary."""
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from runtime.session import GameSession


def main() -> int:
    session = GameSession.new(ROOT, "boundary-check")
    assert session.view().event_id == "E01"
    assert session.available_choices() == ("E01-A", "E01-B")
    session.choose("E01-A")
    assert session.state.turn == 2
    assert "E02" in session.available_events()
    session.select_event("E02")
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "save.json"
        session.save(path)
        restored = GameSession.load(ROOT, path)
        assert restored.state.snapshot() == session.state.snapshot()
        assert restored.snapshot_digest() == session.snapshot_digest()
    print("RUNTIME SESSION BOUNDARY: PASS")
    print(f"events={len(session.engine.catalog.events)}")
    print(f"current_event={session.state.current_event_id}")
    print(f"turn={session.state.turn}")
    print(f"available_events={len(session.available_events())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
