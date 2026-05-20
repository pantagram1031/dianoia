# Phase 2 Smoke - resume.md and 00-intake.md Active Guards

Date: 2026-05-20

Patch under test:
- `prompts/resume.md` malformed `.active` and fresh-problem boundary.
- `prompts/00-intake.md` malformed/missing/closed active failures.

## Checks

1. Wrote a malformed two-line `problems/.active` in `dianoia-run`.
2. Confirmed the malformed pointer condition is detectable before any phase uses it.
3. Replaced `.active` with a fake halted problem:

```text
halt_flag: true
halt_reason: FAILURE-AMBITION-GAP
```

4. Simulated a fresh problem statement through the patched `prove.md` contract
   after the resume/intake guard patch.

## Verification Output

```json
{
  "malformedActiveDetected": true,
  "fakeSlug": "fake-halted-smoke-resume-intake-20260520-180907",
  "newSlug": "prove-that-the-s-a-set-4cb341",
  "activeEqualsNewSlug": true,
  "intakeExists": true,
  "oldJournalSupersession": true
}
```

## Evidence Paths

| condition | evidence |
|-----------|----------|
| fake halted active existed | `dianoia-run/problems/fake-halted-smoke-resume-intake-20260520-180907/session_state.md` |
| fresh slug created | `dianoia-run/problems/prove-that-the-s-a-set-4cb341/problem.md` |
| `.active` points to fresh slug | `dianoia-run/problems/.active` |
| intake written | `dianoia-run/problems/prove-that-the-s-a-set-4cb341/intake.md` |
| old journal supersession note | `dianoia-run/problems/fake-halted-smoke-resume-intake-20260520-180907/work_journal.md` |

## Verdict

PASS for the prompt-level R3/R4 guard patch.

UNVERIFIED for the AGENTS-level R1 route-selection problem. That remains a
constitutional routing issue unless a later smoke demonstrates that the
first-message router deterministically invokes `prompts/prove.md` for fresh
problem statements under closed stale active state.
