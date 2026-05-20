# Research Candidate Source

id: R020
area: discrete geometry
target_type: proof | counterexample | bound improvement
status: OPEN-VERIFIED

## Target Statement

Resolve the no-three-in-line problem: determine the exact maximum `D(n)` of
points in the `n x n` grid with no three collinear, including whether the
trivial upper bound `D(n) <= 2n` is attained for arbitrarily large or all `n`.

## Primary Source

- Authors: Thomas Prellberg
- Year: 2026
- Title: Constraint Satisfaction Programming for the No-three-in-line Problem
- Exact statement reference: arXiv:2602.07751 abstract
- URL or local artifact: https://arxiv.org/abs/2602.07751
- Relationship to target: 2026 CSP paper extends the verified `D(n)=2n` range
  only to `n <= 60`, explicitly leaving the next exact case unknown.

## Background Sources

1. Authors: Wikipedia contributors
   Year: 2026
   Title: No-three-in-line problem
   Exact statement reference: current article, upper/lower bounds section
   URL or local artifact: https://en.wikipedia.org/wiki/No-three-in-line_problem
   Relationship to target: independent source saying the exact function
   `D(n)` is not known and recording current small-case progress.

2. Authors: Thomas Prellberg
   Year: 2026
   Title: No-three-in-line sets on the checkerboard grid
   Exact statement reference: arXiv:2605.09215 abstract
   URL or local artifact: https://arxiv.org/abs/2605.09215
   Relationship to target: May 2026 variant paper gives new finite/continuum
   certificates for a checkerboard-restricted version, showing current active
   frontier work.

3. Authors: Anubhab Ghosal
   Year: 2026
   Title: A note on the extensible no-three-in-line problem
   Exact statement reference: arXiv:2605.07000 abstract
   URL or local artifact: https://arxiv.org/abs/2605.07000
   Relationship to target: May 2026 related lower-bound improvement preserves
   a gap to the trivial upper bound.

## Candidate Transformation

Target replayable discrete-geometry progress: reproduce CSP certificates for
known `D(n)=2n` cases, search exact cases beyond the current frontier, or prove
a restricted-grid upper/lower bound with exact certificate files.
