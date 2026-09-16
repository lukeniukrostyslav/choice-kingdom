from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from .state import GameState

END_STEWARD = "END_STEWARD"
END_IRON_CROWN = "END_IRON_CROWN"
END_GOLDEN_COMPACT = "END_GOLDEN_COMPACT"
END_PEOPLES_CHARTER = "END_PEOPLES_CHARTER"
END_BROKEN_DIADEM = "END_BROKEN_DIADEM"
END_QUIET_THRONE = "END_QUIET_THRONE"
END_SECOND_FOUNDER = "END_SECOND_FOUNDER"

ENDING_IDS = frozenset(
    {
        END_STEWARD,
        END_IRON_CROWN,
        END_GOLDEN_COMPACT,
        END_PEOPLES_CHARTER,
        END_BROKEN_DIADEM,
        END_QUIET_THRONE,
        END_SECOND_FOUNDER,
    }
)
POSITIVE_ENDINGS = frozenset(
    {
        END_STEWARD,
        END_IRON_CROWN,
        END_GOLDEN_COMPACT,
        END_PEOPLES_CHARTER,
        END_SECOND_FOUNDER,
    }
)


class EndingResolutionError(ValueError):
    """Raised when an ending cannot be resolved without inventing authored semantics."""


@dataclass(frozen=True)
class EndingResolution:
    ending_id: str
    qualified_positive_endings: tuple[str, ...]
    failure: bool
    withdrawal: bool


class EndingResolver:
    """Deterministic ending boundary; predicate production remains outside this consumer."""

    SAVE_SCHEMA_VERSION = 1

    def resolve(
        self,
        state: GameState,
        *,
        qualified_endings: Sequence[str] = (),
        collapse_failure: bool = False,
        explicit_withdrawal: bool = False,
        authored_priority: Mapping[tuple[str, str], str] | None = None,
    ) -> EndingResolution:
        self._validate_terminal_boundary(state)
        qualified = self._canonical_positive_set(qualified_endings)
        priority = authored_priority or {}
        candidates_for_priority = set(qualified)
        if explicit_withdrawal:
            candidates_for_priority.add(END_QUIET_THRONE)
        self._validate_priority_table(priority, candidates_for_priority)

        if collapse_failure:
            winner = END_BROKEN_DIADEM
        elif explicit_withdrawal:
            winner = self._select_by_authored_priority(candidates_for_priority, priority)
        elif not qualified:
            raise EndingResolutionError("no ending qualifies and no authored fallback exists")
        else:
            winner = self._select_by_authored_priority(set(qualified), priority)

        self._record_immutable_identity(state, winner)
        return EndingResolution(
            ending_id=winner,
            qualified_positive_endings=tuple(sorted(qualified)),
            failure=collapse_failure,
            withdrawal=explicit_withdrawal,
        )

    def _validate_terminal_boundary(self, state: GameState) -> None:
        if not state.terminal:
            raise EndingResolutionError("ending resolution requires terminal runtime state")
        if state.snapshot().get("schema_version") != self.SAVE_SCHEMA_VERSION:
            raise EndingResolutionError("unsupported runtime save schema for ending resolution")

    @staticmethod
    def _canonical_positive_set(ending_ids: Sequence[str]) -> set[str]:
        values = set(ending_ids)
        unknown = values - POSITIVE_ENDINGS
        if unknown:
            raise EndingResolutionError(
                "non-canonical positive ending id: " + ", ".join(sorted(unknown))
            )
        return values

    @staticmethod
    def _validate_priority_table(
        priority: Mapping[tuple[str, str], str], candidates: set[str]
    ) -> None:
        for (left, right), winner in priority.items():
            if left not in ENDING_IDS or right not in ENDING_IDS or left == right:
                raise EndingResolutionError(f"invalid authored priority pair: {(left, right)!r}")
            if winner not in {left, right}:
                raise EndingResolutionError(
                    f"priority winner must be one of the pair: {(left, right)!r} -> {winner!r}"
                )

        if len(candidates) <= 1:
            return
        ordered = sorted(candidates)
        for index, left in enumerate(ordered):
            for right in ordered[index + 1 :]:
                if (left, right) not in priority and (right, left) not in priority:
                    raise EndingResolutionError(
                        f"missing authored priority for simultaneous endings: {left} × {right}"
                    )

    @staticmethod
    def _select_by_authored_priority(
        candidates: set[str], priority: Mapping[tuple[str, str], str]
    ) -> str:
        if not candidates:
            raise EndingResolutionError("no ending candidates")
        if len(candidates) == 1:
            return next(iter(candidates))

        remaining = set(candidates)
        ordered = sorted(candidates)
        for index, left in enumerate(ordered):
            for right in ordered[index + 1 :]:
                if left not in remaining or right not in remaining:
                    continue
                winner = priority.get((left, right), priority.get((right, left)))
                if winner is None:
                    raise EndingResolutionError(
                        f"missing authored priority for simultaneous endings: {left} × {right}"
                    )
                remaining.discard(right if winner == left else left)
        if len(remaining) != 1:
            raise EndingResolutionError(
                "authored priority does not produce one deterministic winner: "
                + ", ".join(sorted(remaining))
            )
        return next(iter(remaining))

    @staticmethod
    def _record_immutable_identity(state: GameState, ending_id: str) -> None:
        try:
            state.set_ending_identity(ending_id)
        except ValueError as exc:
            raise EndingResolutionError(str(exc)) from exc
