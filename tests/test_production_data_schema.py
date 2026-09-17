from pathlib import Path

from runtime.catalog import AuthoredCatalog
from runtime.state import EXCLUDED_EVENTS, RELATIONSHIPS, RESOURCES
from tools.validate_production_data_schema import EXPECTED

ROOT = Path(__file__).resolve().parents[1]


def test_production_schema_matches_frozen_scope_and_canonical_vocabulary() -> None:
    catalog = AuthoredCatalog.from_repository(ROOT)
    catalog.validate()
    assert set(catalog.events) == EXPECTED
    assert EXCLUDED_EVENTS == frozenset({"E273", "E274", "E275", "E276", "E277"})
    assert RESOURCES == ("gold", "trust", "security", "power", "reputation")
    assert RELATIONSHIPS == ("mara", "rowan", "seris", "ivo", "amara", "toma")


def test_production_schema_choice_identity_is_canonical_for_every_authored_choice() -> None:
    catalog = AuthoredCatalog.from_repository(ROOT)
    for event_id, event in catalog.events.items():
        for choice in event.choices:
            assert choice.choice_id == f"{event_id}-{choice.label}"
            assert choice.label == choice.label.upper()
            assert choice.text.strip()
            assert choice.body.strip()
            assert set(choice.resource_deltas).issubset(RESOURCES)
            assert set(choice.relationship_deltas).issubset(RELATIONSHIPS)


def test_production_schema_prerequisites_and_immediate_unlocks_stay_in_scope() -> None:
    catalog = AuthoredCatalog.from_repository(ROOT)
    for event_id in EXPECTED:
        assert all(prerequisite in EXPECTED for prerequisite in catalog.authored_prerequisites(event_id))
        for choice in catalog.get(event_id).choices:
            import re
            unlocks = re.findall(r"^-\s*\*\*Unlocks?\*\*\s+`?(E\d{2,3})", choice.body, re.I | re.M)
            assert set(unlocks).issubset(EXPECTED)
