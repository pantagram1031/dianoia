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
| 9 | RESEARCH INFRA | COMPLETE | `connectors/lean/`, enhanced `connectors/arxiv/`, openness/novelty skills, research-state verifier, and candidate templates |
| 10 | CURATION | COMPLETE | `research-bank/INDEX.md` records 20 `OPEN-VERIFIED` candidates across 10 areas |
| 11 | ATTEMPTS | READY | P10 gate satisfied; begin candidate attempts from highest-tractability bank entries |
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
| P9 infra | COMPLETE | `connectors/lean/`, enhanced arXiv lookup, openness skill, adversarial novelty skill, `tools/verify_research_state.py`, `templates/research_candidate/` |
| P10 curation | COMPLETE | `research-bank/INDEX.md` with 20 verified-open candidates across 10 areas |
| P11 attempts | READY | First attempt should target a rank A candidate with exact-checkable artifacts |
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

P11 ATTEMPTS. P10 curation is complete: `research-bank/INDEX.md` records 20
`OPEN-VERIFIED` candidates across 10 areas, plus one `OPEN-WEAK` warm-up
candidate (`research-bank/R001/`). Begin attempts from rank A/B candidates
whose subtargets have exact certificate paths.

Recommended first P11 target: `research-bank/R020/` no-three-in-line, rank A.
Reason: it has current 2026 CSP frontier evidence, exact integer
collinearity checks, and a natural first deliverable: replay one known
`D(n)=2n` certificate with an auditable verifier before searching beyond the
frontier. Alternative rank A target: `research-bank/R013/` 1/3-2/3 posets,
where exact linear-extension counts provide similarly replayable artifacts.
