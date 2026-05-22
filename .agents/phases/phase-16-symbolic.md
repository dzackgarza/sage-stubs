# Phase 16 — Symbolic, Calculus, Functions

**Tier:** 3
**Status:** ⬜ Not Started
**Depends on:** Phase 02
**Unblocks:** Phase 17 (parts)

## Goal

Cover `sage.symbolic/`, `sage.calculus/`, `sage.functions/`. These have
**zero** existing stubs and they are heavily entangled with the Pynac/Maxima
backends, so the public surface is the only meaningful target.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T16.1 | **Symbolic core** — `expression`, `ring`, `function`, `function_factory`, `assumptions`, `constants_c`, `constants`. | 7 | — | ⬜ | `expression.pyx` is huge — capture only documented public methods. |
| T16.2 | **Symbolic: ring & callable** — `callable`, `comparison`, `expression_conversions`, `expression_conversion_algebraic`, `expression_conversion_sympy`, `operators`, `units`. | 7 | T16.1 | ⬜ | |
| T16.3 | **Symbolic: misc / parser / pynac** — `pynac`, `pynac_function_impl`, `pynac_impl`, `pynac_wrap`, `random_tests`, `subring`, `symengine`, `tests`. | ~8 | T16.1 | ⬜ | Many `pynac*` files are pure C glue — confirm Exempt in Phase-1 audit. |
| T16.4 | **Calculus** — `calculus`, `desolvers`, `functional`, `functions`, `interpolation`, `integration`, `riemann`, `transforms/`, `var`, `wester`, `predefined`, `tests`. | ~13 | — | ⬜ | |
| T16.5 | **Calculus: ODEs & wave** — `ode`, `tests/wave_pde`, plus any leftovers from the 18 files in `calculus/`. | ~5 | T16.4 | ⬜ | |
| T16.6 | **Functions: airy / Bessel / gamma / hypergeometric** — `airy`, `bessel`, `error`, `exp_integral`, `gamma`, `hypergeometric`, `hyperbolic`. | 7 | — | ⬜ | |
| T16.7 | **Functions: log / trig / piecewise / orthogonal** — `log`, `trig`, `piecewise`, `orthogonal_polys`, `special`, `transcendental`, `prime_pi`, `min_max`, `wigner`, `jacobi`, `spike_function`, `generalized`. | ~12 | — | ⬜ | |
| T16.8 | **Functions: misc / other** — `other`, `all`, `tests`, plus remaining leaves from the 20 files. | ~4 | — | ⬜ | |

## Parallelism

- T16.1 first. Then T16.2, T16.3 chain.
- T16.4, T16.6, T16.7, T16.8 independent of symbolic and of each other.

## Risks

- `expression.pyx` exposes a huge surface; Sage docstrings frequently
  describe arithmetic via SR coercion. Use `Self | Expression | int | float
  | Rational` unions, never `Any`.
- `function_factory.py` constructs symbolic functions dynamically; only
  expose the documented `function()` constructor, not the dynamic classes.
- Maxima/Pynac glue files are Exempt unless they declare public Python
  classes.
