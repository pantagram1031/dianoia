# Connector Smoke - oeis

Date: 2026-05-20

Command:

```powershell
python connectors/oeis/server.py fetch A214583
```

Result: PASS.

Key output fields:

```json
{
  "id": "A214583",
  "name": "Numbers m such that for all k with gcd(m, k) = 1 and m > k^2, m - k^2 is prime.",
  "data": "3,4,6,8,12,14,18,20,24,30,32,38,42,48,54,60,62,68,72,80,84,90,98,108,110,132,138,140,150,180,182,198,252,318,360,398,468,570,572,930,1722",
  "url": "https://oeis.org/A214583"
}
```

Connector status: working for OEIS sequence fetch of the S_a-adjacent source.
