# Openness Verification

candidate_id: R001
verified_date: 2026-05-20
status: OPEN-WEAK

## Exact Target Checked

Directed-3-cycle special case of the locally finite perturbation tournament
analogue: construct a countably infinite tournament with no directed 3-cycle
such that every nonempty locally finite perturbation contains a directed
3-cycle.

## Source Angles

1. Original source:
   - citation: Bonamy; Groenland; Johnston; Morrison; Scott, 2026, "Infinite
     induced-saturated graphs", Section 8 Problem 8.3 and Conjecture 8.4.
   - exact location: Cambridge Core article, Section 8 Open problems.
   - evidence quote: "If T is not transitive"
   - relationship: names the all-nontransitive-tournament locally finite
     perturbation conjecture.

2. ArXiv/source identity:
   - citation: Bonamy; Groenland; Johnston; Morrison; Scott, 2025,
     "Infinite induced-saturated graphs", arXiv:2506.08810v3.
   - exact location: arXiv abstract metadata and access page.
   - evidence quote: "Combinatorics (math.CO)"
   - relationship: verifies the preprint identity and version trail; not
     independent openness evidence.

3. Recent search:
   - tool/query: `python connectors/arxiv/server.py search "infinite induced-saturated graphs" --category math.CO --from-date 2025-06-01 --max-results 3`
   - date window: 2025-06-01 to 2026-05-20
   - query_meta: search query is `all:infinite AND all:induced-saturated AND all:graphs AND cat:math.CO AND submittedDate:[202506010000 TO 202605202359]`.
   - evidence: returned arXiv:2506.08810v3, the source paper, and no separate
     closure record in this narrow connector search.
   - relationship: weak recent-search angle only; it does not establish
     broad literature openness.

## Alias And Closure Search

- aliases checked: finite tournament locally finite perturbation; T-free
  tournament; induced-saturated tournament; directed triangle perturbation.
- stronger theorems checked: none found in the narrow connector/search sweep.
- special cases checked: source gives the directed triangle as a single-arc
  example for Problem 8.3, not explicitly as a locally finite perturbation
  theorem.
- counterexamples checked: none found in the narrow search.
- recent author/citation trails checked: Cambridge Core article, arXiv record,
  author-hosted PDF.

## Verdict

`OPEN-WEAK`. This candidate is useful as a tractable warm-up, but it is not a
P10 verified-open row yet because the openness trail does not have three
independent sources. Before any P11 promotion or claim, rerun broader web,
MathSciNet-like, author-page, and citation-trail searches.
