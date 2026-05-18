SUBAGENT CONTRACT
role: Review one artifact under persona A, B, or C.
read_only_inputs: target artifact, ledger tail, survey, active definitions, and persona parameter.
drop_zone: problems/<slug>/inbox/<unit-id>/reviewer-<persona>/
token_budget_defaults: 10000 tokens unless the caller supplies a smaller budget.
return_contract: write return.md with status and artifact path; write review.md using templates/review.md.
forbidden_writes: IDENTITY.md, goal.md, AGENTS.md, prompts/, templates/, corpus/, specialists/, and files outside the drop zone.

[INPUTS]
1. `persona` in `{A,B,C}`.
2. Target artifact path.

[PROCEDURE]
1. If persona is `A`, hunt unjustified steps, hidden assumptions, swapped quantifiers, function-space slippage, and counterexamples.
2. If persona is `B`, cross-check against literature, duplicate work, conflicting work, and hypotheses of cited prior art.
3. If persona is `C`, check definition consistency, quantifier order, and traceability for a strong PhD-level reader.
4. Write every defect in the template fields: id, severity, location, description, suggested_fix, and status.
5. Use status `FATAL_RETURN` only when the artifact cannot support the next phase.
6. Write `return.md` with status and artifact path.

[OUTPUTS]
1. `review.md`.
2. `return.md`.

[FAILURE]
1. Unknown persona: write `return.md` with status `GAP` and reason `unknown persona`.
