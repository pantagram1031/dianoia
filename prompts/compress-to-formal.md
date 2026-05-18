Compress a prose proof into WN without repairing gaps or changing the original.

[INPUTS]
1. Path to a prose proof in PDF or markdown.
2. Optional destination path for the `*.fml` output.

[PROCEDURE]
1. Read the source proof without editing it.
2. Extract statement, definitions, assumptions, claims, and proof steps.
3. Translate each step into WN tactics.
4. For every step, cite a ledger or corpus ID, or write `[GAP: <missing> | suffices: <what would close>]`.
5. Preserve the original quantifier order and hypotheses.
6. Record unresolved references as `[REFERENCE NEEDS VERIFICATION]`.
7. Write the output `*.fml` beside the source unless a destination is supplied.
8. Do not patch the original prose file.

[OUTPUTS]
1. A faithful WN `*.fml` translation.

[FAILURE]
1. Missing or unreadable input: print `BLOCKED: provide a readable prose proof.` and stop.
