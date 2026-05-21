# Sage Stubs Progress Tracker

## Quality Contract
- No `Any` anywhere (not even with justification) — check_stubs.py enforces this
- No `object` as return type (except `__new__`) — check_stubs.py enforces this
- Concrete sage types: `Ring`, `CommutativeRing`, `Field`, `Element`, `FractionFieldElement`, etc.
- Never fall back to `Parent` when the actual type is knowable from source
- Phase discipline: Enumerate → Resolve Types → Write — all in initial prompt

## Completed Stubs

| File | Jules Session | Notes |
|------|--------------|-------|
| `rings/lazy_series.pyi` (LazyPowerSeries) | 2045195418505124698 | Trap canary (May 2026 methods). Passes lint. |
| `rings/fraction_field.pyi` (FractionField_generic) | 11993709386155845619 | Passes lint/custom checker |

## Pre-existing Stubs (Need Cleanup)

These stubs exist but have `Any` violations that need Jules sessions to fix:

| File | Violations |
|------|-----------|
| `categories/category.pyi` | 12+ Any violations |
| `categories/cartesian_product.pyi` | 5 Any violations |
| `structure/parent.pyi` | 12+ Any violations |
| `structure/element.pyi` | `object` return type on `parent()` |
| `categories/functor.pyi` | `__call__` returns Any |
| `categories/homset.pyi` | `__call__` returns Any |
| `categories/morphism.pyi` | `__call__` returns Any |
| `misc/lazy_import.pyi` | `__call__` returns Any |
| `rings/real_mpfi.pyi` | `lower`/`upper` return `object` |
| `sets/condition_set.pyi` | 4 Any violations |
| `structure/category_object.pyi` | 2 Any violations |

## Active Jules Sessions

| Session ID | Target | Status | Notes |
|-----------|--------|--------|-------|
| 14415206495966720236 | PolynomialRing_general (new) | In Progress | |
| 11088439005315309442 | IntegerRing_class (new) | In Progress | |
| 8199371162199757075 | structure/parent.pyi (cleanup) | In Progress | |
| 15673998272445908728 | RationalField (new) | In Progress | |
| 3400950749309612373 | MatrixSpace (new) | In Progress | |
| 7595694660387721782 | categories/category.pyi (cleanup) | In Progress | |
| 8664373267979715905 | structure/element.pyi (cleanup) | In Progress | |
| 3692623478821225612 | Integer class (new) | In Progress | |
| 16578394648550438696 | NumberField_generic (new) | In Progress | |
| 12249685295038896733 | PowerSeriesRing_generic (new) | In Progress | |

## Next Targets (Prioritized)

Fresh stubs needed:
1. `rings/polynomial/polynomial_ring.py` → `PolynomialRing_general`
2. `rings/integer_ring.py` → `IntegerRing_class` (ZZ)
3. `rings/rational_field.py` → `RationalField` (QQ)
4. `rings/number_field/number_field.py` → `NumberField_generic`
5. `rings/finite_rings/finite_field_base.py` → `FiniteField`
6. `matrix/matrix_space.py` → `MatrixSpace`
7. `rings/power_series_ring.py` → `PowerSeriesRing_generic`
8. `rings/real_double.py` → `RealDoubleField_class` (RDF)

Cleanups (fix existing Any violations):
1. `structure/parent.pyi` — high-value, imported by everything
2. `categories/category.pyi` — high-value
3. `structure/element.pyi` — fix `parent() -> object`

## Commit Log

| Date | Action | Session |
|------|--------|---------|
| 2026-05-21 | Add LazyPowerSeries stub (trap experiment) | 2045195418505124698 |
| 2026-05-21 | Add FractionField_generic stub | 11993709386155845619 |
