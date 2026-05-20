# Claim Verification Gate

candidate_id:
claim_id:
gate_status: PENDING | PASSED | DOWNGRADED | BLOCKED_EXTERNAL_REVIEW

## Gate Checklist

- openness verification:
- adversarial novelty check:
- Reviewer D attacks:
- computation evidence:
- formal verification:
- confidence 1-10:

## Evidence Paths

- SOURCE.md:
- OPENNESS.md:
- TRACTABILITY.md:
- log.md:
- NOVELTY.md:
- formal/computation:
- draft note:

## Downgrade Conditions

Downgrade to `PARTIAL-PROGRESS` if confidence is below 8, any required gate
fails, or a key verification step is `UNVERIFIED` without a narrow rationale.

## External Review Halt

If every gate passes and confidence is at least 8, update `CLAIMS.md` to
`BLOCKED-EXTERNAL-REVIEW`, write `QUESTIONS.md`, and halt for user-mediated
external mathematician review.
