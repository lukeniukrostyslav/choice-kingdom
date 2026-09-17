from pathlib import Path

from runtime.catalog import AuthoredCatalog

ROOT = Path(__file__).resolve().parents[1]


def _catalog() -> AuthoredCatalog:
    catalog = AuthoredCatalog.from_repository(ROOT)
    catalog.validate()
    return catalog


def _choice_tokens(catalog: AuthoredCatalog, event_id: str, choice_id: str) -> set[str]:
    choice = next(choice for choice in catalog.get(event_id).choices if choice.choice_id == choice_id)
    return set(choice.state_tokens)


def test_budget_reform_producers_are_authored_and_distinct() -> None:
    catalog = _catalog()
    assert "auditor_independence" in _choice_tokens(catalog, "E142", "E142-A")
    assert "crown_audited" in _choice_tokens(catalog, "E154", "E154-A")
    assert "legislative_budget_lock" in _choice_tokens(catalog, "E198", "E198-A")


def test_final_charter_consumes_prerequisites_without_manufacturing_them() -> None:
    catalog = _catalog()
    assert "crown_audited" in _choice_tokens(catalog, "E154", "E154-A")
    assert "full_crown_audit_published" in _choice_tokens(catalog, "E155", "E155-A")
    assert "house_assembly" in _choice_tokens(catalog, "E161", "E161-A")
    assert "military_red_line" in _choice_tokens(catalog, "E199", "E199-A")
    assert "systemic_explanation_convergence" in _choice_tokens(catalog, "E270", "E270-A")
    assert catalog.get("E209").trigger == "pred.final_charter_prerequisites"
    assert "pred.final_charter_prerequisites" not in _choice_tokens(catalog, "E209", "E209-A")
    assert "pred.final_charter_prerequisites" not in _choice_tokens(catalog, "E210", "E210-A")


def test_audit_variants_are_one_constitutional_domain() -> None:
    catalog = _catalog()
    assert "crown_audited" in _choice_tokens(catalog, "E154", "E154-A")
    assert "full_crown_audit_published" in _choice_tokens(catalog, "E155", "E155-A")
    assert "crown_audited" not in _choice_tokens(catalog, "E155", "E155-A")
