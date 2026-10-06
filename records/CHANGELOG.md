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
