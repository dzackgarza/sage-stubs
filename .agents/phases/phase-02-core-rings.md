# Phase 02 — Core Rings & Arithmetic

**Tier:** 1
**Status:** 🟡 In Progress
**Depends on:** Phase 01
**Unblocks:** Phase 03, 04, 06, 07, 08, 13, 14, 16, 17, 18

## Goal

Cover the root of `sage.rings/` (everything *not* under
`polynomial/`, `number_field/`, `padics/`, `finite_rings/`,
`function_field/`, `valuation/`, `asymptotic/`, `semirings/`, `bernmm/`,
`convert/`, `invariants/`, `weil/`, `pbori/` subdirectories) plus
`sage.arith/`. This is the wide base every algebraic stub leans on.

## Exit criteria

- Every in-scope module listed below has a `.pyi` (or is Exempt).
- `mypy --strict` passes.
- Existing stubs (`integer`, `rational`, `infinity`, `real_double`,
  `real_mpfi`, `real_mpfr`, `complex_double`, `complex_mpfr`, `qqbar`,
  `lazy_series`, `morphism`, `fraction_field`, `ring`, `power_series_*`,
  `laurent_series_*`) are *audited* for completeness, not narrowed.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T02.1 | **`sage.arith`** — `misc`, `functions`, `multi_modular`, `numerical_approx`, `power`, `rational_reconstruction`, `srange`, `long`. | ~8 | — | ✅ Done | `misc` already has a stub; complete the rest. |
| T02.2 | **Real / complex floating point** — audit & complete `real_mpfr`, `real_double`, `real_double_element_gsl`, `real_arb`, `real_interval_absolute`, `real_lazy`, `real_mpfi`, `real_field`, `complex_double`, `complex_mpfr`, `complex_mpc`, `complex_arb`, `complex_interval`, `complex_interval_field`, `complex_conversion`, `cc.py`, `cif.py`. | ~17 | — | 🟡 In Progress | Several stubs already exist — extend, never narrow. |
| T02.3 | **Integer / rational base** — audit & complete `integer`, `integer_ring`, `integer_fake`, `rational`, `rational_field`, `factorint`, `factorint_flint`, `factorint_pari`, `bernoulli_mod_p`, `bernmm` (root), `numbers_abc`, `fast_arith`. | ~12 | — | ⬜ | Most files have existing stubs; audit Phase-1 / Phase-2 of AGENTS.md. |
| T02.4 | **Algebraic numbers & continued fractions** — `qqbar`, `qqbar_decorators`, `continued_fraction`, `continued_fraction_gosper`, `universal_cyclotomic_field`, `imaginary_unit`. | ~6 | — | ⬜ | |
| T02.5 | **Ring base classes & morphisms** — `ring`, `generic`, `morphism`, `homset`, `ideal`, `ideal_monoid`, `noncommutative_ideals`, `commutative_algebra`, `derivation`, `abc`. | ~10 | — | ⬜ | `ring`, `morphism`, `abc` have existing stubs. |
| T02.6 | **Power / Laurent / Puiseux series** — `power_series_ring`, `power_series_ring_element`, `power_series_poly`, `power_series_mpoly`, `power_series_pari`, `laurent_series_ring`, `laurent_series_ring_element`, `puiseux_series_ring`, `puiseux_series_ring_element`, `big_oh`. | ~10 | T02.5 | ⬜ | |
| T02.7 | **Fractions, localisations, quotients** — `fraction_field`, `fraction_field_element`, `fraction_field_FpT`, `localization`, `quotient_ring`, `quotient_ring_element`, `monomials`. | ~7 | T02.5 | ⬜ | |
| T02.8 | **Lazy series & lazy species** — `lazy_series`, `lazy_series_ring`, `lazy_species`. | 3 | T02.5 | ⬜ | Small but tightly coupled — bundle. |
| T02.9 | **Ring extensions & Tate algebra** — `ring_extension`, `ring_extension_conversion`, `ring_extension_element`, `ring_extension_homset`, `ring_extension_morphism`, `tate_algebra`, `tate_algebra_element`, `tate_algebra_ideal`. | 8 | T02.5 | ⬜ | |
| T02.10 | **C-finite, Pari, Bernmm, sum_of_squares, species, tests** — `cfinite_sequence`, `pari_ring`, `bernmm` package surface, `sum_of_squares`, `species`, `infinity`. | ~6 | — | ⬜ | `infinity` has an existing stub. |
| T02.11 | **Convert** — `sage.rings.convert/` (typically `mpfi`, `to_real_ramp` style helpers). | ~3 | — | ⬜ | Some files may be Exempt — list explicitly. |
| T02.12 | **Invariants** — `sage.rings.invariants/` (binary form invariants). | ~3 | T02.6 | ⬜ | |

## Parallelism

- T02.1, T02.3, T02.4, T02.5, T02.10, T02.11 — independent, run in
  parallel.
- T02.2 — independent but high-volume; one owner.
- T02.6, T02.7, T02.8, T02.9 — chain after T02.5 lands.
- T02.12 — needs T02.6.

## Risks

- `integer.pyx` / `rational.pyx` are foundational; do not rewrite
  existing stubs unless mypy proves them wrong.
- `ring.pyx` has overloaded `__mul__`, `__pow__` etc. — use `@overload`,
  never collapse to `object`.
- Coercion forwards on numeric types: prefer `Self` or `Union[Self, int,
  Rational]` rather than `object`. `object` is only acceptable where the
  Sage source explicitly documents "arbitrary Python object" coercion.
