from runtime.localization_contract import build_locale_contract


def test_locale_contract_covers_frozen_production_surface(repo_root):
    contract = build_locale_contract(repo_root)
    assert contract["event_count"] == 272
    assert contract["choice_count"] == 520
    assert contract["narrative_key_count"] == 272 * 2 + 520 * 2
    assert len(contract["locales"]) == 28
