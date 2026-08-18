from collections.abc import Sequence
from typing import Self

from sage.matrix.matrix_generic_dense import Matrix_generic_dense
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.parent import ElementConstructorInput, Parent


class Matrix_polynomial_dense(Matrix_generic_dense[Polynomial]):
    def __init__(
        self,
        parent: Parent[Self],
        entries: Sequence[Polynomial | ElementConstructorInput] | ElementConstructorInput = ...,
        copy: bool = ...,
        coerce: bool = ...,
    ) -> None: ...
    def determinant(self, algorithm: str = ...) -> Polynomial: ...
    det = determinant
    def trace(self) -> Polynomial: ...
    def characteristic_polynomial(self, var: str = ...) -> Polynomial: ...
    charpoly = characteristic_polynomial
    def content(self) -> Polynomial: ...
    def degree(self) -> int: ...
    def resultant(self, other: Self, variable: object | None = ...) -> Polynomial: ...
