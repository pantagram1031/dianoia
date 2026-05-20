# Research Candidate Source

id: R014
area: number theory
target_type: proof | counterexample | bound improvement
status: OPEN-VERIFIED

## Target Statement

Resolve Artin's primitive root conjecture: for any integer `a` that is neither
`-1` nor a square, there are infinitely many primes `p` for which `a` is a
primitive root modulo `p`, with the predicted Artin density where applicable.

## Primary Source

- Authors: Leo Goldmakher, Greg Martin, Paul Peringuey
- Year: 2025
- Title: Refinements of Artin's primitive root conjecture
- Exact statement reference: arXiv:2502.19601 abstract
- URL or local artifact: https://arxiv.org/abs/2502.19601
- Relationship to target: recent paper says Artin's original conjecture remains
  open, proves refinements under GRH, and gives weaker unconditional versions.

## Background Sources

1. Authors: Wikipedia contributors
   Year: 2026
   Title: Artin's conjecture on primitive roots
   Exact statement reference: current article lead and partial results
   URL or local artifact: https://en.wikipedia.org/wiki/Artin%27s_conjecture_on_primitive_roots
   Relationship to target: independent current source states the conjecture is
   unresolved as of 2026 and not proved for any single value of `a`.

2. Authors: Emergent Mind
   Year: 2026
   Title: Artin's primitive root conjecture
   Exact statement reference: open-problems page
   URL or local artifact: https://www.emergentmind.com/open-problems/artins-primitive-root-conjecture
   Relationship to target: current open-problem source records that Hooley's
   proof is conditional on GRH and no unconditional proof is known.

3. Authors: Gabriele Fici, Esteban Gabory, Giuseppe Romana, Marinella Sciortino
   Year: 2025
   Title: Unclustered BWTs of any Length over Non-Binary Alphabets
   Exact statement reference: arXiv:2508.20879 abstract
   URL or local artifact: https://arxiv.org/abs/2508.20879
   Relationship to target: recent adjacent combinatorics/CS paper notes a
   binary case related to Artin's conjecture remains open.

## Candidate Transformation

Do not attack the full conjecture first. Target exact Chebotarev-style
computation or conditional-to-finite reformulation work: reproduce predicted
density data for small `a`, formalize primitive-root tests, or find bounded
evidence against a proposed refinement.
