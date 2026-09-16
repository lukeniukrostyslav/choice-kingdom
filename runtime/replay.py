from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .state import GameState, REPLAY_EXPORT_SCHEMA, REPLAY_META_KEYS


@dataclass(frozen=True)
class CompletedRunExport:
    """Typed boundary for the only data allowed to cross a completed-run boundary."""

    prior_run_id: str
    meta_keys: tuple[str, ...]
    schema_version: int = REPLAY_EXPORT_SCHEMA
    completed: bool = True

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "run_id": self.prior_run_id,
            "completed": self.completed,
            "meta_keys": list(self.meta_keys),
        }


class ReplayBoundary:
    """Production replay boundary: reset run-local state, import only canonical meta."""

    @staticmethod
    def export(state: GameState) -> CompletedRunExport:
        data = state.export_completed_run_meta()
        return CompletedRunExport(
            prior_run_id=data["run_id"],
            meta_keys=tuple(data["meta_keys"]),
        )

    @staticmethod
    def start_new_run(run_id: str, export: CompletedRunExport | dict[str, Any]) -> GameState:
        if isinstance(export, CompletedRunExport):
            payload = export.as_dict()
        else:
            payload = dict(export)
        if payload.get("schema_version") != REPLAY_EXPORT_SCHEMA:
            raise ValueError("unsupported replay export schema")
        if payload.get("completed") is not True:
            raise ValueError("replay export is not a completed run")
        prior_run_id = payload.get("run_id")
        if not isinstance(prior_run_id, str) or not prior_run_id:
            raise ValueError("replay export is missing prior run identity")
        if prior_run_id == run_id:
            raise ValueError("replay run identity must differ from prior run")
        keys = payload.get("meta_keys", [])
        if not isinstance(keys, list):
            raise ValueError("replay export meta_keys must be a list")
        if any(key not in REPLAY_META_KEYS for key in keys):
            raise ValueError("replay export contains non-canonical meta key")
        if len(keys) != len(set(keys)):
            raise ValueError("replay export contains duplicate meta key")
        return GameState.new_run_from_completed_prior(run_id, payload)
