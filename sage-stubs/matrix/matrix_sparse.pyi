from collections.abc import Callable, Iterable, Mapping
from typing import Generic, Literal, Self, TypeVar, overload

from sage.categories.morphism import Morphism
from sage.matrix.matrix import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.structure.element import Element, RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)
_RightScalar = TypeVar("_RightScalar", bound=RingElement)


class Matrix_sparse(
    Matrix[_Scalar],
    Generic[_Scalar],
):
    def change_ring(
        self,
        ring: Parent[_NewScalar],
    ) -> Matrix_sparse[_NewScalar]: ...
    def __copy__(self) -> Self: ...
    def _multiply_classical(
        self,
        right: Matrix_sparse[_Scalar],
    ) -> Self: ...
    def _multiply_classical_with_cache(
        self,
        right: Matrix_sparse[_Scalar],
    ) -> Self: ...
    def _lmul_(self, right: _Scalar) -> Self: ...
    def _pickle(
        self,
    ) -> tuple[dict[tuple[int, int], _Scalar], Literal[-1]]: ...
    def _unpickle_generic(
        self,
        data: Mapping[tuple[int, int], _Scalar],
        version: int,
    ) -> None: ...
    def _richcmp_(
        self,
        other: Matrix_sparse[_Scalar],
        op: int,
    ) -> bool: ...
    def transpose(self) -> Self: ...
    def antitranspose(self) -> Self: ...
    def _reverse_unsafe(self) -> None: ...
    def charpoly(
        self,
        var: str = ...,
        **kwds: object,
    ) -> Polynomial: ...
    def determinant(self, **kwds: object) -> _Scalar: ...
    def _elementwise_product(
        self,
        right: Matrix_sparse[_Scalar],
    ) -> Self: ...
    def apply_morphism(
        self,
        phi: Morphism[_Scalar, _NewScalar],
    ) -> Matrix_sparse[_NewScalar]: ...

    @overload
    def apply_map(
        self,
        phi: Callable[[_Scalar], _NewScalar],
        R: None = ...,
        sparse: bool = ...,
    ) -> Matrix[_NewScalar]: ...
    @overload
    def apply_map(
        self,
        phi: Callable[[_Scalar], ElementConstructorInput],
        R: Parent[_NewScalar],
        sparse: bool = ...,
    ) -> Matrix[_NewScalar]: ...
    @overload
    def apply_map(
        self,
        phi: Callable[[_Scalar], ElementConstructorInput],
        R: None = ...,
        sparse: bool = ...,
    ) -> Matrix[RingElement]: ...

    def _derivative(
        self,
        var: Element | None = ...,
        R: Parent | None = ...,
    ) -> Matrix_sparse[RingElement]: ...
    def density(self) -> int | Rational: ...
    def matrix_from_rows_and_columns(
        self,
        rows: Iterable[int | Integer],
        columns: Iterable[int | Integer],
    ) -> Self: ...
    def augment(
        self,
        right: Matrix[_RightScalar] | FreeModuleElement[_RightScalar],
        subdivide: bool = ...,
    ) -> Self: ...
