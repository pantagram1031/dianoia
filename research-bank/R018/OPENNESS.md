# Openness Verification

candidate_id: R018
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The Hadwiger-Boltyanski illumination conjecture for general convex bodies in
dimension `n >= 3`.

## Source Angles

1. Current survey-style source:
   - citation: Arman et al., 2024, "On Hadwiger's covering problem in small
     dimensions", Canadian Mathematical Bulletin.
   - exact location: introduction.
   - evidence quote: "is wide open"
   - relationship: identifies the equivalent illumination conjecture and its
     current open status.

2. Current seminar/status source:
   - citation: Vritsiou, 2026, University of Missouri seminar abstract.
   - exact location: abstract.
   - evidence quote: "still open in dimension 3 and above"
   - relationship: confirms the full conjecture remains open while special
     symmetric bodies have progress.

3. Recent partial-progress source:
   - citation: "Illumination number of 3-dimensional cap bodies", 2026,
     Discrete Mathematics 349(7).
   - exact location: abstract.
   - evidence quote: "remains open in general"
   - relationship: proves the conjecture for a broader cap-body class, not for
     all convex bodies.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'illumination conjecture convex bodies Hadwiger' --category math.MG --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned `[]` on 2026-05-20.
   - relationship: no narrow recent arXiv closure found in geometry.

## Alias And Closure Search

- aliases checked: Hadwiger covering conjecture; illumination conjecture;
  Boltyanski illumination problem; Gohberg-Markus homothetic covering problem.
- stronger theorems checked: all convex bodies, centrally symmetric bodies,
  1-symmetric bodies, 1-unconditional bodies, zonoids, constant-width bodies,
  and cap bodies.
- special cases checked: dimension 2, symmetric cap bodies, 3D cap bodies,
  1-symmetric and 1-unconditional classes.
- counterexamples checked: no accepted counterexample found in status sources.
- recent author/citation trails checked: 2024 small-dimension covering paper,
  2026 seminar abstract, 2026 cap-body paper, and current encyclopedia status.

## Verdict

`OPEN-VERIFIED`. Full resolution is too ambitious for a first attempt, but
restricted body classes, finite polytope reductions, and exact illumination
certificates provide concrete partial-progress targets.
