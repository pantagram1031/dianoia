# Context Manifest

unit_id:
phase:
phase_prompt:
timestamp:

always:
  - IDENTITY.md
  - goal.md
  - AGENTS.md
  - problems/<slug>/session_state.md
  - problems/<slug>/claim_ledger.md

phase_active:
  artifact:
  prompt:
  required_inputs: []
  produced_outputs: []

this_unit:
  artifacts_written: []
  artifacts_reviewed: []
  reviewer_files: []
  subagent_returns: []
  journal_fragments_merged: []
  ledger_delta: []
  open_markers: []

checkpoint_evidence:
  forbidden_word_scan:
  citation_check:
  review_status:
  next_atomic_unit:

dropped:
  - path: <path or summary id>
    reason: <why it is safe to omit from immediate context>
    recovery: <where to reload or summarize it from>

notes:
  - <context compression, head/tail summary, or starve-mode note>