# R020 Certificate Replay: Prellberg and Flammenkamp Frontier

candidate_id: R020
date: 2026-05-20
status: VERIFIED-REPLAY

## Source

- Paper: Thomas Prellberg, "Constraint Satisfaction Programming for the
  No-three-in-line Problem", arXiv:2602.07751.
- Prellberg source file: https://raw.githubusercontent.com/ThomasPrellberg/no-three-in-line---CP-SAT/main/Table%201.txt
- Entries replayed from this table: `N=47`, `N=49`, `N=51`, and
  `N=53` through `N=60`.
- Flammenkamp source page: https://wwwhomes.uni-bielefeld.de/achim/no3in/readme.html
- Flammenkamp encoded files replayed: `n48_rot4`, `n50_rot4`, and `n52_rot4`
  from https://wwwhomes.uni-bielefeld.de/~achim/no3in/download/configurations/
- Source SHA-256 of downloaded `Table 1.txt`:
  `6769b67a863590a1c777114e08a2e8057876c6d1d1cd4e2334014b4efe35ddeb`
- Flammenkamp source SHA-256 values are recorded in each generated
  `flammenkamp-n*.json` certificate.

## Local Artifacts

- Source table snapshot: `research-bank/R020/certificates/prellberg-table1.txt`
- Encoded Flammenkamp snapshots:
  `research-bank/R020/certificates/flammenkamp-n48_rot4.txt`,
  `research-bank/R020/certificates/flammenkamp-n50_rot4.txt`, and
  `research-bank/R020/certificates/flammenkamp-n52_rot4.txt`
- Certificates:
  `research-bank/R020/certificates/prellberg-n*.json` and
  `research-bank/R020/certificates/flammenkamp-n*.json`
- Per-certificate verifier outputs:
  `research-bank/R020/certificates/*.verify.json`
- Batch summary:
  `research-bank/R020/certificates/prellberg-frontier-summary.json`
- Verifier: `tools/no_three_in_line_verify.py`
- Batch replay harness: `tools/no_three_in_line_frontier.py`

## Replay Command

```powershell
python tools\no_three_in_line_frontier.py verify-dir `
  research-bank\R020\certificates
```

## Replay Result

The batch verifier returned `ok: true` for all 14 replayed certificates.
The summary records the following `(N, point_count)` pairs:

`(47, 94)`, `(48, 96)`, `(49, 98)`, `(50, 100)`, `(51, 102)`,
`(52, 104)`, `(53, 106)`, `(54, 108)`, `(55, 110)`, `(56, 112)`,
`(57, 114)`, `(58, 116)`, `(59, 118)`, and `(60, 120)`.

## Interpretation

This is not a new mathematical contribution and does not affect `CLAIMS.md`.
It is P11 setup evidence: dianoia now has a solver-independent replay path for
published no-three-in-line certificates across every `N=47` through `N=60`.
The next R020 step must be an actual mathematical attempt, not more replay:

- run a bounded search/normalization experiment for a frontier extension or
  obstruction, with this verifier as the acceptance gate; or
- switch to another rank A candidate if R020 requires unavailable solver
  machinery rather than dianoia-level mathematical work.
