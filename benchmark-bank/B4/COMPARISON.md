# B4 Comparison

## Verdict

VALUE_ADDED

## Raw Baseline

Path: `C:\Users\SAMSUNG\Downloads\raw-attempt-5`

Raw answer overclaims:

```text
Verdict: YES.
```

Raw answer universalizes the model class:

```text
random matrix models with exploding moments satisfy a central limit theorem
```

Raw answer universalizes statistics:

```text
generally for arbitrary test functions.
```

## Dianoia Run

Path: `C:\Users\SAMSUNG\Downloads\dianoia-run\problems\b4-random-matrix-clt`

Dianoia researcher records exact scope:

```text
Theorem 2.6 proves a CLT for normalized traces of elliptic random matrices
satisfying Condition 2.1
```

Dianoia ledger rejects all-model scope:

```text
C-002 ... all random matrix models with exploding moments. | REJECTED
```

Dianoia ledger rejects arbitrary-test-function scope:

```text
C-003 ... arbitrary test functions. | REJECTED
```

## Machinery Audit

| item | raw | dianoia |
|------|-----|---------|
| exact theorem citation | DID_NOT_FIRE | FIRED: `inbox/u01/researcher/verified.md` |
| scope sanity check | DID_NOT_FIRE | FIRED: `sanity/scope-check.md` |
| claim ledger | DID_NOT_FIRE | FIRED: `claim_ledger.md` |
| adversarial citation review | DID_NOT_FIRE | FIRED: `reviews/reviewer-B.md` |

## Three Differences

1. Raw claims a universal CLT; dianoia restricts the claim to specified
   ensembles and theorem hypotheses.
2. Raw claims arbitrary test functions; dianoia records normalized
   trace/monomial-statistic scope.
3. Raw uses abstract-level support; dianoia uses exact theorem citation, ledger,
   sanity check, and reviewer defect.
