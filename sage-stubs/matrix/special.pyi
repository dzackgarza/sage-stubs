from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import ParamSpec, TypeVar, overload

from sage.matrix.matrix import Matrix
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_P = ParamSpec("_P")
_Return = TypeVar("_Return")

type MatrixBlock[_Scalar: RingElement] = (
    Matrix[_Scalar]
    | ElementConstructorInput
    | None
)
type VectorData[_Scalar: RingElement] = (
    Sequence[_Scalar | ElementConstructorInput]
    | FreeModuleElement[_Scalar]
)


@overload
def matrix_method(
    func: Callable[_P, _Return],
    name: str | None = ...,
) -> Callable[_P, _Return]: ...


@overload
def matrix_method(
    func: None = ...,
    name: str | None = ...,
) -> Callable[[Callable[_P, _Return]], Callable[_P, _Return]]: ...


@overload
def column_matrix(
    ring: Parent[_Scalar],
    *args: object,
    **kwds: object,
) -> Matrix[_Scalar]: ...


@overload
def column_matrix(
    *args: object,
    **kwds: object,
) -> Matrix[RingElement]: ...


def random_matrix(
    ring: Parent[_Scalar],
    nrows: int | Integer,
    ncols: int | Integer | None = ...,
    algorithm: str = ...,
    implementation: str | type[Matrix[_Scalar]] | None = ...,
    *args: object,
    **kwds: object,
) -> Matrix[_Scalar]: ...


@overload
def diagonal_matrix(
    arg0: Parent[_Scalar],
    arg1: Iterable[_Scalar | ElementConstructorInput],
    arg2: None = ...,
    sparse: bool = ...,
) -> Matrix[_Scalar]: ...


@overload
def diagonal_matrix(
    arg0: Parent[_Scalar],
    arg1: int | Integer,
    arg2: Iterable[_Scalar | ElementConstructorInput],
    sparse: bool = ...,
) -> Matrix[_Scalar]: ...


@overload
def diagonal_matrix(
    arg0: Iterable[_Scalar | ElementConstructorInput],
    arg1: None = ...,
    arg2: None = ...,
    sparse: bool = ...,
) -> Matrix[_Scalar]: ...


@overload
def diagonal_matrix(
    arg0: int | Integer,
    arg1: Iterable[ElementConstructorInput],
    arg2: None = ...,
    sparse: bool = ...,
) -> Matrix[RingElement]: ...


@overload
def identity_matrix(
    ring: Parent[_Scalar],
    n: int | Integer = ...,
    sparse: bool = ...,
) -> Matrix[_Scalar]: ...


@overload
def identity_matrix(
    ring: int | Integer,
    n: int | Integer = ...,
    sparse: bool = ...,
) -> Matrix[Integer]: ...


@overload
def lehmer(
    ring: Parent[_Scalar],
    n: int | Integer = ...,
) -> Matrix[_Scalar]: ...


@overload
def lehmer(
    ring: int | Integer,
    n: int | Integer = ...,
) -> Matrix[Rational]: ...


@overload
def zero_matrix(
    ring: Parent[_Scalar],
    nrows: int | Integer | None = ...,
    ncols: int | Integer | None = ...,
    sparse: bool = ...,
) -> Matrix[_Scalar]: ...


@overload
def zero_matrix(
    ring: int | Integer,
    nrows: int | Integer | None = ...,
    ncols: int | Integer | None = ...,
    sparse: bool = ...,
) -> Matrix[Integer]: ...


@overload
def ones_matrix(
    ring: Parent[_Scalar],
    nrows: int | Integer | None = ...,
    ncols: int | Integer | None = ...,
    sparse: bool = ...,
) -> Matrix[_Scalar]: ...


@overload
def ones_matrix(
    ring: int | Integer,
    nrows: int | Integer | None = ...,
    ncols: int | Integer | None = ...,
    sparse: bool = ...,
) -> Matrix[Integer]: ...


@overload
def elementary_matrix(
    arg0: MatrixSpace[_Scalar],
    arg1: int | Integer | None = ...,
    **kwds: ElementConstructorInput,
) -> Matrix[_Scalar]: ...


@overload
def elementary_matrix(
    arg0: Parent[_Scalar],
    arg1: int | Integer | None = ...,
    **kwds: ElementConstructorInput,
) -> Matrix[_Scalar]: ...


@overload
def elementary_matrix(
    arg0: int | Integer,
    arg1: int | Integer | None = ...,
    **kwds: ElementConstructorInput,
) -> Matrix[Integer]: ...


def circulant(
    v: VectorData[_Scalar],
    sparse: bool | None = ...,
) -> Matrix[_Scalar]: ...


def block_matrix(
    *args: (
        Parent[_Scalar]
        | MatrixSpace[_Scalar]
        | MatrixBlock[_Scalar]
        | Sequence[MatrixBlock[_Scalar]]
        | Sequence[Sequence[MatrixBlock[_Scalar]]]
        | int
        | Integer
    ),
    **kwds: object,
) -> Matrix[_Scalar]: ...


def block_diagonal_matrix(
    *sub_matrices: Matrix[_Scalar],
    **kwds: object,
) -> Matrix[_Scalar]: ...


def jordan_block(
    eigenvalue: _Scalar,
    size: int | Integer,
    sparse: bool = ...,
) -> Matrix[_Scalar]: ...


def companion_matrix(
    poly: Polynomial,
    format: str = ...,
) -> Matrix[RingElement]: ...


def random_rref_matrix(
    parent: MatrixSpace[_Scalar],
    num_pivots: int | Integer,
) -> Matrix[_Scalar]: ...


def random_echelonizable_matrix(
    parent: MatrixSpace[_Scalar],
    rank: int | Integer,
    upper_bound: int | Integer | None = ...,
    max_tries: int | Integer = ...,
) -> Matrix[_Scalar]: ...


def random_subspaces_matrix(
    parent: MatrixSpace[_Scalar],
    rank: int | Integer | None = ...,
) -> Matrix[_Scalar]: ...


def random_unimodular_matrix(
    parent: MatrixSpace[_Scalar],
    upper_bound: int | Integer | None = ...,
    max_tries: int | Integer = ...,
) -> Matrix[_Scalar]: ...


def random_unitary_matrix(
    parent: MatrixSpace[_Scalar],
) -> Matrix[_Scalar]: ...


def random_bistochastic_matrix(
    parent: MatrixSpace[_Scalar],
) -> Matrix[_Scalar]: ...


def random_diagonalizable_matrix(
    parent: MatrixSpace[_Scalar],
    eigenvalues: Sequence[_Scalar] | None = ...,
    dimensions: Sequence[int | Integer] | None = ...,
) -> Matrix[_Scalar]: ...


@overload
def vector_on_axis_rotation_matrix(
    v: VectorData[_Scalar],
    i: int | Integer,
    ring: Parent[_Scalar],
) -> Matrix[_Scalar]: ...


@overload
def vector_on_axis_rotation_matrix(
    v: Sequence[ElementConstructorInput] | FreeModuleElement[RingElement],
    i: int | Integer,
    ring: None = ...,
) -> Matrix[RingElement]: ...


@overload
def ith_to_zero_rotation_matrix(
    v: VectorData[_Scalar],
    i: int | Integer,
    ring: Parent[_Scalar],
) -> Matrix[_Scalar]: ...


@overload
def ith_to_zero_rotation_matrix(
    v: Sequence[ElementConstructorInput] | FreeModuleElement[RingElement],
    i: int | Integer,
    ring: None = ...,
) -> Matrix[RingElement]: ...


@overload
def hilbert(
    dim: int | Integer,
    ring: Parent[_Scalar],
) -> Matrix[_Scalar]: ...


@overload
def hilbert(
    dim: int | Integer,
    ring: None = ...,
) -> Matrix[Rational]: ...


@overload
def vandermonde(
    v: VectorData[_Scalar],
    ring: Parent[_Scalar],
) -> Matrix[_Scalar]: ...


@overload
def vandermonde(
    v: Sequence[ElementConstructorInput] | FreeModuleElement[RingElement],
    ring: None = ...,
) -> Matrix[RingElement]: ...


@overload
def toeplitz(
    c: VectorData[_Scalar],
    r: VectorData[_Scalar],
    ring: Parent[_Scalar],
) -> Matrix[_Scalar]: ...


@overload
def toeplitz(
    c: Sequence[ElementConstructorInput] | FreeModuleElement[RingElement],
    r: Sequence[ElementConstructorInput] | FreeModuleElement[RingElement],
    ring: None = ...,
) -> Matrix[RingElement]: ...


@overload
def hankel(
    c: VectorData[_Scalar],
    r: VectorData[_Scalar] | None = ...,
    ring: Parent[_Scalar] = ...,
) -> Matrix[_Scalar]: ...


@overload
def hankel(
    c: Sequence[ElementConstructorInput] | FreeModuleElement[RingElement],
    r: Sequence[ElementConstructorInput] | FreeModuleElement[RingElement] | None = ...,
    ring: None = ...,
) -> Matrix[RingElement]: ...
