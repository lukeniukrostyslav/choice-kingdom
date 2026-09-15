# Choice Kingdom — Producer / Consumer Audit E01–E070

Status: **SOURCE-LEVEL QA — NOT ENGINE INPUT**

This audit records authored durable outputs and explicit downstream hooks from the canonical E01–E70 sources. It deliberately does not invent missing runtime predicates.

## E01–E34

| Event | Authored durable outputs / hooks | QA note |
|---|---|---|
| E01 | `open_petition_hall`; `court_first`; delayed E07/E06 unlocks | first-turn root; delayed unlock needs exact due-turn |
| E02 | `emergency_decree_used`; `decree_investigation`; hidden-ledger unlock | later emergency and forgery chain consumers |
| E03 | `free_grain_imports`; grain-reserve depletion delayed effect | food reserve vs food-pressure predicate must remain distinct |
| E04 | `ledger_public_scrutiny`; `quiet_accounts` | public/secret ledger route |
| E05 | `emergency_guard_authority`; delayed procurement-fraud hook | military route + delayed consequence |
| E06 | `nobles_challenged`; temporary exemption delayed renewal | noble exception lifecycle needs exact source/due turn |
| E07 | `quiet_market_inquiry`; `ledger_fragment_a` delayed reveal | investigation source; delayed evidence identity |
| E08 | `merchant_charter`; delayed price-fixing risk; `competitive_market` | commercial route predicate needed |
| E09 | `audit_office`; `flexible_accounts` | major institutional fork |
| E10 | `central_command`; `local_command` | military command route |
| E11 | `noble_advisory_council` | noble constitutional route |
| E12 | `lantern_funded`; welfare-cut delayed winter effect | Amara route and food/winter contract |
| E13 | `toma_recruited`; `toma_rejected`; information-network unlock | information route identity |
| E14 | `market_reform`; `petty_tax_policy` | market-reform identity needed |
| E15 | `public_diplomacy`; private diplomatic branch | diplomatic route |
| E16 | joint-survey peaceful settlement hook | no durable flag authored; predicate must be explicit |
| E17 | hidden durability state; `quality_armaments`; delayed failure | delayed equipment identity/exactly-once |
| E18 | `merchant_charter` consumer; `public_bridge`; delayed toll escalation | infrastructure route |
| E19 | `guild_broken`; price-ceiling branch | food/market consequences need canonical state |
| E20 | `soldier_compensation` | Rowan/military welfare route |
| E21 | `ledger_fragment_a`; `evidence_destroyed` | evidence source and suppression identity |
| E22 | festival-held implicit state; delayed assassination risk | authored trigger/result needs explicit canonical flag if consumed |
| E23 | `ledger_public`; `ledger_secret`; delayed inquiry/legitimacy effects | ledger visibility route |
| E24 | `auditor_missing_public`; quiet-search branch | auditor disappearance route |
| E25 | `dock_route` trigger; stronger evidence delayed | investigation source identity |
| E26 | `seris_witness`; `seris_exposed` | Seris evidence route |
| E27 | decoy/scandal delayed branch | unresolved durable predicate if later consumed |
| E28 | `royal_forgery_proven`; `forgery_leverage`; delayed blackmail risk | explicit forgery producers for E099 |
| E29 | severe winter/granary outcome implicit; no durable flag | winter/food severity must be canonicalized |
| E30 | warehouse rescue vs sealed-district delayed arson route | later warehouse crisis consumers |
| E31 | `war_mobilization`; negotiated withdrawal hook | military/diplomatic escalation |
| E32 | `shared_crisis_command`; unresolved-crisis worsening | multi-crisis state needs canonical formula |
| E33 | `emergency_power`; `constitutional_limit`; delayed Iron Crown/Second Founder hooks | emergency lifecycle is major ending input |
| E34 | `people_heard`; relief-orders branch | civic route |

## E35–E60

| Event | Authored durable outputs / hooks | QA note |
|---|---|---|
| E35 | `emergency_expiry_announced`; `emergency_expiry_flexible` | emergency lifecycle |
| E36 | `mara_independent_mandate`; `mara_resigned` | must remain distinct from E95 `mara_independence` |
| E37 | `army_law_oath`; `army_crown_oath` | constitutional military route |
| E38 | `hereditary_seats_limited`; `hereditary_seats_rejected` | noble constitutional route |
| E39 | `guild_emergency_credit`; `civic_war_bonds`; delayed commercial leverage/repayment | economic power route |
| E40 | `local_relief_councils`; `central_relief`; delayed distribution effects | Amara institutional route |
| E41 | `crate_route_traced`; `customs_accused`; delayed intermediary/scapegoat | evidence route |
| E42 | `witness_protected`; `witness_public`; delayed testimony/credibility | witness lifecycle |
| E43 | `ledger_network_public`; `ledger_network_compromised` | systemic investigation route |
| E44 | `houses_self_reconcile`; `house_arms_restricted` | noble conflict route |
| E45 | `public_infrastructure_trust`; `infrastructure_concession` | later E126/E130/E181 consumers |
| E46 | `lawful_refusal_defended`; `lawful_refusal_punished` | military constitutional consequence |
| E47 | `constitution_first`; `crown_powers_first` | major ending input |
| E48 | `permanent_emergency_blocked`; `emergency_renewal_possible` | emergency lifecycle |
| E49 | `guild_political_representation`; `guild_political_exclusion` | later guild-influence consumers |
| E50 | `people_charter_endorsed`; `people_charter_delayed` | People's Charter ending input |
| E51 | `mutual_veto`; `crown_veto`; `public_renewal_rule` | constitutional architecture |
| E52 | `military_audit_final`; `military_patronage_final` | final military route |
| E53 | `full_ledger_published`; `verified_ledger_only` | final evidence/institution route |
| E54 | `seris_constitutional_office`; `nobility_equal_under_law` | noble constitutional route |
| E55 | `guild_books_submitted`; `guild_books_sealed` | early Ivo evidence; distinct from late E269 |
| E56 | `relief_guarantee`; `relief_discretion` | welfare constitutional route |
| E57 | `systemic_corruption_confirmed`; `mastermind_hunt`; delayed alliance risk | systemic-vs-mastermind fork |
| E58 | `final_emergency_invoked`; `final_emergency_refused` | ending/emergency state |
| E59 | `mandate_renewed_legally`; `succession_limited` | succession/legacy route |
| E60 | `all_voices_heard`; `crown_decides_alone` | replay/endgame identity |

## E61–E70

| Event | Authored output | QA note |
|---|---|---|
| E61 | Ending `STEWARD` | trigger must be derived from canonical institutions/security/emergency state |
| E62 | Ending `IRON_CROWN` | consumes emergency + military + crown-power history |
| E63 | Ending `GOLDEN_COMPACT` | consumes treasury + commercial leverage + guild political representation |
| E64 | Ending `PEOPLES_CHARTER` | consumes trust + charter + distributed institutions |
| E65 | Ending `BROKEN_DIADEM` | unresolved crises + collapsed relationships/institutions |
| E66 | Ending `QUIET_THRONE` | survival/withdrawal/low institutional ambition; derived predicate required |
| E67 | Ending `SECOND_FOUNDER` | constitutional limit + verified/cross-confirmed ledger + cooperation + redesign + no permanent emergency |
| E68 | historian epilogue | reads historical visibility/record state |
| E69 | infrastructure epilogue | consumes `public_infrastructure_trust` or `infrastructure_concession` |
| E70 | investigation epilogue | consumes investigation route/history |

## High-priority closure findings

1. **E01–E70 now have an exact source-level producer inventory**, but several authored prose concepts remain without machine-safe canonical predicates.
2. **Delayed effects** occur throughout the range. Before runtime, each needs source event, choice identity, due turn, cancellation/invalidation and exactly-once semantics.
3. **E28 is the authoritative upstream producer** for `royal_forgery_proven` / `forgery_leverage`; E099 can therefore consume these without inventing an upstream source.
4. **E45 is the upstream producer** for `public_infrastructure_trust` / `infrastructure_concession`; later bridge callbacks can consume these exact facts.
5. **E36 `mara_independent_mandate` and E95 `mara_independence` are semantically distinct** and must not be aliased.
6. **E55 and E269 are distinct evidence nodes**; the late E269 event must not overwrite the meaning of E55.
7. **E61–E67 are ending nodes, not ordinary flags.** Their predicates need a separate ending qualification contract.
8. `food prices rise`, `severe winter`, `strong relationships`, `early Act II`, `ledger chain active`, `late campaign`, `unresolved severe crisis`, and similar prose triggers require canonical derivation before production schema freeze.

## Gate

Source-level producer inventory: **PASS for E01–E70**.

Canonical trigger closure: **INCOMPLETE**.

Runtime reachability: **NOT VERIFIED**.

Production schema: **BLOCKED until canonical contracts freeze**.
