# Choice Kingdom — S12.27 Delayed Lifecycle Gate Matrix

Date: 2026-09-15
Status: **PARTIAL — SOURCE IDENTITIES FROZEN WHERE PROVEN**
Frozen production scope: E01–E272

## Purpose
Convert the currently closed delayed-source identities into an explicit lifecycle gate without inventing exact turns from vague authored phrases.

| Callback | Source identity | Authored timing | Exact cancellation / supersession | Status |
|---|---|---|---|---|
| E181 | toll concession source | 5+ turns | open | PARTIAL |
| E182 | E117-B `veteran_patronage` | 4+ turns | open | PARTIAL |
| E183 | E118-B `estate_exception` | 5+ turns | open | PARTIAL |
| E184 | secret evidence route | 4+ turns | open; producer unresolved | OPEN |
| E185 | E17-A `cheap_weapons` | later military crisis | open | PARTIAL |
| E242 | E118-B `estate_exception` | 6+ turns | open | PARTIAL |
| E243 | E18-B `public_bridge` | 5+ turns | open | PARTIAL |
| E244 | E09-B `flexible_accounts` | 5+ turns | open | PARTIAL |
| E245 | compensation route candidates E20-A/E125-A/E156-A | 6+ turns | open; producer unresolved | OPEN |
| E246 | E160-A `winter_rent_ceiling` | 5+ turns | open | PARTIAL |

## Exact-once identity

Every delayed callback must eventually use:

`sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersession rule`

No callback is promoted to runtime merely because its source identity is known.

## Timing rule

The authored expressions `4+`, `5+`, `6+`, and `later` are relative constraints, not invented absolute turns. Runtime encoding must preserve the minimum delay and separately define the resolution condition where the source text provides one. No arbitrary fixed turn is permitted.

## Source distinction rules

- E245 candidates remain distinct until authoritative source text proves a composite or family rule.
- E243 remains tied to `public_bridge`, not a generic bridge investment alias.
- E246 remains tied to `winter_rent_ceiling`; do not rename it to a generic price-ceiling producer without source evidence.
- E185 requires the later military-crisis condition in addition to `cheap_weapons`.
- E184 cannot be closed by assuming any generic evidence flag is equivalent to the secret-evidence route.

## Save/load and replay gate

Pending callbacks must survive save/load with their original source identity and exactly-once key. Ordinary first-run callbacks must not cross into replay metadata. Replay-only callbacks require explicit `meta.*` producers and isolation.

## Acceptance

PASS — currently known source identities are separated from lifecycle semantics.
PASS — vague timing is not converted into guessed absolute turns.
PASS — E245 remains open rather than being falsely unioned.
PASS — replay boundary retained.
OPEN — cancellation/supersession matrix.
OPEN — complete E01–E272 delayed inventory.
OPEN — executable producer/consumer graph.
