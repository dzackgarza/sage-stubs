from sage.rings.power_series_ring_element import PowerSeries
from sage.rings.real_mpfr import RealField_class, RealNumber
from sage.symbolic.function import BuiltinFunction, FunctionArgument, FunctionKeyword, FunctionResult, GinacFunction


class Function_zeta(GinacFunction):
    def __init__(self) -> None: ...
class Function_stieltjes(GinacFunction):
    def __init__(self) -> None: ...
class Function_HurwitzZeta(BuiltinFunction):
    def __init__(self) -> None: ...
class Function_zetaderiv(GinacFunction):
    def __init__(self) -> None: ...
class DickmanRho(BuiltinFunction):
    def __init__(self) -> None: ...
    def power_series(self, n: int, abs_prec: int) -> PowerSeries: ...
    def approximate(
        self,
        x: FunctionArgument,
        parent: RealField_class | None = None,
    ) -> RealNumber: ...


zeta: Function_zeta
stieltjes: Function_stieltjes
hurwitz_zeta_func: Function_HurwitzZeta
zetaderiv: Function_zetaderiv
dickman_rho: DickmanRho

def hurwitz_zeta(
    s: FunctionArgument,
    x: FunctionArgument,
    **kwargs: FunctionKeyword,
) -> FunctionResult: ...
def zeta_symmetric(s: FunctionArgument) -> FunctionResult: ...
