# R020 Dianoia Attempt

date: 2026-05-20
mode: verifier-backed P11 attempt
verdict: PARTIAL-PROGRESS

## Problem

Make progress on the no-three-in-line problem through a replayable certificate
pipeline before making any new search or proof claim.

## Work Performed

1. Added `tools/no_three_in_line_verify.py`, a solver-independent checker for
   finite grid certificates.
2. Added unit coverage in `tests/test_no_three_in_line_verify.py` for valid
   certificates, collinearity failures, duplicate/out-of-bounds points, and
   certificate parsing.
3. Extracted the `N=47` certificate from Prellberg's public `Table 1.txt` into
   `research-bank/R020/certificates/prellberg-n47.json`.
4. Replayed it with the local verifier using `--require-2n`,
   `--require-two-per-row`, and `--require-two-per-column`.
5. Wired the replay command into `tools/verify_all.py`.

## Verification

Replay command:

```powershell
python tools\no_three_in_line_verify.py `
  research-bank\R020\certificates\prellberg-n47.json `
  --require-2n `
  --require-two-per-row `
  --require-two-per-column
```

Replay output:

```json
{
  "errors": [],
  "grid_size": 47,
  "line_violations": [],
  "ok": true,
  "point_count": 94
}
```

Full verification command:

```powershell
python tools\verify_all.py
```

The full verifier now includes the R020 `N=47` replay check.

## Outcome

`PARTIAL-PROGRESS`. This is a verified replay and infrastructure result, not a
new mathematical contribution. It lowers the cost of future R020 attempts by
giving dianoia an exact acceptance gate for certificate search or replay
through the current frontier.
