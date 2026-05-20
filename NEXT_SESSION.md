# Next Session

Resume the RESEARCH_CONTRIBUTION objective.

Immediate next step:
Continue P11 ATTEMPTS. P10 is complete; R020 and R013 have produced
`PARTIAL-PROGRESS`, not solved claims.

Recommended next work:
Do not keep expanding replay as a substitute for mathematics. Choose one:

- continue `R013` by extracting a structural lemma candidate from
  `STRUCTURAL_NOTES.md`, adding width/thinness filters, or speeding up
  canonical generation before attempting `n=7`; or
- return to `R020` only for bounded search/proof work accepted by the verifier,
  not for more source-format replay; or
- switch to `R017` Graceful Tree Conjecture if both R013 and R020 become mostly
  solver engineering.

Current state:
- Active goal: RESEARCH_CONTRIBUTION. Do not mark complete unless a real
  contribution passes the configured gates or an honest ceiling condition is
  reached.
- P9 INFRA is complete.
- P10 CURATION is complete with 20 `OPEN-VERIFIED` candidates across 10 areas.
- P11 ATTEMPTS is in progress.
- R020 artifacts now include:
  - `tools/no_three_in_line_verify.py`
  - `tools/no_three_in_line_frontier.py`
  - `tests/test_no_three_in_line_verify.py`
  - `tests/test_no_three_in_line_frontier.py`
  - `research-bank/R020/certificates/prellberg-table1.txt`
  - `research-bank/R020/certificates/prellberg-frontier-summary.json`
  - table-derived certificates and verification JSON for `N=47`, `N=49`,
    `N=51`, and `N=53` through `N=60`
  - Flammenkamp source snapshots, certificates, and verification JSON for
    `N=48`, `N=50`, and `N=52`
  - `research-bank/R020/attempt-20260520/`
- `tools/verify_all.py` now runs:
  `python tools/no_three_in_line_frontier.py verify-dir research-bank/R020/certificates`.
- R013 artifacts now include:
  - `tools/poset_balance.py`
  - `tests/test_poset_balance.py`
  - `research-bank/R013/attempt-20260520/RAW.md`
  - `research-bank/R013/attempt-20260520/DIANOIA.md`
  - `research-bank/R013/attempt-20260520/VERDICT.md`
  - `research-bank/R013/attempt-20260520/small-posets-n5.json`
  - `research-bank/R013/attempt-20260520/unlabeled-posets-n5.json`
  - `research-bank/R013/attempt-20260520/unlabeled-posets-n6.json`
  - `research-bank/R013/attempt-20260520/STRUCTURAL_NOTES.md`
  - `tools/verify_all.py` runs `python tools/poset_balance.py exhaustive-small --max-n 5`
    and `python tools/poset_balance.py exhaustive-unlabeled --max-n 5`.
- No `CLAIMS.md` row exists for R020 because no new mathematical result has
  been produced. No `CLAIMS.md` row exists for R013 for the same reason.

Operational reminders:
- Run `git fetch; git pull origin main --rebase` first.
- Read `ROADMAP.md`, `DEVLOG.md`, `RESEARCH_LOG.md`, and this file.
- Commit and push every logical unit.
- Run `python tools\verify_all.py` before final status; historical B1-B5 token
  accounting warnings are expected unless the verifier changes.
