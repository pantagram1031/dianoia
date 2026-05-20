# BLOCKED_ON_USER

Date: 2026-05-20

## Blocker

Phase 2 cannot be honestly marked complete while DIAGNOSIS R1 remains unresolved.
R1 requires a routing change in `AGENTS.md`, which is constitutional under the
active goal and cannot be edited without user approval.

## Options

1. APPROVE: Allow the requested `AGENTS.md` routing guard in
   `APPROVED_CHANGES.md`, then continue Phase 2 and run the router-level smoke
   test.
2. DECLINE: Do not change `AGENTS.md`; accept prompt-level mitigations only.
   Phase 2 will remain UNVERIFIED at router level.
3. MODIFY: Provide a different routing rule for closed or malformed
   `problems/.active`.

## Recommended Choice

APPROVE.

Reason: the observed S_a failure occurred before `prompts/prove.md` fired, so
the durable fix belongs at the first-message routing boundary.
