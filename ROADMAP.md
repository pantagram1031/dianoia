# Roadmap

Initialized: 2026-05-20T17:54:05+09:00

## Phase Status

| Phase | Name | Status | Evidence |
|-------|------|--------|----------|
| 0 | VERIFY PRIOR EXPERIMENT | COMPLETE | capability-test/VERIFY_PRIOR.md |
| 1 | DIAGNOSE | COMPLETE | DIAGNOSIS.md |
| 2 | FIX | COMPLETE | AGENTS.md routing guard plus Phase 2 smoke artifacts |
| 3 | RE-TEST SAME PROBLEM | COMPLETE: VALUE_ADDED | capability-test/RETEST.md |
| 4 | EXPAND BENCHMARK BANK | ONGOING | B1-B5 are historical baseline rows; B6+ must build the contamination-free novel objective bank |
| 5 | BUILD SKILLS | COMPLETE | 5/5 skills added and referenced by subagent prompts |
| 6 | BUILD CONNECTORS | COMPLETE | 2/2 connectors added: arxiv, oeis |
| 7 | DOCS | COMPLETE | README.md, ARCHITECTURE.md, EXAMPLES.md, CHANGELOG.md current as of B5/Phase 5/Phase 6 |
| 8 | DEEPER RESEARCH | GATED | Requires 5 contamination-free novel VALUE_ADDED B6+ rows across 3 areas |

## Continuous Improvement Track

The former MASTERPIECE checklist is now a baseline, not a terminal state. The
current victory condition is 5 contamination-free novel VALUE_ADDED
head-to-head benchmarks against raw GPT-5.5 across at least 3 mathematical
areas. Ongoing work should keep improving dianoia's capability, honesty, and
reproducibility toward that evidence standard.

| Track | Status | Next Evidence |
|-------|--------|---------------|
| Benchmark expansion | IN_PROGRESS | Add B6+ contamination-free novel raw-vs-dianoia benchmark with full fresh artifacts |
| Benchmark reproducibility | IN_PROGRESS | Add verifier/runbook/templates that reject weak or simulated rows |
| Phase-loop reliability | IN_PROGRESS | Routing, checkpoint, Reviewer D, and subagent-fire checks are covered by local verifiers; next add smoke checks from real fresh runs |
| Skills/connectors | WATCH | Connector files and subagent wiring are covered by `tools/verify_connectors.py`; add or revise only when benchmark evidence shows a reusable need |
| Docs | WATCH | `tools/verify_dianoia_state.py` checks required docs and referenced capability artifacts; keep README/ARCHITECTURE/EXAMPLES/CHANGELOG synced after substantive changes |
| Deeper research | GATED | Begin only after 5 contamination-free novel VALUE_ADDED B6+ rows across 3 areas |

## Current Priority

Harden benchmark reproducibility before adding B6, then run B6 as the first
forward-objective contamination-free novel benchmark. Local verification should
make it obvious which rows are full fresh runs, which are weaker controlled
comparisons, and which evidence is missing. The verifier suite now includes
state, phase-loop, routing-guard, and connector checks through
`python tools\verify_all.py`.
