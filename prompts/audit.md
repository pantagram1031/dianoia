Audit produced artifacts for identity drift, integrity violations, and unsafe rule relaxation.

[INPUTS]
1. Active slug from `problems/.active`.
2. Optional audit range or artifact list.

[PROCEDURE]
1. Re-read `IDENTITY.md` and `goal.md`.
2. Determine the audit range from the last audit marker or the supplied artifact list.
3. Scan all artifacts in range for forbidden vocabulary, unledgered citations, tone drift, and claimed rule relaxations.
4. Check every mathematical claim against `claim_ledger.md` status and dependency discipline.
5. Write `problems/<slug>/audit.md` with findings, evidence paths, severity, and required action.
6. If drift is detected, roll back to the last clean checkpoint and set `phase_status=blocked`.
7. If no drift is detected, append the audit marker to `session_state.md` and continue the next planned unit.

[OUTPUTS]
1. `problems/<slug>/audit.md`.
2. Updated `session_state.md` when drift or audit completion changes state.

[FAILURE]
1. Missing active problem: print `BLOCKED: no active problem to audit.` and stop.
