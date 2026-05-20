# Openness Verification

candidate_id: R011
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The centrally symmetric Mahler conjecture in dimensions `n >= 4`.

## Source Angles

1. Recent frontier paper:
   - citation: Chen, Li, Xi, and Xu, 2026, "The Symmetric Mahler Inequality in
     Dimension Three via Admissible Shadow Systems", arXiv:2605.13795.
   - exact location: abstract.
   - evidence quote: "dimension three"
   - relationship: current work gives a new 3D proof, not higher-dimensional
     resolution.

2. Independent status source:
   - citation: Wikipedia contributors, 2026, "Mahler volume".
   - exact location: Extreme shapes section.
   - evidence quote: "unsolved when n >= 4"
   - relationship: current reference source explicitly states the unresolved
     dimensional range.

3. Earlier expository/source paper:
   - citation: Matthew Tointon, 2018, "The Mahler conjecture in two dimensions
     via the probabilistic method", arXiv:1707.07502.
   - exact location: abstract.
   - evidence quote: "open in dimensions 4 and greater"
   - relationship: independent paper cleanly records the higher-dimensional
     open range and lower-dimensional history.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Mahler conjecture convex body' --category math.MG --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned arXiv:2605.09334 and arXiv:2605.13795, both
     dimension-three progress; no higher-dimensional closure found.
   - relationship: current arXiv sweep found recent boundary progress, not
     resolution of the target range.

## Alias And Closure Search

- aliases checked: Mahler volume; symmetric Mahler conjecture; volume product;
  Hanner polytope minimizer; cube/cross-polytope minimizer.
- stronger theorems checked: non-symmetric dimension-three result, symmetric
  dimension-three proofs, local minimizer results near Hanner polytopes.
- special cases checked: dimensions 2 and 3, unconditional bodies, zonoids,
  Hanner-polytopal neighborhoods.
- counterexamples checked: no accepted counterexample to the symmetric
  higher-dimensional conjecture found.
- recent author/citation trails checked: Chen-Li-Xi-Xu 2026, Tointon 2018,
  MathWorld/Wikipedia-style status, and current arXiv metric-geometry results.

## Verdict

`OPEN-VERIFIED`. The full conjecture is hard, but local stability, shadow-system
subclaims, and finite-dimensional reductions are plausible intermediate wins.
