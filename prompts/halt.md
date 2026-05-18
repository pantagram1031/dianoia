Wind down the active problem into a resumable state.

[INPUTS]
1. Trigger reason: `SUCCESS`, `SOFT_BUDGET`, `HARD_BUDGET`, `USER_HALT`, or `BLOCKED`.
2. Active slug from `problems/.active` unless a slug is supplied by the caller.

[PROCEDURE]
1. Refuse to begin any new atomic unit.
2. Read `IDENTITY.md`, `goal.md`, and `problems/<slug>/session_state.md`.
3. Determine whether the current unit is below 50 percent completion from session notes; if so, roll back to the last checkpoint marker.
4. If the current unit is at least 50 percent complete and the trigger is not `HARD_BUDGET`, finish only the minimal persistence work required to close that unit.
5. Sweep orphan mathematical content from chat, scratch notes, and subagent inbox fragments into `problems/<slug>/work_journal.md`.
6. Append any pending ledger rows; never rewrite an existing row.
7. Update `phase_status`, `last_atomic_unit_completed`, `next_atomic_unit`, and `needs_human`.
8. For non-hard and non-emergency triggers, distill a compact digest of results since the last phase close.
9. Write `problems/<slug>/resume_brief.md` with current phase, next unit, open gaps, deferred defects, hot files, and block reasons.
10. Print a digest of at most 10 lines and exit.

[OUTPUTS]
1. `problems/<slug>/resume_brief.md`.
2. Updated `session_state.md`, `work_journal.md`, and `claim_ledger.md`.
3. A stdout digest of at most 10 lines.

[FAILURE]
1. Missing active problem: print `BLOCKED: no active problem to halt.` and stop.
