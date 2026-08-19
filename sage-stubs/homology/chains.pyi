from collections.abc import Hashable, Iterable
from typing import Generic, TypeVar

from sage.combinat.free_module import CombinatorialFreeModule
from sage.homology.chain_complex import Chain_class, ChainComplex_class
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.parent import Parent
from sage.topology.cell_complex import GenericCellComplex

_Cell = TypeVar("_Cell", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class CellComplexReference(Generic[_Cell]):
    def __init__(
        self,
        cell_complex: GenericCellComplex,
        degree: int | Integer,
        cells: Iterable[_Cell] | None = ...,
    ) -> None: ...
    def cell_complex(self) -> GenericCellComplex: ...
    def degree(self) -> int | Integer: ...


class Chains(
    CellComplexReference[_Cell],
    CombinatorialFreeModule,
    Generic[_Cell, _Scalar],
):
    class Element(IndexedFreeModuleElement[_Cell, _Scalar]):
        def parent(self) -> Chains[_Cell, _Scalar]: ...
        def to_complex(self) -> Chain_class[Integer, _Scalar]: ...
        def boundary(self) -> Chains[_Cell, _Scalar].Element: ...
        def is_cycle(self) -> bool: ...
        def is_boundary(self) -> bool: ...

    element_class: type[Element]

    def __init__(
        self,
        cell_complex: GenericCellComplex,
        degree: int | Integer,
        cells: Iterable[_Cell] | None = ...,
        base_ring: Parent[_Scalar] | None = ...,
    ) -> None: ...
    def base_ring(self) -> Parent[_Scalar]: ...
    def dual(self) -> Cochains[_Cell, _Scalar]: ...
    def chain_complex(self) -> ChainComplex_class[Integer, _Scalar]: ...


class Cochains(
    CellComplexReference[_Cell],
    CombinatorialFreeModule,
    Generic[_Cell, _Scalar],
):
    class Element(IndexedFreeModuleElement[_Cell, _Scalar]):
        def parent(self) -> Cochains[_Cell, _Scalar]: ...
        def to_complex(self) -> Chain_class[Integer, _Scalar]: ...
        def coboundary(self) -> Cochains[_Cell, _Scalar].Element: ...
        def is_cocycle(self) -> bool: ...
        def is_coboundary(self) -> bool: ...
        def eval(self, other: Chains[_Cell, _Scalar].Element) -> _Scalar: ...
        def cup_product(
            self,
            cochain: Cochains[_Cell, _Scalar].Element,
        ) -> Cochains[_Cell, _Scalar].Element: ...

    element_class: type[Element]

    def __init__(
        self,
        cell_complex: GenericCellComplex,
        degree: int | Integer,
        cells: Iterable[_Cell] | None = ...,
        base_ring: Parent[_Scalar] | None = ...,
    ) -> None: ...
    def base_ring(self) -> Parent[_Scalar]: ...
    def dual(self) -> Chains[_Cell, _Scalar]: ...
    def cochain_complex(self) -> ChainComplex_class[Integer, _Scalar]: ...
