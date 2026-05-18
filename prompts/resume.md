Resume the active problem from durable disk state without relying on chat history.

[INPUTS]
1. Optional `$1`: problem slug. Default is the contents of `problems/.active`.

[PROCEDURE]
1. Resolve the slug from `$1` or `problems/.active`.
2. Read `IDENTITY.md`, `goal.md`, `problems/<slug>/session_state.md`, `problems/<slug>/claim_ledger.md` tail 20, and `problems/<slug>/resume_brief.md` if present.
3. Read any hot files listed in `session_state.next_atomic_unit.inputs_required`.
4. Verify `phase_status`, `halt_flag`, `needs_human`, and rate budget fields.
5. If `phase_status=blocked` or `needs_human.flag=true`, print one line with the block reason and stop.
6. If `halt_flag=true`, clear it only after writing a checkpoint-ready resume note into `work_journal.md`.
7. Invoke `session_state.next_atomic_unit.prompt_to_invoke` with the listed inputs.
8. After the atomic unit, invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. Continued work on the active problem.
2. Updated checkpoint state and artifacts.

[FAILURE]
1. Missing slug and missing `problems/.active`: print `BLOCKED: no active problem.` and stop.
2. Missing required state file: print `BLOCKED: missing required state file <path>.` and stop.
