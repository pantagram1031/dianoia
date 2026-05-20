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
2. For arXiv papers or arXiv-id-like queries, invoke
   `connectors/arxiv/server.py` and write the compact metadata result into the
   drop zone before judging whether the reference is complete. Consult
   `skills/arxiv-fetch/SKILL.md` to separate metadata, fallback abstract-page
   evidence, and exact statement verification.
3. For OEIS sequence ids or sequence-like computational evidence, invoke
   `connectors/oeis/server.py` and write the compact metadata result into the
   drop zone. Treat OEIS as computational/reference evidence unless a separate
   proof source is verified.
4. For claims that may be formalized or already have a Lean artifact, invoke
   `connectors/lean/server.py env` and, when a `.lean` file exists, invoke
   `connectors/lean/server.py check <file>`. Record `UNVERIFIED` explicitly if
   Lean is unavailable or the check cannot be run.
5. Consult `skills/citation-discipline/SKILL.md`; for each candidate
   reference, collect author, year, title, exact statement reference, and the
   relationship between the cited statement and target claim.
6. If the target claim involves small primes with prescribed quadratic
   character behavior, consult `skills/pollack-character/SKILL.md` before
   deciding whether the reference supports finiteness, explicit bounds, or only
   an ineffective obstruction.
7. Put complete references in `verified.md`.
8. Put incomplete or unresolved references in `unverified.md` with missing fields named.
9. Do not use unverified references as support for claims.
10. Write `return.md` with status and artifact paths.

[OUTPUTS]
1. `verified.md`.
2. `unverified.md`.
3. `return.md`.

[FAILURE]
1. Fetch cap exhausted: write `return.md` with status `GAP` and summarize what remains unverified.
