from collections.abc import Sequence
from typing import Self

from sage.matrix.matrix_complex_double_dense import Matrix_complex_double_dense
from sage.modules.vector_double_dense import Vector_double_dense
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.real_double import RealDoubleElement
from sage.structure.parent import ElementConstructorInput


class Vector_complex_double_dense(
    Vector_double_dense[ComplexDoubleElement]
):
    def __init__(
        self,
        parent: object,
        entries: Sequence[complex | ComplexDoubleElement | ElementConstructorInput] = ...,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def list(self, copy: bool = ...) -> list[ComplexDoubleElement]: ...
    def dot_product(
        self,
        right: Vector_complex_double_dense,
    ) -> ComplexDoubleElement: ...
    def hermitian_inner_product(
        self,
        right: Vector_complex_double_dense,
    ) -> ComplexDoubleElement: ...
    inner_product = hermitian_inner_product
    def pairwise_product(self, right: Vector_complex_double_dense) -> Self: ...
    def norm(self, p: int | float | str = ...) -> float: ...
    def conjugate(self) -> Self: ...
    def real(self) -> Vector_real_double_dense: ...
    def imag(self) -> Vector_real_double_dense: ...
    def row(self) -> Matrix_complex_double_dense: ...
    def column(self) -> Matrix_complex_double_dense: ...


from sage.modules.vector_real_double_dense import Vector_real_double_dense
