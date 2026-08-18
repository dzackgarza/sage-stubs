from collections.abc import Sequence
from typing import Generic, Self, TypeVar

from sage.libs.gap.element import GapElement
from sage.matrix.matrix_dense import Matrix_dense
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class Matrix_gap(Matrix_dense[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        parent: Parent[Self],
        entries: Sequence[ElementConstructorInput] | GapElement = ...,
        copy: bool = ...,
        coerce: bool = ...,
    ) -> None: ...
    def gap(self) -> GapElement: ...
    def _gap_(self) -> GapElement: ...
    def determinant(self, algorithm: str = ...) -> _Scalar: ...
    det = determinant
    def rank(self, algorithm: str = ...) -> int: ...
    def trace(self) -> _Scalar: ...
    def characteristic_polynomial(self, var: str = ...) -> Polynomial: ...
    charpoly = characteristic_polynomial
    def inverse(self) -> Self: ...
    __invert__ = inverse
    def transpose(self) -> Self: ...
