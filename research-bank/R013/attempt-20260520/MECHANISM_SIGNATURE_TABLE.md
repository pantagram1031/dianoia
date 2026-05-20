# Mechanism Signature Table

Status: PARTIAL-PROGRESS, not a claim.

## Scope

This table combines the two mechanism-batch artifacts currently most relevant
to the width-3, height-4, rank-layer-shape `2,2,2,1` proof search:

- Dangerous/boundary classes: `normal-form-cases/u6-p1-p8-mechanism-batch-depth5.json`
- Probability-weakest unprocessed classes:
  `normal-form-cases/vector-near-unprocessed/mechanism-batch-depth5.json`

Together these cover 37 rank-normal forms: 22 from U6/P1-P8 and 15 from U1-U5.
All 37 resolve by recurrence depth at most 5.

## Aggregate Counts

| Family | Forms |
|--------|-------|
| `forced-block` | 27 |
| `balanced-core-plus-forced-first` | 5 |
| `balanced-core-with-forced-blocks` | 5 |
| unresolved | 0 |

## U6/P1-P8 Dangerous Forms

| Form | Depth | Mechanism | Lower probability |
|------|-------|-----------|-------------------|
| `p1-form-1` | 1 | `balanced-core-plus-forced-first` | `14/39` |
| `p1-form-2` | 3 | `forced-block` | `15/33` |
| `p1-form-3` | 1 | `forced-block` | `14/33` |
| `p2-form-1` | 3 | `forced-block` | `19/44` |
| `p2-form-2` | 3 | `forced-block` | `25/51` |
| `p2-form-3` | 3 | `forced-block` | `22/44` |
| `p2-form-4` | 3 | `forced-block` | `18/37` |
| `p2-form-5` | 1 | `forced-block` | `14/35` |
| `p2-form-6` | 3 | `balanced-core-with-forced-blocks` | `15/36` |
| `p3-form-1` | 5 | `forced-block` | `15/31` |
| `p3-form-2` | 5 | `balanced-core-with-forced-blocks` | `23/47` |
| `p3-form-3` | 3 | `forced-block` | `14/35` |
| `p3-form-4` | 3 | `forced-block` | `16/33` |
| `p4-form-1` | 3 | `forced-block` | `12/30` |
| `p5-form-1` | 4 | `forced-block` | `14/35` |
| `p6-form-1` | 3 | `balanced-core-plus-forced-first` | `12/30` |
| `p7-form-1` | 3 | `forced-block` | `19/41` |
| `p7-form-2` | 3 | `forced-block` | `13/32` |
| `p8-form-1` | 3 | `balanced-core-plus-forced-first` | `13/32` |
| `p8-form-2` | 3 | `balanced-core-with-forced-blocks` | `15/33` |
| `u6-form-1` | 5 | `forced-block` | `30/70` |
| `u6-form-2` | 5 | `balanced-core-with-forced-blocks` | `31/63` |

## U1-U5 Weakest Unprocessed Forms

| Form | Depth | Mechanism | Lower probability |
|------|-------|-----------|-------------------|
| `u1-form-1` | 5 | `forced-block` | `31/63` |
| `u1-form-2` | 3 | `forced-block` | `21/45` |
| `u1-form-3` | 3 | `balanced-core-plus-forced-first` | `21/51` |
| `u2-form-1` | 5 | `forced-block` | `26/57` |
| `u2-form-2` | 3 | `forced-block` | `33/69` |
| `u2-form-3` | 3 | `forced-block` | `18/40` |
| `u2-form-4` | 3 | `forced-block` | `24/50` |
| `u2-form-5` | 5 | `forced-block` | `22/48` |
| `u2-form-6` | 3 | `balanced-core-plus-forced-first` | `22/53` |
| `u3-form-1` | 5 | `forced-block` | `24/51` |
| `u3-form-2` | 3 | `forced-block` | `15/36` |
| `u3-form-3` | 5 | `forced-block` | `21/45` |
| `u4-form-1` | 3 | `forced-block` | `8/19` |
| `u5-form-1` | 3 | `forced-block` | `12/27` |
| `u5-form-2` | 5 | `balanced-core-with-forced-blocks` | `14/33` |

## Algorithmic Lesson

This table is the anti-overfitting object for the current R013 line.

The evidence does not say "memorize P7/P8" or "fit U6." It says that several
apparently different vector classes collapse into three reusable recurrence
mechanisms. Dianoia's next useful behavior is therefore:

1. identify the local structural trigger for each mechanism;
2. prove the trigger once;
3. route future finite-poset cases to the matching trigger, not to the
   historical class label.

This is exactly the generalized-but-specialized direction: specialized
mechanisms, chosen by structural features, reused across unfamiliar cases.

## Remaining Gap

The table covers 37 forms, not all unprocessed vector classes. It supports a
candidate lemma, but it does not yet prove the restricted rank-2221 subcase and
does not justify a `CLAIMS.md` row.

