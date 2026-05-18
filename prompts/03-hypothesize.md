Generate falsifiable hypotheses from three selected perspectives and test them quickly.

[INPUTS]
1. Active slug from `problems/.active`.
2. `problems/<slug>/perspectives.md`.
3. `problems/<slug>/survey.md`.
4. `claim_ledger.md` tail.

[PROCEDURE]
1. Read the three selected perspectives and their day-one sub-questions.
2. For each perspective, generate three to five hypotheses.
3. State each hypothesis with explicit quantifiers, definitions, and refutation conditions.
4. For each hypothesis, cite the nearest existing result or tag `[UNVERIFIED]` and keep it out of downstream reasoning.
5. Design a 10-minute sanity check for each hypothesis: computation, small-case probe, known-counterexample probe, or limit case.
6. Execute the sanity checks as reasoning tasks and record evidence.
7. Mark killed hypotheses with the reason and surviving hypotheses with the exact survival evidence.
8. Append conjectural ledger rows only for survivors that are precise enough to track.
9. Invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. `problems/<slug>/hypotheses_live.md`.
2. Sanity-check log attached inside `hypotheses_live.md`.

[FAILURE]
1. Missing perspectives: print `BLOCKED: run 02-perspective before 03-hypothesize.` and stop.
