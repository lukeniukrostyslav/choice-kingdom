# Block 10 — Localization 20+ Gate

Status: **IN PROGRESS — 84%**.

## Verified implementation
- Canonical registry for 28 locale tags.
- English fallback and region-tag normalization.
- RTL metadata for Arabic and Hebrew.
- Android per-app locale configuration for all 28 declared locales.
- AndroidX AppCompat per-app locale switching seam.
- Stable navigation keys so translated screen labels cannot corrupt navigation state.
- Android player-facing UI copy routed through resources instead of previous hardcoded presentation strings.
- Localized Android resource overlays for the declared release locales.
- Automated critical-key coverage tests.
- A dedicated NarrativeLocalizer separates authored narrative semantics from localized presentation text and makes untranslated fallback observable to QA.

## Remaining before 100%
1. Populate narrative localization for E01–E272: titles, triggers, choice labels/text/body, consequence copy and ending presentation.
2. Provide verified translations for every declared locale rather than counting English fallback as translation.
3. Add an authoritative generated inventory for all 520 authored choices and all narrative keys.
4. Use the authoritative inventory as the locale translation contract and make the locale gate fail when a release locale silently falls back on a required narrative key.
5. Add Android runtime smoke for locale switching, Arabic/Hebrew RTL, long strings and CJK rendering.
6. Run and verify the complete Block 10 GitHub Actions gate.

Fallback strings are deliberately observable and are never counted as completed translations.