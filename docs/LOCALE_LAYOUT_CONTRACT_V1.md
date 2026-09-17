# Choice Kingdom — Locale / RTL Layout Contract v1

This contract is presentation-only. Localization must never alter gameplay semantics, identifiers, routing, effects, or canonical state.

## Rules

- LTR locales use normal navigation ordering.
- RTL locales mirror directional navigation and alignment while preserving meaning.
- All player-facing narrative and choice text may wrap; truncation of critical text is forbidden.
- Large-text mode increases text scale and lets secondary content reflow/stack before shrinking text.
- Choice controls retain their minimum touch target while text expands.
- Numeric/resource meaning remains stable when layout direction changes.
- Icons that encode direction must be reviewed individually; neutral status icons must not be mirrored blindly.
- Internal event IDs and implementation keys never appear as localization strings.
- CJK/long-string expansion is treated as a layout case, not a translation exception.
- Locale policy is derived at presentation time and does not mutate `GameSession`.

## Representative proof requirements

The locale proof must cover Event, Main Menu, History, Investigation, Ending and Settings in at least:

- LTR + default text size;
- RTL + default text size;
- LTR + large text;
- RTL + large text;
- long choice labels and long narrative strings.

The proof is not a claim of full 20+ locale completion; production locale coverage remains open until real translations and Android rendering are verified.
