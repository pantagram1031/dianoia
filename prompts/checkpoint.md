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

[STATUS LINE — MSP R5]
On unit close, after updating session_state.md and merging
work_journal fragments, emit exactly one line to stdout in this
format:

  [<slug> p<phase> u<unit-id> L@<ledger_head> g<open_gaps_count> t<used>/<cap>%]

Example:
  [prove-that-2-is-irrational-35bb78 p3 u03-hypothesize L@C-002 g0 t12/85%]

No additional chat output is permitted at unit close.

[JOURNAL ENTRY CONTENT REQUIREMENTS]
Each checkpoint MUST append exactly one entry to work_journal.md with:

  ## <ISO8601> | <agent> | u<phase-id>
  decisions: <2-4 bullets — what choices were made this phase>
  artifacts: <files written this phase, relative paths>
  ledger_delta: <new ledger row IDs, or "none">
  open: <gaps/conjectures introduced this phase, or "none">

If the phase produced no decisions worth recording, the phase did not
do work — that is a defect to investigate, not an entry to skip.

The status line (MSP R5) is emitted to stdout IMMEDIATELY after the
journal entry is written. No other stdout in checkpoint.md.
