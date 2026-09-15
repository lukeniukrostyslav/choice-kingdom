# Choice Kingdom — Scenario QA S10.4 Delayed Source/Target Reconciliation 01

Date: 2026-09-15  
Status: **PARTIAL PASS — SOURCE-LEVEL QA**  
Frozen production scope: **E01–E272**  
Expansion candidates: **E273–E277 excluded**

## Purpose

Reconcile the delayed-consequence inventory against the authoritative producer chronology without inventing source choices, due turns, resolution targets or replay metadata.

Required canonical callback identity remains:

`sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersession rule`

## Source-identity results

| Callback | Source identity | Timing evidence | Target / resolution | Gate |
|---|---|---|---|---|
| E181 | **E45-B** is the current producer-inventory source identity for the infrastructure/toll concession family | authored family says 5+ turns; exact normalized timing still open | E181-A/B outcome; exact callback lifecycle open | PARTIAL |
| E182 | **E117-B → veteran_patronage** | authored trigger says 4+ turns | E182-A/B | SOURCE CLOSED / lifecycle open |
| E183 | **E118-B → estate_exception** | authored trigger says 5+ turns | E183-A/B | SOURCE CLOSED / lifecycle open |
| E184 | secret-evidence route | 4+ turns authored | E184-A/B | SOURCE OPEN — exact producer not frozen |
| E185 | **E17-A → cheap weapons** | later military crisis; no executable crisis turn supplied | E185-A prevents / E185-B delayed-loss branch | SOURCE CLOSED / lifecycle open |
| E242 | **E118-B explicit candidate**, broader prior-exception union not admitted | 6+ turns authored | E242-A/B | PARTIAL — exact source union open |
| E243 | **E18-B → public_bridge** | 5+ turns authored | E243-A/B | SOURCE CLOSED / lifecycle open |
| E244 | **E09-B → flexible_accounts** | 5+ turns authored | E244-A/B | SOURCE CLOSED / lifecycle open |
| E245 | **E125-A + E156-A candidates** | 6+ turns authored | E245-A/B | OPEN — exact authored source rule required |
| E246 | **E160-A → winter_rent_ceiling** | 5+ turns authored | E246-A/B | CONDITIONAL normalization |
| E247 | second-run information route | replay trigger, no ordinary-run timing | E247-A/B | META OPEN |
| E248 | replay callback / forgotten favor | replay trigger | E248-A/B | META OPEN |

## Important normalization decisions

1. `E181` uses **E45-B** as the current canonical source identity because the producer inventory explicitly records that source. No E18 alias is introduced merely because E18 is also a bridge/toll decision.
2. E182/E183/E185/E243/E244 have source-closed producer identities. Their delayed callbacks are still not runtime-closed because exactly-once, cancellation/supersession, save/load and executable timing semantics remain unresolved.
3. E242 cannot silently become "any noble exception". E118-B is explicitly source-backed, while a broader authored union requires direct catalog evidence and a deterministic source-set rule.
4. E245 cannot silently union `border_compensation` and `requisition_compensation`; the canonical contract must explicitly define whether the authored compensation route is one source, an authored union, or a separate source family.
5. E246 normalizes the authored phrase `price ceiling` to `winter_rent_ceiling` only conditionally; generic price-control flags are forbidden.
6. E247/E248 remain replay/meta consumers. Ordinary history flags cannot automatically cross the replay boundary.

## Timing rule

Authored phrases such as `4+ turns`, `5+ turns`, and `6+ turns` are retained as **relative timing evidence**, not silently converted to absolute engine turns. A production contract must define `earliestTurn = sourceTurn + N` (or another explicitly authored rule), plus resolution window and supersession semantics, before runtime implementation.

## Exactly-once / cancellation gate

No delayed family is promoted to runtime-closed by this pass. Each callback still requires a deterministic exactly-once key and observable cancellation/supersession state. E185 additionally requires the military-crisis lifecycle to be canonicalized before the delayed-loss callback can be executable.

## Replay isolation

E247/E248 remain isolated from ordinary run-local state. Pending callbacks, active predicates and unresolved crises must not cross into a new run unless explicitly authored as `meta.*` data. No ordinary flag is promoted to `meta.*` by implication.

## E273–E277 integrity

No E273–E277 event is admitted as a delayed source, producer, target or replay key for frozen production. Expansion candidates remain quarantined.

## Gate result

**S10.4 PARTIAL PASS.**

This pass materially reduces ambiguity in delayed source identity for E181–E185 and E242–E246, but it does not claim executable delayed contracts. The remaining work is exact timing normalization, resolution-target identity, exactly-once/cancellation semantics, save/load persistence and replay metadata.

**S10 remains 72%. Scenario QA remains 65%.**

## Next autonomous block

1. Continue S10 against the remaining E218/E225 and E251–E272 delayed/lifecycle families.
2. Reconcile E32/E136 transport lifecycle with delayed persistence and expiry.
3. Audit S11 ending prerequisites, incoming paths and precedence.
4. Audit S12 fresh-run reachability and replay reachability.
