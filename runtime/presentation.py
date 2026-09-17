from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from typing import Any

from .session import SessionView


@dataclass(frozen=True)
class PresentationChoice:
    """Immutable UI-facing choice projection; contains no gameplay semantics."""

    id: str
    label: str
    text: str
    state: str = "idle"


@dataclass(frozen=True)
class PresentationSnapshot:
    """Stable serialization boundary between GameSession and presentation clients."""

    schema_version: int
    run_id: str
    event_id: str
    title: str
    turn: int
    choices: tuple[PresentationChoice, ...]
    terminal: bool

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["choices"] = [asdict(choice) for choice in self.choices]
        return payload

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, sort_keys=True, separators=(",", ":"))


class GameSessionPresentationBridge:
    """Read-only bridge from canonical GameSession views to UI contracts.

    It accepts only SessionView data and cannot mutate GameState, execute
    choices, route events, or calculate gameplay rules.
    """

    SCHEMA_VERSION = 1

    @classmethod
    def snapshot(cls, view: SessionView) -> PresentationSnapshot:
        return PresentationSnapshot(
            schema_version=cls.SCHEMA_VERSION,
            run_id=view.run_id,
            event_id=view.event_id,
            title=view.title,
            turn=view.turn,
            choices=tuple(
                PresentationChoice(id=choice_id, label=label, text=text)
                for choice_id, label, text in view.choices
            ),
            terminal=view.terminal,
        )

    @classmethod
    def snapshot_json(cls, view: SessionView) -> str:
        return cls.snapshot(view).to_json()
