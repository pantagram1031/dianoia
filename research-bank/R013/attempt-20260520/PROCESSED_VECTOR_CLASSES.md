# R013 Processed Vector Classes

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This table extracts the processed vector feature classes from:

```text
width3-rank2221-all-matrix-feature-partition-vector.json
```

Here "processed" means the class has minimum lower orientation probability at
most `13/32` in the rank-shape `2,2,2,1`, width-3, height-4 search artifact.
The table is intended as a proof-planning aid, not as a theorem statement.

## Table

| Id | Min lower prob. | Profiles | Adjacent vector | Skip vector | Cover matrix |
|----|------------------|----------|-----------------|-------------|--------------|
| P1 | `14/39` | 3 | `(2,2,1)` | `(2,0,1)` | `[[0,2,2,0],[0,0,2,1],[0,0,0,1],[0,0,0,0]]` |
| P2 | `2/5` | 6 | `(2,2,1)` | `(1,0,1)` | `[[0,2,1,0],[0,0,2,1],[0,0,0,1],[0,0,0,0]]` |
| P3 | `2/5` | 4 | `(2,3,1)` | `(1,0,0)` | `[[0,2,1,0],[0,0,3,0],[0,0,0,1],[0,0,0,0]]` |
| P4 | `2/5` | 1 | `(2,3,2)` | `(0,0,0)` | `[[0,2,0,0],[0,0,3,0],[0,0,0,2],[0,0,0,0]]` |
| P5 | `2/5` | 1 | `(2,3,1)` | `(2,0,1)` | `[[0,2,2,0],[0,0,3,1],[0,0,0,1],[0,0,0,0]]` |
| P6 | `2/5` | 1 | `(3,2,1)` | `(2,0,1)` | `[[0,3,2,0],[0,0,2,1],[0,0,0,1],[0,0,0,0]]` |
| P7 | `13/32` | 2 | `(2,3,1)` | `(1,0,1)` | `[[0,2,1,0],[0,0,3,1],[0,0,0,1],[0,0,0,0]]` |
| P8 | `13/32` | 2 | `(3,2,1)` | `(1,0,1)` | `[[0,3,1,0],[0,0,2,1],[0,0,0,1],[0,0,0,0]]` |

## First Pattern Read

All eight processed classes have small top adjacency: the final adjacent-vector
entry is either `1` or `2`, and the only `2` case has no skip vector. The
lowest class P1 has both bottom-to-middle skip multiplicity `2` and middle-to-
top skip multiplicity `1`, while still having only one top adjacent cover.

The two `13/32` boundary classes P7 and P8 share skip vector `(1,0,1)` and
adjacent total `6`; they differ by shifting one adjacent cover between the
bottom and middle layers. This suggests the boundary phenomenon may be stable
under a bottom/middle dual-ish transfer, but this is only a signal.

## Lemma Target

Try to prove a dichotomy:

```text
Either the vector class is one of P1-P8, where existing hand/count ledgers
certify the lower bound directly, or the vector class has enough adjacent
placement slack to force a balanced incomparable pair with lower probability
at least 13/32.
```

The next proof-support step is to identify a local probability move that turns
"extra adjacent placement slack" into a lower bound without enumerating all 51
remaining vector classes individually.

## Claim Discipline

No `CLAIMS.md` row. This is a compact extraction from a finite artifact and
does not prove the published open problem.
