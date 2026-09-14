# Choice Kingdom — Localization Requirements

Localization is part of the initial release, not a post-launch feature.

## Target locales
At least 20 locales must ship in the first release. The exact final list is tracked in the implementation and must include major European languages plus Russian, Ukrainian, Arabic, Hebrew, Hindi, Indonesian, Vietnamese, Thai, Japanese, Korean, Simplified Chinese and Traditional Chinese.

## Coverage
Every user-visible string must be localizable:
- menu/UI labels
- event titles and bodies
- choice labels
- consequence feedback
- character names where localization requires it
- resource names
- endings
- tutorial/help
- save/load errors
- accessibility text
- purchase/store copy where applicable

## Runtime rules
- Device locale is detected on first launch.
- Unsupported device locales fall back to English.
- User-selected language is persisted.
- Changing language does not reset gameplay state.
- Missing translation keys are detected by automated checks; raw internal keys must never be presented as final UI.
- Pluralization and interpolation must be explicit and safe.
- RTL layouts must be tested for Arabic and Hebrew.
- Long strings must not silently overflow, overlap or become unreadable.

## Quality gate
A locale is not considered complete because a CSV column exists. It requires key coverage, valid parsing, runtime loading, fallback validation and UI smoke coverage.
