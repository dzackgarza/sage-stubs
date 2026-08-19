
from collections.abc import Callable, Hashable, Iterator
from types import NotImplementedType
from typing import Generic, Protocol, Self, TypeVar

from sage.categories.category import Category
from sage.combinat.free_module import CombinatorialFreeModule
from sage.combinat.posets.posets import FinitePoset
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.parent import AlgebraPrintOption, Parent

_Coefficient = TypeVar(
    "_Coefficient",
    bound=RingElement,
    default=RingElement,
)
_Cell = TypeVar("_Cell", bound=Hashable)
_ModuleIndex = TypeVar("_ModuleIndex", bound=Hashable)
_SourceIndex = TypeVar("_SourceIndex", bound=Hashable)

class _CellularAlgebraElement(Protocol):
    def parent(self) -> Parent[RingElement]: ...

_AlgebraElement = TypeVar(
    "_AlgebraElement",
    bound=_CellularAlgebraElement,
    default=_CellularAlgebraElement,
)

type CellularBasisIndex[_Cell: Hashable, _ModuleIndex: Hashable] = tuple[
    _Cell,
    _ModuleIndex,
    _ModuleIndex,
]

class _CellModuleIndexSet(Protocol[_ModuleIndex]):
    def __iter__(self) -> Iterator[_ModuleIndex]: ...
    def __contains__(self, value: Element) -> bool: ...
    def cardinality(self) -> int | Integer: ...

class _CellularAlgebra(
    Protocol[_Coefficient, _Cell, _ModuleIndex, _SourceIndex, _AlgebraElement],
):
    def base_ring(self) -> Parent[_Coefficient]: ...
    def category(self) -> Category: ...
    def cell_poset(self) -> FinitePoset: ...
    def cell_module_indices(
        self,
        cell: _Cell,
    ) -> _CellModuleIndexSet[_ModuleIndex]: ...
    def one(self) -> _AlgebraElement: ...
    def __call__(
        self,
        value: _CellularBasisElement[
            _Coefficient,
            _Cell,
            _ModuleIndex,
            _SourceIndex,
            _AlgebraElement,
        ],
    ) -> _AlgebraElement: ...

class _CellularBasisElement(
    CombinatorialFreeModule.Element,
    Generic[
        _Coefficient,
        _Cell,
        _ModuleIndex,
        _SourceIndex,
        _AlgebraElement,
    ],
):
    def parent(
        self,
    ) -> CellularBasis[
        _Coefficient,
        _Cell,
        _ModuleIndex,
        _SourceIndex,
        _AlgebraElement,
    ]: ...
    def monomial_coefficients(
        self,
        copy: bool = True,
    ) -> dict[CellularBasisIndex[_Cell, _ModuleIndex], _Coefficient]: ...

class CellularBasis(
    CombinatorialFreeModule,
    Generic[_Coefficient, _Cell, _ModuleIndex, _SourceIndex, _AlgebraElement],
):
    Element: type[
        _CellularBasisElement[
            _Coefficient,
            _Cell,
            _ModuleIndex,
            _SourceIndex,
            _AlgebraElement,
        ]
    ]

    def __init__(
        self,
        A: _CellularAlgebra[
            _Coefficient,
            _Cell,
            _ModuleIndex,
            _SourceIndex,
            _AlgebraElement,
        ],
        to_algebra: Callable[
            [CellularBasisIndex[_Cell, _ModuleIndex]],
            _AlgebraElement,
        ]
        | NotImplementedType
        | None = None,
        from_algebra: Callable[
            [_SourceIndex],
            _CellularBasisElement[
                _Coefficient,
                _Cell,
                _ModuleIndex,
                _SourceIndex,
                _AlgebraElement,
            ],
        ]
        | NotImplementedType
        | None = None,
        **kwargs: AlgebraPrintOption,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_term(
        self,
        x: CellularBasisIndex[_Cell, _ModuleIndex],
    ) -> str: ...
    def cellular_basis_of(
        self,
    ) -> _CellularAlgebra[
        _Coefficient,
        _Cell,
        _ModuleIndex,
        _SourceIndex,
        _AlgebraElement,
    ]: ...
    def cell_poset(self) -> FinitePoset: ...
    def cell_module_indices(
        self,
        la: _Cell,
    ) -> _CellModuleIndexSet[_ModuleIndex]: ...
    def cellular_basis(self) -> Self: ...
    def one(
        self,
    ) -> _CellularBasisElement[
        _Coefficient,
        _Cell,
        _ModuleIndex,
        _SourceIndex,
        _AlgebraElement,
    ]: ...
    def product_on_basis(
        self,
        x: CellularBasisIndex[_Cell, _ModuleIndex],
        y: CellularBasisIndex[_Cell, _ModuleIndex],
    ) -> _CellularBasisElement[
        _Coefficient,
        _Cell,
        _ModuleIndex,
        _SourceIndex,
        _AlgebraElement,
    ]: ...
    def monomial(
        self,
        index: CellularBasisIndex[_Cell, _ModuleIndex],
    ) -> _CellularBasisElement[
        _Coefficient,
        _Cell,
        _ModuleIndex,
        _SourceIndex,
        _AlgebraElement,
    ]: ...
