# B5 Comparison

## Verdict

VALUE_ADDED

## Raw Baseline

Path: `C:\Users\SAMSUNG\Downloads\raw-attempt-6`

Raw answer overclaims:

```text
Verdict: YES.
```

Raw answer erases the hypothesis:

```text
No extra hypothesis on H is needed beyond being finite.
```

Raw audit records the missing exact reference:

```text
No exact theorem or corollary number was cited.
```

## Dianoia Run

Path: `C:\Users\SAMSUNG\Downloads\dianoia-run\problems\b5-center-preserving-representations`

Dianoia researcher preserves the theorem hypothesis:

```text
Theorem 1.2 is conditional on H having a faithful irreducible representation rho.
```

Dianoia ledger rejects the universal claim:

```text
C-003 ... Every finite H <= G has such a representation ... REJECTED
```

Dianoia result states the corrected answer:

```text
conditional/iff theorem for eligible finite groups H, not a universal theorem
for all finite subgroups.
```

## Machinery Audit

| item | raw | dianoia |
|------|-----|---------|
| exact theorem/corollary citation | DID_NOT_FIRE | FIRED: `inbox/u01/researcher/verified.md` |
| quantifier sanity check | DID_NOT_FIRE | FIRED: `sanity/quantifier-check.md` |
| claim ledger | DID_NOT_FIRE | FIRED: `claim_ledger.md` |
| adversarial citation review | DID_NOT_FIRE | FIRED: `reviews/reviewer-B.md` |

## Three Differences

1. Raw makes the result universal for all finite H; dianoia keeps the faithful
   irreducible representation prerequisite.
2. Raw cites no exact theorem; dianoia records Theorem 1.2 and Corollary 1.3.
3. Raw has no review or ledger; dianoia records the rejected overclaim,
   quantifier sanity check, and reviewer defect.
