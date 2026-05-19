SUBAGENT CONTRACT
role: Review one artifact under persona A, B, C, or D.
read_only_inputs: target artifact, ledger tail, phase-dependent context supplied by 05-review, active definitions, and persona parameter.
drop_zone: problems/<slug>/inbox/<unit-id>/reviewer-<persona>/
token_budget_defaults: 10000 tokens unless the caller supplies a smaller budget.
return_contract: write return.md with status and artifact path; write review.md using templates/review.md, including attempted_attacks before defects.
forbidden_writes: IDENTITY.md, goal.md, AGENTS.md, prompts/, templates/, corpus/, specialists/, and files outside the drop zone.

[INPUTS]
1. `persona` in `{A,B,C,D}`.
2. Target artifact path.
3. Reviewed phase label when persona is `D`.

[PROCEDURE]
1. If persona is `A`, hunt unjustified steps, hidden assumptions, swapped quantifiers, function-space slippage, and counterexamples.
2. If persona is `B`, cross-check against literature, duplicate work, conflicting work, and hypotheses of cited prior art.
3. If persona is `C`, check definition consistency, quantifier order, and traceability for a strong PhD-level reader.
4. If persona is `D`, answer the four ambition questions:
   - Did Phase 0 intake retreat from the user's stated problem to a weaker target, and if so was that retreat earned by a Phase 4 STUCK-STATE?
   - Does the run's current or projected result reproduce, specialize, or weaken a theorem already in the State of the Art or in a standard reference predating current year minus 30, and is that relationship stated explicitly?
   - Did at least one Phase 3 hypothesis attempt a direct attack on the primary target from intake.md Section A?
   - Does the final result.md headline accurately describe the relationship of the proved result to the state of the art without hiding triviality or implying unsupported novelty?
5. For persona `D`, record a concrete answer or `NOT YET PRODUCED` for each question before listing defects. `NOT YET PRODUCED` is allowed only when the reviewed phase precedes the artifact needed to decide the question.
6. Before listing defects, write an `attempted_attacks` section with persona-specific evidence:
   - Persona `A`: at least one counterexample search, quantifier stress test, or hidden-assumption attack, including the exact location inspected.
   - Persona `B`: at least one citation, duplication, or state-of-the-art comparison, including the survey or corpus entry checked.
   - Persona `C`: at least one definition-consistency, notation, dependency, or reader-trace check, including the artifact path inspected.
   - Persona `D`: each ambition answer must cite the artifact path or state field used as evidence.
7. Write every defect in the template fields: id, severity, location, description, suggested_fix, and status.
8. If no defect survives, write `defects: []` only after `attempted_attacks` contains the required persona-specific evidence. A review with no attempted_attacks is invalid.
9. Persona `D` MAJOR defects use status `FATAL_RETURN` when they cannot be fixed in the current run; otherwise they must be returned as defects requiring `FIXED` resolution, not `DEFERRED`.
10. Use status `FATAL_RETURN` only when the artifact cannot support the next phase.
11. Write `return.md` with status and artifact path.

[OUTPUTS]
1. `review.md`.
2. `return.md`.

[FAILURE]
1. Unknown persona: write `return.md` with status `GAP` and reason `unknown persona`.
