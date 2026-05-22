# Phase 14 — Modular Forms & Hecke Modules

**Tier:** 4
**Status:** ⬜ Not Started
**Depends on:** Phase 04, Phase 05
**Unblocks:** Phase 17 (parts)

## Goal

Cover `sage.modular/`. Existing stubs cover `hecke/*`, `modsym/*`,
`modform/element`, `modform/space`, `modform/eis_series`, `arithgroup/*`,
`abvar/abvar`, `btquotients/btquotient`, `cusps`, `dirichlet`.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T14.1 | **Modular root** — `cusps`, `cusps_nf`, `dims`, `dirichlet`, `etaproducts`, `multiple_zeta`, `multiple_zeta_F_algebra`. | 7 | — | ⬜ | `cusps` and `dirichlet` have existing stubs. |
| T14.2 | **Arithgroup** — audit existing 6 stubs; complete `arithgroup_element`, `arithgroup_perm`, `congroup`, `congroup_gamma`, `congroup_generic`, `farey_symbol`, `tests`. | ~7 | — | ⬜ | |
| T14.3 | **Modular forms: ambient & spaces** — audit existing `space`, `element`, `eis_series`. Add `ambient`, `ambient_R`, `ambient_eps`, `ambient_g0`, `ambient_g1`, `constructor`, `cuspidal_submodule`, `eisenstein_submodule`, `submodule`, `ring`. | ~13 | — | ⬜ | |
| T14.4 | **Modular forms: invariants** — `eis_series_cython`, `half_integral`, `j_invariant`, `l_series_gross_zagier`, `l_series_gross_zagier_coeffs`, `hecke_operator_on_qexp`, `numerical`, `periods`, `theta`, `vm_basis`, `weight1`, `defaults`. | ~12 | T14.3 | ⬜ | |
| T14.5 | **Modular symbols** — audit existing `ambient`, `element`, `hecke_operator`, `modsym`, `space`, `subspace`. Add `apply`, `boundary`, `g1list`, `ghlist`, `heilbronn`, `manin_symbol`, `manin_symbol_list`, `modular_symbols`, `p1list`, `p1list_nf`, `relation_matrix`, `relation_matrix_pyx`. | ~13 | T14.3 | ⬜ | |
| T14.6 | **Hecke modules** — audit existing `algebra`, `ambient_module`, `element`, `hecke_operator`, `module`, `morphism`, `submodule`. Add `degenmap`, `homspace`. | ~4 | — | ⬜ | |
| T14.7 | **Abelian varieties** — `abvar/` subpackage (13 files): audit existing `abvar`. Add `abvar_ambient_jacobian`, `abvar_endomorphism`, `abvar_newform`, `constructor`, `cuspidal_subgroup`, `finite_subgroup`, `homology`, `homspace`, `lseries`, `morphism`, `torsion_subgroup`, `torsion_point`. | ~13 | T14.1 | ⬜ | |
| T14.8 | **BT quotients** — `btquotients/` subpackage (3 files): audit existing `btquotient`, add `pautomorphicform`, `interface`. | 3 | — | ⬜ | |
| T14.9 | **Modular forms Hecke triangle** — `modform_hecketriangle/` subpackage (15 files): `abstract_ring`, `abstract_space`, `analytic_type`, `constructor`, `element`, `functors`, `graded_ring`, `graded_ring_element`, `hecke_triangle_group_element`, `hecke_triangle_groups`, `readme`, `series_constructor`, `space`, `subspace`, `theta_blocks`. | ~14 | T14.3 | ⬜ | |
| T14.10 | **Drinfeld modular forms** — `drinfeld_modform/` subpackage (5 files). | 5 | — | ⬜ | |
| T14.11 | **Local components & overconvergent** — `local_comp/` (5), `overconvergent/` (4). | 9 | T14.3 | ⬜ | |
| T14.12 | **Pollack-Stevens, quasimodform, quatalg, ssmod** — `pollack_stevens/` (9), `quasimodform/` (3), `quatalg/` (2), `ssmod/` (2). | ~16 | T14.3, T14.7 | ⬜ | Bundle into 2 commits. |

## Parallelism

- T14.1, T14.2, T14.6, T14.7, T14.8, T14.10 mutually independent.
- T14.3 first within modform; T14.4, T14.5, T14.9, T14.11, T14.12 chain
  after T14.3.

## Risks

- Modular symbols code has many `M[...]` element-fetching overloads —
  represent as `@overload` on `__getitem__`.
- Hecke triangle and overconvergent forms depend on lazy series — Phase
  02 (T02.8) must land first.
