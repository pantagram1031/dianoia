# Openness Verification

candidate_id: R003
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

Full Minkowski and Hausdorff dimension for all Kakeya sets in `R^n`, restricted
to dimensions `n >= 4`.

## Source Angles

1. Open-problem page:
   - citation: Emergent Mind editors, 2026, "Kakeya set conjecture in higher
     dimensions (n >= 4)", Statement and Background sections.
   - exact location: Statement and Background sections.
   - evidence quote: "remaining open cases are n >= 4"
   - relationship: current open-problem statement after the 3D breakthrough.

2. Independent mathematical-institute article:
   - citation: Institute for Advanced Study, 2025, "A Three-Dimensional
     Breakthrough", Institute Letter Spring 2025.
   - exact location: paragraph on further work and higher dimensions.
   - evidence quote: "further work remains"
   - relationship: independent account confirms that solving 3D did not close
     higher dimensions.

3. Primary theorem source:
   - citation: Hong Wang; Joshua Zahl, 2025, "Volume estimates for unions of
     convex sets, and the Kakeya set conjecture in three dimensions", arXiv
     abstract.
   - exact location: arXiv abstract.
   - evidence quote: "Kakeya set in R^3"
   - relationship: theorem source proves only `R^3`, matching the candidate
     boundary `n >= 4`.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Kakeya conjecture higher dimensions' --from-date 2025-02-01 --max-results 5`
   - date window: 2025-02-01 to 2026-05-20
   - query_meta: tokenized all-field query over `Kakeya`, `conjecture`,
     `higher`, `dimensions`.
   - evidence: connector returned no matching arXiv closure records for that
     exact phrase window.
   - relationship: weak recent-search angle; used only together with the three
     named sources above.

## Alias And Closure Search

- aliases checked: Kakeya set conjecture; Besicovitch sets; Euclidean Kakeya;
  higher-dimensional Kakeya; Kakeya in `R^4`.
- stronger theorems checked: Wang-Zahl 3D theorem; no `n >= 4` closure found.
- special cases checked: `n=2` solved, `n=3` solved, `n>=4` candidate remains.
- counterexamples checked: none found; candidate asks for dimension lower bound.
- recent author/citation trails checked: Wang-Zahl arXiv page, IAS article,
  Emergent Mind open-problem page.

## Verdict

`OPEN-VERIFIED`. This is high difficulty, but it is a clean post-2025 boundary
candidate because the 3D theorem sharply defines what remains open.
