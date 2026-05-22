from typing import Literal, overload
from sage.rings.integer import Integer

@overload
def factor_using_pari(
    n: Integer | int,
    int_: Literal[True],
    debug_level: int = 0,
    proof: bool | None = None,
) -> list[tuple[int, int]]: ...

@overload
def factor_using_pari(
    n: Integer | int,
    int_: Literal[False] = False,
    debug_level: int = 0,
    proof: bool | None = None,
) -> list[tuple[Integer, int]]: ...

@overload
def factor_using_pari(
    n: Integer | int,
    int_: bool = False,
    debug_level: int = 0,
    proof: bool | None = None,
) -> list[tuple[Integer | int, int]]: ...
