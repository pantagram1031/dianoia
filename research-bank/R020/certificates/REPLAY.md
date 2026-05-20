# R020 Certificate Replay: Prellberg Table 1

candidate_id: R020
date: 2026-05-20
status: VERIFIED-REPLAY

## Source

- Paper: Thomas Prellberg, "Constraint Satisfaction Programming for the
  No-three-in-line Problem", arXiv:2602.07751.
- Source file: https://raw.githubusercontent.com/ThomasPrellberg/no-three-in-line---CP-SAT/main/Table%201.txt
- Entries replayed from this table: `N=47`, `N=49`, `N=51`, and
  `N=53` through `N=60`.
- Entries not in this table: `N=48`, `N=50`, and `N=52`; the source says those
  are available from Flammenkamp's earlier page.
- Source SHA-256 of downloaded `Table 1.txt`:
  `6769b67a863590a1c777114e08a2e8057876c6d1d1cd4e2334014b4efe35ddeb`

## Local Artifacts

- Source table snapshot: `research-bank/R020/certificates/prellberg-table1.txt`
- Certificates: `research-bank/R020/certificates/prellberg-n*.json`
- Per-certificate verifier outputs:
  `research-bank/R020/certificates/prellberg-n*.verify.json`
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

The batch verifier returned `ok: true` for all 11 table-derived certificates.
The summary records the following `(N, point_count)` pairs:

`(47, 94)`, `(49, 98)`, `(51, 102)`, `(53, 106)`, `(54, 108)`,
`(55, 110)`, `(56, 112)`, `(57, 114)`, `(58, 116)`, `(59, 118)`,
and `(60, 120)`.

## Interpretation

This is not a new mathematical contribution and does not affect `CLAIMS.md`.
It is P11 setup evidence: dianoia now has a solver-independent replay path for
published no-three-in-line certificates. The next R020 step is to fill the
Flammenkamp-sourced `N=48`, `N=50`, and `N=52` replay gap or use this verifier
as the acceptance gate for:

- running a bounded search for a new certificate or obstruction with exact
  replay output.
