Consolidate established work into final result artifacts and promote eligible theorems to the corpus.

[INPUTS]
1. Active slug from `problems/.active`.
2. `claim_ledger.md`.
3. Surviving proof, obstruction, falsification, reformulation, or conjecture artifacts.

[PRECONDITIONS]
1. Phase 4 develop has completed.
2. `claim_ledger.md` exists and records the statuses of all claims needed for consolidation.
3. At least one proof, failure, obstruction, falsification, reformulation, or conjecture artifact from Phase 4 exists for consolidation.

[PROCEDURE]
1. Read all `PROVED` and `CITED` ledger rows needed for the result.
2. Choose the strongest honest result type from meta-goal outputs (a) through (e).
3. Write `problems/<slug>/result.md` with a one-sentence headline stating exactly what was established.
4. Write the formal statement with all assumptions explicit.
5. Write the full proof or evidence chain, with every step backed by ledger rows.
6. Write significance, residual obstruction, and two to five concrete open problems.
7. Write `problems/<slug>/result.fml` as the WN source of truth when a formal theorem, obstruction, or reformulation exists.
8. Write `problems/<slug>/executive_summary.md` in at most 250 words.
9. Promote eligible `PROVED` ledger rows to `corpus/theorems/<sha12>.fml` after light review.
10. Update `corpus/INDEX.md`.
11. Invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. `problems/<slug>/result.md`.
2. `problems/<slug>/result.fml`.
3. `problems/<slug>/executive_summary.md`.
4. Optional promoted theorem files and updated `corpus/INDEX.md`.

[FAILURE]
1. No established result: print `BLOCKED: no consolidated result survived review.` and stop.

[POST-INVOCATION SILENCE]
Do NOT echo the result, proof, or summary to chat. Chat output for the
entire invocation is limited to the wind-down digest (≤10 lines, fixed
schema from prompts/halt.md). The file IS the deliverable. A bare file
path pointer is the only chat output permitted after wind-down.

[CORPUS SELF-CONTAINMENT]
- corpus/theorems/<sha12>.fml MUST contain the full WN content:
  definitions used, all supporting lemmas with proofs, and the main
  theorem with proof. A pointer to problems/<slug>/proofs/*.fml is
  insufficient.
- The corpus entry must be readable and verifiable WITHOUT opening
  any file under problems/. The origin_problem field records
  provenance only; downstream problems must be able to consume the
  corpus entry standalone.
- If a proof is too long for inline inclusion (>500 lines), inline
  the theorem statement and the top-level proof skeleton, then
  reference the full lemma stack by ID — but the lemma statements
  and proofs themselves must also be in the corpus entry or in
  separate corpus/theorems/<sha12>.fml entries.

INVARIANTS (v4 meaningfulness gate):
Before corpus promotion, the result must pass the meaningfulness test:

(a) Direct attack closed with proof → MEANINGFUL. Promote.
(b) Direct attack stuck, but the STUCK-STATE names an obstruction or technique-class failure not recorded in any prior corpus entry, prior session attempt_log, or survey.md citation → MEANINGFUL. Promote with headline acknowledging partial nature and the precise newly-identified obstacle.
(c) Result strictly stronger than the strongest survey.md "State of the Art" entry (proves more, requires less, or has a strictly weaker hypothesis) → MEANINGFUL. Promote with explicit comparison in headline.
(d) Result equivalent to or weaker than a survey.md "State of the Art" entry, OR re-derivation of any textbook fact → NOT MEANINGFUL. Block corpus promotion. Halt reason becomes BLOCKED-ITERATE if attack angles remain, FAILURE-AMBITION-GAP if exhausted.

Reviewer D MAJOR defects unfixed at this phase force halt reason FAILURE-AMBITION-GAP regardless of (a)/(b)/(c)/(d).
