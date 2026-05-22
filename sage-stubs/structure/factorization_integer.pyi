from collections.abc import Callable

from sage.rings.integer import Integer
from sage.structure.factorization import Factorization

class IntegerFactorization(Factorization):
    def __init__(
        self,
        x: list[tuple[Integer, int]],
        unit: Integer | None = None,
        cr: bool = False,
        sort: bool = True,
        simplify: bool = True,
        unsafe: bool = False,
    ) -> None: ...
    def __sort__(
        self, key: Callable[[tuple[Integer, int]], int] | None = None
    ) -> None: ...
    def __floordiv__(
        self, other: Integer | IntegerFactorization | Factorization
    ) -> Factorization | Integer: ...
