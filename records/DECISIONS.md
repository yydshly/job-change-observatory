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
