from collections.abc import Callable, Sequence
from typing import Self

from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.structure.element import ElementConstructorInput

class Vector_mod2_dense(FreeModuleElement[IntegerMod_abstract]):
    def __init__(
        self,
        parent: FreeModule_generic[IntegerMod_abstract],
        x: Sequence[ElementConstructorInput] | int,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def _richcmp_(
        self,
        right: Vector_mod2_dense,
        op: int,
    ) -> bool: ...
    def _add_(self, right: Vector_mod2_dense) -> Self: ...
    def _sub_(self, right: Vector_mod2_dense) -> Self: ...
    def hamming_weight(self) -> int: ...
    def _dot_product_(
        self,
        right: Vector_mod2_dense,
    ) -> IntegerMod_abstract: ...
    def _pairwise_product_(
        self,
        right: Vector_mod2_dense,
    ) -> Self: ...
    def _lmul_(self, left: IntegerMod_abstract) -> Self: ...
    def _neg_(self) -> Self: ...
    def list(self, copy: bool = ...) -> list[IntegerMod_abstract]: ...
    def __reduce__(
        self,
    ) -> tuple[
        Callable[..., Vector_mod2_dense],
        tuple[
            FreeModule_generic[IntegerMod_abstract],
            list[IntegerMod_abstract],
            int,
            bool,
        ],
    ]: ...

def unpickle_v0(
    parent: FreeModule_generic[IntegerMod_abstract],
    entries: Sequence[ElementConstructorInput],
    degree: int,
    immutable: bool,
) -> Vector_mod2_dense: ...
