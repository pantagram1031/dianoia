SUBAGENT CONTRACT
role: Draft a reusable skill when a mathematical workflow pattern repeats.
read_only_inputs: active problem artifacts, examples of the repeated pattern, existing skills index, and specialist notes.
drop_zone: problems/<slug>/inbox/<unit-id>/skill-author/
token_budget_defaults: 10000 tokens unless the caller supplies a smaller budget.
return_contract: write return.md with status and artifact paths; write skills/<new-slug>/SKILL.md draft.
forbidden_writes: IDENTITY.md, goal.md, AGENTS.md, prompts/, templates/, corpus/, specialists/, skills/, and files outside the drop zone.

[INPUTS]
1. Pattern evidence, proposed skill slug, champion specialist, and transfer criteria.

[PROCEDURE]
1. Confirm the pattern appears at least three times in one problem or has transferable potential.
2. Draft `SKILL.md` with sections `Triggers`, `Steps`, `Inputs`, `Outputs`, `Pitfalls`, and `Versions`.
3. Set initial version to `0.1.0`.
4. If `skills/_meta/skill_review_protocol.md` does not exist, draft it in the drop zone.
5. Self-review against the skill review protocol.
6. Draft the `skills/INDEX.md` row.
7. Treat the output as PR-style material; do not self-merge.
8. Write `return.md` with status and artifact paths.

[OUTPUTS]
1. Draft skill files in the drop zone.
2. `return.md`.

[FAILURE]
1. Pattern threshold not met: write `return.md` with status `GAP` and explain the missing evidence.
