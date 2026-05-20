# Openness Verification

candidate_id: R010
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The worst-case constant infinity-norm discrepancy version of the Komlos
conjecture for unit Euclidean-norm columns.

## Source Angles

1. Current expert seminar:
   - citation: Nikhil Bansal, 2026, "On the Komlos Conjecture", Simons
     Institute.
   - exact location: abstract.
   - evidence quote: "O((log n)^(1/4)) bound"
   - relationship: current state-of-art talk reports a polylogarithmic bound,
     not the conjectured constant.

2. Open-problem-bank source:
   - citation: Emergent Mind, 2026, "Komlos conjecture (constant l-infinity
     discrepancy for unit-norm columns)".
   - exact location: open-problems page.
   - evidence quote: "central open problems"
   - relationship: independent problem-bank source labels Komlos as open.

3. Recent algorithmic paper:
   - citation: Gribanov et al., 2026, "Algorithms for Standard-form ILP
     Problems via Komlos' Discrepancy Setting", arXiv:2604.09806.
   - exact location: abstract.
   - evidence quote: "Under the Komlos conjecture"
   - relationship: uses the conjecture as a conditional assumption in 2026.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Komlos conjecture discrepancy' --category math.CO --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned `[]` for this narrow math.CO query on 2026-05-20.
   - relationship: no recent arXiv closure was found by this query; because
     the query is narrow, the verdict relies on the three source angles above.

## Alias And Closure Search

- aliases checked: Komlos conjecture; vector balancing; matrix discrepancy;
  l-infinity discrepancy; unit-norm columns.
- stronger theorems checked: Beck-Fiala variants, Banaszczyk bounds,
  smoothed-analysis results, algorithmic discrepancy bounds.
- special cases checked: smoothed setting, vector coloring, bounded column
  degree, and ILP consequences under the conjecture.
- counterexamples checked: no accepted counterexample to the base conjecture
  found; withdrawn or erroneous adjacent preprints are not counted as evidence.
- recent author/citation trails checked: Bansal 2026, Gribanov et al. 2026,
  Bansal-Jiang-Meka-Singla-Sinha smoothed-analysis trail, and open-problem
  index pages.

## Verdict

`OPEN-VERIFIED`. This is a probability/discrepancy candidate with strong
intermediate-win potential: exact hard-instance construction and restricted
matrix-class bounds can be independently verified.
