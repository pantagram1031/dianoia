# B6 Partial Run Manifest

benchmark_id: B6
run_class: full-fresh-candidate

## Problem Statement

See `benchmark-bank/B6/PROBLEM.md`.

## Raw Workspace

Path: `C:\Users\SAMSUNG\Downloads\raw-attempt-7`

Freshness evidence:

- Workspace created for B6 raw baseline.
- Contains `answer.md` and `run.md`.
- Raw worker was instructed not to inspect dianoia source, dianoia-run, or prior
  raw attempts.

## Dianoia Workspace

Path: `C:\Users\SAMSUNG\Downloads\dianoia-run\problems\b6-infinite-induced-saturated-graphs`

Freshness evidence:

- Dianoia-side worker dispatched with no raw-attempt access.
- Run still pending at the time of this partial manifest.

## Freshness Protocol

- Raw run: isolated worker, raw-attempt-7 only.
- Dianoia run: isolated worker, dianoia-run B6 problem directory only, no
  raw-attempt access.
- Coordinator read raw output before dianoia output; therefore the coordinator
  must not author the dianoia mathematical answer.

## Commands Or Manual Steps

1. Source selected and documented in `SOURCE.md`.
2. Raw baseline worker created `raw-attempt-7/answer.md` and `raw-attempt-7/run.md`.
3. Dianoia-side worker dispatched to create dianoia-style artifacts in
   `dianoia-run/problems/b6-infinite-induced-saturated-graphs/`.

## Subagent Fire Audit

| subagent | expected | fired | evidence |
|----------|----------|-------|----------|
| raw baseline worker | yes | FIRED | `raw-attempt-7/answer.md`; `raw-attempt-7/run.md` |
| dianoia-side worker | yes | PENDING | worker dispatched; artifacts pending |

## Reviewer Fire Audit

Pending until dianoia run returns.

## Token Accounting

Method: UNVERIFIED
Raw tokens: UNVERIFIED
Dianoia tokens: UNVERIFIED
Uncertainty: UNVERIFIED
Blocker: Codex desktop worker token logs are not exposed in the artifact files.
Removal plan: add transcript token counting or explicit runtime token export before promoting B6 to `RUN.md`.

## Known Weaknesses

- This file is intentionally named `RUN-PARTIAL.md`, not `RUN.md`, because B6 is
  not ready for verifier promotion or a `BENCHMARK.md` row.
- Dianoia output and head-to-head verdict are pending.
