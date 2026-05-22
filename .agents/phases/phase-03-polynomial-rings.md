# Phase 03 — Polynomial Rings

**Tier:** 1
**Status:** ⬜ Not Started
**Depends on:** Phase 01
**Unblocks:** Phase 04 (parts), Phase 06, 07, 09, 10, 11, 13, 14

## Goal

Cover `sage.rings.polynomial/` and its `pbori/`, `padics/`, `weil/`
subdirectories. This is the single largest subpackage under `rings/` and
imports cycle through coercion, so the existing `polynomial_element`,
`multi_polynomial`, `polynomial_ring`, `multi_polynomial_ring`,
`polynomial_quotient_ring*`, `laurent_polynomial`, `ore_polynomial_ring`,
`multi_polynomial_ideal`, `groebner_fan`, `polynomial_ring_constructor`
stubs must be audited rather than rewritten.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T03.1 | **Univariate core** — audit & complete `polynomial_element`, `polynomial_element_generic`, `polynomial_ring`, `polynomial_ring_constructor`, `polynomial_ring_homomorphism`, `polynomial_compiled`, `polynomial_singular_interface`, `commutative_polynomial`. | ~8 | — | ⬜ | Existing stubs in this group. |
| T03.2 | **Univariate specialised dense** — `polynomial_integer_dense_flint`, `polynomial_integer_dense_ntl`, `polynomial_rational_flint`, `polynomial_real_mpfr_dense`, `polynomial_real_arb`, `polynomial_complex_arb`, `polynomial_number_field`. | 7 | T03.1 | ⬜ | All `.pyx`; many Sage-specific overloads. |
| T03.3 | **Univariate finite-field & GF(2)** — `polynomial_gf2x`, `polynomial_modn_dense_ntl`, `polynomial_zmod_flint`, `polynomial_zz_pex`, `evaluation_flint`, `evaluation_ntl`. | 6 | T03.1 | ⬜ | Depends on `finite_rings` only via signatures — forward-ref OK. |
| T03.4 | **Multivariate core** — audit & complete `multi_polynomial`, `multi_polynomial_element`, `multi_polynomial_ring`, `multi_polynomial_ring_base`, `multi_polynomial_ideal`, `multi_polynomial_ideal_libsingular`, `multi_polynomial_libsingular`, `multi_polynomial_sequence`, `polydict`, `plural`, `hilbert`. | ~11 | T03.1 | ⬜ | Heavy `libsingular` coupling — keep `object` only where Sage source forwards arbitrary Python objects. |
| T03.5 | **Ideals, term order, fans** — `ideal`, `term_order`, `groebner_fan`, `symmetric_ideal`, `symmetric_reduction`, `toy_buchberger`, `toy_d_basis`, `toy_variety`, `flatten`, `omega`. | ~10 | T03.4 | ⬜ | |
| T03.6 | **Laurent polynomials** — `laurent_polynomial`, `laurent_polynomial_ring`, `laurent_polynomial_ring_base`, `laurent_polynomial_mpair`, `laurent_polynomial_ideal`. | 5 | T03.1 | ⬜ | |
| T03.7 | **Ore / skew polynomials** — `ore_polynomial_element`, `ore_polynomial_ring`, `ore_function_element`, `ore_function_field`, `skew_polynomial_element`, `skew_polynomial_ring`, `skew_polynomial_finite_field`, `skew_polynomial_finite_order`. | 8 | T03.1 | ⬜ | |
| T03.8 | **Infinite polynomial rings & misc** — `infinite_polynomial_element`, `infinite_polynomial_ring`, `cyclotomic`, `complex_roots`, `convolution`, `polynomial_fateman`, `q_integer_valued_polynomials`, `integer_valued_polynomials`, `msolve`, `real_roots`, `refine_root`, `binary_form_reduce`. | ~12 | T03.1 | ⬜ | |
| T03.9 | **Polyboris (`pbori`) subpackage** — `pbori/pbori.pyx`, `pbori/brial.py`, plus catalog. | ~4 | T03.4 | ⬜ | Bring in only what the Sage source exposes publicly. |
| T03.10 | **`padics/` polynomial subpackage** — `padics/factor_padic`, related helpers (full file list in Phase-1 exempt audit). | ~6 | T03.1 | ⬜ | Coordinate with Phase 04 (padics). |
| T03.11 | **`weil/` polynomial subpackage** — Weil polynomial helpers. | ~4 | T03.1 | ⬜ | |

## Bootstrap with stubgen

Every task in this phase should start with
`python3 -m mypy.stubgen -p sage.rings.polynomial.<module>` (or the
`just scaffold <module>` shortcut). Cython `.pyx` modules often resolve
via the compiled `.so`, so stubgen's `--inspect-mode` is required there.
Treat the scaffold as a Phase-1 method enumeration only — every `Any` and
every inherited method must be removed before commit (see
[feature.md](../feature.md#tooling-auto-scaffolding-from-source)).

## Parallelism

- T03.1 first (foundation). Then T03.2, T03.3, T03.4, T03.6, T03.7,
  T03.8 in parallel.
- T03.5, T03.9 wait on T03.4. T03.10 coordinates with Phase 04.

## Risks

- The polynomial type tower has overloaded arithmetic in every direction;
  every binary op must be `@overload`'d, not collapsed.
- `polydict.pyx` is a Cython class with dict-like behaviour. Use
  `__getitem__` / `__setitem__` / `__contains__` signatures; never inherit
  from `dict` in the stub.
- `multi_polynomial_ideal.py` re-exports many helpers — verify each is
  defined in this module before listing it directly (AGENTS.md
  "no inherited-method inflation").
