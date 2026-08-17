from typing import Literal, overload

from sage.rings.ring import Ring
from sage.structure.parent import Parent
from sage.symbolic.expression import Expression


class SymbolicSeries:
    def __init__(self, SR: Parent[Expression]) -> None: ...
    def is_terminating_series(self) -> bool: ...
    def truncate(self) -> Expression: ...
    def default_variable(self) -> Expression: ...
    @overload
    def coefficients(
        self,
        x: Expression | None = None,
        sparse: Literal[True] = True,
    ) -> list[tuple[Expression, int]]: ...
    @overload
    def coefficients(
        self,
        x: Expression | None,
        sparse: Literal[False],
    ) -> list[Expression]: ...
    def power_series(self, base_ring: Ring) -> Parent: ...
