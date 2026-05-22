# Phase 13 — Schemes & Dynamics

**Tier:** 4
**Status:** ⬜ Not Started
**Depends on:** Phase 04, Phase 12
**Unblocks:** Phase 14 (parts)

## Goal

Cover `sage.schemes/` and `sage.dynamics/`. Existing stubs cover
`affine/`, `projective/`, and parts of `elliptic_curves/`.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T13.1 | **Schemes generic** — `schemes/generic/` subpackage (12 files): `algebraic_scheme`, `ambient_space`, `divisor`, `divisor_group`, `homset`, `hypersurface`, `morphism`, `point`, `scheme`, `spec`, `glue`, `notion`. | 12 | — | ⬜ | |
| T13.2 | **Affine schemes** — audit existing `affine_space`, `affine_subscheme`. Add `affine_homset`, `affine_morphism`, `affine_point`, `affine_rational_point`, `affine_curve`, `affine_jacobian`. | ~7 | — | ⬜ | |
| T13.3 | **Projective schemes** — audit existing `projective_space`, `projective_subscheme`. Add `projective_homset`, `projective_morphism`, `projective_point`, `projective_rational_point`, `proj_bdd_height_iterator`. | ~6 | — | ⬜ | |
| T13.4 | **Product projective** — `product_projective/` subpackage (7 files). | 7 | — | ⬜ | |
| T13.5 | **Weighted projective** — `weighted_projective/` subpackage (5 files). | 5 | — | ⬜ | |
| T13.6 | **Toric schemes** — `toric/` subpackage (18 files). Split into two commits: (a) `divisor`, `divisor_class`, `homset`, `morphism`, `toric_subscheme`, `variety` (~9), (b) `chow_group`, `fano_variety`, `ideal`, `library`, `points`, `sheaf/`, `weierstrass*` (~9). | ~18 (two commits) | — | ⬜ | |
| T13.7 | **Elliptic curves: foundations** — audit `constructor`, `ell_field`, `ell_finite_field`, `ell_generic`, `ell_number_field`, `ell_point`, `ell_rational_field`. | 7 (audit) | — | ⬜ | |
| T13.8 | **Elliptic curves: heights, isogeny, mod, padic** — `height`, `heegner`, `hom`, `hom_composite`, `hom_velusqrt`, `isogeny_class`, `isogeny_small_degree`, `kraus`, `kodaira_symbol`, `mod_poly`, `mod5family`, `modular_parametrization`. | ~12 | T13.7 | ⬜ | |
| T13.9 | **Elliptic curves: residue** — remaining files from `elliptic_curves/` (55 total) including `period_lattice`, `period_lattice_region`, `padics`, `ell_torsion`, `ell_curve_isogeny`, `cm`, `cardinality`, `gal_reps`, `gal_reps_number_field`, `ell_egros`, `ell_local_data`, `ell_tate_curve`. | ~12 | T13.7 | ⬜ | |
| T13.10 | **Hyperelliptic curves** — `hyperelliptic_curves/` subpackage (23 files). Split into two commits along (a) constructor/generic/finite_field/padic/rational_field, (b) jacobian/mestre/monsky_washnitzer/kummer_surface. | ~23 (two commits) | — | ⬜ | |
| T13.11 | **Curves general** — `curves/` subpackage (10 files): `affine_curve`, `closed_point`, `constructor`, `curve`, `point`, `projective_curve`, `zariski_vankampen`. | 10 | T13.2, T13.3 | ⬜ | |
| T13.12 | **Plane conics / quartics / cyclic covers / berkovich / jacobians / riemann_surfaces** — `plane_conics/` (7), `plane_quartics/` (3), `cyclic_covers/` (5), `berkovich/` (3), `jacobians/` (2), `riemann_surfaces/` (2). | ~22 | T13.1 | ⬜ | Bundle into 2–3 commits along subpackage seams. |
| T13.13 | **Dynamics root** — `dynamics/arithmetic_dynamics/` (audit existing `affine_ds`, `projective_ds`; add `berkovich_ds`, `dynamical_semigroup`, `endPN_automorphism_group`, `endPN_minimal_model`, `generic_ds`, `height`, `product_projective_ds`, `wehlerk3`). | ~9 | T13.2, T13.3 | ⬜ | |
| T13.14 | **Dynamics: complex / cellular** — `complex_dynamics/mandel_julia` (existing), plus `arithmetic_dynamics/affine_ds`, residue of `dynamics/` (cellular automata, finite/sandpile, deformation). | ~7 | — | ⬜ | |

## Parallelism

- T13.1 first. Then T13.2–T13.6, T13.7, T13.10, T13.12 in parallel.
- T13.8, T13.9 chain after T13.7. T13.11 needs T13.2 and T13.3.
- T13.13, T13.14 independent.

## Risks

- Elliptic curve methods have heavy overloading (`P + Q`, `2 * P`, etc.).
  Use `@overload` aggressively.
- Toric variety code uses `Variety` and `Polyhedron` interchangeably —
  align with Phase 12 outputs.
