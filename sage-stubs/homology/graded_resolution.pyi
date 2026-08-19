from collections.abc import Sequence
from typing import Generic, Literal, TypeVar, overload

from sage.homology.free_resolution import (
    FiniteFreeResolution,
    FiniteFreeResolution_free_module,
    FiniteFreeResolution_singular,
    ResolutionModule,
)
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
from sage.structure.element import Element, RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type GradingDegree = (
    int
    | Integer
    | FreeModuleElement[Integer]
    | tuple[int | Integer, ...]
)
type VariableDegrees = Sequence[GradingDegree]
type ModuleShifts = Sequence[GradingDegree]


class GradedFiniteFreeResolution(
    FiniteFreeResolution[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        module: ResolutionModule[_Scalar],
        degrees: VariableDegrees | None = ...,
        shifts: ModuleShifts | None = ...,
        name: str = ...,
        **kwds: Element | int | str | bool | None,
    ) -> None: ...
    def _repr_module(self, i: int | Integer) -> str: ...
    def shifts(self, i: int | Integer) -> list[GradingDegree]: ...

    @overload
    def betti(
        self,
        i: int | Integer,
        a: None = ...,
    ) -> dict[GradingDegree, int]: ...
    @overload
    def betti(
        self,
        i: int | Integer,
        a: GradingDegree,
    ) -> int: ...

    def K_polynomial(
        self,
        names: str | Sequence[str] | None = ...,
    ) -> LaurentPolynomial: ...


class GradedFiniteFreeResolution_free_module(
    GradedFiniteFreeResolution[_Scalar],
    FiniteFreeResolution_free_module[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        module: ResolutionModule[_Scalar],
        degrees: VariableDegrees | None = ...,
        *args: Element | int | str | bool,
        **kwds: Element | int | str | bool | None,
    ) -> None: ...


class GradedFiniteFreeResolution_singular(
    GradedFiniteFreeResolution[_Scalar],
    FiniteFreeResolution_singular[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        module: ResolutionModule[_Scalar],
        degrees: VariableDegrees | None = ...,
        shifts: ModuleShifts | None = ...,
        name: str = ...,
        algorithm: Literal["heuristic", "minimal", "shreyer", "standard"] = ...,
        **kwds: Element | int | str | bool | None,
    ) -> None: ...
