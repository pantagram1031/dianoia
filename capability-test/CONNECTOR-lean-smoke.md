# Lean Connector Smoke

Command:

```powershell
python connectors\lean\server.py env
```

Expected result:

- `status: OK` when Lean is installed and on `PATH`.
- `status: UNAVAILABLE` when Lean is not installed.

The important invariant is honesty: unavailable Lean is reported as
`UNAVAILABLE`/`UNVERIFIED`, never as a successful formal check.
