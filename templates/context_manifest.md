# Context Manifest

unit_id:
phase:
timestamp:

always:
  - IDENTITY.md
  - goal.md
  - AGENTS.md
  - problems/<slug>/session_state.md
  - problems/<slug>/claim_ledger.md

phase_active:
  - <phase prompt>
  - <current phase artifact>

this_unit:
  - <artifact written or reviewed in this atomic unit>
  - <inbox fragments merged in this atomic unit>

dropped:
  - path: <path or summary id>
    reason: <why it is safe to omit from immediate context>
    recovery: <where to reload or summarize it from>

notes:
  - <context compression, head/tail summary, or starve-mode note>
