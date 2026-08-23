from typing import Generic, Literal, Self, TypeVar, overload

import numpy as np

from sage.modules.vector_numpy_dense import Vector_numpy_dense
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.infinity import MinusInfinity, PlusInfinity
from sage.structure.element import FieldElement
from sage.structure.parent import ElementConstructorInput

_DoubleScalar = TypeVar(
    "_DoubleScalar",
    bound=FieldElement,
    default=FieldElement,
)

type NormOrder = int | float | Literal["frob"] | PlusInfinity | MinusInfinity


class Vector_double_dense(
    Vector_numpy_dense[_DoubleScalar],
    Generic[_DoubleScalar],
):
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def _dot_product_(self, right: Self) -> _DoubleScalar: ...
    def _pairwise_product_(self, right: Self) -> Self: ...
    def _rmul_(self, left: ElementConstructorInput) -> Self: ...
    def _lmul_(self, right: ElementConstructorInput) -> Self: ...
    def inv_fft(self) -> Vector_complex_double_dense: ...
    @overload
    def fft(
        self,
        direction: Literal["forward", "backward"] = ...,
        inplace: Literal[False] = ...,
    ) -> Self: ...
    @overload
    def fft(
        self,
        direction: Literal["forward", "backward"] = ...,
        inplace: Literal[True] = ...,
    ) -> None: ...
    @overload
    def fft(
        self,
        direction: Literal["forward", "backward"] = ...,
        inplace: bool = ...,
    ) -> Self | None: ...
    def complex_vector(self) -> Vector_complex_double_dense: ...
    def zero_at(self, eps: float = ...) -> None: ...
    def norm(self, p: NormOrder = ...) -> _DoubleScalar | np.float64: ...
    def mean(self) -> _DoubleScalar: ...
    def variance(self, population: bool = ...) -> _DoubleScalar: ...
    def standard_deviation(self, population: bool = ...) -> _DoubleScalar: ...
    def stats_kurtosis(
        self,
        fisher: bool = ...,
        bias: bool = ...,
    ) -> _DoubleScalar: ...
    def prod(self) -> _DoubleScalar: ...
    def sum(self) -> _DoubleScalar: ...


from sage.modules.vector_complex_double_dense import Vector_complex_double_dense
