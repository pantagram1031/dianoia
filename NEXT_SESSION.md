# Next Session

Resume continuous improvement.

Immediate next step:
Harden benchmark reproducibility before adding B6.

Current state:
- Phase 2 is complete: `prompts/prove.md`, `prompts/resume.md`,
  `prompts/00-intake.md`, and `AGENTS.md` are patched and smoke-tested.
- `capability-test/PHASE2-SMOKE-agents-router.md` records router-level smoke
  evidence.
- Phase 3 is complete with VALUE_ADDED in `capability-test/RETEST.md`.
- Prior MASTERPIECE baseline is complete with 5/5 VALUE_ADDED rows in `BENCHMARK.md`: B1 number
  theory, B2 combinatorics, B3 geometry, B4 probability, and B5 algebra.
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
- `capability-test/MASTERPIECE.md` is baseline evidence, not a stop condition.
- Current continuous-improvement priority: add reproducibility tooling/runbook
  so future B6+ rows prefer full fresh raw and dianoia runs and clearly label
  weaker evidence.
- Baseline verifier exists: `python tools\verify_dianoia_state.py`. Latest
  smoke is `capability-test/BENCHMARK-DIFFERENCE-EVIDENCE-VERIFY-20260521.md`;
  warnings are expected for UNVERIFIED token accounting in B1-B5. It also
  checks B6+ source citation metadata, structured comparison difference
  evidence, and that docs/state references to `capability-test/*.md` artifacts
  resolve.
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
