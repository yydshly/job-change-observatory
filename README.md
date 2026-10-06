# 岗位变化观察站

私有网页：[岗位变化观察站](https://job-change-observatory.yydshly.chatgpt.site)。仅项目所有者可访问；GitHub 仓库也保持私有。

网页发布源版本：`33db2c5fa2eea305d15631ba819a99526a9be5f0`。此仓库保存可独立运行的完整源代码、归一化证据快照、测试和项目记录；后续 GitHub 提交不会自动更新独立网页。

A bounded, source-linked personal learning research product. V0.1 closes the loop from a real public API response to immutable snapshots, deterministic skill mentions, and a Chinese evidence explorer.

## Run

Requirements: Python 3.10+, Node.js 18+. No production dependencies, credentials or paid services.

```sh
python scripts/build.py
npm test
python -m http.server 8769 --directory dist
```

Open http://localhost:8769. The static site must be served over HTTP; opening index.html as a file will block the JSON fetch in many browsers.

## Collect another real snapshot

```sh
python scripts/collect.py
python scripts/build.py
npm test
```

The collector runs one first-page Jobicy GET, at most 100 jobs. It refuses a second pass within one hour, validates canonical URLs and IDs, deduplicates by ID, and never overwrites an existing snapshot. An empty/invalid response fails without replacing prior data. Collection is manual in this release; no timer, CI schedule or hosted background worker has been enabled.

For a genuine previously retrieved response, use `--input PATH --observed-at ACTUAL_UTC_TIMESTAMP`. This is an import path for provenance, not a way to generate fake history. Original full API responses are not included in this repository or public assets.

## Evidence & limitations

- Source: [Jobicy public API](https://jobicy.com/jobs-rss-feed), no authentication used
- Baseline: 2026-10-06 17:56:43 UTC, latest 100 unique listings; response hasMore=true
- Source documents a seven-day publication window and three-hour delay. This sample covers only the first page, not the entire window
- Sales is the largest category (21/100); Software Engineering is 6/100. Neither this sample nor its filtered subsets represent all technical hiring or the Chinese job market
- Skills are keyword mentions in title/body, not verified requirements, levels, candidate fit or learning ROI
- Save only metadata, matched words and hashes. No full descriptions, logos, candidate data or contact details are retained in product assets
- One baseline cannot establish growth. Feed absence is not closure
- Source URLs and attribution are preserved. This is not an openly licensed job dataset; Jobicy fair-use conditions still apply
- No salary ranking: currencies, periods and missing values differ
- Saved markers are browser-local; no cloud sync

## Checks

`npm test`: Python core/data tests and JavaScript syntax. `tests/browser.mjs` is a reproducible Playwright UI test (install Playwright locally; configure CHROMIUM_EXECUTABLE if needed). See `records/VERIFICATION.md` for passed versus blocked checks; browser QA was attempted but blocked by this cloud runtime, and is not claimed complete.

## Structure

- `scripts/core.py`: sanitization, deterministic extraction, change-set semantics
- `scripts/collect.py`: bounded API collection and append-only snapshots
- `scripts/build.py`: produces the static current-data asset
- `snapshots/`: normalized evidence snapshots
- `dist/`: deployable static product, no external script/font/image dependencies
- `tests/`: tests
- `records/`: product decisions, provenance, verification and change log

## Next decision

Test whether the tool improves one learning choice: fix a target role/eligible geography, manually audit 20 relevant postings, then run a two-week small project. Improve coverage and extraction before scaling features. Daily same-filter snapshots and source status checks are the next step; automated operation needs verified scheduling/deployment and monitoring, not a UI promise.
