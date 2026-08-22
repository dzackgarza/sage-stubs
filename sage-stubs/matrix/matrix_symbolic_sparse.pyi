from collections.abc import Sequence
from typing import Literal, Self, overload

from sage.matrix.matrix import Matrix
from sage.matrix.matrix_generic_sparse import Matrix_generic_sparse
from sage.matrix.matrix_symbolic_dense import Matrix_symbolic_dense
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
    def echelonize(self, **kwds: object) -> None: ...
    def eigenvalues(self, extend: bool = ...) -> list[Expression]: ...
    def eigenvectors_left(
        self,
        other: Matrix[Expression] | None = ...,
    ) -> list[SymbolicSparseEigenvectorData]: ...
    def eigenvectors_right(
        self,
        other: Matrix[Expression] | None = ...,
    ) -> list[SymbolicSparseEigenvectorData]: ...
    def exp(self) -> Matrix_symbolic_dense: ...
    def charpoly(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial: ...
    def minpoly(self, var: str = ...) -> Polynomial: ...
    def fcp(self, var: str = ...) -> Factorization: ...

    @overload
    def jordan_form(
        self,
        subdivide: bool = ...,
        transformation: Literal[False] = ...,
    ) -> Matrix_symbolic_dense: ...
    @overload
    def jordan_form(
        self,
        subdivide: bool,
        transformation: Literal[True],
    ) -> tuple[Matrix_symbolic_dense, Self]: ...
    @overload
    def jordan_form(
        self,
        subdivide: bool = ...,
        transformation: bool = ...,
    ) -> Matrix_symbolic_dense | tuple[Matrix_symbolic_dense, Self]: ...

    def simplify(self) -> Self: ...
    def simplify_trig(self) -> Matrix_symbolic_dense: ...
    def simplify_rational(self) -> Matrix_symbolic_dense: ...
    def simplify_full(self) -> Self: ...
    def canonicalize_radical(self) -> Self: ...
    def factor(self) -> Self: ...
    def expand(self) -> Self: ...
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
