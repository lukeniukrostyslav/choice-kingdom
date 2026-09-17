# Block 10 — Localization 20+ Gate

Status: **IN PROGRESS — 89%**.

## Verified implementation
- Canonical registry for 8 release locale tags.
- English fallback and region-tag normalization.
- RTL metadata for Arabic and Hebrew.
- Android per-app locale configuration for all 8 release locales.
- AndroidX AppCompat per-app locale switching seam.
- Stable navigation keys so translated screen labels cannot corrupt navigation state.
- Android player-facing UI copy routed through resources instead of previous hardcoded presentation strings.
- Localized Android resource overlays for the declared release locales.
- Automated critical-key coverage tests.
- Canonical generated narrative-key inventory/locale contract: **272 events, 520 choices, 1,584 narrative keys, 8 release locales**.
- NarrativeLocalizer separates authored narrative semantics from localized presentation text and exposes missing/fallback keys.
- Strict JSON narrative-pack repository loader validates schema, locale identity, non-empty fallback and non-empty translation.
- Block 10 CI now executes the strict narrative-pack repository tests before the Android build.

## Remaining before 100%
1. Populate actual narrative translations for **all 1,584 keys in each of the 7 translated release locales** (RU, UK, IT, DE, FR, ES, PT). English is the canonical source language; it is not counted as a translation.
2. Preserve authored gameplay semantics exactly: event IDs, choice IDs, effects, conditions and state tokens must never be translated into gameplay identifiers.
3. Add a complete translation-pack coverage gate that rejects any locale with fewer than 1,584 translated keys or any translation equal to the English fallback.
4. Add Android runtime smoke for locale switching, Arabic/Hebrew RTL, long strings and CJK rendering.
5. Run and verify the complete Block 10 GitHub Actions gate after the real translation packs are populated.

## Important QA rule
The current architecture intentionally refuses to count a missing translation as completed localization. Android may fall back to res/values/strings.xml when a localized resource is absent, so locale declaration alone is not evidence of translation completeness. citeturn0search1turn0search0

**No false 100%:** the remaining gap is the actual translated narrative corpus, not another documentation or percentage-labeling task.