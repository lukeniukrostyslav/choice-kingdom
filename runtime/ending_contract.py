from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet, Iterable

# These are the only ending-relevant derived predicates that the canonical graph
# currently declares.  This module deliberately does not infer new predicates
# from route names, relationships, or arbitrary flags.
CANONICAL_ENDING_PREDICATES: FrozenSet[str] = frozenset(
    {
        "pred.border_crisis",
        "pred.food_stable",
        "pred.guild_influence_strong",
        "pred.systemic_explanation_verified",
        "pred.coalition_cooperation",
        "pred.constitutional_prepared_strong",
        "pred.budget_reform",
        "pred.final_charter_prerequisites",
        "pred.market_pressure",
        "pred.winter_severe",
        "pred.transport_disruption",
        "pred.border_tension",
    }
)

CANONICAL_ENDING_HISTORY = frozenset(
    {
        "history.guild_logistics_cooperation",
        "history.guild_representation",
        "history.cross_faction_package",
        "history.house_assembly",
    }
)

CANONICAL_ENDING_THREADS = frozenset(
    {
        "thread.military_constitutional",
        "thread.final_constitutional_phase",
        "thread.endgame_convergence",
    }
)

CANONICAL_ENDING_FLAGS = frozenset(
    {
        "people_charter_endorsed",
        "guild_political_representation",
        "constitution_first",
        "crown_powers_first",
        "emergency_power",
        "constitutional_limit",
        "systemic_explanation_convergence",
        "four_way_bargain",
        "negotiated_withdrawal",
        "public_infrastructure_trust",
        "military_red_line",
    }
)


class EndingContractError(ValueError):
    """Raised when ending qualification input is outside the canonical vocabulary."""


@dataclass(frozen=True)
class EndingQualification:
    """Machine-readable ending qualification supplied by an authored producer.

    The contract validates vocabulary and namespace boundaries only.  It does not
    manufacture a predicate from a similarly named history/thread/flag token.
    """

    positive_endings: FrozenSet[str] = frozenset()
    predicates: FrozenSet[str] = frozenset()
    history: FrozenSet[str] = frozenset()
    threads: FrozenSet[str] = frozenset()
    flags: FrozenSet[str] = frozenset()
    collapse_failure: bool = False
    explicit_withdrawal: bool = False

    @classmethod
    def build(
        cls,
        *,
        positive_endings: Iterable[str] = (),
        predicates: Iterable[str] = (),
        history: Iterable[str] = (),
        threads: Iterable[str] = (),
        flags: Iterable[str] = (),
        collapse_failure: bool = False,
        explicit_withdrawal: bool = False,
    ) -> "EndingQualification":
        predicate_set = frozenset(predicates)
        history_set = frozenset(history)
        thread_set = frozenset(threads)
        flag_set = frozenset(flags)

        unknown_predicates = predicate_set - CANONICAL_ENDING_PREDICATES
        unknown_history = history_set - CANONICAL_ENDING_HISTORY
        unknown_threads = thread_set - CANONICAL_ENDING_THREADS
        unknown_flags = flag_set - CANONICAL_ENDING_FLAGS
        errors: list[str] = []
        if unknown_predicates:
            errors.append("non-canonical ending predicate: " + ", ".join(sorted(unknown_predicates)))
        if unknown_history:
            errors.append("non-canonical ending history: " + ", ".join(sorted(unknown_history)))
        if unknown_threads:
            errors.append("non-canonical ending thread: " + ", ".join(sorted(unknown_threads)))
        if unknown_flags:
            errors.append("non-canonical ending flag: " + ", ".join(sorted(unknown_flags)))
        if "systemic_explanation_verified" in flag_set:
            errors.append("unscoped systemic_explanation_verified cannot satisfy a pred.* prerequisite")
        if "coalition_cooperation" in flag_set:
            errors.append("unscoped coalition_cooperation cannot satisfy a pred.* prerequisite")
        if errors:
            raise EndingContractError("; ".join(errors))

        return cls(
            positive_endings=frozenset(positive_endings),
            predicates=predicate_set,
            history=history_set,
            threads=thread_set,
            flags=flag_set,
            collapse_failure=collapse_failure,
            explicit_withdrawal=explicit_withdrawal,
        )
