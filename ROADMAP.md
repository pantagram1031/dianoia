# Roadmap

Initialized: 2026-05-20T17:54:05+09:00

## Phase Status

| Phase | Name | Status | Evidence |
|-------|------|--------|----------|
| 0 | VERIFY PRIOR EXPERIMENT | COMPLETE | capability-test/VERIFY_PRIOR.md |
| 1 | DIAGNOSE | COMPLETE | DIAGNOSIS.md |
| 2 | FIX | IN_PROGRESS | prompts/prove.md patch smoke-tested; R1 router risk remains |
| 3 | RE-TEST SAME PROBLEM | PENDING | capability-test/RETEST.md pending |
| 4 | EXPAND BENCHMARK BANK | BLOCKED_BY_PHASE_3 | BENCHMARK.md initialized |
| 5 | BUILD SKILLS | BLOCKED_BY_PHASE_3_ROTATION | skills/INDEX.md exists, no SKILL.md entries yet |
| 6 | BUILD CONNECTORS | BLOCKED_BY_PHASE_3_ROTATION | connectors/ absent |
| 7 | DOCS | BLOCKED_BY_PHASE_3_ROTATION | README.md stale; ARCHITECTURE.md absent |
| 8 | DEEPER RESEARCH | GATED | Requires 5 VALUE_ADDED rows across 3 areas |

## Current Priority

Continue Phase 2 fixes in DIAGNOSIS.md severity order. The prompt-level
`prove.md` stale-active guard passed smoke testing; remaining R1 risk may
require constitutional `AGENTS.md` approval if no prompt-only mitigation can
make first-message routing deterministic.
