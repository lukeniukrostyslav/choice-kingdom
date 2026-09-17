from tools.audit_p6_choice_catalog_coverage import build_report


def test_p6_catalog_family_audit_covers_frozen_production_catalog():
    report = build_report()
    assert report["events"] == 272
    assert report["choices"] >= report["events"] * 2
    assert report["two_way_events"] > 0
    assert report["three_plus_way_events"] > 0
    assert report["resource_delta_choices"] > 0
    assert report["relationship_delta_choices"] > 0
    assert report["state_token_choices"] > 0
    assert report["triggered_events"] > 0


def test_p6_catalog_family_audit_is_deterministic():
    assert build_report() == build_report()
