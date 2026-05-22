# Phase 09 — Combinatorics: Leaves & Foundations

**Tier:** 2
**Status:** ⬜ Not Started
**Depends on:** Phase 02
**Unblocks:** Phase 10, Phase 11, Phase 17 (parts)

## Goal

Cover the *root* of `sage.combinat/` — every `.py`/`.pyx` directly under
`sage-src/src/sage/combinat/` — plus the small leaf subpackages
(`chas/`, `cluster_algebra_quiver/`, `designs/`, `integer_lists/`,
`matrices/`, `ncsym/`, `species/`). Defers `sf/`, `ncsf_qsym/`,
`root_system/` to Phase 10, and `crystals/`, `posets/`, `words/`,
`rigged_configurations/`, `path_tableaux/` to Phase 11.

Many root files already have stubs (`binary_tree`, `combination`,
`composition`, `core`, `dyck_word`, `free_module`, `integer_vector`,
`ordered_tree`, `partition`, `partition_tuple`, `permutation`,
`plane_partition`, `ribbon_tableau`, `set_partition`,
`skew_partition`, `skew_tableau`, `subset`, `tableau`). These get audited
in T09.1.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T09.1 | **Existing leaf audit** — re-verify every existing combinat root stub for completeness against current Sage 10.7 source. No narrowing. | ~18 (audit only) | — | ⬜ | |
| T09.2 | **Permutations & symmetric group** — `affine_permutation`, `baxter_permutations`, `colored_permutations`, `decorated_permutation`, `permutation_cython`, `symmetric_group_algebra` (this lives at combinat root, not algebras), `symmetric_group_representations`. | 7 | T09.1 | ⬜ | |
| T09.3 | **Compositions / partitions extras** — `composition_signed`, `composition_tableau`, `partition_kleshchev`, `partition_shifting_algebras`, `partitions` (`.pyx`), `superpartition`, `vector_partition`, `multiset_partition_into_sets_ordered`. | 8 | T09.1 | ⬜ | |
| T09.4 | **Tableaux extras** — `k_tableau`, `lr_tableau`, `shifted_primed_tableau`, `super_tableau`, `tableau_residues`, `tableau_tuple`, `ribbon`, `ribbon_shaped_tableau`. | 8 | T09.1 | ⬜ | |
| T09.5 | **Trees & maps & SJT** — `abstract_tree`, `rooted_tree`, `tamari_blossoming_tree`, `tamari_lattices`, `nu_tamari_lattice`, `SJT`, `combinatorial_map`, `growth`, `hillman_grassl`. | 9 | T09.1 | ⬜ | |
| T09.6 | **Dyck/parking/words extras** — `nu_dyck_word`, `parking_functions`, `non_decreasing_parking_function`, `binary_recurrence_sequences`, `recognizable_series`, `regular_sequence`, `regular_sequence_bounded`. | 7 | T09.1 | ⬜ | |
| T09.7 | **Cluster / quiver / sequences** — `cluster_complex`, `cluster_algebra_quiver/` subpackage (7 files), `interval_posets`, `shard_order`, `kazhdan_lusztig`. | ~11 | T09.1 | ⬜ | |
| T09.8 | **Set partitions & extras** — `set_partition_iterator`, `set_partition_ordered`, `subsets_hereditary`, `subsets_pairwise`, `subword`, `subword_complex`, `subword_complex_c`, `t_sequences`, `tiling`, `sidon_sets`, `similarity_class_type`. | ~11 | T09.1 | ⬜ | |
| T09.9 | **Misc combinat root** — `algebraic_combinatorics`, `backtrack`, `bijectionist`, `catalog_partitions`, `combinat`, `combinat_cython`, `constellation`, `counting`, `cyclic_sieving_phenomenon`, `derangements`, `diagram`, `dlx`, `enumeration_mod_permgroup`, `enumerated_sets`, `e_one_star`, `expnums`, `family`, `fast_vector_partitions`, `finite_state_machine`, `finite_state_machine_generators`, `fully_commutative_elements`, `fully_packed_loop`, `gelfand_tsetlin_patterns`, `graph_path`, `gray_codes`, `hall_polynomial`. | ~26 | T09.1 | ⬜ | This task is the largest — *split into two commits* if it crosses 25 files. |
| T09.10 | **Remaining combinat root** — `integer_matrices`, `integer_vector_weighted`, `integer_vectors_mod_permgroup`, `key_polynomial`, `knutson_tao_puzzles`, `misc`, `necklace`, `output`, `parallelogram_polyomino`, `perfect_matching`, `q_analogues`, `q_bernoulli`, `quickref`, `ranker`, `restricted_growth`, `rsk`, `schubert_polynomial`, `shuffle`, `sine_gordon`, `six_vertex_model`, `sloane_functions`, `specht_module`, `tools`, `triangles_FHM`, `tuple`, `tutorial`, `yang_baxter_graph`, `debruijn_sequence`, `degree_sequences`, `restricted_growth`. | ~26 | T09.1 | ⬜ | Split if needed. |
| T09.11 | **Combinat algebras** — `descent_algebra` (also see Phase 06), `diagram_algebras`, `free_dendriform_algebra`, `free_prelie_algebra`, `fqsym`, `grossman_larson_algebras`, `partition_algebra`, `blob_algebra`. | 8 | T09.1 | ⬜ | Cross-listed with Phase 06 — pick whichever phase lands first; remove from the other's task. |
| T09.12 | **Combinat: chas, integer_lists, matrices, ncsym, species, designs** — leaf subpackages. | ~5+5+5+4+19+24=~62 | T09.1 | ⬜ | Split into 3–4 commits along subpackage boundaries: (a) chas+ncsym+integer_lists, (b) matrices+species, (c) designs (24 files — one commit on its own). |

## Parallelism

- T09.1 first. T09.2–T09.12 mostly independent thereafter.
- T09.11 coordinate with Phase 06 to avoid double work.
- T09.12 is the heaviest — split it across multiple agents along the
  sub-subpackage seams.

## Risks

- `partition.py` has hundreds of method definitions inherited via
  `CombinatorialClass`; verify direct definition (AGENTS.md anti-inflation).
- `set_partition_iterator.pyx` is mostly internal — confirm public surface.
- `family.py` is heavily used by category infrastructure — must align with
  Phase 01 `sets.family` stub.
