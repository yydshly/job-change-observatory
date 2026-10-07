# Change log

## V0.1 — 2026-10-06
Purpose: establish a truthful, reviewable collection→snapshot→analysis→display loop.

Implemented:
- Bounded official Jobicy collector, one-hour minimum interval, schema/URL validation, de-duplication and failure-safe output
- First immutable real snapshot, response/description/record hashes and explicit sample limits
- Deterministic skill dictionary with original matched tokens
- Chinese responsive evidence interface: overview, skill counts, original postings, keyword/category/skill filters, pagination, local markers, detail dialog, method and provenance, JSON download
- First-snapshot state, source attribution and no-trend language
- Core tests, UI regression script, product decision and source records

Validation:
- 8 Python tests pass; JavaScript syntax passes
- UI test invocation initially failed module resolution, fixed to use the runtime-compatible require resolver
- Standalone Chromium and supported cloud browser preview attempts were blocked by environment restrictions; no browser success is claimed
- See VERIFICATION.md for final check status

GitHub: submission is a separate release handoff; actual remote commit receipt will be reported after verified push. Do not interpret this file as proof of a GitHub push.

## V0.2 — 2026-10-06
Purpose: meet the requested continuous-information outcome, instead of stopping at a one-off static report.

- Same private Site upgraded to a dependency-free Worker with platform R2; daily data updates do not require rebuilding or republishing
- Append-only normalized snapshots, original baseline import, hourly failure logs and durable synchronization status
- Daily idempotence and a minimum 20-hour interval after success; failed attempts cannot retry for one hour
- Source population fixed to first 100 unfiltered Jobicy jobs; no concurrent/all-page collection
- UI reads latest durable data, shows freshness (>36 hours stale), last attempt/success, failures, schedule state and comparable snapshot differences
- Explicit extractor-version gate: v1 baseline and v2 Worker extraction are not treated as comparable trends
- Supported service access uses existing platform owner-private access only; no app secrets, new credentials, paid API or expanded sharing
- 15 in-memory Worker/R2 contract tests added, including append, readback, dedupe, no-overwrite, failure preservation, rate limiting and cross-origin rejection
- Coordinator confirmed enabled flexible daily schedule at 08:00 Asia/Shanghai from 2026-10-08; first execution remains pending. Page schedule metadata is updated only after that confirmation

## V0.3 — 2026-10-07
Purpose: reduce misleading cross-industry skill inference before expanding source volume.

- Defined technical17, software6 and full100 baseline cohorts using explicit source categories
- Unified cohort denominators across overview, skill counts, employer counts, learning suggestion and evidence explorer; default technical cohort12/17 Python evidence is separate from all-source18/100
- Cohort switch resets incompatible filters; ordinary filter reset preserves the selected cohort
- Added explicit17/100 coverage text and category rules, plus empty-cohort safeguards
- Investigated bounded additional employer feeds; none met both current-data and sufficiently clear use-rights requirements, so no extra source was ingested
- Added cohort regression checks; kept all true snapshots, R2 daily collector, schedule and sharing unchanged
- Real-browser visual testing is still unverified; DOM tests are not presented as visual acceptance

## V0.4 — 2026-10-07
Purpose: make saved history reviewable without waiting idle for the next collection or fabricating a second observation.

- Added read-only `/api/compare` with explicit before/after snapshot and observation-cohort selection
- Separated new-to-source, missing-from-latest, category entry/exit, and same-role content changes
- Added per-sample skill counts alongside fixed-shared-role counts so composition changes are not mistaken for changes inside the same postings
- Added exact role links, added/removed skill mentions, changed metadata fields, body-hash changes and complete comparison JSON download
- Blocked comparisons with missing/different scope or extractor metadata, reversed/equal dates, or unknown snapshots; object reads use the saved history allowlist
- Single-baseline state stays disabled and honest; tests use in-memory fixtures only
- Protected interface from stale async responses and repeated clicks; failures preserve existing snapshots
- Daily schedule, source population, collection gate and production snapshot content remain unchanged
