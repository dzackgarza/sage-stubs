# Phase 11 — Combinatorics: Crystals, Posets, Words, Tableaux Extras

**Tier:** 3
**Status:** ⬜ Not Started
**Depends on:** Phase 09
**Unblocks:** none (terminal in this branch)

## Goal

Cover the remaining `sage.combinat/` subpackages:
`crystals/`, `posets/`, `words/`, `rigged_configurations/`,
`path_tableaux/`. The existing thin stubs (`crystals/crystals`,
`crystals/letters`, `crystals/tensor_product`, `posets/posets`,
`posets/lattices`, `posets/hasse_diagram`, `words/word`,
`words/abstract_word`, `words/finite_word`) must be audited and expanded.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T11.1 | **Crystals: foundations** — `crystals`, `letters`, `tensor_product`, plus `affine`, `affine_factorization`, `affinization`, `alcove_path`, `bkk_crystals`, `crystal_of_words`. | ~10 | — | ⬜ | First three exist — audit. |
| T11.2 | **Crystals: classical & types** — `direct_sum`, `elementary_crystals`, `fast_crystals`, `fully_commutative_stable_grothendieck`, `generalized_young_walls`, `highest_weight_crystals`, `induced_from_crystals`, `infinity_crystals`, `littelmann_path`. | ~9 | T11.1 | ⬜ | |
| T11.3 | **Crystals: kirillov / kyoto / monomial / mv** — `kac_modules/`, `kirillov_reshetikhin`, `kyoto_path_model`, `monomial_crystals`, `mv_polytopes`, `multisegments`, `polyhedral_realization`, `pbw_crystal`. | ~8 | T11.1 | ⬜ | |
| T11.4 | **Crystals: spins / star / sub / tensor variants / virtual** — `spins`, `star_crystal`, `subcrystal`, `tensor_product_element`, `virtual_crystal`, plus any remaining `crystals/` leaves. | ~6 | T11.1 | ⬜ | The `crystals/` dir has 36 files — split if needed. |
| T11.5 | **Posets: foundations** — audit `posets`, `lattices`, `hasse_diagram`. Add `bubble_shuffle`, `cartesian_product`, `d_complete`, `elements`, `forest`, `incidence_algebras`, `linear_extensions`, `linear_extension_iterator`, `mobile`, `moebius_algebra`, `poset_examples`, `posets_catalog`, `poset_lattice`. | ~16 | — | ⬜ | First three exist; 19 files in `posets/` total. |
| T11.6 | **Words: foundations** — audit `word`, `abstract_word`, `finite_word`. Add `infinite_word`, `word_char`, `word_datatypes`, `word_generators`, `word_infinite_datatypes`, `word_options`, `lyndon_word`, `morphic`, `paths`, `shuffle_product`, `suffix_trees`, `word_subword`, `alphabet`, `words`. | ~17 | — | ⬜ | 18 files total. |
| T11.7 | **Rigged configurations** — `rigged_configurations/` subpackage (23 files). Split into two commits: (a) core rigged configurations + Bijection (~12), (b) Kleber tree + tensor product + crystal RC bijections (~11). | ~23 (two commits) | T11.1 | ⬜ | |
| T11.8 | **Path tableaux** — `path_tableaux/` subpackage (6 files). | 6 | — | ⬜ | |

## Parallelism

- T11.1 first within crystals; T11.2–T11.4 in parallel.
- T11.5, T11.6, T11.7, T11.8 mutually independent.

## Risks

- Crystals subclasses are deep; AGENTS.md "no inherited-method inflation"
  is the main hazard. Re-verify each method is direct on the class.
- `STUB_GAPS.md` Posets blocker affects the *category* surface, not the
  `combinat.posets/` subpackage — but the override-variance issue is the
  same shape, so use precise element types when stubbing direct methods.
