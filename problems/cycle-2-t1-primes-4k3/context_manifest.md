# Context Manifest

unit_id: halt-success
phase: 6
phase_prompt: prompts/06-consolidate.md
timestamp: 2026-05-20T06:30:00+09:00
always:
  - IDENTITY.md
  - goal.md
  - AGENTS.md
  - problems/cycle-2-t1-primes-4k3/session_state.md
  - problems/cycle-2-t1-primes-4k3/claim_ledger.md
phase_active:
  artifact: problems/cycle-2-t1-primes-4k3/result.md
  prompt: prompts/06-consolidate.md
  required_inputs: [claim_ledger.md, proofs/primes-4k3.fml, corpus/theorems/t1primes4k3.fml]
  produced_outputs: [result.md, result.fml, executive_summary.md]
this_unit:
  artifacts_written: [result.md, result.fml, executive_summary.md]
  artifacts_reviewed: [result.md]
  reviewer_files: [reviews/consolidate-reviewer-A.md, reviews/consolidate-reviewer-B.md, reviews/consolidate-reviewer-C.md, reviews/consolidate-reviewer-D.md]
  subagent_returns: none
  journal_fragments_merged: none
  ledger_delta: none
  open_markers: none
checkpoint_evidence:
  forbidden_word_scan: none
  citation_check: C-001 present
  review_status: PASS
  next_atomic_unit: none
dropped: []
