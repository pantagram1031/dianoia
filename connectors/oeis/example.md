# oeis connector example

Command:

```powershell
python connectors/oeis/server.py fetch A214583
```

Expected use by researcher subagent:

1. Fetch OEIS metadata for candidate sequence evidence.
2. Record sequence name, data, comments, and references in the subagent drop
   zone.
3. Treat the sequence as computational/reference evidence unless a proof source
   is separately verified.
