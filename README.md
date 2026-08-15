# sage-stubs

Type stubs for SageMath category and structure infrastructure.

This package provides PEP 561-compliant type stubs (`.pyi` files) that enable static type checking with mypy for code using SageMath's category framework, without requiring a full SageMath installation during development.

## What This Package Provides

- **Type stubs** for SageMath's category infrastructure (`sage.categories.*`)
- **Type stubs** for SageMath's structural components (`sage.structure.*`)
- **Type stubs** for essential utilities (`sage.misc.*`, `sage.sets.*`, etc.)
- **Zero runtime overhead** - stub-only package, not imported at runtime
- **Automatic mypy discovery** via PEP 561 naming convention

## Installation

Add as a git dependency in your `pyproject.toml`:

```toml
[project]
dependencies = [
    "sage-stubs @ git+https://github.com/sagemath/sage-stubs.git",
]
```

Or with uv:

```bash
uv add git+https://github.com/sagemath/sage-stubs.git
```

That's it! Your type checker (mypy, pyright, etc.) will automatically discover the stubs.

## Usage

Once installed, mypy will automatically discover these stubs when analyzing code that imports from `sage.*` modules. No additional configuration is required.

Example:

```python
from sage.categories.groups import Groups
from sage.structure.parent import Parent

class MyGroup(Parent):
    def __init__(self):
        super().__init__(category=Groups())
    
    def _repr_(self) -> str:
        return "My Group"
```

Run mypy:

```bash
mypy your_code.py
```

## Version Compatibility

| sage-stubs version | Compatible SageMath version |
|--------------------|-----------------------------|
| 10.7.x             | SageMath 10.7               |

Install the version matching your target SageMath deployment.

## Covered Modules

This package includes stubs for:

### Category Framework
- `sage.categories.category` — `Category`, `CategoryWithParameters`, `JoinCategory`
- `sage.categories.category_with_axiom` — `CategoryWithAxiom` variants
- `sage.categories.cartesian_product` — `CartesianProductsCategory`
- `sage.categories.functor` — `Functor`
- `sage.categories.homset` — `Homset`
- `sage.categories.morphism` — `Morphism`
- Various category provider modules (additive groups, semirings, etc.)

### Structure
- `sage.structure.category_object` — `CategoryObject`
- `sage.structure.element` — `Element`
- `sage.structure.parent` — `Parent`

### Utilities
- `sage.misc.abstract_method` — `abstract_method`, `AbstractMethod`
- `sage.misc.cachefunc` — `cached_method`
- `sage.misc.lazy_import` — `LazyImport`
- `sage.sets.condition_set` — `ConditionSet`
- `sage.matrix.matrix2` — `Matrix`
- `sage.rings.real_mpfi` — `RealIntervalField`
- `sage.rings.polynomial.ore_polynomial_ring` — `OrePolynomialRing`
- `sage.combinat.posets.posets` — `FinitePoset`

## Limitations

- **Stub accuracy**: Stubs approximate the SageMath API surface. Some signatures may differ from actual runtime behavior due to SageMath's dynamic nature.
- **Not exhaustive**: Only covers modules needed for category infrastructure type checking. Many SageMath modules are not included.
- **Version coupling**: Tied to specific SageMath releases. Update when upgrading SageMath.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development workflows and setup instructions.
