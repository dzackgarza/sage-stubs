import builtins
from collections.abc import (
    Hashable,
)
from typing import Self

from sage.structure.element import Element

class _SageObject: ...

class SplittingAlgebraElement:
    def __invert__(self) -> Self: ...
    def is_unit(self) -> bool: ...
    def monomial_coefficients(
        self, copy: builtins.bool = ...
    ) -> dict[Hashable, Element]: ...
    dict: _SageObject

class SplittingAlgebra:
    Element: _SageObject

    def __init__(
        self,
        monic_polynomial: builtins.object,
        names: builtins.str = ...,
        iterate: builtins.bool = ...,
        warning: builtins.bool = ...,
    ) -> None: ...
    def __reduce__(self) -> tuple[Element, ...]: ...
    def hom(
        self,
        im_gens: builtins.object,
        codomain: builtins.object = ...,
        check: builtins.bool = ...,
        base_map: builtins.object = ...,
    ) -> _SageObject: ...
    def is_completely_split(self) -> bool: ...
    def lifting_map(self) -> _SageObject: ...
    def splitting_roots(self) -> list[Element]: ...
    def scalar_base_ring(self) -> _SageObject: ...
    def defining_polynomial(self) -> _SageObject: ...

def solve_with_extension(
    self,
    root_names: builtins.object = ...,
    var: builtins.str = ...,
    flatten: builtins.bool = ...,
    warning: builtins.bool = ...,
) -> list[tuple]: ...
