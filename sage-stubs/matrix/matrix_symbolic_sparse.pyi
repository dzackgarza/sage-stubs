from collections.abc import Sequence
from typing import Literal, Self, overload

from sage.matrix.matrix import Matrix
from sage.matrix.matrix_generic_sparse import Matrix_generic_sparse
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.factorization import Factorization
from sage.symbolic.expression import (
    Expression,
    SymbolicInput,
    SymbolicSubstitution,
)

type SymbolicSparseEigenvectorData = tuple[
    Expression,
    list[FreeModuleElement[Expression]],
    Integer,
]


class Matrix_symbolic_sparse(Matrix_generic_sparse[Expression]):
    # Classical echelon form and exact Maxima spectral data
    def echelonize(self, **kwds: object) -> None: ...
    def eigenvalues(self, extend: bool = ...) -> list[Expression]: ...
    def eigenvectors_left(
        self,
        other: Matrix_symbolic_sparse | None = ...,
    ) -> list[SymbolicSparseEigenvectorData]: ...
    def eigenvectors_right(
        self,
        other: Matrix_symbolic_sparse | None = ...,
    ) -> list[SymbolicSparseEigenvectorData]: ...
    def exp(self) -> Self: ...

    # Characteristic, minimal, and Jordan forms
    def charpoly(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial: ...
    characteristic_polynomial = charpoly
    def minpoly(self, var: str = ...) -> Polynomial: ...
    minimal_polynomial = minpoly
    def fcp(self, var: str = ...) -> Factorization: ...

    @overload
    def jordan_form(
        self,
        subdivide: bool = ...,
        transformation: Literal[False] = ...,
    ) -> Self: ...
    @overload
    def jordan_form(
        self,
        subdivide: bool,
        transformation: Literal[True],
    ) -> tuple[Self, Self]: ...

    # Symbolic simplification and normalization
    def simplify(self) -> Self: ...
    def simplify_trig(self) -> Self: ...
    def simplify_rational(self) -> Self: ...
    def simplify_full(self) -> Self: ...
    def canonicalize_radical(self) -> Self: ...
    def factor(self) -> Self: ...
    def expand(self) -> Self: ...

    # Variables, evaluation, and callable symbolic matrices
    def variables(self) -> tuple[Expression, ...]: ...
    def arguments(self) -> tuple[Expression, ...]: ...
    def number_of_arguments(self) -> int: ...
    def __call__(
        self,
        *args: SymbolicSubstitution,
        **kwargs: SymbolicInput,
    ) -> Self: ...
    def function(
        self,
        *args: Expression | Sequence[Expression],
    ) -> Matrix[Expression]: ...
