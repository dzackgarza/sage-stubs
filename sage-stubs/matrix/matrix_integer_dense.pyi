from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Literal, Never, Self, overload

from sage.interfaces.singular import Singular, SingularElement
from sage.libs.pari.gen import gen
from sage.matrix.matrix import Matrix
from sage.matrix.matrix1 import Matrix as Matrix1
from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.fraction_field_element import FractionFieldElement
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import Expression, RingElement
from sage.structure.parent import ElementConstructorInput, Parent

type _IntegerMatrixEntries = (
    int
    | Integer
    | Sequence[int | Integer | ElementConstructorInput]
    | Sequence[Sequence[int | Integer | ElementConstructorInput]]
    | Mapping[tuple[int, int], int | Integer | ElementConstructorInput]
    | Callable[[int, int], int | Integer | ElementConstructorInput]
    | ElementConstructorInput
    | None
)
type _IntegerDecompositionFactor = tuple[
    FreeModule_generic[Integer],
    bool,
]

type _List[_T] = list[_T]

class Matrix_integer_dense(Matrix_dense[Integer]):
    def __init__(
        self,
        parent: MatrixSpace[Integer],
        entries: _IntegerMatrixEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def __bool__(self) -> bool: ...
    def is_one(self) -> bool: ...
    def _list(self) -> _List[Integer]: ...
    def list(self) -> _List[Integer]: ...
    def row(
        self,
        i: int | Integer,
        from_list: bool = ...,
    ) -> FreeModuleElement[Integer]: ...
    def column(
        self,
        j: int | Integer,
        from_list: bool = ...,
    ) -> FreeModuleElement[Integer]: ...
    def transpose(self) -> Self: ...
    def antitranspose(self) -> Self: ...
    def augment[T: RingElement](
        self,
        right: Matrix1[T] | FreeModuleElement[T],
        subdivide: bool = ...,
    ) -> Self: ...
    def insert_row(
        self,
        index: int | Integer,
        row: Sequence[int | Integer] | FreeModuleElement[Integer],
    ) -> Self: ...
    def __neg__(self) -> Self: ...
    @overload
    def __pow__(
        self,
        n: int | Integer,
        dummy: None = ...,
    ) -> Self | Matrix_rational_dense: ...
    @overload
    def __pow__(
        self,
        n: Expression,
        dummy: None = ...,
    ) -> Matrix[Expression]: ...
    def trace(self) -> Integer: ...
    def determinant(
        self,
        algorithm: str | None = ...,
        proof: bool | None = ...,
        stabilize: int = ...,
    ) -> Integer: ...
    det = determinant
    def rank(self, algorithm: str = ...) -> int: ...
    def height(self) -> Integer: ...
    def content(self) -> Integer: ...
    gcd = content
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
    def elementary_divisors(self, algorithm: str | None = ...) -> _List[Integer]: ...
    def pivots(self) -> tuple[int, ...]: ...
    def prod_of_row_sums(
        self,
        cols: Iterable[int | Integer],
    ) -> Integer: ...
    @overload
    def echelon_form(
        self,
        algorithm: str = ...,
        proof: bool | None = ...,
        include_zero_rows: bool = ...,
        transformation: Literal[False] = ...,
        D: int | Integer | None = ...,
    ) -> Self: ...
    @overload
    def echelon_form(
        self,
        algorithm: str,
        proof: bool | None,
        include_zero_rows: bool,
        transformation: Literal[True],
        D: int | Integer | None = ...,
    ) -> tuple[Self, Self]: ...
    @overload
    def echelon_form(
        self,
        algorithm: str = ...,
        proof: bool | None = ...,
        include_zero_rows: bool = ...,
        transformation: bool = ...,
        D: int | Integer | None = ...,
    ) -> Self | tuple[Self, Self]: ...
    @overload
    def echelon_form(
        self,
        algorithm: str = ...,
        cutoff: int = ...,
        **kwds: object,
    ) -> Never: ...
    @overload
    def hermite_form(
        self,
        algorithm: str = ...,
        proof: bool | None = ...,
        include_zero_rows: bool = ...,
        transformation: Literal[False] = ...,
        D: int | Integer | None = ...,
    ) -> Self: ...
    @overload
    def hermite_form(
        self,
        algorithm: str,
        proof: bool | None,
        include_zero_rows: bool,
        transformation: Literal[True],
        D: int | Integer | None = ...,
    ) -> tuple[Self, Self]: ...
    @overload
    def hermite_form(
        self,
        include_zero_rows: bool = ...,
        transformation: Literal[False] = ...,
    ) -> Self: ...
    @overload
    def hermite_form(
        self,
        include_zero_rows: bool,
        transformation: Literal[True],
    ) -> tuple[Self, Self]: ...
    @overload
    def smith_form(
        self,
        transformation: Literal[True] = ...,
        integral: Parent | bool | None = ...,
        exact: bool = ...,
    ) -> tuple[Self, Self, Self]: ...
    @overload
    def smith_form(
        self,
        transformation: Literal[False],
        integral: Parent | bool | None = ...,
        exact: bool = ...,
    ) -> Self: ...
    @overload
    def smith_form(
        self,
        transformation: bool,
        integral: Parent | bool | None = ...,
        exact: bool = ...,
    ) -> Self | tuple[Self, Self, Self]: ...
    @overload
    def frobenius_form(
        self,
        flag: Literal[0] = ...,
        var: str = ...,
    ) -> Self: ...
    @overload
    def frobenius_form(
        self,
        flag: Literal[1],
        var: str = ...,
    ) -> _List[Polynomial]: ...
    @overload
    def frobenius_form(
        self,
        flag: Literal[2],
        var: str = ...,
    ) -> tuple[Matrix_rational_dense, Matrix_rational_dense]: ...
    @overload
    def frobenius_form(
        self,
        flag: int | Integer = ...,
        var: str = ...,
    ) -> (
        Self | _List[Polynomial] | tuple[Matrix_rational_dense, Matrix_rational_dense]
    ): ...
    def saturation(
        self,
        p: int | Integer = ...,
        proof: bool | None = ...,
        max_dets: int = ...,
    ) -> Self: ...
    def index_in_saturation(self, proof: bool | None = ...) -> Integer: ...
    def is_primitive(self) -> bool: ...
    def symplectic_form(self) -> tuple[Self, Self]: ...
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
    ) -> tuple[Self, Self]: ...
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
    ) -> Self | tuple[Self, Self]: ...
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
        algorithm: str = ...,
    ) -> bool: ...
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
    ) -> FreeModule_generic[Integer]: ...
    def left_kernel(
        self,
        *args: object,
        **kwds: object,
    ) -> FreeModule_generic[Integer]: ...
    def column_space(self) -> FreeModule_generic[Integer]: ...
    def image(self) -> FreeModule_generic[Integer]: ...
    def rational_reconstruction(
        self,
        modulus: int | Integer,
    ) -> Matrix_rational_dense: ...
    def inverse(self) -> Matrix_rational_dense: ...
    __invert__ = inverse
    @overload
    def inverse_of_unit(self) -> Self: ...
    @overload
    def inverse_of_unit(self, algorithm: Literal["df"] | None) -> Never: ...
    @overload
    def decomposition(
        self,
        *,
        dual: Literal[False] = ...,
        **kwds: object,
    ) -> _List[_IntegerDecompositionFactor]: ...
    @overload
    def decomposition(
        self,
        *,
        dual: Literal[True],
        **kwds: object,
    ) -> (
        _List[_IntegerDecompositionFactor]
        | tuple[
            _List[_IntegerDecompositionFactor],
            _List[_IntegerDecompositionFactor],
        ]
    ): ...
    @overload
    def decomposition(
        self,
        *,
        dual: bool = ...,
        **kwds: object,
    ) -> (
        _List[_IntegerDecompositionFactor]
        | tuple[
            _List[_IntegerDecompositionFactor],
            _List[_IntegerDecompositionFactor],
        ]
    ): ...
    @overload
    def decomposition(
        self,
        algorithm: str = ...,
        is_diagonalizable: bool = ...,
        dual: Literal[False] = ...,
    ) -> _List[_IntegerDecompositionFactor]: ...
    @overload
    def decomposition(
        self,
        algorithm: str,
        is_diagonalizable: bool,
        dual: Literal[True],
    ) -> tuple[
        _List[_IntegerDecompositionFactor],
        _List[_IntegerDecompositionFactor],
    ]: ...
    @overload
    def randomize(
        self,
        density: float = ...,
        x: int | Integer | None = ...,
        y: int | Integer | None = ...,
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
    def _singular_(
        self,
        singular: Singular | None = ...,
    ) -> SingularElement: ...
    def p_minimal_polynomials(
        self,
        p: int | Integer,
        s_max: int | Integer | None = ...,
    ) -> dict[int, Polynomial]: ...
    def null_ideal(self, b: int | Integer = ...) -> Ideal_generic: ...
    def integer_valued_polynomials_generators(
        self,
    ) -> tuple[Polynomial, _List[Polynomial | FractionFieldElement]]: ...
