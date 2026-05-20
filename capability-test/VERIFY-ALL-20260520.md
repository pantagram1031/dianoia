# Verify All Smoke

Date: 2026-05-20

Command:

```text
python tools\verify_all.py
```

Included checks:

- `python -m unittest discover -s tests`
- `python tools\verify_dianoia_state.py`
- `python tools\verify_phase_loop.py`

Result:

```text
Ran 3 tests
OK

SUMMARY ok=10 warn=5 fail=0
SUMMARY ok=18 fail=0
SUMMARY all verification commands passed
```

Known warning:

- B1-B5 token accounting remains `UNVERIFIED`. This is historical baseline
  debt; B6+ manifests must do better.
