from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from typing import Generic, Literal, Never, Self, TypeVar, overload

from sage.matrix.matrix import Matrix
from sage.matrix.matrix_space import MatrixIndexKeys, MatrixSpace
from sage.modules.with_basis.morphism import ModuleMorphism
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_Entry = TypeVar("_Entry", default=object)

type MatrixArgsEntries[_Scalar: RingElement] = (
    Matrix[_Scalar]
    | Sequence[ElementConstructorInput]
    | Sequence[Sequence[ElementConstructorInput]]
    | Mapping[tuple[int, int], ElementConstructorInput]
    | Callable[[object, object], ElementConstructorInput]
    | Iterable[ElementConstructorInput]
    | ElementConstructorInput
    | None
)


class SparseEntry(Generic[_Entry]):
    i: int
    j: int
    entry: _Entry

    def __init__(self, i: int, j: int, entry: _Entry) -> None: ...
    def __iter__(self) -> Iterator[int | _Entry]: ...
    def __repr__(self) -> str: ...


class MatrixArgs(Generic[_Scalar]):
    space: Parent | None
    base: Parent[_Scalar] | None
    nrows: int
    ncols: int
    row_keys: MatrixIndexKeys | None
    column_keys: MatrixIndexKeys | None
    entries: MatrixArgsEntries[_Scalar]
    sparse: bool
    kwds: dict[str, object]

    def __init__(
        self,
        *args: object,
        base_ring: Parent[_Scalar] | None = ...,
        nrows: int | None = ...,
        ncols: int | None = ...,
        entries: MatrixArgsEntries[_Scalar] = ...,
        sparse: bool | None = ...,
        row_keys: MatrixIndexKeys | None = ...,
        column_keys: MatrixIndexKeys | None = ...,
        space: Parent | None = ...,
        **kwds: object,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __reduce__(self) -> Never: ...
    def __iter__(self) -> Iterator[_Scalar]: ...

    @overload
    def iter(
        self,
        convert: Literal[True] = ...,
        sparse: Literal[False] = ...,
    ) -> Iterator[_Scalar]: ...

    @overload
    def iter(
        self,
        convert: Literal[False],
        sparse: Literal[False] = ...,
    ) -> Iterator[ElementConstructorInput]: ...

    @overload
    def iter(
        self,
        convert: Literal[True] = ...,
        sparse: Literal[True] = ...,
    ) -> Iterator[SparseEntry[_Scalar]]: ...

    @overload
    def iter(
        self,
        convert: Literal[False],
        sparse: Literal[True],
    ) -> Iterator[SparseEntry[ElementConstructorInput]]: ...

    @overload
    def iter(
        self,
        convert: bool = ...,
        sparse: bool = ...,
    ) -> Iterator[_Scalar | ElementConstructorInput | SparseEntry]: ...

    def __len__(self) -> int: ...

    @overload
    def matrix(self, convert: Literal[True] = ...) -> Matrix[_Scalar]: ...

    @overload
    def matrix(self, convert: Literal[False]) -> Matrix[RingElement]: ...

    def element(
        self,
        immutable: bool = ...,
    ) -> Matrix[_Scalar] | ModuleMorphism: ...

    @overload
    def list(self, convert: Literal[True] = ...) -> list[_Scalar]: ...

    @overload
    def list(self, convert: Literal[False]) -> list[ElementConstructorInput]: ...

    @overload
    def dict(self, convert: Literal[True] = ...) -> dict[tuple[int, int], _Scalar]: ...

    @overload
    def dict(
        self,
        convert: Literal[False],
    ) -> dict[tuple[int, int], ElementConstructorInput]: ...

    def set_column_keys(self, column_keys: MatrixIndexKeys) -> int: ...
    def set_row_keys(self, row_keys: MatrixIndexKeys) -> int: ...
    def set_space(self, space: Parent) -> int: ...
    def finalized(self) -> Self: ...


def MatrixArgs_init(
    space: Parent,
    entries: MatrixArgsEntries[_Scalar],
) -> MatrixArgs[_Scalar]: ...
