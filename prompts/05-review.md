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
