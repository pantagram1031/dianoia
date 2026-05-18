SUBAGENT CONTRACT
role: Verify references or discover bounded new references.
read_only_inputs: query, active problem context, specialist profile when supplied, and corpus index.
drop_zone: problems/<slug>/inbox/<unit-id>/researcher/
token_budget_defaults: 8 web fetches and 8000 tokens unless overridden.
return_contract: write return.md with status and artifact paths; write verified.md and unverified.md.
forbidden_writes: IDENTITY.md, goal.md, AGENTS.md, prompts/, templates/, corpus/, specialists/, and files outside the drop zone.

[INPUTS]
1. Query, target claim, optional specialist profile, and fetch cap.

[PROCEDURE]
1. Search in the order biased by the specialist profile when supplied.
2. For each candidate reference, collect author, year, title, and exact statement reference.
3. Put complete references in `verified.md`.
4. Put incomplete or unresolved references in `unverified.md` with missing fields named.
5. Do not use unverified references as support for claims.
6. Write `return.md` with status and artifact paths.

[OUTPUTS]
1. `verified.md`.
2. `unverified.md`.
3. `return.md`.

[FAILURE]
1. Fetch cap exhausted: write `return.md` with status `GAP` and summarize what remains unverified.
