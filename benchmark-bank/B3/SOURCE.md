# B3 Source

## Metadata

- Author: Miraj Samarakkody
- Year: 2026
- Title: "Formalizing the Classical Isoperimetric Inequality in the
  Two-Dimensional Case"
- Exact statement reference: arXiv:2603.14663v1, Section 7.7, Theorem 7.5

## Source

arXiv:2603.14663, DOI-style URL: `https://arxiv.org/abs/2603.14663`.

## Modification

The benchmark asks whether the paper formalizes the full unrestricted classical
statement for all simple closed plane curves, including equality uniqueness for
circles.

This modifies the paper's precise Lean theorem by stripping its regularity,
arc-length, Fourier-identity, and summability hypotheses and by adding equality
uniqueness. The benchmark tests whether dianoia catches hypothesis and
contribution-scope overclaims.

## Area

geometry

## Artifacts

- Raw baseline: `C:\Users\SAMSUNG\Downloads\raw-attempt-4`
- Dianoia run: `C:\Users\SAMSUNG\Downloads\dianoia-run\problems\b3-isoperimetric-formalization`
- Source checks: arXiv abstract page and HTML version for Theorem 7.5.
