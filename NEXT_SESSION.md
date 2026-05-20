# Next Session

Resume continuous improvement.

Immediate next step:
Continue P10 CURATION for the RESEARCH_CONTRIBUTION objective: add more
`OPEN-VERIFIED` research-bank candidates, prioritizing tractable rank A/B
targets and maintaining area diversity.

Current state:
- Phase 2 is complete: `prompts/prove.md`, `prompts/resume.md`,
  `prompts/00-intake.md`, and `AGENTS.md` are patched and smoke-tested.
- `capability-test/PHASE2-SMOKE-agents-router.md` records router-level smoke
  evidence.
- Phase 3 is complete with VALUE_ADDED in `capability-test/RETEST.md`.
- Prior MASTERPIECE baseline has 5/5 VALUE_ADDED rows in `BENCHMARK.md`: B1
  number theory, B2 combinatorics, B3 geometry, B4 probability, and B5 algebra.
  These are historical baseline rows, not the current victory condition.
- Phase 5 is complete with 5/5 skills: `skills/pollack-character/SKILL.md`,
  `skills/coverage-systems/SKILL.md`, `skills/arxiv-fetch/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, and
  `skills/citation-discipline/SKILL.md`, each referenced by at least one
  subagent prompt.
- Phase 6 has 2/2 connectors: `connectors/arxiv/` and `connectors/oeis/`,
  both referenced by the researcher subagent prompt.
- Phase 7 docs are current as of B5 plus completed Phase 5/6:
  `README.md`, `ARCHITECTURE.md`, `EXAMPLES.md`, and `CHANGELOG.md`.

Important:
- Active goal changed to RESEARCH_CONTRIBUTION. Do not continue benchmark-only
  work unless it directly supports research contribution infrastructure.
- MASTERPIECE baseline is present, so the active phase is P9 INFRA.
- Persistent research state files now include `RESEARCH_LOG.md`, `CLAIMS.md`,
  and `research-bank/`.
- P9 INFRA is complete:
  - `connectors/lean/` reports `UNVERIFIED` when Lean is unavailable.
  - `connectors/arxiv/` supports date/category search and `openness` queries
    with reproducible `query_meta`.
  - `skills/openness-verification/` and
    `skills/adversarial-novelty-check/` are wired into Researcher.
  - `tools/verify_research_state.py` is included in `tools/verify_all.py`.
  - `templates/research_candidate/` contains the P10/P12 artifact skeletons.
- `capability-test/MASTERPIECE.md` is baseline evidence, not a stop condition.
- Live victory condition: a verifiable math contribution that passes openness,
  novelty, adversarial, and formal/computational gates, then halts
  BLOCKED_ON_USER for external mathematician review.
- B6 source is selected:
  `benchmark-bank/B6/SOURCE.md` and `benchmark-bank/B6/PROBLEM.md`.
- B6 raw baseline is complete:
  `C:\Users\SAMSUNG\Downloads\raw-attempt-7\answer.md` and
  `C:\Users\SAMSUNG\Downloads\raw-attempt-7\run.md`.
- B6 has `benchmark-bank/B6/RUN-PARTIAL.md` and
  `benchmark-bank/B6/RAW-AUDIT.md`; do not create `BENCHMARK.md` row until the
  dianoia run and comparison artifacts exist.
- Current priority: P10 curation of 20 verified-open candidates across 4
  areas. Use `templates/research_candidate/` for each candidate and preserve
  openness search metadata.
- P10 seed state: `research-bank/R001/` exists as an `OPEN-WEAK`
  combinatorics warm-up candidate for the directed-3-cycle special case of
  Bonamy-Groenland-Johnston-Morrison-Scott Conjecture 8.4. It is not counted
  toward the 20 verified-open target until broader independent openness sources
  are added.
- P10 counted state: 10/20 `OPEN-VERIFIED` candidates across 6/4 required
  areas:
  - `research-bank/R002/`: perfect cuboid, number theory, rank C.
  - `research-bank/R003/`: Kakeya set conjecture in dimensions `n >= 4`, real
    analysis, rank D.
  - `research-bank/R004/`: Koethe conjecture, algebra, rank D.
  - `research-bank/R005/`: Frankl's union-closed sets conjecture,
    combinatorics, rank B.
  - `research-bank/R006/`: Hadwiger-Nelson chromatic number of the plane,
    geometry, rank C.
  - `research-bank/R007/`: Hadwiger's graph-minor conjecture,
    combinatorics, rank D.
  - `research-bank/R008/`: Erdos-Straus conjecture, number theory, rank B.
  - `research-bank/R009/`: Lonely Runner conjecture, number theory, rank B.
  - `research-bank/R010/`: Komlos discrepancy conjecture, probability, rank C.
  - `research-bank/R011/`: symmetric Mahler conjecture in dimensions `n >= 4`,
    geometry, rank C.
- `tools/verify_research_state.py` now reports P10 counts and rejects
  `OPEN-VERIFIED` index rows whose candidate `OPENNESS.md` status disagrees.
- `connectors/arxiv/server.py` now returns explicit `UNVERIFIED` records for
  HTTP 429 and timeout failures; preserve those records in openness trails
  instead of treating failed searches as evidence of closure.
- Next concrete deliverable: add at least 2-3 more `OPEN-VERIFIED` candidates,
  prioritizing higher-tractability rank A/B targets and exact-checkable
  subtargets. P10 still needs 10 more counted candidates before P11 scale-up.
- Baseline verifier exists: `python tools\verify_dianoia_state.py`. Latest
  smoke is `capability-test/BENCHMARK-RUN-WORKSPACE-PATHS-VERIFY-20260521.md`;
  warnings are expected for UNVERIFIED token accounting in B1-B5. It also
  checks B6+ source citation metadata, comparison verdict consistency,
  structured comparison difference evidence, source artifact paths, run
  workspace paths,
  `UNVERIFIED` token blockers/plans, and that docs/state references to
  `capability-test/*.md` artifacts resolve.
- Phase-loop verifier exists: `python tools\verify_phase_loop.py`. Latest smoke
  is `capability-test/PHASE-LOOP-VERIFY-20260520.md`.
- Routing guard verifier exists: `python tools\verify_routing_guards.py`.
  Latest smoke is `capability-test/ROUTING-GUARDS-VERIFY-20260520.md`.
- Connector contract verifier exists: `python tools\verify_connectors.py`.
  Latest smoke is `capability-test/CONNECTOR-CONTRACT-VERIFY-20260520.md`.
- Full verifier exists: `python tools\verify_all.py`. It now runs unit tests,
  state verification, phase-loop verification, routing-guard verification, and
  connector contract verification. Latest smoke is
  `capability-test/CONNECTOR-CONTRACT-VERIFY-20260520.md`.
- B6+ benchmark format is governed by `benchmark-bank/RUNBOOK.md` and
  `templates/benchmark_case/`; the verifier fails B6+ rows missing `RUN.md`.
