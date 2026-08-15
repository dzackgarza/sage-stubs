from collections.abc import Callable, Iterable
from typing import TypeVar

_Coefficient = TypeVar("_Coefficient")
_Monomial = TypeVar("_Monomial")

def coeff_repr(c: object, is_latex: bool = ...) -> str: ...
def repr_lincomb(
    terms: Iterable[tuple[_Monomial, _Coefficient]],
    is_latex: bool = ...,
    scalar_mult: str = ...,
    strip_one: bool = ...,
    repr_monomial: Callable[[_Monomial], str] | None = ...,
    latex_scalar_mult: str | None = ...,
) -> str: ...
