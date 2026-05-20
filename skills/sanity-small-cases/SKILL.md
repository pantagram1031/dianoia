# sanity-small-cases

description: Use bounded small-case probes when a conjecture, lemma, benchmark
answer, or subagent claim can be quickly refuted or calibrated by checking
minimal examples, edge cases, or finite prefixes.

## When To Use

- A claim has a natural first few cases, smallest counterexample, or boundary
  condition.
- A proof idea may fail for `n=0`, `n=1`, equality endpoints, empty sets, or
  degenerate parameters.
- A benchmark comparison needs evidence that a proposed theorem is not merely
  plausible on prose grounds.
- A subagent supplies a hypothesis with a clear kill condition and a bounded
  computation or hand-check can test it.

## When Not To Use

- The claim is purely existential and has no meaningful finite prefix or edge
  case.
- The finite probe would require unbounded search or unverifiable heuristics.
- The result of a small-case check would be used as a proof of a general
  theorem without a separate induction, coverage, or structural argument.
- The problem already has a rigorous counterexample or proof in the ledger.

## Procedure

1. Restate the claim with quantifiers and parameter ranges explicit.
2. Identify the smallest meaningful cases, equality endpoints, and degenerate
   inputs.
3. Define the kill condition before computing: what exact output would refute
   or weaken the claim.
4. Use the smallest reliable method available: hand arithmetic, short script,
   table, or cited known sequence.
5. Record the checked domain and all assumptions. Never leave the range
   implicit.
6. Return one of:
   - `KILLS`: a counterexample or boundary failure was found.
   - `SURVIVES`: the claim survived only the stated finite probe.
   - `GAP`: the probe was inconclusive or the kill condition was ill-posed.
7. If the claim is finite-list completeness, switch to
   `skills/coverage-systems/SKILL.md` before upgrading `SURVIVES` to a proof.

## Examples

Example trigger:

```text
Hypothesis: every n in S_2 is odd. Kill condition: find an even n <= 200 in S_2.
```

Expected use:

```text
checked_domain: even n, 2 <= n <= 200
status: SURVIVES
note: This is not a proof; it only calibrates the hypothesis.
```

Example edge-case trigger:

```text
The theorem says for all k <= sqrt(n/a), n-a*k^2 is prime.
```

Expected use:

```text
Check the equality endpoint k = sqrt(n/a). If n-a*k^2 = 0, primality fails,
so either the endpoint must be impossible or the statement needs a bridge
lemma explaining why it is harmless.
```

Example non-use:

```text
Prove infinitely many primes in an arithmetic progression.
```

Reason not to use:

```text
Small cases can illustrate the statement but cannot provide meaningful
evidence for the general infinitude proof.
```
