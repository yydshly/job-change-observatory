# Daily update contract — V0.2

## Stable target
Same owner-private Site: `appgprj_6ac535dec3188191b39e9e24438a4c3b`.
Origin: https://job-change-observatory.yydshly.chatgpt.site
Confirmed schedule: flexible daily at 08:00 Asia/Shanghai, starting 2026-10-08. First execution is pending. No need for the owner to keep a browser open.

## Supported access
Each run reads this Site with the native Sites `get_site` tool and confirms active, owner-private access. Use only the existing platform-managed service-access path returned for this Site. Send its existing credential only in the supported header to this exact Site, never to Jobicy, a different service, a repository, logs or the task prompt. Do not create/rotate credentials or change access. If supported access is unavailable, report the blocker and preserve data.

The upstream collection is a no-key public GET to `https://jobicy.com/api/v2/remote-jobs?count=100`, performed by the Worker. No connected account or visitor consent is needed for this public source. The endpoint never accepts an arbitrary source URL.

## Each daily run
1. Confirm the linked Site is the same active owner-private product. Stop if access is public or changed.
2. POST an empty body to `/api/sync` using the existing supported Site service access. Do not send an API key to Jobicy.
3. Read `/api/status` and `/api/data` through the same Site access, verifying the reported observedAt, saved count, hash/history and success/failure status.
4. Treat `succeeded` as complete only after readback agrees. `not_due` or `already_attempted_this_hour`/`attempt_rate_limited` means no new snapshot was created; do not force a retry. A transient failure preserves the old snapshot and records an error. Do not retry within one hour. Normal next scheduled run is sufficient unless the owner needs a time-sensitive update.
5. Notify the owner only on a material blocker (e.g. source/persistence fails or freshness exceeds 36 hours) or a useful new, evidence-backed finding. Avoid routine success pings.

## One-time setup verification
POST `/api/bootstrap` to persist the already collected genuine baseline, then GET `/api/data` to confirm `syncInfo.storage` is `r2`, the baseline time/hash match and history length remains one. Repeating bootstrap must return already_seeded and must not duplicate the snapshot. Do not manufacture another observation to demonstrate history.

After the actual platform schedule is successfully saved, POST `/api/schedule-status` with `{"enabled":true,"description":"每天 08:00 前后（Asia/Shanghai），2026-10-08 起"}` and verify the same description through `/api/status`. This metadata does not create a scheduler. If the schedule is disabled later, update it to false.

## Persistence and safety
R2 keeps immutable `snapshots/` objects and append-only `runs/` outcomes; no routine deletes. `state/` only contains latest operational state and schedule metadata. Normal data refresh never republishes code. One first-page population and source URL remain fixed. Missing postings are labeled absent from latest sample, never confirmed closed. Cross-extractor-version comparisons are disabled. No full job descriptions, contact information or paid response fields are stored.

## Deployment / source changes
Use normal Site source workflow only for code changes; run tests, then deploy privately and verify. Keep the private GitHub repository in sync through its authorized publication workflow. No credentials in either source.
