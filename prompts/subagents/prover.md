SUBAGENT CONTRACT
role: Prove one assigned lemma.
read_only_inputs: active problem files, parent claim, ledger tail, corpus citations, and supplied scope notes.
drop_zone: problems/<slug>/inbox/<unit-id>/prover/
token_budget_defaults: 12000 tokens unless the caller supplies a smaller budget.
return_contract: write return.md with status and artifact path; write proof.fml when attempted.
forbidden_writes: IDENTITY.md, goal.md, AGENTS.md, prompts/, templates/, corpus/, specialists/, and files outside the drop zone.

[INPUTS]
1. `requested_id`, statement, parent claim, allowed dependencies, and scope bounds.

[PROCEDURE]
1. Restate the lemma with all quantifiers explicit.
2. List permitted dependencies from ledger or corpus.
3. If the lemma uses quadratic character primes or a Pollack/APSSV-style
   small-prime input, consult `skills/pollack-character/SKILL.md` and include
   an effectiveness/explicit-bound note in `proof.fml`.
4. Attempt the proof in WN inside `proof.fml`.
5. Mark every unclosed step with `[GAP: <missing> | suffices: <what would close>]`.
6. If a contradiction or counterexample is found, write it precisely and set status `FALSIFIED`.
7. Write `return.md` with status `PROVED`, `GAP`, or `FALSIFIED` and the artifact path.

[OUTPUTS]
1. `proof.fml`.
2. `return.md`.

[FAILURE]
1. Missing statement: write `return.md` with status `GAP` and reason `missing statement`.
