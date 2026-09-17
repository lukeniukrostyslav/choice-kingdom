# Choice Kingdom — Audio & Haptics Design Contract V1

Status: ACTIVE — semantic feedback vocabulary

## Purpose

Audio and haptics reinforce player-facing meaning without becoming required for comprehension. The runtime vocabulary is presentation-only and must never calculate gameplay outcomes.

## Semantic mapping

| Semantic | Sound token | Haptic token | Intent |
|---|---|---|---|
| choice_focus | `ui_focus` | `tick_soft` | Quietly identifies focus/selection movement |
| choice_confirm | `choice_confirm` | `confirm_medium` | Confirms a committed choice |
| consequence_reveal | `consequence_reveal` | `reveal_medium` | Marks consequence information becoming visible |
| consequence_pending | `pending_pulse` | `pulse_soft` | Signals unresolved/delayed information |
| error | `ui_error` | `error_light` | Signals invalid/unavailable interaction |
| navigate | `ui_navigate` | `tick_soft` | Provides restrained navigation feedback |
| ending_reveal | `ending_reveal` | `reveal_strong` | Gives the ending its deliberate emotional landing |

## Premium rules

- Feedback must be semantic, restrained and interruptible where possible.
- Audio and haptics are redundant with visual state, never the sole source of meaning.
- Separate user settings can disable sound and haptics independently.
- Reduced-motion and accessibility settings must not remove essential visual state communication.
- Ending feedback may be stronger than navigation feedback, but must remain consistent with the visual hierarchy.
- No sound/haptic token may mutate `GameSession` or determine a gameplay result.
- Android-specific implementation is deferred until the Android module exists; these tokens are the stable cross-platform contract.

## Exit evidence

P23 remains below production completion until these semantics are bound to real Android audio/haptic APIs, tested with accessibility settings, and covered by representative cross-screen regression evidence.
