from typing import Literal, overload

from sage.plot.graphics import Graphics
from sage.rings.complex_mpfr import ComplexNumber
from sage.structure.parent import Parent


type FourierValue = int | float | complex | ComplexNumber | tuple[float, float]
type FourierCoefficient = tuple[float, float]
type PlotStyle = Literal["rect", "polar"]
type PlotOption = bool | int | float | str | tuple[float, float, float] | None


def FastFourierTransform(
    size: int,
    base_ring: Parent | None = None,
) -> FastFourierTransform_complex: ...
FFT = FastFourierTransform


class FastFourierTransform_base:
    def __init__(self) -> None: ...


class FastFourierTransform_complex(FastFourierTransform_base):
    def __init__(self, n: int, stride: int = 1) -> None: ...
    def __len__(self) -> int: ...
    def __setitem__(self, i: int, xy: FourierValue) -> None: ...
    @overload
    def __getitem__(self, i: int) -> FourierCoefficient: ...
    @overload
    def __getitem__(self, i: slice) -> list[FourierCoefficient]: ...
    def __repr__(self) -> str: ...
    def plot(
        self,
        style: PlotStyle = "rect",
        xmin: int | None = None,
        xmax: int | None = None,
        **args: PlotOption,
    ) -> Graphics: ...
    def forward_transform(self) -> None: ...
    def inverse_transform(self) -> None: ...
    def backward_transform(self) -> None: ...
