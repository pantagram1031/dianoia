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
| 11 | ATTEMPTS | IN_PROGRESS | R020 and R013 recorded `PARTIAL-PROGRESS`; R013 has unlabeled exact replay through `n=7` |
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
| P11 attempts | IN_PROGRESS | Scale R013 exact poset attempt or use completed R020 replay gate for actual search/proof work |
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
candidate (`research-bank/R001/`). R020 attempt work remains
`PARTIAL-PROGRESS`: dianoia now has solver-independent no-three-in-line
certificate verification plus batch replay of every published certificate in
the local frontier window `N=47` through `N=60`.

R013 is now also `PARTIAL-PROGRESS`: dianoia has exact finite-poset validation,
linear-extension counting, exhaustive labeled-poset replay through five
elements, and canonical unlabeled replay through seven elements with no
counterexample to the base 1/3-2/3 conjecture.

Next P11 target: continue actual mathematical attempts rather than replay
expansion. Prefer R013 structural lemma extraction around the exact small-data
signals in `research-bank/R013/attempt-20260520/STRUCTURAL_NOTES.md`,
especially the width-3 proof target in
`research-bank/R013/attempt-20260520/WIDTH3_EXTREMAL_NOTES.md`: classify
width-3, height-4, rank-layer-shape `2,2,2,1` posets. The restricted class now
has an exact artifact: 103 unlabeled profiles, worst lower probability
`14/39`, next worst `2/5`, a coarse 12-bucket split, a matrix 67-bucket split,
and a fine 103-singleton split. `MATRIX_BUCKET_NOTES.md` now extracts the
3-profile bucket containing the `14/39` extremal, and
`width3-rank2221-extremal-matrix-bucket-n7.json` makes that extraction
reproducible. `RANK_NORMAL_FORM_NOTES.md` now rewrites those cases with stable
rank-layer labels, and `NORMAL_FORM_COUNT_LEDGER.md` certifies the three
orientation counts from named case inputs. `COVER_MATRIX_DERIVATION.md` now
derives the same three forms directly from the cover matrix.
`RECURRENCE_LEDGER.md` now exposes depth-2 recurrences for Cases A/B/C, and
`BRANCH_ENUMERATION_LEDGER.md` reduces those residual branch totals to
terminal chain/shuffle counts for the common cover-matrix subcase.
`MATRIX_BUCKET_ROADMAP.md` ranks the remaining near-boundary matrix buckets,
and `SECOND_MATRIX_BUCKET_NOTES.md` hand-classifies the singleton second bucket
with lower probability `2/5`. `THIRD_MATRIX_BUCKET_NOTES.md` now classifies
the next six-profile `2/5` bucket with generated exact counts and a hand count
for the equality form. `FOURTH_MATRIX_BUCKET_NOTES.md` now classifies the next
four-profile `2/5` bucket similarly. Next target another remaining singleton
`2/5` bucket. `FIFTH_MATRIX_BUCKET_NOTES.md` and
`SIXTH_MATRIX_BUCKET_NOTES.md` now classify those two singletons; next target
the first `13/32` bucket. `SEVENTH_MATRIX_BUCKET_NOTES.md` now classifies that
bucket. `EIGHTH_MATRIX_BUCKET_NOTES.md` now classifies the second `13/32`
bucket. `NEAR_BOUNDARY_SYNTHESIS.md` now abstracts the completed buckets into
residual-count patterns and proof obligations. `FEATURE_PARTITION_NOTES.md`
interprets the thresholded feature partition; next target an all-bucket
feature partition with processed/unprocessed labels.
`ALL_FEATURE_PARTITION_NOTES.md` now records that all-67-bucket partition:
53 feature groups, 8 processed buckets, 59 unprocessed buckets, and 2 mixed
feature groups. Next target: refine the feature key using exact adjacent/skip
vectors or shadowed-skip data to separate the mixed groups.
`VECTOR_FEATURE_PARTITION_NOTES.md` now records that exact adjacent/skip vector
grouping separates the mixed classes: 59 vector feature groups and 0 mixed
processed/unprocessed groups. Next target: extract the eight processed vector
classes into a lemma table and attempt a vector-class dominance argument for
the remaining classes.
`PROCESSED_VECTOR_CLASSES.md` now extracts those eight processed vector classes
as P1-P8 with minimum probabilities, profile counts, adjacent vectors, skip
vectors, and cover matrices. Next target: prove or refute the candidate
vector-class dichotomy.
R020 remains available if the next step is bounded search/proof work rather
than external solver engineering.
