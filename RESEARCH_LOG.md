# Research Log

Purpose: session-by-session record for the RESEARCH_CONTRIBUTION objective.

Current objective:

- Produce a verifiable mathematical contribution: proof of a published-as-open
  problem, counterexample to a published conjecture, improvement to a published
  bound, or a new published connection.
- Any breakthrough or intermediate win must pass adversarial review,
  openness/novelty confirmation, and formal/computational checking where
  applicable.
- Do not claim publication or public mathematical priority. A successful gate
  halts as `BLOCKED_ON_USER` for external mathematician review.

## 2026-05-20T21:58:00+09:00

- Opened P11 with `R020` no-three-in-line.
- Raw route outcome: `NO-PROGRESS`; it located the Prellberg 2026 CSP source
  but did not independently verify or extend it.
- Dianoia route outcome: `PARTIAL-PROGRESS`; added an exact verifier and
  replayed Prellberg's `N=47` certificate with no line violations.
- Verification evidence:
  `research-bank/R020/certificates/prellberg-n47.verify.json`,
  `tests/test_no_three_in_line_verify.py`, and `tools/verify_all.py`.
- Claim discipline: no new result, no `CLAIMS.md` row, no external-review halt.

## 2026-05-20T21:46:00+09:00

- Added six counted P10 `OPEN-VERIFIED` candidates:
  - `R016`: Barnette's conjecture, graph theory, rank B.
  - `R017`: Graceful Tree Conjecture, graph theory, rank A.
  - `R018`: Hadwiger-Boltyanski illumination conjecture, geometry, rank C.
  - `R019`: Ryser-Brualdi-Stein Latin square transversal conjecture, design
    theory, rank B.
  - `R020`: no-three-in-line problem, discrete geometry, rank A.
  - `R021`: Erdos-Gyarfas power-of-two cycles conjecture, graph theory, rank B.
- Current P10 progress: 20/20 `OPEN-VERIFIED` candidates across 10/4 required
  areas. P10 gate is satisfied.
- P11 selection note: prioritize `R020` first because exact coordinates,
  integer line checks, and CSP certificate replay make a fast honest attempt
  path. `R013` and `R017` are the next rank-A alternatives.

## 2026-05-20T21:31:00+09:00

- Added four counted P10 `OPEN-VERIFIED` candidates:
  - `R012`: Caccetta-Haggkvist conjecture, combinatorics, rank B.
  - `R013`: 1/3-2/3 conjecture for finite posets, order theory, rank A.
  - `R014`: Artin primitive root conjecture, number theory, rank C.
  - `R015`: Erdos-Szekeres happy ending conjecture, geometry, rank B.
- Current P10 progress: 14/20 `OPEN-VERIFIED` candidates across 7/4 required
  areas. Need 6 more candidates before P11 scale-up.
- Selection bias note: this batch added two rank-B computational combinatorics
  candidates and one rank-A exact poset candidate, improving the bank's
  practical P11 attack surface.

## 2026-05-20T21:22:00+09:00

- Added four counted P10 `OPEN-VERIFIED` candidates:
  - `R008`: Erdos-Straus conjecture, number theory, rank B.
  - `R009`: Lonely Runner conjecture, number theory, rank B.
  - `R010`: Komlos discrepancy conjecture, probability, rank C.
  - `R011`: symmetric Mahler conjecture in dimensions `n >= 4`, geometry,
    rank C.
- Current P10 progress: 10/20 `OPEN-VERIFIED` candidates across 6/4 required
  areas. Need 10 more candidates before P11 scale-up.
- Selection bias note: the newly added rank B/C candidates emphasize bounded,
  exact-checkable intermediate wins: modular covers, certificate replay,
  finite discrepancy checks, and rational convex-polytope computations.

## 2026-05-20T21:12:00+09:00

- Hardened the arXiv connector's search path against live API instability:
  HTTP 429 and timeout failures now become explicit `UNVERIFIED` records with
  query URLs, preserving honesty in openness trails.
- Added three counted P10 `OPEN-VERIFIED` candidates:
  - `R005`: Frankl's union-closed sets conjecture, combinatorics, rank B.
  - `R006`: Hadwiger-Nelson chromatic number of the plane, geometry, rank C.
  - `R007`: Hadwiger's graph-minor conjecture, combinatorics, rank D.
- Current P10 progress: 6/20 `OPEN-VERIFIED` candidates across 5/4 required
  areas. Need 14 more candidates; area diversity gate is satisfied but should
  keep broadening.

## 2026-05-20T20:34:00+09:00

- Enhanced `connectors/arxiv/` with category/date-bounded search and an
  `openness` command that emits reproducible `query_meta` for openness trails.
- Added `tools/verify_research_state.py` and wired it into
  `tools/verify_all.py` so P9-P13 scaffolding is checked every session.
- Added `templates/research_candidate/` for P10 candidate curation and P12
  novelty/claim gates.
- Marked P9 INFRA complete and opened P10 CURATION as the current priority.
- Fixed arXiv multi-word search precision after a live openness-search smoke
  returned unrelated records.
- Added `research-bank/R001/` as an `OPEN-WEAK` combinatorics warm-up candidate:
  the directed-3-cycle special case of the locally finite tournament
  perturbation conjecture. It is not counted toward the 20 verified-open P10
  target.

## 2026-05-20T20:56:00+09:00

- Strengthened `tools/verify_research_state.py` so P10 progress is counted
  from `research-bank/INDEX.md` and index `OPEN-VERIFIED` rows must match each
  candidate's `OPENNESS.md` status.
- Added three counted `OPEN-VERIFIED` candidates:
  - `R002`: perfect cuboid, number theory, rank C.
  - `R003`: Kakeya set conjecture in dimensions `n >= 4`, real analysis,
    rank D.
  - `R004`: Koethe conjecture, algebra, rank D.
- Current P10 progress: 3/20 `OPEN-VERIFIED` candidates across 3/4 required
  areas. Need to prioritize one more area plus more tractable rank A/B rows.

## 2026-05-21T02:05:00+09:00

- Goal updated from forward benchmark evidence to research contribution.
- MASTERPIECE artifact is present, so the new work starts at P9 INFRA.
- Immediate focus: build formal-check, openness-verification, and
  adversarial-novelty infrastructure before curating 20 verified-open problems.

## 2026-05-21T02:16:00+09:00

- Added `connectors/lean/` as the first P9 formal-check connector.
- The wrapper reports `UNAVAILABLE`/`UNVERIFIED` when Lean is not installed
  rather than silently passing a formal gate.

## 2026-05-21T02:24:00+09:00

- Added `skills/openness-verification/SKILL.md` and
  `skills/adversarial-novelty-check/SKILL.md`.
- Wired researcher prompt to use both skills for research-bank candidates and
  any novelty-sensitive `CLAIMS.md` promotion.
