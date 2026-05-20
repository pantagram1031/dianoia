# Connector Contract Verification - 2026-05-20

Purpose: verify dianoia connectors have deterministic offline contracts before
future benchmark rows rely on them for mathematical source lookup.

Commands:

```powershell
python -m unittest discover -s tests -p test_verify_connectors.py
python tools\verify_connectors.py
python tools\verify_all.py
```

Observed targeted test output:

```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.228s

OK
```

Observed connector verifier output:

```text
OK connectors/arxiv/README.md exists
OK connectors/arxiv/example.md exists
OK connectors/arxiv/server.py exists
OK connectors/arxiv/server.py exposes search/fetch JSON CLI contract
OK researcher.md invokes connectors/arxiv/server.py
OK connectors/oeis/README.md exists
OK connectors/oeis/example.md exists
OK connectors/oeis/server.py exists
OK connectors/oeis/server.py exposes search/fetch JSON CLI contract
OK researcher.md invokes connectors/oeis/server.py
SUMMARY ok=10 fail=0
```

Notes:

- This is an offline contract check. It compiles each wrapper, checks the
  `search`/`fetch` JSON CLI shape, checks documentation/example files, and
  checks researcher subagent invocation.
- Live network smoke tests remain separate so ordinary local verification is
  deterministic and not dependent on arXiv/OEIS availability.
