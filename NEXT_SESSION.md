# Next Session

Resume the RESEARCH_CONTRIBUTION objective.

Immediate next step:
Continue P11 ATTEMPTS. P10 is complete; R020 attempt 1 produced
`PARTIAL-PROGRESS`, not a solved claim.

Recommended next work:
Continue `research-bank/R020/` no-three-in-line by replaying the remaining
Prellberg frontier certificates through `N=60` using
`tools/no_three_in_line_verify.py`. After replay coverage exists, choose one:

- run a bounded search/normalization experiment toward `N=61`, or
- switch to another rank A candidate (`R013` 1/3-2/3 posets or `R017`
  Graceful Tree Conjecture) if R020 search requires unavailable solver setup.

Current state:
- Active goal: RESEARCH_CONTRIBUTION. Do not mark complete unless a real
  contribution passes the configured gates or an honest ceiling condition is
  reached.
- P9 INFRA is complete.
- P10 CURATION is complete with 20 `OPEN-VERIFIED` candidates across 10 areas.
- P11 ATTEMPTS is in progress.
- R020 artifacts now include:
  - `tools/no_three_in_line_verify.py`
  - `tests/test_no_three_in_line_verify.py`
  - `research-bank/R020/certificates/prellberg-n47.json`
  - `research-bank/R020/certificates/prellberg-n47.verify.json`
  - `research-bank/R020/certificates/REPLAY.md`
  - `research-bank/R020/attempt-20260520/`
- `tools/verify_all.py` now runs the R020 `N=47` replay check.
- No `CLAIMS.md` row exists for R020 because no new mathematical result has
  been produced.

Operational reminders:
- Run `git fetch; git pull origin main --rebase` first.
- Read `ROADMAP.md`, `DEVLOG.md`, `RESEARCH_LOG.md`, and this file.
- Commit and push every logical unit.
- Run `python tools\verify_all.py` before final status; historical B1-B5 token
  accounting warnings are expected unless the verifier changes.
