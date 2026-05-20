# Phase 2 Smoke - prove.md Stale Active Guard

Date: 2026-05-20

Patch under test: `prompts/prove.md` stale-active/closed-active handling.

## Required Scenario

Create `problems/.active` pointing to a fake problem with:

```text
halt_flag: true
halt_reason: FAILURE-AMBITION-GAP
```

Then simulate a first user math statement routed through the patched
`prompts/prove.md` contract.

## First Attempt

An initial smoke attempt created a fresh slug and `intake.md`, but PowerShell
reported template-copy errors. That attempt is not counted as clean.

## Clean Attempt

Workspace: `C:\Users\SAMSUNG\Downloads\dianoia-run`

Fresh user statement:

```text
Prove that for fixed positive integer a, the set S_a is finite. Smoke stamp 20260520-180641.
```

Observed verification output:

```json
{
  "fakeSlug": "fake-halted-smoke-clean-20260520-180641",
  "newSlug": "prove-that-for-fixed-positive-integer-2579e5",
  "activeEqualsNewSlug": true,
  "newProblemExists": true,
  "intakeExists": true,
  "oldJournalSupersession": true
}
```

## Evidence Paths

| condition | evidence |
|-----------|----------|
| fake halted active existed | `dianoia-run/problems/fake-halted-smoke-clean-20260520-180641/session_state.md` |
| fresh slug created | `dianoia-run/problems/prove-that-for-fixed-positive-integer-2579e5/problem.md` |
| `.active` points to fresh slug | `dianoia-run/problems/.active` |
| intake written | `dianoia-run/problems/prove-that-for-fixed-positive-integer-2579e5/intake.md` |
| closed old journal not polluted silently | `dianoia-run/problems/fake-halted-smoke-clean-20260520-180641/work_journal.md` contains a supersession note |

## Verdict

PASS for the prompt-level R2 success criterion: direct `prove.md` invocation
under stale `halt_flag=true` active state creates a fresh slug and writes
`intake.md`.

UNVERIFIED for the AGENTS-level R1 success criterion: `AGENTS.md` is
constitutional and was not changed in this patch, so this smoke does not prove
that first-message routing itself will always invoke `prove.md`.
