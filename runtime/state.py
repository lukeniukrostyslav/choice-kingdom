from __future__ import annotations

from dataclasses import asdict, dataclass, field
import json
from pathlib import Path
from typing import Any

PRODUCTION_FIRST = 1
PRODUCTION_LAST = 272
EXCLUDED_EVENTS = frozenset({"E273", "E274", "E275", "E276", "E277"})
RESOURCES = ("gold", "trust", "security", "power", "reputation")
RELATIONSHIPS = ("mara", "rowan", "seris", "ivo", "amara", "toma")


@dataclass(frozen=True)
class PendingDelay:
    exactly_once_key: str
    source_event_id: str
    source_choice_id: str
    resolution_target: str
    scheduled_turn: int | None
    condition_bound: bool = False
    priority: int = 0
    status: str = "pending"
    supersedes: str | None = None

    def __post_init__(self) -> None:
        if self.source_event_id in EXCLUDED_EVENTS or self.resolution_target in EXCLUDED_EVENTS:
            raise ValueError("excluded event cannot enter runtime delay state")
        if self.status not in {"pending", "resolved", "cancelled", "superseded"}:
            raise ValueError("invalid delay status")
        if self.condition_bound and self.scheduled_turn is not None:
            raise ValueError("condition-bound delay must not invent a turn")


@dataclass
class GameState:
    run_id: str
    turn: int = 1
    current_event_id: str = "E01"
    resources: dict[str, int] = field(default_factory=lambda: {key: 50 for key in RESOURCES})
    relationships: dict[str, int] = field(default_factory=lambda: {key: 0 for key in RELATIONSHIPS})
    flags: set[str] = field(default_factory=set)
    history: set[str] = field(default_factory=set)
    threads: set[str] = field(default_factory=set)
    pending_delays: dict[str, PendingDelay] = field(default_factory=dict)
    imported_meta_keys: set[str] = field(default_factory=set)
    terminal: bool = False

    @classmethod
    def fresh(cls, run_id: str) -> "GameState":
        return cls(run_id=run_id)

    def apply_delta(self, resource: str, delta: int) -> None:
        if resource not in RESOURCES:
            raise ValueError(f"non-canonical resource: {resource}")
        self.resources[resource] = max(0, min(100, self.resources[resource] + delta))

    def set_relationship_delta(self, character: str, delta: int) -> None:
        if character not in RELATIONSHIPS:
            raise ValueError(f"non-canonical relationship: {character}")
        self.relationships[character] = max(-3, min(3, self.relationships[character] + delta))

    def schedule(self, delay: PendingDelay) -> None:
        existing = self.pending_delays.get(delay.exactly_once_key)
        if existing is not None:
            if existing.status == "pending":
                raise ValueError(f"duplicate pending delay: {delay.exactly_once_key}")
            raise ValueError(f"delay key already consumed: {delay.exactly_once_key}")
        if delay.supersedes is not None:
            prior = self.pending_delays.get(delay.supersedes)
            if prior is None:
                raise KeyError(f"superseded delay not found: {delay.supersedes}")
            if prior.status == "pending":
                self.pending_delays[delay.supersedes] = PendingDelay(**{**asdict(prior), "status": "superseded"})
            elif prior.status in {"resolved", "cancelled", "superseded"}:
                raise ValueError(f"cannot supersede consumed delay: {delay.supersedes}")
        self.pending_delays[delay.exactly_once_key] = delay

    def cancel_delay(self, exactly_once_key: str) -> PendingDelay:
        delay = self.pending_delays.get(exactly_once_key)
        if delay is None:
            raise KeyError(exactly_once_key)
        if delay.status != "pending":
            raise ValueError(f"delay is not pending: {exactly_once_key}")
        cancelled = PendingDelay(**{**asdict(delay), "status": "cancelled"})
        self.pending_delays[exactly_once_key] = cancelled
        return cancelled

    def supersede_delay(self, exactly_once_key: str, superseding_key: str) -> PendingDelay:
        delay = self.pending_delays.get(exactly_once_key)
        replacement = self.pending_delays.get(superseding_key)
        if delay is None or replacement is None:
            raise KeyError(exactly_once_key if delay is None else superseding_key)
        if delay.status != "pending":
            raise ValueError(f"delay is not pending: {exactly_once_key}")
        if replacement.status != "pending":
            raise ValueError(f"replacement delay is not pending: {superseding_key}")
        superseded = PendingDelay(**{**asdict(delay), "status": "superseded"})
        self.pending_delays[exactly_once_key] = superseded
        return superseded

    def resolve_delay(self, exactly_once_key: str) -> PendingDelay:
        delay = self.pending_delays.get(exactly_once_key)
        if delay is None:
            raise KeyError(exactly_once_key)
        if delay.status != "pending":
            raise ValueError(f"delay is not pending: {exactly_once_key}")
        resolved = PendingDelay(**{**asdict(delay), "status": "resolved"})
        self.pending_delays[exactly_once_key] = resolved
        return resolved

    def snapshot(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "run_id": self.run_id,
            "turn": self.turn,
            "current_event_id": self.current_event_id,
            "resources": dict(sorted(self.resources.items())),
            "relationships": dict(sorted(self.relationships.items())),
            "flags": sorted(self.flags),
            "history": sorted(self.history),
            "threads": sorted(self.threads),
            "pending_delays": {
                key: asdict(value) for key, value in sorted(self.pending_delays.items())
            },
            "imported_meta_keys": sorted(self.imported_meta_keys),
            "terminal": self.terminal,
        }

    @classmethod
    def from_snapshot(cls, payload: dict[str, Any]) -> "GameState":
        if payload.get("schema_version") != 1:
            raise ValueError("unsupported runtime save schema")
        if payload.get("current_event_id") in EXCLUDED_EVENTS:
            raise ValueError("excluded event cannot be restored as current production event")
        pending = {
            key: PendingDelay(**value) for key, value in payload.get("pending_delays", {}).items()
        }
        return cls(
            run_id=str(payload["run_id"]),
            turn=int(payload["turn"]),
            current_event_id=str(payload["current_event_id"]),
            resources={key: int(value) for key, value in payload["resources"].items()},
            relationships={key: int(value) for key, value in payload["relationships"].items()},
            flags=set(payload.get("flags", [])),
            history=set(payload.get("history", [])),
            threads=set(payload.get("threads", [])),
            pending_delays=pending,
            imported_meta_keys=set(payload.get("imported_meta_keys", [])),
            terminal=bool(payload.get("terminal", False)),
        )


class SaveStore:
    """Versioned local JSON persistence boundary for headless runtime tests."""

    @staticmethod
    def save(state: GameState, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(state.snapshot(), indent=2, sort_keys=True) + "\n", encoding="utf-8")

    @staticmethod
    def load(path: Path) -> GameState:
        return GameState.from_snapshot(json.loads(path.read_text(encoding="utf-8")))
