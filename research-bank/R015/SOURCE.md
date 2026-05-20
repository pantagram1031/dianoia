# Research Candidate Source

id: R015
area: geometry
target_type: proof | counterexample | bound improvement
status: OPEN-VERIFIED

## Target Statement

Resolve the Erdos-Szekeres happy ending conjecture: determine whether
`g(n) = 2^(n-2) + 1` points always force `n` points in convex position for all
`n >= 3`.

## Primary Source

- Authors: Adrian Dumitrescu, Jozsef Solymosi, and collaborators in current
  Erdos-Szekeres literature
- Year: 2026
- Title: The Erdos-Szekeres conjecture revisited
- Exact statement reference: Journal of Combinatorial Theory, Series A 222
  (2026), abstract
- URL or local artifact: https://www.sciencedirect.com/science/article/pii/S0097316526000385
- Relationship to target: 2026 open-access paper calls the 1935 conjecture
  famous and still open, proving relaxed split-polygon results instead.

## Background Sources

1. Authors: Eric W. Weisstein
   Year: 2026
   Title: Happy End Problem
   Exact statement reference: MathWorld entry, updated 2026-05-10
   URL or local artifact: https://mathworld.wolfram.com/HappyEndProblem.html
   Relationship to target: current reference source says the general problem
   remains open and `g(n)` for `n >= 7` is unknown.

2. Authors: Wikipedia contributors
   Year: 2026
   Title: Happy ending problem
   Exact statement reference: current article, status statement
   URL or local artifact: https://en.wikipedia.org/wiki/Happy_ending_problem
   Relationship to target: independent status source for definitions and known
   small values.

3. Authors: SAT/ASP geometry authors
   Year: 2026
   Title: Combinatorial Geometry of Erdos-Szekeres Type Problems: SAT/ASP
   Modeling and Linear Subreduction
   Exact statement reference: arXiv:2604.20120 abstract
   URL or local artifact: https://arxiv.org/abs/2604.20120
   Relationship to target: very recent computational geometry paper on
   Erdos-Szekeres-type problems and certificate workflows.

## Candidate Transformation

Target replayable computational geometry progress: reproduce small `g(n)`
certificates, verify SAT encodings for known cases, or improve a relaxed
variant such as split polygons or constrained point sets.
