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

> [!NOTE]
> **Re-baseline (Phase 01 Completion — May 2026):**
> Confirmed still blocked. With the foundation stubs (Phase 01) now 100% complete, the local `sage-stubs/categories/posets.pyi` does not include these methods. Because the `Any` ban is strictly enforced, we cannot launder these as `Any` or `object` without triggering override-variance type failures in consumer tests. Adding these requires full-parity poset element type representation which is scheduled for Phase 11 (`phases/phase-11-combinat-crystals-posets.md`).

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

> [!NOTE]
> **Re-baseline (Phase 01 Completion — May 2026):**
> Confirmed still blocked. The local `sage-stubs/categories/infinite_enumerated_sets.pyi` remains clean of the `random_element` stub. Resolving this signature mismatch requires self-type/provider-type alignment for all enumerated set stubs, which is deferred to the Tier 3 domain rollout (Phase 11 Crystals and Posets or Phase 9 Combinatorics foundations).

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

> [!NOTE]
> **Re-baseline (Phase 01 Completion — May 2026):**
> Confirmed still blocked. While `sage-stubs/categories/category.pyi` declares `_make_named_class_key(self, name: str) -> Hashable: ...`, any further refinement of the return type is blocked by the external category-specs wrapper relationship. The existing stub remains minimal and stable.

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
