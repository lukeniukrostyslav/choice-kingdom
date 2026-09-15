# Choice Kingdom — Local Source Corrections 02

Date: 2026-09-15
Status: **APPLIED IN THE LOCAL WORKING COPY; SOURCE-LEVEL QA ONLY**

## Corrections

### E211–E270 catalog

Removed the duplicate post-catalog E271 bridge from `docs/EVENT_CATALOG_EXPANSION_211_270.md`.

Reason: the authoritative E271/E272 source is `docs/EVENT_CATALOG_EXPANSION_271_280.md`. Keeping E271 in both files creates two source definitions for one stable event ID.

### E212

Changed:

`clerk_discipled`

to:

`clerk_disciplined`

Reason: this is a confirmed source typo already identified by the QA inventory. The misspelling must not enter future production data.

## Verification

The authoritative source headings now reconcile as:

- E01–E32: 32
- E35–E70: 36
- E71–E110: 40
- E111–E150: 40
- E151–E210: 60
- E211–E270: 60
- E271–E272: 2

Total present authoritative event IDs: **270**, all unique.

Missing from the required E01–E272 ID boundary: **E33 and E34**.

This document intentionally does not fabricate E33/E34 and does not promote any runtime/schema readiness.
