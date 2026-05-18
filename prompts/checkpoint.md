Close one atomic unit by persisting claims, journals, integrity checks, and next-state fields.

[INPUTS]
1. Active slug from `problems/.active`.
2. Current atomic-unit artifacts named by `session_state.md`.

[PROCEDURE]
1. Read `IDENTITY.md`, `goal.md`, and `problems/<slug>/session_state.md`.
2. Append new claim rows from the unit artifact into `problems/<slug>/claim_ledger.md`.
3. Merge `problems/<slug>/inbox/<unit-id>/journal-fragment.md` files into `problems/<slug>/work_journal.md` with timestamp and source attribution.
4. Run a citation check: every citation-like token used for reasoning must match a `claim_ledger.md` row or be tagged `[UNVERIFIED]`.
5. Run the forbidden vocabulary scan for the words listed in `goal.md`; record count and locations.
6. Inventory every `[GAP]`, `[ASSUMPTION]`, and `[CONJECTURE]` marker in the unit artifact.
7. Update `last_atomic_unit_completed`, `next_atomic_unit`, `ledger_head`, `rate_window`, `context`, and `forbidden_word_count`.
8. On any integrity failure, set `phase_status=blocked`, set `needs_human.flag=true`, and write the reason.
9. Emit only the MSP R5 status line.

[OUTPUTS]
1. Updated `session_state.md`.
2. Updated `claim_ledger.md` and `work_journal.md`.
3. Integrity inventory recorded in the active problem directory.

[FAILURE]
1. Missing active state: print `BLOCKED: cannot checkpoint without session_state.md.` and stop.
