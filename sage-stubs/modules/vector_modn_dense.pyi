from collections.abc import Sequence
from typing import Self

from sage.modules.free_module_element import FreeModuleElement_generic_dense
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.structure.parent import ElementConstructorInput


class Vector_modn_dense(
    FreeModuleElement_generic_dense[IntegerMod_abstract]
):
    def __init__(
        self,
        parent: object,
        entries: Sequence[IntegerMod_abstract | ElementConstructorInput] = ...,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def list(self, copy: bool = ...) -> list[IntegerMod_abstract]: ...
    def dot_product(self, right: Vector_modn_dense) -> IntegerMod_abstract: ...
    inner_product = dot_product
    def pairwise_product(self, right: Vector_modn_dense) -> Self: ...
