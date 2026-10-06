# 岗位变化观察站

私有网页：[岗位变化观察站](https://job-change-observatory.yydshly.chatgpt.site)。网站与源码仓库均仅按当前私有权限开放。网页发布源版本：`20b5e815e62250ed63a478efe5f2fcf1657b23f0`。GitHub源码与独立网页分开部署；网页每日更新由已配置的私有平台调度驱动，并非GitHub定时任务。

A bounded, source-linked personal learning research product. V0.2 closes the loop from a real public API response to immutable snapshots, deterministic skill mentions, and a Chinese evidence explorer.

## Run

Requirements: Python 3.10+, Node.js 18+. No production package dependencies or paid APIs. Hosted persistence uses the existing private Site platform and its R2 binding.

```sh
npm run build
npm test
python -m http.server 8769 --directory dist
```

Open http://localhost:8769. The static site must be served over HTTP; opening index.html as a file will block the JSON fetch in many browsers.

## Collect another real snapshot

```sh
python scripts/collect.py
npm run build
npm test
```

The collector runs one first-page Jobicy GET, at most 100 jobs. It refuses a second pass within one hour, validates canonical URLs and IDs, deduplicates by ID, and never overwrites an existing snapshot. An empty/invalid response fails without replacing prior data. The hosted Worker supports daily same-source synchronization into durable R2, without republishing. The daily schedule is confirmed enabled for 08:00 Asia/Shanghai (flexible), starting 2026-10-08; first execution is pending. Live status records the active schedule and subsequent attempts. See records/UPDATE-ROUTINE.md.

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
- `dist/`: UI assets plus generated Cloudflare-compatible Worker; no external script/font/image dependencies
- `server/`: durable snapshot and sync routes using platform R2
- `tests/`: tests
- `records/`: product decisions, provenance, verification and change log

## Next decision

Test whether the tool improves one learning choice: fix a target role/eligible geography, manually audit 20 relevant postings, then run a two-week small project. Improve coverage and extraction before scaling features. Daily same-source snapshots are implemented. Source status checks and broader technical coverage remain next steps; schedule activation needs a verified platform schedule, not a UI promise.

## Live hosted routes

GET `/api/data` returns latest durable snapshot/history/status. GET `/api/status` returns operations metadata. POST `/api/bootstrap` idempotently imports the genuine baseline. POST `/api/sync` performs a rate-limited daily collection. These shared update endpoints rely on the confirmed owner-private platform access boundary; do not make the Site public without adding independent write authorization. No service credential is committed.
