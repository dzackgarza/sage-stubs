from sage.plot.graphics import Graphics
from sage.rings.integer import Integer
from sage.symbolic.function import BuiltinFunction, FunctionArgument, FunctionKeyword, FunctionResult


class PrimePi(BuiltinFunction):
    def __init__(self) -> None: ...
    def __call__(
        self,
        *args: FunctionArgument,
        coerce: bool = True,
        hold: bool = False,
    ) -> FunctionResult: ...
    def plot(
        self,
        xmin: float = 0,
        xmax: float = 100,
        vertical_lines: bool = True,
        **kwds: FunctionKeyword,
    ) -> Graphics: ...


prime_pi: PrimePi

def legendre_phi(x: int | Integer, a: int | Integer) -> Integer: ...
partial_sieve_function = legendre_phi
