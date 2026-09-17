from __future__ import annotations

from dataclasses import dataclass

from .presentation import SessionPresentation, SessionPresenter


@dataclass(frozen=True)
class RealmScreen:
    session: SessionPresentation

    @property
    def resources(self):
        return self.session.resources

    @property
    def pending_consequences(self):
        return self.session.pending_delays


@dataclass(frozen=True)
class HistoryScreen:
    session: SessionPresentation

    @property
    def entries(self) -> tuple[str, ...]:
        return self.session.history


@dataclass(frozen=True)
class PeopleScreen:
    session: SessionPresentation

    @property
    def relationships(self):
        return self.session.relationships


@dataclass(frozen=True)
class InvestigationScreen:
    session: SessionPresentation

    @property
    def threads(self) -> tuple[str, ...]:
        return self.session.threads

    @property
    def evidence(self) -> tuple[str, ...]:
        return self.session.ending_evidence


@dataclass(frozen=True)
class EndingScreen:
    session: SessionPresentation

    @property
    def ending_identity(self) -> str | None:
        return self.session.ending_identity

    @property
    def evidence(self) -> tuple[str, ...]:
        return self.session.ending_evidence

    @property
    def terminal(self) -> bool:
        return self.session.terminal


@dataclass(frozen=True)
class SettingsScreen:
    reduced_motion: bool = False
    large_text: bool = False
    rtl: bool = False


class JourneyScreenHost:
    """Production-facing projection host for the non-mutating journey surfaces.

    All screen models derive from the same canonical SessionPresenter snapshot.
    No screen computes gameplay effects, routing, relationships, evidence, or
    delayed-consequence semantics.
    """

    def __init__(self, presenter: SessionPresenter):
        self.presenter = presenter

    def realm(self) -> RealmScreen:
        return RealmScreen(self.presenter.snapshot())

    def history(self) -> HistoryScreen:
        return HistoryScreen(self.presenter.snapshot())

    def people(self) -> PeopleScreen:
        return PeopleScreen(self.presenter.snapshot())

    def investigation(self) -> InvestigationScreen:
        return InvestigationScreen(self.presenter.snapshot())

    def ending(self) -> EndingScreen:
        return EndingScreen(self.presenter.snapshot())

    @staticmethod
    def settings(*, reduced_motion: bool = False, large_text: bool = False, rtl: bool = False) -> SettingsScreen:
        return SettingsScreen(reduced_motion=reduced_motion, large_text=large_text, rtl=rtl)
