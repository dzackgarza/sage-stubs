from collections.abc import Mapping, Sequence
from typing import Self

from sage.modules.free_module_element import FreeModuleElement_generic_sparse
from sage.structure.parent import ElementConstructorInput
from sage.symbolic.expression import Expression


class Vector_symbolic_sparse(FreeModuleElement_generic_sparse[Expression]):
    def __init__(
        self,
        parent: object,
        entries: Mapping[int, Expression | ElementConstructorInput]
        | Sequence[Expression | ElementConstructorInput] = ...,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def dict(self, copy: bool = ...) -> dict[int, Expression]: ...
    def dot_product(self, right: Vector_symbolic_sparse) -> Expression: ...
    inner_product = dot_product
    def pairwise_product(self, right: Vector_symbolic_sparse) -> Self: ...
    def simplify(self, algorithm: str | None = ...) -> Self: ...
    def expand(self) -> Self: ...
    def factor(self) -> Self: ...
    def subs(
        self,
        substitutions: Mapping[object, ElementConstructorInput] | None = ...,
        **kwds: ElementConstructorInput,
    ) -> Self: ...
    substitute = subs
    def derivative(self, *args: object) -> Self: ...
    diff = derivative
    def dense_vector(self) -> Vector_symbolic_dense: ...


from sage.modules.vector_symbolic_dense import Vector_symbolic_dense
