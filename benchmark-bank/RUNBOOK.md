# Benchmark Runbook

This runbook governs B6 and later. B1-B5 remain baseline controlled
comparisons, but future rows should be more reproducible and harder to inflate.

## Required Files Per Benchmark

Each `benchmark-bank/B<N>/` directory for `N >= 6` must contain:

- `SOURCE.md`: source metadata, modification, area, and artifact paths.
- `RUN.md`: reproducibility manifest for raw and dianoia runs.
- `COMPARISON.md`: head-to-head verdict with three cited differences.

## Source Rules

`SOURCE.md` must include:

- author(s)
- year
- title
- exact statement reference
- source URL or identifier
- modification description, if the benchmark is a modified statement
- area tag

## Run Manifest Rules

`RUN.md` must include:

- `benchmark_id`
- `problem_statement`
- `raw_workspace`
- `dianoia_workspace`
- `freshness_protocol`
- `commands_or_manual_steps`
- `subagent_fire_audit`
- `reviewer_fire_audit`
- `token_accounting`
- `known_weaknesses`

When a full fresh end-to-end dianoia run is not feasible, `RUN.md` must say
`run_class: controlled-comparison` and name the limitation. Full fresh runs
should say `run_class: full-fresh`.

## Comparison Rules

`COMPARISON.md` must include:

- `## Verdict` with one of `VALUE_ADDED`, `NEUTRAL`, or `DEGRADED`
- `## Raw Baseline`
- `## Dianoia Run`
- `## Machinery Audit`
- `## Three Differences`

Each VALUE_ADDED verdict must quote or point to three concrete differences from
artifact files. A difference that only says "dianoia is more structured" is not
enough; it must name the artifact and the claim or check that changed the
answer. For B6 and later, each numbered item in `## Three Differences` must
include both `artifact:` and `quote:` fields so `tools/verify_dianoia_state.py`
can reject unsupported verdicts.

## Token Accounting

B1-B5 are allowed to retain `UNVERIFIED` token accounting as historical
baseline rows. For B6+, token accounting must be one of:

- exact token counts from tool/runtime logs
- estimated counts with method and uncertainty
- `UNVERIFIED` plus a named blocker and a plan to remove the blocker

The verifier warns on `UNVERIFIED` tokens and fails B6+ rows missing `RUN.md`.
