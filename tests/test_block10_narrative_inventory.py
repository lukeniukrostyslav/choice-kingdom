from runtime.narrative_inventory import build_narrative_key_inventory


def test_production_narrative_inventory_matches_frozen_catalog(repo_root):
    inventory = build_narrative_key_inventory(repo_root)
    assert inventory["event_count"] == 272
    assert inventory["choice_count"] == 520
    assert inventory["events"][0]["event_id"] == "E01"
    assert inventory["events"][-1]["event_id"] == "E272"
