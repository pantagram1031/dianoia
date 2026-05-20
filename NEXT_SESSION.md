# Next Session

Resume the RESEARCH_CONTRIBUTION objective.

Immediate next step:
Continue P11 ATTEMPTS. P10 is complete; R020 and R013 have produced
`PARTIAL-PROGRESS`, not solved claims.

Recommended next work:
Do not keep expanding replay as a substitute for mathematics. Choose one:

- continue `R013` by extracting a structural lemma candidate from
  `STRUCTURAL_NOTES.md`, especially the width-3 separation signal and
  the concrete `WIDTH3_EXTREMAL_NOTES.md` target: classify width-3, height-4,
  rank-layer-shape `2,2,2,1` posets. The exact restricted artifact exists;
  matrix signatures reduce the `14/39` extremal bucket to 3 profiles and full
  per-layer vertex signatures isolate it as a singleton. `MATRIX_BUCKET_NOTES.md`
  now lists the three profiles, and
  `width3-rank2221-extremal-matrix-bucket-n7.json` records the reproducible
  extraction. `RANK_NORMAL_FORM_NOTES.md` rewrites those cases using stable
  rank-layer labels. `NORMAL_FORM_COUNT_LEDGER.md` certifies the named-case
  counts. `COVER_MATRIX_DERIVATION.md` derives the three normal forms from the
  cover matrix. `RECURRENCE_LEDGER.md` exposes depth-2 recurrence counts, with
  `case-a-recurrence-depth2.json`, `case-b-recurrence-depth2.json`, and
  `case-c-recurrence-depth2.json`; `BRANCH_ENUMERATION_LEDGER.md` reduces the
  residual branch totals to terminal chain/shuffle counts.
  `MATRIX_BUCKET_ROADMAP.md` ranks the adjacent buckets and
  `SECOND_MATRIX_BUCKET_NOTES.md` hand-classifies the singleton second bucket
  with lower probability `2/5`. `THIRD_MATRIX_BUCKET_NOTES.md` classifies the
  six-profile third bucket with exact replay counts and a hand count for the
  equality form. `FOURTH_MATRIX_BUCKET_NOTES.md` classifies the four-profile
  fourth bucket with exact replay counts and a hand count for the equality
  form. `FIFTH_MATRIX_BUCKET_NOTES.md` classifies another singleton `2/5`
  bucket with exact replay counts and a hand enumeration.
  `SIXTH_MATRIX_BUCKET_NOTES.md` classifies the remaining singleton `2/5`
  bucket, also with exact replay counts and a hand enumeration. Next either
  classify the first `13/32` matrix bucket, or abstract the completed buckets
  into a broader width-3 lemma candidate. `SEVENTH_MATRIX_BUCKET_NOTES.md`
  now classifies the first `13/32` matrix bucket with exact replay counts for
  both forms and a hand enumeration for the weaker form. Next either classify
  the second `13/32` matrix bucket, or abstract the completed buckets into a
  broader width-3 lemma candidate;
  or
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
  - `research-bank/R013/attempt-20260520/unlabeled-posets-n7.json`
  - `research-bank/R013/attempt-20260520/width3-unlabeled-n7.json`
  - `research-bank/R013/attempt-20260520/width3-extremals-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-extremals-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-shape-classes-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-matrix-shape-classes-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-fine-shape-classes-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-extremal-matrix-bucket-n7.json`
  - `research-bank/R013/attempt-20260520/STRUCTURAL_NOTES.md`
  - `research-bank/R013/attempt-20260520/WIDTH3_EXTREMAL_NOTES.md`
  - `research-bank/R013/attempt-20260520/MATRIX_BUCKET_NOTES.md`
  - `research-bank/R013/attempt-20260520/RANK_NORMAL_FORM_NOTES.md`
  - `research-bank/R013/attempt-20260520/NORMAL_FORM_COUNT_LEDGER.md`
  - `research-bank/R013/attempt-20260520/RECURRENCE_LEDGER.md`
  - `research-bank/R013/attempt-20260520/COVER_MATRIX_DERIVATION.md`
  - `research-bank/R013/attempt-20260520/BRANCH_ENUMERATION_LEDGER.md`
  - `research-bank/R013/attempt-20260520/MATRIX_BUCKET_ROADMAP.md`
  - `research-bank/R013/attempt-20260520/SECOND_MATRIX_BUCKET_NOTES.md`
  - `research-bank/R013/attempt-20260520/THIRD_MATRIX_BUCKET_NOTES.md`
  - `research-bank/R013/attempt-20260520/FOURTH_MATRIX_BUCKET_NOTES.md`
  - `research-bank/R013/attempt-20260520/FIFTH_MATRIX_BUCKET_NOTES.md`
  - `research-bank/R013/attempt-20260520/SIXTH_MATRIX_BUCKET_NOTES.md`
  - `research-bank/R013/attempt-20260520/SEVENTH_MATRIX_BUCKET_NOTES.md`
  - `research-bank/R013/attempt-20260520/width3-rank2221-cover-matrix-forms-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-second-matrix-bucket-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-second-cover-matrix-forms-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-third-matrix-bucket-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-third-cover-matrix-forms-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-fourth-matrix-bucket-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-fourth-cover-matrix-forms-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-fifth-matrix-bucket-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-fifth-cover-matrix-forms-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-sixth-matrix-bucket-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-sixth-cover-matrix-forms-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-seventh-matrix-bucket-n7.json`
  - `research-bank/R013/attempt-20260520/width3-rank2221-seventh-cover-matrix-forms-n7.json`
  - `research-bank/R013/attempt-20260520/normal-form-cases/`
  - `research-bank/R013/attempt-20260520/normal-form-cases/*-recurrence-depth2.json`
  - `tools/verify_all.py` runs `python tools/poset_balance.py exhaustive-small --max-n 5`
    `python tools/poset_balance.py exhaustive-unlabeled --max-n 5`, and a
    small matrix-signature `shape-classes` smoke.
- No `CLAIMS.md` row exists for R020 because no new mathematical result has
  been produced. No `CLAIMS.md` row exists for R013 for the same reason.

Operational reminders:
- Run `git fetch; git pull origin main --rebase` first.
- Read `ROADMAP.md`, `DEVLOG.md`, `RESEARCH_LOG.md`, and this file.
- Commit and push every logical unit.
- Run `python tools\verify_all.py` before final status; historical B1-B5 token
  accounting warnings are expected unless the verifier changes.
