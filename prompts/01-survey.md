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

INVARIANTS (v4 state of the art):
- The survey ends with a "State of the Art" section recording the strongest known results toward the primary target with full 4-field citations (author, year, title, exact statement reference). Minimum 1 entry, recommended 3 or more. Use web tools as needed.
- For each candidate proof route in the terrain map, name at least one known obstruction or barrier theorem against that route (e.g. supercriticality barrier, scaling obstruction, no-go theorem). A route with zero known barriers indicates either a trivial route or an inadequate survey.
- Each sub-result in the "Open Terrain Map" carries a tag [TEXTBOOK] (in any standard reference predating current year - 30) or [FRONTIER]. A proof plan composed entirely of [TEXTBOOK] sub-results is a fatal defect at Phase 1.
