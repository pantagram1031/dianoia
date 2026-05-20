# Roadmap

Initialized: 2026-05-20T17:54:05+09:00

## Phase Status

| Phase | Name | Status | Evidence |
|-------|------|--------|----------|
| 0 | VERIFY PRIOR EXPERIMENT | COMPLETE | capability-test/VERIFY_PRIOR.md |
| 1 | DIAGNOSE | COMPLETE | DIAGNOSIS.md |
| 2 | FIX | COMPLETE | AGENTS.md routing guard plus Phase 2 smoke artifacts |
| 3 | RE-TEST SAME PROBLEM | COMPLETE: VALUE_ADDED | capability-test/RETEST.md |
| 4 | EXPAND BENCHMARK BANK | COMPLETE | 5/5 VALUE_ADDED rows across 5 areas |
| 5 | BUILD SKILLS | COMPLETE | 5/5 skills added and referenced by subagent prompts |
| 6 | BUILD CONNECTORS | COMPLETE | 2/2 connectors added: arxiv, oeis |
| 7 | DOCS | COMPLETE | README.md, ARCHITECTURE.md, EXAMPLES.md, CHANGELOG.md current as of B5/Phase 5/Phase 6 |
| 8 | DEEPER RESEARCH | GATED | Requires 5 VALUE_ADDED rows across 3 areas |

## Continuous Improvement Track

The former MASTERPIECE checklist is now a baseline, not a terminal state.
Ongoing work should keep improving dianoia's capability, honesty, and
reproducibility.

| Track | Status | Next Evidence |
|-------|--------|---------------|
| Benchmark expansion | IN_PROGRESS | Add B6+ with full fresh raw and dianoia artifacts when feasible |
| Benchmark reproducibility | IN_PROGRESS | Add verifier/runbook/templates that reject weak or simulated rows |
| Phase-loop reliability | IN_PROGRESS | Routing, checkpoint, Reviewer D, and subagent-fire checks are covered by local verifiers; next add smoke checks from real fresh runs |
| Skills/connectors | WATCH | Connector files and subagent wiring are covered by `tools/verify_connectors.py`; add or revise only when benchmark evidence shows a reusable need |
| Docs | WATCH | Keep README/ARCHITECTURE/EXAMPLES/CHANGELOG synced after substantive changes |
| Deeper research | READY-BUT-GATED-BY-JUDGMENT | Begin only with honest reports and no publishable claim without user approval |

## Current Priority

Harden benchmark reproducibility before adding B6: local verification should
make it obvious which rows are full fresh runs, which are weaker controlled
comparisons, and which evidence is missing. The verifier suite now includes
state, phase-loop, and routing-guard checks through `python tools\verify_all.py`.
