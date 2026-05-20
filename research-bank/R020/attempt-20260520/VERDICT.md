# R020 P11 Attempt Verdict

date: 2026-05-20
candidate_id: R020
verdict: PARTIAL-PROGRESS
claim_status: NO_SOLVED_CLAIM

## Summary

The attempt did not solve the no-three-in-line problem, improve a published
bound, or produce a new certificate. It did produce a replayable verifier and
validated one published frontier certificate (`N=47`) from Prellberg's 2026 CSP
work.

## Evidence

1. Verifier exists: `tools/no_three_in_line_verify.py`.
2. Tests exist and passed: `tests/test_no_three_in_line_verify.py`.
3. Replayed certificate: `research-bank/R020/certificates/prellberg-n47.json`.
4. Replay output: `research-bank/R020/certificates/prellberg-n47.verify.json`
   with `ok: true`, `point_count: 94`, and no line violations.
5. Full verification: `tools/verify_all.py` now runs the R020 replay command.

## Why This Is Not A Claim

- The certificate is published-source replay, not new mathematics.
- No `CLAIMS.md` row is warranted.
- No P12 solved-claim gate is triggered.
- The next honest step is more replay or bounded search, not external review.

## Next Step

Use the verifier to replay the remaining Prellberg frontier certificates
through `N=60`, then attempt a bounded search or certificate-normalization
improvement with exact artifacts.
