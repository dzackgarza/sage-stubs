# sage-stubs

PEP 561 stub-only package for Sage 10.7 category/structure interfaces.

Provides `.pyi` type stubs for the Sage category infrastructure surface
(Category, CategoryWithAxiom, Parent, Element, Morphism, Homset, cached_method,
abstract_method, LazyImport, etc.) so that mypy can analyze code that imports
from `sage.categories.*`, `sage.structure.*`, and `sage.misc.*`.

## Usage

Install alongside `sage-mypy-category-plugin`:

```bash
sage -python -m pip install sage-mypy-category-plugin sage-stubs
```

Because this package follows the PEP 561 `<package>-stubs` naming convention,
mypy automatically discovers these stubs for `sage.*` imports without any
`mypy_path` configuration.

## Version coupling

This package is versioned to the Sage release it covers:

| sage-stubs version | Sage version |
|--------------------|--------------|
| 10.7.x             | 10.7         |

## Scope

Stubs cover the plugin-facing infrastructure surface:

- `sage.categories.category` — Category, CategoryWithParameters, JoinCategory
- `sage.categories.category_with_axiom` — CategoryWithAxiom variants, all_axioms
- `sage.categories.cartesian_product` — CartesianProductsCategory, cartesian_product
- `sage.categories.functor` — Functor
- `sage.categories.homset` — Homset
- `sage.categories.morphism` — Morphism
- `sage.structure.category_object` — CategoryObject
- `sage.structure.element` — Element
- `sage.structure.parent` — Parent
- `sage.misc.abstract_method` — abstract_method, AbstractMethod
- `sage.misc.cachefunc` — cached_method
- `sage.misc.lazy_import` — LazyImport
- `sage.sets.condition_set` — ConditionSet
- `sage.matrix.matrix2` — Matrix
- `sage.rings.real_mpfi` — RealIntervalField
- `sage.rings.polynomial.ore_polynomial_ring` — OrePolynomialRing
- `sage.combinat.posets.posets` — FinitePoset
