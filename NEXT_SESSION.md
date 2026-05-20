# Next Session

Resume Phase 2.

Immediate next step:
Implement the first DIAGNOSIS.md patch in severity order.

First patch target:
- `prompts/prove.md`: add stale-active/closed-active handling, supersession
  evidence, and postconditions that make the fake `halt_flag=true` smoke test
  deterministic.

Important:
- `AGENTS.md` is constitutional. If the required smoke test cannot pass without
  changing `AGENTS.md`, write `APPROVED_CHANGES.md` and `QUESTIONS.md`, then
  halt BLOCKED_ON_USER.
