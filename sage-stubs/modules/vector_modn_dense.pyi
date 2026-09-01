from collections.abc import Callable, Sequence
from typing import Self

from sage.modules.free_module import FreeModule_generic, ModuleRank
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.finite_rings.integer_mod import (
    IntegerMod_abstract,
    IntegerMod_int,
    IntegerMod_int64,
)
from sage.rings.integer import Integer
from sage.structure.parent import ElementConstructorInput

MAX_MODULUS: int

type NativeIntegerMod = IntegerMod_int | IntegerMod_int64


class Vector_modn_dense(FreeModuleElement[IntegerMod_abstract]):
    def __init__(
        self,
        parent: FreeModule_generic[IntegerMod_abstract],
        x: (
            Sequence[ElementConstructorInput]
            | int
            | Integer
            | IntegerMod_abstract
        ),
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def _richcmp_(
        self,
        right: FreeModuleElement[IntegerMod_abstract],
        op: int,
    ) -> bool: ...
    def __reduce__(
        self,
    ) -> tuple[
        Callable[..., Vector_modn_dense],
        tuple[
            FreeModule_generic[IntegerMod_abstract],
            list[IntegerMod_abstract],
            int,
            int,
            bool,
        ],
    ]: ...
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def _dot_product_(self, right: Self) -> NativeIntegerMod: ...
    def _pairwise_product_(self, right: Self) -> Self: ...
    def _lmul_(self, left: IntegerMod_abstract) -> Self: ...
    def _neg_(self) -> Self: ...


def unpickle_v0(
    parent: FreeModule_generic[IntegerMod_abstract],
    entries: Sequence[ElementConstructorInput],
    degree: ModuleRank,
    p: int,
) -> Vector_modn_dense: ...
def unpickle_v1(
    parent: FreeModule_generic[IntegerMod_abstract],
    entries: Sequence[ElementConstructorInput],
    degree: ModuleRank,
    p: int,
    immutable: bool,
) -> Vector_modn_dense: ...
