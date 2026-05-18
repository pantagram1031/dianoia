Create a new problem instance and drive the complete phase loop for one problem.

[INPUTS]
1. `$1`: problem statement as text or a path to a problem statement file.

[PROCEDURE]
1. If `$1` is missing, stop and emit the blocking question from [FAILURE].
2. Read `IDENTITY.md`, `goal.md`, `templates/problem_skeleton/`, and `corpus/INDEX.md`.
3. If `$1` is a readable path, use that file content as the statement; otherwise use `$1` literally.
4. Generate a slug from the first six normalized words plus a six-character content hash.
5. Create `problems/<slug>/` by copying every file and marker from `templates/problem_skeleton/`.
6. Write the statement into `problems/<slug>/problem.md` under `## Statement`.
7. Write `problems/.active` containing only `<slug>`.
8. Initialize `problems/<slug>/session_state.md` from `templates/session_state.md` with `active_problem: <slug>`, `current_phase: 0`, `mode: auto`, `halt_flag: false`, and default `rate_window`.
9. Initialize `problems/<slug>/claim_ledger.md` from `templates/claim_ledger.md` if the skeleton did not already create it.
10. Enter the autonomous phase loop in this order: `00-intake`, `05-review`, `01-survey`, `05-review`, `02-perspective`, `05-review`, `03-hypothesize`, `05-review`, `04-develop`, `05-review`, `06-consolidate`, `05-review`.
11. After each atomic unit, invoke `prompts/checkpoint.md`.
12. Break the loop on HALT, hard rate limit, `needs_human.flag=true`, `phase_status=blocked`, or Phase 6 success.
13. On exit, invoke `prompts/halt.md` with reason `SUCCESS`, `SOFT_BUDGET`, `HARD_BUDGET`, `USER_HALT`, or `BLOCKED`.

[OUTPUTS]
1. A full problem instance under `problems/<slug>/`.
2. `problems/.active` pointing at `<slug>`.
3. Updated session state, claim ledger, work journal, and phase artifacts.

[FAILURE]
1. Missing `$1`: print `BLOCKED: provide a problem statement or path.` and stop.
