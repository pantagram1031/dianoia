# Context Manifest

unit_id: cycle-2-t6-ambition-gap
phase: 6-consolidate
phase_prompt: prompts/06-consolidate.md
timestamp: 2026-05-20T10:00:00+09:00

always:
  - IDENTITY.md
  - goal.md
  - AGENTS.md
  - problems/cycle-3-t6-perfect-numbers/session_state.md
  - problems/cycle-3-t6-perfect-numbers/claim_ledger.md

phase_active:
  artifact: problems/cycle-3-t6-perfect-numbers/failures/ambition-gap.md
  prompt: prompts/06-consolidate.md
  required_inputs:
    - hypotheses_live.md
    - proofs/perfect-numbers-attempt.fml
    - dialogue/panel-u03.md
  produced_outputs:
    - failures/ambition-gap.md
    - result.md
    - resume_brief.md

this_unit:
  artifacts_written:
    - failures/ambition-gap.md
    - result.md
    - resume_brief.md
  artifacts_reviewed:
    - hypotheses_live.md
    - proofs/perfect-numbers-attempt.fml
    - dialogue/panel-u03.md
  reviewer_files:
    - reviews/intake-reviewer-D.md
    - reviews/hypotheses-reviewer-D.md
    - reviews/develop-reviewer-D.md
    - reviews/consolidate-reviewer-D.md
  subagent_returns:
    - inbox/u01-survey/researcher/return.md
    - inbox/u03-hypothesize/sanity-checker/sanity.md
    - inbox/u04-develop/prover/return.md
    - inbox/u04-develop/muser/return.md
  journal_fragments_merged:
    - work_journal.md
    - dialogue/panel-u03.md
    - failures/ambition-gap.md
  ledger_delta:
    - C-001
    - C-002
    - C-003
  open_markers:
    - Mersenne-prime infinitude barrier
    - odd-perfect-number obstruction

checkpoint_evidence:
  forbidden_word_scan: zero forbidden ritual markers found
  citation_check: researcher engaged Euclid-Euler and odd-perfect-number state of the art
  review_status: all required A/B/C/D reviews complete with attempted_attacks
  next_atomic_unit: cycle-2 REPORT.md

dropped:
  - path: completed T1-T5 problem directories
    reason: REPORT.md can recover them through T-audits
    recovery: capability-test/cycle-2/T*-audit.md and problems/cycle-2-t*/

notes:
  - SUCCESS-MEANINGFUL is explicitly blocked for T6.