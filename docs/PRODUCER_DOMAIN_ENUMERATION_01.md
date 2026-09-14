# Choice Kingdom — Producer Domain Enumeration 01

Status: SOURCE-LEVEL QA — CANDIDATE ENUMERATION, NOT SCHEMA
Date: 2026-09-15

This pass enumerates exact authored candidates for the remaining frozen combination domains. It intentionally distinguishes evidence from qualification producers.

## 1. Strong guild influence — candidate domains

Frozen predicate requires at least two distinct institutional domains.

| Domain | Candidate authored producer | Durable marker |
|---|---|---|
| Political representation | E144-A/B | `history.guild_representation` |
| Commercial institutional seat | E203-B | `guild_binding_seat` |
| Market/credit leverage | E39-A, E165 choices | existing commercial markers; exact canonical marker still needs freeze |
| Guild tribunal | E168-A/B | `guild_tribunal_independent` / `guild_tribunal_controlled` |
| Logistics cooperation | E136-B → E194-A qualification chain | `history.guild_logistics_cooperation` → `guild_neutral_inspectors` → qualified predicate |

Safest schema candidates are representation + binding seat, or representation + the now-separated logistics cooperation chain. A relationship value must never qualify the predicate by itself.

## 2. Systemic explanation verified — evidence domains

| Evidence class | Candidate producers | Required canonical state |
|---|---|---|
| Warehouse/financial | E186-A, E191-B, E234 | exact warehouse/financial evidence marker still needs freeze |
| Document/language | E132-A, E188-A, E233-A | exact document/language evidence marker still needs freeze |
| Witness/organizational | E135-A, E189-A, E236-A, E270-A | exact witness/organizational evidence marker still needs freeze |
| Explicit convergence | no safe existing producer identified | **OPEN P0** |

E207 must remain a consumer. E210 is convergence-only and cannot substitute for the explicit evidence decision.

## 3. Coalition cooperation — distinct faction evidence

E148-A creates the package but does not prove cooperation.

Candidate faction-domain evidence:
- Commons: E122-A / civic legitimacy markers;
- Houses: E161-A / `history.house_assembly`;
- Guilds: E136-B logistics cooperation followed by E194-A neutral-inspector qualification, or E203-B;
- Border/military: E199-A / `army_constitution_oath` or E204-A / `military_constitutional_refusal`;
- Lantern/civic: E205-A;
- Information: E206-A.

P0 requirement: choose and freeze three distinct faction identities as durable cooperation markers. Generic route count and `four_way_bargain` are insufficient.

## 4. Strong constitutional preparation — three independent domains

Candidate upstream producers:

### Civic / commons
- E111-A `local_recall_allowed`
- E114-A `local_budget_vote`
- E122-A `tax_transparency`
- E145-A `regional_courts`
- E205-A `medical_neutrality_protected`

### Audit / institutional
- E142-A `auditor_independence`
- E151-A `clerks_oath_public`
- E154-A `crown_audited`
- E155-A `full_crown_audit_published`
- E198-A `legislative_budget_lock`

### Cross-faction / constitutional
- E148-A `history.cross_faction_package`
- E150-A `constitution_bad_ruler_test`
- E199-A `army_constitution_oath`
- E204-A `military_constitutional_refusal`

The final formula should require one durable producer from each domain, with no dependence on E197-E210 outputs.

## 5. Final charter prerequisites — upstream enumeration

Required domains and strongest candidate producers:

- Civic/commons legitimacy: E122-A, E145-A, or equivalent frozen civic marker.
- Institutional/audit legitimacy: E154-A + E155-A or equivalent audit marker.
- Faction/house/guild representation: E161-A + E144-A/B, or explicit equivalent.
- Military/security constitutional route where required: E199-A or E204-A.
- Information/evidence legitimacy: systemic evidence qualification must be closed first.
- Coalition cooperation: dedicated predicate must be closed first.
- No unresolved mandatory crisis blocker: canonical blocker set must be enumerated rather than inferred from absence of one event.

E209 remains a pure consumer.

## 6. Transport disruption

E136 closes the repair/stable side. The active-disruption producer is still missing. Do not classify E251 or E192 as producers merely because they consume low transport or food logistics pressure.

## 7. Newly closed cycle-risk finding

The previous E194 self-dependency is now explicitly specified for correction in `docs/CANONICAL_SOURCE_CORRECTIONS_02.md`:
- E136-B is the earlier logistics-cooperation source;
- E194 consumes that history marker rather than the final predicate;
- E194-A supplies the neutral-inspector qualification needed for the final predicate;
- E194-B supplies an explicit immunity-risk blocker and does not qualify cooperation.

This is a source correction specification only; the authoritative event catalogs have not yet been rewritten to avoid replacing reconstructed files.

## Decision

No candidate above is automatically promoted to canonical production state. Each candidate must be checked against exact choice identity, existing semantics, downstream consumers, conflicts, and graph reachability before schema freeze.

Runtime readiness remains 0%.
