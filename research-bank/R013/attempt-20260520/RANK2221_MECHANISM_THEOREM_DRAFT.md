# R013 Rank-2221 Mechanism Theorem Draft

date: 2026-05-21
status: DRAFT-NOT-CLAIM

## Target

Restricted theorem candidate:

```text
Let P be a finite poset of width 3, height 4, and rank-layer-shape 2,2,2,1.
Within the rank-normal-form decomposition used in the R013 artifacts, P has an
incomparable pair (x,y) whose smaller orientation class has size at least
13/32 of all linear extensions of P.
```

This is a restricted 1/3-2/3-style statement. It is not a proof of the full
conjecture and is not yet a verified restricted theorem.

## Decomposition Lemma Candidate

Input artifacts:

```text
width3-rank2221-all-matrix-feature-partition-vector.json
width3-rank2221-vector-frontier.json
width3-rank2221-all-vector-form-ledger.json
width3-rank2221-vector-coverage-check.json
```

Candidate lemma:

```text
Every width-3, height-4, rank-layer-shape 2,2,2,1 instance represented by the
current matrix enumeration falls into exactly one of 59 adjacent/skip vector
classes. Those 59 classes expand to 103 rank-normal forms, and the
normal-form ledger has one checked form for each partition profile.
```

Current evidence:

- vector partition groups: 59;
- frontier classes: 59;
- ledger classes: 59;
- partition buckets: 67;
- partition profiles: 103;
- ledger forms: 103;
- coverage-check errors: none.

Human proof obligation:

```text
Replace the JSON synchronization check with a written derivation that the
feature map is invariant under the intended rank-normal-form isomorphisms,
that every enumerated matrix profile maps to one listed vector class, and that
the form ledger contains exactly the profiles counted by the partition.
```

## Mechanism Lemma Candidates

Input artifact:

```text
normal-form-cases/vector-all/mechanism-batch-depth5.json
```

All 103 forms currently resolve by one of four labels:

| Mechanism | Count |
|-----------|-------|
| `forced-block` | 55 |
| `balanced-core-plus-forced-first` | 31 |
| `balanced-core-plus-forced-second` | 1 |
| `balanced-core-with-forced-blocks` | 16 |

The `balanced-core-plus-forced-first` and
`balanced-core-plus-forced-second` labels should be folded into one
orientation-symmetric lemma.

### Forced-Block Lemma

Candidate statement:

```text
Fix an incomparable pair (x,y). Expand the linear-extension recurrence by
initial choices to depth d <= 5. If every depth-d leaf has forced either x<y
or y<x, and the terminal residual counts sum to L_xy and L_yx, then the pair
split in the original poset is exactly (L_xy,L_yx). If min(L_xy,L_yx) >=
13/32*(L_xy+L_yx), the restricted theorem follows for that form.
```

Current generated role: 55 forms.

Proof obligations:

1. give the recurrence partition proof independent of the code;
2. tabulate the terminal residual counts for the 55 forms in a compact,
   checkable appendix;
3. prove each listed terminal residual count, preferably by rank-local
   counting rather than by trusting a trace file.

### Balanced-Core Plus Forced-Side Lemma

Candidate statement:

```text
Fix an incomparable pair (x,y). At depth d <= 5, suppose each leaf is either
forced to one orientation or has a residual core with an exact 1:1 split for
(x,y). Then the original split is the sum of the forced leaves plus equal
balanced-core contributions. If the smaller total is at least 13/32 of the
root total, the form is certified.
```

Current generated role: 32 forms after folding first/second orientation:
31 first-side cases and 1 second-side case.

Proof obligations:

1. state the balanced-core symmetry condition as an isomorphism or involution
   on residual linear extensions;
2. show that the side label is orientation-only, not a new structural case;
3. tabulate the forced-side leaves and balanced-core leaves for all 32 forms.

### Balanced-Core With Forced-Blocks Lemma

Candidate statement:

```text
Fix an incomparable pair (x,y). At depth d <= 5, suppose the recurrence leaves
split into forced orientation blocks and balanced residual cores. Sum all
forced-block counts and add half of each balanced-core count to both
orientations. If the smaller resulting total is at least 13/32 of the root
total, the form is certified.
```

Current generated role: 16 forms.

Proof obligations:

1. prove that every unseen residual marked balanced has a genuine orientation
   reversing bijection;
2. prove that every forced residual contributes wholly to the marked
   orientation;
3. tabulate the final lower-count inequalities for the 16 forms.

## Proof Assembly Skeleton

1. Apply the decomposition lemma to reduce the restricted rank-2221 universe to
   103 normal forms.
2. For each normal form, choose the incomparable pair and recurrence depth
   recorded in `mechanism-batch-depth5.json`.
3. Route the form to one of the three folded mechanism lemmas:
   forced-block, balanced-core plus forced-side, or balanced-core with
   forced-blocks.
4. Verify the terminal count table for that lemma family.
5. Conclude that each normal form has a pair whose smaller orientation class is
   at least `13/32` of the linear extensions.
6. Use the rank-normal-form equivalence to transfer the certified pair split
   back to every poset represented by the form.

## Current Gap

The generated artifacts give a strong route map, but this draft is still below
the bar for a mathematical contribution. The missing step is a compact
hand-checkable table of local hypotheses and terminal inequalities for all 103
forms, plus a written invariant proof for the vector decomposition.

No `CLAIMS.md` entry should be added until those two pieces are complete.
