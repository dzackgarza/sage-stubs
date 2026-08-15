# Phase 03 — Polynomial Rings

**Tier:** 1
**Status:** 🟡 In Progress
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
| T03.1 | **Univariate core** — audit & complete `polynomial_element`, `polynomial_element_generic`, `polynomial_ring`, `polynomial_ring_constructor`, `polynomial_ring_homomorphism`, `polynomial_compiled`, `polynomial_singular_interface`, `commutative_polynomial`. | ~8 | — | ✅ Done | polynomial_element: 115-method Polynomial + dense/inexact + 2 map classes; element_generic: 18 classes; ring: 19 classes + polygen/polygens; constructor: 4 functions. PolynomialRing_general renamed -> PolynomialRing_generic (source name). |
| T03.2 | **Univariate specialised dense** — `polynomial_integer_dense_flint`, `polynomial_integer_dense_ntl`, `polynomial_rational_flint`, `polynomial_real_mpfr_dense`, `polynomial_real_arb`, `polynomial_complex_arb`, `polynomial_number_field`. | 7 | T03.1 | ✅ Done | flint/ntl: full ZZ[x] arithmetic + factoring surface; rational_flint: galois_group, hensel_lift, 13 series hooks, numerator/denominator; mpfr dense: PolynomialRealDense + make_PolynomialRealDense; arb pair: 12 transcendental series hooks + compose_trunc; number_field: absolute/relative gcd. |
| T03.3 | **Univariate finite-field & GF(2)** — `polynomial_gf2x`, `polynomial_modn_dense_ntl`, `polynomial_zmod_flint`, `polynomial_zz_pex`, `evaluation_flint`, `evaluation_ntl`. | 6 | T03.1 | ✅ Done | gf2x: Polynomial_GF2X + GF2X_Build* helpers; modn: 4-class NTL tower (dense_mod_n/zz/ZZ/mod_p) + make_element + small_roots; zmod_flint: rational_reconstruction, factor, squarefree_decomposition; zz_pex: inverse_series_trunc, _richcmp_; evaluation_*: cdef-only, empty stubs. Polynomial_template modelled as empty intermediate base (pxi include). |
| T03.4 | **Multivariate core** — audit & complete `multi_polynomial`, `multi_polynomial_element`, `multi_polynomial_ring`, `multi_polynomial_ring_base`, `multi_polynomial_ideal`, `multi_polynomial_ideal_libsingular`, `multi_polynomial_libsingular`, `multi_polynomial_sequence`, `polydict`, `plural`, `hilbert`. | ~11 | T03.1 | ✅ Done | multi_polynomial: MPolynomial(CommutativePolynomial) 57-method base + empty MPolynomial_libsingular base; polydict: PolyDict + ETuple (~110 methods); polydict element (68); ring_base (55, moved per source layout) + ring_polydict; MPolynomialRing_libsingular + MPolynomial_libsingular (~100); ideal: full 6-mixin hierarchy (~110) + NCPolynomialIdeal + quotient ideal; ideal_libsingular helpers; PolynomialSequence_generic/gf2/gf2e; plural: G_AlgFactory + NCPolynomialRing_plural + NCPolynomial_plural + SCA/ExteriorAlgebra; hilbert. Delivered as 3 commits. |
| T03.5 | **Ideals, term order, fans** — `ideal`, `term_order`, `groebner_fan`, `symmetric_ideal`, `symmetric_reduction`, `toy_buchberger`, `toy_d_basis`, `toy_variety`, `flatten`, `omega`. | ~10 | T03.4 | ✅ Done | ideal: Ideal_1poly_field; term_order: TermOrder completed (55 methods + termorder_from_singular); groebner_fan: legacy audit — module helpers added, homogeneity_space corrected to PolyhedralCone (source L1180), _gfan_* internals added; symmetric_ideal (13) + symmetric_reduction (14); toy_buchberger/toy_d_basis/toy_variety; flatten: 4 specialization morphisms; omega: MacMahonOmega + 9 helpers. |
| T03.6 | **Laurent polynomials** — `laurent_polynomial`, `laurent_polynomial_ring`, `laurent_polynomial_ring_base`, `laurent_polynomial_mpair`, `laurent_polynomial_ideal`. | 5 | T03.1 | ✅ Done | laurent_polynomial.pyi rewritten: LaurentPolynomial(CommutativeAlgebraElement) + LaurentPolynomial_univariate (72 methods); new mpair (52), ring_base (28), ring (2 subclasses + LaurentPolynomialRing + helpers), ideal (23). |
| T03.7 | **Ore / skew polynomials** — `ore_polynomial_element`, `ore_polynomial_ring`, `ore_function_element`, `ore_function_field`, `skew_polynomial_element`, `skew_polynomial_ring`, `skew_polynomial_finite_field`, `skew_polynomial_finite_order`. | 8 | T03.1 | ✅ Done | ore_polynomial_element: OrePolynomial + generic_dense (58+33 methods, left/right gcd-lcm-xgcd families); ore_polynomial_ring rewritten from 8-line legacy (UniqueRepresentation base, twisting_morphism/derivation, fraction_field); ore_function pair incl. center injection sections; skew element/ring incl. power_mod, minimal_vanishing/lagrange; finite_order (reduced trace/norm/charpoly, bound); finite_field (irreducible divisors, factor, factorizations). |
| T03.8 | **Infinite polynomial rings & misc** — `infinite_polynomial_element`, `infinite_polynomial_ring`, `cyclotomic`, `complex_roots`, `convolution`, `polynomial_fateman`, `q_integer_valued_polynomials`, `integer_valued_polynomials`, `msolve`, `real_roots`, `refine_root`, `binary_form_reduce`. | ~12 | T03.1 | ✅ Done | infinite element: InfinitePolynomial base (36) + sparse/dense (12 each); ring: factory + 2 dict helpers + sparse/dense rings + InfinitePolynomialGen; cyclotomic_coeffs/value/bateman_bound; complex_roots; convolution FFT family; fateman; q/integer valued rings; msolve (groebner_basis_degrevlex, variety); real_roots (interval_bernstein hierarchy, ocean/island, real_roots, to_bernstein, ~40 helpers); refine_root; binary_form_reduce. |
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
