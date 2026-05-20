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

## 2026-05-20T20:34:00+09:00

- Enhanced `connectors/arxiv/` with category/date-bounded search and an
  `openness` command that emits reproducible `query_meta` for openness trails.
- Added `tools/verify_research_state.py` and wired it into
  `tools/verify_all.py` so P9-P13 scaffolding is checked every session.
- Added `templates/research_candidate/` for P10 candidate curation and P12
  novelty/claim gates.
- Marked P9 INFRA complete and opened P10 CURATION as the current priority.

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
