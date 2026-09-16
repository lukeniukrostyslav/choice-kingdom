import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_contract() -> dict:
    return json.loads(
        (ROOT / "docs" / "MACHINE_BUDGET_REFORM_CONTRACT_01.json").read_text(
            encoding="utf-8"
        )
    )


def test_budget_reform_has_exact_three_independent_authored_domains():
    contract = load_contract()
    domains = contract["independent_domains"]
    assert [item["event"] for item in domains] == ["E142-A", "E154-A", "E198-A"]
    assert [item["domain"] for item in domains] == [
        "audit_independence",
        "crown_audit",
        "legislative_budget_control",
    ]
    assert len({item["domain"] for item in domains}) == 3
    assert contract["required_combination"] == "all_three_independent_domains"


def test_budget_reform_negative_branches_and_downstream_evidence_cannot_qualify():
    contract = load_contract()
    assert contract["negative_branches"] == [
        "E142-B-auditor_crown_control",
        "E154-B-crown_exempt_from_audit",
        "E198-B-executive_budget_override_retained",
    ]
    assert contract["downstream_only"] == ["E155-full_crown_audit_published"]
    assert contract["consumer"] == "E258"
    assert contract["consumer_cannot_manufacture"] is True


def test_budget_reform_runtime_gate_is_not_claimed_prematurely():
    contract = load_contract()
    assert contract["runtime_verified"] is False
    assert set(contract["remaining_checks"]) == {
        "producer_before_consumer_ordering",
        "producer_reachability",
        "negative_branch_exclusion",
        "no_retroactive_prerequisite_creation",
        "save_replay_preservation",
        "contradiction_and_cycle_checks",
    }
