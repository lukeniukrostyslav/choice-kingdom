# Choice Kingdom — Scenario QA S06 E211–E270 Inventory

Scope: frozen production candidates E211–E270. Source: `docs/EVENT_CATALOG_EXPANSION_211_270.md`, blob SHA `7feccad310906c4cdc2d0aae628e67a069b446b7`.

This is a direct source inventory and semantic QA pass, not proof of runtime reachability.

## E211–E225 — institutions, economy, social pressure

| Event | Trigger | Authored outputs / effects |
|---|---|---|
| E211 | `full_crown_audit_published` or `tax_transparency` | `public_ledger_room` / `ledger_summary_access` |
| E212 | `clerks_oath_public` | `clerk_protected` / discipline branch |
| E213 | `regional_courts` | trust/power; override branch |
| E214 | institutional reform | `appointment_transparent` / `appointment_patronage` |
| E215 | `law_notices_public` | `free_law_copies` / `law_copy_fee` |
| E216 | low gold + high reform spending | `treasury_shortfall_public` / `quiet_treasury_loan` |
| E217 | `quiet_treasury_loan` | creditor political-access branch / `creditor_advisor` |
| E218 | food pressure | `grain_contract_inspected` / `grain_contract_rushed` |
| E219 | strong market oversight | `merchant_margin_disclosure` / `merchant_margin_tax` |
| E220 | `trade_risk_insurance` | `trade_guarantee_honored` / `trade_guarantee_challenged` |
| E221 | `winter_rent_ceiling` or high civic trust | `tenant_panels` / private-dispute branch |
| E222 | veteran route | civil-service/veteran-preference branches |
| E223 | Amara route | `competence_medical_license` / `house_medical_license` |
| E224 | `river_compact` | `river_safety_barriers` / fine-town branch |
| E225 | severe food pressure | `bread_queue_heard` / `bread_queue_dispersed` |

## E226–E241 — character pressure and investigation network

| Event | Trigger | Authored outputs / contract |
|---|---|---|
| E226 | Mara <= -1 or repeated executive overrides | `mara_independent_mandate` / `mara_resigned`; explicitly late institutional-stress consequence, not E36 duplicate |
| E227 | Rowan route + constitutional reform | `military_red_line` / command-judgment branch |
| E228 | noble constitutional route | representation/veto branches |
| E229 | Ivo >= 1 | `ivo_shortcut_closed` / `ivo_shortcut_used` |
| E230 | Amara >= 1 | refusal-protection / compelled-certification branches |
| E231 | Toma route + high information pressure | `toma_verification_first` / `toma_immediate_release` |
| E232 | >=2 procurement clues | `intermediary_chain_traced` / `visible_suppliers_charged` |
| E233 | forgery route | `seal_forensics` / `duplicate_seal_suppressed` |
| E234 | `payment_date_crosscheck` | `payment_pattern_public` / `payment_pattern_private` |
| E235 | `intermediary_chain_traced` | archive search branches / `middleman_family_archive` |
| E236 | witness route | witness-protection/publication vs sealed-ledger branches |
| E237 | public accountability route | consultative-role vs dismissive branch |
| E238 | noble constitutional route | public/private credit branches |
| E239 | guild logistics route | public forecast vs independent forecast office |
| E240 | border route | local intelligence vs central intelligence |
| E241 | Amara route | early-warning authority vs official-confirmation branch |

## E242–E246 — delayed callbacks

| Event | Trigger / timing | Authored outputs |
|---|---|---|
| E242 | any prior noble exception, 6+ turns | close/extend precedent branches |
| E243 | public bridge investment, 5+ turns | public credit vs emergency-credit branch |
| E244 | flexible accounts, 5+ turns | admit accounting gap vs `reconstructed_accounts` |
| E245 | compensation route, 6+ turns | merit vs family-favor branch |
| E246 | price ceiling, 5+ turns | end on schedule vs extend branch |

These nodes have authored source identity, but exact delayed callback contracts remain S10 work: sourceEventId/sourceChoiceId/consequenceId, persistence, ordering, exactly-once identity and cancellation/supersession.

## E247–E250 — replay/information

E247 is explicitly second-run information; E248 is a replay callback. Exact `meta.*` producer/key closure remains S11 work. E249 and E250 are ordinary archive/investigation information unless a later canonical contract explicitly promotes them to meta-state. No implicit replay inheritance is permitted.

## E251–E260 — winter/crisis and constitutional stress

E251–E255 add state-pressure branches for transport, illness, border and simultaneous crises. E253 consumes border-crisis state and must not create `pred.border_crisis`. E255 is a multi-crisis prioritization node and must not manufacture missing crisis predicates.

E256–E260 are constitutional stress tests. Their outputs are direct choice effects unless explicitly named; none may be inferred as sufficient for `pred.constitutional_prepared_strong` without the independent upstream qualification contract.

## E261–E265 — cross-faction endgame

E261 `four_way_bargain` is a positive negotiation marker, not automatically `pred.coalition_cooperation`. E262 adds a fifth voice but does not itself prove coalition cooperation. E263 publishes coalition costs; E264 is a failure/withdrawal pressure node; E265 is a positive final-text agreement. Deterministic coalition qualification remains an S09/S11 concern and must use independent prerequisites rather than a single bargain marker.

## E266–E270 — final personal/evidence nodes

E266–E269 are consequence-stage character/evidence nodes. E269 explicitly distinguishes itself from E55 and must remain a separate late-stage evidence handoff. E270 combines Amara and Toma accounts; it must not be treated as an automatic systemic-explanation or final-charter qualification producer.

## S06 semantic QA findings

1. **Unnamed state effects:** several E211–E270 choices alter trust/power/security/relationships without named flags. This is acceptable only if the production schema models them as direct numeric state mutations and no downstream predicate silently consumes an unnamed fact.
2. **E226 duplicate boundary is explicit:** E226 is a late institutional-stress consequence and must not be canonicalized as a duplicate of E36's initial Mara constitutional scene.
3. **E253 hard negative:** consuming border-crisis state does not create it. The producer remains E271-A.
4. **E261 coalition boundary:** `four_way_bargain` is not equivalent to `pred.coalition_cooperation`; qualification requires independent authored conditions.
5. **E265 positive coalition candidate:** final agreement is a strong candidate input, but deterministic predicate qualification and failure precedence remain open.
6. **E269 duplicate boundary is explicit:** E269 is distinct from E55 and must retain its late consequence-stage identity.
7. **E270 evidence boundary:** combining two witnesses does not by itself satisfy systemic evidence or final charter prerequisites.
8. **Delayed nodes E242–E246:** source identity is present, but lifecycle/exactly-once semantics remain unclosed.
9. **Replay E247–E248:** replay awareness is authored, but no implicit `meta.*` producer/key may be invented.
10. **No global Scenario QA increase claimed:** this batch is not sufficient to close exhaustive global producer/consumer, predicate-cycle, ending, replay, or reachability gates.

## S06 status
Direct source inventory for E211–E270 is complete and semantic hard-negative boundaries are recorded.

**S06: 50% / IN PROGRESS.**
