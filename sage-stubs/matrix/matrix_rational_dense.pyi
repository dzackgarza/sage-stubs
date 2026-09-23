from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Literal, Never, Self, overload

from sage.libs.pari.gen import gen
from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.structure.parent import ElementConstructorInput

type _RationalMatrixEntries = (
    float
    | int
    | Integer
    | Rational
    | Sequence[int | Integer | Rational | ElementConstructorInput]
    | Sequence[Sequence[int | Integer | Rational | ElementConstructorInput]]
    | Mapping[tuple[int, int], int | Integer | Rational | ElementConstructorInput]
    | Callable[[int, int], int | Integer | Rational | ElementConstructorInput]
    | ElementConstructorInput
    | None
)
type _RationalDecompositionFactor = tuple[
    FreeModule_generic[Rational],
    bool,
]

class Matrix_rational_dense(Matrix_dense[Rational]):
    def __init__(
        self,
        parent: MatrixSpace[Rational],
        entries: _RationalMatrixEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def __neg__(self) -> Self: ...
    def _list(self) -> list[Rational]: ...
    def list(self) -> list[Rational]: ...
    def matrix_from_columns(
        self,
        columns: Iterable[int | Integer],
    ) -> Self: ...
    def add_to_entry(
        self,
        i: int | Integer,
        j: int | Integer,
        elt: ElementConstructorInput,
    ) -> None: ...
    def row(
        self,
        i: int | Integer,
        from_list: bool = ...,
    ) -> FreeModuleElement[Rational]: ...
    def column(
        self,
        j: int | Integer,
        from_list: bool = ...,
    ) -> FreeModuleElement[Rational]: ...
    def transpose(self) -> Self: ...
    def antitranspose(self) -> Self: ...
    def set_row_to_multiple_of_row(
        self,
        i: int | Integer,
        j: int | Integer,
        s: ElementConstructorInput,
    ) -> None: ...
    def inverse(
        self,
        algorithm: str | None = ...,
        check_invertible: bool = ...,
    ) -> Self: ...
    __invert__ = inverse
    def determinant(
        self,
        algorithm: str | None = ...,
        proof: bool | None = ...,
    ) -> Rational: ...
    det = determinant
    def rank(self, algorithm: str | None = ...) -> int: ...
    def trace(self) -> Rational: ...
    def denominator(self) -> Integer: ...
    def _clear_denom(self) -> tuple[Matrix_integer_dense, Integer]: ...
    def height(self) -> Integer: ...
    def charpoly(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial: ...
    def minpoly(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial: ...
    def prod_of_row_sums(
        self,
        cols: Iterable[int | Integer],
    ) -> Rational: ...
    @overload
    def echelonize(
        self,
        algorithm: str | None = ...,
        height_guess: int | Integer | None = ...,
        proof: bool | None = ...,
        **kwds: object,
    ) -> None: ...
    @overload
    def echelonize(
        self,
        algorithm: str = ...,
        cutoff: int = ...,
        **kwds: object,
    ) -> Never: ...
    @overload
    def echelon_form(
        self,
        algorithm: str | None = ...,
        height_guess: int | Integer | None = ...,
        proof: bool | None = ...,
        **kwds: object,
    ) -> Self: ...
    @overload
    def echelon_form(
        self,
        algorithm: str = ...,
        cutoff: int = ...,
        **kwds: object,
    ) -> Never: ...
    def pivots(self) -> tuple[int, ...]: ...
    def nonpivots(self) -> tuple[int, ...]: ...
    def _right_kernel_matrix(
        self,
        **kwds: object,
    ) -> tuple[str, Self]: ...
    def right_kernel_matrix(
        self,
        *args: object,
        **kwds: object,
    ) -> Self: ...
    def left_kernel_matrix(
        self,
        *args: object,
        **kwds: object,
    ) -> Self: ...
    def right_kernel(
        self,
        *args: object,
        **kwds: object,
    ) -> FreeModule_generic[Rational]: ...
    def left_kernel(
        self,
        *args: object,
        **kwds: object,
    ) -> FreeModule_generic[Rational]: ...
    def image(self) -> FreeModule_generic[Rational]: ...
    @overload
    def decomposition(
        self,
        is_diagonalizable: bool = ...,
        dual: Literal[False] = ...,
        algorithm: str | None = ...,
        height_guess: int | Integer | None = ...,
        proof: bool | None = ...,
    ) -> Sequence[_RationalDecompositionFactor]: ...
    @overload
    def decomposition(
        self,
        is_diagonalizable: bool,
        dual: Literal[True],
        algorithm: str | None = ...,
        height_guess: int | Integer | None = ...,
        proof: bool | None = ...,
    ) -> tuple[
        Sequence[_RationalDecompositionFactor],
        Sequence[_RationalDecompositionFactor],
    ]: ...
    @overload
    def decomposition(
        self,
        is_diagonalizable: bool = ...,
        dual: bool = ...,
        algorithm: str | None = ...,
        height_guess: int | Integer | None = ...,
        proof: bool | None = ...,
    ) -> (
        Sequence[_RationalDecompositionFactor]
        | tuple[
            Sequence[_RationalDecompositionFactor],
            Sequence[_RationalDecompositionFactor],
        ]
    ): ...
    @overload
    def decomposition(
        self,
        algorithm: str = ...,
        is_diagonalizable: bool = ...,
        dual: Literal[False] = ...,
    ) -> Sequence[_RationalDecompositionFactor]: ...
    @overload
    def decomposition(
        self,
        algorithm: str,
        is_diagonalizable: bool,
        dual: Literal[True],
    ) -> tuple[
        Sequence[_RationalDecompositionFactor],
        Sequence[_RationalDecompositionFactor],
    ]: ...
    @overload
    def LLL(
        self,
        delta: float | None = ...,
        eta: float | None = ...,
        algorithm: str = ...,
        fp: str | None = ...,
        prec: int = ...,
        early_red: bool = ...,
        use_givens: bool = ...,
        use_siegel: bool = ...,
        transformation: Literal[False] = ...,
        **kwds: object,
    ) -> Self: ...
    @overload
    def LLL(
        self,
        delta: float | None,
        eta: float | None,
        algorithm: str,
        fp: str | None,
        prec: int,
        early_red: bool,
        use_givens: bool,
        use_siegel: bool,
        transformation: Literal[True],
        **kwds: object,
    ) -> tuple[Self, Matrix_integer_dense]: ...
    @overload
    def LLL(
        self,
        delta: float | None = ...,
        eta: float | None = ...,
        algorithm: str = ...,
        fp: str | None = ...,
        prec: int = ...,
        early_red: bool = ...,
        use_givens: bool = ...,
        use_siegel: bool = ...,
        transformation: bool = ...,
        **kwds: object,
    ) -> Self | tuple[Self, Matrix_integer_dense]: ...
    def BKZ(
        self,
        delta: float | None = ...,
        algorithm: str = ...,
        fp: str | None = ...,
        block_size: int = ...,
        prune: int = ...,
        use_givens: bool = ...,
        precision: int = ...,
        proof: bool | None = ...,
        **kwds: object,
    ) -> Self: ...
    def is_LLL_reduced(
        self,
        delta: float | None = ...,
        eta: float | None = ...,
    ) -> bool: ...
    @overload
    def randomize(
        self,
        density: float = ...,
        num_bound: int | Integer = ...,
        den_bound: int | Integer = ...,
        distribution: str | None = ...,
        nonzero: bool = ...,
    ) -> None: ...
    @overload
    def randomize(
        self,
        density: float = ...,
        nonzero: bool = ...,
        *args: object,
        **kwds: object,
    ) -> None: ...
    def __pari__(self) -> gen: ...
