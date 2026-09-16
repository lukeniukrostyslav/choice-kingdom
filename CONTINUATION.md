# CONTINUATION — Choice Kingdom

## Repository
- GitHub: `lukeniukrostyslav/choice-kingdom`
- Project: **Choice Kingdom**
- Separate from `rulebreak8`.

## Product
Original premium Android-first offline decision-and-consequence game set in Avelune. Frozen production scope **E01–E272**; E273–E277 are excluded expansion candidates. Target is a one-time purchase, offline core, no ads/subscription/mandatory backend, 20+ locales including RTL.

## Development order
**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → APK → release.**

## Current runtime state
Blocks 1–6 are closed at their defined boundaries. Runtime now contains:
- versioned `GameState` and persistence/recovery;
- authored choice execution and deterministic immediate routing;
- canonical delayed lifecycle and target execution;
- replay/meta transfer;
- ending qualification and precedence;
- presentation-neutral `GameSession` / `SessionView`.

## Latest local verification
- Full regression: **181 passed**.
- Production catalog: **PASS**, 272 events / 520 choices / 13 no-choice special nodes.
- Session boundary: **PASS**, 272-event catalog.
- Structural graph: **305 edges / 140 roots / 272 structurally reachable / 0 structurally unreachable**.
- Deterministic campaign audit: **61 unique events executed / 211 remaining / 0 execution errors**, stopping at E230 under currently implemented trigger/routing semantics.

The campaign audit is diagnostic only. The 211 remaining events are not declared impossible. Unresolved authored prose predicates and producer semantics are not guessed or invented.

## Major block percentages
- Foundation / Rules: **100%**
- Authored Content: **90%**
- Canonical IDs / Continuity: **100%**
- Producer / Consumer QA: **100% source-level**
- Derived Predicates / Machine Contracts: **100% source-level**
- Delayed Consequences: **100% runtime-verified**
- Replay / Meta-state: **100% runtime-verified**
- Endings / precedence: **100% runtime-verified at executable boundary**
- Reachability / Causal Graph: **100% source-level; full gameplay reachability open**
- Production Data Schema: **50%**
- Runtime State / Persistence Foundation: **100% current foundation**
- Decision Engine / Application Runtime: **35%**
- UI / UX: **0%**
- Localization 20+ / RTL: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **20%**
- APK / AAB: **0%**
- Release / Store: **0%**

## Latest work saved to GitHub
- `tools/audit_runtime_campaign.py` — deterministic full-campaign runtime diagnostic.
- `tests/test_runtime_campaign_audit.py` — regression contract for deterministic audit results.
- `.github/workflows/runtime-campaign-audit.yml` — GitHub Actions gate.
- `docs/RUNTIME_CAMPAIGN_AUDIT_01.md` — audit report and semantic boundary.
- `PROJECT_STATE.md` — updated current percentages and runtime evidence.

## Next work
1. Close authoritative trigger/producer semantics without inventing game rules.
2. Bind each verified semantic into the runtime.
3. Re-run all 181+ regression tests and the campaign audit after every closure.
4. Expand `GameSession` to exhaustive E01–E272 execution.
5. Build Android UI only after the runtime boundary is sufficiently complete.

## Owner gates
Physical Android QA, production signing and store publication remain owner-controlled and are never marked complete by local automation alone.
