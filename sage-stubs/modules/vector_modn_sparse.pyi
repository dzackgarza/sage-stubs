from collections.abc import Mapping, Sequence
from typing import Self

from sage.modules.free_module_element import FreeModuleElement_generic_sparse
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.structure.parent import ElementConstructorInput


class Vector_modn_sparse(
    FreeModuleElement_generic_sparse[IntegerMod_abstract]
):
    def __init__(
        self,
        parent: object,
        entries: Mapping[int, IntegerMod_abstract | ElementConstructorInput]
        | Sequence[IntegerMod_abstract | ElementConstructorInput] = ...,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def dict(self, copy: bool = ...) -> dict[int, IntegerMod_abstract]: ...
    def dot_product(self, right: Vector_modn_sparse) -> IntegerMod_abstract: ...
    inner_product = dot_product
    def pairwise_product(self, right: Vector_modn_sparse) -> Self: ...
    def dense_vector(self) -> Vector_modn_dense: ...


from sage.modules.vector_modn_dense import Vector_modn_dense
