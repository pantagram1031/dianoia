# Candidate Log

candidate_id: R020

## 2026-05-20 Curation

- Added to P10 bank as `OPEN-VERIFIED`.
- Area: discrete geometry.
- Initial rank: A.
- Initial attack surface: exact grid-point certificates, CSP replay, and
  variant-separated finite frontier work.

## 2026-05-20 P11 Attempt 1

- Verdict: `PARTIAL-PROGRESS`.
- Raw route: recorded `NO-PROGRESS` in
  `research-bank/R020/attempt-20260520/RAW.md`; it located the Prellberg
  source but produced no independent replay or new claim.
- Dianoia route: added `tools/no_three_in_line_verify.py`, unit tests, and a
  replayed `N=47` certificate from Prellberg's 2026 CSP table.
- Replay artifact:
  `research-bank/R020/certificates/prellberg-n47.verify.json` reports
  `ok: true`, `point_count: 94`, and no line violations.
- Claim discipline: no `CLAIMS.md` row added because this is published-source
  certificate replay, not a new result.
