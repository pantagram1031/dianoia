# Decisions

| ID | date | decision | rationale | status |
|----|------|----------|-----------|--------|
| D-001 | 2026-05-20 | Treat the pulled cycle-4 repository state as the prior experiment under audit. | The active goal names cycle-4 and stale problems/.active as the current baseline; the worktree after pull contains those artifacts. | ACTIVE |
| D-002 | 2026-05-20 | Treat `capability-test/MASTERPIECE.md` as baseline evidence, not a terminal condition. | The user clarified that dianoia is a self-improving prompt/workflow and should keep improving after the initial checklist. | ACTIVE |
| D-003 | 2026-05-21 | Treat B1-B5 as historical baseline rows; the forward victory condition is 5 contamination-free novel VALUE_ADDED head-to-head benchmarks across at least 3 mathematical areas. | The user clarified that the stale phase ladder text is outdated in details but the fundamental target remains automatic mathematical problem solving with honest value-added comparisons against raw GPT-5.5. Current work should harden B6+ and then run fresh contamination-free benchmarks rather than re-declaring mastery from the old rows. | ACTIVE |
| D-004 | 2026-05-20 | Treat P10 research-bank entries as gated artifacts, not informal leads. | The RESEARCH_CONTRIBUTION goal can be derailed by plausible-sounding but closed or renamed problems. Each candidate therefore starts from `templates/research_candidate/`, requires a current `OPENNESS.md`, and is checked by `tools/verify_research_state.py` before P11 attempts. | ACTIVE |
