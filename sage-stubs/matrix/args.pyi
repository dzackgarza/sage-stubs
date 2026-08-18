from collections.abc import Iterator, Mapping, Sequence
from typing import Generic, TypeVar

from sage.matrix.matrix import Matrix
from sage.matrix.matrix_space import MatrixIndexKeys, MatrixSpace
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class SparseEntry(Generic[_Scalar]):
    i: int
    j: int
    entry: _Scalar
    def __init__(self, i: int, j: int, entry: _Scalar) -> None: ...
    def __iter__(self) -> Iterator[int | _Scalar]: ...


class MatrixArgs(Generic[_Scalar]):
    base: Parent[_Scalar] | None
    nrows: int
    ncols: int
    entries: ElementConstructorInput
    sparse: bool
    row_keys: MatrixIndexKeys | None
    column_keys: MatrixIndexKeys | None
    space: MatrixSpace[_Scalar] | None
    kwds: dict[str, object]

    def __init__(
        self,
        *args: object,
        base_ring: Parent[_Scalar] | None = ...,
        nrows: int | Integer | None = ...,
        ncols: int | Integer | None = ...,
        entries: ElementConstructorInput = ...,
        sparse: bool | None = ...,
        row_keys: MatrixIndexKeys | None = ...,
        column_keys: MatrixIndexKeys | None = ...,
        space: MatrixSpace[_Scalar] | None = ...,
        **kwds: object,
    ) -> None: ...
    def __iter__(self) -> Iterator[_Scalar]: ...
    def iter(self, convert: bool = ..., sparse: bool = ...) -> Iterator[_Scalar | SparseEntry[_Scalar]]: ...
    def __len__(self) -> int: ...
    def finalized(self) -> MatrixArgs[_Scalar]: ...
    def set_nrows(self, nrows: int) -> None: ...
    def set_ncols(self, ncols: int) -> None: ...
    def set_sparse(self, sparse: bool) -> None: ...
    def set_row_keys(self, row_keys: MatrixIndexKeys) -> None: ...
    def set_column_keys(self, column_keys: MatrixIndexKeys) -> None: ...
    def set_space(self, space: MatrixSpace[_Scalar]) -> None: ...
    def matrix(self) -> Matrix[_Scalar]: ...
    def list(self) -> list[_Scalar]: ...
    def dict(self) -> dict[tuple[int, int], _Scalar]: ...
