Build a literature terrain map rooted at the active problem.

[INPUTS]
1. Active slug from `problems/.active`.
2. `problems/<slug>/intake.md`.
3. Existing `claim_ledger.md` and `corpus/INDEX.md`.

[PROCEDURE]
1. Read the intake classification, success criteria, and corpus seed rows.
2. Create a literature tree rooted at the active problem.
3. For each node, record a four-field citation: author, year, title, and exact statement reference.
4. For each node, state the key theorem or result in precise mathematical language.
5. For each node, state what the result forecloses for this investigation.
6. For each node, state what remains open.
7. Tag unresolved references `[REFERENCE NEEDS VERIFICATION]` and do not use them downstream.
8. Append verified literature claims as `CITED` ledger rows.
9. Conclude with a one-page open terrain map.
10. Invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. `problems/<slug>/survey.md`.
2. New `CITED` rows in `claim_ledger.md` when references are verified.

[FAILURE]
1. Missing intake: print `BLOCKED: run 00-intake before 01-survey.` and stop.
