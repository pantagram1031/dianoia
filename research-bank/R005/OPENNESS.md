# Openness Verification

candidate_id: R005
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The full Frankl union-closed sets conjecture for all finite nonempty
union-closed families.

## Source Angles

1. Recent source paper:
   - citation: Christopher Bouchard, 2025, "On the lattice formulation of the
     union-closed sets conjecture", arXiv:2503.00277.
   - exact location: arXiv abstract.
   - evidence quote: "well-studied problem"
   - relationship: recent work gives necessary conditions for a minimum
     counterexample rather than a full proof.

2. Independent status source:
   - citation: Wikipedia contributors, 2026, "Union-closed sets conjecture".
   - exact location: article lead and partial-progress history.
   - evidence quote: "open problem"
   - relationship: current independent status page marks the full conjecture
     open while recording partial constant lower bounds.

3. Classic formulation source:
   - citation: Bjorn Poonen, 1992, "Union-closed families", Journal of
     Combinatorial Theory A.
   - exact location: abstract page.
   - evidence quote: "problem remains unsolved"
   - relationship: older independent source gives equivalent formulations and
     small special cases, so it is useful for guarding against alias confusion.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Frankl union closed sets conjecture' --category math.CO --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned `[]` on 2026-05-20.
   - relationship: no recent arXiv closure candidate was found by this narrow
     connector query; because absence is weak evidence, the verdict also relies
     on the three source angles above.

## Alias And Closure Search

- aliases checked: Frankl conjecture; union-closed families conjecture; lattice
  formulation; intersection-closed dual.
- stronger theorems checked: entropy constant lower bounds after Gilmer; lattice
  necessary conditions; non-uniform distribution variants.
- special cases checked: small ground-set classifications, FC-family variants,
  and equivalent graph/lattice formulations.
- counterexamples checked: no accepted counterexample or general proof found in
  the current source sweep.
- recent author/citation trails checked: Bouchard 2025, Gilmer-era constant
  improvements, Poonen equivalent formulations, current problem-bank pages.

## Verdict

`OPEN-VERIFIED`. The global conjecture is high-risk, but finite classification,
minimal-counterexample filters, and exact-search certificates provide concrete
P11 attack surfaces.
