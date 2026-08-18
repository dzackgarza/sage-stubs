from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import TypeVar, overload

from sage.matrix.matrix import Matrix as MatrixClass
from sage.matrix.matrix_space import MatrixIndexKeys, MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type MatrixEntries = (
    MatrixClass[_Scalar]
    | FreeModuleElement[_Scalar]
    | Sequence[ElementConstructorInput]
    | Sequence[Sequence[ElementConstructorInput]]
    | Mapping[tuple[int, int], ElementConstructorInput]
    | Callable[[int, int], ElementConstructorInput]
)


class MatrixFactory:
    @overload
    def __call__(
        self,
        ring: Parent[_Scalar],
        nrows: int | Integer,
        ncols: int | Integer,
        entries: MatrixEntries[_Scalar] | ElementConstructorInput = ...,
        *,
        sparse: bool | None = ...,
        immutable: bool = ...,
    ) -> MatrixClass[_Scalar]: ...
    @overload
    def __call__(
        self,
        ring: Parent[_Scalar],
        entries: MatrixEntries[_Scalar],
        *,
        sparse: bool | None = ...,
        immutable: bool = ...,
    ) -> MatrixClass[_Scalar]: ...
    @overload
    def __call__(
        self,
        entries: MatrixEntries[RingElement],
        *,
        sparse: bool | None = ...,
        immutable: bool = ...,
    ) -> MatrixClass[RingElement]: ...
    def diagonal(
        self,
        entries: Iterable[ElementConstructorInput],
        ring: Parent[_Scalar] | None = ...,
    ) -> MatrixClass[_Scalar]: ...
    def identity(self, ring: Parent[_Scalar], n: int | Integer) -> MatrixClass[_Scalar]: ...
    def zero(
        self,
        ring: Parent[_Scalar],
        nrows: int | Integer,
        ncols: int | Integer | None = ...,
    ) -> MatrixClass[_Scalar]: ...
    def block(self, blocks: Iterable[MatrixClass[_Scalar] | None]) -> MatrixClass[_Scalar]: ...


matrix: MatrixFactory
Matrix = matrix


def identity_matrix(
    ring: Parent[_Scalar],
    n: int | Integer,
) -> MatrixClass[_Scalar]: ...
def zero_matrix(
    ring: Parent[_Scalar],
    nrows: int | Integer,
    ncols: int | Integer | None = ...,
) -> MatrixClass[_Scalar]: ...
def diagonal_matrix(
    ring: Parent[_Scalar],
    entries: Iterable[ElementConstructorInput],
) -> MatrixClass[_Scalar]: ...
def matrix_space(
    ring: Parent[_Scalar],
    nrows: int | Integer,
    ncols: int | Integer | None = ...,
    sparse: bool = ...,
) -> MatrixSpace[_Scalar]: ...
