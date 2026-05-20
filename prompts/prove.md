Create a new problem instance and drive the complete phase loop for one problem.

[INPUTS]
1. `$1`: problem statement as text or a path to a problem statement file.

[PRECONDITIONS]
1. `$1` is present and non-empty after trimming whitespace.
2. If `problems/.active` exists, it names exactly one slug or is treated as
   malformed stale state. Malformed stale state MUST NOT receive new problem
   content.
3. If `problems/.active` names an existing problem whose `session_state.md`
   has `halt_flag: true` with halt reason `SUCCESS-MEANINGFUL` or
   `FAILURE-AMBITION-GAP`, the old problem is closed. A new problem statement
   MUST create a fresh slug; do not resume, append to, or mutate mathematical
   artifacts of the closed problem.
4. If `problems/.active` names an existing problem with `halt_flag: true` and
   no resume-eligible `BLOCKED-ITERATE` halt reason, treat it as closed stale
   state for fresh problem creation.
5. If `problems/.active` names an open problem and `$1` is not explicitly a
   continuation, still create a fresh slug for a fresh problem statement. Use
   `prompts/resume.md` for continuation.

[PROCEDURE]
1. If `$1` is missing, stop and emit the blocking question from [FAILURE].
2. Read `IDENTITY.md`, `goal.md`, `templates/problem_skeleton/`, `templates/session_state.md`, `templates/claim_ledger.md`, and `corpus/INDEX.md`.
3. Inspect `problems/.active` if present:
   - If absent, continue fresh.
   - If it does not contain exactly one slug, record `superseded_active: malformed` in the new `work_journal.md` after skeleton creation and continue fresh.
   - If it names a slug whose `session_state.md` is missing, record `superseded_active: missing-state <slug>` in the new `work_journal.md` after skeleton creation and continue fresh.
   - If it names a closed problem (`halt_flag: true` with halt reason `SUCCESS-MEANINGFUL`, `FAILURE-AMBITION-GAP`, or any non-`BLOCKED-ITERATE` reason), append a timestamped supersession note to `problems/<old-slug>/work_journal.md` stating that a fresh problem statement is being routed to a new slug, then continue fresh.
   - If it names an open problem, do not append `$1` to that problem. Continue fresh unless the caller explicitly invoked `prompts/resume.md`.
4. If `$1` is a readable path, use that file content as the statement; otherwise use `$1` literally.
5. Generate a slug from the first six normalized words plus a six-character content hash.
6. Create `problems/<slug>/` by copying every file and marker from `templates/problem_skeleton/`.
7. Write the statement into `problems/<slug>/problem.md` under `## Statement`.
8. If Step 3 detected malformed or missing stale active state, write the corresponding `superseded_active` note into `problems/<slug>/work_journal.md` before intake.
9. Write `problems/.active` containing only `<slug>`.
10. Initialize `problems/<slug>/session_state.md` from `templates/session_state.md` with `active_problem: <slug>`, `current_phase: 0`, `mode: auto`, `msp_narration: quiet`, `halt_flag: false`, and default `rate_window`.
11. Initialize `problems/<slug>/claim_ledger.md` from `templates/claim_ledger.md` if the skeleton did not already create it.
12. Immediately invoke `prompts/00-intake.md`. Do not emit chat output or proceed to later phases until `problems/<slug>/intake.md` exists.
13. Enter the remaining autonomous phase loop in this order: `05-review`, `01-survey`, `05-review`, `02-perspective`, `05-review`, `03-hypothesize`, `05-review`, `04-develop`, `05-review`, `06-consolidate`, `05-review`.
14. After each atomic unit, invoke `prompts/checkpoint.md`.
15. Break the loop on HALT, hard rate limit, `needs_human.flag=true`, `phase_status=blocked`, or Phase 6 success.
16. On exit, invoke `prompts/halt.md` with reason `SUCCESS`, `SOFT_BUDGET`, `HARD_BUDGET`, `USER_HALT`, or `BLOCKED`.

[OUTPUTS]
1. A full problem instance under `problems/<slug>/`.
2. `problems/.active` pointing at `<slug>`.
3. Updated session state, claim ledger, work journal, and phase artifacts.
4. If stale active state existed, supersession evidence in either the old
   closed problem journal or the new problem journal.

[FAILURE]
1. Missing `$1`: print `BLOCKED: provide a problem statement or path.` and stop.

[POST-INVOCATION SILENCE]
Do NOT echo the result, proof, or summary to chat. Chat output for the
entire invocation is limited to the wind-down digest (≤10 lines, fixed
schema from prompts/halt.md). The file IS the deliverable. A bare file
path pointer is the only chat output permitted after wind-down.

[PHASE LOOP DISCIPLINE]
- After EACH phase prompt (00..06) completes, prompts/checkpoint.md
  MUST be invoked as a separate atomic unit BEFORE the next phase
  prompt is read. This is non-negotiable; merging phases into a
  single edit is a violation.
- After Phase 6 closes successfully, prompts/halt.md MUST be invoked
  with trigger reason SUCCESS to emit the wind-down digest. Returning
  a file pointer without running halt.md is incomplete.
- A successful invocation ends with halt.md's 10-line digest written
  to stdout, followed by the result.md path. Nothing else.

[BATCHING PROHIBITED]
- Phases 00 through 06 MUST be executed strictly sequentially.
- Each phase produces its own commit-worthy set of artifacts before
  the next phase begins. Reading multiple phase prompt files into
  context up-front is permitted; writing outputs for multiple phases
  in one edit pass is NOT.
- After each phase's artifacts are written, prompts/checkpoint.md
  MUST be invoked as a separate atomic unit. checkpoint.md is the
  ONLY place where work_journal.md is updated and the status line is
  emitted. Inline work_journal updates inside a phase artifact write
  are violations.
- Equivalently: there must be exactly one work_journal.md entry per
  phase per invocation, no more and no fewer.
