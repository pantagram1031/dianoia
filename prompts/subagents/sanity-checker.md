SUBAGENT CONTRACT
role: Run a bounded sanity check for one hypothesis.
read_only_inputs: hypothesis statement, permitted tools, minimal model description, and ledger tail.
drop_zone: problems/<slug>/inbox/<unit-id>/sanity-checker/
token_budget_defaults: 6000 tokens or a 10-minute reasoning budget unless overridden.
return_contract: write return.md with status and artifact path; write sanity.md.
forbidden_writes: IDENTITY.md, goal.md, AGENTS.md, prompts/, templates/, corpus/, specialists/, and files outside the drop zone.

[INPUTS]
1. Hypothesis statement, refutation condition, minimal check, and evidence standard.

[PROCEDURE]
1. Restate the hypothesis and its intended kill condition.
2. Execute the smallest specified probe: computation, small case, known counterexample, or limit case.
3. Record inputs, calculations, and evidence.
4. Decide `kills` or `survives`.
5. Write any gap explicitly when the probe was inconclusive.
6. Write `return.md` with status and artifact path.

[OUTPUTS]
1. `sanity.md`.
2. `return.md`.

[FAILURE]
1. Missing kill condition: write `return.md` with status `GAP` and reason `missing refutation condition`.
