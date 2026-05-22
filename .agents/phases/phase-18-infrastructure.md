# Phase 18 — Infrastructure: Numerical, Plot, Interfaces, Dev

**Tier:** 5 (last)
**Status:** ⬜ Not Started
**Depends on:** Phase 02
**Unblocks:** none — this is the closing phase

## Goal

Cover the remaining subpackages that are either rarely typed by downstream
consumers or that consist mostly of glue / interfaces / dev tooling:
`numerical/`, `stats/`, `probability/`, `plot/`, `interacts/`, `typeset/`,
`interfaces/`, `libs/`, `repl/`, `doctest/`, `parallel/`, `sat/`,
`logic/`, `databases/`, `features/`, `ext/`, `tests/`, `cli/`, `tensor/`.

Many of these will land with a high fraction of Exempt modules; the
Phase-1 audit must cover them so this phase has a clean target list.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T18.1 | **Numerical** — `numerical/` (32 files): split into 2 commits along (a) `optimize`, `interpolation`, `linear_functions`, `linear_tensor`, `mip`, `sdp`, `gauss_legendre`, (b) `backends/` subpackage. | ~32 (two commits) | — | ⬜ | |
| T18.2 | **Statistics & probability** — `stats/` (12 files) + `probability/` (2 files). | 14 | — | ⬜ | One commit. |
| T18.3 | **Tensor** — `tensor/` (18 files): `differential_forms`, `differential_form_element`, `modules/`, plus catalog. | 18 | T05.7 | ⬜ | |
| T18.4 | **Plot: foundations** — `plot/` core (24 of 48): `plot`, `plot3d/`, `colors`, `graphics`, `line`, `point`, `polygon`, `text`, `arrow`, `bar_chart`, `circle`, `contour_plot`, `density_plot`, `disk`, `ellipse`, `histogram`, `hyperbolic_arc`, `hyperbolic_polygon`, `hyperbolic_regular_polygon`, `matrix_plot`, `misc`, `multigraphics`, `plot_field`, `scatter_plot`, `step`. | ~25 | — | ⬜ | |
| T18.5 | **Plot: 3D & advanced** — `plot3d/` subpackage and remaining 2D leaves (~23). | ~23 | T18.4 | ⬜ | |
| T18.6 | **Interacts, typeset** — `interacts/` (7), `typeset/` (6). | 13 | — | ⬜ | Bundle as one commit. |
| T18.7 | **Interfaces: classical** — `interfaces/` core (~28 of 57): `axiom`, `expect`, `fricas`, `gap`, `gap3`, `gnuplot`, `interface`, `kash`, `lie`, `macaulay2`, `magma`, `magma_free`, `maple`, `mathematica`, `mathics`, `matlab`, `maxima`, `maxima_abstract`, `maxima_lib`, `mupad`, `mwrank`, `octave`, `pari`, `polymake`, `qsieve`, `quit`, `r`, `rubik`. | ~28 | — | ⬜ | Some of these are mostly subprocess shells with thin public API. |
| T18.8 | **Interfaces: misc & remainder** — `interfaces/` remaining (~29). | ~29 | T18.7 | ⬜ | Likely many Exempt. |
| T18.9 | **Libs: pari & ntl** — `libs/pari/` and `libs/ntl/` subpackages (typically ~20 files each). | ~25 | — | ⬜ | Two commits along subpackage seam. |
| T18.10 | **Libs: gap, singular, flint** — `libs/gap/`, `libs/singular/`, `libs/flint/` (~30 files combined). | ~30 (two commits) | — | ⬜ | |
| T18.11 | **Libs: residue** — remaining `libs/` subpackages (105 files total). | ~30 | — | ⬜ | Two commits along subpackage seam. |
| T18.12 | **Repl** — `repl/` (42 files): split into 2 commits along (a) `display/`, `interpreter/`, `ipython_extension`, `ipython_kernel/`, (b) `attach`, `preparse`, `rich_output/`, `user_globals`. | ~42 (two commits) | — | ⬜ | |
| T18.13 | **Doctest** — `doctest/` (15 files): `control`, `external`, `fixtures`, `forker`, `marked_output`, `parsing`, `reporting`, `sources`, `test`, `util`, `external`, plus residue. | ~15 | — | ⬜ | |
| T18.14 | **Parallel, sat, logic** — `parallel/` (7), `sat/` (10), `logic/` (6). | ~23 | — | ⬜ | Bundle into 2 commits. |
| T18.15 | **Databases & features & ext & tests & cli** — `databases/` (15), `features/` (61), `ext/` (3), `tests/` (88, but most Exempt as test scaffolding), `cli/` (11). | ~30 in-scope after audit | T01.1 (audit) | ⬜ | Heaviest Exempt rate. Split into 2–3 commits. |
| T18.16 | **Final pyproject & README sync** — register every newly-stubbed subpackage in `pyproject.toml`; rewrite `README.md` "Scope" to describe full parity. | ~2 file edits | T18.1–T18.15 | ⬜ | Last task in the entire feature. |

## Parallelism

- Every task in Phase 18 is independent of every other (with the
  exception of T18.5 → T18.4 chain and T18.16 last). Parallelise freely.

## Risks

- `features/` modules are mostly classes with class-level `find()` /
  `is_present()` methods returning `FeatureTestResult`. Stub the protocol
  precisely.
- `libs/pari/` exposes the `Pari` instance with hundreds of forwarded
  methods; only stub the documented public surface, not the dynamic
  forwards.
- `repl/` modules depend on IPython internals. Forward-reference IPython
  types as strings; do not add IPython to the dependency closure.
- `tests/` directory often contains modules that exist purely to be
  imported by doctests — Exempt list will be long.
