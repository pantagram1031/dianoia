# lean connector

Purpose: local Lean availability and file-check wrapper for dianoia research
verification gates.

## Capabilities

- Report whether a `lean` executable is available on `PATH`.
- Run `lean <file>` on a provided `.lean` file when Lean is installed.
- Emit compact JSON with `VERIFIED`, `FAILED`, `UNVERIFIED`, or `UNAVAILABLE`
  status.

## Usage

```powershell
python connectors/lean/server.py env
python connectors/lean/server.py check path\to\lemma.lean
```

## Contract

This connector never upgrades a mathematical claim by itself. It only records
whether a local Lean file was checked. If Lean is unavailable, the output is
`UNVERIFIED`, and the claim must either use another verification route or remain
below the P12 confidence gate.

