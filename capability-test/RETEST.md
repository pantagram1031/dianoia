# Phase 3 - S_a Retest

Date: 2026-05-20

## Protocol

Problem:

```text
For fixed positive integer a, prove that S_a = { n > 0 : for every integer k with 1 <= k <= sqrt(n/a) and gcd(k,n)=1, n - a*k^2 is prime } is finite. Also state whether an explicit bound or complete small-a lists are proved.
```

Source:

- Boris Alexeev; Moe Putterman; Mehtaab Sawhney; Mark Sellke; Gregory Valiant,
  2026, "Short proofs in combinatorics, probability and number theory II",
  arXiv:2604.06609, Section 6 Theorem 6.1 / arXiv abstract finiteness theorem.
- Official arXiv metadata: submitted 2026-04-08; abstract says the paper
  includes a finiteness theorem for integers `n` such that `n-a k^2` is prime
  for all admissible coprime `k`.

## Artifacts

| branch | path | notes |
|--------|------|-------|
| raw baseline | `C:\Users\SAMSUNG\Downloads\raw-attempt-2` | fresh direct answer; no phase loop |
| dianoia retest | `C:\Users\SAMSUNG\Downloads\dianoia-run\problems\p3-sa-finiteness-apssv-2026` | fresh slug created despite deliberately stale `.active` |
| stale-active test | `C:\Users\SAMSUNG\Downloads\dianoia-run\problems\fake-halted-p3-sa-20260520-182055` | fake closed active problem superseded |

## Stale Active Verification

Before the dianoia run, `.active` deliberately pointed to:

```text
fake-halted-p3-sa-20260520-182055
```

The fake problem had:

```text
halt_flag: true
halt_reason: FAILURE-AMBITION-GAP
```

Smoke output:

```json
{
  "fakeSlug": "fake-halted-p3-sa-20260520-182055",
  "route": "prompts/prove.md",
  "slug": "p3-sa-finiteness-apssv-2026",
  "active": "p3-sa-finiteness-apssv-2026",
  "intake": true,
  "result": true,
  "reviewerD": true,
  "researcher": true
}
```

Verdict: stale `.active` no longer blocked fresh problem instantiation in this
retest.

## Machinery-Fire Audit

| component | verdict | evidence |
|-----------|---------|----------|
| `AGENTS.md` route E2 | FIRED | smoke output field `"route": "prompts/prove.md"` |
| `prompts/prove.md` | FIRED | fresh slug `p3-sa-finiteness-apssv-2026` exists and `.active` points to it |
| `00-intake` | FIRED | `intake.md`: "For each fixed positive integer a, define S_a..." |
| `01-survey` | FIRED | `survey.md`: "APSSV 2026 directly proves the requested finiteness." |
| `02-perspective` | FIRED | `perspectives.md`: "number-theorist: match the user set to APSSV..." |
| `03-hypothesize` | FIRED | `hypotheses_live.md`: "APSSV Theorem 6.1 directly applies to S_a." |
| `04-develop` | FIRED | `proofs/sa-finiteness.fml`: "conclude S_a is finite by APSSV and bridge." |
| `06-consolidate` | FIRED | `result.md`: "For every fixed positive integer a, S_a is finite." |
| Reviewer D - intake | FIRED | `reviews/intake-reviewer-D.md` exists and targets S_a ambition |
| Reviewer D - hypotheses | FIRED | `reviews/hypotheses-reviewer-D.md` exists and targets S_a ambition |
| Reviewer D - develop | FIRED | `reviews/develop-reviewer-D.md` exists and targets S_a ambition |
| Reviewer D - consolidate | FIRED | `reviews/consolidate-reviewer-D.md` exists and blocks explicit-bound overclaim |
| subagent `researcher` | FIRED | `inbox/u01-survey/researcher/return.md`: "Verified arXiv metadata for 2604.06609" |
| subagent `surveyor` | FIRED | `inbox/u01-survey/surveyor/return.md`: "APSSV 2026 Section 6" |
| subagent `sanity-checker` | FIRED | `inbox/u03-hypothesize/sanity-checker/sanity.md`: "Endpoint convention and overclaim guard both survive" |
| subagent `prover` | FIRED | `inbox/u04-develop/prover/return.md`: "PROVED_BY_CITATION_PLUS_BRIDGE" |
| subagent `muser` | FIRED | `inbox/u04-develop/muser/return.md`: "NO_NEW_ANGLE_NEEDED" |
| subagent `reviewer` | FIRED | A/B/C reviewer files exist for intake, survey, perspectives, hypotheses, develop, consolidate; D exists for gated phases |
| subagent `specialist-factory` | DID_NOT_FIRE | Not needed; existing perspectives covered number theory, analysis, and combinatorial counting |
| subagent `skill-author` | DID_NOT_FIRE | Not needed in Phase 3; skills are Phase 5 work |

## Head-to-Head Comparison

### Raw Attempt 2

Raw proves finiteness by citation:

```text
Finiteness: proved by citation to APSSV 2026 Theorem 6.1.
```

Raw blocks unsupported extras:

```text
Explicit bound: not supplied.
Small-case completeness: not supplied.
```

Raw gap:

```text
The raw attempt does not create a claim ledger, reviewer files, or adversarial checks.
```

### Dianoia Retest

Dianoia proves the same finiteness statement with a ledgered bridge:

```text
| C-003 | The set S_a in the user statement is the APSSV admissible set, with endpoint k=sqrt(n/a) harmless because n-a k^2=0 is not prime. | PROVED |
```

Dianoia blocks unsupported extras in the final result:

```text
No explicit bound in terms of a is proved in this run.
No complete lists for small a are proved in this run.
```

Dianoia proves the machinery fix fired:

```text
- prior_active: fake-halted-p3-sa-20260520-182055
- route: prompts/prove.md
- new_slug: p3-sa-finiteness-apssv-2026
```

## Three Cited Differences

1. Fresh routing: raw has no routing machinery, while dianoia records
   `route: prompts/prove.md` and `new_slug: p3-sa-finiteness-apssv-2026` in
   `work_journal.md`.
2. Endpoint bridge: raw says the citation applies directly; dianoia records a
   proved bridge row, `C-003`, explaining why the endpoint convention is
   harmless.
3. Adversarial discipline: raw states it has no reviewer files; dianoia records
   Reviewer D files and `review_consolidated.md` says reviewers agree finiteness
   is proved while explicit bounds and exact small-a lists are not claimed.

## Verdict

VALUE_ADDED.

The retest does not show dianoia discovering a stronger theorem than raw.
It does show that the fixed machinery now:

1. avoids the stale `.active` failure that caused the degraded comparison,
2. instantiates a fresh problem and fires the phase loop for S_a,
3. adds a useful endpoint bridge and ledger discipline,
4. preserves honesty about explicit bounds and small-case lists.

Branch instruction: proceed to Phase 4+.
