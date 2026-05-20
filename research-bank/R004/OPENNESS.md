# Openness Verification

candidate_id: R004
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

General Koethe conjecture across all associative rings, not a special class
such as polynomial identity rings, right Noetherian rings, or complete metric
algebras over normed fields.

## Source Angles

1. Current open-problem page:
   - citation: Emergent Mind editors, 2026, "Koethe's Conjecture (general
     case)", Statement and Background sections.
   - exact location: Background section.
   - evidence quote: "general solution is still lacking"
   - relationship: current open-problem statement that distinguishes special
     classes from the general case.

2. Independent status source:
   - citation: Wikipedia contributors, 2026, "Koethe conjecture", lead section
     and equivalent formulations.
   - exact location: lead section.
   - evidence quote: "open as of 2025"
   - relationship: independent current status and equivalent formulations.

3. Survey source:
   - citation: Miguel Ferrero, 2001, "An Introduction to Koethe's Conjecture
     and Polynomial Rings", Introduction, page 139.
   - exact location: Introduction.
   - evidence quote: "most famous open problem"
   - relationship: older survey source giving historical and equivalent-form
     grounding.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Kothe conjecture ring theory' --from-date 2025-01-01 --max-results 5`
   - date window: 2025-01-01 to 2026-05-20
   - query_meta: tokenized all-field search over `Kothe`, `conjecture`, `ring`,
     `theory`.
   - evidence: connector returned no matching arXiv closure records in that
     query window.
   - relationship: weak recent-search angle; reinforces absence of an obvious
     recent closure but is not used alone.

## Alias And Closure Search

- aliases checked: Koethe conjecture; Koethe problem; nil one-sided ideals;
  upper nil radical; polynomial-ring formulation.
- stronger theorems checked: complete metric algebra special case, PI/right
  Noetherian special cases; no general proof found.
- special cases checked: special-class positive results are not counted as
  closing the general case.
- counterexamples checked: no general counterexample found.
- recent author/citation trails checked: Emergent Mind page referencing 2025
  partial result, Wikipedia status, Ferrero survey.

## Verdict

`OPEN-VERIFIED`. This is a hard algebra candidate; initial value should come
from verified special-class reductions, counterexample search for strengthenings,
or a precise obstruction map.
