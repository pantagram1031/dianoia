# R013 Matrix Bucket Notes

date: 2026-05-20
status: OBSERVATION-NOT-CLAIM

## Scope

This note isolates the three profiles in the matrix-signature bucket containing
the `14/39` extremal from
`width3-rank2221-matrix-shape-classes-n7.json`.

Common signature:

```text
layers=2,2,2,1
covers=8
mins=2
maxs=2
cover_matrix=[[0,2,2,0],[0,0,2,1],[0,0,0,1],[0,0,0,0]]
```

The matrix bucket contains three unlabeled profiles. This is still finite-data
evidence, not a theorem, but it is small enough to be a plausible manual proof
subcase.

## Three Cases

### Case A

- linear extensions: 39
- best lower orientation probability: `14/39`
- best pair: `[0,1]`
- cover relations:

```text
0<3, 0<4, 1<3, 1<4, 2<5, 3<5, 6<0, 6<2
```

Layer vertex signatures:

```text
L0: [0,3,3,[0,0,0,0],[0,0,2,0]],
    [0,5,1,[0,0,0,0],[0,2,0,0]]
L1: [1,1,4,[1,0,0,0],[0,0,0,1]],
    [1,3,2,[1,0,0,0],[0,0,2,0]]
L2: [3,0,3,[1,1,0,0],[0,0,0,0]],
    [3,1,2,[1,1,0,0],[0,0,0,1]]
L3: [5,0,1,[0,1,1,0],[0,0,0,0]]
```

### Case B

- linear extensions: 33
- best lower orientation probability: `14/33`
- best pair: `[3,5]`
- cover relations:

```text
0<4, 1<4, 3<6, 5<0, 5<1, 5<2, 6<0, 6<2
```

The main visible difference from Case A is in the bottom layer: both bottom
vertices have upper-comparable count 4, while Case A has upper-comparable
counts 3 and 5.

### Case C

- linear extensions: 33
- best lower orientation probability: `5/11`
- best pair: `[0,5]`
- cover relations:

```text
0<6, 3<0, 3<5, 4<1, 4<6, 5<1, 5<2, 6<2
```

The main visible difference from Case A is in rank layer 1: both layer-1
vertices have upper-comparable count 2, while Case A has upper-comparable
counts 1 and 3.

## Proof-Split Target

For this matrix bucket, the finite evidence suggests the following sublemma:

> Every seven-element width-3, height-4 poset with rank-layer shape `2,2,2,1`
> and the common cover matrix above has a balanced pair with lower orientation
> probability at least `14/39`, with equality only in Case A.

The next proof move is to replace the computational labels with a small
coordinate-free argument: choose the two bottom vertices, the two rank-1
vertices, the two rank-2 vertices, and the top vertex; then split by the
bottom-layer and rank-1 layer vertex-signature patterns above.

## Claim Discipline

No `CLAIMS.md` row. This note is a proof-work artifact for a finite subcase,
not a new mathematical contribution or a publishable bound.
