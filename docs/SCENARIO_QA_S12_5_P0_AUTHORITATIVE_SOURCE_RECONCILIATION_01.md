# Choice Kingdom — S12.5 P0 Authoritative Source Reconciliation 01

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — VERIFIED AGAINST AUTHORITATIVE CATALOG TEXT**  
Frozen production scope: **E01–E272**. E273–E277 remain excluded.

## 1. Purpose

Verify whether the previously proposed P0 authored patches are actually present in the authoritative event catalogs, rather than merely present in QA documents.

## 2. Authoritative catalog findings

| Area | Evidence in authored catalog | Status |
|---|---|---|
| E136 transport recovery | E136-A/B explicitly write `transport_network_stable`; both clear `transport_disruption_active`; E136-B writes `history.guild_logistics_cooperation` and `roads_guild_contract` | **APPLIED / VERIFIED** |
| E144 guild representation | E144-A/B explicitly write `history.guild_representation`; legacy trigger `guild_political_representation` is documented as a source-language alias | **APPLIED / VERIFIED** |
| E148 coalition package | E148-A writes `history.cross_faction_package` and `coalition_candidate_package`; six named participants are recorded in authored prose; contract explicitly says package alone is insufficient | **APPLIED / PARTIAL** — participant identities are authored, but machine-normalized identity tokens remain needed |
| E192 food logistics | E192-A writes `food_logistics_unstable`; E192-B writes `food_logistics_stabilized`; no numeric food resource effect appears | **APPLIED / VERIFIED** |
| E194 guild convoy | E194-A writes `guild_neutral_inspectors`; B writes immunity-risk marker; downstream qualification explicitly requires upstream cooperation and no immunity blocker | **APPLIED / VERIFIED** |
| Border crisis | Canonical source closure already establishes E271-A declaration and E272-A/B resolution; catalog text for E139 explicitly rejects treating border infrastructure as crisis | **SOURCE CHAIN VERIFIED**; late-catalog lifecycle still requires exhaustive graph reconciliation |
| E197 constitutional preparation | Canonical P0 contract states E197 is consumer-only and cannot manufacture its prerequisite | **CONTRACT VERIFIED**; exact authored event row still requires machine extraction |
| E200 guild influence | Canonical P0 contract states E200 consumes `pred.guild_influence_strong`; source domains are identified, but exact qualification formula remains open | **PARTIAL / CONTRACT VERIFIED** |
| E207 systemic explanation | Canonical P0 contract defines four evidence families and explicit convergence; exact immutable evidence IDs remain open | **PARTIAL / CONTRACT VERIFIED** |
| E209 final charter | Canonical P0 contract defines upstream dependency boundary and rejects consumer-as-producer behavior; exact formula remains open | **PARTIAL / CONTRACT VERIFIED** |
| E210 convergence | Canonical contract explicitly preserves convergence-only semantics | **VERIFIED / CONVERGENCE-ONLY** |

## 3. E192 semantic decision

The authoritative catalog does **not** directly write `pred.food_stable` from E192. It writes the more specific canonical logistics outcomes:

- `food_logistics_unstable`
- `food_logistics_stabilized`

Therefore the earlier proposed alias from `food_logistics_stabilized` to `pred.food_stable` is **rejected as an implicit alias**.

`pred.food_stable` remains OPEN/BLOCKED until a complete authored producer/lifecycle contract is independently demonstrated. E192 is not promoted as that producer merely because its grain-first branch improves logistics.

## 4. P0 delta

The authoritative source catalogs already contain most of the previously proposed P0 source-level edits. The remaining work is therefore no longer blind patch application; it is machine normalization and proof:

1. Convert E148 participant identities from prose into stable canonical identity tokens.
2. Normalize E144 legacy trigger alias into a producer-backed canonical route.
3. Keep `food_logistics_stabilized` separate from `pred.food_stable`.
4. Compile exact evidence IDs for E207.
5. Freeze the qualification formula for guild influence, constitutional preparation, coalition cooperation, budget reform and final-charter prerequisites.
6. Extract exact E197/E200/E207/E209/E210 rows into the machine producer/consumer registry.
7. Reconcile E271/E272 border lifecycle against all late consumers.

## 5. Hard-negative checks

PASS:
- E136 recovery does not reactivate transport disruption.
- E194 cannot self-create its upstream logistics qualification.
- E148 package does not alias directly to coalition cooperation.
- E192 does not create a sixth resource.
- `food_logistics_stabilized` is not silently aliased to `pred.food_stable`.
- E273–E277 remain outside production edges.

OPEN:
- exhaustive E01–E272 producer/consumer registry;
- exact P0 qualification formulas;
- exact delayed identity/timing/cancellation rows;
- ending incoming-path closure;
- fresh-run/replay reachability;
- machine graph ↔ catalog equality.

## 6. Gate result

**S12.5: PASS for authoritative P0 source reconciliation, PARTIAL for machine contract closure.**

This pass materially changes the next work: the main blocker is no longer whether E136/E144/E192/E194 source patches exist. They do. The remaining blocker is converting the authored semantics into a deterministic, exhaustive machine contract without inventing aliases or producers.

Production schema remains **BLOCKED** until the machine graph and ending/reachability gates pass.
