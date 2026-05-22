# Phase 10 — Combinatorics: Symmetric Functions & Root Systems

**Tier:** 3
**Status:** ⬜ Not Started
**Depends on:** Phase 09
**Unblocks:** Phase 17 (parts)

## Goal

Cover `sage.combinat.sf/`, `sage.combinat.ncsf_qsym/`,
`sage.combinat.root_system/`. Several existing stubs cover the most-used
bases (`schur`, `monomial`, `powersum`, `elementary`, `homogeneous`,
`jack`, `hall_littlewood`, `macdonald`, `llt`, `dual`, `witt`, `sfa`,
`root_system`, `weyl_group`, `coxeter_group`, `ambient_space`,
`weight_space`, `weight_lattice_realizations`,
`root_lattice_realizations`, `cartan_type`, `branching_rules`, `ncsf`,
`qsym`).

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T10.1 | **Symmetric functions: audit existing** — `sfa`, `schur`, `monomial`, `powersum`, `elementary`, `homogeneous`, `jack`, `hall_littlewood`, `macdonald`, `llt`, `dual`, `witt`. | 12 (audit) | — | ⬜ | Existing stubs — extend, don't narrow. |
| T10.2 | **Symmetric functions: gaps** — remaining sf module files not yet stubbed: `character`, `classical`, `kfpoly`, `kschur`, `multiplicative`, `new_kschur`, `ns_macdonald`, `orthogonal`, `orthotriang`, `schur_e`, `symplectic`. | ~11 | T10.1 | ⬜ | |
| T10.3 | **Symmetric functions: misc** — any remaining `sf/` leaves (verify in Phase-1 audit; possibly `k_dual`, `k_dual_morphism`). | ~3 | T10.1 | ⬜ | |
| T10.4 | **NCSF / QSym / NCSym** — audit `ncsf`, `qsym`; complete `combinatorial_hopf_algebras`, `tutorial`, `generic_basis_code`, `ncsf_qsym/`-root files. Plus `ncsym/` subpackage (4 files). | ~10 | — | ⬜ | |
| T10.5 | **chas / characteristic algebras** — `combinat.chas/` subpackage (3 files). | 3 | — | ⬜ | May overlap with Phase 09 T09.12; pick one. |
| T10.6 | **Root system: audit existing** — `root_system`, `weyl_group`, `coxeter_group`, `ambient_space`, `weight_space`, `weight_lattice_realizations`, `root_lattice_realizations`, `cartan_type`, `branching_rules`. | 9 (audit) | — | ⬜ | |
| T10.7 | **Root system: Cartan / Dynkin / type families** — `cartan_matrix`, `dynkin_diagram`, `type_*` modules (`type_A`, `type_B`, `type_C`, `type_D`, `type_E`, `type_F`, `type_G`, `type_BC_affine`, `type_dual`, `type_folded`, `type_reducible`, `type_relabel`, `type_super_A`, `type_affine`, `type_marked`, `type_indefinite`). | ~17 | T10.6 | ⬜ | |
| T10.8 | **Root system: roots / weights / words** — `root_space`, `coroot_space`, `coroot_lattice_realizations`, `extended_affine_weyl_group`, `pieri_factors`, `plot`, `non_symmetric_macdonald_polynomials`, `reflection_group_complex`, `reflection_group_real`, `reflection_group_element`. | ~10 | T10.6 | ⬜ | |
| T10.9 | **Root system: Weyl & fundamental groups** — `fundamental_group`, `hecke_algebra_representation`, `integrable_representations`, `weyl_characters`, `weyl_group_action`. | ~5 | T10.6 | ⬜ | |
| T10.10 | **Root system: residue** — anything left from the 57 `root_system/` files. | ~6 | T10.6 | ⬜ | |

## Parallelism

- T10.1 / T10.6 audit tasks first. Then T10.2/T10.3, T10.4, T10.5,
  T10.7–T10.10 can run in parallel.

## Risks

- Type-A,B,C,…,G modules subclass with deep MRO chains; preserve them
  exactly (AGENTS.md no-flattening rule).
- `reflection_group_complex.py` interacts with GAP-backed groups —
  forward-reference `sage.libs.gap` rather than importing.
