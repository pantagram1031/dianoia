SUBAGENT CONTRACT
role: Draft a new specialist profile for an unfilled mathematical perspective.
read_only_inputs: active problem, specialists index, corpus index, and missed-opportunity notes.
drop_zone: problems/<slug>/inbox/<unit-id>/specialist-factory/
token_budget_defaults: 10000 tokens unless the caller supplies a smaller budget.
return_contract: write return.md with status and artifact paths; write PROFILE.md draft and supporting files.
forbidden_writes: IDENTITY.md, goal.md, AGENTS.md, prompts/, templates/, corpus/, specialists/, and files outside the drop zone.

[INPUTS]
1. Missing perspective, MSC need, and reason existing profiles are insufficient.

[PROCEDURE]
1. Draft `PROFILE.md` using the schema in `specialists/<slug>/PROFILE.md`.
2. Invoke or request researcher work to seed up to five verified references in `known_papers.md`.
3. Initialize empty `corpus_pin.md`, `skills_pin.md`, `log.md`, and `sparks/`.
4. Draft the registration row for `specialists/INDEX.md`.
5. Treat the output as PR-style material; do not self-merge.
6. Write `return.md` with status and artifact paths.

[OUTPUTS]
1. Draft specialist directory in the drop zone.
2. `return.md`.

[FAILURE]
1. Missing perspective: write `return.md` with status `GAP` and reason `missing perspective`.
