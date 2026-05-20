# Openness Verification

candidate_id: R007
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

Hadwiger's graph-minor conjecture in full generality, especially unresolved
cases `t >= 7`.

## Source Angles

1. Recent arXiv source:
   - citation: Costa, Luu, Wood, and Yip, 2025, "Verifying Hadwiger's
     Conjecture for Examples of Graphs with alpha(G)=2", arXiv:2512.17114.
   - exact location: abstract.
   - evidence quote: "important open problems"
   - relationship: proves special examples and identifies remaining unknown
     alpha(G)=2 classes rather than closing the conjecture.

2. Recent journal source:
   - citation: Yepremyan et al., 2025, "Dense minors of graphs with
     independence number two", Journal of Combinatorial Theory B.
   - exact location: abstract page.
   - evidence quote: "wide open"
   - relationship: independent recent partial-progress paper states the
     unresolved general range.

3. Current seminar/status source:
   - citation: Agnes Totschnig, 2026, "Colouring graphs with forbidden
     7-vertex minors", University of Waterloo seminar abstract.
   - exact location: abstract.
   - evidence quote: "k at least 7 remain open"
   - relationship: current research seminar source gives live status for the
     first unresolved range.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Hadwiger conjecture graph minor chromatic' --category math.CO --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned arXiv:2512.17114 and arXiv:2512.20392; neither records
     a proof of the full Hadwiger graph-minor conjecture.
   - relationship: recent connector sweep found special-case progress and a
     related odd-Hadwiger disproof, not a closure of the base conjecture.

## Alias And Closure Search

- aliases checked: Hadwiger graph-minor conjecture; clique minor coloring
  conjecture; `K_t` minor conjecture; alpha(G)=2 Hadwiger.
- stronger theorems checked: odd Hadwiger variants, dense-minor relaxations,
  topological-minor variants, and asymptotic coloring bounds.
- special cases checked: `t <= 6`, alpha(G)=2 subclasses, forbidden
  7-vertex-minor approximations.
- counterexamples checked: no accepted counterexample to the base conjecture
  found; related stronger variants have counterexamples and are not conflated
  with the base target.
- recent author/citation trails checked: Costa-Luu-Wood-Yip 2025, Yepremyan
  et al. 2025, Totschnig 2026, and current encyclopedia status.

## Verdict

`OPEN-VERIFIED`. The full conjecture is rank-D hard, but restricted-class and
near-minor variants are suitable for dianoia's adversarial, computational, and
formal-review gates.
