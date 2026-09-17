from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .adaptive_navigation import AdaptiveNavigationModel
from .presentation import SessionPresentation


class MainMenuDestination(str, Enum):
    CONTINUE = "continue"
    NEW_RUN = "new_run"
    HISTORY = "history"
    SETTINGS = "settings"


@dataclass(frozen=True)
class MainMenuAction:
    destination: MainMenuDestination
    enabled: bool
    primary: bool = False


@dataclass(frozen=True)
class MainMenuScreen:
    """Premium launcher projection; it never mutates gameplay state."""

    title: str
    subtitle: str
    actions: tuple[MainMenuAction, ...]
    navigation: AdaptiveNavigationModel
    has_continue: bool
    last_event_id: str | None


def build_main_menu(
    session: SessionPresentation | None,
    navigation: AdaptiveNavigationModel,
    *,
    title: str = "Avelune",
    subtitle: str = "Every choice leaves a trace.",
) -> MainMenuScreen:
    """Build the launcher from canonical session presence only.

    Continue availability is derived from the existence of an active run. No
    gameplay qualification, routing, or state mutation belongs in the launcher.
    """
    has_continue = session is not None and not session.terminal
    last_event_id = session.event_id if session is not None else None

    actions = (
        MainMenuAction(MainMenuDestination.CONTINUE, enabled=has_continue, primary=True),
        MainMenuAction(MainMenuDestination.NEW_RUN, enabled=True),
        MainMenuAction(MainMenuDestination.HISTORY, enabled=session is not None),
        MainMenuAction(MainMenuDestination.SETTINGS, enabled=True),
    )
    return MainMenuScreen(
        title=title,
        subtitle=subtitle,
        actions=actions,
        navigation=navigation,
        has_continue=has_continue,
        last_event_id=last_event_id,
    )
