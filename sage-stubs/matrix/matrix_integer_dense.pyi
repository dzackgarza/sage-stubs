from collections.abc import Callable, Mapping, Sequence
from typing import Literal, Self, overload

from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.fraction_field_element import FractionFieldElement
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
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


class Matrix_integer_dense(Matrix_dense[Integer]):
    def __init__(
        self,
        parent: MatrixSpace[Integer],
        entries: _IntegerMatrixEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
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

    @overload
    def hermite_form(
        self,
        algorithm: str = ...,
        proof: bool | None = ...,
        include_zero_rows: bool = ...,
        transformation: Literal[False] = ...,
        **kwds: object,
    ) -> Self: ...
    @overload
    def hermite_form(
        self,
        algorithm: str,
        proof: bool | None,
        include_zero_rows: bool,
        transformation: Literal[True],
        **kwds: object,
    ) -> tuple[Self, Self]: ...

    @overload
    def smith_form(
        self,
        transformation: Literal[False] = ...,
        integral: bool | None = ...,
    ) -> Self: ...
    @overload
    def smith_form(
        self,
        transformation: Literal[True],
        integral: bool | None = ...,
    ) -> tuple[Self, Self, Self]: ...

    def saturation(
        self,
        p: int | Integer = ...,
        proof: bool | None = ...,
        max_dets: int = ...,
    ) -> Self: ...
    def index_in_saturation(self, proof: bool | None = ...) -> Integer: ...
    def is_primitive(self) -> bool: ...
    def symplectic_form(self) -> Self: ...

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
    def BKZ(
        self,
        delta: float | None = ...,
        algorithm: str = ...,
        fp: str | None = ...,
        block_size: int = ...,
        prune: int = ...,
        use_givens: bool = ...,
        proof: bool | None = ...,
    ) -> Self: ...
    def is_LLL_reduced(
        self,
        delta: float | None = ...,
        eta: float | None = ...,
        algorithm: str = ...,
    ) -> bool: ...

    def rational_reconstruction(
        self,
        modulus: int | Integer,
    ) -> Matrix_rational_dense: ...
    def inverse(self) -> Matrix_rational_dense: ...
    __invert__ = inverse
    def inverse_of_unit(self) -> Self: ...
    def solve_right(
        self,
        B: Self | FreeModuleElement[Integer],
    ) -> Matrix_rational_dense | FreeModuleElement[Rational]: ...
    def solve_left(
        self,
        B: Self | FreeModuleElement[Integer],
    ) -> Matrix_rational_dense | FreeModuleElement[Rational]: ...
    def decomposition(
        self,
        **kwds: object,
    ) -> list[tuple[FreeModule_generic[Rational], bool]]: ...
    def randomize(
        self,
        density: float = ...,
        x: int | None = ...,
        y: int | None = ...,
        distribution: str | None = ...,
        **kwds: object,
    ) -> None: ...
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
