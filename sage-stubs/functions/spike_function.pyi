from collections.abc import Iterable

from sage.modules.free_module_element import FreeModuleElement
from sage.plot.graphics import Graphics
from sage.rings.real_double import RealDoubleElement
from sage.structure.sage_object import SageObject


type Spike = tuple[float, float]


class SpikeFunction(SageObject):
    support: list[float]
    height: list[float]
    eps: float
    def __init__(self, v: Iterable[Spike], eps: float = 1e-7) -> None: ...
    def __repr__(self) -> str: ...
    def __call__(self, x: float) -> float: ...
    def plot_fft_abs(
        self,
        samples: int = 2**12,
        xmin: float | None = None,
        xmax: float | None = None,
        **kwds: float | int | str | bool,
    ) -> Graphics: ...
    def plot_fft_arg(
        self,
        samples: int = 2**12,
        xmin: float | None = None,
        xmax: float | None = None,
        **kwds: float | int | str | bool,
    ) -> Graphics: ...
    def vector(
        self,
        samples: int = 2**16,
        xmin: float | None = None,
        xmax: float | None = None,
    ) -> FreeModuleElement[RealDoubleElement]: ...
    def plot(
        self,
        xmin: float | None = None,
        xmax: float | None = None,
        **kwds: float | int | str | bool,
    ) -> Graphics: ...


spike_function: type[SpikeFunction]
