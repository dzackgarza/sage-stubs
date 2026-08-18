from collections.abc import Mapping, Sequence
from typing import Self

from sage.modules.free_module_element import FreeModuleElement_generic_sparse
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.parent import ElementConstructorInput


class Vector_rational_sparse(FreeModuleElement_generic_sparse[Rational]):
    def __init__(
        self,
        parent: object,
        entries: Mapping[int, Rational | ElementConstructorInput]
        | Sequence[Rational | ElementConstructorInput] = ...,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def dict(self, copy: bool = ...) -> dict[int, Rational]: ...
    def denominator(self) -> Integer: ...
    def dot_product(self, right: Vector_rational_sparse) -> Rational: ...
    inner_product = dot_product
    def pairwise_product(self, right: Vector_rational_sparse) -> Self: ...
    def dense_vector(self) -> Vector_rational_dense: ...


from sage.modules.vector_rational_dense import Vector_rational_dense
