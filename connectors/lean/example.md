# lean connector example

Command:

```powershell
python connectors/lean/server.py env
```

Expected shape:

```json
{
  "status": "OK | UNAVAILABLE | ERROR",
  "lean_path": "...",
  "message": "..."
}
```

When checking a file:

```powershell
python connectors/lean/server.py check notes\formalization\lemma.lean
```

If Lean is not installed locally, this returns `UNVERIFIED` rather than
pretending the formal check ran.
