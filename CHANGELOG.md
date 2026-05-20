# Changelog

## 2026-05-20 Research Contribution P9 Infra

- Added Lean formal-check connector scaffolding, with explicit `UNVERIFIED`
  behavior when Lean is unavailable.
- Enhanced the arXiv connector with date/category search and openness-lead
  query metadata.
- Added openness-verification and adversarial-novelty skills and wired them
  into Researcher.
- Added research-state verification and candidate templates to prepare P10
  curation and P12 claim gates.
- Fixed arXiv multi-word query precision after live smoke testing and seeded
  `research-bank/R001/` as an `OPEN-WEAK` warm-up candidate.

## 2026-05-21 Continuous Objective Refresh

- Re-centered ROADMAP, README, BENCHMARK, NEXT_SESSION, and DECISIONS on the
  forward objective: 5 contamination-free novel VALUE_ADDED head-to-head
  benchmarks against raw GPT-5.5 across at least 3 mathematical areas.
- Clarified that B1-B5 remain historical baseline evidence, not current victory
  evidence.

## 2026-05-20 MASTERPIECE Workstream

- Phase 0: added `capability-test/VERIFY_PRIOR.md`, showing the earlier S_a
  experiment was not a fair test because stale `.active` state prevented the
  fresh phase loop from firing.
- Phase 1: added `DIAGNOSIS.md` with ranked root causes and success criteria.
- Phase 2: fixed stale-active routing in `prompts/prove.md`,
  `prompts/resume.md`, `prompts/00-intake.md`, and approved `AGENTS.md`
  routing; added smoke artifacts under `capability-test/`.
- Phase 3: retested the S_a problem and recorded VALUE_ADDED in
  `capability-test/RETEST.md`.
- Phase 4: promoted the S_a retest into benchmark B1 under
  `benchmark-bank/B1/`, added B2 for Bai-Berczi properly colored trees, and
  added B3 for Samarakkody's isoperimetric formalization, and added B4 for
  Jana-Rani random-matrix CLT scope checking, and added B5 for
  Caprace-Janssens-Thilmany representation-theory quantifier checking.
- Phase 5: added five referenced skills under `skills/`.
- Phase 6: added working arXiv and OEIS connectors under `connectors/`.
- Phase 7: refreshed README, architecture, examples, and changelog docs to
  reflect the current repository state through B5.

- iter-1 | dimensions: 2 Verifying | B1 scoped Phase 5 review ordering to the reviewed artifact instead of only 04-develop.
- iter-2 | dimensions: 2 Verifying, 3 Attempting | B2 wired Persona D into Phase 5 review and reviewer subagent contract.
- iter-3 | dimensions: 2 Verifying, 7 Organizing materials | M1 made Phase 5 review inputs depend on the artifact phase so intake review does not require survey.md.
- iter-4 | dimensions: 2 Verifying, 7 Organizing materials | M2 added explicit preconditions to every phase prompt from intake through consolidation.
- iter-5 | dimensions: 7 Organizing materials | M3 added corpus/theorems placeholder for self-contained Phase 6 promotions.
- iter-6 | dimensions: 4 Ideating, 6 Researching collaboratively | M4 added top-level muse and consult prompts for AGENTS first-message routes.
- iter-7 | dimensions: 1 Proving, 3 Attempting, 4 Ideating, 7 Organizing materials, 8 Reading papers | M5 wired surveyor, sanity-checker, prover, muser, and skill-author into their natural phases.
- iter-8 | dimensions: 7 Organizing materials | M6 added a context manifest template and checkpoint rule for per-unit context tracking.
- iter-9 | dimensions: 3 Attempting, 7 Organizing materials | M7 guarded resume so closed v4 halt reasons cannot be reopened by clearing halt_flag.
- iter-10 | dimensions: 1 Proving, 7 Organizing materials | m1 added formalization notes placeholder to the problem skeleton.
- iter-11 | dimensions: 7 Organizing materials | m2 added explicit MSP narration mode to both session state templates.
- iter-12 | dimensions: 5 Asking, 7 Organizing materials | Added audit-backed needs_human gate to prevent evasive user blocking.
- iter-13 | dimensions: 4 Ideating, 6 Researching collaboratively | Added panel prompt and disagreement-triggered panel routing for specialist collaboration.
- iter-14 | dimensions: 8 Reading papers | Wired Researcher into Phase 1 survey citation verification for State of the Art and high-impact references.
- iter-15 | dimensions: 1 Proving, 7 Organizing materials | Added Phase 4 formalization stub or skip-rationale rule for key lemmas.
- iter-16 | dimensions: 7 Organizing materials | Initialized new problem session_state with concrete msp_narration: quiet.
- iter-17 | dimensions: all | Recorded plateau after three consecutive clean/minor-only audits with all dimensions at least 4.
cycle-1 iter-1 | dimensions: 2 Verifying | Require reviewer attempted_attacks evidence before empty defect lists.
cycle-1 iter-2 | dimensions: 1 Proving | Add Phase 4 proof granularity and circularity gate.
cycle-1 iter-3 | dimensions: 7 Organizing materials | Require concrete checkpoint context-manifest evidence fields.
