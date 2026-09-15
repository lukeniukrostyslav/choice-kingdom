# Choice Kingdom — Expansion Events E211–E270

These are authored production candidates that deepen causal variety before engine implementation. They are intentionally subject to later canonical graph, contradiction, reachability and pacing QA.

## Public institutions

### E211 — The Public Ledger Room
**Trigger:** `full_crown_audit_published` or `tax_transparency`.
Citizens ask to inspect the evidence behind published figures.
- **A — Open a reading room:** +5 trust, -2 power; `public_ledger_room`.
- **B — Publish summaries only:** +2 trust, +2 power; `ledger_summary_access`.

### E212 — The Clerk Who Refused
**Trigger:** `clerks_oath_public`.
A clerk refuses an order that contradicts the new audit rules.
- **A — Back the clerk:** +5 trust, -2 power; `clerk_protected`.
- **B — Discipline the clerk:** +3 power, -5 trust; `clerk_discipled`.

### E213 — The Appeal Court
**Trigger:** `regional_courts`.
A noble appeals a local ruling and asks the Crown to intervene.
- **A — Let the court decide:** +5 trust, -2 power.
- **B — Override for stability:** +4 power, -5 trust; `royal_appeal_override`.

### E214 — The Public Appointment
**Trigger:** institutional reform.
The first independent office appointment is contested.
- **A — Publish qualifications and process:** +4 trust, -2 power; `appointment_transparent`.
- **B — Appoint a trusted ally:** +4 power, -4 trust; `appointment_patronage`.

### E215 — The Rulebook Copy
**Trigger:** `law_notices_public`.
People ask whether local copies of law should be free.
- **A — Make them free:** -2 gold, +4 trust; `free_law_copies`.
- **B — Charge a small fee:** +2 gold, -2 trust; `law_copy_fee`.

## Economic consequences

### E216 — The Empty Purse
**Trigger:** low gold + high reform spending.
The treasury cannot fund every promise.
- **A — Publish the shortfall:** -2 power, +5 trust; `treasury_shortfall_public`.
- **B — Borrow quietly:** +6 gold now, -4 trust later; `quiet_treasury_loan`.

### E217 — The Creditor's Seat
**Trigger:** `quiet_treasury_loan`.
A creditor asks for a permanent advisory seat.
- **A — Refuse political access:** +4 trust, -2 gold pressure.
- **B — Grant the seat:** +4 gold, -5 trust; `creditor_advisor`.

### E218 — The Grain Contract
**Trigger:** food pressure.
A supplier offers cheap grain with a suspiciously short contract.
- **A — Require independent inspection:** +4 trust, -2 gold; `grain_contract_inspected`.
- **B — Sign immediately:** +6 gold-equivalent relief, -4 trust; `grain_contract_rushed`.

### E219 — The Honest Price
**Trigger:** strong market oversight.
Merchants publish their margins voluntarily.
- **A — Reward disclosure:** -2 gold, +5 trust; `merchant_margin_disclosure`.
- **B — Tax the margins:** +5 gold, -3 trust; `merchant_margin_tax`.

### E220 — The Failed Insurance
**Trigger:** `trade_risk_insurance`.
A storm destroys a convoy covered by the Crown.
- **A — Honor the guarantee:** -7 gold, +5 trust; `trade_guarantee_honored`.
- **B — Challenge the claim:** +3 gold, -5 trust; `trade_guarantee_challenged`.

## Social pressure

### E221 — The Tenant Council
**Trigger:** `winter_rent_ceiling` or high civic trust.
Tenants ask for representation in disputes with landlords.
- **A — Create local tenant panels:** +5 trust, -2 power; `tenant_panels`.
- **B — Keep disputes private:** +2 power, -3 trust.

### E222 — The Veteran's Daughter
**Trigger:** veteran route.
A veteran's daughter asks why military service is the only respected path to advancement.
- **A — Expand civil service access:** +4 trust, -2 Rowan.
- **B — Preserve veteran preference:** +3 Rowan, +2 security, -3 trust.

### E223 — The Healer's Apprentice
**Trigger:** Amara route.
A healer asks to practice without belonging to a noble house.
- **A — License by competence:** +5 trust, +2 Amara; `competence_medical_license`.
- **B — Require house sponsorship:** +3 power, -4 trust; `house_medical_license`.

### E224 — The River Children
**Trigger:** river compact.
Children are injured near an unguarded bridge.
- **A — Fund safety barriers:** -3 gold, +5 trust; `river_safety_barriers`.
- **B — Fine the town:** +2 gold, -4 trust.

### E225 — The Bread Queue
**Trigger:** severe food pressure.
A queue becomes a political demonstration.
- **A — Listen publicly:** +5 trust, -2 power; `bread_queue_heard`.
- **B — Disperse it:** +4 security, -6 trust; `bread_queue_dispersed`.

## Character pressure

### E226 — Mara's Final Resignation Test
**Trigger:** Mara <= -1 or repeated executive overrides.
Late in the constitutional struggle, Mara offers to resign rather than legitimize a system repeatedly altered by executive intervention. This is a consequence test of accumulated institutional strain, not a second generic resignation scene.
- **A — Give her independent authority:** -2 power, +4 Mara, +4 trust; `mara_independent_mandate`.
- **B — Accept resignation:** +3 power, -5 Mara; `mara_resigned`.

**QA distinction:** E226 is retained only as a late institutional-stress consequence. Its presentation must reference accumulated executive overrides or comparable prior institutional strain; it must not replay E36's early constitutional introduction.

### E227 — Rowan's Line
**Trigger:** Rowan route + constitutional reform.
Rowan says soldiers need a clear line they cannot cross.
- **A — Write the line into law:** +5 trust, -2 Rowan; `military_red_line`.
- **B — Leave it to command judgment:** +4 security, +3 Rowan, -5 trust.

### E228 — Seris and the Veto
**Trigger:** noble constitutional route.
Seris admits that old houses fear becoming irrelevant.
- **A — Give them representation without veto:** +4 Seris, +4 trust.
- **B — Give limited veto:** +3 Seris, +3 power, -4 trust.

### E229 — Ivo's Last Shortcut
**Trigger:** Ivo >= 1.
Ivo offers one final loophole that could solve a fiscal emergency.
- **A — Close the loophole publicly:** +5 trust, -3 Ivo; `ivo_shortcut_closed`.
- **B — Use it once:** +7 gold, -5 trust; `ivo_shortcut_used`.

### E230 — Amara's Refusal
**Trigger:** Amara >= 1.
Amara refuses to certify a military operation that would endanger patients.
- **A — Protect her refusal:** +5 trust, +3 Amara, -2 security.
- **B — Compel certification:** +4 security, -6 trust, -3 Amara.

### E231 — Toma's Final Price
**Trigger:** Toma route + high information pressure.
Toma has evidence that could destroy a powerful ally.
- **A — Verify before release:** +5 power, +3 Toma; `toma_verification_first`.
- **B — Release immediately:** +6 trust, -4 reputation; `toma_immediate_release`.

## Investigation network

### E232 — The Procurement Chain
**Trigger:** at least two procurement clues.
Investigators discover that three suppliers changed names but retained the same intermediaries.
- **A — Follow the intermediaries:** +5 power; `intermediary_chain_traced`.
- **B — Charge the visible suppliers:** +4 security, -3 trust; `visible_suppliers_charged`.

### E233 — The Duplicate Seal
**Trigger:** forgery route.
Two official seals appear on documents issued months apart.
- **A — Compare ink and dates:** +4 power, +2 reputation; `seal_forensics`.
- **B — Destroy the weaker document:** +3 power, -4 trust; `duplicate_seal_suppressed`.

### E234 — The Payment Calendar
**Trigger:** `payment_date_crosscheck`.
Payments cluster immediately before emergency decrees.
- **A — Publish the pattern:** +5 trust, -2 reputation; `payment_pattern_public`.
- **B — Investigate privately:** +4 power; `payment_pattern_private`.

### E235 — The Missing Middleman
**Trigger:** `intermediary_chain_traced`.
The person connecting two factions disappeared years ago.
- **A — Search old tax records:** +3 power, -2 gold.
- **B — Search family archives:** +3 power, +1 Seris; `middleman_family_archive`.

### E236 — The Witness Ledger
**Trigger:** witness route.
A ledger records payments to people who testified under emergency law.
- **A — Protect witnesses and publish payments:** +5 trust, -3 power.
- **B — Seal the ledger:** +4 power, -5 trust.

## Faction credibility

### E237 — The Commons Were Right
**Trigger:** public accountability route.
Commons representatives correctly predicted a tax backlash.
- **A — Give them a permanent consultative role:** +5 trust, -2 power.
- **B — Thank them and move on:** +2 power, -2 trust.

### E238 — The Houses Were Right
**Trigger:** noble constitutional route.
A noble warning prevents a confiscation that would have triggered violence.
- **A — Credit the warning publicly:** +3 Seris, +4 trust.
- **B — Keep the credit private:** +3 power, -2 trust.

### E239 — The Guilds Were Right
**Trigger:** guild logistics route.
Guild forecasting correctly predicts a shortage.
- **A — Use guild forecasts publicly:** +4 Ivo, +4 trust.
- **B — Build an independent forecast office:** -3 gold, +5 trust.

### E240 — The Border Was Right
**Trigger:** border route.
A border commander correctly identifies a threat dismissed by the capital.
- **A — Expand local intelligence:** +5 security, +2 Rowan.
- **B — Centralize intelligence:** +4 power, -2 Rowan.

### E241 — The Lanterns Were Right
**Trigger:** Amara route.
Healers detect a crisis before officials do.
- **A — Give them early-warning authority:** +5 trust, +3 Amara.
- **B — Require official confirmation first:** +3 power, -3 Amara.

## Delayed callbacks

### E242 — The Renewed Exception
**Trigger:** any prior noble exception, 6+ turns later.
A new family cites precedent.
- **A — Close precedent:** +5 trust, -3 Seris.
- **B — Extend precedent:** +3 Seris, +2 power, -5 trust.

### E243 — The Old Bridge
**Trigger:** public bridge investment, 5+ turns later.
The bridge saves a convoy during a storm.
- **A — Publicly credit the investment:** +5 trust.
- **B — Claim emergency leadership credit:** +3 power, -3 trust.

### E244 — The Audit Comes Due
**Trigger:** flexible accounts, 5+ turns later.
A missing accounting trail becomes impossible to reconstruct.
- **A — Admit the gap:** +3 trust, -2 power.
- **B — Reconstruct a plausible account:** +3 power, -5 trust; `reconstructed_accounts`.

### E245 — The Soldier's Son Returns
**Trigger:** compensation route, 6+ turns later.
The compensated family member joins the civil service.
- **A — Let merit decide advancement:** +4 trust.
- **B — Favor the family:** +2 Rowan, -3 trust.

### E246 — The Price Ceiling Memory
**Trigger:** price ceiling, 5+ turns later.
Merchants remember whether the temporary measure ended on time.
- **A — End it on schedule:** +4 trust, +2 Ivo.
- **B — Extend it:** +3 trust now, -4 Ivo later.

## Replay divergence

### E247 — The Different Suspect
**Trigger:** second-run information route.
A different official becomes plausible when an earlier clue is interpreted differently.
- **A — Test the alternative:** +5 power; `alternate_suspect_tested`.
- **B — Stay with the original theory:** +3 power.

### E248 — The Forgotten Favor
**Trigger:** replay callback.
A minor favor from early in the reign becomes relevant to a late witness.
- **A — Honor it:** +3 trust, +2 reputation; `forgotten_favor_honored`.
- **B — Treat it as irrelevant:** +2 power, -2 trust.

### E249 — The Second Map
**Trigger:** archive route.
A map reveals that emergency supply routes were deliberately rerouted.
- **A — Compare against old decrees:** +5 power.
- **B — Secure the map:** +3 security, -2 trust.

### E250 — The Pattern Break
**Trigger:** three or more related clues.
One event does not fit the apparent system.
- **A — Preserve the anomaly:** +4 power, +2 reputation; `pattern_anomaly_preserved`.
- **B — Force it into the existing theory:** +3 power, -3 trust.

## Winter and crisis

### E251 — The Frozen Treasury Road
**Trigger:** winter + low transport.
A treasury shipment cannot reach the capital.
- **A — Prioritize food shipments:** -4 gold, +5 trust.
- **B — Prioritize treasury security:** +4 power, -4 trust.

### E252 — The Hospital Bell
**Trigger:** illness + Amara route.
A hospital rings its emergency bell for supplies.
- **A — Divert a royal convoy:** -4 gold, +5 trust.
- **B — Wait for scheduled delivery:** +2 power, -5 trust.

### E253 — The Border Fire
**Trigger:** border crisis.
A warning fire is mistaken for an invasion signal.
- **A — Verify before mobilizing:** -2 security, +5 reputation.
- **B — Mobilize immediately:** +6 security, -5 gold, -3 reputation.

### E254 — The Grain Warehouse Vote
**Trigger:** food crisis + local governance.
A town votes to open a private warehouse.
- **A — Respect the vote:** +5 trust, -2 power.
- **B — Seize the warehouse:** +5 security, -6 trust.

### E255 — The Three-Crisis Budget
**Trigger:** simultaneous food, border and civic pressure.
Only two crises can be fully funded.
- **A — Publish the prioritization:** +4 trust, -2 power.
- **B — Decide secretly:** +5 power, -5 trust.

## Constitutional stress tests

### E256 — The Bad Successor
**Trigger:** succession route.
The council imagines the throne occupied by a ruler less trustworthy than the current player.
- **A — Limit the successor:** +6 trust, -4 power.
- **B — Trust the office:** +5 power, -5 trust.

### E257 — The Emergency Clock
**Trigger:** emergency powers.
A legal emergency must have an expiry date.
- **A — Automatic expiry:** +6 trust, -3 power.
- **B — Renewal by executive order:** +5 power, -6 trust.

### E258 — The Independent Purse
**Trigger:** budget reform.
Auditors ask whether their office should control its own budget.
- **A — Independent budget:** +5 trust, -2 power.
- **B — Crown-controlled budget:** +4 power, -4 trust.

### E259 — The Military Appeal
**Trigger:** army constitutional route.
A soldier appeals an unlawful order.
- **A — Independent review:** +6 trust, -3 Rowan.
- **B — Command review:** +4 security, -5 trust.

### E260 — The Public Archive Law
**Trigger:** archive reform.
Citizens request a legal right to historical records after a fixed period.
- **A — Create access law:** +6 trust, -3 power.
- **B — Keep executive classification:** +5 power, -5 trust.

## Cross-faction endgame

### E261 — The Four-Way Bargain
**Trigger:** at least four faction routes.
Commons, Houses, Guilds and Border each demand one concession.
- **A — Accept a balanced package:** -4 power, +7 trust; `four_way_bargain`.
- **B — Choose two strongest factions:** +4 power, -6 trust; `two_faction_bargain`.

### E262 — The Fifth Voice
**Trigger:** `four_way_bargain`.
Lanterns or independent civic voices demand representation.
- **A — Add them:** +5 trust, -2 power.
- **B — Keep the original four:** +3 power, -4 trust.

### E263 — The Coalition Audit
**Trigger:** coalition route.
Every faction's promised benefit is calculated publicly.
- **A — Publish the costs:** +6 trust, -3 power.
- **B — Publish only benefits:** +3 power, -5 trust.

### E264 — The Coalition Breaks
**Trigger:** low coalition trust.
One faction threatens to withdraw before ratification.
- **A — Renegotiate:** -3 power, +5 trust.
- **B — Replace the faction with executive authority:** +5 power, -7 trust.

### E265 — The Coalition Holds
**Trigger:** high coalition trust.
The coalition agrees to a final text.
- **A — Make the agreement public:** +6 trust.
- **B — Keep negotiation details private:** +3 power, -3 trust.

## Final-act personal choices

### E266 — Mara's Last Report
**Trigger:** Mara active.
Mara submits a report that criticizes the ruler personally.
- **A — Publish it unchanged:** +6 trust, +2 Mara.
- **B — Edit it:** +4 power, -5 trust, -2 Mara.

### E267 — Rowan's Last Order
**Trigger:** Rowan active.
Rowan receives an order he believes is lawful but dangerous.
- **A — Let him refuse on constitutional grounds:** +5 trust, -3 Rowan.
- **B — Require obedience:** +5 security, -6 trust.

### E268 — Seris's Last Bargain
**Trigger:** Seris active.
Seris offers to persuade the Houses if the Crown protects legitimate property rights.
- **A — Protect rights equally:** +4 trust, +3 Seris.
- **B — Grant house-specific protection:** +4 Seris, -5 trust.

### E269 — Ivo's Late Account
**Trigger:** Ivo active.
Late in the endgame, Ivo hands over a private account showing where emergency profits went. Unlike E55's earlier ledger-disclosure decision, this is a consequence-stage evidence handoff that tests what the accumulated commercial route has produced.
- **A — Preserve and publish it:** +6 trust, -2 Ivo.
- **B — Use it as leverage:** +5 power, +2 Ivo, -5 trust.

**QA distinction:** E269 is the late endgame consequence/evidence node. It must never be presented or referenced as a duplicate of E55, which remains the earlier guild-books disclosure node.

### E270 — Amara and Toma at Dawn
**Trigger:** Amara and Toma both active.
A healer and a courier arrive with two different accounts of the final crisis; neither is complete alone.
- **A — Combine both accounts before acting:** +6 power, +5 trust; `dual_witness_account`.
- **B — Choose the more politically useful account:** +5 power, -6 trust; `single_witness_account`.

## QA note

E211–E270 are authored nodes, not verified runtime content. They must be reconciled with E01–E210, assigned canonical triggers/turn windows, checked for state conflicts and dead ends, and simulated before any event-count percentage is treated as production completion.

## Canonical bridge — E271 (producer node, post-catalog extension)

### E271 — The Border Council Alarm
**Trigger:** `thread.border` active + `pred.border_tension` + frontier warning infrastructure (`frontier_military_watch` or `civilian_signal_authority`).

The council receives corroborated reports that the frontier threat has crossed from tension into an active crisis. This node is deliberately separate from E139, E171, E195 and E253: those events provide warning, legal/military responses, or crisis consumption, but none of them silently creates the crisis predicate.

- **A — Declare a formal border crisis**
  - Immediate: `border_crisis_declared = true`.
  - Clears: `border_crisis_resolved = false`.
  - Durable state: `thread.border_crisis = active`.
  - Consumer unlock: `pred.border_crisis` becomes eligible for E195/E253/E255 and later crisis logic.

- **B — Verify and de-escalate before declaring**
  - Immediate: `border_crisis_resolved = true`.
  - Durable state: `thread.border_crisis = resolved_without_declaration`.
  - This choice must not satisfy `pred.border_crisis`.

### E271 QA contract
E271 is an authored producer bridge, not a generic graph edge. `pred.border_crisis` is true only after E271-A and while no later canonical resolution marker invalidates it. E271-B is an explicit non-crisis branch. A later authored event may resolve an active crisis, but neither E195 nor E253 may create one merely by being reached.

## QA note

E211–E271 are authored nodes, not verified runtime content. They must be reconciled with E01–E210, assigned canonical triggers/turn windows, checked for state conflicts and dead ends, and simulated before any event-count percentage is treated as production completion.
