# Phase 08 — Groups

**Tier:** 2
**Status:** ⬜ Not Started
**Depends on:** Phase 02, Phase 05
**Unblocks:** Phase 10 (parts), Phase 11, Phase 14, Phase 17

## Goal

Cover `sage.groups/`. Several subdirs already have a thin stub footprint
that must be expanded.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T08.1 | **Groups root** — `group`, `generic`, `group_exp`, `group_semidirect_product`, `class_function`, `kernel_subgroup`, `indexed_free_group`, `fqf_orthogonal`, `groups_catalog`. | ~9 | — | ⬜ | |
| T08.2 | **Conjugacy & galois** — `conjugacy_classes`, `galois_group`, `galois_group_perm`. | 3 | — | ⬜ | `conjugacy_classes` and `galois_group` have existing stubs. |
| T08.3 | **Braid / Artin / Cubic braid / Cactus** — `braid`, `artin`, `cubic_braid`, `cactus_group`. | 4 | — | ⬜ | |
| T08.4 | **Free / finitely presented** — `free_group`, `finitely_presented`, `finitely_presented_catalog`, `finitely_presented_named`. | 4 | — | ⬜ | `free_group` and `finitely_presented` have existing stubs. |
| T08.5 | **Libgap interop** — `libgap_group`, `libgap_mixin`, `libgap_morphism`, `libgap_wrapper`. | 4 | T08.1 | ⬜ | Forward-ref `sage.libs.gap` (Phase 18). |
| T08.6 | **Permutation groups** — `perm_gps/` subdir (22 files). | ~22 | — | ⬜ | `permgroup` and `permgroup_element` have existing stubs. |
| T08.7 | **Matrix groups** — `matrix_gps/` subdir (23 files). | ~23 | T05.1 | ⬜ | `matrix_group`, `linear`, `orthogonal`, `symplectic`, `unitary` have existing stubs. |
| T08.8 | **Abelian groups** — `abelian_gps/` subdir (10 files). | 10 | — | ⬜ | `abelian_group` has existing stub. |
| T08.9 | **Additive abelian** — `additive_abelian/` subdir (5 files). | 5 | — | ⬜ | |
| T08.10 | **Affine / Lie / Misc / Semimonomial** — `affine_gps/` (5), `lie_gps/` (3), `misc_gps/` (5), `semimonomial_transformations/` (3). | ~16 | — | ⬜ | Group in one phase commit per subdir, or bundle small ones. |

## Parallelism

- T08.6 and T08.7 are large and independent of each other. Assign to
  separate agents.
- T08.1–T08.5 are independent — parallel.
- T08.8–T08.10 are independent — parallel.

## Risks

- `libgap_wrapper.pyx` has dynamic dispatch into GAP; signatures need
  precise `object` opacity at the GAP boundary, never `Any`.
- `permgroup_element.pyx` has overloaded `__mul__` for group action on
  many types — `@overload`.
