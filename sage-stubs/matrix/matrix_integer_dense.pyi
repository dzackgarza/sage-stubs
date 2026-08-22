from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Literal, Self, overload

from sage.interfaces.singular import Singular, SingularElement
from sage.libs.pari.gen import gen
from sage.matrix.matrix import Matrix
from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.fraction_field_element import FractionFieldElement
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.structure.element import Expression
from sage.structure.parent import ElementConstructorInput


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
    def _list(self) -> list[Integer]: ...
    def list(self) -> list[Integer]: ...
    def row(
        self,
        i: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[Integer]: ...
    def column(
        self,
        j: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[Integer]: ...
    def transpose(self) -> Self: ...
    def antitranspose(self) -> Self: ...
    def stack(
        self,
        bottom: Self | FreeModuleElement[Integer],
        subdivide: bool = ...,
    ) -> Self: ...
    def augment(
        self,
        right: Self | FreeModuleElement[Integer],
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
        algorithm: str = ...,
        proof: bool | None = ...,
        stabilize: int = ...,
    ) -> Integer: ...
    det = determinant
    def rank(self, algorithm: str = ...) -> int: ...
    def height(self) -> Integer: ...
    def content(self) -> Integer: ...
    gcd = content
    def characteristic_polynomial(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial: ...
    charpoly = characteristic_polynomial
    def minimal_polynomial(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial: ...
    minpoly = minimal_polynomial
    def elementary_divisors(self, algorithm: str = ...) -> list[Integer]: ...
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
    hermite_form = echelon_form

    @overload
    def smith_form(
        self,
        transformation: Literal[True] = ...,
        integral: bool | None = ...,
    ) -> tuple[Self, Self, Self]: ...
    @overload
    def smith_form(
        self,
        transformation: Literal[False],
        integral: bool | None = ...,
    ) -> Self: ...
    @overload
    def smith_form(
        self,
        transformation: bool,
        integral: bool | None = ...,
    ) -> Self | tuple[Self, Self, Self]: ...

    @overload
    def frobenius_form(
        self,
        flag: Literal[0] = ...,
        var: str = ..,
    ) -> Self: ...
    @overload
    def frobenius_form(
        self,
        flag: Literal[1],
        var: str = ..,
    ) -> list[Polynomial]: ...
    @overload
    def frobenius_form(
        self,
        flag: Literal[2],
        var: str = ..,
    ) -> tuple[Matrix_rational_dense, Matrix_rational_dense]: ..
    @overload
    def frobenius_form(
        self,
        flag: int | Integer = ...,
        var: str = ...,
    ) -> (
        Self
        | list[Polynomial]
        | tuple[Matrix_rational_dense, Matrix_rational_dense]
    ): ...

    def saturation(
        self,
        p: int | Integer = ..,
        proof: bool | None = ..,
        max_dets: int = ...,
    ) -> Self: ...
    def index_in_saturation(self, proof: bool | None = ...) -> Integer: ...
    def is_primitive(self) -> bool: ...
    def symplectic_form(self) -> tuple[Self, Self]: ...

    @overload
    def LLL\(
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
    def row_space(self) -> FreeModule_generic[Integer]: ...
    def column_space(self) -> FreeModule_generic[Integer]: ...
    def image(self) -> FreeModule_generic[Integer]: ...

    def rational_reconstruction(
        self,
        modulus: int | Integer,
    ) -> Matrix_rational_dense: ...
    def inverse(self) -> Matrix_rational_dense: ...
    __invert__ = inverse
    def inverse_of_unit(self) -> Self: ...
    @overload
    def solve_right(
        self,
        B: Self,
        check: bool = ...,
        *,
        extend: bool = ...,
    ) -> Matrix_rational_dense: ...
    @overload
    def solve_right(
        self,
        B: FreeModuleElement[Integer],
        check: bool = ...,
        *,
        extend: bool = ...,
    ) -> FreeModuleElement[Rational]: ...
    @overload
    def solve_left(
        self,
        B: Self,
        check: bool = ...,
        *,
        extend: bool = ...,
    ) -> Matrix_rational_dense: ...
    @overload
    def solve_left(
        self,
        B: FreeModuleElement[Integer],
        check: bool = ...,
        *,
        extend: bool = ...,
    ) -> FreeModuleElement[Rational]: ...

    @overload
    def decomposition(
        self,
        *,
        dual: Literal[False] = ...,
        **kwds: object,
    ) -> list[_IntegerDecompositionFactor]: ...
    @overload
    def decomposition(
        self,
        *,
        dual: Literal[True],
        **kwds: object,
    ) -> (
        list[_IntegerDecompositionFactor]
        | tuple[
            list[_IntegerDecompositionFactor],
            list[_IntegerDecompositionFactor],
        ]
    ): ...
    @overload
    def decomposition(
        self,
        *,
        dual: bool = ...,
        **kwds: object,
    ) -> (
        list[_IntegerDecompositionFactor]
        | tuple[
            list[_IntegerDecompositionFactor],
            list[_IntegerDecompositionFactor],
        ]
    ): ...

    def randomize(
        self,
        density: float = ...,
        x: int | Integer | None = ...,
        y: int | Integer | None = ...,
        distribution: str | None = ...,
        nonzero: bool = ...,
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
    ) -> tuple[Polynomial, list[Polynomial | FractionFieldElement]]: ...


from sage.matrix.matrix_rational_dense import Matrix_rational_dense
