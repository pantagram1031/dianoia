Run a bounded multi-specialist panel on a concrete disagreement or attack choice.

[INPUTS]
1. Active slug from `problems/.active`.
2. Two or three specialist slugs from `specialists/INDEX.md`.
3. A concrete disagreement, attack choice, obstruction, or hypothesis-ranking question.

[PRECONDITIONS]
1. `problems/.active` names exactly one slug.
2. Each requested specialist appears in `specialists/INDEX.md`.
3. Each requested `specialists/<slug>/PROFILE.md` exists.
4. The active problem directory exists with `problem.md`, `session_state.md`, `claim_ledger.md`, and the current phase artifact.

[PROCEDURE]
1. Read `IDENTITY.md`, `goal.md`, `specialists/_meta/etiquette.md`, requested specialist profiles, active problem summary, ledger tail, open gaps, and `survey.md` when present.
2. Apply `Panel Mode` from `specialists/_meta/etiquette.md`: at most three turns per specialist unless the Director extends the panel.
3. Require each turn to make one mathematical move: definition, example, lemma, obstruction, or question.
4. Require disagreements to point to a statement, quantifier, model, citation, or obstruction.
5. Separate proved statements, cited facts, heuristics, analogies, and conjectural suggestions.
6. End with a ranked list of next testable moves and at least one falsifiability hook or obstruction candidate.
7. Write the panel artifact to `problems/<slug>/dialogue/panel-<unit-id>.md`.
8. Do not add claims to `claim_ledger.md` unless a later Director checkpoint promotes a precise, supported claim.
9. Invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. `problems/<slug>/dialogue/panel-<unit-id>.md`.

[FAILURE]
1. Missing active problem: print `BLOCKED: no active problem for panel.` and stop.
2. Fewer than two registered specialists supplied: print `BLOCKED: panel requires at least two registered specialists.` and stop.
3. Missing concrete disagreement or question: print `BLOCKED: panel requires a concrete disagreement or attack question.` and stop.
