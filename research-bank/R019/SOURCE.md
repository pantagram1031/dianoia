# Research Candidate Source

id: R019
area: design theory
target_type: proof | counterexample | bound improvement
status: OPEN-VERIFIED

## Target Statement

Resolve the Ryser-Brualdi-Stein Latin square transversal conjecture: every
Latin square of order `n` has a partial transversal of size at least `n-1`, and
if `n` is odd it has a full transversal.

## Primary Source

- Authors: Richard Montgomery
- Year: 2026
- Title: Transversals in Latin Squares
- Exact statement reference: survey, Conjecture 3.2 and Section 5 discussion
- URL or local artifact: https://rhmontgomery.warwick.ac.uk/papers/37transversalssurvey.pdf
- Relationship to target: current survey states the combined conjecture and
  explains that large-even progress does not supply the odd full-transversal
  case.

## Background Sources

1. Authors: Richard Montgomery
   Year: 2023
   Title: A proof of the Ryser-Brualdi-Stein conjecture for large even n
   Exact statement reference: arXiv:2310.19779 abstract
   URL or local artifact: https://arxiv.org/abs/2310.19779
   Relationship to target: proves the `n-1` part for sufficiently large `n`,
   but does not settle the full odd-order transversal claim.

2. Authors: Emergent Mind open-problem index
   Year: 2026
   Title: Ryser-Brualdi-Stein conjecture on Latin square transversals
   Exact statement reference: open problem page
   URL or local artifact: https://www.emergentmind.com/open-problems/ryser-brualdi-stein-latin-square-transversals
   Relationship to target: current open-problem page says odd full
   transversals remain open in general.

3. Authors: Douglas B. West
   Year: 2026
   Title: Kedzy-Snevily, Ryser, and Brualdi Conjectures
   Exact statement reference: open-problems page
   URL or local artifact: https://dwest.web.illinois.edu/regs/permcov.html
   Relationship to target: independent formulation of Ryser and Brualdi
   conjectures through permutation-covering language.

## Candidate Transformation

Target exact design-theory progress: verify small Latin-square/rainbow-matching
instances, improve a restricted odd-order class, or formalize a translation
between Latin transversals and tripartite hypergraph matchings for a bounded
family.
