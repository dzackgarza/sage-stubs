from typing import Generic, Literal, Self, TypeVar, overload

from sage.modules.vector_numpy_dense import Vector_numpy_dense
from sage.rings.infinity import MinusInfinity, PlusInfinity
from sage.rings.real_double import RealDoubleElement
from sage.structure.element import Element, FieldElement, RingElement

_DoubleScalar = TypeVar(
    "_DoubleScalar",
    bound=FieldElement,
    default=FieldElement,
)

type NormOrder = int | float | RingElement | PlusInfinity | MinusInfinity
type FourierDirection = Literal["forward", "backward"]


class Vector_double_dense(
    Vector_numpy_dense[_DoubleScalar],
    Generic[_DoubleScalar],
):
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def _dot_product_(self, right: Self) -> _DoubleScalar: ...
    def _pairwise_product_(self, right: Self) -> Self: ...
    def _rmul_(self, left: Element) -> Self: ...
    def _lmul_(self, right: Element) -> Self: ...
    @overload
    def inv_fft(
        self,
        algorithm: str = ...,
        inplace: Literal[False] = ...,
    ) -> Vector_complex_double_dense | Self: ...
    @overload
    def inv_fft(
        self,
        algorithm: str = ...,
        inplace: Literal[True] = ...,
    ) -> Self | None: ...
    @overload
    def inv_fft(
        self,
        algorithm: str = ...,
        inplace: bool = ...,
    ) -> Vector_complex_double_dense | Self | None: ...
    @overload
    def fft(
        self,
        direction: FourierDirection = ...,
        algorithm: str = ...,
        inplace: Literal[False] = ...,
    ) -> Vector_complex_double_dense | Self: ...
    @overload
    def fft(
        self,
        direction: FourierDirection = ...,
        algorithm: str = ...,
        inplace: Literal[True] = ...,
    ) -> Self | None: ...
    @overload
    def fft(
        self,
        direction: FourierDirection = ...,
        algorithm: str = ...,
        inplace: bool = ...,
    ) -> Vector_complex_double_dense | Self | None: ...
    def complex_vector(self) -> Vector_complex_double_dense: ...
    def zero_at(self, eps: float | RingElement) -> Self: ...
    def norm(self, p: NormOrder = ...) -> RealDoubleElement: ...
    def mean(self) -> _DoubleScalar: ...
    def variance(self, population: bool = ...) -> _DoubleScalar: ...
    def standard_deviation(self, population: bool = ...) -> _DoubleScalar: ...
    def stats_kurtosis(self) -> _DoubleScalar: ...
    def prod(self) -> _DoubleScalar: ...
    def sum(self) -> _DoubleScalar: ...


from sage.modules.vector_complex_double_dense import Vector_complex_double_dense
