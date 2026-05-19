Consult one registered specialist on a bounded mathematical sub-question.

[INPUTS]
1. Active slug from `problems/.active`.
2. Specialist slug from `specialists/INDEX.md`.
3. A concrete sub-question, obstruction, gap, or proposed move to evaluate.

[PRECONDITIONS]
1. `problems/.active` names exactly one slug.
2. `specialists/INDEX.md` contains the requested specialist slug.
3. `specialists/<specialist>/PROFILE.md` exists.
4. The active problem directory exists with `problem.md`, `session_state.md`, and `claim_ledger.md`.

[PROCEDURE]
1. Read `IDENTITY.md`, `goal.md`, `specialists/_meta/etiquette.md`, the requested specialist profile, active problem summary, ledger tail, open gaps, and `survey.md` when present.
2. Answer the requested sub-question first, following `Consult Mode` in `specialists/_meta/etiquette.md`.
3. Separate proved statements, cited facts, heuristics, and conjectural suggestions.
4. End with the next best testable sub-question.
5. Write the consult artifact to `problems/<slug>/dialogue/consult-<specialist>-<unit-id>.md`.
6. Do not add claims to `claim_ledger.md` unless a later Director checkpoint promotes a precise, supported claim.
7. Invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. `problems/<slug>/dialogue/consult-<specialist>-<unit-id>.md`.

[FAILURE]
1. Missing active problem: print `BLOCKED: no active problem for consult.` and stop.
2. Unknown specialist slug: print `BLOCKED: unknown specialist <slug>.` and stop.
3. Missing sub-question: print `BLOCKED: consult requires a concrete sub-question.` and stop.
