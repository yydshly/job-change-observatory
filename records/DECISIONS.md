# Decision record — 2026-10-06

## Goal and first-release acceptance
Help the owner understand evidence in public job postings and choose a learning experiment. First version must use real data, preserve provenance, support source inspection, and avoid fabricated trends. This is a market/skills exploration product, not a freelance-sales funnel.

## Chosen approach
1. **Official API before scraping:** Jobicy explicitly supports research tools and internal dashboards and permits attributed listing interfaces. Avoid scraping login sites and avoid collecting applicant information.
2. **Narrow first batch:** One latest-page sample of 100 jobs. The response hasMore=true. No all-market claims. Largest category Sales=21; Software Engineering=6.
3. **Explainable extraction:** 41-label keyword dictionary (see runtime dictionarySize) with matched source tokens. The user can open the exact Jobicy listing. No opaque AI score, skill trend, candidate ranking or resume data.
4. **Minimize stored content:** Metadata, matched keywords, collection time, canonical links, description and record hashes. Complete job descriptions are processed transiently and excluded from product storage.
5. **Static delivery:** The website can be inspected without new paid services, credentials, accounts or backend maintenance. Browser-local markers are clearly labeled. No “refresh” button that pretends to run background ingestion.
6. **Learning experiment:** Python appears in 18/100 listings. The proposed next step is to read three actual listings and try a reproducible data-cleaning project. This is a tentative exploration, not proof of optimal career direction.
7. **No salary comparison:** Mixed currencies/periods and incomplete salary data would make a single salary chart misleading.
8. **No historical fiction:** First snapshot is the baseline. Comparison code distinguishes firstSeen / changed / notInLatestSample; missing is never labeled closed. A trend UI waits for comparable observations over time.

## Alternatives considered
- Remotive: actual GET succeeded (18 returned jobs) but API-specific and general terms have ambiguities. Not selected for this release.
- Arbeitnow: public JSON verified by research, mainly European scope; general copying restrictions make archival use less clear. Not selected.
- Full database, login and scheduled backend: useful later, but unnecessary for establishing source→evidence→learning value in V0.1.

## Stop / continue criteria
Continue if source-backed exploration helps make one concrete learning decision and manual audit finds an acceptable precision level. Fix coverage/extraction before expanding if irrelevant roles or false matches dominate. Add a separately named technical sample on the next permitted synchronization, preserving query/filter metadata and separate denominators. Do not merge different collection universes into a spurious trend.

## 2026-10-07 / V0.3 — Bounded cohort design

Problem: the newest 100 unfiltered Jobicy postings are heavily affected by source ordering and industry mix; only 6 carry Software Engineering. The whole-sample Python ratio 18/100 conflates very different roles.

Decision: default to a precisely defined technical-function subset, with optional software-only and whole-source views. Technical categories are exactly Software Engineering, DevOps & Infrastructure, Cybersecurity, and Data Science & Analytics. Match source category labels, not keyword mentions or an inferred claim that a role is technical. Source labels themselves may be imperfect; read the original duties.

Measured baseline: technical=17 roles / 11 employers / Python mentions12; software-only=6 roles; all-source=100 roles / 53 employers / Python18. Keep the underlying single snapshot intact. This improves denominator/evidence consistency, not external market coverage. Every chart, selected-skill result and learning experiment uses the selected cohort. Empty cohorts generate no borrowed statistics.

Additional-source decision: no new employer feed included this release. A populated Wealthfront Lever endpoint conflicts with broad scraping/copying restrictions linked from its careers site; Plaid and DuckDuckGo Lever endpoints return404; Mistral's Lever endpoint returns an empty array and its careers site uses Ashby. Official ATS docs establish technical access but do not settle all employer-specific research/display rights. Prefer a smaller clearly bounded dataset over silently including uncertain sources. No paid APIs, credentials, outreach, schedule changes or Jobicy refresh were introduced.

Next coverage gate: verify an explicitly permitted technical employer feed or coordinate a separately named Jobicy technical collection sequence. Record its selection rule, retrieval time, licence/access evidence, original URLs and denominator before inclusion. Do not merge that future sequence into the existing unfiltered history or call sample differences market trends.

## 2026-10-07 / V0.4 — Distinguish sample turnover from within-role change

A changing first-page feed can make skill totals move even when no retained posting changed. The history explorer therefore shows two views: counts in each complete chosen cohort (denominators can differ), and counts for IDs present inside that cohort at both times (one fixed denominator). New postings, unavailable-in-latest postings and category movement are listed separately.

Neither view is a hiring-demand trend or proof of job closure. A category-exiting role may still be in the source sample. A missing role may have moved down the latest-page ordering or out of the source's time window. The product preserves source URLs and necessary field/skill differences; it cannot reproduce historical full descriptions because those were intentionally not stored.

Comparison is read-only. Before/after selections are resolved against stored snapshot metadata, never used directly as object paths. Missing scope/extractor metadata is a blocker rather than assumed compatibility. Equal or reversed observation dates are rejected. First v1 baseline versus v2 Worker collection will remain incomparable; later same-version snapshots become comparable.

A single actual baseline remains a single baseline. Demonstrations and edge cases are unit/DOM fixtures only, never inserted into R2 or the production interface. The daily source collection schedule is not modified to create data for this feature.
