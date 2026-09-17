# Choice Kingdom — History / Chronicle Contract v1

Status: DESIGN-CLOSURE ARTIFACT
Scope: D7 History / Chronicle

## Purpose

History is the player's reliable retrospective of decisions and known consequences. It must distinguish what happened from what remains unknown or pending.

## Entry anatomy

Every HistoryEntry uses this order:

1. event/decision title;
2. player-facing date/sequence marker when available;
3. decision summary;
4. known consequence summary;
5. pending/uncertain marker when applicable;
6. links to relevant character/faction/evidence context when available.

Internal event IDs and implementation identifiers never appear.

## Entry states

| State | Presentation |
|---|---|
| Recorded | Normal completed entry with decision and known consequences. |
| Pending | Decision is recorded, but a future consequence remains unresolved. |
| Unresolved | The record exists but the game cannot safely expose a final interpretation. |
| Empty | Clear explanation that no decisions are recorded yet. |
| Long | Full text wraps; entry height grows instead of clipping or shrinking below readable size. |

## Ordering

Newest relevant decision appears first by default. If chronological reconstruction is unavailable, the UI must not fabricate timestamps. Entries use the game's actual sequence metadata when provided.

## RTL and localization

- Directional layout mirrors under RTL.
- Semantic order remains decision → known result → pending/uncertain context.
- Long translations and CJK strings wrap naturally.
- Labels are never truncated in a way that removes state meaning.

## Accessibility

- Each HistoryEntry is one semantic group with title, decision, consequence, and state.
- State is expressed by text/icon plus optional surface treatment, not color alone.
- Focus order follows visual/semantic reading order.
- Touch targets remain at least 48dp.

## Acceptance criteria for D7 closure

- [x] Entry anatomy defined.
- [x] Recorded/pending/unresolved/empty/long states defined.
- [x] Ordering rules avoid fabricated dates.
- [x] Internal identifiers excluded.
- [x] RTL/localization/CJK behavior defined.
- [x] Accessibility and focus grouping defined.
- [x] Long content behavior defined.

D7 closure evidence: this contract plus the production token contract and screen matrix completes the design-level History specification. Runtime implementation and device QA remain separate gates.
