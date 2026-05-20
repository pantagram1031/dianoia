# Research Candidate Source

id: R013
area: order theory
target_type: proof | counterexample | bound improvement
status: OPEN-VERIFIED

## Target Statement

Resolve the 1/3-2/3 conjecture for finite posets: every finite partially
ordered set that is not a chain has two elements `x,y` such that the probability
that `x` precedes `y` in a uniformly random linear extension lies between
`1/3` and `2/3`.

## Primary Source

- Authors: Jeff Kahn and Max Aires
- Year: 2026
- Title: Balancing extensions in posets of large width
- Exact statement reference: Harvard-MIT Combinatorics seminar abstract,
  2026-05-11
- URL or local artifact: https://www.math.harvard.edu/event/balancing-extensions-in-posets-of-large-width/
- Relationship to target: current expert seminar says researchers are still
  far from proving the 1/3-2/3 conjecture and related width conjecture.

## Background Sources

1. Authors: Emily J. Olson and Bruce E. Sagan
   Year: 2018
   Title: On the 1/3-2/3 Conjecture
   Exact statement reference: arXiv:1706.04985 abstract
   URL or local artifact: https://arxiv.org/abs/1706.04985
   Relationship to target: states the conjecture and proves only certain
   families of posets.

2. Authors: Graham Brightwell and Colin Wright
   Year: 1992
   Title: The 1/3-2/3 Conjecture for 5-Thin Posets
   Exact statement reference: SIAM Journal on Discrete Mathematics abstract
   URL or local artifact: https://epubs.siam.org/doi/10.1137/0405037
   Relationship to target: classic computer-assisted special-case proof,
   useful for exact replay and subcase benchmarking.

3. Authors: Wikipedia contributors
   Year: 2026
   Title: 1/3-2/3 conjecture
   Exact statement reference: current article, related conjectures and known
   gaps
   URL or local artifact: https://en.wikipedia.org/wiki/1/3%E2%80%932/3_conjecture
   Relationship to target: independent status and terminology source for
   balanced pairs, width, and related gold-partition variants.

## Candidate Transformation

Target exact finite progress first: reproduce known small-width searches,
improve a finite-width or cover-graph class, or find counterexamples to
stronger gap/gold-partition variants without conflating them with the base
conjecture.
