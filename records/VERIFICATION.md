# Verification — V0.1, 2026-10-06

## Passed
- Actual Jobicy public API HTTP 200; parsed 100 unique jobs, hasMore=true; exact response hash retained
- 8 Python unit/data tests: word boundaries (Java versus JavaScript; English go), duplicate mentions, special-language tokens, HTML stripping, missing-record semantics, changed-record comparison, unsafe canonical URL rejection, real snapshot integrity
- `node --check dist/app.js`
- Static build from real normalized snapshot; no placeholder dataset or fabricated history
- 16 JSDOM application-logic checks: true sample count/baseline, ten-row pagination, skill→evidence filter, detail content/close, local saved markers, saved-only filter, zero-result state/reset, next/previous, category subset, navigation, coverage disclosure, canonical source links, no raw job HTML insertion
- DOM verification machine-readable record: `dom-verification.json`

## Not completed / environment blocked
- Real browser desktop/mobile layout and visual screenshot review
- Native browser dialog focus/Escape and full accessibility behavior
- Real browser Back/Forward and persistent markers after full reload
- Standalone Chromium launch failed at runtime with socket() Operation not permitted, including the approved elevated attempt. Supported cloud browser local preview reported ERR_BLOCKED_BY_CLIENT. No bypass attempted
- `tests/browser.mjs` records the intended executable regression flow for a browser-enabled environment. Its assertions have not passed here
- JSDOM uses fetch/dialog shims and does not constitute browser or visual QA

## Not claimed
- Complete seven-day Jobicy coverage, other job boards, China market or global representativeness
- Historical trends, active/closed job state, validated required-versus-optional skills, proficiency, candidate fit, optimal career direction
- Automatic periodic operation: collection is manual and the page is a published snapshot
- GitHub CI/remote submission until independent push verification

## Reproduce
Run `npm test`. Optional DOM verification requires `jsdom` available to Node and runs via `node tests/dom.mjs`. Optional browser verification requires Playwright and a browser-enabled environment, the local HTTP server on 8769, and `node tests/browser.mjs`. UI regression scripts intentionally assert the delivered baseline fixture (100 jobs); adjust expected evidence counts when testing a later snapshot, without altering data to satisfy tests.
