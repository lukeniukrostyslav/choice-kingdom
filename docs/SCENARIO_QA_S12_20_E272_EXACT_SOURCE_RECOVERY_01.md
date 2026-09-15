# Choice Kingdom — S12.20 E272 Exact Source Recovery 01

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — EXACT SOURCE RECOVERED**  
Scope: frozen production E01–E272

## Purpose

Recover the exact authored E272 branch contract before promoting the border-crisis lifecycle into machine-readable production semantics.

## Recovery

Repository history contains commit `f573dbe45661a9cd7a8b836dcf2efdb8e94a7fd0` (`content: add canonical border crisis resolution E272`). The authoritative file is `docs/EVENT_CATALOG_EXPANSION_271_280.md`.

The recovered E272 source is explicit:

### Trigger
`thread.border_crisis = active` + `border_crisis_declared = true` + one available resolution route:
- `joint_border_survey`
- `negotiated_withdrawal`
- `border_commander_report`
- `military_red_line`

### E272-A — Ratify the joint border settlement
- `border_crisis_resolved = true`
- `border_crisis_declared = true` remains historical
- `thread.border_crisis = resolved`
- `pred.border_crisis = false`
- `history.border_crisis_resolved_diplomatically`
- effects: +5 reputation, +3 trust, -2 security

### E272-B — End the crisis under a military security guarantee
- `border_crisis_resolved = true`
- `border_crisis_declared = true` remains historical
- `thread.border_crisis = resolved_under_security_guarantee`
- `pred.border_crisis = false`
- `history.border_crisis_resolved_by_guarantee`
- effects: +5 security, -3 gold, -3 reputation

## Chronology gate

E271-A is the only declaration producer. E272-A/B are resolution producers and require the active crisis established by E271-A. E271-B cannot satisfy the E272 crisis-resolution prerequisite.

## Invariants

1. Resolution clears the active predicate without erasing the historical declaration.
2. Resolution history is immutable evidence and cannot reactivate the active predicate.
3. E195/E253/E255 remain consumers only.
4. No numeric resource is introduced.
5. E273–E277 remain excluded from production semantics.

## Acceptance

- Exact E272 source: **CLOSED**.
- Exact E272-A/B branch tokens: **CLOSED**.
- Border-crisis lifecycle source closure: **CLOSED at source level**.
- Runtime schema promotion: **still blocked** by remaining composite predicates, replay producers, delayed contracts, ending precedence and executable graph closure.

## Verification note

The recovered source was re-read directly from the repository history/file and is not inferred from the earlier placeholder registry. The prior S12.16 blocker is therefore superseded for E272 exact-token recovery.
