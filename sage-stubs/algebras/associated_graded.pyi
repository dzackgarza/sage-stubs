from __future__ import annotations

from collections.abc import Hashable, Iterable, Iterator
from typing import Generic, Protocol, Self, TypeVar

from sage.categories.category import Category
from sage.combinat.free_module import CombinatorialFreeModule
from sage.structure.element import RingElement
from sage.structure.parent import Parent

class _GradingDegree(Protocol):
    def __add__(self, other: Self) -> Self: ...
    def __lt__(self, other: Self) -> bool: ...
    def __le__(self, other: Self) -> bool: ...

_Coefficient = TypeVar(
    "_Coefficient",
    bound=RingElement,
    default=RingElement,
)
_BasisIndex = TypeVar("_BasisIndex", bound=Hashable)
_Degree = TypeVar("_Degree", bound=_GradingDegree)
_ElementCoefficient = TypeVar(
    "_ElementCoefficient",
    bound=RingElement,
    covariant=True,
)
_ElementBasisIndex = TypeVar(
    "_ElementBasisIndex",
    bound=Hashable,
    covariant=True,
)

class _FilteredElement(
    Protocol[_ElementCoefficient, _ElementBasisIndex],
):
    def __iter__(
        self,
    ) -> Iterator[tuple[_ElementBasisIndex, _ElementCoefficient]]: ...

_SourceElement = TypeVar(
    "_SourceElement",
    bound=_FilteredElement[RingElement, Hashable],
    default=_FilteredElement[RingElement, Hashable],
)

class _ElementFamily(Protocol[_SourceElement]):
    def __getitem__(self, key: Hashable) -> _SourceElement: ...
    def __iter__(self) -> Iterator[_SourceElement]: ...
    def keys(self) -> Iterable[Hashable]: ...
    def values(self) -> Iterable[_SourceElement]: ...

class _BasisFamily(Protocol[_BasisIndex, _SourceElement]):
    def __getitem__(self, key: _BasisIndex) -> _SourceElement: ...
    def __iter__(self) -> Iterator[_SourceElement]: ...
    def keys(self) -> Iterable[_BasisIndex]: ...

class _FilteredAlgebraWithBasis(
    Protocol[_Coefficient, _BasisIndex, _Degree, _SourceElement],
):
    def base_ring(self) -> Parent[_Coefficient]: ...
    def category(self) -> Category: ...
    def basis(self) -> _BasisFamily[_BasisIndex, _SourceElement]: ...
    def algebra_generators(self) -> _ElementFamily[_SourceElement]: ...
    def gen(self, key: Hashable) -> _SourceElement: ...
    def degree_on_basis(self, x: _BasisIndex) -> _Degree: ...
    def one_basis(self) -> _BasisIndex: ...
    def product_on_basis(
        self,
        x: _BasisIndex,
        y: _BasisIndex,
    ) -> _SourceElement: ...

class _AssociatedGradedElement(
    CombinatorialFreeModule.Element,
    Generic[_Coefficient, _BasisIndex, _Degree, _SourceElement],
):
    def parent(
        self,
    ) -> AssociatedGradedAlgebra[
        _Coefficient,
        _BasisIndex,
        _Degree,
        _SourceElement,
    ]: ...
    def monomial_coefficients(
        self,
        copy: bool = True,
    ) -> dict[_BasisIndex, _Coefficient]: ...

class AssociatedGradedAlgebra(
    CombinatorialFreeModule,
    Generic[_Coefficient, _BasisIndex, _Degree, _SourceElement],
):
    Element: type[
        _AssociatedGradedElement[
            _Coefficient,
            _BasisIndex,
            _Degree,
            _SourceElement,
        ]
    ]

    def __init__(
        self,
        A: _FilteredAlgebraWithBasis[
            _Coefficient,
            _BasisIndex,
            _Degree,
            _SourceElement,
        ],
        category: Category | None = None,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _element_constructor_(
        self,
        x: _SourceElement
        | _AssociatedGradedElement[
            _Coefficient,
            _BasisIndex,
            _Degree,
            _SourceElement,
        ],
    ) -> _AssociatedGradedElement[
        _Coefficient,
        _BasisIndex,
        _Degree,
        _SourceElement,
    ]: ...
    def gen(
        self,
        key: Hashable,
    ) -> _AssociatedGradedElement[
        _Coefficient,
        _BasisIndex,
        _Degree,
        _SourceElement,
    ]: ...
    def algebra_generators(
        self,
    ) -> _ElementFamily[
        _AssociatedGradedElement[
            _Coefficient,
            _BasisIndex,
            _Degree,
            _SourceElement,
        ]
    ]: ...
    def degree_on_basis(self, x: _BasisIndex) -> _Degree: ...
    def one_basis(self) -> _BasisIndex: ...
    def product_on_basis(
        self,
        x: _BasisIndex,
        y: _BasisIndex,
    ) -> _AssociatedGradedElement[
        _Coefficient,
        _BasisIndex,
        _Degree,
        _SourceElement,
    ]: ...
    def monomial(
        self,
        index: _BasisIndex,
    ) -> _AssociatedGradedElement[
        _Coefficient,
        _BasisIndex,
        _Degree,
        _SourceElement,
    ]: ...
    def sum_of_terms(
        self,
        terms: Iterable[tuple[_BasisIndex, _Coefficient]],
        distinct: bool = False,
    ) -> _AssociatedGradedElement[
        _Coefficient,
        _BasisIndex,
        _Degree,
        _SourceElement,
    ]: ...
