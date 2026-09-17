# Block 10 — Localization 20+ Gate

Status: **IN PROGRESS — 55%**.

Implemented:
- Canonical registry for 28 locale tags.
- English fallback and region-tag normalization.
- RTL metadata for Arabic and Hebrew.
- Android per-app locale configuration for all 28 declared locales.
- AndroidX AppCompat per-app locale switching seam with persisted application locales.
- Android UI strings have a default resource catalog instead of relying exclusively on future locale overlays.
- Dedicated Python + Android build gate.

Remaining before 100%:
- Complete translated resource coverage for every Android user-visible string in all 28 locales.
- Localize the full E01–E272 event/choice/ending narrative surface, not merely the UI shell.
- Add automated key-completeness and untranslated/fallback detection for every locale.
- Add locale-specific runtime smoke coverage, including Arabic/Hebrew RTL and long/CJK strings.

Android's localization guidance requires a complete default resource set and recommends resource-based localized strings; Android 13+ also supports per-app language preferences and Android 14 can generate locale configuration from resources. The current implementation establishes the infrastructure but does not claim translation completeness yet.
