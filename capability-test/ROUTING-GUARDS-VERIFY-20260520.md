# Routing Guard Verification - 2026-05-20

Purpose: prove local verification now checks stale `.active`, closed-active,
resume-only, and intake safety guard text rather than relying on informal
review.

Commands:

```powershell
python -m unittest discover -s tests -p test_verify_routing_guards.py
python tools\verify_routing_guards.py
python tools\verify_all.py
```

Observed targeted test output:

```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.059s

OK
```

Observed routing verifier output:

```text
OK AGENTS.md malformed active fresh-route guard contains required guard phrases
OK AGENTS.md contains closed active fresh-route guard
OK prove.md stale-active guard contains required guard phrases
OK resume.md contains BLOCKED-ITERATE-only guard
OK 00-intake.md closed active guard contains required guard phrases
SUMMARY ok=5 fail=0
```

Observed full verifier result:

```text
Ran 6 tests in 0.198s
SUMMARY ok=10 warn=5 fail=0
SUMMARY ok=18 fail=0
SUMMARY ok=5 fail=0
SUMMARY all verification commands passed
```

Known warnings:

- `tools\verify_dianoia_state.py` still reports B1-B5 token accounting as
  `UNVERIFIED`; this is expected legacy evidence, and B6+ rows are required to
  carry stronger run manifests.
