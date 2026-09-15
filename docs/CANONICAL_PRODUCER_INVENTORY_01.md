# Choice Kingdom — Canonical Producer Inventory 01

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — MACHINE-CHECKABLE INVENTORY WORKING RECORD**  
Frozen production scope: **E01–E272**  
Expansion candidates E273–E277 are tracked separately and are not admitted to the frozen catalog.

## Purpose

This inventory converts the latest source audits into explicit producer records without inventing runtime facts. It distinguishes source-closed producers, source-closed lifecycle pairs, candidate producer sets, unresolved consumers, and legacy vocabulary that must be normalized before schema freeze.

A trigger phrase is not a producer. A consumer cannot manufacture its own prerequisite.

## 1. Source-closed producer records

| Canonical fact / predicate | Producer | Choice | Source evidence | Status |
|---|---|---|---|---|
| `public_bridge` | E18 | B | Explicitly keeps the bridge public | CLOSED |
| `flexible_accounts` | E09 | B | Explicitly keeps accounting system flexible | CLOSED |
| `veteran_patronage` | E117 | B | Reserves posts for veterans | CLOSED |
| `estate_exception` | E118 | B | Creates transitional estate exception | CLOSED |
| `border_compensation` | E125 | A | Compensates border families | CLOSED |
| `requisition_compensation` | E156 | A | Pays full requisition compensation | CLOSED |
| `winter_rent_ceiling` | E160 | A | Temporary rent ceiling | CLOSED |
| `history.guild_logistics_cooperation` | E136 | B | Guild transport cooperation marker | CLOSED |
| `history.guild_representation` | E144 | A/B | Both choices establish same immutable representation marker | CLOSED |
| `history.cross_faction_package` | E148 | A | Explicit cross-faction package with named participants | CLOSED |
| `pred.market_pressure` | E19 | B | Establishes current market-pressure cycle | CLOSED at source level |
| clear `pred.market_pressure` | E19 | A | Clears active market-pressure cycle while retaining history | CLOSED at source level |
| `pred.winter_severe` | E29 | A/B | Explicit current winter-cycle producer | CLOSED at source level |
| `pred.transport_disruption` | E32 | explicit crisis outcome | Explicit current compound-crisis producer | CLOSED at source level |
| clear `pred.transport_disruption` | E136 | A/B | Clears active disruption and establishes stable network | CLOSED at source level |
| `pred.border_crisis` | E271 | A | Declares active border crisis | CLOSED at source level |
| clear `pred.border_crisis` | E272 | A/B | Resolves declared active crisis | CLOSED at source level |
| `army_constitution_oath` / military constitutional evidence | E199 | A | Explicit army constitutional oath route | CLOSED at source level |
| `auditor_independence` | E142 | A | Explicit independent auditor route | CLOSED at source level |
| `crown_audited` | E154 | A | Explicit Crown audit route | CLOSED at source level |
| `legislative_budget_lock` | E198 | A | Explicit legislative budget-lock route | CLOSED at source level |
| `soldier_compensation` | E20 | A | Publicly compensates the soldier's family; exact subject identity matches E245 | CLOSED |
| `cheap_weapons` | E17 | A | Explicitly buys cheaper weapons; E185 later consumes this identity | CLOSED_IDENTITY |
| `infrastructure_concession` | E45 | B | Grants long-term bridge/infrastructure concession; E181 later consumes this identity | CLOSED_IDENTITY |

### Guild representation normalization

E49's legacy `guild_political_representation` flag and E144's canonical `history.guild_representation` marker are now explicitly treated as **one representation domain**. They must never count as two independent domains for `pred.guild_influence_strong`. The canonical contract permits both authored sources but requires vocabulary normalization before executable schema freeze.

### Transport-disruption reconciliation

An earlier audit wording described the active producer as open. That wording is superseded by the later source re-read: **E32 is the explicit source-level producer of the current `pred.transport_disruption` crisis state**, and **E136-A/B are its recovery/clear producers**.

The unresolved portion is runtime lifecycle semantics only: save/load persistence, ordering with delayed effects, expiry/supersession and exact cycle identity. No additional producer should be invented to resolve that runtime question.

## 2. Delayed-consumer producer closure

| Consumer | Authored trigger | Producer closure | Canonical treatment |
|---|---|---|---|
| E181 | infrastructure/toll concession | E45-B | exact source identity retained; lifecycle still open |
| E182 | `veteran_patronage` | E117-B | source-closed |
| E183 | `estate_exception` | E118-B | source-closed |
| E184 | `secret evidence route` | none | OPEN; no safe alias |
| E185 | `cheap_weapons` + later military crisis | E17-A | source-closed producer; crisis lifecycle open |
| E242 | prior noble exception | E118-B explicit, possibly broader set | PARTIAL; no generic alias |
| E243 | `public bridge investment` | E18-B → `public_bridge` | SOURCE-EQUIVALENT; normalize vocabulary |
| E244 | `flexible accounts` | E09-B | source-closed |
| E245 | `compensation route` | E20-A → `soldier_compensation` | SOURCE-CLOSED; exact Soldier's Son / compensated-family identity match; E125/E156 remain distinct |
| E246 | `price ceiling` | E160-A → `winter_rent_ceiling` | SOURCE-CLOSED; lifecycle and vocabulary normalization remain open |

## 3. Derived predicates whose producer domains are frozen but not fully compiled

### `pred.guild_influence_strong`

Independent domains currently recognized by source QA:

1. guild representation (`E49` legacy / `E144` canonical);
2. guild tribunal;
3. commercial/market evidence;
4. qualified logistics cooperation.

Anti-double-counting rule: E49/E144 representation evidence is one domain, not two. `rel.ivo` alone is never sufficient.

**Status: SOURCE-LEVEL CONTRACT CLOSED — executable aggregation, contradiction handling, save/load and fresh-run reachability remain open.**

### `pred.constitutional_prepared_strong`

Frozen independent domains:

- civic: `people_charter_endorsed`;
- institutional: `crown_audited` / `full_crown_audit_published`;
- factional: `house_assembly`;
- military: `army_constitution_oath` from E199-A.

At least three independent domains are required by the current source contract. E199-A is the canonical military-law source; E227's `military_red_line` is supporting constitutional-stress evidence and must not silently replace the authored E199 producer.

**Status: SOURCE-LEVEL CONTRACT CLOSED — executable aggregation, contradiction handling, save/load and fresh-run reachability remain open.**

### `pred.systemic_explanation_verified`

Required evidence families:

- warehouse/financial;
- document/language;
- witness/organizational.

A raw clue count is forbidden. An explicit convergence decision is required. Current source-backed candidates are recorded by S12.26; the immutable convergence producer/key remains open.

**Status: PARTIAL — evidence-family identities materially frozen; exact convergence producer remains open.**

### `pred.coalition_cooperation`

E148-A is the authoritative cooperation-package source candidate. Qualification requires explicit participant identities, positive cooperation outcome and absence of an unresolved collapse blocker. `pred.faction_routes_4` is not an alias. E261-A `four_way_bargain` alone is insufficient.

**Status: SOURCE-LEVEL CONTRACT CLOSED — participant persistence, collapse evaluation, deterministic qualification, save/load and fresh-run reachability remain open.**

### `pred.budget_reform`

The source-closed institutional layers are:

- E142-A → `auditor_independence`;
- E154-A → `crown_audited`;
- E198-A → `legislative_budget_lock`.

Negative blockers are E142-B, E154-B and E198-B. E155-A `full_crown_audit_published` is same-domain downstream evidence and cannot count as a second independent domain.

**Status: SOURCE-CLOSED — runtime lifecycle/invalidation/reachability still open.**

## 4. Replay meta-state

No ordinary flag/history marker is promoted automatically to `meta.*`.

Current unresolved consumers:

- E186 — ordinary `warehouse_arson` vs previous-run informational unlock;
- E247 — second-run information route;
- E248 — replay callback;
- E249 — replay-sensitive divergence support;
- E250 — systemic-information/Second Founder support;
- E270 — replay-transfer qualification reference.

**Status: OPEN.** Design isolation is closed; exact producer/key inventory is not.

## 5. Hard negative rules

The following substitutions are explicitly forbidden:

- `rel.ivo` → `pred.guild_influence_strong`;
- E194 → `pred.guild_logistics_cooperation` from its own trigger;
- `thread.border` → `thread.border_crisis`;
- security alone → `pred.border_crisis`;
- E197 → `pred.constitutional_prepared_strong`;
- E209 → `pred.final_charter_prerequisites`;
- `four_way_bargain` → `pred.coalition_cooperation` without qualification;
- ordinary history/flag → `meta.*`;
- `price ceiling` → every price-control event;
- generic `compensation route` → union of compensation outcomes without authored decision.

## 6. Next machine-checkable pass

The next pass must compile, from the authoritative catalogs:

1. every concrete output token;
2. every trigger token;
3. producer → consumer edges;
4. duplicate semantic writers;
5. contradictory writers;
6. undefined consumers;
7. undefined producers;
8. predicate dependency cycles;
9. delayed source/target identities;
10. ending prerequisite paths;
11. fresh-run and replay reachability.

The present inventory intentionally does not promote runtime facts that are absent from the authoritative narrative source.
