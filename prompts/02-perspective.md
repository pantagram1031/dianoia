Select three specialist lenses and extract day-one sub-questions for the active problem.

[INPUTS]
1. Active slug from `problems/.active`.
2. `problems/<slug>/survey.md`.
3. `specialists/INDEX.md`.

[PROCEDURE]
1. Read `specialists/INDEX.md` and all listed specialist profiles needed for scoring.
2. Score each specialist against the active problem by MSC overlap, recent activity, and blind-spot relevance.
3. Select exactly three specialists.
4. If a slot cannot be filled from existing profiles, invoke `prompts/subagents/specialist-factory.md`.
5. For each selected specialist, write the perspective framing and one day-one sub-question.
6. Record why the three selected views are jointly useful and where their blind spots differ.
7. Write the output without adding claims to the ledger unless a formal mathematical claim is introduced.
8. Invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. `problems/<slug>/perspectives.md`.

[FAILURE]
1. Missing survey: print `BLOCKED: run 01-survey before 02-perspective.` and stop.

[REGISTRY GATE]
- The specialists chosen MUST appear in specialists/INDEX.md.
  Inventing a specialist name not in the index is a fatal defect.
- If a needed lens is absent from the registry, invoke
  prompts/subagents/specialist-factory.md to add it (with PROFILE.md
  and INDEX.md registration) BEFORE writing perspectives.md.
- perspectives.md MUST cite each selected specialist's slug exactly
  as it appears in specialists/INDEX.md.
