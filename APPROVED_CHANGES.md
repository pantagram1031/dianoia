# Approved Changes Request

Date: 2026-05-20

Status: PENDING USER APPROVAL

## Constitutional File

`AGENTS.md`

## Why This Is Needed

Phase 0 and Phase 1 show that the prior S_a comparison failed at the
first-message routing boundary. A stale closed `problems/.active` pointed to
`cycle-4-t6-perfect-numbers`, and the fresh S_a problem statement was appended
to the closed problem's `work_journal.md` instead of invoking
`prompts/prove.md`.

Prompt-level guards now exist in:

- `prompts/prove.md`
- `prompts/resume.md`
- `prompts/00-intake.md`

But DIAGNOSIS R1 remains unresolved because `AGENTS.md` still contains no
closed-active guard before the active-unit fallback.

## Requested Edit

Modify the first-message routing section of `AGENTS.md` so that before route F
("Otherwise -> input to active unit or clarification"), the router checks the
active problem state.

Proposed rule:

```text
Before route F, if problems/.active exists, read
problems/<slug>/session_state.md. If halt_flag=true and halt_reason is
SUCCESS-MEANINGFUL, FAILURE-AMBITION-GAP, or any reason other than
BLOCKED-ITERATE, then a non-command user message is treated as a fresh problem
statement and routed to prompts/prove.md with the message as $1. Do not append
fresh problem content to the closed active problem.
```

Also add:

```text
If problems/.active is malformed, missing its slug directory, or missing
session_state.md, then a non-command user message is treated as a fresh problem
statement and routed to prompts/prove.md. The stale pointer is superseded by
prove.md.
```

## Success Criterion

The Phase 2 smoke test passes at router level:

1. Create a fake active problem with `halt_flag=true` and
   `halt_reason=FAILURE-AMBITION-GAP`.
2. Set `problems/.active` to that fake slug.
3. Simulate a first user math statement.
4. Confirm the router invokes `prompts/prove.md`, creates a fresh slug, writes
   `problem.md`, writes `intake.md`, updates `.active`, and leaves a
   supersession note rather than appending math content to the old closed
   problem.
