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
7. Write or refresh `problems/<slug>/context_manifest.md` from `templates/context_manifest.md` for the just-completed unit, filling `always`, `phase_active`, `this_unit`, and `dropped`.
8. Update `last_atomic_unit_completed`, `next_atomic_unit`, `ledger_head`, `rate_window`, `context`, and `forbidden_word_count`.
9. On any integrity failure, set `phase_status=blocked`, set `needs_human.flag=true`, and write the reason.
10. Emit only the MSP R5 status line.

[OUTPUTS]
1. Updated `session_state.md`.
2. Updated `claim_ledger.md` and `work_journal.md`.
3. Updated `context_manifest.md` for the just-completed unit.
4. Integrity inventory recorded in the active problem directory.

[FAILURE]
1. Missing active state: print `BLOCKED: cannot checkpoint without session_state.md.` and stop.

[STATUS LINE ??MSP R5]
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
  decisions: <2-4 bullets ??what choices were made this phase>
  artifacts: <files written this phase, relative paths>
  ledger_delta: <new ledger row IDs, or "none">
  open: <gaps/conjectures introduced this phase, or "none">

If the phase produced no decisions worth recording, the phase did not
do work ??that is a defect to investigate, not an entry to skip.

The status line (MSP R5) is emitted to stdout IMMEDIATELY after the
journal entry is written. No other stdout in checkpoint.md.

[CONTEXT MANIFEST REQUIREMENTS]
Each checkpoint MUST write `problems/<slug>/context_manifest.md` using
`templates/context_manifest.md`. The manifest records:

  always: constitutional anchors, active session state, and ledger.
  phase_active: the current phase prompt and phase-level artifact(s).
  this_unit: artifacts written, reviewed, or merged in this atomic unit.
  dropped: files or summaries deliberately omitted from immediate
           context, with recovery path or summary pointer.

The manifest is rewritten at every checkpoint to describe the unit
that just closed. It is not a proof artifact and does not create
ledger rows.

[NEEDS_HUMAN GATE]
Set `needs_human.flag=true` only when the system is genuinely blocked
and the next required information cannot be derived from active
artifacts, corpus entries, specialist profiles, survey/researcher
work, or bounded subagent attempts.

Before setting the flag, write a `needs_human` block in
`session_state.md` with:

  reason: <one-sentence blocker>
  exhausted:
    - <artifact, corpus, specialist, web/research, or subagent path checked>
  question: <specific user question>
  allowed_answers: <short options or expected shape of answer>
  resumes_at: <next_atomic_unit prompt and artifact>

Do NOT set `needs_human.flag=true` merely because a proof attempt is
hard, a direct attack is stuck, a citation is currently unverified, a
fallback is tempting, or a phase produced a `[GAP]`. Those cases must
be handled as STUCK-STATE, `[REFERENCE NEEDS VERIFICATION]`,
fallback-chain evidence, or ordinary open gaps unless a specific user
decision is truly required.
[CONTEXT MANIFEST EVIDENCE GATE]
A checkpoint manifest is invalid if it only names broad categories.
It MUST include concrete paths or explicit `none` values for:

- `phase_prompt`
- `phase_active.artifact`
- `phase_active.required_inputs`
- `phase_active.produced_outputs`
- `this_unit.artifacts_written`
- `this_unit.artifacts_reviewed`
- `this_unit.reviewer_files` when closing a review unit
- `this_unit.subagent_returns` when subagents fired
- `this_unit.journal_fragments_merged`
- `this_unit.ledger_delta`
- `this_unit.open_markers`
- `checkpoint_evidence.forbidden_word_scan`
- `checkpoint_evidence.citation_check`
- `checkpoint_evidence.review_status`
- `checkpoint_evidence.next_atomic_unit`

Skeletal manifests are invalid. If a field does not apply, write
`none` and the reason. If context was dropped, each dropped item must
include a recovery path or summary pointer.
