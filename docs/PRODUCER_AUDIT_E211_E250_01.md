# Choice Kingdom — Producer / Consumer Audit E211–E250

Status: SOURCE-LEVEL QA — NOT ENGINE INPUT

Purpose: record exact authored outputs and qualification boundaries for E211–E250 before production schema freeze. This pass does not invent missing producers and does not claim runtime reachability.

## E211–E215 — public institutions

| Event | Trigger | Authored durable outputs |
|---|---|---|
| E211 | `full_crown_audit_published` or `tax_transparency` | `public_ledger_room`, `ledger_summary_access` |
| E212 | `clerks_oath_public` | `clerk_protected`, `clerk_discipled` |
| E213 | `regional_courts` | no durable flag authored |
| E214 | institutional reform | `appointment_transparent`, `appointment_patronage` |
| E215 | `law_notices_public` | `free_law_copies`, `law_copy_fee` |

Finding: several triggers are upstream qualifications and are not produced by these events. `institutional reform` remains a prose/normalized concept until mapped to canonical predicate(s).

## E216–E220 — economic consequences

| Event | Trigger | Authored durable outputs |
|---|---|---|
| E216 | low gold + high reform spending | `treasury_shortfall_public`, `quiet_treasury_loan` |
| E217 | `quiet_treasury_loan` | `creditor_advisor` on B |
| E218 | food pressure | `grain_contract_inspected`, `grain_contract_rushed` |
| E219 | strong market oversight | `merchant_margin_disclosure`, `merchant_margin_tax` |
| E220 | `trade_risk_insurance` | `trade_guarantee_honored`, `trade_guarantee_challenged` |

Finding: E216's trigger is a derived predicate contract, not an event output. E218 food pressure and E219 market oversight remain dependent on canonical predicate definitions. E220 is a clean consumer of an authored upstream flag.

## E221–E225 — social pressure

| Event | Trigger | Authored durable outputs |
|---|---|---|
| E221 | `winter_rent_ceiling` or high civic trust | `tenant_panels` on A |
| E222 | veteran route | no durable flag authored |
| E223 | Amara route | `competence_medical_license`, `house_medical_license` |
| E224 | river compact | `river_safety_barriers` on A |
| E225 | severe food pressure | `bread_queue_heard`, `bread_queue_dispersed` |

Finding: E221/E222/E223 use route concepts that require canonical relationship/thread derivation. E225 consumes severe food pressure and does not establish food stability.

## E226–E231 — character pressure

| Event | Trigger | Authored durable outputs |
|---|---|---|
| E226 | Mara <= -1 or repeated executive overrides | `mara_independent_mandate`, `mara_resigned` |
| E227 | Rowan route + constitutional reform | `military_red_line` on A |
| E228 | noble constitutional route | no durable flag authored |
| E229 | Ivo >= 1 | `ivo_shortcut_closed`, `ivo_shortcut_used` |
| E230 | Amara >= 1 | no durable flag authored |
| E231 | Toma route + high information pressure | `toma_verification_first`, `toma_immediate_release` |

Finding: E226 is explicitly a late institutional-stress consequence and must not become a duplicate generic resignation event. `mara_independent_mandate` and `mara_resigned` already exist elsewhere, so their semantics require exact same-fact multi-producer handling or outcome identity must be clarified; do not treat duplicate names as new facts.

E227's `military_red_line` is a distinct downstream output and does not itself prove `thread.military_constitutional` unless the canonical thread contract explicitly says so.

## E232–E236 — investigation network

| Event | Trigger | Authored durable outputs |
|---|---|---|
| E232 | at least two procurement clues | `intermediary_chain_traced`, `visible_suppliers_charged` |
| E233 | forgery route | `seal_forensics`, `duplicate_seal_suppressed` |
| E234 | `payment_date_crosscheck` | `payment_pattern_public`, `payment_pattern_private` |
| E235 | `intermediary_chain_traced` | `middleman_family_archive` on B |
| E236 | witness route | no durable flag authored |

Finding: E232's "two procurement clues" must become an explicit evidence-cardinality predicate; it cannot be inferred from raw prose. E234 has a clean flag consumer relationship to an upstream `payment_date_crosscheck` marker. E236 produces no explicit durable marker in the authored source.

## E237–E241 — faction credibility

| Event | Trigger | Authored durable outputs |
|---|---|---|
| E237 | public accountability route | no durable flag authored |
| E238 | noble constitutional route | no durable flag authored |
| E239 | guild logistics route | no durable flag authored |
| E240 | border route | no durable flag authored |
| E241 | Amara route | no durable flag authored |

Finding: these are primarily callback/consequence nodes. Their route triggers cannot be used as proof of `pred.coalition_cooperation`, `pred.guild_influence_strong`, or other late composite predicates without explicit canonical rules.

## E242–E246 — delayed callbacks

| Event | Trigger | Authored durable outputs |
|---|---|---|
| E242 | prior noble exception + 6+ turns | no durable flag authored |
| E243 | public bridge investment + 5+ turns | no durable flag authored |
| E244 | flexible accounts + 5+ turns | `reconstructed_accounts` on B |
| E245 | compensation route + 6+ turns | no durable flag authored |
| E246 | price ceiling + 5+ turns | no durable flag authored |

Finding: these events prove the catalog contains delayed callback concepts, but their actual scheduling/identity/exactly-once behavior remains runtime work. E244's `reconstructed_accounts` is a new authored durable outcome and needs downstream inventory.

## E247–E250 — replay divergence

| Event | Trigger | Authored durable outputs |
|---|---|---|
| E247 | second-run information route | `alternate_suspect_tested` on A |
| E248 | replay callback | `forgotten_favor_honored` on A |
| E249 | archive route | no durable flag authored |
| E250 | three or more related clues | `pattern_anomaly_preserved` on A |

Finding: replay triggers are meta-state concepts and must remain separated from current-run state. E247 cannot become reachable merely because an ordinary current-run information flag exists; the production contract must require explicit replay metadata.

## Open P0/P1 boundaries exposed by this pass

1. `institutional reform` still needs canonical producer/derivation mapping.
2. `food_pressure` / `severe food pressure` require frozen derived-predicate definitions.
3. `strong market oversight` requires deterministic canonical derivation.
4. `veteran route`, `Amara route`, `Toma route`, `border route`, `noble constitutional route`, and `guild logistics route` require explicit thread/relationship predicates rather than prose triggers.
5. `two procurement clues` requires an evidence-cardinality contract.
6. E226 duplicate semantic outputs require exact same-fact producer treatment; no new meaning may be invented.
7. Delayed callbacks E242–E246 need source-choice identity, due turn, cancellation and exactly-once semantics in runtime.
8. Replay nodes E247–E250 require explicit `meta.*` gating.
9. E211–E250 still require downstream consumer inventory and reachability analysis before production schema freeze.

## Gate

SOURCE-LEVEL PASS for authored-output extraction in this range. Production schema: BLOCKED. Runtime reachability: NOT VERIFIED. Automated validator: intentionally NOT BUILT until canonical data contracts are frozen.
