# Choice Kingdom — Graph ↔ Catalog Reconciliation 04

Date: 2026-09-14
Status: **SOURCE-VERIFIED AUDIT — NOT RUNTIME**
Scope: E211–E270.

## Purpose
This pass compares the causal edges declared in `EVENT_GRAPH.md` with the actual authored trigger/effect language in the E211–E270 catalog. The graph is treated as a design candidate only. An edge is promoted toward production only when the target trigger can be satisfied by a durable marker, relationship, event history, replay metadata, delayed contract, or deterministic derived predicate whose producer is known.

## Verified direct dependencies

- **E211 → E212/E216**: E211 produces `public_ledger_room` or `ledger_summary_access`; however the authored triggers of E212/E216 do not directly consume either marker. These graph edges are therefore **not yet runtime-proven** and need canonical predicate/route definitions.
- **E212 → E213/E214**: E212 produces `clerk_protected` / `clerk_discipled`, while E213 requires `regional_courts` and E214 requires institutional reform. **Design edge only** until a producer for those route predicates is mapped.
- **E214 → E215**: E214 produces `appointment_transparent` / `appointment_patronage`; E215 requires `law_notices_public`. **Not a direct marker dependency**.
- **E216 → E217**: direct and valid: E216 choice B produces `quiet_treasury_loan`, and E217 consumes it.
- **E218 → E219/E220**: E218 produces grain-contract markers; E219 requires market oversight and E220 requires `trade_risk_insurance`. **Not direct**; the graph is currently thematic unless a hidden route marker is specified.
- **E220 → E248**: E220 produces `trade_guarantee_honored` / `trade_guarantee_challenged`; E248 requires replay callback. **Not direct** without an explicit replay-transfer rule.
- **E222 → E245**: E222 has no durable marker in either choice, while E245 requires compensation route. **Graph edge not proven**.
- **E223 → E241/E252**: E223 produces medical-license markers; E241 requires Amara route and E252 requires illness + Amara route. **Relationship/route dependency may exist, but the marker contract is not explicit**.
- **E224 → E243**: E224 produces `river_safety_barriers` only on choice A, while E243 requires public bridge investment. **Possible semantic relationship but not exact marker match**.
- **E225 → E255**: E225 has `bread_queue_heard` / `bread_queue_dispersed`; E255 requires simultaneous food, border and civic pressure. **Derived-predicate dependency, not direct marker**.
- **E226 → E266**: E226 produces `mara_independent_mandate` / `mara_resigned`; E266 is an ending-qualification node. **Candidate ending influence, but exact qualification must be defined**.
- **E227 → E259/E267**: E227 choice A produces `military_red_line`; E259 requires army constitutional route. **Needs canonical route mapping**.
- **E229 → E219/E269**: E229 produces `ivo_shortcut_closed` / `ivo_shortcut_used`; E219 requires market oversight and E269 is an ending qualifier. **No direct runtime proof yet**.
- **E231 → E236/E269/E270**: E231 produces `toma_verification_first` / `toma_immediate_release`; later nodes require witness/evidence/replay qualification. **Needs explicit information-route contract**.
- **E232 → E233/E234/E235**: direct producer `intermediary_chain_traced` only appears on E232 choice A and is consumed directly by E235. E233/E234 are logically related but their own triggers (`forgery route`, `payment date`) need separate producers. **Partial verification**.
- **E233 → E249/E250**: E233 produces `seal_forensics` / `duplicate_seal_suppressed`; E249 requires archive route and E250 requires three or more related clues. **Derived evidence count needed; not direct**.
- **E234 → E236/E250**: E234 produces payment-pattern markers; E236 requires witness route and E250 clue cardinality. **Candidate evidence contribution, but cardinality must be modeled explicitly**.
- **E235 → E238/E268**: E235 produces `middleman_family_archive` only on choice B; E238 requires noble constitutional route and E268 is ending qualification. **Candidate, not direct**.
- **E236 → E263/E269**: E236 choices do not expose a unique `coalition route` or ending marker. **Needs canonical evidence/coalition contract**.
- **E237 → E261/E262**: no explicit marker on either choice. The graph assumes public-accountability/faction route state. **Needs durable marker**.
- **E238 → E228/E265**: no durable marker in E238. **Needs noble credibility marker or route history**.
- **E239 → E219/E261**: no durable marker. **Needs guild-logistics credibility state**.
- **E240 → E227/E259**: no durable marker. **Needs border intelligence route state**.
- **E241 → E223/E262**: no durable marker. **Needs Lantern credibility state**.
- **E242 → E228/E238**: E242 itself has no durable choice markers. **Graph candidate only**.
- **E243 → E224/E239**: E243 choice A has no marker and choice B has none. **Graph candidate only**.
- **E244 → E216/E258**: E244 has `reconstructed_accounts` only on choice B; targets require treasury shortfall / budget reform. **Needs accounting-state contract**.
- **E245 → E222/E246**: no durable marker. **Graph candidate only**.
- **E246 → E219/E257**: no explicit marker. **Graph candidate only**.
- **E247 → E232/E249/E250**: E247 has `alternate_suspect_tested` only on A; target routes need replay/evidence/archive predicates. **Requires explicit replay/evidence contract**.
- **E248 → E231/E265**: `forgotten_favor_honored` does not directly satisfy Toma route or ending qualification. **Requires replay-transfer mapping**.
- **E249 → E233/E250/E256**: no explicit marker on either choice. **Graph candidate only**.
- **E250 → systemic explanation / Second Founder**: this is an ending-support node, but the graph must define a durable `systemic_explanation_verified` or equivalent marker. **Currently under-specified**.
- **E251 → E252/E254/E255**: E251 has no durable marker. These are compound winter/food/local-governance predicates and require derived-state production.
- **E252 → E230/E241/E270**: no unique durable marker; relies on illness/Amara/civic predicates. **Needs canonical predicate mapping**.
- **E253 → E259/E267**: no explicit marker. **Needs border-crisis history/predicate contract**.
- **E254 → E237/E261**: no explicit marker. **Needs local-governance / civic route state**.
- **E255 → E261/E264**: no explicit marker. **Needs multi-crisis history marker**.
- **E256 → E257/E265**: no explicit marker. **Needs succession stress-test history**.
- **E257 → E260/E267**: no explicit marker. **Needs emergency-expiry constitutional state**.
- **E258 → E263**: no explicit marker. **Needs independent-budget institutional state**.
- **E259 → E227/E267**: no explicit marker. **Needs military-appeal constitutional state**.
- **E260 → E265**: no explicit marker. **Needs archive-law state**.
- **E261 → E262/E263/E264/E265**: direct on E261 A via `four_way_bargain`; E262 consumes it. Other edges require separate canonical coalition markers.
- **E262 → E263/E265**: E262 choices lack a durable marker. **Needs fifth-voice representation state**.
- **E263 → E265/E266**: no explicit marker. **Needs coalition-audit state**.
- **E265–E270**: these are endgame qualification nodes. They must consume explicit canonical ending predicates/history, not undocumented narrative labels.

## High-priority canonical gaps exposed by this pass

1. **Route predicates are overused without producers.** `institutional reform`, `regional courts`, `market oversight`, `veteran route`, `guild logistics route`, `border route`, `Amara route`, `coalition route`, `succession route`, `budget reform` and `archive reform` need explicit producer definitions.
2. **Many graph edges are thematic rather than causal.** They must not be encoded simply because the events are in the same chapter or concern the same faction.
3. **Evidence cardinality needs deterministic state.** `at least two procurement clues`, `three or more related clues`, and similar conditions require an auditable set of evidence markers and a deterministic count.
4. **Civic/food/border simultaneous pressure must be a derived predicate.** It must not be stored as an independent sixth resource.
5. **Replay-exclusive nodes need a strict metadata boundary.** Previous-run discoveries can unlock interpretation, but replay metadata must not accidentally satisfy ordinary current-run conditions.
6. **Ending nodes E265–E270 need a canonical qualification contract before any engine implementation.**

## Immediate blockers

- E35–E40 source ID collision remains unresolved.
- Canonical route producers are incomplete.
- E211–E270 graph edges are only partially source-proven.
- Compound predicates and evidence cardinality are not machine-defined.
- Ending qualification is not yet a production schema.
- Reachability cannot be honestly declared until the above is represented in machine-readable form.

## Gate result

**E211–E270 graph/catalog reconciliation: substantial source audit completed, production gate FAILED/PENDING.**

The correct next action is canonical producer extraction and predicate closure, not engine coding.
