Run adversarial review passes and force every defect into fixed, deferred, or fatal status.

[INPUTS]
1. Active slug from `problems/.active`.
2. Phase artifact to review.
3. `claim_ledger.md`, `survey.md`, and current `session_state.md`.

[PROCEDURE]
1. Invoke `prompts/subagents/reviewer.md` with persona `A` for skeptic review.
2. Invoke `prompts/subagents/reviewer.md` with persona `B` for specialist review.
3. Invoke `prompts/subagents/reviewer.md` with persona `C` for editor review.
4. Collect all reviewer returns into `problems/<slug>/reviews/`.
5. Consolidate defects into `problems/<slug>/review_consolidated.md`.
6. Mark every defect `FIXED`, `DEFERRED`, or `FATAL`.
7. For `FIXED`, attach the patch or artifact path that resolves the defect.
8. For `DEFERRED`, append a ledger row or deferred-defect entry with reason.
9. For `FATAL`, set the next phase to return to Phase 3 and set `phase_status=blocked` until the return path is written.
10. Invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. Reviewer artifacts under `problems/<slug>/reviews/`.
2. `problems/<slug>/review_consolidated.md`.
3. Updated `session_state.md` and ledger/deferred-defect state.

[FAILURE]
1. Missing review target: print `BLOCKED: no phase artifact supplied for review.` and stop.

[INVARIANTS]
- 05-review MUST be a separate atomic unit invoked AFTER 04-develop's
  artifacts exist on disk. Do not interleave with 04-develop.
- Each reviewer persona writes its OWN file in problems/<slug>/reviews/
  BEFORE consolidation:
    reviews/<artifact>-reviewer-A.md  (Skeptic)
    reviews/<artifact>-reviewer-B.md  (Specialist)
    reviews/<artifact>-reviewer-C.md  (Editor)
- Reviewer A MUST attempt at least one explicit counter-construction
  or precise objection. A reviewer file with zero raised defects is
  itself a defect (insufficient adversarial pressure) and triggers
  re-invocation of that reviewer with a stricter prompt before the
  phase may close.
- Only after all three reviewer files exist may
  review_consolidated.md be written.

PERSONA D (v4 Ambition Reviewer):
Reviewer D fires at the 05-review pass for these phases ONLY: 00-intake, 03-hypothesize, 04-develop, 06-consolidate. At other phases only personas A, B, C fire.

Reviewer D answers four mandatory questions in each review file:

1. Did Phase 0 intake retreat from the user's stated problem to a weaker target? If yes, is the retreat earned by a Phase 4 STUCK-STATE recorded in work_journal.md, or is it unprovoked? Unprovoked retreat is severity MAJOR.

2. Does the run's result (current or projected) reproduce, specialize, or weaken a theorem already in survey.md "State of the Art" or in any standard reference predating (current year - 30)? If yes, does result.md headline state the relationship explicitly ("This is a simplified form of [Author Year]" or equivalent)? Failure to state relationship is severity MAJOR.

3. Did at least one Phase 3 hypothesis attempt direct attack on the primary target as defined in intake.md Section A? If no, severity MAJOR.

4. Does the final result.md headline accurately describe the relationship of the proved result to the state of the art? Defensive wording that hides triviality is severity MAJOR. Implication of novelty not actually claimed is severity MAJOR.

Reviewer D MAJOR defects cannot be DEFERRED. They must be FIXED. If a MAJOR defect is unfixable in the current run (e.g. the result is genuinely a textbook re-derivation and cannot be sharpened in this session), halt.md records reason FAILURE-AMBITION-GAP and corpus promotion is blocked. FAILURE-AMBITION-GAP is honest reporting, not system malfunction.
