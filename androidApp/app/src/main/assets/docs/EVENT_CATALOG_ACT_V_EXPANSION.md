# Choice Kingdom — Act V and Endgame Event Expansion

This file is a continuation of `docs/EVENT_CATALOG.md`. It extends the initial E01–E34 skeleton into a production-scale campaign. These events are authored as causal story nodes, not filler cards. The engine must later consume the final reconciled catalog.

## Act V — The Crown's Answer

### E35 — The Day After Emergency
**Trigger:** E33 resolved.

The thirty-day emergency authority has begun to change how officials speak to the Crown. Petitions arrive already stamped “urgent.”

**A — Set a public expiry date**
- Immediate: +4 trust, -2 power.
- Flag: `emergency_expiry_announced`.
- Delayed: officials begin planning for ordinary procedures again.

**B — Keep the expiry flexible**
- Immediate: +3 power, -2 trust.
- Flag: `emergency_expiry_flexible`.
- Delayed: nobles and officers begin treating emergency rule as normal.

### E36 — Mara's Resignation
**Trigger:** Mara relationship <= -1 or emergency powers + weak audit.

Mara places her seal on the desk and says she will not administer a government whose rules change whenever the Crown is frightened.

**A — Give her an independent mandate**
- Immediate: -2 power, +3 Mara.
- Flag: `mara_independent_mandate`.
- Delayed: strengthens institutional ending routes.

**B — Accept her resignation**
- Immediate: +2 power, -3 Mara.
- Flag: `mara_resigned`.
- Delayed: bureaucratic continuity weakens during the final crisis.

### E37 — Rowan's Oath
**Trigger:** Rowan relationship >= 1 or military crisis.

Rowan asks a dangerous question: if the Crown orders something illegal, who does the army obey?

**A — The law comes first**
- Immediate: +3 trust, -1 Rowan if he expected loyalty to the Crown.
- Flag: `army_law_oath`.

**B — The Crown decides in crisis**
- Immediate: +4 security, +2 Rowan.
- Flag: `army_crown_oath`.
- Delayed: strengthens Iron Crown route.

### E38 — Seris and the Old Houses
**Trigger:** Seris relationship >= 0.

Seris offers the Crown a coalition of houses in exchange for guaranteed hereditary seats in the post-crisis council.

**A — Accept limited representation**
- Immediate: +2 power, +2 Seris, -2 trust.
- Flag: `hereditary_seats_limited`.

**B — Reject hereditary guarantees**
- Immediate: +3 trust, -2 Seris.
- Flag: `hereditary_seats_rejected`.
- Delayed: unlocks broader constitutional bargaining.

### E39 — Ivo's Last Bargain
**Trigger:** Ivo >= 1 and treasury pressure.

Ivo offers emergency grain credit at a price: the guild wants the right to appoint inspectors at every river port.

**A — Accept the credit**
- Immediate: +10 gold, +2 Ivo, -3 trust.
- Flag: `guild_emergency_credit`.
- Delayed: creates commercial leverage over the Crown.

**B — Borrow from citizens instead**
- Immediate: +4 gold, +4 trust, -2 power.
- Flag: `civic_war_bonds`.
- Delayed: strengthens distributed-power ending routes if repayment succeeds.

### E40 — Amara's Winter List
**Trigger:** winter mortality risk or Amara >= 1.

Amara produces a list of villages that survived because of small local decisions the palace never noticed.

**A — Fund local relief councils**
- Immediate: -5 gold, +5 trust, +2 Amara.
- Flag: `local_relief_councils`.

**B — Centralize relief distribution**
- Immediate: +2 power, +2 security, -3 Amara.
- Flag: `central_relief`.
- Delayed: faster where administration is strong, catastrophic where it is not.

### E41 — Toma's Missing Crate
**Trigger:** Toma recruited and investigation route active.

Toma finds the customs crate from the old ledger, but the documents inside have been replaced by children's toys.

**A — Ask who knew the route**
- Immediate: +2 power, +1 Toma.
- Flag: `crate_route_traced`.
- Delayed: identifies an intermediary rather than the ultimate conspirator.

**B — Publicly accuse the customs office**
- Immediate: +3 trust, -2 reputation.
- Flag: `customs_accused`.
- Delayed: innocent officials may become scapegoats.

### E42 — The Witness at the Bell Tower
**Trigger:** `crate_route_traced` or `seris_witness`.

An elderly bell keeper saw sealed documents moved on the night the old treasurer died.

**A — Protect the witness quietly**
- Immediate: +1 security, +2 power.
- Flag: `witness_protected`.
- Delayed: testimony survives the final political bargain.

**B — Bring the witness before the council**
- Immediate: +4 trust, -2 security.
- Flag: `witness_public`.
- Delayed: enemies can attack the witness's credibility.

### E43 — The Ledger's Second Name
**Trigger:** two or more investigation sources agree.

The hidden ledger does not name a single mastermind. It records a network of temporary offices that made emergency theft profitable for everyone who participated.

**A — Publish the network**
- Immediate: +6 trust, -3 power, -2 reputation.
- Flag: `ledger_network_public`.

**B — Protect cooperating insiders**
- Immediate: +4 power, +2 security.
- Flag: `ledger_network_compromised`.
- Delayed: institutions can be repaired faster, but legitimacy becomes fragile if secrecy is exposed.

### E44 — The House Divides
**Trigger:** `seris_witness` or `seris_exposed`.

Seris's family splits. One faction wants amnesty; another wants to restore the old order by force.

**A — Let the family negotiate itself**
- Immediate: +2 trust, -1 security.
- Flag: `houses_self_reconcile`.

**B — Separate the armed faction**
- Immediate: +4 security, -2 Seris.
- Flag: `house_arms_restricted`.

### E45 — The Price of the Bridge
**Trigger:** `public_bridge` or repeated toll policy.

The rebuilt bridge opens. Traders ask whether it belongs to the Crown, the guilds, or everyone who paid for it.

**A — Declare it a public trust**
- Immediate: +4 trust, -2 power.
- Flag: `public_infrastructure_trust`.

**B — Grant long-term concession**
- Immediate: +6 gold, +2 Ivo, -3 trust.
- Flag: `infrastructure_concession`.

### E46 — The Soldier Who Refused
**Trigger:** `army_law_oath` + emergency crisis.

A captain refuses an illegal order and waits to see whether the Crown punishes him.

**A — Defend his refusal**
- Immediate: +5 trust, -2 security.
- Flag: `lawful_refusal_defended`.

**B — Punish him for insubordination**
- Immediate: +4 security, -4 trust.
- Flag: `lawful_refusal_punished`.

### E47 — The Constitutional Table
**Trigger:** E35–E46 milestone; at least three factions active.

Representatives demand to know what powers the Crown will retain after winter.

**A — Write limits first**
- Immediate: -2 power, +5 trust.
- Flag: `constitution_first`.

**B — Write powers first**
- Immediate: +5 power, -3 trust.
- Flag: `crown_powers_first`.

### E48 — The Missing Clause
**Trigger:** `constitution_first`.

Mara discovers an old legal clause allowing emergency powers to be renewed indefinitely if three councils agree.

**A — Remove the clause publicly**
- Immediate: +4 trust, -2 power.
- Flag: `permanent_emergency_blocked`.

**B — Keep it as a last resort**
- Immediate: +3 power, -2 trust.
- Flag: `emergency_renewal_possible`.

### E49 — The Guild's Vote
**Trigger:** `guild_emergency_credit` or strong Ivo relationship.

Ivo admits the guild can keep the kingdom supplied, but only if the Crown accepts that merchants will gain political power.

**A — Accept commercial representation**
- Immediate: +5 gold, +3 Ivo, -3 trust.
- Flag: `guild_political_representation`.

**B — Keep merchants outside government**
- Immediate: +4 trust, -2 Ivo.
- Flag: `guild_political_exclusion`.

### E50 — The People's Charter
**Trigger:** `people_heard` or `local_relief_councils` + high trust.

Petitioners propose a charter guaranteeing access to courts, relief and public accounts.

**A — Endorse it**
- Immediate: +6 trust, -3 power.
- Flag: `people_charter_endorsed`.

**B — Promise review after the crisis**
- Immediate: +2 power, -3 trust.
- Flag: `people_charter_delayed`.

## Final crisis — Who Owns the Future?

### E51 — The Three Seals
**Trigger:** E47 complete.

Three seals are placed on the constitutional draft: Crown, Council, and Commons. One must be allowed to veto the others.

**A — Mutual veto**
- Immediate: +4 trust, -2 power.
- Flag: `mutual_veto`.

**B — Crown veto**
- Immediate: +5 power, -4 trust.
- Flag: `crown_veto`.

**C — No veto; require public renewal**
- Immediate: +5 trust, -3 power.
- Flag: `public_renewal_rule`.

### E52 — Rowan's Final Report
**Trigger:** Rowan arc active.

Rowan reports that the army is loyal, but officers have learned that emergency orders are profitable.

**A — Audit military procurement**
- Immediate: -3 gold, +3 trust.
- Flag: `military_audit_final`.

**B — Reward loyal commanders**
- Immediate: +4 security, +2 Rowan.
- Flag: `military_patronage_final`.

### E53 — Mara's Final Ledger
**Trigger:** audit route or `ledger_network_public`.

Mara places the complete emergency ledger on the table. It can clear the Crown or implicate people who helped the Crown survive.

**A — Publish everything**
- Immediate: +7 trust, -4 power.
- Flag: `full_ledger_published`.

**B — Publish only proven crimes**
- Immediate: +3 trust, +2 power.
- Flag: `verified_ledger_only`.

### E54 — Seris's Choice
**Trigger:** Seris arc active.

Seris can bring enough houses to accept constitutional reform, but only if she receives a place in the new order.

**A — Give her a constitutional office**
- Immediate: +3 Seris, +3 power.
- Flag: `seris_constitutional_office`.

**B — Ask her to accept ordinary citizenship**
- Immediate: +5 trust, -2 Seris.
- Flag: `nobility_equal_under_law`.

### E55 — Ivo's Last Account
**Trigger:** Ivo arc active.

Ivo reveals that the guild's books contain evidence that could destroy several nobles but also expose his own family.

**A — Let him submit the books under protection**
- Immediate: +5 trust, +1 Ivo.
- Flag: `guild_books_submitted`.

**B — Seal the books and use them privately**
- Immediate: +4 power, +2 Ivo.
- Flag: `guild_books_sealed`.

### E56 — Amara's Question
**Trigger:** Amara arc active.

Amara asks the ruler what happens when the constitution protects procedure but people are still hungry.

**A — Add a minimum relief guarantee**
- Immediate: +5 trust, -3 gold.
- Flag: `relief_guarantee`.

**B — Leave relief to future budgets**
- Immediate: +2 power, +2 gold.
- Flag: `relief_discretion`.

### E57 — Toma's Final Rumor
**Trigger:** Toma recruited or street route active.

Toma brings one final rumor: the person who began the emergency network is dead, and the surviving system has no master.

**A — Accept the network explanation**
- Immediate: +2 power, +2 Toma.
- Flag: `systemic_corruption_confirmed`.

**B — Keep searching for a mastermind**
- Immediate: -2 power, +2 security.
- Flag: `mastermind_hunt`.
- Delayed: risks destroying innocent alliances in pursuit of a satisfying villain.

### E58 — The Last Emergency
**Trigger:** unresolved severe crisis.

A final fire, border alarm and food riot happen within the same hour. The player can invoke emergency authority one final time.

**A — Invoke it**
- Immediate: +8 security, +6 power, -5 trust.
- Flag: `final_emergency_invoked`.

**B — Refuse and execute the constitutional plan**
- Immediate: -5 security, +7 trust.
- Flag: `final_emergency_refused`.

### E59 — The Crown Is Offered Back
**Trigger:** final emergency resolved.

The council asks whether the ruler will keep the crown beyond the original succession arrangement.

**A — Renew the mandate through the new rules**
- Immediate: +3 power, +3 trust.
- Flag: `mandate_renewed_legally`.

**B — Set a fixed succession limit**
- Immediate: -2 power, +5 trust.
- Flag: `succession_limited`.

### E60 — The Founding Night
**Trigger:** final constitutional conditions.

The ruler sits alone with six sealed letters from Mara, Rowan, Seris, Ivo, Amara and Toma. Each represents a different future for Avelune.

**A — Open every letter before deciding**
- Immediate: +2 power, +2 trust.
- Flag: `all_voices_heard`.

**B — Decide without reading**
- Immediate: +4 power.
- Flag: `crown_decides_alone`.

## Ending resolution nodes

### E61 — Steward's Oath
**Trigger:** strong institutions + no permanent emergency powers + stable security.

The Crown becomes a constitutional steward rather than an unchecked ruler.

**Ending:** `STEWARD`.

### E62 — Iron Crown
**Trigger:** `emergency_power` + military dependency + `crown_powers_first` or repeated emergency use.

The kingdom survives because the Crown became the institution that cannot be questioned.

**Ending:** `IRON_CROWN`.

### E63 — Golden Compact
**Trigger:** strong treasury + `merchant_charter`/commercial leverage + guild political representation.

Avelune becomes prosperous, but commerce now sits beside the throne as a second power center.

**Ending:** `GOLDEN_COMPACT`.

### E64 — People's Charter
**Trigger:** high trust + `people_charter_endorsed` + distributed institutions.

The Crown accepts that legitimacy belongs to citizens as much as to the dynasty.

**Ending:** `PEOPLES_CHARTER`.

### E65 — Broken Diadem
**Trigger:** multiple unresolved crises + collapsed relationships/institutions + no stable constitutional settlement.

The kingdom does not necessarily fall in one night. It simply stops obeying one center.

**Ending:** `BROKEN_DIADEM`.

### E66 — Quiet Throne
**Trigger:** strong personal survival + withdrawal from public conflict + low institutional ambition.

The ruler keeps peace by refusing to solve the deeper question of power.

**Ending:** `QUIET_THRONE`.

### E67 — Second Founder
**Trigger:** `constitutional_limit` + verified or cross-confirmed ledger truth + cross-faction cooperation + institutional redesign + no permanent emergency powers.

The ruler deliberately weakens the Crown so the kingdom can outlive the ruler.

**Ending:** `SECOND_FOUNDER`.

## Post-ending epilogues / replay hooks

### E68 — The Historian's Footnote
**Trigger:** any ending.

A later historian interprets the ruler's reign using records created by the player's choices.

**Purpose:** the same event is remembered differently depending on whether records were public, secret or destroyed.

### E69 — The Child at the Bridge
**Trigger:** `public_infrastructure_trust` or `infrastructure_concession`.

Years later, a child asks who owns the bridge. The answer reflects the player's infrastructure decision.

**Purpose:** callback showing that an apparently economic choice became part of civic identity.

### E70 — The Ledger in the Archive
**Trigger:** investigation ending route.

A surviving copy of the emergency ledger is found by a future archivist.

**Purpose:** rewards investigation-heavy replay and confirms that information choices changed history rather than merely unlocking dialogue.

## Production expansion requirements after E70

E01–E70 form the current authored spine and ending framework. They are **not** the final release count. The next content pass must expand between these anchors with additional character scenes, faction disputes, ordinary-life consequences, investigation branches, economic/security dilemmas, callback events, alternate approaches to the same crisis, and replay-exclusive information until the full release reaches approximately 250–350+ meaningful authored events/story nodes.

The expansion must not simply insert extra cards between turns. Every new node must have at least one meaningful downstream effect, relationship/information consequence, branch interaction, delayed callback, or ending influence.
