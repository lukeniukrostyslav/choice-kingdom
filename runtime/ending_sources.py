from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet, Iterable


@dataclass(frozen=True)
class SourceClosedEndingFacts:
    """Deterministic compilation of authored source facts into derived predicates.

    This layer intentionally accepts only canonical state namespaces and explicit
    evidence-family inputs. It never infers an ending, promotes relationships to
    institutional evidence, or treats a consumer event as a producer.
    """

    predicates: FrozenSet[str]


class EndingSourceContractError(ValueError):
    pass


class EndingSourceCompiler:
    @staticmethod
    def compile(
        *,
        flags: Iterable[str] = (),
        history: Iterable[str] = (),
        threads: Iterable[str] = (),
        systemic_evidence_families: Iterable[str] = (),
        coalition_participants: Iterable[str] = (),
        unresolved_coalition_blockers: Iterable[str] = (),
        unresolved_mandatory_crisis_blockers: Iterable[str] = (),
    ) -> SourceClosedEndingFacts:
        flags_set = frozenset(flags)
        history_set = frozenset(history)
        threads_set = frozenset(threads)
        evidence = frozenset(systemic_evidence_families)
        participants = frozenset(coalition_participants)
        coalition_blockers = frozenset(unresolved_coalition_blockers)
        mandatory_blockers = frozenset(unresolved_mandatory_crisis_blockers)

        predicates: set[str] = set()

        # Constitutional preparation: at least three distinct authored domains.
        domains = {
            "civic" if "people_charter_endorsed" in flags_set else None,
            "institutional" if {"crown_audited", "full_crown_audit_published"} & flags_set else None,
            "factional" if "history.house_assembly" in history_set else None,
            "military" if {"military_red_line"} & flags_set or "thread.military_constitutional" in threads_set else None,
        }
        domains.discard(None)
        if len(domains) >= 3:
            predicates.add("pred.constitutional_prepared_strong")

        # Budget reform: all three documented producer facts are required.
        if {"auditor_independence", "crown_audited", "legislative_budget_lock"} <= flags_set:
            predicates.add("pred.budget_reform")

        # Systemic explanation: three independent families plus explicit E270-A
        # convergence. The convergence token alone is never sufficient.
        required_evidence = {
            "warehouse_or_financial",
            "document_or_language",
            "witness_or_organizational",
        }
        if required_evidence <= evidence and "systemic_explanation_convergence" in flags_set:
            predicates.add("pred.systemic_explanation_verified")

        # Coalition cooperation is sourced by the positive coalition route and
        # requires canonical participant identity plus no unresolved blocker.
        if (
            "history.cross_faction_package" in history_set
            and participants
            and not coalition_blockers
        ):
            predicates.add("pred.coalition_cooperation")

        # Final charter is a consumer-only derived gate. It requires all authored
        # upstream domains and an explicit blocker check; E209/E210 cannot create it.
        charter_upstream = {
            "people_charter_endorsed" in flags_set,
            bool({"crown_audited", "full_crown_audit_published"} & flags_set),
            "history.house_assembly" in history_set and "history.guild_representation" in history_set,
            bool({"military_red_line"} & flags_set) or "thread.military_constitutional" in threads_set,
            "pred.systemic_explanation_verified" in predicates,
            "pred.coalition_cooperation" in predicates,
        }
        if all(charter_upstream) and not mandatory_blockers:
            predicates.add("pred.final_charter_prerequisites")

        return SourceClosedEndingFacts(frozenset(predicates))
