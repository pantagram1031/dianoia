# Near-Unprocessed Slack Notes

Status: PARTIAL-PROGRESS, not a claim.

## Question

After reducing all U6/P1-P8 dangerous vector forms, the next risk was
over-specializing to the already-processed boundary cases. This note tests the
opposite side: the weakest still-unprocessed vector classes U1-U5.

The purpose is algorithmic as much as mathematical: decide whether dianoia
should keep enumerating case buckets, or whether the evidence now points to a
reusable mechanism lemma.

## Exact slack summary

Artifact:
`research-bank/R013/attempt-20260520/width3-rank2221-unprocessed-slack-summary.json`.

The summary covers 51 unprocessed vector classes and reports:

- `all_meet_threshold: true` for threshold `13/32`.
- `below_threshold_ids: []`.
- `componentwise_minimal_ids: ["U6"]`.
- The probability-weakest classes are U1-U5, not U6:
  - U1 has lower probability `7/17`, gap `3/544` above `13/32`.
  - U2 has lower probability `22/53`, gap `15/1696`.
  - U3 has lower probability `5/12`, gap `1/96`.
  - U4 has lower probability `8/19`, gap `9/608`.
  - U5 has lower probability `14/33`, gap `19/1056`.

This refutes the naive proof plan "prove U6, then use monotonicity." U6 is
componentwise-minimal in the adjacent/skip vector order, but it is not the
weakest probability class.

## Near-threshold normal forms

Artifacts:

- `width3-rank2221-near-unprocessed-form-ledger.json`
- `normal-form-cases/vector-near-unprocessed/summary.json`
- `normal-form-cases/vector-near-unprocessed/mechanism-batch-depth5.json`

The U1-U5 block contains 15 rank-normal forms:

- U1: 3 forms, minimum `7/17`.
- U2: 6 forms, minimum `22/53`.
- U3: 3 forms, minimum `5/12`.
- U4: 1 form, minimum `8/19`.
- U5: 2 forms, minimum `14/33`.

The depth-5 mechanism batch resolves all 15 forms:

- 12 forced-block forms.
- 2 balanced-core-plus-forced-first forms.
- 1 balanced-core-with-forced-blocks form.
- 0 unresolved forms.

The resolved weak forms are:

- U1-form-3: `7/17`, balanced-core-plus-forced-first, depth 3.
- U2-form-6: `22/53`, balanced-core-plus-forced-first, depth 3.
- U3-form-2: `5/12`, forced-block, depth 3.
- U4-form-1: `8/19`, forced-block, depth 3.
- U5-form-2: `14/33`, balanced-core-with-forced-blocks, depth 5.

## Interpretation

The important signal is not that another finite batch passed. The signal is
that the weakest unprocessed classes and the earlier dangerous classes reduce
to the same small family of recurrence mechanisms:

- forced-block;
- balanced-core-plus-forced-first;
- balanced-core-with-forced-blocks.

This argues against tuning dianoia to a fixed benchmark or a single extremal
class. The next useful mathematical object is a mechanism lemma:

> For width-3, height-4, rank-layer-shape `2,2,2,1` posets, certain local
> skip/adjacency configurations force a bounded-depth partition of linear
> extensions into forced orientation blocks, possibly with balanced residual
> cores. The resulting lower orientation probability is at least `13/32`.

This is still a candidate lemma. It is not yet a proof because the 51
unprocessed vector classes have not been reduced uniformly, and the current
evidence is generated enumeration plus recurrence certificates rather than a
human-readable universal argument.

## Next proof move

Do not keep adding isolated buckets as a substitute for mathematics.

Next target:

1. Build a mechanism signature table over all 59 vector classes, using the
   existing batch outputs where available and expanding only enough of the
   remaining 46 unprocessed classes to test whether the three mechanism
   families cover them.
2. Extract the minimal local hypotheses for each mechanism family.
3. Try to prove those hypotheses imply the recurrence split without referring
   to class labels U1, U2, etc.

If that works, the contribution candidate becomes a restricted finite-poset
lemma for the width-3/rank-2221 subcase. If it does not, record the obstruction
as the next dianoia proof-search lesson.

