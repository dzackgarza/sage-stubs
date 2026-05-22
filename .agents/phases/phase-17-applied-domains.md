# Phase 17 — Applied Domains

**Tier:** 3
**Status:** ⬜ Not Started
**Depends on:** Phase 02, Phase 05
**Unblocks:** none

## Goal

Cover the applied-mathematics subpackages: `coding/`, `crypto/`,
`lfunctions/`, `quadratic_forms/`, `matroids/`, `quivers/`, `knots/`,
`monoids/`, `sandpiles/`, `game_theory/`, `games/`. Existing stubs are
thin (`coding`: 4, `lfunctions`: 4; rest: 0).

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T17.1 | **Coding: foundations** — audit existing `decoder`, `encoder`, `linear_code`. Add `abstract_code`, `bch_code`, `binary_code`, `bounds`, `channel`, `code_bounds`, `code_constructions`, `codecan/`, `cyclic_code`, `extended_code`, `golay_code`. | ~12 | — | ⬜ | |
| T17.2 | **Coding: GRS / hamming / linear** — `grs_code`, `guruswami_sudan/`, `hamming_code`, `kasami_codes`, `linear_code_no_metric`, `linear_rank_metric`, `parity_check_code`, `punctured_code`, `reed_muller_code`, `relative_finite_field_extension`. | ~10 | T17.1 | ⬜ | |
| T17.3 | **Coding: source / subfield / two_weight** — `source_coding/`, `subfield_subcode`, `two_weight_db`, `linear_code_test`, `databases`. Plus residue from the 46 files. | ~10 | T17.1 | ⬜ | |
| T17.4 | **Coding: GRS Cython algorithms** — `binary_code.pyx`, `codecan/codecan.pyx`, `codecan/autgroup_can_label.pyx`, etc. | ~8 | T17.1 | ⬜ | |
| T17.5 | **Crypto** — `crypto/` subpackage (28 files): split into 2 commits along (a) classical / public_key / mq, (b) lwe / boolean / lattice. | ~28 (two commits) | — | ⬜ | |
| T17.6 | **L-functions** — audit existing `dokchitser`, `lcalc`, `zero_sums`. Add `pari`, `sympow`, plus leaves. | ~5 | — | ⬜ | |
| T17.7 | **Quadratic forms** — `quadratic_forms/` (34 files): split into 2 commits along (a) base / definite / ternary, (b) genera/, count_local, mass, special_form, theta. | ~34 (two commits) | — | ⬜ | |
| T17.8 | **Matroids** — `matroids/` (28 files): split into 2 commits along (a) basis / circuit / dual / linear_matroid / matroid, (b) advanced + extension. | ~28 (two commits) | — | ⬜ | |
| T17.9 | **Quivers** — `quivers/` (8 files): `algebra`, `algebra_elements`, `homspace`, `morphism`, `path_semigroup`, `paths`, `representation`. | 8 | T06.1 | ⬜ | |
| T17.10 | **Knots** — `knots/` (6 files): `gauss_code`, `knot`, `knotinfo`, `link`, `__init__`. | 6 | — | ⬜ | |
| T17.11 | **Monoids** — `monoids/` (12 files): `automatic_semigroup`, `free_abelian_monoid`, `free_abelian_monoid_element`, `free_monoid`, `free_monoid_element`, `hecke_monoid`, `indexed_free_monoid`, `monoid`, `string_monoid`, `string_monoid_element`, `string_ops`, `trace_monoid`. | 12 | T02.5 | ⬜ | |
| T17.12 | **Sandpiles / game_theory / games** — `sandpiles/sandpile` (2 files), `game_theory/` (6 files), `games/` (4 files). | ~12 | — | ⬜ | Bundle as one commit. |

## Parallelism

- Every task is independent of every other within this phase (no internal
  T-dependencies except T17.9 lightly on Phase 06 algebras). Parallelise
  freely.

## Risks

- `linear_code.py` and `abstract_code.py` have many inherited methods —
  audit direct definitions only.
- Crypto modules use `randint` heavily — return `int`, not `Integer`,
  where Python `random` is the source.
- `quadratic_forms/genera/` has many small helper modules; verify each
  has public surface before stubbing.
