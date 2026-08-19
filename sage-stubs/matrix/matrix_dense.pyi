from collections.abc import Sequence
from typing import Generic, Literal, Self, TypeVar

from sage.matrix.matrix import Matrix
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class Matrix_dense(
    Matrix[_Scalar],
    Generic[_Scalar],
):
    def __copy__(self) -> Self: ...
    def _pickle(self) -> tuple[list[_Scalar], Literal[-1]]: ...
    def _unpickle_generic(
        self,
        data: Sequence[_Scalar],
        version: int,
    ) -> None: ...
    def _richcmp_(
        self,
        right: Matrix_dense[_Scalar],
        op: int,
    ) -> bool: ...
    def transpose(self) -> Self: ...
    def antitranspose(self) -> Self: ...
    def _reverse_unsafe(self) -> None: ...
    def _elementwise_product(
        self,
        right: Matrix_dense[_Scalar],
    ) -> Self: ...
    def _derivative(
        self,
        var: Element | None = ...,
        R: Parent | None = ...,
    ) -> Matrix[RingElement]: ...
    def _multiply_classical(
        self,
        right: Matrix[_Scalar],
    ) -> Self: ...
