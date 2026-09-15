# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Meaningful choices, recurring characters, delayed consequences, hidden information, systemic event chains, multiple endings and replayable paths.

## Release target
- Android-first premium one-time purchase, approximately €2.99–€4.99.
- No ads, no subscription, no mandatory backend for core gameplay.
- 20+ locales including RTL and long-string validation.
- Full authored campaign target: approximately 250–350+ meaningful nodes and 8–12 recognizable endings.

## Frozen authored scope
Production catalog is **E01–E272**. E273–E277 are expansion candidates and are excluded from production semantics, producer/consumer edges and reachability.

## Development order
**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → APK → release.**

No mock/stub gameplay or premature production-readiness claims.

## Current phase
**Narrative/content canonicalization and QA.** Authored checkpoint E01–E272. Production schema and Decision Engine remain blocked until canonical contracts and reachability are sufficiently closed.

## Scenario QA
Dedicated Scenario QA score is approximately **89%**. This is distinct from overall project completion and is not runtime/Android readiness.

### S01–S12 working indicators
- S01 **80%**
- S02 **70%**
- S03 **70%**
- S04 **70%**
- S05 **60%**
- S06 **55%**
- S07 **80%**
- S08 **78%**
- S09 **62%** — replay meta producer boundary audited; exact meta producer/key inventory remains open.
- S10 **72%**
- S11 **58%** — ending prerequisite satisfiability screen closes additional false-positive routes; deterministic precedence remains open.
- S12 **88%** — source-level machine QA includes delayed source tokens, producer/consumer collision screening, ending satisfiability and replay-meta boundary audits. Runtime reachability remains unverified.

## Latest QA work
- **Replay Meta Producer Audit 01:** added `docs/SCENARIO_QA_REPLAY_META_PRODUCER_AUDIT_01.md`. Audited E186/E247/E248/E249/E250/E270 against the required `metaKey + sourceEvent/sourceChoice + promotionTiming + isolationRule + persistenceScope` tuple. No complete producer/key was promoted; ordinary history remains isolated from replay meta-state. Commit `546a1866c4a6d4eec4ccbf04738347e142cba2d0`.
- **Ending Prerequisite Satisfiability Audit 01:** added `docs/SCENARIO_QA_ENDING_PREREQUISITE_SATISFIABILITY_01.md`. It audits all seven ending families for consumer-only prerequisites, circular/self-manufactured evidence, replay isolation and unsatisfied graph routes. People's Charter is explicitly blocked on an executable final-charter producer; Second Founder remains blocked on replay/convergence closure. Commit `e0cd54a247f2233ee4e4ee30e995c3dd0f2f9574`.
- **Machine Ending Prerequisite Satisfiability 01:** added `docs/MACHINE_ENDING_PREREQUISITE_SATISFIABILITY_01.json`, freezing the seven family boundaries and explicit non-claims for fresh-run reachability, replay reachability and precedence. Commit `294a60cae1e2fd3f4a948a7c6cc6a0275042aa9d`.
- **Ending Satisfiability Validator:** added `tools/validate_ending_prerequisite_satisfiability.py`. Commit `a73533fa1432122beaf7f2f57280d9bcb596f017`.
- **CI wiring:** `.github/workflows/canonical-graph.yml` now runs the ending prerequisite satisfiability validator and uploads its machine report. Commit `3880941b168ce3e353f8e3bce6d88486f974bd27`.
- **Producer/Consumer Collision Audit 01:** added `docs/SCENARIO_QA_PRODUCER_CONSUMER_COLLISION_AUDIT_01.md`. E245 remains exclusively E20-A; E242 remains partial; E184 remains open; E185 source identity and later crisis lifecycle remain separate. Commit `ce2f20b9664dd37b0c0f9ddc5362f5748b851a3b`.
- **Machine Producer/Consumer Collision Contract 01:** added `docs/MACHINE_PRODUCER_CONSUMER_COLLISION_01.json`. Commit `f221fd3a8649ac6cf91b70f27d0c5bc57d4ceef7`.
- **Producer/Consumer Collision Validator:** added `tools/validate_producer_consumer_collision.py`. Commit `adf6796f78a665fb333556a78dc7db8cef0b454e`.
- **CI wiring:** collision validator added to canonical graph QA. Commit `41286730fc5e071d4b9efe4d8959eee31fe5910e`.

## Current canonical source status

### Source-closed delayed producers
- E18-B → `public_bridge` → E243
- E09-B → `flexible_accounts` → E244
- E117-B → `veteran_patronage` → E182
- E118-B → `estate_exception` → E183/E242
- E17-A → `cheap_weapons` → E185
- E160-A → `winter_rent_ceiling` → E246
- E136-B → `history.guild_logistics_cooperation` → E194
- **E20-A → `soldier_compensation` → E245**

### Ending prerequisite status
- Steward: positive route candidates exist; blockers/precedence/fresh-run reachability OPEN.
- Iron Crown: authority/security support candidates exist; blockers/precedence/reachability OPEN.
- Golden Compact: economic/guild support candidates exist; blockers/precedence/reachability OPEN.
- People's Charter: **OPEN/BLOCKED** because E209 is consumer-only for `pred.final_charter_prerequisites`.
- Broken Diadem: failure routes exist; deterministic failure precedence OPEN.
- Quiet Throne: narrative withdrawal/stability route exists; blocker precedence OPEN.
- Second Founder: **OPEN/BLOCKED** by replay meta producer/key plus systemic convergence and fresh-run/replay separation.

### Replay meta status
Replay-sensitive nodes E186/E247/E248/E249/E250/E270 are now explicitly audited. The repository has a hard boundary requiring a complete five-field producer tuple before any ordinary history can become persistent replay state. No such complete inventory is currently closed; replay reachability and save/load isolation remain unverified.

## Major unresolved gates
- authoritative source recovery or explicit authored correction for E33/E34 exact headings/effects;
- `pred.food_stable` vs `food_logistics_stabilized`;
- exact executable producer compilation for `pred.guild_influence_strong`;
- explicit convergence producer/key for `pred.systemic_explanation_verified`;
- runtime qualification/invalidation for `pred.coalition_cooperation`;
- executable ordering for `pred.constitutional_prepared_strong`;
- `pred.final_charter_prerequisites`;
- replay `meta.*` producer/key inventory;
- remaining delayed cancellation/supersession rules;
- E184 producer closure and E185 crisis resolution;
- ending incoming paths and deterministic precedence;
- exhaustive E01–E272 graph and fresh-run reachability;
- machine graph ↔ authoritative catalog semantic equality beyond ID parity.

## Current honest progress
- Foundation / rules: **95%**
- Authored content: **90%**
- Canonical Event IDs / continuity: **100%**
- Producer / Consumer QA: **99%**
- Derived Predicates / Machine Contracts: **99%**
- Delayed Consequences: **98%**
- Replay / Meta-state: **67%**
- Endings / precedence: **72%**
- Reachability / Causal Graph: **64%**
- Production Data Schema: **36%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **60%**. Scenario QA remains approximately **89%**; S09 moved to **62%**, S11 is **58%**, S12 is **88%**, and Endings / precedence is **72%**. These source-QA percentages must not be conflated with overall project completion or runtime/Android readiness.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.
