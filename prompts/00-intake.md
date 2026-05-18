Convert a raw problem statement into a formal investigation brief and initialized state.

[INPUTS]
1. Active slug from `problems/.active`.
2. `problems/<slug>/problem.md`.

[PROCEDURE]
1. Read `IDENTITY.md`, `goal.md`, `corpus/INDEX.md`, and the active `problem.md`.
2. Write `problems/<slug>/intake.md` section A: formal restatement with all quantifiers explicit and every symbol defined.
3. Write section B: classification using MSC 2020 codes and problem type such as open, proof, disproof, construction, classification, computation, or reformulation.
4. Write section C: success criteria as the applicable subset of meta-goal outputs (a) through (e).
5. Write section D: scope and out-of-scope adjacent problems.
6. Write section E: a risk register with the top three failure modes and their defenses.
7. Write section F: initialized ledger and session-state summary.
8. Initialize `claim_ledger.md` and `session_state.md` if they are absent.
9. Search `corpus/INDEX.md` by MSC and preload relevant prior theorems as `CITED` rows with all four citation fields.
10. Invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. `problems/<slug>/intake.md`.
2. Initialized or updated `claim_ledger.md` and `session_state.md`.

[FAILURE]
1. Missing `problem.md`: print `BLOCKED: missing problem statement.` and stop.
