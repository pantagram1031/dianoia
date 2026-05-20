# Candidate Log

candidate_id: R013

## 2026-05-20 Curation

- Added to P10 bank as `OPEN-VERIFIED`.
- Area: order theory.
- Initial rank: A.
- Initial attack surface: exact linear-extension counting and finite
  small-poset certificate replay.

## 2026-05-20 P11 Attempt 1

- Verdict: `PARTIAL-PROGRESS`.
- Raw route: recorded `NO-PROGRESS` in
  `research-bank/R013/attempt-20260520/RAW.md`; it restated the conjecture but
  produced no exact reusable artifact.
- Dianoia route: added `tools/poset_balance.py`, unit tests, and an exact
  exhaustive labeled-poset check through five elements.
- Replay artifact:
  `research-bank/R013/attempt-20260520/small-posets-n5.json` reports
  `counterexample_count: 0` across all non-chain labeled posets for
  `2 <= n <= 5`.
- Claim discipline: no `CLAIMS.md` row added because this is a small-case
  sanity baseline and verification gate, not a novel result.
