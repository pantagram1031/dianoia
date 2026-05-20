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
2. Consult `skills/sanity-small-cases/SKILL.md` to make the checked domain,
   edge cases, and kill condition explicit before running the probe.
3. Execute the smallest specified probe: computation, small case, known counterexample, or limit case.
4. If the hypothesis claims finite-list completeness, residue-class exhaustion,
   or no remaining candidates, consult `skills/coverage-systems/SKILL.md` and
   require a coverage certificate or explicit uncovered classes.
5. Record inputs, calculations, and evidence.
6. Decide `kills` or `survives`.
7. Write any gap explicitly when the probe was inconclusive.
8. Write `return.md` with status and artifact path.

[OUTPUTS]
1. `sanity.md`.
2. `return.md`.

[FAILURE]
1. Missing kill condition: write `return.md` with status `GAP` and reason `missing refutation condition`.
