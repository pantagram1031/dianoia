# R013 Vector Coverage Check Notes

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note records an independent bookkeeping check for the width-3, height-4,
rank-layer-shape `2,2,2,1` finite-poset subproblem. It verifies that the vector
feature partition, vector frontier, all-vector normal-form ledger, and
depth-5 mechanism batch are talking about the same restricted universe.

Generated evidence:

```text
width3-rank2221-vector-coverage-check.json
```

Command:

```text
python tools/poset_balance.py matrix-vector-coverage-check \
  research-bank/R013/attempt-20260520/width3-rank2221-all-matrix-feature-partition-vector.json \
  research-bank/R013/attempt-20260520/width3-rank2221-vector-frontier.json \
  research-bank/R013/attempt-20260520/width3-rank2221-all-vector-form-ledger.json \
  --mechanism-batch research-bank/R013/attempt-20260520/normal-form-cases/vector-all/mechanism-batch-depth5.json \
  --output research-bank/R013/attempt-20260520/width3-rank2221-vector-coverage-check.json
```

## Result

The check returned `ok: true` and no errors.

| Quantity | Value |
|----------|-------|
| vector partition groups | 59 |
| frontier classes | 59 |
| ledger classes | 59 |
| vector partition buckets | 67 |
| partition profiles | 103 |
| ledger normal forms | 103 |
| mechanism cases | 103 |
| mechanism found cases | 103 |
| mechanism unresolved cases | 0 |

Mechanism counts agree with `ALL_VECTOR_MECHANISM_REDUCTION.md`:

| Mechanism | Count |
|-----------|-------|
| `forced-block` | 55 |
| `balanced-core-plus-forced-first` | 31 |
| `balanced-core-plus-forced-second` | 1 |
| `balanced-core-with-forced-blocks` | 16 |

## Checks Performed

For each frontier class, the checker verifies:

1. its feature key appears in the vector partition;
2. its class id appears in the normal-form ledger;
3. the partition `profile_count`, frontier `profile_count`, and ledger
   `form_count` are equal;
4. the adjacent vector and skip vector agree between the frontier and ledger;
5. no partition feature key is left uncovered by the frontier;
6. no ledger class id is absent from the frontier;
7. total partition profiles equal total ledger normal forms;
8. the optional mechanism batch has one case per ledger form, no missing
   mechanism certificate, and no unresolved case.

## Interpretation

This is not a mathematical proof of the restricted subcase by itself. It is a
machine-checkable guardrail for the next proof step: the human theorem can now
refer to a single vector decomposition with 59 classes and 103 normal forms,
knowing that the generated coverage, form ledger, and mechanism certificates
are synchronized.

The immediate proof-facing task remains to turn the four mechanism labels into
local lemmas with hand-checkable hypotheses and terminal lower-count
inequalities. No `CLAIMS.md` row is justified by this note alone.
