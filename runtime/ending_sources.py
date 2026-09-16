from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, FrozenSet, Iterable

if TYPE_CHECKING:
    from .state import GameState


CANONICAL_COALITION_PARTICIPANTS = frozenset({
    "mara",
    "rowan",
    "seris",
    "ivo",
    "amara",
    "toma",
})
COALITION_MIN_DISTINCT_PARTICIPANTS = 3
COALITION_POSITIVE_OUTCOME_MARKER = "coalition_candidate_package"


@dataclass(frozen=True)
class SourceClosedEndingFacts:
    """Deterministic compilation of authored source facts into derived predicates."""

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

        # E192-B is the sole source-closed producer of the current food-stability
        # cycle; E192-A clears it. Keep this typed marker in the same compiler used
        # by runtime trigger evaluation instead of maintaining a second special case.
        if "food_logistics_stabilized" in flags_set and "food_logistics_unstable" not in flags_set:
            predicates.add("pred.food_stable")

        domains = {
            "civic" if "people_charter_endorsed" in flags_set else None,
            "institutional" if {"crown_audited", "full_crown_audit_published"} & flags_set else None,
            "factional" if "history.house_assembly" in history_set else None,
            # E199-A is the canonical military-law producer for this domain.
            # `military_red_line` is later supporting constitutional-stress evidence
            # and must not silently substitute for the authored oath decision.
            "military" if "army_constitution_oath" in flags_set else None,
        }
        domains.discard(None)
        if len(domains) >= 3:
            predicates.add("pred.constitutional_prepared_strong")

        if {"auditor_independence", "crown_audited", "legislative_budget_lock"} <= flags_set:
            predicates.add("pred.budget_reform")

        required_evidence = {
            "warehouse_or_financial",
            "document_or_language",
            "witness_or_organizational",
        }
        if required_evidence <= evidence and "systemic_explanation_convergence" in flags_set:
            predicates.add("pred.systemic_explanation_verified")

        canonical_participants = participants & CANONICAL_COALITION_PARTICIPANTS
        if (
            COALITION_POSITIVE_OUTCOME_MARKER in flags_set
            and "history.cross_faction_package" in history_set
            and len(canonical_participants) >= COALITION_MIN_DISTINCT_PARTICIPANTS
            and not coalition_blockers
        ):
            predicates.add("pred.coalition_cooperation")

        # Guild influence requires three distinct authored domains. Relationship
        # values and generic guild history are intentionally not accepted as domains.
        guild_domains = {
            "representation" if "history.guild_representation" in history_set else None,
            "tribunal" if "guild_tribunal_independent" in flags_set else None,
            "commercial_market" if {"audited_monopoly", "merchant_charter"} & flags_set else None,
            "qualified_logistics"
            if (
                "history.guild_logistics_cooperation" in history_set
                and "guild_neutral_inspectors" in flags_set
                and "guild_logistics_immunity_risk" not in flags_set
            )
            else None,
        }
        guild_domains.discard(None)
        if len(guild_domains) >= 3:
            predicates.add("pred.guild_influence_strong")

        charter_upstream = {
            "people_charter_endorsed" in flags_set,
            bool({"crown_audited", "full_crown_audit_published"} & flags_set),
            "history.house_assembly" in history_set and "history.guild_representation" in history_set,
            "army_constitution_oath" in flags_set,
            "pred.systemic_explanation_verified" in predicates,
            "pred.coalition_cooperation" in predicates,
        }
        if all(charter_upstream) and not mandatory_blockers:
            predicates.add("pred.final_charter_prerequisites")

        return SourceClosedEndingFacts(frozenset(predicates))

    @staticmethod
    def compile_state(state: "GameState") -> SourceClosedEndingFacts:
        """Compile only canonical ending facts already recorded on a live GameState.

        No relationship score, route name, stale alias, or consumer event is promoted
        into an ending prerequisite. The state owns evidence and blocker lifecycle;
        this compiler only derives the documented predicates from those facts.
        """
        return EndingSourceCompiler.compile(
            flags=state.flags,
            history=state.history,
            threads=state.threads,
            systemic_evidence_families=state.ending_evidence_families,
            coalition_participants=state.coalition_participants,
            unresolved_coalition_blockers=state.unresolved_coalition_blockers,
            unresolved_mandatory_crisis_blockers=state.unresolved_mandatory_crisis_blockers,
        )
