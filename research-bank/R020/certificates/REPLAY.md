# R020 Certificate Replay: Prellberg N=47

candidate_id: R020
date: 2026-05-20
status: VERIFIED-REPLAY

## Source

- Paper: Thomas Prellberg, "Constraint Satisfaction Programming for the
  No-three-in-line Problem", arXiv:2602.07751.
- Source file: https://raw.githubusercontent.com/ThomasPrellberg/no-three-in-line---CP-SAT/main/Table%201.txt
- Entry replayed: `N=47`.
- Source SHA-256 of downloaded `Table 1.txt`:
  `723d0d85029562fa08990a3b27f55e4b9e696458e56b89b572d77b9f25e236ba`

## Local Artifacts

- Certificate: `research-bank/R020/certificates/prellberg-n47.json`
- Verifier output: `research-bank/R020/certificates/prellberg-n47.verify.json`
- Verifier: `tools/no_three_in_line_verify.py`

## Replay Command

```powershell
python tools\no_three_in_line_verify.py `
  research-bank\R020\certificates\prellberg-n47.json `
  --require-2n `
  --require-two-per-row `
  --require-two-per-column
```

## Replay Result

The verifier returned:

```json
{
  "errors": [],
  "grid_size": 47,
  "line_violations": [],
  "ok": true,
  "point_count": 94
}
```

## Interpretation

This is not a new mathematical contribution and does not affect `CLAIMS.md`.
It is P11 setup evidence: dianoia now has a solver-independent replay path for
published no-three-in-line certificates. The next R020 step is to use this
verifier as the acceptance gate for either:

- replaying additional frontier certificates through `N=60`, or
- running a bounded search for a new certificate or obstruction with exact
  replay output.
