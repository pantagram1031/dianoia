# Openness Verification

candidate_id: R015
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The full Erdos-Szekeres happy ending conjecture for all `n`, especially the
unknown range `n >= 7`.

## Source Angles

1. Recent journal source:
   - citation: 2026, "The Erdos-Szekeres conjecture revisited", Journal of
     Combinatorial Theory, Series A 222.
   - exact location: abstract.
   - evidence quote: "famous and still open"
   - relationship: current paper proves relaxed related results, not the full
     convex-position conjecture.

2. Current reference source:
   - citation: Eric W. Weisstein, 2026, "Happy End Problem", MathWorld.
   - exact location: general status section.
   - evidence quote: "general problem remains open"
   - relationship: independent reference source records `g(n)` known only
     through small values and unknown for `n >= 7`.

3. Independent encyclopedia/status source:
   - citation: Wikipedia contributors, 2026, "Happy ending problem".
   - exact location: current article status.
   - evidence quote: "unknown for all"
   - relationship: independent status source for exact statement and small
     verified values.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Erdos Szekeres conjecture convex polygons' --category math.CO --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned `[]` on 2026-05-20.
   - relationship: no recent narrow arXiv closure found; live search results
     instead show 2026 relaxed/computational Erdos-Szekeres-type work.

## Alias And Closure Search

- aliases checked: Erdos-Szekeres conjecture; happy ending problem; convex
  polygon problem; `g(n)` convex position.
- stronger theorems checked: SAT/formal proofs for `g(6)=17`, upper-bound
  improvements, split-polygon relaxations, empty hexagon variants.
- special cases checked: `n=3,4,5,6`, SAT/formalized hexagon certificates,
  relaxed split `k`-gon thresholds.
- counterexamples checked: lower-bound constructions match known small values;
  no accepted counterexample to the conjectured formula found.
- recent author/citation trails checked: 2026 JCTA revisited paper, MathWorld,
  Wikipedia status, and recent SAT/ASP modeling work.

## Verdict

`OPEN-VERIFIED`. The full conjecture is difficult, but certificate replay and
relaxed-variant improvements make it a concrete P11 candidate.
