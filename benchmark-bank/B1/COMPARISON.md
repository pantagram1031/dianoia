# B1 Comparison

## Verdict

VALUE_ADDED

## Raw Baseline

Path: `C:\Users\SAMSUNG\Downloads\raw-attempt-2`

Raw answer proves finiteness by citation:

```text
Finiteness: proved by citation to APSSV 2026 Theorem 6.1.
```

Raw blocks unsupported extras:

```text
Explicit bound: not supplied.
Small-case completeness: not supplied.
```

Raw admits missing machinery:

```text
The raw attempt does not create a claim ledger, reviewer files, or adversarial checks.
```

## Dianoia Run

Path: `C:\Users\SAMSUNG\Downloads\dianoia-run\problems\p3-sa-finiteness-apssv-2026`

Dianoia records fresh routing:

```text
- prior_active: fake-halted-p3-sa-20260520-182055
- route: prompts/prove.md
- new_slug: p3-sa-finiteness-apssv-2026
```

Dianoia records the endpoint bridge in the ledger:

```text
| C-003 | The set S_a in the user statement is the APSSV admissible set, with endpoint k=sqrt(n/a) harmless because n-a k^2=0 is not prime. | PROVED |
```

Dianoia blocks overclaim in result:

```text
No explicit bound in terms of a is proved in this run.
No complete lists for small a are proved in this run.
```

## Three Differences

1. Routing: dianoia proves the stale-active fix fired; raw has no equivalent
   machinery.
2. Bridge lemma: dianoia records a ledgered endpoint bridge; raw only states the
   citation applies.
3. Review discipline: dianoia records Reviewer D and consolidated review files;
   raw explicitly has no reviewer files or adversarial checks.
