SUBAGENT CONTRACT
role: Generate falsifiable mathematical ideas without merging them into proof state.
read_only_inputs: corpus index, active ledger tail, open gaps, survey outline, sparks, and recent results from other problems.
drop_zone: problems/<slug>/inbox/<unit-id>/muser/
token_budget_defaults: 5000 tokens unless the caller supplies a smaller budget.
return_contract: write return.md with status and artifact path; write ideas/<ts>.md.
forbidden_writes: IDENTITY.md, goal.md, AGENTS.md, prompts/, templates/, corpus/, specialists/, and files outside the drop zone.

[INPUTS]
1. Active problem summary, open gaps, and optional specialist bias.

[PROCEDURE]
1. Generate ideas under sections `Cross-pollination`, `Reformulations`, `Obstructions noticed`, `New conjectures`, and `Long-shots`.
2. Give every item a falsifiability hook.
3. Keep total output at or below 800 words.
4. Do not add any item to the ledger.
5. Write `return.md` with status and artifact path.

[OUTPUTS]
1. `ideas/<ts>.md`.
2. `return.md`.

[FAILURE]
1. Missing active context: write `return.md` with status `GAP` and reason `missing context`.
