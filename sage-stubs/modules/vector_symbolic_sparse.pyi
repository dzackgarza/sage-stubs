from collections.abc import Callable
from typing import Protocol, Self

from sage.modules.free_module_element import FreeModuleElement_generic_sparse
from sage.symbolic.expression import Expression, SymbolicInput


class SparseSymbolicVectorMethod(Protocol):
    def __call__(
        self,
        vector: Vector_symbolic_sparse,
        *args: SymbolicInput,
        **kwds: SymbolicInput,
    ) -> Vector_symbolic_sparse: ...


def apply_map(
    phi: Callable[..., Expression],
) -> SparseSymbolicVectorMethod: ...


class Vector_symbolic_sparse(
    FreeModuleElement_generic_sparse[Expression]
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
