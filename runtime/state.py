from __future__ import annotations

from dataclasses import asdict, dataclass, field
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any

PRODUCTION_FIRST = 1
PRODUCTION_LAST = 272
EXCLUDED_EVENTS = frozenset({"E273", "E274", "E275", "E276", "E277"})
RESOURCES = ("gold", "trust", "security", "power", "reputation")
RELATIONSHIPS = ("mara", "rowan", "seris", "ivo", "amara", "toma")
CANONICAL_COALITION_PARTICIPANTS = frozenset(RELATIONSHIPS)
REPLAY_META_KEYS = frozenset({
    "meta.replay.warehouse_investigation_unlock",
    "meta.replay.second_run_information_route",
    "meta.replay.callback_forgotten_favor",
})
REPLAY_EXPORT_SCHEMA = 1
RUNTIME_SAVE_FORMAT_VERSION = 2
RUNTIME_SNAPSHOT_SCHEMA = 1
ENDING_IDS = frozenset({
    "END_STEWARD",
    "END_IRON_CROWN",
    "END_GOLDEN_COMPACT",
    "END_PEOPLES_CHARTER",
    "END_BROKEN_DIADEM",
    "END_QUIET_THRONE",
    "END_SECOND_FOUNDER",
})
ENDING_EVIDENCE_FAMILIES = frozenset({
    "warehouse_or_financial",
    "document_or_language",
    "witness_or_organizational",
})


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
    activated_delayed_targets: set[str] = field(default_factory=set)
    imported_meta_keys: set[str] = field(default_factory=set)
    ending_evidence_families: set[str] = field(default_factory=set)
    coalition_participants: set[str] = field(default_factory=set)
    unresolved_coalition_blockers: set[str] = field(default_factory=set)
    unresolved_mandatory_crisis_blockers: set[str] = field(default_factory=set)
    terminal: bool = False
    ending_identity: str | None = None

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

    def record_ending_evidence(self, family: str) -> bool:
        if family not in ENDING_EVIDENCE_FAMILIES:
            raise ValueError(f"non-canonical ending evidence family: {family}")
        if family in self.ending_evidence_families:
            return False
        self.ending_evidence_families.add(family)
        return True

    def record_coalition_participant(self, participant: str) -> bool:
        if participant not in CANONICAL_COALITION_PARTICIPANTS:
            raise ValueError(f"non-canonical coalition participant: {participant!r}")
        if participant in self.coalition_participants:
            return False
        self.coalition_participants.add(participant)
        return True

    def set_coalition_blocker(self, blocker: str, unresolved: bool = True) -> None:
        if not isinstance(blocker, str) or not blocker:
            raise ValueError("coalition blocker identity must be a non-empty canonical string")
        if unresolved:
            self.unresolved_coalition_blockers.add(blocker)
        else:
            self.unresolved_coalition_blockers.discard(blocker)

    def set_mandatory_crisis_blocker(self, blocker: str, unresolved: bool = True) -> None:
        if not isinstance(blocker, str) or not blocker:
            raise ValueError("mandatory crisis blocker identity must be a non-empty canonical string")
        if unresolved:
            self.unresolved_mandatory_crisis_blockers.add(blocker)
        else:
            self.unresolved_mandatory_crisis_blockers.discard(blocker)

    def record_replay_meta(self, key: str) -> bool:
        if key not in REPLAY_META_KEYS:
            raise ValueError(f"non-canonical replay meta key: {key}")
        if key in self.imported_meta_keys:
            return False
        self.imported_meta_keys.add(key)
        return True

    def export_completed_run_meta(self) -> dict[str, Any]:
        if not self.terminal:
            raise ValueError("replay metadata can only be exported from a completed run")
        return {
            "schema_version": REPLAY_EXPORT_SCHEMA,
            "run_id": self.run_id,
            "completed": True,
            "meta_keys": sorted(self.imported_meta_keys),
        }

    @classmethod
    def new_run_from_completed_prior(
        cls, run_id: str, prior_export: dict[str, Any] | None = None
    ) -> "GameState":
        state = cls.fresh(run_id)
        if prior_export is None:
            return state
        if prior_export.get("schema_version") != REPLAY_EXPORT_SCHEMA:
            raise ValueError("unsupported replay export schema")
        if prior_export.get("completed") is not True:
            raise ValueError("prior replay export is not a completed run")
        prior_run_id = prior_export.get("run_id")
        if not isinstance(prior_run_id, str) or not prior_run_id:
            raise ValueError("replay export is missing prior run identity")
        for key in prior_export.get("meta_keys", []):
            if key in REPLAY_META_KEYS:
                state.record_replay_meta(key)
        return state

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

    def activate_delayed_target(self, exactly_once_key: str) -> PendingDelay:
        delay = self.pending_delays.get(exactly_once_key)
        if delay is None:
            raise KeyError(exactly_once_key)
        if delay.status != "pending":
            raise ValueError(f"delay is not pending: {exactly_once_key}")
        self.current_event_id = delay.resolution_target
        self.activated_delayed_targets.add(delay.resolution_target)
        return self.resolve_delay(exactly_once_key)

    def set_ending_identity(self, ending_id: str) -> None:
        if ending_id not in ENDING_IDS:
            raise ValueError(f"non-canonical ending identity: {ending_id}")
        if not self.terminal:
            raise ValueError("ending identity requires terminal runtime state")
        if self.ending_identity is not None and self.ending_identity != ending_id:
            raise ValueError("ending identity is immutable")
        self.ending_identity = ending_id

    def snapshot(self) -> dict[str, Any]:
        return {
            "schema_version": RUNTIME_SNAPSHOT_SCHEMA,
            "run_id": self.run_id,
            "turn": self.turn,
            "current_event_id": self.current_event_id,
            "resources": dict(sorted(self.resources.items())),
            "relationships": dict(sorted(self.relationships.items())),
            "flags": sorted(self.flags),
            "history": sorted(self.history),
            "threads": sorted(self.threads),
            "pending_delays": {key: asdict(value) for key, value in sorted(self.pending_delays.items())},
            "activated_delayed_targets": sorted(self.activated_delayed_targets),
            "imported_meta_keys": sorted(self.imported_meta_keys),
            "ending_evidence_families": sorted(self.ending_evidence_families),
            "coalition_participants": sorted(self.coalition_participants),
            "unresolved_coalition_blockers": sorted(self.unresolved_coalition_blockers),
            "unresolved_mandatory_crisis_blockers": sorted(self.unresolved_mandatory_crisis_blockers),
            "terminal": self.terminal,
            "ending_identity": self.ending_identity,
        }

    @classmethod
    def from_snapshot(cls, payload: dict[str, Any]) -> "GameState":
        if not isinstance(payload, dict):
            raise ValueError("runtime snapshot must be an object")
        if payload.get("schema_version") != RUNTIME_SNAPSHOT_SCHEMA:
            raise ValueError("unsupported runtime save schema")
        run_id = payload.get("run_id")
        if not isinstance(run_id, str) or not run_id:
            raise ValueError("runtime snapshot is missing run identity")
        turn = payload.get("turn")
        if not isinstance(turn, int) or isinstance(turn, bool) or turn < 1:
            raise ValueError("runtime snapshot has invalid turn")
        current_event = payload.get("current_event_id")
        if not isinstance(current_event, str) or not re.fullmatch(r"E\d{2,3}", current_event):
            raise ValueError("runtime snapshot has invalid current event identity")
        if current_event in EXCLUDED_EVENTS or not (
            PRODUCTION_FIRST <= int(current_event[1:]) <= PRODUCTION_LAST
        ):
            raise ValueError("excluded or non-production event cannot be restored")
        resources = payload.get("resources")
        relationships = payload.get("relationships")
        if not isinstance(resources, dict) or set(resources) != set(RESOURCES):
            raise ValueError("runtime snapshot has non-canonical resource set")
        if not all(isinstance(v, int) and not isinstance(v, bool) and 0 <= v <= 100 for v in resources.values()):
            raise ValueError("runtime snapshot has invalid resource value")
        if not isinstance(relationships, dict) or set(relationships) != set(RELATIONSHIPS):
            raise ValueError("runtime snapshot has non-canonical relationship set")
        if not all(isinstance(v, int) and not isinstance(v, bool) and -3 <= v <= 3 for v in relationships.values()):
            raise ValueError("runtime snapshot has invalid relationship value")
        pending_payload = payload.get("pending_delays", {})
        if not isinstance(pending_payload, dict):
            raise ValueError("runtime snapshot has invalid pending delay map")
        if any(key != value.get("exactly_once_key") for key, value in pending_payload.items() if isinstance(value, dict)):
            raise ValueError("runtime snapshot delay key mismatch")
        if any(not isinstance(value, dict) for value in pending_payload.values()):
            raise ValueError("runtime snapshot has invalid pending delay record")
        imported_meta = set(payload.get("imported_meta_keys", []))
        if not imported_meta.issubset(REPLAY_META_KEYS):
            raise ValueError("snapshot contains non-canonical replay meta key")
        evidence = set(payload.get("ending_evidence_families", []))
        if not evidence.issubset(ENDING_EVIDENCE_FAMILIES):
            raise ValueError("snapshot contains non-canonical ending evidence family")
        participants = set(payload.get("coalition_participants", []))
        if not participants.issubset(CANONICAL_COALITION_PARTICIPANTS):
            raise ValueError("snapshot contains non-canonical coalition participant")
        terminal = payload.get("terminal", False)
        if not isinstance(terminal, bool):
            raise ValueError("runtime snapshot has invalid terminal flag")
        ending_identity = payload.get("ending_identity")
        if ending_identity is not None and ending_identity not in ENDING_IDS:
            raise ValueError("snapshot contains non-canonical ending identity")
        if ending_identity is not None and terminal is not True:
            raise ValueError("non-terminal snapshot cannot contain ending identity")
        for collection_key in (
            "flags",
            "history",
            "threads",
            "activated_delayed_targets",
            "unresolved_coalition_blockers",
            "unresolved_mandatory_crisis_blockers",
        ):
            values = payload.get(collection_key, [])
            if not isinstance(values, list) or not all(isinstance(value, str) and value for value in values):
                raise ValueError(f"runtime snapshot has invalid {collection_key}")
        pending = {key: PendingDelay(**value) for key, value in pending_payload.items()}
        return cls(
            run_id=run_id,
            turn=turn,
            current_event_id=current_event,
            resources={key: int(value) for key, value in resources.items()},
            relationships={key: int(value) for key, value in relationships.items()},
            flags=set(payload.get("flags", [])),
            history=set(payload.get("history", [])),
            threads=set(payload.get("threads", [])),
            pending_delays=pending,
            activated_delayed_targets=set(payload.get("activated_delayed_targets", [])),
            imported_meta_keys=imported_meta,
            ending_evidence_families=evidence,
            coalition_participants=participants,
            unresolved_coalition_blockers=set(payload.get("unresolved_coalition_blockers", [])),
            unresolved_mandatory_crisis_blockers=set(payload.get("unresolved_mandatory_crisis_blockers", [])),
            terminal=terminal,
            ending_identity=ending_identity,
        )


class SaveStore:
    """Versioned local persistence with atomic replacement and integrity checking.

    The on-disk format is an envelope around the canonical snapshot. Legacy raw
    schema-v1 snapshots remain readable so existing saves are not stranded.
    """

    @staticmethod
    def _digest(snapshot: dict[str, Any]) -> str:
        canonical = json.dumps(
            snapshot, separators=(",", ":"), sort_keys=True, ensure_ascii=False
        ).encode("utf-8")
        return hashlib.sha256(canonical).hexdigest()

    @classmethod
    def snapshot_digest(cls, state: GameState) -> str:
        return cls._digest(state.snapshot())

    @classmethod
    def save(cls, state: GameState, path: Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        snapshot = state.snapshot()
        envelope = {
            "format_version": RUNTIME_SAVE_FORMAT_VERSION,
            "snapshot": snapshot,
            "snapshot_sha256": cls._digest(snapshot),
        }
        payload = json.dumps(
            envelope, indent=2, sort_keys=True, ensure_ascii=False
        ) + "\n"
        temp = path.with_name(f".{path.name}.tmp")
        backup = path.with_name(f"{path.name}.bak")
        temp.write_text(payload, encoding="utf-8")
        with temp.open("rb") as handle:
            os.fsync(handle.fileno())
        if path.exists():
            os.replace(path, backup)
        os.replace(temp, path)

    @classmethod
    def _read(cls, path: Path) -> GameState:
        payload = json.loads(path.read_text(encoding="utf-8"))
        # Legacy raw snapshot compatibility.
        if isinstance(payload, dict) and "snapshot" not in payload:
            return GameState.from_snapshot(payload)
        if not isinstance(payload, dict) or payload.get("format_version") != RUNTIME_SAVE_FORMAT_VERSION:
            raise ValueError("unsupported runtime save format")
        snapshot = payload.get("snapshot")
        if not isinstance(snapshot, dict):
            raise ValueError("runtime save is missing snapshot")
        expected = payload.get("snapshot_sha256")
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
            raise ValueError("runtime save integrity digest is malformed")
        if expected != cls._digest(snapshot):
            raise ValueError("runtime save integrity check failed")
        return GameState.from_snapshot(snapshot)

    @classmethod
    def load(cls, path: Path) -> GameState:
        return cls._read(Path(path))

    @classmethod
    def load_with_recovery(cls, path: Path) -> GameState:
        path = Path(path)
        try:
            return cls._read(path)
        except (OSError, ValueError, json.JSONDecodeError) as primary_error:
            backup = path.with_name(f"{path.name}.bak")
            if not backup.exists():
                raise primary_error
            return cls._read(backup)
