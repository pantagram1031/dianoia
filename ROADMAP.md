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
| 9 | RESEARCH INFRA | IN_PROGRESS | Build formal-check, openness-verification, and adversarial-novelty infrastructure |
| 10 | CURATION | PENDING | Requires research-bank with 20 verified-open candidates across 4 areas |
| 11 | ATTEMPTS | PENDING | Requires curated research-bank candidate selection |
| 12 | VERIFICATION GATE | PENDING | Mandatory for any SOLVED-CLAIM |
| 13 | INTERMEDIATE WINS | PENDING | Draft note plus BLOCKED_ON_USER before any external claim |

## Research Contribution Track

The user updated the active goal to RESEARCH_CONTRIBUTION. The prior
MASTERPIECE baseline remains complete evidence, but the live objective is now a
verifiable mathematical contribution that survives openness confirmation,
adversarial novelty review, and formal/computational checking where applicable.
No solved or publishable claim may be self-declared; a successful gate halts
for external mathematician review.

| Track | Status | Next Evidence |
|-------|--------|---------------|
| P9 infra | IN_PROGRESS | `connectors/lean/`, enhanced arXiv lookup, openness skill, adversarial novelty skill |
| P10 curation | PENDING | `research-bank/INDEX.md` with 20 verified-open candidates across 4 areas |
| P11 attempts | PENDING | One candidate attempt log per session after P10 seed set exists |
| P12 verification | PENDING | `CLAIMS.md` rows with gates, confidence, and downgrade/blocked status |
| P13 notes | PENDING | `research-bank/<id>/draft-note.md` for any intermediate win |

## Continuous Improvement Track

Legacy heading retained for verifier compatibility. The old continuous
improvement benchmark track is now subordinate to the RESEARCH_CONTRIBUTION
goal.

## Benchmark Baseline

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

P9 INFRA. Build local tooling and prompts so later research attempts cannot
mistake stale literature, renamed known results, or unverified proofs for a
contribution. First concrete deliverables: Lean formal-check wrapper, enhanced
arXiv/open-search support, openness-verification skill, adversarial-novelty
skill, and Researcher prompt wiring.
