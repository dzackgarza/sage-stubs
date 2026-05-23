# Phase 04 — Number-Theoretic Rings

**Tier:** 1
**Status:** ⬜ Not Started
**Depends on:** Phase 01
**Unblocks:** Phase 13, 14, 17

## Goal

Cover `sage.rings.number_field/`, `sage.rings.padics/`,
`sage.rings.finite_rings/`, `sage.rings.function_field/`,
`sage.rings.valuation/`, `sage.rings.asymptotic/`, `sage.rings.semirings/`,
`sage.rings.bernmm/`. Several have a thin existing stub footprint that must
be audited and expanded, not rewritten.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T04.1 | **Finite rings: element types** — `element_base`, `element_givaro`, `element_ntl_gf2e`, `element_pari_ffelt`, `integer_mod`. | 5 | — | ⬜ | `integer_mod` has an existing stub. |
| T04.2 | **Finite rings: fields & rings** — `finite_field_base`, `finite_field_constructor`, `finite_field_givaro`, `finite_field_ntl_gf2e`, `finite_field_pari_ffelt`, `finite_field_prime_modn`, `integer_mod_ring`. | 7 | T04.1 | ⬜ | All have existing stubs except `ntl_gf2e`. |
| T04.3 | **Finite rings: homs & residue fields** — `hom_finite_field`, `hom_finite_field_givaro`, `hom_prime_finite_field`, `homset`, `galois_group`, `maps_finite_field`, `residue_field`, `residue_field_givaro`, `residue_field_ntl_gf2e`, `residue_field_pari_ffelt`, `conway_polynomials`, `algebraic_closure_finite_field`. | ~12 | T04.2 | ⬜ | `algebraic_closure_finite_field` lives at `sage.rings/` root. |
| T04.4 | **Number field core** — `number_field`, `number_field_base`, `number_field_element`, `number_field_element_base`, `number_field_element_quadratic`, `number_field_ideal`, `number_field_ideal_rel`, `number_field_rel`, `number_field_morphisms`, `morphism`. | ~10 | — | ⬜ | All have existing stubs — audit. |
| T04.5 | **Number field auxiliaries** — `order`, `order_ideal`, `unit_group`, `class_group`, `galois_group`, `homset`, `maps`, `structure`, `selmer_group`, `bdd_height`, `S_unit_solver`, `splitting_field`, `small_primes_of_degree_one`. | ~13 | T04.4 | ⬜ | `order` and `galois_group` have existing stubs. |
| T04.6 | **Number field: totally real / Kuni** — `totallyreal`, `totallyreal_data`, `totallyreal_rel`, `totallyreal_phc`. | 4 | T04.4 | ⬜ | |
| T04.7 | **p-adic generic infrastructure** — `padic_generic`, `padic_generic_element`, `padic_base_generic`, `padic_base_leaves`, `padic_extension_generic`, `padic_extension_leaves`, `local_generic`, `local_generic_element`, `generic_nodes`, `factory`, `misc`. | ~11 | — | ⬜ | Five have existing stubs — audit. |
| T04.8 | **p-adic element implementations** — `padic_capped_absolute_element`, `padic_capped_relative_element`, `padic_fixed_mod_element`, `padic_floating_point_element`, `padic_ext_element`, `padic_ZZ_pX_element`, `padic_ZZ_pX_CA_element`, `padic_ZZ_pX_CR_element`, `padic_ZZ_pX_FM_element`, `padic_relaxed_element`, `padic_lattice_element`. | ~11 | T04.7 | ⬜ | `padic_ZZ_pX_element` has an existing stub. |
| T04.9 | **p-adic q-adic flint variants** — `qadic_flint_CA`, `qadic_flint_CR`, `qadic_flint_FM`, `qadic_flint_FP`, `relative_extension_leaves`, `relative_ramified_CA`, `relative_ramified_CR`, `relative_ramified_FM`, `relative_ramified_FP`, `eisenstein_extension_generic`, `unramified_extension_generic`. | ~11 | T04.7 | ⬜ | |
| T04.10 | **p-adic auxiliaries** — `padic_valuation`, `padic_printing`, `lattice_precision`, `precision_error`, `pow_computer`, `pow_computer_ext`, `pow_computer_flint`, `pow_computer_relative`, `witt_vector`, `witt_vector_ring`, `tutorial`, `morphism`, `common_conversion`. | ~13 | T04.7 | ⬜ | |
| T04.11 | **Function field core** — `function_field`, `function_field_polymod`, `function_field_rational`, `element`, `element_polymod`, `element_rational`, `constructor`. | 7 | — | ⬜ | All have existing stubs except `function_field_polymod` / `_rational`. |
| T04.12 | **Function field morphisms / orders / ideals / places** — `maps`, `order`, `order_basis`, `order_polymod`, `order_rational`, `ideal`, `ideal_polymod`, `ideal_rational`, `place`, `place_polymod`, `place_rational`, `extensions`, `divisor`. | ~13 | T04.11 | ⬜ | |
| T04.13 | **Function field differentials / derivations / valuation / Jacobian** — `differential`, `derivations`, `derivations_polymod`, `derivations_rational`, `valuation`, `valuation_ring`, `jacobian_base`, `jacobian_hess`, `jacobian_khuri_makdisi`, `jacobian_unique_hess`, `hermite_form_polynomial`, `riemann_roch`, `khuri_makdisi`. | ~13 | T04.11 | ⬜ | |
| T04.14 | **Function field: drinfeld_modules subpackage** — full subdir. | ~6 | T04.11 | ⬜ | |
| T04.15 | **Valuation subpackage** — `valuation`, `augmented_valuation`, `developing_valuation`, `gauss_valuation`, `inductive_valuation`, `limit_valuation`, `mapped_valuation`, `scaled_valuation`, `trivial_valuation`, `valuation_space`, `valuations_catalog`, `value_group`. | ~12 | — | ⬜ | `valuation` has existing stub. |
| T04.16 | **Asymptotic ring subpackage** — `asymptotic_ring`, `asymptotic_expansion_generators`, `asymptotics_multivariate_generating_functions`, `growth_group`, `growth_group_cartesian`, `term_monoid`, `misc`. | 7 | — | ⬜ | `asymptotic_ring` has existing stub. |
| T04.17 | **Semirings & remaining** — `semirings/` subdir, plus anything else surveyed in Phase 1 audit that lives at `sage.rings/` root but wasn't covered in Phase 02 (e.g. `noncommutative_ideals`, `species`, `cfinite_sequence`). | ~6 | — | ⬜ | |

## Parallelism

- All four subtrees (finite_rings, number_field, padics, function_field)
  are mutually independent — assign one per agent.
- Within each subtree, the chain is core → element implementations →
  auxiliaries (see Depends column).

## Risks

- p-adic stubs touch C-level flint pow computers; signature drift between
  template `.pxi` files is common. Stick to the public `.pyx` surface.
- Number field stubs reference `sage.libs.pari` — those stubs come in
  Phase 18. Add direct imports only after the minimal source-backed support
  stub exists; quoted/string type references are banned.
- `STUB_GAPS.md` blockers concerning finite fields are partially resolved;
  re-check after T04.2 lands.
