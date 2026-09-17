from __future__ import annotations

from pathlib import Path

from .presentation import GameSessionPresentationBridge
from .session import GameSession


class AndroidRuntime:
    """Thin Android embedding adapter over the canonical GameSession.

    Android supplies only the writable canonical-content root and user intent.
    Gameplay rules, routing, persistence semantics and authored consequences
    remain exclusively inside GameSession/DecisionEngine.
    """

    def __init__(self, root: str | Path, run_id: str):
        self.root = Path(root)
        self.session = GameSession.new(self.root, run_id)

    def snapshot_json(self) -> str:
        return GameSessionPresentationBridge.snapshot_json(self.session.view())

    def choose(self, choice_id: str) -> str:
        self.session.choose(choice_id)
        return self.snapshot_json()


def start(root: str, run_id: str) -> AndroidRuntime:
    return AndroidRuntime(root, run_id)
