from collections.abc import Callable
from typing import Self

from sage.modules.free_module_element import FreeModuleElement_generic_dense
from sage.symbolic.expression import Expression, SymbolicInput


def apply_map(
    phi: Callable[..., Expression],
) -> Callable[..., Vector_symbolic_dense]: ...


class Vector_symbolic_dense(
    FreeModuleElement_generic_dense[Expression]
):
    def simplify(
        self,
        *args: SymbolicInput,
        **kwds: SymbolicInput,
    ) -> Self: ...
    def simplify_factorial(
        self,
        *args: SymbolicInput,
        **kwds: SymbolicInput,
    ) -> Self: ...
    def simplify_log(
        self,
        *args: SymbolicInput,
        **kwds: SymbolicInput,
    ) -> Self: ...
    def simplify_rational(
        self,
        *args: SymbolicInput,
        **kwds: SymbolicInput,
    ) -> Self: ...
    def simplify_trig(
        self,
        *args: SymbolicInput,
        **kwds: SymbolicInput,
    ) -> Self: ...
    def simplify_full(
        self,
        *args: SymbolicInput,
        **kwds: SymbolicInput,
    ) -> Self: ...
    def trig_expand(
        self,
        *args: SymbolicInput,
        **kwds: SymbolicInput,
    ) -> Self: ...
    def canonicalize_radical(
        self,
        *args: SymbolicInput,
        **kwds: SymbolicInput,
    ) -> Self: ...
    def trig_reduce(
        self,
        *args: SymbolicInput,
        **kwds: SymbolicInput,
    ) -> Self: ...
