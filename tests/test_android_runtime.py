from pathlib import Path

from runtime.android_runtime import start

ROOT = Path(__file__).resolve().parents[1]


def test_android_runtime_starts_from_canonical_session_and_round_trips_choice():
    runtime = start(str(ROOT), "android-adapter-test")

    first = runtime.snapshot_json()
    assert '"schema_version":1' in first
    assert '"event_id":"E01-A"' in first
    assert '"run_id":"android-adapter-test"' in first

    second = runtime.choose("E01-A-C1")
    assert '"schema_version":1' in second
    assert '"event_id":"E01-A"' not in second or '"turn":2' in second
