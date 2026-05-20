Resume the active problem from durable disk state without relying on chat history.

[INPUTS]
1. Optional `$1`: problem slug. Default is the contents of `problems/.active`.

[PRECONDITIONS]
1. If `$1` is absent, `problems/.active` exists and contains exactly one slug.
2. A slug is a problem directory name, not a free-form problem statement.
3. Resume is only for continuing an existing `BLOCKED-ITERATE` problem. It is
   never the router for a fresh theorem/problem statement.
4. If the active problem is closed, do not append new user content to it. Fresh
   problem statements must go through `prompts/prove.md`.

[PROCEDURE]
1. Resolve the slug from `$1` or `problems/.active`.
2. Read `IDENTITY.md`, `goal.md`, `problems/<slug>/session_state.md`, `problems/<slug>/claim_ledger.md` tail 20, and `problems/<slug>/resume_brief.md` if present.
3. Read any hot files listed in `session_state.next_atomic_unit.inputs_required`.
4. Verify `phase_status`, `halt_flag`, `needs_human`, rate budget fields, and the most recent halt reason in `resume_brief.md`.
5. If the prior halt reason is `SUCCESS-MEANINGFUL` or `FAILURE-AMBITION-GAP`, print `BLOCKED: problem is closed with halt_reason=<reason>.` and stop without clearing `halt_flag`.
6. If `phase_status=blocked` or `needs_human.flag=true`, print one line with the block reason and stop.
7. If `halt_flag=true` and the prior halt reason is not `BLOCKED-ITERATE`, print `BLOCKED: halt_flag true without resume-eligible halt reason.` and stop.
8. If `halt_flag=true` and the prior halt reason is `BLOCKED-ITERATE`, clear it only after writing a checkpoint-ready resume note into `work_journal.md`.
9. Invoke `session_state.next_atomic_unit.prompt_to_invoke` with the listed inputs.
10. After the atomic unit, invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. Continued work on the active problem.
2. Updated checkpoint state and artifacts.

[FAILURE]
1. Missing slug and missing `problems/.active`: print `BLOCKED: no active problem.` and stop.
2. Missing required state file: print `BLOCKED: missing required state file <path>.` and stop.
3. Malformed `problems/.active` with zero, multiple, or whitespace-only slugs:
   print `BLOCKED: malformed active problem pointer.` and stop.
4. `$1` looks like a fresh problem statement rather than an existing slug:
   print `BLOCKED: fresh problem statements use prompts/prove.md.` and stop.

INVARIANTS (v4 resume discipline):
- Only `BLOCKED-ITERATE` is resume-eligible. `SUCCESS-MEANINGFUL` and `FAILURE-AMBITION-GAP` are closed states and MUST NOT have `halt_flag` cleared by resume.
- Closed problems are immutable except for explicit supersession notes written
  by `prompts/prove.md`; resume MUST NOT write mathematical content into a
  closed problem.
- On resume from a BLOCKED-ITERATE problem, do NOT re-run Phase 0 intake. Read prior session_state.md, the most recent STUCK-STATE entry in work_journal.md, and the NEXT-SESSION ATTACK PLAN in resume_brief.md.
- Phase 3 hypotheses for the new session must include the refined attack plan as at least one hypothesis. The original direct attack from the first session is restated and re-tested at this point.
- The new session may invoke SpecialistFactory if the refined attack plan names a specialist domain not present in specialists/INDEX.md.
- The new session may invoke the Researcher subagent to investigate the specific obstruction named in the prior STUCK-STATE.
- session_state.session_count increments by 1 at session start. session_state.attempt_log gains a new entry after Phase 4.
- A resumed session that produces the same STUCK-STATE as the prior session without a new attack angle is itself a Reviewer D MAJOR defect at Phase 4. Each session must try something the prior sessions did not.
