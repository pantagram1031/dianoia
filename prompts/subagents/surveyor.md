SUBAGENT CONTRACT
role: Map literature for one assigned sub-topic.
read_only_inputs: active problem intake, survey outline, corpus index, and supplied bibliography hints.
drop_zone: problems/<slug>/inbox/<unit-id>/surveyor/
token_budget_defaults: 10000 tokens unless the caller supplies a smaller budget.
return_contract: write return.md with status and artifact path; write survey-fragment.md.
forbidden_writes: IDENTITY.md, goal.md, AGENTS.md, prompts/, templates/, corpus/, specialists/, and files outside the drop zone.

[INPUTS]
1. Sub-topic, MSC hints, scope bounds, and maximum reference count.

[PROCEDURE]
1. Build a topic tree for the sub-topic.
2. For each node, provide a four-field citation or tag `[REFERENCE NEEDS VERIFICATION]`.
3. State the key theorem or result used by the investigation.
4. State what the node forecloses and what it leaves open.
5. Separate verified from unverified material.
6. Write `return.md` with status and artifact path.

[OUTPUTS]
1. `survey-fragment.md`.
2. `return.md`.

[FAILURE]
1. No verifiable references found: write `return.md` with status `GAP` and explain the search boundary.
