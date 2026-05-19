Generate falsifiable hypotheses from three selected perspectives and test them quickly.

[INPUTS]
1. Active slug from `problems/.active`.
2. `problems/<slug>/perspectives.md`.
3. `problems/<slug>/survey.md`.
4. `claim_ledger.md` tail.

[PRECONDITIONS]
1. Phase 2 perspective selection has completed.
2. `problems/<slug>/perspectives.md` exists and names exactly three selected specialist lenses.
3. `problems/<slug>/survey.md` exists for nearest-result and obstruction checks.

[PROCEDURE]
1. Read the three selected perspectives and their day-one sub-questions.
2. For each perspective, generate three to five hypotheses.
3. State each hypothesis with explicit quantifiers, definitions, and refutation conditions.
4. For each hypothesis, cite the nearest existing result or tag `[UNVERIFIED]` and keep it out of downstream reasoning.
5. Design a 10-minute sanity check for each hypothesis: computation, small-case probe, known-counterexample probe, or limit case.
6. For each hypothesis, invoke `prompts/subagents/sanity-checker.md` with the statement, refutation condition, minimal check, and evidence standard.
7. Merge sanity-checker returns into `hypotheses_live.md` and record the evidence.
8. If the three selected perspectives genuinely disagree about direct-attack viability, obstruction severity, or hypothesis ranking, invoke `prompts/panel.md` with the disagreeing specialist slugs and the concrete disputed statement.
9. If the direct-attack hypothesis is killed or a new angle is needed before choosing a fallback, invoke `prompts/subagents/muser.md` with the open blocker and specialist bias from the selected perspectives.
10. Mark killed hypotheses with the reason and surviving hypotheses with the exact survival evidence.
11. Append conjectural ledger rows only for survivors that are precise enough to track.
12. Invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. `problems/<slug>/hypotheses_live.md`.
2. Sanity-check log attached inside `hypotheses_live.md`.
3. Sanity-checker return artifacts under `problems/<slug>/inbox/<unit-id>/sanity-checker/`.
4. Panel dialogue artifacts when selected perspectives disagree.
5. Muser return artifacts when a direct-attack blocker or new-angle need occurs.

[FAILURE]
1. Missing perspectives: print `BLOCKED: run 02-perspective before 03-hypothesize.` and stop.

INVARIANTS (v4 attack discipline):
- At least one hypothesis must be a direct frontal attack on the primary target stated in intake.md Section A, with original quantifiers intact. Conditional, reformulated, or restricted versions do not qualify as direct attack.
- The direct-attack hypothesis receives a sanity check like every other hypothesis. If the sanity check kills it, work_journal.md gains an entry "RETREAT TRIGGER: <precise reason>" before any fallback hypothesis is selected.
- If hypotheses_live.md Survivors contain only conditional/reformulation/obstruction/conjecture entries AND work_journal.md has no RETREAT TRIGGER entry for this Phase 3, the artifact is a fatal defect.
- Survivors selected for Phase 4 must include the direct attack if it survived. If it died, Survivors must include a documented fallback chain stating, for each weaker hypothesis, why it is the strongest still-living attempt.
