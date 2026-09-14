# Choice Kingdom — Graph ↔ Catalog Reconciliation 03

Date: 2026-09-14
Status: **SOURCE-VERIFIED AUDIT — NOT RUNTIME**
Scope: E151–E210.

## Canonical rule
A graph edge is eligible for production only when the target consumes a durable source flag/history/thread, explicitly counts prior completion/history, receives a documented delayed consequence, or consumes a locked derived predicate. Shared themes, characters, or similar wording are not dependencies.

## Verified relationships

| Source | Durable producer | Consumer | Disposition |
|---|---|---|---|
| E151 | `clerks_oath_public` / `clerks_oath_private` | E212 and institutional descendants | valid institutional branch; exact consumers require full catalog scan |
| E153 | `archive_access_shared` / `archive_access_restricted` | archive/investigation descendants | valid archive branch; do not collapse access levels |
| E154 | `crown_audited` / `crown_exempt_from_audit` | E155, E211 | verified and already covered by prior inventory |
| E155 | `full_crown_audit_published` / `audit_summary_only` | E211 | verified public-accountability fork |
| E156 | `requisition_compensation` / `requisition_tax_credit` | E245 | verified delayed family callback |
| E162 | `estate_map_audit` / `targeted_estate_audit` | noble evidence descendants | valid investigation split |
| E164 | `private_army_rejected` / `private_army_licensed` | border/security descendants | valid security-route split |
| E168 | `guild_tribunal_independent` / `guild_tribunal_controlled` | guild descendants | valid guild governance split |
| E169 | `apprentice_safety_law` / `apprentice_strike_broken` | labor/social descendants | valid labor branch |
| E172 | `civilian_signal_authority` / `military_signal_control` | border crisis descendants | valid authority split; keep distinct |
| E173 | `barracks_shelter` | winter/civic descendants | valid civic callback; rebuilding path still needs explicit durable marker if consumed later |
| E175 | `humane_quarantine` / `hard_quarantine` | E176 | verified direct consumer |
| E177 | `licensed_courier_network` / `courier_surveillance` | information descendants | valid information-route split |
| E178 | `unsent_letter_traced` / `unsent_letter_replaced` | information/investigation descendants | valid evidence-route split |
| E180 | `informant_family_relocated` / `informant_guard` | information descendants | valid source-protection split |
| E181 | `toll_escalation_sold` | economic descendants | valid delayed economic consequence candidate |
| E182 | `veteran_positions_granted` | security/character descendants | valid veteran-route marker |
| E183 | `exception_precedent_closed` / `exception_precedent_extended` | noble descendants | valid precedent fork |
| E184 | `quiet_evidence_published` / `quiet_evidence_kept` | evidence/reputation descendants | valid evidence visibility split |
| E185 | `steel_failure_prevented` | later military consequences | verified callback; alternative choice needs explicit delayed marker |
| E186 | `warehouse_second_box` / `warehouse_fire_focus` | replay/investigation descendants | replay branch; exact replay metadata must remain separate from persistent campaign state |
| E187 | `payment_date_crosscheck` | E234 | verified direct investigation dependency |
| E188 | `necessity_phrase_history` | replay/institutional descendants | valid historical callback |
| E189 | `witness_reopened` | evidence descendants | valid witness route |
| E190 | map/beneficiary investigation outcome | later investigation | candidate dependency; target consumers must explicitly consume the resulting marker before graph promotion |

## Compound trigger risks

The E151–E210 catalog contains multiple prose predicates that cannot yet be engine conditions:

- `document audit route`;
- `institutional reform`;
- `high noble influence` + `low security`;
- `strong market oversight`;
- `guild labor tension`;
- `border pressure` / `border tension`;
- `low army readiness`;
- `winter illness`;
- `information route`;
- `secret evidence route`;
- `road pressure`;
- `late constitutional route`;
- `strong constitutional preparation`;
- `high information pressure`;
- evidence cardinality (`two or more procurement clues`, `three or more related clues`).

These require canonical flags/history/threads or deterministic predicates with explicitly defined producers and thresholds.

## Delayed consequence findings

1. E181 explicitly uses a 5+ turn delay. The source of the original toll concession must be identified and represented by a canonical history marker; a generic `toll concession` string is insufficient.
2. E182 explicitly uses `veteran_patronage`, 4+ turns later. This is a valid delayed producer relationship already established in earlier inventory.
3. E183 uses `estate_exception`, 5+ turns later; exact-once resolution must be preserved.
4. E184 uses secret evidence, 4+ turns later; the evidence source and replay interaction need canonical representation.
5. E185 is a compound callback: `cheap_weapons` plus later military crisis. The first condition alone cannot schedule the outcome.
6. E242 in the later catalog references any prior noble exception 6+ turns later; this should not be implemented as a simple event-completion count until the canonical history semantics are fixed.

## Source-quality issues discovered

- E163's choice A describes relationship stress without a canonical durable marker. If no later content consumes that state, it may remain a relationship-only consequence; if later content needs it, a marker must be authored.
- E170 choice A has no explicit durable marker while choice B has `veteran_land_grants`; asymmetry is acceptable only if no later event needs to distinguish the wage-only decision.
- E173 choice A (`Rebuild`) has no explicit marker while choice B has `barracks_shelter`; this must be checked against later consumers before schema freeze.
- E185 choice B promises a severe delayed loss but the excerpted catalog does not expose a stable marker in the choice line; this is a production-schema blocker until its delayed consequence is explicit.
- E190 describes an investigation outcome without showing a stable flag in the excerpt; it must not become a graph edge solely from narrative wording.

## Gate impact

- E151–E210 graph reconciliation: **source-verified partial pass**.
- Production graph: **still blocked**.
- Production schema: **still blocked** pending canonical predicates, delayed markers and source ID reconciliation.
- Reachability simulation: blocked until machine-readable canonical representation exists.
