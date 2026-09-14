# Choice Kingdom — Event Expansion E71–E110

This file is an authored expansion layer around the E01–E70 spine. It is part of the narrative source set and must be merged into the canonical event catalog after narrative QA. These nodes are designed to add causal depth, ordinary-life texture, faction legitimacy, character callbacks, and replay divergence rather than filler.

## Act I–II expansion: consequences of the first crown

### E71 — The Baker's Ledger
**Trigger:** E03 completed; any grain policy.

A baker brings two ledgers: one official, one kept by hand after prices changed.

**A — Compensate honest bakers**
- Immediate: -2 gold, +2 trust.
- Flag: `baker_relief`.
- Later: increases cooperation during rationing.

**B — Enforce the official price**
- Immediate: +2 power, -2 trust.
- Flag: `price_enforcement`.
- Later: shortages are less visible but black-market pressure rises.

### E72 — The Empty Granary Clerk
**Trigger:** `open_petition_hall` or `baker_relief`.

A junior clerk admits that reserve counts are copied rather than measured.

**A — Protect the whistleblower**
- +2 Mara, +2 trust; flag `clerk_protected`.
- Later audit evidence becomes available.

**B — Discipline the clerk for bypassing procedure**
- +2 power, -2 Mara; flag `clerk_silenced`.
- Later a missing inventory trail appears.

### E73 — Three Stamps
**Trigger:** `audit_office`.

Mara discovers three officials can approve the same emergency purchase, making responsibility impossible to trace.

**A — Require named responsibility**
- -2 power, +3 Mara, flag `named_authority`.

**B — Keep overlapping authority during emergencies**
- +3 power, flag `overlapping_authority`.
- Delayed: faster response but weaker accountability.

### E74 — A Noble's Debt
**Trigger:** `nobles_challenged` or temporary exemption.

A minor noble admits his house cannot survive a sudden tax reform without selling ancestral land.

**A — Offer a gradual transition**
- -2 gold, +1 Seris, +1 trust, flag `noble_transition`.

**B — Enforce the new tax immediately**
- +2 power, +3 trust, -2 Seris, flag `hard_tax_reform`.

### E75 — The River Widow
**Trigger:** `public_bridge` or `merchant_charter`.

A ferryman's widow says bridge policy has doubled her family's travel costs.

**A — Create a small public crossing fund**
- -2 gold, +3 trust, flag `crossing_fund`.

**B — Tell the guild to solve it**
- +2 Ivo, +1 power; flag `guild_social_contract`.
- Later the guild can claim public legitimacy for itself.

### E76 — Umbrella Day
**Trigger:** `petty_tax_policy`.

Rain turns the ruler's umbrella tax into a citywide joke; merchants sell deliberately oversized umbrellas.

**A — Repeal it publicly and laugh**
- -1 power, +3 trust, flag `umbrella_repealed`.
- Later Ivo can use the incident to humanize the Crown.

**B — Defend the tax**
- +2 gold, -2 trust, flag `umbrella_defended`.
- Later opposition uses it as shorthand for arbitrary rule.

### E77 — The Guard's Meal
**Trigger:** `central_command` or `emergency_guard_authority`.

Soldiers receive inferior rations while officers eat well.

**A — Eat the same ration publicly**
- -2 gold, +3 Rowan, +2 trust, flag `shared_rations`.

**B — Leave discipline to commanders**
- +2 power, -2 Rowan, flag `command_discipline`.

### E78 — The Quiet Cartographer
**Trigger:** `public_diplomacy` or joint survey.

A Veyran cartographer offers an old map showing the disputed border was once jointly administered.

**A — Preserve it as evidence**
- +2 reputation, flag `old_border_map`.
- Later enables a non-military settlement.

**B — Hide it until negotiations**
- +2 power, flag `map_secret`.
- Later the Crown can surprise both factions, but exposure damages trust.

### E79 — The Guild Apprentice
**Trigger:** Ivo >= 1.

Young guild workers ask why guild prosperity never reaches apprentices.

**A — Support an apprenticeship charter**
- -2 gold, +3 trust, -1 Ivo, flag `guild_apprenticeship`.

**B — Leave wages to guild negotiation**
- +2 Ivo, +1 gold, flag `guild_autonomy`.

### E80 — The Lantern Bell
**Trigger:** Amara >= 1.

House of Lanterns asks for a bell tower to coordinate winter relief.

**A — Fund it**
- -3 gold, +2 trust, +1 Amara, flag `lantern_network`.

**B — Require civic volunteers to fund it**
- +2 power, +1 trust, flag `volunteer_relief`.

## Act II expansion: information becomes political capital

### E81 — The Second Ledger
**Trigger:** `audit_office` + `ledger_public_scrutiny`.

A second set of emergency accounts contains identical numbers written in a different hand.

**A — Compare handwriting publicly**
- +4 trust, -2 reputation, flag `handwriting_public`.

**B — Preserve the sample secretly**
- +2 power, flag `handwriting_secret`.
- Later investigation gains an alternative proof route.

### E82 — Toma's Price
**Trigger:** `toma_recruited`.

Toma refuses to name a source unless the Crown protects the source's family.

**A — Promise protection**
- -2 power, +2 Toma, flag `source_protection`.
- Delayed: unlocks a deeper ledger witness.

**B — Demand the name first**
- +2 power, -2 Toma, flag `source_demanded`.
- Delayed: information arrives faster but less reliably.

### E83 — Seris's Cousin
**Trigger:** Seris >= 1.

Seris's cousin asks whether reform means confiscation.

**A — Explain limits in writing**
- +2 Seris, +1 trust, flag `reform_guarantee`.

**B — Refuse guarantees**
- +2 power, -2 Seris, flag `reform_uncertainty`.

### E84 — The Honest Smuggler
**Trigger:** `quiet_market_inquiry` or Toma route.

A smuggler offers proof that some illegal shipments are medicine, not stolen grain.

**A — Separate humanitarian smuggling from profiteering**
- +3 trust, +1 Toma, flag `humanitarian_smuggling`.

**B — Ban all smuggling**
- +3 security, -3 trust, flag `total_smuggling_ban`.

### E85 — The Auditor's Wife
**Trigger:** `audit_office` + missing auditor.

The missing auditor's wife asks whether the Crown actually wants him found.

**A — Tell her the truth**
- -1 power, +3 trust, flag `auditor_family_trust`.
- Delayed: she provides a private letter.

**B — Give a reassuring official statement**
- +2 power, flag `official_reassurance`.
- If the auditor is later found alive, the family remembers the lie.

### E86 — The Price of Quiet
**Trigger:** `quiet_accounts` or `ledger_secret`.

A courtier offers to make the discrepancy disappear permanently.

**A — Pay for silence**
- -5 gold, +3 power, flag `paid_silence`.
- Delayed: creates blackmail exposure.

**B — Refuse and record the offer**
- -2 power, +3 trust, flag `silence_recorded`.

### E87 — The Bridge Engineer
**Trigger:** `public_bridge`.

The engineer warns that a cheaper repair will fail during winter floods.

**A — Pay for the durable repair**
- -5 gold, +2 security, flag `durable_bridge`.
- Later protects supply routes.

**B — Patch it cheaply**
- -1 gold, +1 power, flag `cheap_bridge_repair`.
- Delayed: bridge failure can isolate a district.

### E88 — The Captain's Map
**Trigger:** Rowan >= 2.

Rowan presents a private map showing patrol gaps caused by local commanders.

**A — Publish the gaps and fix them**
- -2 security now, +3 Rowan, flag `patrol_transparency`.

**B — Keep the map secret**
- +2 security, +2 power, flag `patrol_secret`.

### E89 — The House Vote
**Trigger:** `noble_advisory_council` or `noble_transition`.

Nobles propose a constitutional council with seats weighted by land.

**A — Accept equal advisory votes**
- +3 trust, -2 Seris, flag `equal_advisory_vote`.

**B — Accept weighted representation**
- +2 Seris, +2 power, flag `land_weighted_council`.

### E90 — The Healer's Exception
**Trigger:** `lantern_funded` or `lantern_network`.

A noble asks Amara to prioritize a wounded heir over common patients.

**A — Treat by medical need**
- +3 Amara, +2 trust, flag `medical_neutrality`.

**B — Prioritize the heir**
- +2 Seris, +1 power, -3 Amara, flag `noble_medical_priority`.

## Act III expansion: the ledger becomes a living network

### E91 — The Missing Page
**Trigger:** any two ledger clues.

One page is missing from every surviving copy.

**A — Search the archive**
- -1 power, flag `archive_search`.
- Delayed: reveals a payment destination.

**B — Ask Seris's family archivist**
- +1 Seris, flag `house_archive_request`.
- Delayed: reveals who benefited socially, not just financially.

### E92 — The Night Ferry
**Trigger:** `old_border_map` or Toma route.

A ferry crosses after curfew carrying sealed diplomatic trunks.

**A — Inspect it**
- +3 security, risk diplomatic damage, flag `night_ferry_inspected`.

**B — Let it pass under observation**
- -1 security, +2 reputation, flag `night_ferry_observed`.
- Delayed: identifies a network participant.

### E93 — The Clerk Who Counted Twice
**Trigger:** `archive_search`.

A clerk admits he was paid to duplicate invoices, but says the payer was not the person the Crown suspects.

**A — Offer immunity for the full chain**
- +2 power, flag `duplicate_invoice_witness`.

**B — Arrest him immediately**
- +3 security, flag `duplicate_invoice_arrest`.
- Delayed: another witness disappears.

### E94 — Ivo's Books
**Trigger:** Ivo >= 2 + ledger chain.

Ivo opens his books and proves one profitable contract was legal, while another was deliberately structured to look legal.

**A — Protect the legal trade and prosecute the scheme**
- +3 Ivo, +4 trust, flag `merchant_books_open`.

**B — Seize everything**
- +3 gold, -3 Ivo, -2 trust, flag `guild_confiscation`.

### E95 — Mara's Resignation Letter
**Trigger:** `flexible_accounts` + failed audit route.

Mara drafts a resignation letter, saying she cannot be the Crown's excuse for opaque rule.

**A — Give her independent authority**
- -2 power, +3 Mara, flag `mara_independence`.

**B — Ask her to stay loyal**
- +2 power, -2 Mara, flag `mara_personal_loyalty`.

### E96 — Rowan's Oath
**Trigger:** `emergency_guard_authority`.

Rowan asks whether his emergency oath binds him to the ruler personally or to Avelune's laws.

**A — Law first**
- -2 power, +3 Rowan, flag `law_bound_guard`.

**B — Crown first**
- +4 power, +2 Rowan, flag `personal_guard_oath`.

### E97 — Seris Names Three Houses
**Trigger:** `seris_witness` or `seris_exposed`.

Seris identifies three houses that profited, but warns that one has already reformed.

**A — Investigate all three equally**
- +3 trust, -1 power, flag `equal_house_inquiry`.

**B — Punish only the worst**
- +2 power, +2 Seris, flag `selective_house_punishment`.

### E98 — The Source Protection Vote
**Trigger:** `source_protection`.

Council must decide whether witness identities can be sealed.

**A — Create protected testimony rules**
- -2 power, +3 trust, flag `protected_testimony`.

**B — Require open testimony**
- +2 reputation, +2 power, flag `open_testimony`.
- Delayed: fewer witnesses come forward.

### E99 — The Forgery's Shadow
**Trigger:** `royal_forgery_proven` or `forgery_leverage`.

A surviving court seal appears on a modern document.

**A — Publish the seal comparison**
- +4 trust, -2 power, flag `seal_comparison_public`.

**B — Use it to pressure a suspect**
- +3 power, flag `seal_pressure`.
- Delayed: suspect can claim coercion.

### E100 — The Ledger's True Purpose
**Trigger:** at least three independent evidence routes.

The investigation reveals the system was not created by one mastermind. It became corrupt because emergency offices rewarded temporary authority, favors, and untraceable procurement.

**A — Frame it as a systemic failure**
- +4 trust, flag `systemic_truth_public`.

**B — Frame it as a conspiracy**
- +5 power, flag `conspiracy_narrative`.
- Delayed: easier political control, harder institutional reform.

## Act IV expansion: winter and ordinary people

### E101 — The Frozen Canal
**Trigger:** winter + bridge or river route.

The canal freezes and supply barges stop.

**A — Break the ice with military crews**
- -3 gold, +3 security, flag `military_icebreakers`.

**B — Hire guild crews**
- -4 gold, +2 Ivo, flag `guild_icebreakers`.
- If guild relationship is hostile, they demand concessions.

### E102 — The Soup Line
**Trigger:** trust < 60 or severe winter.

A soup kitchen has more people than bowls.

**A — Open palace kitchens**
- -4 gold, +5 trust, flag `palace_kitchens`.

**B — Issue vouchers to merchants**
- -2 gold, +2 power, flag `food_vouchers`.
- If price fixing exists, vouchers may be captured by merchants.

### E103 — The Broken Bell
**Trigger:** `lantern_network` or `volunteer_relief`.

The relief bell cracks during a storm.

**A — Replace it immediately**
- -1 gold, +2 trust, flag `relief_bell_repaired`.

**B — Use runners instead**
- +1 power, -1 trust, flag `runner_relief`.

### E104 — The Mutiny's Demand
**Trigger:** `shared_crisis_command` or low security.

Soldiers demand regular pay and a written limit on emergency service.

**A — Pay them and write the limit**
- -7 gold, +4 trust, +2 Rowan, flag `soldier_charter`.

**B — Suppress the mutiny**
- +5 security, -5 trust, flag `mutiny_suppressed`.

### E105 — The Noble Winter House
**Trigger:** `land_weighted_council` or Seris >= 2.

A noble opens a manor as a public winter shelter, but demands recognition.

**A — Accept the shelter without political payment**
- +4 trust, -1 Seris, flag `noble_shelter_public`.

**B — Grant ceremonial privilege**
- +2 Seris, +1 power, flag `noble_shelter_patronage`.

### E106 — The Guild's Empty Warehouse
**Trigger:** guild route + winter.

Ivo admits one warehouse is empty because he chose to sell early rather than speculate.

**A — Praise the restraint**
- +3 Ivo, +2 trust, flag `merchant_restraint`.

**B — Accuse him of hoarding**
- +3 security, -3 Ivo, flag `merchant_accusation`.

### E107 — The Veyran Child
**Trigger:** diplomatic route + border crisis.

A Veyran child is found on the Avelune side of the river after a patrol clash.

**A — Return the child publicly**
- +5 reputation, +2 trust, flag `child_returned`.

**B — Keep the child as leverage**
- +3 power, -5 reputation, flag `child_leverage`.

### E108 — The Ash Ledger
**Trigger:** warehouse fire + investigation.

Half-burned invoices show emergency procurement continued during a supposed freeze.

**A — Preserve every fragment**
- -1 security, +3 investigation depth, flag `ash_ledger_preserved`.

**B — Photograph only the decisive page**
- +2 security, +2 power, flag `ash_ledger_selective`.

### E109 — Amara's Ultimatum
**Trigger:** winter + Amara <= 0.

Amara threatens to close the House of Lanterns unless relief is protected from political interference.

**A — Guarantee independence**
- -2 power, +3 Amara, flag `lantern_independence`.

**B — Bring it under Crown administration**
- +4 power, -4 Amara, flag `lantern_centralized`.

### E110 — The Night of Three Letters
**Trigger:** late Act IV; at least two character routes active.

Three letters arrive: Mara offers institutional reform, Rowan offers security guarantees, Seris offers a noble compromise. None can be accepted without disappointing another coalition.

**A — Publish all three proposals**
- +5 trust, -3 power, flag `three_letters_public`.
- Unlocks broader constitutional debate.

**B — Negotiate privately with each**
- +3 power, flag `three_letters_private`.
- Later coalition outcomes depend on which promises are kept.

---

## Expansion QA notes

- E71–E110 intentionally creates additional downstream hooks rather than independent filler.
- Several nodes are mutually exclusive through flags: `mara_independence`/`mara_personal_loyalty`, `law_bound_guard`/`personal_guard_oath`, `systemic_truth_public`/`conspiracy_narrative`, `three_letters_public`/`three_letters_private` and others.
- The expansion deliberately gives every major faction at least one credible position with a material benefit, not only a moral label.
- These nodes must be wired into the canonical event graph and machine-readable catalog only after content QA confirms trigger reachability and no contradiction with E01–E70.
