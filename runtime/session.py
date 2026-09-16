from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .ending_contract import EndingQualification
from .endings import EndingResolution, EndingResolver
from .ending_sources import EndingSourceCompiler, SourceClosedEndingFacts
from .engine import DecisionEngine, ExecutionResult, DelayedActivationResult
from .replay import CompletedRunExport, ReplayBoundary
from .state import GameState, SaveStore


@dataclass(frozen=True)
class SessionView:
    """Presentation-neutral snapshot for a future UI layer."""

    run_id: str
    turn: int
    event_id: str
    title: str
    trigger: str
    choices: tuple[tuple[str, str, str], ...]
    resources: tuple[tuple[str, int], ...]
    relationships: tuple[tuple[str, int], ...]
    terminal: bool
    ending_identity: str | None


class GameSession:
    """Production-facing orchestration boundary around the canonical runtime.

    The session owns lifecycle operations used by a UI/application layer while
    delegating every state mutation to the existing DecisionEngine/GameState
    contracts. No gameplay rule is duplicated here.
    """

    def __init__(self, root: Path, state: GameState):
        self.root = Path(root)
        self.engine = DecisionEngine(self.root)
        self.state = state
        self.ending_resolver = EndingResolver()
        self._selected_event_id = state.current_event_id

    @classmethod
    def new(cls, root: Path, run_id: str) -> "GameSession":
        return cls(root, GameState.fresh(run_id))

    @classmethod
    def load(cls, root: Path, path: Path) -> "GameSession":
        return cls(root, SaveStore.load(Path(path)))

    @classmethod
    def load_with_recovery(cls, root: Path, path: Path) -> "GameSession":
        return cls(root, SaveStore.load_with_recovery(Path(path)))

    def view(self) -> SessionView:
        event = self.engine.event(self._selected_event_id)
        return SessionView(
            run_id=self.state.run_id,
            turn=self.state.turn,
            event_id=event.event_id,
            title=event.title,
            trigger=event.trigger,
            choices=tuple((choice.choice_id, choice.label, choice.text) for choice in event.choices),
            resources=tuple(sorted(self.state.resources.items())),
            relationships=tuple(sorted(self.state.relationships.items())),
            terminal=self.state.terminal,
            ending_identity=self.state.ending_identity,
        )

    def available_events(self) -> tuple[str, ...]:
        return tuple(event.event_id for event in self.engine.available(self.state))

    def available_choices(self) -> tuple[str, ...]:
        return tuple(choice.choice_id for choice in self.engine.event(self._selected_event_id).choices)

    def choose(self, choice_id: str) -> ExecutionResult:
        result = self.engine.execute(self.state, self._selected_event_id, choice_id)
        self._selected_event_id = self.state.current_event_id
        return result

    def select_event(self, event_id: str) -> None:
        """Move presentation focus to an event already qualified by the engine."""
        if event_id not in self.available_events():
            raise ValueError(f"event is not currently available: {event_id}")
        self._selected_event_id = event_id

    def activate_delayed_target(
        self,
        exactly_once_key: str,
        *,
        condition_satisfied: bool | None = None,
    ) -> DelayedActivationResult:
        """Activate one canonical delayed consequence through the application seam."""
        result = self.engine.activate_delayed_target(
            self.state,
            exactly_once_key,
            condition_satisfied=condition_satisfied,
        )
        self._selected_event_id = result.target_event_id
        return result

    def execute_delayed_target(
        self,
        exactly_once_key: str,
        choice_id: str,
        *,
        condition_satisfied: bool | None = None,
    ) -> ExecutionResult:
        """Activate and execute one canonical delayed target through the same seam as normal choices."""
        result = self.engine.execute_delayed_target(
            self.state,
            exactly_once_key,
            choice_id,
            condition_satisfied=condition_satisfied,
        )
        self._selected_event_id = self.state.current_event_id
        return result

    def activate_next_due_delay(self) -> DelayedActivationResult:
        result = self.engine.activate_next_due_delay(self.state)
        self._selected_event_id = result.target_event_id
        return result

    def execute_next_due_delay(self, choice_id: str) -> ExecutionResult:
        due = self.engine.activate_next_due_delay(self.state)
        result = self.engine.execute(self.state, due.target_event_id, choice_id)
        self._selected_event_id = self.state.current_event_id
        return result

    def ending_source_facts(self) -> SourceClosedEndingFacts:
        """Expose only source-closed derived ending facts for application code."""
        return EndingSourceCompiler.compile_state(self.state)

    def resolve_ending(self, qualification: EndingQualification) -> EndingResolution:
        if self.state.terminal:
            return self.ending_resolver.resolve_qualification(self.state, qualification)
        self.state.terminal = True
        try:
            return self.ending_resolver.resolve_qualification(self.state, qualification)
        except Exception:
            self.state.terminal = False
            raise

    def save(self, path: Path) -> None:
        SaveStore.save(self.state, Path(path))

    def snapshot_digest(self) -> str:
        return SaveStore.snapshot_digest(self.state)

    def export_replay(self) -> CompletedRunExport:
        return ReplayBoundary.export(self.state)

    @classmethod
    def new_replay(cls, root: Path, run_id: str, prior: CompletedRunExport | dict) -> "GameSession":
        state = ReplayBoundary.start_new_run(run_id, prior)
        return cls(root, state)
