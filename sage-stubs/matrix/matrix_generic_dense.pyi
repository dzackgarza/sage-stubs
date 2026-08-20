from collections.abc import Callable, Mapping, Sequence
from typing import Generic, Literal, Self, TypeVar

from sage.matrix.matrix import Matrix
from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixData, MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


type GenericDenseEntries[_T: RingElement] = (
    Matrix[_T]
    | Sequence[ElementConstructorInput]
    | Sequence[Sequence[ElementConstructorInput]]
    | Mapping[tuple[int, int], ElementConstructorInput]
    | Callable[[int, int], ElementConstructorInput]
    | MatrixData[_T]
    | None
)


class Matrix_generic_dense(
    Matrix_dense[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        parent: MatrixSpace[_Scalar],
        entries: GenericDenseEntries[_Scalar] = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def _reverse_unsafe(self) -> None: ...
    def _pickle(self) -> tuple[list[_Scalar], Literal[0]]: ...
    def _unpickle(
        self,
        data: list[_Scalar],
        version: int,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def __bool__(self) -> bool: ...
    def _list(self) -> list[_Scalar]: ...
    def list(self) -> list[_Scalar]: ...
    def _dict(self) -> dict[tuple[int, int], _Scalar]: ...
    def dict(self, copy: bool = ...) -> dict[tuple[int, int], _Scalar]: ...
    def row(
        self,
        i: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[_Scalar]: ...
    def column(
        self,
        j: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[_Scalar]: ...
    def _add_(
        self,
        right: Matrix_generic_dense[_Scalar],
    ) -> Self: ...
    def _sub_(
        self,
        right: Matrix_generic_dense[_Scalar],
    ) -> Self: ...
    def _lmul_(self, scalar: _Scalar) -> Self: ...
    def _rmul_(self, scalar: _Scalar) -> Self: ...
    def __neg__(self) -> Self: ...
    def _multiply_classical(
        self,
        right: Matrix[_Scalar],
    ) -> Matrix[_Scalar]: ...
    def transpose(self) -> Self: ...
    T = transpose
    def antitranspose(self) -> Self: ...
    def randomize(
        self,
        density: float = ...,
        nonzero: bool = ...,
        *args: object,
        **kwds: object,
    ) -> None: ...
