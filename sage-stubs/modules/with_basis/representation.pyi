from collections.abc import Callable, Hashable, Iterable
from typing import Generic, TypeVar

from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent

_Index = TypeVar("_Index", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_Actor = TypeVar("_Actor", bound=Element, default=Element)


class Representation_abstract(
    CombinatorialFreeModule,
    Generic[_Actor, _Index, _Scalar],
):
    def semigroup(self) -> Parent[_Actor]: ...
    def side(self) -> str: ...
    def representation_matrix(
        self,
        g: _Actor,
        side: str | None = ...,
    ) -> object: ...
    def character(self) -> Callable[[_Actor], _Scalar]: ...
    def invariant_module(
        self,
        S: Iterable[_Actor] | None = ...,
    ) -> CombinatorialFreeModule: ...
    def twisted_invariant_module(
        self,
        chi: Callable[[_Actor], _Scalar],
        S: Iterable[_Actor] | None = ...,
    ) -> CombinatorialFreeModule: ...
    def tensor_product(
        self,
        other: Representation_abstract[_Actor, Hashable, _Scalar],
    ) -> Representation_abstract[_Actor, tuple[_Index, Hashable], _Scalar]: ...


class Representation(
    Representation_abstract[_Actor, _Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(
        self,
        semigroup: Parent[_Actor],
        module: CombinatorialFreeModule,
        on_basis: Callable[
            [_Actor, _Index],
            IndexedFreeModuleElement[_Index, _Scalar],
        ],
        side: str = ...,
        category: object | None = ...,
    ) -> None: ...
    def action_on_basis(
        self,
        g: _Actor,
        index: _Index,
    ) -> IndexedFreeModuleElement[_Index, _Scalar]: ...


class Representation_Exterior(
    Representation_abstract[_Actor, tuple[_Index, ...], _Scalar],
    Generic[_Actor, _Index, _Scalar],
):
    def degree(self) -> int: ...
    def characteristic_polynomial(
        self,
        g: _Actor,
        var: str = ...,
    ) -> Polynomial: ...
