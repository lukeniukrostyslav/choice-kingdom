from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from runtime.presentation import InteractionState, SessionPresenter
from runtime.session import GameSession


class PremiumPresentationProjectionTests(unittest.TestCase):
    def test_session_projection_exposes_history_threads_delays_and_ending_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            session = GameSession.new(Path(tmp), "premium-projection")
            presenter = SessionPresenter(session)
            view = presenter.snapshot()

            self.assertEqual(view.history, ())
            self.assertEqual(view.threads, ())
            self.assertEqual(view.pending_delays, ())
            self.assertEqual(view.ending_evidence, ())
            self.assertEqual(view.relationships[0].value, 0)
            self.assertEqual(view.terminal, False)

    def test_choice_state_remains_presentation_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            session = GameSession.new(Path(tmp), "premium-state")
            presenter = SessionPresenter(session)
            choice_id = session.available_choices()[0]

            presenter.focus_choice(choice_id)
            self.assertEqual(presenter.snapshot().choices[0].state, InteractionState.FOCUSED)
            self.assertEqual(session.view().turn, 1)

            presenter.press_choice(choice_id)
            self.assertEqual(presenter.snapshot().choices[0].state, InteractionState.PRESSED)
            self.assertEqual(session.view().turn, 1)


if __name__ == "__main__":
    unittest.main()
