from collections.abc import Iterable, Sequence
from typing import Generic, Literal, Self, TypeVar, overload

import numpy as np
from numpy.typing import DTypeLike, NDArray

from sage.matrix.matrix0 import Matrix as Matrix0
from sage.matrix.matrix_space import MatrixData, MatrixSpace
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import FieldElement, RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)
_OtherScalar = TypeVar("_OtherScalar", bound=RingElement)


class Matrix(
    Matrix0[_Scalar],
    Generic[_Scalar],
):
    def numpy(
        self,
        dtype: DTypeLike | None = ...,
        copy: bool = ...,
    ) -> NDArray[np.generic]: ...

    def matrix_over_field(self) -> Matrix[FieldElement]: ...
    def lift(self) -> Matrix[RingElement]: ...
    def lift_centered(self) -> Matrix[RingElement]: ...

    @overload
    def row_ambient_module(
        self,
        base_ring: None = ...,
        sparse: bool | None = ...,
    ) -> FreeModule_generic[_Scalar]: ...
    @overload
    def row_ambient_module(
        self,
        base_ring: Parent[_NewScalar],
        sparse: bool | None = ...,
    ) -> FreeModule_generic[_NewScalar]: ...

    @overload
    def column_ambient_module(
        self,
        base_ring: None = ...,
        sparse: bool | None = ...,
    ) -> FreeModule_generic[_Scalar]: ...
    @overload
    def column_ambient_module(
        self,
        base_ring: Parent[_NewScalar],
        sparse: bool | None = ...,
    ) -> FreeModule_generic[_NewScalar]: ...

    @overload
    def columns(
        self,
        copy: Literal[True] = ...,
    ) -> list[FreeModuleElement[_Scalar]]: ...
    @overload
    def columns(
        self,
        copy: Literal[False],
    ) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    @overload
    def columns(
        self,
        copy: bool,
    ) -> list[FreeModuleElement[_Scalar]] | tuple[FreeModuleElement[_Scalar], ...]: ...

    @overload
    def rows(
        self,
        copy: Literal[True] = ...,
    ) -> list[FreeModuleElement[_Scalar]]: ...
    @overload
    def rows(
        self,
        copy: Literal[False],
    ) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    @overload
    def rows(
        self,
        copy: bool,
    ) -> list[FreeModuleElement[_Scalar]] | tuple[FreeModuleElement[_Scalar], ...]: ...

    @overload
    def dense_columns(
        self,
        copy: Literal[True] = ...,
    ) -> list[FreeModuleElement[_Scalar]]: ...
    @overload
    def dense_columns(
        self,
        copy: Literal[False],
    ) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    @overload
    def dense_columns(
        self,
        copy: bool,
    ) -> list[FreeModuleElement[_Scalar]] | tuple[FreeModuleElement[_Scalar], ...]: ...

    @overload
    def dense_rows(
        self,
        copy: Literal[True] = ...,
    ) -> list[FreeModuleElement[_Scalar]]: ...
    @overload
    def dense_rows(
        self,
        copy: Literal[False],
    ) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    @overload
    def dense_rows(
        self,
        copy: bool,
    ) -> list[FreeModuleElement[_Scalar]] | tuple[FreeModuleElement[_Scalar], ...]: ...

    @overload
    def sparse_columns(
        self,
        copy: Literal[True] = ...,
    ) -> list[FreeModuleElement[_Scalar]]: ...
    @overload
    def sparse_columns(
        self,
        copy: Literal[False],
    ) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    @overload
    def sparse_columns(
        self,
        copy: bool,
    ) -> list[FreeModuleElement[_Scalar]] | tuple[FreeModuleElement[_Scalar], ...]: ...

    @overload
    def sparse_rows(
        self,
        copy: Literal[True] = ...,
    ) -> list[FreeModuleElement[_Scalar]]: ...
    @overload
    def sparse_rows(
        self,
        copy: Literal[False],
    ) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    @overload
    def sparse_rows(
        self,
        copy: bool,
    ) -> list[FreeModuleElement[_Scalar]] | tuple[FreeModuleElement[_Scalar], ...]: ...

    def column(
        self,
        i: int | Integer,
        from_list: bool = ...,
    ) -> FreeModuleElement[_Scalar]: ...
    def row(
        self,
        i: int | Integer,
        from_list: bool = ...,
    ) -> FreeModuleElement[_Scalar]: ...

    def stack(
        self,
        bottom: Matrix[_OtherScalar] | FreeModuleElement[_OtherScalar],
        subdivide: bool = ...,
    ) -> Matrix[RingElement]: ...
    def augment(
        self,
        right: Matrix[_OtherScalar] | FreeModuleElement[_OtherScalar],
        subdivide: bool = ...,
    ) -> Self: ...

    def matrix_from_columns(
        self,
        columns: Iterable[int | Integer],
    ) -> Self: ...
    def delete_columns(
        self,
        dcols: Iterable[int | Integer],
        check: bool = ...,
    ) -> Self: ...
    def matrix_from_rows(
        self,
        rows: Iterable[int | Integer],
    ) -> Self: ...
    def delete_rows(
        self,
        drows: Iterable[int | Integer],
        check: bool = ...,
    ) -> Self: ...
    def matrix_from_rows_and_columns(
        self,
        rows: Iterable[int | Integer],
        columns: Iterable[int | Integer],
    ) -> Self: ...
    def submatrix(
        self,
        row: int | Integer = ...,
        col: int | Integer = ...,
        nrows: int | Integer = ...,
        ncols: int | Integer = ...,
    ) -> Self: ...

    def set_row(
        self,
        row: int | Integer,
        v: Sequence[ElementConstructorInput] | FreeModuleElement[_Scalar],
    ) -> None: ...
    def set_column(
        self,
        col: int | Integer,
        v: Sequence[ElementConstructorInput] | FreeModuleElement[_Scalar],
    ) -> None: ...

    @overload
    def zero_pattern_matrix(
        self,
        ring: None = ...,
    ) -> Matrix[Integer]: ...
    @overload
    def zero_pattern_matrix(
        self,
        ring: Parent[_NewScalar],
    ) -> Matrix[_NewScalar]: ...

    def dense_matrix(self) -> Matrix[_Scalar]: ...
    def sparse_matrix(self) -> Matrix[_Scalar]: ...
    def matrix_space(
        self,
        nrows: int | Integer | None = ...,
        ncols: int | Integer | None = ...,
        sparse: bool | None = ...,
    ) -> MatrixSpace[_Scalar]: ...
    def new_matrix(
        self,
        nrows: int | Integer | None = ...,
        ncols: int | Integer | None = ...,
        entries: MatrixData[_Scalar] = ...,
        coerce: bool = ...,
        copy: bool = ...,
        sparse: bool | None = ...,
    ) -> Matrix[_Scalar]: ...
    def block_sum(
        self,
        other: Matrix[_OtherScalar],
    ) -> Matrix[RingElement]: ...
