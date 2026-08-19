from collections.abc import Sequence
from typing import Generic, Self, TypeVar

from sage.libs.gap.element import GapElement
from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class Matrix_gap(Matrix_dense[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        parent: MatrixSpace[_Scalar],
        entries: Sequence[ElementConstructorInput]
        | Sequence[Sequence[ElementConstructorInput]]
        | GapElement
        | ElementConstructorInput = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def _list(self) -> list[_Scalar]: ...
    def list(self) -> list[_Scalar]: ...
    def row(
        self,
        i: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[_Scalar]: ...
    def column(
        self,
        j: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[_Scalar]: ...
    def gap(self) -> GapElement: ...
    def _gap_(self) -> GapElement: ...
    def determinant(self, algorithm: str = ...) -> _Scalar: ...
    det = determinant
    def rank(self, algorithm: str = ...) -> int: ...
    def trace(self) -> _Scalar: ...
    def characteristic_polynomial(
        self,
        var: str = ...,
    ) -> Polynomial: ...
    charpoly = characteristic_polynomial
    def inverse(self) -> Self: ...
    __invert__ = inverse
    def transpose(self) -> Self: ...
