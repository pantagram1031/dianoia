# Phase 2 Smoke - AGENTS.md Router Guard

Date: 2026-05-20

Patch under test: approved constitutional routing guard in `AGENTS.md`.

## Scenario

1. Copied patched `AGENTS.md` into `C:\Users\SAMSUNG\Downloads\dianoia-run`.
2. Created fake active problem:

```text
fake-halted-router-20260520-181546
halt_flag: true
halt_reason: FAILURE-AMBITION-GAP
```

3. Set `dianoia-run/problems/.active` to the fake slug.
4. Simulated a non-command first user math statement.
5. Applied the new AGENTS route E2 rule.

## Verification Output

```json
{
  "fakeSlug": "fake-halted-router-20260520-181546",
  "route": "prompts/prove.md",
  "closedActiveDetected": true,
  "newSlug": "prove-that-for-fixed-positive-integer-a7f651",
  "activeEqualsNewSlug": true,
  "problemExists": true,
  "intakeExists": true,
  "oldJournalSupersession": true
}
```

## Evidence Paths

| condition | evidence |
|-----------|----------|
| fake halted active existed | `dianoia-run/problems/fake-halted-router-20260520-181546/session_state.md` |
| router selected prove.md | verification output field `"route": "prompts/prove.md"` |
| fresh slug created | `dianoia-run/problems/prove-that-for-fixed-positive-integer-a7f651/problem.md` |
| `.active` points to fresh slug | `dianoia-run/problems/.active` |
| intake written | `dianoia-run/problems/prove-that-for-fixed-positive-integer-a7f651/intake.md` |
| old journal supersession note | `dianoia-run/problems/fake-halted-router-20260520-181546/work_journal.md` |

## Verdict

PASS. DIAGNOSIS R1 is resolved at router level for the stale
`halt_flag=true` / `FAILURE-AMBITION-GAP` case that caused the S_a degraded
comparison.
