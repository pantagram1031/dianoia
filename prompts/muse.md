Route a bounded idea-generation request to the muser subagent without merging ideas into proof state.

[INPUTS]
1. Active slug from `problems/.active`.
2. Optional focus string from the user or current open gap.

[PRECONDITIONS]
1. `problems/.active` names exactly one slug.
2. The active problem directory exists with `problem.md`, `session_state.md`, `claim_ledger.md`, and `work_journal.md`.

[PROCEDURE]
1. Read `IDENTITY.md`, `goal.md`, active `session_state.md`, the ledger tail, current open gaps, and `survey.md` when present.
2. Invoke `prompts/subagents/muser.md` with the active problem summary, open gaps, and optional focus string.
3. Require the muser to write only inside `problems/<slug>/inbox/<unit-id>/muser/`.
4. Leave muser artifacts in the inbox drop zone; a later Director review may copy selected ideas to `problems/<slug>/ideas/`.
5. Invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. `problems/<slug>/inbox/<unit-id>/muser/return.md`.
2. Optional idea artifact referenced by the muser return.

[FAILURE]
1. Missing active problem: print `BLOCKED: no active problem for muse.` and stop.
2. Missing active context files: print `BLOCKED: missing muse input <path>.` and stop.
