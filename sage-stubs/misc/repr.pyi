from collections.abc import Callable
from typing import TypeVar

_Coefficient = TypeVar("_Coefficient")
_Monomial = TypeVar("_Monomial")

def coeff_repr(self, is_latex: bool = ...) -> str: ...
def repr_lincomb(
    self,
    is_latex: bool = ...,
    scalar_mult: str = ...,
    strip_one: bool = ...,
    repr_monomial: Callable[[_Monomial], str] | None = ...,
    latex_scalar_mult: str | None = ...,
) -> str: ...
