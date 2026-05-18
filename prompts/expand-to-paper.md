Expand a WN proof file into paper prose while preserving every formal step.

[INPUTS]
1. Path to a `*.fml` file.
2. Its referenced `claim_ledger.md` and corpus citations.

[PROCEDURE]
1. Read the input `*.fml` file and compute a source hash.
2. Create a sibling markdown file with the same stem.
3. Preserve every tactic step and dependency from the WN source.
4. Expand tactics into paper prose with sections `Statement`, `Proof`, and `Remarks`.
5. Include a notation key for all nonlocal notation.
6. Format every citation with author, year, title, and exact statement reference.
7. Replace any unsupported step with `[GAP: <missing> | suffices: <what would close>]`.
8. Scan for forbidden vocabulary from `goal.md` and rewrite or block on any occurrence.
9. Append a source-hash footer linking the prose file to the `*.fml` source.

[OUTPUTS]
1. Sibling `*.md` paper-prose file.

[FAILURE]
1. Missing input file: print `BLOCKED: provide a readable *.fml file.` and stop.
