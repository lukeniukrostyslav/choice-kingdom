from __future__ import annotations

from pathlib import Path

from .presentation import GameSessionPresentationBridge
from .session import GameSession
from .state import SaveStore


ANDROID_SAVE_FILENAME = "android-runtime-save.json"


class AndroidRuntime:
    """Android embedding adapter over the canonical GameSession.

    The Android layer sends only user intents and renders immutable projections.
    Gameplay rules and mutation authority remain exclusively inside GameSession.
    The adapter adds only Android-local resume persistence around that canonical
    session, using the runtime's versioned/integrity-checked SaveStore.
    """

    def __init__(self, root: str | Path, run_id: str):
        self.root = Path(root)
        self.save_path = self.root / ANDROID_SAVE_FILENAME
        if self.save_path.exists():
            state = SaveStore.load_with_recovery(self.save_path)
            if state.run_id != run_id:
                raise ValueError("Android resume save belongs to a different run")
            self.session = GameSession(self.root, state)
        else:
            self.session = GameSession.new(self.root, run_id)

    def snapshot_json(self) -> str:
        return GameSessionPresentationBridge.snapshot_json(self.session.view())

    def choose(self, choice_id: str) -> str:
        self.session.choose(choice_id)
        self.session.save(self.save_path)
        return self.snapshot_json()

    def save(self) -> None:
        self.session.save(self.save_path)

    @property
    def run_id(self) -> str:
        return self.session.state.run_id


def start(root: str, run_id: str) -> AndroidRuntime:
    runtime = AndroidRuntime(root, run_id)
    runtime.save()
    return runtime
