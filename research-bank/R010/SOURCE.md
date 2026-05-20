# Research Candidate Source

id: R010
area: probability
target_type: proof | counterexample | bound improvement
status: OPEN-VERIFIED

## Target Statement

Resolve the Komlos conjecture in discrepancy theory: for any collection of
vectors in the Euclidean unit ball, assign signs so that the infinity norm of
the signed sum is bounded by an absolute constant independent of dimension and
the number of vectors.

## Primary Source

- Authors: Nikhil Bansal
- Year: 2026
- Title: On the Komlos Conjecture
- Exact statement reference: Simons Institute abstract, 2026-05-28 talk
- URL or local artifact: https://simons.berkeley.edu/talks/nikhil-bansal-university-michigan-2026-05-28
- Relationship to target: current expert talk states the conjecture and reports
  an improved `O((log n)^(1/4))` bound, not a constant bound.

## Background Sources

1. Authors: Emergent Mind
   Year: 2026
   Title: Komlos conjecture (constant l-infinity discrepancy for unit-norm columns)
   Exact statement reference: open-problems page
   URL or local artifact: https://www.emergentmind.com/open-problems/komlos-conjecture-constant-linfty-discrepancy
   Relationship to target: current open-problem-bank source classifies Komlos
   as a central open discrepancy problem.

2. Authors: Dmitry Gribanov, Tagir Khayaleyev, Mikhail Cherniavskii,
   Maxim Klimenko, Dmitry Malyshev, Stanislav Moiseev
   Year: 2026
   Title: Algorithms for Standard-form ILP Problems via Komlos' Discrepancy Setting
   Exact statement reference: arXiv:2604.09806 abstract
   URL or local artifact: https://arxiv.org/abs/2604.09806
   Relationship to target: recent algorithmic paper states consequences that
   would follow under the Komlos conjecture, indicating it is still an
   assumption rather than a theorem.

3. Authors: Nikhil Bansal, Haotian Jiang, Raghu Meka, Sahil Singla, Makrand Sinha
   Year: 2022
   Title: Smoothed Analysis of the Komlos Conjecture
   Exact statement reference: arXiv:2204.11427 abstract
   URL or local artifact: https://arxiv.org/abs/2204.11427
   Relationship to target: proves a smoothed-analysis setting, useful for
   separating partial probabilistic progress from the full worst-case claim.

## Candidate Transformation

Aim for a bounded improvement or reproducible obstruction: formalize the gap
between the current polylogarithmic bound and the constant conjecture on a
restricted matrix class, or find explicit hard instances for proposed
strengthenings.
