# Openness Verification

candidate_id: R009
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The full Lonely Runner Conjecture for arbitrary numbers of runners.

## Source Angles

1. Recent survey:
   - citation: "The Lonely Runner Conjecture turns 60", 2024,
     arXiv:2409.20160.
   - exact location: abstract.
   - evidence quote: "still widely open"
   - relationship: survey-level source states the broad target remains open.

2. Recent partial progress:
   - citation: Sungkawichai and Trakulthongchai, 2026, "Eleven, twelve, and
     thirteen lonely runners", arXiv:2604.23906.
   - exact location: abstract.
   - evidence quote: "computer-assisted proof"
   - relationship: proves only specified finite cases and therefore confirms
     the general statement is not being claimed there.

3. Current journal source:
   - citation: Fan and Sun, 2026, "Amending the Lonely Runner Spectrum
     Conjecture", Electronic Journal of Combinatorics.
   - exact location: introduction.
   - evidence quote: "long-standing problem"
   - relationship: current paper studies variants and formulations, not a
     general proof.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'lonely runner conjecture' --category math.CO --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned finite-case progress through arXiv:2604.23906 and
     counterexamples to shifted variants; no closure of the original full
     conjecture found.
   - relationship: current arXiv sweep found active partial progress and
     variant hazards, not resolution.

## Alias And Closure Search

- aliases checked: lonely runner problem; Wills-Cusick conjecture; view
  obstruction; maximum loneliness/gap; zonotope formulation.
- stronger theorems checked: finite runner cases, spectrum conjectures, shifted
  Lonely Runner variants, and zonotope/counterexample papers.
- special cases checked: verified finite counts up to recent 2026 claims,
  shifted variants, and computer-assisted reductions.
- counterexamples checked: shifted-version counterexamples exist and are not
  counterexamples to the original conjecture.
- recent author/citation trails checked: Rosenfeld, Trakulthongchai,
  Sungkawichai, Fan-Sun, and current encyclopedia status.

## Verdict

`OPEN-VERIFIED`. This is a good P11 candidate for certificate replay or finite
case simplification; the full conjecture remains too broad for an immediate
solution claim.
