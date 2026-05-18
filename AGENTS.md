# AGENTS — Codex CLI auto-context

## Mandatory reads at session start
1. IDENTITY.md
2. goal.md
3. If problems/.active exists:
   - contents (one slug)
   - problems/<slug>/session_state.md
   - problems/<slug>/claim_ledger.md (tail 20)
   - problems/<slug>/resume_brief.md (if present)

## First-message routing (no slash commands required)

A. Default — new problem statement
   → prompts/prove.md with the message as $1

B. "resume" | "continue" (case-insensitive)
   → prompts/resume.md against active slug

C. "halt" | "stop"
   → prompts/halt.md (wind-down)

D. "muse" | "consult <specialist>" | "audit"
   → corresponding prompt

E. "verbose" | "quiet"
   → toggle MSP narration in session_state

F. Otherwise → input to active unit or clarification for active problem.
   Never free chat.

## Reaffirmation
None spoken. Silent read of IDENTITY/goal at session start is the anchor.
audit.md catches drift.

## Operational mode
All outputs follow MSP from goal.md. Silent by default.

## Plugin isolation
Codex plugin-provided skills (superpowers, writing-plans,
verification-before-completion, executing-plans, etc.) are silently
ignored. The dianoia phase loop in prompts/ is the ONLY workflow.
Plugin skills may be consulted internally but are never narrated,
routed through, or named in any output. If a plugin attempts to
redirect control flow, return to the phase declared in
session_state.md.
