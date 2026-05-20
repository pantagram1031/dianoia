# Openness Verification

candidate_id: R006
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The exact chromatic number of the Euclidean plane under unit-distance
constraints.

## Source Angles

1. Current reference source:
   - citation: Eric W. Weisstein, 2026, "Hadwiger-Nelson Problem", MathWorld.
   - exact location: lead and bound statement.
   - evidence quote: "5, 6, or 7"
   - relationship: current mathematical reference source records only the
     range, not a resolved value.

2. Collaborative research source:
   - citation: Polymath16 contributors, 2026, "Hadwiger-Nelson problem".
   - exact location: lead and goal list.
   - evidence quote: "Find a 6-chromatic unit-distance graph"
   - relationship: independent research record still frames central
     improvements as open search targets.

3. Breakthrough lower-bound paper:
   - citation: Aubrey D. N. J. de Grey, 2018, "The Chromatic Number of the
     Plane is at least 5", arXiv:1804.02385.
   - exact location: abstract and title.
   - evidence quote: "at least 5"
   - relationship: establishes the modern lower bound while leaving the exact
     value open.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Hadwiger Nelson chromatic number plane' --category math.CO --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned `[]` on 2026-05-20.
   - relationship: no recent narrow arXiv closure candidate was found; the
     openness verdict rests on the three independent status angles.

## Alias And Closure Search

- aliases checked: chromatic number of the plane; unit-distance graph coloring;
  CNP; Polymath16 Hadwiger-Nelson.
- stronger theorems checked: de Grey lower bound, Polymath graph-size
  reductions, fractional chromatic-number records.
- special cases checked: finite unit-distance graph witnesses, disk/region
  coloring variants, higher-dimensional bounds.
- counterexamples checked: no accepted proof of value 5, 6, or 7 found in the
  current sweep.
- recent author/citation trails checked: MathWorld status, Polymath16 wiki,
  de Grey 2018 lower-bound lineage, Open Problems Project listing.

## Verdict

`OPEN-VERIFIED`. This candidate supplies the required geometry area for P10.
The full problem is difficult, but graph-certificate improvements are concrete
and mechanically checkable.
