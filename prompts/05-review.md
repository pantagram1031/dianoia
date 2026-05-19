Run adversarial review passes and force every defect into fixed, deferred, or fatal status.

[INPUTS]
1. Active slug from `problems/.active`.
2. Phase artifact to review.
3. Reviewed phase label, supplied by the caller or inferred from the artifact path: one of `00-intake`, `01-survey`, `02-perspective`, `03-hypothesize`, `04-develop`, `06-consolidate`.
4. Common state: current `claim_ledger.md` tail and `session_state.md`.
5. Phase-dependent context:
   - `00-intake`: `problem.md` and `intake.md`; `survey.md` is not required.
   - `01-survey`: `intake.md`, `survey.md`, and `corpus/INDEX.md`.
   - `02-perspective`: `survey.md`, `perspectives.md`, and `specialists/INDEX.md`.
   - `03-hypothesize`: `intake.md`, `survey.md`, `perspectives.md`, and `hypotheses_live.md`.
   - `04-develop`: `intake.md`, `survey.md`, `hypotheses_live.md`, current proof or failure artifacts, and `work_journal.md`.
   - `06-consolidate`: `survey.md`, `result.md`, `result.fml` when present, `executive_summary.md`, and any proposed corpus entry.

[PRECONDITIONS]
1. The reviewed non-review phase has completed.
2. The specific phase artifact to review exists on disk.
3. The phase-dependent context listed for the reviewed phase exists, except optional files explicitly marked `when present`.

[PROCEDURE]
1. Invoke `prompts/subagents/reviewer.md` with persona `A` for skeptic review.
2. Invoke `prompts/subagents/reviewer.md` with persona `B` for specialist review.
3. Invoke `prompts/subagents/reviewer.md` with persona `C` for editor review.
4. If the reviewed phase is `00-intake`, `03-hypothesize`, `04-develop`, or `06-consolidate`, invoke `prompts/subagents/reviewer.md` with persona `D` for ambition review.
5. Collect all reviewer returns into `problems/<slug>/reviews/`.
6. Consolidate defects into `problems/<slug>/review_consolidated.md`.
7. Mark every defect `FIXED`, `DEFERRED`, or `FATAL`.
8. For `FIXED`, attach the patch or artifact path that resolves the defect.
9. For `DEFERRED`, append a ledger row or deferred-defect entry with reason.
10. For `FATAL`, set the next phase to return to Phase 3 and set `phase_status=blocked` until the return path is written.
11. Invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. Reviewer artifacts under `problems/<slug>/reviews/`.
2. `problems/<slug>/review_consolidated.md`.
3. Updated `session_state.md` and ledger/deferred-defect state.

[FAILURE]
1. Missing review target: print `BLOCKED: no phase artifact supplied for review.` and stop.
2. Missing a phase-dependent input for the reviewed phase: print `BLOCKED: missing review input <path>.` and stop.

[INVARIANTS]
- 05-review MUST be a separate atomic unit invoked AFTER the specific
  phase artifact it reviews exists on disk. Do not interleave review
  work with the phase that produced that artifact.
- Each reviewer persona writes its OWN file in problems/<slug>/reviews/
  BEFORE consolidation:
    reviews/<artifact>-reviewer-A.md  (Skeptic)
    reviews/<artifact>-reviewer-B.md  (Specialist)
    reviews/<artifact>-reviewer-C.md  (Editor)
    reviews/<artifact>-reviewer-D.md  (Ambition, only for gated phases)
- Reviewer A MUST attempt at least one explicit counter-construction
  or precise objection. A reviewer file with zero raised defects is
  itself a defect (insufficient adversarial pressure) and triggers
  re-invocation of that reviewer with a stricter prompt before the
  phase may close.
- Only after all required reviewer files for the reviewed phase exist may
  review_consolidated.md be written.

PERSONA D (v4 Ambition Reviewer):
Reviewer D fires at the 05-review pass for these phases ONLY: 00-intake, 03-hypothesize, 04-develop, 06-consolidate. At other phases only personas A, B, C fire.

Reviewer D answers four mandatory questions in each review file:

1. Did Phase 0 intake retreat from the user's stated problem to a weaker target? If yes, is the retreat earned by a Phase 4 STUCK-STATE recorded in work_journal.md, or is it unprovoked? Unprovoked retreat is severity MAJOR.

2. Does the run's result (current or projected) reproduce, specialize, or weaken a theorem already in survey.md "State of the Art" or in any standard reference predating (current year - 30)? If yes, does result.md headline state the relationship explicitly ("This is a simplified form of [Author Year]" or equivalent)? Failure to state relationship is severity MAJOR.

3. Did at least one Phase 3 hypothesis attempt direct attack on the primary target as defined in intake.md Section A? If no, severity MAJOR.

4. Does the final result.md headline accurately describe the relationship of the proved result to the state of the art? Defensive wording that hides triviality is severity MAJOR. Implication of novelty not actually claimed is severity MAJOR.

Reviewer D MAJOR defects cannot be DEFERRED. They must be FIXED. If a MAJOR defect is unfixable in the current run (e.g. the result is genuinely a textbook re-derivation and cannot be sharpened in this session), halt.md records reason FAILURE-AMBITION-GAP and corpus promotion is blocked. FAILURE-AMBITION-GAP is honest reporting, not system malfunction.
