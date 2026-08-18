from collections.abc import Mapping, Sequence
from typing import Self

from sage.matrix.matrix_sparse import Matrix_sparse
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.parent import ElementConstructorInput, Parent
from sage.symbolic.expression import Expression


class Matrix_symbolic_sparse(Matrix_sparse[Expression]):
    def __init__(
        self,
        parent: Parent[Self],
        entries: Sequence[Expression | ElementConstructorInput]
        | Mapping[tuple[int, int], Expression | ElementConstructorInput]
        | ElementConstructorInput = ...,
        copy: bool = ...,
        coerce: bool = ...,
    ) -> None: ...
    def determinant(self, algorithm: str = ...) -> Expression: ...
    det = determinant
    def trace(self) -> Expression: ...
    def characteristic_polynomial(self, var: str = ...) -> Polynomial: ...
    charpoly = characteristic_polynomial
    def simplify(self, algorithm: str | None = ...) -> Self: ...
    def expand(self) -> Self: ...
    def factor(self) -> Self: ...
    def subs(self, *args: object, **kwds: ElementConstructorInput) -> Self: ...
    substitute = subs
    def derivative(self, *args: object) -> Self: ...
    diff = derivative
    def dense_matrix(self) -> Matrix_symbolic_dense: ...


from sage.matrix.matrix_symbolic_dense import Matrix_symbolic_dense
