from typing import Literal

from sage.libs.gsl.array import GSLDoubleArray
from sage.plot.graphics import Graphics


type WaveletType = Literal[
    "daubechies",
    "daubechies_centered",
    "haar",
    "haar_centered",
    "bspline",
    "bspline_centered",
]
type PlotOption = bool | int | float | str | tuple[float, float, float] | None


def WaveletTransform(
    n: int,
    wavelet_type: WaveletType,
    wavelet_k: int,
) -> DiscreteWaveletTransform: ...
DWT = WaveletTransform


class DiscreteWaveletTransform(GSLDoubleArray):
    def __init__(
        self,
        n: int,
        stride: int,
        wavelet_type: WaveletType,
        wavelet_k: int,
    ) -> None: ...
    def forward_transform(self) -> None: ...
    def backward_transform(self) -> None: ...
    def plot(
        self,
        xmin: int | None = None,
        xmax: int | None = None,
        **args: PlotOption,
    ) -> Graphics: ...


def is2pow(n: int) -> bool: ...
