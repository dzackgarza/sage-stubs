from collections.abc import Callable, Iterable, Mapping
from typing import Generic, Literal, Self, TypeVar

from sage.categories.category import Category
from sage.combinat.free_module import CombinatorialFreeModule
from sage.monoids.indexed_free_monoid import (
    IndexedFreeAbelianMonoid,
    IndexedFreeAbelianMonoidElement,
)
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.sets.family import AbstractFamily
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type MatrixIndex = tuple[int | Integer, int | Integer]
type QuantumGenerator = MatrixIndex | Literal["c"]
type QuantumMonomial = IndexedFreeAbelianMonoidElement[QuantumGenerator]
type QuantumTensorElement[_Scalar: RingElement] = IndexedFreeModuleElement[
    tuple[QuantumMonomial, QuantumMonomial],
    _Scalar,
]

class QuantumMatrixElement(
    IndexedFreeModuleElement[QuantumMonomial, _Scalar],
    Generic[_Scalar],
):
    def parent(
        self,
    ) -> QuantumMatrixCoordinateAlgebra_abstract[_Scalar]: ...
    def bar(self) -> Self: ...

class QuantumMatrixCoordinateAlgebra_abstract(
    CombinatorialFreeModule,
    Generic[_Scalar],
):
    Element: type[QuantumMatrixElement[_Scalar]]
    element_class: type[QuantumMatrixElement[_Scalar]]

    @staticmethod
    def __classcall__(
        cls: type[
            QuantumMatrixCoordinateAlgebra_abstract[_Scalar]
        ],
        q: _Scalar | None = ...,
        bar: Callable[[_Scalar], _Scalar] | None = ...,
        R: Ring | None = ...,
        **kwds: object,
    ) -> QuantumMatrixCoordinateAlgebra_abstract[_Scalar]: ...
    def __init__(
        self,
        gp_indices: Iterable[QuantumGenerator],
        n: int | Integer,
        q: _Scalar,
        bar: Callable[[_Scalar], _Scalar] | None,
        R: Ring,
        category: Category,
        indices_key: Callable[[QuantumGenerator], object] | None = ...,
    ) -> None: ...
    def base_ring(self) -> Ring: ...
    def indices(self) -> IndexedFreeAbelianMonoid[QuantumGenerator]: ...
    def _repr_term(self, m: QuantumMonomial) -> str: ...
    def _latex_term(self, m: QuantumMonomial) -> str: ...
    def n(self) -> int | Integer: ...
    def q(self) -> _Scalar: ...
    def one_basis(self) -> QuantumMonomial: ...
    def one(self) -> QuantumMatrixElement[_Scalar]: ...
    def zero(self) -> QuantumMatrixElement[_Scalar]: ...
    def monomial(
        self,
        index: QuantumMonomial,
    ) -> QuantumMatrixElement[_Scalar]: ...
    def term(
        self,
        index: QuantumMonomial,
        coeff: _Scalar,
    ) -> QuantumMatrixElement[_Scalar]: ...
    def _from_dict(
        self,
        d: Mapping[QuantumMonomial, _Scalar],
        coerce: bool = ...,
        remove_zeros: bool = ...,
    ) -> QuantumMatrixElement[_Scalar]: ...
    def gens(self) -> tuple[QuantumMatrixElement[_Scalar], ...]: ...
    def algebra_generators(self) -> AbstractFamily: ...
    def quantum_determinant(self) -> QuantumMatrixElement[_Scalar]: ...
    def product_on_basis(
        self,
        a: QuantumMonomial,
        b: QuantumMonomial,
    ) -> QuantumMatrixElement[_Scalar]: ...
    def _bar_on_basis(
        self,
        x: QuantumMonomial,
    ) -> QuantumMatrixElement[_Scalar]: ...
    def counit_on_basis(self, x: QuantumMonomial) -> _Scalar: ...

class QuantumMatrixCoordinateAlgebra(
    QuantumMatrixCoordinateAlgebra_abstract[_Scalar],
    Generic[_Scalar],
):
    @staticmethod
    def __classcall_private__(
        cls: type[QuantumMatrixCoordinateAlgebra[_Scalar]],
        m: int | Integer,
        n: int | Integer | None = ...,
        q: _Scalar | None = ...,
        bar: Callable[[_Scalar], _Scalar] | None = ...,
        R: Ring | None = ...,
    ) -> QuantumMatrixCoordinateAlgebra[_Scalar]: ...
    def __init__(
        self,
        m: int | Integer,
        n: int | Integer,
        q: _Scalar,
        bar: Callable[[_Scalar], _Scalar] | None,
        R: Ring,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def m(self) -> int | Integer: ...
    def algebra_generators(self) -> AbstractFamily: ...
    def coproduct_on_basis(
        self,
        x: QuantumMonomial,
    ) -> QuantumTensorElement[_Scalar]: ...

class QuantumGL(
    QuantumMatrixCoordinateAlgebra_abstract[_Scalar],
    Generic[_Scalar],
):
    @staticmethod
    def __classcall_private__(
        cls: type[QuantumGL[_Scalar]],
        n: int | Integer,
        q: _Scalar | None = ...,
        bar: Callable[[_Scalar], _Scalar] | None = ...,
        R: Ring | None = ...,
    ) -> QuantumGL[_Scalar]: ...
    def __init__(
        self,
        n: int | Integer,
        q: _Scalar,
        bar: Callable[[_Scalar], _Scalar] | None,
        R: Ring,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def algebra_generators(self) -> AbstractFamily: ...
    @property
    def _qdet_cancel_monomial(self) -> QuantumMonomial: ...
    @property
    def _qdet_remaining(self) -> QuantumMatrixElement[_Scalar]: ...
    def product_on_basis(
        self,
        a: QuantumMonomial,
        b: QuantumMonomial,
    ) -> QuantumMatrixElement[_Scalar]: ...
    def _antipode_on_generator(
        self,
        i: int | Integer,
        j: int | Integer,
    ) -> QuantumMatrixElement[_Scalar]: ...
    def antipode_on_basis(
        self,
        x: QuantumMonomial,
    ) -> QuantumMatrixElement[_Scalar]: ...
    def coproduct_on_basis(
        self,
        x: QuantumMonomial,
    ) -> QuantumTensorElement[_Scalar]: ...
