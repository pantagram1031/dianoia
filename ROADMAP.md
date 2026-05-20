# Roadmap

Initialized: 2026-05-20T17:54:05+09:00

## Phase Status

| Phase | Name | Status | Evidence |
|-------|------|--------|----------|
| 0 | VERIFY PRIOR EXPERIMENT | COMPLETE | capability-test/VERIFY_PRIOR.md |
| 1 | DIAGNOSE | COMPLETE | DIAGNOSIS.md |
| 2 | FIX | IN_PROGRESS | prompts/templates patches pending |
| 3 | RE-TEST SAME PROBLEM | PENDING | capability-test/RETEST.md pending |
| 4 | EXPAND BENCHMARK BANK | BLOCKED_BY_PHASE_3 | BENCHMARK.md initialized |
| 5 | BUILD SKILLS | BLOCKED_BY_PHASE_3_ROTATION | skills/INDEX.md exists, no SKILL.md entries yet |
| 6 | BUILD CONNECTORS | BLOCKED_BY_PHASE_3_ROTATION | connectors/ absent |
| 7 | DOCS | BLOCKED_BY_PHASE_3_ROTATION | README.md stale; ARCHITECTURE.md absent |
| 8 | DEEPER RESEARCH | GATED | Requires 5 VALUE_ADDED rows across 3 areas |

## Current Priority

Begin Phase 2 fixes in DIAGNOSIS.md severity order. First patch should address
R1/R2 as far as possible within non-constitutional prompt files, then run the
required stale `.active` smoke test.
