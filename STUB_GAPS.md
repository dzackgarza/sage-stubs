# Sidecar Stub Gaps

This file tracks real `category_specs` diagnostics that need `sage-stubs`
work. A candidate belongs here only when a fresh consumer run shows the
diagnostic and Sage 10.7 source identifies the corresponding provider or
interface surface.

## Ready Candidates

None currently passed the real-consumer regression gate.

## Resolved Candidates

### `sage.categories.finite_fields.FiniteFields.__contains__`

Fresh baseline:
`.mypy_cache/category-specs-error-classification/raw_errors_sets_enum_batch2_fresh.txt`
reported:

```text
category_specs/rings/subcategories/finite_field.py:43:
Unsupported right operand type for in ("FiniteFields")
```

Sage 10.7 source defines `FiniteFields.__contains__` directly at
`sage-src/src/sage/categories/finite_fields.py:69`.

The sidecar now declares:

```python
class FiniteFields:
    def __contains__(self, x: object) -> bool: ...
```

Fresh validation with `raw_errors_finite_fields_contains_fresh.txt` removed
the `finite_field.py:43` diagnostic. The remaining finite-field diagnostics at
lines 47 and 54 were unchanged.

## Blocked Candidates

### `category_specs` local override bases, not missing Sage sidecars

Fresh ledger:
`reports/workstreams/category-specs-mypy-ledger/latest.json` reports
`override` diagnostics under the `missing sidecar ordinary signature` owner
for several project-local `ParentMethods` classes. These rows look like
missing Sage methods, but the affected override base is the local
`category_specs` provider class, not the concrete Sage class that owns the
method.

For `category_specs/rings/subcategories/rational_field.py`, the current
`sage-stubs/rings/rational_field.pyi` already declares the source-backed
surface for `RationalField`, including `algebraic_closure`, `degree`,
`absolute_degree`, `signature`, `discriminant`, `absolute_discriminant`,
`automorphisms`, `class_number`, `power_basis`, `places`, and
`maximal_order`. Sage 10.7 defines these directly at
`sage-src/src/sage/rings/rational_field.py:541`, `:552`, `:574`, `:585`,
`:623`, `:638`, `:939`, `:950`, `:1007`, `:1034`, and `:1073`.

- Searched: current `category_specs` ledger; `/home/dzack/research/category_specs/rings/subcategories/rational_field.py`; `sage-stubs/rings/rational_field.pyi`; Sage 10.7 `sage-src/src/sage/rings/rational_field.py`.
- Found: the Sage source and stub contain the key `RationalField` methods, while the downstream diagnostics are `@override` failures on a local nested `ParentMethods` class.
- Conclusion: inference — the remaining `rational_field.py` rows are local category-provider inheritance/design rows, not missing ordinary `RationalField` sidecar methods.
- Confidence: High.
- Gaps: Some number-field-style methods in that file may still need separate source review, especially rows delegated through `as_number_field()`.

For `category_specs/sets/subcategories/image.py:116` and
`category_specs/sets/subcategories/real_set.py:205`, the ordinary Sage
sidecars already expose `_an_element_`:
`sage-stubs/sets/image_set.pyi:36` and `sage-stubs/sets/real_set.pyi:109`.
Sage 10.7 defines the corresponding methods at
`sage-src/src/sage/sets/image_set.py:401` and
`sage-src/src/sage/sets/real_set.py:2348`.

- Searched: current `category_specs` ledger; `sage-stubs/sets/image_set.pyi`; `sage-stubs/sets/real_set.pyi`; Sage 10.7 `sage-src/src/sage/sets/image_set.py` and `sage-src/src/sage/sets/real_set.py`.
- Found: both ordinary sidecars and both Sage source files already define `_an_element_`.
- Conclusion: inference — these two rows are local wrapper/provider inheritance rows, not missing ordinary `image_set` or `real_set` sidecar methods.
- Confidence: High.
- Gaps: This does not classify other `ImageSubobject` or `RealSet` argument/return variance diagnostics.

For `category_specs/modules/subcategories/free.py`, Sage 10.7 defines the
finite-rank free-module methods directly on
`sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule_abstract`:
`exterior_power` at `:1618`, `alternating_form` at `:2369`,
`default_basis` at `:2759`, `set_default_basis` at `:2797`, and `bases` at
`:2873`.

- Searched: current `category_specs` ledger; Sage 10.7 `sage-src/src/sage/tensor/modules/finite_rank_free_module.py`; an isolated local sidecar experiment for `sage-stubs/tensor/modules/finite_rank_free_module.pyi`.
- Found: Sage defines the requested methods, but the isolated sidecar experiment changed the downstream ordinary error count from `1816` to `1824` and did not clear the targeted local override rows.
- Conclusion: inference — the current `free.py` override rows depend on local wrapper/provider inheritance and constructor modeling, not just the absence of an importable finite-rank module sidecar.
- Confidence: Medium.
- Gaps: A full finite-rank module sidecar may still be needed later, but it must model constructors and category provider bases before it can be a clean issue #5 fix.

### `sage.categories.posets.Posets.ParentMethods`

Fresh baseline:
`.mypy_cache/category-specs-error-classification/raw_errors_sets_enum_batch2_fresh.txt`
reports missing-base errors for:

- `category_specs/posets/__init__.py:88` — `le`
- `category_specs/posets/__init__.py:94` — `lt`
- `category_specs/posets/__init__.py:100` — `ge`
- `category_specs/posets/__init__.py:106` — `gt`
- `category_specs/posets/__init__.py:113` — `upper_covers`
- `category_specs/posets/__init__.py:120` — `lower_covers`
- `category_specs/posets/__init__.py:127` — `order_ideal`
- `category_specs/posets/__init__.py:134` — `order_filter`

Sage 10.7 source defines those methods directly on
`sage.categories.posets.Posets.ParentMethods` at:

- `sage-src/src/sage/categories/posets.py:160`
- `sage-src/src/sage/categories/posets.py:179`
- `sage-src/src/sage/categories/posets.py:201`
- `sage-src/src/sage/categories/posets.py:223`
- `sage-src/src/sage/categories/posets.py:246`
- `sage-src/src/sage/categories/posets.py:259`
- `sage-src/src/sage/categories/posets.py:272`
- `sage-src/src/sage/categories/posets.py:290`

Blocked because the source methods are unannotated over the element type of
the poset. A minimal `object`-typed sidecar patch passed stub syntax checks but
regressed the fresh consumer capture:

```text
843 raw_errors_sets_enum_batch2_fresh.txt
928 raw_errors_posets_object_wheel_fresh.txt
```

It converted blind missing-base errors into override-variance errors, for
example `le(self, PosetElement, PosetElement)` overriding
`le(self, object, object)`. `Any` would hide the variance issue, but
`sage-stubs/AGENTS.md` bans `Any` for named parameters. This needs a typed
poset element/subset model before filling the provider methods.

### `sage.categories.infinite_enumerated_sets.InfiniteEnumeratedSets.ParentMethods.random_element`

Fresh baseline:
`.mypy_cache/category-specs-error-classification/raw_errors_sets_enum_batch2_fresh.txt`
reports:

```text
category_specs/sets/subcategories/countable.py:177:
Method "random_element" is marked as an override, but no base method was found
```

Sage 10.7 source defines `random_element` directly at
`sage-src/src/sage/categories/infinite_enumerated_sets.py:48`.

Blocked because a source-backed direct-method experiment regressed the real
consumer capture:

```text
843 raw_errors_sets_enum_batch2_fresh.txt
911 raw_errors_infinite_enum_batch_fresh.txt
```

The missing-base diagnostic turned into self-type argument errors. This needs
the enumerated-set provider self type aligned before adding the method.

### `sage.categories.category.CategoryWithParameters._make_named_class_key`

Fresh baseline:
`.mypy_cache/category-specs-error-classification/raw_errors_sets_enum_batch2_fresh.txt`
reports missing-base errors at:

- `category_specs/rings/subcategories/constructions/parameterized.py:54`
- `category_specs/rings/subcategories/constructions/parameterized.py:106`

Sage 10.7 source defines the abstract method at
`sage-src/src/sage/categories/category.py:2849`.

A narrow sidecar patch:

```python
class CategoryWithParameters(Category):
    def _make_named_class_key(
        self, name: str
    ) -> Category | type | tuple[object, ...]: ...
```

removed both targeted missing-base diagnostics, but it also exposed broader
local-wrapper `Category` mismatches in the real consumer capture:

```text
843 raw_errors_sets_enum_batch2_fresh.txt
902 raw_errors_make_key_fresh.txt
```

This needs the `category_specs` local wrapper `CategoryWithParameters` relation
fixed or projected before the sidecar method becomes a clean addition.

### `sage.rings.infinity.oo`

GitHub issue #4 listed `sage.rings.infinity.oo` as a possible alias/export to
verify for `category_specs/rings/subcategories/polynomial_ring.py:83`.

- Searched: GitHub issue #4 P2 request; Sage 10.7
  `src/sage/rings/infinity.py` around the module-level infinity assignments;
  `git -C sage-src grep -n "oo =\|infinity =" 10.7 --
  src/sage/rings/infinity.py`.
- Found: Sage 10.7 defines `infinity = InfinityRing.gen(0)`,
  `Infinity = infinity`, and `minus_infinity = InfinityRing.gen(1)` in
  `sage.rings.infinity`; I found no module-level `oo` assignment in that
  source file.
- Conclusion: inference — `sage.rings.infinity.oo` is not a source-backed
  sidecar export for Sage 10.7, so adding it to `rings/infinity.pyi` would be
  prompt-driven invention rather than stub data.
- Confidence: High.
- Gaps: This does not rule out `oo` being exported by another aggregation
  module such as `sage.all`; it only blocks adding `oo` to
  `sage.rings.infinity`.

## Search Notes

The following were checked and should not be re-tried as direct sidecar method
patches without new evidence:

- Homsets broad class/base modeling: local experiments produced
  `raw_errors_homsets_batch_fresh.txt` and
  `raw_errors_homsets_methods_batch_fresh.txt`, both worse than the current
  baseline.
- Sage category top-level base inheritance such as `Sets(Category_singleton)`
  and `Posets(Category)`: source-correct for Sage, but it does not fix
  consumer errors that expect `category_specs.cat.Category`.
- Direct-method additions using `object` where the consumer override narrows
  parameters to local element/provider types.
