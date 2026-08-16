import builtins
from typing import Self

from sage.structure.element import Element

class _SageObject: ...

class CartesianProductFactory:
    def create_key_and_extra_args(
        self,
        growth_groups: builtins.object,
        category: builtins.object,
        **kwds: builtins.object,
    ) -> _SageObject: ...
    def create_object(
        self, version: builtins.object, args: builtins.object, **kwds: builtins.object
    ) -> _SageObject: ...

CartesianProductGrowthGroups: _SageObject

class GenericProduct:
    def __init__(
        self, sets: builtins.object, category: builtins.object, **kwds: builtins.object
    ) -> None: ...
    def some_elements(self) -> _SageObject: ...
    def cartesian_injection(
        self, factor: builtins.object, element: builtins.object
    ) -> _SageObject: ...
    def gens_monomial(self) -> tuple[Element, ...]: ...
    def variable_names(self) -> _SageObject: ...

    class Element:
        is_lt_one: _SageObject

        def __pow__(self, exponent: builtins.object) -> Self: ...
        def factors(self) -> _SageObject: ...
        log: _SageObject
        log_factor: _SageObject
        rpow: _SageObject

        def exp(self) -> _SageObject: ...
        def __invert__(self) -> Self: ...
        def variable_names(self) -> _SageObject: ...

    CartesianProduct: _SageObject

class UnivariateProduct:
    def __init__(
        self,
        sets: builtins.object,
        category: builtins.object,
        **kwargs: builtins.object,
    ) -> None: ...
    CartesianProduct: _SageObject

class MultivariateProduct:
    def __init__(
        self,
        sets: builtins.object,
        category: builtins.object,
        **kwargs: builtins.object,
    ) -> None: ...
    CartesianProduct: _SageObject
