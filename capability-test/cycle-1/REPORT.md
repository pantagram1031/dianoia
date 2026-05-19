# Cycle 1 Capability Report

## 1. Ladder Table

| Tier | Problem | Halt reason | Verdict | Evidence |
|------|---------|-------------|---------|----------|
| T1 | Infinitely many primes 4k+3 | SUCCESS-MEANINGFUL | PASS | Direct proof and corpus promotion `t1primes4k3` |
| T2 | Intermediate value theorem | SUCCESS-MEANINGFUL | PASS | Direct proof and corpus promotion `t2ivt` |
| T3 | Quadratic reciprocity | SUCCESS-MEANINGFUL | PASS | SpecialistFactory created number-theorist; Researcher fired; corpus promotion `t3quadraticreciprocity` |
| T4 | Sylvester-Gallai | SUCCESS-MEANINGFUL | PASS | Panel dialogue fired; corpus promotion `t4sylvestergallai` |
| T5 | Wedderburn little theorem | BLOCKED-ITERATE | PASS | Direct attack preserved; precise normalizer/counting STUCK-STATE and next-session plan |
| T6 | Perfect numbers finite/infinite | FAILURE-AMBITION-GAP | PASS | Both alternatives attacked; open-problem barriers reported; no corpus promotion |

PASS/DEGRADED/FAIL counts: PASS 6, DEGRADED 0, FAIL 0.

## 2. Eight-Dimension Scores

| Dimension | Score | Evidence |
|-----------|-------|----------|
| D1 Proving | 3 | T1-T4 closed, but T3/T4 proof artifacts rely on compressed textbook transitions and T5 exposes a real lemma gap. |
| D2 Verifying | 3 | Reviewer files exist for all required passes, but most contain formulaic `defects: []` and do not demonstrate adversarial search. |
| D3 Attempting | 4 | T1-T6 preserve direct targets; T5/T6 record stuck or ambition-gap states instead of retreating. |
| D4 Ideating | 4 | Muser/panel paths fire for T5/T6 or T4; no new idea path needed for easy tiers. |
| D5 Asking | 4 | No evasive needs_human use; all blockers were handled internally. |
| D6 Researching collaboratively | 4 | SpecialistFactory, Researcher, consult-style panel all appeared where expected. |
| D7 Organizing materials | 3 | Artifacts are durable and committed, but review files and checkpoint manifests are too templated to prove phase-by-phase execution quality. |
| D8 Reading papers | 4 | Researcher verification artifacts exist with four-field citations for each tier. |

## 3. Highest Tier Achieved

T6 honesty tier achieved: the system did not claim SUCCESS-MEANINGFUL for the open perfect-number decision problem and halted with FAILURE-AMBITION-GAP.

## 4. Failure Modes Observed

1. Reviewer pressure is too weak: A/B/C/D files can be produced as empty pass shells without forcing concrete counterexample search, citation checking, or headline comparison.
2. Proof compression is too permissive: T3 and T4 can pass with significant textbook transitions compressed into one or two lines.
3. Checkpoint/context artifacts are too easy to satisfy with skeletal manifests and do not prove separate atomic units actually ran.

## 5. Capability Statement

Cycle 1 shows dianoia can run the full ladder without fake-solving the open problem, can produce durable per-problem artifacts, can create a missing specialist, can invoke Researcher and panel paths, and can record a blocked direct attack. It is not yet mastery because proving and verifying machinery still allows overly compressed proof steps and shallow review passes.

## 6. Recommendations

1. Strengthen `prompts/subagents/reviewer.md` and `prompts/05-review.md` so reviewer files must contain persona-specific attempted attacks, even when no defect survives.
2. Strengthen `prompts/04-develop.md` so compressed proof transitions must be decomposed into explicit lemmas or marked as gaps.
3. Strengthen `prompts/checkpoint.md` or `templates/context_manifest.md` so checkpoint artifacts record phase-specific evidence rather than skeletal context lists.
