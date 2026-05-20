# Phase 0 - Verify Prior Experiment

Date: 2026-05-20

## Scope

This audit verifies the prior S_a controlled comparison named in the MASTERPIECE
goal, not the fixed T1-T6 mastery ladder alone. The relevant run workspace is
`C:\Users\SAMSUNG\Downloads\dianoia-run`; the raw baseline is
`C:\Users\SAMSUNG\Downloads\raw-attempt`.

## Timeline Reconstruction

### Requested Git Window: 2026-05-20 17:00-17:30 +09:00

Command run in both `dianoia` and `dianoia-run`:

```text
git log --since='2026-05-20 17:00:00 +0900' --until='2026-05-20 17:30:00 +0900' --date=iso-strict --pretty=format:'%H %ad %s'
```

Result: no commits in the requested window.

This is material: the S_a comparison happened in the filesystem, but it was not
captured as a git commit during the requested interval.

### Filesystem Events in the Requested Window

| path | timestamp | evidence |
|------|-----------|----------|
| `dianoia-run/problems/cycle-4-t6-perfect-numbers/work_journal.md` | 2026-05-20T17:22:35.3636202+09:00 | contains the S_a entry |
| `raw-attempt/answer.md` | 2026-05-20T17:23:07.4264842+09:00 | raw answer artifact |
| `raw-attempt/searches.md` | 2026-05-20T17:23:07.4304852+09:00 | raw search log |
| `raw-attempt/honest_gaps.md` | 2026-05-20T17:23:07.4326059+09:00 | raw gap log |
| `raw-attempt/code.md` | 2026-05-20T17:24:24.7676483+09:00 | raw computation log |
| `raw-attempt/timing.md` | 2026-05-20T17:24:35.5795633+09:00 | raw timing log |

### Nearest Relevant Git Commits

The cycle-4 mastery ladder was committed much earlier:

| commit | time | subject |
|--------|------|---------|
| `91fecf8c01a879b6fb642bd4c8dc033d7cf48677` | 2026-05-20T01:38:09+09:00 | cycle-4: init cycle |
| `24e8440964ffbef1396e3c5f6937f7880b13543d` | 2026-05-20T01:38:50+09:00 | cycle-4: T1 SUCCESS-MEANINGFUL |
| `0b83586f41920a7dde497488f386c72afe027ef9` | 2026-05-20T01:38:53+09:00 | cycle-4: T2 SUCCESS-MEANINGFUL |
| `291406e9f999fbda42e131b196e6a0a9aff52b19` | 2026-05-20T01:38:56+09:00 | cycle-4: T3 SUCCESS-MEANINGFUL |
| `13791f116e35206e923159b87f521dea2fca2dce` | 2026-05-20T01:38:59+09:00 | cycle-4: T4 SUCCESS-MEANINGFUL |
| `94cf9e3c6ec34b94eaade62c74a320486abc98f1` | 2026-05-20T01:39:01+09:00 | cycle-4: T5 BLOCKED-ITERATE-with-new-obstruction |
| `2358472ee67a11fe60a42698efa3a210b599318f` | 2026-05-20T01:39:05+09:00 | cycle-4: T6 FAILURE-AMBITION-GAP |
| `d45f9a6f1dae1e37baf9bf61e776e1e7901e91bf` | 2026-05-20T01:39:39+09:00 | cycle-4: capability report |
| `7d5715e384ba91811d0db0018ce115485845ecf1` | 2026-05-20T01:39:58+09:00 | cycle-4: diagnosis |
| `32ccc9ceff381da9fd2200d3abf8c8fd379a7007` | 2026-05-20T01:40:22+09:00 | cycle-4: post-improve audit |
| `498a6239e6f6f03d358c236c4afaf38ed2765025` | 2026-05-20T01:40:35+09:00 | cycle-4: tracking update |
| `b143aa5c0e3a713f2d50245a79d692a246bb4835` | 2026-05-20T01:41:08+09:00 | MASTERY reached at cycle-4 |

## Core Stale-Active Evidence

At the time of the S_a attempt, `dianoia-run/problems/.active` still contained:

```text
cycle-4-t6-perfect-numbers
```

The active problem state was closed:

```text
halt_flag: true
current_phase: 6
phase_status: failure-ambition-gap
halt_reason: FAILURE-AMBITION-GAP
```

Instead of creating a fresh S_a problem slug, the S_a task was appended to the
old perfect-number work journal:

```text
2026-05-20T17:22:22+09:00 | Codex | user-posed quadratic-prime-set task
- Statement examined: S_a = {n > 0 : for every k with 1 <= k <= sqrt(n/a), gcd(k,n)=1, n-a k^2 is prime}.
```

The old active intake still says:

```text
original_problem: Prove that the set of perfect numbers is infinite, or prove that it is finite.
normalized_target: Decide whether there are infinitely many perfect numbers or finitely many perfect numbers by proving one alternative.
```

## Machinery-Fire Audit

Verdict key:

- FIRED means the component produced S_a-specific evidence for the 17:22 task.
- DID_NOT_FIRE means only stale cycle-4 perfect-number evidence exists, or no
  evidence exists.

| component | verdict | quoted file evidence |
|-----------|---------|----------------------|
| `prompts/prove.md` fresh slug creation | DID_NOT_FIRE | `.active` remained `cycle-4-t6-perfect-numbers`; S_a appears only in the old work journal: `user-posed quadratic-prime-set task`. |
| `00-intake` | DID_NOT_FIRE | stale intake: `original_problem: Prove that the set of perfect numbers is infinite, or prove that it is finite.` |
| `01-survey` | DID_NOT_FIRE | stale survey: `[FRONTIER] Infinitude of Mersenne primes is open...`; no S_a/APSSV survey file exists under a new slug. |
| `02-perspective` | DID_NOT_FIRE | stale perspective: `number-theorist: perfect numbers and Mersenne primes.` |
| `03-hypothesize` | DID_NOT_FIRE | stale hypotheses: `There are infinitely many perfect numbers.` and `There are finitely many perfect numbers.` |
| `04-develop` | DID_NOT_FIRE | stale proof target: `target: Prove infinitude or finiteness of perfect numbers.` |
| `05-review` after intake | DID_NOT_FIRE | stale review file says `phase_reviewed: intake` and attacks Mersenne/odd-perfect routes, not S_a. |
| `05-review` after survey | DID_NOT_FIRE | stale survey reviewers say `phase_reviewed: survey` and check perfect-number claims. |
| `05-review` after perspective | DID_NOT_FIRE | stale perspective reviewers say `phase_reviewed: perspectives` and check perfect-number claims. |
| `05-review` after hypothesize | DID_NOT_FIRE | stale hypotheses reviewers say `phase_reviewed: hypotheses` and check perfect-number claims. |
| `05-review` after develop | DID_NOT_FIRE | stale develop reviewers say `phase_reviewed: develop` and check perfect-number claims. |
| `06-consolidate` | DID_NOT_FIRE | stale result: `No proof of finiteness or infinitude was obtained...` for perfect numbers. |
| `05-review` after consolidate | DID_NOT_FIRE | stale consolidated review: `D reviewed intake, hypotheses, develop, and consolidate`; no S_a review exists. |
| Reviewer D - intake | DID_NOT_FIRE | stale D review: `# Reviewer D - intake`; attack text concerns Euclid-Euler/Mersenne primes. |
| Reviewer D - hypotheses | DID_NOT_FIRE | stale D review: `# Reviewer D - hypotheses`; Q2 says both infinitude and finiteness of perfect numbers were attacked. |
| Reviewer D - develop | DID_NOT_FIRE | stale D review: `# Reviewer D - develop`; attack text concerns Euclid-Euler/Mersenne primes. |
| Reviewer D - consolidate | DID_NOT_FIRE | stale D review: `# Reviewer D - consolidate`; `SUCCESS-MEANINGFUL and corpus promotion are blocked` for T6. |
| subagent `researcher` | DID_NOT_FIRE | stale return: `status: VERIFIED`; verified citations are Euler/Nielsen perfect-number citations. |
| subagent `surveyor` | DID_NOT_FIRE | no S_a surveyor return exists; context manifest lists only researcher/sanity/prover/muser returns. |
| subagent `specialist-factory` | DID_NOT_FIRE | no S_a specialist-factory return exists in the active T6 context. |
| subagent `sanity-checker` | DID_NOT_FIRE | stale return: `status: kills-both-direct-routes`; artifact is `hypotheses_live.md` for perfect numbers. |
| subagent `prover` | DID_NOT_FIRE | stale return: `status: GAP`; artifact is `proofs/perfect-numbers-attempt.fml`. |
| subagent `muser` | DID_NOT_FIRE | stale return: `status: NO_SAFE_NEW_ANGLE`; artifact is `failures/ambition-gap.md`. |
| subagent `skill-author` | DID_NOT_FIRE | no S_a skill-author return exists; no `skills/<slug>/SKILL.md` was created. |
| subagent `reviewer` | DID_NOT_FIRE | reviewer files exist only for stale perfect-number phases; no S_a reviewer file exists. |

## Raw Baseline Contrast

The raw attempt did address S_a directly. Its answer begins with:

```text
Problem: for fixed positive integer `a`,
`S_a = { n > 0 : for every integer k with 1 <= k <= sqrt(n/a) and gcd(k,n)=1, n - a k^2 is prime }`.
```

It also cites the intended paper:

```text
Boris Alexeev, Moe Putterman, Mehtaab Sawhney, Mark Sellke, Gregory Valiant, 2026, "Short proofs in combinatorics, probability and number theory II", Theorem 6.1
```

This contrast is enough to identify the failure mode: the raw branch worked on
the S_a problem, while dianoia-run never instantiated S_a as a dianoia problem.

## Verdict

The prior S_a experiment was not a fair test of dianoia's phase machinery.

Machinery silently failed at the routing/instantiation boundary: stale
`problems/.active` pointed to `cycle-4-t6-perfect-numbers`, whose
`session_state.md` had `halt_flag: true`, and the S_a task was appended to that
closed problem's `work_journal.md` instead of invoking `prompts/prove.md` to
create a fresh slug and run `00-intake`.

Downstream phases, Reviewer D, and subagents therefore did not fire for S_a.
The observed DEGRADED comparison is valid as evidence of a blocking workflow
bug, but invalid as evidence that a working dianoia phase loop underperforms raw
attempts on S_a.
